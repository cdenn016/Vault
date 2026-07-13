# Belief-Inertia Theorem-First Revision: Final Verification

Date: 2026-07-13
Branch: `codex/belief-inertia-ultradeep-review-20260712`
Scope: the complete theorem-first revision prepared from 2026-07-12 through 2026-07-13
Initial review record: `docs/reviews/2026-07-12-belief-inertia-ultradeep-peer-review.md`

## Result and publication verdict

The revision passes its mathematical, documentary, bibliographic, and repository acceptance gates. The gauge-covariant VFE objective and four-part stiffness decomposition now organize the manuscript; Fisher--Rao flow is primary; the second-order kinetic model is explicitly postulated; the `M=H_F` spectral degeneracy is disclosed; and every social-model comparison is restricted to the regime actually derived. The initial review's theoretical blockers have therefore been resolved in the revised branch.

The revised work is suitable for author-led submission preparation as a specialized theory/model paper. This is not a claim of empirical validation or venue acceptance. It still needs ordinary authorial editing, journal formatting, and an eventual empirical program if the author wants psychological or sociological construct-validity claims stronger than the present conditional predictions.

No new data were created, analyzed, or claimed in this revision.

## Branch and revision range

The verification was performed in the isolated worktree `C:\tmp\Research-belief-inertia-review-20260712`; the live Research checkout was not modified. At the start of final verification:

```text
branch:      codex/belief-inertia-ultradeep-review-20260712
origin/main: 4d9633993f05c89f8944431dbb5f4f9b49940981
merge base:  5acb73ef2818214ca5bbac00ed78c42be73d5d80
ahead/behind relative to origin/main: 18 / 2 before this final verification commit
```

The branch-only sequence before the final commit was:

```text
a6935be docs: design belief-inertia theorem-first revision
1882626 docs: plan belief-inertia theorem-first revision
5d3e289 fix: make research vault lint root explicit
5533b27 docs: add belief-inertia comparator literature
8759076 docs: clarify oscillatory-opinion source provenance
8c15742 docs: refocus belief inertia around gauge VFE
1234a0d docs: establish canonical gauge VFE objective
1366f67 docs: reconcile belief-inertia notation and transport
61dc102 docs: prove four-part relational stiffness
380157e docs: correct stacked covariance gauge Jacobian
40ebfc8 docs: separate belief kinetics from VFE stiffness
ed72bb9 docs: correct modal normalization and momentum notation
2eefd48 docs: restrict social dynamics claims to proved regimes
dfcdb04 docs: tighten social metastability and reversible-flow scope
8ba7d09 docs: complete theorem-first belief-inertia manuscript
f5b0bff test: verify belief-inertia derivations symbolically
0a762c1 docs: reconcile belief inertia across research wiki
ac3097a docs: align collective inference project tags
```

`origin/main` advanced by two commits after this branch was created. All three-dot comparisons in this report therefore use the recorded merge base; no rebase, merge, push, or live-checkout mutation was performed.

## Exact changed-file set

The final `origin/main...HEAD` change set consists of the following files, including this report and the retained peer-review record:

```text
docs/_lint.py
docs/reviews/2026-07-12-belief-inertia-symbolic-checks.py
docs/reviews/2026-07-12-belief-inertia-ultradeep-peer-review.md
docs/reviews/2026-07-12-belief-inertia-revision-verification.md
docs/superpowers/plans/2026-07-12-belief-inertia-theorem-first-reorientation.md
docs/superpowers/specs/2026-07-12-belief-inertia-theorem-first-reorientation-design.md
index.md
log.md
manuscripts/belief_inertia.tex
manuscripts/references.bib
manuscripts/verified-ledger.md
sources/manuscripts/belief-inertia-2026-07-12-theorem-first-revision.md
sources/papers/bass-1969-product-growth.md
sources/papers/baumann-sokolov-tyloo-2020-second-order-consensus.md
sources/papers/chirco-2022-statistical-bundle-dynamics.md
sources/papers/girolami-calderhead-2011-riemann-hmc.md
sources/papers/leok-zhang-2017-information-geometric-mechanics.md
sources/papers/martins-2015-opinion-particles.md
sources/papers/nevin-mandell-atak-1983-behavioral-momentum.md
sources/papers/pistone-2018-statistical-bundle-lagrangian.md
sources/papers/sampson-porter-restrepo-2025-oscillatory-opinion.md
sources/papers/xue-hirche-cao-2020-opinion-port-hamiltonian.md
wiki/concepts/Belief inertia.md
wiki/concepts/Belief perseverance and confirmation bias.md
wiki/concepts/Collective active inference.md
wiki/concepts/Echo chambers and polarization.md
wiki/concepts/Hamiltonian belief dynamics.md
wiki/concepts/Mass as Fisher information.md
wiki/concepts/Multi-agent variational free energy.md
wiki/concepts/Sociophysics.md
wiki/projects/Gauge-Theoretic Multi-Agent VFE Model.md
wiki/projects/SocialPhysics.md
wiki/themes/Statistical physics of social systems and collective behavior.md
```

## Static and citation checks

The final static checks passed:

```text
git diff --check                         exit 0
git diff --check origin/main...HEAD      exit 0
changed-scope editor-marker files        0
introduced British-English prose hits    0
```

The broad language scan prescribed by the plan also finds American variants such as `behavior`, `modeling`, and `fiber`, LaTeX `\centering`, and the immutable canonical wikilink target `Agents as fibre-bundle sections`; these are classified nonfailures. No British spelling was introduced in changed prose.

The manuscript citation scan produced:

```text
citation commands:       33
citation-key uses:       51
unique cited keys:       21
BibTeX entries:          405
missing cited keys:       0
duplicate BibTeX keys:    0
```

The existing Hegselmann--Krause record was corrected from `@incollection`/`booktitle` to `@article`/`journal` while preserving its key, title, authors, volume, number, and year. The clean BibTeX run accepted the corrected record without warning.

## Clean LaTeX and BibTeX build

The final authoritative build used an empty auxiliary directory outside the worktree:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=C:\tmp\belief-inertia-build-20260712 belief_inertia.tex
# exit 0

Set-Location C:\tmp\belief-inertia-build-20260712
$env:BIBINPUTS='C:\tmp\Research-belief-inertia-review-20260712\manuscripts;'
bibtex belief_inertia
# exit 0

Set-Location C:\tmp\Research-belief-inertia-review-20260712\manuscripts
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=C:\tmp\belief-inertia-build-20260712 belief_inertia.tex
# exit 0
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=C:\tmp\belief-inertia-build-20260712 belief_inertia.tex
# exit 0
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=C:\tmp\belief-inertia-build-20260712 belief_inertia.tex
# exit 0
```

The plan's literal `bibtex "C:\tmp\belief-inertia-build-20260712\belief_inertia"` form was separately attempted during build diagnosis and exited `1` because TeX Live's `openout_any=p` policy refused to create an absolute-path `.blg`. Running BibTeX from inside the same clean build directory with `BIBINPUTS` pointing to the manuscript directory is the proportional, output-equivalent invocation; it exited `0` and is the authoritative result above.

Final artifact and log scan:

```text
PDF pages:                                      37
LaTeX warning lines:                             0
natbib warning lines:                            0
BibTeX warnings or errors:                       0
overfull hboxes:                                 0
forbidden unresolved/error diagnostics:          0
underfull hboxes:                                18
```

Six material overfull boxes in the review build were eliminated with a document-level `\emergencystretch` of `2em`; the table float specifier was broadened from `[h]` to `[ht]`, eliminating the final LaTeX float warning. The remaining underfull diagnostics are nonblocking layout notices: sixteen arise in deliberately narrow comparison-table cells, and two are low-badness prose diagnostics (1077 and 1005) in the classical-opinion-dynamics paragraph. No mathematical or social claim was changed to suppress them.

## Symbolic and vault checks

Fresh final commands and results:

```text
python docs/reviews/2026-07-12-belief-inertia-symbolic-checks.py
belief-inertia symbolic checks: PASS
exit 0

python docs/_lint.py --root .
files: 981
BROKEN wikilinks: 0
GRAPH grey nodes: 0
EMPTY files: 0
CASE collisions: 0
IDENTITY collisions: 0
exit 0
```

## Primary-source and DOI verification

Task 2 queried all ten version-of-record DOI endpoints live through DOI content negotiation and queried every applicable arXiv API record. Final verification rechecked all ten immutable notes for exact parity among YAML `doi`, canonical `https://doi.org/<doi>` URL, and embedded BibTeX DOI; all ten passed:

| Comparator | Version-of-record URL | Applicable arXiv record |
|---|---|---|
| Martins | https://doi.org/10.1016/j.physleta.2014.11.021 | https://arxiv.org/abs/1307.3304 |
| Chirco--Malagò--Pistone | https://doi.org/10.1142/S0219887822502140 | https://arxiv.org/abs/2009.09431 |
| Girolami--Calderhead | https://doi.org/10.1111/j.1467-9868.2010.00765.x | not canonical; current arXiv:0907.1100 v3 is withdrawn and has different title/authorship |
| Leok--Zhang | https://doi.org/10.3390/e19100518 | none |
| Pistone | https://doi.org/10.3390/e20020139 | none |
| Nevin--Mandell--Atak | https://doi.org/10.1901/jeab.1983.39-49 | none |
| Xue--Hirche--Cao | https://doi.org/10.1109/TNSE.2019.2894565 | none |
| Baumann--Sokolov--Tyloo | https://doi.org/10.1103/PhysRevE.102.052313 | https://arxiv.org/abs/2008.08163 |
| Bass | https://doi.org/10.1287/mnsc.15.5.215 | none |
| Sampson--Restrepo--Porter | https://doi.org/10.1103/PhysRevE.112.024303 | https://arxiv.org/abs/2408.13336 |

The Sampson journal/DOI and arXiv metadata order is Sampson--Restrepo--Porter. The current rendered arXiv v2 manuscript byline orders Sampson--Porter--Restrepo; the source note records this discrepancy and follows the published version of record.

## Manuscript-versus-wiki contradiction audit

The abstract, conclusion, epistemic-status table, relevant ledger supersession, immutable revision note, and all touched synthesis pages were checked family by family. Statuses agree:

| Claim family | Final status |
|---|---|
| Gauge/VFE objective | Engineered gauge-covariant consensus energy; rowwise source-mixture interpretation requires the stated source-independence assumption. |
| Primary dynamics | Fisher--Rao natural-gradient flow is primary. Second-order dynamics require a separate positive kinetic metric. |
| Fisher, Hessian, kinetic tensor | Intrinsic Fisher metric `G`, loss Hessian/local stiffness `H_F`, and kinetic metric `M` are distinct objects. |
| `M=H_F` | When the same Hessian supplies mass and restoring stiffness, the generalized spectrum is `omega^2=1` up to scale; nontrivial modal claims require independent identification. |
| Four-part stiffness | Local mean stiffness separates into prior, sensory, incoming relational, and outgoing relational/recoil terms. |
| Canonical attention | The entropy-retaining optimized row has reduced value `-tau log Z` and an envelope gradient. |
| Surrogate attention | The entropy-suppressed expected-energy surrogate is a different objective and retains a covariance response. |
| Adaptive precision | The full optimized envelope coefficient `c0/(b0+D)` differs from the derivative `b0 c0/(b0+D)^2` of the bare optimized product. |
| Asymmetric fixed attention | The scalar energy remains conservative when both sender and receiver derivatives are retained; detached one-sided updates are a truncation. |
| Polarization | Positive finite-temperature attractive coupling gives metastable separation only in the stated unanchored, symmetric reciprocal two-cluster reduction, not exact stable polarization. |
| DeGroot | Derived only for a fixed symmetric or reversible continuous-time subclass, not general directed row-stochastic influence. |
| Friedkin--Johnsen | Restricted anchored equilibrium; heterogeneous susceptibility needs agent-indexed anchor precision or coupling. |
| Diffusion | Not derived. Bass diffusion requires an explicit adoption state and hazard and remains future work. |
| Confirmation bias | Only a kernel-conditional selective-exposure mechanism is supported; passive attractive weighting is not active confirmation-biased sampling. |
| Belief perseverance | Revision latency and conditional kinetic coasting are candidate mechanisms; explanatory perseverance requires a slow explanatory state. |
| Leadership/recoil | Outgoing curvature is contemporaneous sender-role stiffness, not accumulated memory or inevitable rigidity. |
| Social Impact Theory | Interpretive comparison only; normalized attention does not reproduce Latané's number law. |

The ledger retains historical entries `[bi-pass16]` and `[bi-alpha-pass]` and explicitly supersedes them with the dated theorem-first revision rather than deleting provenance.

## Protected files and immutable provenance

Both protected comparisons against `origin/main` exited `0`:

```text
git diff --quiet origin/main -- manuscripts/PIFB2.tex                         exit 0
git diff --quiet origin/main -- sources/manuscripts/belief-inertia.md         exit 0
```

Final SHA-256 values match the Task 1 baselines exactly:

```text
manuscripts/PIFB2.tex
50F382C51BFAC8B8841A4FE6AFF2887CE05D3D47DD905C6D20A91A688152D81B

sources/manuscripts/belief-inertia.md
ADD9AA3AE8497AE9DB28FB66B07F55C56DBB80F8601726160BDBE0DC5DCB5E92
```

Additional final verification hashes before the completion commit:

```text
manuscripts/belief_inertia.tex
5C31D0A6F4D088E11783B708E8CDF658A2F6956836E303AB5A67C8CE5A9F1639

manuscripts/references.bib
01491289DB2DBB426F5EC156C9D123F568F415E04378FDB626E721F6654F3E62

docs/reviews/2026-07-12-belief-inertia-ultradeep-peer-review.md
2D5D5694A08DA334DF89E44C9AEC5DD1B935ED386D097FE2CF31176C81D5F1DE

docs/reviews/2026-07-12-belief-inertia-symbolic-checks.py
258951A75AF7B2F59A6D13A862A1A499040F1622DA8E512E1BAFD09CA08C46F6
```

## Known limitations retained after revision

1. The principal closed-form results are local Gaussian, affine-transport, frozen-attention or local-consensus statements. They are not global convergence theorems for arbitrary nonlinear, directed, or time-varying populations.
2. The kinetic metric remains a modeling postulate. Its empirical identification must be separated from Fisher geometry, restoring stiffness, and damping.
3. Exact long-lived polarization requires mechanisms beyond the proved positive finite-temperature attractive reduction, such as anchors, repulsion, support truncation, or active candidate selection.
4. Psychological constructs require explicit measurement models. Selective exposure, revision latency, and a slow explanatory state must not be conflated.
5. Oscillation alone cannot identify belief inertia because time-varying coupling, network resonance, and group-opinion feedback supply alternative mechanisms.
6. DeGroot, Friedkin--Johnsen, bounded-confidence, Social Impact, and Bass comparisons retain their stated restricted or interpretive status.
7. The ten comparator notes are immutable evidence records; the Girolami withdrawn-preprint issue and Sampson byline discrepancy remain explicitly documented rather than silently normalized away.

## Completion statement

All acceptance gates in the approved theorem-first implementation plan are satisfied. The branch is ready for author review without integration. No push, merge, rebase, or mutation of the live Research checkout was performed.
