---
type: concept
title: Psi-epistemic view of the quantum state
aliases: ["Epistemic vs ontic quantum state", "Psi-epistemic / psi-ontic", "Quantum state as information"]
tags:
  - cluster/participatory
  - cluster/participatory/quantum-foundations
  - project/multi-agent
status: draft
created: 2026-06-19
updated: 2026-11-18
---

# Psi-epistemic view of the quantum state

The psi-epistemic view holds that the quantum state $\psi$ is not a direct description of physical reality but a representation of an agent's *incomplete information* about an underlying reality. On this reading the wavefunction is a bookkeeping device for what a participant knows and how confidently it should bet, rather than an objective property carried by the system itself. The position is defined by contrast with **psi-ontic** state-realism, which takes $\psi$ to be (or to be in one-to-one correspondence with) a real physical attribute of the system. The stakes of the distinction are interpretive but consequential: if the state is epistemic, then much of what is taken to be "quantum weirdness" — measurement disturbance, the multiplicity of pure-state preparations of a mixed state, no-cloning, interference — is reinterpreted as the ordinary signature of reasoning under a restriction on attainable knowledge, and the notorious measurement problem softens into a question about belief revision rather than physical law. The view is the technical heart of the agent-centered family surveyed in [[Participatory realism and quantum foundations]]; see also [[QBism]] and [[Participatory realism (it from bit)]].

## Evidence from restricted knowledge: the toy theory

The cleanest piece of constructive evidence is Spekkens' toy theory ([[spekkens-2007-toy-theory]]). It is a *manifestly classical* model — systems have definite ontic states — governed by a single epistemic restriction, the **knowledge balance principle**: in a state of maximal knowledge, the number of answered questions about the underlying ontic state always equals the number left unanswered. With each elementary system carrying four ontic states and an agent permitted to know at most "half," a fixed catalogue of allowed epistemic states (the toy analogues of pure states) follows, and measurement updates knowledge while disturbing the ontic state to preserve the restriction. From this one constraint Spekkens recovers a striking list of supposedly quantum phenomena — noncommutativity, interference, no-cloning, no-broadcasting, the non-uniqueness of mixed-state decompositions, teleportation, dense coding, and mutually unbiased bases — all as artifacts of *fundamentally restricted knowledge* rather than nonclassical ontology. Equally important is where the analogy *fails*: the local toy theory cannot reproduce Bell-inequality violation or genuine contextuality. This failure is the value of the model — it demarcates exactly which quantum features are "merely informational" and which require an irreducibly nonclassical core, giving a sharp boundary on how far ignorance-plus-coherence can go.

## Collapse as belief updating; states as personal credence

If the state is information, then its abrupt change on measurement need not be a separate dynamical law. Johnson and Caticha ([[johnson-2011-entropic-dynamics-measurement|johnson-caticha-2011-measurement-problem]]) argue within the Entropic Dynamics framework that quantum theory's two modes of evolution — smooth unitary (Schrödinger) flow and abrupt "collapse" — are two limits of *one* process: entropic updating of probabilities. Collapse is the Bayesian/entropic conditioning of a distribution on newly acquired data, continuous with ordinary inference, so the projection postulate is dispensable and the measurement problem dissolves once $\psi$ is read as an agent's information. The personalist version is made quantitatively precise by Fuchs and Schack ([[fuchs-schack-2013-bayesian-coherence]]), the technical core of QBism: the Born rule is recast not as a law about objective propensities but as a normative *coherence condition* an agent imposes on its own credences. Using a symmetric informationally complete measurement (SIC-POVM) as a fiducial reference, the rule becomes a fixed, dimension-dependent deformation of the classical law of total probability connecting an agent's credences for the fiducial outcomes to those for any other measurement. Schematically, the quantum content reduces to one relation of the form $q(j) = \big[(d+1)\textstyle\sum_i p(i)\,r(j|i)\big] - 1/d$, a near-classical deformation living entirely in probability space with no objective state anywhere in it. Carlo Rovelli's relational quantum mechanics ([[rovelli-1996-relational-qm]]) supplies the metaphysical sibling: there is *no observer-independent state*; quantities are definite only relative to a second system that has interacted with the first, the wavefunction encodes what one system "knows" about another, and measurement is just a physical interaction in which information (correlation) is acquired. Because there is no view from nowhere, there is no frame-independent fact about when collapse happens — different observers can give different, equally valid accounts of the same events. The price of the epistemic reading, made vivid by the [[Observer-dependent facts and Wigner's friend]] no-go results, is that objectivity can no longer be assumed; it must be *built* from inter-agent relations.

## Sources

- [[spekkens-2007-toy-theory]] — epistemic-restriction toy model; "quantum" phenomena from restricted knowledge, and the nonlocality/contextuality boundary.
- [[fuchs-schack-2013-bayesian-coherence]] — the QBist technical core; Born rule as a personalist coherence constraint via SIC-POVMs.
- [[johnson-2011-entropic-dynamics-measurement|johnson-caticha-2011-measurement-problem]] — collapse as entropic/Bayesian updating; unitary evolution and collapse as one inference process.
- [[rovelli-1996-relational-qm]] — relational QM; no observer-independent state, the wavefunction as relative information.
