---
type: concept
title: "Discrete spin and majority-rule models of opinion"
aliases:
  - "Discrete opinion models"
  - "Spin models of opinion"
  - "Majority-rule opinion dynamics"
  - "Galam models"
tags:
  - cluster/social-physics
  - project/social-physics
status: stable
created: 2026-06-19
updated: 2026-07-13
---

# Discrete spin and majority-rule models of opinion

## Definition

**Discrete spin and majority-rule models of opinion** are the wing of sociophysics that represents an agent's opinion as a discrete variable — usually a binary Ising spin $S_i = \pm 1$ standing for two competing positions — and lets the population evolve by a local interaction rule borrowed from magnetism: align with your neighbours. The family is distinguished from averaging models of [[Opinion dynamics]] (DeGroot, Friedkin–Johnsen) by the fact that opinions never take intermediate values; each update is a hard switch between states, and the collective question is whether the lattice or graph orders into a single magnetized (consensus) phase or stays disordered (diverse). Three update rules organize the family. The **majority-vote rule** polls a neighbourhood and sets the central agent to the majority state, optionally with noise — a probability of perversely adopting the minority — that plays the role of temperature ([[deoliveira-1992-majority-vote-model]]). The **outward-persuasion rule** of the Sznajd model inverts the information flow: rather than a site copying its surroundings, a locally agreeing *pair* of agents imposes its shared opinion on the neighbours outside it, formalizing "united we stand, divided we fall" ([[sznajd-weron-sznajd-2000-closed-community]]). The **iterated-grouping rule** of the Galam models repeatedly partitions the population into small groups, replaces each group by its local-majority verdict, and feeds the verdicts into the next round, so that the dynamics is a coarse-graining map on the support fraction rather than a site update ([[galam-1986-majority-rule-hierarchical]], [[galam-2002-minority-opinion-spreading]]). The historical root of the entire wing is the original strike model, which wrote a group "dissatisfaction function" as an Ising Hamiltonian and minimized it ([[galam-gefen-shapir-1982-sociophysics-strike]]).

## Why it matters here

For the SocialPhysics program founded on [[belief-inertia]], discrete spin and majority-rule models are genealogical benchmarks, not shared machinery or fixed points already subsumed by the VFE flow. Their hard binary updates, majority amplification, order-disorder transition, minority spreading, and Galam coarse-graining are not derived from gauge-transported Gaussian KL coupling. The current first-order result is limited to fixed symmetric DeGroot under the primary unweighted Fisher flow, a nonuniform reversible transient under $G_\rho$ or agent-specific rates, and a restricted reversible anchored stationary equilibrium independent of the positive flow metric. Attention temperature is not thereby identified with spin temperature, and a biased attention prior does not prove minority takeover. These models instead provide explicit transition and topology benchmarks for future discrete-state, majority-sensitive, and coarse-grained extensions. Cross-links: [[Sociophysics]], [[Multi-agent variational free energy]], [[Opinion dynamics]], [[Echo chambers and polarization]], and [[Collective active inference]].

## Details

The **majority-vote model** ([[deoliveira-1992-majority-vote-model]]) places spins $\sigma_i = \pm 1$ on a square lattice and flips each according to the sign of its neighbourhood sum, perturbed by noise $q$:
$$
w_i(\sigma) = \tfrac{1}{2}\Big[\,1 - (1 - 2q)\,\sigma_i\,\mathrm{sgn}\!\Big(\textstyle\sum_{j \in \partial i}\sigma_j\Big)\Big].
$$
With probability $q$ a site adopts the *minority* state, so $q$ acts as a temperature. The dynamics is genuinely nonequilibrium — it derives from no Hamiltonian and violates detailed balance — yet it shows a continuous order-disorder transition at $q_c \approx 0.075$, and de Oliveira's central result is that its critical exponents (from magnetization, susceptibility, and the Binder cumulant) place it in the **two-dimensional Ising universality class**, an early clean demonstration that nonequilibrium majority dynamics can share the critical behaviour of an equilibrium magnet.

The **Sznajd model** ([[sznajd-weron-sznajd-2000-closed-community]]) reverses the direction of influence. On a one-dimensional chain of $\pm 1$ spins, if an adjacent pair agrees, $S_i = S_{i+1}$, both outer neighbours $S_{i-1}$ and $S_{i+2}$ are converted to that common opinion; if the pair disagrees, the original "antiferromagnetic" variant pushes the outer neighbours apart, while other variants leave them untouched. Information thus flows *outward from locally agreeing pairs* rather than inward from a neighbourhood average — the feature that distinguishes it from both the voter model (copy one neighbour) and majority rule (poll a group). From a random start the closed community is driven to one of a few absorbing states: the two full-consensus ("dictatorship") configurations or a frozen stalemate, with the time to reach a decision distributed as a power law, the signature of self-organized relaxation.

The **Galam majority-rule program** is the iterated-grouping branch. In the hierarchical model ([[galam-1986-majority-rule-hierarchical]]) the support fraction $p$ for a position is mapped level by level by the majority-vote map
$$
p' = P_r(p) = \sum_{k > r/2} \binom{r}{k} p^k (1-p)^{r-k},
$$
for groups of size $r$ electing a representative by majority. The map has stable fixed points at $0$ and $1$ and an unstable interior threshold $p_c$ (for instance $p_c \approx 0.77$ for groups of three when ties favour an incumbent), so iterating up the tiers drives any starting majority above threshold to total control of the top and any below to extinction — the "democratic totalitarianism" by which bottom-up aggregation entrenches a fixed group, and structurally a real-space renormalization on the support probability. The minority-spreading result ([[galam-2002-minority-opinion-spreading]]) shows the threshold's displacement is the whole story: with groups updating by local majority and *ties broken toward one designated opinion A*, the interior fixed point $p_c$ is pushed below one-half, so any initial support exceeding the lowered threshold flows under repeated random grouping to total victory $p \to 1$ — an initial minority becomes the global majority through nothing but the asymmetry in resolving ties, compounded by iteration, with the effect surviving an average over a distribution of group sizes (the "random geometry"). Both Galam results trace back to the founding strike paper ([[galam-gefen-shapir-1982-sociophysics-strike]]), where each worker is a two-state strike/work variable, the collective dissatisfaction is an Ising-like Hamiltonian with pairwise colleague couplings and a coupling to external fields (conditions, salary, pressure), and the equilibrium striker fraction is the self-consistent mean-field minimizer; above a critical coupling the group responds collectively and discontinuously (a small shift in conditions triggers an all-or-nothing strike), below it the response is smooth and individual, making the strike an emergent ordered phase and the collective/individual boundary a phase transition.

Read together, the family spans the discrete corner of the [[Statistical physics of social systems and collective behavior]]: a noisy lattice spin model with a documented universality class, an outward-persuasion chain with power-law decision times, and an iterated-grouping coarse-graining whose tie-breaking asymmetry produces the counterintuitive flagship in which the minority wins.

## Sources

- [[deoliveira-1992-majority-vote-model]] — noisy majority-vote spin model on a square lattice; nonequilibrium dynamics in the Ising universality class with a critical noise $q_c$.
- [[sznajd-weron-sznajd-2000-closed-community]] — the Sznajd model: outward persuasion by agreeing pairs ("united we stand"), absorbing consensus/stalemate states, power-law decision times.
- [[galam-1986-majority-rule-hierarchical]] — hierarchical local-majority aggregation; the iterated majority-vote map $P_r$, its unstable threshold, and "democratic totalitarianism" as real-space RG.
- [[galam-2002-minority-opinion-spreading]] — minority opinion spreading via tie-breaking bias in iterated random grouping; the threshold pushed below one-half so a minority can conquer.
- [[galam-gefen-shapir-1982-sociophysics-strike]] — founding sociophysics paper; the strike as an Ising free-energy minimization with a collective/individual phase transition.
