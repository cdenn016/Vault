# G4 panel report: Appendices H and I through a statistical-field-theory lens

**Lens:** G4, statistical field theorist (gauge-fixed functional integrals, Faddeev-Popov and quotient measures, loop expansions, adiabatic elimination), refereeing for a physics journal.
**Model:** Claude Opus 5.5 (`claude-opus-5-5`), investigator only; no adjudication.
**Target:** `Research/manuscripts/PIFB2.tex` (bytes as fixed in BRIEF.md).
**Lines read in full:** 3413-3568 (Appendix H), 3569-3790 (Appendix I working forms, gauge-action paragraph, closure ansatz, residuals, constrained gap, Laplace step, inter-cluster couplings, adiabatic elimination, retention, detector, start of the theorem subsection), 3915-3941 (detector remark and theorem, adiabatic-elimination paragraph at 3934, finite-size scaling, summary). Context read: 929-1005 (timescales and natural-gradient conventions). Prior panel reports L05, L06, L07 were read for overlap; Theory `c08_two_timescales.tex:245-282` and `c11_network_coarsegraining.tex:100-125, 1064-1080` were read for complementarity.
**Executed (bare `python`, NumPy 2.4.4, SciPy 1.17.1, SymPy 1.14; each script finishes in under 5 s):**
`scripts/G4_quotient_one_loop.py` (check a), `scripts/G4_constrained_gap.py` (check b), `scripts/G4_slow_metric.py` (checks c and d). Outputs quoted below are from those runs. No citation was re-verified online by this lens; bibliographic data for Fenichel 1979, Faddeev-Popov 1967, Abbott 1982 and Cornwall-Jackiw-Tomboulis 1974 in `references.bib` agree with the standard references as I know them, but that is not a primary-source check.

Registered items touched and not re-argued: eq:rg_reduced_hessian is a verified Schur complement (ledger); the Gibbs lift is verified (ledger); the one-loop parent-entropy shift (L06-6), (A6) and closure (L06-2), and the T_cfg data-blind limit (L05-7) are not re-raised, except that G4-8 refines the determinant convention in the L06-6 fix.

## Findings

### G4-1: The force-residual bound in eq:rg_schur_flow is false at T_cfg > 0, because the deterministic slow flow does not feel the entropic (fluctuation-determinant) force that F^exact_{s+1} contains

**Location:** PIFB2.tex:3711-3720 (`eq:rg_schur_flow` and the sentence "The force residual is dimensionful and is bounded by δ_{I,1}"), 3660 (`eq:rg_closure`, definition of δ_{I,1}), 3934 (restatement), with 3582 (the Gibbs law is not the law of the implemented deterministic dynamics) and 3690 (`eq:rg_laplace`).

**Severity:** high

**Evidence:** δ_{I,1} = ||d r_I||_{G_slow^{-1}} with r_I = F^exact_{s+1} − F̂^agent_{s+1}, and F^exact_{s+1} is the pushforward free energy at finite T_cfg (`eq:rg_exact_free_energy`). By `eq:rg_laplace`, F^exact_{s+1}(Y) = F_eff(Y) + (T_cfg/2) log det' H_I^⊥(Y) + const + O(T_cfg²), where F_eff(Y) = inf over the fiber of F_s (the zero-temperature profile written at 3639). The flow the paper runs is deterministic natural-gradient descent (3582 says so explicitly). On the slow manifold its reduced vector field is −grad_{G_slow} F_eff, not −grad_{G_slow} F^exact_{s+1}. Hence

R_cl = −grad(F_eff − F̂) = −grad r_I + (T_cfg/2) grad log det' H_I^⊥ + O(T_cfg²),

and the most that follows is ||R_cl|| ≤ δ_{I,1} + (T_cfg/2) ||d log det' H_I^⊥||_{G_slow^{-1}} + O(T_cfg²).

Counterexample (`G4_slow_metric.py`, part d1). Take F(Y, ξ) = bY²/2 + a₀e^{kY}ξ²/(2ε). Then F^exact_{s+1}(Y) = bY²/2 + (T/2)kY + const. Choose the agent ansatz F̂ := F^exact_{s+1}, so δ_{I,0} = δ_{I,1} = 0. Integrating the ODE with b = 1, k = 2, T = 0.1 gives Ẏ = −bY to eight digits at ε = 10⁻² and at ε = 10⁻³. The residual is R_cl = Tk/2 = 0.100000 in both cases, independent of ε, so it cannot be absorbed into R_ts = O(ε_ts). The inequality ||R_cl|| ≤ δ_{I,1} fails with δ_{I,1} = 0. This is not a toy artifact. In PIFB2's mean sector the Y-dependence of log det' H_I^⊥ is the −(|I|−1) log det Σ_I shift established by L06-6, so the omitted force is generically nonzero.

**Fix:** Choose one of the following and state it at 3711.
(i) Define the force residual against the zero-temperature profile: "Let r_I^{(0)} = F_eff − F̂^agent_{s+1} with F_eff(Y) = inf_{R_s(X)=Y} F_s(X), and δ_{I,1} := ||d r_I^{(0)}||_{L^∞(N_I; G_slow^{-1})}. Then ||R_cl||_{G_slow} ≤ η δ_{I,1}." Keep the calibrated finite-T δ_{I,0} for the static (Gibbs) statements.
(ii) Keep F^exact_{s+1} and add the entropic term: "||R_cl||_{G_slow} ≤ η[δ_{I,1} + (T_cfg/2)||d log det' H_I^⊥||_{G_slow^{-1}}] + O(T_cfg²)."
(iii) Declare overdamped Langevin dynamics at T_cfg. The reduced drift is then the mean force, but the reduced equation acquires noise and metric-divergence (Itô) terms, and 3582 would have to be withdrawn.
Option (i) matches the paper's own statement that contact with the dynamics is made only at T_cfg → 0. The residual can also be written as the semiconjugacy defect of the coarse map (Theory `c11`, `eq:rg-pointwise-parent-semiconjugacy-defect`), which is the exact dynamical notion. (η is the mobility; see G4-7.)

**Falsifies:** A statement elsewhere in PIFB2 that the parent flow in `eq:rg_schur_flow` is the mean-force drift of a stochastic dynamics at temperature T_cfg, together with the missing noise and Itô terms. Alternatively, a restriction of `eq:rg_schur_flow` to T_cfg → 0. I found neither in 3569-3941.

**Status:** The bound is presented as D conditional on small δ_{I,1}. As stated it is false for T_cfg > 0 (counterexample above) and correct only in the T_cfg → 0 limit or under option (i).

### G4-2: eq:beyond_mf_one_loop leaves μ, g_phys and Γ_measure undefined; with a fixed μ the remainder is O(T log T), not O(T²), and the quotient metric requires a gauge-invariant ambient metric that PIFB2's frame sector does not supply

**Location:** PIFB2.tex:3546-3554 (`eq:beyond_mf_one_loop` and the paragraph after it), 3520-3527 (`eq:beyond_mf_generating_functional`, dν_phys).

**Severity:** medium

**Evidence:** The Laplace expansion of Z_phys = ∫ e^{−A/T} dν_phys around a nondegenerate quotient saddle, with dν_phys = ρ_phys vol_{g_phys}, is

Γ[X̄] = A(X̄) + (T/2) log det(g_phys^{−1}H_phys/(2πT)) − T log ρ_phys(X̄) + O(T²).

This matches the displayed form only if μ² = 2πT_cfg and Γ_measure = −T log ρ_phys(X̄). The manuscript defines none of μ, g_phys or Γ_measure (grep finds each symbol only at 3549-3554). With μ a fixed scale the difference is −(n_phys/2) T log(2πT/μ²), where n_phys is the number of physical modes. That is an O(T log T) term, so the stated O(T_cfg²) remainder is false unless it is absorbed into Γ_measure.

Compact test (`G4_quotient_one_loop.py`, Part A). Take two K = 2 means with diagonal SO(2) redundancy and F = (|a|²−1)² + ½(|b|²−2)² + 0.8(a·b − 0.6)² + 0.6(a×b − 0.9)². Evaluate Z_phys = Z_full/vol(SO(2)) exactly by the polar change of variables on a 221³ grid. The saddle has |grad| = 4×10⁻¹⁵, a Hessian kernel exactly along the orbit generator V (|HV| = 4.5×10⁻¹⁵), and horizontal eigenvalues 3.50, 6.88, 10.97. With Γ_measure = −(T/2) log Gram, where Gram = |V|² = 2.796 is the Gram matrix of the redundancy generators in the ambient metric (the orbit-volume density), and μ² = 2πT, the residual divided by T² is −0.1525, −0.1485, −0.1465, −0.1456 and −0.1451 for T = 0.2, 0.1, 0.05, 0.025 and 0.0125. The remainder is therefore O(T²). With μ = 1 fixed, the residual divided by T is 3.8144 at T = 0.0125, against −(3/2)log(2πT) = 3.8162. That residual grows like T log T, as predicted. Γ_measure itself is −0.51 T here, the same order as the one-loop term, so it cannot be dropped.

Noncompact test (Part B). GL⁺(2) acts on Gaussian (μ, Σ) with the Fisher metric. The determinant of the Gram matrix of the four generators is 5.499008264463 at three random points of one orbit, so it is constant along orbits and Γ_measure is finite. The Weil quotient density of the Fisher volume (Haar normalized to Lebesgue at the identity) equals sqrt(det Gram)·sqrt(g_uu) to 10⁻¹⁰ at u = 0.5, 1, 1.5 and 2.5. The one-loop quotient formula against the exact one-dimensional quotient integral gives residual/T² of 0.162 to 0.182, again O(T²). By Weil's formula the raw invariant integral equals vol_Haar(GL⁺(2)) × Z_quot = ∞, so the manuscript's "Raw Haar integration ... is not admissible" is correct (analytic, not numerically run). With the non-invariant coordinate (Lebesgue) metric, the same Gram determinant varies from 4.7×10⁻⁵ to 8.4 along one orbit, so no quotient metric or quotient density is defined without a slice. PIFB2's own frame metric (`eq:pullback_metric`, ambient Frobenius) is not invariant under the redundancy U_i → U_i g (L07-5). For GL⁺(K_q) frames, g_phys in `eq:beyond_mf_one_loop` is therefore undefined unless a right-invariant metric is adopted.

**Fix:** Replace the display and the following sentence with:
"Γ[X̄] = A_o[X̄] + (T_cfg/2) Tr log(g_phys^{−1}H_phys/(2πT_cfg)) + Γ_measure[X̄] + O(T_cfg²), with Γ_measure = −T_cfg log ρ_phys(X̄), where dν_phys = ρ_phys vol_{g_phys}. For a free action of the redundancy group by isometries of a G-invariant ambient metric g, with ν the Riemannian volume of g, the Weil quotient measure has ρ_phys = (det 𝒢_{ab})^{1/2} with 𝒢_{ab} = g(V_a, V_b) the Gram matrix of the redundancy generators, so Γ_measure = −(T_cfg/2) log det 𝒢. In a gauge-fixed calculation with slice χ = 0 the same result is (T_cfg/2) log det H_slice − T_cfg log|det FP|, where FP = ∂χ/∂θ, since det FP²/det H_slice = det 𝒢/det H_phys."
Add a hypothesis that the ambient metric and reference measure are invariant under the quotiented redundancy, and note that `eq:pullback_metric` is not.

**Falsifies:** A definition of μ with μ² = 2πT_cfg, or of Γ_measure containing the T log T term, anywhere in PIFB2. Or a redundancy that PIFB2 quotients which acts non-freely at the backgrounds used, where the formula needs orbifold corrections instead.

**Status:** D (standard Laplace expansion). The content is correct once the symbols are defined as above. As written the display is underdetermined, and its remainder claim is wrong for a T-independent μ.

### G4-3: λ_{I,w} is neither the internal relaxation rate nor the Laplace stiffness, so hypothesis (b), (A3) and t_int ∼ m_I^{−1} use the wrong quantity

**Location:** PIFB2.tex:3682-3685 (`eq:rg_constrained_gap`, m_I), 3702 (hypotheses b and d), 3740 (A3), 3934 (t_int ∼ m_I^{−1}), 3861 (||H^{−1}|| ≤ m_I^{−1}).

**Severity:** medium

**Evidence:** λ_{I,w} minimizes ξᵀLξ/ξᵀξ, with a Euclidean norm, over the barycentric hyperplane wᵀξ = 0. Three distinct quantities are involved.

(1) Dynamics. The fast flow ẋ = −g^{−1}Lx/ε, with g the child metric (Fisher blocks in natural-gradient descent), relaxes at the nonzero generalized eigenvalues of (L, g). These do not depend on w. `G4_slow_metric.py` part c3, weighted K₄: with g = 1 the slowest internal rate is 4.000 for every w, while λ_{I,w} = 1.523 for w = (0.97, 0.01, 0.01, 0.01), an underestimate by a factor of 2.6. With g = (1, 2, 0.5, 1.5) and uniform w, λ_{I,w} = 4.000 overestimates the true rate 2.582. The two agree (2.581868) exactly when w ∝ g and the fiber is measured in the g-norm.

(2) Statics. The coarea fiber integral of exp(−ξᵀLξ/2T) with the normal-Jacobian factor is √n (2πT)^{(n−1)/2} det'(L)^{−1/2}, independent of w (`G4_constrained_gap.py` part 4, relative residual ≤ 1.1×10⁻¹⁵).

(3) Anharmonic control. λ_{I,w}λ_min(F) is the smallest eigenvalue of the fiber Hessian in Euclidean fiber coordinates. It legitimately bounds ||H^{−1}|| at 3861, and that is its only correct role.

Two further points. Under natural-gradient descent, H ≈ L⊗F and G ≈ I⊗F give rates eig(L)⊗1, independent of F, so m_I = λ_{I,w}λ_min(F) is a stiffness, not a rate. And in "Fisher-normal coordinates around q_I" (3674) F(q_I) = I by construction, so λ_min(F(q_I)) = 1 there; the formula for m_I mixes coordinate systems.

**Fix:** At 3685 and 3934 write: "The internal relaxation rate is t_int^{−1} = η_q λ₂(L_I; W_g), the smallest nonzero generalized eigenvalue of L_I v = λ W_g v with W_g the child metric weights (for equal Fisher blocks, η_q λ₂(L_I)). The constrained quantity λ_{I,w}λ_min(F) bounds the inverse fiber Hessian in Euclidean fiber coordinates and controls the Laplace remainder. The two coincide when w_i^I ∝ g_i and the fiber carries the g-norm." Restate (b) and (A3) with λ₂(L_I; W_g), and drop λ_min(F) from m_I, or state the coordinates in which F ≠ I.

**Falsifies:** An implemented dynamics that holds the barycenter fixed while internal modes relax (a constrained flow). PIFB2's flow (929-1005) does not.

**Status:** D. "Relevant stiffness" at 3683 and "t_int ∼ m_I^{−1}" at 3934 misidentify the quantity; this is inflation of a definitional choice into a dynamical claim.

### G4-4: "Parametrically smaller" and "only for uniform weights" are overstated; an interlacing bound limits the effect to a factor |I|·||w||²

**Location:** PIFB2.tex:3685 (sentence after `eq:rg_constrained_gap`).

**Severity:** low

**Evidence:** Proof. Write ξ = a𝟙/√n + η with η ⊥ 𝟙. The constraint gives a = −√n wᵀη = −√n (w − 𝟙/n)ᵀη, so ξᵀξ ≤ (1 + n||w − 𝟙/n||²)|η|² = n||w||²|η|², while ξᵀLξ = ηᵀLη ≥ λ₂|η|². Cauchy interlacing gives the upper bound. Hence

λ₂/(n||w||²) ≤ λ_{I,w} ≤ λ₂, and since n||w||² ≤ n, λ_{I,w} ≥ λ₂/|I|.

`G4_constrained_gap.py`: 2000 random connected graphs with n ≤ 8 and Dirichlet weights show 0 violations. Fully concentrated weights give ratios λ_{I,w}/λ₂ as follows. On the complete graph K_n the ratio is exactly 1/n (0.3333, 0.2000, 0.1000, 0.0500, 0.0250 for n = 3, 5, 10, 20, 40), so the lower bound is attained. On the star with the weight on a leaf the ratio tends to 1/n. On the path and the cycle it tends to 1/4. On the star with the weight on the hub the ratio is 1.0000. On P₃ with the nonuniform symmetric weights (0.1, 0.8, 0.1) and (0.45, 0.1, 0.45), λ_{I,w} = λ₂ to 12 digits. So "reduces to λ₂(L_I) only for uniform weights" is false, and the ratio can tend to 0 only as the cluster size grows.

**Fix:** "λ₂(L_I)/(|I|·||w||²) ≤ λ_{I,w} ≤ λ₂(L_I), with equality on the right for uniform weights (and also for some nonuniform ones, e.g. symmetric weights on a path); concentrated weights can lower the constrained gap by at most a factor |I|."

**Falsifies:** A connected graph and a nonnegative normalized w with λ_{I,w} < λ₂/(n||w||²). The proof above excludes one.

**Status:** D (proved here); the manuscript's sentence is S-grade and overstated.

### G4-5: The graph-pullback versus quotient-metric statement is correct, but the manuscript omits the concrete condition, the Loewner ordering, and the fact that under (A4) the barycenter fibers are not the Fenichel fibers

**Location:** PIFB2.tex:3702-3712 (`eq:rg_slow_graph_metric`, G_quot, equality condition), 3572 ("agrees with the graph pullback only under the compatibility condition stated below"), 3740 (A4), 3934.

**Severity:** medium

**Evidence:** (1) Identity. G_slow(D) − G_quot = (D − C*)ᵀ G_ξξ (D − C*) with C* = −G_ξξ^{−1}G_ξY, obtained by completing the square (residual 8.9×10⁻¹⁶, `G4_slow_metric.py` c1). So G_quot ⪯ G_slow always, and the two agree to O(ε) only if ||Dξ* − C*|| = O(ε^{1/2}).

(2) Fenichel check on a linear two-timescale gradient flow (m = 2 slow, r = 3 fast, random SPD metric G with G_Yξ ≠ 0). The exact slow invariant subspace ξ = S_εY satisfies ||S_ε − C||/ε = 0.778, 0.766, 0.764, 0.764 for ε = 10⁻¹ to 10⁻⁴, so it is O(ε)-close as claimed. The slow eigenvalues predicted by G_slow(C)^{−1}B have error 6.3×10⁻³ down to 6.5×10⁻⁶ (O(ε)). Those predicted by G_quot^{−1}B have error 1.01, which is O(1). The manuscript's choice of the graph pullback is therefore right.

(3) Barycentric chart, which is the chart the RG uses. Write x_i = Y + ξ_i with Σ w_iξ_i = 0 and child metric diag(g). At consensus Dξ* = 0, G_slow = Σg_i and G_quot = 1/Σ(w_i²/g_i). By Cauchy-Schwarz they are equal if and only if w ∝ g. The script gives 5.000 against 5.000, 3.840 and 1.917 for w ∝ g, uniform w and concentrated w respectively.

(4) Fibers. Because the internal energy is translation invariant, the fast flow conserves Σg_ix_i. The Fenichel (stable) fibers are therefore level sets of the g-weighted mean, not of the w-barycenter. In the example, x₀ relaxes to consensus 0.29, which equals the g-mean, while the w-barycenter of x₀ is 0.88. (A4) fixes w ∝ r (edge marginals), which is generically not proportional to g. The static coarse-graining map R_s then assigns a non-equilibrated cluster a parent state that the dynamics does not reach. The mismatch is of order ||ξ||·||w − g/Σg||.

**Fix:** After G_quot at 3709 add: "G_slow − G_quot = (Dξ* − C*)ᵀG_ξξ(Dξ* − C*) ⪰ 0. In the barycentric chart with child metric weights g_i, G_quot = G_slow if and only if w_i^I ∝ g_i; the same condition makes the barycenter fibers coincide with the linearized Fenichel fibers and makes the metric block diagonal. Under (A4) the weights are fixed by edge marginals instead, so the parent assigned by R_s to a cluster off the slow manifold differs from the dynamically reached parent at first order in the internal displacement."

**Falsifies:** A nonlinear internal energy in PIFB2 that is not invariant under common translation of the children in the chart, so that Σg_ix_i is not conserved. The KL alignment energies are invariant to leading order in Fisher-normal coordinates.

**Status:** The manuscript's statement is D and correct. The missing condition and the fiber mismatch are D here.

### G4-6: The four adiabatic-elimination hypotheses are partly vacuous and name the wrong fast operator; the Fenichel hypotheses are not all stated

**Location:** PIFB2.tex:3702 (hypotheses a-d), 3934.

**Severity:** low

**Evidence:** (a) "G_ξξ is invertible" is automatic for a Riemannian ambient metric, since a principal block of an SPD matrix is SPD (G_ξξ eigenvalues 1.09, 5.36, 9.22 in the toy). (b) and (c) require positivity, which is automatic for a connected cluster graph because λ_{I,w} ≥ λ₂/(n||w||²) > 0 (G4-4). "λ_{I,w} > 0" therefore does not separate internal from retained modes. The separation is carried entirely by ε_ts ≪ 1, and ε_ts must use the correct fast rate.

For the gradient flow ż = −G^{−1}∇F with stiff internal energy (1/2ε)(ξ − CY)ᵀA(ξ − CY), the transverse (layer) rates are eig(A N G^{−1} Nᵀ)/ε with N = [−C, I]. `G4_slow_metric.py` c1: the predicted values 0.538, 1.123 and 26.90 match the exact rates to 7×10⁻⁵ at ε = 10⁻⁴. The frozen-Y operator G_ξξ^{−1}A gives 0.145, 0.590 and 7.75. When G_Yξ ≠ 0 the stiff force also moves Y at rate O(1/ε), so "internal modes at frozen parent" is not the layer problem.

Fenichel's theorem additionally needs a smooth one-parameter singularly perturbed family, a compact normally hyperbolic piece of the critical manifold (hence "locally invariant"), and C^r data. The manuscript states only the second, implicitly. L07-3 raises the same omission for the body section 963-965. The Theory's `open:obs-slow-manifold` (`c08_two_timescales.tex:251-275`) assumes a block-diagonal metric G_f ⊕ G_s. In the barycentric chart that holds if and only if w ∝ g (G4-5).

**Fix:** Replace (a)-(d) at 3702 with the Theory's three hypotheses (C², block metric in a chart with G_slow independent of the fast coordinates, a compact slow region with uniform fast curvature ∂²_ff F ⪰ c₁G_f), and define ε_ts through the smallest layer rate eig(A N G^{−1} Nᵀ), or through λ₂(L_I; W_g) in the chart w ∝ g. Cite `open:obs-slow-manifold` for the open application.

**Falsifies:** A metric for which G_ξξ is singular (only at the dexp-singular locus, `prop:dexp_regularity`, which the paper already excludes).

**Status:** P by citation (Fenichel 1979), conditional; the hypothesis list is incomplete and partly vacuous.

### G4-7: Units in the reduced flow and the closure diagnostics

**Location:** PIFB2.tex:3660-3667 (`eq:rg_closure`, `eq:rg_closure_dimensionless`), 3715-3720 (`eq:rg_schur_flow`), 3685 (m_I).

**Severity:** low

**Evidence:** Dimensional check, analytic. F_s is built from KL divergences, so it is measured in nats. T_cfg therefore carries F's unit, and it is a dimensionless tempering exponent if F is in nats. δ_{I,0} carries F's unit, and so does c_I^Z (correct). δ_{I,1} is in F-units per unit G_slow-length (correct). ε_I is dimensionless and invariant under F^exact → F^exact + c, because c_I^Z shifts by the same c (correct).

`eq:rg_schur_flow` is not dimensionally closed. Ẏ is a rate, while −grad_{G_slow}F̂ has units F/(G-length²) × length. The mobility η (η_q, η_s or η_φ of 939-951) is missing, and so is a velocity scale in ||R_ts|| = O(ε_ts). Numerically, the calibrated residual obeys δ^quot_{I,0} ≤ δ_{I,0} ≤ 2δ^quot_{I,0}: over 2000 random neighborhoods the ratio ranged from 1.000001 to 2.000000 (`G4_slow_metric.py` d2). Proof: c_I^Z = T log E_exact[e^{D/T}] lies in [inf D, sup D] with D = F^exact − F^agent. The manuscript does not state this bound, and it is the natural bridge between its two residuals.

**Fix:** Write Ẏ_I = −η grad_{G_slow}F̂ + R_ts + R_cl with ||R_cl||_{G_slow} ≤ η δ_{I,1} (after G4-1) and ||R_ts||_{G_slow} = O(ε_ts)·η||dF̂||_{G_slow^{−1}}. Add "δ^quot_{I,0} ≤ δ_{I,0} ≤ 2δ^quot_{I,0}". Set E_ref := T_cfg unless another scale is intended.

**Falsifies:** A convention stated elsewhere that sets η = 1 and measures time in units of 1/η.

**Status:** D (dimensional analysis and a proved inequality).

### G4-8: det' in eq:rg_laplace should be the pseudo-determinant (kernel = common translation); the normal Jacobian in dH_Y cancels the constraint factor, which refines the fix proposed in L06-6

**Location:** PIFB2.tex:3690 (`eq:rg_laplace`), 3637 (dH_Y "including the normal-Jacobian factor"); cross-reference L06-6.

**Severity:** low

**Evidence:** det(L|_{w⊥}) = det'(L)/(n||w||²) (`G4_constrained_gap.py` part 4, exact to 10 digits in three random trials). This is L06-6's c(w). The coarea density, however, carries the normal Jacobian 1/||∇R|| = ||w||^{−K}, and that factor cancels the constraint determinant exactly. The fiber integral is √n (2πT)^{(n−1)/2}det'(L)^{−1/2} for every w (relative residual ≤ 1.1×10⁻¹⁵). With the manuscript's dH_Y, the pseudo-determinant det' is therefore the correct object. L06-6's recommendation to "replace det' by the determinant on the constraint subspace" would add a spurious term (KT_cfg/2) log(n||w(Y)||²). Under (A4) the weights w ∝ r(Y) depend on the state, so that term is Y-dependent. L06-6's main result (the entropy-weight shift) is unaffected.

**Fix:** At 3690: "det' denotes the product of the nonzero eigenvalues of H_I^⊥ on the full internal space, whose kernel is the common translation 𝟙 ⊗ ℝ^{K}; with the normal-Jacobian factor of dH_Y this is independent of the barycentric weights."

**Falsifies:** A reading of dH_Y as the induced fiber Lebesgue measure without the normal Jacobian, contradicting 3637.

**Status:** D (proved and computed here).

## Verified, no defect (ledger candidates)

**Direct-quotient and Faddeev-Popov prescriptions are alternatives (3554).** On the SO(2) saddle with slice a₂ = 0 and FP = |a₁|, FP²/det H_slice = Gram/det H_h = 0.0105705922 (relative residual 0.0). Keeping both the FP factor and Γ_measure would add −T log|a₁| (0.055 T here), so "must not be multiplied together" is correct. Script `G4_quotient_one_loop.py` Part A.

**Quotient one-loop formula with μ² = 2πT and Γ_measure = −(T/2) log det Gram.** Remainder O(T²): residual/T² → −0.145 (SO(2), n_phys = 3) and → 0.182 (GL⁺(2) on (μ, Σ), n_phys = 1) for T from 0.2 to 0.0125. Script `G4_quotient_one_loop.py`.

**Γ_measure is finite in the noncompact case with an invariant (Fisher) metric.** det Gram is constant along GL⁺(2) orbits (5.499008264463 at three random group elements). The Weil density equals sqrt(det Gram)·sqrt(g_uu) to 10⁻¹⁰, and the raw invariant integral diverges as vol_Haar (Weil formula, analytic). This supports "Raw Haar integration ... is not admissible" and "quotient or gauge fixing" (3554) and the Remark at 3630. Script `G4_quotient_one_loop.py` Part B.

**Graph-pullback metric as the Fenichel slow metric (3704, 3934).** ||S_ε − C|| = O(ε) with constant 0.764. Slow spectrum error O(ε) with G_slow and O(1) with G_quot. Identity G_slow − G_quot = (D − C*)ᵀG_ξξ(D − C*), residual 8.9×10⁻¹⁶. Script `G4_slow_metric.py` c1.

**Constrained-gap interlacing bound λ₂/(n||w||²) ≤ λ_{I,w} ≤ λ₂.** Proof in G4-4; 0 violations in 2000 trials; attained on K_n. Script `G4_constrained_gap.py`.

**Constraint determinant and coarea cancellation.** det(L|_{w⊥}) = det'(L)/(n||w||²); the fiber integral is w-independent (≤ 1.1×10⁻¹⁵). Script `G4_constrained_gap.py`.

**Calibrated residual.** δ^quot_{I,0} ≤ δ_{I,0} ≤ 2δ^quot_{I,0} (ratio range [1.000001, 2.000000] over 2000 trials; proof in G4-7). ε_I is shift invariant (analytic). Script `G4_slow_metric.py` d2.

**Connected propagator G^{AB} = T(Γ^{(2)})^{−1} and the Legendre convention (3530-3541).** Already verified by L05 (`L05_nested_effective_action`); not recomputed.

**2PI paragraph (3556).** The description of the double Legendre transform and stationarity δΓ₂/δG = 0 matches Cornwall-Jackiw-Tomboulis, and "proposed completion" is correctly fenced. Method: reading against the standard construction; no script.

## Physics-audience and standalone notes

A field theorist reading Appendix H will look for three things the text names but does not display. The first is an explicit gauge fixing. One sentence with a worked slice would anchor the discussion: for the global right-translation redundancy (a) of 3642, fix U₁ = 1, which is a global slice with unit Faddeev-Popov determinant because the action is free and transitive on the first factor. That example also shows why action (a) never produces Gribov copies, while slices for the base-local action (b) can. The second is the Faddeev-Popov determinant, or equivalently the orbit-volume density, written as −(T/2) log det 𝒢_{ab} (G4-2). The third is the count of physical modes: n_phys = dim X − dim G_red + dim Stab(X̄), which enters through the (n_phys/2) T log(2πT) term and matters whenever backgrounds on different strata are compared, as Appendix I's "fixed-dimensional positive-weight strata" do.

The symbol μ² in `eq:beyond_mf_one_loop` will be read as a renormalization scale. There are no ultraviolet divergences in this finite-dimensional integral, nothing is renormalized, and the Appendix I "RG" is not a flow in μ. Write 2πT_cfg instead.

"Γ₂[φ, G]" for the full 2PI effective action clashes with the CJT convention, where Γ₂ is the sum of 2PI vacuum graphs inside Γ[φ, G]. Rename it Γ[φ, G] or Γ_{2PI}.

"Massive" for m_I (3685) is field-theory usage for a Hessian eigenvalue, but m_I has the dimension of a mass squared (an inverse susceptibility) and is a stiffness, not a rate (G4-3). "Fisher-normal coordinates" should be defined once as Riemannian normal coordinates of the Fisher metric at q_I.

For the adiabatic-elimination paragraph, a physicist will recognize the Mori-Zwanzig or Born-Oppenheimer structure. What is needed is the statement that the reduced deterministic dynamics follows the zero-temperature profile, whereas the Gibbs pushforward carries the fluctuation determinant (G4-1). Stated this way the free energy is not confused with the potential that drives the flow, which is the standard pitfall in coarse-grained molecular dynamics (potential of mean force versus minimum-energy path).

For length, Appendix H's effective-action subsection is compact and standard. With G4-2's definitions it can stay as is. The Appendix I Fenichel material (3701-3720, 3933-3934) could be reduced to one paragraph that states the Theory's hypotheses and cites `open:obs-slow-manifold`.

## Complementarity notes

At 3701-3720 and 3934, cite Theory `c08_two_timescales.tex`, `open:obs-slow-manifold`, for the exact hypotheses (C², block metric with G_s independent of f, compact region with uniform fast curvature) and for the open status. PIFB2's barycentric chart satisfies the block-metric hypothesis only when w ∝ g (G4-5, G4-6).

For the force residual (G4-1), the exact dynamical object is the semiconjugacy defect δ_t = ∂_tF_t + DF_t𝒱_t − 𝒱̄_t∘F_t of Theory `c11_network_coarsegraining.tex`, `open:rg-pointwise-parent-dynamics` (`eq:rg-pointwise-parent-semiconjugacy-defect`). Defining R_cl as that defect with 𝒱̄ = −η grad_{G_slow}F̂ removes the finite-temperature error.

For the static pushforward (3636-3638), Theory `c11`, `thm:rg-effective-action` (conditional-partition formula with a proper reference probability), is the rigorous counterpart. It sidesteps the quotient-measure issues of G4-2 by never using an improper reference.

No conflict with a Theory result was found in this scope. All recommendations are PIFB2-side.

## Not covered

I did not compute the one-loop formula at a background with a nontrivial stabilizer (orbifold point), where Γ_measure diverges logarithmically. The GL⁺(K_q) frame sector with the paper's Frobenius-pullback metric was treated only through the invariance failure (reused from L07-5), not with a one-loop computation. The Bethe/Kikuchi paragraph (3474-3493), the nested identity (3441-3457) and the propagator identity were left to L05, which verified them. I did not check the inter-cluster conductance paragraph (3692-3699), the retention rules (3722-3727), Propositions `thm:rg_residual` and `thm:rg_residual_explicit` (3805-3912), or the anharmonic coefficients (L06 verified them). No citation was checked against its primary source by this lens.
