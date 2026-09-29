---
type: paper
title: "The cutoff phenomenon in finite Markov chains"
aliases:
  - "Diaconis 1996"
  - "Cutoff phenomenon in finite Markov chains"
authors:
  - Diaconis P.
year: 1996
doi: "10.1073/pnas.93.4.1659"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC39998/"
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
created: 2026-09-28
updated: 2026-09-28
---

# The cutoff phenomenon in finite Markov chains

> [!info] Citation
> P. Diaconis (1996). "The cutoff phenomenon in finite Markov chains." *Proceedings of the National Academy of Sciences USA* **93**(4), 1659–1664. doi:10.1073/pnas.93.4.1659. PMID 11607633, PMCID PMC39998.

## Verification record

Metadata verified on 2026-09-28 against the Crossref record. Full text read from the PMC page images for pp. 1659–1662 and 1664; the image for p. 1663, which holds Section 5 and its Theorem 5, could not be retrieved, so nothing is recorded about that section. Gathered by Claude Opus 5.5, verified by Claude Fable 5.1 (verdict VERIFIED). Also checked in the transitions lens, where it was left to this note to avoid duplication.

## Verified content

The introduction closes (p. 1660) with a formal definition of an $(a_n,b_n)$ cutoff: at $k_n=a_n+\theta b_n$ with $b_n/a_n\to0$, $\|P_n^{k_n}-\pi_n\|\to c(\theta)$, where $c(\theta)\to0$ as $\theta\to+\infty$ and $c(\theta)\to1$ as $\theta\to-\infty$. Theorem 1 (p. 1659) gives Gilbert–Shannon–Reeds riffle shuffles a cutoff at $\frac32\log_2n$ with the explicit profile $\|P^k-\pi\|=1-2\Phi\big(-2^{-\theta}/(4\sqrt3)\big)+O(1/\sqrt n)$ at $k=\frac32\log_2n+\theta$. Section 2A, Theorem 2, shows that the Ehrenfest urn started at $0$ has a cutoff at $\frac14d\log d$, while the chain started at $d/2$ needs order $d$ steps, which are also sufficient, and has no cutoff: $\|P^k_{d/2}-\pi\|\sim f(\theta)$ at $k=\theta d$ with $f$ continuous. Section 4 (p. 1662) attributes cutoffs to high multiplicity of the second eigenvalue. The final section (p. 1664) compares total variation with the chi-square distance and entropy, $\mathrm{Ent}(\pi,P)\le\log(1+\chi(P,\pi))$, and remarks that one feature of a chain can mix at a different time from the whole chain.

## Relevance to this research

The Ehrenfest contrast states the mechanism behind the activation threshold of [[multiagentelbo-2026-09-28-early-parent]] in its original setting. The cutoff exists because the chain starts far from equilibrium; started near equilibrium, relaxation is gradual and has no threshold. Read for the model, a collective whose members begin close to consensus has no sharp activation time, and the sharpness in $s=\theta/\log(1/\epsilon)$ comes from a founding imprint that is large compared with the noise scale $\sqrt T$. The remark on feature-specific mixing matches the parent construction: retained features (slow shared coordinates, the source assignment, the loop) and discarded features (the fast within-pair disagreements) have different thresholds, so "formed" has to be stated feature by feature. The attribution of cutoffs to a highly degenerate second eigenvalue points to where a large network could produce a threshold even without small noise, which the Ornstein–Uhlenbeck results of [[boursier-2023-universal-cutoff-dyson-ornstein-uhlenbeck]] and [[lachaud-2005-cutoff-hitting-times-ornstein-uhlenbeck]] make explicit. The final section compares chi-square and entropy distances, not the relative entropy of a parent's discarded conditional law. These mappings are interpretive. See [[Soft formation and the activation clock]].

## Cross-links

- Concepts: [[Soft formation and the activation clock]], [[Coarse Graining]]
- Related sources: [[aldous-1986-shuffling-cards-stopping-times]], [[levin-undated-markov-chains-and-mixing-times-retrieved-author-text]], [[barrera-2020-thermalisation-small-random-perturbations]], [[boursier-2023-universal-cutoff-dyson-ornstein-uhlenbeck]]

## BibTeX

```bibtex
@article{diaconis1996cutoff,
  author  = {Diaconis, P.},
  title   = {The cutoff phenomenon in finite {Markov} chains},
  journal = {Proceedings of the National Academy of Sciences USA},
  volume  = {93},
  number  = {4},
  pages   = {1659--1664},
  year    = {1996},
  doi     = {10.1073/pnas.93.4.1659}
}
```
