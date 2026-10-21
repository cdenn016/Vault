---
type: paper
title: "Universal cutoff for Dyson Ornstein Uhlenbeck process"
aliases:
  - "Boursier, Chafaï and Labbé 2023"
  - "Boursier Chafai Labbe 2023"
  - "Dyson Ornstein-Uhlenbeck cutoff"
authors:
  - Boursier J.
  - Chafaï D.
  - Labbé C.
year: 2023
arxiv: "2107.14452"
doi: "10.1007/s00440-022-01158-5"
url: "https://arxiv.org/abs/2107.14452"
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
created: 2026-09-28
updated: 2026-09-28
---

# Universal cutoff for Dyson Ornstein Uhlenbeck process

> [!info] Citation
> J. Boursier, D. Chafaï and C. Labbé (2023). "Universal cutoff for Dyson Ornstein Uhlenbeck process." *Probability Theory and Related Fields* **185**(1–2), 449–512. doi:10.1007/s00440-022-01158-5. arXiv:2107.14452 (v3, 13 Jul 2022).

## Verification record

Metadata verified on 2026-09-28 from the arXiv abstract page (journal reference PTRF 185(1–2), 449–512, 2023); the Springer and Crossref pages were rate-limited. Full text of arXiv v3 read. Gathered by Claude Opus 5.5, verified by Claude Fable 5.1 (verdict VERIFIED). The verifier corrected one attribution, adopted here: Remark 3.2 states the bias/variance split for total variation, Hellinger and $\chi^2$, where a triangle inequality is available, and not for relative entropy; for relative entropy the split is read directly off eq. 3.3.

## Verified content

The paper's subject is the Dyson Ornstein–Uhlenbeck process, an interacting many-particle diffusion; the verified locators below concern its non-interacting benchmark, $dZ=\sqrt{2/n}\,dB-Z\,dt$ in $\mathbb R^n$ (eq. 1.8, Sec. 1.4). Theorem 1.1 (mean-field regime) gives cutoff at $c_n=\log n$ in total variation, Hellinger, relative entropy (Kullback) and $\chi^2$, at $\frac12\log n$ in Wasserstein and at $\frac32\log n$ in Fisher information. Theorem 1.2 (general initial condition) gives $c_n=\log(n|z_0|)\vee\frac14\log n$ for total variation, Hellinger, Kullback and $\chi^2$, $\log(n|z_0|)\vee\frac12\log n$ for Fisher, and a Wasserstein dichotomy with no cutoff when $|z_0|$ stays bounded. Section 2.7 defines window and profile. Equation 3.3 is the exact identity

$$2\,\mathrm{Kullback}\big(\mathrm{Law}(Z_t)\,|\,P\big)=n|z_0|^2e^{-2t}-ne^{-2t}-n\log\big(1-e^{-2t}\big).$$

Remark 3.2 splits the cutoff into a bias time $c^A=\log(n|z_0|)$ and a variance time $c^B=\frac14\log n$. Table 1 and eq. 3.11 give explicit Kullback profiles: $\frac12e^{-2b}$ in the bias-dominated regime, $\frac14e^{-4b}$ in the variance-dominated regime, and $\frac12ae^{-2b}+\frac14e^{-4b}$ in between, with a window that is always of size one. The paper cites Barrera, Högele and Pardo for cutoff in total variation, entropy and Wasserstein in fixed dimension with vanishing noise, stating that the results and proofs are essentially the same in the two settings, and notes that in fixed dimension with vanishing noise there is no cutoff from initial conditions of small enough norm.

## Relevance to this research

The asymptotic parameter here is the dimension $n$, not the noise. The transfer to the model's small-temperature setting is by the explicit Gaussian formula and by the cited fixed-dimension result, not by the $n\to\infty$ theorems. Those theorems matter in their own right for the program's target of networks with hundreds of agents: they show that the number of coordinates alone produces a logarithmic cutoff, through the variance time $\frac14\log n$ and the $n$ inside $\log(n|z_0|)$. This reading is interpretive. See [[Meta-agents and hierarchical emergence]].

## Cross-links

- Concepts: [[Meta-agents and hierarchical emergence]]
- Related sources: [[barrera-2020-thermalisation-small-random-perturbations]], [[lachaud-2005-cutoff-hitting-times-ornstein-uhlenbeck]], [[diaconis-1996-cutoff-phenomenon-markov-chains]], [[levin-undated-markov-chains-and-mixing-times-retrieved-author-text]]

## BibTeX

```bibtex
@article{boursier2023universal,
  author        = {Boursier, J. and Chafa{\"\i}, D. and Labb{\'e}, C.},
  title         = {Universal cutoff for {Dyson Ornstein Uhlenbeck} process},
  journal       = {Probability Theory and Related Fields},
  volume        = {185},
  number        = {1-2},
  pages         = {449--512},
  year          = {2023},
  doi           = {10.1007/s00440-022-01158-5},
  eprint        = {2107.14452},
  archivePrefix = {arXiv}
}
```
