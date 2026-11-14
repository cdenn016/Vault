---
type: paper
title: "A Bayesian Interpretation of the Internal Model Principle"
aliases: ["Baltieri et al. 2025 bayesian internal model principle"]
authors: ["Manuel Baltieri", "Martin Biehl", "Matteo Capucci", "Nathaniel Virgo"]
year: 2025
venue: "arXiv preprint (math.OC); v1 1 Mar 2025, v2 19 Apr 2025"
arxiv: "2503.00511"
doi: "10.48550/arXiv.2503.00511"
url: "https://arxiv.org/abs/2503.00511"
version: "arXiv:2503.00511v2 [math.OC], 19 Apr 2025 (14 pages, two-column). No journal reference is printed on the PDF."
tags: [cluster/vfe, project/multi-agent, field/mathematics, field/cs-ml, field/statistics]
created: 2026-11-13
updated: 2026-11-13
---

# A Bayesian Interpretation of the Internal Model Principle

> [!info] Citation
> Manuel Baltieri, Martin Biehl, Matteo Capucci, Nathaniel Virgo (2025). *A Bayesian Interpretation of the Internal Model Principle*. arXiv preprint (math.OC); v1 1 Mar 2025, v2 19 Apr 2025. [arXiv:2503.00511](https://arxiv.org/abs/2503.00511)

[Local PDF](../pdfs/baltieri-2025-bayesian-internal-model-principle.pdf), 14 pages; retrieved November 13, 2026. Version read: arXiv:2503.00511v2 [math.OC], 19 Apr 2025 (14 pages, two-column). No journal reference is printed on the PDF. Reading basis: Read in full from the extracted text: Sections I-V (pp. 1-12) and Appendices A and B (pp. 12-13); the reference list (pp. 13-14) was skimmed. The first reader worked from the extracted text and did not see the typeset pages. Equations written in set notation, (1)-(13), (16)-(17), (37)-(40), (42)-(43), (47), (49)-(50) and (52), are legible in the text. The commutative diagrams (4), (8), (14), (15), (18)-(21), (51), (53), (54) were reconstructed from the node and arrow labels in the extraction together with the surrounding prose. The string-diagram equations (41), (44)-(46), (48), (55)-(63) and (64)-(70) were not seen as pictures and are reported only at the level of the authors' prose. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-002, page-003, page-004, page-005, page-006, page-009, page-010, page-011, page-012, page-013). Confirmed against those pages: (1) and (5) on p. 2; (8) on p. 3; (10)-(13) on p. 4; (49) and (50) on p. 10; the commuting square (51) and its definition (52) on p. 10; (55) with c defined by discarding X and applying upd_M on p. 11; (57) as the consistency statement of Theorem IV.5 on p. 11; (58)-(63) as the examples on pp. 11-12. Also checked: Definitions II.3, II.7 and III.9-III.10; Assumptions 1-4; Theorem II.13 and its proof (p. 5); Theorem II.15 (p. 6); Proposition IV.2 (p. 10) with its proof in Appendix A; Theorem IV.5 (p. 11) with its proof in Appendix B, which uses positivity (Definition A.1, p. 13); the discussion after Theorem IV.5 on ignored observations, disjoint beliefs and bijective mu_s (p. 11); and the version stamp arXiv:2503.00511v2 [math.OC] 19 Apr 2025.

## TL;DR

The paper restates the Hepburn-Wonham internal model principle for discrete systems as a statement about maps of systems: under the regulation and error-feedback assumptions, the autonomous attracting controller is a model (a surjective, dynamics-preserving image) of the attracting full system, and under a further isomorphism assumption, of the attracting environment. It then proves that any such model between autonomous systems induces a Bayesian filtering interpretation in the possibilistic Markov category $\mathsf{Rel}^+$, with the fiber relation $\mu_s^{-1}$ as interpretation map. The control-theoretic internal model is thereby a special and degenerate case of the interpretation-map notion: observations are ignored and beliefs are disjoint sets.

## Problem & setting

Cybernetics and control theory hold that a good regulator must contain a model of what it regulates, and Bayesian accounts of cognition say that agents model their environments; it is unclear whether the two uses of 'internal model' name the same formal object. The paper takes a first step by formalizing both and relating them. Systems are discrete in time and state, deterministic and fully observable: a set $X$ of states, a set $I$ of inputs and an update function $\mathrm{upd}_X: X \times I \to X$ (Definition II.1), with maps of systems in the sense of charts from categorical systems theory (Myers). The control side follows the algebraic internal model principle of Wonham (1976) and Hepburn and Wonham (1981, 1984), itself descended from Francis and Wonham and from Conant and Ashby. The Bayesian side follows the interpretation maps of Virgo, Biehl and McGregor (2021) and Biehl and Virgo (2022), formulated in Markov categories (Cho and Jacobs, Fritz), here instantiated in $\mathsf{Rel}^+$, the category of sets and left-total relations, which models possibilistic and not probabilistic uncertainty.

## Method

A map of systems $f: \mathsf{X} \to \mathsf{X}'$ (Definition II.3) is a pair $f_s: X \to X'$, $f_i: X \times I \to I'$ with $f_s(\mathrm{upd}_X(x, i)) = \mathrm{upd}_{X'}(f_s(x), f_i(x, i))$ (eq. 5). Definition II.7 calls such a map $\mu: \mathsf{X} \to \mathsf{M}$ a model of the referent $\mathsf{X}$ by the referrer $\mathsf{M}$ when $\mu_s$ is surjective and $\mu_i(x, -)$ is surjective for each $x$; for autonomous systems this is a surjection of states commuting with the dynamics (Remark II.8). The regulation setup (Assumption 1) has an autonomous environment $\mathrm{upd}_E: E \to E$, a plant $\mathrm{upd}_P: P \times E \times C \to P$ and a controller $\mathrm{upd}_C: C \times P \to C$, composed into an autonomous full system $\mathsf{S}$ on $E \times P \times C$ (eq. 13). Assumption 2 posits an attracting subsystem $\mathsf{S}^*$ contained in the target set $K = C \times \tilde K$; Assumption 3 posits that on the attracting set the controller runs open loop, giving an autonomous attracting controller $\mathsf{C}^*_{\mathrm{aut}}$; Assumption 4 posits an isomorphism $\mathsf{S}^* \cong \mathsf{E}^*$. On the Bayesian side, Definition III.10 says that for a deterministic map $c: Y \otimes \Theta \to \Theta$ a Bayesian filtering interpretation is an interpretation map $\psi$ from $\Theta$ to $X$ and a hidden Markov model $\kappa$ from $X$ to $X \otimes Y$ satisfying the consistency equation (48), the condition that $\psi$ is a conjugate prior for filtering with update $c$. For a surjection $f: A \to B$, Construction IV.1 defines the fiber relation $f^{-1}(b) = \{a : f(a) = b\}$ and the closure $\Diamond_f(a) = \{a' : f(a') = f(a)\}$ (eqs. 49-50), and eq. (52) defines the coarsened dynamics $\overline{\mathrm{upd}}_X$ as $\mathrm{upd}_X$ followed by $\Diamond_{\mu_s}$.

## Key results

Theorem II.13 (p. 5): under Assumptions 1 to 3, $\mathsf{C}^*_{\mathrm{aut}}$ models the attracting full system $\mathsf{S}^*$ via the projection. The proof is a few lines, since Assumption 3 supplies the autonomous system and hence surjectivity on inputs. The authors present this as the stronger and more basic statement, in which the controller models the whole system that contains it. Theorem II.15 (p. 6): adding Assumption 4, $\mathsf{C}^*_{\mathrm{aut}}$ models the attracting environment $\mathsf{E}^*$ by composing with the isomorphism; this is their reformulation of the Hepburn-Wonham principle. Proposition IV.2 (p. 10, proof in Appendix A): for autonomous $\mathsf{M}$ modeling $\mathsf{X}$, the square of eq. (51) commutes in $\mathsf{Rel}^+$, that is, applying $\mathrm{upd}_M$ and then $\mu_s^{-1}$ equals applying $\mu_s^{-1}$ and then $\overline{\mathrm{upd}}_X$. Theorem IV.5 (p. 11, proof in Appendix B, using the positivity property of Markov categories with conditionals): with $c: X \otimes M \to M$ defined by discarding the $X$ input and applying $\mathrm{upd}_M$ (eq. 55) and $\kappa$ built from $\overline{\mathrm{upd}}_X$ (eq. 56), the pair $(\mu_s^{-1}, \kappa)$ is a Bayesian filtering interpretation of $c$ (eq. 57). Examples IV.6 and IV.7 (pp. 11-12) apply this to the two theorems above: the autonomous attracting controller carries a filtering interpretation over $\mathsf{S}^*$ and, under Assumption 4, over $\mathsf{E}^*$. The discussion after Theorem IV.5 argues in prose that the induced interpretations are of a restricted kind: the posterior does not depend on the observation, the beliefs are the disjoint fibers of a surjection, the hidden model is a possibilistic approximation of the true dynamics, and a bijective $\mu_s$ gives beliefs concentrated on single states. The authors conclude that Bayesian filtering interpretations are a strictly more general notion of model than the one in the internal model principle. All results are proved set-theoretically or diagrammatically; there are no simulations.

## Limits

The authors restrict to discrete deterministic systems and expect, without proof, that the structural account extends to smooth or stochastic ones. They call Assumption 3 strong, since it excludes error feedback with noise and a tolerance margin, and Assumption 4 hard to motivate. The Bayesian result covers autonomous systems only, the uncertainty is possibilistic, and the model is a map between system descriptions that exists at the level of an external designer, not a mechanism inside the controller. They say they do not fully answer whether cognitive-science and control-theoretic internal models coincide. My observation: Theorem II.13 follows almost directly from Assumption 3, and the induced filtering never uses data, so the paper establishes compatibility of two vocabularies and not a derivation of inference from regulation.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper is the closest theorem-level relative, outside stochastic thermodynamics, of the Bayesian-mechanics claim that persistence entails modeling, and it shows what that claim reduces to when every assumption is explicit in the deterministic discrete case: a surjection from the attracting dynamics onto the controller whose fibers are possibilistic beliefs. For the vault's program it informs two objects. The first is the synchronization-map step: $\mu_s^{-1}$, sending a controller state to the set of full-system states compatible with it, is a set-valued analog of sending internal states to beliefs over external states. The word fibre in the paper means a plain preimage; there is no structure group or connection, so any reading as a statistical fiber is interpretive. The second is coarse-graining to meta-agents: Definition II.7 is a lumpability-type condition, and Proposition IV.2 with Theorem IV.5 says that a dynamically consistent coarse-graining equips the coarse level with a consistent belief about the fine level. That direction of belief is one a meta-agent construction could adopt, but here it is possibilistic, with disjoint beliefs and no Gaussian or Fisher structure. The paper says nothing on transport between agents, natural gradient or Hamiltonian dynamics. The link is moderate for blankets and coarse-graining and weak elsewhere.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Markov blanket interpretation debate]]; [[Coarse Graining]]; [[Meta-agents and hierarchical emergence]]; [[Bayesian Inference]]; [[Generative model]]; [[State space models]]; [[Conjugate-Exponential Family]].

Related sources: [[virgo-2021-interpreting-dynamical-systems-bayesian]]; [[biehl-2023-interpreting-systems-pomdps]]; [[baltieri-2020-predictions-eye-beholder]]; [[smithe-2023-compositional-bayesian-brain]]; [[fritz-2019-a-synthetic-approach-to-markov-kernels-conditional-independence-and-th]]; [[cho-2017-disintegration-and-bayesian-inversion-via-string-diagrams]]; [[dacosta-2021-bayesian-mechanics]]; [[ramstead-2023-bayesian-mechanics]].

## BibTeX

```bibtex
@misc{baltieri2025bayesian,
  author = {Baltieri, Manuel and Biehl, Martin and Capucci, Matteo and Virgo, Nathaniel},
  title = {A {Bayesian} Interpretation of the Internal Model Principle},
  year = {2025},
  eprint = {2503.00511},
  archivePrefix = {arXiv},
  primaryClass = {math.OC},
  doi = {10.48550/arXiv.2503.00511},
  note = {arXiv v2, 19 April 2025}
}
```
