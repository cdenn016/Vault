---
type: reference
title: "Knitting a Markov Blanket is Hard When You are Out-of-Equilibrium: Two Examples in Canonical Nonequilibrium Models"
aliases: ["aguilera2023knitting"]
authors: ["Miguel Aguilera", "Ángel Poc-López", "Conor Heins", "Christopher L. Buckley"]
year: 2023
venue: "Active Inference: Third International Workshop, IWAI 2022, Grenoble, France, September 19, 2022, Revised Selected Papers"
doi: "10.1007/978-3-031-28719-0_5"
arxiv: "2207.12914"
url: "https://doi.org/10.1007/978-3-031-28719-0_5"
tags: [cluster/vfe, cluster/multi-agent, project/multi-agent, field/neuroscience, field/physics]
created: 2026-11-10
updated: 2026-11-10
---
# Knitting a Markov Blanket is Hard When You are Out-of-Equilibrium: Two Examples in Canonical Nonequilibrium Models

> [!info] Citation
> Aguilera, M., Poc-López, Á., Heins, C., Buckley, C. L. (2023). *Knitting a Markov Blanket is Hard When You are Out-of-Equilibrium: Two Examples in Canonical Nonequilibrium Models*. In Active Inference: Third International Workshop, IWAI 2022, Grenoble, France, September 19, 2022, Revised Selected Papers, Communications in Computer and Information Science 1721, 65-74. Springer. [DOI](https://doi.org/10.1007/978-3-031-28719-0_5), [arXiv](https://arxiv.org/abs/2207.12914)

[Local PDF](../pdfs/aguilera-2023-knitting-markov-blanket.pdf), 10 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper tests whether sparse connectivity yields a Markov blanket in the steady-state density of nonequilibrium systems, using a pair of coupled Lorenz systems and a nonequilibrium Ising model. It reports that sparse connectivity does not guarantee a blanket.

## Problem & setting

The introduction defines a Markov blanket as a set $b$ that makes two other sets $x$ and $y$ conditionally independent, $p(x,y\mid b)=p(x\mid b)p(y\mid b)$. It states that the free energy principle literature assumes blankets arise from sparse structural connectivity, an intuition taken from acyclic Bayesian networks, and the paper restricts attention to conditional independence in the steady-state density.

## Key results

In both examples sparse connectivity did not produce a blanket in the steady-state density. In the Ising model the authors observe that greater distance from equilibrium goes with greater distance from displaying a blanket, and they conclude that further assumptions may be needed. The abstract states these as findings in two models, not as a general theorem.

## Relevance to this research

The manuscript cites this paper for the statement that direct tests found no blanket in coupled Lorenz systems where a Hessian-based treatment had certified one, and it records that this exchange is known through secondary accounts. I read the opening pages of the paper itself. The point matters for the vault's collective-boundary material, which needs a blanket condition to hold for communicating agents. See [[Markov blanket interpretation debate]], [[Markov Blanket]], [[Nonequilibrium steady state]] and [[Active inference communication and collective boundaries]].

## Cross-links

[[Collective agents literature map]]; [[Markov blanket interpretation debate]]; [[Markov Blanket]]; [[Nonequilibrium steady state]]; [[Active inference communication and collective boundaries]]; [[aguilera-2023-free-energy-principle]].

## BibTeX

```bibtex
@incollection{aguilera2023knitting,
  author        = {Aguilera, Miguel and Poc-L{\'o}pez, {\'A}ngel and Heins, Conor and Buckley, Christopher L.},
  title         = {Knitting a {Markov} Blanket is Hard When You are Out-of-Equilibrium: Two Examples in Canonical Nonequilibrium Models},
  booktitle     = {Active Inference: Third International Workshop, {IWAI} 2022, Grenoble, France, September 19, 2022, Revised Selected Papers},
  series        = {Communications in Computer and Information Science},
  volume        = {1721},
  pages         = {65--74},
  publisher     = {Springer},
  address       = {Cham},
  year          = {2023},
  doi           = {10.1007/978-3-031-28719-0_5},
  eprint        = {2207.12914},
  archivePrefix = {arXiv}
}
```
