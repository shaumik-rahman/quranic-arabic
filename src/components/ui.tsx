"use client";
import { isGlyph } from "@/lib/course";

export function Emoji({ e, className = "" }: { e: string; className?: string }) {
  if (!e) return null;
  if (isGlyph(e)) return <span className={`ar leading-none text-emerald ${className}`} style={{ lineHeight: 1 }}>{e}</span>;
  return <span className={`leading-none ${className}`} role="img" aria-hidden>{e}</span>;
}

export function Ring({ pct, size = 44, stroke = 5, color = "var(--color-emerald)", track = "var(--color-line)", children }: {
  pct: number; size?: number; stroke?: number; color?: string; track?: string; children?: React.ReactNode;
}) {
  const r = (size - stroke) / 2;
  const c = 2 * Math.PI * r;
  const p = Math.max(0, Math.min(100, pct));
  return (
    <div className="relative inline-flex items-center justify-center" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="-rotate-90">
        <circle cx={size / 2} cy={size / 2} r={r} stroke={track} strokeWidth={stroke} fill="none" />
        <circle cx={size / 2} cy={size / 2} r={r} stroke={color} strokeWidth={stroke} fill="none"
          strokeDasharray={c} strokeDashoffset={c * (1 - p / 100)} strokeLinecap="round" style={{ transition: "stroke-dashoffset .6s" }} />
      </svg>
      <div className="absolute inset-0 flex items-center justify-center">{children}</div>
    </div>
  );
}

export function Bar({ pct, color = "bg-emerald", className = "" }: { pct: number; color?: string; className?: string }) {
  return (
    <div className={`h-3 w-full overflow-hidden rounded-full bg-line ${className}`}>
      <div className={`h-full rounded-full ${color} transition-all duration-500`} style={{ width: `${Math.max(0, Math.min(100, pct))}%` }} />
    </div>
  );
}

export function StrengthDots({ level }: { level: number }) {
  return (
    <span className="inline-flex gap-0.5" aria-label={`strength ${level} of 3`}>
      {[1, 2, 3].map((i) => (
        <span key={i} className={`h-2 w-2 rounded-full ${i <= level ? (level === 3 ? "bg-gold" : "bg-emerald") : "bg-line"}`} />
      ))}
    </span>
  );
}

export const fmtPct = (n: number) => (n < 10 ? n.toFixed(1) : Math.round(n).toString());
