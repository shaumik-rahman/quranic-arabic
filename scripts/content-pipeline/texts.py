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
 (1, 2, 4): "(of) the worlds",
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
      expl_en="The shape فَاعِل (fāʿil) means “the one who does it”: مَٰلِك = owner, حَاسِد = envier, كَاتِب = writer (Bangla কাতিব).",
      expl_bn="فَاعِل (ফা‘ইল) গড়ন মানে “যে করে”: مَٰلِك = মালিক, حَاسِد = হিংসুক, كَاتِب = লেখক (কাতিব)।"),
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

# ---------------------------------------------------------------------------
# Fuller explanations for pattern cards (shown when a pattern is introduced and in the Library)
PATTERN_MORE = {
 "al": ("Arabic has no separate word for “the”: ٱلۡـ is joined to the word. Without it a word usually means “a / an”: كِتَابٌ = a book, ٱلۡكِتَابُ = the book. Before 14 “sun letters” (ت ث د ذ ر ز س ش ص ض ط ظ ل ن) the ل is silent and the next letter is doubled: ٱلرَّحۡمَٰن = ar-Raḥmān, ٱلنَّاس = an-nās. Before the others you hear the l: ٱلۡحَمۡدُ = al-ḥamd.",
        "আরবিতে “the”-এর আলাদা শব্দ নেই: ٱلۡـ শব্দের সাথে জুড়ে যায়। এটি না থাকলে সাধারণত অর্থ “একটি”: كِتَابٌ = একটি বই, ٱلۡكِتَابُ = বইটি। ১৪টি “সূর্য অক্ষরের” (ت ث د ذ ر ز س ش ص ض ط ظ ل ن) আগে ل উচ্চারিত হয় না, পরের অক্ষর দ্বিগুণ হয়: ٱلرَّحۡمَٰن = আর-রহমান, ٱلنَّاس = আন-নাস। বাকিগুলোর আগে ল শোনা যায়: ٱلۡحَمۡدُ = আল-হামদ।"),
 "wa": ("وَ is always written joined to the next word, so وَإِيَّاكَ is really two words: وَ + إِيَّاكَ = and You alone. It is the most common word in the Quran. At the start of a surah, وَ + a noun is an oath: وَٱلۡعَصۡرِ = By time!",
        "وَ সবসময় পরের শব্দের সাথে জুড়ে লেখা হয়, তাই وَإِيَّاكَ আসলে দুটি শব্দ: وَ + إِيَّاكَ = এবং কেবল তোমাকেই। এটি কুরআনে সবচেয়ে বেশি আসা শব্দ। সূরার শুরুতে وَ + বিশেষ্য মানে শপথ: وَٱلۡعَصۡرِ = সময়ের শপথ!"),
 "bi": ("بِـ is joined to the next word and its meaning depends on context: “in” (بِسۡمِ ٱللَّهِ = in the name of Allah), “with” (بِٱلۡحَقِّ = with the truth, بِٱلۡقَلَمِ = with the pen), “in / by” (أَعُوذُ بِرَبِّ = I seek refuge in the Lord). The word after it ends in -i.",
        "بِـ পরের শব্দের সাথে জুড়ে যায়, অর্থ প্রসঙ্গ অনুযায়ী: “-এ/নামে” (بِسۡمِ ٱللَّهِ = আল্লাহর নামে), “সাথে/দিয়ে” (بِٱلۡحَقِّ = সত্যের সাথে, بِٱلۡقَلَمِ = কলম দিয়ে), “কাছে” (أَعُوذُ بِرَبِّ = রবের কাছে আশ্রয় চাই)। এর পরের শব্দ -ই দিয়ে শেষ হয়।"),
 "li": ("لِـ means “for / to / belongs to”: لِلَّهِ = for Allah, لِرَبِّكَ = for your Lord. With a pronoun it becomes لَـ: لَهُۥ = for him, لَكَ = for you, but لِي = for me. ٱلۡحَمۡدُ لِلَّهِ, word for word: “the praise — for Allah”.",
        "لِـ মানে “জন্য / -র”: لِلَّهِ = আল্লাহর জন্য, لِرَبِّكَ = তোমার রবের জন্য। সর্বনামের সাথে হয় لَـ: لَهُۥ = তাঁর জন্য, لَكَ = তোমার জন্য, কিন্তু لِي = আমার জন্য। ٱلۡحَمۡدُ لِلَّهِ শব্দে শব্দে: “প্রশংসা — আল্লাহর জন্য”।"),
 "fa": ("فَـ links two things: “so / then / and so”. فَصَلِّ لِرَبِّكَ = so pray to your Lord (because We gave you Al-Kawthar). فَسَبِّحۡ = then glorify. Like وَ, it is written joined to the next word.",
        "فَـ দুটি কথাকে যুক্ত করে: “তাই / তারপর”। فَصَلِّ لِرَبِّكَ = তাই তোমার রবের জন্য নামাজ পড়ো (কারণ আমরা তোমাকে কাওসার দিয়েছি)। فَسَبِّحۡ = তখন তাসবিহ পড়ো। وَ-এর মতো এটিও পরের শব্দের সাথে জুড়ে লেখা হয়।"),
 "na": ("ـنَا on the end = “us / our”. On a noun: رَبَّنَا = our Lord. On a request: ٱهۡدِنَا = guide us, ءَاتِنَا = give us, قِنَا = protect us. On a past verb it means “we did”: ظَلَمۡنَا = we wronged.",
        "শেষে ـنَا = “আমাদের / আমাদেরকে”। বিশেষ্যে: رَبَّنَا = আমাদের রব। অনুরোধে: ٱهۡدِنَا = আমাদের পথ দেখাও, ءَاتِنَا = আমাদের দাও। অতীত ক্রিয়ায় অর্থ “আমরা করেছি”: ظَلَمۡنَا = আমরা জুলুম করেছি।"),
 "ka": ("ـكَ = “you / your”, speaking to one person: رَبُّكَ = your Lord, إِيَّاكَ = you (alone), عَلَيۡكَ = upon you. In salah: ٱلسَّلَٰمُ عَلَيۡكَ أَيُّهَا ٱلنَّبِيُّ.",
        "ـكَ = “তুমি / তোমার” (একজনকে বলা): رَبُّكَ = তোমার রব, إِيَّاكَ = কেবল তোমাকে, عَلَيۡكَ = তোমার উপর। নামাজে: ٱلسَّلَٰمُ عَلَيۡكَ أَيُّهَا ٱلنَّبِيُّ।"),
 "kum": ("ـكُمۡ = “you / your” for many people: عَلَيۡكُمۡ = upon you all, رَبُّكُمۡ = your Lord. Compare: ـكَ is for one person, ـكُمۡ for a group, which is why we greet with ٱلسَّلَٰمُ عَلَيۡكُمۡ.",
        "ـكُمۡ = “তোমাদের” (অনেকজন): عَلَيۡكُمۡ = তোমাদের উপর, رَبُّكُمۡ = তোমাদের রব। ـكَ একজনের জন্য, ـكُمۡ দলের জন্য — তাই আমরা বলি ٱلسَّلَٰمُ عَلَيۡكُمۡ।"),
 "hu": ("ـهُۥ / ـهِۦ = “him / his / it”. After an i-sound it becomes -hi: عَبۡدُهُۥ = his servant, but بِإِذۡنِهِۦ = by His permission. In the Quran it very often refers to Allah: لَهُۥ = to Him (belongs).",
        "ـهُۥ / ـهِۦ = “তার / তাঁর / তাঁকে”। ই-ধ্বনির পরে হয় -হি: عَبۡدُهُۥ = তাঁর বান্দা, কিন্তু بِإِذۡنِهِۦ = তাঁর অনুমতিতে। কুরআনে প্রায়ই আল্লাহকে বোঝায়: لَهُۥ = তাঁরই।"),
 "hum": ("ـهُمۡ / ـهِمۡ = “them / their” (many people): عَلَيۡهِمۡ = upon them, أَيۡدِيهِمۡ = their hands. Like ـهُ, it becomes -him after an i or ī sound.",
        "ـهُمۡ / ـهِمۡ = “তাদের” (অনেকে): عَلَيۡهِمۡ = তাদের উপর, أَيۡدِيهِمۡ = তাদের হাত। ـهُ-এর মতো ই/ঈ-ধ্বনির পরে হয় -হিম।"),
 "huma": ("ـهُمَا = “the two of them / both”. Arabic has a special form for exactly two! ٱرۡحَمۡهُمَا = have mercy on them both (our parents), حِفۡظُهُمَا = guarding them both (the heavens and the earth).",
        "ـهُمَا = “তাদের দুজন”। আরবিতে ঠিক দুইয়ের জন্য আলাদা রূপ আছে! ٱرۡحَمۡهُمَا = তাঁদের দুজনকে দয়া করো (বাবা-মা), حِفۡظُهُمَا = এ দুটির রক্ষণাবেক্ষণ (আকাশ ও পৃথিবী)।"),
 "i": ("ـِي = “me / my”: رَبِّي = my Lord, أَبِي = my father, زِدۡنِي = increase me. When calling out, the ي is often dropped: رَبِّ ٱغۡفِرۡ لِي = (O) my Lord, forgive me.",
        "ـِي = “আমার / আমাকে”: رَبِّي = আমার রব, أَبِي = আমার বাবা, زِدۡنِي = আমাকে বাড়িয়ে দাও। ডাকার সময় ي প্রায়ই বাদ যায়: رَبِّ ٱغۡفِرۡ لِي = হে আমার রব, আমাকে ক্ষমা করো।"),
 "we_do": ("In present-tense verbs the first letter shows who is doing it: نَـ = we. نَعۡبُدُ = we worship, نَسۡتَعِينُ = we ask for help, نَقۡرَأُ = we read. The middle carries the root (ع ب د); the start tells you the doer.",
           "বর্তমান কালের ক্রিয়ার প্রথম অক্ষর বলে কে করছে: نَـ = আমরা। نَعۡبُدُ = আমরা ইবাদত করি, نَسۡتَعِينُ = আমরা সাহায্য চাই, نَقۡرَأُ = আমরা পড়ি। মাঝে থাকে মূল অক্ষর (ع ب د); শুরু বলে কে করছে।"),
 "i_do": ("أَ / أُ at the start of a present-tense verb = I: أَعُوذُ = I seek refuge, أَشۡهَدُ = I bear witness, أَكۡتُبُ = I write. Compare نَعۡبُدُ (we worship) and أَعۡبُدُ (I worship): only the first letter changes.",
          "বর্তমান কালের ক্রিয়ার শুরুতে أَ / أُ = আমি: أَعُوذُ = আমি আশ্রয় চাই, أَشۡهَدُ = আমি সাক্ষ্য দিই, أَكۡتُبُ = আমি লিখি। نَعۡبُدُ (আমরা ইবাদত করি) আর أَعۡبُدُ (আমি ইবাদত করি) — শুধু প্রথম অক্ষর বদলায়।"),
 "ya": ("يَـ / يُـ at the start = he (or it): يَعۡلَمُ = He knows, يَذۡهَبُ = he goes. Add ـُونَ at the end for “they”: يَدۡخُلُونَ = they enter. The four starts to remember: أَ I · نَـ we · يَـ he · تَـ you.",
        "শুরুতে يَـ / يُـ = সে / তিনি: يَعۡلَمُ = তিনি জানেন, يَذۡهَبُ = সে যায়। শেষে ـُونَ যোগ করলে “তারা”: يَدۡخُلُونَ = তারা প্রবেশ করে। চারটি শুরু মনে রাখুন: أَ আমি · نَـ আমরা · يَـ সে · تَـ তুমি।"),
 "you_did": ("Past-tense verbs show the doer at the END. ـتَ = you did: أَنۡعَمۡتَ = You blessed, رَأَيۡتَ = you saw. The plain form (no ending) means “he did”: أَنۡعَمَ = he blessed, رَأَى = he saw.",
             "অতীত কালের ক্রিয়ায় কর্তা থাকে শেষে। ـتَ = তুমি করেছ: أَنۡعَمۡتَ = তুমি নিয়ামত দিয়েছ, رَأَيۡتَ = তুমি দেখেছ। শেষে কিছু না থাকলে “সে করেছে”: أَنۡعَمَ = সে নিয়ামত দিয়েছে।"),
 "we_did": ("ـنَا at the end of a past verb = we did: ظَلَمۡنَا = we wronged, أَعۡطَيۡنَا = We gave. When Allah says “We” in the Quran it expresses majesty, not more than one.",
            "অতীত ক্রিয়ার শেষে ـنَا = আমরা করেছি: ظَلَمۡنَا = আমরা জুলুম করেছি, أَعۡطَيۡنَا = আমরা দিয়েছি। কুরআনে আল্লাহ “আমরা” বললে তা মহিমা বোঝায়, একাধিক নয়।"),
 "they_did": ("ـُواْ at the end of a past verb = they did: ءَامَنُواْ = they believed, عَمِلُواْ = they did, ذَهَبُواْ = they went. The final ا is written but not pronounced.",
              "অতীত ক্রিয়ার শেষে ـُواْ = তারা করেছে: ءَامَنُواْ = তারা ঈমান এনেছে, عَمِلُواْ = তারা আমল করেছে, ذَهَبُواْ = তারা গেছে। শেষের ا লেখা হয় কিন্তু পড়া হয় না।"),
 "cmd": ("A command is short: قُلۡ = say!, ٱهۡدِنَا = guide us!, ٱغۡفِرۡ = forgive!, سَبِّحۡ = glorify! It often starts with ٱ and ends with a sukun. Said to Allah in a dua it is a humble request, not an order: رَبِّ ٱغۡفِرۡ لِي = My Lord, forgive me.",
         "আদেশ ছোট হয়: قُلۡ = বলো!, ٱهۡدِنَا = পথ দেখাও!, ٱغۡفِرۡ = ক্ষমা করো!, سَبِّحۡ = তাসবিহ পড়ো! প্রায়ই ٱ দিয়ে শুরু ও সুকুন দিয়ে শেষ হয়। দোয়ায় আল্লাহকে বললে তা বিনীত অনুরোধ: رَبِّ ٱغۡفِرۡ لِي = হে আমার রব, আমাকে ক্ষমা করো।"),
 "plural": ("ـُونَ (as the subject) or ـِينَ (after a preposition or as the object) make “many people”: مُؤۡمِن = a believer → ٱلۡمُؤۡمِنُونَ / ٱلۡمُؤۡمِنِينَ = the believers; صَالِح → ٱلصَّٰلِحِينَ = the righteous. Things often use ـَات: صَالِحَة (a good deed) → ٱلصَّٰلِحَٰتِ (good deeds).",
            "ـُونَ (কর্তা হলে) বা ـِينَ (অব্যয়ের পরে বা কর্ম হলে) দিয়ে “অনেক মানুষ”: مُؤۡمِن = একজন মুমিন → ٱلۡمُؤۡمِنُونَ / ٱلۡمُؤۡمِنِينَ = মুমিনরা; صَالِح → ٱلصَّٰلِحِينَ = নেককাররা। জিনিসের বহুবচনে প্রায়ই ـَات: صَالِحَة (একটি সৎকাজ) → ٱلصَّٰلِحَٰتِ (সৎকাজসমূহ)।"),
 "doer": ("Most roots have three letters. Put them in the shape فَاعِل (ā after the 1st letter, i after the 2nd) and you get “the one who does it”: ك ت ب (write) → كَاتِب writer; م ل ك (own) → مَالِك owner; ح س د (envy) → حَاسِد envier; خ ل ق (create) → خَالِق Creator.",
          "বেশিরভাগ মূলে তিনটি অক্ষর। এগুলো فَاعِل ছাঁচে বসালে (১ম অক্ষরের পরে আ, ২য়টির পরে ই) অর্থ হয় “যে করে”: ك ت ب (লেখা) → كَاتِب লেখক; م ل ك (মালিকানা) → مَالِك মালিক; ح س د (হিংসা) → حَاسِد হিংসুক; خ ل ق (সৃষ্টি) → خَالِق স্রষ্টা।"),
 "done_to": ("The shape مَفۡعُول (ma- … -ū-) means “the one it is done to”: ك ت ب → مَكۡتُوب written (Bangla মকতুব); غ ض ب → مَغۡضُوب the one under anger; ح م د → مَحۡمُود praised (Mahmud); ح ب ب → مَحۡبُوب beloved (Mahbub).",
             "مَفۡعُول ছাঁচ (মা- … -ঊ-) মানে “যার প্রতি করা হয়েছে”: ك ت ب → مَكۡتُوب লিখিত (মকতুব); غ ض ب → مَغۡضُوب গজবপ্রাপ্ত; ح م د → مَحۡمُود প্রশংসিত (মাহমুদ); ح ب ب → مَحۡبُوب প্রিয় (মাহবুব)।"),
}

# "Notice" bullets for sentence patterns, each with an example
STRUCTURE_NOTES = {
 "is": [
  ("Word for word, ٱللَّهُ أَكۡبَرُ is “Allah — greatest”. English and Bangla add “is”; Arabic doesn't need it.",
   "শব্দে শব্দে ٱللَّهُ أَكۡبَرُ হলো “আল্লাহ — সবচেয়ে বড়”। বাংলায় “হলেন” যোগ করি; আরবিতে লাগে না।"),
  ("With هَٰذَا (this) and ذَٰلِكَ (that): هَٰذَا قَلَمٌ = this (is) a pen. The -un ending (قَلَمٌ) means “a”.",
   "هَٰذَا (এটি) ও ذَٰلِكَ (ওটি) দিয়ে: هَٰذَا قَلَمٌ = এটি (হলো) একটি কলম। শেষের -উন (قَلَمٌ) মানে “একটি”।"),
  ("Pronouns work the same way: هُوَ أَبِي = he (is) my father, هِيَ أُمِّي = she (is) my mother.",
   "সর্বনামেও একই নিয়ম: هُوَ أَبِي = তিনি (হলেন) আমার বাবা, هِيَ أُمِّي = তিনি আমার মা।"),
 ],
 "of": [
  ("Word for word, بَيۡتُ ٱللَّهِ is “house — Allah”: the House of Allah.",
   "শব্দে শব্দে بَيۡتُ ٱللَّهِ হলো “ঘর — আল্লাহ”: আল্লাহর ঘর।"),
  ("The first word loses ٱلۡـ and the -un ending: بَيۡتٌ (a house) → بَيۡتُ ٱللَّهِ (the House of Allah). It is already “the” because it belongs to someone.",
   "প্রথম শব্দ ٱلۡـ ও -উন হারায়: بَيۡتٌ (একটি ঘর) → بَيۡتُ ٱللَّهِ (আল্লাহর ঘর)। কারও হওয়ায় এটি এমনিতেই নির্দিষ্ট।"),
  ("The second word ends in -i, and chains are possible: مَٰلِكِ يَوۡمِ ٱلدِّينِ = Master (of) the Day (of) Judgment.",
   "দ্বিতীয় শব্দ -ই দিয়ে শেষ হয়, আর শিকলও হয়: مَٰلِكِ يَوۡمِ ٱلدِّينِ = বিচার দিনের মালিক।"),
 ],
 "after": [
  ("The order is the opposite of English and Bangla: بَيۡتٌ كَبِيرٌ = house big: a big house.",
   "ক্রম বাংলার উল্টো: بَيۡتٌ كَبِيرٌ = ঘর বড় → একটি বড় ঘর।"),
  ("Both words match: both with ٱلۡـ (ٱلۡبَيۡتُ ٱلۡكَبِيرُ = the big house) or both without (بَيۡتٌ كَبِيرٌ = a big house).",
   "দুটি শব্দ মিলে যায়: দুটিতেই ٱلۡـ (ٱلۡبَيۡتُ ٱلۡكَبِيرُ = বড় ঘরটি) অথবা কোনোটিতেই নয় (بَيۡتٌ كَبِيرٌ = একটি বড় ঘর)।"),
  ("ٱلۡـ only on the first word makes a sentence: ٱلۡبَيۡتُ كَبِيرٌ = the house (is) big. One little ٱلۡـ changes the meaning!",
   "শুধু প্রথম শব্দে ٱلۡـ থাকলে বাক্য হয়: ٱلۡبَيۡتُ كَبِيرٌ = ঘরটি বড়। একটি ছোট্ট ٱلۡـ অর্থ বদলে দেয়!"),
 ],
 "verb": [
  ("Look at the first letter: أَ = I, نَـ = we, يَـ = he, تَـ = you. نَقۡرَأُ = we read, أَكۡتُبُ = I write.",
   "প্রথম অক্ষর দেখুন: أَ = আমি, نَـ = আমরা, يَـ = সে, تَـ = তুমি। نَقۡرَأُ = আমরা পড়ি, أَكۡتُبُ = আমি লিখি।"),
  ("The verb often comes first: يَذۡهَبُ أَبِي = goes my father: my father goes.",
   "ক্রিয়া প্রায়ই আগে আসে: يَذۡهَبُ أَبِي = যান আমার বাবা → আমার বাবা যান।"),
  ("Putting the object first adds “only”: نَعۡبُدُكَ = we worship You; إِيَّاكَ نَعۡبُدُ = You ALONE we worship.",
   "কর্ম আগে বসালে “কেবল” অর্থ আসে: نَعۡبُدُكَ = আমরা তোমার ইবাদত করি; إِيَّاكَ نَعۡبُدُ = কেবল তোমারই ইবাদত করি।"),
 ],
 "inna": [
  ("إِنَّ + noun + description: إِنَّ ٱللَّهَ قَرِيبٌ = indeed Allah (is) near.",
   "إِنَّ + বিশেষ্য + বর্ণনা: إِنَّ ٱللَّهَ قَرِيبٌ = নিশ্চয়ই আল্লাহ কাছে।"),
  ("The noun after إِنَّ ends in -a: ٱللَّهُ becomes إِنَّ ٱللَّهَ, ٱلۡإِنسَٰنُ becomes إِنَّ ٱلۡإِنسَٰنَ.",
   "إِنَّ-এর পরের বিশেষ্য -আ দিয়ে শেষ হয়: ٱللَّهُ → إِنَّ ٱللَّهَ।"),
  ("With a pronoun attached: إِنَّهُۥ = indeed he, إِنَّآ = indeed We: إِنَّآ أَعۡطَيۡنَٰكَ ٱلۡكَوۡثَرَ.",
   "সর্বনাম জুড়ে: إِنَّهُۥ = নিশ্চয়ই তিনি, إِنَّآ = নিশ্চয়ই আমরা: إِنَّآ أَعۡطَيۡنَٰكَ ٱلۡكَوۡثَرَ।"),
 ],
 "alladhina": [
  ("ٱلَّذِي = the one who (one man); ٱلَّذِينَ = those who (many).",
   "ٱلَّذِي = যে (একজন); ٱلَّذِينَ = যারা (অনেকে)।"),
  ("Follow it with a verb: ٱلَّذِينَ ءَامَنُواْ = those who believed; ٱلَّذِي يَقۡرَأُ = the one who reads.",
   "এরপর ক্রিয়া বসে: ٱلَّذِينَ ءَامَنُواْ = যারা ঈমান এনেছে; ٱلَّذِي يَقۡرَأُ = যে পড়ে।"),
  ("It can describe a noun: صِرَٰطَ ٱلَّذِينَ أَنۡعَمۡتَ عَلَيۡهِمۡ = the path of those whom You blessed.",
   "এটি বিশেষ্যের বর্ণনাও দিতে পারে: صِرَٰطَ ٱلَّذِينَ أَنۡعَمۡتَ عَلَيۡهِمۡ = তাদের পথ, যাদের তুমি নিয়ামত দিয়েছ।"),
 ],
}

# ===========================================================================
# Sentence patterns for Units 3–14
# ===========================================================================
YA = ("يَا", "O", "হে", "X:ya", [])
ABI = ("أَبِي", "my father", "আমার বাবা", "أَب|أبو", ["i"])
UMMI = ("أُمِّي", "my mother", "আমার মা", "أُمّ|أمم", ["i"])
MASJID_I = ("ٱلۡمَسۡجِدِ", "the mosque", "মসজিদ", "مَسْجِد|سجد", ["al"])
ILA = ("إِلَى", "to", "দিকে", "إِلَى|", [])
EVERYDAY += [
 # calling
 E("e_yaabi", "O my father!", "হে আমার বাবা!", [YA, ABI]),
 E("e_yaummi", "O my mother, this is a book.", "মা, এটি একটি বই।", [YA, UMMI, HADHA, ("كِتَابٌ", "a book", "একটি বই", "كِتاب|كتب", [])]),
 E("e_rabbighfirabi", "My Lord, forgive my father.", "হে আমার রব, আমার বাবাকে ক্ষমা করো।", [
    ("رَبِّ", "My Lord", "হে আমার রব", "رَبّ|ربب", []), ("ٱغۡفِرۡ", "forgive", "ক্ষমা করো", "غَفَرَ|غفر", ["cmd"]),
    ("لِأَبِي", "my father", "আমার বাবাকে", "أَب|أبو", ["li", "i"])]),
 E("e_rabbanaghfir", "Our Lord, forgive us.", "হে আমাদের রব, আমাদের ক্ষমা করো।", [
    ("رَبَّنَا", "Our Lord", "হে আমাদের রব", "رَبّ|ربب", ["na"]), ("ٱغۡفِرۡ", "forgive", "ক্ষমা করো", "غَفَرَ|غفر", ["cmd"]),
    ("لَنَا", "us", "আমাদের", "PRON:1P", ["li"])]),
 # saying no
 E("e_laalamu", "I don't know.", "আমি জানি না।", [("لَا", "not", "না", "لا|", []), ("أَعۡلَمُ", "I know", "আমি জানি", "عَلِمَ|علم", ["i_do"])]),
 E("e_lanalamu", "We don't know.", "আমরা জানি না।", [("لَا", "not", "না", "لا|", []), ("نَعۡلَمُ", "we know", "আমরা জানি", "عَلِمَ|علم", ["we_do"])]),
 E("e_lamadhhab", "I did not go to the mosque.", "আমি মসজিদে যাইনি।", [
    ("لَمۡ", "did not", "নি", "لَم|", []), ("أَذۡهَبۡ", "I go", "আমি যাই", "ذَهَبَ|ذهب", ["i_do"]), ILA, MASJID_I]),
 E("e_lamyaqra", "My father did not read the book.", "আমার বাবা বইটি পড়েননি।", [
    ("لَمۡ", "did not", "নি", "لَم|", []), ("يَقۡرَأۡ", "reads", "পড়েন", "قَرَأَ|قرأ", ["ya"]), ABI,
    ("ٱلۡكِتَابَ", "the book", "বইটি", "كِتاب|كتب", ["al"])]),
 # none but / only
 E("e_lakitab", "There is no book in the house.", "ঘরে কোনো বই নেই।", [
    ("لَا", "no", "নেই", "لا|", []), ("كِتَابَ", "book", "কোনো বই", "كِتاب|كتب", []), ("فِي", "in", "-এ", "فِي|", []),
    ("ٱلۡبَيۡتِ", "the house", "ঘর", "بَيْت|بيت", ["al"])]),
 E("e_lanabudu", "We worship none but Allah.", "আমরা আল্লাহ ছাড়া কারও ইবাদত করি না।", [
    ("لَا", "not", "না", "لا|", []), ("نَعۡبُدُ", "we worship", "আমরা ইবাদত করি", "عَبَدَ|عبد", ["we_do"]),
    ("إِلَّا", "except", "ছাড়া", "إِلّا|", []), ("ٱللَّهَ", "Allah", "আল্লাহ", "اللَّه|أله", [])]),
 E("e_laaqrau", "I read nothing but the Quran.", "আমি কুরআন ছাড়া কিছু পড়ি না।", [
    ("لَا", "not", "না", "لا|", []), ("أَقۡرَأُ", "I read", "আমি পড়ি", "قَرَأَ|قرأ", ["i_do"]),
    ("إِلَّا", "except", "ছাড়া", "إِلّا|", []), ("ٱلۡقُرۡءَانَ", "the Quran", "কুরআন", "قُرْءان|قرأ", ["al"])]),
 # when
 E("e_idhajaa", "When my father comes, we go to the mosque.", "বাবা এলে আমরা মসজিদে যাই।", [
    ("إِذَا", "when", "যখন", "إِذا|", []), ("جَآءَ", "comes", "আসেন", "جاءَ|جيأ", []), ABI,
    ("نَذۡهَبُ", "we go", "আমরা যাই", "ذَهَبَ|ذهب", ["we_do"]), ILA, MASJID_I]),
 E("e_idhadakhalta", "When you enter the mosque, pray.", "মসজিদে প্রবেশ করলে নামাজ পড়ো।", [
    ("إِذَا", "when", "যখন", "إِذا|", []), ("دَخَلۡتَ", "you enter", "তুমি প্রবেশ করো", "دَخَلَ|دخل", ["you_did"]),
    ("ٱلۡمَسۡجِدَ", "the mosque", "মসজিদে", "مَسْجِد|سجد", ["al"]), ("فَصَلِّ", "then pray", "তখন নামাজ পড়ো", "صَلَّى|صلو", ["fa", "cmd"])]),
 # place words
 E("e_abifilbayt", "My father is in the house.", "আমার বাবা ঘরে আছেন।", [ABI, ("فِي", "(is) in", "-এ", "فِي|", []), ("ٱلۡبَيۡتِ", "the house", "ঘর", "بَيْت|بيت", ["al"])]),
 E("e_qalamala", "The pen is on the book.", "কলমটি বইয়ের উপর।", [
    ("ٱلۡقَلَمُ", "The pen", "কলমটি", "قَلَم|قلم", ["al"]), ("عَلَى", "(is) on", "উপর", "عَلَى|", []),
    ("ٱلۡكِتَابِ", "the book", "বইয়ের", "كِتاب|كتب", ["al"])]),
 E("e_dhahabaila", "My father went to the mosque.", "আমার বাবা মসজিদে গেলেন।", [("ذَهَبَ", "went", "গেলেন", "ذَهَبَ|ذهب", []), ABI, ILA, MASJID_I]),
 E("e_khayrmin", "Good comes from Allah.", "কল্যাণ আল্লাহর পক্ষ থেকে।", [
    ("ٱلۡخَيۡرُ", "Good", "কল্যাণ", "خَيْر|خير", ["al"]), ("مِنَ", "(is) from", "থেকে", "مِن|", []), ("ٱللَّهِ", "Allah", "আল্লাহ", "اللَّه|أله", [])]),
 # asking (duas)
 E("e_ighfirwalidayn", "My Lord, forgive my father and my mother.", "হে আমার রব, আমার বাবা ও মাকে ক্ষমা করো।", [
    ("رَبِّ", "My Lord", "হে আমার রব", "رَبّ|ربب", []), ("ٱغۡفِرۡ", "forgive", "ক্ষমা করো", "غَفَرَ|غفر", ["cmd"]),
    ("لِأَبِي", "my father", "আমার বাবাকে", "أَب|أبو", ["li", "i"]), ("وَأُمِّي", "and my mother", "ও আমার মাকে", "أُمّ|أمم", ["wa", "i"])]),
 E("e_irhamna", "Our Lord, have mercy on us.", "হে আমাদের রব, আমাদের প্রতি দয়া করো।", [
    ("رَبَّنَا", "Our Lord", "হে আমাদের রব", "رَبّ|ربب", ["na"]), ("ٱرۡحَمۡنَا", "have mercy on us", "আমাদের দয়া করো", "رَحِمَ|رحم", ["cmd", "na"])]),
 E("e_ihdini", "My Lord, guide me.", "হে আমার রব, আমাকে পথ দেখাও।", [
    ("رَبِّ", "My Lord", "হে আমার রব", "رَبّ|ربب", []), ("ٱهۡدِنِي", "guide me", "আমাকে পথ দেখাও", "هَدَى|هدي", ["cmd", "i"])]),
 E("e_latadhhab", "Don't go!", "যেয়ো না!", [("لَا", "don't", "না", "لا|", []), ("تَذۡهَبۡ", "go", "যাও", "ذَهَبَ|ذهب", [])]),
 # having
 E("e_libayt", "I have a big house.", "আমার একটি বড় ঘর আছে।", [
    ("لِي", "to me (is)", "আমার আছে", "PRON:1S", ["li"]), ("بَيۡتٌ", "a house", "একটি ঘর", "بَيْت|بيت", []), ("كَبِيرٌ", "big", "বড়", "كَبِير|كبر", [])]),
 E("e_indiqalam", "I have a new pen.", "আমার কাছে একটি নতুন কলম আছে।", [
    ("عِندِي", "with me (is)", "আমার কাছে আছে", "عِند|عند", ["i"]), ("قَلَمٌ", "a pen", "একটি কলম", "قَلَم|قلم", []), ("جَدِيدٌ", "new", "নতুন", "جَدِيد|جدد", [])]),
 E("e_liabikitab", "My father has a book.", "আমার বাবার একটি বই আছে।", [
    ("لِأَبِي", "to my father (is)", "আমার বাবার আছে", "أَب|أبو", ["li", "i"]), ("كِتَابٌ", "a book", "একটি বই", "كِتاب|كتب", [])]),
 E("e_lanarabb", "We have a merciful Lord.", "আমাদের একজন দয়ালু রব আছেন।", [
    ("لَنَا", "to us (is)", "আমাদের আছেন", "PRON:1P", ["li"]), ("رَبٌّ", "a Lord", "একজন রব", "رَبّ|ربب", []), ("رَحِيمٌ", "merciful", "দয়ালু", "رَحِيم|رحم", [])]),
 # questions
 E("e_mahadha", "What is this?", "এটি কী?", [("مَا", "What", "কী", "ما|", []), ("هَٰذَا", "(is) this", "এটি", "ذا|", [])]),
 E("e_manhadha", "Who is this?", "এ কে?", [("مَنۡ", "Who", "কে", "مَن|", []), ("هَٰذَا", "(is) this", "এ", "ذا|", [])]),
 E("e_aynalmasjid", "Where is the mosque?", "মসজিদ কোথায়?", [("أَيۡنَ", "Where", "কোথায়", "أَيْن|", []), ("ٱلۡمَسۡجِدُ", "(is) the mosque", "মসজিদ", "مَسْجِد|سجد", ["al"])]),
 E("e_aynatadhhab", "Where are you going?", "তুমি কোথায় যাচ্ছ?", [("أَيۡنَ", "Where", "কোথায়", "أَيْن|", []), ("تَذۡهَبُ", "you go", "তুমি যাও", "ذَهَبَ|ذهب", [])]),
 E("e_haldhahaba", "Did my father go to the mosque?", "বাবা কি মসজিদে গেছেন?", [
    ("هَلۡ", "Did", "কি", "هَل|", []), ("ذَهَبَ", "go", "গেছেন", "ذَهَبَ|ذهب", []), ABI, ILA, MASJID_I]),
]

H = lambda grp, lid: ("h", grp, lid)
STRUCTURES += [
 S("call", "u3", "Calling: يَا …", "ডাকা: يَا …", "📣",
   [("يَا", "O", "হে", "call"), ("أَبِي", "my father", "আমার বাবা", "thing")],
   "To call someone, put يَا (O …) before them: يَا أَبِي = O my father! When we call Allah, يَا is usually left out: رَبِّ = (O) my Lord, رَبَّنَا = (O) our Lord.",
   "কাউকে ডাকতে তার আগে يَا (হে …) বসান: يَا أَبِي = হে আমার বাবা! আল্লাহকে ডাকার সময় সাধারণত يَا বাদ যায়: رَبِّ = (হে) আমার রব, رَبَّنَا = (হে) আমাদের রব।",
   [H("salah", "jalsa"), H("salah", "rabbana"), Q(2, 21, 1, 2), Q(12, 4, 5, 7), Q(2, 104, 1, 3)],
   ["e_yaabi", "e_yaummi", "e_rabbighfirabi", "e_rabbanaghfir"], chunk=Q(2, 104, 1, 3)),
 S("no", "u4", "Saying no: لَا and لَمۡ", "না বলা: لَا ও لَمۡ", "🙅",
   [("لَمۡ", "did not", "নি", "no"), ("يَلِدۡ", "beget", "জন্ম দেন", "do")],
   "لَا before a verb = does not: لَا أَعۡلَمُ = I do not know. لَمۡ before a verb = did not: لَمۡ يَلِدۡ = He did not beget. After لَمۡ the verb looks present but means past, and its last vowel becomes a sukun.",
   "ক্রিয়ার আগে لَا = না (করে না): لَا أَعۡلَمُ = আমি জানি না। ক্রিয়ার আগে لَمۡ = করেনি: لَمۡ يَلِدۡ = তিনি জন্ম দেননি। لَمۡ-এর পরে ক্রিয়া বর্তমানের মতো দেখায় কিন্তু অর্থ অতীত, আর শেষ স্বর সুকুন হয়।",
   [Q(112, 3), Q(109, 2), Q(96, 5)],
   ["e_laalamu", "e_lanalamu", "e_lamadhhab", "e_lamyaqra"]),
 S("only", "u5", "None but: لَا … إِلَّا", "ছাড়া কেউ নয়: لَا … إِلَّا", "☝️",
   [("لَآ", "no", "নেই", "no"), ("إِلَٰهَ", "god", "ইলাহ", "thing"), ("إِلَّا", "except", "ছাড়া", "except"), ("ٱللَّهُ", "Allah", "আল্লাহ", "thing")],
   "لَا + a noun = there is no … at all. Add إِلَّا (except) and you have the strongest way to say “only”: لَآ إِلَٰهَ إِلَّا ٱللَّهُ = no god except Allah, so Allah alone is God.",
   "لَا + বিশেষ্য = কোনো … নেই। إِلَّا (ছাড়া) যোগ করলে “কেবল” বলার সবচেয়ে জোরালো উপায়: لَآ إِلَٰهَ إِلَّا ٱللَّهُ = আল্লাহ ছাড়া কোনো ইলাহ নেই, অর্থাৎ কেবল আল্লাহই ইলাহ।",
   [H("azan", "az_end"), Q(2, 255, 2, 5), Q(2, 2, 3, 5)],
   ["e_lakitab", "e_lanabudu", "e_laaqrau"], chunk=Q(2, 255, 2, 5)),
 S("when", "u8", "When: إِذَا …", "যখন: إِذَا …", "⏰",
   [("إِذَا", "when", "যখন", "when"), ("جَآءَ", "comes", "আসে", "do"), ("نَصۡرُ ٱللَّهِ", "the help of Allah", "আল্লাহর সাহায্য", "thing")],
   "إِذَا + a past verb = “when … happens”. The second half says what happens then, often starting with فَـ: إِذَا جَآءَ نَصۡرُ ٱللَّهِ … فَسَبِّحۡ = When Allah's help comes … then glorify.",
   "إِذَا + অতীত ক্রিয়া = “যখন … ঘটে”। দ্বিতীয় অংশ বলে তখন কী হয়, প্রায়ই فَـ দিয়ে শুরু: إِذَا جَآءَ نَصۡرُ ٱللَّهِ … فَسَبِّحۡ = যখন আল্লাহর সাহায্য আসে … তখন তাসবিহ পড়ো।",
   [Q(110, 1), Q(99, 1), Q(16, 98)],
   ["e_idhajaa", "e_idhadakhalta"]),
 S("place", "u9", "Place words: فِي, مِنۡ, عَلَى, إِلَى", "স্থানবাচক শব্দ: فِي, مِنۡ, عَلَى, إِلَى", "📍",
   [("مِن", "from", "থেকে", "place"), ("شَرِّ", "the evil", "অনিষ্ট", "thing")],
   "Little words like فِي (in), مِنۡ (from), عَلَى (on) and إِلَى (to) go before a noun to say where. The noun after them ends in -i: مِن شَرِّ = from the evil, فِي ٱلۡبَيۡتِ = in the house.",
   "فِي (-এ), مِنۡ (থেকে), عَلَى (উপর), إِلَى (দিকে) এর মতো ছোট শব্দ বিশেষ্যের আগে বসে স্থান বোঝায়। এদের পরের বিশেষ্য -ই দিয়ে শেষ হয়: مِن شَرِّ = অনিষ্ট থেকে, فِي ٱلۡبَيۡتِ = ঘরে।",
   [Q(113, 2), Q(114, 5), Q(2, 261, 5, 7)],
   ["e_abifilbayt", "e_qalamala", "e_dhahabaila", "e_khayrmin"]),
 S("ask", "u12", "Asking in a dua", "দোয়ায় চাওয়া", "🤲",
   [("رَبِّ", "My Lord", "হে আমার রব", "call"), ("زِدۡنِي", "increase me", "আমাকে বাড়িয়ে দাও", "do"), ("عِلۡمًا", "in knowledge", "জ্ঞানে", "thing")],
   "Most duas have three parts: call Allah (رَبِّ / رَبَّنَا), ask with the command form (ٱغۡفِرۡ, ٱرۡحَمۡ, زِدۡ), and say for whom (ـنِي me, ـنَا us, لِي for me). رَبِّ زِدۡنِي عِلۡمًا = My Lord, increase me in knowledge.",
   "বেশিরভাগ দোয়ার তিন অংশ: আল্লাহকে ডাকা (رَبِّ / رَبَّنَا), আদেশ-রূপে চাওয়া (ٱغۡفِرۡ, ٱرۡحَمۡ, زِدۡ), আর কার জন্য (ـنِي আমাকে, ـنَا আমাদের, لِي আমার জন্য)। رَبِّ زِدۡنِي عِلۡمًا = হে আমার রব, আমার জ্ঞান বাড়িয়ে দাও।",
   [Q(20, 114, 14, 17), Q(20, 25, 2, 5), Q(20, 26), Q(71, 28, 1, 4), Q(9, 40, 19, 23)],
   ["e_ighfirwalidayn", "e_irhamna", "e_ihdini", "e_latadhhab"]),
 S("have", "u13", "Having: لِـ and عِندَ", "থাকা: لِـ ও عِندَ", "🎒",
   [("لَّهُۥ", "to Him (belongs)", "তাঁরই", "owner"), ("مَا فِي ٱلسَّمَٰوَٰتِ", "what is in the heavens", "যা আকাশে আছে", "thing")],
   "Arabic has no verb “to have”. It says “to me (is) …” with لِـ, or “with me (is) …” with عِندَ: لِي بَيۡتٌ = I have a house, عِندِي قَلَمٌ = I have a pen. لَّهُۥ مَا فِي ٱلسَّمَٰوَٰتِ = to Him belongs whatever is in the heavens.",
   "আরবিতে “থাকা/আছে” বোঝানোর আলাদা ক্রিয়া নেই। বলা হয় “আমার জন্য (আছে) …” لِـ দিয়ে, অথবা “আমার কাছে (আছে) …” عِندَ দিয়ে: لِي بَيۡتٌ = আমার একটি ঘর আছে, عِندِي قَلَمٌ = আমার কাছে একটি কলম আছে। لَّهُۥ مَا فِي ٱلسَّمَٰوَٰتِ = আকাশে যা আছে সব তাঁরই।",
   [Q(2, 255, 13, 19), Q(109, 6), Q(112, 4)],
   ["e_libayt", "e_indiqalam", "e_liabikitab", "e_lanarabb"]),
 S("question", "u14", "Asking questions: مَا, مَنۡ, أَيۡنَ, هَلۡ", "প্রশ্ন করা: مَا, مَنۡ, أَيۡنَ, هَلۡ", "❓",
   [("مَا", "what", "কী", "ask"), ("هَٰذَا", "(is) this", "এটি", "thing")],
   "Put the question word first, then a normal sentence: مَا (what?), مَنۡ (who?), أَيۡنَ (where?), هَلۡ (is it…? does…?). مَا هَٰذَا = What is this? مَن ذَا ٱلَّذِي يَشۡفَعُ = Who is it that intercedes?",
   "প্রথমে প্রশ্নবোধক শব্দ, তারপর সাধারণ বাক্য: مَا (কী?), مَنۡ (কে?), أَيۡنَ (কোথায়?), هَلۡ (কি?)। مَا هَٰذَا = এটি কী? مَن ذَا ٱلَّذِي يَشۡفَعُ = কে আছে যে সুপারিশ করবে?",
   [Q(2, 255, 20, 26), Q(81, 26), Q(101, 2), Q(88, 1)],
   ["e_mahadha", "e_manhadha", "e_aynalmasjid", "e_aynatadhhab", "e_haldhahaba"]),
]

SEG_TR.update({
 "2:21:1-2": ("O mankind", "হে মানুষ"),
 "12:4:5-7": ("O my father, indeed I saw", "হে আমার পিতা, আমি দেখেছি"),
 "2:104:1-3": ("O you who have believed", "হে মুমিনগণ"),
 "2:2:3-5": ("no doubt in it", "এতে কোনো সন্দেহ নেই"),
 "2:255:2-5": ("there is no god except Him", "তিনি ছাড়া কোনো ইলাহ নেই"),
 "2:261:5-7": ("in the way of Allah", "আল্লাহর পথে"),
 "20:25:2-5": ("My Lord, expand for me my chest", "হে আমার রব, আমার বুক প্রশস্ত করে দাও"),
 "71:28:1-4": ("My Lord, forgive me and my parents", "হে আমার রব, আমাকে ও আমার বাবা-মাকে ক্ষমা করো"),
 "9:40:19-23": ("Do not grieve; indeed Allah is with us.", "চিন্তা কোরো না, নিশ্চয়ই আল্লাহ আমাদের সাথে আছেন।"),
 "2:255:13-19": ("To Him belongs whatever is in the heavens and whatever is on the earth.", "আকাশ ও পৃথিবীতে যা কিছু আছে সব তাঁরই।"),
 "2:255:20-26": ("Who is it that can intercede with Him except by His permission?", "কে আছে যে তাঁর অনুমতি ছাড়া তাঁর কাছে সুপারিশ করবে?"),
})

# ===========================================================================
# "Understand your salah": the prayer in order. Extra lines said in salah that no unit teaches yet.
# ===========================================================================
ALLAHUMMA = ("ٱللَّهُمَّ", "O Allah", "হে আল্লাহ", "اللَّهُمَّ|أله", [])
MUHAMMAD_I = ("مُحَمَّدٍ", "Muhammad", "মুহাম্মাদ", "مُحَمَّد|حمد", [])
WA_ALA = ("وَعَلَىٰ", "and upon", "এবং … উপর", "عَلَى|", ["wa"])
ALA = ("عَلَىٰ", "upon", "উপর", "عَلَى|", [])
AAL = ("ءَالِ", "the family of", "পরিবার", "آل|أول", [])
IBRAHIM = ("إِبۡرَٰهِيمَ", "Ibrahim", "ইবরাহিম", "إِبْراهِيم|", [])
KAMA = ("كَمَا", "as", "যেমন", "ما|", [])
INNAKA_HAMID = [("إِنَّكَ", "indeed You", "নিশ্চয়ই তুমি", "إِنّ|", ["ka"]), ("حَمِيدٌ", "(are) Praiseworthy", "প্রশংসিত", "حَمِيد|حمد", []),
                ("مَّجِيدٌ", "Glorious", "মহিমান্বিত", "مَجِيد|مجد", [])]
GUIDE = [
 L("thana", "Glory be to You, O Allah, and praise be to You. Blessed is Your name, high is Your majesty, and there is no god other than You.",
   "হে আল্লাহ, তুমি পবিত্র, সব প্রশংসা তোমার। তোমার নাম বরকতময়, তোমার মর্যাদা সুউচ্চ, তুমি ছাড়া কোনো ইলাহ নেই।", [
    ("سُبۡحَٰنَكَ", "Glory be to You", "তুমি পবিত্র", "سُبْحان|سبح", ["ka"]), ALLAHUMMA,
    ("وَبِحَمۡدِكَ", "and with Your praise", "এবং তোমার প্রশংসাসহ", "حَمْد|حمد", ["wa", "bi", "ka"]),
    ("وَتَبَارَكَ", "and blessed is", "এবং বরকতময়", "تَبارَكَ|برك", ["wa"]), ("ٱسۡمُكَ", "Your name", "তোমার নাম", "اسْم|سمو", ["ka"]),
    ("وَتَعَٰلَىٰ", "and high is", "এবং সুউচ্চ", "تَعالَى|علو", ["wa"]), ("جَدُّكَ", "Your majesty", "তোমার মর্যাদা", "جَدّ|جدد", ["ka"]),
    ("وَلَآ", "and (there is) no", "এবং নেই", "لا|", ["wa"]), ("إِلَٰهَ", "god", "কোনো ইলাহ", "إِلٰه|أله", []),
    ("غَيۡرُكَ", "other than You", "তুমি ছাড়া", "غَيْر|غير", ["ka"])],
   "One common opening dua, said quietly after the first takbir.", "প্রথম তাকবিরের পর নিচু স্বরে পড়া একটি প্রচলিত দোয়া।"),
 L("taawwudh", "I seek refuge in Allah from Satan, the rejected.", "আমি বিতাড়িত শয়তান থেকে আল্লাহর আশ্রয় চাই।", [
    ("أَعُوذُ", "I seek refuge", "আমি আশ্রয় চাই", "عُذْ|عوذ", ["i_do"]), ("بِٱللَّهِ", "in Allah", "আল্লাহর কাছে", "اللَّه|أله", ["bi"]),
    ("مِنَ", "from", "থেকে", "مِن|", []), ("ٱلشَّيۡطَٰنِ", "Satan", "শয়তান", "شَيْطان|شطن", ["al"]),
    ("ٱلرَّجِيمِ", "the rejected", "বিতাড়িত", "رَجِيم|رجم", ["al"])],
   "Said quietly before Al-Fatiha.", "ফাতিহার আগে নিচু স্বরে।"),
 L("salawat1", "O Allah, send prayers upon Muhammad and the family of Muhammad, as You sent prayers upon Ibrahim and the family of Ibrahim. Indeed, You are Praiseworthy, Glorious.",
   "হে আল্লাহ, মুহাম্মাদ ও তাঁর পরিবারের উপর রহমত পাঠাও, যেমন ইবরাহিম ও তাঁর পরিবারের উপর পাঠিয়েছ। নিশ্চয়ই তুমি প্রশংসিত, মহিমান্বিত।", [
    ALLAHUMMA, ("صَلِّ", "send prayers", "রহমত পাঠাও", "صَلَّى|صلو", ["cmd"]), ALA, MUHAMMAD_I, WA_ALA, AAL, MUHAMMAD_I, KAMA,
    ("صَلَّيۡتَ", "You sent prayers", "তুমি পাঠিয়েছ", "صَلَّى|صلو", ["you_did"]), ALA, IBRAHIM, WA_ALA, AAL, IBRAHIM] + INNAKA_HAMID,
   "After the tashahhud in the last sitting.", "শেষ বৈঠকে তাশাহহুদের পর।"),
 L("salawat2", "O Allah, bless Muhammad and the family of Muhammad, as You blessed Ibrahim and the family of Ibrahim. Indeed, You are Praiseworthy, Glorious.",
   "হে আল্লাহ, মুহাম্মাদ ও তাঁর পরিবারকে বরকত দাও, যেমন ইবরাহিম ও তাঁর পরিবারকে বরকত দিয়েছ। নিশ্চয়ই তুমি প্রশংসিত, মহিমান্বিত।", [
    ALLAHUMMA, ("بَارِكۡ", "bless", "বরকত দাও", "بارَكَ|برك", ["cmd"]), ALA, MUHAMMAD_I, WA_ALA, AAL, MUHAMMAD_I, KAMA,
    ("بَارَكۡتَ", "You blessed", "তুমি বরকত দিয়েছ", "بارَكَ|برك", ["you_did"]), ALA, IBRAHIM, WA_ALA, AAL, IBRAHIM] + INNAKA_HAMID),
]
HAND["guide"] = GUIDE

def G(id, en, bn, when_en, when_bn, segs, unit=None):
    return dict(id=id, en=en, bn=bn, when_en=when_en, when_bn=when_bn, segs=segs, unit=unit)

SALAH_GUIDE = [
 G("takbir", "Takbir: starting", "তাকবির: শুরু", "Raise your hands and begin.", "হাত তুলে নামাজ শুরু।", [H("salah", "takbir")], "u3"),
 G("thana", "Opening dua", "সানা", "Quietly, after the first takbir.", "প্রথম তাকবিরের পর, নিচু স্বরে।", [H("guide", "thana")]),
 G("taawwudh", "Seeking refuge & Bismillah", "আউযুবিল্লাহ ও বিসমিল্লাহ", "Before Al-Fatiha.", "ফাতিহার আগে।", [H("guide", "taawwudh"), Q(1, 1)], "u1"),
 G("fatiha", "Al-Fatiha", "সূরা ফাতিহা", "In every rakʿah.", "প্রতি রাকাতে।", [Q(1, v) for v in range(2, 8)], "u1"),
 G("surah", "A short surah (e.g. Al-Ikhlas)", "একটি ছোট সূরা (যেমন ইখলাস)", "After Al-Fatiha in the first two rakʿahs. Any surah you know.", "প্রথম দুই রাকাতে ফাতিহার পর। যেকোনো জানা সূরা।",
   [Q(112, v) for v in range(1, 5)], "u4"),
 G("ruku", "Rukūʿ: bowing", "রুকু", "Bowing, hands on knees.", "ঝুঁকে, হাঁটুতে হাত রেখে।", [H("salah", "ruku")], "u3"),
 G("rising", "Rising from rukūʿ", "রুকু থেকে ওঠা", "Standing up again.", "আবার দাঁড়িয়ে।", [H("salah", "sami"), H("salah", "rabbana")], "u3"),
 G("sujud", "Sujūd: prostrating", "সিজদা", "Forehead on the ground.", "কপাল মাটিতে।", [H("salah", "sujud")], "u3"),
 G("jalsa", "Sitting between the two sujūd", "দুই সিজদার মাঝে বসা", "", "", [H("salah", "jalsa")], "u3"),
 G("tashahhud", "Tashahhud", "তাশাহহুদ", "Sitting, after every two rakʿahs.", "প্রতি দুই রাকাত পর বসে।",
   [H("tashahhud", x) for x in ("t1", "t2", "t3", "t4", "t5")], "u11"),
 G("salawat", "Salawat on the Prophet ﷺ", "দরুদ", "In the last sitting.", "শেষ বৈঠকে।", [H("guide", "salawat1"), H("guide", "salawat2")]),
 G("salam", "Salam: ending", "সালাম: শেষ", "Turning right, then left.", "ডানে, তারপর বামে ফিরে।", [H("tashahhud", "taslim")], "u11"),
]
