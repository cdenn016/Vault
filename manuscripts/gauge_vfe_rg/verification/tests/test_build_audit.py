"""Machine-readable build-audit contract and malformed-log fixtures."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
AUDIT_PATH = ROOT / "verification" / "build_audit.py"


def audit_module():
    assert AUDIT_PATH.is_file(), "missing build-audit implementation"
    spec = importlib.util.spec_from_file_location("gauge_vfe_rg_build_audit", AUDIT_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def audit(log_text: str):
    module = audit_module()
    assert hasattr(module, "audit_build_log"), "missing build-log audit interface"
    return module.audit_build_log(log_text=log_text, root=ROOT, revision="a" * 40)


def test_clean_fixture_records_every_required_machine_readable_field():
    outcome = audit("This is pdfTeX\nOutput written on main.pdf (12 pages, 12345 bytes).\n")
    assert outcome.ok is True
    assert outcome.revision == "a" * 40
    assert outcome.tool_versions
    assert outcome.input_inventory
    assert outcome.source_manifest_digest
    assert outcome.pdf_sha256
    assert outcome.pdf_byte_count == 12345
    assert outcome.page_count == 12
    assert outcome.undefined_references == []
    assert outcome.undefined_citations == []
    assert outcome.rerun_requests == []
    assert outcome.overfull_boxes == []
    assert outcome.literal_double_question_marks == []
    assert outcome.invalid_status_tags == []
    assert outcome.stale_auxiliary_files == []


@pytest.mark.parametrize(
    "log_text",
    [
        "LaTeX Warning: Reference `missing' on page 2 undefined.\n",
        "LaTeX Warning: Citation `missing-source' on page 2 undefined.\n",
        "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n",
        "Overfull \\hbox (12.0pt too wide) in paragraph at lines 1--2\n",
        "Rendered output contains ??\n",
        "STATUS: NOT_A_STATUS\n",
        "stale auxiliary file: main.aux\n",
    ],
)
def test_build_audit_fails_closed_for_each_bad_log_fixture(log_text: str):
    outcome = audit(log_text)
    assert outcome.ok is False
    assert outcome.failures
