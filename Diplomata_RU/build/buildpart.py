#!/usr/bin/env python3
"""python3 build/buildpart.py <부> : 해당 부의 모든 화를 docx+pdf로 변환"""
import sys,re,subprocess,glob
P=sys.argv[1]
tr=dict(zip("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",["a","b","v","g","d","e","e","zh","z","i","y","k","l","m","n","o","p","r","s","t","u","f","kh","ts","ch","sh","shch","","y","","e","yu","ya"]))
def tl(s): return re.sub(r'[^A-Za-z0-9_]+','_',''.join(tr.get(c,c) for c in s.lower())).strip('_').capitalize()
for n in range(1,13):
    f=f'build/p{P}e{n}_a.txt'
    try: t=open(f,encoding='utf-8').read()
    except: continue
    title=re.search(r'^@title (.+)$',t,re.M).group(1)
    stem=f'{P}부{n}화_{tl(title)}'
    r=subprocess.run(['build/mk.sh',P,str(n),stem],capture_output=True,text=True)
    print(stem,r.stdout.strip().replace('\n',' '),r.stderr.strip()[:100])
