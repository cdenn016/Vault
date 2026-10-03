---
type: manuscript
title: "MultiAgentELBO entropic GL dynamics and stationary scale law, October 3, 2026"
aliases: ["GL amplitude entropic time scale"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/vfe, cluster/info-geometry, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-03
---

# Entropic GL dynamics and stationary scale law

> [!info] Citation
> MultiAgentELBO project (2026). *The entropic time scale of the shared-amplitude GL model*. Code commit [0c2f8d3](https://github.com/cdenn016/MultiAgentELBO/commit/0c2f8d3278078ab56de916078f2bdcce2410419f), [PR122](https://github.com/cdenn016/MultiAgentELBO/pull/122). The [immutable derivation](../archives/multiagentelbo-2026-10-03-entropic-time-scale/entropic-time-scale.md.txt) and [symbolic checks](../archives/multiagentelbo-2026-10-03-entropic-time-scale/entropic-time-scale-checks.json) preserve committed source bytes.

## Continuity and model

This concludes the third round of the bounded investigation begun in [[multiagentelbo-2026-10-03-restoring-zero-action]] and continued in [[multiagentelbo-2026-10-03-gated-handoff-obstruction]]. It treats the introduced normalized configuration model E=|a|^2 Q_Theta(x)/2, where Q_Theta(x)=x^T A_Theta x is the mismatch of a connected GL network in a compact uniformly coercive chart. Matter dimension n=NK permits every fixed N>=512; amplitude dimension m is declared separately. All constants may depend on network size. No thermodynamic limit or complete hierarchy admission follows.

The live sources include c08's envelope, reduced-flow and noninvariance clauses, c12's persistent-hierarchy problem, c13's configuration-law free energy, SPEC R14–R15, the Meta-agents and hierarchical emergence wiki concept, and PIFB2's current information-clock module. Pavliotis and Stuart's primary averaging notes, Chapter 10 and Remark 10.2, supply methodological context; the model-specific proof is written in the archived record. Slow time tau=Tt is an analysis of the declared diffusion, not a physical-clock or RG-scale identification.

## Exact stationary elimination

On the declared fixed product integration domains and smooth positive prior density f, the amplitude integral J_T(x,Theta) gives the exact retained stationary density J_T/Z_T and the conditional amplitude law. For a flat amplitude prior it has an incomplete-gamma formula. Away from zero mismatch its asymptotic factor is (2 pi T)^(m/2) f(0,x,Theta) Q^(-m/2). The exact force remains finite at Q=0; the singular reciprocal-Q term belongs to an outer approximation.

At m=n=d the normalizer is (2 pi T)^(d/2) log(1/T) W/2+O(T^(d/2)), with W equal to the sphere area times the integral of f(0,0,Theta) det(A_Theta)^(-1/2). The transformed stationary law of negative log matter radius divided by log(1/T) converges in total variation to a uniform law on [0,1/2], independently of a nontrivial limiting angle/link distribution. Link determinants and angular weights are retained. In particular, the one-time stationary mismatch probability P(Q<=T^(2b)) tends to 1-2b for 0<b<1/2. This is not a window or entrance-rate estimate.

For m<n the formal weight is integrable and gives a normalized retained limit. For m=n it has a logarithmic divergence. For m>n the matter scale sqrt(T) and an amplitude-dependent Gaussian mixture give the appropriate limit. These dimension cases diagnose the introduced amplitude choice; they do not change the user's model specification.

## Actual local dynamics and initial slip

In a constant-prior neighborhood with Q bounded below, the declared slow mobility B=diag(A_Theta^(-1),M_Theta) includes the GL metric and its coordinate divergence. After rescaling a=sqrt(T)b and tau=Tt, the frozen b process is Ornstein-Uhlenbeck with second moment m/Q. The resulting slow generator is Q^(m/2) div(Q^(-m/2) B grad). Matter and links therefore retain an entropic drift rather than following the zero-temperature minimum E=0.

An explicit quadratic Poisson corrector controls the integrated averaging error. The proof includes a separate path-supremum bound and requires only vanishing initial fourth amplitude moment. It yields weak convergence of stopped slow paths on bounded slow horizons. Thermally prepared amplitudes give an O(sqrt(T)) bound for the integrated coefficient error, not an asserted global path-TV rate.

For a specified compact class of fixed initial densities whose deterministic slip trajectories stay inside the coercive tube, the actual initial shift is computed using accumulated amplitude ell: dZ/dell=-h(Z), ending when twice the integral of Q reaches the initial squared amplitude. A physical burn time sqrt(log(1/T)) converges to that pushed-forward initial law and makes the amplitude fourth moment vanish. The subsequent local slow limit uses the actual process, without a reset. The restriction to this slip basin is explicit; the every-initial-density formation requirement remains open.

## Boundary and remaining work

At the balanced scaling a=T^(1/4)alpha, x=T^(1/4)xi and sigma=sqrt(T)t, both blocks remain active in the leading generator, while links move at higher order on bounded inner intervals. This is coefficient scaling, not a solved crossing or return law. The outer approximation cannot be extended through Q=0 by declaring its nonnormalizable weight stationary.

All three rounds are now used. The remaining obligation is to match the actual outer and inner laws, cover the required initial laws, and establish the full R14/R15 handoff and stationary comparison. Intrinsic partitions, consistent hierarchical feedback and practical O1 accuracy/complexity remain open. Exact symbolic corrector/exponent algebra passed; no simulation, GPU calculation, production test or active configuration change occurred.
