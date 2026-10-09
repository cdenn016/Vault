---
type: run
title: "Population recognition moments and original-record decoder transfer"
aliases: ["Population decoder transfer", "Growing-block recognition record-information bound"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Population recognition moments and original-record decoder transfer

Codex (2026). *Population recognition moments and original-record decoder transfer*. MultiAgentELBO [PR259](https://github.com/cdenn016/MultiAgentELBO/pull/259), source commit 2166c006d72c8aecdd0b31506f151de64b447390 and merge 47d54a7cda45002e8a5846209ded97aadb031721, publishes R2-POPULATION-DECODER-TRANSFER.md. The original T=0 unit-Fisher population descent supplies a time/volume-uniform row-weighted generator recognition second moment under the ideal finite preparation law. That bound transfers the existing shared-geometry decoder and normalized-window information estimate to its evolving recognition law. A supplied growing-block hierarchy retains increasingly many parents while its fixed-query original-record information loss tends to zero. This concerns fresh baseline matter and original source labels under recognized generators. Accuracy against the exact native posterior, numerical or finite-q9 transfer, continuation beyond the supplied window, complete state coding and persistent formation remain open. All four RG completion gates remain open; the roughly 65% planning estimate is unchanged.

```bibtex
@misc{codex2026populationdecodertransfer,
  author = {Codex},
  title = {Population recognition moments and original-record decoder transfer},
  year = {2026},
  howpublished = {MultiAgentELBO mathematical checkpoint PR259},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/259}
}
```

## Law and inherited construction

The declared family is V_k=(Z/(16k)Z) times (Z/(32k)Z), N_k=512k^2, at fixed c_*. It has real GL+(2) links with two owned primitives per cell and shared inverse reversals, four generator episodes, three observed matter/source episodes, generator prior precision aI4 with a=100/9 and zero anchor, mass 16 and loop coefficient 1/4. Future matter has the original baseline N((.7,-.4),I2); record noise is N(0,I2); each self-free nearest-neighbor receiver has four source slots with original pi=1/4 and tau=1. Incoming and outgoing candidate-incidence caps are four. The graph supplies no base-manifold transport.

For the complete frozen preparation/data mark field w, X_k(t;w) is exact continuous zero-thermostat, unit-mobility population joint Fisher descent from the prescribed baseline. [[multiagentelbo-2026-10-09-nonstationary-population-flow]] supplies finite-volume global existence, nonincreasing nonnegative shifted energy E_k(t;w), and the uniform expected initial energy density M_pop. Preparation uses the declared finite-MH candidates, with the selected truth allowed to be global and dependent. It is not the exact nonlinear tilted-prior law. The present result requires neither successful finite-budget fitted startup nor stationary recognition.

At time t, R_{k,t}^w is the product Gaussian recognition law of the full primitive generator histories. Episode-3 forecast generators are drawn from that law. Fresh matter, source labels pi and original record noise are then drawn independently. Fitted prefix matter means/covariances and beta remain provenance coordinates, rather than replacing the future matter/source law. Inference uses the observed prefix; an archived future record is an evaluation query.

This extends the existing incident-cache and normalized-channel constructions to R_t. The old fixed-model rho_h posterior-average cancellation supplies no evolving-recognition moment; here that moment follows directly from original population energy. [[multiagentelbo-2026-10-09-joint-word-carrier]] and the actual-history notes remain separate results with their own laws and obligations.

## Correctly weighted recognition moment

For one d=4 generator factor N(m,C) with prior N(0,a^-1 I), let K_gen be its exact prior KL and lambda_l the eigenvalues of aC. The source proves

$$
K_{gen}=\frac12\left[a\|m\|^2+\sum_{l=1}^d(\lambda_l-\log\lambda_l-1)\right],

a\mathbb E_R\|\omega\|_F^2\leq4K_{gen}+2d\log2.
$$

The scalar inequality log lambda<=lambda/2+log2-1 controls covariance trace. This bounds generator coordinates, without requiring exponential moments of evolved link matrices. Frobenius reshaping and reversal signs preserve the square.

Put v_e=E_{R_{k,t}^w}||omega_e^3||_F^2. Each primitive appears in both endpoint source rows with weight 1/4, so the correct row-weighted average is

$$
\overline M_k(t,w)
=\frac1{N_k}\sum_{i,\alpha}\pi_i(\alpha)v_{e(i,\alpha)}
=\frac1{2N_k}\sum_{e\in E_+}v_e,
 |E_+|=2N_k.
$$

The nonnegative original energy dominates all generator prior KLs and is bounded by its initial value. Consequently

$$
\overline M_k(t,w)\leq
\frac{2E_k(0;w)/N_k+8\log2}{100/9},

\sup_{k,t\geq0}\mathbb E_w\overline M_k(t,w)
\leq M_R=\frac{2M_{pop}+8\log2}{100/9}<\infty.
$$

The supremum is over expected moments at deterministic inference times. It is not a per-link deterministic bound or a maximum over the network. M_pop is the explicit finite, potentially large analytical baseline envelope in the preceding population record; no useful .01-nat numerical allowance is inferred.

The same pathwise initial-energy majorant permits an almost-surely finite measurable clock selected from preparation/population trajectories before drawing the receiver query and fresh forecast variables. No optional-stopping identity is needed. This corollary keeps the original input law: query-adaptive clocks, conditioning on clock existence and successful-only startup reweighting are excluded.

## Shared incident decoder and exact normalized window

A query S is an independent uniform subset of r distinct original receiver rows. One full generator component G supplies the supported incident primitives and all source/copy/sign metadata. Its unique receivers and supported sources share the same fresh fine matter coordinates. For source pattern alpha, D_alpha has rows E_i-exp(s omega_e)E_j, with contributions on a repeated fine node in the same columns. The exact marginal record decoder is

$$
q_C(o)=\sum_\alpha\pi_S(\alpha)
\mathcal N\left(o;D_\alpha a_{U_S},I_{rK}+D_\alpha D_\alpha^T\right),
 K=2.
$$

Every covariance is at least I, the source masses sum to one, and the density is positive in original record units. Repeated or reversed links refer to the same primitive. The prefix-only recognition forecast is exactly the integral of q_{C_S(G)} against R_{k,t}^w. Extracting this cache preserves that forecast when its correct joint cache law is retained; it supplies no comparison of recognition to the native posterior or truth.

Supply a compatible nested hard rooted hierarchy with nonempty connected parents, finite-word transports, deterministic positive weights and full-rank readouts. Its hierarchy/tree/phase is fixed before the independent query and future matter/labels. Write P_0 for the initial raw readout, Q_0=P_0P_0^T, W_0=Q_0^-1/2 P_0 and Y_0=W_0 xi. Adjacent raw maps C_j induce coisometries A_j=Q_{j+1}^-1/2 C_j Q_j^1/2, so Y_{j+1}=A_jY_j and A_jA_j^T=I. This is Gaussian coordinate normalization; actual noncommuting product order is retained.

The joint carrier contains the incident cache, all adjacent normalized channels, the sparse node blocks L_u=W_{0,I_0(u),u}, initial-parent identities and tree/phase/depth/support tags, all pushed forward from that same G. With F_alpha=D_alpha W_0^T and V_alpha=I+D_alpha D_alpha^T, the exact conditional bridge is

$$
O_S\mid Y_0=y,\alpha,\mathcal K_S^+
\sim N(D_\alpha a_{U_S}+F_\alpha y,R_\alpha),

R_\alpha=I+D_\alpha(I-W_0^TW_0)D_\alpha^T\succeq I.
$$

Sparse assembly adds shared-parent contributions. At deeper windows the actual ordered channel product supplies the cross covariance. Omitting L_u leaves a contracted information comparison but loses the directly evaluable target conditional. Independent catalog/channel/node-block marginals cannot replace the joint pushforward.

Let P retain the true original record/window joint and Q retain its same geometry, query and normalized window marginal while drawing the record from q_C independently of the window at that geometry. Both laws use the same free-coordinate Gaussian graph measure, including the deterministic adjacent-channel constraints. They do not use a Lebesgue density on every depth coordinate. Before carrier projection, their KL equals I(O_S;Y_{0:D}|G,S,w,t)=I(O_S;Y_0|G,S,w,t). Projecting to the same full carrier can only reduce KL.

## Growing-block original-record information allowance

For initial block volume v=N_k/B_0 and any threshold s>0, the source reconstructs the good/bad-row bound. Normalized projection leverage sums to KB_0; uniform query inclusion is r/N_k; incoming incidence is capped by four. Good rows use ||exp(plus/minus omega)||<=e^s. Bad rows use original positive-noise Gaussian conditioning and the logarithmic record charge controlled by E||omega||_F^2. Geometry and readout projection may remain dependent.

Joining both comparisons to their identical preparation law gives

$$
D(P_{k,t}^{\mathcal K}\Vert Q_{k,t}^{\mathcal K})
\leq r\left[
\frac K v(1+4e^{2s})
+\frac K2\left(\frac{\log3}{s^2}+\frac2s\right)M_R
\right].
$$

This is one jointly scored original-record vector in nats; division by r gives nats per original record. Its allowance has no extra window-depth factor, since a window containing Y_0 adds no fresh matter at known channels. Hiding independent source labels and projecting to the common carrier use the same-law information contraction. The hierarchy cannot be chosen adaptively from the query.

For 0<alpha<1 and s=(alpha/2)log v, K=2 yields

$$
\varepsilon_R(v)=
\frac2v+8v^{\alpha-1}
+\frac{4M_R\log3}{\alpha^2(\log v)^2}
+\frac{4M_R}{\alpha\log v}\longrightarrow0.
$$

Fixed r gives vanishing total vector KL; more generally r=o(log v) suffices. There is no all-row conclusion with r=N_k.

A supplied compatible dyadic diagonal takes k_n=2^n, n>=4, initial stage ell_0=floor(n/2), and window depth D_n=floor((n-ell_0)/2). Then N_n=512*4^n, v_0=4^ell_0 tends to infinity, and endpoint parent count B_{D_n}=512*4^(n-ell_0-D_n) also tends to infinity. Both initial and endpoint parent counts survive. For each fixed r the deterministic-time annealed discrepancies are bounded uniformly over t by r epsilon_R(v_0(n)), which vanishes. The pre-query finite-clock corollary has the same allowance on the unchanged input law.

This is a vanishing information loss from dropping hypothetical parent context within the declared forecast joint. It is not a predictive benefit, accuracy gain against original truth, recognition-to-posterior KL, inference-time path KL, pathwise maximum-record guarantee, weak convergence of the changing-dimensional whole carrier, autonomous RG transition, or compatible continuation beyond the supplied window. The growing readouts are not promoted to continuous local functions of the rooted population path limit.

## Sparse channel precision and fully charged state

The query cache retains at most 4r unique primitives and 5r unique fine nodes. Under uniform pi=1/4, its maximum X_* satisfies E X_*^2<=4r M_R and E X_*<=sqrt(4r M_R), uniformly in deterministic time and volume. This unweighted-incidence transfer is not asserted for general nonuniform pi.

Keep the incident cache and L_u exact and apply the existing signed binary-grid/row-polar code to adjacent coisometries. For per-vector per-depth record tolerance epsilon>0 and b_*=4, the expected channel precision is bounded by

$$
\mathbb E b\leq
2+\log_2(2DK\sqrt{b_*})
+\frac12\log_2^+\left(\frac5{2\epsilon}\right)
+\frac12\log_2(1+2rK)
+\frac{\sqrt{4rM_R}}{\log2}.
$$

The smoothing comparison uses the same actual Y_j, source masses, component coupling and coded-carrier marginal. Its conditional original-record KL allowance is separately charged at each depth. No KL triangle combines it with the context-dropping bound; no density KL between differently constrained deterministic windows follows. Precision grows logarithmically with supplied depth and inverse tolerance. Matrix-exponential, square-root, exact-cache and node-block arithmetic errors remain separate.

Per complete component, channel values require at most (4/3)K^2 B_0 scalars; incident generator coordinates and node blocks require at most 4rK^2 and 5rK^2 scalars. The signed channel grid plus its precision integer uses at most m_ch(b+2)+2b+3 bits before indices/tree/phase/support tags. Exact incident and node coordinates remain real-valued, so this is a channel code rather than a complete finite-bit state codec. Source-pattern enumeration has 4^r components and record covariance uses O((rK)^2) workspace per pattern.

Every whole-component bank retains its normalized masses, identities and joint provenance and multiplies component-specific storage by its size. No continuous-recognition integration or required component-count bound is supplied. Equality for an extracted finite bank does not certify the continuous target bound for the archived 256-component rule. Full frozen inputs, integration/workspace history and original geometry preprocessing remain charged. Four episodes of dense 2N generator means and 4-by-4 precision matrices alone contain 160N stored recognition scalars; the future slice contains 40N. Subextensive query-channel output on the diagonal does not remove those costs. Internal/non-tree/parallel/reversed original copies and words remain part of complete source geometry; omitted copies cannot be evaluated from this cache.

## Source binding and epistemic status

The completed record used one constructive source/derivation round, followed by the parent's full reconstruction of coercivity, weighted incidence, the joint decoder/window law, diagonal, random-clock scope and sparse precision. It is a mathematical source checkpoint, without a formal verification-ledger closure. No simulation, sampler, scientific producer, test or GPU work occurred. This ingestion writes only the new immutable source and existing theme/index/log, with one vault lint; manuscripts, scientific model and previous source notes remain unchanged.

| Published item | Bytes | SHA256 |
|---|---:|---|
| R2-POPULATION-DECODER-TRANSFER.md | 30334 | 94c8aaed613eb2fb3cd8787b952e54ef7c057c4a3724841178ec934f08a513e1 |
| evidence/r2-population-decoder-source-intake-20261009.json | 5269 | 2c133a514039207a5a8e5653ca7c6c820bbc36db815d5cea6dfd1aaab06ec672 |
| artifacts/r2-population-decoder-handoff-20261009.json | 574686 | 085f9ebab297e62d07d0cfadbcc122bb5f5d1449017569d1d31e5d95591c5a2f |

The source inventory binds nine repository records and three live theory files. Relevant live reads are c06_attention.tex, def:obs-attention-label-model; c10_network_state.tex, rooted datum, linear cross-scale maps and composite-tree composition; c12_multiscale_vfe.tex, def:full-graph-coarse-links and its all-copy properties. Their bytes match the published inventory. The cited wiki context is explicitly historical, as of Research 56f54cec before the Code258 ingest; it is not a claim that the subsequently updated theme retains its former hash.

The information-theory background is Polyanskiy and Wu, [*Information Theory*, August 16, 2024 author-hosted edition](https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf), Theorem 2.15 (chain rule, printed p.32/PDF zero-based p.56), Theorem 2.17 (KL contraction, pp.34–35/PDF pp.58–59), and Theorem 3.7(c) (mutual-information contraction, p.52/PDF p.76). Those statements were checked in the primary text. They supply measure-theoretic identities, while original energy/coercivity and the component/window calculation supply this native recognition moment and record allowance.

Actual canonical Code main, HEAD and origin/main were confirmed at 47d54a7cda45002e8a5846209ded97aadb031721 before ingestion. The administrative handoff receipt matches both canonical and implementation copies. It records preservation and source/parity checks rather than additional mathematical evidence.

## Relevance to this research

This record links the positive population path construction to an explicit original-record consumer under its evolving recognition law, preserving shared noncommuting geometry and original source/matter kernels. It advances [[Staged hierarchy formation and RG composability]] with a growing-block, surviving-parent information allowance instead of assuming recognition obeys the exact-posterior Bayes cancellation.

The next named obligation is controlled continuation of the retained joint carrier beyond its supplied window, retaining the required original-copy, word and raw evaluator with original-record error under this recognition law. Quantitative transfer to the numerical/native posterior process remains a separate obligation, as do the second model channel, all-copy evolving compression, soft/adaptive membership and endogenous persistent hierarchy. All four RG completion gates remain open at roughly 65%. No GPU is needed for this source-only intake.
