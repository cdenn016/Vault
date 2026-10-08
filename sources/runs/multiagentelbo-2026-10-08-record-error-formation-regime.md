---
type: run
title: "MultiAgentELBO original-record error, regular parent coordinates, and prepared formation regime"
aliases: ["Original-record error and prepared formation regime"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/info-geometry, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO original-record error, regular parent coordinates, and prepared formation regime

[Code PR191](https://github.com/cdenn016/MultiAgentELBO/pull/191), merged at 144f7828875fdd5243a11d076d0d042f77b9c7d3, continues [[multiagentelbo-2026-10-08-discarded-energy-device-admission]]. The batch derives an original-record prediction bound, constructs stationary hidden-recognition coordinates while locating a continuous-history limitation, and supplies a prepared finite-window regime for the existing normalized bond candidate. This note reports those source arguments and executed algebra checks; ingestion is not independent mathematical adjudication.

```bibtex
@misc{codex2026recorderrorformationregime,
  author = {Codex},
  title = {Original-Record Error, Regular Parent Coordinates, and a Prepared Formation Regime},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/191},
  note = {Conditional analytical results and exact coefficient grounding at fixed base point}
}
```

## Original-record prediction error

The [record-error derivation](https://github.com/cdenn016/MultiAgentELBO/blob/144f7828875fdd5243a11d076d0d042f77b9c7d3/docs/research/2026-10-03-latent-link-rg-plan/R3-ORIGINAL-RECORD-ERROR.md) compares the original product recognition law $q=N(\mu,C)$ with its centered reconstruction $\widetilde q=N(\widehat\mu,C)$ at the same retained state. With block diagonal $C$, positive observation noise and identical source/generator mixing laws, the mean marginal row KL obeys

$$
\mathcal E_{\rm row}\leq\frac{1}{2m}\sum_i d_i r_i^TC_i^{-1}r_i
\leq\frac{\Delta}{2m}R_*,
 r=\mu-\widehat\mu,
 \Delta=\max_i d_i.
$$

Here $m$ is the number of queried original rows and $d_i$ is their source-prior-weighted incidence on matter block $i$. The inequality follows from the whitened Gaussian record operator being bounded by the projector onto its incident coordinates. Its constant does not depend on link singular values. Uniform four-neighbor source weights give $\Delta=2$ and, for one queried row per agent, the bound $R_*/N$. Sparse support alone does not control a hub's incoming source mass.

This is expected excess marginal composite log loss under the original recognition-induced record law. It is distinct from realized score differences on arbitrary data, exact latent-posterior error, and the separate joint-network KL bound $R_*/2$. The previous stopped residual integral transfers to integrated row error with factor $\Delta/(2m)$, but does not control errors from an independently evolving approximate retained state. Eleven exact rational fixture checks ground the retained mean, Gaussian row KL, Woodbury identity, incidence bound and joint bound; their small coordinate dimension is not evidence for a thermodynamic limit.

## Regular snapshots and continuous retained histories

The [regular-parent record](https://github.com/cdenn016/MultiAgentELBO/blob/144f7828875fdd5243a11d076d0d042f77b9c7d3/docs/research/2026-10-03-latent-link-rg-plan/R3-REGULAR-PARENT-REPRESENTATION.md) uses the positively anchored native Fisher thermostat under stationary initialization, a fixed finite graph and its stated temperature range. Conditional recognition means have law $N(u,TK^{-1})$ before conditioning on $M=A\mu$. This is a distribution of recognition parameters, distinct from the latent matter belief $N(\mu,C)$. Fixed pivot coordinates on the hidden affine fiber yield a smooth Gaussian density against common Lebesgue measure, continuously differentiable into $L^1$, with continuous initialization from the retained snapshot. The parameter count is independent of temperature and horizon but grows with the fine dimension.

Exact Gaussian moments also supply an averaged local retained diffusion, including the covariance term lost by substituting only the conditional mean. The source establishes local existence and an infinitesimal reversibility identity, not global conservativity. For a disjoint rooted-tree cover with at least one nontrivial tree, positive weights independent of primitive generator means, complete primitive geometry and exact continuous observation, cross quadratic covariations reveal the hidden recognition means after activation. Their history-conditioned laws are Dirac measures, so the stationary snapshot decoder is not the history filter. Under these assumptions and stationary initialization, every state-only first-order diffusion on the stated retained coordinates has path total-variation distance one from the native projected path. This is not a negative resolution of Chapter 11's different switching class, arbitrary augmented filters, overlapping readouts or finite-resolution observations.

The sampled primitive generator offers an explicit coordinate alternative rather than automatic compression: with the actual upper precision-Cholesky convention, its quadratic variation is $V_\omega=R D_\epsilon R^T$, where $D_\epsilon$ is known and positive. Reverse Cholesky recovers $R$, the complete recognition covariance, and the recognition mean from $(\omega,V_\omega,\epsilon)$. Continuous primitive paths therefore retain that information; only $\omega$ at activation does not determine its bracket. Eight exact dimension-two identities ground these coefficients and the stationary conditional formulas. Finite-time initialization, a regular compressed history filter, structural jump updates and both required switching horizons remain open.

## Prepared finite-window promotion

The [formation-regime construction](https://github.com/cdenn016/MultiAgentELBO/blob/144f7828875fdd5243a11d076d0d042f77b9c7d3/docs/research/2026-10-03-latent-link-rg-plan/R4-FORMATION-REGIME.md) supplies an open regime for each fixed compatible periodic lattice, including the N512 and N1024 layouts. Initial laws are supported in a sufficiently small compact subset of that prepared region. A four-vertex island has prepared mean and width asymmetry, while model rewards are homogeneous. Initially all structural bonds are off and source probability rows are uniform; no discrete source matching is prescribed. Original Gaussian observations have small positive precision, generator laws have small positive full width with noncommuting GL+(2) means, and a normalized pathwise reward learner has small positive mobility. Every actual parameter is fixed before temperature tends to zero. A scaled-coordinate perturbation argument controls all continuous coordinates and actual whole-catalog redraws over the declared finite window; numerical thresholds and a native simulation were not supplied.

The first event produces two proper coherent components before handoff $h=.1$ with limiting probability $.02e^{-.1}$. The counterfactual has no redraw before handoff under the same process and data. The second event is existence of an episode starting in $[h,h+1]$ during which their union is exactly one proper component and maintains fitted-mean coherence for duration $.1$. It does not require persistence after an uncontrolled early first join. With fixed mean-coherence radius $1/20$, the construction obtains a conditional event-probability margin greater than $.3290$ and positive instantaneous Fisher-weighted mean-contrast curvature. The source checks seven exact scalar identities and its explicit finite margins separately from the general perturbation argument.

The selected island is seeded by its initial means and widths; this is not unseeded or every-initial-law formation. The same construction works with reward learning frozen, so learning is not established as causally necessary. The frozen-reward equilibrium control favors the fully active pattern; a proper transient block does not establish learned stationary recurrence or the required horizon condition. Source-assignment coherence, a hierarchy spanning growing size/depth, structural parent errors and full parent closure remain open. No full RG gate is claimed closed.

## Relevance to this research

These results refine [[Renormalization-group flow of beliefs]] by separating original-record loss from hidden-recognition filtering, and refine [[Staged hierarchy formation and RG composability]] by replacing an unspecified favorable bridge regime with an explicit prepared finite-window construction. Within [[Gauge-Theoretic Multi-Agent VFE Model]], the next gaps remain learning-compatible recurrence and horizons, the original initial-law quantifier, and a parent representation with controlled native path and conditional errors. No manuscript edit, new network experiment, GPU execution or retry of historical failures accompanied this batch.
