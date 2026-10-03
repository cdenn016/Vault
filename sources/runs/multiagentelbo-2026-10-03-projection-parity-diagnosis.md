---
type: run
title: "MultiAgentELBO projection parity diagnosis, October 3, 2026"
aliases: ["Projection parity non-reproduction"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/cs-ml, field/statistics]
created: 2026-10-03
---

# Projection parity diagnosis

MultiAgentELBO project (2026). *Bounded diagnosis of source projection parity*. Code commit [3f05d15](https://github.com/cdenn016/MultiAgentELBO/commit/3f05d152395f11b056b646eba332cd7c8be1428f), [PR 127](https://github.com/cdenn016/MultiAgentELBO/pull/127). Immutable [results](../archives/multiagentelbo-2026-10-03-projection-parity-diagnosis/results.md.txt), [collection checks](../archives/multiagentelbo-2026-10-03-projection-parity-diagnosis/collection-checks.json), [first-event metadata](../archives/multiagentelbo-2026-10-03-projection-parity-diagnosis/first-event-metadata.json), [history trace](../archives/multiagentelbo-2026-10-03-projection-parity-diagnosis/history-trace-metadata.json) and [spawned discriminator](../archives/multiagentelbo-2026-10-03-projection-parity-diagnosis/spawn-discriminator-metadata.json) preserve committed source bytes. The code commit retains executed scripts, terminal output, full first-event covariance data, new projection diagnostics and JUnit.

This follows [[multiagentelbo-2026-10-03-source-projection-entropy]]. The original failed attempt named fine_mean for N512 path 000 but retained neither the failed values nor the discrepancy magnitude. A fixed-observation first-event comparison found identical archived/off/on mean, covariance, source rows and integration-error values. Complete path000 traces checked 194 boundaries in each on/off arm and both matched all thirty archived candidate fields. Four distinct spawned workers then matched all thirty fields on each of the first four N512 paths. These calculations took 9.111574, 78.250998 and 49.261807 CPU seconds respectively. They do not explain the original failure or show that it was harmless floating-point noise.

The measurement runner now captures every actual candidate array, the differing reference field, first unequal index, both values, unequal-element count and maximum absolute difference before its unchanged exception. Two tiny scalar/matrix capture tests passed in 1.423 seconds; the two expected missing-helper failures are retained. The runner was not executed after the repair. No scientific arithmetic, active profile or historical failure was changed, and no 32-path retry or GPU job ran.

## Relevance and limits

The evidence prevents mistaking incomplete residual measurements for an all-path accuracy result. The numerical cause, full residual sample, binary-backend integrability, native survival accuracy, practical O1 bounds and full O4 remain unresolved. A future discrepancy should be diagnosed from its now-retained values before changing arithmetic or relaxing parity. See [[Staged hierarchy formation and RG composability]] and [[Gauge-Theoretic Multi-Agent VFE Model]].
