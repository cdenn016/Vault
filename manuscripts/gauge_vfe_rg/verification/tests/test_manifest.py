"""Manifest mutation controls for every release-bound input class."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
RUNNER_PATH = ROOT / "verification" / "run_checks.py"


def runner_module():
    spec = importlib.util.spec_from_file_location("gauge_vfe_rg_manifest_runner", RUNNER_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verifier():
    module = runner_module()
    assert hasattr(module, "verify_release_manifest"), "missing fail-closed manifest verifier"
    return module.verify_release_manifest


@pytest.mark.parametrize(
    "path",
    [
        "main.tex", "SPEC.md", "../references.bib", "scientific_report.sty", "build.ps1",
        "verification/claims.json", "verification/run_checks.py", "verification/requirements.txt",
        "verification/release-schema.json", "verification/release-policy.json",
        "verification/release_lifecycle.py", "verification/build_audit.py",
        "verification/tests/test_factorization_gap.py", "verification/tests/test_release_cli.py",
        "verification/tests/test_manifest.py", "verification/tests/test_release_lifecycle.py",
        "verification/tests/test_build_audit.py",
    ],
)
def test_manifest_rejects_a_byte_mutation_to_every_bound_input(path: str, tmp_path: Path):
    outcome = verifier()(root=ROOT, result=tmp_path / "result.json", mutation={"path": path, "kind": "byte"})
    assert outcome.ok is False
    assert outcome.reason == "manifest_mismatch"


@pytest.mark.parametrize(
    "mutation",
    [
        {"kind": "malformed_json", "path": "verification/claims.json"},
        {"kind": "missing_manifest_field", "field": "semantic_payload_digest"},
        {"kind": "extra_manifest_field", "field": "unbound"},
        {"kind": "missing_bound_path", "path": "SPEC.md"},
        {"kind": "unexpected_bound_path", "path": "surprise.tex"},
        {"kind": "line_endings", "path": "main.tex"},
        {"kind": "semantic_payload", "path": "main.tex"},
        {"kind": "unknown_check", "check_id": "CHK-UNKNOWN"},
        {"kind": "duplicate_check", "check_id": "CHK-DUPLICATE"},
        {"kind": "git_revision", "revision": "0" * 40},
        {"kind": "nonfinite", "value": "NaN"},
        {"kind": "nonfinite", "value": "Infinity"},
    ],
)
def test_manifest_rejects_each_structural_mutation(mutation: dict[str, str], tmp_path: Path):
    outcome = verifier()(root=ROOT, result=tmp_path / "result.json", mutation=mutation)
    assert outcome.ok is False
    assert outcome.reason in {"manifest_mismatch", "invalid_result", "revision_mismatch"}
