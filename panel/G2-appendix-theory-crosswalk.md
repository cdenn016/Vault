# G2: Appendix-to-Theory crosswalk for a physics-journal PIFB2

**Lens:** G2, program architect: which appendix material stays in a physics-journal PIFB2 and which becomes a citation to the Theory manuscript.
**Model:** Claude Opus 5.5 (`claude-opus-5-5`), investigator. No adjudication was run.
**Target:** `Research/manuscripts/PIFB2.tex` (bytes per BRIEF). The Theory was read at the Desktop checkout, HEAD `45ef312`. `git diff --stat 5f643dc 45ef312 -- Theory` is empty, so the Theory tree is byte-identical to the brief's `5f643dc`.

**Lines read (PIFB2):** 2212-2515 (App. A) in full; 2592-3161 (C, D, E, F) in full; 3413-3941 (H, I) in full, with long lines printed whole via `sed | fold`. I grepped the whole file for `\ref` targets into these appendices.

**Lines read (Theory):** c03 436-575; c04 207-255; c05 649-888; c06 1-215, 357-400, 560-880; c07 112-139; c08 108-152; c09 125-240, 370-492; c10 297-418; c11 47-160, 580-770; c12 42-70, 221-340, 700-760; c13 203-236; g02 226-290; g03 31-76; g04 60-140; g05 40-236; g07 182-240, 455-482, 561-600; g09 39-125; g10 212-300; SPEC.md 1-40. I also built a full index of all 705 Theory claim headings (`\*heading{title}{label}`) in c*, g* and b* files and grepped it for every counterpart named below. Every Theory label cited here was confirmed to exist.

**Prior panel reports consulted, so their findings are not repeated:** L03-1, L03-9, L04-9, L05 (verified list), L06-1 to L06-10, L07-6, L10-1, L10 (verified list), L17-4, L17-8, L18-11 (node table), L19-1 (division-of-labor table). Also C1-pifb2-program-alignment.md, nodes N6, N15 and N21.

**Executed (bare `python`, CPython 3.14.4, NumPy/SciPy, all float64, each script under 3 s):**
- `scripts/G2_repr_crosswalk.py` covers the Appendix F identity, the normalized pairwise joint versus the geometric pool, and the τ-map of the reduced Hessian.
- `scripts/G2_appD_crosswalk.py` covers the entropy weight of the App. D functional, the Theory block optimum, the homogeneous contrast, and the App. E fixed-W form.
- `scripts/G2_rg_crosswalk.py` covers the pushforward crosswalk, Schur closure, the functoriality witness, the aggregation semigroup, and nested VFE against the tower VFE.

## Findings

### G2-1: Appendix I restates in weaker form what the Theory proves; most of its theorem block should become citations, but three items must stay

**Location:** PIFB2.tex:3569-3941. Labels: `eq:rg_exact_free_energy` (3637), `thm:rg_pushforward` (3776), `thm:rg_semigroup` (3785), `thm:rg_exact_closure` (3820), `thm:rg_residual` (3882), `thm:rg_residual_explicit` (3896), `thm:rg_detector_retention` (3920). Also `thm:belief_configuration_gibbs_lift` (3578), `thm:rg_covariance` (3806), `eq:rg_reduced_hessian` (3678).

**Severity:** high. Appendix I is 6,884 words, the largest appendix, and it is cited from the body nine times as `app:rigorous_rg` (1535-1863).

**Evidence:**
1. *Pushforward.* The Theory's conditional-partition formula (c11 `def:rg-measure-pair`, `thm:rg-effective-action`) is stated for any Markov kernel. It pushes a probability reference together with the evidence measure, preserves total mass (`prop:rg-measure-pair-composition`), and composes along a tower. PIFB2 instead picks a separate parent reference ν_{s+1} and a coarea density. `G2_rg_crosswalk.py` (1) sets x∈R², ν_s=N(0,I), a quadratic-plus-linear F, T_cfg=0.7 and R(x)=mean. It confirms F_{s+1}(z) = T·H^c(z) − T·log(dν^c/dν_{s+1})(z), where H^c = −log E_ν[e^{−F/T} | Z=z] and ν^c = R_#ν_s = N(0,1/2). The residual is 8.9e-16 over five z, and Z_s = Z_{s+1} = 0.480421025322 exactly. So PIFB2's renormalized energy is the Theory's effective action plus a reference-change term. That term exists only because ν_{s+1} was chosen independently. The coarea machinery, and the sentence behind registered item (b) (ledger), both disappear when the Theory's pushed reference is used.
2. *Functoriality.* `thm:rg_semigroup` is the chain case of c09 `prop:rg-scale-functoriality` (i), where "the composition law imposes no condition". The Theory also gives the case with content: non-chain posets, with the majority witness. `G2_rg_crosswalk.py` (3) reproduces that witness: pairs then triple gives 1, triples then pair gives 0. PIFB2's following remark says a coupling-space semigroup "is not established here". The Theory establishes one for Galerkin aggregation on the Gaussian interaction family (g09 `prop:grg-aggregation-semigroup`, g07 `prop:cg-gaussian-aggregation`). Script (4) confirms that the coarse blocks stay in the family and that A_{S2}A_{S1} = A_{S1S2} (3.6e-15). Aggregation is conditioning on zero internal disagreement (g07 `prop:cg-aggregation-conditioning`), not marginalization, and Kron marginalization leaves the family (g07 `prop:cg-kron-leaves-family`).
3. *Exact closure.* The constant-block case of `thm:rg_exact_closure`, with `eq:rg_app_schur_complement`, is g07 `prop:cg-normalized-schur-action`, and the Theory version also carries the source and the constant. Script (2) confirms −log∫e^{−E}dξ = ½Λ_eff x² − h_eff x + c_eff (5.8e-15). The Y-dependent (A6) case has no Theory counterpart; L06-2 treats its content.
4. *Residual and detector.* The Theory has no schematic closure bound. It has an exact residual identity (c11 `def:rg-retained-projection`, `prop:rg-interaction-residual`), generic hyperedge generation (`prop:rg-hyperedge-generation`), and the finite-network obstruction (`prop:rg-interaction-finite-network-obstruction`). It has no detector theorem. c09 `open:cg-natural-selector` records that no cost analyzed so far selects a partition, and `thm:cg-evidence-preserving-channel` records that the coarse ELBO rise is discarded information, "neither model improvement nor evidence ascent" (L18-2 draws the consequence for the licensing criterion).
5. *Holonomy residual.* PIFB2's group-level spread H_IJ (Karcher mean of Θ^{IJ}_{ij}) has a law-level replacement in c10 `thm:cg-holonomy-kl-marginal` and `prop:cg-holonomy-compact-closed-form`. For noncompact GL links with generic loop holonomy, `cor:cg-holonomy-noncompact-gaussian` shows that no Gaussian parent is admissible. L06-3 shows H_IJ is trivial in App. I's own state space; the Theory result is what a Regime II version needs.
6. *Items with no Theory replacement.* `thm:belief_configuration_gibbs_lift` is PIFB2's own (see G2-7). `thm:rg_covariance` verifies, for the Karcher and barycenter map, the equivariance that c09 `prop:cg-equivariant-channels` takes as a hypothesis. `eq:rg_reduced_hessian` is c06 `prop:obs-attention-reduced-hessian` after multiplying by τ (script `G2_repr_crosswalk.py` (3), 2.9e-9 by finite differences); the ledger already records it as a Schur complement.

**Fix:** In the physics-journal version, cut the following to one paragraph that cites the Theory: the coarea display, Actions (a)/(b), `thm:rg_pushforward`, `thm:rg_semigroup`, the constant-block part of `thm:rg_exact_closure`, the H_IJ paragraph and the finite-size-scaling paragraph. Move `ass:closure_regime`, `thm:rg_residual`, `thm:rg_residual_explicit`, `thm:rg_detector_retention` and the Fenichel paragraph to the online supplement, or cut them. Keep, in about 900 words:
- `thm:belief_configuration_gibbs_lift` and its remark;
- `thm:rg_covariance`, stated at one base point for one global g (c02 `prop:geo-active-image-point`) with its scope fixed per L06-10;
- the Laplace display `eq:rg_laplace` with the coupling-shift sentence of L06-6.

Suggested replacement for the exact-pushforward paragraph: "Any Markov coarse channel C acting on a proper reference probability ϱ and on the evidence measure e^{−F/T_cfg}ϱ defines an effective energy through the conditional partition function, −log E_ϱ[e^{−F/T_cfg} | Z]. It preserves the partition function and every retained observable, and it composes along any chain of resolutions [DennisTheory, Ch. 11, Theorem 'Conditional-partition formula and composition']. We use this form throughout; it needs no coarea density and no separately chosen parent reference."

**Falsifies:** A Theory statement that fails to cover the deterministic-map, proper-reference case of `eq:rg_exact_free_energy`, which script (1) instantiates. Or a body claim of PIFB2 that uses the (A6) Y-dependent closure or the explicit constants, which would force them to stay.

**Status:** The PIFB2 items are P as stated (L06 verified list). They are weaker than, or special cases of, ESTABLISHED Theory statements. No inflation beyond what L06 already records.

### G2-2: The Theory has no replacement for the representation theorem; it declares the transported KL rather than deriving it, and what it can supply is a normalized-model statement about a different object

**Location:** PIFB2.tex:2956-3161 (`thm:representation_app` 3039, `eq:geometric_mean_target_app` 3048, `cor:closure_forces_kl` 3058, `lem:richness_app` 3120). Cited from 594, 2893, 2970, 3069 and 3160.

**Severity:** medium.

**Evidence:**
1. *The Theory declares the divergence.* The Theory defines the transported divergence KL(q_i‖(Θ_e)_#q_j) (c12 `def:full-graph-transported-divergences`) and the role divergence (c06 `eq:obs-selective-role-divergence` in `def:obs-selective-comparison`) by declaration. The softmax result (`cor:obs-selective-softmax`, `prop:full-graph-gibbs-rows`) holds for any fixed energies. c03 `prop:prob-law-point-energy` shows that such a law-point divergence is not the expectation of any sample energy. A grep of c*, g* and b* for f-divergence, argument-order and direction language finds no statement that selects KL or its direction for this object. The only KL direction the Theory derives is KL(Q‖Π) in the evidence bound (c05 `thm:elbo-exact-identity`). So the C1 program review's N6 entry, "Not needed once the source-label joint fixes the divergence", and L03-1's alternative fix ("anchor the KL direction on the Theory's source-label joint") overstate the Theory. The source-label joint fixes the row form. It does not fix the divergence.
2. *What the Theory can supply is about a different object.* In a normalized joint the exact block E-coordinate (c05 `prop:elbo-exact-e-coordinate` (iii); c12 `rem:full-graph-inference-loop`; Gaussian case g04 `thm:restrict-exact-block-optimum`, `eq:restrict-cavi-mean`) is log-linear in the factors with unit exponents (a product of experts). The agent's appearance in its neighbors' factors is included automatically, which answers the sender-row gap of L03-1 for that object. `G2_repr_crosswalk.py` (2) takes L03-1's priors p1=N(0,1) and p2=N(3,0.25) with a normalized pair factor e^{−(k1−k2)²/2}. The CAVI means equal the exact posterior mean (4.4e-16), the variances are 1/(A_i+w) (unit exponents), and the gradient of the joint negative ELBO at the fixed point is 2.5e-10 in all four coordinates. c06 `prop:obs-selective-receiver-update` gives the exact receiver update for the comparison-record model.
3. *The forward half of Theorem F is one exact identity.* KL(q‖p) + Σ_j β_j KL(q‖r_j) = (1+B)·KL(q‖g) − (1+B)·log Z_g, where g ∝ p^{1/(1+B)} Π r_j^{β_j/(1+B)}. `G2_repr_crosswalk.py` (1) confirms it by quadrature with random Gaussians and a non-optimal q; the maximum residual is 8.9e-16. The 1/(1+B) exponents are the reciprocal of the entropy weight (see G2-3).

**Fix:** Keep the theorem, scoped to the frozen-neighbor best response as L03-1 requires. Condense App. F to about 600 words: the identity above as a displayed lemma (it proves Step 2 and the dual-cost line at once), the scoped theorem statement, and one paragraph on opinion pooling (per L03-8). Move `lem:richness_app`, `cor:closure_forces_kl`, `rem:analyticity_role` and the proof of the converse to the supplement. Add after the statement: "The companion theory [DennisTheory] declares this transported divergence rather than deriving it. In a normalized joint the analogous coordinate update is a product of the prior and pair factors with unit exponents, and its stationarity includes each agent's appearance in its neighbors' factors [DennisTheory, Ch. 5, 'Local Gibbs bound and the exact block E-coordinate']. The present theorem characterizes the choice only for the frozen-neighbor best response." Do not claim that the Theory fixes the divergence.

**Falsifies:** A Theory statement that selects KL(q_i‖Θ_#q_j) among divergences, or that derives its argument order, for law-point energies.

**Status:** Theorem F is P for the receiver-only problem (L03-1). The phrase "pinned" is S beyond that scope. The C1 N6 claim about the Theory is unsupported.

### G2-3: The ½ in App. D and the 1/(1+B) in App. F share one origin: the consensus potential equilibrates each belief at temperature 1+B_i relative to Bayesian updating

**Location:** PIFB2.tex:2718-2795 (`eq:sigma_fixed_point_beta` 2746, `eq:sigma_fixed_point_map` 2755, the unlabeled proposition at 2759, the homogeneous limit 2770-2795), 2885-2890 (collapse to message passing), 2892-2945 (App. E), and 3048.

**Severity:** medium.

**Evidence:**
1. *Where the factor comes from.* The receiver functional KL(q‖p) + Σ_j β_ij KL(q‖Ω_ij q_j) carries the belief entropy −½log det Σ_i with weight 1+B_i. Minimizing E_q[U] − (1+B)H(q) gives q ∝ e^{−U/(1+B)}, a Gibbs state at temperature 1+B in units where Bayesian updating has temperature 1. `G2_appD_crosswalk.py` (1) finds the minimizer at Σ = (1+B)M^{-1} with M = Σ_p^{-1} + Λ_o + Σ_j β_ij(Ω_ijΣ_jΩ_ij^T)^{-1}. The residuals are 2.5e-8 at B=1 (which is `eq:sigma_fixed_point_beta`) and 7.6e-9 at B=2.5. The geometric-mean exponents of G2-2 (3) are the same effect.
2. *The Theory's normalized counterpart.* For a normalized Gaussian joint in the interaction family (g03 `def:gauss-interaction-family`), the mean-field covariance is Λ_ii^{-1} = (A_i + Σ_j W_ij)^{-1} (g04 `thm:restrict-exact-block-optimum`; g02 `prop:gauss-conditional-precision`). It is reached in one step and contains no neighbor covariance, so there is no fixed-point problem. Script (2) confirms it by direct minimization of KL(Q‖P) over block-diagonal Gaussians with N=3 and K=2: covariance error 1.9e-8, mean error 4.7e-8.
3. *Homogeneous case.* PIFB2 finds Σ_∞ = Σ_0, "the equilibrium covariance reproduces the shared prior" (2795); script (3) reproduces this to 8.9e-16. A normalized two-agent joint with edge precision Σ_0^{-1} gives Σ_0/2 (4.4e-16), which is precision addition.
4. *Message passing.* The "no surviving covariance precision factor" of 2885-2890 differs from the exact receiver update of c06 `prop:obs-selective-receiver-update`, whose value map Σ_i^+S^{QT}W̃S^K keeps a gain below one.
5. *App. E.* With a fixed coupling W, the expected quadratic form is exactly the common-covariance KL plus a trace term (g05 `prop:ig-fixed-covariance-kl` with g03 `prop:gauss-interaction-energy-kernel`); script (4) agrees by Monte Carlo to relative 1.7e-3 at n = 4e5. The state-dependent Λ_ij of 2924 turns this into value-level matching; L03-9 covers the direction issue.

L07-6 and L10-1 (existence criterion ρ(L)<2, gauge dependence of the stated hypothesis) are not repeated here.

**Fix:**
- *App. D scope paragraph (2665).* Add: "The covariance fixed point below is a property of the consensus potential, which weights the belief entropy by 1+Σ_jβ_ij, so each belief is a Gibbs state at temperature 2 relative to Bayesian updating. In a normalized Gaussian joint the entropy enters once, and the mean-field covariance is the inverse diagonal precision block, fixed in one step and independent of the neighbors' covariances [DennisTheoryG, 'Block optimum']."
- *Homogeneous-limit conclusion (2795).* Replace with: "…reproduces the shared prior; this reflects the doubled entropy weight, and a normalized joint with the same coupling gives precision addition instead."
- *Placement.* Move App. D to the supplement (as L17-4). Cut App. E's KL identification and keep one sentence citing the fixed-W statement.

**Falsifies:** A normalized joint whose mean-field optimum reproduces `eq:sigma_fixed_point_beta` with the factor ½ while the entropy enters with weight one.

**Status:** The App. D algebra is D, and correct (L10 verified list). The physical reading of Σ_∞ = Σ_0 as the equilibrium of the population is S. It is presented without its source, the entropy weight.

### G2-4: Appendix H is orphaned, and only its nested bound has a Theory counterpart; "replace by citation" would delete the effective-action content rather than relocate it

**Location:** PIFB2.tex:3413-3568 (`sec:beyond_mean_field_gauge_vfe`, `thm:nested_state_configuration_vfe` 3445, `eq:beyond_mf_effective_action` 3532, `eq:beyond_mf_one_loop` 3552).

**Severity:** medium.

**Evidence:**
1. *Orphaned.* A grep for every label in 3413-3568 finds no `\ref` from outside App. H. The body never mentions "beyond mean field", "effective action", "one-loop" or "2PI".
2. *Nested bound.* `thm:nested_state_configuration_vfe` divided by T_cfg is the two-level case of c12 `def:full-graph-tower-vfe` with latent (X,Y). `G2_rg_crosswalk.py` (5) gives residual 0.0 on a finite model; L05 checked the identity itself.
3. *No Theory counterpart for the rest.* The Theory contains no Legendre-transform effective action, loop expansion, Bethe or Kikuchi region functional, or 2PI construction; a grep for Legendre, one-loop, 1PI, 2PI, irreducible, Bethe, Kikuchi and generating functional finds only unrelated hits. L17-4's disposition for H, "Replace by Theory citation (c12 `sec:full-graph-vfe-global`)", therefore covers only 3420-3471.
4. *Terminology collision.* H calls the Legendre transform Γ (1PI) the "effective action". The Theory's "effective action" H^c (c11 `thm:rg-effective-action`) is the Wilsonian conditional partition function, which is also what App. I's F_{s+1} is. A physics referee will read the two as one object unless they are named apart.
5. *What the one-loop term approximates.* The quantity approximated by `eq:beyond_mf_one_loop` at J=0 is −T_cfg log Z. Its exact value is the Theory's evidence identity M_o = ∫e^{−H^c}dϱ^c.

**Fix:** Replace App. H by a roughly 300-word Outlook paragraph in the discussion. It should:
- cite the Theory's tower free energy for the nested bound;
- keep the ordering "mean-field saddle, correlated family with one-loop correction, 2PI" as a proposed program;
- name Γ as "the one-particle-irreducible effective action" and F_{s+1} as "the Wilsonian effective energy".

Keep `rem:beyond_mf_no_double_counting` as one sentence; its content is c04 `rem:gen-appended-energy` and c05 `cor:obs-correlated-ledger`. The Gaussian block-precision family (3494-3501) can cite g04 `thm:restrict-determinant-gap`, whose exact price for the block-diagonal restriction is the dual total correlation (g04 `cor:restrict-gap-dual-total-correlation`).

**Falsifies:** A body argument that depends on `eq:beyond_mf_one_loop` or on the Bethe construction.

**Status:** The nested bound is P (L05). The effective-action tier is C (a proposal), and the text fences it correctly at 3556 and 3567.

### G2-5: Appendices A and C have Theory counterparts only for their standard content; the canonical gradient is a one-line consequence of a Theory lemma, so the surrogate machinery can go

**Location:** PIFB2.tex:2212-2515 (App. A), 2592-2661 (App. C).

**Severity:** low. L04-9 and L17-4/L17-8 cover the disposition; this finding adds the Theory targets.

**Evidence:**
1. *No Theory gradient appendix.* The Theory has none, and it excludes executables (SPEC section 0).
2. *What the Theory does supply:*
   - the envelope identity and the reduced slow natural-gradient flow (c08 `lem:obs-envelope-slow-flow`);
   - the reduced-row gradient ∇R_i = τ^{-1}Σ_jβ_ij∇E_ij and its Hessian (c06 `prop:obs-attention-reduced-hessian`);
   - the natural-gradient response to a quadratic disagreement (c06 `prop:obs-selective-response`);
   - the Gaussian KL derivatives (g04 `eq:restrict-derivatives`, equivalent to PIFB2 2260 and 2307);
   - the Fisher metric in the moment chart with its GL(n) affine isometry (g05 `prop:ig-fisher-moment-chart`), which is the gauge-covariance content of 2322-2328.
3. *Absent from the Theory:* the Fréchet derivatives of the matrix exponential, the transport-derivative formulas `eq:kl_omega_directional`/`eq:kl_omega_unconstrained`, the sender φ-gradients, the retraction, and the complexity count.
4. *App. C counterparts:* `app:variational_prelim` corresponds to c05 `thm:elbo-exact-identity`, `app:gaussian_kl` to g04 `eq:restrict-gaussian-kl`, and `app:fisher_gaussian` to g05 `prop:ig-fisher-moment-chart`. The SO(3) generators (historical, per 2639) and the Cholesky scheme have no counterpart.

**Fix:**
- *App. A.* Cut the entropy-suppressed surrogate subsections (2224-2290, 2293-2315, 2351-2426 and the surrogate half of 2428-2489). Keep about 700 words: the canonical envelope gradient in one line, citing the Theory lemma; the direct-KL receiver and sender gradients; and `eq:kl_omega_directional` with the SO(K) projection sentence. Move the retraction, Fréchet forms, complexity and fp32 paragraphs to the ML companion or code documentation.
- *App. C.* Keep the Gaussian KL and Fisher displays (about 400 words) with citations to g04 and g05. Cut 2637-2660.

**Falsifies:** A body claim whose support is the surrogate formula rather than the canonical gradient. By 2239 and 2493 there is none.

**Status:** App. A and App. C content is D, and correct (L04 and L10 verified lists).

### G2-6: `thm:rg_covariance` should stay, but at one base point it is a statement about one global g, and its holonomy-free scope should point to the Theory's law-level holonomy results

**Location:** PIFB2.tex:3641-3643 (Actions (a)/(b)), 3806-3815 (`thm:rg_covariance`).

**Severity:** low.

**Evidence:**
- *One global g.* At c_* the active gauge image is one copy of G (c02 `prop:geo-active-image-point`). The "base-local" map h(c) of Action (b), restricted to the single base point the brief's scope gate fixes, is therefore one global g.
- *Hypothesis versus verification.* The Theory's channel-level statement (c09 `prop:cg-equivariant-channels`) assumes kernel equivariance. PIFB2's theorem verifies it for the compact Karcher and M-projection map, which is the half the Theory lacks for this specific map. The barycenter half is g08 `prop:cg-gaussian-forward-kl-barycenter` and `cor:cg-compact-holonomy-barycenter`.
- *Holonomy.* With independent links, the relevant object is c10 `thm:cg-holonomy-kl-marginal`, and for noncompact links `cor:cg-holonomy-noncompact-gaussian` shows the Gaussian parent generically does not exist. L06-10 covers the statement's narrowness.

**Fix:** State the theorem "at one base point, for the diagonal action of one g∈G". Add: "With independent links carrying loop holonomy, the parent must be fixed by the holonomy group; for noncompact GL links this generically leaves no Gaussian parent [DennisTheory, Ch. 10]."

**Falsifies:** A PIFB2 use of Action (b) with h varying across base points inside the single-point theorems. The theorems are stated on a finite grid, but only pointwise equivariance is used.

**Status:** P (L06 verified the mechanism).

### G2-7: The belief-configuration Gibbs lift answers part of a named Theory open problem and should say which part

**Location:** PIFB2.tex:3578-3632 (`thm:belief_configuration_gibbs_lift`, `rem:gibbs_lift_interpretation`).

**Severity:** low.

**Evidence:**
- *Match.* c03 `open:prob-law-point-prior` asks for a normalized generative law on law points and lists five settlement conditions: (i) a sigma-finite reference, (ii) a finite normalizer, (iii) the gauge transformation law, (iv) record kernels that read law points, and (v) compatibility with sample-level recognition. The Gibbs lift supplies (i) and (ii) for finite-dimensional Gaussian presentations (a proper ν_0 and 0<Z<∞), and the remark addresses (iii) through the Haar discussion. It does not supply (iv) or (v).
- *Form.* c13 `eq:rg-formation-physical-prior` is a configuration prior of the same Gibbs form. The ledger already verifies that the lift does not produce the excluded state-level ELBO.

**Fix:** Add to the remark: "This construction supplies the proper reference and finite normalizer that a normalized law-point prior needs; record kernels that read law points and their compatibility with sample-level recognition marginals remain open [DennisTheory, Ch. 3, open problem 'A normalized law-point prior']." Keep the theorem. It is short and correct, and it is PIFB2's own.

**Falsifies:** A Theory construction of the full law-point prior, which would make this remark stale.

**Status:** P.

## Crosswalk table (Appendices A, C, D, E, F, H, I)

Relations used in the table:
- **eq:** equivalent.
- **Th>:** the Theory is strictly stronger.
- **Th<:** the Theory is weaker.
- **diff:** a different object.
- **abs:** absent from the Theory.

Dispositions are keep, condense, cite (replace by citation), supp (move to the online supplement), and cut. Theory files are given without `.tex`.

| PIFB2 label (line) | Theory file: label | Rel. | Disposition |
| --- | --- | --- | --- |
| App. A surrogate S and the (1−KL/κ) response (2224-2290, 2351-2426) | c08: `lem:obs-envelope-slow-flow`; c06: `prop:obs-attention-reduced-hessian` (the canonical gradient only) | abs (surrogate) | cut |
| receiver ∂KL/∂μ, ∂KL/∂Σ (2260, 2307) | g04: `eq:restrict-derivatives` | eq | condense |
| natural gradient and gauge law (2290, 2319-2328) | g05: `prop:ig-fisher-moment-chart` | Th> | condense, cite |
| congruence-invariant metric family (2328) | c07: `prop:ig-fisher-characterizations` (Čencov/Campbell; the SPD family itself is absent) | diff | keep one sentence (citation per L14-7) |
| retraction (2330-2349) | none | abs | supp or ML companion |
| `eq:frechet_dexp` (2368), `eq:frechet_dexp_sender` (2443) | none | abs | supp |
| `eq:kl_omega_directional` (2378), `eq:kl_omega_unconstrained` (2383) | none | abs | keep in condensed App. A |
| `eq:sender_phi_gradient` (2448), `eq:sender_softmax_entry` (2466), `eq:sender_autograd` (2471), `eq:total_gradient_mu_complete` (2483) | c05: `thm:obs-local-global-potential`, `cor:obs-potential-game` (sender terms automatic in a normalized joint) | abs (for the composite potential) | keep direct-KL sender terms; cut surrogate responses |
| complete update equations (2493-2502) | c08: `prop:obs-rate-separated-flow` | diff (typing) | condense, cite |
| complexity, stability, verification (2504-2514) | none | abs | cut (L17-8) |
| `app:variational_prelim` (2596) | c05: `thm:elbo-exact-identity`, `thm:elbo-extended-gap` | Th> | cite, two displays |
| `app:gaussian_kl` (2609) | g04: `prop:restrict-gaussian-reverse-kl` | eq | keep |
| `app:fisher_gaussian` (2619) | g05: `prop:ig-fisher-moment-chart` | Th> | keep display, cite |
| SO(3) generators and BCH (2637-2651) | g02: `prop:gen-lg-compact-frames` (general compact frames) | abs | cut |
| Cholesky (2653-2660) | none | abs | cut |
| App. D covariance gradient (2668-2731) | g04: `eq:restrict-derivatives` | eq (formula), diff (objective) | supp |
| `eq:sigma_fixed_point_beta` (2746), `eq:sigma_fixed_point_map` (2755), proposition (2759) | g04: `thm:restrict-exact-block-optimum`; g02: `prop:gauss-conditional-precision` | diff (G2-3) | supp with scope sentence |
| homogeneous limit (2770-2795) | g04: `thm:restrict-exact-block-optimum` | diff (Σ_0 vs Σ_0/2) | supp |
| `eq:beta_weighted_precision` (2846) | none | abs | cut (L07-6) |
| gradient-flow stability (2863-2881) | c08: `prop:obs-local-block-descent`; g10: `thm:obs-star-fixed-point-contraction` | Th> for normalized models | supp |
| collapse to message passing (2885-2890) | c06: `prop:obs-selective-receiver-update` | diff (gain survives) | cut or cite |
| `eq:quadratic_expectation_formula` (2900) | g03: `prop:gauss-interaction-energy-kernel` | eq (standard) | keep one line |
| `eq:belief_quadratic_expansion` (2916), KL identification (2920-2945) | g05: `prop:ig-fixed-covariance-kl` | Th> (fixed W, exact) | cut identification, cite |
| `sec:raw_alignment_weights` (2947) | c06: `prop:obs-attention-elbo`; c12: `prop:full-graph-gibbs-rows` | Th> | cite |
| `eq:F_i_app` (2982) | c05: `thm:obs-local-multiagent-elbo` | diff | keep, scoped |
| `thm:representation_app` (3039) | none; the divergence is declared in c12 `def:full-graph-transported-divergences` and c06 `def:obs-selective-comparison` | abs | condense (G2-2) |
| `eq:geometric_mean_target_app` (3048) | c05: `prop:elbo-exact-e-coordinate`; c12: `rem:full-graph-inference-loop`; g04: `eq:restrict-cavi-mean` | diff (unit exponents) | keep with the identity of G2-2 |
| `cor:closure_forces_kl` (3058), `rem:analyticity_role` (3065), `lem:richness_app` (3120) | none | abs | supp |
| dual cost (3143-3149) | c06: `cor:obs-selective-softmax`; c12: `prop:full-graph-gibbs-rows` | Th> | cite |
| `eq:beyond_mf_state_vfe`, `eq:beyond_mf_state_elbo_identity` (3433-3440) | c05: `thm:elbo-exact-identity` | eq | cite |
| `thm:nested_state_configuration_vfe` (3445) | c12: `def:full-graph-tower-vfe`, `thm:full-graph-vfe-decomposition` | eq (special case, ×T_cfg) | cite |
| `eq:beyond_mf_configuration_prior` (3469) | c13: `eq:rg-formation-physical-prior`; c04: `rem:gen-appended-energy` | eq (form) | condense |
| `eq:beyond_mf_pairwise_joint` (3481), `eq:beyond_mf_bethe_entropy` (3488) | none | abs | Outlook sentence |
| `eq:beyond_mf_block_gaussian` (3499) | g04: `thm:restrict-determinant-gap`; c05: `cor:obs-correlated-ledger` | Th> | cite |
| `eq:beyond_mf_bare_action` to `eq:beyond_mf_one_loop` (3514-3552), 2PI (3556) | none (the Theory's "effective action" is Wilsonian, c11 `thm:rg-effective-action`) | abs | Outlook paragraph (G2-4) |
| `rem:beyond_mf_no_double_counting` (3563) | c04: `rem:gen-appended-energy`; c05: `cor:obs-correlated-ledger` | eq (partly) | one sentence |
| `thm:belief_configuration_gibbs_lift` (3578) | c03: `open:prob-law-point-prior` (partial answer); c13: `eq:rg-formation-physical-prior` | Th< (Theory open) | keep (G2-7) |
| `eq:rg_exact_free_energy` (3637) | c11: `def:rg-measure-pair`, `thm:rg-effective-action` | Th> | cite (G2-1) |
| Actions (a)/(b) (3641-3643) | c02: `prop:geo-active-image-point`, `prop:geo-common-frame-gauge` | Th> at c_* | condense |
| `eq:rg_closure` (3660), `eq:rg_closure_dimensionless` (3666) | c11: `def:rg-retained-projection`, `prop:rg-interaction-residual` | diff (exact identity vs sup-norm diagnostic) | supp |
| `eq:rg_internal_hessian` (3673), `eq:rg_constrained_gap` (3683) | none | abs | supp |
| `eq:rg_reduced_hessian` (3678) | c06: `prop:obs-attention-reduced-hessian` | eq (×τ) | cite |
| `eq:rg_laplace` (3690) | none | abs | keep, with L06-6 |
| `eq:rg_inter_cluster` (3697) | c11: `prop:rg-attention-single-edge-weights`, `prop:rg-meta-attention-pushforward`; g07: `prop:cg-gaussian-aggregation` | Th> (L18-10) | cite |
| `eq:rg_slow_graph_metric` (3705), `eq:rg_schur_flow` (3718) | c08: `open:obs-slow-manifold`, `rem:obs-rate-separation-witnesses` | Theory open | supp |
| Wilsonian relevance, `eq:rg_retention_gain` (3722-3727) | c11: `prop:rg-interaction-finite-network-obstruction`; b05: `prop:rg-finite-depth-no-asymptotics`; c09: `thm:cg-evidence-preserving-channel` | contradicted for finite networks (L18-11) | cut relevance; retention to supp |
| `ass:closure_regime` (3739) | none | abs | supp |
| `thm:rg_pushforward` (3776) | c11: `prop:rg-measure-pair-composition`, `thm:rg-effective-action`; c09: `thm:rg-exact-coarse-vfe` (i) | Th> | cite |
| `thm:rg_semigroup` (3785) | c09: `prop:cg-markov-category`, `prop:rg-scale-functoriality`; g09: `prop:grg-aggregation-semigroup` | Th> | cite |
| `thm:rg_covariance` (3806) | c09: `prop:cg-equivariant-channels`; g08: `prop:cg-gaussian-forward-kl-barycenter` | complementary (PIFB2 verifies the Theory's hypothesis) | keep (G2-6) |
| `thm:rg_exact_closure` (3820), `eq:rg_app_schur_complement` (3837) | g07: `prop:cg-normalized-schur-action`; g02: `lem:gauss-schur`; c11: `prop:rg-hyperedge-generation` | eq (constant block); abs ((A6) case) | cite the constant block; cut (A6) |
| inter-cluster transport, H_IJ (3863-3874) | c10: `thm:cg-holonomy-kl-marginal`, `prop:cg-holonomy-compact-closed-form`, `cor:cg-holonomy-noncompact-gaussian` | Th> | cite |
| `thm:rg_residual` (3882) | c11: `prop:rg-interaction-residual` | diff | cut |
| `thm:rg_residual_explicit` (3896) | none | abs | cut (L06-7) |
| `thm:rg_detector_retention` (3920) | none; c09: `open:cg-natural-selector` | abs | supp or cut |
| finite-size scaling (3936-3937) | Supplement B b05, b06 (infinite networks) | Th> (deferred base scope) | cut; one-sentence pointer |

Net effect on the seven appendices in scope: from about 19,100 raw words (A 3,923; C 847; D 1,838; E 726; F 2,686; H 2,185; I 6,884) to about 3,000 retained (A 700, C 400, F 600, I 900, remainder in the discussion), with about 5,500 moved to the supplement.

## Verified, no defect (ledger candidates)

1. **Pushforward crosswalk.** PIFB2's F_{s+1} = T_cfg·H^c − T_cfg·log(dν^c/dν_{s+1}), where H^c is the Theory's conditional-partition effective action. Residual 8.9e-16; Z_s = Z_{s+1} to 12 digits. Script `G2_rg_crosswalk.py` (1). Residual caveat: one Gaussian instance with a deterministic mean map.
2. **Constant-block closure equals g07's normalized Schur marginal**, including h_eff and c_eff. Residual 5.8e-15. Script (2).
3. **Functoriality witness** of c09 `prop:rg-scale-functoriality` (iii): values 1 and 0, reproduced. Script (3).
4. **Galerkin aggregation** stays in the interaction family and satisfies A_{S2}A_{S1} = A_{S1S2}. Residual 3.6e-15. Script (4).
5. **Nested VFE equals the two-level tower VFE** up to the factor T_cfg. Residual 0.0. Script (5).
6. **KL-sum identity** KL(q‖p) + Σβ_j KL(q‖r_j) = (1+B)KL(q‖g) − (1+B)log Z_g for any q; the Gaussian pool mean and variance agree with the closed form. Residual 8.9e-16. `G2_repr_crosswalk.py` (1).
7. **Normalized pairwise joint.** CAVI equals the exact mean (4.4e-16), the variances are 1/(A_i+w), and the joint negative-ELBO gradient at the fixed point is 2.5e-10. Script (2).
8. **Reduced-Hessian units map.** τ·∇²R_i (Theory) equals PIFB2 `eq:rg_reduced_hessian`. Residual 2.9e-9 (finite-difference second differences). Script (3).
9. **App. D functional has entropy weight 1+B.** The minimizer is (1+B)M^{-1}; residuals 2.5e-8 (B=1) and 7.6e-9 (B=2.5). `G2_appD_crosswalk.py` (1).
10. **Theory block optimum** Λ_ii^{-1}: covariance error 1.9e-8, mean error 4.7e-8. Script (2). Homogeneous contrast Σ_0 against Σ_0/2: 8.9e-16 and 4.4e-16. Script (3).
11. **Fixed-W expected quadratic form** equals the common-covariance KL plus ½tr(W(Σ_i+ΩΣ_jΩ^T)). Monte Carlo relative error 1.7e-3 at n = 4e5 (sampling-limited). Script (4).

## Physics-audience and standalone notes

A physics referee expects appendices to hold the proofs of main-text claims. In the scope appendices about half the words are implementation (App. A surrogate and retraction, App. C Cholesky, the App. I closure diagnostics) or program sketches (App. H), and App. H is referenced from nowhere. The crosswalk above keeps what the Wheeler thesis uses:
- the Gibbs lift (a normalized law over belief configurations is how "bits" of many observers become a statistical ensemble);
- the covariance theorem (what "the same meta-agent in every frame" means);
- the Laplace coupling shift;
- the scoped representation statement.

Three vocabulary points will trip a physicist:
1. *"Effective action".* It is used for both the 1PI Γ (H) and the Wilsonian energy (I, and the Theory). Name them apart.
2. *Temperature.* The consensus potential makes each belief a Gibbs state at temperature 1+B_i relative to Bayesian updating (G2-3). A statistical physicist will want that stated once, next to the definitions of T_cfg, τ and κ (L16-2 lists the τ collisions).
3. *"RG".* The Theory's "exact coarse-graining" is the safer term (L06-1). The replacement text in G2-1 uses it.

For standalone reading, replacing the App. I theorem block by a citation costs little. What PIFB2 proves there is either measure-theoretic bookkeeping, which a physics reader accepts from a one-line statement, or a hypothesis-laden bound the body does not use.

## Complementarity notes

Draft paragraph for the appendices (L19-1 covers the main body). It uses no LaTeX spacing macros.

"Relation to the companion theory. Several appendices overlap with results that the companion manuscript [DennisTheory] and its Gaussian supplement [DennisTheoryG] prove at greater generality. The exact coarse-graining of Appendix I is a special case of the companion's conditional-partition formula. There, a Markov channel acts on a reference probability and on the evidence measure, preserves the partition function, and composes along any chain of resolutions. The coarea display used here differs from it only by the logarithm of the density of the pushed reference with respect to the parent reference we chose. The constant-block closure of Theorem [thm:rg_exact_closure] is the companion's normalized Schur marginal. The companion shows that marginalization generically generates hyperedges, and it replaces the schematic residual bound of Proposition [thm:rg_residual] by an exact residual identity. The nested bound of Appendix H is the two-level case of the companion's tower free energy. The one-particle-irreducible and two-particle-irreducible effective actions have no counterpart there and remain proposals. The covariance fixed point of Appendix D and the geometric-mean form of Appendix F belong to the consensus potential of this paper, which weights each belief entropy by 1+Σ_jβ_ij. In a normalized Gaussian joint the entropy enters once, the mean-field covariance is fixed in one step by the diagonal precision block, and the coordinate update multiplies the prior and pair factors with unit exponents. The companion declares the transported divergence KL(q_i‖Ω_ij q_j) rather than deriving it. Appendix F characterizes that choice only for an agent's best response with its neighbors held fixed. The belief-configuration Gibbs lift of Appendix I supplies the proper reference and finite normalizer that the companion lists as missing for a normalized prior on belief configurations. The other conditions listed there remain open."

As the brief requires, every recommendation is PIFB2-side; no Theory change is needed. One point concerns the Theory's own review record rather than its text: C1-pifb2-program-alignment.md, node N6, says the source-label joint "fixes the divergence". Per G2-2 it fixes the row form but not the divergence. Whether to correct that review note is the author's decision; SPEC section 0 is unaffected.

## Not covered

- **Theory proofs.** I did not read the proof appendices (`ca_proofs*`) and relied on the statements. I did not read Supplement B (b00-b09) beyond the claim index; the labels cited from b05 were checked to exist, not read. I read g01, g06 and g10 only at the one theorem cited.
- **PIFB2 scope.** Appendices B and G are out of scope. I did not re-derive any App. A, D, E or I identity already on the L04, L05, L06 or L10 verified lists, and I cite those lists.
- **Out of scope for this lens.** I did not check external citations (Wilson, Cardy, Fenichel, Bethe/Kikuchi, Cornwall-Jackiw-Tomboulis); those belong to L14 and L15.
- **Crosswalk depth.** For the representation theorem I did not attempt a normalized-model analogue of the converse direction. The word counts are raw LaTeX words (`wc -w`), not prose words.
