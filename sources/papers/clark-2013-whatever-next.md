---
type: paper
title: "Whatever Next? Predictive Brains, Situated Agents, and the Future of Cognitive Science"
aliases:
  - "Clark 2013"
  - "Whatever Next"
authors:
  - Clark, Andy
year: 2013
arxiv: null
url: https://doi.org/10.1017/S0140525X12002142
tags:
  - cluster/vfe
  - project/multi-agent
  - field/neuroscience
  - field/philosophy
  - field/psychology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Whatever Next? Predictive Brains, Situated Agents, and the Future of Cognitive Science

> [!info] Citation
> Clark, Andy (2013). "Whatever Next? Predictive Brains, Situated Agents, and the Future of Cognitive Science." *Behavioral and Brain Sciences*, 36(3), 181–204. https://doi.org/10.1017/S0140525X12002142

## TL;DR

Clark argues that the brain is fundamentally a hierarchical prediction machine: it continuously generates top-down predictions about sensory inputs and updates its internal models by minimizing prediction error (free energy). This predictive processing (PP) framework, which Clark traces from Helmholtz through Rao & Ballard to Friston, unifies perception, action, and attention under a single principle and challenges classical sandwich models of mind in which perception and action are separated by central cognition.

## Problem & setting

Classical cognitive science treats perception as stimulus-driven bottom-up processing and action as a downstream consequence of completed percepts. Clark surveys mounting evidence that this picture is inverted: neural responses are better described as error signals correcting top-down generative predictions than as feature detectors. The key challenge is to show how a single predictive hierarchy can account not only for passive perception but also for motor control, attention, and the sense of embodied agency, all without positing dedicated intermediate representational stages.

## Method

The paper is a synthetic theoretical review rather than an empirical study. Clark integrates Helmholtz's unconscious inference, the Rao-Ballard (1999) predictive-coding network model, and Friston's free-energy principle into a unified predictive processing (PP) account. The core mechanism is hierarchical message-passing: higher levels send down predictions (priors) and lower levels send up only the residual prediction errors. Mathematically the brain minimizes variational free energy $F = D_\text{KL}[q(\theta)\,\|\,p(\theta|s)] - \log p(s)$, where $q$ is the approximate posterior over hidden causes $\theta$ and $s$ is sensory input --- equivalent to maximizing model evidence (minimizing surprise) while bounding intractable posterior inference. Action enters through active inference: rather than updating beliefs to match prediction errors, the organism can also emit motor commands that bring sensory data into alignment with predictions, closing the loop without a separate motor controller.

## Key results

Clark identifies five core claims of PP: (1) the brain encodes a hierarchical generative model of its sensory stream; (2) perception is Bayesian inference within that model; (3) prediction errors, not raw stimuli, are the primary bottom-up signal; (4) attention is precision-weighting of prediction errors; and (5) action is active inference --- motor predictions that are fulfilled by movement. He argues these five claims jointly explain a wide range of phenomena including binocular rivalry, the hollow mask illusion, sensory attenuation of self-generated stimuli, and psychopathology (hallucination as uncorrected prior, autism as overly precise sensory weighting). The target article attracted 26 peer commentaries, making it a de facto field-defining position paper on predictive processing.

## Relevance to this research

This paper is the canonical tutorial and conceptual foundation for predictive coding as free energy minimization, directly underpinning both the VFE Transformer program and the multi-agent active inference model. Several specific connections are load-bearing.

Variational free energy as the unifying objective. Clark's expression $F = D_\text{KL}[q\|p] - \log p(s)$ is the single-layer instance of the multi-level belief-coupling free energy used in the VFE transformer ($F = \alpha\,\text{KL}(q_i\|p_i) + \lambda_h\,\text{KL}(s_i\|h) + \sum_{ij}[\beta_{ij}\,\text{KL}(q_i\|\Omega_{ij}q_j) + \tau\beta_{ij}\log(\beta_{ij}/\pi_{ij})] - \mathbb{E}_q[\log p(o|x)]$). The hyper-prior term and the self-coupling term are direct extensions of Clark's hierarchy to the gauge-equivariant multi-agent setting.

Attention as precision weighting. Clark's identification of attention with the precision (inverse variance) of prediction errors is the conceptual ancestor of the SPD belief geometry in the VFE transformer, where $\Sigma^{-1}$ modulates the effective coupling weight between agents and the GL(K) transport $\Omega_{ij}$ rotates beliefs before comparison.

Active inference closing perception-action. The active inference loop (an agent moves to fulfill its own predictions) motivates the multi-agent model's treatment of belief updates and inter-agent message passing as two sides of the same VFE minimization --- agents do not passively receive social signals but act to bring their beliefs into predictive alignment with neighbors.

Hierarchical generative models. The $h \to s \to p \to q \to o$ hierarchy in the VFE transformer (hyper-prior to models to priors to beliefs to observations) directly instantiates Clark's predictive hierarchy in Gaussian exponential family form with gauge-equivariant transport between levels.

## Cross-links

- Concepts: [[Predictive processing and controlled hallucination]], [[Variational free energy]], [[Collective active inference]], [[Multi-agent variational free energy]]
- Related sources: [[rao-1999-predictive-coding]], [[friston-2010-free-energy-principle]], [[friston-2016-active-inference-learning]], [[friston-2019-particular-physics]], [[bogacz-2017-free-energy-tutorial]], [[smith-2022-active-inference-tutorial]]
- Methods: [[Free-energy principle active inference]], [[Predictive coding network]]
- Manuscript/Project: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{Clark2013,
  author  = {Clark, Andy},
  title   = {Whatever Next? {P}redictive Brains, Situated Agents, and the Future of Cognitive Science},
  journal = {Behavioral and Brain Sciences},
  year    = {2013},
  volume  = {36},
  number  = {3},
  pages   = {181--204},
  doi     = {10.1017/S0140525X12002142},
}
```
