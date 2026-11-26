"use client";
import { Volume2 } from "lucide-react";
import type { Line } from "@/lib/course";
import { playVerse, playWordSequence } from "@/lib/audio";
import { useProgress } from "@/lib/store";
import { tokenPayload, useWordSheet } from "./WordSheet";

/** A verse / phrase where every word is tappable. */
export function ArabicLine({ line, size = "text-3xl", showGloss = false, highlightKnown = false, showTranslation = true, highlightKey }: {
  line: Line; size?: string; showGloss?: boolean; highlightKnown?: boolean; showTranslation?: boolean; highlightKey?: string;
}) {
  const open = useWordSheet();
  const lang = useProgress((s) => s.settings.lang);
  const translit = useProgress((s) => s.settings.translit);
  const items = useProgress((s) => s.items);
  const play = () => (line.verseAudio ? playVerse(line.verseAudio) : playWordSequence(line.tokens.map((t) => t.audio)));
  return (
    <div>
      <div className="flex items-start gap-2">
        <button onClick={play} className="mt-3 shrink-0 rounded-full bg-sky-light p-2 text-sky" aria-label="Play"><Volume2 size={18} /></button>
        <div dir="rtl" className="flex flex-1 flex-wrap gap-x-2 gap-y-1">
          {line.tokens.map((t, i) => {
            const known = highlightKnown && !!items[t.key];
            const hl = highlightKey && t.key === highlightKey;
            return (
              <button key={i} onClick={() => open(tokenPayload(t))}
                className={`rounded-xl px-1 text-center transition hover:bg-gold-light ${hl ? "bg-gold-light ring-2 ring-gold" : known ? "bg-emerald-light/70" : ""}`}>
                <span className={`ar block ${size}`}>{t.ar}</span>
                {translit && t.tr && <span className="block text-[11px] italic text-muted" dir="ltr">{t.tr}</span>}
                {showGloss && <span className={`block max-w-28 text-xs leading-tight text-muted ${lang === "bn" ? "bn" : ""}`} dir="ltr">{lang === "bn" ? t.bn : t.en}</span>}
              </button>
            );
          })}
        </div>
      </div>
      {showTranslation && (
        <p className={`mt-2 text-[15px] leading-relaxed text-ink/80 ${lang === "bn" ? "bn" : ""}`}>
          {lang === "bn" ? line.bn : line.en}
          {line.ref && <span className="ml-2 text-xs font-bold text-muted">{line.ref}</span>}
        </p>
      )}
    </div>
  );
}
