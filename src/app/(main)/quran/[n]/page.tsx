"use client";
import { useScript } from "@/lib/script";
import Link from "next/link";
import { useParams } from "next/navigation";
import { useEffect, useMemo, useState } from "react";
import { ArrowLeft, ChevronLeft, ChevronRight, Volume2 } from "lucide-react";
import { WORDS, coverage, verseAudioUrl } from "@/lib/course";
import { useProgress } from "@/lib/store";
import { playUrls } from "@/lib/audio";
import { useT } from "@/lib/i18n";
import { useWordSheet } from "@/components/WordSheet";
import { Ring } from "@/components/ui";

type Lemma = [key: string, ar: string, root: string, count: number];
type SurahData = { n: number; verses: { v: number; en: string; bn: string; w: [string, string, string, number, string?][] }[] };

let lemmaCache: Lemma[] | null = null;
async function getLemmas() {
  if (!lemmaCache) lemmaCache = await fetch("/quran/lemmas.json").then((r) => r.json());
  return lemmaCache!;
}

export default function SurahReader() {
  const { n } = useParams<{ n: string }>();
  const num = Number(n);
  const meta = coverage.surahs[num - 1];
  const { lang } = useT();
  const open = useWordSheet();
  const { script } = useScript();
  const items = useProgress((s) => s.items);
  const translit = useProgress((s) => s.settings.translit);
  const [data, setData] = useState<SurahData | null>(null);
  const [lemmas, setLemmas] = useState<Lemma[] | null>(null);
  const [showTr, setShowTr] = useState(true);
  useEffect(() => {
    if (data && typeof window !== "undefined" && window.location.hash) {
      setTimeout(() => document.getElementById(window.location.hash.slice(1))?.scrollIntoView({ block: "center", behavior: "smooth" }), 300);
    }
  }, [data]);

  useEffect(() => {
    setData(null);
    fetch(`/quran/${num}.json`).then((r) => r.json()).then(setData).catch(() => {});
    getLemmas().then(setLemmas).catch(() => {});
  }, [num]);

  const stats = useMemo(() => {
    if (!data || !lemmas) return { pct: 0, known: 0, total: 0 };
    let total = 0, known = 0;
    for (const v of data.verses) for (const w of v.w) { total++; if (items[lemmas[w[3]][0]]) known++; }
    return { pct: (100 * known) / Math.max(1, total), known, total };
  }, [data, lemmas, items]);

  if (!meta) return <p>Not found</p>;
  const pad = (x: number) => String(x).padStart(3, "0");

  return (
    <div>
      <div className="mb-3 flex items-center justify-between">
        <Link href="/quran" className="inline-flex items-center gap-1 font-bold text-muted"><ArrowLeft size={18} /> {lang === "bn" ? "সব সূরা" : "All surahs"}</Link>
        <div className="flex gap-2">
          {num > 1 && <Link href={`/quran/${num - 1}`} className="chip p-1.5"><ChevronLeft size={18} /></Link>}
          {num < 114 && <Link href={`/quran/${num + 1}`} className="chip p-1.5"><ChevronRight size={18} /></Link>}
        </div>
      </div>
      <section className="card flex items-center gap-4 p-4">
        <Ring pct={stats.pct} size={64} stroke={7}>
          <span className="text-sm font-black text-emerald">{Math.round(stats.pct)}%</span>
        </Ring>
        <div className="flex-1">
          <div className="text-lg font-black">{meta.n}. {meta.tr}</div>
          <div className={`text-sm text-muted ${lang === "bn" ? "bn" : ""}`}>{lang === "bn" ? meta.bn : meta.en} · {meta.verses} {lang === "bn" ? "আয়াত" : "verses"}</div>
          <div className={`text-xs font-bold text-emerald ${lang === "bn" ? "bn" : ""}`}>
            {lang === "bn" ? `${stats.total} শব্দের ${stats.known}টি আপনি চেনেন` : `You know ${stats.known} of ${stats.total} words`}
          </div>
        </div>
        <div className="ar text-3xl">{meta.ar}</div>
      </section>
      <div className="mt-3 flex gap-2">
        <button onClick={() => data && playUrls(data.verses.map((v) => verseAudioUrl(pad(num) + pad(v.v))))} className="btn btn-gold flex-1 py-2.5"><Volume2 size={18} /> {lang === "bn" ? "শুনুন" : "Listen"}</button>
        <button onClick={() => setShowTr(!showTr)} className="btn btn-ghost py-2.5 text-sm">{showTr ? (lang === "bn" ? "অনুবাদ লুকান" : "Hide translation") : (lang === "bn" ? "অনুবাদ দেখান" : "Show translation")}</button>
      </div>

      {num !== 1 && num !== 9 && <div className="ar mt-6 text-center text-3xl text-emerald">{script === "indopak" ? "بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِیْمِ" : "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ"}</div>}

      {!data || !lemmas ? (
        <div className="mt-10 flex justify-center"><div className="h-10 w-10 animate-spin rounded-full border-4 border-line border-t-emerald" /></div>
      ) : (
        <div className="mt-4 space-y-3">
          {data.verses.map((v) => (
            <div key={v.v} id={`v${v.v}`} className="card scroll-mt-20 p-4">
              <div className="flex items-start gap-2">
                <button onClick={() => playUrls([verseAudioUrl(pad(num) + pad(v.v))])} className="mt-2 flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-sand text-xs font-black text-muted">{v.v}</button>
                <div dir="rtl" className="flex flex-1 flex-wrap gap-x-1.5 gap-y-1">
                  {v.w.map((w, i) => {
                    const [key, lar, root, count] = lemmas[w[3]];
                    const known = !!items[key];
                    const loc = `${pad(num)}_${pad(v.v)}_${pad(i + 1)}`;
                    return (
                      <button key={i}
                        onClick={() => open({ ar: w[0], ip: w[4] || null, en: w[1], bn: undefined, tr: w[2], key: WORDS[key] ? key : undefined, audio: loc, lemma: { ar: lar, root, count } })}
                        className={`rounded-lg px-1 transition ${known ? "bg-emerald-light text-emerald-dark" : "hover:bg-gold-light"}`}>
                        <span className="ar block text-[28px]">{script === "indopak" && w[4] ? w[4] : w[0]}</span>
                        {translit && <span className="block text-[10px] italic text-muted" dir="ltr">{w[2]}</span>}
                      </button>
                    );
                  })}
                </div>
              </div>
              {showTr && <p className={`mt-2 text-sm leading-relaxed text-ink/75 ${lang === "bn" ? "bn" : ""}`}>{lang === "bn" ? v.bn : v.en}</p>}
            </div>
          ))}
          <p className="pt-2 text-center text-xs text-muted">
            {lang === "bn" ? "অনুবাদ: মুহিউদ্দীন খান" : "Translation: Saheeh International"} · {lang === "bn" ? "শব্দার্থ: quran.com (ইংরেজি)" : "Word meanings: quran.com"}
          </p>
        </div>
      )}
    </div>
  );
}
