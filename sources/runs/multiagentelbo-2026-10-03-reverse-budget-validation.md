---
type: run
title: "MultiAgentELBO reverse-budget validation at 512 and 1024 agents, October 3, 2026"
aliases: ["Large-network candidate-driven reverse-budget validation"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/cs-ml, field/statistics]
created: 2026-10-03
---

# Reverse-budget large-network validation

MultiAgentELBO project (2026). *Candidate-driven reverse-budget validation at 512 and 1024 agents*. Code commit [836cbe2](https://github.com/cdenn016/MultiAgentELBO/commit/836cbe2dd7b0f58bd869618bdca8f19e808f9190), [PR 131](https://github.com/cdenn016/MultiAgentELBO/pull/131). The immutable [report](../archives/multiagentelbo-2026-10-03-reverse-budget-validation/results.md.txt), [pre-run contract](../archives/multiagentelbo-2026-10-03-reverse-budget-validation/contract.md.txt), [metadata](../archives/multiagentelbo-2026-10-03-reverse-budget-validation/evidence/metadata.json), source snapshot, inputs, compact paths, JUnit and independent reports preserve this checkpoint. It follows [[multiagentelbo-2026-10-03-reverse-budget-implementation]].

One fresh path per size completed on paired coarse/fine meshes in 119.085644 CPU seconds. The fixed profile used saved learned GL(2,R) activation, frozen mobility Sigma, temperature 0.5, block size 16, horizon one, 64 coarse intervals and two source probes. Model seed was 20261002; path seeds were 20261010 and 20361010. CPU float64 and sequential BLAS were used; no GPU or retry ran. Two new tiny runner tests passed. Independent NumPy reconstruction passed all four grids, with a maximum Euler discrepancy of 2.220446e-16 and successful final hidden covariance Cholesky checks. The 112 arrays in committed compact paths match their full local originals exactly. Full final covariance matrices remain in the local original archives identified in the summary; those complete files were checked before archival.

At N512 the coarse and fine total functional estimates were 77.168919 and 78.135652 nats, with three visible assignment changes on both meshes. At N1024 they were 151.359655 and 151.909986, with zero proposals on the declared fixed seed. Actual source reset at N1024 and invisible self events at either size were therefore not exercised by these large-network paths. Hypothetical source probes were exercised at both sizes, and the earlier tiny tests cover self events. The respective grid changes were 1.25% and 0.36% of the coarse total. Roughly 92% of each fine total came from source cost.

## Relevance to this research

These are single-path finite-grid samples of a conservative comparison-law functional. They are not retained KL values, continuous expected-budget certificates, seed-variance estimates, scaling evidence or demonstrations of poor retained prediction. One path and two source probes per size do not establish practical O1 accuracy. Endpoint conditioning, mesh dependence and the checker's lack of independent source integration retain their stated limits.

The next accuracy obligation is to distinguish reverse auxiliary hidden-state comparison cost from retained conditional-prediction error before launching a full replicated measurement. The existing native-weighted conditional decomposition cannot simply be used in this different expectation. If the functional itself is to be characterized empirically, a separate paired-grid design with more paths and probes is needed. Quantitative O1 in both horizon regimes, forward native integrability, the previous parity failure and O4 remain open. One exact-Gaussian analytical round remains; this validation does not restart the exhausted O4 loop. See [[Staged hierarchy formation and RG composability]] and [[Gauge-Theoretic Multi-Agent VFE Model]].
