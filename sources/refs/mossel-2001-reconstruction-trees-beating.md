---
type: reference
title: "Reconstruction on Trees: Beating the Second Eigenvalue"
aliases: ["mossel2001reconstruction"]
authors: ["Elchanan Mossel"]
year: 2001
venue: "The Annals of Applied Probability"
doi: "10.1214/aoap/998926994"
url: "https://doi.org/10.1214/aoap/998926994"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/mathematics, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# Reconstruction on Trees: Beating the Second Eigenvalue

> [!info] Citation
> Mossel, E. (2001). *Reconstruction on Trees: Beating the Second Eigenvalue*. The Annals of Applied Probability, 11(1), 285-300. [DOI](https://doi.org/10.1214/aoap/998926994)

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: abstract.

## TL;DR

The paper studies the transmission of a symbol from the root of a noisy tree network through independent copies of a Markov channel on each edge, and asks whether the root symbol can be recovered from the symbols at depth $n$. It shows that for the asymmetric binary channel and for the symmetric channel on many symbols, reconstruction can sometimes succeed even when $d\lambda_2^2(M)<1$.

## Problem & setting

A uniform symbol from a finite alphabet is placed at the root of a $d$-ary tree, and each edge applies an independent copy of an irreducible, aperiodic channel $M$. Reconstruction asks whether the probability of guessing the root correctly stays bounded away from the chance level $1/|\mathcal A|$ as the depth grows. The abstract records that reconstruction is known to be possible when $d\lambda_2^2(M)>1$, where $\lambda_2$ is the second eigenvalue of $M$, and that this threshold is sharp for the symmetric binary channel.

## Key results

According to the abstract, the second-eigenvalue threshold is not sharp in general: for the binary asymmetric channel and for the symmetric channel on many symbols, reconstruction is sometimes possible below it. The abstract draws the conclusion that the location of the data on the boundary of the tree matters for reconstruction in many tree-indexed Markov chains, in contrast with the majority algorithm that ignores location.

## Relevance to this research

The collective-agents manuscript cites this paper for the statement that the condition on $b$ times the squared second eigenvalue of the channel is sufficient for reconstruction on a $b$-ary tree but is not tight for every channel, even though it is tight for the binary symmetric channel. The reference sits in the manuscript's discussion of how far information about a source survives passage through repeated noisy links, which connects to [[Data processing inequality]] and [[Channel Capacity]] as used for communicating agents. The manuscript's reading record states only that the bibliographic data were checked against Crossref; the content here rests on the abstract alone.

## Cross-links

[[Collective agents literature map]]; [[Data processing inequality]]; [[Channel Capacity]].

## BibTeX

```bibtex
@article{mossel2001reconstruction,
  author  = {Mossel, Elchanan},
  title   = {Reconstruction on Trees: Beating the Second Eigenvalue},
  journal = {The Annals of Applied Probability},
  volume  = {11},
  number  = {1},
  pages   = {285--300},
  year    = {2001},
  doi     = {10.1214/aoap/998926994}
}
```
