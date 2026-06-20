---
type: concept
title: "Quantum information geometry"
aliases:
  - "Quantum Fisher information"
  - "Monotone metrics"
  - "Bures metric"
  - "SLD metric"
  - "Quantum information geometry (QIG)"
tags:
  - cluster/info-geometry
  - cluster/participatory
  - project/multi-agent
  - project/transformer
status: draft
created: 2026-06-19
updated: 2026-06-19
---

# Quantum information geometry

## Definition

**Quantum information geometry** is the generalization of classical Fisher–Rao geometry from probability distributions to density operators $\rho$ on a Hilbert space. Where the classical theory equips a family of densities $p(x\mid\theta)$ with the [[Fisher information metric]], the quantum theory asks for a Riemannian metric on the convex manifold of density matrices that measures the *distinguishability* of nearby quantum states. The defining structural fact is **non-uniqueness**. Classically, Čencov's theorem ([[cencov-1982-statistical-decision-rules]]) singles out the Fisher metric as the *only* metric contracting under stochastic (Markov) maps, so the geometry is forced. Quantumly, [[petz-1996-monotone-metrics]] proved that the metrics contracting under all completely positive trace-preserving (CPTP) maps form an *infinite family*, in one-to-one correspondence with operator-monotone functions through Kubo–Ando operator-mean theory. There is no single canonical quantum Fisher metric; one must be *chosen*.

The family has distinguished extremes. The smallest monotone metric is the **Bures / SLD metric**, the quantum Fisher information defined by [[braunstein-caves-1994-quantum-fisher]] through the symmetric logarithmic derivative $L_\theta$ via $\partial_\theta\rho = \tfrac12(L_\theta\rho + \rho L_\theta)$, with $F_Q = \mathrm{Tr}(\rho L_\theta^2)$. Operationally it is the classical Fisher information of the measurement statistics, maximized over all POVMs — the best distinguishability an observer can extract, yielding the quantum Cramér–Rao bound. Its lineage runs back to [[wootters-1981-statistical-distance]], who identified pure-state statistical distance with the Hilbert-space angle, and to [[uhlmann-1976-transition-probability]], whose transition probability (fidelity) generates the Bures distance. On commuting (diagonal) states the whole family collapses to the unique classical Fisher–Rao metric.

## Why it matters here

This page is the held input for a **deferred** extension of the participatory program. The manuscript [[participatory-it-from-bit]] builds physical-like geometry by *pulling back* a distinguishability metric from a statistical fibre to a noumenal base — and that fibre is, at the implemented scales, the real Gaussian one with its classical [[Fisher information metric]]. PIFB's own ontology declares a $U(\mathcal{H})$ quantum gauge group at the "open" scale-0 level, where agents would be density operators rather than Gaussian belief tuples. Quantum information geometry is what that scale-0 fibre needs: the metric to pull back when the section is quantum.

The non-uniqueness theorem matters directly for PIFB's rhetoric. The classical argument that "the geometry is forced" rests entirely on Čencov uniqueness ([[cencov-1982-statistical-decision-rules]]); Petz removes exactly that crutch in the quantum regime. A quantum lift of [[Physics from Fisher information]] therefore cannot transplant the "canonical, not arbitrary" framing — it must *justify* a chosen member of the monotone family, most naturally the operationally favored Bures/SLD metric. This is an honest gap, not a solved correspondence: the deferred scale-0 density-operator extension is theory-only, and the quantum metric it would require is non-canonical by theorem.

## Details

The **monotone family** is parameterized by operator-monotone functions $f$ with $f(1)=1$ and $f(t)=tf(1/t)$; each gives a metric $\langle A,B\rangle_\rho^f$ built from the left/right multiplication superoperators. The SLD/Bures metric corresponds to $f(t)=(1+t)/2$ (smallest), the right-logarithmic-derivative metric to $f(t)=2t/(1+t)$ (largest), with the Kubo–Mori/Bogoliubov metric (the second derivative of von Neumann relative entropy, the natural quantum analogue of KL curvature) sitting between. [[bengtsson-zyczkowski-2017-geometry-quantum-states]] is the standard reference treating these metrics, the Bures geometry, fidelity, and the convex-body structure of state space together. [[brody-hughston-2001-geometric-qm]] gives the complementary *pure-state* picture: the projective Hilbert space $\mathbb{CP}^n$ carries the Fubini–Study metric as its distinguishability geometry, recasting quantum mechanics itself as Hamiltonian flow on a Kähler manifold — the geometric-QM frame in which "it from bit" would be naturally phrased at scale 0.

The classical–quantum contrast is the conceptual core, and it links the sibling pages: the uniqueness side lives at [[Fisher information metric]] and [[Information geometry and natural gradient]]; the physics-induction program is [[Physics from Fisher information]]; and the participatory pullback that would consume this metric is [[Participatory realism (it from bit)]].

## Sources

- [[petz-1996-monotone-metrics]] — classifies all CPTP-monotone metrics on density matrices via operator-monotone functions; the quantum non-uniqueness theorem versus classical Čencov uniqueness.
- [[braunstein-caves-1994-quantum-fisher]] — quantum Fisher information via the SLD; measurement-optimized Fisher information, Bures metric, quantum Cramér–Rao bound.
- [[wootters-1981-statistical-distance]] — pure-state statistical distance as Hilbert-space angle; origin of the distinguishability lineage.
- [[uhlmann-1976-transition-probability]] — transition probability / fidelity generating the Bures distance.
- [[bengtsson-zyczkowski-2017-geometry-quantum-states]] — standard reference on the geometry of quantum states, monotone metrics, Bures geometry, fidelity.
- [[brody-hughston-2001-geometric-qm]] — geometric quantum mechanics; Fubini–Study metric on projective Hilbert space as pure-state distinguishability geometry.
- [[cencov-1982-statistical-decision-rules]] — classical uniqueness of the Fisher metric under sufficient statistics; the foil the quantum case breaks.

## See also

- [[Fisher information metric]]
- [[Physics from Fisher information]]
- [[Information geometry and natural gradient]]
- [[Participatory realism (it from bit)]]
- [[participatory-it-from-bit]]
