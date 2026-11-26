# Content pipeline

Builds the app's learning data from open Quran datasets + the hand-written curriculum.

| File | What it is |
|---|---|
| `content.py` | **Every word**: emoji, English & Bangla meaning, related words in English/Bangla/Hindi, tips |
| `texts.py` | Bangla word-by-word glosses, salah / azan / tashahhud lines, texts, units, pattern ("salt") cards |
| `build.py` | Joins the above with the Quran data → `src/data/*.json` and `public/quran/*.json` |
| `load.py` | Reads the source datasets |
| `ip_manual.py` | Hand-written IndoPak spellings for forms the converter can't be trusted with |
| `indopak_convert.py` | Uthmani → IndoPak spelling for short teaching forms (run it to see its accuracy against the whole Quran). Real Quran words always use the IndoPak text itself |
| `indopak_converted_review.json` | Written by the build: every converted form, for a human to check |

## Re-run after editing content

```bash
./fetch_sources.sh        # once: downloads the datasets into ./sources (needs curl + npm)
python3 build.py          # writes ../../src/data and ../../public/quran
```

The build prints a report (words per unit, lessons, % of the Quran covered) and lists any `PROBLEMS`
(e.g. a Bangla gloss list that doesn't match the number of words in a verse).

## Adding a unit
1. Add the text to `TEXTS` and the unit to `UNITS` in `texts.py` (Quran verses: `Q(surah, verse[, from_word, to_word])`).
2. Add Bangla glosses for those verses to `BN`.
3. Run `python3 build.py` — it lists every new word that has no entry yet (`no content for word ...`). Add them to `content.py`.

## Sources
- Morphology (roots, lemmas): Quranic Arabic Corpus via github.com/mustafa0x/quran-morphology (GPL)
- Word-by-word English glosses, transliteration, word audio ids: quran.com via `@kmaslesa/holy-quran-word-by-word-full-data`
- Quran text, Saheeh International (en) and Muhiuddin Khan (bn) translations: tanzil.net via `quran-json`
- IndoPak Nastaleeq text (quran.com / QUL) via github.com/quran8vs/IndoPak; font “AlQuran IndoPak by QuranWBW” v4.2.1 from quran.com (credit Ayman Siddiqui, QuranWBW.com — not for sale)
