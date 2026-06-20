---
type: manuscript
title: "Attention as Gauge-Theoretic Variational Inference"
aliases:
  - "GL(K) Attention"
  - "Gauge-Theoretic Attention"
  - "Attention as Gauge-Theoretic Variational Inference"
authors:
  - Robert C. Dennis
year: 2026
status: in preparation
tags:
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
created: 2026-06-18
updated: 2026-06-20
---

# Attention as Gauge-Theoretic Variational Inference

> [!info] Manuscript
> Source files: `GL(K)_attention.tex` (main) and `GL(K)_supplementary.tex` (supplement), Manuscripts-Theory.
> Author: Robert C. Dennis (Independent Researcher). Status: **in preparation**.
> Code: `github.com/cdenn016/epistemic-geometry`.

## Abstract

The manuscript advances a single thesis: *transformer attention is variational inference over information sources.* Each token is modeled as a Gaussian "agent" $q_i = \mathcal{N}(\mu_i, \Sigma_i)$ living on a statistical fiber bundle, and the generalized attention weight

$$\beta_{ij} = \operatorname{softmax}_j\!\left(-\,D_{\mathrm{KL}}\!\left[q_i \,\|\, \Omega_{ij} q_j\right]/\tau\right)$$

is *derived* from minimizing the variational free energy of a mixture-of-sources generative model, in which each agent infers — via gauge transport $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ — which neighbor generated its state. The KL divergence arises exactly; the softmax follows from constrained optimization over the categorical source-selection posterior.

Under successive limits of this principle, standard transformer design choices are recovered as special cases of the variational geometry: the temperature scaling $1/\sqrt{d_k}$ from dimensional concentration of the KL divergence; layer normalization as the geometric condition for frame-independent inference; multi-head attention as a block-diagonal restriction of the gauge algebra; and causal masking / positional biases from non-uniform attention priors $\pi_j$. Two successive limits (isotropic covariances, then flat gauge connection) recover the standard rule $\beta_{ij} \propto \operatorname{softmax}(Q_i K_j^\top / \sqrt{d_k})$, with the invertible head-space factor of $W_Q W_K^\top$ identified as $\sigma^{-2}\Omega^{-\top}$.

## Core contributions

- **Attention as derived, not assumed.** The full KL+softmax attention rule is obtained from a multi-agent variational free energy on a principal $G$-bundle with statistical-manifold fibers, rather than posited as an architectural primitive.
- **Standard attention as a degenerate limit.** Standard dot-product attention is the isotropic, flat-bundle, constant-gauge limit of gauge-theoretic attention; the rectangular projections $W_Q, W_K$ are *not* individually gauge transformations, but their product's invertible head-space factor is identified with $\sigma^{-2}\Omega^{-\top}$.
- **A working unreduced model.** A $\mathrm{GL}^+(K)$ gauge transformer is trained using *only* information divergences, gauge transport, and natural-gradient dynamics — with no learned attention projections, no MLPs, and no pointwise activation functions (a single linear output projection is the lone neural component).
- **Architectural explanations.** The framework supplies first-principles accounts of temperature scaling, layer normalization (key-norm cancellation condition $\|\mu_j\|^2 \approx C$), multi-head structure ($\bigoplus_a \mathfrak{gl}(d_{\mathrm{head}})$), and RoPE as position-dependent gauge frames.
- **Learning as symmetry breaking.** The untrained network is a gauge-symmetric vacuum whose degeneracy is broken by observations; training is interpreted as explicit symmetry breaking.

## Key results / theorems

- **Theorem ($\mathrm{GL}(K)$ Gauge Invariance).** For Gaussians $P, Q$ on $\mathbb{R}^K$ and any $\Omega \in \mathrm{GL}(K)$, $D_{\mathrm{KL}}(\Omega_* P \,\|\, \Omega_* Q) = D_{\mathrm{KL}}(P \,\|\, Q)$; the $(\det\Omega)^2$ factors cancel identically. The result extends to **all $f$-divergences**, so transport need only satisfy $\det\Omega_{ij}\neq 0$ — the full $\mathrm{GL}(K)$ acts as a gauge symmetry. (The $e^\phi$ parameterization restricts to the identity component $\det>0$.)
- **Lemma (Vanishing holonomy / cocycle identity).** The vertex-frame transport $\Omega_{ij}=\exp(\phi_i)\exp(-\phi_j)$ satisfies $\Omega_{ij}\Omega_{jk}\Omega_{ki}=I$ as an algebraic identity, so both the gauge transformer and standard transformers operate in a **flat-bundle regime with trivially vanishing reconstructed holonomy** (Regime I). The edge-relaxed extension $\Omega_{ij}=\exp(\phi_i)\exp(\delta_{ij}G)\exp(-\phi_j)$ promotes the bundle to non-trivial holonomy (Regime II), reserved for the companion paper.
- **Three-limit reduction.** Standard $Q K^\top$ attention is recovered through ordered limits (flat connection $\to$ gauge variation $\to$ anisotropy), with $W_Q W_K^\top = \sigma^{-2}\Omega^{-\top}$ in the constant-gauge isotropic limit.
- **Proposition (Conditional CLT contraction of the gauge VFE family).** Defining couplings $g_1$ (anisotropy), $g_2$ (gauge variation), $g_3$ (holonomy), under an i.i.d. token-perturbation assumption the central limit theorem gives scaling dimensions $y_1=-\tfrac12$, $y_2=y_3=-1$ (and $y_3^{(\mathrm{action})}=-2$), all irrelevant, so the transformer limit $g^*=0$ is an infrared-stable fixed point. **Conjecture (Universality):** trained transformers occupy this fixed point — *stated, not validated*; measured graph exponents ($y_2\approx-0.6$, $y_3\approx+0.2$) deviate and the interpretation is left open.

### Empirical results (as reported)

- **WikiText-103:** a $\mathrm{GL}(15)$ gauge transformer ($K=90$, 81.4M params) reaches **test perplexity 71.6**, outperforming a standard transformer at matched embedding dimension ($d_{\text{model}}=90$, PPL 118.6) by **$1.66\times$**, while a parameter-matched standard transformer ($d_{\text{model}}=1{,}280$, 84.2M params) still wins at PPL 48.5. A $\mathrm{GL}(10)$ embedding sweep improves monotonically to PPL **64.9** at $K=120$.
- **Japanese Wikipedia:** a $\mathrm{GL}(15)$ model with $K=90$ reaches **test perplexity 24.2** (headline run combines diagonal covariance with RoPE on $\mu$; subject to a stated approximation).
- **Learned gauge frames** develop categorical separation in a low-dimensional subspace with within-category diversification in the bulk.

### Supplementary

The supplement (`GL(K)_supplementary.tex`) collects derivations and additional validations:

- **Covariance dynamics (App. B).** Derives $\partial\mathcal{F}_i/\partial\Sigma_i$ and the matrix-valued precision fixed point $\Sigma_i^{-1}=\tfrac12[\Sigma_{p,i}^{-1}+\sum_j\beta_{ij}(\Omega_{ij}\Sigma_j\Omega_{ij}^\top)^{-1}]$; in the alignment-dominated limit ($\alpha_i,\tau$ small), $\Sigma_i^{-1}\approx\langle(\Omega_{ij}\Sigma_j\Omega_{ij}^\top)^{-1}\rangle_\beta$. The $\beta$-fixed Hessian is positive-definite (stationarity), with an un-suppressed Schur correction $-\tau^{-1}\mathrm{Cov}_\beta(\cdot)$ that can be indefinite.
- **Gauge-frame gradients (App. C).** Derives $\partial\mathcal{F}/\partial\phi_i$ via the differential of the matrix exponential, with $\mathrm{SO}(N)$ (Rodrigues) and $\mathrm{GL}(K)$ (Higham integral / block-matrix) specializations, plus a Cartan/Killing-form preconditioner.
- **Numerical methods (App. D).** Natural-gradient descent on the Gaussian manifold and SPD-manifold retraction for $\Sigma$.
- **BERT validation (App. E).** Frozen `BERT-base-uncased` across **105 passages** and five architectures: at the empirical optimum $\tau=19.0$ (theory value $2\sqrt{d}=16$, $d=64$), the flat-bundle KL attention $\beta^{\text{flat}}_{ij}=\operatorname{softmax}(-\|Q_i-K_j\|^2/\tau)$ agrees with dot-product attention at grand mean $\bar r = 0.804$ (95% CI $[0.771,0.838]$), entropy matching $H(\beta)/H(\alpha)=1.076$, key-norm bias Cohen's $d=1.43$, per-head temperature dispersion (RoBERTa median $\tau=25$). Treated as a consistency check, since high $r$ partly follows from an algebraic identity.
- **RG universality (App. F).** Numerically reproduces the CLT exponents on synthetic i.i.d. data; flags graph-measured deviations as open.
- **Symmetry-breaking simulations (App. G).** Six $\mathrm{SO}(3)$ ($\ell=4$) agents on a 2D base: without observations beliefs converge to a common gauge orbit (a shared nonzero norm at distinct directions, $\mathrm{Var}(\|\mu\|)\to$ machine precision; the $\ell=4$ $\mathrm{SO}(3)$ irrep has no nonzero invariant vector, so the orbit, not any single belief vector, is the invariant object); with observations symmetry breaks and norms diverge. Also gives the full two-channel **model-channel free energy** $\mathcal{F}_{\text{full}}$ with belief/model alignment terms $\beta_{ij}, \gamma_{ij}$ (set $\gamma_{ij}=0$ here).
- **Conditional uniqueness of forward KL (App. H).** Within the convex $f$-divergence class, the forward KL ($f(t)=t\log t - t +1$, $f'(t)=\log t$) is the unique divergence yielding a closed-form Gibbs belief update with exponential-family closure *and* a consistent dual (envelope-theorem) interpretation of the attention weights — reverse KL, $\chi^2$, and Jensen-Shannon each break log-linearity.
- **Prior-bank decode derivation (App. I).** Shows the decode $\mathrm{logits}=-D_{\mathrm{KL}}(q_i^\star\|\pi_v)/\tau$ is the composition of the Bishop Gaussian quadratic discriminant with the variational plug-in $\mathbb{E}_q[\cdot]$, identifying it with the accuracy term of $\mathcal{F}$ (structural, not a training-objective, claim).

## Relevance to the program

This manuscript is the attention-mechanism cornerstone of the gauge-theoretic variational-free-energy program, sitting in both the [[VFE Transformer Program]] and the [[Gauge-Theoretic Multi-Agent VFE Model]] projects. It operationalizes the [[Variational free energy]] principle ([[Free-energy principle active inference]]) as the generator of attention, and supplies the formal backbone for several program concepts:

- [[Gauge transformation]], [[Parallel transport]], [[Holonomy]], and [[Agents as fibre-bundle sections]] — the bundle scaffold from which attention is derived.
- [[Group equivariance]] / [[Gauge equivariant CNN]] / [[Group equivariant CNN (G-CNN)]] — the geometric-deep-learning lineage the paper positions against ([[Gauge equivariance and geometric deep learning]]).
- [[Fisher information metric]] and [[Natural gradient]] — the information-geometric training dynamics ([[Information geometry and natural gradient]]).
- [[Precision weighting]] and [[Prediction error]] — recovered in the covariance fixed point and predictive-coding connection ([[Variational free energy and predictive coding]], [[Predictive coding network]]).
- [[SPD-manifold geometry and Riemannian optimization]] — the $\Sigma$ updates and retraction.
- [[Attention mechanisms — theory and positional structure]] — the core theme this paper anchors; RoPE-as-gauge-frame and multi-head-as-block-algebra results.
- [[Meta-agents and hierarchical emergence]], [[Renormalization-group flow of beliefs]], [[Ouroboros multi-scale dynamics]] — the coarse-graining/RG conjecture and meta-agent consensus connect to the companion [[participatory-it-from-bit]] manuscript (cited in-text as the source of the cross-scale prior-propagation and Regime-II holonomy program). The "learning as symmetry breaking" reading also touches [[Participatory realism (it from bit)]].

Related program manuscripts: [[belief-inertia]], [[meta-entropy-manuscript]].

## Peer review (2026-06-19)

A multi-agent, wiki-grounded peer review (eight expert lenses, adversarial verification; full report in the `V3_Transformer` repo at `docs/reviews/2026-06-19-glk-attention-wiki-peer-review.md`) found the core derivations sound — the $\mathrm{GL}(K)$-invariance theorem, the softmax-as-KKT derivation, the covariance precision fixed point, the SPD retraction, and the App. H forward-KL uniqueness result all survived adversarial verification, and no finding overturns a derivation. The consequential weakness is bibliographic: the standalone manuscript is systematically under-cited against this knowledge base. Confirmed overlooked connections (each catalogued here, none engaged in the GL(K) body):

- **Gauge–FEP prior art.** [[sengupta-friston-2017-bayesian-gauge-theory]] ("approximate Bayesian inference *is* a gauge theory") and [[sengupta-2016-neuronal-gauge-theory]] are the most direct precursors; the Introduction's "stubbornly separated" framing overstates novelty against them. The body cites neither (see bib defect below).
- **Architecture-as-RG.** [[mehta-schwab-2014-variational-rg-deep-learning]] (exact variational-RG ↔ deep-learning map) and [[beny-osborne-2015-info-geometric-rg]] (RG as a Fisher–Bures monotone flow) are the precedents the RG-fixed-point conjecture must position against; both uncited.
- **Depth and the no-MLP claim.** [[dong-2021-rank-collapse]] (pure attention loses rank doubly-exponentially with depth) reframes residual connections as a load-bearing anti-collapse counterforce and exposes the "no-MLP minimality" claim as untested — every experiment is single-layer. Held at *major*.
- **Attention-as-clustering.** [[geshkovski-2023-mathematical-transformers]] is the rigorous mathematics of the consensus / emergent-cluster results the paper reports; uncited. Held at *major*.
- **Head specialization.** [[voita-2019-multihead]] supplies the exact taxonomy the emergent-structure section uses, plus a concrete falsification (head pruning); in bib, uncited in body.
- **Minor but apt:** [[wang-2023-riemannian-self-attention-spd]] (nearest SPD-attention prior art), [[von-oswald-2022-transformers-gradient-descent]] ("layers as VFE iterations"), [[petz-1996-monotone-metrics]] (matrix Chentsov uniqueness, bears on App. H), and the multi-agent FEP / Bayesian-mechanics clusters ([[friston-2024-federated-inference]], [[dacosta-2021-bayesian-mechanics]]).

**Bibliography defect.** `references.bib` contains `Sengupta2016NeuronalGauge` and a `SenguptaFriston2018` key that points to a *different* paper (arXiv:1810.08750, belief-state synchronization); the most-direct prior art, arXiv:1705.06614, is **absent** from the bib. Fix applied 2026-06-19: added it under key `sengupta2017gauge` and drafted a dedicated Introduction related-work paragraph plus abstract/positional calibration clauses into the manuscript.

## Deep review passes 3–4 (2026-06-20)

Three further multi-agent passes (wiki-grounded, each finding adversarially verified before it could be reported) extended the 2026-06-19 review; all confirmed fixes were applied to the manuscript and pushed to the `V3_Transformer` branch `vfe3-per-layer-figures`. Reports live in that repo at `docs/reviews/2026-06-19-glk-attention-deep-review-pass3.md` and `docs/reviews/2026-06-20-glk-attention-deep-review-pass4.md`, with a durable per-proof verification log at `Manuscripts-Theory/DERIVATION_VERIFICATION.md`.

**Derivations and code fidelity (pass 3).** The seven load-bearing proofs — $\mathrm{GL}(K)$ invariance, softmax-as-KKT, the three-limit reduction, the covariance precision fixed point with its Schur correction, the gradient-descent update, App. H forward-KL uniqueness, and the App. C dexp gradients — were re-derived with SymPy/NumPy and all hold; no sign, transpose, or index error was found. The substantive catch was documentation-versus-code drift: the supplement named functions absent from the released tree (`sanitize_sigma`, and `retract_to_principal_ball` with a modulo-$2\pi$/antipodal algorithm) and labeled the Regime-II mechanism a `connection.py` "MLP mode" when it is a single bilinear `connection_W` parameter ($\delta_{ij}^a=\mu_i^\top W^a\mu_j$, default off, gauge-invariant only at $W=0$). The prose was rewritten to the real `retract_phi` group-aware Frobenius trust-region clamp and the actual inline SPD eigenvalue clamp. A stale glossary entry making the per-head temperature $\kappa_a\propto\sigma_a^2$ (double-counting the covariance scale) was corrected to the $\sigma$-independent sharpness handle $\tau_a=\kappa_a\sqrt{d_{\mathrm{head}}}$.

**RG $g_2$ exponent — settled.** Both earlier passes flagged an apparent tension between the scaling dimension $y_2=-1$ and an $n^{-1/2}$ reading suggested by $g_2$'s single-edge norm definition. It resolves in favor of $y_2=-1$: under the manuscript's own coarse-graining the meta-agent transport $\Omega_{AB}=(|A||B|)^{-1}\sum_{i\in A, j\in B}\Omega_{ij}$ averages $|A||B|=n^2$ inter-cluster edges and so contracts as $(n^2)^{-1/2}=n^{-1}$, whereas the intrinsic anisotropy $g_1$ averages only $n$ token covariances and contracts as $n^{-1/2}$. Confirmed numerically (the contraction ratio matches $1/n$ to three significant figures) and against the supplement's own CLT validation table. The earlier doubt was a main-text exposition gap — the $n^2$-edge bookkeeping lived only in the supplement — now closed by porting the edge-count justification into the main text; no exponent changed. The *trained-model* exponents still deviate (graph-measured $y_2\approx-0.66$, $y_3\approx+0.17$), an honest open question; see [[Renormalization-group flow of beliefs]].

**Dimensional, numerical, and cross-paper consistency (pass 4).** Confirmed and fixed: the boxed GLU summary equation dropped the gauge-transport sandwich metric $(\Omega_{ij}\Sigma_j\Omega_{ij}^\top)^{-1}$ that its own preceding equations carry (a presentational defect; the derivation is correct); a Discussion ablation ratio stated as $1.87$–$1.91\times$ was computed against the $\mathrm{GL}(10)$/PPL-76.4 model but attributed to the $\mathrm{GL}(15)$/PPL-71.6 headline model (correct ratios $1.94$–$2.04\times$); a training-curve caption disagreed with its body on initial/final perplexity. The load-bearing cross-paper catch: the manuscript deferred the Fisher–Bures "metric-level $g_2$ formulation" and the trained-model RG validation to the companion [[participatory-it-from-bit]], which contains no $g_i$ couplings, no Fisher–Bures formulation, and explicitly disclaims a derived RG flow ("an RG-flavored cascade but is not a derived RG flow"); the two deferrals were retargeted to "future work." Two conclusion-level framing claims — the residual as "the substantive content of the correspondence rather than a coincidence of form," and "learning is symmetry breaking" stated as a revealed result — were calibrated to match the body's own status-S taxonomy and the Elitzur reparameterization-redundancy caveat. A batch of minor consistency fixes followed: the $\kappa$ reduction reconciled with the companion, the overloaded $\lambda$ renamed to $\lambda_K$ in the key-norm section, two uncited supplementary tables anchored, the Euclidean-versus-affine-invariant caveat on the coarse-grained $\Sigma_A$, an [[amari-1998-natural-gradient|Amari (1998)]] citation at the natural-gradient subsection, a WikiText-103 token-count annotation, and a $g_3$-normalization note.

> [!note] Do not re-flag (rejected on adversarial verification). Future reviews should not resurrect these: (i) the cited entry point `transformer/vfe/train_vfe.py` is **correct** — the released artifact is the separate `github.com/cdenn016/epistemic-geometry` repository, not the `V3_Transformer` clean-room rebuild, so its absence from V3 is a category error; (ii) the edge-relaxed holonomy does **not** collapse to an abelian phase, since $\delta_{ij}\cdot G$ is the basis contraction $\sum_a\delta_{ij}^a G_a$ (matrix-valued, non-abelian; numerical commutator norm $\approx 0.5$); (iii) the meta-agent arithmetic-mean transport leaving $\mathrm{GL}(K)$ is a terminology nit that does **not** invalidate the RG exponents (the intrinsic mean gives $y_2=-1.01$); (iv) the holonomy/compositionality bridge is **not** unfalsifiable-as-stated — the Flat-Bundle-Limit section already demotes it to an open question with a COGS/SCAN measurement sketch; (v) the abstract copula "attention is variational inference" attaches to the exactly-derived attention rule, not to the structural/interpretive architecture components of Table 1.

## Deep review passes 5–7 (2026-06-20)

Three further recompute-driven multi-agent passes closed out the deep review; all confirmed fixes were applied to the canonical vault manuscripts (`manuscripts/GL(K)_attention.tex`, `manuscripts/GL(K)_supplementary.tex`, commit `168468d`) and the reports live in the `V3_Transformer` repo at `docs/reviews/2026-06-20-glk-attention-deep-review-pass{5,6,7}.md`. Passes 5–6 were notation/citation hygiene plus a deep mathematical recompute sweep (16 raw findings, 10 confirmed). Pass 7 (a 17-agent completion run) confirmed the remaining actionable items and ran six fresh recomputation lenses with three-voter adversarial verification. After seven passes the mathematics is robust: pass 7 found a single genuine new defect (the App I decode constant) plus equation-level precision fixes, while fifteen separately recomputed identities returned correct or already-candid.

**Pass-7 fixes (each independently recomputed in NumPy/SymPy):**

- **App I decode constant $C$ (supplement).** The stated $C = -(K/2)\log 2\pi - K/2$ is wrong; the cross-entropy identity $\mathbb{E}_q[\log p] = -D_{\mathrm{KL}}(q\|\pi_v) - H(q)$ is exact, so **$C = 0$** (residual machine-zero versus $+5.68$ for the stated value; three voters plus the numerical-stats lens agree). Inert for every downstream claim ($C$ is $v$-invariant and cancels in the softmax) but a flatly wrong displayed identity in a rigorous appendix.
- **Connection transformation law (supplement, bundle overlaps).** The displayed adjoint form was wrong under the manuscript's own left-invariant convention $A = U^{-1}\partial U$, and the textbook $(\partial\Omega)\Omega^{-1}$ fix is *also* wrong here (it belongs to the right-invariant convention) — the adversarial verifier caught the trap. Corrected to the left-invariant form $A^{(i)} = A^{(j)} + U_j^{-1}(\Omega^{-1}\partial\Omega)U_j$ (confirmed numerically, residual $3.4\times10^{-10}$), with a note giving the textbook form for the right-invariant convention. Non-load-bearing scaffold; the cocycle/holonomy/curvature identities in the section were re-confirmed correct.
- **Multi-head block transport (main).** $\Omega^a = (\sigma^2 W_K^a (W_Q^a)^\top)^{-1}$ used the rectangular $W$ (rank $\le d_{\text{head}}$, singular); corrected to the invertible head-space SVD factor $A$ ($\Omega^a = (\sigma^2 A_K^a (A_Q^a)^\top)^{-1} \in \mathrm{GL}(d_{\text{head}})$).
- **Temperature relabel (main, Discussion).** The grand mean $\bar r = 0.804$ / posterior $0.867$ were tied to the "theory-predicted optimal $\tau \approx 2\sqrt{d_k}$" but were measured at the **empirical optimum $\tau = 19.0$** (theory value 16); relabeled to match the careful phrasing already used elsewhere.
- **RoPE config token (main).** `rope_full_gauge='off'` $\to$ `=False` (`config.py` declares it `bool`).
- **App G vacuum wording (supplement).** "rotationally invariant vacuum state / collapsing to a common point" $\to$ **common gauge orbit**: the figure shows a shared nonzero norm ($0.2857$) at six distinct directions, and the $\ell=4$ $\mathrm{SO}(3)$ irrep has no nonzero invariant vector, so the orbit (not any single vector) is the invariant object.
- **SPD trust region (supplement).** Documented that the diagonal retraction arm clips $\delta\sigma/\sigma$ componentwise (an $\ell^\infty$ bound), distinct from the full arm's Frobenius clip.
- **Central-QK reduction (main).** Added a one-line closure note that under $\Sigma_j = U_j C U_j^\top$ the $j$-only log-determinant terms collapse to the $j$-independent $\log\det C$, so no residual $j$-dependent log-det bias survives in $b_{ij}$.

**Recompute-confirmed robust (no change):** softmax-$\beta$ stationarity with the entropy term (a delta without it); the $-\tau^{-1}\mathrm{Cov}_\beta$ surrogate/envelope gradient gap; the geometric-mean belief update; EM separation / mean-field factorization; App H forward-KL uniqueness (rigorous after the pass-6 realizability fix); the Fisher mean preconditioner $G_\mu^{-1}=\Sigma$ and the covariance natural-gradient projection; the Pennec affine-invariant retraction and Rodrigues dexp; and every reported BERT/ablation statistic.

**Residual items for a future pass (not defects):** the meta-agent moment-matching identity $\Sigma_A = \langle\Sigma_i\rangle + \mathrm{Var}_A(\mu)$; the ALiBi/T5/window logit reductions versus the published forms; the Frobenius-pullback natural-gradient metric (App D).

## References cited

Resolved from `references.bib` (unique keys across the main paper and supplement):

- [[vaswani-2017-attention|Vaswani et al. (2017), Attention is all you need]]
- Bahdanau, Cho & Bengio (2014), Neural machine translation by jointly learning to align and translate
- [[amari-1998-natural-gradient|Amari (1998), Natural gradient works efficiently in learning]]
- [[bronstein-2021-geometric-deep-learning|Bronstein, Bruna, Cohen & Veličković (2021), Geometric deep learning: grids, groups, graphs, geodesics, and gauges]]
- Friston (2010), The free-energy principle: a unified brain theory? *(cite key `friston2010free`)*
- [[friston-2010-free-energy-principle|Friston (2010), The free-energy principle: a unified brain theory? (supplement, cite key `Friston2010`)]]
- Friston, Parr & de Vries (2017), The graphical brain: belief propagation and active inference
- [[parr-2022-active-inference|Parr, Pezzulo & Friston (2022), Active Inference: The Free Energy Principle in Mind, Brain, and Behavior]]
- [[ramstead-2019-variational-neuroethology|Ramstead, Constant, Badcock & Friston (2019), Variational ecology and the physics of sentient systems]]
- Clark, Khandelwal, Levy & Manning (2019), What does BERT look at? An analysis of BERT's attention
- Fuchs, Worrall, Fischer & Welling (2020), SE(3)-Transformers: 3D roto-translation equivariant attention networks
- Thomas et al. (2018), Tensor field networks: rotation- and translation-equivariant neural networks for 3D point clouds
- Kondor & Trivedi (2018), On the generalization of equivariance and convolution in neural networks to the action of compact groups
- Finzi, Stanton, Ohana & Wilson (2020), Generalizing convolutional neural networks for equivariance to Lie groups on arbitrary continuous data
- Weiler, Geiger, Welling, Boomsma & Cohen (2018), 3D steerable CNNs
- Geiger & Smidt (2022), e3nn: Euclidean Neural Networks
- [[bonnabel-2013-riemannian-sgd|Bonnabel (2013), Stochastic gradient descent on Riemannian manifolds]]
- [[absil-2008-optimization-matrix-manifolds|Absil, Mahony & Sepulchre (2008), Optimization Algorithms on Matrix Manifolds]]
- [[tsai-2019-kernel-attention|Tsai et al. (2019), Transformer dissection: a unified understanding of transformer's attention via the lens of kernel]]
- [[katharopoulos-2020-linear-transformers|Katharopoulos, Vyas, Pappas & Fleuret (2020), Transformers are RNNs: fast autoregressive transformers with linear attention]]
- [[ramsauer-2021-hopfield|Ramsauer et al. (2021), Hopfield networks is all you need]]
- Tishby & Zaslavsky (2015), Deep learning and the information bottleneck principle
- Shwartz-Ziv & Tishby (2017), Opening the black box of deep neural networks via information
- Hinton (2022), The forward-forward algorithm: some preliminary investigations
- [[rao-1999-predictive-coding|Rao & Ballard (1999), Predictive coding in the visual cortex]]
- [[bogacz-2017-free-energy-tutorial|Bogacz (2017), A tutorial on the free-energy framework for modelling perception and learning]]
- [[millidge-2020-pc-approximates-backprop|Millidge, Seth & Buckley (2021), Predictive coding: a theoretical and experimental review]]
- Bishop (2006), Pattern Recognition and Machine Learning
- Murphy (2012), Machine Learning: A Probabilistic Perspective
- Kullback & Leibler (1951), On information and sufficiency
- Su et al. (2024), RoFormer: enhanced transformer with rotary position embedding
- Kim & Linzen (2020), COGS: a compositional generalization challenge based on semantic interpretation
- Lake & Baroni (2018), Generalization without systematicity: on the compositional skills of seq2seq networks
- Devlin, Chang, Lee & Toutanova (2018), BERT: pre-training of deep bidirectional transformers
- [[nakahara-2003-geometry-topology-physics|Nakahara (2003), Geometry, Topology and Physics]]
- [[frankel-2011-geometry-of-physics|Frankel (2011), The Geometry of Physics: An Introduction]]
- [[baez-muniain-1994-gauge-fields|Baez & Muniain (1994), Gauge Fields, Knots and Gravity]]
- [[hall-2015-lie-groups|Hall (2015), Lie Groups, Lie Algebras, and Representations]]
- [[cencov-1982-statistical-decision-rules|Čencov (1982), Statistical Decision Rules and Optimal Inference]]
- [[amari-2016-information-geometry-applications|Amari (2016), Information Geometry and Its Applications]]
- [[pennec-2006-affine-invariant-tensor|Pennec (2006), Intrinsic Statistics on Riemannian Manifolds]]
- [[bhatia-2007-positive-definite-matrices|Bhatia (2007), Positive Definite Matrices]]
- Fulton & Harris (1991), Representation Theory: A First Course
- Sternberg (1994), Group Theory and Physics
- Weinberg (1996), The Quantum Theory of Fields
- Higham (2008), Functions of Matrices: Theory and Computation
- Gallier & Quaintance (2020), Differential Geometry and Lie Groups: A Computational Perspective
- Culver (1966), On the existence and uniqueness of the real logarithm of a matrix
- Boyd & Vandenberghe (2004), Convex Optimization
- Beal (2003), Variational Algorithms for Approximate Bayesian Inference
- Wainwright & Jordan (2008), Graphical models, exponential families, and variational inference
- Blei, Kucukelbir & McAuliffe (2017), Variational inference: a review for statisticians
- Csiszár (1967), Information-type measures of difference of probability distributions
- Cover & Thomas (2006), Elements of Information Theory
- Petersen & Pedersen (2012), The Matrix Cookbook
- Milnor (1976), Curvatures of left invariant metrics on Lie groups
- Cuturi (2013), Sinkhorn distances: lightspeed computation of optimal transport
- Cardy (1996), Scaling and Renormalization in Statistical Physics
- Goldenfeld (1992), Lectures on Phase Transitions and the Renormalization Group
- Wilson & Kogut (1974), The renormalization group and the ε expansion
- Wilson (1974), Confinement of quarks
- Kogut & Susskind (1975), Hamiltonian formulation of Wilson's lattice gauge theories
- Creutz (1983), Quarks, Gluons and Lattices
- Kadanoff (1966), Scaling laws for Ising models near $T_c$
- García-Pérez et al. (2018), Multiscale unfolding of real networks by geometric renormalization
- Anderson (1984/1988), Neurocomputing: Foundations of Research *(cite key `anderson1984basic`)*
- Hoffman & Gelman (2014), The No-U-Turn sampler
- Salvatier, Wiecki & Fonnesbeck (2016), Probabilistic programming in Python using PyMC3
- Bai, Kolter & Koltun (2019), Deep Equilibrium Models
- Chung et al. (2015), A Recurrent Latent Variable Model for Sequential Data
- Fraccaro et al. (2016), Sequential Neural Models with Stochastic Layers
- Krishnan, Shalit & Sontag (2017), Structured Inference Networks for Nonlinear State Space Models
- Dempster, Laird & Rubin (1977), Maximum likelihood from incomplete data via the EM algorithm
- Dai et al. (2019), Transformer-XL: attentive language models beyond a fixed-length context
- Dauphin et al. (2017), Language Modeling with Gated Convolutional Networks
- Radford et al. (2019), Language models are unsupervised multitask learners
- Raffel et al. (2020), Exploring the limits of transfer learning with a unified text-to-text transformer
- Merity et al. (2017), Pointer sentinel mixture models
- Grave et al. (2017), Improving neural language models with a continuous cache
- Chen & Goodman (1998), An empirical study of smoothing techniques for language modeling
- Press, Smith & Lewis (2022), Train short, test long: attention with linear biases (ALiBi)
- Beltagy, Peters & Cohan (2020), Longformer: the long-document transformer
- Xiao et al. (2024), Efficient streaming language models with attention sinks
- Elhage et al. (2021), A mathematical framework for transformer circuits
- Hendrycks & Gimpel (2016), Gaussian error linear units (GELUs)
- Ramachandran, Zoph & Le (2018), Searching for Activation Functions
- Jiang et al. (2023), Mistral 7B

