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
echo "Sources ready in $(pwd)/.."
