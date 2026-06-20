---
type: concept
title: Cultural group selection
aliases: ["Multilevel selection of culture", "Between-group cultural variance"]
tags:
  - cluster/social-physics
  - cluster/social-physics/evolutionary-and-cultural
  - project/social-physics
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Cultural group selection

## What it is

Cultural group selection is the multi-scale mechanism by which natural selection acts on whole groups as differentiated, heritable units rather than only on the individuals inside them. The classical objection to group selection is statistical: selection among groups can only matter if there is appreciable heritable variation *between* groups for it to act on, yet for most traits migration and within-group mixing erode between-group differences far faster than differential group success can build them up, so genetic group selection is usually a weak force. The thesis of the dual-inheritance program is that *culture* escapes this trap. Where genetic inheritance offers selection little purchase at the group level, the population dynamics of socially learned variants can manufacture and maintain exactly the kind of stable, group-level differences that a higher selective level requires ([[boyd-richerson-1985-culture-evolutionary-process]], [[richerson-boyd-2005-not-by-genes-alone]]). In Nowak's synthesis of the cooperation literature, group (multilevel) selection appears as one of the five canonical routes by which costly cooperation can be favored, alongside kin selection, direct and indirect reciprocity, and network reciprocity ([[nowak-2006-five-rules-cooperation]]).

The concept is the evolutionary route from coupled individual learning to a group-level adaptive unit, and it depends on two ingredients pulling against each other: a *within-group homogenizing* force strong enough to drive each group toward its own internal consensus, and *between-group* differentiation that this consensus, against limited migration, holds in place. It is the multi-scale companion to the broader survey of transmission biases in [[Cultural evolution and social learning]]; this page isolates the multilevel argument specifically.

## The mechanism: conformity manufactures the variance selection needs

The engine of within-group homogenization is **conformist transmission** — a frequency-dependent learning bias in which an individual sampling $n$ models adopts whichever variant is most common at a *greater-than-proportional* rate ([[henrich-boyd-1998-conformist-transmission]], [[boyd-richerson-1985-culture-evolutionary-process]]). Where an unbiased (DeGroot-like) learner adopts a variant at frequency $p$ with probability exactly $p$, a conformist adopts it with probability

$$
p' = p + D\,p(1-p)(2p-1), \qquad D > 0,
$$

a cubic rule with stable fixed points at $p=0$ and $p=1$ and an unstable interior equilibrium at $p=1/2$. This bistability is the crux: within a group, conformity amplifies any small majority to fixation, so each group is driven toward one or the other internal consensus rather than toward a blended global mean. Crucially, Henrich and Boyd show that this conformist psychology is itself adaptive across a wide range of conditions — particularly when environments vary in space and asocial (individual) learning is costly or error-prone — so it is favored by selection on the learning rule, not assumed ([[henrich-boyd-1998-conformist-transmission]]).

The multilevel payoff follows from setting this homogenizing force against migration. Migration tends to mix groups and wipe out between-group differences; conformist transmission pushes back, because an immigrant carrying a minority variant into a group is, on average, more likely to *adopt the local majority* than to convert locals to the import. The net effect is that conformity maintains persistent inter-group variation that linear imitation or unbiased copying would dissolve — it manufactures and preserves precisely the heritable group-level variance on which selection among groups can then operate ([[henrich-boyd-1998-conformist-transmission]], [[richerson-boyd-2005-not-by-genes-alone]]). Once such stable group differences exist, group-beneficial but individually costly variants — cooperative norms, institutions, prosocial practices — can spread by differential group success even when they are disfavored by selection *within* each group. Nowak frames the resulting condition compactly: with cooperation cost $c$, benefit $b$, group size $n$ and number of groups $m$, group selection favors cooperation roughly when $b/c > 1 + n/m$ — cooperation is easier to sustain when groups are small and numerous, i.e. when between-group variance is large relative to within-group variance ([[nowak-2006-five-rules-cooperation]]). This is the formal version of the program's larger empirical claim, that gene–culture coevolution — culture's capacity to sustain group-level adaptive units — is what scaffolded human-scale cooperation and the cumulative "collective brain" of an interconnected population ([[henrich-2016-secret-of-our-success]], [[richerson-boyd-2005-not-by-genes-alone]]).

## Relevance to this research

Cultural group selection is the cleanest evolutionary statement of a claim at the heart of the [[SocialPhysics]] program and the gauge-theoretic VFE picture: that a population of coupled, belief-carrying agents can become, at a coarser scale, a single adaptive unit. Its two-part mechanism maps directly onto the program's machinery. The within-group homogenizer is the conformist nonlinearity, whose bistable cubic $p' = p + D\,p(1-p)(2p-1)$ is exactly the frequency-dependent structure a coupling kernel must produce to *break the contractivity of pure averaging* and generate metastable belief basins rather than one global consensus — the polarization phenomenology of [[Echo chambers and polarization]]. In the [[Multi-agent variational free energy]] functional this corresponds to a regime where the attention weights $\beta_{ij}$ over-weight agreement with the local majority, so that the gauge-transported coupling $\beta_{ij}\,\mathrm{KL}(q_i \,\|\, \Omega_{ij}[q_j])$ stops behaving like linear consensus dynamics and instead supports separated, self-reinforcing belief clusters. Migration limited against this force is what keeps those clusters distinct, supplying between-group variance — the macroscopic analogue of the program's strong prior self-coupling $\alpha\,\mathrm{KL}(q_i\,\|\,p_i)$, which similarly resists global homogenization and is one of the levers of [[Belief inertia]].

The "selection acts on groups as units" half is the program's [[Meta-agents and hierarchical emergence]] thesis seen from evolution's side: when within-group conformity locks a cluster of agents into a coherent shared belief, that cluster acquires a group-level state that can be carried, compared, and selected as a single object — precisely the coarse-graining that the [[Renormalization-group flow of beliefs]] picture formalizes. Nowak's network-reciprocity and group-selection conditions are also the natural evolutionary index for the cooperation subsection ([[Evolutionary game theory and cooperation]]); network reciprocity treats agents as nodes on a coupling graph, as the VFE program does, and group selection prefigures its hierarchical coarse-graining directly ([[nowak-2006-five-rules-cooperation]]). The relevance is mechanism-level for the within-group bistability and framing-level for the multilevel/emergence reading: cultural group selection specifies *what* dynamics the kernel and coupling-graph topology must reproduce to yield group-level adaptive units, while the gauge-theoretic functional is where those behaviors would be recovered as limits of the coupling kernel.

## Sources

- [[henrich-boyd-1998-conformist-transmission]] — formal model showing conformist transmission is adaptive; the cubic adoption rule, its within-group bistability, and how it maintains between-group variance against migration.
- [[boyd-richerson-1985-culture-evolutionary-process]] — dual-inheritance theory in recursion form; the bias taxonomy and the argument that conformity plus limited migration sustains group differences enabling group selection.
- [[richerson-boyd-2005-not-by-genes-alone]] — prose synthesis; why conformity and limited migration enable cultural group selection and gene–culture coevolution of cooperation.
- [[nowak-2006-five-rules-cooperation]] — group (multilevel) selection as one of five routes to cooperation; the $b/c > 1 + n/m$ condition and the role of between- vs within-group variance.
- [[henrich-2016-secret-of-our-success]] — cumulative culture, the "collective brain," and group-level adaptive capacity as the empirical face of the multilevel argument.
