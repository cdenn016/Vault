---
type: run
title: "Compressed source-adapted Gaussian message pilot, October 3, 2026"
aliases: ["Half-block compressed switching-history message pilot"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/cs-ml, field/statistics]
created: 2026-10-03
---

# Compressed source-adapted message pilot

MultiAgentELBO project (2026). *Compressed source-adapted message pilot*. Code commit [dc892c4](https://github.com/cdenn016/MultiAgentELBO/commit/dc892c4b945c2e746ee1de452fd9d45c33982aaa), [PR 133](https://github.com/cdenn016/MultiAgentELBO/pull/133). The immutable [report](../archives/multiagentelbo-2026-10-03-compressed-message/results.md.txt), [pre-run contract](../archives/multiagentelbo-2026-10-03-compressed-message/contract.md.txt), [metadata](../archives/multiagentelbo-2026-10-03-compressed-message/evidence/metadata.json), source, inputs, scores and JUnit preserve the checkpoint. It follows [[multiagentelbo-2026-10-03-reverse-retained-decomposition]] and the existing source-adapted predictor in [[multiagentelbo-2026-10-02-source-adapted-gaussian]].

The optional decoder stores only moments of declared half-block contrasts between observations. It lifts them through the activation Gaussian conditional, runs the existing source/propagation/conditioning step, and encodes the next message. Discarded conditional structure is reset to the reference. The default dense scorer and native switching law are unchanged. The fixed basis uses no future observations and has no claimed optimality for quadratic source prediction.

Two saved paths each at N512/N1024 completed all 64 microsteps in 340.684909 CPU seconds, without native resampling, relearning or GPU use. The profile preserves K=2, block 16, learned GL comparison maps, temperature 0.5, refresh rate one, dt=1/64, and the previous shortcut threshold 1e-12. Dense and reset controls use archived scores from the same paths. Ten tiny CPU checks passed, including independent Gaussian conditioning, rank-zero/full-hidden recovery and causal prefixes. A separate scalar calculation reproduced all 24 loss contrasts and four event counts. Mean/covariance fiber errors stayed below 1.4e-16; initial scores agreed with the dense archive within 1.14e-13.

Mean compressed-minus-dense path loss was 9.356349 nats at N512 and 8.065625 at N1024. Corresponding compressed-minus-reset values were -0.853014 and -0.144102. Thus compression predicted worse than dense on every pilot path and modestly better than reset. The two N512 paths each had two assignment changes; N1024 had two and zero. The report retains all source/configuration components and descriptive paired standard errors. Two paths and one realization per size are underpowered; these are neither absolute retained-KL estimates nor independent held-out validation.

## Relevance to this research

The message carries 64 or 128 hidden means and a full covariance: 4160 or 16512 stored scalars, compared with 1049600 or 4196352 fine-coordinate mean/covariance scalars in the dense scorer. Those ratios are about 252-254. However the decoder has 1311744 or 5244928 immutable tensor entries, and each step reconstructs dense fine covariance workspaces. Native model/schedule constants, retained coordinates, assignment labels and score arrays are additional. No reduction of total resident/peak memory or speedup is established, and ranks remain proportional to size.

This supplies an executable compression comparison for informative switching histories. It does not establish practical O1 accuracy, continuous regular-filter admission, either required horizon regime, endogenous formation or O4. The next candidate comparison should choose source-informed coordinates before scoring and compare them with this fixed coordinate control at matched rank; the old Gaussian-record spectral optimum does not automatically transfer. The previous parity failure and the provisional reverse-cost record's missing formal verification remain open. No canonical theory manuscript changed. See [[Staged hierarchy formation and RG composability]] and [[Gauge-Theoretic Multi-Agent VFE Model]].
