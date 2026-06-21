#!/usr/bin/env python3
"""Compact vault linter: broken wikilinks, case-insensitive basename collisions,
empty files. Read-only. Reusable."""
import os, re
from collections import defaultdict
ROOT = r"C:\Users\chris and christine\Desktop\Research"
DIRS = ["wiki","sources","manuscripts","templates","inbox"]
WL = re.compile(r"\[\[([^\]]+)\]\]")

def strip_code(t):
    t = re.sub(r"```.*?```","",t,flags=re.S)
    return re.sub(r"`[^`]*`","",t)
def split_fm(t):
    if not t.startswith("---"): return ""
    e=t.find("\n---",3); return t[3:e] if e!=-1 else ""
def aliases_of(fm):
    out=[]; lines=fm.split("\n")
    for i,l in enumerate(lines):
        m=re.match(r"^aliases:\s*(.*)$",l)
        if not m: continue
        rest=m.group(1).strip()
        if rest.startswith("["):
            out+=[p.strip().strip("'\"") for p in rest.strip("[]").split(",") if p.strip()]
        else:
            j=i+1
            while j<len(lines):
                bm=re.match(r"^\s*-\s+(.+?)\s*$",lines[j])
                if bm: out.append(bm.group(1).strip().strip("'\"")); j+=1
                else: break
    return out

files=[]
for d in DIRS:
    for dp,_,fn in os.walk(os.path.join(ROOT,d)):
        for f in fn:
            if f.endswith(".md"): files.append(os.path.join(dp,f))
for f in os.listdir(ROOT):
    if f.endswith(".md"): files.append(os.path.join(ROOT,f))

names=defaultdict(list); aliasmap=defaultdict(list); wc={}
for p in files:
    t=open(p,encoding="utf-8").read()
    base=os.path.splitext(os.path.basename(p))[0]
    names[base.lower()].append(p)
    fm=split_fm(t)
    for a in aliases_of(fm): aliasmap[a.lower()].append(p)
    wc[p]=len(t[len(fm):].split())

def rel(p): return os.path.relpath(p,ROOT).replace("\\","/")
def resolve(tgt):
    t=tgt.split("|")[0].split("#")[0].strip().lower()
    if not t: return True
    return t in names or t in aliasmap or (t.endswith(".md") and t[:-3] in names)

broken=defaultdict(list)
for p in files:
    for m in WL.finditer(strip_code(open(p,encoding="utf-8").read())):
        if not resolve(m.group(1)):
            broken[m.group(1).split("|")[0].split("#")[0].strip()].append(rel(p))
coll={k:[rel(x) for x in v] for k,v in names.items() if len(v)>1}
empty=[rel(p) for p in files if wc[p]<12]
print("files:",len(files))
print("BROKEN wikilinks:",len(broken))
for k,v in sorted(broken.items()): print("   ",repr(k),"<-",v[:3])
print("CASE collisions:",len(coll))
for k,v in sorted(coll.items()): print("   ",k,v)
print("EMPTY files:",len(empty))
for e in empty: print("   ",e)
