#!/bin/bash
# 사용: ./mk.sh <부> <화> <파일이름> — build/p<부>e<화>_*.txt 합쳐 docx+pdf
cd "$(dirname "$0")/.."
P=$1; N=$2; STEM=$3
cat build/p${P}e${N}_[a-z].txt > build/p${P}e${N}.txt
python3 build/build.py build/p${P}e${N}.txt . "$STEM"
soffice --headless --convert-to pdf --outdir pdf "docx/${STEM}.docx" >/dev/null 2>&1
ls pdf/"${STEM}.pdf" >/dev/null && pdfinfo "pdf/${STEM}.pdf" | grep Pages
