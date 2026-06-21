#!/usr/bin/env python3
"""Compact vault linter. Read-only. Reusable.

Reports:
  BROKEN wikilinks   - links that resolve via NEITHER filename NOR alias (true dead links).
  GRAPH grey nodes   - links whose target is not a real (non-inbox) FILENAME. Obsidian's
                       graph view does NOT resolve aliases, so every alias-only link shows
                       as a grey placeholder node and clicking it creates an empty inbox note.
                       Fix by pointing the link at the canonical filename: [[Canonical|display]].
  EMPTY files        - 0-byte / near-empty notes (inbox shadow stubs included).
  CASE collisions    - two notes whose basenames match ignoring case.
  IDENTITY collisions- one name/alias claimed by >1 note (ambiguous resolution / autocomplete).
"""
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
            # quote-aware: do NOT split on commas inside quoted strings
            for tok in re.findall(r'"[^"]*"|\'[^\']*\'|[^,\[\]]+', rest):
                tok=tok.strip().strip('"\'').strip()
                if tok: out.append(tok)
        else:
            j=i+1
            while j<len(lines):
                bm=re.match(r"^\s*-\s+(.+?)\s*$",lines[j])
                if bm: out.append(bm.group(1).strip().strip('"\'')); j+=1
                elif lines[j].strip()=="": break
                else: break
    return out
def is_inbox(p): return (os.sep+"inbox"+os.sep) in p

files=[]
for d in DIRS:
    for dp,_,fn in os.walk(os.path.join(ROOT,d)):
        for f in fn:
            if f.endswith(".md"): files.append(os.path.join(dp,f))
for f in os.listdir(ROOT):
    if f.endswith(".md"): files.append(os.path.join(ROOT,f))

names=defaultdict(list); aliasmap=defaultdict(list); wc={}
realnames_nonbox=set()
for p in files:
    t=open(p,encoding="utf-8").read()
    base=os.path.splitext(os.path.basename(p))[0]
    names[base.lower()].append(p)
    if not is_inbox(p): realnames_nonbox.add(base.lower())
    fm=split_fm(t)
    for a in aliases_of(fm): aliasmap[a.lower()].append(p)
    body=t[len(fm)+8:] if fm else t
    wc[p]=len(body.split())

def rel(p): return os.path.relpath(p,ROOT).replace("\\","/")
def norm(tgt): return tgt.split("|")[0].split("#")[0].split("^")[0].strip().lower()
def resolve(tgt):  # alias-aware (Obsidian navigation)
    t=norm(tgt)
    if not t: return True
    return t in names or t in aliasmap or (t.endswith(".md") and t[:-3] in names)
def graph_ok(tgt):  # filename-only (Obsidian GRAPH view)
    t=norm(tgt)
    if not t: return True
    if t.endswith(".md"): t=t[:-3]
    return t in realnames_nonbox

broken=defaultdict(list); grey=defaultdict(list)
for p in files:
    if is_inbox(p): continue
    for m in WL.finditer(strip_code(open(p,encoding="utf-8").read())):
        tgt=m.group(1); disp=tgt.split("|")[0].split("#")[0].split("^")[0].strip()
        if not resolve(tgt): broken[disp].append(rel(p))
        if not graph_ok(tgt): grey[disp].append(rel(p))
coll={k:[rel(x) for x in v] for k,v in names.items() if len(v)>1}
empty=[rel(p) for p in files if wc[p]<12]
ident=defaultdict(set)
for k,v in names.items():
    for p in v: ident[k].add(p)
for k,v in aliasmap.items():
    for p in v: ident[k].add(p)
idcoll={k:sorted(rel(x) for x in v) for k,v in ident.items() if len(v)>1}

print("files:",len(files))
print("BROKEN wikilinks:",len(broken))
for k,v in sorted(broken.items()): print("   ",repr(k),"<-",v[:3])
print("GRAPH grey nodes:",len(grey))
for k,v in sorted(grey.items()): print("   ",repr(k),"<-",v[:3])
print("EMPTY files:",len(empty))
for e in empty: print("   ",e)
print("CASE collisions:",len(coll))
for k,v in sorted(coll.items()): print("   ",k,v)
print("IDENTITY collisions:",len(idcoll))
for k,v in sorted(idcoll.items()): print("   ",repr(k),v)
