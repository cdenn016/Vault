---
type: manuscript
title: "MultiAgentELBO limits of gated formation extensions, October 3, 2026"
aliases: ["Gated formation handoff obstruction"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/vfe, cluster/info-geometry, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-03
---

# Limits of gated formation extensions

> [!info] Citation
> MultiAgentELBO project (2026). *Limits of the gated formation extensions*. Code commit [91c2d44](https://github.com/cdenn016/MultiAgentELBO/commit/91c2d44aa7906d651663eb42d70ab84abf53c957), [PR121](https://github.com/cdenn016/MultiAgentELBO/pull/121). The [immutable derivation](../archives/multiagentelbo-2026-10-03-gated-handoff-obstruction/gated-handoff-obstruction.md.txt) and [symbolic checks](../archives/multiagentelbo-2026-10-03-gated-handoff-obstruction/gated-handoff-obstruction-checks.json) preserve the committed source bytes.

## Continuity and scope

This is round 2 of the bounded investigation begun in [[multiagentelbo-2026-10-03-restoring-zero-action]]. The earlier restoring-coherence result remains intact. The extension attempts fail a different requirement: formation from every fixed initial density with actual R14 counterfactual handoffs. The new failures hold on horizons H_T=o(1/T), at fixed dimension and network size. They do not exclude longer protocols, other gates, intrinsic partition branching or O4 generally.

The live sources are SPEC R13–R15, c13's configuration-law and cycle-experiment definitions, c12's hierarchy problem and partition/global-VFE definitions, and the Gaussian supplement's Fisher conventions. A restricted recognition family Q_z with an exact KL is distinguished from a law q over configurations with scaled entropy T KL(q||p_0). Diffusing the recognition parameter does not itself establish full configuration-law admission.

## Handoff and slow-record failure

For an initial density supported on a fixed-gap branch of the preceding quartic valley, opposite-branch probability tends to zero on the declared horizons. Counting either orientation at the proved logarithmic handoff makes coherence asymptotically certain, so nonformation histories have vanishing probability. These particular handoff choices therefore fail R14's positive-weight comparison.

The slow-record extension has energy E=sr/2+kappa[y-g(r)]^2/2+lambda y^2|w|^2/2, with s=|u|^2, r=|v|^2 and a smooth gate g that vanishes above a fixed r threshold. An exact regular Gaussian-recognition realization supplies its full Fisher metric. In an open gate-off region the y coordinate decays, and its integrated square stays bounded. A fixed smooth initial density there leaves the later contrast |w| bounded away from zero with probability tending to one through every o(1/T) horizon. The proof uses stopped gap, boundary and logarithmic-radius martingale estimates for the actual diffusion. The enlarged model's stationary comparison remains unproved; it cannot inherit the earlier model's surplus.

## Normalized interacting GL configuration model

At every fixed N>=512 and K>=2, declare a connected network with independent dynamic GL links and comparisons r_e=x_j-Theta_e x_i. In a compact chart with no nonzero parallel section, Q_Theta(x)=sum r_e^T H_e r_e=x^T A_Theta x is uniformly positive definite. Two noncommuting cycle holonomies demonstrate local attainability; constants depend on network size. The small matrices ground that algebra only.

A proper configuration prior and normalized binary records with success probability exp[-|a|^2 r_e^T H_e r_e/(2T)]/2 give the exact posterior proportional to p_0 exp[-E/T], E=|a|^2 Q_Theta(x)/2. The graph, base forms, prior and mobility are fixed while the common thermal divisor is explicit. This observes configurations directly; it does not delete covariance terms from a different Gaussian-latent likelihood. The amplitude/matter choice is introduced, and a nondegenerate partition law is still absent.

The declared reversible mobility is diag(I_a,A_Theta^{-1},M_Theta), with the inverse of a smooth GL metric for links and all coordinate/prior corrections included. For a fixed smooth initial density with small amplitude but matter norm bounded away from zero, stopped Ito estimates show that amplitude decays before matter can relax. Matter mismatch stays bounded below with probability tending to one on o(1/T) horizons. Thus active noncommuting links alone do not repair this candidate's universal-initial-density failure. Existence of an admitted reflecting process and local coercivity are explicit assumptions; the proof stops inside that neighborhood.

An amplitude floor removes this branch but produces terminal stationary matter concentration above the thermal scale under the stated prior bounds. That one-time estimate gives no full-window, entrance-rate or recurrence claim.

## Evidence and remaining work

Exact SymPy checks establish the displayed radial Fisher solve, determinant and two-matrix holonomy algebra. They do not certify the stochastic estimates or constitute a large-network experiment. No simulation, production test, GPU job or active configuration change occurred. O1 practical accuracy/complexity and O4's full formation, partition and feedback requirements remain open. A continuation must provide actual nonformation handoffs from each fixed initial density and compare the same full protocol under stationarity.
