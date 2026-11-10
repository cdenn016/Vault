---
type: reference
title: "Causal Blankets: Theory and Algorithmic Framework"
aliases: ["rosas2020causal"]
authors: ["Fernando E. Rosas", "Pedro A. M. Mediano", "Martin Biehl", "Shamil Chandaria", "Daniel Polani"]
year: 2020
venue: "Active Inference: First International Workshop, IWAI 2020, Co-located with ECML/PKDD 2020, Ghent, Belgium, September 14, 2020, Proceedings"
doi: "10.1007/978-3-030-64919-7_19"
arxiv: "2008.12568"
url: "https://doi.org/10.1007/978-3-030-64919-7_19"
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/statistics, field/neuroscience]
created: 2026-11-10
updated: 2026-11-10
---

# Causal Blankets: Theory and Algorithmic Framework

> [!info] Citation
> Rosas, F. E., Mediano, P. A. M., Biehl, M., Chandaria, S., Polani, D. (2020). *Causal Blankets: Theory and Algorithmic Framework*. In Active Inference: First International Workshop, IWAI 2020, Co-located with ECML/PKDD 2020, Ghent, Belgium, September 14, 2020, Proceedings (Communications in Computer and Information Science 1326), pp. 187-198. Springer, Cham. [DOI](https://doi.org/10.1007/978-3-030-64919-7_19), [arXiv](https://arxiv.org/abs/2008.12568)

[Local PDF](../pdfs/rosas-2020-causal-blankets-algorithmic.pdf), 12 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper introduces causal blankets, a data-driven way to identify perception-action loops using computational mechanics. It shows that every bipartite stochastic process has a causal blanket, while the usefulness of the resulting loop description depends on the integrated information of the bipartition.

## Problem & setting

The introduction notes that the free-energy literature formalizes perception-action loops through Markov blankets, usually for ergodic Markovian processes with a steady-state distribution satisfying a conditional independence of internal and external variables given sensory and active variables. The authors argue that this condition does not fix the direction of the loop, because it is symmetric in internal and external variables, and that, holding synchronously, it does not guarantee causal relations. Additional diachronic restrictions are then needed, for instance as coupled stochastic differential equations.

## Method

Causal blankets capture sensory and active variables as dynamical sufficient statistics, the "differences that make a difference". The construction requires neither a steady state nor Markovian dynamics.

## Key results

Every bipartite stochastic process has a causal blanket, and how effective the loop formulation is varies with the integrated information of the bipartition. Only the abstract and introduction were read for this note.

## Relevance to this research

The manuscript lists causal blankets among information-theoretic order parameters related to its own blanket-based definition of a collective, and states in its reading record that it knows the paper through secondary accounts. The first pages read here confirm the problem framing above. See [[Markov Blanket]], [[Markov blanket interpretation debate]] and [[Active inference communication and collective boundaries]].

## Cross-links

[[Collective agents literature map]]; [[Markov Blanket]]; [[Markov blanket interpretation debate]]; [[Active inference communication and collective boundaries]]; [[shalizi-2025-what-macrostate-subjective]].

## BibTeX

```bibtex
@incollection{rosas2020causal,
  author        = {Rosas, Fernando E. and Mediano, Pedro A. M. and Biehl, Martin and Chandaria, Shamil and Polani, Daniel},
  title         = {Causal Blankets: Theory and Algorithmic Framework},
  booktitle     = {Active Inference: First International Workshop, {IWAI} 2020, Co-located with {ECML/PKDD} 2020, Ghent, Belgium, September 14, 2020, Proceedings},
  series        = {Communications in Computer and Information Science},
  volume        = {1326},
  pages         = {187--198},
  publisher     = {Springer},
  address       = {Cham},
  year          = {2020},
  doi           = {10.1007/978-3-030-64919-7_19},
  eprint        = {2008.12568},
  archivePrefix = {arXiv}
}
```
