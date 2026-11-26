"use client";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { ChevronRight, Cloud, LogOut, Shield, Trophy } from "lucide-react";
import { useAuth, type Role } from "@/lib/auth";
import { useProgress } from "@/lib/store";
import { badges, liveStreak, quranCoverage, weeklyXp } from "@/lib/stats";
import { useT } from "@/lib/i18n";
import { fmtPct } from "@/components/ui";

export default function ProfilePage() {
  const p = useProgress();
  const auth = useAuth();
  const { t, lang } = useT();
  const router = useRouter();
  const cov = quranCoverage(p);
  const bs = badges(p);
  const bn = lang === "bn" ? "bn" : "";
  const roleLabel = auth.role === "superadmin" ? "Superadmin" : auth.role === "teacher" ? t("teacher") : lang === "bn" ? "শিক্ষার্থী" : "Learner";

  return (
    <div className="space-y-5">
      <section className="card flex items-center gap-4 p-5">
        <div className="flex h-16 w-16 items-center justify-center rounded-full bg-emerald text-3xl font-black text-white">
          {(p.settings.displayName || auth.user?.email || "?").slice(0, 1).toUpperCase()}
        </div>
        <div className="min-w-0 flex-1">
          <div className="truncate text-xl font-black">{p.settings.displayName || auth.user?.email}</div>
          <div className="truncate text-sm text-muted">{auth.demo ? (lang === "bn" ? "ডেমো মোড — এই ডিভাইসে সংরক্ষিত" : "Demo mode — saved on this device") : auth.user?.email}</div>
          <span className={`mt-1 inline-block rounded-full px-2 py-0.5 text-xs font-extrabold ${auth.isTeacher ? "bg-plum/15 text-plum" : "bg-sand text-muted"}`}>{roleLabel}</span>
        </div>
        {!auth.demo && (
          <span title="Sync" className={`text-xs font-bold ${auth.syncState === "error" ? "text-coral" : "text-muted"}`}>
            <Cloud size={18} className="inline" /> {auth.syncState === "saving" ? "…" : auth.syncState === "error" ? "!" : "✓"}
          </span>
        )}
      </section>

      <section className="grid grid-cols-2 gap-3">
        <StatCard emoji="🔥" value={liveStreak(p)} label={t("streak")} sub={`${lang === "bn" ? "সর্বোচ্চ" : "best"} ${p.longestStreak}`} />
        <StatCard emoji="⭐" value={p.xp} label="XP" sub={`${weeklyXp(p)} ${lang === "bn" ? "এই সপ্তাহে" : "this week"}`} />
        <StatCard emoji="📚" value={cov.wordsLearned} label={t("wordsLearned")} sub={`${cov.wordsMastered} ${t("mastered")}`} />
        <StatCard emoji="📖" value={`${fmtPct(cov.pctLearned)}%`} label={t("ofQuran")} sub={`${fmtPct(cov.pctMastered)}% ${t("mastered")}`} />
      </section>

      <section>
        <h2 className="mb-2 px-1 text-sm font-extrabold uppercase tracking-wider text-muted">{t("badges")}</h2>
        <div className="grid grid-cols-3 gap-2">
          {bs.map((b) => (
            <div key={b.id} title={lang === "bn" ? b.hint_bn : b.hint_en} className={`card flex flex-col items-center p-2.5 text-center ${b.earned ? "" : "opacity-40 grayscale"}`}>
              <div className="text-3xl">{b.emoji}</div>
              <div className={`mt-1 text-[11px] font-extrabold leading-tight ${bn}`}>{lang === "bn" ? b.bn : b.en}</div>
            </div>
          ))}
        </div>
      </section>

      <section className="card divide-y-2 divide-line overflow-hidden">
        <Link href="/leaderboard" className="flex items-center gap-3 px-4 py-3 font-bold"><Trophy size={20} className="text-gold-dark" /> <span className="flex-1">{t("leaderboard")}</span><ChevronRight size={18} className="text-muted" /></Link>
        {auth.isAdmin && (
          <Link href="/admin" className="flex items-center gap-3 px-4 py-3 font-bold"><Shield size={20} className="text-plum" /> <span className="flex-1">{lang === "bn" ? "অ্যাডমিন: শিক্ষক নির্ধারণ" : "Admin: manage teachers"}</span><ChevronRight size={18} className="text-muted" /></Link>
        )}
      </section>

      <section className="card space-y-4 p-4">
        <h2 className="text-lg font-black">{t("settings")}</h2>
        <label className="block">
          <span className={`text-sm font-bold text-muted ${bn}`}>{lang === "bn" ? "নাম" : "Display name"}</span>
          <input value={p.settings.displayName} onChange={(e) => p.setSettings({ displayName: e.target.value.slice(0, 40) })}
            className="mt-1 w-full rounded-xl border-2 border-line bg-white px-3 py-2 outline-none focus:border-emerald" />
        </label>
        <div>
          <span className={`text-sm font-bold text-muted ${bn}`}>{t("language")}</span>
          <div className="mt-1 grid grid-cols-2 gap-2">
            {(["en", "bn"] as const).map((l) => (
              <button key={l} onClick={() => p.setSettings({ lang: l })} className={`rounded-xl border-2 py-2 font-extrabold ${p.settings.lang === l ? "border-emerald bg-emerald-light text-emerald-dark" : "border-line bg-white"}`}>
                {l === "en" ? "English" : "বাংলা"}
              </button>
            ))}
          </div>
        </div>
        <div>
          <span className={`text-sm font-bold text-muted ${bn}`}>{lang === "bn" ? "কুরআনের লিপি" : "Quran script"}</span>
          <div className="mt-1 grid grid-cols-2 gap-2">
            {([["indopak", "IndoPak", "بِسْمِ اللّٰهِ"], ["uthmani", "Uthmani", "بِسۡمِ ٱللَّهِ"]] as const).map(([v, label, sample]) => (
              <button key={v} onClick={() => p.setSettings({ script: v })} data-script-option={v}
                className={`rounded-xl border-2 py-1.5 font-extrabold ${(p.settings.script ?? "indopak") === v ? "border-emerald bg-emerald-light text-emerald-dark" : "border-line bg-white"}`}>
                <span className="block text-sm">{label}</span>
                <span className="block text-xl leading-tight" style={{ fontFamily: v === "indopak" ? '"IndoPak Nastaleeq"' : '"Amiri Quran"' }} dir="rtl">{sample}</span>
              </button>
            ))}
          </div>
        </div>
        <div>
          <span className={`text-sm font-bold text-muted ${bn}`}>{t("daily")}</span>
          <div className="mt-1 grid grid-cols-4 gap-2">
            {[10, 20, 30, 50].map((g) => (
              <button key={g} onClick={() => p.setSettings({ dailyGoal: g })} className={`rounded-xl border-2 py-2 text-sm font-extrabold ${p.settings.dailyGoal === g ? "border-gold bg-gold-light" : "border-line bg-white"}`}>{g} XP</button>
            ))}
          </div>
        </div>
        <Toggle label={t("translit")} on={p.settings.translit} set={(v) => p.setSettings({ translit: v })} />
        <Toggle label={t("sound")} on={p.settings.sound} set={(v) => p.setSettings({ sound: v })} />
        <Toggle label={lang === "bn" ? "লিডারবোর্ডে আমাকে দেখান" : "Show me on the leaderboard"} on={p.settings.leaderboard} set={(v) => p.setSettings({ leaderboard: v })} />
      </section>

      {auth.demo && (
        <section className="card space-y-2 p-4">
          <h2 className="font-black">Demo mode</h2>
          <p className="text-sm text-muted">Supabase isn&apos;t connected yet, so there&apos;s no login and progress stays on this device. Switch role to test:</p>
          <div className="grid grid-cols-3 gap-2">
            {(["learner", "teacher", "superadmin"] as Role[]).map((r) => (
              <button key={r} onClick={() => auth.setDemoRole(r)} className={`rounded-xl border-2 py-2 text-sm font-bold ${auth.role === r ? "border-plum bg-plum/10 text-plum" : "border-line bg-white"}`}>{r}</button>
            ))}
          </div>
          <button onClick={() => { if (confirm("Reset all progress on this device?")) useProgress.getState().resetFor("demo"); }} className="text-sm font-bold text-coral">Reset progress</button>
        </section>
      )}

      {!auth.demo && (
        <button onClick={async () => { await auth.signOut(); router.replace("/login"); }} className="btn btn-ghost w-full text-coral"><LogOut size={18} /> {t("signOut")}</button>
      )}

      <section className="px-1 pb-4 text-xs leading-relaxed text-muted">
        <b>Sources.</b> Quran text &amp; translations (Saheeh International, Muhiuddin Khan): tanzil.net. Word-by-word meanings &amp; word audio: quran.com.
        Roots &amp; word forms: Quranic Arabic Corpus (corpus.quran.com). Recitation: Mishary Alafasy (everyayah.com). IndoPak text &amp; “AlQuran IndoPak” font by Ayman Siddiqui (QuranWBW / Quran.com).
        Bangla word meanings and related words were written for this app — please report anything that needs correcting.
      </section>
    </div>
  );
}

function StatCard({ emoji, value, label, sub }: { emoji: string; value: React.ReactNode; label: string; sub?: string }) {
  return (
    <div className="card p-3">
      <div className="flex items-center gap-2"><span className="text-2xl">{emoji}</span><span className="text-2xl font-black">{value}</span></div>
      <div className="text-xs font-bold text-muted">{label}</div>
      {sub && <div className="text-xs text-muted">{sub}</div>}
    </div>
  );
}

function Toggle({ label, on, set }: { label: string; on: boolean; set: (v: boolean) => void }) {
  return (
    <button onClick={() => set(!on)} className="flex w-full items-center justify-between">
      <span className="font-bold">{label}</span>
      <span className={`relative h-7 w-12 rounded-full transition ${on ? "bg-emerald" : "bg-line"}`}>
        <span className={`absolute top-1 h-5 w-5 rounded-full bg-white shadow transition-all ${on ? "left-6" : "left-1"}`} />
      </span>
    </button>
  );
}
