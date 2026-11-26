# -*- coding: utf-8 -*-
"""Build app data from Quran sources + hand-authored content.
Outputs:
  OUT/src/data/course.json    — words, patterns, texts (with tokens), units (with lessons)
  OUT/src/data/coverage.json  — surah list + per-surah counts of curriculum words
  OUT/public/quran/N.json     — every surah word-by-word for the reader
  OUT/public/quran/lemmas.json
"""
import json, os, sys, re, unicodedata, collections
from load import load, stem
import content, texts as T
content.W = {unicodedata.normalize('NFC', k): v for k, v in content.W.items()}
for grp in T.HAND.values():
    for l in grp:
        l['tokens'] = [(a, e, b, unicodedata.normalize('NFC', k) if k else k, p) for (a, e, b, k, p) in l['tokens']]

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(os.path.join(HERE, '..', '..'))
from load import SRC
words, wb, tw, qj = load()

def key_of(sg):
    f = sg['f']
    if 'LEM' in f: return unicodedata.normalize('NFC', f['LEM'] + '|' + f.get('ROOT', ''))
    tags = f.get('_tags', [])
    if 'PRON' in tags:
        for t in tags:
            if re.fullmatch(r'[123][MFP]?[SDP]?', t) and t != 'PRON': return 'PRON:' + t
    return '?'

# ---------------- global lemma stats ----------------
tok_key = {}
cnt = collections.Counter()
surah_cnt = collections.defaultdict(collections.Counter)
surah_tot = collections.Counter()
root_of = {}
lem_forms = collections.defaultdict(collections.Counter)
for loc, segs in words.items():
    sg = stem(segs); k = key_of(sg)
    tok_key[loc] = k; cnt[k] += 1; surah_cnt[k][loc[0]] += 1; surah_tot[loc[0]] += 1
    root_of[k] = sg['f'].get('ROOT', '')
    lem_forms[k][loc] += 0
TOTAL = sum(cnt.values())
rank = {k: i + 1 for i, (k, _) in enumerate(cnt.most_common())}
first_loc = {}
for loc, k in tok_key.items(): first_loc.setdefault(k, loc)

def norm(s):
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]', '', s)
    return s.replace('ٱ', 'ا').replace('ى', 'ي')
def norm2(s):
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'[\u06D6-\u06DC\u06DE\u06E9]', '', s)   # pause / sajda marks
    return s.replace('\u06E1', '\u0652').replace('\u0670', '').replace('ى', 'ي').replace('ٰ', '')
exact_idx, norm_idx = {}, {}
for loc, t in sorted(tw.items()):
    exact_idx.setdefault(unicodedata.normalize('NFC', t), loc); norm_idx.setdefault(norm2(t), loc)

def wbw_gloss(loc): return wb[loc]['translation']['text'].strip()
def wbw_tr(loc): return wb[loc]['transliteration']['text'].strip()
def audio_of(loc): return '%03d_%03d_%03d' % loc

# ---------------- pattern detection (Quran tokens) ----------------
PRON_P = {'1P': 'na', '2MS': 'ka', '2MP': 'kum', '3MS': 'hu', '3MP': 'hum', '3D': 'huma', '1S': 'i'}
def person(tags):
    for t in tags:
        if re.fullmatch(r'[123](M|F)?(S|D|P)', t): return t
    return None
def patterns_of(segs):
    pats = []
    verb = None; subj_consumed = False
    for sg in segs:
        tags = sg['f'].get('_tags', []); lem = sg['f'].get('LEM', '')
        if 'PREF' in tags:
            if 'DET' in tags: pats.append('al')
            elif lem == 'و': pats.append('wa')
            elif lem == 'ب': pats.append('bi')
            elif lem == 'ل' and 'EMPH' not in tags: pats.append('li')
            elif lem == 'ف': pats.append('fa')
            continue
        if 'SUFF' in tags and 'PRON' in tags:
            p = person(tags)
            if verb and not subj_consumed and p == verb[1] and verb[0] in ('PERF', 'IMPF', 'IMPV'):
                subj_consumed = True; continue
            if p in PRON_P: pats.append(PRON_P[p])
            continue
        if sg['pos'] == 'V':
            asp = 'PERF' if 'PERF' in tags else 'IMPF' if 'IMPF' in tags else 'IMPV' if 'IMPV' in tags else None
            p = person(tags); verb = (asp, p)
            if asp == 'PERF':
                pats += {'2MS': ['you_did'], '1P': ['we_did'], '3MP': ['they_did']}.get(p, [])
            elif asp == 'IMPF':
                pats += {'1P': ['we_do'], '1S': ['i_do'], '3MS': ['ya'], '3MP': ['ya']}.get(p, [])
            elif asp == 'IMPV':
                pats.append('cmd')
            continue
        if sg['pos'] == 'N':
            vf1 = sg['f'].get('VF') == '1'
            if 'ACT_PCPL' in tags and vf1: pats.append('doer')
            if 'PASS_PCPL' in tags and vf1: pats.append('done_to')
            if 'MP' in tags and 'PRON' not in tags and re.search(r'(ين|ون)[ً-ٰٟ]*$', sg['form']): pats.append('plural')
    out = []
    for p in pats:
        if p not in out: out.append(p)
    return out

# ---------------- verse translations ----------------
def load_tr(lang):
    d = json.load(open(f'{SRC}/npm/qj/package/dist/quran_{lang}.json'))
    m = {}
    for ch in d:
        for v in ch['verses']: m[(ch['id'], v['id'])] = v['translation']
    return m
TR_EN, TR_BN = load_tr('en'), load_tr('bn')
CH_EN = {c['id']: c for c in json.load(open(f'{SRC}/npm/qj/package/dist/chapters/en/index.json'))}
CH_BN = {c['id']: c for c in json.load(open(f'{SRC}/npm/qj/package/dist/chapters/bn/index.json'))}

# ---------------- build texts ----------------
problems = []
def quran_line(s, v, a, b):
    allw = sorted(w for (x, y, w) in words if (x, y) == (s, v))
    a = a or 1; b = b or allw[-1]
    bn = T.BN.get(f'{s}:{v}')
    if bn is None: problems.append(f'no BN for {s}:{v}'); bn = []
    if len(bn) == allw[-1] and (a, b) != (1, allw[-1]): bn = bn[a - 1:b]
    if len(bn) != b - a + 1: problems.append(f'BN length mismatch {s}:{v} {len(bn)} vs {b-a+1}')
    toks = []
    for i, w in enumerate(range(a, b + 1)):
        loc = (s, v, w)
        toks.append(dict(ar=tw.get(loc) or ''.join(sg['form'] for sg in words[loc]),
                         en=T.EN_OVERRIDE.get(loc, wbw_gloss(loc)), bn=bn[i] if i < len(bn) else '',
                         key=tok_key[loc], pats=patterns_of(words[loc]), audio=audio_of(loc), tr=wbw_tr(loc),
                         loc=f'{s}:{v}:{w}'))
    full = (a == 1 and b == allw[-1])
    seg_id = f'{s}:{v}' if full else f'{s}:{v}:{a}-{b}'
    if full: en, bn_tr = TR_EN[(s, v)], TR_BN[(s, v)]
    else:
        if seg_id not in T.SEG_TR: problems.append('no SEG_TR ' + seg_id)
        en, bn_tr = T.SEG_TR.get(seg_id, ('', ''))
    return dict(id=seg_id, ref=f'{CH_EN[s]["transliteration"]} {s}:{v}', kind='quran',
                verseAudio='%03d%03d' % (s, v) if full else None, en=en, bn=bn_tr, tokens=toks,
                ar=' '.join(t['ar'] for t in toks))

def hand_line(group, lid):
    l = next(x for x in T.HAND[group] if x['id'] == lid)
    toks = []
    for (ar, en, bn, key, pats) in l['tokens']:
        loc = exact_idx.get(unicodedata.normalize('NFC', ar)) or norm_idx.get(norm2(ar))
        exact = loc is not None
        toks.append(dict(ar=ar, en=en, bn=bn, key=key, pats=pats,
                         audio=audio_of(loc) if loc and exact else None,
                         tr=wbw_tr(loc) if loc and exact else '', loc=None))
    return dict(id=lid, ref='', kind='hand', verseAudio=None, en=l['en'], bn=l['bn'], tokens=toks,
                note_en=l['note_en'], note_bn=l['note_bn'], ar=' '.join(t['ar'] for t in toks))

def build_seg(seg):
    if seg[0] == 'q': return quran_line(*seg[1:])
    return hand_line(seg[1], seg[2])

texts_out = []
for t in T.TEXTS:
    lines = [build_seg(sg) for sg in t['segs']]
    texts_out.append(dict({k: v for k, v in t.items() if k != 'segs'}, lines=lines))
text_by_id = {t['id']: t for t in texts_out}

# ---------------- units & lessons ----------------
known_words, known_pats = set(), set()
units_out = []
for u in T.UNITS:
    if 'segs' in u: lines = [build_seg(sg) for sg in u['segs']]
    else: lines = text_by_id[u['text']]['lines']
    new_words, new_pats, pat_first_word = [], [], {}
    for ln in lines:
        for tk in ln['tokens']:
            k = tk['key']
            if k not in known_words and k not in new_words: new_words.append(k)
            for p in tk['pats']:
                if p not in known_pats and p not in new_pats:
                    new_pats.append(p); pat_first_word[p] = k
    # chunk words into lessons of ~4
    n = len(new_words); chunks = []
    if n <= 5: chunks = [new_words]
    else:
        nl = max(1, round(n / 4)); size = n / nl
        idx = [round(i * size) for i in range(nl + 1)]
        chunks = [new_words[idx[i]:idx[i + 1]] for i in range(nl)]
    lessons = []
    for i, ch in enumerate(chunks):
        lessons.append(dict(id=f'{u["id"]}-l{i+1}', type='learn', words=ch, patterns=[]))
    # attach patterns to the lesson that introduces their first word (max 2 per lesson, overflow forward)
    for p in new_pats:
        fw = pat_first_word[p]
        li = next((i for i, l in enumerate(lessons) if fw in l['words']), len(lessons) - 1)
        while li < len(lessons) - 1 and len(lessons[li]['patterns']) >= 2: li += 1
        lessons[li]['patterns'].append(p)
    lessons.append(dict(id=f'{u["id"]}-final', type='final', words=[], patterns=[]))
    known_words |= set(new_words); known_pats |= set(new_pats)
    units_out.append(dict(id=u['id'], text=u['text'], en=u['en'], bn=u['bn'], completes=u.get('completes'),
                          lines=lines, lessons=lessons, newWords=new_words, newPatterns=new_pats,
                          emoji=text_by_id[u['text']]['emoji']))

# ---------------- words ----------------
all_keys = []
for u in units_out:
    for k in u['newWords']:
        if k not in all_keys: all_keys.append(k)
first_tok = {}
for u in units_out:
    for ln in u['lines']:
        for tk in ln['tokens']:
            if tk['key'] not in first_tok or (first_tok[tk['key']]['audio'] is None and tk['audio']):
                first_tok.setdefault(tk['key'], tk)
                if first_tok[tk['key']]['audio'] is None and tk['audio']: first_tok[tk['key']] = tk

by_root = collections.defaultdict(list)
for k, c in cnt.items():
    r = root_of.get(k)
    if r: by_root[r].append(k)
def lemma_ar(k): return k.split('|')[0] if not k.startswith('PRON:') else k
def family(root, self_key):
    out = []
    for k in sorted(by_root.get(root, []), key=lambda k: -cnt[k]):
        loc = first_loc[k]
        out.append(dict(key=k, ar=lemma_ar(k), count=cnt[k], ex=tw.get(loc, ''), gloss=wbw_gloss(loc),
                        ref=f'{loc[0]}:{loc[1]}', self=(k == self_key)))
    return out[:10]

words_out = {}
for k in all_keys:
    c = content.W.get(k)
    if not c:
        problems.append('no content for word ' + k); c = dict(ar=lemma_ar(k), en='?', bn='?', emoji='', cog={}, tip='', root=None)
    root = c.get('root') or root_of.get(k, '')
    ft = first_tok.get(k, {})
    words_out[k] = dict(key=k, ar=c['ar'], en=c['en'], bn=c['bn'], emoji=c['emoji'], cog=c['cog'], tip=c['tip'],
                        lemma=lemma_ar(k) if not k.startswith('X:') else c['ar'], root=root,
                        rootSpaced=' '.join(root), count=cnt.get(k, 0), rank=rank.get(k),
                        audio=ft.get('audio') or (audio_of(first_loc[k]) if k in first_loc else None), family=family(root, k) if root else [])
unused = [k for k in content.W if k not in words_out]

# ---------------- patterns with examples ----------------
pat_ex = collections.defaultdict(list)
for u in units_out:
    for ln in u['lines']:
        for tk in ln['tokens']:
            for p in tk['pats']:
                if len(pat_ex[p]) < 4 and all(e['ar'] != tk['ar'] for e in pat_ex[p]):
                    pat_ex[p].append(dict(ar=tk['ar'], en=tk['en'], bn=tk['bn'], audio=tk['audio']))
patterns_out = {}
for p in T.PATTERNS:
    patterns_out[p['id']] = dict(p, examples=pat_ex.get(p['id'], []))
used_pats = set(p for u in units_out for p in u['newPatterns'])
for p in used_pats:
    if p not in patterns_out: problems.append('pattern without card: ' + p)

course = dict(totalTokens=TOTAL, words=words_out, patterns=patterns_out,
              texts=[dict({k: v for k, v in t.items()}) for t in texts_out], units=units_out)

# ---------------- coverage ----------------
surahs = []
for n in range(1, 115):
    surahs.append(dict(n=n, ar=CH_EN[n]['name'], tr=CH_EN[n]['transliteration'], en=CH_EN[n]['translation'],
                       bn=CH_BN[n]['translation'], verses=CH_EN[n]['total_verses'], total=surah_tot[n]))
lemma_surah = {k: sorted(surah_cnt[k].items()) for k in words_out if k in surah_cnt}
coverage = dict(totalTokens=TOTAL, surahs=surahs, lemmaSurah=lemma_surah)

os.makedirs(f'{OUT}/src/data', exist_ok=True); os.makedirs(f'{OUT}/public/quran', exist_ok=True)
# Tanzil uses U+065E for open dammatan; fonts implement the standard U+08F1
def dump(obj, path):
    open(path, 'w').write(json.dumps(obj, ensure_ascii=False, separators=(',', ':')).replace('\u065e', '\u08f1'))
dump(course, f'{OUT}/src/data/course.json')
json.dump(coverage, open(f'{OUT}/src/data/coverage.json', 'w'), ensure_ascii=False, separators=(',', ':'))

# ---------------- reader files ----------------
lem_list = [k for k, _ in cnt.most_common()]
lem_idx = {k: i for i, k in enumerate(lem_list)}
json.dump([[k, lemma_ar(k), root_of.get(k, ''), cnt[k]] for k in lem_list],
          open(f'{OUT}/public/quran/lemmas.json', 'w'), ensure_ascii=False, separators=(',', ':'))
for n in range(1, 115):
    vs = []
    for v in range(1, CH_EN[n]['total_verses'] + 1):
        ws = sorted(w for (x, y, w) in words if x == n and y == v) if False else None
        vs.append(v)
    out = []
    by_v = collections.defaultdict(list)
    for loc, segs in words.items():
        if loc[0] == n: by_v[loc[1]].append(loc)
    for v in sorted(by_v):
        out.append(dict(v=v, en=TR_EN[(n, v)], bn=TR_BN[(n, v)],
                        w=[[tw.get(l) or ''.join(sg['form'] for sg in words[l]), wbw_gloss(l), wbw_tr(l), lem_idx[tok_key[l]]]
                           for l in sorted(by_v[v])]))
    dump(dict(n=n, verses=out), f'{OUT}/public/quran/{n}.json')

# ---------------- report ----------------
print('total tokens', TOTAL, '| curriculum words', len(words_out), '| patterns', len(used_pats))
for u in units_out:
    print(u['id'], u['en'], '| words', len(u['newWords']), '| lessons', [(l['id'], len(l['words']), l['patterns']) for l in u['lessons']])
cov = sum(cnt.get(k, 0) for k in words_out)
print('coverage if all learned: %.1f%%' % (100 * cov / TOTAL))
print('unused content keys:', unused)
print('PROBLEMS:', *problems, sep='\n  ')
