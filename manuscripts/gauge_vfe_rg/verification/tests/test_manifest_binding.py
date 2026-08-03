"""Real temporary-tree mutation contract for fail-closed manifest binding."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import re

import pytest


RUNNER_PATH = Path(__file__).resolve().parents[1] / "run_checks.py"
BOUND_FILES = (
    "manuscripts/gauge_vfe_rg/main.tex", "manuscripts/gauge_vfe_rg/chapters/child.tex", "manuscripts/gauge_vfe_rg/SPEC.md", "manuscripts/references.bib", "manuscripts/gauge_vfe_rg/scientific_report.sty", "manuscripts/gauge_vfe_rg/build.ps1", "manuscripts/gauge_vfe_rg/verification/claims.json", "manuscripts/gauge_vfe_rg/verification/run_checks.py", "manuscripts/gauge_vfe_rg/verification/requirements.txt", "manuscripts/gauge_vfe_rg/verification/VERIFICATION.md", "manuscripts/gauge_vfe_rg/verification/result.schema.json", "manuscripts/gauge_vfe_rg/verification/manifest-policy.json", "manuscripts/gauge_vfe_rg/verification/lifecycle_gate.py", "manuscripts/gauge_vfe_rg/verification/build_audit.py", "manuscripts/gauge_vfe_rg/verification/tests/test_factorization_gap.py", "manuscripts/gauge_vfe_rg/verification/tests/test_runner_cli.py", "manuscripts/gauge_vfe_rg/verification/tests/test_manifest_binding.py", "manuscripts/gauge_vfe_rg/verification/tests/test_lifecycle_gate.py", "manuscripts/gauge_vfe_rg/verification/tests/test_build_audit.py",
)
TEST_RESULT_SCHEMA = {
    "type": "object",
    "required": ["schema_version", "generated_at_utc", "source_revision", "source_dirty", "overall_status", "environment", "manifest", "checks", "semantic_payload_digest"],
    "additionalProperties": False,
    "properties": {
        "schema_version": {"const": "3.0"},
        "generated_at_utc": {"type": "string", "pattern": r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z"},
        "source_revision": {"type": "string", "pattern": r"[0-9a-f]{40}"},
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
                "bound_inputs": {
                    "type": "object",
                    "additionalProperties": {
                        "type": "object", "required": ["byte_count", "sha256"], "additionalProperties": False,
                        "properties": {"byte_count": {"type": "integer"}, "sha256": {"type": "string", "pattern": r"[0-9a-f]{64}"}},
                    },
                },
            },
        },
        "checks": {
            "type": "array", "minItems": 1,
            "items": {
                "type": "object", "required": ["check_id", "status", "evidence_kind", "observed"], "additionalProperties": False,
                "properties": {"check_id": {"type": "string"}, "status": {"enum": ["PASS", "FAIL", "INCONCLUSIVE"]}, "evidence_kind": {"type": "string"}, "observed": {"type": "object"}},
            },
        },
        "semantic_payload_digest": {"type": "string", "pattern": r"[0-9a-f]{64}"},
    },
}


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


def schema_errors(value, schema: dict, path: str = "$") -> list[str]:
    errors: list[str] = []
    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: not in declared enum")
    expected_type = schema.get("type")
    matches_type = {
        "object": isinstance(value, dict), "array": isinstance(value, list),
        "string": isinstance(value, str), "boolean": isinstance(value, bool),
        "integer": isinstance(value, int) and not isinstance(value, bool),
    }.get(expected_type, True)
    if not matches_type:
        return errors + [f"{path}: expected {expected_type}"]
    if isinstance(value, str) and "pattern" in schema and re.fullmatch(schema["pattern"], value) is None:
        errors.append(f"{path}: pattern mismatch")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: too few items")
        for index, item in enumerate(value):
            errors.extend(schema_errors(item, schema.get("items", {}), f"{path}[{index}]"))
    if isinstance(value, dict):
        required = set(schema.get("required", []))
        errors.extend(f"{path}: missing {name}" for name in sorted(required - set(value)))
        properties = schema.get("properties", {})
        additional = schema.get("additionalProperties", True)
        if additional is False:
            errors.extend(f"{path}: unexpected {name}" for name in sorted(set(value) - set(properties)))
        for name, item in value.items():
            child_schema = properties.get(name, additional if isinstance(additional, dict) else {})
            errors.extend(schema_errors(item, child_schema, f"{path}.{name}"))
    return errors


def canonical_fixture_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def seeded_json(relative: str) -> object:
    if relative.endswith("result.schema.json"):
        return TEST_RESULT_SCHEMA
    if relative.endswith("manifest-policy.json"):
        return {"schema_version": "1.0", "bound_paths": list(BOUND_FILES), "reject_unexpected_governed_paths": True}
    if relative.endswith("claims.json"):
        return {"schema_version": "1.0", "checks": [{"check_id": "CHK-FIXTURE-PASS"}]}
    return {}


def tree(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    for relative in BOUND_FILES:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(canonical_fixture_bytes(seeded_json(relative)) + b"\n" if path.suffix == ".json" else f"bound:{relative}\n".encode())
    return root


def independent_golden(root: Path, source_revision: str) -> dict:
    bound_inputs = {}
    for relative in BOUND_FILES:
        raw = (root / relative).read_bytes()
        bound_inputs[relative] = {"byte_count": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
    document = {
        "schema_version": "3.0",
        "generated_at_utc": "2026-08-03T00:00:00Z",
        "source_revision": source_revision,
        "source_dirty": False,
        "overall_status": "PASS",
        "environment": {"python": "fixture-python-3.14", "python_executable": "C:/fixture/python.exe", "platform": "fixture-windows", "machine": "AMD64", "dependencies": {"numpy": "2.4.4", "scipy": "1.17.1", "sympy": "1.14.0", "mpmath": "1.3.0", "jsonschema": "4.25.1"}},
        "manifest": {"hash_algorithm": "SHA-256", "hash_domain": "raw file bytes", "path_semantics": "repository-relative POSIX paths", "bound_inputs": bound_inputs},
        "checks": [{"check_id": "CHK-FIXTURE-PASS", "status": "PASS", "evidence_kind": "reproduced_output", "observed": {"fixture_complete": True}}],
        "semantic_payload_digest": "",
    }
    payload = {key: value for key, value in document.items() if key not in {"generated_at_utc", "semantic_payload_digest"}}
    document["semantic_payload_digest"] = hashlib.sha256(canonical_fixture_bytes(payload)).hexdigest()
    return document


def golden(root: Path, result: Path):
    document = api("build_result", "golden bound result")(root, "a" * 40)
    if not isinstance(document, dict):
        document = independent_golden(root, "a" * 40)
    errors = schema_errors(document, TEST_RESULT_SCHEMA)
    assert not errors, f"DEFECT [golden fixture shape]: complete baseline violates independent result schema: {errors}"
    assert set(document["manifest"]["bound_inputs"]) == set(BOUND_FILES), "DEFECT [golden fixture shape]: complete baseline must bind every governed path"
    encoded = api("canonical_json_bytes", "golden canonical bytes")(document)
    if not isinstance(encoded, bytes):
        encoded = canonical_fixture_bytes(document)
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
