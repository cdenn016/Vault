"""Sentence-level negation census for LaTeX manuscripts (philosophy-of-science lens).

Core negation set (as specified in the panel brief): not, no, neither, nor, cannot
("need not", "does not" are covered by "not").  Extended scope-disclaimer set adds:
never, none, without, unless, nothing, alone, merely, automatically, by itself,
in general, generally, necessarily.  Prose only: comments, TikZ, floats and display
math are removed; inline math becomes X; citations and references become REF.
"""
import re, sys, json, collections, pathlib

B = chr(92)
EB = re.escape(B)
CORE = re.compile(r"\b(not|no|neither|nor|cannot)\b|n't\b", re.I)
EXT = re.compile(r"\b(not|no|neither|nor|cannot|never|none|without|unless|nothing|alone|merely|automatically|generally|necessarily)\b|\bby itself\b|\bin general\b|n't\b", re.I)
ABBR = ["Eqs.", "Eq.", "Secs.", "Sec.", "Figs.", "Fig.", "Apps.", "App.", "e.g.", "i.e.", "cf.", "et al.", "vs.",
        "resp.", "Ref.", "Refs.", "Prop.", "Thm.", "approx.", "pp.", "p.", "Vol.", "No.", "Def.", "Lem.", "Cor.",
        "Tab.", "Alg.", "Ch.", "Chap.", "w.r.t.", "a.s.", "i.i.d.", "Dr.", "Mr.", "St.", "etc."]
ENVS_DROP = ["tikzpicture", "figure", "figure*", "table", "table*", "algorithm", "algorithmic", "equation",
             "equation*", "align", "align*", "gather", "gather*", "multline", "multline*", "eqnarray",
             "eqnarray*", "tabular", "tabularx", "lstlisting", "verbatim", "thebibliography", "displaymath",
             "wrapfigure", "subequations", "IEEEeqnarray", "longtable"]

def env_re(env):
    return re.escape(B + "begin{" + env + "}") + ".*?" + re.escape(B + "end{" + env + "}")

def clean(tex):
    tex = re.sub("(?<!" + EB + ")%.*", "", tex)
    for env in ENVS_DROP:
        tex = re.sub(env_re(env), " ", tex, flags=re.S)
    tex = re.sub(re.escape(B + "[") + ".*?" + re.escape(B + "]"), " ", tex, flags=re.S)
    tex = re.sub(r"\$\$.*?\$\$", " ", tex, flags=re.S)
    tex = re.sub(re.escape(B + "(") + ".*?" + re.escape(B + ")"), " X ", tex, flags=re.S)
    tex = re.sub("(?<!" + EB + r")\$[^$]*\$", " X ", tex)
    tex = re.sub(EB + r"(cite[a-z]*|ref|eqref|autoref|cref|Cref|pageref)\*?(\[[^\]]*\])*\{[^}]*\}", " REF ", tex)
    tex = re.sub(EB + r"(label|url|href|bibliography|bibliographystyle|graphicspath|usepackage|input|include)(\[[^\]]*\])*\{[^}]*\}", " ", tex)
    tex = tex.replace("~", " ")
    for a in ABBR:
        tex = tex.replace(a, a.replace(".", "<DOT>"))
    tex = re.sub(EB + r"[A-Za-z]+\*?", " ", tex)
    tex = re.sub("[{}" + EB + "]", " ", tex)
    return tex

def sentences(text):
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9X(\"'`])", text)
    out = []
    for p in parts:
        p = p.replace("<DOT>", ".").strip()
        if len(re.findall(r"[A-Za-z]{2,}", p)) >= 3:
            out.append(p)
    return out

def nwords(s):
    return len(re.findall(r"[A-Za-z][A-Za-z'\-]*", s))

def census(text):
    ss = sentences(clean(text))
    tw = sum(nwords(s) for s in ss)
    core = [s for s in ss if CORE.search(s)]
    ext = [s for s in ss if EXT.search(s)]
    return dict(sentences=len(ss), words=tw, core_neg=len(core), core_frac=len(core) / max(1, len(ss)),
                core_word_frac=sum(nwords(s) for s in core) / max(1, tw), ext_neg=len(ext),
                ext_frac=len(ext) / max(1, len(ss)), core_list=core)

def body_of(tex):
    bd = B + "begin{document}"
    if bd in tex:
        tex = tex.split(bd, 1)[1]
    tex = tex.split(B + "end{document}", 1)[0]
    tex = re.split(re.escape(B + "begin{thebibliography}") + "|" + re.escape(B + "bibliography{"), tex)[0]
    return tex

def split_sections(tex):
    out = collections.OrderedDict()
    m = re.search(re.escape(B + "begin{abstract}") + "(.*?)" + re.escape(B + "end{abstract}"), tex, flags=re.S)
    if m:
        out["Abstract"] = m.group(1)
        tex = tex.replace(m.group(0), " ")
    sec = EB + r"section\*?\{([^}]*)\}"
    parts = re.split("(" + EB + r"section\*?\{[^}]*\})", tex)
    cur = "Front matter"
    for p in parts:
        h = re.match(sec, p)
        if h:
            cur = h.group(1)
            continue
        out[cur] = out.get(cur, "") + p
    return out

def fmt(h, c):
    return f"{h[:56]:56s} {c['sentences']:5d} {c['core_neg']:4d} {c['core_frac']:6.1%} {c['core_word_frac']:6.1%} {c['ext_neg']:4d} {c['ext_frac']:6.1%}"

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "sections":
        tex = body_of(pathlib.Path(sys.argv[2]).read_text(encoding="utf-8", errors="replace"))
        secs = split_sections(tex)
        print(f"{'Section':56s} {'sent':>5s} {'neg':>4s} {'frac':>6s} {'wfrac':>6s} {'ext':>4s} {'efrac':>6s}")
        for h, t in secs.items():
            c = census(t)
            if c["sentences"]:
                print(fmt(h, c))
        tot = census(" ".join(secs.values()))
        print(fmt("TOTAL", tot) + f"  words={tot['words']}")
    elif mode == "lines":
        path, a, b = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
        lines = pathlib.Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
        c = census("\n".join(lines[a - 1:b]))
        print(json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in c.items() if k != "core_list"}))
        if len(sys.argv) > 5:
            for i, s in enumerate(c["core_list"], 1):
                print(f"  [{i}] {s}")
    elif mode == "total":
        tex = " ".join(body_of(pathlib.Path(p).read_text(encoding="utf-8", errors="replace")) for p in sys.argv[2:])
        c = census(tex)
        print(json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in c.items() if k != "core_list"}))
