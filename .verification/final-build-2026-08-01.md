# Final mechanical verification record

Artifact: `manuscripts/gauge_vfe_rg/main.pdf`
Build date: 2026-08-01
Build command: `manuscripts/gauge_vfe_rg/build.ps1`

The build script ran `pdflatex`, `bibtex`, `pdflatex`, and `pdflatex` from the
manuscript directory and returned exit status zero. The final artifact and log
at the paths recorded here were produced by that run.

## PDF and log checks

- Pages: 162
- Bytes: 1,101,044
- PDF SHA-256:
  `F1275DC2DAA3CDA4410273FDB910DD9FDD286A00F30A47286DF83D9067FE80E7`
- Extracted characters: 487,168
- Literal `??` in extracted PDF text: 0
- Final-log matches for LaTeX/package warnings, undefined or multiply defined
  references, rerun requests, overfull/underfull boxes, fatal errors,
  emergency stops, and float-size errors: 0
- TeX labels: 532 declared, 532 unique, 0 duplicates
- Literal `??` in manuscript TeX: 0
- `TODO`, `FIXME`, `TBD`, `PLACEHOLDER`, or `CITATION NEEDED` tokens in
  manuscript TeX: 0
- Invalid `\status{OPTIONAL}` tags: 0
- `git diff --check`: no whitespace errors (only Git's line-ending notices)

The contents pages establishing the general-before-Gaussian order, the general
holonomy-KL theorem and proof, and the Gaussian barycenter and counterexample
pages were rendered to PNG and visually inspected. Text is readable; equations
and headings are not clipped or overlapped.

## Numerical checks

- Command: `C:\Python314\python.exe manuscripts\gauge_vfe_rg\verification\run_checks.py`
- Result: 29 PASS, 0 FAIL, 0 INCONCLUSIVE
- Claim inventory: PASS
- Tagged numerical occurrences: 11
- Substantive numerical claims: 9, all mapped to passing checks
- Live result SHA-256:
  `71D06107DD63A39F7039EBDC521415FA4CA6983A71073EC5ED43534DF7780F62`
- A second fresh run to an independent output path returned the same 29/0/0
  totals and PASS inventory.

## Independent rereview

- General holonomy-KL rereview: no mathematical regression; clean verdict.
- Gaussian specialization rereview: channel typing, fixed-sector theorem,
  projector, barycenter, compact-holonomy formulas, and attainment caveat are
  clean.
- Manuscript-integration rereview: all eight identified consistency findings
  were rechecked after repair and found resolved.
