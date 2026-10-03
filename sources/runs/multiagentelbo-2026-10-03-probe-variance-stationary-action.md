---
type: run
title: "MultiAgentELBO source-probe variance and stationary-action obstruction, October 3, 2026"
aliases: ["Frozen-parent probe variance and stationary action"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/statistics, field/mathematics]
created: 2026-10-03
---

# Source-probe variance and stationary-action obstruction

> [!info] Citation
> MultiAgentELBO project (2026). *Source-probe variance and stationary-action obstruction*. Code commit [4a15917](https://github.com/cdenn016/MultiAgentELBO/commit/4a15917de4a1607ba6c49b11a5754e9541ac3384), [PR117](https://github.com/cdenn016/MultiAgentELBO/pull/117). The immutable archive is sources/archives/multiagentelbo-2026-10-03-probe-variance-stationary-action/. This continues [[multiagentelbo-2026-10-03-continuous-parent-limits]] and [[multiagentelbo-2026-10-03-conditional-parent-error]].

## Saved-data variance decomposition

The [contract](../archives/multiagentelbo-2026-10-03-probe-variance-stationary-action/probe-variance-CONTRACT.md.txt) fixes all sixteen saved paths at each of N512/N1024 and both grids. Conditional on simulated native/message histories and proposal-enriched meshes, each source probe uses an independent uniform time and native-prefix uniforms under the declared random-tape model. The lift uses exact product-row KL at the same times. Whole-current-assignment self corrections and pairing across arms/grids are retained.

For Y_i=D_i+H(G_i1+G_i2)/2, v_i=H^2(G_i1-G_i2)^2/4 estimates conditional probe variance. Subtracting its path mean from the sample variance of Y estimates variance of the conditional mean. The identities are derived in the [results record](../archives/multiagentelbo-2026-10-03-probe-variance-stationary-action/probe-variance-RESULTS.md.txt). Negative residual estimates and fractions above one are retained.

Fine Gaussian budget variance has estimated probe fractions 0.3621 and 0.3857 at N512/N1024; Gaussian-minus-lift has 0.3457 and 0.2526. For the paired fine-minus-coarse contrast, fractions are 0.7059 and 0.8536. One postprocessing invocation completed in 0.2344153 seconds with 1,234 arithmetic comparisons over 18 groups and 288 rows. Independent scalar reconstruction reproduces all eighteen summaries and prior means/standard errors, with maximum discrepancy 1.42109e-14. No trajectories, new probes, Gaussian propagation or GPU work ran.

These are noisy estimates from two probes, sixteen paths and one model per size. Time/prefix noise cannot be separated. No confidence interval, finite-grid bias, optimal allocation or absolute retained-law error is supplied. More probes could clarify grid sensitivity; they do not remove the unknown hidden-information contribution.

## Necessary zero stationary action

The [proof](../archives/multiagentelbo-2026-10-03-probe-variance-stationary-action/stationary-action-obstruction.md.txt) assumes a fixed finite network, Gibbs stationary law proportional to exp(-E/T), finite normalization at one positive temperature, positive finite-measure bounded sets arbitrarily near the essential energy minimum, and the same full protocol kernel under every start. These introduced assumptions are not asserted for every model in Chapter 12.

Universal success bounded below from every fixed initial density requires -T log P_rho_T(F_T) -> 0 for the full matched lineage event. The proof constructs one fixed density on a bounded low-energy set and compares it directly with Gibbs initialization. It includes stopping-time/randomized protocols without a mixing assumption; selected conditional handoffs cannot replace the full event without denominator control.

If success contains a state-set visit lasting ell_T within deterministic full horizon H_T, stationarity gives P_rho_T(F_T) <= H_T rho_T(C_T)/ell_T. A fixed energy gap Delta, limsup T log H_T < Delta and T log(1/ell_T) -> 0 then exclude universal success. This bounds persistent-event probability, not entrance rate from occupation. The old candidate's chosen exponential horizon is not claimed to satisfy this new gap condition; its previous matched-protocol failure is separate.

An exact OU example in dimension at least 512 has success from every fixed initial density, vanishing stationary probability and zero stationary action. It delimits the obstruction only: residual displacement is not restoring coherence or a recursive hierarchy. All statements hold at fixed N; no joint N,T or thermodynamic limit follows.

## Relevance to this research

[[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]] now have a sampling diagnosis and a necessary condition excluding another class of rare-well searches. O1 still requires small true conditional prediction error in both horizon regimes. O4 still requires actual-history facilitation with positive-weight nonformation handoffs, restoring coherence, a matched stationary horizon comparison, intrinsic partition selection and consistent slow feedback. Neither result changes the active neighborhood profile or theory manuscripts.

## BibTeX

    @misc{multiagentelbo2026probevariance,
      author = {{MultiAgentELBO project}},
      title = {Source-Probe Variance and Stationary-Action Obstruction},
      year = {2026},
      howpublished = {Research records, MultiAgentELBO commit 4a15917},
      url = {https://github.com/cdenn016/MultiAgentELBO/commit/4a15917de4a1607ba6c49b11a5754e9541ac3384}
    }
