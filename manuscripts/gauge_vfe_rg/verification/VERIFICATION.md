# Numerical reproducibility package

## Current source and historical harness

The current manuscript is the three-document source rooted at `Theory/main.tex`,
`Theory/supplement_gaussian.tex`, and `Theory/supplement_base.tex`. The inventory
on September 26, 2026 has respectively 1, 0, and 3 literal
`\status{NUMERICAL}` tokens across their input closures; the main token is the
status-taxonomy entry. These counts do not certify any numerical result.

The production manifest, runner, bootstrap, and lifecycle files below belong
to the earlier `manuscripts/gauge_vfe_rg` layout. They still require paths and
claim inventories absent from this checkout and are retained as historical
protocol artifacts. Their commands are not current manuscript acceptance
commands. The retained results have not been regenerated or reclassified.
Do not invoke bundled tamper or forgery tests: those checks are user-excluded.

For the current document build, copy `Theory/*.tex`, `*.bib`, and `*.sty` to a
scratch directory and run `latexmk -pdf` there, in the order `main.tex`,
`supplement_gaussian.tex`, `supplement_base.tex`. Check all three logs for
undefined references, undefined citations, and multiply defined labels.
The source-only cross-document checker is
`docs/reviews/2026-09-23-theory-streamlining-review/scripts/phase2/labelgraph.py split`.
Neither compilation nor that checker is a mathematical proof. The September 26
review's analytic counterexamples, symbolic checks, independent reconstruction,
and build record are in `docs/reviews/2026-09-26-theory-deep-review/`.

## Historical protocol description

The following counts and commands describe the pre-split protocol. In that
source snapshot there were **13 literal `\status{NUMERICAL}` tokens**:

- 11 substantive, current-protocol claims;
- one scope summary; and
- one status-taxonomy entry.

Local chapter status registers were removed. Bare table cells such as
`& NUMERICAL &` are forbidden. The runner discovers every `*.tex` file under
the manuscript source root and fails closed if the number or order of tokens,
the declared check mapping, or the source manifest drifts.

Each mapped numerical token must be the sole status in its prose paragraph
(apart from the explicitly captioned Status taxonomy table), and its
`source_line_at_inventory` value in `claims.json` must equal the current
literal source line. This binds one semantic numerical claim to one token and
one source location.

## Run

The authenticated production entry is the externally approved one-line
`build_bootstrap_transport.txt`, supplied as raw ASCII standard input to fixed
Windows PowerShell. Its decoded readable audit body is
`build_bootstrap_reference.ps1.txt`; that readable file is not itself an
authenticated launcher. Bootstrap modes `NumericalUpdate` and
`NumericalVerify` authenticate and retain the source `run_checks.py` identity
before execution. The externally asserted transport byte count and SHA-256 are
release inputs, not values learned from the checkout being tested.

Direct checkout execution is an unauthenticated developer convenience only.
It can diagnose the runner contract, but it cannot establish production
release provenance. A convenience verification from the repository root is:

```powershell
& "C:\Python314\python.exe" -I -S manuscripts/gauge_vfe_rg/verification/run_checks.py `
  --verify C:\tmp\gauge-vfe-rg-results.json `
  --report C:\tmp\gauge-vfe-rg-verify-report.json
```

The corresponding unauthenticated convenience update is:

```powershell
& "C:\Python314\python.exe" -I -S manuscripts/gauge_vfe_rg/verification/run_checks.py `
  --update C:\tmp\gauge-vfe-rg-results.json `
  --source-revision <full-lowercase-40-hex-commit> `
  --report C:\tmp\gauge-vfe-rg-update-report.json
```

If `--source-revision` is omitted in update mode, the runner uses the current
full `HEAD`. `--source-revision` is rejected in verify mode. `--update` and
`--verify` are mutually exclusive and each requires a result path. A report
target must differ from the result and must be outside the repository. An
update target must likewise be outside the repository, except for the exact
canonical `verification/current-results.json` path. Every invocation prints
the complete strict JSON operation report. A fresh safe `--report` target may
receive a failure document. An existing report is never overwritten on a
precommit failure; the current diagnostic remains on standard output. A
success report contains an invocation-unique lowercase 32-hex
`transaction_receipt_id` and a 64-hex `published_result_sha256`. Consumers
must require `ok=true`, `input_unchanged=true`, and exact equality among the
current result's raw SHA-256, `input_sha256_before`, `input_sha256_after`, and
`published_result_sha256`, in addition to exact lexical result path, protocol
profile, source revision, and a fresh receipt.

The checked-in `current-results.json` is still the older 29-check artifact. It
is intentionally historical and this implementation does not regenerate it.
It is not evidence for the 30-check package described below. A separately
governed evidence regeneration remains required before that evidence is
current.

## Files and binding

- `claims.json` maps every numerical-status token to its semantic claim,
  protocol, checks, and disposition. It and `manifest-policy.json`
  independently carry the exact `gauge-vfe-rg-production-v1` profile marker.
- `run_checks.py` is the deterministic CPU entry point.
- `result.schema.json` closes the schema-3 result envelope, dependency map,
  manifest entries, and four-field check records.
- `manifest-policy.json` declares the nonshrinkable protocol profile, recursive
  classes, exact inputs, style search order, governed namespaces, and explicit
  exclusions. The separately marked `synthetic-test-fixture-v1` profile is a
  closed test-fixture envelope; production mode cannot infer it from a
  top-level `checks` list.
- `lifecycle_gate.py` and `build_audit.py` close the revision and build-artifact
  lanes and are themselves bound inputs.
- `build_bootstrap_reference.ps1.txt` is the readable audit body.
  `build_bootstrap_transport.txt` is the exact governed one-line ASCII
  transport; strict base64 decoding must reproduce the reference bytes
  byte-for-byte. Both files and `tests/test_build_bootstrap.py` are mandatory
  at every production lifecycle endpoint.
- Every release phase enumerates the complete commit DAG reachable from its
  newer endpoint but not from its older endpoint (`rev-list newer ^older`).
  Every newly reachable commit is checked against the phase baseline, and
  every immediate parent-to-child edge whose child is newly reachable is
  checked independently. Parents already reachable from the older endpoint are
  baseline anchors rather than new phase commits; their trees still must load
  so their outgoing phase edges satisfy the same path, status, type, and
  regular-blob policy without a skip or waiver.
- Post-`W` lifecycle and publication purity uses the same complete
  newly-reachable enumeration for `W..HEAD`, `W..P`, and `P..HEAD`. Every
  returned tree must equal `W` on the entire protected path union, including
  existence, mode, object type, and blob identity. Per-edge checks are not
  needed for this lane because exact comparison of every newly reachable tree
  to the fixed `W` baseline detects each transient protected state directly.
  A newly imported pre-`W` side commit that lacks `W`'s protected state is
  rejected; an unrelated integration is admissible only when every imported
  tree preserves the exact `W` protected projection.
- `requirements.txt` is a strict six-line exact-pin contract for NumPy 2.4.4,
  SciPy 1.17.1, SymPy 1.14.0, mpmath 1.3.0, pypdf 6.12.2, and pytest 9.0.2.
  All six packages are mandatory. Results record non-null provenance for each;
  metadata, the dependency map, provenance versions, and the exact pins must
  agree. Uniform LF and uniform CRLF checkout bytes are both parsed; BOMs,
  mixed endings, bare carriage returns, whitespace, ranges, and comments fail.
- `current-results.json` is excluded from its own manifest, as is the compiled
  `main.pdf`; neither exclusion can be enlarged by editing the policy.

The production TeX lane binds the bibliography by the logical name
`references`. `BIBINPUTS` is exactly the absolute `manuscripts` directory and
`BSTINPUTS` is exactly the admitted style directory; neither value carries a
trailing search-list separator that would restore a default lookup path. The
retained BibTeX AUX and BLG snapshots must report exactly `plainnat` /
`plainnat.bst` and `references` / `references.bib`. The build audit acquires
deny-write/delete read handles for the complete isolated build-file inventory
before M0, derives hashes and semantic parses from those same held bytes, and
retains the handles through M1 and audit-report publication. Canonical
`main.fls` must be byte-identical to the retained pass-4 recorder, and every
recorded repository input must already belong to the prelocked source
envelope. The audit report itself is published only to an absent path with a
CreateNew/no-replace handle retained through exact SHA-256 marker emission; a
raced-in or preexisting target is preserved unchanged.

The manifest maps every bound repository-relative POSIX path to the SHA-256
digest and byte count of its raw worktree bytes. Discovery includes every TeX
source recursively, `SPEC.md`, the bibliography, every existing style
candidate in search order, `build.ps1`, all verification core files, and every
recursive `test_*.py`. Any other regular file in a governed namespace must be
an allowed explicit exclusion or discovery fails. Missing files, symlinks,
junctions, reparse traversal, path escape, duplicate/case-colliding paths, and
pre/post-read metadata drift fail closed. A literal `bound_paths` list may add
inputs but cannot replace or shrink the required recursive declarations.

Every Git subprocess receives an environment with all caller-provided `GIT_*`
variables removed and uses the fixed Git executable with
`--no-replace-objects`. Nonempty graft, shallow-boundary, local alternate, or
HTTP-alternate metadata is rejected around ancestry and object reads.
Source-tree lookup uses literal
pathspecs with exactly one NUL-terminated record. The full governed path set is
also enumerated from the source revision and must equal both current discovery
and the stored manifest, so deleting a committed recursive TeX or `test_*.py`
cannot shrink verification. The recorded source
revision `S` must resolve to itself and be an ancestor of current `HEAD=E`.
Each current retained raw manifest entry and stored manifest entry must equal
the byte count and SHA-256 of the regular blob at `S`. This comparison admits
no line-ending normalization: untracked `.gitattributes`,
`.git/info/attributes`, `core.autocrlf`, custom clean filters, `ident`, and
working-tree encodings cannot relax a raw-byte mismatch.
A Windows checkout materialized with CRLF while `S` stores LF is therefore
rejected; production and evidence worktrees must contain the exact blob bytes.
The release protocol assumes no concurrent writer can create, use, and restore
Git administrative metadata wholly between one subprocess's stable preflight
and postflight checks; kernel directory-event monitoring is intentionally
outside this verifier profile.

Persisted JSON is the project-specific compact canonical form: UTF-8,
`ensure_ascii=False`, sorted keys, `separators=(",", ":")`, finite values only,
and no trailing newline. Parsing rejects invalid UTF-8, duplicate keys,
nonfinite constants, overflow-to-infinity numbers, malformed input, and any
byte representation that is not this form. This is not a claim of RFC 8785/JCS
number canonicalization. The semantic digest authenticates exactly the entire
top-level document except `generated_at_utc` and
`semantic_payload_digest`; same-named nested fields remain authenticated.
`protocol_profile` is therefore authenticated. `source_dirty=false` is the
derived statement that this governed path set binds byte-for-byte to `S`; it
is not a claim that unrelated, ungoverned worktree paths are clean.

The runner's admitted child startup is the fixed
`C:\Python314\python.exe -I -S` invocation. Before any third-party import, the
stdlib-only bootstrap parses the exact pins, inventories and hashes every
actual RECORD file, and authenticates all six distributions. Only NumPy,
SciPy, SymPy, and mpmath are imported at runtime; pypdf and pytest remain
metadata-only. A meta-path finder rejects undeclared fixed-site modules, and
each delegated loader is bound to its M0 file hash from `create_module` through
`exec_module`. Bytecode writes are disabled and a fresh, non-reparse, empty
cache prefix must remain empty. Python, Git, dependency bytes, current `HEAD`,
and the cache policy are compared exactly at run M0, before persistence, after
staging, and at final closure. The hardcoded manifest-policy path is locked
first; the runner then discovers, source-binds, and transactionally retains
deny-write/delete handles for the exact governed set. Policy, claims, schema,
requirements, and manifest reads are served from those same handles. Exact
rediscovery, raw bytes, handle identity, lexical-path identity, and source
binding are rechecked before publication. On Windows, retained kernel handles
also deny executable and result-file replacement across the relevant evidence
window. These controls trust the Windows kernel, NTFS identity and sharing
semantics, the verifier process, and the fixed interpreter installation; they
do not authenticate transitive DLLs and are not a malware-resistance claim.

Update construction is in-memory and repository-read-only. Canonical result
and report bytes are staged through dedicated deny-write/delete, rename-capable
Windows handles without changing either target. All M1 source, governed-input,
tool, dependency, and report-staging closure runs before either target is
published, and every retained evidence handle is closed before commit. The
two-file commit order is deliberately result first, report second. The exact
published result handle transitions without an unguarded interval to a strict
retained read handle, its raw hash is checked, and it remains held through
report commit. A report-commit failure may therefore leave a valid new result,
but it leaves any old report untouched and emits a failed diagnostic with no
`published_result_sha256`; the old report is mechanically stale by hash and
receipt. Every failure before result commit preserves both existing result and
existing report bytes. A fresh absent report may receive a failure document.
There is no corrective rewrite of a previously published success report.

Verify mode reads the result through one retained Windows handle, cross-checks
that held file identity against the lexical path, independently rebuilds the
manifest before and after recomputation, runs all checks freshly in memory,
stages the report, and retains the result handle through report commit. It
never writes the result. Production results contain
the 30 deterministic numerical checks plus `CHK-SOURCE-INVENTORY`; PASS requires
all 31 ordered checks to be present exactly once and to pass.

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
not attain its high nominal labels. The runtime check separately counts all
3,138 attempted schedule cases, successfully evaluated 100-digit exact-binary64
references, and completed production-reference comparisons. PASS requires
3,138 in each category and zero failures, while every failure retains its
complete case identity and diagnostics. The 18 controls remain a designated
stratum, not the sole all-case evidence.

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
policies. Early `range-or-condition`, `binary64-linear-algebra`, and
`binary64-svd` fallbacks occur before residual evaluation, so
`cholesky_residual`, `solve_residual`, `residual_tolerance`, `backward_error`,
and their corresponding aggregates are `null`. A residual-health fallback
instead retains each finite binary64 measurement, including finite values above
the health threshold. A field is `null` only when no finite usable numeric
diagnostic exists, either because an attempted measurement is nonfinite or
because a derived diagnostic requires an unavailable constituent;
independently finite siblings remain numeric. The finite threshold method
retains the
`binary64-residual-health` reason. Nonfinite method suffixes identify
`nonfinite-cholesky`, `nonfinite-solve`, or `nonfinite-tolerance`, listing
multiple causes in fixed Cholesky, solve, tolerance order. These local backward
diagnostics do not become forward-error bounds or enter a forward tolerance.
In all cases, `null` denotes neither failure nor zero. The zero-step one-block
result continues to report numeric zero diagnostics. The `GapStep` API retains
the fieldwise residual quartet. `FactorizationCaseRecord` serializes only the
aggregate `backward_error_bound`, `maximum_cholesky_residual`, and ordered
`evaluation_methods` tuple, not per-step solve or tolerance values. Despite
its compatibility name, numeric `backward_error_bound` is an aggregate of
one-ULP-up summaries of already rounded local residual measurements; it is
not a certified perturbation or forward-error bound.

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

## Record moved from the manuscript's numerical appendix

When the Theory manuscript was split into a main manuscript and two supplements (Phase 2 of the 2026-09-23 streamlining review, `docs/reviews/2026-09-23-theory-streamlining-review/phase2/PLAN.md`, section 2.2), its numerical appendix ("Numerical Provenance", `app:numerical-provenance`) was reduced to one index table per document, carrying claim label, check label, what is tested, control, and seed or "no randomness", with no repository locator (`Theory/SPEC.md`, rule R9). The package table, run command, stress-protocol strata and digests, binary64 fallback and field semantics, freshness note, and thermodynamic script locators moved here. Each passage below is reproduced verbatim from `Theory/appendix_numerical_provenance.tex` at commit `2d012d1` (map `phase2/map-E8.md`, appendix_numerical_provenance rows 1, 3, 5 and the locators of row 6). Row 2 (the stress protocol) becomes one row of the Supplement G numerical index, row 4 ("What a passing run means") was cut as a restatement of the NUMERICAL row of the status table, and the controls of row 6 become rows of the Supplement B numerical index.

### Package table, run command, and source root

The appendix opened with the package table and the declared run command:

Source: `Theory/appendix_numerical_provenance.tex:4-48` at commit `2d012d1`.

```tex
The verification package in \path{Theory/verification} consists of the
following files:
\begin{center}
\footnotesize
\begin{tabularx}{0.94\textwidth}{@{}>{\raggedright\arraybackslash}p{0.40\textwidth}X@{}}
\toprule
\path{verification/claims.json} &
claim inventory, seeds, sample counts, tolerances, mappings, and open
obligations \\
\path{verification/run_checks.py} &
single deterministic CPU runner \\
\path{verification/current-results.json} &
environment, source and protocol hashes, individual outcomes,
residuals, and overall result of the recorded run \\
\path{verification/VERIFICATION.md} &
human-readable protocol and interpretation \\
\bottomrule
\end{tabularx}
\normalsize
\end{center}

The declared run is
\begin{verbatim}
& "C:\Python314\python.exe" manuscripts/gauge_vfe_rg/verification/run_checks.py
\end{verbatim}
and it cannot be executed against this copy of the sources. The runner takes
its repository root to be the directory two levels above the manuscript
directory that contains \path{verification}, and it scans
\path{manuscripts/gauge_vfe_rg} beneath that root. For this copy the
manuscript directory is \path{Theory}, the root is therefore the parent of the
repository, and the scanned path does not exist; the runner resolves only in
the mirrored layout of the author's research vault, in which the manuscript
directory is itself \path{manuscripts/gauge_vfe_rg}. The claim inventory
\path{verification/claims.json} lists 13 entries, one for each literal
NUMERICAL status tag present when it was written; the
manuscript now carries more such tags, and the three computation-only
paragraphs of \Cref{ch:agent-network-rg} and the comparisons of
\Cref{sec:rg-thermo-numerical-provenance} are not inventoried. The checked-in
\path{verification/current-results.json} records 29 checks and 11 inventoried
occurrences; it contains no entry for the factorization-gap stress check
described below, so it predates the stress values tabulated in this
appendix, which are recorded only in \path{verification/VERIFICATION.md}.
The checks listed in the package are therefore regression corroboration of
proved identities and of stated finite protocols, and no current certified
run exists for this copy of the manuscript.
```

The source root is stale in this repository, and the runner has not been changed. `run_checks.py` sets `TEX_ROOT = HERE.parent`, which is `Theory/`, and `REPO_ROOT = TEX_ROOT.parents[1]` (line 80), which is the directory containing the repository, and it resolves the manuscript sources under `manuscripts/gauge_vfe_rg` (`_MANUSCRIPT_RELATIVE`, line 285). That layout exists only in the research vault, where the manuscript directory is `manuscripts/gauge_vfe_rg`. For this repository the corrected source root is `Theory/` itself, with `REPO_ROOT = TEX_ROOT.parent` and `_MANUSCRIPT_RELATIVE = "Theory"`; with that correction the declared command becomes `& "C:\Python314\python.exe" Theory/verification/run_checks.py` from the repository root. The correction has not been applied or run. The runner also hardcodes the pre-split chapter file names, so updating it for the three documents is a separate task (PLAN section 5.5), and until then no check of this package certifies the split documents.

### Factorization-gap stress protocol

The strata table printed in the appendix is identical, value for value, to the achieved-range table of the section "Stable factorization-gap protocol" above, which was its source; the appendix itself noted that no checked-in results record contains those ranges and that they were not regenerated. The positive-excursion witness digest, 200-digit gap, raw excursion, and outward allowance printed in the appendix also match that section. The appendix text is kept for the record:

Source: `Theory/appendix_numerical_provenance.tex:50-92` at commit `2d012d1`.

```tex
\paragraph{Factorization-gap stress protocol.}
The check \texttt{CHK-CG-FACTOR-GAP-STRESS-3138} is a deterministic
protocol.  Seed
\texttt{20260803} fixes exactly $3{,}138$ case identities: $2{,}400$ general,
$200$ exactly block diagonal, $200$ nearly decoupled, $120$ scale, $120$
permutation, $80$ nested-refinement, and $18$ 100-decimal-digit control cases.
Every stratum covers dimensions 2 through 16 and condition-number tiers
$1,10^2,\ldots,10^{14}$ as nominal pre-transform generator labels.  The
field \texttt{condition\_number} stores that nominal label, while every
digest-bound record also stores \texttt{achieved\_condition\_number}, defined
as \texttt{numpy.linalg.cond} of the regenerated matrix.  The observed global
range is $[1,1.015265553314175\times10^{14}]$, but this is only a global
coverage claim.  The achieved ranges are:
\begin{center}
\footnotesize
\begin{tabularx}{0.94\textwidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}X>{\raggedleft\arraybackslash}X@{}}
\toprule
Stratum & Minimum & Maximum \\
\midrule
Global & $1$ & $1.015265553314175\times10^{14}$ \\
General & $1$ & $1.015265553314175\times10^{14}$ \\
Exactly block diagonal & $1$ & $1.0075938532153164\times10^{14}$ \\
Nearly decoupled & $1.0000000000000002$ & $9.273791153286738\times10^8$ \\
Scale & $1$ & $1.0036120669923527\times10^{14}$ \\
Permutation & $1$ & $1.0071935024197442\times10^{14}$ \\
Nested refinement & $1$ & $1.0077056571347422\times10^{14}$ \\
100-digit controls & $1.0000000000000004$ & $1.0048132000124055\times10^{14}$ \\
\bottomrule
\end{tabularx}
\normalsize
\end{center}
The two scalar blocks in the dimension-two exactly-block-diagonal cases cannot
realize their nominal targets, and the nearly-decoupled transformation does
not attain its high nominal tiers.  Each record binds the regenerated binary64
matrix and partition by SHA-256, and repeated executions must agree exactly.
The named runtime check separately records all $3{,}138$ attempted schedule
cases, successfully evaluated 100-decimal-digit exact-binary64 references, and
completed production-reference comparisons.  PASS requires $3{,}138$ in each
category and zero failures; the $18$ designated controls remain a named stratum
rather than the sole accuracy evidence.  The achieved ranges above are taken
from \path{verification/VERIFICATION.md}; no checked-in results record
contains them, and they have not been regenerated for this copy.
\status{NUMERICAL}
```

### Binary64 fallback path and field semantics

The appendix paragraph below duplicates, in the manuscript's wording, the field semantics of the section "Stable factorization-gap protocol" above. One point is settled by the code. The aggregate `backward_error_bound` is `math.fsum` over merge steps of the per-step `backward_error` (function `factorization_gap`, lines 4114-4167 of `run_checks.py`), and each per-step value is `math.nextafter(max(cholesky_residual, solve_residual), math.inf)` or `null` (lines 3985-3990). The aggregate is therefore a sum of per-step one-ULP-up summaries, as the appendix says; the former restriction chapter used the same wording. It is not a certified perturbation or forward-error bound.

Source: `Theory/appendix_numerical_provenance.tex:94-147` at commit `2d012d1`.

```tex
The ordinary value path uses Cholesky triangular solves, canonical-correlation
singular values, and \texttt{log1p(-rho**2)}.  Near the floating-point boundary,
including a raw excursion above one, the runner compares two binary64 solve
backends, applies a $64n\epsilon_{\rm mach}$ operational rejection guard, and
uses a 200-decimal-digit evaluation of the exact stored binary64 input for the
reported gap.  The value path also falls back when
$\kappa_2(J)\epsilon_{\rm mach}\geq10^{-4}$; this is a protocol
conditioning trigger, not a proved perturbation radius.  A nonfinite binary64
condition estimate also triggers exact-input evaluation, rather than
rejection, after high-precision Cholesky certification of positive
definiteness.  On this boundary path the value of the diagnostic
\texttt{residual\_derived\_clip\_bound} is the outward-rounded discrepancy between
the maximum raw binary64 $\rho^2$ and the high-precision exact-input $\rho^2$.
It is not presented as a general residual perturbation bound.  The positive
excursion witness is a separate focused regression fixture, not an outcome of
the ordinary $3{,}138$-case schedule.  Its matrix digest is
\texttt{45310a74550d3759fed0f83f71a6cf3b0f45942499361d723a2248bbe243e2e3},
its 200-digit exact-input gap rounds to $22.777105858844084$, its raw excursion
is $4.440892098500626\times10^{-16}$, and its outward allowance is
$9.432369402326953\times10^{-16}$.  The check mechanically recomputes all four
quantities and requires PASS.  Its value comes from the exact-input fallback
rather than from clipping $\rho^2$ below one.  The
fields \texttt{clipping\_applied} and \texttt{clipping\_amount} record that a
positive cross-backend excursion was admitted and its maximum excess above
one; they do not say that this amount was substituted into the returned value.
Exact-input domain violations and raw excursions whose discrepancies exceed
the guard are rejected.  Cholesky and solve residuals remain local backward
diagnostics; the protocol does not promote them to canonical-correlation or
gap, relative-entropy, monotonicity, scale, or oracle-comparison forward-error
bounds, and no forward tolerance includes them.  Forward comparisons instead
use independent exact-binary64 high-precision references plus separately
declared endpoint-roundoff or protocol-acceptance policies.  Their
finite-health gate is $64\gamma_n$, with
$\gamma_n=n u/(1-n u)$ and binary64 unit roundoff
$u=\epsilon_{\rm mach}/2$.  Early high-precision fallbacks selected before
residual evaluation serialize the residual, tolerance, and backward-error
diagnostics as \texttt{null} because they were not evaluated.  A
residual-health fallback instead retains each finite binary64 measurement,
including finite values that exceed the health gate.  A field is
\texttt{null} only when it has no finite usable numeric value, either because
an attempted measurement is nonfinite or because a derived diagnostic requires
an unavailable constituent; finite sibling fields remain numeric.  The
evaluation method distinguishes the finite threshold case from nonfinite
Cholesky, solve, or tolerance causes and lists multiple causes in that fixed
order.  These retained measurements remain local backward diagnostics and do
not enter a forward-error tolerance.  In every branch, \texttt{null} denotes
neither failure nor zero.  The exact zero diagnostics for a one-block,
zero-step result remain numeric zero.  The \texttt{GapStep} API retains the
fieldwise residual quartet.  A \texttt{FactorizationCaseRecord} serializes only
the aggregate backward diagnostic, maximum Cholesky residual, and ordered
evaluation-method tuple, not per-step solve or tolerance values.  The
field \texttt{backward\_error\_bound} is a sum of one-ULP-up
summaries of already rounded local residual measurements; it is not a
certified perturbation or forward-error bound. \status{NUMERICAL}
```

### Freshness and scope

Source: `Theory/appendix_numerical_provenance.tex:158-168` at commit `2d012d1`.

```tex
\paragraph{Freshness and scope.}
The result artifact records interpreter and dependency versions and binds
the discovered manuscript sources and verification protocol by SHA-256.
Any source, protocol, input, dependency, or environment change requires a
new run before the numerical evidence is current.  The suite uses no GPU and
makes no GPU claim.  A missing protocol for an empirical statement remains
inconclusive even when every implemented check passes.  The inventory names
30 check identifiers, while the checked-in results record covers 29 of them,
and none of the 24 source files whose hashes it binds matches the present
sources; as stated at the start of this appendix, it is not evidence for the
current manuscript.
```

At the split the claim inventory still listed 13 entries while the manuscript carried more NUMERICAL tags, and the checked-in `current-results.json` covered 29 of the 30 check identifiers and bound none of the present sources. In the split documents a proved statement carries no NUMERICAL tag, so a regenerated inventory must follow the new numerical index tables rather than the old tags.

### Thermodynamic Fisher controls

The finite comparisons of the former section "Finite thermodynamic Fisher controls" (`sec:rg-thermo-numerical-provenance`) are test cases of `tests/rg_v2/test_thermodynamic_fisher.py`, which exercises `src/multiagent_elbo/rg_v2/thermodynamic_fisher.py`. The driver `docs/verification/2026-09-10-thermodynamic-fisher-rg/run_thermodynamic_fisher_tests.py` runs that file alone, and its retained record `docs/verification/2026-09-10-thermodynamic-fisher-rg/thermodynamic-fisher-20260910T142506078054Z.result.json` reports exit code 0, 22 test cases, no failure, error, or skip, and an unchanged source binding. That record documents one run; it was not repeated for the split. All comparisons use exact rational arithmetic with no floating-point tolerance and no random sampling. The check labels below are the test names.

| Check label | Statement corroborated | What is tested | Control | Randomness |
|---|---|---|---|---|
| `test_affine_simplex_all_c2_entries_and_singular_coordinate` | lattice-free labeled Fisher decomposition (main manuscript, coarse-channel chapter) | affine-simplex families in parameter dimensions 1, 2, 3 against independent rational Fisher formulas through derivative degree two | a null third coordinate; reordered input data | none |
| `test_rational_tie_subextensive_and_vanishing_label_controls` | finite-mixture Fisher theorem, tie and subextensive cases | two-label logistic families at tie, subextensive-score, and decreasing-weight configurations | volume parameters are finite algebraic examples, not lattice enumerations | none |
| `test_varying_label_and_branch_derivatives_include_cross_terms` | labeled Fisher decomposition with varying labels and branches | full Fisher decomposition and its differentiated weight-times-branch terms | none separate | none |
| `test_nontrivial_channel_conditional_covariance_and_both_area_scales` | fixed-channel accounting | zeroth residual-score covariance and degree-two derivative accounting for supplied areas `(4,1)` and `B=2`, with both multipliers `B^2` and `B^4` | the supplied areas do not make the channel a spatial block map | none |
| `test_coherent_geometry_and_carrier_relabeling` | relabeling invariance of the above | coherent geometry and carrier relabelings | identity of results under relabeling | none |
| `test_structural_zero_atoms_and_undefined_empty_fibers` | empty-fiber convention | an empty conditional fiber stays undefined and contributes zero after weighting | none separate | none |
| `test_native_side_two_raw_jets_partition_and_score_gram` | native raw-factor and partition jets (Supplement B lattice part) | exhaustive summation over 256 sign configurations at `(b,t)=(1/4,1/20)`, all raw-factor and physical-partition derivatives through total degree three | independent normalized-score Gram comparison at Fisher derivative degree zero | none |
| `test_native_side_one_product_fisher_is_singular` | singular product Fisher tensor at side one | two signs at `(b,t)=(1/3,1/20)`, native partition one, a null plaquette coordinate, field Fisher derivatives | none separate | none |
| `test_positive_varying_posterior_factor_compatibility_and_induced_push` | selected-posterior derivatives (Supplement B lattice part) | two side-one branches with global factor normalization, posterior derivatives against an independent two-coordinate Taylor-quotient calculation through total degree three, and the induced pushed posterior and evidence derivatives | the native partition is identically one, so a hierarchical posterior with a nonconstant native divisor is not exercised | none |

The numerical index of Supplement B (`tab:base-numerical`) does not print test names, which are code identifiers. Its three lattice rows carry these check labels: `CHK-RG-THERMO-NATIVE-JETS` is `test_native_side_two_raw_jets_partition_and_score_gram`, `CHK-RG-THERMO-SINGULAR-FISHER` is `test_native_side_one_product_fisher_is_singular`, and `CHK-RG-THERMO-POSTERIOR-PUSH` is `test_positive_varying_posterior_factor_compatibility_and_induced_push`.

The table has nine named tests; the record counts 22 cases because several tests are parameterized, and `test_legitimate_domain_boundaries` covers input validation rather than a manuscript statement. The former section, with the review-stage wording already removed in Phase 1, read:

Source: `Theory/appendix_numerical_provenance.tex:170-250` at commit `2d012d1`.

```tex
\section{Finite thermodynamic Fisher controls}
\label{sec:rg-thermo-numerical-provenance}

The following finite computational comparisons concern the retained-label
experiments of \Cref{sec:rg-thermo-finite-experiment}. Each is a test case
of \path{tests/rg_v2/test_thermodynamic_fisher.py}, which exercises
\path{src/multiagent_elbo/rg_v2/thermodynamic_fisher.py}. The driver
\path{docs/verification/2026-09-10-thermodynamic-fisher-rg/run_thermodynamic_fisher_tests.py}
runs that test file alone, and its retained record
\path{thermodynamic-fisher-20260910T142506078054Z.result.json}, in the same
directory, reports 22 passing test cases with no failure, error, or skip. That
record documents one run; it was not repeated for this appendix. The
comparisons used exact rational arithmetic, without a floating-point
acceptance tolerance or random sampling; no random seed was used.
Affine-simplex controls in parameter dimensions one, two, and three
(\path{test_affine_simplex_all_c2_entries_and_singular_coordinate}) matched
their independent rational Fisher formulas through derivative degree two,
including a null third coordinate and reordered input data. Two-label
logistic controls
(\path{test_rational_tie_subextensive_and_vanishing_label_controls}) matched
the corresponding rational Fisher derivatives at declared tie,
subextensive-score, and decreasing-weight configurations. Their volume
parameters specify finite algebraic examples rather than enumerations of
larger spatial lattices. These are numerical observations, not proofs of
arbitrary-dimensional or thermodynamic claims. \status{NUMERICAL}

The varying-label and varying-branch comparison
(\path{test_varying_label_and_branch_derivatives_include_cross_terms})
matched the full Fisher decomposition and its differentiated
weight-times-branch terms. A fixed stochastic-channel control
(\path{test_nontrivial_channel_conditional_covariance_and_both_area_scales})
matched the zeroth residual-score covariance
and the degree-two derivative accounting for supplied areas
$(V_{\rm fine},V_{\rm coarse})=(4,1)$ and $B=2$, including both
multipliers $B^2$ and $B^4$. The supplied areas do not identify that
channel as a spatial block map. Coherent geometry and carrier
relabelings preserved the results
(\path{test_coherent_geometry_and_carrier_relabeling}). An empty conditional
fiber remained undefined and contributed zero after weighting
(\path{test_structural_zero_atoms_and_undefined_empty_fibers}). These numerical
comparisons retain their fixed-support and fixed-channel scope.
\status{NUMERICAL}

For the native side-two square at $(b,t)=(1/4,1/20)$
(\path{test_native_side_two_raw_jets_partition_and_score_gram}), exhaustive
summation over all 256 configurations of eight signs matched every raw-factor
and physical-partition derivative through total degree three. There is one
internal plaquette. The independent normalized-score Gram comparison was
at Fisher derivative degree zero. At side one with
$(b,t)=(1/3,1/20)$ (\path{test_native_side_one_product_fisher_is_singular}),
the comparison used two signs, native partition one,
a null plaquette coordinate, and the stated field Fisher derivatives.
These finite numerical observations do not supply derivative-convergence
estimates as the square grows. \status{NUMERICAL}

A separate selected-posterior comparison
(\path{test_positive_varying_posterior_factor_compatibility_and_induced_push})
used two side-one branches with
global factor normalization, a fixed reference, varying raw masses,
geometry weight and physical scalar, and a binary sensor on one edge.
Its mean was $\eta_\gamma=k_\gamma b$, with
$k_\gamma\in\{1/2,1/3\}$. The posterior derivatives matched an independent
two-coordinate Taylor-quotient calculation through total degree three;
the induced pushed posterior and evidence derivatives also agreed.
The physical scalar varied, but the underlying native partition was
identically one. This numerical comparison therefore does not exercise a
hierarchical posterior with a nonconstant native partition divisor.
\status{NUMERICAL}

These retained finite comparisons contain no independently evaluated
all-edge source-shift derivative, multistage information telescope,
prescribed curvature-action derivative, or recognition-to-posterior
conditional-KL VFE comparison. Their scientific scope is the finite
comparisons stated above; they supply no computational proof of native
thermodynamic response, limiting label weights, regular-chart inverses,
curvature limits, or physical identification. The mathematical conclusions
rest on the proofs in
\Cref{ch:thermodynamic-fisher-draft,app:thermodynamic-fisher-draft-proofs}
under their stated hypotheses.
No new calculation is asserted by recording these numerical observations
here. \status{NUMERICAL}
```
