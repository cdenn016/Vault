---
type: concept
title: Natural gradient
aliases:
  - Natural gradient descent
  - Fisher-preconditioned gradient
  - NGD
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-10-08
---

# Natural gradient

## Definition

The **natural gradient** is the direction of steepest descent of a loss function when the parameter space is treated not as flat Euclidean space but as a Riemannian manifold whose metric is the [[Fisher information metric]]. Concretely, for a loss $L(\theta)$ over parameters $\theta$ that index a family of probability distributions $p_\theta$, the ordinary (Euclidean) gradient $\nabla L$ answers "which way increases $L$ fastest per unit change in the *coordinates* $\theta$" — an answer that depends on how the model happens to be parameterized. The natural gradient instead measures distance in *distribution space* using the Fisher metric $F(\theta)$, and the steepest-descent direction becomes

$$\tilde\nabla L(\theta) = F(\theta)^{-1}\nabla L(\theta).$$

The defining property, established by [[amari-1998-natural-gradient]], is that
the natural-gradient tangent vector is coordinate invariant: a smooth change of
coordinates transforms $F$ and $\nabla L$ in compensating ways. An exact flow
therefore describes the same distribution-space direction. A finite Euler step
is not automatically invariant, because its result also depends on step size
and the chosen integration or retraction map.

## Why it matters here

[[multiagentelbo-2026-10-08-discarded-mean-stationary-bound]] reconstructs the complete receiver/sender matter quadratic at four actual old field states and checks its natural mean force and centered lift. Under $C\succeq\ell J_0^{-1}$, exact discarded energy is at most $\ell^{-2}$ times mean Fisher dissipation, yielding stopped zero-temperature integral control. Saved positive-temperature residuals increase slightly; this diagnostic excludes moving-map/covariance/source/generator noise and the full parent field. Population transfer also pays same-state Fisher-norm rule and computed-input errors.

[[multiagentelbo-2026-10-08-preparation-paths-moment-trajectory]] records four order-9 common-old-state Fisher fields and positive proposals on the unchanged archived Brownian path, reaching additional inference time $10^{-4}$. Independent saved-only replay passes 445 comparisons, with 32 selected generator tangent checks rather than full generator-gradient reconstruction. Finite coupled endpoint forecast comparisons do not bound population field error or trajectory convergence. Stationary native local path limits still require unresolved dense generator resolvent range for full-past Markov identification. PR207 also independently replays both complete finite forecast banks and static two-depth original-record/parent joints; retained/filter updates and original-flow feedback remain open. Computed arithmetic, arbitrary R0 starts and posterior accuracy remain separate.

[[multiagentelbo-2026-10-08-blockwise-budget-stationary-process]] refines the unchanged four-step exact quadrature/Cholesky scheme's future forecast and first-grid exit budgets, retaining all upstream sender/source errors and actual powers of the step. Conditional expected original joint forecast KL is at most $9.179\times10^{-6}$ nats per receiver on common survival. A closed infinite local gradient form also realizes the original population Fisher SDE as a conservative reversible stationary diffusion for admitted snapshot starts. Computed arithmetic, M16/posterior accuracy and arbitrary nonstationary R0 starts remain separate.

[[multiagentelbo-2026-10-08-recognition-spatial-source-moment]] gives the exact conditional Euclidean tangent second moment of the existing centered source softmax correction. Its sharp four-choice outer-box coefficient is 0.0111, replacing only the loose source term $32/3$; matter/generator covariance corrections and higher remainders remain separate. Thirty-seven polynomial identities ground the algebra. The accompanying spatial recognition theorem retains Gaussian Fisher volume and full covariance/source interiors, but supplies neither dynamical convergence nor a complete numerical path certificate.

[[multiagentelbo-2026-10-08-saved-forecast-local-exit]] supplies population Fisher coefficient ceilings for the fixed N512 sparse model, retaining all sender/source contributions and the actual Cholesky noise. A constraint-specific continuous native-exit bound is at most 0.038196 over inference time $10^{-4}$, conditional on the declared exact reference initial state and boxes. The direct four-step sufficient numerical exit/forecast budget fails; this does not establish inaccurate dynamics. M16/population discrepancy, function arithmetic and native-posterior accuracy remain separate.

[[multiagentelbo-2026-10-08-product-moment-fisher]] executes the opt-in product-Gaussian quadrature field with full covariance/precision Fisher derivatives and receiver, sender and supported-source contributions at one old state, distinct from joint-row M16. Six tiny Cartesian checks and 190 N512 saved-only comparisons pass; 24 generator tangents are checked, not the complete generator gradient. C1 integration plus rational actual-rule bounds give a scoped drift component, excluding Cholesky/exponential/autograd/accumulation arithmetic. Under uniform dependency row and column bounds, stopped mean-square error per block is C_H(h+q_n^2); global exits remain size-dependent. No population path, invariant law or RG gate is certified.

[[multiagentelbo-2026-10-08-fisher-trajectory-admission]] reaches the opt-in Gaussian/source Fisher retraction on N512 with the same old-state finite-quadrature field for every block. Seven coupled proposals and their complete moving-probe readouts pass independent saved-array reconstruction. Its stopped-grid mean-square bound uses the actual Cholesky driving noise and separates integration error from uniform empirical/population drift error, native exits and floating-point failures. A different noise square root can preserve the generator while changing the named-path coupling; neither this one path nor the generic net bound certifies the retained sixteen-draw population field or invariant sampling.

In MultiAgentELBO, [[multiagentelbo-2026-10-08-native-flow-handoff-fisher-step]] supplies an opt-in proposal for the already-declared full product-Fisher recognition thermostat. Its positive covariance retraction includes the joint mean/covariance Itô correction, and supported-source softmax noise supplies the declared inward drift through curvature. Seven tiny coefficient/layout checks pass. Its zero-temperature tangent matches common-state descent; finite steps differ from BLR, and local consistency does not establish trajectory convergence or exact invariant sampling. Population/quadrature direction noise and trajectory Brownian inputs remain distinct.

Natural-gradient claims apply to the Gaussian belief mean/covariance updates, whose statistical family has a Fisher metric. At each recorded source SHA, the committed gate and stored configuration route the audited frame table through AdamW on the outer objective; dirty provenance prevents byte-level reconstruction. Heavy-ball belongs only to the disabled custom outer frame optimizer, BCH/retraction only to disabled in-E-step revision, and the optional Cartan/Killing or exponential-pullback conditioner would not thereby be Fisher, reparameterization invariant, or gauge invariant if enabled.

These invariance and efficiency properties hold when the actual Fisher metric of a statistical family is used. They support belief-side updates, not a frame update identified only by analogy.

## Details

For a model $p_\theta(x)$, the Fisher information matrix is the expected outer product of the score, $F(\theta) = \mathbb{E}_{p_\theta}\big[\nabla_\theta \log p_\theta \nabla_\theta \log p_\theta^{\top}\big]$, and it is the unique (up to scale) metric on the manifold of distributions invariant under sufficient statistics — the foundational result of [[Fisher information metric]] and the broader apparatus catalogued in [[amari-2000-methods-information-geometry]]. The natural gradient $F^{-1}\nabla L$ is then the Riemannian gradient under this metric.

Several complementary readings of the same object guide the implementation:

- **Second-order view.** [[martens-2020-natural-gradient-insights]] relates the
  Fisher matrix to the Generalized Gauss–Newton matrix under specified
  model-output and loss conditions. Those conditions are general background;
  they have not been established for the frame objective or its conditioner.
- **Tractability via factorization.** The full Fisher matrix is $O(d^2)$ to form
  and $O(d^3)$ to invert. [[martens-2015-kfac]] makes neural-network natural
  gradients tractable by a Kronecker factorization. The transformer's
  block structure does not by itself identify its frame conditioner as K-FAC
  or as an approximation to any frame Fisher matrix.
- **Metric families for nets.** [[ollivier-2015-riemannian-metrics-nn]] derives a spectrum of Fisher-based, reparameterization-invariant training metrics for feedforward networks — full, backpropagated, unitwise, and quasi-diagonal — clarifying how much of the metric one must retain to keep invariance while staying cheap, and supplying the information-geometric counterpart to the model's block-structured updates.
- **Manifold connection.** Natural-gradient steps are Riemannian optimization
  on a statistical manifold. [[absil-2008-optimization-matrix-manifolds]] and
  [[boumal-2023-optimization-smooth-manifolds]] provide general retraction and
  transport machinery, while [[bonnabel-2013-riemannian-sgd]] gives convergence
  under its stated stochastic assumptions. Those results do not automatically
  grant convergence to the deployed finite-step covariance update or to the
  separate plain-AdamW gauge-frame update.

A divergence can induce a local Fisher metric without transferring all of its
global geometry. The configured `renyi` family is an order-$\alpha$ pairwise
discrepancy studied in [[vanerven-2014-renyi-kl]]. The Li–Turner variational
Rényi bound and Amari's alpha-divergences with their alpha-connections are
distinct constructions. A nonlinear monotone relation between divergence
values does not preserve gradients, Hessians, or affine connections, and a
smooth order-Rényi member recovers Fisher locally only up to an order-dependent
positive scale.

> [!note] Editorial (2026-07-10): The joint Gaussian belief update uses Fisher
> geometry; its covariance block is one-half conventional AIRM. The architecture
> also uses a configurable order-Rényi pairwise discrepancy.
> It does not sweep Amari alpha-connections, and the audited frame table remains
> on plain AdamW.

## In this work

Natural gradient surfaces wherever the VFE transformer optimizes a distribution:

- **Frame M-step.** The committed gate at each recorded SHA routes the frame table through AdamW, subject to the dirty-provenance caveat. Optional per-block conditioning and heavy-ball are inactive fields, not an identified Fisher/K-FAC natural gradient; the BCH retraction dispatcher is a separate optional in-E-step route.
- **Opt-in frame pullback group descent.** The rebuilt 2026-07-18 route is a stateless
  exponential-coordinate Frobenius-pullback solve followed by a right group update. Its first
  retained K=10 run was numerically healthy but optimized outer cross-entropy slowly: validation
  PPL fell from 456.32 at step 1,500 to 365.57 at step 9,000, while the pulled-back direction stayed
  0.991 cosine-aligned with the raw covector, the median generalized condition number stayed near
  1.90, and no trust/backtracking reduction activated. This is evidence about an extrinsic frame
  optimizer, not a Fisher natural gradient. The exact K=10 AdamW gap is not reconstructable from
  the retained artifacts, and the registered pullback learning-rate sweep remains incomplete.
- **E-step / online belief updates.** The per-token Gaussian beliefs $(\mu,\Sigma)$ are refined with the belief-family Fisher geometry. [[khan-rue-2023-bayesian-learning-rule]] supplies a related exponential-family natural-parameter update, but it does not identify the entire program or its separate decode/frame M-steps with one Bayesian learning rule. Adaptive-optimizer cautions must therefore be assessed per optimizer rather than transferred from the belief update to every channel.
- **SPD covariance geometry.** The covariance $\Sigma$ lives on the SPD
  manifold under the `spd_affine` retraction. For a zero-mean Gaussian, the
  covariance block of the Fisher metric is one-half the conventional AIRM; the
  constant factor changes gradient scale but not the underlying geodesic paths.
  This covariance-only statement must not be extended to the full joint
  mean-covariance manifold or to gauge frames. Spectral differentiation and its
  repeated-eigenvalue hazards are treated in
  [[ionescu-2015-matrix-backpropagation]], and the SPD cone as a symmetric space
  is developed in [[Symmetric spaces and the SPD cone]].
- **Invariance as a design principle.** The exact natural-gradient vector field
  is coordinate invariant on a specified statistical manifold. Finite discrete
  trajectories also depend on step size and the chosen integration or retraction
  scheme. This statistical-coordinate statement is an analogy to gauge
  invariance, not a proof of the model's gauge equivariance.

The operative natural-gradient claim in the reference configuration is the Gaussian belief update, not per-block Fisher preconditioning of the frame M-step.

## Constrained ELBO geometry

An equality of scalar ELBO and KL objectives does not automatically imply equality of their
natural-gradient vector fields after restriction to a model family. [[ay-2025-natural-gradient-elbo]]
separates the ambient joint-distribution statement from the constrained-model statement and gives
a cylindrical-model condition under which the ELBO and target-KL natural gradients remain
compatible under marginalization. A structured, coarse, quotient, or gauge-constrained recognition
family must verify the corresponding tangent compatibility; cylindricity is not automatic.

[[lukashchuk-2025-quotient-bayesian-learning]] supplies a complementary quotient construction for
specified marginal families. It is a comparator for [[Quotient Bayesian learning]], not a proof
that the project's noncompact passive-frame quotient is regular or that its deployed update is the
quotient natural gradient.

## Parameter symmetries and optimizer drift (2026-09-23)

Continuous symmetries of a loss yield conservation laws of gradient flow ([[kunin-2021-neural-mechanics]], Theorem 1). For the rescaling symmetry of two consecutive linear layers the conserved quantity is $W^{(h)}W^{(h)\top}-W^{(h+1)\top}W^{(h+1)}$ ([[du-2018-balanced-layers]], Theorem 2.2). Weight decay, momentum, stochasticity, and finite learning rates break these laws, and an adaptive optimizer does not follow the gradient flow at all. The v2 revision of the GL(K) attention manuscript uses this to read its conditioning diagnostics. The comparison maps have a cogredient $\mathrm{GL}(r_h)$ redundancy, so gradient flow would conserve $S_QS_Q^\top+S_KS_K^\top$, whereas AdamW without weight decay drifted along the orbit in the reported run and made raw condition numbers depend on the basis. In the same run, AdamW's decoupled weight decay ([[loshchilov-hutter-2019-adamw]]) acting on the stored log-variances drove the variances from 15 to about 1.045.

## Frame tables and receiver updates (2026-09-28 and 2026-10-02)

Two later notes give the program natural gradients with a stated statistical model. For the stored frame tables, [[dennis-2026-phi-natgrad]] takes the Fisher information of the reference prior $\mathcal N(U^{-1}\mu_v,U^{-1}\Sigma_vU^{-\top})$ with respect to the frame; its kernel is the stabilizer algebra of that Gaussian, so a covariant completion must be chosen, and the existing Frobenius-pullback step turns out to be projected Euclidean descent on $U$ rather than a Fisher step. For the receiver of the gradient attention route, [[dennis-2026-projected-gradient]] uses the exact natural-parameter solution of the Gaussian Fisher flow of a quadratic energy, $J^+=(1-\rho)J+\rho\Lambda/\kappa$, which avoids the step-size bound $\varepsilon<2/\kappa$ of the explicit Fisher step; see [[Projected gradient attention]]. Neither has been shown to train better than the alternatives.

## Fisher metric of a link and the singular boundary (2026-10-02)

[[dennis-2026-link-curvature]] pulls the Fisher-Rao metric back through the action $N(\mu,\Sigma)\mapsto N(g\mu,g\Sigma g^\top)$ of a group element: for $\delta g=Ag$ and output Cholesky factor $L'$, $ds^2=\|Z\eta\|^2+2\|\mathrm{sym}Z\|_F^2$ with $Z=L'^{-1}AL'$ and $\eta=L'^{-1}\mu'$, the same metric as in [[dennis-2026-phi-natgrad]] but for a link acting on a source belief. In the exponential chart $A=\frac{e^{\mathrm{ad}_X}-1}{\mathrm{ad}_X}\delta X$. Along $g_t=\mathrm{diag}(e^{-t},1,\dots,1)$ the divergence is $\mathrm{KL}(q_t\|q_0)\sim t=-\log\sigma_{\min}$ and the Fisher-Rao distance is at least $\sqrt2\,t$, so the singular boundary of $\mathrm{GL}(K)$ is at infinite Fisher distance, while in the affine chart with Euclidean metric it is at finite distance $\sigma_{\min}$. An additive update $M\leftarrow M-\eta\Delta$ can cross $\det=0$ in one step when $\eta\|\Delta\|_2\ge\sigma_{\min}(M)$ with $\Delta$ aligned to the smallest singular direction; a multiplicative update $g\leftarrow e^{-\eta A}g$ cannot, since $\det(e^{-\eta A}g)=e^{-\eta\,\mathrm{tr}A}\det g\neq0$. The loss does not diverge there (covariance floors), so the barrier is a property of the update geometry. The note compares with the finished run 54.73 (content learning rate $2.5\times10^{-3}$, AdamW, $\sigma_{\min}$ of the stacked operator $10^{-5}$ to $4\times10^{-3}$) as an order-of-magnitude estimate only, not a measurement of crossings, and states that the link actually applied in that run ($I+M$) stayed far from the boundary. Multiplicative, Fisher-preconditioned updates for the content maps are suggested and not implemented or tested.

## Latent links and the link Fisher (2026-10-03)

When the link generators are latent variables of the free energy ([[dennis-2026-dynamic-links]]), their inference dynamics are a natural-gradient relaxation. For point-mass links the preconditioner is the Fisher information of the transported Gaussian with respect to the generator, $\mathcal I[E,E']=\beta\operatorname{tr}(\bar Q^{-1}L(X,E)S_jL(X,E')^\top)$, with $L$ the Fréchet derivative of the exponential and $S_j$ the source second moment; it is the Gauss–Newton matrix of the transport term and the mean part of the link Fisher pullback above. For Gaussian link posteriors the natural-gradient updates are those of the Bayesian learning rule ([[khan-rue-2023-bayesian-learning-rule]]). These dynamics are first order, with the Fisher information acting as friction; the note obtains inertia only for the maximum a posteriori path over depth, with Euclidean sign (see [[Mass as Fisher information]]).

In the multi-agent theory, [[multiagentelbo-2026-10-04-lie-algebra-links]] proves the general statement (`prop:link-recognition-flow`): the natural-gradient flow of a Gaussian recognition law of the generators has an explicit Euler step that is the Gaussian Bayesian learning rule of [[khan-rue-2023-bayesian-learning-rule]], Eqs. (12) and (37). The flow is first order. Inertia appears only for the most probable history across learning episodes, as a discrete Newton equation of Euclidean sign.

## Sources

- [[dennis-2026-phi-natgrad]] — belief-Fisher natural gradient for the frame tables; the pullback step as projected Euclidean descent.
- [[dennis-2026-link-curvature]] — Fisher metric of a group-element link; infinite Fisher distance to the singular boundary; additive versus multiplicative updates (float64 checks, nothing trained).
- [[dennis-2026-dynamic-links]] — Fisher preconditioning of latent link generators; first-order inference dynamics; Bayesian-learning-rule updates for Gaussian link posteriors.
- [[dennis-2026-projected-gradient]] — exact Fisher flow and closed-form receiver updates on the gradient attention route.
- [[amari-1998-natural-gradient]] — the natural gradient as Fisher-preconditioned steepest descent; reparameterization invariance and Fisher efficiency.
- [[amari-2000-methods-information-geometry]] — Fisher metric and Amari alpha-connections; order-Rényi divergence is a distinct family.
- [[martens-2020-natural-gradient-insights]] — natural gradient as a Gauss–Newton-related curvature method under matching output/loss conditions; damping.
- [[martens-2015-kfac]] — Kronecker-factored Fisher approximation as general background; no frame-Fisher identification is asserted here.
- [[ollivier-2015-riemannian-metrics-nn]] — families of Fisher-based, invariant metrics for neural networks.
- [[absil-2008-optimization-matrix-manifolds]] — retractions and vector transports for the Riemannian realization of natural-gradient steps.
- [[bonnabel-2013-riemannian-sgd]] — convergence of stochastic Riemannian descent.
- [[li-turner-2016-renyi-vi]], [[vanerven-2014-renyi-kl]] — respectively the variational Rényi bound and order-Rényi divergence; both recover KL-related limits but are not interchangeable.
- [[sra-hosseini-2015-conic-geometric-optimization]] — conic geometric optimization on the SPD cone as a symmetric space; geodesic convexity and affine-invariant descent.
- [[nielsen-2020-elementary-introduction-information-geometry]] — pedagogical grounding for KL geometry and Gaussian belief natural gradients.
- [[martens-2010-hessian-free-optimization]] — truncated-Newton background; no audited frame-Fisher M-step is inferred.

- [[ay-2025-natural-gradient-elbo]] — the ambient/constrained distinction and a sufficient
- [[multiagentelbo-2026-10-04-lie-algebra-links]] — natural-gradient recognition flow of latent link generators; Euler step equals the Gaussian Bayesian learning rule.
  cylindrical-model condition for ELBO/target-KL natural-gradient compatibility.
- [[lukashchuk-2025-quotient-bayesian-learning]] — a quotient Bayesian learning rule for declared
  marginal families, with scope distinct from the project's passive-frame quotient.
- [[kunin-2021-neural-mechanics]] — symmetry-induced conservation laws of gradient flow and their breaking by weight decay, momentum, stochasticity, and discretization.
- [[du-2018-balanced-layers]] — gradient flow preserves the balance of consecutive layers in homogeneous networks.

## See also

- [[Fisher information metric]]
- [[Variational EM]]
- [[Variational free energy]]
- [[Renyi divergence]]
- [[Alpha-divergence]]
- [[Precision weighting]]
- [[Prediction error]]
- [[Gauge transformation]]
- [[Information geometry and natural gradient]]
- [[SPD-manifold geometry and Riemannian optimization]]
- [[Physics from Fisher information]]
- [[Symmetric spaces and the SPD cone]]

## Related sources (ingested 2026-06-20)

- [[kingma-ba-2015-adam]] — Adaptive first-order optimizer;
- [[loshchilov-hutter-2019-adamw]] — Decoupled weight decay;
- [[yang-2022-tensor-programs-v-mup]] — muP (maximal-update parametrization): width-stable init and learning-rate scaling, bearing on whether $\phi$/$\sigma$ init and $\kappa$ in $\tau=\kappa\sqrt{\dim_h}$ transfer across the K-sweep;
