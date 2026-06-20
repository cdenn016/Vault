---
type: concept
title: "MDL and BIC model selection"
aliases:
  - MDL
  - BIC
  - Minimum description length
  - Bayesian Information Criterion
  - Penalized model selection
  - VFE as compression
tags:
  - cluster/methodology
  - project/multi-agent
  - project/transformer
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# MDL and BIC model selection

## Definition

**Penalized model selection** chooses among candidate models by trading goodness-of-fit against a complexity cost, so that an extra parameter is admitted only when it buys enough explanatory power to justify itself. Two classical formalizations realize this Occam tradeoff in complementary ways. The **Bayesian Information Criterion** (BIC) of Schwarz (1978) arises from a Laplace expansion of the Bayes marginal likelihood: to leading asymptotic order, the log marginal of a $k$-parameter model fit to $n$ samples is

$$
\log p(x) \;=\; \log \hat L_k \;-\; \tfrac{1}{2}\,k \log n \;+\; O(1),
$$

so the Bayes-optimal model is the one maximizing $\log \hat L_k - \tfrac12 k \log n$. The penalty $\tfrac12 k\log n$ is an automatic, sample-size-growing Occam term, heavier than AIC's constant-per-parameter cost and consistent for model order. The **Minimum Description Length** principle of Rissanen (1978) reaches the same place through coding theory: the best model is the one giving the shortest total encoding of *both* the parameters and the data given the parameters,

$$
L_{\text{total}} \;=\; \underbrace{L(\theta)}_{\text{describe the model}} \;+\; \underbrace{L(x \mid \theta)}_{\text{describe the data given the model}},
$$

minimized jointly. The data-coding cost is the negative log-likelihood; the parameter-coding cost asymptotically reproduces the same $\tfrac12 k\log n$ term, so MDL and BIC coincide in the large-sample limit. MDL makes "a good model compresses the data" operational.

## Why it matters here

These two criteria do double duty in the participatory program. First, MDL supplies the **compression reading of variational free energy**. The VFE decomposes into accuracy (expected log-likelihood, the bits to encode the data given the belief) minus complexity (the [[Variational free energy|KL]] from belief to prior, the bits to encode the belief relative to the prior), which is exactly Rissanen's two-part code length. Reading $\mathcal F$ as a description length recasts free-energy minimization as an MDL principle, giving the whole objective an information-theoretic, "it-from-bit" footing that the manuscript [[participatory-it-from-bit]] develops. Second, BIC and MDL are the **two retention criteria** for hierarchical growth. When the model coarse-grains a cluster into a parent ([[Meta-agents and hierarchical emergence]]), introducing that meta-agent adds parameters; the candidate is kept only if the gain in fit beats the $\tfrac12 k\log n$ penalty (BIC reading) or, equivalently, only if it shortens the total code length of the agent population (MDL reading). This gives the species-gated condensation rule a principled stopping condition rather than an arbitrary threshold.

## Details

BIC is the asymptotic Bayesian counterpart of MDL: both descend from the same Laplace/saddle-point expansion of the marginal likelihood, the same technique that governs the RG closure test used to license coarse-grainings. MDL is the more general (prequential, coding) statement; BIC is its leading-order Gaussian-prior specialization. The compression view links naturally to the evidence-bound view, since maximizing marginal likelihood is what both the [[Variational free energy|VFE/ELBO]] and BIC approximate. Where the per-scale closure diagnostic answers *which* clusters are coherent enough to merge, these criteria answer *whether the merge is worth its parameter cost*.

The $\tfrac12 k\log n$ penalty is not postulated but *derived*, and the derivation is pure integral asymptotics. Writing the marginal likelihood as a parameter-space integral $p(x) = \int e^{\,n\,\ell(\theta)}\pi(\theta)\,d\theta$ and expanding about its peak (the MLE $\hat\theta$) is exactly **Laplace's method**: the leading exponential factor gives $\hat L_k$, the Gaussian curvature integral over $k$ directions contributes the $-\tfrac12 k\log n$ term, and a Fisher-information determinant survives at $O(1)$. The rigorous version of this step — Laplace's method, steepest descent / saddle point, Watson's lemma, with controlled error bounds — is the subject of [[wong-2001-asymptotic-integrals|Wong (2001)]], and the same asymptotic-methods toolkit (dominant balance, asymptotic series, WKB, matched asymptotics alongside Laplace integrals) is set out in [[bender-orszag-1999-asymptotic-methods|Bender & Orszag (1999)]]. This is the identical apparatus the program uses for the thermodynamic-limit reasoning behind [[Meta-entropy]] and the saddle-point closure of the renormalization-group flow of beliefs, so BIC, MDL, and the meta-entropy limit all rest on one shared piece of asymptotic mathematics.

## Sources

- [[schwarz-1978-bic]] — derives BIC as the leading terms of the Bayes marginal likelihood; the $\tfrac12 k\log n$ Occam penalty and the consistent model-order selection it gives.
- [[rissanen-1978-mdl]] — introduces the Minimum Description Length principle; two-part code length and the compression reading of model quality that the project applies to VFE.
- [[wong-2001-asymptotic-integrals]] — rigorous Laplace's method, steepest descent, and Watson's lemma with error control; the integral-asymptotics backstop for the BIC marginal-likelihood expansion.
- [[bender-orszag-1999-asymptotic-methods]] — classic asymptotic-methods and perturbation-theory text (Laplace/saddle-point integrals, dominant balance, matched asymptotics) underpinning the same Laplace expansion.

## See also

- [[Meta-agents and hierarchical emergence]]
- [[Variational free energy]]
- [[participatory-it-from-bit]]
