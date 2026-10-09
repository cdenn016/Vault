---
type: run
title: "Generated-prefix recognition conditional and relative normalizer"
aliases: ["N512 generated R2 M2 conditional relative-tilt bound"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Generated-prefix recognition conditional and relative normalizer

This intake records [MultiAgentELBO PR224](https://github.com/cdenn016/MultiAgentELBO/pull/224), source commit `47bb21d83c2a177579c23253dd9378491944b4df`, merge/frozen execution `7e68af3aaf03c9d479601f55c54eede8b4a82050`, and [PR225](https://github.com/cdenn016/MultiAgentELBO/pull/225), outcome commit `080b6cde41ec6432ab536a6f72c87256ac2d9e19`, merge `637333ce8a6b607662fcfc91db0c19c52a0d154d`. One already-generated R2/M2 retained history is conditioned under the original R1-to-R2 likelihood and joint physical Gaussian path reference. The computation bounds the relative tilt's normalization and both directed entropies. It does not integrate the nonlinear downward posterior, evaluate a full observation-density normalizer or establish an actual-history error expectation.

```bibtex
@misc{codex2026generatedprefixfilter,
  author = {Codex},
  title = {Generated-prefix recognition conditional and relative normalizer},
  year = {2026},
  howpublished = {MultiAgentELBO research records, pull requests 224 and 225},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/225}
}
```

## Causal inputs and original likelihood

[The frozen contract](https://github.com/cdenn016/MultiAgentELBO/blob/637333ce8a6b607662fcfc91db0c19c52a0d154d/docs/research/2026-10-03-latent-link-rg-plan/R3-GENERATED-PREFIX-FILTER-CONTRACT.md) selects only `depth-0-prefix-1-draw-0` from [[multiagentelbo-2026-10-09-conditional-parent-kernel]], extending known fine initialization and the first original A1/M1 constraint to the generated A2/M2 constraint at 128 parents. The law stays the unselected positive float64 raw order-nine Fisher proposal with N512, K2, 1024 original primitive reversal pairs, mass 16, h=1/40000 and T=.05. Original source support, copied primitive identities, tree, model, probe and observations stay fixed. Generated transports retain both generator-mean and precision-Cholesky probe dependence; no transport exponential is recomputed.

All 15,872 old-R1 scalar coordinates are retained: 1,536 source, 4,096 generator-mean and 10,240 generator-covariance coordinates. Only old polynomial B,b,c and structural metadata are used; archived y is excluded. New chart observations are reencoded from generated R2 in the original R1 source/generator metrics, including complete source contrast covariance and covariance-log normalization. These banks describe the completed R2 conditional likelihood given hidden x1 and retained R1. They are not force banks at the new R2 state. The complete affine Gaussian path (x1,x2) is jointly conditioned on A1x1=M1 and A2x2=M2, preserving singular physical covariance, cross-child/cross-time blocks and both original constraints without a Gaussian reset.

Generated selected hidden means, latent-mixture normals, Brownian families, future observed records and success events are not conditioning variables. Generated preceding-slice means and retained covariances/source/generator parameters are included. Numerical arrays from later-containing upstream snapshots are excluded from computation; their bytes are retained for provenance and storage accounting. Belief covariances determine original physical increment covariances, but are not substituted for the hidden conditional covariance.

## Relative tilt and sufficient conditional values

Known initialization gives p1=q1. At the generated prefix, let m be the jointly conditioned Gaussian path mean, v_r(delta)=delta^T B_r delta+(2B_rm+b_r)^T delta, r_r=y_r-f_r(m), a=sum_r r_r v_r and b=sum_r v_r^2. The exact relative tilt is exp(a-b/2), with b nonnegative and quartic. Its complete factored local representation is retained rather than a dense fourth-order tensor. The existing Gaussian cumulant bounds L1,L2 and upper B0>=E_q b give the directed entropy upper bounds L1+B0/2 and L2+B0. The fixed MGF guards pass, rho1=1.162079e-6 and rho2=2.324158e-6. No scientific accuracy threshold is attached to this one descriptive case.

| Conditional quantity | Computational sufficient value |
| --- | ---: |
| D(q path || p path), reverse | 4.743084780418287e-6 nat |
| D(p path || q path), forward | 1.433429821702882e-5 nat |
| chi-square(p path || q path) | 1.433440095357239e-5 |
| B0, upper bound on E_q b | 4.638052172462772e-6 |
| E_q a | 1.192234538220411e-8 |
| Centered log relative normalizer interval | [-2.319026086231386e-6, 2.424058694186901e-6] |
| Raw log relative normalizer interval | [-2.307103740849182e-6, 2.435981039569105e-6] |

The centered interval concerns E_q exp(a-E_q a-b/2); the raw interval concerns E_q exp(a-b/2). The raw interval shifts by the nonzero E_q a. Both omit retained-only Gaussian density constants and chart Jacobians, so neither is a full observation-density normalizer. The same scalar shift preserves the normalized posterior. The entropy values are whole-joint path quantities, with endpoint bounds by data processing, without receiver normalization. The chi-square value uses the specific likelihood second-moment bound, rather than a generic implication from KL. These computational values exclude finite-rule/degree-24 response mismatch and floating input, matrix-log, factorization, solve, contraction and bound arithmetic.

## Once-run reconstruction and replay

[The result record](https://github.com/cdenn016/MultiAgentELBO/blob/637333ce8a6b607662fcfc91db0c19c52a0d154d/docs/research/2026-10-03-latent-link-rg-plan/R3-GENERATED-PREFIX-FILTER-RESULTS.md) preserves one producer and one independent reader, with no first-outcome failure, retry, new threshold, field/response evaluation, proposal, trajectory or noise draw. Independent original-increment-factor QR reconstructs every observation row, aggregate, conditional covariance, centering shift, interval and scalar bound. All 3,106 comparisons over 30,434,663 entries pass, maximum absolute discrepancy 7.016609515630990e-14. The parent-constraint error is 2.220446049250313e-16, covariance annihilation 1.210201970840354e-21 and symmetry error zero. All 405 producer-input, 17 source and 859 reader bindings match their original/snapshot lengths and SHA256s. Six distinct pre-outcome tiny JUnit fixtures remain passing and were not rerun after scientific execution.

The producer uses 5.290211 seconds with cumulative peak 333,025,280 bytes; the reader uses 2.156641 seconds with peak 437,452,800 bytes. Fourteen numerical NPZ outputs carry 172,056,112 logical bytes and occupy 47,514,686 compressed bytes; input/source snapshots occupy 196,034,043/195,050 bytes. Full known initialization, retained/fine dependencies, uncompressed history and dense conditioning work remain charged. The canonical replay at `MultiAgentELBO/artifacts/gaussian-generated-prefix-filter/r3-n512-generated-prefix-filter-20261009/` contains 438 files totaling 246,124,449 bytes, copied with complete count/length/SHA256 parity. The GPU remains user-owned; this CPU intake launches no scientific calculation or test.

Runtime producer receipt is 576,529 bytes, SHA256 `f8538992f75f67aac5184e6549eb07f9ba3a5283d3d72fc973f06228c9b2a896`; reader receipt is 1,804,141 bytes, SHA256 `348ff720c5b24d3dbc9d736a1c232e95eca3d3f014d3f9758cfc8079fcc6fbc1`. The replay manifest is 187,694 bytes, SHA256 `65cb43372774c00c648770188cda70e3d09beb7ae4331970c951e0aa1b026f36`. Runtime snapshots preserve original bytes when Git newline normalization changes tracked copies. The canonical Desktop code intake at merge `637333ce8a6b607662fcfc91db0c19c52a0d154d` reads the contract as 11,746 bytes, SHA256 `d265d9346864d37b57c462b49be8f898f58c627cc5e750ba5c5d37baf95aab00`, and the result as 4,793 bytes, SHA256 `a8d8f1f7d55d52c1b476f09a9642135c0bb4fe651d8be8d2a321940d403289e6`. These checkout bindings remain distinct from executing-source ancestry.

## Relevance to this research

This completes the one generated-prefix conditional component identified after [[multiagentelbo-2026-10-09-compact-raw-history]]. It advances [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] under the same original finite kernel, without replacing the hidden law by a mean-force update or selecting a new formation model. The small conditional upper values do not repair the uninformative global stopped-TV ceiling or the unrestricted entropy-reference tail.

The next preparation constructs complete new-R2 force and prediction coefficients, including the advanced geometry of all four generator slices. That preparation is in progress and has no new evaluation outcome at this publication. [[Gauge-Theoretic Multi-Agent VFE Model]] still requires nonlinear posterior integration, useful actual-history expectations, compact recursive feedback, continuous/native-posterior control and growing size/depth results. All four RG gates remain open, the full goal stays active, the GPU stays user-owned and the 144-case CUDA grid remains unrun.
