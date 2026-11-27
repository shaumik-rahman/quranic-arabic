# Deploying Quranic Arabic

About 20 minutes, all free tiers. You need accounts on **GitHub**, **Supabase** and **Vercel** (sign up to Vercel and Supabase with GitHub to make it easy).

> Without Supabase keys the app runs in **demo mode**: no login, progress saved on the device, and a role switcher on the **Me** page for testing Teacher mode. That's handy for trying it locally, but deploy with Supabase so people can have accounts.

---

## 1. Try it locally (optional)

```bash
npm install
npm run dev          # http://localhost:3000 (demo mode)
```

## 2. Supabase (accounts + database)

1. https://supabase.com → **New project**. Pick a region near your users (e.g. Singapore / Mumbai), set a database password, create.
2. **SQL Editor → New query**: paste all of `supabase/schema.sql` → **Run**. You should see "Success".
   - This creates the tables, security rules and the admin functions.
   - `shaumik.rahman@gmail.com` automatically becomes **superadmin** when that account signs up (change the email in the file if needed *before* running).
3. **Project Settings → API Keys** (or **Settings → API**): copy
   - the **Project URL** (`https://xxxx.supabase.co`)
   - the **publishable / anon public** key (safe to use in the browser).

## 3. Put the code on GitHub

```bash
git init && git add -A && git commit -m "Quranic Arabic v1"   # skip if already a repo
# create an empty repo on github.com (e.g. quranic-arabic), then:
git remote add origin https://github.com/<you>/quranic-arabic.git
git branch -M main
git push -u origin main
```

## 4. Vercel (hosting)

1. https://vercel.com → **Add New… → Project** → import the GitHub repo.
2. Framework is detected as Next.js. Open **Environment Variables** and add:
   | Name | Value |
   |---|---|
   | `NEXT_PUBLIC_SUPABASE_URL` | your Project URL |
   | `NEXT_PUBLIC_SUPABASE_ANON_KEY` | your publishable / anon key |
3. **Deploy**. You'll get a URL like `https://quranic-arabic.vercel.app`.

## 5. Tell Supabase your site's address

Supabase → **Authentication → URL Configuration**:
- **Site URL**: `https://quranic-arabic.vercel.app`
- **Redirect URLs**: add `https://quranic-arabic.vercel.app/**` and `http://localhost:3000/**`

## 6. Google sign-in

1. https://console.cloud.google.com → create a project (any name).
2. **APIs & Services → OAuth consent screen**: External, app name "Quranic Arabic", your email → save. Add yourself as a test user, or **Publish app** so anyone can sign in.
3. **APIs & Services → Credentials → Create credentials → OAuth client ID** → *Web application*.
   - **Authorized redirect URI**: `https://<your-project-ref>.supabase.co/auth/v1/callback`
     (Supabase shows this exact URL on its Google provider page.)
4. Copy the **Client ID** and **Client secret** → Supabase → **Authentication → Sign In / Providers → Google** → enable, paste both, save.

## 7. Make yourself superadmin & add teachers

1. Open the site, **Get started → Continue with Google** using `shaumik.rahman@gmail.com`.
2. Go to **Me → Admin: manage teachers**. Search a user and tap **Make teacher**.
   Teachers get every lesson unlocked and unlimited hearts. (They must have signed up first.)

## 8. Add to Home Screen

- **iPhone (Safari)**: open the site → **Share** → **Add to Home Screen**.
- **Android (Chrome)**: open the site → **⋮** → **Install app** / **Add to Home screen**.

It opens full-screen like an app, works offline for lessons you've opened, and caches audio after the first play.

---

### Notes
- **Email sign-up**: Supabase sends a confirmation email. Its built-in mailer only allows a few emails per hour. For real use, add your own SMTP (Authentication → Emails → SMTP), or turn off "Confirm email" (Authentication → Sign In / Providers → Email).
- **Updates**: every `git push` to `main` redeploys automatically.
- **Editing content** (meanings, Bangla, emojis, new units): see `scripts/content-pipeline/README.md`.

## Edit content (superadmin)
Run `supabase/content_overrides.sql` once in Supabase → SQL Editor. Then Profile → Admin → **Edit content** lets the
superadmin fix any meaning, explanation, question or translation. Edits are stored in the `content_overrides` table and
reach every learner the next time they open the app. “Download all edits” saves them as a file, so they can also be
merged into the source (`scripts/content-pipeline/`) later.
