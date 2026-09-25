"""L16: inventory of decorated uses of overloaded symbols in PIFB2.tex, with line numbers.

Usage: python L16_symbols.py <name> [<name> ...]
Prints, for each symbol, every distinct math token (symbol plus immediate sub/superscript)
with the list of source lines where it occurs (first 15), so collisions can be read off.
"""
import re
import sys
import collections

TEX = r"C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex"
lines = open(TEX, encoding="utf-8").read().split("\n")

SYM = {
    "Omega": r"\\Omega", "tau": r"\\tau", "kappa": r"\\kappa", "beta": r"\\beta",
    "gamma": r"\\gamma", "alpha": r"\\alpha", "chi": r"\\chi", "phi": r"\\phi",
    "Phi": r"\\Phi", "varphi": r"\\varphi", "rho": r"\\rho", "sigma": r"\\sigma", "Sigma": r"\\Sigma",
    "lambda": r"\\lambda", "Lambda": r"\\Lambda", "epsilon": r"\\(?:var)?epsilon", "omega": r"\\omega",
    "eta": r"\\eta", "mu": r"\\mu", "nu": r"\\nu", "xi": r"\\xi", "Gamma": r"\\Gamma", "Psi": r"\\Psi",
    "psi": r"\\psi", "theta": r"\\theta", "Theta": r"\\Theta", "delta": r"\\delta", "Delta": r"\\Delta",
    "pi": r"\\pi", "zeta": r"\\zeta",
    "M": r"(?<![\\A-Za-z])M", "G": r"(?<![\\A-Za-z])G", "K": r"(?<![\\A-Za-z])K",
    "c": r"(?<![\\A-Za-z{])c(?![A-Za-z])", "I": r"(?<![\\A-Za-z])I(?![A-Za-z])",
    "r": r"(?<![\\A-Za-z{])r(?![A-Za-z])", "s": r"(?<![\\A-Za-z{])s(?![A-Za-z])",
    "N": r"(?<![\\A-Za-z])N(?![A-Za-z])", "T": r"(?<![\\A-Za-z])T(?![A-Za-z])",
    "Z": r"(?<![\\A-Za-z])Z(?![A-Za-z])", "A": r"(?<![\\A-Za-z])A(?![A-Za-z])",
    "F": r"(?<![\\A-Za-z])F(?![A-Za-z])", "H": r"(?<![\\A-Za-z])H(?![A-Za-z])",
    "E": r"(?<![\\A-Za-z])E(?![A-Za-z])", "L": r"(?<![\\A-Za-z])L(?![A-Za-z])",
    "d": r"(?<![\\A-Za-z{])d(?![A-Za-z])", "g": r"(?<![\\A-Za-z{])g(?![A-Za-z])",
    "m": r"(?<![\\A-Za-z{])m(?![A-Za-z])", "k": r"(?<![\\A-Za-z{])k(?![A-Za-z])",
    "B": r"(?<![\\A-Za-z])B(?![A-Za-z])", "D": r"(?<![\\A-Za-z])D(?![A-Za-z])",
    "R": r"(?<![\\A-Za-z])R(?![A-Za-z])", "Q": r"(?<![\\A-Za-z])Q(?![A-Za-z])",
    "U": r"(?<![\\A-Za-z])U(?![A-Za-z])", "W": r"(?<![\\A-Za-z])W(?![A-Za-z])",
    "C": r"(?<![\\A-Za-z])C(?![A-Za-z])", "S": r"(?<![\\A-Za-z])S(?![A-Za-z])",
    "P": r"(?<![\\A-Za-z])P(?![A-Za-z])", "X": r"(?<![\\A-Za-z])X(?![A-Za-z])",
}
DECOR = r"(?:\s*(?:_\{(?:[^{}]|\{[^{}]*\})*\}|_\\?[A-Za-z0-9]+|\^\{(?:[^{}]|\{[^{}]*\})*\}|\^\\?[A-Za-z0-9]+|'))*"


def math_spans(l: str):
    """Yield inline and display math fragments of one source line (heuristic)."""
    for m in re.finditer(r"\$(.+?)\$", l):
        yield m.group(1)
    if not re.search(r"\$", l):
        yield l  # display lines usually have no dollars


env_math = False
for name in sys.argv[1:]:
    rx = re.compile(SYM[name] + r"(?![A-Za-z])" + DECOR) if name[0].islower() and len(name) > 1 or name in ("Omega", "Phi", "Sigma", "Lambda", "Gamma", "Psi", "Theta", "Delta") else re.compile(SYM[name] + DECOR)
    found = collections.defaultdict(list)
    for n, l in enumerate(lines, 1):
        if l.lstrip().startswith("%"):
            continue
        for frag in math_spans(l):
            for m in rx.finditer(frag):
                tok = re.sub(r"\s+", "", m.group(0))
                if not found[tok] or found[tok][-1] != n:
                    found[tok].append(n)
    print(f"===== {name}: {len(found)} distinct tokens")
    for tok, ns in sorted(found.items(), key=lambda t: -len(t[1])):
        print(f"  {tok:40s} x{len(ns):4d}  {ns[:15]}")
