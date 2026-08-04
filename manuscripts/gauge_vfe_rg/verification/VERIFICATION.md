# Numerical reproducibility package

This directory makes the manuscript's computational claims auditable without
confusing numerical agreement with mathematical proof.

The post-review source contains **12 literal `\status{NUMERICAL}` tokens**:

- 10 substantive, current-protocol claims;
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

The checked-in `current-results.json` is still the older 29-check artifact. It
is not evidence for the 30-check package described below; Task 4 must regenerate
it under the governed result lifecycle.

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

## Stable factorization-gap protocol

`CHK-CG-FACTOR-GAP-STRESS-3138` is a new frozen protocol with seed `20260803`.
It regenerates 3,138 case-bound SPD matrices and partitions across dimensions
2 through 16 and nominal pre-transform generator-condition labels from 1
through `1e14`, records matrix and partition SHA-256 digests, and includes 18
designated exact-input controls evaluated at 100 decimal digits. Every record's
legacy `condition_number` field remains the nominal label; its
`achieved_condition_number` field is exactly `numpy.linalg.cond` of that same
digest-bound regenerated matrix. Repeated calls with the same schedule are
byte-for-byte deterministic at the record level.

The achieved 2-norm condition-number ranges are:

| stratum | minimum | maximum |
|---|---:|---:|
| global | `1` | `1.015265553314175e14` |
| general | `1` | `1.015265553314175e14` |
| exact block diagonal | `1` | `1.0075938532153164e14` |
| near decoupled | `1.0000000000000002` | `9.273791153286738e8` |
| scale | `1` | `1.0036120669923527e14` |
| permutation | `1` | `1.0071935024197442e14` |
| nested refinement | `1` | `1.0077056571347422e14` |
| 100-digit controls | `1.0000000000000004` | `1.0048132000124055e14` |

Only the global schedule is claimed to reach achieved conditioning near
`1e14`. Dimension-two exact-block cases contain two scalar blocks and therefore
do not realize their nominal targets; the near-decoupled stratum likewise does
not attain its high nominal labels. The runtime check evaluates an independent
100-digit exact-binary64 reference for every one of the 3,138 cases and retains
complete case identities and diagnostics for every failure. The 18 controls
remain a designated stratum, not the sole all-case evidence.

The ordinary implementation uses Cholesky factors, SciPy triangular solves,
canonical-correlation singular values, and `log1p(-rho**2)`. It does not form an
explicit inverse or subtract log determinants. A value within
`64*n*epsilon` of the singular-value boundary is routed to a 200-decimal-digit
evaluation of the exact binary64 input. A second binary64 solve backend defines
the raw-excursion diagnostic as the maximum observed across those two declared
binary64 backends. Exact-input domain violations and
raw excursions whose discrepancies exceed the operational guard fail closed.
The exact-input value path is also used when
`kappa_2(precision)*epsilon >= 1e-4`, when global power-of-two normalization
would lose a nonzero entry, or when a binary64 Cholesky, solve, SVD, or condition
diagnostic is unusable. This is a frozen-suite conditioning trigger, not a
universal perturbation radius; a nonfinite binary64 condition estimate triggers
adaptive-precision exact-dyadic Cholesky certification and reevaluation rather
than rejection. Cholesky and
solve residuals remain local backward diagnostics only. Their finite-health
gate is `64*gamma_n`, where `gamma_n=n*u/(1-n*u)` and binary64 unit roundoff is
`u=epsilon/2`; this gate is not used as a forward bound on `rho`, the gap,
relative entropy, monotonicity, scale invariance, or any oracle comparison.
Forward comparisons use independent exact-binary64 high-precision references
and separately labeled endpoint-roundoff or declared protocol-acceptance
policies.

The compatibility field `residual_derived_clip_bound` does not assert a general
residual-to-forward-error theorem. On the boundary path it reports the
outward-rounded discrepancy between the maximum raw binary64 `rho**2` and its
high-precision exact-input value. The positive-excursion witness is a separate
focused regression fixture, not an ordinary 3,138-case schedule outcome. It
binds matrix SHA-256
`45310a74550d3759fed0f83f71a6cf3b0f45942499361d723a2248bbe243e2e3`, exact
gap `22.777105858844084`, raw excursion `4.440892098500626e-16`, outward
allowance `9.432369402326953e-16`, and PASS status. The runtime check
mechanically recomputes all four quantities. A nearest-below-one clipped value
is not accepted as the gap. The compatibility
fields `clipping_applied` and `clipping_amount` identify an admitted positive
cross-backend excursion and its maximum excess above one; they do not describe
a numerical adjustment used to obtain the returned value.

## Coverage

The suite contains **30 deterministic checks** covering:

- Gaussian interaction structure, conditioning, and exact Kron witnesses;
- Gaussian restriction identities, the 3,138-case stable determinant-gap
  protocol, and information-geometric charts;
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
