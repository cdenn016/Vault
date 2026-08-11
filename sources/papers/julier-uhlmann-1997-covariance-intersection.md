---
type: paper
title: "A Non-divergent Estimation Algorithm in the Presence of Unknown Correlations"
aliases:
  - "Julier and Uhlmann 1997 covariance intersection"
  - "Covariance intersection (CI)"
authors:
  - Julier, Simon J.
  - Uhlmann, Jeffrey K.
year: 1997
arxiv: null
doi: 10.1109/ACC.1997.609105
url: https://doi.org/10.1109/ACC.1997.609105
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
  - field/cs-ml
  - field/mathematics
created: 2026-08-10
---

# A Non-divergent Estimation Algorithm in the Presence of Unknown Correlations

> [!info] Citation
> Simon J. Julier and Jeffrey K. Uhlmann (1997). "A Non-divergent Estimation Algorithm in the Presence of Unknown Correlations." *Proceedings of the 1997 American Control Conference*, vol. 4, 2369--2373. DOI: [10.1109/ACC.1997.609105](https://doi.org/10.1109/ACC.1997.609105).

## TL;DR

Covariance intersection fuses Gaussian estimates conservatively when their unknown cross-correlation makes an ordinary Kalman fusion unsafe. It trades optimality for consistency: the reported covariance remains a valid uncertainty bound without reconstructing the missing cross-covariance.

## Problem & setting

Two estimators describe the same state by means and covariances, but the correlation between their errors is unknown. This is common in decentralized systems because information can travel through multiple paths and return to a node. Treating the estimates as independent can then double count evidence and produce an overconfident, potentially divergent filter.

## Method

For a scalar weight $\omega\in[0,1]$, covariance intersection combines information matrices and information vectors as
$$
P_{\mathrm{CI}}^{-1}=\omega P_1^{-1}+(1-\omega)P_2^{-1},\qquad
P_{\mathrm{CI}}^{-1}m_{\mathrm{CI}}=\omega P_1^{-1}m_1+(1-\omega)P_2^{-1}m_2.
$$
The weight can be selected to minimize a scalar measure of the fused covariance while preserving the consistency guarantee.

## Key results

The paper proves that the CI estimate is consistent regardless of the actual unknown correlation and illustrates why a standard Kalman fusion can fail in the same decentralized setting. CI does not recover the exact Bayesian posterior and can be conservative; its guarantee is a robust bound under missing correlation information.

## Relevance to this research

This is the foundational source for [[Conservative information fusion]]. It provides a mandatory negative control whenever MultiAgentELBO treats peer beliefs as evidence: if peers share priors, observations, ancestors, or prior messages, their errors are correlated. A Gaussian KL or product pool is exact only under additional information-lineage assumptions. CI tests the cost of refusing to invent those assumptions.

## Cross-links

- Concepts: [[Conservative information fusion]], [[Probabilistic opinion pooling]], [[Decentralized Bayesian inference]]
- Related sources: [[battistelli-chisci-2014-kl-density-consensus]], [[bandyopadhyay-chung-2018-logop-filtering]]

## BibTeX

```bibtex
@inproceedings{JulierUhlmann1997,
  author    = {Julier, Simon J. and Uhlmann, Jeffrey K.},
  title     = {A Non-divergent Estimation Algorithm in the Presence of Unknown Correlations},
  booktitle = {Proceedings of the 1997 American Control Conference},
  volume    = {4},
  pages     = {2369--2373},
  year      = {1997},
  doi       = {10.1109/ACC.1997.609105}
}
```
