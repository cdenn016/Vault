---
type: reference
title: "Broadcasting on Random Directed Acyclic Graphs"
aliases: ["makur2020broadcasting"]
authors: ["Anuran Makur", "Elchanan Mossel", "Yury Polyanskiy"]
year: 2020
venue: "IEEE Transactions on Information Theory"
doi: "10.1109/TIT.2019.2935772"
url: "https://doi.org/10.1109/TIT.2019.2935772"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/statistics, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---

# Broadcasting on Random Directed Acyclic Graphs

> [!info] Citation
> Makur, A., Mossel, E., Polyanskiy, Y. (2020). *Broadcasting on Random Directed Acyclic Graphs*. IEEE Transactions on Information Theory, 66(2), 780-812. [DOI](https://doi.org/10.1109/TIT.2019.2935772)

[Local PDF](../pdfs/makur-2020-broadcasting-random-directed.pdf), 35 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and abstract.

## TL;DR

A study of whether a single source bit can be reconstructed from the values at a deep layer of an infinite directed acyclic graph whose edges are noisy binary channels and whose vertices apply a Boolean processing function.

## Problem & setting

A source vertex holds a random bit. Each non-source vertex receives bits from its parents in the previous layer through independent binary symmetric channels with crossover probability below one half, and combines them with a deterministic function. The goal is to recover the source bit with error bounded away from one half from all values at an arbitrarily deep layer. The abstract connects the question to reliable computation and storage and to information flow in biological networks.

## Key results

Per the abstract, for random DAGs, broadcasting is possible only below a critical noise level that depends on the in-degree and the processing function. The abstract states the critical threshold for in-degree at least three with majority processing, and a similar result for in-degree two with the NAND function. It also gives a partial converse, an explicit expander-based construction with bounded degree, and a doubly exponential advantage over trees in the layer size needed to store a bit. The local file is a different arXiv version, titled "Broadcasting on Bounded Degree DAGs", whose abstract also treats a two-dimensional grid with AND or XOR processing; the description above follows the abstract in the bibliographic record.

## Relevance to this research

The manuscript cites the paper, known from its abstract, for the point that on low-dimensional lattices with linear relays condensation of information would need long-range links, nonlinear processing, or persistent memory, and it names majority processing as one such nonlinear option. The paper relates to [[Data processing inequality]], [[Channel Capacity]] and [[Communication-constrained inference]].

## Cross-links

[[Collective agents literature map]]; [[Data processing inequality]]; [[Channel Capacity]]; [[Communication-constrained inference]]; [[makur-2020-comparison-contraction-coefficients]].

## BibTeX

```bibtex
@article{makur2020broadcasting,
  author  = {Makur, Anuran and Mossel, Elchanan and Polyanskiy, Yury},
  title   = {Broadcasting on Random Directed Acyclic Graphs},
  journal = {IEEE Transactions on Information Theory},
  volume  = {66},
  number  = {2},
  pages   = {780--812},
  year    = {2020},
  doi     = {10.1109/TIT.2019.2935772}
}
```
