---
type: concept
title: "Coarse Graining"
aliases:
  - "Coarse-graining"
  - "Blocking"
  - "Aggregation invariance"
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - cluster/social-physics/networks-and-contagion
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-09-28
---

# Coarse Graining

## What the parent discards and when, September 28, 2026

For the four-cycle parent of [[multiagentelbo-2026-09-28-early-parent]], the discarded coordinates are the fast within-pair disagreements and the kept ones are the slow shared modes, the source assignment, and the loops. The discarded relative entropy vanishes only once $\theta-\log(1/\epsilon)\to\infty$, so the coarse-graining is valid on a time window and not from the founding instant; [[Soft formation and the activation clock]] develops this. The classical counterpart is aggregation of nearly decomposable systems, one variable per block after the within-block short run ([[simon-1961-aggregation-variables-dynamic-systems]]), and the stationary criterion for a self-contained coarse level is informational closure, which strong lumpability implies ([[rosas-2024-software-natural-world]]). Sociologically, Sherif's shared norm is the kept coordinate and individual deviations are the discarded ones ([[sherif-1935-social-factors-perception]]). In Markov-chain terms, [[diaconis-1996-cutoff-phenomenon-markov-chains]] notes that one feature of a chain can mix at a different time from the whole chain, so the time from which a coarse-graining is valid has to be stated for the discarded features specifically; the cutoff reading of the four-cycle threshold is on the Soft formation page. These mappings are interpretive.

## Marginal and path errors: primary-source checks, September 26, 2026

[[hartmann-2020-coarse-graining-nonreversible-sdes]] proves separate bounds for time marginals and complete paths. Its path result requires resolved diffusion independent of hidden coordinates, integrability and Novikov conditions, and coefficient control on a fixed horizon; its bound includes a horizon-dependent term. It does not make a Markovian projection with correct marginals reproduce temporal correlations. [[backhoff-veraguas-2023-specific-relative-entropy]] studies a different divergence: normalized KL on finer time meshes, which can stay finite between singular diffusion laws. It cannot replace ordinary path KL in an unchanged fidelity criterion. The project-specific checked uses are recorded in [[multiagentelbo-2026-09-26-selection-and-reference-review]].


## Nonlinear adaptive cyclic formation, September 13

[[multiagentelbo-2026-09-13-nonlinear-adaptive-attention-rg]] constructs, for every fixed finite L>=2, nonlinear cyclic coalescence with exact marked parents and actual-law model learning. A model-posterior source row changes by TV greater than 0.37, and physical and optimizing hidden conditionals change by KL greater than 1/200 on the same 2/epsilon horizon. Conditional KL is O_L(epsilon^2), with separate complete-score and retained-path bounds. Every parent starts from the full actual retained joint law.

Source assignments are retained discrete coordinates with zero mobility. Their recognition masses stay fixed; changing model-posterior attention is distinguished from the actual recognition conditional that weights the marginal force. This admission repairs the collapsed proposal's marked-activation gap. Supplied contrasts, internal-neighbor support, calibration, small fixed standardized nonlinearity, and a shrinking amplitude/temperature regime remain explicit. All loops survive and base transport remains deferred. Earlier dated sections retain their original scopes.

> [!note] Current scope, September 11, 2026
> The normalized construction now gives exact common-channel VFE accounting with correlated recognition and posterior-fiber equality conditions; see [[multiagentelbo-2026-09-11-normalized-core]]. Compatible channels compose without a fixed-point assumption. Precision pooling, a coordinate statistic, a probability pushforward, an action-family projection and a changed experiment remain distinct operations; no universal RG orientation follows just from a tighter Gaussian covariance. [[multiagentelbo-2026-09-11-neighborhoods]] supplies normalized overlap and boundary contracts, while [[multiagentelbo-2026-09-11-gaussian-closure]] records Gaussian and Kron closure conditions.


Coarse graining is the procedure of integrating out or aggregating microscopic degrees of freedom to obtain an effective description at a larger scale, discarding detail while preserving relevant macroscopic behavior. It is the operational heart of statistical mechanics, the [[Renormalization group flow|renormalization group]], and emergent (entropic) descriptions of dynamics, and underlies the program's meta-agent hierarchy and [[Renormalization-group flow of beliefs|renormalization-group flow of beliefs]].

## Changing conditionals and actual parent learning

[[multiagentelbo-2026-09-12-adaptive-cyclic-rg]] makes the adaptive Gaussian distinction explicit: physical prior/posterior kernels determine the generative parent and its evaluator; the variational optimizer conditional defines the inherited restricted-family objective. The latter retains its original scalar offset and its derivative. Differentiating the optimizing lift gives each parent the complete model covector evaluated under its own law; replacing it with a bare marginal score would change the kinetics.

Noncommuting covariance barriers and moving mean defects bound discarded conditional KL directly. Actual-law activation preserves those bounds without covariance resets. Exact retained paths require inherited memory and colored noise; the autonomous parent has a separate finite-horizon approximation. Required raw cut marks remain full correlated kernels whenever they are not retained coordinates.

## Successive dynamical reduction with controlled conditional cost

[[multiagentelbo-2026-09-12-finite-depth-dynamical-rg]] gives exact normalized parent laws and conditional-family VFE identities through any prescribed finite depth in a compact path family. The sequential reduced process activates each parent from the actual current retained law. Its conditional KL, force and path errors are bounded separately; conditional losses at different times are not combined into a fictitious telescoping objective. Generated interactions and compact boundary identifications are retained. Approximate dynamical closure does not follow from exact static channel composition alone.

## Three operations that are routinely conflated

The MAgent exact-ELBO white paper's coarse-graining chapter makes a distinction the rest of the literature usually leaves implicit, and it is the sharpest available statement of what "coarse-graining" can mean inside a variational bound.

| Operation | Evidence $\log p(o)$ | Achievable bound |
|---|---|---|
| **Restriction** of the recognition family (e.g. tying a cluster to a common value) | unchanged | **lowered** |
| **Exact marginalization** of generative latents | unchanged (Fubini) | **raised** (collapsed VB) |
| **Model replacement** — discarding rather than integrating | **changed** | not comparable |

Only the third moves the evidence, and it is misspecification rather than coarse-graining: a bound computed for one model stands in no order relation to the evidence of a replaced model. The first two move the bound in *opposite* directions, which is the sharpest demonstration that they are not two descriptions of one procedure.

## Additive closure under a declared aggregation rule

The random-graph and Gaussian constructions below act on different laws and maps. Their additivity correspondence is an analogy to investigate.

**Networks.** [[garuccio-2023-multiscale-network-renormalization]] treats independent Bernoulli edges in binary undirected graphs, retaining self-loops. OR aggregation over nonoverlapping partitions preserves the specified fitness/dyadic family,
$$
p_{ij}=1-e^{-\delta x_i x_j F_{ij}},\quad i\ne j,\qquad
p_{ii}=1-e^{-\delta x_i^2F_{ii}/2}.
$$
For positive block fitnesses,
$$
X_I=\sum_{i\in I}x_i,\qquad
F_{IJ}=\frac{\sum_{i\in I,j\in J}x_i x_jF_{ij}}{X_I X_J}.
$$
Here $F=f(d)$ and $\delta$ is unchanged. Internal unordered edges and loops contribute once to a coarse self-loop. The reported uniqueness is conditional on the declared parameterization and additive fitness. [Published paper, Section II, Eqs. (1)–(7), Appendix A](https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.5.043101). The [retained PDF](../../sources/pdfs/garuccio-2023-multiscale-network-renormalization-arxiv-v3.pdf) is arXiv v3.

**Beliefs.** The white paper gives a separate Gaussian tying construction with a matrix-valued parameter. Tying a cluster is a congruence $\Lambda_c = S^\top \Lambda S$ by the $0/1$ aggregation matrix, under which the within-cluster Laplacian contributions cancel identically and

$$(\Lambda_c)_{IJ} = -\sum_{i\in I,j\in J} W_{ij}, \qquad (\Lambda_c)_{II} = \sum_{i\in I} A_i + \sum_{i\in I,j\notin I} W_{ij}.$$

Thus **the coarse coupling is exactly the sum of the fine couplings on cut edges** — a renormalization rule that is derived rather than posited, requiring no conductance ansatz. Marginalization, by contrast, is a Schur complement, which manufactures couplings between previously uncoupled agents and need not preserve the sign structure. The complementarity is the practical conclusion: *marginalization preserves the evidence and breaks the form; tying preserves the form and costs bound.*

> [!note] Editorial: scope of the analogy (2026-09-05)
> The immutable [[garuccio-2023-multiscale-network-renormalization]] note proposes a Gaussian uniqueness analog. That proposal is not established by the cited graph result. A matrix-precision claim needs its own admissible family, aggregation map and proof. For RG v2, use MSM as an independent-edge adjacency comparator; correlated gauge laws, ordered transports, holonomies and action-family closure retain separate obligations. Working with $F=f(d)$ also avoids assuming an inverse for $f$.

## What is lossless, and what a scale even is

**Sufficiency.** With constituents linked to a parent by $y_i \mid b \sim \mathcal N(\Omega_i b, R_i)$, the likelihood factors so that $T(y) = \sum_i \Omega_i^\top R_i^{-1} y_i$ is *sufficient* for the parent and the quadratic-term matrix is the precision-addition rule. Reduction to $T$ therefore discards nothing, and minimal sufficient statistics are unique up to bijection, so the reduction is canonical. A transported arithmetic mean is not sufficient; the [[Fisher information metric|Fisher]] information gap between the two rules measures constituent heterogeneity, which is the precise sense in which averaging is safe on a coherent cluster and lossy otherwise.

**The direction of the flow.** [[berman-2023-bayesian-renormalization]] fixes the RG parameter as $\tau = 1/T$ with $T$ the observation count: coarse-graining *widens* the posterior, inference *narrows* it. Precision addition increases $T$. Combined with sufficiency, this says that **precision pooling is not a coarse-graining at all** — it is a change of coordinates that runs the flow toward the UV — and only the family restriction is a renormalization step. This resolves a recurring puzzle in the [[Ouroboros multi-scale dynamics|tower]]: a coarse agent is *more* certain than its constituents, which is backwards for a coarse-graining and correct for a sufficient statistic.

**Selecting the scale.** Two complementary criteria, developed in the MAgent repo at `docs/derivations/2026-07-28-renormalization-literature-application.md`. [[villegas-2023-laplacian-renormalization-group|Laplacian RG]] locates the scale spectrally, from peaks of the entropic susceptibility $C(\tau) = -dS/d\log\tau$ of the density matrix $e^{-\tau L}/Z$, and hands over the partition as diffusion-equivalence cells. [[berman-2023-bayesian-renormalization|Bayesian RG]] prices it: tying kills the within-cluster *difference* subspace, and forcing a direction to a point is cheap exactly when its precision is *large*, so the selection objective is $\max_S \tfrac12\log\det(B_\perp^\top \Lambda B_\perp)$ over the orthogonal complement of the tied subspace. Because the restriction cost is a pure log-determinant it is **observation-independent** — the price of coarsening is a property of the coupling structure, not of the data — which is what makes a resolution scale attach to a *model* rather than to a run.

> [!warning] Contradiction in orientation, and it is only apparent
> Laplacian/Wilsonian schemes renormalize the **sample space** and keep the **soft** (small-eigenvalue) modes. Bayesian/[[berman-2023-bayesian-renormalization|BKS]] schemes renormalize the **model space** and keep the **stiff** (large-Fisher) directions. On one and the same matrix these select opposite subspaces. They are dual constructions on different spaces, not rival answers; but a sentence of the form "coarse-graining keeps the relevant directions" is ambiguous between them and, read the wrong way, is false.

## Recovery and partition selection

Losslessness has at least three strengths. A statistic can preserve one law, a channel can preserve
one tangent or score direction, or one parameter-independent recovery kernel can reconstruct an
entire statistical experiment. [[blackwell-1953-experiment-comparison]] supplies the last and
strongest comparison; [[Statistical experiment comparison and deficiency]] records quantitative
relaxations when exact recovery fails. The project's finite Fisher-equality diagnostics therefore do
not by themselves establish experiment-level recovery.

For finite Markov dynamics, [[geiger-2013-kl-aggregation]] proposes a KL-divergence-rate objective
and information-bottleneck search for candidate partitions, while
[[geiger-temmel-2013-information-preserving-aggregation]] gives conditions for lossless aggregation
in its declared finite-chain setting. These are useful partition baselines, not intrinsic selectors
for the gauge-VFE model. Candidate blocks should still be graded by lumpability, KL rate,
retained-interaction residual, and gauge/relabeling invariance. [[ahn-2018-bucket-renormalization]]
is a complementary factor-graph/tensor-network approximate-inference comparator; it does not prove
the project's open Bayesian-RG equivalence or natural-gradient semiconjugacy.

## Gaussian Galerkin pushforward and gauge-absorbed gains (review, September 23, tentative)

Investigator X11 of the 2026-09-23 Theory review ([[multiagentelbo-2026-09-23-theory-streamlining-review]]) corrects two framing claims in the Gaussian realization. First, the Galerkin coarse Gaussian is a Markov pushforward. For $\Lambda\succ0$ and injective $S$, with $\Lambda_c=S^\top\Lambda S$ and $P_\Lambda=\Lambda_c^{-1}S^\top\Lambda$, the identity $P_\Lambda\Lambda^{-1}P_\Lambda^\top=\Lambda_c^{-1}$ shows that $P_\Lambda$ maps $\mathcal N(\Lambda^{-1}h,\Lambda^{-1})$ to $\mathcal N(\Lambda_c^{-1}S^\top h,\Lambda_c^{-1})$. On each fixed-precision mean fiber this is one parameter-independent kernel, so data processing applies with Fisher defect $\Lambda-\Lambda S\Lambda_c^{-1}S^\top\Lambda\succeq0$, the maps compose across levels, and with an observation-free precision the coarse posterior preserves the evidence. What fails is a single law-independent kernel on the whole precision cone. The manuscript's "restriction, not a Markov pushforward" therefore names the wrong obstruction.

Second, the SPEC rotation witness that the Gaussian interaction family "is not a consequence of directed linear-Gaussian models" is pure gauge. The directed law depends on gain and link only through $T_i=G_i\Theta_{i,\mathrm{pa}(i)}$, which transforms like a link, and on a forest every assignment with $\det T_i>0$ can be absorbed into the frames. For one edge, X11 states the chart-independent criterion that $J\succ0$ with invertible $J_{12}$ can be reframed by $\mathrm{GL}^+(K)$ into the interaction family exactly when $(-1)^K\det J_{12}>0$. Chart-independent witnesses are an orientation-reversing gain or a v-structure. If the theory forbids absorbing gains into frames, the original witness stands as a typed statement.

> [!warning] Tentative: investigator recomputation, same model family, not adjudicated
> Short identities and random-instance checks (residuals near $10^{-15}$) by one investigator (Claude Opus 5.5). These items belong to the proposed Gaussian supplement.

### Incorporation in the restructured manuscript (September 24)

Both corrections are now statements of Supplement G at `623e4fe` ([[multiagentelbo-2026-09-24-theory-restructure]]), tagged ESTABLISHED. `prop:ig-galerkin-pushforward` in Chapter G7, "Galerkin aggregation is a precision-dependent pushforward", states for $\Lambda\succ0$ and injective $S$ that $P_\Lambda=\Lambda_c^{-1}S^\top\Lambda$ pushes $\mathcal N(\Lambda^{-1}\mathsf h,\Lambda^{-1})$ to the Gaussian with natural parameters $(S^\top\mathsf h,S^\top\Lambda S)$, that on a fixed-precision mean fiber it is one parameter-independent kernel whose pushed Fisher metric $\Lambda S\Lambda_c^{-1}S^\top\Lambda\preceq\Lambda$ is equal to $\Lambda$ exactly on tangent directions in $\operatorname{range}(S)$, and that nested aggregations compose. The varying-precision case, the singular boundary member and unbounded depth form one open problem, `open:grg-galerkin-monotonicity` (Chapter G9). In the main manuscript, Chapter 9's section "Pushforward, precomposition, and Galerkin restriction" (`sec:cg-three-operations`) keeps the three operations apart: `prop:cg-hard-identification` shows that precomposition on a finite space is conditioning, which can increase relative entropy (from 0.0031 to 0.0589 in its witness), so data processing and evidence preservation do not transfer to it, and `def:cg-galerkin-data` types Galerkin data by the coarse form of aggregation-based algebraic multigrid.

The gauge absorption is `prop:gauss-gain-absorption`, "Gain absorption and the orientation criterion", in Chapter G3: the directed law depends on gain and link only through one transition that transforms like a link, forests with positive-determinant transitions are absorbed by $\mathrm{GL}^+(K)$ frames, a two-agent precision with invertible off-diagonal block is reachable exactly when $(-1)^K\det\Lambda_{12}>0$, and the original SPEC witness is absorbed. `prop:gauss-law-level-witnesses` gives the chart-independent witnesses: a receiving factor whose transition has negative determinant, a sign invariant of cycles, and, for odd $K$, a v-structure. The same restructure corrected functoriality of nested blockings, recorded in [[Renormalization-group flow of beliefs]].

> [!warning] Status
> Manuscript statements with proofs, written and checked by Claude Opus 5.5 agents with their own scripts; no cross-model check (the author's choice) and not adjudicated.

## Related

[[Renormalization group flow]], [[Renormalization-group flow of beliefs]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]], [[Fisher information metric]], [[Graph Laplacian]], [[Entropic Force]], [[Mean-Field Approximation]], [[Evidence lower bound (ELBO)]]

## Sources

- [[blackwell-1953-experiment-comparison]] — experiment-level comparison by common
  parameter-independent garbling/recovery kernels.
- [[geiger-2013-kl-aggregation]] — KL-rate Markov aggregation and an information-bottleneck
  partition-search baseline.
- [[geiger-temmel-2013-information-preserving-aggregation]] — lossless finite-chain aggregation
  under explicit structural conditions.
- [[ahn-2018-bucket-renormalization]] — bucket-renormalization approximate inference as a
  factor-graph/RG comparator.

- [[garuccio-2023-multiscale-network-renormalization]] — uniqueness of the aggregation-invariant connection probability; additivity as the renormalizability criterion; the scale-free vs. scale-invariant demarcation.
- [[villegas-2023-laplacian-renormalization-group]] — diffusion time as an intrinsic RG scale; entropic susceptibility as a scale detector; diffusion-equivalence supernodes.
- [[gabrielli-2025-network-renormalization]] — the three-step program and the survey placing geometric, Laplacian and multiscale schemes against it.
- [[berman-2023-bayesian-renormalization]] — the Fisher metric as an emergent RG scale; stiff/sloppy as relevant/irrelevant; $\tau = 1/T$ fixing the direction of the flow.
- [[beny-osborne-2015-info-geometric-rg]] — coarse-graining as metric contraction on a statistical manifold.
- [[garciaperez-2018-multiscale]] — geometric renormalization of real networks by latent-space proximity.
- [[verlinde-2011-entropic-gravity]] — coarse-graining and entropic descriptions of dynamics.
