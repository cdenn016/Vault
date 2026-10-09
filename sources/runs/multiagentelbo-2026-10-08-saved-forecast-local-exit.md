---
type: run
title: "Saved Fisher forecasts and finite-network exit budgets"
aliases: ["Saved forecast KL and local Fisher containment"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# Saved Fisher forecasts and finite-network exit budgets

This record continues [[multiagentelbo-2026-10-08-product-moment-fisher]] and [[multiagentelbo-2026-10-08-fisher-trajectory-admission]]. [Code PR202](https://github.com/cdenn016/MultiAgentELBO/pull/202) publishes the saved forecast calculation and local coefficient/native-exit analysis at result revision `8f98ebc0ca87f3e2b995eb1f3a09df2efbecb6d5`, merged as `95aeba5aa9ea0e1542ca46fbed3795731692f133`. The saved forecast calculator and pre-outcome contract were frozen at `c0dc11cd776dd8b3b08b20e18ea29bd6a4f680e9`. The analytical work retains the live manuscript's Gaussian recognition Fisher flow in `c08b_lie_links.tex`, `prop:link-recognition-flow`, and the existing original-record/distinct-primitive loop moments in `g11_latent_links.tex`, `eq:glink-expected-record` and `prop:glink-expected-loop`. Root reconstructed the derivations and receipt rational checks; no formal adjudication state is assigned.

```bibtex
@misc{codex2026savedforecastlocalexit,
  author = {Codex},
  title = {Saved Fisher Forecasts and Finite-Network Exit Budgets},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/202},
  note = {Result revision 8f98ebc0; saved-state endpoint comparisons, conditional native containment and failed sufficient numerical budgets}
}
```

## Eight saved-state forecast comparisons

The [frozen saved-only calculation](https://github.com/cdenn016/MultiAgentELBO/blob/8f98ebc0ca87f3e2b995eb1f3a09df2efbecb6d5/docs/research/2026-10-03-latent-link-rg-plan/R3-SAVED-FORECAST-KL.md) compares the initial and one-/two-/four-step endpoints of the existing M16 Brownian-coupled Fisher admission. Each forecast uses the full episode-3 product-Gaussian generator recognition law, containing 1,024 four-dimensional primitive factors, and the same original future kernel. Fresh matter uses the original baseline and future labels use the original source prior; prefix matter and source factors never become future priors. Shared matter, primitive links and reversed occurrences remain in the full correlated original future-record vector. No future observation archive, new field, trajectory or sample enters the calculation.

Common-kernel KL contraction bounds joint forecast KL per receiver by $U_J=\sum_e\mathrm{KL}(q_e\Vert p_e)/512$. The separate marginal composite bound is $U_M=\sum_e\rho_e\mathrm{KL}(q_e\Vert p_e)$, with $\rho_e=512^{-1}\sum_{i,j:e(i,j)=e}\pi_{ij}$. The [first receipt](https://github.com/cdenn016/MultiAgentELBO/blob/8f98ebc0ca87f3e2b995eb1f3a09df2efbecb6d5/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-saved-fisher-forecast-kl.json) retains these eight directed float64 evaluations in the frozen order:

| Direction | Product Gaussian KL (nats) | $U_J$ (nats/receiver) | $U_M$ (nats/receiver) |
|:--|--:|--:|--:|
| `steps-1 || steps-2` | 3.442241105e-7 | 6.723127159e-10 | 3.361563579e-10 |
| `steps-2 || steps-1` | 3.442241739e-7 | 6.723128396e-10 | 3.361564198e-10 |
| `steps-2 || steps-4` | 1.684444860e-7 | 3.289931367e-10 | 1.644965683e-10 |
| `steps-4 || steps-2` | 1.684444686e-7 | 3.289931027e-10 | 1.644965513e-10 |
| `steps-1 || steps-4` | 5.057182208e-7 | 9.877309001e-10 | 4.938654500e-10 |
| `steps-4 || steps-1` | 5.057191691e-7 | 9.877327522e-10 | 4.938663761e-10 |
| `initial || steps-4` | 7.283975982e-2 | 1.422651559e-4 | 7.113257795e-5 |
| `steps-4 || initial` | 7.283767638e-2 | 1.422610867e-4 | 7.113054334e-5 |

Here every primitive has incident prior weight exactly $1/2$, so $U_M=U_J/2$; that relation belongs to this graph/prior. All 8,192 directed primitive comparisons satisfy both compact Gaussian chart inequalities within their frozen absolute/relative allowances $10^{-14}/10^{-10}$. Cholesky whitening and a degree-20 series for the small relative precision eigenvalues avoid cancellation. A tiny noncommuting fixture grounds KL orientation and the near-zero calculation against rational and 60-digit Decimal values. The one saved calculation completes in 0.2022 seconds on isolated Anaconda CPU float64 with one sequential math thread.

The 26-file portable archive totals 3,942,507 bytes, with 24 exact source/input snapshots, one first-result JSON and one replay NPZ. Replay arrays contain 1,253,504 logical bytes and occupy 1,187,691 file bytes. Root copied all 26 files hash-identically to the canonical code checkout. Tiny precision asymmetries require the declared real symmetric SPD interpretation; input symmetrization, Cholesky/solve and other floating evaluation rounding remain outside a certified interval budget. The series remainder is not a complete arithmetic certificate. The displayed values are finite endpoint comparisons of continuous recognition forecasts, rather than measured joint forecast densities, atomic-mixture accuracy, population convergence or native-posterior error.

## Population local coefficients and conditional native containment

The [local coefficient derivation](https://github.com/cdenn016/MultiAgentELBO/blob/8f98ebc0ca87f3e2b995eb1f3a09df2efbecb6d5/docs/research/2026-10-03-latent-link-rg-plan/R3-LOCAL-COEFFICIENT-BUDGET.md) concerns the existing population product-Gaussian Fisher diffusion at fixed $c_*$, with unchanged lower-Cholesky Brownian representation, temperature $T=1/20$, kinetic mass 16 and inference horizon $H=10^{-4}$. Its N512, C3/J4 layout retains 7,168 recognition blocks: 1,536 matter Gaussians, 4,096 generator Gaussians and 1,536 supported four-choice source rows. The independent Gaussian family, distinct primitives within each loop and fixed sparse original support remain assumptions; this does not cover correlated recognition, repeated-primitive loops or dense priors.

On the outer box, matter satisfies $\|\mu\|\leq2$, $I/2\preceq\Sigma\preceq I$; generators satisfy $\|\mu^\omega\|\leq1/20$, $12I\preceq\Lambda\preceq16I$; supported source coordinates are at least $3/20$. The inner box uses matter $\|\mu\|\leq9/5$, $(3/5)I\preceq\Sigma\preceq(19/20)I$, generator $\|\mu^\omega\|\leq9/200$, $(121/10)I\preceq\Lambda\preceq(159/10)I$, and source floor $9/50$. Covariance coordinates are $C^\omega=\Lambda^{-1}$. Exact Gaussian integration by parts gives $D_C E f[H]=\tfrac12 E\sum_{r,s}H_{rs}\partial_{rs}f$ and simplifies the native covariance drift to $(1+Td)C-CPC$. Centered-Gaussian odd-word cancellation bounds noncommuting exponential derivatives without a generic precision-Cholesky overestimate.

The [rational scalar receipt](https://github.com/cdenn016/MultiAgentELBO/blob/8f98ebc0ca87f3e2b995eb1f3a09df2efbecb6d5/docs/research/2026-10-03-latent-link-rg-plan/evidence/local-coefficient-budget.json) passes the fixed coefficient targets: complete outer block drift $B_0\leq76$, derivative row sum $L_{\rm row}\leq1130$, column sum $L_{\rm col}\leq28250$, noise Lipschitz square $L_\sigma^2\leq368/45<9$ and inner generator covariance operator drift below 0.890789. All sender contributions, source tangents, temporal neighbors and ordered-loop incidences are retained. The column estimate uses at most 25 dependent outputs per matter input; these are finite saved-model incidence bounds, not arbitrary-network uniformity.

Constraint-specific scalar martingale tails with a fixed sphere net give

$$
\Pr_{x_0}\{X_t\notin\mathcal K_0\text{ for some }t\leq10^{-4}\}\leq0.038196<1/20.
$$

The dominant contribution is generator covariance, below 0.038195278. This controls continuous native paths, including exits followed by returns before a saved endpoint. It is conditional on an exact native initial reference: stored binary means, symmetric stored matter covariance, symmetric stored generator precision and exactly row-normalized stored binary source probabilities. Exact rational LDL tests establish all 1,536 matter covariance and 4,096 generator precision bounds; the source normalization and matter symmetrization changes are exactly below $10^{-12}$. Neither state archive is altered. Unknown initialization/evaluation error relative to an ideal producer remains separate. The union factor depends on finite N and the result is neither arbitrary-N nor temperature-uniform containment of the numerical scheme.

The first scalar invocation fails during receipt serialization because a rational integer exceeds Python's 4,300-digit string limit. A serialization-only repair emits outward 30-decimal rational intervals; the next invocation writes one completed scalar outcome, retaining both exit codes and source hashes. Scientific calculations, targets and comparisons remain unchanged, without widened intervals or a scientific retry. No model, trajectory or GPU runs in this scalar analysis.

## Retained failure of the direct four-step sufficient budget

The declared numerical mesh is $h=H/4=1/40000$, with targets of total common exit budget at most $1/20$ and expected original joint forecast KL per receiver at most $10^{-3}$. The generic global native-exit formula is vacuous here even under hypothetical zero drift; the positive constraint-specific certificate above avoids mixing the smallest generator covariance margin with unrelated block noise.

For the particular direct numerical bound, the four-choice source correction is $r_Q=32/3$, so its sufficient constant obeys $C_H\geq32/625=0.0512$. That floor alone makes its common-exit Markov term exceed 59,380 and its joint forecast upper-budget expression exceed 0.00114688, above the declared forecast target. These are lower floors of the selected sufficient upper-bound formulas, not lower bounds on actual numerical error, exits or forecast KL. Setting the population quadrature component to zero cannot rescue this four-step bound. The remaining nonnegative remainder/propagation terms are therefore not evaluated; no full numerical $C_H$ certificate is claimed. A sharper constraint-specific coupled numerical calculation may improve this bound, and a smaller step would require a new pre-outcome contract rather than selection from these results.

## Relevance to this research

[[Natural gradient]] gains finite-model population coefficient and conditional continuous containment estimates, while [[Renormalization-group flow of beliefs]] gains eight saved original-forecast comparisons and a precise remaining numerical obligation. [[Staged hierarchy formation and RG composability]] still requires an admitted recognition-to-population forecast error budget, actual function/input arithmetic, native-posterior forward KL, autonomous parent/filter feedback and persistent growing formation. The order-9 rational integration/rule component from [[multiagentelbo-2026-10-08-product-moment-fisher]] remains separate from these obligations and does not certify the M16 empirical field. All four full RG gates remain open; no reward model is adopted, the 144-case calibration remains unrun, and the GPU stays with the user.
