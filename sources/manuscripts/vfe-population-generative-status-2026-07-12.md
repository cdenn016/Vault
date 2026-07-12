---
type: manuscript
title: "Population VFE Generative-Model Status and Two-Hop Theory Record"
aliases:
  - "Population VFE generative-model theorem record"
  - "V3 two-hop theory record"
authors:
  - Robert C. Dennis
year: 2026
status: in preparation
tags:
  - cluster/vfe
  - cluster/multi-agent
  - cluster/attention
  - cluster/gauge-theory
  - project/multi-agent
  - project/transformer
  - field/mathematics
  - field/statistics
  - field/cs-ml
created: 2026-07-12
updated: 2026-07-12
---

# Population VFE Generative-Model Status and Two-Hop Theory Record

## Scope and provenance

This immutable record banks the July 12, 2026 derivation added to the current `manuscripts/PIFB2.tex` working manuscript and its synchronized `V3_Transformer/Manuscripts-Theory/PIFB2.tex` mirror. The starting manuscript SHA-256 was `9D7415330A98D68B6331A9F4F5175040182D992E1A7E6AA88716B2D711E2A0CE`. The edited authoritative LF serialization has SHA-256 `AE19E7DAB5C41E66C951203B1E1FEA11FBAFCC911A00B7E10391099E5F8D2C59` and Research Git blob `ff0e41c7f40d955205e5a99da2422cb11a61829f`. The V3 mirror is line-for-line identical after end-of-line normalization and retains the repository's existing CRLF serialization pattern as Git blob `3efc1034bb9f459fd1bb03495bb350b2a7b731db`, avoiding an unrelated whole-file line-ending rewrite. The V3 investigation was based on `origin/main` commit `25eb817`. The existing immutable source note [[participatory-it-from-bit]] was not rewritten.

The result separates three claims that had previously been compressed into one question: whether the consensus functional is the mean-field ELBO of one fixed joint on the original state latents, whether a fixed auxiliary model can be obtained after equilibrium selection, and whether the functional defines an energy-based probability law on the larger space of belief configurations.

## Fixed state-level mean-field obstruction

Let $Q_q=\bigotimes_iq_i$ range over an open product family of positive state densities. For any fixed normalized joint density $p_\theta$, independent of $q$,

$$
D_{\mathrm{KL}}(Q_q\Vert p_\theta)
=\sum_i\int q_i\log q_i d\nu_i
-\int\left(\prod_iq_i\right)\log p_\theta d\nu_{1:N}.
$$

The entropy is separable and the fixed-model energy is affine in each individual factor. Therefore, for distinct $i$ and $j$,

$$
D^3_{q_iq_jq_j}
D_{\mathrm{KL}}(Q_q\Vert p_\theta)[a_i,h_j,h_j]=0
$$

for admissible zero-mass perturbations $a_i$ and $h_j$. This is the structural signature of an ordinary fixed-model mean-field ELBO [[wainwright-2008-graphical-models-variational]].

For one active transported consensus edge,

$$
C_{ij}(q)=\beta_{ij}D_{\mathrm{KL}}(q_i\Vert T_{ij}q_j),
$$

with fixed positive $\beta_{ij}$ and fixed positive mass-preserving transport $T_{ij}$, use $q_i(s)=q_i+s a_i$ and $q_j(t)=q_j+t h_j$. Direct differentiation gives

$$
\left.
\frac{\partial^3 C_{ij}}{\partial s\partial t^2}
\right|_{s=t=0}
=\beta_{ij}\int a_i
\left(\frac{T_{ij}h_j}{T_{ij}q_j}\right)^2d\nu_i.
$$

If $g_{ij}=(T_{ij}h_j/T_{ij}q_j)^2$ is bounded and nonconstant under $q_i$, the admissible choice $a_i=q_i(g_{ij}-\mathbb E_{q_i}[g_{ij}])$ makes the derivative

$$
\beta_{ij}\mathrm{Var}_{q_i}(g_{ij})>0.
$$

For several positive heads on the same ordered pair, replace $g_{ij}$ by their weighted sum

$$
G_{ij}=\sum_h\beta_{ij}^{(h)}
\left(\frac{T_{ij}^{(h)}h_j}{T_{ij}^{(h)}q_j}\right)^2
$$

and choose $a_i=q_i(G_{ij}-\mathbb E_{q_i}[G_{ij}])$; the complete same-pair variation is $\mathrm{Var}_{q_i}(G_{ij})>0$ when $G_{ij}$ is nonconstant. Unrelated edges omit one varied factor, the reverse edge is affine in the repeated sender variation outside its factor-separable entropy, and the theorem assumes the remaining terms have zero $q_i,q_j,q_j$ variation. They cannot cancel the obstruction.

Thus the coupled consensus functional is not, in general, $D_{\mathrm{KL}}(\bigotimes_iq_i\Vert p_\theta)+c$ for one $q$-independent joint density on the original agent-state product space. The theorem applies to the entropy-retaining construction while attention rows are treated as independent variational coordinates and held fixed during the state variation. Substituting the state-dependent optimum $\beta^\ast(q)$ produces a different reduced functional that requires its own representation test.

The quantifiers matter. The obstruction does not exclude zero coupling, fixed source templates, degenerate restricted families, compatible auxiliary variables, a joint selected after equilibrium, or a probability law whose random variable is an entire belief configuration.

## Exact and conditional constructions

### Zero-within-scale Gaussian hierarchy

At raw within-scale coupling $\widetilde\beta=\widetilde\gamma=0$, the PIFB2 cross-scale construction is already a proper hierarchical Gaussian generative model. Finite-variance parent-child links give a block-sparse quadratic negative log joint. The link quadratic is positive semidefinite, and its kernel is the consistent-transport subspace. A full-rank Gaussian prior at the top scale removes that kernel, so the stacked precision is symmetric positive definite. The mean-field coordinate equations are Gauss-Seidel sweeps on the resulting SPD system and converge to the unique optimum. This is an exact state-level ELBO exception because the within-scale belief-against-belief denominators are absent.

### Equilibrium-frozen auxiliary source model

On a finite latent alphabet, take strictly positive $p_i$, strictly positive normalized rows $\pi_i$, fixed coefficients $a_i>0$, $\lambda>0$, and $\tau>0$, and stochastic transports with a uniform positive floor. Define

$$
E_{ij}(q)=D_{\mathrm{KL}}(q_i\Vert T_{ij}q_j),
\qquad
\beta_{ij}(q)=
\frac{\pi_{ij}e^{-E_{ij}(q)/\tau}}
{\sum_m\pi_{im}e^{-E_{im}(q)/\tau}}.
$$

The normalized geometric-pooling response is

$$
B_i(q)(x)=
\frac{
p_i(x)^{a_i/A_i}
\prod_j[T_{ij}q_j(x)]^{\lambda\beta_{ij}(q)/A_i}}
{\sum_u
p_i(u)^{a_i/A_i}
\prod_j[T_{ij}q_j(u)]^{\lambda\beta_{ij}(q)/A_i}},
\qquad A_i=a_i+\lambda.
$$

It is continuous on the compact product simplex, so Brouwer gives at least one own-row filtering fixed point $q^\ast=B(q^\ast)$. This does not establish stationarity of a smoothing objective that differentiates the incoming source roles. At a selected fixed point,

$$
P_i^\ast(x,j)=\pi_{ij}T_{ij}q_j^\ast(x),
\qquad
Q_i^\ast(x,j)=\beta_{ij}^\ast q_i^\ast(x)
$$

are normalized and satisfy

$$
D_{\mathrm{KL}}(Q_i^\ast\Vert P_i^\ast)
=\sum_j\beta_{ij}^\ast D_{\mathrm{KL}}(q_i^\ast\Vert T_{ij}q_j^\ast)
+D_{\mathrm{KL}}(\beta_i^\ast\Vert\pi_i).
$$

The row source model is therefore proper and fixed after equilibrium selection. Its product duplicates the transported source templates and is not automatically a joint over shared $(x_1,\ldots,x_N)$. A shared joint needs compatible conditionals, an acyclic factorization, or a normalized undirected potential. The identity agrees with the canonical unscaled row KL at unit attention temperature; arbitrary temperature is a loss-tempered generalized-Bayes construction [[bissiri-2016-general-bayesian-updating]]. The existence theorem does not prove uniqueness or convergence of the implemented update schedule.

### Belief-configuration Gibbs lift

Let $X$ be a full belief configuration, let $\rho_0$ be a proper reference probability measure, and let $T_{\mathrm{cfg}}>0$. For a measurable population energy $\mathcal F$ define

$$
Z_{\mathcal F}=\int
e^{-\mathcal F(X)/T_{\mathrm{cfg}}}d\rho_0(X).
$$

A probability model

$$
\frac{dP_{\mathcal F}}{d\rho_0}(X)
=Z_{\mathcal F}^{-1}e^{-\mathcal F(X)/T_{\mathrm{cfg}}}
$$

exists exactly when $0<Z_{\mathcal F}<\infty$. For every $R\ll\rho_0$ with finite terms,

$$
\mathbb E_R[\mathcal F]
+T_{\mathrm{cfg}}D_{\mathrm{KL}}(R\Vert\rho_0)
=T_{\mathrm{cfg}}D_{\mathrm{KL}}(R\Vert P_{\mathcal F})
-T_{\mathrm{cfg}}\log Z_{\mathcal F}.
$$

This is an exact meta-level VFE and variational principle. The exact density relation is

$$
\frac{\mathcal F(X)}{T_{\mathrm{cfg}}}
=-\log\frac{dP_{\mathcal F}}{d\rho_0}(X)-\log Z_{\mathcal F}.
$$

Thus $\mathcal F$ is the configuration energy, equivalently the temperature-scaled negative log Radon-Nikodym density up to normalization. It does not turn the pointwise functional into the state-level ELBO excluded above. In an enlarged hierarchy one may draw $X\sim P_{\mathcal F}$, then draw each state from its sampled belief and observations from a fixed likelihood. The complete ELBO includes the configuration entropy in addition to $\mathbb E_R[\mathcal F]$.

Normalizability is the substantive existence condition: $e^{-\mathcal F/T_{\mathrm{cfg}}}$ must be integrable under the chosen proper reference law. A bounded-below energy that is finite on a set of positive reference measure is sufficient; coercivity is another sufficient condition, not a necessary one. On noncompact Gaussian means, SPD covariances, and $\mathrm{GL}^+(K)$ frames, invariant orbit volume may diverge. A compact regulator, gauge fixing with the relevant Jacobian, or a quotient measure can remove that orbit-volume divergence, but integrability in the remaining physical directions must still be checked. An unregulated Haar measure on a noncompact gauge orbit is not a probability law. This is the precise bridge to [[meta-entropy-manuscript]].

## V3 experimental two-hop term

For the selected filtering/MM route, the V3 implementation defines

$$
W_{ik}^{(2,h)}(\bar q)
=\sum_j\beta_{ij}^{(h)}(\bar q)\beta_{jk}^{(h)}(\bar q),
\qquad
\mathcal F_2(\bar q;q)
=\lambda_2\sum_{h,i,k}W_{ik}^{(2,h)}(\bar q)
\widehat E_{ik}^{q,h}(q_i;\bar q_k),
$$

where $\bar q$ marks the detached source state and $\widehat E$ is the registry-selected, clamped value-energy grid with live receiver query $q_i$ and detached source key $\bar q_k$; its derivative is gated by the destination clamp mask. `vfe3/free_energy.py` implements $W^{(2)}$ as `beta.detach() @ beta.detach()`. Those two hop weights are detached on every route. Endpoint keys are detached under filtering, while the smoothing oracle shares the live belief leaves between query and key roles and differentiates the endpoint energy through both. The main configuration, training entry point, and baseline ablation set `lambda_twohop=0.0`; the selected dedicated ablation sweeps `0.0`, `0.001`, `0.005`, and `0.01`.

Because $\beta$ is row-stochastic, $W^{(2)}$ is the two-step transition kernel of the attention Markov chain. The term is therefore the expected direct endpoint energy after two source-selection steps. It is not a canonical second Gibbs row: $W^{(2)}$ is derived rather than independently varied, and the implementation supplies neither a fixed two-hop prior nor a relative-entropy term for it. Every derivative route omits the response derivative of the live $\beta(q)^2$ weights; filtering additionally freezes the endpoint keys, whereas smoothing retains their endpoint-energy derivative.

In the flat vertex cocycle,

$$
\Omega_{ij}\Omega_{jk}=\Omega_{ik},
$$

so the direct endpoint transport used in $E_{ik}$ agrees with transport composed along a two-edge path. The probabilistic energy is still not path-additive: KL has no general triangle equality, and $E_{ik}$ does not become $E_{ij}+E_{jk}$. In edge-local Regime II, direct $\Omega_{ik}$ generally differs from the path product $\Omega_{ij}\Omega_{jk}$, so a composed-generative-path interpretation fails unless the selected connection is flat.

The selected ablation uses `e_step_update="mm_exact"`, `mm_damping=0.75`, and a frozen belief covariance. It adds a positive endpoint-precision block to the frozen belief-row majorizer and changes only the damped mean target, $\mu_i^+=0.25\mu_i+0.75\mu_i^\ast$; it does not take a literal gradient step. A sufficient anchored contraction condition extends by replacing the one-hop neighbor operator with the one-plus-two-hop operator and requiring its preconditioned norm to remain below one. The active implementation also has a state-dependent self precision, so this observation does not prove convergence of the live state-dependent iteration.

The code scope is belief-only. There is no corresponding model-channel gamma two-hop sector. The frame-alignment subproblem omits `lambda_twohop`, so nonzero two-hop coupling and nonzero frame refinement would update different coordinate objectives; the selected sweep keeps frame refinement off. The ordinary reflection-aware belief path retains the term, but the Metropolis reflection accept/reject scorer omits it; both reflection routes are off in the baseline. Production validation diagnostics retain the term through the captured state. The no-snapshot E-step trace used by both the end-of-run report and `test_results.json::estep_final_f_per_token` omits the coefficient. The purity ledger therefore classifies every nonzero `lambda_twohop` run as outside the canonical pure path.

The two-hop term can be included without contradiction in the belief-configuration Gibbs energy when the enlarged partition function remains finite. It cannot evade the fixed state-level mean-field obstruction. A canonical two-hop row would require an independently normalized variational row, a fixed row prior, its own categorical relative entropy, and a joint stationarity derivation.

## Relevance to this research

This record fixes the probabilistic status of the shared population objective across [[participatory-it-from-bit]], [[Multi-agent variational free energy]], and [[VFE Transformer Program]]. It supplies a theorem-level boundary for ELBO claims, a constructive higher-level generative model for the meta-entropy and RG programs, and the exact interpretation of the experimental V3 two-hop sweep. It also distinguishes receiver-response filtering equilibria from stationary points of the global smoothing scalar, which constrains how fixed-point and convergence claims may be stated in [[Inference machinery — variational EM and filtering]].

## Sources

- [[participatory-it-from-bit]] — PIFB2 base manuscript and the cross-scale Gaussian construction.
- [[meta-entropy-manuscript]] — configuration-space counting measure and thermodynamic interpretation.
- [[wainwright-2008-graphical-models-variational]] — fixed-model mean-field variational structure.
- [[bissiri-2016-general-bayesian-updating]] — coherent loss-based generalized Bayesian updating.
- [[VFE Transformer Program]] — executable language-model program and experimental two-hop route.
