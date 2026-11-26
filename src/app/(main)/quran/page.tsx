"use client";
import Link from "next/link";
import { useMemo, useState } from "react";
import { useProgress } from "@/lib/store";
import { quranCoverage, surahCoverage } from "@/lib/stats";
import { useT } from "@/lib/i18n";
import { Ring, fmtPct } from "@/components/ui";

export default function QuranPage() {
  const p = useProgress();
  const { lang } = useT();
  const [sort, setSort] = useState<"order" | "best" | "short">("order");
  const cov = quranCoverage(p);
  const surahs = useMemo(() => {
    const s = surahCoverage(p);
    if (sort === "best") return [...s].sort((a, b) => b.pct - a.pct);
    if (sort === "short") return [...s].sort((a, b) => a.total - b.total);
    return s;
  }, [p, sort]);

  return (
    <div>
      <section className="pattern-bg rounded-3xl p-5 text-white shadow-[0_5px_0_var(--color-emerald-dark)]">
        <div className="flex items-center gap-4">
          <Ring pct={cov.pctLearned} size={84} stroke={8} color="var(--color-gold)" track="rgba(255,255,255,.2)">
            <span className="text-xl font-black">{fmtPct(cov.pctLearned)}%</span>
          </Ring>
          <div className={`flex-1 ${lang === "bn" ? "bn" : ""}`}>
            <div className="text-lg font-black">{lang === "bn" ? "আপনার কুরআন" : "Your Quran"}</div>
            <div className="text-sm text-white/85">
              {lang === "bn"
                ? `${cov.wordsLearned}টি শব্দ শিখেছেন — কুরআনে এগুলো ${cov.occurrencesLearned.toLocaleString()} বার এসেছে।`
                : `You've learned ${cov.wordsLearned} words. They appear ${cov.occurrencesLearned.toLocaleString()} times in the Quran.`}
            </div>
          </div>
        </div>
      </section>

      <p className={`mt-4 px-1 text-sm text-muted ${lang === "bn" ? "bn" : ""}`}>
        {lang === "bn" ? "যেকোনো সূরা খুলুন — যে শব্দগুলো আপনি জানেন সেগুলো সবুজ দেখাবে।" : "Open any surah — the words you know light up green."}
      </p>
      <div className="no-scrollbar my-3 flex gap-2 overflow-x-auto">
        {([["order", lang === "bn" ? "ক্রমানুসারে" : "In order"], ["best", lang === "bn" ? "সবচেয়ে বেশি বোঝা" : "Best understood"], ["short", lang === "bn" ? "ছোট সূরা" : "Shortest"]] as const).map(([k, l]) => (
          <button key={k} onClick={() => setSort(k)} className={`shrink-0 rounded-full border-2 px-3 py-1 text-sm font-bold ${sort === k ? "border-emerald bg-emerald-light text-emerald-dark" : "border-line bg-white text-muted"}`}>{l}</button>
        ))}
      </div>
      <div className="card divide-y-2 divide-line overflow-hidden">
        {surahs.map((s) => (
          <Link key={s.n} href={`/quran/${s.n}`} className="flex items-center gap-3 px-3 py-2.5">
            <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-sand text-sm font-black text-muted">{s.n}</div>
            <div className="min-w-0 flex-1">
              <div className="flex items-baseline justify-between gap-2">
                <span className="truncate font-extrabold">{s.tr}</span>
                <span className="ar text-xl leading-tight">{s.ar}</span>
              </div>
              <div className="mt-1 flex items-center gap-2">
                <div className="h-2 flex-1 overflow-hidden rounded-full bg-line">
                  <div className={`h-full rounded-full ${s.pct >= 50 ? "bg-gold" : "bg-emerald"}`} style={{ width: `${s.pct}%` }} />
                </div>
                <span className="w-10 text-right text-xs font-black text-emerald">{Math.round(s.pct)}%</span>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
