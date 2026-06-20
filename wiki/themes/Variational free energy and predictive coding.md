---
type: theme
title: Variational free energy and predictive coding
aliases:
  - Free energy and predictive coding
tags:
  - cluster/vfe
  - project/transformer
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Variational free energy and predictive coding

## The big picture

Variational free energy is the organizing objective of this entire research program. The idea is deceptively simple: when a model cannot compute the true posterior over latent causes of its observations, it instead posits a tractable approximate belief and minimizes a single scalar — the *variational free energy* — that upper-bounds the negative log evidence of the data. Minimizing that bound simultaneously pulls the approximate belief toward the true posterior and improves the model's account of the data. In machine learning the same quantity is read with the opposite sign and called the [[Evidence lower bound (ELBO)]]; in computational neuroscience it is read as an upper bound on *surprise* and called free energy. The [[VFE Transformer Program]] takes this quantity literally as its training loss, maintaining a per-token Gaussian belief `(mu, Sigma)` and descending the free energy of those beliefs rather than a conventional cross-entropy alone.

The reason this theme is foundational rather than decorative is structural. A free-energy objective factors naturally into two coupled optimizations: an inner step that updates beliefs about latents while holding parameters fixed, and an outer step that updates parameters while holding beliefs fixed. This is exactly the E-step / M-step decomposition the architecture implements, and it is what licenses the model's "filtering" gradient mode, in which beliefs are refined online by a small number of inner relaxation steps rather than solved to convergence. The two great lineages feeding this theme — the [[Variational autoencoder (VAE)]] tradition from machine learning and the [[Predictive coding network]] / [[Free-energy principle active inference]] tradition from neuroscience — turn out to be two presentations of the same coordinate ascent, and the VFE transformer is best understood as a deliberate fusion of the two.

A second deep idea threads through everything here: *precision weighting*. Under a Gaussian belief, the free energy is a sum of squared prediction errors, each weighted by a precision (inverse variance). Errors the model is confident about dominate; errors it is uncertain about are discounted. This single mechanism reappears as the architecture's [[Precision weighting|precision-weighted attention]]: attention is not merely a learned similarity but a reliability-weighted routing of prediction errors, with the covariance `Sigma` playing the role of an uncertainty that gates information flow. The theme thus connects directly to the attention cluster, and — because precisions are themselves symmetric-positive-definite objects and the natural updates to them are metric-aware — to the SPD-geometry and information-geometry clusters as well.

## Key threads

**Free energy as one functional, two steps.** The cleanest statement of the E-step / M-step structure is [[neal-1998-variational-em]], which recasts the EM algorithm as coordinate ascent on a *single* negative-free-energy functional whose E-step optimizes the belief distribution `q` and whose M-step optimizes the parameters. Crucially, Neal and Hinton show the E-step need not run to convergence: partial, incremental, and sparse updates still increase the same bound. This is the formal license for the architecture's filtering mode, where beliefs are nudged rather than fully solved each step. See [[Variational EM]] for the method page.

**The neuroscience lineage: predictive coding.** [[rao-1999-predictive-coding]] introduced hierarchical predictive coding of visual cortex, in which feedback connections carry top-down predictions and feedforward connections carry *precision-weighted prediction errors*. [[friston-2010-free-energy-principle]] then elevated this into a unifying claim — the [[Free-energy principle active inference|free-energy principle]] — casting perception, attention, learning, and action as minimization of variational free energy, an upper bound on surprise. [[bogacz-2017-free-energy-tutorial]] supplies the explicit, step-by-step derivation for Gaussian beliefs, yielding the precise precision-weighted E-step belief-relaxation and M-step precision-learning updates that the model's filtering gradient mode mirrors. [[buckley-2017-fep-mathematical-review]] gives the cleanest self-contained derivation of the continuous-state free-energy principle — the Laplace-encoded variational free energy, the gradient-descent E-step on `mu`, and the precision-weighted prediction-error dynamics that the transformer's filtering E-step reproduces — serving as a worked-derivation bridge between the Bishop/Beal ELBO canon and the Friston-style FEP claims. For the discrete (POMDP) presentation, [[smith-2022-active-inference-tutorial]] is the standard operational reference, with explicit variational and expected-free-energy update equations and a worked mean-field factorization over hidden states, policies, and parameters — an equation-level E-step/M-step template to benchmark the program's filtering loop against. Together these ground the architecture's claim that attention *is* prediction-error routing, and that learning the covariance `Sigma` *is* learning precision. The method page is [[Predictive coding network]].

**The machine-learning lineage: amortized variational inference.** [[kingma-2013-auto-encoding-variational-bayes]] introduced the [[Variational autoencoder (VAE)]]: the ELBO trained end-to-end via the [[Reparameterization trick]] and an amortized Gaussian recognition network. This is the blueprint for optimizing per-token diagonal-Gaussian beliefs by gradient descent. But a single forward pass leaves an *amortization gap* — the encoder's one-shot guess is generally worse than the belief that would minimize free energy for that specific input. [[marino-2018-iterative-amortized-inference]] closes this gap with [[Iterative amortized inference]], learning an optimizer that repeatedly encodes free-energy gradients to refine the belief, which is precisely the design pattern behind the VFE transformer's iterated E-step. Where these treat the belief as a single object, [[winn-2005-variational-message-passing]] casts mean-field variational inference on conjugate-exponential models as local message passing on a factor graph — the computational structure the gauge-VFE attention realizes when it routes precision-weighted prediction errors between token-belief factors, and the formalism that pins down which mean-field factorization underwrites a given E-step update.

**The bridge: predictive coding *is* backprop.** The two lineages are unified by [[millidge-2020-pc-approximates-backprop]], which proves that predictive-coding free-energy minimization with purely *local* prediction-error updates converges to exact backpropagation gradients along arbitrary computation graphs. This is the keystone result for the program: it means the biologically motivated E-step/M-step inference loop and standard end-to-end gradient training are not rivals but the same computation viewed at different granularities, so the architecture can claim a principled inference interpretation without sacrificing trainability.

**Cross-cluster reach.** The free-energy theme does not stay in its lane. The M-step is a parameter update on a statistical manifold, so it is naturally a [[Natural gradient]] step preconditioned by the [[Fisher information metric]] ([[amari-1998-natural-gradient]]); the architecture's per-block Fisher preconditioning is the GL(k) analogue. The choice of *which* divergence the free energy is built on is a free parameter: [[li-turner-2016-renyi-vi]] generalizes the ELBO to a one-parameter [[Renyi divergence|Renyi]] family of bounds, and [[vanerven-2014-renyi-kl]] shows the ordinary KL-based free energy is exactly the order-one limit — the basis for the model's `renyi` divergence family. And because the Gaussian belief's covariance `Sigma` lives on the SPD cone, every belief update is implicitly a Riemannian step on that manifold (see [[SPD-manifold geometry and Riemannian optimization]]). These connections are developed in the sibling themes [[Information geometry and natural gradient]] and [[Inference machinery — variational EM and filtering]].

## How it lands in this work

In the [[VFE Transformer Program]] the free-energy theme is not an analogy but the literal mechanism. Each token carries a Gaussian belief `(mu, Sigma)`; the family is `gaussian_diagonal`. The training objective is the variational free energy / ELBO, generalized to a [[Renyi divergence|Renyi]] order so KL is the recovered special case. The E-step performs precision-weighted belief relaxation in the manner of [[bogacz-2017-free-energy-tutorial]] and [[marino-2018-iterative-amortized-inference]], run only partially under the `filtering` gradient mode — licensed by the incremental-EM argument of [[neal-1998-variational-em]] and made consistent with end-to-end gradients by [[millidge-2020-pc-approximates-backprop]]. The M-step updates parameters, and because it is a step on a statistical manifold it is preconditioned in the information-geometric sense rather than taken in raw coordinates.

The most direct architectural payoff is [[Precision weighting|precision-weighted attention]]: where a standard transformer ([[vaswani-2017-attention]]) computes softmax similarities, the VFE transformer routes precision-weighted prediction errors in the Rao–Ballard sense ([[rao-1999-predictive-coding]]), with the belief covariance gating each token's contribution. The kernel reinterpretation of attention ([[tsai-2019-kernel-attention]]) makes this swap natural: precision weighting is simply a particular, uncertainty-aware choice of attention kernel. An attention-entropy term and causal beta/gamma attention priors in the config are recognizable as the surprise/complexity terms of the free-energy decomposition.

> [!note] Editorial: The config's pairing of a free-energy objective with a *gauge* parameterization is the program's distinctive bet — that beliefs should be transported between token frames (parallel transport / holonomy) rather than compared in a fixed coordinate system. No source in this digest treats free energy and gauge structure jointly; that synthesis is original to this work and is elaborated in [[Gauge equivariance and geometric deep learning]].

## Open questions / gaps

- **Renyi free energy under filtering.** [[li-turner-2016-renyi-vi]] derives the Renyi bound for fully optimized beliefs; the model uses it under *partial* (filtering) E-steps. Whether the incremental-EM monotonicity guarantee of [[neal-1998-variational-em]] survives the move from KL to a general Renyi order is not established by any source here.
- **Backprop-equivalence with curved beliefs.** [[millidge-2020-pc-approximates-backprop]] assumes standard (Euclidean) prediction-error dynamics. The VFE transformer's beliefs live on the SPD manifold and are transported across gauge frames; whether the exact-backprop equivalence carries over to manifold-valued, transported beliefs is open.
- **Precision learning vs. attention learning.** Predictive coding learns precisions explicitly ([[bogacz-2017-free-energy-tutorial]]); transformers learn attention weights implicitly. The architecture conflates the two via precision-weighted attention, but the digest contains no source quantifying when learned attention faithfully recovers the optimal precisions.
- **Depth of the inner loop.** [[marino-2018-iterative-amortized-inference]] shows iterative refinement closes the amortization gap but is silent on how many filtering steps are needed before the belief is good enough that the M-step gradient is trustworthy — a practical hyperparameter the program must set empirically.

## Sources synthesized

- [[neal-1998-variational-em]] — EM as coordinate ascent on one negative-free-energy functional; license for incremental/partial (filtering) E-steps.
- [[friston-2010-free-energy-principle]] — Free-energy principle; perception/attention/learning/action as free-energy minimization.
- [[rao-1999-predictive-coding]] — Hierarchical predictive coding; precision-weighted prediction errors as the ancestor of precision-weighted attention.
- [[bogacz-2017-free-energy-tutorial]] — Explicit Gaussian-belief derivation of the precision-weighted E-step and precision-learning M-step.
- [[buckley-2017-fep-mathematical-review]] — Self-contained mathematical review of the continuous-state FEP; Laplace-encoded VFE and gradient-descent E-step bridging ELBO canon and FEP claims.
- [[smith-2022-active-inference-tutorial]] — Step-by-step discrete (POMDP) active-inference tutorial; explicit VFE/EFE updates and mean-field factorization as an E-step/M-step template.
- [[kingma-2013-auto-encoding-variational-bayes]] — VAE; ELBO via reparameterization and amortized Gaussian recognition.
- [[marino-2018-iterative-amortized-inference]] — Iterative amortized inference; learned optimizer closing the amortization gap.
- [[winn-2005-variational-message-passing]] — Mean-field VI on conjugate-exponential models as factor-graph message passing; the message-routing structure behind gauge-VFE attention.
- [[millidge-2020-pc-approximates-backprop]] — Predictive coding with local updates approximates exact backprop; unifies the inference loop with gradient training.
- [[vaswani-2017-attention]] (cross-cluster) — Softmax-attention baseline the precision-weighted variant modifies.
- [[tsai-2019-kernel-attention]] (cross-cluster) — Kernel view of attention; precision weighting as an uncertainty-aware kernel.
- [[li-turner-2016-renyi-vi]] (cross-cluster) — Renyi family of variational bounds generalizing the ELBO.
- [[vanerven-2014-renyi-kl]] (cross-cluster) — KL as the order-one limit of Renyi divergence.
- [[amari-1998-natural-gradient]] (cross-cluster) — Fisher-preconditioned natural gradient grounding the M-step.
- [[friston-2023-fep-simpler]] — Streamlined statement of the free-energy principle and its [[Bayesian mechanics]] reading.
- [[bissiri-holmes-walker-2016-general-bayes]] — General Bayesian updating from a loss-based coherence argument, motivating divergence choices beyond KL.

## See also

- [[Bayesian mechanics]]
- [[Markov blanket interpretation debate]]
- [[Information bottleneck]]

## Related sources (ingested 2026-06-20)

- [[bishop-2006-pattern-recognition-machine-learning]] — Ch.
- [[wainwright-jordan-2008-graphical-models-variational-inference]] — Exponential-family / convex-duality foundation of variational inference;
- [[beal-2003-variational-algorithms-approximate-bayesian-inference]] — Beal's thesis - variational Bayesian EM and the free-energy lower bound for latent-variable models;
