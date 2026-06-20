---
type: concept
title: "Information bottleneck"
aliases:
  - IB
  - Information bottleneck method
  - IB Lagrangian
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-19
updated: 2026-06-19
---

# Information bottleneck

## Definition

The **information bottleneck** (IB) formalizes the extraction of the *relevant* part of a signal. Given a source variable $X$ and a relevance variable $Y$, one seeks a compressed representation $T$ that throws away as much of $X$ as possible while keeping as much as possible of what $X$ tells us about $Y$. This is posed as a single trade-off, minimized over stochastic encoders $p(t \mid x)$,

$$
\mathcal{L}_{\mathrm{IB}} \;=\; I(X; T) \;-\; \beta\, I(T; Y),
$$

where $I(X;T)$ is the *complexity* (description length) of the code, $I(T;Y)$ is its *accuracy* (relevance retained), and the Lagrange multiplier $\beta$ sets the exchange rate between the two. The stationarity condition gives a self-consistent fixed point in which the optimal assignment is a **softmax over a KL distortion**, $p(t \mid x) \propto p(t)\,\exp\!\big(-\beta\,\mathrm{KL}(p(y\mid x)\,\|\,p(y\mid t))\big)$, solvable by Blahut-Arimoto-style alternating projection. Sweeping $\beta$ traces the **information plane**, the optimal complexity-versus-accuracy curve $\big(I(X;T), I(T;Y)\big)$.

## Why it matters here

The IB Lagrangian is the participatory free energy of [[participatory-it-from-bit]] in another guise. PIFB's [[Variational free energy]] sets a compression pressure — the self-coupling $\alpha\,\mathrm{KL}(q_i \| p_i)$ that penalizes a belief's deviation from its prior, a cost on representational complexity — against an accuracy pressure, the observation-likelihood term $-\mathbb{E}_q[\log p(o\mid x)]$. That is structurally $I(X;T)$ against $I(T;Y)$, with PIFB's $\alpha$ playing Tishby's $\beta$. The match runs deeper than the objective: the IB's defining feature, a softmax over a KL distortion, is precisely the form of PIFB's attention weight $\beta_{ij} = \mathrm{softmax}(-\mathrm{KL}(q_i \| \Omega_{ij} q_j)/\tau)$, so the IB supplies the variational pedigree for both the capacity floor and the KL-distortion-softmax structure of belief coupling. The PIFB **capacity floor** — an irreducible loss set by how far beliefs can compress while staying predictive — is the IB bound read in belief coordinates, and a layer-by-layer descent of $F$ is a candidate mechanism for an IB-like fitting-then-compression trajectory through the information plane.

## Details

The original IB is a *soft* assignment; its **deterministic** limit replaces $I(X;T)$ with the code entropy $H(T)$, collapsing the optimum to a hard clustering — the variational account of PIFB's low-temperature ($\tau = \kappa\sqrt{K}$) attention and crisp meta-agent membership. The **Gaussian IB** solves the trade-off in closed form when $X, Y$ are jointly Gaussian: the optimum is a noisy linear projection along eigenvectors of $\Sigma_{x\mid y}\Sigma_x^{-1}$, switching on one at a time as $\beta$ grows. This is the case nearest PIFB, whose representations are Gaussian belief tuples $(\mu, \Sigma, \phi)$, tying the trade-off to a covariance-eigenstructure problem on the SPD manifold (see [[Information geometry and natural gradient]]). The **agglomerative** IB — merge the cluster pair losing the least relevant information — is the coarse-graining cousin of [[Meta-agents and hierarchical emergence]] formation. And **predictive information**, the mutual information between past and future, supplies the currency for PIFB's $h \to s \to p \to q$ hierarchy: each level captures the sub-extensive, learnable structure that predicts the level below.

## Sources

- [[tishby-1999-information-bottleneck]] — founding IB variational principle; KL-distortion softmax assignment and the information plane.
- [[bialek-2001-predictability-complexity]] — predictive information as a complexity measure; the $\tfrac{K}{2}\log T$ counting law, currency for the $h \to s \to p \to q$ hierarchy.
- [[chechik-2005-gaussian-ib]] — closed-form Gaussian IB; spectral, phase-transition optimum matching PIFB's Gaussian belief tuples.
- [[strouse-2017-deterministic-ib]] — deterministic (hard-clustering) IB limit; account of low-temperature attention and crisp meta-agent membership.
- [[slonim-2000-agglomerative-ib]] — bottom-up agglomerative IB; relevance-preserving coarse-graining cousin of meta-agent formation.
- [[shwartz-ziv-2017-opening-black-box]] — information-plane dynamics of deep nets; fitting-then-compression reading of layerwise $F$ descent.
- [[cover-thomas-2006-elements-information-theory]] — defines entropy, KL/relative entropy, and mutual information, the quantities underpinning the IB Lagrangian's $I(X;T)$ and $I(T;Y)$, the free-energy KL terms, and the attention-entropy term.

## See also

- [[Variational free energy]]
- [[Meta-agents and hierarchical emergence]]
- [[Information geometry and natural gradient]]
- [[Renormalization-group flow of beliefs]]
- [[Multi-agent variational free energy]]
- [[participatory-it-from-bit]]
