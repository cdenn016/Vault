---
type: run
title: "Source-informed Gaussian compression at matched rank, October 3, 2026"
aliases: ["Frozen-weight source-sensitivity compression pilot"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/cs-ml, field/statistics]
created: 2026-10-03
---

# Source-informed Gaussian compression at matched rank

MultiAgentELBO project (2026). *Source-informed compression at matched rank*. Code commit [8d1e114](https://github.com/cdenn016/MultiAgentELBO/commit/8d1e114235ce3301db49330ee42b5efa0865f339), [PR 134](https://github.com/cdenn016/MultiAgentELBO/pull/134). The immutable [report](../archives/multiagentelbo-2026-10-03-source-informed-compression/results.md.txt), [pre-run contract](../archives/multiagentelbo-2026-10-03-source-informed-compression/contract.md.txt), [metadata](../archives/multiagentelbo-2026-10-03-source-informed-compression/evidence/metadata.json), basis matrices, scores, source and JUnit retain the executed checkpoint. This follows [[multiagentelbo-2026-10-03-compressed-message]].

The candidate uses the activation Gaussian conditioned at its mean retained value and the first structural state's binary source rows. It accumulates second moments of quadratic log-odds gradients, freezes each probability weight at the mean, whitens the hidden reference and selects leading directions. Covariance terms preserve nonzero sensitivity even at zero mean. No later paths, observations or scores select the basis. It is a source-sensitivity heuristic, not expected Fisher information or the g07 linear Gaussian exterior-record optimum.

The declared two saved paths at each of N512/N1024 use ranks 64/128, matching the previous half-block control. The existing decoder and source-adapted scorer remain unchanged. K=2, block 16, model seed 20261002, tau 0.5, rate-one refresh, dt 1/64, the eight-interval schedule, and shortcut threshold 1e-12 match the archives. Actual retained inputs and assignments equal the half-block archive; dense, reset and half-block scores were loaded without rerunning those arms.

Mean total source-informed-minus-half-block loss is -1.295775 nats at N512 and +0.085335 at N1024. Corresponding source components are +0.077146 and -0.533730, with configuration components -1.372921 and +0.619065. Thus the source/configuration tradeoff is mixed. Against dense, total losses remain +8.060574/+8.150960. The sample is underpowered, one larger-network path has no assignment changes, and no population, scaling or retained-KL conclusion follows. The report preserves per-path results and descriptive paired standard errors.

Fifteen focused tiny CPU tests passed, including independent autograd source-gradient moments and NumPy conditional eigenbasis checks. All four paths passed numerical checks; a separate scalar checker reconstructed 36 loss components and four event counts. The sole run completed in 353.558043 seconds on CPU float64 with one Torch thread and sequential MKL. CUDA was available and unused.

## Relevance to this research

Persistent mean/covariance entries remain 4160/16512, with dense immutable decoder constants and fine covariance workspaces. No total-memory or runtime improvement is established. This candidate did not consistently lower joint loss on the declared pilot. The next proposed comparison includes retained-configuration records alongside source labels, with channel weights declared from the transition law before scoring. That is a candidate direction, not a proven optimum or changed O1 criterion.

Practical O1, regular-filter admission, both horizon regimes, and endogenous second formation/O4 remain open. The historical parity failure and formal verification of the provisional reverse retained-cost analysis remain unresolved. Neither exhausted analytical loop was restarted. No GPU, native resampling, failed-study retry or canonical theory edit occurred. See [[Staged hierarchy formation and RG composability]] and [[Gauge-Theoretic Multi-Agent VFE Model]].
