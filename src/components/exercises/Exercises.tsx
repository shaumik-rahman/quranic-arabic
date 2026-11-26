"use client";
import { useEffect, useMemo, useState } from "react";
import { PATTERNS, STRUCTURES, WORDS, linesWithWord, meaning, type Line, type Token } from "@/lib/course";
import { lineById, type Step } from "@/lib/exercises";
import { playLine, playVerse, sfx } from "@/lib/audio";
import { useT } from "@/lib/i18n";
import { useProgress } from "@/lib/store";
import { useScript } from "@/lib/script";
import { Volume2 } from "lucide-react";
import { Emoji } from "../ui";
import { ArabicLine } from "../ArabicLine";

export type Evaluate = () => { correct: boolean; answer: React.ReactNode };
export interface ExProps<K extends Step["kind"]> {
  step: Extract<Step, { kind: K }>;
  setEvaluate: (fn: Evaluate | null) => void; // graded steps: set when the user has a selection
  locked: boolean; // after checking
  onDone: (correct: boolean) => void; // for self-completing steps (match)
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
    <div className="flex flex-wrap gap-1.5">
      {list.map((p) => (
        <span key={p} className={`rounded-full bg-white px-2 py-0.5 text-sm font-bold ${lang === "bn" ? "bn" : ""}`}>
          <span className="ar text-lg text-emerald">{A(PATTERNS[p].ar)}</span> = {lang === "bn" ? PATTERNS[p].bn : PATTERNS[p].en}
        </span>
      ))}
    </div>
  );
}

// ---------------- New word ----------------
export function IntroEx({ step }: ExProps<"intro">) {
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
  return (
    <div className="animate-pop space-y-3">
      <Badge color="bg-plum/15 text-plum">✨ {t("newWord")}</Badge>
      <div className="card flex flex-col items-center p-5 text-center">
        <Emoji e={w.emoji} className="text-6xl" />
        <div className="ar mt-2 text-5xl text-ink">{F(w.ar)}</div>
        {w.ar.includes(" / ") && <div className="ar text-2xl text-muted">{A(w.ar.split(" / ")[1])}</div>}
        <div className={`mt-1 text-2xl font-black text-emerald ${bn}`}>{meaning(w, lang)}</div>
        {pos && <div className={`mt-1 text-xs font-bold uppercase tracking-wider text-muted ${bn}`}>{lang === "bn" ? pos[1] : pos[0]}</div>}
      </div>

      {(firstTok?.pats.length || w.tip || w.root || w.count > 0) && (
        <Box title={lang === "bn" ? "বুঝে নিন" : "Understand it"} tone="sky">
          <div className={`space-y-2 text-[15px] leading-relaxed ${bn}`}>
            {firstTok && firstTok.pats.length > 0 && (
              <div>
                <div className="mb-1">
                  <span className="ar text-xl">{T(firstTok, true)}</span>{" "}
                  {lang === "bn" ? "শব্দে আছে:" : "is built with:"}
                </div>
                <PatternChips pats={firstTok.pats} />
              </div>
            )}
            {w.tip && <div>💡 {A(w.tip)}</div>}
            {w.count > 0 && (
              <div>
                📖 {lang === "bn" ? `কুরআনে ${w.count} বার এসেছে।` : `Appears ${w.count} times in the Quran.`}
                {w.root && <> {lang === "bn" ? "মূল অক্ষর" : "Root letters"} <bdi className="ar text-lg text-emerald">{w.rootSpaced}</bdi>.</>}
              </div>
            )}
            {family.length > 0 && (
              <div>
                <div className="mb-1">{lang === "bn" ? "একই পরিবারের শব্দ:" : "Same family:"}</div>
                <div className="flex flex-wrap gap-1.5">
                  {family.map((f) => (
                    <span key={f.key} className="rounded-xl bg-white px-2 py-0.5 text-sm">
                      <span className="ar text-lg">{T({ ar: f.ex, ip: f.exIp }, true).replace(CLEAN, "")}</span>{" "}
                      <span className={bn}>{WORDS[f.key] ? meaning(WORDS[f.key], lang) : f.gloss}</span>
                    </span>
                  ))}
                </div>
              </div>
            )}
          </div>
        </Box>
      )}

      {cogs.length > 0 && (
        <Box title={t("related")} tone="gold">
          {cogs.map(([l, v]) => (
            <div key={l} className="text-sm"><span className="mr-2 inline-block w-20 font-bold text-gold-dark">{l === "en" ? "English" : l === "bn" ? "বাংলা" : "Hindi/Urdu"}</span><span className={l === "bn" ? "bn" : ""}>{v}</span></div>
          ))}
        </Box>
      )}

      {examples.length > 0 && (
        <Box title={lang === "bn" ? "উদাহরণ" : "Examples"}>
          <div className="space-y-3">
            {examples.map(({ line }) => <ArabicLine key={line.id} line={line} size="text-2xl" highlightKey={step.word} />)}
          </div>
        </Box>
      )}
    </div>
  );
}

// ---------------- Pattern (a pinch of grammar) ----------------
export function PatternEx({ step }: ExProps<"pattern">) {
  const { t, lang } = useT();
  const { A, F, T } = useForm();
  const p = PATTERNS[step.pattern];
  const bn = lang === "bn" ? "bn" : "";
  useEffect(() => { useProgress.getState().learn(["p:" + step.pattern]); }, [step.pattern]);
  return (
    <div className="animate-pop space-y-3">
      <Badge color="bg-gold-light text-gold-dark">🧂 {t("newPattern")}</Badge>
      <div className="card p-5 text-center">
        <div className="ar text-6xl text-emerald">{A(p.ar)}</div>
        <div className={`mt-1 text-2xl font-black ${bn}`}>{p.emoji} {lang === "bn" ? p.bn : p.en}</div>
        <p className={`mt-3 text-left text-[15px] leading-relaxed text-ink/85 ${bn}`}>{A(lang === "bn" ? p.expl_bn : p.expl_en)}</p>
        {(p.more_en || p.more_bn) && <p className={`mt-2 text-left text-[15px] leading-relaxed text-ink/70 ${bn}`}>{A(lang === "bn" ? p.more_bn : p.more_en)}</p>}
      </div>
      <Box title={lang === "bn" ? "যা আপনি পড়েন তাতে" : "In what you recite"}>
        <div className="divide-y-2 divide-line">
          {p.examples.slice(0, 4).map((e, i) => {
            const base = e.key ? WORDS[e.key] : undefined;
            return (
              <div key={i} className="flex items-center gap-3 py-2">
                <span className="ar min-w-20 text-right text-2xl">{T({ ar: e.ar, ip: e.ip }, true).replace(CLEAN, "")}</span>
                <div className={`flex-1 text-sm ${bn}`}>
                  <div className="font-bold">{lang === "bn" ? e.bn : e.en}</div>
                  {base && <div className="text-muted"><span className="ar text-base">{F(base.ar)}</span> ({meaning(base, lang)}) + <span className="ar text-base text-emerald">{A(p.ar)}</span></div>}
                </div>
              </div>
            );
          })}
        </div>
      </Box>
    </div>
  );
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
      <div className={`mb-5 text-center text-sm text-muted ${lang === "bn" ? "bn" : ""}`}>💡 <span className="ar text-lg text-emerald">{A(p.ar)}</span> = {lang === "bn" ? p.bn : p.en}</div>
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
export function StructureEx({ step }: ExProps<"structure">) {
  const { t, lang } = useT();
  const { A } = useForm();
  const st = STRUCTURES[step.structure];
  const bn = lang === "bn" ? "bn" : "";
  return (
    <div className="animate-pop space-y-3">
      <Badge color="bg-sky-light text-sky">🧩 {t("structure")}</Badge>
      <div className="card p-5">
        <div className={`text-2xl font-black ${bn}`}>{st.emoji} {lang === "bn" ? st.bn : st.en}</div>
        <div dir="rtl" className="mt-4 flex flex-wrap justify-center gap-2">
          {st.shape.map((c, i) => (
            <div key={i} className={`rounded-2xl border-2 px-3 py-1 text-center ${ROLE_COLORS[c.role] || "bg-sand border-line"}`}>
              <div className="ar text-3xl text-ink">{A(c.ar).replace(CLEAN, "").replace(/\s+/g, " ").trim()}</div>
              <div dir="ltr" className={`text-xs font-bold ${bn}`}>{lang === "bn" ? c.bn : c.en}</div>
            </div>
          ))}
        </div>
        <p className={`mt-4 text-[15px] leading-relaxed text-ink/85 ${bn}`}>{A(lang === "bn" ? st.expl_bn : st.expl_en)}</p>
      </div>
      {st.notes?.length > 0 && (
        <Box title={lang === "bn" ? "লক্ষ করুন" : "Notice"} tone="sky">
          <ul className={`space-y-2 text-[15px] leading-relaxed ${bn}`}>
            {st.notes.map((n, i) => <li key={i} className="flex gap-2"><span className="font-black text-sky">{i + 1}.</span><span>{A(lang === "bn" ? n.bn : n.en)}</span></li>)}
          </ul>
        </Box>
      )}
      <Box title={t("inYourText")}><ArabicLine line={st.quran[0]} size="text-2xl" /></Box>
      {st.quran.length > 1 && (
        <Box title={t("inQuran")}>
          <div className="space-y-3">{st.quran.slice(1).map((l) => <ArabicLine key={l.id} line={l} size="text-2xl" fadeUnknown />)}</div>
        </Box>
      )}
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
      <div className={`text-lg font-black ${bn}`}>{st.emoji} {lang === "bn" ? st.bn : st.en}</div>
      {lines.map((l) => (
        <div key={l.id} className="card p-4">
          <ArabicLine line={l} size="text-3xl" showGloss showTranslation={false} />
          <div className={`mt-2 rounded-xl bg-sand px-3 py-2 text-sm ${bn}`}>
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
