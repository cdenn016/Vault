---
type: paper
title: "Whatever next? Predictive brains, situated agents, and the future of cognitive science"
aliases:
  - "Clark 2013"
  - "Whatever Next"
  - "Predictive Brains"
authors:
  - Clark, Andy
year: 2013
arxiv: null
url: https://doi.org/10.1017/S0140525X12000477
tags:
  - cluster/participatory/philosophy-of-mind
  - project/multi-agent
  - field/neuroscience
  - field/philosophy
  - field/cs-ml
  - field/psychology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Whatever next? Predictive brains, situated agents, and the future of cognitive science

> [!info] Citation
> Clark, Andy (2013). "Whatever next? Predictive brains, situated agents, and the future of cognitive science." *Behavioral and Brain Sciences*, 36, 181–253. https://doi.org/10.1017/S0140525X12000477

## TL;DR
Clark argues that brains are fundamentally prediction machines implementing hierarchical predictive coding: top-down generative models continuously predict sensory inputs, and only residual prediction errors propagate upward. This "hierarchical predictive processing" account, extended to action via active inference, offers a unifying framework for perception, cognition, attention, and action under the banner of free-energy minimization. The paper critically examines the framework's virtues, challenges, and broader implications for mind, agency, and cognitive science.

## Problem & setting
The central problem is understanding how the brain — a black box with access only to its own internal states — comes to accurately represent and act upon the world. Prior work in Helmholtz's analysis-by-synthesis tradition, the Helmholtz Machine (Dayan et al. 1995), predictive coding in signal processing, and Rao & Ballard (1999)'s hierarchical visual cortex model all set the stage. The paper synthesizes this lineage with Friston's free-energy principle and action-oriented extensions, asking whether prediction-error minimization can serve as the single organizing principle for a unified science of mind.

## Method
This is a theoretical and review target article (with 25 invited commentaries and rejoinder, published separately in *Frontiers in Theoretical and Philosophical Psychology*). The core architecture is a bidirectional hierarchical generative model: top-down backward connections carry predictions; bottom-up forward connections carry precision-weighted prediction errors. Key mechanisms surveyed include:

- **Hierarchical predictive coding**: each cortical level predicts activity at the level below; only the residual error propagates upward. Formally, the system minimizes surprisal (negative log-evidence), bounded above by variational free energy $F = \text{KL}[q \| p] - \log p(o)$, where $q$ is the approximate posterior and $p(o)$ the model evidence.
- **Duplex architecture**: functionally distinct "representation units" (encoding conditional expectations of causes; deep pyramidal cells, conveying top-down predictions) and "error units" (encoding precision-weighted prediction errors; superficial pyramidal cells, conveying forward error signals).
- **Attention as precision-weighting**: attention modulates the gain on error units, controlling the relative influence of top-down priors versus bottom-up evidence at each level.
- **Action-oriented predictive processing / active inference**: motor intentions are predictions about proprioceptive consequences; prediction errors at the motor level self-suppress by eliciting movement rather than updating beliefs, making perception and action computationally unified.
- **Free-energy principle**: all quantities of an adaptive system change to minimize an information-theoretic analog of thermodynamic free energy, providing a normative grounding for prediction-error minimization.

## Key results
The paper is a theoretical review rather than an empirical study; its principal claims and supporting evidence are:

1. A variety of indirect neural evidence supports hierarchical predictive coding: non-classical receptive field effects (surround suppression explained as error signaling), repetition suppression (reduced by unexpectedness, consistent with predictability reducing error), and biphasic response dynamics in LGN neurons, all accounted for by predictive coding simulations (Rao & Ballard 1999; Jehee & Ballard 2009).
2. fMRI results (Murray et al. 2002; Alink et al. 2010; Egner et al. 2010) show that FFA responses are better characterized as a sum of feature expectation and surprise signals than as bottom-up feature detection, supporting the duplex representation/error-unit architecture.
3. Behavioral evidence for Bayesian optimality (Weiss et al. 2002; Ernst & Banks 2002; Körding et al. 2007) aligns with the Bayesian brain hypothesis implemented by hierarchical predictive processing.
4. Binocular rivalry (Hohwy et al. 2008) is neatly explained as competition between top-down hypotheses in a double-well energy landscape where no single hypothesis explains all sensory data.
5. The framework naturally extends to situated agency, multi-agent coordination, and cultural niche construction: organisms structure their environments to reduce mutual prediction error, and socio-cultural "designer environments" feed back into cortical generative model learning.
6. Scope limits: the framework does not on its own specify the full human cognitive architecture (representational formats, exploit–explore trade-offs, or the precise mechanisms of subcortical and evolutionary kluges).

## Relevance to this research
This paper is foundational background for the VFE transformer program. Several connections are direct:

- **Variational free energy**: Clark's exposition of Friston's free-energy principle (section 1.6) directly motivates the VFE transformer's objective — beliefs $q$ minimizing $F = \alpha \cdot \text{KL}(q \| p) + \text{coupling terms} - \mathbb{E}_q[\log p(o|x)]$. The "surprisal" minimization framing maps onto the observation likelihood term in the VFE functional.
- **Hierarchical belief structure**: Clark's $h \to s \to p \to q \to o$ intuition (hyper-priors, models, priors, beliefs, observations) precisely matches the VFE transformer's belief hierarchy and the $\lambda_h \cdot \text{KL}(s_i \| h)$ hyper-prior term.
- **Precision-weighted attention**: The identification of attention with precision-weighted gain on error units is the predecessor of the VFE transformer's $\beta_{ij}$ attention weights derived as stationary points of the free-energy functional — both mechanize attention as uncertainty-modulated belief coupling.
- **Active inference**: The action-oriented extension (section 1.5) grounds the multi-agent active inference framing in the MAgent_Model, where agents reduce mutual prediction error through coordinated action.
- **Participatory realism**: Clark's section 3.4 on situated agents, cultural niche construction, and "designer environments" resonates with the participatory realism / "it from bit" perspective developed in the PIFB manuscript — agents do not merely passively represent the world but co-constitute it through prediction-error minimizing action.
- **GL(K) attention**: The duplex representation/error-unit architecture motivates the VFE transformer's separation of mean ($\mu$) and precision ($\Sigma^{-1}$) belief parameters, and the role of gauge-equivariant transport $\Omega_{ij}$ in comparing beliefs across positions parallels the hierarchical top-down predictive cascade.

## Cross-links
- Concepts: [[Predictive Coding]] · [[Variational Free Energy]] · [[Active Inference]] · [[Attention as Precision]] · [[Hierarchical Generative Model]]
- Related sources: [[friston-2010-free-energy]] · [[rao-ballard-1999]] · [[hohwy-2013-predictive-mind]]
- Manuscript/Project: [[VFE Transformer Program]] · [[GL(K) Attention Manuscript]] · [[PIFB Manuscript]]

## BibTeX
```bibtex
@article{Clark2013,
  author  = {Clark, Andy},
  title   = {Whatever next? {Predictive} brains, situated agents, and the future of cognitive science},
  journal = {Behavioral and Brain Sciences},
  year    = {2013},
  volume  = {36},
  number  = {3},
  pages   = {181--253},
  doi     = {10.1017/S0140525X12000477},
}
```
