"use client";
import { useScript } from "@/lib/script";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { BookOpen, BookOpenCheck, Check, Crown, Lock, Puzzle, Star } from "lucide-react";
import { useReadableVerses } from "@/lib/readable";
import { UNITS, WORDS, textById, meaning } from "@/lib/course";
import { useProgress } from "@/lib/store";
import { useAuth } from "@/lib/auth";
import { currentLessonId, isLessonUnlocked, quranCoverage, textUnderstanding, unitProgress } from "@/lib/stats";
import { useT } from "@/lib/i18n";
import { Emoji, Ring, fmtPct } from "@/components/ui";
import { DailyVerse } from "@/components/DailyVerse";
import { useSalahUnderstanding } from "@/lib/salah";

const COLORS = [
  { bg: "bg-emerald", dark: "var(--color-emerald-dark)", hex: "var(--color-emerald)" },
  { bg: "bg-sky", dark: "#1f6fae", hex: "var(--color-sky)" },
  { bg: "bg-plum", dark: "#6d3fd6", hex: "var(--color-plum)" },
  { bg: "bg-gold", dark: "var(--color-gold-dark)", hex: "var(--color-gold)" },
  { bg: "bg-coral", dark: "var(--color-coral-dark)", hex: "var(--color-coral)" },
];
const OFFSETS = [0, 44, 64, 44, 0, -44, -64, -44];

export default function LearnPage() {
  const p = useProgress();
  const { isTeacher } = useAuth();
  const { t, lang } = useT();
  const router = useRouter();
  const { A } = useScript();
  const cov = quranCoverage(p);
  const readable = useReadableVerses();
  const current = currentLessonId(p);
  const currentRef = useRef<HTMLDivElement>(null);
  const [toast, setToast] = useState("");
  const salah = useSalahUnderstanding();

  useEffect(() => {
    if (Object.keys(useProgress.getState().completed).length > 0) currentRef.current?.scrollIntoView({ block: "center", behavior: "smooth" });
  }, []);
  useEffect(() => { if (toast) { const id = setTimeout(() => setToast(""), 1800); return () => clearTimeout(id); } }, [toast]);

  return (
    <div>
      {/* Progress hero */}
      <section className="pattern-bg relative overflow-hidden rounded-3xl p-5 text-white shadow-[0_5px_0_var(--color-emerald-dark)]">
        <div className="flex items-center gap-4">
          <Ring pct={cov.pctLearned} size={92} stroke={9} color="var(--color-gold)" track="rgba(255,255,255,.2)">
            <div className="text-center leading-none">
              <div className="text-2xl font-black">{fmtPct(cov.pctLearned)}%</div>
            </div>
          </Ring>
          <div className="flex-1">
            <div className={`text-sm font-bold text-white/80 ${lang === "bn" ? "bn" : ""}`}>
              {lang === "bn" ? "কুরআনের যত শতাংশ শব্দ আপনি চেনেন" : "of all words in the Quran are words you know"}
            </div>
            <div className="mt-2 flex gap-4 text-sm">
              <div><span className="text-xl font-black">{cov.wordsLearned}</span> <span className="text-white/80">{t("wordsLearned")}</span></div>
            </div>
            <div className="text-sm text-white/80">
              <span className="font-black text-gold">{cov.wordsMastered}</span> {t("mastered")} · {fmtPct(cov.pctMastered)}%
            </div>
            <Link href="/quran#readable" className={`mt-1 inline-flex items-center gap-1 rounded-full bg-white/15 px-2 py-0.5 text-sm font-bold ${lang === "bn" ? "bn" : ""}`}>
              📖 <span className="font-black text-gold">{readable ? readable.count : "…"}</span> {t("versesYouUnderstand")}
            </Link>
          </div>
        </div>
        {current && (
          <button onClick={() => router.push(`/lesson/${current}`)} className="btn btn-gold mt-4 w-full">
            {Object.keys(p.completed).length ? t("continue") : t("start")} →
          </button>
        )}
      </section>

      <DailyVerse />
      <Link href="/salah" className="card mt-4 flex items-center gap-3 p-4" data-testid="salah-link">
        <Ring pct={salah.pct} size={52} stroke={6} color="var(--color-emerald)">
          <span className="text-[13px] font-black">{Math.round(salah.pct)}%</span>
        </Ring>
        <span className="flex-1">
          <span className={`block text-[17px] font-black ${lang === "bn" ? "bn" : ""}`}>🕌 {lang === "bn" ? "নিজের নামাজ বুঝুন" : "Understand your salah"}</span>
          <span className={`block text-[14px] text-muted ${lang === "bn" ? "bn" : ""}`}>{lang === "bn" ? "নামাজের প্রতিটি অংশ, ধাপে ধাপে" : "Every part of the prayer, step by step"}</span>
        </span>
        <span className="text-xl text-muted">›</span>
      </Link>

      {/* Path */}
      <div className="mt-6 space-y-8">
        {UNITS.map((u, ui) => {
          const col = COLORS[ui % COLORS.length];
          const prog = unitProgress(p, u.id);
          const text = textById(u.text)!;
          const done = prog.done === prog.total;
          const und = textUnderstanding(p, u.text);
          return (
            <section key={u.id}>
              <div className={`${col.bg} pattern-soft relative overflow-hidden rounded-3xl p-4 text-white`} style={{ boxShadow: `0 5px 0 ${col.dark}` }}>
                <div className="flex items-center gap-3">
                  <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-white/20 text-3xl"><Emoji e={text.emoji} /></div>
                  <div className="flex-1 min-w-0">
                    <div className="text-xs font-extrabold uppercase tracking-wider text-white/80">{lang === "bn" ? `ইউনিট ${ui + 1}` : `Unit ${ui + 1}`}</div>
                    <div className={`truncate text-lg font-black ${lang === "bn" ? "bn" : ""}`}>{lang === "bn" ? u.bn : u.en}</div>
                    <div className="ar truncate text-lg leading-tight text-white/90">{A(text.ar)}</div>
                  </div>
                  <Link href={`/read/${u.text}`} className="flex flex-col items-center rounded-2xl bg-white/20 px-2.5 py-1.5 text-xs font-extrabold">
                    <BookOpenCheck size={20} />
                    {Math.round(und)}%
                  </Link>
                </div>
                <div className="mt-3 flex flex-wrap gap-1.5">
                  {u.newWords.slice(0, 8).map((k) => (
                    <span key={k} className={`rounded-full px-2 py-0.5 text-xs font-bold ${p.items[k] ? "bg-white text-ink" : "bg-white/15 text-white/90"}`}>
                      <span className="ar">{A(WORDS[k].ar.split(" / ")[0])}</span> {p.items[k] ? meaning(WORDS[k], lang).split(/[,;(]/)[0] : ""}
                    </span>
                  ))}
                  {u.newWords.length > 8 && <span className="rounded-full bg-white/15 px-2 py-0.5 text-xs font-bold">+{u.newWords.length - 8}</span>}
                </div>
              </div>

              <div className="mt-12 flex flex-col items-center gap-5">
                {u.lessons.map((l, li) => {
                  const completed = !!p.completed[l.id];
                  const unlocked = isLessonUnlocked(p, l.id, isTeacher);
                  const isCurrent = l.id === current;
                  const final = l.type === "final";
                  const Icon = final ? Crown : l.type === "structure" ? Puzzle : l.type === "verses" ? BookOpen : Star;
                  const label = l.type === "structure" ? t("makeSentences") : l.type === "verses" ? t("newVerses") : "";
                  const off = OFFSETS[(li + ui * 3) % OFFSETS.length];
                  return (
                    <div key={l.id} ref={isCurrent ? currentRef : undefined} style={{ transform: `translateX(${off}px)` }} className="relative">
                      {isCurrent && (
                        <div className="animate-floaty absolute -top-11 z-10 left-1/2 -translate-x-1/2 whitespace-nowrap rounded-xl border-2 border-line bg-white px-3 py-1 text-sm font-extrabold text-emerald shadow">
                          {t("start")}
                        </div>
                      )}
                      <button
                        onClick={() => (unlocked ? router.push(`/lesson/${l.id}`) : setToast(t("locked")))}
                        aria-label={`Lesson ${li + 1}`}
                        className={`flex h-[70px] w-[70px] items-center justify-center rounded-full text-white transition active:translate-y-1 ${
                          completed ? "bg-gold" : unlocked ? col.bg : "bg-line text-muted"
                        } ${isCurrent ? "ring-8 ring-white" : ""}`}
                        style={{ boxShadow: `0 6px 0 ${completed ? "var(--color-gold-dark)" : unlocked ? col.dark : "#cfc5ae"}` }}
                      >
                        {completed && !final && l.type === "learn" ? <Check size={32} strokeWidth={3.5} /> : unlocked || completed ? <Icon size={30} strokeWidth={2.5} fill={l.type === "learn" ? "currentColor" : "none"} /> : <Lock size={26} />}
                      </button>
                      {label && <div className={`mt-2 text-center text-xs font-extrabold text-muted ${lang === "bn" ? "bn" : ""}`}>{label}</div>}
                    </div>
                  );
                })}
              </div>
              {done && u.completes && (
                <Link href={`/read/${u.completes}`} className="btn btn-ghost mx-auto mt-6 flex w-fit text-emerald">
                  📖 {t("readIt")}
                </Link>
              )}
            </section>
          );
        })}
        <div className="card p-5 text-center text-muted">
          <div className="text-3xl">🌱</div>
          <div className={`mt-1 font-bold ${lang === "bn" ? "bn" : ""}`}>{lang === "bn" ? "আরও ইউনিট আসছে, ইনশাআল্লাহ" : "More units coming, in sha Allah"}</div>
        </div>
      </div>
      {toast && (
        <div className="fixed inset-x-0 bottom-28 z-40 mx-auto w-fit animate-pop rounded-2xl bg-ink px-4 py-2 text-sm font-bold text-white">{toast}</div>
      )}
    </div>
  );
}
