# -*- coding: utf-8 -*-
"""
Hand-authored curriculum content for "Quranic Arabic" v1.
Everything here should be reviewed by a knowledgeable person (meanings, Bangla, cognates).

WORDS: keyed by Quranic Arabic Corpus lemma key "LEMMA|ROOT" (or "PRON:3MS", or "X:name" for
       words that are not a Quranic lemma, e.g. حَيَّ in the azan).
       ar     = teaching form (as met in the texts)
       en/bn  = core meaning
       emoji  = picture ("" = none; "ﷲ"/"ﷺ" glyphs render as calligraphy)
       cog    = related words in English / Bangla / Hindi that learners already know
       tip    = optional one-liner shown in "More"
"""

W = {}
def w(key, ar, en, bn, emoji, en_c="", bn_c="", hi_c="", tip="", root=None):
    W[key] = dict(ar=ar, en=en, bn=bn, emoji=emoji,
                  cog={k: v for k, v in dict(en=en_c, bn=bn_c, hi=hi_c).items() if v},
                  tip=tip, root=root)

# ---------- Al-Fatiha ----------
w("اسْم|سمو", "ٱسۡمٌ", "name", "নাম", "🏷️", bn_c="ইসম (ইসমে আজম)", hi_c="ism",
  tip="بِسۡمِ = بِ (in) + ٱسۡم (name) → “in the name”")
w("اللَّه|أله", "ٱللَّهُ", "Allah", "আল্লাহ", "ﷲ")
w("رَحْمٰن|رحم", "ٱلرَّحۡمَٰنُ", "the Most Merciful (to all)", "পরম করুণাময়", "💗",
  bn_c="রহমান (আবদুর রহমান)", hi_c="rahmaan")
w("رَحِيم|رحم", "رَحِيمٌ", "the Especially Merciful", "অসীম দয়ালু", "🤍",
  bn_c="রহিম", hi_c="raheem")
w("حَمْد|حمد", "حَمۡدٌ", "praise", "প্রশংসা", "👏", bn_c="হামদ (হামদ-নাত)", hi_c="hamd",
  tip="Same root ح م د as Muhammad, Ahmad and Mahmud: “the praised one”.")
w("رَبّ|ربب", "رَبٌّ", "Lord (who cares for and raises)", "রব (প্রতিপালক)", "🌱",
  bn_c="রব", hi_c="rab")
w("عالَم|علم", "ٱلۡعَٰلَمِينَ", "worlds, all creation", "জগতসমূহ", "🌌",
  bn_c="আলম (দুনিয়া-আলম)", hi_c="aalam (world)",
  tip="Same root ع ل م as عِلۡم (knowledge): the world is how we come to know its Maker.")
w("مالِك|ملك", "مَٰلِكٌ", "Master, Owner", "মালিক", "🔑", bn_c="মালিক", hi_c="maalik")
w("يَوْم|يوم", "يَوۡمٌ", "day", "দিন", "📅")
w("دِين|دين", "دِينٌ", "religion; the Judgment (recompense)", "দ্বীন; প্রতিদান", "⚖️",
  bn_c="দ্বীন (দ্বীন-দুনিয়া)", hi_c="deen (deen-imaan)")
w("إِيّا|", "إِيَّاكَ", "You alone", "কেবল তোমাকেই", "🫵")
w("عَبَدَ|عبد", "نَعۡبُدُ", "we worship", "আমরা ইবাদত করি", "🧎",
  bn_c="ইবাদত, আবদুল", hi_c="ibaadat")
w("اسْتَعِينُ|عون", "نَسۡتَعِينُ", "we ask for help", "আমরা সাহায্য চাই", "🆘")
w("هَدَى|هدي", "ٱهۡدِنَا", "guide us", "আমাদের পথ দেখাও", "🧭",
  bn_c="হেদায়েত", hi_c="hidaayat (instruction)")
w("صِراط|صرط", "صِرَٰطٌ", "path", "পথ", "🛤️", bn_c="সিরাত (পুলসিরাত)")
w("مُسْتَقِيم|قوم", "مُسۡتَقِيمٌ", "straight", "সরল, সোজা", "📏", bn_c="মুস্তাকিম",
  tip="Root ق و م = to stand: a path that “stands straight”.")
w("الَّذِي|", "ٱلَّذِي / ٱلَّذِينَ", "who, the one(s) who", "যে / যারা", "👉")
w("أَنْعَمَ|نعم", "أَنۡعَمۡتَ", "You blessed", "তুমি নিয়ামত দিয়েছ", "🌸",
  bn_c="নিয়ামত", hi_c="nemat")
w("عَلَى|", "عَلَىٰ", "on, upon", "উপর", "🔛")
w("غَيْر|غير", "غَيۡرُ", "not, other than", "নয়, অন্য", "🔀",
  bn_c="গায়ের (গায়রে মাহরাম)", hi_c="ghair (stranger, other)")
w("مَغْضُوب|غضب", "مَغۡضُوبٌ", "those under (Allah's) anger", "গজবপ্রাপ্ত", "😠",
  bn_c="গজব", hi_c="ghazab")
w("لا|", "لَا", "no, not", "না", "🚫")
w("ضالّ|ضلل", "ٱلضَّآلِّينَ", "those who went astray", "পথভ্রষ্টরা", "🌀",
  )

# ---------- Al-Ikhlas ----------
w("قالَ|قول", "قُلۡ", "say! / he said", "বলো / বলল", "🗣️",
  bn_c="কওল, কাওয়ালি", hi_c="qaul (word, promise), qawwaali")
w("PRON:3MS", "هُوَ", "he, He", "সে, তিনি", "👆")
w("أَحَد|أحد", "أَحَدٌ", "one, anyone", "এক, কেউ", "1️⃣", bn_c="আহাদ")
w("صَمَد|صمد", "ٱلصَّمَدُ", "the Self-Sufficient (whom all need)", "অমুখাপেক্ষী", "🧲")
w("لَم|", "لَمۡ", "did not", "না (করেননি)", "⛔")
w("وَلَدَ|ولد", "يَلِدۡ", "to give birth, beget", "জন্ম দেওয়া", "👶",
  bn_c="আওলাদ", hi_c="aulaad (children), walad")
w("كانَ|كون", "كَانَ", "was, is", "ছিল, হয়", "🕰️")
w("كُفُو|كفأ", "كُفُوًا", "equal", "সমকক্ষ", "🟰", bn_c="কুফু (বিয়েতে সমতা)")

# ---------- Al-Kawthar ----------
w("إِنّ|", "إِنَّ", "indeed, surely", "নিশ্চয়ই", "❗")
w("أَعْطَى|عطو", "أَعۡطَيۡنَٰكَ", "We have given you", "আমরা তোমাকে দিয়েছি", "🎁",
  bn_c="আতা (দান)", hi_c="ata karna (to bestow)")
w("كَوْثَر|كثر", "ٱلۡكَوۡثَرُ", "Al-Kawthar: abundant good (a river in Paradise)", "কাওসার: প্রচুর কল্যাণ", "🏞️",
  bn_c="কাওসার", hi_c="aksar (often), kasrat",
  tip="Root ك ث ر = “much, many”. Hindi/Urdu “aksar” (often) comes from أَكۡثَر!")
w("صَلَّى|صلو", "صَلِّ", "pray!", "নামাজ পড়ো", "🕋", bn_c="সালাত", hi_c="salaat")
w("انْحَرْ|نحر", "ٱنۡحَرۡ", "sacrifice!", "কুরবানি করো", "🐑")
w("شانِئ|شنأ", "شَانِئٌ", "hater, enemy", "বিদ্বেষী, শত্রু", "😡")
w("أَبْتَر|بتر", "ٱلۡأَبۡتَرُ", "cut off (from all good)", "নির্বংশ, বিচ্ছিন্ন", "✂️")

# ---------- Al-Asr ----------
w("عَصْر|عصر", "عَصۡرٌ", "time; afternoon", "সময়; আসর", "🌇", bn_c="আসর (নামাজ)", hi_c="asr")
w("إِنسان|أنس", "إِنسَٰنٌ", "human being", "মানুষ", "🧑",
  bn_c="ইনসান, ইনসানিয়াত", hi_c="insaan, insaaniyat")
w("فِي|", "فِي", "in", "মধ্যে, -তে", "📥")
w("خُسْر|خسر", "خُسۡرٌ", "loss", "ক্ষতি", "📉", bn_c="খেসারত", hi_c="khasaara (loss)")
w("إِلّا|", "إِلَّا", "except", "ছাড়া, তবে", "➖")
w("آمَنَ|أمن", "ءَامَنُواْ", "they believed", "তারা ঈমান এনেছে", "💚",
  bn_c="ঈমান, আমানত, আমিন", hi_c="imaan, amaanat, aman (peace)",
  tip="Root أ م ن = safety, trust. Iman is trusting Allah and feeling safe with Him.")
w("عَمِلَ|عمل", "عَمِلُواْ", "they did (deeds)", "তারা আমল করেছে", "🛠️",
  bn_c="আমল, আমলা", hi_c="amal (implementation), amla (staff)")
w("صالِحَة|صلح", "صَٰلِحَٰتٌ", "good deeds", "সৎকাজ", "🌟",
  bn_c="সালেহ, ইসলাহ", hi_c="sulah (reconciliation), islaah")
w("تَواصَ|وصي", "تَوَاصَوۡاْ", "advised one another", "পরস্পরকে উপদেশ দিয়েছে", "💬",
  bn_c="অসিয়ত (উইল)", hi_c="wasiyat (will)")
w("حَقّ|حقق", "حَقٌّ", "truth; right", "সত্য; হক", "✔️",
  bn_c="হক, হকদার, হাকিকত", hi_c="haq, haqeeqat (reality)")
w("صَبْر|صبر", "صَبۡرٌ", "patience", "সবর, ধৈর্য", "⏳", bn_c="সবর", hi_c="sabr")

# ---------- An-Nasr ----------
w("إِذا|", "إِذَا", "when", "যখন", "⏰")
w("جاءَ|جيأ", "جَآءَ", "came", "এলো", "🚶")
w("نَصْر|نصر", "نَصۡرٌ", "help (that brings victory)", "সাহায্য", "🤝",
  bn_c="নুসরাত, নাসির", hi_c="nusrat")
w("فَتْح|فتح", "فَتۡحٌ", "victory; opening", "বিজয়; খুলে যাওয়া", "🏆",
  bn_c="ফতেহ, ফাতিহা", hi_c="fatah (victory)",
  tip="Al-Fātiḥa = “the Opener”: same root ف ت ح!")
w("رَأَى|رأي", "رَأَيۡتَ", "you saw", "তুমি দেখলে", "👀", bn_c="রায় (মতামত)", hi_c="raay (opinion)")
w("ناس|أنس", "ٱلنَّاسُ", "people, mankind", "মানুষ (সকলে)", "👥",
  tip="Same root as إِنسَٰن (human).")
w("دَخَلَ|دخل", "يَدۡخُلُونَ", "they enter", "তারা প্রবেশ করে", "🚪",
  bn_c="দখল, দাখিল", hi_c="daakhila (admission), dakhal")
w("فَوْج|فوج", "أَفۡوَاجًا", "in crowds", "দলে দলে", "👨‍👩‍👧‍👦", bn_c="ফৌজ (সেনাদল)", hi_c="fauj (army)")
w("سَبَّحَ|سبح", "سَبِّحۡ", "glorify!", "তাসবিহ পড়ো", "📿", bn_c="তসবি", hi_c="tasbeeh")
w("اسْتَغْفَرَ|غفر", "ٱسۡتَغۡفِرۡ", "ask forgiveness!", "ক্ষমা চাও", "🙏",
  bn_c="ইস্তেগফার, মাগফিরাত", hi_c="maghfirat")
w("تَوّاب|توب", "تَوَّابٌ", "Ever-Accepting of repentance", "তওবা কবুলকারী", "🔁",
  bn_c="তওবা", hi_c="tauba")

# ---------- Al-Falaq ----------
w("عُذْ|عوذ", "أَعُوذُ", "I seek refuge", "আমি আশ্রয় চাই", "🛡️", bn_c="আউযু বিল্লাহ")
w("فَلَق|فلق", "ٱلۡفَلَقُ", "daybreak", "ভোর", "🌅")
w("مِن|", "مِنۡ", "from, of", "থেকে", "↩️")
w("شَرّ|شرر", "شَرٌّ", "evil", "অনিষ্ট", "⚠️", hi_c="sharaarat (mischief)")
w("ما|", "مَا", "what; not", "যা; না", "❓")
w("خَلَقَ|خلق", "خَلَقَ", "He created", "তিনি সৃষ্টি করেছেন", "✨",
  bn_c="খালিক, মাখলুক, আখলাক", hi_c="makhlooq, akhlaaq (manners)")
w("غاسِق|غسق", "غَاسِقٌ", "darkness (of night)", "অন্ধকার রাত", "🌑")
w("وَقَبَ|وقب", "وَقَبَ", "it settles in", "ছেয়ে যায়", "🌒")
w("نَفّاثَة|نفث", "نَفَّٰثَٰتٌ", "those who blow (on knots)", "ফুঁ দানকারিণীরা", "💨")
w("عُقْدَة|عقد", "عُقَدٌ", "knots", "গিঁট", "🪢",
  bn_c="আকদ (বিয়ে), আকিদা", hi_c="aqeeda (belief), aqd")
w("حاسِد|حسد", "حَاسِدٌ", "envier", "হিংসুক", "😒", hi_c="hasad (envy)")
w("حَسَدَ|حسد", "حَسَدَ", "he envied", "হিংসা করল", "🫤")

# ---------- An-Nas ----------
w("مَلِك|ملك", "مَلِكٌ", "King", "বাদশাহ", "👑",
  bn_c="মুলুক (দেশ)", hi_c="mulk (country), malika (queen)")
w("إِلٰه|أله", "إِلَٰهٌ", "god (one who is worshipped)", "ইলাহ (উপাস্য)", "☝️", bn_c="ইলাহ")
w("وَسْواس|وسوس", "وَسۡوَاسٌ", "whisperer", "কুমন্ত্রণাদাতা", "🤫",
  bn_c="ওয়াসওয়াসা", hi_c="waswasa (anxious thought)")
w("خَنّاس|خنس", "خَنَّاسٌ", "one who slinks back", "আত্মগোপনকারী", "🫣")
w("وَسْوَسَ|وسوس", "يُوَسۡوِسُ", "whispers", "কুমন্ত্রণা দেয়", "🗯️")
w("صَدْر|صدر", "صُدُورٌ", "chests, hearts", "বুক, অন্তর", "🫁",
  bn_c="সদর (প্রধান, সদর দপ্তর)", hi_c="sadar (president)")
w("جِنَّة|جنن", "ٱلۡجِنَّةُ", "jinn", "জিন", "🫥", en_c="genie", bn_c="জিন, জান্নাত, মজনু", hi_c="jinn, jannat, majnoon",
  tip="Root ج ن ن = hidden. Jinn are hidden; Jannah is a garden hidden by trees.")

# ---------- Duas ----------
w("مَن|", "مَنۡ", "who, whoever", "কে, যে", "🙋")
w("آتَى|أتي", "ءَاتِنَا", "give us", "আমাদের দাও", "🤲")
w("دُنْيا|دنو", "ٱلدُّنۡيَا", "this world", "দুনিয়া", "🌎", en_c="dunya", bn_c="দুনিয়া", hi_c="duniya")
w("حَسَنَة|حسن", "حَسَنَةٌ", "good (thing)", "কল্যাণ", "🌈",
  bn_c="হাসান, এহসান, হুসন", hi_c="ehsaan (favour), husn, haseen")
w("آخِر|أخر", "ٱلۡأٓخِرَةُ", "the Hereafter", "আখেরাত", "🌄",
  bn_c="আখেরাত, আখেরে (শেষে)", hi_c="aakhir (finally), aakhirat")
w("وَقَى|وقي", "قِنَا", "protect us", "আমাদের রক্ষা করো", "☂️", bn_c="তাকওয়া, মুত্তাকি", hi_c="taqwa")
w("عَذاب|عذب", "عَذَابٌ", "punishment", "আজাব, শাস্তি", "⛓️", bn_c="আজাব", hi_c="azaab")
w("نار|نور", "نَارٌ", "fire", "আগুন", "🔥",
  tip="Corpus root ن و ر — same root as نُور (light)!")
w("زادَ|زيد", "زِدۡنِي", "increase me", "আমাকে বাড়িয়ে দাও", "📈", hi_c="zyaada (more)")
w("عِلْم|علم", "عِلۡمٌ", "knowledge", "ইলম, জ্ঞান", "🧠",
  en_c="ulema", bn_c="ইলম, আলেম, তালিম, মালুম", hi_c="ilm, taaleem, maaloom (known)")
w("رَحْمَة|رحم", "رَحۡمَةٌ", "mercy", "রহমত, দয়া", "💞", bn_c="রহমত", hi_c="rahmat")
w("رَحِمَ|رحم", "ٱرۡحَمۡ", "have mercy!", "দয়া করো", "💕")
w("رَبَّيَ|ربو", "رَبَّيَانِي", "they raised me", "তাঁরা আমাকে লালন-পালন করেছেন", "👨‍👩‍👦")
w("صَغِير|صغر", "صَغِيرٌ", "small, young", "ছোট", "🐣", bn_c="সগিরা (ছোট গুনাহ)")
w("ظَلَمَ|ظلم", "ظَلَمۡنَا", "we wronged", "আমরা জুলুম করেছি", "💔",
  bn_c="জুলুম, জালিম", hi_c="zulm, zaalim")
w("نَفْس|نفس", "أَنفُسٌ", "selves, souls", "নিজেরা, নফস", "🪞", bn_c="নফস (নফসি নফসি)", hi_c="nafs")
w("إِن|", "إِنۡ", "if", "যদি", "🤔")
w("غَفَرَ|غفر", "ٱغۡفِرۡ", "forgive", "ক্ষমা করো", "🧼",
  bn_c="মাগফিরাত, গফুর", hi_c="maghfirat")
w("خاسِر|خسر", "ٱلۡخَٰسِرِينَ", "losers", "ক্ষতিগ্রস্তরা", "😞", bn_c="খেসারত", hi_c="khasaara")
w("والِدَي|ولد", "وَٰلِدَيَّ", "my parents", "আমার পিতা-মাতা", "👪",
  bn_c="ওয়ালেদাইন", hi_c="waalid, waalidain (parents)")
w("مُؤْمِن|أمن", "ٱلۡمُؤۡمِنِينَ", "believers", "মুমিনরা", "🫶", bn_c="মুমিন", hi_c="momin")
w("قامَ|قوم", "يَقُومُ", "stands, is established", "দাঁড়ায়, প্রতিষ্ঠিত হয়", "🧍",
  bn_c="কায়েম, কিয়ামত, কওম", hi_c="qaayam, qayaamat, qaum")
w("حِساب|حسب", "حِسَابٌ", "account, reckoning", "হিসাব", "🧮", bn_c="হিসাব", hi_c="hisaab")
w("PRON:1P", "نَحۡنُ / ـنَا", "we, us", "আমরা, আমাদের", "👨‍👩‍👧")
w("PRON:1S", "أَنَا / ـِي", "I, me", "আমি, আমাকে", "🙋")
w("PRON:2MS", "أَنتَ / ـكَ", "you", "তুমি, তোমাকে", "🫵")
w("كَما|", "كَمَا", "just as", "যেমন", "🪞")

# ---------- Ayatul Kursi ----------
w("حَيّ|حيي", "حَيٌّ", "the Ever-Living", "চিরঞ্জীব", "🌳", bn_c="হায়াত (জীবন)", hi_c="hayaat (life)")
w("قَيُّوم|قوم", "قَيُّومٌ", "Sustainer of all", "সবকিছুর ধারক", "🏛️", bn_c="কাইয়ুম")
w("أَخَذَ|أخذ", "تَأۡخُذُ", "takes, overtakes", "ধরে, পেয়ে বসে", "✊")
w("سِنَة|وسن", "سِنَةٌ", "drowsiness", "তন্দ্রা", "🥱")
w("نَوْم|نوم", "نَوۡمٌ", "sleep", "ঘুম", "😴")
w("سَماء|سمو", "سَمَٰوَٰتٌ", "heavens, skies", "আকাশসমূহ", "☁️")
w("أَرْض|أرض", "أَرۡضٌ", "earth, land", "পৃথিবী, জমি", "🌍")
w("ذا|", "ذَا", "this; (who) is it", "এই; সে কে", "👇")
w("يَشْفَعُ|شفع", "يَشۡفَعُ", "intercedes", "সুপারিশ করে", "🫱", bn_c="শাফায়াত", hi_c="shafaa'at")
w("عِند|عند", "عِندَ", "with, near", "কাছে", "📍")
w("إِذْن|أذن", "إِذۡنٌ", "permission", "অনুমতি", "🎫",
  bn_c="আজান", hi_c="azaan", tip="Same root أ ذ ن as أَذَان (azan): “announcement, hearing”.")
w("عَلِمَ|علم", "يَعۡلَمُ", "knows", "জানেন", "💡", bn_c="মালুম", hi_c="maaloom")
w("بَيْن|بين", "بَيۡنَ", "between", "মাঝে", "↔️", bn_c="বয়ান", hi_c="bayaan (statement)")
w("يَد|يدي", "أَيۡدِي", "hands", "হাত", "✋",
  tip="مَا بَيۡنَ أَيۡدِيهِمۡ = “what is between their hands” = what is in front of them.")
w("خَلْف|خلف", "خَلۡفَ", "behind", "পেছনে", "🔙",
  bn_c="খলিফা, খেলাফ, খেলাপি", hi_c="khilaaf (against)")
w("أَحاطَ|حوط", "يُحِيطُونَ", "they encompass", "তারা আয়ত্ত করে", "⭕", hi_c="ahaata (enclosure)")
w("شَىْء|شيأ", "شَيۡءٌ", "thing", "কিছু, জিনিস", "📦", hi_c="shai (thing)")
w("شاءَ|شيأ", "شَآءَ", "He willed", "তিনি চাইলেন", "🌠", bn_c="ইনশাআল্লাহ, মাশাআল্লাহ")
w("وَسِعَ|وسع", "وَسِعَ", "extends over", "পরিব্যাপ্ত", "🌐", hi_c="wus'at (vastness)")
w("كُرْسِيّ|كرس", "كُرۡسِيٌّ", "Kursi (Footstool)", "কুরসি", "💠", bn_c="কুরসি (চেয়ার)", hi_c="kursi (chair)")
w("يَئُودُ|أود", "يَـُٔودُ", "tires, burdens", "ক্লান্ত করে", "😮‍💨")
w("حِفْظ|حفظ", "حِفۡظٌ", "guarding, preserving", "রক্ষণাবেক্ষণ", "🔒",
  bn_c="হাফেজ, হেফাজত", hi_c="hifaazat, haafiz (Khuda haafiz)")
w("عَلِيّ|علو", "عَلِيٌّ", "the Most High", "সর্বোচ্চ", "🏔️", bn_c="আলী", hi_c="aala (excellent)")
w("عَظِيم|عظم", "عَظِيمٌ", "Magnificent, Great", "মহান", "⛰️", bn_c="আজিম, আজমত", hi_c="azeem, azmat")
w("تَعالَى|علو", "تَعَٰلَى", "exalted is", "মহিমান্বিত", "🔼")
w("مَلِك|ملك", "مَلِكٌ", "King", "বাদশাহ", "👑",
  bn_c="মুলুক (দেশ)", hi_c="mulk (country), malika (queen)")

# ---------- Salah, Azan, Tashahhud ----------
w("أَكْبَر|كبر", "أَكۡبَرُ", "greatest, greater", "সবচেয়ে বড়", "🔝",
  bn_c="আকবর, তাকবীর, কবিরা", hi_c="akbar, kabeer")
w("سُبْحان|سبح", "سُبۡحَٰنَ", "glory be to", "পবিত্র (মহিমা)", "✨", bn_c="সুবহানাল্লাহ")
w("سَمِعَ|سمع", "سَمِعَ", "hears, heard", "শোনেন", "👂")
w("X:hamida", "حَمِدَ", "praised", "প্রশংসা করল", "🙌", root="حمد")
w("أَعْلَى|علو", "أَعۡلَىٰ", "the Most High", "সর্বোচ্চ", "⬆️", hi_c="aala")
w("تَحِيَّة|حيي", "تَحِيَّاتٌ", "greetings", "অভিবাদন", "👋",
  tip="Root ح ي ي = life: a greeting wishes someone a good life.")
w("صَلاة|صلو", "ٱلصَّلَوٰةُ", "prayer (salah)", "সালাত, নামাজ", "🕌", bn_c="সালাত", hi_c="salaat")
w("طَيِّب|طيب", "طَيِّبَٰتٌ", "good, pure things", "পবিত্র বিষয়", "🍃", bn_c="তৈয়ব, তাইয়েবা")
w("سَلام|سلم", "سَلَٰمٌ", "peace", "সালাম, শান্তি", "🕊️",
  en_c="salaam, Islam, Muslim", bn_c="সালাম, ইসলাম, মুসলিম, সালামত", hi_c="salaam, salaamat",
  tip="Islam and Muslim come from the same root س ل م: peace through submission.")
w("أَيُّها|", "أَيُّهَا", "O (you)", "হে", "📣")
w("نَبِيّ|نبأ", "نَبِيٌّ", "Prophet", "নবী", "📜", bn_c="নবী", hi_c="nabi")
w("بَرَكَة|برك", "بَرَكَٰتٌ", "blessings", "বরকত", "🌾",
  bn_c="বরকত, মুবারক", hi_c="barakat, mubaarak", tip="“Eid Mubarak” = a blessed Eid: same root ب ر ك.")
w("عَبْد|عبد", "عَبۡدٌ / عِبَادٌ", "servant (of Allah)", "বান্দা", "👤",
  bn_c="আবদুল্লাহ = আল্লাহর বান্দা", hi_c="abdul")
w("صالِح|صلح", "ٱلصَّٰلِحِينَ", "the righteous", "নেককাররা", "😇", bn_c="সালেহ", hi_c="sulah")
w("شَهِدَ|شهد", "أَشۡهَدُ", "I bear witness", "আমি সাক্ষ্য দিই", "👁️",
  bn_c="শহীদ, শাহাদাত", hi_c="shaheed, shahaadat")
w("أَنّ|", "أَنَّ", "that", "যে", "🔗")
w("أَن|", "أَنۡ", "that; to", "যে", "🔗")
w("مُحَمَّد|حمد", "مُحَمَّدٌ", "Muhammad ﷺ (the praised one)", "মুহাম্মাদ ﷺ", "ﷺ",
  tip="مُحَمَّد = “the one who is praised again and again”, root ح م د.")
w("رَسُول|رسل", "رَسُولٌ", "messenger", "রাসূল", "✉️", bn_c="রাসূল, রিসালাত", hi_c="rasool, risaala (magazine)")
w("X:hayya", "حَيَّ", "come! hurry to", "এসো", "🏃‍♂️")
w("X:falah", "فَلَاحٌ", "success", "সফলতা", "🏅", hi_c="falaah (welfare)", root="فلح",
  tip="In the Quran you will meet ٱلۡمُفۡلِحُونَ: “the successful ones”.")
w("خَيْر|خير", "خَيۡرٌ", "good; better", "উত্তম, কল্যাণ", "👍",
  bn_c="খায়ের, খয়রাত", hi_c="khair, khairiyat, khairaat")
w("قَد|", "قَدۡ", "indeed, already", "অবশ্যই, ইতিমধ্যে", "☑️")

# remaining Quran lemmas met in the v1 texts
w("عَجِلَ|عجل", "تَعۡجَلۡ", "hurry", "তাড়াহুড়া করো", "⏩")
w("قُرْءان|قرأ", "ٱلۡقُرۡءَانُ", "Quran (the Recitation)", "কুরআন", "📖", bn_c="কারী, কেরাত", hi_c="qaari")
w("قَبْل|قبل", "قَبۡل", "before", "আগে", "⏮️", bn_c="কবুল, কিবলা", hi_c="qabool",
  tip="Root ق ب ل = to face/receive: before (in front), qibla (what we face), qabul (accept).")
w("قَضَى|قضي", "يُقۡضَىٰ", "is completed / decreed", "সম্পন্ন হয়", "🏁",
  bn_c="কাজী, কাজা (নামাজ)", hi_c="qaazi")
w("إِلَى|", "إِلَىٰ", "to, towards", "দিকে", "➡️")
w("وَحْى|وحي", "وَحۡي", "revelation", "ওহি", "📩", bn_c="ওহি")
w("اخْفِضْ|خفض", "ٱخۡفِضۡ", "lower!", "নামিয়ে দাও", "⬇️")
w("جَناح|جنح", "جَنَاح", "wing", "ডানা", "🪽")
w("ذُلّ|ذلل", "ذُّلّ", "humility", "বিনয়", "🙇", bn_c="জিল্লতি", hi_c="zillat")

# ---------- Everyday words for sentence building (all appear in the Quran) ----------
w("ذا|", "هَٰذَا / ذَٰلِكَ", "this / that", "এই / ওই", "👇",
  tip="In the Quran: ذَٰلِكَ ٱلۡكِتَٰبُ = “That is the Book” (2:2). This little word appears over 1,000 times.")
w("PRON:3FS", "هِيَ", "she, it", "সে (মেয়ে), এটি", "👩")
w("أَب|أبو", "أَبٌ", "father", "বাবা, পিতা", "👨", bn_c="আব্বা", hi_c="abba",
  tip="أَبِي = my father. In the Quran: إِذۡ قَالَ إِبۡرَٰهِيمُ لِأَبِيهِ (6:74).")
w("أُمّ|أمم", "أُمٌّ", "mother", "মা", "👩‍🍼", bn_c="আম্মা, উম্মে (উম্মে কুলসুম)", hi_c="ammi",
  tip="Also “source”: أُمُّ ٱلۡكِتَٰبِ = the Mother of the Book (3:7).")
w("قَلَم|قلم", "قَلَمٌ", "pen", "কলম", "🖊️", bn_c="কলম", hi_c="qalam",
  tip="In the Quran: عَلَّمَ بِٱلۡقَلَمِ = He taught by the pen (96:4).")
w("بَيْت|بيت", "بَيۡتٌ", "house", "ঘর, বাড়ি", "🏠", bn_c="বায়তুল্লাহ (আল্লাহর ঘর)",
  tip="ٱلۡبَيۡت in the Quran is usually the Kaaba: رَبَّ هَٰذَا ٱلۡبَيۡتِ = the Lord of this House (106:3).")
w("كِتاب|كتب", "كِتَابٌ", "book; scripture", "কিতাব, বই", "📘", bn_c="কিতাব", hi_c="kitaab",
  tip="Same root ك ت ب as كَتَبَ (he wrote).")
w("كَتَبَ|كتب", "أَكۡتُبُ", "I write", "আমি লিখি", "✍️", bn_c="কাতিব, মকতব", hi_c="maktab, kaatib")
w("قَرَأَ|قرأ", "نَقۡرَأُ", "we read / recite", "আমরা পড়ি", "👓", bn_c="কেরাত, কারী", hi_c="qaari",
  tip="Same root ق ر أ as قُرۡءَان: “the Recitation”.")
w("ذَهَبَ|ذهب", "يَذۡهَبُ", "he goes", "সে যায়", "🚶‍♂️")
w("مَسْجِد|سجد", "مَسۡجِدٌ", "mosque", "মসজিদ", "🕌", bn_c="মসজিদ", hi_c="masjid",
  tip="Root س ج د = to prostrate: a masjid is the place of sujood.")
w("كَبِير|كبر", "كَبِيرٌ", "big, great", "বড়", "🐘", bn_c="কবিরা (বড় গুনাহ)", hi_c="kabeer")
w("جَدِيد|جدد", "جَدِيدٌ", "new", "নতুন", "🆕", hi_c="jadeed")
w("قَرِيب|قرب", "قَرِيبٌ", "near", "কাছে", "🤏", bn_c="করিব", hi_c="qareeb",
  tip="In the Quran: فَإِنِّي قَرِيبٌ = “then indeed I am near” (2:186).")
w("صَلاة|صلو", "ٱلصَّلَوٰةُ", "prayer (salah)", "সালাত, নামাজ", "🛐", bn_c="সালাত", hi_c="salaat")

# ---------- words for the later sentence patterns ----------
w("X:ya", "يَا", "O … (calling someone)", "হে …", "📣", bn_c="ইয়া (ইয়া আল্লাহ)", hi_c="ya (ya Allah)",
  tip="يَا comes before the name of the one you call: يَا أَبِي = O my father! In the Quran it is often joined: يَٰٓأَيُّهَا.")
w("أَيْن|", "أَيۡنَ", "where?", "কোথায়?", "📍", tip="فَأَيۡنَ تَذۡهَبُونَ = So where are you going? (81:26)")
w("هَل|", "هَلۡ", "is it…? does…? (yes/no question)", "কি? (হ্যাঁ/না প্রশ্ন)", "❓",
  tip="هَلۡ turns a sentence into a yes/no question: هَلۡ أَتَىٰكَ = Has (the news) come to you?")
