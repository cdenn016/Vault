"""Retrieve authorized author-hosted papers sequentially and record provenance."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent
VAULT = ROOT.parents[2]


def save_json(path: Path, value: object) -> None:
    """Write a UTF-8 provenance record."""
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    """Download one paper at a time, validate PDF parsing, and extract page text."""
    sys.stdout.reconfigure(encoding="utf-8")
    rows = json.loads((ROOT / "selection.json").read_text(encoding="utf-8"))
    prior_path = ROOT / "downloads.json"
    prior = json.loads(prior_path.read_text(encoding="utf-8")) if prior_path.exists() else []
    done = {row["id"]: row for row in prior}
    (ROOT / "extracted").mkdir(exist_ok=True)
    (ROOT / "packets").mkdir(exist_ok=True)
    for row in sorted(rows, key=lambda z: (z["lane"] != "physics", z["lane"] != "active", z["id"])):
        if not row["selected"] or row["lane"] == "book":
            continue
        if row["id"] in done and done[row["id"]].get("status") == "downloaded":
            continue
        url = row["pdf_url"]
        if "arxiv.org/abs/" in url:
            url = url.replace("http://", "https://").replace("/abs/", "/pdf/")
        result = {"id": row["id"], "slug": row["slug"], "url": url, "retrieved": "2026-11-01"}
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ResearchLibrary/1.0 (personal scholarly collection)"})
            with urllib.request.urlopen(req, timeout=25) as response:
                data = response.read()
                result["resolved_url"] = response.url
                result["content_type"] = response.headers.get("Content-Type")
            if not data.startswith(b"%PDF-"):
                raise ValueError("Response is not a PDF")
            doc = pymupdf.open(stream=data, filetype="pdf")
            pages = [page.get_text() for page in doc]
            if not pages or sum(map(len, pages)) < 100:
                raise ValueError("PDF has no useful extracted text")
            dest = VAULT / "sources" / "pdfs" / (row["slug"] + ".pdf")
            if dest.exists() and dest.read_bytes() != data:
                raise FileExistsError("Existing PDF differs; preserved existing bytes")
            if not dest.exists():
                dest.write_bytes(data)
            text_path = ROOT / "extracted" / (row["slug"] + ".txt")
            text_path.write_text("\n".join(f"\n--- PDF PAGE {i + 1} ---\n{text}" for i, text in enumerate(pages)), encoding="utf-8")
            # A reading packet is a locator aid. Notes must identify which pages were read.
            keep = set(range(min(3, len(pages))))
            for i, text in enumerate(pages):
                if re.search(r"(?im)^\s*(?:\d+[. ]+)?(?:conclusions?|discussion|summary|concluding remarks)\b", text):
                    keep.update(range(max(0, i - 1), min(len(pages), i + 2)))
            keep.update(range(max(0, len(pages) - 2), len(pages)))
            packet_path = ROOT / "packets" / (row["slug"] + ".txt")
            packet_path.write_text(json.dumps(row, ensure_ascii=False) + "\n" + "\n".join(f"\n--- PDF PAGE {i + 1} ---\n{pages[i]}" for i in sorted(keep)), encoding="utf-8")
            result.update({"status": "downloaded", "pdf": str(dest.relative_to(VAULT)).replace("\\", "/"), "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "pages": len(pages), "pdf_metadata": doc.metadata, "text": str(text_path), "packet": str(packet_path), "packet_pages": [i + 1 for i in sorted(keep)]})
        except Exception as exc:
            result.update({"status": "failed", "error": str(exc)})
        done[row["id"]] = result
        save_json(prior_path, sorted(done.values(), key=lambda z: z["id"]))
        print(f"{row['id']:3} {result['status']}: {row['title']}", flush=True)
        time.sleep(0.12)
    print(json.dumps({"downloaded": sum(r["status"] == "downloaded" for r in done.values()), "failed": [r for r in done.values() if r["status"] != "downloaded"]}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
