"""Real, monotone Git-history RED contract for S/E/C/W lifecycle gates."""

from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path

import pytest


GATE_PATH = Path(__file__).resolve().parents[1] / "lifecycle_gate.py"


def git(repo: Path, *args: str) -> str:
    completed = subprocess.run(["git", *args], cwd=repo, text=True, capture_output=True, check=False)
    assert completed.returncode == 0, f"DEFECT [git fixture]: git {' '.join(args)} failed: {completed.stderr}"
    return completed.stdout.strip()


def commit(repo: Path, message: str) -> str:
    git(repo, "add", "-A")
    git(repo, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-m", message)
    return git(repo, "rev-parse", "HEAD")


def write(repo: Path, relative: str, text: str = "x\n") -> None:
    path = repo / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def checkout(repo: Path, branch: str, revision: str) -> None:
    git(repo, "checkout", "-B", branch, revision)


def history(tmp_path: Path) -> tuple[Path, dict[str, str]]:
    repo = tmp_path / "history"
    repo.mkdir()
    git(repo, "init")
    write(repo, "manuscripts/gauge_vfe_rg/main.tex")
    revisions = {"S": commit(repo, "source")}
    checkout(repo, "evidence", revisions["S"])
    write(repo, "manuscripts/gauge_vfe_rg/verification/current-results.json", "{}\n")
    write(repo, "docs/derivations/evidence/numerics.json", "{}\n")
    revisions["E"] = commit(repo, "evidence")
    checkout(repo, "closure", revisions["E"])
    write(repo, "docs/derivations/closure-attestation.json", "{}\n")
    write(repo, "docs/derivations/release.json", "{}\n")
    revisions["C"] = commit(repo, "closure")
    checkout(repo, "wiki", revisions["C"])
    write(repo, "sources/manuscripts/gauge-vfe-rg-cross-scale-operator-theory-2026-08-03.md")
    write(repo, "wiki/concepts/Coarse Graining.md")
    write(repo, "index.md")
    write(repo, "log.md")
    revisions["W"] = commit(repo, "wiki")
    return repo, revisions


def gate_module():
    if not GATE_PATH.is_file():
        pytest.fail("DEFECT [lifecycle module]: missing planned lifecycle_gate.py")
    spec = importlib.util.spec_from_file_location("lifecycle_gate_contract", GATE_PATH)
    assert spec and spec.loader, "DEFECT [lifecycle module]: lifecycle_gate.py must be importable"
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def require_gate(name: str, defect: str):
    value = getattr(gate_module(), name, None)
    assert callable(value), f"DEFECT [{defect}]: lifecycle_gate.py must export {name}"
    return value


def test_gate_accepts_monotone_real_allowed_s_e_c_w_history_and_authorized_source_note(tmp_path: Path):
    repo, revisions = history(tmp_path)
    outcome = require_gate("validate_lifecycle", "real S/E/C/W gate")(repo, revisions["S"], revisions["E"], revisions["C"], revisions["W"])
    assert getattr(outcome, "ok", None) is True, "DEFECT [real S/E/C/W gate]: allowed monotone history was rejected"


@pytest.mark.parametrize("boundary, forbidden", [("S..E", "manuscripts/gauge_vfe_rg/main.tex"), ("S..E", "manuscripts/references.bib"), ("E..C", "docs/reviews/adversarial.md"), ("C..W", "docs/derivations/release.json")])
def test_gate_rejects_forbidden_change_on_the_exact_monotone_boundary(tmp_path: Path, boundary: str, forbidden: str):
    repo, valid = history(tmp_path)
    revised = dict(valid)
    if boundary == "S..E":
        checkout(repo, "bad-evidence", valid["S"])
        write(repo, forbidden, "forbidden\n")
        revised["E"] = commit(repo, "forbidden evidence")
        checkout(repo, "bad-closure", revised["E"])
        write(repo, "docs/derivations/closure-attestation.json", "still monotone\n")
        revised["C"] = commit(repo, "closure after bad evidence")
        checkout(repo, "bad-wiki", revised["C"])
        write(repo, "index.md", "wiki after bad evidence\n")
        revised["W"] = commit(repo, "wiki after bad evidence")
    elif boundary == "E..C":
        checkout(repo, "bad-closure", valid["E"])
        write(repo, forbidden, "forbidden\n")
        revised["C"] = commit(repo, "forbidden closure")
        checkout(repo, "bad-wiki", revised["C"])
        write(repo, "index.md", "wiki after bad closure\n")
        revised["W"] = commit(repo, "wiki after bad closure")
    else:
        checkout(repo, "bad-wiki", valid["C"])
        write(repo, forbidden, "forbidden\n")
        revised["W"] = commit(repo, "forbidden wiki")
    outcome = require_gate("validate_lifecycle", f"forbidden {boundary} {forbidden}")(repo, revised["S"], revised["E"], revised["C"], revised["W"])
    assert getattr(outcome, "ok", None) is False, f"DEFECT [forbidden {boundary}]: gate accepted {forbidden}"


def test_gate_parses_real_nul_delimited_add_modify_delete_rename_copy_and_space_paths(tmp_path: Path):
    repo, revisions = history(tmp_path)
    checkout(repo, "status-fixture", revisions["W"])
    write(repo, "sources/manuscripts/copy source.md", "same bytes\n")
    write(repo, "sources/manuscripts/delete me.md", "delete\n")
    start = commit(repo, "add sources")
    write(repo, "sources/manuscripts/copy source.md", "modified bytes\n")
    write(repo, "sources/manuscripts/copy destination.md", "same bytes\n")
    (repo / "sources/manuscripts/delete me.md").unlink()
    write(repo, "sources/manuscripts/sp ace-✓.md", "added\n")
    middle = commit(repo, "modify delete copy")
    git(repo, "mv", "sources/manuscripts/copy source.md", "sources/manuscripts/renamed source.md")
    end = commit(repo, "rename")
    raw = subprocess.run(["git", "diff", "--name-status", "-z", "-C", "--find-copies-harder", start, end], cwd=repo, capture_output=True, check=True).stdout
    assert b"\x00" in raw and "sp ace-✓.md".encode() in raw, "DEFECT [NUL fixture]: real NUL-delimited status record is missing"
    entries = require_gate("parse_name_status_z", "NUL-safe diff parser")(raw)
    assert {entry.status[0] for entry in entries} >= {"A", "M", "D", "R", "C"}, "DEFECT [NUL-safe parser]: real add/modify/delete/rename/copy statuses were not preserved"
    assert any("sp ace-✓.md" in " ".join(entry.paths) for entry in entries), "DEFECT [NUL-safe parser]: spaced path lost its byte identity"
    assert middle != end, "DEFECT [NUL fixture]: fixture history is not monotone"


def test_gate_rejects_invalid_revision_and_publication_byte_drift(tmp_path: Path):
    repo, revisions = history(tmp_path)
    invalid = require_gate("validate_lifecycle", "invalid revision")(repo, "0" * 40, revisions["E"], revisions["C"], revisions["W"])
    assert getattr(invalid, "ok", None) is False, "DEFECT [invalid revision]: gate accepted nonexistent revision"
    checkout(repo, "publication-drift", revisions["W"])
    write(repo, "manuscripts/gauge_vfe_rg/main.tex", "changed after W\n")
    publication = commit(repo, "publication drift")
    identity = require_gate("verify_publication_identity", "publication byte identity")(repo, revisions["W"], publication)
    assert getattr(identity, "ok", None) is False, "DEFECT [publication identity]: gate accepted altered bound bytes"
