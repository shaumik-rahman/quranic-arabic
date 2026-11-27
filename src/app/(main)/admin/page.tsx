"use client";
import Link from "next/link";
import { useCallback, useEffect, useState } from "react";
import { ArrowLeft, Search } from "lucide-react";
import { supabase } from "@/lib/supabase";
import { useAuth, type Role } from "@/lib/auth";

interface U { id: string; email: string; display_name: string | null; role: Role; total_xp: number; words_learned: number; created_at: string }

export default function AdminPage() {
  const { isAdmin, demo, user } = useAuth();
  const [q, setQ] = useState("");
  const [users, setUsers] = useState<U[] | null>(null);
  const [msg, setMsg] = useState("");

  const load = useCallback(async () => {
    if (!supabase) return;
    const { data, error } = await supabase.rpc("admin_list_users", { search: q });
    if (error) setMsg(error.message); else setUsers(data as U[]);
  }, [q]);
  useEffect(() => { if (isAdmin) { const id = setTimeout(load, 250); return () => clearTimeout(id); } }, [load, isAdmin]);

  const setRole = async (u: U, role: Role) => {
    if (!supabase) return;
    const { error } = await supabase.rpc("set_user_role", { target: u.id, new_role: role });
    if (error) setMsg(error.message);
    else { setMsg(`${u.email} → ${role}`); load(); }
  };

  if (!isAdmin) return <div className="card p-6 text-center">Only the superadmin can open this page. <Link className="text-emerald underline" href="/profile">Back</Link></div>;

  return (
    <div>
      <Link href="/profile" className="mb-3 inline-flex items-center gap-1 font-bold text-muted"><ArrowLeft size={18} /> Profile</Link>
      <Link href="/admin/content" className="card mb-4 flex items-center gap-3 p-4">
        <span className="text-3xl">✏️</span>
        <span className="flex-1"><span className="block text-lg font-black">Edit content</span><span className="block text-sm text-muted">Fix meanings, explanations, questions and translations</span></span>
        <span className="text-xl text-muted">›</span>
      </Link>
      <h1 className="text-2xl font-black">Manage teachers</h1>
      <p className="mt-1 text-sm text-muted">Teachers have every lesson unlocked and unlimited hearts.</p>
      {demo ? (
        <div className="card mt-4 p-4 text-sm">Demo mode: connect Supabase (see DEPLOY.md) to manage real accounts. You can test the Teacher role from the Profile page.</div>
      ) : (
        <>
          <div className="mt-4 flex items-center gap-2 rounded-2xl border-2 border-line bg-white px-3">
            <Search size={18} className="text-muted" />
            <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search by email or name" className="w-full bg-transparent py-2.5 outline-none" />
          </div>
          {msg && <p className="mt-2 text-sm font-bold text-emerald">{msg}</p>}
          <div className="card mt-3 divide-y-2 divide-line overflow-hidden">
            {!users ? <div className="p-4 text-center text-muted">…</div> : users.length === 0 ? <div className="p-4 text-center text-muted">No users found</div> : users.map((u) => (
              <div key={u.id} className="flex items-center gap-3 px-4 py-3">
                <div className="min-w-0 flex-1">
                  <div className="truncate font-bold">{u.display_name || u.email}</div>
                  <div className="truncate text-xs text-muted">{u.email} · {u.total_xp} XP · {u.words_learned} words</div>
                </div>
                {u.role === "superadmin" ? (
                  <span className="rounded-full bg-plum/15 px-2 py-1 text-xs font-extrabold text-plum">Superadmin</span>
                ) : (
                  <button disabled={u.id === user?.id} onClick={() => setRole(u, u.role === "teacher" ? "learner" : "teacher")}
                    className={`rounded-xl border-2 px-3 py-1.5 text-sm font-extrabold ${u.role === "teacher" ? "border-plum bg-plum text-white" : "border-line bg-white"}`}>
                    {u.role === "teacher" ? "Teacher ✓" : "Make teacher"}
                  </button>
                )}
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
