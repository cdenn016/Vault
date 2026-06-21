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
updated: 2026-06-20
---

# Participatory realism and quantum foundations

This theme weaves together the quantum-foundations sources of the `cluster/participatory`
research cluster into a single picture and shows why that picture is the conceptual
backbone of the gauge-theoretic VFE program — in particular the
[[Gauge-Theoretic Multi-Agent VFE Model]] and its manuscript
[[participatory-it-from-bit]]. The unifying thesis is that an agent's perspective is
ineliminable from physics: the quantum formalism is not a God's-eye description of
agent-independent facts but an account of how a *participant* engages, predicts, and
revises. The interesting work, both in foundations and in the model, is then to explain
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
presenting QBism as their disciplined modern descendant. The program adopts this banner
directly, and its distinctive contribution is to make participatory realism
*constructive and multi-agent*: where Fuchs emphasizes the single agent's participation,
the program supplies the machinery by which many participating agents reach partial
agreement.

That machinery has a clear technical anchor on the QBist side. The Born rule, in
[[fuchs-schack-2013-bayesian-coherence]], is not a law about objective propensities but a
**normative coherence condition** a single agent imposes on its own personal Bayesian
credences — recast, via a symmetric informationally complete measurement (SIC-POVM), as a
fixed, dimension-dependent deformation of the classical law of total probability.
Quantum mechanics becomes a single constraint among an agent's subjective probabilities,
with no objective state anywhere in sight. This is precisely the stance the program takes
toward belief updates: an agent's variational posterior is revised to minimize
[[Variational free energy]] as a normative, agent-internal consistency condition, not as
estimation of an external truth. Probabilities live *with* the agent; the formalism only
constrains how they hang together. [[QBism]] develops this concept page; the present
theme situates it in the wider family.

N. David Mermin's "correlations without correlata" ([[mermin-1998-correlations]]) gives
the family its sharpest one-line thesis. Quantum theory, on his Ithaca reading, is about
*correlation and only correlation*: the relations between subsystems are physical and
definite even when the absolute, correlate properties of the subsystems are not. This
sits at the hinge between Rovelli's relational program and the emerging QBist line, and it
states in compact form the program's relational commitment — what is objective is the
*relation between agents' beliefs*, recovered by [[Parallel transport]] between
[[Agents as fibre-bundle sections]], not any agent's intrinsic belief content, with the
absence of canonical correlata reflected in nonzero [[Holonomy]].

## Relational quantum mechanics and the construction of agreement

Carlo Rovelli's relational quantum mechanics (RQM) is the family's most thoroughgoing
anti-substantialism. *Helgoland* ([[rovelli-2021-helgoland]]) develops RQM into an
explicit relations-first metaphysics: a system's properties are defined only relative to
another system, there is no observer-free state, and "objects" are derivative nodes where
relations meet. This is the foundational-physics analogue of the program's insistence
that an agent's belief is meaningful only in relation to other agents, expressed through
the connection that transports between frames under a [[Gauge transformation]]; it links
the participatory cluster to [[Structural realism]] and supplies the metaphysical reading
under which the program's gauge structure is ontology, not mere formalism.

RQM faces an obvious tension: if information is physical yet the facts one observer holds
are in principle inaccessible to any other, how do observers ever agree? Adlam and Rovelli
repair this in [[adlam-2022-cross-perspective|adlam-rovelli-2022-cross-perspective]] by adding a **cross-perspective
links** postulate: whenever an observer has obtained a definite value, that information is
stored in physical variables and is therefore accessible by measurement to other
observers, who will find consistent values. Agreement is thus a *physical achievement*,
not an a priori posit, and is reached without any frame-independent ledger of absolute
facts. This is the closest existing-physics analogue of the program's inter-agent transport
map $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$: the program *constructs* the access that
RQM posits, as transport along a connection between [[Agents as fibre-bundle sections]],
with the failure of perfect agreement quantified by [[Holonomy]] and the consensus drive
supplied by the coupling term of [[Multi-agent variational free energy]].

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
objectivity must be built from inter-agent relations. In the program's reading, the failure
of assumption C and the violation of Brukner's inequality are the foundational-physics
shadow of generically nonzero holonomy between agent frames; the
[[Observer-dependent facts and Wigner's friend]] concept page develops this strand in
detail. The program's answer — objectivity as *transported consensus* among coupled
agents — is designed to be compatible with exactly these no-go results.

Richard Healey's pragmatism ([[healey-2017-quantum-revolution]]) marks the precise middle
ground the program steers toward. Healey reads the quantum state neither as an ontic
feature of the world nor as one agent's private whim, but as furnishing *authoritative,
objectively correct prescriptions* for how any suitably situated agent ought to apportion
credence. This is objectivity-without-ontic-states: binding for everyone in a given
situation, yet not a wavefunction-of-the-world. The program's consensus-as-objectivity is
structurally this pragmatist middle ground — the belief an agent would hold after its
variational dynamics equilibrate against the shared coupling field, intersubjectively
binding in the sense that beliefs agree up to [[Parallel transport]], with residual
disagreement measured by [[Holonomy]].

## Quantum reference frames: covariance as shareability

The most literal physics precedent for the program's structural claim — that **gauge
covariance is the formal expression of shareability between agents** — is the quantum
reference frame (QRF) program, developed on its own [[Quantum reference frames]] concept
page and grounded in [[giacomini-2019-qrf-covariance]], [[bartlett-2007-reference-frames|bartlett-rudolph-spekkens-2007-reference-frames]],
and [[vanrietvelde-2020-qrf-perspective-neutral|vanrietvelde-2020-change-of-perspective]]. Promoting the reference frame to a quantum
system makes superposition and entanglement *frame-relative*; the speakable/unspeakable
split distinguishes shareable from frame-local content; and recasting frame change as
gauge-fixing makes "frame choice = choice of gauge" exact. Each agent's local gauge frame
$\phi_i$ is then a genuine reference frame in this sense, and comparing perspectives is a
state-aware gauge transformation rather than a relabeling. This strand is where the
participatory cluster connects most directly to the program's gauge-theoretic core and to
the block-$GL(K)$ structure of the [[VFE Transformer Program]].

## Information-first foundations and the program's chosen lane

Several sources frame physics as information-first, and the program positions itself
carefully among them. Lucien Hardy's reconstruction ([[hardy-2001-five-axioms]]) derives
finite-dimensional quantum theory from five operational axioms about probabilities, with
only a continuity-of-reversible-transformations axiom distinguishing it from classical
probability. This is the methodological template for the program's "it from bit, then
emergent structure" arc: begin with bare informational primitives and *derive* the rich
geometry ([[Fisher information metric]], [[Quantum information geometry]],
[[Gauge transformation]]) rather than postulate it. Robert Spekkens' toy theory
([[spekkens-2007-toy-theory]]) shows how far a single epistemic restriction reproduces
"quantum" phenomena, demarcating which features of agent agreement/disagreement are mere
incomplete knowledge and which demand the stronger relational/transport machinery — a clean
model of the program's *pre-consensus* regime.

The remaining information-first sources sharpen the program's position by contrast and by
extension. Deutsch and Marletto's constructor theory of information
([[deutsch-2015-constructor-information|deutsch-marletto-2015-constructor-information]]) is the explicit **contrast class**:
both programs are information-first, but constructor theory grounds information in
*objective, agent-independent* possibility/impossibility facts about physical
transformations, whereas the program grounds objectivity in *consensus among coupled
agents*. Citing it lets the manuscript stake out its participatory commitment — it accepts
the priority of information from [[wheeler-1990-it-from-bit]] but sides with relational and
QBist accounts against locating information in observer-independent physical possibility.
Seth Lloyd's computational-capacity bounds ([[lloyd-2002-computational-capacity-universe|lloyd-2002-computational-capacity]]) supply
the *computational* face of "it from bit": physical processes as literal computations on a
finite stock of bits, the natural partner of the program's stance that emergent structure
is produced by *running* an inference computation (iterative VFE minimization) rather than
read off a static substrate; this connects to the [[Emergent spacetime and holography]]
theme. Finally, Connes and Rovelli's thermal time hypothesis
([[connes-rovelli-1994-thermal-time]]) completes the cluster's *observer-relative time*
strand: in a generally covariant theory there is no preferred external time, and the flow
of time emerges as the Tomita–Takesaki modular flow of the observer's statistical state.
Time is therefore state-dependent and observer-relative — the temporal analogue of the
program's stance that dynamical structure is an inference notion driven by an agent's
informational state rather than presupposed.

## Open questions / gaps

- **From analogy to derivation.** The correspondences here — QRF change $\leftrightarrow$
  inter-agent belief transport, failure of FR's assumption C $\leftrightarrow$ nonzero
  holonomy, cross-perspective links $\leftrightarrow$ $\Omega_{ij}$ — are structural
  analogies the program asserts, not theorems. Hardy's reconstruction standard suggests
  the discipline the program should hold itself to: show its geometry *follows* from
  reasonable axioms about agent inference, not merely that it is convenient.
- **Compact vs. non-compact groups.** The QRF and quantum-foundations literature works
  with unitary or compact symmetry groups, whereas the program's classical scale uses the
  non-compact $GL(K,\mathbb{R})$. Whether the participatory correspondence survives this
  change, or only holds at a genuinely quantum scale-0 level, is unresolved.
- **What grounds consensus dynamics?** The no-go results say objectivity must be built;
  Adlam–Rovelli and Healey say agreement is physically/normatively achievable. The program
  models this with belief coupling, but the precise conditions under which transported
  consensus converges (and the meaning of the forbidden *total* consensus, the informational
  heat death) need sharper statement.
- **Does the toy-theory boundary map cleanly?** Spekkens isolates exactly which quantum
  features are not epistemic (nonlocality, contextuality). Whether the program's
  ignorance-plus-coherence regime respects the same boundary, or blurs it, is open.

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
- [[spekkens-2007-toy-theory]] — epistemic-restriction toy model; the pre-consensus regime.
- [[deutsch-2015-constructor-information|deutsch-marletto-2015-constructor-information]] — constructor theory; the agent-independent contrast class.
- [[lloyd-2002-computational-capacity-universe|lloyd-2002-computational-capacity]] — computational-universe bounds; the computational face of "it from bit".
- [[zenil-2013-computable-universe]] — anthology of the digital-physics / "nature as computation" lineage (Zuse, Wolfram, 't Hooft, Lloyd; Penrose foreword); the computational wing of "it from bit," cited as both kin and observer-independent contrast class.
- [[nelson-1967-brownian-motion]] — stochastic mechanics deriving the Schrödinger equation from a conservative diffusion; the physics-from-information ancestor of the entropic-dynamics strand.
- [[bell-2004-speakable-unspeakable]] — Bell's collected foundational papers; the theorem against local observer-independent values that the sharpened Wigner's-friend no-go results extend.
- [[connes-rovelli-1994-thermal-time]] — thermal time hypothesis; observer-relative emergent time.
