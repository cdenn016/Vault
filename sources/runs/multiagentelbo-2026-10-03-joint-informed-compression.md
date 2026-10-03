---
type: run
title: "Joint-channel Gaussian compression at matched rank, October 3, 2026"
aliases: ["Hold-refresh joint-sensitivity compression pilot"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/cs-ml, field/statistics]
created: 2026-10-03
---

# Joint-channel Gaussian compression at matched rank

MultiAgentELBO project (2026). *Joint-channel compression at matched rank*. Code commit [8180edb](https://github.com/cdenn016/MultiAgentELBO/commit/8180edbba581abdd91ffd63597013882be7c3a85), [PR 135](https://github.com/cdenn016/MultiAgentELBO/pull/135). The immutable [report](../archives/multiagentelbo-2026-10-03-joint-informed-compression/results.md.txt), [pre-run contract](../archives/multiagentelbo-2026-10-03-joint-informed-compression/contract.md.txt), [metadata](../archives/multiagentelbo-2026-10-03-joint-informed-compression/evidence/metadata.json), basis matrices, scores, source and JUnit retain the checkpoint. This follows [[multiagentelbo-2026-10-03-source-informed-compression]].

The fixed basis adds configuration sensitivity to the existing activation-conditioned source proxy. The configuration matrix averages the full assignment Jacobian Gram, including assignment variance and all sender terms. Its hold/refresh expectation mixes whole product-law second moments, preserving the native global coin's correlations. The source term is weighted by the native refresh probability. Selection uses only activation, mobility, the first structural state and the declared clock; no observed path or later state selects coordinates.

The source weights remain frozen at the mean, and the coin is treated as an augmented record. This is a joint-channel sensitivity proxy, not exact observed-kernel Fisher information, retained KL or a path optimum. The g07 linear Gaussian exterior-interface theorem does not certify switching-law optimality; the c11 regular-filter and two-horizon requirements remain unchanged.

The same two saved paths per N512/N1024, ranks 64/128, K=2, block 16, seed 20261002, tau 0.5, refresh rate one, dt 1/64, 64 microsteps and existing schedule/shortcut conventions were used. Dense, reset, half-block and source-only scores were loaded without rerunning controls. Input arrays and assignments agree with the prior compression archives.

Mean candidate-minus-source-only total loss is -0.107034 nats at N512 and -0.000006 at N1024. The individual N1024 contrasts are +0.002407 and -0.002419, so their near-zero mean is not an exact equality. The gap to dense remains +7.953540/+8.150953 nats. One N1024 path has no assignment changes. These underpowered exploratory results do not establish general superiority, population scaling or absolute accuracy.

Five new tiny CPU checks passed in 0.508 seconds. Independent autograd energy Hessians and complete binary enumeration validate assignment second moments, inverse links, sender terms, variance, global mixture and joint eigenpairs. All four large paths passed numerical checks, and a separate scalar reconstruction reproduced 48 loss components plus four event counts. The sole run completed in 338.723305 CPU seconds; CUDA was available and unused. Weighted source/configuration proxy traces are 7.585179/0.150000 at N512 and 16.755897/0.304659 at N1024; these are not predictive losses.

## Relevance to this research

Mean/covariance storage remains 4160/16512 entries with dense constants and temporary fine covariance. No total-memory or speed improvement is established. Next freeze all three basis definitions and evaluate further saved histories under a predeclared paired protocol, keeping the pilot and extension summaries separate. That would assess variability in this fixed model and would not establish the c11 asymptotic class or endogenous formation.

O1/O4, the historical source-projection parity failure and formal verification of the provisional reverse-cost analysis remain open. No GPU, native resampling, baseline rerun, failed-study retry, analytical-loop restart or canonical theory change occurred. See [[Staged hierarchy formation and RG composability]] and [[Gauge-Theoretic Multi-Agent VFE Model]].
