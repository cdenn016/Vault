---
type: concept
title: "Dressing field method"
aliases:
  - "Dressing field"
  - "Dressing fields"
  - "Dressing-field method"
tags:
  - cluster/gauge-theory
  - project/transformer
status: draft
created: 2026-09-23
updated: 2026-09-23
---

# Dressing field method

## Definition

The dressing field method reduces a gauge symmetry by a change of field variables. It is distinct from gauge fixing, spontaneous symmetry breaking, and reduction of the principal bundle ([[fournel-2014-gauge-invariant-composite-fields]], Section 1). Consider a gauge theory with structure group $H$, a connection $\alpha$, and a matter field $\varphi$, with gauge transformations $\alpha^\gamma=\gamma^{-1}\alpha\gamma+\gamma^{-1}d\gamma$ and $\varphi^\gamma=\rho(\gamma^{-1})\varphi$. A **dressing field** is a field $u$, built from the theory's own variables and valued in a group $G\supseteq H$, that transforms as $u^\gamma=\gamma^{-1}u$. The Main Lemma of [[fournel-2014-gauge-invariant-composite-fields]] then makes the composite fields $\hat\alpha=u^{-1}\alpha u+u^{-1}du$ and $\hat\varphi=\rho(u^{-1})\varphi$ gauge invariant, together with their curvature and covariant derivative. The dressing resembles a gauge transformation by $u$ but is not one, because $u$ is not an element of the gauge group. When $u$ dresses only a normal subgroup $J$, the Lagrangian rewritten in the dressed variables is an $H/J$ gauge theory ([[francois-2019-artificial-gauge-symmetries]], Section 2).

## Why it matters here

[[francois-2019-artificial-gauge-symmetries]] (Section 2.2) turns the method into a test of what a gauge symmetry is worth. Criterion (C1) says that a local dressing field, whose value at a point depends only on the fields at that point, signals an artificial symmetry, one that can be erased at no cost, as in the Stueckelberg rewriting of the Proca model. Criterion (C2) says that a symmetry admitting only non-local dressing fields, as for Dirac's dressed electron, is substantial. The test makes operational Kretschmann's objection that covariance can be obtained by reformulation and is then physically vacuous ([[norton-1993-general-covariance]], Section 5.1). François's examples include the tetrad of general relativity, a local dressing field for local Lorentz symmetry when no spinor matter is present, and the vielbein "clock field" of massive gravity.

## In this work

The September 2026 v2 revision of the GL(K) attention manuscript (`manuscripts/Attention/GL(K)_attention_v2.tex`, Section 3.2, "Covariance of the attention operator") applies the method to its learned frames. A passive frame change sends $(\mu_i,\Sigma_i,U_i)$ to $(g_i\mu_i,g_i\Sigma_ig_i^\top,g_iU_i)$ and leaves the reference moments $\xi_i=U_i^{-1}\mu_i$ and $C_i=U_i^{-1}\Sigma_iU_i^{-\top}$ unchanged ([[dennis-2026-glk-matrix-links-2026-09-20]]). These are the dressed composite fields, and the frame $U_i$ is a local dressing field. The covariance proof uses only this invariance, so any operator that reads the states through $(\xi_i,C_i)$ is covariant in the same sense, including dot-product attention on dressed means. By (C1) the local $\mathrm{GL}(K)$ covariance is artificial, and it places no constraint on the learned maps $S_Q$, $S_K$, $T$, $O$. In the language of [[weiler-2021-coordinate-independent-cnns]] (Sections 2.1.1 and 3.1.3), the learned frames fix an $\{e\}$-structure, a global frame field that admits no nontrivial gauge transformations.

Gauge-equivariant networks on manifolds ([[cohen-2019-gauge-cnn]], [[weiler-2021-coordinate-independent-cnns]]) are the contrasting case. There the frame is geometric data defined only up to the structure group, and weight sharing forces the shared maps to be intertwiners. The revision records that, for $G=\prod_b\mathrm{GL}(d_b)$, this requirement would confine each $O_hT_h$ to $\bigoplus_b\mathbb RI_{d_b}$. The rank deficiency, block mixing, and composition defect of its matrix links are therefore available only because the frames are learned. See [[GL(K) gauge-equivariant attention]], [[Gauge transformation]], and [[Gauge equivariance and geometric deep learning]].

> [!note] Editorial: The convention match with the Main Lemma is exact. With $\gamma=g_i^{-1}$ the manuscript's law reads $U_i^\gamma=\gamma^{-1}U_i$ and $\mu_i^\gamma=\rho(\gamma^{-1})\mu_i$, so the dressed matter field $\hat\varphi=\rho(U_i^{-1})\mu_i$ is exactly $\xi_i$.

## Sources

- [[fournel-2014-gauge-invariant-composite-fields]] — Main Lemma and examples; origin of the method.
- [[francois-2019-artificial-gauge-symmetries]] — criteria (C1) and (C2) for artificial versus substantial gauge symmetry.
- [[norton-1993-general-covariance]] — Kretschmann's objection (Section 5.1) and the general-covariance debate.
- [[weiler-2021-coordinate-independent-cnns]] — $G$-structures and $\{e\}$-structures in coordinate-independent CNNs.
- [[cohen-2019-gauge-cnn]] — gauge-equivariant convolution with frames defined up to the structure group.
- [[dennis-2026-glk-matrix-links-2026-09-20]] — the passive frame action and reference moments of the matrix-link manuscript.

## See also

[[GL(K) gauge-equivariant attention]] · [[Gauge transformation]] · [[Diffeomorphism invariance]] · [[Gauge Theory]] · [[Gauge equivariance and geometric deep learning]]
