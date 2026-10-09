---
type: run
title: "First deterministic fixed-H2 projected-history expectation enclosure"
aliases: ["N512 projected expectation envelope"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# First deterministic fixed-H2 projected-history expectation enclosure

Codex (2026). *First deterministic fixed-H2 projected-history expectation enclosure*. MultiAgentELBO [PR240](https://github.com/cdenn016/MultiAgentELBO/pull/240) publishes source commit 6abc3d0b213d3d724d414e27952b8a678af3ee74 at merge 9c91b2f57470361b44b97c3d58b21ffdb8611e3a. [PR241](https://github.com/cdenn016/MultiAgentELBO/pull/241) publishes outcome commit e5d8a0fed750554080a19aed9588f362c9342934 at merge baa4b7182d3c18daee1b7a5f329ed3b167728414. The once-run calculation completes a nontrivial deterministic computational expected-cost enclosure at one fixed H2, following [[multiagentelbo-2026-10-09-selected-block-cost]]. Its approximately 0.10 TV ceilings remain loose and exclude uncertified arithmetic; they do not meet the complete RG accuracy objective.

```bibtex
@misc{codex2026projectedexpectationenvelope,
  author = {Codex},
  title = {First deterministic fixed-H2 projected-history expectation enclosure},
  year = {2026},
  howpublished = {MultiAgentELBO source PR240 and results PR241},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/241}
}
```

## Fixed target, event and original law

The [contract](https://github.com/cdenn016/MultiAgentELBO/blob/9c91b2f57470361b44b97c3d58b21ffdb8611e3a/docs/research/2026-10-03-latent-link-rg-plan/R3-PROJECTED-EXPECTATION-ENVELOPE-CONTRACT.md) bounds mu_a=E_(bar_H3|H2) a1, where a1 is the bounded causal local cost under the declared projected-hybrid reference starting from the original fixed H2. It does not use the saved H3 cost to choose an event or replace this expectation. The fixed network has 512 agents, matter dimension 2, 1024 real GL(2) primitive reversal pairs, three observed/four generator slices and selected slice 2. Mass 16, h=1/40000, T=.05, the literal positive q9 rule, original directed hard source supports/copies/sender terms and the supplied 128-parent forest remain unchanged. Known initialization, full retained R/model/history and original mean-and-precision readout remain part of the scope.

The predeclared event intersects the r=7.5 box for all 97,280 raw physical Fisher normal coordinates, the u=7.5 marginal-standard-deviation box for 1024 old physical hidden coordinates, and the next physical standardized Gaussian norm event with d=1024 and t=log(10^6). The adaptive rank-256 projector preserves pathwise norm contraction but does not reduce the Gaussian tail dimension. The event complement is charged by

$$
\beta=\min\left(1,2(97280)e^{-r^2/2}+2(1024)e^{-u^2/2}+e^{-t}\right).
$$

No innovation is truncated or conditioned on success. The original root/free embedding and complete within-parent physical covariance give fixed mminus=F2 m2+d2 and P3=F2 bar_C2 F2^T+Q2. These physical covariances are distinct from belief Sigma. Complete old chart B/b/c point values and coordinate perturbation bounds propagate through the original source-softmax, generator mean/SPD and hidden-independent matter-SPD proposals. This evaluates enclosures of those maps without drawing noise, proposing a new state, constructing a field or inspecting a future observation.

All literal weighted signed moment/response ceilings retain exact source/copy incidence, uniform support unions, source mixing, symmetric precision trace pairing and native chart preconditioning. Their sufficient guard a_es<=sqrt(8) covers both implemented degree-24 guards. Complete supportwise physical covariance and mean controls feed Gamma_upper; complete parent-diagonal deletion and receiver/sender majorants feed Koff and the correlation controls. With rho_op<1, the information and bounded-cost enclosures are

$$
\overline I=\frac{\rho_F^2}{4(1-\rho_{op})},
a_E=\min\left(1,\min(1,\sqrt{2\overline\Gamma})+\min(1,\sqrt{\overline I/2})\right),
\overline\mu=a_E+(1-a_E)\beta.
$$

The contract would preserve a first guard/correlation failure and charge the event cost one, without retuning or retry. Neither failure occurred. Under the real-arithmetic assumptions, inherited startup e_start and fixed first-step a0 give min(1,e_start+a0+mu_upper) for joint history and min(1,2e_start+2a0+mu_upper) for expected downward TV. Their printed float64 realizations are computational ceilings rather than outward-rounded exact-law certificates.

## First outcome and limiting scope

The [results](https://github.com/cdenn016/MultiAgentELBO/blob/baa4b7182d3c18daee1b7a5f329ed3b167728414/docs/research/2026-10-03-latent-link-rg-plan/R3-PROJECTED-EXPECTATION-ENVELOPE-RESULTS.md) report that all 1024 primitives pass: maximum sample-norm upper is 2.5024802778977286 below sqrt(8), and discriminant upper is 3.1312037706335465 below four. The 250 independent comparisons over 2,467,978 entries pass with maximum observed difference 3.730349362740526e-14.

| Quantity | Computational value |
| --- | ---: |
| Uniform Gamma_upper | .004763026171473923 |
| rho_op | .000266925404843467 |
| rho_F | .005827117118848697 |
| Information_upper | 8.491089966821841e-6 |
| Event cost a_E | .09966196967632546 |
| Event complement beta | 1.1199689566310632e-6 |
| Projected-history expected-cost mu_upper | .0996629780269699 |
| Inherited startup | .002025898793124062 |
| Fixed first-step a0 | .001542794125569835 |
| Two-transition joint-history TV upper | .1032316709456638 |
| Expected downward-TV upper | .10680036386435769 |

These are deterministic expectation-enclosure calculations, not sampled means, the observed two-cost sum or a saved-point maximum. The preserved support-control postprocessing separates Gamma into source .00045787237796737496, generator mean .000030100963507525893 and generator covariance .004275052829999022. Their respective linear contributions are .00045786725427239495, .00003010076950091854 and .004275024424906913; quadratic trace/variance contributions are much smaller. This locates the sufficient linear norm envelope as a concrete remaining looseness. It does not show that actual-law error is of that size.

The next baseline-geometric/relative-coefficient construction is under derivation and remains unpublished and unrun. It is not a completed or validated result here. A tighter computational ceiling and then explicit input/matrix-function/solve/response/contraction rounding allowances are needed before a certified quantitative claim. TV alone controls no unbounded original-record log loss and proves no 0.01-nat criterion. Actual nonlinear filtering, native episode-posterior or continuous Fisher path accuracy, Chapter 11 regular/common-measure closure, uniform growing size/depth and endogenous formation remain separate. All four RG gates remain open; the GPU remains user-owned and the 144-case CUDA grid unrun.

## Execution, resources and byte provenance

The producer and independent reader each completed once from clean published 9c91b2f57470361b44b97c3d58b21ffdb8611e3a. Producer time/peak were 4.340260199969634 seconds/576,241,664 bytes; reader time/peak were 4.27643219998572 seconds/170,438,656 bytes. The reader imports none of the new producer/driver-box/coefficient implementations and separately reconstructs dense physical embedding/covariance, driver, chart and scalar formulas. Sparse factors, complete covariance restrictions, decoded inputs, coefficient/node arrays and dense validation work are charged. This is not a controlled timing comparison with the selected-only evaluator.

Fifteen NPZ archives contain 11,983,054 logical array bytes and 1,360,137 compressed bytes. Direct input/source snapshots contain 7,114,528/265,979 bytes. The [package manifest](https://github.com/cdenn016/MultiAgentELBO/blob/baa4b7182d3c18daee1b7a5f329ed3b167728414/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-projected-expectation-envelope-package.json) records 20 direct input, 27 source and 2894 reader bindings, with exact canonical copy parity for all 64 replay files/10,430,568 bytes. Complete linked selected-cost and live packages also have exact canonical parity: 95 files/30,451,854 bytes and 150 files/74,186,084 bytes. Their historical executing source revisions and reader bindings remain linked rather than relabeled or copied into a new transitive tree.

Eight distinct tiny cases pass across four machine XMLs, with zero failures/errors/skips: driver-box three cases/.270 seconds, coefficient-envelope one/.292, producer two/.236 and reader two/.341. Preserved initial/first-attempt receipts remain separately available; the root producer fixture's first attempt passed and is not called an initial red. Passing fixtures were not rerun after unchanged arithmetic. No scientific failure, retry, history, original force/response construction, noise, proposal, readout, sampling choice, GPU allocation, model/default change or manuscript edit accompanied the enclosure.

| Read canonical artifact | Bytes | SHA256 |
| --- | ---: | --- |
| Contract | 8054 | 0698307fbe92e7500292fac79332c82a0d7d6aee4a49639a09bdfa7f146503ea |
| Results | 4688 | 5f1176a4c3b8fea3f256e15e45e64277805299b5f87efb7a3bc620ed3143cc4e |
| Runtime producer/result receipt | 42370 | 26e997413d74d669a693171a8797941092a5537e83fdf3c88e0822a89757ffb4 |
| Runtime independent reader | 1647554 | 545a979260770921808106c508e4b52b649ee3f9babe498bba2c125d40e08518 |
| Replay manifest | 15695 | 6e4ec9720d916b1b7edaa3acfa3301c7f438f13f4f21e5a4713a7ca00f181357 |

## Relevance to this research

[[Renormalization-group flow of beliefs]] now has a completed deterministic computational bound on one projected-history expectation, rather than only observed local costs. [[Gauge-Theoretic Multi-Agent VFE Model]] retains its finite fixed-H2, original-law and arithmetic qualifications. [[Staged hierarchy formation and RG composability]] keeps the bounded reference-history comparison distinct from nonlinear native assimilation, unbounded predictive loss and growing hierarchy closure. The original generated path remains [[multiagentelbo-2026-10-09-live-block-parent]], and [[multiagentelbo-2026-10-09-selected-block-cost]] remains the prior immutable dependency/conditional-proof intake.
