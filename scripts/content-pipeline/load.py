import json, collections, re
import os
SRC=os.environ.get('QA_SOURCES', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sources'))
def feats(f):
    d={}
    for p in f.split('|'):
        if ':' in p: k,v=p.split(':',1); d[k]=v
        else: d.setdefault('_tags',[]).append(p)
    return d
def load():
    words=collections.OrderedDict()
    for line in open(f'{SRC}/morph.txt',encoding='utf-8'):
        loc,form,tag,feat=line.rstrip('\n').split('\t')
        s,v,w,seg=map(int,loc.split(':'))
        words.setdefault((s,v,w),[]).append(dict(form=form,pos=tag,f=feats(feat),raw=feat))
    d=json.load(open(f'{SRC}/npm/wbw/package/data.json'))
    wb={}
    for page in d:
        for a in page['ayahs']:
            for x in a['words']:
                if x and x['char_type_name']=='word':
                    s,v=map(int,x['parentAyahVerseKey'].split(':'))
                    wb[(s,v,x['position'])]=x
    q=json.load(open(f'{SRC}/npm/qj/package/dist/quran.json'))
    tw={}
    for ch in q:
        for vv in ch['verses']:
            for i,t in enumerate(vv['text'].split(' '),1): tw[(ch['id'],vv['id'],i)]=t
    return words,wb,tw,q
def stem(segs):
    # first segment that's not a prefix and not a suffix
    for sg in segs:
        tags=sg['f'].get('_tags',[])
        if 'PREF' in tags or 'SUFF' in tags: continue
        return sg
    return segs[0]
def lemkey(sg):
    return sg['f'].get('LEM','?')+'|'+sg['f'].get('ROOT','')

def load_indopak(words):
    """IndoPak Nastaleeq text (quran.com / QUL) split into words aligned with the corpus.
    Pause marks (tokens without letters) are attached to the preceding word."""
    import json, re, collections
    path = os.path.join(SRC, 'indopak.json')
    if not os.path.exists(path): return {}
    d = json.load(open(path, encoding='utf-8'))
    LET = re.compile(r'[ء-يٱ-ۓۺ-ۿ]')
    cnt = collections.Counter((a, b) for (a, b, c) in words)
    ip = {}
    for k, t in d.items():
        s, v = map(int, k.split(':'))
        out = []
        for tok in t.split():
            if LET.search(tok) or not out: out.append(tok)
            else: out[-1] += ' ' + tok
        if len(out) != cnt[(s, v)]: continue  # 7 verses split differently: no IndoPak for them
        for i, w in enumerate(out, 1): ip[(s, v, i)] = w
    return ip
