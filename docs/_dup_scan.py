#!/usr/bin/env python3
"""Detect duplicate source notes by normalized title, and index drift. Read-only."""
import os, re, json
from collections import defaultdict

ROOT = r"C:\Users\chris and christine\Desktop\Research"

def norm_title(t):
    if not t: return ""
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return " ".join(t.split())

def get_fm(text):
    if not text.startswith("---"): return {}
    end = text.find("\n---", 3)
    if end == -1: return {}
    fm = text[:end]
    d = {}
    m = re.search(r"^title:\s*(.+?)\s*$", fm, re.M)
    if m: d["title"] = m.group(1).strip().strip("'\"")
    m = re.search(r"^year:\s*(.+?)\s*$", fm, re.M)
    if m: d["year"] = m.group(1).strip()
    m = re.search(r"^status:\s*(.+?)\s*$", fm, re.M)
    if m: d["status"] = m.group(1).strip()
    m = re.search(r"^type:\s*(.+?)\s*$", fm, re.M)
    if m: d["type"] = m.group(1).strip()
    # first author
    am = re.search(r"^authors:\s*(.*)$", fm, re.M)
    return d

# Collect source notes
src_files = []
for sub in ["papers", "refs", "manuscripts", "web", "runs"]:
    base = os.path.join(ROOT, "sources", sub)
    if not os.path.isdir(base): continue
    for f in os.listdir(base):
        if f.endswith(".md"):
            src_files.append(os.path.join(base, f))

by_title = defaultdict(list)
info = {}
for p in src_files:
    text = open(p, encoding="utf-8").read()
    fm = get_fm(text)
    rel = os.path.relpath(p, ROOT).replace("\\","/")
    wc = len(text.split())
    info[rel] = dict(title=fm.get("title",""), year=fm.get("year",""),
                     status=fm.get("status",""), wc=wc)
    nt = norm_title(fm.get("title",""))
    if nt:
        by_title[nt].append(rel)

# Duplicate title clusters (>1 note same normalized title)
dups = []
for nt, files in by_title.items():
    if len(files) > 1:
        dups.append((nt, sorted(files, key=lambda f: -info[f]["wc"])))

dups.sort(key=lambda x: x[0])
print("="*70)
print("DUPLICATE SOURCE NOTES (same normalized title): %d clusters" % len(dups))
print("="*70)
tot_extra = 0
for nt, files in dups:
    tot_extra += len(files)-1
    print(f"\n  TITLE: {info[files[0]]['title']!r}")
    for f in files:
        i = info[f]
        print(f"      [{i['wc']:4d}w {i['status'] or 'full':5s}] {f}")
print(f"\n  => {tot_extra} redundant notes across {len(dups)} clusters")

# Index drift: which sources/papers, sources/refs appear in index.md
idx = open(os.path.join(ROOT,"index.md"), encoding="utf-8").read()
idx_links = set(m.group(1).split("|")[0].split("#")[0].strip().lower()
                for m in re.finditer(r"\[\[([^\]]+)\]\]", idx))
missing_from_index = defaultdict(list)
for p in src_files:
    rel = os.path.relpath(p, ROOT).replace("\\","/")
    slug = os.path.splitext(os.path.basename(p))[0]
    # consider it indexed if slug or title alias appears
    if slug.lower() not in idx_links:
        sub = rel.split("/")[1]
        missing_from_index[sub].append(slug)

print("\n" + "="*70)
print("INDEX DRIFT: source notes whose slug is NOT linked in index.md")
print("="*70)
for sub, slugs in sorted(missing_from_index.items()):
    print(f"  sources/{sub}: {len(slugs)} not in index")

# Also wiki pages missing from index
wiki_files = []
for sub in ["concepts","methods","themes","projects","fields","dashboards"]:
    base = os.path.join(ROOT,"wiki",sub)
    if not os.path.isdir(base): continue
    for f in os.listdir(base):
        if f.endswith(".md"):
            wiki_files.append((sub, os.path.splitext(f)[0]))
wiki_missing = defaultdict(list)
for sub, slug in wiki_files:
    if slug.lower() not in idx_links:
        wiki_missing[sub].append(slug)
print("\n  WIKI pages not in index.md:")
for sub, slugs in sorted(wiki_missing.items()):
    print(f"    wiki/{sub}: {len(slugs)} missing -> {slugs[:5]}{'...' if len(slugs)>5 else ''}")

# Dump
json.dump(dict(dups=dups, info=info,
               missing_index={k:v for k,v in missing_from_index.items()},
               wiki_missing={k:v for k,v in wiki_missing.items()}),
          open(os.path.join(ROOT,"docs","_dup_scan.json"),"w",encoding="utf-8"), indent=1)
print("\nJSON -> docs/_dup_scan.json")
