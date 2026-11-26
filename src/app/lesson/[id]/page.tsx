"use client";
import { useScript } from "@/lib/script";
import Link from "next/link";
import { useParams, useRouter } from "next/navigation";
import { useState } from "react";
import { AuthGate } from "@/components/AppShell";
import { LessonPlayer, Modal, type FinishInfo } from "@/components/LessonPlayer";
import { buildLesson, type Step } from "@/lib/exercises";
import { LESSON_INDEX, WORDS, lessonById, meaning, textById, unitById } from "@/lib/course";
import { snapshot, useProgress } from "@/lib/store";
import { useAuth } from "@/lib/auth";
import { isLessonUnlocked, quranCoverage, textUnderstanding } from "@/lib/stats";
import { useT } from "@/lib/i18n";
import { Emoji, fmtPct } from "@/components/ui";

export default function LessonPage() {
  return <AuthGate><LessonInner /></AuthGate>;
}

function LessonInner() {
  const { id } = useParams<{ id: string }>();
  const router = useRouter();
  const { t, lang } = useT();
  const { isTeacher } = useAuth();
  const { A } = useScript();
  const valid = id in LESSON_INDEX;
  const [steps] = useState<Step[]>(() => (valid ? buildLesson(id, snapshot()) : []));
  const [before] = useState(() => quranCoverage(snapshot()).pctLearned);
  const hearts = useProgress((s) => s.hearts);

  if (!valid) return <div className="p-8 text-center">Lesson not found. <Link href="/learn" className="text-emerald underline">Back</Link></div>;
  const lesson = lessonById(id);
  const unit = unitById(lesson.unitId);
  if (!isLessonUnlocked(snapshot(), id, isTeacher)) {
    return <Modal><div className="text-5xl">🔒</div><p className="mt-2 font-bold">{t("locked")}</p><Link href="/learn" className="btn btn-primary mt-4 w-full">{t("backHome")}</Link></Modal>;
  }
  if (!isTeacher && hearts <= 0) {
    return (
      <Modal>
        <div className="text-6xl">💔</div>
        <h3 className="mt-2 text-2xl font-black">{t("outOfHearts")}</h3>
        <p className="mt-1 text-muted">{t("outOfHeartsBody")}</p>
        <button onClick={() => router.replace("/practice")} className="btn btn-primary mt-5 w-full">{t("practiceEarn")}</button>
        <Link href="/learn" className="btn btn-ghost mt-3 w-full">{t("backHome")}</Link>
      </Modal>
    );
  }

  const xpFor = (info: FinishInfo) => (lesson.type === "final" ? 20 : lesson.type === "verses" ? 15 : 10) + (info.mistakes === 0 ? 5 : 0);
  const onFinish = (info: FinishInfo) => {
    const st = useProgress.getState();
    st.completeLesson(id, info.mistakes === 0);
    st.addXp(xpFor(info));
  };

  const renderDone = (info: FinishInfo) => {
    const p = snapshot();
    const after = quranCoverage(p).pctLearned;
    const completesText = lesson.type === "final" && unit.completes ? textById(unit.completes) : null;
    const newWords = info.newItems.filter((k) => WORDS[k]);
    const acc = Math.round((100 * Math.max(0, info.graded - info.mistakes)) / Math.max(1, info.graded));
    return (
      <div className="pattern-soft flex min-h-dvh flex-col items-center px-5 pb-10 pt-safe text-center">
        <div className="mx-auto w-full max-w-md flex-1 pt-10">
          <div className="animate-pop text-7xl">{completesText ? completesText.emoji : "🎉"}</div>
          <h1 className={`mt-3 text-3xl font-black text-emerald ${lang === "bn" ? "bn" : ""}`}>
            {completesText ? t("unitDone") : lesson.type === "verses" ? (lang === "bn" ? "মা শা আল্লাহ!" : "Masha'Allah!") : t("lessonDone")}
          </h1>
          {lesson.type === "verses" && (
            <p className={`mt-2 text-lg font-bold ${lang === "bn" ? "bn" : ""}`}>
              {lang === "bn" ? `আপনি ${unit.newVerses.length}টি আয়াত বুঝলেন যা কেউ আপনাকে শেখায়নি।` : `You just understood ${unit.newVerses.length} verses nobody taught you.`}
            </p>
          )}
          {lesson.type === "structure" && (
            <p className={`mt-2 text-lg font-bold ${lang === "bn" ? "bn" : ""}`}>
              {lang === "bn" ? "আপনি নিজেই আরবি বাক্য বানালেন!" : "You built Arabic sentences yourself!"}
            </p>
          )}
          {completesText && (
            <p className={`mt-2 text-lg font-bold ${lang === "bn" ? "bn" : ""}`}>
              {lang === "bn"
                ? `${completesText.bn}-এর ${Math.round(textUnderstanding(p, completesText.id))}% শব্দ এখন আপনি বোঝেন।`
                : `You now understand ${Math.round(textUnderstanding(p, completesText.id))}% of the words in ${completesText.en}.`}
            </p>
          )}
          <div className="mt-6 grid grid-cols-3 gap-3">
            <Stat label="XP" value={`+${xpFor(info)}`} color="text-gold-dark" />
            <Stat label={lang === "bn" ? "নির্ভুল" : "Accuracy"} value={`${acc}%`} color="text-emerald" />
            <Stat label={lang === "bn" ? "কুরআন" : "Quran"} value={`${fmtPct(after)}%`} color="text-sky" sub={after > before ? `+${fmtPct(after - before)}%` : undefined} />
          </div>
          {newWords.length > 0 && (
            <div className="card mt-5 p-4 text-left">
              <div className="mb-2 text-xs font-extrabold uppercase tracking-wider text-muted">{lang === "bn" ? "নতুন শেখা শব্দ" : "Words you learned"}</div>
              <div className="space-y-1.5">
                {newWords.map((k) => (
                  <div key={k} className="flex items-center gap-3">
                    <Emoji e={WORDS[k].emoji} className="w-8 text-center text-2xl" />
                    <span className="ar text-2xl">{A(WORDS[k].ar.split(" / ")[0])}</span>
                    <span className={`flex-1 text-sm font-bold ${lang === "bn" ? "bn" : ""}`}>{meaning(WORDS[k], lang)}</span>
                    <span className="text-xs text-muted">{WORDS[k].count}×</span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
        <div className="mx-auto mt-6 w-full max-w-md space-y-3">
          {completesText && <Link href={`/read/${completesText.id}`} className="btn btn-gold w-full text-lg">📖 {t("readIt")}</Link>}
          <Link href="/learn" className="btn btn-primary w-full text-lg">{t("continue")}</Link>
        </div>
      </div>
    );
  };

  return <LessonPlayer steps={steps} mode="lesson" onFinish={onFinish} renderDone={renderDone} />;
}

function Stat({ label, value, color, sub }: { label: string; value: string; color: string; sub?: string }) {
  return (
    <div className="card p-3">
      <div className="text-xs font-extrabold uppercase text-muted">{label}</div>
      <div className={`text-2xl font-black ${color}`}>{value}</div>
      {sub && <div className="text-xs font-bold text-emerald">{sub}</div>}
    </div>
  );
}
