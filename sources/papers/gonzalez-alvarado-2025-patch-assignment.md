---
type: paper
title: Riemannian Patch Assignment Gradient Flows
aliases:
  - Gonzalez-Alvarado 2025 patch assignment flows
authors:
  - Gonzalez-Alvarado, Daniel
  - Schlindwein, Fabio
  - Cassel, Jonas
  - Steingruber, Laura
  - Petra, Stefania
  - Schnörr, Christoph
year: 2025
arxiv: "2504.13024"
url: https://arxiv.org/abs/2504.13024
doi: 10.1007/978-3-031-92369-2_21
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-08-12
updated: 2026-08-12
---

# Riemannian Patch Assignment Gradient Flows

> [!info] Citation
> Daniel Gonzalez-Alvarado, Fabio Schlindwein, Jonas Cassel, Laura Steingruber, Stefania Petra and Christoph Schnörr. "Riemannian Patch Assignment Gradient Flows." In *Scale Space and Variational Methods in Computer Vision* (SSVM 2025), Lecture Notes in Computer Science vol. 15668, Springer, 2025, chapter 21. [doi:10.1007/978-3-031-92369-2_21](https://doi.org/10.1007/978-3-031-92369-2_21); preprint [arXiv:2504.13024](https://arxiv.org/abs/2504.13024). Affiliations: Heidelberg University (Image and Pattern Analysis Group; Research Station Geometry and Dynamics) and University of Augsburg (Theoretical Medicine / Anatomy and Cell Biology; Mathematical Imaging Group & CAAPS). Funded by DFG Excellence Strategy EXC-2181/1 – 390900948 (Heidelberg STRUCTURES Excellence Cluster) and DFG grant SCHN 457/17-2 within SPP 2298.

## TL;DR

**Patch assignment flows (P-AFs)** extend the [[Assignment flow]] framework so that regularisation of a labeling is encoded *entirely* by a **dictionary of labeled template patches** and the adjacency graph those templates induce, rather than by a spatial affinity matrix. The state is a field of probability vectors over the dictionary, living on a product of probability simplices with the **Fisher-Rao product metric**; the flow is the Riemannian gradient ascent of a bilinear patch-consistency objective. Two structural results are proved: the flow is independent of the (arbitrary) orientation of the underlying graph, and it is a **critical point of a Lagrangian action functional** whose kinetic term is the Fisher-Rao norm of $\dot P$. Experiments are illustrative, and include uncertainty quantification of label assignments obtained from symmetries of the patch dictionary.

## Problem & setting

The basic assignment flow $\dot W=R_W[\Omega W]$ evolves assignment vectors $W_i\in\mathcal S_c$ (probability simplices over $c$ labels) at each vertex of a graph, coupled through a spatial interaction matrix $\Omega(t)$ that can be learned from data; geometric integration of the flow generates a network, so assignment flows serve as "neural ODEs on graphs". Vectorised, the flow reads $\dot w=R^{\mathfrak v}_w[(\Omega\otimes I_c)w]$, which invites the generalisation $\dot w=R^{\mathfrak v}_w[(\Omega\otimes\Omega_c)w]$ so that **labels interact with each other**, not only positions with positions — a formulation general enough to cover multi-population and multi-game dynamics.

The paper's specific choice is to realise *both* the spatial and the label interaction through a **labeled patch dictionary**. The related work being displaced is the classical patch literature for denoising and restoration (structure sparsity, Gaussian-mixture priors), which uses *continuous* patches; here each patch template is *labeled*, so a label represents an equivalence class of signals and the object being regularised is a structured prediction, not a reconstruction.

**Geometry.** $\mathcal S_c$ is the relative interior of the simplex with the Fisher-Rao metric $g^{\mathcal S_c}_w(u,v)=\langle u,\mathrm{Diag}(w)^{-1}v\rangle$; its inverse in ambient coordinates is the **replicator operator** $R_w x=w\circ x-\langle x,w\rangle w$. The assignment manifold is the product $\mathcal S_c^n$ with the Fisher-Rao product metric, and assignment flows are the coupled replicator system $\dot W=R_W[F(W)]$ with fitness/payoff function $F$ — the same object studied in evolutionary game theory and population dynamics.

## Method

**Patch dictionary graph.** For a directed grid graph $\mathcal G_{\mathcal V}=(\mathcal V,\mathcal E_{\mathcal V})$ with edges split into horizontal and vertical classes, a labeled patch dictionary $\mathcal D$ is a set of labeled templates of common size $p$. A nonnegative similarity $\omega_{d_{[i]}d'_{[j]}}$ — e.g. the normalised agreement of the two templates on the intersection of their supports, or its binary variant — induces the **patch dictionary graph** $\mathcal G_{\mathcal D}=(\mathcal D,\mathcal E_{\mathcal D})$ and, by translation invariance, two asymmetric template adjacency matrices $\Omega^h_{\mathcal D},\Omega^v_{\mathcal D}$.

**Flow.** The state is $P\in\mathcal S^n_{|\mathcal D|}$, one distribution over dictionary templates per vertex. The objective is patch consistency
$$J(P)=\big\langle P,\;A^h_{\mathcal V}P(\Omega^h_{\mathcal D})^\top+A^v_{\mathcal V}P(\Omega^v_{\mathcal D})^\top\big\rangle=\sum_{ij\in\mathcal E^h_{\mathcal V}}\langle P_i,\Omega^h_{\mathcal D}P_j\rangle+\sum_{ij\in\mathcal E^v_{\mathcal V}}\langle P_i,\Omega^v_{\mathcal D}P_j\rangle,$$
and the **patch assignment flow** is the Riemannian ascent flow
$$\dot P=\mathrm{grad}\,J(P)=R_P\big[\mathcal A_\Omega(P)+\mathcal A^\top_\Omega(P)\big],\qquad P(0)=P_0.$$
At convergence, vertex $i$ is assigned the template $d=\arg\max_d P_{id}(\infty)$ and the class label is that template's centre value.

**Initialisation and the single parameter.** An initial *local* labeling $W^0$ (from any pixelwise classifier — an SVM in the real-data experiment) is softmaxed against the dictionary, $P_{0;i,d}\propto\exp\langle W^\lambda_{[i]},d_{[i]}\rangle$ with $W^\lambda_i=(1-\lambda)W^0_i+\lambda\mathbb 1_{\mathcal S_c}$. The mixing weight $\lambda\in[0,1]$ balancing data against dictionary regularisation is the **only user parameter**.

**Uncertainty quantification.** For binary problems the *mean patch assignment function* $\overline{\ell_{\mathcal V}}(i)=\frac1{|\mathcal D|}\sum_{j\in[i]_{\mathcal V}}\sum_{d\in\mathcal D}P_{j,d}(T)\,d_{[j]}(i)$ pastes the convex combination of assigned templates back onto the graph; values near the middle of the range mark vertices where several locally consistent labelings compete, and one can sample among them from $P(T)$.

## Key results

- **Lemma 1** rewrites the matrix objective as an edge-wise patch-consistency sum, so maximising $J$ is literally maximising agreement of overlapping labeled templates.
- **Proposition 1 (orientation independence).** The flow does not depend on the orientation chosen for $\mathcal G_{\mathcal V}$: reversing edges transposes $\mathcal G_{\mathcal D}$ and leaves $\mathrm{grad}\,J$ unchanged. This also holds if only the horizontal or only the vertical orientations are reversed.
- **Proposition 2 (action functional).** The solution $P(t)$ is a **critical point of the Lagrangian action**
  $$\mathcal L(P)=\tfrac12\int_{t_0}^{t_1}\Big(\|\dot P(t)\|_g^2+\sum_{i\in\mathcal V}\mathrm{var}_{P_i(t)}\big[(\mathcal A_\Omega(P)+\mathcal A^\top_\Omega(P))_i\big]\Big)\,dt,$$
  with $\|\cdot\|_g$ the Fisher-Rao product metric. The proof invokes the geometric-mechanics result of Savarino, Albers and Schnörr (*Information Geometry* 7, 2024), whose **sufficient condition is that the differential $dF$ of the affinity function be self-adjoint**; here $F(P)=\mathcal A_\Omega(P)+\mathcal A^\top_\Omega(P)$ is linear with symmetric differential, so the condition holds.
- **Experiments are qualitative and illustrative.** A synthetic "small world of binary crossing structure" dictionary shows both labeling-pattern *suppression* and *formation*, and shows that symmetry of the dictionary graph yields genuine multiplicity of locally consistent labelings, which the mean patch assignment function exposes as uncertainty. A real-data example segments anti-myosin immunostained cross-sectional skeletal muscle (from a fibre-type composition study of respiratory muscle in COVID-19 patients), using a dictionary whose adjacency structure encodes the prior that connected components of the two foreground classes must be separated by background. **No quantitative benchmark, accuracy figure or baseline comparison is reported**; integration uses a deliberately tiny geometric-Euler step ($h=0.02$) specifically to rule out discretisation error rather than to demonstrate efficiency.
- The conclusion flags future work on the design of labeled dictionaries and on **discrete symmetries, from the viewpoint of locally equivariant networks generated by geometric flows** — an explicit forward reference to [[cassel-2025-bundle-scale-spaces]].

## Relevance to this research

This is the least geometrically ambitious of the four Heidelberg papers ingested here, but it is the one that bears most directly on the vault's **Lagrangian / inertial** line rather than its gauge line.

**Action-functional characterisation of a first-order flow.** `PIFB2.tex` is careful to say that its analogy with physical action principles holds "at the level of variational stationarity (here first-order natural-gradient flow rather than the second-order Euler-Lagrange systems of classical mechanics, general relativity, and Yang-Mills theory)". Proposition 2 is exactly the missing bridge: it shows a first-order replicator/natural-gradient flow on a Fisher-Rao product manifold *is* the critical point of a genuine second-order action, with kinetic term $\|\dot P\|_g^2$ in the Fisher-Rao metric and a potential given by the fitness variance. That is directly relevant to [[Hamiltonian belief dynamics]], [[Belief inertia]] and [[Mass as Fisher information]], where a kinetic-metric postulate is currently *added* rather than derived. The **self-adjointness of $dF$** is the transferable hypothesis, and it is precisely the condition the manuscript identifies as missing for its receiver-only asymmetric update, which it records as lacking an established conservative-Hamiltonian reading. The underlying theorem is Savarino-Albers-Schnörr (2024), which should be ingested separately if this line is pursued.

**Fisher-Rao product geometry on a product of simplices** is the discrete, categorical counterpart of the owner's product-of-statistical-manifolds fibre picture. The replicator operator $R_w$ is the inverse Fisher metric in ambient coordinates — the same natural-gradient preconditioning the manuscript applies to Gaussian fibres, specialised to the simplex. The link to [[Replicator dynamics]] and to multi-population/multi-game dynamics is made explicitly by the authors and connects the assignment-flow programme to the evolutionary-game literature already in this vault.

**Where it differs, and what it does not have.** There is **no bundle, no structure group, no connection and no curvature**: the coupling $\Omega_{\mathcal D}$ is a fixed nonnegative similarity matrix, not a group-valued transport, and nothing is transported between frames. The coupling is a **bilinear affinity**, not a divergence — contrast the owner's $\beta_{ij}\mathrm{KL}(q_i\Vert\Omega_{ij}q_j)$, which is gauge-covariant precisely because it is a divergence between a section and a transported section. There is no variational free energy, no prior/belief distinction and no ELBO reading; $J$ is a consistency score, not evidence. And the convergence guarantees invoked are the assignment-flow ones (Zern-Zeilmann-Schnörr) for the *existing* framework, imported by structural analogy rather than reproved for P-AFs.

**Importable ideas.** (i) The action-functional recharacterisation and its self-adjointness hypothesis. (ii) **Uncertainty quantification from symmetry of the interaction structure** — reading multiplicity of equally-consistent configurations off the converged state — which is a cheap, principled diagnostic the owner's multi-agent implementation currently lacks. (iii) Encoding structural prior knowledge in the *adjacency structure* of the interaction graph rather than in a loss term.

## Cross-links

- Concepts: [[Assignment flow]], [[Fisher information metric]], [[Statistical manifold]], [[Natural gradient]], [[Replicator dynamics]], [[Hamiltonian belief dynamics]], [[Belief inertia]], [[Mass as Fisher information]], [[Information Geometry]], [[Harmonic map]]
- Themes: [[Information geometry and natural gradient]], [[Variational free energy and predictive coding]]
- Related sources: [[cassel-2024-sigma-flows]], [[cassel-2025-bundle-scale-spaces]], [[cassel-2025-yang-mills-data]], [[amari-2000-methods-information-geometry]], [[hofbauer-sigmund-1998-evolutionary-games-population-dynamics]], [[participatory-it-from-bit]]

## BibTeX

```bibtex
@inproceedings{gonzalezalvarado2025patch,
  author    = {Gonzalez-Alvarado, Daniel and Schlindwein, Fabio and Cassel, Jonas and Steingruber, Laura and Petra, Stefania and Schn{\"o}rr, Christoph},
  title     = {Riemannian Patch Assignment Gradient Flows},
  booktitle = {Scale Space and Variational Methods in Computer Vision (SSVM 2025)},
  series    = {Lecture Notes in Computer Science},
  volume    = {15668},
  publisher = {Springer},
  year      = {2025},
  doi       = {10.1007/978-3-031-92369-2_21},
  eprint    = {2504.13024},
  archivePrefix = {arXiv}
}
```
