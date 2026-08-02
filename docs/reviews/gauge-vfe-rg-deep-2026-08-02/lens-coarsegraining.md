# Lens review — coarse-graining / Markov channels / variational

**Reviewer lens:** variational inference specialising in coarse-graining and Markov channels.
**Chapters read in full:** `06_general_coarsegraining.tex`, `09_coarsegraining.tex`.
**Supporting reads:** `05_elbo.tex` (1–240), `07_restrictions.tex` (140–328), `07b_agent_network_rg.tex` (1–130),
`appendix_claim_ledger.tex`, `main.tex`, `verification/claims.json`.
**Out of scope (per `00-settled-ground.md`):** RG-1, RG-2, LG-1/2, PB-1..4, FINAL-01..08, R01..R21, and every
obligation the manuscript's own ledger declares OPEN or CONJECTURE.

**Method.** Every load-bearing identity in both chapters was recomputed by hand and then re-verified numerically
in `C:/Python314/python.exe` (numpy 2.4.4 / scipy 1.17.1). Scripts:

- `<scratch>/cg_verify.py` — 100 checks
- `<scratch>/cg_verify2.py` — corrected DPI-equality construction, adversarial probes
- `<scratch>/cg_verify3.py` — sub-Markov witness, quotient-volume normalizer chain
- `<scratch>/labelcheck.py` — cross-reference resolution

(`<scratch>` = `C:\Users\CHRISA~1\AppData\Local\Temp\claude\C--Users-chris-and-christine-Desktop-Research\21b92b09-6f32-47fa-8f90-6f5faa59e5a3\scratchpad`)

**Headline.** I found **no wrong mathematics** in either chapter. Every exactness claim I could test survived
every counterexample I could construct; residuals are at machine precision (worst genuine residual `1.1e-14`,
median `~1e-16`). All 54 `\Cref`/`\eqref` targets in the two chapters resolve, and there are no duplicate labels.
The defects are **definitional and attributional**: one load-bearing symbol in the conclusion of an `ESTABLISHED`
theorem is never defined anywhere in the manuscript, three more symbols in Chapter 9 are used without definition
or cross-reference, one is used ten lines before its definition, and two theorems carry hypotheses that are not
the ones doing the work.

---

## Adjudication of the carried-over candidate finding #1

> `\mathcal L^{\rm ext}` undefined — `06_general_coarsegraining.tex:209,213`.

**Confirmed, at MEDIUM not critical.** Details in CG-1. The inequality `eq:cg-elbo-monotone` is **correct**
regardless of the naming, under either of the two plausible readings of "extended", both verified numerically.

---

# Findings

## CG-1 — `\mathcal L^{\rm ext}` / `\bar{\mathcal L}^{\rm ext}` is never defined in the manuscript

**Claim.** "the extended ELBOs satisfy `eq:cg-elbo-monotone`".
**Location.** `06_general_coarsegraining.tex:207` (prose), `:209`, `:213` (inside `eq:cg-elbo-monotone`,
the conclusion of `thm:cg-evidence-preserving-channel`, `:197`).
**Severity.** medium.
**Status tag.** `\status{ESTABLISHED}` (`06:216`). Prose does **not** inflate the claim — if anything it
under-claims, since `07b:34–57` proves the sharper exact chain rule. The defect is that the tagged theorem's
conclusion is written in a symbol that has no definition.

**Evidence.**

1. Whole-directory search: the glyph occurs exactly twice.
   ```
   ./06_general_coarsegraining.tex:209:\bar{\mathcal L}^{\rm ext}(\bar Q_o;o)
   ./06_general_coarsegraining.tex:213:=\mathcal L^{\rm ext}(Q_o;o).
   ```
   `grep -rn "rm ext"`, `grep -rn "mathrm{ext}"`, `grep -rn "\^{ext}"` over all `*.tex` return nothing else.
   The strings "extended ELBO", "extended free", "extended variational" occur only at `06:207`.
   `SPEC.md` does not contain it. `appendix_notation.tex` contains no ELBO entry at all.
   `main.tex:35` defines only `\newcommand{\Lelbo}{\mathcal L}`; the `^{\rm ext}` superscript is the entire
   semantic content and is unglossed.

2. It is **not** a missing cross-reference to a definition elsewhere under another glyph. The manuscript's
   defined ELBO is `\Lelbo(Q_X;X)=\E_{Q_X}[\log p_\theta(o,Y\given X)-\log q_X(Y\given o)]`
   (`05_elbo.tex:121–128`, `eq:elbo-definition`), a **density-based** object requiring the reference measure
   `\nu_D^Y` and hypotheses (H1)–(H4). No superscripted variant exists. The nearest neighbour in `05_elbo.tex`
   is `\widetilde{\Lelbo}` (`:54`, `eq:elbo-pseudo-elbo`), which is a **different** object — the *pseudo-ELBO*,
   larger than `\Lelbo` by the total correlation and **explicitly not a lower bound** (`05_elbo.tex:66`,
   `:76`). A reader meeting an undefined decorated `\mathcal L` twelve pages later is one glyph away from the
   one object the manuscript went out of its way to warn against.

3. **The same statement is written twice more, with different symbols each time.**
   - `07_restrictions.tex:302–305` states it verbatim with the *defined* symbols
     `\bar{\mathcal L}(\bar Q;o)` and `\mathcal L(Q;o)` — no `\rm ext`.
   - `07b_agent_network_rg.tex:34–57` (`thm:rg-exact-coarse-vfe`) states the sharper version with
     `\Fenergy_P(Q_o)` / `\Fenergy_{P^c}(Q_o^c)` and the in-prose gloss "Let the fine and coarse VFE
     expressions be defined as **extended-real sums**, with the common finite evidence term separated from
     their KL gaps" (`07b:35–36`).
   That gloss is almost certainly what `^{\rm ext}` means, and it is the only place it is said. Chapter 6 also
   uses "extended-real" in this sense at `06:464` ("the extended-real forward-KL score").

4. **The inequality is correct as an inequality, under both readings.** Verified numerically
   (`cg_verify2.py` block D1), joint on `O={o_1,o_2,o_3} × X={1..4}`, explicit row-stochastic
   `K: X → Y={a,b,c}`:
   ```
   reading 1 (extended-real ELBO)  log p(o) - KL(Q_o || P_o)          = -1.597517911652527
   reading 2 (ELBO on X x Y)       log p(o) - KL(Q_o(x)K || P_o(x)K)  = -1.597517911652527
                                   RESIDUAL                            = 2.220e-16
   coarse                          log p(o) - KL(Q_oK || P_oK)        = -1.162496432606812
   rise = 0.4350214790 >= 0 ;  both <= log p(o) = -1.1416272501
   ```
   The two readings agree because attaching a common channel preserves relative entropy. Supporting exact
   checks (`cg_verify.py` Part B): `|\bar P^O - P^O|_\infty = 0.000e+00`; `|\bar P_o - P_oK|_\infty =
   0.000e+00`; coarse density-form ELBO vs `\log p(o)-\KL` residual `0.000e+00`; `07b`'s chain rule
   `\KL(Q\Vert P_o) = \KL(QK\Vert P_oK) + \E_z\KL(\widehat Q(\cdot|z)\Vert\widehat\Pi(\cdot|z))` residual
   `0.000e+00`.

5. **Counterexample attempts, all failed** (i.e. the theorem is robust): 2×10⁵ Dirichlet-random
   recognition laws with adversarially re-drawn channels — max violation of `\bar{\mathcal L} \ge \mathcal L`
   was `0.000e+00`, max violation of `\bar{\mathcal L} \le \log p(o)` was `0.000e+00`.

**Fix.** Add one display in `06`, immediately before `thm:cg-evidence-preserving-channel`:
```
\mathcal L^{\rm ext}(Q;o) := \log p(o) - \KL(Q\Vert P_o) \in [-\infty,\ \log p(o)],
```
with one sentence: "this is the extended-real form of `\eqref{eq:elbo-definition}`; the two agree whenever
a reference measure on `\mathsf Y` and hypothesis (H4) are declared at that scale, and the extended form
requires neither." Then either reuse the symbol in `07_restrictions.tex:302–305` or drop it there too, so the
same statement is not written with three different symbols in three chapters.

**Secondary point, same fix.** Under the *density* reading the theorem is missing hypotheses. `eq:elbo-definition`
needs a declared reference measure `\bar\nu` on `\mathsf Y` under which `\bar P(o,\cdot)` and `\bar Q_o` have
densities, plus coarse (H4). `thm:cg-evidence-preserving-channel` declares neither, and the pushforward `\nu K`
of a σ-finite reference need not be σ-finite or dominating. This is exactly the standard the chapter itself
imposes on the *other* two operations — `06:239–246` ("defines a new model only after `\bar\nu` and a finite
`\bar Z` are declared") and `06:331–338` ("Its reference measure, normalizer, and any gauge action must be
propagated separately"). The extended-real definition removes the gap entirely, because `\log p(o)-\KL` is
reference-measure-free. That is the reason to adopt it explicitly rather than leave it implied.

**Falsifies.** Nothing. It falsifies only the *presentation* of `thm:cg-evidence-preserving-channel`; the
theorem's content stands and is independently re-proved with defined symbols at `07_restrictions.tex:302–305`
and strengthened at `07b:34–57`.

---

## CG-2 — `B`, `B_\perp` are used in Chapter 9 without definition or cross-reference, and `\mathcal G_{\rm tie}` is used ten lines before it is defined

**Claim.** `eq:cg-epsilon-divergence` and `eq:cg-mean-tie-cost`.
**Location.** `09_coarsegraining.tex:849–855` (`eq:cg-epsilon-divergence`, uses `B_\perp` and
`\mathcal G_{\rm tie}`), `:858–867` (`eq:cg-mean-tie-cost`, first definition of `\mathcal G_{\rm tie}`),
`:873–877` (proof, uses `\nu=Ba` and "the orthogonal basis `[B,B_\perp]`"), `:883–892` (`eq:cg-loewner`,
equality condition `B^\top\Lambda B_\perp=0`).
**Severity.** medium.
**Status tag.** `\status{ESTABLISHED}` at `:854`, `:867`, `:892`. Prose does not inflate; the results are
exactly true. The defect is that the statements are unreadable from within the chapter.

**Evidence.**

1. `B` and `B_\perp` appear nowhere else in `09_coarsegraining.tex` (grep: the only other `B`-like tokens are
   `B_\perp` inside these four equations). They are defined only in `07_restrictions.tex:159`:
   "Let `[B\ B_\perp]` be an orthogonal matrix with `B\in\R^{n\times r}`" — and Chapter 9 does not cite that
   proposition, this section, or that chapter at this point.
2. `\mathcal G_{\rm tie}` first *appears* at `:852` inside `eq:cg-epsilon-divergence` and is first *defined* at
   `:862`. Definition used before it is given — explicitly in scope per the settled-ground contract.
3. The identification `\operatorname{range}(B)=\operatorname{range}(S)` is never stated, yet it is what makes
   `r=NK-mK` at `:854` correct (`\dim\operatorname{range}(S)=mK` by `eq:cg-aggregation-matrix`).
4. `r` collides across chapters with opposite meaning: `07_restrictions.tex:159` has `r` = **retained**
   dimension (`B\in\R^{n\times r}`); `09:854` has `r=NK-mK` = **transverse** dimension. Both are internally
   consistent, jointly confusing.
5. **The mathematics is exact.** `cg_verify.py` Part I, `d=7`, `r_{\rm ret}=3`, random SPD `\Lambda`:
   - `eq:cg-mean-tie-cost` vs brute-force constrained minimisation: residual `1.421e-14`
     (`G_tie = 46.1694164536`); 2×10⁴ random `\nu\in\operatorname{range}(B)` never beat it (best `46.488323`).
   - `eq:cg-loewner`: `\lambda_{\min}(B_\perp^\top\Lambda B_\perp - (B_\perp^\top\Lambda^{-1}B_\perp)^{-1}) \ge 0`,
     residual `0.000e+00`; equality under `\Lambda`-orthogonality, residual `5.329e-15`.
   - `eq:cg-epsilon-divergence` (`cg_verify2.py` block C1): the absolute residual is **exactly** linear in `\varepsilon`,
     ```
     eps=1e-02  abs resid = 2.946e-01   resid/eps = 29.464395
     eps=1e-03  abs resid = 2.946e-02   resid/eps = 29.464395
     eps=1e-04  abs resid = 2.946e-03   resid/eps = 29.464395
     eps=1e-05  abs resid = 2.946e-04   resid/eps = 29.464395
     eps=1e-06  abs resid = 2.946e-05   resid/eps = 29.464395
     ```
     and the coefficient is precisely `\tfrac12\Tr(B_\perp^\top\Lambda B_\perp) = 29.46439473`.
     I also tested the **stronger** family where cross-covariance blocks between retained and transverse
     directions are left free (only `B_\perp^\top\Sigma B_\perp=\varepsilon I` imposed): the optimum drives them
     to `O(\sqrt\varepsilon)` and the residual stays `O(\varepsilon)` with coefficient
     `\tfrac12[\Tr\Lambda_{22}-\Tr(\Lambda_{12}^\top\Lambda_{11}^{-1}\Lambda_{12})]=24.96194107`. So the stated
     `+O(\varepsilon)` is correct and is not an artefact of a narrower family than the prose suggests.
   - `eq:cg-factorization-gap` vs brute-force block-diagonal optimum: residual `1.776e-15`
     (`G_fact = 0.3544776657`); decreases under merging (`0.354478 → 0.250684`), consistent with Fischer.

**Fix.** In `09`, immediately before `eq:cg-epsilon-divergence`: "let `[B\ B_\perp]` be orthogonal with
`\operatorname{range}(B)=\operatorname{range}(S)`, so `B\in\R^{NK\times mK}` and `r:=NK-mK` is the transverse
dimension, as in `\Cref{prop:restrict-mean-cost}`"; move `eq:cg-mean-tie-cost` ahead of
`eq:cg-epsilon-divergence`; and add the `\Cref{prop:restrict-mean-cost}` / `\Cref{thm:restrict-determinant-gap}`
citations, since `\mathcal G_{\rm tie}` and `\mathcal G_{\rm fact}` are `eq:restrict-mean-cost` and
`eq:restrict-combined-cost`'s first term with `J\to\Lambda`.

**Falsifies.** Nothing mathematical.

---

## CG-3 — `G`, `Q`, and `\operatorname{pdet}` in `eq:cg-quotient-generalized-determinant` are undefined; `Q` collides with the recognition law

**Claim.** `\det(G^{-1}Q)=\operatorname{pdet}\Lambda_{\rm c}/(\operatorname{pdet}H)^K
=\operatorname{pdet}\Lambda_{\rm c}/J_{\mathcal P}^2`.
**Location.** `09_coarsegraining.tex:826–833` (`eq:cg-quotient-generalized-determinant`).
**Severity.** medium-low.
**Status tag.** `\status{ESTABLISHED}` at `:836`. Correct; unreadable.

**Evidence.**

1. `G` occurs exactly once in the chapter, at `:828`. `Q` in this sense occurs exactly once, at `:828` — and
   `Q` is the recognition law throughout the rest of the manuscript (`05_elbo.tex`, `06:200`, `07_restrictions`).
   Neither is defined. `\operatorname{pdet}` is used at `:797`, `:829`, `:830` and defined nowhere in the
   manuscript (`grep -rn pdet` returns only those three lines and `appendix_notation.tex` has no entry).
2. The intended reading is `G=H\otimes I_K`, `Q=\Lambda_{\rm c}`, `\operatorname{pdet}` = product of nonzero
   eigenvalues. Under that reading the identity is exact. Verified (`cg_verify3.py` block G1), `N=5`, `K=2`,
   partition `{0,1,2},{3,4}`, `A_i=0` so `\ker\Lambda=\mathbf 1\otimes\R^K`:
   ```
   dim ker Lambda   = 2  (= K)
   dim ker Lambda_c = 2  (= K);  ker Lambda_c == 1_m (x) R^K  residual = 2.220e-16
   pdet H = 2.4000000000 = m*prod(s_i)/n ;  J_P = 2.4000000000
   det(G^-1 Q) via pdets = 116.4804464003 ;  pdet(Lambda_c)/J_P^2 = 116.4804464003 ;  resid = 0.000e+00
   Z_std = 0.2425728068 ;  Z_ind = J_P Z_std = 0.5821747364 ;
   (2pi)^(d/2) det(G^-1 Q)^(-1/2) = 0.5821747364 ;  resid = 0.000e+00
   log J_P = 0.8754687374
   ```
   The whole normalizer chain of `sec:cg-quotient-volume` is therefore exact, including the flagged
   partition-dependent offset `\log J_{\mathcal P}` at `:837–839`, and including `eq:cg-quotient-metric`
   (`\operatorname{pdet}H = m\prod s_i/n`, residual `3.553e-15`; principal cofactor `\prod s_i/n`, residual
   `8.882e-16`; `\min_a\|Px+a\mathbf 1\|^2 = x^\top Hx`, residual `2.075e-11` on a grid).
   `eq:cg-partial-properness` also verified: singular `\Lambda_{\rm c}` when
   `\operatorname{range}(S)\cap\ker\Lambda\neq\{0\}` (`\lambda_{\min}=-1.065e-15`), and
   `\Lambda_{\rm c}\succ0` (`\lambda_{\min}=1.247036`) after adding anchors.
3. Aggravating context: within the *same section* `P` has been redefined at `:790` as the `\{0,1\}` assignment
   matrix `\widehat S`, and `H` at `:795` as the quotient metric — while `H` is the congruence chart of
   `\mathcal C_H` at `:126` and a holonomy element at `:776`. So `\det(G^{-1}Q)` sits three lines below a
   redefined `P` and a third `H`.

**Fix.** One clause: "write `G=H\otimes I_K` for the induced quotient metric and `Q=\Lambda_{\rm c}` for the
coarse form, and `\operatorname{pdet}` for the product of the nonzero eigenvalues", then one sentence stating
what `\det(G^{-1}Q)` is for — namely `Z_{\rm ind}=(2\pi)^{(m-1)K/2}\det(G^{-1}Q)^{-1/2}`, which is the only
reason the quantity appears. Rename `Q` (e.g. `\Lambda_{\rm c}` directly) to avoid the recognition-law clash.

**Falsifies.** Nothing.

---

## CG-4 — `thm:cg-evidence-preserving-channel` lists "does not read `Q_o`" as the hypothesis, but the hypothesis the display needs is normalization

**Claim.** "Fix ... and normalized channel `K:\mathsf X\rightsquigarrow\mathsf Y` **that does not read `Q_o`**."
**Location.** `06_general_coarsegraining.tex:197–222`.
**Severity.** low.
**Status tag.** `\status{ESTABLISHED}`. Correct as stated; the hypothesis attribution is imprecise, in a
chapter that is otherwise scrupulous about exactly this (`06:58`: "Parameter independence is load bearing").

**Evidence.**

1. `Q_o`-independence is **not used** anywhere in the proof of the display, and cannot be: a `Q`-dependent
   `K_Q` still satisfies `K_Q(x,\mathsf Y)=1`, hence still gives `\bar P^O=P^O`, `\bar P_o=P_oK_Q`, and DPI at
   that `Q`. Verified over 2×10⁵ adversarially `Q`-dependent Dirichlet channels (`cg_verify2.py` D2):
   ```
   max violation of  Lbar >= L        : 0.000e+00
   max violation of  Lbar <= log p(o) : 0.000e+00
   ```
2. **Normalization is what carries the display**, and dropping it reverses the ordering. Sub-Markov
   `K\to cK` (`cg_verify3.py` F1), same joint:
   ```
   c=1.00  log barp(o)=-1.141627  coarse L=-1.162496  fine L=-1.597518  ordering HOLDS
   c=0.50  log barp(o)=-1.834774  coarse L=-1.855644  fine L=-1.597518  ordering FAILS
   c=0.20  log barp(o)=-2.751065  coarse L=-2.771934  fine L=-1.597518  ordering FAILS
   c=0.05  log barp(o)=-4.137360  coarse L=-4.158229  fine L=-1.597518  ordering FAILS
   c=0.01  log barp(o)=-5.746797  coarse L=-5.767667  fine L=-1.597518  ordering FAILS
   ```
   `|\bar P^O-P^O|_\infty = 0.085269` at `c=0.25`.
3. `Q_o`-independence **is** load bearing — but for the surrounding paragraph (`06:224–228`, "ELBOs are
   comparable") and for `prop:restrict-principle`, whose proof turns on "Constancy of the evidence is load
   bearing: the generative kernel is fixed once `(\theta,X)` is fixed and does not read `Q`"
   (`05_elbo.tex:238–240`). With a `Q`-dependent channel `\bar P` is not one joint, so its supremum over `Q`
   is not a bound/gap decomposition for a single model, even though every individual inequality holds.
4. Note for completeness: `K` is permitted to read `o` without damage. Verified (`cg_verify.py`): with three
   different channels indexed by `o`, `|\bar P^O-P^O|_\infty = 0.000e+00` and the ordering still holds
   (residual `0.000e+00`). So the exclusion is specifically of the *recognition* law, not of the observation.

**Fix.** Split the hypothesis line: "`K` is normalized, `K(x,\mathsf Y)=1` — this is what preserves the
evidence and hence the display — and `K` does not read `Q_o`, which is what makes `\bar P` one fixed coarse
joint across the recognition family, as required by `\Cref{prop:restrict-principle}`."

**Falsifies.** Nothing.

---

## CG-5 — the cited DPI theorem is stated only under `\KL(P\Vert Q)<\infty`, but `eq:cg-elbo-monotone` is invoked without that hypothesis

**Claim.** Proof of `thm:cg-evidence-preserving-channel`: "Absolute continuity and `\eqref{eq:cg-elbo-monotone}`
follow from the preceding data-processing theorem."
**Location.** `06_general_coarsegraining.tex:218–222`, referring to `thm:cg-dpi-equality` (`:65–85`), whose
hypotheses are `P\ll Q` **and** `\KL(P\Vert Q)<\infty` (`:66–67`).
**Severity.** low.
**Status tag.** `\status{ESTABLISHED}` on both. The conclusion is true; the citation chain is formally short.

**Evidence.** `thm:cg-evidence-preserving-channel` assumes only `Q_o\ll P_o`, not finiteness. When
`\KL(Q_o\Vert P_o)=+\infty` the display is still true — DPI holds in `[0,+\infty]` — but that case is not
covered by the theorem as stated, whose finiteness hypothesis is genuinely needed only for the *equality
clause* `eq:cg-kl-equality` (conditional-Jensen equality with a strictly convex `\phi`). Witness
(`cg_verify2.py` A2): `P=(\tfrac12,\tfrac12,0,0)`, `Q=(0,0,\tfrac12,\tfrac12)`, `K` merging `\{1,2,3\}\to a`,
`4\to b`:
```
KL(P||Q)   = inf
KL(PK||QK) = 0.6931471806     -> inequality holds, equality clause vacuous
```
Also verified that `Q_o\ll P_o \Rightarrow Q_oK\ll P_oK` (used, correct).

**Fix.** In `thm:cg-dpi-equality`, state the inequality in `[0,+\infty]` and attach `\KL(P\Vert Q)<\infty` only
to the equality clause. One clause.

**Falsifies.** Nothing.

---

## CG-6 — "as it is under trivial represented holonomy" asserts an implication that does not hold

**Claim.** "Suppose the admissible parent family is the full nondegenerate Gaussian family, **as it is under
trivial represented holonomy**."
**Location.** `09_coarsegraining.tex:604–609`.
**Severity.** low.
**Status tag.** `\status{HYPOTHESIS}` at `:609`, so the "Suppose" carries the load. The appositive is
nonetheless a false implication.

**Evidence.** In `thm:cg-holonomy-kl-marginal` the admissible set is
`\mathscr Q_{I,\rm fix}^x(r)=\{Q\in\mathscr M_r^x:(H)_\#Q=Q\ \forall H\}` (`eq:cg-holonomy-fixed-parent`).
Trivial represented holonomy gives `\mathscr Q_{I,\rm fix}^x(r)=\mathscr M_r^x` — nothing more. The parent-law
family `\mathscr M_i^x\subseteq\mathcal P(\mathsf Z_i^x)` is a *declared, arbitrary, equivariant* input
(`06:441–448`), never fixed to be the full nondegenerate Gaussian family. So "the admissible parent family is
the full nondegenerate Gaussian family" requires an independent declaration `\mathscr M_r^x=\{\mathcal N(m,C):
C\succ0\}` that the manuscript never makes.

**Fix.** "Declare `\mathscr M_r^x` to be the full nondegenerate Gaussian family; under trivial represented
holonomy `\mathscr Q_{I,\rm fix}^x(r)` then equals it."

**Falsifies.** Nothing downstream: `prop:cg-gaussian-forward-kl-barycenter` verifies exactly
(`eq:cg-gaussian-barycenter-score` residual `1.110e-16`, `D^\star=0.4863020793`; moment matching unbeaten in
2×10⁴ perturbations, residual `0.000e+00`).

---

## CG-7 — `cor:cg-compact-holonomy-barycenter`'s compactness hypothesis excludes the generic case the chapter's own realization produces

**Claim.** "Let `\mathcal H\subset\GL(K)` be a compact represented holonomy group with normalized Haar
probability measure `\mu_{\mathcal H}`."
**Location.** `09_coarsegraining.tex:670–699`.
**Severity.** low.
**Status tag.** `\status{ESTABLISHED}`. The corollary is correct; its hypothesis is narrower than it needs to
be, and narrower than the chapter's own constructions.

**Evidence.**

1. A subgroup of `\GL(K)` that is compact *as a subset* is closed. The represented holonomy group of a finite
   graph is finitely generated by the `\Theta_e` (`09:352–360`), and a finitely generated subgroup of a compact
   group need not be closed — a single irrational rotation generates a dense, non-closed, non-compact subgroup
   of `\mathrm{SO}(2)`. So for generic `\Theta_e\in\mathrm{SO}(K)` the corollary does not apply as written,
   even though the conclusion is true.
2. The repair is one clause and is sound: `h\mapsto h_\#\mathcal N(m,C)` is continuous, so the stabiliser of a
   measure is closed, hence `\mathcal H`-invariance `\iff` `\overline{\mathcal H}`-invariance, and
   `\overline{\mathcal H}` is compact whenever `\mathcal H` is bounded.
3. The corollary's mathematics is exact. Verified (`cg_verify.py` Part J), `K=3`, four constituent Gaussians,
   `\mathcal H=\{I,-I\}`:
   ```
   C_H positive definite                                   resid = 0.000e+00
   N(a_H,C_H) is H-invariant                               resid = 0.000e+00
   eq:cg-gaussian-haar-score                               resid = 4.441e-16   (D*_H = 0.6736103634)
   minimal among H-invariant Gaussians (2e4 perturbations)  resid = 0.000e+00
   ```
   The `09:660–668` witness also verifies: `\tfrac12\log(1+\lVert u\rVert^2)`, residual `5.551e-17`. The
   `09:721–725` non-compactness remark (`2I_K` admits no invariant SPD Gaussian) is correct.

**Fix.** "Let `\mathcal H\subset\GL(K)` have compact closure `\overline{\mathcal H}`. Since
`\mathcal H`-invariance of a Gaussian is equivalent to `\overline{\mathcal H}`-invariance, apply Haar measure
on `\overline{\mathcal H}`."

**Falsifies.** Nothing.

---

## CG-8 — "Pairwise equality does not prove that stronger statement" is ambiguous, and false under the natural all-pairs reading

**Claim.** `06_general_coarsegraining.tex:129–133`.
**Severity.** low.
**Status tag.** `\status{ESTABLISHED}`. True under the one-pair reading (which is `cor:cg-pairwise-bayes-recovery`'s
setting); false under the all-pairs reading.

**Evidence.**

1. The positive statement immediately above (`:122–129`) is correct and is the standard Kullback–Leibler
   characterization of Bayes sufficiency. Verified (`cg_verify2.py` A3), three-parameter dominated experiment
   on `\{1,2,3,4\}` with the lumping `K` and `P_0=\tfrac13\sum P_\theta`:
   ```
   max_theta |KL(P_th K||P_0 K) - KL(P_th||P_0)| = 2.776e-17
   max_theta ||P_th K R_{P_0} - P_th||_inf       = 0.000e+00     -> single R recovers all
   control (one non-sufficient member): KL gap = 0.023587, ||P K R - P||_inf = 0.075000
   ```
2. If "pairwise equality" is read as "equality for **every** pair", the sentence is false: every likelihood
   ratio `dP_i/dP_j` then has a `\sigma(Y)`-measurable version, which is Halmos–Savage factorization, hence
   sufficiency, hence one common `R`. I searched 2×10⁵ random configurations (3 laws on `\{1,2,3,4\}`,
   deterministic lumpings to 2 states) for a configuration with all pairwise equalities but no common
   recovery kernel: **none found** (`cg_verify2.py` A4). Targeted hand attempts with mutually singular and
   partially singular families all fail for the same structural reason.

**Fix.** Write "Equality for a single pair does not prove that stronger statement", and optionally note that
equality against a Halmos–Savage `P_0` is exactly sufficiency.

**Falsifies.** Nothing; `cor:cg-pairwise-bayes-recovery` itself is exact — verified
(`cg_verify2.py` A1, corrected lumpable channel with disjoint `Y`-supports):
```
r = [1.2 1.2 0.8 0.8]  (constant on the two K-fibres)
KL(P||Q)   = 0.020135513550689
KL(PK||QK) = 0.020135513550689     residual 3.469e-17  -> eq:cg-kl-equality attained
||QKR_Q - Q||_inf = 0.000e+00
||PKR_Q - P||_inf = 2.776e-17
control, non-lumpable K: fine=0.0201355136 coarse=0.0029206302 (strict);
                         ||QKR_Q - Q||=5.551e-17 (always 0); ||PKR_Q - P||=5.163e-02 (recovery fails)
```

---

## CG-9 — symbol overloading across and within the two chapters, inconsistent with the manuscript's own disambiguation practice

**Location.** `06:343–353`, `06:421`, `06:564–570`; `09:45`, `09:126`, `09:271–273`, `09:296–304`, `09:352`,
`09:505`, `09:541`, `09:776`, `09:790`, `09:795`, `09:929`.
**Severity.** low.
**Status tag.** n/a (notation).

**Evidence.** In a chapter pair whose subject *is* the bookkeeping of measures, normalizers and channels, the
following glyphs each carry three or more meanings:

| glyph | meanings |
|---|---|
| `H` | congruence chart `H\in\GL(K)` in `\mathcal C_H` (`09:126`); quotient metric `D-ss^\top/n` (`09:795`); a holonomy element `\operatorname{diag}(1,-1,-1)` (`09:776`); Galerkin propagator `R^{-1}L` (`06:348`); `\mathcal H` the holonomy group (`09:671`) |
| `S` | aggregation matrix `\widehat S\otimes I_K` (`09:45`); partition selector `S(X)` (`06:421`); partial injections `S_{iI}` (`09:296–304`); a covariance `\bar S` (`09:929`) |
| `P` | probability law (throughout); Galerkin prolongator `P:V_c\to V_f` (`06:343`); tree transports `P_{v\leftarrow r}` (`09:352`); the `\{0,1\}` assignment matrix `P=\widehat S` (`09:790`) |
| `A` | anchor `A_i` (`09:30`); `\sum\Theta_e^\top W_e\Theta_e` (`09:273`); `R^{-1/2}LR^{-1/2}` (`09:541`); `\mathsf A` the log-normalizer (`06_gaussian:16`) |
| `C` | Galerkin reduction (`06:346`); `\sum W_e` (`09:271`); recovery kernel (`06:564`); edge factor `C_e` (`09:291`); covariances `C_i` (`09:607`); cone `\mathcal C_H` (`09:127`) |
| `R` | reference form (`06:343`); Bayes recovery kernel `R_Q` (`06:105`); endpoint maps `R_{i,e}` (`09:298`); metric `R\succ0` (`09:505`) |
| `Q` | recognition law (throughout); the unnamed coarse form in `\det(G^{-1}Q)` (`09:828`) |

The manuscript demonstrates it knows this is a hazard — `06:569–570` explicitly says "Here `C,R` are local
kernel notation, not the Galerkin reduction and reference form in `\eqref{eq:cg-galerkin-data}`." The
remaining collisions are held to a lower standard than the one the text sets for itself, and CG-3 is the case
where it actually costs readability.

**Fix.** Disambiguate `H` (congruence chart `\Xi`, quotient metric `M_{\mathcal P}`), `P` in `sec:cg-quotient-volume`
(use `\widehat S`, which is already defined), and `Q` in `eq:cg-quotient-generalized-determinant`; or add the
`06:569`-style one-line disclaimer at each reuse.

---

## CG-10 — `\mathcal E` carries two sign conventions and two normalizations

**Location.** `06:236–246` (`\bar P\propto e^{-\bar E}`), `06:306–313` (`\bar Z_{\mathcal P}=\int
e^{\mathcal E_\theta(\iota_{\mathcal P}\bar z)}\nu_0^{\otimes\mathcal P}`), `09:34–39`
(`\mathcal E(z)=\sum z_i^\top A_iz_i+\dots`, i.e. `z^\top\Lambda z`, entering `\exp(-\tfrac12\cdot)` per
`06_gaussian:16`), `09:530` (`\mathcal E(z)=\tfrac12z^\top Lz`).
**Severity.** low.
**Status tag.** n/a.

**Evidence.** Within seventy lines of Chapter 6, `E` enters the Boltzmann weight with a minus sign and
`\mathcal E_\theta` with a plus sign. Within Chapter 9 the same glyph `\mathcal E` denotes `z^\top\Lambda z`
at `:35` and `\tfrac12 z^\top Lz` at `:530` — a factor of two. Neither is an error inside its own section, and
the normalizer identity `Z_{\rm ind}=J_{\mathcal P}Z_{\rm std}` is convention-independent (it is a change of
reference measure, verified above at residual `0.000e+00`). But `sec:cg-quotient-volume` never displays the
density it normalizes, so the reader must guess which of the two conventions `\Lambda_{\rm c}` enters with; the
relation `Z=(2\pi)^{(m-1)K/2}\det(G^{-1}Q)^{-1/2}` that makes `eq:cg-quotient-generalized-determinant` useful
holds only for `\exp(-\tfrac12 z^\top\Lambda_{\rm c}z)`.

**Fix.** State the density once in `sec:cg-quotient-volume`; give `\mathcal E_\theta` (natural-parameter,
`e^{+}`) and `\mathcal E` (Boltzmann, `e^{-}`) distinct glyphs.

---

## CG-11 — two `\status{}` tags on one paragraph with no indication of scope

**Location.** `06_general_coarsegraining.tex:180` (`\status{ESTABLISHED} \status{NOT-CLAIMED}`),
`09_coarsegraining.tex:599` (same pair).
**Severity.** low.

**Evidence.** `main.tex:110` defines `\status` as a per-claim epistemic register, and the manuscript's contract
is one tag per non-trivial claim. A paragraph closing with `[ESTABLISHED] [NOT-CLAIMED]` and no sentence-level
attribution defeats a status audit: at `06:169–180` the first two sentences are the ESTABLISHED transfer and
the third is the NOT-CLAIMED semiconjugacy caveat, but nothing in the markup says so.

**Fix.** Attach each tag to its own sentence, as done correctly at `06:228–230`.

---

## CG-12 — the one Gaussian operation to which `eq:cg-elbo-monotone` actually applies is never identified as such (observation)

**Location.** `09:4–8` ("This chapter realizes the three operations of `\Cref{ch:coarsegraining}`"),
`09:84–90`, `09:133–160`, `09:911–915`.
**Severity.** low (editorial, not a defect).

**Evidence.** Chapter 6 classifies the operations as Markov pushforward / energy precomposition / recognition
restriction (`06:248–252`), and only the first carries `eq:cg-elbo-monotone`. Chapter 9 correctly disclaims the
hard trace at `:911–915`. What it never says is where the *positive* case lives: exact node marginalization
(`sec:cg-kron`) **is** a Markov pushforward (`06:248`), so on the congruence-diagonal cone `\mathcal C_H`,
where `thm:cg-congruence-diagonal-kron` shows closure, the chapter does exhibit a family-preserving,
evidence-preserving coarse channel — the Gaussian realization of `thm:cg-evidence-preserving-channel`.
Off `\mathcal C_H` it does not, by `prop:cg-kron-leaves-family`. Naming this would close the loop the chapter
opens at `:4–8`.

Supporting verification (all exact): `eq:cg-coarse-blocks` residual `3.553e-15` and coarse `\Lambda_{\rm c}` is
*in* the declared interaction family (residual `3.553e-15`); Kron witness leading minors
`[2,6,18,48,102,233]` residual `8.527e-14`; `\Lambda_{33}=\begin{psmallmatrix}4&1\\1&5\end{psmallmatrix}`,
`\det=19`, residual `3.553e-15`; `eq:cg-kron-asymmetric` `=\tfrac1{19}\begin{psmallmatrix}9&3\\4&14\end{psmallmatrix}`
residual `0.000e+00` with asymmetry `5.263e-02`; five-node `\mathcal C_H` Schur complement stays in
`\mathcal C_H` with correct signs, residual `6.685e-16`; `XY-YX=\begin{psmallmatrix}0&-5\\5&0\end{psmallmatrix}`
residual `0.000e+00`.

---

## CG-13 — `CHK-CG-*` supplemental check IDs are declared in the harness but referenced nowhere in the chapters (adjacent, flag only)

`verification/claims.json` declares `CHK-CG-AGGREGATION`, `CHK-CG-EPSILON-DIVERGENCE`, `CHK-CG-FACTOR-GAP`,
`CHK-CG-FRAME-CANCELLATION`, `CHK-CG-EQUIVARIANCE`, `CHK-CG-PAIR-MERGE`, `CHK-CG-BIADDITIVE`,
`CHK-CG-MAXIMAL-CLUSTERS`, `CHK-CG-LAMBDA-CONTINUUM`, `CHK-GRAPH-HOLONOMY`, `CHK-KRON-EXACT-WITNESS`,
`CHK-KRON-MONTE-CARLO`. `grep -n "NUMERICAL\|CHK-"` over `06_general_coarsegraining.tex` and
`09_coarsegraining.tex` returns **nothing**, whereas `07_restrictions.tex:200` does cite
`\texttt{CHK-RESTRICTION-SCHUR}`. So the coarse-graining checks have no in-text provenance anchor.
This is adjacent to settled R18 (clipped status registers) but is a different object — R18 concerned rendering,
this concerns linkage — and it may fall outside my lens. Severity low; flagged, not pressed.

---

# Recomputation ledger — everything that verified

100 checks in `cg_verify.py` plus 18 in `cg_verify2.py`/`cg_verify3.py`. Every manuscript identity below
verified; residuals are `\|{\rm lhs}-{\rm rhs}\|_\infty` unless noted. The three failures in the first run were
**my** construction bugs (a channel whose `Y`-supports were not disjoint; a degenerate parameter-dependent
kernel; a residual reported per-`\varepsilon`), all corrected and re-verified.

**Chapter 6.**

| result | residual |
|---|---|
| `prop:cg-markov-category` (`PK` normalized, `P(KL)=(PK)L`) | `0.000e+00` |
| `eq:cg-kl-dpi` RN formula `d(PK)/d(QK)=\bar r` | `0.000e+00` |
| `eq:cg-kl-dpi` DPI inequality | `0.000e+00` (gap `1.721e-02` in the strict control) |
| `eq:cg-kl-equality` equality attained on a lumpable channel | `3.469e-17` |
| `cor:cg-pairwise-bayes-recovery` `QKR_Q=Q` | `0.000e+00` |
| `cor:cg-pairwise-bayes-recovery` `PKR_Q=P` under equality | `2.776e-17` (fails at `5.163e-02` without) |
| converse (one `R` recovering both forces equality) | `0.000e+00` |
| `06:122–129` simultaneous-`P_0` equalities give one common `R` | `0.000e+00` |
| `thm:cg-evidence-preserving-channel` `\bar P^O=P^O` | `0.000e+00` |
| `thm:cg-evidence-preserving-channel` `\bar P_o=P_oK` | `0.000e+00` |
| `eq:cg-elbo-monotone` (rise `0.4350214790`, both `\le\log p(o)`) | `0.000e+00` |
| coarse density-form ELBO `=\log p(o)-\KL(\bar Q\Vert\bar P_o)` | `0.000e+00` |
| `07b` exact chain rule (consistency cross-check) | `0.000e+00` |
| `eq:cg-fisher-loss` `I_Y\preceq I_X`, `\theta\in\{0,0.2,0.5\}` | `0.000e+00` |
| `06:182–192` witness `I_X(0)=I_Y(0)=0.25\neq0` | `0.000e+00` |
| `06:190` no parameter-independent reverse kernel (lstsq) | residual `3.352e-01` (correctly nonzero) |
| Fisher equality iff score is `Y`-measurable (lumping control) | `0.000e+00`; strict loss `0.25` when fibres cut the score |
| `eq:cg-coarse-energy`/`eq:cg-coarse-parameters` under `eq:cg-diagonal-affinity`, 500 random blockings | `1.066e-14` |
| `eq:cg-galerkin-data` `CP=I`, `H_c=R_c^{-1}P^\top LP` | `5.638e-16`, `1.388e-16` |
| `eq:cg-message-residual` `CH-H_cC=CH(I-PC)` | `1.561e-17` |
| `PC` is the `R`-orthogonal projector; `H` `R`-self-adjoint | `2.665e-15`, `1.332e-15` |
| invariant `\operatorname{range}P` `\Rightarrow` exact message passing | `8.327e-16` |

**Chapter 9.**

| result | residual |
|---|---|
| `eq:cg-aggregation-matrix` `S^\top S=\operatorname{diag}(n_I)\otimes I_K` | `0.000e+00` |
| `eq:cg-coarse-blocks` (`prop:cg-gaussian-aggregation`) | `3.553e-15` |
| coarse `\Lambda_{\rm c}` lies in `eq:cg-interaction-family`; PSD by congruence | `3.553e-15`, `0.000e+00` |
| `prop:cg-kron-leaves-family`: minors, `\Lambda_{33}`, `eq:cg-kron-asymmetric` | `8.527e-14`, `3.553e-15`, `0.000e+00` |
| `thm:cg-congruence-diagonal-kron` Schur stays in `\mathcal C_H` (5 nodes, 2 eliminated) | `6.685e-16` |
| `09:169` `XY-YX=\begin{psmallmatrix}0&-5\\5&0\end{psmallmatrix}` | `0.000e+00` |
| `eq:cg-weighted-invisibility` on the `09:251–263` triangle; loop `=2I` | `0.000e+00`, `0.000e+00` |
| `eq:cg-cut-excess` `\Delta=A-B^\top C^{-1}B=\sum(\Theta_e-\bar\Theta)^\top W_e(\Theta_e-\bar\Theta)\succeq0` | `3.553e-15` |
| `\Delta=0` iff common twists; `09:284` `\bar\Theta=0` witness | `1.776e-15`, `0.000e+00` |
| `prop:cg-kernel-holonomy` `\dim\ker L_I=\dim\operatorname{Fix}(\operatorname{Hol})` (`=1` for `\operatorname{diag}(1,-1,-1)`; `=K` trivial) | `0.000e+00` |
| `prop:cg-nested-sections-compose` `\ker L_A=\iota\ker L_A^{(1)}` (dims `2=2`) | `2.220e-16` |
| `eq:cg-partial-properness` `L_I\iota_I=0`, `\Lambda_{\rm c}\succeq0` | `1.110e-16`, `1.443e-17` |
| `prop:cg-gaussian-fixed-relaxation`: convergence to `\Pi_0^Rz_0`, `eq:cg-transverse-decay`, `eq:cg-fixed-flow-dissipation` | `3.566e-12`, `0.000e+00`, `3.673e-10` |
| `eq:cg-flow-congruence` `\Pi_0^{R'}=T\Pi_0^RT^{-1}` | `1.865e-14` |
| `eq:cg-fixed-covariance-kl` and the natural-gradient identification | `0.000e+00` |
| `prop:cg-gaussian-forward-kl-barycenter` moments + `eq:cg-gaussian-barycenter-score` | `1.110e-16`; unbeaten in 2×10⁴ perturbations |
| `cor:cg-compact-holonomy-barycenter` (`C_{\mathcal H}\succ0`, invariance, `eq:cg-gaussian-haar-score`, minimality) | `0.000e+00`, `0.000e+00`, `4.441e-16`, `0.000e+00` |
| `09:666` witness `\tfrac12\log(1+\lVert u\rVert^2)` | `5.551e-17` |
| `eq:cg-fixed-covariance-pairwise-identity` (both forms) | `1.110e-16` |
| `eq:cg-trivial-holonomy-large-kl` `=2a^2`; `09:753–757` `=2`; `H` preserves `\mathcal N(0,\sigma^2I)` | `1.110e-16`, `0.000e+00`, `0.000e+00` |
| `eq:cg-quotient-metric` (`\ker H`, `\operatorname{pdet}H`, cofactor, variational form) | `2.220e-16`, `3.553e-15`, `8.882e-16`, `2.075e-11` |
| `eq:cg-quotient-jacobian` `J_{\mathcal P}^2=(\operatorname{pdet}H)^K` | `1.028e-15` |
| `eq:cg-quotient-generalized-determinant`; `Z_{\rm ind}=J_{\mathcal P}Z_{\rm std}` | `0.000e+00`, `0.000e+00` |
| `eq:cg-mean-tie-cost`, `eq:cg-loewner` (+ equality case) | `1.421e-14`, `0.000e+00`, `5.329e-15` |
| `eq:cg-epsilon-divergence` (exactly `O(\varepsilon)`, coefficient `\tfrac12\Tr\Lambda_{22}`, robust to free cross-covariance) | `\le 2.946e-01\cdot\varepsilon/10^{-2}` |
| `eq:cg-factorization-gap` (+ Fischer monotonicity under merging) | `1.776e-15`, `0.000e+00` |
| `eq:cg-frame-cancellation` mean and covariance | `2.220e-16`, `5.684e-14` |
| `09:934–939` no left-equivariant permutation-symmetric `F` | `\lvert\det(I-v)\rvert=3\neq0` |

**Counterexample attempts that failed (i.e. the manuscript survives).**

1. `Q`-dependent coarse channel breaking `eq:cg-elbo-monotone` — 2×10⁵ trials, max violation `0.000e+00`.
2. `o`-dependent coarse channel breaking evidence preservation — `0.000e+00`.
3. All-pairs KL equality without a common recovery kernel — 2×10⁵ random configurations, none found.
4. Free cross-covariance blocks changing `eq:cg-epsilon-divergence` at `O(1)` — they change it at `O(\varepsilon)` only.
5. Free-covariance perturbations beating the moment-matched barycenter / the Haar barycenter — 4×10⁴ trials, none.
6. Random `\nu\in\operatorname{range}(B)` beating `\mathcal G_{\rm tie}` — 2×10⁴ trials, none.
7. Non-representable diagonal restriction breaking `thm:cg-graph-exponential-closure` — correctly *does* break
   it (residual `3.886e+00` against the best affine representation), confirming
   `eq:cg-diagonal-affinity` is load bearing rather than cosmetic.

**Probes confirming that stated hypotheses are load bearing.**

- Parameter-dependent `K_\theta` reverses the Fisher inequality: `I_X(0)=0.250000`,
  `I_Y(0)=400.000000` — violation `399.75`. So "let `K` be parameter independent" in
  `thm:cg-fisher-contraction` is genuinely required, and the chapter's insistence at `06:58–60` is right.
- Sub-Markov `K` reverses the ELBO ordering (CG-4 table).
- Non-lumpable `K` breaks Bayes recovery (`5.163e-02`) while `QKR_Q=Q` still holds (`5.551e-17`) — confirming
  the asymmetry `cor:cg-pairwise-bayes-recovery` states.

---

# Cross-reference and label integrity (both chapters)

`labelcheck.py`, resolving both `\label{}` and the `\*heading{}{}` macro form:

```
06_general_coarsegraining.tex  refs: 25  MISSING: []
09_coarsegraining.tex          refs: 29  MISSING: []
duplicate labels: []
```

No dangling references, no duplicate labels. The only unresolved *symbols* are CG-1, CG-2, CG-3.
