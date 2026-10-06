#!/usr/bin/env python3
"""New, read-only replay audit. Does not re-fit keys or certify manuscript truth.
Run from this reading packet: python3 replay.py
"""
from pathlib import Path
import json,csv,hashlib,re,string,sys
P=Path(__file__).resolve().parent
E=P/'evidence' if (P/'evidence').exists() else P/'repro_inventory_core'
REPORT={}
def txt(p):return p.read_text(encoding='utf-8')
def js(p):return json.loads(txt(p))
def sha(b):return hashlib.sha256(b).hexdigest()
def record(topic,**kw):REPORT[topic]={'status':'PASS','scope':'mechanical replay only',**kw}

if sys.flags.optimize:
 raise SystemExit('Run normal Python; assertion checks must remain enabled.')

# Malsburg: use the retained input directly, independently of the historical runner.
m=E/'Malsburg_1637_evidence_and_code/Malsburg_1637/cryptanalysis'
a='abcdefghiklmnopqrstuwxyz'; shifts=(4,5,3,6,2)
c=txt(m/'normalized_ciphertext.txt').strip();p=txt(m/'literal_plaintext.txt').strip()
out=''.join(a[(a.index(x)-shifts[i%5])%24] for i,x in enumerate(c))
assert len(c)==510 and out==p
assert sha(c.encode())=='c9fd887a1db86f327b5d68cc0ad3bdaff27356e37bf142b0d056f95ae2460d29'
assert sha(out.encode())=='16f6843b74bd7703d2ad64129a795c863e753904af7d6c5f590cbd54e952f10d'
assert ''.join(a[(a.index(x)+shifts[i%5])%24] for i,x in enumerate(out))==c
branches=[]
for line in txt(m/'inputs/reviewed_variant_ensemble.jsonl').splitlines():
 v=json.loads(line);ass=v['assumptions']
 if ass['cancelled_patch_slots']==0 and ass['numeral_groups']=='omit' and ass['angular_pairs']=='omit':
  s=''.join(t['value'].replace('ü','u').replace('ÿ','y') for t in v['tokens'])
  assert s==c; branches.append(v['variant_id'])
record('malsburg-1637',positions=510,ciphertext_sha256=sha(c.encode()),literal_sha256=sha(p.encode()),compatible_visual_variants=branches,historical_branch1_dependency_present=(m/'alphabet.json').exists())

print(json.dumps(REPORT,ensure_ascii=False,indent=2))
