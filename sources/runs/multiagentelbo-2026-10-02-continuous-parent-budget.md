---
type: run
title: "MultiAgentELBO frozen parent budget failed run, October 2, 2026"
aliases: ["Frozen parent budget Cholesky failure"]
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
year: 2026
created: 2026-10-02
---

# Frozen parent budget failed run

> [!info] Citation
> MultiAgentELBO project (2026). *Frozen parent budget failed run*. Execution metadata records code base 96c1bc4ca7f9f24548792a0b847cac2bd4faeffc, with working-tree edits captured in source.zip. The exact contract, local discretization record, failed-run report, numerical-failure note, activation inputs, twenty-five retained path files, metadata, terminal record, log and focused JUnit evidence are retained in sources/archives/multiagentelbo-2026-10-02-continuous-parent-budget/. No publication revision is inferred from the execution base. This follows [[multiagentelbo-2026-10-02-source-adapted-gaussian]].

## Terminal failure and retained outputs

The declared CPU study failed and the parent exited with code one after 2234.792734 seconds. It retained all sixteen N512 path files and nine N1024 path files, with N1024 indices 0 through 7 and 9. The N512 runner case is computationally complete; the N1024 case and overall study are incomplete. These are recorded output counts, not a claim that every other submitted worker task returned no internal calculation.

The terminal traceback reaches observe_gaussian at gaussian_message.py line 77 through _run_grid at continuous_budget.py line 112. Cholesky factorization of projected_covariance fails because leading minor 72 is not positive definite. This is a numerical failure in the declared conditional-Gaussian calculation, not a completed passing budget study. No N1024 sample mean or complete sixteen-path summary is constructed from the nine retained outputs.

Separately, the completed N1024 path001 reports fine covariance-fiber residual 1.870831516263757e-07, above the proposed absolute acceptance tolerance 1e-8. That retained instrumentation documents a conditional-fiber error; it does not identify which failed worker path caused the terminal Cholesky exception or establish their causal relation. Covariance histories and local condition numbers were not retained, so root cause and resulting score bias are unresolved. The [archived numerical-failure note](../archives/multiagentelbo-2026-10-02-continuous-parent-budget/continuous-budget-numerical-failure.md.txt) records the diagnosis and its limits.

The full-result checker was not executed because its contract requires a completed passing run. No budget-accounting reconstruction was run. The partial path arrays and reported N512 summaries remain diagnostic outputs without full-result validation. Neither the failed run nor the earlier path001 residual was replaced by a retry, and no tolerance was relaxed.

## Declared experiment and bounded preflight

The failed study froze the archived activation means, node covariances, source priors and independent GL+(2,R) links on cycle/stride-17 source rows. Its profile has K=2, link scale 0.2, tau=0.5, diffusion covariance Q=2M with mobility equal to the activation covariance, and arithmetic retained blocks of 16 agents. A product-Gaussian initial configuration is drawn independently of product-prior source labels. There is no later learning or structural schedule. These are the declared inputs, not evidence that the evolved conditional covariance stayed valid.

One model per size uses model seed 20261002; sixteen independent paths per size were planned over horizon 1.0. Path seed 20261007+100000*size_index+10*path_index supplies six random streams. The coarse/fine maximum steps are 1/64 and 1/128, with shared proposal times, summed Brownian increments, proposal uniforms and budget-probe uniforms. Each path has 2 uniform-time source probes. The failed study's partial data does not support an across-model conclusion or a complete two-size budget comparison.

Seven distinct tiny CPU checks passed in three disjoint final JUnit packets totaling 2.880 seconds. They ground exact-enumeration source costs, shared tapes, local correlated-noise coefficients and spawned runner wiring. They did not establish the conditional-covariance requirement at the study's scale. Both the historical preflight RED and the terminal large-run failure are preserved; small validation examples do not set the theory's direction.

## Continuous limit and remaining obligations

The local forecast/conditioning expansion matches continuous correlated-noise gain and Riccati coefficients. It does not prove global path-law or budget convergence, and it does not erase this numerical failure. Mesh subdivisions at invisible self-proposals can affect a finite-grid message even when no self-label is assimilated; the continuous retained-history regular filter does not use those invisible times. Disappearance of that numerical dependence in a limit remains unproved.

The target is the actual-law integral of projected drift error plus visible-intensity divergence including survival compensation. The failed execution supplies no accepted estimate of that continuous budget, retained-path KL or confidence upper bound. The partial outputs are not used to assess source-cost dominance. A numerical diagnosis and discriminating validation precede any further study; uniform small-error control, growing-horizon behavior, endogenous structural feedback and intrinsic recursive formation remain open. O1 and O4 are not closed. No GPU, full suite, historical heavy node, active run_lab profile change, base transport or manuscript edit was used.

## Relevance to this research

[[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]] retain this checkpoint as a failed numerical experiment with preserved partial evidence. [[Mathematics MOC]] and [[Statistics MOC]] distinguish seven passing tiny checks from the failed larger run and its unvalidated partial outputs. The completed predecessor's saved-path comparison keeps its separate scope.
