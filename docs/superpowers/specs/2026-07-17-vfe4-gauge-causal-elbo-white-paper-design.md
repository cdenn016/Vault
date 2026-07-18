# VFE 4.0 Gauge-Causal ELBO White Paper Design

Date: 2026-07-17
Status: Approved by the author on 2026-07-17, including the natural-parameter extension
Branch: codex/vfe4-white-paper-20260717
Primary artifact: `manuscripts/VFE4_gauge_causal_elbo_whitepaper.tex`

## Objective

Write a publication-track technical white paper that specifies a gauge-covariant, structured latent-variable language model whose inference and parameter-learning operations are updates of one evidence lower bound. The paper will define the probabilistic model before introducing an inference algorithm, retain a normalized categorical observation likelihood, and state precisely which results are definitions, algebraic identities, propositions, implementation choices, or empirical hypotheses.

The paper will present VFE 4.0 as a new research architecture rather than as a toggle inside V3. The current V3 model remains the experimental baseline and engineering ancestor. Its live posterior-to-posterior consensus terms will not be relabeled as fixed generative factors. The configuration-space Gibbs construction will be discussed as a different probabilistic level, not as the state-level ELBO developed in the main text.

## Audience, Genre, and Contribution

The primary audience is researchers in probabilistic machine learning, variational inference, language modeling, geometric deep learning, and information geometry. The paper will be written as a self-contained theoretical white paper rather than as a report of completed VFE 4.0 experiments. It will use a readable executive summary but will retain equation-level definitions, derivations, proof sketches, claim-status labels, and a preregistered empirical program.

The intended one-sentence contribution is:

> We construct a normalized causal latent-variable language model on associated bundles whose structured state inference, model-channel inference, source selection, and categorical decoder learning optimize one evidence lower bound, and we state falsifiable conditions under which this architecture could improve language modeling.

The paper will not claim that a valid ELBO guarantees an exact posterior, monotone convergence under arbitrary truncated updates, improved perplexity, avoidance of posterior collapse, or scaling to a large language model. Those are separate questions with separate tests.

## Design Alternatives Considered

### Construction-first exact ELBO

This is the approved approach. The paper begins with a causal token graph, principal and associated bundles, normalized transition and emission kernels, a fixed generative joint, and a structured variational law. It derives the ELBO from those objects and only then maps its factors and coordinate updates to transformer-like operations. This order makes the exactness claim auditable and prevents current V3 loss terms from silently determining the generative story.

### V3-to-V4 repair narrative

This approach would begin with the current V3 functional and replace incompatible sectors one at a time. It is rejected as the main narrative because it invites a false impression that moving posterior-to-posterior KL terms are nearly ordinary generative transitions. A concise V3/V4 crosswalk will instead appear near the end of the paper.

### State/configuration dual theory

This approach would give equal weight to the state-level causal ELBO and the belief-configuration Gibbs lift. It is rejected as the main architecture because the two constructions have different random variables, entropy terms, and empirical meanings. The configuration lift will remain a clearly separated extension and comparison.

## Scope and Non-Scope

The exact core contains a causal token graph, continuous state and model latents, categorical source variables, deterministic geometric data, normalized Gaussian transition kernels, a normalized categorical token emission, and a structured variational posterior. The core supports both filtering and smoothing recognition families while keeping predictive evaluation strictly causal.

The first exact reference regime fixes each source to the immediate causal predecessor and uses linear-Gaussian transitions. Categorical source selection is added only after that regime is proved and numerically checked. Independent Regime II link variables, latent gauge frames, configuration-Gibbs priors, Bethe or Kikuchi approximations, two-hop terms, curvature energies, and backprop-free training are extensions. None will be inserted into the exact core without its own normalized factorization.

The paper is not an analysis of the 28-epoch baseline or its plateau. It may identify V3 as the baseline architecture and state which comparison arms are required, but it will not infer VFE 4.0 performance from existing V3 results.

## Claim Taxonomy

The manuscript will label claims using the following boundaries.

Definitions cover the causal token graph, principal and associated bundles, gauge-compatible transition kernel, source variables, structured recognition law, information-form Gaussian family, and exact VFE 4.0 objective.

Algebraic identities and lemmas cover normalization of the directed joint, the evidence decomposition, the conditional KL chain rule, Gaussian natural/moment coordinate conversion, gauge transformation laws, Gaussian factor assembly in information form, and equality of monolithic and decomposed ELBO evaluations.

Propositions cover gauge invariance under simultaneous pushforward, preservation of token-block precision sparsity under local gauge changes, Regime I flatness and identity loop holonomy, nonclosure of diagonal covariance under general GL(K), and the non-equivalence between V3 peer KL and a fixed VFE 4.0 transition.

Empirical hypotheses cover posterior-structure gains, coordinate-update efficiency, posterior collapse, calibration, predictive performance, emergent source selection, curvature benefits, and scaling. A statement that V3 is an exact limit of VFE 4.0 will remain a conjecture unless an explicit reduction is proved.

## Observations and Autoregressive Semantics

Training tokens are observations. For a sequence (x_{1:T}), the model assigns a normalized probability

$$
p_\theta(x_{1:T})
=
\prod_{t=1}^{T}p_\theta(x_t\mid x_{<t}).
$$

The latent predictive prior at position (t) may depend on previously generated tokens and latent states but not on (x_t). A training recognition law may condition on (x_t), or on the full observed sequence for smoothing, because it approximates the posterior after the observation has been supplied. Predictive evaluation and generation must integrate or sample from the causal prior and must never use the target-conditioned recognition law.

The observation factor is categorical:

$$
L_{\theta,t}(x_t=v\mid z_t,m_t)
=
\frac{\exp \ell_{t,v}(z_t,m_t)}
{\sum_{u=1}^{V}\exp \ell_{t,u}(z_t,m_t)}.
$$

Its negative expected log likelihood is expected cross-entropy. VFE 4.0 therefore supplements rather than removes cross-entropy. A Gaussian-template or other energy parameterization of the logits remains a categorical cross-entropy after vocabulary normalization.

## Geometric Base and Bundle Construction

Let

$$
D_T=(V_T,E_T),
\qquad
V_T=\{0,\ldots,T\},
\qquad
(j,t)\in E_T\Rightarrow j<t
$$

be a finite causal token graph. The working geometric realization carries the trivial principal bundle

$$
P=|D_T|\times G\longrightarrow |D_T|,
$$

where the initial exact path uses a declared matrix group (G). For (G=\mathrm{GL}(K)), the paper will distinguish the full group, its positive-determinant component, and any restricted block representation used by an implementation.

Representations (\rho_z:G\to\mathrm{GL}(V_z)) and (\rho_m:G\to\mathrm{GL}(V_m)) define associated state and model bundles

$$
E_z=P\times_{\rho_z}V_z,
\qquad
E_m=P\times_{\rho_m}V_m.
$$

The continuous latent path is a random section of the direct-sum bundle

$$
\mathbb E_T
=
\bigoplus_{t=0}^{T}(E_{z,t}\oplus E_{m,t}).
$$

Discrete transports (\Omega^z_{tj}:E_{z,j}\to E_{z,t}) and (\Omega^m_{tj}:E_{m,j}\to E_{m,t}) act on permitted causal edges. A model-to-state bundle morphism (B_t:E_{m,t}\to E_{z,t}) supplies the generative bridge missing from the current two-channel handoff.

Under local gauges (g_t), the fields and transports obey

$$
z_t'=\rho_z(g_t)z_t,
\qquad
m_t'=\rho_m(g_t)m_t,
$$

$$
\Omega_{tj}^{z\prime}
=
\rho_z(g_t)\Omega_{tj}^z\rho_z(g_j)^{-1},
\qquad
\Omega_{tj}^{m\prime}
=
\rho_m(g_t)\Omega_{tj}^m\rho_m(g_j)^{-1},
$$

and

$$
B_t'=\rho_z(g_t)B_t\rho_m(g_t)^{-1}.
$$

The paper will say explicitly that a finite token base is topologically trivial in the working construction. The geometry resides in frames, representations, links, and connection observables rather than in a claimed nontrivial bundle topology.

## Fixed Normalized Generative Joint

Let (a_t\in\operatorname{Pa}_z(t)) and (b_t\in\operatorname{Pa}_m(t)) be categorical source variables with fixed normalized priors (\pi_t^z) and (\pi_t^m). Let (\Gamma) collect frame and connection data. The proposed joint is

$$
\begin{aligned}
p_\theta(x,z,m,a,b,\Gamma)
={}&p_\theta(\Gamma)p_{\theta,0}(z_0,m_0\mid\Gamma)\\
&\times\prod_{t=1}^{T}
\pi_t^m(b_t)
K^m_{\theta,tb_t}(m_t\mid m_{b_t},x_{<t},\Gamma)\\
&\times\pi_t^z(a_t)
K^z_{\theta,ta_t}(z_t\mid z_{a_t},m_t,x_{<t},\Gamma)\\
&\times L_{\theta,t}(x_t\mid z_t,m_t,\Gamma).
\end{aligned}
$$

The exact initial implementation will treat (\Gamma) as a deterministic model parameter and condition the joint on it. A latent (\Gamma) is admitted only with a proper prior, an explicit variational law, its entropy contribution, and a treatment of noncompact gauge volume.

A minimal non-neural Gaussian path uses

$$
K^m_{\theta,tj}
=
\mathcal N(m_t;\Omega^m_{tj}m_j+c_t^m,R_t^m),
$$

$$
K^z_{\theta,tj}
=
\mathcal N(z_t;\Omega^z_{tj}z_j+B_tm_t+c_t^z,R_t^z).
$$

Every transition retains its quadratic, trace, determinant, and normalization terms. Its receiver covariance transforms by congruence. The conditional mean map, offset, covariance, and emission parameters must transform together.

The categorical emission must be gauge invariant. For linear logits, dual weights transform as

$$
W_t^{z\prime}=W_t^z\rho_z(g_t)^{-1},
\qquad
W_t^{m\prime}=W_t^m\rho_m(g_t)^{-1}.
$$

A fixed decoder that is exempted from this action reduces the gauge symmetry to its stabilizer. The paper will not call the full objective locally gauge invariant while leaving the observation channel fixed.

## Structured Variational Family

The general recognition law is normalized and may retain temporal, cross-channel, and source-assignment dependence:

$$
Q_\psi(z,m,a,b,\Gamma\mid x)
=
Q_\psi(\Gamma\mid x)
Q_{\psi,0}(z_0,m_0\mid x,\Gamma)
\prod_{t=1}^{T}Q_{\psi,t}(z_t,m_t,a_t,b_t\mid\mathcal H_t,x,\Gamma),
$$

where (\mathcal H_t) contains the preceding latent history. A filtering recognition family uses (x_{\le t}); a smoothing family may use (x_{1:T}). Both are distinct from the causal predictive prior.

The exact Gaussian reference family conditions on the discrete source assignments and uses one joint Gaussian over all continuous latents. Marginalizing source variables generally produces a Gaussian mixture. A single-Gaussian moment projection is an approximation and must be labeled as such.

Mean-field appears only as a nested control:

$$
Q_{\mathrm{MF}}(z,m\mid x)
=
\prod_t q_t^z(z_t\mid x)q_t^m(m_t\mid x).
$$

It is not the foundational assumption of VFE 4.0.

## Canonical Gaussian Coordinates

VFE 4.0 will use a dual-coordinate design. Let

$$
y=\operatorname{col}(z_0,m_0,\ldots,z_T,m_T)\in\mathbb R^D.
$$

Conditionally on source and geometric variables, the canonical posterior representation is the information form

$$
q(y)
=
\exp\left(
h^\top y-rac12y^\top Jy-A(h,J)
\right),
\qquad
J=J^\top\succ0,
$$

with

$$
A(h,J)
=
\frac12h^\top J^{-1}h
-\frac12\log\det J
+\frac D2\log(2\pi).
$$

The familiar moments are derived through linear solves:

$$
\Sigma=J^{-1},
\qquad
\mu=J^{-1}h,
\qquad
h=J\mu.
$$

For a correlated posterior, the token block satisfies

$$
h_t=\sum_sJ_{ts}\mu_s,
$$

so (h_t\) is not generally (J_{tt}\mu_t). Similarly, (J_{tt}\) is a conditional precision, while (\Sigma_{tt}^{-1}\) is the marginal precision.

The exponential-family natural parameters and sufficient statistics are

$$
\eta_1=h,
\qquad
\eta_2=-\frac12J,
\qquad
T_1(y)=y,
\qquad
T_2(y)=yy^\top.
$$

Their dual expectation coordinates are

$$
\tau_1=\mu,
\qquad
\tau_2=M=\mathbb E[yy^\top]=\Sigma+\mu\mu^\top.
$$

The paper will not call ((\mu,\Sigma)) the exact expectation-coordinate dual of ((h,J)). It will call ((\mu,\Sigma)) the moment view and ((\mu,M)) the expectation coordinates.

Natural parameters are selected as the canonical inference and message-passing representation because Gaussian factor products add information contributions and a Markov posterior has sparse block precision even when its covariance is dense. Moment coordinates remain the canonical interface for token emissions, Monte Carlo sampling, predictive summaries, calibration, and human interpretation.

The scalable path will never form (J^{-1}) as a dense matrix. It will use sparse or block-banded factorizations and linear solves to obtain (\mu), selected covariance blocks, samples, and log determinants. The paper will describe storage and solver choices as implementation requirements rather than as part of the ELBO theorem.

## Information-Form Gauge Laws and Closure

Let the stacked local gauge action be (y'=\mathsf G y). The joint Gaussian transforms as

$$
h'=\mathsf G^{-\top}h,
\qquad
J'=\mathsf G^{-\top}J\mathsf G^{-1},
$$

while its moments transform as

$$
\mu'=\mathsf G\mu,
\qquad
\Sigma'=\mathsf G\Sigma\mathsf G^\top.
$$

Each cross-token precision block therefore obeys

$$
J_{ts}'=G_t^{-\top}J_{ts}G_s^{-1}.
$$

Local block-diagonal gauge transformations preserve the zero pattern between token blocks. General GL(K) transformations do not preserve scalar-diagonal or within-token diagonal covariance. The theoretically pure GL(K) path must therefore retain full within-token blocks, use an explicitly closed representation class, or restrict the group. Natural parameters do not cure a family-closure failure.

The log partition and differential entropy acquire the same Jacobian shift under a coordinate change. Neither differential entropy nor log density is separately gauge invariant. The complete KL and ELBO are invariant when the generative and variational measures are pushed forward together.

## Gaussian Factor Assembly

For a linear-Gaussian factor

$$
y_t=A_{tj}y_j+b_t+\epsilon_t,
\qquad
\epsilon_t\sim\mathcal N(0,R_t),
$$

the joint information matrix receives

$$
\begin{aligned}
J_{tt}&\mathrel{+}=R_t^{-1},
&J_{tj}&\mathrel{+}=-R_t^{-1}A_{tj},\\
J_{jt}&\mathrel{+}=-A_{tj}^\top R_t^{-1},
&J_{jj}&\mathrel{+}=A_{tj}^\top R_t^{-1}A_{tj},
\end{aligned}
$$

and

$$
h_t\mathrel{+}=R_t^{-1}b_t,
\qquad
h_j\mathrel{+}=-A_{tj}^\top R_t^{-1}b_t.
$$

This additive assembly is the main computational reason to prefer information form. It also provides an analytic oracle for the first implementation phase.

The implementation must preserve (J\succ0). It may assemble (J) from normalized Gaussian factors or use a sparse Cholesky or LDL factorization. Unconstrained Euclidean updates to the entries of (J) are not an acceptable default. Damping between valid natural parameters is permitted when the resulting precision remains positive definite and the objective change is measured.

## Exact ELBO and Free Energy

Let (Y=(z,m,a,b,\Gamma)). The primary theorem is the standard but fully instantiated identity

$$
\log p_\theta(x)
=
\mathcal L(\theta,\psi)
+
D_{\mathrm{KL}}
\left(
Q_\psi(Y\mid x)
\middle\Vert
p_\theta(Y\mid x)
\right),
$$

where

$$
\mathcal L(\theta,\psi)
=
\mathbb E_{Q_\psi}
\left[
\log p_\theta(x,Y)-\log Q_\psi(Y\mid x)
\right].
$$

The VFE 4.0 loss is

$$
\mathcal F_4(\theta,\psi)=-\mathcal L(\theta,\psi).
$$

Under matched conditional factorizations, the ELBO decomposes into expected token log likelihood, initial-state complexity, source-assignment complexity, model-transition complexity, state-transition complexity, and geometric complexity when geometry is latent. The source-assignment terms are ordinary categorical KL divergences

$$
D_{\mathrm{KL}}(\gamma_t\Vert\pi_t^m),
\qquad
D_{\mathrm{KL}}(\beta_t\Vert\pi_t^z).
$$

Their coefficient is one in an ordinary ELBO. An arbitrary attention temperature requires a separately normalized tempered model or a generalized-Bayes interpretation; it cannot be inserted as an unexplained loss multiplier.

For the joint Gaussian posterior, the entropy is

$$
H(q)
=
\frac12
\left[
D(1+\log(2\pi))-\log\det J
\right].
$$

The complete joint log determinant must enter the ELBO. Replacing it with a sum of node entropies drops the total-correlation contribution and reintroduces a mean-field error.

The paper will provide both the monolithic log-ratio form and a decomposed implementation form, then require numerical equality between them on reference problems.

## Coordinate Updates and Natural Gradient

The E-direction updates (Q_\psi\) with (\theta) fixed. Its state, model, and source-coordinate updates must include the observation likelihood and every downstream factor that depends on the updated variable. A target-blind predictive state remains a prior object; it is not relabeled as an observation-conditioned posterior.

The M-direction updates (\theta) with (Q_\psi) fixed. This includes the categorical emission, transition parameters, source priors, and deterministic geometry. A categorical-softmax decoder generally lacks a closed-form M-step, so a gradient step that increases the same ELBO is generalized EM rather than exact coordinate maximization.

For exponential-family natural coordinates (\eta) and expectation coordinates (\tau), the Fisher duality is

$$
\widetilde\nabla_\eta\mathcal F
=
\nabla_\tau\mathcal F,
\qquad
\widetilde\nabla_\tau\mathcal F
=
\nabla_\eta\mathcal F.
$$

Ordinary SGD or Adam on ((h,J)) is not automatically a natural gradient. The paper will reserve that term for an explicitly Fisher-preconditioned or dual-coordinate update. A conjugate Gaussian information update may have a closed form; the categorical emission remains nonconjugate. Sampling, a declared site approximation, or a nested lower bound is still required for its expected likelihood when no analytic expectation exists.

Any quadratic bound on the softmax likelihood must be labeled as a second lower bound beneath the original ELBO. Laplace, expectation propagation, and Bethe or Kikuchi procedures are approximation layers, not identities of the exact core.

## Transformer and Language-Model Correspondence

The paper will map the VFE 4.0 factors to transformer operations only after the probabilistic derivation.

The categorical source posteriors (\beta_t) and (\gamma_t) are attention-like routing distributions. Their logits arise from a fixed source prior and expected conditional evidence, not from an unexplained softmax over moving posterior KL values. The state transition carries transported source content and the model-to-state contribution through (B_t). The model channel supplies a slower or more abstract latent process. The expected categorical emission produces the token prediction. Repeated updates of the structured posterior play the role of iterative inference depth.

This correspondence is structural. The paper will not claim algebraic equivalence to a standard dot-product transformer unless all required limiting assumptions are written and proved. It will also avoid calling the proposed system a large language model before it has been scaled and evaluated as one.

## Relation to V3

The crosswalk will make the following distinctions explicit.

V3 stores one Gaussian belief per token with within-token covariance. VFE 4.0 stores or represents one joint law with cross-token and cross-channel dependencies. An (N\times N) routing-energy array is not a cross-token covariance matrix.

V3 uses moving posterior-to-posterior KL terms as engineered consensus energies. VFE 4.0 uses fixed normalized transition kernels whose parameters do not depend on the variational posterior being optimized.

V3 performs target-blind model and belief refinement followed by a separate decoder cross-entropy update. VFE 4.0 distinguishes the causal predictive prior from the observation-conditioned posterior and evaluates all E-like and M-like updates against one ELBO.

V3's mean decoder is a point prediction. VFE 4.0 evaluates expected categorical log likelihood under the joint posterior, with a point estimate appearing only as a declared deterministic limit.

V3's Regime I vertex transport is a reusable flat geometric primitive. Its geometry, numerical SPD routines, causal masks, data windows, and selected decoder machinery may seed a future implementation. V3's `BeliefState`, pairwise free-energy scalar, E-step, and checkpoint schema are not treated as VFE 4.0 abstractions.

## Normalizability and Gauge-Volume Boundary

Every initial law, source prior, transition, emission, and geometric prior must be normalized. The generative joint must be independent of (Q_\psi). A valid information-form Gaussian requires (J\succ0), finite log determinant, and finite entropy.

There is no finite uniform Haar probability on noncompact GL(K). A latent-frame model therefore needs a proper quotient measure, gauge fixing with the appropriate Jacobian, a compact regulator, or a coercive proper prior on gauge-fixed physical directions. A Gaussian distribution on a Lie-algebra chart is not automatically a gauge-invariant distribution on the group and does not cover every component or every group element.

The initial exact path avoids this issue by treating frames and links as deterministic parameters. Regime I transport

$$
\Omega_{tj}=U_tU_j^{-1}
$$

is gauge covariant but flat, with identity loop holonomy. Nontrivial holonomy requires independent links and cycles in an underlying undirected graph or cell complex; a causal DAG has no directed causal loops.

## Hypotheses and Falsification Program

The paper will distinguish four questions: whether the ELBO identity is implemented correctly, whether a structured posterior improves approximation for a fixed model, whether the selected optimizer reaches the intended optimum, and whether learning the generative model improves prediction.

### H1: ELBO identity

For an analytically solvable linear-Gaussian chain,

$$
\log p_\theta(x)
=
\mathcal L(\theta,\psi)
+D_{\mathrm{KL}}(Q_\psi\Vert p_\theta(\cdot\mid x))
$$

must hold within a preregistered float32 tolerance. A residual above (10^{-3}) nats per window falsifies the first implementation.

### H2: Coordinate representation equivalence

Moment and information representations of the same Gaussian law must agree on log probability, entropy, KL, samples in distribution, and ELBO. Their ELBO difference at an identical distribution must remain below (10^{-4}). A difference is an implementation defect, not evidence that one coordinate system defines a better posterior family.

### H3: Correlations matter

For fixed generative parameters with a correlated exact posterior, the structured family must attain a tighter ELBO and recover lag correlations more accurately than its factorized subfamily. Two controls answer different questions. Holding the generative model fixed while constraining the variational cross-covariance tests posterior-family expressiveness. In an analytic synthetic model, setting transition coupling to zero while preserving the observation marginals and emission difficulty tests whether the structured advantage disappears when the exact posterior factorizes. Temporal shuffling of real language is not used as a decisive correlation control because it changes the prediction problem.

### H4: Information form improves computation, not the optimum

Information-form factor assembly and sparse solves should reduce memory or convergence cost relative to an equivalent moment implementation. When both reach stationarity in the same variational family, their optima must be statistically indistinguishable. Equal learning rates are not treated as a fair cross-coordinate comparison.

### H5: Shared-objective updates are coherent

Exact conjugate coordinate updates and valid majorize-minimize reference steps must not decrease the same ELBO beyond declared numerical tolerance. A deterministic generalized-EM proposal counts as an accepted update only when a line search or direct evaluation confirms that it increases the ELBO. No monotonicity claim will be made for unconstrained stochastic-gradient, Adam, or finite-step natural-gradient updates; those routes will be evaluated with confidence intervals and stationarity measures. Raw Euclidean coordinate-gradient norms will not be compared across parameterizations as if they shared a metric.

### H6: Posterior improvement reaches prediction

After fixed-model inference tests pass, matched end-to-end models will be evaluated from the causal prior. A tighter training posterior does not count as success unless held-out evidence estimates, prior-predictive negative log likelihood or perplexity, calibration, or another preregistered predictive measure improves.

### H7: Gauge covariance

After adding geometric transport, simultaneous transformation of latent variables, information parameters, transition factors, and decoder parameters must leave the complete joint log density up to its coordinate Jacobian and leave KL and ELBO values invariant. The proposed numerical residual threshold is (10^{-4}).

### H8: Sparse scaling

The promoted path must reach at least (T=128) and (K=20) without a dense (O((TK)^2)) covariance allocation. The initial suggested gates are no more than three times the factorized step time and two times its memory, subject to revision after the analytic prototype establishes a realistic baseline.

## Experimental Sequence and Promotion Gates

The first implementation should be a sealed sidecar probe that reuses only data and numerical utilities. It will compare an analytic linear-Gaussian positive control, a zero-coupling negative control, a factorized categorical language arm, and a structured categorical language arm for identical fixed generative parameters. It will then run matched end-to-end training only if the fixed-model comparison passes.

VFE 4.0 implementation promotion requires correct evidence and ELBO identities, correct natural/moment round trips, correlation-specific structured gains, target-leakage checks, predictive improvement across at least three seeds, observation-sensitive posterior covariance, gauge covariance after geometry is enabled, and demonstrated sparse feasibility. A suggested material bound-improvement gate is (0.02) nats per token with a 95 percent interval above zero. This threshold is a preregistration proposal, not a result.

If the Gaussian oracle passes but the categorical language arm shows no held-out benefit, the program stops before a full VFE 4.0 build. If structured inference improves only the training bound, the program does not claim a language-model gain. If any benefit disappears under compute matching or representation-equivalence controls, it is not attributed to posterior correlation.

## Paper Architecture

The manuscript will use the following dependency order:

1. Executive summary and claim-status table.
2. Language tokens as observations and the V3 objective mismatch.
3. Causal token graph and autoregressive semantics.
4. Principal bundle, associated bundles, and discrete connection.
5. Fixed normalized generative joint.
6. Structured posterior and source-variable factorization.
7. Natural, expectation, and moment coordinates for the joint Gaussian.
8. Exact ELBO derivation and conditional KL decomposition.
9. Gauge covariance and normalizability propositions.
10. E-like and M-like coordinate updates on the shared scalar.
11. Transformer correspondence and limiting cases.
12. Hypotheses, controls, stopping rules, and scaling gates.
13. V3/V4 crosswalk and configuration-Gibbs comparison.
14. Limitations and research program.
15. Technical appendices with derivations, sparse information-form identities, and verification oracles.

The abstract, introduction, discussion, and conclusion will be written as continuous prose. Tables will be used only where exact claim-status, V3/V4, or hypothesis mappings are clearer than prose.

## Planned Figures

The paper will contain at least four visual elements.

The graphical abstract will show observed tokens, causal predictive priors, observation-conditioned structured inference on associated bundles, shared ELBO updates, and prior-based generation.

The generative-factor graph will distinguish observed tokens, state latents, model latents, source variables, geometric data, and causal dependencies. It will visually separate the generative joint from the recognition law.

The bundle and information-geometry schematic will show the principal bundle, associated state and model fibers, cross-channel morphism, transported edges, and the dual coordinate views ((h,J)), ((\mu,M)), and ((\mu,\Sigma)).

The validation ladder will separate identity, posterior approximation, optimization, prediction, gauge covariance, and scaling. It will display explicit stop conditions rather than implying automatic promotion.

Each figure will be checked at final rendered size for legibility and will have a caption that states which arrows are probabilistic dependencies, inference dependencies, or coordinate transformations.

## Literature and Citation Plan

The paper will cite primary sources for variational EM and ELBO identities, exponential-family dual geometry and natural gradients, structured variational inference for sequential models, latent-variable language modeling and posterior collapse, gauge-equivariant geometric learning, transformer attention, and Gaussian graphical-model inference. Existing Research-vault sources and bibliography entries will be reused only after their metadata are checked against the primary publication or preprint.

No citation will be created from memory alone. Every bibliography key used by the new manuscript must resolve in `manuscripts/references.bib`, and every cited entry must be verified for author list, title, year, venue, and stable URL or DOI. The manuscript will distinguish results established by those sources from the proposed VFE 4.0 synthesis.

## Artifact and Formatting Design

The primary file will be `manuscripts/VFE4_gauge_causal_elbo_whitepaper.tex`. It will share `manuscripts/references.bib` and will not edit existing manuscript prose. White-paper styling will use a locally available report style only if it compiles reproducibly in the isolated worktree; otherwise the paper will use a self-contained standard LaTeX preamble matching the current manuscript toolchain. Formatting will not be allowed to block the mathematical artifact.

The source will use American English, punctuated display equations, and consistent notation. It will not use banned LaTeX spacing macros or the project’s banned stock phrases. The final document will contain no placeholder citations, `TBD`, `TODO`, or unsupported empirical result.

The task will update the dated Research edit record or create the repository’s expected dated post-edit record if none exists for 2026-07-17. It will not write new wiki synthesis or immutable source notes without a separate author confirmation.

## Verification Design

The manuscript must compile from a clean isolated build directory. References, equation labels, figure labels, and internal links must resolve. The log will be scanned for undefined citations, undefined references, multiply defined labels, overfull boxes that damage readability, missing glyphs, and fatal warnings.

The rendered PDF will be inspected page by page, with special attention to the graphical abstract, factor graph, long equations, tables, and bibliography. Mathematical checks will compare the joint and decomposed ELBO expressions, verify sign conventions, verify Gaussian log-partition and entropy constants, verify gauge transformation types, and ensure every theorem states its assumptions.

The Research wiki lint will run only if wiki or root navigation files are changed. Manuscript-only work will use LaTeX build and source checks rather than treating wiki lint as evidence for mathematical correctness.

## Acceptance Criteria

The design is satisfied when the white paper provides one fixed normalized joint, one normalized structured posterior, one authoritative ELBO, a precise natural-parameter construction, a valid moment interface, gauge-compatible transition and emission laws, a complete claim taxonomy, and falsifiable language-model hypotheses.

The paper must state plainly that cross-entropy remains the normalized observation term; V3 peer KL is not promoted to a fixed generative transition; mean-field is a control rather than an assumption; natural coordinates do not make Adam a natural gradient; diagonal Gaussian families are not closed under general GL(K); and exact ELBO identity does not imply predictive success.

The drafting task is complete only after the manuscript and figures compile, citations are verified, required edit documentation is updated, the intended diff is committed and pushed, the task branch is merged to `main`, `origin/main` is confirmed at the merge result, and the dirty live Research checkout is left untouched unless a safe fast-forward can be proved not to overwrite its WIP.
