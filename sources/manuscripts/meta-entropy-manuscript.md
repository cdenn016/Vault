---
type: manuscript
title: "Configurational Meta-Entropy of a Population of Variational Beliefs: Toward a Thermodynamic Limit for the Gauge-Theoretic Free Energy Transformer"
aliases:
  - "Meta-Entropy of Variational Beliefs"
  - "Thermodynamic Limit of the Gauge-Theoretic VFE Transformer"
authors:
  - Robert C. Dennis
year: 2026
status: in preparation
tags:
  - cluster/multi-agent
  - project/multi-agent
created: 2026-06-18
updated: 2026-06-18
---

# Configurational Meta-Entropy of a Population of Variational Beliefs: Toward a Thermodynamic Limit for the Gauge-Theoretic Free Energy Transformer

> [!info] Manuscript
> File: `meta_entropy.tex` (Manuscripts-Theory)
> Status: in preparation. The `\author` field is empty in the source; authorship recorded as Robert C. Dennis (the program's other manuscripts — belief_inertia, participatory_it_from_bit — are single-authored by Robert C. Dennis).
> This is the author's own novel theoretical work; all claims below are grounded in the manuscript file.

## Abstract

The gauge-theoretic variational free energy (VFE) transformer assigns to a population of agents a single scalar functional $\mathcal{F}$ over their Gaussian belief tuples $(\boldsymbol{\mu}_i, \boldsymbol{\Sigma}_i, \boldsymbol{\phi}_i)$. Because a given value of $\mathcal{F}$ is realised by many distinct belief configurations, the manuscript proposes a statistical-mechanical reading: in the large-population limit the log-count of belief configurations at fixed belief-sector free energy is a candidate **configurational meta-entropy** $S_{\mathrm{meta}}(\mathcal{F}_0) = \log W(\mathcal{F}_0)$, an analogue of Boltzmann's $S = k\log W$.

The note develops this construction and carefully delimits what can and cannot yet be claimed. It first separates three easily-conflated entropies (intra-belief Gaussian entropy, attention-distribution entropy, and the configurational meta-entropy). It takes the counting measure on the belief sector to be the Riemannian volume form of the Fisher–Rao metric — fixed up to a positive scalar by Chentsov's theorem, the information-geometric counterpart of the Liouville measure — while noting that the gauge sector requires a separately specified group measure plus a quotient or regulator. The coupling energy is shown to be rendered extensive by the Kac normalization implicit in row-stochastic softmax attention, provided the attention-entropy contribution is absorbed into the row log-partition $-\tau\log Z_i$. The meta-entropy is given a large-deviation form via a single declared reference measure, and the McKean–Vlasov stationary form of its constrained minimizer is identified, retaining the directed row structure of attention. The conjugate **meta-temperature** is given an operational reading as the noise level of stochastic natural-gradient belief updating through the Riemannian Langevin equation. A solvable Gaussian instance is a linear-response calculation (susceptibility $\chi = 1/\alpha$ diverging as $\alpha\to0$) rather than a delivered phase transition. The note closes with a conjecture — conditional on an edge-local connection with nontrivial holonomy and extensive ground-state degeneracy — that geometric frustration leaves a residual meta-entropy; in the vertex-frame transport actually used in $\mathcal{F}$ the loop holonomy is identically trivial, so the conjecture concerns a distinct, edge-relaxed regime.

## Core contributions

- **Definition of a configurational meta-entropy.** $S_{\mathrm{meta}}(\mathcal{F}_0) = \log W(\mathcal{F}_0)$, with $W$ the count of belief configurations realising a fixed value of the belief-sector free energy $\mathcal{F}_{\mathrm{belief}}$ — an entropy of a *free-energy landscape*, a second-order construction with the formal status of the quenched free energies of disordered systems.
- **Disambiguation of three entropies at three levels.** The intra-belief Gaussian entropy $\mathcal{S}[q_i] = \tfrac12\log\det(2\pi e\boldsymbol{\Sigma}_i)$; the attention-distribution entropy $\tau\beta_{ij}\log(\beta_{ij}/\pi_{ij})$ (a within-configuration quantity already inside $\mathcal{F}$); and the new configurational meta-entropy (a property of configuration space). Only the third is the analogue of $S = k\log W$.
- **A principled counting measure.** The single-agent reference $\mathrm{d}\mu_1 = \mathrm{d}\mathrm{Vol}_{\mathrm{FR}}(\boldsymbol{\mu},\boldsymbol{\Sigma}) \times \mathrm{d}\mu_{\mathrm{Haar}}^{\mathcal{G}}(U)$ combines the Fisher–Rao Riemannian volume (uniqueness from Chentsov's theorem) with a Haar group measure on the gauge factor; the role-analogy "Chentsov : meta-entropy :: Liouville : thermodynamic entropy" is made explicit, the present measure curved rather than flat.
- **Extensivity via Kac normalisation.** Inserting the softmax stationary point yields the row-reduced free energy $-\tau\log Z_i$ with $Z_i = \tfrac1N\sum_j e^{-D_{\mathrm{KL}}(q_i\|\Omega_{ij}q_j)/\tau}$; keeping the $1/N$ inside the logarithm is exactly the Kac prescription that renders all-to-all coupling extensive ($O(N)$ rather than $O(N\log N)$).
- **Large-deviation / mean-field formulation.** Via Sanov's theorem and the contraction principle, the meta-entropy density $s(f) = -\inf\{D_{\mathrm{KL}}(\rho\|\mu_1) : \mathcal{F}[\rho] = f\} + \text{const}$, with constrained minimiser of McKean–Vlasov self-consistent form (directed row structure retained, no symmetric $1/2$ factor).
- **Operational meta-temperature.** $T_{\mathrm{meta}} = 1/\beta_{\mathrm{meta}}$ is identified as the noise level of the Riemannian Langevin dynamics whose stationary law is the metric-weighted canonical ensemble — an operational quantity, not an analogy, and the configuration-level counterpart of active-inference precision.
- **Gauge-sector analysis.** Separation of common-pushforward invariance, active local covariance, and true gauge redundancy; identification of the prior (and observation channel) as the explicit symmetry-breaking field.
- **Holonomy / frustration conjecture.** A falsifiable conjecture for an edge-local connection regime, distinct from the trivial-holonomy vertex-frame regime of $\mathcal{F}$.

## Key results / theorems

- **Lemma 1 (Affine invariance of the Gaussian divergence).** For invertible $G\in\mathrm{GL}(K)$ and $T(x) = Gx + c$, $D_{\mathrm{KL}}(T_\# q_1 \| T_\# q_2) = D_{\mathrm{KL}}(q_1 \| q_2)$ — exact and verified.
- **Proposition (Local covariance of the belief coupling).** Under $q_i \mapsto (G_i)_\# q_i$, $e^{\boldsymbol{\phi}_i} \mapsto G_i e^{\boldsymbol{\phi}_i}$, the transport maps as $\Omega_{ij}\mapsto G_i\Omega_{ij}G_j^{-1}$ and each summand $D_{\mathrm{KL}}(q_i\|\Omega_{ij}q_j)$ is invariant; the belief-coupling functional is therefore locally $\mathrm{GL}^+(K)$-covariant (a pre-regulator algebraic identity on the ambient group).
- **Proposition (The prior is the symmetry-breaking field).** With fixed M-step priors $p_i$, the local covariance of $\mathcal{F}_{\mathrm{belief}}$ is explicitly broken by the prior-anchoring term $\alpha\sum_i D_{\mathrm{KL}}(q_i\|p_i)$ (strength $\alpha$) and by the observation term $-\mathbb{E}_q[\log p(o\mid x)]$.
- **Proposition (Gaussian meta-ensemble susceptibility).** For isotropic means-only beliefs with trivial gauge and all-to-all coupling, mean-field self-consistency gives $m\alpha = b$, zero-field magnetisation $m^\star = 0$, and susceptibility $\chi = \partial m/\partial b = 1/\alpha$, independent of coupling $J$ and of $\beta_{\mathrm{meta}}$. This is a *linear-response* signature (diverging as $\alpha\to0$), explicitly **not** an order–disorder phase transition.
- **Trivial vertex-frame holonomy.** With $\Omega_{ij} = g_i g_j^{-1}$, $g_i = e^{\boldsymbol{\phi}_i}$, the loop product telescopes to $\mathbf{I}$, so holonomy is identically trivial in the regime $\mathcal{F}$ defines; no residual holonomy entropy can arise there.
- **Conjecture (Holonomy-induced residual meta-entropy, edge-local regime).** For an edge-local connection with nontrivial holonomy on extensively many independent loops and a compact/regulated sector, if the near-ground set is an extensive flat (or discretely resolved) manifold with log-volume linear in $N$, then $\lim_{T_{\mathrm{meta}}\to0}\lim_{N\to\infty} N^{-1}S_{\mathrm{meta}} > 0$ — analogous to the residual entropy of ice and spin-glass ground-state degeneracy. Falsifiable by simulation via thermodynamic integration of $\langle\mathcal{F}_{\mathrm{belief}}\rangle$ over $\beta_{\mathrm{meta}}$ on a frustrated lattice.

> [!note] Editorial: The manuscript is scrupulous about confidence levels. Exact/verified: Lemma 1, the covariance and breaking propositions, $\chi=1/\alpha$, and trivial vertex-frame holonomy. Imported standard results: the Kac extensivity criterion, Chentsov uniqueness, Sanov/contraction apparatus, the Riemannian-Langevin stationary law, and the active-inference reading of $\beta_{\mathrm{meta}}$. Conjectural: the holonomy-frustration mechanism and a genuine consensus phase transition (not delivered by the Gaussian model).

## Relevance to the program

This note is the statistical-mechanical / thermodynamic-limit layer of the [[Gauge-Theoretic Multi-Agent VFE Model]] and sits within the [[VFE Transformer Program]]. It counts configurations of the [[Multi-agent variational free energy]] functional and so directly elaborates [[Meta-entropy]] as a program concept.

Connections drawn in the file:

- The counted functional is the belief-sector restriction of the [[Multi-agent variational free energy]]; the per-agent term makes each contribution a [[Variational free energy]] rather than a bare energy.
- The counting measure is the [[Fisher information metric]] (Fisher–Rao) Riemannian volume; the meta-temperature is the noise of stochastic [[Natural gradient]] updating (Riemannian Langevin), linking to [[Information geometry and natural gradient]].
- The transport $\Omega_{ij} = e^{\boldsymbol{\phi}_i}e^{-\boldsymbol{\phi}_j}$ and congruence action are [[Gauge transformation]]s realised through [[Parallel transport]]; the loop result is the trivial [[Holonomy]] of the vertex-frame regime, with [[Agents as fibre-bundle sections]] as the underlying picture, situating the work in [[Gauge equivariance and geometric deep learning]].
- The susceptibility analysis identifies the prior as the explicit breaker of an otherwise exact local $\mathrm{GL}^+(K)$ covariance, connecting to [[Mass as Fisher information]] and the role of [[Precision weighting]] / [[Prediction error]] in the underlying functional.
- The covariance sector lives on the SPD manifold with the affine-invariant geodesic, i.e. [[SPD-manifold geometry and Riemannian optimization]].
- Row-stochastic softmax attention as a Kac-normalised all-to-all coupling ties the construction to [[Attention mechanisms — theory and positional structure]].
- The meta-temperature's reading as configuration-level precision draws on [[Free-energy principle active inference]].
- The work connects to companion manuscripts in the program: the participatory / active-frame interpretation of the gauge sector ([[participatory-it-from-bit]], i.e. [[Participatory realism (it from bit)]]) and the vanishing-holonomy result for vertex-frame transport in the attention manuscript ([[gl-k-attention]]); the meta-entropy program also relates to [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]], and [[Renormalization-group flow of beliefs]], with [[belief-inertia]] / [[Belief inertia]] and [[Hamiltonian belief dynamics]] as adjacent dynamical pieces.

## References cited

Unique citation keys resolved against the manuscript's embedded bibliography. None of the keys in this file match the program BIBMAP exactly (the file uses lowercase author-year keys), so all entries are rendered as plain text.

- Amari & Nagaoka (2000), *Methods of Information Geometry*
- Berlin & Kac (1952), The spherical model of a ferromagnet
- Chentsov (1982), *Statistical Decision Rules and Optimal Inference*
- Cover & Thomas (2006), *Elements of Information Theory* (2nd ed.)
- Csiszár (1975), $I$-divergence geometry of probability distributions and minimization problems
- Kardar (2007), *Statistical Physics of Fields*
- Comets (1989), Large deviation estimates for a conditional probability distribution; applications to random interaction Gibbs measures
- Culver (1966), On the existence and uniqueness of the real logarithm of a matrix
- Dawson & Gärtner (1987), Large deviations from the McKean–Vlasov limit for weakly interacting diffusions
- Dembo & Zeitouni (1998), *Large Deviations Techniques and Applications* (2nd ed.)
- Ellis (1985), *Entropy, Large Deviations, and Statistical Mechanics*
- Faddeev & Popov (1967), Feynman diagrams for the Yang–Mills field
- Friston (2010), The free-energy principle: a unified brain theory?
- Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo (2017), Active inference: a process theory
- Girolami & Calderhead (2011), Riemann manifold Langevin and Hamiltonian Monte Carlo methods
- Xifara, Sherlock, Livingstone, Byrne & Girolami (2014), Langevin diffusions and the Metropolis-adjusted Langevin algorithm
- Goldstein (1980), *Classical Mechanics* (2nd ed.)
- Hall (2015), *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (2nd ed.)
- Higham (2008), *Functions of Matrices: Theory and Computation*
- Kac, Uhlenbeck & Hemmer (1963), On the van der Waals theory of the vapor–liquid equilibrium. I
- Mandt, Hoffman & Blei (2017), Stochastic gradient descent as approximate Bayesian inference
- Mézard, Parisi & Virasoro (1987), *Spin Glass Theory and Beyond*
- Nielsen (2020), An elementary introduction to information geometry
- Pennec, Fillard & Ayache (2006), A Riemannian framework for tensor computing
- Pinele, Strapasson & Costa (2020), The Fisher–Rao distance between multivariate normal distributions: special cases, bounds and applications
- Skovgaard (1984), A Riemannian geometry of the multivariate normal model
- Pauling (1935), The structure and entropy of ice and of other crystals with some randomness of atomic arrangement
- Sznitman (1991), Topics in propagation of chaos
- Touchette (2009), The large deviation approach to statistical mechanics
- Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser & Polosukhin (2017), Attention is all you need
- Welling & Teh (2011), Bayesian learning via stochastic gradient Langevin dynamics
