---
type: paper
title: "Threshold Models of Collective Behavior"
aliases: ["Granovetter 1978", "Threshold models of collective behavior"]
authors: ["Granovetter M. S."]
year: 1978
url: https://doi.org/10.1086/226707
tags: [cluster/social-physics, project/social-physics, field/sociology, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Threshold Models of Collective Behavior

> [!info] Citation
> Granovetter, M. S. (1978). *Threshold Models of Collective Behavior*. American Journal of Sociology, 83(6), 1420-1443. doi:10.1086/226707.

## TL;DR
Granovetter models binary collective action — joining a riot, adopting an innovation, going on strike — through individual *thresholds*: the fraction (or number) of others who must already have acted before a given person is willing to act. The aggregate trajectory is then the fixed point of the equilibrium condition relating the cumulative threshold distribution to the realized participation level. The central, counterintuitive result is that two populations with nearly identical *average* dispositions can produce radically different macro outcomes — total quiescence versus a full bandwagon — because behavior depends on the entire shape of the threshold distribution, not on its mean.

## What it establishes
Let $r(t)$ be the fraction who have acted by time $t$ and let $F$ be the cumulative distribution of thresholds across the population. The dynamics iterate
$$r(t+1) = F\big(r(t)\big),$$
and equilibria are the fixed points $r^* = F(r^*)$, with stability set by $F'(r^*)$. A single individual whose threshold shifts from, say, 4 to 3 can be the difference between a chain reaction that recruits the whole crowd and one that stalls after a few actors — the system sits near a tipping point where the stable equilibrium jumps discontinuously. The model thereby demonstrates that aggregate outcomes are emphatically *not* simple averages of individual preferences and that small perturbations to the threshold distribution can trigger qualitative regime change.

## Relevance to this research
Threshold adoption is the discrete-choice cousin of the continuous belief flip that an agent in the VFE model undergoes once accumulated social KL pressure from its neighbors exceeds the restoring pull of its own prior. Granovetter's demonstration that macro states are not averages of micro dispositions directly motivates why the gauge-coupled VFE functional supports non-trivial collective phases — consensus, polarization, and cascades — that cannot be read off from the agents' individual priors. The link to the social-coupling terms is strong and interpretive. See [[Threshold models and complex contagion]], [[Opinion dynamics]], and [[Echo chambers and polarization]].

## Cross-links
- Concept: [[Threshold models and complex contagion]]
- Related sources: [[watts-2002-global-cascades]], [[centola-macy-2007-complex-contagion]], [[kempe-kleinberg-tardos-2003-influence-maximization]]

## BibTeX
```bibtex
@article{granovetter1978threshold,
  author  = {Granovetter, Mark S.},
  title   = {Threshold Models of Collective Behavior},
  journal = {American Journal of Sociology},
  year    = {1978},
  volume  = {83},
  number  = {6},
  pages   = {1420--1443},
  doi     = {10.1086/226707}
}
```
