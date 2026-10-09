---
type: run
title: "Fixed-prefix actual-law error and bounded hybrid-history recurrence"
aliases: ["N512 held-fixed H2 native recognition error and capped hybrid TV accumulation"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Fixed-prefix actual-law error and bounded hybrid-history recurrence

This intake records [MultiAgentELBO PR230](https://github.com/cdenn016/MultiAgentELBO/pull/230), producer source `fcad20b4334a6e42d5b886e62eaffac52b254f8a`; [PR231](https://github.com/cdenn016/MultiAgentELBO/pull/231), reader repair `9fef0ea420a9094f25b8454c6f4d4ee948b8bca2`; [PR232](https://github.com/cdenn016/MultiAgentELBO/pull/232), bounded recurrence/journal source and repaired execution `0ab1f1c60a162a49dc8654d11ae938586ed668c1`; and [PR233](https://github.com/cdenn016/MultiAgentELBO/pull/233), result merge `0b7bdbbc7a93ec7aa23cff4b3e020c6b9997f63c`. One held-fixed H2 actual-law next-conditional error is bounded from saved Gaussian moments and inherited error. A separate bounded-TV recurrence places finite-horizon local costs under the existing hybrid's evolving history law. Its useful history expectation remains unevaluated. The first reader failure is preserved and the separately frozen repair passes; the producer is not rerun.

```bibtex
@misc{codex2026fixedprefixnativeerror,
  author = {Codex},
  title = {Fixed-prefix actual-law error and bounded hybrid-history recurrence},
  year = {2026},
  howpublished = {MultiAgentELBO research records, pull requests 230 through 233},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/233}
}
```

## Actual law at one fixed old history

[R3-FIXED-PREFIX-ACTUAL-LAW-ERROR.md](https://github.com/cdenn016/MultiAgentELBO/blob/0b7bdbbc7a93ec7aa23cff4b3e020c6b9997f63c/docs/research/2026-10-03-latent-link-rg-plan/R3-FIXED-PREFIX-ACTUAL-LAW-ERROR.md), equations (1)-(8), fixes the already generated H2 from [[multiagentelbo-2026-10-09-generated-prefix-filter]], with actual hidden endpoint eta2 and physical Gaussian reference q2. The inherited whole-prefix K2/C_chi bound endpoint KL/chi-square by contraction. The original current-R2 kernel from [[multiagentelbo-2026-10-09-advanced-retained-coefficients]] remains unchanged. A neutral proof comparison S freezes source contrasts and both selected generator mean/covariance shifts at the q2 mean, retaining the selected affine mean kernel, every noise covariance, chart normalization/Jacobian and full new precision-dependent parent readout. Under S, q3(Y) is the exact Gaussian downward conditional; it is only an approximation under the original q2-mixed kernel Q.

For each original whitened quadratic chart row, u_r=f_r(x)-f_r(m) retains its nonzero trace bias and complete support covariance. With M2_r=E_q u_r^2 and M4_r=E_q u_r^4, the centered inherited-error allowance is

$$
\Gamma_P\leq\Gamma_Q+\frac{\sqrt{C_\chi}}2\sum_r\sqrt{M4_r-M2_r^2},
\Gamma_Q=\frac12\sum_r M2_r.
$$

This requires no independence between rows. Finite Gaussian fourth moments and the inherited chi-square bound establish these actual-law expectations at the fixed H2. The augmented KL chain gives expected next-conditional KL under the actual next-observation law at most K2+Gamma_P; Pinsker/Jensen give expected conditional TV at most min(1,sqrt((K2+Gamma_P)/2)). The separate Gaussian-projected joint Q_Y q3(Y) uses the documentary ceiling 2K2+Gamma_P. The inherited K2 appears once in the conditional bound and twice in that joint bound, without a KL triangle inequality or summing unrelated saved-prefix bounds.

[The frozen consumer contract](https://github.com/cdenn016/MultiAgentELBO/blob/0b7bdbbc7a93ec7aa23cff4b3e020c6b9997f63c/docs/research/2026-10-03-latent-link-rg-plan/R3-FIXED-PREFIX-NATIVE-ERROR-CONTRACT.md) evaluates all 15,872 current-R2 rows: 1,536 source, 4,096 generator mean and 10,240 generator covariance rows. The original N512/K2, 1024 primitive reversal pairs, mass 16, q9 rule, observed episode prefix 0-2, four generator slices, 128-parent forest, h=1/40000 and T=.05 stay fixed. No future y, hidden realization, original noise or success event enters conditioning. Full physical covariance and trace bias are retained. Field, response, proposal, readout and noise evaluation counters are zero.

| Fixed-H2 computational quantity | Value |
| --- | ---: |
| Inherited K2 | 1.4334298217028817e-5 nat |
| Inherited C_chi | 1.4334400953572388e-5 |
| Gamma_Q | 8.956669850110417e-7 |
| Centered chi-square inflation | 4.795712924577853e-9 |
| Gamma_P upper | 9.004626979356196e-7 |
| Actual next-conditional forward-KL upper | 1.5234760914964436e-5 nat |
| Expected next-conditional TV upper | 0.002759960227518183 |

There is no receiver division or accuracy pass target. These values average over the actual next observation while holding old H2 fixed. They do not average over random old histories from original initialization, integrate the posterior or certify floating/response/population/native accuracy. The legacy uncentered component allowance remains descriptive and is not selected instead of the declared centered result.

## Bounded accumulation under hybrid histories

[R3-HYBRID-REFERENCE-TV-RECURRENCE.md](https://github.com/cdenn016/MultiAgentELBO/blob/0b7bdbbc7a93ec7aa23cff4b3e020c6b9997f63c/docs/research/2026-10-03-latent-link-rg-plan/R3-HYBRID-REFERENCE-TV-RECURRENCE.md), equations (1)-(8), keeps the existing hybrid retained transition q_j K_j and augments it by drawing its endpoint from the next causal Gaussian q_(j+1). This normalized augmentation has the same hybrid retained-history law. Its Gaussian downward redraw is an explicit approximation, not the nonlinear downward conditional of q_j T_j or a changed original fine law. It preserves the selected endpoint/noises used to generate the retained observation, full moving geometry, both generator mean/precision probe dependence and all available constraints.

Let e_j be TV between the actual history/current-endpoint joint and this augmented hybrid joint. The same original-kernel propagation contracts old error; replacing the provisional hybrid endpoint costs c_j(H)=min(1,sqrt(2 Gamma_Q(H))). Consequently

$$
e_{j+1}\leq e_j+E_{\widetilde P_{H_j}}c_j(H_j),
\operatorname{TV}(P_{H_n},\widetilde P_{H_n})\leq e_{n-1},
$$
$$
E_{P_{H_n}}\operatorname{TV}(\eta_n,q_n)\leq\min(1,e_n+e_{n-1}).
$$

Each local cost is bounded by one, so its finite-horizon hybrid-history expectation exists without a global raw entropy moment. This establishes integrability, not a small numerical expectation. From known initialization e0=e1=0; a four-step initialized allowance needs the hybrid expectations of c1,c2,c3. A study started instead at held-fixed H2 has a nonzero inherited startup allowance and a different history expectation. The fixed-H2 result above and four draws in [[multiagentelbo-2026-10-09-recursive-parent-kernel]] are not independent complete hybrid histories and cannot be summed as that budget.

The remaining estimand is E_hybrid sum_j c_j(H_j), with complete own-current-R coefficients and physical q endpoints at every evolved prefix. A finite sample average would need a frozen statistical upper allowance and separate arithmetic/model-error allowances. Failed or uncertified local costs cannot be silently deleted or selected by survival; an unavailable local certificate may conservatively cost one, while failures to draw the declared law require execution-error control. The unrestricted raw-reference entropy divergence and uninformative stopped caps in [[multiagentelbo-2026-10-09-compact-raw-history]] are unchanged. Dense endpoint covariance, full retained R/model and source/history costs remain charged; no compact network-size/depth codec, regular Chapter 11 class or common-measure decoder is established.

## Preserved failure, separate repair and replay

The producer completes once from `fcad20b4334a6e42d5b886e62eaffac52b254f8a`. The first reader stops before moment comparisons because its orchestration asks an upstream reader to hash its own completed receipt as an input. [The repair record](https://github.com/cdenn016/MultiAgentELBO/blob/0b7bdbbc7a93ec7aa23cff4b3e020c6b9997f63c/docs/research/2026-10-03-latent-link-rg-plan/R3-FIXED-PREFIX-READBACK-REPAIR.md) removes only that impossible self-input check, retaining the complete package manifest and explicit receipt digest binding. The mathematical helpers, producer arrays, supports, moment/scalar tolerances and original archived checker stay unchanged. The named failure journal remains separate from the five mathematical archives. No producer rerun occurs and the failed receipt is not counted as a passing readback.

The immutable first failed receipt is 2,666,244 bytes, SHA256 `f6c5de54c9178068b88f373f394b3cf230cc68d5c463d176f9d9309eeb93f073`; its 392-byte failure archive has SHA256 `c33679db3a72d115f9ba7fdfd7c1e671958f81e2c81f1179c6d8c77a9c0503a9`. The separately published corrected reader executes once from `0ab1f1c60a162a49dc8654d11ae938586ed668c1`, using positive Wick-chaos squared-shift variances rather than the producer's cumulant/Bell route. It passes 8,310 comparisons over 3,685,443 entries, maximum absolute discrepancy 2.117582368135751e-22. Five prior tiny JUnit cases remain passing, producer two/.294 seconds and reader three/.125, zero failures/errors/skips, without reruns. Original collection/syntax receipts remain preserved separately.

[The result record](https://github.com/cdenn016/MultiAgentELBO/blob/0b7bdbbc7a93ec7aa23cff4b3e020c6b9997f63c/docs/research/2026-10-03-latent-link-rg-plan/R3-FIXED-PREFIX-NATIVE-ERROR-RESULTS.md) reports producer time 3.571586 seconds/peak 90,619,904 bytes and repaired reader 4.556210 seconds/peak 101,240,832 bytes. Five mathematical NPZs carry 17,068,280 logical bytes and occupy 11,067,106 compressed bytes; direct input/source snapshots use 52,541,166/143,499 bytes. Root matches 13 input, 15 original source, two corrected source and 1,421 passing-reader bindings. The canonical replay at `MultiAgentELBO/artifacts/gaussian-fixed-prefix-native-error/r3-n512-fixed-prefix-native-error-20261009/` contains 39 files and 71,027,506 bytes with exact count/length/SHA256 parity. Both complete linked prior coefficient/filter packages keep exact canonical parity without redundant copying, retaining all fine initialization/model/probe/history charges.

Runtime producer receipt is 20,367 bytes, SHA256 `c4217e3406561d4e4d8c7d46ec602ecf277b24722b3d504e04df65b1b4926344`; separate repaired receipt is 4,555,738 bytes, SHA256 `f7752a91458000970b74fc928c9a4b0e7837e88270266190dc6ffef524a49a6a`. Package manifest is 11,930 bytes, SHA256 `0300c2fd34b97e339ace846617690959c9da3f31020fc0a8f2433f93bd9bca28`. Runtime snapshots preserve exact original bytes separately from Git newline-normalized tracked copies. Canonical Desktop code bindings at result merge `0b7bdbbc7a93ec7aa23cff4b3e020c6b9997f63c` are: actual-law proof 10,663 bytes/SHA256 `7df81c373975a1fe6deffcce3771016d5dc53f64dd8ff371f6a6715ea57bde65`; contract 10,111/`c9a48f5652c61fd76b26ef22cbc369b621997f377c182d467c249c0514259eea`; repair 4,007/`10bb127010257a858eadd45cf9de7b8b8dc660602842ab45e4fe3399a92bb2c6`; result 5,352/`a13a64b4cdd400ec50ff4e0b15e10cb00515e48d4b89cf5689df7298d7a8f1e1`; bounded recurrence 15,686/`e2ade5720c3d3fcfd157c8d1b567415e59f84b226ef0c174e6a0fc4c7ee02e01`.

## Relevance to this research

This advances [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] from four conditional diagnostics to a held-fixed-old-history actual-law next-observation allowance, while isolating a bounded accumulated-history target. It preserves the original fine dynamics and explicitly distinguishes the Gaussian-projected hybrid's downward law. Bounded forecast/decoder losses contract under common kernels; unbounded log scores or forces require separate moment hypotheses.

[[Gauge-Theoretic Multi-Agent VFE Model]] still requires useful hybrid-history expectation control, nonlinear posterior integration/assimilation, native episode and continuous regular closure, compact size/depth limits and endogenous formation. No new empirical hybrid-history budget, field, trajectory or GPU run is recorded by the recurrence or this intake. All four RG gates stay open, the full goal remains active, the GPU remains user-owned and the 144-case CUDA grid remains unrun.
