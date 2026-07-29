---
type: run
title: "Exact congruence versus diagonal truncation: two covariance families and a negative result (2026-07-25)"
aliases:
  - "exact congruence negative result"
  - "gaussian_diagonal_exact"
  - "gaussian_frame_diagonal"
  - "2026-07-25 covariance family runs"
tags:
  - cluster/spd-geometry
  - cluster/gauge-theory
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - field/mathematics
  - field/cs-ml
created: 2026-07-25
updated: 2026-07-25
---

# Exact congruence versus diagonal truncation: two covariance families and a negative result (2026-07-25)

> [!info] Provenance and evidence boundary
> Repository `V3_Transformer` at `4686082`, clean worktree. Training arms are single-seed
> (seed 6), $K=20$, `block_glk`, 15,000 planned steps on WikiText-103, against the baseline
> `vfe3_runs/ablations_single_seed/138.40_mstep-phi-norm=5` at validation PPL 139.3. Energy
> statistics were measured on that same trained state at `kl_max=160`, one sequence, unclamped, and
> off-diagonal pairs only. Timing figures are four timed steps after two warmup steps on an
> RTX 5090 under `C:/anaconda/python.exe`. Correctness pins are float64 unit tests. The
> implementation record is `V3_Transformer/docs/2026-07-25-edits.md`.

## The two families

`gaussian_diagonal`, the program's live family, declares the covariance diagonal in a fixed ambient
basis. That family is not closed under a general $\mathrm{GL}(K)$ congruence, so
`transport_covariance` pushes the key forward and truncates
$\Omega\,\mathrm{diag}(s_j)\,\Omega^\top$ to its diagonal. Two variants were built to remove that
truncation in different directions, both registered behind the family registry and both default OFF.

`gaussian_frame_diagonal` declares the covariance diagonal in the agent's own fiber frame,
$\Sigma_i=U_i\,\mathrm{diag}(\sigma_i)\,U_i^\top$, which **is** closed under $\mathrm{GL}(K)$.
`gaussian_diagonal_exact` keeps the same distribution family and computes the coupling energy
exactly, by pulling the query back rather than pushing the key forward. Because a divergence is
invariant under a common invertible pushforward,

$$
\mathrm{KL}\big(\mathcal N(\mu_i,\mathrm{diag}\,s_i)\,\big\Vert\,\mathcal N(\Omega\mu_j,\Omega\,\mathrm{diag}(s_j)\,\Omega^\top)\big)
=\mathrm{KL}\big(\mathcal N(\Omega^{-1}\mu_i,\Omega^{-1}\mathrm{diag}(s_i)\Omega^{-\top})\,\big\Vert\,\mathcal N(\mu_j,\mathrm{diag}\,s_j)\big),
$$

which leaves the second argument exactly diagonal and needs the first only through its diagonal and
its determinant. Under the flat Regime-I cocycle $\Omega_{ij}=U_iU_j^{-1}$ the inverse is the pair
transpose, $\Omega_{ij}^{-1}=\Omega_{ji}$, so the fast route reuses every existing transport kernel
verbatim and $\log\lvert\det\Omega_{ij}\rvert=\ell_i-\ell_j$ needs only per-vertex block
log-determinants. A dense reference route inverts explicitly and assumes nothing about the
connection. Anything the identity does not cover — Regime II, direct links, RoPE-wrapped transport,
an uncertified factored cocycle, unequal transport blocks, or a non-KL divergence — raises rather
than silently falling back to the truncated energy.

The implementation is correct. Against a dense reference the exact energy agrees to about
$3\times10^{-13}$ per pair and per irrep block, where the truncated form is off by more than 80 nats
at $\mathrm{cond}(U)\approx200$; the factored, compact and dense routes agree to
$5\times10^{-13}$; self-pairs are exactly zero, which the softmax and the saturation mask depend on;
and at $\Omega=I$ the two families coincide exactly. The cost is about 3% over `mm_exact` and 13%
over the gradient baseline at the live training shape, since the transpose route adds only one
log-determinant per vertex block.

## Both arms are much worse

| arm | validation PPL | `guard_energy_klmax_frac` | `self_divergence` | `vertex_cond_median` |
|---|---|---|---|---|
| `gaussian_diagonal` (baseline) | **139.3** | **0.0000** | 0.008 | 47.3 |
| `gaussian_frame_diagonal` | 308.1 | 0.894 | 4.8 | 1.65 ($\phi$ frozen) |
| `gaussian_diagonal_exact` | abandoned; train PPL 432 at step 7,900 | **0.979** | 415 | 24.4 |

The frame-intrinsic family fails for a clean structural reason, verified rather than assumed. Under
the Regime-I coboundary the sender frame cancels from the congruence and the receiver frame from the
location, so the pair energy depends only on $(a_i,\sigma_i,a_j,\sigma_j)$ with $a=U^{-1}\mu$. The
gauge leaves the belief coupling entirely, which shows up end to end as `phi_embed.grad is None` —
under this family the 452M-parameter gauge table receives no gradient at all under any estimator.
It is therefore an ablation of whether the gauge earns its keep, not a candidate improvement, and
the answer it returns (139.3 to 308.1 with $\phi$ disconnected) is a measurement worth keeping.

## Why exactness fails: the energy scale

The exact arm never recovers. Training perplexity bottoms near 543 at step 2,000, rises to 622 by
step 3,300, and is still 432 at step 7,900 against the baseline's 147 train and 139 validation,
while `self_divergence` runs 11 to 213 to 402 to 415 and the median belief condition number goes
from 2.5 to 24 over the same span. Measured on the same trained state, with vertex $\mathrm{cond}(U)$
median 11.6, p99 79.8, and maximum 108.9:

| energy $E_{ij}$ (nats) | median | p90 | p99 | max | fraction $\geq k_\text{max}$ |
|---|---|---|---|---|---|
| truncated (`gaussian_diagonal`) | 5.65 | 13.79 | 21.75 | 58.9 | 0.0000 |
| exact (`gaussian_diagonal_exact`) | 34.10 | 326.72 | 1882.89 | **10912.2** | 0.1894 |

The exact-to-truncated ratio is 7.2 at the median, 66.9 at p90, 426 at p99, and 4604 at the maximum.
For the exact energy not to clamp on a state the baseline runs at exactly zero saturation,
$k_\text{max}$ would have to exceed about 10,900 rather than 160.

The mechanism is a difference of kind, not degree. The truncated key covariance
$[\mathrm{diag}(\Omega\,\mathrm{diag}(s_j)\Omega^\top)]_k=\sum_l\Omega_{kl}^2 s_{jl}$ is a sum of
squares: always inflated, never near-singular. The exact
$\Omega\,\mathrm{diag}(s_j)\,\Omega^\top$ **is** near-singular along the contracted directions of an
ill-conditioned $\Omega$, and KL against a near-singular covariance grows like
$\mathrm{cond}(\Omega)^2$ through its trace term. The observed maximum bears that out to within 10%:
$\mathrm{cond}_{\max}=108.9$ gives $\mathrm{cond}_{\max}^2=11858$ against an observed maximum energy
of 10912.

The runaway that follows is self-reinforcing. Above $k_\text{max}$ the clamp emits a constant whose
derivative is zero, and the pair mask `(energy > 0) & (energy < kl_max)` then zeroes the pair
derivative, removing the one term that would push $\phi$ back toward well-conditioned frames.
Saturation runs 0.06 to 0.15 to 0.20 to 0.80 to 0.97 to 0.979 over 7,900 steps, with attention
entropy washing back out toward uniform (2.48 to 1.27 to 2.41) as the grid flattens onto the clamp.
The baseline holds that metric at exactly 0.0000 for all 15,000 steps. This is a distinct and
sharper instance of [[Divergence clamp saturation]] than the 2026-06-21 hyper-prior case: there a
saturated regularizer went silently inert, whereas here the saturated term is the one whose gradient
maintains the conditioning that keeps it below the ceiling.

## Reading

The diagonal truncation is not an approximation error to be removed; it is the regularizer that
makes a genuinely non-compact $\mathrm{GL}(K)$ gauge usable — see
[[Diagonal truncation as gauge regularization]] for the general statement. The exact congruence
energy and an ill-conditioned $\mathrm{GL}(K)$ frame are in direct tension: the exact form is tame
only when $\Omega$ is near-orthogonal, and precisely there the truncation error it removes is
negligible, so the two paths coincide and there is nothing to win. That tension is the finding. The
implementation is correct to $3\times10^{-13}$; the model simply cannot run on the energy it
computes at this conditioning.

Both toggles stay default OFF and are retained as measurement instruments. The exact family
quantifies how much divergence mass the truncated attention score discards (a factor of 7 at the
median, 426 at p99), and the frame family quantifies what the gauge channel is worth.

## Incidental engineering findings

`torch.linalg` rejects bfloat16 and float16 outright, so the first live run under `amp_dtype='bf16'`
crashed in the model channel's gamma coupling, which runs at the caller's autocast dtype while the
oracle and hand kernels have their own float32 islands. The log-determinant and dense inverse are
now promoted to float32 and the determinant is *returned* at float32 rather than cast back, because
it enters the energy additively and a bfloat16 evaluation would be wrong rather than merely rounded.

Separately, the float32 congruence guard in `geometry/transport.py` fires during ordinary evaluation
of the $K=300$ baseline (`diagonal congruence lost nonnegativity, min=-329.324`), which
independently supports the concern that the diagonal covariance family is poorly conditioned under
the untied block gauge.

## Relevance to this research

The result settles a recurring question in the [[VFE Transformer Program]] about whether the
diagonal projection in `transport_covariance` is a defect to be repaired. It is not. More generally
it identifies a structural cost of choosing a non-compact structure group: with $\mathrm{GL}(K)$
frames free to become ill-conditioned, an exact congruence-based divergence has an unbounded
condition-number-squared tail, and something in the pipeline must bound it. Truncation is the
program's implicit answer. The alternatives — a compact or tied gauge, an explicit conditioning
penalty, or a covariance family closed under congruence — are the remaining design options, and
`gaussian_frame_diagonal` shows that the third one dissolves the gauge coupling rather than
preserving it.

## Cross-links

- Project: [[VFE Transformer Program]]
- Concept introduced here: [[Diagonal truncation as gauge regularization]]
- Companion results the same day: [[2026-07-25-estep-character-and-channel-decomposition]] ·
  [[2026-07-25-phi-table-and-beta-channel-measurements]] · [[2026-07-25-shadow-prior-refutation]]
- Theory: [[Divergence clamp saturation]] · [[GL(K) gauge group]] ·
  [[GL(K) gauge-equivariant attention]] · [[Symmetric spaces and the SPD cone]] ·
  [[Parallel transport]] · [[Renyi divergence]]
- Prior clamp finding: [[2026-06-21-k160-hyperprior-saturation]]
