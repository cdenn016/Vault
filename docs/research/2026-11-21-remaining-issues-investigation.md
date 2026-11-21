# Remaining issues: four-investigator reports (2026-11-21)

Four read-only investigators ran in parallel. Each finding below is single-investigator evidence (no skeptic pass); statuses are as the investigators reported them, and numerical claims rest on scratch scripts that were not rerun by the coordinator. Paths: `CA/` = `manuscripts/Collective_Agents/sections/`, `MA/` = `manuscripts/MAgent_Theory_2.0/chapters/`.

## Ranked synthesis

**Critical**

1. **The two-firms candidate is not a meta-agent: contrast is undefined** (two-firms F1, computed, new). The world-conditional precision of the firm's members is not diffusive at every declared setting, for two structural reasons: a collider through the price (both firms' order flows set it) and the singular lazy-ring consensus matrix (eigenvalue 0 on the alternating vector). So `def:col-collective` cannot be applied and the exact-fusion clause fails with it. Closure, partner randomization and agency pass. The only passing modification found (homogeneous noise, no consensus coupling, non-performative acts) is degenerate. Fix: in `rem:agy-h1-status` (`CA/s05_agency.tex:247`) and `rem:met-no-selection` (`CA/10a_meta_agents.tex:270-272`), replace "contrast … not computed" with "precision not diffusive, contrast undefined, fails the collective clause". The existence problem stays open, now with a sharper obstruction: a meta-agent candidate needs a diffusive precision, which colliders and singular consensus both destroy.

**Major**

2. **The two-firms agency computation evaluates the wrong act law** (two-firms F3, new). The dynamics use Gaussian acts with independent noise; the agency paragraph evaluates a discrete logit chain. A linear-Gaussian deliberation model exists (Gaussian habits, Gibbs conditionals, stationary law equal to the tilted group posterior of `thm:met-h5a`(v)); evaluated on the actual act rule the index is 0.91 to 0.99 and depends strongly on the declared habit variance.
3. **`conj:agy-synchronous` is half proved and half refuted** (notes F1, reconstructed). The literal same-γ statement and the binary-policy class statement are proved (note's C1, C2); for |A_i| ≥ 3 the strong reading the main text uses is false (C3, C4 reconstructed independently, TV 2.5e-16). Text at `CA/05_agency.tex:253`, `s01_introduction.tex:146`, `10e_open_problems.tex:80`, `11_predictions.tex:13`, `ext3_obj.tex:165` still calls it conjectured. Fix: proposition (C1, C2) plus a counterexample example.
4. **The formation theorem's merged branch rests on a calibration that is off by a factor of about 8 there** (Tier 2 F1, computed, new). Self-consistent calibration keeps a symmetric merged fixed point to at least γ = 350, past the frozen fold (105.9) and γ_T (242.1). The theorem about the frozen map stays correct; the bistable window and "single attracting fixed point above γ_T" are frozen-map properties only, and `open:frm-self-consistent` gets a negative answer at the base point. Stability of the self-consistent branch is only partly checked.
5. **Exact fusion is not a global posterior** (unification F2, refuted as stated). CA's exact fusion is each agent's fixed-model posterior under the true conditional likelihood, not the agent's block of one global posterior. Mean and posterior-sample messages have identical cross-covariances and differ only in variance; the comparison report's reading of `imem:scalar-calibration` was wrong. Unification obligation 1 therefore fails as posed and needs restating as a per-agent identification.
6. **Level-0 is explicit Euler of MA's per-agent mean flow** (unification F1, proved). With F = I, Q = 0, CA's level-0 step is one explicit-Euler step (h = 1) of MA's frozen-covariance, frozen-source per-agent Gaussian flow (also implicit Euler in the prior metric). So CA's literal receivers implement MA's per-agent picture, not the reciprocal potential. Differences: frozen covariance, a stricter stability condition (ρ(W) < 1 against Re spec(W) < 1), and CA's strict light cone, which is a discrete-step artifact absent from the flow.
7. **`open:coh-amplification-noisy` (c) is answered** (notes F2, self-proved, partly reconstructed). With a common code of rank ≥ 2, amplification is excluded for all priors iff the noises are proportional; for N = 2 the supremum is exactly cosh²(d_H/4).
8. **`open:nrg-rate` is largely answered by `problem_8.md`** (notes F3). Its C2 (lossless retention iff row(C) ⊇ range(Ω)) was reconstructed independently; C1 is long and author-checked only; C4 refuted correctly; C5 open. `CA/ext6_nrg.tex:3, 59-65, 156-158` should be updated once C1 gets a fresh check.
9. **Contrast is frame-invariant only under the covariant action** (unification F3). Under an action that fixes a reference object it is not, by the mechanism of `CA/ext2_rfm.tex:113-120`. Unification obligation 4 holds in its covariant form.
10. **MA (F4) grading differs by declared probe rule, unflagged** (Tier 2 F3). Ch. 12's pass rests on an external querier of the kind ch. 13 declines; the chapters should state the probe class each uses.

**Minor**

11. Calibration-root uniqueness holds wherever sampled and is unproved (Tier 2 F2). 
12. The ring wall count (walls − Ψ ∈ {−1, 0, 1}) holds in exhaustive search, self-proved, not in the manuscript (notes F4); the manuscript's bounds are looser than the note's.
13. MA companion `c18` still has the 0.2 percent pitchfork framing (unification F4).
14. Two-firms: inference clause exact only for noiseless members (needs α_I ≥ 0.0134); agency passes in the discrete model for any Agency_0 below 0.72 at n_c = 1, but no Agency_0 is declared (two-firms F4, F5).
15. Tier 2 items 1, 2, 3b, 3d, 4, 5, 9, 11, 12: confirmed and already acknowledged in the text; no error. The coverage grep of MA companion, supplements and Items, and CA ext3/4/6/7 found no other stale theorem-level claim (not a full audit).

The raw reports follow.

## Investigator: two-firms-meta-agent

## Verdict

C_1 in ex:met-two-firms is **not a meta-agent** under def:agy-meta-agent at the declared parameters. It fails the first clause. Its world-conditional precision Π^c is **not diffusive**, so contrast r(C_1) is undefined (def:col-contrast, 04_collectives.tex:182; def:col-collective, 04_collectives.tex:214-221 requires a diffusive precision). Because exact-fusion survival needs "blocks at r ≥ r_0" (def:agy-nulls, 05_agency.tex:332-335), that clause fails with it. The other clauses pass:
- closure (exact)
- partner randomization, using the manuscript's substitute MI selector (p = 0.01, the minimum possible with 99 draws)
- agency, for any declared Agency_0 below the computed index

The non-diffusivity has two separate structural causes in the example. I found a modification that passes the contrast clause only by removing both of them, and that variant is degenerate. Status: computed (numerical linear algebra on an exact reconstruction of the model). This finding is new: the manuscript says contrast was "not computed" (s05_agency.tex:247; 10a_meta_agents.tex:270-272) and does not say that it is undefined.

## (1) Findings, ranked

**F0. The reconstruction is validated.** Status: computed. I rebuilt the fine process from s10a_meta_agents.tex:108-127. It reproduces every reported number I checked:
- dimensions 49 and 33
- ρ(A) = 0.7972 and 0.8240
- P̄_2 = 0.125711
- ρ(F̄) = 0.6178
- C_1 predictive and filtered price variances 0.117717 and 0.081666
- error variance of the member average 0.117717 (exact model) and 0.127339 (bounded model)
- E[a_C] ≈ −0.650 at n_c = 4

Everything below is computed from this model.

**F1 (critical, new). The contrast clause fails because Π^c is not diffusive at every declared setting.** Location: ex:met-two-firms against def:col-contrast and def:col-collective. I computed Π^c as the inverse of the one-time conditional covariance of the 8 members' price-coordinate filter states, conditioned on the price path over a 61-round window. Relative convergence between T = 40 and T = 60 is ≤ 3×10⁻⁷.

| Setting | Largest positive off-diagonal entry | Smallest row sum |
|---|---|---|
| Exact, n_c = 1 (declared) | +156.9 | −1.16 |
| Exact, n_c = 0 | +0.0515 | 3.55 |
| Exact, n_c = 4 | +0.0895 | −11.0 |
| Bounded, n_c = 1 | +166.3 | −0.82 |

The two causes:
- **(a) Collider through the price.** Both firms' order flows drive p, so conditioning on the p path pins b(a_{C1} + a_{C2}) + w. This gives every cross-firm entry a positive value of about 0.03 at every n_c. Even with g_u = 0 the act noise still moves the price, and the entry stays at about 0.012. The sign argument is heuristic; the values are computed.
- **(b) Consensus mixing of sensory noise.** The declared lazy ring W = ½I + ¼(shifts) is singular, with eigenvalue 0 on (1,−1,1,−1) (proved: ½ + ½cos π = 0). That direction receives only the 10⁻³ computation noise, so Π^c contains a large rank-one term along it. This is the +122/+157 entries between opposite members. With a nonsingular ring (κ = 0.15) the opposite-member entry is still +8.8, consistent with the distance-two sign pattern of W⁻¹.

The formal r(C_1) values (2.68 at n_c = 1, 0.46 at n_c = 0) are undefined per the manuscript. Even taken formally, the n_c = 0 value is below 1.

For the exact model there is an additional problem. Members' filter states are 5-dimensional, so contrast also needs the Kronecker form Σ^sc ⊗ I_K or a declared scalar error coordinate. Neither is declared.

Smallest fix: replace "its contrast at a level r_0 > 1 … not computed" in rem:agy-h1-status (s05_agency.tex:247) and rem:met-no-selection (10a_meta_agents.tex:270-272) with "its world-conditional precision is not diffusive (collider through the price, singular consensus matrix), so contrast is undefined (open:col-non-diffusive) and C_1 fails the collective clause".

**F2 (major, new). The only passing modification I found is degenerate.** Status: computed. The variant (bounded model) is:
- homogeneous sensing noise R = (1,1,1,1) in both firms
- n_c = 0
- acts with no price effect (b_act = 0)

Π^c is then diffusive (largest off-diagonal 7×10⁻¹⁵) and ε_max/ε̄ = 1. r(C_1) = 1.02983, against these baselines:
- Exchangeable mean-coupling baseline, def:col-baseline(c): r̄_hom = 1.02557, attained by the whole population. C_1 is a collective for r_0 ∈ (1.0256, 1.0298], a margin of 0.4%.
- Declared interaction-graph baseline, clause (b): r̄_hom = 1.02983 = r(C_1), attained by C_1 itself. The strict inequality fails.

In this variant the acts are not performative, so the deliberation law equals the habits and Agency = 1 only by the denominator-zero convention, which is vacuous. Heterogeneous R or b_act ≠ 0 brought back positive entries in every case I computed. A non-degenerate passing modification is **open**.

**F3 (major, new; answers the reviewer). The agency computation evaluates a different act law from the population's own.** In the fine process (s10a_meta_agents.tex:109) acts follow u_i = −g_u p̂_i + N(0, 0.01). Given the members' estimates this is a product law. The agency paragraph (s10a_meta_agents.tex:143) instead evaluates a discrete logit chain on {−1,0,1}⁴, whose stationary law is correlated through a_C. So the reviewer's objection is stronger than "not strictly linear-Gaussian": the deliberated acts are not the acts in the dynamics.

A linear-Gaussian version exists:
- Use continuous u_i with Gaussian habits N(0, σ_E²) and G_C = (Λ*/2)(f m_C + bΣu)².
- (P4) becomes random-scan Gibbs with linear-Gaussian conditionals u_i | u_{−i} ~ N(−c(f m_i + bΣ_{j≠i} u_j), 1/(σ_E⁻² + γΛ*b²)).
- Its stationary law is N(−K⁻¹γΛ*bf m, K⁻¹), with K = σ_E⁻² I + γΛ*b² 11ᵀ. This is the tilted group posterior of thm:met-h5a(v).
- Gibbs invariance for densities is standard. CA states the result only for finite policy sets (def:agy-group-model, 05_agency.tex:157), so treat this as a derivation, not an established result in CA.

Two routes:
- **Route A (recommended).** Keep the fine-process act rule and evaluate the agency index on it with a Gaussian class (Λ* = 4, γ_C free). With σ_E² = 0.01 the index is 0.9108 without tilts and 0.9936 with tilts at the n_c = 1 dispersion. It is strictly below 1 because the act noise is independent while any group posterior with γ_C > 0 and b ≠ 0 correlates the acts. The index depends strongly on the declared habits: with σ_E² = 0.1 it is 0.060.
- **Route B.** Use the deliberated law as the act rule. This gives index 1, but the act noise is then correlated across channels, which breaks the per-channel-noise hypothesis of thm:met-h5a. Whether (i) still holds is unchecked.

Smallest fix: keep the open problem's wording, and change the example's agency evaluation to Route A with a declared σ_E². If the discrete model is kept, the open problem should say "linear-Gaussian dynamics, with agency evaluated on a declared finite deliberation model at decision states".

**F4 (minor, new). The agency clause passes in the discrete model as stated, but the result depends on the declared class.** Status: computed. Setup: decision state m_C = 0.3, γ = 2, Λ* = 4, deviations drawn at the stated dispersions, 200 draws. With uniform habits held fixed and γ_C ≥ 0 fitted:

| n_c | Agency index | Fitted γ_C |
|---|---|---|
| 0 | 0.33–0.34 | ≈ 2.0 |
| 1 | 0.715–0.72 | ≈ 2.0 |
| 4 | 0.994 | ≈ 2.0 |

The index is 1 for any class that contains the tilted-habit model. So Agency_0 = 0.5 passes at n_c = 1 with a margin of about 0.21. No Agency_0 is declared in the text.

**F5 (minor, new). The inference clause is exact only for noiseless members.** Status: computed. With the declared computation noise of 10⁻³, the expected relative entropy from N(y^η, P̄⁻) to the exact predictive law is 0.01336 nats (price marginal 0.00196). So α_I must be at least 0.0134; Table tab:met-firms reports noiseless members only. The memory clause holds at α_M = 0 (d_cl ≈ 10⁻¹¹ in the table; it is closed exactly by thm:met-h5a(ii)).

**F6 (minor). Partner randomization passes with the substitute selector.** Status: computed. The selector is the MI ratio of s05_agency.tex:232. I redrew consensus partners for all 8 receivers (2 partners, quenched) and kept the order-flow read at firm level, which is my own declaration choice. The full model's statistic is 1989, with the argmax block equal to C_1. Over 99 null draws: median 4.05, 95% quantile 11.3, maximum 27.8, so p = 0.010. This does not rescue the collective clause, which needs contrast.

**F7 (minor, interpretive). Exact fusion is close to an identity intervention here.** The members already fuse in information form, so 𝔑_ex changes nothing, and survival reduces to the contrast clause. That clause is undefined, so this clause fails too. Whether C_2's bounded dynamics model counts as "misreading" is interpretive. I did not compute the type-D deletion and freezing nulls with the MI selector (see section 2).

## (2) What I could not settle

- A non-degenerate modification of the example that passes every clause. Removing the price collider requires acts without effect on the world or a different conditioning set. Removing the consensus-induced positive entries needs a protocol whose noise precision is diffusive. I found neither.
- Whether the type-D deletion nulls (𝔑_lp, 𝔑_inf), evaluated with the MI selector, give a partition different from the full model's. With within-firm order-flow reads intact, 𝔑_lp alone may keep {C_1, C_2}.
- Whether Route B's correlated act noise keeps thm:met-h5a(i).
- Whether the substitute MI selector is admissible for the collective clause. I read the definition as saying it is not; it only serves the tests.

## (3) Commands run and outputs

All scripts are in `C:/Users/CHRISA~1/AppData/Local/Temp/claude/63c81c17e87f0010/34faeca5-ea90-45d1-8cc4-412bdf898c58/scratchpad/firms/`. Each was run single-threaded with bare `python`.

- **`model.py`**: reconstruction of the fine process.
- **`validate.py`**: prints Pbar2 0.12571, ρ(F̄) 0.6178, predictive 0.11772, filtered 0.08167; dim 49, ρ(A) 0.7972, error variance 0.117717; dim 33, ρ(A) 0.8240, error variance 0.127339.
- **`contrast.py`, `scan.py`**: Π^c matrices. Declared n_c = 1: max off-diagonal 156.9, diffusive False. n_c = 0: 0.0515, False. κ = 0.15: 8.76, False. No acts, n_c = 0: 0.0122, False. T-convergence ≤ 3×10⁻⁷.
- **`scan2.py`**: with R = 1111, b_act = 0, n_c = 0: diffusive True, r(C_1) 1.0298. Graph baseline 1.02983 at (0,1,2,3); exchangeable baseline 1.02557 at the whole population.
- **`agency.py`**: discrete agency index medians 0.340, 0.7205, 0.9938 at n_c = 0, 1, 4. KL(P‖E) = 0.1535 and E[a] = −0.6497 with no dispersion.
- **`agency_lg.py`**: Gaussian route. σ_E² = 0.01: untilted 0.6501, 0.9108, 0.9933; tilted 0.9924, 0.9936, 0.9947. σ_E² = 0.1: about 0.06.
- **`npr.py`**: selector 1988.8 with block (0,1,2,3); null q95 11.3, max 27.8, median 4.05; p = 0.010.
- **Inline inference check**: expected KL 0.013355 (price marginal 0.001964); ρ of the closed-loop matrix 0.636.

Files read: 05_agency.tex:10-40, 150-262, 300-402; 04_collectives.tex:128-225; s05_agency.tex:232, 246-280; s04_collectives.tex:267; 10a_meta_agents.tex:200-300; s10a_meta_agents.tex:1-200; chk10a_meta_agents.tex:54-56. No repository or vault files were modified.

## Investigator: self-reviewed-notes

## Fresh-context check of four CA research notes (verdicts first)

**(a) conj_agy_synchronous.md: confirmed. The conjecture as written is true, and its intended strong reading is false once |A_i|≥3.** "Refuted for |A_i|≥3" holds only for the free-precision / strong-class reading, which is the one the main text uses. The literal same-γ statement in `s05_agency.tex:107-109` is proved (note's C1).

**(b) open_coh_amplification_noisy.md: every claim I tested holds.** The decisive answer is C7: amplification under a common code of rank ≥2 is excluded for all priors if and only if the noises are proportional. For N=2 the supremum is exactly cosh²(d_H/4). The note is self-reviewed only.

**(c) problem_8.md: the claim statements hold numerically, and I reconstructed C2 independently.** C1 (the limit plus a second-order constant at exponential rate) is a long proof that only its author has checked. C4 is correctly marked refuted. C5 is open.

**(d) Ring claim and sca C5.** Walls minus Ψ ∈ {−1,0,1} on rings holds in an exhaustive brute-force search. It is self-proved only, and the manuscript does not contain it. sca C5 is open, and the narrowed `conj:sca-common-code` (`s08_scale.tex:12-16`) states it exactly. No edit is needed there.

### 1. Findings, ranked

**F1 (major; new to the manuscript; refuted / proved).** The main text says the strong statement is conjectured, but for |A_i|≥3 it is false.
- **Locations:** `05_agency.tex:253` says "the corresponding failure for three or more members is conjectured", and the "corresponding failure" is the class statement of `prop:agy-synchronous` (no group posterior with product habits, γ_C>0 and redundant slots). The same framing appears at `s01_introduction.tex:146`, `10e_open_problems.tex:80`, `11_predictions.tex:13` (which lists the conjecture among those with refuting observations) and `ext3_obj.tex:165`.
- **Evidence, recomputed end to end:**
  - **C3 (same group model, other precision).** I built the 12-dimensional Gaussian slot model myself, computed G_C from log-determinants and took ψ_s as the slot entropy. At ε=0.05, a=0.1, solving the three Z-equations gives b=0.167276, c=0.010605, γ_C=0.010398. The resulting law satisfies TV(P_sync(γ=1), P_C(γ_C; E, G_C)) = 2.5e-16. At the same γ, TV(P_sync, P_C(1)) = 6.786574e-3. The pairwise redundancies come out as the targets 0.1, 0.167276, 0.010605, 0.1.
  - **C4 (closed-form reversed cycle).** log P_sync fits unary terms plus reversed-cycle interactions 1[π_i=1]1[π_{i+1}=2] with residual ≤3.2e-14 at γ = 0.2, 1 and 5. The coefficients are all negative, which means positive redundancy. In the clockwise basis the residual is 1.4e-4 to 8.9e-2.
  - **Why C4 works.** Peretto's synchronous stationary law is ∏w_i ∏Z_k(π_{k−1},π_{k+1}). Each Z_k depends only on two indicators, so it is exactly pairwise. Its cross-ratio is −(B−x)(C−y)<0, which I derived by hand.
- **Status:**
  - C1 (literal, same γ): proved. I re-derived the second-difference identity and the one-step residual step. The one-step residual is nonzero for these instances (TV 0.009 and 0.027).
  - C2 (binary policies, all n, strong class): proved. I reconstructed it from the antitone coupling, Harris's inequality, and the negative covariance under redundancy.
  - C3 and C4: refute the strong reading; computed and proved.
- **Fix:**
  - Replace `conj:agy-synchronous` with a proposition stating C1 (P_sync = P_C(γ) if and only if all conditional redundancies vanish) and C2 (binary policies, any n ≥ 2: no redundant group posterior with γ_C>0).
  - Add an example (C3 or C4) showing that for |A_i|≥3 synchronous deliberation can reproduce a group posterior of the same model at a smaller γ_C. That instance has agency index 1 in any class that holds (q_C, 𝔅, ψ, E) fixed and leaves γ_C free.
  - Rewrite `05_agency.tex:253` and the four cross-references to match.
  - Optional: C3's γ_C ≈ 0.0104 shows the "precision bounded below" escape clause of `05_agency.tex:251` has bite. Say so.

**F2 (major; new; proved by the note, partly reconstructed by me).** `open:coh-amplification-noisy` (`s06_coherence.tex:143-145`), part (c), now has an answer that removes the open clause.
- **C7(1).** Proportional noises R̂_i = α_i R̂_0 give ρ ≤ ∏ snr/(1+snr) < 1. This follows by similarity through R̂_0^{1/2}, and it generalizes the scalar clause of `prop:coh-no-amplification(d)`.
- **C7(2).** Non-proportional noises give sup over priors of ρ = cosh²(d_H/4) > 1 for N=2.
- **Checks:**
  - With a rank-one-limit grid over prior directions, I reproduced the supremum to 4 digits in both test cases: 3.0244 vs 3.025, and 1.35037 vs 1.35042.
  - 20,000 random priors gave a maximum of 1.101, below the formula's 1.350.
  - 3,000 random proportional-noise 3-cycles gave a maximum ρ of 0.99994.
  - The Kantorovich lemma of C6(2) had 0 violations in 5,000 trials.
  - The registered instance has supremum (10M+1)²/(40M) = 3.025 at M=1, which is consistent with the manuscript's 1.36 for its particular priors.
- **N≥3.** I only sketched the extension (pad the non-chosen edges with large isotropic priors so B_j ≈ I). I did not test it numerically.
- **Fix:**
  - In `prop:coh-no-amplification(d)`, add the proportional-noise case.
  - Replace the last sentence of the open problem with C7: proportionality is necessary and sufficient, with the exact N=2 supremum.
  - Keep (a) and (b) open but cite the partial results:
    - C1: noisy round trips break `thm(b)`. I confirmed ρ(A_c)=0.5, ρ(Ā)=7/6 at base 1 and 1 at base 2, so amplification depends on the base point.
    - C4: posterior headers never amplify. I rederived the bound, and 1,500 random 3-cycles gave 0 violations.
    - C5: lagged headers can amplify. This is a single-round snapshot, not a stationary Riccati orbit, so state it that way.
- Run the note's pending O1 fresh-context check on C2, C3 and C6 before adoption.

**F3 (major once adopted; new; computed, and C2 proved).** `open:nrg-rate` (`ext6_nrg.tex:156-158`), `obs:nrg-spectral` (`ext6_nrg.tex:59-65`), and the section abstract at `ext6_nrg.tex:3` ("rate of a coarse description, which is supported by computation only").
- **C1.** In the directed ring, n·ē − D_n = 0.0884361126 at n=8 and 0.0884361144 at n=16, 32 and 64, with ē = 0.346653. That is consistent with an O(τⁿ) remainder. The first-order limit is a classical Gaussian relative-entropy-rate statement, but no primary source is checked, and the second-order proof is self-reviewed only.
- **C2.** I proved it independently.
  - S_full⁻¹ − S̄_full⁻¹ = 2i sinθ Ω.
  - The bound ē ≤ ep holds pointwise, because complex-Gaussian data processing applies and both log-determinant terms vanish.
  - Equality forces the conditional law on ker C to match, which means Ω z = 0 for every z ∈ ker C.
  - Numerically at d=5 with rank Ω = 4, ē(range Ω) = ep = 16.19164 and a tilted C gives 10.93.
- **C4 (refuted).** I reproduced the mixed-subspace fractions 0.570743 and 0.960691 and the invariant-plane fraction 0.5. One deviation, 0.5002, is quadrature error.
- **Fix:**
  - After a fresh-context check of C1, upgrade `obs:nrg-spectral` to a theorem (limit and e₀). Otherwise state only the first-order limit, with a checked primary citation.
  - Add C2 as a proposition: lossless if and only if row(C) ⊇ range(Ω), the minimal lossless dimension is rank Ω, and an odd-d system loses nothing at m = d−1.
  - Add the C4 fact that invariant subspaces are not optimal and no uniform cap below 1 exists.
  - Narrow `open:nrg-rate` to C5 (closed-form maximizers for 2 ≤ m < r_Ω).
  - Update `ext6_nrg.tex:3`.

**F4 (minor; new; computed, proof self-reviewed).** The wall counts in the manuscript are now looser than what the note establishes.
- **Evidence.** Exhaustive 2^N search over 2,500 instances with N ∈ {3, 5, 8, 11} and J ∈ {0.5, 1, 2}:
  - Ring walls − Ψ has histogram {−1: 1356, 0: 1066, +1: 78}.
  - Open-chain domains − Ψ has histogram {0: 1592, 1: 800, 2: 108}.
- **Status:** consistent with the note's C2 (rings and chains) and with the range of C3. I did not check C3's σ_flip/σ_end formula term by term, or the drawdown bound in C4.
- **Text:** the widened `conj:coh-walls` (`app06_coherence.tex:210-211`) and `06_coherence.tex:174` agree with C3's range. `lem:coh-counting` (`app06_coherence.tex:186-188`, ⌊Ψ/2⌋−1 ≤ walls ≤ 2Ψ+4) and the constants 26(J/h)²+7 in `thm:coh-domains-1d(b)` are outdated but still true.
- **Fix:** after a fresh check, either replace `lem:coh-counting` with walls ∈ [Ψ−1, Ψ+1] on rings and chains and promote `conj:coh-walls` to a proposition (generic case, with lim ℓ̄_N = E T_J), or keep the conjecture and add the ring statement as a remark marked computed.

**F5 (no edit needed; open).** The sca note's C5 is the narrowed `conj:sca-common-code` word for word. Its Q ≻ 0 is implicit in the manuscript, and the status labels at `s08_scale.tex:15-16` and `09_minimal.tex:36` match the note.

### 2. What I could not settle
- The full proof of problem_8 C1 (the second-order constant and the 2d×2d boundary-integral formula for e₀). I only checked one instance numerically.
- Coherence note:
  - C7(2) for N≥3 is only a sketch with no numerical test.
  - The C3 characteristic equations are unchecked. I verified the τ° dichotomy only given those equations.
  - C5 is not shown on a stationary filtered orbit.
- Walls note: C3's exact σ_flip/σ_end formula and the C4 drawdown constant (π+4)/√(2π) are unchecked.
- Whether the authors meant the same-γ or the free-γ reading of `conj:agy-synchronous`. The text supports both, which is why both statements should appear.

### 3. Commands run and deciding outputs
All scripts are in `C:/Users/CHRISA~1/AppData/Local/Temp/claude/63c81c17e87f0010/34faeca5-ea90-45d1-8cc4-412bdf898c58/scratchpad/inv_notes/`, run with bare `python` and single-threaded.

- **`agy.py`:**
  - C4 reversed-cycle fit residual 2.66e-15, 5.33e-15 and 3.20e-14 at γ = 0.2, 1 and 5. Clockwise-basis residual 1.4e-4 to 8.9e-2. Best same-model TV over γ_C is 0.0237, so C4's law is not a same-model posterior.
  - C3: `TV(sync, P_C(gC))=2.549e-16  TV(sync,P_C(1))=6.786574e-03`, with E = (0.05924, 0.47038, 0.47038) and R_s = 0.0535276.
  - C1 random instances: TV 0.0093 and 0.0275.
- **`coh.py`:**
  - The first run exceeded the time limit and was killed. I reran it with a lighter grid.
  - Output: `C1a rho(Ac)=0.5 rho(Abar base1)=1.1667 rho(Abar base2)=1.0`; posterior bound violations 0/1500; Kantorovich violations 0.
  - N=2 grid supremum 3.02440 vs formula 3.025, and 1.350368 vs 1.350420.
  - Random maximum 1.101; proportional-noise maximum 0.99994.
- **`nrg.py`:**
  - Ring: ep = 0.925926, ē = 0.3466535, n·ē − D_n = 0.08843611 for n from 8 to 64.
  - d=5: rank Ω = 4, ē(range Ω) = ē(I) = 16.19164, tilted C gives 10.927.
  - C4 fractions: 0.570743 vs 0.571429, and 0.960691 vs 0.962029.
- **`walls.py`:** the ring and open-chain histograms quoted in F4.

The repository and vault were not modified.


## Investigator: tier2-sweep

## Tier 2 verification (items 1, 2, 3, 4, 5, 8, 9, 11, 12)

**Verdict.** Every item is confirmed in substance, and every item except one part of 8 is already acknowledged in the text. There are two new findings. (A) Item 3a is quantitatively worse than "acknowledged": on the merged branch the frozen split calibration is off by about a factor of 8 in the cross-edge mismatch cost, and with self-consistent calibration the merged branch persists well past the frozen fold and past γ_T. (B) Item 8 is not a misapplication of (F4). It is an unflagged difference in declared probe rules: ch. 12's (F4) pass rests on an external querier of the kind ch. 13 declines. On item 3, the uniqueness of the calibration root is numerically settled (unique everywhere sampled) but not proved.

### (1) Findings, ranked

**F1. CA item 3a: the frozen calibration is used on the merged branch, where it is far off (major, new, computed).**
- **Location.** `CA/07_formation.tex:107` (asm:frm-mean-field(a)) and `:111` ("Part (a) is accurate on the split branch").
- **Merged-branch numbers that use it.** `07_formation.tex:153`: γ_M=6.84, folds at 60.05 and 105.9, symmetry breaking at 87.9. `s07_formation.tex:36`: γ_T=242.1. `tab:frm-stochastic`, "merged branch; 0.344, 0.127". `open:frm-closure` (`07_formation.tex:297`).
- **Method.** I built the frozen-slow stationary second moments of (e, η) for the 8-agent model at the base point. They are exact over all 35 attention sets per receiver, with cross error φ=±xϑ. From them I computed the model's own idealized calibration E‖ỹ−η‖²/K at the current error (def:frm-two-group(v)).
- **Validation.** The split values reproduce the text. At γ=80 the frozen map gives x=0.9659, and self-consistent calibration gives 0.9655 (the text says 0.9656). The split σ_in is 0.29872. At the merged state σ_in=0.29924, against the text's learned-null value of 0.29916 (`chk07:39`).
- **Result on the merged branch.** At γ=80 the effective mismatch coefficient is (σ_× − σ_in)/(1 − cos φ) = 0.157, against the frozen D_cal=1.241. The mechanism is the one `prop:frm-own-data`'s discussion names: senders that fuse counter-rotated messages carry a rotated cross moment (b≠0).
- **Merged fixed points** (attention P, bias fraction x):

| γ | frozen map | self-consistent |
|---|---|---|
| 40 | (0.395, 0.113) | (0.425, 0.106) |
| 80 | (0.344, 0.127) | (0.421, 0.107) |
| 105 | merged branch ends (fold at 105.9) | (0.418, 0.107) |
| 150 | no merged point | (0.413, 0.109) |
| 242 | no merged point | (0.401, 0.111) |
| 300 | no merged point | (0.393, 0.113) |
| 350 | no merged point | (0.384, 0.116) |
| 400 | — | iteration fell to the split; existence there not settled |

- **Stability checked only partly.** With calibration held at its self-consistent value, the symmetric multiplier at γ=150 is 0.957. The symmetry-breaking multiplier and calibration feedback were not computed.
- **Consequence.** The bistable window, the merged-branch stability boundary and the "single attracting fixed point above γ_T" are properties of the frozen map only. The self-consistent map has a symmetric merged fixed point at least up to γ=350. In effect, open:frm-self-consistent has a negative answer at the base point. The theorem as stated (about the frozen map) remains correct.
- **Side observation, not settled.** The full simulation at γ=40 (0.392, 0.116) matches the frozen map better than the self-consistent one. This suggests the stochastic runs used frozen split constants plus D_cal(1−cos φ). A separate codebase, `ActInf_1.0/src/actinf/formation.py:3-5`, has exactly such a "frozen_split" mode, but I could not confirm that the manuscript's runs used it.
- **Minimal fix** (append after `07_formation.tex:111`): "Off the split it is not: on the merged branch at the base point the model's own calibration corresponds to a mismatch coefficient of about 0.16 rather than D_cal=1.24, because senders that fuse counter-rotated messages carry a rotated cross moment (see the discussion after prop:frm-own-data), and the symmetric merged fixed point of the self-consistent map persists beyond the fold at γ=105.9 and beyond γ_T. The thresholds, folds and stability boundaries reported below are properties of the frozen map."
- **Two related edits.** In obs:frm-stochastic, state which calibration the simulations use. In open:frm-closure, do not attribute the γ=80 merged-start gap solely to α. The self-consistent merged point (0.421, 0.107) is even farther from the simulation's (0.254, 0.569), so calibration does not explain the gap, but the map compared against is the frozen one.

**F2. CA item 3c: calibration-root uniqueness holds numerically and is unproved (minor; numerical; existence-only proof acknowledged).**
- **Location.** `app07_formation.tex` proof of thm:frm-split-contrast(d) (intermediate value theorem, existence only). The definite article appears at `07_formation.tex:173` ("its own calibration fixed point") and in `lem:frm-calibration` ("The in-group value … is a fixed point").
- **What already handles it.** Part (e) is local-branch only and is correct without uniqueness. `chk07:31` reports a single root on the 162-point grid.
- **My closed-form check (lem:frm-split-law).** It reproduces the base root 0.2987168. Over 20,000 random points × {split, comparison medium}, with ranges given in section (3), I found exactly one sign change of Ψ_cal on a 6000-point log grid in every case. An adversarial Nelder–Mead search (400 starts) for the largest dMSE/dσ found 2.0e-3, far below 1. Uniqueness holds wherever Ψ' = MSE' − 1 < 0, so all evidence says the root is unique.
- **Not obtained.** A proof that MSE'(σ) < 1 on (R_c, ∞).
- **Minimal fix.** Add to (d): "Uniqueness is not proved; on the grid of obs:frm-grid and on random parameter samples a single root was found, with dMSE/dσ well below one."

**F3. MA item 8: (F4) grading across chapters (corrected; minor-to-major; partly new).**
- **Not a misapplication.** `inh:protocol-classes(P)` (`MA/05_inheritance.tex:811-822`) requires B_I to contain every protocol of A_J for the merged blocks, applied before the handoff. Removing a pre-handoff probe at the handoff is therefore built into (P) for every construction.
  - Ch. 10 declares no B_I explicitly (`10_boundary_closure.tex:4`). Its (F4) witness is the pre-join child responses (`:280`), which are the minimal mandated B_I, so (F4) holds there.
  - Ch. 12 (`12_open_formation.tex:530`) and ch. 13 (`13_per_agent_inheritance.tex:358`) each apply (F4) correctly to their own declarations.
- **The real asymmetry.** Ch. 12's singleton query comes from an external querier "in a fixed angular frame that no agent holds" (`12_open_formation.tex:413`). Thm open:formation(b) says no element of A_pop resolves the discarded distinction at any time. Ch. 13 declines the analogous hidden-angle query because "no agent … reads the hidden angle", and calls the device "deleting a probe at the handoff".
- **Consequence.** Under an agent-readable probe rule, ch. 12's (F4) would fail, as ch. 13's does. Neither chapter cross-references the other.
- **Minimal fix.** At `12:530`, after "(F4) holds": "this rests on the external querier of open:response; with B_I restricted to probes that some agent can apply, (F4) fails here as in ch:per-agent". At `13:358`, cite ch. 12 as the construction that declares such a rule. At `10:4`, name B_I as the pre-join fresh-descendant responses of the children.

**F4. CA item 1: contrast scope (confirmed and acknowledged; partly corrected; not an error).**
- **Non-reciprocal attention.** Acknowledged at `04_collectives.tex:180` and `s04_collectives.tex:267-269` (open:col-non-diffusive).
- **Exact fusion.** Acknowledged at `s04:271-273` (open:col-exact-fusion).
- **Records (corrected).** Contrast is defined with record nodes included whenever the precision is diffusive (def:col-contrast, "records included"; `s04:131`). It fails only for noisy records that break diffusivity, and that case falls under the open problem.
- **Galerkin.** Acknowledged with error control: `10c_renormalization.tex:38`, and thm:ren-closure(a),(f) at `:196,201` bound the exact law's departure from the Galerkin precision by 𝒟.
- **Fix.** None needed.

**F5. CA item 2: declared geometry and baselines (geometry part confirmed; "uncertifiable" partly refuted; acknowledged).**
- **Geometry.** Dependence on the declared geometry is a stated design choice (rem:col-declared-geometry, `s04:147`).
- **Finite closed populations.** Baselines are computed by exhaustive enumeration: 247, 4083 and 65519 regions (`chk04:53,98`; `chk07:35`). These are certified up to floating point, not "uncertifiable".
- **What remains open.** Only baselines on infinite lattices and large boxes, where the bracket method does not close (`chk04:83`, 12×3 box), as stated in open:col-extent (`s04:285`). The ext2 medium is "not an instance of that clause" (`ext2_rfm.tex:147`), also stated.
- **Fix.** None needed.

**F6. CA items 3b and 3d: learning input off the split; stochastic-to-mean-field step (confirmed and acknowledged).**
- **3b.** The discussion after prop:frm-own-data says "an idealization that the proposition does not support". It is also an open problem at `07_formation.tex:301`.
- **3d.** open:frm-closure (`07_formation.tex:296-298`).

**F7. Further confirmed and acknowledged items.**
- **CA item 4.** H5a is disconnected from contrast selection, as rem:met-no-selection (`10a_meta_agents.tex:271-273`) states explicitly. The bounds' looseness is reported in the text: 10³ to 8×10³ (`ext1_apx.tex:125`), "three orders" (`:828`), and median factors 3×10⁶ and 7×10¹¹ far from closure (`chkext1_apx.tex:39`).
- **CA item 5.** The H5c sensing objective is "declare[d] … and claim no more" (`s10d_environments.tex:36`; rem:env-efe-horizon-free and rem:env-two-step show that the one-step EFE can oppose it).
- **MA item 9.** "The known-code hypothesis is essential" (`17_communication_links.tex:158`). it2:dictionary-exchange (`18_link_dynamics.tex:58-61`) states that λ>0 needs communication "between agents that no edge of ℰ joins", lists the results it governs, and defers the protocol to it2:open-messages.
- **MA item 11.** open:constants (`12_open_formation.tex` remark after open:null-control): "The witness is nonconstructive." The verdicts on (F2), (F5) and (F6b) are stated as undetermined (`:530`).
- **CA item 12.** `ext8_idn.tex:97`: "The grade of def:agy-meta-agent is accordingly not a functional of the recorded law."

### (2) Not settled
- An analytic proof of calibration-root uniqueness (MSE'(σ) < 1).
- For F1: whether the self-consistent merged point is stable in the symmetry-breaking direction and with calibration feedback; where the self-consistent merged branch ends (somewhere between γ=350 and 400 in my iteration); and which calibration the manuscript's stochastic runs used.
- For F1: I held the claimed prior variance at its expected fixed point, as the frozen-slow model does, rather than letting it vary round by round.

### (3) Commands run and deciding outputs
All runs used bare `python`, single-threaded. Scripts are in `C:/Users/CHRISA~1/AppData/Local/Temp/claude/63c81c17e87f0010/34faeca5-ea90-45d1-8cc4-412bdf898c58/scratchpad/inv_t2/`.
- **`calroot.py`** (random F∈(0.01, 0.9999); Q, R^s, R_c log-uniform over 10^-3..10^2, 10^-3..10^3, 10^-4..10^3; n=2..20; κ=1..n−1). Output: `base root 0.2987167966546719`; `cases with !=1 root: 0`.
- **`calroot2.py`** (adversarial search). Output: `max dMSE/dsigma found: 0.00205`.
- **`merged.py`** (base point):
  - `gamma=80: frozen x=0.9659 | selfcons x=0.9655 sig_in=0.29897 Dcal(eff)=1.2338`
  - `gamma=80 merged: frozen x=0.1274 P=0.3442 | selfcons x=0.1067 P=0.4206 Dcal(eff)=0.1566`
  - `gamma=40: frozen x=0.1129 P=0.3948 | selfcons x=0.1058 P=0.4247`
- **`merged3.py`, `merged4.py`:**
  - `110/150 frozen from 0.11 -> x=0.998/1.000` (split only)
  - `selfcons merged: 105 x=0.107, 150 x=0.109, 242 x=0.111, 300 x=0.113, 350 x=0.116; 400 -> split`
  - `g'(x*) at gamma=150 = 0.957`
- **Reads.** `sed`/`grep` over the CA sections (04, s04, 07, s07, app07, chk07, 10a, 10c, 10d, s10d, ext1, chkext1, ext8) and the MA chapters (05_inheritance, 10, 12, 13, 14, 17, 18).


## Investigator: coverage-and-unification

# Investigator 3: coverage sweep (A) and unification obligations 1, 2 and 4 (B)

**Verdicts.**
- **Part A:** the grep sweep found no stale theorem-level claims in the unread files. It found one stale piece of wording: the 0.2 percent pitchfork framing in MA companion c18. The sweep is not a full audit of those files.
- **Part B1:** refuted as stated. CA's exact fusion is the per-agent fixed-model free-energy posterior under the true conditional likelihood. It is not, in general, the agent's block of a global posterior. Mean messages and posterior-sample messages have identical cross-covariances and differ only in variance. The comparison report's reading of `imem:scalar-calibration` is wrong.
- **Part B2:** exact in a restricted sense. With F=I and Q=0, the conditional-mean level-0 step is exactly one explicit-Euler step (h=1) of MA's frozen-covariance, frozen-source per-agent Gaussian mean flow. Six differences are listed below; one of them is that CA's light cone is an artifact of the discrete step.
- **Part B4:** contrast is invariant under the covariant embedded frame action. It is not invariant under an action that leaves a reference object fixed, which is the same mechanism as `ext2_rfm.tex:113-120`.

## 1. Findings, ranked

### F1 (major, new). B2: level-0 is explicit Euler of MA's per-agent mean flow, under stated restrictions

**Status:** the identity is proved; the numerical check is computed.

**Location:** CA `sections/02_framework.tex:313-330` (def:fw-level0). MA `chapters/03_dynamics.tex:260` (eq:dyn-gaussian-flow), `:402` (per-agent class), `:517` (cor:dyn-frozen-source), `:572` (thm:dyn-three-limits(iii)).

**Derivation.**
- Take receiver i with claimed prior covariance P_i, sensing (H^s_i, R^s_i), and code models Ĥ_ij with assigned noises R̂_ij. Assume these noises are independent across the sensor and the senders, which is level-0's "channel noise specific to the receiver".
- Set P_i^+ = (P_i^{-1} + H^sᵀR^{s-1}H^s + Σ_j Ĥ_ijᵀR̂_ij^{-1}Ĥ_ij)^{-1}.
- The joint gain has the information form: K^s_i = P_i^+H^sᵀR^{s-1} and K_ij = P_i^+Ĥ_ijᵀR̂_ij^{-1}.
- Let Φ_i(x) = ½|s_i − H^s x|²_{R^{s-1}} + Σ_j ½|y_ij − Ĥ_ij x|²_{R̂_ij^{-1}}. Then CA's update is m_i^+ = m_i − P_i^+ ∇Φ_i(m_i). This is one explicit-Euler step, of size h=1, of the Gaussian Fisher flow μ̇ = −Σ∇_μ with Σ_i = P_i^+ frozen.
- The same step is also an implicit-Euler step in the prior metric P_i. That is the proximal form of the Kalman update.
- Now set F=I and Q=0, and average over the local noises v and ν given η. The drift is the gradient of the record term at η plus the coded peer cost ½|Ĥ_ij x − H_j m_j|² weighted by R̂^{-1}.
  - At level 1, R̂ = R_c + H_jP_jH_jᵀ. This weight is the mean part of KL(Ĥ_#q_i ‖ (H_j)_#q_j ∗ N(0,R_c)).
  - At R_c=0 it is the mean part of CA's own E_ij (lem:fw-reception-identity(b)).
- **Classification:** CA's literal receivers implement the per-agent picture with frozen sources. They do not implement the reciprocal potential, because the source-side gradient terms ∂E_ki/∂m_i are absent.
- In the scalar case, any nonnegative gains can be represented this way: k^s_i = h, k_ij = hβ̃_ij, and every anchor a_i = η. In the vector case, Σ_i^{-1}K_ijĤ_ij must be symmetric PSD; Kalman-form gains satisfy this automatically.

**Differences that remain.**
- (i) The covariance is frozen. MA evolves Σ by Σ̇ = −2Σ∇_ΣΣ. With F=I and Q=0, CA's fixed claimed gains are not the Riccati gains, which tend to 0.
- (ii) Fixed points coincide exactly, but stability differs:
  - The map needs ρ(W)<1; the ODE needs Re spec(W)<1.
  - CA's condition is strictly stronger.
- (iii) **Light cone.** (Wⁿ)_ij=0 beyond graph distance n, while e^{−t(I−W)} has full support on each connected component for every t>0. CA's strict light cone (thm:sca-lightcone) therefore has no exact counterpart in MA's flow.
- (iv) **Noise.** CA injects O(1) noise every step. This is not an Euler–Maruyama discretization of an SDE with an h→0 limit. MA's flow is deterministic on laws, so it has no object corresponding to CA's world-conditional error covariance, on which contrast is defined.
- (v) **Self-anchor.** CA's self-anchor is a fresh sensing record each round. MA's is a fixed evaluator. They agree only in conditional mean.
- (vi) **F≠I.** The step is m ↦ F(m − P^+∇Φ), a splitting of a prediction step and a gradient step. The rotational part of F is not a Fisher gradient. Any MA reading here is interpretive.

**Next step:** state this as a proposition in CA's ext or s02, citing MA thm:dyn-three-limits(iii).

### F2 (major, new). B1: exact fusion and a global free energy with a world latent

**Location:** CA `02_framework.tex:135-153` (def:fw-levels, eq:fw-track) and `:154-166` (prop:fw-level-optimality(d)). MA `03_dynamics.tex:321` (eq:dyn-fixed-vfe) and `:333-345` (prop:dyn-global-local).

**(a) Proved.** Let Π be the true joint law of η and all data. Then q_i^ex = Π(η | Z_i, y_ij). This is the unique minimizer of the fixed-model free energy KL(Q‖Π(η|Z_i)) − E_Q log p(y_ij | η, Z_i), by eq:dyn-fixed-vfe. So exact fusion is a correctly specified per-agent free energy. It is a family of conditionals of one joint law, each on a different σ-algebra.

**(b) Refuted** as "the posterior of a global VFE". MA's global posterior Π_o conditions on all records, so its η-marginal equals q_i^ex if and only if σ(Z_i, y_ij) is sufficient for η relative to all records. Counterexample: a rank-deficient code (r_c<K) together with a private source of j in ker H_j. Product-recognition copy models of the M_n type do not repair this: in the two-agent scalar case, (I+L_W)^{-1}a reaches the exact-fusion mean (a₁+a₂)/2 only as β→∞.

**(c) Proved; Monte Carlo agrees.** Mean messages versus posterior-sample messages. Let ξ_j = m_j + ζ_j with ζ_j ~ N(0,P_j) independent of everything else.
- Then Cov(ξ_j, X) = Cov(m_j, X) for every X built from η and the data.
- Hence A_ij and the offset H_jΣ_jiΣ_ii^{-1}m_i in eq:fw-track are unchanged.
- The only change is R^ex_ij → R^ex_ij + H_jP_jH_jᵀ.

**Report error (minor, new).** The comparison report §5 item 1 says `imem:scalar-calibration` (MA `appendices/interacting_memory.tex:555`) shows mean and sample messages differ in cross-covariance. They do not. That equation compares a sample message with a direct sensor of Y₁ at equal marginal variance. In MA's own notation, mean and sample messages share Cov(X₀,H) = aS.

**Open:** whether a network of exact fusers is mean-field coordinate descent of one global Gaussian. Read as an analogy, the scalar mean-slice analogue is MA thm(iv)'s reversibility condition. This is not proved.

### F3 (major, new). B4: is contrast invariant under the frame action?

**Location:** CA `04_collectives.tex:182-188` (def:col-contrast), `ext2_rfm.tex:113-120` (prop:rfm-representation), `02_framework.tex:270-283`.

**Proved.** Contrast is computed from world-coordinate errors e_i = m_i − η. Under the covariant action, U_i ↦ g_iU_i, Θ_ij ↦ g_iΘ_ijg_j^{-1}, μ_i ↦ g_iμ_i:
- m_i, the mistranslation Υ_ij = U_i^{-1}Θ_ijU_j, the effective code H_j and the code model Ĥ_ij are all unchanged, provided T_cg_j = T_c.
- Therefore W, B^mis, Q^ζ, Π^c and r(C) are invariant under ∏_j Stab(T_c).
- For g_j outside the stabilizer, the shared-language hypothesis T̄^c = T_c breaks, so the action leaves CA's model class.

**Not invariant.** Take the active action: frames move while translations, or the default α̂⁰ of ext2, stay fixed. With planar rotations this gives Υ_ij ↦ Rot(δ_j − δ_i)Υ_ij, hence W ↦ D*WD and Σ ↦ D*ΣD.
- (i) D*(Σ^sc⊗I)D is generally not of Kronecker form, so def:col-contrast is then undefined.
- (ii) ξ_out uses the untwisted average 1_C. A gauge-covariant contrast would need the average to transform with the frames.

**What ext2 implies (proved there, not rechecked by me).** In ext2:113-120, the formation event is representation-dependent unless the default transforms as α̂⁰ ↦ α̂⁰ + δ_c − δ_d. For example, δ_c = −θ_c gives no event at any γ. So the contrast of the outcome depends on representation through the non-equivariant dynamics, not through the definition of r. Part (c) of that proposition confirms that recoding an aggregate leaves contrast unchanged.

**Smallest fix:**
- State the stabilizer invariance next to def:col-contrast.
- State that representation independence of formation requires a covariant default, as MA's transported references do in eq:int-reference-equivariance.

### F4 (minor, new). MA companion c18 keeps the 0.2 percent framing

**Location:** `MAgent_Theory_2.0/companion/c18_link_dynamics.tex:383`. It reads: "the response term exceeds 32T_c by less than 0.2 percent and reverses the classification".

**Status:** computed with exact rationals.
- R − 32T_c = 0.01836, which is 0.177 percent. That arithmetic is correct.
- The reversal, however, is decided by R against the straight-line value: SL − R = 6c exactly, equal to −0.6339, which is 6.1 percent of R.
- The chapter was corrected in commit 34b8bb2 (`chapters/18_link_dynamics.tex:630`).

**Fix:** copy the chapter's sentence. Also, c18:394 still says "float64 continuation … c≈+0.023", while the chapter now says "40 significant digits … +0.0229".

### F5 (minor, new). Coverage sweep results

**Grep:** first-event, (F5), one-stage, selection stage, 0.2/percent/pitchfork, primary objective, no global, common code, coh-walls and sca-common.

**Corpus:** MA companion/*, supplements/*, Item_1/2/3, and CA ext3/4/6/7 with their app and chk files.

**Hits:**
- No restatement of the old gf:first-event corollary.
- No "no objective primary" claim. The companion glossary:20 and c03/c11 are consistent with the corrected README.
- No common-code or coh-walls claim. CA ext3/4/6/7 cite none of conj:sca-common-code, conj:coh-walls or prop:min-common-code.
- Items 1, 2 and 3 carry "superseded by the main chapter" status lines, so any stale content there is already disclaimed.
- glossary:42 ("single-stage selection … recursion clause fails") concerns (F6) and is correct.

### F6 (minor). CA ext6 checks

**Computed:** thm:nrg-ep (`ext6_nrg.tex:25-31`). The values tr(Q⁻¹JAᵀ), the two-term form and a direct D₁ agree to 1e-14 on the ring (25/27) and on three random 4×4 instances. The ring pair rate D_n/n (0.341, 0.344, 0.345 at n=16, 32, 64) is consistent with "about 0.35".

**Acknowledged open, possibly stale:** obs:nrg-spectral (`:72-75`) still says "not proved". `Collective_Agents/docs/research/problem_8.md` claims a self-reviewed proof of open:nrg-rate. That proof is not adopted and not verified by me.

## 2. What I could not settle

- **No full audit.** I did not do a line-by-line Tier 1/2 mathematical audit of CA ext3_obj, ext4_prv or ext7_evo and their appendices. I read only ext7's statements (prop:evo-transmission, thm:evo-record-channel) and found no defect. I checked one inequality by hand: in thm:evo-record-channel(e), the coefficient is at most h₀ because ε+β+g ≥ ε+g(1−f).
- **MA supplements s01–s04** were checked only by grep.
- **B1 network question:** whether coupled exact fusers form a global mean-field descent is open.
- **B2 with F≠I:** no MA counterpart exists. The splitting reading is interpretive.
- **B4 for record nodes and exact fusion:** contrast is undefined there (Tier 2.1), so no invariance statement is possible.

## 3. Commands run and the outputs that decide

Scripts are in `C:/Users/CHRISA~1/AppData/Local/Temp/claude/63c81c17e87f0010/34faeca5-ea90-45d1-8cc4-412bdf898c58/scratchpad/inv3/`. All ran single-threaded under bare python.

- **`chk.py`**
  - Information-form gain error: 5.6e-16.
  - Kalman step equals explicit Euler with metric P⁺: error 5.3e-16.
  - Monte Carlo with N=4e5, mean versus sample messages:
    - Cov(η,y_m) = (−0.584, −0.179, 0.545) against Cov(η,y_s) = (−0.585, −0.179, 0.546).
    - Cov(m_i,·) also agrees.
    - Var difference 0.2305 against H P_j Hᵀ = 0.2279 (sampling error).
- **`nrg.py`:** the ep formulas equal D₁ (0.925926 = 25/27; 3.02857; 36.9827; 10.7822). Ring pair D_n/n = 0.3411, 0.3439, 0.3453.
- **Exact-fraction one-liner** on the c18 constants:
  - A+4Δ = −0.6156; 32T_c = 10.3388; R = 10.3572.
  - (R − 32T_c)/R = 0.00177; (R − SL)/R = 0.0612.
  - SL − R == 6c is True.
- **Greps** as listed in F5. **git:** `git show a842652` and `git show 34b8bb2`, to confirm the chapter fixes and that the companion was untouched.
