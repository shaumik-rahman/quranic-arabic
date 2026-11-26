"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import { ArrowLeft } from "lucide-react";
import { supabase } from "@/lib/supabase";
import { useAuth } from "@/lib/auth";
import { useProgress } from "@/lib/store";
import { weeklyXp } from "@/lib/stats";
import { useT } from "@/lib/i18n";

interface Row { display_name: string; weekly_xp: number; words_learned: number; is_me: boolean }

export default function LeaderboardPage() {
  const { demo } = useAuth();
  const { t, lang } = useT();
  const p = useProgress();
  const [rows, setRows] = useState<Row[] | null>(null);
  const [err, setErr] = useState("");

  useEffect(() => {
    if (!supabase) return;
    supabase.rpc("get_leaderboard").then(({ data, error }) => {
      if (error) setErr(error.message); else setRows((data as Row[]) || []);
    });
  }, []);

  const me: Row = { display_name: p.settings.displayName || "You", weekly_xp: weeklyXp(p), words_learned: Object.keys(p.items).length, is_me: true };
  const list = demo ? [me] : rows;
  const medal = (i: number) => ["🥇", "🥈", "🥉"][i] ?? `${i + 1}`;

  return (
    <div>
      <Link href="/profile" className="mb-3 inline-flex items-center gap-1 font-bold text-muted"><ArrowLeft size={18} /> {t("profile")}</Link>
      <section className="pattern-bg rounded-3xl p-5 text-center text-white">
        <div className="text-5xl">🏆</div>
        <h1 className="mt-1 text-2xl font-black">{lang === "bn" ? "সাপ্তাহিক লিডারবোর্ড" : "Weekly leaderboard"}</h1>
        <p className="text-sm text-white/80">{lang === "bn" ? "প্রতি সোমবার নতুন করে শুরু হয়" : "Resets every Monday"}</p>
      </section>
      {!p.settings.leaderboard && (
        <div className="mt-4 rounded-2xl bg-gold-light p-3 text-sm">
          {lang === "bn" ? "আপনি লিডারবোর্ডে নেই। " : "You're hidden from the leaderboard. "}
          <button onClick={() => p.setSettings({ leaderboard: true })} className="font-extrabold text-emerald underline">{lang === "bn" ? "যোগ দিন" : "Join"}</button>
        </div>
      )}
      {err && <p className="mt-4 text-sm text-coral">{err}</p>}
      <div className="card mt-4 divide-y-2 divide-line overflow-hidden">
        {!list ? (
          <div className="p-6 text-center text-muted">…</div>
        ) : list.length === 0 ? (
          <div className="p-6 text-center text-muted">{lang === "bn" ? "এখনো কেউ নেই — প্রথম হোন!" : "No one yet — be the first!"}</div>
        ) : (
          list.map((r, i) => (
            <div key={i} className={`flex items-center gap-3 px-4 py-3 ${r.is_me ? "bg-emerald-light" : ""}`}>
              <span className="w-8 text-center text-lg font-black">{medal(i)}</span>
              <span className="flex-1 truncate font-bold">{r.display_name || "—"}</span>
              <span className="text-xs text-muted">{r.words_learned} 📚</span>
              <span className="w-16 text-right font-black text-gold-dark">{r.weekly_xp} XP</span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
