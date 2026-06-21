---
type: paper
title: "Long Short-Term Memory"
aliases:
  - "Hochreiter 1997"
  - "LSTM"
authors:
  - Hochreiter, Sepp
  - Schmidhuber, Jürgen
year: 1997
arxiv: null
url: https://doi.org/10.1162/neco.1997.9.8.1735
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/neuroscience
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Long Short-Term Memory

> [!info] Citation
> Hochreiter, S., & Schmidhuber, J. (1997). "Long Short-Term Memory." *Neural Computation*, 9(8), 1735–1780. https://doi.org/10.1162/neco.1997.9.8.1735

## TL;DR
LSTM addresses the vanishing and exploding gradient problem in recurrent networks by introducing a novel architecture centered on a constant error carousel (CEC): a self-connected linear unit with a fixed weight of 1.0 that allows error signals to flow back through time without exponential decay. Multiplicative input and output gate units learn when to write to and read from the memory cell, resolving the input/output weight conflict that makes naive constant-error approaches unworkable. The resulting algorithm is O(W) per time step and local in both space and time, learning to bridge time lags exceeding 1000 steps where all prior recurrent methods fail.

## Problem & setting
Recurrent networks trained by backpropagation through time (BPTT) or real-time recurrent learning (RTRL) suffer from exponential error decay across time: the gradient of an error at time t with respect to a unit activation at time t−q scales as a product of q Jacobian factors, each typically less than 1 in magnitude (for logistic sigmoids, f′_max = 0.25). When all |f′ · w| < 1 the error signal vanishes geometrically; when any exceeds 1 it may blow up. The result is that networks cannot reliably learn dependencies spanning more than a few dozen steps. Prior remedies — time constants (Mozer 1992), Kalman filters (Puskorius & Feldkamp 1994), hierarchical chunkers (Schmidhuber 1992/1993), second-order sigma-pi units (Watrous & Kuhn 1992) — either require task-specific tuning, do not scale, or fail to generalize to unseen lag durations.

## Method
The core idea is to enforce constant error flow through a self-connected linear unit (the constant error carousel, CEC), satisfying f′_j(net_j) · w_jj = 1.0, which requires f_j linear with w_jj = 1. Each CEC unit forms the center of a memory cell c_j. The cell's internal state evolves as:

    s_{c_j}(t) = s_{c_j}(t-1) + y_{in_j}(t) · g(net_{c_j}(t))

and its output is:

    y_{c_j}(t) = y_{out_j}(t) · h(s_{c_j}(t))

where g squashes the cell input and h scales the output. Two multiplicative gate units — an input gate in_j and an output gate out_j — control write and read access respectively. Their activations are computed via standard sigmoid units connected to all other units. Error signals arriving at memory cell net inputs are truncated (not propagated further back in time) except within the CEC itself, where they flow back indefinitely unchanged. This truncated RTRL variant achieves O(W) complexity per time step with storage requirements independent of sequence length. Memory cell blocks of size S share a single input and output gate, providing a distributed internal representation per block.

## Key results
LSTM was evaluated against RTRL, BPTT, recurrent cascade correlation, Elman nets, and neural sequence chunking on a series of artificial tasks designed so that random weight guessing is infeasible and minimal time lags are long throughout the training set. Key empirical findings include: (1) On embedded Reber grammar tasks (short-to-medium lags), LSTM clearly outperforms RTRL and BPTT in number of successful runs and learning speed. (2) On distractor tasks with minimal time lags of 100, 500, and 1000 steps and noisy input, LSTM solves all conditions while BPTT and RTRL fail already at 10-step lags. (3) On the "adding problem" and other continuous-valued long-lag tasks, LSTM succeeds where all competing methods fail entirely. The truncated update rule renders the algorithm O(W) per time step with no activation stack, unlike full BPTT which is local in space but not in time, or RTRL which is local in time but O(W²) in space.

## Relevance to this research
LSTM is the canonical prior work on learned gating mechanisms for controlling information flow over time, which provides direct conceptual ancestry for the attention mechanisms in the VFE transformer. The gate-as-multiplicative-selector pattern — where a learned scalar modulates information passage — resurfaces in softmax attention as β_{ij} weighting belief transport Ω_{ij} q_j. The CEC's constant error flow under truncated gradients is structurally analogous to the VFE free-energy minimization objective maintaining stable belief geometry across transformer layers. More concretely, the GL(K) gauge-equivariant attention mechanism can be viewed as replacing LSTM's scalar gates with group-valued parallel transport operators, generalizing gating from R to GL(K) while preserving a similar information-routing function. The O(W) local-in-space-and-time property of LSTM motivates comparable efficiency aspirations in the per-layer VFE update rules.

## Cross-links
- Concepts: [[Attention Mechanism]], [[Recurrent Networks]], [[Vanishing gradient|Vanishing Gradient Problem]]
- Related sources: [[vaswani-2017-attention|vaswani2017attention]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{hochreiter1997long,
  author  = {Hochreiter, Sepp and Schmidhuber, J{\"u}rgen},
  title   = {Long Short-Term Memory},
  journal = {Neural Computation},
  volume  = {9},
  number  = {8},
  pages   = {1735--1780},
  year    = {1997},
  doi     = {10.1162/neco.1997.9.8.1735},
}
```
