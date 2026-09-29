---
type: paper
title: "Experimental evidence for tipping points in social convention"
aliases:
  - "Centola et al. 2018"
  - "Committed-minority tipping point experiment"
authors:
  - Centola D.
  - Becker J.
  - Brackbill D.
  - Baronchelli A.
year: 2018
doi: "10.1126/science.aas8827"
url: "https://doi.org/10.1126/science.aas8827"
tags:
  - cluster/social-physics
  - cluster/social-physics/networks-and-contagion
  - cluster/multi-agent
  - project/social-physics
  - project/multi-agent
  - field/sociology
  - field/physics
created: 2026-09-28
updated: 2026-09-28
---

# Experimental evidence for tipping points in social convention

> [!info] Citation
> D. Centola, J. Becker, D. Brackbill, and A. Baronchelli (2018). "Experimental evidence for tipping points in social convention." *Science* **360**(6393), 1116–1119. doi:10.1126/science.aas8827. Supplementary Materials: sections "Tipping Point," "Robustness to Population Size," and "Effect of Memory Parameter" (Figs. S4, S5).

## Verification record

Metadata verified on 2026-09-28 against Crossref. Main text and Supplementary Materials read from author-hosted PDFs. Gathered by Claude Opus 5.5, verified by Claude Fable 5.1 (verdict VERIFIED; the original mapping was flagged as overstated in two places and is corrected below).

## Verified content

A committed minority of about 25% overturned an established convention; below that size, on average only 6% of the noncommitted population adopted the alternative. The model fits a memory length $9\le M\le 13$ (lower-bound estimate $M=12$). The main text gives the model's tipping point as approaching 24.3% of the population; the Supplementary Materials give 24.2%, stable for population sizes from 1,000 to 100,000. The main text notes that for short periods ($T<100$ interactions) the critical-mass prediction is not exact, while over longer periods ($T>1000$) the transition becomes more precise. The Supplementary Materials state that the model is a Markov chain with only one absorbing state, and that in finite time a subcritical minority leaves the model in a quasi-stationary state; long-term adoption at $T=1000$ rounds shows a sharp transition near 24.2%, whereas after 20 rounds full convergence is not reached even with a committed fraction of 50%. The critical mass rises with memory length, to 40% at $M=100$.

## Relevance to this research

The sharpness of this tipping point is a limit phenomenon, requiring large $N$ and long observation time, with a smooth crossover at finite size and finite time. The threshold in [[multiagentelbo-2026-09-28-early-parent]] is also sharp only in a limit (a threshold in $s=\theta/\log(1/\epsilon)$ as $\epsilon\to0$) and a smooth crossover at finite temperature. The two are analogous as limit-sharpened crossovers, not structurally identical: here the sharp object is a bifurcation in a control parameter (the committed fraction), there it is a cutoff in time. The memory length $M$ is a microscopic agent parameter that sets the inertia of an established convention against a committed minority; it is not a parent-level memory variable carrying the founding imprint, so it illustrates rather than instantiates the second remedy. The mechanism studied, a committed minority overturning a norm, also differs from formation. The mapping is interpretive. See [[Soft formation and the activation clock]] and [[Phase transitions in social systems]].

## Cross-links

- Concepts: [[Soft formation and the activation clock]], [[Phase transitions in social systems]], [[Threshold models and complex contagion]]
- Themes: [[Statistical physics of social systems and collective behavior]]
- Related sources: [[centola-2015-spontaneous-emergence-conventions]], [[young-1993-evolution-conventions]], [[centola-2010-online-experiment]]

## BibTeX

```bibtex
@article{centola2018experimental,
  author  = {Centola, D. and Becker, J. and Brackbill, D. and Baronchelli, A.},
  title   = {Experimental evidence for tipping points in social convention},
  journal = {Science},
  volume  = {360},
  number  = {6393},
  pages   = {1116--1119},
  year    = {2018},
  doi     = {10.1126/science.aas8827}
}
```
