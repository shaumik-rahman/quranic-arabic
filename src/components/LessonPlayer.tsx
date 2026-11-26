"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { X } from "lucide-react";
import confetti from "canvas-confetti";
import { isGraded, type Step } from "@/lib/exercises";
import { useProgress } from "@/lib/store";
import { useAuth } from "@/lib/auth";
import { sfx, stopAudio } from "@/lib/audio";
import { DEMO_MODE } from "@/lib/supabase";
import { useT } from "@/lib/i18n";
import { Bar } from "./ui";
import {
  ArrangeEx, BreakdownEx, BuildEx, CheckEx, FillEx, IntroEx, MatchEx, McqEx, MeaningEx, PatternEx, PatternQEx, ReadEx, SpotEx, StructureEx, type Evaluate, type Pager,
} from "./exercises/Exercises";

export interface FinishInfo { mistakes: number; graded: number; newItems: string[] }

export function LessonPlayer({ steps: initial, mode, onFinish, renderDone }: {
  steps: Step[];
  mode: "lesson" | "practice";
  onFinish: (info: FinishInfo) => void;
  renderDone: (info: FinishInfo) => React.ReactNode;
}) {
  const router = useRouter();
  const { t } = useT();
  const { isTeacher } = useAuth();
  const hearts = useProgress((s) => s.hearts);
  const [queue, setQueue] = useState<Step[]>(initial);
  const [i, setI] = useState(0);
  const [ready, setReady] = useState(false);
  const [feedback, setFeedback] = useState<null | { correct: boolean; answer: React.ReactNode; why?: React.ReactNode }>(null);
  const [pager, setPager] = useState<Pager | null>(null);
  const [mistakes, setMistakes] = useState(0);
  const [finished, setFinished] = useState<FinishInfo | null>(null);
  const [outOfHearts, setOutOfHearts] = useState(false);
  const [confirmQuit, setConfirmQuit] = useState(false);
  const evalRef = useRef<Evaluate | null>(null);
  const graded = useRef(new Set<string>());
  const learnedNow = useRef(new Set<string>());
  const totalGraded = initial.filter(isGraded).length || 1;
  const [doneGraded, setDoneGraded] = useState(0);

  const step = queue[i];
  const setEvaluate = useCallback((fn: Evaluate | null) => { evalRef.current = fn; setReady(!!fn); }, []);

  useEffect(() => {
    // remember which items were new in this session (they shouldn't be graded the same day)
    if (step?.kind === "intro") learnedNow.current.add(step.word);
    if (step?.kind === "pattern") learnedNow.current.add("p:" + step.pattern);
    setReady(false); evalRef.current = null;
  }, [step]);
  useEffect(() => () => stopAudio(), []);

  const grade = (item: string | undefined, correct: boolean) => {
    if (!item || learnedNow.current.has(item)) return;
    if (graded.current.has(item)) return;
    graded.current.add(item);
    if (useProgress.getState().items[item]) useProgress.getState().answer(item, correct);
  };

  const finish = (m: number) => {
    const info: FinishInfo = { mistakes: m, graded: totalGraded, newItems: Array.from(learnedNow.current) };
    sfx("complete");
    confetti({ particleCount: 120, spread: 80, origin: { y: 0.6 }, colors: ["#0e7c66", "#f6be3b", "#2f8fd8", "#e5534b"] });
    onFinish(info);
    setFinished(info);
  };

  const advance = () => {
    setFeedback(null);
    if (outOfHeartsPending.current) { setOutOfHearts(true); return; }
    if (i + 1 >= queue.length) finish(mistakes);
    else setI(i + 1);
  };
  const outOfHeartsPending = useRef(false);

  const check = () => {
    const fn = evalRef.current;
    if (!fn) return;
    const r = fn();
    setFeedback(r);
    grade(step.item, r.correct);
    if (r.correct) {
      sfx("correct");
      setDoneGraded((d) => d + 1);
    } else {
      sfx("wrong");
      setMistakes((m) => m + 1);
      // it comes back at the end (a check comes back with its options in a new order)
      const again = step.kind === "check" ? { ...step, order: [...step.order].sort(() => Math.random() - 0.5) } : step;
      setQueue((q) => [...q, { ...again, id: step.id + "r" }]);
      // a check right after teaching is for understanding: it comes back later, but costs no heart
      if (mode === "lesson" && !isTeacher && step.kind !== "check") {
        useProgress.getState().loseHeart();
        if (useProgress.getState().hearts <= 0) outOfHeartsPending.current = true;
      }
    }
  };

  const selfDone = (correct: boolean) => {
    // intro / pattern (continue) and match (finishes itself)
    if (step.kind === "match") {
      step.words.forEach((w) => grade(w, correct));
      setDoneGraded((d) => d + 1);
      if (!correct) setMistakes((m) => m + 1);
    }
    if (i + 1 >= queue.length) finish(mistakes + (step.kind === "match" && !correct ? 1 : 0));
    else setI(i + 1);
  };

  // test helper — only in demo mode with localStorage "qa-debug" = "1"
  const debug = DEMO_MODE && typeof window !== "undefined" && localStorage.getItem("qa-debug") === "1";
  const debugPass = () => {
    if (step.kind === "intro" || step.kind === "pattern" || step.kind === "match" || step.kind === "structure" || step.kind === "read" || step.kind === "breakdown") return selfDone(true);
    setFeedback({ correct: true, answer: "" }); setDoneGraded((d) => d + 1); grade(step.item, true);
  };

  if (finished) return <>{renderDone(finished)}</>;
  if (!step) return null;

  const pct = (100 * doneGraded) / totalGraded;
  const props = { setEvaluate, locked: !!feedback, onDone: selfDone, setPager } as const;
  const selfContinue = step.kind === "intro" || step.kind === "pattern" || step.kind === "structure" || step.kind === "read" || step.kind === "breakdown";

  return (
    <div className="flex min-h-dvh flex-col bg-cream">
      <div className="pt-safe mx-auto flex w-full max-w-lg items-center gap-3 px-4 py-3">
        <button onClick={() => setConfirmQuit(true)} className="shrink-0 text-muted" aria-label="Quit"><X size={28} /></button>
        <Bar pct={pct} className="h-4" />
        {mode === "lesson" && <div className="flex shrink-0 items-center gap-1 whitespace-nowrap font-extrabold text-coral">❤️ {isTeacher ? "∞" : hearts}</div>}
        {debug && !feedback && <button data-testid="debug-pass" onClick={debugPass} className="rounded bg-plum px-2 text-xs text-white">auto</button>}
      </div>

      <div key={step.id} data-kind={step.kind} className="mx-auto w-full max-w-lg flex-1 px-4 pb-44 pt-2">
        {step.kind === "intro" && <IntroEx step={step} {...props} />}
        {step.kind === "pattern" && <PatternEx step={step} {...props} />}
        {step.kind === "mcq" && <McqEx step={step} {...props} />}
        {step.kind === "patternq" && <PatternQEx step={step} {...props} />}
        {step.kind === "spot" && <SpotEx step={step} {...props} />}
        {step.kind === "fill" && <FillEx step={step} {...props} />}
        {step.kind === "match" && <MatchEx step={step} {...props} />}
        {step.kind === "build" && <BuildEx step={step} {...props} />}
        {step.kind === "meaning" && <MeaningEx step={step} {...props} />}
        {step.kind === "structure" && <StructureEx step={step} {...props} />}
        {step.kind === "breakdown" && <BreakdownEx step={step} {...props} />}
        {step.kind === "arrange" && <ArrangeEx step={step} {...props} />}
        {step.kind === "read" && <ReadEx step={step} {...props} />}
        {step.kind === "check" && <CheckEx step={step} {...props} />}
      </div>

      {/* footer */}
      {step.kind !== "match" && (
        <div className={`pb-safe fixed inset-x-0 bottom-0 z-20 border-t-2 ${feedback ? (feedback.correct ? "border-emerald/30 bg-emerald-light" : "border-coral/30 bg-coral-light") : "border-line bg-cream"}`}>
          <div className="mx-auto max-w-lg px-4 py-4">
            {feedback && (
              <div className="mb-3 animate-pop">
                <div className={`text-xl font-black ${feedback.correct ? "text-emerald-dark" : "text-coral-dark"}`}>
                  {feedback.correct ? `✅ ${t("correct")}` : `${t("wrong")}`}
                </div>
                {!feedback.correct && <div className="mt-1 text-coral-dark"><b>{t("answer")}:</b> {feedback.answer}</div>}
                {feedback.why && <div className={`mt-1 text-[16px] leading-snug ${feedback.correct ? "text-emerald-dark" : "text-coral-dark"}`}>💡 {feedback.why}</div>}
              </div>
            )}
            {selfContinue ? (
              pager && pager.at < pager.total - 1 ? (
                <button onClick={pager.next} className="btn btn-primary w-full text-lg">{t("next")} → <span className="ml-1 text-sm opacity-80">{pager.at + 1}/{pager.total}</span></button>
              ) : (
                <button onClick={() => selfDone(true)} className="btn btn-primary w-full text-lg">{t("continue")}</button>
              )
            ) : feedback ? (
              <button onClick={advance} className={`btn w-full text-lg ${feedback.correct ? "btn-primary" : "btn-coral"}`}>{t("continue")}</button>
            ) : (
              <button onClick={check} disabled={!ready} className="btn btn-primary w-full text-lg">{t("check")}</button>
            )}
          </div>
        </div>
      )}

      {outOfHearts && (
        <Modal>
          <div className="text-6xl">💔</div>
          <h3 className="mt-2 text-2xl font-black">{t("outOfHearts")}</h3>
          <p className="mt-1 text-muted">{t("outOfHeartsBody")}</p>
          <button onClick={() => router.replace("/practice")} className="btn btn-primary mt-5 w-full">{t("practiceEarn")}</button>
          <button onClick={() => router.replace("/learn")} className="btn btn-ghost mt-3 w-full">{t("backHome")}</button>
        </Modal>
      )}
      {confirmQuit && (
        <Modal>
          <div className="text-5xl">🥺</div>
          <h3 className="mt-2 text-2xl font-black">{t("quit")}</h3>
          <p className="mt-1 text-muted">{t("quitBody")}</p>
          <button onClick={() => setConfirmQuit(false)} className="btn btn-primary mt-5 w-full">{t("keepGoing")}</button>
          <button onClick={() => router.replace("/learn")} className="btn btn-ghost mt-3 w-full text-coral">{t("quitYes")}</button>
        </Modal>
      )}
    </div>
  );
}

export function Modal({ children }: { children: React.ReactNode }) {
  return (
    <div className="fixed inset-0 z-50 flex items-end justify-center bg-black/40 sm:items-center">
      <div className="pb-safe animate-slideup w-full max-w-md rounded-t-3xl bg-cream p-6 text-center sm:rounded-3xl">{children}</div>
    </div>
  );
}
