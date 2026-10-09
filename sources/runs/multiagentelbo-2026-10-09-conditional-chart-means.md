---
type: run
title: "Same-prefix conditional chart means and Gaussian L2 transfer"
aliases: ["N512 conditional proposal-chart means and chi-square field transfer"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Same-prefix conditional chart means and Gaussian L2 transfer

[Code PR216](https://github.com/cdenn016/MultiAgentELBO/pull/216), published at `dcb1d5cc3e673901392dfbb0f27ddf817f3da4ab`, adds the fixed-prefix chi-square transfer proof and freezes the saved-only conditional chart-mean consumer. [Code PR217](https://github.com/cdenn016/MultiAgentELBO/pull/217), outcome commit `5ff4e4f2e8efbb1d37c0f465b59c39fd3deb6bc4` and merge `d6f23391cab6441d2133ec53a46612edb985d14c`, publishes its once-run six-case results. This advances the conditional field operation prepared in [[multiagentelbo-2026-10-09-recursive-recognition-filter-bound]], retaining the original model and raw recognition law. All four scientific RG gates remain open.

```bibtex
@misc{codex2026conditionalchartmeans,
  author = {Codex},
  title = {Same-Prefix Conditional Chart Means and Gaussian L2 Transfer},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/217},
  note = {Source PR216 dcb1d5cc; outcome PR217 merge d6f23391; known initialization and original unselected numerical recognition kernel}
}
```

## Exact fixed-prefix transfer

The [new proof](https://github.com/cdenn016/MultiAgentELBO/blob/dcb1d5cc3e673901392dfbb0f27ddf817f3da4ab/docs/research/2026-10-03-latent-link-rg-plan/R3-CHI-SQUARE-FIELD-TRANSFER.md) reuses the already established same-fiber conditional likelihood $p=Z^{-1}e^{a-b/2}q$, $b\geq0$, from the complete observed-prefix Gaussian path comparison. Its inputs are the actual sufficient likelihood estimates $\log E_qe^{2a}-2E_qa\leq L_2$ and $E_qb\leq B_0$. Jensen gives $\log Z\geq E_qa-E_qb/2$, while $2(a-b/2)\leq2a$, so

$$
\chi^2(p\Vert q)=E_q\left[\left(\frac{dp}{dq}-1\right)^2\right]
\leq\operatorname{expm1}(L_2+B_0).
$$

For every real $f\in L^2(q)$, Cauchy-Schwarz then gives

$$
|E_pf-E_qf|\leq\sqrt{\operatorname{Var}_q(f)\operatorname{expm1}(L_2+B_0)}.
$$

The density-ratio hypotheses are stronger than a generic KL assertion; bare KL alone supplies no such inequality. Endpoint projection preserves this chi-square upper bound by conditional Jensen. All finite-degree Gaussian polynomials, including cubic moving-parent drift, have finite variance on the singular affine fiber without an inverse ambient covariance or jitter. Cubic means and variances require moments through degrees three and six, including cross-child covariance. No exponential moment of the cubic field is required. This removes the earlier need for a useful large density-domination constant in polynomial transfer, but does not evaluate a cubic coefficient bank or certify nonlinear matrix-exponential expectations.

## Once-run quadratic chart readout

The [frozen contract](https://github.com/cdenn016/MultiAgentELBO/blob/dcb1d5cc3e673901392dfbb0f27ddf817f3da4ab/docs/research/2026-10-03-latent-link-rg-plan/R3-CONDITIONAL-FIELD-MEAN-CONTRACT.md) declares old prefixes one, two and three at alternative 128/32-parent constraints, N512, E1024, original GL(2) copies, order-nine moments, $h=1/40000$ and $T=.05$. Each prediction uses only retained observations through that prefix. Prefix one is the exact physical conditional from a known fine prestate; later prefixes use their jointly conditioned Gaussian endpoint. The consumer decodes saved B,b,c, supports and structural metadata, excluding the later observed chart y and hidden fine-mean verification anchors. It generates no field, response bank, proposal, trajectory, observation or sample.

The [published outcome](https://github.com/cdenn016/MultiAgentELBO/blob/d6f23391cab6441d2133ec53a46612edb985d14c/docs/research/2026-10-03-latent-link-rg-plan/R3-CONDITIONAL-FIELD-MEAN-RESULTS.md) evaluates all 95,232 scalar coordinates: 1,536 source contrasts, 4,096 generator means and 10,240 orthonormal symmetric generator covariance-log coordinates per case. These are whitened proposal-chart means, not raw forces or physical matrix means. For $f=x^TBx+b^Tx+c$ and its actual supported physical Gaussian covariance $C_q$,

$$
E_qf=m^TBm+b^Tm+c+\operatorname{tr}(BC_q),
v_f=2\operatorname{tr}(BC_qBC_q)+(2Bm+b)^TC_q(2Bm+b).
$$

The declared computational error allowance remains $\sqrt{2v_fK}+2L_fK$, with $L_f=c_q\|B\|_{op}$ from the proved covariance ceiling. It uses the whole-joint forward KL upper $K$, never its per-receiver normalization. The chi-square proof above is a separate extension; it does not retrospectively change the frozen readout formula. Maximum component allowances in the original whitened chart units are:

| Prefix | Parents | Source contrasts | Generator means | Generator covariance chart |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 128 | 0 | 0 | 0 |
| 1 | 32 | 0 | 0 | 0 |
| 2 | 128 | 5.398514461213701e-7 | 9.276859602315995e-8 | 1.6930958991774332e-8 |
| 2 | 32 | 5.419549518460646e-7 | 9.93907076579757e-8 | 1.8244033605199428e-8 |
| 3 | 128 | 1.414235709771060e-6 | 2.425294784258328e-7 | 4.428099025126924e-8 |
| 3 | 32 | 1.4198798610660002e-6 | 2.5983500589882617e-7 | 4.7712432603286607e-8 |

The largest family Euclidean allowance is 1.935245980563117e-5 for the 1,536 source coordinates at prefix three and 32 parents; summing squared component bounds assumes no independence. Prefix-one filter-comparison error is exactly zero under the mathematical known-prestate law, with numerical arithmetic still excluded. No new scientific acceptance threshold was selected.

The saved covariance trace corrections reach absolute maxima 2.881072520672313e-8, 3.837542026154664e-9 and 5.9506729964684415e-9 for source, mean and covariance charts. Evaluating only at m omits these terms. Their small computed sizes are subject to rounding exclusions; the 1e-8 coefficient-derived comparison allowance does not certify corrections below that allowance. Negative evaluated variance would be retained as a failure rather than clipped.

## Evidence, costs and limits

The [independent reader](https://github.com/cdenn016/MultiAgentELBO/blob/d6f23391cab6441d2133ec53a46612edb985d14c/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-conditional-field-means-readback.json) passes 1,161 comparisons over 21,871,319 entries with maximum discrepancy 2.3822801641527197e-22. It independently chooses prefixes, reconstructs first-prefix physical covariance by child-pair blocks and evaluates supported contractions/eigenvalue norms. All 24 NPZ outputs, coordinate metadata, ancestry, snapshot lengths and storage/workspace charges are compared. Three producer and two reader JUnit fixtures passed before source publication; neither the scientific run nor passing fixtures was retried.

The [producer receipt](https://github.com/cdenn016/MultiAgentELBO/blob/d6f23391cab6441d2133ec53a46612edb985d14c/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-conditional-field-means.json) records 7.340939600020647 seconds and cumulative process peak 86,634,496 bytes; the reader records 2.611750000040047 seconds and peak 125,440,000 bytes. Available RAM was 29,484,417,024 bytes above the frozen 2GiB guard. Derived arrays occupy 103,932,096 logical bytes and 51,163,151 compressed NPZ bytes; input/source snapshots occupy 63,123,008/104,942 bytes. Known initialization, complete retained history, endpoint covariance, coefficient banks and upstream construction work remain charged. Both processes used isolated sequential one-thread Anaconda CPU float64 with no CUDA tensors.

Root matched 139 producer input, 13 source and 177 reader bindings. The [canonical replay manifest](https://github.com/cdenn016/MultiAgentELBO/blob/d6f23391cab6441d2133ec53a46612edb985d14c/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-conditional-field-means-package.json) contains 178 files totaling 114,874,488 bytes, with root-recorded actual Desktop relative-path/length/SHA256 parity. This is a finite saved-prefix computation with full O(N), history-dependent state. Input, signed-moment response/coefficient, factor/solve and floating contraction errors remain outside certification. Known full initialization and the unselected raw kernel remain required; admission success is provenance, not a conditioning event. It establishes no native latent-posterior accuracy or physical softmax/exponential/inverse-precision interval by evaluating those maps at chart means.

## Pinned published bytes

| Published input | SHA256 |
| :--- | :--- |
| R3-CHI-SQUARE-FIELD-TRANSFER.md | 9200928b81730af9dc09d85460e683c335395ae8bfeb83a8ea902e0ecacaea1c |
| R3-CONDITIONAL-FIELD-MEAN-CONTRACT.md | 7dbeec45314933c36ddf300954779c7d9ceca2061b7215d96ac24adc3371dec6 |
| R3-CONDITIONAL-FIELD-MEAN-RESULTS.md | 5c8d5f2e5fab4a61a5b03c2f2e28183f22044912b9f48a1b0733dd4ba6cdaffc |
| Producer receipt | 9b345dc03dce196fb34ae17dcee188ab868a306d783f709b822e967a6c850fc2 |
| Reader receipt | dd28656f063a6da5635618bd51d8331a2997386c4f1d0fad84f8e022c2251aac |
| Canonical replay manifest | bbff2dc3365485532baad19920d7b2af51528a9a0562dd089d4b7f719ed0f74a |

## Relevance to this research

[[Natural gradient]], [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] now have an executed causal chart-mean readout and a useful Gaussian-L2 transfer theorem for the next moving-parent cubic coefficients. At these publications that complete coefficient assembly and degree-six moment calculation remain unrun. Replacing the original normalized kernel by an expectation-force SDE would change the scientific law; the valid downward operation is the regular conditional of the same approximate joint. The original fresh-record decoder still uses fresh $a,J_0^{-1},\pi$ and the fixed future generator law independently of hidden recognition means. Integrated actual-history error, unknown initialization, stopped/continuous containment, compact feedback, persistent formation, growing size/depth and all four RG gates remain open. The separate minimal-form stationary identification obligation in [[multiagentelbo-2026-10-09-recursive-recognition-filter-bound]] is unchanged. The user owns the GPU; the 144-case CUDA calibration remains unrun. This intake launches no scientific work and edits no manuscript, model or older immutable source.
