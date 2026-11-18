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
updated: 2026-11-18
---

# Emergent spacetime and holography

## The big picture

A large and increasingly mainstream body of theoretical physics holds that spacetime geometry is not a primitive of nature but an emergent, coarse-grained, information-theoretic description of some more fundamental substrate. The opening move of the whole program is thermodynamic: [[jacobson-1995-einstein-equation-of-state|jacobson-1995-thermodynamics-spacetime]] derived the Einstein field equations not by postulating them but by demanding that the Clausius relation $\delta Q = T\,\delta S$ hold for the Rindler horizon seen by every local accelerated observer, with entropy proportional to horizon area. Gravity, on this reading, is an equation of state — a thermodynamic identity that holds because the microscopic degrees of freedom have already equilibrated, in the same way the ideal-gas law holds without anyone deriving it from molecular trajectories. The entropy that drives the argument descends from black-hole thermodynamics, [[bekenstein-1973-black-holes-entropy]]'s proposal that a black hole carries entropy proportional to its horizon area, later given a covariant Noether-charge footing by [[wald-1993-black-hole-entropy-noether]]. The area-not-volume scaling of that entropy is the seed of the **holographic principle** ([[thooft-1993-dimensional-reduction]], [[bousso-2002-holographic|bousso-2002-holographic-principle]]): the information content of a region is bounded by its boundary area, so a $d$-dimensional gravitational world is encoded on a $(d-1)$-dimensional screen.

The modern synthesis sharpens "emergence" into a concrete dictionary. [[maldacena-1999-adscft|maldacena-1998-ads-cft]]'s AdS/CFT correspondence supplied the first exact instance — a gravitating bulk equivalent to a boundary conformal field theory — and [[ryu-takayanagi-2006-holographic-entanglement-entropy]] then identified the boundary's *entanglement entropy* with the area of a bulk minimal surface, welding geometry to quantum information. [[VanRaamsdonk-2010-spacetime-entanglement|vanraamsdonk-2010-entanglement-spacetime]] read this constructively: disentangling boundary regions tears the bulk apart, so spacetime connectivity *is* entanglement. [[maldacena-2013-er-epr|maldacena-susskind-2013-er-epr]] pushed the slogan to ER=EPR, equating Einstein-Rosen bridges with EPR pairs, and [[faulkner-2014-gravitation-from-entanglement]] showed that the linearized Einstein equations follow from the first law of entanglement entropy — Jacobson's thermodynamic argument reincarnated in quantum-information language. Running parallel are the entropic-force readings of [[verlinde-2011-entropic-gravity]] and [[padmanabhan-2010-thermodynamical-gravity|padmanabhan-2010-thermodynamic-gravity]], where gravity is an emergent statistical tendency rather than a fundamental interaction, and a discrete, constructive lineage — [[swingle-2012-entanglement-renormalization-holography|swingle-2012-entanglement-renormalization]] and [[vidal-2007-entanglement-renormalization]]'s identification of the MERA tensor network with a discretized holographic geometry, [[cao-carroll-2017-space-from-hilbert-space]]'s program to grow spatial geometry directly from the entanglement structure of an abstract Hilbert-space state, and the computational/complexity readings of [[lloyd-2002-computational-capacity-universe|lloyd-2002-computational-capacity]] and [[susskind-2014-complexity-black-hole-horizons]]. [[connes-rovelli-1994-thermal-time]] adds a further twist, deriving the very flow of time from the thermal (Tomita-Takesaki) structure of a state. [[carlip-2014-emergent-gravity|carlip-2014-challenges-emergent-gravity]] is the indispensable skeptic, cataloguing what "emergent gravity" must explain — diffeomorphism invariance, the right Newton constant, Lorentz signature — before the slogan earns the name.

## Key threads

The first thread is **geometry as thermodynamics of horizons**: Einstein's equations as an equation of state ([[jacobson-1995-einstein-equation-of-state|jacobson-1995-thermodynamics-spacetime]]), generalized to a *maximal vacuum entanglement* variational principle in [[jacobson-2016-entanglement-equilibrium]], with the entropic-force restatements of [[verlinde-2011-entropic-gravity]] and [[padmanabhan-2010-thermodynamical-gravity|padmanabhan-2010-thermodynamic-gravity]] and the black-hole entropy foundations of [[bekenstein-1973-black-holes-entropy]] and [[wald-1993-black-hole-entropy-noether]]. The second is **entanglement builds geometry**: the Ryu-Takayanagi area law ([[ryu-takayanagi-2006-holographic-entanglement-entropy]]), its constructive reading ([[VanRaamsdonk-2010-spacetime-entanglement|vanraamsdonk-2010-entanglement-spacetime]]), the derivation of dynamics from the entanglement first law ([[faulkner-2014-gravitation-from-entanglement]]), and the ER=EPR identification ([[maldacena-2013-er-epr|maldacena-susskind-2013-er-epr]]), all underwritten by the exact AdS/CFT duality ([[maldacena-1999-adscft|maldacena-1998-ads-cft]]). The third is **discrete and computational holography**: tensor-network geometry via MERA ([[swingle-2012-entanglement-renormalization-holography|swingle-2012-entanglement-renormalization]], [[vidal-2007-entanglement-renormalization]]), space from Hilbert space ([[cao-carroll-2017-space-from-hilbert-space]]), the holographic bound ([[thooft-1993-dimensional-reduction]], [[bousso-2002-holographic|bousso-2002-holographic-principle]]), and the computational/complexity perspective ([[lloyd-2002-computational-capacity-universe|lloyd-2002-computational-capacity]], [[susskind-2014-complexity-black-hole-horizons]], with emergent time in [[connes-rovelli-1994-thermal-time]]). The fourth thread is the **critical audit** ([[carlip-2014-emergent-gravity|carlip-2014-challenges-emergent-gravity]]) that any emergent-gravity claim must survive.

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
- [[Renormalization group flow]]
- [[wheeler-1990-it-from-bit]]

## Communication, error correction, and geometric representation

The Fields–Glazebrook–Marcianò–Zappala sequence connects communication protocols, quantum error correction, and TQFT. Part I specifies encoding, decoding, and error structure; Part II adds spin-network and related topological constructions. The geometric interpretation depends on those supplied structures. Addazi and colleagues' gauge/gravity treatment also introduces ambient Lorentzian spacetime before its gravity specialization. These papers therefore provide construction methods to compare, while leaving a separate obligation to derive physical signature, dimension, clocks, and gravitational dynamics. [[fields-2024-qecc-tqft-i-protocols]], [[fields-2024-qecc-tqft-ii-spacetimes]], [[addazi-2021-generalized-holographic-principle-gauge-invariance-and-the-emergence-of-gravity-a-la-wilczek]]

The ER=EPR article studies a finite-screen, monogamous-entanglement limit and gives an operational topological identification; it does not construct a gravitational metric. The 2026 amplituhedra preprint supplies a further quantum-computation/scattering representation with stated restrictions on its uniqueness claim. [[fields-2025-er-epr-is-an-operational-theorem]], [[fields-2026-amplituhedra-generic-quantum-processes]], [[Chris Fields and physics as communication]]
