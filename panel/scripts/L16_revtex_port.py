"""L16: write a minimally ported REVTeX 4.2 / apsrev4-2 copy of PIFB2.tex into the scratch folder.

Changes only: document class, drop geometry, bibliography style. The abstract is moved
before \\maketitle because REVTeX requires it there. Nothing in the manuscripts folder is written.
"""
import re
import sys

SRC = r"C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex"
OUT = sys.argv[1]
t = open(SRC, encoding="utf-8").read()
t = t.replace(r"\documentclass[11pt]{article}",
              r"\documentclass[prd,onecolumn,nofootinbib,superscriptaddress]{revtex4-2}", 1)
t = t.replace("\\usepackage{geometry}\n", "", 1).replace("\\geometry{margin=1in}\n", "", 1)
t = t.replace(r"\bibliographystyle{unsrt}", r"\bibliographystyle{apsrev4-2}", 1)
if "--fix-preamble" in sys.argv:
    # the two preamble clashes the first REVTeX pass reports
    t = t.replace("\\usepackage{cite}\n", "", 1)
    t = t.replace("\\newenvironment{acknowledgments}\n  {\\section*{Acknowledgments}}\n  {}\n", "", 1)
ab = re.search(r"\\begin\{abstract\}.*?\\end\{abstract\}\n", t, re.S)
t = t[:ab.start()] + t[ab.end():]
t = t.replace("\\maketitle\n", ab.group(0) + "\\maketitle\n", 1)
open(OUT, "w", encoding="utf-8").write(t)
print("wrote", OUT)
