---
type: run
title: "Recursive recognition filter bounds and conditional density energy"
aliases: ["N512 same-history Gaussian filter comparison and maximal weak energy"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Recursive recognition filter bounds and conditional density energy

[Code PR214](https://github.com/cdenn016/MultiAgentELBO/pull/214), merged at `910e00d5dfab122e5ab1750eca92c3a6d3cb07c7`, publishes the exact raw recognition-filter recursion, Gaussian whole-path comparison, conditional parent construction and frozen consumer. [Code PR215](https://github.com/cdenn016/MultiAgentELBO/pull/215), outcome commit `12f1673bf4629c6e0a7fed28e21e61fa5af69e09` and merge `a4102c441a47c09ab02ab8e4eaa5fe5499a926de`, publishes the once-run six-case outcome and a separate stationary conditional-density weak-energy proof. The new conditional comparison advances beyond [[multiagentelbo-2026-10-09-first-step-filter-source-domain]] without replacing the scientific model or making its first-step Gaussian an exact recursive filter. All four RG gates remain open.

```bibtex
@misc{codex2026recursiverecognitionfilter,
  author = {Codex},
  title = {Recursive Recognition Filter Bounds and Conditional Density Energy},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/215},
  note = {Source PR214 merge 910e00d5; outcome PR215 merge a4102c44; known fine initialization, unselected numerical recognition kernel and separate stationary native weak energy}
}
```

## Exact recursion and Gaussian reference

The [recursion](https://github.com/cdenn016/MultiAgentELBO/blob/910e00d5dfab122e5ab1750eca92c3a6d3cb07c7/docs/research/2026-10-03-latent-link-rg-plan/R3-RECOGNITION-FILTER-RECURSION.md) keeps N512, E1024, GL(2), all four generator-history slices, original records/signs/reversals, mass16, order-nine moments, $h=1/40000$, $T=.05$ and the fixed probe/trees. The inference index differs from the episode index. Hidden $x_j=\mu_{2,j}$ is a recognition parameter; retained $R_j$ includes preceding matter means, every belief covariance/source row and every generator mean/precision. The complete fine initialization is known. Conditioning includes the actual retained prefix and all parent means through it, while excluding hidden noise realizations, successful box admission, later success and future records.

At fixed old retained state, the selected raw mean substep is

$$
x'=Dx+c+\epsilon,\qquad D=I-hCK,\qquad c=hCh_0,\qquad \epsilon\sim N(0,Q),\qquad Q=2ThC,
$$

where $C=\operatorname{blockdiag}\Sigma_2$ and the complete mean force is $Kx-h_0$, including incident sender records. After observing $R'$, the moving map $A'=A(R')$ is fixed. Its parent marginal has physical covariance $A'QA'^T$. Let $\mathcal K(dx'\mid x,R',M')$ be the corresponding normalized singular Gaussian fiber kernel, and $G_j(x)$ the retained transition density times the parent marginal density. Then

$$
\eta_{j+1}(dx')=
\frac{\int G_j(x)\mathcal K(dx'\mid x,R',M')\eta_j(dx)}{\int G_j(x)\eta_j(dx)},\qquad \eta_0=\delta_{x_0}.
$$

Retained source and generator shifts are quadratic in hidden means. Their observed Gaussian chart likelihoods generate quartic penalties, so this probability-valued recursion is generally non-Gaussian after the first update. Source contrasts preserve their full covariance, generator means use $2Th\Lambda^{-1}$, and the orthonormal symmetric covariance log chart uses $4ThI$. Belief covariance is not physical uncertainty in hidden recognition parameters. SPD/source Jacobians cancel from normalized hidden weights but remain in normalized predictive kernels. A stopped/alive law would additionally require its survival and truncated-kernel factors.

The [Gaussian path comparison](https://github.com/cdenn016/MultiAgentELBO/blob/910e00d5dfab122e5ab1750eca92c3a6d3cb07c7/docs/research/2026-10-03-latent-link-rg-plan/R3-GAUSSIAN-PATH-FILTER-BOUND.md) jointly conditions the entire affine path on every observed parent mean. Later means within the available prefix may smooth earlier coordinates; no later prefix is used for an earlier forecast. The covariance is singular on the compatible ambient fiber, with no jitter. For the exact hidden-path conditional $p$ and Gaussian reference $q$,

$$
p=Z^{-1}e^{a-b/2}q,\qquad a=\sum r_j^Tv_j,\qquad b=\sum\|v_j\|^2\geq0.
$$

The $v_j$ are full local quadratic retained shifts. Completing squares bounds $a-b/2$ above, establishing finite normalization and polynomial moments. Gaussian quadratic cumulants and Wick bounds yield explicit directed KL upper bounds. Source whitening uses the receiver plus all supported senders; generator supports use all original incident records with shared reversal primitives. These sufficient bounds do not evaluate the exact non-Gaussian normalizer or exact KL numerically.

## First six-case outcome and independent readback

The [frozen contract](https://github.com/cdenn016/MultiAgentELBO/blob/910e00d5dfab122e5ab1750eca92c3a6d3cb07c7/docs/research/2026-10-03-latent-link-rg-plan/R3-NONLINEAR-FILTER-CONTRACT.md) declares prefixes two, three and four at both alternative 128/32-parent constraints, with a .001-nat-per-original-receiver target in each direction. The [published outcome](https://github.com/cdenn016/MultiAgentELBO/blob/a4102c441a47c09ab02ab8e4eaa5fe5499a926de/docs/research/2026-10-03-latent-link-rg-plan/R3-RECOGNITION-FILTER-RESULTS.md) reports all six cases passing:

| Prefix | Parents | $D(q\Vert p)$ upper per 512 receivers | $D(p\Vert q)$ upper per 512 receivers |
| --- | ---: | ---: | ---: |
| 2 | 128 | 8.884777228838912e-9 | 2.6480431564775908e-8 |
| 2 | 32 | 8.884764873892975e-9 | 2.6480597187888764e-8 |
| 3 | 128 | 4.0440679432129645e-8 | 1.2094390497147087e-7 |
| 3 | 32 | 4.043999299611739e-8 | 1.209426411091589e-7 |
| 4 | 128 | 1.0790822549369285e-7 | 3.227318899228039e-7 |
| 4 | 32 | 1.0790150587210958e-7 | 3.227087993993582e-7 |

The entries are total joint KL upper bounds divided by 512 original receivers. A scalar field error bound must use the total forward KL, not this normalization; the largest total forward upper is 1.652387276404756e-4. Prefixes end at $5\times10^{-5}$, $7.5\times10^{-5}$ and $10^{-4}$ inference time. The largest $t=2$ quadratic-MGF guard is 8.514343126647528e-6, below one. Maximum parent-constraint and covariance-annihilation discrepancies are 4.440892098500626e-16 and 3.676152931232734e-21.

The [producer](https://github.com/cdenn016/MultiAgentELBO/blob/a4102c441a47c09ab02ab8e4eaa5fe5499a926de/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-recognition-filter.json) ran once from clean published `910e00d5`, taking 829.635797600029 seconds with cumulative process peak 956,702,720 bytes. Available RAM was 27,037,995,008 bytes, exceeding the frozen 6GiB guard. The [independent reader](https://github.com/cdenn016/MultiAgentELBO/blob/a4102c441a47c09ab02ab8e4eaa5fe5499a926de/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-recognition-filter-readback.json) passes 741 comparisons over 211,925,925 entries, with maximum discrepancy 1.2256862191861728e-13, taking 268.88676929997746 seconds and cumulative peak 947,441,664 bytes. Its analytic 2-by-2 exponential responses, complete coefficient interpolation and noise-factor QR path conditioning are independent of the producer. Archived hidden means are verification-only anchors. Source fixtures had thirteen passing JUnit cases; neither producer, reader nor those passing fixtures was retried.

The 37 NPZ outputs hold 709,128,352 logical array bytes and occupy 80,749,870 compressed bytes. Input/source snapshots occupy 15,087,436/195,945 bytes. Shared static context adds 978,400 logical bytes; complete retained histories, response banks and dense conditioning workspace remain charged. The [canonical replay manifest](https://github.com/cdenn016/MultiAgentELBO/blob/a4102c441a47c09ab02ab8e4eaa5fe5499a926de/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-n512-recognition-filter-package.json) contains 118 files totaling 96,279,674 bytes, with root-recorded canonical length/SHA256 parity and 61 input, 18 source and 117 reader bindings. The state remains O(N) with history-dependent dimension; dense path covariance costs O((Nn)^2). The comparison has explicit input, response, matrix-function, solve and contraction rounding exclusions and is not an interval or population/native-posterior certificate.

## Controlled conditional parent operation

The [parent construction](https://github.com/cdenn016/MultiAgentELBO/blob/910e00d5dfab122e5ab1750eca92c3a6d3cb07c7/docs/research/2026-10-03-latent-link-rg-plan/R3-CONDITIONAL-PARENT-UPDATE.md) averages the unchanged normalized raw kernel over the same-prefix hidden filter. Replacing that mixing law by the same-prefix Gaussian gives one-step forward KL at most the complete conditional path KL. The downward decoder is the regular conditional of this same approximate joint; inserting a mean force in a changed SDE is a different scientific law. A path error budget requires the actual-history expectation of the sum of prefix errors, which these six archived observations do not supply.

For $f(x)=x^TBx+b^Tx+c$, the Gaussian conditional expectation includes $\operatorname{tr}(BC_q)$, and its variance is $v=2\operatorname{tr}(BC_qBC_q)+(2Bm+b)^TC_q(2Bm+b)$. If $C_q\preceq c_qI$ and $D(p\Vert q)\leq K$, Gaussian quadratic exponential moments give $|E_pf-E_qf|\leq\sqrt{2vK}+2c_q\|B\|_{op}K$. Bare KL does not control arbitrary unbounded fields. Moving rooted mean drift can be cubic; the separate fixed-prefix density-domination/Hellinger bound requires a useful domination/tail budget. PR215 includes a helper grounded by three tiny Gaussian-pairing/tilt/coordinate fixtures for the next conditional field means, but no saved-prefix field-mean consumer has executed at this publication. Fresh original forecasts use $a,J_0^{-1},\pi$ and the future generator law; at fixed retained future-generator parameters they are independent of hidden recognition means. The filter concerns later recognition updates, rather than reinterpretation of that fixed original forecast kernel.

## Stationary conditional density: maximal energy and the remaining domain

The separate [weak-energy proof](https://github.com/cdenn016/MultiAgentELBO/blob/a4102c441a47c09ab02ab8e4eaa5fe5499a926de/docs/research/2026-10-03-latent-link-rg-plan/R5-CONDITIONAL-DENSITY-WEAK-ENERGY.md) concerns the admitted marked stationary native Fisher family and its local weak path limits, with original Fisher/source coefficients, frozen marks and chosen minimal cylinder-closure form unchanged. It is not a theorem about the numerical recognition proposal or nonstationary R0 starts. For every bounded whole-past event variable $A\in\mathcal F_s$ and finite $H$, let $r_t(x)=E_Q[A\mid X_t=x]$, including the entire frozen mark field. Finite-volume reversible dissipation and compact local integration by parts prove

$$
\int_s^{s+H}\mathcal E_{\max}(r_t,r_t)dt\leq\tfrac12E_Q[A^2].
$$

Here $\mathcal E_{\max}$ uses the full summed conditional weak gradients. The original compact-tail nest also approximates bounded $r_t$ by compact-nest-supported functions in this maximal energy, removing source-face/Gaussian-infinity localization at that level. These proofs improve the earlier conditional (EA) route; they do not establish membership in the chosen minimal closed form.

The precise remaining obligation is equation (14) of the source: approximate $r$ in time-integrated L2 plus full gradient energy by the enlarged finite cylinder algebra $\mathscr C_+$. An infinite product compact is not a finite cylinder. Boundary-force covariance terms still obstruct the available cylinder-approximation argument. Minimal/maximal domain equality or the specified minimal-form Mosco liminf would suffice but is unproved. Conditional on that approximation, (EA) and the existing whole-past Markov identification follow; without it, full stationary path-law identification remains open.

## Pinned source bytes

| Published input | SHA256 |
| --- | --- |
| R3-RECOGNITION-FILTER-RESULTS.md | 8e86a596b72149bab206f1e91edcba16988b2f910c374fd6175341fe71354831 |
| R3-RECOGNITION-FILTER-RECURSION.md | d786eb1e620ecb90640908e722bc1e794f2a7c685d0665d2589c3b37d124d37f |
| R3-GAUSSIAN-PATH-FILTER-BOUND.md | 0bcef4da344195e2c5b6a49c2011b64bead41b3f721067b4d8ed5639a111b1e6 |
| R3-CONDITIONAL-PARENT-UPDATE.md | 9c3a774d0a36cc99e6ffe19e34f9eeb6365fbff47a882443dd136a5362885d1b |
| R3-NONLINEAR-FILTER-CONTRACT.md | 65635722ba530f51b9a4e781738ffcab4e2ea6ab63c5ce27ad050db292646c73 |
| Producer receipt | cae6d93aaeed095e4e0bbc1f46180bc0957a575bfacf72316b3ec205294d8d93 |
| Reader receipt | 43bfe7ffbfa4760c41e8eeebfd86002d1c8ce0c7d6457f07f3b209af28fc8fe4 |
| Canonical replay manifest | 97a2da65bb881a451d0d3fa0cbdfe8e7e0bdfe72721a1f55d8871ca3eeac2614 |
| R5-CONDITIONAL-DENSITY-WEAK-ENERGY.md | 04e0662328a86416ef444a4aa8227de2b8a881f7094262bbb4c4f89ba8ea9561 |

## Relevance to this research

[[Natural gradient]], [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] gain a same-law nonlinear filter formulation and an executed short-prefix Gaussian comparison. The next material numerical operation is conditional quadratic field means with the full joint entropy budget, not a belief-covariance reset or another fixed forecast adapter. The separate stationary result narrows the outstanding whole-past identification problem to the chosen minimal-domain approximation. Unknown fine initialization, stopped/continuous residual control, native posterior accuracy, compact causal feedback, persistent formation, growing size/depth/horizon and all four RG gates remain open. Both scientific calculations used isolated sequential one-thread Anaconda CPU float64, allocating no CUDA tensors. The user owns the GPU and the 144-case CUDA grid remains unrun. This intake launches no scientific work and edits no model, manuscript or older immutable source.
