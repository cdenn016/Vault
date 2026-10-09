---
type: run
title: "Blockwise Fisher forecast budgets and stationary native recognition"
aliases: ["Exact-reference forecast containment and stationary recognition process"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# Blockwise Fisher forecast budgets and stationary native recognition

This record continues [[multiagentelbo-2026-10-08-recognition-spatial-source-moment]] and [[multiagentelbo-2026-10-08-saved-forecast-local-exit]]. [Code PR204](https://github.com/cdenn016/MultiAgentELBO/pull/204) publishes the refined finite-horizon budgets and stationary recognition-process construction at result revision `ea50b5903185b0530595008ceeb9d0104318e660`, merged as `714abfe22ad572b4ac327f892449c6a71a968db0`. Intake uses those exact published records, excluding separate unpublished work. Root reconstructed the proofs, Brownian normalizations and source bindings, and read both load-bearing process references. No formal adjudication state is assigned.

```bibtex
@misc{codex2026blockwiseprocess,
  author = {Codex},
  title = {Blockwise Fisher Forecast Budgets and Stationary Native Recognition},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/204},
  note = {Result revision ea50b590; exact-reference finite-horizon budgets and conditional stationary weak process existence}
}
```

## Refined future-block forecast budget at the unchanged mesh

The [blockwise forecast construction](https://github.com/cdenn016/MultiAgentELBO/blob/ea50b5903185b0530595008ceeb9d0104318e660/docs/research/2026-10-03-latent-link-rg-plan/R3-BLOCKWISE-FORECAST-BUDGET.md) retains the existing N512, K2/D4, C3/J4 product recognition model at $c_*$, kinetic mass 16, temperature $T=1/20$, inference horizon $H=10^{-4}$ and four steps $h=1/40000$. Both paths use the same actual Cholesky Brownian representation and declared exact initial reference. The mathematical population-versus-quadrature/rule discrepancy remains at most $3.932\times10^{-7}$ per complete block. This assumes exact evaluation of that field; computational field, input, inverse, Cholesky, exponential, softmax and automatic-differentiation arithmetic remain excluded.

The exact covariance quadratic-correction moment is $T^2[(d+2)(\operatorname{tr}C)^2+(d+4)\operatorname{tr}(C^2)]$ per $h^2$, yielding sharp matter/generator ceilings $7/100$ and $1/450$. The source component remains the previously derived $111/10000$. Explicit covariance and softmax remainder estimates retain their actual powers of $h$, including accumulated bias/variance terms proportional to $h^2$. Large sufficient source remainders remain in the full upstream error; they are not dropped or promoted to an $h$ contribution by a generic step bound.

The selected future episode contains 1,024 complete generator Gaussians and no observed records. Its original drift retains prior, same-episode ordered loops and kinetic coupling to episode-2 means. The proof propagates full earlier matter/source/generator errors through that coupling, while bounding future noise through its own covariance. Common-kernel contraction then controls the complete correlated original future-record law, with fresh shared baseline matter, original source prior, shared primitives/reversals and original record noise. It does not multiply independent row-mixture scores or construct an autonomous future process.

The [first exact-rational scalar receipt](https://github.com/cdenn016/MultiAgentELBO/blob/ea50b5903185b0530595008ceeb9d0104318e660/docs/research/2026-10-03-latent-link-rg-plan/evidence/blockwise-forecast-budget.json) meets the frozen masked forecast target. Its future average complete-Gaussian coupled mean-square error is at most $6.896\times10^{-8}$, and the common native/numerical outer-survival masked expected joint forecast KL is at most $8.827\times10^{-6}$ nats per receiver. The scalar calculation runs once on Python 3.14.4 CPU in approximately 0.13 seconds, using exact rational operations, upward roots and exponential bounds. It executes no field or trajectory. The earlier unrefined sufficient-budget failure remains recorded; this result sharpens the estimate without changing the model, boxes, temperature or mesh.

## First-grid numerical exit and conditional forecast transfer

The [numerical exit derivation](https://github.com/cdenn016/MultiAgentELBO/blob/ea50b5903185b0530595008ceeb9d0104318e660/docs/research/2026-10-03-latent-link-rg-plan/R3-NUMERICAL-EXIT-BUDGET.md) starts from the same exact normalized/symmetric reference previously admitted by rational Gaussian/source checks. It bounds the unchanged exact quadrature-driven exponential/softmax retraction's first outer-box grid exit, including the first overshoot. Old-state coefficients remain predictable. Constraint-specific Gaussian martingale crossing estimates use actual initial margins and a good-input event to bound nonlinear remainders; Gaussian inputs are neither truncated nor redrawn. No projection or stopped proposal is added to the producer.

The [first numerical-exit receipt](https://github.com/cdenn016/MultiAgentELBO/blob/ea50b5903185b0530595008ceeb9d0104318e660/docs/research/2026-10-03-latent-link-rg-plan/evidence/numerical-exit-budget.json) gives the following outward ceilings:

| Exact-reference quantity | Bound |
|:--|--:|
| Future average complete-Gaussian coupled mean-square error | at most 6.896e-8 |
| Common outer-survival masked expected joint forecast KL per receiver | at most 8.827e-6 nats |
| Numerical outer first-grid exit probability through four steps | at most 4.77777e-5 |
| Native continuous inner exit or numerical outer first-grid exit | at most 0.038243778 |
| Common native-inner/numerical-outer survival probability | at least 0.961756222 |
| Expected joint forecast KL per receiver conditional on that survival | at most 9.179e-6 nats |

The combined exit target is below 0.05. Conditional forecast transfer divides the nonnegative masked expectation by the admitted survival lower bound; it is distinct from the masked expectation and from an unconditional guarantee. Native containment concerns continuous inner-box paths, while numerical containment concerns outer-box grid endpoints. No numerical intergrid-containment conclusion follows. The observation-only marginal obeys the same KL ceiling.

The numerical-exit calculator runs once on standard-library Python 3.14.4 CPU in approximately 8.22 seconds. All residual margins and pass/fail comparisons use exact rational arithmetic before outward receipt serialization. These are evaluated probability/error upper bounds, rather than empirical exit frequencies or a new path measurement. Actual producer arithmetic and initial-reference differences remain necessary applicability budgets. Neither result certifies M16 empirical-field accuracy, a finite atomic forecast mixture or native correlated-posterior accuracy.

## Exact source-byte replay

The [source replay record](https://github.com/cdenn016/MultiAgentELBO/blob/ea50b5903185b0530595008ceeb9d0104318e660/docs/research/2026-10-03-latent-link-rg-plan/evidence/FISHER-BUDGET-SOURCE-REPLAY.md) preserves the two calculators' original input bindings. Every other source/script hash matches the published Git blobs directly. Two JSON inputs were read with CRLF while Git stores their LF forms; the [7,190-byte replay ZIP](https://github.com/cdenn016/MultiAgentELBO/blob/ea50b5903185b0530595008ceeb9d0104318e660/docs/research/2026-10-03-latent-link-rg-plan/evidence/fisher-budget-source-inputs.zip) retains the original producer-read bytes, with archive SHA256 `6491c788f2778e7a447e102b884a223060cb0f6793db8bf6482b81a05052438f`. Its members are the 21,135-byte local-coefficient receipt and 10,770-byte blockwise receipt. No scientific calculation is rerun or receipt outcome changed to reconcile line endings. This is input provenance, separate from computed floating arithmetic.

## Stationary standard diffusion for a chosen native snapshot law

The [native process construction](https://github.com/cdenn016/MultiAgentELBO/blob/ea50b5903185b0530595008ceeb9d0104318e660/docs/research/2026-10-03-latent-link-rg-plan/R5-NATIVE-RECOGNITION-PROCESS.md) applies to each interior marked DLR probability from the previous spatial snapshot theorem, under its compact admissible core marks, fixed finite locality catalog and empirical original-observation second-moment hypotheses. It uses the unchanged countable sum of unit-mobility block gradient energies, with form $T\int\Gamma(f,g)dP$. The local mean/covariance Fisher metric and categorical metric are retained; Gaussian Fisher volume and ordinary source-simplex Lebesgue reference supply the original covariance/source Itô drifts. Every local derivative includes all receiver/sender incident records. No finite-valued infinite free-energy sum is assumed.

Conditional positive smooth local densities prove closability of the cylinder gradient. Complete Gaussian Fisher cutoffs, localized logarithmic source-face cutoffs and zero-energy data cutoffs produce a compact form nest in the original countable product topology. The source estimate first bounds every Gaussian/data coordinate in its cost neighborhood; it does not assume a globally bounded source marginal density. A form-dense continuous cylinder family and countable separating family establish the quasi-regular correspondence hypotheses. The two load-bearing primary results are Albeverio and Ma's Dirichlet-form/right-process correspondence and Fukushima's nestwise smooth-measure semimartingale characterization, linked and applied in the published proof. Root read both; an optional inaccessible Cambridge page supplies no step of the argument.

The closed form therefore supports a conservative reversible standard diffusion with invariant probability $P$ and continuous product paths, outside an exceptional initial set. Constants and mark functions have zero energy, proving actual semigroup conservation and frozen core/data marks. Nest-supported conditional integration by parts identifies the coordinate-local population Fisher SDE and bracket $2T\Gamma$. Whitening and redundant null-noise completion give the original independent Cholesky/source Brownian coefficients without changing the generator or boundary law. Local finite-neighborhood compactness along an interior continuous path justifies the drift integrals; globally integrable drift moments are not presumed.

The process exists for stationary starts with law $P$ and quasi-everywhere admitted initial configurations, with conditional stationary laws for almost every limiting whole mark field. It also applies to a snapshot of the explicitly periodic mathematical reference family. It does not establish arbitrary prescribed R0 starts, every deterministic mark field, pathwise uniqueness, a strong solution in a summable state norm or finite-volume trajectory convergence. The registered independently generated volume family still needs its own mark/data admission. No mixing rate, size-uniform numerical accuracy, growing-depth readout, infinite original posterior or autonomous formation/RG law follows.

## Relevance to this research

[[Natural gradient]] gains sharper exact-reference finite-mesh forecast/exit estimates and a stationary realization of the unchanged infinite local Fisher equations. [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] retain separate requirements for actual computed arithmetic, nonstationary growing-volume initial laws/path limits, native-posterior accuracy, autonomous parent feedback and persistent growing formation. All four full RG gates remain open; the reward choice remains unadopted and the 144-case GPU calibration remains unrun. This batch performs no scientific trajectory, new model, manuscript edit or GPU work.
