---
type: run
title: "MultiAgentELBO consistent binary source moments, October 3, 2026"
aliases: ["Binary source probability and moment integration"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/vfe, cluster/info-geometry, project/multi-agent, field/statistics, field/mathematics]
created: 2026-10-03
---

# Consistent binary source probability and moment integration

MultiAgentELBO project (2026). *Consistent binary source moments: implementation and saved-event results*. Code commit [ec48675](https://github.com/cdenn016/MultiAgentELBO/commit/ec4867529b0e1438683ef8f81946ad661be4b5fc), [PR124](https://github.com/cdenn016/MultiAgentELBO/pull/124). Immutable [results](../archives/multiagentelbo-2026-10-03-binary-source-moments/results.md.txt), [contract](../archives/multiagentelbo-2026-10-03-binary-source-moments/contract.md.txt), [run metadata](../archives/multiagentelbo-2026-10-03-binary-source-moments/metadata.json), [test summary](../archives/multiagentelbo-2026-10-03-binary-source-moments/test-summary.json) and [array checks](../archives/multiagentelbo-2026-10-03-binary-source-moments/array-checks.json) retain committed source bytes. Per-row arrays, executed source and failure/pass JUnit packets are archived in the code commit.

## Method and runtime

This addresses the local integration defect measured in [[multiagentelbo-2026-10-03-activation-source-calibration]]. For a standard Gaussian quadratic logit Z, the characteristic function phi and the complex Gaussian mean h and covariance S give first/second weighted transforms phi h and phi(S+hh^T). Integrating their imaginary parts against the logistic inversion weight produces unnormalized moments for one label; the complementary moments sum to the incoming Gaussian. Mapping the selected mean and covariance through the same physical Cholesky factor makes the probability and moment update consistent.

The opt-in source_backend=binary_integral mode uses CPU float64 and exactly two source labels. It reaches actual source updates, sampled-prefix probes and self-assignment scoring through the spawned budget runner. The square-root update retains conditional residual covariance and fixed block sums. Numerical quadrature failure, non-interior probability or failed Cholesky stops the update, without clipping or variance floors. Each later row still uses a Gaussian approximation to the preceding nonlinear tilt.

## Saved-event comparison

The predeclared selection takes the first saved path with a visible source event and its first event at each size. These were N512-path000 at time 0.25586339 and N1024-path001 at 0.02158746. Replaying saved retained observations reproduced pre-event candidate means and old cubature post-event means exactly in this execution. No native trajectory, source draw or probe was generated.

The full ascending receiver sequences changed some row probabilities by 0.152714 and 0.150983, and final mean coordinates by up to 0.178082 and 0.225304. Selected joint log scores changed from -324.462201 to -320.709764 and from -637.934550 to -635.618746. Both final hidden covariances passed Cholesky and retained-fiber residuals were below 5.2e-17. Integral sequence runtime was 2.4624 and 10.7252 seconds; the full comparison took 25.3555 CPU seconds.

There are only two selected events, one per frozen model. Higher observed scores are descriptive sensitivity results, not general native-prediction improvement. Later rows follow each backend's own approximate Gaussian prefix. Neither backend includes the native survival filter, and the previous cubature-specific integrability and continuous-limit results have not been transferred to the new mode.

## Validation and relevance

Twenty-five final tiny tests passed across three packets: independent moment/physical-coordinate quadrature, complementary moment reconstruction, coordinate changes, positive hidden covariance, retained fibers, input preservation and full consumer/worker configuration routing. Two earlier test-collection failures and one three-case standard-error assertion failure are preserved. The latter was a bit-exact scaled-versus-unscaled arithmetic comparison differing by 3.47e-18; the corrected test uses the independent two-sample formula with a machine-roundoff bound. Production statistics did not change.

The next practical O1 comparison is a matched complete-history replay with both backends, measuring source and drift budgets and runtime. Auxiliary budgets remain distinct from retained path KL. Exact native conditional characteristics, survival conditioning, effective complexity, both horizon regimes and full O4 remain open. Active profiles and default cubature are unchanged. No GPU, historical heavy node or theory-manuscript edit occurred.
