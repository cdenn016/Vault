---
type: manuscript
title: "MultiAgentELBO pairing-selection proof and primary-reference review, September 26, 2026"
aliases: ["MultiAgentELBO September 26 pairing-selection result"]
tags: [cluster/multi-agent, cluster/vfe, cluster/gauge-theory, cluster/info-geometry, project/multi-agent, field/mathematics, field/statistics]
created: 2026-09-26
---

# MultiAgentELBO pairing-selection proof and primary-reference review

## Source record

This records the local proof artifact `C:/Users/chris and christine/Desktop/MultiAgentELBO/Theory/ca_selection_proofs.tex`, SHA-256 `4841221a5af9419016db3998e957ef2ce2432ca9687f366583eb834e9808750b`, and its independent reconstructions in `docs/reviews/2026-09-26-theory-deep-review/`: `entropy-balance.md`, `selection-dependencies.md`, `selection-proof-reconstruction.md`, `selection-imprint-verification.md`, and `selection-dependencies-verification.md`. The coordinator confirmed the final proof reconstruction before this ingest. The stable result label remains `conj:phil-contrast-formation`; the label's prefix is historical and is not the mathematical status. Publication and document builds are tracked by the repository review, not inferred from this ingest.

## Model and supported result

The model is the scalar homogeneous four-cycle at one base point, with one shared translation variable per undirected edge, complete neighbor palettes, tied belief/model translations, Gaussian configuration reference, the stated evaluator, identity continuous mobility, and one rate-one clock redrawing the complete assignment. The initial configuration law is $N(m_0,I_{12})$, assignments and source rows start uniform, and deterministic product rows learn from the actual recognition-law marginals.

There exists $T_0>0$ such that, for every fixed $T\in(0,T_0]$ and Lebesgue-almost every fixed mean $m_0$, one perfect matching receives recognition mass tending to one, uniformly on $[t_L,2t_L]$, as learning mobility $\epsilon_L\downarrow0$, where $t_L=C_T\epsilon_L^{-1}\log(1/\epsilon_L)$ and every $C_T>1/\alpha(T)$ is admitted. Here $\alpha(T)>0$ is the unstable matching eigenvalue of the reduced row field at uniform rows. For the frozen-row arm, the matching-mass difference tends to zero for every $T>0$ and every mean.

The proof combines a nonzero analytic transient imprint, actual-law entropy balance, a frozen entropy-production bound whose loss near the row boundary is logarithmic, and dominated escape along the matching direction followed by attraction to its endpoint. The initial law supplies the asymmetry; the kinetics do not select a nonsymmetric law from an invariant preparation. Convergence is pointwise in the fixed mean and is not uniform near the imprint's zero set.

The result does not claim selection for all positive temperatures, arbitrary starting row vectors, a joint vanishing-temperature/mobility limit, all-time persistence at a masked vertex, path-law equivalence with the reduced ODE, or recursive parent formation. These remain separate questions.

## Checked primary references

[[hairer-2011-harris-ergodic-theorem]] supplies the hypothesis-checked weighted ergodicity theorem; its preprint Assumptions 1–2 and Theorem 1.3 were read on pp. 2–3. [[hartmann-2020-coarse-graining-nonreversible-sdes]] separates marginal estimates from path estimates under additional assumptions (Theorems 2.4, 2.7, 2.9, pp. 10–13). [[backhoff-veraguas-2023-specific-relative-entropy]] distinguishes mesh-normalized specific entropy from ordinary path KL (Definition 1, Remark 1, Assumption 1, Theorem 1, pp. 1–3). The latter two papers are comparators; neither is the proof of the four-cycle selection theorem.

The existing immutable [[jotz-2008-closedness-of-the-tangent-spaces-to-the-orbits-of-proper-actions]] is reused. The journal PDF, *Journal of Lie Theory* **18** (2008), 517–521, was additionally downloaded from the publisher. Theorem 2.1 on p. 518 gives closed infinitesimal orbit ranges for smooth proper Banach–Lie actions on Banach manifolds. Corollary 2.5 on p. 520 requires a free proper action and a Hilbert manifold to obtain the quotient manifold and submersion. A weak Fisher metric is not thereby made strong or nondegenerate. [Journal PDF](../pdfs/jotz-2008-proper-actions-journal-lie-theory.pdf).

The existing immutable [[feray-2013-mod-phi-convergence-i-normality-zones-and-precise-deviations]] and its arXiv:1304.2934v4 PDF are reused. Read Definition 9.1 (p. 70), Theorems 9.7–9.8 (p. 71), and Section 9.4.2, Eq. (47) (p. 78). For uniformly bounded variables with a genuine dependency graph, the joint cumulant bound is $2^{r-1}A^{r-1}\mathbb E|Y_{\alpha_1}|$ times the number of spanning trees of the induced occurrence graph. The independence-of-separated-families hypothesis and the graph counting must be checked in each application; generic correlation decay is not that hypothesis.

## Relevance to this research

Updates [[Staged hierarchy formation and RG composability]], [[Gauge-VFE RG research synthesis September 2026]], and [[Gauge-Theoretic Multi-Agent VFE Model]] with the scoped law-level selection result. The reference checks support distinctions on [[Coarse Graining]], [[Riemannian Quotient Manifold]], and [[Central Limit Theorem]]. External research settings are archived separately in [[exa-2026-agent-create-run]] and are not scientific evidence.

## Bibliographic supplement for reused sources

```bibtex
@article{JotzNeeb2008Journal,
  author = {Jotz, Madeleine and Neeb, Karl-Hermann},
  title = {Closedness of the Tangent Spaces to the Orbits of Proper Actions},
  journal = {Journal of Lie Theory}, volume = {18}, pages = {517--521},
  year = {2008}, url = {https://www.heldermann-verlag.de/jlt/jlt18/neebla2e.pdf}
}
@misc{FerayMeliotNikeghbali2015Preprint,
  author = {F{\'e}ray, Valentin and M{\'e}liot, Pierre-Lo{\"i}c and Nikeghbali, Ashkan},
  title = {Mod-{$\phi$} convergence, I: Normality zones and precise deviations},
  year = {2015}, eprint = {1304.2934}, archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1304.2934v4},
  note = {Version 4 dated 2015-11-23; first version 2013}
}
```
