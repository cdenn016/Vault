---
type: concept
title: Predictive processing and controlled hallucination
aliases:
  - "Perception as inference"
  - "Controlled hallucination"
  - "Predictive mind"
  - "Predictive Processing"
tags:
  - cluster/participatory
  - cluster/participatory/consciousness
  - project/multi-agent
status: draft
created: 2026-06-19
updated: 2026-06-19
---

# Predictive processing and controlled hallucination

Predictive processing is the doctrine that perception is not a passive readout of sensory inputs but an active, inference-like construction: the brain maintains a hierarchical generative model of the hidden causes of its sensations and continually generates top-down predictions, propagating upward only the residual *prediction error* — the part of the signal it failed to anticipate. On this view the percept *is* the prediction, corrected (not built) by sensory evidence, which is why the modern slogan for the experienced world is **controlled hallucination**: a hallucination because its content is endogenously generated, controlled because it is reined in by incoming error. The lineage is explicitly Helmholtzian. Helmholtz's nineteenth-century doctrine of *unconscious inference* ([[helmholtz-1867-physiological-optics]]) already held that, because the retinal image is consistent with many world states, the visual system must resolve this underdetermination by inferring the most probable external cause under prior experience — the proto-Bayesian, prior-times-likelihood structure from which the contemporary program descends. Clark's *Surfing Uncertainty* ([[clark-2016-surfing-uncertainty]]) and Hohwy's *The Predictive Mind* ([[hohwy-2013-predictive-mind]]) are its two canonical philosophical statements, and Seth's *Being You* ([[seth-2021-being-you]]) its most widely read scientific synthesis, the source of the "controlled hallucination" framing used here.

## Mechanism: hierarchical prediction-error minimization with precision weighting

The unifying computational motif is a single operation applied recursively across a cortical hierarchy: minimize prediction error, weighted by its expected reliability. Each level holds a belief about the level below and sends down a prediction $\hat{x}$; the level below returns the error $\varepsilon = x - \hat{x}$ between that prediction and its own current estimate. Crucially, errors are not all treated equally — each is scaled by a **precision** $\pi$ (the inverse variance, the brain's estimate of how reliable that error signal is), so the quantity that drives belief revision is the precision-weighted error $\pi\,\varepsilon$. Optimizing precision is what the program identifies with **attention**: turning up $\pi$ on a channel lets its errors override prior expectations, turning it down makes the prediction dominate. Clark ([[clark-2016-surfing-uncertainty]]) shows that this one motif unifies perception (inference about causes), action (active inference, where the agent moves the body to *make* its predictions true rather than revising the prediction), and attention (precision control); the "surfing" metaphor casts the agent as riding waves of sensory prediction error rather than passively receiving inputs. Hohwy ([[hohwy-2013-predictive-mind]]) presses the *internalist* corollary hardest: because the brain is separated from the world by a sensory/statistical boundary (a Markov-blanket-like "evidentiary boundary"), the mind is in a sense *secluded*, inferring its world from behind a veil of sensory effects rather than reaching out to grasp it directly. Seth ([[seth-2021-being-you]]) extends the same machinery inward, casting selfhood — and especially the interoceptive sense of *being alive* — as itself a controlled hallucination grounded in homeostatic, life-preserving inference (the "beast machine"), and reframes the research agenda as the *real problem*: explaining the phenomenology in terms of mechanism rather than first dissolving the metaphysical hard problem (see [[Consciousness and the hard problem]]). All four sources present this informally; the formal descendant is the [[Variational free energy]] functional, whose [[Prediction error]] and [[Precision weighting]] terms make the verbal machinery explicit (the "Helmholtz machine" lineage, via [[Free-energy principle active inference]]).

## Relevance to this research

Predictive processing supplies the cognitive-science motivation for the project's frame-relative, participatory reading of an agent's accessible reality. Where the physics-side sources argue from quantum foundations that an agent's perspective is ineliminable (see [[Participatory realism and quantum foundations]]), the predictive-processing literature reaches the same conclusion empirically and from the inside: the perceived world is the perceiving system's precision-weighted best guess, so an agent never confronts a pre-given world but only its own model of it. This is the neuroscientific cousin of [[Participatory realism (it from bit)]], and Hohwy's *secluded* mind behind an evidentiary boundary is the cleanest statement of the premise the manuscript [[participatory-it-from-bit]] leans on for its noumenal-pullback claim — the agent reading its world only through sensory effects, in its own local frame, is exactly what the program models as frame-relative content registered and transported between [[Agents as fibre-bundle sections]]. The program formalizes the verbal terms directly: [[Prediction error]] and [[Precision weighting]] become explicit components of [[Variational free energy]] and of the precision-weighted couplings in [[Multi-agent variational free energy]], where each agent is a Seth-style inferential self maintaining its own controlled hallucination and social dynamics arise when many such self-models interact. The hierarchical generative model maps onto the project's multi-scale structure ([[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]]). Finally, Seth's "beast machine" — a self-model that persists because maintaining it is what keeps the agent viable — resonates with the program's dynamical reading of belief: a self resists perturbation, which is the phenomenological face of [[Belief inertia]] and [[Mass as Fisher information]], and connects to the broader belief-momentum picture of [[Opinion dynamics]] in the social setting.

> [!note] Editorial: These four sources are conceptual and motivational rather than technical. Quantitative claims in the project's manuscripts should be cited to the primary active-inference and information-geometry sources, not to these monographs. Clark's embodied/action-oriented reading and Hohwy's internalist-seclusion reading disagree internally; the project draws its participatory motivation from predictive processing *generally* and need not adjudicate that dispute.

## Sources

- [[helmholtz-1867-physiological-optics]] — unconscious inference; perception as construction under priors (the historical wellspring).
- [[clark-2016-surfing-uncertainty]] — the embodied, action-oriented philosophical synthesis; prediction-error minimization unifying perception, action, attention.
- [[hohwy-2013-predictive-mind]] — the internalist statement; the secluded mind behind an evidentiary boundary.
- [[seth-2021-being-you]] — the scientific synthesis; "controlled hallucination," the self as inference, the beast machine.
