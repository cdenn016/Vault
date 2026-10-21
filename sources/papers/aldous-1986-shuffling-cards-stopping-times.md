---
type: paper
title: "Shuffling cards and stopping times"
aliases:
  - "Aldous and Diaconis 1986"
  - "Strong uniform times"
authors:
  - Aldous D.
  - Diaconis P.
year: 1986
doi: "10.1080/00029890.1986.11971821"
url: "https://doi.org/10.1080/00029890.1986.11971821"
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
created: 2026-09-28
updated: 2026-09-28
---

# Shuffling cards and stopping times

> [!info] Citation
> D. Aldous and P. Diaconis (1986). "Shuffling cards and stopping times." *The American Mathematical Monthly* **93**(5), 333–348. doi:10.1080/00029890.1986.11971821.

## Verification record

Metadata verified on 2026-09-28 against the Crossref record (93(5), 333–348, 1986); the publisher page returned 403. Pages 333–336 were read as images from the JSTOR scan hosted at stat.duke.edu; the rest of the article was not read. Gathered by Claude Opus 5.5, verified by Claude Fable 5.1 (verdict VERIFIED).

## Verified content

Example 1 is the top-in-at-random shuffle, analyzed on p. 333 through the time $T=T_{n-1}+1$ at which the card originally at the bottom has risen to the top and been reinserted. Equations 2.3 and 2.4 (p. 335) define the variation distance and $d(k)$. Theorem 1 (p. 335) states that (a) $d(n\log n+cn)\le e^{-c}$ for all $c\ge0$ and $n\ge2$, and (b) $d(n\log n-c_nn)\to1$ as $n\to\infty$ whenever $c_n\to\infty$. The same page names the "cut-off phenomenon", with a critical $k_0$ at which $d$ drops from near 1 to near 0 (Fig. 2). On p. 336 the authors note that the Perron–Frobenius asymptotics $d(k)\sim a\lambda^k$ miss the cutoff. Definitions 1 and 2 (p. 336) define a stopping rule and a strong uniform time, one for which $P(T=k,X_k=g)$ does not depend on $g$, and Lemma 1 bounds $d(k)\le P(T>k)$. Remark (iii) confirms that the time in Example 1 is a strong uniform time.

## Cross-links

- Concepts: [[Meta-agents and hierarchical emergence]]
- Related sources: [[diaconis-1996-cutoff-phenomenon-markov-chains]], [[levin-undated-markov-chains-and-mixing-times-retrieved-author-text]], [[barrera-2020-thermalisation-small-random-perturbations]]

## BibTeX

```bibtex
@article{aldous1986shuffling,
  author  = {Aldous, D. and Diaconis, P.},
  title   = {Shuffling cards and stopping times},
  journal = {The American Mathematical Monthly},
  volume  = {93},
  number  = {5},
  pages   = {333--348},
  year    = {1986},
  doi     = {10.1080/00029890.1986.11971821}
}
```
