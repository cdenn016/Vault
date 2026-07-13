---
type: concept
title: Social Impact Theory
aliases:
  - "Latané social impact"
  - "Sublinear social influence law"
  - "Division of impact"
  - "Power Law"
  - "Diffusion of Responsibility"
  - "Social Loafing"
tags:
  - cluster/social-physics
  - cluster/social-physics/social-influence
  - project/social-physics
status: stable
created: 2026-06-19
updated: 2026-07-13
---

# Social Impact Theory

## What it is

**Social Impact Theory** is Bibb Latané's quantitative ansatz that the total influence a population of other people exerts on a target individual is a *multiplicative* function of three properties of that source population: its **strength** (status, power, persuasiveness, credibility), its **immediacy** (closeness in space and time, the absence of intervening barriers), and its **number** ([[latane1981psychology|latane-1981-social-impact]]). Written compactly, the impact on a target is $I = f(S, I_m, N)$, by deliberate analogy with physical field laws in which an effect intensifies with the magnitude, proximity, and multiplicity of its sources — a "social force field" sourced by an aggregate of others and decaying with social distance. The theory's project is to fold a heterogeneous catalogue of social-psychological phenomena — conformity, persuasion, stage fright, bystander intervention, social loafing — into this single parameterized law, and in doing so it became one of the canonical formal models the [[Statistical physics of social systems and collective behavior]] tradition later carried forward into spatial, dynamical lattice models of [[Opinion dynamics|opinion formation]]. It sits inside the broader [[Social influence and conformity]] literature as the specifically *quantitative* (rather than mechanistic) statement of how much, not why, others move us.

## The mechanism — a sublinear power law, run in both directions

The distinctive empirical claim is the **number** term: impact does not grow linearly with the size of the source population but scales *sublinearly* as a power law,
$$
I \;\propto\; S \cdot I_m \cdot N^{t}, \qquad t < 1,
$$
so the marginal effect of the $N$th additional person is smaller than that of the $(N-1)$th — a "psychosocial law" of diminishing returns that mirrors the compression of subjective intensity in psychophysical power laws ([[latane1981psychology|latane-1981-social-impact]]). This sublinear saturation is exactly the shape the conformity data take: Asch's line-judgment experiments showed conformity rising as a unanimous majority grows from one to three or four confederates and then *plateauing*, with further additions adding little ([[asch-1955-opinions-and-social-pressure]]), and Bond and Smith's meta-analysis of 133 line-judgment studies across 17 countries confirmed the dependence on majority size $N$ is monotonic but saturating, with diminishing returns past three or four ([[bond-smith-1996-culture-and-conformity]]). The same meta-analysis supplies a reading of the **strength** factor as culturally modulated: conformity is reliably higher in collectivist than individualist cultures, so the value a society places on group harmony scales the effective normative pressure a source carries ([[bond-smith-1996-culture-and-conformity]]).

The theory is deliberately two-sided, and the second side is the **division of impact**. Run the same multiplicative law in reverse: when many *targets* jointly receive impact from a single source, the impact is divided among them, so the load borne by each falls as the number of co-targets rises. This division principle is what grounds **diffusion of responsibility** (the bystander effect — each onlooker feels less compelled to act as the crowd grows) and **social loafing** (individual effort slackening in larger groups) ([[latane1981psychology|latane-1981-social-impact]]). Strength, immediacy, and number thus govern both how impact accumulates on a lone target and how it dilutes across a shared one — a single law with a dual.

## Relevance to this research

The current theorem-first record [[belief-inertia-2026-07-12-theorem-first-revision]] treats this relationship as **interpretive only**. The gauge-VFE relational force contains source precision, transported discrepancy, and attention weights, so strength and immediacy have loose geometric analogs. But each attention row is normalized: adding sources redistributes a fixed attention budget unless an independent raw exposure strength is changed. It therefore does not derive Latané's increasing-number law, the sublinear $N^t$ law, or the multiplicative strength--immediacy--number form.

Recovering the number law would require an unnormalized exposure-intensity term or another explicit dependence of the total social strength $\lambda_s$ on source count. The division-of-impact phenomena likewise require target-level behavioral variables absent from the current belief-state model. The local loss Hessian is stiffness, not latency: at fixed Fisher geometry and learning rate, larger positive stiffness reduces matched-force displacement and speeds linear relaxation. Any slower response, coasting, overshoot, or resonance requires a separately specified mobility, damping law, kinetic metric, or slow state. Social Impact Theory is therefore a comparison and empirical benchmark, not a force law or underdamped limit already recovered by [[Multi-agent variational free energy]].

## Sources

- [[latane1981psychology|latane-1981-social-impact]] — Latané's foundational statement of Social Impact Theory: impact as a multiplicative function $I = f(S, I_m, N)$ of source strength, immediacy, and number; the sublinear power law $I \propto N^{t}$ with $t<1$; and the dual division-of-impact principle grounding diffusion of responsibility and social loafing.
- [[asch-1955-opinions-and-social-pressure]] — line-judgment conformity rising with majority size to three or four and then plateauing, the empirical signature of the saturating number term.
- [[bond-smith-1996-culture-and-conformity]] — meta-analysis of 133 Asch studies across 17 countries: monotonic-but-saturating dependence of conformity on majority size $N$, and the collectivist/individualist moderator scaling effective source strength.

## See also

- [[Social influence and conformity]] — the broader conformity literature (Sherif, Asch, Deutsch–Gerard, French) of which this is the quantitative law.
- [[Opinion dynamics]] · [[Sociophysics]] · [[Statistical physics of social systems and collective behavior]] — the dynamical/lattice descendants of the impact law.
- [[Multi-agent variational free energy]] — the functional whose normalized coupling permits only an interpretive comparison unless raw exposure intensity is added.
- [[Belief inertia]] · [[Mass as Fisher information]] · [[Hamiltonian belief dynamics]] — the separately conditional kinetic extension and its scope limits.
- [[Fisher information metric]] · [[Agents as fibre-bundle sections]] · [[Gauge transformation]] — the relational geometry generalizing the scalar impact field.
- [[Echo chambers and polarization]] · [[Bounded confidence]] — the bounded, distance-weighted-impact regime.
