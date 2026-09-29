---
type: paper
title: "Cut-off and hitting times of a sample of Ornstein-Uhlenbeck processes and its average"
aliases:
  - "Lachaud 2005"
  - "Cutoff for a sample of Ornstein-Uhlenbeck processes"
authors:
  - Lachaud B.
year: 2005
doi: "10.1239/jap/1134587817"
url: "https://doi.org/10.1239/jap/1134587817"
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
created: 2026-09-28
updated: 2026-09-28
---

# Cut-off and hitting times of a sample of Ornstein-Uhlenbeck processes and its average

> [!info] Citation
> Béatrice Lachaud (2005). "Cut-off and hitting times of a sample of Ornstein-Uhlenbeck processes and its average." *Journal of Applied Probability* **42**(4), 1069–1080. doi:10.1239/jap/1134587817.

## Verification record

Metadata and abstract verified on 2026-09-28 against the Crossref record (author, journal, volume 42, issue 4, pages 1069–1080, 2005). Cambridge Core returned 403, so the full text was not read and theorem numbers are unverified. Access: abstract only. Gathered by Claude Opus 5.5, verified by Claude Fable 5.1 (verdict VERIFIED).

## TL;DR (abstract level)

A sample of $n$ independent Ornstein–Uhlenbeck processes and its average both show a cutoff. Their distributions stay far from equilibrium before a time of order $\log n$ and converge exponentially fast afterwards: the total-variation distance drops from almost 1 to almost 0 over an interval of length $O(1)$ around $\log(n)/(2\alpha)$, where $\alpha$ is the viscosity (restoring) coefficient. The distribution of the hitting time of 0 by the sample average is computed; as $n$ grows it concentrates around the cutoff instant, with tails that match the total-variation estimates.

## Relevance to this research

This is an early Ornstein–Uhlenbeck cutoff with an explicit $O(1)$ window, with the sample size $n$ as the large parameter where the four-cycle of [[multiagentelbo-2026-09-28-early-parent]] uses $1/T$. It supports reading the model's threshold as a cutoff at $\frac{1}{2\lambda}\log(\text{large parameter})$, and it shows that many independent relaxing coordinates produce a logarithmic threshold with no small-noise limit at all, which is the relevant regime for networks with many discarded coordinates. The hitting-time result is a possible primary anchor for a detector-firing time, the first time a coherence statistic of several fast coordinates reaches a level; that link is interpretive and was not checked against the text, although the abstract's concentration of the hitting time at the cutoff instant is consistent with it. See [[Soft formation and the activation clock]].

## Cross-links

- Concepts: [[Soft formation and the activation clock]]
- Related sources: [[boursier-2023-universal-cutoff-dyson-ornstein-uhlenbeck]], [[barrera-2020-thermalisation-small-random-perturbations]], [[diaconis-1996-cutoff-phenomenon-markov-chains]]

## BibTeX

```bibtex
@article{lachaud2005cutoff,
  author  = {Lachaud, B{\'e}atrice},
  title   = {Cut-off and hitting times of a sample of {Ornstein-Uhlenbeck} processes and its average},
  journal = {Journal of Applied Probability},
  volume  = {42},
  number  = {4},
  pages   = {1069--1080},
  year    = {2005},
  doi     = {10.1239/jap/1134587817}
}
```
