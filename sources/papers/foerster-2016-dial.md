---
type: paper
title: "Learning to Communicate with Deep Multi-Agent Reinforcement Learning"
aliases:
  - Foerster 2016
  - DIAL
  - RIAL
  - foerster2016learning
authors:
  - Foerster, Jakob N.
  - Assael, Yannis M.
  - de Freitas, Nando
  - Whiteson, Shimon
year: 2016
arxiv: "1605.06676"
url: https://arxiv.org/abs/1605.06676
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Learning to Communicate with Deep Multi-Agent Reinforcement Learning

> [!info] Citation
> Foerster, J. N., Assael, Y. M., de Freitas, N., & Whiteson, S. (2016). "Learning to Communicate with Deep Multi-Agent Reinforcement Learning." arXiv:1605.06676.

## TL;DR
This paper introduces two end-to-end learning algorithms — Reinforced Inter-Agent Learning (RIAL) and Differentiable Inter-Agent Learning (DIAL) — for cooperative multi-agent systems that must discover communication protocols from scratch. DIAL's key innovation is allowing real-valued gradients to flow across agents through the communication channel during centralised training, while execution remains decentralised with discretised binary messages. Experiments on riddle and vision tasks show DIAL substantially outperforms RL-only baselines, particularly when multi-step information integration is required.

## Problem & setting
Multiple cooperative agents must jointly maximise a shared discounted reward in partially observable environments where no communication protocol is given a priori. Each agent observes only a private observation correlated with the hidden Markov state and may communicate through a discrete limited-bandwidth channel. The agents must simultaneously discover how to encode and decode messages — a coordination problem with an exponentially large joint policy space that is intractable for classical global optimisation. Prior work either assumed fixed protocols or used tabular/evolutionary methods that do not scale to complex environments with raw observations.

## Method
Two algorithms are proposed under a centralised-learning / decentralised-execution paradigm. RIAL pairs Deep Recurrent Q-Networks (DRQN) with independent Q-learning: each agent learns separate Q-functions for environment actions and communication actions, with optional parameter sharing across agents. DIAL goes further by replacing discrete communication actions during centralised training with direct real-valued connections between agents' C-Networks. Messages pass through a Discretise/Regularise Unit (DRU): during training, $\hat{m} = \text{Logistic}(\mathcal{N}(m, \sigma))$; during decentralised execution, $\hat{m} = \mathbf{1}\{m > 0\}$. This makes the channel differentiable, so the downstream DQN error is backpropagated from recipient to sender: the message gradient chain $\mu^a_t$ accumulates $\partial(\Delta Q^{a'}_{t+1})^2 / \partial \hat{m}^a_t$ across time. The Gaussian noise $\sigma$ regularises the channel to encourage natural discretisation. The model architecture uses GRU-based RNNs with shared parameters, batch normalisation on incoming messages, and separate output heads for Q-values and messages.

## Key results
On the Switch Riddle with $n=3$ agents, all methods (RIAL and DIAL, with and without parameter sharing) reach near-optimal policy within 5k episodes, substantially outperforming a no-communication baseline. At $n=4$, DIAL with parameter sharing uniquely converges to near-optimal, while RIAL without parameter sharing fails to beat the no-communication baseline. On the two MNIST-based games (Colour-Digit MNIST and Multi-Step MNIST, 5 steps, 1 bit per step), RIAL completely fails to learn on Multi-Step MNIST while DIAL achieves near-optimal performance by propagating gradients across four agent-to-agent hops. The reason is structural: when rewards are antisymmetric the scalar TD error cancels in expectation (paper eq. 3), so RIAL receives no informative learning signal, whereas the inter-agent gradient through the channel (eq. 4) does not cancel and remains informative — the analytic case for differentiable over reinforced communication. DIAL's learned protocols are interpretable: a decision tree extracted for the Switch Riddle matches a known optimal strategy, and binary digit encodings are recoverable from Multi-Step MNIST communication bits. Analysis of channel noise shows that $\sigma \approx 2$ forces bimodal activations and is essential for stable discretisation; without noise the channel learns centred (non-discrete) activations.

## Relevance to this research
DIAL's architecture introduces differentiable inter-agent communication as a form of gradient-coupled belief passing — a precursor to the message-passing / belief-propagation view in the VFE multi-agent framework. The centralised-learning / decentralised-execution paradigm mirrors the structure of the VFE multi-agent model, where free-energy minimisation coordinates beliefs across agents while each agent acts on its own posterior. The DRU's regularised-then-discretised channel is structurally analogous to the continuous relaxation of discrete communication in variational inference settings. DIAL's gradient chain through the communication bottleneck is a non-probabilistic analogue of the belief-coupling KL terms in the VFE free energy functional ($\sum_{ij} \beta_{ij} \text{KL}(q_i \| \Omega_{ij} q_j)$), where message content is shaped by downstream prediction error rather than free-energy gradient. The parameter-sharing finding (shared network, differentiated only by agent index and hidden state) parallels the shared prior / model structure in the MAgent model. This work is foundational background for understanding emergent communication in cooperative multi-agent systems.

## Cross-links
- Concepts: [[Collective active inference|Multi-Agent Active Inference]], [[Variational Free Energy]], [[Belief Propagation]]
- Related sources: [[lowe-2017-maddpg]], [[sukhbaatar-2016-commnet]]
- Manuscript/Project: [[Gauge-Theoretic Multi-Agent VFE Model|MAgent Model]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{Foerster2016,
  author  = {Foerster, Jakob N. and Assael, Yannis M. and de Freitas, Nando and Whiteson, Shimon},
  title   = {Learning to Communicate with Deep Multi-Agent Reinforcement Learning},
  journal = {arXiv preprint arXiv:1605.06676},
  year    = {2016},
  url     = {https://arxiv.org/abs/1605.06676},
}
```
