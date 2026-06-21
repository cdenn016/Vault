---
type: concept
title: "Quantum reference frames"
aliases:
  - "QRF"
  - "QRFs"
  - "Quantum reference frame"
  - "Frame covariance"
  - "Reference Frames"
  - "referenceframes"
  - "Reference frames"
tags:
  - cluster/gauge-theory
  - cluster/participatory
  - project/multi-agent
status: draft
created: 2026-06-19
updated: 2026-06-19
---

# Quantum reference frames

## Definition

A *quantum reference frame* (QRF) is a physical reference frame — an orientation, a phase, a position, a clock — that is promoted from an idealized external scaffold to a *dynamical quantum system* in its own right, with its own degrees of freedom, superpositions, and entanglement. Standard quantum mechanics tacitly attaches measurements to a classical rigid rod and clock that carry no quantum state; the QRF program drops that idealization and asks how physical descriptions transform when one changes from one quantum frame to another that may itself be delocalized relative to the first. The central result of [[giacomini-2019-qrf-covariance]] is that the laws of physics can be made *covariant* under such quantum changes of perspective: an explicit unitary "QRF transformation" maps states and observables from particle A's frame to particle B's, generalizing the classical Galilean change of origin, and the Schrödinger dynamics retain their form under it. Properties once thought absolute become frame-relative — a state that is a sharp product state in one QRF can appear entangled and indefinite in another. The operational substrate was laid out earlier by [[bartlett-2007-reference-frames|bartlett-rudolph-spekkens-2007-reference-frames]], who separate *speakable* information (communicable bit strings) from *unspeakable* information (a direction, a phase) that is meaningful only relative to a shared physical frame, with the missing-frame symmetry group $G$ controlling what survives comparison. [[vanrietvelde-2020-qrf-perspective-neutral|vanrietvelde-2020-change-of-perspective]] then recast the whole construction in gauge-theoretic language: a redundant *perspective-neutral* (gauge-invariant) total description exists, and each observer's view is one gauge slice of it, so switching frames is gauge-fixing followed by re-fixing. The deepest version of the stance, [[rovelli-1996-relational-qm]], denies any observer-independent state at all — quantities are defined only relative to a reference system, and there is no view from nowhere.

## Why it matters here

QRFs are the literal physics precedent for the interpretive backbone of [[Participatory realism (it from bit)]]: *gauge covariance is the formal expression of shareability between agents*. Where Giacomini, Castro-Ruiz, and Brukner demand that physical laws be covariant under a change of quantum frame, the [[Gauge-Theoretic Multi-Agent VFE Model]] demands that an agent's belief content be covariant under a change of agent frame, and meets that demand with the same machinery a physicist would. The per-agent gauge frame $\phi_i$ is read not as bookkeeping but as a genuine reference frame in the Bartlett–Rudolph–Spekkens sense; the inter-agent transport $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ is the inferential analogue of the QRF transformation operator, factoring a perspective change through a common reference exactly as the perspective-neutral two-step switch (reduce to neutral, re-embed to a new frame) of [[vanrietvelde-2020-qrf-perspective-neutral|vanrietvelde-2020-change-of-perspective]] does. The speakable/unspeakable split maps directly onto the project's distinction between frame-invariant belief content (objective, shareable) and frame-dependent content (agent-local), which is what the participatory program means by objectivity-as-survival-under-transport. And the quantity that measures how much fails to be shareable — the obstruction to a single global gauge slice, the residue when frames cannot be aligned — is exactly the [[Holonomy]] of the connection. The frame-invariant residual $\mathrm{KL}(q_i \,\|\, \Omega_{ij}[q_j])$ that drives belief coupling is the cognitive counterpart of the QRF-relative comparison: only after transport is comparison meaningful, and the leftover divergence is what no choice of frame can wash away.

## Details

The four sources form a ladder of increasing structure. Rovelli supplies the ontological floor (no absolute states; all quantities relational), Bartlett–Rudolph–Spekkens the operational accounting (frames as physical tokens that degrade with use; the missing-frame symmetry group fixes the invariant/relative split), Giacomini et al. the concrete covariant transformation operator, and Vanrietvelde et al. the explicit identification *frame change = gauge transformation* within constrained-Hamiltonian / principal-bundle formalism. That last identification is what licenses the project to treat [[Agents as fibre-bundle sections]] over a base where no global section is canonical, with each agent's view a local trivialization and frame choice a gauge-fixing. The finding that entanglement and superposition are frame-relative is the physics shadow of the project's claim that "objective" structure is not absolute but is whatever survives a [[Gauge transformation]] between perspectives — the relational reading also shared with [[QBism]], where states are agent-relative probability assignments rather than ontic facts. A useful caution: the QRF literature works with unitary $U(\mathcal{H})$ or compact symmetry groups, whereas the classical scale of this model uses the non-compact real $\mathrm{GL}(K,\mathbb{R})$, so the correspondence is structural rather than a one-to-one mathematical identity, and the model reserves the genuinely quantum $U(\mathcal{H})$ picture for the open scale-0 level.

## Sources

- [[giacomini-2019-qrf-covariance]] — promotes the reference frame to a quantum system; explicit covariant QRF transformation operator; entanglement/superposition shown frame-relative. The most literal precedent for gauge-covariance-as-shareability.
- [[bartlett-2007-reference-frames|bartlett-rudolph-spekkens-2007-reference-frames]] — operational theory of QRFs; speakable vs. unspeakable information; missing frame ⇔ superselection rule; frames as physical, degradable systems.
- [[vanrietvelde-2020-qrf-perspective-neutral|vanrietvelde-2020-change-of-perspective]] — perspective-neutral (gauge-invariant) description; frame change = gauge-fixing then re-fixing; QRF physics as Dirac quantization of a gauge theory.
- [[rovelli-1996-relational-qm]] — relational stance: no observer-independent state; quantities defined only relative to a reference system; "no view from nowhere."
- [[participatory-it-from-bit]] — the manuscript whose shareability-as-gauge-covariance thesis these QRF works underwrite.

## See also

- [[Gauge transformation]]
- [[Participatory realism (it from bit)]]
- [[Agents as fibre-bundle sections]]
- [[QBism]]
- [[Parallel transport]]
- [[Holonomy]]
- [[Multi-agent variational free energy]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
