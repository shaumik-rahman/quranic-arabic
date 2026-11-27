"use client";
import Link from "next/link";
import { useState } from "react";
import { ChevronDown, ChevronUp } from "lucide-react";
import { UNITS } from "@/lib/course";
import { useSalahUnderstanding } from "@/lib/salah";
import { useT } from "@/lib/i18n";
import { ArabicLine } from "@/components/ArabicLine";
import { Ring } from "@/components/ui";

export default function SalahPage() {
  const { lang } = useT();
  const bn = lang === "bn" ? "bn" : "";
  const u = useSalahUnderstanding();
  const [open, setOpen] = useState<Record<string, boolean>>({});
  return (
    <div>
      <section className="pattern-bg rounded-3xl p-5 text-white shadow-[0_5px_0_var(--color-emerald-dark)]">
        <div className="flex items-center gap-4">
          <Ring pct={u.pct} size={92} stroke={9} color="var(--color-gold)" track="rgba(255,255,255,.2)">
            <div className="text-2xl font-black">{Math.round(u.pct)}%</div>
          </Ring>
          <div className="flex-1">
            <h1 className={`text-[22px] font-black leading-tight ${bn}`}>{lang === "bn" ? "নিজের নামাজ বুঝুন" : "Understand your salah"}</h1>
            <p className={`mt-1 text-[15px] text-white/85 ${bn}`}>
              {lang === "bn" ? `নামাজে যা বলেন তার ${u.known}/${u.total}টি শব্দ আপনি বোঝেন। নতুন শব্দ শিখলে এখানে সবুজ হয়ে ওঠে।`
                : `You understand ${u.known} of the ${u.total} words you say in salah. Every word you learn turns green here.`}
            </p>
          </div>
        </div>
      </section>

      <ol className="mt-5 space-y-3">
        {u.parts.map(({ g, pct }, i) => {
          const unitIdx = g.unit ? UNITS.findIndex((x) => x.id === g.unit) : -1;
          const isOpen = open[g.id] ?? pct < 100;
          return (
            <li key={g.id} className="card p-4" data-testid="salah-part">
              <button onClick={() => setOpen((o) => ({ ...o, [g.id]: !isOpen }))} className="flex w-full items-center gap-3 text-left">
                <span className={`flex h-9 w-9 shrink-0 items-center justify-center rounded-full font-black ${pct >= 100 ? "bg-emerald text-white" : "bg-sand text-muted"}`}>{i + 1}</span>
                <span className="flex-1">
                  <span className={`block text-[18px] font-black leading-tight ${bn}`}>{lang === "bn" ? g.bn : g.en}</span>
                  {(g.when_en || g.when_bn) && <span className={`block text-[14px] text-muted ${bn}`}>{lang === "bn" ? g.when_bn : g.when_en}</span>}
                </span>
                <span className={`rounded-full px-2.5 py-1 text-sm font-black ${pct >= 100 ? "bg-emerald-light text-emerald-dark" : "bg-gold-light text-gold-dark"}`}>{Math.round(pct)}%</span>
                {isOpen ? <ChevronUp size={18} className="text-muted" /> : <ChevronDown size={18} className="text-muted" />}
              </button>
              {isOpen && (
                <div className="mt-3 space-y-4 border-t-2 border-line pt-3">
                  {g.lines.map((l) => <ArabicLine key={l.id} line={l} size="text-3xl" highlightKnown />)}
                  {pct < 100 && unitIdx >= 0 && (
                    <Link href="/learn" className={`inline-block text-[15px] font-bold text-sky ${bn}`}>
                      {lang === "bn" ? `ইউনিট ${unitIdx + 1}-এ এর শব্দগুলো শিখুন →` : `Learn these words in Unit ${unitIdx + 1} →`}
                    </Link>
                  )}
                </div>
              )}
            </li>
          );
        })}
      </ol>
      <p className={`mt-4 text-center text-[13px] text-muted ${bn}`}>
        {lang === "bn" ? "সবুজ শব্দগুলো আপনি জানেন। যেকোনো শব্দে চাপ দিলে অর্থ দেখাবে। মাযহাব অনুযায়ী কিছু দোয়ার শব্দ সামান্য ভিন্ন হতে পারে।"
          : "Green words are ones you know. Tap any word for its meaning. Some duas differ slightly between schools."}
      </p>
    </div>
  );
}
