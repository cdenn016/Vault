"""Real-artifact RED contract for machine-readable TeX build auditing."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest


AUDIT_PATH = Path(__file__).resolve().parents[1] / "build_audit.py"


class MissingAudit:
    def __init__(self, name: str):
        self.name = name

    def __call__(self, **_kwargs):
        return self


def audit_module():
    if not AUDIT_PATH.is_file():
        return None
    spec = importlib.util.spec_from_file_location("build_audit_contract", AUDIT_PATH)
    assert spec and spec.loader, "DEFECT [build audit module]: build_audit.py must be importable"
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def audit_api():
    loaded = audit_module()
    value = getattr(loaded, "audit_build", None) if loaded is not None else None
    return value if callable(value) else MissingAudit("audit_build")


def one_page_pdf() -> bytes:
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>",
        b"<< /Length 37 >>\nstream\nBT /F1 12 Tf 72 720 Td (audit) Tj ET\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    document = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for number, body in enumerate(objects, 1):
        offsets.append(len(document))
        document.extend(f"{number} 0 obj\n".encode() + body + b"\nendobj\n")
    xref = len(document)
    document.extend(f"xref\n0 {len(objects) + 1}\n".encode())
    document.extend(b"0000000000 65535 f \n")
    document.extend(b"".join(f"{offset:010d} 00000 n \n".encode() for offset in offsets[1:]))
    document.extend(f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    return bytes(document)


def validate_pdf_fixture(path: Path) -> None:
    # This intentionally does not trust the audit module: it checks the fixture's
    # PDF cross-reference, catalog, pages tree, and stream framing independently.
    raw = path.read_bytes()
    assert raw.startswith(b"%PDF-1.4\n") and b"xref\n0 6\n" in raw and raw.rstrip().endswith(b"%%EOF"), "DEFECT [PDF fixture]: missing PDF header/xref/trailer"
    assert b"/Type /Catalog /Pages 2 0 R" in raw and b"/Type /Pages /Kids [3 0 R] /Count 1" in raw, "DEFECT [PDF fixture]: invalid one-page catalog/pages tree"
    assert b"/Type /Page /Parent 2 0 R" in raw and b"stream\nBT /F1 12 Tf" in raw and b"endstream" in raw, "DEFECT [PDF fixture]: page content stream is malformed"


def validate_tex_fixture(root: Path, build: Path) -> None:
    source = (root / "main.tex").read_text(encoding="utf-8")
    auxiliary = (build / "main.aux").read_text(encoding="utf-8")
    bibliography = (build / "main.bbl").read_text(encoding="utf-8")
    assert r"\n" not in source and source.count("\n") == 4, "DEFECT [TeX fixture]: source must use actual line breaks and contain no literal \\n command"
    assert r"\label{one}" in source and r"\newlabel{one}" in auxiliary, "DEFECT [TeX fixture]: source and auxiliary label records disagree"
    assert r"\cite{x}" in source and r"\bibitem{x}" in bibliography, "DEFECT [TeX fixture]: source and bibliography citation records disagree"


def artifacts(tmp_path: Path, log: str | None = None) -> tuple[Path, Path, dict[str, object]]:
    root, build = tmp_path / "repo", tmp_path / "build"
    root.mkdir()
    build.mkdir()
    (root / "main.tex").write_text("\\documentclass{article}\n\\begin{document}\n\\label{one}Audit~\\cite{x}.\n\\end{document}\n", encoding="utf-8")
    pdf_bytes = one_page_pdf()
    (build / "main.pdf").write_bytes(pdf_bytes)
    validate_pdf_fixture(build / "main.pdf")
    if log is None:
        log = f"This is pdfTeX\nOutput written on main.pdf (1 page, {len(pdf_bytes)} bytes).\n"
    (build / "main.log").write_text(log, encoding="utf-8")
    (build / "main.aux").write_text("\\relax \n\\newlabel{one}{{1}{1}}\n", encoding="utf-8")
    (build / "main.bbl").write_text("\\begin{thebibliography}{1}\n\\bibitem{x} X.\n\\end{thebibliography}\n", encoding="utf-8")
    (build / "main.toc").write_text("\\contentsline {section}{Audit}{1}{}%\n", encoding="utf-8")
    validate_tex_fixture(root, build)
    commands = [
        {"argv": ["pdflatex", "-interaction=nonstopmode", "main.tex"], "returncode": 0, "tool_version": "fixture-pdftex-1"},
        {"argv": ["bibtex", "main"], "returncode": 0, "tool_version": "fixture-bibtex-1"},
        {"argv": ["pdflatex", "-interaction=nonstopmode", "main.tex"], "returncode": 0, "tool_version": "fixture-pdftex-1"},
        {"argv": ["pdflatex", "-interaction=nonstopmode", "main.tex"], "returncode": 0, "tool_version": "fixture-pdftex-1"},
    ]
    (build / "commands.json").write_text(json.dumps(commands), encoding="utf-8")
    inventory = {"main.tex": hashlib.sha256((root / "main.tex").read_bytes()).hexdigest()}
    expected = {
        "commands": commands,
        "tool_versions": {"pdflatex": "fixture-pdftex-1", "bibtex": "fixture-bibtex-1"},
        "input_inventory": inventory,
        "source_manifest_digest": hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
        "pdf_sha256": hashlib.sha256(pdf_bytes).hexdigest(),
        "pdf_byte_count": len(pdf_bytes),
        "page_count": 1,
        "artifact_hashes": {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(build.iterdir()) if path.is_file()},
    }
    return root, build, expected


def run_audit(root: Path, build: Path, defect: str):
    return audit_api()(repo_root=root, build_dir=build, source_revision="a" * 40, command_record=build / "commands.json")


def require_field(value, name: str, defect: str):
    assert hasattr(value, name), f"DEFECT [{defect}]: missing {name}"
    return getattr(value, name)


def test_clean_parseable_artifacts_emit_verified_metadata_not_fabricated_defaults(tmp_path: Path):
    root, build, expected = artifacts(tmp_path)
    outcome = run_audit(root, build, "clean artifact audit")
    required = ("ok", "tool_versions", "commands", "input_inventory", "source_manifest_digest", "pdf_sha256", "pdf_byte_count", "page_count", "artifact_hashes", "changed_pages", "duplicate_labels", "undefined_references", "undefined_citations", "rerun_requests", "fatal_errors", "overfull_boxes", "literal_double_question_marks", "invalid_status_tags", "stale_auxiliary_files")
    for field in required:
        require_field(outcome, field, "clean artifact audit")
    pdf = build / "main.pdf"
    assert require_field(outcome, "ok", "clean artifact audit") is True, "DEFECT [clean artifact audit]: valid artifacts must pass"
    for field in ("pdf_sha256", "pdf_byte_count", "page_count", "commands", "tool_versions", "input_inventory", "source_manifest_digest", "artifact_hashes"):
        assert require_field(outcome, field, "clean artifact audit") == expected[field], f"DEFECT [clean artifact audit]: exact {field} does not match fixture bytes/records"
    assert require_field(outcome, "changed_pages", "clean artifact audit") == [1], "DEFECT [clean artifact audit]: changed-page selection must identify page 1"


@pytest.mark.parametrize("kind, log", [("undefined_reference", "LaTeX Warning: Reference `missing' undefined.\n"), ("undefined_citation", "LaTeX Warning: Citation `missing' undefined.\n"), ("rerun", "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n"), ("fatal", "! Emergency stop.\n"), ("overfull", "Overfull \\hbox (2.0pt too wide)\n"), ("question_marks", "output ??\n"), ("invalid_status", "STATUS: NOT_A_STATUS\n")])
def test_each_real_bad_log_fixture_fails_closed(tmp_path: Path, kind: str, log: str):
    root, build, _ = artifacts(tmp_path, log)
    outcome = run_audit(root, build, f"{kind} log fixture")
    assert require_field(outcome, "ok", f"{kind} log fixture") is False, f"DEFECT [{kind} log fixture]: audit accepted real bad log"


@pytest.mark.parametrize("kind", ["missing_pdf", "missing_aux", "duplicate_label", "failed_command", "fabricated_metadata", "stale_aux"])
def test_missing_or_fabricated_real_artifacts_fail_closed(tmp_path: Path, kind: str):
    root, build, _ = artifacts(tmp_path)
    if kind == "missing_pdf":
        (build / "main.pdf").unlink()
    elif kind == "missing_aux":
        (build / "main.aux").unlink()
    elif kind == "duplicate_label":
        (build / "main.aux").write_text("\\newlabel{one}{{1}{1}}\n\\newlabel{one}{{2}{2}}\n", encoding="utf-8")
    elif kind == "failed_command":
        commands = json.loads((build / "commands.json").read_text(encoding="utf-8"))
        commands[-1]["returncode"] = 1
        (build / "commands.json").write_text(json.dumps(commands), encoding="utf-8")
    elif kind == "fabricated_metadata":
        (build / "main.pdf").write_bytes(b"not a PDF")
        (build / "main.pdf.metadata.json").write_text(json.dumps({"page_count": 1, "sha256": "fabricated"}), encoding="utf-8")
    else:
        (build / "stale.aux").write_text("stale\n", encoding="utf-8")
    outcome = run_audit(root, build, f"{kind} artifact fixture")
    assert require_field(outcome, "ok", f"{kind} artifact fixture") is False, f"DEFECT [{kind} artifact fixture]: audit accepted bad artifact state"
