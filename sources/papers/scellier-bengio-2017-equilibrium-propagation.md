---
type: paper
title: "Equilibrium Propagation: Bridging the Gap between Energy-Based Models and Backpropagation"
aliases: [Equilibrium propagation, EqProp]
authors: [Scellier B., Bengio Y.]
year: 2017
arxiv: 1602.05179
url: https://arxiv.org/abs/1602.05179
tags: [cluster/vfe, project/transformer, field/cs-ml, field/neuroscience]
created: 2026-07-11
---

# Equilibrium Propagation: Bridging the Gap between Energy-Based Models and Backpropagation

> [!info] Citation
> Scellier, B., & Bengio, Y. (2017). *Equilibrium Propagation: Bridging the Gap between Energy-Based Models and Backpropagation*. Frontiers in Computational Neuroscience, 11:24. arXiv:1602.05179.

## TL;DR
For an energy-based model whose inference settles to an equilibrium of energy $E$, the gradient of the supervised loss with respect to any parameter equals the $\beta\to 0$ limit of the contrast $\frac{1}{\beta}\big[\partial_\theta E|_{s^*_\beta} - \partial_\theta E|_{s^*_0}\big]$ between two equilibria: a free phase and a phase weakly nudged toward the target by a clamping strength $\beta$. Learning therefore needs only local energy derivatives evaluated at two settled states — no backward pass.

## Problem & setting
Energy-based recurrent networks (continuous Hopfield) trained with contrastive Hebbian learning require a fully clamped phase whose fixed point can be far from the free one, biasing the gradient. EqProp shows an infinitesimally nudged second phase yields the exact loss gradient in the limit, connecting energy-based local learning to backprop.

## Method
Free phase: relax state $s$ to a minimum $s^*_0$ of $E(\theta, s)$. Nudged phase: relax $F_\beta = E + \beta\,\ell(s, y)$ from $s^*_0$ to $s^*_\beta$. The estimator $\widehat{g}_\theta = \frac{1}{\beta}\big[\partial_\theta E(s^*_\beta) - \partial_\theta E(s^*_0)\big] \to d\ell/d\theta$ as $\beta \to 0$. Later work (Laborieux et al. 2021) shows a **symmetric** two-sided contrast at $\pm\beta$ cancels the $O(\beta)$ bias and is what makes deeper models train.

## Key results
Exact gradient theorem at equilibrium; MNIST-scale demonstrations in the original paper; the symmetric variant scales to CIFAR-class ConvNets. No language-model results exist in this line.

## Relevance to this research
EqProp supplies the through-$q^*$ credit estimator for the [[VFE Transformer Program]]'s backprop-free prescription ([[Nudged two-phase EM]]): the vfe3 E-step is already an energy-minimizing relaxation of the free energy $F$, so nudging it with the canonical observation term (which [[participatory-it-from-bit|PIFB]] places inside the belief subsystem) and contrasting the analytic envelope statistics $\partial F/\partial\theta$ between $\pm\lambda$ equilibria estimates exactly the credit path that the target-blind clean-EM attempt (VFE_2.0 pure_fep) structurally dropped. The caveats that bind in vfe3 are the theorem's premises: truncated (non-equilibrium) settling and a feedforward prior-handoff cascade violate the single-joint-energy assumption, which is why the plan demands shared-start symmetric continuations, stationarity-residual gates, and finite-difference oracle checks rather than claiming the theorem.

## Cross-links
- Concepts: [[Variational free energy]] · [[Energy-Based Models]] · [[Fixed-point iteration]]
- Methods: [[Nudged two-phase EM]] · [[Predictive coding network]] · [[Variational EM]]
- Related sources: [[millidge-2020-pc-approximates-backprop]] · [[hinton-2022-forward-forward]] · [[bai2019deep-equilibrium]]

## BibTeX
```bibtex
@article{scellier2017equilibrium,
  title   = {Equilibrium Propagation: Bridging the Gap between Energy-Based Models and Backpropagation},
  author  = {Scellier, Benjamin and Bengio, Yoshua},
  journal = {Frontiers in Computational Neuroscience},
  volume  = {11},
  pages   = {24},
  year    = {2017},
  eprint  = {1602.05179},
  archivePrefix = {arXiv}
}
```
