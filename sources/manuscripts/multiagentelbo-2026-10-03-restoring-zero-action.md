---
type: manuscript
title: "MultiAgentELBO restoring coherence with zero stationary action, October 3, 2026"
aliases: ["Restoring zero-action recognition mechanism"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/vfe, cluster/info-geometry, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-03
---

# Restoring coherence with zero stationary action

> [!info] Citation
> MultiAgentELBO project (2026). *Restoring coherence with zero stationary action*. Code commit [88960dc](https://github.com/cdenn016/MultiAgentELBO/commit/88960dc80feeacec57ac100903f2391abcf0e514), [PR120](https://github.com/cdenn016/MultiAgentELBO/pull/120). The [immutable derivation](../archives/multiagentelbo-2026-10-03-restoring-zero-action/restoring-zero-action.md.txt) and [symbolic checks](../archives/multiagentelbo-2026-10-03-restoring-zero-action/restoring-zero-action-checks.json) preserve the committed source bytes.

## Result and introduced model

This continues the necessary-condition argument in [[multiagentelbo-2026-10-03-probe-variance-stationary-action]]. That argument excludes universal success when a matched full event has positive stationary action. Its former Gaussian boundary example supplied only surviving displacement. The new construction proves compatibility of zero action with actual transverse restoration and a stationary probability surplus for coherence itself.

The introduced recognition domain is the compact ball |u|^2+|v|^2<=1, with two equal-dimensional blocks in R^D. D is arbitrary and fixed, including D>=512. These blocks are not automatically a network of gauge agents. The energy is E=|u|^2|v|^2/2. A regular recognition family Q_z=N(m(z),I), with sine-cosine pairs for each u and v coordinate and additional means u_i v_j, has exact KL to N(0,I) equal to D+E. Its Fisher metric is G=I+J^T J, where J differentiates u tensor v; its eigenvalues lie in [1,2] on the domain. The positive free-energy offset is a restriction gap, not a dropped normalization term.

The diffusion has generator T Delta_G minus the Fisher natural gradient of E, with G-normal reflection. Its stationary density is proportional to exp(-E/T)sqrt(det G). All model and metric coefficients are temperature independent. The coordinate Ito correction is retained. The interaction is supplied by the curved recognition family; this is not an interacting gauge-network realization or an intrinsic generative hierarchy.

## Persistence and matched stationarity

For 0<a<1/4 and 1/4<b<1/2-a, let the coherence resolution be r_T=T^b, the winner threshold be T^a, and the observation window begin at h_T=log^2(1/T). From every fixed absolutely continuous initial law, the event that one block stays above the winner threshold while the other stays below the coherence resolution throughout any fixed-duration window has probability tending to one. The proof localizes the initial squared-radius gap and boundary distance, controls the actual gap martingale, and applies a killed-process contraction estimate. It includes joint motion of the restoring coordinate.

The actual restoring rate times r_T^2/T tends to infinity. Radial integration gives stationary normalization proportional to T^(D/2)log(1/T), at fixed D. The corresponding one-time stationary event probability tends to 4a. Plain coherence, defined only by min(|u|,|v|)<=r_T, has stationary probability tending to 2-4b. Thus the same full observation protocol has stationary probability deficits at least 1-4a and 4b-1 respectively. The persistent-window stationary probability is also bounded below by a positive fixed-D constant divided by log(1/T); its stationary action tends to zero. No entrance rate is inferred from occupation.

## Relevance and unresolved obligations

For [[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]], this rules out extending the prior positive-action obstruction to all restoring episodes solely by adding a restoring requirement. The example is a sharply scoped compatibility construction. A bilinear likelihood averaged over independent nondegenerate Gaussian latents instead adds positive variance-dependent mass terms; those cannot be dropped to recover the valleys in an existing model.

There is no first-stage formation event, actual positive-weight nonformation handoff, or second-stage facilitation comparison. Two contraction thresholds do not establish R14 recursion. A coordinate-dependent partition catalog, interacting noncommuting links, transported law coherence and separated parent-child feedback remain unconstructed. The constants are not uniform in D and can be large; no useful temperature threshold at D=512 or joint size/temperature theorem follows. O4 remains open, as do practical parent accuracy and resource control. This result does not authorize a new GPU experiment.

## Evidence and scope

Separate constructive stationary and dynamical calculations were reconstructed against the exact event and natural metric. Exact symbolic checks returned zero residual for the radial determinant, natural-gradient identity, characteristic polynomial and equality of the two radial interaction drifts. Document checks covered 24 equation tags, local links, delimiters and whitespace. These checks accompany the written proof; they are not a model simulation or a formal-verification certificate. No production code, active profile, GPU calculation, historical heavy node, theory manuscript or previous immutable source was changed or run.

## BibTeX

    @misc{multiagentelbo2026restoringzeroaction,
      author = {{MultiAgentELBO project}},
      title = {Restoring Coherence with Zero Stationary Action},
      year = {2026},
      howpublished = {Research records, MultiAgentELBO commit 88960dc},
      url = {https://github.com/cdenn016/MultiAgentELBO/commit/88960dc80feeacec57ac100903f2391abcf0e514}
    }
