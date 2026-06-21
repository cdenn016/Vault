---
type: concept
title: "Active Inference"
aliases:
  - "Active inference"
  - "Active Inference (process theory)"
tags:
  - cluster/vfe
  - project/multi-agent
  - project/transformer
status: draft
created: 2026-06-21
updated: 2026-06-21
---

# Active Inference

**Active inference** is the claim that *both perception and action* are one and the same operation
— the minimization of [[Variational free energy]] (VFE) — carried out by an agent equipped with a
[[Generative model]] of how its sensations are caused. Perception minimizes free energy by updating
beliefs to better explain the senses; action minimizes it by changing the senses to match
predictions. It is the *corollary* of the [[Free-energy principle active inference|free-energy principle]]
(FEP): the FEP is the general normative imperative ("any persisting agent must resist disorder by
minimizing surprise"), while active inference is the concrete *process theory* — laid out by Friston
in [[friston-2017-active-inference-process-theory]] and reviewed mathematically by
[[buckley-2017-fep-mathematical-review]] — that says *how* a creature does so.

## What it is — and is not

Active inference must be distinguished from two neighbours. **(a) The FEP** is the bare principle;
active inference adds a *model of action* on top of it. **(b) [[Predictive coding network|Predictive coding]]**
is the *perception-only* special case: under Gaussian (Laplace) assumptions, belief-updating reduces to
precision-weighted prediction-error descent, the perceptual half of active inference. Active inference
re-incorporates the action half that predictive coding leaves out — the agent acts to fulfil its own
predictions, a stance [[friston-frith-2015-duet]] dramatizes as two agents inferring each other.

## Formalism: the POMDP/MDP generative model

The discrete-state formulation casts the agent as a partially observable Markov decision process. A
generative model factorizes over hidden states $s_t$, outcomes $o_t$, and policies $\pi$:
$$
P(o_{1:T}, s_{1:T}, \pi) = P(\pi)\,\prod_t P(o_t\mid s_t)\,P(s_t \mid s_{t-1}, \pi),
$$
with a likelihood matrix $\mathbf{A}=P(o\mid s)$, transition matrices $\mathbf{B}(\pi)=P(s'\mid s,\pi)$,
and prior preferences $\mathbf{C}=P(o)$ that encode goals as expected outcomes
([[friston-2016-active-inference-learning]]). State estimation is ordinary VFE minimization; what is
new is that **action selection is itself inference** — the agent infers which policy it is pursuing.

## Expected free energy

Policies are scored not by past free energy but by **[[Expected Free Energy]]** $G(\pi)$ — the free
energy expected over *future* outcomes a policy would induce. Crucially it decomposes into an
*epistemic* (information-gain / exploratory) term and a *pragmatic* (preference-satisfying /
exploitative) term, so a single quantity resolves the explore–exploit trade-off without a bolted-on
reward or exploration bonus. The agent then assigns $P(\pi)\propto\exp(-G(\pi))$, preferring
low-EFE policies. This is what makes active inference an alternative to reward-maximizing
reinforcement learning ([[friston-2009-reinforcement-active-inference]]); see [[Expected Free Energy]]
for the full decomposition.

## Role in this research program

Active inference is the theoretical backbone of the [[Collective active inference|multi-agent MAgent model]],
where many free-energy-minimizing agents — each carrying Gaussian beliefs $(\mu,\Sigma)$ — couple
into a collective whose meta-agents themselves do active inference, grounding the model's
self-organization and belief dynamics. For the **vfe3 transformer**, the project imports active
inference's *perceptual* half (precision-weighted belief-updating as attention) but generally not its
expected-free-energy planning over actions.

> [!note] Editorial: The map from active inference's policy selection onto a sequence model is loose;
> the transformer borrows the belief-updating/precision-as-attention reading, while EFE-style planning
> is native to the multi-agent setting. The "Bayesian mechanics" of [[dacosta-2021-bayesian-mechanics]]
> gives the continuous-time, stationary-process foundation underneath both.

## See also

- [[Free-energy principle active inference]] — the method/synthesis page (the *what* and the geometry this project adds).
- [[Expected Free Energy]] — the $G(\pi)$ functional and its epistemic/pragmatic split.
- [[Variational free energy]] — the quantity minimized in perception.
- [[Generative model]] — the $P(o,s,\pi)$ object the agent inverts.
- [[Predictive coding network]] — the perception-only special case.
- [[Collective active inference]] — the multi-agent / MAgent realization.
- [[Consciousness and Active Inference]] — the participatory / consciousness reading.
