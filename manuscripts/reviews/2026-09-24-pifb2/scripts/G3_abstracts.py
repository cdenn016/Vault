"""G3: fetch abstracts for the proposed and cited references (INSPIRE first, then Semantic Scholar).

Usage: python G3_abstracts.py [KEY ...]
Prints the first ~900 characters of each abstract so that the one-line "supports the
proposed use" judgment in the G3 panel report rests on the source's own summary.
Read-only network lookups; no files are written.
"""
from __future__ import annotations

import sys
import time

import requests

DOIS: dict[str, str] = {
    "Wootters1981": "10.1103/PhysRevD.23.357",
    "BraunsteinCaves1994": "10.1103/PhysRevLett.72.3439",
    "HawkingKingMcCarthy1976": "10.1063/1.522874",
    "Malament1977": "10.1063/1.523436",
    "BombelliLeeMeyerSorkin1987": "10.1103/PhysRevLett.59.521",
    "Greensite1993": "10.1016/0370-2693(93)90744-3",
    "LiebRobinson1972": "10.1007/BF01645779",
    "Zurek2009": "10.1038/nphys1202",
    "SalamonBerry1983": "10.1103/PhysRevLett.51.1127",
    "Crooks2007": "10.1103/PhysRevLett.99.100602",
    "Zeilinger1999": "10.1023/A:1018820410908",
    "ChiribellaDArianoPerinotti2011": "10.1103/PhysRevA.84.012311",
    "MasanesMueller2011": "10.1088/1367-2630/13/6/063001",
    "Hoehn2017": "10.22331/q-2017-12-14-38",
    "Mueller2020": "10.22331/q-2020-07-20-301",
    "Caticha2005": "10.1063/1.2149814",
    "Caticha2019st": "10.3390/proceedings2019033015",
    "Erdmenger2020": "10.21468/SciPostPhys.8.5.073",
    "Fields2022": "10.1016/j.pbiomolbio.2022.05.006",
    "WuYang1975": "10.1103/PhysRevD.12.3845",
    "Utiyama1956": "10.1103/PhysRev.101.1597",
    "vanEnterFernandezSokal1993": "10.1007/BF01048183",
    "Machta2013": "10.1126/science.1238723",
    "Kikuchi1951": "10.1103/PhysRev.81.988",
    "KochJanuszRingel2018": "10.1038/s41567-018-0081-4",
    "SingerWu2012": "10.1002/cpa.21395",
    "HansenGhrist2021": "10.1137/20M1341088",
    "LavisStreater2002": "10.1016/S1355-2198(02)00007-2",
    "Ladyman1998": "10.1016/S0039-3681(98)80129-5",
    "DaCosta2021": "10.3390/e23040454",
    "Andruchow2014": "10.1016/j.geomphys.2014.08.009",
    "Kendall1990": "10.1112/plms/s3-61.2.371",
    "Afsari2011": "10.1090/S0002-9939-2010-10541-5",
    "KogutSusskind1975": "10.1103/PhysRevD.11.395",
    "FaddeevPopov1967": "10.1016/0370-2693(67)90067-6",
    "CornwallJackiwTomboulis1974": "10.1103/PhysRevD.10.2428",
    "Abbott1981NPB": "10.1016/0550-3213(81)90371-0",
    "Wilson1971": "10.1103/PhysRevB.4.3174",
    "KadanoffHoughtonYalabik1976": "10.1007/BF01011765",
}
ARXIV: dict[str, str] = {"Hardy2001": "quant-ph/0101012", "Matsueda2013": "1310.1831", "Pinchetti2022": "2211.03481"}


def inspire(doi: str) -> str | None:
    r = requests.get(
        "https://inspirehep.net/api/literature",
        params={"q": f"doi:{doi}", "fields": "abstracts", "size": 1},
        timeout=30,
    )
    hits = r.json()["hits"]["hits"]
    if hits and hits[0]["metadata"].get("abstracts"):
        return hits[0]["metadata"]["abstracts"][0]["value"]
    return None


def s2(ident: str) -> str | None:
    r = requests.get(
        f"https://api.semanticscholar.org/graph/v1/paper/{ident}", params={"fields": "abstract"}, timeout=30
    )
    if r.status_code != 200:
        return None
    return r.json().get("abstract")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    sel = set(sys.argv[1:])
    items = [(k, "DOI:" + v, v) for k, v in DOIS.items()] + [(k, "ARXIV:" + v, None) for k, v in ARXIV.items()]
    for key, s2id, doi in items:
        if sel and key not in sel:
            continue
        ab = None
        try:
            if doi:
                ab = inspire(doi)
            src = "INSPIRE"
            if not ab:
                time.sleep(1.2)
                ab = s2(s2id)
                src = "S2"
        except Exception as exc:
            print(f"[{key}] ERROR {exc!r}")
            continue
        text = " ".join((ab or "NO ABSTRACT").split())
        print(f"[{key}] ({src}) {text[:900]}\n")


if __name__ == "__main__":
    main()
