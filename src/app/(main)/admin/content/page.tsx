"use client";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { Suspense, useEffect, useMemo, useState } from "react";
import { ArrowLeft, Download, RotateCcw, Search } from "lucide-react";
import { PATTERNS, ROOTS, SALAH, STRUCTURES, TEXTS, WORDS, teachOf, type Line } from "@/lib/course";
import { getValue, originalValue, revertOverride, saveOverride, useContent, type Path } from "@/lib/overrides";
import { useAuth } from "@/lib/auth";
import { useScript } from "@/lib/script";

type Tab = "words" | "grammar" | "sentences" | "roots" | "texts";
const TABS: [Tab, string][] = [["words", "Words"], ["grammar", "Grammar"], ["sentences", "Sentence patterns"], ["roots", "Roots"], ["texts", "Texts & salah"]];

/** One editable text. Saves to Supabase; everyone sees the change on their next visit. */
function Field({ path, label, long = false }: { path: Path; label: string; long?: boolean }) {
  const k = JSON.stringify(path);
  const edited = useContent((s) => k in s.edits);
  const version = useContent((s) => s.version);
  const current = getValue(path);
  const [val, setVal] = useState(current);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");
  useEffect(() => { setVal(getValue(path)); }, [k, version]); // eslint-disable-line react-hooks/exhaustive-deps
  const dirty = val !== current;
  const run = async (f: () => Promise<string | null>) => { setBusy(true); setErr((await f()) ?? ""); setBusy(false); };
  const isBn = label.includes("বাংলা") || label.endsWith("(bn)");
  return (
    <label className="block">
      <span className="mb-0.5 flex items-center gap-2 text-[12px] font-extrabold uppercase tracking-wider text-muted">
        {label}
        {edited && <span className="rounded-full bg-gold-light px-1.5 text-[10px] text-gold-dark">edited</span>}
        {edited && !dirty && (
          <button type="button" onClick={() => run(() => revertOverride(path))} className="ml-auto inline-flex items-center gap-1 normal-case text-sky" title={`Original: ${originalValue(path)}`}>
            <RotateCcw size={12} /> original
          </button>
        )}
      </span>
      <textarea dir="auto" value={val} onChange={(e) => setVal(e.target.value)} rows={long ? Math.min(8, Math.max(2, Math.ceil(val.length / 60))) : 1}
        className={`w-full resize-y rounded-xl border-2 bg-white px-3 py-2 text-[15px] outline-none focus:border-emerald ${dirty ? "border-gold" : "border-line"} ${isBn ? "bn" : ""}`} />
      {dirty && (
        <span className="mt-1 flex gap-2">
          <button type="button" disabled={busy} onClick={() => run(() => saveOverride(path, val))} className="btn btn-primary px-3 py-1 text-sm">{busy ? "Saving…" : "Save"}</button>
          <button type="button" onClick={() => setVal(current)} className="btn btn-ghost px-3 py-1 text-sm">Cancel</button>
        </span>
      )}
      {err && <span className="mt-1 block text-sm text-coral-dark">{err}</span>}
    </label>
  );
}
const Pair = ({ base, en, bn, long }: { base: Path; en: string | number; bn: string | number; long?: boolean }) => (
  <div className="grid gap-2 sm:grid-cols-2">
    <Field path={[...base, en]} label="English" long={long} />
    <Field path={[...base, bn]} label="বাংলা" long={long} />
  </div>
);

function Item({ title, ar, children, open }: { title: string; ar?: string; children: React.ReactNode; open?: boolean }) {
  const { A } = useScript();
  return (
    <details className="card group p-3" open={open}>
      <summary className="flex cursor-pointer list-none items-center gap-3">
        {ar && <span className="ar text-2xl">{A(ar)}</span>}
        <span className="flex-1 font-bold">{title}</span>
        <span className="text-muted group-open:rotate-90">›</span>
      </summary>
      <div className="mt-3 space-y-3 border-t-2 border-line pt-3">{children}</div>
    </details>
  );
}

/** teaching pages + check questions of a grammar card ("p:al") or sentence pattern ("s:is") */
function Teach({ refId }: { refId: string }) {
  const t = teachOf(refId);
  return (
    <>
      {t.pages.map((pg, i) => (
        <div key={i} className="rounded-xl bg-sand/60 p-3">
          <div className="mb-2 text-sm font-black">Page {i + 1}</div>
          <Pair base={["page", refId, i]} en="t_en" bn="t_bn" />
          <div className="mt-2"><Pair base={["page", refId, i]} en="x_en" bn="x_bn" long /></div>
          {(["vs", "ex"] as const).map((kind) => pg[kind].map((x, j) => (
            <div key={kind + j} className="mt-2">
              <div className="ar text-xl">{x.ar}</div>
              <Pair base={["pageex", refId, i, kind, j]} en="en" bn="bn" />
            </div>
          )))}
        </div>
      ))}
      {t.checks.map((c, n) => (
        <div key={"c" + n} className="rounded-xl bg-emerald-light/50 p-3">
          <div className="mb-2 text-sm font-black">Check question {n + 1} <span className="font-normal text-muted">(first option is the right answer)</span></div>
          <Pair base={["check", refId, n]} en="q_en" bn="q_bn" />
          {c.options.map((o, j) => typeof o === "string"
            ? <div key={j} className="ar text-xl">{j + 1}. {o}</div>
            : <div key={j} className="mt-1"><Pair base={["checkopt", refId, n, j]} en="en" bn="bn" /></div>)}
          <div className="mt-2"><Pair base={["check", refId, n]} en="why_en" bn="why_bn" long /></div>
        </div>
      ))}
    </>
  );
}

function LineFields({ line }: { line: Line }) {
  return (
    <div className="rounded-xl bg-sand/60 p-3">
      <div dir="rtl" className="ar text-2xl">{line.ar}</div>
      <div className="mt-2"><Pair base={["line", line.id]} en="en" bn="bn" long /></div>
      <details className="mt-2">
        <summary className="cursor-pointer text-sm font-bold text-sky">Word meanings</summary>
        <div className="mt-2 space-y-2">
          {line.tokens.map((t, i) => (
            <div key={i} className="grid items-center gap-2 sm:grid-cols-[6rem_1fr_1fr]">
              <span className="ar text-xl">{t.ar}</span>
              <Field path={["tok", line.id, i, "en"]} label="English" />
              <Field path={["tok", line.id, i, "bn"]} label="বাংলা" />
            </div>
          ))}
        </div>
      </details>
    </div>
  );
}

function Editor() {
  const { isAdmin, demo } = useAuth();
  const params = useSearchParams();
  const [tab, setTab] = useState<Tab>((params.get("tab") as Tab) || "words");
  const [q, setQ] = useState(params.get("q") || "");
  const edits = useContent((s) => s.edits);
  const match = (...xs: (string | undefined)[]) => !q || xs.some((x) => x?.toLowerCase().includes(q.toLowerCase()));

  const words = useMemo(() => Object.values(WORDS).filter((w) => match(w.key, w.ar, w.en, w.bn)).slice(0, 60), [q]); // eslint-disable-line react-hooks/exhaustive-deps
  const download = () => {
    const blob = new Blob([JSON.stringify(Object.entries(edits).map(([p, v]) => ({ path: JSON.parse(p), value: v })), null, 1)], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `content-edits-${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
  };

  if (!isAdmin) return <div className="card p-6 text-center">Only the superadmin can edit content. <Link className="text-emerald underline" href="/profile">Back</Link></div>;
  return (
    <div>
      <Link href="/admin" className="mb-3 inline-flex items-center gap-1 font-bold text-muted"><ArrowLeft size={18} /> Admin</Link>
      <h1 className="text-2xl font-black">Edit content</h1>
      <p className="mt-1 text-sm text-muted">Fix any meaning, explanation or question. Saved changes reach every learner the next time they open the app. “original” brings back the built-in text.</p>
      {demo && <div className="card mt-3 p-3 text-sm">Demo mode: connect Supabase to save edits.</div>}
      <div className="mt-3 flex items-center gap-2 text-sm">
        <span className="font-bold">{Object.keys(edits).length} edits</span>
        <button onClick={download} className="btn btn-ghost ml-auto inline-flex items-center gap-1 px-3 py-1 text-sm"><Download size={14} /> Download all edits</button>
      </div>
      <div className="mt-3 flex flex-wrap gap-1.5">
        {TABS.map(([id, label]) => (
          <button key={id} onClick={() => setTab(id)} className={`rounded-full px-3 py-1.5 text-sm font-extrabold ${tab === id ? "bg-emerald text-white" : "bg-sand text-muted"}`}>{label}</button>
        ))}
      </div>
      <div className="relative mt-3">
        <Search size={16} className="absolute left-3 top-3 text-muted" />
        <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search (Arabic, English or Bangla)" className="w-full rounded-xl border-2 border-line bg-white py-2 pl-9 pr-3 outline-none focus:border-emerald" />
      </div>

      <div className="mt-4 space-y-2">
        {tab === "words" && words.map((w) => (
          <Item key={w.key} title={`${w.en}${w.bn ? " · " + w.bn : ""}`} ar={w.ar.split(" / ")[0]} open={!!q && words.length === 1}>
            <Pair base={["word", w.key]} en="en" bn="bn" />
            <Field path={["word", w.key, "tip"]} label="Tip (English)" long />
            <div className="grid gap-2 sm:grid-cols-3">
              <Field path={["word", w.key, "cog.en"]} label="Related: English" />
              <Field path={["word", w.key, "cog.bn"]} label="Related: বাংলা" />
              <Field path={["word", w.key, "cog.hi"]} label="Related: Hindi/Urdu" />
            </div>
            <Field path={["word", w.key, "emoji"]} label="Emoji" />
          </Item>
        ))}
        {tab === "grammar" && Object.values(PATTERNS).filter((p) => match(p.id, p.ar, p.en, p.bn, p.expl_en, p.expl_bn)).map((p) => (
          <Item key={p.id} title={`${p.en} · ${p.bn}`} ar={p.ar.split(" / ")[0]}>
            <Pair base={["pattern", p.id]} en="en" bn="bn" />
            <Pair base={["pattern", p.id]} en="expl_en" bn="expl_bn" long />
            <Teach refId={"p:" + p.id} />
          </Item>
        ))}
        {tab === "sentences" && Object.values(STRUCTURES).filter((s) => match(s.id, s.en, s.bn, s.expl_en, s.expl_bn)).map((s) => (
          <Item key={s.id} title={`${s.en} · ${s.bn}`}>
            <Pair base={["struct", s.id]} en="en" bn="bn" />
            <Pair base={["struct", s.id]} en="expl_en" bn="expl_bn" long />
            <Teach refId={"s:" + s.id} />
            <div className="text-sm font-black">Everyday sentences</div>
            {s.everyday.map((l) => <LineFields key={l.id} line={l} />)}
          </Item>
        ))}
        {tab === "roots" && Object.entries(ROOTS).filter(([r, x]) => match(r, x.idea_en, x.idea_bn, x.story_en, x.story_bn)).map(([r, x]) => (
          <Item key={r} title={`${r.split("").join(" ")} = ${x.idea_en}`}>
            <Pair base={["root", r]} en="idea_en" bn="idea_bn" />
            <Pair base={["root", r]} en="story_en" bn="story_bn" long />
          </Item>
        ))}
        {tab === "texts" && (
          <>
            {TEXTS.filter((t) => match(t.en, t.bn, ...t.lines.flatMap((l) => [l.en, l.bn, l.ar]))).map((t) => (
              <Item key={t.id} title={t.en} ar={t.ar}>{t.lines.map((l) => <LineFields key={l.id} line={l} />)}</Item>
            ))}
            {SALAH.filter((g) => match(g.en, g.bn, ...g.lines.flatMap((l) => [l.en, l.bn, l.ar]))).map((g) => (
              <Item key={"s" + g.id} title={`Salah: ${g.en}`}>{g.lines.map((l) => <LineFields key={l.id} line={l} />)}</Item>
            ))}
          </>
        )}
      </div>
    </div>
  );
}

export default function ContentEditorPage() {
  return <Suspense><Editor /></Suspense>;
}
