"""Release-revision allowlist contract for source, evidence, closure, and wiki phases."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
LIFECYCLE_PATH = ROOT / "verification" / "release_lifecycle.py"


def lifecycle_module():
    assert LIFECYCLE_PATH.is_file(), "missing release lifecycle implementation"
    spec = importlib.util.spec_from_file_location("gauge_vfe_rg_release_lifecycle", LIFECYCLE_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(boundary: str, changed_paths: list[str]):
    module = lifecycle_module()
    assert hasattr(module, "validate_revision_boundary"), "missing revision-boundary validator"
    return module.validate_revision_boundary(boundary=boundary, changed_paths=changed_paths)


@pytest.mark.parametrize(
    ("boundary", "changed_paths"),
    [
        ("S..E", ["manuscripts/gauge_vfe_rg/verification/current-results.json", "docs/derivations/evidence/numerics.json"]),
        ("E..C", ["docs/derivations/closure-attestation.json", "docs/derivations/release.json"]),
        ("C..W", ["wiki/sources/gauge-vfe-rg-2026-08-03.md", "wiki/concepts/Coarse Graining.md", "index.md", "log.md"]),
    ],
)
def test_each_revision_boundary_accepts_only_its_allowlist(boundary: str, changed_paths: list[str]):
    outcome = validate(boundary, changed_paths)
    assert outcome.allowed is True
    assert outcome.forbidden_paths == []


@pytest.mark.parametrize(
    ("boundary", "forbidden_path"),
    [
        ("S..E", "manuscripts/gauge_vfe_rg/07_restrictions.tex"),
        ("S..E", "manuscripts/references.bib"),
        ("S..E", "manuscripts/gauge_vfe_rg/verification/tests/test_manifest.py"),
        ("S..E", "manuscripts/gauge_vfe_rg/verification/run_checks.py"),
        ("S..E", "wiki/concepts/Coarse Graining.md"),
        ("E..C", "manuscripts/gauge_vfe_rg/verification/current-results.json"),
        ("E..C", "docs/reviews/adversarial.md"),
        ("C..W", "manuscripts/gauge_vfe_rg/main.tex"),
        ("C..W", "docs/derivations/release.json"),
    ],
)
def test_each_revision_boundary_rejects_an_injected_forbidden_file(boundary: str, forbidden_path: str):
    outcome = validate(boundary, [forbidden_path])
    assert outcome.allowed is False
    assert outcome.forbidden_paths == [forbidden_path]
