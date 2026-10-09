---
type: run
title: "Finite preparation marks, stationary path limits and moment forecast joints"
aliases: ["Preparation mark admission and stationary path identification"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# Finite preparation marks, stationary path limits and moment forecast joints

This intake continues [[multiagentelbo-2026-10-08-blockwise-budget-stationary-process]]. [Code PR205](https://github.com/cdenn016/MultiAgentELBO/pull/205), merged at `d68e5d7c8b51502d54a9c1262d578fef615753e7`, publishes three bounded R5 arguments and the four-step CPU moment-trajectory contract. [Code PR206](https://github.com/cdenn016/MultiAgentELBO/pull/206), merged at `b9e72d5d3503965ad7d58c4baf060611cf8a244a`, publishes that trajectory's first numerical outcome and the complete-component forecast adapter contract. [Code PR207](https://github.com/cdenn016/MultiAgentELBO/pull/207), result `a891fb1e9c2f0403679b72708af6c752df50268d` and merge `175ed6ecc676610fce38daa12de0e0751b8bd9fe`, publishes the adapter's first result. Root reconstructed the analytical arguments and numerical receipts. No formal adjudication state is assigned.

```bibtex
@misc{codex2026preparationpathsmoment,
  author = {Codex},
  title = {Finite Preparation Marks, Stationary Path Limits and Moment Forecast Joints},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/205},
  note = {PR205 d68e5d7c analytical results and frozen trajectory; PR206 b9e72d5d trajectory outcome and adapter contract; PR207 a891fb1e complete-bank adapter outcome}
}
```

## Almost sure observation admission for an explicit finite-preparation family

The [finite-preparation mark construction](https://github.com/cdenn016/MultiAgentELBO/blob/d68e5d7c8b51502d54a9c1262d578fef615753e7/docs/research/2026-10-03-latent-link-rg-plan/R5-FINITE-PREPARATION-MARK-ADMISSION.md) declares increasing tori $(16k)\times(32k)$, with $N_k=512k^2$, the original nearest-neighbor source/primitive/plaquette catalog and fixed homogeneous R1 preparation core. It retains K2/D4, four generator episodes, three original observed episodes, mass 16, Gaussian reference width 0.3, plaquette coefficient 0.25 and uniform four-choice source prior. The existing whole-history preparation has 256 burn-in plus 64 retained sweeps, thinning one and pCN parameter one. Ideal Gaussian/uniform inputs and exact arithmetic define a mathematical family; the registered finite calibration and its fixed seeded archives are unchanged.

Each selected primitive history is one of its initial Gaussian candidate and 320 independent whole-history proposal candidates. Its acceptance index can depend on other edges; no local dependence or mixing of the selected MH output is assumed. The maximum norm of this finite candidate set bounds both orientations of every episode's exponential. All positive exponential moments of that envelope are finite uniformly in volume, with within-history temporal correlations retained. This is a finite-Gaussian-candidate bound, rather than an exponential-moment theorem for the exact nonlinear tilted prior.

An original-record envelope keeps receiver matter, all four possible transported source terms, original noise and shared reverse primitives. Its input dependence lies within radius two, even when the selected histories/records have nonlocal MH dependence. The covariance sum gives variance at most $13V_*/N_k$. Chebyshev's inequality and the summable $k^{-2}$ volume schedule imply only finitely many excess-envelope events almost surely. Consequently the entire realized input family satisfies

$$
\sup_{k\geq1}\frac1{512k^2}\sum_{i,t<3}\|O_{k,i,t}\|^2<\infty
\quad\text{almost surely}.
$$

The bound is a finite random realization-dependent constant, not a deterministic sure tolerance. Conditioning on any realization in this probability-one event discharges the empirical observation-mark hypothesis of the native recognition snapshot theorem, with compact admissible core marks and fixed $0<T<1/4$. Neither finite-chain convergence to the nonlinear prior, a pseudorandom/floating implementation certificate nor identification of archived finite arrays with an infinite family follows. Exact nonlinear-prior-generated observation admission remains a different tail obligation.

## Stationary finite-volume paths and their local weak limits

The [stationary path theorem](https://github.com/cdenn016/MultiAgentELBO/blob/d68e5d7c8b51502d54a9c1262d578fef615753e7/docs/research/2026-10-03-latent-link-rg-plan/R5-STATIONARY-PATH-LIMIT.md) takes exact finite native population Fisher diffusions started in their own Gibbs recognition probabilities. Actual core/data marks remain frozen. A single uniform root shifts each entire path and its marks, with that root held fixed throughout inference time. Within any snapshot-convergent subsequence, further path subsequences converge on each bounded time window, consistently across integer windows.

Reversibility supplies Lyons-Zheng forward/reverse martingale control, avoiding a global drift-moment assumption. Gaussian distance cutoffs and localized source-face/data cutoffs give uniform fixed-coordinate path containment and time tightness. Regular-radius stopped-martingale passage identifies the original coordinate-local mean/covariance/source Fisher SDE and Brownian brackets, retaining all incident sender records and the original Gaussian Fisher/source-Lebesgue drifts. The limit has continuous product paths, stationary reversible time marginals equal to the chosen marked DLR snapshot and frozen limiting marks. No numerical value or convergence rate is measured by this proof.

Conditioned on the realized ideal finite-preparation family above, these stationary-start path subsequences therefore exist for its exact recognition laws. This discharges a stationary local path-subsequence obligation, distinct from arbitrary/nonstationary R0 initialization, numerical trajectory convergence or a unique selected Markov path law. It supplies no growing-horizon/low-temperature limit, mixing estimate, growing-depth retained readout, all-prefix posterior or formation/RG closure.

## Conditional identification and the unresolved native generator range

The [stationary law-identification argument](https://github.com/cdenn016/MultiAgentELBO/blob/d68e5d7c8b51502d54a9c1262d578fef615753e7/docs/research/2026-10-03-latent-link-rg-plan/R5-STATIONARY-LAW-IDENTIFICATION.md) keeps one selected snapshot $P$ and its existing closed gradient-form generator $L$. For the native cylinder functions whose local generator is square integrable, let $\mathscr D_0=\{f\in\mathscr C:\mathcal L_{\rm loc}f\in L^2(P)\}$. If the range $(\lambda-\mathcal L_{\rm loc})\mathscr D_0$ is dense in $L^2(P)$ for some positive $\lambda$, the stationary local martingales extend to the complete generator domain. Backward semigroup tests against arbitrary whole-past events then identify the entire continuous-path law with the chosen closed-form Markov realization.

That dense native range is unresolved. A form core concerns energy norm, while a generator core concerns graph norm; small-energy cutoffs do not control their local generator in $L^2(P)$. Equality of two-time conditional operators alone does not supply the whole-past Markov identity. The constructive next obligation is resolvent-range approximation for a dense collection of native cylinder targets, without changing coefficients or boundaries.

The note's exact OU example uses an expressly smaller algebra of tests flat near zero. A mixture of ordinary stationary OU paths and signed absolute-OU paths is stationary/reversible and satisfies that restricted algebra's local identities while failing the observed full-past Markov property. It isolates the inference from form-core density to generator/path identification. It is not a counterexample to the native full cylinder problem and supplies no new scientific arm or native uniqueness refutation.

## Published four-step moment-field trajectory

The [frozen trajectory contract](https://github.com/cdenn016/MultiAgentELBO/blob/d68e5d7c8b51502d54a9c1262d578fef615753e7/docs/research/2026-10-03-latent-link-rg-plan/R3-MOMENT-TRAJECTORY-CONTRACT.md) and [first result](https://github.com/cdenn016/MultiAgentELBO/blob/b9e72d5d3503965ad7d58c4baf060611cf8a244a/docs/research/2026-10-03-latent-link-rg-plan/R3-MOMENT-TRAJECTORY-RESULTS.md) retain the actual R1 simultaneous endpoint, original N512/E1024/K2 model, three observed prefix episodes, four generator episodes, mass 16, all sender terms, $T=.05$ and the same four archived finest Brownian tuples. Exactly four order-9 common-old-state `factorized_moment_fisher` fields and four positive finite proposals advanced additional inference time to $10^{-4}$. All $9^4=6561$ Cartesian nodes and actual enclosed rule constants remained present, with primitive chunk 32. No future record entered the field, and no clipping, jitter, later row repair, redraw, objective acceptance test, adaptation or retry occurred.

The explicitly saved initial transformation changed covariance by at most $3.469446951953614\times10^{-18}$ and source probabilities by at most $5.551115123125783\times10^{-17}$; precision was unchanged. These measured changes do not certify equality with the exact-real reference used by the analytical budgets. Every numerical checkpoint passed the outer-box comparisons with zero allowance, full SPD/symmetry checks, original source support and normalization. The final source mass error was $2.220446049250313\times10^{-16}$ and its smallest supported mass was .22065199487423345.

The [independent NumPy/SciPy receipt](https://github.com/cdenn016/MultiAgentELBO/blob/b9e72d5d3503965ad7d58c4baf060611cf8a244a/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-moment-trajectory-readback.json) records 445 passing comparisons over 3,748,308 entries. It reconstructs all signed moments, original costs, distinct-primitive ordered-loop defects, energy components, complete matter/source fields, supplied Brownian tuples, proposals, Itô drifts and clocks. Independent original-copy traversal checks observed-episode-2 static geometry probes at both parent depths, direct/staged composition, canonical fields and transports. Future episode 3 uses evolved generators with fresh baseline matter and original source prior. Its zero-query component is a single geometry probe, not a complete component mixture or an observed future context.

The 413 ordinary comparisons have maximum absolute discrepancy $1.0913936421275139\times10^{-11}$; the 32 selected generator mean/symmetric-precision tangent checks have maximum discrepancy $3.643909716609557\times10^{-10}$. Selected probes do not reconstruct the complete generator gradient. Root checked the executing checker against its retained snapshot, all 13 input bindings, all 22 source bindings and passing flags. [Six tiny pre-outcome tests](https://github.com/cdenn016/MultiAgentELBO/blob/d68e5d7c8b51502d54a9c1262d578fef615753e7/docs/research/2026-10-03-latent-link-rg-plan/evidence/moment-trajectory-focused.xml) remain separate routing/replay evidence: zero failures, errors or skips in 2.315 seconds, with no production-scale pytest or broader suite.

The four directed saved-state comparisons use the complete future-slice product-Gaussian parameters and one common original all-row future kernel. KL contraction bounds correlated original-record disagreement by summed primitive Gaussian KL, reported per receiver; it does not fit independent rows.

| Directed saved comparison | Original joint forecast KL upper bound per receiver |
|---|---:|
| Initial to moment final | $1.4226646635099753\times10^{-4}$ |
| Moment final to initial | $1.422622865440721\times10^{-4}$ |
| M16 finest final to moment final | $6.348455451769024\times10^{-10}$ |
| Moment final to M16 finest final | $6.348553114211253\times10^{-10}$ |

These finite endpoint comparisons describe one coupled short-window path. They do not establish M16 population field accuracy, distributional trajectory convergence or latent posterior accuracy. The ideal forecast/containment budgets retain their exact-reference and computed-field/input-arithmetic exclusions.

The producer ran once from clean `d68e5d7c` in 626.7729404999409 seconds, with 1,182,732,288-byte process peak; readback took 43.65488789998926 seconds. Producer arrays occupy 30,082,272 logical and 23,060,877 compressed bytes; Gaussian-KL replay adds 589,888 logical and 575,434 compressed bytes. Input snapshots occupy 14,543,291 bytes and source snapshots 307,935 bytes. [The package manifest](https://github.com/cdenn016/MultiAgentELBO/blob/b9e72d5d3503965ad7d58c4baf060611cf8a244a/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-moment-trajectory-package.json) retains 92 exact files totaling 38,627,640 bytes. Root copied them to the actual canonical code artifact directory and matched every length and SHA256. Storage counts are separate from measured process peak. No GPU or new scientific input was used by this intake.

## Complete finite forecast banks and original-record parent joints

PR206 also publishes [the next adapter contract](https://github.com/cdenn016/MultiAgentELBO/blob/b9e72d5d3503965ad7d58c4baf060611cf8a244a/docs/research/2026-10-03-latent-link-rg-plan/R3-MOMENT-FLOW-QUERY-CONTRACT.md). It reparameterizes both saved initial/final future generator laws with every one of the unchanged 256 archived forecast-noise vectors, preserving archive-order component IDs and uniform masses $1/256$. These are quadrature identities, not posterior-chain identities. The supplied fresh baseline matter/source law is retained; fitted prefix matter/source arrays provide provenance only.

At each endpoint the frozen target retains the original receivers 0/1 joint with all 16 source patterns, shared primitive reversal pairs and summed coefficients at shared fine nodes. The two hard 2x2 stages retain all 1024 original copies, yielding 128 then 32 parents with direct/staged tree checks. Full fine-to-parent normalized coefficients, sparse query coefficients, regression and residual matrices determine original-unit conditional mixtures at the declared linspace normalized contexts. Those endpoint-specific hypothetical contexts are separate from the causal original future marginal and from an observed raw-parent value. Row scores are never multiplied into a joint density.

The [adapter result](https://github.com/cdenn016/MultiAgentELBO/blob/a891fb1e9c2f0403679b72708af6c752df50268d/docs/research/2026-10-03-latent-link-rg-plan/R3-MOMENT-FLOW-QUERY-RESULTS.md) completed once from clean published producer `b9e72d5d`. Both complete banks and parent joints were constructed before episode-3 evaluation records were decoded or used; earlier byte hashing served provenance only. Initial components reproduce the retained R1 bank within $4.440892098500626\times10^{-16}$, and its candidate/component-row/marginal log scores within $7.105427357601002\times10^{-15}$, $3.552713678800501\times10^{-15}$ and $1.7763568394002505\times10^{-15}$, respectively. These comparisons retain the declared initial transformation; they do not certify its complete rounding error.

The [saved-only NumPy/SciPy receipt](https://github.com/cdenn016/MultiAgentELBO/blob/a891fb1e9c2f0403679b72708af6c752df50268d/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-moment-flow-query-readback.json) passes 198 comparisons over 21,455,394 entries, with maximum absolute discrepancy $1.0658141036401503\times10^{-13}$ against the frozen $10^{-8}$ allowance. It independently reconstructs all components, incident catalogs, source patterns, original joint coefficients/covariances/masses, all-copy geometry, both trees, normalized channels/composition, sparse coefficients, regression/residual matrices and original-unit scores. Identity checks use zero allowance, symmetry $10^{-12}$ and clock $10^{-15}$; residual Cholesky has no floor. Root matched all ten input and eleven source/checker snapshot bindings and passing flags. The three pre-outcome tiny tests remain separate route/layout/replay evidence. No field call, new inference, input regeneration or retry occurred.

| Same archived original receivers 0/1 query | Initial log density | Final log density | Final minus initial |
|---|---:|---:|---:|
| Original joint record | -6.916531190857590 | -6.916718561539034 | -0.00018737068144414337 |
| Given 128-parent normalized context | -6.858527668197016 | -6.858691053252325 | -0.00016338505530821834 |
| Given 32-parent normalized context | -6.920379011958255 | -6.920559918329607 | -0.00018090637135159682 |

These changes describe two finite supplied mixtures at one fixed query. Their negative signs do not establish predictive degradation, improvement, independent-instance performance or posterior accuracy. The initial sum of row marginal log scores is -7.066187789713138, distinct from its shared joint log density. Endpoint-specific normalized charts also do not represent one fixed raw-parent observation.

The [producer receipt](https://github.com/cdenn016/MultiAgentELBO/blob/a891fb1e9c2f0403679b72708af6c752df50268d/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-moment-flow-query.json) records 3.9262625999981537 seconds and 786,587,648-byte process peak; readback took 6.010737800039351 seconds with 292,528,128-byte peak. Both use CPU float64, sequential MKL and one math thread. Derived arrays occupy 120,111,120 logical and 89,712,188 compressed NPZ bytes. Each endpoint retains 26,331,152 logical geometry bytes, 10,747,904 normalized-channel bytes and 8,388,608 generator-bank bytes; its separately charged direct-composition workspace is 13,451,264 bytes and contiguous exponential input 8,388,608 bytes. Input snapshots occupy 24,429,921 bytes and source snapshots 145,851 bytes. These are charged replay/workspace counts, distinct from peak memory or a minimal retained state.

The [complete manifest](https://github.com/cdenn016/MultiAgentELBO/blob/a891fb1e9c2f0403679b72708af6c752df50268d/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-moment-flow-query-package.json) retains 41 files totaling 114,344,602 bytes, including both complete banks/joints, contexts, scores, first outcome, readback and exact source/input snapshots. Root copied the complete package to the canonical Desktop code artifact directory and matched every length and SHA256. The endpoint-to-complete-forecast interface is therefore exercised at the declared tolerance. Continuous Gaussian component integration, all computed/input error, retained/filter updates, moving-geometry conditional information and original-flow downward feedback remain separate obligations; static conditioning does not supply an autonomous parent process.

## Relevance to this research

[[Natural gradient]] gains one admitted deterministic-moment numerical trajectory and complete finite forecast/parent joints with saved-only arithmetic replay, while retaining computed-arithmetic and complete-generator replay obligations. [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] gain an admitted ideal fixed-preparation mark family and stationary path subsequences. Dense native resolvent range, actual nonstationary starts, population/posterior accuracy, retained/filter dynamics, original-flow parent feedback, growing-depth control and persistent formation remain unresolved. All four RG gates remain open, reward choice remains unadopted and the 144-case CUDA calibration remains unrun while the GPU stays with the user. This intake performs no new science execution or manuscript/model change.
