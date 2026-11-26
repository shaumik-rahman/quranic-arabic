-- Quranic Arabic — Supabase schema
-- Run this once in Supabase → SQL Editor → New query → Run.
-- The superadmin email is set below; that account gets the "superadmin" role on sign-up.

-- ============ tables ============
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null,
  display_name text,
  role text not null default 'learner' check (role in ('learner', 'teacher', 'superadmin')),
  leaderboard_opt_in boolean not null default false,
  total_xp integer not null default 0,
  weekly_xp integer not null default 0,
  week_start date,
  words_learned integer not null default 0,
  created_at timestamptz not null default now()
);

create table if not exists public.progress (
  user_id uuid primary key references auth.users(id) on delete cascade,
  state jsonb not null,
  updated_at timestamptz not null default now()
);

-- (ready for later) classes a teacher can run
create table if not exists public.classes (
  id uuid primary key default gen_random_uuid(),
  teacher_id uuid not null references public.profiles(id) on delete cascade,
  name text not null,
  join_code text unique not null default substr(md5(random()::text), 1, 6),
  created_at timestamptz not null default now()
);
create table if not exists public.class_members (
  class_id uuid references public.classes(id) on delete cascade,
  user_id uuid references public.profiles(id) on delete cascade,
  joined_at timestamptz not null default now(),
  primary key (class_id, user_id)
);

-- ============ helpers ============
create or replace function public.is_superadmin() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and role = 'superadmin');
$$;

-- new user → profile row (superadmin by email)
create or replace function public.handle_new_user() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, email, display_name, role)
  values (
    new.id,
    coalesce(new.email, ''),
    coalesce(new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'name'),
    case when lower(new.email) = 'shaumik.rahman@gmail.com' then 'superadmin' else 'learner' end
  )
  on conflict (id) do nothing;
  return new;
end $$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

-- users can't change their own role (only the superadmin, via set_user_role)
create or replace function public.protect_role() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  -- auth.uid() is null when run from the SQL Editor / server, where role changes are allowed
  if new.role is distinct from old.role and auth.uid() is not null and not public.is_superadmin() then
    new.role := old.role;
  end if;
  return new;
end $$;
drop trigger if exists protect_role on public.profiles;
create trigger protect_role before update on public.profiles
  for each row execute function public.protect_role();

-- ============ table access for signed-in users (row level security below still restricts rows) ============
grant usage on schema public to authenticated;
grant select, insert, update on public.profiles to authenticated;
grant select, insert, update, delete on public.progress to authenticated;
grant select, insert, update, delete on public.classes, public.class_members to authenticated;

-- ============ row level security ============
alter table public.profiles enable row level security;
alter table public.progress enable row level security;
alter table public.classes enable row level security;
alter table public.class_members enable row level security;

drop policy if exists "own profile read" on public.profiles;
create policy "own profile read" on public.profiles for select using (id = auth.uid() or public.is_superadmin());
drop policy if exists "own profile update" on public.profiles;
create policy "own profile update" on public.profiles for update using (id = auth.uid()) with check (id = auth.uid());

drop policy if exists "own progress" on public.progress;
create policy "own progress" on public.progress for all using (user_id = auth.uid()) with check (user_id = auth.uid());

drop policy if exists "teacher classes" on public.classes;
create policy "teacher classes" on public.classes for all using (teacher_id = auth.uid() or public.is_superadmin()) with check (teacher_id = auth.uid());
drop policy if exists "class members" on public.class_members;
create policy "class members" on public.class_members for select using (
  user_id = auth.uid() or exists (select 1 from public.classes c where c.id = class_id and c.teacher_id = auth.uid()) or public.is_superadmin()
);

-- ============ RPCs ============
create or replace function public.get_leaderboard()
returns table (display_name text, weekly_xp integer, words_learned integer, is_me boolean)
language sql stable security definer set search_path = public as $$
  select coalesce(p.display_name, split_part(p.email, '@', 1)), p.weekly_xp, p.words_learned, p.id = auth.uid()
  from public.profiles p
  where p.leaderboard_opt_in
    and p.week_start = (date_trunc('week', now() at time zone 'utc'))::date
    and p.weekly_xp > 0
  order by p.weekly_xp desc
  limit 50;
$$;

create or replace function public.admin_list_users(search text default '')
returns table (id uuid, email text, display_name text, role text, total_xp integer, words_learned integer, created_at timestamptz)
language plpgsql stable security definer set search_path = public as $$
begin
  if not public.is_superadmin() then raise exception 'not allowed'; end if;
  return query
    select p.id, p.email, p.display_name, p.role, p.total_xp, p.words_learned, p.created_at
    from public.profiles p
    where search = '' or p.email ilike '%' || search || '%' or coalesce(p.display_name, '') ilike '%' || search || '%'
    order by p.created_at desc
    limit 200;
end $$;

create or replace function public.set_user_role(target uuid, new_role text)
returns void language plpgsql security definer set search_path = public as $$
begin
  if not public.is_superadmin() then raise exception 'not allowed'; end if;
  if new_role not in ('learner', 'teacher') then raise exception 'bad role'; end if;
  update public.profiles set role = new_role where id = target and role <> 'superadmin';
end $$;

grant execute on function public.get_leaderboard() to authenticated;
grant execute on function public.admin_list_users(text) to authenticated;
grant execute on function public.set_user_role(uuid, text) to authenticated;
