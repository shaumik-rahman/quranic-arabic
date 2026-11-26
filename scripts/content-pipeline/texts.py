# -*- coding: utf-8 -*-
"""Texts, units, Bangla word-by-word glosses and pattern ("salt") cards."""

# ---------------------------------------------------------------------------
# Bangla word-by-word glosses for Quran segments, keyed "s:v" -> list aligned to word positions
# (only the words used in the curriculum; for partial verses the list starts at the first used word)
BN = {
 "1:1": ["নামে", "আল্লাহর", "পরম করুণাময়", "অসীম দয়ালু"],
 "1:2": ["সব প্রশংসা", "আল্লাহর জন্য", "রব", "জগতসমূহের"],
 "1:3": ["পরম করুণাময়", "অসীম দয়ালু"],
 "1:4": ["মালিক", "দিনের", "প্রতিদানের (বিচারের)"],
 "1:5": ["কেবল তোমারই", "আমরা ইবাদত করি", "এবং কেবল তোমারই কাছে", "আমরা সাহায্য চাই"],
 "1:6": ["আমাদের পথ দেখাও", "পথ", "সরল"],
 "1:7": ["পথ", "তাদের, যাদের", "তুমি নিয়ামত দিয়েছ", "তাদের উপর", "নয়", "গজবপ্রাপ্তদের",
         "তাদের উপর", "এবং না", "পথভ্রষ্টদের"],
 "112:1": ["বলো", "তিনি", "আল্লাহ", "এক"],
 "112:2": ["আল্লাহ", "অমুখাপেক্ষী"],
 "112:3": ["না", "তিনি জন্ম দেন", "এবং না", "তাঁকে জন্ম দেওয়া হয়েছে"],
 "112:4": ["এবং না", "আছে", "তাঁর জন্য", "সমকক্ষ", "কেউ"],
 "108:1": ["নিশ্চয়ই আমরা", "আমরা তোমাকে দিয়েছি", "কাওসার"],
 "108:2": ["তাই নামাজ পড়ো", "তোমার রবের জন্য", "এবং কুরবানি করো"],
 "108:3": ["নিশ্চয়ই", "তোমার বিদ্বেষী", "সে-ই", "নির্বংশ"],
 "103:1": ["সময়ের শপথ"],
 "103:2": ["নিশ্চয়ই", "মানুষ", "অবশ্যই মধ্যে", "ক্ষতির"],
 "103:3": ["তবে", "যারা", "ঈমান এনেছে", "এবং আমল করেছে", "সৎকাজ",
           "এবং পরস্পরকে উপদেশ দিয়েছে", "সত্যের", "এবং পরস্পরকে উপদেশ দিয়েছে", "ধৈর্যের"],
 "110:1": ["যখন", "আসবে", "সাহায্য", "আল্লাহর", "এবং বিজয়"],
 "110:2": ["এবং তুমি দেখবে", "মানুষকে", "প্রবেশ করছে", "মধ্যে", "দ্বীনের", "আল্লাহর", "দলে দলে"],
 "110:3": ["তখন তাসবিহ পড়ো", "প্রশংসার সাথে", "তোমার রবের", "এবং তাঁর কাছে ক্ষমা চাও",
           "নিশ্চয়ই তিনি", "হলেন", "তওবা কবুলকারী"],
 "113:1": ["বলো", "আমি আশ্রয় চাই", "রবের কাছে", "ভোরের"],
 "113:2": ["থেকে", "অনিষ্ট", "যা", "তিনি সৃষ্টি করেছেন"],
 "113:3": ["এবং থেকে", "অনিষ্ট", "অন্ধকার রাতের", "যখন", "তা ছেয়ে যায়"],
 "113:4": ["এবং থেকে", "অনিষ্ট", "ফুঁ দানকারিণীদের", "মধ্যে", "গিঁটগুলোর"],
 "113:5": ["এবং থেকে", "অনিষ্ট", "হিংসুকের", "যখন", "সে হিংসা করে"],
 "114:1": ["বলো", "আমি আশ্রয় চাই", "রবের কাছে", "মানুষের"],
 "114:2": ["বাদশাহ", "মানুষের"],
 "114:3": ["ইলাহ", "মানুষের"],
 "114:4": ["থেকে", "অনিষ্ট", "কুমন্ত্রণাদাতার", "আত্মগোপনকারী"],
 "114:5": ["যে", "কুমন্ত্রণা দেয়", "মধ্যে", "বুকে (অন্তরে)", "মানুষের"],
 "114:6": ["থেকে", "জিনদের", "এবং মানুষদের"],
 "2:201": ["হে আমাদের রব", "আমাদের দাও", "মধ্যে", "দুনিয়া", "কল্যাণ", "এবং মধ্যে",
           "আখেরাত", "কল্যাণ", "এবং আমাদের রক্ষা করো", "শাস্তি", "আগুনের"],
 "20:114": ["এবং বলো", "হে আমার রব", "আমাকে বাড়িয়ে দাও", "জ্ঞানে"],
 "17:24": ["এবং বলো", "হে আমার রব", "তাঁদের দুজনকে দয়া করো", "যেমন",
           "তাঁরা আমাকে লালন-পালন করেছেন", "ছোটবেলায়"],
 "7:23": ["তারা দুজন বলল", "হে আমাদের রব", "আমরা জুলুম করেছি", "আমাদের নিজেদের উপর",
          "এবং যদি", "না", "তুমি ক্ষমা করো", "আমাদের", "এবং আমাদের দয়া করো",
          "অবশ্যই আমরা হব", "মধ্যে", "ক্ষতিগ্রস্তদের"],
 "14:41": ["হে আমাদের রব", "ক্ষমা করো", "আমাকে", "এবং আমার পিতা-মাতাকে", "এবং মুমিনদের",
           "দিনে", "প্রতিষ্ঠিত হবে", "হিসাব"],
 "2:255": ["আল্লাহ", "নেই", "কোনো ইলাহ", "ছাড়া", "তিনি", "চিরঞ্জীব", "সবকিছুর ধারক",
           "না", "তাঁকে পেয়ে বসে", "তন্দ্রা", "এবং না", "ঘুম", "তাঁরই", "যা কিছু", "মধ্যে",
           "আকাশসমূহ", "এবং যা কিছু", "মধ্যে", "পৃথিবী", "কে", "সে", "যে", "সুপারিশ করবে",
           "তাঁর কাছে", "ছাড়া", "তাঁর অনুমতি", "তিনি জানেন", "যা", "মাঝে", "তাদের হাতের (সামনে)",
           "এবং যা", "তাদের পেছনে", "এবং না", "তারা আয়ত্ত করতে পারে", "কোনো কিছু", "থেকে",
           "তাঁর জ্ঞান", "ছাড়া", "যতটুকু", "তিনি চান", "পরিব্যাপ্ত", "তাঁর কুরসি", "আকাশসমূহ",
           "এবং পৃথিবী", "এবং না", "তাঁকে ক্লান্ত করে", "এ দুটির রক্ষণাবেক্ষণ", "এবং তিনি",
           "সর্বোচ্চ", "মহান"],
}

# English word-gloss overrides (the quran.com glosses are good; these fix a few awkward ones)
EN_OVERRIDE = {
 (2, 255, 29): "between",
 (2, 255, 30): "their hands (before them)",
 (1, 2, 1): "All praise",
 (103, 2, 3): "surely in",
 (108, 3, 2): "your hater",
}

# Segment translations we author ourselves (partial verses / split verses)
SEG_TR = {
 "2:201:4-14": ("Our Lord, give us good in this world and good in the Hereafter, and protect us from the punishment of the Fire.",
                "হে আমাদের রব, আমাদের দুনিয়াতে কল্যাণ দাও, আখেরাতেও কল্যাণ দাও এবং আমাদের আগুনের শাস্তি থেকে রক্ষা করো।"),
 "20:114:14-17": ("And say: “My Lord, increase me in knowledge.”",
                  "এবং বলো: “হে আমার রব, আমার জ্ঞান বাড়িয়ে দাও।”"),
 "17:24:7-12": ("And say: “My Lord, have mercy on them both, as they raised me when I was small.”",
                "এবং বলো: “হে আমার রব, তাঁদের দুজনের প্রতি দয়া করো, যেমন তাঁরা ছোটবেলায় আমাকে লালন-পালন করেছেন।”"),
 "2:255:1-26": ("Allah: there is no god except Him, the Ever-Living, the Sustainer of all. Neither drowsiness nor sleep overtakes Him. To Him belongs whatever is in the heavens and whatever is on the earth. Who could intercede with Him except by His permission?",
                "আল্লাহ, তিনি ছাড়া কোনো ইলাহ নেই, তিনি চিরঞ্জীব, সবকিছুর ধারক। তন্দ্রা বা ঘুম তাঁকে স্পর্শ করে না। আকাশসমূহ ও পৃথিবীতে যা কিছু আছে সবই তাঁর। কে আছে যে তাঁর অনুমতি ছাড়া তাঁর কাছে সুপারিশ করবে?"),
 "2:255:27-50": ("He knows what is before them and what is behind them, and they grasp nothing of His knowledge except what He wills. His Kursi extends over the heavens and the earth, and guarding them does not tire Him. He is the Most High, the Magnificent.",
                 "তাদের সামনে ও পেছনে যা আছে সবই তিনি জানেন। তিনি যতটুকু চান তা ছাড়া তাঁর জ্ঞানের কিছুই তারা আয়ত্ত করতে পারে না। তাঁর কুরসি আকাশসমূহ ও পৃথিবী পরিব্যাপ্ত, আর এ দুটির রক্ষণাবেক্ষণ তাঁকে ক্লান্ত করে না। তিনি সর্বোচ্চ, মহান।"),
}

# ---------------------------------------------------------------------------
# Hand-authored lines (not Quran verses). Each token: (arabic, en, bn, lemma_key or None, [patterns])
def L(id, en, bn, tokens, note_en="", note_bn=""):
    return dict(id=id, en=en, bn=bn, tokens=tokens, note_en=note_en, note_bn=note_bn)

ALLAH = ("ٱللَّهُ", "Allah", "আল্লাহ", "اللَّه|أله", [])
SALAH = [
 L("takbir", "Allah is the Greatest.", "আল্লাহ সবচেয়ে বড়।", [
    ALLAH, ("أَكۡبَرُ", "is the Greatest", "সবচেয়ে বড়", "أَكْبَر|كبر", [])],
   "Said to start the prayer and at every movement.", "নামাজ শুরু ও প্রতিটি ওঠা-নামায় বলা হয়।"),
 L("ruku", "Glory be to my Lord, the Magnificent.", "পবিত্র আমার মহান রব।", [
    ("سُبۡحَٰنَ", "Glory be to", "পবিত্রতা", "سُبْحان|سبح", []),
    ("رَبِّيَ", "my Lord", "আমার রব", "رَبّ|ربب", ["i"]),
    ("ٱلۡعَظِيمِ", "the Magnificent", "মহান", "عَظِيم|عظم", ["al"])],
   "In rukūʿ (bowing).", "রুকুতে বলা হয়।"),
 L("sami", "Allah hears whoever praises Him.", "যে আল্লাহর প্রশংসা করে, আল্লাহ তার কথা শোনেন।", [
    ("سَمِعَ", "hears", "শোনেন", "سَمِعَ|سمع", []), ALLAH,
    ("لِمَنۡ", "the one who", "যে", "مَن|", ["li"]),
    ("حَمِدَهُۥ", "praises Him", "তাঁর প্রশংসা করে", "X:hamida", ["hu"])],
   "Rising from rukūʿ.", "রুকু থেকে ওঠার সময়।"),
 L("rabbana", "Our Lord, and to You belongs all praise.", "হে আমাদের রব, সব প্রশংসা তোমারই।", [
    ("رَبَّنَا", "Our Lord", "হে আমাদের রব", "رَبّ|ربب", ["na"]),
    ("وَلَكَ", "and to You", "এবং তোমারই", "PRON:2MS", ["wa", "li"]),
    ("ٱلۡحَمۡدُ", "all praise", "সব প্রশংসা", "حَمْد|حمد", ["al"])],
   "Standing after rukūʿ.", "রুকুর পর দাঁড়িয়ে।"),
 L("sujud", "Glory be to my Lord, the Most High.", "পবিত্র আমার রব, যিনি সর্বোচ্চ।", [
    ("سُبۡحَٰنَ", "Glory be to", "পবিত্রতা", "سُبْحان|سبح", []),
    ("رَبِّيَ", "my Lord", "আমার রব", "رَبّ|ربب", ["i"]),
    ("ٱلۡأَعۡلَىٰ", "the Most High", "সর্বোচ্চ", "أَعْلَى|علو", ["al"])],
   "In sujūd (prostration).", "সিজদায় বলা হয়।"),
 L("jalsa", "My Lord, forgive me.", "হে আমার রব, আমাকে ক্ষমা করো।", [
    ("رَبِّ", "my Lord", "হে আমার রব", "رَبّ|ربب", []),
    ("ٱغۡفِرۡ", "forgive", "ক্ষমা করো", "غَفَرَ|غفر", ["cmd"]),
    ("لِي", "me", "আমাকে", "PRON:1S", ["li"])],
   "Sitting between the two prostrations.", "দুই সিজদার মাঝে বসে।"),
]

SHAHADA1 = [("أَشۡهَدُ", "I bear witness", "আমি সাক্ষ্য দিই", "شَهِدَ|شهد", ["i_do"]),
            ("أَن", "that", "যে", "أَن|", []),
            ("لَّآ", "(there is) no", "নেই", "لا|", []),
            ("إِلَٰهَ", "god", "কোনো ইলাহ", "إِلٰه|أله", []),
            ("إِلَّا", "except", "ছাড়া", "إِلّا|", []), ALLAH]
SALAT = ("ٱلصَّلَوٰةِ", "the prayer", "নামাজ", "صَلاة|صلو", ["al"])
AZAN = [
 L("az_takbir", "Allah is the Greatest.", "আল্লাহ সবচেয়ে বড়।", SALAH[0]["tokens"], "Said four times at the start.", "শুরুতে চারবার।"),
 L("az_shahada1", "I bear witness that there is no god except Allah.", "আমি সাক্ষ্য দিচ্ছি যে আল্লাহ ছাড়া কোনো ইলাহ নেই।", SHAHADA1),
 L("az_shahada2", "I bear witness that Muhammad is the Messenger of Allah.", "আমি সাক্ষ্য দিচ্ছি যে মুহাম্মাদ ﷺ আল্লাহর রাসূল।", [
    SHAHADA1[0], ("أَنَّ", "that", "যে", "أَنّ|", []),
    ("مُحَمَّدٗا", "Muhammad", "মুহাম্মাদ", "مُحَمَّد|حمد", []),
    ("رَّسُولُ", "(is the) Messenger", "রাসূল", "رَسُول|رسل", []),
    ("ٱللَّهِ", "of Allah", "আল্লাহর", "اللَّه|أله", [])]),
 L("az_hayya_salah", "Come to the prayer.", "নামাজের দিকে এসো।", [
    ("حَيَّ", "Come!", "এসো", "X:hayya", []), ("عَلَى", "to", "দিকে", "عَلَى|", []), SALAT]),
 L("az_hayya_falah", "Come to success.", "সফলতার দিকে এসো।", [
    ("حَيَّ", "Come!", "এসো", "X:hayya", []), ("عَلَى", "to", "দিকে", "عَلَى|", []),
    ("ٱلۡفَلَاحِ", "success", "সফলতা", "X:falah", ["al"])]),
 L("az_fajr", "Prayer is better than sleep.", "ঘুমের চেয়ে নামাজ উত্তম।", [
    ("ٱلصَّلَوٰةُ", "The prayer", "নামাজ", "صَلاة|صلو", ["al"]),
    ("خَيۡرٞ", "(is) better", "উত্তম", "خَيْر|خير", []),
    ("مِّنَ", "than", "চেয়ে", "مِن|", []),
    ("ٱلنَّوۡمِ", "sleep", "ঘুম", "نَوْم|نوم", ["al"])], "Added in the Fajr azan.", "ফজরের আজানে।"),
 L("az_iqamah", "The prayer has begun.", "নামাজ শুরু হয়ে গেছে।", [
    ("قَدۡ", "Indeed", "অবশ্যই", "قَد|", []),
    ("قَامَتِ", "has stood (begun)", "দাঁড়িয়ে গেছে", "قامَ|قوم", []),
    ("ٱلصَّلَوٰةُ", "the prayer", "নামাজ", "صَلاة|صلو", ["al"])], "Said in the iqamah.", "ইকামতে বলা হয়।"),
 L("az_end", "There is no god except Allah.", "আল্লাহ ছাড়া কোনো ইলাহ নেই।", SHAHADA1[2:]),
]

SALAM = ("ٱلسَّلَٰمُ", "Peace", "শান্তি", "سَلام|سلم", ["al"])
TASHAHHUD = [
 L("t1", "All greetings are for Allah, and all prayers and all good things.",
   "সব অভিবাদন আল্লাহর জন্য, সব নামাজ ও সব পবিত্র বিষয়ও।", [
    ("ٱلتَّحِيَّاتُ", "All greetings", "সব অভিবাদন", "تَحِيَّة|حيي", ["al"]),
    ("لِلَّهِ", "(are) for Allah", "আল্লাহর জন্য", "اللَّه|أله", ["li"]),
    ("وَٱلصَّلَوَٰتُ", "and the prayers", "এবং নামাজসমূহ", "صَلاة|صلو", ["wa", "al"]),
    ("وَٱلطَّيِّبَٰتُ", "and the good things", "এবং পবিত্র বিষয়সমূহ", "طَيِّب|طيب", ["wa", "al"])]),
 L("t2", "Peace be upon you, O Prophet, and the mercy of Allah and His blessings.",
   "হে নবী, আপনার উপর শান্তি, আল্লাহর রহমত ও তাঁর বরকত।", [
    SALAM, ("عَلَيۡكَ", "upon you", "আপনার উপর", "عَلَى|", ["ka"]),
    ("أَيُّهَا", "O", "হে", "أَيُّها|", []),
    ("ٱلنَّبِيُّ", "Prophet", "নবী", "نَبِيّ|نبأ", ["al"]),
    ("وَرَحۡمَةُ", "and the mercy", "এবং রহমত", "رَحْمَة|رحم", ["wa"]),
    ("ٱللَّهِ", "of Allah", "আল্লাহর", "اللَّه|أله", []),
    ("وَبَرَكَٰتُهُۥ", "and His blessings", "এবং তাঁর বরকত", "بَرَكَة|برك", ["wa", "hu"])]),
 L("t3", "Peace be upon us and upon the righteous servants of Allah.",
   "শান্তি আমাদের উপর এবং আল্লাহর নেক বান্দাদের উপর।", [
    SALAM, ("عَلَيۡنَا", "upon us", "আমাদের উপর", "عَلَى|", ["na"]),
    ("وَعَلَىٰ", "and upon", "এবং উপর", "عَلَى|", ["wa"]),
    ("عِبَادِ", "the servants", "বান্দাদের", "عَبْد|عبد", []),
    ("ٱللَّهِ", "of Allah", "আল্লাহর", "اللَّه|أله", []),
    ("ٱلصَّٰلِحِينَ", "the righteous", "নেককার", "صالِح|صلح", ["al", "plural", "doer"])]),
 L("t4", "I bear witness that there is no god except Allah.", "আমি সাক্ষ্য দিচ্ছি যে আল্লাহ ছাড়া কোনো ইলাহ নেই।", SHAHADA1),
 L("t5", "And I bear witness that Muhammad is His servant and His Messenger.",
   "এবং আমি সাক্ষ্য দিচ্ছি যে মুহাম্মাদ ﷺ তাঁর বান্দা ও রাসূল।", [
    ("وَأَشۡهَدُ", "And I bear witness", "এবং আমি সাক্ষ্য দিই", "شَهِدَ|شهد", ["wa", "i_do"]),
    ("أَنَّ", "that", "যে", "أَنّ|", []),
    ("مُحَمَّدًا", "Muhammad", "মুহাম্মাদ", "مُحَمَّد|حمد", []),
    ("عَبۡدُهُۥ", "(is) His servant", "তাঁর বান্দা", "عَبْد|عبد", ["hu"]),
    ("وَرَسُولُهُۥ", "and His Messenger", "এবং তাঁর রাসূল", "رَسُول|رسل", ["wa", "hu"])]),
 L("taslim", "Peace be upon you and the mercy of Allah.", "আপনাদের উপর শান্তি ও আল্লাহর রহমত।", [
    SALAM, ("عَلَيۡكُمۡ", "upon you (all)", "আপনাদের উপর", "عَلَى|", ["kum"]),
    ("وَرَحۡمَةُ", "and the mercy", "এবং রহমত", "رَحْمَة|رحم", ["wa"]),
    ("ٱللَّهِ", "of Allah", "আল্লাহর", "اللَّه|أله", [])],
   "Turning the head right and left to end the prayer.", "নামাজ শেষে ডানে-বামে সালাম ফেরানো।"),
]

HAND = {"salah": SALAH, "azan": AZAN, "tashahhud": TASHAHHUD}

# ---------------------------------------------------------------------------
# Texts (things the learner "unlocks" and can read) — segments are (s, v, from_word, to_word) or hand line ids
def Q(s, v, a=None, b=None): return ("q", s, v, a, b)
TEXTS = [
 dict(id="fatiha", en="Al-Fatiha", bn="সূরা আল-ফাতিহা", ar="ٱلۡفَاتِحَة", emoji="🌅",
      desc_en="Recited at least 17 times a day in salah.", desc_bn="প্রতিদিন নামাজে অন্তত ১৭ বার পড়া হয়।",
      segs=[Q(1, v) for v in range(1, 8)]),
 dict(id="salah", en="Salah: bowing & prostrating", bn="নামাজের তাসবিহ", ar="أَذۡكَارُ ٱلصَّلَاة", emoji="🕌",
      desc_en="What you say in rukūʿ, sujūd and between them.", desc_bn="রুকু, সিজদা ও তার মাঝে যা বলি।",
      segs=[("h", "salah", l["id"]) for l in SALAH]),
 dict(id="ikhlas", en="Al-Ikhlas", bn="সূরা আল-ইখলাস", ar="ٱلۡإِخۡلَاص", emoji="☝️",
      desc_en="Equal to a third of the Quran.", desc_bn="কুরআনের এক-তৃতীয়াংশের সমান।",
      segs=[Q(112, v) for v in range(1, 5)]),
 dict(id="azan", en="The Azan", bn="আজান", ar="ٱلۡأَذَان", emoji="📢",
      desc_en="The call you hear five times a day.", desc_bn="দিনে পাঁচবার যে ডাক শুনি।",
      segs=[("h", "azan", l["id"]) for l in AZAN]),
 dict(id="kawthar", en="Al-Kawthar", bn="সূরা আল-কাওসার", ar="ٱلۡكَوۡثَر", emoji="🏞️",
      desc_en="The shortest surah.", desc_bn="সবচেয়ে ছোট সূরা।",
      segs=[Q(108, v) for v in range(1, 4)]),
 dict(id="asr", en="Al-Asr", bn="সূরা আল-আসর", ar="ٱلۡعَصۡر", emoji="🌇",
      desc_en="The whole of success in three verses.", desc_bn="তিন আয়াতে সফলতার পুরো সূত্র।",
      segs=[Q(103, v) for v in range(1, 4)]),
 dict(id="nasr", en="An-Nasr", bn="সূরা আন-নাসর", ar="ٱلنَّصۡر", emoji="🏆",
      desc_en="When the help of Allah comes.", desc_bn="যখন আল্লাহর সাহায্য আসে।",
      segs=[Q(110, v) for v in range(1, 4)]),
 dict(id="falaq", en="Al-Falaq", bn="সূরা আল-ফালাক", ar="ٱلۡفَلَق", emoji="🌅",
      desc_en="Seeking refuge with the Lord of daybreak.", desc_bn="ভোরের রবের কাছে আশ্রয়।",
      segs=[Q(113, v) for v in range(1, 6)]),
 dict(id="nas", en="An-Nas", bn="সূরা আন-নাস", ar="ٱلنَّاس", emoji="👥",
      desc_en="Protection from the whisperer.", desc_bn="কুমন্ত্রণাদাতা থেকে আশ্রয়।",
      segs=[Q(114, v) for v in range(1, 7)]),
 dict(id="tashahhud", en="Tashahhud", bn="তাশাহহুদ", ar="ٱلتَّشَهُّد", emoji="🤲",
      desc_en="What you say while sitting in salah.", desc_bn="নামাজে বসে যা পড়ি।",
      segs=[("h", "tashahhud", l["id"]) for l in TASHAHHUD]),
 dict(id="duas", en="Duas from the Quran", bn="কুরআনের দোয়া", ar="أَدۡعِيَة قُرۡآنِيَّة", emoji="🤲",
      desc_en="Five duas you can make every day.", desc_bn="প্রতিদিনের পাঁচটি দোয়া।",
      segs=[Q(2, 201, 4, 14), Q(20, 114, 14, 17), Q(17, 24, 7, 12), Q(7, 23), Q(14, 41)]),
 dict(id="kursi", en="Ayat al-Kursi", bn="আয়াতুল কুরসি", ar="آيَةُ ٱلۡكُرۡسِيّ", emoji="💠",
      desc_en="The greatest verse of the Quran.", desc_bn="কুরআনের সবচেয়ে মহান আয়াত।",
      segs=[Q(2, 255)]),
]

# Units = the learning path. Each teaches the words in `segs`; `completes` marks the text as fully understood.
UNITS = [
 dict(id="u1", text="fatiha", en="Bismillah & Al-Fatiha 1–4", bn="বিসমিল্লাহ ও ফাতিহা ১–৪", segs=[Q(1, v) for v in range(1, 5)]),
 dict(id="u2", text="fatiha", en="Al-Fatiha 5–7", bn="ফাতিহা ৫–৭", segs=[Q(1, v) for v in range(5, 8)], completes="fatiha"),
 dict(id="u3", text="salah", en="In salah", bn="নামাজে", completes="salah"),
 dict(id="u4", text="ikhlas", en="Al-Ikhlas", bn="আল-ইখলাস", completes="ikhlas"),
 dict(id="u5", text="azan", en="The Azan", bn="আজান", completes="azan"),
 dict(id="u6", text="kawthar", en="Al-Kawthar", bn="আল-কাওসার", completes="kawthar"),
 dict(id="u7", text="asr", en="Al-Asr", bn="আল-আসর", completes="asr"),
 dict(id="u8", text="nasr", en="An-Nasr", bn="আন-নাসর", completes="nasr"),
 dict(id="u9", text="falaq", en="Al-Falaq", bn="আল-ফালাক", completes="falaq"),
 dict(id="u10", text="nas", en="An-Nas", bn="আন-নাস", completes="nas"),
 dict(id="u11", text="tashahhud", en="Tashahhud", bn="তাশাহহুদ", completes="tashahhud"),
 dict(id="u12", text="duas", en="Duas from the Quran", bn="কুরআনের দোয়া", completes="duas"),
 dict(id="u13", text="kursi", en="Ayat al-Kursi 1", bn="আয়াতুল কুরসি ১", segs=[Q(2, 255, 1, 26)]),
 dict(id="u14", text="kursi", en="Ayat al-Kursi 2", bn="আয়াতুল কুরসি ২", segs=[Q(2, 255, 27, 50)], completes="kursi"),
]

# ---------------------------------------------------------------------------
# Pattern cards — the "salt". No grammar terms; each says what the piece *does*.
PATTERNS = [
 dict(id="al", ar="ٱلۡـ", en="the", bn="নির্দিষ্ট (the)", emoji="👉",
      expl_en="ٱلۡـ at the start of a word means “the”. Sometimes the ل is silent and the next letter doubles: ٱلرَّحِيمِ = ar-raḥīm.",
      expl_bn="শব্দের শুরুতে ٱلۡـ মানে নির্দিষ্ট করা (the)। কখনো ل উচ্চারিত হয় না, পরের অক্ষরে তাশদীদ পড়ে: ٱلرَّحِيمِ।"),
 dict(id="wa", ar="وَ", en="and", bn="এবং", emoji="➕",
      expl_en="وَ stuck to the front of a word means “and”. At the start of a surah it can mean “By…!” (an oath): وَٱلۡعَصۡرِ = By time!",
      expl_bn="শব্দের সামনে وَ মানে “এবং”। সূরার শুরুতে শপথ বোঝায়: وَٱلۡعَصۡرِ = সময়ের শপথ!"),
 dict(id="bi", ar="بِـ", en="in / with / by", bn="দিয়ে / সাথে / -তে", emoji="🔗",
      expl_en="بِـ on the front means “in, with, by”: بِسۡمِ = in the name, بِٱلۡحَقِّ = with the truth.",
      expl_bn="সামনে بِـ মানে “দিয়ে, সাথে, -তে”: بِسۡمِ = নামে, بِٱلۡحَقِّ = সত্যের সাথে।"),
 dict(id="li", ar="لِـ", en="for / belongs to", bn="জন্য / -র", emoji="🎯",
      expl_en="لِـ means “for, to, belongs to”: لِلَّهِ = for Allah (belongs to Allah).",
      expl_bn="لِـ মানে “জন্য, -র”: لِلَّهِ = আল্লাহর জন্য।"),
 dict(id="fa", ar="فَـ", en="so / then", bn="তাই / তখন", emoji="⏭️",
      expl_en="فَـ on the front means “so, then”: فَصَلِّ = so pray.",
      expl_bn="সামনে فَـ মানে “তাই, তখন”: فَصَلِّ = তাই নামাজ পড়ো।"),
 dict(id="na", ar="ـنَا", en="us / our", bn="আমাদের", emoji="👨‍👩‍👧",
      expl_en="ـنَا at the end means “us, our”: رَبَّنَا = our Lord, ٱهۡدِنَا = guide us.",
      expl_bn="শেষে ـنَا মানে “আমাদের”: رَبَّنَا = আমাদের রব, ٱهۡدِنَا = আমাদের পথ দেখাও।"),
 dict(id="ka", ar="ـكَ", en="you / your", bn="তোমার / তোমাকে", emoji="🫵",
      expl_en="ـكَ at the end means “you, your”: رَبِّكَ = your Lord, لَكَ = for you.",
      expl_bn="শেষে ـكَ মানে “তুমি, তোমার”: رَبِّكَ = তোমার রব।"),
 dict(id="kum", ar="ـكُمۡ", en="you all / your (plural)", bn="তোমাদের", emoji="👥",
      expl_en="ـكُمۡ is “you” for many people: عَلَيۡكُمۡ = upon you all.",
      expl_bn="ـكُمۡ মানে “তোমাদের” (অনেকে): عَلَيۡكُمۡ = তোমাদের উপর।"),
 dict(id="hu", ar="ـهُۥ / ـهِۦ", en="him / his / it", bn="তাঁর / তাঁকে", emoji="👆",
      expl_en="ـهُۥ or ـهِۦ at the end means “him, his, it”: عَبۡدُهُۥ = His servant.",
      expl_bn="শেষে ـهُۥ / ـهِۦ মানে “তাঁর, তাঁকে”: عَبۡدُهُۥ = তাঁর বান্দা।"),
 dict(id="hum", ar="ـهُمۡ / ـهِمۡ", en="them / their", bn="তাদের", emoji="👥",
      expl_en="ـهُمۡ or ـهِمۡ at the end means “them, their”: عَلَيۡهِمۡ = upon them.",
      expl_bn="শেষে ـهُمۡ / ـهِمۡ মানে “তাদের”: عَلَيۡهِمۡ = তাদের উপর।"),
 dict(id="huma", ar="ـهُمَا", en="both of them", bn="তাদের দুজনের", emoji="✌️",
      expl_en="ـهُمَا means “the two of them”: ٱرۡحَمۡهُمَا = have mercy on them both.",
      expl_bn="ـهُمَا মানে “তাদের দুজন”: ٱرۡحَمۡهُمَا = তাঁদের দুজনকে দয়া করো।"),
 dict(id="i", ar="ـِي / ـِيَ", en="me / my", bn="আমার / আমাকে", emoji="🙋",
      expl_en="ـِي at the end means “me, my”: رَبِّي = my Lord, زِدۡنِي = increase me.",
      expl_bn="শেষে ـِي মানে “আমার, আমাকে”: رَبِّي = আমার রব।"),
 dict(id="we_do", ar="نَـ…", en="we do…", bn="আমরা করি…", emoji="👨‍👩‍👧",
      expl_en="A verb starting with نَـ (or نُـ) means “we do…”: نَعۡبُدُ = we worship.",
      expl_bn="ক্রিয়া نَـ দিয়ে শুরু হলে মানে “আমরা করি”: نَعۡبُدُ = আমরা ইবাদত করি।"),
 dict(id="i_do", ar="أَ…", en="I do…", bn="আমি করি…", emoji="🙋",
      expl_en="A verb starting with أَ (or أُ) means “I do…”: أَعُوذُ = I seek refuge, أَشۡهَدُ = I bear witness.",
      expl_bn="ক্রিয়া أَ দিয়ে শুরু হলে মানে “আমি করি”: أَعُوذُ = আমি আশ্রয় চাই।"),
 dict(id="ya", ar="يَـ…", en="he does… / they do…", bn="সে করে… / তারা করে…", emoji="👤",
      expl_en="A verb starting with يَـ (or يُـ) means “he does…”; with ـُونَ at the end, “they do…”: يَعۡلَمُ = He knows, يَدۡخُلُونَ = they enter.",
      expl_bn="ক্রিয়া يَـ দিয়ে শুরু হলে “সে করে”; শেষে ـُونَ থাকলে “তারা করে”: يَعۡلَمُ = তিনি জানেন।"),
 dict(id="you_did", ar="…تَ", en="you did…", bn="তুমি করেছ…", emoji="🫵",
      expl_en="A past verb ending in ـتَ means “you did…”: أَنۡعَمۡتَ = You blessed, رَأَيۡتَ = you saw.",
      expl_bn="অতীত ক্রিয়ার শেষে ـتَ মানে “তুমি করেছ”: أَنۡعَمۡتَ = তুমি নিয়ামত দিয়েছ।"),
 dict(id="we_did", ar="…نَا", en="we did…", bn="আমরা করেছি…", emoji="👨‍👩‍👧",
      expl_en="A past verb ending in ـنَا means “we did…”: ظَلَمۡنَا = we wronged.",
      expl_bn="অতীত ক্রিয়ার শেষে ـنَا মানে “আমরা করেছি”: ظَلَمۡنَا = আমরা জুলুম করেছি।"),
 dict(id="they_did", ar="…ُوا", en="they did…", bn="তারা করেছে…", emoji="👥",
      expl_en="A past verb ending in ـُواْ means “they did…”: ءَامَنُواْ = they believed, عَمِلُواْ = they did.",
      expl_bn="অতীত ক্রিয়ার শেষে ـُواْ মানে “তারা করেছে”: ءَامَنُواْ = তারা ঈমান এনেছে।"),
 dict(id="cmd", ar="!", en="Do it! (a command)", bn="করো! (আদেশ)", emoji="📢",
      expl_en="Many short words are commands: قُلۡ = Say!, ٱهۡدِنَا = Guide us!, ٱغۡفِرۡ = Forgive! In a dua, a command is a humble request.",
      expl_bn="অনেক ছোট শব্দ আদেশ: قُلۡ = বলো!, ٱغۡفِرۡ = ক্ষমা করো! দোয়ায় এটা বিনীত অনুরোধ।"),
 dict(id="plural", ar="ـِينَ / ـُونَ", en="many people", bn="বহুবচন (অনেকে)", emoji="👥",
      expl_en="ـِينَ or ـُونَ at the end often makes “many people”: مُؤۡمِن (a believer) → مُؤۡمِنِينَ (believers).",
      expl_bn="শেষে ـِينَ / ـُونَ থাকলে প্রায়ই বহুবচন: مُؤۡمِن (মুমিন) → مُؤۡمِنِينَ (মুমিনরা)।"),
 dict(id="doer", ar="فَاعِل", en="the doer", bn="যে করে", emoji="🧑‍🔧",
      expl_en="The shape ـَاـِـ (fāʿil) means “the one who does it”: مَٰلِك = owner, حَاسِد = envier, كَاتِب = writer (Bangla কাতিব).",
      expl_bn="ـَاـِـ (ফা‘ইল) গড়ন মানে “যে করে”: مَٰلِك = মালিক, حَاسِد = হিংসুক, كَاتِب = লেখক (কাতিব)।"),
 dict(id="done_to", ar="مَفۡعُول", en="the one it's done to", bn="যার প্রতি করা হয়", emoji="🎯",
      expl_en="The shape مَـ…ـُو… (mafʿūl) means “the one it is done to”: مَغۡضُوب = one under anger, مَحۡمُود (Mahmud) = praised, مَحۡبُوب (Mahbub) = beloved.",
      expl_bn="মাফ‘উল গড়ন মানে “যার প্রতি করা হয়”: مَغۡضُوب = গজবপ্রাপ্ত, مَحۡمُود (মাহমুদ) = প্রশংসিত, مَحۡبُوب (মাহবুব) = প্রিয়।"),
]

# ---------------------------------------------------------------------------
# STRUCTURES — sentence shapes. Each is shown (1) in the text the learner knows, (2) elsewhere in the
# Quran, (3) in everyday sentences the learner builds. Everyday words are all Quranic where possible.
BN.update({
 "2:2": ["সেই", "কিতাব"],
})
SEG_TR.update({
 "2:2:1-2": ("That is the Book", "এটি সেই কিতাব"),
 "112:1:2-4": ("He is Allah, One.", "তিনি আল্লাহ, এক।"),
 "1:2:3-4": ("the Lord of the worlds", "জগতসমূহের রব"),
 "1:2:1-2": ("All praise is for Allah", "সব প্রশংসা আল্লাহর"),
 "110:1:3-4": ("the help of Allah", "আল্লাহর সাহায্য"),
 "1:4:1-3": ("Master of the Day of Judgment", "বিচার দিনের মালিক"),
 "1:6:2-3": ("the straight path", "সরল পথ"),
 "2:255:49-50": ("the Most High, the Magnificent", "সর্বোচ্চ, মহান"),
 "1:5:1-2": ("You alone we worship", "আমরা কেবল তোমারই ইবাদত করি"),
 "103:3:2-5": ("those who believe and do good deeds", "যারা ঈমান আনে ও সৎকাজ করে"),
 "1:7:1-3": ("the path of those You have blessed", "তাদের পথ, যাদের তুমি নিয়ামত দিয়েছ"),
 "108:3": ("Indeed, your enemy is the one cut off.", "নিশ্চয়ই তোমার শত্রুই নির্বংশ।"),
})

def E(id, en, bn, tokens):
    """An everyday sentence the learner builds. tokens: (arabic, en, bn, key, patterns)"""
    return dict(id=id, en=en, bn=bn, tokens=tokens, everyday=True)

HADHA = ("هَٰذَا", "This (is)", "এটি", "ذا|", [])
DHALIKA = ("ذَٰلِكَ", "That (is)", "ওটি", "ذا|", [])
EVERYDAY = [
 # "is" is invisible
 E("e_pen", "This is a pen.", "এটি একটি কলম।", [HADHA, ("قَلَمٌ", "a pen", "একটি কলম", "قَلَم|قلم", [])]),
 E("e_house", "That is a house.", "ওটি একটি ঘর।", [DHALIKA, ("بَيۡتٌ", "a house", "একটি ঘর", "بَيْت|بيت", [])]),
 E("e_book", "This is a book.", "এটি একটি বই।", [HADHA, ("كِتَابٌ", "a book", "একটি বই", "كِتاب|كتب", [])]),
 E("e_father", "He is my father.", "তিনি আমার বাবা।", [("هُوَ", "He (is)", "তিনি", "PRON:3MS", []), ("أَبِي", "my father", "আমার বাবা", "أَب|أبو", ["i"])]),
 E("e_mother", "She is my mother.", "তিনি আমার মা।", [("هِيَ", "She (is)", "তিনি", "PRON:3FS", []), ("أُمِّي", "my mother", "আমার মা", "أُمّ|أمم", ["i"])]),
 E("e_rabbi", "Allah is my Lord.", "আল্লাহ আমার রব।", [("ٱللَّهُ", "Allah (is)", "আল্লাহ", "اللَّه|أله", []), ("رَبِّي", "my Lord", "আমার রব", "رَبّ|ربب", ["i"])]),
 # "of" is invisible
 E("e_kitabullah", "the Book of Allah", "আল্লাহর কিতাব", [("كِتَابُ", "the Book (of)", "কিতাব", "كِتاب|كتب", []), ("ٱللَّهِ", "Allah", "আল্লাহর", "اللَّه|أله", [])]),
 E("e_baytabi", "my father's house", "আমার বাবার ঘর", [("بَيۡتُ", "the house (of)", "ঘর", "بَيْت|بيت", []), ("أَبِي", "my father", "আমার বাবার", "أَب|أبو", ["i"])]),
 E("e_qalamummi", "my mother's pen", "আমার মায়ের কলম", [("قَلَمُ", "the pen (of)", "কলম", "قَلَم|قلم", []), ("أُمِّي", "my mother", "আমার মায়ের", "أُمّ|أمم", ["i"])]),
 E("e_baytullah", "This is the House of Allah.", "এটি আল্লাহর ঘর।", [HADHA, ("بَيۡتُ", "the house (of)", "ঘর", "بَيْت|بيت", []), ("ٱللَّهِ", "Allah", "আল্লাহর", "اللَّه|أله", [])]),
 # describing word comes after
 E("e_bigmasjid", "a big mosque", "একটি বড় মসজিদ", [("مَسۡجِدٌ", "a mosque", "একটি মসজিদ", "مَسْجِد|سجد", []), ("كَبِيرٌ", "big", "বড়", "كَبِير|كبر", [])]),
 E("e_thebighouse", "the big house", "বড় ঘরটি", [("ٱلۡبَيۡتُ", "the house", "ঘরটি", "بَيْت|بيت", ["al"]), ("ٱلۡكَبِيرُ", "the big", "বড়", "كَبِير|كبر", ["al"])]),
 E("e_houseisbig", "The house is big.", "ঘরটি বড়।", [("ٱلۡبَيۡتُ", "The house (is)", "ঘরটি", "بَيْت|بيت", ["al"]), ("كَبِيرٌ", "big", "বড়", "كَبِير|كبر", [])]),
 E("e_newpen", "The pen is new.", "কলমটি নতুন।", [("ٱلۡقَلَمُ", "The pen (is)", "কলমটি", "قَلَم|قلم", ["al"]), ("جَدِيدٌ", "new", "নতুন", "جَدِيد|جدد", [])]),
 E("e_masjidnear", "The mosque is near.", "মসজিদটি কাছে।", [("ٱلۡمَسۡجِدُ", "The mosque (is)", "মসজিদটি", "مَسْجِد|سجد", ["al"]), ("قَرِيبٌ", "near", "কাছে", "قَرِيب|قرب", [])]),
 E("e_thisbigmasjid", "This is a big mosque.", "এটি একটি বড় মসজিদ।", [HADHA, ("مَسۡجِدٌ", "a mosque", "একটি মসজিদ", "مَسْجِد|سجد", []), ("كَبِيرٌ", "big", "বড়", "كَبِير|كبر", [])]),
 # the verb shows who
 E("e_weread", "We read the Quran.", "আমরা কুরআন পড়ি।", [("نَقۡرَأُ", "We read", "আমরা পড়ি", "قَرَأَ|قرأ", ["we_do"]), ("ٱلۡقُرۡءَانَ", "the Quran", "কুরআন", "قُرْءان|قرأ", ["al"])]),
 E("e_iwrite", "I write with the pen.", "আমি কলম দিয়ে লিখি।", [("أَكۡتُبُ", "I write", "আমি লিখি", "كَتَبَ|كتب", ["i_do"]), ("بِٱلۡقَلَمِ", "with the pen", "কলম দিয়ে", "قَلَم|قلم", ["bi", "al"])]),
 E("e_fathergoes", "My father goes to the mosque.", "আমার বাবা মসজিদে যান।", [("يَذۡهَبُ", "goes", "যান", "ذَهَبَ|ذهب", ["ya"]), ("أَبِي", "my father", "আমার বাবা", "أَب|أبو", ["i"]), ("إِلَى", "to", "দিকে", "إِلَى|", []), ("ٱلۡمَسۡجِدِ", "the mosque", "মসজিদ", "مَسْجِد|سجد", ["al"])]),
 E("e_wego", "We go to the mosque.", "আমরা মসজিদে যাই।", [("نَذۡهَبُ", "We go", "আমরা যাই", "ذَهَبَ|ذهب", ["we_do"]), ("إِلَى", "to", "দিকে", "إِلَى|", []), ("ٱلۡمَسۡجِدِ", "the mosque", "মসজিদ", "مَسْجِد|سجد", ["al"])]),
 # inna / alladhina
 E("e_innahouse", "Indeed, the house is near.", "নিশ্চয়ই ঘরটি কাছে।", [("إِنَّ", "Indeed", "নিশ্চয়ই", "إِنّ|", []), ("ٱلۡبَيۡتَ", "the house", "ঘরটি", "بَيْت|بيت", ["al"]), ("قَرِيبٌ", "(is) near", "কাছে", "قَرِيب|قرب", [])]),
 E("e_innaallah", "Indeed, Allah is near.", "নিশ্চয়ই আল্লাহ কাছে।", [("إِنَّ", "Indeed", "নিশ্চয়ই", "إِنّ|", []), ("ٱللَّهَ", "Allah", "আল্লাহ", "اللَّه|أله", []), ("قَرِيبٌ", "(is) near", "কাছে", "قَرِيب|قرب", [])]),
 E("e_alladhi", "the one who reads the Quran", "যে কুরআন পড়ে", [("ٱلَّذِي", "the one who", "যে", "الَّذِي|", []), ("يَقۡرَأُ", "reads", "পড়ে", "قَرَأَ|قرأ", ["ya"]), ("ٱلۡقُرۡءَانَ", "the Quran", "কুরআন", "قُرْءان|قرأ", ["al"])]),
 E("e_alladhina", "those who went to the mosque", "যারা মসজিদে গেল", [("ٱلَّذِينَ", "those who", "যারা", "الَّذِي|", []), ("ذَهَبُواْ", "went", "গেল", "ذَهَبَ|ذهب", ["they_did"]), ("إِلَى", "to", "দিকে", "إِلَى|", []), ("ٱلۡمَسۡجِدِ", "the mosque", "মসজিদ", "مَسْجِد|سجد", ["al"])]),
]

def S(id, unit, en, bn, emoji, shape, expl_en, expl_bn, quran, everyday, chunk=None):
    return dict(id=id, unit=unit, en=en, bn=bn, emoji=emoji, shape=shape, expl_en=expl_en, expl_bn=expl_bn,
                quran=quran, everyday=everyday, chunk=chunk)

STRUCTURES = [
 S("is", "u1", "“is” is invisible", "“হয়/হচ্ছে” শব্দটি লুকানো", "👻",
   [("ٱللَّهُ", "Allah", "আল্লাহ", "thing"), ("أَكۡبَرُ", "(is) greatest", "সবচেয়ে বড়", "about")],
   "Arabic has no word for “is”. Put two words side by side and you have a sentence: the first is what you're talking about, the second says something about it.",
   "আরবিতে “হয়/হচ্ছে” শব্দ নেই। দুটি শব্দ পাশাপাশি বসালেই বাক্য হয়: প্রথমটি কার কথা, দ্বিতীয়টি তার সম্পর্কে কী।",
   [Q(1, 2, 1, 2), Q(2, 2, 1, 2), Q(112, 1, 2, 4)],
   ["e_pen", "e_house", "e_book", "e_father", "e_mother", "e_rabbi"]),
 S("of", "u1", "“of” is invisible", "“-এর/-র” লুকানো", "🔗",
   [("رَبِّ", "Lord", "রব", "thing"), ("ٱلۡعَٰلَمِينَ", "(of) the worlds", "জগতসমূহের", "whose")],
   "Put a noun right before another one and the second means “of …”: رَبِّ ٱلۡعَٰلَمِينَ = Lord of the worlds. The first word never takes ٱلۡـ.",
   "একটি বিশেষ্যের ঠিক পরে আরেকটি বসালে দ্বিতীয়টির অর্থ হয় “-এর”: رَبِّ ٱلۡعَٰلَمِينَ = জগতসমূহের রব। প্রথম শব্দে কখনো ٱلۡـ বসে না।",
   [Q(1, 2, 3, 4), Q(1, 4, 1, 3), Q(110, 1, 3, 4)],
   ["e_kitabullah", "e_baytabi", "e_qalamummi", "e_baytullah"]),
 S("after", "u2", "The describing word comes after", "বিশেষণ পরে বসে", "🎨",
   [("ٱلصِّرَٰطَ", "the path", "পথ", "thing"), ("ٱلۡمُسۡتَقِيمَ", "the straight", "সরল", "like")],
   "A describing word comes after its noun and copies its ٱلۡـ: ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ = the straight path. If only the first word has ٱلۡـ, it's a sentence: ٱلۡبَيۡتُ كَبِيرٌ = the house is big.",
   "বিশেষণ বিশেষ্যের পরে বসে এবং তার ٱلۡـ নকল করে: ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ = সরল পথ। শুধু প্রথম শব্দে ٱلۡـ থাকলে সেটা বাক্য: ٱلۡبَيۡتُ كَبِيرٌ = ঘরটি বড়।",
   [Q(1, 6, 2, 3), Q(1, 3), Q(2, 255, 49, 50)],
   ["e_bigmasjid", "e_thebighouse", "e_houseisbig", "e_newpen", "e_masjidnear", "e_thisbigmasjid"]),
 S("verb", "u2", "The verb tells you who", "ক্রিয়াই বলে দেয় কে", "🏃",
   [("نَـ", "we", "আমরা", "who"), ("عۡبُدُ", "worship", "ইবাদত করি", "do")],
   "The first letter of a verb tells you who is doing it: نَـ = we, أَ = I, يَـ = he. نَعۡبُدُ = we worship. Arabic often puts the verb first: يَذۡهَبُ أَبِي = goes my father → my father goes. Putting the object first adds “only”: إِيَّاكَ نَعۡبُدُ = You alone we worship.",
   "ক্রিয়ার প্রথম অক্ষর বলে কে করছে: نَـ = আমরা, أَ = আমি, يَـ = সে। আরবিতে প্রায়ই ক্রিয়া আগে আসে: يَذۡهَبُ أَبِي = আমার বাবা যান। কর্ম আগে বসালে “কেবল” অর্থ হয়: إِيَّاكَ نَعۡبُدُ = কেবল তোমারই ইবাদত করি।",
   [Q(1, 5, 1, 2), Q(1, 5)],
   ["e_weread", "e_iwrite", "e_fathergoes", "e_wego"]),
 S("inna", "u7", "إِنَّ = “indeed”", "إِنَّ = “নিশ্চয়ই”", "❗",
   [("إِنَّ", "Indeed", "নিশ্চয়ই", "inna"), ("ٱلۡإِنسَٰنَ", "mankind", "মানুষ", "thing"), ("لَفِي خُسۡرٍ", "(is) surely in loss", "অবশ্যই ক্ষতিতে", "about")],
   "إِنَّ makes a statement strong. The word after it ends in -a (ٱلۡإِنسَٰنَ, ٱللَّهَ). Sometimes لَـ is added for even more force: لَفِي خُسۡرٍ = surely in loss.",
   "إِنَّ বাক্যকে জোরালো করে। এর পরের শব্দ -আ দিয়ে শেষ হয় (ٱلۡإِنسَٰنَ, ٱللَّهَ)। আরও জোর দিতে লَـ যোগ হয়: لَفِي خُسۡرٍ = অবশ্যই ক্ষতিতে।",
   [Q(103, 2), Q(108, 3)],
   ["e_innahouse", "e_innaallah"]),
 S("alladhina", "u7", "ٱلَّذِينَ + verb = “those who …”", "ٱلَّذِينَ + ক্রিয়া = “যারা …”", "👥",
   [("ٱلَّذِينَ", "those who", "যারা", "who"), ("ءَامَنُواْ", "believed", "ঈমান এনেছে", "do")],
   "ٱلَّذِي (one) / ٱلَّذِينَ (many) + a verb = “the one(s) who …”. The Quran's most repeated description of the good: ٱلَّذِينَ ءَامَنُواْ وَعَمِلُواْ ٱلصَّٰلِحَٰتِ — learn it as one phrase.",
   "ٱلَّذِي (একজন) / ٱلَّذِينَ (অনেকে) + ক্রিয়া = “যে / যারা …”। কুরআনে ভালো মানুষের সবচেয়ে বেশি আসা বর্ণনা: ٱلَّذِينَ ءَامَنُواْ وَعَمِلُواْ ٱلصَّٰلِحَٰتِ — পুরোটা একসাথে শিখুন।",
   [Q(103, 3, 2, 5), Q(1, 7, 1, 3)],
   ["e_alladhi", "e_alladhina"],
   chunk=Q(103, 3, 2, 5)),
]
