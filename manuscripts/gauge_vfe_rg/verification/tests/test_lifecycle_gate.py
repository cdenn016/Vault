"""Real Git-history contract for S/E/C/W lifecycle gates."""

from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path

import pytest


GATE_PATH = Path(__file__).resolve().parents[1] / "lifecycle_gate.py"


def git(repo: Path, *args: str) -> str:
    completed = subprocess.run(["git", *args], cwd=repo, text=True, capture_output=True, check=False)
    assert completed.returncode == 0, f"fixture git command failed: git {' '.join(args)}: {completed.stderr}"
    return completed.stdout.strip()


def commit(repo: Path, message: str) -> str:
    git(repo, "add", "-A")
    git(repo, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-m", message)
    return git(repo, "rev-parse", "HEAD")


def write(repo: Path, relative: str, text: str = "x\n") -> None:
    path = repo / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def history(tmp_path: Path) -> tuple[Path, dict[str, str]]:
    repo = tmp_path / "history"
    repo.mkdir()
    git(repo, "init")
    write(repo, "manuscripts/gauge_vfe_rg/main.tex")
    revisions = {"S": commit(repo, "source")}
    write(repo, "manuscripts/gauge_vfe_rg/verification/current-results.json", "{}\n")
    write(repo, "docs/derivations/evidence/numerics.json", "{}\n")
    revisions["E"] = commit(repo, "evidence")
    write(repo, "docs/derivations/closure-attestation.json", "{}\n")
    write(repo, "docs/derivations/release.json", "{}\n")
    revisions["C"] = commit(repo, "closure")
    write(repo, "sources/manuscripts/gauge-vfe-rg-cross-scale-operator-theory-2026-08-03.md")
    write(repo, "wiki/concepts/Coarse Graining.md")
    write(repo, "index.md")
    write(repo, "log.md")
    revisions["W"] = commit(repo, "wiki")
    return repo, revisions


def gate_module():
    assert GATE_PATH.is_file(), "DEFECT [lifecycle module]: missing planned lifecycle_gate.py"
    spec = importlib.util.spec_from_file_location("lifecycle_gate_contract", GATE_PATH)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def require_gate(name: str, defect: str):
    value = getattr(gate_module(), name, None)
    assert callable(value), f"DEFECT [{defect}]: lifecycle_gate.py must export {name}"
    return value


def test_gate_accepts_real_allowed_s_e_c_w_history_and_authorized_source_note(tmp_path: Path):
    repo, revisions = history(tmp_path)
    validate = require_gate("validate_lifecycle", "real S/E/C/W gate")
    outcome = validate(repo, revisions["S"], revisions["E"], revisions["C"], revisions["W"])
    assert getattr(outcome, "ok", None) is True, "DEFECT [real S/E/C/W gate]: allowed real history was rejected"


@pytest.mark.parametrize("boundary, forbidden", [("S..E", "manuscripts/gauge_vfe_rg/main.tex"), ("S..E", "manuscripts/references.bib"), ("E..C", "docs/reviews/adversarial.md"), ("C..W", "docs/derivations/release.json")])
def test_gate_rejects_real_forbidden_change_at_each_boundary(tmp_path: Path, boundary: str, forbidden: str):
    repo, revisions = history(tmp_path)
    write(repo, forbidden, "forbidden\n")
    bad = commit(repo, "forbidden")
    revised = dict(revisions)
    if boundary == "S..E":
        revised["E"] = bad
    elif boundary == "E..C":
        revised["C"] = bad
    else:
        revised["W"] = bad
    outcome = require_gate("validate_lifecycle", f"forbidden {boundary} {forbidden}")(repo, revised["S"], revised["E"], revised["C"], revised["W"])
    assert getattr(outcome, "ok", None) is False, f"DEFECT [forbidden {boundary}]: gate accepted {forbidden}"


def test_gate_parses_real_nul_delimited_add_modify_delete_rename_and_copy_statuses(tmp_path: Path):
    repo, revisions = history(tmp_path)
    write(repo, "sources/manuscripts/space name.md", "one\n")
    write(repo, "sources/manuscripts/delete me.md", "delete\n")
    add = commit(repo, "add")
    write(repo, "sources/manuscripts/space name.md", "two\n")
    (repo / "sources/manuscripts/delete me.md").unlink()
    (repo / "sources/manuscripts/copied name.md").write_text("two\n", encoding="utf-8")
    modify = commit(repo, "modify")
    git(repo, "mv", "sources/manuscripts/space name.md", "sources/manuscripts/renamed name.md")
    rename = commit(repo, "rename")
    raw = subprocess.run(["git", "diff", "--name-status", "-z", "-C", "--find-copies-harder", add, rename], cwd=repo, capture_output=True, check=True).stdout
    assert b"\x00" in raw and b"renamed name.md" in raw, "fixture must contain real NUL-safe Git status data"
    parser = require_gate("parse_name_status_z", "NUL-safe diff parser")
    entries = parser(raw)
    assert {entry.status[0] for entry in entries} >= {"A", "M", "D", "R", "C"}, "DEFECT [NUL-safe parser]: real add/modify/delete/rename/copy statuses were not preserved"


def test_gate_rejects_invalid_revision_and_failed_publication_byte_identity(tmp_path: Path):
    repo, revisions = history(tmp_path)
    validate = require_gate("validate_lifecycle", "invalid revision and publication identity")
    invalid = validate(repo, "0" * 40, revisions["E"], revisions["C"], revisions["W"])
    assert getattr(invalid, "ok", None) is False, "DEFECT [invalid revision]: gate accepted nonexistent revision"
    write(repo, "manuscripts/gauge_vfe_rg/main.tex", "changed after W\n")
    publication = commit(repo, "publication drift")
    identity = require_gate("verify_publication_identity", "publication byte identity")(repo, revisions["W"], publication)
    assert getattr(identity, "ok", None) is False, "DEFECT [publication identity]: gate accepted altered bound bytes"
