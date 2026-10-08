---
type: run
title: "MultiAgentELBO paired score assessment, augmented-filter boundary, and reward-learning domain"
aliases: ["Paired score assessment and filter-learning boundaries"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/info-geometry, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO paired score assessment, augmented-filter boundary, and reward-learning domain

[Code PR192](https://github.com/cdenn016/MultiAgentELBO/pull/192), with results pinned to `827424de21798442ee73e5937e75cf8e3e460571`, continues [[multiagentelbo-2026-10-08-record-error-formation-regime]]. It implements assessment of future saved flow scores and specifies two construction boundaries at fixed $c_*$. This note reports the source arguments and existing mechanical evidence; ingestion is not independent mathematical adjudication. No network experiment or GPU workload ran in this batch.

```bibtex
@misc{codex2026filterboundarylearningdomain,
  author = {Codex},
  title = {Paired Score Assessment, Augmented-Filter Boundary, and Reward-Learning Domain},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/192},
  note = {Results pinned to 827424de21798442ee73e5937e75cf8e3e460571}
}
```

## Paired assessment of saved scores

The [assessment contract](https://github.com/cdenn016/MultiAgentELBO/blob/827424de21798442ee73e5937e75cf8e3e460571/docs/research/2026-10-03-latent-link-rg-plan/R1-FLOW-ASSESSMENT-CONTRACT.md) fixes a pure NumPy consumer for the future complete grid: eight independent preparations at each of N512 and N1024, three control arms and three step sizes, all at accepted time one. For saved row log densities $l_{sr}$, it scores each row by $\ell_r=\log\operatorname{mean}_s e^{l_{sr}}$ and reports loss $-\operatorname{mean}_r\ell_r$. Its draw influence is $g_s=1-\operatorname{mean}_r e^{l_{sr}-\ell_r}$; sample standard deviation divided by $\sqrt S$ supplies the first-order Monte Carlo standard error. Paired contrasts use differences of aligned draw influences, preserving common-noise correlation. Receiver rows are not independent Monte Carlo replicates. The deterministic held-anchor arm contributes zero influence.

Twice MCSE, the half-pool loss difference and successive step-refinement loss differences have declared $.0025$ screens. The consumer retains all signed contrasts, rejects incomplete grids or mismatched endpoint times, and summarizes finest-step contrasts across the eight preparations per size. These are exploratory conditional precision and score-stabilization screens, not bias bounds, native-accuracy guarantees or state convergence. The [focused JUnit receipt](https://github.com/cdenn016/MultiAgentELBO/blob/827424de21798442ee73e5937e75cf8e3e460571/docs/research/2026-10-03-latent-link-rg-plan/evidence/r1-flow-assessment-focused.xml) records fifteen tests, no failures or skips, in .218 seconds. The 144-case grid remains disabled and unrun; CUDA agreement and capacity admission remain pending.

## Boundary of conditional-generator averaging

The [augmented-filter record](https://github.com/cdenn016/MultiAgentELBO/blob/827424de21798442ee73e5937e75cf8e3e460571/docs/research/2026-10-03-latent-link-rg-plan/R3-AUGMENTED-FILTER-BOUNDARY.md) studies the finite native population Fisher thermostat with full continuously observed geometry, a disjoint rooted-tree cover, positive weights independent of primitive generator means and at least one nontrivial tree. The algebra contains the identity direction. The candidate may carry auxiliary filter memory, but its retained generator must average the full native drift and covariance over a normalized Lebesgue density of all hidden means, with finite second moments and the stated drift integrability.

With retained mean $M=A\mu$, covariance $V=ACA^T$, active geometry covariance $a_Y$ and derivative $J=\partial_G(A\mu)$ extended across the other active coordinates, the native mean covariance after conditioning out geometry increments has Schur complement $V$. Conditional-generator averaging instead gives

$$
V+\Delta_\rho,
\Delta_\rho=\mathbb E_\rho[(J-\mathbb E_\rho J)a_Y(J-\mathbb E_\rho J)^T].
$$

The rooted-tree observability argument makes $\operatorname{tr}\Delta_\rho>0$ for such a nondegenerate hidden-mean density; it does not assert that the whole matrix is positive definite. Exact continuous-path quadratic covariations then separate the two laws, giving path total-variation distance one at every positive horizon and allowed positive temperature, for every interior initial law. Stationarity is no longer required. This excludes the specified averaging construction, not all augmented parents, alternative noise channels, finite-resolution observations or Chapter 11's different switching class. A Dirac hidden-mean carrier escapes the density condition but retains fine information; a point-lift plug-in changes the generator prescription. Neither supplies the requested regular compressed closure automatically.

## Global domain of the reward learner

The [learning-horizon record](https://github.com/cdenn016/MultiAgentELBO/blob/827424de21798442ee73e5937e75cf8e3e460571/docs/research/2026-10-03-latent-link-rg-plan/R4-LEARNING-HORIZON.md) keeps the positive finite binary catalog, nonnegative costs, fixed remaining generative parameters, realized-mark natural learning and positive fixed mobility. Writing $A=\log Z$, $m=\nabla A$ and $G=\nabla^2A$ gives $\dot\eta=\epsilon G^{-1}(B-m)$ and exactly $\dot m=\epsilon(B-m)$. A sufficiently long zero-mark interval reaches the original nonnegative reward domain's boundary with positive probability. The interior formula therefore needs a declared global boundary rule.

An explicitly unadopted extension to unrestricted rewards is conservative in the stated native temperature range, but has positive probability that all subsequent redraws select zero while every reward tends to minus infinity. There are still infinitely many redraws. This excludes an invariant probability on that extension's finite-reward state space; it is not a general obstruction to learned formation. Constants are finite-instance quantities without a uniform growing-size prevalence claim.

Two unadopted completions are described: tangent-cone projection in the Fisher metric on a declared compact reward box, or a proper conjugate prior on unrestricted rewards with an explicitly augmented MAP objective. The second confines the mean parameters inside the open cube, but permits negative rewards and is not a finite-KL variational claim for a Dirac recognition law on continuous rewards. It also does not settle the original nonnegative boundary choice. The [saved algebra receipt](https://github.com/cdenn016/MultiAgentELBO/blob/827424de21798442ee73e5937e75cf8e3e460571/docs/research/2026-10-03-latent-link-rg-plan/evidence/learning-horizon-algebra.json) records twelve exact coefficient and hazard identities. These checks are not a network simulation or an independent proof of recurrence. Neither completion was adopted, implemented or simulated; the user's choice remains pending.

## Relevance to this research

[[Renormalization-group flow of beliefs]] now distinguishes regular snapshot decoding from this specific conditional-generator boundary. [[Staged hierarchy formation and RG composability]] retains the prepared finite-window episode result while requiring a selected global learner, stationary control of the complete coupled process and quantitative entrance or excess-probability estimates. Reward confinement alone supplies none of those recurrence estimates. [[Gauge-Theoretic Multi-Agent VFE Model]] retains the unrun calibration and device admissions. General initialization, growing hierarchy and full parent closure remain unresolved; all four full RG gates stay open.
