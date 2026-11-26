"use client";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { BookOpen, GraduationCap, Library, RotateCcw, User } from "lucide-react";
import { useAuth } from "@/lib/auth";
import { useProgress, MAX_HEARTS } from "@/lib/store";
import { liveStreak, todayXp, dueItems } from "@/lib/stats";
import { useT, type StrKey } from "@/lib/i18n";
import { Ring } from "./ui";

export function useHydrated() {
  const [h, setH] = useState(false);
  useEffect(() => setH(true), []);
  return h;
}

export function AuthGate({ children }: { children: React.ReactNode }) {
  const { status } = useAuth();
  const router = useRouter();
  const hydrated = useHydrated();
  useEffect(() => { if (status === "signedOut") router.replace("/login"); }, [status, router]);
  if (!hydrated || status !== "signedIn") {
    return (
      <div className="flex min-h-dvh items-center justify-center">
        <div className="h-12 w-12 animate-spin rounded-full border-4 border-line border-t-emerald" />
      </div>
    );
  }
  return <>{children}</>;
}

export function TopBar() {
  const p = useProgress();
  const { isTeacher } = useAuth();
  const { t, lang } = useT();
  const streak = liveStreak(p);
  const goalPct = (100 * todayXp(p)) / p.settings.dailyGoal;
  return (
    <header className="pt-safe sticky top-0 z-30 border-b-2 border-line bg-cream/95 backdrop-blur">
      <div className="mx-auto flex max-w-lg items-center justify-between px-4 py-2">
        <button
          onClick={() => p.setSettings({ lang: lang === "en" ? "bn" : "en" })}
          className="chip px-2.5 py-1 text-sm font-extrabold"
          aria-label={t("language")}
        >
          {lang === "en" ? "EN" : "বাং"}
        </button>
        <div className="flex items-center gap-1 font-extrabold" title={`${streak} ${t("streak")}`}>
          <span className={streak > 0 ? "" : "grayscale opacity-50"}>🔥</span>
          <span className={streak > 0 ? "text-orange-500" : "text-muted"}>{streak}</span>
        </div>
        <div className="flex items-center gap-1 font-extrabold" title={t("daily")}>
          <Ring pct={goalPct} size={30} stroke={4} color="var(--color-gold)">
            <span className="text-[11px]">⭐</span>
          </Ring>
          <span className="text-gold-dark">{todayXp(p)}</span>
        </div>
        <div className="flex items-center gap-1 font-extrabold">
          <span>❤️</span>
          <span className="text-coral">{isTeacher ? "∞" : `${p.hearts}`}</span>
          {!isTeacher && p.hearts < MAX_HEARTS && <span className="text-xs text-muted">/{MAX_HEARTS}</span>}
        </div>
      </div>
    </header>
  );
}

const NAV: { href: string; icon: typeof BookOpen; label: StrKey }[] = [
  { href: "/learn", icon: GraduationCap, label: "learn" },
  { href: "/review", icon: RotateCcw, label: "review" },
  { href: "/quran", icon: BookOpen, label: "quran" },
  { href: "/library", icon: Library, label: "library" },
  { href: "/profile", icon: User, label: "profile" },
];

export function BottomNav() {
  const path = usePathname();
  const { t } = useT();
  const p = useProgress();
  const due = dueItems(p).length;
  return (
    <nav className="pb-safe fixed inset-x-0 bottom-0 z-30 border-t-2 border-line bg-cream/95 backdrop-blur">
      <div className="mx-auto flex max-w-lg justify-around px-2 pt-1.5">
        {NAV.map(({ href, icon: Icon, label }) => {
          const active = path.startsWith(href);
          return (
            <Link key={href} href={href}
              className={`relative flex w-16 flex-col items-center rounded-2xl py-1 text-[11px] font-extrabold ${active ? "bg-emerald-light text-emerald" : "text-muted"}`}>
              <Icon size={24} strokeWidth={active ? 2.6 : 2} />
              {t(label)}
              {href === "/review" && due > 0 && (
                <span className="absolute right-2 top-0 min-w-5 rounded-full bg-coral px-1 text-center text-[10px] leading-5 text-white">{due > 99 ? "99+" : due}</span>
              )}
            </Link>
          );
        })}
      </div>
    </nav>
  );
}
