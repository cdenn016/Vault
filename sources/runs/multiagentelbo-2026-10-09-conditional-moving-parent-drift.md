---
type: run
title: "Complete same-prefix conditional moving-parent drift"
aliases: ["N512 cubic moving-parent mean and quadratic covariance drift readout"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Complete same-prefix conditional moving-parent drift

[Code PR218](https://github.com/cdenn016/MultiAgentELBO/pull/218), merged at `421f9d2056cd46476c95582dc28af0b4a4a304c9`, freezes the complete coefficient construction, consumer, independent reader and contract. [Code PR219](https://github.com/cdenn016/MultiAgentELBO/pull/219), outcome commit `3630bbef` and merge `9bfe7b60665f57b2fe34cd52b336578060138525`, publishes the once-run six-case result. This completes the instantaneous moving-parent drift readout pending in [[multiagentelbo-2026-10-09-conditional-chart-means]]. It does not adopt averaged-force dynamics or close any RG gate.

```bibtex
@misc{codex2026conditionalmovingparentdrift,
  author = {Codex},
  title = {Complete Same-Prefix Conditional Moving-Parent Drift},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/219},
  note = {Source PR218 merge 421f9d20; outcome PR219 merge 9bfe7b60; complete instantaneous finite-rule coefficients and same-prefix Gaussian readout}
}
```

## Existing-law coefficient construction

The [derivation](https://github.com/cdenn016/MultiAgentELBO/blob/421f9d2056cd46476c95582dc28af0b4a4a304c9/docs/research/2026-10-03-latent-link-rg-plan/R3-CONDITIONAL-MOVING-COEFFICIENTS.md) and [frozen contract](https://github.com/cdenn016/MultiAgentELBO/blob/421f9d2056cd46476c95582dc28af0b4a4a304c9/docs/research/2026-10-03-latent-link-rg-plan/R3-CONDITIONAL-MOVING-FIELD-CONTRACT.md) preserve N512, E1024, GL(2), generator dimension four, selected observed slice two, signed order-nine moments, $h=1/40000$, $T=.05$, original copies/signs/reversals, fixed probe/forests and weights .25/.0625. The only cases are old prefixes one/two/three at alternative 128/32 parents. Each field uses its current-prefix physical Gaussian endpoint law, with full known fine initialization and unselected raw recognition kernel. Successful admission is provenance, not conditioning information. Later chart y and hidden fine means are not decoded.

The original-generator drift is recovered from the saved old-only quadratic chart banks, retaining all prior, loop, history, thermal and sender/receiver record constants. With $L=\operatorname{chol}(\Lambda^{-1})$, $\alpha=\sqrt{2Th}$, $\gamma=\sqrt{4Th}$, four-vector chart polynomial $f^m$ and symmetric matrix covariance-chart polynomial $F$, inversion gives

$$
b^m=(\alpha Lf^m-m)/h,
b^\Lambda=T(d+1)\Lambda-(\gamma/h)L^{-T}FL^{-1},
d=4.
$$

The $T(d+1)$ constant follows by solving the covariance chart; together with its chart constant it returns the actual $H-\Lambda+T(d+2)\Lambda$ precision drift. The original normalized driver factor uses four mean and ten diagonal-first trace-orthonormal symmetric precision coordinates, with negative precision columns $-\sqrt2\Lambda LH_sL^T\Lambda$. Solving in that complete factor preserves covariance/precision coupling; its physical noise multiplier is $\sqrt{2T}$. No raw Euclidean generator update or new Brownian draw is introduced.

Geometry-only jets regenerate every transport value, original shared driver column and curvature from retained geometry and persistent $\epsilon$, with zero supplied flow. The probe factor $\operatorname{chol}(\Lambda)^{-T}$ is distinct from $L$. Let $U_{ia}=DT_i[\sigma_a]$, $\kappa_i=\sum_aD^2T_i[\sigma_a,\sigma_a]$ and $F_i(x)=DT_i[b_G(x)]$, where $x$ is the hidden selected-slice recognition mean treated as an independent matter coordinate. The saved full matter quadratic gives $b_i^\mu=-\Sigma_i(Kx-h_0)_i$ and $b_i^\Sigma=\Sigma_i-\Sigma_iK_{ii}\Sigma_i+Tk\Sigma_i$, $k=2$, for the current R0 matter-prior/expected-record family. Thus

$$
B_{M,p}(x)=\sum_{i\in p}w_i[T_ib_i^\mu(x)+F_i(x)x_i+T\kappa_ix_i],
$$

$$
\begin{aligned}
B_{V,p}(x)=\sum_{i\in p}w_i^2[&T_ib_i^\Sigma T_i^T+F_i(x)\Sigma_iT_i^T+T_i\Sigma_iF_i(x)^T\\
&+T(\kappa_i\Sigma_iT_i^T+T_i\Sigma_i\kappa_i^T+2\sum_aU_{ia}\Sigma_iU_{ia}^T)].
\end{aligned}
$$

Mean drift is cubic and covariance drift is quadratic. Repeated/reversed/dressed occurrences retain the same original driver ID before contraction. The representation stores two cubic tensors and five quadratic matrices on internal parent coordinates, with five affine neighbor vectors on their full structural support. External-to-internal physical covariance remains in the Gaussian linear-chaos variance. This is exact coefficient algebra for the declared finite rule, with its separate response, population and floating/input error scope. It is not an equality between conditional drift and the mean of a nonlinear finite exponential proposal. No new bracket calculation is included in this consumer.

## Once-run conditional means and allowances

The [published result](https://github.com/cdenn016/MultiAgentELBO/blob/9bfe7b60665f57b2fe34cd52b336578060138525/docs/research/2026-10-03-latent-link-rg-plan/R3-CONDITIONAL-MOVING-FIELD-RESULTS.md) contains 480 parent coefficient archives and 2,400 scalar fields, ordered $M_0,M_1,V_{00},V_{11},\sqrt2V_{01}$. Complete physical endpoint covariance enters Gaussian pairings through degree six. Point values, trace corrections and the linear/quadratic/cubic chaos variances are saved separately. The previously proved likelihood second moment gives each component allowance

$$
e_f=\sqrt{\operatorname{Var}_{q_j}(f)\operatorname{expm1}(L_{2,j}+B_{0,j})}.
$$

The separate whole-path likelihood ingredients are used without receiver normalization. A generic KL bound alone cannot replace these hypotheses. Prefix one has zero likelihood mismatch under the exact known-initialization conditional. Variances/allowances are finite and nonnegative, with no coefficient deletion or variance repair.

| Prefix | Parents | Maximum component allowance | Euclidean allowance across all components | Maximum absolute trace correction |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 128 | 0 | 0 | 2.257685188282e-7 |
| 1 | 32 | 0 | 0 | 3.334976104909e-7 |
| 2 | 128 | 5.718936431312e-6 | 4.673506778577e-5 | 4.513486110442e-7 |
| 2 | 32 | 4.553951044730e-6 | 2.076471655936e-5 | 6.681412342266e-7 |
| 3 | 128 | 1.500576892464e-5 | 1.223470958095e-4 | 6.779832425322e-7 |
| 3 | 32 | 1.198022238056e-5 | 5.440015904390e-5 | 1.007636543129e-6 |

These are declared drift-coordinate units, rather than the previous whitened chart units. No scientific pass target, confidence level or acceptance threshold was selected. Their sufficient expectation interpretation remains conditional on the mathematical likelihood/coefficient hypotheses and numerical exclusions. Mechanical tolerance 1e-8 does not certify smaller trace corrections. Known fine initialization, complete retained/filter history, unselected raw numerical law and uncompressed O(N) state remain charged; this supplies neither unknown-initialization nor native latent-posterior accuracy.

## Independent reconstruction and replay

The [independent reader](https://github.com/cdenn016/MultiAgentELBO/blob/9bfe7b60665f57b2fe34cd52b336578060138525/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-conditional-moving-fields-readback.json) differentiates all 1,440 primitive geometries with local Torch Jacobians/Hessians and separate rooted traversal. Canonical monomial assembly reconstructs every raw/natural/driver coefficient and parent tensor, shared transport column and current-prefix reference; independent Gaussian chaos contractions reconstruct all statistics and allowances. It passes 7,971 comparisons over 40,521,582 entries with maximum discrepancy 6.535882945968297e-13. Structural IDs/supports/padding/prefixes use zero allowance; physical covariance/symmetry and final likelihood allowances use 1e-12; coefficients/geometry/statistics use 1e-8. Thirteen previously passing tiny JUnit fixtures were not rerun.

The [producer](https://github.com/cdenn016/MultiAgentELBO/blob/9bfe7b60665f57b2fe34cd52b336578060138525/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-conditional-moving-fields.json) ran once in 12.019264900009148 seconds, cumulative peak 128,536,576 bytes. The reader ran once in 55.45215989998542 seconds, peak 1,475,538,944 bytes. Both used isolated Anaconda CPU float64, sequential MKL and one math thread, with no CUDA allocation. The 502 NPZ outputs contain 124,656,816 logical bytes and occupy 50,403,686 compressed bytes; input/source snapshots occupy 111,410,376/182,293 bytes. Available producer RAM 29,320,138,752 bytes exceeded the 4GiB guard. Complete original context and earlier construction/conditioning arrays remain charged, so timing/peak are descriptive measurements rather than a scaling result.

The [complete replay manifest](https://github.com/cdenn016/MultiAgentELBO/blob/9bfe7b60665f57b2fe34cd52b336578060138525/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-conditional-moving-fields-package.json) has 709 files totaling 164,185,609 bytes. Original/snapshot lengths and SHA256 match for 184 input and 21 source bindings; all 708 reader input bindings and executing reader hash match. Root independently verified actual canonical Desktop relative-path/length/hash parity. The receipts are unchanged first scientific outcomes. Packaging/intake performs no scientific rerun.

## Pinned published bytes

| Published input | SHA256 |
| :--- | :--- |
| R3-CONDITIONAL-MOVING-COEFFICIENTS.md | b182bf299bf9917c3589e0f57b7be5037fc5b3ea7d44bd34fcd062ac854aa955 |
| R3-CONDITIONAL-MOVING-FIELD-CONTRACT.md | 3457ae6d51381281b459896472fe9cc9febb467de7da5d87c7d91492c77b2477 |
| R3-CONDITIONAL-MOVING-FIELD-RESULTS.md | 48e30033406015008e95150ed28724dba65e2e71308aeadc20356b2ed2c7b536 |
| Producer receipt | 66cc9c460e6e8de9606c1fa52427c2a6d54875cd8dd4a74e61508dd2ad7cc73f |
| Reader receipt | e7da20e5a212e208f45f8dc4b6e17e105e1ca567bc59b8726dca9273aaf8119b |
| Canonical replay manifest | a263f1bed61c72d15ce2a3adfa8c4579a93b07eb1680dcd2ec0a83a34e202c2d |

## Relevance to this research

[[Natural gradient]], [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] now have a complete instantaneous moving-parent drift readout under the existing same-prefix recognition filter reference, including the cubic term and shared geometry responses. The next dependency is the unchanged normalized joint predictive/downward kernel and an actual-law expected history budget. That predictive operation has not executed at this publication; a sum at these six saved prefixes is not an expectation over histories. New bracket execution, nonlinear finite-proposal moments, stopped/continuous error and containment, compressed regular filters, persistent endogenous formation and growing size/depth remain open. The original fresh-record forecast retains fresh $a,J_0^{-1},\pi$ and the future generator law, independently of hidden recognition means at fixed future geometry. All four RG gates remain open, the user owns the GPU and the 144-case CUDA calibration remains unrun. This intake changes no model, manuscript, prior immutable source or scientific law.
