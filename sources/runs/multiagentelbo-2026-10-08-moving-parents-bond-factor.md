---
type: run
title: "MultiAgentELBO moving-parent noise and normalized bond candidate"
aliases: ["Moving-parent noise and normalized bond candidate"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/info-geometry, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO moving-parent noise and normalized bond candidate

[Code PR189](https://github.com/cdenn016/MultiAgentELBO/pull/189), merged at `4a2bc57bbde407391716827ac52e517910a2616d`, continues [[multiagentelbo-2026-10-08-independent-preparations-native-trajectory]] on the surviving Gaussian code after the repository cleanup. It adds a tested matched-time calibration driver and completes two bounded analytical constructions. All four full RG gates remain open. This source records the derivations and executed coefficient checks; it does not independently adjudicate the mathematics.

```bibtex
@misc{codex2026movingparentsbondfactor,
  author = {Codex},
  title = {Moving-Parent Noise and a Normalized Bond Candidate},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/189},
  note = {Conditional finite constructions and CPU coefficient checks; full RG gates open}
}
```

## Moving rooted maps

The [R3 derivation](https://github.com/cdenn016/MultiAgentELBO/blob/4a2bc57bbde407391716827ac52e517910a2616d/docs/research/2026-10-03-latent-link-rg-plan/R3-RETAINED-QUADRATIC-VARIATION.md) declares a fixed independent Gaussian probe per primitive to couple conditional sampled links across inference time. This preserves each recognition snapshot but adds a temporal choice distinct from the implemented latent episode-history law. For a readout $M=A\mu$, $V=ACA^T$, with $A$ depending on separate geometry coordinates $G$, its continuous mean covariance is $2T(V+J a_GJ^T)dt$, where $J=\partial_G(A\mu)$. Cross-covariances with geometry and $V$ preserve all shared-primitive derivative terms. The map is restricted to the stated product metric; matter-dependent membership requires a larger Jacobian.

On a positive-weight rooted GL tree, the central generator direction identifies each descendant subtree's transported mean through the mean/generator cross-variation. Retaining those subtree sums gives an invertible exact carrier at O(N) mean-storage cost, alongside all fine covariance and geometry state. It is an exact reference without compression. A separate lossy carrier uses the weighted lift $\widehat\mu=a+CA^TV^{-1}(M-Aa)$. The source derives a stopped synchronous path-Wasserstein bound controlled by the integrated discarded energy $\|\mu-\widehat\mu\|_{C^{-1}}^2$ and local coefficient constants. It supplies no uniform residual, exit or growing-horizon control, path total variation, regular filter or structural-jump comparison.

The [coefficient output](https://github.com/cdenn016/MultiAgentELBO/blob/4a2bc57bbde407391716827ac52e517910a2616d/docs/research/2026-10-03-latent-link-rg-plan/evidence/retained-noise-algebra.json) records eight CPU float64 identities within 2.23e-16 on a three-node noncommuting GL+(2) tree with fixed generator covariances and zero probe. These ground coefficients only; no stochastic path was simulated.

## Normalized structural candidate

The [R4 derivation](https://github.com/cdenn016/MultiAgentELBO/blob/4a2bc57bbde407391716827ac52e517910a2616d/docs/research/2026-10-03-latent-link-rg-plan/R4-NORMALIZED-STRUCTURAL-FACTOR.md) instantiates the existing globally normalized partition-factor direction with Bernoulli bonds, reversal-symmetric transported matter costs and finite rewards. An all-zero bond contribution bounds its global normalizer away from zero at every fixed finite volume. Conditional matter integration gives explicit Gaussian precision, determinants and parent/child disintegrations; marginalizing generators retains a mixture. The extension changes the fine generative law and has not been adopted or implemented.

Population recognition forces use the existing Fisher metric, and generative learning retains the global normalizer score. The latent bond conditional, variational coordinate optimum and recognition-thermostat redraw are different laws. Local curvature is derived after marginalizing actual bonds, including the negative mixture-curvature term. It holds in a stated coherence region and does not establish entry, persistence, nontrivial blocks or second-stage dependence. A high-bond regime can merge the whole graph, so a hierarchical mechanism and counterfactual margin remain required. SPEC R13 supplies symmetry provenance, rather than a replacement for normalized learning.

The [structural coefficient output](https://github.com/cdenn016/MultiAgentELBO/blob/4a2bc57bbde407391716827ac52e517910a2616d/docs/research/2026-10-03-latent-link-rg-plan/evidence/structural-factor-algebra.json) records Gaussian integration, link derivatives, bond-marginal curvature and fiber reconstruction checks; maximum absolute discrepancy is 1.34e-11 in a finite-difference derivative. This tiny noncommuting fixture validates formulas, not formation at the intended scale.

## Numerical continuation and relevance

The [flow driver record](https://github.com/cdenn016/MultiAgentELBO/blob/4a2bc57bbde407391716827ac52e517910a2616d/docs/research/2026-10-03-latent-link-rg-plan/R1-INDEPENDENT-FLOW-CALIBRATION.md) describes eleven passing tiny CPU tests, with saved JUnit, for accepted-time integration, incomplete-state preservation, inference-only input routing and fresh future matter/source scoring. Its 144-case candidate grid remains disabled pending actual CPU/CUDA agreement, capacity admission and frozen assessment budgets. The GPU was occupied and no allocation occurred. Existing parent-context precision remains inconclusive without extension.

These constructions refine the parent-noise and structural-model obligations for [[Gauge-Theoretic Multi-Agent VFE Model]], [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]]. Neither a theory-wide metric or loop family nor base-manifold transport is introduced. No manuscript edit, large-network run, full test suite, historical retry or formation claim accompanies this batch.
