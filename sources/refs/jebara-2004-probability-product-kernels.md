---
type: reference
title: "Probability Product Kernels"
aliases:
  - "Jebara, Kondor and Howard 2004"
  - "Probability Product Kernels"
  - "Jebara2004ProbabilityProduct"
authors:
  - Tony Jebara
  - Risi Kondor
  - Andrew Howard
year: 2004
url: https://www.jmlr.org/papers/v5/jebara04a.html
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-09-23
updated: 2026-09-23
---

# Probability Product Kernels

> [!info] Citation
> Tony Jebara, Risi Kondor, Andrew Howard (2004). "Probability Product Kernels." *Journal of Machine Learning Research* **5**, 819–844. [JMLR page](https://www.jmlr.org/papers/v5/jebara04a.html).

## TL;DR

The paper defines a kernel between probability distributions as the integral of the product of their densities raised to a power $\rho$. Setting $\rho=1/2$ gives the Bhattacharyya kernel, which is tied to the Hellinger distance; setting $\rho=1$ gives the expected likelihood kernel $\mathbb E_p[p']=\mathbb E_{p'}[p]$. The kernel has closed forms for exponential families, including full-covariance Gaussians. It also has closed forms for mixtures, hidden Markov models, and linear Gaussian models. Sampling and structured mean-field approximations cover intractable models.

## What it establishes

Definition 1 (Eq. 2) sets $k_\rho(p,p')=\int_{\mathcal X}p(x)^\rho p'(x)^\rho\mathrm dx=\langle p^\rho,p'^\rho\rangle_{L_2}$ for densities whose $2\rho$ powers are integrable. The kernel is positive definite because it is an inner product in $L_2(\mathcal X)$.

Section 2.1 covers two special cases:
- $\rho=1/2$ gives the Bhattacharyya kernel, with Hellinger distance $H(p,p')^2=2-2k(p,p')$.
- $\rho=1$ gives the expected likelihood kernel (Eq. 3).

Section 2.2 fits the distributions to single data points by maximum likelihood or by Bayesian estimation.

Section 3 treats exponential families. Section 3.1 handles the Gaussian case: for $p=\mathcal N(\mu,\Sigma)$ and $p'=\mathcal N(\mu',\Sigma')$, completing the square gives the general kernel (Eq. 5), with $\Sigma^\dagger=(\Sigma^{-1}+\Sigma'^{-1})^{-1}$ and $\mu^\dagger=\Sigma^{-1}\mu+\Sigma'^{-1}\mu'$. For isotropic fixed covariance and $\rho=1$, the kernel recovers the Gaussian RBF kernel up to a constant. Sections 3.2 to 3.4 give the Bernoulli, multinomial, gamma, and exponential cases.

The remaining sections cover:
- Section 4: mixtures, hidden Markov models, Bayesian networks, linear Gaussian models, and linear dynamical systems.
- Section 5: a sampling approximation.
- Section 6: structured mean-field approximations for intractable models such as switching linear dynamical systems.
- Section 7: comparison with the Fisher kernel, the heat kernel, and exponentiated-KL kernels.
- Section 8: experiments on text (multinomial models), biological sequences (hidden Markov models), and time series (linear dynamical systems).

> [!note] Editorial: The paper writes the $\rho=1$ Gaussian case explicitly only for isotropic fixed covariance. For general covariances, Eq. 5 at $\rho=1$ reduces to $\mathcal N(\mu;\mu',\Sigma+\Sigma')$, because $\det\Sigma^\dagger=\det\Sigma\det\Sigma'/\det(\Sigma+\Sigma')$. This is the standard Gaussian product integral.

## Relevance to this research

The noisy-query routing remark in Section 5.2 of the v2 GL(K) manuscript (`manuscripts/GL(K)_attention_v2.tex`) uses this kernel. The remark treats the projected query mean $a_i$ as a noisy measurement, with noise covariance $V_{Q,i}$, of a draw from the key law $p_{K,j}=\mathcal N(b_j,V_{K,j})$. Then
$$p(a_i\mid J=j)=\mathbb E_{q_{Q,i}}[p_{K,j}]=\mathcal N(a_i;b_j,V_{Q,i}+V_{K,j}),$$
which is the expected likelihood kernel between the query and key laws. The exact source posterior is therefore $\beta_{ij}\propto\pi_{ij}\mathcal N(a_i;b_j,V_{Q,i}+V_{K,j})$.

Gibbs (KL) routing instead normalizes $\pi_{ij}\exp\mathbb E_{q_{Q,i}}[\log p_{K,j}]$. The query covariance then enters only through a trace term, which cancels when key covariances are shared. So Gibbs routing does not flatten as the query law broadens, whereas the noisy-query posterior does.

The two rules agree in the point-query limit. There both reduce to the mixture responsibility of [[movellan-2020-probabilistic-transformers]] and [[nguyen-2022-probabilistic-attention-keys]].

The evaluated model does not implement the noisy-query rule. See [[GL(K) gauge-equivariant attention]] and [[Attention mechanisms — theory and positional structure]].

## Local full text

The JMLR PDF is stored at `sources/pdfs/Jebara2004ProbabilityProduct.pdf` ([local PDF](../pdfs/Jebara2004ProbabilityProduct.pdf)). Source: [JMLR](https://www.jmlr.org/papers/volume5/jebara04a/jebara04a.pdf). SHA-256: `fa17f3a8b0ba99a49e10b6aef096d9a55ca277ccb23d59c28e3a6713ff21ead7`.

## BibTeX

```bibtex
@article{Jebara2004ProbabilityProduct,
  author = {Jebara, Tony and Kondor, Risi and Howard, Andrew},
  title = {Probability Product Kernels},
  journal = {Journal of Machine Learning Research},
  volume = {5},
  pages = {819--844},
  year = {2004},
  url = {https://www.jmlr.org/papers/v5/jebara04a.html}
}
```
