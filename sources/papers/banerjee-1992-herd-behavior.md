---
type: paper
title: "A Simple Model of Herd Behavior"
aliases: ["Banerjee 1992", "Banerjee herd behavior model"]
authors: ["Banerjee A. V."]
year: 1992
url: https://doi.org/10.2307/2118364
tags: [cluster/social-physics, project/social-physics, field/economics, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# A Simple Model of Herd Behavior

> [!info] Citation
> Banerjee, A. V. (1992). *A Simple Model of Herd Behavior*. Quarterly Journal of Economics, 107(3), 797-817. DOI: [10.2307/2118364](https://doi.org/10.2307/2118364).

## TL;DR
Banerjee builds the minimal sequential-decision model in which fully rational, optimizing agents end up imitating one another to the point of collective error. Agents choose an action one at a time, each privately observing a noisy signal about which choice is correct, but also observing the choices (not the signals) of everyone who moved before them. Because an earlier agent's action partially reveals her private information, a later agent rationally treats predecessors' choices as evidence and can find it optimal to discard her own signal and follow the crowd. The result is a *herd*: the population converges on a single action that may be wrong, and the equilibrium is inefficient because individual signals stop being aggregated into the public record once herding begins.

## What it establishes
The decision rule is Bayesian: agent $t$ chooses the action maximizing expected payoff given her private signal $s_t$ and the history of observed actions $a_1,\dots,a_{t-1}$. Banerjee shows that once the public history tilts decisively toward one option, the posterior induced by that history can dominate any single private signal, so

$$\Pr(\text{correct}\mid a_1,\dots,a_{t-1}) \;\gg\; \Pr(\text{correct}\mid s_t)$$

and the agent rationally copies. A central feature of his model is the *tie-breaking* assumption that an indifferent agent follows her own signal, which seeds the cascade and makes the herd path-dependent on the order and content of early signals. The equilibrium exhibits the hallmark pathologies: herds are fragile (sensitive to early movers), informationally wasteful (later signals are never expressed), and can settle on the inferior choice with positive probability. Herding here is an *externality of information*: each agent ignores that her imitation deprives the group of her private signal.

## Relevance to this research
This is one of the two 1992 founding papers of rational-herding theory and the canonical demonstration that copying neighbors can be individually rational yet collectively wrong, the precise tension the VFE coupling term encodes. In the belief-inertia functional, the self-coupling term $\alpha\,\mathrm{KL}(q_i\|p_i)$ binds an agent to its own evidence-shaped prior, while the neighbor-coupling term $\sum_j \beta_{ij}\,\mathrm{KL}(q_i\|\Omega_{ij}[q_j])$ pulls it toward transported neighbor beliefs; Banerjee's herd is what happens in the limit where the latter overwhelms the former and private signal weight collapses to zero. The connection is honest but qualitative: Banerjee's mechanism is discrete, sequential, and game-theoretic, whereas the program's dynamics are continuous gradient flow on a Gaussian belief manifold — the program should be able to *recover* herding as a regime, not claim it as an existing identity.

See [[Information cascades and herding]], [[Multi-agent variational free energy]], [[Opinion dynamics]], [[Belief inertia]].

## Cross-links
- Concept: [[Information cascades and herding]]
- Related sources: [[bikhchandani-hirshleifer-welch-1992-informational-cascades]], [[smith-sorensen-2000-pathological-observational-learning]], [[acemoglu-dahleh-lobel-ozdaglar-2011-bayesian-learning-networks]]

## BibTeX
```bibtex
@article{banerjee1992herd,
  author  = {Banerjee, Abhijit V.},
  title   = {A Simple Model of Herd Behavior},
  journal = {The Quarterly Journal of Economics},
  year    = {1992},
  volume  = {107},
  number  = {3},
  pages   = {797--817},
  doi     = {10.2307/2118364}
}
```
