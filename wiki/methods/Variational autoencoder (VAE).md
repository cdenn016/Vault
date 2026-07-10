---
type: method
title: "Variational autoencoder (VAE)"
aliases:
  - VAE
  - Auto-encoding variational Bayes
  - Variational auto-encoder
  - "Variational Autoencoder"
tags:
  - cluster/vfe
  - project/transformer
status: stable
created: 2026-06-18
updated: 2026-07-09
---

# Variational autoencoder (VAE)

## What it is

A variational autoencoder is a deep generative model that learns a latent-variable distribution by maximizing a tractable lower bound on the data log-likelihood, with the inference distribution produced by a neural network rather than optimized per data point. It was introduced by Kingma and Welling in [[kingma-2013-auto-encoding-variational-bayes]] ("Auto-Encoding Variational Bayes"), which paired a learned amortized recognition network with the [[Reparameterization trick]] to enable end-to-end gradient training of both the generative and inference models.

## How it works

The VAE posits a generative model `p(x, z) = p(z) p_theta(x | z)` with latent variable `z` (typically a standard Gaussian prior) and a decoder `p_theta(x | z)` parameterized by a neural network. Exact posterior inference over `z` is intractable, so the VAE introduces an approximate posterior `q_phi(z | x)` — the **recognition** or **encoder** network — that maps each input directly to the parameters (mean and diagonal covariance) of a Gaussian belief over the latent. Because a single network produces the belief for any input, inference is **amortized**: the cost of optimizing a per-datapoint posterior is replaced by one forward pass through a shared encoder (see [[Amortized inference]]).

Training maximizes the **evidence lower bound** ([[Evidence lower bound (ELBO)]]),

```
log p_theta(x) >= E_{q_phi(z|x)}[ log p_theta(x | z) ] - KL( q_phi(z | x) || p(z) ),
```

a reconstruction term minus a divergence that pulls the approximate posterior toward the prior. The ELBO is exactly the negative [[Variational free energy]], so a VAE is a free-energy-minimizing model in the sense of [[neal-1998-variational-em]] and [[friston-2010-free-energy-principle]]: the encoder performs the E-step (optimize the belief `q`), and the decoder/generative parameters absorb the M-step (optimize `theta`).

The decisive technical move is the [[Reparameterization trick]]: rather than sampling `z ~ q_phi(z|x)` directly (which blocks gradients), one writes `z = mu_phi(x) + sigma_phi(x) * epsilon` with `epsilon ~ N(0, I)`. This makes the sampling step differentiable with respect to the encoder parameters, so a low-variance Monte Carlo estimate of the ELBO can be optimized by ordinary stochastic backpropagation. For diagonal-Gaussian families both the reconstruction expectation and the KL term have stable, low-variance estimators, with the KL available in closed form.

## Strengths / limitations

**Strengths.** The VAE delivers fast, single-pass approximate inference, principled likelihood-based training via a single coherent objective (the ELBO), and a smooth latent geometry useful for interpolation and representation learning. The reparameterization estimator is unbiased and low-variance for Gaussian families, and the framework scales to large datasets through minibatch stochastic gradients.

**Limitations.** A single feedforward encoder leaves an **amortization gap**: the amortized `q_phi(z|x)` is generally worse than the optimum a per-datapoint optimizer would find, capping inference quality. [[marino-2018-iterative-amortized-inference]] addresses exactly this by learning an iterative optimizer that repeatedly refines the belief from free-energy gradients rather than emitting it in one shot. The mean-field diagonal-Gaussian posterior also limits expressiveness, and the standard ELBO (an `alpha -> 1` KL objective) can yield blurry reconstructions and posterior collapse; richer divergence families such as the Renyi bound of [[li-turner-2016-renyi-vi]] trade off mode-covering versus mode-seeking behavior.

## Relation to this work

The VAE is a reference point for the VFE transformer's per-token diagonal-Gaussian beliefs, not a direct blueprint for its complete training loop. The model has no neural recognition network and does not train one shared VAE ELBO: its target-blind belief objective and decode cross-entropy are distinct. Reparameterized Gaussian differentiation, where used, is the narrower Kingma–Welling connection. [[gl-k-attention-2026-07-09-review-revision]]

The VFE transformer **differs** from the vanilla VAE on several axes that the registry's other sources supply:

- **Iterative rather than single-pass inference.** The `filtering` mode applies a one-step belief refinement. This resembles [[Iterative amortized inference]] but does not establish a VAE amortization-gap result or exact-backprop equivalence for the deployed schedule.
- **Rényi rather than pure KL.** The belief-side `divergence_family "renyi"` provides a one-parameter [[Renyi divergence]] family with KL as its order-one limit; it does not generalize the separate decode objective into one VAE bound.
- **Curved belief geometry.** The VAE treats the Gaussian covariance as an unconstrained diagonal vector; the VFE transformer treats `Sigma` as a point on the SPD manifold and updates it with an `spd_affine` retraction under the affine-invariant metric ([[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]]), a structure the original VAE does not impose.
- **Scoped geometry.** Fisher/AIRM geometry supports the Gaussian belief update. The audited frame table uses plain AdamW, and no Fisher/Killing natural-gradient parameter M-step is established; the configured geometric frame fields are inactive.

In short, the VAE supplies Gaussian-latent and differentiable-sampling background. The transformer's filtering, transported-belief geometry, and two-objective schedule are separate constructions rather than improvements to one inherited VAE ELBO. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial: The registry does not contain a dedicated [[Prediction error]] or [[Precision weighting]] derivation specific to the VAE; the link from VAE reconstruction error to precision-weighted prediction error is made through the predictive-coding sources rather than [[kingma-2013-auto-encoding-variational-bayes]] itself.

## Sources

- [[kingma-2013-auto-encoding-variational-bayes]] — the originating VAE / Auto-Encoding Variational Bayes paper: ELBO, amortized recognition network, reparameterization trick.
- [[neal-1998-variational-em]] — EM as coordinate ascent on the negative free energy / ELBO, the E-step/M-step view the VAE instantiates.
- [[friston-2010-free-energy-principle]] — variational free energy as the unifying objective; ELBO = negative free energy.
- [[bogacz-2017-free-energy-tutorial]] — explicit Gaussian-belief free-energy updates underlying the filtering E-step.
- [[marino-2018-iterative-amortized-inference]] — the amortization gap and its iterative remedy.
- [[millidge-2020-pc-approximates-backprop]] — local free-energy minimization recovers backprop.
- [[li-turner-2016-renyi-vi]] / [[vanerven-2014-renyi-kl]] — Renyi generalization of the ELBO and KL as its `alpha -> 1` limit.

## See also

- [[Evidence lower bound (ELBO)]]
- [[Variational free energy]]
- [[Reparameterization trick]]
- [[Amortized inference]]
- [[Variational EM]]
- [[Iterative amortized inference]]
- [[Predictive coding network]]
- [[Free-energy principle active inference]]
- [[Renyi divergence]]
- [[Natural gradient]]
