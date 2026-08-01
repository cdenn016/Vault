# Gauge–VFE–RG Ultradeep Review, Revision, and Final Reconciliation

**Date:** 2026-07-29; common-principal-bundle correction 2026-08-01
**Working branch:** `codex/gauge-vfe-rg-ultradeep-20260729`
**Baseline:** `origin/main` at `f568b7b`
**Reviewed artifact:** `manuscripts/gauge_vfe_rg/main.pdf`
**Disposition:** the finite mathematical core is internally typed, the cited
source relationships are bounded to what those sources establish, and the
remaining research problems are explicit. No medium-or-higher issue survived
the final integrated referee pass.

## Executive summary for a physicist

The theory now has a simple order.

1. One principal \(G\)-bundle lies over the base manifold. It induces belief
   and model probability laws as **different associated bundles**, possibly
   through inequivalent representations. They can use different local
   principal frames and different connections.
2. The maps
   \[
   \Phi:\mathcal E_b\to\mathcal E_m,\qquad
   \widetilde\Phi:\mathcal E_m\to\mathcal E_b
   \]
   compare the two families over the same base point. They need not be
   inverses, linear, or isomorphisms.
3. Each family has its own connection. Hence transport along a base path
   \(\gamma\) is described by \(\Omega_\gamma\) for beliefs and
   \(\widetilde\Omega_\gamma\) for models. A covariant defect measures whether
   a cross-family map commutes with these transports.
4. Graph-edge links are separate data. They are not silently identified with
   base-manifold parallel transport. When an identification is desired, it is
   a stated additional hypothesis.
5. Renormalization is first defined abstractly as a sequence of typed coarse
   maps between changing state spaces. The multivariate-Gaussian construction
   is then one realization of that general theory, not the definition of the
   theory.

In physics language, the manuscript now distinguishes three operations that
were previously liable to be conflated: changing coordinates in one fiber,
transporting a state along the base, and mapping between belief and model
fibers. It also distinguishes graph blocking from transport in a smooth
bundle. These distinctions are what make the covariance statements and the RG
composition laws checkable.

The rebuilt manuscript is **155 pages**, down from **255 pages**: a reduction
of **100 pages (39.2%)**. The cut came primarily from removing repeated status
registers, duplicated Gaussian setup, hand-numbered restatements, and
long-form qualifications that are now centralized.

## Review protocol

Ten independent specialist lanes were used, followed by integrated geometry,
source, concision, and final-referee waves.

| Lane | Primary question |
|---|---|
| Bayesian RG | What Berman–Klinger–Stapleton (BKS) proves, and what bridge to the present RG remains open |
| Network/Laplacian RG | Which scalar network-RG statements extend to matrix/gauge data |
| Graph machine learning | What graph pooling, message passing, and oversmoothing results actually guarantee |
| Markov coarse maps | Whether general stochastic coarse maps, disintegrations, and composition laws are typed |
| Effective support/holonomy | Whether kernels, support quotients, and cycle obstructions are correct |
| Quotient measure/exponential families | Whether quotient laws and variational-family closure are measure-theoretically sound |
| Variational semantics | Whether ELBO, moving-target, and coarse-evidence statements have the required hypotheses |
| RG dynamics/limits | Whether fixed points, cocycles, changing spaces, and two-index limits are distinguished |
| Matrix-cone probability | Whether PSD/Wishart/infinite-divisibility and matrix-refinement claims are valid |
| Concision/flow | Whether the theory-first ordering is readable, nonrepetitive, and physicist-accessible |

The specialist records are retained in
`docs/reviews/gauge-vfe-rg-pass2/`. A final referee challenged the integrated
source rather than the earlier memos. Its only high-severity finding exposed a
real edge-labeling ambiguity; after repair, the same referee reported zero
remaining medium-or-higher issues.

A later common-principal-bundle challenge wave separately checked gauge
symmetry, differential geometry, and manuscript-wide consistency. It caught
and closed three medium gauge issues (the active gauge group, the stabilizer of
a shared-link constraint, and the scope of a common trivialization), plus
three specification drifts. The gauge and integration referees then returned
clean rechecks; the differential-geometer reported no finding.

## Structural result

The final document has four parts:

| Part | Content | Starts on printed page |
|---|---|---:|
| I | General Gauge-Variational Foundations | 1 |
| II | General Coarse Maps and Renormalization | 50 |
| III | The Multivariate-Gaussian Realization | 66 |
| IV | Boundaries, Evidence, and Interpretation | 119 |

The general restriction theorem, stochastic coarse maps, changing-space RG
category, scale cocycle, bundle data at each scale, and cross-scale defects all
appear before any Gaussian specialization. Gaussian generative structure,
restrictions, information geometry, graph coarsening, and Gaussian RG are then
applied as a coherent realization.

## Principal mathematical repairs

### One principal geometry, two associated statistical geometries

The manuscript now begins with one principal \(G\)-bundle \(P\to\mathcal C\)
and constructs the probability-law objects as associated bundles
\(\mathcal E_b,\mathcal E_m\) using possibly different representations. The
law actions are induced from the sample actions, so the text does not treat a
probability bundle as principal.

Separate local sections \(u_i^b,u_i^m\) of \(P\) determine a unique relative
principal-frame field \(h_i\) through \(u_i^m=u_i^b h_i\). This field exists
even for inequivalent or different-dimensional representations, but it does
not define a cross-fiber operator. Such an operator requires the independent
equivariant data \(\Phi\) or \(\widetilde\Phi\).

The cross maps \(\Phi\) and \(\widetilde\Phi\) cover the identity on the base.
They are independent morphisms. Consequently
\(\widetilde\Phi\Phi\) and \(\Phi\widetilde\Phi\) are endomorphisms, not
identities unless an additional theorem supplies that property.

### Parallel transport and covariant defects

Separate connections \(\omega_b,\omega_m\) on the same \(P\) induce horizontal distributions
\(H^b,H^m\) and law-bundle transports
\(\Omega_\gamma,\widetilde\Omega_\gamma\). For a nonlinear cross map, the
correct infinitesimal obstruction is the vertical-valued difference
\[
(\mathcal D\Phi)_e(X)
=T_e\Phi(H_e^bX)-H^m_{\Phi(e)}X,
\]
with the analogous formula for \(\widetilde\Phi\). The familiar
\(D\Phi=\nabla^m\Phi-\Phi\nabla^b\) is retained only as the linear-vector-bundle
specialization.

### Graph links are not base transport

The graph is now an edge-labeled directed multigraph with a reversal
involution. Parallel edge copies are permitted and retain their labels. Every
edge copy satisfies
\(\Theta_{\bar e}=\Theta_e^{-1}\), while a two-edge cycle may use distinct
copies \(e\ne f\), so
\(H=\Theta_f\Theta_e\) can be nontrivial without contradicting the inverse-edge
rule. This closes the final referee's high-severity objection.

The text separately defines:

- graph link maps \(\Theta_e^b,\Theta_e^m\);
- pointwise frame comparisons;
- base transports \(\Omega_\gamma,\widetilde\Omega_\gamma\); and
- the optional hypothesis equating an induced graph link with transport along
  a chosen base path.

### General RG before Gaussian RG

The general scale theory now declares a target category, a state functor,
typed coarse arrows, level-dependent bundles and connections, and cocycle
composition. Cross-scale commutation failures are pairs of parallel arrows
with a declared equality locus; subtraction is used only when the target
supports it. The optional cross-channel identification \(\Xi_\ell\) is not
identified with either \(\Phi_\ell\) or \(\widetilde\Phi_\ell\).

### Probability, ELBO, and matrix cones

The revision separates existence of a conditional law from a chosen version,
states the hypotheses needed for moving-target ELBO comparisons, and avoids
claiming monotonic evidence when only an alternating optimization step is
available.

Wishart infinite divisibility is no longer stated generically on the full PSD
cone. The manuscript distinguishes the restricted Wishart domain from
matrix-Gamma/Dirichlet-type stochastic refinement and from a deterministic
two-sided inverse of aggregation.

## Source audit and allowed use

| Primary source | What it supports here | Boundary retained |
|---|---|---|
| Berman, Klinger & Stapleton, *Bayesian Renormalization*, MLST 4 (2023), DOI `10.1088/2632-2153/ad0102`, arXiv:2305.10491 | Posterior-concentration and information-geometric Bayesian-RG construction | No theorem identifying its flow with this manuscript's coarse-graining flow |
| Howard, Klinger, Maiti & Stapleton, *Bayesian RG Flow in Neural Network Field Theories* (2025), DOI `10.21468/SciPostPhysCore.8.1.027` | A concrete later Bayesian-RG application | Not evidence for gauge-bundle closure |
| Garuccio, Lalli & Garlaschelli, *Multiscale network renormalization* (2023), DOI `10.1103/PhysRevResearch.5.043101` | Geometry-free scalar network blocking and survival-product structure | Does not by itself provide matrix/gauge covariance |
| Villegas et al., *Laplacian renormalization group for heterogeneous networks* (2023), DOI `10.1038/s41567-022-01866-8` | Heat-kernel scale diagnostics and scalar Laplacian RG | Its real-space blocking is not promoted to a unique gauge-covariant rule |
| Gabrielli et al., *Network renormalization* (2025), DOI `10.1038/s42254-025-00817-5` | Current network-RG taxonomy and open problems | Review-level synthesis, not a new closure proof |
| Catanzaro, Garlaschelli & Patil, *Renormalization of Interacting Random Graph Models* (2026), DOI `10.1103/34n8-pw8x` | Interacting random-graph RG beyond independent-edge models | Does not erase the hypotheses of the independent-edge result |
| Joly & Keriven (2024); Loukas (2019); Ying et al. (2018) | Message-passing, spectral/cut, and learned-pooling precedents | Approximation or learned pooling is not exact closure of this theory |
| Oono & Suzuki (2020) | A rigorous oversmoothing/expressivity result for a specified GNN regime | Used as analogy unless its hypotheses are reproduced |
| Mehta & Schwab (2014) | Exact mapping between a variational-RG construction and deep learning under stated conditions | Not a universal RG–deep-learning equivalence |
| Hansen & Ghrist (2019) | Spectral language for cellular sheaves and connection-like graph data | Does not identify graph links with a smooth base connection |
| Mayerhofer (2010); Pérez-Abreu & Stelzer (2014) | Wishart parameter restrictions and infinitely divisible matrix-Gamma laws | Infinite divisibility gives stochastic refinement, not deterministic invertibility |

### Exact relationship to BKS

BKS supplies a statistically natural flow built from Bayesian updating,
posterior concentration, and information geometry. Near a regular posterior
mode, a nonlinear observable \(G(\theta)\) has the local delta-method
approximation
\[
G(\theta)\ \dot\sim\
\mathcal N\!\left(G(\mu_\tau),
\tau J_G I(\mu_\tau)^{-1}J_G^\mathsf T\right).
\]
This is exact for affine \(G\), but only leading-order local asymptotics for a
general nonlinear \(G\). The covariance uses the pushed-forward inverse Fisher
tensor, not the Fisher metric with its indices left covariant.

The present manuscript therefore treats BKS as a **typed comparison bridge**.
It does not claim that the Bayesian flow and the graph/blocking flow are the
same dynamical system, nor that their UV/IR orientations are automatically
opposite. Proving such a correspondence remains an explicit research
obligation.

## What is established and what remains open

The revision closes the finite theorem claims that can be proved from the
declared hypotheses. It deliberately does not relabel a research program as a
theorem. The central open directions are:

- a continuum/projective-limit law-bundle theory;
- regularity of the gauge quotient and effective support;
- existence, uniqueness, and stability of projection-based closure;
- an equivariant block selector and recovery map;
- projective consistency of RG laws across arbitrary blocking schedules;
- interchange of thermodynamic, continuum, and repeated-coarse-graining
  limits;
- a proved BKS-to-coarse-RG bridge, including orientation and scale matching;
- attraction in a declared scalarized or projective metric;
- classification of admissible matrix cones and stochastic refinements;
- nonflat compression with controlled holonomy;
- intrinsic scale selection for gauge-valued graph Laplacians;
- a model-Fisher to coupling/precision transfer theorem;
- stochastic inverse-RG identifiability and uncertainty;
- robustness of update dynamics under approximate closure;
- operational identification of base holonomy from observables;
- conditions identifying graph transport with base-manifold transport; and
- a physical-law claim tied to a specified system, observable, protocol,
  baseline, and held-out prediction.

These are research-grade questions, not hidden gaps in the proved core. Each is
now either stated as an open problem, hypothesis, or non-claim in the central
appendix.

## Mechanical and numerical verification

- Clean source-only mirror build using `build.ps1`; the in-place `main.log`
  was locked, so no stale worktree auxiliary file entered the final build.
- PDF: 155 pages, 1,057,185 bytes.
- PDF SHA-256:
  `F935CC5B35F26660065CE7351D2D2998C958C7C5610441F466B591A7BFCC7F79`.
- Numerical record SHA-256:
  `04C09073F7AAEB94212FD921034ACBA16D37513FF8E630E949529C2FA63C3D3D`.
- Numerical suite: **29 PASS, 0 FAIL, 0 INCONCLUSIVE**.
- Numerical claim inventory: 11 tagged occurrences, 9 substantive claims,
  all 9 mapped to passing checks.
- Labels: 486 declared, 486 unique.
- Undefined references/citations/control sequences: 0.
- Literal `??` in TeX source: 0.
- Literal `??` in extracted PDF text: 0.
- Multiply defined labels and rerun warnings: 0.
- Overfull and underfull boxes: 0.
- Visual inspection: title, contents, all four part boundaries, notation,
  central open-obligation ledger, numerical provenance, and final bibliography pages
  render cleanly.

The isolated baseline itself also contained no literal `??`; the user's
observed placeholders were therefore consistent with a stale or incomplete
compiled artifact rather than the frozen source. The new build is bound to the
current revised source and has been checked directly.

## Final assessment

The manuscript is now a rigorous theory document in the appropriate sense:
every central map has a domain and codomain, covariance is tied to declared
actions, general RG composition is well typed, the Gaussian model is clearly a
realization, and source-backed statements stop at the source boundary.

It would be mathematically misleading to call the whole research program
“finished” or to claim a verified physical law. The correct stronger result is
that the **present finite core is closed under its stated hypotheses**, while
the genuinely unresolved continuum, universality, inverse, and empirical
questions are visible and falsifiable.

No commit or push was performed.
