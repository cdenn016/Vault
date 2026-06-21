#!/usr/bin/env python3
"""Split dup clusters and stub list into batch files for review agents."""
import os, json, math

ROOT = r"C:\Users\chris and christine\Desktop\Research"
PARTS = os.path.join(ROOT, "docs", "_review_parts")
os.makedirs(PARTS, exist_ok=True)

dup = json.load(open(os.path.join(ROOT,"docs","_dup_scan.json"), encoding="utf-8"))
lint = json.load(open(os.path.join(ROOT,"docs","_lint_scan.json"), encoding="utf-8"))

# --- duplicate clusters ---
dups = dup["dups"]           # list of [norm_title, [files...]]
info = dup["info"]
clusters = []
for nt, files in dups:
    clusters.append({
        "title": info[files[0]]["title"],
        "notes": [{"path": f, "words": info[f]["wc"], "status": info[f]["status"]} for f in files],
    })

DUP_BATCH = 8
n = math.ceil(len(clusters)/DUP_BATCH)
for b in range(DUP_BATCH):
    chunk = clusters[b*n:(b+1)*n]
    if not chunk: continue
    json.dump(chunk, open(os.path.join(PARTS, f"dup_batch_{b}.json"),"w",encoding="utf-8"), indent=1)
print(f"dup clusters: {len(clusters)} -> {DUP_BATCH} batches (~{n} each)")

# --- stubs ---
stubs = lint["stubs"]   # [rel, wc, type]
# sort so concepts and papers interleave by name
stub_items = [{"path": r, "words": wc, "type": t} for r, wc, t in stubs]
stub_items.sort(key=lambda x: x["path"])
STUB_BATCH = 13
n2 = math.ceil(len(stub_items)/STUB_BATCH)
for b in range(STUB_BATCH):
    chunk = stub_items[b*n2:(b+1)*n2]
    if not chunk: continue
    json.dump(chunk, open(os.path.join(PARTS, f"stub_batch_{b}.json"),"w",encoding="utf-8"), indent=1)
print(f"stubs: {len(stub_items)} -> {STUB_BATCH} batches (~{n2} each)")
print("parts dir:", PARTS)
