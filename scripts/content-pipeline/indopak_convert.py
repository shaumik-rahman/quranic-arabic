# -*- coding: utf-8 -*-
"""Convert Tanzil Uthmani spelling to QUL/quran.com IndoPak Nastaleeq spelling.
Only used for short teaching forms that don't occur verbatim in the Quran; real Quran words always
come from the IndoPak text itself. `python3 indopak_convert.py` measures accuracy against every Quran word."""
import re, unicodedata

FATHA, DAMMA, KASRA, SUKUN, SHADDA, DAGGER = 'َ', 'ُ', 'ِ', 'ْ', 'ّ', 'ٰ'
MARKS = 'ً-ْٰٓ-ٗۤ'
PAUSE = re.compile('[ۖ-ۜ۞۟۠۩-]')
CONS = 'ب-غف-ه'   # consonants that take an explicit sukun


def convert(s, standalone=False):
    lead = 'ـ' if s.startswith('ـ') else ''
    trail = 'ـ' if s.endswith('ـ') else ''
    bare_end = bool(re.search('[ء-ي]$', s))   # teaching form without a final vowel
    s = unicodedata.normalize('NFD', s)
    s = PAUSE.sub('', s).replace('ـ', '')
    s = s.replace('ۡ', SUKUN)
    # Allah / lillah
    s = re.sub('ٱلل[' + MARKS + ']*ه', 'اللّٰه', s)
    if standalone and s.startswith('اللّٰه'): s = 'اَ' + s[1:]   # Allah at the start of a phrase: اَللّٰهُ
    s = re.sub('لِل[' + MARKS + ']*ه', 'لِلّٰه', s)
    # tanween: iqlab small meem and Tanzil "open" tanween
    s = s.replace(FATHA + 'ۢ', 'ً').replace(DAMMA + 'ۢ', 'ٌ').replace(KASRA + 'ۭ', 'ٍ')
    s = s.replace('ٞ', 'ٌ').replace('ٗ', 'ً').replace('ٖ', 'ٍ')
    s = s.replace('ۢ', '').replace('ۭ', '')
    # hu / hi with small waw / yeh -> inverted damma / subscript alif
    s = s.replace('ه' + DAMMA + 'ۥ', 'هٗ').replace('ه' + KASRA + 'ۦ', 'هٖ')
    s = s.replace('ۥ', '').replace('ۦ', '')
    # madd
    s = s.replace('ء' + FATHA + 'ا', 'اٰ')                    # ءَا -> اٰ
    s = re.sub('ا[' + FATHA + ']?ٔٓ', 'اٰ', s)           # أٓ -> اٰ
    s = re.sub('آ(?=[ءئؤ])', 'آ', s)               # madd before hamza: آ
    s = re.sub('آ', 'اۤ', s)                                  # other madd on alif: اۤ
    # hamza on alif -> bare alif keeping its vowel (NFD puts the vowel before the hamza)
    s = re.sub('(ا[ً-ْ]*)[ٕٔ]', r'\1', s)
    # alif wasla
    if standalone:
        s = re.sub('^ٱ(?=ل)', 'ا' + FATHA, s)
        s = re.sub('^ٱ', 'ا' + KASRA, s)
    s = s.replace('ٱ', 'ا')
    # dagger alif
    s = re.sub(FATHA + 'و' + DAGGER, DAGGER + 'و', s)                                   # salah
    s = re.sub(FATHA + '(' + SHADDA + '?)ى' + DAGGER + 'ٓ', r'\1' + DAGGER + 'ۤى', s)
    s = re.sub(FATHA + '(' + SHADDA + '?)ى' + DAGGER, r'\1' + DAGGER + 'ى', s)           # ـَىٰ -> ـٰی
    s = re.sub(FATHA + '(' + SHADDA + '?)' + DAGGER, r'\1' + DAGGER, s)
    s = s.replace('ٓ', 'ۤ')
    # Farsi yeh
    s = s.replace('ي', 'ی').replace('ى', 'ی')
    # long ī / ū carry a sukun
    s = re.sub('(' + KASRA + '|' + KASRA + SHADDA + '|' + SHADDA + KASRA + ')ی(?![ً-ْٰٓ-ٗ])', r'\1ی' + SUKUN, s)
    s = re.sub('(' + DAMMA + '|' + DAMMA + SHADDA + '|' + SHADDA + DAMMA + ')و(?![ً-ْٰٓ-ٗ])', r'\1و' + SUKUN, s)
    s = s.replace('ا' + SUKUN, 'ا')  # silent alif of ...ُوا
    # bare consonants (ikhfa / idgham / word-final) get a sukun
    out, chars = [], list(s)
    for i, ch in enumerate(chars):
        out.append(ch)
        if not re.match('[' + CONS + ']', ch) or ch == 'ة':
            continue
        nxt = chars[i + 1] if i + 1 < len(chars) else ''
        if nxt and re.match('[' + MARKS + ']', nxt):
            continue
        if ch == 'ل':
            if SHADDA in ''.join(chars[i + 2:i + 4]):  # al- / lil- + sun letter (assimilated)
                continue
            if nxt == 'ل':  # Allah
                continue
        out.append(SUKUN)
    res = ''.join(out).strip()
    if standalone and bare_end and res.endswith(SUKUN):
        res = res[:-1]
    return lead + unicodedata.normalize('NFC', res) + trail


def canon(s):
    s = PAUSE.sub('', s).replace('ـ', '').split(' ')[0]
    return unicodedata.normalize('NFC', unicodedata.normalize('NFD', s))


def test_convert(show=25):
    import sys, collections
    sys.path.insert(0, '.')
    from load import load, load_indopak
    words, wb, tw, q = load()
    IP = load_indopak(words)
    ok = n = 0
    bad = collections.Counter()
    for loc, ip in IP.items():
        if loc not in tw:
            continue
        n += 1
        if canon(convert(tw[loc])) == canon(ip):
            ok += 1
        else:
            bad[(tw[loc], canon(ip))] += 1
    print(f'exact {ok}/{n} = {100 * ok / n:.1f}%')
    for (u, i), c in bad.most_common(show):
        print(c, u, '->', convert(u), '| want', i)


if __name__ == '__main__':
    test_convert()
