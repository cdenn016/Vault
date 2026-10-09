---
type: run
title: "Initialized actual-history information and directed filter KL"
aliases: ["N512 initialized actual-history KL average", "Directed non-Gaussian recognition information recurrence"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Initialized actual-history information and directed filter KL

Codex (2026). *Initialized actual-history information and directed filter KL*. MultiAgentELBO [PR256](https://github.com/cdenn016/MultiAgentELBO/pull/256), commit d52e39f3bf96ec593689ae338668584090735b3f and merge c4b5214511ee8343e036ec214dccbcfe0406ec24, publishes two mathematical records. For a fixed known full initialization and either supplied parent forest separately, the actual two-update average of the complete causal Gaussian-reference KL is finite. A directed extension charges inherited KL once plus chart information evaluated under the actual old non-Gaussian filter. It gives finite almost-sure conditional comparisons at every finite prefix, while the next outer information average a2 and later averages remain unresolved. The existence estimate supplies no useful numerical or size/depth-uniform allowance. All four RG completion gates remain open; the roughly 65% planning estimate is unchanged.

```bibtex
@misc{codex2026actualinformation,
  author = {Codex},
  title = {Initialized actual-history information and directed filter KL},
  year = {2026},
  howpublished = {MultiAgentELBO mathematical checkpoint PR256},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/256}
}
```

## Fixed initialized law and complete reference

The [initialized-average record](https://github.com/cdenn016/MultiAgentELBO/blob/c4b5214511ee8343e036ec214dccbcfe0406ec24/docs/research/2026-10-03-latent-link-rg-plan/R3-FIRST-ACTUAL-INFORMATION-AVERAGE.md) fixes deterministic complete fine prestate X0 and finite observation/model inputs at c_*. The exact-real, unselected finite-q9 raw recognition law retains N512, E1024, GL(2), matter dimension two, four generator/three observed slices, mass 16, h=1/40000 and T=.05. Initial covariances/precisions are positive and all fixed fields finite. The supplied 128-parent and 32-parent forests are alternatives, each treated separately. There is no source/noise cutoff, success or exit conditioning, rounded-weight renormalization or new dynamics.

The hidden xj consists of selected recognition means, not newly drawn latent matter. Hj carries the available retained history, moving parent observations and fixed charged inputs. The actual conditional eta_j is compared with the complete physical Gaussian qj produced by the causal reference recurrence. qj is not a product of free-parent marginals, a reset of eta_j or a future-smoothed law. Conditional Gaussian measures handle singular observation fibers without ambient inversion or jitter. The first updated actual filter is exactly eta1=q1.

## First actual-history average

The first selected-mean update is x1=mbar0+LQ xi with Q0=LQ LQ^T positive and the original Cholesky noise orientation. Its Gaussian driver is independent of the first retained updates at the fixed old state. In these coordinates the rooted observation projector is

$$
P_A=L_Q^TA^T(AQ_0A^T)^{-1}AL_Q,
\qquad
m_1=\bar m_0+L_QP_A\xi,
\qquad
C_1=L_Q(I-P_A)L_Q^T.
$$

Orthogonality gives norm(m1)<=norm(mbar0)+sqrt(norm(Q0)) norm(xi) and 0<=C1<=Q0. This controls the physical conditional Gaussian without a random-readout conditioning or norm bound. It preserves the moving readout's dependence on the retained state.

Let U and V be norms of the finite-dimensional first mean and covariance Gaussian drivers. The record bounds both physical covariance and inverse covariance by a fixed multiple of exp(2 alpha V), alpha=sqrt(T h). Complete exact finite-node matrix exponential/Frechet responses, precision-Cholesky differentiation and natural whitening bound the affected quadratic chart coefficients. Source-whitening inverse is globally bounded by (2 T h)^(-1/2), including arbitrarily small positive source weights. Original sender, shared-copy, reversal and supported-record terms remain charged; constants cancel only from chart variance. The exact finite-q9 derivative field is used, rather than substituting its optional guarded polynomial helper.

For all 15,872 original chart rows this yields a logarithmic majorant

$$
\log(1+v_b)\leq K_0+K_1U+K_1\exp(\alpha V),
\qquad
v_b=\operatorname{Var}_{q_1}f_b.
$$

Both E U and E exp(alpha V) are finite under the original first Gaussian drivers. The latter has the crude bound exp(alpha^2) 2^(dV/2). Constants depend on the fixed prestate, data, model and finite row counts, and can be enormous; this establishes integrability rather than a usable error number.

Starting from actual eta1=q1, the unchanged second raw update creates the actual joint J(R2,x2). The normalized comparison is its actual retained marginal times the complete Gaussian endpoint predictor. Adjoining the same moving parent observation and applying the KL chain gives

$$
\mathbb E_{\mathrm{actual}\,H_2\mid H_1}D(\eta_2\Vert q_2)
\leq\mathcal I(H_1),
\qquad
\mathbb E_{\mathrm{actual}\,H_2}D(\eta_2\Vert q_2)<\infty.
$$

Every identical measurable normalized future kernel contracts this averaged KL. A literal rounded finite-q9 forecast functional needs an explicitly declared unit-mass normalizer to qualify as such a kernel; this does not normalize the drift weights. The finite two-update average is compatible with the earlier infinite frozen-center entropy and individual signal-moment averages, which concern different comparisons. No actual-history numerical integration, random-initialization/data average, horizon-uniform bound or continuous-Fisher/fixed-prior conclusion is supplied.

## Directed extension under the actual non-Gaussian filter

The [directed-recurrence record](https://github.com/cdenn016/MultiAgentELBO/blob/c4b5214511ee8343e036ec214dccbcfe0406ec24/docs/research/2026-10-03-latent-link-rg-plan/R3-ACTUAL-INFORMATION-KL-RECURRENCE.md) fixes an available old history H and actual eta, with complete Gaussian q at that same history. Write k(H)=D(eta||q), T_H for the unchanged retained/selected-mean transition and Phi_H for its selected-mean kernel. The actual next joint is J_eta=eta T_H, with endpoint marginal mu_eta=eta Phi_H; phi_q=q Phi_H is the complete Gaussian predictor. The comparison L=J_(eta,R') tensor phi_q keeps the actual new retained marginal. The exact chain decomposes

$$
D(J_\eta\Vert L)
=D(\eta\Phi_H\Vert q\Phi_H)+I_{J_\eta}(x';R'),
\qquad
D(\eta\Phi_H\Vert q\Phi_H)\leq k(H).
$$

After adjoining the same moving observation M'=A(R')x', the conditional Gaussian of L is the original complete q_next. Dropping the nonnegative retained-observation marginal term gives

$$
\mathbb E_{\mathrm{actual}\,Y'\mid H}D(\eta_{\mathrm{next}}\Vert q_{\mathrm{next}})
\leq k(H)+\mathcal I_\eta(H),
\qquad
\mathcal I_\eta(H)=\tfrac12\sum_b\log(1+\operatorname{Var}_\eta f_b).
$$

Inherited KL appears once. No KL triangle, filter reset, expectation under a hybrid-history law or fixed-prior moment transfer enters this step. The original retained charts invert to f_H(x)+independent standard Gaussian noise, with any further hidden-independent noise kept separate. For a non-Gaussian eta, an auxiliary Gaussian output law and the KL chain bound noisy-chart information by its covariance/logarithmic capacity. Gaussian maximum entropy, chain rule and common-kernel contraction are the primary results in Polyanskiy and Wu, [*Information Theory*](https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf), Theorems 2.8 and 2.15–2.17; the repository records reconstruct this application.

The actual quadratic variance depends on joint third and fourth moments, not Gaussian pairing or covariance alone. Existing finite-prefix conditional moment control makes the information allowance finite almost surely; it does not establish outer integrability. The saved Gaussian-only consumer in [[multiagentelbo-2026-10-09-chart-information]] cannot evaluate this new non-Gaussian allowance.

Writing Dbar_j=E_actual Hj D(eta_j||qj) and a_j=E_actual Hj I_(eta_j)(Hj), the directed recurrence is Dbar_(j+1)<=Dbar_j+a_j, with nonnegative extended expectations. The initialized proof gives Dbar1=0, a1 finite and Dbar2 finite. Iteration also gives finite k_j almost surely at each finite raw history. Neither conclusion makes a2 or later outer expectations finite. Shared normalized future kernels contract the corresponding average, which may be infinite at unresolved later steps.

## Provenance, remaining obligation and scope

The [source intake](https://github.com/cdenn016/MultiAgentELBO/blob/c4b5214511ee8343e036ec214dccbcfe0406ec24/docs/research/2026-10-03-latent-link-rg-plan/evidence/r3-actual-information-source-intake-20261009.json) binds fourteen repository sources and three live manuscript sources. The relevant live sections are the raw sample-record law in g11_latent_links.tex, prop:glink-sample-record; recognition flow in c08b_lie_links.tex, prop:link-recognition-flow; and the regular-filter definition/open parent-dynamics question in c11_network_coarsegraining.tex. They retain their own raw/continuous/regular scopes. Actual canonical Code main, main ref and origin/main agree at c4b5214511ee8343e036ec214dccbcfe0406ec24 with a clean checkout. Its administrative handoff receipt SHA256 is bcf3a125f0d44904ced8b215d36e53ccb3901e852c9c159a678eea90bb5b7b22.

| Published record | SHA256 |
| --- | --- |
| Initialized first actual-history average | 482866786e938c165a30383affd6a96edf033abe5474fa03f028cdfbcf8945af |
| Directed actual-information recurrence | c13e0d243a503b8ed0fbe2cc0b72b13551fc16ea4ebdb32060a2d32fbffbf0ba |
| Source intake | 241e4511a1cdb602536cd2966850ad4e212f466bbd2f4092e17390d2ddec7c39 |

The next obligation is the actual H2 average a2, or the sharper actual H2 average of endpoint/retained mutual information at the third update, with a finite and useful allowance. Later outer history averages, operational nonlinear assimilation, compact native memory, regular-class closure, growing network size/depth and persistent endogenous formation remain open. No directed sum against a projected product reference, useful uniform allowance or original-record accuracy follows automatically. All four RG gates stay open. This intake records published mathematical arguments only; no new scientific execution, tests, GPU use, model/configuration or manuscript edit occurs.

[[Staged hierarchy formation and RG composability]] carries the initialized-average progress and the actual-filter recurrence alongside these limits. [[Renormalization-group flow of beliefs]] separates finite-prefix conditional control from averaged and growing-family closure. Earlier [[multiagentelbo-2026-10-09-chart-information]], [[multiagentelbo-2026-10-09-joint-word-carrier]] and [[multiagentelbo-2026-10-09-second-history-expectation]] remain immutable historical records.
