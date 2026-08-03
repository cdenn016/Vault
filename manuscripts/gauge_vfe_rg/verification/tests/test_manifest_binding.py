"""Real temporary-tree mutation contract for fail-closed manifest binding."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest


RUNNER_PATH = Path(__file__).resolve().parents[1] / "run_checks.py"
BOUND_FILES = (
    "manuscripts/gauge_vfe_rg/main.tex", "manuscripts/gauge_vfe_rg/chapters/child.tex", "manuscripts/gauge_vfe_rg/SPEC.md", "manuscripts/references.bib", "manuscripts/gauge_vfe_rg/scientific_report.sty", "manuscripts/gauge_vfe_rg/build.ps1", "manuscripts/gauge_vfe_rg/verification/claims.json", "manuscripts/gauge_vfe_rg/verification/run_checks.py", "manuscripts/gauge_vfe_rg/verification/requirements.txt", "manuscripts/gauge_vfe_rg/verification/VERIFICATION.md", "manuscripts/gauge_vfe_rg/verification/result.schema.json", "manuscripts/gauge_vfe_rg/verification/manifest-policy.json", "manuscripts/gauge_vfe_rg/verification/lifecycle_gate.py", "manuscripts/gauge_vfe_rg/verification/build_audit.py", "manuscripts/gauge_vfe_rg/verification/tests/test_factorization_gap.py", "manuscripts/gauge_vfe_rg/verification/tests/test_runner_cli.py", "manuscripts/gauge_vfe_rg/verification/tests/test_manifest_binding.py", "manuscripts/gauge_vfe_rg/verification/tests/test_lifecycle_gate.py", "manuscripts/gauge_vfe_rg/verification/tests/test_build_audit.py",
)


class MissingAPI:
    def __init__(self, name: str):
        self.name = name

    def __call__(self, *_args, **_kwargs):
        return MissingResult(self.name)


class MissingResult:
    def __init__(self, name: str):
        self.name = name


def module():
    spec = importlib.util.spec_from_file_location("manifest_contract_runner", RUNNER_PATH)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def api(name: str, defect: str):
    value = getattr(module(), name, None)
    return value if callable(value) else MissingAPI(name)


def tree(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    for relative in BOUND_FILES:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("{}\n" if path.suffix == ".json" else f"bound:{relative}\n", encoding="utf-8")
    return root


def golden(root: Path, result: Path):
    document = api("build_result", "golden bound result")(root, "a" * 40)
    if not isinstance(document, dict):
        document = {"source_revision": "a" * 40, "semantic_payload_digest": "b" * 64, "checks": [], "bound_inputs": {}}
    encoded = api("canonical_json_bytes", "golden canonical bytes")(document)
    if not isinstance(encoded, bytes):
        encoded = json.dumps(document, sort_keys=True, separators=(",", ":")).encode("utf-8")
    result.write_bytes(encoded)
    return document


def assert_rejected(result: Path, root: Path, defect: str):
    report = api("verify_result", defect)(result, root)
    assert getattr(report, "ok", None) is False, f"DEFECT [{defect}]: verifier accepted mutation"


def test_discovery_recursively_finds_every_governed_class_and_no_constant_allowlist(tmp_path: Path):
    root = tree(tmp_path)
    found = api("discover_bound_inputs", "recursive governed discovery")(root)
    assert isinstance(found, dict), "DEFECT [recursive governed discovery]: missing public discovery interface"
    paths = set(found)
    assert set(BOUND_FILES) <= paths, "DEFECT [recursive governed discovery]: missing governed inputs"
    assert "manuscripts/gauge_vfe_rg/chapters/child.tex" in paths, "DEFECT [recursive governed discovery]: recursive TeX omitted"


@pytest.mark.parametrize("relative", BOUND_FILES)
def test_each_real_bound_file_byte_mutation_is_rejected(tmp_path: Path, relative: str):
    root, result = tree(tmp_path), tmp_path / "result.json"
    golden(root, result)
    path = root / relative
    path.write_bytes(path.read_bytes() + b"changed\n")
    assert_rejected(result, root, f"byte mutation {relative}")


@pytest.mark.parametrize("kind", ["malformed", "missing_bound_file", "extra_bound_file", "missing_result_field", "extra_result_field", "newline", "semantic", "unknown_check", "duplicate_check", "revision", "nan", "infinity"])
def test_real_tree_and_result_mutations_fail_closed(tmp_path: Path, kind: str):
    root, result = tree(tmp_path), tmp_path / "result.json"
    document = golden(root, result)
    if kind == "malformed":
        (root / "manuscripts/gauge_vfe_rg/verification/claims.json").write_text("{", encoding="utf-8")
    elif kind == "missing_bound_file":
        (root / BOUND_FILES[0]).unlink()
    elif kind == "extra_bound_file":
        extra = root / "manuscripts/gauge_vfe_rg/chapters/unexpected.tex"
        extra.parent.mkdir(parents=True, exist_ok=True)
        extra.write_text("unexpected\n", encoding="utf-8")
    elif kind == "missing_result_field":
        required = next((field for field in ("source_revision", "semantic_payload_digest", "checks") if field in document), None)
        assert required is not None, "DEFECT [missing result field fixture]: build_result must emit a required result field"
        document.pop(required)
        result.write_text(json.dumps(document) + "\n", encoding="utf-8")
    elif kind == "extra_result_field":
        document["unrecognized_result_field"] = {"must": "fail closed"}
        result.write_text(json.dumps(document) + "\n", encoding="utf-8")
    elif kind == "newline":
        path = root / BOUND_FILES[0]
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
    elif kind == "semantic":
        document["semantic_payload_digest"] = "0" * 64
        result.write_text(json.dumps(document) + "\n", encoding="utf-8")
    elif kind in {"unknown_check", "duplicate_check"}:
        document["checks"] = [{"check_id": "UNKNOWN"}] if kind == "unknown_check" else [{"check_id": "DUP"}, {"check_id": "DUP"}]
        result.write_text(json.dumps(document) + "\n", encoding="utf-8")
    elif kind == "revision":
        document["source_revision"] = "0" * 40
        result.write_text(json.dumps(document) + "\n", encoding="utf-8")
    else:
        result.write_text('{"value": ' + ("NaN" if kind == "nan" else "Infinity") + "}\n", encoding="utf-8")
    assert_rejected(result, root, f"real {kind} mutation")
