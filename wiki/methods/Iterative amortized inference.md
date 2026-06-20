---
type: method
title: Iterative amortized inference
aliases:
  - Iterative inference models
  - Learned-optimizer inference
  - IAI
tags:
  - cluster/vfe
  - project/transformer
status: draft
created: 2026-06-18
updated: 2026-06-18
---

# Iterative amortized inference

## What it is

Iterative amortized inference is an inference scheme, introduced by Marino, Yue, and Mandt in [[marino-2018-iterative-amortized-inference]], that learns an *optimizer* rather than a single forward map. Instead of predicting variational parameters in one shot from the data, it trains a neural network that repeatedly refines those parameters by consuming the gradients of the variational objective. It sits squarely in the variational-inference lineage: it inherits the [[Evidence lower bound (ELBO)]] objective and the [[Amortized inference]] idea from the [[Variational autoencoder (VAE)]] of [[kingma-2013-auto-encoding-variational-bayes]], while reintroducing the per-datapoint optimization that classical [[Variational EM]] performs in its E-step ([[neal-1998-variational-em]]).

## How it works

In standard amortized inference, a recognition (encoder) network $f_\phi$ maps an observation $x$ directly to the parameters $\lambda = (\mu, \Sigma)$ of an approximate posterior $q_\lambda(z\mid x)$, and the whole system is trained by maximizing the [[Evidence lower bound (ELBO)]] — equivalently minimizing [[Variational free energy]] — via the [[Reparameterization trick]] ([[kingma-2013-auto-encoding-variational-bayes]]). This single pass is fast but suboptimal: the encoder cannot in general output the exact stationary point of the ELBO for every datapoint, leaving a residual gap between the amortized posterior and the best posterior achievable in the chosen variational family.

Iterative amortized inference closes that gap by amortizing the *optimization process* itself ([[marino-2018-iterative-amortized-inference]]). It maintains current variational parameters $\lambda_t$ and updates them through a learned iterative rule of the form

$$\lambda_{t+1} = \lambda_t + f_\phi\big(\lambda_t,\ \nabla_\lambda \mathcal{L}(\lambda_t)\big),$$

where $\mathcal{L}$ is the ELBO/free-energy objective and $\nabla_\lambda \mathcal{L}$ is its gradient with respect to the variational parameters. The network $f_\phi$ plays the role of a learned, data-conditioned optimizer: it reads the local free-energy gradient — which under a Gaussian generative model is built from precision-weighted [[Prediction error]] terms ([[bogacz-2017-free-energy-tutorial]]) — and emits a refined belief. Running it for several steps drives $q$ toward the ELBO optimum more closely than a single encoder pass, recovering much of the accuracy of full per-datapoint optimization at a fraction of its cost. The encoder parameters $\phi$ and the generative (decoder) parameters $\theta$ are still trained end-to-end against the same objective, so the method interpolates between pure amortization (one step) and explicit iterative optimization (many steps).

Conceptually this is the same two-timescale structure as [[Variational EM]]: an inner loop that optimizes the belief $q$ for fixed parameters (the E-step) wrapped inside an outer loop that optimizes the parameters (the M-step), all on a single negative-free-energy functional ([[neal-1998-variational-em]]). The novelty is that the inner E-step is no longer hand-derived coordinate ascent but a *learned* gradient-based update. This connects directly to predictive-coding accounts of inference, where belief updating is itself a gradient descent on free energy driven by prediction-error signals ([[rao-1999-predictive-coding]], [[friston-2010-free-energy-principle]]); iterative amortized inference can be read as a learned, accelerated predictive-coding loop. Because predictive-coding free-energy minimization with local error updates provably tracks backprop gradients along arbitrary computation graphs ([[millidge-2020-pc-approximates-backprop]]), the learned-optimizer view and the gradient-training view coincide.

## Strengths / limitations

The central strength is that iterative refinement shrinks the *amortization gap* — the systematic suboptimality a single-pass encoder leaves on the table — without sacrificing the speed advantage of amortization, since the learned optimizer typically converges in a handful of steps and generalizes the update rule across datapoints ([[marino-2018-iterative-amortized-inference]]). It also yields a graceful accuracy/compute trade-off: more iterations buy tighter posteriors. Feeding the objective's gradient as input gives the encoder a stable, problem-aware signal, which tends to improve conditioning relative to learning an update from raw observations alone.

The limitations are equally clear. Each inference step requires a fresh evaluation of $\nabla_\lambda \mathcal{L}$, so a $T$-step procedure costs roughly $T$ times a single forward/backward pass at inference time. Unrolling the iterative updates for training can be memory-intensive and prone to the usual pathologies of learned optimizers (vanishing or exploding meta-gradients, sensitivity to the number of unrolled steps). And the method inherits the expressiveness ceiling of the chosen variational family: refining a diagonal-Gaussian belief more precisely cannot capture posterior structure the family cannot represent.

## Relation to this work

The VFE transformer treats each token as carrying a Gaussian belief $(\mu, \Sigma)$ and alternates an E-step that updates those beliefs with an M-step that updates parameters, under an ELBO/free-energy objective with `gradient_mode` set to *filtering*. Iterative amortized inference is the most direct conceptual template for that E-step: each transformer block can be viewed as one iteration of a learned optimizer that reads precision-weighted prediction errors and refines the per-token belief, rather than a single VAE-style encoder pass.

What the program **borrows**: the core move of amortizing not a posterior but an *update rule*, and the use of free-energy gradients as the driving signal for belief refinement ([[marino-2018-iterative-amortized-inference]]), layered on top of the VAE's amortized Gaussian recognition and reparameterization machinery ([[kingma-2013-auto-encoding-variational-bayes]]). The two-timescale E-step/M-step decomposition is taken from incremental [[Variational EM]] ([[neal-1998-variational-em]]), and the explicit precision-weighted form of the belief update comes from the Gaussian free-energy derivations of [[bogacz-2017-free-energy-tutorial]] and the predictive-coding tradition ([[rao-1999-predictive-coding]], [[friston-2010-free-energy-principle]]).

How it **differs / improves**: the VFE transformer enriches the flat Euclidean update of the original method with geometry the latter does not consider. The belief covariance lives on the SPD manifold and is refined through an `spd_affine` retraction under the affine-invariant metric, so the iterative update is a Riemannian step rather than a plain gradient step. The parameter side replaces a vanilla M-step with a [[Natural gradient]] / Fisher-preconditioned update, in the spirit of treating learned-optimizer refinement as steepest descent on a statistical manifold rather than in raw coordinates. The training objective generalizes from the strict KL-based ELBO to a [[Renyi divergence]] family (`divergence_family = "renyi"`, with KL as the order-$\to 1$ limit), so the iterated objective $\mathcal{L}$ being refined is itself a tunable variational bound. Finally, the GL($k$) gauge structure means the iterative belief update must be transported across token frames consistently — a constraint absent from the original Euclidean formulation but compatible with its learned-optimizer skeleton.

> [!note] Editorial: The mapping "one transformer block = one iterative-inference step" is an interpretive bridge offered by this program; the original paper frames the method for VAE-style latent-variable models, not sequence transformers.

## Sources

- [[marino-2018-iterative-amortized-inference]] — the method's defining paper: learning an optimizer that iteratively refines beliefs to close the amortization gap.
- [[kingma-2013-auto-encoding-variational-bayes]] — single-pass amortized inference and the reparameterization trick that the iterative scheme generalizes.
- [[neal-1998-variational-em]] — the E-step/M-step free-energy decomposition underlying the inner/outer loop structure.
- [[bogacz-2017-free-energy-tutorial]] — explicit precision-weighted Gaussian belief updates that instantiate the free-energy gradient.
- [[rao-1999-predictive-coding]], [[friston-2010-free-energy-principle]] — predictive-coding and free-energy-principle accounts of inference as iterative error-driven belief updating.
- [[millidge-2020-pc-approximates-backprop]] — equivalence of local free-energy minimization and backprop, unifying the learned-optimizer and end-to-end-gradient views.

## See also

- [[Amortized inference]]
- [[Variational free energy]]
- [[Evidence lower bound (ELBO)]]
- [[Prediction error]]
- [[Precision weighting]]
- [[Reparameterization trick]]
- [[Variational EM]]
- [[Variational autoencoder (VAE)]]
- [[Predictive coding network]]
- [[Free-energy principle active inference]]
- [[Natural gradient]]
- [[Renyi divergence]]
