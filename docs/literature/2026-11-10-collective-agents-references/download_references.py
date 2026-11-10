"""Acquire open-access copies of the references in references.json and validate each local PDF.

For every reference the script looks for an open copy at arXiv (when the record carries an arXiv identifier) and at the
open-access locations that OpenAlex lists for the DOI. A file is kept only if it is a readable PDF and, when it has a
text layer, its first pages carry the first author's surname and a distinctive title word. Existing PDFs are never
overwritten. References without an open copy are recorded as access gaps; nothing behind a sign-in is requested.
"""

from __future__ import annotations

import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import threading
import time
from typing import Any
import unicodedata

for name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[name] = "4"

import pymupdf as fitz
import requests

ROOT = Path(__file__).resolve().parents[3]
PDFS = ROOT / "sources" / "pdfs"
OUT = Path(__file__).resolve().parent
HEADERS = {"User-Agent": "ResearchLibrary/1.0 (academic reading)"}
MAX_BYTES = 60 * 1024 * 1024
ARXIV_LOCK = threading.Lock()
ARXIV_LAST = [0.0]
# The arXiv preprint of Raz and Sims carries an earlier title than the journal article.
IDENTITY_OVERRIDES = {"raz-2009-estimating-lieb-robinson": ["raz", "anharmonic"]}


def ascii_low(text: str) -> str:
    text = re.sub(r"\\[`'\"^~=.]|\\[a-zA-Z]+\s*|[{}$]", "", text)
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()


def identity_tokens(ref: dict[str, Any]) -> list[str]:
    """First-author surname and the longest early title word, both in ASCII lower case."""
    tokens = []
    if ref["authors"]:
        first = ref["authors"][0]
        surname = first.split(",")[0] if "," in first else first.split()[-1]
        parts = re.findall(r"[a-z]+", ascii_low(surname))
        if parts:
            tokens.append(max(parts, key=len))
    words = [w for w in re.findall(r"[a-z]+", ascii_low(ref["title"])) if len(w) >= 5][:5]
    if words:
        tokens.append(max(words, key=len))
    return tokens


def arxiv_get(url: str) -> requests.Response:
    """Serialize arXiv requests and space them by three seconds."""
    with ARXIV_LOCK:
        wait = 3.0 - (time.monotonic() - ARXIV_LAST[0])
        if wait > 0:
            time.sleep(wait)
        try:
            return requests.get(url, timeout=(20, 120), headers=HEADERS)
        finally:
            ARXIV_LAST[0] = time.monotonic()


def openalex(ref: dict[str, Any]) -> dict[str, Any]:
    """Abstract and open-access PDF locations from the OpenAlex record of the DOI or arXiv identifier."""
    if ref["doi"]:
        ident = "doi:" + ref["doi"]
    elif re.fullmatch(r"\d{4}\.\d{4,5}", ref["eprint"] or ""):
        ident = "doi:10.48550/arXiv." + ref["eprint"]
    else:
        return {}
    url = "https://api.openalex.org/works/" + requests.utils.quote(ident, safe=":/")
    for attempt in range(3):
        response = requests.get(url, timeout=(20, 60), headers=HEADERS,
                                params={"select": "id,title,publication_year,abstract_inverted_index,open_access,best_oa_location,primary_location,locations,ids"})
        if response.status_code == 429:
            time.sleep(4 * (attempt + 1))
            continue
        if response.status_code != 200:
            return {"openalex_status": response.status_code}
        break
    else:
        return {"openalex_status": 429}
    work = response.json()
    index = work.get("abstract_inverted_index") or {}
    words = sorted((pos, word) for word, positions in index.items() for pos in positions)
    urls: list[str] = []
    for loc in [work.get("best_oa_location"), work.get("primary_location"), *(work.get("locations") or [])]:
        if loc and loc.get("is_oa") and loc.get("pdf_url") and loc["pdf_url"] not in urls:
            urls.append(loc["pdf_url"])
    oa_url = (work.get("open_access") or {}).get("oa_url")
    if oa_url and oa_url not in urls:
        urls.append(oa_url)
    pmcid = (work.get("ids") or {}).get("pmcid", "")
    match = re.search(r"PMC\d+", pmcid or "")
    if match:
        urls.append(f"https://europepmc.org/articles/{match.group(0)}?pdf=render")
    return {"openalex_status": 200, "openalex_id": work.get("id"), "openalex_title": work.get("title"),
            "openalex_year": work.get("publication_year"), "abstract": " ".join(word for _, word in words),
            "oa_status": (work.get("open_access") or {}).get("oa_status"), "oa_pdf_urls": urls}


def inspect_pdf(data: bytes, tokens: list[str]) -> dict[str, Any]:
    """Check that the bytes are a readable PDF and, where there is text, that the first pages name the paper."""
    if not data.startswith(b"%PDF-"):
        raise ValueError("response is not a PDF")
    with fitz.open(stream=data, filetype="pdf") as doc:
        pages = len(doc)
        if pages == 0:
            raise ValueError("PDF has no pages")
        first = "\n".join(doc[i].get_text() for i in range(min(3, pages)))
        extract = "\n".join(doc[i].get_text() for i in range(min(10, pages)))
    normalized = re.sub(r"\s+", " ", ascii_low(first))
    if len(normalized) < 200:
        identity = "no text layer: identity not machine-checked"
    else:
        absent = [t for t in tokens if t not in normalized and t not in normalized.replace(" ", "").replace("-", "")]
        if absent:
            raise ValueError(f"identity tokens missing from the first pages: {absent}")
        identity = "first-pages text carries " + ", ".join(tokens)
    return {"page_count": pages, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "identity": identity, "extract": extract[:60000]}


def obtain(ref: dict[str, Any]) -> dict[str, Any]:
    """Find, validate and store one open copy; record every attempt."""
    slug = ref["slug"]
    path = PDFS / f"{slug}.pdf"
    row: dict[str, Any] = {k: ref[k] for k in ("key", "slug", "title", "year", "doi", "eprint")}
    row.update({"local_path": path.relative_to(ROOT).as_posix(), "attempts": [], "status": "pending"})
    tokens = IDENTITY_OVERRIDES.get(slug) or identity_tokens(ref)
    try:
        meta = openalex(ref)
    except Exception as exc:
        meta = {"openalex_status": f"{type(exc).__name__}: {exc}"}
    row.update(meta)
    candidates: list[str] = []
    if ref["eprint"]:
        candidates.append("https://arxiv.org/pdf/" + ref["eprint"])
    candidates += [u for u in meta.get("oa_pdf_urls", []) if u not in candidates]
    data = None
    if path.exists():
        data = path.read_bytes()
        row["file_existed_before_run"] = True
    else:
        row["file_existed_before_run"] = False
        for url in candidates[:6]:
            attempt: dict[str, Any] = {"url": url}
            row["attempts"].append(attempt)
            try:
                if "arxiv.org" in url:
                    response = arxiv_get(url)
                else:
                    response = requests.get(url, timeout=(20, 120), headers=HEADERS, stream=True)
                attempt.update({"status_code": response.status_code, "final_url": response.url,
                                "content_type": response.headers.get("Content-Type", "")})
                response.raise_for_status()
                length = int(response.headers.get("Content-Length") or 0)
                if length > MAX_BYTES:
                    raise ValueError(f"file larger than {MAX_BYTES} bytes")
                body = response.content
                if len(body) > MAX_BYTES:
                    raise ValueError(f"file larger than {MAX_BYTES} bytes")
                if not body.startswith(b"%PDF-") and b"citation_pdf_url" in body:
                    # A landing page: follow the PDF address that the page itself declares.
                    match = re.search(rb'citation_pdf_url"\s+content="([^"]+)"|content="([^"]+)"\s+name="citation_pdf_url"', body)
                    if match:
                        declared = requests.compat.urljoin(response.url, (match.group(1) or match.group(2)).decode("utf-8", "replace").replace("&amp;", "&"))
                        attempt["declared_pdf_url"] = declared
                        response = requests.get(declared, timeout=(20, 120), headers=HEADERS)
                        response.raise_for_status()
                        body = response.content
                        if len(body) > MAX_BYTES:
                            raise ValueError(f"file larger than {MAX_BYTES} bytes")
                inspect_pdf(body, tokens)
                data = body
                row["download_url"] = response.url
                break
            except Exception as exc:
                attempt["error"] = f"{type(exc).__name__}: {exc}"[:300]
    if data is None:
        row["status"] = "no open copy" if not candidates else "failed"
        return row
    try:
        evidence = inspect_pdf(data, tokens)
        extract = evidence.pop("extract")
        row.update(evidence)
        if not path.exists():
            with path.open("xb") as stream:
                stream.write(data)
        (OUT / "reading" / f"{slug}.txt").write_text(extract, encoding="utf-8")
        row["reading_extract"] = f"reading/{slug}.txt"
        row["status"] = "validated"
    except Exception as exc:
        row["status"] = "failed"
        row["error"] = f"{type(exc).__name__}: {exc}"[:300]
    return row


def write_reports(rows: list[dict[str, Any]]) -> None:
    """Write the local manifest, the published provenance (no abstracts, no extracts) and the download table."""
    (OUT / "download_manifest.json").write_text(json.dumps({"date": "2026-11-10", "papers": rows}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    keep = ("key", "slug", "title", "year", "doi", "eprint", "local_path", "status", "file_existed_before_run", "download_url",
            "page_count", "bytes", "sha256", "identity", "oa_status", "openalex_id", "error")
    public = []
    for row in rows:
        entry = {k: row[k] for k in keep if k in row}
        entry["attempts"] = [{k: a[k] for k in ("url", "status_code", "error") if k in a} for a in row.get("attempts", [])]
        public.append(entry)
    (OUT / "provenance.json").write_text(json.dumps({"date": "2026-11-10", "validation": "PDF signature, PyMuPDF open, page count, first-pages surname and title-word check where a text layer exists", "papers": public}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    got = [r for r in rows if r["status"] == "validated"]
    lines = ["# Collective agents references: download record", "",
             f"Checked on November 10, 2026. {len(got)} of {len(rows)} references have a validated local PDF; the others have no open copy that passed validation.", "",
             "| Source note | Local PDF | Pages | Identity check |", "|---|---|---|---|"]
    for row in sorted(got, key=lambda r: r["slug"]):
        lines.append(f"| [[{row['slug']}]] | `{row['local_path']}` | {row['page_count']} | {row['identity']} |")
    lines += ["", "## References without a local copy", "", "| Source note | Outcome |", "|---|---|"]
    for row in sorted((r for r in rows if r["status"] != "validated"), key=lambda r: r["slug"]):
        why = row["status"]
        errors = [a.get("error", "") for a in row.get("attempts", []) if a.get("error")]
        if errors:
            why += ": " + errors[-1].replace("|", "/")[:140]
        lines.append(f"| [[{row['slug']}]] | {why} |")
    (OUT / "downloads.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """Run one acquisition pass; references validated by an earlier pass are not requested again."""
    (OUT / "reading").mkdir(exist_ok=True)
    refs = json.loads((OUT / "references.json").read_text(encoding="utf-8"))
    manifest_path = OUT / "download_manifest.json"
    prior: dict[str, dict[str, Any]] = {}
    if manifest_path.exists():
        prior = {row["slug"]: row for row in json.loads(manifest_path.read_text(encoding="utf-8"))["papers"]}
    pending = [ref for ref in refs if prior.get(ref["slug"], {}).get("status") != "validated"]
    if len(sys.argv) > 1:
        pending = [ref for ref in pending if ref["slug"] in sys.argv[1:]]
    acquired: dict[str, dict[str, Any]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for row in pool.map(obtain, pending):
            acquired[row["slug"]] = row
            print(f"{row['status']}: {row['slug']} ({row.get('page_count', '-')} pages)", flush=True)
    rows = [acquired.get(ref["slug"], prior.get(ref["slug"])) for ref in refs]
    write_reports(rows)
    print("validated", sum(1 for r in rows if r["status"] == "validated"), "of", len(rows), flush=True)


if __name__ == "__main__":
    main()
