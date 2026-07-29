---
type: run
title: "Gauge-table ablations, frame-norm calibration, and the beta channel decomposition (2026-07-25)"
aliases:
  - "2026-07-25 Stage 0 measurements"
  - "phi_embed ablation"
  - "beta decomposition M6"
  - "phi norm bound calibration"
tags:
  - cluster/gauge-theory
  - cluster/attention
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/mathematics
created: 2026-07-25
updated: 2026-07-25
---

# Gauge-table ablations, frame-norm calibration, and the beta channel decomposition (2026-07-25)

> [!info] Provenance and evidence boundary
> Checkpoint-only measurements; no model was trained and no checkpoint on disk was written to.
> Repository `V3_Transformer` at `4686082`, clean worktree. Interpreter `C:/anaconda/python.exe`
> (CUDA build, torch 2.10.0.dev20251210+cu128, RTX 5090). Baseline
> `data/55.41_wikitext-103_K300_block_glk_linear_mix_s6/best_model.pt`, scored on the full
> WikiText-103 test split (137 batches of $16\times128$). Every ablation is an in-memory mutation of
> a GPU copy of the weights, with `phi_embed` restored from a pristine clone and verified to
> reproduce the baseline exactly. The write-up of record is
> `V3_Transformer/docs/2026-07-25-phi-bound-calibration-and-stage0-report.md`.
>
> **Baseline restatement.** The checkpoint rebuilds under current HEAD at 498,747,258 parameters
> against the recorded 528,901,458, a difference of exactly 30,154,200, and `load_state_dict`
> reports all keys matched after `normalize_legacy_model_state` drops `prior_bank.mu_embed` and
> `prior_bank.sigma_log_embed` — byte-exact confirmation that those two tables were inert during the
> run. Rescored under current HEAD the same weights give CE 4.012327 / PPL 55.275 against the
> recorded 4.014838 / 55.414, the 0.0025-nat difference coming from fixes landed 2026-07-20. Every
> comparison below uses 4.012327 as the baseline.

## The gauge table is load-bearing, precision-redundant, and rank-saturated

`phi_embed` holds 452,313,000 parameters, 85.5% of the run's total, and an agent sweep had proposed
that it might be decorative.

| variant | CE | PPL | $\Delta$CE |
|---|---|---|---|
| baseline | 4.012327 | 55.275 | — |
| $\phi:=0$ (identity gauge) | 5.928340 | 375.531 | +1.916 |
| $\phi:=$ single corpus-mean row | 5.920477 | 372.589 | +1.908 |
| $\phi:=$ 4-bit per-row quantized | 4.023128 | 55.876 | **+0.011** |
| $\phi$ restored | 4.012327 | 55.275 | 0.000 |

Zeroing the table costs 320 PPL, so it is not decorative. Mean-collapse costs the same as zeroing,
which localizes the value in the per-token variation rather than the overall gauge level — expected,
since a globally constant frame is close to a no-op under equivariance. But 4-bit per-row
quantization costs only 0.6 PPL, so the table tolerates an eightfold precision reduction essentially
for free and carries on the order of four useful bits per parameter against thirty-two stored.

Whether that redundancy is dimensional was tested independently by exact truncated SVD via the Gram
matrix, $\phi_r=(\phi V_r)V_r^\top$. The spectrum has no knee: it takes rank 2,486 of 9,000 to
capture half the Frobenius energy, 6,760 for 90%, and 8,681 for 99%, with leading singular values
192.3, 153.9, 108.2, 99.8 decaying smoothly. Scored, rank 4,096 (a 45% parameter saving) still costs
7.09 PPL, rank 2,048 costs 26.4, rank 1,024 costs 54.6, and every smaller rank is catastrophic
(rank 16 gives PPL 289).

The characterization is therefore precise: `phi_embed` is **highly redundant in precision and
saturated in rank**. Roughly four bits per parameter suffice, but all 9,000 directions carry signal.
This settles the gauge re-budgeting question against every factorization proposal, since a low-rank
$\phi_\text{embed}=CB$ would have to keep essentially full rank to preserve quality, at which point
it costs more parameters than the dense table. It also argues against `gauge_group='tied_block_glk'`
($n_\text{gen}=900$) as a free win: a tenfold dimensional cut on a table already using its
dimensions is a substantial capacity reduction to be paid for elsewhere, not recovered slack. If the
footprint must come down, reduced storage precision is the supported route.

## The beta channel decomposition: attention is mostly positional

$\beta_{ij}=\mathrm{softmax}_j(\log\pi_{ij}-E_{ij}/\tau)$. Under this configuration $\log\pi$
carries three things — the `causal_alibi_noself` positional prior, a detached precision bias, and
(because `gamma_as_beta_prior=True` with `lambda_gamma=0.75`) a detached fold of the model-channel
gamma posterior — while $E_{ij}$ is the belief-coupling energy, the only content-dependent channel.
With `e_step_update='mm_exact'` and `e_phi_lr=0` the only $\beta$ softmax on the evaluation path is
`gradients/kernels.py::mm_exact_update`, so patching its module-level `attention_weights` binding
isolates the belief $\beta$ exactly and leaves the gamma weights untouched.

| arm | $\beta$ | CE | PPL | $\Delta$CE (nats) |
|---|---|---|---|---|
| A full (as trained) | $\mathrm{softmax}(\log\pi-E/\tau)$ | 4.012327 | **55.275** | — |
| B energy ablated | $\mathrm{softmax}(\log\pi)$ | 4.222406 | 68.197 | +0.210 |
| C prior flattened | $\mathrm{softmax}(-E/\tau)$ on the causal/no-self support | 4.624550 | 101.957 | +0.612 |
| D gamma fold removed | $\log\pi$ without the gamma term | 4.015244 | 55.437 | +0.0029 |
| E gamma removed and energy ablated | ALiBi plus precision only | 4.279532 | 72.207 | +0.267 |

Arm A reproduces the baseline to every digit, which validates the harness. The positional prior
carries roughly three times what the content channel does: flattening $\log\pi$ costs 0.612 nats
while ablating the entire belief-coupling energy costs 0.210. The content-dependent part of
attention is worth about 12.5% of what context is worth in total and about 5% of the model's
cross-entropy. The gamma fold into $\beta$ is worth 0.0029 nats, which must not be over-read: arm D
removes only gamma's fold into $\beta$'s prior, while the model channel also sets the initial belief
through `s_e_step=True` and shaped the learned tables during training. With the energy already gone,
removing gamma costs 0.057 nats, so the two are mildly compensating rather than independent.

Read against the $\phi$ ablation, zeroing `phi_embed` costs about nine times what the whole content
channel of attention is worth. The gauge earns its keep mainly through the **value** path,
transporting $\mu_j$ into the query frame, not through the attention scores it also feeds.
Functionally the model is an ALiBi-weighted average of gauge-transported values with a modest
content-dependent reweighting on top.

Why the content channel is weak connects to the E-step's structure. `free_energy()`'s
`log_likelihood` argument is a gated stub with no production caller, so the E-step descends
$\alpha\mathrm{KL}(q\Vert p)+\sum_j\beta\,\mathrm{KL}(q\Vert\Omega q)+\text{entropy}$ with no data
term. $E_{ij}$ is therefore a measure of belief *agreement*, not of predictive relevance, and
nothing in the objective asks it to be discriminative for the next token. This is the same
target-blind E-step already recorded in [[2026-06-29-sigma-gate-fail-and-collapse]], seen from the
attention side.

## Context use saturates near 32 tokens

| context tokens available | CE |
|---|---|
| 0 | 5.599 |
| 1 | 4.982 |
| 2–3 | 4.713 |
| 4–7 | 4.417 |
| 8–15 | 4.151 |
| 16–31 | 4.033 |
| 32–63 | 3.959 |
| 64–127 | 3.929 |

Context is worth 1.68 nats from position 0 to position 127, which refutes a prior reading — taken
from the logged `pos_loss_ratio = 0.9796` — that the model barely uses context. That summary was an
artifact of comparing quartile means, since the first quartile is dominated by positions 16 to 31
which are already near-converged; computing the same ratio directly from this curve gives 0.9282.
The discrepancy with the logged metric could not be reconciled from the artifacts, and the direct
measurement is the one to trust. The operational conclusion survives for a different reason: the
model extracts 1.57 of the 1.68 nats within the first 32 tokens and then saturates, with a marginal
gain of only 0.030 nats from the 32–63 band to the 64–127 band. Extending the context window from
128 to 512 should be expected to buy very little.

## Two tuning claims refuted, and the frame-norm bound calibrated

An eight-point sweep of the attention temperature $\tau=\kappa_\beta\sqrt{30}$ found the shipped
$\kappa_\beta=1.0$ to be the measured minimum, with the proposed move toward the ELBO-exact
$\tau=1$ monotonically worse (+0.0266 nats at $\kappa_\beta=0.1826$) and the curve flat within about
$\pm0.5$ in $\kappa_\beta$. Local optimality is partly circular because the weights were trained at
that value, but the advertised free win does not exist, and the flatness argues against the
"starved for content signal" reading.

The transport Frobenius clamp had been identified as the run's largest defect on the grounds that
above threshold the code returns $\exp(20M/\lVert M\rVert_F)$ rather than $\exp(M)$. That statement
about the operator is true, but the performance conclusion drawn from it was wrong: at
`TRANSPORT_CLAMP_MAX_NORM` of 10 the model gives PPL 99.393, at the shipped 20 it gives 55.275, at
40 it gives 67.000, at 60 it gives 78.431, and at $10^6$ it raises `FloatingPointError` on a
nonfinite $\Omega$ before inversion. The trained weights depend on the clamp; the surrogate operator
is this model's operator, and widening it after training breaks a learned map.

That reconciles with a $K=20$ result. Bounding $\lVert\phi\rVert$ *during* training so the clamp
never has to fire is a different and evidently better intervention. Decomposing the four sibling
$K=20$ ablation runs shows that the arms named for the bound also switch the positional composition:
`bch` to `group_product` alone is +0.103 PPL (slightly worse), adding `bound=10` has exactly zero
effect (the two runs agree to twelve significant figures because the largest trained row norm at
$K=20$ is 7.399, so a bound of 10 never binds), and `bound=5` gives $-0.235$ PPL against the
`group_product` arm. The gain is attributable to the norm bound, not to the positional composition,
whose value appears to be that it makes the bound meaningful. For `block_glk` the generators are
elementary matrices orthonormal under the Frobenius inner product, so
$\lVert\sum_a\phi_aG_a\rVert_F=\lVert\phi_v\rVert_2$ exactly and the M-step projection bounds the
parameter row 2-norm directly. The bound-5 run's maximum is exactly 5.000 while its median is
unchanged (3.196 against 3.199), confirming a pure tail operation.

Porting the value 5 to $K=300$ would not reproduce the experiment. A bound of 5 clips 2.12% of live
rows at $K=20$ but 92.87% at $K=300$. Four calibration criteria — matched clip fraction (12.93),
matched ratio to median trained norm (16.12), per-block $\sqrt H$ scaling (11.18), and matched ratio
to initialization norm (33.54, discounted because the initialization norm scales as
$\phi_\text{scale}\sqrt{n_\text{gen}}$ while trained norms do not) — put the equivalent in the range
11 to 16, with 13 recommended as the primary arm and 16 as a gentler second.

**Significance caveat.** The $K=20$ arms are single-seed 15,000-step runs whose entire spread is
0.235 PPL on a base of 138.5, or 0.17%, with no seed-variance estimate. A 0.13 PPL improvement is
not established as larger than seed noise, and the mechanism is a reason to take it seriously rather
than a substitute for a multi-seed repeat.

## Dead vocabulary rows

In the $K=300$ checkpoint a set of `phi_embed` rows sits at exactly zero norm. These are token types
with zero training-corpus occurrences, driven to zero by decoupled weight decay: `pb.phi_embed[token_ids]`
produces a dense gradient, so AdamW decays all 50,257 rows every step whether or not the token
appeared, and with `phi_weight_decay=0.03` the shrinkage factor is roughly $e^{-27}$. Rows for very
low-count types sit below their random initialization. `output_proj_weight` escapes this because the
softmax gives every row a dense gradient. Exempting the Zipfian encode tables from decay is free and
independent of everything above, though the achievable gain is bounded: the rare and mid strata
together account for at most about 8% of total test cross-entropy.

## Claims that did not survive measurement

Recorded because they were ranked highly before being tested. That the transport clamp is the
largest defect and worth 1 to 4 PPL; that attention temperature is off by an order of magnitude and
moving toward $\tau=1$ is a free win; that 85% of parameters are decorative and the model barely
uses context; that `pos_phi_compose='group_product'` is the right call on its own; and that the
gauge table can be factored or its $n_\text{gen}$ shrunk to free capacity. All five were refuted.
The Baker–Campbell–Hausdorff accuracy argument that motivated the fourth is still arithmetically
correct (median relative error 0.094, maximum 0.580), which is a reminder that a correct statement
about an operator does not by itself predict the sign of a performance change.

## Relevance to this research

These measurements set the empirical boundary conditions for any redesign of the
[[VFE Transformer Program]]'s gauge and attention machinery. They establish that the
[[GL(K) gauge group|GL(K)]] frame table is genuinely load-bearing but stores its information
diffusely, that the derived divergence score contributes about a third of what a fixed positional
decay does, and that four separate "free win" hypotheses about temperature, clamping, factorization,
and positional composition are unavailable. The content-channel weakness has a single root cause
shared with the sigma collapse of [[2026-06-29-sigma-gate-fail-and-collapse]]: the E-step carries no
data term, so the energy feeding $\beta$ measures agreement rather than predictive relevance.

## Cross-links

- Project: [[VFE Transformer Program]]
- Companion results the same day: [[2026-07-25-estep-character-and-channel-decomposition]] ·
  [[2026-07-25-exact-congruence-truncation-tension]] · [[2026-07-25-shadow-prior-refutation]]
- Prior findings: [[2026-06-29-sigma-gate-fail-and-collapse]] ·
  [[2026-06-21-k160-hyperprior-saturation]] · [[2026-07-05-blocks-k48-gauge-block-scaling]]
- Theory: [[GL(K) gauge-equivariant attention]] · [[GL(K) gauge group]] ·
  [[Attention mechanisms — theory and positional structure]] · [[Relative positional encoding]] ·
  [[Baker-Campbell-Hausdorff formula]] · [[Divergence clamp saturation]]
