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
TEST_RESULT_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["schema_version", "generated_at_utc", "source_revision", "source_dirty", "overall_status", "environment", "manifest", "checks", "semantic_payload_digest"],
    "additionalProperties": False,
    "properties": {
        "schema_version": {"const": "3.0"},
        "generated_at_utc": {"type": "string"},
        "source_revision": {"type": "string", "pattern": "[0-9a-f]{40}"},
        "source_dirty": {"type": "boolean"},
        "overall_status": {"enum": ["PASS", "FAIL"]},
        "environment": {
            "type": "object",
            "required": ["python", "python_executable", "platform", "machine", "dependencies"],
            "additionalProperties": False,
            "properties": {
                "python": {"type": "string"}, "python_executable": {"type": "string"},
                "platform": {"type": "string"}, "machine": {"type": "string"},
                "dependencies": {"type": "object", "additionalProperties": {"type": "string"}},
            },
        },
        "manifest": {
            "type": "object",
            "required": ["hash_algorithm", "hash_domain", "path_semantics", "bound_inputs"],
            "additionalProperties": False,
            "properties": {
                "hash_algorithm": {"const": "SHA-256"},
                "hash_domain": {"const": "raw file bytes"},
                "path_semantics": {"const": "repository-relative POSIX paths"},
                "bound_inputs": {"type": "object"},
            },
        },
        "checks": {
            "type": "array", "minItems": 1,
            "items": {
                "type": "object",
                "required": ["check_id", "status", "evidence_kind", "observed"],
                "additionalProperties": False,
                "properties": {
                    "check_id": {"type": "string"},
                    "status": {"enum": ["PASS", "FAIL", "INCONCLUSIVE"]},
                    "evidence_kind": {"type": "string"},
                    "observed": {"type": "object"},
                },
            },
        },
        "semantic_payload_digest": {"type": "string", "pattern": "[0-9a-f]{64}"},
    },
}


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


def git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 0, f"git {' '.join(args)} failed: {completed.stderr}"
    return completed.stdout.strip()


def commit_all(root: Path, message: str) -> str:
    git(root, "add", "--all")
    git(
        root,
        "-c", "user.name=Runner Contract",
        "-c", "user.email=runner-contract@example.invalid",
        "commit", "--quiet", "-m", message,
    )
    return git(root, "rev-parse", "HEAD")


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def refresh_semantic_digest(document: dict) -> None:
    payload = {key: value for key, value in document.items() if key not in {"generated_at_utc", "semantic_payload_digest"}}
    document["semantic_payload_digest"] = hashlib.sha256(canonical_json_bytes(payload)).hexdigest()


def report_codes(path: Path) -> set[str]:
    document = json.loads(path.read_text(encoding="utf-8"))
    return {
        issue["code"]
        for issue in document.get("issues", [])
        if isinstance(issue, dict) and isinstance(issue.get("code"), str)
    }


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
        "manuscripts/scientific_report.sty": "parent style\n",
        "manuscripts/gauge_vfe_rg/build.ps1": "build\n",
        "manuscripts/references.bib": "@book{x,title={x}}\n",
        "manuscripts/gauge_vfe_rg/verification/claims.json": json.dumps({"schema_version": "1.0", "checks": [{"check_id": "CHK-FIXTURE-PASS"}]}, sort_keys=True) + "\n",
        "manuscripts/gauge_vfe_rg/verification/requirements.txt": "numpy>=2\n",
        "manuscripts/gauge_vfe_rg/verification/VERIFICATION.md": "protocol\n",
        "manuscripts/gauge_vfe_rg/verification/result.schema.json": json.dumps(TEST_RESULT_SCHEMA, sort_keys=True) + "\n",
        "manuscripts/gauge_vfe_rg/verification/lifecycle_gate.py": "# gate\n",
        "manuscripts/gauge_vfe_rg/verification/build_audit.py": "# audit\n",
    }.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    shutil.copy2(RUNNER, root / RUNNER_RELATIVE)
    fixture_tests = root / "manuscripts/gauge_vfe_rg/verification/tests"
    fixture_tests.mkdir(parents=True, exist_ok=True)
    for source in sorted((RUNNER.parent / "tests").glob("test_*.py")):
        shutil.copy2(source, fixture_tests / source.name)
    bound_paths = [
        path.relative_to(root).as_posix()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    ]
    policy_path = root / "manuscripts/gauge_vfe_rg/verification/manifest-policy.json"
    policy_path.write_text(
        json.dumps(
            {
                "schema_version": "1.0",
                "bound_paths": sorted([*bound_paths, policy_path.relative_to(root).as_posix()]),
                "reject_unexpected_governed_paths": True,
                "explicit_exclusions": ["manuscripts/gauge_vfe_rg/verification/current-results.json", "**/__pycache__/**"],
            },
            sort_keys=True,
        ) + "\n",
        encoding="utf-8",
    )
    git(root, "init", "--quiet")
    commit_all(root, "valid governed source fixture")
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


@pytest.mark.parametrize("corruption", ["trailing_whitespace", "semantic", "revision", "nan", "infinity"])
def test_each_real_result_corruption_fails_without_mutating_input_or_other_files(tmp_path: Path, corruption: str):
    root, result, report = governed_tree(tmp_path), tmp_path / "result.json", tmp_path / f"{corruption}.report.json"
    bootstrap = invoke(root, "--update", str(result))
    assert bootstrap.returncode == 0, f"DEFECT [{corruption} fixture]: update must create a valid result"
    document = json.loads(result.read_text(encoding="utf-8"))
    if corruption == "trailing_whitespace":
        old = result.read_bytes()
        corrupted = old + b"\n"
        assert corrupted != old and json.loads(corrupted.decode("utf-8")) == document
        result.write_bytes(corrupted)
    elif corruption == "semantic":
        document["semantic_payload_digest"] = "0" * 64
        result.write_bytes(canonical_json_bytes(document))
    elif corruption == "revision":
        document["source_revision"] = "0" * 40
        refresh_semantic_digest(document)
        result.write_bytes(canonical_json_bytes(document))
    else:
        document["checks"][0]["observed"]["number"] = float("nan" if corruption == "nan" else "inf")
        result.write_text(json.dumps(document, sort_keys=True, separators=(",", ":"), allow_nan=True), encoding="utf-8")
    before, inventory = result.read_bytes(), files(tmp_path)
    verify = invoke(root, "--verify", str(result), "--report", str(report))
    assert verify.returncode != 0, f"DEFECT [{corruption}]: verifier accepted a real corrupted result"
    assert result.read_bytes() == before, f"DEFECT [{corruption}]: verifier rewrote corrupted input"
    assert_only_report_added(inventory, files(tmp_path), report, f"{corruption} immutability")
    expected_code = {
        "trailing_whitespace": "NONCANONICAL_RESULT_BYTES",
        "semantic": "SEMANTIC_DIGEST_MISMATCH",
        "revision": "SOURCE_REVISION_NOT_FOUND",
        "nan": "NONFINITE_JSON",
        "infinity": "NONFINITE_JSON",
    }[corruption]
    assert expected_code in report_codes(report), f"DEFECT [{corruption} specificity]: expected {expected_code}, got {sorted(report_codes(report))}"


def test_atomic_update_replaces_sentinel_without_temp_leak(tmp_path: Path):
    root = governed_tree(tmp_path)
    success_result = tmp_path / "success.json"
    success_result.write_bytes(b"SUCCESS-SENTINEL")
    update = invoke(root, "--update", str(success_result))
    assert update.returncode == 0 and success_result.read_bytes() != b"SUCCESS-SENTINEL", "DEFECT [atomic replace]: update must replace existing sentinel"
    assert set(path.name for path in tmp_path.iterdir()) == {"repo", "success.json"}, "DEFECT [atomic replace]: successful update leaked a temporary artifact"


def test_failed_atomic_update_preserves_sentinel_and_leaks_only_explicit_report(tmp_path: Path):
    root = governed_tree(tmp_path)
    failed_result, report = tmp_path / "failed.json", tmp_path / "failed.report.json"
    failed_result.write_bytes(b"FAILURE-SENTINEL")
    claims = root / "manuscripts/gauge_vfe_rg/verification/claims.json"
    claims.write_bytes(claims.read_bytes() + b"\n")
    before_failure = files(tmp_path)
    failed = invoke(
        root,
        "--update", str(failed_result),
        "--source-revision", git(root, "rev-parse", "HEAD"),
        "--report", str(report),
    )
    assert failed.returncode != 0, "DEFECT [failed atomic update]: governed source drift must fail update"
    assert failed_result.read_bytes() == b"FAILURE-SENTINEL", "DEFECT [failed atomic update]: failure changed the sentinel target"
    assert_only_report_added(before_failure, files(tmp_path), report, "failed atomic update")
    assert "SOURCE_BLOB_MISMATCH" in report_codes(report), f"DEFECT [failed atomic update specificity]: got {sorted(report_codes(report))}"


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
