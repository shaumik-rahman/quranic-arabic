# Quranic Arabic

A gamified web app (installable on iPhone & Android) that teaches a complete beginner to **understand** the Quran, starting from what Muslims already recite: Al-Fatiha, salah, the azan, the last surahs, everyday duas and Ayat al-Kursi.

**Deploy:** see [DEPLOY.md](DEPLOY.md).

## What's inside (v1)
- **14 units, 51 lessons, 152 Quranic words, 22 pattern cards.** Those 152 words make up **48%** of all the words in the Quran.
- **Lesson types**: new word (emoji + audio + example in a verse), multiple choice (Arabic→meaning, meaning→Arabic, listening), tap the word in a verse, fill the missing word, match pairs, build a verse's meaning word by word, choose the verse's meaning.
- **Grammar as salt**: 22 small "pattern" cards (وَ, بِـ, ٱلۡـ, ـنَا, نَـ = we…, فَاعِل = the doer…), each introduced only when a verse needs it. No grammar terms.
- **Spaced repetition**: every word and pattern is scheduled; the Review tab brings them back just before you'd forget them.
- **Gamification**: XP, daily goal, streaks, hearts (refill over time, or earn one by reviewing), badges, weekly leaderboard (opt-in).
- **Progress you can feel**: "% of the Quran's words you know" (learned and mastered), a percentage for each surah, and a **full Quran reader** where known words light up green.
- **Every word is tappable**: meaning, audio, then **More** → root letters, how often it appears, the word family in the Quran, and related words in **English / Bangla / Hindi** (e.g. حِسَاب → হিসাব / हिसाब).
- **Library** of everything learned (sort by path, frequency, root, weakest) + all pattern cards.
- **Languages**: English meanings by default; switch to Bangla anytime (EN/বাং button).
- **Accounts**: email + Google sign-in via Supabase; progress syncs across devices. Superadmin can mark accounts as **Teacher** (all lessons unlocked, unlimited hearts).
- **PWA**: add to home screen, works offline, caches audio.

## Tech
Next.js 16 (App Router) · TypeScript · Tailwind CSS 4 · Zustand · Supabase · deployed on Vercel.

```
src/app/            pages (learn, lesson/[id], practice, review, library, quran, quran/[n], read/[id], profile, leaderboard, admin, auth)
src/components/     LessonPlayer, exercises, WordSheet (tap-a-word), ArabicLine, AppShell
src/lib/            course data access, exercise generator, spaced repetition, progress store, auth + sync
src/data/           course.json, coverage.json (generated)
public/quran/       114 surahs word-by-word for the reader (generated)
scripts/content-pipeline/  the curriculum source (edit here) + build script
supabase/schema.sql database, security rules, admin functions
```

## Content review needed
The English word glosses come from quran.com, and the verse translations from Saheeh International (English) and Muhiuddin Khan (Bangla). The **Bangla word meanings, the related English/Bangla/Hindi words, emojis and tips were written for this app** and should be checked by someone knowledgeable. They're all in `scripts/content-pipeline/content.py` and `texts.py`.

## Credits
Quran text & translations: tanzil.net · Word-by-word & word audio: quran.com · Morphology: Quranic Arabic Corpus (corpus.quran.com) · Recitation: Mishary Alafasy via everyayah.com · Fonts: Amiri Quran, Nunito, Hind Siliguri.
