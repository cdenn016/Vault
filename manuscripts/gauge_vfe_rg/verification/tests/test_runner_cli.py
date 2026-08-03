"""Black-box RED contract for the positional update/verify runner interface."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import threading
from pathlib import Path

import pytest


RUNNER = Path(__file__).resolve().parents[1] / "run_checks.py"
RUNNER_RELATIVE = Path("manuscripts/gauge_vfe_rg/verification/run_checks.py")


class MissingAtomicWrite:
    def __call__(self, *_args, **_kwargs):
        return None


def runner_module():
    spec = importlib.util.spec_from_file_location("runner_cli_contract", RUNNER)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def runner_api(name: str, defect: str):
    value = getattr(runner_module(), name, None)
    return value if callable(value) else MissingAtomicWrite()


def files(root: Path) -> dict[str, str]:
    return {path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(root.rglob("*")) if path.is_file()}


def assert_only_report_added(before: dict[str, str], after: dict[str, str], report: Path, defect: str) -> None:
    expected = dict(before)
    expected[report.name] = after.get(report.name, "")
    assert report.name in after, f"DEFECT [{defect}]: explicit report was not written"
    assert after == expected, f"DEFECT [{defect}]: verify changed existing bytes or wrote outside its explicit report"


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
    assert_only_report_added(before_inventory, files(tmp_path), report, "verify writes")


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
    assert_only_report_added(inventory, files(tmp_path), report, f"{corruption} immutability")


def test_atomic_update_replaces_sentinel_and_failure_leaves_sentinel_and_no_temp_leak(tmp_path: Path):
    root, result = governed_tree(tmp_path), tmp_path / "result.json"
    result.write_bytes(b"SENTINEL")
    update = invoke(root, "--update", str(result))
    assert update.returncode == 0 and result.read_bytes() != b"SENTINEL", "DEFECT [atomic replace]: update must replace existing sentinel"
    assert not list(tmp_path.glob("*.tmp")), "DEFECT [atomic replace]: successful replacement leaked a temporary file"


def test_public_atomic_write_is_all_or_nothing_under_success_serialization_failure_and_reader_race(tmp_path: Path):
    target = tmp_path / "result.json"
    target.write_text(json.dumps({"state": "old"}), encoding="utf-8")
    atomic_write = runner_api("atomic_write_json", "public atomic write")
    assert not isinstance(atomic_write, MissingAtomicWrite), "DEFECT [public atomic write]: run_checks.py must export atomic_write_json"
    old_bytes = target.read_bytes()
    old_hash = hashlib.sha256(old_bytes).hexdigest()
    observed_errors: list[str] = []
    observed_hashes: list[str] = []
    overlap_reads = [0]
    old_read, writer_alive, stop = threading.Event(), threading.Event(), threading.Event()

    def reader() -> None:
        while not stop.is_set():
            try:
                raw = target.read_bytes()
                json.loads(raw.decode("utf-8"))
                observed_hashes.append(hashlib.sha256(raw).hexdigest())
                old_read.set()
                if writer_alive.is_set():
                    overlap_reads[0] += 1
            except (OSError, json.JSONDecodeError) as exc:
                observed_errors.append(type(exc).__name__)

    thread = threading.Thread(target=reader, daemon=True)
    thread.start()
    assert old_read.wait(timeout=2), "DEFECT [public atomic write]: reader never completed an old-file read before writer start"
    new_document = {"state": "new", "payload": "x" * 20_000_000}
    new_bytes = json.dumps(new_document, sort_keys=True, separators=(",", ":")).encode("utf-8")
    new_hash = hashlib.sha256(new_bytes).hexdigest()

    def writer() -> None:
        writer_alive.set()
        try:
            atomic_write(target, new_document)
        finally:
            writer_alive.clear()

    writer_thread = threading.Thread(target=writer, daemon=True)
    writer_thread.start()
    writer_thread.join(timeout=10)
    assert not writer_thread.is_alive(), "DEFECT [public atomic write]: writer did not complete"
    stop.set()
    thread.join(timeout=2)
    assert not thread.is_alive(), "DEFECT [public atomic write]: reader thread did not terminate"
    assert old_hash in observed_hashes, "DEFECT [public atomic write]: reader did not observe the old complete document"
    assert overlap_reads[0] > 0, "DEFECT [public atomic write]: reader completed no read while writer was alive"
    assert set(observed_hashes) <= {old_hash, new_hash}, "DEFECT [public atomic write]: reader observed bytes other than complete old/new JSON"
    assert hashlib.sha256(target.read_bytes()).hexdigest() == new_hash, "DEFECT [public atomic write]: successful write did not replace the exact new document"
    assert not observed_errors, f"DEFECT [public atomic write]: reader observed partial JSON: {observed_errors}"
    before_failure = target.read_bytes()
    with pytest.raises((TypeError, ValueError)):
        atomic_write(target, {"unserializable": object()})
    assert target.read_bytes() == before_failure, "DEFECT [serialization failure]: failed public write changed existing bytes"
    assert list(tmp_path.iterdir()) == [target], "DEFECT [serialization failure]: failed public write leaked temporary files"
