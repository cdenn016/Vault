# L05 panel report: hierarchical variational inference (PIFB2.tex)

Lens: hierarchical generative models, mean field, Bethe and region free energies. Investigator model: Claude Opus 5.5. No verifier or adjudication pass was run; these are investigator findings.

Target bytes: `Research/manuscripts/PIFB2.tex`, SHA-256 `f80e6dab...080ec4` (checked), 3956 lines.

Lines read in full (long lines printed whole with `fold`): 1533-1678 (Coarse-Graining I and II), 3162-3412 (Appendix G), 3413-3568 (Appendix H). Targeted reads: 3905-3941 (detector-retention theorem and Appendix I summary), and grep contexts for every occurrence of "detector" in the manuscript (lines 63, 81, 245, 1535, 1613-1625, 1681, 1744, 3572, 3731, 3736, 3800, 3913, 3930, 3940, 3952). Prior reviews consulted: the C1 program-alignment table (nodes N13, N14, N21) and the 2026-09-13 pifb-geometry review. Nothing below repeats them except where cited.

Executed (bare `python`, SymPy 1.14, NumPy 2.4.4, SciPy 1.17.1; all scripts are in `reviews/2026-09-24-pifb2/scripts/` and each runs in seconds):
`L05_shadow_rigid_link.py` (SymPy: linear-Gaussian marginal, mean-field component, rigid limit, Jensen gap),
`L05_augmented_gaussian.py` (float64 Gaussian instance of the augmented joint with observations: precision blocks, kernel, Gauss-Seidel, exact vs shadow vs cavity child posteriors, bound test, empirical-Bayes reading),
`L05_barycenter_variational.py` (M-step optimum, I-projection barycenter and its equivariance),
`L05_softmin_savings.py` (sign of the "savings" at Gibbs rows),
`L05_region_bethe.py` (Bethe counting numbers on a tree, product reduction, loop),
`L05_nested_effective_action.py` (nested VFE identity, vacuum decomposition, zero-temperature limit, Legendre transform and one-loop remainder),
`L05_self_consistent.py` (row-KL identity, geometric pooling, Banach-bound counterexample),
`L05_shadow_nogo.py` (third mixed variation on the child-parent shadow edge).

Primary sources checked:
- Sønderby et al. 2016 (arXiv:1602.02282v3, Eqs. 1-5, text extracted from the PDF).
- Wainwright and Jordan 2008 (FnT PDF, Proposition 4.1 and Section 5.3).
- Waade et al. 2025 (Entropy 27:143, abstract).
- Yedidia-Freeman-Weiss 2005 and Cornwall-Jackiw-Tomboulis 1974 (bibliographic data checked against references.bib).

Registered (ledger), not re-raised: the observation-term typing (669, 689); the non-sigma-finite pushforward sentence (3633-3639); the meta-clock square root (1861); and the Theory's framing decision that same-time shadows are superseded by its typing prohibition. The findings below concern PIFB2's own internal derivations, not the Theory's prohibition.

## Findings

### L05-1: The rigid-link "parent-predictive prior" double counts the constituent's evidence, and the shadow functional is not a bound for the augmented joint it is said to reduce to
**Location:** PIFB2.tex:1675 (Coarse-Graining II); 3236-3257 `lem:shadow_mf_optimum`; 3259-3261 `rem:shadow_marginal_vs_mf`; 3265-3267 (Implications); 3271.
**Severity:** high
**Evidence:** The marginalization identity itself is correct (L05_shadow_rigid_link: log-density residual 0, rigid-limit variance ω²S). The defect is in how it is used. Section 1675 says the shadow "emerges as the parent-predictive prior" of the augmented joint and places the framework "in continuity with" hierarchical VI. Line 3265 calls the construction "a hierarchical generative model with a specified mean-field reduction". Three executed checks contradict that reading.

(i) Double counting. I built a K = 2 instance of Definition `def:augmented_joint`: one parent, two children, GL⁺(2) transports, and Gaussian observations under each child. I compared the exact child posterior with the scheme the text uses, in which the child posterior is the shadow of the exact parent posterior times the child's own likelihood. At σ² = 0.3 the shadow scheme's mean error is 1.29e-1 and its covariance error is 3.1e-2. In the rigid limit σ² = 1e-8, the shadow scheme's precision exceeds the exact child precision by exactly R⁻¹ = diag(2.5, 1.667), which is the precision of the child's own observation. That observation enters the parent posterior and then enters the child a second time. The belief-propagation cavity message (the parent posterior with the child's own message removed) reproduces the exact child posterior to 1.1e-16 at σ² = 0.3 and to 6e-10 at σ² = 1e-8 (L05_augmented_gaussian, parts d-f). In the rigid limit the joint forces k_i = Ω_i k_P, so the exact child posterior *is* the pushforward of the exact parent posterior. Using that pushforward as a prior and multiplying in the likelihood again is exactly the double count.

(ii) Not a bound. Take the same-time shadow functional λKL(q_P‖p_top) + Σ_i[KL(q_i‖N(μ_P, Σ_P + σ²)) − E log p(o_i|k_i)] and minimize it over Gaussians at σ² = 0.05. The minimum falls below the surprisal −log p_σ(o) of the augmented joint by 12.98 nats for o = (2, −2), by 0.14 nats for concordant data o = (1, 1), and by 30.53 nats for o = (3, −3, 0.5) (part g). A variational free energy of that joint cannot go below its surprisal. The mechanism is the Jensen inequality E_{q_i}[−log ∫χ q_P] ≤ E_{q_i q_P}[−log χ]; the gap is 14.33 nats at the sample point in L05_shadow_rigid_link part 5. Retaining the parent covariance in the prior, the property Remark `rem:shadow_marginal_vs_mf` advertises, is what opens this gap.

(iii) The paper's own obstruction applies. The child-parent term KL(q_i‖Ω_{i,I}q_I), with q_I a varying factor, has the nonzero mixed third variation of Eq. `eq:consensus_third_variation`: the finite difference is 5.22046 against the predicted Var_{q_i}(g) = 5.22044 (L05_shadow_nogo). By Theorem `thm:state_level_elbo_nogo` (3282), the shadow edge therefore has no fixed state-level ELBO representation, which is the same status the paper assigns to the peer terms. Line 3271 ("does not affect the status of the cross-scale shadow ... within a well-defined hierarchical generative model") contradicts this.

**Fix:** Restate Lemma `lem:shadow_mf_optimum` as a computation of the variational predictive density, and drop "emerges", "reduction", and "continuity with the standard scheme" for the shadow. State in Section 1675 that the shadow evaluated against the full parent posterior is not a message of the augmented joint. Then name the three ELBO-consistent alternatives:
- the conditional (mean-field or ladder) coupling E_{q_I}KL(q_i‖χ(·|k_I));
- the cavity predictive ∫χ q_I^{∖i};
- the random-effects reading of L05-3.

Suggested sentence: "Evaluated against the full parent posterior, the shadow reuses each constituent's own evidence; the ELBO-consistent downward message uses the parent posterior with that constituent's contribution removed."
**Falsifies:** Either of two results would retract this finding. The first is an exact-posterior computation of the augmented joint, at σ² > 0 and with observations under the child, in which the child posterior equals shadow times likelihood with the full parent posterior. The second is a proof that the shadow functional is at least −log p_σ(o) for all o. The executed counterexamples rule out both for the model as written.
**Status:** The marginalization identity is P. The identification of the shadow as the prior of the augmented joint is S. The prose ("emerges", "derive the cross-scale shadow", "a hierarchical generative model with a specified mean-field reduction") inflates S to D.

### L05-2: The exact Gaussian cross-scale result is transferred to shadow dynamics it does not describe
**Location:** PIFB2.tex:3275 ("The reduction above settles the cross-scale construction at zero within-scale coupling"); 3335-3337 (Exact Cross-Scale Gaussian Exception); 3411 ("The cross-scale augmented joint supplies the closed, uniquely-solvable backbone of the dynamics").
**Severity:** high
**Evidence:** The Gaussian statements are correct for mean field on the augmented joint:
- the stated precision blocks match a finite-difference Hessian of the negative log joint to 1.5e-7;
- the link-only precision has a kernel of dimension exactly K = 2, spanned by consistent-propagation vectors (|J_link v| = 9.8e-16);
- the top prior makes the precision SPD (minimum eigenvalue 1.69);
- Gauss-Seidel mean-field sweeps converge to J⁻¹h (residual 5.6e-17; L05_augmented_gaussian parts a-c).

But the framework does not run mean field. Remark `rem:shadow_marginal_vs_mf` and the Implications paragraph (3265) say that the shadow "proceeds via the predictive rather than the strict mean-field parent message, so the manuscript's dynamics are not identified with the mean-field equations themselves". Uniqueness, the exact ELBO interpretation, and Gauss-Seidel convergence therefore attach to dynamics the framework does not use. L05-1(ii) shows that the shadow dynamics lack an ELBO interpretation even at zero within-scale coupling.
**Fix:** At 3275 and 3411, replace the transfer with: "Mean field on the augmented joint is exact and uniquely solvable at zero within-scale coupling; the shadow dynamics of Section 1669 are not this mean field (Remark `rem:shadow_marginal_vs_mf`) and inherit none of these guarantees." Cite the Theory's anchored Gaussian star (see Complementarity) for the exact statement.
**Falsifies:** A demonstration that the shadow-scheme fixed point coincides with the mean-field fixed point of the augmented joint at σ² > 0. Part (d) of L05_augmented_gaussian shows they differ.
**Status:** The Gaussian exception is P. Its transfer to "the backbone of the dynamics" is unsupported, and the prose inflates it.

### L05-3: Two incompatible generative readings support the barycenter-plus-shadow; only the empirical-Bayes one is ELBO-exact, and the text leans on the other
**Location:** PIFB2.tex:1602 ("The strict barycenter is therefore an exact M-step coordinate"), versus 1675 and Appendix G.
**Severity:** medium
**Evidence:** The M-step claim at 1602 is correct. Maximizing Σ_i w_i E_{q_i}[log N(Ω_{i,I}μ_I, Ω_{i,I}Σ_IΩ_{i,I}^⊤)] over (μ_I, Σ_I) returns the barycenter with the dispersion term (optimizer tolerance 1e-6, L05_barycenter_variational part 1). This objective differs from the barycenter objective `eq:meta_agent_barycenter` by a q_I-independent constant (the difference is constant to 1.3e-9 across two parent states). The barycenter therefore minimizes the constituents' own prior terms.

The generative model that makes this an exact EM coordinate is a random-effects model. The constituents are *independent draws* k_i ~ N(Ω_{i,I}m, Ω_{i,I}SΩ_{i,I}^⊤) with a point hyperparameter θ = (m, S). In the scalar test, min over (q, θ) of Σ_i[KL(q_i‖p_θ,i) − E log lik] equals −max_θ log p_θ^RE(o) to 8.9e-16, and θ* equals the barycenter-with-dispersion of the q_i (part h). This is type-II maximum likelihood (empirical Bayes), and it is monotone under Neal and Hinton's coordinate argument.

Appendix G's model is a different one: one parent *latent*, children as noisy copies of it, and Σ_I as parent posterior uncertainty. In its rigid limit all children are identical up to transport, so the joint gives zero probability to the constituent dispersion that the barycenter's dispersion term records. The two readings assign different meanings to Σ_I (population spread versus posterior uncertainty) and cannot both be the model.
**Fix:** In Section 1675, present the random-effects reading as the one that makes the shadow a legitimate prior: the parent is a fitted hyperparameter, q_I is a point estimate rather than a posterior, and Σ_I is the population covariance. Demote Appendix G's rigid-link lemma to an illustration, per L05-1. This also settles the "tension with the Level-3 commitment" that 1602 itself raises, because under the ELBO-exact reading the parent carries no belief.
**Falsifies:** A single generative model in which both the rigid-link predictive reading and the M-step barycenter-with-dispersion are exact coordinates of one functional.
**Status:** The M-step identity is P (verified). The Appendix G reading is S. The text does not say that the two readings are distinct models.

### L05-4: The "savings" rationale for the licensing criterion has the wrong sign for the canonical functional
**Location:** PIFB2.tex:1600 (savings paragraph under `eq:meta_agent_FE_criterion`, 1596); consequences at 3930 (the hypothesis A_I > 0 of `thm:rg_detector_retention`).
**Severity:** medium
**Evidence:** The text locates the savings in "replacing the intra-cluster pairwise alignment terms of F*" and bounds the gross removal by |I|ε. In the entropy-retaining F*, however, each row sits at its Gibbs value A_i = −τ log Σ_j π_j e^{−E_j/τ}. Removing the intra-cluster sources raises A_i when they are the low-energy sources, which is the high-coherence regime the paragraph assumes:
- with the prior left unnormalized, the change is τ log(1 + Z_in/Z_out) > 0;
- with the prior renormalized over the survivors, the change is positive iff the π-average of e^{−E/τ} over the cluster exceeds that over the rest, which holds whenever intra-cluster energies are smaller.

Across 20,000 random rows with intra-cluster E < ε ≤ extra-cluster E, the minimum change was +7.3e-4 (unnormalized) and +4.6e-4 (renormalized). No row showed a saving (L05_softmin_savings). The |I|ε figure bounds Σ_{j∈I} β_ij E_ij before re-optimization, not the change in F*. The positive saving A_I > 0 that `thm:rg_detector_retention` takes as a hypothesis therefore has no identified source among the terms the paragraph names. In addition, C(I) is left unspecified ("natural choices are an entropy or minimum-description-length term"), so the criterion contains a free function.
**Fix:** Replace the savings sentence with: "At Gibbs-optimal rows, deleting coherent intra-cluster sources raises each row's optimized value; any net gain must come from the rows of agents outside the cluster, which couple to one parent instead of |I| constituents, or from the parent's prior term. This is not derived here." Delete the |I|ε "upper bound on what is removed", or state it only for the energetic part at frozen β.
**Falsifies:** A high-coherence configuration in which the re-optimized F* decreases when intra-cluster sources are deleted. For rows as defined, the analytic sign argument above rules this out.
**Status:** The criterion is C, as the text says. The quantitative bound, read as a bound on savings, is incorrect.

### L05-5: The detector is promoted beyond "heuristic" in three places
**Location:** PIFB2.tex:1580 (Definition of Meta-Agent, condition (1)); 3940 (Appendix I summary); 1588 (Waade et al.).
**Severity:** medium
**Evidence:** Line 1615 states that the detector-criterion relation is "heuristic and partial" and that the detector is "a coherence or similarity filter rather than a net-gain maximizer". Line 3913 states that Theorem `thm:rg_detector_retention` "validates the strengthened detector stated here rather than the implemented one". Three passages contradict this:
- (a) The formal Definition at 1580 makes Γ > Γ_min the first defining condition for a meta-agent to form, while 1535 and 1596 assign the "when" to the free-energy criterion. The surrogate has thus been written into the definition.
- (b) The Appendix I summary at 3940 reads: "The threshold detector of Section `sec:meta_agent_threshold` is a sufficient-condition surrogate for positive variational retention gain". That is the body detector, which the paper elsewhere excludes from the theorem.
- (c) Line 1588 says Waade et al. "show that a collective constitutes a bona fide group-level agent exactly when it sustains a group-level Markov blanket", and that w_i^I and Γ_min "operationalize that criterion". The Waade abstract says a collective "can, if they maintain a group-level Markov blanket, constitute a larger group-level active inference agent". That is a sufficient condition, and the paper's contribution is a data-driven estimation method, not a characterization. Moreover, a KL-similarity threshold does not test a conditional-independence (blanket) structure.

**Fix:**
- (a) Define a meta-agent by the free-energy criterion `eq:meta_agent_FE_criterion`, together with the cluster-support and size conditions, and move Γ > Γ_min to Section 1607 as the deployed candidate filter.
- (b) At 3940, write "The strengthened detector with the gap condition is a sufficient-condition surrogate ...; the body detector is not covered".
- (c) At 1588, write "Waade et al. propose that a collective can constitute a group-level agent if it maintains a group-level Markov blanket; the detector here does not test that condition."

**Falsifies:** Showing that the Definition's condition (1) is intended only as a candidate filter, with the criterion as the formation rule, and that 3940 refers to the gap-strengthened detector. The text as written supports neither reading.
**Status:** The detector is S (a heuristic filter). The three passages inflate it to P or D.

### L05-6: The coherence weights are called both a saddle-point approximation and a declared modeling choice
**Location:** PIFB2.tex:1633 versus 1602.
**Severity:** medium
**Evidence:** Line 1633 says w_i^I = χ_i exp[−KL(Ω_{I,i}q_i‖q̄_I)] "is the leading-order saddle-point approximation of the variational cluster-aggregation weights w_i^I in `eq:meta_agent_barycenter`". Line 1602 says: "The derivation fixes the form and not the weights: any weight vector yields a valid M-step coordinate, so the coherence factor exp[−KL] remains a declared modeling choice." In `eq:meta_agent_barycenter` the weights are inputs. No variational problem for w is stated, so there is no saddle point to approximate. Softmax-in-KL weights would arise as E-step responsibilities if each constituent carried a latent membership indicator (parent versus a background component), but no such mixture appears in the manuscript.
**Fix:** Delete the saddle-point clause at 1633, or add the membership-mixture model that yields exp[−KL] responsibilities and derive them from it. Otherwise keep the statement at 1602.
**Falsifies:** A stated variational problem over w whose Laplace approximation gives χ exp[−KL].
**Status:** The weights are a modeling choice (S). The clause at 1633 inflates this to D.

### L05-7: The configuration-temperature scaling makes the zero-temperature limit data-blind
**Location:** PIFB2.tex:3445 (`thm:nested_state_configuration_vfe`); 3456 (`eq:beyond_mf_configuration_prior`); 3514 (`eq:beyond_mf_bare_action`); 3416; 3567.
**Severity:** medium
**Evidence:** Both terms of J carry T_cfg, and P_0 ∝ exp(−F_vac/T_cfg). The configuration optimum is therefore R* ∝ exp(−F_vac/T_cfg)p(o|X). In A_o the state surprisal enters at order T_cfg, the same order as the one-loop determinant. As T_cfg → 0, R* concentrates on argmin F_vac independently of o. Test case: F_vac = X²/2 and p(o|X) = N(o; X, 1) give E_{R*}[X] = oT/(1+T). At T = 0.001 and o = 5 this is 0.0050, matching the closed form (L05_nested_effective_action part 3).

The opening paragraph (3416) lists "deterministic minimization of one population functional" as one of the mean-field levels, and 3567 lists T_cfg → 0 among the limits that recover it. What the limit actually recovers is minimization of the observation-free vacuum functional. The paper's own rule excludes observations from F_vac (3471), so in this limit the slow variables stop learning from data.
**Fix:** Either temper the likelihood, taking J = T KL(R‖P_0) + ∫F_state R so that R* ∝ P_0 p(o|X)^{1/T} and T → 0 gives data-driven MAP learning of X, or state at 3567: "T_cfg → 0 concentrates the configuration on the vacuum minimizer; data enter only at order T_cfg."
**Falsifies:** A T-scaling in the displayed definitions under which R* at T → 0 depends on o. The definitions as written give the data-blind limit.
**Status:** The nested identity is P (verified). The implied zero-temperature correspondence is S and is incorrect as stated.

### L05-8: The Banach guarantee for the frozen mean sub-map is false as stated
**Location:** PIFB2.tex:3409 (Scalar Objectives and Update Fields).
**Severity:** medium
**Evidence:** The text claims the following. With covariances and attention frozen and orthogonal transports, the mean map μ_i ← (αΛ_p + Σ_jβ_ijΛ_{t,ij})⁻¹(αΛ_pμ_{p,i} + Σ_jβ_ijΛ_{t,ij}Ω_ijμ_j) has neighbor-operator norm at most λ_max(M)/[αλ_min(Λ_p) + λ_max(M)] < 1.

Counterexample: N = 3, K = 2, α = 0.05, Λ_p = I, anisotropic Λ_{t,ij}, and rotations Ω_ij. The stated bound is 0.9993, but the Jacobian's spectral radius is 1.173. Iterating the map multiplies the error by 1.3e3 in 60 steps, so the map is not a contraction in any norm (L05_self_consistent part 3b). A random search found ‖J‖₂ exceeding the bound by up to 3.75. The argument fails because (αΛ_p + M)⁻¹β_jΛ_{t,ij} can have operator norm above β_jλ_max(Λ_{t,ij})/λ_max(M) when M and Λ_{t,ij} do not commute.
**Fix:** Restrict the claim to isotropic couplings, Λ_{t,ij} = λ_ijI and Λ_p = I. The block-∞ row norm is then Σ_jβ_ijλ_ij/(α + Σ_jβ_ijλ_ij) < 1. Alternatively, assume symmetric coupling (a convex scalar potential), under which Gauss-Seidel converges on an SPD system.
**Falsifies:** An error in the script's Jacobian. The direct iteration in part 3b does not use the Jacobian and shows the growth independently.
**Status:** The claim is presented as P. It is false outside the isotropic case.

### L05-9: Internal inconsistencies in the barycenter subsection
**Location:** PIFB2.tex:1540; 1573-1575 versus 1644 and 1655.
**Severity:** low
**Evidence:**
- (a) Line 1540 calls the M-projection barycenter "the one construction that is at once a genuine variational minimizer and gauge-covariant under the diagonal group action". The I-projection argmin_q Σ w_i KL(q‖Ω_{Ii}q_i) also qualifies. It is a strict variational minimizer: its closed form, the precision average Λ = Σ w_iΛ̃_i, matches a numeric minimizer to 1.4e-7. It is exactly covariant (residual 4.8e-14 under a random GL⁺(2) element). It also differs from the M-projection (|Δμ| = 0.59, |ΔΣ| = 2.0; L05_barycenter_variational part 2). Line 1655 itself mentions this product-of-experts form.
- (b) The 2026 paragraph at 1575 states that the additive frame's "O(‖φ_i‖²) accuracy claim above names the wrong controlling parameter". Lines 1644 and 1655 nevertheless restate that claim unchanged, and 1644 says the licensing argument "inherits the same O(‖φ‖²) approximation".

**Fix:**
- (a) Replace "the one construction" with "a construction", and give the actual reason for choosing the M-projection: it is the M-step coordinate of L05-3, and it pools uncertainty rather than sharpening it.
- (b) Update 1573, 1644, and 1655 to match the 1575 finding: the additive frame is not equivariant, and its defect is controlled by the gauge-transformation magnitude.

**Falsifies:** For (a), a failure of the I-projection's equivariance or strict convexity. Neither occurred.
**Status:** (a) is a false uniqueness claim. (b) is an internal contradiction.

### L05-10: Citation and notation defects in Appendices G and H
**Location:** PIFB2.tex:3224, 3228, 3265, 3267, 3374; notation throughout Appendix G.
**Severity:** low
**Evidence:**
- (a) `\cite[Prop.~4.1]{Wainwright2008}` is cited for the mean-field fixed-point equations (3228, 3265). In the FnT text, Proposition 4.1 reads "The inclusion M(G) ⊆ L(G) holds for any graph", which concerns the marginal polytope. Naive mean-field coordinate ascent is in Section 5.3.
- (b) At 3224 the parent message is called the "upward message" and the children's messages "downward", which reverses the usual top-down/bottom-up convention. The text also says "the first sum" of what is a single term.
- (c) Sønderby et al. Eq. 2 write p_θ(z_i|z_{i+1}) = N(z_i|μ_{p,i}(z_{i+1}), σ²_{p,i}(z_{i+1})), with a per-dimension variance rather than σ²I. More substantively, their bound (Eqs. 4-5) is KL(q_φ(z|x)‖p_θ(z)) on the joint, so the conditional prior is evaluated at parent samples. That is exactly where the ladder VAE differs from the predictive shadow (L05-1), and the "becomes precise" comparison at 3267 omits it. The ladder objective also diverges as σ² → 0 unless q degenerates, so the "deterministic-decoder limit" is singular for the variational problem: L05_shadow_rigid_link part 4 shows the mean-field link energy diverging as 1/σ².
- (d) The identity `eq:equilibrium_row_kl_identity` (3374) holds for every (q, β), not only at the equilibrium (residual 0.0 at a random non-equilibrium point).
- (e) In Appendix G, χ denotes both the spatial support function and the Gibbs factor, and π denotes the parent map, the top prior, and the attention prior.

**Fix:**
- (a) Cite Wainwright and Jordan 2008, Section 5.3, and Bishop 2006, Section 10.1.
- (b) Rename the messages "top-down (from the parent)" and "bottom-up (from the children)".
- (c) Add one sentence on the conditional versus predictive KL.
- (d) Write "for every (q, β), and in particular at q*".
- (e) Rename the Gibbs factor (for example K_{i,π(i)}) and the top prior (for example ρ_top).

**Falsifies:** An edition of Wainwright and Jordan in which Proposition 4.1 is the mean-field update.
**Status:** Citation and presentation defects.

## Verified, no defect (ledger candidates)

- **Parent-predictive marginal.** The linear-Gaussian marginal `eq:shadow_soft` and its rigid limit. SymPy scalar integral: log-density residual 0, limit ω²S. Script L05_shadow_rigid_link (parts 1 and 3).
- **Strict mean-field child component.** It is N(Ωμ_P, σ²I), with the parent covariance absorbed into the constant (Remark `rem:shadow_marginal_vs_mf`). SymPy coefficient extraction gives a k² coefficient of −1/(2σ²) and a k coefficient of ωμ/σ². L05_shadow_rigid_link part 2.
- **Mean-field parent update.** In the augmented joint it is precision addition, Λ_p + σ⁻²ΣΩ^⊤Ω, independent of the constituent covariances (1602). Symbolic component as above; the matrix version is exact by construction (residual 0.0). L05_barycenter_variational part 3.
- **Gaussian exception (3335-3337).** Diagonal blocks σ⁻²(I + Σ_jΩ_{j,i}^⊤Ω_{j,i}), off-diagonal blocks −σ⁻²Ω_{i,π(i)}, top block Λ_top + σ⁻²ΣΩ^⊤Ω; finite-difference Hessian residual 1.5e-7. The link kernel has dimension K on the consistent-propagation subspace (9.8e-16), the full precision is SPD, and Gauss-Seidel reaches J⁻¹h to 5.6e-17. L05_augmented_gaussian parts a-c.
- **Barycenter as M-step (1602), dispersion term included.** Optimizer residual 1.1e-6 (mean) and 3.1e-6 (covariance) in K = 2 with random GL⁺ transports. Equivalent to the objective of `eq:meta_agent_barycenter` up to a constant (residual 1.3e-9). L05_barycenter_variational part 1. The scalar empirical-Bayes version is exact to 8.9e-16 (L05_augmented_gaussian part h).
- **Moment matching in `prop:barycenter_existence`.** Covered by the M-step check above; the Bregman convexity argument was checked analytically.
- **No-go hypothesis on a child-parent edge.** The hypothesis of `thm:state_level_elbo_nogo` holds there: mixed third variation 5.22046 against Var 5.22044. L05_shadow_nogo.
- **Self-consistent equilibrium.** Row-KL identity `eq:equilibrium_row_kl_identity`: residual 0.0. Geometric-pooling Euler equation `eq:self_consistent_response_map`: residual 4.6e-9. L05_self_consistent parts 1-2.
- **Bethe entropy `eq:beyond_mf_bethe_entropy`.** The counting numbers c_i = 1 − d_i agree with Yedidia-Freeman-Weiss 2005. On a 5-node tree, F_Bethe at exact marginals equals −log Z (residual 0.0) and H_B equals the joint entropy (4.4e-16). Product beliefs reduce H_B to Σ H(q_i) exactly (0.0), including an isolated node. On a 4-cycle, F_Bethe at exact marginals differs from −log Z by 0.099, consistent with "not a generic bound". L05_region_bethe.
- **Nested state and configuration VFE `eq:nested_state_configuration_identity`.** Residual 1.1e-16 on a finite model with random R and Q_X. The vacuum-prior decomposition, including the +T log Z_0 constant with unnormalized ν_0, has residual 0.0. L05_nested_effective_action parts 1-2.
- **Effective action (3526-3552).** φ = δW/δJ equals ⟨ξ⟩ (residual 2.8e-8), and T W'' equals the connected variance (7.8e-10), consistent with G = T(Γ⁽²⁾)⁻¹. For the one-loop form, −T log Z − [A + (T/2) log(A''/(2πT))] scales as T², with coefficient 0.0440 converging to g/(8a²) − 5c²/(24a³) = 0.04400. This also corroborates Appendix I's integrated coefficients 1/8 and 5/24 (3905). L05_nested_effective_action part 4.
- **Parent-frame cancellation (1575).** Ω_{i,I}μ_I = U_iU_I⁻¹μ_I = U_i m and Ω_{i,I}Σ_IΩ_{i,I}^⊤ = U_iSU_i^⊤. Analytic; no script.
- **Dispersion-drop bound `eq:dispersion_drop_bound`.** Re-derived analytically via the pairwise-difference identity and the mean-term KL bound; no script. Residual caveat: the pass band bounds the unweighted mean KL, while the bound uses the w-weighted ε̄_w. The two coincide only for uniform weights; this was not tested numerically.
- **2PI.** The description (Cornwall-Jackiw-Tomboulis 1974) and its status as a "proposed completion" are correctly fenced (3556); no claim is inflated.

## Physics-audience and standalone notes

A physics referee will read Appendix G as a lattice-field construction and will look for the physics names of its objects. The augmented joint is a Gaussian tree with nearest-neighbor couplings between scales, so the "Gibbs factor" χ is a normalized transition kernel (a propagator), not a Boltzmann weight. The meta-agent barycenter is a block spin in Kadanoff's sense (Kadanoff 1966), and citing that would anchor the coarse-graining vocabulary. The region free energy is the Bethe-Peierls and Kikuchi cluster-variation method (Bethe 1935; Kikuchi 1951), which physicists know by those names; at present only YFW 2005 and Wainwright-Jordan are cited.

The machine-learning vocabulary (E-step, M-step, ladder VAE, amortized, information bottleneck) should either be translated or moved to a comparison paragraph. Suitable translations are the saddle point of a two-block functional, type-II maximum likelihood, and empirical Bayes. The ladder-VAE and information-bottleneck paragraphs (3267, 1604) are not needed for Wheeler's thesis and could be cut to one sentence each. References to implementation artifacts (`MAgent_Model/gauge_agent/meta_agents.py::ConsensusDetector` at 1613, the "checked-in FullVFE path" at 3400) do not belong in a physics journal and should be replaced by a data-availability statement. Phrases such as "heat death of the informational universe" and "epistemic death" (1660) are rhetorical and will read as overreach unless tied to a stated entropy functional.

The convention W = +T log Z with Γ = Jφ − W (3526-3530) is the statistical-field-theory convention. One line stating that Γ at J = 0 equals −T log Z, the configuration free energy, would prevent confusion with W = −T log Z. The four meanings of "mean field" listed at 3416 are helpful for physicists. The text should also note that T_cfg is not a physical temperature (see L05-7).

Standalone reading: the participatory feedback equation (1669-1673) is the manuscript's operative realization of Wheeler's loop, and its only derivational support is Appendix G, which a reader who never sees the Theory would take as a derivation. After L05-1 to L05-3, the honest standalone statement is as follows. The downward leg is ELBO-exact in the empirical-Bayes reading (the parent as a fitted hyperparameter), or in the cavity or conditional-KL readings, but not as the full-posterior shadow. The main text should say which reading carries the Wheeler interpretation. Under the ELBO-exact reading the parent carries no belief, which bears directly on the Level-3 claim that meta-agents are agents.

## Complementarity notes

- **Anchored Gaussian star.** The Theory's anchored Gaussian star (`g10_reciprocal_pairs.tex`, `sec:obs-star`, `thm:obs-star-fixed-point-contraction`) is the same model as PIFB2's Gaussian cross-scale exception: an apex latent with a proper prior and conditionally independent transported children. At 3335, PIFB2 should cite it for the exact fixed point and contraction rate instead of re-deriving a weaker statement.
- **Conditional cross-scale KL.** The ELBO-consistent downward coupling that L05-1 recommends is the Theory's conditional cross-scale KL (`c12_multiscale_vfe.tex`, `prop:full-graph-downward-coupling`, `eq:full-graph-cross-scale-kl`), E_Q KL(Q_Z(·|Y_{ℓ+1})‖K_↓(·|Y_{ℓ+1})). PIFB2 can cite it as the form in which "meta-agents shape constituent expectations" holds with evidence semantics.
- **Appended energies.** The general statement behind L05-1(ii) is `c04_generative.tex` `prop:gen-gibbs-counterexample` together with `rem:gen-appended-energy`: an energy appended without its normalizer is not an evidence bound. `req:gen-typing-prohibition` is the registered framing decision (ledger) and is not re-argued here.
- **Block coordinate ascent.** `c12_multiscale_vfe.tex` `rem:full-graph-inference-loop`, which treats the inference loop as block coordinate ascent on a fixed joint, is the rigorous counterpart of PIFB2's E-step and M-step language at 1602. Citing it would let PIFB2 keep the M-step claim while pointing to the Theory for the monotonicity argument.
- **Appendix H.** No Theory result replaces PIFB2's Appendix H nested identity (C1 node N21 records the 1PI and 2PI program as absent from the Theory). Appendix H is therefore the one place in my scope where PIFB2 supplies content the Theory lacks. Apart from L05-7, that content is correct (see the verified list).

## Not covered

- The proof sketch of `lem:weight_contraction` (1636-1641), which belongs to the information-geometry lens.
- The Karcher frame barycenter and the no-equivariant-map argument at 1575, beyond checking their internal consistency; these belong to the gauge lens.
- A numerical check of the dispersion bound with non-uniform coherence weights.
- The Gibbs lift of Appendix I (3578), except where its summary at 3940 bears on the detector.
- Background-field and Faddeev-Popov details of `eq:beyond_mf_one_loop`, beyond the scalar check.
- The consensus-foils subsection (1657-1661) was read but contains no checkable variational claim.
