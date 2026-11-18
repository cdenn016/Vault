---
type: concept
title: "Information bottleneck"
aliases:
  - IB
  - Information bottleneck method
  - IB Lagrangian
  - "Distributional Clustering"
  - "Distributional clustering"
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-19
updated: 2026-11-18
---

# Information bottleneck

## Definition

The **information bottleneck** (IB) formalizes the extraction of the *relevant* part of a signal. Given a source variable $X$ and a relevance variable $Y$, one seeks a compressed representation $T$ that throws away as much of $X$ as possible while keeping as much as possible of what $X$ tells us about $Y$. This is posed as a single trade-off, minimized over stochastic encoders $p(t \mid x)$

$$
\mathcal{L}_{\mathrm{IB}} \;=\; I(X; T) \;-\; \beta\, I(T; Y),
$$

where $I(X;T)$ is the *complexity* (description length) of the code, $I(T;Y)$ is its *accuracy* (relevance retained), and the Lagrange multiplier $\beta$ sets the exchange rate between the two. The stationarity condition gives a self-consistent fixed point in which the optimal assignment is a **softmax over a KL distortion**, $p(t \mid x) \propto p(t)\,\exp\!\big(-\beta\,\mathrm{KL}(p(y\mid x)\,\|\,p(y\mid t))\big)$, solvable by Blahut-Arimoto-style alternating projection. Sweeping $\beta$ traces the **information plane**, the optimal complexity-versus-accuracy curve $\big(I(X;T), I(T;Y)\big)$.

## Details

The conceptual core of the IB family is **distributional clustering**: grouping objects by the similarity of their associated conditional distributions $p(y\mid x)$ — typically in KL or Jensen-Shannon divergence — rather than by feature vectors, so clusters preserve mutual information with the relevance variable while compressing the input. This is the information-theoretic version of coarse-graining. The original IB is a *soft* assignment; its **deterministic** limit replaces $I(X;T)$ with the code entropy $H(T)$, collapsing the optimum to a hard clustering. The **Gaussian IB** solves the trade-off in closed form when $X, Y$ are jointly Gaussian: the optimum is a noisy linear projection along eigenvectors of $\Sigma_{x\mid y}\Sigma_x^{-1}$, switching on one at a time as $\beta$ grows. This ties the trade-off to a covariance-eigenstructure problem on the SPD manifold (see [[Information geometry and natural gradient]]). The **agglomerative** IB — merge the cluster pair losing the least relevant information — is a bottom-up coarse-graining. And **predictive information**, the mutual information between past and future, measures the sub-extensive, learnable structure of a signal.

## Markov aggregation boundary

[[geiger-2013-kl-aggregation]] uses an information-bottleneck objective to search for state
aggregations that control a KL divergence rate, with tightness tied to lumpability in the source
setting. This makes IB a concrete partition-selection baseline for finite Markov dynamics. An
unregularized information objective can admit degenerate selectors. [[Coarse Graining]] therefore
combines the IB score with exact lumpability, retained-interaction residual, and gauge/relabeling
checks.

## Sources

- [[geiger-2013-kl-aggregation]] — information-bottleneck search for KL-rate Markov aggregation
  with scope restricted to the declared finite Markov setting.

- [[tishby-1999-information-bottleneck]] — founding IB variational principle; KL-distortion softmax assignment and the information plane.
- [[bialek2001predictability|bialek-2001-predictability-complexity]] — predictive information as a complexity measure; the $\tfrac{K}{2}\log T$ counting law.
- [[chechik2005information-bottleneck-gaussian|chechik-2005-gaussian-ib]] — closed-form Gaussian IB; spectral, phase-transition optimum.
- [[strouse-2017-deterministic-ib]] — deterministic (hard-clustering) IB limit.
- [[slonim-2000-agglomerative-ib]] — bottom-up agglomerative IB; relevance-preserving coarse-graining.
- [[shwartz-ziv-2017-opening-black-box]] — information-plane dynamics of deep nets; fitting-then-compression.
- [[cover-thomas-2006-elements-information-theory]] — defines entropy, KL/relative entropy, and mutual information, the quantities underpinning the IB Lagrangian's $I(X;T)$ and $I(T;Y)$, the free-energy KL terms, and the attention-entropy term.

## See also

- [[Variational free energy]]
- [[Information geometry and natural gradient]]
- [[Renormalization group flow]]
