---
type: theme
title: Emergent spacetime and holography
aliases:
  - Emergent spacetime
  - Holographic principle
  - Entanglement and geometry
  - Information-theoretic gravity
  - "Holography"
  - "Holography and AdS-CFT"
  - "Entanglement Renormalization"
  - "Anti-de Sitter Space"
  - "AdS-CFT Correspondence"
  - "AdS/CFT correspondence"
  - "AdS-CFT"
tags:
  - cluster/participatory
  - project/multi-agent
status: draft
created: 2026-06-19
updated: 2026-06-19
---

# Emergent spacetime and holography

## The big picture

A large and increasingly mainstream body of theoretical physics holds that spacetime geometry is not a primitive of nature but an emergent, coarse-grained, information-theoretic description of some more fundamental substrate. The opening move of the whole program is thermodynamic: [[jacobson-1995-einstein-equation-of-state|jacobson-1995-thermodynamics-spacetime]] derived the Einstein field equations not by postulating them but by demanding that the Clausius relation $\delta Q = T\,\delta S$ hold for the Rindler horizon seen by every local accelerated observer, with entropy proportional to horizon area. Gravity, on this reading, is an equation of state — a thermodynamic identity that holds because the microscopic degrees of freedom have already equilibrated, in the same way the ideal-gas law holds without anyone deriving it from molecular trajectories. The entropy that drives the argument descends from black-hole thermodynamics, [[bekenstein-1973-black-holes-entropy]]'s proposal that a black hole carries entropy proportional to its horizon area, later given a covariant Noether-charge footing by [[wald-1993-black-hole-entropy-noether]]. The area-not-volume scaling of that entropy is the seed of the **holographic principle** ([[thooft-1993-dimensional-reduction]], [[bousso-2002-holographic|bousso-2002-holographic-principle]]): the information content of a region is bounded by its boundary area, so a $d$-dimensional gravitational world is encoded on a $(d-1)$-dimensional screen.

The modern synthesis sharpens "emergence" into a concrete dictionary. [[maldacena-1999-adscft|maldacena-1998-ads-cft]]'s AdS/CFT correspondence supplied the first exact instance — a gravitating bulk equivalent to a boundary conformal field theory — and [[ryu-takayanagi-2006-holographic-entanglement-entropy]] then identified the boundary's *entanglement entropy* with the area of a bulk minimal surface, welding geometry to quantum information. [[VanRaamsdonk-2010-spacetime-entanglement|vanraamsdonk-2010-entanglement-spacetime]] read this constructively: disentangling boundary regions tears the bulk apart, so spacetime connectivity *is* entanglement. [[maldacena-2013-er-epr|maldacena-susskind-2013-er-epr]] pushed the slogan to ER=EPR, equating Einstein-Rosen bridges with EPR pairs, and [[faulkner-2014-gravitation-from-entanglement]] showed that the linearized Einstein equations follow from the first law of entanglement entropy — Jacobson's thermodynamic argument reincarnated in quantum-information language. Running parallel are the entropic-force readings of [[verlinde-2011-entropic-gravity]] and [[padmanabhan-2010-thermodynamical-gravity|padmanabhan-2010-thermodynamic-gravity]], where gravity is an emergent statistical tendency rather than a fundamental interaction, and a discrete, constructive lineage — [[swingle-2012-entanglement-renormalization-holography|swingle-2012-entanglement-renormalization]] and [[vidal-2007-entanglement-renormalization]]'s identification of the MERA tensor network with a discretized holographic geometry, [[cao-carroll-2017-space-from-hilbert-space]]'s program to grow spatial geometry directly from the entanglement structure of an abstract Hilbert-space state, and the computational/complexity readings of [[lloyd-2002-computational-capacity-universe|lloyd-2002-computational-capacity]] and [[susskind-2014-complexity-black-hole-horizons]]. [[connes-rovelli-1994-thermal-time]] adds a further twist, deriving the very flow of time from the thermal (Tomita-Takesaki) structure of a state. [[carlip-2014-emergent-gravity|carlip-2014-challenges-emergent-gravity]] is the indispensable skeptic, cataloguing what "emergent gravity" must explain — diffeomorphism invariance, the right Newton constant, Lorentz signature — before the slogan earns the name.

This theme is assembled here as the **external benchmark** against which the [[participatory-it-from-bit|participatory "it from bit"]] program of the [[Gauge-Theoretic Multi-Agent VFE Model]] is contrasted. Both camps share one conviction — that geometry is downstream of information — but they differ in machinery, and naming the difference precisely is what keeps the comparison honest rather than rhetorical.

## Key threads

The first thread is **geometry as thermodynamics of horizons**: Einstein's equations as an equation of state ([[jacobson-1995-einstein-equation-of-state|jacobson-1995-thermodynamics-spacetime]]), generalized to a *maximal vacuum entanglement* variational principle in [[jacobson-2016-entanglement-equilibrium]], with the entropic-force restatements of [[verlinde-2011-entropic-gravity]] and [[padmanabhan-2010-thermodynamical-gravity|padmanabhan-2010-thermodynamic-gravity]] and the black-hole entropy foundations of [[bekenstein-1973-black-holes-entropy]] and [[wald-1993-black-hole-entropy-noether]]. The second is **entanglement builds geometry**: the Ryu-Takayanagi area law ([[ryu-takayanagi-2006-holographic-entanglement-entropy]]), its constructive reading ([[VanRaamsdonk-2010-spacetime-entanglement|vanraamsdonk-2010-entanglement-spacetime]]), the derivation of dynamics from the entanglement first law ([[faulkner-2014-gravitation-from-entanglement]]), and the ER=EPR identification ([[maldacena-2013-er-epr|maldacena-susskind-2013-er-epr]]), all underwritten by the exact AdS/CFT duality ([[maldacena-1999-adscft|maldacena-1998-ads-cft]]). The third is **discrete and computational holography**: tensor-network geometry via MERA ([[swingle-2012-entanglement-renormalization-holography|swingle-2012-entanglement-renormalization]], [[vidal-2007-entanglement-renormalization]]), space from Hilbert space ([[cao-carroll-2017-space-from-hilbert-space]]), the holographic bound ([[thooft-1993-dimensional-reduction]], [[bousso-2002-holographic|bousso-2002-holographic-principle]]), and the computational/complexity perspective ([[lloyd-2002-computational-capacity-universe|lloyd-2002-computational-capacity]], [[susskind-2014-complexity-black-hole-horizons]], with emergent time in [[connes-rovelli-1994-thermal-time]]). The fourth thread is the **critical audit** ([[carlip-2014-emergent-gravity|carlip-2014-challenges-emergent-gravity]]) that any emergent-gravity claim must survive.

## How it lands in this work

The participatory program inhabits the same "information to geometry" spirit but runs on different — classical and gauge-theoretic — machinery, and the contrast is sharp enough to be load-bearing. Where the physics tradition builds geometry from *quantum entanglement entropy* on a boundary, the multi-agent model builds it from a *classical-information pullback*: the [[Fisher information metric]] on a statistical fibre, pulled back along an agent's belief section onto a noumenal base manifold, as set out in [[participatory-it-from-bit]] and [[Participatory realism (it from bit)]]. The MERA/holographic coarse-graining of [[swingle-2012-entanglement-renormalization-holography|swingle-2012-entanglement-renormalization]] and [[vidal-2007-entanglement-renormalization]] is the natural foil for the model's own multi-scale coarse-graining — the [[Ouroboros multi-scale dynamics]] tower and its [[Renormalization-group flow of beliefs]] — where meta-agents are coarse-grainings of clusters rather than tensor-network layers, and the "radial/holographic" direction becomes the model's scale index. The thermodynamic-equilibrium reading of [[jacobson-1995-einstein-equation-of-state|jacobson-1995-thermodynamics-spacetime]] and [[jacobson-2016-entanglement-equilibrium]] is the foil for the model's variational-free-energy stationarity: both make geometry a stationary point of an information functional, but the model's functional is a free energy over agent beliefs, not an entanglement entropy over horizons. The honest caveat, in the project's own house style, is that the model's pullback is a *structural analogue, not a derivation* of these results: it shares the slogan, reproduces the qualitative architecture (geometry from information, multi-scale holographic compression), and leaves the genuinely hard pieces — Lorentzian signature, the right dynamics, diffeomorphism invariance — exactly where [[carlip-2014-emergent-gravity|carlip-2014-challenges-emergent-gravity]] says the burden lies.

## Open questions / gaps

The signature problem is shared and unsolved on both sides: the entanglement-geometry program lives natively in a Lorentzian bulk, whereas the Fisher pullback is positive semi-definite by construction (Sylvester's law), so the participatory program must *postulate* complexification to reach $(-,+,+,+)$, and none of the physics sources here hands it a principled fix. Whether the classical-information pullback can recover anything like the Ryu-Takayanagi area law — an entropy-area relation rather than a score-outer-product metric — is open; the model's entropy is configurational [[Meta-entropy|meta-entropy]] over beliefs, not boundary entanglement. It is unclear whether the model's free-energy stationarity can yield field equations in the manner of [[faulkner-2014-gravitation-from-entanglement]], or whether [[lloyd-2002-computational-capacity-universe|lloyd-2002-computational-capacity]]'s and [[susskind-2014-complexity-black-hole-horizons]]'s complexity bounds have any counterpart in the agent dynamics. These are the points at which the benchmark is most useful: it specifies precisely what a serious "emergent geometry from beliefs" claim would have to deliver before it could stand beside the quantum-holographic results rather than merely echo their slogans.

## Sources synthesized

- [[jacobson-1995-einstein-equation-of-state|jacobson-1995-thermodynamics-spacetime]] — Einstein equations as a horizon equation of state (Clausius relation + area entropy).
- [[jacobson-2016-entanglement-equilibrium]] — gravity from a maximal-vacuum-entanglement equilibrium variational principle.
- [[padmanabhan-2010-thermodynamical-gravity|padmanabhan-2010-thermodynamic-gravity]] — gravitational dynamics as emergent thermodynamics of spacetime.
- [[verlinde-2011-entropic-gravity]] — gravity as an entropic force on holographic screens.
- [[ryu-takayanagi-2006-holographic-entanglement-entropy]] — boundary entanglement entropy as a bulk minimal-surface area.
- [[faulkner-2014-gravitation-from-entanglement]] — linearized Einstein equations from the entanglement first law.
- [[swingle-2012-entanglement-renormalization-holography|swingle-2012-entanglement-renormalization]] — MERA tensor networks as discretized holographic geometry.
- [[vidal-2007-entanglement-renormalization]] — entanglement renormalization / MERA, the coarse-graining substrate.
- [[maldacena-1999-adscft|maldacena-1998-ads-cft]] — the AdS/CFT bulk-boundary duality underwriting holography.
- [[maldacena-2013-er-epr|maldacena-susskind-2013-er-epr]] — ER=EPR: wormholes as entanglement.
- [[cao-carroll-2017-space-from-hilbert-space]] — growing spatial geometry from Hilbert-space entanglement structure.
- [[bekenstein-1973-black-holes-entropy]] — black-hole entropy proportional to horizon area.
- [[thooft-1993-dimensional-reduction]] — dimensional reduction / the holographic bound.
- [[wald-1993-black-hole-entropy-noether]] — black-hole entropy as a Noether charge.
- [[susskind-2014-complexity-black-hole-horizons]] — computational complexity and the growth of black-hole interiors.
- [[bousso-2002-holographic|bousso-2002-holographic-principle]] — the covariant holographic entropy bound.
- [[carlip-2014-emergent-gravity|carlip-2014-challenges-emergent-gravity]] — the skeptic's catalogue of what emergent gravity must still explain.
- [[lloyd-2002-computational-capacity-universe|lloyd-2002-computational-capacity]] — the computational capacity of the universe (the cosmos as computer).
- [[connes-rovelli-1994-thermal-time]] — the thermal-time hypothesis: time flow from a state's modular structure.
- [[VanRaamsdonk-2010-spacetime-entanglement|vanraamsdonk-2010-entanglement-spacetime]] — building up spacetime with quantum entanglement.

## See also

- [[Participatory realism (it from bit)]]
- [[Fisher information metric]]
- [[Renormalization-group flow of beliefs]]
- [[Ouroboros multi-scale dynamics]]
- [[wheeler-1990-it-from-bit]]
- [[participatory-it-from-bit]]
