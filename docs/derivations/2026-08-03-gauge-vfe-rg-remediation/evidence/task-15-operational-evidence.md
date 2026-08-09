<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 15 lean operational-evidence replay

## Scope, revision binding, and method

This memo replays only the six remaining operational claims from the existing
Task 13 and Task 14 records. It does not rerun tests or build the manuscript.
It performs read-only parsing, path/revision checks, and SHA-256 checks against
the durable artifacts. The scope is ordinary personal-research
reproducibility.

The replay checkout was at
`14551bb8d463f229a3b451d7222042d134c2c52d`. Task 13 is bound to source
revision `4ed9ddf6bbb0cc7870118a6aa51710e9bbc2c0ae`, tree
`07ca0745bc74d96102aa070dc1c04d67be2d19ab`. Task 14 is bound to source
revision `28f66d63aff177d6ff9326796a485dff7afc8b8d`, tree
`d348f023ddacf1b43cd7f3ee959ea0ba320f5e7d`. Both revisions are ancestors of
the replay checkout, and `git diff 28f66d6..HEAD -- manuscripts/gauge_vfe_rg`
is empty. Thus the Task 14 manuscript source is also the manuscript source at
the replay checkout.

For tracked text artifacts, the identities below are SHA-256 over the committed
Git-object bytes (LF). For the XML, ZIP, PDF, and one-line numerical result,
they are SHA-256 over the raw durable bytes. Windows CRLF materialization can
give a different working-tree hash for multiline text without changing its Git
object; the Task 14 pullback ledger records both forms for the prior derivation.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `evidence/task-13-tests.xml` | 80,010 | `63870af5c4ba52e90a15b1978958acdecb02098130943909cc2839a3475cc609` |
| `evidence/task-13-manifest-verification.json` | 3,639 | `0ea14d2e872c22459c83f496146b9a79f4cb372c72e5a748ec351230fd36dbe4` |
| `manuscripts/gauge_vfe_rg/verification/current-results.json` | 69,785 | `30bf14ebf03348ed3092ee2715fc7f23741c1c615f028049ff52a4cfd41b8058` |
| `evidence/task-13-pullback-validation.md` | 11,710 | `32eff6669c5223cfea72089c0f143fe4aaa506b249ce0abf5f4114bc83c65c58` |
| `evidence/task-13-pullback-geometry-ledger.json` | 5,057 | `79ce0a4a70944f4e509daaad12653c673009ede867990f776b3fea06a10a5cce` |
| `evidence/task-14-build-audit.json` | 7,329 | `e7376eba240444a35b33e6182373cd5d7de8bf637bea039f505d7d76f0ed1e4d` |
| `evidence/task-14-visual-audit.json` | 5,236 | `75ce1c4d66575e7d923c22c4052692bd961cd14b79cd174d0edcd75a4822adb8` |
| `evidence/task-14-pullback-geometry-ledger.json` | 7,035 | `54d58f9c61b0b2bbe5d4d7a9d641062a35a8832ce95cb46b3f24faa091697b18` |
| `evidence/task-14-render-manifest.csv` | 11,441 | `255a316d1c8031be180abfd0959376a1e7ddc57ac44772b7b2ba5b4a2e0b9641` |
| `evidence/task-14-build-logs.zip` | 15,634 | `2d5980c115f784c638027e220fb94f85d8d0ad44aedd6adc2bb400b9e5840241` |
| `evidence/task-14-main.pdf` | 1,847,095 | `fc4f111131ef39bf18762784f1ce80336304415db0adddc6b41744e3544ffd3d` |

All `evidence/...` paths above are relative to
`docs/derivations/2026-08-03-gauge-vfe-rg-remediation/`.

## Machine-readable replay observations

The Task 13 JUnit XML parses to 420 tests, zero failures, zero errors, and zero
skips. Its factorization-gap class contains 33 passing cases. The ordinary
manifest subset includes 23 per-bound-file mutation cases, 13 malformed or
incomplete tree/result cases, six result-corruption/nonmutation cases, the
update-then-verify byte-preservation case, and four UTC timestamp-validation
cases, with no failure or error node.

The numerical result parses as `overall_status: PASS` and records UTC time
`2026-08-08T23:27:27Z`, source revision `4ed9ddf6...`, `source_dirty: false`,
semantic payload digest
`c98fc5f856a83df34f776f640d6897695779d279e1ba8569f3423f031552ce04`,
44 bound input paths, and 31 ordered checks. The Task 13 summary independently
records the same result hash and digest.

The determinant-gap record reports seed `20260803`, 3,138 scheduled cases,
3,138 independent 100-digit exact-input references, zero oracle or protocol
failures, condition numbers reaching approximately `1.0153e14`, 18 named
high-precision controls, 684 high-precision fallbacks, 23 boundary fallbacks,
and zero clipping cases in the frozen schedule. The source path bound by the
manifest uses Cholesky triangular solves and canonical-correlation singular
values (`run_checks.py:3720-3776`), `log1p(-rho^2)` with a positive-domain guard
(`run_checks.py:3959-3967`), and an explicit sum of two-block increments along
the declared merge order (`run_checks.py:3994-4056`). The separate focused
boundary witness reports its diagnostic clipping explicitly; it is not
silently counted as an ordinary schedule case.

The Task 13 and Task 14 pullback ledgers contain five distinct manuscript paths
each. Direct `git cat-file` checks find all five at each ledger's bound
revision. The Task 14 ledger preserves PB-1 through PB-3 and closes PB-4 with
the current build and visual records; all four PB states are
`EVIDENCE_VERIFIED` and their open-obligation arrays are empty.

The Task 14 build record reports a fresh external output directory, four
successful TeX/BibTeX passes, 300 pages, zero unresolved references or
citations, zero fatal errors, and a complete generated-auxiliary inventory.
The ZIP independently contains the recorded `main.log` (61,310 bytes) and
`main.blg` (923 bytes). Git ignores the ordinary TeX auxiliary extensions. A
historical tracked `manuscripts/gauge_vfe_rg/main.pdf` exists, but its SHA-256
is `83b1d9b92f1cbbd9385e0b965448cefdf561021f8ee72763bf4be7fc0fac01de`,
not the release PDF hash, and no Task 14 record cites it as evidence.

The PDF metadata record contains `timeless inference histories` and does not
contain `emergent time`. This agrees with `main.tex:21`, with the explicit
refusal to identify information duration or RG depth with physical time in
`01_introduction.tex:117`, `05d_relational_inference.tex:17,1555-1622`, and
`12_philosophy.tex:58`. The status macro is globally wrapped in `\mbox` at
`main.tex:104`, and the visual record reports 847 source status tokens, zero
rendered wrapping defects, and zero clipping defects in its audited scope.

## Claim dispositions

### `pullback-ledger-provenance`

**State: `EVIDENCE_VERIFIED`.** The two recorded source trees match Git, every
cited manuscript path exists at the relevant bound revision, the Task 14
ledger explicitly preserves the Task 13 derivation identity, and PB-1 through
PB-4 are closed at the unchanged Task 14 manuscript source.

**Falsifier.** A bound tree mismatch, a cited path absent at its bound revision,
an incorrect recorded artifact hash, a nonempty PB obligation, or a manuscript
change after `28f66d6` that invalidates the stated applicability would refute
this closure.

### `determinant-gap-stability`

**State: `EVIDENCE_VERIFIED` as a numerical observation, not a proof over all
positive-definite matrices.** The implementation mechanism and the declared
finite stress schedule are both evidenced, and the current machine-readable
result contains no failed case.

**Falsifier.** A regenerated declared case outside its stated reference
acceptance, a negative gap beyond the documented rounding allowance, a silent
clip, a schedule/count/digest mismatch, or a failure/error in the bound check
would refute this finite numerical claim.

### `manifest-fail-closed`

**State: `EVIDENCE_VERIFIED`.** The result binds raw bytes for 44 declared
inputs, UTC time, source revision, and semantic digest. The machine-readable
JUnit evidence exercises ordinary missing, extra, malformed, mutated,
revision-mismatched, nonfinite, and result-nonmutation controls, including a
passing compare-without-rewrite case.

**Falsifier.** A declared mutation or malformed/missing/extra input that
verifies successfully, a verified result with a wrong source revision or
semantic digest, or a verify invocation that changes the bound result bytes
would refute this operational claim.

### `minor-emergent-time-keyword`

**State: `EVIDENCE_VERIFIED`.** The released metadata omits `emergent time`,
uses `timeless inference histories`, and is consistent with the manuscript's
explicit non-identification of Fisher duration, RG depth, and physical time.

**Falsifier.** A released metadata keyword asserting emergent physical time, or
a metadata/source contradiction on this point, would refute the claim.

### `minor-status-unbreakable`

**State: `EVIDENCE_VERIFIED`.** Every status invocation passes through the
single `\status` macro whose `\mbox` prevents internal line breaking; the
current visual record additionally reports no status wrapping or clipping
defect.

**Falsifier.** A status path bypassing the unbreakable macro or any status token
split or clipped in the released PDF would refute the claim.

### `minor-generated-aux`

**State: `EVIDENCE_VERIFIED`.** The current release record names an external
fresh output directory, inventories the generated files from the successful
four-pass build, and cites only the separately preserved Task 14 PDF and logs.
The older tracked manuscript PDF is distinguishable by path and hash and is not
treated as current evidence.

**Falsifier.** A stale auxiliary influencing the recorded build, an inventory
hash mismatch, a missing required build product, or a release record citing the
older tracked PDF as the Task 14 artifact would refute the claim.

## Frozen verdict

**PASS.** All six operational claims are `EVIDENCE_VERIFIED` at their recorded
artifact revisions and scopes. No defect was found. The numerical and visual
statements remain bounded by their finite protocols; this memo does not convert
them into universal mathematical proofs and does not refresh them beyond the
recorded source, inputs, and environment.
