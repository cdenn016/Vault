---
type: run
title: "MultiAgentELBO L5 captured exponential diagnosis"
aliases: ["MultiAgentELBO L5 coefficient diagnosis"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/statistics, field/mathematics, field/physics, field/cs-ml]
created: 2026-10-07
updated: 2026-10-07
---

# MultiAgentELBO L5 captured exponential diagnosis

The captured N8192 forward exponential is reproduced exactly by using the correct trace and traceless matrix but omitting the diagonal-square term from the scalar discriminant. The live source includes that term. Two distinct 64-iteration probes on the one saved draw did not reproduce the failure. Cause and both full N8192 readbacks remain unresolved; no scientific replay, tolerance change, runtime adjustment or GPU allocation occurred.

## Evidence and scope

This follows [[multiagentelbo-2026-10-07-l5-unthinned-precision]], whose six sampling cases completed with four successful full readbacks and two N8192 failures. For the captured Gaussian-control matrix, the correct discriminant is -0.0021632896786903657. Its off-diagonal product is -0.0032181076526026932, and its squared diagonal contribution is 0.0010548179739123273. Reconstructing with the off-diagonal product alone reproduces all four captured forward entries exactly in float64. This is an arithmetic signature, not proof of which native operation failed.

The first probe retained the original strided input and unsplit discriminant expression, compared staged operations, multiplication and contiguous squaring against scalar references, and checked square roots and the captured location's coefficients. At c1b7bca it completed 64 iterations in 6.570038 seconds; maximum discrepancy was 1.1102230246251565e-16. The separate context arm ran the reconstructor's SVD, loop products and reductions around instrumented exponential calls on that same fixed draw. At 12e2ec7 it completed 64 iterations in 47.956766 seconds; every inverse residual was 7.771561172376096e-16 and no additional discriminant guard fired. Retaining intermediate arrays changes their lifetime, and fixed-draw repetition does not reproduce the failed process's varying-draw allocation history. These are non-reproductions, not repairs or full-case acceptance.

The checked Python path loads raw samples read-only, makes a private matrix copy and explicitly includes the square term. No Python-level input mutation, persistent exponential cache or supplied shared output buffer explains the captured value. NumPy 2.0 introspection reports SSE41 square/sqrt and AVX2 add/multiply, without changing dispatch. The source pin for the published report is 45df76067ddbe9f97ef9ff9c7ab6e5a33fdd5471: [diagnosis](https://github.com/cdenn016/MultiAgentELBO/blob/45df76067ddbe9f97ef9ff9c7ab6e5a33fdd5471/docs/research/2026-10-03-latent-link-rg-plan/L5-NUMERICAL-DIAGNOSIS.md), [coefficient probe](https://github.com/cdenn016/MultiAgentELBO/blob/45df76067ddbe9f97ef9ff9c7ab6e5a33fdd5471/docs/research/2026-10-03-latent-link-rg-plan/evidence/l5-coefficient-probe-20261007.json), [context probe](https://github.com/cdenn016/MultiAgentELBO/blob/45df76067ddbe9f97ef9ff9c7ab6e5a33fdd5471/docs/research/2026-10-03-latent-link-rg-plan/evidence/l5-context-probe-20261007.json). Runtime was C:/anaconda/python.exe, CPU float64, one math thread and sequential MKL.

## Relevance to this research

The original fixed-c_* GL history law, sampler, numerical guards and active configuration are unchanged. Both N8192 producer summaries retain incomplete independent numerical coverage. Another ordinary case replay or longer repetition of these exhausted probes is not justified by their negative results. A future numerical discriminator needs to capture the intermediate at the event. The CUDA capacity/timing arm remained unrun because a live Spyder GPU workload became active before launch.

The broad goal is active. Source-first work on the existing noncompact-prior tightness and local conditional-law limit can continue independently, followed by compatible coarse kernels and uniform size/depth error. These probes establish no stationary law, O5 spectral scaling, formation, original joint dynamics or thermodynamic closure. No manuscript or prior immutable source is changed by this ingestion.

[[Gauge-Theoretic Multi-Agent VFE Model]]
[[Staged hierarchy formation and RG composability]]
[[Meta-agents and hierarchical emergence]]
[[Cellular sheaves and sheaf Laplacians]]
[[Physics MOC]]
[[Mathematics MOC]]
[[Statistics MOC]]
[[CS-ML MOC]]
