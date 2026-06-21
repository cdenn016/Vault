---
type: paper
title: "The graphical brain: Belief propagation and active inference"
aliases:
  - "graphical brain"
authors:
  - Friston, Karl J.
  - Parr, Thomas
  - de Vries, Bert
year: 2017
arxiv: null
url: https://doi.org/10.1162/netn_a_00018
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
  - field/neuroscience
  - field/cs-ml
  - field/statistics
  - field/physics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The graphical brain: Belief propagation and active inference

> [!info] Citation
> Friston, K. J., Parr, T., & de Vries, B. (2017). "The graphical brain: Belief propagation and active inference." *Network Neuroscience*, 1(4), 381–414. https://doi.org/10.1162/netn_a_00018

## TL;DR
This paper formulates neuronal processing as belief propagation under deep generative models using Forney (normal) factor graphs, deriving the requisite message-passing schedules for both discrete (categorical/Markov decision process) and continuous (generalized coordinates of motion) state spaces. A key technical contribution is the linking of discrete and continuous representations through Bayesian model averaging and comparison, proposed to be implemented in thalamocortical loops. The result is a principled computational connectome grounded in variational free energy minimization that maps onto canonical cortical microcircuits.

## Problem & setting
The paper addresses the question of what form of neuronal message passing is entailed by active inference — the principle that brains minimize variational free energy (equivalently, maximize Bayesian model evidence) through both perception and action. Prior work on predictive coding handled continuous states, while discrete state-space (MDP) formulations handled categorical latents; these two regimes ran on separate formalisms. The challenge is to unify them in a single computational architecture and map the result onto known neuroanatomy.

## Method
The authors employ Forney factor graphs as the organizing formalism. For discrete generative models (MDP-based), belief propagation is derived as a softmax-update over hidden state expectations that combines forward messages (empirical prior from past), backward messages (empirical prior from future), and likelihood messages from observations — equivalent to a Bayesian smoother operating before all outcomes are seen. For continuous models, a generalized Bayesian filter is derived using generalized coordinates of motion (position, velocity, acceleration, jerk, ...), yielding prediction-error gradient descent equations of the form:

$$\dot{\tilde{\mu}}_x - \Delta\tilde{\mu}_x = \partial_{\tilde{x}}\tilde{g}\cdot\Pi_o\tilde{\varepsilon}_o + \partial_{\tilde{x}}\tilde{f}\cdot\Pi_x\tilde{\varepsilon}_x - \Delta^{\top}\Pi_x\tilde{\varepsilon}_x$$

Mixed (discrete + continuous) generative models are linked via a Bayesian model averaging factor, where posterior beliefs about discrete causes provide empirical priors over continuous dynamics, and continuous evidence is compressed into discrete posteriors by Bayesian model comparison. Policy selection uses expected free energy $G(\pi,\tau) = -\mathbb{E}[\ln Q(s_\tau|o_\tau,\pi) - \ln Q(s_\tau|\pi)] - \mathbb{E}[\ln Q(o_\tau)]$, decomposing into epistemic (information gain) and pragmatic (prior preference) value.

## Key results
The Forney factor graph representation reveals that forward, backward, and likelihood messages in discrete models map onto identifiable neural populations: state prediction errors (granular layers), expected states (supragranular pyramidal cells), and outcome prediction errors (infragranular layers projecting to subcortical structures). The formal equivalence between representations of future trajectories in discrete models and generalized motion in continuous models is demonstrated explicitly. Bayesian model averaging linking hierarchical levels requires policy expectations (expected free energy) to gate descending empirical priors — a cortico-basal ganglia-thalamic circuit interpretation. Simulations of pictographic reading illustrate how discrete semantic inferences and continuous visuomotor sampling (saccades) are integrated through this architecture.

## Relevance to this research
This paper is directly relevant to the VFE transformer program on multiple levels. The variational free energy objective and the belief-update equations (gradient descent on marginal free energy, prediction-error dynamics) are the continuous precursors of the discrete belief-tuple updates $(\mu, \Sigma, \phi)$ in the VFE transformer's E-step. The factor-graph message-passing schedule — forward, backward, likelihood, and policy-expectation messages — provides a principled template for the inter-layer and cross-agent information flow in both the single-agent transformer and the multi-agent active inference model. The Bayesian model averaging link between levels is structurally analogous to the VFE transformer's hierarchical belief propagation across token positions. Expected free energy's decomposition into epistemic and pragmatic value is the same decomposition invoked in the multi-agent free energy (the lambda_h hyper-prior term and the attention-coupling KL terms). The derivation of softmax attention as the stationary point of a free energy with an entropy regularizer (the tau*beta*log(beta/pi) term in the VFE functional) is foreshadowed by the policy-selection equations here.

## Cross-links
- Concepts: [[Variational Free Energy]], [[Active Inference]], [[Belief Propagation]], [[Predictive Coding]], [[Expected Free Energy]]
- Related sources: [[friston-2016-active-inference-learning|friston2016active]], [[friston-2023-fep-simpler|friston2022free]], [[parr-2022-active-inference|parr2022active]]
- Manuscript/Project: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model|MAgent Model]]

## BibTeX
```bibtex
@article{friston2017graphical,
  author  = {Friston, Karl J. and Parr, Thomas and de Vries, Bert},
  title   = {The graphical brain: Belief propagation and active inference},
  journal = {Network Neuroscience},
  year    = {2017},
  volume  = {1},
  number  = {4},
  pages   = {381--414},
  doi     = {10.1162/netn_a_00018},
}
```
