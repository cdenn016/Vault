# C14 change log (original lines 3569-3956: Appendix I, notation, bibliography commands)

Edited file: `remediation/chunks/C14.tex` (CRLF preserved). A scratch build of the chunk under the original preamble compiled with no LaTeX errors (undefined cross-chunk references expected); one 5 pt overfull display was fixed. Verification scripts re-run for numbers placed in the text: `L06_karcher_semigroup.py` (7.309e-3 two-stage versus one-stage Karcher gap; H_IJ spread 4.5e-16; Afsari radius pi/sqrt2 in d_G), `L06_oneloop_logdet.py` (3.6e-15), `G4_slow_metric.py` (R_cl = 0.100000 = T k/2 with delta = 0; Loewner identity 8.9e-16; calibrated-residual ratio in [1, 2]; g-mean 0.29 against w-barycenter 0.88), `L06_laplace_detector.py` (1/8, 5/24; self-loop -1.732334 against -1.429181). All reproduced the panel values. Every Theory statement cited was read in `MultiAgentELBO/Theory/` (c01 l.172-186, c02 l.87-150, c03 l.544-555, c06 prop. attention-reduced potential, c08 l.251-275, c09 l.131-175, 378-395, 429-445, 470-487, c10 l.395-405, c11 l.47-135, 589-640, 718-735, 816-870, 1064-1075, g07 l.234-240 and 561-580, g09 l.55-95).

## 1. Items

| Item | Disposition | Reason or description | New line or label |
| --- | --- | --- | --- |
| M11 retitle | applied | Section retitled "Exact Coarse-Graining for Meta-Agent Formation"; subsection retitled "Statements and Proofs"; all "RG" and "renormalized free energy" wording replaced by coarse-graining terms | l.1, l.192; `sec:meta_agent_rg`, `app:rigorous_rg` kept |
| M11 relation to physicist's RG (D4a) | applied | Opening paragraph: Kadanoff block-variable map without rescaling, no coupling-space flow or fixed point, finite tower of at most log_b N levels, Theory Ch. 1 and Ch. 11, Supplement B Chs. B5-B6; Kadanoff 1966, 1975, KHY 1976 cited | l.4 |
| M11 / L06-2 closure theorem | applied | `thm:rg_exact_closure` restated as Lemma "Mean-sector Gaussian elimination" (mean-only linear map, fixed covariances, frames, couplings; with source and constant; short proof; cites Supp. G Ch. G7). Remark explains why (A6) is unsatisfiable for the map retaining Sigma_I (bounded fibers, one-line derivation) or empty under arbitrary charts (triangular transport), and why a Y-dependent log det does not close; (A1)-(A5) idle hypotheses removed from the statement | lemma at l.~275; label kept |
| M11 / L06-3 H_IJ = 0 in Regime I | applied | Derivation Theta = U_I U_J^{-1}; H_IJ is a closure error only with independent links; Theory Ch. 10 for the law-level case; C_2 term flagged as vanishing in Regime I; (A7) dropped | `eq:rg_holonomy_trivial` |
| M11 / L06-4 negative semigroup statement | applied | Belief sector composes (mixture of mixtures); Karcher frame mean does not (nonlinear Karcher equation; SO(3) witness 7.3e-3, rerun); Theory Ch. 9 cited for "no condition on a chain" | paragraph after `thm:rg_semigroup` |
| M11 / L06-6 one-loop coupling shift | applied | Derived log det'(L tensor Sigma^{-1}) = K_q log det'L - (|I|-1) log det Sigma_I; shift of the entropy weight by -(|I|-1)T_cfg/2; states that fixed coefficients across levels hold only by assumption | `eq:rg_entropy_shift` |
| M11 / G4-8 det' | applied | det' kept and defined as the pseudo-determinant on the full internal space with kernel the common translation; w-independent with the normal Jacobian. L06-6's determinant replacement not adopted | text after `eq:rg_laplace` |
| M11 / L06-7 C_1 | applied | `eq:rg_C1_explicit`, the Pinsker-Edgeworth composition and the Hermite-threshold hypothesis deleted; proposition retitled "Two-loop anharmonic constants, one internal mode" with a short proof; C_1 in the schematic bound declared underived | `thm:rg_residual_explicit` kept |
| M11 / L06-1 / L18-11 Wilsonian relevance at 3723 | applied | Relevance paragraph replaced: no self-map, no declared comparison map, finitely many steps, no comparison identification for finite agent spaces (Theory Ch. 11); asymptotics deferred to Supplement B | "Retention" paragraph |
| M11 / G2-1 pushforward | applied | Conditional-partition formula with the pushed reference stated first (Theory Ch. 11); a declared parent reference adds -T_cfg log(d nu^c / d nu_{l+1}); coarea display kept only as the smooth-density representation used for the Laplace step | `eq:rg_conditional_partition` (new), `eq:rg_exact_free_energy` kept |
| M11 Theory citations (Ch. 9, Ch. 11) | applied | Pushforward, composition, functoriality, residual identity, hyperedge generation, meta-attention pushforward, semiconjugacy defect cited by chapter | throughout |
| G2-1 cut theorem block to a paragraph | partially applied | Spec sets no word target; theorems kept (they are correct), with Theory citations added and the underived material removed | n/a |
| D8(b) sigma-finiteness sentence (3633-3639) | applied | Deleted; replaced by the correct statement that the pushed reference is a probability measure and the density is the conditional expectation E_nu[e^{-F/T} given R = Y] | "Exact pushforward" paragraph |
| M12 / G4-1 force residual | applied (option i) | delta_{I,1} redefined against the zero-temperature profile F_eff; bound ||R_cl|| <= eta delta_{I,1} derived by the envelope identity; counterexample F = bY^2/2 + a_0 e^{kY} xi^2/(2 eps) stated; R_ts + R_cl identified as the Theory Ch. 11 semiconjugacy defect | `eq:rg_closure`, `eq:rg_zero_temperature_profile` (new), `eq:rg_schur_flow` |
| M12 / G4-3 lambda_{I,w} is not the relaxation rate | applied | m_I described as stiffness (inverse susceptibility) bounding ||H^{-1}||; relaxation rate t_int^{-1} = eta lambda_2(L_I; W_g) stated separately; "Fisher-normal coordinates" replaced by native coordinates so F(q_I) = Sigma_I^{-1} in the mean sector | text after `eq:rg_constrained_gap` |
| M12 / G4-4 "parametrically smaller" | applied | Interlacing bound with proof replaces the overstated sentence | `eq:rg_gap_interlacing` (new) |
| M12 / G4-5 Fenichel fibers | applied | Loewner identity G_slow - G_quot = (D xi* - C*)^T G (D xi* - C*); block-diagonal iff w proportional to g; fast flow conserves the g-weighted mean, so R_l's parent differs at first order under edge-marginal weights | "Adiabatic elimination" paragraph |
| M12 / G4-6 Theory slow-manifold hypotheses | applied | Hypotheses (a)-(d) replaced by the Theory Ch. 8 hypotheses (a)-(c) plus Fenichel's smooth-family and compact normally hyperbolic conditions; open status stated | "Adiabatic elimination", "Slow manifold" |
| M12 / G4-7 mobility and units | applied | Mobility eta inserted in `eq:rg_schur_flow`; R_ts scale stated; delta^quot <= delta_{I,0} <= 2 delta^quot proved in one line; E_ref = T_cfg default | `eq:rg_schur_flow`, text after `eq:rg_closure` |
| M13 / G1-1 / G3-1 / L06-10(c) Karcher radius at 3762 | applied | G1-1 replacement: global uniqueness below r_cx = (1/2) min{inj G, pi/sqrt Delta} (Afsari Thm 2.1), pi/sqrt2 in d_G (rotation angle pi/2); Kendall's radius attributed to the ball-restricted mean; "which also lies below the injectivity radius" deleted; "locally unique" replaced by "unique" | "Coarse-graining map" paragraph |
| G1-2 frame hypothesis | partially applied | In C14: radius condition added to the candidate-cluster conditions and to (A5); stated that gauge-invariant weights and detector cannot see frame spread; frame-free parent pair shown U_I-independent (one-line derivation). The Definition itself is in C06 | cross-chunk note 4 |
| L14-1 / L15-5 / L16-1 missing keys at 3762 | moot | `Kendall1990` and `Afsari2011` now exist in references.bib (bibliography agent) | n/a |
| G3-7(b) Cardy pins | applied | Unverified Cardy pins for the Radon-Nikodym form and the Laplace step removed; Laplace step cited to Wong, pushforward to Theory Ch. 11 | l.4, "Integrating out" sentence |
| G3-7(c) / L14-5 Kadanoff | applied | Kadanoff 1966, Kadanoff 1975, Kadanoff-Houghton-Yalabik 1976 cited at the block-variable statement; Machta, Berman and van Enter at 1683-1685 belong to C07 | l.4 |
| 3578 / G2-7 scoping sentence | applied | Remark lists the five Theory Ch. 3 conditions; the lift supplies (i)-(ii), the Haar paragraph addresses (iii), (iv)-(v) open | `rem:gibbs_lift_interpretation` |
| 3694 / L18-10 | applied | "must be constructed" removed; pooling identified as the exact block row of the single-edge label model; per-receiver model and edge-event law stated (Theory Ch. 11) | text after `eq:rg_inter_cluster` |
| 3705-3707 / L06-11 self-loop | applied | Sum over L includes L = I; kappa^R_II is an effective parent self-loop; identical-children identity requires it (script: -1.732334 with, -1.429181 without) | text after `eq:rg_inter_cluster` |
| 3806 / G2-6 / L06-10(a),(b) covariance theorem | applied | Stated at one base point for the diagonal action of one g; proof via left invariance; extends to any Lie group with a left-invariant metric; compactness only for the reference measure; "frame-consistent, not uniquely correct"; Theory Ch. 9 hypothesis verified; Theory Ch. 10 for holonomy | `thm:rg_covariance` |
| D4(b) gauge vocabulary (3641-3643) | applied | Actions (a)/(b) paragraph rewritten with the trichotomy passive re-expression, change of reference, active group (one copy of G, Theory Ch. 2); the false sentence that per-agent transformations are "active changes" and the "index-space lattice gauge" sentence removed | "Gauge actions at one base point" |
| 3913-3940 / L05-5(b) detector summary | applied | Body detector stated as not covered; summary no longer calls it a sufficient surrogate; "reference implementation" removed | detector paragraph, Summary |
| M14 / L05-4 A_I > 0 | applied | New remark: sign argument (unnormalized and renormalized priors) shows deleting coherent intra-cluster sources raises row values; A_I = T_cfg m_I not derived; hypothesis open; theorem retitled "conditionally" | `rem:rg_detector_saving` (new), `thm:rg_detector_retention` kept |
| M14 / L18-2 exact-parent degeneracy | applied | Retention paragraph: under an exact parent the free-energy decrease is discarded conditional information (Theory Ch. 9); no cost selects a partition | "Retention" |
| 3935-3937 finite-size scaling | applied | Exponents in N declared as own quantities (a_M, a_S, b), lattice relation given with hatted standard exponents (no beta/gamma collision); susceptibility is the mean cluster size (percolation convention); infinite networks to Supplement B | "Finite-size scaling" |
| Notation (3942-3953) / L16-2, L16-3, L16-5, L16-7, D3 | applied | Rewritten as a symbol table: l for level, vartheta_i clock, beta_W, (q)/(s) channel decorations, D_KL, T_cfg; transformer-only symbols (PriorBank, Renyi alpha, attention compatibility M, kappa factorization) and the software optimizer sentence removed; false "(s) never competes" rule removed | `tab:notation` (new), `sec:notation` kept |
| L16-6 notation collisions | partially applied | Table disambiguates Omega_{ij}, Omega_{Ii}, T_3/T_4 against T_cfg; the column marginal s_j renamed r-bar_j (collided with the model section); Omega_gamma/Gamma_gamma and T_ab fixes lie in other chunks | table; "Edge-marginal compatibility" |
| L03-2 forward/reverse naming | applied | "forward-KL" removed from the chunk; "M-projection (moment-matching) barycenter" used | throughout |
| D3(a) level index | applied | Every scale s became l (X_l, I_l, F_l, nu_l, Z_l, P_l, Lambda_l, R_l, N_{l+1}, delta_{l+1,0}) | throughout |
| D3(e) model-channel collision in App. I | applied | The appendix's second fiber p_i = N(m_i, Pi_i) (which collided with the prior p_i) renamed to the model section s_i; V^(p), tau_p, C_p, L_p became V^(s), tau_s, C_s, L_s; the reconciliation sentence deleted | throughout |
| D3(d) typography | applied | \mathrm{KL} replaced by D_KL in the chunk | throughout |
| D2 status language | applied | No Level/fence text was present; statuses stated in words (proved, derived here, conjectural, open) with a pointer to Table tab:claim_status | l.6, Summary |
| D7 transformer removal | applied | Notation references to `sec:transformers` (PriorBank, Renyi order) removed | notation table |
| D9 software content | applied | "reference implementation", "optional optimizer path", "working implementation" factorization removed | n/a |
| D13 style | applied | No banned words, no spacing macros, no "rather than" in the chunk; display punctuation checked | n/a |
| L16-10 label prefixes (thm:rg_residual, thm:rg_residual_explicit) | not applied | D14: do not rename labels unless required; environments are propositions and text says "Proposition" | n/a |
| L17-11 three conclusions | not applied | The appendix "Summary" is an appendix summary, not a conclusion; kept and corrected | Summary |
| G4-2 (App. H one-loop display) | moot | Lies in C13 | n/a |

## 2. Labels removed

- `eq:rg_C1_explicit` (the underived C_1 display). Grep of `PIFB2.orig.tex` finds no reference to it anywhere.

## 3. Labels added

- `eq:rg_conditional_partition`, `eq:rg_zero_temperature_profile`, `eq:rg_gap_interlacing`, `eq:rg_entropy_shift`, `eq:rg_holonomy_trivial`, `rem:rg_detector_saving`, `tab:notation`.

## 4. New bib keys needed

None. All keys cited in the chunk exist in `references.bib` (checked after the bibliography agent's additions): `DennisGaugeVFE2026`, `DennisGaugeVFESuppG2026`, `DennisGaugeVFESuppB2026`, `Kadanoff1975`, `KadanoffHoughtonYalabik1976`, `Kendall1990`, `Afsari2011`, plus pre-existing `kadanoff1966scaling`, `Karcher1977`, `wong2001asymptotic`, `HornJohnson2013`, `fenichel1979geometric`, `Wilson1971`, `Wilson1974`, `Schwarz1978`, `Rissanen1978`, `BissiriHolmesWalker2016`, `Amari2016`, `BenderOrszag1999`. `Cardy1996` and `CoverThomas2006` are no longer cited from this chunk.

## 5. Cross-chunk notes

1. `thm:rg_exact_closure` is now a **Lemma** ("Mean-sector Gaussian elimination"). C07 at 1683 cites it as "Theorem" and as closure into the quadratic-plus-log-determinant class; it should read "Lemma~\ref{thm:rg_exact_closure}" and describe only mean-sector Gaussian elimination at fixed covariances, frames, and couplings.
2. C02 at 694 ("The same lambda_h appears at every scale"): the exact pushforward shifts the parent's entropy weight by -(|I|-1)T_cfg/2 log det Sigma_I at one loop (`eq:rg_entropy_shift`); C02 should say the coefficients are held fixed across levels by assumption and cite this equation.
3. Claim-status table (C00, `tab:claim_status`): exact closure theorem becomes "mean-sector Schur lemma, P"; schematic residual bound, C; detector-retention theorem, P as a conditional statement with an open hypothesis A_I > 0 (no identified source), body detector not covered; one-loop entropy shift, D; force-residual bound, D against the zero-temperature profile (the finite-T version is false); covariance theorem, P at one base point for one global g, extends to left-invariant metrics; Karcher uniqueness radius, P with r_cx = pi/sqrt2 in d_G.
4. C06 (1573, 1577, 1580-1585, 1607-1633, 1644): use the same Karcher radius text (rotation angle below pi/2, Afsari Thm 2.1; Kendall's radius is for the ball-restricted mean); add the frame-radius condition to the Definition or declare U_I a convention and define the parent by the frame-free pair, whose U_I-independence is derived in the appendix "Coarse-graining map" paragraph; the body detector must not be called a sufficient surrogate, and `thm:rg_covariance` licenses the barycenter as "frame-consistent", not "the correct coarse-graining target". The body detector's model dispersion V^{(s)}_I should drop the scale superscript meaning (use l for level).
5. C07 (1679-1702): section title should drop "Renormalization-Group"; the relevance and fixed-point language is now superseded by the appendix "Retention" paragraph; 1683 can cite `eq:rg_inter_cluster` with the self-loop proviso.
6. The appendix now uses s_i for the model section (formerly p_i in App. I). Any body text that referred to the appendix's "(q, p) pair" should say (q, s).
7. Notation table (`tab:notation`, `sec:notation`, referenced at 92): C00 may move it to the front. The integration phase should prune entries whose symbols disappear after other chunks' edits (for example `M_{\mu\mu}`, `\mathcal{M}` if C05 changes; the p_i description once C07 recasts the shadow as the lagged predictive prior) and confirm vartheta_i (C09) and beta_W (C01) match. The table references `sec:mass`, `sec:cross_scale_shadows`, `sec:time_info`, `sec:timescales`, `sec:meta_agent_threshold`, `eq:transport_def`, `eq:pointwise_free_energy`; these labels must survive.
8. `Table~\ref{tab:claim_status}` is referenced from the appendix opening and must be created by C00.

## Integration pass

Integration editor model: Claude Opus 5.5. Checked against C00 (`tab:wheeler_correspondence`, `tab:claim_status`), the GENERAL and C14 integration notes, and the C13 boundary (C14 closes the document). The full assembly builds with latexmk: 0 errors, 0 undefined references, 0 undefined citations, 166 pages; one 0.9 pt overfull line in the functoriality theorem header.

### Notes applied or rejected

| Note (source) | Disposition | Reason or action |
|---|---|---|
| C00: Kadanoff block-variable citations reusable | applied (confirmed) | Opening paragraph cites kadanoff1966scaling, Kadanoff1975, KadanoffHoughtonYalabik1976 with the no-rescaling statement. |
| C02: one-loop entropy-weight shift must exist in `sec:meta_agent_rg`; `thm:belief_configuration_gibbs_lift` cited | applied (confirmed) | `eq:rg_entropy_shift` and the Gibbs-lift theorem are present. |
| C06 (3762): Afsari radius, drop the injectivity-radius clause, "unique"; `thm:rg_covariance` at one base point for one global g, left-invariant metrics | applied (confirmed) | Already in the coarse-graining-map paragraph and the covariance theorem. |
| C06 (3940): restrict the sufficient-surrogate claim to the gap-strengthened detector | applied (confirmed) | Summary and detector paragraph say the body detector is not covered. |
| C06 (3930): A_I > 0 has no identified source | applied (confirmed) | `rem:rg_detector_saving`. |
| C06 (general): drop "forward/reverse KL" at orig 3807, 3811 | applied (confirmed) | No such wording remains; "forward" occurs only in "pushforward". |
| C06 (general): `\mathcal{U}_I` support region, U_I parent frame | applied | Added to the notation table; C14 uses U_I only as the parent frame. |
| C07: keep `sec:meta_agent_rg`, `app:rigorous_rg`, `eq:rg_inter_cluster`, `thm:rg_covariance`, `thm:rg_exact_closure`; one-loop sentence; left-invariant extension | applied (confirmed) | All present. |
| C09: notation (vartheta_i; t for P5; x^0..x^3 and psi_0..psi_3; G^(q) covariant Fisher block; widetilde G^(q) with declared kappa; L_0; tau temperature only) | applied | Table rows added or amended; the unindexed kappa row records its two declared uses (C09 horizontal coupling, C11 temperature scale tau = kappa sqrt(K_q)). |
| C11: notation (cond, duplication matrix, photon channel ph, SO(3) spin j); tau^(q)_ij sentence wrong | applied / moot | Rows added (App C is `app:math`, App B is `app:examples`); the tau^(q)_ij sentence no longer exists. |
| C11: right-translation paragraph cites `sec:gauge_covariance_principle` | moot for C14 | Concerns C11 only. |
| C12: c^(q)_ij, c^(s)_ij, W^(q), W^(s); Lambda_i, anchor A_i, strength a, map L on Sym(K)^N | applied | Rows added; App E has no section label, so the table cites `sec:raw_alignment_weights`; the anchor A_i is marked distinct from the saving term A_I. |
| C13: F^exact called the Wilsonian effective energy; notation for link kernel, p_top, T_ij, C_cons, Gamma_2PI | applied | Table rows added, with Gamma and Gamma_2PI marked distinct from the detector score Gamma_I and T_3, T_4 distinct from the sans-serif T_ij. C13 now calls F^exact "the coarse energy", C14's term, with the block-variable qualification. |
| C14 own note 7: prune stale table entries | applied | "M_{mu mu}, M_i; mathcal M" corrected to "M_{mu mu}, M_{Sigma Sigma}, M_i; M_K" (C05 uses M_K for the kinetic metric, `sec:velocity_quadratic`); the p_i entry names the lagged predictive prior; tau_gamma added; the so(K_q) Killing form (K_q - 2) tr(XY) used in C05, which is not the restriction of the gl(K_q) form, added; the false claim that no symbol is redefined locally removed. |

### Other edits

- Retired vocabulary: subsection title "Theorem-Level Statements" (contained "Level"; the original log's retitle had not been applied) renamed "Statements and Proofs", label `app:rigorous_rg` kept; "prior renormalized over the surviving sources" changed to "prior normalized again".
- Dated phrasing: "no cost analyzed so far" changed to "no cost analyzed in the companion theory".
- Tightening: the Statements-and-Proofs preamble no longer repeats the three-claim split and the pointwise, no-transport statement (both stated earlier). The independent-C^1 caveat on delta_{I,1} now stands in the working-form closure paragraph, the conductance paragraph, the residual preamble, and the Summary; its three further restatements (after the flow counterexample, after the schematic proposition, and in the slow-manifold paragraph, with the repeated epsilon_I remark) were deleted. The detector paragraph now points to Proposition `thm:rg_residual` for the residual contributions and says "is expected to admit", since the proposition is conjectural. The multi-partner colinearity sentence duplicated in the conductance paragraph now points to the edge-marginal paragraph. Assumption `ass:closure_regime` references conditions (i)-(v) instead of restating them. The raw-Haar pointer sentence became a parenthetical reference. The Summary was condensed and carries the status codes of `tab:claim_status` (P, D, C).
- Notation table converted from a floating `table`/`tabular` to `longtable` (loaded by C00), because it grew to about 45 rows.
- Words: 8,819 -> 8,859. About 300 words of prose removed and about 340 added in the notation table at other chunks' request. No result, proof, correction, or citation removed.

### Table changes needed in C00 (`tab:claim_status`)

Appendix I has two rows (Gibbs lift; exact coarse-graining). To match the appendix, add: mean-sector Gaussian elimination (Lemma `thm:rg_exact_closure`), P; gauge covariance of R_ell at one base point for one global g, extending to left-invariant metrics, P; composition holds in the belief sector and fails in the frame sector (Karcher), P with an SO(3) witness; one-loop entropy-weight shift (`eq:rg_entropy_shift`), D; force-residual bound against the zero-temperature profile, D (the finite-temperature version is false, counterexample in the appendix); schematic closure-residual bound (Proposition `thm:rg_residual`), C; strengthened-detector retention theorem, P as a conditional statement with open hypothesis A_I > 0, body detector not covered.

### Cross-chunk note

- C07 line 30 calls `thm:rg_exact_closure` "Theorem"; it is a Lemma in C14 and should read "Lemma~\ref{thm:rg_exact_closure}".

## Consistency fixes

- Issue 1 (medium, "reorganization event"): applied. Confirmed at C14 line 393; "reorganization event" occurred nowhere else in the chunks, while C07 (Section `sec:participatory`) and C11 use "formation event". Replaced with "the main text accordingly speaks of a formation event (Section~\ref{sec:participatory}), not of a phase transition in the statistical-mechanical sense." The companion change to C10 line 144 ("A finite-coupling transition remains conjectural" to "A finite-coupling formation threshold remains conjectural") was not applied because it lies outside this chunk; flagged here as a cross-chunk note for the C10 owner.
