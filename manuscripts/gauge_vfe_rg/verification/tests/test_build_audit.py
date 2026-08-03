"""Real-artifact RED contract for the machine-readable TeX build audit."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest


AUDIT_PATH = Path(__file__).resolve().parents[1] / "build_audit.py"


def audit_module():
    assert AUDIT_PATH.is_file(), "DEFECT [build audit module]: missing planned build_audit.py"
    spec = importlib.util.spec_from_file_location("build_audit_contract", AUDIT_PATH)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def audit_api():
    value = getattr(audit_module(), "audit_build", None)
    assert callable(value), "DEFECT [build audit API]: build_audit.py must export audit_build"
    return value


def artifacts(tmp_path: Path, log: str = "This is pdfTeX\nOutput written on main.pdf (1 page, 8 bytes).\n") -> tuple[Path, Path]:
    root, build = tmp_path / "repo", tmp_path / "build"
    root.mkdir()
    build.mkdir()
    (root / "main.tex").write_text("\\label{one}\n", encoding="utf-8")
    (build / "main.pdf").write_bytes(b"%PDF-1.4")
    (build / "main.log").write_text(log, encoding="utf-8")
    (build / "main.aux").write_text("\\newlabel{one}{{1}{1}}\n", encoding="utf-8")
    (build / "main.bbl").write_text("\\bibitem{x}\n", encoding="utf-8")
    (build / "main.toc").write_text("\\contentsline {section}{One}{1}{}%\n", encoding="utf-8")
    (build / "commands.json").write_text(json.dumps([{"argv": ["pdflatex", "main.tex"], "returncode": 0}]), encoding="utf-8")
    return root, build


def run_audit(root: Path, build: Path, defect: str):
    return audit_api()(repo_root=root, build_dir=build, source_revision="a" * 40, command_record=build / "commands.json")


def test_clean_real_artifacts_emit_all_required_audit_fields(tmp_path: Path):
    root, build = artifacts(tmp_path)
    outcome = run_audit(root, build, "clean artifact audit")
    required = ("ok", "tool_versions", "commands", "input_inventory", "source_manifest_digest", "pdf_sha256", "pdf_byte_count", "page_count", "artifact_hashes", "changed_pages", "duplicate_labels", "undefined_references", "undefined_citations", "rerun_requests", "fatal_errors", "overfull_boxes", "literal_double_question_marks", "invalid_status_tags", "stale_auxiliary_files")
    for field in required:
        assert hasattr(outcome, field), f"DEFECT [clean artifact audit]: missing {field}"
    assert outcome.ok is True, "DEFECT [clean artifact audit]: valid real artifacts must pass"


@pytest.mark.parametrize("kind, log", [("undefined_reference", "LaTeX Warning: Reference `missing' undefined.\n"), ("undefined_citation", "LaTeX Warning: Citation `missing' undefined.\n"), ("rerun", "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n"), ("fatal", "! Emergency stop.\n"), ("overfull", "Overfull \\hbox (2.0pt too wide)\n"), ("question_marks", "output ??\n"), ("invalid_status", "STATUS: NOT_A_STATUS\n")])
def test_each_real_bad_log_fixture_fails_closed(tmp_path: Path, kind: str, log: str):
    root, build = artifacts(tmp_path, log)
    outcome = run_audit(root, build, f"{kind} log fixture")
    assert getattr(outcome, "ok", None) is False, f"DEFECT [{kind} log fixture]: audit accepted real bad log"


@pytest.mark.parametrize("kind", ["missing_pdf", "missing_aux", "duplicate_label", "failed_command", "fabricated_metadata", "stale_aux"])
def test_missing_or_fabricated_real_artifacts_fail_closed(tmp_path: Path, kind: str):
    root, build = artifacts(tmp_path)
    if kind == "missing_pdf":
        (build / "main.pdf").unlink()
    elif kind == "missing_aux":
        (build / "main.aux").unlink()
    elif kind == "duplicate_label":
        (build / "main.aux").write_text("\\newlabel{one}{{1}{1}}\n\\newlabel{one}{{2}{2}}\n", encoding="utf-8")
    elif kind == "failed_command":
        (build / "commands.json").write_text(json.dumps([{"argv": ["pdflatex"], "returncode": 1}]), encoding="utf-8")
    elif kind == "fabricated_metadata":
        (build / "main.pdf").write_bytes(b"not a pdf")
    else:
        (build / "stale.aux").write_text("stale\n", encoding="utf-8")
    outcome = run_audit(root, build, f"{kind} artifact fixture")
    assert getattr(outcome, "ok", None) is False, f"DEFECT [{kind} artifact fixture]: audit accepted bad artifact state"
