# Live-vault WIP reconciliation

- Date: 2026-08-01
- Common ancestor: `f568b7b18973268fc1febafd3805f3cce64f933d`
- Preserved live WIP: `670f433d00eed79c012bb49783729ec5e61e39c4`
- Reviewed manuscript: `96b7b5f6467b39b7ba5dae4d1adf4aadda99d193`

## Decision

The five overlapping source edits and the old compiled PDF were reconciled, not discarded. No
source hunk from the preserved live WIP should be replayed onto the reviewed manuscript. The sound
intent of those edits--general theory before the Gaussian realization, explicit operator-versus-law
typing, holonomy-aware coarse-graining, and concise presentation--is already present in the reviewed
manuscript in a more general and more carefully qualified form. The remaining live-WIP differences
either reverse later mathematical corrections, delete required source records, or restore an older
compiled artifact.

The preserved WIP remains recoverable on the local-only branch
`codex/local-gauge-vfe-wip-safety-20260801`; this report records why its overlapping changes are not
reapplied.

## Three-way result

A three-way merge using `f568b7b` as the base produced content conflicts in all four edited prose
files and an add/add conflict in `main.pdf`. The bibliography deletions applied automatically, which
is precisely why an automatic merge was unsafe: one deleted entry is cited twice by the reviewed
manuscript. Every conflict was therefore adjudicated semantically against the proofs, claim-status
ledger, compiled references, and general-before-Gaussian structure rather than resolved by a blanket
Git strategy.

| Live-WIP path | Reconciliation | Reason |
|---|---|---|
| `05a_expfamily.tex` | Keep reviewed version | The WIP collapses the ambient theory back to one regular exponential family and deletes the law/kernel, dominated/non-dominated, smooth, stratified, and infinite-dimensional type hierarchy. Its useful operator/probability-layer idea survives in the reviewed exponential-family subclass, while the ambient law-fiber theory is retained. The WIP also introduces an incorrect factor in the Gaussian moment pair and weakens the domination argument used to justify differentiation. |
| `09_coarsegraining.tex` | Keep reviewed version | The WIP recombines general and Gaussian material and restores the overstrong rule "coarsenable iff trivial holonomy." The reviewed split places law-level coarse channels, recovery, holonomy-fixed KL distortion, and cross-morphism compatibility in `06_general_coarsegraining.tex`, then gives fixed-section, effective-support, sheaf, and Gaussian formulas in `09_coarsegraining.tex`. It correctly retains partial sectors and weight-null exceptions and distinguishes structural admissibility from current belief agreement. |
| `10_renormalization.tex` | Keep reviewed version | The WIP treats aggregation too quickly as a flow, makes nonflat failure more absolute than the proved weighted-support result, and blends general RG with the Gaussian operator realization. The reviewed split puts typed kernels, BKS Fisher ordering, Laplacian/network RG comparisons, and the general RG arrow in `07_general_renormalization.tex`; `10_renormalization.tex` is explicitly the multivariate-Gaussian operator realization. |
| `SPEC.md` | Keep reviewed version | The WIP removes the regular-pencil qualification, the exact Kron counterexample, the effective-support exceptions, and several open-obligation qualifiers. It also restores the unsupported claims that internal variation must be exhausted by one spectral exponent, that connected agents have no observable variation, and that a flat base leaves no detectable trace. The reviewed specification rejects those overclaims and keeps graph holonomy, base-connection holonomy, and principal-bundle topology distinct. |
| `references.bib` | Keep reviewed version | The WIP deletes `AyJostLeSchwachhoefer2018` and `PistoneSempi1995`. The former is cited in both `05a_expfamily.tex` and `06_general_coarsegraining.tex`, so replaying the deletion breaks the represented source record. The latter belongs to the shared vault bibliography; deleting an unused shared entry does not shorten the rendered paper and risks unrelated manuscript drift. |
| `main.pdf` | Keep reviewed version | The WIP PDF is a 1,538,624-byte older build. The reviewed PDF is the 1,101,044-byte, 162-page production artifact verified with no unresolved references, citations, placeholders, or layout warnings. |

## Sound intent that is already incorporated

The reconciliation found no lost independent theorem, derivation, citation, or structural edit. The
live draft's valid aims are represented as follows:

- the ambient belief and model law fibers, generative kernels, and selected smooth tiers are typed
  before any exponential-family coordinates;
- one principal bundle supports two associated statistical bundles, potentially using inequivalent
  representations, separate induced connections, and the cross maps
  `\Phi:\mathcal E_b\to\mathcal E_m` and
  `\widetilde\Phi:\mathcal E_m\to\mathcal E_b`;
- general coarse channels, data processing, recovery/sufficiency, transported KL distortion, and
  holonomy-fixed parent laws precede the Gaussian realization;
- represented holonomy determines the available parallel sector, transported KL measures present
  marginal-law coherence, and a separate free-energy/MDL/rate rule licenses a nontrivial scale;
- Bayesian renormalization, Laplacian RG, network RG, and graph learning are compared as typed
  neighboring constructions rather than silently identified with this theory; and
- the multivariate-Gaussian material follows the general coarse-graining and general RG chapters.

## Immutable artifact identities

| Path | Preserved-WIP blob | Reviewed blob |
|---|---|---|
| `05a_expfamily.tex` | `43b44b136920bf527f52c3b6f7918e882d81c343` | `d6f83a247cd8a39bfe4a524a90d7956a5035a41b` |
| `09_coarsegraining.tex` | `2560bbaad24aec0fbb1a241789ffa4807e8f2905` | `014068d28d06b7080868e51bbc9914031d2592a9` |
| `10_renormalization.tex` | `d4b51578a40d6bd2d7a8f3bbf89a928dbf99ff3f` | `7b49fafffd4f9f0e2321f4d6415561ef8603aa42` |
| `SPEC.md` | `6e09c6af4db15160766be6f06fb04178d2bee9b4` | `2851ed972c123c3f004b6c0c4aff00746f2781a7` |
| `references.bib` | `bd4f6a12e9d8949d11e8dc58a9b904ac7f8f358b` | `ca9ec62f0b2f6cfa081ca8ec1809500e6ddc451c` |
| `main.pdf` | `574c1dea5ce01bbd7befc637d9833ea9983019fa` | `f97f01a1706765a6727404749f4ed7f9577964eb` |

## Result

The reconciled source tree is the reviewed tree, with no silent replay of the contradictory draft.
The safety commit remains the exact recovery point for the original live edits. This is a semantic
merge decision: it preserves the user's work as history while keeping the live manuscript on the
proof-checked theory.

Two independent read-only comparisons reached the same result. One classified every WIP span as
either already incorporated or conflicting/obsolete. The second rechecked the Git objects, citation
delta, chapter order, bundle terminology, blob identities, and the WIP's changed Gaussian moment
factor; it found no missing sound hunk and no overstatement in this report.
