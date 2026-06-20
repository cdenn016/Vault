---
type: paper
title: "Learning from Neighbours"
aliases: ["Bala & Goyal 1998", "Learning from neighbours"]
authors: ["Bala V.", "Goyal S."]
year: 1998
url: https://doi.org/10.1111/1467-937X.00059
tags: [cluster/social-physics, project/social-physics, field/economics, field/sociology, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Learning from Neighbours

> [!info] Citation
> Bala, V., & Goyal, S. (1998). *Learning from Neighbours*. The Review of Economic Studies, 65(3), 595-621. DOI: [10.1111/1467-937X.00059](https://doi.org/10.1111/1467-937X.00059).

## TL;DR
Bala and Goyal recast social learning explicitly as a process running over a **network of neighbourhoods**. Each agent repeatedly chooses an action, observes the actions and realized payoffs of the agents in its local neighbourhood, and updates its beliefs accordingly, so information diffuses through the graph rather than through a single sequential queue. The central results are about long-run behavior: in a *connected* society beliefs and actions converge so that the population reaches **social conformism** (neighbours eventually act alike), but whether the society converges to the *correct* action depends on structure. They identify **local independence** — neighbourhoods that overlap little, so different parts of the network sample experience independently — as the property that protects against premature lock-in and aids correct learning, because it keeps diverse evidence flowing into the collective.

## What it establishes
The model is a repeated Bayesian decision problem with **local observation**: agent $i$'s information set at each date is the history of its own and its neighbours' actions and payoffs. The authors prove convergence theorems showing that connectedness forces asymptotic agreement among linked agents (conformism), but that the *content* of the consensus is path- and structure-dependent — a connected society can lock onto a suboptimal action. The constructive insight is that network architecture is the lever: societies with sufficient **local independence** (overlapping but not nested neighbourhoods, "royal family"-free structures) aggregate dispersed information well and tend toward the optimal action, whereas highly centralized or tightly overlapping structures can trap the society on an inferior choice. Learning success is thus a property of the *graph*, not merely of the agents.

## Relevance to this research
This paper casts herding explicitly as **learning over a network graph**, the same object as the multi-agent VFE coupling graph, making it a strong bridge for the program. Bala and Goyal's neighbourhood structure is the direct analog of the attention/coupling topology defined by $\beta_{ij}$, and their conformism result — connected societies converge to agreement — is exactly the consensus attractor of the neighbor-coupling term $\sum_j\beta_{ij}\,\mathrm{KL}(q_i\|\Omega_{ij}[q_j])$ when coupling dominates. Their finding that *local independence* protects correct learning parallels how attention topology in the program drives the choice between healthy consensus and pathological fragmentation or wrong lock-in: dense, redundant coupling collapses diversity, while structured, weakly-overlapping coupling preserves the evidentiary spread needed for the population to track the truth. The relevance is genuine and structural, though their belief update is discrete Bayesian over actions/payoffs while the program's is continuous variational updating of Gaussian $(\mu,\Sigma,\phi)$ tuples.

See [[Information cascades and herding]], [[Multi-agent variational free energy]], [[Community detection and modularity]], [[Opinion dynamics]].

## Cross-links
- Concept: [[Information cascades and herding]]
- Related sources: [[acemoglu-dahleh-lobel-ozdaglar-2011-bayesian-learning-networks]], [[banerjee-1992-herd-behavior]], [[smith-sorensen-2000-pathological-observational-learning]]

## BibTeX
```bibtex
@article{bala1998neighbours,
  author  = {Bala, Venkatesh and Goyal, Sanjeev},
  title   = {Learning from Neighbours},
  journal = {The Review of Economic Studies},
  year    = {1998},
  volume  = {65},
  number  = {3},
  pages   = {595--621},
  doi     = {10.1111/1467-937X.00059}
}
```
