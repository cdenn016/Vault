---
type: run
title: "MultiAgentELBO pointwise Gaussian network baseline, September 30, 2026"
aliases: ["Pointwise held-link Gaussian network baseline September 2026"]
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/cs-ml, field/statistics, field/physics]
year: 2026
created: 2026-09-30
---

# Pointwise Gaussian network baseline

> [!info] Citation
> MultiAgentELBO project (2026). *Pointwise Gaussian network implementation: September 30, 2026*. Repository implementation and retained CPU evidence, published in [PR #99](https://github.com/cdenn016/MultiAgentELBO/pull/99), merge revision `73d004df079e1f6d414622d1f8da15c476245a1f`. [Implementation and results at that revision](https://github.com/cdenn016/MultiAgentELBO/blob/73d004df079e1f6d414622d1f8da15c476245a1f/docs/reviews/2026-09-30-codebase-next-phase/IMPLEMENTATION.md).

## Summary

The first tensor implementation of the complete held-link Gaussian action and coordinate Schur parents at $c_*$ passed ten tiny CPU tests and, in one 512-agent study, all 45 numerical comparisons across five structural-map cases. The largest absolute parity residual was $9.094947017729282\times10^{-13}$ at `atol=rtol=1e-9`. The measured study duration was 3.288605500012636 seconds including artifact writing/compression and excluding interpreter/import startup. These are finite conditional-law and implementation results. No latent-link mixture closure, intrinsic formation, autonomous parent, large-network path simulation, GPU comparison, or thermodynamic-limit result was established.

## Problem and setting

Each directed observed record has residual $A_e x_i-B_e x_j-o_e$, SPD real precision $\Gamma_e^{-1}$, and its full normalized Gaussian likelihood. Independent proper node priors supply SPD precisions $J_{0,i}$ and means $\mu_{0,i}$. The graph, source assignments, structural maps, comparison maps, record precisions, and observed records are held; only real node coordinates are integrated. Rectangular and rank-deficient comparison maps are admitted with proper priors and SPD record noise. Integrating random maps would be another operation and need not leave a Gaussian law.

The implementation follows the canonical manuscript's complete-action and reverse-conditional construction in `manuscripts/MultiAgentELBO_Theory/g07_coarse_maps.tex`, section `sec:cg-kron-normalized-action`, proposition `prop:cg-normalized-schur-action`. It extends the runtime integration, rather than proposing a new Gaussian decimation theorem. The existing nonflat series-class theory retains its own scope. Prior context is [[multiagentelbo-2026-09-11-gaussian-closure]]; projected memory is distinguished from static closure in Chapter 11, `c11_network_coarsegraining.tex`.

## Method

The complete real energy is
$$
E(x)=\frac12 x^T Jx-h^Tx+c.
$$
The proper-prior and record-likelihood constants are retained in $c$, so the raw mass of $\exp(-E)$ is the observed-record evidence. This energy offset is the negative of the existing exact `GaussianInfo` oracle's positive log coefficient. Endpoint Gram blocks, information terms, and scalar contributions are assembled without discarding generated cross interactions.

For ordered retained coordinates $r$ and hidden coordinates $h$, the parent retains
$$
J_c=J_{rr}-J_{rh}J_{hh}^{-1}J_{hr},\qquad
h_c=h_r-J_{rh}J_{hh}^{-1}h_h,
$$
$$
c_c=c+\frac12\left[\log\det J_{hh}-d_h\log(2\pi)-h_h^T J_{hh}^{-1}h_h\right].
$$
Its equilibrium reverse conditional has gain $-J_{hh}^{-1}J_{hr}$, intercept $J_{hh}^{-1}h_h$, and covariance $J_{hh}^{-1}$. The lift reconstructs fine moments using this conditional in the original coordinate order. It does not recover an arbitrary nonequilibrium hidden conditional from retained moments alone.

Complex maps are explicitly realified with real coordinates followed by imaginary coordinates within each node. Circular complex priors of the form $\exp[-(z-\mu)^*H(z-\mu)]$ use real precision $2R(H)$. The complex-case record likelihoods follow the declared normalized real Gaussian convention; no latent Haar prior or noncompact-link prior is introduced.

## Executed evidence

The grounding packet reports ten tests, zero failures, zero errors, and zero skips in 1.571 seconds (`green.xml`). Tiny CPU tensors are compared with exact rational or independent numerical oracles for complete normalization, observed records, ordered Schur reduction, staged composition, reverse recovery, generated cross blocks, rectangular rank-deficient records, passive GL frame changes, finite-difference map gradients, complex realification, and stationary memory. The expected pre-implementation missing-module failure remains in the repository's `red.xml`; it is not counted as a passing test.

The standalone study used seed 20260930, link scale 0.2, float64 CPU tensors, and one torch thread. Its graph has 512 nodes and 1,024 directed records: a cycle plus stride-17 chords. Every fourth node was retained, giving 128 retained nodes. This supplied coordinate selection is a benchmark grouping and does not assert intrinsic formation. Real cases share priors and means, and the complex cases share theirs; rectangular and full-map record dimensions differ, so their evidence values do not rank model quality.

| Held-map case | Fine to retained real dimensions | Case compute seconds | Largest absolute parity residual | Conditional drift-variance Frobenius norm |
| --- | --- | --- | --- | --- |
| Flat GL+(2,R) frames | 1024 to 256 | 0.215 | 4.55e-13 | 2.086 |
| Independent GL+(2,R) maps | 1024 to 256 | 0.187 | 3.55e-15 | 1.862 |
| Rank-one matrix communication with distinct rectangular receiver/source maps | 1024 to 256 | 0.201 | 4.55e-13 | 0.546 |
| Realified GL(2,C) maps | 2048 to 512 | 1.158 | 9.09e-13 | 1.278 |
| Realified SU(2) maps | 2048 to 512 | 1.106 | 3.55e-15 | 1.100 |

Each case passed nine comparisons: fine/direct and fine/staged evidence mass; selected means and covariances; direct/staged $J$, $h$, and $c$; and fine mean/covariance recovery through the reverse conditional. These are measured parity residuals for generated instances, not universal bounds for ill-conditioned inputs. Per-case timings precede compression. There was one study invocation and no repeated timing estimate. The dense precision alone occupies 8 MiB for real cases and 32 MiB for realified cases; multiple covariance and elimination buffers coexist and peak memory was not measured. Dense storage is $O(d^2)$ and generic factorization is $O(d^3)$.

The runtime was `C:/anaconda/python.exe`, CPython 3.12.7, torch `2.10.0.dev20251210+cu128`, Windows 10. CUDA was visible but this execution used CPU while the GPU was occupied; the increment required no GPU. Unit-test thread environment variables were `OMP_NUM_THREADS=MKL_NUM_THREADS=OPENBLAS_NUM_THREADS=1`. The test and study commands are recorded in the archived report and JSON. No full suite, historical heavy replay, Lean work, or new literature search ran.

## Dynamical boundary

The parent exposes a separately specified held stationary example,
$$
dX=-(JX-h)dt+\sqrt{2}dW,
$$
with identity mobility and stationary microscopic preparation. Its selected lag covariance comes from $\exp(-Jt)J^{-1}$; its memory kernel is $J_{rh}\exp(-J_{hh}t)J_{hr}$; and its conditional drift-variance tensor is $J_{rh}J_{hh}^{-1}J_{hr}$. The kernel alone omits the hidden initial residual and colored forcing needed for a complete projected equation. Tiny checks compare stationary lag covariance and memory with a SciPy oracle and distinguish the projected process from an OU process chosen from the Schur marginal.

The 512-agent study evaluated only the drift-variance tensor. Its nonzero values show hidden coupling in this stated coordinate process. No large-network path or nonstationary activation comparison was executed, and no gauge-covariant kinetic model or switching-link parent approximation was certified. The current formation results, including [[multiagentelbo-2026-09-28-early-parent]], retain their separate assumptions and finite grounding scopes.

## Relevance to this research

This increment supplies a declared 512-agent runtime bridge for [[Coarse Graining]] in the [[Gauge-Theoretic Multi-Agent VFE Model]], across nonabelian and noncompact held maps and rectangular communication. Complete actions and equilibrium reverse kernels can now be reused while keeping the open dynamical obligation explicit: declare an evolving pointwise model, retained source/link histories, actual activation law, mobility, discarded conditional information, and prediction horizon. [[Staged hierarchy formation and RG composability]] distinguishes exact static composition from that inherited parent comparison; [[Soft formation and the activation clock]] preserves the activation-law context. General soft/recursive formation and the thermodynamic limit remain open, and base transport remains outside the current phase.

## Archive and publication context

The compact immutable archive is `sources/archives/multiagentelbo-2026-09-30-pointwise-gaussian-network/`: final published `IMPLEMENTATION.txt`, `checks.json`, `baseline-result.json`, `green.xml`, and source snapshots `network.py`, `network_experiment.py`, `gaussian_network.py`, and `test_gaussian_network.py`. The original complete case inputs and fine/parent arrays remain local in MultiAgentELBO `artifacts/pointwise-gaussian-network/20260930T164301694258Z/`; large NPZ files were not copied into the vault.

The tests and study were executed on the new implementation before publication from base revision `cc6645b1163d08697313bcd3de750c761ecfcaf1`. The code was later published through feature commit `d47159e03bae92781f1ff924bfe62979ab64d25b` and merge `73d004df079e1f6d414622d1f8da15c476245a1f`. Publication changed trailing whitespace and status wording, with no executable statement change or new science run. The merge revision locates the published implementation; it does not turn the retained execution into a fresh clean-revision calculation.

## Cross-links

[[Coarse Graining]], [[Staged hierarchy formation and RG composability]], [[Gauge-Theoretic Multi-Agent VFE Model]], [[Soft formation and the activation clock]], [[multiagentelbo-2026-09-11-gaussian-closure]], [[multiagentelbo-2026-09-28-early-parent]].

## BibTeX

```bibtex
@misc{MultiAgentELBO2026PointwiseGaussianNetwork,
  author = {{MultiAgentELBO project}},
  title = {Pointwise Gaussian Network Implementation: September 30, 2026},
  year = {2026},
  howpublished = {Repository implementation and retained CPU evidence},
  url = {https://github.com/cdenn016/MultiAgentELBO/blob/73d004df079e1f6d414622d1f8da15c476245a1f/docs/reviews/2026-09-30-codebase-next-phase/IMPLEMENTATION.md},
  note = {Conditional held-link Gaussian laws at one base point; one five-case 512-agent CPU study}
}
```
