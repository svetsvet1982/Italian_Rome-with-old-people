#!/usr/bin/env python3
"""원고 점검: python3 check.py p1e1_a.txt p1e1_b.txt ... (한 화의 파일들을 순서대로)"""
import re,sys
pat=re.compile(r'^([^:|]{1,30}):\s*(.+?)\s*\|\|\|\s*(.+)$')
turns=0;bad=[];speakers=set();secs=0;ann=0
for f in sys.argv[1:]:
    for i,l in enumerate(open(f,encoding='utf-8'),1):
        l=l.rstrip('\n')
        if not l.strip() or l.startswith('@') or l.startswith('+ '): 
            if l.startswith('+ '): ann+=1
            continue
        if l.startswith('## '): secs+=1; continue
        m=pat.match(l)
        if m: turns+=1; speakers.add(m.group(1))
        else: bad.append((f,i,l[:80]))
print('turns',turns,'sections',secs,'annotations',ann,'speakers',sorted(speakers))
for b in bad: print('BAD',b)
if not re.search(r'[А-Яа-я]',open(sys.argv[1],encoding='utf-8').read()): print('NO CYRILLIC')
