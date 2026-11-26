"use client";
import { useScript } from "@/lib/script";
import Link from "next/link";
import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/lib/auth";
import { TOTAL_TOKENS, WORDS } from "@/lib/course";

const COURSE_PCT = Math.round((100 * Object.values(WORDS).reduce((a, w) => a + w.count, 0)) / TOTAL_TOKENS);
const N_WORDS = Object.keys(WORDS).length;

export default function Landing() {
  const { status } = useAuth();
  const router = useRouter();
  const { A } = useScript();
  useEffect(() => { if (status === "signedIn") router.replace("/learn"); }, [status, router]);

  return (
    <div className="pattern-bg flex min-h-dvh flex-col text-white">
      <div className="pt-safe mx-auto flex w-full max-w-md flex-1 flex-col px-6">
        <div className="flex-1 pt-14 text-center">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src="/icon-192.png" alt="" className="mx-auto h-24 w-24 rounded-3xl shadow-lg" />
          <h1 className="mt-6 text-4xl font-black leading-tight">Understand the Quran you already recite</h1>
          <p className="bn mt-3 text-lg text-white/85">যে কুরআন আপনি পড়েন, এবার তা বুঝুন</p>
          <div className="ar mt-8 text-4xl leading-relaxed text-gold">{A("ٱلۡحَمۡدُ")} {A("لِلَّهِ")} {A("رَبِّ")} {A("ٱلۡعَٰلَمِينَ").split(" ")[0]}</div>
          <div className="mt-1 text-white/80">All praise is for Allah, Lord of the worlds</div>
          <div className="mt-8 grid grid-cols-3 gap-2 text-center">
            <Feature emoji="🧩" text="5-minute lessons" />
            <Feature emoji="🕌" text="Starts with Al-Fatiha & salah" />
            <Feature emoji="📈" text={`${N_WORDS} words = ${COURSE_PCT}% of the Quran`} />
          </div>
        </div>
        <div className="space-y-3 pb-10 pt-8">
          <Link href="/signup" className="btn btn-gold w-full text-lg">Get started — it&apos;s free</Link>
          <Link href="/login" className="btn w-full border-2 border-white/40 bg-white/10 text-lg text-white">I already have an account</Link>
        </div>
      </div>
    </div>
  );
}

function Feature({ emoji, text }: { emoji: string; text: string }) {
  return (
    <div className="rounded-2xl bg-white/10 p-3">
      <div className="text-2xl">{emoji}</div>
      <div className="mt-1 text-xs font-bold leading-tight">{text}</div>
    </div>
  );
}
