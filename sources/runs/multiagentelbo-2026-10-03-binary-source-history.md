---
type: run
title: "MultiAgentELBO complete saved-history binary source comparison, October 3, 2026"
aliases: ["Binary source complete-history replay"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/vfe, cluster/info-geometry, project/multi-agent, field/statistics, field/mathematics]
created: 2026-10-03
---

# Complete saved-history binary source comparison

MultiAgentELBO project (2026). *Complete saved-history comparison of binary source integration*. Code commit [d348827](https://github.com/cdenn016/MultiAgentELBO/commit/d348827c033792949438c7abec6450f706253ce8), [pull request](https://github.com/cdenn016/MultiAgentELBO/pull/125). Immutable [results](../archives/multiagentelbo-2026-10-03-binary-source-history/results.md.txt), [contract](../archives/multiagentelbo-2026-10-03-binary-source-history/contract.md.txt), [summary](../archives/multiagentelbo-2026-10-03-binary-source-history/summary.json), [metadata](../archives/multiagentelbo-2026-10-03-binary-source-history/metadata.json), [array checks](../archives/multiagentelbo-2026-10-03-binary-source-history/array-checks.json) and [test summary](../archives/multiagentelbo-2026-10-03-binary-source-history/test-summary.json) retain committed source bytes. Candidate arrays, executed source, terminal output and both JUnit packets are retained in the code commit.

## Matched history result

This follows [[multiagentelbo-2026-10-03-binary-source-moments]] and replays all 32 archived frozen-model paths, sixteen at each of N=512 and N=1024, with the consistent binary source backend. Both event-augmented grids, horizon one, block size sixteen and the two original probes are fixed by the predeclared contract. The old cubature outputs are retained controls, not a fresh performance benchmark. Each new candidate carries its own moments through the complete history.

Every native path, assignment history, timestamp, Brownian increment, sampled probe label/native row and event count matches the corresponding control exactly. Fine-grid auxiliary totals changed by -1.88235349 and -3.97757285, with empirical paired path standard errors 0.16627869 and 0.201332467. All six budget components, coarse/fine values and paired refinement summaries are archived. These observations concern one frozen learned model per size and two probes per trajectory; they are not confidence bounds or independent node samples.

## Checks and limits

All 32 path jobs passed in one 1378.157451-second CPU invocation using four workers with one numerical thread each. No GPU or new stochastic tape was used. Three tiny replay tests passed in 1.991 seconds. An initial three-test failure exposed the need to pass mobility separately from recognition covariance; that failure and its correction are retained.

Independent NumPy formulas performed 1152 array comparisons, including sender forces and the stable self correction; scalar pair-difference arithmetic checked 216 aggregate means and standard errors. All candidate arrays are finite and the retained-fiber and row-normalization diagnostics passed their declared tolerances. Full covariance history and self-prefix rows are not retained, so their internal update checks remain producer evidence.

This completes the declared finite-grid backend comparison. It does not separately isolate the probability and moment changes, replace the native survival filter, measure the unobserved conditional-information gap or estimate retained-path KL. Each nonlinear tilt is still Gaussian-projected for subsequent receivers. Earlier cubature-specific continuum and integrability results have not been transferred. Practical O1 accuracy/complexity, both regular-filter horizon regimes and full O4 remain open. The active neighborhood profile, default backend and theory manuscripts are unchanged.
