---
type: reference
title: "Dynamics in near-potential games"
aliases: ["candogan2013dynamics"]
authors: ["Ozan Candogan", "Asuman Ozdaglar", "Pablo A. Parrilo"]
year: 2013
venue: "Games and Economic Behavior"
doi: "10.1016/j.geb.2013.07.001"
arxiv: "1107.4386"
url: "https://doi.org/10.1016/j.geb.2013.07.001"
tags: [cluster/multi-agent, project/multi-agent, field/economics, field/mathematics, field/cs-ml]
created: 2026-11-10
updated: 2026-11-10
---

# Dynamics in near-potential games

> [!info] Citation
> Candogan, O., Ozdaglar, A., Parrilo, P. A. (2013). *Dynamics in near-potential games*. Games and Economic Behavior, 82, 66-90. [DOI](https://doi.org/10.1016/j.geb.2013.07.001); [arXiv](https://arxiv.org/abs/1107.4386)

[Local PDF](../pdfs/candogan-2013-dynamics-near-potential.pdf), 42 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

The paper quantifies how far the dynamical properties of potential games carry over to games that are close to a potential game, for better and best response, logit response and fictitious play.

## Problem & setting

Outside special classes, adaptive dynamics in games need not converge to Nash equilibrium, and potential games are a restrictive class where they do. The introduction gives examples showing that games close in payoffs can have very different limiting behavior under simple dynamics, and sets the goal of making the intuition of continuity precise.

## Method

Distance to a potential game is measured in payoffs, and a close potential game can be found by convex optimization. For logit response the analysis uses a Markov chain on pure strategy profiles parametrized by a smoothing parameter, and characterizes its stationary distribution through the distance to the close potential game and that game's potential function.

## Key results

The abstract states that better and best response sequences converge to an approximate equilibrium set whose size depends on the distance, that stochastically stable profiles of logit response are pure approximate equilibria, and that under fictitious play the empirical frequencies converge to a neighborhood of mixed equilibria whose size grows with the distance.

## Relevance to this research

The collective-agents manuscript cites this paper in two places: for the statement that near-potential games have logit laws near a Gibbs law, and for a per-profile bound from the arXiv version that the manuscript adapts, with a halved argument of the hyperbolic tangent and a total-variation form. The reading record lists the definitions, proposition, theorem, lemma and corollaries read in the arXiv version, with journal numbering unchecked. The link to the vault is the Gibbs-form stationary behavior of interacting decision makers and its robustness to departures from a potential, see [[Evolutionary game theory and cooperation]], [[Bounded Rationality]] and [[Multi-agent variational free energy]].

## Cross-links

[[Collective agents literature map]]; [[Evolutionary game theory and cooperation]]; [[Bounded Rationality]]; [[Multi-agent variational free energy]]; [[blume-1993-statistical-mechanics-strategic]].

## BibTeX

```bibtex
@article{candogan2013dynamics,
  author        = {Candogan, Ozan and Ozdaglar, Asuman and Parrilo, Pablo A.},
  title         = {Dynamics in near-potential games},
  journal       = {Games and Economic Behavior},
  volume        = {82},
  pages         = {66--90},
  year          = {2013},
  doi           = {10.1016/j.geb.2013.07.001},
  eprint        = {1107.4386},
  archivePrefix = {arXiv}
}
```
