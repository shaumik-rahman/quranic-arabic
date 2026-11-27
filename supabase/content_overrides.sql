-- Run this once in Supabase → SQL Editor to enable "Edit content" (Admin page).
create table if not exists public.content_overrides (
  path text primary key,            -- JSON array naming the text, e.g. ["word","عَبْد|عبد","bn"]
  value text not null,
  updated_by uuid references auth.users(id) on delete set null,
  updated_at timestamptz not null default now()
);
alter table public.content_overrides enable row level security;
drop policy if exists "read content edits" on public.content_overrides;
create policy "read content edits" on public.content_overrides for select using (true);
drop policy if exists "superadmin edits content" on public.content_overrides;
create policy "superadmin edits content" on public.content_overrides for all to authenticated
  using (public.is_superadmin()) with check (public.is_superadmin());
grant select on public.content_overrides to anon, authenticated;
grant insert, update, delete on public.content_overrides to authenticated;
