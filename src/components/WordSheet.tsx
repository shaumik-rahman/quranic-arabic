"use client";
import { useScript } from "@/lib/script";
import { createContext, useCallback, useContext, useEffect, useState } from "react";
import { ChevronDown, ChevronUp, Volume2, X } from "lucide-react";
import { PATTERNS, TOTAL_TOKENS, WORDS, meaning, type Token } from "@/lib/course";
import { playWord } from "@/lib/audio";
import { useProgress } from "@/lib/store";
import { strengthLevel } from "@/lib/srs";
import { useT } from "@/lib/i18n";
import { Emoji, StrengthDots, fmtPct } from "./ui";

/** Anything tappable: a curriculum token, a curriculum word, or a word from the full-Quran reader. */
export interface SheetPayload {
  ar: string;
  ip?: string | null; // IndoPak spelling when known
  en?: string; // contextual gloss
  bn?: string;
  key?: string; // curriculum / lemma key
  pats?: string[];
  audio?: string | null;
  tr?: string;
  lemma?: { ar: string; root: string; count: number }; // for words outside the curriculum
}

const Ctx = createContext<(p: SheetPayload) => void>(() => {});
export const useWordSheet = () => useContext(Ctx);
export const tokenPayload = (t: Token): SheetPayload => ({ ar: t.ar, ip: t.ip, en: t.en, bn: t.bn, key: t.key, pats: t.pats, audio: t.audio, tr: t.tr });

export function WordSheetProvider({ children }: { children: React.ReactNode }) {
  const [p, setP] = useState<SheetPayload | null>(null);
  const open = useCallback((x: SheetPayload) => { setP(x); if (x.audio) playWord(x.audio); }, []);
  return (
    <Ctx.Provider value={open}>
      {children}
      {p && <Sheet p={p} onClose={() => setP(null)} />}
    </Ctx.Provider>
  );
}

function Sheet({ p, onClose }: { p: SheetPayload; onClose: () => void }) {
  const { t, lang } = useT();
  const [more, setMore] = useState(false);
  const items = useProgress((s) => s.items);
  const translit = useProgress((s) => s.settings.translit);
  const { A, T } = useScript();
  const w = p.key ? WORDS[p.key] : undefined;
  useEffect(() => { setMore(false); }, [p]);
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  const ctxGloss = lang === "bn" && p.bn ? p.bn : p.en;
  const core = w ? meaning(w, lang) : undefined;
  const count = w?.count ?? p.lemma?.count ?? 0;
  const root = w?.rootSpaced ?? (p.lemma?.root ? p.lemma.root.split("").join(" ") : "");
  const known = p.key ? items[p.key] : undefined;
  const cogs = w ? Object.entries(w.cog) : [];

  return (
    <div className="fixed inset-0 z-50 flex items-end justify-center bg-black/30" onClick={onClose}>
      <div className="animate-slideup pb-safe w-full max-w-lg rounded-t-3xl bg-cream px-5 pt-3 shadow-2xl max-h-[85dvh] overflow-y-auto"
        onClick={(e) => e.stopPropagation()}>
        <div className="mx-auto mb-2 h-1.5 w-10 rounded-full bg-line" />
        <div className="flex items-start gap-4">
          {w?.emoji ? <Emoji e={w.emoji} className="text-5xl" /> : null}
          <div className="flex-1 min-w-0">
            <div className="ar text-4xl text-ink" dir="rtl">{T(p)}</div>
            {translit && p.tr && <div className="text-sm italic text-muted">{p.tr}</div>}
          </div>
          <div className="flex flex-col gap-2">
            <button onClick={onClose} className="rounded-full p-2 text-muted hover:bg-sand" aria-label="Close"><X size={20} /></button>
            {(p.audio || w?.audio) && (
              <button onClick={() => playWord(p.audio || w?.audio)} className="rounded-full bg-sky-light p-2 text-sky" aria-label={t("listen")}><Volume2 size={20} /></button>
            )}
          </div>
        </div>

        <div className={`mt-2 text-xl font-extrabold ${lang === "bn" ? "bn" : ""}`}>{ctxGloss || core}</div>
        {core && ctxGloss && core !== ctxGloss && (
          <div className={`text-muted ${lang === "bn" ? "bn" : ""}`}>
            <span className="ar text-lg">{A(w!.ar)}</span> = {core}
          </div>
        )}
        {known && (
          <div className="mt-2 inline-flex items-center gap-2 rounded-full bg-emerald-light px-3 py-1 text-sm font-bold text-emerald-dark">
            <StrengthDots level={strengthLevel(known)} /> {lang === "bn" ? "আপনি জানেন" : "You know this"}
          </div>
        )}
        {cogs.length > 0 && (
          <div className="mt-3 rounded-2xl bg-gold-light p-3">
            <div className="mb-1 text-xs font-extrabold uppercase tracking-wider text-gold-dark">{t("related")}</div>
            {cogs.map(([l, v]) => (
              <div key={l} className="text-sm"><span className="mr-2 inline-block w-20 font-bold text-muted">{l === "en" ? "English" : l === "bn" ? "বাংলা" : "Hindi/Urdu"}</span><span className={l === "bn" ? "bn" : ""}>{v}</span></div>
            ))}
          </div>
        )}

        <button onClick={() => setMore(!more)} className="btn btn-ghost mt-4 w-full py-2.5">
          {more ? <ChevronUp size={18} /> : <ChevronDown size={18} />} {more ? t("less") : t("more")}
        </button>

        {more && (
          <div className="mt-4 space-y-4 pb-4">
            {(root || count > 0) && (
              <div className="grid grid-cols-2 gap-3">
                {root && (
                  <div className="card p-3 text-center">
                    <div className="text-xs font-bold uppercase text-muted">{t("root")}</div>
                    <div className="ar text-3xl text-emerald">{root}</div>
                  </div>
                )}
                <div className="card p-3 text-center">
                  <div className="text-xs font-bold uppercase text-muted">{t("appears")}</div>
                  <div className="text-2xl font-black text-emerald">{count.toLocaleString()}×</div>
                  <div className="text-xs text-muted">{fmtPct((100 * count) / TOTAL_TOKENS)}% {lang === "bn" ? "কুরআনের" : "of the Quran"}</div>
                </div>
              </div>
            )}
            {w?.tip && <div className="rounded-2xl bg-sky-light p-3 text-sm">💡 {A(w.tip)}</div>}
            {p.pats && p.pats.length > 0 && (
              <div>
                <div className="mb-2 text-xs font-extrabold uppercase tracking-wider text-muted">{t("newPattern")}</div>
                <div className="space-y-2">
                  {p.pats.filter((x) => PATTERNS[x]).map((x) => (
                    <div key={x} className="rounded-2xl bg-white p-3 text-sm border-2 border-line">
                      <span className="ar mr-2 text-xl text-emerald">{A(PATTERNS[x].ar)}</span>
                      <b>{lang === "bn" ? PATTERNS[x].bn : PATTERNS[x].en}</b>
                      <div className={`mt-1 text-muted ${lang === "bn" ? "bn" : ""}`}>{A(lang === "bn" ? PATTERNS[x].expl_bn : PATTERNS[x].expl_en)}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}
            {w && w.family.length > 1 && (
              <div>
                <div className="mb-2 text-xs font-extrabold uppercase tracking-wider text-muted">{t("family")} · <span className="ar normal-case">{root}</span></div>
                <div className="divide-y-2 divide-line overflow-hidden rounded-2xl border-2 border-line bg-white">
                  {w.family.map((f) => {
                    const fw = WORDS[f.key];
                    return (
                      <div key={f.key} className={`flex items-center gap-3 px-3 py-2 ${f.self ? "bg-emerald-light" : ""}`}>
                        <div className="w-24 text-right"><span className="ar text-xl">{T({ ar: f.ex, ip: f.exIp })}</span></div>
                        <div className="flex-1 text-sm">
                          <div className="font-bold">{fw ? meaning(fw, lang) : f.gloss}</div>
                          <div className="text-xs text-muted">{f.count}× · {f.ref}{items[f.key] ? " · ✓" : ""}</div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
