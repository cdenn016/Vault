"""G3: verify bibliographic metadata of proposed PIFB2 references against Crossref and arXiv.

Usage: python G3_crossref.py
Prints, for each candidate DOI, the Crossref record (authors, title, container,
volume, issue, pages, year). For entries without a known DOI it runs a Crossref
bibliographic query and prints the top hits; arXiv-only items use the arXiv API.
Read-only network lookups; no files are written.
"""
from __future__ import annotations

import re
import sys
import time
import xml.etree.ElementTree as ET

import requests

UA = {"User-Agent": "PIFB2-review-G3/1.0 (mailto:noreply@example.org)"}

DOIS: list[tuple[str, str]] = [
    ("Wootters1981", "10.1103/PhysRevD.23.357"),
    ("BraunsteinCaves1994", "10.1103/PhysRevLett.72.3439"),
    ("HawkingKingMcCarthy1976", "10.1063/1.522874"),
    ("Malament1977", "10.1063/1.523436"),
    ("BombelliLeeMeyerSorkin1987", "10.1103/PhysRevLett.59.521"),
    ("LiebRobinson1972", "10.1007/BF01645779"),
    ("Zurek2009", "10.1038/nphys1202"),
    ("SalamonBerry1983", "10.1103/PhysRevLett.51.1127"),
    ("Crooks2007", "10.1103/PhysRevLett.99.100602"),
    ("Zeilinger1999", "10.1023/A:1018820410908"),
    ("ChiribellaDArianoPerinotti2011", "10.1103/PhysRevA.84.012311"),
    ("MasanesMueller2011", "10.1088/1367-2630/13/6/063001"),
    ("Hoehn2017", "10.22331/q-2017-12-14-38"),
    ("Mueller2020", "10.22331/q-2020-07-20-301"),
    ("Erdmenger2020", "10.21468/SciPostPhys.8.5.073"),
    ("Fields2022", "10.1016/j.pbiomolbio.2022.05.006"),
    ("WuYang1975", "10.1103/PhysRevD.12.3845"),
    ("Utiyama1956", "10.1103/PhysRev.101.1597"),
    ("vanEnterFernandezSokal1993", "10.1007/BF01048183"),
    ("Machta2013", "10.1126/science.1238723"),
    ("Kikuchi1951", "10.1103/PhysRev.81.988"),
    ("KochJanuszRingel2018", "10.1038/s41567-018-0081-4"),
    ("SingerWu2012", "10.1002/cpa.21395"),
    ("HansenGhrist2021", "10.1137/20M1341088"),
    ("LavisStreater2002", "10.1016/S1355-2198(02)00007-2"),
    ("Ladyman1998", "10.1016/S0039-3681(98)80129-5"),
    ("DaCosta2021", "10.3390/e23040454"),
    ("Andruchow2014", "10.1016/j.geomphys.2014.08.009"),
    ("Kendall1990", "10.1112/plms/s3-61.2.371"),
    ("Afsari2011", "10.1090/S0002-9939-2010-10541-5"),
    # Part 2: cited works
    ("WilsonConfinement1974", "10.1103/PhysRevD.10.2445"),
    ("KogutSusskind1975", "10.1103/PhysRevD.11.395"),
    ("Wilson1971", "10.1103/PhysRevB.4.3174"),
    ("WilsonKogut1974", "10.1016/0370-1573(74)90023-4"),
    ("Milnor1976", "10.1016/S0001-8708(76)80002-3"),
    ("Wainwright2008", "10.1561/2200000001"),
    ("Yedidia2005", "10.1109/TIT.2005.850085"),
    ("FaddeevPopov1967", "10.1016/0370-2693(67)90067-6"),
    ("CornwallJackiwTomboulis1974", "10.1103/PhysRevD.10.2428"),
    ("Abbott1981NPB", "10.1016/0550-3213(81)90371-0"),
    ("KadanoffHoughtonYalabik1976", "10.1007/BF01011765"),
    ("Kadanoff1975PRL", "10.1103/PhysRevLett.34.1005"),
    ("DeWitt1967", "10.1103/PhysRev.162.1195"),
]

QUERIES: list[tuple[str, str]] = [
    ("Greensite1993", "Greensite Dynamical origin of the Lorentzian signature of spacetime Physics Letters B 1993"),
    ("Caticha2006", "Caticha The information geometry of space and time AIP Conference Proceedings 803"),
    ("Caticha2019st", "Caticha The information geometry of space-time Proceedings 2019"),
    ("Matsueda2013", "Matsueda Emergent general relativity from Fisher information metric"),
    ("Pinchetti2022", "Pinchetti Salvatori Predictive coding beyond Gaussian distributions"),
    ("Abbott1982APPB", "Abbott Introduction to the background field method Acta Physica Polonica"),
    ("Kendall1990q", "Kendall Probability convexity and harmonic maps with small image uniqueness and fine existence"),
]

ARXIV: list[tuple[str, str]] = [
    ("Hardy2001", "quant-ph/0101012"),
    ("Caticha2006arXiv", "gr-qc/0508108"),
    ("Caticha2019st_arXiv", "1909.09657"),
    ("Matsueda2013arXiv", "1310.1831"),
    ("Pinchetti2022arXiv", "2211.03481"),
    ("Mehta2014arXiv", "1410.3831"),
    ("Greensite1993arXiv", "gr-qc/9210008"),
]


def fmt(msg: dict) -> str:
    """Format a Crossref work record as a one-line citation."""
    au = "; ".join(
        f"{a.get('family', '')}, {a.get('given', '')}".strip(", ") for a in msg.get("author", [])
    )
    title = " ".join(msg.get("title", [""]))
    cont = " ".join(msg.get("container-title", [""]))
    yr = None
    for k in ("published-print", "issued", "published-online"):
        if k in msg:
            yr = msg[k]["date-parts"][0][0]
            break
    return (
        f"{au} | {title} | {cont} | vol={msg.get('volume')} issue={msg.get('issue')} "
        f"pages={msg.get('page')} art={msg.get('article-number')} year={yr} doi={msg.get('DOI')}"
    )


def get_doi(doi: str) -> str:
    r = requests.get(f"https://api.crossref.org/works/{doi}", headers=UA, timeout=30)
    if r.status_code != 200:
        return f"HTTP {r.status_code}"
    return fmt(r.json()["message"])


def query(q: str, n: int = 3) -> list[str]:
    r = requests.get(
        "https://api.crossref.org/works",
        params={"query.bibliographic": q, "rows": n},
        headers=UA,
        timeout=30,
    )
    return [fmt(m) for m in r.json()["message"]["items"]]


def arxiv(aid: str) -> str:
    r = requests.get("http://export.arxiv.org/api/query", params={"id_list": aid}, timeout=30)
    ns = {"a": "http://www.w3.org/2005/Atom", "ar": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(r.text)
    e = root.find("a:entry", ns)
    if e is None:
        return "no entry"
    title = re.sub(r"\s+", " ", e.findtext("a:title", "", ns))
    au = "; ".join(x.findtext("a:name", "", ns) for x in e.findall("a:author", ns))
    pub = e.findtext("a:published", "", ns)[:10]
    jr = e.findtext("ar:journal_ref", "", ns)
    doi = e.findtext("ar:doi", "", ns)
    return f"{au} | {title} | submitted {pub} | journal_ref={jr} | doi={doi}"


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    sel = set(sys.argv[1:])
    for key, doi in DOIS:
        if sel and key not in sel:
            continue
        try:
            print(f"[DOI] {key}: {get_doi(doi)}")
        except Exception as exc:  # network failures are reported, not hidden
            print(f"[DOI] {key}: ERROR {exc!r}")
        time.sleep(0.2)
    for key, q in QUERIES:
        if sel and key not in sel:
            continue
        try:
            for i, h in enumerate(query(q)):
                print(f"[Q] {key} #{i}: {h}")
        except Exception as exc:
            print(f"[Q] {key}: ERROR {exc!r}")
    for key, aid in ARXIV:
        if sel and key not in sel:
            continue
        try:
            print(f"[arXiv] {key}: {arxiv(aid)}")
        except Exception as exc:
            print(f"[arXiv] {key}: ERROR {exc!r}")
        time.sleep(3)


if __name__ == "__main__":
    main()
