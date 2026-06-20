---
type: paper
title: "Opinion Evolution in Closed Community"
aliases: ["Sznajd-Weron & Sznajd 2000", "Sznajd model"]
authors: ["Sznajd-Weron K.", "Sznajd J."]
year: 2000
url: https://doi.org/10.1142/S0129183100000936
tags: [cluster/social-physics, project/social-physics, field/physics, field/sociology, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Opinion Evolution in Closed Community

> [!info] Citation
> Sznajd-Weron, K., & Sznajd, J. (2000). *Opinion Evolution in Closed Community*. International Journal of Modern Physics C 11(6), 1157-1165. DOI: [10.1142/S0129183100000936](https://doi.org/10.1142/S0129183100000936). arXiv:cond-mat/0101130.

## TL;DR
The Sznajd model is a one-dimensional Ising-spin opinion dynamic built on the social maxim "united we stand, divided we fall." A pair of adjacent agents who agree act together to persuade their neighbours to adopt their shared opinion, whereas a disagreeing pair leaves the surroundings unchanged (or pushes them apart, depending on the variant). Starting from a random configuration of $\pm 1$ opinions in a closed community, the dynamics drives the system to one of a small set of steady states: complete consensus in either direction ("dictatorship") or a frozen stalemate. The model also exhibits a characteristic power-law distribution of the time required to reach a decision.

## What it establishes
Opinions are binary spins $S_i = \pm 1$ on a chain. The defining rule is outward persuasion by an agreeing pair: if $S_i = S_{i+1}$, then both neighbours $S_{i-1}$ and $S_{i+2}$ are set to that common value; if $S_i \ne S_{i+1}$, the original "antiferromagnetic" variant flips the outer neighbours to disagree. The absorbing states are the two ferromagnetic (full-consensus) configurations and, for the disagreeing rule, an antiferromagnetic stalemate. The model's signature is that information flows outward from locally agreeing pairs rather than inward from a neighbourhood average, distinguishing it from the voter model (which copies a single neighbour) and from majority rule (which polls a group). The distribution of decision times follows a power law, a hallmark of the model's self-organized relaxation.

## Relevance to this research
This is a widely cited spin model of opinion spreading and represents the discrete statistical-mechanics wing of sociophysics. Honestly assessed, it is adjacent context rather than machinery the belief-inertia functional uses: it shares the magnetic-ordering analogy with the program's free-energy framing but operates on binary spins with a local outward-persuasion rule, not on gauge-transported Gaussian beliefs with a precision-weighted KL coupling. It is most valuable as a contrast case — a discrete, inertia-free imitation dynamic against which the program's continuous, momentum-carrying belief dynamics can be positioned. See [[Discrete spin and majority-rule models of opinion]], [[Sociophysics]], [[Opinion dynamics]].

## Cross-links
- Concept: [[Discrete spin and majority-rule models of opinion]]
- Related sources: [[deoliveira-1992-majority-vote-model]], [[galam-2002-minority-opinion-spreading]]

## BibTeX
```bibtex
@article{sznajdweron2000opinion,
  author  = {Sznajd-Weron, Katarzyna and Sznajd, J{\'o}zef},
  title   = {Opinion Evolution in Closed Community},
  journal = {International Journal of Modern Physics C},
  year    = {2000},
  volume  = {11},
  number  = {6},
  pages   = {1157--1165},
  doi     = {10.1142/S0129183100000936}
}
```
