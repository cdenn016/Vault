"""Real, monotone Git-history RED contract for S/E/C/W lifecycle gates."""

from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path

import pytest


GATE_PATH = Path(__file__).resolve().parents[1] / "lifecycle_gate.py"

E_TO_C_PATHS = (
    "docs/derivations/closure-attestation.json",
    "docs/derivations/release.json",
)


class MissingGate:
    def __init__(self, name: str):
        self.name = name

    def __call__(self, *_args, **_kwargs):
        return [] if self.name == "parse_name_status_z" else self


def git(repo: Path, *args: str) -> str:
    completed = subprocess.run(["git", *args], cwd=repo, text=True, capture_output=True, check=False)
    assert completed.returncode == 0, f"DEFECT [git fixture]: git {' '.join(args)} failed: {completed.stderr}"
    return completed.stdout.strip()


def commit(repo: Path, message: str) -> str:
    git(repo, "add", "-A")
    git(repo, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-m", message)
    return git(repo, "rev-parse", "HEAD")


def empty_commit(repo: Path, message: str) -> str:
    git(
        repo,
        "-c",
        "user.name=Fixture",
        "-c",
        "user.email=fixture@example.invalid",
        "commit",
        "--allow-empty",
        "-m",
        message,
    )
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
    for path in E_TO_C_PATHS:
        write(repo, path, "{}\n")
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
        return None
    spec = importlib.util.spec_from_file_location("lifecycle_gate_contract", GATE_PATH)
    assert spec and spec.loader, "DEFECT [lifecycle module]: lifecycle_gate.py must be importable"
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def require_gate(name: str, defect: str):
    loaded = gate_module()
    value = getattr(loaded, name, None) if loaded is not None else None
    return value if callable(value) else MissingGate(name)


def test_gate_accepts_monotone_real_allowed_s_e_c_w_history_and_authorized_source_note(tmp_path: Path):
    repo, revisions = history(tmp_path)
    outcome = require_gate("validate_lifecycle", "real S/E/C/W gate")(repo, revisions["S"], revisions["E"], revisions["C"], revisions["W"])
    assert getattr(outcome, "ok", None) is True, "DEFECT [real S/E/C/W gate]: allowed monotone history was rejected"


@pytest.mark.parametrize(
    "boundary, forbidden",
    [
        ("S..E", "manuscripts/gauge_vfe_rg/main.tex"),
        ("S..E", "manuscripts/references.bib"),
        ("E..C", "docs/reviews/adversarial.md"),
        ("E..C", "docs/derivations/closure.json"),
        ("C..W", "docs/derivations/release.json"),
    ],
)
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


def test_gate_parses_exact_nul_statuses_and_utf8_paths_without_lossy_decoding():
    raw = (
        b"A\x00sources/manuscripts/sp ace-\xe2\x9c\x93.md\x00"
        b"M\x00manuscripts/gauge_vfe_rg/line\nbreak.tex\x00"
        b"D\x00docs/old\tname.md\x00"
        b"R100\x00wiki/concepts/Old Name.md\x00wiki/concepts/New Name.md\x00"
        b"C75\x00docs/source.json\x00docs/copied.json\x00"
    )
    entries = require_gate("parse_name_status_z", "NUL-safe diff parser")(raw)
    observed = tuple((entry.status, entry.paths) for entry in entries)
    assert observed == (
        ("A", ("sources/manuscripts/sp ace-\u2713.md",)),
        ("M", ("manuscripts/gauge_vfe_rg/line\nbreak.tex",)),
        ("D", ("docs/old\tname.md",)),
        ("R100", ("wiki/concepts/Old Name.md", "wiki/concepts/New Name.md")),
        ("C75", ("docs/source.json", "docs/copied.json")),
    ), "DEFECT [NUL-safe parser]: status/path tuples changed or UTF-8 was decoded lossily"


@pytest.mark.parametrize("kind", ["divergent", "nonmonotone"])
def test_gate_rejects_individually_valid_but_nonancestral_revision_tuples(tmp_path: Path, kind: str):
    repo, revisions = history(tmp_path)
    if kind == "divergent":
        checkout(repo, "parallel-evidence", revisions["E"])
        divergent_e = empty_commit(repo, "parallel evidence with identical tree")
        candidate = (revisions["S"], divergent_e, revisions["C"], revisions["W"])
    else:
        checkout(repo, "later-closure", revisions["C"])
        later_c = empty_commit(repo, "later closure with identical tree")
        candidate = (revisions["S"], revisions["E"], later_c, revisions["C"])
    outcome = require_gate("validate_lifecycle", f"{kind} ancestry")(repo, *candidate)
    assert getattr(outcome, "ok", None) is False, f"DEFECT [{kind} ancestry]: gate accepted a revision tuple that is not S -> E -> C -> W"


def test_gate_rejects_invalid_revision(tmp_path: Path):
    repo, revisions = history(tmp_path)
    invalid = require_gate("validate_lifecycle", "invalid revision")(repo, "0" * 40, revisions["E"], revisions["C"], revisions["W"])
    assert getattr(invalid, "ok", None) is False, "DEFECT [invalid revision]: gate accepted nonexistent revision"


def test_publication_identity_accepts_unrelated_integration_change(tmp_path: Path):
    repo, revisions = history(tmp_path)
    checkout(repo, "publication-integration", revisions["W"])
    write(repo, "docs/unrelated/remote-note.md", "unrelated integration\n")
    publication = commit(repo, "unrelated integration")
    identity = require_gate("verify_publication_identity", "positive publication byte identity")(repo, revisions["W"], publication)
    assert getattr(identity, "ok", None) is True, "DEFECT [publication identity]: unrelated integration was rejected despite preserving every protected byte"


@pytest.mark.parametrize(
    "protected_path",
    [
        "manuscripts/gauge_vfe_rg/main.tex",
        "manuscripts/gauge_vfe_rg/verification/current-results.json",
        "docs/derivations/closure-attestation.json",
        "docs/derivations/release.json",
    ],
)
def test_publication_identity_rejects_each_protected_byte_drift(tmp_path: Path, protected_path: str):
    repo, revisions = history(tmp_path)
    checkout(repo, "publication-drift", revisions["W"])
    write(repo, protected_path, "changed after W\n")
    publication = commit(repo, "publication drift")
    identity = require_gate("verify_publication_identity", "publication byte identity")(repo, revisions["W"], publication)
    assert getattr(identity, "ok", None) is False, f"DEFECT [publication identity]: gate accepted drift in protected path {protected_path}"
