"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import { KIND_LABEL, PATTERNS, ROOTS, RULES, STRUCTURES, WORDS, linesWithWord, meaning, teachOf, type FamilyMember, type Line, type TeachPage, type Token } from "@/lib/course";
import { lineById, type Step } from "@/lib/exercises";
import { playLine, playVerse, sfx } from "@/lib/audio";
import { useT } from "@/lib/i18n";
import { useProgress } from "@/lib/store";
import { useScript } from "@/lib/script";
import { Volume2 } from "lucide-react";
import { Emoji } from "../ui";
import { ArabicLine } from "../ArabicLine";

export type Evaluate = () => { correct: boolean; answer: React.ReactNode; why?: React.ReactNode };
export interface Pager { at: number; total: number; next: () => void }
export interface ExProps<K extends Step["kind"]> {
  step: Extract<Step, { kind: K }>;
  setEvaluate: (fn: Evaluate | null) => void; // graded steps: set when the user has a selection
  locked: boolean; // after checking
  onDone: (correct: boolean) => void; // for self-completing steps (match)
  setPager?: (p: Pager | null) => void; // steps made of swipeable pages
}

const firstForm = (ar: string) => ar.split(" / ")[0];
const CLEAN = /[ۖ-ۭ-]/g;
/** forms in the learner's script; C() drops pause / verse-end marks */
function useForm() {
  const { A, T } = useScript();
  return { F: (ar: string) => A(firstForm(ar)), A, T, C: (s: string) => A(s).replace(CLEAN, "").trim() };
}
const Title = ({ children }: { children: React.ReactNode }) => {
  const { lang } = useT();
  return <h2 className={`mb-5 text-2xl font-black ${lang === "bn" ? "bn" : ""}`}>{children}</h2>;
};
const Badge = ({ color, children }: { color: string; children: React.ReactNode }) => (
  <div className={`mb-3 inline-block rounded-full px-3 py-1 text-xs font-extrabold uppercase tracking-wider ${color}`}>{children}</div>
);
const Box = ({ title, children, tone = "plain" }: { title?: string; children: React.ReactNode; tone?: "plain" | "gold" | "sky" }) => (
  <div className={`rounded-2xl p-3 ${tone === "gold" ? "bg-gold-light" : tone === "sky" ? "bg-sky-light" : "border-2 border-dashed border-line"}`}>
    {title && <div className={`mb-1.5 text-xs font-extrabold uppercase tracking-wider ${tone === "gold" ? "text-gold-dark" : tone === "sky" ? "text-sky" : "text-muted"}`}>{title}</div>}
    {children}
  </div>
);

const POS_LABEL: Record<string, [string, string]> = {
  noun: ["a thing or person", "বস্তু বা ব্যক্তি"], verb: ["an action", "একটি কাজ"], adj: ["describes something", "বর্ণনা করে"],
  particle: ["a small linking word", "ছোট সংযোগ শব্দ"], pron: ["stands for a person", "ব্যক্তির বদলে বসে"], name: ["a name", "একটি নাম"],
  dem: ["points at something", "কিছু নির্দেশ করে"], rel: ["“who / which”", "“যে / যা”"],
};

function Option({ selected, state, onClick, children, className = "" }: {
  selected: boolean; state?: "right" | "wrong" | null; onClick: () => void; children: React.ReactNode; className?: string;
}) {
  const cls = state === "right" ? "border-emerald bg-emerald-light shadow-[0_3px_0_var(--color-emerald)]"
    : state === "wrong" ? "border-coral bg-coral-light shadow-[0_3px_0_var(--color-coral)] animate-shake"
    : selected ? "border-sky bg-sky-light shadow-[0_3px_0_var(--color-sky)]" : "";
  return <button onClick={onClick} className={`chip p-3 text-left ${cls} ${className}`}>{children}</button>;
}

/** "word = base + piece" rows explaining how a form is built from patterns */
function PatternChips({ pats }: { pats: string[] }) {
  const { lang } = useT();
  const { A } = useForm();
  const list = pats.filter((p) => PATTERNS[p]);
  if (!list.length) return null;
  return (
    <div className="flex flex-wrap gap-2">
      {list.map((p) => (
        <span key={p} className={`rounded-full bg-white px-3 py-1 text-[16px] font-bold ${lang === "bn" ? "bn" : ""}`}>
          <span className="ar text-2xl text-emerald">{A(PATTERNS[p].ar)}</span> = {lang === "bn" ? PATTERNS[p].bn : PATTERNS[p].en}
        </span>
      ))}
    </div>
  );
}

// ---------------- teaching building blocks ----------------
const AR_RUN = /[؀-ۿݐ-ݿࢠ-ࣿ]+(?:[  ]+[؀-ۿݐ-ݿࢠ-ࣿ]+)*/g;
/** Text with Arabic inside it: the Arabic is shown in the Quran font, large enough to read every haraka. */
export function Rich({ text, className = "" }: { text: string; className?: string }) {
  const { A } = useScript();
  const parts: React.ReactNode[] = [];
  let last = 0;
  for (const m of text.matchAll(AR_RUN)) {
    if (m.index! > last) parts.push(text.slice(last, m.index));
    parts.push(<bdi key={m.index} className={`ar ar-in ${className}`}>{A(m[0])}</bdi>);
    last = m.index! + m[0].length;
  }
  if (last < text.length) parts.push(text.slice(last));
  return <>{parts}</>;
}

/** Swipeable pages (swipe, tap the dots, or the footer's "Next" button via setPager). */
function Pages({ pages, setPager }: { pages: React.ReactNode[]; setPager?: (p: Pager | null) => void }) {
  const [at, setAt] = useState(0);
  const [h, setH] = useState<number | undefined>();
  const refs = useRef<(HTMLDivElement | null)[]>([]);
  const touch = useRef<{ x: number; y: number } | null>(null);
  const total = pages.length;
  const go = (i: number) => setAt(Math.max(0, Math.min(total - 1, i)));
  useEffect(() => {
    setPager?.({ at, total, next: () => go(at + 1) });
    if (at > 0) window.scrollTo({ top: 0, behavior: "smooth" });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [at, total]);
  useEffect(() => () => setPager?.(null), [setPager]);
  // the frame is as tall as the page being shown
  useEffect(() => {
    const el = refs.current[at];
    if (!el) return;
    const ro = new ResizeObserver(() => setH(el.offsetHeight));
    ro.observe(el);
    return () => ro.disconnect();
  }, [at]);
  return (
    <div>
      {total > 1 && (
        <div className="mb-3 flex items-center justify-center gap-1.5" data-testid="page-dots">
          {pages.map((_, i) => (
            <button key={i} onClick={() => go(i)} aria-label={`page ${i + 1}`}
              className={`h-2.5 rounded-full transition-all ${i === at ? "w-7 bg-emerald" : "w-2.5 bg-line"}`} />
          ))}
        </div>
      )}
      <div className="overflow-hidden transition-[height] duration-300" style={{ height: h }}
        onTouchStart={(e) => (touch.current = { x: e.touches[0].clientX, y: e.touches[0].clientY })}
        onTouchEnd={(e) => {
          const t0 = touch.current; touch.current = null;
          if (!t0) return;
          const dx = e.changedTouches[0].clientX - t0.x, dy = e.changedTouches[0].clientY - t0.y;
          if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) go(at + (dx < 0 ? 1 : -1));
        }}>
        <div className="flex items-start transition-transform duration-300 ease-out" style={{ transform: `translateX(-${at * 100}%)` }}>
          {pages.map((p, i) => (
            <div key={i} ref={(el) => { refs.current[i] = el; }} aria-hidden={i !== at} className="w-full shrink-0 px-1 pb-2">{p}</div>
          ))}
        </div>
      </div>
    </div>
  );
}

/** Arabic (big) next to / above its meaning */
function ExRow({ ar, text }: { ar: string; text: string }) {
  const { lang } = useT();
  const { C } = useForm();
  const long = ar.replace(/[^ء-يٱ-ۓ]/g, "").length > 9;
  return (
    <div className={`py-3 ${long ? "" : "flex items-center gap-4"}`}>
      <div dir="rtl" className={`ar text-3xl text-ink ${long ? "text-right" : "min-w-[38%] text-right"}`}>{C(ar)}</div>
      <div className={`text-[17px] font-semibold leading-snug ${long ? "mt-1" : "flex-1"} ${lang === "bn" ? "bn" : ""}`}><Rich text={text} /></div>
    </div>
  );
}

export function TeachCard({ page }: { page: TeachPage }) {
  const { lang } = useT();
  const { C } = useForm();
  const bn = lang === "bn" ? "bn" : "";
  const tx = (x: { en: string; bn: string }) => (lang === "bn" ? x.bn : x.en);
  return (
    <div className="card p-5">
      <h3 className={`text-[22px] font-black leading-tight ${bn}`}><Rich text={lang === "bn" ? page.t_bn : page.t_en} /></h3>
      <p className={`mt-3 text-[18px] leading-relaxed text-ink/90 ${bn}`}><Rich text={lang === "bn" ? page.x_bn : page.x_en} /></p>
      {page.vs.length > 0 && (
        <div className={`mt-4 grid gap-2 ${page.vs.length === 3 ? "grid-cols-3" : "grid-cols-2"}`}>
          {page.vs.map((v, i) => (
            <div key={i} className="flex flex-col items-center justify-center rounded-2xl border-2 border-line bg-sand/60 px-2 py-3 text-center">
              <div className={`ar ${page.vs.length === 3 || v.ar.length > 14 ? "text-3xl" : "text-4xl"} text-emerald-dark`}>{C(v.ar)}</div>
              <div className={`mt-1 text-[16px] font-bold leading-snug ${bn}`}><Rich text={tx(v)} /></div>
            </div>
          ))}
        </div>
      )}
      {page.ex.length > 0 && (
        <div className="mt-3 divide-y-2 divide-line">
          {page.ex.map((e, i) => <ExRow key={i} ar={e.ar} text={tx(e)} />)}
        </div>
      )}
    </div>
  );
}

/** one word from the same root: its form, meaning, and how its shape links it to the root */
export function FamilyRow({ f }: { f: FamilyMember }) {
  const { lang } = useT();
  const { T } = useForm();
  const fw = WORDS[f.key];
  const kind = f.kind && KIND_LABEL[f.kind];
  const gloss = fw ? meaning(fw, lang) : lang === "bn" && f.bn ? f.bn : f.gloss;
  return (
    <div className="flex items-center gap-4 py-3">
      <span dir="rtl" className="ar min-w-[34%] text-right text-3xl">{T({ ar: f.ex, ip: f.exIp }, true).replace(CLEAN, "")}</span>
      <div className={`flex-1 leading-snug ${lang === "bn" ? "bn" : ""}`}>
        <div className="text-[17px] font-bold">{gloss}</div>
        <div className="mt-0.5 flex flex-wrap items-center gap-1.5 text-[13px] text-muted">
          {kind && <span className="rounded-full bg-sky-light px-2 py-0.5 font-bold text-sky">{lang === "bn" ? kind[1] : kind[0]}</span>}
          <span>{f.count}×</span>
        </div>
      </div>
    </div>
  );
}

/** the root's core idea, how its words connect, and a few of them */
export function RootBox({ word, max = 3 }: { word: string; max?: number }) {
  const { lang } = useT();
  const w = WORDS[word];
  const info = ROOTS[w.root];
  const bn = lang === "bn" ? "bn" : "";
  const family = w.family.filter((f) => !f.self).slice(0, max);
  return (
    <div className="card p-5">
      <div className={`text-[13px] font-extrabold uppercase tracking-wider text-muted ${bn}`}>{lang === "bn" ? "মূল অক্ষর" : "Root letters"}</div>
      <div className="mt-1 flex flex-wrap items-baseline gap-x-3">
        <span dir="rtl" className="ar text-4xl text-emerald">{w.rootSpaced}</span>
        {info && <span className={`text-[20px] font-black ${bn}`}>= {lang === "bn" ? info.idea_bn : info.idea_en}</span>}
      </div>
      {info && <p className={`mt-3 text-[17px] leading-relaxed text-ink/90 ${bn}`}><Rich text={lang === "bn" ? info.story_bn : info.story_en} /></p>}
      {family.length > 0 && (
        <div className="mt-2 divide-y-2 divide-line border-t-2 border-line">
          {family.map((f) => <FamilyRow key={f.key} f={f} />)}
        </div>
      )}
    </div>
  );
}

// ---------------- New word ----------------
export function IntroEx({ step, setPager }: ExProps<"intro">) {
  const { t, lang } = useT();
  const { F, A, T } = useForm();
  const w = WORDS[step.word];
  const bn = lang === "bn" ? "bn" : "";
  const examples = useMemo(() => {
    const all = linesWithWord(step.word);
    const seen = new Set<string>();
    return all.filter(({ line }) => (seen.has(line.en) ? false : (seen.add(line.en), true))).slice(0, 3);
  }, [step.word]);
  const firstTok = examples[0]?.line.tokens[examples[0].index];
  const family = w.family.filter((f) => !f.self).slice(0, 3);
  useEffect(() => { useProgress.getState().learn([step.word]); }, [step.word]);
  const cogs = Object.entries(w.cog);
  const pos = POS_LABEL[w.pos];
  const understand = !!(firstTok?.pats.length || w.tip || w.count > 0);

  const page1 = (
    <div className="space-y-3">
      <Badge color="bg-plum/15 text-plum">✨ {t("newWord")}</Badge>
      <div className="card flex flex-col items-center p-5 text-center">
        <Emoji e={w.emoji} className="text-6xl" />
        <div className="ar mt-2 text-5xl text-ink">{F(w.ar)}</div>
        {w.ar.includes(" / ") && <div className="ar text-3xl text-muted">{A(w.ar.split(" / ")[1])}</div>}
        <div className={`mt-1 text-[26px] font-black text-emerald ${bn}`}>{meaning(w, lang)}</div>
        {pos && <div className={`mt-1 text-sm font-bold uppercase tracking-wider text-muted ${bn}`}>{lang === "bn" ? pos[1] : pos[0]}</div>}
      </div>
      {cogs.length > 0 && (
        <Box title={t("related")} tone="gold">
          {cogs.map(([l, v]) => (
            <div key={l} className="py-0.5 text-[17px]"><span className="mr-2 inline-block w-24 font-bold text-gold-dark">{l === "en" ? "English" : l === "bn" ? "বাংলা" : "Hindi/Urdu"}</span><span className={l === "bn" ? "bn" : ""}>{v}</span></div>
          ))}
        </Box>
      )}
    </div>
  );
  const page2 = (
    <div className="space-y-3">
      <Badge color="bg-sky-light text-sky">💡 {lang === "bn" ? "বুঝে নিন" : "Understand it"}</Badge>
      {understand && (
        <div className={`card space-y-4 p-5 text-[17px] leading-relaxed ${bn}`}>
          {firstTok && firstTok.pats.length > 0 && (
            <div>
              <div className="mb-2"><span className="ar text-3xl">{T(firstTok, true)}</span> {lang === "bn" ? "শব্দে আছে:" : "is built with:"}</div>
              <PatternChips pats={firstTok.pats} />
            </div>
          )}
          {w.tip && <div><Rich text={w.tip} /></div>}
          {w.count > 0 && (
            <div>
              📖 {lang === "bn" ? `কুরআনে ${w.count} বার এসেছে।` : `Appears ${w.count} times in the Quran.`}
              {w.root && <> {lang === "bn" ? "মূল অক্ষর" : "Root letters"} <bdi className="ar ar-in text-emerald">{w.rootSpaced}</bdi>.</>}
            </div>
          )}
        </div>
      )}
      {w.root && (ROOTS[w.root] || family.length > 0) && <RootBox word={step.word} />}
      {examples.length > 0 && (
        <Box title={lang === "bn" ? "উদাহরণ" : "Examples"}>
          <div className="space-y-3">
            {examples.map(({ line }) => <ArabicLine key={line.id} line={line} size="text-3xl" highlightKey={step.word} />)}
          </div>
        </Box>
      )}
    </div>
  );
  return <div className="animate-pop"><Pages pages={understand || examples.length || family.length ? [page1, page2] : [page1]} setPager={setPager} /></div>;
}

// ---------------- Pattern (a pinch of grammar) ----------------
export function PatternEx({ step, setPager }: ExProps<"pattern">) {
  const { t, lang } = useT();
  const { A, F, T } = useForm();
  const p = PATTERNS[step.pattern];
  const bn = lang === "bn" ? "bn" : "";
  useEffect(() => { useProgress.getState().learn(["p:" + step.pattern]); }, [step.pattern]);
  const hero = (
    <div className="space-y-3">
      <Badge color="bg-gold-light text-gold-dark">🧂 {t("newPattern")}</Badge>
      <div className="card p-6 text-center">
        <div dir="rtl" className="flex flex-wrap items-center justify-center gap-x-6">
          {p.ar.split(" / ").map((part, i) => (
            // a lone ending (ـٌ) gets a longer line to sit on, so the haraka is easy to see
            <span key={i} className="ar text-6xl text-emerald">{A(part).replace(/^ـ(?=[\u064B-\u0652])/, "ـــ")}</span>
          ))}
        </div>
        <div className={`mt-2 text-[26px] font-black ${bn}`}>{p.emoji} {lang === "bn" ? p.bn : p.en}</div>
        <p className={`mt-4 text-left text-[18px] leading-relaxed text-ink/90 ${bn}`}><Rich text={lang === "bn" ? p.expl_bn : p.expl_en} /></p>
      </div>
    </div>
  );
  const pages = (p.pages?.length ? p.pages : p.more_en ? [{ t_en: p.en, t_bn: p.bn, x_en: p.more_en, x_bn: p.more_bn ?? "", ex: [], vs: [] }] : [])
    .map((pg, i) => <TeachCard key={i} page={pg} />);
  const recite = p.examples.length > 0 && (
    <div className="card p-5">
      <h3 className={`text-[22px] font-black ${bn}`}>{lang === "bn" ? "যা আপনি পড়েন তাতে" : "In what you recite"}</h3>
      <div className="mt-2 divide-y-2 divide-line">
        {p.examples.slice(0, 4).map((e, i) => {
          const base = e.key ? WORDS[e.key] : undefined;
          return (
            <div key={i} className="flex items-center gap-4 py-3">
              <span className="ar min-w-[35%] text-right text-3xl">{T({ ar: e.ar, ip: e.ip }, true).replace(CLEAN, "")}</span>
              <div className={`flex-1 text-[17px] leading-snug ${bn}`}>
                <div className="font-bold">{lang === "bn" ? e.bn : e.en}</div>
                {base && <div className="text-muted"><bdi className="ar ar-in">{F(base.ar)}</bdi> ({meaning(base, lang)}) + <bdi className="ar ar-in text-emerald">{A(p.ar)}</bdi></div>}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
  const ac = p.across;
  const acrossWords = ac && ac.words.length > 0 && (
    <div className="card p-5">
      <h3 className={`text-[22px] font-black ${bn}`}>{lang === "bn" ? "পুরো কুরআনে" : "Across the Quran"}</h3>
      <p className={`mt-2 text-[17px] leading-relaxed text-ink/90 ${bn}`}>
        {lang === "bn" ? <>কুরআনে <b>{ac.count.toLocaleString("bn")}</b>টি শব্দে <bdi className="ar ar-in text-emerald">{A(p.ar)}</bdi> আছে। কয়েকটি:</>
          : <><bdi className="ar ar-in text-emerald">{A(p.ar)}</bdi> appears on <b>{ac.count.toLocaleString()}</b> words in the Quran. A few of them:</>}
      </p>
      <div className="mt-2 divide-y-2 divide-line">
        {ac.words.map((e, i) => {
          const base = e.key ? WORDS[e.key] : undefined;
          return (
            <div key={i} className="flex items-center gap-4 py-3">
              <span dir="rtl" className="ar min-w-[35%] text-right text-3xl">{T({ ar: e.ar, ip: e.ip }, true).replace(CLEAN, "")}</span>
              <div className={`flex-1 text-[17px] leading-snug ${bn}`}>
                <div className="font-bold">{lang === "bn" && e.bn ? e.bn : e.en}</div>
                {base && <div className="text-muted"><bdi className="ar ar-in">{F(base.ar)}</bdi> ({meaning(base, lang)}) + <bdi className="ar ar-in text-emerald">{A(p.ar)}</bdi></div>}
                <div className="text-[13px] text-muted">{e.ref}</div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
  const acrossVerses = ac && ac.verses.length > 0 && (
    <div className="space-y-3">
      <div className="card p-5">
        <h3 className={`text-[22px] font-black ${bn}`}>{lang === "bn" ? "আয়াতের ভেতরে" : "Inside a verse"}</h3>
        <p className={`mt-2 text-[17px] leading-relaxed text-ink/90 ${bn}`}>
          {lang === "bn" ? <>হলুদ শব্দে <bdi className="ar ar-in text-emerald">{A(p.ar)}</bdi> আছে। শব্দে চাপ দিলে অর্থ দেখাবে।</>
            : <>The yellow words carry <bdi className="ar ar-in text-emerald">{A(p.ar)}</bdi>. Tap any word for its meaning.</>}
        </p>
      </div>
      {ac.verses.map((v) => (
        <div key={v.id} className="card p-4">
          <div className="mb-1 text-[13px] font-bold text-muted">{v.ref}</div>
          <ArabicLine line={v} size="text-3xl" highlightPat={p.id} showGloss />
        </div>
      ))}
    </div>
  );
  const extra = [recite, acrossWords, acrossVerses].filter(Boolean) as React.ReactElement[];
  return <div className="animate-pop"><Pages pages={[hero, ...pages, ...extra]} setPager={setPager} /></div>;
}

// ---------------- MCQ ----------------
export function McqEx({ step, setEvaluate, locked }: ExProps<"mcq">) {
  const { t, lang } = useT();
  const [sel, setSel] = useState<string | null>(null);
  const [res, setRes] = useState<boolean | null>(null);
  const w = WORDS[step.word];
  const { F } = useForm();
  useEffect(() => {
    if (!sel) return setEvaluate(null);
    setEvaluate(() => {
      const ok = sel === step.word;
      setRes(ok);
      return { correct: ok, answer: step.mode === "mean2ar" ? <span className="ar text-2xl">{F(w.ar)}</span> : meaning(w, lang) };
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [sel, step.word, step.mode, lang]);
  const optState = (k: string) => (!locked || res === null ? null : k === step.word ? "right" : k === sel ? "wrong" : null);
  return (
    <div>
      {step.mode === "mean2ar" ? (
        <>
          <Title>{t("whichArabic")} “{meaning(w, lang)}”?</Title>
          <div className="mb-6 text-center"><Emoji e={w.emoji} className="text-6xl" /></div>
        </>
      ) : (
        <>
          <Title>{t("whatMeans")}</Title>
          <div className="ar mb-6 text-center text-5xl">{F(w.ar)}</div>
        </>
      )}
      <div className="grid grid-cols-2 gap-3">
        {step.options.map((k) => {
          const o = WORDS[k];
          return (
            <Option key={k} selected={sel === k} state={optState(k)} onClick={() => !locked && setSel(k)}
              className="flex min-h-24 flex-col items-center justify-center text-center">
              {step.mode === "mean2ar" ? (
                <span className="ar text-3xl">{F(o.ar)}</span>
              ) : (
                <>
                  <Emoji e={o.emoji} className="text-3xl" />
                  <span className={`mt-1 text-[15px] font-bold leading-tight ${lang === "bn" ? "bn" : ""}`}>{meaning(o, lang)}</span>
                </>
              )}
            </Option>
          );
        })}
      </div>
    </div>
  );
}

// ---------------- Pattern question ----------------
export function PatternQEx({ step, setEvaluate, locked }: ExProps<"patternq">) {
  const { t, lang } = useT();
  const [sel, setSel] = useState<number | null>(null);
  const [res, setRes] = useState<boolean | null>(null);
  const p = PATTERNS[step.pattern];
  const { A, T } = useForm();
  const gl = (x: Token) => (lang === "bn" && x.bn ? x.bn : x.en);
  useEffect(() => {
    if (sel === null) return setEvaluate(null);
    setEvaluate(() => {
      const ok = gl(step.options[sel]) === gl(step.token);
      setRes(ok);
      return { correct: ok, answer: gl(step.token) };
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [sel, lang]);
  return (
    <div>
      <Title>{t("whatMeans")}</Title>
      <div className="ar mb-2 text-center text-5xl">{T(step.token, true)}</div>
      <div className={`mb-5 text-center text-[17px] text-muted ${lang === "bn" ? "bn" : ""}`}>💡 <span className="ar text-2xl text-emerald">{A(p.ar)}</span> = {lang === "bn" ? p.bn : p.en}</div>
      <div className="flex flex-col gap-3">
        {step.options.map((o, i) => (
          <Option key={i} selected={sel === i} onClick={() => !locked && setSel(i)}
            state={!locked || res === null ? null : gl(o) === gl(step.token) ? "right" : i === sel ? "wrong" : null}>
            <span className={`font-bold ${lang === "bn" ? "bn" : ""}`}>{gl(o)}</span>
          </Option>
        ))}
      </div>
    </div>
  );
}

// ---------------- Spot the word ----------------
export function SpotEx({ step, setEvaluate, locked }: ExProps<"spot">) {
  const { t, lang } = useT();
  const line = lineById(step.lineId);
  const w = WORDS[step.word];
  const { T } = useForm();
  const [sel, setSel] = useState<number | null>(null);
  const [res, setRes] = useState<boolean | null>(null);
  useEffect(() => {
    if (sel === null) return setEvaluate(null);
    setEvaluate(() => {
      const ok = line.tokens[sel].key === step.word;
      setRes(ok);
      const right = line.tokens.find((x) => x.key === step.word)!;
      return { correct: ok, answer: <span className="ar text-2xl">{T(right, true)}</span> };
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [sel, step.word]);
  return (
    <div>
      <Title>{lang === "bn" ? <>“{meaning(w, lang)}” অর্থের শব্দটিতে ট্যাপ করুন <Emoji e={w.emoji} /></> : <>{t("tapWord")} “{meaning(w, lang)}” <Emoji e={w.emoji} /></>}</Title>
      <div dir="rtl" className="card flex flex-wrap justify-center gap-2 p-4">
        {line.tokens.map((tk, i) => {
          const st = !locked || res === null ? null : tk.key === step.word ? "right" : i === sel ? "wrong" : null;
          return (
            <Option key={i} selected={sel === i} state={st} onClick={() => !locked && setSel(i)} className="px-3 py-1">
              <span className="ar text-3xl">{T(tk, true)}</span>
            </Option>
          );
        })}
      </div>
      <p className={`mt-3 text-center text-sm text-muted ${lang === "bn" ? "bn" : ""}`}>{line.ref || (lang === "bn" ? line.bn : line.en)}</p>
    </div>
  );
}

// ---------------- Fill the blank ----------------
export function FillEx({ step, setEvaluate, locked }: ExProps<"fill">) {
  const { t, lang } = useT();
  const line = lineById(step.lineId);
  const [sel, setSel] = useState<string | null>(null);
  const [res, setRes] = useState<boolean | null>(null);
  const answer = line.tokens[step.blank].ar;
  const { T, C } = useForm();
  useEffect(() => {
    if (!sel) return setEvaluate(null);
    setEvaluate(() => { const ok = sel === answer; setRes(ok); return { correct: ok, answer: <span className="ar text-2xl">{T(line.tokens[step.blank], true)}</span> }; });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [sel, answer]);
  return (
    <div>
      <Title>{line.kind === "everyday" ? (lang === "bn" ? "বাক্যটি পূর্ণ করুন" : "Complete the sentence") : t("fillBlank")}</Title>
      <div className="card p-4">
        <div dir="rtl" className="flex flex-wrap items-center gap-x-2 gap-y-1">
          {line.tokens.map((tk, i) =>
            i === step.blank ? (
              <span key={i} className={`ar min-w-20 rounded-xl border-b-4 px-2 text-center text-3xl ${sel ? (res === false && locked ? "border-coral text-coral" : res && locked ? "border-emerald text-emerald" : "border-sky text-sky") : "border-line text-transparent"}`}>
                {sel ? C(sel) : "ـــــ"}
              </span>
            ) : (
              <span key={i} className="ar text-3xl">{T(tk)}</span>
            ),
          )}
        </div>
        <p className={`mt-2 text-sm text-muted ${lang === "bn" ? "bn" : ""}`}>{lang === "bn" ? line.bn : line.en}</p>
      </div>
      <div className="mt-5 flex flex-wrap justify-center gap-3" dir="rtl">
        {step.options.map((o) => (
          <Option key={o} selected={sel === o} onClick={() => !locked && setSel(o)} className="px-4 py-2"
            state={!locked || res === null ? null : o === answer ? "right" : o === sel ? "wrong" : null}>
            <span className="ar text-3xl">{C(o)}</span>
          </Option>
        ))}
      </div>
    </div>
  );
}

// ---------------- Match pairs ----------------
export function MatchEx({ step, onDone }: ExProps<"match">) {
  const { t, lang } = useT();
  const right = useMemo(() => [...step.words].sort(() => Math.random() - 0.5), [step.words]);
  const [l, setL] = useState<string | null>(null);
  const [r, setR] = useState<string | null>(null);
  const [done, setDone] = useState<string[]>([]);
  const [bad, setBad] = useState<string[]>([]);
  const [mistakes, setMistakes] = useState(0);
  const { F } = useForm();
  useEffect(() => {
    if (!l || !r) return;
    if (l === r) {
      sfx("correct");
      const nd = [...done, l];
      setDone(nd); setL(null); setR(null);
      if (nd.length === step.words.length) setTimeout(() => onDone(mistakes === 0), 400);
    } else {
      sfx("wrong");
      setBad([l, r]); setMistakes((m) => m + 1);
      setTimeout(() => { setBad([]); setL(null); setR(null); }, 500);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [l, r]);
  const cls = (k: string, side: "l" | "r") =>
    done.includes(k) ? "opacity-30 pointer-events-none border-emerald bg-emerald-light"
      : bad.includes(k) && ((side === "l" && l === k) || (side === "r" && r === k)) ? "border-coral bg-coral-light animate-shake"
      : (side === "l" ? l : r) === k ? "border-sky bg-sky-light" : "";
  return (
    <div>
      <Title>{t("matchPairs")}</Title>
      <div className="grid grid-cols-2 gap-3">
        <div className="flex flex-col gap-3">
          {step.words.map((k) => (
            <button key={k} onClick={() => setL(k)} className={`chip min-h-16 p-2 ${cls(k, "l")}`}>
              <span className="ar text-2xl">{F(WORDS[k].ar)}</span>
            </button>
          ))}
        </div>
        <div className="flex flex-col gap-3">
          {right.map((k) => (
            <button key={k} onClick={() => setR(k)} className={`chip min-h-16 p-2 text-sm font-bold leading-tight ${lang === "bn" ? "bn" : ""} ${cls(k, "r")}`}>
              <Emoji e={WORDS[k].emoji} /> {meaning(WORDS[k], lang)}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}

// ---------------- Build the meaning word-by-word ----------------
export function BuildEx({ step, setEvaluate, locked }: ExProps<"build">) {
  const { t, lang } = useT();
  const line = lineById(step.lineId);
  const seg = line.tokens.slice(step.from, step.to + 1);
  const { T } = useForm();
  const gl = (x: Token) => (lang === "bn" && x.bn ? x.bn : x.en);
  const tiles = useMemo(
    () => [...seg, ...step.extras].map((x, i) => ({ id: i, text: gl(x) })).sort(() => Math.random() - 0.5),
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [step.id, lang],
  );
  const [picked, setPicked] = useState<number[]>([]);
  const [res, setRes] = useState<boolean | null>(null);
  useEffect(() => {
    if (picked.length < seg.length) return setEvaluate(null);
    setEvaluate(() => {
      const ok = picked.every((id, i) => tiles.find((x) => x.id === id)!.text === gl(seg[i]));
      setRes(ok);
      return { correct: ok, answer: seg.map(gl).join(" · ") };
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [picked]);
  const tap = (id: number) => { if (!locked && picked.length < seg.length && !picked.includes(id)) setPicked([...picked, id]); };
  const wholeVerse = line.verseAudio && step.from === 0 && step.to === line.tokens.length - 1;
  return (
    <div>
      <Title>{t("buildMeaning")}</Title>
      <div className="card p-3">
        <div dir="rtl" className="flex flex-wrap justify-center gap-2">
          {seg.map((tk, i) => {
            const pid = picked[i];
            const ok = locked && res !== null ? tiles.find((x) => x.id === pid)?.text === gl(tk) : null;
            return (
              <div key={i} className="flex w-[30%] min-w-24 flex-col items-center">
                <span className="ar text-3xl">{T(tk)}</span>
                <button dir="ltr" onClick={() => !locked && pid !== undefined && i === picked.length - 1 && setPicked(picked.slice(0, -1))}
                  className={`mt-1 min-h-11 w-full rounded-xl border-2 border-dashed px-1 py-1 text-[13px] font-bold leading-tight ${lang === "bn" ? "bn" : ""} ${
                    pid === undefined ? (i === picked.length ? "border-sky bg-sky-light/60" : "border-line") : ok === false ? "border-coral bg-coral-light" : ok ? "border-emerald bg-emerald-light" : "border-solid border-sky bg-white"}`}>
                  {pid !== undefined ? tiles.find((x) => x.id === pid)!.text : ""}
                </button>
              </div>
            );
          })}
        </div>
        {wholeVerse && (
          <button onClick={() => playVerse(line.verseAudio!)} className="mx-auto mt-2 flex items-center gap-1 text-sm font-bold text-sky"><Volume2 size={16} /> {t("listen")}</button>
        )}
      </div>
      <div className="mt-4 flex flex-wrap justify-center gap-2">
        {tiles.map((x) => (
          <button key={x.id} onClick={() => tap(x.id)} disabled={picked.includes(x.id)}
            className={`chip px-3 py-2 text-[15px] font-bold ${lang === "bn" ? "bn" : ""} ${picked.includes(x.id) ? "opacity-25" : ""}`}>
            {x.text}
          </button>
        ))}
      </div>
    </div>
  );
}

// ---------------- Verse / sentence meaning ----------------
export function MeaningEx({ step, setEvaluate, locked }: ExProps<"meaning">) {
  const { t, lang } = useT();
  const line = lineById(step.lineId);
  const [sel, setSel] = useState<string | null>(null);
  const [res, setRes] = useState<boolean | null>(null);
  const tx = (id: string) => (lang === "bn" ? lineById(id).bn : lineById(id).en);
  useEffect(() => {
    if (!sel) return setEvaluate(null);
    setEvaluate(() => { const ok = sel === step.lineId; setRes(ok); return { correct: ok, answer: tx(step.lineId) }; });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [sel, lang]);
  return (
    <div>
      <Title>{t("verseMeaning")}</Title>
      <div className="card mb-5 p-4"><ArabicLine line={line} size="text-3xl" showTranslation={false} /></div>
      <div className="flex flex-col gap-3">
        {step.options.map((id) => (
          <Option key={id} selected={sel === id} onClick={() => !locked && setSel(id)}
            state={!locked || res === null ? null : id === step.lineId ? "right" : id === sel ? "wrong" : null}>
            <span className={`text-[15px] font-semibold leading-snug ${lang === "bn" ? "bn" : ""}`}>{tx(id)}</span>
          </Option>
        ))}
      </div>
    </div>
  );
}

// ---------------- Sentence pattern card ----------------
const ROLE_COLORS: Record<string, string> = {
  thing: "bg-sky-light border-sky text-sky", about: "bg-emerald-light border-emerald text-emerald-dark",
  whose: "bg-plum/10 border-plum text-plum", like: "bg-gold-light border-gold text-gold-dark",
  who: "bg-coral-light border-coral text-coral-dark", do: "bg-emerald-light border-emerald text-emerald-dark",
  inna: "bg-coral-light border-coral text-coral-dark",
};
export function StructureEx({ step, setPager }: ExProps<"structure">) {
  const { t, lang } = useT();
  const { A } = useForm();
  const st = STRUCTURES[step.structure];
  const bn = lang === "bn" ? "bn" : "";
  const hero = (
    <div className="space-y-3">
      <Badge color="bg-sky-light text-sky">🧩 {t("structure")}</Badge>
      <div className="card p-5">
        <div className={`text-[24px] font-black leading-tight ${bn}`}>{st.emoji} <Rich text={lang === "bn" ? st.bn : st.en} /></div>
        <div dir="rtl" className="mt-4 flex flex-wrap justify-center gap-2">
          {st.shape.map((c, i) => (
            <div key={i} className={`rounded-2xl border-2 px-3 py-1 text-center ${ROLE_COLORS[c.role] || "bg-sand border-line"}`}>
              <div className="ar text-4xl text-ink">{A(c.ar).replace(CLEAN, "").replace(/\s+/g, " ").trim()}</div>
              <div dir="ltr" className={`text-sm font-bold ${bn}`}>{lang === "bn" ? c.bn : c.en}</div>
            </div>
          ))}
        </div>
        <p className={`mt-4 text-[18px] leading-relaxed text-ink/90 ${bn}`}><Rich text={lang === "bn" ? st.expl_bn : st.expl_en} /></p>
      </div>
    </div>
  );
  const pages = st.pages?.length
    ? st.pages.map((pg, i) => <TeachCard key={i} page={pg} />)
    : st.notes.map((n, i) => <TeachCard key={i} page={{ t_en: `${i + 1}`, t_bn: `${i + 1}`, x_en: n.en, x_bn: n.bn, ex: [], vs: [] }} />);
  const quran = (
    <div className="space-y-3">
      <Box title={t("inYourText")}><ArabicLine line={st.quran[0]} size="text-3xl" /></Box>
      {st.quran.length > 1 && (
        <Box title={t("inQuran")}>
          <div className="space-y-3">{st.quran.slice(1).map((l) => <ArabicLine key={l.id} line={l} size="text-3xl" fadeUnknown />)}</div>
        </Box>
      )}
    </div>
  );
  return <div className="animate-pop"><Pages pages={[hero, ...pages, quran]} setPager={setPager} /></div>;
}

// ---------------- Grammar in action: what does the piece on this real word tell you? ----------------
export function RuleEx({ step, setEvaluate, locked }: ExProps<"rule">) {
  const { lang } = useT();
  const { A, F, T } = useForm();
  const g = RULES[step.group];
  const bn = lang === "bn" ? "bn" : "";
  const [sel, setSel] = useState<string | null>(null);
  const [res, setRes] = useState<boolean | null>(null);
  const label = (id: string) => { const l = id.startsWith("x:") ? g.others[id.slice(2)] : g.opts[id]; return lang === "bn" ? l[1] : l[0]; };
  // the base word's meaning helps, unless it would give the answer away (a verb is taught in one person,
  // and a word taught with its ending is the very form asked about)
  const plain = (x: string) => x.replace(/[^\u0621-\u064A\u0671]/g, "").replace(/^[اٱ]ل/, "");
  const b0 = WORDS[step.token.key];
  const base = b0 && step.group !== "now" && step.group !== "past" && plain(b0.ar.split(" / ")[0]) !== plain(step.token.ar) ? b0 : undefined;
  const p = PATTERNS[step.pattern];
  useEffect(() => {
    if (sel === null) return setEvaluate(null);
    setEvaluate(() => {
      const ok = sel === step.pattern;
      setRes(ok);
      return {
        correct: ok, answer: <span className={bn}>{label(step.pattern)}</span>,
        why: <span className={bn}><bdi className="ar ar-in">{A(p.ar)}</bdi> = {lang === "bn" ? p.bn : p.en}. <bdi className="ar ar-in">{T(step.token, true)}</bdi> = {lang === "bn" && step.token.bn ? step.token.bn : step.token.en}</span>,
      };
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [sel, lang]);
  const state = (o: string) => (!locked || res === null ? null : o === step.pattern ? "right" : o === sel ? "wrong" : null);
  return (
    <div>
      <Badge color="bg-gold-light text-gold-dark">🔍 {lang === "bn" ? "ব্যাকরণ প্রয়োগ" : "Grammar in action"}</Badge>
      <h2 className={`mb-4 text-[22px] font-black leading-snug ${bn}`}>{lang === "bn" ? g.q_bn : g.q_en}</h2>
      <div className="card mb-5 p-5 text-center">
        <span className="ar text-6xl">{T(step.token, true)}</span>
        {base && (
          <div className={`mt-2 text-[17px] text-muted ${bn}`}>
            <bdi className="ar ar-in">{F(base.ar)}</bdi> = {meaning(base, lang)}
          </div>
        )}
      </div>
      <div className="flex flex-col gap-3">
        {step.options.map((o) => (
          <Option key={o} selected={sel === o} state={state(o)} onClick={() => !locked && setSel(o)} className="text-left">
            <span className={`text-[17px] font-bold ${bn}`}>{label(o)}</span>
          </Option>
        ))}
      </div>
    </div>
  );
}

// ---------------- Check your understanding (a written question about the idea just taught) ----------------
export function CheckEx({ step, setEvaluate, locked }: ExProps<"check">) {
  const { t, lang } = useT();
  const { C } = useForm();
  const c = teachOf(step.ref).checks[step.n];
  const bn = lang === "bn" ? "bn" : "";
  const [sel, setSel] = useState<number | null>(null);
  const [res, setRes] = useState<boolean | null>(null);
  const label = (i: number) => {
    const o = c.options[i];
    return typeof o === "string" ? <span className="ar text-3xl">{C(o)}</span> : <span className={`text-[17px] font-bold leading-snug ${bn}`}><Rich text={lang === "bn" ? o.bn : o.en} /></span>;
  };
  useEffect(() => {
    if (sel === null) return setEvaluate(null);
    setEvaluate(() => {
      const ok = sel === 0;
      setRes(ok);
      return { correct: ok, answer: label(0), why: <span className={bn}><Rich text={lang === "bn" ? c.why_bn : c.why_en} /></span> };
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [sel, lang]);
  const state = (i: number) => (!locked || res === null ? null : i === 0 ? "right" : i === sel ? "wrong" : null);
  return (
    <div>
      <Badge color="bg-emerald-light text-emerald-dark">🧠 {t("checkUnderstanding")}</Badge>
      <h2 className={`mb-5 text-[22px] font-black leading-snug ${bn}`}><Rich text={lang === "bn" ? c.q_bn : c.q_en} className="text-emerald-dark" /></h2>
      {c.ar && !(lang === "bn" ? c.q_bn : c.q_en).includes(c.ar) && <div className="card mb-5 p-4 text-center"><span className="ar text-5xl">{C(c.ar)}</span></div>}
      <div className={c.ar_opts ? "grid grid-cols-2 gap-3" : "flex flex-col gap-3"}>
        {step.order.map((i) => (
          <Option key={i} selected={sel === i} state={state(i)} onClick={() => !locked && setSel(i)}
            className={c.ar_opts ? "flex min-h-20 items-center justify-center text-center" : "text-left"}>
            {label(i)}
          </Option>
        ))}
      </div>
    </div>
  );
}

// ---------------- See how it's built (word for word vs natural) ----------------
export function BreakdownEx({ step }: ExProps<"breakdown">) {
  const { lang } = useT();
  const st = STRUCTURES[step.structure];
  const bn = lang === "bn" ? "bn" : "";
  const lines: Line[] = step.lineIds.map(lineById);
  // word for word: drop the helper words in brackets — they are exactly what Arabic leaves out
  const gl = (x: Token) => (lang === "bn" && x.bn ? x.bn : x.en).replace(/\s*[([][^)\]]*[)\]]/g, "").replace(/\.$/, "").trim();
  return (
    <div className="animate-pop space-y-3">
      <Badge color="bg-sky-light text-sky">🔍 {lang === "bn" ? "কীভাবে গঠিত দেখুন" : "See how it's built"}</Badge>
      <div className={`text-[22px] font-black ${bn}`}>{st.emoji} <Rich text={lang === "bn" ? st.bn : st.en} /></div>
      {lines.map((l) => (
        <div key={l.id} className="card p-4">
          <ArabicLine line={l} size="text-3xl" showGloss showTranslation={false} />
          <div className={`mt-2 space-y-1 rounded-xl bg-sand px-3 py-2.5 text-[17px] leading-snug ${bn}`}>
            <div><span className="font-bold text-muted">{lang === "bn" ? "শব্দে শব্দে:" : "Word for word:"}</span> {l.tokens.map(gl).join(" · ")}</div>
            <div><span className="font-bold text-emerald">{lang === "bn" ? "অর্থ:" : "Meaning:"}</span> {lang === "bn" ? l.bn : l.en}</div>
          </div>
        </div>
      ))}
    </div>
  );
}

// ---------------- Arrange Arabic tiles to say a sentence ----------------
export function ArrangeEx({ step, setEvaluate, locked }: ExProps<"arrange">) {
  const { t, lang } = useT();
  const { T, C } = useForm();
  const line = lineById(step.lineId);
  const tiles = useMemo(
    () => [...line.tokens.map((x, i) => ({ id: i, ar: x.ar, disp: T(x, true) })), ...step.extras.map((a, i) => ({ id: 100 + i, ar: a, disp: C(a) }))]
      .sort(() => Math.random() - 0.5),
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [step.id],
  );
  const [picked, setPicked] = useState<number[]>([]);
  const [res, setRes] = useState<boolean | null>(null);
  useEffect(() => {
    if (picked.length < line.tokens.length) return setEvaluate(null);
    setEvaluate(() => {
      const ok = picked.every((id, i) => tiles.find((x) => x.id === id)!.ar === line.tokens[i].ar);
      setRes(ok);
      return { correct: ok, answer: <span className="ar text-2xl">{line.tokens.map((x) => T(x, true)).join(" ")}</span> };
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [picked]);
  const tap = (id: number) => { if (!locked && picked.length < line.tokens.length && !picked.includes(id)) setPicked([...picked, id]); };
  return (
    <div>
      <Title>{t("sayInArabic")}</Title>
      <div className={`card mb-4 p-4 text-xl font-extrabold ${lang === "bn" ? "bn" : ""}`}>“{lang === "bn" ? line.bn : line.en}”</div>
      <div dir="rtl" className={`flex min-h-20 flex-wrap items-center gap-2 rounded-2xl border-2 border-dashed p-3 ${
        locked && res !== null ? (res ? "border-emerald bg-emerald-light" : "border-coral bg-coral-light") : "border-line"}`}>
        {picked.map((id, i) => (
          <button key={id} onClick={() => !locked && i === picked.length - 1 && setPicked(picked.slice(0, -1))} className="chip px-3 py-1">
            <span className="ar text-3xl">{tiles.find((x) => x.id === id)!.disp}</span>
          </button>
        ))}
        {picked.length === 0 && <span className="text-sm text-muted" dir="ltr">{lang === "bn" ? "নিচের শব্দগুলো ডান থেকে বামে সাজান" : "Tap the words below, right to left"}</span>}
      </div>
      <div dir="rtl" className="mt-5 flex flex-wrap justify-center gap-2">
        {tiles.map((x) => (
          <button key={x.id} onClick={() => tap(x.id)} disabled={picked.includes(x.id)} className={`chip px-3 py-1 ${picked.includes(x.id) ? "opacity-25" : ""}`}>
            <span className="ar text-3xl">{x.disp}</span>
          </button>
        ))}
      </div>
    </div>
  );
}

// ---------------- Read a verse (new verse / repeated phrase) ----------------
export function ReadEx({ step }: ExProps<"read">) {
  const { t, lang } = useT();
  const line = lineById(step.lineId);
  const [show, setShow] = useState(false);
  return (
    <div className="animate-pop">
      <Badge color="bg-gold-light text-gold-dark">📖 {step.title === "chunk" ? t("readPhrase") : t("readNewVerse")}</Badge>
      <div className="card p-4">
        <ArabicLine line={line} size="text-3xl" fadeUnknown highlightKeys={step.highlight} showTranslation={false} />
        {show ? (
          <p className={`mt-3 text-[15px] leading-relaxed ${lang === "bn" ? "bn" : ""}`}>
            {lang === "bn" ? line.bn : line.en} <span className="text-xs font-bold text-muted">{line.ref}</span>
          </p>
        ) : (
          <button onClick={() => setShow(true)} className="btn btn-ghost mt-3 w-full py-2 text-sm">{t("showMeaning")}</button>
        )}
      </div>
      <p className={`mt-3 text-center text-sm text-muted ${lang === "bn" ? "bn" : ""}`}>{t("fadedHint")}</p>
    </div>
  );
}

export { playLine };
