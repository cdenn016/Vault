---
type: concept
title: "Renormalization-group flow of beliefs"
aliases:
  - "RG flow of beliefs"
  - "Belief renormalization group"
  - "Multi-agent renormalization group"
  - "Real-space RG for beliefs"
tags:
  - cluster/multi-agent
  - cluster/social-physics
  - cluster/info-geometry
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-07-09
---

# Renormalization-group flow of beliefs

## Definition

The **renormalization-group (RG) flow of beliefs** is the program proposal, in the [[Gauge-Theoretic Multi-Agent VFE Model]], to treat the meta-agent hierarchy as a real-space renormalization group on a population of variational beliefs. The manuscript is explicit that this is **RG-inspired rather than a rigorous RG** (see the editorial note below): the defining rescaling-to-original-units step is not performed, no analytic $\beta$-function or fixed point is derived from the variational principle, and the closure ansatz (that the coarse-grained functional stays in the multi-agent KL class) is posited, not proven. At each scale $s$ a system of $N(s)$ agents carries Gaussian beliefs $q_i^{(s)}$, priors $p_i^{(s)}$, and $GL(K)$ gauge frames $\Omega_i^{(s)}$ (see [[Agents as fibre-bundle sections]]). A *blocking* (coarse-graining) step groups agents into blocks $B_I$, replaces each block by a single effective agent at scale $s+1$, and re-measures a vector of effective coupling constants $g(s)$. Iterating the block-then-measure map traces a trajectory through coupling-constant space whose flow, fixed-point *candidates*, and critical exponents are **estimated numerically** by an exploratory pipeline (`gauge_agent/renormalization.py`), distinct from an analytic derivation.

Concretely, in `gauge_agent/renormalization.py` the coupling vector is the eight-component

$$
g(s) = \big(\langle \mathrm{KL}(q_i\Vert p_i)\rangle,\ \langle \mathrm{KL}(q_i\Vert \Omega_{ij}[q_j])\rangle,\ \langle \mathrm{KL}(s_i\Vert \tilde\Omega_{ij}[s_j])\rangle,\ H[\beta_{ij}],\ \Gamma,\ f,\ \xi,\ \Psi\big),
$$

i.e. mean self-KL, mean belief-fiber alignment, mean model-fiber alignment, attention entropy, consensus score, free-energy density, correlation length, and order parameter. The RG map sends $g(s)\mapsto g(s+1)$ by coarse-graining, and the discrete **beta function** is the rate of change of $g$ per logarithmic change of scale.

> [!note] Editorial: RG status, aligned with the manuscript (2026-06-19). The companion [[participatory-it-from-bit]] explicitly demarcates this as RG-*inspired*: it states the construction is "RG-inspired rather than a rigorous-RG analysis," that "we have not exhibited an analytic $\beta$-function ... nor proved scale invariance," that the functoriality result "is not an RG semigroup acting on a coupling space," and that the form-preserving closure class is conceded "empty in the operational regime" (so the five-term form-preservation posit fails there rather than merely being unproven). The `renormalization.py` pipeline that computes $\xi$, $\nu$, $d_f$, $\lambda_{\mathrm{eff}}$, and the discrete $\beta$-function is therefore **exploratory numerical machinery for probing the RG conjecture**, not a proof of an RG flow on a coupling space, and "fixed points / critical exponents" should be read as numerical candidates. An earlier version of this page asserted the hierarchy "*is* a real-space renormalization group" with exponents "computed directly"; that wording has been calibrated to the manuscript's position. The rigorous information-geometric backbones the program leans toward are [[beny-osborne-2015-info-geometric-rg]] (RG as Fisher-metric contraction per scale, the continuous monotone analogue of the closure residual) and [[mehta-schwab-2014-variational-rg-deep-learning]] (a variational coarse-graining that can be an exact RG step).

## Why it matters here

This concept is what lets the [[Gauge-Theoretic Multi-Agent VFE Model]] talk about *emergence across scales* as a controlled, measurable object rather than a metaphor. The same coarse-graining that builds [[Meta-agents and hierarchical emergence|meta-agents]] from blocks of consensus agents is reinterpreted as a Kadanoff/Wilson block-spin step (cf. [[wilson-1975-renormalization-group]], [[wilson-1971-rg-critical-phenomena]]): microscopic belief details wash out under blocking, and what survives is the universal flow of a handful of effective couplings. The module's docstring frames the three-phase picture the manuscript reports — independent $\to$ critical $\to$ hierarchical condensation — and ties RG fixed points to scale-invariant belief theories. Reading the blocking map as an RG on a learned representation rather than on a physical spin lattice follows the variational-RG / deep-learning correspondence of [[mehta-schwab-2014-variational-rg-deep-learning]], and its information-geometric formulation — coarse-graining as a flow on the space of distributions — is made precise by [[beny-osborne-2015-info-geometric-rg]].

RG flow is the natural companion to [[Meta-entropy]] (a thermodynamic-limit counting of belief configurations) and to [[Ouroboros multi-scale dynamics]] (the bidirectional multi-scale tower): RG supplies the scale-by-scale coarse-graining language, meta-entropy supplies the extensive state count, and the Ouroboros tower supplies the running dynamics whose base-scale couplings the RG sweep measures. In the runtime it is exposed as `CONFIG['mode'] = 'rg'`, the **Renormalization-group flow with KL-proximity blocking** preset.

## RG in the GL(K) attention manuscript

The transformer-side Regime-I variables are vertex-shared. Equal-weight blocking therefore averages $n$ vertex fluctuations and gives RMS scaling $n^{-1/2}$, so $y_2=-1/2$. Its cocycle $\Omega_{ij}=U_iU_j^{-1}$ makes $H_{ijk}=I$ and $g_3=0$ identically, leaving no Regime-I holonomy exponent to fit. The rates $n^{-1}$ for a linear edge observable and $n^{-2}$ for its squared action apply only to an explicitly iid independent-edge ensemble. Generic edge relaxation permits nontrivial holonomy but does not establish those independence premises or rates. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial (2026-07-09): a nonzero graph-measured $y_3$ diagnoses an edge-relaxed graph observable; it cannot validate or falsify strict Regime I, where $g_3=0$ algebraically. Regime-I vertex fluctuations instead predict the RMS exponent $y_2=-1/2$. [[gl-k-attention-2026-07-09-review-revision]]

## Details

**Blocking schemes.** Two coarse-graining maps are implemented in `BlockingScheme`. *Majority-rule* blocking groups agents into fixed-size blocks (adjacent pairs in 1D, $2\times2$ cells in 2D). *KL-proximity* blocking is the information-geometric natural choice: it agglomeratively merges the agents whose beliefs are closest in pairwise KL, using a union-find over pairs sorted by alignment energy and stopping at a target block count or a maximum within-block KL. Different blocking schemes should give the same critical exponents — this is the **universality** check, implemented in `UniversalityTest.compare_flows`, which declares two flows to be in the same universality class when their final couplings, scaling dimensions, and exponents agree within tolerance.

**Beta function.** Writing $\zeta$ for the running scale, the code defines

$$
\beta(g) = \frac{dg}{d\ln\zeta} \approx \frac{g(s+1)-g(s)}{\Delta\ln\zeta},\qquad \Delta\ln\zeta = \ln\!\frac{N(s)}{N(s+1)} .
$$

The denominator is the log of the blocking ratio $b_s = N(s)/N(s+1)$ rather than a unit step: because KL-proximity blocking merges a variable number of agents per scale, $\Delta\ln\zeta$ is not constant, and dividing by it makes raw $\Delta g$ magnitude-comparable across scales (an `AUDIT_hierarchy` correction matching manuscript §4.3.2). A degenerate-ratio fallback uses $\Delta\ln\zeta = 1$.

**Fixed points and relevance.** A fixed point is $\beta(g^\*) = 0$, a scale-invariant theory. The engine detects candidates as local minima of $\lVert\beta\rVert$ along the trajectory. Linearizing $\beta(g)\approx M\,(g-g^\*)$ near a fixed point, the eigenvalues of the stability matrix $M$ classify directions: $\lambda>0$ **relevant** (grows under coarse-graining), $\lambda<0$ **irrelevant** (shrinks), $\lambda=0$ **marginal**. Because a single 1D trajectory makes the full Jacobian rank-deficient, the code uses a scalar surrogate $\lambda_{\mathrm{eff}}\approx \lVert d\beta\rVert/\lVert dg\rVert$ with sign taken from $\mathrm{sign}(d\beta\cdot dg)$.

**Correlation length and exponents.** The correlation length $\xi$ is fit from the exponential decay of pairwise KL with distance: a weighted least-squares slope of $\log\mathrm{KL}$ against agent-pair distance gives slope $=-1/\xi$. On a curved base manifold the fit uses geodesic distance and per-agent Riemannian volume weights $w_i\approx\sqrt{|g(c_i)|}$ (the $\chi$-weighted mean of $\sqrt{|g|}$ within each agent's support); it falls back to flat $|i-j|$ distances otherwise. The correlation-length exponent $\nu$ comes from a log-log fit of $\xi\sim|s-s_c|^{-\nu}$ near a fixed point, and the free-energy **scaling dimension** $d_f$ from $f\sim N^{-d_f}$, i.e. $\log f = -d_f\log N + \text{const}$.

**Consensus coupling.** The logged consensus score $\Gamma$ uses the manuscript-conformant Gibbs form $\Gamma_{ij} = \exp(-V_q/\tau_q)\,\exp(-V_s/\tau_s)$ with symmetric pair potential $V_{ij} = (\mathrm{KL}_{ij}+\mathrm{KL}_{ji})/4$, so that the coupling logged by the RG sweep is on the same scale as the criterion the embedded `ConsensusDetector` uses to license meta-agent formation. This keeps the RG diagnostic consistent with the actual coarse-graining: a block is replaced by a meta-agent via `MetaAgentFormation.form_meta_agent`, with the pooled spatial support $\chi$ carried forward so the coarse system does not falsely claim global support.

> [!note] Editorial: The module's header attributes the three-phase scaling picture and a power-law $\Delta E^2 \propto |t-t_c|^{-\alpha}$ with $\alpha\approx 1.8$ to the manuscript (Sections 4, 6). These are manuscript-side results quoted in the docstring; the code computes $\xi$, $\nu$, $d_f$, $\lambda_{\mathrm{eff}}$, and the beta function but does not itself assert that numerical value, so it is recorded here only as the manuscript's claim, not a runtime output.

## In this work

The RG machinery lives in `gauge_agent/renormalization.py` (Layer 7), alongside `ouroboros.py`. The public class `RenormalizationGroupFlow` (exported via `gauge_agent.__all__`) performs the initialize $\to$ equilibrate $\to$ measure $\to$ block $\to$ repeat loop and returns coupling trajectories, beta functions, fixed-point candidates, critical exponents, scaling dimension, correlation lengths, and order parameters; `CouplingConstants` and `CouplingExtractor` define and measure $g(s)$; `BlockingScheme` supplies the coarse-graining maps; `UniversalityTest` checks universality. It is driven from `run_experiment.py` via `CONFIG['mode'] = 'rg'` with `RGConfig(enable, blocking, block_size, max_scales, ...)`, where `blocking` is typed `Literal['kl_proximity', 'majority_rule']`; an RG run additionally emits `<preset>_coupling_trajectory.{pdf,png}`. The flow reuses [[Multi-agent variational free energy|FullVFE / FreeEnergyFunctional]] for equilibration and the consensus/meta-agent formation path shared with [[Meta-agents and hierarchical emergence]].

This page develops the multi-scale, coarse-graining facet of the model; for the configuration-counting thermodynamics see [[Meta-entropy]], for the running multi-scale tower see [[Ouroboros multi-scale dynamics]], and for the inertial / Hamiltonian belief dynamics that drive equilibration at each scale see [[Belief inertia]] and [[Hamiltonian belief dynamics]] (manuscript [[belief-inertia]]).

## Sources

- [[wilson-1975-renormalization-group]] — Wilson's RG: scale-by-scale coarse-graining, fixed points, relevant/irrelevant operators, universality; the template this module adapts to beliefs.
- [[wilson-1971-rg-critical-phenomena]] — Wilson's foundational RG treatment of critical phenomena and the Kadanoff block picture.
- [[wilson-kogut-1974-epsilon-expansion]] — Wilson–Kogut review establishing the epsilon-expansion and the systematic computation of critical exponents from the RG flow.
- [[cardy-1996-scaling-renormalization]] — Cardy's text on scaling and renormalization: correlation-length exponents, scaling dimensions, and the relevance/irrelevance classification used here.
- [[mehta-schwab-2014-variational-rg-deep-learning]] — exact mapping between variational RG and deep learning, the precedent for treating blocking as RG on a learned representation.
- [[beny-osborne-2015-info-geometric-rg]] — information-geometric formulation of RG as a flow on the manifold of distributions, the natural language for KL-proximity blocking.
- [[berges-tetradis-wetterich-2002-nonperturbative-rg]] — nonperturbative / functional RG and the flow of the effective action, a continuum counterpart to the discrete beta function measured here.
- [[vidal-2007-entanglement-renormalization]] — entanglement renormalization (MERA): real-space coarse-graining that disentangles before blocking, a structural parallel to scale-by-scale belief coarse-graining.
- [[participatory-it-from-bit]] — the manuscript (`Participatory_it_from_bit.tex`) that the codebase implements; §4.3.2 supplies the RG-by-blocking-ratio scaling and §§4, 6 the three-phase / condensation picture.
- [[meta-entropy-manuscript]] — configurational meta-entropy and the thermodynamic limit the RG flow's free-energy density and scaling dimension speak to.
- [[belief-inertia]] — Fisher-precision-as-mass belief dynamics underlying per-scale equilibration.
- [[degroot-1974-consensus]], [[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]], [[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]], [[hegselmann-2002-opinion|hegselmann-krause-2002]], [[galam-2008-sociophysics]] — opinion-dynamics / sociophysics precedents for coarse-grained collective belief behavior.
- [[delamotte-2012-nonperturbative-rg]] — pedagogical functional (nonperturbative) RG: the Wetterich flow of the whole effective action, the formalism for making belief coarse-graining exact rather than schematic.

## See also

- [[Meta-agents and hierarchical emergence]]
- [[Ouroboros multi-scale dynamics]]
- [[Meta-entropy]]
- [[Multi-agent variational free energy]]
- [[Agents as fibre-bundle sections]]
- [[Belief inertia]]
- [[Hamiltonian belief dynamics]]
- [[Fisher information metric]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
- [[Community detection and modularity]]
- [[Geometric singular perturbation theory]]
- [[Emergent spacetime and holography]]
