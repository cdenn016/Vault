---
type: paper
title: "Approximating the Kullback Leibler Divergence Between Gaussian Mixture Models"
aliases:
  - Hershey Olsen 2007
  - hershey2007
  - Variational KL approximation for GMMs
authors:
  - Hershey, John R.
  - Olsen, Peder A.
year: 2007
url: https://doi.org/10.1109/ICASSP.2007.366913
tags:
  - cluster/info-geometry
  - project/transformer
  - field/statistics
  - field/cs-ml
created: 2026-09-27
---

# Approximating the Kullback Leibler Divergence Between Gaussian Mixture Models

> [!info] Citation
> Hershey, J. R., & Olsen, P. A. (2007). *Approximating the Kullback Leibler divergence between Gaussian mixture models*. IEEE ICASSP 2007, vol. 4, pp. IV-317–IV-320. doi:10.1109/ICASSP.2007.366913.

## TL;DR
The KL divergence between two Gaussian mixtures has no closed form. The paper compares Monte Carlo, matched-bound, unscented, product-of-Gaussians and variational approximations and proposes variational approximations built from closed-form component-to-component divergences.

## Method
For $f=\sum_a\pi_af_a$ and $g=\sum_b\omega_bg_b$, the variational approximation is
$$D_{\mathrm{var}}(f\|g)=\sum_a\pi_a\log\frac{\sum_{a'}\pi_{a'}e^{-D(f_a\|f_{a'})}}{\sum_b\omega_be^{-D(f_a\|g_b)}}.$$

## Key results
Among the methods compared, the variational approximations are accurate at modest cost relative to Monte Carlo on the speech-model benchmarks reported.

## Relevance to this research
For a single-Gaussian first argument, $D_{\mathrm{var}}$ reduces to $-\log\sum_b\omega_be^{-D(f\|g_b)}$, which is the optimal free energy (soft minimum of KLs) of the mixture-prior construction in [[Template routing]]. [[dennis-2026-template-routing]] proves that this quantity upper-bounds $D(f\|g)$ in the single-component case by Jensen's inequality.

> [!note] Editorial: The single-component reduction and the upper-bound statement are derived in [[dennis-2026-template-routing]]; this note does not claim the paper states them in that form.

## Cross-links
- Concepts: [[Mean-Field Approximation]], [[Evidence lower bound (ELBO)]]
- Methods: [[Template routing]]
- Related sources: [[dennis-2026-template-routing]]

## BibTeX
```bibtex
@inproceedings{hershey2007approximating,
  author    = {Hershey, John R. and Olsen, Peder A.},
  title     = {Approximating the {K}ullback {L}eibler Divergence Between {G}aussian Mixture Models},
  booktitle = {IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  volume    = {4},
  pages     = {IV-317--IV-320},
  year      = {2007},
  doi       = {10.1109/ICASSP.2007.366913}
}
```
