---
type: reference
title: "On the scaling of the chemical distance in long-range percolation models"
aliases: ["biskup2004scaling"]
authors: ["Marek Biskup"]
year: 2004
venue: "The Annals of Probability"
doi: "10.1214/009117904000000577"
url: "https://doi.org/10.1214/009117904000000577"
tags: [cluster/multi-agent, project/multi-agent, field/mathematics, field/physics]
created: 2026-11-10
updated: 2026-11-10
---

# On the scaling of the chemical distance in long-range percolation models

> [!info] Citation
> Biskup, M. (2004). *On the scaling of the chemical distance in long-range percolation models*. The Annals of Probability, 32(4), 2938-2977. [DOI](https://doi.org/10.1214/009117904000000577)

[Local PDF](../pdfs/biskup-2004-scaling-chemical-distance.pdf), 42 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

A theorem on the graph distance within the infinite cluster of long-range percolation on $\mathbb Z^d$, showing that it grows as a power of the logarithm of the Euclidean distance when connection probabilities decay as a power with exponent between $d$ and $2d$.

## Problem & setting

Distinct sites $x,y\in\mathbb Z^d$ are joined with probability $p_{xy}=|x-y|^{-s+o(1)}$, and the resulting random graph is assumed to contain an infinite component $C_\infty$. The quantity studied is the graph distance $D(x,y)$ measured within $C_\infty$. The introduction ties the question to percolation theory and to small-world phenomena.

## Method

The extract covers the abstract and the opening of the introduction. The keywords list renormalization among the tools, and the abstract mentions bounds on the probability that the largest cluster in a finite box occupies a positive fraction of the sites.

## Key results

For $s\in(d,2d)$, the abstract states that $D(x,y)=(\log|x-y|)^{\Delta+o(1)}$, where $\Delta^{-1}$ is the binary logarithm of $2d/s$ and the error term tends to zero in probability as $|x-y|\to\infty$.

## Relevance to this research

The collective-agents manuscript cites this result for the chemical distance on a fixed graph with random long links, which it uses to apply a clustering statement in the graph metric; it notes that the result does not apply outside the stated range of the decay exponent. The reading record says only the abstract was read, and the extract supports the statement of the main result. The link to the vault is the effect of graph geometry on how far influence travels among communicating agents, see [[Network structure — small-world and scale-free]], [[Critical Phenomena]] and [[Renormalization group flow]].

## Cross-links

[[Collective agents literature map]]; [[Network structure — small-world and scale-free]]; [[Critical Phenomena]]; [[Renormalization group flow]]; [[campanino-2003-ornstein-zernike-finite]].

## BibTeX

```bibtex
@article{biskup2004scaling,
  author  = {Biskup, Marek},
  title   = {On the scaling of the chemical distance in long-range percolation models},
  journal = {The Annals of Probability},
  volume  = {32},
  number  = {4},
  pages   = {2938--2977},
  year    = {2004},
  doi     = {10.1214/009117904000000577}
}
```
