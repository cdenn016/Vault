---
type: run
title: "Native minimal Fisher recovery: covariance and Mosco endpoints"
aliases: ["R5 final minimal-form recovery checkpoint", "R5 covariance and Mosco endpoints"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Native minimal Fisher recovery: covariance and Mosco endpoints

Codex (2026). *Native minimal Fisher recovery: covariance and Mosco endpoints*. [Code PR270](https://github.com/cdenn016/MultiAgentELBO/pull/270), source 8f86b9ee216fb5fe7f6bce29bdc005740e5f60a8 and merge 4c44d2bad3d6f9db0c67fd79be1609309065639d, publishes [R5-BOUNDARY-COVARIANCE-ATTEMPT.md](https://github.com/cdenn016/MultiAgentELBO/blob/4c44d2bad3d6f9db0c67fd79be1609309065639d/docs/research/2026-10-03-latent-link-rg-plan/R5-BOUNDARY-COVARIANCE-ATTEMPT.md) and [R5-MINIMAL-MOSCO-ATTEMPT.md](https://github.com/cdenn016/MultiAgentELBO/blob/4c44d2bad3d6f9db0c67fd79be1609309065639d/docs/research/2026-10-03-latent-link-rg-plan/R5-MINIMAL-MOSCO-ATTEMPT.md). These are the second and third, final bounded rounds following [[multiagentelbo-2026-10-09-minimal-conditional-domain]]. The covariance route stops at an unproved weighted susceptibility estimate. The Mosco route establishes core diagonal recovery and reconstructs sufficient full-domain recovery implications, while their native interfaces remain unproved. This ends the three-round investigation without minimal admission, full-past-law identification, a same-model counterexample or an RG-gate closure. All four gates remain OPEN at roughly 65%.

```bibtex
@misc{codex2026minimalformrecovery,
  author = {Codex},
  title = {Native minimal Fisher recovery: covariance and Mosco endpoints},
  year = {2026},
  howpublished = {MultiAgentELBO research checkpoint PR270},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/270}
}
@article{kuwae2003convergence,
  author = {Kazuhiro Kuwae and Takashi Shioya},
  title = {Convergence of spectral structures: a functional analytic theory and its applications to spectral geometry},
  journal = {Communications in Analysis and Geometry},
  volume = {11},
  number = {4},
  pages = {599--673},
  year = {2003},
  url = {https://intlpress.com/site/pub/files/_fulltext/journals/cag/2003/0011/0004/CAG-2003-0011-0004-a001.pdf}
}
```

## Retained native process and exact admission target

The fixed-c_* increasing real GL+(2) lattice family, finite record/primitive/source/loop/episode catalogs, admissible compact core marks, positive baseline/noise spectra, supported prior floor, rooted observation second moment, first local-action moments and fixed 0<T<1/d_max remain. Gaussian recognition blocks retain the full mean/covariance Fisher metric. Source rows retain the original ordinary simplex Lebesgue reference and categorical Fisher mobility in independent interior coordinates. The entire core/observation mark field is frozen with zero energy; all sender, receiver, loop and adjacent-episode terms remain.

P_n are rooted finite stationary marked laws, P is their admitted local weak interior DLR limit, and Q_n converges along an admitted stationary reversible continuous local path subsequence to Q with marginal P. A finite periodic lift evaluates fixed cylinders but is not an infinite DLR law: remote copies reveal finite coordinates, so its conditional specification cannot be identified with P. Native finite forms count each torus block once. The continuous exact-population recognition law remains separate from the latent generator Gibbs history and fitted nonstationary finite-quadrature proposal.

For a bounded continuous finite-past cylinder A through s and I=[s,s+H], use its identical native pullback A_n and the actual densities r_n(t)=E_Qn[A_n|X_t^n], r(t)=E_Q[A|X_t]. These have the supplied uniform bound ||A||_infinity, convergence against bounded continuous time/state cylinders, and integrated finite energy allowances at most E_Qn[A_n^2]/2, whose allowances converge to E_Q[A^2]/2. This does not assert convergence of their energies. The target is admission to the previously chosen minimal cylinder closure V=D(E_min), with the pure-energy liminf

$
r\in L^2(I;V),\qquad
\int_I\mathcal E_{\min}(r_t)dt
\leq\liminf_n\int_I\mathcal E_n(r_n(t))dt
\leq\tfrac12 E_Q[A^2].
$

The last inequality uses the supplied finite energy allowances. Such admission would yield the original finite-time-step enlarged-cylinder approximation, then the recorded enlarged-source implication to full-past stationary path-law identification for this same P. Bounded finite-past cylinders suffice through the recorded bounded L2(Q) approximation and energy estimate for differences. These consequences remain conditional.

## Second round: exact boundary stack and unproved weighted susceptibility

Retain the first proof's compact-localized actual density u_k=r_t(1-H_k), all-mark conditioning G_B=sigma(w,x_B), conditional expectation Pi_B, projection v_k,B=Pi_Bu_k and original inverse Fisher A_i. The first proof already admits each fixed finite projection to V and identifies its derivative's exact original drift covariance J_i. The native dependency boundary includes every sender, receiver, primitive record, loop and temporal dependency.

For the own-block smooth cutoff chi_k,i and symmetric interior square root, the second record defines the finite centered dual-Fisher force stack

$
\zeta_{i,k}=A_i^{-1/2}\chi_{k,i}b_i,\qquad
Z_{i,k}^B=\zeta_{i,k}-\Pi_B\zeta_{i,k},\qquad
G_{k,B}=\Pi_B[Z_{k,B}Z_{k,B}^T],\qquad
\lambda_{k,B}=\lambda_{\max}(G_{k,B}).
$

Localized drift-square integrability makes each fixed finite stack well-defined. Own-block volume, mobility-divergence, baseline and entropy terms cancel after centering. The remaining stack is the original crossing interaction-force fluctuation, with no averaged-force replacement. Finite range specifies the dependencies but does not make exterior-conditioned boundary components independent.

With delta_k,B(t)=Pi_B[(u_k-v_k,B)^2], conditional Cauchy-Schwarz applied to the stack's maximizing retained-state direction gives the exact covariance equality and operator bound (second record, Eqs.5-6),

$
C_{k,B}=(A_i^{-1/2}J_{i,k}^B)_{i\in\partial B}
=\Pi_B[(u_k-v_{k,B})Z_{k,B}],\qquad
\sum_{i\in\partial B}(J_{i,k}^B)^T A_i^{-1}J_{i,k}^B
\leq\delta_{k,B}\lambda_{k,B}.
$

For every nested exhaustion B_n, the integrated residual variance tends to zero by conditional expectation convergence, and 0<=delta_k,Bn<=||A||_infinity^2. Every fixed eigenvalue is integrable, bounded in expectation by the finite stack's drift-square trace. These facts supply no rate pairing variance decay with growing weighted susceptibility. The unproved sufficient estimate (second record, Eq.9) is, for each fixed k,A,I, some nested exhaustion with

$
\sup_n\int_I\int\delta_{k,B_n}(t)\lambda_{k,B_n}dPdt<\infty.
$

If established, this would give the first proof's CP exactly as stated: a finite per-cutoff exhaustion covariance bound, without required vanishing or uniformity in k. It is an unadopted additional sufficient estimate, not a necessary criterion or a proved native consequence; the density's actual covariance direction may be smaller than the largest eigenvalue.

Native stationarity and reversal give the valid additive-functional bound E_Q|integral_a^(a+h) Lf(X_t)dt|^2<=2h E_min(f), directly from the forward and reverse cylinder martingales. Dividing by h produces a bound 2h^-1 E_min(f), which diverges as h decreases. This time-integrated estimate neither bounds the equal-time conditional covariance matrix nor makes its interacting drift fluctuations diagonal noise. Conditioning the instantaneous drift on retained current state also does not identify the projected path's past-filtration drift. Assuming that projected process Markov, or representing r_t by the chosen minimal semigroup, would import the unresolved identification. No mixing, curvature, global score/inverse-mobility or conditional-normalizer bound is added. The round neither proves CP nor disproves actual minimal admission.

## Third round: genuine core recovery and the full adjoint interface

Let H=L2(P), K=L2(P;direct-sum_i R^d_i), and

$
(B_0f)_i=\sqrt T A_i^{1/2}D_if,\qquad
B=\overline{B_0},\qquad
D(B)=V,\qquad
\mathcal E_{\min}(f)=\|Bf\|_{\mathsf K}^2.
$

B_n is the corresponding closed native finite-torus gradient. Concrete scalar cylinders and localized finite-component vector cylinders supply dense comparison representatives; frozen marks remain in their Hilbert spaces and are not differentiated. Fixed comparison norms and pairings converge because their integrands are bounded continuous and local. Pullbacks J_n apply to those representatives rather than arbitrary P-equivalence classes.

For every fixed enlarged-core f, eventual support injection gives its original finite-form pullback and convergence of both its norm and native energy. Compact Gaussian derivative supports and bounded source derivatives/categorical mobility make those energy integrands bounded local tests. Form-core approximation followed by increasing volume thresholds yields a genuine diagonal f_n converging strongly to every f already in V, with E_n(f_n) converging to E_min(f). Finite time sums and a second diagonal extend recovery to functions already in L2(I;V). This is the established limsup statement (third record, Eqs.6-7); it does not admit a weakly convergent sequence to V.

The sufficient full-adjoint recovery interface is

$
\text{For every }\phi\in D(B^*),\ \text{there exist }\phi_n\in D(B_n^*)
\text{ with }\phi_n\to\phi,\quad B_n^*\phi_n\to B^*\phi
\text{ strongly in their comparison spaces.}
\tag{AR}
$

The source reconstructs its conditional implication. A bounded-gradient subsequence has a weak vector limit V with ||V||^2 bounded by the pure energy liminf. Passing the finite adjoint identities against strongly recovering tests gives <V(t),phi>=<r(t),B*phi> for every phi in the full adjoint domain, outside a common null set obtained from a countable graph-dense family. Closedness and B**=B then give r(t) in D(B), Br=V and the exact sharp liminf. No unproved limiting scalar-norm subtraction is used.

The existing compact local force-square control already supplies formal adjoint identities on appropriately localized smooth finite-component vector fields. Those tests recover their native finite-volume adjoints when complete active dependency neighborhoods and marks are localized. The gap is recovery of the entire D(B*) graph, or proof that these recoverable tests are graph-dense there. Density in K and scalar form-core density do not establish adjoint graph-core density. Testing only local vector fields gives the already established maximal weak domain. The capacity nest does not approximate arbitrary adjoint fields and their divergences uniformly across volumes. AR remains unproved; no new local drift-integrability gap, source-face extension or replacement maximal domain is introduced.

## The existing candidate's uniform Galerkin-resolvent interface

The sole already-created final Exa candidate gives another sufficient formulation within this same Mosco route. Put a_n=<.,.>_n+E_n and a=<.,.>+E_min, and choose nested finite-dimensional concrete cylinder spaces S_m whose union is form-dense after deleting limiting linear dependencies. For each fixed cylinder h, the finite and limiting Galerkin solutions g_m,n and g_m have converging fixed-m Gram matrices. This establishes fixed-m approximation only. With L=-B*B, L_n=-B_n*B_n, u=(1-L)^-1h and u_n=(1-L_n)^-1J_nh, the additional unproved uniform residual is

$
\lim_{m\to\infty}\limsup_{n\to\infty}
\sup_{\substack{v\in D(\mathcal E_n),\ a_n(v,v)\leq1\\
a_n(v,J_n\psi)=0\ (\psi\in S_m)}}
|\langle J_nh,v\rangle_n|^2=0.
\tag{R}
$

The supremum equals a_n(u_n-g_m,n,u_n-g_m,n). If R held, it would yield strong resolvent recovery; energy and full generator recovery follow from the resolvent identities, contraction and dense-source approximation. The source separately derives the target pure-energy liminf from E_n(r_n)>=-2<r_n,L_nF_n>-E_n(F_n), full-generator test recovery and spectral truncation of C=-L. It does not infer AR from R. Either full-domain interface is sufficient, and R is stronger than admission of these particular densities.

The source independently checks [Kuwae and Shioya (2003), official publisher PDF](https://intlpress.com/site/pub/files/_fulltext/journals/cag/2003/0011/0004/CAG-2003-0011-0004-a001.pdf), Section 2.2 at printed pp.611-613, Definition 2.11 at p.626, and Theorem 2.4(1)-(2) at pp.627-628. Their separable-Hilbert comparison requires a dense domain with asymptotic norm preservation; the native bounded local comparison cylinders meet that framework. The theorem equates Mosco convergence of densely defined closed nonnegative forms with strong resolvent convergence at one negative parameter. The paper's nonnegative operators are C_n=-L_n, C=-L, and its resolvent at zeta=-1 is the negative of (1-L_n)^-1. The frozen-mark sector remains represented in the dense scalar comparison core. No flat mobility, compact state space or uniform-normalizer hypothesis is imported.

That theorem does not establish native R or AR. Fixed-m matrix convergence and form density do not exchange the displayed m,n limits. The supremum retains arbitrary complete finite-mark dependence. The source's direct conditional-density proof also stands independently of invoking the abstract theorem. Localized fixed-cylinder calculations alone cannot close the full-domain gap.

## External provenance and exact published handoff

Only the existing final run agent_run_949d3fcc59e0412d9bcf88679d2fe322 was recovered through the helper's explicit status argument, selecting its GET branch. It completed with schema_satisfied at 2026-10-10T01:51:23.116Z, total $2.0044 ($1.9984 compute and $.006 search). Its creation receipt records 2026-10-10T01:46:28.277Z; the terminal response's createdAt is 2026-10-10T01:46:28.316Z. Both originals remain. UTC October 10 timestamps retain October 9 local research dating. No new request is made by recovery or this ingest.

The eight transmitted source files and original Code269 merge e8449c3b129142a6b357e4148ac144f1bbf31e9d / Vault189 merge 43e7a68e75985c9adf25cf09f9cda557c16b3e8e pins are preserved. The round-two source-read packet separately retains Code268 12c7493d658f98e9fccd5077850c9ad61a780837 and Vault189. The final consulted Vault190 context is 944e4aa6d1059600762799848eaffba088f15981, with staged-hierarchy theme 135180 bytes, SHA256 cf6be543766a80b0138171a63989d02827962433b78112ddff2995ec1943d878. None of these older transmission/read pins is repinned to the later publication.

The official PDF and exact printed-page extracts remain in the thirteen-file ignored Code provenance folder. Failed web fetches and failed optional extraction imports are distinguished from the successful official download and TeX Live pdftotext extraction. The candidate is preserved as provenance, while the final source reconstructs the conditional argument and checks the primary locator.

| Published or preserved item | Bytes | SHA256 |
|---|---:|---|
| R5-BOUNDARY-COVARIANCE-ATTEMPT.md | 12130 | 891740efde817095320acf7cf3b2088468ade57b5768979340e9af9ea682c195 |
| R5-MINIMAL-MOSCO-ATTEMPT.md | 20182 | b8f5fa35e108d7d9f07ff51015b45464d4fe7f2c298c0e6201cbb215d4013d5c |
| evidence/r5-minimal-domain-final-source-intake-20261009.json | 26208 | d73f5ab56d83858b6d81c44e0b15c513bfe02bf46f86b1d4967c3a1ff12804b0 |
| artifacts/r5-minimal-domain-final-handoff-20261009.json | 648694 | 294918c2b9546ef2a593e3294f44e4b7abfc0d4097d09462d426f3360d4c4237 |
| primary-source-check.md | 4220 | 301b6deed200e919a8bdfab26961e1e8d2d23f0a010c5bc4b1d0a8679b7c96d0 |
| kuwae-shioya-2003.pdf | 564067 | baaeb2e2259199d581df85c7d7264e0f7f9d5d9193070482e0e03faa9d442fe2 |

The final Code intake has 101 repository bindings, five live theory bindings and the separately dated consulted-theme context. All 101 repository bindings and the intake/handoff bytes are exact in the implementation and canonical Code checkouts; all five live bindings match the read-only vault. The completed handoff records seven checkpoint paths, twenty historical receipts preserved, non-WIP tracked parity, seven tracked and twenty-one untracked WIP entries preserved, and seventeen new ignored files aligned before fast-forward. Before vault mutation, actual canonical Code main, HEAD and origin/main agree at 4c44d2bad3d6f9db0c67fd79be1609309065639d.

## Pause point, open obligations and relevance to this research

This develops [[Staged hierarchy formation and RG composability]] without reopening [[multiagentelbo-2026-10-09-local-budget]]'s completed uninformative scalar route. The smallest missing gradient statement is AR at least on a graph-dense subset of the full closed adjoint; native R is a separately sufficient full-generator interface inside the same final route. CP and the weighted susceptibility estimate remain open alternatives from the earlier rounds. No same-model counterexample to actual minimal admission is established. Minimal liminf, actual conditional-density admission, whole-past-law identification, compatible growing identified laws, nonstationary native evolution, useful hierarchy output and persistent formation remain open. The four RG gates and roughly 65% planning estimate are unchanged.

The published Code status, standing open-question entry and existing latent-link plan now carry the next-session checkpoint. The next registered operation is the unrun R1 144-case CUDA calibration grid at target time one, under R1-CUDA-CALIBRATION-EXECUTION.md, with destination artifacts/gaussian-independent-flow-calibration/r1-independent-flow-calibration-candidate-20261008 still absent in both Code checkouts. Its nine completed prerequisite CPU/CUDA arms and two saved-only readers are retained without replay. The GPU is occupied; that next operation waits for renewed availability. The user's requested break begins after the present publication and canonical synchronization.

Only this new immutable source, the existing theme, root index and append-only log change in this ingest. All 34 prior October 9 notes, sixteen prior postflight receipts, nine unique live source files, unowned tracked files and the protected weekly-report WIP remain byte-identical. The prior theme synthesis remains alongside this later endpoint, and the previous log remains an unchanged prefix. No scientific field/proposal/scalar execution, test, GPU workload, additional external request, model/configuration/default/host/Lean change or manuscript edit occurs. The vault is a continuity record of the published conditional results and remaining obligations, not a closure certificate.
