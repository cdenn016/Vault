---
type: run
title: "VFE_3.0 paper arms at K = 128, one epoch of WikiText-103, October 25 to 26, 2026"
aliases: ["vfe3 paper arms October 2026", "Paper arms October 2026"]
tags: [cluster/attention, cluster/gauge-theory, project/transformer, field/cs-ml, field/statistics]
year: 2026
created: 2026-10-27
---

# VFE_3.0 paper arms at K = 128, one epoch of WikiText-103, October 25 to 26, 2026

> [!info] Scope
> Ingested at the user's explicit request (rule 0): the results of the registered main-results comparison for the VFE transformer, run on October 25 and 26, 2026. Repository references are deliberately left out. Eleven arms at three seed pairs, 33 runs, all completed on one RTX 5090.

## Setup

The base model is the gaussian_diagonal family with learned per-type $GL(K)$ frames, $K=128$, four heads, six layers, the ALiBi distance prior ([[press2022-alibi]]) without rotary encoding, an attention residual, a coordinate block MLP, a chunked diagonal decoder and no decay on the stored covariance. Every arm is a declared change of that configuration, trained for 15,000 steps of 32 sequences of 256 tokens (122.9M tokens, about 1.05 epochs), with 250 warmup steps and cosine decay to zero. The seed pairs (model seed, data seed) are (6, 3), (23, 23) and (54, 54). Statistics are test cross-entropy at the best-validation checkpoint, paired by seed pair, with 95% Student-t intervals on two degrees of freedom.

The registered decision rule sets a margin of $\max(2\,\mathrm{SE}, 0.03)$ nats on the paired test CE difference. The frame claim stands if (a) the per-type read-table comparator exceeds the evaluated arm by more than the margin, (b) freezing the frames costs at least the margin, and (c) an identity-frame model given a per-type additive table of the frame table's size exceeds the evaluated arm by more than the margin.

## Results

| arm | test PPL (mean ± SD) | paired test CE minus evaluated (nats) | 95% interval | parameters |
|---|---|---|---|---|
| Evaluated: learned frames | 35.16 ± 0.18 | 0 | | 233.6M |
| Covariance-blind routing (mean distance) | 35.23 ± 0.31 | +0.002 | [−0.010, +0.015] | 233.6M |
| Identity frames, per-type additive table of equal size | 41.00 ± 0.18 | +0.154 | [+0.142, +0.166] | 233.6M trainable |
| Frames frozen at random initialization | 43.24 ± 0.13 | +0.207 | [+0.190, +0.224] | 27.7M trainable |
| Identity frames | 43.47 ± 0.39 | +0.212 | [+0.178, +0.247] | 27.7M trainable |
| Conventional transformer, matched total parameters (width 1024) | 29.96 ± 0.04 | −0.160 | [−0.171, −0.149] | 228.9M |
| Conventional transformer, matched context-processing parameters | 57.99 ± 0.54 | +0.500 | [+0.482, +0.519] | 14.9M |
| Per-type read table, ALiBi (as run) | 50.43 ± 0.17 | +0.361 | [+0.346, +0.375] | 220.7M |
| Per-type read table, ALiBi, the VFE model's optimizer | 39.61 ± 0.26 | +0.119 | [+0.091, +0.147] | 220.7M |
| Per-type read-and-write table, ALiBi | 50.03 ± 0.16 | +0.353 | [+0.336, +0.370] | 220.7M |
| Per-type read table, ALiBi, shared post-norm | 50.96 ± 0.08 | +0.371 | [+0.362, +0.380] | 220.7M |

The decision rule returns **stands**: (a) +0.361 nats, (b) +0.207, (c) +0.154, each against the 0.03-nat floor (2 SE is below it in every clause).

## Reading

Learned frames carry the advantage over the frame-free variants. Removing them costs 0.212 nats; random frozen frames recover 0.005 of that, and the equal-size additive table recovers 0.058, about 27%. The additive-capacity explanation fails. A per-type multiplicative map without gauge structure, acting where the frames act, is untested and is the nearest remaining capacity alternative.

The conventional transformer with matched total parameters beats the VFE model by 0.160 nats. It spends about 126M parameters on context processing against the VFE model's 2.0M, trains in 39 minutes against 83, and ran with an untuned hidden-matrix learning rate (the base peak rate 0.003 scaled by 128/1024). Changing only the read-table comparator's optimizer to the VFE model's (Adam $\beta_2=0.999$ instead of 0.95 ([[kingma-ba-2015-adam]]), no decay on matrices, decay 0.1 on the table) moves it from 50.43 to 39.61 PPL, so 0.119 nats, not 0.361, is the defensible size of the frame model's advantage over the read table. Mean-distance routing matches Gaussian-KL routing at 61% of the wall time; at this operating point the routing cost reads nothing measurable from the covariance, though the decoder still does.

## Training trajectories per step

Differences are seed-mean arm CE minus evaluated CE at the same step (positive: the VFE model ahead). Train CE is the mean over each 500-step logging window; validation runs every 3,000 steps. All arms share batch, warmup and schedule, so steps are tokens.

| arm | train, 500 | 1000 | 2000 | 3000 | 6000 | 9000 | 12000 | 15000 |
|---|---|---|---|---|---|---|---|---|
| Matched total parameters | −0.064 | +0.153 | +0.115 | +0.083 | +0.011 | −0.025 | −0.078 | −0.099 |
| Read table, VFE optimizer | +0.163 | +0.250 | +0.156 | +0.109 | +0.069 | +0.082 | +0.103 | +0.136 |
| Read table, as run | +0.225 | +0.401 | +0.382 | +0.382 | +0.410 | +0.419 | +0.397 | +0.447 |
| Frozen frames | +0.139 | +0.131 | +0.139 | +0.148 | +0.179 | +0.194 | +0.216 | +0.294 |
| Identity frames, capacity table | +0.123 | +0.116 | +0.113 | +0.117 | +0.134 | +0.143 | +0.162 | +0.227 |
| Mean distance | −0.025 | +0.040 | +0.034 | +0.031 | +0.027 | +0.026 | +0.024 | +0.032 |

| arm | val, 3000 | 6000 | 9000 | 12000 | 15000 |
|---|---|---|---|---|---|
| Matched total parameters | +0.044 | −0.034 | −0.077 | −0.131 | −0.160 |
| Read table, VFE optimizer | +0.093 | +0.066 | +0.082 | +0.103 | +0.113 |
| Frozen frames | +0.145 | +0.179 | +0.189 | +0.206 | +0.212 |

Per step, the VFE model learns faster early than every conventional arm. Its lead over the matched-total transformer peaks at 0.153 nats of train CE at step 1,000; the validation curves cross near step 4,700 and the train curves near step 7,000, after which the transformer gains about 0.04 nats per 3,000 steps. The early lead is confounded with that arm's low, untuned hidden-matrix rate (3.75e-4 at width 1024), so it is not evidence of higher sample efficiency than a tuned transformer. The frame arms behave the other way: their gap is 0.12 to 0.14 nats from step 500 and grows through training. In the last interval the evaluated arm's train CE is 0.056 below its validation CE while the frozen-frame arm's is 0.026 above, so part of the learned frames' late train advantage does not transfer to held-out text.

## What is not established

One operating point: $K=128$, six layers, one epoch. A longer K = 192, eight-layer run with rotary encoding operates in a memorization regime that one epoch excludes, and the frame and capacity tables here train about one-eighth as long per type. An earlier one-epoch sweep on an eight-layer configuration with rotary encoding gave a similar capacity gap (+0.165 nats in validation CE). Three seeds give paired SEs of 0.003 to 0.008 nats. The conventional baselines' learning rates were not tuned.

## Relevance to this research

This is the registered test of the [[VFE Transformer Program]]'s frame claim: learned per-type $GL(K)$ frames beat frame-free per-type tables, random frames and an equal-size additive table, so the advantage is attributable to learned frame structure and not to raw capacity. It also bounds the program's broader claim: at equal total parameters a conventional transformer ([[vaswani-2017-attention]]) is better after the first third of training at this operating point. See [[Gauge equivariance and geometric deep learning]] and [[Attention mechanisms — theory and positional structure]].
