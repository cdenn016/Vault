"""Black-box specification for explicit update and nonmutating verify modes."""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "verification" / "run_checks.py"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def invoke(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(RUNNER), *args],
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
    )


def test_cli_rejects_implicit_mode(tmp_path: Path):
    result = invoke("--root", str(ROOT), cwd=tmp_path)
    assert result.returncode != 0
    assert "exactly one of --update or --verify" in result.stderr


def test_cli_rejects_conflicting_update_and_verify_modes(tmp_path: Path):
    result = invoke("--root", str(ROOT), "--update", "--verify", cwd=tmp_path)
    assert result.returncode != 0
    assert "exactly one of --update or --verify" in result.stderr


@pytest.mark.parametrize("mutation", ["line-ending", "semantic", "revision", "nan", "infinity"])
def test_verify_mode_fails_closed_without_rewriting_bound_result(tmp_path: Path, mutation: str):
    result_path = tmp_path / "result.json"
    result_path.write_text('{"mutation": "' + mutation + '"}\n', encoding="utf-8")
    before = digest(result_path)
    completed = invoke(
        "--root", str(ROOT), "--verify", "--result", str(result_path), "--report", str(tmp_path / "report.json"), cwd=tmp_path
    )
    assert completed.returncode != 0
    assert digest(result_path) == before
    assert (tmp_path / "report.json").is_file()


def test_update_writes_result_atomically_and_verify_writes_only_separate_report(tmp_path: Path):
    result_path = tmp_path / "result.json"
    report_path = tmp_path / "verify-report.json"
    update = invoke("--root", str(ROOT), "--update", "--result", str(result_path), cwd=tmp_path)
    assert update.returncode == 0
    assert result_path.is_file()
    assert not list(tmp_path.glob("*.tmp"))
    before = digest(result_path)
    verify = invoke("--root", str(ROOT), "--verify", "--result", str(result_path), "--report", str(report_path), cwd=tmp_path)
    assert verify.returncode == 0
    assert digest(result_path) == before
    assert report_path.is_file()
