"use client";
import Link from "next/link";
import { useParams } from "next/navigation";
import { ArrowLeft, Volume2 } from "lucide-react";
import { textById } from "@/lib/course";
import { useProgress } from "@/lib/store";
import { textUnderstanding } from "@/lib/stats";
import { playUrls } from "@/lib/audio";
import { verseAudioUrl, wordAudioUrl } from "@/lib/course";
import { useT } from "@/lib/i18n";
import { ArabicLine } from "@/components/ArabicLine";
import { Emoji, Ring } from "@/components/ui";

export default function ReadPage() {
  const { id } = useParams<{ id: string }>();
  const p = useProgress();
  const { lang } = useT();
  const text = textById(id);
  if (!text) return <p>Not found</p>;
  const und = textUnderstanding(p, text.id);
  const playAll = () =>
    playUrls(text.lines.flatMap((l) => (l.verseAudio ? [verseAudioUrl(l.verseAudio)] : l.tokens.filter((t) => t.audio).map((t) => wordAudioUrl(t.audio!)))));
  return (
    <div>
      <Link href="/learn" className="mb-3 inline-flex items-center gap-1 font-bold text-muted"><ArrowLeft size={18} /> {lang === "bn" ? "ফিরে যান" : "Back"}</Link>
      <section className="pattern-bg rounded-3xl p-5 text-white shadow-[0_5px_0_var(--color-emerald-dark)]">
        <div className="flex items-center gap-4">
          <Emoji e={text.emoji} className="text-5xl" />
          <div className="flex-1">
            <div className="ar text-3xl leading-tight">{text.ar}</div>
            <div className={`text-lg font-black ${lang === "bn" ? "bn" : ""}`}>{lang === "bn" ? text.bn : text.en}</div>
            <div className={`text-sm text-white/80 ${lang === "bn" ? "bn" : ""}`}>{lang === "bn" ? text.desc_bn : text.desc_en}</div>
          </div>
          <Ring pct={und} size={64} stroke={7} color="var(--color-gold)" track="rgba(255,255,255,.2)">
            <span className="text-sm font-black">{Math.round(und)}%</span>
          </Ring>
        </div>
        <button onClick={playAll} className="btn btn-gold mt-4 w-full py-2.5"><Volume2 size={18} /> {lang === "bn" ? "শুনুন" : "Listen"}</button>
      </section>
      <p className={`mt-4 px-1 text-sm text-muted ${lang === "bn" ? "bn" : ""}`}>
        {lang === "bn" ? "যেকোনো শব্দে ট্যাপ করুন। সবুজ = আপনি জানেন।" : "Tap any word. Green = a word you know."}
      </p>
      <div className="mt-3 space-y-4">
        {text.lines.map((l) => (
          <div key={l.id} className="card p-4">
            <ArabicLine line={l} size="text-[32px]" highlightKnown showGloss />
            {(l.note_en || l.note_bn) && <p className={`mt-1 text-xs font-bold text-gold-dark ${lang === "bn" ? "bn" : ""}`}>💡 {lang === "bn" ? l.note_bn : l.note_en}</p>}
          </div>
        ))}
      </div>
      <p className="mt-6 text-center text-xs text-muted">
        {lang === "bn" ? "অনুবাদ: মুহিউদ্দীন খান (tanzil.net)" : "Translation: Saheeh International (tanzil.net)"} · {lang === "bn" ? "তিলাওয়াত" : "Recitation"}: Mishary Alafasy
      </p>
    </div>
  );
}
