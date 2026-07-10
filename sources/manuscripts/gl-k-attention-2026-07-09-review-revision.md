---
type: manuscript
title: "Attention as Gauge-Theoretic Variational Inference: 2026-07-09 Review and Revision Record"
aliases:
  - "GL(K) Attention 2026-07-09 Review Revision"
  - "GL(K) review revision"
authors:
  - Robert C. Dennis
year: 2026
status: in preparation (major revision)
tags:
  - cluster/gauge-theory
  - cluster/attention
  - cluster/vfe
  - cluster/info-geometry
  - cluster/spd-geometry
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/mathematics
  - field/statistics
  - field/physics
created: 2026-07-09
updated: 2026-07-10
---

# Attention as Gauge-Theoretic Variational Inference: 2026-07-09 Review and Revision Record

> [!info] Manuscript revision record
> Author: Robert C. Dennis. Status: **in preparation (major revision)**.
> This note supersedes specific claims in [[gl-k-attention]]; the older source note remains an immutable historical snapshot.

## Provenance

- Peer-review report SHA-256: `5054879310967C48C094EE6BEB8D7DC10E6726F70039D57E25EEB963DD69418B`.
- Pre-revision main-manuscript SHA-256: `CDE4229198DF48B4D6C1674F0AB828712D22EE77084FEAF99C56270E425F6549`.
- Pre-revision supplement SHA-256: `0C0E356D5B04A91DADB8C0DC4F9A2D16D57746CFBC0A74AB537262DCD0C862C2`.
- Reviewed public V3 commit: `e504f1c5ad5d277f653534cfc7fb63fd3b1bee61`.
- Immutable prior source-note SHA-256: `26F4724AF429C67F985815409E7F311D044D7122EE89B4A68F8A8CB9A0781F20`.
- Research branch and base: `fix/glk-peer-review-findings-20260709`, based on `9496e1e3ed28e90f05d7414a5e8365d45cd97918`; branch HEAD available when ingest drafting began was `daa758896f4aebf56d22b4ebb239372b875af91c`.
- Final main-manuscript SHA-256: `0E38184A9953FA7E4339D8550075359247A9D0ED130EAAB91C4F936FE7C9B986`.
- Final supplement SHA-256: `0136AFC436DE4E093B9BA24FE97457F19EDE59B8868F128E566D4374810C6011`.
- Final bibliography SHA-256: `3E2FE474BE8F36ABDCC6E7DB5C803AA929B2948D67A48C6AD367A0067B924838`.
- Integrated Research revision commit: a commit cannot embed its own identifier without changing its content. The reviewed base, final content hashes, and repository history together provide the non-self-referential provenance record; no post-commit self-edit is promised.

## Counterexample-backed corrections

### 1. Regime-I transport and the transformer comparison

Realized Regime I uses the vertex cocycle $\Omega_{ij}=U_iU_j^{-1}$, which makes loop transport flat but does not make each pairwise transport the identity. If one edge-independent transport is assigned to every attended edge and the set includes a self edge, then $\Omega_{ii}=I$ fixes that constant to the identity. Equally, if the same transport occurs on all three edges of a transitive triple, the cocycle gives $\Omega^2=\Omega$, so invertibility again forces $\Omega=I$. The shared-frame or edge-independent constant reduction therefore yields an identity-bilinear score plus a key-norm bias. A general transformer compatibility $M=W_QW_K^\top$, including a singular matrix, is an additional structural morphism rather than nonidentity Regime-I transport.

### 2. Canonical and surrogate vector fields

The entropy-regularized canonical attention functional and the entropy-suppressed surrogate share the same nonattention contribution, but their belief vector fields differ by the exact response term $-\tau^{-1}\operatorname{Cov}_\beta(E,\nabla E)$. Joint stationarity of the canonical functional does not force the surrogate vector field to vanish. The two vector fields agree exactly where that covariance gap is zero. The row-wise KKT derivation of the unique softmax weights and reduced value $-\tau\log Z$ survives. In the deployed transformer, the target-blind belief objective and the decode cross-entropy are distinct objectives, so a one-step belief update is a filter rather than an exact coordinate argmin and does not inherit shared-functional EM monotonicity.

### 3. Ambient invariance and the realized family

The full-Gaussian KL and $f$-divergence invariance theorem remains exact when one common realized bijection acts on both arguments within the same statistical channel and dimension. It does not compare arguments acted on through different representations. Its realized implementation has two additional restrictions. A single real exponential coordinate $U=\exp(\phi)$ reaches only $\operatorname{image}(\exp)$, a proper subset of $\mathrm{GL}^+(K)$. The live diagonal-covariance family is closed under congruence only for the monomial subgroup, consisting of a nonsingular diagonal matrix times a permutation. A general congruence followed by diagonal projection is an approximation to the ambient action. The isotropic geometric bias also measures scale as well as shape: $\Omega=cR$ with $R\in\mathrm{O}(K)$ preserves isotropy but changes covariance scale and has nonzero bias when $c\ne1$. Nonzero bias is therefore not an anisotropy statistic.

### 4. Frame metrics and belief natural gradients

The literal $\mathfrak{gl}(K)$ Killing form is degenerate on the center and indefinite on noncompact directions. The positive transpose-based Cartan form is invariant under the conformal-orthogonal subgroup, whose central scalar acts trivially, but not under general $\mathrm{GL}(K)$ conjugation. The Frobenius exponential-coordinate pullback is extrinsic and is positive definite only where the differential of the exponential has full rank. These are optional frame conditioners, not demonstrated full-$\mathrm{GL}(K)$ frame natural gradients. At each recorded source SHA, the committed optimizer gate combined with the stored `m_phi_natural_grad=false` configuration routes the frame table to ordinary AdamW through the outer cross-entropy graph at learning rate `0.015` and frame weight decay `0.05`. Every provenance record has `git_dirty=true`, and no dirty diff survives, so the exact executed optimizer implementation cannot be independently reconstructed. The heavy-ball and momentum fields belong only to the disabled custom outer optimizer. The BCH/retraction fields belong only to optional in-E-step frame revision, disabled by `e_phi_lr=0`; neither outer optimizer calls that retraction dispatcher. The pullback preconditioner can serve either optional frame route, but both routes are off in the retained sweep. The Gaussian belief mean and covariance Fisher natural gradients remain valid only for the belief objective within their stated family; they do not define a frame or decode metric.

### 5. Regime-I coarse-graining and holonomy

Regime-I edge transports share vertex variables rather than forming $n^2$ independent edges. For centered iid vertex fluctuations with a finite nonzero second moment, the exact block-mean difference has RMS order $n^{-1/2}$, so $y_2=-1/2$. The vertex cocycle telescopes around every loop, giving $H=I$ and $g_3=0$ identically; there is no Regime-I holonomy exponent. The RMS $n^{-1}$ linear rate and $n^{-2}$ squared-action rate belong only to an explicitly iid independent-edge ensemble. A generic edge-relaxed parameterization permits nontrivial holonomy but does not by itself establish edge independence or either rate. The law-of-total-covariance term $\operatorname{Var}_A(\mu)$ is positive-semidefinite covariance broadening and may be isotropic. Its norm is not an ``emergent anisotropy.'' When evaluated with the block-averaged input-covariance deviation, their historical additive sum is only a triangle-inequality upper-bound proxy for the actual block deviation, not an equality in general.

### 6. Conditional forward-KL uniqueness

The uniqueness argument now requires one fixed admissible witness with a nonempty open essential range of density ratios, or a connected overlap family that forces configuration-specific constants to agree. Ranges from unrelated configurations cannot be pooled. Under this strengthened richness hypothesis and $f''(1)>0$, log-linear closure selects the positive ray $f_c(t)=c(t\log t-t+1)$ up to divergence-null affine terms. A separate normalization, such as $f''(1)=1$, fixes the unit forward-KL scale. For the nested belief minimization, the envelope identity is $\partial F_i/\partial\beta_{ij}=C_{ij}(q_i^*(\beta_i))$. The attention-coordinate objective at fixed $q_i$ is linear in $\beta_i$ plus its entropy regularizer and yields the Gibbs row. After eliminating $q_i$, the same condition becomes an implicit Gibbs fixed point. Differentiating the product $\sum_j\beta_{ij}C_{ij}(q_i^*(\beta_i))$ as though it were the reduced value function is incorrect.

### 7. Same-channel common representations and the fixed readout

The ambient invariance identity applies when both divergence arguments occupy the same channel and receive the same bijective pushforward $\rho_a(g)$. Belief pairs use $\rho_q$ and model pairs use $\rho_p$; a shared abstract group element does not make distinct realized maps identical. For example, applying scalar maps $x\mapsto2x$ and $x\mapsto3x$ to $P=Q=\mathcal{N}(0,1)$ changes the forward KL from zero to
\[
D_{\mathrm{KL}}\bigl(\mathcal{N}(0,4)\mathrel{\|}\mathcal{N}(0,9)\bigr)
=-\frac{5}{18}+\log\frac{3}{2}>0.
\]
The theorem therefore does not license a KL comparison across different representations or dimensions. Nor does divergence-sector invariance make a fixed observation likelihood or vocabulary readout invariant; the complete objective is invariant only when that sector is absent or transformed covariantly. A fixed non-invariant readout generally reduces the redundancy to its stabilizer rather than removing it completely. This does not by itself force specialization, unequal Euclidean norms, or a phase transition; those claims require a declared order parameter and evidence not supplied by the retained sweep.

### 8. Order-Rényi divergence, Amari alpha geometry, and belief-only Fisher scope

The current configuration uses `divergence_family="renyi"` for pairwise order-Rényi belief discrepancies and `renyi_order` for their order, with forward KL at order one. This is distinct from the Li-Turner variational Rényi bound and from Amari alpha-divergences and alpha-connections. For an equal-covariance scalar Gaussian mean displacement, the local Hessian is $a/\sigma^2$ at Rényi order $a$, an order-dependent positive multiple of Fisher rather than one identically normalized metric. The Gaussian Fisher formulas apply to belief means and covariances only. At each recorded source SHA, the committed optimizer route places the frame table and vocabulary parameters in AdamW groups on the separate outer cross-entropy objective; the unavailable dirty diffs preclude an exact claim about the executed optimizer implementation.

### 9. Pointwise bilinear reach and restricted whitened RoPE

For one prescribed pair, varying $U_i$, $U_j$, and $\Sigma_j$ can realize any invertible $M_{ij}=U_i^{-\top}U_j^\top\Sigma_j^{-1}$. This pointwise fact does not establish equality with a standard head that uses one shared, possibly singular compatibility $W_QW_K^\top$ across all inputs and pairs. The gauge family factorizes as $M_{ij}=A_iB_j$ and obeys cross-pair constraints; it is not an arbitrary independent matrix table. Under $\Sigma_j=U_jCU_j^\top$, the score acts on $C^{-1/2}U_i^{-1}\mu_i$ and $C^{-1/2}U_j^{-1}\mu_j$. Raw RoPE follows only for isotropic whitening, or after compatible shared prewhitening when $C$ commutes with the position rotations. The surviving statement is a restricted symmetric RoPE-style score, not general RoPE with independent learned query and key projections.

### 10. Independent objective and derivative-support axes

The implementation has two independent switches. `include_attention_entropy` selects the canonical entropy-regularized belief objective or its entropy-suppressed surrogate; `gradient_mode` selects detached-key own-row filtering or live-key global smoothing. Adaptive self-coupling retains $\alpha_iD_i+R(\alpha_i)$ in both objectives, so the optimized-$\alpha_i$ envelope has no explicit $\partial\alpha_i/\partial q_i$ response. The singular family $\mathcal{N}(\mu_i,\epsilon I)$ does not have the previously stated finite adaptive-$\alpha_i$ limit: its full prior KL diverges and $\alpha_i^*=c_0/(b_0+D_i)\to0$. A finite mean-only comparison therefore holds covariance positive and $\alpha_i$ fixed, or explicitly defines a different mean-only gate.

For $\Sigma_i=\sigma^2I$, Fisher preconditioning cancels the explicit $\sigma^{-2}$ only in the alignment term. If the Euclidean gradient is $g=\lambda_p\delta+\sigma^{-2}A-L$, the natural step is $-\eta(\sigma^2\lambda_p\delta+A-\sigma^2L)$. No single redefinition $\widetilde{\eta}=\eta\sigma^2$ leaves every bracket coefficient unchanged. The deployed default omits $L$ because its belief revision is target-blind; the held-out next-token cross-entropy is optimized separately and supplies no shared-functional EM monotonicity guarantee.

### 11. The hard-attention response limit is nonuniform

The surrogate response $-\tau^{-1}\operatorname{Cov}_\beta(E,\partial E)$ vanishes for each fixed configuration with a unique positive energy gap as $\tau\to0$, at rate $O(e^{-\Delta/\tau}/\tau)$ for fixed gap $\Delta$. It does not vanish uniformly over configurations approaching a tie. For two keys with $E_1-E_2=c\tau$ and derivative contrast $d=\partial E_1-\partial E_2$, the response approaches
\[
-\frac{cd}{4\cosh^2(c/2)},
\]
which is generally finite and nonzero. Exact ties, fixed positive gaps, and temperature-scaled near-tie paths are distinct limits.

## 2026-07-10 empirical and architectural reconciliation

The audited optimizer path freezes frame revision inside the E-step with `e_phi_lr=0`, but it does not freeze the token-frame table during training. At each recorded source SHA, the committed optimizer gate combined with `m_phi_natural_grad=false` routes that table to ordinary AdamW at learning rate `0.015` with frame weight decay `0.05`. Because every provenance record has `git_dirty=true` and no dirty diff survives, the exact executed optimizer implementation cannot be independently reconstructed. The configured heavy-ball and momentum fields belong only to the disabled custom outer optimizer; BCH/retraction belongs only to the disabled in-E-step frame route; and the stored pullback field is inactive because both optional frame routes are off.

All 36 archived configurations set `prior_source=model_channel`, `s_e_step=true`, `e_s_mu_lr=0.85`, `e_s_sigma_lr=0.1`, `lambda_h=0.25`, `lambda_gamma=0.75`, `kappa_gamma=1`, `learnable_r=true`, and `r_update_mode=gradient`; every summary scaling point has `model_channel_active=true`. The retained sweep is therefore two-channel, not single-channel. Within each forward pass, one target-blind model refinement moves token-indexed $s_i$ toward a learned global, token-uniform $r$ and gamma-weighted model consensus using the shared fixed frame. The refined state supplies $q_i^{(0)}=p_i=s_i^{(1)}$ before one belief refinement. The outer cross-entropy differentiates through both unrolled paths. In `s_e_step` mode, the hyper-prior and gamma terms act inside the model refinement and are not separately added to the scored outer scalar, avoiding double counting. The active learned route includes the model tables, $r$, token and learned positional frame parameters (`pos_phi="learned"`), the linear output projection and bias (`decode_bias=true`), and the mixer where enabled. These are two same-scale refinements, not evidence for a slower model timescale or a realization of the full multiscale PIFB theory. The archived configurations plus the committed code at their source SHAs reconstruct this route, but the unavailable dirty diffs preclude byte-level proof of the executed code.

The width sweep also changes the post-belief architecture at its first endpoint. `use_head_mixer=false` at $K=10$ and true at every $K\geq20$. The identity-initialized $H\times H$ remap contributes $H^2$ parameters, occupies a $W_O$-like slot, and is not equivariant under the live untied $\mathrm{GL}(10)^H$ action. In the one-layer linear-decode path it is absorbable into the output projection as a function-class statement, but no matched mixer-off control isolates its optimization effect. The width trend therefore varies width, head count, mixer activation, seed, and at some widths source commit.

The zero-based causal row at position $i$ has support $\{0,\ldots,i\}$ and therefore uses the normalized uniform prior $\pi_{ij}=1/(i+1)$ on that support. The former $1/i$ display was singular at $i=0$ and inconsistent with the manuscript's own later indexing statement; it is corrected in this revision.

The retained cross-entropy offset fit uses raw trainable parameter count, weighted nonlinear least squares with per-width SEM residual scales, and a 2,000-replicate nested cluster bootstrap over widths and within-width records. It gives $\alpha=0.556$ with interval $[0.400,0.600]$, $A\approx9666$, $E=3.945$, and cross-entropy-space $R^2=0.9995$. Each run saw 491.52 million tokens while tokens per parameter fell from 64.66 to 5.42, so this is neither iso-compute nor compute-optimal scaling and its exponent is not comparable to compute-optimal data/model scaling exponents. Excluding the mismatched $K=90$, seed-6 record changes the fitted values only to $\alpha=0.55829$, $A\approx9963$, and $E=3.95065$.

## Results that survive

The ambient full-Gaussian KL and $f$-divergence invariance theorem survives for one common realized bijection applied to both arguments in one channel and dimension. The entropy-regularized row KKT calculation, its unique Gibbs weights, and the reduced $-\tau\log Z$ value survive. Gaussian Fisher natural gradients for belief means and covariances survive within the belief family. The differential-of-exponential formulas and $J^\top J$ calculations survive as local and extrinsic facts. The Gaussian score expansion, identity-bilinear shared-frame subcase, key-norm residual, fixed-pair bilinear reach, restricted whitened RoPE comparison, fixed-$\alpha_i$ positive-covariance mean comparison, exact termwise Fisher scaling, and fixed-gap hard-attention limit survive within their revised scopes. The fixed-witness forward-KL direction and overlap extension survive under the revised hypotheses.

## Claims superseded

The revision withdraws arbitrary nonidentity constant Regime-I transport as an origin for general QK, canonical-stationarity parity with the entropy-suppressed surrogate, global coverage of $\mathrm{GL}^+(K)$ by one real exponential chart, exact general-congruence closure of the diagonal family, full-$\mathrm{GL}(K)$ frame-natural-gradient interpretations, Regime-I values $y_2=-1$ and nonzero $g_3$, and unconditional forward-KL uniqueness based on pooled configuration ranges. It also withdraws extension of common-pushforward invariance across unequal realized maps, invariance of a complete fixed-readout objective, forced specialization or a phase transition from readout non-invariance alone, the labeling of $\operatorname{Var}_A(\mu)$ as emergent anisotropy, differentiation of $\sum_j\beta_{ij}C_{ij}(q_i^*(\beta_i))$ as the reduced value function, conflation of order-Rényi with Li-Turner or Amari constructions, pointwise $M_{ij}$ reach as function-class equivalence, unwhitened general-covariance RoPE, the finite adaptive-$\alpha_i$ Dirac limit, conflation of canonical/surrogate with filtering/smoothing, uniform disappearance of the hard-attention response near ties, any shared-functional EM interpretation of the deployed filter and cross-entropy update, the claim that the audited frame update used heavy-ball, the claim that the retained sweep is single-channel, and any interpretation of the width fit as a controlled mixer-free or compute-optimal scaling law. The former “review-exhausted,” “mathematically exhausted,” and submission-ready assessments remain withdrawn.

## Reproducibility and literature-positioning status

The current V3 implementation is public at `https://github.com/cdenn016/V3_Transformer`; this revision reviewed commit `e504f1c5ad5d277f653534cfc7fb63fd3b1bee61`. That commit is not a self-contained reproduction package for every historical result: it lacks the complete manuscript figure set, exact historical per-run configurations and seeds, complete raw metric series and test results, data/tokenizer/environment provenance manifests, and a one-command reproduction workflow. Historical artifacts recovered from a separate dirty legacy checkout are audit trail rather than a frozen public release.

The retained empirical result is the fixed-$\mathrm{GL}^+(10)$ WikiText-103 width sweep over twelve widths and three development records at $491{,}520{,}000$ tokens per run. All 36 provenance records mark dirty worktrees and the runs span ten source commits, with mixed-SHA cells, a K90/seed-6 overwrite mismatch, and a head mixer that is absent at $K=10$ but active at $K\geq20$; the curve is therefore a heterogeneous within-sweep development trend rather than a frozen benchmark, a pure seed experiment, or a transferable scaling law. The archived configurations and corresponding committed code reconstruct the same-scale $s\to q$ route, but the missing dirty diffs prevent exact reconstruction of the executed bytes. The former single-seed divergence-order and positional-extrapolation comparisons are not retained as empirical claims. The frozen-BERT material is retained only as a historical algebraic score comparison. Its $\tau=19$ choice and evaluation used the same 105 passages, observations are clustered by passage and head, and no current-package held-out or passage-aware reanalysis was available.

The novelty statement is narrowed against direct prior work in structured and variational attention, implicit structural inference, gauge-equivariant self-attention, energy-minimizing attention, and later unrolled-inference/free-energy interpretations. Sengupta and Friston already use geometric parallel transport of sufficient statistics. The remaining contribution claim is the specific combination of transported Gaussian posteriors, token-local frames, and a $\mathrm{GL}(K)$ entropy-regularized variational construction, together with the same-channel common-pushforward theorem and the implemented iterative diagonal-covariance model.

## Relevance to this research

This revision changes how the [[VFE Transformer Program]] connects [[GL(K) gauge-equivariant attention]], [[Attention Mechanism]], [[Renormalization-group flow of beliefs]], [[Holonomy]], [[Killing form]], [[Natural gradient]], and [[Probabilistic opinion pooling]]. It restricts invariance to same-channel common realized maps, separates a fixed readout from the invariant divergence sector, distinguishes order-Rényi from Li-Turner and Amari constructions, limits Fisher geometry to belief statistics, replaces pointwise bilinear equivalence by a restricted whitened RoPE comparison, separates the canonical/surrogate and filtering/smoothing axes, records the valid fixed-$\alpha_i$ mean comparison and termwise Fisher scaling, preserves the finite near-tie response, separates exact ambient theorems from the live diagonal and single-exponential realization, and moves nontrivial holonomy experiments to edge-relaxed Regime II.

## Related

[[gl-k-attention]] · [[VFE Transformer Program]] · [[GL(K) gauge-equivariant attention]] · [[GL(K) gauge group]] · [[Attention mechanisms — theory and positional structure]] · [[Gauge equivariance and geometric deep learning]] · [[Information geometry and natural gradient]] · [[SPD-manifold geometry and Riemannian optimization]] · [[participatory-it-from-bit]]
