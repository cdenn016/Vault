---
type: concept
title: Conformist transmission
aliases: ["Frequency-dependent bias", "Conformist bias", "Conformity bias (cultural evolution)"]
tags:
  - cluster/social-physics
  - cluster/social-physics/evolutionary-and-cultural
  - project/social-physics
status: draft
created: 2026-06-19
updated: 2026-06-19
---

# Conformist transmission

## What it is

**Conformist transmission** is the frequency-dependent social-learning bias in which a cultural variant is adopted at a *greater-than-proportional* rate when it is common. It is one of the three families of transmission bias in Boyd and Richerson's dual-inheritance theory — alongside *content (direct) bias*, which evaluates variants on their intrinsic merit, and *model-based (prestige) bias*, which copies whoever displays a marker of success — and is the canonical case of *frequency-dependent bias*, where the probability of adopting a variant depends nonlinearly on how common it is among the models a learner samples ([[boyd-richerson-1985-culture-evolutionary-process]], [[richerson-boyd-2005-not-by-genes-alone]]). The contrast that defines it is sharp: an *unbiased* learner who samples $n$ models and adopts a variant present at frequency $p$ does so with probability exactly $p$ — the linear, DeGroot-style rule of proportional copying — whereas a *conformist* learner over-weights the majority, adopting a common variant more often than its frequency warrants and a rare one less often ([[henrich-boyd-1998-conformist-transmission]]). It sits within the broader program of [[Cultural evolution and social learning]], which treats socially transmitted information as a Darwinian inheritance system exhibiting variation, selection, and inheritance ([[mesoudi-2011-cultural-evolution]]), and it is the cultural-evolution name for the "copy-the-majority" strategy in Laland's "when/whom to copy" taxonomy of conditional social-learning rules ([[laland-2004-social-learning-strategies]]).

## The cubic adoption rule and within-group bistability

The formal signature of conformity is a cubic adoption rule. Writing $p$ for the frequency of a variant among the sampled models, the conformist adoption probability is
$$
p' = p + D\,p(1-p)(2p-1), \qquad D > 0,
$$
where $D$ is the strength of the conformist bias ([[henrich-boyd-1998-conformist-transmission]], [[boyd-richerson-1985-culture-evolutionary-process]]). The correction term $D\,p(1-p)(2p-1)$ is positive when the variant is in the majority ($p > 1/2$) and negative when it is in the minority ($p < 1/2$), so adoption is pushed above the proportional baseline for common variants and below it for rare ones. This rule has stable fixed points at $p = 0$ and $p = 1$ and an unstable interior equilibrium at $p = 1/2$, making the within-group dynamics **bistable**: any initial majority, however slight, is amplified across iterations until the variant reaches fixation or extinction. This is precisely the nonlinearity that no purely linear averaging model can produce — linear (DeGroot-style) consensus dynamics are contractive and drive a population toward a single weighted mean, whereas the cubic rule breaks that contractivity and creates two competing basins of attraction.

Henrich and Boyd ([[henrich-boyd-1998-conformist-transmission]]) place this bias on an adaptive footing: natural selection on social-learning psychology favors a conformist tendency across a broad range of conditions, particularly when the environment varies in space and individual (asocial) learning is costly or error-prone, because copying the local majority is a cheap and reliable way to acquire locally adaptive behavior. The bias is adaptive at the individual level, but it has a striking population-level consequence. Within a group, conformity is a homogenizing force that drives every group toward one consensus or the other. Between groups, it counteracts the mixing effect of migration: because each group is pulled toward fixation on whichever variant happens to be locally common, conformist transmission *maintains stable cultural differences between groups* even in the face of inter-group migration that would otherwise erode them. This persistent inter-group variance is the raw material on which cultural group selection can act — a precondition Henrich and Boyd emphasize ([[henrich-boyd-1998-conformist-transmission]], [[richerson-boyd-2005-not-by-genes-alone]]). Empirically the picture is more nuanced than the clean model: experimental audits find robust support for state-dependent reliance on social information but only *partial* support for strict frequency-dependent conformity, so the cubic rule is best read as the idealized formal mechanism rather than a universally confirmed behavioral law ([[laland-2004-social-learning-strategies]]).

## Relevance to this research

Conformist transmission is the cleanest cultural-evolution statement of the nonlinearity that separates genuine social influence from linear consensus, and it specifies exactly what a population-level [[Multi-agent variational free energy|VFE]] model of belief must be able to reproduce. The [[Statistical physics of social systems and collective behavior|SocialPhysics]] program (founded on [[belief-inertia]]) shows that a large fraction of opinion-dynamics models are the *overdamped limit* of gradient flow on a multi-agent free-energy functional, with inter-agent disagreement carried by the gauge-transported divergence $\mathrm{KL}(q_i \,\|\, \Omega_{ij}[q_j])$ between Gaussian beliefs weighted by softmax attention $\beta_{ij}$. Under uniform coupling this flow is contractive and reproduces DeGroot averaging and Friedkin–Johnsen anchoring — the *linear* baseline that conformity is defined against ([[Opinion dynamics]]). The cubic adoption rule is the term that breaks this contractivity: its bistable structure, with stable fixity at $p = 0, 1$ and an unstable interior at $p = 1/2$, is precisely what the coupling kernel must produce to generate metastable, separated belief basins rather than a single global consensus — the mechanism behind [[Echo chambers and polarization]]. In the gauge-theoretic functional this maps onto a regime where the attention kernel $\beta_{ij}$ over-weights agreement with the local majority, a majority-amplifying weighting that turns the smooth averaging flow into a tipping dynamics with two consensus attractors.

The relevance is therefore *specificational* rather than a literal import: the cubic rule is not a term the functional currently derives, but a target behavior the coupling kernel ought to recover under the right (majority-amplifying) weighting, just as uniform coupling gives averaging and status-weighted $\beta_{ij}$ gives prestige bias ([[boyd-richerson-1985-culture-evolutionary-process]], [[laland-2004-social-learning-strategies]]). It connects naturally to [[Belief inertia]]: where the cubic rule produces bistability through a per-generation frequency nonlinearity, the belief-inertia program produces metastability and resistance to averaging through strong prior self-coupling $\alpha\,\mathrm{KL}(q_i \,\|\, p_i)$ and, in its underdamped extension, through inertial mass — distinct mechanisms that share the goal of explaining how stable, separated belief clusters survive the homogenizing pull of social coupling. The deeper anthropological motivation — that conformity sustains the between-group variance needed for cultural group selection — is framing-level support for [[Meta-agents and hierarchical emergence]] and [[Collective active inference]], where coupled belief-updating yields stable group-level structure no single agent holds.

## Sources

- [[henrich-boyd-1998-conformist-transmission]] — formal model showing selection favors conformist bias; the cubic adoption rule $p' = p + D\,p(1-p)(2p-1)$, its bistability, and the maintenance of stable between-group differences for cultural group selection.
- [[boyd-richerson-1985-culture-evolutionary-process]] — dual-inheritance theory in recursion-equation form; the content/conformist/prestige bias taxonomy and the conformist sigmoid as the nonlinearity distinguishing social influence from linear averaging.
- [[richerson-boyd-2005-not-by-genes-alone]] — prose synthesis; why frequency-dependent (conformist) bias is adaptive and how conformity plus limited migration sustains between-group differences.
- [[mesoudi-2011-cultural-evolution]] — textbook map of the field; conformist transmission within the Darwinian-triad framing and the transmission-chain experimental paradigm.
- [[laland-2004-social-learning-strategies]] — the "copy-the-majority" strategy and its place in the "when/whom to copy" taxonomy of conditional social-learning rules.

## See also

- [[Cultural evolution and social learning]] — the parent concept; the full bias taxonomy and transmission-channel models.
- [[Social influence and conformity]] — the social-psychology evidence base (Asch, Sherif) for majority pressure on beliefs.
- [[Multi-agent variational free energy]] · [[belief-inertia]] · [[SocialPhysics]] — the functional and program whose coupling kernel must reproduce the conformist nonlinearity.
- [[Echo chambers and polarization]] · [[Discrete spin and majority-rule models of opinion]] — the bistable, majority-amplifying regime in opinion space.
- [[Opinion dynamics]] · [[Statistical physics of social systems and collective behavior]] — the linear (DeGroot) baseline conformity is defined against, and the surrounding map.
