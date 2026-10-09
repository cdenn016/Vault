---
type: run
title: "First live N512 projected parent-block Gaussian path and causal projection ceiling"
aliases: ["N512 two-transition live block-parent admission"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# First live N512 projected parent-block Gaussian path and causal projection ceiling

This intake records [MultiAgentELBO PR236](https://github.com/cdenn016/MultiAgentELBO/pull/236), frozen source merge `405c001960aef7f59ed0a192e5e84cac4443b362`, and [PR237](https://github.com/cdenn016/MultiAgentELBO/pull/237), result merge `a0233aa1848582f6c38c55237966dec4e86e2c16`. One newly generated projected-hybrid path completes exactly two transitions from the held-fixed old H2. The producer and independent reader each complete on their first scientific invocation. A causal Gaussian projection proof supplies the next-projection ceiling before its new readout arrives. The observed two-cost sum remains descriptive; it does not evaluate the required projected-history expectation.

```bibtex
@misc{codex2026liveblockparent,
  author = {Codex},
  title = {First live N512 projected parent-block Gaussian path and causal projection ceiling},
  year = {2026},
  howpublished = {MultiAgentELBO research records, pull requests 236 and 237},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/237}
}
```

## Declared path and unchanged original kernel

[The frozen contract](https://github.com/cdenn016/MultiAgentELBO/blob/a0233aa1848582f6c38c55237966dec4e86e2c16/docs/research/2026-10-03-latent-link-rg-plan/R3-LIVE-BLOCK-PARENT-CONTRACT.md) continues [[multiagentelbo-2026-10-09-block-filter-screen]] at c_* with N512, real GL(2), 1024 original primitive reversal pairs, generator dimension four, three observed matter/source slices, four generator slices, selected slice two, literal positive q9, mass 16, h=1/40000 and T=.05. The supplied first forest has 128 parents, four agents per parent, weight .25 and six free coordinates per parent. H2 to H3 and H3 to H4 are inference-clock transitions on the same original three-episode record prefix. They introduce no new episode data, locality/source protocol, reward model, forest or scientific dynamics.

At each transition the wrapper regenerates every current retained-state coefficient, complete receiver/sender K/h0, signed moments/responses and all 15,872 affected source/generator-mean/generator-covariance chart rows. The current block endpoint mean is only a coefficient anchor. A draw from the complete within-parent Gaussian law supplies the hidden selected mean to the unchanged complete raw Fisher proposal; it is not replaced by an expected force. All five original noise families, source row gauge and natural preconditioning remain. Both updated generator mean and full precision enter the persistent probe and original rooted readout. The next call carries the new retained R, omitting the hidden selected mean, and its newly conditioned/projected Gaussian block state.

The selected-mean neutral Gaussian predictor uses the complete sparse physical P and global V solve. Only after conditioning at the actual generated A/M does projection preserve every complete parent free-coordinate marginal while discarding between-parent covariance. Root reconstruction retains cross-child and root/free correlations. No per-parent approximation replaces the global V solve, and no clipping, covariance floor, jitter, source floor or smaller step repairs a failure. A dense neutral Gaussian endpoint is carried separately at the same block-generated retained history for validation; it never supplies the operational block covariance or fine draw. It is neither an independently generated full-hybrid path nor the actual nonlinear filter.

The single NumPy PCG64 seed is 2026100904. Each step draws its 128-by-6 block innovation before the complete original matter-mean, matter-covariance, source, generator-mean and generator-covariance standard-normal arrays. The original 98,048-coordinate first-transition tuple, including hard-zero source positions, is preserved for replay. No success event, hidden generated mean, later-prefix chart observation or future episode enters the causal cost. This is one generated path, not independent-network statistics or a history-expectation estimate.

## Uniform causal Gaussian projection proof

[R3-CAUSAL-BLOCK-PROJECTION-BUDGET.md](https://github.com/cdenn016/MultiAgentELBO/blob/a0233aa1848582f6c38c55237966dec4e86e2c16/docs/research/2026-10-03-latent-link-rg-plan/R3-CAUSAL-BLOCK-PROJECTION-BUDGET.md), equations (1)-(8), fixes a positive definite original neutral predictor N(m,P) and the same disjoint parent partition. For every block-local readout with invertible root coefficient, the map from each parent's fine coordinates to its free coordinates and observed parent is invertible. The product of predictor parent marginals has total correlation

$$
I(P)=\frac12\left(\sum_a\log\det P_{aa}-\log\det P\right).
$$

The relative-entropy chain rule followed by the product-projection identity splits I(P) into retained-observation total correlation, conditional free-coordinate projection KL and the nonnegative information that other parents' observations deliver to each parent. Gaussian conditional covariance is observation-value independent. Therefore

$$
K_{proj}(A)\leq I(P)
$$

holds for every admitted block-local A and every observation value. This is a conditional Gaussian result with explicit positive-definiteness and root-map assumptions. It does not identify the original hidden law conditioned on an adaptive readout with that Gaussian or assume adaptive geometry independent of the hidden mean. Its uniformity permits the neutral-reference comparison at each original realized readout.

The next-projection TV ceiling is thus current-prefix measurable, delta_star=min(1,sqrt(I(P)/2)). The original chart-shift ceiling is c=min(1,sqrt(2 Gamma_Q)), retaining quadratic trace bias and full physical same-parent covariance. Both are fixed at the old prefix, so the joint-level local cost a_j=min(1,c_j+delta_star,j) is valid. This differs from capping an observation-dependent conditional error inside an expectation. Global prediction/conditioning and original forces are unchanged. The causal proof supplies no uniform growing-size/depth, overlapping/soft partition or continuous-native-law claim.

## First computational outcome and charged startup

[R3-LIVE-BLOCK-PARENT-RESULTS.md](https://github.com/cdenn016/MultiAgentELBO/blob/a0233aa1848582f6c38c55237966dec4e86e2c16/docs/research/2026-10-03-latent-link-rg-plan/R3-LIVE-BLOCK-PARENT-RESULTS.md) reports these computational quantities. The KL values are in nats and refer to the declared Gaussian comparisons.

| Quantity | H2 to H3 | H3 to H4 |
| --- | ---: | ---: |
| Complete block-law Gamma_Q | 8.956654740597e-7 | 1.343295537467e-6 |
| Causal predictor I(P), independent eigenvalues | 8.355020001850e-8 | 1.145186138859e-7 |
| New conditional projection KL, independent eigenvalues | 6.276884880731e-8 | 7.944924943858e-8 |
| Full neutral endpoint to compact endpoint KL on the same history | 1.412167918059e-7 | 3.177455498958e-7 |
| Old-prefix local joint TV computational ceiling a_j | .001542794126 | .001878375789 |

The inherited fixed-H2 error in [[multiagentelbo-2026-10-09-fixed-prefix-native-error]] and old Gaussian projection are charged by ordinary TV triangle:

$$
e_{start}=\min\left(1,\min\left(\sqrt{K2/2},\sqrt{C_\chi}/2\right)+\sqrt{K_{proj,old}/2}\right).
$$

Startup is .002025898793. At this held-fixed H2 the first-transition joint and expected downward conditional TV computational ceilings are .003568692919 and .005594591712. The latter uses the retained-marginal preservation of the final projection. No KL triangle or zero-startup assumption is used. These ceilings retain input, finite-q9, degree-24 response, coefficient, matrix-function, solve, norm, determinant and contraction exclusions; floating readback does not certify a mathematical upper endpoint.

The observed two-cost sum is .003421169914 and its sum with startup is .005447068708. Neither is a two-step actual-law error bound or an estimate of E_barH3[a1(H3)]. The full-neutral-to-compact KL also remains a same-history Gaussian validation value, not actual posterior error.

Independent reconstruction passes all 537 comparisons over 18,530,551 entries, maximum discrepancy 1.27675647831893e-11. It reconstructs current NumPy fields, signed responses, local polynomials, original raw-noise proposals, original forests, physical-support trace moments, original-noise QR and whitened eigenvalue KL. Frozen field/mean/covariance/scalar allowances are 1e-8/1e-10/1e-12/1e-9, with exact structural identities. The reader checks determinant information against eigenvalue information, then the TV square root from the checked nonnegative saved scalar and separately reports eigenvalue-derived TV. Poor square-root conditioning near zero remains distinct from interval certification.

Nine pre-outcome tiny fixtures pass in six preserved XML receipts with zero failures/errors/skips. Initial collection and wrapper dimension/noise-field failures remain separate source evidence. There is no scientific failure, retry, producer rerun or passing-fixture rerun. This intake executes no tests or science.

## Provenance and resource costs

The producer/readback elapsed times are 800.636265/279.538723 seconds, with cumulative process peaks 1,699,819,520/442,245,120 bytes. Both use isolated Anaconda CPU float64, sequential MKL and one math thread; no GPU allocation occurs. Sixty numerical archives contain 120,912,350 logical bytes and 48,888,284 compressed bytes. Direct input/source snapshots occupy 22,881,079/720,395 bytes. All 18 direct inputs, 70 executing sources and 2,700 reader bindings remain recorded. Root copies and rehashes all 150 replay files totaling 74,186,084 bytes into the actual canonical Desktop code folder with exact set/length/hash parity; all three linked packages also retain canonical parity without another ancestry copy.

The operational Gaussian mean/block payload remains 43,008 bytes, compared with 8,396,800 bytes for full physical Gaussian m,C. Complete retained R, model, records, geometry/probe, original rule, current dense K, moment/response construction, sparse embeddings/P/V/LU fill and dense oracle work are additional. This is no total-codec, uniformly sparse, linear-work or growing-size/depth memory theorem.

The replay root is `MultiAgentELBO/artifacts/gaussian-live-block-parent/r3-n512-live-block-parent-20261009/`. Runtime producer receipt is 62,328 bytes/SHA256 `7959daa10ccc71e8b21a7a6efd5927ed96e23ab46d8b6a9ebe27ad54d9c60905`; independent receipt is 1,633,998/`3aa067d07a752117ebe0b5604cebd541cb5a29d8543e5716e92cf77cfa09d179`; package manifest is 32,129/`ae2374a5b06c18090e32ba8072e4d6c77bcc107d897765eedf3160005c792aab`. Canonical Desktop bindings at result merge `a0233aa1848582f6c38c55237966dec4e86e2c16` are results 5,237/`bbd20de34a980d0ed7322f8275547efab0fd56890492e5d24cafd99a314be315`, contract 15,509/`0b9a565852886faae0ca71f5e598d4d019f5bf8ebeb4b7f151db925d65d8360d`, causal proof 11,919/`482ff449e79cea9e37a7541701504be5588df1026666b0056f62acf63ad4a07a`, and expectation design 22,529/`49301a196b7a2dfc5d65e9fe6a76d1576b70b421e43b95a17ef39aacdfa0fcc7`. Runtime executed snapshots retain their bytes separately from Git newline-normalized checkout files.

## Relevance to this research

[R3-PROJECTED-HISTORY-EXPECTATION-DESIGN.md](https://github.com/cdenn016/MultiAgentELBO/blob/a0233aa1848582f6c38c55237966dec4e86e2c16/docs/research/2026-10-03-latent-link-rg-plan/R3-PROJECTED-HISTORY-EXPECTATION-DESIGN.md) locates the next quantitative dependency at mu_a=E_barH3[a1(H3)] after the same held-fixed H2. A pathwise adaptive Gaussian projector bounds the reference mean without asserting independence, and the projected physical covariance is bounded by the predictor's complete parent diagonal blocks. Declared compact raw-driver and Gaussian-coordinate events could combine uniform selected-cost/correlation envelopes with a charged complement probability. Those numerical envelopes and useful accuracy values remain uncomputed; finite compactness alone proves no smallness.

The design also traces the exact cancellation of chart constants in f_r(x)-f_r(m). It permits a selected-slice cost-only evaluation seam while preserving original record responses, source whitening, both generator preconditioners and complete sender terms. That seam would evaluate a cost after generation, not replace the full original proposal force. Its separate implementation and benchmark are not results in this batch. A possible fixed 32-trial bounded-mean fallback remains unselected and unregistered; even its zero-cost best-case confidence ceiling is about .08937, so it cannot establish .01-scale expectation accuracy.

This advances [[Renormalization-group flow of beliefs]], [[Staged hierarchy formation and RG composability]] and [[Gauge-Theoretic Multi-Agent VFE Model]] from paired saved updates to one causal evolving projected-hybrid path. Useful controlled history expectations, original-record forecasting, actual nonlinear posterior assimilation, native episode and continuous Fisher equivalence, Chapter 11 regular/common-measure closure, uniform size/depth and endogenous formation remain open. The original unrestricted entropy divergence and uninformative stopped-TV outcomes retain their separate scopes. All four RG gates remain open and the autonomous goal active; the GPU stays user-owned and the 144-case CUDA grid remains unrun.
