---
type: paper
title: "A Mathematical Theory of Communication"
aliases:
  - "Shannon 1948"
  - "Shannon information theory"
  - "AMTC"
  - "shannon1948mathematical"
  - "A Mathematical Theory of Communication"
authors:
  - Shannon, Claude E.
year: 1948
arxiv: null
url: https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A Mathematical Theory of Communication

> [!info] Citation
> Shannon, Claude E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal*, 27(3), 379–423 (Part I); 27(4), 623–656 (Part II). DOI: 10.1002/j.1538-7305.1948.tb01338.x

## TL;DR

Shannon establishes information theory as a mathematical discipline by defining entropy as the unique measure of information content satisfying natural axioms, proving the channel capacity theorem, and showing that reliable communication is achievable at any rate below capacity. The key objects — entropy $H$, mutual information $I$, channel capacity $C$ — are all defined in terms of probability distributions, grounding the entire framework in the same statistical language used by modern variational inference. This is the paper that made KL divergence, entropy, and free energy mathematically precise concepts.

## Problem & setting

The fundamental engineering problem is: given a noisy communication channel, how much information can be transmitted reliably per unit time? Prior to 1948 this question lacked a precise mathematical formulation. Shannon's setting is a discrete or continuous source producing symbols drawn from a probability distribution, a possibly noisy channel characterized by a conditional distribution $p(y|x)$, and a decoder attempting to reconstruct the original message. The question requires a rigorous definition of "information" that is independent of the semantic content of messages and depends only on statistical structure.

## Method

Shannon defines the **entropy** of a discrete random variable $X$ with distribution $p$ as
$$H(X) = -\sum_x p(x) \log p(x),$$
and shows this is the unique functional (up to a positive constant) satisfying: (i) continuity in $p$, (ii) maximality at the uniform distribution, and (iii) consistency under grouping (the chain rule). For continuous variables, the analogous **differential entropy** is $h(X) = -\int p(x)\log p(x)\,dx$, though this lacks the absolute, non-negative character of the discrete case.

**Mutual information** between source $X$ and channel output $Y$ is
$$I(X; Y) = H(X) - H(X|Y) = \sum_{x,y} p(x,y)\log\frac{p(x,y)}{p(x)p(y)},$$
which equals the KL divergence between the joint and product distributions: $I(X;Y) = D_{\mathrm{KL}}(p(x,y) \| p(x)p(y))$.

**Channel capacity** is defined as the maximum mutual information over all input distributions:
$$C = \max_{p(x)} I(X; Y).$$

The **source coding theorem** (noiseless coding) states that the minimum average codeword length for lossless compression of a source $X$ is $H(X)$ bits per symbol (to base-2 logarithm). The **channel coding theorem** (noisy channel coding) states that for any rate $R < C$ there exists a code achieving arbitrarily small error probability, while for $R > C$ reliable communication is impossible.

For Gaussian channels with power constraint $P$ and noise variance $N$, capacity is
$$C = \frac{1}{2}\log\!\left(1 + \frac{P}{N}\right).$$

## Key results

1. Entropy $H$ is the unique measure of uncertainty satisfying the natural axioms; it sets the fundamental limit on lossless data compression (source coding theorem).
2. Channel capacity $C = \max_{p(x)} I(X;Y)$ is the supremum of reliable communication rates; below $C$ reliable transmission is possible, above $C$ it is not (noisy channel coding theorem).
3. The KL divergence $D_{\mathrm{KL}}(p\|q) = \sum_x p(x)\log(p(x)/q(x))$ — though not named as such here — appears implicitly as the difference between cross-entropy and entropy, and as the structure of mutual information. Its non-negativity ($D_{\mathrm{KL}} \ge 0$, equality iff $p=q$) follows from Jensen's inequality applied to the convexity of $-\log$.
4. The differential entropy of a Gaussian with variance $\sigma^2$ is $\frac{1}{2}\log(2\pi e \sigma^2)$, the maximum differential entropy for fixed variance — establishing the Gaussian as the maximum-entropy distribution under a variance constraint.

## Relevance to this research

Shannon's framework is the bedrock on which the VFE transformer's entire objective rests. Every term in the variational free energy
$$F = \alpha\,D_{\mathrm{KL}}(q_i \| p_i) + \lambda_h\,D_{\mathrm{KL}}(s_i \| h) + \sum_{ij}\beta_{ij}\,D_{\mathrm{KL}}(q_i \| \Omega_{ij} q_j) + \tau\sum_{ij}\beta_{ij}\log\frac{\beta_{ij}}{\pi_{ij}} - \mathbb{E}_q[\log p(o|x)]$$
is, in Shannon's terms, a difference of entropies or a cross-entropy. The self-coupling term $D_{\mathrm{KL}}(q_i\|p_i)$ is the information-theoretic cost of the beliefs deviating from their priors; the attention-entropy term $\tau\beta_{ij}\log(\beta_{ij}/\pi_{ij})$ is the KL divergence of the attention weights from a uniform prior, enforcing that $\beta$ at stationarity takes the softmax form. Without Shannon's entropy axioms, none of these terms has a principled justification.

Specific connections:

- **KL divergence as the divergence primitive.** The transport terms $D_{\mathrm{KL}}(q_i\|\Omega_{ij}q_j)$ measure information lost by transporting belief $q_j$ to token $i$'s frame before comparing; Shannon's mutual information is $I(X;Y) = D_{\mathrm{KL}}(p_{XY}\|p_Xp_Y)$, establishing KL as the canonical measure of statistical dependence and cost.
- **Maximum-entropy Gaussians.** The choice of Gaussian belief tuples $(\mu,\Sigma)$ throughout the VFE stack is justified by Shannon's result that the Gaussian maximizes entropy for fixed second moments — the least-committed belief given only mean and covariance information, which is exactly what the M-step infers.
- **Free energy as compressed description length.** The ELBO / VFE can be written as $F = \mathbb{E}_q[-\log p(o,x)] - H(q)$, i.e., the expected negative log-joint minus the entropy of the approximate posterior. Shannon's source coding theorem makes $-\log p$ the description length, so minimizing $F$ is literally minimizing the expected description length of the data under a compressed probabilistic model.
- **Information geometry lineage.** The Fisher information metric — the Riemannian metric used in [[amari-1998-natural-gradient]] and throughout the VFE optimizer design — is the Hessian of the KL divergence at $p=q$, a second-order Taylor expansion of Shannon's entropy difference. All of [[amari-2000-methods-information-geometry]] is an elaboration of the geometry implicit in Shannon's $H$ and $D_{\mathrm{KL}}$.
- **Attention entropy regularization.** The $\tau\beta_{ij}\log(\beta_{ij}/\pi_{ij})$ term in $F$ is precisely Shannon entropy (negated, with uniform reference $\pi_{ij}=1/N$). Its role — ensuring $\beta$ is the softmax stationary point of $F$ rather than a Dirac delta — is the variational analogue of Shannon's maximum-entropy principle: among all distributions that achieve a given expected KL cost, the one that maximizes entropy is the softmax. This derivation is spelled out explicitly in `Manuscripts-Theory/GL(K)_attention.tex`.

## Cross-links

- Concepts: [[Entropy]], [[KL divergence]], [[Mutual information]], [[Channel capacity]], [[Maximum entropy principle]]
- Related sources: [[amari-1998-natural-gradient]], [[amari-2000-methods-information-geometry]], [[li-turner-2016-renyi-vi]], [[neal-1998-variational-em]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) attention manuscript]]

## BibTeX

```bibtex
@article{Shannon1948,
  author  = {Shannon, Claude E.},
  title   = {A Mathematical Theory of Communication},
  journal = {Bell System Technical Journal},
  volume  = {27},
  number  = {3--4},
  pages   = {379--423, 623--656},
  year    = {1948},
  doi     = {10.1002/j.1538-7305.1948.tb01338.x},
  url     = {https://doi.org/10.1002/j.1538-7305.1948.tb01338.x}
}
```
