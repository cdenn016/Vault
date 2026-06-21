---
type: paper
title: "Functionally dissociable influences on learning rate in a dynamic environment"
aliases:
  - "McGuire 2014"
  - "Adaptive learning rate dissociation"
authors:
  - McGuire, Joseph T.
  - Nassar, Matthew R.
  - Gold, Joshua I.
  - Kable, Joseph W.
year: 2014
arxiv: null
url: https://doi.org/10.1016/j.neuron.2014.10.013
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

# Functionally dissociable influences on learning rate in a dynamic environment

> [!info] Citation
> McGuire, J. T., Nassar, M. R., Gold, J. I., & Kable, J. W. (2014). "Functionally dissociable influences on learning rate in a dynamic environment." *Neuron*, 84(4), 870–881. https://doi.org/10.1016/j.neuron.2014.10.013

## TL;DR
Using fMRI and computational modeling in a spatial-prediction task, this paper decomposes adaptive learning into three functionally and neuroanatomically distinct components: surprise-driven updating (change-point probability, CPP), uncertainty-driven updating (relative uncertainty, RU), and a context-inappropriate reward-driven bias. These factors dissociate both behaviorally and in terms of their neural correlates, yet converge on a core set of regions including dorsomedial frontal cortex (DMFC) that collectively govern adaptive belief updating.

## Problem & setting
Decision-making in non-stationary environments requires agents to dynamically modulate how much they weight new observations against prior beliefs. The learning rate in a simple delta rule should scale with how surprising an observation is (CPP) and how uncertain the current belief is (RU). While prior work identified DMFC as a correlate of adaptive learning, the field lacked a rigorous dissociation of the distinct computational influences on learning rate and their separate neural substrates. The task involved 32 human participants predicting the location of a hidden helicopter from sequentially dropped bags, with orthogonal manipulations of observation noise and reward salience.

## Method
An approximately Bayesian normative model (from Nassar et al. 2010, 2012) computes trial-wise learning rate as:

$$\alpha_t = \Omega_t + (1 - \Omega_t)\,\tau_t$$

where $\Omega_t$ is change-point probability (CPP) and $\tau_t$ is relative uncertainty (RU). CPP is computed from the likelihood ratio of the current observation under the stable vs. change-point hypothesis (with fixed hazard rate $H = 0.1$). RU is a Kalman-filter-like quantity — the fraction of total predictive uncertainty attributable to imprecision in the helicopter location estimate rather than observation noise. These model-derived regressors, plus a reward-value binary, were entered as amplitude modulators in a voxelwise fMRI GLM. Behavioral analysis used linear regression of trial-wise bucket updates on $\delta \times \text{CPP}$, $\delta \times (1-\text{CPP}) \times \text{RU}$, and reward value.

## Key results
Behaviorally, participants modulated learning rates with CPP (median coefficient 0.53) and RU (median 0.32), and showed a small but significant reward-driven bias (median 0.03) despite its normative irrelevance. In fMRI: CPP drove selective BOLD responses in primary and higher-order visual cortex; RU drove selective responses in anterior PFC (aPFC), posterior parietal cortex, and cerebellum; reward value selectively engaged ventral striatum. All three factors converged in a set of common adaptive learning-rate regions: bilateral occipitoparietal cortex, bilateral anterior insula, DMFC (near pre-SMA), and posterior cingulate cortex. Task-dependent psychophysiological interaction (PPI) analyses confirmed that the common regions showed stronger functional connectivity with the CPP-selective occipital cluster when CPP dominated learning, and with the RU-selective aPFC cluster when RU dominated. Individual differences in BOLD responsiveness to CPP and RU in the common regions explained 44% of between-subject behavioral variance; DMFC was the strongest single predictor (r = 0.47 after Bonferroni correction).

## Relevance to this research
This paper is directly relevant to the VFE transformer's free-energy framework in several respects. First, the two normative factors CPP and RU correspond precisely to the two information-theoretic terms that govern Bayesian belief updating: CPP is proportional to a KL divergence or prediction error (the surprise term that appears in the self-coupling $\alpha \cdot \text{KL}(q_i \| p_i)$ when the prior shifts), while RU maps onto belief uncertainty — the variance of $q_i$ relative to the prior. The VFE canonical free energy contains both a self-coupling KL term and belief uncertainty (through the Gaussian belief tuple $(\mu, \Sigma, \phi)$), providing a formal link. Second, the convergence of CPP and RU signals in DMFC mirrors the convergence of free-energy gradient terms at a shared inference system — in the VFE multi-agent model, this corresponds to the aggregation of per-token belief updates into a common coupling term. Third, the dissociable factor-specific pathways (visual cortex for CPP, aPFC/parietal for RU, striatum for reward) are suggestive of a hierarchical or modular architecture consistent with the VFE hierarchy $h \to s \to p \to q \to \text{observations}$. Fourth, the reward-driven bias — a context-inappropriate tendency that nonetheless propagates to the common learning-rate system — is an empirical instance of the kind of non-normative influence that the VFE framework can model by including an observation-likelihood term that conflates task-relevant and task-irrelevant signals.

## Cross-links
- Concepts: [[Variational Free Energy]], [[Bayesian Belief Updating]], [[Change-Point Detection]], [[Relative Uncertainty]]
- Related sources: [[nassar2010-approximately-bayesian]], [[behrens2007-learning-value-information]]
- Manuscript/Project: [[VFE Transformer Program]], [[multi-agent active inference]]

## BibTeX
```bibtex
@article{mcguire2014,
  author  = {McGuire, Joseph T. and Nassar, Matthew R. and Gold, Joshua I. and Kable, Joseph W.},
  title   = {Functionally dissociable influences on learning rate in a dynamic environment},
  journal = {Neuron},
  year    = {2014},
  volume  = {84},
  number  = {4},
  pages   = {870--881},
  doi     = {10.1016/j.neuron.2014.10.013},
}
```
