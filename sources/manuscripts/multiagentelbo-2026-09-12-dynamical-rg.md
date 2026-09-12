---
type: manuscript
title: "Finite VFE-driven coalescence and two dynamical RG reductions, September 12, 2026"
aliases: ["Finite dynamical RG construction September 2026"]
tags: [cluster/multi-agent, cluster/vfe, cluster/gauge-theory, cluster/info-geometry, project/multi-agent, field/mathematics, field/physics, field/statistics]
created: 2026-09-12
updated: 2026-09-12
year: 2026
---

# Finite VFE-driven coalescence and two dynamical RG reductions, September 12, 2026

## Citation and provenance

MultiAgentELBO research program (2026). *A finite dynamical RG construction at one base point*. Internal derivations and independent reconstruction, September 12, 2026. Original contributor attribution is retained in the archived files.

This immutable note records the completed finite existential construction and its stated limits. The [source archive](../archives/multiagentelbo-2026-09-12-dynamical-rg-snapshot.zip) preserves 76 files; the [manifest](../archives/multiagentelbo-2026-09-12-dynamical-rg-manifest.json) gives their original paths and hashes. Archive SHA-256: `f14ab1ca007feae78b288dc134b3d28b90ff206c5038d7829ea1537013ea2f84`. The canonical MultiAgentELBO checkout was at `de254119d370c983578228bae025455aa3280679`, but the new derivations were uncommitted working-tree files. That commit does not identify their content. The snapshot, rather than the moving checkout, fixes this note's source bytes. Older dependencies remain in [[multiagentelbo-2026-09-11-research-snapshot]] or at the source locators recorded in the derivations.

## Problem and admitted model

The target is a nonempty finite model family joining intrinsic VFE-driven coherence to two compatible reductions at a single base point. The ambient agents remain paired belief/model law sections with independent dynamic interaction links. The proof examines their pointwise network and introduces no base-manifold transport. It develops the internal-Hessian, inherited-metric and conditional-prior ideas already present in the live PIFB2; those ideas retain their claim-specific maturity and are not used as proof.

The joined example is a three-agent cycle with two Gaussian law channels, fixed distinct covariances, circle-valued means and six independent SO(2) link angles. Its configuration space is $\mathbb T^{12}$ with normalized product Haar measure. Positive intrinsic interactions and a normalized Gaussian physical evaluator define one proper generative law. Correlated outer recognition and a declared local reversible diffusion supply the variational and kinetic structure. These choices are assumptions of the construction. In particular, the specified node rates and the elimination order are supplied; neither universal slow models nor a hierarchy of clocks is derived. No capability, storage, or externally priced formation criterion is imposed.

## Exact VFE and parent laws

The evaluator's information projection has an explicit nonnegative cost $d(W)$. For generative configuration law $P_0$, arbitrary correlated recognition $Q$, and positive temperature $T$,
$$
\mathcal F_T(Q)=T\operatorname{KL}(Q\Vert P_0)+T\mathbb E_Q d,
\qquad \Pi=c^{-1}e^{-d}P_0,
\qquad c=\mathbb E_{P_0}e^{-d}>0.
$$
This is the negative ELBO of the unchanged augmented model in its declared conditional recognition family. The generative law $P_0$, the variational optimizer $\Pi$, and the evolving recognition law $Q_t$ are distinct. The diffusion decreases this density-level objective; it is not identified with every agent's deterministic Fisher inference.

The fixed recognition-independent maps successively remove node 2's two matter angles and node 1's two matter angles, while retaining the root laws and every independent link. They give $\mathbb T^{12}\to\mathbb T^{10}\to\mathbb T^8$. For the first map, write $Q_1=C_{1\#}Q$, $P_1=C_{1\#}P_0$ and
$$
d_1(y)=-\log\mathbb E_{P_0(\cdot\mid y)}e^{-d(W)},
\qquad K_1^*(dW\mid y)=e^{-d(W)+d_1(y)}P_0(dW\mid y).
$$
Then
$$
\mathcal F_T(Q)/T=\operatorname{KL}(Q_1\Vert P_1)+\mathbb E_{Q_1}d_1
+\mathbb E_{Q_1}\operatorname{KL}\bigl(Q(\cdot\mid y)\Vert K_1^*(\cdot\mid y)\bigr).
$$
The first two terms form the exact parent objective after minimizing over the hidden conditional. The original generative conditional $P_0(dW\mid y)$ supplies downward priors and normalized parent evaluators; it must not be replaced by the recognition-optimal $K_1^*$. Repeating the same construction on $(P_1,d_1)$ agrees with direct elimination by conditional expectation. Generated interactions, evidence constants and conditional variational costs remain present. The integrated hidden kernel belongs to the parent's distributional structure, not an independently evolving parent coordinate. Removing those latent variables from both augmented distributions produces a further conditional-KL term.

## Coherence, response and inherited dynamics

The complete unforced action has a three-dimensional coherent minimum manifold. Nine independent mismatch constraints have rank nine, and the full Hessian is positive in the nine normal directions. This proves an open deterministic basin with relaxing mismatches and actual link motion. With root and links held fixed, positive conditional Hessians and a positive Schur complement show that both eliminations remove restoring matter modes. They are not reductions obtained solely by forgetting passive gauge coordinates. Whole-block coherence permits a first connected reduction and then a second; it does not prove a prior pair-only formation episode or select a unique partition.

The stochastic parents inherit their conditional-integral forces and mobilities from the same microscopic diffusion. Fixed-temperature Poisson estimates give two successive finite-horizon path comparisons. A separate argument in that same compact model joins coherence and reduction: deterministic tracking, uniform force-level Laplace estimates, and Brownian maximal bounds admit a nonempty regime obtained by choosing the middle rate, a faster inner rate, and finally sufficiently small positive temperature. Constants and neighborhood margins are explicit in the parent bridge. These are existence bounds, not experimentally calibrated parameter recommendations.

Normalized external heading observations produce collective response under matched observation strengths. A sufficiently strong declared mismatch force gives a finite exit from the admitted coherence neighborhood. A controlled local parent approximation loses its license after that exit, while exact probability pushforwards still exist. This supplies a departure mechanism, not an unrestricted law for repeated merging and membership turnover.

The separate noncompact SO($d$) radial construction supplies a nonzero attracting basin and stabilizer-holonomy examples. It is additional scoped mathematics; it is not substituted for the compact witness at the two-reduction interface. On the compact SO(2) coherent manifold the loop sector is flat, although off-manifold links and their holonomies remain dynamic.

## Evidence and unresolved extensions

The frozen contract records `COMPLETE_AFFIRMATIVE` for this finite existential target. Three construction specialists and three independent checking specialists produced written derivations and reconstructions. Their number or agreement is not mathematical evidence: the archive retains the formulas, hypotheses, corrected interfaces and argument for each dependency. The release validator checked package structure and source bindings. A separate tiny exact Fourier calculation checked four induced-interaction identities; it does not prove the dynamical estimates. This ingestion performed no new proof review or scientific rerun.

Path accuracy does not control the dimensionless transient conditional KL in the displayed identity. The actual fine conditional need not equal $K_1^*$, and the autonomous parent is not proved to reproduce the full fine VFE trajectory. A uniquely selected grouping, unsupplied clock hierarchy, unrestricted noncompact reduction, arbitrary initial states, general repeated merger episodes, infinite depth and physical-time identification remain open. The result retains complete conditional-integral interactions and does not claim closure in the original short pairwise ansatz.

## Source locators

Within the archive, the current synthesis and three main derivations are under `MultiAgentELBO/docs/derivations/2026-09-11-meta-agent-formation-frontier-and-locality/`: `dynamical-rg-assembly.md`, `microscopic-vfe-dynamics-construction.md`, `complete-coherence-dynamics.md`, and `dynamical-parent-rg-bridge.md`. The last document's Sections 7.1–7.3 carry the joined regime. Beside them, `coherence-independent-check.md`, `parent-independent-check.md`, and `model-and-contract-independent-check.md` preserve the independent reconstructions. The frozen contract, claim dependencies, proof snapshots and release records are under `evidence/2026-09-12-dynamical-rg-goal/`. Prior ideas are preserved in `Research/manuscripts/PIFB2.tex`, including `sec:meta_agent_rg`, `sec:time_info` and `sec:scale_dependent_time`.

The [live synthesis](<C:/Users/chris and christine/Desktop/MultiAgentELBO/docs/derivations/2026-09-11-meta-agent-formation-frontier-and-locality/dynamical-rg-assembly.md>) is a convenience link and may evolve after ingestion.

## Relevance to this research

This result develops intrinsic coalescence within [[Multi-agent variational free energy]] and connects it to [[Meta-agents and hierarchical emergence]], [[Coarse Graining]] and [[Renormalization group flow]]. It extends the finite operational studies in [[multiagentelbo-2026-09-11-formation]] through actual relaxing law/link dynamics. [[Gauge-VFE RG research synthesis September 2026]] and [[Staged hierarchy formation and RG composability]] distinguish exact law composition from approximate inherited paths. [[Gauge-Theoretic Multi-Agent VFE Model]] retains the broader section-valued ontology and the unresolved general hierarchy problem.
