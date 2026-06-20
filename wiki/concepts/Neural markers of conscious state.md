---
type: concept
title: Neural markers of conscious state
aliases: ["Neural correlates of consciousness", "Entropy and integration markers of consciousness"]
tags:
  - cluster/participatory
  - cluster/participatory/consciousness
  - project/multi-agent
status: draft
created: 2026-06-19
updated: 2026-06-19
---

# Neural markers of conscious state

## What it is

**Neural markers of conscious state** are empirical, information-theoretic *order parameters* — scalar quantities extracted from neuroimaging — that track whether a brain is conscious and, more ambitiously, how rich that consciousness is. Rather than asking *which* contents are experienced, this line of work asks *how much* and *of what global character*, seeking macroscopic observables that change reliably across the wake/sleep/anaesthesia/disorders-of-consciousness gradient. Two complementary candidates anchor the picture. The first is **neural entropy**: the *entropic-brain hypothesis* of [[carhart-harris-2014-entropic-brain]] holds that the richness and character of a conscious state track the entropy of the underlying brain dynamics, with ordinary waking cognition poised near a critical point and "primary" states (the psychedelic state, REM, early psychosis) marked by elevated entropy and a loosening of the brain's normally constrained, hierarchically organized activity. The second is a **balance of integration versus functional diversity**: [[luppi-2019-consciousness-integration-diversity]] identifies, via dynamic functional connectivity and graph theory, a *consciousness-specific* dynamic interplay in which both extremes are pathological — consciousness requires that the brain neither fragment into independent modules nor collapse into a single over-integrated mode. Both markers are part of the wider [[Mathematical consciousness science]] program of rendering theories of consciousness into measurable, falsifiable quantities.

## Key results and mechanism

The entropic-brain claim is an inverted-U / criticality picture: writing $S$ for an entropy of the moment-to-moment repertoire of brain states, normal waking sits at an intermediate $S$ near a self-organized critical point, where the system balances order against flexibility. *Reducing* entropy below this point yields rigid, narrowed cognition; *raising* it (pharmacologically or in REM) yields the loosened, less-constrained dynamics of primary states. The signature is thus not "more entropy is better" but a tuned operating point at the edge of order and disorder. The Luppi result sharpens the complementary axis. Loss of consciousness *compromises informational capacity*: under anaesthesia and in disorders of consciousness, cortical networks lose functional diversity precisely when activity becomes highly integrated, and posterior default-mode regions show reduced integration *and* reduced diversity during unconsciousness. Schematically, if $I$ measures network integration and $D$ measures functional diversity, the conscious regime is a specific *joint* relationship $\,(I, D)\,$ — a co-fluctuating balance — rather than a maximum of either marginal. The two markers are facets of one idea: consciousness lives at an intermediate, tuned point on an integration–segregation (order–disorder) spectrum, where a system is rich enough to support many distinguishable states yet coherent enough to bind them into a single capacity.

## Relevance to this research

These markers matter to the gauge-theoretic VFE program because they are *empirical order parameters of exactly the kind the program manufactures from first principles*, and the manuscript [[participatory-it-from-bit]] cites them on that basis. The entropic-brain marker is the neuroscientific echo of [[Meta-entropy]]: where Carhart-Harris posits an entropy of the brain's state repertoire as the correlate of conscious richness, the program defines a configurational meta-entropy $S_{\mathrm{meta}}(\mathcal{F}_0) = \log W(\mathcal{F}_0)$ counting the belief configurations of a population of agents consistent with a fixed free energy, with a conjugate *meta-temperature* $T_{\mathrm{meta}}$ that sets the noise level of stochastic [[Natural gradient|natural-gradient]] belief updating. The shared move is to make an information-theoretic scalar the macrostate variable of a dynamical inferential system; the criticality framing connects to the program's multi-scale story through [[Ouroboros multi-scale dynamics]] and [[Renormalization group flow]]. The Luppi integration/diversity marker maps just as directly onto the program's central *integration-versus-segregation coarse-graining trade-off*: the formation of [[Meta-agents and hierarchical emergence|meta-agents]] is a controlled integration of beliefs across coupled agents, and the open question is exactly when integration enriches versus impoverishes the collective's informational capacity — the same tension Luppi measures, now expressed through the [[Fisher information metric]] geometry of [[Multi-agent variational free energy]] rather than through fMRI graphs. This correspondence is interpretive, not a borrowed theorem: the program does not adopt the psychedelic-specific claims of the entropic brain, and it offers a frame-relative, participatory reading of information rather than the substrate-intrinsic measures these markers presuppose, in keeping with [[Participatory realism (it from bit)]]. What the markers supply is external, quantitative *traction* — candidate observables against which a meta-entropy or integration/diversity prediction of the model could in principle be compared. The broader placement of these markers among rival theories of consciousness is developed in [[Mathematical consciousness science]] and the [[Consciousness and the hard problem]] theme.

## Sources

- [[carhart-harris-2014-entropic-brain]] — the entropic-brain hypothesis: neural entropy as a correlate of conscious-state richness, with a criticality/edge-of-order operating point.
- [[luppi-2019-consciousness-integration-diversity]] — a consciousness-specific dynamic balance of brain integration and functional diversity; loss of consciousness compromises informational capacity.

## See also

- [[Meta-entropy]]
- [[Multi-agent variational free energy]]
- [[Meta-agents and hierarchical emergence]]
- [[Ouroboros multi-scale dynamics]]
- [[Fisher information metric]]
- [[Mathematical consciousness science]]
- [[Consciousness and the hard problem]]
- [[Participatory realism (it from bit)]]
- [[Renormalization group flow]]
