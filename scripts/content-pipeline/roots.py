# -*- coding: utf-8 -*-
"""Root letters: the core idea of each root, and how the words built on it connect.

ROOTS[root] = (idea_en, idea_bn, story_en, story_bn)
  idea  = the root's core meaning in a few words
  story = one or two sentences linking the family members' meanings back to that idea
"""

ROOTS = {}


def R(root, idea, story):
    ROOTS[root] = (idea[0], idea[1], story[0], story[1])


R("سمو", ("being high, raised", "উঁচু হওয়া, উপরে ওঠা"),
  ("سَمَآءٌ (sky) is what is high above us. ٱسۡمٌ (a name) raises a thing up so it can be known. سَمَّىٰ means to give a name.",
   "سَمَآءٌ (আকাশ) হলো যা আমাদের উপরে উঁচুতে। ٱسۡمٌ (নাম) কোনো কিছুকে তুলে ধরে, যেন তাকে চেনা যায়। سَمَّىٰ মানে নাম রাখা।"))
R("أله", ("the one who is worshipped", "যার ইবাদত করা হয়"),
  ("إِلَٰهٌ is anything that is worshipped. ٱللَّهُ is the One true God, linked to al-ilāh, “THE God”. ٱللَّهُمَّ means “O Allah”.",
   "إِلَٰهٌ মানে যার ইবাদত করা হয়। ٱللَّهُ হলেন একমাত্র সত্য ইলাহ, “আল-ইলাহ” (সেই ইলাহ) থেকে। ٱللَّهُمَّ মানে “হে আল্লাহ”।"))
R("رحم", ("tender mercy; the womb", "কোমল দয়া; মাতৃগর্ভ"),
  ("The same letters give رَحِمٌ, the womb (plural أَرۡحَامٌ), where a mother's care surrounds her child. رَحۡمَةٌ is mercy, رَحِمَ is to show mercy, ٱلرَّحۡمَٰنُ is mercy that covers everyone, رَحِيمٌ is mercy that keeps on giving.",
   "একই অক্ষরে رَحِمٌ মানে মাতৃগর্ভ (বহুবচন أَرۡحَامٌ), যেখানে মায়ের মমতা সন্তানকে ঘিরে রাখে। رَحۡمَةٌ দয়া, رَحِمَ দয়া করা, ٱلرَّحۡمَٰنُ সবার প্রতি ব্যাপক দয়া, رَحِيمٌ যে দয়া অবিরাম দেয়।"))
R("حمد", ("praise", "প্রশংসা"),
  ("حَمۡدٌ is praise, حَمِيدٌ is praiseworthy, مَحۡمُودٌ is praised. The names مُحَمَّدٌ (praised again and again) and أَحۡمَدُ (most praised) come from it too.",
   "حَمۡدٌ প্রশংসা, حَمِيدٌ প্রশংসার যোগ্য, مَحۡمُودٌ প্রশংসিত। নাম مُحَمَّدٌ (বারবার প্রশংসিত) ও أَحۡمَدُ (সর্বাধিক প্রশংসিত) এখান থেকেই।"))
R("ربب", ("raising, owning and caring for", "লালন, মালিকানা ও যত্ন"),
  ("رَبٌّ is the one who owns something and raises it step by step, taking care of it. A رَبَّانِيٌّ is a person devoted to the Lord.",
   "رَبٌّ হলেন যিনি মালিক, যিনি ধাপে ধাপে লালন করেন ও যত্ন নেন। رَبَّانِيٌّ হলো রবের প্রতি নিবেদিত মানুষ।"))
R("علم", ("knowing; a sign", "জানা; চিহ্ন"),
  ("عِلۡمٌ is knowledge, عَلِمَ is to know, عَلِيمٌ is the All-Knowing, عَلَّمَ is to teach (make someone know). عَالَمٌ (a world) is everything that is a sign of its Creator.",
   "عِلۡمٌ জ্ঞান, عَلِمَ জানা, عَلِيمٌ সর্বজ্ঞ, عَلَّمَ শেখানো (কাউকে জানানো)। عَالَمٌ (জগত) হলো যা কিছু তার স্রষ্টার চিহ্ন বহন করে।"))
R("ملك", ("owning, having power", "মালিকানা, ক্ষমতা"),
  ("مَٰلِكٌ is an owner, مَلِكٌ a king, مُلۡكٌ a kingdom, مَلَكَ to own, مَمۡلُوكٌ something owned.",
   "مَٰلِكٌ মালিক, مَلِكٌ রাজা, مُلۡكٌ রাজত্ব, مَلَكَ মালিক হওয়া, مَمۡلُوكٌ যার মালিক অন্য কেউ।"))
R("دين", ("what is owed and paid back", "যা পাওনা ও যার প্রতিদান দেওয়া হয়"),
  ("دَيۡنٌ is a debt. دِينٌ is the way of life we owe to Allah, and يَوۡمُ ٱلدِّينِ is the Day when everyone is repaid.",
   "دَيۡنٌ মানে ঋণ। دِينٌ হলো আল্লাহর প্রতি আমাদের ঋণী জীবনব্যবস্থা, আর يَوۡمُ ٱلدِّينِ সেই দিন যেদিন সবাই প্রতিদান পাবে।"))
R("بيت", ("spending the night", "রাত কাটানো"),
  ("A بَيۡتٌ (house) is where you spend the night. يَبِيتُ is to spend the night, and بَيَٰتًا means “by night”.",
   "بَيۡتٌ (ঘর) হলো যেখানে রাত কাটানো হয়। يَبِيتُ মানে রাত কাটানো, بَيَٰتًا মানে “রাতে”।"))
R("كتب", ("writing; writing down as a rule", "লেখা; বিধান হিসেবে লিখে দেওয়া"),
  ("كَتَبَ is to write, كِتَابٌ is something written (a book), كَاتِبٌ is a writer, مَكۡتُوبٌ is written. “Written” also means prescribed: كُتِبَ عَلَيۡكُمُ ٱلصِّيَامُ, fasting is written (prescribed) for you.",
   "كَتَبَ লেখা, كِتَابٌ যা লেখা হয়েছে (বই), كَاتِبٌ লেখক, مَكۡتُوبٌ লিখিত। “লেখা” মানে বিধানও: كُتِبَ عَلَيۡكُمُ ٱلصِّيَامُ, তোমাদের উপর রোজা লিখে (ফরজ করে) দেওয়া হয়েছে।"))
R("أبو", ("father", "বাবা"),
  ("أَبٌ is a father, ءَابَآءٌ are fathers or forefathers, and أَبَوَانِ (“the two fathers”) means both parents.",
   "أَبٌ বাবা, ءَابَآءٌ পিতৃপুরুষ, আর أَبَوَانِ (“দুই পিতা”) মানে বাবা-মা দুজন।"))
R("أمم", ("heading towards; the source", "কোনো দিকে যাওয়া; উৎস"),
  ("أُمٌّ (mother) is where we come from. أُمَّةٌ is a community heading the same way, إِمَامٌ is the one in front whom everyone follows, أَمَامَ means “in front of”.",
   "أُمٌّ (মা) আমাদের উৎস। أُمَّةٌ একই দিকে চলা জাতি, إِمَامٌ সামনে থাকা নেতা যাকে সবাই অনুসরণ করে, أَمَامَ মানে “সামনে”।"))
R("عبد", ("serving", "সেবা করা, দাসত্ব"),
  ("عَبۡدٌ is one who serves (a servant), عَبَدَ is to serve and worship, عِبَادَةٌ is the act of worship, عَابِدٌ is the one doing it (a worshipper).",
   "عَبۡدٌ যে সেবা করে (বান্দা), عَبَدَ সেবা ও ইবাদত করা, عِبَادَةٌ ইবাদতের কাজ, عَابِدٌ যে ইবাদত করে (ইবাদতকারী)।"))
R("عون", ("helping", "সাহায্য"),
  ("أَعَانَ is to help. With ٱسۡتَـ (asking for) it becomes نَسۡتَعِينُ, “we ask for help”. تَعَاوَنُواْ is “help one another”, and ٱلۡمَاعُونَ are small everyday kindnesses.",
   "أَعَانَ সাহায্য করা। ٱسۡتَـ (চাওয়া) যোগে হয় نَسۡتَعِينُ, “আমরা সাহায্য চাই”। تَعَاوَنُواْ “পরস্পরকে সাহায্য করো”, আর ٱلۡمَاعُونَ ছোটখাটো দৈনন্দিন সাহায্য।"))
R("هدي", ("guiding gently; a gift", "কোমলভাবে পথ দেখানো; উপহার"),
  ("هَدَىٰ is to guide, هُدًى is guidance, ٱهۡتَدَىٰ is to be guided, هَادٍ is a guide. The same letters give هَدِيَّةٌ, a gift: guidance is a gift from Allah.",
   "هَدَىٰ পথ দেখানো, هُدًى হিদায়াত, ٱهۡتَدَىٰ পথ পাওয়া, هَادٍ পথপ্রদর্শক। একই অক্ষরে هَدِيَّةٌ মানে উপহার: হিদায়াত আল্লাহর উপহার।"))
R("قوم", ("standing up", "দাঁড়ানো"),
  ("قَامَ is to stand, قَوۡمٌ is a people who stand together, ٱلۡقِيَٰمَةُ is the Day of Standing (Resurrection), أَقَامَ is to make something stand (أَقِيمُواْ ٱلصَّلَوٰةَ, establish the prayer), مُسۡتَقِيمٌ is standing straight, قَيُّومٌ is the One who keeps everything standing.",
   "قَامَ দাঁড়ানো, قَوۡمٌ যারা একসাথে দাঁড়ায় (জাতি), ٱلۡقِيَٰمَةُ দাঁড়ানোর দিন (কিয়ামত), أَقَامَ দাঁড় করানো (أَقِيمُواْ ٱلصَّلَوٰةَ নামাজ কায়েম করো), مُسۡتَقِيمٌ সোজা দাঁড়ানো, قَيُّومٌ যিনি সবকিছুকে দাঁড় করিয়ে রাখেন।"))
R("نعم", ("ease, softness, blessing", "স্বাচ্ছন্দ্য, কোমলতা, নিয়ামত"),
  ("نِعۡمَةٌ is a blessing, أَنۡعَمَ is to bless, نَعِيمٌ is bliss. نَعَمٌ (cattle) were a blessing of wealth, and نِعۡمَ means “how excellent!”.",
   "نِعۡمَةٌ নিয়ামত, أَنۡعَمَ নিয়ামত দেওয়া, نَعِيمٌ পরম সুখ। نَعَمٌ (গবাদি পশু) ছিল সম্পদের নিয়ামত, আর نِعۡمَ মানে “কতই না উত্তম!”।"))
R("غير", ("other; changing", "অন্য; বদলানো"),
  ("غَيۡرُ means “other than, not”. يُغَيِّرُ is to change something (make it other): إِنَّ ٱللَّهَ لَا يُغَيِّرُ مَا بِقَوۡمٍ, Allah does not change a people's condition… (13:11).",
   "غَيۡرُ মানে “ছাড়া, নয়”। يُغَيِّرُ মানে বদলে দেওয়া (অন্যরকম করা): إِنَّ ٱللَّهَ لَا يُغَيِّرُ مَا بِقَوۡمٍ, আল্লাহ কোনো জাতির অবস্থা বদলান না… (১৩:১১)।"))
R("غضب", ("anger", "রাগ"),
  ("غَضَبٌ is anger, غَضِبَ is to become angry, غَضۡبَانُ is angry. مَغۡضُوبٌ (the done-to shape) is the one the anger is on.",
   "غَضَبٌ রাগ, غَضِبَ রাগ করা, غَضۡبَانُ রাগান্বিত। مَغۡضُوبٌ (যার প্রতি করা হয় ছাঁচ) মানে যার উপর রাগ।"))
R("ضلل", ("losing the way", "পথ হারানো"),
  ("ضَلَّ is to lose the way, ضَآلٌّ is one who is lost, ضَلَٰلٌ is being lost (error), أَضَلَّ is to make someone lose the way, مُضِلٌّ is a misleader.",
   "ضَلَّ পথ হারানো, ضَآلٌّ যে পথ হারিয়েছে, ضَلَٰلٌ পথভ্রষ্টতা, أَضَلَّ পথ ভোলানো, مُضِلٌّ যে পথভ্রষ্ট করে।"))
R("سجد", ("prostrating", "সিজদা করা"),
  ("سَجَدَ is to prostrate, سُجُودٌ is prostration, سَاجِدٌ is one who prostrates, and مَسۡجِدٌ (the shape مَفۡعِل = a place) is the place of prostration: a mosque.",
   "سَجَدَ সিজদা করা, سُجُودٌ সিজদা, سَاجِدٌ যে সিজদা করে, আর مَسۡجِدٌ (مَفۡعِل ছাঁচ = স্থান) সিজদার স্থান: মসজিদ।"))
R("كبر", ("bigness", "বড় হওয়া"),
  ("كَبِيرٌ is big, أَكۡبَرُ is bigger / the greatest, كَبُرَ is to grow big. ٱسۡتَكۡبَرَ is to see yourself as big: to be arrogant.",
   "كَبِيرٌ বড়, أَكۡبَرُ আরও বড় / সবচেয়ে বড়, كَبُرَ বড় হওয়া। ٱسۡتَكۡبَرَ নিজেকে বড় মনে করা: অহংকার করা।"))
R("جدد", ("cutting fresh", "নতুন করে কাটা"),
  ("جَدِيدٌ is new: freshly made, like cloth just cut. جُدَدٌ are streaks or tracks cut into the mountains (35:27).",
   "جَدِيدٌ মানে নতুন: সদ্য তৈরি, সদ্য কাটা কাপড়ের মতো। جُدَدٌ পাহাড়ের গায়ে কাটা রেখা বা পথ (৩৫:২৭)।"))
R("قرب", ("nearness", "নৈকট্য"),
  ("قَرِيبٌ is near, أَقۡرَبُ is nearer, ٱلۡقُرۡبَىٰ are relatives (people near you), مُقَرَّبٌ is one brought near. لَا تَقۡرَبَا means “do not go near”.",
   "قَرِيبٌ কাছে, أَقۡرَبُ আরও কাছে, ٱلۡقُرۡبَىٰ আত্মীয় (কাছের মানুষ), مُقَرَّبٌ যাকে কাছে আনা হয়েছে। لَا تَقۡرَبَا মানে “কাছেও যেয়ো না”।"))
R("قرأ", ("reading aloud", "উচ্চস্বরে পড়া"),
  ("قَرَأَ is to read or recite. ٱلۡقُرۡءَانُ is “the Recitation”: the book that is read aloud.",
   "قَرَأَ পড়া বা তিলাওয়াত করা। ٱلۡقُرۡءَانُ মানে “যা পড়া হয়”: যে কিতাব উচ্চস্বরে পাঠ করা হয়।"))
R("ذهب", ("going", "যাওয়া"),
  ("ذَهَبَ is to go, أَذۡهَبَ is to make something go (take it away), ذَاهِبٌ is one going. ذَهَبٌ (gold) also comes from these letters.",
   "ذَهَبَ যাওয়া, أَذۡهَبَ সরিয়ে নেওয়া (চলে যেতে বাধ্য করা), ذَاهِبٌ যে যাচ্ছে। ذَهَبٌ (সোনা)-ও এই অক্ষরগুলো থেকে।"))
R("سبح", ("gliding along; declaring far above", "ভেসে চলা; পবিত্রতা ঘোষণা"),
  ("The root first means gliding, swimming: planets يَسۡبَحُونَ, glide in their orbits. سَبَّحَ is to declare Allah far above every fault, and سُبۡحَٰنَ means “Glory be to…”.",
   "মূল অর্থ ভেসে চলা, সাঁতার কাটা: গ্রহরা يَسۡبَحُونَ, কক্ষপথে ভেসে চলে। سَبَّحَ মানে আল্লাহকে সব ত্রুটি থেকে বহু ঊর্ধ্বে ঘোষণা করা, আর سُبۡحَٰنَ মানে “পবিত্র…”।"))
R("عظم", ("greatness; bone", "মহত্ত্ব; হাড়"),
  ("عَظِيمٌ is great, أَعۡظَمُ is greater. عَظۡمٌ is a bone (plural عِظَٰمٌ), the strong frame that holds the body up.",
   "عَظِيمٌ মহান, أَعۡظَمُ আরও মহান। عَظۡمٌ হাড় (বহুবচন عِظَٰمٌ), যে শক্ত কাঠামো দেহকে ধরে রাখে।"))
R("سمع", ("hearing", "শোনা"),
  ("سَمِعَ is to hear, سَمۡعٌ is hearing, سَمِيعٌ is the All-Hearing, ٱسۡتَمَعَ is to listen carefully. In salah: سَمِعَ ٱللَّهُ لِمَنۡ حَمِدَهُۥ, Allah hears whoever praises Him.",
   "سَمِعَ শোনা, سَمۡعٌ শ্রবণ, سَمِيعٌ সর্বশ্রোতা, ٱسۡتَمَعَ মনোযোগ দিয়ে শোনা। নামাজে: سَمِعَ ٱللَّهُ لِمَنۡ حَمِدَهُۥ, যে আল্লাহর প্রশংসা করে আল্লাহ তা শোনেন।"))
R("علو", ("height", "উচ্চতা"),
  ("عَلِيٌّ is the Most High, أَعۡلَىٰ is the Highest (سُبۡحَٰنَ رَبِّيَ ٱلۡأَعۡلَىٰ in sajdah), تَعَالَىٰ is “exalted”. تَعَالَ means “come!”: literally “come up”.",
   "عَلِيٌّ সর্বোচ্চ, أَعۡلَىٰ সবচেয়ে উঁচু (সিজদায় سُبۡحَٰنَ رَبِّيَ ٱلۡأَعۡلَىٰ), تَعَالَىٰ “মহিমান্বিত”। تَعَالَ মানে “এসো!”: আক্ষরিক অর্থে “উপরে এসো”।"))
R("غفر", ("covering and protecting", "ঢেকে দেওয়া ও রক্ষা করা"),
  ("A helmet is مِغۡفَرٌ: it covers and protects. When Allah غَفَرَ (forgives), He covers the sin and protects you from its harm. ٱسۡتَغۡفَرَ is to ask for that, مَغۡفِرَةٌ is forgiveness, غَفُورٌ is the One who forgives again and again.",
   "শিরস্ত্রাণকে বলে مِغۡفَرٌ: যা ঢেকে রাখে ও রক্ষা করে। আল্লাহ যখন غَفَرَ (ক্ষমা করেন), তিনি গুনাহ ঢেকে দেন ও তার ক্ষতি থেকে রক্ষা করেন। ٱسۡتَغۡفَرَ তা চাওয়া, مَغۡفِرَةٌ ক্ষমা, غَفُورٌ যিনি বারবার ক্ষমা করেন।"))
R("قول", ("saying", "বলা"),
  ("قَالَ is “he said”, قُلۡ is “Say!”, قَوۡلٌ is a saying or word, قَآئِلٌ is a speaker.",
   "قَالَ “সে বলল”, قُلۡ “বলো!”, قَوۡلٌ কথা, قَآئِلٌ বক্তা।"))
R("أحد", ("one", "এক"),
  ("أَحَدٌ is one (the One, in قُلۡ هُوَ ٱللَّهُ أَحَدٌ), and also “anyone”. إِحۡدَىٰ is “one” for feminine words.",
   "أَحَدٌ মানে এক (قُلۡ هُوَ ٱللَّهُ أَحَدٌ-এ একক), আবার “কেউ”। إِحۡدَىٰ স্ত্রীবাচক শব্দের জন্য “এক”।"))
R("ولد", ("giving birth", "জন্ম দেওয়া"),
  ("وَلَدَ is to give birth, وَلَدٌ is a child, وَالِدٌ (the doer shape) is a father, وَالِدَةٌ a mother, وَٰلِدَانِ both parents, مَوۡلُودٌ (the done-to shape) is one who is born.",
   "وَلَدَ জন্ম দেওয়া, وَلَدٌ সন্তান, وَالِدٌ (কর্তা ছাঁচ) বাবা, وَالِدَةٌ মা, وَٰلِدَانِ বাবা-মা, مَوۡلُودٌ (কর্ম ছাঁচ) যে জন্মেছে।"))
R("كون", ("being, existing", "হওয়া, থাকা"),
  ("كَانَ is “was”, يَكُونُ is “is / will be”, كُن is “Be!”. مَكَانٌ (the place shape) is where something is.",
   "كَانَ “ছিল”, يَكُونُ “হয় / হবে”, كُن “হও!”। مَكَانٌ (স্থান ছাঁচ) যেখানে কিছু থাকে।"))
R("شهد", ("being present, seeing for yourself", "উপস্থিত থাকা, নিজে দেখা"),
  ("شَهِدَ is to witness, شَاهِدٌ and شَهِيدٌ are witnesses (شَهِيدٌ is also a martyr), شَهَادَةٌ is testimony, أَشۡهَدُ is “I bear witness”, مَشۡهُودٌ is witnessed.",
   "شَهِدَ সাক্ষী হওয়া, شَاهِدٌ ও شَهِيدٌ সাক্ষী (شَهِيدٌ শহীদও), شَهَادَةٌ সাক্ষ্য, أَشۡهَدُ “আমি সাক্ষ্য দিই”, مَشۡهُودٌ যা প্রত্যক্ষ করা হয়।"))
R("رسل", ("sending", "পাঠানো"),
  ("أَرۡسَلَ is to send, رَسُولٌ is one who is sent (a messenger), رِسَالَةٌ is a message, مُرۡسِلٌ is a sender, مُرۡسَلٌ is one sent.",
   "أَرۡسَلَ পাঠানো, رَسُولٌ যাকে পাঠানো হয় (রাসূল), رِسَالَةٌ বার্তা, مُرۡسِلٌ প্রেরক, مُرۡسَلٌ প্রেরিত।"))
R("صلو", ("prayer; turning towards", "নামাজ; অভিমুখী হওয়া"),
  ("صَلَوٰةٌ is the prayer, صَلَّىٰ is to pray, مُصَلٍّ is one who prays, مُصَلًّى is a place of prayer. When Allah “prays” on the Prophet (صَلَّى ٱللَّهُ عَلَيۡهِ), it means He sends blessings.",
   "صَلَوٰةٌ নামাজ, صَلَّىٰ নামাজ পড়া, مُصَلٍّ যে নামাজ পড়ে, مُصَلًّى নামাজের স্থান। আল্লাহ যখন নবীর উপর صَلَّى করেন, তার মানে তিনি রহমত পাঠান।"))
R("فلح", ("splitting the soil; success", "মাটি চষা; সফলতা"),
  ("A farmer is فَلَّاحٌ: he splits the soil and reaps a harvest. فَلَاحٌ is that kind of success, أَفۡلَحَ is to succeed, مُفۡلِحٌ is one who succeeds.",
   "কৃষককে বলে فَلَّاحٌ: সে মাটি চষে ফসল তোলে। فَلَاحٌ সেই রকম সফলতা, أَفۡلَحَ সফল হওয়া, مُفۡلِحٌ সফলকাম।"))
R("خير", ("good; choosing", "ভালো; বেছে নেওয়া"),
  ("خَيۡرٌ is good or better. ٱخۡتَارَ is to choose (pick the good), خِيَرَةٌ is a choice. صَلَاةُ ٱلِٱسۡتِخَارَةِ is the prayer asking Allah to choose the good for you.",
   "خَيۡرٌ ভালো বা উত্তম। ٱخۡتَارَ বেছে নেওয়া (ভালোটা নেওয়া), خِيَرَةٌ পছন্দ। صَلَاةُ ٱلِٱسۡتِخَارَةِ হলো আল্লাহর কাছে ভালোটা বেছে দেওয়ার প্রার্থনা।"))
R("نوم", ("sleep", "ঘুম"),
  ("نَوۡمٌ is sleep, نَآئِمٌ is one sleeping, مَنَامٌ is sleep or a dream. In the Fajr adhan: ٱلصَّلَوٰةُ خَيۡرٌ مِّنَ ٱلنَّوۡمِ, prayer is better than sleep.",
   "نَوۡمٌ ঘুম, نَآئِمٌ ঘুমন্ত, مَنَامٌ ঘুম বা স্বপ্ন। ফজরের আজানে: ٱلصَّلَوٰةُ خَيۡرٌ مِّنَ ٱلنَّوۡمِ, ঘুমের চেয়ে নামাজ উত্তম।"))
R("عطو", ("giving", "দেওয়া"),
  ("أَعۡطَىٰ is to give, عَطَآءٌ is a gift. أَعۡطَيۡنَٰكَ is “We have given you”.",
   "أَعۡطَىٰ দেওয়া, عَطَآءٌ দান। أَعۡطَيۡنَٰكَ মানে “আমরা তোমাকে দিয়েছি”।"))
R("كثر", ("much, many", "অনেক"),
  ("كَثِيرٌ is many, أَكۡثَرُ is most. ٱلۡكَوۡثَرُ is good in great abundance. ٱلتَّكَاثُرُ (Surah 102) is competing to have more.",
   "كَثِيرٌ অনেক, أَكۡثَرُ সবচেয়ে বেশি। ٱلۡكَوۡثَرُ প্রচুর কল্যাণ। ٱلتَّكَاثُرُ (সূরা ১০২) বেশি পাওয়ার প্রতিযোগিতা।"))
R("شنأ", ("hatred", "ঘৃণা"),
  ("شَنَـَٔانُ is hatred, and شَانِئٌ (the doer shape) is one who hates: an enemy.",
   "شَنَـَٔانُ ঘৃণা, আর شَانِئٌ (কর্তা ছাঁচ) যে ঘৃণা করে: শত্রু।"))
R("عصر", ("pressing, squeezing", "চাপ দেওয়া, নিংড়ানো"),
  ("يَعۡصِرُونَ is to press (grapes or olives, 12:49), مُعۡصِرَٰتٌ are clouds pressing out rain. عَصۡرٌ is time, and the afternoon: the day pressed towards its end.",
   "يَعۡصِرُونَ নিংড়ানো (আঙুর বা জলপাই, ১২:৪৯), مُعۡصِرَٰتٌ বৃষ্টি নিংড়ে দেওয়া মেঘ। عَصۡرٌ সময়, আর বিকেল: দিন যখন শেষের দিকে চেপে আসে।"))
R("أنس", ("closeness, feeling at home", "ঘনিষ্ঠতা, আপন বোধ"),
  ("Humans are social: they feel at home with each other. إِنسَٰنٌ is a human being, ٱلنَّاسُ are people, ٱلۡإِنسُ is mankind, ءَانَسَ is to notice something near.",
   "মানুষ সামাজিক: একে অপরের সাথে আপন বোধ করে। إِنسَٰنٌ মানুষ, ٱلنَّاسُ লোকজন, ٱلۡإِنسُ মানবজাতি, ءَانَسَ কাছে কিছু অনুভব করা।"))
R("خسر", ("loss", "ক্ষতি"),
  ("خُسۡرٌ and خُسۡرَانٌ are loss, خَسِرَ is to lose, خَٰسِرٌ (the doer shape) is a loser.",
   "خُسۡرٌ ও خُسۡرَانٌ ক্ষতি, خَسِرَ ক্ষতিগ্রস্ত হওয়া, خَٰسِرٌ (কর্তা ছাঁচ) ক্ষতিগ্রস্ত।"))
R("أمن", ("safety and trust", "নিরাপত্তা ও আস্থা"),
  ("أَمِنَ is to be safe, ءَامِنٌ is safe, أَمِينٌ is trustworthy. ءَامَنَ (to believe) is to trust and so be safe: إِيمَٰنٌ is faith, مُؤۡمِنٌ is a believer.",
   "أَمِنَ নিরাপদ হওয়া, ءَامِنٌ নিরাপদ, أَمِينٌ বিশ্বস্ত। ءَامَنَ (ঈমান আনা) মানে আস্থা রেখে নিরাপদ হওয়া: إِيمَٰنٌ ঈমান, مُؤۡمِنٌ মুমিন।"))
R("عمل", ("working, doing", "কাজ করা"),
  ("عَمِلَ is to do or work, عَمَلٌ is a deed, عَامِلٌ (the doer shape) is a worker.",
   "عَمِلَ কাজ করা, عَمَلٌ আমল (কাজ), عَامِلٌ (কর্তা ছাঁচ) কর্মী।"))
R("صلح", ("being sound and right", "ঠিক ও সুস্থ থাকা"),
  ("صَٰلِحٌ is one who is sound (righteous), صَٰلِحَٰتٌ are good deeds, أَصۡلَحَ is to set something right, إِصۡلَٰحٌ is putting right, مُصۡلِحٌ is one who puts things right.",
   "صَٰلِحٌ যে ঠিক পথে (নেককার), صَٰلِحَٰتٌ সৎকাজ, أَصۡلَحَ কোনো কিছু ঠিক করা, إِصۡلَٰحٌ সংশোধন, مُصۡلِحٌ সংশোধনকারী।"))
R("وصي", ("advising, connecting", "উপদেশ দেওয়া, যুক্ত করা"),
  ("وَصَّىٰ is to advise strongly, وَصِيَّةٌ is a will (last advice). تَوَاصَوۡاْ is “they advised one another”.",
   "وَصَّىٰ জোর দিয়ে উপদেশ দেওয়া, وَصِيَّةٌ অসিয়ত (শেষ উপদেশ)। تَوَاصَوۡاْ “তারা পরস্পরকে উপদেশ দিয়েছে”।"))
R("حقق", ("truth; what is due", "সত্য; প্রাপ্য"),
  ("حَقٌّ is the truth and also a right (what is due). حَقَّ is to become due, أَحَقُّ is more deserving, ٱلۡحَآقَّةُ is the Sure Reality (Surah 69).",
   "حَقٌّ সত্য, আবার অধিকার (যা প্রাপ্য)। حَقَّ অবধারিত হওয়া, أَحَقُّ বেশি হকদার, ٱلۡحَآقَّةُ অবশ্যম্ভাবী সত্য (সূরা ৬৯)।"))
R("صبر", ("holding firm", "দৃঢ় থাকা"),
  ("صَبۡرٌ is patience, صَبَرَ is to hold firm, صَابِرٌ is one who is patient, صَبَّارٌ (the فَعَّال shape = a lot) is very patient.",
   "صَبۡرٌ ধৈর্য, صَبَرَ দৃঢ় থাকা, صَابِرٌ ধৈর্যশীল, صَبَّارٌ (فَعَّال ছাঁচ = খুব বেশি) অত্যন্ত ধৈর্যশীল।"))
R("نصر", ("helping to win", "বিজয়ে সাহায্য"),
  ("نَصَرَ is to help, نَصۡرٌ is help that brings victory, نَاصِرٌ and نَصِيرٌ are helpers, ٱنتَصَرَ is to defend oneself.",
   "نَصَرَ সাহায্য করা, نَصۡرٌ বিজয় এনে দেওয়া সাহায্য, نَاصِرٌ ও نَصِيرٌ সাহায্যকারী, ٱنتَصَرَ আত্মরক্ষা করা।"))
R("فتح", ("opening", "খোলা"),
  ("فَتَحَ is to open, فَتۡحٌ is an opening (a victory), مَفَاتِحُ are keys, ٱلۡفَتَّاحُ is the One who opens and judges. ٱلۡفَاتِحَةُ is “the Opening”: the first surah.",
   "فَتَحَ খোলা, فَتۡحٌ উন্মোচন (বিজয়), مَفَاتِحُ চাবি, ٱلۡفَتَّاحُ যিনি খুলে দেন ও ফয়সালা করেন। ٱلۡفَاتِحَةُ মানে “সূচনা”: প্রথম সূরা।"))
R("رأي", ("seeing", "দেখা"),
  ("رَأَىٰ is to see, أَرَىٰ is to show, رُءۡيَا is a dream (what you see in sleep), رِئَآءٌ is showing off (doing good to be seen).",
   "رَأَىٰ দেখা, أَرَىٰ দেখানো, رُءۡيَا স্বপ্ন (ঘুমে যা দেখা হয়), رِئَآءٌ লোক দেখানো (দেখানোর জন্য ভালো কাজ)।"))
R("دخل", ("entering", "প্রবেশ"),
  ("دَخَلَ is to enter, أَدۡخَلَ is to make someone enter, دَاخِلٌ is one entering, مُدۡخَلٌ is an entrance.",
   "دَخَلَ প্রবেশ করা, أَدۡخَلَ প্রবেশ করানো, دَاخِلٌ যে প্রবেশ করে, مُدۡخَلٌ প্রবেশপথ।"))
R("توب", ("turning back", "ফিরে আসা"),
  ("تَابَ is to turn back. A person turns back to Allah (repents); Allah turns back to him with mercy. تَوۡبَةٌ is repentance, تَوَّابٌ (the فَعَّال shape = a lot) is the One who turns back again and again.",
   "تَابَ মানে ফিরে আসা। মানুষ আল্লাহর দিকে ফেরে (তওবা করে); আল্লাহ রহমত নিয়ে তার দিকে ফেরেন। تَوۡبَةٌ তওবা, تَوَّابٌ (فَعَّال ছাঁচ = বারবার) যিনি বারবার ফেরেন।"))
R("عوذ", ("seeking shelter", "আশ্রয় চাওয়া"),
  ("أَعُوذُ is “I seek refuge”, ٱسۡتَعِذۡ is “seek refuge!”, and مَعَاذَ ٱللَّهِ means “refuge in Allah!” (God forbid).",
   "أَعُوذُ “আমি আশ্রয় চাই”, ٱسۡتَعِذۡ “আশ্রয় চাও!”, আর مَعَاذَ ٱللَّهِ মানে “আল্লাহর আশ্রয়!” (আল্লাহ রক্ষা করুন)।"))
R("فلق", ("splitting open", "চিরে ফেলা"),
  ("ٱلۡفَلَقُ is daybreak: the night split open by light. فَالِقُ ٱلۡحَبِّ is the One who splits the seed (6:95), and ٱنفَلَقَ is “it split” (the sea for Musa).",
   "ٱلۡفَلَقُ ভোর: আলোয় রাত চিরে যাওয়া। فَالِقُ ٱلۡحَبِّ যিনি বীজ চিরে দেন (৬:৯৫), আর ٱنفَلَقَ “তা ফেটে গেল” (মুসার জন্য সমুদ্র)।"))
R("شرر", ("evil, harm", "অনিষ্ট"),
  ("شَرٌّ is evil or harm. شَرَرٌ are sparks that fly from a fire.", "شَرٌّ অনিষ্ট বা ক্ষতি। شَرَرٌ আগুন থেকে ছিটকে আসা স্ফুলিঙ্গ।"))
R("خلق", ("creating, shaping", "সৃষ্টি, আকার দেওয়া"),
  ("خَلَقَ is to create, خَلۡقٌ is creation, خَٰلِقٌ is the Creator, خَلَّاقٌ (the فَعَّال shape) the Creator of everything. خُلُقٌ is a person's character: the shape of their nature (إِنَّكَ لَعَلَىٰ خُلُقٍ عَظِيمٍ).",
   "خَلَقَ সৃষ্টি করা, خَلۡقٌ সৃষ্টি, خَٰلِقٌ স্রষ্টা, خَلَّاقٌ (فَعَّال ছাঁচ) সবকিছুর স্রষ্টা। خُلُقٌ মানুষের চরিত্র: স্বভাবের আকার (إِنَّكَ لَعَلَىٰ خُلُقٍ عَظِيمٍ)।"))
R("غسق", ("deepening darkness", "গাঢ় অন্ধকার"),
  ("غَسَقُ ٱلَّيۡلِ is the darkness of night, and غَاسِقٌ is darkness as it spreads.", "غَسَقُ ٱلَّيۡلِ রাতের অন্ধকার, আর غَاسِقٌ ছড়িয়ে পড়া অন্ধকার।"))
R("عقد", ("tying", "গিঁট দেওয়া"),
  ("عُقۡدَةٌ is a knot (plural عُقَدٌ), and عُقُودٌ are contracts: agreements that tie people together. Musa asked: ٱحۡلُلۡ عُقۡدَةً مِّن لِّسَانِي, untie the knot from my tongue.",
   "عُقۡدَةٌ গিঁট (বহুবচন عُقَدٌ), আর عُقُودٌ চুক্তি: যা মানুষকে বেঁধে রাখে। মুসা বলেছিলেন: ٱحۡلُلۡ عُقۡدَةً مِّن لِّسَانِي, আমার জিহ্বার গিঁট খুলে দাও।"))
R("حسد", ("envy", "হিংসা"),
  ("حَسَدٌ is envy, حَسَدَ is to envy, حَاسِدٌ (the doer shape) is an envier.", "حَسَدٌ হিংসা, حَسَدَ হিংসা করা, حَاسِدٌ (কর্তা ছাঁচ) হিংসুক।"))
R("وسوس", ("whispering", "ফিসফিস করা"),
  ("The word sounds like what it means: وَسۡوَسَ is to whisper, وَسۡوَاسٌ is the whisperer.", "শব্দটির ধ্বনিই অর্থ বোঝায়: وَسۡوَسَ ফিসফিস করা, وَسۡوَاسٌ কুমন্ত্রণাদাতা।"))
R("خنس", ("drawing back, hiding", "পিছিয়ে লুকানো"),
  ("خَنَّاسٌ (the فَعَّال shape = again and again) is one who slinks back and hides whenever Allah is remembered. ٱلۡخُنَّسِ are the stars that seem to draw back (81:15).",
   "خَنَّاسٌ (فَعَّال ছাঁচ = বারবার) যে আল্লাহর জিকিরে বারবার পিছিয়ে লুকায়। ٱلۡخُنَّسِ পিছিয়ে যাওয়া নক্ষত্র (৮১:১৫)।"))
R("صدر", ("the chest; coming out", "বুক; বেরিয়ে আসা"),
  ("صَدۡرٌ is the chest, where feelings live (plural صُدُورٌ). Musa asked: رَبِّ ٱشۡرَحۡ لِي صَدۡرِي, my Lord, open my chest for me. يَصۡدُرُ is to come out.",
   "صَدۡرٌ বুক, অনুভূতির স্থান (বহুবচন صُدُورٌ)। মুসা বলেছিলেন: رَبِّ ٱشۡرَحۡ لِي صَدۡرِي, হে আমার রব, আমার বুক প্রশস্ত করে দাও। يَصۡدُرُ বেরিয়ে আসা।"))
R("جنن", ("hidden, covered", "লুকানো, ঢাকা"),
  ("Everything here is hidden: ٱلۡجِنُّ are beings hidden from us, جَنَّةٌ is a garden hidden under its trees, جُنَّةٌ is a shield, مَجۡنُونٌ is one whose mind is covered (mad). جَنَّ عَلَيۡهِ ٱلَّيۡلُ: night covered him.",
   "এখানে সবই লুকানো: ٱلۡجِنُّ আমাদের থেকে লুকানো সৃষ্টি, جَنَّةٌ গাছে ঢাকা বাগান, جُنَّةٌ ঢাল, مَجۡنُونٌ যার বুদ্ধি ঢাকা পড়েছে (পাগল)। جَنَّ عَلَيۡهِ ٱلَّيۡلُ: রাত তাকে ঢেকে ফেলল।"))
R("حيي", ("life", "জীবন"),
  ("حَيٌّ is alive, حَيَوٰةٌ is life, أَحۡيَا is to give life. تَحِيَّةٌ is a greeting: wishing someone life (ٱلتَّحِيَّاتُ in the tashahhud). The name يَحۡيَىٰ means “he lives”.",
   "حَيٌّ জীবিত, حَيَوٰةٌ জীবন, أَحۡيَا জীবন দেওয়া। تَحِيَّةٌ অভিবাদন: কারও জীবন কামনা করা (তাশাহহুদে ٱلتَّحِيَّاتُ)। নাম يَحۡيَىٰ মানে “সে বাঁচে”।"))
R("طيب", ("good and pure", "ভালো ও পবিত্র"),
  ("طَيِّبٌ is good and pure, طَيِّبَٰتٌ are good, pure things, طَابَ is to be good, طُوبَىٰ is a blessed, happy state.",
   "طَيِّبٌ ভালো ও পবিত্র, طَيِّبَٰتٌ পবিত্র জিনিস, طَابَ ভালো হওয়া, طُوبَىٰ সুখময় অবস্থা।"))
R("سلم", ("safety and peace; giving yourself over", "নিরাপত্তা ও শান্তি; আত্মসমর্পণ"),
  ("سَلَٰمٌ is peace and safety. أَسۡلَمَ is to give yourself over to Allah and so be safe: إِسۡلَٰمٌ is that submission and مُسۡلِمٌ is one who does it. سَلَّمَ is to greet with peace.",
   "سَلَٰمٌ শান্তি ও নিরাপত্তা। أَسۡلَمَ নিজেকে আল্লাহর কাছে সঁপে দিয়ে নিরাপদ হওয়া: إِسۡلَٰمٌ সেই আত্মসমর্পণ, مُسۡلِمٌ যে তা করে। سَلَّمَ সালাম দেওয়া।"))
R("نبأ", ("important news", "গুরুত্বপূর্ণ সংবাদ"),
  ("نَبَأٌ is important news, نَبَّأَ is to inform, نَبِيٌّ is a prophet: one who brings news from Allah. نُبُوَّةٌ is prophethood.",
   "نَبَأٌ গুরুত্বপূর্ণ সংবাদ, نَبَّأَ জানানো, نَبِيٌّ নবী: যিনি আল্লাহর কাছ থেকে সংবাদ আনেন। نُبُوَّةٌ নবুয়ত।"))
R("برك", ("settling down and staying", "থিতু হয়ে থাকা"),
  ("A camel “بَرَكَ” when it kneels and stays. بَرَكَةٌ is blessing: good that stays and grows. بَارَكَ is to bless, مُبَارَكٌ is blessed, تَبَارَكَ is “Blessed is…”.",
   "উট যখন বসে থিতু হয়, বলে بَرَكَ। بَرَكَةٌ বরকত: যে কল্যাণ থেকে যায় ও বাড়ে। بَارَكَ বরকত দেওয়া, مُبَارَكٌ বরকতময়, تَبَارَكَ “বরকতময় তিনি…”।"))
R("أتي", ("coming; bringing", "আসা; নিয়ে আসা"),
  ("أَتَىٰ is to come. ءَاتَىٰ is to make something come to someone: to give. ءَاتِنَا is “give us”, إِيتَآءُ ٱلزَّكَوٰةِ is giving zakah.",
   "أَتَىٰ আসা। ءَاتَىٰ কারও কাছে কিছু পৌঁছে দেওয়া: দেওয়া। ءَاتِنَا “আমাদের দাও”, إِيتَآءُ ٱلزَّكَوٰةِ জাকাত দেওয়া।"))
R("دنو", ("near and low", "নিকট ও নিচু"),
  ("ٱلدُّنۡيَا is the nearer, lower life: this world. أَدۡنَىٰ is nearer or lower, دَانِيَةٌ is fruit hanging low.",
   "ٱلدُّنۡيَا নিকটবর্তী, নিচু জীবন: এই দুনিয়া। أَدۡنَىٰ আরও কাছে বা নিচে, دَانِيَةٌ নিচু হয়ে ঝুলে থাকা ফল।"))
R("حسن", ("beauty, goodness", "সৌন্দর্য, কল্যাণ"),
  ("حَسَنٌ is good and beautiful, حَسَنَةٌ is a good deed or good thing, أَحۡسَنَ is to do something well, أَحۡسَنُ is better or best, مُحۡسِنٌ is one who does good, إِحۡسَانٌ is excellence. ٱلۡأَسۡمَآءُ ٱلۡحُسۡنَىٰ are the most beautiful names.",
   "حَسَنٌ ভালো ও সুন্দর, حَسَنَةٌ সৎকাজ বা কল্যাণ, أَحۡسَنَ সুন্দরভাবে করা, أَحۡسَنُ উত্তম, مُحۡسِنٌ সৎকর্মশীল, إِحۡسَانٌ উৎকর্ষ। ٱلۡأَسۡمَآءُ ٱلۡحُسۡنَىٰ সুন্দরতম নামসমূহ।"))
R("أخر", ("later, after", "পরে, শেষে"),
  ("ءَاخِرٌ is last, so ٱلۡأٓخِرَةُ is the last life: the Hereafter. ءَاخَرُ is “another”, and أَخَّرَ is to put something later (delay).",
   "ءَاخِرٌ শেষ, তাই ٱلۡأٓخِرَةُ শেষ জীবন: আখিরাত। ءَاخَرُ “অন্য”, আর أَخَّرَ পিছিয়ে দেওয়া।"))
R("وقي", ("protecting", "রক্ষা করা"),
  ("وَقَىٰ is to protect, قِنَا is “protect us”. تَقۡوَىٰ is protecting yourself from Allah's displeasure (God-consciousness), and مُتَّقٍ is one who does that.",
   "وَقَىٰ রক্ষা করা, قِنَا “আমাদের রক্ষা করো”। تَقۡوَىٰ আল্লাহর অসন্তুষ্টি থেকে নিজেকে রক্ষা করা (তাকওয়া), আর مُتَّقٍ যে তা করে।"))
R("عذب", ("punishment; fresh water", "শাস্তি; মিঠা পানি"),
  ("عَذَابٌ is punishment and عَذَّبَ is to punish. The same letters also give عَذۡبٌ: fresh, sweet water (25:53).",
   "عَذَابٌ শাস্তি, عَذَّبَ শাস্তি দেওয়া। একই অক্ষরে عَذۡبٌ মানে মিঠা পানি (২৫:৫৩)।"))
R("نور", ("light", "আলো"),
  ("Light and fire both shine: نُورٌ is light, نَارٌ is fire, مُنِيرٌ is shining.", "আলো ও আগুন দুটোই জ্বলে: نُورٌ আলো, نَارٌ আগুন, مُنِيرٌ উজ্জ্বল।"))
R("زيد", ("increasing", "বৃদ্ধি"),
  ("زَادَ is to increase, زِدۡنِي is “increase me”, زِيَادَةٌ is an increase, مَزِيدٌ is more.", "زَادَ বাড়ানো, زِدۡنِي “আমাকে বাড়িয়ে দাও”, زِيَادَةٌ বৃদ্ধি, مَزِيدٌ আরও।"))
R("ربو", ("growing, rising", "বেড়ে ওঠা"),
  ("رَبَّيَانِي is “they raised me” (made me grow). رَبَتۡ is “it swelled”, رَبۡوَةٌ is raised ground, and رِبَوٰا is usury: money made to grow unfairly. (رَبٌّ comes from ر ب ب, a close cousin.)",
   "رَبَّيَانِي “তাঁরা আমাকে লালন করেছেন” (বড় করেছেন)। رَبَتۡ “তা ফুলে উঠল”, رَبۡوَةٌ উঁচু জমি, আর رِبَوٰا সুদ: অন্যায়ভাবে বাড়ানো টাকা। (رَبٌّ এসেছে ر ب ب থেকে, কাছের আত্মীয়।)"))
R("صغر", ("smallness", "ছোট হওয়া"),
  ("صَغِيرٌ is small or young, أَصۡغَرُ is smaller, صَٰغِرٌ is one made small (humbled).", "صَغِيرٌ ছোট, أَصۡغَرُ আরও ছোট, صَٰغِرٌ যাকে ছোট করা হয়েছে (লাঞ্ছিত)।"))
R("ظلم", ("darkness; putting things in the wrong place", "অন্ধকার; কোনো কিছুকে ভুল জায়গায় রাখা"),
  ("ظُلۡمٌ is injustice: putting something where it doesn't belong. ظَلَمَ is to wrong, ظَٰلِمٌ is a wrongdoer, and ظُلُمَٰتٌ are darknesses. Injustice is a kind of darkness.",
   "ظُلۡمٌ অন্যায়: কিছুকে তার অনুপযুক্ত জায়গায় রাখা। ظَلَمَ জুলুম করা, ظَٰلِمٌ জালিম, আর ظُلُمَٰتٌ অন্ধকারসমূহ। অন্যায় এক ধরনের অন্ধকার।"))
R("نفس", ("breath; self", "শ্বাস; সত্তা"),
  ("نَفۡسٌ is the self or soul (plural أَنفُسٌ), linked to breath: تَنَفَّسَ is to breathe (ٱلصُّبۡحِ إِذَا تَنَفَّسَ, the dawn as it breathes). تَنَافَسَ is to compete for something precious.",
   "نَفۡسٌ সত্তা বা প্রাণ (বহুবচন أَنفُسٌ), শ্বাসের সাথে যুক্ত: تَنَفَّسَ শ্বাস নেওয়া (ٱلصُّبۡحِ إِذَا تَنَفَّسَ, ভোর যখন শ্বাস নেয়)। تَنَافَسَ মূল্যবান কিছুর জন্য প্রতিযোগিতা করা।"))
R("حسب", ("counting", "গণনা"),
  ("حِسَابٌ is an account, حَسِيبٌ is the Reckoner. حَسِبَ is to think (count something as so). حَسۡبُنَا ٱللَّهُ: Allah is enough for us, counted as all we need.",
   "حِسَابٌ হিসাব, حَسِيبٌ হিসাবগ্রহণকারী। حَسِبَ মনে করা (কিছুকে এমন গণ্য করা)। حَسۡبُنَا ٱللَّهُ: আল্লাহই আমাদের জন্য যথেষ্ট।"))
R("أخذ", ("taking", "নেওয়া"),
  ("أَخَذَ is to take, ٱتَّخَذَ is to take for yourself (adopt), تَأۡخُذُهُۥ is “overtakes Him” (Ayat al-Kursi), يُؤَاخِذُ is to take someone to task.",
   "أَخَذَ নেওয়া, ٱتَّخَذَ নিজের জন্য গ্রহণ করা, تَأۡخُذُهُۥ “তাঁকে স্পর্শ করে” (আয়াতুল কুরসি), يُؤَاخِذُ পাকড়াও করা।"))
R("شفع", ("pairing, joining", "জোড়া বাঁধা"),
  ("شَفۡعٌ is “even” (a pair). شَفَٰعَةٌ is intercession: joining your request to someone else's, standing beside them as a pair. شَفِيعٌ is an intercessor, يَشۡفَعُ is to intercede.",
   "شَفۡعٌ মানে জোড় (জোড়া)। شَفَٰعَةٌ সুপারিশ: অন্যের আবেদনের সাথে নিজেরটা জুড়ে তার পাশে দাঁড়ানো। شَفِيعٌ সুপারিশকারী, يَشۡفَعُ সুপারিশ করা।"))
R("عند", ("with, beside", "কাছে, পাশে"),
  ("عِندَ means “with, at, near”. عَنِيدٌ (stubborn) shares the letters: one who stands apart and opposes.", "عِندَ মানে “কাছে, নিকট”। عَنِيدٌ (একগুঁয়ে) একই অক্ষরে: যে আলাদা হয়ে বিরোধিতা করে।"))
R("أذن", ("the ear; hearing; permission", "কান; শোনা; অনুমতি"),
  ("أُذُنٌ is the ear. إِذۡنٌ is permission: something you have heard you may do. أَذَّنَ is to call out for all to hear: the أَذَان, and the مُؤَذِّنٌ who calls it. ٱسۡتَـٔۡذَنَ is to ask permission.",
   "أُذُنٌ কান। إِذۡنٌ অনুমতি: যা করা যাবে বলে শোনা গেছে। أَذَّنَ সবাইকে শুনিয়ে ডাকা: أَذَان, আর যিনি ডাকেন مُؤَذِّنٌ। ٱسۡتَـٔۡذَنَ অনুমতি চাওয়া।"))
R("بين", ("between; standing apart, clear", "মাঝে; আলাদা, স্পষ্ট"),
  ("بَيۡنَ is “between”. Something clear stands apart from everything else: مُبِينٌ is clear, بَيِّنَةٌ is clear proof, بَيَّنَ is to make clear.",
   "بَيۡنَ মানে “মাঝে”। যা স্পষ্ট তা অন্য সব থেকে আলাদা হয়ে থাকে: مُبِينٌ স্পষ্ট, بَيِّنَةٌ সুস্পষ্ট প্রমাণ, بَيَّنَ স্পষ্ট করা।"))
R("خلف", ("behind, coming after", "পেছনে, পরে আসা"),
  ("خَلۡفَ is “behind”, خَلِيفَةٌ is one who comes after (a successor). ٱخۡتِلَٰفُ ٱلَّيۡلِ وَٱلنَّهَارِ is night and day coming one after the other, and ٱخۡتَلَفَ is to differ (go different ways).",
   "خَلۡفَ “পেছনে”, خَلِيفَةٌ যে পরে আসে (প্রতিনিধি)। ٱخۡتِلَٰفُ ٱلَّيۡلِ وَٱلنَّهَارِ রাত-দিনের একের পর এক আসা, আর ٱخۡتَلَفَ মতভেদ করা (ভিন্ন পথে যাওয়া)।"))
R("حوط", ("surrounding", "ঘিরে রাখা"),
  ("أَحَاطَ is to surround completely, مُحِيطٌ is the All-Encompassing. A wall (حَآئِطٌ) is what surrounds a place.", "أَحَاطَ সম্পূর্ণ ঘিরে ফেলা, مُحِيطٌ সর্বব্যাপী। দেয়াল (حَآئِطٌ) যা কোনো জায়গা ঘিরে রাখে।"))
R("شيأ", ("thing; willing", "বস্তু; ইচ্ছা"),
  ("شَآءَ is to will, شَيۡءٌ is a thing: something willed into being. إِن شَآءَ ٱللَّهُ is “if Allah wills”.", "شَآءَ ইচ্ছা করা, شَيۡءٌ বস্তু: যা ইচ্ছায় অস্তিত্বে আসে। إِن شَآءَ ٱللَّهُ “আল্লাহ চাইলে”।"))
R("وسع", ("width, room", "প্রশস্ততা"),
  ("وَسِعَ is to have room for everything, وَٰسِعٌ is the All-Encompassing, سَعَةٌ is plenty, وُسۡعٌ is capacity: لَا يُكَلِّفُ ٱللَّهُ نَفۡسًا إِلَّا وُسۡعَهَا, Allah does not burden a soul beyond its capacity.",
   "وَسِعَ সবকিছুর জায়গা থাকা, وَٰسِعٌ সর্বব্যাপী, سَعَةٌ প্রাচুর্য, وُسۡعٌ সামর্থ্য: لَا يُكَلِّفُ ٱللَّهُ نَفۡسًا إِلَّا وُسۡعَهَا, আল্লাহ কাউকে সামর্থ্যের বাইরে দায়িত্ব দেন না।"))
R("حفظ", ("guarding, keeping", "সংরক্ষণ"),
  ("حَفِظَ is to guard or keep (a حَافِظ keeps the Quran in memory), حِفۡظٌ is guarding, حَفِيظٌ is a guardian, مَحۡفُوظٌ is kept safe (ٱللَّوۡحِ ٱلۡمَحۡفُوظِ).",
   "حَفِظَ রক্ষা বা সংরক্ষণ করা (حَافِظ কুরআন স্মৃতিতে ধরে রাখেন), حِفۡظٌ সংরক্ষণ, حَفِيظٌ রক্ষক, مَحۡفُوظٌ সুরক্ষিত (ٱللَّوۡحِ ٱلۡمَحۡفُوظِ)।"))
