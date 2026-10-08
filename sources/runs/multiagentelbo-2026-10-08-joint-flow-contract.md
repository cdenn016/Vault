---
type: run
title: "MultiAgentELBO simultaneous inference and finite retained-state contract"
aliases: ["R0-R2 simultaneous inference CPU admission"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO simultaneous inference and finite retained-state contract

The resumed fixed-c_* RG program now has an executed common-state finite-width inference step. Matter, source and generator directions use the same initial state and one jointly accepted step. The primary expected-Hessian Bayesian learning rule remains distinct from natural-gradient descent of the finite reparameterized sample objective. The accompanying finite correlated Gaussian/record construction identifies an adapter into already implemented conditioning and projection kernels. It does not complete the growing retained-state limit, native parent dynamics, or endogenous hierarchy.

## Source and frozen scope

Code revision `20c83bc19c8f456c0721bf7ce6a7b2883730d06d`, merged in [MultiAgentELBO PR177](https://github.com/cdenn016/MultiAgentELBO/pull/177), contains [the common contract](https://github.com/cdenn016/MultiAgentELBO/blob/20c83bc19c8f456c0721bf7ce6a7b2883730d06d/docs/research/2026-10-03-latent-link-rg-plan/COMPLETION-CONTRACT.md), [R1 implementation results](https://github.com/cdenn016/MultiAgentELBO/blob/20c83bc19c8f456c0721bf7ce6a7b2883730d06d/docs/research/2026-10-03-latent-link-rg-plan/R1-JOINT-FLOW-RESULTS.md), [R2 construction](https://github.com/cdenn016/MultiAgentELBO/blob/20c83bc19c8f456c0721bf7ce6a7b2883730d06d/docs/research/2026-10-03-latent-link-rg-plan/R2-OPERATIONAL-STATE.md) and their executed evidence. The live theory baseline was Research `e2cefb4a071592a8dbed2f2ee5c544a3a0c73053`. No manuscript changed.

```bibtex
@misc{codex2026jointflowcontract,
  author = {Codex},
  title = {Simultaneous Latent Inference and Finite Retained-State Contract},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/177},
  note = {MultiAgentELBO implementation and conditional mathematical construction}
}
```

The first execution family is a positively anchored real GL+(2) interaction lattice at one base point. Generative parameters stay fixed. Inference time, normalized generative episode history and coarse depth are distinct. The normalized history retains its backward partition factors; Proca-like history stationarity is not substituted for a causal generative transition. Original-record prediction is measured in nats with its declared reference measure. The initial engineering target is 0.01 nat excess loss per original record with numerical/conditional integration error at most 0.0025 nat; these are prospective finite-study targets, not established theorem constants or achieved accuracy.

## Executed evidence

Ten tiny three-agent, two-dimensional CPU tests pass, covering common-state derivatives, one-way sender forces, Gaussian and categorical Fisher behavior, support/admissibility, estimator distinction and the actual profile route. One saved N512 instance used 16 inference draws and 256 independent scoring draws in CPU float64. Direction construction, one accepted joint step and scoring took about 5.45 seconds in total; the step 0.01 needed no backtracking. The archived prior draw is a finite MCMC output, not an independent-network ensemble or an exact prior sample.

A short refinement study on that same saved input reached inference time 0.04 at h=0.02, 0.01 and 0.005. Successive endpoint RMS differences decreased by factors 0.479-0.495 across all five state blocks, consistent with first-order behavior on this interval. The separate-batch objective changes per record were -0.59659, -0.59230 and -0.59023. They are objective changes, not predictive excess losses; one evaluation batch estimates no Monte Carlo uncertainty. CUDA admission and the eight-instance N512/N1024 calibration remain unrun. The GPU was occupied and no competing workload was started.

## Finite state and remaining gap

For a declared finite original-record vector and a common component law, retain full joint means/covariances, record cross-covariances, all dressed copies, both channels, weights, normalization and coordinate tags. Affine blocking updates those moments by congruence, while Gaussian conditioning supplies the joint record decoder. The report derives a finite expected predictive-KL bound from relative covariance and mean errors and propagates these errors through a finite channel composition. Eight rational identities and ten comparisons against the existing runtime pass, with maximum absolute discrepancy 8.88e-16. These executed fixtures ground the derivation; they are neither large-network evidence nor independent mathematical adjudication.

The construction assumes positive-definite joint covariance and full-row-rank retained coordinates. Redundant concatenated channels, overlapping coordinates and singular posterior support require separate support-aware treatment; no jitter was added. Continuous mixture memory, arbitrary future queries, growing common-space tightness, all-copy cancellation amplitudes and uniform nonlinear error remain unresolved. A disjoint union of finite coordinate spaces is an exact finite comparison device, not a growing RG limit.

## Relevance and continuation

This batch advances [[Gauge-Theoretic Multi-Agent VFE Model]], [[Staged hierarchy formation and RG composability]] and [[Renormalization-group flow of beliefs]] by implementing a missing runtime reference and locating the native-parent handoff seam. The next implementation carries actual component moments, weights, geometry and record identities into existing full-covariance kernels. GPU capacity admission and independent-instance calibration proceed when resources permit. All four full RG gates remain open, and the goal remains active without automatic phase pauses. Both historical N8192 readback failures are preserved and were not retried.
