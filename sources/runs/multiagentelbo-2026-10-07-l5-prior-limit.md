---
type: run
title: "MultiAgentELBO L5 anchored history prior spatial existence"
aliases: ["L5 anchored prior infinite-volume construction"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/physics, field/statistics]
created: 2026-10-07
updated: 2026-10-07
---

# MultiAgentELBO L5 anchored history prior spatial existence

The declared positively anchored Gaussian-increment link-history prior now has an analytical spatial existence construction: a volume-uniform one-cell entropy bound gives generator second moments and tightness, and finite-cylinder conditional identities give subsequential infinite-volume DLR laws for the unchanged nonlinear based-plaquette action. The fixed-horizon proof was independently reconstructed. It establishes neither uniqueness nor convergence of whole-slice episode kernels, a full agent joint, or the two-index RG limit. Both N8192 numerical readback failures remain unresolved; no experiment or GPU was used.

## Source and mathematical result

Codex (2026), *L5 anchored history prior: a spatial infinite-volume limit*, MultiAgentELBO research record, source revision `7de84996368e4b4d3f7bfb9499a6ee75d94ab8b1`. The [complete proof](https://github.com/cdenn016/MultiAgentELBO/blob/7de84996368e4b4d3f7bfb9499a6ee75d94ab8b1/docs/research/2026-10-03-latent-link-rg-plan/L5-PRIOR-LIMIT.md), [independent reconstruction](https://github.com/cdenn016/MultiAgentELBO/blob/7de84996368e4b4d3f7bfb9499a6ee75d94ab8b1/docs/research/2026-10-03-latent-link-rg-plan/L5-PRIOR-LIMIT-CHECK.md), and [source intake](https://github.com/cdenn016/MultiAgentELBO/blob/7de84996368e4b4d3f7bfb9499a6ee75d94ab8b1/docs/research/2026-10-03-latent-link-rg-plan/evidence/l5-prior-limit-intake-20261007.json) preserve the derivation and its correspondence to the live theory and code. This is an analytical investigation filed with the program's run records; no sampling experiment was performed.

```bibtex
@misc{codex2026l5priorlimit,
  author = {Codex},
  title = {L5 Anchored History Prior: A Spatial Infinite-Volume Limit},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/blob/7de84996368e4b4d3f7bfb9499a6ee75d94ab8b1/docs/research/2026-10-03-latent-link-rg-plan/L5-PRIOR-LIMIT.md},
  note = {MultiAgentELBO research record, revision 7de84996368e4b4d3f7bfb9499a6ee75d94ab8b1}
}
```

At fixed $c_*$, a cell contains the two complete primitive generator histories. For fixed $K,T$, positive anchor precision $a$, mass $m\geq0$, and spatial coefficient $c\geq0$, the edge reference has precision $(aI_T+mL_{\mathrm{path},T})\otimes I_{K^2}$. The nonlinear action sums the original ordered based plaquette Frobenius defects. The actual L5 instance is $K=2$, $T=16$, $a=.3^{-2}$, $m=16$, and $c=0$ or $.25$. The law is over generator coordinates, not Haar measure on the full group. The temporal path has no closing edge.

Writing $C_0$ for the finite reference expectation of one cell's local action and $q$ for the two-history Gaussian cell reference, the proof derives $D(P_{r,s}^{\{0\}}\|q)\leq C_0$, $\mathbb E\|Y_0\|^2\leq (4/a)(C_0+K^2T\log2)$, and $\mathbb E\Phi_0\leq C_0$, uniformly in spatial volume. Periodic lifts are tight on the countable product. Any weakly convergent subsequence has the declared spatial DLR conditionals because their action has finite range, their normalized kernels map continuous cylinder tests to continuous cylinder tests, and the finite-torus identities pass to the limit. The proof explicitly avoids conditioning a periodic lift on its whole infinite exterior, which would reveal its interior through periodic copies.

The live intake was `manuscripts/MultiAgentELBO_Theory/c08b_lie_links.tex`, the generator-history definition and proposition, their appendix proofs, and the countable-law/two-index discussion in `b06_wilsonian_limits.tex` and lattice typing question in `b07_lattice_rg.tex`. The finite-normalization proof was existing work; the volume-uniform bound and limiting construction supply the previously open prior-existence step. The source trace confirms that seeded matter states do not enter the L5 prior. Rœlly and Zass's [2020 entropy-method paper](https://doi.org/10.1007/s10955-020-02559-3) and its [2022 correction](https://doi.org/10.1007/s10955-022-02972-w) were consulted as methodological background, without applying their marked point-process theorem to this lattice model.

## Relevance to this research

This gives a noncompact prior-law input for subsequent retained-state and coarse-kernel constructions. It controls spatial subsequences and bounded continuous local observables. It gives no quantitative rate, uniqueness, phase selection, uniform exponential tails, growing-path moment bound, vanishing-anchor limit, or infinite episode horizon. Spatial DLR kernels do not by themselves establish convergence of the manuscript's whole-slice backward-normalized episode kernels or temporal Markovness at infinite spatial volume. The alternative nonlinear time-like kinetic term was not analyzed.

The next obligation is the actual retained state and compatible fixed-depth kernels, followed by integrability and approximation bounds useful as block size and surviving parent count both grow. Original joint descent, normalized belief/model channels, recognition and prediction accuracy, endogenous formation, O1/O3/O5, graph-family loop choice S1, and the complete RG program remain open. [[multiagentelbo-2026-10-07-l5-exponential-diagnosis]] retains the numerical failure state; the existence proof neither uses nor repairs those computations. No manuscript or older immutable source was edited. The broader goal remains active.

[[Gauge-Theoretic Multi-Agent VFE Model]]
[[Staged hierarchy formation and RG composability]]
[[Renormalization-group flow of beliefs]]
[[Mathematics MOC]]
[[Physics MOC]]
[[Statistics MOC]]
