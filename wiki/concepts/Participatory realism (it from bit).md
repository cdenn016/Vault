---
type: concept
title: "Participatory realism (it from bit)"
aliases:
  - "It from bit"
  - "Participatory universe"
  - "Pullback it-from-bit"
  - "PIFB.tex"
  - "PIFB"
tags:
  - cluster/multi-agent
  - cluster/participatory
  - cluster/info-geometry
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-07-02
---

# Participatory realism (it from bit)

## Definition

**Participatory realism** is the interpretive program of the [[Gauge-Theoretic Multi-Agent VFE Model]] in which geometric, "physics-like" structure is not presupposed but *induced* from the informational dynamics of interacting epistemic agents. The name borrows Wheeler's slogan **"it from bit"** — that physical reality ("it") derives its existence from registered information ("bit") — and gives it a precise mathematical realisation: a metric on a noumenal base manifold $\mathcal{C}$ is constructed as the **pullback** of a fibre-respecting metric on an information-bearing bundle along an agent's belief/model section.

The manuscript [[participatory-it-from-bit]] is explicit that this is a *structural correspondence, not a derivation*. The framework "does not derive" Wheeler's or Kant's claims; it "exhibits information-geometric analogues of physics-like structures within an interacting-agent formalism." Three epistemic tiers are declared up front: Level 1 (implemented and empirically probed — attention recovery and the WikiText-103 scaling sweep), Level 2 (mathematical implementation — the Ouroboros participatory loop in working code), and Level 3 (speculative physical interpretation — the pullback metric and signature program).

> [!note] Editorial: The page maps Wheeler's *"it from bit"* specifically to the **pullback metric**, not to attention. The author's own Table (Wheeler 1990 vs. this framework) reads: "It from bit" $\to$ structural pullback metric; "Participatory universe" $\to$ cross-scale meta-agent feedback loops; "Observer-dependent reality" $\to$ gauge-frame-dependent pullback metrics; "Self-excited circuit" $\to$ sustained non-equilibrium under threshold detection.

## Why it matters here

Participatory realism is the philosophical and ontological spine that ties the otherwise separate machinery of the multi-agent model together. Three of the model's distinctive constructions are read as its components:

- **It from bit** $\Leftrightarrow$ the pullback of the [[Fisher information metric]] from the statistical fibre to the base, giving an *emergent* geometry from belief fields.
- **Participatory universe** $\Leftrightarrow$ the cross-scale loop in which agent clusters form [[Meta-agents and hierarchical emergence|meta-agents]] whose statistics propagate back as priors to constituents — the [[Ouroboros multi-scale dynamics]] tower.
- **Observer-dependent reality** $\Leftrightarrow$ the [[Gauge transformation|gauge]]-frame dependence of the induced metric: different agents pull back different geometries from the *same* noumenal substrate, and there is no agent-independent "correct" geometry.

The framework adopts a **pan-agentic, panprotopsychist** ontology: every system at every scale carries gauge-frame structure plus participation in variational dynamics on a statistical manifold appropriate to its scale ($\mathrm{GL}(K,\mathbb{R})$ on a real Gaussian fibre classically; $U(\mathcal{H})$ at the open scale-0 quantum level). An electron is a scale-0 agent, a molecule a higher-scale meta-agent, a brain higher still. This is the move that lets the single-agent [[parr-2022-active-inference|active-inference]] / [[friston-2017-active-inference-process-theory|free-energy]] substrate be generalised into a *multi-agent, gauge-theoretic* theory of co-constituted physical and cognitive structure.

A functioning participatory system must *not* collapse into global consensus: complete agreement across all agents is the "heat death" of the informational universe — a static, non-participatory state with no information gradients to drive dynamics and no perspective diversity to generate new structure.

## Details

### The pullback construction

Agent $i$ carries smooth sections over the base $\mathcal{C}$ (the noumenal domain): a belief section $\sigma_i^{(q)}$ giving $q_i(c)$, a prior $p_i(c)$, a generative-model section $s_i(c)$ and a hyper-prior $r_i(c)$, all relative to agent $i$'s gauge frame $\phi_i(c)$. The statistical fibre $\mathcal{B}$ carries the Fisher–Rao metric, which for Gaussians is

$$
g_{\mathcal{B}}(\delta q,\delta q) = \delta\mu^\top \Sigma^{-1}\delta\mu + \tfrac{1}{2}\,\mathrm{tr}\!\big(\Sigma^{-1}\delta\Sigma\,\Sigma^{-1}\delta\Sigma\big).
$$

Equipping the associated bundle $\mathcal{E} = P\times_G \mathcal{B}$ with a fibre-respecting bundle metric (vertical block = Fisher–Rao, horizontal block = a frame-twist quadratic form built from the connection itself) and pulling back along $\sigma_i^{(q)}$ gives the **induced metric** on $\mathcal{C}$:

$$
\boxed{\,G^{(q)}_{i,\mu\nu}(c) = \mathcal{K}\big(A^{(i)}_\mu, A^{(i)}_\nu\big) + \mathbb{E}_{q_i(c)}\big[(\nabla^{(i)}_\mu \log q_i)(\nabla^{(i)}_\nu \log q_i)\big]\,}
$$

The first term is the **horizontal frame-twist block**: $\mathcal{K}(\cdot,\cdot)$ is the [[Killing form|bilinear (Killing) form]] on the gauge Lie algebra evaluated on the connection one-form $A^{(i)}_\mu = U_i^{-1}\partial_\mu U_i$. The second is the **vertical Fisher block**: the [[Fisher information metric]] sampled along the section. Physical distance under this geometry is thus a sum of *frame-twist length* (how fast the agent's representational basis rotates between two base points) and *information distance* (how fast the statistical field distinguishes them).

The same construction applied to $p_i, s_i, r_i$ yields four coexistent tensors $G^{(q)}_i, G^{(p)}_i, G^{(s)}_i, G^{(r)}_i$, organised by timescale into **three tiers**: the belief tier $G^{(q)}_i$ is *epistemic* geometry (an instantaneous attention-and-uncertainty map); $G^{(p)}_i$ is *expectational* geometry; and the slow-channel $G^{(s)}_i, G^{(r)}_i$ are *structural* geometry. The author proposes that what an agent phenomenally experiences as "ambient space" is identified with the **structural tier $G^{(s)}_i$**, the slow generative-model pullback — mapping onto Kant's "form of intuition" rather than an instantaneous prior.

### Gauge-frame dependence

The frame-twist block is *not* gauge-invariant: under $U_i \to U_i\,g(c)$ the connection picks up a Maurer–Cartan piece, so $\mathcal{K}(A_\mu,A_\nu)$ transforms with cross terms. This is a feature, not a bug — it is exactly the mechanism by which "different gauge fixings of the same agent yield different horizontal contributions," giving the *observer-dependent reality* reading. Genuinely agent-independent geometry, if it exists, must be recovered through a regulated **consensus / Haar-averaged metric** restricted to the gauge frames realised within a cognitive species; as constructed that average over a non-compact subgroup of $\mathrm{GL}(K)$ is *regulator-dependent*, so the consensus metric is a heuristic target rather than a finite gauge-invariant observable.

### Observable sectors and signature

The symmetric tensor $G_i(c)$ admits a spectral decomposition $G_i(c)=\sum_a \lambda_a\,(e_a\otimes e_a)$, with each $\lambda_a$ a squared information rate. These split into an **observable** sector ($\lambda_a > \Lambda_{\text{obs}}$, the "perceived spacetime", conjectured $\approx 4$ base dimensions for humans), a **subthreshold informational** sector, and an **internal** sector ($\lambda_a$ negligible). The Gaussian fibre dimension itself is $\dim(\mathcal{B}) = K(K+3)/2$ (e.g. $\approx 2.96\times 10^5$ at $K=768$), of which only $\dim(\mathcal{C})$ directions are sampled by the section.

A central problem is signature: the vertical Fisher block is positive **semi-definite**, and the fibre congruence $\Sigma \mapsto \Omega\Sigma\Omega^\top$ stays positive-definite for real $\Omega$ (Sylvester's law of inertia), yet observed spacetime is Lorentzian $(-,+,+,+)$. The indefinite signature must therefore live in the *horizontal frame-twist block* $\mathrm{tr}(A_\mu A_\nu)$, which is already indefinite on $\mathfrak{gl}(K_q,\mathbb{R})$: negative-definite on the skew subalgebra $\mathfrak{so}(K_q)$, positive-definite on its symmetric complement. The manuscript's 2D abelian-exact worked example reaches $\mathrm{SO}^+(1,1)$ by *postulating* a complexified frame ($\phi_\tau = i\psi_\tau T$, $T$ symmetric with $\mathrm{tr}(T^2)>0$), a $+\mathrm{tr}(AB)$ bilinear form, and a real-part projection $G^{\mathrm{Lor}}_{\mu\nu}:=\mathrm{Re}(G_{\mu\nu})$; free-energy minimisation is *not* shown to select this configuration, so it demonstrates structural compatibility, not derivation. The round-2 revision (below) shows the complexification is dispensable in four dimensions.

> [!note] Editorial: PIFB round-8 review corrections (2026-06-20). A deep adversarial pass corrected two participatory-program claims. (1) **Worked-example representation.** The 2D abelian-exact signature toy realises the two-dimensional vector representation of $\mathrm{SO}^+(1,1)$ in $\mathrm{GL}(2,\mathbb{R})$ (single generator $T=\mathrm{diag}(1,-1)$, $K_q=2$, 2D base), *not* the four-dimensional vector representation of $\mathrm{SO}^+(1,3)$; the 4D Lorentz case is available inside the complexified $\mathrm{GL}(K_q,\mathbb{C})$ only through a four-generator extension the manuscript does not carry out. (PIFB had attached the 4D $\mathrm{SO}^+(1,3)$ rep to the worked example; corrected at the signature-resolution and open-problems statements.) *(The four-generator extension is now carried out, and in the real sector, by the round-2 result below.)* (2) **Gauge-curvature falsifier sign.** The conditional (Regime-II) gauge-curvature-minimisation conjecture reads curvature as transport *inefficiency*, so it entails a strictly **positive** partial correlation between the plaquette-averaged Wilson curvature $1-W_{ijk}/K_q$ (zero at flatness, growing as holonomy departs from $I$) and corpus cross-entropy per token (a cost; lower = more efficient), with a non-positive partial correlation as the falsifier. PIFB's pre-registered test had the sign inverted (predicted negative, "non-negative falsifies"), so it would have confirmed the conjecture exactly when false; now corrected.

> [!note] Editorial: PIFB2 round-2 review result (2026-07-02) — the 4D signature is reachable in the all-real sector. The deep review closed the flagged four-dimensional gap. For $K_q \ge 6$, take one **real skew** generator $S$ supported on two coordinates ($\mathrm{tr}(S^2) = -2 < 0$, the temporal direction) together with **three traceless, mutually trace-orthogonal symmetric diagonal** generators on the remaining coordinates (the spatial directions). All four generators commute, so $\phi = \psi_\tau S + \sum_a \psi_a T_a$ is confined to an abelian subalgebra and the connection is abelian-exact, $A_\mu = \partial_\mu\phi$ (Regime I, $F_{\mu\nu} = 0$). Because $\mathrm{tr}(SX) = 0$ identically for skew $S$ and symmetric $X$, every temporal–spatial cross term vanishes *with no projection*, and the frame-twist metric $G_{\mu\nu} = \mathrm{tr}(A_\mu A_\nu)$ is real, diagonal, rank four, of signature $(-,+,+,+)$ wherever the four differentials are independent, with orthonormal-frame group $\mathrm{SO}^+(1,3)$. This eliminates the imaginary-frame, complex-bilinear-pairing, and real-part-projection postulates entirely; they survive only in the 2D single-generator example, where abelian exactness confines $\phi$ to one generator whose real trace form carries a single sign. Verified numerically this session (signature exact; abelian exactness of $U^{-1}\mathrm{d}U = \mathrm{d}\phi$ to $7\times10^{-7}$). Honest limits: the resulting metric is $\mathrm{d}s^2 = -(\mathrm{d}\chi_0)^2 + \sum_a (\mathrm{d}\chi_a)^2$, the pullback of the Minkowski metric along $\psi:\mathcal{C}\to\mathbb{R}^{1,3}$, hence *coordinate-flat* — the construction settles signature **availability**, not curvature. The open problem sharpens accordingly: no longer whether an indefinite pullback exists in 4D, but whether free-energy dynamics **select** one compact and three non-compact commuting frame directions (the $1{+}3$ split). Source: [[participatory-it-from-bit]] round-2 revision (Proposition `prop:4d_signature`).

### The participatory loop

The "participatory universe" half is realised dynamically: there is **no external controller** of belief dynamics, and the variational free energy is "not imposed from outside; it is the definition of what agents minimize." Natural-gradient descent is the steepest-descent flow $\dot\theta = -\mathrm{grad}_g\,\mathcal{F}$ on the Fisher–Rao metric (distinct from geodesic flow). The loop closes through top-down cross-scale flow

$$
\mathcal{I}_{s\to s+1} = \sum_{I,\,i\in I}\mathrm{KL}\!\big(q_i^{(s)} \,\big\|\, \Omega_{i,I}[q_I^{(s+1)}]\big) \ge 0,
$$

vanishing only at perfect post-detection consensus. In the single reported run, far-from-equilibrium operation is *transient*: the non-equilibrium score spikes to $\approx 0.63$ during reorganisation then returns to $\approx 0.05$, so sustained non-equilibrium ("self-excited circuit") is *not* demonstrated by that configuration.

## In this work

- **Manuscript.** The page is developed in [[participatory-it-from-bit]] (Dennis), principally in the "It From Bit: The Pullback Construction" section (the boxed induced-metric equations), the three-tiers / observable-sectors sections, and the signature-problem analysis. The RG-spine successor `PIFB2.tex` restructures the epistemic hedges into a single numbered fence register (F1–F6) and gives Part II a consolidated postulate register (P1–P10) with the pullback, signature, and consensus results stated as numbered theorems and propositions (round-2 deep review, 2026-07-02). The README ([[Gauge-Theoretic Multi-Agent VFE Model]]) frames the whole repository as "Wheeler's 'It From Bit' implemented as a participatory loop of agents observing themselves into existence."
- **Code.** The induced geometry lives in `gauge_agent/pullback.py` (`PullbackMetric.induced_metric(agent, tier=...)`, with a `MetricDecomposition` classifier splitting eigenvalues into observable/dark/internal masks). Per the manuscript's *Implementation scope* note, the codebase realises only the **belief-tier, flat-frame ($A^{(i)}=0$) score-only pullback** plus a participation-ratio effective dimension and a uniform-mean consensus surrogate; the structural/prior/raw tiers, the frame-twist block, and the Haar-averaged consensus metric are theory-only and exercised only by the test suite. The pullback module is listed as `[Layer 8]` in the module map alongside `manifolds.py` and `manifold_system.py`.
- **Related model constructs.** The participatory loop is carried by [[Ouroboros multi-scale dynamics]] and [[Meta-agents and hierarchical emergence]]; the multi-scale read-off relates to [[Renormalization-group flow of beliefs]]. The dynamical substrate is [[Multi-agent variational free energy]] minimised by [[Natural gradient]] descent on the [[Fisher information metric]], with agents formalised via [[Agents as fibre-bundle sections]] and inter-agent [[Gauge transformation|gauge]] transport $\Omega_{ij}=\exp(\phi_i)\exp(-\phi_j)$.

## Sources

- [[participatory-it-from-bit]] — the manuscript that defines the pullback "it from bit" construction, the three induced-geometry tiers, observable sectors, and the participatory loop.
- [[wheeler-1990-it-from-bit]] — Wheeler's source essay: reality is informational, "no phenomenon is a phenomenon until it is an observed phenomenon."
- [[parr-2022-active-inference]], [[friston-2017-active-inference-process-theory|friston-2017-active-inference-process]], [[ramstead-2019-enactive-inference|ramstead-2019-variational-neuroethology]] — the single-agent active-inference / Markov-blanket substrate the framework generalises.
- [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]] — the entropic-dynamics precedent for deriving physical structure from information geometry.
- [[fuchs2014-qbism-locality|fuchs-2014-qbism]], [[rovelli-1996-relational-qm]], [[seth-2021-being-you]], [[tononi-2016-iit]], [[VanRaamsdonk-2010-spacetime-entanglement|vanraamsdonk-2010-entanglement-spacetime]], [[zurek-2003-einselection|zurek-2003-decoherence]], [[page-wootters-1983]] — participatory / observer-relative / emergent-geometry neighbours discussed in the related-work and observer sections.
- [[fuchs-2017-participatory-realism]] — the source naming "participatory realism" as the common interpretive thread across QBism and relational quantum mechanics, the observer-as-participant reading this page extends.
- [[brukner-2018-no-go-observer-facts]], [[adlam-2022-cross-perspective|adlam-rovelli-2022-cross-perspective]] — the no-go theorem against observer-independent facts and the cross-perspective links restoring consistency, sharpening the "observer-dependent reality" / consensus-metric tier.
- [[caticha-bartolomeo-reginatto-2015-entropic-dynamics]] — the entropic-dynamics reconstruction of quantum theory from information geometry, the precedent for inducing physics-like structure the pullback construction follows.
- [[ladyman-ross-2007-every-thing-must-go]], [[cassirer-1910-substance-function]] — the structural-realist and relational ("function over substance") ontological backing for a framework where geometry is induced relationally rather than presupposed.
- [[lahav-2022-relativistic-consciousness|lahav-neemeh-2022-relativistic-consciousness]] — the observer-relative ("relativistic") account of conscious experience, a neighbour to the agent-dependent structural-tier geometry $G^{(s)}_i$.
- [[zenil-2013-computable-universe]] — survey anthology of the digital-physics / "nature as computation" lineage (Zuse, Wolfram, 't Hooft, Lloyd; Penrose foreword), the computational wing of "it from bit" the framework inherits and positions against.

## See also

- [[Gauge-Theoretic Multi-Agent VFE Model]]
- [[Multi-agent variational free energy]]
- [[Agents as fibre-bundle sections]]
- [[Ouroboros multi-scale dynamics]]
- [[Meta-agents and hierarchical emergence]]
- [[Renormalization-group flow of beliefs]]
- [[Fisher information metric]]
- [[Natural gradient]]
- [[Gauge transformation]]
- [[Killing form]]
- [[Holonomy]]
- [[Parallel transport]]
- [[QBism]]
- [[Quantum reference frames]]
- [[Observer-dependent facts and Wigner's friend]]
- [[Structural realism]]
- [[Relativized a priori]]
- [[Bayesian mechanics]]
- [[Emergent spacetime and holography]]
- [[Physics from Fisher information]]
- [[Quantum information geometry]]
- [[Explanatory gap]]
- [[Mathematical consciousness science]]
- [[Collective active inference]]
