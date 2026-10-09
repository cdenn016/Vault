---
type: run
title: "Same-event relative-Cholesky expectation refinement"
aliases: ["N512 relative expectation envelope"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Same-event relative-Cholesky expectation refinement

Codex (2026). *Same-event relative-Cholesky expectation refinement*. MultiAgentELBO [PR246](https://github.com/cdenn016/MultiAgentELBO/pull/246) publishes executing source 6bccc881a37429d148cc72635ef66c92cf45ba84. [PR247](https://github.com/cdenn016/MultiAgentELBO/pull/247) publishes the completed result at merge 74a85a1cc5e85a653cafbc8cc2e73f29a5b2e922. This once-run deterministic operation continues [[multiagentelbo-2026-10-09-baseline-expectation-envelope]] by bounding relative covariance factors along the actual original exponential proposal path and replacing only the affected coefficient-bound contributions. The computational fixed-H2 expected-cost ceiling decreases from .0235061313400429 to .00888041985169924 on the same event. This is a sufficient real-arithmetic enclosure, not an outward-rounded exact-law certificate, measured history expectation or completed RG accuracy result.

```bibtex
@misc{codex2026relativeexpectationenvelope,
  author = {Codex},
  title = {Same-event relative-Cholesky expectation refinement},
  year = {2026},
  howpublished = {MultiAgentELBO source PR246 and results PR247},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/247}
}
```

## Original law and relative-factor construction

The [frozen contract](https://github.com/cdenn016/MultiAgentELBO/blob/6bccc881a37429d148cc72635ef66c92cf45ba84/docs/research/2026-10-03-latent-link-rg-plan/R3-RELATIVE-EXPECTATION-ENVELOPE-CONTRACT.md) retains 512 agents, matter dimension two, 1024 original real GL(2) reversal-pair primitives, generator dimension four, mass 16 and the literal positive q9 rule with 6,561 nodes. The same h=1/40000, T=.05, selected slice two, old prefix two, supplied 128-parent forest and six free coordinates per parent remain. Hard source support, every sender/reversed/parallel record, source reference choices, chart IDs, native preconditioning and full retained state/model/history are preserved. Complete physical parent covariance is distinct from belief Sigma.

The event remains r=u=7.5, t=log(10^6), d=1024, Gaussian norm radius approximately 35.9098 and all 97,280 physical proposal coordinates. Adaptive projection does not reduce the Gaussian tail dimension. The complement is charged one, giving beta=1.1199689566310632e-6. No advanced state, future history, observed maximum or outcome selects or retunes this event.

The [relative-factor derivation](https://github.com/cdenn016/MultiAgentELBO/blob/6bccc881a37429d148cc72635ef66c92cf45ba84/docs/research/2026-10-03-latent-link-rg-plan/R3-RELATIVE-CHOLESKY-ENVELOPE.md) follows the original covariance path

$$
\begin{aligned}
C(t)&=L_0\exp(tE)L_0^T,& L(t)&=\operatorname{chol}C(t),\\
S(t)&=\operatorname{chol}(C(t)^{-1})^{-T},& O(t)&=S(t)^{-1}L(t).
\end{aligned}
$$

Here L0 is the lower covariance Cholesky factor. The supplied original driver box gives a symmetric exponent center Ecenter and a Frobenius radius eta. Put g=norm_F(Ecenter)+eta and rho=norm_op(Ecenter)+eta. Orthogonal conjugacy of the normalized covariance derivative and cancellation of the rotation's symmetric parts give

$$
\begin{aligned}
\max(\|L(1)-L(0)\|_F,\|S(1)-S(0)\|_F)&\leq \frac{g}{\sqrt{2\lambda_{\min}(\Lambda_0)}}I(\rho),\\
\|O(1)-O(0)\|_{op}&\leq\min(2,g).
\end{aligned}
$$

$$
I(\rho)=\begin{cases}\operatorname{expm1}(\rho/2)/(\rho/2),&\rho>0,\\1,&\rho=0.\end{cases}
$$

The original noncommuting factor order, Frobenius-radius hypothesis and complete natural paired directions are retained. The consumer takes each minimum with its prior valid factor ceiling. Both endpoint degree-24 response approximation allowances and the inherited endpoint-domain guards remain charged; no response approximation error is subtracted as a common cancellation.

The [coefficient-refinement derivation](https://github.com/cdenn016/MultiAgentELBO/blob/6bccc881a37429d148cc72635ef66c92cf45ba84/docs/research/2026-10-03-latent-link-rg-plan/R3-RELATIVE-COEFFICIENT-REFINEMENT.md) uses the completed baseline decomposition into an unchanged nonnegative term and a moment-dependent term. It computes

$$
\begin{aligned}
b_{new}&=b_{baseline}+(d_{new}-d_{old}),\\
0&\leq b_{new}\leq b_{baseline}.
\end{aligned}
$$

This inequality is conditional on the exact same-event decomposition and monotonic factor/response bounds. It subtracts explicit sufficient-bound contributions, not actual coefficient norms. Source inverse-whitening changes, source reference/prefix maxima, beta changes and every incident generator record remain. Old signed B0/b0, integer IDs, complete supports and supplied ordering are preserved without rebuilding response banks. The numerical diagnostic records minimum recovered unchanged contribution zero and maximum bound increase zero, with 64-machine-epsilon scaled allowance and no clipping or repair. That diagnostic supplies no arithmetic interval certificate.

The unchanged physical-geometric helper uses archived predictor P3 in CSR and complete eight-coordinate D3,max parent blocks, including cross-child entries. Signed old rows are matched by original IDs and padded into their complete uniform supports. Weighted nuclear, Frobenius and linear majorants retain trace bias and the adaptive projection shift. Gamma_relative_geometric is half the sum over all 1,536 source, 4,096 generator-mean and 10,240 generator-covariance rows. The predeclared selection is min(raw relative-geometric Gamma, saved baseline Gamma) after the inherited guard passes; failed guards charge unit cost before any refinement.

## First outcome and scope

The [published result record](https://github.com/cdenn016/MultiAgentELBO/blob/74a85a1cc5e85a653cafbc8cc2e73f29a5b2e922/docs/research/2026-10-03-latent-link-rg-plan/R3-RELATIVE-EXPECTATION-ENVELOPE-RESULTS.md) records one producer and one independent reader, both complete. All 1024 primitives are refined and all required guards pass. All 257 comparisons over 2,547,381 entries pass, with maximum absolute discrepancy 1.1102230246251565e-16. The reader imports none of the new producer, relative-factor or coefficient helpers: it derives the factor controls, directly differentiates triangular factors in original native directions, independently replaces moment-dependent terms and uses the earlier independent physical geometry and scalar budget. Its frozen tolerance is 1e-8 absolute plus 1e-11 relative, with exact IDs, hashes and byte counts.

| Quantity | Computational value |
| --- | ---: |
| Raw Gamma_relative_geometric, selected | .0000232482744578688 |
| Saved Gamma_baseline | .00022993469831728624 |
| Information_upper, unchanged | 8.491089966821841e-6 |
| Event complement beta, unchanged | 1.1199689566310632e-6 |
| Expected-cost mu_upper | .00888041985169924 |
| Inherited startup, unchanged | .002025898793124062 |
| Fixed first-step a0, unchanged | .001542794125569835 |
| Two-transition joint-history TV upper | .012449112770393136 |
| Expected downward-TV upper | .016017805689087034 |

Source, generator-mean and generator-covariance Gamma contributions are 1.1817759211656644e-5, 5.232370915718284e-7 and 1.0907278154640328e-5. Source and covariance contributions are now comparable in this sufficient enclosure; their proportions do not establish a mechanism or size/depth limit. The next quantitative obligation is accumulated cost along independently evolving projected-hybrid histories, rebuilding complete current-state original coefficients before each transition. The fixed-H2 value cannot be reused unchanged at later random old histories.

These values bound the same conditional projected-history expectation under the stated real-arithmetic assumptions. The reduction reflects a tighter sufficient inequality, not changed dynamics, new histories, a measured error or integrated nonlinear posterior. Input, Cholesky/solve/norm/matrix-function/response/contraction rounding remains uncertified. TV controls no unbounded original-record log score and proves no R0 0.01-nat criterion. Useful accumulated random-history and multihorizon control, continuous Fisher accuracy, Chapter 11 regular/common-measure closure, uniform growing size/depth and endogenous formation remain unresolved. All four RG gates stay open; the GPU remains user-owned and the 144-case CUDA grid unrun.

## Resources, first attempts and immutable provenance

The isolated CPU float64 one-thread producer runs 19.802193099982105 seconds with peak 103,022,592 bytes; the reader runs 32.0615672999993 seconds with peak 129,462,272 bytes. Nine NPZs retain 3,576,930 logical array bytes and 1,301,576 compressed bytes. Direct input/source snapshots use 6,092,347/267,550 bytes. Input numeric arrays use 17,050,294 bytes; relative-factor, old/new dynamic, physical CSR, local geometry/cache and transient/process costs are recorded separately. Complete R/model/history/geometry and linked ancestry remain additional storage. This is not a complete compact codec or a controlled speedup comparison.

The [producer receipt](https://github.com/cdenn016/MultiAgentELBO/blob/74a85a1cc5e85a653cafbc8cc2e73f29a5b2e922/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-relative-expectation-envelope-result.json), [reader receipt](https://github.com/cdenn016/MultiAgentELBO/blob/74a85a1cc5e85a653cafbc8cc2e73f29a5b2e922/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-relative-expectation-envelope-readback.json) and [replay manifest](https://github.com/cdenn016/MultiAgentELBO/blob/74a85a1cc5e85a653cafbc8cc2e73f29a5b2e922/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-relative-expectation-envelope-package.json) bind 19 direct inputs, 27 current sources and 3,103 reader paths. The complete replay package has 57 files/9,418,075 bytes with exact canonical Desktop parity. The completed baseline 54-file package and its linked original 64-file, natural 44-file and live 150-file ancestry remain verified through the cached path union, without transitive recopying. The replay root is `artifacts/gaussian-relative-expectation-envelope/r3-n512-relative-expectation-envelope-20261009`.

Fresh analytical calculations charge 6,718,464 node-primitive pairs, 94,058,496 paired tangent-bound coordinate entries, 33,592,320 scalar exponential entries and 1,024 relative-factor expm1 entries. No new histories, noise tuples, proposals, readouts, full-history fields, selected signed moments, original forward moments, response banks or matrix exponentials are evaluated. The later host crash affected unpublished report/intake work only. Post-crash read-only hashing recovered exact parity of all 57 saved files; no scientific rerun, retry, event adjustment, model/default, host-setting or manuscript change occurred.

Nine distinct new tiny cases pass across four source-bound machine XMLs with zero accepted failures/errors/skips: relative factors three/.274 seconds, coefficient helper two/.151, producer two/.279 and independent reader two/.336. These validate factor order, covariance derivative/rotation cancellation, zero-radius continuity, signed/parallel routing and guard behavior; they do not determine the N512 theory or a growing-network limit. Initial collection failures and the coefficient fixture's first matrix-layout failure are preserved; only that failed fixture was rerun after its input layout repair. The reader's changed inactive branch was run separately. The coefficient and reader XMLs explicitly aggregate accepted distinct cases from those invocations. No passing fixture or scientific outcome is rerun during intake.

| Receipt | SHA256 |
| --- | --- |
| Frozen contract | 851d545b0c6c4a75ebd4371d51b511d9a553ebf0aa2f5c9bc1a57d0e5fad83a7 |
| Replay manifest | 4d1202ccb9ed50c2ae6580f5474f08d6614dc4339b31708b4429bcc0d1d68fff |
| Runtime producer/result | 4dc6b31f5ccfe735724e4384342ae9496f7e08cfd896b553ece87e3ade87cb3d |
| Runtime independent reader | 7a044ddbeedb86634b3dc3018eaec77f14e07d3c18ccb7b3465a4c49a6bcdc76 |

## Relevance to this research

[[Natural gradient]] distinguishes original native paired-direction bounds from changes to the dynamics. [[Renormalization-group flow of beliefs]] records the same-event relative-factor refinement after [[multiagentelbo-2026-10-09-baseline-expectation-envelope]], preserving unchanged information/startup and a0. [[Staged hierarchy formation and RG composability]] keeps conditional projected-history control separate from accumulated multihorizon, native/regular/growing closure. [[Gauge-Theoretic Multi-Agent VFE Model]] retains the immutable baseline, [[multiagentelbo-2026-10-09-natural-expectation-envelope]] and [[multiagentelbo-2026-10-09-projected-expectation-envelope]] checkpoints without rewriting their historical facts.
