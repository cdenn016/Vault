---
type: paper
title: "Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer"
aliases:
  - "Yang et al. 2022 — muP"
  - "Tensor Programs V"
  - "Maximal Update Parametrization"
authors:
  - Greg Yang
  - Edward J. Hu
  - Igor Babuschkin
  - Szymon Sidor
  - Xiaodong Liu
  - David Farhi
  - Nick Ryder
  - Jakub Pachocki
  - Weizhu Chen
  - Jianfeng Gao
year: 2022
arxiv: 2203.03466
url: https://arxiv.org/abs/2203.03466
tags:
  - cluster/methodology
  - project/transformer
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer

> [!info] Citation
> Yang, G., Hu, E. J., Babuschkin, I., Sidor, S., Liu, X., Farhi, D., Ryder, N., Pachocki, J., Chen, W., & Gao, J. (2022). Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer. NeurIPS 2021. arXiv:2203.03466.

## TL;DR

Optimal hyperparameters — learning rate above all — normally drift as a network grows, so the conventional recipe re-tunes them at every scale, which is ruinous for billion-parameter models where a single training run is the budget. This paper identifies a specific parametrization of initialization variances, per-layer learning-rate multipliers, and output-layer scaling, the **Maximal Update Parametrization (muP)**, under which the optimal hyperparameters become *stable across width*: the loss landscape, viewed in the right coordinates, does not deform as the model widens. The practical consequence is **muTransfer**, a zero-shot procedure in which one tunes hyperparameters on a small, cheap proxy model and copies them, unchanged, to a target model that is orders of magnitude wider. The stability is not a heuristic observation but a prediction of the Tensor Programs framework's infinite-width limit: muP is precisely the parametrization in which *every* layer continues to learn a non-trivial feature update at infinite width, as opposed to the standard "neural tangent kernel" parametrization in which hidden features freeze. The authors demonstrate the method by tuning small proxies and transferring to BERT-large and a 6.7B-parameter GPT-3, matching or beating the published, individually-tuned models at a small fraction of the tuning compute.

## Problem & setting

Training a large model is dominated by the cost of one run, so the standard practice of sweeping hyperparameters at the target scale is infeasible — yet hyperparameters demonstrably do not transfer naively. Under the conventional "standard parametrization" (SP), the learning rate that is optimal for a narrow network is wrong for a wide one, because the magnitude of activations, gradients, and weight updates all scale with width $n$ in parametrization-dependent ways. The prior theoretical lens for the infinite-width limit, the Neural Tangent Kernel (NTK) parametrization, makes the network behave as a linearized kernel machine in which the hidden layers do not move from their initialization — feature learning is lost — so it cannot explain or preserve the behavior of real, finite, feature-learning networks. The question Yang et al. pose is geometric in spirit: is there a parametrization in which the *training dynamics themselves*, not merely the function at initialization, converge to a well-defined and width-independent limit, so that the location of the optimum in hyperparameter space stops moving as $n \to \infty$?

## Method

The construction assigns, to each weight matrix, a width-dependent triple of scales — the initialization variance, a multiplier on the learning rate, and (for input and output layers) a multiplier on the layer's contribution — chosen so that three quantities are all $\Theta(1)$ in width throughout training: the preactivations, the change in preactivations induced by one gradient step, and the logits. Concretely, for a hidden weight matrix of fan-in $n$, muP initializes with variance $\propto 1/n$ and scales the (Adam) learning rate $\propto 1/n$, while the output (readout) layer is initialized smaller and its output divided by $n$, and embedding-like input layers are treated as $\Theta(1)$-fan-in. The governing principle is *maximality*: among parametrizations that admit a sensible infinite-width limit, muP is the unique one in which **every** layer's features receive an update of the largest stable order, $\Theta(1)$, rather than $\Theta(1/\sqrt{n})$ (vanishing, as in NTK) or $\Theta(\sqrt{n})$ (blowing up). Writing $n$ for width, the contrast with standard parametrization is that SP couples the effective per-coordinate update size to $n$, so the curvature of the loss in hyperparameter space drifts; muP cancels that coupling. Because the limit is a *feature-learning* limit derived inside the Tensor Programs calculus, the optimal learning rate, initialization scale, and related knobs provably approach width-independent constants, which is the formal content of transferability:

$$\eta^\star(n) \xrightarrow{\;n\to\infty\;} \eta^\star_\infty, \qquad \text{under muP}.$$

muTransfer operationalizes this: parametrize the target in muP, sweep hyperparameters on a narrow proxy, and transfer the optimum verbatim. The paper notes transfer is empirically robust across width and, to a useful degree, across depth, batch size, sequence length, and training horizon, though width is the dimension with rigorous backing.

## Key results

The central theoretical result is that muP yields a non-degenerate, feature-learning infinite-width limit in which optimal hyperparameters are width-invariant, derived as a consequence of the Tensor Programs master theorem rather than asserted. Empirically the method is validated by transfer at scale: tuning on small proxy models and copying the hyperparameters to far larger targets, the authors report that a muTransferred BERT-large outperformed its published, separately-tuned baseline, and that a muTransferred 6.7B-parameter GPT-3 matched or exceeded the published model while spending only a small fraction (single-digit percent) of the total pretraining compute on the entire tuning procedure. Diagnostic learning-rate sweeps show the characteristic signature: under standard parametrization the optimal learning rate shifts steadily leftward as width grows, whereas under muP the loss-versus-learning-rate curves for different widths share a common minimum. The evidence is strong for transfer across *width* — both theoretically grounded and demonstrated on flagship models — and more empirical-than-proven for the secondary axes (depth, batch, horizon), a distinction the paper is careful to make.

## Relevance to this research

muP is the discipline this program must satisfy if any hyperparameter is to survive the $K$-sweep over belief dimension. The model's parameters and scales — the Lie-algebra `phi` initialization, the covariance `sigma` init, and especially the temperature coefficient $\kappa$ in $\tau = \kappa\sqrt{\dim_h}$ — play the role muP assigns to per-layer init variances and learning-rate multipliers: they must be set so that activations, belief updates, and gradients stay $\Theta(1)$ as the width-like dimensions ($K$, $\dim_h$, head count) grow, or else a $\kappa$ tuned at small $K$ silently becomes wrong at large $K$. The explicit $\sqrt{\dim_h}$ factor in $\tau$ is already a width-correction of exactly muP's flavor (it is the same scale that keeps softmax logits $\Theta(1)$), which makes muP the right yardstick for asking whether the *remaining* coefficient $\kappa$ is genuinely width-stable or whether it absorbs a hidden $K$-dependence that should have been factored out. Because the VFE update is a [[Natural gradient]]-style preconditioned step rather than raw SGD, the relevant muP learning-rate rule is the one for adaptive/Adam-like optimizers, and the program's per-block metric preconditioning may already supply some of the width-correction muP imposes by hand; whether the two coincide or double-count is a falsifiable question a small-vs-large $K$ learning-rate sweep would settle. This connects directly to the program's scaling story: muP is what lets the [[Neural scaling laws]] of Kaplan and Chinchilla be measured cleanly, since without width-stable hyperparameters a scaling curve conflates the true compute-optimal frontier with per-scale tuning noise.

## Cross-links

- Concepts / Themes: [[Neural scaling laws]], [[Natural gradient]]
- Related sources: [[amari-1998-natural-gradient]]

## BibTeX

```bibtex
@inproceedings{yang2022tensorprog,
  author    = {Yang, Greg and Hu, Edward J. and Babuschkin, Igor and Sidor, Szymon and Liu, Xiaodong and Farhi, David and Ryder, Nick and Pachocki, Jakub and Chen, Weizhu and Gao, Jianfeng},
  title     = {Tensor Programs {V}: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2022},
  eprint    = {2203.03466},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/2203.03466}
}
```
