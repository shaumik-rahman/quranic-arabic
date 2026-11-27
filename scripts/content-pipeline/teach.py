# -*- coding: utf-8 -*-
"""Teaching pages and understanding checks.

Every grammar pinch ("p:<pattern id>") and sentence pattern ("s:<structure id>") is taught as a few swipeable
pages, each with one idea and big examples, and then checked with questions written to test that idea.

  P(title, text, ex=[...], vs=[...])   one page.  title/text = (English, Bangla)
      ex = example rows  X(arabic, English, Bangla)
      vs = two (or three) forms side by side to compare, also X(...)
  K(question, options, why, ar=None)   one check. The FIRST option is the right one (shuffled in the app).
      options are (English, Bangla) pairs, or Arabic strings for "which Arabic…" questions
      ar = Arabic shown big under the question
"""


def X(ar, en, bn):
    return dict(ar=ar, en=en, bn=bn)


def P(t, x, ex=(), vs=()):
    return dict(t_en=t[0], t_bn=t[1], x_en=x[0], x_bn=x[1], ex=list(ex), vs=list(vs))


def K(q, options, why, ar=None):
    ar_opts = isinstance(options[0], str)
    return dict(q_en=q[0], q_bn=q[1], ar=ar, ar_opts=ar_opts,
                options=[o if ar_opts else dict(en=o[0], bn=o[1]) for o in options], why_en=why[0], why_bn=why[1])


TEACH = {}

# =====================================================================================
# Grammar pinches
# =====================================================================================
TEACH["p:al"] = dict(pages=[
    P(("“the” is joined to the word", "“the” শব্দের সাথে জোড়া"),
      ("Arabic has no separate word for “the”. Instead ٱلۡـ is written on the front of the word. Without it, the word usually means “a”.",
       "আরবিতে “the” (নির্দিষ্ট করার) আলাদা শব্দ নেই। এর বদলে শব্দের সামনে ٱلۡـ লেখা হয়। এটি না থাকলে শব্দের অর্থ সাধারণত “একটি”।"),
      vs=[X("كِتَابٌ", "a book", "একটি বই"), X("ٱلۡكِتَابُ", "the book", "বইটি")],
      ex=[X("ٱلۡحَمۡدُ", "the praise", "প্রশংসা (সমস্ত)"), X("ٱلۡعَٰلَمِينَ", "the worlds", "জগতসমূহ"), X("ٱلرَّحِيمِ", "the Most Merciful", "পরম দয়ালু")]),
    P(("Sometimes you don't hear the ل", "কখনো ل শোনা যায় না"),
      ("Before 14 “sun letters” (ت ث د ذ ر ز س ش ص ض ط ظ ل ن) the ل is silent and the next letter is doubled: it gets a shadda ( ّ ). Before the other letters you hear al-.",
       "১৪টি “সূর্য অক্ষরের” (ت ث د ذ ر ز س ش ص ض ط ظ ل ن) আগে ل উচ্চারিত হয় না, পরের অক্ষরে তাশদীদ ( ّ ) পড়ে। বাকি অক্ষরের আগে “আল” শোনা যায়।"),
      ex=[X("ٱلرَّحۡمَٰنِ", "ar-Raḥmān: ل silent", "আর-রহমান: ل নীরব"), X("ٱلنَّاسِ", "an-nās: ل silent", "আন-নাস: ل নীরব"),
          X("ٱلۡحَمۡدُ", "al-ḥamd: ل heard", "আল-হামদ: ل শোনা যায়"), X("ٱلۡكِتَابُ", "al-kitāb: ل heard", "আল-কিতাব: ل শোনা যায়")]),
], checks=[
    K(("Which one means “the book”?", "কোনটির অর্থ “বইটি” (the book)?"),
      ["ٱلۡكِتَابُ", "كِتَابٌ", "كِتَابِي", "كِتَابُكَ"],
      ("ٱلۡـ on the front = “the”. كِتَابٌ = a book, كِتَابِي = my book, كِتَابُكَ = your book.",
       "সামনে ٱلۡـ = নির্দিষ্ট (the)। كِتَابٌ = একটি বই, كِتَابِي = আমার বই, كِتَابُكَ = তোমার বই।")),
])

TEACH["p:wa"] = dict(pages=[
    P(("وَ is glued to the next word", "وَ পরের শব্দের সাথে জোড়া"),
      ("وَ is a single letter, so it is never written alone. It sticks to the front of the next word. So وَإِيَّاكَ looks like one word, but it is two: وَ + إِيَّاكَ.",
       "وَ একটি মাত্র অক্ষর, তাই একা লেখা হয় না। এটি পরের শব্দের সামনে জুড়ে যায়। তাই وَإِيَّاكَ দেখতে এক শব্দ, আসলে দুটি: وَ + إِيَّاكَ।"),
      ex=[X("وَإِيَّاكَ", "and You alone", "এবং কেবল তোমারই"), X("وَعَمِلُواْ", "and they did", "এবং তারা করেছে"), X("وَٱلۡأَرۡضِ", "and the earth", "এবং পৃথিবী")]),
    P(("At the start of a surah: “By …!”", "সূরার শুরুতে: “শপথ …!”"),
      ("When a surah opens with وَ + a noun, it is an oath. Allah swears by something to make us pay attention to it.",
       "সূরা যখন وَ + বিশেষ্য দিয়ে শুরু হয়, তখন তা শপথ। আল্লাহ কোনো কিছুর শপথ করে আমাদের মনোযোগ টানেন।"),
      ex=[X("وَٱلۡعَصۡرِ", "By time!", "সময়ের শপথ!"), X("وَٱلضُّحَىٰ", "By the morning light!", "পূর্বাহ্নের শপথ!"), X("وَٱلشَّمۡسِ", "By the sun!", "সূর্যের শপথ!")]),
], checks=[
    K(("وَإِيَّاكَ is…", "وَإِيَّاكَ হলো…"),
      [("two words: “and” + “You alone”", "দুটি শব্দ: “এবং” + “কেবল তোমাকে”"), ("one word meaning “we”", "এক শব্দ, অর্থ “আমরা”"),
       ("a name", "একটি নাম"), ("“By You!” (an oath)", "“তোমার শপথ!”")],
      ("وَ is one letter, so it is joined to the next word: وَ (and) + إِيَّاكَ (You alone). It is an oath only at the start of a surah, before a noun.",
       "وَ একটি অক্ষর, তাই পরের শব্দের সাথে জুড়ে যায়: وَ (এবং) + إِيَّاكَ (কেবল তোমাকে)। শপথ হয় কেবল সূরার শুরুতে, বিশেষ্যের আগে।")),
])

TEACH["p:bi"] = dict(pages=[
    P(("بِـ = in / with / by", "بِـ = -এ / দিয়ে / সাথে"),
      ("Like وَ, بِـ is one letter joined to the next word. Its meaning depends on the sentence: “in”, “with” or “by”. You have said it thousands of times in بِسۡمِ ٱللَّهِ.",
       "وَ-এর মতো بِـ-ও একটি অক্ষর, পরের শব্দের সাথে জুড়ে যায়। অর্থ বাক্য অনুযায়ী: “-এ”, “দিয়ে” বা “সাথে”। بِسۡمِ ٱللَّهِ-তে আপনি এটি হাজারবার বলেছেন।"),
      ex=[X("بِسۡمِ ٱللَّهِ", "in the name of Allah", "আল্লাহর নামে"), X("بِٱلۡقَلَمِ", "with the pen", "কলম দিয়ে"),
          X("بِٱلۡحَقِّ", "with the truth", "সত্যের সাথে"), X("أَعُوذُ بِٱللَّهِ", "I seek refuge in Allah", "আমি আল্লাহর কাছে আশ্রয় চাই")]),
], checks=[
    K(("بِٱلۡقَلَمِ means…", "بِٱلۡقَلَمِ অর্থ…"),
      [("with the pen", "কলম দিয়ে"), ("the pen", "কলমটি"), ("my pen", "আমার কলম"), ("a pen", "একটি কলম")],
      ("بِـ (with) + ٱلۡـ (the) + قَلَم (pen).", "بِـ (দিয়ে) + ٱلۡـ (নির্দিষ্ট) + قَلَم (কলম)।"), ar="بِٱلۡقَلَمِ"),
])

TEACH["p:li"] = dict(pages=[
    P(("لِـ = for / belongs to", "لِـ = জন্য / -এর"),
      ("لِـ is joined to the next word. ٱلۡحَمۡدُ لِلَّهِ word for word is “the praise — for Allah”: all praise belongs to Allah.",
       "لِـ পরের শব্দের সাথে জুড়ে যায়। ٱلۡحَمۡدُ لِلَّهِ শব্দে শব্দে “প্রশংসা — আল্লাহর জন্য”: সব প্রশংসা আল্লাহরই।"),
      ex=[X("لِلَّهِ", "for Allah", "আল্লাহর জন্য"), X("لِرَبِّكَ", "for your Lord", "তোমার রবের জন্য"), X("لِي", "for me", "আমার জন্য")]),
    P(("Before “him, you…” it becomes لَـ", "“তার, তোমার…”-এর আগে হয় لَـ"),
      ("When an ending like ـهُۥ (him) or ـكَ (you) is added, the vowel changes from لِـ to لَـ. The meaning stays “for / belongs to”.",
       "ـهُۥ (তার) বা ـكَ (তোমার) জুড়লে لِـ বদলে لَـ হয়। অর্থ একই থাকে: “জন্য / -এর”।"),
      ex=[X("لَهُۥ", "for Him / His", "তাঁর জন্য / তাঁরই"), X("لَكَ", "for you", "তোমার জন্য"), X("لَكُمۡ", "for you all", "তোমাদের জন্য")]),
], checks=[
    K(("In ٱلۡحَمۡدُ لِلَّهِ, what does لِـ add?", "ٱلۡحَمۡدُ لِلَّهِ-তে لِـ কী যোগ করে?"),
      [("for / belongs to", "জন্য / -এর"), ("and", "এবং"), ("with", "দিয়ে"), ("the", "নির্দিষ্ট (the)")],
      ("لِـ = for: “the praise is for Allah”.", "لِـ = জন্য: “প্রশংসা আল্লাহর জন্য”।"), ar="ٱلۡحَمۡدُ لِلَّهِ"),
])

TEACH["p:fa"] = dict(pages=[
    P(("فَـ = so / then", "فَـ = তাই / তারপর"),
      ("فَـ links two ideas: the second one follows from the first. It is joined to the next word, like وَ.",
       "فَـ দুটি কথাকে জোড়ে: দ্বিতীয়টি প্রথমটির ফল। وَ-এর মতো এটিও পরের শব্দের সাথে জুড়ে যায়।"),
      ex=[X("فَصَلِّ", "so pray", "তাই নামাজ পড়ো"), X("فَسَبِّحۡ", "so glorify", "তাই তাসবিহ পড়ো"), X("فَٱعۡلَمۡ", "so know", "তাই জেনে রাখো")]),
    P(("وَ adds, فَـ follows", "وَ যোগ করে, فَـ ফল বোঝায়"),
      ("Al-Kawthar: “We have given you al-Kawthar, SO pray to your Lord.” The prayer is because of the gift. وَ would only say “and”.",
       "সূরা কাওসার: “আমরা তোমাকে কাওসার দিয়েছি, তাই তোমার রবের জন্য নামাজ পড়ো।” নামাজ সেই দানের কারণে। وَ শুধু “এবং” বলত।"),
      vs=[X("وَ", "and: just adds", "এবং: শুধু যোগ করে"), X("فَـ", "so: because of what came before", "তাই: আগের কথার কারণে")],
      ex=[X("فَصَلِّ لِرَبِّكَ", "so pray to your Lord", "তাই তোমার রবের জন্য নামাজ পড়ো")]),
], checks=[
    K(("فَصَلِّ means…", "فَصَلِّ অর্থ…"),
      [("So pray", "তাই নামাজ পড়ো"), ("And pray", "এবং নামাজ পড়ো"), ("Pray for", "-এর জন্য নামাজ পড়ো"), ("He prayed", "সে নামাজ পড়েছে")],
      ("فَـ = so, then.", "فَـ = তাই, তারপর।"), ar="فَصَلِّ"),
])

TEACH["p:na"] = dict(pages=[
    P(("On a noun: “our”", "বিশেষ্যে: “আমাদের”"),
      ("ـنَا at the end of a noun means “our”.", "বিশেষ্যের শেষে ـنَا মানে “আমাদের”।"),
      ex=[X("رَبَّنَا", "our Lord", "আমাদের রব"), X("بَيۡتُنَا", "our house", "আমাদের ঘর"), X("إِلَٰهُنَا", "our God", "আমাদের ইলাহ")]),
    P(("On a request: “us”", "অনুরোধে: “আমাদেরকে”"),
      ("On a command or a dua, ـنَا means “us”.", "আদেশ বা দোয়ায় ـنَا মানে “আমাদেরকে”।"),
      ex=[X("ٱهۡدِنَا", "guide us", "আমাদের পথ দেখাও"), X("ءَاتِنَا", "give us", "আমাদের দাও"), X("ٱغۡفِرۡ لَنَا", "forgive us", "আমাদের ক্ষমা করো")]),
    P(("On a past verb: “we did”", "অতীত ক্রিয়ায়: “আমরা করেছি”"),
      ("On a past-tense verb, ـنَا shows that “we” did it.", "অতীত কালের ক্রিয়ায় ـنَا বোঝায় “আমরা” করেছি।"),
      ex=[X("ظَلَمۡنَا", "we wronged", "আমরা জুলুম করেছি"), X("ءَامَنَّا", "we believed", "আমরা ঈমান এনেছি")]),
], checks=[
    K(("ٱهۡدِنَا means…", "ٱهۡدِنَا অর্থ…"),
      [("Guide us", "আমাদের পথ দেখাও"), ("Guide me", "আমাকে পথ দেখাও"), ("our guidance", "আমাদের হিদায়াত"), ("He guided us", "তিনি আমাদের পথ দেখিয়েছেন")],
      ("ٱهۡدِ (guide!) + ـنَا (us).", "ٱهۡدِ (পথ দেখাও!) + ـنَا (আমাদের)।"), ar="ٱهۡدِنَا"),
])

TEACH["p:ka"] = dict(pages=[
    P(("ـكَ = you / your", "ـكَ = তুমি / তোমার"),
      ("ـكَ at the end means “you” or “your”, speaking to one person.", "শেষে ـكَ মানে “তোমাকে” বা “তোমার”, একজনকে বলা।"),
      ex=[X("رَبُّكَ", "your Lord", "তোমার রব"), X("عَلَيۡكَ", "upon you", "তোমার উপর"), X("إِيَّاكَ", "You (alone)", "কেবল তোমাকে"), X("بَيۡتُكَ", "your house", "তোমার ঘর")]),
    P(("Same word, different owner", "একই শব্দ, ভিন্ন মালিক"),
      ("Only the ending changes. The word in front stays the same.", "শুধু শেষটা বদলায়। সামনের শব্দ একই থাকে।"),
      vs=[X("رَبِّي", "my Lord", "আমার রব"), X("رَبُّكَ", "your Lord", "তোমার রব"), X("رَبُّنَا", "our Lord", "আমাদের রব")]),
], checks=[
    K(("رَبُّكَ means…", "رَبُّكَ অর্থ…"),
      [("your Lord", "তোমার রব"), ("my Lord", "আমার রব"), ("our Lord", "আমাদের রব"), ("their Lord", "তাদের রব")],
      ("ـكَ at the end = your.", "শেষে ـكَ = তোমার।"), ar="رَبُّكَ"),
])

TEACH["p:kum"] = dict(pages=[
    P(("ـكُمۡ = you all / your (many)", "ـكُمۡ = তোমরা / তোমাদের"),
      ("ـكَ is for one person; ـكُمۡ is for a group. That is why we greet with ٱلسَّلَٰمُ عَلَيۡكُمۡ: peace be upon you all.",
       "ـكَ একজনের জন্য; ـكُمۡ দলের জন্য। তাই আমরা সালাম দিই ٱلسَّلَٰمُ عَلَيۡكُمۡ: তোমাদের সবার উপর শান্তি।"),
      vs=[X("عَلَيۡكَ", "upon you (one person)", "তোমার উপর (একজন)"), X("عَلَيۡكُمۡ", "upon you all (a group)", "তোমাদের উপর (অনেকে)")],
      ex=[X("رَبُّكُمۡ", "your Lord (all of you)", "তোমাদের রব"), X("لَكُمۡ دِينُكُمۡ", "for you is your religion", "তোমাদের জন্য তোমাদের দ্বীন")]),
], checks=[
    K(("Why ـكُمۡ, not ـكَ, in ٱلسَّلَٰمُ عَلَيۡكُمۡ?", "ٱلسَّلَٰمُ عَلَيۡكُمۡ-এ ـكَ নয়, ـكُمۡ কেন?"),
      [("It greets everyone (a group)", "এটি সবাইকে (দলকে) সালাম দেয়"), ("It is for one person", "এটি একজনের জন্য"),
       ("It means “our”", "এর অর্থ “আমাদের”"), ("It means “them”", "এর অর্থ “তাদের”")],
      ("ـكُمۡ = you all.", "ـكُمۡ = তোমরা সবাই।")),
])

TEACH["p:hu"] = dict(pages=[
    P(("ـهُۥ = him / his / it", "ـهُۥ = তাকে / তার"),
      ("ـهُۥ at the end means “him”, “his” or “it”. In the Quran it very often refers to Allah; translations write “His” with a capital H.",
       "শেষে ـهُۥ মানে “তাকে”, “তার”। কুরআনে প্রায়ই এটি আল্লাহকে বোঝায়: “তাঁর”, “তাঁকে”।"),
      ex=[X("عَبۡدُهُۥ", "His servant", "তাঁর বান্দা"), X("رَسُولُهُۥ", "His messenger", "তাঁর রাসূল"), X("لَهُۥ", "for Him / His", "তাঁরই")]),
    P(("-hu or -hi? Same meaning", "-হু নাকি -হি? অর্থ একই"),
      ("After an i-sound, ـهُۥ becomes ـهِۦ. It is only easier to say; the meaning does not change.",
       "ই-ধ্বনির পরে ـهُۥ হয়ে যায় ـهِۦ। এটা শুধু উচ্চারণের সুবিধা; অর্থ বদলায় না।"),
      vs=[X("عَبۡدُهُۥ", "His servant: -hu", "তাঁর বান্দা: -হু"), X("بِإِذۡنِهِۦ", "by His permission: -hi", "তাঁর অনুমতিতে: -হি")]),
], checks=[
    K(("رَسُولُهُۥ means…", "رَسُولُهُۥ অর্থ…"),
      [("His messenger", "তাঁর রাসূল"), ("my messenger", "আমার রাসূল"), ("your messenger", "তোমার রাসূল"), ("their messenger", "তাদের রাসূল")],
      ("ـهُۥ at the end = his / His.", "শেষে ـهُۥ = তার / তাঁর।"), ar="رَسُولُهُۥ"),
])

TEACH["p:hum"] = dict(pages=[
    P(("ـهُمۡ = them / their", "ـهُمۡ = তাদের"),
      ("ـهُمۡ at the end means “them” or “their”: many people. After an i-sound it becomes ـهِمۡ.",
       "শেষে ـهُمۡ মানে “তাদের”: অনেক মানুষ। ই-ধ্বনির পরে হয় ـهِمۡ।"),
      ex=[X("عَلَيۡهِمۡ", "upon them", "তাদের উপর"), X("رَبُّهُمۡ", "their Lord", "তাদের রব"), X("لَهُمۡ", "for them", "তাদের জন্য")]),
    P(("One or many?", "একজন নাকি অনেকে?"),
      ("Add a م and “him” becomes “them”.", "একটি م যোগ করলে “তার” হয়ে যায় “তাদের”।"),
      vs=[X("رَبُّهُۥ", "his Lord (one)", "তার রব (একজন)"), X("رَبُّهُمۡ", "their Lord (many)", "তাদের রব (অনেকে)")]),
], checks=[
    K(("عَلَيۡهِمۡ means…", "عَلَيۡهِمۡ অর্থ…"),
      [("upon them", "তাদের উপর"), ("upon him", "তার উপর"), ("upon you", "তোমার উপর"), ("upon us", "আমাদের উপর")],
      ("ـهِمۡ = them.", "ـهِمۡ = তাদের।"), ar="عَلَيۡهِمۡ"),
])

TEACH["p:huma"] = dict(pages=[
    P(("A special form for two", "দুইয়ের জন্য আলাদা রূপ"),
      ("Arabic has a form for exactly two people or things! ـهُمَا = the two of them.",
       "আরবিতে ঠিক দুজন বা দুটি জিনিসের জন্য আলাদা রূপ আছে! ـهُمَا = তারা দুজন।"),
      vs=[X("ـهُۥ", "him: one", "তার: একজন"), X("ـهُمَا", "both of them: two", "তাদের দুজনের: দুই"), X("ـهُمۡ", "them: three or more", "তাদের: তিন বা বেশি")],
      ex=[X("ٱرۡحَمۡهُمَا", "have mercy on them both (my parents)", "তাঁদের দুজনকে দয়া করো (বাবা-মা)"),
          X("حِفۡظُهُمَا", "guarding them both (heavens and earth)", "এ দুটির রক্ষণাবেক্ষণ (আকাশ ও পৃথিবী)")]),
], checks=[
    K(("رَّبِّ ٱرۡحَمۡهُمَا is a dua for…", "رَّبِّ ٱرۡحَمۡهُمَا দোয়াটি কাদের জন্য?"),
      [("two people: my parents", "দুজনের জন্য: বাবা-মা"), ("one person", "একজনের জন্য"), ("a big group", "একটি বড় দলের জন্য"), ("myself", "নিজের জন্য")],
      ("ـهُمَا = the two of them.", "ـهُمَا = তারা দুজন।")),
])

TEACH["p:i"] = dict(pages=[
    P(("ـِي = me / my", "ـِي = আমার / আমাকে"),
      ("ـِي at the end means “my” on a noun and “me” on a verb.", "শেষে ـِي মানে বিশেষ্যে “আমার”, ক্রিয়ায় “আমাকে”।"),
      ex=[X("رَبِّي", "my Lord", "আমার রব"), X("أَبِي", "my father", "আমার বাবা"), X("أُمِّي", "my mother", "আমার মা"), X("زِدۡنِي", "increase me", "আমাকে বাড়িয়ে দাও")]),
    P(("When calling, the ي often drops", "ডাকার সময় ي প্রায়ই বাদ পড়ে"),
      ("In a dua, رَبِّي often becomes رَبِّ. It still means “my Lord”: the kasra under ب is what is left of the ي.",
       "দোয়ায় رَبِّي প্রায়ই হয়ে যায় رَبِّ। অর্থ তবুও “আমার রব”: ب-এর নিচের যের হলো ي-এর চিহ্ন।"),
      vs=[X("رَبِّي", "my Lord", "আমার রব"), X("رَبِّ ٱغۡفِرۡ لِي", "My Lord, forgive me", "হে আমার রব, আমাকে ক্ষমা করো")]),
], checks=[
    K(("أُمِّي means…", "أُمِّي অর্থ…"),
      [("my mother", "আমার মা"), ("a mother", "একজন মা"), ("your mother", "তোমার মা"), ("our mother", "আমাদের মা")],
      ("ـِي at the end = my.", "শেষে ـِي = আমার।"), ar="أُمِّي"),
])

TEACH["p:we_do"] = dict(pages=[
    P(("The first letter tells you who", "প্রথম অক্ষর বলে কে"),
      ("In a present-tense verb the root letters sit in the middle, and the first letter tells you who does it. نَـ = we.",
       "বর্তমান কালের ক্রিয়ায় মূল অক্ষর মাঝে থাকে, আর প্রথম অক্ষর বলে কে করছে। نَـ = আমরা।"),
      ex=[X("نَعۡبُدُ", "we worship", "আমরা ইবাদত করি"), X("نَسۡتَعِينُ", "we ask for help", "আমরা সাহায্য চাই"),
          X("نَقۡرَأُ", "we read", "আমরা পড়ি"), X("نَذۡهَبُ", "we go", "আমরা যাই")]),
    P(("Spot the root", "মূল অক্ষর খুঁজুন"),
      ("Take away نَـ and you find the root. ع ب د is about worship: the same letters as عَبۡدٌ, a servant (Abdullah = servant of Allah).",
       "نَـ সরালে মূল পাওয়া যায়। ع ب د মানে ইবাদত: عَبۡدٌ (বান্দা)-এর একই অক্ষর (আব্দুল্লাহ = আল্লাহর বান্দা)।"),
      vs=[X("عَبۡدٌ", "a servant", "একজন বান্দা"), X("نَعۡبُدُ", "we worship", "আমরা ইবাদত করি")]),
], checks=[
    K(("نَذۡهَبُ means…", "نَذۡهَبُ অর্থ…"),
      [("we go", "আমরা যাই"), ("I go", "আমি যাই"), ("he goes", "সে যায়"), ("they went", "তারা গেল")],
      ("نَـ at the start = we.", "শুরুতে نَـ = আমরা।"), ar="نَذۡهَبُ"),
])

TEACH["p:i_do"] = dict(pages=[
    P(("أَ at the start = I", "শুরুতে أَ = আমি"),
      ("A present-tense verb starting with أَ (or أُ) means “I do…”.", "বর্তমান কালের ক্রিয়া أَ (বা أُ) দিয়ে শুরু হলে মানে “আমি করি…”।"),
      ex=[X("أَعُوذُ", "I seek refuge", "আমি আশ্রয় চাই"), X("أَشۡهَدُ", "I bear witness", "আমি সাক্ষ্য দিই"),
          X("أَكۡتُبُ", "I write", "আমি লিখি"), X("أَقۡرَأُ", "I read", "আমি পড়ি")]),
    P(("Only the first letter changes", "শুধু প্রথম অক্ষর বদলায়"),
      ("Compare: same verb, different person.", "তুলনা করুন: একই ক্রিয়া, ভিন্ন কর্তা।"),
      vs=[X("نَعۡبُدُ", "we worship", "আমরা ইবাদত করি"), X("أَعۡبُدُ", "I worship", "আমি ইবাদত করি")],
      ex=[X("لَآ أَعۡبُدُ مَا تَعۡبُدُونَ", "I do not worship what you worship (109:2)", "তোমরা যার ইবাদত করো আমি তার ইবাদত করি না (১০৯:২)")]),
], checks=[
    K(("أَشۡهَدُ means…", "أَشۡهَدُ অর্থ…"),
      [("I bear witness", "আমি সাক্ষ্য দিই"), ("we bear witness", "আমরা সাক্ষ্য দিই"), ("he bears witness", "সে সাক্ষ্য দেয়"), ("Bear witness!", "সাক্ষ্য দাও!")],
      ("أَ at the start = I.", "শুরুতে أَ = আমি।"), ar="أَشۡهَدُ"),
])

TEACH["p:ya"] = dict(pages=[
    P(("يَـ at the start = he", "শুরুতে يَـ = সে"),
      ("A present-tense verb starting with يَـ (or يُـ) means “he does…” (or “it does…”).", "বর্তমান কালের ক্রিয়া يَـ (বা يُـ) দিয়ে শুরু হলে মানে “সে করে…”।"),
      ex=[X("يَعۡلَمُ", "He knows", "তিনি জানেন"), X("يَذۡهَبُ", "he goes", "সে যায়"), X("يَقۡرَأُ", "he reads", "সে পড়ে")]),
    P(("Add ـُونَ for “they”", "“তারা”-র জন্য ـُونَ"),
      ("Keep يَـ at the start and add ـُونَ at the end: now it is “they do…”.", "শুরুতে يَـ রেখে শেষে ـُونَ যোগ করলে: “তারা করে…”।"),
      vs=[X("يَعۡلَمُ", "he knows", "সে জানে"), X("يَعۡلَمُونَ", "they know", "তারা জানে")],
      ex=[X("يَدۡخُلُونَ", "they enter", "তারা প্রবেশ করে")]),
    P(("The four starts", "চারটি শুরু"),
      ("One verb, four people. Learn these four letters and you can read thousands of verbs.",
       "একটি ক্রিয়া, চারজন কর্তা। এই চারটি অক্ষর শিখলে হাজারো ক্রিয়া পড়তে পারবেন।"),
      ex=[X("أَقۡرَأُ", "I read", "আমি পড়ি"), X("نَقۡرَأُ", "we read", "আমরা পড়ি"), X("يَقۡرَأُ", "he reads", "সে পড়ে"), X("تَقۡرَأُ", "you read", "তুমি পড়ো")]),
], checks=[
    K(("يَعۡلَمُونَ means…", "يَعۡلَمُونَ অর্থ…"),
      [("they know", "তারা জানে"), ("he knows", "সে জানে"), ("we know", "আমরা জানি"), ("I know", "আমি জানি")],
      ("يَـ at the start + ـُونَ at the end = they.", "শুরুতে يَـ + শেষে ـُونَ = তারা।"), ar="يَعۡلَمُونَ"),
])

TEACH["p:you_did"] = dict(pages=[
    P(("Past verbs show “who” at the END", "অতীত ক্রিয়ায় কর্তা থাকে শেষে"),
      ("In the past tense the plain form means “he did”. Add ـتَ at the end and it means “you did”.",
       "অতীত কালে শেষে কিছু না থাকলে মানে “সে করেছে”। শেষে ـتَ যোগ করলে “তুমি করেছ”।"),
      vs=[X("أَنۡعَمَ", "he blessed", "সে নিয়ামত দিয়েছে"), X("أَنۡعَمۡتَ", "You blessed", "তুমি নিয়ামত দিয়েছ")],
      ex=[X("رَأَيۡتَ", "you saw", "তুমি দেখেছ"), X("خَلَقۡتَ", "You created", "তুমি সৃষ্টি করেছ")]),
], checks=[
    K(("خَلَقۡتَ means…", "خَلَقۡتَ অর্থ…"),
      [("You created", "তুমি সৃষ্টি করেছ"), ("he created", "সে সৃষ্টি করেছে"), ("we created", "আমরা সৃষ্টি করেছি"), ("they created", "তারা সৃষ্টি করেছে")],
      ("ـتَ at the end of a past verb = you.", "অতীত ক্রিয়ার শেষে ـتَ = তুমি।"), ar="خَلَقۡتَ"),
])

TEACH["p:we_did"] = dict(pages=[
    P(("ـنَا at the end = we did", "শেষে ـنَا = আমরা করেছি"),
      ("Add ـنَا to a past verb and it means “we did”.", "অতীত ক্রিয়ায় ـنَا যোগ করলে “আমরা করেছি”।"),
      ex=[X("ظَلَمۡنَا", "we wronged", "আমরা জুলুম করেছি"), X("ءَامَنَّا", "we believed", "আমরা ঈমান এনেছি"), X("أَعۡطَيۡنَٰكَ", "We gave you", "আমরা তোমাকে দিয়েছি")]),
    P(("When Allah says “We”", "আল্লাহ যখন “আমরা” বলেন"),
      ("In the Quran Allah often says “We”. This is the “We” of majesty, as a king speaks. It never means more than one God.",
       "কুরআনে আল্লাহ প্রায়ই “আমরা” বলেন। এটি মহিমার “আমরা”, যেমন রাজা বলেন। এর অর্থ কখনো একাধিক ইলাহ নয়।"),
      ex=[X("إِنَّآ أَعۡطَيۡنَٰكَ ٱلۡكَوۡثَرَ", "Indeed, We have given you al-Kawthar", "নিশ্চয়ই আমরা তোমাকে কাওসার দিয়েছি")]),
], checks=[
    K(("ظَلَمۡنَا means…", "ظَلَمۡنَا অর্থ…"),
      [("we wronged", "আমরা জুলুম করেছি"), ("he wronged", "সে জুলুম করেছে"), ("you wronged", "তুমি জুলুম করেছ"), ("they wronged", "তারা জুলুম করেছে")],
      ("ـنَا at the end of a past verb = we.", "অতীত ক্রিয়ার শেষে ـنَا = আমরা।"), ar="ظَلَمۡنَا"),
])

TEACH["p:they_did"] = dict(pages=[
    P(("ـُواْ at the end = they did", "শেষে ـُواْ = তারা করেছে"),
      ("Add ـُواْ to a past verb for “they did”. The last ا is written but not read.",
       "অতীত ক্রিয়ায় ـُواْ যোগ করলে “তারা করেছে”। শেষের ا লেখা হয়, পড়া হয় না।"),
      vs=[X("ءَامَنَ", "he believed", "সে ঈমান এনেছে"), X("ءَامَنُواْ", "they believed", "তারা ঈমান এনেছে")],
      ex=[X("عَمِلُواْ", "they did", "তারা করেছে"), X("ذَهَبُواْ", "they went", "তারা গেছে")]),
], checks=[
    K(("ذَهَبُواْ means…", "ذَهَبُواْ অর্থ…"),
      [("they went", "তারা গেছে"), ("he went", "সে গেছে"), ("we went", "আমরা গেছি"), ("Go!", "যাও!")],
      ("ـُواْ at the end of a past verb = they.", "অতীত ক্রিয়ার শেষে ـُواْ = তারা।"), ar="ذَهَبُواْ"),
])

TEACH["p:cmd"] = dict(pages=[
    P(("A command is short", "আদেশ ছোট হয়"),
      ("Many short words in the Quran are commands: “Do it!”", "কুরআনের অনেক ছোট শব্দ আদেশ: “করো!”"),
      ex=[X("قُلۡ", "Say!", "বলো!"), X("ٱقۡرَأۡ", "Read!", "পড়ো!"), X("ٱغۡفِرۡ", "Forgive!", "ক্ষমা করো!"), X("سَبِّحۡ", "Glorify!", "তাসবিহ পড়ো!")]),
    P(("How to spot one", "কীভাবে চিনবেন"),
      ("Often a command starts with ٱ and ends with a sukun ( ۡ ). Compare it with “he reads”.",
       "আদেশ প্রায়ই ٱ দিয়ে শুরু হয় আর সুকুন ( ۡ ) দিয়ে শেষ হয়। “সে পড়ে”-র সাথে তুলনা করুন।"),
      vs=[X("يَقۡرَأُ", "he reads", "সে পড়ে"), X("ٱقۡرَأۡ", "Read!", "পড়ো!")]),
    P(("To Allah, it is a humble request", "আল্লাহকে বললে বিনীত অনুরোধ"),
      ("In a dua the same command form is said to Allah. Then it is not an order but a humble request.",
       "দোয়ায় একই আদেশ-রূপ আল্লাহকে বলা হয়। তখন তা আদেশ নয়, বিনীত অনুরোধ।"),
      ex=[X("رَبِّ ٱغۡفِرۡ لِي", "My Lord, forgive me", "হে আমার রব, আমাকে ক্ষমা করো"), X("ٱهۡدِنَا", "Guide us", "আমাদের পথ দেখাও")]),
], checks=[
    K(("ٱقۡرَأۡ means…", "ٱقۡرَأۡ অর্থ…"),
      [("Read!", "পড়ো!"), ("he reads", "সে পড়ে"), ("I read", "আমি পড়ি"), ("we read", "আমরা পড়ি")],
      ("ٱ at the start and sukun at the end: a command.", "শুরুতে ٱ আর শেষে সুকুন: আদেশ।"), ar="ٱقۡرَأۡ"),
])

TEACH["p:plural"] = dict(pages=[
    P(("ـُونَ / ـِينَ = many people", "ـُونَ / ـِينَ = অনেক মানুষ"),
      ("Add ـُونَ or ـِينَ to a word for a person and you get many of them.", "ব্যক্তিবাচক শব্দে ـُونَ বা ـِينَ যোগ করলে বহুবচন হয়।"),
      vs=[X("مُؤۡمِنٌ", "a believer", "একজন মুমিন"), X("مُؤۡمِنُونَ", "believers", "মুমিনরা")],
      ex=[X("ٱلۡمُسۡلِمُونَ", "the Muslims", "মুসলিমরা"), X("ٱلصَّٰلِحِينَ", "the righteous", "নেককাররা")]),
    P(("-ūna or -īna? Same meaning", "-ঊনা নাকি -ঈনা? অর্থ একই"),
      ("ـُونَ is used when they are the ones doing something; ـِينَ after a small word like فِي or مِنَ, or when something is done to them. For now, just recognise both.",
       "তারা নিজেরা কিছু করলে ـُونَ; فِي বা مِنَ-এর মতো ছোট শব্দের পরে বা তাদের প্রতি কিছু করা হলে ـِينَ। আপাতত দুটোই চিনে রাখুন।"),
      vs=[X("ٱلۡمُؤۡمِنُونَ", "the believers", "মুমিনরা"), X("ٱلۡمُؤۡمِنِينَ", "the believers", "মুমিনরা")]),
    P(("Things often use ـَات", "জিনিসের বহুবচনে প্রায়ই ـَات"),
      ("Many words for things make their plural with ـَات.", "অনেক বস্তুবাচক শব্দের বহুবচন হয় ـَات দিয়ে।"),
      vs=[X("صَالِحَةٌ", "a good deed", "একটি সৎকাজ"), X("ٱلصَّٰلِحَٰتِ", "good deeds", "সৎকাজসমূহ")]),
], checks=[
    K(("ٱلۡمُؤۡمِنُونَ means…", "ٱلۡمُؤۡمِنُونَ অর্থ…"),
      [("the believers", "মুমিনরা"), ("a believer", "একজন মুমিন"), ("the believer", "মুমিন ব্যক্তিটি"), ("belief", "ঈমান")],
      ("ـُونَ at the end = many people.", "শেষে ـُونَ = অনেক মানুষ।"), ar="ٱلۡمُؤۡمِنُونَ"),
])

TEACH["p:doer"] = dict(pages=[
    P(("Words grow from 3 root letters", "শব্দ জন্মায় ৩টি মূল অক্ষর থেকে"),
      ("Most Arabic words are built on three root letters. ك ت ب is about writing. Put the letters into different shapes and you get related words.",
       "বেশিরভাগ আরবি শব্দ তিনটি মূল অক্ষরে গড়া। ك ت ب মানে লেখা। অক্ষরগুলো ভিন্ন ছাঁচে বসালে সম্পর্কিত শব্দ হয়।"),
      ex=[X("كَتَبَ", "he wrote", "সে লিখেছে"), X("كِتَابٌ", "a book", "একটি বই"), X("كَاتِبٌ", "a writer", "একজন লেখক"), X("مَكۡتُوبٌ", "written", "লিখিত")]),
    P(("The shape فَاعِل = the doer", "فَاعِل ছাঁচ = যে করে"),
      ("Put ā after the 1st root letter and i after the 2nd: you get “the one who does it”.",
       "১ম মূল অক্ষরের পরে আ, ২য়টির পরে ই বসালে হয় “যে কাজটি করে”।"),
      ex=[X("كَاتِبٌ", "a writer (ك ت ب)", "লেখক (ك ت ب)"), X("مَٰلِكٌ", "an owner, master (م ل ك)", "মালিক (م ل ك)"),
          X("خَالِقٌ", "a creator (خ ل ق)", "স্রষ্টা (خ ل ق)"), X("حَاسِدٌ", "an envier (ح س د)", "হিংসুক (ح س د)")]),
], checks=[
    K(("ع ب د = worship. So عَابِدٌ means…", "ع ب د = ইবাদত। তাহলে عَابِدٌ অর্থ…"),
      [("a worshipper", "ইবাদতকারী"), ("worship", "ইবাদত"), ("one who is worshipped", "যার ইবাদত করা হয়"), ("we worship", "আমরা ইবাদত করি")],
      ("The فَاعِل shape = the one who does it.", "فَاعِل ছাঁচ = যে কাজটি করে।"), ar="عَابِدٌ"),
])

TEACH["p:done_to"] = dict(pages=[
    P(("The shape مَفۡعُول = the one it is done to", "مَفۡعُول ছাঁচ = যার প্রতি করা হয়"),
      ("Put مَـ in front and ū before the last root letter: you get “the one it is done to”. Compare with the doer.",
       "সামনে مَـ আর শেষ মূল অক্ষরের আগে ঊ বসালে হয় “যার প্রতি কাজটি করা হয়েছে”। কর্তার সাথে তুলনা করুন।"),
      vs=[X("كَاتِبٌ", "a writer (does it)", "লেখক (যে লেখে)"), X("مَكۡتُوبٌ", "written (it is done to)", "লিখিত (যা লেখা হয়েছে)")]),
    P(("You already know some!", "কিছু আপনি আগেই জানেন!"),
      ("Many names have this shape.", "অনেক নাম এই ছাঁচে গড়া।"),
      ex=[X("مَحۡمُودٌ", "praised: Mahmud (ح م د)", "প্রশংসিত: মাহমুদ (ح م د)"), X("مَحۡبُوبٌ", "beloved: Mahbub (ح ب ب)", "প্রিয়: মাহবুব (ح ب ب)"),
          X("ٱلۡمَغۡضُوبِ", "those under anger (غ ض ب)", "যাদের উপর গজব (غ ض ب)")]),
], checks=[
    K(("ع ب د = worship. So مَعۡبُودٌ means…", "ع ب د = ইবাদত। তাহলে مَعۡبُودٌ অর্থ…"),
      [("one who is worshipped", "যার ইবাদত করা হয়"), ("a worshipper", "ইবাদতকারী"), ("he worshipped", "সে ইবাদত করেছে"), ("we worship", "আমরা ইবাদত করি")],
      ("The مَفۡعُول shape = the one it is done to.", "مَفۡعُول ছাঁচ = যার প্রতি করা হয়।"), ar="مَعۡبُودٌ"),
])

# ---------------- two ideas that used to be mentioned in passing ----------------
NEW_PATTERNS = [
    dict(id="un", ar="ـٌ / ـً / ـٍ", en="a / an", bn="একটি", emoji="☝️",
         expl_en="A doubled vowel at the end (read -un, -an or -in) means “a / an”.",
         expl_bn="শেষে দ্বিগুণ স্বরচিহ্ন (পড়া হয় -উন, -আন বা -ইন) মানে “একটি”।"),
    dict(id="endings", ar="ـُ / ـِ / ـَ", en="the last vowel moves", bn="শেষ স্বরচিহ্ন বদলায়", emoji="🔄",
         expl_en="The vowel on the last letter changes with the word's job in the sentence. The meaning of the word stays the same.",
         expl_bn="বাক্যে শব্দের কাজ অনুযায়ী শেষ অক্ষরের স্বরচিহ্ন বদলায়। শব্দের অর্থ একই থাকে।"),
]

TEACH["p:un"] = dict(pages=[
    P(("a pen or the pen?", "একটি কলম নাকি কলমটি?"),
      ("Look at the end of قَلَمٌ. The vowel is doubled ( ٌ ), so you read qalam-un. This -un is how Arabic says “a”.",
       "قَلَمٌ-এর শেষে দেখুন: স্বরচিহ্ন দ্বিগুণ ( ٌ ), তাই পড়া হয় কালাম-উন। এই -উন দিয়েই আরবিতে “একটি” বোঝায়।"),
      vs=[X("قَلَمٌ", "a pen", "একটি কলম"), X("ٱلۡقَلَمُ", "the pen", "কলমটি")]),
    P(("Three ways to write it", "লেখার তিনটি রূপ"),
      ("The doubled vowel can be ـٌ (-un), ـً (-an) or ـٍ (-in). All three mean “a”. Which one appears depends on the sentence (like the last vowel you will meet later).",
       "দ্বিগুণ স্বরচিহ্ন হতে পারে ـٌ (-উন), ـً (-আন) বা ـٍ (-ইন)। তিনটিরই অর্থ “একটি”। কোনটি বসবে তা বাক্যের উপর নির্ভর করে।"),
      ex=[X("كِتَابٌ", "kitāb-un: a book", "কিতাব-উন: একটি বই"), X("رَسُولًا", "rasūl-an: a messenger", "রাসূল-আন: একজন রাসূল"),
          X("خُسۡرٍ", "khusr-in: a loss", "খুসর-ইন: একটি ক্ষতি")]),
    P(("Never both", "দুটো একসাথে কখনো নয়"),
      ("A word has ٱلۡـ (the) or the doubled vowel (a), never both. So you can always tell “a” from “the” by looking at the two ends of the word.",
       "শব্দে হয় ٱلۡـ (নির্দিষ্ট) থাকে, নয়তো দ্বিগুণ স্বরচিহ্ন (একটি), কখনো দুটো একসাথে নয়। তাই শব্দের দুই প্রান্ত দেখেই বোঝা যায়।"),
      vs=[X("بَيۡتٌ", "a house", "একটি ঘর"), X("ٱلۡبَيۡتُ", "the house", "ঘরটি")]),
    P(("In the Quran", "কুরআনে"),
      ("You have recited these many times.", "এগুলো আপনি বহুবার পড়েছেন।"),
      ex=[X("لَفِي خُسۡرٍ", "surely in a loss (103:2)", "অবশ্যই ক্ষতিতে (১০৩:২)"), X("نَارٌ حَامِيَةٌ", "a blazing fire (101:11)", "একটি জ্বলন্ত আগুন (১০১:১১)"),
          X("سَلَٰمٌ هِيَ", "Peace it is (97:5)", "শান্তিময় সেই রাত (৯৭:৫)")]),
], checks=[
    K(("قَلَمٌ means…", "قَلَمٌ অর্থ…"),
      [("a pen", "একটি কলম"), ("the pen", "কলমটি"), ("my pen", "আমার কলম"), ("pens", "কলমগুলো")],
      ("The doubled vowel ـٌ (-un) = “a”.", "দ্বিগুণ স্বরচিহ্ন ـٌ (-উন) = “একটি”।"), ar="قَلَمٌ"),
    K(("Which one means “a house”?", "কোনটির অর্থ “একটি ঘর”?"),
      ["بَيۡتٌ", "ٱلۡبَيۡتُ", "بَيۡتِي", "بَيۡتُكَ"],
      ("بَيۡتٌ ends with -un = a house. ٱلۡبَيۡتُ = the house, بَيۡتِي = my house, بَيۡتُكَ = your house.",
       "بَيۡتٌ-এর শেষে -উন = একটি ঘর। ٱلۡبَيۡتُ = ঘরটি, بَيۡتِي = আমার ঘর, بَيۡتُكَ = তোমার ঘর।")),
])

TEACH["p:endings"] = dict(pages=[
    P(("Same word, three endings", "একই শব্দ, তিন রকম শেষ"),
      ("All three are “Allah”. Only the last vowel moved: -u, -i, -a.", "তিনটিই “আল্লাহ”। শুধু শেষ স্বরচিহ্ন বদলেছে: -উ, -ই, -আ।"),
      ex=[X("ٱللَّهُ أَكۡبَرُ", "Allāh-u akbar: Allah is the Greatest", "আল্লাহু আকবার: আল্লাহ সবচেয়ে বড়"),
          X("بِسۡمِ ٱللَّهِ", "bismi-llāh-i: in the name of Allah", "বিসমিল্লাহি: আল্লাহর নামে"),
          X("إِنَّ ٱللَّهَ", "inna-llāh-a: indeed Allah", "ইন্নাল্লাহা: নিশ্চয়ই আল্লাহ")]),
    P(("A rough guide", "মোটামুটি নিয়ম"),
      ("-u: the word the sentence is about. -i: after “of”, or after بِـ, لِـ, فِي. -a: after إِنَّ, or when something is done to it.",
       "-উ: যে শব্দ নিয়ে বাক্য। -ই: “-এর” অর্থে, অথবা بِـ, لِـ, فِي-এর পরে। -আ: إِنَّ-এর পরে, অথবা যার প্রতি কাজ করা হয়।"),
      ex=[X("ٱلۡحَمۡدُ لِلَّهِ", "-u on ٱلۡحَمۡدُ: what it is about. -i on ٱللَّهِ: after لِـ", "ٱلۡحَمۡدُ-এ -উ: যা নিয়ে বাক্য। ٱللَّهِ-এ -ই: لِـ-এর পরে"),
          X("كِتَابُ ٱللَّهِ", "-i on ٱللَّهِ: the Book OF Allah", "ٱللَّهِ-এ -ই: আল্লাহর কিতাব"),
          X("نَقۡرَأُ ٱلۡقُرۡءَانَ", "-a on ٱلۡقُرۡءَانَ: what we read", "ٱلۡقُرۡءَانَ-এ -আ: যা আমরা পড়ি")]),
    P(("Recognise, don't worry", "চিনুন, চিন্তা নয়"),
      ("To understand the Quran you don't need to choose endings. Just recognise the word, whatever its last vowel.",
       "কুরআন বুঝতে শেষ স্বরচিহ্ন বেছে নিতে হবে না। শুধু শব্দটি চিনুন, শেষ স্বর যা-ই হোক।"),
      vs=[X("رَبُّ", "Lord", "রব"), X("رَبِّ", "Lord", "রব"), X("رَبَّ", "Lord", "রব")]),
], checks=[
    K(("ٱللَّهُ, ٱللَّهِ and ٱللَّهَ mean…", "ٱللَّهُ, ٱللَّهِ ও ٱللَّهَ অর্থ…"),
      [("All three: Allah", "তিনটিই: আল্লাহ"), ("Three different words", "তিনটি ভিন্ন শব্দ"),
       ("Allah, a god, gods", "আল্লাহ, একজন ইলাহ, ইলাহগণ"), ("Allah, my Allah, your Allah", "আল্লাহ, আমার আল্লাহ, তোমার আল্লাহ")],
      ("Only the last vowel moves; the word and its meaning stay the same.", "শুধু শেষ স্বরচিহ্ন বদলায়; শব্দ ও অর্থ একই থাকে।")),
    K(("Why does ٱللَّهِ end in -i in بِسۡمِ ٱللَّهِ?", "بِسۡمِ ٱللَّهِ-তে ٱللَّهِ কেন -ই দিয়ে শেষ?"),
      [("It means “of Allah”: the name OF Allah", "এর অর্থ “আল্লাহর”: আল্লাহর নাম"), ("It means “a god”", "এর অর্থ “একজন ইলাহ”"),
       ("It is a command", "এটি আদেশ"), ("It means “my Allah”", "এর অর্থ “আমার আল্লাহ”")],
      ("After “of” the word ends in -i.", "“-এর” অর্থে শব্দ -ই দিয়ে শেষ হয়।"), ar="بِسۡمِ ٱللَّهِ"),
])

# =====================================================================================
# Sentence patterns (the first page, with the coloured shape, is built from the structure itself)
# =====================================================================================
TEACH["s:is"] = dict(pages=[
    P(("Word for word", "শব্দে শব্দে"),
      ("You say this in every salah. Word for word it is “Allah — greatest”. English and Bangla need “is”; Arabic doesn't.",
       "প্রতি নামাজে আপনি এটি বলেন। শব্দে শব্দে “আল্লাহ — সবচেয়ে বড়”। বাংলায় “হলেন” লাগে; আরবিতে লাগে না।"),
      ex=[X("ٱللَّهُ أَكۡبَرُ", "Allah (is) the Greatest", "আল্লাহ (হলেন) সবচেয়ে বড়"), X("ٱللَّهُ رَبِّي", "Allah (is) my Lord", "আল্লাহ (হলেন) আমার রব")]),
    P(("This and that", "এটি ও ওটি"),
      ("هَٰذَا = this (near), ذَٰلِكَ = that (far). Then the thing. Remember: the doubled vowel at the end = “a”.",
       "هَٰذَا = এটি (কাছে), ذَٰلِكَ = ওটি (দূরে)। তারপর জিনিসটি। মনে রাখুন: শেষে দ্বিগুণ স্বরচিহ্ন = “একটি”।"),
      ex=[X("هَٰذَا قَلَمٌ", "This (is) a pen.", "এটি (হলো) একটি কলম।"), X("ذَٰلِكَ بَيۡتٌ", "That (is) a house.", "ওটি (হলো) একটি ঘর।"),
          X("هَٰذَا كِتَابٌ", "This (is) a book.", "এটি (হলো) একটি বই।")]),
    P(("He and she", "সে (ছেলে) ও সে (মেয়ে)"),
      ("هُوَ = he, هِيَ = she. Put a word after it and you have a sentence.", "هُوَ = সে/তিনি (পুরুষ), هِيَ = সে/তিনি (নারী)। পরে একটি শব্দ বসালেই বাক্য।"),
      ex=[X("هُوَ أَبِي", "He (is) my father.", "তিনি (হলেন) আমার বাবা।"), X("هِيَ أُمِّي", "She (is) my mother.", "তিনি (হলেন) আমার মা।")]),
    P(("In the Quran", "কুরআনে"),
      ("The same pattern, again and again.", "একই গঠন, বারবার।"),
      ex=[X("ذَٰلِكَ ٱلۡكِتَٰبُ", "That (is) the Book (2:2)", "ওটি (হলো) সেই কিতাব (২:২)"), X("ٱللَّهُ ٱلصَّمَدُ", "Allah (is) the Eternal Refuge (112:2)", "আল্লাহ (হলেন) অমুখাপেক্ষী (১১২:২)")]),
], checks=[
    K(("هُوَ أَبِي means…", "هُوَ أَبِي অর্থ…"),
      [("He is my father.", "তিনি আমার বাবা।"), ("his father", "তার বাবা"), ("he and my father", "সে আর আমার বাবা"), ("my father's house", "আমার বাবার ঘর")],
      ("هُوَ (he) + أَبِي (my father): “is” is invisible.", "هُوَ (তিনি) + أَبِي (আমার বাবা): “হলেন” লুকানো।"), ar="هُوَ أَبِي"),
    K(("Where is the word “is” in ٱللَّهُ أَكۡبَرُ?", "ٱللَّهُ أَكۡبَرُ-এ “হলেন” শব্দটি কোথায়?"),
      [("Nowhere: Arabic leaves it out", "কোথাও নেই: আরবিতে লাগে না"), ("ٱللَّهُ", "ٱللَّهُ"), ("أَكۡبَرُ", "أَكۡبَرُ"), ("the -u at the end", "শেষের -উ")],
      ("Two words side by side already make a sentence.", "দুটি শব্দ পাশাপাশি বসালেই বাক্য হয়।")),
    K(("How do you say “That is a house.”?", "“ওটি একটি ঘর।” আরবিতে কোনটি?"),
      ["ذَٰلِكَ بَيۡتٌ", "هَٰذَا بَيۡتٌ", "ذَٰلِكَ قَلَمٌ", "هُوَ بَيۡتِي"],
      ("ذَٰلِكَ = that, بَيۡتٌ = a house.", "ذَٰلِكَ = ওটি, بَيۡتٌ = একটি ঘর।")),
])

TEACH["s:of"] = dict(pages=[
    P(("Word for word", "শব্দে শব্দে"),
      ("Put two nouns side by side and the second means “of …”. In English you add “of” between them.",
       "দুটি বিশেষ্য পাশাপাশি বসালে দ্বিতীয়টির অর্থ হয় “-এর”। বাংলায় দ্বিতীয়টি আগে বলে “-এর” যোগ করুন।"),
      ex=[X("بَيۡتُ ٱللَّهِ", "house · Allah = the House of Allah", "ঘর · আল্লাহ = আল্লাহর ঘর"),
          X("كِتَابُ ٱللَّهِ", "book · Allah = the Book of Allah", "কিতাব · আল্লাহ = আল্লাহর কিতাব"),
          X("رَبِّ ٱلۡعَٰلَمِينَ", "Lord · the worlds = Lord of the worlds", "রব · জগতসমূহ = জগতসমূহের রব")]),
    P(("The first word drops ٱلۡـ and -un", "প্রথম শব্দ ٱلۡـ ও -উন হারায়"),
      ("The first word is already “the” because it belongs to someone. So it takes no ٱلۡـ and no doubled vowel.",
       "প্রথম শব্দটি কারও হওয়ায় এমনিতেই নির্দিষ্ট। তাই এতে ٱلۡـ বা দ্বিগুণ স্বরচিহ্ন বসে না।"),
      ex=[X("بَيۡتٌ", "a house", "একটি ঘর"), X("ٱلۡبَيۡتُ", "the house", "ঘরটি"), X("بَيۡتُ ٱللَّهِ", "the House of Allah: no ٱلۡـ, no -un", "আল্লাহর ঘর: ٱلۡـ নেই, -উন নেই")]),
    P(("Whose? My father's, my mother's", "কার? বাবার, মায়ের"),
      ("The second word can be anyone, also “my father” or “my mother”.", "দ্বিতীয় শব্দ যে কেউ হতে পারে, “আমার বাবা” বা “আমার মা”-ও।"),
      ex=[X("بَيۡتُ أَبِي", "my father's house", "আমার বাবার ঘর"), X("قَلَمُ أُمِّي", "my mother's pen", "আমার মায়ের কলম")]),
    P(("Chains", "শিকল"),
      ("You can link more than two: each word is “of” the next.", "দুটির বেশিও জোড়া যায়: প্রতিটি শব্দ পরেরটির “-এর”।"),
      ex=[X("مَٰلِكِ يَوۡمِ ٱلدِّينِ", "Master · day · judgment = Master of the Day of Judgment", "মালিক · দিন · বিচার = বিচার দিনের মালিক")]),
], checks=[
    K(("Which one means “the Book of Allah”?", "কোনটির অর্থ “আল্লাহর কিতাব”?"),
      ["كِتَابُ ٱللَّهِ", "ٱلۡكِتَابُ ٱللَّهِ", "كِتَابٌ ٱللَّهِ", "ٱللَّهُ كِتَابٌ"],
      ("The first word takes no ٱلۡـ and no -un, and the owner comes second.", "প্রথম শব্দে ٱلۡـ বা -উন বসে না, আর মালিক বসে দ্বিতীয়তে।")),
    K(("بَيۡتُ أَبِي means…", "بَيۡتُ أَبِي অর্থ…"),
      [("my father's house", "আমার বাবার ঘর"), ("My father is a house.", "আমার বাবা একটি ঘর।"), ("a house and my father", "একটি ঘর আর আমার বাবা"), ("my house's father", "আমার ঘরের বাবা")],
      ("house · my father = the house of my father.", "ঘর · আমার বাবা = আমার বাবার ঘর।"), ar="بَيۡتُ أَبِي"),
])

TEACH["s:after"] = dict(pages=[
    P(("The opposite order", "উল্টো ক্রম"),
      ("In Arabic the thing comes first, then the describing word: “house big” = a big house.",
       "আরবিতে আগে জিনিস, পরে বিশেষণ: “ঘর বড়” = একটি বড় ঘর।"),
      ex=[X("بَيۡتٌ كَبِيرٌ", "house · big = a big house", "ঘর · বড় = একটি বড় ঘর"), X("مَسۡجِدٌ كَبِيرٌ", "a big mosque", "একটি বড় মসজিদ"),
          X("قَلَمٌ جَدِيدٌ", "a new pen", "একটি নতুন কলম")]),
    P(("They match", "দুটি মিলে যায়"),
      ("The describing word copies its noun: both with ٱلۡـ, or both with the doubled vowel.",
       "বিশেষণ তার বিশেষ্যকে নকল করে: দুটিতেই ٱلۡـ, অথবা দুটিতেই দ্বিগুণ স্বরচিহ্ন।"),
      ex=[X("ٱلۡبَيۡتُ ٱلۡكَبِيرُ", "the big house", "বড় ঘরটি"), X("بَيۡتٌ كَبِيرٌ", "a big house", "একটি বড় ঘর"),
          X("ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ", "the straight path", "সরল পথ")]),
    P(("One ٱلۡـ makes a sentence", "একটি ٱلۡـ বাক্য বানায়"),
      ("If only the first word has ٱلۡـ, it is no longer “the big house”: it is a full sentence. One little ٱلۡـ changes everything!",
       "শুধু প্রথম শব্দে ٱلۡـ থাকলে আর “বড় ঘরটি” নয়: পুরো বাক্য হয়ে যায়। একটি ছোট্ট ٱلۡـ সব বদলে দেয়!"),
      vs=[X("ٱلۡبَيۡتُ ٱلۡكَبِيرُ", "the big house", "বড় ঘরটি"), X("ٱلۡبَيۡتُ كَبِيرٌ", "The house is big.", "ঘরটি বড়।")]),
], checks=[
    K(("Which one is the sentence “The house is big.”?", "কোনটি বাক্য “ঘরটি বড়।”?"),
      ["ٱلۡبَيۡتُ كَبِيرٌ", "ٱلۡبَيۡتُ ٱلۡكَبِيرُ", "بَيۡتٌ كَبِيرٌ"],
      ("ٱلۡـ only on the first word = a sentence. Both with ٱلۡـ = “the big house”, both with -un = “a big house”.",
       "শুধু প্রথম শব্দে ٱلۡـ = বাক্য। দুটিতে ٱلۡـ = “বড় ঘরটি”, দুটিতে -উন = “একটি বড় ঘর”।")),
    K(("ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ means…", "ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ অর্থ…"),
      [("the straight path", "সরল পথ"), ("The path is straight.", "পথটি সরল।"), ("a straight path", "একটি সরল পথ"), ("the path of the straight one", "সরল ব্যক্তির পথ")],
      ("Both words have ٱلۡـ: one phrase, “the straight path”.", "দুটিতেই ٱلۡـ: একটি শব্দগুচ্ছ, “সরল পথ”।"), ar="ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ"),
])

TEACH["s:verb"] = dict(pages=[
    P(("The first letter = who", "প্রথম অক্ষর = কে"),
      ("One verb, four people. Only the first letter changes.", "একটি ক্রিয়া, চারজন কর্তা। শুধু প্রথম অক্ষর বদলায়।"),
      ex=[X("أَقۡرَأُ", "I read", "আমি পড়ি"), X("نَقۡرَأُ", "we read", "আমরা পড়ি"), X("يَقۡرَأُ", "he reads", "সে পড়ে"), X("تَقۡرَأُ", "you read", "তুমি পড়ো")]),
    P(("The verb often comes first", "ক্রিয়া প্রায়ই আগে আসে"),
      ("Arabic often starts with the action, then says who: “goes my father”. Turn it around in English.",
       "আরবিতে প্রায়ই আগে কাজ, পরে কে: “যান আমার বাবা”। বাংলায় উল্টে নিন।"),
      ex=[X("يَذۡهَبُ أَبِي", "goes · my father = My father goes.", "যান · আমার বাবা = আমার বাবা যান।"),
          X("نَقۡرَأُ ٱلۡقُرۡءَانَ", "we read · the Quran = We read the Quran.", "আমরা পড়ি · কুরআন = আমরা কুরআন পড়ি।")]),
    P(("Object first = “only”", "কর্ম আগে = “কেবল”"),
      ("Normally “You” is joined to the end of the verb. Putting it in front adds “only”. That is why al-Fatiha says إِيَّاكَ نَعۡبُدُ.",
       "সাধারণত “তোমাকে” ক্রিয়ার শেষে জোড়া থাকে। সামনে আনলে “কেবল” অর্থ যোগ হয়। তাই ফাতিহায় إِيَّاكَ نَعۡبُدُ।"),
      vs=[X("نَعۡبُدُكَ", "We worship You.", "আমরা তোমার ইবাদত করি।"), X("إِيَّاكَ نَعۡبُدُ", "You ALONE we worship.", "কেবল তোমারই ইবাদত করি।")]),
], checks=[
    K(("تَقۡرَأُ means…", "تَقۡرَأُ অর্থ…"),
      [("you read", "তুমি পড়ো"), ("I read", "আমি পড়ি"), ("we read", "আমরা পড়ি"), ("he reads", "সে পড়ে")],
      ("تَـ at the start = you.", "শুরুতে تَـ = তুমি।"), ar="تَقۡرَأُ"),
    K(("Why does إِيَّاكَ come first in إِيَّاكَ نَعۡبُدُ?", "إِيَّاكَ نَعۡبُدُ-এ إِيَّاكَ কেন আগে?"),
      [("To say “You ALONE”", "“কেবল তোমাকেই” বলতে"), ("Arabic always puts “you” first", "আরবিতে “তুমি” সবসময় আগে বসে"),
       ("It is a question", "এটি প্রশ্ন"), ("It means “and”", "এর অর্থ “এবং”")],
      ("Putting the object in front adds “only”.", "কর্ম সামনে আনলে “কেবল” অর্থ যোগ হয়।")),
    K(("يَذۡهَبُ أَبِي means…", "يَذۡهَبُ أَبِي অর্থ…"),
      [("My father goes.", "আমার বাবা যান।"), ("I go to my father.", "আমি বাবার কাছে যাই।"), ("My father went.", "আমার বাবা গেলেন।"), ("We go with my father.", "আমরা বাবার সাথে যাই।")],
      ("Verb first: “goes · my father”.", "ক্রিয়া আগে: “যান · আমার বাবা”।"), ar="يَذۡهَبُ أَبِي"),
])

TEACH["s:inna"] = dict(pages=[
    P(("إِنَّ makes it certain", "إِنَّ নিশ্চিত করে"),
      ("Put إِنَّ in front of an “is” sentence to make it strong and certain: “Indeed, …”.",
       "“হয়” ধরনের বাক্যের সামনে إِنَّ বসালে বাক্য জোরালো ও নিশ্চিত হয়: “নিশ্চয়ই …”।"),
      ex=[X("إِنَّ ٱللَّهَ قَرِيبٌ", "Indeed, Allah is near.", "নিশ্চয়ই আল্লাহ কাছে।"), X("إِنَّ ٱلۡبَيۡتَ قَرِيبٌ", "Indeed, the house is near.", "নিশ্চয়ই ঘরটি কাছে।")]),
    P(("The next word ends in -a", "পরের শব্দ -আ দিয়ে শেষ"),
      ("The word right after إِنَّ changes its last vowel to -a. It is still the same word.",
       "إِنَّ-এর ঠিক পরের শব্দের শেষ স্বর -আ হয়ে যায়। শব্দ একই থাকে।"),
      vs=[X("ٱللَّهُ قَرِيبٌ", "Allah is near.", "আল্লাহ কাছে।"), X("إِنَّ ٱللَّهَ قَرِيبٌ", "Indeed, Allah is near.", "নিশ্চয়ই আল্লাহ কাছে।")]),
    P(("Even stronger: لَـ", "আরও জোর: لَـ"),
      ("Sometimes لَـ (surely) is added to the second part for extra force, as in Al-Asr.",
       "কখনো দ্বিতীয় অংশে لَـ (অবশ্যই) যোগ হয় আরও জোর দিতে, যেমন সূরা আসরে।"),
      ex=[X("إِنَّ ٱلۡإِنسَٰنَ لَفِي خُسۡرٍ", "Indeed, mankind is SURELY in loss.", "নিশ্চয়ই মানুষ অবশ্যই ক্ষতিতে।")]),
    P(("With “he”, “we”, “you”", "“তিনি”, “আমরা”, “তুমি” সহ"),
      ("The endings you know can join إِنَّ directly.", "আপনার চেনা শেষাংশগুলো সরাসরি إِنَّ-এর সাথে জোড়ে।"),
      ex=[X("إِنَّهُۥ", "indeed he / He", "নিশ্চয়ই তিনি"), X("إِنَّآ", "indeed We", "নিশ্চয়ই আমরা"), X("إِنَّكَ", "indeed you", "নিশ্চয়ই তুমি")]),
], checks=[
    K(("Why ٱللَّهَ, not ٱللَّهُ, in إِنَّ ٱللَّهَ قَرِيبٌ?", "إِنَّ ٱللَّهَ قَرِيبٌ-এ ٱللَّهُ নয়, ٱللَّهَ কেন?"),
      [("After إِنَّ the next word ends in -a", "إِنَّ-এর পরের শব্দ -আ দিয়ে শেষ হয়"), ("It means “of Allah”", "এর অর্থ “আল্লাহর”"),
       ("It is a command", "এটি আদেশ"), ("It means “a god”", "এর অর্থ “একজন ইলাহ”")],
      ("Same word, last vowel -a after إِنَّ.", "একই শব্দ, إِنَّ-এর পরে শেষ স্বর -আ।")),
    K(("إِنَّهُۥ means…", "إِنَّهُۥ অর্থ…"),
      [("indeed he", "নিশ্চয়ই তিনি"), ("indeed we", "নিশ্চয়ই আমরা"), ("his house", "তার ঘর"), ("and he", "এবং তিনি")],
      ("إِنَّ (indeed) + ـهُۥ (him).", "إِنَّ (নিশ্চয়ই) + ـهُۥ (তিনি)।"), ar="إِنَّهُۥ"),
])

TEACH["s:alladhina"] = dict(pages=[
    P(("One or many", "একজন নাকি অনেকে"),
      ("ٱلَّذِي is for one person, ٱلَّذِينَ for many.", "ٱلَّذِي একজনের জন্য, ٱلَّذِينَ অনেকের জন্য।"),
      vs=[X("ٱلَّذِي", "the one who", "যে (একজন)"), X("ٱلَّذِينَ", "those who", "যারা (অনেকে)")]),
    P(("Add a verb", "পরে ক্রিয়া বসান"),
      ("After it comes what they do or did.", "এর পরে আসে তারা কী করে বা করেছে।"),
      ex=[X("ٱلَّذِي يَقۡرَأُ ٱلۡقُرۡءَانَ", "the one who reads the Quran", "যে কুরআন পড়ে"), X("ٱلَّذِينَ ذَهَبُواْ", "those who went", "যারা গেল"),
          X("ٱلَّذِينَ ءَامَنُواْ", "those who believed", "যারা ঈমান এনেছে")]),
    P(("Describing a noun", "বিশেষ্যের বর্ণনা"),
      ("It can also tell you which people: “the path of those whom…”.", "কোন মানুষ তাও বলতে পারে: “তাদের পথ, যাদের…”।"),
      ex=[X("صِرَٰطَ ٱلَّذِينَ أَنۡعَمۡتَ عَلَيۡهِمۡ", "the path of those You have blessed", "তাদের পথ, যাদের তুমি নিয়ামত দিয়েছ")]),
    P(("Learn it as one phrase", "পুরোটা একসাথে শিখুন"),
      ("The Quran's most repeated description of good people. It appears in about 50 verses.",
       "কুরআনে ভালো মানুষের সবচেয়ে বেশি আসা বর্ণনা। প্রায় ৫০টি আয়াতে এসেছে।"),
      ex=[X("ٱلَّذِينَ ءَامَنُواْ وَعَمِلُواْ ٱلصَّٰلِحَٰتِ", "those who believe and do good deeds", "যারা ঈমান আনে ও সৎকাজ করে")]),
], checks=[
    K(("ٱلَّذِينَ ذَهَبُواْ means…", "ٱلَّذِينَ ذَهَبُواْ অর্থ…"),
      [("those who went", "যারা গেল"), ("the one who went", "যে গেল"), ("they go", "তারা যায়"), ("Who will go?", "কে যাবে?")],
      ("ٱلَّذِينَ = those who (many), ذَهَبُواْ = they went.", "ٱلَّذِينَ = যারা (অনেকে), ذَهَبُواْ = তারা গেল।"), ar="ٱلَّذِينَ ذَهَبُواْ"),
    K(("Which one means “the one who reads”?", "কোনটির অর্থ “যে পড়ে” (একজন)?"),
      ["ٱلَّذِي يَقۡرَأُ", "ٱلَّذِينَ يَقۡرَءُونَ", "نَقۡرَأُ", "يَقۡرَأُ"],
      ("ٱلَّذِي = the one who (one person). ٱلَّذِينَ يَقۡرَءُونَ = those who read.", "ٱلَّذِي = যে (একজন)। ٱلَّذِينَ يَقۡرَءُونَ = যারা পড়ে।")),
])

# Where the two new ideas are taught (lesson id -> patterns put first in that lesson)
PLACE = {"u1-s-is-1": ["un"], "u1-s-of": ["endings"]}
# patterns moved to a lighter lesson of the same unit (so no lesson teaches too much at once)
MOVE = {"doer": "u1-s-of"}

# =====================================================================================
# "Grammar in action" questions: show a real Quran word and ask what its piece tells you.
# Each group lists the pieces that compete with each other; the options are what each piece means.
# `others` are fixed options for forms that have no piece of their own (e.g. "he" in the past tense).
# =====================================================================================
RULES = {
    "owner": dict(q_en="Whose? Look at the ending.", q_bn="কার? শেষটা দেখুন।",
                  opts={"i": ("my / me", "আমার / আমাকে"), "ka": ("your (one person)", "তোমার (একজন)"),
                        "kum": ("your (many people)", "তোমাদের (অনেকে)"), "hu": ("his / him", "তার / তাকে"),
                        "huma": ("of the two of them", "তাদের দুজনের"), "hum": ("their / them", "তাদের"), "na": ("our / us", "আমাদের")},
                  others={}),
    "now": dict(q_en="Who does it? Look at the first letter.", q_bn="কে করে? প্রথম অক্ষর দেখুন।",
                opts={"i_do": ("I", "আমি"), "we_do": ("we", "আমরা"), "ya": ("he / they", "সে / তারা")},
                others={"you": ("you", "তুমি")}),
    "past": dict(q_en="Who did it? Look at the ending.", q_bn="কে করেছে? শেষটা দেখুন।",
                 opts={"you_did": ("you", "তুমি"), "we_did": ("we", "আমরা"), "they_did": ("they", "তারা")},
                 others={"he": ("he (no ending)", "সে (শেষে কিছু নেই)")}),
    "the_a": dict(q_en="“a …” or “the …”?", q_bn="“একটি …” নাকি নির্দিষ্ট “…টি”?",
                  opts={"al": ("the …", "…টি (নির্দিষ্ট)"), "un": ("a …", "একটি …")}, others={}),
    "shape": dict(q_en="What does the shape tell you?", q_bn="ছাঁচটি কী বলে?",
                  opts={"doer": ("the one who does it", "যে কাজটি করে"), "done_to": ("the one it is done to", "যার প্রতি কাজটি করা হয়")},
                  others={"act": ("the action itself", "কাজটি নিজেই")}),
    "joined": dict(q_en="What does the little letter at the front add?", q_bn="সামনের ছোট অক্ষরটি কী যোগ করে?",
                   opts={"wa": ("and", "এবং"), "bi": ("in / with / by", "-এ / দিয়ে"), "li": ("for / belongs to", "জন্য / -এর"), "fa": ("so / then", "তাই / তারপর")},
                   others={}),
}

# =====================================================================================
# Sentence patterns for Units 3–14
# =====================================================================================
TEACH["s:call"] = dict(pages=[
    P(("Put يَا before the name", "নামের আগে يَا"),
      ("To call someone, say يَا and then who you are calling. It works like “O …!” or simply saying their name out loud.",
       "কাউকে ডাকতে يَا বলে তারপর যাকে ডাকছেন তাকে বলুন। এটি “হে …!” বা নাম ধরে ডাকার মতো।"),
      ex=[X("يَا أَبِي", "O my father!", "হে আমার বাবা!"), X("يَا أُمِّي", "O my mother!", "হে আমার মা!"), X("يَا رَبِّ", "O my Lord!", "হে আমার রব!")]),
    P(("Calling Allah: يَا is usually silent", "আল্লাহকে ডাকা: يَا সাধারণত থাকে না"),
      ("In duas, يَا is usually left out. You just start with رَبِّ or رَبَّنَا, and it still means “O my Lord” / “O our Lord”. ٱللَّهُمَّ means “O Allah”: the مَّ at the end does the job of يَا.",
       "দোয়ায় সাধারণত يَا বাদ যায়। শুধু رَبِّ বা رَبَّنَا দিয়ে শুরু, তবু অর্থ “হে আমার রব” / “হে আমাদের রব”। ٱللَّهُمَّ মানে “হে আল্লাহ”: শেষের مَّ يَا-এর কাজ করে।"),
      ex=[X("رَبِّ ٱغۡفِرۡ لِي", "(O) my Lord, forgive me", "(হে) আমার রব, আমাকে ক্ষমা করো"),
          X("رَبَّنَا وَلَكَ ٱلۡحَمۡدُ", "(O) our Lord, and to You is all praise", "(হে) আমাদের রব, সব প্রশংসা তোমারই"),
          X("ٱللَّهُمَّ", "O Allah", "হে আল্লাহ")]),
    P(("Before ٱلۡـ: يَٰٓأَيُّهَا", "ٱلۡـ-এর আগে: يَٰٓأَيُّهَا"),
      ("When the one you call has ٱلۡـ, the Quran says يَٰٓأَيُّهَا. Watch for it: it tells you who the next verses speak to.",
       "যাকে ডাকা হচ্ছে তাতে ٱلۡـ থাকলে কুরআন বলে يَٰٓأَيُّهَا। খেয়াল রাখুন: এটি বলে দেয় পরের আয়াতগুলো কাদের উদ্দেশে।"),
      ex=[X("يَٰٓأَيُّهَا ٱلنَّاسُ", "O mankind!", "হে মানুষ!"), X("يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُواْ", "O you who believe! (89 times)", "হে মুমিনগণ! (৮৯ বার)"),
          X("أَيُّهَا ٱلنَّبِيُّ", "O Prophet (in the tashahhud)", "হে নবী (তাশাহহুদে)")]),
], checks=[
    K(("How do you call your father?", "বাবাকে কীভাবে ডাকবেন?"),
      ["يَا أَبِي", "هُوَ أَبِي", "بَيۡتُ أَبِي", "لِأَبِي"],
      ("يَا + the one you call. هُوَ أَبِي = He is my father.", "يَا + যাকে ডাকছেন। هُوَ أَبِي = তিনি আমার বাবা।")),
    K(("رَبِّ ٱغۡفِرۡ لِي — where is the “O”?", "رَبِّ ٱغۡفِرۡ لِي — “হে” কোথায়?"),
      [("Left out: with Allah, يَا is usually silent", "বাদ গেছে: আল্লাহকে ডাকতে يَا সাধারণত থাকে না"), ("in ٱغۡفِرۡ", "ٱغۡفِرۡ-এ"),
       ("in لِي", "لِي-তে"), ("There is no calling here", "এখানে ডাকা নেই")],
      ("رَبِّ alone already means “O my Lord”.", "শুধু رَبِّ-ই মানে “হে আমার রব”।")),
])

TEACH["s:no"] = dict(pages=[
    P(("لَا = not (now)", "لَا = না (এখন)"),
      ("Put لَا before a present verb: “does not / do not”.", "বর্তমান ক্রিয়ার আগে لَا বসালে: “করে না”।"),
      ex=[X("لَا أَعۡلَمُ", "I do not know", "আমি জানি না"), X("لَا نَعۡلَمُ", "we do not know", "আমরা জানি না"),
          X("لَآ أَعۡبُدُ مَا تَعۡبُدُونَ", "I do not worship what you worship (109:2)", "তোমরা যার ইবাদত করো আমি তার ইবাদত করি না (১০৯:২)")]),
    P(("لَمۡ = did not (past)", "لَمۡ = করেনি (অতীত)"),
      ("Strange but true: after لَمۡ you use the present form, and it means the past.", "আশ্চর্য হলেও সত্য: لَمۡ-এর পরে বর্তমান রূপ বসে, কিন্তু অর্থ হয় অতীত।"),
      vs=[X("ذَهَبَ", "he went", "সে গেল"), X("لَمۡ يَذۡهَبۡ", "he did not go", "সে যায়নি")]),
    P(("After لَمۡ the verb ends in a sukun", "لَمۡ-এর পরে ক্রিয়ার শেষে সুকুন"),
      ("The verb loses its last -u and ends in a sukun. That is how you can spot it.", "ক্রিয়ার শেষের -উ চলে গিয়ে সুকুন বসে। এভাবেই চেনা যায়।"),
      vs=[X("يَعۡلَمُ", "he knows", "সে জানে"), X("لَمۡ يَعۡلَمۡ", "he did not know", "সে জানত না")],
      ex=[X("لَمۡ يَلِدۡ وَلَمۡ يُولَدۡ", "He did not beget, nor was He born (112:3)", "তিনি জন্ম দেননি, জন্ম নেননি (১১২:৩)"),
          X("عَلَّمَ ٱلۡإِنسَٰنَ مَا لَمۡ يَعۡلَمۡ", "He taught man what he did not know (96:5)", "তিনি মানুষকে শিখিয়েছেন যা সে জানত না (৯৬:৫)")]),
], checks=[
    K(("لَمۡ يَذۡهَبۡ means…", "لَمۡ يَذۡهَبۡ অর্থ…"),
      [("He did not go.", "সে যায়নি।"), ("He does not go.", "সে যায় না।"), ("He went.", "সে গেল।"), ("Don't go!", "যেয়ো না!")],
      ("لَمۡ + verb = did not.", "لَمۡ + ক্রিয়া = করেনি।"), ar="لَمۡ يَذۡهَبۡ"),
    K(("Which one means “I don't know”?", "কোনটির অর্থ “আমি জানি না”?"),
      ["لَا أَعۡلَمُ", "لَمۡ أَعۡلَمۡ", "أَعۡلَمُ", "لَا نَعۡلَمُ"],
      ("لَا + present = not now. لَمۡ أَعۡلَمۡ = I did not know, لَا نَعۡلَمُ = we don't know.", "لَا + বর্তমান = এখন না। لَمۡ أَعۡلَمۡ = আমি জানতাম না, لَا نَعۡلَمُ = আমরা জানি না।")),
])

TEACH["s:only"] = dict(pages=[
    P(("لَا + a noun = none at all", "لَا + বিশেষ্য = একদমই নেই"),
      ("لَا before a noun means “there is no … at all”. The noun ends in -a, with no doubled vowel.", "বিশেষ্যের আগে لَا মানে “কোনো … নেই”। বিশেষ্য -আ দিয়ে শেষ হয়, দ্বিগুণ স্বর থাকে না।"),
      ex=[X("لَا رَيۡبَ فِيهِ", "no doubt (at all) in it (2:2)", "এতে কোনো সন্দেহ নেই (২:২)"), X("لَا كِتَابَ فِي ٱلۡبَيۡتِ", "There is no book in the house.", "ঘরে কোনো বই নেই।")]),
    P(("Add إِلَّا: “only”", "إِلَّا যোগ: “কেবল”"),
      ("First say “none”, then make one exception. This is the strongest way to say “only”.", "প্রথমে বলুন “কেউ নেই”, তারপর একটি ব্যতিক্রম। “কেবল” বলার সবচেয়ে জোরালো উপায়।"),
      vs=[X("لَآ إِلَٰهَ", "no god", "কোনো ইলাহ নেই"), X("لَآ إِلَٰهَ إِلَّا ٱللَّهُ", "no god except Allah", "আল্লাহ ছাড়া কোনো ইলাহ নেই")]),
    P(("With verbs too", "ক্রিয়ার সাথেও"),
      ("لَا + verb + إِلَّا = do nothing but …", "لَا + ক্রিয়া + إِلَّا = … ছাড়া কিছু করি না"),
      ex=[X("لَا نَعۡبُدُ إِلَّا ٱللَّهَ", "We worship none but Allah.", "আমরা আল্লাহ ছাড়া কারও ইবাদত করি না।"),
          X("لَا يُكَلِّفُ ٱللَّهُ نَفۡسًا إِلَّا وُسۡعَهَا", "Allah does not burden a soul except with what it can bear (2:286)", "আল্লাহ কাউকে সাধ্যের বাইরে দায়িত্ব দেন না (২:২৮৬)")]),
    P(("The words of the shahada", "কালিমার শব্দ"),
      ("Every Muslim's testimony is built on this pattern: first deny (لَآ إِلَٰهَ), then affirm (إِلَّا ٱللَّهُ).",
       "প্রতিটি মুসলিমের সাক্ষ্য এই গঠনে: আগে অস্বীকার (لَآ إِلَٰهَ), তারপর স্বীকার (إِلَّا ٱللَّهُ)।"),
      ex=[X("لَآ إِلَٰهَ إِلَّا هُوَ", "there is no god except Him (2:255)", "তিনি ছাড়া কোনো ইলাহ নেই (২:২৫৫)")]),
], checks=[
    K(("لَآ إِلَٰهَ إِلَّا ٱللَّهُ, word for word:", "لَآ إِلَٰهَ إِلَّا ٱللَّهُ, শব্দে শব্দে:"),
      [("no · god · except · Allah", "নেই · ইলাহ · ছাড়া · আল্লাহ"), ("Allah · is not · a god", "আল্লাহ · নন · ইলাহ"),
       ("there is · a god · Allah", "আছেন · ইলাহ · আল্লাহ"), ("no · god · and · Allah", "নেই · ইলাহ · এবং · আল্লাহ")],
      ("لَا (no) + إِلَٰهَ (god) + إِلَّا (except) + ٱللَّهُ.", "لَا (নেই) + إِلَٰهَ (ইলাহ) + إِلَّا (ছাড়া) + ٱللَّهُ।")),
    K(("لَا نَعۡبُدُ إِلَّا ٱللَّهَ means…", "لَا نَعۡبُدُ إِلَّا ٱللَّهَ অর্থ…"),
      [("We worship only Allah.", "আমরা কেবল আল্লাহর ইবাদত করি।"), ("We do not worship Allah.", "আমরা আল্লাহর ইবাদত করি না।"),
       ("Allah does not worship.", "আল্লাহ ইবাদত করেন না।"), ("We worship Allah and others.", "আমরা আল্লাহ ও অন্যদের ইবাদত করি।")],
      ("“None but Allah” = only Allah.", "“আল্লাহ ছাড়া কেউ নয়” = কেবল আল্লাহ।"), ar="لَا نَعۡبُدُ إِلَّا ٱللَّهَ"),
])

TEACH["s:when"] = dict(pages=[
    P(("إِذَا + a past verb = “when”", "إِذَا + অতীত ক্রিয়া = “যখন”"),
      ("After إِذَا the verb is in the past form, but the meaning is “when it happens”. English uses the present here.",
       "إِذَا-এর পরে ক্রিয়া অতীত রূপে থাকে, কিন্তু অর্থ “যখন ঘটে”।"),
      ex=[X("إِذَا جَآءَ نَصۡرُ ٱللَّهِ", "When the help of Allah comes (110:1)", "যখন আল্লাহর সাহায্য আসে (১১০:১)"),
          X("إِذَا زُلۡزِلَتِ ٱلۡأَرۡضُ", "When the earth is shaken (99:1)", "যখন পৃথিবী প্রকম্পিত হবে (৯৯:১)")]),
    P(("Then: فَـ", "তখন: فَـ"),
      ("The second half says what to do then. It often starts with فَـ (so, then).", "দ্বিতীয় অংশ বলে তখন কী করতে হবে। প্রায়ই فَـ (তাই, তখন) দিয়ে শুরু হয়।"),
      ex=[X("إِذَا دَخَلۡتَ ٱلۡمَسۡجِدَ فَصَلِّ", "When you enter the mosque, (then) pray.", "মসজিদে প্রবেশ করলে (তখন) নামাজ পড়ো।"),
          X("فَإِذَا قَرَأۡتَ ٱلۡقُرۡءَانَ فَٱسۡتَعِذۡ بِٱللَّهِ", "When you recite the Quran, seek refuge in Allah (16:98)", "যখন কুরআন পড়বে, আল্লাহর আশ্রয় চাও (১৬:৯৮)")]),
    P(("إِذَا and إِنۡ", "إِذَا ও إِنۡ"),
      ("إِذَا is “when”: it will happen. إِنۡ is “if”: it may or may not happen.", "إِذَا মানে “যখন”: এটি ঘটবেই। إِنۡ মানে “যদি”: ঘটতেও পারে, নাও পারে।"),
      vs=[X("إِذَا", "when (sure)", "যখন (নিশ্চিত)"), X("إِنۡ", "if (maybe)", "যদি (হয়তো)")],
      ex=[X("وَإِن لَّمۡ تَغۡفِرۡ لَنَا", "and if You do not forgive us (7:23)", "আর যদি তুমি আমাদের ক্ষমা না করো (৭:২৩)")]),
], checks=[
    K(("إِذَا جَآءَ أَبِي means…", "إِذَا جَآءَ أَبِي অর্থ…"),
      [("When my father comes", "যখন বাবা আসেন"), ("My father came.", "বাবা এসেছিলেন।"), ("If my father", "যদি বাবা"), ("My father will not come.", "বাবা আসবেন না।")],
      ("إِذَا + past verb = when it happens.", "إِذَا + অতীত ক্রিয়া = যখন ঘটে।"), ar="إِذَا جَآءَ أَبِي"),
    K(("In إِذَا دَخَلۡتَ ٱلۡمَسۡجِدَ فَصَلِّ, what does فَـ do?", "إِذَا دَخَلۡتَ ٱلۡمَسۡجِدَ فَصَلِّ-এ فَـ কী করে?"),
      [("It starts what to do then: “(then) pray”", "তখন কী করতে হবে তা শুরু করে: “(তখন) নামাজ পড়ো”"), ("It means “and”", "এর অর্থ “এবং”"),
       ("It means “in”", "এর অর্থ “-এ”"), ("It means “not”", "এর অর্থ “না”")],
      ("فَـ = so, then: it opens the second half.", "فَـ = তাই, তখন: দ্বিতীয় অংশ শুরু করে।")),
])

TEACH["s:place"] = dict(pages=[
    P(("Four little place words", "চারটি ছোট স্থানবাচক শব্দ"),
      ("These four come up in almost every page of the Quran.", "কুরআনের প্রায় প্রতিটি পৃষ্ঠায় এই চারটি আসে।"),
      ex=[X("فِي", "in", "-এ, মধ্যে"), X("مِنۡ", "from, of", "থেকে"), X("عَلَى", "on, upon", "উপরে"), X("إِلَى", "to, towards", "দিকে")]),
    P(("Where is it? (no “is”)", "কোথায়? (“আছে” লাগে না)"),
      ("Like the invisible “is”: say the thing, then the place word and the place.", "লুকানো “আছে”-র মতোই: জিনিসটি বলুন, তারপর স্থানবাচক শব্দ ও স্থান।"),
      ex=[X("أَبِي فِي ٱلۡبَيۡتِ", "My father (is) in the house.", "আমার বাবা ঘরে (আছেন)।"), X("ٱلۡقَلَمُ عَلَى ٱلۡكِتَابِ", "The pen (is) on the book.", "কলমটি বইয়ের উপর।"),
          X("ٱلسَّلَٰمُ عَلَيۡكُمۡ", "Peace (be) upon you.", "তোমাদের উপর শান্তি।")]),
    P(("The next word ends in -i", "পরের শব্দ -ই দিয়ে শেষ"),
      ("The noun after a place word takes -i at the end. Same word, new ending.", "স্থানবাচক শব্দের পরের বিশেষ্য শেষে -ই নেয়। একই শব্দ, নতুন শেষ।"),
      vs=[X("ٱلۡبَيۡتُ", "the house", "ঘরটি"), X("فِي ٱلۡبَيۡتِ", "in the house", "ঘরে")],
      ex=[X("فِي سَبِيلِ ٱللَّهِ", "in the way of Allah", "আল্লাহর পথে")]),
    P(("With “me, you, him…”", "“আমি, তুমি, সে…” সহ"),
      ("The endings you know join them directly.", "আপনার চেনা শেষাংশগুলো সরাসরি জোড়ে।"),
      ex=[X("عَلَيۡكَ", "upon you", "তোমার উপর"), X("فِيهِ", "in it", "এতে"), X("مِنۡهُ", "from him / it", "তার থেকে"), X("إِلَيۡكَ", "to you", "তোমার দিকে")]),
], checks=[
    K(("أَبِي فِي ٱلۡبَيۡتِ means…", "أَبِي فِي ٱلۡبَيۡتِ অর্থ…"),
      [("My father is in the house.", "আমার বাবা ঘরে আছেন।"), ("my father's house", "আমার বাবার ঘর"), ("My father went home.", "বাবা বাড়ি গেলেন।"), ("The house is my father's.", "ঘরটি বাবার।")],
      ("thing + فِي (in) + place. No “is” needed.", "জিনিস + فِي (-এ) + স্থান। “আছে” লাগে না।"), ar="أَبِي فِي ٱلۡبَيۡتِ"),
    K(("Which little word means “from”?", "কোন ছোট শব্দের অর্থ “থেকে”?"),
      ["مِنۡ", "فِي", "عَلَى", "إِلَى"],
      ("مِنۡ = from. فِي = in, عَلَى = on, إِلَى = to.", "مِنۡ = থেকে। فِي = -এ, عَلَى = উপরে, إِلَى = দিকে।")),
])

TEACH["s:ask"] = dict(pages=[
    P(("Three parts of a dua", "দোয়ার তিন অংশ"),
      ("Call Allah, ask with the command form, say for whom.", "আল্লাহকে ডাকুন, আদেশ-রূপে চান, কার জন্য তা বলুন।"),
      ex=[X("رَبِّ", "1. call: My Lord", "১. ডাকা: হে আমার রব"), X("زِدۡنِي", "2. ask: increase me", "২. চাওয়া: আমাকে বাড়িয়ে দাও"),
          X("عِلۡمًا", "3. in what: in knowledge", "৩. কীসে: জ্ঞানে")]),
    P(("For whom?", "কার জন্য?"),
      ("ـنِي / ـنَا join the request; لِي / لَنَا come after it.", "ـنِي / ـنَا চাওয়ার সাথে জোড়ে; لِي / لَنَا পরে আসে।"),
      ex=[X("رَبِّ ٱهۡدِنِي", "My Lord, guide me.", "হে আমার রব, আমাকে পথ দেখাও।"), X("رَبَّنَا ٱرۡحَمۡنَا", "Our Lord, have mercy on us.", "হে আমাদের রব, আমাদের দয়া করো।"),
          X("رَبِّ ٱغۡفِرۡ لِي وَلِوَٰلِدَيَّ", "My Lord, forgive me and my parents (71:28)", "হে আমার রব, আমাকে ও আমার বাবা-মাকে ক্ষমা করো (৭১:২৮)")]),
    P(("Duas of the prophets", "নবীদের দোয়া"),
      ("Musa's dua before facing Pharaoh. Now you can see every part.", "ফেরাউনের সামনে যাওয়ার আগে মুসার দোয়া। এখন প্রতিটি অংশ চেনা যায়।"),
      ex=[X("رَبِّ ٱشۡرَحۡ لِي صَدۡرِي", "My Lord, open my chest for me (20:25)", "হে আমার রব, আমার বুক প্রশস্ত করে দাও (২০:২৫)"),
          X("وَيَسِّرۡ لِيٓ أَمۡرِي", "and make my task easy for me (20:26)", "আর আমার কাজ সহজ করে দাও (২০:২৬)")]),
    P(("Don't …! لَا + verb", "… কোরো না! لَا + ক্রিয়া"),
      ("To ask someone not to do something: لَا + the “you” verb, ending in a sukun.", "কাউকে কিছু না করতে বলতে: لَا + “তুমি”-র ক্রিয়া, শেষে সুকুন।"),
      ex=[X("لَا تَذۡهَبۡ", "Don't go!", "যেয়ো না!"), X("لَا تَحۡزَنۡ إِنَّ ٱللَّهَ مَعَنَا", "Do not grieve; indeed Allah is with us (9:40)", "চিন্তা কোরো না, নিশ্চয়ই আল্লাহ আমাদের সাথে আছেন (৯:৪০)")]),
], checks=[
    K(("رَبِّ ٱهۡدِنِي means…", "رَبِّ ٱهۡدِنِي অর্থ…"),
      [("My Lord, guide me.", "হে আমার রব, আমাকে পথ দেখাও।"), ("My Lord guided me.", "আমার রব আমাকে পথ দেখিয়েছেন।"),
       ("My Lord, guide us.", "হে আমার রব, আমাদের পথ দেখাও।"), ("My guide is my Lord.", "আমার পথপ্রদর্শক আমার রব।")],
      ("call (رَبِّ) + request (ٱهۡدِ) + me (ـنِي).", "ডাকা (رَبِّ) + চাওয়া (ٱهۡدِ) + আমাকে (ـنِي)।"), ar="رَبِّ ٱهۡدِنِي"),
    K(("Which one is “Our Lord, forgive us”?", "কোনটি “হে আমাদের রব, আমাদের ক্ষমা করো”?"),
      ["رَبَّنَا ٱغۡفِرۡ لَنَا", "رَبِّ ٱغۡفِرۡ لِي", "رَبُّنَا غَفُورٌ", "رَبَّنَا وَلَكَ ٱلۡحَمۡدُ"],
      ("رَبَّنَا (our Lord) + ٱغۡفِرۡ (forgive) + لَنَا (us).", "رَبَّنَا (আমাদের রব) + ٱغۡفِرۡ (ক্ষমা করো) + لَنَا (আমাদের)।")),
])

TEACH["s:have"] = dict(pages=[
    P(("No verb “to have”", "“আছে” ক্রিয়া নেই"),
      ("Arabic says “to me (is) a house”. لِـ + the owner, then what they have.", "আরবিতে বলা হয় “আমার জন্য (আছে) একটি ঘর”। لِـ + মালিক, তারপর যা আছে।"),
      ex=[X("لِي بَيۡتٌ", "I have a house.", "আমার একটি ঘর আছে।"), X("لِأَبِي كِتَابٌ", "My father has a book.", "আমার বাবার একটি বই আছে।"),
          X("لَنَا رَبٌّ رَحِيمٌ", "We have a merciful Lord.", "আমাদের একজন দয়ালু রব আছেন।")]),
    P(("عِندَ = with, at", "عِندَ = কাছে"),
      ("عِندِي (with me) is the everyday way to say “I have (on me)”.", "عِندِي (আমার কাছে) দিয়ে প্রতিদিনের “আমার কাছে আছে” বলা হয়।"),
      ex=[X("عِندِي قَلَمٌ جَدِيدٌ", "I have a new pen.", "আমার কাছে একটি নতুন কলম আছে।"), X("عِندَهُۥ", "with Him", "তাঁর কাছে")]),
    P(("To Him belongs everything", "সবকিছু তাঁরই"),
      ("The same pattern says that everything belongs to Allah.", "একই গঠনে বলা হয়, সবকিছু আল্লাহর।"),
      ex=[X("لَّهُۥ مَا فِي ٱلسَّمَٰوَٰتِ وَمَا فِي ٱلۡأَرۡضِ", "To Him belongs whatever is in the heavens and the earth (2:255)", "আকাশ ও পৃথিবীতে যা আছে সব তাঁরই (২:২৫৫)"),
          X("لَكُمۡ دِينُكُمۡ وَلِيَ دِينِ", "For you is your religion, and for me is mine (109:6)", "তোমাদের দ্বীন তোমাদের, আমার দ্বীন আমার (১০৯:৬)")]),
], checks=[
    K(("عِندِي قَلَمٌ means…", "عِندِي قَلَمٌ অর্থ…"),
      [("I have a pen.", "আমার কাছে একটি কলম আছে।"), ("This is my pen.", "এটি আমার কলম।"), ("I am a pen.", "আমি একটি কলম।"), ("I write with a pen.", "আমি কলম দিয়ে লিখি।")],
      ("عِندِي = with me → I have.", "عِندِي = আমার কাছে → আমার আছে।"), ar="عِندِي قَلَمٌ"),
    K(("How do you say “I have a house”?", "“আমার একটি ঘর আছে” কোনটি?"),
      ["لِي بَيۡتٌ", "بَيۡتِي", "هَٰذَا بَيۡتٌ", "فِي ٱلۡبَيۡتِ"],
      ("لِي (to me) + بَيۡتٌ (a house). بَيۡتِي = my house (just the phrase).", "لِي (আমার) + بَيۡتٌ (একটি ঘর)। بَيۡتِي = আমার ঘর (শুধু শব্দগুচ্ছ)।")),
])

TEACH["s:question"] = dict(pages=[
    P(("Four question words", "চারটি প্রশ্নবোধক শব্দ"),
      ("Put one at the start. The rest is a normal sentence.", "শুরুতে একটি বসান। বাকিটা সাধারণ বাক্য।"),
      ex=[X("مَا", "what?", "কী?"), X("مَنۡ", "who?", "কে?"), X("أَيۡنَ", "where?", "কোথায়?"), X("هَلۡ", "is it…? did…? (yes / no)", "কি? (হ্যাঁ / না)")]),
    P(("Everyday questions", "প্রতিদিনের প্রশ্ন"),
      ("Notice: still no “is”.", "খেয়াল করুন: এখনও “হয়/আছে” লাগে না।"),
      ex=[X("مَا هَٰذَا", "What (is) this?", "এটি কী?"), X("مَنۡ هَٰذَا", "Who (is) this?", "এ কে?"), X("أَيۡنَ ٱلۡمَسۡجِدُ", "Where (is) the mosque?", "মসজিদ কোথায়?"),
          X("هَلۡ ذَهَبَ أَبِي إِلَى ٱلۡمَسۡجِدِ", "Did my father go to the mosque?", "বাবা কি মসজিদে গেছেন?")]),
    P(("Questions in the Quran", "কুরআনের প্রশ্ন"),
      ("The Quran often asks questions to make us think.", "কুরআন প্রায়ই প্রশ্ন করে আমাদের ভাবায়।"),
      ex=[X("فَأَيۡنَ تَذۡهَبُونَ", "So where are you going? (81:26)", "তবে তোমরা কোথায় যাচ্ছ? (৮১:২৬)"),
          X("هَلۡ أَتَىٰكَ حَدِيثُ ٱلۡغَٰشِيَةِ", "Has the story of the Overwhelming come to you? (88:1)", "তোমার কাছে কি আচ্ছন্নকারীর খবর এসেছে? (৮৮:১)"),
          X("مَن ذَا ٱلَّذِي يَشۡفَعُ عِندَهُۥٓ", "Who is it that can intercede with Him? (2:255)", "কে আছে যে তাঁর কাছে সুপারিশ করবে? (২:২৫৫)")]),
], checks=[
    K(("مَا هَٰذَا means…", "مَا هَٰذَا অর্থ…"),
      [("What is this?", "এটি কী?"), ("Who is this?", "এ কে?"), ("Where is this?", "এটি কোথায়?"), ("This is what.", "এটি যা।")],
      ("مَا = what.", "مَا = কী।"), ar="مَا هَٰذَا"),
    K(("Which one asks “Where is the mosque?”", "কোনটি জিজ্ঞেস করে “মসজিদ কোথায়?”"),
      ["أَيۡنَ ٱلۡمَسۡجِدُ", "مَا ٱلۡمَسۡجِدُ", "مَنۡ فِي ٱلۡمَسۡجِدِ", "هَٰذَا ٱلۡمَسۡجِدُ"],
      ("أَيۡنَ = where.", "أَيۡنَ = কোথায়।")),
])
