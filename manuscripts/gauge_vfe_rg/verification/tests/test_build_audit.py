"""Real-artifact RED contract for machine-readable TeX build auditing."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
from pathlib import Path

import pytest


AUDIT_PATH = Path(__file__).resolve().parents[1] / "build_audit.py"
BUILD_SCRIPT_PATH = Path(__file__).resolve().parents[2] / "build.ps1"

PDF_METADATA = {
    "title": "Gauge VFE RG Build Audit Fixture",
    "author": "Robert C. Dennis",
    "subject": "Lifecycle build verification",
    "keywords": "gauge, VFE, RG",
    "creator": "pytest fixture",
    "producer": "hand-built PDF fixture",
    "creation_date": "D:20260803093000-05'00'",
    "modification_date": "D:20260803093000-05'00'",
}


class MissingAudit:
    def __init__(self, name: str):
        self.name = name

    def __call__(self, **_kwargs):
        return self


def audit_module():
    if not AUDIT_PATH.is_file():
        return None
    spec = importlib.util.spec_from_file_location("build_audit_contract", AUDIT_PATH)
    assert spec and spec.loader, "DEFECT [build audit module]: build_audit.py must be importable"
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def audit_api():
    loaded = audit_module()
    value = getattr(loaded, "audit_build", None) if loaded is not None else None
    return value if callable(value) else MissingAudit("audit_build")


def git(repo: Path, *args: str) -> str:
    completed = subprocess.run(["git", *args], cwd=repo, text=True, capture_output=True, check=False)
    assert completed.returncode == 0, f"DEFECT [git fixture]: git {' '.join(args)} failed: {completed.stderr}"
    return completed.stdout.strip()


def commit(repo: Path, message: str) -> str:
    git(repo, "add", "-A")
    git(repo, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-m", message)
    return git(repo, "rev-parse", "HEAD")


def two_page_pdf() -> bytes:
    first_stream = b"BT /F1 12 Tf 72 720 Td (audit page one) Tj ET"
    second_stream = b"BT /F1 12 Tf 72 720 Td (audit page two) Tj ET"
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R 4 0 R] /Count 2 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 7 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 7 0 R >> >> /Contents 6 0 R >>",
        f"<< /Length {len(first_stream)} >>\nstream\n".encode() + first_stream + b"\nendstream",
        f"<< /Length {len(second_stream)} >>\nstream\n".encode() + second_stream + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        (
            b"<< /Title (Gauge VFE RG Build Audit Fixture) /Author (Robert C. Dennis) "
            b"/Subject (Lifecycle build verification) /Keywords (gauge, VFE, RG) "
            b"/Creator (pytest fixture) /Producer (hand-built PDF fixture) "
            b"/CreationDate (D:20260803093000-05'00') /ModDate (D:20260803093000-05'00') >>"
        ),
    ]
    document = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for number, body in enumerate(objects, 1):
        offsets.append(len(document))
        document.extend(f"{number} 0 obj\n".encode() + body + b"\nendobj\n")
    xref = len(document)
    document.extend(f"xref\n0 {len(objects) + 1}\n".encode())
    document.extend(b"0000000000 65535 f \n")
    document.extend(b"".join(f"{offset:010d} 00000 n \n".encode() for offset in offsets[1:]))
    document.extend(f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R /Info 8 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    return bytes(document)


def validate_pdf_fixture(path: Path) -> None:
    # This intentionally does not trust the audit module: it checks the fixture's
    # PDF cross-reference, catalog, pages tree, and stream framing independently.
    raw = path.read_bytes()
    assert raw.startswith(b"%PDF-1.4\n") and b"xref\n0 9\n" in raw and raw.rstrip().endswith(b"%%EOF"), "DEFECT [PDF fixture]: missing PDF header/xref/trailer"
    assert b"/Type /Catalog /Pages 2 0 R" in raw and b"/Type /Pages /Kids [3 0 R 4 0 R] /Count 2" in raw, "DEFECT [PDF fixture]: invalid two-page catalog/pages tree"
    assert raw.count(b"/Type /Page /Parent 2 0 R") == 2 and raw.count(b"stream\nBT /F1 12 Tf") == 2, "DEFECT [PDF fixture]: page content streams are malformed"
    assert b"/Info 8 0 R" in raw and b"/Title (Gauge VFE RG Build Audit Fixture)" in raw and b"/Subject (Lifecycle build verification)" in raw, "DEFECT [PDF fixture]: real /Info metadata is missing"


def validate_tex_fixture(root: Path, build: Path) -> None:
    source = (root / "main.tex").read_text(encoding="utf-8")
    auxiliary = (build / "main.aux").read_text(encoding="utf-8")
    bibliography = (build / "main.bbl").read_text(encoding="utf-8")
    assert r"\n" not in source and source.count("\n") == 4, "DEFECT [TeX fixture]: source must use actual line breaks and contain no literal \\n command"
    assert r"\label{one}" in source and r"\newlabel{one}" in auxiliary, "DEFECT [TeX fixture]: source and auxiliary label records disagree"
    assert r"\cite{x}" in source and r"\bibitem{x}" in bibliography, "DEFECT [TeX fixture]: source and bibliography citation records disagree"


def artifacts(tmp_path: Path, log: str | None = None) -> tuple[Path, Path, dict[str, object]]:
    root, build = tmp_path / "repo", tmp_path / "build"
    root.mkdir()
    build.mkdir()
    (root / "main.tex").write_text("\\documentclass{article}\n\\begin{document}\n\\label{one}Audit~\\cite{x}.\n\\end{document}\n", encoding="utf-8")
    git(root, "init")
    source_revision = commit(root, "source")
    pdf_bytes = two_page_pdf()
    (build / "main.pdf").write_bytes(pdf_bytes)
    validate_pdf_fixture(build / "main.pdf")
    if log is None:
        log = f"This is pdfTeX\nOutput written on main.pdf (2 pages, {len(pdf_bytes)} bytes).\n"
    else:
        log = f"This is pdfTeX\n{log}Output written on main.pdf (2 pages, {len(pdf_bytes)} bytes).\n"
    (build / "main.log").write_text(log, encoding="utf-8")
    (build / "main.aux").write_text("\\relax \n\\newlabel{one}{{1}{1}}\n", encoding="utf-8")
    (build / "main.bbl").write_text("\\begin{thebibliography}{1}\n\\bibitem{x} X.\n\\end{thebibliography}\n", encoding="utf-8")
    (build / "main.toc").write_text("\\contentsline {section}{Audit}{1}{}%\n", encoding="utf-8")
    validate_tex_fixture(root, build)
    commands = [
        {"argv": ["pdflatex", "-interaction=nonstopmode", "main.tex"], "returncode": 0, "tool_version": "fixture-pdftex-1"},
        {"argv": ["bibtex", "main"], "returncode": 0, "tool_version": "fixture-bibtex-1"},
        {"argv": ["pdflatex", "-interaction=nonstopmode", "main.tex"], "returncode": 0, "tool_version": "fixture-pdftex-1"},
        {"argv": ["pdflatex", "-interaction=nonstopmode", "main.tex"], "returncode": 0, "tool_version": "fixture-pdftex-1"},
    ]
    (build / "commands.json").write_text(json.dumps(commands), encoding="utf-8")
    inventory = {"main.tex": hashlib.sha256((root / "main.tex").read_bytes()).hexdigest()}
    expected = {
        "commands": commands,
        "tool_versions": {"pdflatex": "fixture-pdftex-1", "bibtex": "fixture-bibtex-1"},
        "input_inventory": inventory,
        "source_manifest_digest": hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
        "pdf_sha256": hashlib.sha256(pdf_bytes).hexdigest(),
        "pdf_byte_count": len(pdf_bytes),
        "page_count": 2,
        "pdf_metadata": PDF_METADATA,
        "source_revision": source_revision,
        "artifact_hashes": {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(build.iterdir()) if path.is_file()},
    }
    return root, build, expected


def run_audit(root: Path, build: Path, defect: str):
    return audit_api()(repo_root=root, build_dir=build, source_revision=git(root, "rev-parse", "HEAD"), command_record=build / "commands.json")


def require_field(value, name: str, defect: str):
    assert hasattr(value, name), f"DEFECT [{defect}]: missing {name}"
    return getattr(value, name)


def diagnostic_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str).lower()


def test_clean_parseable_artifacts_emit_verified_metadata_not_fabricated_defaults(tmp_path: Path):
    root, build, expected = artifacts(tmp_path)
    outcome = run_audit(root, build, "clean artifact audit")
    diagnostics = (
        "errors",
        "duplicate_labels",
        "undefined_references",
        "undefined_citations",
        "rerun_requests",
        "fatal_errors",
        "overfull_boxes",
        "literal_double_question_marks",
        "invalid_status_tags",
        "doubled_status_tags",
        "stale_auxiliary_files",
    )
    required = (
        "ok",
        "source_revision",
        "tool_versions",
        "commands",
        "input_inventory",
        "source_manifest_digest",
        "pdf_sha256",
        "pdf_byte_count",
        "page_count",
        "pdf_metadata",
        "artifact_hashes",
        "changed_pages",
        *diagnostics,
    )
    for field in required:
        require_field(outcome, field, "clean artifact audit")
    assert require_field(outcome, "ok", "clean artifact audit") is True, "DEFECT [clean artifact audit]: valid artifacts must pass"
    for field in ("source_revision", "pdf_sha256", "pdf_byte_count", "page_count", "pdf_metadata", "commands", "tool_versions", "input_inventory", "source_manifest_digest", "artifact_hashes"):
        assert require_field(outcome, field, "clean artifact audit") == expected[field], f"DEFECT [clean artifact audit]: exact {field} does not match fixture bytes/records"
    for field in diagnostics:
        assert require_field(outcome, field, "clean artifact audit") == [], f"DEFECT [clean artifact audit]: clean diagnostic {field} must be empty"
    commands = require_field(outcome, "commands", "clean artifact audit")
    assert tuple(Path(command["argv"][0]).stem.lower() for command in commands) == (
        "pdflatex",
        "bibtex",
        "pdflatex",
        "pdflatex",
    ), "DEFECT [clean artifact audit]: command evidence must be exactly pdflatex, bibtex, pdflatex, pdflatex"
    assert require_field(outcome, "changed_pages", "clean artifact audit") == [1, 2], "DEFECT [clean artifact audit]: without a baseline, every PDF page must be selected for rendering"


@pytest.mark.parametrize(
    "kind, log, diagnostic_field",
    [
        ("undefined_reference", "LaTeX Warning: Reference `missing' undefined.\n", "undefined_references"),
        ("undefined_citation", "LaTeX Warning: Citation `missing' undefined.\n", "undefined_citations"),
        ("rerun", "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n", "rerun_requests"),
        ("fatal", "! Emergency stop.\n", "fatal_errors"),
        ("overfull", "Overfull \\hbox (2.0pt too wide)\n", "overfull_boxes"),
        ("question_marks", "output ??\n", "literal_double_question_marks"),
        ("invalid_status", "STATUS: NOT_A_STATUS\n", "invalid_status_tags"),
    ],
)
def test_each_real_bad_log_fixture_populates_its_named_diagnostic(tmp_path: Path, kind: str, log: str, diagnostic_field: str):
    root, build, _ = artifacts(tmp_path, log)
    outcome = run_audit(root, build, f"{kind} log fixture")
    assert require_field(outcome, "ok", f"{kind} log fixture") is False, f"DEFECT [{kind} log fixture]: audit accepted real bad log"
    assert require_field(outcome, diagnostic_field, f"{kind} log fixture"), f"DEFECT [{kind} log fixture]: audit failed without populating {diagnostic_field}"


@pytest.mark.parametrize(
    "kind, diagnostic_field, token",
    [
        ("missing_pdf", "errors", "main.pdf"),
        ("missing_aux", "errors", "main.aux"),
        ("duplicate_label", "duplicate_labels", "one"),
        ("failed_command", "errors", "pdflatex"),
        ("wrong_command_order", "errors", "command"),
        ("fabricated_metadata", "errors", "main.pdf"),
        ("stale_aux", "stale_auxiliary_files", "stale.aux"),
    ],
)
def test_bad_artifact_state_populates_its_named_diagnostic(tmp_path: Path, kind: str, diagnostic_field: str, token: str):
    root, build, _ = artifacts(tmp_path)
    if kind == "missing_pdf":
        (build / "main.pdf").unlink()
    elif kind == "missing_aux":
        (build / "main.aux").unlink()
    elif kind == "duplicate_label":
        (build / "main.aux").write_text("\\newlabel{one}{{1}{1}}\n\\newlabel{one}{{2}{2}}\n", encoding="utf-8")
    elif kind == "failed_command":
        commands = json.loads((build / "commands.json").read_text(encoding="utf-8"))
        commands[-1]["returncode"] = 1
        (build / "commands.json").write_text(json.dumps(commands), encoding="utf-8")
    elif kind == "wrong_command_order":
        commands = json.loads((build / "commands.json").read_text(encoding="utf-8"))
        commands[0], commands[1] = commands[1], commands[0]
        (build / "commands.json").write_text(json.dumps(commands), encoding="utf-8")
    elif kind == "fabricated_metadata":
        (build / "main.pdf").write_bytes(b"not a PDF")
        (build / "main.pdf.metadata.json").write_text(json.dumps({"page_count": 1, "sha256": "fabricated"}), encoding="utf-8")
    else:
        (build / "stale.aux").write_text("stale\n", encoding="utf-8")
    outcome = run_audit(root, build, f"{kind} artifact fixture")
    assert require_field(outcome, "ok", f"{kind} artifact fixture") is False, f"DEFECT [{kind} artifact fixture]: audit accepted bad artifact state"
    diagnostic = require_field(outcome, diagnostic_field, f"{kind} artifact fixture")
    assert token in diagnostic_text(diagnostic), f"DEFECT [{kind} artifact fixture]: {diagnostic_field} did not name {token}"


def test_build_script_verifies_result_nonmutating_before_any_tex_command(tmp_path: Path):
    repo = tmp_path / "script-repo"
    source = repo / "manuscripts" / "gauge_vfe_rg"
    verification = source / "verification"
    verification.mkdir(parents=True)
    script = source / "build.ps1"
    script.write_bytes(BUILD_SCRIPT_PATH.read_bytes())
    (source / "main.tex").write_text("\\documentclass{article}\n\\begin{document}x\\end{document}\n", encoding="utf-8")
    (verification / "run_checks.py").write_text("# controlled fake runner target\n", encoding="utf-8")
    (verification / "build_audit.py").write_text("# controlled fake audit target\n", encoding="utf-8")
    result = verification / "result.json"
    result.write_bytes(b'{"sentinel":"must-not-change"}')
    git(repo, "init")
    source_revision = commit(repo, "script fixture")

    tools = tmp_path / "fake-tools"
    tools.mkdir()
    trace = tmp_path / "tool-trace.txt"

    def fake_command(name: str, label: str, returncode: int) -> Path:
        path = tools / f"{name}.cmd"
        path.write_text(
            f'@echo off\r\n>>"{trace}" echo {label} %*\r\nexit /b {returncode}\r\n',
            encoding="ascii",
        )
        return path

    fake_python = fake_command("python", "python", 23)
    fake_pdflatex = fake_command("pdflatex", "pdflatex", 0)
    fake_bibtex = fake_command("bibtex", "bibtex", 0)
    before = result.read_bytes()
    build_dir = tmp_path / "isolated-build"
    report = tmp_path / "verification-report.json"
    audit = tmp_path / "build-audit.json"
    powershell = Path(r"C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe")
    environment = dict(os.environ)
    environment["PATH"] = f"{tools}{os.pathsep}{environment.get('PATH', '')}"
    completed = subprocess.run(
        [
            str(powershell),
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(script),
            "-OutputDirectory",
            str(build_dir),
            "-AuditPath",
            str(audit),
            "-SourceRevision",
            source_revision,
            "-VerificationResult",
            str(result),
            "-VerificationReport",
            str(report),
            "-PythonPath",
            str(fake_python),
            "-PdflatexPath",
            str(fake_pdflatex),
            "-BibtexPath",
            str(fake_bibtex),
        ],
        cwd=repo,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )
    observed = trace.read_text(encoding="utf-8").splitlines() if trace.is_file() else []
    assert completed.returncode != 0, "DEFECT [build verify-first]: failed numerical verification did not fail the build"
    assert result.read_bytes() == before, "DEFECT [build verify-first]: build mutated the verification result"
    assert observed and observed[0].startswith("python ") and "--verify" in observed[0], "DEFECT [build verify-first]: numerical --verify was not the first external command"
    assert not any(line.startswith(("pdflatex ", "bibtex ")) for line in observed), "DEFECT [build verify-first]: TeX ran after failed numerical verification"


def test_build_script_runs_exact_pass_order_then_fails_on_audit_finding(tmp_path: Path):
    repo = tmp_path / "script-repo"
    source = repo / "manuscripts" / "gauge_vfe_rg"
    verification = source / "verification"
    verification.mkdir(parents=True)
    script = source / "build.ps1"
    script.write_bytes(BUILD_SCRIPT_PATH.read_bytes())
    (source / "main.tex").write_text("\\documentclass{article}\n\\begin{document}x\\end{document}\n", encoding="utf-8")
    (verification / "run_checks.py").write_text("# controlled fake runner target\n", encoding="utf-8")
    (verification / "build_audit.py").write_text("# controlled fake audit target\n", encoding="utf-8")
    result = verification / "result.json"
    result.write_bytes(b'{"sentinel":"must-not-change"}')
    git(repo, "init")
    source_revision = commit(repo, "script fixture")

    tools = tmp_path / "fake-tools"
    tools.mkdir()
    trace = tmp_path / "tool-trace.txt"
    build_dir = tmp_path / "isolated-build"
    report = tmp_path / "verification-report.json"
    audit = tmp_path / "build-audit.json"
    fake_python = tools / "python.cmd"
    fake_python.write_text(
        "\r\n".join(
            [
                "@echo off",
                f'>>"{trace}" echo python %*',
                'echo %* | findstr /C:"run_checks.py" >nul',
                "if not errorlevel 1 (",
                f'  >"{report}" echo {{"ok":true,"source_revision":"{source_revision}"}}',
                "  exit /b 0",
                ")",
                'echo %* | findstr /C:"build_audit.py" >nul',
                "if not errorlevel 1 (",
                f'  >"{audit}" echo {{"ok":false,"errors":["forced audit finding"]}}',
                "  exit /b 0",
                ")",
                "exit /b 97",
                "",
            ]
        ),
        encoding="ascii",
    )
    fake_pdflatex = tools / "pdflatex.cmd"
    fake_pdflatex.write_text(
        "\r\n".join(
            [
                "@echo off",
                f'>>"{trace}" echo pdflatex %*',
                ">main.pdf echo fake pdf",
                ">main.log echo Output written on main.pdf (1 page, 9 bytes).",
                ">main.aux echo auxiliary",
                ">main.toc echo contents",
                "exit /b 0",
                "",
            ]
        ),
        encoding="ascii",
    )
    fake_bibtex = tools / "bibtex.cmd"
    fake_bibtex.write_text(
        f'@echo off\r\n>>"{trace}" echo bibtex %*\r\n>main.bbl echo bibliography\r\nexit /b 0\r\n',
        encoding="ascii",
    )
    before = result.read_bytes()
    powershell = Path(r"C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe")
    environment = dict(os.environ)
    environment["PATH"] = f"{tools}{os.pathsep}{environment.get('PATH', '')}"
    completed = subprocess.run(
        [
            str(powershell),
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(script),
            "-OutputDirectory",
            str(build_dir),
            "-AuditPath",
            str(audit),
            "-SourceRevision",
            source_revision,
            "-VerificationResult",
            str(result),
            "-VerificationReport",
            str(report),
            "-PythonPath",
            str(fake_python),
            "-PdflatexPath",
            str(fake_pdflatex),
            "-BibtexPath",
            str(fake_bibtex),
        ],
        cwd=repo,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )
    observed = trace.read_text(encoding="utf-8").splitlines() if trace.is_file() else []
    labels = tuple(line.split(" ", 1)[0] for line in observed)
    assert completed.returncode != 0, "DEFECT [build audit gate]: audit ok=false did not fail the build"
    assert result.read_bytes() == before, "DEFECT [build audit gate]: build mutated the verification result"
    assert labels == ("python", "pdflatex", "bibtex", "pdflatex", "pdflatex", "python"), "DEFECT [build audit gate]: external command order was not verify, pdflatex, bibtex, pdflatex, pdflatex, audit"
    assert audit.is_file() and json.loads(audit.read_text(encoding="utf-8"))["ok"] is False, "DEFECT [build audit gate]: controlled audit finding was not emitted"
