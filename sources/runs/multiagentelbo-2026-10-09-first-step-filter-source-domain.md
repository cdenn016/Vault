---
type: run
title: "First-step recognition filter and enlarged stationary source domain"
aliases: ["N512 physical first-step conditional and stationary source tests"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# First-step recognition filter and enlarged stationary source domain

[Code PR213](https://github.com/cdenn016/MultiAgentELBO/pull/213), merged at `2b96517e005cf5a2b001c4f8b19f55835c25e50b`, publishes two separate advances following [[multiagentelbo-2026-10-09-own-parent-trajectory-forecast]]. The once-run saved-only first-step filter evaluates the physical conditional distribution of hidden recognition means at the original retained coordinates. Its independent QR reader passes 259 comparisons over 7,988,651 entries, including both complete 1024-coordinate conditional covariances, with maximum discrepancy $1.4210854715202004\times10^{-13}$. Separately, the enlarged stationary source domain lies in the same closed native generator and supports true cylinder martingales in the whole-past filtration. Neither result supplies the later recursive recognition filter, full-past stationary path-law identification, or an RG-gate closure.

```bibtex
@misc{codex2026firststepfiltersourcedomain,
  author = {Codex},
  title = {First-Step Recognition Filter and Enlarged Stationary Source Domain},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/213},
  note = {Merge 2b96517e; filter execution 18a6dfef; first unselected native numerical kernel and same-form conditional stationary identification}
}
```

## Physical first-step conditional

The [derivation](https://github.com/cdenn016/MultiAgentELBO/blob/2b96517e005cf5a2b001c4f8b19f55835c25e50b/docs/research/2026-10-03-latent-link-rg-plan/R3-FIRST-STEP-RECOGNITION-FILTER.md) and [frozen contract](https://github.com/cdenn016/MultiAgentELBO/blob/2b96517e005cf5a2b001c4f8b19f55835c25e50b/docs/research/2026-10-03-latent-link-rg-plan/R3-FIRST-STEP-FILTER-CONTRACT.md) keep the original N512/E1024 GL(2) model, selected matter slice two, order-nine direction, fixed probe and supplied 128/32-parent alternatives. At the complete known native initial prestate $x_0$, the selected raw mean proposal has law

$$
\mu_1\sim\mathcal N(m_1,Q_1),\qquad
m_1=\mu_0-hC_0g_0,\qquad Q_1=2ThC_0=C_0/400000,
$$

where $C_0=\operatorname{blockdiag}(\Sigma_{0,i})$, $h=1/40000$ and $T=.05$. The registered covariance/source/generator innovations and preceding mean entries are independent of the selected mean innovation. Consequently conditioning on the updated other retained coordinates $R_1$ preserves this Gaussian before imposing $M_1=A_1\mu_1$. The original hard forest makes $A_1$ full row rank. Writing $V_Q=A_1Q_1A_1^T$ gives the conditional mean and complete singular covariance

$$
m_{\mathrm{cond}}=m_1+Q_1A_1^TV_Q^{-1}(M_1-A_1m_1),\qquad
C_{\mathrm{cond}}=Q_1-Q_1A_1^TV_Q^{-1}A_1Q_1.
$$

The new belief covariance $C_1$ supplies the energy metric and centered point lift $\widehat\mu_1=u_1+C_1A_1^T(A_1C_1A_1^T)^{-1}(M_1-A_1u_1)$; it is not the transition covariance of hidden recognition parameters. The exact conditional quadratic identity is

$$
E[R_*\mid R_1,M_1,x_0]
=(m_{\mathrm{cond}}-\widehat\mu_1)^TC_1^{-1}(m_{\mathrm{cond}}-\widehat\mu_1)
+\operatorname{tr}(C_1^{-1}C_{\mathrm{cond}}).
$$

Shared parent columns $U_i=Q_iA_i^T\operatorname{chol}(V_{Q,p(i)})^{-T}$ encode $C_{\mathrm{cond}}=\operatorname{blockdiag}(Q_i)-UU^T$, including every same-parent cross-child covariance. The sparse factors describe a correlated fiber law, rather than a collection of independent fine marginals.

The [published result](https://github.com/cdenn016/MultiAgentELBO/blob/2b96517e005cf5a2b001c4f8b19f55835c25e50b/docs/research/2026-10-03-latent-link-rg-plan/R3-FIRST-STEP-FILTER-RESULTS.md) reports:

| Alternative | Mean mismatch contribution | Physical covariance contribution | Conditional expected R* | Actual archived R* |
| --- | ---: | ---: | ---: | ---: |
| 128 parents | 159.74270632122057 | .001919692808392296 | 159.74462601402897 | 159.80391042275377 |
| 32 parents | 183.78024981747936 | .002399677243699767 | 183.78264949472305 | 183.8715138946994 |

The conditional mean mismatch dominates these reported quadratics. Actual archived R* values enter only after both laws are fixed and are descriptive single-realization references. No distributional calibration test or scientific energy threshold follows. The conditional concerns a known fine initialization and the unselected raw numerical proposal kernel. A parent supplied only an initial mean would require an additional mixture over unknown fine initialization. Conditioning on successful box admission or later success would generally truncate the fiber law; upstream completed statuses serve byte provenance only.

At later unreset native updates, the original source log-ratio means depend quadratically on hidden fine means. Conditioning on source innovations produces a generally quartic density tilt, and retained generator observations add further hidden-state dependence. The first-step Gaussian and the existing deterministic point-lift candidate do not implement that recursive filter. Continuous native-Fisher accuracy, stopped residual integrals, posterior accuracy, causal feedback and persistent formation remain separate obligations.

## Independent replay and complete costs

The consumer ran once from clean published `18a6dfef6db7c87a5b8ffae2949860b30d11dd84`, generating no field, proposal, trajectory, observation or sample. The reader uses positive-diagonal QR of $(A_1\sqrt{Q_1})^T$, independently of the producer's covariance-Cholesky conditioning. It reconstructs 2,097,152 complete conditional covariance entries. Both parent mean constraints hold within $4.440892098500626\times10^{-16}$, cross-parent covariances are exactly zero, and physical factor/annihilation checks pass the frozen $10^{-12}$ allowance. Tiny negative local eigenvalues around $-10^{-21}$/$-3\times10^{-21}$ remain rounding diagnostics; no covariance jitter or clipping occurs. Means/energies use the frozen $10^{-8}$ allowance. Input, factor/solve/contraction and computed-state rounding remain excluded; readback is not an interval certificate.

The [producer receipt](https://github.com/cdenn016/MultiAgentELBO/blob/2b96517e005cf5a2b001c4f8b19f55835c25e50b/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-first-step-filter.json) and [reader receipt](https://github.com/cdenn016/MultiAgentELBO/blob/2b96517e005cf5a2b001c4f8b19f55835c25e50b/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-first-step-filter-readback.json) record .21260349999647588/.2572524999268353 seconds and 43,769,856/136,822,784-byte process peaks. Producer/reader JUnits record three/two passes in .272/.263 seconds, with zero failures/errors/skips. Earlier tiny-fixture failures and a clean-checkout gate refusal remain visible; no scientific outcome or passing test was retried.

Conditional mean, physical covariance blocks and sparse reduction blocks require 40,960 tensor bytes per alternative, plus 4,096-byte parent IDs unless reused from the charged contract. Complete retained states require 772,096/770,560 bytes, and shared original model/offset/rule/readout context requires 978,400 logical bytes. Dense readouts cost 2,097,152/524,288 bytes; energy centers, parent factors, known-prestate transition construction and reader workspace are additional. This is O(N) storage. All derived arrays occupy 4,682,320 logical bytes and 1,001,449 compressed bytes. Input/source snapshots occupy 3,436,261/140,316 bytes. The [canonical replay package](https://github.com/cdenn016/MultiAgentELBO/blob/2b96517e005cf5a2b001c4f8b19f55835c25e50b/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-first-step-filter-package.json) contains 40 files totaling 4,658,634 bytes, with canonical length/SHA256 parity. Root matched 16 input, 13 source and 39 reader bindings, including the executing reader hash.

| Pinned input | SHA256 |
| --- | --- |
| R3-FIRST-STEP-FILTER-RESULTS.md | 7bb9772c9bc3a85ef9e3acbca54704ebba9ec9fcf9c4427920b710a718eff485 |
| R3-FIRST-STEP-RECOGNITION-FILTER.md | 073f283e62b778052a1a0d0fe4672ed8d4a19e0e842d76bb80510216e32a18ea |
| R3-FIRST-STEP-FILTER-CONTRACT.md | 3274bcad94a788526f050422e019d94b67b4459288a822a9345e833fca1abce8 |
| Producer receipt | 4dbc96b67fbf4b48cc3dc6dcbb4bc9df84b12a0ce5fcdecf2843e3a92fb1f33e |
| Reader receipt | 11da6c8a334e4f020df4cdd359c25b96db9fd7355e152ac40904a8aba7811ea2 |
| R5-ENLARGED-SOURCE-DOMAIN.md | ce6d61f561afed8169f5fe5592ec35d5fc47746a36363a7162e10cb0f58f8b41 |

## Enlarged stationary source domain, with conditional identification

The separate [R5 derivation](https://github.com/cdenn016/MultiAgentELBO/blob/2b96517e005cf5a2b001c4f8b19f55835c25e50b/docs/research/2026-10-03-latent-link-rg-plan/R5-ENLARGED-SOURCE-DOMAIN.md) retains the admitted marked Gibbs law P, original native Fisher mobility/noise and the already chosen closed gradient form $(\mathcal E,D(\mathcal E))$. It adds smooth closed-simplex source factors with bounded derivatives to the old cylinder algebra. It does not change a source boundary condition or scientific law. The older compact-interior source algebra's dense-generator-range route was refuted in PR212; that result did not refute the conservative form realization.

For each supported row with a choices and prior floor $\pi_-$, subtracting the minimum comparison cost only inside its conditional estimate gives $U_\delta=\sum_j\beta_j(c_j-\min_kc_k)$. The published contraction-of-simplex argument bounds

$$
E[e^{sU_\delta/T}\mid e]\le e^{\log(1/\pi_-)/T}(1-s)^{-(a-1)},\qquad 0<s<1.
$$

This controls the source-force second moments uniformly in exterior costs. Combining it with the existing localized Gaussian-force estimates establishes the enlarged algebra $\mathscr C_+\subset D(L)$, with $L$ the same self-adjoint form generator, and globally square-integrable local generators. Source-face cutoff approximation makes it a core of the same form; generator graph-core density does not follow. Stationarity, the original coordinate-local SDE and bounded cylinder brackets give true cylinder martingales in the whole-past filtration under every admitted stationary reversible path limit with one-time law P.

The remaining conditional identification route is explicit. For every bounded $A\in\mathcal F_s$ and finite H, let $r_t(x)=E[A\mid X_t=x]$, including all frozen marks. If

$$
\int_s^{s+H}\mathcal E(r_t,r_t)dt<\infty,
$$

then the enlarged martingale identities extend to the form's weak evolution equation. Resolvent regularization and its energy identity yield $r_t=e^{(t-s)L}r_s$, hence $E[f(X_t)\mid\mathcal F_s]=(e^{(t-s)L}f)(X_s)$ and the entire stationary continuous-path law of the chosen form. The displayed energy assumption (EA) is unproved for the native law. Finite-neighborhood projection exposes conditional boundary-force covariance terms; growing boundary counts, absent correlation decay and Gaussian localization removal prevent the available estimates from proving it. Whole-past identification is therefore conditional, not established by form-core membership or weak path convergence alone.

## Relevance to this research

[[Natural gradient]], [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] gain an executed first nonstationary hidden-recognition conditional and a larger stationary test domain in the same native model. The next material filter obligation is the later nonlinear conditional under actual retained observations, followed by stopped residual/feedback control. The independent stationary obligation is (EA), or another established whole-past uniqueness argument for that same law and form. Arbitrary uncertain fine initialization, population/native-posterior accuracy, compact operational parents, intrinsic persistent second formation, growing size/depth and all four RG gates remain open. Both published calculations use isolated Anaconda CPU float64, sequential MKL and one thread; the user retains the GPU and the 144-case calibration remains unrun. This intake edits no manuscript, model or older immutable source and launches no scientific work.
