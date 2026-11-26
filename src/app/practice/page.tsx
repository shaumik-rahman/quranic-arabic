"use client";
import Link from "next/link";
import { useState } from "react";
import { AuthGate } from "@/components/AppShell";
import { LessonPlayer, type FinishInfo } from "@/components/LessonPlayer";
import { buildPractice, type Step } from "@/lib/exercises";
import { snapshot, useProgress } from "@/lib/store";
import { useT } from "@/lib/i18n";

export default function PracticePage() {
  return <AuthGate><Inner /></AuthGate>;
}

function Inner() {
  const { t, lang } = useT();
  const [steps] = useState<Step[]>(() => buildPractice(snapshot()));
  if (!steps.length) {
    return (
      <div className="flex min-h-dvh flex-col items-center justify-center p-8 text-center">
        <div className="text-6xl">🌱</div>
        <p className="mt-3 text-lg font-bold">{lang === "bn" ? "প্রথমে কিছু শব্দ শিখুন!" : "Learn a few words first!"}</p>
        <Link href="/learn" className="btn btn-primary mt-5">{t("backHome")}</Link>
      </div>
    );
  }
  const onFinish = () => {
    const st = useProgress.getState();
    st.addXp(10);
    st.gainHearts(1);
  };
  const renderDone = (info: FinishInfo) => (
    <div className="pattern-soft flex min-h-dvh flex-col items-center justify-center px-6 text-center">
      <div className="animate-pop text-7xl">💪</div>
      <h1 className="mt-3 text-3xl font-black text-emerald">{t("great")}</h1>
      <p className={`mt-2 text-lg ${lang === "bn" ? "bn" : ""}`}>
        +10 XP · +1 ❤️ · {Math.round((100 * Math.max(0, info.graded - info.mistakes)) / Math.max(1, info.graded))}%
      </p>
      <div className="mt-8 w-full max-w-sm space-y-3">
        <Link href="/learn" className="btn btn-primary w-full text-lg">{t("continue")}</Link>
        <Link href="/review" className="btn btn-ghost w-full">{t("review")}</Link>
      </div>
    </div>
  );
  return <LessonPlayer steps={steps} mode="practice" onFinish={onFinish} renderDone={renderDone} />;
}
