---
type: concept
title: Meta-entropy
aliases:
  - Configurational meta-entropy
  - Meta-entropy of belief configurations
  - Meta-temperature
tags:
  - cluster/multi-agent
  - cluster/info-geometry
  - cluster/social-physics
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Meta-entropy

## Definition

The **(configurational) meta-entropy** is the Boltzmann-style log-count of the *belief configurations* of the gauge-theoretic [[Multi-agent variational free energy|VFE]] transformer that realise a fixed value of the belief-sector free energy. Writing a microstate as a full population configuration $\omega = \{(\boldsymbol\mu_i, \boldsymbol\Sigma_i, \boldsymbol\phi_i)\}_{i=1}^N$ of Gaussian beliefs and gauge frames, and $\mathcal{F}_{\mathrm{belief}}$ for the belief-sector restriction of the global functional, the microcanonical meta-entropy is

$$
S_{\mathrm{meta}}(\mathcal{F}_0) = \log W(\mathcal{F}_0), \qquad
W(\mathcal{F}_0) = \int_{\mathcal{D}^N} \delta\bigl(\mathcal{F}_{\mathrm{belief}}^{\mathrm{red}}(\omega) - \mathcal{F}_0\bigr)\, \mu_1^{\otimes N}(\mathrm{d}\omega),
$$

the direct analogue of Boltzmann's $S = k\log W$, with $\mu_1$ a single-agent counting measure. The point is that one value of $\mathcal{F}$ does **not** pin down the configuration: the beliefs can be distributed among the agents in many ways at fixed free-energy cost, and the logarithm of that multiplicity is the meta-entropy. Because $\mathcal{F}$ is itself already a *free energy* rather than an energy, the meta-entropy is "an entropy of a free-energy landscape" — a second-order construction with the same formal status as the quenched free energies of disordered systems.

The manuscript is careful to separate this from two other entropies it is easily conflated with (see [Details](#details)); only the meta-entropy is a property of the configuration *space* rather than of a single configuration, and only it is the new object.

## Why it matters here

In the [[Gauge-Theoretic Multi-Agent VFE Model]] a whole population of agents is assigned a *single scalar functional* $\mathcal{F}$ over their belief tuples $(\boldsymbol\mu_i, \boldsymbol\Sigma_i, \boldsymbol\phi_i)$, and inference is iterative minimisation of $\mathcal{F}$ (no learned projections). The meta-entropy is the manuscript's attempt to give this multi-agent free-energy functional a genuine **thermodynamic limit**: a statistical mechanics of belief *populations* in which the large-$N$ behaviour, fluctuations, and possible phase structure of the transformer become analytic objects rather than empirical observations.

This matters for the model in several connected ways:

- It supplies the **macrostate / microstate** vocabulary the rest of the program lacks: the value $\mathcal{F}_0$ is a macrostate; the many belief configurations consistent with it are its microstates.
- Its conjugate **meta-temperature** $T_{\mathrm{meta}}$ is given an operational reading as the noise level of stochastic [[Natural gradient|natural-gradient]] belief updating — i.e. a concrete knob on the inference dynamics, not a metaphor.
- It identifies the **gauge sector** (the per-agent frames $\boldsymbol\phi_i$) as the structure that distinguishes this thermodynamics from ordinary statistical mechanics, connecting meta-entropy to [[Holonomy]] and to the [[Renormalization-group flow of beliefs]] / [[Meta-agents and hierarchical emergence]] themes of the wider program.
- It connects the transformer to classical [[degroot-1974-consensus|consensus]] / [[friedkin-johnsen-1990|opinion-dynamics]] models through the solvable Gaussian case, where a "consensus transition" becomes a question about susceptibility and symmetry breaking.

## Details

**Three entropies at three levels.** The manuscript insists on separating: (1) the *intra-belief* Gaussian entropy $\mathcal{S}[q_i] = \tfrac12\log\det(2\pi e\,\boldsymbol\Sigma_i)$, which is what makes each agent's term a free energy; (2) the *attention-distribution* entropy, the terms $\tau\,\beta_{ij}\log(\beta_{ij}/\pi_{ij})$ whose minimisation over $\beta_{ij}$ returns softmax attention $\beta_{ij}=\operatorname{softmax}_j(\log\pi_{ij}-D_{\mathrm{KL}}(q_i\,\|\,\Omega_{ij}q_j)/\tau)$; and (3) the **meta-entropy** proper. The first two are within-configuration quantities already present in $\mathcal{F}$; only the third is the new $S=k\log W$ object.

**The counting measure (Fisher–Rao / Chentsov).** A microstate lives in $\mathcal{M}_1 = \mathbb{R}^K \times \mathrm{SPD}(K) \times \mathcal{G}$ with ambient gauge group $\mathcal{G}=\mathrm{GL}^+(K)$. Where Hamiltonian mechanics gets its canonical measure from Liouville's theorem, the VFE dynamics is gradient descent, so a different principle must fix the measure. The manuscript takes the single-agent reference to be the product of the **Fisher–Rao Riemannian volume** on the statistical factor and a group (Haar) measure on the gauge factor,

$$
\mathrm{d}\mu_1 = \mathrm{d}\mathrm{Vol}_{\mathrm{FR}}(\boldsymbol\mu,\boldsymbol\Sigma) \times \mathrm{d}\mu_{\mathrm{Haar}}^{\mathcal{G}}(U).
$$

By Chentsov's theorem the [[Fisher information metric|Fisher–Rao]] metric is, up to a positive scalar, the unique metric invariant under Markov morphisms; so "Chentsov's theorem is to the belief part of the meta-entropy what Liouville's theorem is to thermodynamic entropy." On the Gaussian sector the volume element is $\sqrt{\det g_{\mathrm{FR}}} = c_K (\det\boldsymbol\Sigma)^{-(K+2)/2}$. Two cautions are carried throughout: Chentsov fixes only the *statistical* metric (the group measure must be specified separately, and $\mathrm{GL}^+(K)$'s exponential map is not a global diffeomorphism), and $\mathrm{GL}^+(K)$ is noncompact so $W(\mathcal{F}_0)$ is finite only after a gauge quotient or a **container** regulator (the two-sided set $\mathcal{D}$ bounding $\boldsymbol\Sigma^{-1}$, $\|\boldsymbol\mu\|$, and $\|\boldsymbol\phi\|_2 \le \pi-\eta$).

**Extensivity via Kac normalisation.** For $S_{\mathrm{meta}}$ to scale with $N$, $\mathcal{F}_{\mathrm{belief}}$ must be extensive. The naive attention-entropy total is $O(N\log N)$ and configuration-dependent. The fix is the **row-reduced** free energy obtained by inserting the softmax stationary point back, which collapses each row's energy-plus-entropy into a log-partition $-\tau\log Z_i$ with $Z_i = \tfrac1N\sum_j e^{-D_{\mathrm{KL}}(q_i\|\Omega_{ij}q_j)/\tau}$. Keeping the $1/N$ *inside* the logarithm is exactly the **Kac normalisation** that renders long-range (all-to-all) coupling extensive — softmax attention is thereby "a Kac-normalised all-to-all coupling," and the reduced functional is $O(N)$.

**Large-deviation (Sanov) form.** With the empirical belief law $\rho_N = \tfrac1N\sum_i \delta_{(\boldsymbol\mu_i,\boldsymbol\Sigma_i,U_i)}$, Sanov's theorem gives $\Pr(\rho_N\approx\rho)\asymp e^{-N\,D_{\mathrm{KL}}(\rho\|\mu_1)}$, and the contraction principle yields the meta-entropy density

$$
s(f) = \lim_{N\to\infty}\tfrac1N\log W(Nf) = -\inf\bigl\{ D_{\mathrm{KL}}(\rho\,\|\,\mu_1) : \mathcal{F}[\rho]=f \bigr\} + \text{const},
$$

"minus the cheapest relative-entropy cost ... of any population belief-distribution consistent with $f$." On the Gaussian sector the rate reduces to a negative Fisher–Rao differential entropy. The constrained minimiser $\rho^\star$ has **McKean–Vlasov** self-consistency form, with the directed (row) structure of attention kept rather than symmetrised — so no factor-of-$1/2$ symmetric pair potential appears; the covariance-active minimiser is recorded as an open problem.

**Meta-temperature as natural-gradient noise.** The Legendre conjugate $\beta_{\mathrm{meta}} = \partial S_{\mathrm{meta}}/\partial\mathcal{F}_0$ defines a canonical meta-ensemble $P[\omega]\propto e^{-\beta_{\mathrm{meta}}\mathcal{F}_{\mathrm{belief}}^{\mathrm{red}}}\mu_1^{\otimes N}$. Rather than posit it, the manuscript identifies it as the stationary law of a **Riemannian Langevin** dynamics whose drift is the natural gradient $g^{ij}\partial_j\mathcal{F}_{\mathrm{belief}}$ plus a metric-divergence term and whose diffusion covariance is $2T_{\mathrm{meta}}\,g^{-1}$. So $T_{\mathrm{meta}} = 1/\beta_{\mathrm{meta}}$ is "the noise level injected into stochastic natural-gradient belief updating, an operational quantity rather than an analogy": $T_{\mathrm{meta}}\to0$ concentrates on minimisers, finite $T_{\mathrm{meta}}$ populates the meta-entropy. The inverse meta-temperature is the configuration-level counterpart of the precision that weights free energy in [[friston-2017-active-inference-process|active-inference policy selection]], lifted from policies to whole belief configurations. This places three scales in the theory: the attention temperature $\tau = \kappa\sqrt{K}$ (fast E-step), the M-step learning rate (slow relaxation), and $T_{\mathrm{meta}}$ (the genuine Gibbs weight over configurations).

**Solvable Gaussian instance.** A means-only, trivial-gauge model with quadratic prior strength $\alpha$ and all-to-all coupling $J$ is solvable in closed form. Its zero-field magnetisation is $m^\star = 0$ and its susceptibility is

$$
\chi = \frac{\partial m}{\partial b} = \frac{1}{\alpha},
$$

independent of $J$ and of $\beta_{\mathrm{meta}}$. This is a **linear-response** signature, not a delivered phase transition: there is no spontaneous consensus at any finite $\alpha$. The prior strength $\alpha$ is the explicit field that breaks an otherwise exact local $\mathrm{GL}^+(K)$ covariance of the interaction; $\chi=1/\alpha$ diverges only in the decoupling limit $\alpha\to0$. A genuine consensus transition is conjectured to require a regulated/spherical constraint or the anharmonicity of an active covariance sector.

**Gauge sector and holonomy frustration.** The affine invariance of the Gaussian divergence makes each coupling summand $D_{\mathrm{KL}}(q_i\|\Omega_{ij}q_j)$ invariant under the joint local action $q_i\mapsto(G_i)_\# q_i$, $\Omega_{ij}\mapsto G_i\Omega_{ij}G_j^{-1}$; the prior anchoring and the observation likelihood are the explicit symmetry-breaking terms. Whether these local frame moves are gauge *redundancies* (to be Faddeev–Popov quotiented, with soft directions reading as pseudo-Goldstone modes) or *active* changes of epistemic configuration is left as a declared structural choice, deferred to the participatory companion manuscript ([[participatory-it-from-bit]]). Crucially, the transport actually used in $\mathcal{F}$ is **vertex-frame**, $\Omega_{ij}=g_i g_j^{-1}$, whose loop product telescopes to the identity — [[Holonomy|holonomy]] is identically trivial, so no residual holonomy entropy arises in the operative regime. A residual meta-entropy at $T_{\mathrm{meta}}\to0$ is *conjectured* only for a distinct **edge-local** connection with nontrivial loop curvature and extensive ground-state degeneracy — the analogue of the residual entropy of ice and of spin-glass ground states — and is recorded as falsifiable by simulation, not as a result.

> [!note] Editorial: All quantities above are drawn directly from `meta_entropy.tex`. The manuscript repeatedly flags its own confidence levels; the consensus phase transition and the holonomy-frustration residual entropy are explicitly **conjectural**, the Gaussian susceptibility and the holonomy telescoping are **exact**, and the Kac/Chentsov/Sanov/Langevin apparatus is **imported** standard machinery. This page preserves those distinctions.

## In this work

Meta-entropy is the subject of its own dedicated manuscript, [[meta-entropy-manuscript]] ("Configurational Meta-Entropy of a Population of Variational Beliefs: Toward a Thermodynamic Limit for the Gauge-Theoretic Free Energy Transformer"), which develops the construction end to end: the three-entropy separation, the Fisher–Rao/Chentsov counting measure, Kac-normalised extensivity, the Sanov large-deviation form with its McKean–Vlasov minimiser, the meta-temperature as Riemannian-Langevin noise, the solvable Gaussian susceptibility $\chi=1/\alpha$, and the edge-local holonomy-frustration conjecture.

It sits atop the same belief-sector functional that the companion manuscripts build: the softmax-from-gauge-transported-KL attention of [[gl-k-attention]], and the per-agent frame action treated as active epistemic configuration in [[participatory-it-from-bit]].

> [!note] Editorial: Independent verification and incorporation (2026-06-19). A multi-agent peer review independently reproduced every claimed-exact result of [[meta-entropy-manuscript]] (Gaussian-KL affine invariance, the gauge-composition identity, prior symmetry-breaking, vertex-frame holonomy telescoping, $\exp$ non-surjectivity on $\mathrm{GL}^+(K)$, the Fisher–Rao volume exponent $-(K+2)/2$, the McKean–Vlasov first variation with no symmetric $1/2$ factor, and the susceptibility $\chi=1/\alpha$) in sympy/numpy, and confirmed the imported machinery (Kac extensivity, Sanov + contraction with the infimum-form Legendre–Fenchel direction, Chentsov, the Riemannian-Langevin metric-divergence drift) is correctly applied; the conjectures (consensus transition; edge-local holonomy-frustration residual entropy) are honestly labelled and falsifiable. A first-pass flag reading $\chi=1/\alpha$ as a fluctuation-dissipation defect was **overturned** by an independent Kubo computation ($\beta_{\mathrm{meta}}\,\mathrm{Var}(M)/N = 1/\alpha$ exactly, so the energy-scale $\chi$ *is* the fluctuation response). Verdict: **verifiably correct.** Following that verdict the companion [[participatory-it-from-bit]] now references this note in three places — the $\chi=1/\alpha$ result answering its open "phase transitions?" question (PIFB §Scaling and Phase Transitions), the RG section's thermodynamic-limit complement, and the Regime-II holonomy-frustration falsifier — under a reference-and-summarize (companion-paper) relationship rather than a merge. It is conceptually adjacent to — but distinct from — the dynamical constructions of [[belief-inertia]] (where the Fisher precision tensor plays the role of inertial [[Mass as Fisher information|mass]] in [[Hamiltonian belief dynamics]]); meta-entropy instead asks a statistical-mechanical, configuration-counting question about the *population* rather than the trajectory of single beliefs. Within the registry it is the [[Gauge-Theoretic Multi-Agent VFE Model]] concept that supplies the program's thermodynamic limit, feeding the [[Renormalization-group flow of beliefs]], [[Meta-agents and hierarchical emergence]], and [[Ouroboros multi-scale dynamics]] themes.

## Sources

- [[meta-entropy-manuscript]] — the manuscript that defines and develops the configurational meta-entropy in full (every equation on this page is grounded here).
- [[gl-k-attention]] — derives softmax attention as gauge-transported KL divergence; supplies the row functional whose stationary point gives the $-\tau\log Z_i$ used for Kac extensivity.
- [[participatory-it-from-bit]] — treats the per-agent frame action $\Omega_{ij}\mapsto G_i\Omega_{ij}G_j^{-1}$ as active epistemic change, the reading that licenses counting the frame directions in $S_{\mathrm{meta}}$.
- [[belief-inertia]] — companion dynamical construction (Fisher-as-mass, Hamiltonian belief dynamics); adjacent but distinct from the configuration-counting meta-entropy.
- [[cencov-1982-statistical-decision-rules]] — Chentsov uniqueness of the Fisher–Rao metric, the theorem fixing the belief-sector counting measure.
- [[amari-2016-information-geometry-applications]], [[ay-2017-information-geometry]] — information-geometric foundations for the Fisher–Rao volume and natural gradient.
- [[friston-2017-active-inference-process]], [[parr-2022-active-inference]] — active-inference reading of inverse temperature / precision, lifted here from policies to belief configurations.
- [[caticha-2019-entropic-dynamics]] — physics precedent for belief dynamics as entropic/maximum-entropy inference on a Fisher-metric configuration space.
- [[wilson-1975-renormalization-group]] — coarse-graining / thermodynamic-limit precedent for the multi-agent scaling story.
- [[hall-2015-lie-groups]] — $\mathrm{GL}^+(K)$ as the identity component and the exponential-map subtleties underlying the gauge counting chart.
- [[degroot-1974-consensus]], [[friedkin-johnsen-1990]] — classical consensus/opinion-dynamics models that the Gaussian consensus-transition question generalises.

## See also

- [[Multi-agent variational free energy]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
- [[Belief inertia]]
- [[Mass as Fisher information]]
- [[Hamiltonian belief dynamics]]
- [[Meta-agents and hierarchical emergence]]
- [[Renormalization-group flow of beliefs]]
- [[Ouroboros multi-scale dynamics]]
- [[Participatory realism (it from bit)]]
- [[Fisher information metric]]
- [[Natural gradient]]
- [[Holonomy]]
- [[Gauge transformation]]
- [[Variational free energy]]
- [[Agents as fibre-bundle sections]]
- [[Information geometry and natural gradient]]
