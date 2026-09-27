import re
BS = chr(92)
L = open(r"C:/Users/chris and christine/Desktop/Research/manuscripts/GL(K)_attention_v2.tex", encoding="utf-8").read().split(chr(10))
ENV = re.compile(re.escape(BS) + "begin[{](equation|align|tikzpicture|table|algorithmic|algorithm)[}].*?" + re.escape(BS) + "end[{]" + BS + "1[}]", re.S)
NEG = re.compile(BS + "b(not|no|neither|nor|cannot|without|insufficient|outside)" + BS + "b")
def count(a, b):
    txt = " ".join(L[a-1:b]); txt = ENV.sub(" ", txt)
    sents = [s for s in re.split("(?<=[.;])" + BS + "s+", txt) if len(s.strip()) > 20]
    neg = [s for s in sents if NEG.search(s)]
    return len(sents), len(neg)
for name, (a, b) in {"Intro 57-73": (57, 73), "Sec2.3 361-402": (361, 402), "Sec2.6.1 726-792": (726, 792),
                     "Sec2.7 796-807": (796, 807), "Sec3.3-3.4 926-959": (926, 959), "Sec4 962-1091": (962, 1091),
                     "Discussion 1164-1191": (1164, 1191)}.items():
    n, k = count(a, b); print("%-22s sentences=%3d negated=%3d frac=%.2f" % (name, n, k, k/n))
