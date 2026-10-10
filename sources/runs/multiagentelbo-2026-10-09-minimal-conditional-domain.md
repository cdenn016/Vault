---
type: run
title: "Conditional minimal Fisher-domain admission through boundary covariance"
aliases: ["R5 finite conditional projection admission", "Minimal recognition-domain conditional criterion"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Conditional minimal Fisher-domain admission through boundary covariance

Codex (2026). *Conditional minimal Fisher-domain admission through boundary covariance*. [Code PR269](https://github.com/cdenn016/MultiAgentELBO/pull/269), source 723bd92a6e6f51cb5e72d01f7981d3eee45d20a4 and merge e8449c3b129142a6b357e4148ac144f1bbf31e9d, publishes [R5-MINIMAL-CONDITIONAL-DOMAIN.md](https://github.com/cdenn016/MultiAgentELBO/blob/e8449c3b129142a6b357e4148ac144f1bbf31e9d/docs/research/2026-10-03-latent-link-rg-plan/R5-MINIMAL-CONDITIONAL-DOMAIN.md). The source derives admission of each localized finite conditional projection to the original minimal Fisher form and an exact covariance formula for its derivative. A sufficient bound CP on the native interaction covariance along an exhaustion would admit the actual whole-past conditional density with the original sharp energy bound. CP remains unproved. This is a conditional domain result, with no full-past-law identification or RG-gate closure; all four gates remain open at roughly 65%.

```bibtex
@misc{codex2026minimalconditionaldomain,
  author = {Codex},
  title = {Conditional minimal Fisher-domain admission through boundary covariance},
  year = {2026},
  howpublished = {MultiAgentELBO research checkpoint PR269},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/269}
}
@misc{tolle2012weighted,
  author = {Jonas M. T{\"o}lle},
  title = {Uniqueness of weighted Sobolev spaces with weakly differentiable weights},
  year = {2012},
  eprint = {1110.2888},
  archivePrefix = {arXiv},
  note = {Version 2, August 21, 2012},
  url = {https://arxiv.org/html/1110.2888}
}
```

## Original recognition process and exact target

The setting stays at fixed c_* on a countable lattice. P is the recorded marked interior DLR snapshot law on (w,x): w retains the entire frozen core/observation field with zero energy, while x contains full Gaussian recognition blocks and supported source rows. Gaussian blocks retain the full mean/covariance or equivalent mean/precision Fisher metric. Source rows retain ordinary simplex Lebesgue reference and the original categorical Fisher mobility, represented in independent affine coordinates by the positive restriction of diag(beta)-beta beta^T. The original supported source-prior floor, positive baseline/noise spectra, admissible compact core marks, action first moments and empirical observation second moment remain in force.

For 0<T<1/d_max, the chosen V=D(E_min) is the closure of the original unital cylinder algebra, equivalently its recorded enlarged form core C_+. Its energy is E_min(f)=T integral sum_i D_i f^T A_i D_i f dP with A_i=g_i^-1. A_i depends only on its own recognition block; on each compact interior block set A_i and its inverse are bounded and uniformly positive. Original sender and receiver records, loop forces and adjacent-episode kinetic dependencies remain. No replacement mobility, source-face extension, global drift/inverse-mobility moment, uniform conditional normalizer, mixing or curvature bound is introduced.

Q denotes an actual stationary reversible continuous interior-path subsequential limit of exact finite-volume native recognition processes with one-time law P. This is the continuous exact-population Fisher law. The fitted nonstationary finite-q proposal and the separate latent Gibbs history are not this process. For bounded real A measurable with respect to the past through s, I=[s,s+H] and r_t=E_Q[A|X_t], the target is finite time-step sums of enlarged cylinders converging to r in integrated L2(P) plus the original Fisher gradient norm (source Eq.2). The target concerns these actual conditional densities in the chosen minimal form; the existing maximal weak-energy estimate alone does not admit them to V.

## Compact localization and finite-dimensional source matching

The prior weak-energy result gives |r_t|<=||A||_infinity and integrated E_max(r_t)<=E_Q[A^2]/2. Original minimal-domain capacity cutoffs H_k, with H_k=1 outside coordinate-dependent product compacts K_k and vanishing E1 norms, give u_k=r_t(1-H_k) converging to r in L2(I;D(E_max)). Each u_k is bounded and zero outside K_k, but can depend on infinitely many recognition coordinates. This does not imply a uniform-volume compact containment result or make u_k a cylinder.

For a finite recognition block set B, G_B=sigma(w,x_B) retains all frozen marks and Pi_B is conditional expectation under P. Localized own-block integration by parts supplies the conditional marginal rho_B^w with positive density almost everywhere, weak derivative D_i rho=rho Pi_B ell_i and locally square-integrable conditional score. Here ell_i is the original local volume score minus T^-1 D_i V_i. The own-block conditional normalizer has no active derivative. The calculation uses own-compact drift/score integrability and supplied moments rather than differentiation of an uncontrolled exterior marginal integral. It yields square-root rho in local ordinary W^{1,2}; no reciprocal-weight or uniform density lower bound is supplied.

The independent primary-source read matches [Jonas M. Tölle, arXiv:1110.2888v2](https://arxiv.org/html/1110.2888), Section 1 condition (Diff), weighted integration-by-parts definition **(1.4)** and Theorem 1.1 at p=2. The candidate had incorrectly called that definition (1.3); the published derivation corrects the locator. The theorem supplies compact smooth approximation in the finite-dimensional weighted integration-by-parts space. Corollary 1.2 adds a reciprocal-weight condition (Reg), which is not used here.

On a fixed finite interior compact, the auxiliary scalar weight [theta sqrt(rho)+(1-theta)]^2 satisfies (Diff), equals rho near the target support and permits smooth approximation followed by a second compact cutoff. Bounded equivalence of the exact Fisher and Euclidean gradient norms on that fixed compact transfers the approximation to the original conditional Fisher form. The auxiliary weight is only a finite-dimensional approximation device. It changes no global native measure, model, source reference, mobility or boundary condition, and provides no estimate uniform in growing B or infinite-product domain equality.

## Exact projection derivative and minimal-form admission

Set v_k,B=Pi_B u_k and choose an own-block smooth chi_k,i equal to one near K_k,i. The source's Eq.11 is

$$
J_{i,k}^B=\Pi_B(u_k\chi_{k,i}b_i)-v_{k,B}\Pi_B(\chi_{k,i}b_i),
\qquad
D_i v_{k,B}=\Pi_B(D_i u_k)+T^{-1}A_i^{-1}J_{i,k}^B.
$$

The drift identity b_i=T div A_i+T A_i ell_i and own-block measurability make this correction the exact original drift covariance. On the localized support, Eq.14 reduces it to J=-A_i Cov_P(u_k,D_i V_i|G_B). Own-block volume, mobility-divergence, baseline and entropy gradients cancel. Only original interaction forces whose dependencies cross the boundary can survive. The actual boundary retains every sender, receiver, primitive record, loop and temporal dependency; this introduces no expectation-force dynamics. J vanishes for a retained block whose complete dependency neighborhood is inside B, and outside the projected compact support.

For each fixed k and finite B, conditional Cauchy-Schwarz, bounded u_k and localized drift-square integrability make the sum of J^T A_i^-1 J finite. Its constants can depend on the coordinate and compact. Finite energy at every B does not itself bound the sequence as B grows.

The finite-dimensional theorem admits v_k,B to L2(I;V) after an explicit cylinder reduction. For almost every (t,w), choose the first successful smooth test from a countable uniform-C1 library, truncate to finitely many selections and approximate the bounded selection coefficients by finite time-step, finite-mark continuous cylinders. Their mark coefficients carry zero recognition derivatives. Smooth finite-recognition tests are then approximated by finite sums of own-block factors with interior cutoffs. These are in the original tensor cylinder algebra and converge in its native form norm. Retaining all frozen marks in Pi_B alone would not make a projection a cylinder; this measurable finite-mark reduction is part of the argument. The finite projection's minimal gradient is exactly the displayed Eq.11. No generator graph-core density or alternate source-face extension is asserted.

## Unproved CP and its conditional consequence

Own-mobility conditional Jensen and the derivative formula give the source's Eq.15:

$$
\int_I\mathcal E_{\min}(v_{k,B})dt
\leq2\int_I\mathcal E_{\max}(u_k)dt
+\frac{2}{T}\int_I\int\sum_{i\in\partial B}
(J_{i,k}^B)^T A_i^{-1}J_{i,k}^B dPdt.
$$

CP (Eq.16) requires, for each k and the actual fixed A,I, a nested finite exhaustion B_n increasing to the whole recognition index set such that

$$
\sup_n\int_I\int\sum_{i\in\partial B_n}
(J_{i,k}^{B_n})^T A_i^{-1}J_{i,k}^{B_n}dPdt
=C_{k,A,I}<\infty.
$$

This is a sufficient condition, not a proved consequence or a necessary criterion. The exhaustion and finite constant may depend on k,A,I. The boundary sum need not vanish, C_k need not approach zero, and no bound uniform in k is required. It is the actual primitive/record/temporal dependency boundary, rather than an aggregate record count.

Assuming CP for every k for this A,I, Eq.15 bounds finite projections in L2(I;V). Conditional expectations converge strongly in L2 to u_k along the exhaustion with all marks retained. Hilbert weak compactness therefore admits u_k to the same minimal form; finite convex averages followed by the established finite-projection cylinder reduction give strong form approximants. Because admitted minimal gradients equal their maximal gradients, the existing cutoff convergence then makes u_k Cauchy in L2(I;V) and admits r. The source retains the sharp original estimate (Eq.17),

$$
r\in L^2(I;V),\qquad
\int_I\mathcal E_{\min}(r_t)dt
=\int_I\mathcal E_{\max}(r_t)dt
\leq\tfrac12 E_Q[A^2].
$$

A diagonal choice of finite time-step enlarged cylinders gives exactly the original target Eq.2. The larger constants in Eq.15 prove admission only and do not replace this sharp bound. CP on a bounded continuous finite-past cylinder class dense in the recorded bounded L2(Q) approximation would suffice to extend admission to every bounded whole-past event by the energy estimate for differences and closedness. Full-past-law identification would then follow through the earlier enlarged-source implication. Neither CP nor that identification is established at this checkpoint.

## Precise open obligation and research scope

The decisive open task is a native boundary-interaction covariance estimate along an exhaustion for localized actual conditional densities, or a sufficient dense finite-past class. Coordinate-dependent compact radii, source-face distances and inverse-mobility/score costs prevent fixed-B finiteness from yielding CP. First action moments, Euclidean source-drift squares, boundary cardinality, conservativity, a capacity nest or the maximal weak-energy estimate alone do not establish the needed weighted sum. No uniform native estimate has been evaluated or proved.

The earlier logarithmic source-face witness refutes the attempted generator graph-core shortcut but has infinite form energy; it is not a counterexample to the present bounded actual-density target. Minimal-form Mosco liminf, full-past path-law identification, compatible growing identified laws, nonstationary native evolution, useful hierarchy output and persistent formation remain open. [[multiagentelbo-2026-10-09-local-budget]] retains its separate uninformative sufficient coding-bound outcome; this domain construction does not reopen that bounded scalar route. All four RG gates remain OPEN and the roughly 65% planning estimate is unchanged. No D_max substitution, new source boundary, source floor, frozen mark, Fisher mobility, model or scientific execution is introduced.

## One external candidate and dated provenance

The completed source records exactly one Exa Agent Ultra request, agent_run_bcc9a660b4e34bd5b45dfd3fc1ca1e34. It completed with schema_satisfied after six searches at total cost $2.3553 ($2.3253 compute plus $.03 search), under the original $10/600-second cap. Six bounded transmitted sources were preserved byte-identically. The candidate supplies provenance and a theorem locator; the independent official primary-source read supplies the corrected finite-dimensional source match. Candidate output does not close CP or any gate. This ingest issues no additional external request.

The external request remains bound to Code266 merge 973aca6e9bb2f8182e89e7a51be6d258efe6925b and Vault188 merge 94f2a0c48c527889bdc6f73b7d88a09a40f0c38a. The final Code269 intake separately consults Vault189 merge 43e7a68e75985c9adf25cf09f9cda557c16b3e8e, whose staged-hierarchy theme is 133,982 bytes with SHA256 adf4bd3afd2e05b59f2ba17e9759dbbd6e09266ba77ac37a3afd43676fff4efd. The older transmitted context is not repinned to the later consulted context. UTC October 10 request/source-read times correspond to October 9 local research dating.

## Published bindings and canonical continuity

| Published item | Bytes | SHA256 |
|---|---:|---|
| R5-MINIMAL-CONDITIONAL-DOMAIN.md | 25802 | d0721398f8ea32aa1630ca0d7fe74e9f5136276b63401b993d21318f80358699 |
| evidence/r5-minimal-conditional-source-intake-20261009.json | 24890 | 3ea90836ffa57a34418fae227fbbc37cfd4a6306917d45ff37e56442768b7908 |
| R5-CONDITIONAL-DENSITY-WEAK-ENERGY.md | 16549 | 04e0662328a86416ef444a4aa8227de2b8a881f7094262bbb4c4f89ba8ea9561 |
| R5-NATIVE-RECOGNITION-PROCESS.md | 32366 | a306a2f8dffaefdb707711b462b49ba7ece406a964c23c43571d2df85f97ac0e |
| primary-source-read.md | 1505 | a8bab1b05edd0613986476048a1426425b3a21e88a95e72cab0c4519461b6815 |

The intake retains 83 repository bindings, five live theory bindings and one dated consulted-theme context. All 83 bound repository paths and the new nine ignored handoff/research files have exact bytes in the implementation and canonical code copies. The completed handoff artifacts/r5-minimal-conditional-handoff-20261009.json has SHA256 c18c46db202bbbb950ad536837a3bdf6ba9e73594002cbcd6060e7014e711acb in both. Before vault mutation, actual canonical Code main, HEAD and origin/main agree at e8449c3b129142a6b357e4148ac144f1bbf31e9d. SPEC, c10/c12 and c08b/g11 remain read-only scope/process/history context and certify no claim by manuscript authority.

This develops [[Staged hierarchy formation and RG composability]] alongside [[multiagentelbo-2026-10-09-local-budget]] and [[multiagentelbo-2026-10-09-local-update-amplification]]. Only this new immutable source, the existing staged-hierarchy theme, root index and append-only log change. All 33 prior October 9 notes, fifteen prior postflight receipts, nine unique live source files and the protected weekly-report WIP are preserved. This ingest runs no field, proposal, scalar producer, scientific test or GPU workload and makes no manuscript/model/config/default/host/Lean change. The unpublished R5-BOUNDARY-COVARIANCE-ATTEMPT and future Code status regrouping are excluded.
