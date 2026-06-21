---
type: concept
title: "Predictive Coding"
aliases:
  - "Predictive coding"
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-06-21
---

# Predictive Coding

**Predictive coding** is the theory that the brain — and, more generally, any inference engine — is a *hierarchical generative model* that perceives by predicting its own inputs. Each level of the hierarchy sends **top-down predictions** of the activity at the level below; the level below returns only the residual it could not predict, the **bottom-up prediction error**. Inference is the process of suppressing that error by updating beliefs until predictions match incoming evidence. Reviewed comprehensively in [[millidge-2021-predictive-coding-review]] and given its influential cognitive-science framing in [[clark-2013-predictive-brains]], predictive coding casts **perception as approximate Bayesian inference** that minimizes [[Variational free energy]].

## Core formalism

Let level $l$ carry a latent belief $\mu^{(l)}$ that generates a prediction $g(\mu^{(l)})$ of the level below. The prediction error is

$$\varepsilon^{(l)} = \mu^{(l-1)} - g(\mu^{(l)}),$$

and — crucially — errors are not propagated raw but **precision-weighted**. The precision $\Pi = \Sigma^{-1}$ is the *inverse variance* of a channel; high-precision (low-uncertainty) errors dominate, low-precision ones are discounted. Under a Gaussian (Laplace) approximation the quantity being minimized across the hierarchy is exactly the variational free energy,

$$F = \tfrac{1}{2}\sum_l \big( \varepsilon^{(l)\top}\,\Pi^{(l)}\,\varepsilon^{(l)} - \log\lvert\Pi^{(l)}\rvert \big),$$

a sum of precision-weighted squared errors plus complexity (log-precision) terms. Belief states $\mu$ descend the free-energy gradient until errors are quenched. Treating the time-derivatives of $\mu$ as additional coordinates yields the [[Generalised coordinates of motion]] used to track dynamic, not just static, causes.

## Distinctions

Keep three things separate. (1) **The theory** — this page: prediction-error minimization in a hierarchical generative model with precision-weighting. (2) **The algorithm** — the concrete Rao–Ballard message-passing network with its E-step error relaxation and local M-step weight learning, written up on [[Predictive coding network]] and detailed in [[bogacz-2017-free-energy-tutorial]]; that page also covers how local updates approximate backprop. (3) **The broader principle** — the [[Free-energy principle active inference|free-energy principle]], which extends prediction-error minimization to *action* (acting to fulfil predictions), and the [[Bayesian brain hypothesis]] it instantiates. The "controlled hallucination" reading of perception lives at [[Predictive processing and controlled hallucination]].

## Relevance to this program

Predictive coding is the conceptual engine of the **vfe3 transformer**: each token carries a Gaussian belief $(\mu,\Sigma)$ trained by free-energy minimization, and **precision gates attention** — confident tokens exert more influence, the Rao–Ballard "precision weights prediction error" mechanism reread as an attention prior (see [[Precision weighting]]). Because precision is inverse variance, it ties directly to the [[Fisher information metric]] and motivates [[Natural gradient]] updates over belief parameters. In the **MAgent** model, hierarchical prediction-error suppression scales to nested agents minimizing each other's surprise. The transformer keeps this *prediction-error-and-precision* core while replacing the flat-Gaussian substrate with SPD-manifold and gauge machinery — see [[Predictive coding network]] for that departure.

## See also

- [[Predictive coding network]] — the algorithmic method page
- [[Variational free energy]]
- [[Free-energy principle active inference]]
- [[Predictive processing and controlled hallucination]]
- [[Precision weighting]]
- [[Generalised coordinates of motion]]
- [[Bayesian brain hypothesis]]
- [[Prediction error]]
