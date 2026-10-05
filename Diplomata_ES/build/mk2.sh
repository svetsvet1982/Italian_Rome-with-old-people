#!/bin/bash
# 사용: ./mk2.sh <화번호> <파일이름> — 2부 원고(p2e<N>_*.txt) → docx+pdf
cd "$(dirname "$0")/.."
N=$1; STEM=$2
cat build/p2e${N}_[a-z].txt > build/p2e${N}.txt
python3 build/build.py build/p2e${N}.txt . "$STEM"
soffice --headless --convert-to pdf --outdir pdf "docx/${STEM}.docx" >/dev/null 2>&1
ls pdf/"${STEM}.pdf" >/dev/null && pdfinfo "pdf/${STEM}.pdf" | grep Pages
