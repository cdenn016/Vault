---
type: reference
title: "Strong Data-Processing Inequalities for Channels and Bayesian Networks"
aliases: ["polyanskiy2017strong"]
authors: ["Yury Polyanskiy", "Yihong Wu"]
year: 2017
venue: "Convexity and Concentration"
doi: "10.1007/978-1-4939-7005-6_7"
arxiv: "1508.06025"
url: "https://doi.org/10.1007/978-1-4939-7005-6_7"
tags: [cluster/info-geometry, cluster/multi-agent, project/multi-agent, field/cs-ml, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# Strong Data-Processing Inequalities for Channels and Bayesian Networks

> [!info] Citation
> Polyanskiy, Y., Wu, Y. (2017). *Strong Data-Processing Inequalities for Channels and Bayesian Networks*. In E. Carlen, M. Madiman, E. M. Werner (eds.), Convexity and Concentration, The IMA Volumes in Mathematics and its Applications 161, 211--249. Springer, New York. [DOI](https://doi.org/10.1007/978-1-4939-7005-6_7), [arXiv](https://arxiv.org/abs/1508.06025)

[Local PDF](../pdfs/polyanskiy-2017-strong-data-processing.pdf), 32 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

A survey-and-extension note on strong data-processing inequalities: it reviews contraction coefficients of a single channel, then shows how per-channel inequalities combine into end-to-end bounds for Bayesian networks, with the bounds read as site percolation probabilities.

## Problem & setting

The ordinary data-processing inequality $I(U;Y)\le I(U;X)$ for a Markov chain $U\to X\to Y$ is a standard tool for converse results. Channel-dependent strengthenings exist, and the question treated is how, given such an inequality for each channel of a Bayesian network, to obtain one for the whole network.

## Method

The approach uses an extract of the Evans-Schulman method, carried out for three kinds of inequality: Ahlswede-Gacs-type contraction coefficients for mutual information, Dobrushin coefficients for total variation, and the FI-curve, the best nonlinear inequality for a given channel. The note also treats the equivalence between a linear inequality and comparison with an erasure channel.

## Key results

The resulting bounds on contraction coefficients are interpreted as the probability of site percolation. As an example the authors derive an inequality for an $n$-letter memoryless channel with feedback from the case $n=1$, and the erasure comparison gives a short proof of an inequality of Samorodnitsky.

## Relevance to this research

The manuscript cites its Theorem 5 and Corollary 7 for a bound on information flow through a network of noisy links, and extends the percolation bound to Gaussian channels, where the input-independent coefficient equals one. The related-work section cites the note for bounding information flow in Bayesian networks by site percolation. This is the basis of the manuscript's limits on how far information about a convention or state propagates through a chain or tree of communicating agents; see [[Data processing inequality]], [[Mutual information]] and [[Channel Capacity]]. A companion note is [[polyanskiy-2019-application-information-percolation]].

## Cross-links

[[Collective agents literature map]]; [[Data processing inequality]]; [[Mutual information]]; [[Channel Capacity]]; [[polyanskiy-2019-application-information-percolation]].

## BibTeX

```bibtex
@incollection{polyanskiy2017strong,
  author        = {Polyanskiy, Yury and Wu, Yihong},
  editor        = {Carlen, Eric and Madiman, Mokshay and Werner, Elisabeth M.},
  title         = {Strong Data-Processing Inequalities for Channels and {Bayesian} Networks},
  booktitle     = {Convexity and Concentration},
  series        = {The IMA Volumes in Mathematics and its Applications},
  volume        = {161},
  pages         = {211--249},
  publisher     = {Springer},
  address       = {New York},
  year          = {2017},
  doi           = {10.1007/978-1-4939-7005-6_7},
  eprint        = {1508.06025},
  archivePrefix = {arXiv}
}
```
