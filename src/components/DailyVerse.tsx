"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import { Volume2 } from "lucide-react";
import { WORDS, coverage } from "@/lib/course";
import { useDailyVerse } from "@/lib/readable";
import { useProgress } from "@/lib/store";
import { useScript } from "@/lib/script";
import { playVerse } from "@/lib/audio";
import { useT } from "@/lib/i18n";
import { useWordSheet } from "./WordSheet";

type Verse = { v: number; en: string; bn: string; w: [string, string, string, number, string?, string?][] };
const pad = (x: number) => String(x).padStart(3, "0");

/** A verse the learner can understand (or nearly), new every day. */
export function DailyVerse() {
  const pick = useDailyVerse();
  const { lang } = useT();
  const { script } = useScript();
  const items = useProgress((s) => s.items);
  const open = useWordSheet();
  const [verse, setVerse] = useState<Verse | null>(null);
  useEffect(() => {
    if (!pick) return;
    fetch(`/quran/${pick.s}.json`).then((r) => r.json())
      .then((d: { verses: Verse[] }) => setVerse(d.verses.find((x) => x.v === pick.v) ?? null)).catch(() => {});
  }, [pick?.s, pick?.v]); // eslint-disable-line react-hooks/exhaustive-deps
  if (!pick || !verse) return null;
  const bn = lang === "bn" ? "bn" : "";
  const meta = coverage.surahs[pick.s - 1];
  return (
    <section className="card mt-5 p-4" data-testid="daily-verse">
      <div className="flex items-center justify-between">
        <div className={`text-[13px] font-extrabold uppercase tracking-wider text-gold-dark ${bn}`}>☀️ {lang === "bn" ? "আজকের আয়াত" : "Verse of the day"}</div>
        <button onClick={() => playVerse(pad(pick.s) + pad(pick.v))} className="rounded-full bg-sky-light p-2 text-sky" aria-label="Play recitation"><Volume2 size={18} /></button>
      </div>
      <p className={`mt-1 text-[15px] text-muted ${bn}`}>
        {pick.full
          ? lang === "bn" ? "এই আয়াতের প্রতিটি শব্দ আপনি চেনেন।" : "You know every word in this verse."
          : lang === "bn" ? "প্রায় সব শব্দ আপনার চেনা। নতুনগুলোর অর্থ নিচে দেওয়া।" : "You know almost every word. The new ones show their meaning."}
      </p>
      <div dir="rtl" className="mt-3 flex flex-wrap gap-x-1.5 gap-y-2">
        {verse.w.map((w, i) => {
          const lm = pick.lemmas[w[3]];
          const known = !!items[lm[0]];
          const gloss = lang === "bn" && w[5] ? w[5] : w[1];
          return (
            <button key={i} onClick={() => open({ ar: w[0], ip: w[4] || null, en: w[1], bn: w[5] || undefined, tr: w[2], key: WORDS[lm[0]] ? lm[0] : undefined, lemma: { ar: lm[1], root: lm[2], count: lm[3] } })}
              className={`rounded-xl px-1 text-center transition hover:bg-gold-light ${known ? "" : "bg-sand"}`}>
              <span className="ar block text-[30px]">{script === "indopak" && w[4] ? w[4] : w[0]}</span>
              {!known && <span className={`block max-w-[7rem] text-[12px] leading-tight text-muted ${bn}`} dir="ltr">{gloss}</span>}
            </button>
          );
        })}
      </div>
      <p className={`mt-3 text-[16px] leading-relaxed text-ink/85 ${bn}`}>{lang === "bn" ? verse.bn : verse.en}</p>
      <div className="mt-2 flex items-center justify-between text-[13px] font-bold text-muted">
        <span>{meta.tr} {pick.s}:{pick.v}</span>
        <Link href={`/quran/${pick.s}#v${pick.v}`} className={`text-sky ${bn}`}>{lang === "bn" ? "সূরাটি খুলুন →" : "Open the surah →"}</Link>
      </div>
    </section>
  );
}
