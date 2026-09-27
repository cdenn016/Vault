---
type: manuscript
title: "MultiAgentELBO joint temperature and mobility selection, September 26, 2026"
aliases: ["MultiAgentELBO joint selection schedule"]
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/mathematics]
created: 2026-09-26
---

# Joint temperature and mobility selection

This local result continues [[multiagentelbo-2026-09-26-selection-and-reference-review]]. Its source snapshots are archived in `sources/archives/multiagentelbo-2026-09-26-joint-temperature/`: the two new manuscript proofs, the chapter statement, two constructive derivations and the independent proof check. The repository keeps the asset hashes in `docs/derivations/2026-09-26-selection-to-formation/stage1-vault-manifest.json`.

For the unchanged homogeneous scalar shared-link four-cycle at one base point, the full frozen entropy-production rate is at least c T^(5/2)/[4+3 log(1/T)+8 log(1/p_min)], with an explicit positive constant c, for 0<T<=1/100. The proof includes the passive Gaussian factor. It gives actual-law one-time tracking when epsilon_L=T^a with a>7/2, uniformly on the logarithmic learning window and bounded sets of initial means. This sufficient tracking condition does not establish branch selection on that power law.

For any sequence of admissible positive temperatures T_n tending to zero and any positive error tolerances tending to zero, deterministic mobility thresholds d_n exist, common to Lebesgue-almost every fixed initial Gaussian mean. Every epsilon_L<=d_n eventually gives the selected matching Gaussian one-time law, vanishing learned entropy to its instantaneous invariant law, and frozen entropy to the uniform-row invariant law, uniformly on [2 epsilon_L^-1 log(1/epsilon_L),4 epsilon_L^-1 log(1/epsilon_L)]. The proof uses the fixed-temperature theorem, a common window constant, continuous explicit entropy majorants, and summable exceptional sets. The mean-space Gaussian measure is a proof device, not a change of preparation. The learned/frozen assignment-law total-variation distance tends to one half.

The thresholds are mathematical existence thresholds, not a computed power law. The matching can vary with n. A quantitative fixed-mean small-temperature imprint estimate is still needed for power-law selection, and eventual sign control is needed for a fixed limiting matching. Neither first coherent-block formation nor parent path-law closure follows from this result. The separate source documents retain those obligations.

No new external mathematical source is required: all new bounds are derived in the archived local proofs from the previously established model. The research used Exa Agent at ultra effort, but generated output is a research lead and is not proof authority. See [[exa-2026-agent-create-run]] for the archived API-setting documentation.

Related synthesis: [[Staged hierarchy formation and RG composability]], [[Gauge-Theoretic Multi-Agent VFE Model]], and [[Geometric singular perturbation theory]].