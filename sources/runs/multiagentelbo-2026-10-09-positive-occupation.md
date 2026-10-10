---
type: run
title: "Positive-strength occupation through exact reset cycles"
aliases: ["Positive-strength MAP reset-cycle occupation", "Conditional complete-cycle stationarity criterion"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Positive-strength occupation through exact reset cycles

Codex (2026). *Positive-strength occupation through exact reset cycles*. MultiAgentELBO [PR262](https://github.com/cdenn016/MultiAgentELBO/pull/262), source commit b93285199d8c575da34855ee9419064f704458f4 and merge 0643d01283b4719a0b8d4e3dac0f1d4f6318f340, publishes [R4-POSITIVE-STRENGTH-OCCUPATION.md](https://github.com/cdenn016/MultiAgentELBO/blob/0643d01283b4719a0b8d4e3dac0f1d4f6318f340/docs/research/2026-10-03-latent-link-rg-plan/R4-POSITIVE-STRENGTH-OCCUPATION.md). The complete unadopted conjugate-prior MAP candidate has an exact constant-rate all-off membership reset decomposition, a cycle kernel retaining every on-sheet excursion, and a bijection between invariant probabilities of that kernel and the complete process. A proper additive cycle inequality would imply tight actual-law Cesaro occupation and a complete invariant law, but the native inequality remains unproved. An exact full-dimensional covariance witness rejects uniform compact recovery during finite all-off intervals, without refuting stationarity. All four RG gates remain open, with the roughly 65% planning estimate unchanged.

```bibtex
@misc{codex2026positiveoccupation,
  author = {Codex},
  title = {Positive-strength occupation through exact reset cycles},
  year = {2026},
  howpublished = {MultiAgentELBO mathematical checkpoint PR262},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/262}
}
```

## Candidate and fixed finite target

This continues the positive-strength stationarity obligation in [[multiagentelbo-2026-10-08-native-flow-handoff-fisher-step]], with the proper conjugate-prior MAP reward learner and native weighted thermostat still unadopted. It is distinct from original R0 dynamics and from the unrestricted unregularized reward extension in [[multiagentelbo-2026-10-08-filter-boundary-learning-domain]]. The source changes no scientific model or adoption decision. Its conditional inequality is an unproved hypothesis, not an added model assumption.

The target is one fixed finite supported graph, finite latent-history and observed-prefix design, strictly positive Gaussian anchors, finite original nonnegative actions, finite transported strengths with at least one positive strength, positive learning parameters alpha and epsilon, a fixed m_* in the open membership-mean cube, and fixed 0<T<1/4 in the real GL+(2) family. Everything is at c_*. Recognition uses full Gaussian means/covariances and supported source simplices; primitive generator blocks have d=4 with all noncommuting matrix directions. Source hard zeros remain omitted from their simplex, independent copies and inverse reversals remain as declared, and the recognition force remains the simultaneous collective product-Fisher force.

The requested result is tight Cesaro occupation from at least one admitted interior preparation, with compact reward means allowed at initialization. A complete invariant probability would follow from the prior conservative Feller process. Invariance concerns preservation of the complete one-time law for every inference-time increment. Uniqueness, mixing, all-start convergence, deterministic-path equivalence and uniform estimates in size or temperature are excluded.

## Compact reward carrier and complete native process

For q membership bits, the complete state is E=M times {0,1}^q times D_*, where M is the product of full Gaussian recognition blocks and supported interior source simplices, and

$$
D_*=\prod_e[\ell_e,u_e]\Subset(0,1)^q,\qquad
\ell_e=\frac{\alpha m_{*,e}}{1+\alpha},\qquad
u_e=\frac{1+\alpha m_{*,e}}{1+\alpha},\qquad
\lambda=\epsilon(1+\alpha).
$$

D_* is an invariant subset of the original open-cube reward-mean domain, rather than a new boundary rule. Its endpoints correspond to finite interior reward parameters; every invariant probability on the larger domain must already give D_* full mass.

For the normalized positive finite generative catalog, let eta(m) be the smooth inverse of its mean map. Recognition sheets and the realized-mark learner are

$$
f_b(x)=F_0(x)+\sum_e b_e\kappa_e C_e(x),\qquad
C_e(x)=\mathbb E_{Q_x}\delta_e\geq0,\qquad
\dot m=\epsilon[b+\alpha m_*-(1+\alpha)m].
$$

F_0 is the original population VFE, without a finite-draw replacement. One independent rate-one Poisson clock redraws the whole membership vector, including redraws returning the present vector, with

$$
r_T(c\mid x,m)=\prod_e p_e^{c_e}(1-p_e)^{1-c_e},\qquad
p_e=\operatorname{sigmoid}\left(
\frac{\eta_e(m)+\operatorname{logit}\rho_e-\kappa_eC_e(x)}{T}\right).
$$

Between events, recognition follows the original Fisher sheet diffusion and rewards follow the affine ODE. The Gaussian covariance geometric drift is Td_j C, and source diffusion uses the supplied reference h=product beta_ij^(1/2). Rewards have no Brownian noise, reflection or clipping. The complete process remains conservative and Feller under the prior local regularity and Gaussian exponential-moment domination assumptions. This is the continuous native candidate process, rather than its discretization or opt-in numerical proposal.

## Exact clock split and full-cycle kernel

Compact D_* and nonnegative C_e give M_e=max_(m in D_*) eta_e(m)<infinity and the uniform all-off floor

$$
r_T(0\mid x,m)\geq
\prod_e\left[1+\exp\left(\frac{M_e+\operatorname{logit}\rho_e}{T}\right)\right]^{-1}
=:a,\qquad 0<a<1.
$$

This is a finite-instance constant; it can deteriorate severely with q and T and supplies no large-network or low-temperature uniform bound. Define the residual law and membership reset by

$$
\widetilde r_T(c\mid x,m)=\frac{r_T(c\mid x,m)-a\mathbf1_{\{c=0\}}}{1-a},
\qquad (R\varphi)(x,b,m)=\varphi(x,0,m).
$$

The residual process H_t uses the same continuous recognition/reward dynamics with residual redraws at rate 1-a. Superposing an independent rate-a split clock that sets b=0 gives exactly the original rate-one conditional redraw law and complete joint path law:

$$
\mathscr L=\mathscr H+a(R-I).
$$

The reset changes membership only. Recognition x and reward means m retain their actual entering values, so this is not independent state regeneration. Residual cycles still include all positive-strength on-sheet forces. A split event returning an already all-off vector is still counted.

On E_0=M times D_*, identified with the b=0 section, let Z_n=(X_(tau_n),M_(tau_n)) at successive split times. Split gaps are independent exponential variables of rate a relative to the starting past, while their dependence on the ensuing endpoint is retained. The exact unnormalized occupation operator and Feller chain kernel are

$$
\mathcal O\varphi(z)=\int_0^\infty e^{-at}H_t\varphi(x,0,m)dt,
\qquad P\psi(z)=a\mathcal O(\psi\circ R)(z),\qquad
\mathcal O1=1/a,\quad P1=1.
$$

For a recognition-only W, resets leave its value unchanged, giving PW=a O W. The cycle is not constrained to remain on b=0.

## Invariant probabilities and conditional actual-law occupation

Invariant probabilities zeta of P and pi of the complete process correspond bijectively through

$$
\pi=a\zeta\mathcal O,\qquad\zeta=\pi R.
$$

The source proves this at the semigroup level through the exact last-split renewal equation, including normalization and both directions. Formal generator annihilation alone is not used as an invariance proof. The correspondence includes every on-sheet excursion and deterministic reward motion; it does not establish existence of either invariant probability by itself.

The sufficient conditional hypothesis is a finite continuous W>=1 whose recognition sublevels are compact, a finite nonnegative measurable V on E_0 and a finite C>=0 such that, at every reset state,

$$
PV-V+a\mathcal O W=PV-V+PW\leq C.
$$

Proper W must control means, large and singular Gaussian covariances, and every supported source face; Gaussian KL sublevels alone do not suffice. V may depend on reward means. The inequality ensures finite PV and PW. It is equivalent, with the same C, to the usual additive form

$$
PU-U+W\leq C,\qquad U\geq0,
$$

using U=V+W in one direction and V=U-W+C in the other. Neither equivalent inequality has been proved for the native positive-strength family.

If the inequality holds, summing it from an interior preparation with b=0, m in D_* and finite V(z_0) gives tight expected discrete Cesaro reset laws and hence a P-invariant probability. A stopped-cycle argument, including the full final cycle, gives the actual continuous-law bound

$$
\mathbb E\int_0^H W(X_t)dt
\leq\frac{V(z_0)+C(1+aH)}{a},
\qquad
\limsup_{H\to\infty}\frac1H\int_0^H
\Pr\{X_t\notin K_R\}dt\leq\frac{C}{R},\quad K_R=\{x:W(x)\leq R\}.
$$

The bound uses the marginal Poisson mean E(N_H+1)=1+aH, without assuming independence of reset states and reset counts. A separate predictable-intensity compensator proof yields the same constant. Compact rewards and finite marks complete tightness of actual full-process occupation, and the conservative Feller semigroup then supplies an invariant complete law. The criterion is sufficient rather than necessary; geometric contraction and exponential return rates are unnecessary stronger assumptions. This implication remains conditional on the native full-cycle bound.

## Why finite all-off intervals do not uniformly restore compactness

The exact witness is an admitted subclass on an existing finite GL+(2) network: empty observed prefix, zero original loop/increment actions, identity Gaussian anchors, and finite positive bond strengths retained. Their forces vanish only during b=0. One existing full d=4 generator Gaussian covariance starts at C_0=exp(-R)I_d, strictly positive with full noncommuting generator support. This is a covariance test inside the complete carrier, not an abelian or diagonal-generator replacement.

Its anchored all-off covariance obeys

$$
dC=[C-C^2+TdC]dt+\sqrt T C^{1/2}(dB+dB^T)C^{1/2},
\qquad
d\log\det C=[d(1-T)-\operatorname{tr}C]dt+2\sqrt{Td}dW_t.
$$

For any fixed compact recognition set K, this block has a covariance floor delta I_d. Writing S=R+log delta, the source's Brownian reflection bound gives

$$
\Pr\{\tau_K\leq h\}\leq
2\exp\left[-\frac{d[S-(1-T)h]^2}{8Th}\right]\longrightarrow0
$$

for each fixed finite h as R grows. If L is an independent exponential duration of any fixed rate gamma>0, choosing h=S/[2(1-T)] gives

$$
\Pr\{\tau_K\leq L\}\leq
 e^{-\gamma S/[2(1-T)]}+2e^{-d(1-T)S/(16T)}\longrightarrow0.
$$

An actual all-off interval ending at the next original redraw has gamma=1; another gamma is a hypothetical holding-duration comparison, without changing native kinetics. Thus the positive all-off floor and an anchored frozen-sheet invariant law do not yield uniformly effective finite/exponential compact state regeneration. The witness rejects only that shortcut. It establishes no escape, nonexistence of a complete invariant law, failure of the conditional cycle criterion, source-face estimate or large-N prevalence. State-dependent restoration times and subsequent full cycles remain possible avenues for control.

## Exact native kernel expansion and remaining obligation

For a fixed sheet b, let X_t^b be its native conservative recognition diffusion, v_b=(b+alpha m_*)/(1+alpha), and Phi_t^b(m)=v_b+(m-v_b)exp(-lambda t). The free-sheet rate-one resolvent S integrates the joint recognition/reward motion against e^-t. J applies the residual state-dependent catalog redraw, I extends a reset-state test to every sheet, and E_0 restricts to b=0. The exact ordered expansion is

$$
P=aE_0\sum_{n=0}^{\infty}(1-a)^n(SJ)^nSI.
$$

Each term contains n residual redraws, the free-sheet interval before every event, and then the split event. Its order retains intervening state-dependent redraws, positive-strength sheet forces and reward evolution. The geometric series converges in operator norm on bounded tests. For nonnegative unbounded tests it is a monotone sum whose finiteness remains unproved; the expansion itself supplies no occupation moment bound.

The next native obligation is an actual state-dependent full-cycle drift or another sufficient tight occupation estimate for this exact P, including entering-covariance restoration and supported source faces. Uniform recovery from a finite all-off interval cannot be reused without a new mechanism. Positive-strength stationarity stays open. Even a future invariant-existence proof would leave R15 stationary entrance statistics, restoring/recurrence comparisons, initial-law quantifiers, causal second coalescence, conditional/dynamical parent errors and growing persistent hierarchy separate and unresolved. The MAP candidate remains unadopted, and all four RG gates stay open at roughly 65%.

## Provenance and relevance to this research

The checkpoint contains one bounded reset-cycle analytical mechanism and the coordinator's reconstruction of exact split/path law, semigroup correspondence, both stopped-cycle occupation arguments, additive equivalence, ordered resolvent expansion and full-dimensional covariance constants. This is not independent mathematical adjudication or formal verification-ledger closure. No scientific execution, simulation, sampler, numerical experiment, test, GPU or Lean work occurred.

One bounded Exa Ultra request completed (`agent_run_f70f4e4a81e7450b9ab82ca73cd37121`, `schema_satisfied`) at recorded total cost $2.4769. It supplied a candidate cycle formulation and kernel expansion; only its structured output was read for consolidation. Its frozen request/creation/terminal/source bindings remain in the published repository evidence directory. Three relevant repository source excerpts were transmitted; no scientific claim closed through that candidate. The coordinator separately inspected the hypotheses of the primary switching-diffusion sources. Those literature references supply context rather than an applied native stationarity theorem.

| Published item | Bytes | SHA256 |
|---|---:|---|
| R4-POSITIVE-STRENGTH-OCCUPATION.md | 25537 | 0c0178e4d6279b836268f08e47d09ef85b7f73631ca22cf7f656a55ade52a17e |
| evidence/r4-positive-occupation-source-intake-20261009.json | 5152 | e6209e54d63d60707a69b91537195a6922f5eeacdc397be4920d7bc2bd5af2a8 |

The intake binds ten repository sources, three live theory sources and one dated wiki context. Read-only live context is SPEC R13-R15, c13_formation.tex lines 1512-1569 and c12_multiscale_vfe.tex lines 363-453, preserving formation and normalization obligations. The consulted theme is explicitly as of Research 09bb10c2e7fc523ff493e93cc521ad805a1acb1a, 127730 bytes, SHA256 01aac326878265a161164c973a57da9451b9160a2a02764e30a27af77c919b09; this ingest subsequently updates its synthesis.

Actual canonical Code main, HEAD and origin/main were confirmed at 0643d01283b4719a0b8d4e3dac0f1d4f6318f340 before vault mutation. Completed artifacts/r4-occupation-handoff-20261009.json has SHA256 62af8c0638572b7bfd609f39c26b384e730c3fb6b57794773b10984d159a19d7 in both code copies. This handoff records source/parity/preservation, rather than another stationarity theorem.

This develops [[Staged hierarchy formation and RG composability]] and the stationarity obligation in [[multiagentelbo-2026-10-08-native-flow-handoff-fisher-step]]. The reset-cycle reduction keeps actual-law occupation distinct from frozen-sheet stability, tight rewards and formation. Only this new immutable source note and the existing theme/index/append-only log change. All 27 prior October 9 immutable notes, nine prior postflight receipts, prior and newly cited live theory bytes and protected weekly-report WIP are preserved. No manuscript, scientific model, runtime, configuration or adoption decision changes.
