#!/bin/bash
# 사용: ./mk.sh <화번호> <파일이름> — build/ep<N>_*.txt 를 합쳐 docx+pdf 생성
cd "$(dirname "$0")/.."
N=$1; STEM=$2
cat build/ep${N}_[a-z].txt > build/ep${N}.txt
python3 build/build.py build/ep${N}.txt . "$STEM"
soffice --headless --convert-to pdf --outdir pdf "docx/${STEM}.docx" >/dev/null 2>&1
ls pdf/"${STEM}.pdf" >/dev/null && pdfinfo "pdf/${STEM}.pdf" | grep Pages
