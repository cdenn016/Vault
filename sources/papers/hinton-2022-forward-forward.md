---
type: paper
title: "The Forward-Forward Algorithm: Some Preliminary Investigations"
aliases:
  - "Hinton 2022"
  - "Forward-Forward"
  - "FF algorithm"
authors:
  - Hinton, Geoffrey
year: 2022
arxiv: "2212.13345"
url: https://arxiv.org/abs/2212.13345
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/neuroscience
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The Forward-Forward Algorithm: Some Preliminary Investigations

> [!info] Citation
> Hinton, G. (2022). "The Forward-Forward Algorithm: Some Preliminary Investigations." arXiv:2212.13345.

## TL;DR
Hinton introduces the Forward-Forward (FF) algorithm, a greedy multi-layer learning procedure that replaces backpropagation's single forward plus backward pass with two forward passes — one on real (positive) data and one on negative (corrupted/generated) data. Each layer optimizes its own local objective: maximizing a layer-wise "goodness" (sum of squared pre-normalization activities) on positive data and minimizing it on negative data. The algorithm is biologically motivated, avoids storing activations for a backward pass, and is compatible with analog hardware and non-differentiable black-box layers.

## Problem & setting
Backpropagation, while empirically powerful, is biologically implausible: it requires exact knowledge of the forward computation, storing activations for a subsequent backward pass, and symmetric top-down connections — none of which are observed in cortex. Learning sequences via BPTT requires frequent interruptions incompatible with real-time sensory processing. Reinforcement learning alternatives suffer from high variance that scales poorly with network size. Prior contrastive approaches (Boltzmann machines, SimCLR, GANs) either require equilibrium sampling (intractable) or still use backpropagation within their networks. FF aims to provide a local, layer-wise, biologically plausible alternative that retains competitive performance on small-to-medium tasks.

## Method
The core idea is to contrast positive data (real examples, possibly with the label embedded in the input) against negative data (corrupted or network-generated examples). For each layer, the goodness function is the sum of squared pre-normalization activities, $g = \sum_j y_j^2$, and the probability of a sample being positive is modeled as:
$$p(\text{positive}) = \sigma\!\left(\sum_j y_j^2 - \theta\right)$$
where $\theta$ is a threshold and $\sigma$ is the logistic function. Layer normalization is applied to the output before passing it to the next layer, which strips the goodness signal and forces each subsequent layer to extract new structure from the orientation (not length) of the activity vector. Weight updates in a given layer do not change the layer-normalized output for the current input vector, enabling simultaneous per-layer online updates — a fast-learning property analogous to the perceptron convergence step. For supervised tasks, the correct label is embedded directly in the input pixels; classification is performed by running the network once per candidate label and choosing the label that accumulates the highest total goodness across layers. A recurrent extension processes static images as repeated video frames, with each layer receiving both bottom-up and top-down inputs from the previous time step, enabling top-down influences on representations without backpropagation. The paper also discusses a connection to predictive coding when the sign of the goodness objective is reversed: top-down signals learn to cancel bottom-up signals on positive data.

## Key results
On permutation-invariant MNIST with four fully connected hidden layers of 2000 ReLUs: FF achieves 1.36% test error (supervised) versus backpropagation's 1.4% baseline. With data augmentation (jittering), FF reaches 0.64% test error, matching convolutional backpropagation networks. The recurrent FF variant achieves 1.31% test error. On CIFAR-10 with non-convolutional local-receptive-field networks, FF achieves 41–44% test error versus 37–39% for backpropagation — somewhat worse but without the performance gap widening with depth. FF is slower to converge than backpropagation (roughly three times more epochs for comparable performance) and generalizes slightly less well on these toy tasks, but these gaps do not preclude biological plausibility or analog hardware use cases.

## Relevance to this research
The FF algorithm is directly relevant to the VFE transformer program in several respects. First, FF's layer-wise goodness optimization — minimizing a local energy-like scalar per layer — is structurally analogous to VFE minimization per layer in the gauge-theoretic transformer: both replace global backpropagation with local objective minimization. Second, the FF positive/negative data contrast is a discrete analog of the KL divergence terms in the VFE free energy, which also contrast a belief distribution against a prior or transported belief; the goodness threshold $\theta$ plays the role of a reference energy. Third, FF's use of layer normalization to pass only the orientation of the activity vector (not its length) to the next layer parallels the normalization implicit in working on the unit sphere or SPD cone in information geometry — in both cases, the "length" (energy/goodness) is factored out as a local signal. Fourth, the connection to predictive coding (section 3.5) is directly relevant since predictive coding is a limiting case of VFE minimization, and the recurrent top-down/bottom-up structure in FF mirrors the hierarchical belief propagation (`h → s → p → q → observations`) in the VFE hierarchy. Fifth, the mortal computation discussion (section 9) and the use of distillation to transfer learned functions (not weights) between hardware instances resonates with the multi-agent active inference setting where agents must transfer beliefs, not parameters.

## Cross-links
- Concepts: [[Variational Free Energy]] [[Predictive Coding]] [[Contrastive Learning]] [[Layer Normalization]] [[Active Inference]]
- Related sources: [[rao-ballard-1999-predictive-coding]] [[hinton-sejnowski-1986-boltzmann]]
- Manuscript/Project: [[VFE Transformer Program]] [[GL(K) Attention]]

## BibTeX
```bibtex
@article{hinton2022forward,
  author  = {Hinton, Geoffrey},
  title   = {The Forward-Forward Algorithm: Some Preliminary Investigations},
  year    = {2022},
  eprint  = {2212.13345},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
}
```
