# Numerical reproducibility package

This directory makes the manuscript's computational claims auditable without
confusing numerical agreement with mathematical proof.

The post-review source contains **11 literal `\status{NUMERICAL}` tokens**:

- 9 substantive, current-protocol claims;
- one scope summary; and
- one status-taxonomy entry.

Local chapter status registers were removed. Bare table cells such as
`& NUMERICAL &` are forbidden. The runner discovers every `*.tex` file under
the manuscript source root and fails closed if the number or order of tokens,
the declared check mapping, or the source manifest drifts.

## Run

From the repository root:

```powershell
& "C:\Python314\python.exe" manuscripts/gauge_vfe_rg/verification/run_checks.py
```

To retain a separate comparison artifact:

```powershell
& "C:\Python314\python.exe" manuscripts/gauge_vfe_rg/verification/run_checks.py `
  --output C:\tmp\gauge-vfe-rg-results.json
```

The default command rewrites `current-results.json` and exits nonzero if the
source inventory, claim mapping, supplemental checks, or numerical endpoints
fail.

## Files and binding

- `claims.json` maps every numerical-status token to its semantic claim,
  protocol, checks, and disposition.
- `run_checks.py` is the deterministic CPU entry point.
- `current-results.json` records environment metadata, the source manifest,
  check results, current line numbers, dispositions, and the complete-result
  digest.
- `requirements.txt` records third-party dependencies.

The result manifest contains the SHA-256 digest and byte count of every
recursively discovered TeX source and of the four protocol files above,
excluding generated `current-results.json` to avoid self-reference. It does
not bind the bibliography, PDF, installed dependency binaries, or external
sources. Those are checked separately by the manuscript build and source
audit.

## Coverage

The suite contains **29 deterministic checks** covering:

- Gaussian interaction structure, conditioning, and exact Kron witnesses;
- Gaussian restriction identities and information-geometric charts;
- generalized-spectrum gauge invariance;
- exact aggregation, holonomy, admissible partitions, associativity,
  bi-additivity, singular limits, frame cancellation, and equivariance;
- finite RG ray, sector, invariant-face, homogeneous, noncommuting-limit, and
  mass-pencil endpoints; and
- star/fold and reciprocal-pair determinant, kernel, and normalizer identities.

Some checks are supplemental because the tightened manuscript no longer
repeats a numerical tag for every corroborating endpoint. They remain mandatory
and are listed explicitly in `claims.json`.

## Interpretation

`PASS` means that the current source and protocol reproduce the declared finite
endpoint within its recorded tolerance. It does **not** prove a theorem,
genericity, convergence, universality, blocking-scheme independence, or a
physical law. Analytic statements are closed only by derivation or an eligible
primary source; asymptotic and physical claims remain open until their separate
obligations are discharged.
