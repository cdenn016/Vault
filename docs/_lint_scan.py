#!/usr/bin/env python3
"""Deep lint scan of the research wiki vault. Read-only analysis."""
import os, re, json, sys
from collections import defaultdict

ROOT = r"C:\Users\chris and christine\Desktop\Research"
DIRS = ["wiki", "sources", "manuscripts", "templates", "inbox"]

WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
FM_TITLE = re.compile(r"^title:\s*(.+?)\s*$", re.M)
FM_STATUS = re.compile(r"^status:\s*(.+?)\s*$", re.M)
FM_TYPE = re.compile(r"^type:\s*(.+?)\s*$", re.M)

def strip_code(text):
    # remove fenced code blocks and inline code so backticked example links don't count
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`]*`", "", text)
    return text

def parse_fm_block(fm):
    """Return (title, aliases[], status, type, tags_raw) from a frontmatter string,
    handling both inline [a,b] and YAML block-list aliases/tags."""
    lines = fm.split("\n")
    title = status = typ = None
    aliases = []
    tags_raw = None
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^title:\s*(.+?)\s*$", line)
        if m: title = m.group(1).strip().strip("'\"")
        m = re.match(r"^status:\s*(.+?)\s*$", line)
        if m: status = m.group(1).strip()
        m = re.match(r"^type:\s*(.+?)\s*$", line)
        if m: typ = m.group(1).strip()
        m = re.match(r"^aliases:\s*(.*)$", line)
        if m:
            rest = m.group(1).strip()
            if rest.startswith("["):
                inner = rest.strip("[]")
                for p in inner.split(","):
                    p = p.strip().strip("'\"")
                    if p: aliases.append(p)
            elif rest and rest not in ("|", ">"):
                aliases.append(rest.strip("'\""))
            else:
                # block list follows
                j = i + 1
                while j < len(lines):
                    bm = re.match(r"^\s*-\s+(.+?)\s*$", lines[j])
                    if bm:
                        aliases.append(bm.group(1).strip().strip("'\""))
                        j += 1
                    elif lines[j].strip() == "" or re.match(r"^\s+\S", lines[j]):
                        # allow blank continuation? stop on a new key
                        if re.match(r"^\S+:", lines[j]):
                            break
                        if lines[j].strip() == "":
                            j += 1
                            continue
                        break
                    else:
                        break
                i = j - 1
        m = re.match(r"^tags:\s*(.*)$", line)
        if m:
            tags_raw = m.group(1).strip() or "BLOCK"
        i += 1
    return title, aliases, status, typ, tags_raw

files = []
for d in DIRS:
    base = os.path.join(ROOT, d)
    for dp, dn, fn in os.walk(base):
        # skip .obsidian etc
        for f in fn:
            if f.endswith(".md"):
                files.append(os.path.join(dp, f))

# also root-level md
for f in os.listdir(ROOT):
    if f.endswith(".md"):
        files.append(os.path.join(ROOT, f))

# Build resolution index: lowercased basename (no ext) + aliases -> canonical file
name_to_file = defaultdict(list)   # lower name -> [files]
alias_to_file = defaultdict(list)  # lower alias -> [files]
meta = {}  # file -> dict

def rel(p):
    return os.path.relpath(p, ROOT).replace("\\", "/")

for p in files:
    try:
        text = open(p, encoding="utf-8").read()
    except Exception as e:
        text = ""
    base = os.path.splitext(os.path.basename(p))[0]
    # frontmatter region
    fm = ""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[:end]
    title, aliases, status, typ, tags = parse_fm_block(fm)
    body = text[len(fm):] if fm else text
    wc = len(body.split())
    meta[p] = dict(base=base, title=title, aliases=aliases, status=status,
                   type=typ, tags=tags, wc=wc, bytes=len(text.encode("utf-8")),
                   rel=rel(p))
    name_to_file[base.lower()].append(p)
    for a in aliases:
        alias_to_file[a.lower()].append(p)

# Resolution function
def resolve(target):
    # strip display part
    t = target.split("|")[0].strip()
    # strip heading/block refs
    t = t.split("#")[0].strip()
    if not t:
        return "self"  # block ref only
    tl = t.lower()
    if tl in name_to_file:
        return name_to_file[tl]
    if tl in alias_to_file:
        return alias_to_file[tl]
    # try with .md stripped
    if tl.endswith(".md") and tl[:-3] in name_to_file:
        return name_to_file[tl[:-3]]
    return None

# Scan links
broken = defaultdict(list)   # target -> [files]
inbound = defaultdict(int)   # resolved file -> count
all_targets = defaultdict(int)
for p in files:
    try:
        text = open(p, encoding="utf-8").read()
    except Exception:
        continue
    code_stripped = strip_code(text)
    for m in WIKILINK.finditer(code_stripped):
        tgt = m.group(1)
        all_targets[tgt.split("|")[0].split("#")[0].strip()] += 1
        r = resolve(tgt)
        if r is None:
            broken[tgt.split("|")[0].split("#")[0].strip()].append(rel(p))
        elif r == "self":
            pass
        else:
            for rf in r:
                inbound[rf] += 1

# Empty / near-empty files
empty = []
for p in files:
    mm = meta[p]
    if mm["wc"] < 12:  # essentially empty body
        empty.append((mm["rel"], mm["wc"], mm["bytes"]))

# Stub-status pages
stubs = []
for p in files:
    mm = meta[p]
    if mm["status"] == "stub":
        stubs.append((mm["rel"], mm["wc"], mm["type"]))

# Thin pages (not stub but low word count) for wiki + sources
thin = []
for p in files:
    mm = meta[p]
    if 12 <= mm["wc"] < 120 and mm["status"] != "stub":
        thin.append((mm["rel"], mm["wc"], mm["status"], mm["type"]))

# Case-insensitive basename collisions
collisions = []
for k, v in name_to_file.items():
    if len(v) > 1:
        collisions.append((k, [rel(x) for x in v]))

# Alias collisions (alias used by >1 file, or alias == a real basename)
alias_collisions = []
for k, v in alias_to_file.items():
    targets = set(rel(x) for x in v)
    extra = []
    if k in name_to_file:
        extra = [rel(x) for x in name_to_file[k]]
    if len(targets) > 1 or extra:
        alias_collisions.append((k, sorted(targets), extra))

# Orphans: wiki pages with 0 inbound (exclude index/log/CLAUDE/templates/dashboards/MOCs maybe)
orphans = []
for p in files:
    mm = meta[p]
    r = mm["rel"]
    if not r.startswith("wiki/"):
        continue
    if inbound.get(p, 0) == 0:
        orphans.append((r, mm["type"], mm["wc"], mm["status"]))

# Missing frontmatter (no type or no title) for wiki/sources
missing_fm = []
for p in files:
    mm = meta[p]
    r = mm["rel"]
    if r.startswith(("wiki/", "sources/")):
        probs = []
        if not mm["type"]: probs.append("no-type")
        if not mm["title"]: probs.append("no-title")
        if not mm["tags"]: probs.append("no-tags")
        if probs:
            missing_fm.append((r, probs))

# Summarize
def head(s): print("\n" + "="*70 + "\n" + s + "\n" + "="*70)

print("TOTAL FILES SCANNED:", len(files))
print("TOTAL WIKILINK TARGETS (distinct):", len(all_targets))

head("BROKEN WIKILINKS (ghost nodes) — distinct targets: %d" % len(broken))
broken_sorted = sorted(broken.items(), key=lambda kv: -len(kv[1]))
for tgt, srcs in broken_sorted:
    print(f"  [{len(srcs):3d}x] {tgt!r}  e.g. {srcs[0]}")

head("EMPTY / NEAR-EMPTY FILES (<12 words body): %d" % len(empty))
for r, wc, b in sorted(empty):
    print(f"  {wc:3d}w {b:5d}B  {r}")

head("STUB-STATUS PAGES: %d" % len(stubs))
by_type = defaultdict(int)
for r, wc, t in stubs:
    by_type[t] += 1
print("  by type:", dict(by_type))
print("  (full list written to JSON)")

head("THIN NON-STUB PAGES (12-120 words): %d" % len(thin))
print("  (full list written to JSON)")

head("CASE-INSENSITIVE BASENAME COLLISIONS: %d" % len(collisions))
for k, v in sorted(collisions):
    print(f"  {k!r}:")
    for x in v:
        print(f"      {x}")

head("ALIAS COLLISIONS (alias shared / alias==basename): %d" % len(alias_collisions))
for k, tgts, extra in sorted(alias_collisions)[:60]:
    print(f"  alias {k!r}: targets={tgts} basename_pages={extra}")
print("  (total %d; full list in JSON)" % len(alias_collisions))

head("ORPHAN WIKI PAGES (0 inbound links): %d" % len(orphans))
for r, t, wc, st in sorted(orphans):
    print(f"  [{t}/{st}] {wc}w  {r}")

head("WIKI/SOURCE PAGES MISSING FRONTMATTER FIELDS: %d" % len(missing_fm))
for r, probs in sorted(missing_fm):
    print(f"  {probs}  {r}")

# Dump JSON for downstream agents
dump = dict(
    broken={k: v for k, v in broken.items()},
    empty=empty, stubs=stubs, thin=thin,
    collisions=collisions, alias_collisions=alias_collisions,
    orphans=orphans, missing_fm=missing_fm,
)
with open(os.path.join(ROOT, "docs", "_lint_scan.json"), "w", encoding="utf-8") as fh:
    json.dump(dump, fh, indent=1)
print("\nJSON dump -> docs/_lint_scan.json")
