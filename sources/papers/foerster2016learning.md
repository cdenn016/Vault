---
type: paper
title: "Learning to Communicate with Deep Multi-Agent Reinforcement Learning"
aliases:
  - "Foerster 2016"
  - "DIAL"
  - "RIAL"
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
This paper addresses the problem of multiple agents that must autonomously discover communication protocols in partially observable cooperative environments. Two algorithms are proposed: Reinforced Inter-Agent Learning (RIAL), which applies deep Q-learning with recurrent networks independently per agent, and Differentiable Inter-Agent Learning (DIAL), which passes real-valued messages and gradients between agents during centralised training, then discretises them for decentralised execution. DIAL substantially outperforms RIAL by enabling end-to-end backpropagation across the communication channel.

## Problem & setting
Cooperative multi-agent tasks with partial observability require agents to coordinate via a discrete, limited-bandwidth communication channel. No protocol is given a priori; agents must discover one through experience. The difficulty is that positive rewards are sparse and arise only when sending and interpreting are properly coordinated, making the joint protocol space exponentially large. The authors adopt a centralised learning / decentralised execution paradigm: unrestricted communication during training, but only the learned discrete channel at execution time.

## Method
Two approaches are presented. RIAL combines Deep Recurrent Q-Networks (DRQN) with independent Q-learning, optionally sharing parameters across agents; gradients do not cross agent boundaries. DIAL replaces discrete communication actions during centralised learning with direct real-valued connections between agents' networks (C-Nets). A Discretise/Regularise Unit (DRU) maps outgoing messages to `DRU(m) = Logistic(N(m, σ))` during training and `DRU(m) = 1{m > 0}` during execution, controlling discretisation error via channel noise `σ`. Backpropagation flows from the receiving agent back to the sender through the DRU, yielding a richer inter-agent gradient signal than the scalar DQN TD-error available to RIAL. The gradient chain for the communication pathway is

    µ^a_t = Σ_{m'≠m} ∂/∂m̂^a_t (ΔQ^{a'}_{t+1})² + µ^{a'}_{t+1} ∂m̂^{a'}_{t+1}/∂m̂^a_t

Parameter sharing across agents (a single shared C-Net parameterisation) is found to be essential for learning consistent protocols.

## Key results
On the Switch Riddle (inspired by the 100-prisoners problem) with n=3 and n=4 agents, DIAL with parameter sharing reaches near-optimal normalised reward substantially faster than RIAL. RIAL without parameter sharing fails to beat a no-communication baseline at n=4. On two MNIST-based multi-agent games (Colour-Digit and Multi-Step MNIST), DIAL substantially outperforms all baselines; RIAL fails entirely on Multi-Step MNIST because the TD error cancels in expectation when rewards are antisymmetric (equation 3 in the paper), while the inter-agent gradient (equation 4) does not cancel and remains informative. Analysis of learned protocols shows that DIAL discovers interpretable binary encodings of task-relevant state. Adding noise to the DRU is essential: without it, activations remain centred and do not discretise cleanly; with σ ≈ 2, the channel is forced into two well-separated modes.

## Relevance to this research
The multi-agent communication setting here is a prototype for the kind of emergent coordination studied in the VFE / active-inference multi-agent framework. The DIAL architecture's centralised-learning / decentralised-execution split is structurally analogous to the training-time free-energy minimisation versus runtime inference split in the MAgent model. The gradient-through-communication-channel mechanism is related to the belief-coupling terms in the VFE free energy (the `beta_ij KL(q_i || Omega_ij q_j)` terms), where belief messages play the role of the continuous channel activations. The discrete / continuous duality (real-valued during learning, binarised at execution) resonates with the Gaussian-to-point-mass belief collapse in variational inference. The parameter-sharing result (a single shared Q-function parameterisation enables protocol convergence) mirrors the shared prior / hyper-prior structure in the VFE hierarchy that ties agents to a common centroid. This paper is a useful empirical anchor for claims about emergent communication in multi-agent VFE systems.

## Cross-links
- Concepts: [[Multi-Agent Active Inference]]
- Related sources: [[lowe2017multi]], [[sukhbaatar2016learning]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{foerster2016learning,
  author  = {Foerster, Jakob N. and Assael, Yannis M. and de Freitas, Nando and Whiteson, Shimon},
  title   = {Learning to Communicate with Deep Multi-Agent Reinforcement Learning},
  journal = {arXiv preprint arXiv:1605.06676},
  year    = {2016},
}
```
