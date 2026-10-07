---
type: run
title: "MultiAgentELBO graded Gaussian retention, October 7, 2026"
aliases: ["MultiAgentELBO O4 graded retention October 7"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, project/multi-agent, field/mathematics, field/statistics, field/physics, field/cs-ml]
created: 2026-10-07
---

# MultiAgentELBO graded Gaussian retention

MultiAgentELBO project (2026). *O4 graded Gaussian retention on original cutoff posteriors*. Published in [PR161](https://github.com/cdenn016/MultiAgentELBO/pull/161), pinned to merge [c480344713bc0b6624598e4b596b6558548d5282](https://github.com/cdenn016/MultiAgentELBO/commit/c480344713bc0b6624598e4b596b6558548d5282). Scientific source is 59046c3559b90f4973a5b72b7af682dc9e846e18 and results commit is a708b599abd4408dba3bbf89b804ffdae949c1e2. Primary records are the [contract](https://github.com/cdenn016/MultiAgentELBO/blob/c480344713bc0b6624598e4b596b6558548d5282/docs/research/2026-10-03-latent-link-rg-plan/O4-GRADED-RETENTION-CONTRACT.md), [results](https://github.com/cdenn016/MultiAgentELBO/blob/c480344713bc0b6624598e4b596b6558548d5282/docs/research/2026-10-03-latent-link-rg-plan/O4-GRADED-RETENTION-RESULTS.md), [terminal manifest](https://github.com/cdenn016/MultiAgentELBO/blob/c480344713bc0b6624598e4b596b6558548d5282/docs/research/2026-10-03-latent-link-rg-plan/evidence/o4-graded-retention-summary.json), [independent readback](https://github.com/cdenn016/MultiAgentELBO/blob/c480344713bc0b6624598e4b596b6558548d5282/docs/research/2026-10-03-latent-link-rg-plan/evidence/o4-graded-retention-readback.json), [all-instance rollup](https://github.com/cdenn016/MultiAgentELBO/blob/c480344713bc0b6624598e4b596b6558548d5282/docs/research/2026-10-03-latent-link-rg-plan/evidence/o4-graded-retention-rollup.json) and [focused JUnit](https://github.com/cdenn016/MultiAgentELBO/blob/c480344713bc0b6624598e4b596b6558548d5282/docs/research/2026-10-03-latent-link-rg-plan/evidence/o4-graded-retention-focused.xml).

```bibtex
@misc{multiagentelbo2026gradedretention,
  author = {{MultiAgentELBO project}},
  title = {O4 graded Gaussian retention on original cutoff posteriors},
  year = {2026},
  howpublished = {MultiAgentELBO PR161, scientific source revision 59046c3},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/161}
}
```

## Declared model and method

The existing live theory's connection-Laplacian and fixed-section compression construction is graded on supplied 16-agent blocks, with 32 coordinates per block, across four original N512/N2048 networks at generator widths .1/.3. There are 32/128 blocks per case. Every agent and all 256 frozen nonabelian $GL^+(2,\mathbb R)$ link histories participate. Original geometry, baseline covariances, source priors, plaquette model and episode-three cutoff are held. Each case's four original truth-chain/sample-zero instances retain 192 candidate histories and sixteen source-label pairs with their actual cutoff posterior weights. The four chains share one underlying network; they are descriptive paired evaluations, not independent network replication. No observation, trajectory, optimization or link exponential was regenerated.

The frozen mean-Fisher metric is $M_i=\Sigma_i^{-1}$. Each internal edge combines both source-prior-weighted directed Gaussian mean-KL quadratic terms, with the edge metric transformed under reversal. The block generalized eigenproblem diagonalizes $S^T L_I S$, where $S$ is the block baseline Cholesky factor. Bottom ranks 2, 4, 8, 16, 24 and 32 are compared with the actual archived two-stage rooted-mean channel at matched rank two. This internal frozen operator is not the complete original collective Hessian, and the rank budget is declared rather than chosen by a formation rule.

The original linear record law rebuilds the cutoff fine Gaussian posterior and reproduces the archived observation/first-parent seams. It does not use the fresh positive-horizon fibers introduced in [[multiagentelbo-2026-10-07-full-graph-feedback]]. In baseline-whitened coordinates, let $a$ be the posterior mean correction and $B$ its shared rank-four covariance factor. With block-orthonormal frame $U_r$, baseline conditional recovery has exact component loss $J(a,B)-J(U_r^T a,U_r^T B)$, where $J(a,B)=\tfrac12[\|a\|^2-\operatorname{tr}(B^TB)-\log\det(I-B^TB)]$. This follows the existing September 11 reference-relative recovery accounting. Shared factors specify the complete correlated joint law, including cross-block corrections; product marginals are not substituted. Decoder fibers are singular affine measures without an ambient density or jitter.

The actual weighted component sum is exact labeled history/source recovery KL and an upper bound on unlabeled mixture KL. It is not an exact unlabeled mixture divergence or a predictive score. A separate frozen internal quadratic mean flow has exact spectral relaxation rates and checked residual/energy bounds at times 0, 1, 4 and 12. Those are declared linear perturbation controls, not original joint-dynamics accuracy.

## Executed outcomes and costs

The once-only producer completed all 112 outcomes in 28.716886 seconds using CPython 3.14.4 and NumPy 2.4.4 with one-thread BLAS settings. One saved-only checker, importing neither the producer nor the new Gaussian API, passed 1,324 comparisons over 205,963,616 entries in 19.242213 seconds, zero failures and maximum absolute discrepancy $7.1054273576\times10^{-14}$ against frozen 1e-9 absolute/relative tolerances. Six tiny dense-oracle/integration tests passed beforehand in .364 JUnit seconds. Small tests ground the construction; the executed networks determine its reported numerical scale. There was no full suite, GPU or scientific retry.

Mean labeled recovery losses over four dependent whole-instance evaluations, in nats, are:

| Agents, width | Rank 2 | Rank 16 | Rank 24 | Rank 32 |
| --- | ---: | ---: | ---: | ---: |
| 512, .1 | 2.264058 | 1.466351 | .842048 | numerical zero |
| 512, .3 | 1.836941 | 1.224898 | .705989 | numerical zero |
| 2048, .1 | 2.871912 | 1.670616 | .924223 | numerical zero |
| 2048, .3 | 2.280529 | 1.654471 | .957284 | numerical zero |

At rank two only about .9-2.2% of the posterior component information relative to baseline is retained. Spectral-minus-rooted loss is positive in fifteen of sixteen paired instances, ranging from -.000193 to .011331 nats. The channels are nearly tied on this archive, with identical charged rank-two costs. No general ranking or population significance follows. All nested losses, full-rank identity and the frozen quadratic bounds pass. The smallest rank-two boundary gap is .076655; other rank boundaries are much narrower. Neither a supplied-block gap nor exact quadratic decay establishes substantial endogenous formation or predictive sufficiency.

Standalone occupied storage includes all instance-specific retained frames, baseline geometry, memberships, history/label/affected indices, posterior weights and sparse retained mean/shared-factor messages. At N512/N2048 it is 3.7556/12.8377 MiB for rank two, 29.6775/101.7595 MiB for rank sixteen, and 59.3025/203.3845 MiB at full rank. The complete common input inventory is 44.7787/169.2113 MiB; per-instance inputs remain separate. An alternative shared 256-history frame dictionary alone costs 4/16 MiB at rank two and 64/256 MiB at full rank. Named dictionary encoder workspace is 276,082,216/1,087,646,248 bytes, and named reconstruction workspace ranges from 70,550,008 to 215,118,568 bytes, excluding library temporaries and interpreter RSS. Compressed NPZ disk size is 805,784,390 bytes, not measured peak RAM. No payload-only storage or speedup advantage is claimed.

The canonical local archive is `MultiAgentELBO/artifacts/gaussian-latent-history/o4-graded-retention-20261007`, including source snapshots, inputs, full numerical arrays, terminal records and logs. PNG/vector PDF were visually inspected. The first plotting-only attempt failed because an external helper printed Unicode under Windows cp1252; UTF-8 repaired only export. Earlier failures and [[multiagentelbo-2026-10-07-recognition-precision|L2 precision_target_unmet]] remain unchanged. Source identities bind provenance; mathematical values determine acceptance.

## Relevance to this research and remaining questions

This partially answers the October 7 soft-fixed-sector question O4 with a frozen Gaussian recovery curve and quadratic bounds, extending the existing [[Cellular sheaves and sheaf Laplacians]], [[Meta-agents and hierarchical emergence]] and [[Staged hierarchy formation and RG composability]] constructions. The result separates slow internal relaxation from record-recovery information, a distinction already formulated in the earlier Gaussian realization review. It supplies no new intrinsic selector and no endogenous formation theorem.

The next decisive soft-sector question is O1: whether small generalized eigenvalues identify substantial near-sectioned mass, rather than localized low modes, under explicit expansion and noncompact transport-conditioning assumptions. Theory-wide O3 remains open beyond this experiment's baseline precision; graph-family S1 remains open beyond the held plaquette model. Original collective-flow error, predictive sufficiency, evolving geometry, continuous-history/L2 precision, independent-instance prediction, nonlinear scaling and the thermodynamic limit remain outstanding. The broad RG goal is active in [[Gauge-Theoretic Multi-Agent VFE Model]]. Navigation: [[Mathematics MOC]], [[Statistics MOC]], [[Physics MOC]] and [[CS-ML MOC]].
