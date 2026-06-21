---
type: concept
title: Belief perseverance and confirmation bias
aliases:
  - Confirmation bias
  - Belief perseverance
  - Epistemic inertia (cognitive)
  - Causal Explanation
  - "Explanation-based belief perseverance"
tags:
  - cluster/social-physics
  - cluster/vfe
  - project/social-physics
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Belief perseverance and confirmation bias

## Definition

**Belief perseverance** is the tendency to retain a belief after the evidence on which it was originally founded has been discredited or withdrawn. In the canonical paradigm a participant is given fabricated feedback that induces a belief (for instance, that they have an unusual aptitude for a discrimination task), the feedback is then explicitly revealed to be bogus, and yet the induced belief persists at a level well above baseline. **Confirmation bias** is the complementary distortion in the *acquisition* of evidence: the tendency to preferentially seek, attend to, weight, and remember information that confirms a held belief while discounting or reinterpreting disconfirming information. The two phenomena are facets of a single asymmetry — incoming evidence is filtered through, and assimilated to, the belief already in place — and both are conventionally catalogued as departures from normative Bayesian rationality ([[nickerson-1998-confirmation-bias]], [[anderson1980-belief-perseverance|anderson-1980-belief-perseverance]]).

## Why it matters here

The founding manuscript of [[SocialPhysics]], [[belief-inertia]] ("The Inertia of Belief"), reframes both effects not as failures of reasoning but as geometric consequences of **epistemic inertia**. Once a belief is modeled as a point on a statistical manifold carrying an inertial mass proportional to its precision ([[Belief inertia]], [[Mass as Fisher information]]), resistance to revision and the asymmetric weighting of new evidence follow from the dynamics rather than from any added irrationality term. A high-precision (high-mass) belief is, by construction, hard to accelerate: the same gradient that would readily move a diffuse belief produces only a small displacement in a confident one. What looks from the outside like stubbornness is the manifold equivalent of a heavy body responding weakly to a force.

This recasting matters for the program because it lets perseverance and confirmation bias be *predicted* from the precision structure of an agent rather than postulated. It also ties the two cognitive phenomena to the same machinery that, at the population level, produces [[Echo chambers and polarization]]: an agent whose belief has high mass both resists correction (perseverance) and, through the attention coupling, weights neighbors who agree more heavily than those who disagree (a social form of confirmation bias).

## Details

### Confirmation bias from precision-weighted assimilation

In the multi-agent free energy the influence of a neighbor (or an observation) on agent $i$ is mediated by a precision-weighted, gauge-transported coupling $\beta_{ik}\,D_{\mathrm{KL}}(q_i\|\Omega_{ik}\cdot q_k)$. The effective pull a source exerts is scaled by the *transported precision* it presents and by the attention weight $\beta_{ik}$, which itself falls off with the KL divergence between the agent's belief and the source. Evidence (or an interlocutor) that already lies close to the held belief is assigned a larger $\beta$ and is assimilated; evidence that lies far away is down-weighted. Preferential weighting of confirming information is therefore not an extra rule but the behavior of the same attention kernel that drives bounded-confidence dynamics ([[hegselmann-2002-opinion|hegselmann-krause-2002]], [[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]]). The asymmetry sharpens further when the source's apparent precision is high: a confident, agreeing neighbor contributes a large block to agent $i$'s mass and pulls hard, while a confident *disagreeing* neighbor is suppressed by the divergence-sensitive $\beta$.

### Causal explanation as the engine of perseverance

A specific cognitive mechanism underwrites why perseverance is so robust: people generate a *causal story* to account for a proposed fact, and that self-constructed explanation then sustains the belief even after the original evidence is fully discredited. Anderson, Lepper and Ross showed this is the engine of belief perseverance — once a causal account is in place, debriefing fails to undo the belief ([[anderson1980-belief-perseverance|anderson-1980-belief-perseverance]]). In the program's terms the explanation acts as a *hysteresis term* resisting evidential updating: it is a psychological microfoundation for the high-mass, slow-to-revise dynamics formalized below, and a route by which an entrenched explanation behaves like accumulated inertia rather than a freshly weighed posterior.

### Belief perseverance as high-mass resistance and overshoot

The four-part mass $M_i = \bar\Lambda_{p_i} + \Lambda_{o_i} + \sum_k \beta_{ik}\tilde\Lambda_{q_k} + \sum_j \beta_{ji}\Lambda_{q_i}$ ([[Mass as Fisher information]]) sets how strongly a belief resists revision. When the evidence underwriting a belief is withdrawn, the corresponding observation precision $\Lambda_{o_i}$ is removed, which lowers the stiffness $K_i$ that pulls the belief back toward its prior — but it does *not* erase the inertia the belief has already accumulated, nor the social and prior precision that continue to anchor it. In the overdamped (gradient-flow) limit the belief relaxes back only slowly, on a timescale set by mass over damping; in the underdamped (Hamiltonian) regime it can coast past, or remain displaced from, the position the now-corrected evidence would warrant. The manuscript's closed forms make this quantitative: the continued-influence (coasting) time scales as $\tau_{\mathrm{relax}} = M_i/\gamma_i$ and the underdamped envelope decays as $\tau_{\mathrm{env}} = 2M_i/\gamma_i$, both *linear in precision*. Perseverance is thus predicted to grow with the confidence at which the belief was held — the discredited-but-retained belief is simply a massive object still in motion ([[Hamiltonian belief dynamics]]).

### Self-reinforcing drift from adaptive self-coupling

A sharper mechanism arises when the prior self-coupling weight is promoted to a per-agent variational precision with a Gamma-type regularizer, giving the stationary value
$$
\alpha_i^*(c) = \frac{c_0}{b_0 + D_{\mathrm{KL}}(q_i\|p_i)} .
$$
This $\alpha_i^*$ rescales the prior block of the mass, $M_i = \alpha_i^*\,\bar\Lambda_{p_i} + \dots$, and it *decreases* as the belief drifts away from its prior. Prior anchoring therefore weakens exactly where the belief has already moved the most. The result is a positive feedback: the further a belief drifts, the less the prior restrains further drift, so an initial perturbation can be self-amplifying rather than self-correcting. This supplies a dynamical, geometric route to entrenchment that mirrors the psychology of belief perseverance without invoking a separate "motivated reasoning" term.

### The empirical comparison: near critical damping

The manuscript is candid that the inertial (underdamped) predictions are an *ansatz* and remain empirically unvalidated ([[Belief inertia]]). Its single empirical comparison, on a helicopter-prediction estimation task, lands the fitted dynamics near **critical damping** — the boundary regime $\gamma_i^2 \approx 4K_iM_i$ at which the system makes the fastest non-oscillatory approach to equilibrium and the framework reduces to a delta-rule (first-order) update. Near-critical damping means that, for this dataset, the distinctive oscillatory signatures (overshoot, ringing, resonance) are not pronounced, and the second-order model is observationally close to the overdamped classical limit. The honest reading is that perseverance-as-inertia is consistent with the data but not yet *distinguished* from a well-tuned first-order account by it; demonstrating overshoot or resonance in a genuinely underdamped regime is the open empirical task.

## Sources

- [[nickerson-1998-confirmation-bias]] — review of confirmation bias as a ubiquitous, multi-form tendency to favor belief-consistent information.
- [[anderson1980-belief-perseverance|anderson-1980-belief-perseverance]] — experimental demonstration that beliefs persist after their evidential basis is discredited.
- [[belief-inertia]] — The Inertia of Belief (primary manuscript; the inertial reframing, the four-part mass, the adaptive self-coupling, and the helicopter-task comparison are taken from this file).

## See also

- [[Belief inertia]]
- [[Mass as Fisher information]]
- [[Hamiltonian belief dynamics]]
- [[Echo chambers and polarization]]
- [[Multi-agent variational free energy]]
- [[Fisher information metric]]
- [[SocialPhysics]]
