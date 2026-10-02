---
type: run
title: "MultiAgentELBO joint retained parents and stationary protocol, October 2, 2026"
aliases: ["Joint retained renormalization checkpoint"]
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
year: 2026
created: 2026-10-02
---

# Joint retained parents and the stationary protocol limit

> [!info] Citation
> MultiAgentELBO project (2026). *Joint configuration/assignment parent comparison and the final stationary comparison for the fixed-energy saddle protocol*. Code base b1144767755689b15a1e6b1750d2bc408965edc1; Research base f3be90c53763d4a1a11960321fc8e277570efdd5. Executed source snapshots, parameters and inputs are archived alongside this note. This continues [[multiagentelbo-2026-10-02-renormalization-studies]] and [[multiagentelbo-2026-10-02-saddle-handoff]].

## Joint retained experiment

The new sampler retains source assignments at every microstep, in addition to configurations. The source transition is one whole-network hold atom plus one product redraw, including refreshes to the old complete assignment. Four normalized scheduled parents combine recognition or lifted pointwise source rows with recognition-weighted or assignment-aware configuration drifts. The lift is the Gaussian activation conditional mean given the observed block means, held as a formula through the study. It is not the actual evolving hidden conditional law.

A conditional relative-entropy decomposition shows that the expected source log ratio plus the analytically integrated projected Gaussian row KL is retained joint-path KL plus a nonnegative candidate-independent information gap. Thus paired scores compare actual joint-path KL; their absolute values are upper-functional estimates, not absolute retained-path divergences or confidence certificates.

One CPU float64 run used the archived activation and learning schedule, N=512 and 1,024, K=2, 1,024 paths per network, 64 microsteps over horizon one, and blocks of 16/32/64. It passed finite-score, curvature and projection gates in 211.978564 seconds. Eighteen tiny mechanical checks passed in two disjoint packets: five new source/history checks and thirteen joint/predecessor checks. Initial RED and test-oracle dtype failures are retained separately.

After the first source contrast was observed, a fixed-activation-mean pointwise control was scored on the saved paths, without resampling or learning. Most of the apparent lifted-versus-recognition gain was already present in that control: 4.480715 +/- 0.295433 and 9.528724 +/- 0.487509 nats per path. At block 16, adding actual block fluctuations improves the score by a further 0.577510 +/- 0.065896 and 1.192004 +/- 0.095668. All uncertainties are empirical paired standard errors. This posthoc distinction prevents attributing the full contrast to observed configurations.

Simply using observed assignments in the configuration drift at this static lift worsens scores by 0.145052 +/- 0.022226 and 0.389434 +/- 0.038465 nats at block 16. This is a limitation of the candidate formula, not of the optimal assignment-aware predictor. The retained source state grows with N, the parameters remain supplied law-level controls, and neither continuous-time closure nor endogenous structural feedback is established.

## Final stationary comparison for the saddle candidate

The third and final bounded candidate round proves that one fixed smooth low-well initialization and the stationary initialization have asymptotically identical distributions for the declared capped post-entrance outcomes. A strongly convex comparison energy agrees with the original in the low strip. Synchronous contraction and a bounded-control total-variation smoothing estimate give local mixing on logarithmic time, while an exponential radial estimate makes early escape negligible. The stationary densities agree conditionally in the strip and concentrate there. Applying the same future stopped-protocol kernel therefore eliminates every limiting probability surplus for this admissible initial law.

The conclusion includes the declared first-stage, future-window and joint indicators, but excludes absolute waiting times and the initial path prefix. Actual repeated searches for the same local motif give a stationary mean completion bound of order exp(C_N/T), shorter than the chosen full horizon exp(2C_N/T). The entrance convention is explicit; a horizon started only after a selected handoff is a different comparison.

This refutes the existing protocol's every-initial-law probability-surplus route. It preserves the conditional high-versus-low facilitation and restoring estimates from [[multiagentelbo-2026-10-02-saddle-handoff]]. It is a fixed-N analytical result for each allowed even N>=512, not a general no-go theorem for the hierarchy program. The three-round candidate loop stops here.

## Relevance to this research

[[Staged hierarchy formation and RG composability]] and [[Gauge-Theoretic Multi-Agent VFE Model]] now distinguish a joint retained predictor baseline from actual parent closure, and conditional facilitation from a matched stationary formation criterion. The next parent increment needs hidden-state conditioning on both configurations and assignments, with an actual-law approximation budget. Intrinsic selection, interacting structural-law coherence and feedback remain unresolved for general recursive formation.

The immutable archive is sources/archives/multiagentelbo-2026-10-02-joint-retained-parent/. Raw research Markdown uses .md.txt to avoid wiki identity collisions. Complete projected paths remain in the canonical code checkout under artifacts/gaussian-joint-parent/20261002T161127396348Z/; portable assignments, scores, source snapshots, runtime metadata, JUnit and the posthoc control accompany the archive. The active neighborhood profile and manuscripts were unchanged. CUDA was available but occupied at the preflight; this increment used CPU only.
