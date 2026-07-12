---
type: method
title: Predictive coding network
aliases:
  - PC network
  - PCN
  - Hierarchical predictive coding
  - Rao-Ballard model
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-07-09
---

# Predictive coding network

## What it is

A **predictive coding network (PCN)** is a hierarchical generative model in which each layer attempts to *predict* the activity of the layer below, and only the residual — the **prediction error** — is propagated upward. The canonical formulation is the cortical model of [[rao-1999-predictive-coding]], in which feedback connections carry top-down predictions and feedforward connections carry **precision-weighted** prediction errors; it was introduced to explain extra-classical receptive-field effects in visual cortex. Predictive coding is the neural-implementation arm of the broader [[Free-energy principle active inference|free-energy principle]] of [[friston-2010-free-energy-principle]]: a PCN is, mathematically, a scheme for minimizing [[Variational free energy|variational free energy]] under Gaussian assumptions. See also the theme page [[Variational free energy and predictive coding]].

## How it works

A PCN posits a layered generative model in which each level's latent state $\mu^{(l)}$ generates a prediction $g(\mu^{(l)})$ of the level below. The discrepancy
$$\varepsilon^{(l)} = \mu^{(l-1)} - g(\mu^{(l)})$$
is the **prediction error**, and the network weights these errors by their inverse variance — their **precision** — so that confident channels dominate inference. Under a Gaussian (Laplace) approximation, the objective being minimized is exactly the variational free energy: a sum, across levels, of precision-weighted squared prediction errors plus log-precision (complexity) terms. The step-by-step derivation of these dynamics for Gaussian beliefs — including the precision-weighted error relaxation and the precision-learning updates — is laid out in [[bogacz-2017-free-energy-tutorial]].

Inference and learning split into two interleaved phases, mirroring [[Variational EM|variational EM]] as recast by [[neal-1998-variational-em]]:

- An **inference (E-step) phase** in which latent states $\mu$ relax along the free-energy gradient until prediction errors are minimized, holding weights fixed. This is local gradient descent on free energy driven by the error signals $\varepsilon$.
- A **learning (M-step) phase** in which the generative weights are updated, again by a local rule proportional to the product of presynaptic activity and postsynaptic prediction error.

Both updates are *local*: each unit needs only the activity of its neighbors and the error units it connects to, never a global backward pass. A central theoretical result, [[millidge-2020-pc-approximates-backprop]], shows that this purely local free-energy minimization converges to the *exact* backpropagation gradients on arbitrary computation graphs, which unifies the biologically motivated E-step/M-step loop with standard end-to-end gradient training. Conceptually, predictive coding is the dynamical, error-correcting counterpart of the amortized recognition models used in the [[Variational autoencoder (VAE)|variational autoencoder]] of [[kingma-2013-auto-encoding-variational-bayes]]; where a VAE infers latents in a single feedforward pass, a PCN iterates error-relaxation dynamics, closer in spirit to [[Iterative amortized inference|iterative amortized inference]] ([[marino-2018-iterative-amortized-inference]]).

## Strengths / limitations

**Strengths.** Predictive coding gives a biologically plausible, fully local implementation of approximate Bayesian inference: there is no separate backward pass, no weight transport, and the same error-correcting circuitry serves both inference and learning. It makes [[Precision weighting|precision]] a first-class quantity, so attention and uncertainty fall out of the same machinery rather than being bolted on. Because it minimizes variational free energy, it inherits the principled [[Evidence lower bound (ELBO)|ELBO]] semantics of variational inference, and — via [[millidge-2020-pc-approximates-backprop]] — it can in principle reproduce backprop's optimization power.

**Limitations.** The inference phase is *iterative*: each forward inference requires relaxing the latent states to (approximate) equilibrium, which is slower than a single feedforward pass and can be sensitive to step size and convergence criteria. The standard formulation assumes Gaussian beliefs with simple (often diagonal) precisions, limiting the posteriors it can represent. Learning the precisions stably is delicate, and the exact-backprop equivalence holds only under specific scheduling assumptions. As a generative model it says nothing, on its own, about how latent states should be *transported* or *coupled* across structured representations — gaps the VFE transformer fills with geometric machinery drawn from elsewhere.

## Relation to this work

The predictive coding network is a conceptual ancestor of the VFE transformer's belief-update core. The retained route maintains per-token diagonal-Gaussian model and belief states, applies one target-blind $s$ refinement, sets $q_i^{(0)}=p_i=s_i^{(1)}$, and then applies one target-blind $q$ refinement. This is not a converged predictive-coding E-step or an argmin on the decode objective. Its precision-weighted attention adapts the Rao–Ballard precision-gating idea ([[rao-1999-predictive-coding]]) to transported Gaussian-KL coupling. The exact-backprop result of [[millidge-2020-pc-approximates-backprop]] depends on its own scheduling and convergence assumptions and does not license the deployed finite, multi-objective loop as exact backpropagation. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial (2026-07-09): The live covariance family is diagonal SPD, with belief-side
> Fisher/AIRM updates. Beliefs are transported across a GL(k) frame structure, and their pairwise
> discrepancy may use order-Rényi divergence. That discrepancy is distinct from the Li–Turner
> variational Rényi bound and Amari alpha-divergence geometry. The committed optimizer route at each
> recorded SHA uses AdamW for the frame table, but dirty provenance prevents exact reconstruction of
> the executed optimizer; the separate decode cross-entropy prevents a single predictive-coding ELBO interpretation.
> [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[rao-1999-predictive-coding]] — hierarchical predictive coding in visual cortex; the precision-weighted prediction-error mechanism.
- [[friston-2010-free-energy-principle]] — predictive coding as variational free-energy minimization.
- [[bogacz-2017-free-energy-tutorial]] — explicit Gaussian-belief free-energy derivation, E-step/M-step updates.
- [[neal-1998-variational-em]] — EM as coordinate ascent on one negative-free-energy functional; incremental guarantees require that shared-functional setting.
- [[millidge-2020-pc-approximates-backprop]] — local predictive-coding updates approximate exact backprop.
- [[kingma-2013-auto-encoding-variational-bayes]] — amortized Gaussian variational inference (contrast: single-pass vs. iterative).
- [[marino-2018-iterative-amortized-inference]] — iterative refinement of beliefs from free-energy gradients.

## See also

- [[Variational free energy and predictive coding]]
- [[Variational free energy]]
- [[Free-energy principle active inference]]
- [[Variational EM]]
- [[Variational autoencoder (VAE)]]
- [[Iterative amortized inference]]
- [[Prediction error]]
- [[Precision weighting]]
- [[Evidence lower bound (ELBO)]]
- [[VFE Transformer Program]]
