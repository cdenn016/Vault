---
type: paper
title: "Random Perturbations of Dynamical Systems (3rd edition)"
aliases:
  - "Freidlin and Wentzell 2012"
  - "Freidlin-Wentzell"
authors:
  - Freidlin M.I.
  - Wentzell A.D.
year: 2012
doi: "10.1007/978-3-642-25847-3"
url: "https://link.springer.com/book/10.1007/978-3-642-25847-3"
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
created: 2026-09-28
updated: 2026-09-28
---

# Random Perturbations of Dynamical Systems (3rd edition)

> [!info] Citation
> M. I. Freidlin and A. D. Wentzell (2012). *Random Perturbations of Dynamical Systems*, 3rd revised and enlarged edition. Grundlehren der mathematischen Wissenschaften **260**. Springer, Berlin Heidelberg. doi:10.1007/978-3-642-25847-3. ISBN 978-3-642-25846-6 (hardcover), 978-3-642-25847-3 (eBook).

## Verification record

Metadata verified on 2026-09-28 against the Crossref record and the Springer book page, which confirm the authors, the 2012 third edition, the series volume number 260 (added by the verifier), the hardcover ISBN and the DOI. Only the publisher's table of contents and blurb were read; no theorem numbers were inspected. Gathered by Claude Opus 5.5, verified by Claude Fable 5.1 (verdict VERIFIED).

## Verified content

The table of contents includes Chapter 4, "Gaussian Perturbations of Dynamical Systems: Neighborhood of an Equilibrium Point"; Chapter 6, "Markov Perturbations on Large Time Intervals"; and Chapter 7, "The Averaging Principle: Fluctuations in Dynamical Systems with Averaging". The third-edition blurb states that the sub-limiting distribution for a given initial point and time scale is identical to the idea of metastability, and that the quasi-potential governs long-time behavior. [[barrera-2020-thermalisation-small-random-perturbations]] (Sec. 2.3) cites this book for the statement that other attractors become accessible only at times of order $e^{c/\epsilon}$.

## Relevance to this research

The book gives a mathematical meaning to a collective that has formed but is not permanent: a formed state is a sub-limiting distribution attached to an initial basin and a time scale. Applied to the four-cycle of [[multiagentelbo-2026-09-28-early-parent]], this suggests three time scales: $O(1)$ local relaxation, a $\log(1/T)$ cutoff at which the discarded coordinates lose the founding imprint, and an $\exp(\Delta/T)$ quasi-potential escape at which the source assignment or matching can change. The parent would be valid on the middle plateau, remembering which basin it formed in while having forgotten the founding detail. That hierarchy is the gatherer's construction, not the book's, and the model's own windows of order $1/T$ and longer are undecided. Chapter 7's averaging principle is a primary source for adiabatic elimination after the initial layer. The chapter-level mapping is interpretive. See [[Soft formation and the activation clock]].

## Cross-links

- Concepts: [[Soft formation and the activation clock]], [[Geometric singular perturbation theory]]
- Related sources: [[barrera-2016-abrupt-convergence-small-perturbations]], [[barrera-2020-thermalisation-small-random-perturbations]], [[bovier-2015-metastability-potential-theoretic-approach]], [[bovier-2004-metastability-diffusions]], [[young-1993-evolution-conventions]]

## BibTeX

```bibtex
@book{freidlin2012random,
  author    = {Freidlin, M. I. and Wentzell, A. D.},
  title     = {Random Perturbations of Dynamical Systems},
  edition   = {3},
  series    = {Grundlehren der mathematischen Wissenschaften},
  volume    = {260},
  publisher = {Springer},
  address   = {Berlin, Heidelberg},
  year      = {2012},
  doi       = {10.1007/978-3-642-25847-3},
  isbn      = {978-3-642-25846-6}
}
```
