---
type: theme
title: Participatory realism and quantum foundations
aliases:
  - "participatory realism synthesis"
  - "quantum foundations theme"
  - "agent-centered quantum interpretations"
  - "Quantum Foundations"
tags: [cluster/participatory, project/multi-agent]
status: stable
created: 2026-06-18
updated: 2026-11-18
---

# Participatory realism and quantum foundations

This theme weaves together the quantum-foundations sources of the `cluster/participatory`
research cluster into a single picture. The unifying thesis is that an agent's perspective is
ineliminable from physics: the quantum formalism is not a God's-eye description of
agent-independent facts but an account of how a *participant* engages, predicts, and
revises. The interesting work is then to explain
how *shared* reality is reconstructed among many such participants without smuggling back
in the view from nowhere.

## Sub-clusters of `cluster/participatory`

This cluster spans three disciplines, so the [[CLAUDE|`cluster/participatory`]] tag is subdivided into three nested sub-tags (the parent still rolls up), each anchored by its own theme essay:

- **`cluster/participatory/quantum-foundations`** *(physics origin)* — QM foundations & interpretation, holography & emergent spacetime, physics-from-information. **This theme** is its home; see also [[Emergent spacetime and holography]].
- **`cluster/participatory/philosophy-of-mind`** *(philosophy origin)* — structural realism, philosophy of science & metaphysics, it-from-bit. Home: [[Structural realism and philosophy of science]].
- **`cluster/participatory/consciousness`** *(neuroscience origin)* — scientific theories of consciousness (IIT, global workspace, neural correlates). Home: [[Consciousness and the hard problem]].

## The participatory family and its lineage

Christopher Fuchs gave the cluster its name. In [[fuchs-2017-participatory-realism]] he
coins **participatory realism** as the umbrella stance shared by the agent-centered
interpretations — QBism, relational quantum mechanics, and Wheeler's
observer-participancy — defined by the indispensability of a first-person perspective.
The position is *realist* (there is a world) but denies *spectator-objectivity* (that
the world is a ledger of agent-independent facts awaiting discovery); reality is in part
*made* in the agent's participation. Fuchs traces the lineage to Wheeler's "law without
law" and "it from bit" ([[wheeler-1990-it-from-bit]], [[Participatory realism (it from bit)]]),
presenting QBism as their disciplined modern descendant.

The stance has a clear technical anchor on the QBist side. The Born rule, in
[[fuchs-schack-2013-bayesian-coherence]], is not a law about objective propensities but a
**normative coherence condition** a single agent imposes on its own personal Bayesian
credences — recast, via a symmetric informationally complete measurement (SIC-POVM), as a
fixed, dimension-dependent deformation of the classical law of total probability.
Quantum mechanics becomes a single constraint among an agent's subjective probabilities,
with no objective state anywhere in sight. Probabilities live *with* the agent; the formalism only
constrains how they hang together. [[QBism]] develops this concept page; the present
theme situates it in the wider family.

N. David Mermin's "correlations without correlata" ([[mermin-1998-correlations]]) gives
the family its sharpest one-line thesis. Quantum theory, on his Ithaca reading, is about
*correlation and only correlation*: the relations between subsystems are physical and
definite even when the absolute, correlate properties of the subsystems are not. This
sits at the hinge between Rovelli's relational program and the emerging QBist line.

## Relational quantum mechanics and the construction of agreement

Carlo Rovelli's relational quantum mechanics (RQM) is the family's most thoroughgoing
anti-substantialism. *Helgoland* ([[rovelli-2021-helgoland]]) develops RQM into an
explicit relations-first metaphysics: a system's properties are defined only relative to
another system, there is no observer-free state, and "objects" are derivative nodes where
relations meet. It links the participatory cluster to [[Structural realism]].

RQM faces an obvious tension: if information is physical yet the facts one observer holds
are in principle inaccessible to any other, how do observers ever agree? Adlam and Rovelli
repair this in [[adlam-2022-cross-perspective|adlam-rovelli-2022-cross-perspective]] by adding a **cross-perspective
links** postulate: whenever an observer has obtained a definite value, that information is
stored in physical variables and is therefore accessible by measurement to other
observers, who will find consistent values. Agreement is thus a *physical achievement*,
not an a priori posit, and is reached without any frame-independent ledger of absolute
facts.

## The no-go theorems: why objectivity must be built, not assumed

Two sharpened Wigner's-friend results turn the philosophical "whose fact is it?" question
into formal impossibility. Frauchiger and Renner ([[frauchiger-renner-2018-no-self-description]])
nest agents who reason with quantum theory about one another and derive a flat logical
contradiction from three natural assumptions — that an agent may certify a Born-rule
prediction (Q), that different agents' certified conclusions are consistent and adoptable
by one another (C), and that a measurement yields a single definite outcome (S). The
relational/QBist family escapes by rejecting C: there is simply no agent-independent fact
for different observers to share. Brukner ([[brukner-2018-no-go-observer-facts]]) converts
the same tension into an *experimentally testable Bell-type inequality* whose violation
rules out the joint existence of observer-independent facts under locality and free choice.
The natural escape is again to deny observer-independence: a friend's outcome is a fact
*relative to the friend*. Together these results are the operational, falsifiable statement
that **there is no pre-given ledger of observer-independent facts**, so any account of
objectivity must be built from inter-agent relations. The
[[Observer-dependent facts and Wigner's friend]] concept page develops this strand in
detail.

Richard Healey's pragmatism ([[healey-2017-quantum-revolution]]) marks a middle
ground. Healey reads the quantum state neither as an ontic
feature of the world nor as one agent's private whim, but as furnishing *authoritative,
objectively correct prescriptions* for how any suitably situated agent ought to apportion
credence. This is objectivity-without-ontic-states: binding for everyone in a given
situation, yet not a wavefunction-of-the-world.

## Quantum reference frames: covariance as shareability

The most literal physics treatment of **gauge covariance as the formal expression of
shareability between agents** is the quantum
reference frame (QRF) program, developed on its own [[Quantum reference frames]] concept
page and grounded in [[giacomini-2019-qrf-covariance]], [[bartlett-2007-reference-frames|bartlett-rudolph-spekkens-2007-reference-frames]],
and [[vanrietvelde-2020-qrf-perspective-neutral|vanrietvelde-2020-change-of-perspective]]. Promoting the reference frame to a quantum
system makes superposition and entanglement *frame-relative*; the speakable/unspeakable
split distinguishes shareable from frame-local content; and recasting frame change as
gauge-fixing makes "frame choice = choice of gauge" exact. This strand is where the
participatory cluster connects most directly to gauge-frame constructions such as
the block-$GL(K)$ structure of the [[VFE Transformer Program]].

## Information-first foundations

Several sources frame physics as information-first. Lucien Hardy's reconstruction ([[hardy-2001-five-axioms]]) derives
finite-dimensional quantum theory from five operational axioms about probabilities, with
only a continuity-of-reversible-transformations axiom distinguishing it from classical
probability. This is the methodological template for an "it from bit, then
emergent structure" arc: begin with bare informational primitives and *derive* the rich
structure rather than postulate it. Robert Spekkens' toy theory
([[spekkens-2007-toy-theory]]) shows how far a single epistemic restriction reproduces
"quantum" phenomena, demarcating which features of agent agreement/disagreement are mere
incomplete knowledge and which demand stronger relational machinery.

Deutsch and Marletto's constructor theory of information
([[deutsch-2015-constructor-information|deutsch-marletto-2015-constructor-information]]) is the
**contrast class** within information-first physics: constructor theory grounds information in
*objective, agent-independent* possibility/impossibility facts about physical
transformations, whereas relational and QBist accounts decline to locate information in
observer-independent physical possibility.
Seth Lloyd's computational-capacity bounds ([[lloyd-2002-computational-capacity-universe|lloyd-2002-computational-capacity]]) supply
the *computational* face of "it from bit": physical processes as literal computations on a
finite stock of bits; this connects to the [[Emergent spacetime and holography]]
theme. Finally, Connes and Rovelli's thermal time hypothesis
([[connes-rovelli-1994-thermal-time]]) completes the cluster's *observer-relative time*
strand: in a generally covariant theory there is no preferred external time, and the flow
of time emerges as the Tomita–Takesaki modular flow of the observer's statistical state.
Time is therefore state-dependent and observer-relative.

## Sources synthesized

- [[fuchs-2017-participatory-realism]] — coins "participatory realism"; the family's name and Wheeler lineage.
- [[fuchs-schack-2013-bayesian-coherence]] — Born rule as a personalist coherence constraint (SIC-POVM); the QBist technical core.
- [[mermin-1998-correlations]] — "correlations without correlata"; the relational thesis in one line.
- [[rovelli-2021-helgoland]] — relational QM as relations-first metaphysics.
- [[adlam-2022-cross-perspective|adlam-rovelli-2022-cross-perspective]] — cross-perspective links; agreement as a physical achievement.
- [[frauchiger-renner-2018-no-self-description]] — Q/C/S trilemma; no shared observer-independent facts.
- [[brukner-2018-no-go-observer-facts]] — testable Bell-type no-go for observer-independent facts.
- [[healey-2017-quantum-revolution]] — pragmatist objectivity-without-ontic-states.
- [[giacomini-2019-qrf-covariance]] — quantum-reference-frame covariance; entanglement as frame-relative.
- [[bartlett-2007-reference-frames|bartlett-rudolph-spekkens-2007-reference-frames]] — operational QRF theory; speakable/unspeakable; superselection.
- [[vanrietvelde-2020-qrf-perspective-neutral|vanrietvelde-2020-change-of-perspective]] — perspective-neutral / gauge-fixing formulation of frame change.
- [[hardy-2001-five-axioms]] — informational reconstruction of quantum theory.
- [[spekkens-2007-toy-theory]] — epistemic-restriction toy model.
- [[deutsch-2015-constructor-information|deutsch-marletto-2015-constructor-information]] — constructor theory; the agent-independent contrast class.
- [[lloyd-2002-computational-capacity-universe|lloyd-2002-computational-capacity]] — computational-universe bounds; the computational face of "it from bit".
- [[zenil-2013-computable-universe]] — anthology of the digital-physics / "nature as computation" lineage (Zuse, Wolfram, 't Hooft, Lloyd; Penrose foreword); the computational wing of "it from bit," cited as both kin and observer-independent contrast class.
- [[nelson-1967-brownian-motion]] — stochastic mechanics deriving the Schrödinger equation from a conservative diffusion; the physics-from-information ancestor of the entropic-dynamics strand.
- [[bell-2004-speakable-unspeakable]] — Bell's collected foundational papers; the theorem against local observer-independent values that the sharpened Wigner's-friend no-go results extend.
- [[connes-rovelli-1994-thermal-time]] — thermal time hypothesis; observer-relative emergent time.

## Chris Fields's communication program

Fields's operational program makes the system boundary and the observer's identification procedures part of the scientific description. The closest connection to participatory realism is that records become usable through a reference frame, an interpretation, and a protocol for comparison. The Chu-space papers describe semantic compatibility, while the quantum interaction papers model finite information exchange between systems under explicit physical assumptions. [[fields-2019-chu-spaces-i-category-theory]], [[fields-2019-chu-spaces-ii-object-identification]], [[fields-2021-minimal-physicalism-as-a-scale-free-substrate-for-cognition-and-consciousness]], [[fields-2019-sharing-nonfungible-information-requires-shared-nonfungible-information]]

This literature contains both constructive models and strong interpretive or no-go claims. The source notes for [[fields-2016-decompositional-equivalence-a-fundamental-symmetry-underlying-quantum-theory]] and [[fields-2014-consistent-quantum-mechanics-admits-no-mereotopology]] identify specific gaps in displayed arguments; their universal conclusions should not be inherited as established premises. The newer [[fields-2025-operational-protocols-cannot-certify-classicality]] concerns unrestricted operational certification and must be distinguished from model-relative inference using declared preparation and measurement assumptions. [[Chris Fields and physics as communication]] organizes the full collection.
