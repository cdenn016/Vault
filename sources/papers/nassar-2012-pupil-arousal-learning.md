---
type: paper
title: "Rational regulation of learning dynamics by pupil–linked arousal systems"
aliases:
  - "Nassar 2012"
  - "pupil-arousal learning rate"
authors:
  - Nassar, Matthew R.
  - Rumsey, Katherine M.
  - Wilson, Robert C.
  - Parikh, Kinjan
  - Heasly, Benjamin
  - Gold, Joshua I.
year: 2012
arxiv: null
url: https://doi.org/10.1038/nn.3130
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

# Rational regulation of learning dynamics by pupil–linked arousal systems

> [!info] Citation
> Nassar, M. R., Rumsey, K. M., Wilson, R. C., Parikh, K., Heasly, B., & Gold, J. I. (2012). "Rational regulation of learning dynamics by pupil–linked arousal systems." *Nature Neuroscience*, 15(7), 1040–1046. https://doi.org/10.1038/nn.3130

## TL;DR
This paper demonstrates that pupil diameter in humans performing a predictive-inference task encodes the two key variables of a reduced Bayesian model: change-point probability (reflected in phasic pupil changes) and relative uncertainty (reflected in baseline/average pupil diameter). These pupil-linked arousal signals, likely mediated by the locus coeruleus–norepinephrine system, causally regulate the learning rate used to update beliefs about a dynamically changing environment, consistent with the Yerkes–Dodson inverted-U relationship between arousal and learning.

## Problem & setting
When inferring the state of a dynamic process, an agent must distinguish between two sources of uncertainty: noise (random fluctuations around a stable mean, favouring averaging over history) and genuine change points (shifts in the mean itself, requiring rapid belief revision). The central question is how the brain tracks these distinct uncertainty sources and uses them to adaptively regulate the learning rate — the fraction of prediction error incorporated into an updated belief. Prior work (Nassar et al., 2010, J. Neurosci.) established that human subjects behave approximately Bayes-optimally in a predictive-inference task; the present study asks whether pupil-linked arousal systems implement this computation.

## Method
Thirty subjects performed an isoluminant predictive-inference task in which outcomes were drawn from a Gaussian distribution whose mean changed at random (hazard rate 0.1) and whose standard deviation was blocked (5 or 10). Learning rate was operationalised as the fraction of the prediction error absorbed into the next prediction (delta-rule: $B_{t+1} = B_t + \alpha \delta_t$). A reduced Bayesian model computed two trial-by-trial quantities:

- **Change-point probability** $\Omega_t$: posterior probability that the generative mean shifted on trial $t$, computed as a ratio of likelihoods under change vs. no-change hypotheses (scales monotonically with $|\delta_t|/\sigma$).
- **Relative uncertainty** $\tau_t$: variance about the estimated mean divided by total predictive variance (analogous to the Kalman gain); peaks at 0.5 immediately after a change point and decays as evidence accumulates.

The optimal learning rate combines both: $\alpha_t = \Omega_t + (1 - \Omega_t)\tau_t$. Pupil diameter was recorded at 120 Hz (infrared eye-tracker) during a 2 s iso-luminant outcome-viewing window, decomposed into pupil change (late minus early 1 s epoch) and pupil average. Linear regression related these pupil metrics to the model quantities. A causal manipulation (unexpected auditory-cue switches, task-irrelevant) artificially elevated pupil diameter and measured downstream effects on learning rate.

## Key results
Pupil change tracked change-point probability: larger phasic dilations occurred for outcomes with high change-point probability; the regression was significant in 15/30 subjects (small model) and 19/30 (large model). Pupil average tracked relative uncertainty: it peaked on the trial after each change point and decayed over subsequent trials, significant in 27/30 subjects. Neither metric showed a relationship with the other model variable (cross-validation within the regression framework confirmed dissociation). Individual differences in average learning rate were predicted by pupil dynamics (r = 0.59, p < 0.001), and trial-by-trial learning rates were predicted by the combined pupil model (r = 0.38, p < 0.001) across all subjects. The auditory arousal manipulation elevated both pupil metrics and increased learning rates selectively when baseline pupil diameter was low (consistent with the ascending limb of the Yerkes–Dodson curve), and had no effect or slightly decreased rates when baseline was high (descending limb).

## Relevance to this research
The reduced Bayesian model here is a concrete, tractable implementation of adaptive belief updating that parallels the VFE framework: change-point probability corresponds to a signal that a new prior is needed (analogous to the KL divergence between new evidence and current belief being anomalously large), while relative uncertainty maps onto the Kalman-gain-like weighting that governs how much a new observation updates the mean belief $\mu_q$. In the VFE transformer, the learning-rate analogue is the softmax attention weight $\beta_{ij}$, which is driven by the KL divergence terms $\mathrm{KL}(q_i \| \Omega_{ij} q_j)$; a high-surprise token (large KL) dominates the attention sum just as high change-point probability drives $\alpha \to 1$ here. The tonic/phasic locus coeruleus decomposition suggests a biological substrate that separates the two uncertainty channels, which resonates with the VFE framework's separation of the self-coupling term $\alpha \cdot \mathrm{KL}(q_i \| p_i)$ (tonic, prior-anchoring) from the pairwise coupling $\beta_{ij} \cdot \mathrm{KL}(q_i \| \Omega_{ij} q_j)$ (phasic, data-driven update). For multi-agent active inference the paper also provides a normative account of how an agent's arousal state should be represented as a hyper-prior over hazard rate, analogous to the hyper-prior $h$ in the VFE hierarchy.

## Cross-links
- Concepts: [[Variational Free Energy]], [[Belief Updating]], [[Kalman Filter]], [[Active Inference]]
- Related sources: [[nassar-2010-bayesian-delta-rule]] [[wilson-2010-bayesian-hazard-rate]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{nassar2012,
  author  = {Nassar, Matthew R. and Rumsey, Katherine M. and Wilson, Robert C. and Parikh, Kinjan and Heasly, Benjamin and Gold, Joshua I.},
  title   = {Rational regulation of learning dynamics by pupil--linked arousal systems},
  journal = {Nature Neuroscience},
  year    = {2012},
  volume  = {15},
  number  = {7},
  pages   = {1040--1046},
  doi     = {10.1038/nn.3130},
}
```
