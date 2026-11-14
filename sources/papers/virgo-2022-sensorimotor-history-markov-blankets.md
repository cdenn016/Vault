---
type: paper
title: "Embracing sensorimotor history: Time-synchronous and time-unrolled Markov blankets in the free-energy principle"
aliases: ["Virgo et al. 2022 sensorimotor history markov blankets"]
authors: ["Nathaniel Virgo", "Fernando E. Rosas", "Martin Biehl"]
year: 2022
venue: "Behavioral and Brain Sciences 45, e215 (open peer commentary on Bruineberg et al.)"
doi: "10.1017/S0140525X22000334"
url: "https://doi.org/10.1017/S0140525X22000334"
version: "Author preprint of the commentary, 4 pages, with no version number, date, or journal pagination printed; presumably the PsyArXiv posting named in the manifest. The version of record (Behavioral and Brain Sciences 45, e215, 2022) was not seen."
tags: [cluster/vfe, project/multi-agent, field/neuroscience, field/statistics, field/philosophy]
created: 2026-11-13
updated: 2026-11-13
---

# Embracing sensorimotor history: Time-synchronous and time-unrolled Markov blankets in the free-energy principle

> [!info] Citation
> Nathaniel Virgo, Fernando E. Rosas, Martin Biehl (2022). *Embracing sensorimotor history: Time-synchronous and time-unrolled Markov blankets in the free-energy principle*. Behavioral and Brain Sciences 45, e215 (open peer commentary on Bruineberg et al.). [DOI](https://doi.org/10.1017/S0140525X22000334)

[Local PDF](../pdfs/virgo-2022-sensorimotor-history-markov-blankets.pdf), 4 pages; retrieved November 13, 2026. Version read: Author preprint of the commentary, 4 pages, with no version number, date, or journal pagination printed; presumably the PsyArXiv posting named in the manifest. The version of record (Behavioral and Brain Sciences 45, e215, 2022) was not seen. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read all 4 pages of text in full, including the caption of Figure 1 and the reference list. The two numbered conditional independence relations are simple and unambiguous in the text. Figure 1 itself (the time-unrolled graph) was not seen; its content is known only from the caption. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, 002, 003, 004). Confirmed against those pages: 1 (p. 2), 2 (p. 3). The Figure 1 caption content and the edge structure were checked against the image: no direct internal-external edge; sensor nodes receive edges from earlier external states; actuator nodes receive edges from earlier internal states.

## TL;DR

A four-page commentary on Bruineberg et al. arguing that a sensor-motor loop does not imply the time-synchronous blanket condition $\mu_t \perp \phi_t \mid s_t, a_t$ used in deriving the free energy principle, and that this condition is very restrictive because it forces all information shared by agent and environment to be present in the current sensorimotor state. The authors propose conditioning on the sensorimotor history instead, an independence that does follow from the loop structure in discrete time.

## Problem & setting

The commentary responds to the target article by Bruineberg, Dolega, Dewhurst and Baltieri on Markov blankets and adds two issues. The free energy literature draws what the authors call influence graphs, whose nodes are dynamical variables and whose edges mark nonzero Jacobian entries; such graphs may be cyclic and Pearl's theorems for Bayesian networks do not apply to them. A stationary distribution over an influence graph therefore need not satisfy the conditional independence that the picture of a sensor-motor loop suggests. The authors build on Biehl, Pollock and Kanai (2021) and Aguilera et al. (2021), who made the point technically, and on the replies by Friston, Da Costa and Parr (2021) and Friston et al. (2021), which add conditions under which the needed independence holds. The setting is a discrete-time sensor-motor loop with internal state $\mu_t$, external state $\phi_t$, sensor state $s_t$ and actuator state $a_t$, unrolled in time into an acyclic Bayesian network (Figure 1). Stationarity is not needed for the main argument; ergodicity is invoked only to remove dependence on initial states.

## Method

The argument is graphical and informal. Because the time-unrolled loop is an acyclic Bayesian network, Pearl's framework applies to it. According to the caption of Figure 1 (p. 2), the current internal and external states $\mu_3$ and $\phi_3$ are conditionally independent given the full sensor and actuator histories $s_1, s_2, s_3$ and $a_1, a_2, a_3$ together with the initial states $\mu_0$ and $\phi_0$, which may be correlated. They are in general not independent given only $s_3$ and $a_3$, because they share ancestors, for example $\mu_1$ and $\phi_1$, that the current sensorimotor nodes do not screen off; the caption states that this holds regardless of stationarity. The time-synchronous condition used in the free energy literature is $\mu_t \perp \phi_t \mid s_t, a_t$ (Eq. 1, p. 2). The proposed replacement is $\mu_t \perp \phi_t \mid s_t, a_t, s_{t-1}, a_{t-1}, s_{t-2}, a_{t-2}, \ldots$ (Eq. 2, p. 3). For an ergodic system the caption says that dependence on the initial states disappears in the infinite limit, so that conditioning on the infinite past history of sensorimotor states is enough. A second argument uses the data processing inequality (Cover and Thomas 2006, p. 34): if Eq. 1 holds, all information that $\mu_t$ and $\phi_t$ share must be present in $(s_t, a_t)$. The counterexample offered on p. 3 is a phone number that is memorized and then shut in a box on a piece of paper: the information is held in the agent and in the environment while absent from the current sensory and active states.

## Key results

Nothing is proved formally and the commentary contains no theorem. Argued by conditional independence on the time-unrolled graph (Figure 1 caption, p. 2, and p. 3): the history-conditioned independence of Eq. 2 holds for a discrete-time sensor-motor loop, given also the initial states or an ergodicity assumption that removes them, while the synchronous condition of Eq. 1 does not follow from the loop structure, with or without stationarity. Argued from the data processing inequality (p. 3): Eq. 1 bounds the information shared between internal and external states by what the current sensor and motor states carry, which the authors regard as unrealistic for living organisms. They grant, citing Parr et al. (2021), that the constraint need not bind during transients even if it holds in the stationary state, and maintain that it is still an unrealistic constraint on stationary dynamics. Asserted: that the additional conditions introduced in the replies by Friston and colleagues are far from trivial and so indicate a narrower scope for the principle than previously thought (p. 3); that an analogous history-conditioned result is expected in continuous time (p. 3, stated as an expectation with no argument); and that a version of the free energy principle rebuilt on Eq. 2 would be more encompassing and close to the originally intended breadth (p. 3, conditional and programmatic). Alternative blanket constructions along these lines are said to be under investigation, with Rosas et al. (2020) on causal blankets cited as an example.

## Limits

The authors give no proof and no continuous-time statement; the piece is a short commentary with one figure. The history-conditioned independence needs conditioning on initial states, or ergodicity and an infinite past, and is stated for discrete time only. My observations: the independence claim is the standard one for a graph of the kind the caption describes, but it depends on the exact edge structure of Figure 1 (no direct edge between internal and external states, sensors driven by external states, actuators by internal states), which Figure 1 (p. 2) displays. The commentary does not say what inference reading survives under Eq. 2: the synchronization map of the stationary theory is defined on the current blanket state, and no replacement on histories is offered.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The commentary bears on how Markov blankets of individual agents and of collectives would be defined in the gauge-theoretic multi-agent model. If two agents interact only through exchanged messages, its argument implies that their belief states are in general dependent given the current messages and independent only given the message history together with initial conditions. A same-time conditional independence between agents, or between a meta-agent and its surroundings, would therefore be an added assumption and not a consequence of the interaction graph. Objects such as belief inertia, which give an agent persistent internal state, are the kind of memory for which the data processing argument says the synchronous condition should fail; that correspondence is qualitative, since the commentary has no dynamics, no metric and no transport. What the paper supplies is a constraint and a direction, toward history-conditioned or path-space blankets, and it supplies no construction. It has no bearing on statistical fibers, the gauge connection or the Fisher metric.

## Cross-links

Concepts: [[Markov Blanket]]; [[Markov blanket interpretation debate]]; [[Bayesian mechanics]]; [[Data processing inequality]]; [[Nonequilibrium steady state]]; [[Free-energy principle active inference]].

Related sources: [[bruineberg-2022-emperors-markov-blankets]]; [[biehl-2021-technical-critique]]; [[aguilera-2022-particular-physics]]; [[rosas-2020-causal-blankets-algorithmic]]; [[friston-2021-stochastic-chaos-markov]]; [[pearl-1988-probabilistic-reasoning-intelligent]]; [[cover-thomas-2006-elements-information-theory]]; [[friston-2021-interesting-observations-fep]]; [[parr-2021-memory-markov-blankets]]; [[sakthivadivel-2026-markov-interacting-particles]]; [[virgo-2021-interpreting-dynamical-systems-bayesian]]; [[pearson-2026-flux-defined-markov-blanket]].

## BibTeX

```bibtex
@article{virgo2022sensorimotor,
  author = {Virgo, Nathaniel and Rosas, Fernando E. and Biehl, Martin},
  title = {Embracing sensorimotor history: Time-synchronous and time-unrolled {M}arkov blankets in the free-energy principle},
  journal = {Behavioral and Brain Sciences},
  volume = {45},
  pages = {e215},
  year = {2022},
  doi = {10.1017/S0140525X22000334},
  note = {Open peer commentary on Bruineberg et al., The Emperor's New Markov Blankets; preprint PsyArXiv doi:10.31234/osf.io/7pqmr}
}
```
