# Numerical reproducibility package

This directory makes the manuscript's numerical-status surface auditable without
turning numerical agreement into mathematical proof.

The frozen source contains **39 literal `\status{NUMERICAL}` macro
occurrences**:

- 30 substantive numerical claims;
- one status-taxonomy entry; and
- eight duplicate/current-summary status-register entries.

Bare status-table cells of the form `& NUMERICAL &` are forbidden. The frozen
source has zero. The runner records any such cell under
`inventory.bare_status_table_entries` and fails the inventory, ensuring the
macro-token inventory covers the complete semantic numerical-status surface.

The runner recursively discovers every `*.tex` file under the manuscript source
root before executing any checks. It fails closed if an occurrence count/order
or declared check ID drifts, including if a `NUMERICAL` tag appears in a
previously undeclared TeX file. It also emits a cryptographic manifest, so edits
to surrounding source that preserve the tag count still change the bound result
artifact.

## Run

From the repository root:

```powershell
& "C:\Python314\python.exe" manuscripts/gauge_vfe_rg/verification/run_checks.py
```

To write a separate comparison artifact:

```powershell
& "C:\Python314\python.exe" manuscripts/gauge_vfe_rg/verification/run_checks.py `
  --output C:\tmp\gauge-vfe-rg-results.json
```

The default command rewrites `current-results.json` and exits nonzero if the TeX
inventory drifts, a claim mapping is invalid, a required supplemental check is
unknown or nonpassing, or any implemented check fails.

## Files

- `claims.json` is the stable claim inventory. Every occurrence has a semantic
  ID, source occurrence and inventory-time line, section or label, stated seed,
  sample count, tolerance, load-bearing classification, current-protocol
  reproducibility assessment, check mapping, disposition, and any open
  obligation.
- `run_checks.py` is the single deterministic CPU entry point. Each check emits
  its seed, sample count, observed values, expected identity or inequality,
  tolerance, evidence kind, and `PASS`/`FAIL`/`INCONCLUSIVE` status.
- `current-results.json` records the current environment, source manifest,
  rescanned source line numbers, all check results, claim dispositions, and
  mapping validation.
- `requirements.txt` lists the third-party dependencies.

Exact Python, NumPy, SciPy, and SymPy versions and floating-point metadata are
stored in `current-results.json`.

## Source binding

`current-results.json.inventory_manifest` records the manuscript source root as
a repository-relative POSIX path and the SHA-256 digest and byte count of the raw
bytes read for every recursively discovered TeX file. The frozen tree has 14:

- `main.tex`;
- `01_introduction.tex` through `05_elbo.tex`;
- `05a_expfamily.tex`; and
- `06_gaussian.tex` through `12_philosophy.tex`.

Files with zero `\status{NUMERICAL}` occurrences are included. This makes an
undeclared tag in any current or newly added TeX source a failing inventory
drift, and makes any other TeX-byte change visible in the manifest.

The same manifest binds the raw bytes of `claims.json`, `run_checks.py`,
`requirements.txt`, and this `VERIFICATION.md`. It deliberately excludes the generated
`current-results.json` itself to avoid self-reference. It also does not claim to
bind the bibliography, generated PDF, other non-TeX manuscript assets,
installed dependency binaries, or external sources. Dependency versions and
runtime metadata are recorded separately under `environment`.

An inventory `PASS` establishes the declared tag counts/order and check
mappings. It is not a semantic interpretation of the surrounding prose. The
manifest and the SHA-256 of the complete result artifact are what bind a
reported run to the exact scanned source and protocol bytes.

Two executions are expected to be byte-identical only under the same source,
protocol, dependency, interpreter, and inherited process environment. The
result intentionally records environment metadata; on Windows,
`environment.machine` can vary with inherited architecture environment
variables even when the source and numerical values are unchanged. Such a
change correctly produces a different complete-result hash and should not be
misreported as same-environment byte nondeterminism.

## What is checked

The current suite contains **29 deterministic checks**. It covers:

- exact projection controls, trivialization, and conditioning for Gaussian
  interaction families;
- restriction-versus-marginal precision and constrained-mean KKT identities;
- expectation-coordinate Fisher geometry, pullback-versus-pushforward metrics,
  and frame-invariant generalized spectra with ordinary-spectrum controls;
- exact aggregation, direct-KL factorization optima, seeded SPD-preserving
  perturbations, refinement monotonicity, scale behavior, explicit twisted
  graph Laplacians, algorithmically generated admissible cluster partitions,
  the full lambda continuum, pair-merge associativity, translation,
  bi-additivity, singular-limit cost, mean ties, frame cancellation, and
  finite-order equivariance;
- RG ray kernels, sector splitting, invariant common-range faces, an explicit
  exact `6 x 6` homogeneous gate, exact symbolic noncommuting limits, a separate
  seeded six-agent floating check, and mass-pencil transfer; and
- star-versus-fold, reciprocal-pair determinant and kernel identities, exact
  matrix-Kron and scalar-normalizer witnesses, and a separate seeded
  matrix-Kron sweep.

For floating checks, reported residuals are paired with their tolerances.
`CHK-RG-NONCOMMUTING-LIMITS` is exact symbolic evidence; the distinct
`CHK-RG-NONCOMMUTING-FLOATING` check is reproduced floating-point evidence.
The suite uses no GPU.

## Supplemental review checks

Six checks are deliberately not mapped one-to-one to a current
`\status{NUMERICAL}` occurrence but are still required to pass:

- `CHK-KRON-EXACT-WITNESS`;
- `CHK-KRON-MONTE-CARLO`;
- `CHK-CG-MAXIMAL-CLUSTERS`;
- `CHK-RG-HOMOGENEOUS-GATE`;
- `CHK-RG-NONCOMMUTING-FLOATING`; and
- `CHK-OBS-NORMALIZER-WITNESS`.

## Interpretation and dispositions

A `PASS` is current reproduced-output evidence for the exact endpoint encoded by
that check. It is not a proof of an analytic statement. The theorem text must
continue to rely on derivations, exact finite witnesses, or cited results.
Repeated numerical agreement cannot establish genericity, convergence,
universality, or a physical law.

The frozen inventory has the following substantive dispositions:

- 29 `keep_exact`;
- 0 `rewrite_to_current_check`;
- 0 `remove`; and
- 1 `retain_as_inconclusive`.

The sole unresolved substantive item is `NUM-RG-PHYSICAL-LAW`. Its register
cross-reference is one of the eight duplicate entries and does not create a
second scientific claim. The current text
does not supply a frozen observable, estimator, parameter grid, convergence
criterion, seed set, or uncertainty analysis capable of verifying a physical
law. It therefore remains `INCONCLUSIVE`; the suite does not replace that
missing scientific protocol.

For every disposition, `current-results.json` includes the current TeX line,
applicable check IDs, and the exact missing obligation. Integration should be
driven from that machine-readable record rather than from remembered numerical
values.
