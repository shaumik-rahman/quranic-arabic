"use client";
import { useScript } from "@/lib/script";
import { useMemo, useState } from "react";
import { Search } from "lucide-react";
import { PATTERNS, UNITS, WORDS, WORD_ORDER, meaning, PATTERN_UNIT, WORD_UNIT } from "@/lib/course";
import { useProgress } from "@/lib/store";
import { useAuth } from "@/lib/auth";
import { strengthLevel } from "@/lib/srs";
import { useT } from "@/lib/i18n";
import { playWord } from "@/lib/audio";
import { Emoji, StrengthDots } from "@/components/ui";
import { useWordSheet } from "@/components/WordSheet";

type Sort = "path" | "freq" | "root" | "weak";

export default function LibraryPage() {
  const p = useProgress();
  const { isTeacher } = useAuth();
  const { t, lang } = useT();
  const open = useWordSheet();
  const { A, T } = useScript();
  const [tab, setTab] = useState<"words" | "patterns">("words");
  const [q, setQ] = useState("");
  const [sort, setSort] = useState<Sort>("path");
  const [showAll, setShowAll] = useState(false);

  const visible = (k: string) => showAll || !!p.items[k];
  const words = useMemo(() => {
    let ks = WORD_ORDER.filter((k) => showAll || p.items[k]);
    const needle = q.trim().toLowerCase();
    if (needle) ks = ks.filter((k) => { const w = WORDS[k]; return w.en.toLowerCase().includes(needle) || w.bn.includes(needle) || (w.ar.includes(needle) || A(w.ar).includes(needle)) || w.root.includes(needle) || w.lemma.includes(needle); });
    if (sort === "freq") ks = [...ks].sort((a, b) => WORDS[b].count - WORDS[a].count);
    if (sort === "root") ks = [...ks].sort((a, b) => (WORDS[a].root || "ي").localeCompare(WORDS[b].root || "ي", "ar"));
    if (sort === "weak") ks = [...ks].sort((a, b) => (p.items[a]?.interval ?? -1) - (p.items[b]?.interval ?? -1));
    return ks;
  }, [p.items, q, sort, showAll]);

  const pats = Object.keys(PATTERNS).filter((id) => PATTERN_UNIT[id] && visible("p:" + id))
    .sort((a, b) => UNITS.findIndex((u) => u.id === PATTERN_UNIT[a]) - UNITS.findIndex((u) => u.id === PATTERN_UNIT[b]));
  const unitNo = (uid: string) => UNITS.findIndex((u) => u.id === uid) + 1;

  return (
    <div>
      <div className="mb-4 grid grid-cols-2 gap-2 rounded-2xl bg-sand p-1">
        {(["words", "patterns"] as const).map((x) => (
          <button key={x} onClick={() => setTab(x)} className={`rounded-xl py-2 font-extrabold ${tab === x ? "bg-white shadow" : "text-muted"}`}>
            {t(x)} <span className="text-muted">({x === "words" ? Object.keys(p.items).filter((k) => WORDS[k]).length : Object.keys(p.items).filter((k) => k.startsWith("p:")).length})</span>
          </button>
        ))}
      </div>

      {tab === "words" && (
        <>
          <div className="mb-3 flex items-center gap-2 rounded-2xl border-2 border-line bg-white px-3">
            <Search size={18} className="text-muted" />
            <input value={q} onChange={(e) => setQ(e.target.value)} placeholder={t("search")} className="w-full bg-transparent py-2.5 outline-none" />
          </div>
          <div className="no-scrollbar mb-3 flex gap-2 overflow-x-auto">
            {([["path", lang === "bn" ? "পাঠক্রম" : "Path order"], ["freq", lang === "bn" ? "বেশি ব্যবহৃত" : "Most frequent"], ["root", lang === "bn" ? "রুট" : "By root"], ["weak", lang === "bn" ? "দুর্বল" : "Weakest"]] as [Sort, string][]).map(([k, label]) => (
              <button key={k} onClick={() => setSort(k)} className={`shrink-0 rounded-full border-2 px-3 py-1 text-sm font-bold ${sort === k ? "border-emerald bg-emerald-light text-emerald-dark" : "border-line bg-white text-muted"}`}>{label}</button>
            ))}
            {isTeacher && (
              <button onClick={() => setShowAll(!showAll)} className={`shrink-0 rounded-full border-2 px-3 py-1 text-sm font-bold ${showAll ? "border-plum bg-plum/10 text-plum" : "border-line bg-white text-muted"}`}>
                {lang === "bn" ? "সব দেখান" : "Show all"}
              </button>
            )}
          </div>
          {words.length === 0 ? (
            <Empty lang={lang} />
          ) : (
            <div className="card divide-y-2 divide-line overflow-hidden">
              {words.map((k) => {
                const w = WORDS[k];
                return (
                  <button key={k} onClick={() => open({ ar: w.ar.split(" / ")[0], ip: A(w.ar.split(" / ")[0]), en: w.en, bn: w.bn, key: k, audio: w.audio })}
                    className="flex w-full items-center gap-3 px-3 py-2.5 text-left">
                    <Emoji e={w.emoji} className="w-8 text-center text-2xl" />
                    <div className="w-24 text-right"><span className="ar text-2xl">{A(w.ar.split(" / ")[0])}</span></div>
                    <div className="min-w-0 flex-1">
                      <div className={`truncate text-sm font-bold ${lang === "bn" ? "bn" : ""}`}>{meaning(w, lang)}</div>
                      <div className="text-xs text-muted">
                        {w.root && <><bdi className="ar">{w.rootSpaced}</bdi> · </>}{w.count}× · {lang === "bn" ? "ইউনিট" : "Unit"} {unitNo(WORD_UNIT[k])}
                      </div>
                    </div>
                    <StrengthDots level={strengthLevel(p.items[k])} />
                  </button>
                );
              })}
            </div>
          )}
        </>
      )}

      {tab === "patterns" && (
        pats.length === 0 ? <Empty lang={lang} /> : (
          <div className="space-y-3">
            <p className={`px-1 text-sm text-muted ${lang === "bn" ? "bn" : ""}`}>
              {lang === "bn" ? "ব্যাকরণ খাবারে লবণের মতো — অল্প, কিন্তু দরকারি।" : "Grammar is like salt in food: a little, but it matters."}
            </p>
            {pats.map((id) => {
              const pt = PATTERNS[id];
              return (
                <div key={id} className="card p-4">
                  <div className="flex items-center gap-3">
                    <span className="ar min-w-16 text-center text-4xl text-emerald">{A(pt.ar)}</span>
                    <div className={`flex-1 text-lg font-black ${lang === "bn" ? "bn" : ""}`}>{pt.emoji} {lang === "bn" ? pt.bn : pt.en}</div>
                    <StrengthDots level={strengthLevel(p.items["p:" + id])} />
                  </div>
                  <p className={`mt-2 text-sm text-ink/80 ${lang === "bn" ? "bn" : ""}`}>{A(lang === "bn" ? pt.expl_bn : pt.expl_en)}</p>
                  <div className="mt-2 flex flex-wrap gap-2" dir="rtl">
                    {pt.examples.map((e, i) => (
                      <button key={i} onClick={() => playWord(e.audio)} className="rounded-xl bg-sand px-2 py-1 text-center">
                        <span className="ar block text-xl">{A(e.ar).split(" ")[0]}</span>
                        <span className={`block text-xs text-muted ${lang === "bn" ? "bn" : ""}`} dir="ltr">{lang === "bn" ? e.bn : e.en}</span>
                      </button>
                    ))}
                  </div>
                </div>
              );
            })}
          </div>
        )
      )}
    </div>
  );
}

function Empty({ lang }: { lang: string }) {
  return (
    <div className="card p-8 text-center text-muted">
      <div className="text-5xl">📚</div>
      <p className={`mt-2 font-bold ${lang === "bn" ? "bn" : ""}`}>{lang === "bn" ? "যা শিখবেন তা এখানে জমা হবে।" : "Everything you learn will collect here."}</p>
    </div>
  );
}
