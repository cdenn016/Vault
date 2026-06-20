---
type: paper
title: On the Variance of the Adaptive Learning Rate and Beyond
aliases:
  - "Liu et al. 2020 — RAdam"
  - "Variance of the Adaptive Learning Rate"
authors:
  - Liyuan Liu
  - Haoming Jiang
  - Pengcheng He
  - Weizhu Chen
  - Xiaodong Liu
  - Jianfeng Gao
  - Jiawei Han
year: 2020
arxiv: 1908.03265
url: https://arxiv.org/abs/1908.03265
tags:
  - cluster/methodology
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# On the Variance of the Adaptive Learning Rate and Beyond

> [!info] Citation
> Liu, L., Jiang, H., He, P., Chen, W., Liu, X., Gao, J., & Han, J. (2020). On the Variance of the Adaptive Learning Rate and Beyond. International Conference on Learning Representations (ICLR 2020). arXiv:1908.03265.

## TL;DR

Adam and the other per-coordinate adaptive optimizers divide each parameter's step by a running root-mean-square of its gradients, $\sqrt{\hat v_t}$. Early in training this denominator is estimated from only a handful of samples, so the *adaptive learning rate* it implies has very large — at the first step, undefined — variance, and the optimizer takes erratic, badly-scaled steps that can push the trajectory into a bad region before the second-moment estimate settles. This paper gives a quantitative account of that variance, argues that the ubiquitous but unprincipled trick of **learning-rate warmup** works precisely because it is a variance-reduction device for those early steps, and then derives **RAdam (Rectified Adam)**: a closed-form rectification term, computed from the effective length of the exponential moving average, that explicitly down-scales (or in the very first steps disables) the adaptive update until enough gradient history has accumulated for the variance to be tractable. The result is an optimizer that recovers warmup-like stability automatically, with one fewer schedule to tune.

## Problem & setting

Adam maintains a biased exponential moving average of squared gradients $v_t = \beta_2 v_{t-1} + (1-\beta_2)\, g_t^2$, bias-corrects it to $\hat v_t$, and scales the (momentum) update by $1/(\sqrt{\hat v_t} + \epsilon)$. The quantity $1/\sqrt{\hat v_t}$ is the *adaptive learning rate*. The authors observe that for small $t$ this average aggregates too few squared-gradient samples to be a reliable estimate of the true second moment, so $1/\sqrt{\hat v_t}$ is a high-variance random quantity. Treating the per-coordinate squared gradients as approximately scaled inverse-chi-square / scaled-inverse-gamma samples, they show the variance of the adaptive learning rate is largest at the start of training and decays as the effective sample size grows. This is the analytical mechanism the paper offers for a long-standing empirical fact: training Transformers and other Adam-trained models from a cold start is unstable, and practitioners patch it with a warmup schedule (ramp the learning rate up from near zero over the first thousands of steps) that the original Adam paper (Kingma & Ba) never prescribed and never explained. The work builds directly on Adam and on the folklore of Transformer warmup (Vaswani et al.), and it shares intellectual lineage with bias-correction arguments and with variance-reduction analyses of stochastic optimization.

## Method

The construction hinges on the *effective length of the simple moving average* implied by $\beta_2$. Its maximum value is
$$ \rho_\infty = \frac{2}{1-\beta_2} - 1, $$
and at step $t$ the instantaneous length is
$$ \rho_t = \rho_\infty - \frac{2 t \,\beta_2^{\,t}}{1 - \beta_2^{\,t}}. $$
When $\rho_t$ is large enough that the variance of the adaptive learning rate is finite and estimable (in practice the paper uses the threshold $\rho_t > 4$), RAdam applies the adaptive update but multiplies it by a **rectification term**
$$ r_t = \sqrt{\frac{(\rho_t - 4)(\rho_t - 2)\,\rho_\infty}{(\rho_\infty - 4)(\rho_\infty - 2)\,\rho_t}}, $$
chosen so that the variance of the rectified adaptive learning rate is approximately constant across steps — it down-weights the adaptive step early, when $\rho_t$ is small, and tends to $1$ as $\rho_t \to \rho_\infty$. When $\rho_t \le 4$ the variance is intractable, so RAdam degenerates to the **non-adaptive** update: it applies the bias-corrected momentum step with the adaptive rescaling switched off, i.e. plain SGD-with-momentum, for those first few iterations. The net effect is an automatically generated warmup: the optimizer begins in a conservative, variance-controlled regime and smoothly transitions to full Adam as the second-moment estimate becomes trustworthy, with no hand-designed schedule.

## Key results

The paper's central claim is conceptual and is supported both analytically and empirically: warmup is a variance-reduction heuristic, and the variance of the adaptive learning rate can be controlled directly. Empirically the authors evaluate RAdam across image classification (e.g. CIFAR and ImageNet), language modeling, and neural machine translation, reporting that RAdam matches or exceeds Adam-with-tuned-warmup while being markedly more robust to the choice of learning rate and removing the warmup schedule as a separate hyperparameter. A frequently-cited qualitative finding is that vanilla Adam without warmup is sensitive to a small number of large, distorted early updates and can converge to noticeably worse solutions, whereas RAdam avoids this failure mode by construction. The evidence is solid for the robustness and ease-of-tuning claims; the strength of RAdam's *final-accuracy* advantage over a well-tuned Adam-plus-warmup baseline is more modest and task-dependent, and later literature has noted that careful warmup tuning can close much of the gap. The lasting contribution is the diagnosis — naming early-training adaptive-learning-rate variance as the thing warmup fixes — more than a uniformly dominant optimizer.

## Relevance to this research

The program's M-step is a Fisher-preconditioned / [[Natural gradient]] update and its E-step is a filtering update of the Gaussian beliefs $(\mu, \Sigma, \phi)$; both are *adaptive-preconditioner* updates by construction, dividing a raw gradient by an estimated curvature or second-moment quantity. RAdam's diagnosis applies directly: any preconditioner estimated online from few samples — an empirical Fisher, a running covariance, a streaming SPD estimate — has its largest variance at the start of training, so the earliest preconditioned steps are the most dangerous, exactly when the model has no LayerNorm module to absorb a bad step (this architecture has none in the pure no-NN path). This paper therefore frames the optimizer-side stability question for the program: either warm up the effective step on the belief and gauge parameters, or rectify the preconditioner by its own estimated variance, before trusting the adaptive scaling. It also reframes warmup not as a Transformer-specific superstition but as a general property of adaptive updates, which bears on how the program's training budget and schedule interact with [[Neural scaling laws]] when the M-step preconditioner is itself learned. The rectification recipe — fall back to a non-adaptive step while the curvature estimate is unreliable, then phase in the preconditioner — is a concrete, transferable design pattern for stabilizing the Fisher-metric and affine-invariant-SPD updates at initialization.

## Cross-links

- Concepts / Themes: [[Natural gradient]], [[Neural scaling laws]]
- Related sources: [[amari-1998-natural-gradient]], [[martens-2015-kfac]]

## BibTeX

```bibtex
@inproceedings{liu2020varianceada,
  author    = {Liu, Liyuan and Jiang, Haoming and He, Pengcheng and Chen, Weizhu and Liu, Xiaodong and Gao, Jianfeng and Han, Jiawei},
  title     = {On the Variance of the Adaptive Learning Rate and Beyond},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2020},
  eprint    = {1908.03265},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/1908.03265}
}
```
