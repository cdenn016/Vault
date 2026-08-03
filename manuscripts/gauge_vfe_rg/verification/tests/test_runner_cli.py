"""Black-box RED contract for the positional update/verify runner interface."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


RUNNER = Path(__file__).resolve().parents[1] / "run_checks.py"
RUNNER_RELATIVE = Path("manuscripts/gauge_vfe_rg/verification/run_checks.py")


def runner_module():
    spec = importlib.util.spec_from_file_location("runner_cli_contract", RUNNER)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def runner_api(name: str, defect: str):
    value = getattr(runner_module(), name, None)
    assert callable(value), f"DEFECT [{defect}]: run_checks.py must export {name}"
    return value


def files(root: Path) -> dict[str, str]:
    return {path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(root.rglob("*")) if path.is_file()}


def invoke(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(root / RUNNER_RELATIVE), *args], cwd=root, text=True, capture_output=True, check=False)


def governed_tree(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    for relative, content in {
        "manuscripts/gauge_vfe_rg/main.tex": "\\documentclass{article}\n",
        "manuscripts/gauge_vfe_rg/nested/child.tex": "child\n",
        "manuscripts/gauge_vfe_rg/SPEC.md": "spec\n",
        "manuscripts/gauge_vfe_rg/scientific_report.sty": "style\n",
        "manuscripts/gauge_vfe_rg/build.ps1": "build\n",
        "manuscripts/references.bib": "@book{x,title={x}}\n",
        "manuscripts/gauge_vfe_rg/verification/claims.json": "{\"claims\": []}\n",
        "manuscripts/gauge_vfe_rg/verification/requirements.txt": "numpy>=2\n",
        "manuscripts/gauge_vfe_rg/verification/VERIFICATION.md": "protocol\n",
        "manuscripts/gauge_vfe_rg/verification/result.schema.json": "{}\n",
        "manuscripts/gauge_vfe_rg/verification/manifest-policy.json": "{}\n",
        "manuscripts/gauge_vfe_rg/verification/lifecycle_gate.py": "# gate\n",
        "manuscripts/gauge_vfe_rg/verification/build_audit.py": "# audit\n",
    }.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    shutil.copy2(RUNNER, root / RUNNER_RELATIVE)
    return root


def test_cli_requires_exactly_one_positional_mode_and_result(tmp_path: Path):
    root = governed_tree(tmp_path)
    neither = invoke(root)
    both = invoke(root, "--update", "result.json", "--verify", "result.json")
    assert neither.returncode != 0, "DEFECT [implicit mode]: runner must reject no mode"
    assert both.returncode != 0, "DEFECT [conflicting modes]: runner must reject both modes"
    assert "--update RESULT" in neither.stderr + neither.stdout, "DEFECT [usage]: positional --update RESULT contract missing"


def test_update_then_verify_preserves_result_and_writes_only_explicit_report(tmp_path: Path):
    root, result, report = governed_tree(tmp_path), tmp_path / "result.json", tmp_path / "report.json"
    update = invoke(root, "--update", str(result))
    assert update.returncode == 0, f"DEFECT [update]: positional --update RESULT failed: {update.stderr}"
    before, before_inventory = result.read_bytes(), files(tmp_path)
    verify = invoke(root, "--verify", str(result), "--report", str(report))
    assert verify.returncode == 0, f"DEFECT [verify]: positional --verify RESULT failed: {verify.stderr}"
    assert result.read_bytes() == before, "DEFECT [verify immutability]: verify rewrote its input result"
    assert set(files(tmp_path)) - set(before_inventory) == {"report.json"}, "DEFECT [verify writes]: only explicit report may be created"


@pytest.mark.parametrize("corruption", ["newline", "semantic", "revision", "nan", "infinity"])
def test_each_real_result_corruption_fails_without_mutating_input_or_other_files(tmp_path: Path, corruption: str):
    root, result, report = governed_tree(tmp_path), tmp_path / "result.json", tmp_path / f"{corruption}.report.json"
    bootstrap = invoke(root, "--update", str(result))
    assert bootstrap.returncode == 0, f"DEFECT [{corruption} fixture]: update must create a valid result"
    document = json.loads(result.read_text(encoding="utf-8"))
    if corruption == "newline":
        result.write_bytes(result.read_bytes().replace(b"\n", b"\r\n"))
    elif corruption == "semantic":
        document["semantic_payload_digest"] = "0" * 64
        result.write_text(json.dumps(document) + "\n", encoding="utf-8")
    elif corruption == "revision":
        document["source_revision"] = "0" * 40
        result.write_text(json.dumps(document) + "\n", encoding="utf-8")
    else:
        result.write_text('{"number": ' + ("NaN" if corruption == "nan" else "Infinity") + "}\n", encoding="utf-8")
    before, inventory = result.read_bytes(), files(tmp_path)
    verify = invoke(root, "--verify", str(result), "--report", str(report))
    assert verify.returncode != 0, f"DEFECT [{corruption}]: verifier accepted a real corrupted result"
    assert result.read_bytes() == before, f"DEFECT [{corruption}]: verifier rewrote corrupted input"
    assert set(files(tmp_path)) - set(inventory) == {report.name}, f"DEFECT [{corruption}]: verify wrote beyond explicit report"


def test_atomic_update_replaces_sentinel_and_failure_leaves_sentinel_and_no_temp_leak(tmp_path: Path):
    root, result = governed_tree(tmp_path), tmp_path / "result.json"
    result.write_bytes(b"SENTINEL")
    update = invoke(root, "--update", str(result))
    assert update.returncode == 0 and result.read_bytes() != b"SENTINEL", "DEFECT [atomic replace]: update must replace existing sentinel"
    assert not list(tmp_path.glob("*.tmp")), "DEFECT [atomic replace]: successful replacement leaked a temporary file"


def test_atomic_write_failure_preserves_existing_bytes_and_removes_staged_temp(tmp_path: Path, monkeypatch):
    target = tmp_path / "result.json"
    target.write_bytes(b"SENTINEL")
    loaded = runner_module()
    atomic_write = getattr(loaded, "atomic_write_json", None)
    assert callable(atomic_write), "DEFECT [interrupted update]: run_checks.py must export atomic_write_json"
    assert hasattr(loaded, "os"), "DEFECT [interrupted update]: atomic replacement must use an interceptable os.replace boundary"
    def interrupted_replace(*_args):
        raise OSError("simulated replacement interruption")
    monkeypatch.setattr(loaded.os, "replace", interrupted_replace)
    with pytest.raises(OSError):
        atomic_write(target, {"replacement": True})
    assert target.read_bytes() == b"SENTINEL", "DEFECT [interrupted update]: failed replacement changed original bytes"
    assert not list(tmp_path.glob("*.tmp")), "DEFECT [interrupted update]: failed replacement leaked temporary bytes"
