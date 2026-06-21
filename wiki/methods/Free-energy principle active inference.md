---
type: method
title: Free-energy principle active inference
aliases:
  - Free-energy principle
  - FEP
  - Friston free energy
  - "Free Energy Principle"
  - "Free energy principle"
tags:
  - cluster/vfe
  - cluster/attention
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-18
updated: 2026-06-18
---

# Free-energy principle active inference

## What it is

The free-energy principle (FEP) is a single normative claim — proposed by Karl Friston in [[friston-2010-free-energy-principle]] — that any self-organizing agent that resists dispersion into disorder must act and perceive so as to minimize *variational free energy*, a tractable upper bound on the surprise (negative log model evidence) of its sensory inputs. *Active inference* is the corollary that both perception and action are two routes to the same minimization: perception adjusts internal beliefs to reduce free energy given the senses, while action changes the senses to match predictions. The principle subsumes perception, attention, learning, and motor control under one objective, and it is the biological and theoretical taproot of this project's training functional and precision-weighted inference.

## How it works

The quantity minimized is the same [[Variational free energy]] that appears in machine learning as the negative [[Evidence lower bound (ELBO)]]. For an agent with sensory data and hidden causes, free energy equals the expected (under a variational belief *q*) negative log joint plus the negative entropy of *q*; equivalently it is the log evidence plus the KL divergence from *q* to the true posterior. Because that KL is non-negative, free energy bounds surprise, and driving it down both sharpens the belief and raises a lower bound on evidence. This is exactly the negative-free-energy / ELBO functional that [[neal-1998-variational-em]] identified at the heart of EM — a single objective whose coordinate ascent gives an E-step over beliefs and an M-step over parameters, the decomposition this work's [[Variational EM]] loop inherits.

Under the standard Gaussian (Laplace) assumptions, free-energy minimization reduces to a strikingly simple dynamics. As [[bogacz-2017-free-energy-tutorial]] derives step by step, beliefs about hidden states relax along [[Prediction error]] signals that are weighted by their precisions (inverse variances), and parameters and precisions are learned by gradient ascent on the same free energy. This [[Precision weighting]] is the formal content of "attention" in the FEP: more precise prediction errors exert more influence, so allocating precision *is* allocating attention. The hierarchical predictive-coding circuit of [[rao-1999-predictive-coding]] supplies the mechanistic picture — feedback connections carry top-down predictions, feedforward connections carry precision-weighted residual errors, and each level only ever sees local errors. [[millidge-2020-pc-approximates-backprop]] then shows that such purely local prediction-error minimization converges to exact backpropagation gradients on arbitrary computation graphs, closing the gap between this biologically motivated inference loop and ordinary end-to-end gradient training.

The modern machine-learning incarnation of the same objective is the variational autoencoder of [[kingma-2013-auto-encoding-variational-bayes]], which trains the ELBO end-to-end with the [[Reparameterization trick]] and an [[Amortized inference]] recognition network. [[marino-2018-iterative-amortized-inference]] sharpens this into an *iterative* amortized scheme that repeatedly encodes free-energy gradients to refine beliefs, narrowing the amortization gap that a single forward pass leaves — a design that mirrors active inference's relaxation dynamics more faithfully than a one-shot encoder.

## Strengths / limitations

The principle's strength is unification: a single scalar functional explains perception, attention (as precision control), learning, and action, and it connects neuroscience, Bayesian inference, and information geometry through one quantity. It is also constructive — the Gaussian case yields concrete, local, biologically plausible update rules. Its limitations are equally well known. The bound is only as good as the variational family; a diagonal-Gaussian *q* can be badly mismatched to a multimodal posterior, leaving a residual KL the objective cannot see. The framework is famously general to the point of being hard to falsify, and the action/policy side of active inference (expected free energy over future trajectories) introduces planning machinery this project does not adopt. Precision estimation can be unstable, and the principle says what is minimized, not how to parameterize the beliefs or the metric — gaps this work fills with explicit manifold geometry.

## Relation to this work

The VFE transformer takes the free-energy principle as its literal training objective and inference semantics, then re-engineers the pieces the FEP leaves underspecified. **What it borrows:** the negative-free-energy/ELBO functional as the loss; the E-step/M-step split of [[Variational EM]] for per-token Gaussian beliefs (mu, Sigma); precision-weighted prediction-error dynamics recast as [[Precision weighting]] inside attention, so that active inference's attention-as-precision enters the transformer's similarity computation as the precision term inside the Gaussian-KL attention logit (cf. the kernel view of attention in [[tsai-2019-kernel-attention]] and the softmax baseline of [[vaswani-2017-attention]]); the config flag literally named `precision_weighted_attention` is a *distinct*, default-OFF, query-independent reliability bias, **not** this structural mechanism (see [[Precision weighting]]); and the *filtering* gradient mode, which performs the partial, online belief updates that [[neal-1998-variational-em]] licenses as valid incremental free-energy descent.

**Where it differs / improves:** classical FEP treats beliefs as flat Euclidean Gaussians, whereas this work makes the covariance Sigma a first-class point on the SPD manifold and updates it with geometry-aware retractions, replacing naive precision gradients with Riemannian ones (see [[SPD-manifold geometry and Riemannian optimization]]). It replaces the KL inside free energy with a one-parameter [[Renyi divergence]] / [[Alpha-divergence]] objective (KL recovered at the alpha to 1 limit) following [[li-turner-2016-renyi-vi]] and [[vanerven-2014-renyi-kl]], tuning the bound's tightness and mass-covering behavior. It conducts the M-step with the [[Natural gradient]] under the [[Fisher information metric]] ([[amari-1998-natural-gradient]]) rather than plain gradient descent, making parameter updates reparameterization-invariant. And it adds an entire layer the FEP never specified: a GL(k) gauge structure over the belief frames (see [[Gauge equivariance and geometric deep learning]]), so that beliefs are transported across tokens and positions in a symmetry-respecting way rather than compared in an arbitrary fixed basis. In short, the free-energy principle supplies the *what* — minimize variational free energy through precision-weighted inference — and this project supplies a richer *geometry* of beliefs, divergences, and gauge frames in which that minimization is carried out.

> [!note] Editorial: The mapping from active inference's action/policy selection onto a sequence transformer is loose; this work imports the perceptual (belief-updating) half of active inference and its precision-as-attention reading, not its expected-free-energy planning over actions.

## Sources

- [[friston-2010-free-energy-principle]] — the canonical free-energy principle and active inference.
- [[bogacz-2017-free-energy-tutorial]] — explicit Gaussian free-energy derivation with precision-weighted updates.
- [[rao-1999-predictive-coding]] — hierarchical predictive coding; precision-weighted error feedforward, prediction feedback.
- [[neal-1998-variational-em]] — EM as coordinate ascent on the negative-free-energy/ELBO functional.
- [[kingma-2013-auto-encoding-variational-bayes]] — the ELBO trained via reparameterization and amortized Gaussian inference.
- [[marino-2018-iterative-amortized-inference]] — iterative refinement of variational beliefs from free-energy gradients.
- [[millidge-2020-pc-approximates-backprop]] — local prediction-error minimization approximates backprop.
- [[li-turner-2016-renyi-vi]], [[vanerven-2014-renyi-kl]] — the Renyi/alpha generalization of the variational bound.
- [[amari-1998-natural-gradient]] — natural gradient for the M-step.
- [[vaswani-2017-attention]], [[tsai-2019-kernel-attention]] — the attention baseline reinterpreted via precision weighting.

## See also

- [[Variational free energy and predictive coding]] — the theme tying this method to predictive coding and the ELBO.
- [[Inference machinery — variational EM and filtering]] — the E-step/M-step/filtering implementation.
- [[Variational EM]] — the coordinate-ascent inference loop.
- [[Predictive coding network]] — the circuit-level realization of free-energy minimization.
- [[Iterative amortized inference]] — learned, iterative belief refinement.
- [[Variational autoencoder (VAE)]] — the gradient-trained ELBO blueprint.
- [[Precision weighting]], [[Prediction error]], [[Evidence lower bound (ELBO)]], [[Variational free energy]] — core constructs.
- [[VFE Transformer Program]] — the project this page serves.
