---
type: concept
title: "QBism"
aliases:
  - "Quantum Bayesianism"
  - "Quantum-Bayesianism"
  - "QBist"
  - "Born rule as coherence constraint"
tags:
  - cluster/participatory
  - project/multi-agent
status: draft
created: 2026-06-19
updated: 2026-06-19
---

# QBism

## Definition

**QBism** (Quantum Bayesianism) is the interpretation of quantum theory, developed principally by Fuchs, Mermin and Schack, in which the quantum state is not an objective feature of the world but a single agent's *personal, Bayesian degrees of belief* about the consequences of that agent's own actions on the world. A wavefunction $|\psi\rangle$ encodes one agent's probabilistic expectations — assigned through the Born rule — for the experiences that agent will have upon acting; distinct agents may legitimately assign different states to the same system, and there is no "true" state waiting to be discovered. The Born rule is recast not as a law about objective propensities but as a *normative coherence condition*: an empirically motivated addition to Bayesian probability calculus that keeps an agent's gambling commitments mutually consistent (a Dutch-book-style consistency constraint). In its sharpest technical form ([[fuchs-schack-2013-bayesian-coherence]]), this is the SIC-POVM reformulation, in which fixing credences for a fiducial symmetric informationally complete measurement reduces the Born rule to a single dimension-dependent *deformation of the classical law of total probability* — quantum theory written entirely in probability space, with no objective state ever posited. A measurement, on this view, is an action the agent takes; its outcome is an experience created in that act, and "collapse" is simply the agent's Bayesian update of belief in light of that experience.

## Why it matters here

QBism is the quantum-foundations precedent for the agent-personal commitment that animates the [[Participatory realism (it from bit)]] program of the [[Gauge-Theoretic Multi-Agent VFE Model]]. The project treats an agent's belief — its variational posterior $(\mu, \Sigma, \phi)$ — not as a passive estimator of an external truth but as the fundamental carried quantity, revised by acting; this is the direct structural analogue of QBism's "state-as-personal-credence revised by Bayesian update." The PIFB thread that "probability is an agent's commitment, and physics only constrains how those commitments hang together" is QBism's Born-rule-as-coherence-condition transplanted into the variational setting, where each [[Multi-agent variational free energy]] update is a normative, agent-internal consistency move rather than estimation of a privileged global state. Fuchs's own essay [[fuchs-2017-participatory-realism]] supplies the umbrella term: he names *participatory realism* as the family uniting QBism, relational quantum mechanics, and Wheeler's observer-participancy under the indispensability of a first-person perspective — and the manuscript [[participatory-it-from-bit]] takes its title and orientation from precisely that family. Where QBism foregrounds the single agent, the project's distinctive contribution is to make participatory realism *constructive and multi-agent*: it adds explicit inter-agent transport $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ so that the relation between two agents' beliefs — not any agent's intrinsic content — carries the objective structure (Mermin's "correlations without correlata," [[mermin-1998-correlations]]).

## Details

The chief tension QBism leaves open is *objectivity*: if every state is one agent's credence, what is binding on everyone? Healey's pragmatist reading ([[healey-2017-quantum-revolution]]) marks the middle ground the project navigates toward — Born probabilities as objectively correct *prescriptions* for any suitably situated agent, objective-but-not-ontic. In the project's terms, that prescription is the belief an agent would hold after its dynamics equilibrate against the shared coupling field, and intersubjective bindingness corresponds to beliefs that agree up to [[Parallel transport]] between gauge frames, with residual disagreement quantified by [[Holonomy]] under a [[Gauge transformation]]. QBism sits naturally beside [[rovelli-1996-relational-qm|relational quantum mechanics]]: both are agent-relative, and the project's apparatus is the formal bridge between them. The SIC deformation of total probability also resonates with the project's information-geometric outlook, where structure lives in relations among probability assignments rather than in any underlying state.

## Sources

- [[fuchs-2014-qbism]] — the canonical short introduction: states as personal credence, Born rule as coherence constraint, measurement as participatory action, dissolution of EPR/Bell nonlocality.
- [[fuchs-schack-2013-bayesian-coherence]] — the technical core: the SIC-POVM reformulation of the Born rule as a single dimension-dependent deformation of the law of total probability.
- [[fuchs-2017-participatory-realism]] — Fuchs coins *participatory realism* as the umbrella over QBism, RQM, and Wheeler observer-participancy; names the project's own stance.
- [[mermin-1998-correlations]] — "correlations without correlata," the Ithaca interpretation bridging relational and QBist lines.
- [[healey-2017-quantum-revolution]] — the pragmatist alternative: Born rule as objectively correct prescription, objectivity without ontic states.

## See also

- [[participatory-it-from-bit]]
- [[Participatory realism (it from bit)]]
- [[Observer-dependent facts and Wigner's friend]]
- [[Quantum reference frames]]
- [[rovelli-1996-relational-qm]]
- [[Multi-agent variational free energy]]
- [[Variational free energy]]
- [[Gauge transformation]]
- [[Parallel transport]]
- [[Holonomy]]
