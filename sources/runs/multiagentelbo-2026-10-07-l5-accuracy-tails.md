---
type: run
title: "MultiAgentELBO L5 nonlinear history accuracy and tails, October 7, 2026"
aliases: ["MultiAgentELBO L5 accuracy tails October 7"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, project/multi-agent, field/mathematics, field/statistics, field/physics, field/cs-ml]
created: 2026-10-07
---

# MultiAgentELBO L5 nonlinear history accuracy and tails

MultiAgentELBO project (2026). *Nonlinear history accuracy and tail measurement through N8192*. Published as [PR165](https://github.com/cdenn016/MultiAgentELBO/pull/165), merge [836a0d5689bdce5fe0ca15697a18b095b36d62e9](https://github.com/cdenn016/MultiAgentELBO/commit/836a0d5689bdce5fe0ca15697a18b095b36d62e9). New producer revision 8e7fca8ad5ea885b5a57483bd0e450e8609543b0; checker 9658e54; results 603f0fc. See the [report](https://github.com/cdenn016/MultiAgentELBO/blob/836a0d5689bdce5fe0ca15697a18b095b36d62e9/docs/research/2026-10-03-latent-link-rg-plan/L5-ACCURACY-TAIL-RESULTS.md), [frozen contract](https://github.com/cdenn016/MultiAgentELBO/blob/836a0d5689bdce5fe0ca15697a18b095b36d62e9/docs/research/2026-10-03-latent-link-rg-plan/L5-ACCURACY-TAIL-CONTRACT.md), [producer manifest](https://github.com/cdenn016/MultiAgentELBO/blob/836a0d5689bdce5fe0ca15697a18b095b36d62e9/docs/research/2026-10-03-latent-link-rg-plan/evidence/l5-tail-producer.json) and [independent readback](https://github.com/cdenn016/MultiAgentELBO/blob/836a0d5689bdce5fe0ca15697a18b095b36d62e9/docs/research/2026-10-03-latent-link-rg-plan/evidence/l5-tail-readback.json).

```bibtex
@misc{multiagentelbo2026l5accuracytails,
  author = {{MultiAgentELBO project}},
  title = {Nonlinear history accuracy and tail measurement through N8192},
  year = {2026},
  howpublished = {MultiAgentELBO PR165, producer revision 8e7fca8},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/165}
}
```

## Law, inputs and execution

This follows [[multiagentelbo-2026-10-07-l5-cpu-resource]] at fixed c_*. The law retains based periodic GL(2,R) links, zero anchor, width .3, identity reference metrics, Gaussian episode-increment mass 16 and horizon 16. Three sizes, 512, 2,048 and 8,192 agents, are crossed with c=0 and c=.25. The nonlinear action remains exp(-S) relative to the normalized temporal Gaussian reference; its partition factor is unestimated. No new loop family, source prior, spectral metric, likelihood, original dynamics or base transport is introduced.

All six cases completed. The N512/N2048 nonlinear histories are the unchanged completed L4 archives. Only three new exact Gaussian controls and the missing N8192 nonlinear case were generated. Four chains retain 64 complete histories each; nonlinear runs use 256 burn-in and 256 postburn sweeps, storing every fourth postburn state. Controls use the direct iid branch with 64 draws and no burn-in. The budgets are different and support no matched-cost or paired-draw claim. One law per size supplies no graph-ensemble uncertainty. CPU float64 uses C:/anaconda/python.exe, torch 2.10.0.dev20251210+cu128, NumPy 2.0.0 and one math thread. The occupied GPU was unused.

The new N8192 nonlinear sampler took 653.260664 seconds; new controls took .332796/1.667902/6.813995 seconds at the three sizes. N8192 retained-history bytes are 2,147,483,648 per arm. Complete new arrays, traces, topology, inputs and source snapshots are retained in the canonical `MultiAgentELBO/artifacts/gaussian-latent-history/l5-accuracy-tails-20261007` archive. Old nonlinear histories remain in their original canonical L4 archive. OS/CUDA peak memory is unmeasured, and these observed costs are not scaling exponents.

## Numerical checks and unresolved precision

Three tiny formula tests passed (JUnit 1.815 session seconds), along with a tiny orchestration check and two separately implemented reference formula checks. Saved-only NumPy/SciPy arithmetic imports no producer/scientific package. It reconstructs ordered loops, primitive inverses, singular values, generator fractions, extreme-energy concentration, Gaussian expectations and finite batch/folded-rank diagnostics from all 1,536 retained full histories. Its 1,299 comparisons cover 36,567 derived-array entries and 88,080,384 based loop products, with maximum discrepancy 5.12727638124e-11 in 122.900942 seconds. Unsaved full burn-in and intermediate histories remain unavailable. This establishes numerical consistency for these artifacts, not an independently adjudicated theorem or a continuous-target error bound.

Inherited scalar screens give 43 passes, two misses and three structurally zero action exemptions. Both misses are fixed-coordinate estimates in the exact N8192 Gaussian control. Fifteen tail channels per case give 63 batch-screen passes, fifteen misses and twelve inconclusive results; the separate folded-rank screen gives 61 passes, seventeen misses and twelve inconclusive results. These criteria test different failure modes. Gaussian expectation screens give eighteen passes and three inconclusive unobserved rare-tail checks. A zero estimated MCSE on an unobserved event is not a stationary absence bound.

Folded-rank diagnostics follow [Vehtari et al. (2021), sections 3.1 and 4.1–4.2](https://arxiv.org/html/1903.08008v5). The retained tail cap totals only 256 histories, below their recommended 400 effective draws, and the inherited batch-means ESS is a different estimator from bulk/tail ESS. Rank screens also miss in direct iid controls; those misses alone do not establish bias. Nonlinear scalar diagnostics use every postburn sweep, while tail diagnostics use only stored full histories. Precision remains unresolved; no exhausted budget was extended or retuned.

## Relevance and next obligation

Sampled mean loop defects are about .798 for c=0 and .683 for c=.25 at all three sizes; top-one-percent loop energy shares are about .095 and .079. These are descriptive initialized-sample contrasts with finite-chain MCSE, not stationary tail exponents or a thermodynamic law. Fractions average edges/episodes inside a full history without counting those entries as independent Monte Carlo replicates.

For [[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]], the next measurement obligation is unthinned tail diagnostics or another justified precision design before rare-event/scaling inference. This adds no formation criterion to [[Meta-agents and hierarchical emergence]] and no eigenvalue or metric choice to [[Cellular sheaves and sheaf Laplacians]]. O5, theory-wide O3, sparse-graph S1, strong non-isometry, original collective dynamics, continuous-target accuracy, independent-instance prediction and thermodynamic closure remain open. The user requested a break after publication and canonical synchronization; this checkpoint does not complete the broader goal. Navigation: [[Mathematics MOC]], [[Statistics MOC]], [[Physics MOC]] and [[CS-ML MOC]].
