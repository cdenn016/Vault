---
type: paper
title: "An Approximately Bayesian Delta-Rule Model Explains the Dynamics of Belief Updating in a Changing Environment"
aliases:
  - "Nassar 2010"
  - "reduced Bayesian delta-rule"
authors:
  - Nassar, Matthew R.
  - Wilson, Robert C.
  - Heasly, Benjamin
  - Gold, Joshua I.
year: 2010
arxiv: null
url: https://doi.org/10.1523/JNEUROSCI.0822-10.2010
tags:
  - cluster/vfe
  - project/multi-agent
  - field/neuroscience
  - field/psychology
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# An Approximately Bayesian Delta-Rule Model Explains the Dynamics of Belief Updating in a Changing Environment

> [!info] Citation
> Nassar, M. R., Wilson, R. C., Heasly, B., & Gold, J. I. (2010). "An Approximately Bayesian Delta-Rule Model Explains the Dynamics of Belief Updating in a Changing Environment." *Journal of Neuroscience*, 30(37), 12366–12378. https://doi.org/10.1523/JNEUROSCI.0822-10.2010

## TL;DR
Human subjects updating beliefs in a noisy, volatile environment modulate learning rates trial-by-trial in a manner consistent with a reduced Bayesian ideal-observer model. This reduced model collapses the full run-length posterior to a single expected run length and change-point probability, yielding a computationally tractable delta-rule whose learning rate is analytically expressible. Individual differences across subjects are captured by a single prior parameter — the subjective hazard rate — which governs the expected frequency of environmental change points.

## Problem & setting
In dynamic environments, an agent must decide how much influence new observations should have on existing beliefs: outcomes surprising because the environment has structurally changed (volatility) should carry more weight than outcomes surprising merely due to persistent stochasticity (noise). Prior work (Behrens et al., 2007) showed that humans elevate learning rates during volatile periods on average, but relied on model fitting to group behavior. Nassar et al. developed a novel estimation task providing trial-by-trial learning-rate measurements, enabling direct comparison of individuals against both the full Bayesian ideal observer and simplified approximations.

## Method
Subjects sequentially predicted numbers drawn from a Gaussian whose mean changed at unsignaled change points (hazard rate H = 0.04) and whose SD varied across blocks (5, 15, 25, 35). The fraction of the prediction error used to update each estimate directly measured the learning rate alpha_t.

The full Bayesian model tracks the joint distribution over generative mean and run length r (number of trials since the last change point), maintained via a message-passing algorithm requiring O(t) nodes after t trials. The **reduced Bayesian model** instead tracks a single expected run length r-hat and change-point probability Omega_t:

```
Omega_t = [U(X_t | 0,300) * H] / [U(X_t | 0,300) * H + N(X_t | mu-hat_t, sigma-hat_t^2) * (1-H)]
```

The mean update collapses to a delta rule:
```
mu-hat_t = mu-hat_{t-1} + alpha_t * delta_t
alpha_t  = (1 + Omega_t * r-hat_t) / (r-hat_t + 1)
r-hat_{t+1} = (r-hat_t + 1)(1 - Omega_t) + Omega_t
```

The predictive variance is sigma-hat_t^2 = N^2 + N^2/r-hat_t, combining irreducible noise with run-length-dependent uncertainty about the mean. Extended variants infer noise online and introduce a likelihood-weighting parameter lambda (0 to 1) attenuating change-point sensitivity, or a drift variance D modeling perceived mean drift (Kalman-filter element).

## Key results
Subjects used trial-by-trial learning rates spanning [0, 1], with rates increasing as a function of z-scored prediction error and decaying gradually over many trials following change points — neither consistent with a fixed learning rate nor with abrupt post-change-point resets. The reduced Bayesian model qualitatively reproduced both trends using the hazard rate H as a single free parameter per block. Best-fitting hazard rates correlated strongly with mean learning rates across subjects (r = 0.84, p < 0.001) and were systematically higher than the true task hazard rate (0.04), indicating subjects overestimate environmental volatility. A three-parameter model adding drift D and likelihood weight lambda provided better quantitative fits (BIC) than the single-parameter reduced model for all 30 subjects. The hazard-rate prior accounted for a counterintuitive individual-difference finding: subjects with higher average learning rates were more confident (smaller confidence windows), explained by chronic underestimation of noise under high hazard-rate priors.

## Relevance to this research
The reduced Bayesian delta-rule is directly structurally analogous to the VFE belief-update equations: both express posterior mean updating as a weighted combination of prior belief and new evidence, with weights determined by surprise relative to expected uncertainty. The change-point probability Omega_t plays the role of the attention weight beta_ij in the VFE transformer — a Bayesian posterior over "is this new observation informative enough to override the prior run?" The run-length r-hat is the VFE analog of accumulated evidence that drives the KL self-coupling alpha_i: as r-hat grows, the belief concentrates and the effective learning rate 1/(r-hat+1) shrinks, mirroring the stabilizing effect of a tight posterior sigma_q in the VFE E-step. The hazard rate H is a prior over environmental change that functions precisely as a hyperprior h in the VFE hierarchy (h -> s -> p -> q), setting the meta-level expectation that drives model coupling lambda_h. The individual-variability account via subjective hazard rates is a concrete empirical grounding for the heterogeneous coupling strengths gamma_ij in multi-agent active inference, where agents with different priors over volatility naturally develop different coupling weights to neighbors. This paper provides a neuroscientific behavioral validation that approximate Bayesian inference (rather than exact inference) underlies human belief dynamics, directly motivating the VFE transformer's iterative approximate E-step rather than a closed-form Kalman filter.

## Cross-links
- Concepts: [[Variational Free Energy]], [[Active Inference]], [[Belief Updating]], [[Predictive Coding]]
- Related sources: [[behrens2007-learning-value-information]], [[wilson2010-bayesian-online-hazard]]
- Manuscript/Project: [[VFE Transformer Program]], [[MAgent Model]]

## BibTeX
```bibtex
@article{nassar2010,
  author  = {Nassar, Matthew R. and Wilson, Robert C. and Heasly, Benjamin and Gold, Joshua I.},
  title   = {An Approximately {Bayesian} Delta-Rule Model Explains the Dynamics of Belief Updating in a Changing Environment},
  journal = {Journal of Neuroscience},
  year    = {2010},
  volume  = {30},
  number  = {37},
  pages   = {12366--12378},
  doi     = {10.1523/JNEUROSCI.0822-10.2010},
}
```
