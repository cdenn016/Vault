---
type: theme
title: "Inference machinery — variational EM and filtering"
aliases:
  - "Variational EM and filtering"
  - "Inference machinery"
  - "E-step / M-step inference loop"
  - "Filtering inference"
tags:
  - cluster/vfe
  - cluster/methodology
  - project/transformer
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Inference machinery — variational EM and filtering

## The big picture

The [[VFE Transformer Program]] treats every token not as a fixed vector but as a
*belief*: a per-token diagonal Gaussian with mean `mu` and covariance `Sigma`. The
machinery that updates those beliefs, and the parameters that shape them, is the
subject of this page. It is the engine room of the architecture — the loop that, on
each forward pass, decides what the model currently believes and how confident it is,
and on each backward pass, decides how to revise the generative model that produced
those beliefs. The conceptual spine is the [[Variational EM]] algorithm: a single
objective, optimized by alternating between an inference step over latent beliefs and a
learning step over parameters.

The unifying observation, due to [[neal-1998-variational-em]], is that the
Expectation-Maximization algorithm is not two unrelated operations but coordinate
ascent on *one* functional — the negative [[Variational free energy]], equivalently the
[[Evidence lower bound (ELBO)]]. The E-step holds parameters fixed and optimizes the
variational belief distribution `q`; the M-step holds `q` fixed and optimizes the
parameters. Crucially, Neal and Hinton show this functional view licenses *incremental*
and *partial* updates: you need not run either step to convergence before switching.
That permission is exactly what the architecture's `gradient_mode = "filtering"`
exploits — beliefs are nudged a few steps toward their optimum rather than relaxed
fully, and parameters are updated on the resulting partially-relaxed beliefs, so
inference and learning interleave online like a filter rather than a batch EM sweep.

Where Neal and Hinton supply the algorithmic justification, [[friston-2010-free-energy-principle]]
supplies the semantics. Friston's free-energy principle casts perception, attention,
and learning as a single imperative: minimize variational free energy, an upper bound on
surprise (negative log model evidence). In this reading the E-step is *perception*
(inferring hidden causes of the input), the M-step is *learning* (improving the
generative model), and the precision terms that weight prediction errors are *attention*.
This is not loose analogy for the VFE transformer; it is the literal training objective
and the literal source of [[Precision weighting]] in its attention.

The remaining ingredient — what makes the beliefs Gaussian and the updates concrete — comes
from the predictive-coding lineage. [[rao-1999-predictive-coding]], [[bogacz-2017-free-energy-tutorial]],
and [[millidge-2020-pc-approximates-backprop]] turn the abstract free-energy functional
into explicit, local, precision-weighted [[Prediction error]] dynamics on Gaussian
variables, and prove that those local dynamics recover the gradients of exact
backpropagation. That equivalence is what lets the architecture run an EM-style belief
loop and still claim it is training the same model end-to-end gradient descent would.

## Key threads

**EM as free-energy coordinate ascent.** The foundational thread is
[[neal-1998-variational-em]]'s reframing of EM. By exhibiting EM as ascent on the negative
free energy `F(q, theta)`, it makes the E-step an explicit optimization over the belief
`q` rather than a fixed posterior computation, which is precisely what is needed when the
exact posterior is intractable and `q` must be an approximating diagonal Gaussian. The
incremental and sparse variants Neal and Hinton justify are the formal ancestors of
"filtering": optimize `q` for a subset, or for a few steps, then update parameters. This
thread connects directly to [[Variational free energy]] and [[Evidence lower bound (ELBO)]]
as the shared objective.

**The free-energy principle and precision-weighted perception.**
[[friston-2010-free-energy-principle]] elevates the same functional to a theory of
neural computation, and [[rao-1999-predictive-coding]] gives its mechanistic prototype:
hierarchical predictive coding, where feedback connections carry top-down predictions and
feedforward connections carry *precision-weighted prediction errors*. The precision (inverse
variance) gates how strongly each error influences belief updates — high precision means
"trust this error, attend to it." This is the conceptual seed of the architecture's
precision-weighted attention (see the theme [[Variational free energy and predictive coding]]
and the method [[Predictive coding network]]). [[bogacz-2017-free-energy-tutorial]] makes the
mapping operational, deriving for Gaussian beliefs the explicit E-step belief-relaxation
update (gradient descent on free energy in `mu`) and the M-step precision-learning update
(updating `Sigma` and weights). The architecture's filtering loop mirrors these two updates
nearly line for line.

**Predictive coding equals backprop.** A pivotal modern result,
[[millidge-2020-pc-approximates-backprop]], proves that free-energy minimization with purely
local prediction-error messages converges to exact backpropagation gradients along arbitrary
computation graphs. For this program the implication is decisive: the E-step/M-step inference
loop is not an *alternative* to gradient training but a *realization* of it. The model can be
described as variational EM and trained as a differentiable network without contradiction,
which is what makes the belief loop and the parameter optimizer coherent halves of one system.

**Amortization and iterative refinement.** A single forward pass that emits beliefs is an
*amortized* inference network: it learns a function from input to `q` rather than optimizing
`q` from scratch per input. [[kingma-2013-auto-encoding-variational-bayes]] is the blueprint —
the variational autoencoder trains the ELBO end-to-end using an amortized Gaussian recognition
network and the [[Reparameterization trick]] to backpropagate through sampling. But a single
amortized pass leaves an *amortization gap*: the learned encoder rarely hits the true per-input
optimum. [[marino-2018-iterative-amortized-inference]] closes that gap by learning an *optimizer*
that repeatedly refines beliefs by encoding free-energy gradients. This is the precise template
for "filtering" as a finite number of belief-refinement iterations per token, sitting between a
one-shot VAE encoder ([[Amortized inference]], [[Variational autoencoder (VAE)]]) and full
per-token relaxation ([[Iterative amortized inference]]).

## How it lands in this work

In the decoded config these threads compose into a concrete loop. Each token carries a Gaussian
belief `(mu, Sigma)` with `family = gaussian_diagonal`. The **E-step** is the filtering update:
starting from the amortized prediction (the [[kingma-2013-auto-encoding-variational-bayes]]
recognition pass), beliefs are refined by a small number of precision-weighted prediction-error
steps in the style of [[bogacz-2017-free-energy-tutorial]] and
[[marino-2018-iterative-amortized-inference]], rather than relaxed to convergence — the partial
update [[neal-1998-variational-em]] permits. The **M-step** updates the generative parameters on
those partially-relaxed beliefs. The objective minimized throughout is variational free energy
(the [[friston-2010-free-energy-principle]] / [[Evidence lower bound (ELBO)]] functional),
and [[millidge-2020-pc-approximates-backprop]] is what guarantees the loop's local updates and
the end-to-end optimizer agree.

The inference machinery does not stand alone; it borrows its *metrics* from the geometry clusters.
The M-step here is not vanilla gradient descent but a [[Natural gradient]] step: the free-energy
gradient is preconditioned by the inverse [[Fisher information metric]], following
[[amari-1998-natural-gradient]], so that parameter updates are invariant to reparameterization of
the beliefs (the cross-cluster theme [[Information geometry and natural gradient]]). Because `Sigma`
is symmetric-positive-definite, the belief-covariance updates live on the SPD manifold and use
Riemannian retractions rather than naive additive steps (the theme
[[SPD-manifold geometry and Riemannian optimization]]). And because the architecture's
training loss is a [[Renyi divergence]] family with KL as the order-one limit, the very ELBO that
EM ascends is generalized to the variational Renyi bound of [[li-turner-2016-renyi-vi]] — a
one-parameter `alpha` interpolation between the standard ELBO and the log marginal likelihood.
The "inference machinery," in other words, is the standard variational-EM loop whose objective,
gradient metric, and covariance arithmetic are each upgraded by a neighboring cluster.

> [!note] Editorial: The literal `"filtering"` label in the config is read here as the
> incremental/partial-E-step regime of [[neal-1998-variational-em]] combined with the
> iterative-refinement optimizer of [[marino-2018-iterative-amortized-inference]]; the sources
> establish each ingredient, but the specific synthesis into a streaming online filter is this
> program's design choice rather than a claim made by any one paper.

## Open questions / gaps

Several tensions remain unresolved by the available sources. First, **how many E-step iterations
suffice.** [[marino-2018-iterative-amortized-inference]] shows refinement helps but offers no
principled stopping rule; a filtering transformer must fix an iteration budget per token, trading
amortization gap against compute, and none of the sources prescribe the optimum.

Second, **the interaction of partial E-steps with the Renyi objective.** The EM coordinate-ascent
guarantee of [[neal-1998-variational-em]] is stated for the KL-based free energy; whether partial,
filtered E-steps retain a monotone-improvement guarantee under the `alpha`-divergence bound of
[[li-turner-2016-renyi-vi]] is not addressed and is a genuine theoretical gap.

Third, **the backprop-equivalence boundary.** [[millidge-2020-pc-approximates-backprop]] proves
local PC updates *converge* to backprop gradients; under truncated filtering the loop is by
construction not converged, so the exactness of the recovered gradient is approximate and its
error is uncharacterized here.

Fourth, **amortization under gauge structure.** The recognition network of
[[kingma-2013-auto-encoding-variational-bayes]] assumes a fixed coordinate frame, but this program
transports beliefs across learned gauge frames; whether an amortized encoder can remain consistent
under parallel transport and holonomy (the cross-cluster theme
[[Gauge equivariance and geometric deep learning]]) is unexamined by any source in this digest.

## Sources synthesized

- [[neal-1998-variational-em]] — EM as coordinate ascent on a single free-energy/ELBO functional;
  justification for incremental and partial (filtering) updates.
- [[friston-2010-free-energy-principle]] — free-energy minimization as a unified account of
  perception, attention, and learning; the training-objective semantics.
- [[rao-1999-predictive-coding]] — hierarchical predictive coding; precision-weighted prediction
  errors as the mechanistic prototype.
- [[bogacz-2017-free-energy-tutorial]] — explicit Gaussian E-step belief-relaxation and M-step
  precision-learning updates.
- [[kingma-2013-auto-encoding-variational-bayes]] — the VAE: amortized Gaussian recognition and the
  reparameterization trick.
- [[marino-2018-iterative-amortized-inference]] — learned iterative optimizer closing the
  amortization gap; template for filtering as finite refinement.
- [[millidge-2020-pc-approximates-backprop]] — local predictive-coding free-energy minimization
  recovers exact backprop, unifying the EM loop with gradient training.

Cross-cluster anchors drawn on above: [[amari-1998-natural-gradient]] and
[[li-turner-2016-renyi-vi]] for the M-step's metric and objective.
