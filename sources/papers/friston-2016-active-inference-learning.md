---
type: paper
title: "Active Inference and Learning"
aliases:
  - "Friston 2016"
  - "Active Inference and Learning"
  - "friston2016active"
authors:
  - Friston, Karl
  - FitzGerald, Thomas
  - Rigoli, Francesco
  - Schwartenbeck, Philipp
  - O'Doherty, John
  - Pezzulo, Giovanni
year: 2016
arxiv: null
url: https://doi.org/10.1016/j.neubiorev.2016.06.022
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/neuroscience
  - field/cs-ml
  - field/psychology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Active Inference and Learning

> [!info] Citation
> Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., O'Doherty, J., & Pezzulo, G. (2016). "Active Inference and Learning." *Neuroscience & Biobehavioral Reviews*, 68, 862–879. https://doi.org/10.1016/j.neubiorev.2016.06.022

## TL;DR

This paper unifies perception, action, and learning under a single variational free energy minimization principle operating at different timescales. Inference (perception) and control (action selection) operate on fast timescales by minimizing free energy with respect to hidden states and policies; learning operates on a slower timescale by minimizing free energy with respect to generative model parameters (concentration parameters of Dirichlet distributions). The paper shows how epistemic foraging — exploration driven by expected information gain — emerges naturally from the same free energy objective without needing separate curiosity or reward signals.

## Problem & setting

Classical reinforcement learning separates perception, action, and learning into distinct modules with different objective functions (likelihood maximization, reward maximization, policy gradient). This fragmentation makes it difficult to explain the intrinsically motivated, exploratory behavior observed in biological agents, or to give a principled account of how priors over policies are updated through experience.

The paper asks: can perception, action selection, and synaptic plasticity (parameter learning) all be derived as gradient flows on a single objective — variational free energy — differing only in what they optimize over and on what timescale? The setting is a partially observable Markov decision process (POMDP) framed generatively, with the agent holding a probabilistic model over hidden states, observations, transitions, and policies.

## Method

The generative model factors as:

```
P(o, s, A, B, C, D) = P(o|s,A) P(s|B,D) P(A) P(B) P(C) P(D)
```

where `A` is the likelihood mapping (observation model), `B` encodes transition dynamics, `C` encodes prior preferences over outcomes, and `D` is the prior over initial hidden states. All parameters carry Dirichlet (or related conjugate) priors, making their sufficient statistics natural objects for gradient updates.

**Perception (fast, state inference).** Given fixed parameters, the agent minimizes variational free energy

```
F = E_q[log q(s)] - E_q[log P(o,s)]
```

with respect to the approximate posterior `q(s)` via mean-field belief propagation, recovering the standard active-inference E-step.

**Action / policy selection (fast).** Policies `π` are selected by minimizing expected free energy `G(π)` over future time steps, which decomposes into an extrinsic value term (aligning expected observations with prior preferences `C`) and an intrinsic epistemic term (expected information gain about hidden states, i.e., Bayesian surprise). Formally:

```
G(π) = E_q[log q(s|π) - log P(o,s|π)]
     ≈ -E_q[log P(o|C)] + E_q[H[P(o|s)]] - I[o;s|π]
```

Softmax over `-G(π)` gives the posterior over policies, and the expected action is the marginal over the first time step.

**Learning (slow, parameter update).** After each trial or epoch, free energy is minimized with respect to the Dirichlet concentration parameters of `A`, `B`, `D` by accumulating sufficient statistics from the posterior `q(s)`. This is a variational Bayes M-step: concentration parameters are incremented proportionally to the posterior expected state occupancies, implementing a form of Hebbian/delta-rule plasticity. The prior over parameters prevents overfitting and encodes innate knowledge.

The three timescales — within-trial state inference, between-trial parameter learning, and developmental prior setting — are made explicit, providing a hierarchical timescale separation analogous to fast synaptic dynamics vs. slow synaptic consolidation.

## Key results

1. **Unified objective.** Perception, action, and learning are shown to be special cases of free energy minimization, differing only in which variables are optimized. No separate reward function, value function, or policy gradient is needed.

2. **Epistemic value emerges naturally.** The expected information gain term in `G(π)` produces curiosity-driven exploration without engineering an intrinsic reward. Simulations reproduce Pavlovian, instrumental, and exploratory behaviors in a foraging task.

3. **Parameter learning as M-step.** Dirichlet parameters accumulate posterior state statistics across trials, implementing a biologically plausible Hebbian rule. The paper demonstrates acquisition of accurate `A` and `B` matrices over repeated exposures, mirroring classical conditioning and model-based RL benchmarks.

4. **Policy priors can be learned.** Concentration parameters on `C` (prior preferences) and initial-state priors `D` are also updated, allowing the agent to develop habitual responses consistent with prior experience — bridging goal-directed and habitual control in a single framework.

5. **Numerical demonstrations** in synthetic POMDPs show that the active-inference agent matches or outperforms standard RL baselines on tasks requiring both exploration and exploitation, without any hand-crafted exploration schedules.

## Relevance to this research

This paper is one of the foundational references for the multi-agent VFE model's treatment of learning. In the VFE transformer program, the hyperprior hierarchy `h → s → p → q → observations` directly mirrors Friston et al.'s timescale separation: fast within-forward-pass belief updates (perception) are the E-step, while any learned parameters (connection weights, prior banks) correspond to the slow M-step parameter updates described here.

More specifically:

- The **free energy functional** in the VFE transformer (`F = α·KL(q‖p) + λ_h·KL(s‖h) + Σβ·KL(q_i‖Ω_ij q_j) + ...`) is the multi-agent, gauge-equivariant extension of the single-agent free energy `F` analyzed here. The KL self-coupling term `α·KL(q‖p)` is precisely the "perception" gradient flow.

- The paper's **policy-as-inference** formulation (softmax over `-G(π)`) is the conceptual ancestor of the softmax attention weights `β_ij` in GL(K) attention, where expected free energy plays the role of attention logits and epistemic value maps to information-geometric divergences between transported beliefs.

- The **Dirichlet parameter learning** as accumulated sufficient statistics is analogous to the PriorBank update in `train_vfe3.py`, where prior parameters are updated via free energy gradients rather than backprop through a loss.

- For the PIFB (Participatory It-From-Bit) manuscript, this paper supplies the active-inference agent model that must be extended to the multi-agent participatory setting.

## Cross-links

- Concepts: [[Variational free energy]], [[Bayesian mechanics]], [[Expected free energy]], [[Active inference]], [[Predictive coding]]
- Theme: [[Variational free energy and predictive coding]]
- Related sources: [[friston-2010-free-energy-principle]], [[friston-frith-2015-duet|friston-2015-active-inference-epistemic]], [[friston-2017-active-inference-process-theory|friston-2017-active-inference-curiosity]]
- Manuscript/Project: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{friston2016active,
  author  = {Friston, Karl and FitzGerald, Thomas and Rigoli, Francesco and Schwartenbeck, Philipp and O'Doherty, John and Pezzulo, Giovanni},
  title   = {Active Inference and Learning},
  journal = {Neuroscience \& Biobehavioral Reviews},
  volume  = {68},
  pages   = {862--879},
  year    = {2016},
  doi     = {10.1016/j.neubiorev.2016.06.022}
}
```
