"use client";
import Link from "next/link";
import { WORDS, meaning } from "@/lib/course";
import { useProgress } from "@/lib/store";
import { dueItems, quranCoverage, wordKeysLearned } from "@/lib/stats";
import { strength, strengthLevel } from "@/lib/srs";
import { useT } from "@/lib/i18n";
import { Emoji, StrengthDots } from "@/components/ui";
import { tokenPayload, useWordSheet } from "@/components/WordSheet";

export default function ReviewPage() {
  const p = useProgress();
  const { t, lang } = useT();
  const open = useWordSheet();
  const due = dueItems(p);
  const learned = wordKeysLearned(p);
  const cov = quranCoverage(p);
  const counts = { learning: 0, strong: 0, mastered: 0 };
  learned.forEach((k) => { const s = strength(p.items[k]); if (s !== "new") counts[s]++; });
  const weakest = [...learned].sort((a, b) => p.items[a].interval - p.items[b].interval || b.localeCompare(a)).slice(0, 8);
  const total = Math.max(1, learned.length);

  return (
    <div className="space-y-5">
      <section className="card p-5 text-center">
        <div className="text-6xl">{due.length ? "🧠" : "✅"}</div>
        <div className="mt-2 text-3xl font-black">{due.length}</div>
        <div className={`font-bold text-muted ${lang === "bn" ? "bn" : ""}`}>{t("dueNow")}</div>
        <p className={`mt-2 text-sm text-muted ${lang === "bn" ? "bn" : ""}`}>
          {lang === "bn" ? "ভুলে যাওয়ার ঠিক আগে শব্দগুলো ফিরে আসে — এভাবেই স্থায়ী হয়।" : "Words come back just before you'd forget them — that's how they stick."}
        </p>
        <Link href="/practice" className={`btn mt-4 w-full text-lg ${learned.length ? "btn-primary" : "btn-ghost pointer-events-none opacity-50"}`}>
          {due.length ? t("startReview") : t("nothingDue")}
        </Link>
        <p className="mt-2 text-xs text-muted">+10 XP · +1 ❤️</p>
      </section>

      <section className="card p-5">
        <div className="mb-3 flex items-baseline justify-between">
          <h2 className="text-lg font-black">{cov.wordsLearned} {t("wordsLearned")}</h2>
          <span className="text-sm font-bold text-gold-dark">{cov.wordsMastered} {t("mastered")}</span>
        </div>
        <div className="flex h-4 overflow-hidden rounded-full bg-line">
          <div className="bg-sky" style={{ width: `${(100 * counts.learning) / total}%` }} />
          <div className="bg-emerald" style={{ width: `${(100 * counts.strong) / total}%` }} />
          <div className="bg-gold" style={{ width: `${(100 * counts.mastered) / total}%` }} />
        </div>
        <div className="mt-2 flex justify-between text-xs font-bold">
          <span className="text-sky">● {lang === "bn" ? "শিখছেন" : "Learning"} {counts.learning}</span>
          <span className="text-emerald">● {lang === "bn" ? "মজবুত" : "Strong"} {counts.strong}</span>
          <span className="text-gold-dark">● {lang === "bn" ? "আয়ত্ত" : "Mastered"} {counts.mastered}</span>
        </div>
        <p className="mt-3 text-xs text-muted">
          {lang === "bn" ? "“আয়ত্ত” = ৩ সপ্তাহ পরেও মনে আছে।" : "“Mastered” = still remembered after 3+ weeks."}
        </p>
      </section>

      {weakest.length > 0 && (
        <section>
          <h2 className="mb-2 px-1 text-sm font-extrabold uppercase tracking-wider text-muted">{lang === "bn" ? "যেগুলো আরও অনুশীলন দরকার" : "Needs the most practice"}</h2>
          <div className="card divide-y-2 divide-line overflow-hidden">
            {weakest.map((k) => {
              const w = WORDS[k];
              return (
                <button key={k} onClick={() => open({ ...tokenPayload({ ar: w.ar.split(" / ")[0], en: w.en, bn: w.bn, key: k, pats: [], audio: w.audio, tr: "", loc: null }) })}
                  className="flex w-full items-center gap-3 px-4 py-2.5 text-left">
                  <Emoji e={w.emoji} className="w-8 text-center text-2xl" />
                  <span className="ar w-24 text-right text-2xl">{w.ar.split(" / ")[0]}</span>
                  <span className={`flex-1 text-sm font-bold ${lang === "bn" ? "bn" : ""}`}>{meaning(w, lang)}</span>
                  <StrengthDots level={strengthLevel(p.items[k])} />
                </button>
              );
            })}
          </div>
        </section>
      )}
    </div>
  );
}
