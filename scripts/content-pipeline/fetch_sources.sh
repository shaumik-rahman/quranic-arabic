#!/usr/bin/env bash
# Downloads the open Quran datasets the content pipeline needs into ./sources
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p sources/npm && cd sources
curl -sL -o morph.txt https://raw.githubusercontent.com/mustafa0x/quran-morphology/master/quran-morphology.txt
cd npm
npm pack -q @kmaslesa/holy-quran-word-by-word-full-data@1.0.6 quran-json@3.1.2 >/dev/null
mkdir -p wbw qj
tar xzf kmaslesa-holy-quran-word-by-word-full-data-1.0.6.tgz -C wbw
tar xzf quran-json-3.1.2.tgz -C qj
# IndoPak Nastaleeq text (quran.com / QUL), via github.com/quran8vs/IndoPak
curl -sL -o ../indopak.json https://raw.githubusercontent.com/quran8vs/IndoPak/main/data/db_font1.json
# Bangla word-by-word glosses: github.com/SadaqaWorks/Word-By-Word-Quran-Android (MIT), extracted to bn_wbw.json
tmp=$(mktemp -d)
git clone -q --depth 1 https://github.com/SadaqaWorks/Word-By-Word-Quran-Android "$tmp/wbw"
python3 -I -c "
import sqlite3, json, sys
c = sqlite3.connect('file:' + sys.argv[1] + '?mode=ro', uri=True)
d = {f'{s}:{v}:{w}': (bn or '').strip() for s, v, w, bn in c.execute('select surah_id, verse_id, words_id, translate_bn from bywords')}
json.dump(d, open(sys.argv[2], 'w'), ensure_ascii=False, separators=(',', ':'))
" "$tmp/wbw/app/src/main/assets/databases/wordbyword.db" ../bn_wbw.json
rm -rf "$tmp"
echo "Sources ready in $(pwd)/.."
