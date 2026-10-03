---
type: manuscript
title: "MultiAgentELBO continuous parent integrability and grid limits, October 3, 2026"
aliases: ["Continuous parent integrability and grid limits"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-03
---

# Continuous parent integrability and grid limits

> [!info] Citation
> MultiAgentELBO project (2026). *Continuous parent integrability and grid limits*. Research records at code commit [5b45634](https://github.com/cdenn016/MultiAgentELBO/commit/5b45634adf8bbefe44faaf9ebff07604872db770), [PR116](https://github.com/cdenn016/MultiAgentELBO/pull/116). The three full derivations are retained under sources/archives/multiagentelbo-2026-10-03-continuous-parent-limits/. This follows [[multiagentelbo-2026-10-03-conditional-parent-error]]. No new scientific calculation was executed.

## Finite continuous budget

For every fixed finite frozen affine switching model, positive-definite constant noise, positive quadratic-softmax source rows, Gaussian activation, fixed retained projection and declared finite cubature rule, the Gaussian-message candidate has a finite expected auxiliary path budget on every finite horizon. The [proof](../archives/multiagentelbo-2026-10-03-continuous-parent-limits/continuous-budget-integrability.md.txt) controls the native-driven error e=z-m by L=e^T adj(I+S)e and augments it with a power of 1+tr S. Its generator is bounded by a fixed constant times this Lyapunov function, including all visible source resets. Higher powers give every fixed polynomial message moment. No covariance floor or inverse-covariance moment is required.

This discharges the additional integrability hypothesis of the preceding conditional entropy argument at its frozen finite-model scope: B=G+D(P_Y||S_Y). The hidden-information term G remains unknown and candidate-independent. The candidate covariance does not equal the true conditional covariance. The constants may grow with dimension, temperature and horizon; finiteness is not a small-error or uniform-regime result. Bishop and Del Moral's [Kalman-Bucy analysis](https://arxiv.org/abs/1610.04686), Sections 1-2, supplies related continuous Riccati context; the label-dependent reset and adjugate arguments are derived explicitly in the research record.

## Exact-arithmetic grid and expectation limits

The [pathwise proof](../archives/multiagentelbo-2026-10-03-continuous-parent-limits/continuous-grid-limit.md.txt) couples meshes through one Brownian path, proposal clock and label uniforms. Subtracting K(S)R from the message mean turns the stochastic update into an ordinary integral equation with a vanishing accumulated discrete remainder. The finite proposal list eventually has identical coupled labels. Smooth visible source maps then give almost-sure uniform state convergence on a fixed finite horizon. Invisible self-proposal subdivisions disappear in the limit. The actual ordered physical cubature coordinates are fixed: signed QR produces the same local Cholesky orientation as the dense method. Arbitrary changes of cubature coordinates are not identified.

The [numerical moment proof](../archives/multiagentelbo-2026-10-03-continuous-parent-limits/continuous-grid-moments.md.txt) applies to deterministic meshes enriched by the independent proposal clock, including the implemented mesh rule. Each endpoint-conditioning step splits exactly into an auxiliary measurement update and an affine Gaussian forecast. Adjugate bounds give a 1+O(step) moment multiplier; source updates give one fixed multiplier per proposal. Averaging that multiplier over the Poisson count establishes uniform higher moments for sufficiently small steps. Together with the pathwise result, these bounds prove L1 convergence of the idealized fixed-probe output and convergence of its expectation to the continuous auxiliary budget.

The fixed two-probe source estimate converges to a random, conditionally unbiased estimator of the continuous source integral. Its sampling variance generally remains positive. The result gives no evaluated finite-grid bias bound, confidence interval for sixteen saved paths, or floating-point stability claim. Reusing an integer seed on a newly generated grid is not itself the required common Brownian coupling. The original dense failure and all archived numerical results remain unchanged.

## Relevance to this research

[[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]] can now proceed from finite budget and qualitative convergence of expected numerical functionals. The next obligations are quantitative discretization and sampling control and, separately, small true retained-prediction error in both Chapter 11 regimes. Endogenous structural feedback and second intrinsic formation remain O4. These results do not close O1 or O4, change the active profile, or edit the theory manuscripts. No experiment, unit test or GPU calculation ran in this analytical round.

## BibTeX

```bibtex
@misc{multiagentelbo2026continuouslimits,
  author = {{MultiAgentELBO project}},
  title = {Continuous Parent Integrability and Grid Limits},
  year = {2026},
  howpublished = {Research records, MultiAgentELBO commit 5b45634},
  url = {https://github.com/cdenn016/MultiAgentELBO/commit/5b45634adf8bbefe44faaf9ebff07604872db770}
}
```
