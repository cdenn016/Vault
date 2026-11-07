"""Download this reading set from primary hosts and validate local PDF identity."""

from __future__ import annotations

import concurrent.futures
import hashlib
import io
import json
import os
from pathlib import Path
import re
from typing import Any

for name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[name] = "4"

import pymupdf as fitz
from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader
import requests

ROOT = Path(__file__).resolve().parents[3]
PDFS = ROOT / "sources" / "pdfs"
OUT = Path(__file__).resolve().parent

# Existing copies are immutable. URLs on reused rows identify a primary source,
# not a claim that the existing file was fetched from that URL in this session.
PAPERS = [
    ("friston-frith-2015-duet", "A Duet for One", "Friston; Frith", "FristonFrith2015duet.pdf", "https://www.fil.ion.ucl.ac.uk/~karl/A%20Duet%20for%20one.pdf", "Existing author-hosted journal article", ["duet", "friston", "frith"]),
    ("friston-frith-2015-hermeneutics", "Active inference, communication and hermeneutics", "Friston; Frith", None, "https://pmc.ncbi.nlm.nih.gov/articles/PMC4502445/pdf/main.pdf", "Published journal article", ["hermeneutics", "friston", "frith"]),
    ("frank-goodman-2012-pragmatic-reasoning", "Predicting pragmatic reasoning in language games", "Frank; Goodman", None, "https://web.stanford.edu/~ngoodman/papers/FrankGoodman-Science2012.pdf", "Author-hosted manuscript with supplement; 2012 Science article", ["pragmatic", "frank", "goodman"]),
    ("albarracin-2022-epistemic-communities", "Epistemic Communities under Active Inference", "Albarracin; Demekas; Ramstead; Heins", "albarracin2022epistemic.pdf", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9027706/", "Existing published journal article", ["epistemic", "albarracin", "demekas"]),
    ("maisto-2024-interactive-inference", "Interactive Inference: A Multi-Agent Model of Cooperative Joint Actions", "Maisto; Donnarumma; Pezzulo", None, "https://arxiv.org/pdf/2210.13113", "arXiv version, inspect footer", ["interactive", "maisto", "pezzulo"]),
    ("ruiz-serra-2025-factorised-active-inference", "Factorised Active Inference for Strategic Multi-Agent Interactions", "Ruiz-Serra; Sweeney; Harre", None, "https://www.ifaamas.org/Proceedings/aamas2025/pdfs/p1793.pdf", "AAMAS 2025 proceedings", ["factorised", "ruiz", "sweeney"]),
    ("gwon-2026-evidence-intervention", "Evidence and Intervention: A Coupled Active-Inference Extension of Rational Speech Act Models", "Gwon; Murphy; Chung", None, "https://arxiv.org/pdf/2610.04347", "arXiv preprint, inspect footer", ["evidence", "gwon", "murphy"]),
    ("millidge-2021-whence-expected-free-energy", "Whence the Expected Free Energy?", "Millidge; Tschantz; Buckley", None, "https://arxiv.org/pdf/2004.08128", "arXiv version of 2021 journal article, inspect footer", ["whence", "millidge", "tschantz"]),
    ("das-2019-tarmac", "TarMAC: Targeted Multi-Agent Communication", "Das et al.", "Das2019TarMAC.pdf", "https://proceedings.mlr.press/v97/das19a/das19a.pdf", "Existing arXiv:1810.11187v2, February 22, 2020; ICML 2019 article", ["tarmac", "das"]),
    ("kim-2019-schednet", "Learning to Schedule Communication in Multi-agent Reinforcement Learning", "Kim et al.", None, "https://yung-web.github.io/home/Publication/Conference/learning%20to%20schedule.pdf", "ICLR 2019 author-hosted paper", ["schedule", "kim"]),
    ("wang-2020-information-bottleneck-communication", "Learning Efficient Multi-agent Communication: An Information Bottleneck Approach", "Wang; He; Yu; Qiu; An; Rabinovich", None, "https://proceedings.mlr.press/v119/wang20i/wang20i.pdf", "ICML 2020 proceedings", ["bottleneck", "wang", "rabinovich"]),
    ("lin-2021-autoencoder-communication", "Learning to Ground Multi-Agent Communication with Autoencoders", "Lin et al.", None, "https://proceedings.neurips.cc/paper_files/paper/2021/file/80fee67c8a4c4989bf8a580b4bbb0cd2-Paper.pdf", "NeurIPS 2021 proceedings", ["autoencoders", "lin"]),
    ("hansen-ghrist-2021-discourse-sheaves", "Opinion Dynamics on Discourse Sheaves", "Hansen; Ghrist", "HansenGhrist2021Discourse.pdf", "https://jakobhansen.org/publications/opiniondynamics.pdf", "Existing arXiv:2005.12798v1, May 26, 2020; 2021 journal article", ["discourse", "hansen", "ghrist"]),
    ("taniguchi-2024-collective-predictive-coding", "Collective predictive coding hypothesis: symbol emergence as decentralized Bayesian inference", "Taniguchi", None, "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1353870/pdf", "Published Frontiers article", ["collective", "taniguchi"]),
    ("palacios-2020-hierarchical-markov-blankets", "On Markov blankets and hierarchical self-organisation", "Palacios; Razi; Parr; Kirchhoff; Friston", None, "https://discovery.ucl.ac.uk/id/eprint/10089189/1/Friston_1-s2.0-S0022519319304588-main.pdf", "Institutional published article", ["markov", "palacios", "razi"]),
    ("heins-2024-collective", "Collective behavior from surprise minimization", "Heins et al.", "heins2024collective.pdf", "https://eprints.whiterose.ac.uk/210480/8/heins-et-al-2024-collective-behavior-from-surprise-minimization.pdf", "Existing arXiv:2307.14804v4, May 14, 2024; PNAS 2024 article", ["collective", "heins"]),
    ("waade-2025-as-one", "As One and Many: Relating Individual and Emergent Group-Level Generative Models in Active Inference", "Thestrup Waade et al.", "waade2025asone.pdf", "https://www.mdpi.com/1099-4300/27/2/143", "Existing published Entropy article", ["one", "waade"]),
    ("maisto-2025-flock-joint-agency", "What the flock knows that the birds do not", "Maisto; Nuzzi; Pezzulo", None, "https://arxiv.org/pdf/2511.10835v2", "arXiv v2, January 29, 2026", ["flock", "maisto", "nuzzi"]),
    ("beck-2025-dynamic-markov-blanket-detection", "Dynamic Markov Blanket Detection for Macroscopic Physics Discovery", "Beck; Ramstead", None, "https://arxiv.org/pdf/2502.21217v1", "arXiv v1", ["dynamic", "beck", "ramstead"]),
    ("biehl-2021-technical-critique", "A Technical Critique of Some Parts of the Free Energy Principle", "Biehl; Pollock; Kanai", "biehl2021technical.pdf", "https://mdpi-res.com/d_attachment/entropy/entropy-23-00293/article_deploy/entropy-23-00293-v2.pdf", "Existing arXiv:2001.06408v3, February 28, 2021; Entropy 2021 article", ["technical", "biehl", "pollock"]),
]

ALTERNATES = {
    "friston-frith-2015-hermeneutics": [
        "https://discovery.ucl.ac.uk/id/eprint/1473042/1/Active%20inference%2C%20communication%20and%20hermeneutics.pdf",
        "https://www.fil.ion.ucl.ac.uk/~karl/Active%20inference%2C%20communication%20and%20hermeneutics.pdf",
    ],
}

VERSION_NOTES = {
    "maisto-2024-interactive-inference": "arXiv:2210.13113v2, December 10, 2022; IEEE journal publication February 2024",
    "gwon-2026-evidence-intervention": "arXiv:2610.04347v1, October 3, 2026 (arXiv record; PDF has no first-page arXiv marker)",
    "millidge-2021-whence-expected-free-energy": "arXiv:2004.08128v5, September 28, 2020; journal publication 2021",
    "kim-2019-schednet": "arXiv:1902.01554v1, February 5, 2019; marked published at ICLR 2019",
    "beck-2025-dynamic-markov-blanket-detection": "arXiv:2502.21217v1, February 28, 2025; PDF title-page date March 3, 2025",
}


def inspect_pdf(data: bytes, tokens: list[str]) -> dict[str, Any]:
    """Check readability and first-page identity using two PDF readers."""
    if not data.startswith(b"%PDF-"):
        raise ValueError("Response is not a PDF")
    reader = PdfReader(io.BytesIO(data))
    doc = fitz.open(stream=data, filetype="pdf")
    pages = len(reader.pages)
    if pages != len(doc) or pages == 0:
        raise ValueError("PDF page count disagrees or is zero")
    first = "\n".join(doc[i].get_text() for i in range(min(2, pages)))
    normalized = re.sub(r"\s+", " ", first).lower()
    absent = [token for token in tokens if token not in normalized]
    if absent:
        raise ValueError(f"First-two-page title/author identity tokens missing: {absent}")
    return {
        "page_count": pages,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "pdf_metadata": {str(k): str(v) for k, v in (reader.metadata or {}).items()},
        "arxiv_markers": sorted(set(re.findall(r"arXiv:[^\n]+", first))),
        "first_two_pages": first,
        "identity_tokens_verified": tokens,
    }


def obtain(paper: tuple) -> dict[str, Any]:
    """Reuse an immutable local copy or append one verified downloaded PDF."""
    slug, title, authors, existing, url, version, tokens = paper
    path = PDFS / (existing or f"{slug}.pdf")
    row = {"slug": slug, "title": title, "authors_expected": authors,
           "source_url": url, "local_path": path.relative_to(ROOT).as_posix(),
           "version_description": version, "new_or_reused": "reused" if existing else "new",
           "attempts": [], "status": "pending"}
    try:
        if path.exists():
            data = path.read_bytes()
            row["file_existed_before_run"] = True
        else:
            if existing:
                raise FileNotFoundError(f"Expected existing PDF is absent: {path}")
            last_error = None
            for candidate in [url, *ALTERNATES.get(slug, [])]:
                try:
                    response = requests.get(candidate, timeout=(20, 90), headers={"User-Agent": "ResearchLibrary/1.0 (academic reading)"})
                    attempt = {"url": candidate, "status_code": response.status_code, "final_url": response.url,
                               "content_type": response.headers.get("Content-Type", "")}
                    row["attempts"].append(attempt)
                    response.raise_for_status()
                    data = response.content
                    inspect_pdf(data, tokens)
                    row["download_url"] = response.url
                    break
                except Exception as exc:
                    last_error = exc
                    if row["attempts"]:
                        row["attempts"][-1]["error"] = f"{type(exc).__name__}: {exc}"
            else:
                raise last_error or ValueError("No download URL succeeded")
            row["file_existed_before_run"] = False
        evidence = inspect_pdf(data, tokens)
        first = evidence.pop("first_two_pages")
        row.update(evidence)
        if not path.exists():
            with path.open("xb") as stream:
                stream.write(data)
        (OUT / "reading" / f"{slug}.txt").write_text(first, encoding="utf-8")
        row["reading_extract"] = f"reading/{slug}.txt"
        row["status"] = "validated"
    except Exception as exc:
        row["status"] = "failed"
        row["error"] = f"{type(exc).__name__}: {exc}"
    return row


def write_reports(rows: list[dict[str, Any]]) -> None:
    """Record download provenance and validation without editing source notes."""
    manifest = {"date": "2026-11-07", "scope": "20 primary papers on active-inference communication and collective boundaries, selected November 7, 2026",
                "validation": "PDF signature, pypdf/PyMuPDF open and agreeing page counts, first-two-page title/author tokens; first-page preview sheets",
                "papers": rows}
    (OUT / "download_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# Active-inference communication reading set", "", "Downloaded or reused on November 7, 2026. Existing PDFs were preserved. Reused rows identify a primary source URL; they do not establish the original download URL of the pre-existing file.", "", "| Paper | Local PDF | Status | Pages | Version |", "|---|---|---|---:|---|"]
    for row in rows:
        lines.append(f"| {row['title']} | `{row['local_path']}` | {row['new_or_reused']}: {row['status']} | {row.get('page_count', '')} | {row['version_description']} |")
    lines += ["", "The JSON manifest records source URLs, redirect destinations for downloads, file sizes, SHA-256 identifiers, PDF metadata, and first-page identity checks. Text extracts contain the first two pages and are reading aids, not independent sources. New PDFs were appended only after validation."]
    for row in rows:
        if row["status"] == "failed":
            lines += ["", f"Access issue for {row['slug']}: {row.get('error', '')}"]
        if row.get("version_caveat"):
            lines += ["", f"Version note for {row['slug']}: {row['version_caveat']}"]
        if row.get("parser_warnings"):
            lines += ["", f"Reader note for {row['slug']}: pypdf reported {len(row['parser_warnings'])} nonfatal object-offset warnings. Both pypdf and PyMuPDF opened the file and reported the same page count. The downloaded PDF was retained without modification; the warning details are in the manifest."]
    (OUT / "downloads.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def make_previews(rows: list[dict[str, Any]]) -> None:
    """Render modest first-page contact sheets for human identity inspection."""
    valid = [row for row in rows if row["status"] == "validated"]
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 17)
    except OSError:
        font = ImageFont.load_default()
    for start in range(0, len(valid), 4):
        sheet = Image.new("RGB", (1100, 1600), "#eeeeee")
        draw = ImageDraw.Draw(sheet)
        for index, row in enumerate(valid[start:start + 4]):
            with fitz.open(ROOT / row["local_path"]) as doc:
                pix = doc[0].get_pixmap(matrix=fitz.Matrix(0.9, 0.9), alpha=False)
            thumb = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            thumb.thumbnail((520, 730))
            col, line = index % 2, index // 2
            x, y = col * 550 + 15, line * 800 + 40
            sheet.paste(thumb, (x, y))
            label = row["slug"]
            if len(label) > 52:
                label = label[:49] + "..."
            draw.text((x, y - 27), label, font=font, fill="black")
        sheet.save(OUT / "previews" / f"first-pages-{start // 4 + 1:02d}.jpg", quality=88)


def main() -> None:
    """Run one network-limited acquisition batch and emit bounded evidence."""
    for subdir in ("reading", "previews"):
        (OUT / subdir).mkdir(parents=True, exist_ok=True)
    manifest_path = OUT / "download_manifest.json"
    prior = {}
    if manifest_path.exists():
        prior = {row["slug"]: row for row in json.loads(manifest_path.read_text(encoding="utf-8"))["papers"]}
    pending = [paper for paper in PAPERS if prior.get(paper[0], {}).get("status") != "validated"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        acquired = {row["slug"]: row for row in pool.map(obtain, pending)}
    rows = []
    for paper in PAPERS:
        row = acquired.get(paper[0], prior.get(paper[0]))
        row["version_description"] = VERSION_NOTES.get(paper[0], paper[5])
        row["date_checked"] = "2026-11-07"
        if paper[0] in ("maisto-2024-interactive-inference", "gwon-2026-evidence-intervention"):
            row["version_source"] = paper[4].replace("/pdf/", "/abs/")
        rows.append(row)
    for row in rows:
        if row["slug"] == "beck-2025-dynamic-markov-blanket-detection":
            row["version_caveat"] = "The arXiv HTML view inspected by the source-note agent displayed August 24, 2026; the downloaded v1 PDF instead says March 3, 2025 and has a February 28, 2025 arXiv footer. The source is classified as a 2025 preprint."
    write_reports(rows)
    make_previews(rows)
    for row in rows:
        print(f"{row['status']}: {row['slug']} ({row.get('page_count', '?')} pages) {row.get('error', '')}", flush=True)


if __name__ == "__main__":
    main()
