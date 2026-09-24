"""L16: display-equation terminal punctuation audit for PIFB2.tex.

For every display (equation, align, gather, multline, their starred forms, and \\[ \\]),
take the math content before the closing delimiter, strip labels/tags/whitespace,
and classify its final character as ',', '.', ';' or none. Then look at the first
word of the following text to flag likely mismatches:
  - none, followed by a lowercase continuation word (where, with, so, and, for, ...) -> missing comma
  - none, followed by a capitalized new sentence -> missing period
  - '.', followed by lowercase continuation -> period should be comma
"""
import re
import collections

TEX = r"C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex"
src = open(TEX, encoding="utf-8").read()
lines = src.split("\n")
# offsets -> line numbers
starts = [0]
for l in lines:
    starts.append(starts[-1] + len(l) + 1)


def lineno(off: int) -> int:
    lo, hi = 0, len(starts) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if starts[mid] <= off:
            lo = mid
        else:
            hi = mid - 1
    return lo + 1


body = re.sub(r"(?<!\\)%[^\n]*", "", src)
ENV = r"(equation|align|gather|multline|eqnarray)\*?"
rx = re.compile(r"\\begin\{(" + ENV + r")\}(.*?)\\end\{\1\}|\\\[(.*?)\\\]", re.S)
stats = collections.Counter()
flags = []
for m in rx.finditer(body):
    content = m.group(3) if m.group(1) else m.group(4)
    if content is None:
        continue
    c = re.sub(r"\\(label|tag|nonumber|notag)\{?[^}\s]*\}?", "", content)
    c = re.sub(r"\\(qquad|quad)", " ", c).rstrip()
    c = re.sub(r"(\\\\|\\right\.|\\right[)\]|]|\\end\{[a-z]+\}|\\\}|[\s}])+$", lambda t: t.group(0) if "," in t.group(0) or "." in t.group(0) else "", c)
    tail = c.rstrip(" }\n\t")
    last = tail[-1:] if tail else ""
    kind = last if last in ",.;:" else "none"
    stats[kind] += 1
    after = body[m.end():m.end() + 80].lstrip()
    fw = re.match(r"[A-Za-z]+", after)
    fw = fw.group(0) if fw else after[:6]
    ln = lineno(m.start())
    cont = fw.lower() in {"where", "with", "so", "and", "for", "which", "since", "because",
                          "i", "is", "in", "gives", "yields", "or", "then", "hence", "as",
                          "whose", "that", "by", "from", "on", "at", "to", "provided", "if",
                          "when", "while", "valid", "up", "until", "subject", "summed"}
    if kind == "none" and cont:
        flags.append((ln, "missing comma before continuation", fw))
    elif kind == "none" and fw[:1].isupper():
        flags.append((ln, "missing period before new sentence", fw))
    elif kind == "." and cont and fw[:1].islower():
        flags.append((ln, "period before lowercase continuation", fw))
print("display count by terminal mark:", dict(stats))
print("flags:", len(flags))
kinds = collections.Counter(f[1] for f in flags)
print(dict(kinds))
for f in flags[:400]:
    print(f)
