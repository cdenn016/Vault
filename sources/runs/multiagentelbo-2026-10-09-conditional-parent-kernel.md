---
type: run
title: "Continuous same-prefix original parent kernel"
aliases: ["N512 continuous Gaussian-fiber original Fisher kernel consumer"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Continuous same-prefix original parent kernel

[Code PR221](https://github.com/cdenn016/MultiAgentELBO/pull/221), outcome commit `6823a91228070b0a1cdc98f6c9a52317539a98da` and merge `45c8be5cf5448b7633bbcd8970aaf9b3ceecd0fc`, publishes the once-run continuous conditional consumer from frozen source `c96f9dd1658d7911dd6baad4826d4d25c041b558`. It executes the normalized Gaussian-reference predictive operation pending in [[multiagentelbo-2026-10-09-conditional-moving-parent-drift]] through the complete original raw joint proposal. Forty-eight saved realizations ground the executable kernel; they estimate neither its mixture integral nor predictive accuracy. The same-joint nonlinear downward posterior integral, actual-law expected history budget and all RG gates remain open.

```bibtex
@misc{codex2026conditionalparentkernel,
  author = {Codex},
  title = {Continuous Same-Prefix Original Parent Kernel},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/221},
  note = {Frozen source c96f9dd1; outcome 6823a912; merge 45c8be5c; continuous Gaussian-fiber raw-kernel consumer at six saved histories}
}
```

## Preserved law and causal information

The [frozen contract](https://github.com/cdenn016/MultiAgentELBO/blob/c96f9dd1658d7911dd6baad4826d4d25c041b558/docs/research/2026-10-03-latent-link-rg-plan/R3-CONDITIONAL-PARENT-KERNEL-CONTRACT.md) fixes N512, E1024, GL(2), observed episode prefix 0-2, selected recognition-mean slice two, order-nine finite rule, $h=1/40000$, $T=.05$, original source support, copies/reversals, persistent probe and rooted trees. The six cases are inference prefixes one/two/three with alternative 128/32-parent histories. These histories are separate conditioning alternatives; their constraints are not multiplied as independent observations. The complete known fine initialization and all O(N), history-dependent retained/filter data remain charged.

At each unchanged saved retained state $R_j$, the neutral reference follows the chronological selected-mean affine dynamics using old belief blocks $C_k=\operatorname{blockdiag}(\Sigma_{2,k})$:

$$
F_k=I-hC_kK_k^{\mathrm{mat}},  d_k=hC_kh_{0,k},  Q_k=2ThC_k.
$$

The full receiver-and-sender matter Hessian is $K_k^{\mathrm{mat}}$. The physical innovation covariance $Q_k$ is distinct from the updated belief covariance. With unconditioned Gaussian path $X=\mu+Gz$, complete available-prefix constraint map $H=A_{\mathrm{path}}G$ and $V=HH^T$, the endpoint conditional is

$$
m=\mu_{\mathrm{end}}+G_{\mathrm{end}}H^TV^{-1}(M-A_{\mathrm{path}}\mu),
J=G_{\mathrm{end}}-G_{\mathrm{end}}H^TV^{-1}H,  x=m+Jz.
$$

Strictly positive physical innovations and full-row-rank parent constraints permit the Gram solve. The conditional covariance $JJ^T$ may be singular; no ambient covariance inversion, eigenvalue clipping, jitter or deleted constraint is used. Only individual checkpoints through the current prefix enter conditioning. Later parent observations, chart y, original selected fine means and archived admission success are excluded from prediction. This continues the physical-filter distinction in [[multiagentelbo-2026-10-09-first-step-filter-source-domain]] and the whole-prefix reference in [[multiagentelbo-2026-10-09-recursive-recognition-filter-bound]].

Fresh latent-mixture normals are separate from the five fresh original proposal-noise families. Seed 20261009 and prefix/depth/draw order produce eight realizations per case. Complete old quadratic chart banks recover every affected source, generator-mean and generator-precision direction at $x$, retaining original priors, loops, history and sender/receiver terms. Hidden-independent blocks retain their old direction. Setting the first supported source-reference gradient to zero changes only a common row constant and preserves the noisy softmax. The unchanged full positive Fisher proposal runs once for every draw, followed by first, staged second and direct second parent readouts with updated geometry and the fixed probe. All directions, noises, updated states and original marks are retained. There are no new objective/field or moment-response evaluations and no raw-proposal selection by an outer-box test.

The continuous law being consumed is $q_j^{\mathrm{end}}K_j^{\mathrm{exact}}$ at a saved $R_j$. It is distinct from the nonlinear same-law recognition conditional $\eta_j$ and from the latent generative posterior. Eight realizations do not replace the continuous mixture by an empirical bank, adopt averaged-force dynamics or construct an autonomous parent law. A subsequent transition from a generated $R'$ needs complete coefficients there; old banks at unchanged $R_j$ cannot supply that transition.

## Local conditional budgets and normalized history reference

The [normalized reference-history derivation](https://github.com/cdenn016/MultiAgentELBO/blob/45c8be5cf5448b7633bbcd8970aaf9b3ceecd0fc/docs/research/2026-10-03-latent-link-rg-plan/R3-NORMALIZED-REFERENCE-HISTORY-BOUND.md), equations (2)-(6), defines a separate normalized causal proof law $Q$ by centering the retained likelihood at the available Gaussian endpoint mean while preserving the original hidden transition. Source/SPD densities and Jacobians are included before their equal normalizations cancel in relative entropy. The proof-reference conditional is the neutral Gaussian path. Entropy chain rules and common-kernel contraction bound the hybrid retained-history relative entropy by actual-law expectations of complete chart discrepancies. For four transitions, the sufficient sum is $3E_P\kappa_0+2E_P\kappa_1+E_P\kappa_2$, with $\kappa_0=0$ from known initialization. A local prefix-three value is valid but is not another term in that four-transition bound.

For every complete whitened scalar retained chart, set $u_b=f_b(x)-f_b(m_j)$ and $\kappa_j=\frac12\sum_bu_b^2$. Complete Gaussian second/fourth moments, through degree eight, preserve physical cross-child covariance and singular fibers. The separately justified likelihood second-moment ceiling $\chi_j$ gives

$$
E_{q_j}\kappa_j=\frac12\sum_bE_{q_j}u_b^2,
E_{\eta_j}[\kappa_j\mid H_j]\leq\frac12\sqrt{1+\chi_j}\sum_b\sqrt{E_{q_j}u_b^4}.
$$

This uses the particular current-prefix likelihood-MGF hypotheses, not a conversion from arbitrary KL. The [published result](https://github.com/cdenn016/MultiAgentELBO/blob/45c8be5cf5448b7633bbcd8970aaf9b3ceecd0fc/docs/research/2026-10-03-latent-link-rg-plan/R3-CONDITIONAL-PARENT-KERNEL-RESULTS.md) evaluates all 95,232 source/generator chart rows across the six cases:

| Prefix | Parents | Conditional $E_q\kappa$ | Conditional $E_\eta\kappa$ ceiling | Chi-square ceiling |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 128 | 4.4784745784430155e-7 | 7.75695646474315e-7 | 0 |
| 1 | 32 | 5.449515223096207e-7 | 9.438850950190497e-7 | 0 |
| 2 | 128 | 8.956367586324125e-7 | 1.5513032692627756e-6 | 1.3558072871004506e-5 |
| 2 | 32 | 1.0898253940556618e-6 | 1.8876512330538105e-6 | 1.3558157671188004e-5 |
| 3 | 128 | 1.3433543664513893e-6 | 2.3268399158752937e-6 | 6.192519663123019e-5 |
| 3 | 32 | 1.6346045192592829e-6 | 2.831318073010919e-6 | 6.192454949365504e-5 |

These are conditional values at six fixed saved histories. Their sum does not evaluate an outer actual-law expectation or an integrated history budget. MGF/coefficient-domain failures and exits remain uncontrolled under the actual raw history law. No scientific accuracy target, confidence interval or acceptance threshold was selected. The entropy proof-reference $Q$ and the executed exact-kernel hybrid serve separate roles; neither is adopted mean-force dynamics.

## Independent reconstruction and complete replay

The [independent reader receipt](https://github.com/cdenn016/MultiAgentELBO/blob/45c8be5cf5448b7633bbcd8970aaf9b3ceecd0fc/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-conditional-parent-kernel-readback.json) passes 4,460 comparisons over 108,970,525 entries with maximum absolute discrepancy 3.077094135051084e-12. It uses independent QR fiber projection, chart inversion, cumulant/Bell fourth moments and earlier NumPy raw-proposal/rooted-geometry formulas, importing none of the new producer/factor/field-adapter/fourth-moment helpers. It reconstructs all causal mappings, six factors, original noise IDs, 48 PRNG tuples, complete directions/states and all first/staged/direct readouts. Structural mappings/PRNG/supports use zero allowance; physical covariance/symmetry/source mass/final likelihood and kappa quantities use 1e-12; coefficient-derived moments/fields/proposals/geometry use 1e-8. These are mechanical comparison allowances, not interval certification. Maximum saved staged/direct discrepancy is 4.9737991503207e-14 and supported-source mass discrepancy is 4.44089209850063e-16.

Thirteen pre-outcome tiny JUnit fixtures remain passing with zero errors/failures/skips and were not rerun. The [producer receipt](https://github.com/cdenn016/MultiAgentELBO/blob/45c8be5cf5448b7633bbcd8970aaf9b3ceecd0fc/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-conditional-parent-kernel.json) records 18.215429700096138 seconds and cumulative process peak 834,535,424 bytes; the reader records 18.915701700025238 seconds and peak 827,801,600 bytes. Both use isolated one-thread Anaconda CPU float64, sequential MKL and no CUDA allocation.

The 319 NPZ outputs contain 722,436,240 logical array bytes and occupy 189,548,324 compressed bytes. Input/source snapshots occupy 163,818,432/258,634 bytes. Original-context logical bytes are 81,712,608, and prior moving/filter construction charges are separately 124,656,816/709,128,352 bytes. These construction/provenance charges are not RSS measurements. The complete known initialization, model/rule/probe/trees, O(N) retained/filter histories, dense conditioning/factor work, chart banks and all new directions/states/noises/readouts remain charged.

The [replay manifest](https://github.com/cdenn016/MultiAgentELBO/blob/45c8be5cf5448b7633bbcd8970aaf9b3ceecd0fc/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-conditional-parent-kernel-package.json) records 592 files totaling 355,320,940 bytes. All 245 original/snapshot input bindings, 26 executed-source/snapshot bindings and 591 reader bindings match. Root independently rehashed the complete actual canonical Desktop package. The manifest binds original executing receipt bytes; the following hashes name the published Git blobs, whose canonical newline representation can differ from those original archived bytes.

| Published Git blob | SHA256 |
| :--- | :--- |
| R3-CONDITIONAL-PARENT-KERNEL-CONTRACT.md | e3517b1b42788d5bacfa2969dfd5887a1adcd516d4d701fc9e7eae9b2610fdc4 |
| R3-NORMALIZED-REFERENCE-HISTORY-BOUND.md | afc14f3bc6624b3e5cc85f1c7c9fb493d2b8ad04f72cb9ad64d55e25a5a13090 |
| R3-CONDITIONAL-PARENT-KERNEL-RESULTS.md | 92080f8f7571a8486939e0a841073f8263e1fd629ed03cc5107d7cc086f2d36a |
| Producer receipt | fc613e91cb5459cfb37e8e685fc348ed86e8d6a2e8b61a0148d94ba549331c70 |
| Reader receipt | 43bb52906a3812fbabb3e36f1db704b4022779554eada59a91bebe35565ce831 |
| Replay manifest | 4e03b38fc41f594608872cd5034a14067a722b74b242d80115f2279c6afb3fcb |

## Relevance to this research

[[Natural gradient]], [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] now have an executable continuous Gaussian-reference consumer of the full original raw recognition transition, following the complete instantaneous drift readout. The remaining dependencies are coefficients at newly generated retained states, the same-joint nonlinear downward posterior integral, actual-law outer history expectations and their domain/exit control. No continuous Fisher path equivalence, native generative-posterior accuracy, fresh-record improvement, finite-dimensional regular closure, endogenous formation or growing-size/depth theorem follows. Fresh generative matter/source baseline $a,J_0^{-1},\pi$ remains distinct from hidden recognition means and is unchanged. All four RG gates remain open; the user owns the GPU and the 144-case CUDA calibration remains unrun. Intake changes no manuscript, scientific model, older immutable source or research direction.
