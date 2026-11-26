# -*- coding: utf-8 -*-
"""Build app data from Quran sources + hand-authored content.
Outputs:
  OUT/src/data/course.json    — words, patterns, texts (with tokens), units (with lessons)
  OUT/src/data/coverage.json  — surah list + per-surah counts of curriculum words
  OUT/public/quran/N.json     — every surah word-by-word for the reader
  OUT/public/quran/lemmas.json
"""
import json, os, sys, re, unicodedata, collections
from load import load, stem, load_indopak
import content, texts as T
content.W = {unicodedata.normalize('NFC', k): v for k, v in content.W.items()}
for grp in T.HAND.values():
    for l in grp:
        l['tokens'] = [(a, e, b, unicodedata.normalize('NFC', k) if k else k, p) for (a, e, b, k, p) in l['tokens']]

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(os.path.join(HERE, '..', '..'))
from load import SRC
words, wb, tw, qj = load()
IP = load_indopak(words)
import ip_manual
ip_manual.IP = {unicodedata.normalize('NFC', k): v for k, v in ip_manual.IP.items()}
from indopak_convert import convert as to_indopak
def ip_word(loc):
    t = IP.get(loc)
    return t.split(' ')[0] if t else None

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
                         loc=f'{s}:{v}:{w}', ip=IP.get(loc)))
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
        ipt = ip_manual.IP.get(unicodedata.normalize('NFC', ar)) or (ip_word(loc) if loc else None) or to_indopak(ar, standalone=not toks)
        if not ipt: problems.append('no IndoPak for hand token ' + ar)
        toks.append(dict(ar=ar, en=en, bn=bn, key=key, pats=pats,
                         audio=audio_of(loc) if loc and exact else None,
                         tr=wbw_tr(loc) if loc and exact else '', loc=None, ip=ipt))
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

# ---------------- everyday sentences ----------------
def everyday_line(e):
    toks = []
    for (ar, en, bn, key, pats) in e['tokens']:
        key = unicodedata.normalize('NFC', key) if key else key
        loc = exact_idx.get(unicodedata.normalize('NFC', ar)) or norm_idx.get(norm2(ar))
        toks.append(dict(ar=ar, en=en, bn=bn, key=key, pats=pats, audio=audio_of(loc) if loc else None,
                         tr=wbw_tr(loc) if loc else '', loc=None,
                         ip=ip_manual.IP.get(unicodedata.normalize('NFC', ar)) or to_indopak(ar, standalone=not toks)))
    return dict(id=e['id'], ref='', kind='everyday', verseAudio=None, en=e['en'], bn=e['bn'], tokens=toks,
                ar=' '.join(t['ar'] for t in toks))
EVERYDAY = {e['id']: everyday_line(e) for e in T.EVERYDAY}
STRUCT_BY_UNIT = collections.defaultdict(list)
for st in T.STRUCTURES: STRUCT_BY_UNIT[st['unit']].append(st)

# verse -> distinct stem-lemma keys (for "new verses" and the readable-verses count)
verse_keys = collections.defaultdict(list)
for loc in sorted(words): verse_keys[loc[:2]].append(tok_key[loc])
curriculum_verses = set()
for t in T.TEXTS:
    for sg in t['segs']:
        if sg[0] == 'q': curriculum_verses.add((sg[1], sg[2]))
for st in T.STRUCTURES:
    for sg in st['quran']: curriculum_verses.add((sg[1], sg[2]))
used_new_verses = set()
used_verse_texts = set()

def reader_line(s, v, known):
    """A Quran verse outside the curriculum, for 'read a new verse'."""
    toks = []
    allw = sorted(w for (x, y, w) in words if (x, y) == (s, v))
    for w in allw:
        loc = (s, v, w); k = tok_key[loc]
        toks.append(dict(ar=tw.get(loc) or ''.join(sg['form'] for sg in words[loc]), en=T.EN_OVERRIDE.get(loc, wbw_gloss(loc)),
                         bn='', key=k, pats=patterns_of(words[loc]), audio=audio_of(loc), tr=wbw_tr(loc),
                         loc=f'{s}:{v}:{w}', ip=IP.get(loc), known=k in known))
    return dict(id=f'{s}:{v}', ref=f'{CH_EN[s]["transliteration"]} {s}:{v}', kind='quran', verseAudio='%03d%03d' % (s, v),
                en=TR_EN[(s, v)], bn=TR_BN[(s, v)], tokens=toks, ar=' '.join(t['ar'] for t in toks), newVerse=True)

def pick_new_verses(known, unit_words, n=3):
    cands = []
    for (s, v), ks in verse_keys.items():
        if (s, v) in curriculum_verses or (s, v) in used_new_verses: continue
        L = len(ks)
        if L < 3 or L > 12: continue
        unknown = [k for k in ks if k not in known]
        if len(set(unknown)) > 2 or (L - len(unknown)) / L < 0.7: continue
        rel = sum(1 for k in ks if k in unit_words)
        cands.append((len(set(unknown)), -rel, L, s, v))
    cands.sort()
    out, surahs = [], set()
    for c in cands:
        txt = norm(' '.join(tw.get((c[3], c[4], w), '') for w in range(1, 40)))
        if c[3] in surahs or txt in used_verse_texts: continue
        out.append((c[3], c[4])); surahs.add(c[3]); used_verse_texts.add(txt)
        if len(out) == n: break
    return out

def chunk_words(new_words):
    n = len(new_words)
    if n <= 5: return [new_words] if n else []
    nl = max(1, round(n / 4)); size = n / nl
    idx = [round(i * size) for i in range(nl + 1)]
    return [new_words[idx[i]:idx[i + 1]] for i in range(nl)]

# ---------------- units & lessons ----------------
known_words, known_pats = set(), set()
units_out = []
for u in T.UNITS:
    if 'segs' in u: lines = [build_seg(sg) for sg in u['segs']]
    else: lines = text_by_id[u['text']]['lines']
    new_words, new_pats, pat_first_word = [], [], {}
    def collect(toks, bucket):
        for tk in toks:
            k = tk['key']
            if k not in known_words and k not in new_words and k not in bucket: bucket.append(k)
            for p in tk['pats']:
                if p not in known_pats and p not in new_pats:
                    new_pats.append(p); pat_first_word[p] = k
    for ln in lines: collect(ln['tokens'], new_words)
    lessons = [dict(id=f'{u["id"]}-l{i+1}', type='learn', words=ch, patterns=[]) for i, ch in enumerate(chunk_words(new_words))]
    # structure lessons: their everyday sentences may bring a few new (Quranic) words
    structures = []
    for st in STRUCT_BY_UNIT.get(u['id'], []):
        st_words = []
        ev_lines = [EVERYDAY[e] for e in st['everyday']]
        for ln in ev_lines: collect(ln['tokens'], st_words)
        new_words += st_words
        q_lines = [build_seg(sg) for sg in st['quran']]
        structures.append(dict(id=st['id'], en=st['en'], bn=st['bn'], emoji=st['emoji'],
                               shape=[dict(ar=a, en=e, bn=b, role=r) for (a, e, b, r) in st['shape']],
                               expl_en=st['expl_en'], expl_bn=st['expl_bn'],
                               notes=[dict(en=a, bn=b) for (a, b) in T.STRUCTURE_NOTES.get(st['id'], [])],
                               quran=q_lines, everyday=ev_lines,
                               chunk=build_seg(st['chunk']) if st.get('chunk') else None))
        parts = [st_words] if len(st_words) <= 5 else [st_words[:4], st_words[4:]]
        for pi, pw in enumerate(parts):
            lessons.append(dict(id=f'{u["id"]}-s-{st["id"]}' + (f'-{pi+1}' if len(parts) > 1 else ''), type='structure',
                                structure=st['id'], part=pi + 1, parts=len(parts), words=pw, patterns=[]))
        if st.get('chunk'):
            ck = [t['key'] for t in structures[-1]['chunk']['tokens']]
            found = []
            for (vs, vv), ks in sorted(verse_keys.items(), key=lambda x: len(x[1])):
                if (vs, vv) in curriculum_verses or len(ks) > 16: continue
                if not any(ks[i:i + len(ck)] == ck for i in range(len(ks) - len(ck) + 1)): continue
                unknown = set(k for k in ks if k not in known_words and k not in new_words and k not in ck)
                if len(unknown) <= 3: found.append((len(unknown), vs, vv))
            found.sort()
            structures[-1]['chunkVerses'] = [reader_line(vs, vv, known_words | set(new_words)) for (_, vs, vv) in found[:3]]
            structures[-1]['chunkCount'] = sum(1 for ks in verse_keys.values() if any(ks[i:i + len(ck)] == ck for i in range(len(ks) - len(ck) + 1)))
    # attach patterns to the lesson that introduces their first word (max 2 per lesson, overflow forward)
    for p in new_pats:
        fw = pat_first_word[p]
        li = next((i for i, l in enumerate(lessons) if fw in l['words']), len(lessons) - 1)
        while li < len(lessons) - 1 and len(lessons[li]['patterns']) >= 2: li += 1
        lessons[li]['patterns'].append(p)
    lessons.append(dict(id=f'{u["id"]}-final', type='final', words=[], patterns=[]))
    known_words |= set(new_words); known_pats |= set(new_pats)
    # read new verses the learner can now (mostly) understand
    picks = pick_new_verses(known_words, set(new_words))
    new_verses = []
    for (s, v) in picks:
        used_new_verses.add((s, v)); new_verses.append(reader_line(s, v, known_words))
    if new_verses:
        lessons.append(dict(id=f'{u["id"]}-v', type='verses', words=[], patterns=[]))
    units_out.append(dict(id=u['id'], text=u['text'], en=u['en'], bn=u['bn'], completes=u.get('completes'),
                          lines=lines, lessons=lessons, newWords=new_words, newPatterns=new_pats,
                          structures=structures, newVerses=new_verses,
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

def pos_of(sg):
    tags = sg['f'].get('_tags', [])
    if 'PRON' in tags and 'LEM' not in sg['f']: return 'pron'
    if sg['pos'] == 'V': return 'verb'
    if sg['pos'] == 'P': return 'particle'
    for t, n in (('DEM', 'dem'), ('REL', 'rel'), ('PN', 'name'), ('ADJ', 'adj'), ('ACT_PCPL', 'adj'), ('PASS_PCPL', 'adj'), ('PRON', 'pron')):
        if t in tags: return n
    return 'noun'
POS = {}
for loc, segs in words.items():
    k = tok_key[loc]
    if k not in POS: POS[k] = pos_of(stem(segs))
POS.update({'X:hayya': 'particle', 'X:hamida': 'verb', 'X:falah': 'noun'})
by_root = collections.defaultdict(list)
for k, c in cnt.items():
    r = root_of.get(k)
    if r: by_root[r].append(k)
def lemma_ar(k): return k.split('|')[0] if not k.startswith('PRON:') else k
def family(root, self_key):
    out = []
    for k in sorted(by_root.get(root, []), key=lambda k: -cnt[k]):
        loc = first_loc[k]
        out.append(dict(key=k, ar=lemma_ar(k), count=cnt[k], ex=tw.get(loc, ''), exIp=ip_word(loc), gloss=wbw_gloss(loc),
                        ref=f'{loc[0]}:{loc[1]}', self=(k == self_key)))
    return out[:10]

words_out = {}
for k in all_keys:
    c = content.W.get(k)
    if not c:
        problems.append('no content for word ' + k); c = dict(ar=lemma_ar(k), en='?', bn='?', emoji='', cog={}, tip='', root=None)
    root = c.get('root') or root_of.get(k, '')
    ft = first_tok.get(k, {})
    pos = POS.get(k) or c.get('pos') or 'noun'
    words_out[k] = dict(key=k, pos=pos, ar=c['ar'], en=c['en'], bn=c['bn'], emoji=c['emoji'], cog=c['cog'], tip=c['tip'],
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
                    pat_ex[p].append(dict(ar=tk['ar'], ip=tk.get('ip'), en=tk['en'], bn=tk['bn'], key=tk['key'], audio=None))
patterns_out = {}
for p in T.PATTERNS:
    more = T.PATTERN_MORE.get(p['id'], ('', ''))
    patterns_out[p['id']] = dict(p, examples=pat_ex.get(p['id'], []), more_en=more[0], more_bn=more[1])
used_pats = set(p for u in units_out for p in u['newPatterns'])
for p in used_pats:
    if p not in patterns_out: problems.append('pattern without card: ' + p)

# ---------------- Uthmani -> IndoPak map for every Arabic string the app shows ----------------
AR2IP = {}
norm_quran = {}
for loc, t in tw.items():
    if loc in IP: norm_quran.setdefault(unicodedata.normalize('NFC', t), ip_word(loc))
converted = {}
def ip_for(s):
    s = s.strip()
    if unicodedata.normalize('NFC', s) in ip_manual.IP: return ip_manual.IP[unicodedata.normalize('NFC', s)]
    v = norm_quran.get(unicodedata.normalize('NFC', s))
    if v: return v
    if re.search('[\u0621-\u064A\u0671]', s):
        converted[s] = to_indopak(s, standalone=not s.startswith('ـ'))
        return converted[s]
    return None
all_lines = [ln for t in texts_out for ln in t['lines']]
for u in units_out:
    all_lines += u['lines'] + u['newVerses']
    for st in u['structures']:
        all_lines += st['quran'] + st['everyday'] + st.get('chunkVerses', []) + ([st['chunk']] if st.get('chunk') else [])
for ln in all_lines:
    for tk in ln['tokens']:
        if tk.get('ip') and tk['ar'] not in AR2IP: AR2IP[tk['ar']] = tk['ip']
missing_ip = []
def need(s):
    for part in s.split(' / '):
        part = part.strip()
        if not part or part in AR2IP: continue
        v = ip_for(part)
        if v: AR2IP[part] = v
        else: missing_ip.append(part)
for k, w in words_out.items(): need(w['ar'])
for p in patterns_out.values():
    need(p['ar'])
    for e in p['examples']: need(e['ar'])
ARAB_RUN = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+(?:\s+[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+)*')
extra_txt = [x for pair in T.PATTERN_MORE.values() for x in pair] + [x for notes in T.STRUCTURE_NOTES.values() for pair in notes for x in pair]
extra_txt += [x for st in T.STRUCTURES for x in (st['expl_en'], st['expl_bn'])]
for txt in [w['tip'] for w in words_out.values()] + [p['expl_en'] for p in T.PATTERNS] + [p['expl_bn'] for p in T.PATTERNS] + extra_txt:
    for run in ARAB_RUN.findall(txt):
        for part in run.split():
            if len(part) > 1 and part not in AR2IP:
                v = ip_for(part)
                if v: AR2IP[part] = v
                elif not re.fullmatch(r'[\u0621-\u064A]', part): missing_ip.append(part)
if missing_ip: problems.append('no IndoPak for: ' + ' | '.join(sorted(set(missing_ip))))
json.dump(converted, open(os.path.join(HERE, 'indopak_converted_review.json'), 'w'), ensure_ascii=False, indent=0)

course = dict(totalTokens=TOTAL, ip=AR2IP, words=words_out, patterns=patterns_out,
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
                        w=[[tw.get(l) or ''.join(sg['form'] for sg in words[l]), wbw_gloss(l), wbw_tr(l), lem_idx[tok_key[l]], IP.get(l, '')]
                           for l in sorted(by_v[v])]))
    dump(dict(n=n, verses=out), f'{OUT}/public/quran/{n}.json')

json.dump([[s_, v_, sorted(set(lem_idx[k] for k in ks))] for (s_, v_), ks in sorted(verse_keys.items())],
          open(f'{OUT}/public/quran/verse-lemmas.json', 'w'), separators=(',', ':'))

# ---------------- report ----------------
print('total tokens', TOTAL, '| curriculum words', len(words_out), '| patterns', len(used_pats))
for u in units_out:
    print(u['id'], u['en'], '| words', len(u['newWords']), '| lessons', [(l['id'], len(l['words']), l['patterns']) for l in u['lessons']], '| new verses', [nv['id'] for nv in u['newVerses']])
cov = sum(cnt.get(k, 0) for k in words_out)
print('coverage if all learned: %.1f%%' % (100 * cov / TOTAL))
print('unused content keys:', unused)
print('PROBLEMS:', *problems, sep='\n  ')
