---
type: paper
title: "Bayesian Learning in Social Networks"
aliases: ["Acemoglu, Dahleh, Lobel & Ozdaglar 2011", "Bayesian learning in social networks"]
authors: ["Acemoglu D.", "Dahleh M. A.", "Lobel I.", "Ozdaglar A."]
year: 2011
url: https://doi.org/10.1093/restud/rdr004
tags: [cluster/social-physics, project/social-physics, field/economics, field/sociology, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Bayesian Learning in Social Networks

> [!info] Citation
> Acemoglu, D., Dahleh, M. A., Lobel, I., & Ozdaglar, A. (2011). *Bayesian Learning in Social Networks*. The Review of Economic Studies, 78(4), 1201-1236. DOI: [10.1093/restud/rdr004](https://doi.org/10.1093/restud/rdr004).

## TL;DR
This paper generalizes the classical sequential-herding models to **arbitrary observation networks**. Agents act once, in sequence, each privately receiving a signal and observing the actions of a *stochastically determined neighborhood* of predecessors rather than the full history. Working in the perfect Bayesian equilibrium of this game, the authors characterize when *asymptotic learning* occurs — i.e. when the probability that a late-moving agent takes the correct action converges to one — purely in terms of the network's topological properties. The headline dichotomy: with unbounded private signals, asymptotic learning obtains for a broad class of "expanding observation" networks, but it can fail when influential agents (or sparse, non-expanding neighborhoods) cause information to bottleneck, reproducing herding and cascade failures as special cases.

## What it establishes
The key construct is the **neighborhood** $B(n) \subseteq \{1,\dots,n-1\}$ that agent $n$ observes, drawn from a distribution over predecessor sets. Learning outcomes hinge on two signal/topology conditions. With *unbounded* signals (private beliefs can take values arbitrarily close to certainty), asymptotic learning holds if and only if the network satisfies an **expanding observations** property — informally, that the most recently informed neighbors are not bounded away from the present, so fresh private information keeps entering the public record. With *bounded* signals, even expanding networks generally fail to learn, recovering the herding/cascade inefficiency of the 1992 models. The framework also shows that **"influential" agents** observed by infinitely many successors can either accelerate learning or, if they herd early, propagate error widely. The contribution is to make the success or failure of social learning an explicit, provable function of graph structure rather than of a fixed line.

## Relevance to this research
This is the modern general-network synthesis of Bayesian herding and the rigorous generalization of the founding cascade models, a strong benchmark for the program. It supplies the topology-dependent learning/no-learning dichotomy against which a gauge-coupled belief network should be measured: in the program, the analog of the observation network is the attention graph defined by the weights $\beta_{ij}$, and the question "does the population converge to the truth or lock onto a wrong consensus?" is exactly Acemoglu et al.'s asymptotic-learning question transposed to continuous Gaussian beliefs. Their expanding-observations condition and bounded-signal failure mode are the cleanest existing statements of *which network structures permit correct collective inference*, giving the program a concrete target: show that the gauge-coupled dynamics inherit the same topology-driven phase boundary. The mapping is a benchmark/analogy rather than a contained result — their setting is one-shot Bayesian game play, the program's is iterative variational gradient flow.

See [[Information cascades and herding]], [[Multi-agent variational free energy]], [[Community detection and modularity]], [[Collective active inference]].

## Cross-links
- Concept: [[Information cascades and herding]]
- Related sources: [[bala-goyal-1998-learning-from-neighbours]], [[bikhchandani-hirshleifer-welch-1992-informational-cascades]], [[smith-sorensen-2000-pathological-observational-learning]]

## BibTeX
```bibtex
@article{acemoglu2011bayesian,
  author  = {Acemoglu, Daron and Dahleh, Munther A. and Lobel, Ilan and Ozdaglar, Asuman},
  title   = {Bayesian Learning in Social Networks},
  journal = {The Review of Economic Studies},
  year    = {2011},
  volume  = {78},
  number  = {4},
  pages   = {1201--1236},
  doi     = {10.1093/restud/rdr004}
}
```
