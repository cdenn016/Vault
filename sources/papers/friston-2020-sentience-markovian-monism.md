---
type: paper
title: "Sentience and the Origins of Consciousness: From Cartesian Duality to Markovian Monism"
aliases: ["Friston et al. 2020 sentience markovian monism"]
authors: ["Karl J. Friston", "Wanja Wiese", "J. Allan Hobson"]
year: 2020
venue: "Entropy 22(5):516"
doi: "10.3390/e22050516"
url: "https://doi.org/10.3390/e22050516"
version: "Journal version of record as printed: Entropy 2020, 22, 516, 31 pages, doi:10.3390/e22050516 (MDPI; received 4 February 2020, accepted 16 April 2020, published 30 April 2020)."
tags: [cluster/vfe, cluster/info-geometry, cluster/participatory/philosophy-of-mind, project/multi-agent, field/neuroscience, field/philosophy, field/physics]
created: 2026-11-13
updated: 2026-11-13
---

# Sentience and the Origins of Consciousness: From Cartesian Duality to Markovian Monism

> [!info] Citation
> Karl J. Friston, Wanja Wiese, J. Allan Hobson (2020). *Sentience and the Origins of Consciousness: From Cartesian Duality to Markovian Monism*. Entropy 22(5):516. [DOI](https://doi.org/10.3390/e22050516)

[Local PDF](../pdfs/friston-2020-sentience-markovian-monism.pdf), 31 pages; retrieved November 13, 2026. Version read: Journal version of record as printed: Entropy 2020, 22, 516, 31 pages, doi:10.3390/e22050516 (MDPI; received 4 February 2020, accepted 16 April 2020, published 30 April 2020). Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read pages 1 to 25 in full (Sections 1 to 16, footnotes and figure captions) and the glossary on pages 25 to 26; the reference list (pages 26 to 31) was spot-checked to resolve references 1, 9, 25, 38, 62, 107, 118 to 123 and 138. Equations 1 to 8 and 10 to 13 are legible in the text and are reported from it. Equation 9 (the Gaussian special case) is partly garbled in the extraction and I describe it only in words. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, 004, 005, 008, 009, 010, 011, 012, 013, 014, 023, 025, 026). Confirmed against those pages: Eqs. 2, 3, 4, 5, 6, 7, 8, 10 (definitions of Gamma_alpha_alpha = k_B T mu_m and U = k_B T I approx k_B T F), 11, 12, 13. Eq. 9 verbal content (Gaussian case: Fisher metric equals precision equals curvature of free energy) confirmed on page 11; its left-hand side is printed as q(mu), apparently a typo for g(mu). Glossary entry G(alpha[tau]) >= A(alpha[tau]|pi_0) confirmed on page 26. Footnote 8 (solenoidal coupling between internal and active states ignored) confirmed on page 8. Title page metadata confirmed.

## TL;DR

The essay argues that any system with a Markov blanket at nonequilibrium steady state carries two information geometries on its internal states: an intrinsic one, given by how the probability density over internal states changes in time, and an extrinsic one, given by the Fisher metric on the beliefs about external states that internal states parameterize. It reads this dual aspect as support for a monist position, Markovian monism, whose preferred interpretation is reductive materialism with consciousness treated as a vague concept tied to temporally deep, hierarchical generative models. The mathematics is taken from Friston (2019); the paper proves nothing new.

## Problem & setting

The paper addresses Cartesian dualism and asks whether the statistical physics of self-organizing systems supplies a principled distinction between mind and matter and between merely sentient and intentional systems. Sentience is used in the thin sense of being responsive to sensory impressions, not in the sense of phenomenal consciousness. The standing assumptions are those of Friston's monograph on a particular physics: the system is a random dynamical system with Langevin dynamics, it possesses a pullback attractor and hence a nonequilibrium steady-state density, and its states admit a partition into external, sensory, active and internal states in which the blanket (sensory and active) states render internal and external states conditionally independent. The dimensionality of internal states is assumed to exceed that of blanket states so that expected internal states map one to one onto conditional densities over external states. The paper builds on Friston (2019), Parr, Da Costa and Friston (2020), information length (Kim; Crooks), and, on the philosophical side, the literature on neutral monism, dual-aspect monism, panprotopsychism, structural realism and integrated information theory.

## Method

All formal content is imported from Friston (2019) in the same notation. States follow $\dot x(\tau)=f(x,\tau)+\omega$ (Eq. 1), and at nonequilibrium steady state the expected flow is $f(x)=(Q-\Gamma)\cdot\nabla I(x)$ with surprisal $I(x)=-\ln p(x)$ (Eq. 2), $\Gamma$ the amplitude of fluctuations and $Q$ antisymmetric. With external states $\eta$, blanket $b=\{s,a\}$, autonomous states $\alpha=\{a,\mu\}$ and particular states $\pi=\{s,\alpha\}$, the autonomous flow is $f_\alpha(\pi)=(Q_{\alpha\alpha}-\Gamma_{\alpha\alpha})\nabla_\alpha I(\pi)$ (Eq. 3). Conditional independence across the blanket is used to define a variational density parameterized by the most likely internal state, $q_\mu(\eta)=p(\eta\mid b)=p(\eta\mid\pi)$ with $\mu(b)\triangleq\arg\max_\mu p(\mu\mid b)$ (Eq. 4), and the flow is rewritten as $f_\alpha(\pi)\approx(Q_{\alpha\alpha}-\Gamma_{\alpha\alpha})\nabla_\alpha F(\pi)$, where $F(\pi)=I(\pi)+D[q_\mu(\eta)\Vert p(\eta\mid\pi)]=E_q[I(\pi\mid\eta)]+D[q_\mu(\eta)\Vert p(\eta)]\ge I(\pi)$ (Eq. 5). The belief manifold carries the Fisher metric $g(\mu)=\nabla_{\mu'\mu'}D[q_{\mu'}(\eta)\Vert q_\mu(\eta)]|_{\mu'=\mu}=E_q[\nabla_\mu\ln q_\mu(\eta)\times\nabla_\mu\ln q_\mu(\eta)]$, with information length $d\ell^2=g_{ij}d\mu^id\mu^j$ (Eq. 6); this is the extrinsic geometry. The intrinsic geometry uses time as the statistical parameter of the density over internal states, $g(\tau)=\nabla_{\tau'\tau'}D[p_{\tau'}(\mu)\Vert p_\tau(\mu)]|_{\tau'=\tau}$ (Eq. 8). Assigning units through $\Gamma_{\alpha\alpha}\triangleq k_BT\cdot\mu_m$ gives a thermodynamic potential $U(\pi)\triangleq k_BT\cdot I(\pi)\approx k_BT\cdot F(\pi)$ whose gradients are forces (Eq. 10). In the path-integral formulation, a critical time $\tau$ after which information length stops growing is characterized by $D[q_\tau(\eta_\tau,\pi_\tau)\Vert p(\eta_\tau,\pi_\tau)]\approx 0$ (Eq. 11), and the action of an autonomous path is related to an expected free energy $G(\alpha[\tau])=E_{q_\tau}[I(\pi_\tau\mid\eta_\tau)]+D[q_\tau(\eta_\tau\mid\pi_\tau)\Vert p(\eta_\tau)]$, the sum of ambiguity and risk (Eq. 12).

## Key results

Nothing is proved in this paper; each formal statement is given with a pointer to pages of Friston (2019). Imported and restated: the steady-state flow decomposition (Eqs. 2 and 3, page 5); the correspondence between expected internal states and conditional densities over external states and the resulting free-energy gradient flow (Eqs. 4 and 5, pages 8 to 9), stated with an approximate equality; the Fisher metric on the belief manifold (Eq. 6, page 9); and the statement that for Gaussian beliefs the metric equals the conditional precision, which is the curvature of free energy at its minimum (Eq. 9, page 11).

The paper's own conceptual contribution is the pairing of intrinsic and extrinsic metrics on the same internal states (Eq. 8, page 11) and the claim that the two are conjugate: any movement of internal states is a movement on both manifolds, and each geometry is reducible to the other. The authors add that a dual geometry by itself confers computational properties only, and that the belief description is an as-if description (footnote 1; Section 9, page 17).

Argued informally: thermodynamic forces and free-energy gradients are the same forces in different units (Eq. 10, page 12); systems differ by the temporal depth of their generative models, measured by the critical time of Eq. 11, and deep systems appear to select actions by expected free energy (Eq. 12, pages 13 to 14); among panprotopsychism, neutral monism, dual-aspect monism and reductive materialism, the last is the most coherent reading (Sections 10 to 13, pages 17 to 21); beliefs about beliefs require hierarchical generative models and hence Markov blankets within Markov blankets (page 20); the five axioms of integrated information theory are met by Bayesian mechanics on an informal review, with the exception that blankets at one scale do not exclude blankets at other scales (Section 14, pages 21 to 22); during sleep, with blanket states sequestered, internal dynamics reduce to minimizing complexity, $F(\mu)=D[q_\mu(\eta)\Vert p(\eta)]$ (Eq. 13, page 23).

Shown by simulation: Figures 4 and 5 (pages 15 to 16) reproduce earlier simulations of handwriting and of saccadic search as illustrations of shallow and deep active inference; no new numerical results are reported.

## Limits

The authors state that the formalism does not settle the metaphysics, that competing monist readings cannot be ruled out, that the belief description is as-if unless further conditions hold, that the benefit of a calculus of beliefs is yet to be shown, and that the comparison with integrated information theory is informal. Footnote 8 notes that solenoidal coupling between internal and active states is ignored. My observations: the one-to-one map from expected internal states to posterior densities (Eq. 4) is asserted from conditional independence plus a dimension count and is the step later contested in the Markov blanket literature. The word conjugate for the two geometries is not given a mathematical definition. Footnote 3 asserts that the steady-state Fokker-Planck solution becomes the solution of a Schrodinger equation, without derivation here. The glossary lists $G\ge A$ as a bound, whereas Eq. 12 writes an approximate equality.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> Among the four papers in this set, this one bears most directly on the program's statistical fibers. The extrinsic geometry is a statistical manifold of beliefs $q_\mu(\eta)$ coordinatized by an agent's internal state and equipped with the Fisher metric, and in the Gaussian case the metric is the precision of the belief. That is the single-particle version of a Gaussian statistical fiber with Fisher metric, and the metric is defined the same way, although the paper's Gaussian statement (Eq. 9) is loose and concerns only the mean. Everything beyond one particle is absent: the paper has one blanket, one belief manifold, no second agent, no map between belief manifolds and no connection. Its closing remark that gauge theories tie into information geometry and precision is a citation of Sengupta et al. (2016), not a construction. The intrinsic geometry, an information length in time for the density over internal states, has no counterpart that I can identify in the fiber picture and is closer to thermodynamic length. The claim that beliefs about beliefs require nested blankets is relevant to hierarchical meta-agents but is asserted without proof. For the interpretation debate, the paper is useful because the lineage's own authors here commit only to an as-if reading of the belief geometry.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Markov Blanket]]; [[Fisher information metric]]; [[Statistical manifold]]; [[Expected Free Energy]]; [[Consciousness and Active Inference]]; [[Structural realism]]; [[Precision weighting]].

Related sources: [[friston-2019-particular-physics]]; [[parr-2020-markov-blankets-thermodynamics]]; [[solms-friston-2018-how-consciousness-arises]]; [[sengupta-2016-neuronal-gauge]]; [[crooks-2007-thermodynamic-length]]; [[kirchhoff-2018-markov-blankets-of-life]]; [[tononi-2016-iit]]; [[chalmers-2013-panpsychism]]; [[friston-2012-free-energy-value-attractors]]; [[friston-2021-interesting-observations-fep]].

## BibTeX

```bibtex
@article{friston2020sentience,
  author  = {Friston, Karl J. and Wiese, Wanja and Hobson, J. Allan},
  title   = {Sentience and the Origins of Consciousness: From {C}artesian Duality to {M}arkovian Monism},
  journal = {Entropy},
  volume  = {22},
  number  = {5},
  pages   = {516},
  year    = {2020},
  doi     = {10.3390/e22050516}
}
```
