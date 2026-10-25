---
type: run
title: "VFE_3.0 backprop-free local-learner test on WikiText-103 bytes, October 21 to 25, 2026"
aliases: ["vfe3 local-learner test", "Local-learner test October 2026"]
tags: [cluster/vfe, project/transformer, field/statistics, field/cs-ml]
year: 2026
created: 2026-10-25
---

# VFE_3.0 backprop-free local-learner test on WikiText-103 bytes, October 21 to 25, 2026

> [!info] Scope
> A small test of whether learning from finite-inference posterior statistics, with no derivative of the inference, comes close to backpropagation through the same inference. It addresses the risk named in the October 21 review of the neural-free continuation package (`VFE_3.0/docs/research/2026-10-20-neural-free-continuation/review-2026-10-21.md`). Code: `VFE_3.0/vfe3/local_learner/`, `local_learner_test.py`, `tests/test_local_learner_20261021.py` (merged to `main` through PR #155). Full records: `VFE_3.0/docs/research/2026-10-21-local-learner-test/{design,results,findings}.md` and `results/*.jsonl` (that folder is git-ignored and exists only on the local disk). All stages ran on the RTX 5090; one seed axis of three stacked seeds per arm.

## Model and learning rules

The model is a latent linear-Gaussian state over bytes, $z_t\mid z_{t-1},y_{t-1}\sim\mathcal N(Gz_{t-1}+e_{y_{t-1}},Q)$, read out through a depth-8 probit vocabulary tree, so every factor is a normalized conditional. Every rule uses one causal assumed-density Gaussian filter ([[minka-2001-expectation-propagation]]). The local arm is stepwise EM ([[cappe-2009-online-em]]) with step $\max((k+1)^{-0.6},0.2)$: the tree nodes use the probit augmentation of [[albert-1993-probit-data-augmentation]], and the transition is a ridge regression on lag-one moments from a windowed Rauch–Tung–Striebel smoother ([[rauch-1965-rts-smoother]]). Backpropagation trains the same model through the same filter (Adam, truncated BPTT). A target-blind control computes transition statistics from the forecast, which removes the token-to-state credit path. Each update uses 8,192 tokens; one pass is 610 updates over 5M training bytes; scores are bits per byte on 200k validation bytes (unigram 4.604, bigram 3.561, trigram 2.980).

## Results

One-pass validation bits per byte, seed means (seed deviations 0.002 to 0.009):

| d | Local (window 16) | Target-blind | Backprop | Local gain / backprop gain |
| --- | --- | --- | --- | --- |
| 8 | 3.498 | 4.387 | 3.501 | 1.003 |
| 16 | 3.403 | 4.240 | 3.361 | 0.966 |
| 32 | 3.370 | 4.138 | 3.270 | 0.925 |
| 64 | 3.356 | 3.944 | 3.227 | 0.906 |

The local rule passes the design's 0.8 viability threshold at every d, and the credit path is present (local beats blind by 0.59 to 0.89 bits per byte). The filter agrees with a 4,096-particle estimate of the exact predictive within 0.007 bits per byte in every run.

The gap was localized by elimination. A 64-step credit horizon changed neither rule by more than 0.002 bits per byte, and EP-cavity node statistics changed the local arm by under 0.001. Started from backpropagation's one-pass parameters, the local rule stayed at 3.264 to 3.269 for a full pass, so backpropagation's optimum is, to this precision, an EM fixed point, and the gap is optimization speed: three local passes reach 0.953 of backpropagation's one-pass gain. This fits the slow EM modes of high missing information ([[dempster-1977-em-algorithm]], [[meng-1994-em-convergence-rates]]); the latent state also has an unidentified $GL(d)$ frame. Parameter expansion of the probit step ([[liu-1998-px-em]]) gained 0.011 bits per byte and overrelaxation at 1.5 ([[salakhutdinov-2003-overrelaxed-bound-optimization]]) a further 0.004, about a 1.2-fold speedup that closes a sixth of the gap. Extrapolation ([[varadhan-2008-squarem]]) was not tried.

## Exponential links

With $G=e^{L}$ (stage C, $d=32$) the chart cost 0.039 bits per byte for the local rule (natural-gradient step through $\operatorname{Dexp}_L$ with a trust radius and backtracking) and 0.018 for backpropagation through `matrix_exp`. The backpropagation transitions in the free chart have near-zero determinants, isolated negative real eigenvalues and in one seed a negative determinant, so they have no real logarithm ([[culver-1966-existence]]) and the chart can approach them only from inside its image. A frozen spectral norm in the local exp run suggests its guarded step stopped being accepted; acceptance was not recorded.

A read-only check of the trained $K=192$ transformer `D:/DATA_KEEP/25.12_wikitext-103_K192_block_glk_mlp_s6` (exponential content chart, eight layers) shows a different pattern: generator real parts down to $-14.4$, link condition numbers $2.8\times10^{3}$ to $1.2\times10^{7}$, 16, 12 and 6 near-annihilated directions in layers 0 to 2, and no eigenvalue near the negative real axis. The loss cost of the chart in that model is unmeasured; a matched `content_link_chart='affine'` run is pending on the user's side.

## What is not established

The ratio declines with d (successive drops 0.037, 0.041, 0.019 per doubling), and the data cannot separate a leveling ratio from a widening gap. The result concerns one linear model under one filter. It says nothing about nonlinear latent dynamics, the GL(K) attention architecture, or competitive perplexity, and the schedule and backpropagation learning rate were tuned on synthetic data with one seed. Two follow-ups are recorded in `VFE_3.0/TODO.md`. The first is a switching linear-Gaussian stage with a Gaussian-sum or expectation-correction smoother ([[ghahramani-2000-switching-state-space]], [[barber-2006-expectation-correction]]), the first test in which the local rule must work through a mixture approximation. The second is a $d=128$ point on the ratio's trend.

## Relevance to this research

This is the first executed evidence on the backprop-free half of the [[VFE Transformer Program]]: on a declared normalized sequence model, a learner using only posterior statistics reaches about nine tenths of backpropagation's held-out gain and shares its optimum. It does not yet bear on the transformer, whose links, memory and routing are nonlinear. See [[Variational EM]] and [[Inference machinery — variational EM and filtering]].
