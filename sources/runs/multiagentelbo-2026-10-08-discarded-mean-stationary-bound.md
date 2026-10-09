---
type: run
title: "Discarded matter means and stationary reconstruction bounds"
aliases: ["Saved discarded-mean and stationary energy bound"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# Discarded matter means and stationary reconstruction bounds

[Code PR208](https://github.com/cdenn016/MultiAgentELBO/pull/208), merged at b04646e159fe5e2a686abded771aac56650dccf1, publishes a saved-state discarded-mean diagnostic and a separate exact domain/stationary bound. It continues [[multiagentelbo-2026-10-08-preparation-paths-moment-trajectory]] and [[multiagentelbo-2026-10-08-discarded-energy-device-admission]]. Root reconstructed the analytical argument and numerical receipts; no formal adjudication state is assigned. The diagnostic ran once from clean published producer 7deec244efb7cf23b285ef0339b2f664d7bea9c2, without a new field, trajectory, observation or GPU allocation.

```bibtex
@misc{codex2026discardedmeanstationary,
  author = {Codex},
  title = {Discarded Matter Means and Stationary Reconstruction Bounds},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/208},
  note = {Immutable merge b04646e1; frozen producer 7deec244; saved q9 matter diagnostic and separate finite stationary theorem}
}
```

## Frozen original-record diagnostic

The [contract](https://github.com/cdenn016/MultiAgentELBO/blob/b04646e159fe5e2a686abded771aac56650dccf1/docs/research/2026-10-03-latent-link-rg-plan/R3-DISCARDED-MEAN-CONTRACT.md) uses the existing N512/E1024/K2, mass-16 order-9 path. Its four old field states are initial and checkpoints 1, 2 and 3; checkpoint 4 has no matching saved moment field and is excluded. Only observed matter slice 2, its current covariance/source weights, original offsets, both signs of shared primitive moments and actual original-copy probe trees enter. Future observations, forecasts and Brownian arrays are not diagnostic inputs.

With every receiver and attended-sender force retained, the expected matter objective has the full 1024-coordinate quadratic $K$, linear term $h_0$ and center $u=K^{-1}h_0$. The producer checks $K\mu-h_0$ and diagonal $K$ blocks against archived matter derivatives/precision targets. This uses live g11_latent_links.tex, proposition prop:glink-sample-record and equation eq:glink-expected-record, with the collective Fisher mean metric. For current block-diagonal covariance $C$, actual parent map $A$ and $V=ACA^T$, the centered lift is

$$
\widehat\mu=u+CA^TV^{-1}A(\mu-u),\qquad
r=\mu-\widehat\mu,\qquad
R_{*,A}=r^TC^{-1}r.
$$

It preserves $A\mu$ and gives same-covariance product-recognition reconstruction KL $R_{*,A}/2$, without bounding the fresh future-generator forecast or latent posterior. The saved defect $-ACKr$ changes only the matter mean force at fixed current covariance/map. Moving geometry, covariance/source/generator drift and common noise are additional terms.

The [first result](https://github.com/cdenn016/MultiAgentELBO/blob/b04646e159fe5e2a686abded771aac56650dccf1/docs/research/2026-10-03-latent-link-rg-plan/R3-DISCARDED-MEAN-RESULTS.md) reports:

| Old field state | KL / fine agent, 128 parents | KL / fine agent, 32 parents |
|---|---:|---:|
| Initial | 0.1560328732051402 | 0.1795121048097736 |
| Checkpoint 1 | 0.1560585062722205 | 0.1795620252877924 |
| Checkpoint 2 | 0.1560625283990370 | 0.1795965002146853 |
| Checkpoint 3 | 0.1561056609567431 | 0.1796210240414634 |

Discarded energy increases slightly across these three short positive-temperature updates. The observed-slice mean Fisher dissipation ranges from 1870.4828584068337 to 1871.164776257196. These are descriptive snapshot values on one path, not a continuous-time integral, convergence result or failure of late activation. Different depths have different coordinate dimensions/geometries; their force norms are not a matched error comparison.

## Exact covariance-domain and finite stationary bounds

The separate [analytical note](https://github.com/cdenn016/MultiAgentELBO/blob/b04646e159fe5e2a686abded771aac56650dccf1/docs/research/2026-10-03-latent-link-rg-plan/R3-DOMAIN-DISCARDED-ENERGY-BOUND.md) retains the native population objective and original sender incidences. Under explicit $C\succeq\ell J_0^{-1}$ it proves $R_{*,A}\leq\ell^{-2}\mathcal I_\mu$ without commuting covariance/Hessian. Exact zero-temperature joint Fisher dissipation then gives stopped time-integrated control for moving full-rank maps, with weighted finite depths paying their total weight. Domain containment, energy drop per agent and growing unweighted depth remain separate. Deterministic decrease is not asserted for the positive-temperature saved path.

Common-state order-9 transfer uses the same covariance and the $C^{-1}$ norm of the native/rule mean-direction difference. It retains the existing rational integration/rule-only budget and excludes input representation, Cholesky, exponential, differentiation and contraction arithmetic. Finite-rule and population centers differ; the saved residual is not a native population certificate.

The stationary theorem assumes the normalized original finite native Fisher invariant law $\Pi_T$, common matter dimension $d$, the existing sufficient normalization condition $0<T<1/d_{\max}$ across all Gaussian factor dimensions, and the stronger inverse-moment condition $0<T<1/(d+2)$. Conditional on generator/source parameters $G$, mean parameters obey $\mu\mid G\sim N(u,TK^{-1})$; covariance factors are independent Wishart laws with degrees of freedom $1/T-1$ and scale $TK_{ii}^{-1}$. Hence $E[C_i^{-1}\mid G]=K_{ii}/[1-T(d+2)]$. Product matter recognition inside the objective does not make the mean parameters independent under this invariant law.

For normalized nonself two-endpoint records and uniform summed receiver precision budget $U\preceq hJ_0$, the complete receiver/sender quadratic satisfies $D(K)\preceq\chi K$, with $\chi=1+h+\sqrt{h^2+h}$. Let $D$ be the included matter-coordinate dimension, so $D/N=d$ for one observed slice and the number of observed slices multiplies this ratio when all are included. Thus

$$
E_{\Pi_T}\frac{R_{*,A}}N
\leq\frac{T\chi}{1-T(d+2)}\frac DN,\qquad
E_{\Pi_T}\frac{\mathrm{KL}(N(\mu,C)\Vert N(\widehat\mu,C))}N
\leq\frac{T\chi}{2[1-T(d+2)]}\frac DN.
$$

The upper bound permits measurable full-rank snapshot maps, including mean-dependent maps. The exact conditional parent trace formula separately requires mean-independent $A$. For one observed $d=2$ slice, $h=1$ and $T=1/20$, energy and recognition-KL ceilings per fine agent are $(2+\sqrt2)/8$ and $(2+\sqrt2)/16$. The bound is uniform over finite size and rooted depth in this declared class and vanishes uniformly as temperature tends to zero. It does not vanish with size/depth at fixed temperature, certify stationary q9 checkpoints or give a nonstationary activation rate. Infinite-law center/decoder and moving-parent constructions remain separate.

## Independent replay and charged costs

The [NumPy/SciPy readback](https://github.com/cdenn016/MultiAgentELBO/blob/b04646e159fe5e2a686abded771aac56650dccf1/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-discarded-mean-readback.json) reconstructs $K,h_0$ by applying archived original receiver/sender forces to a full coordinate basis and zero mean, then independently checks lifts, residuals and force defects. All 256 comparisons over 16,119,384 entries pass; maximum discrepancy is $4.547473508864641\times10^{-13}$ against absolute $10^{-8}$, with symmetry $10^{-12}$ and exact identity/alignment/hash checks. Successful Cholesky is a binary64 positivity check, not certified exact arithmetic. Root matched all 30 producer inputs, six sources, 40 readback input bindings and the executing checker snapshot.

The [producer receipt](https://github.com/cdenn016/MultiAgentELBO/blob/b04646e159fe5e2a686abded771aac56650dccf1/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-discarded-mean.json) records 1.2940983000444248 seconds and 107,659,264-byte process peak; readback takes 1.8202754999510944 seconds and peaks at 261,849,088 bytes. Both use isolated Anaconda float64, sequential MKL and one math thread. [Focused JUnit](https://github.com/cdenn016/MultiAgentELBO/blob/b04646e159fe5e2a686abded771aac56650dccf1/docs/research/2026-10-03-latent-link-rg-plan/evidence/discarded-mean-focused.xml) records three tiny grounding tests, zero failures/errors/skips and 1.773 seconds. No broader suite or retry occurred.

Derived arrays occupy 93,043,104 logical and 5,050,260 compressed bytes; inputs occupy 9,570,265 snapshot bytes and sources 91,486 bytes. Each whole matrix/basis costs 8,388,608 bytes; receiver/sender basis arrays each cost 33,554,432 bytes. Charged workspaces, storage and measured peaks differ. The [complete manifest](https://github.com/cdenn016/MultiAgentELBO/blob/b04646e159fe5e2a686abded771aac56650dccf1/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-discarded-mean-package.json) retains 50 files totaling 14,795,249 bytes. Root copied them to the actual canonical code artifact directory and matched every length and SHA256.

## Relevance to this research

[[Natural gradient]] gains a saved common-state matter quadratic/lift diagnostic and explicit domain dissipation bound. [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] gain a finite stationary recognition expectation uniform in size/depth within the declared record class. Full moving-map drift/quadratic variation, retained/filter updates, original-flow feedback, nonstationary/size-depth limits and persistent formation remain open. No full parent or RG gate closes; reward choice remains unadopted and the 144-case CUDA calibration remains unrun while the user owns the GPU. This intake modifies no manuscript/model and executes no new science.
