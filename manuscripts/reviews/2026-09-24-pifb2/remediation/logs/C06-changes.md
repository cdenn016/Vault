# C06 change log (original lines 1533-1661; coarse-graining I)

New line numbers refer to the revised `chunks/C06.tex` (149 lines, CRLF preserved).

## 1. Items

| Item | Disposition | Reason or description | New line / label |
| --- | --- | --- | --- |
| M13 / G1-1 | applied | Radius replaced by Afsari's global-uniqueness radius r_cx = (1/2) min{inj G, pi/sqrt(Delta)} (Thm. 2.1); SO(K_q): pi/sqrt(2) in d_G, rotation angle pi/2 for SO(3); Delta and inj stated; Kendall's larger radius attributed to the ball-restricted mean, with the three-rotation witness (minimum 16 pi^2/27 attained three times). Numbers confirmed by rerunning `G3_karcher_radius.py`. | 59 |
| M13 / G3-1 | applied | Same fix; the false "below the injectivity radius" clause is not reproduced. | 59 |
| M13 / Grove-Karcher credit (G1-1) | applied | "The construction is Karcher's" replaced by Grove-Karcher 1973 for the construction, Karcher 1977 for the estimates. New key `GroveKarcher1973`. | 59 |
| M13 / L14-8 | applied | Bonnabel-Sepulchre (fixed-rank PSD) removed; left-invariant metrics cited to Milnor 1976 and Andruchow et al. 2014. | 61 |
| M13 / G1-2 | applied | Both options combined: U_I is declared a gauge convention and the parent is defined by the frame-free pair (m, S) (Definition); the Karcher convention is single-valued when frames lie in an r_cx ball, and the Definition and line 59 state that Gamma cannot detect this condition. | 59, 65-72 |
| M13 / G1-3 | applied | Added: ||log(U^{-1}V)||_F is not a distance on GL+; obstruction is to a bi-invariant variance, not a mean; Pennec-Arsigny exponential barycenter (Thms. 11-12) is bi-invariant; Afsari applies under a left-invariant metric (left-equivariant only). Additive frame average described as the first fixed-point iterate of the exponential barycenter from the identity. Open problem restricted to the choice of convention. New key `PennecArsigny2013`. | 61, 143 |
| M13 / L01-10 | applied (in-chunk part) | O(||phi||^2) accuracy sentences at 1573, 1644, 1655 deleted; 1577 "correct coarse-graining target" replaced; the licensing argument inherits no frame error when one convention is used consistently. The 2649 truncated-transport holonomy remark lies outside C06 (cross-chunk note). | 63, 132, 143 |
| M13 / L05-9(b), L17-7 | applied | 1575 retraction and the contradictory 1573/1644/1655 sentences reconciled; additive frame stated as non-equivariant with defect controlled by the gauge transformation and the spread of the phi_i. | 143 |
| M13 / 1575 as proposition (L17-3 item 4, L17-7, M10) | applied | New Proposition (parent frame is pure gauge; no symmetric left-equivariant map GL+(K)^n -> GL+(K), also on SO(K)) with proof; (i) extended to show the barycenter's (m, S) is U_I-independent. Dated "findings recorded in 2026" paragraph, "no substitute metric has ever felt principled", and the reference-pooling sentence deleted (the last replaced by the statement that symmetric equivariant means exist only on restricted domains, which exclude the cyclic tuples). | `prop:parent_frame_gauge`, 38-52 |
| M13 / 1577 wording (L06-10(b), L18-2) | applied | "Correct coarse-graining target" becomes "frame-consistent coarse-graining maps" after a declared frame convention; covariance does not single out the maps (I-projection equally covariant) and is not exactness; exact parent = pushforward under a declared kernel, cited to Theory Ch. 9 (pointwise parent-datum corollary); barycenter with dispersion = moment projection of the mixture and the dispersion-free pooled form = image of no parameter-independent kernel, cited to Supplement G Ch. G8 (both read in Theory `c09`, `g08`). | 63 |
| M13 / L06-10(a),(c) | not applied here | Restating `thm:rg_covariance` for left-invariant metrics and the radius at 3762 are in C14. | cross-chunk |
| M13 / L14-1, L15-5, L16-1 | applied (keys) / moot (1685) | `Kendall1990`, `Afsari2011` now resolve through G3's BibTeX (D12 list). `DorflerBullo2013` is at 1685 (C07), not in C06. | 59 |
| M14 / L05-4 | applied | Savings rationale rewritten: the |I| epsilon cap is kept only as a bound on the energetic intra-cluster term at frozen beta; at Gibbs rows deleting intra-cluster sources raises each row by tau log(1 + Z_in/Z_out) > 0 (unnormalized prior) and still raises it with the renormalized prior in the high-coherence case; any gain must come from outside rows or the parent prior, not derived. C(I) stated to be a free function. | 84-86 |
| M14 / L18-2 | applied | Criterion degenerate under exact parents: F_fine = F_coarse + Delta_A, Delta_A >= 0, at unchanged evidence; criterion reduces to Delta_A > C(I); licensing needs a functional not monotone under refinement (Theory Ch. 9, exact coarse free-energy theorem, evidence-preserving corollary, partition-selector open problem; read in `c09`). "Merging the cluster reduces the total free energy net of overhead" deleted. | 88 |
| M14 / L05-5(a) | applied | Gamma > Gamma_min removed from the Definition; Definition keeps support and size; licensing by the criterion; detector declared a candidate filter, not part of the definition. | 65-72, 101 |
| M14 / L05-5(b) | not applied here | The 3940 Appendix I summary is in C14. | cross-chunk |
| M14 / L05-5(c) | applied | Waade et al. restated as "propose that a collective can constitute a group-level agent if it maintains a group-level Markov blanket"; the detector does not test that condition; "operationalize" deleted. | 74 |
| M14 / L05-6 | applied | "Leading-order saddle-point approximation" clause deleted; weight declared a modeling choice. | 110 |
| M14 / G1-4 | applied | "Guaranteed in the high-coherence regime" replaced by the max-pairwise condition; mean-versus-max implication max KL <= |I|^2 tau log(1/Gamma_min); separate maximum-divergence check required; n = 610 outlier example with two stable fixed points and outlier weight 0.974 (rerun of `G1_weight_contraction.py` reproduced). Implementation "warns on non-convergence / strict setting" sentence deleted (D9); replaced by the remark that a non-convergence test cannot detect bistability. | 110 |
| M14 / eps0 <= 2 (G1-4) | applied | Lemma states every admissible constant satisfies eps0 <= 2 at lambda_min = lambda_max = 1; proof includes the pitchfork m -> a tanh(am), eps = 2a^2 (rerun reproduced). | 123-130 |
| M14 / G1-5 (minor 1637-1641) | applied | Lemma restated in (mu, Sigma) coordinates with Euclidean/Frobenius norms, maps into the hull H, Lip = C epsilon on H (was C sqrt(epsilon)), eps0 = 1/C (was C^{-2}), sum chi_i > 0, max-pairwise hypothesis, Regime I; proof sketch corrected (moments, not expectation parameters; gradient differences O(sqrt(epsilon))). | `lem:weight_contraction`, 123-130 |
| M14 / G1-6 | applied | Pass-band corollary replaced by the always-valid eps_w <= |I|^2 (max w)^2 eps-bar; the 0.035 figure kept only for uniform weights at the illustrative values. | 108 |
| M14 / G1-7 (i) | moot | The "intermediate coherence where the net gain is largest" sentence is deleted with the savings rewrite (L05-4), so no interior-optimum claim remains. | 86, 103 |
| M14 / G1-7 (ii)-(iv) | applied | "Controlled" made conditional on uniform weights; "guaranteed" fixed (G1-4); "operationalize" fixed (L05-5c). | 108, 110, 74 |
| M6 part / L05-3 (1602) | applied | M-step reading stated as exact for a random-effects (empirical-Bayes) model with the frame-free parent pair as a point hyperparameter; cited Neal-Hinton and Theory Ch. 12 (aggregate-prior proposition, read in `c12`); parent carries no belief, Sigma_I is population covariance; Appendix G's single-parent-latent model named as a distinct model in which Sigma_I is posterior uncertainty. The "tension with the Level-3 commitment" sentence removed. | 90 |
| Minor 1540 (L05-9(a)) | applied | "The one construction" removed; I-projection noted as an equally covariant strict minimizer; M-projection chosen for the M-step reading and uncertainty pooling. | 23 |
| Minor 1660 | applied | "Heat death of the informational universe", "informational analog of thermal equilibrium", and the "epistemic death" name removed; section retitled "The Consensus Foil: Pointwise Consensus"; statement reduced to the trivial fact that coupling terms attain their minimum zero; "gauge freedom preserving distinct perspectives" deleted (D4b). | `sec:epistemic_collapse` (label kept), 146-149 |
| L03-2 | applied (in chunk) | "Forward/reverse KL" dropped: coupling described as receiver law in the first slot (I-projection direction), barycenter as M-projection. | 13, 34 |
| L16-3 / D3a | applied | Scale superscripts (s), (s+1) become (l), (l+1); "scale-s agents" becomes "level-l agents"; V^{(l)}_I. | 66-70, 99-100, 116-117, 136-140 |
| L16-6 | applied | Comma subscripts Omega_{I,i}, Omega_{i,I} become Omega_{Ii}, Omega_{iI}. | throughout |
| L16-2 | moot | No clock symbol in C06; the temperatures tau_q, tau_s are unchanged (D3b); the code name tau_KL removed. | 99 |
| L16-10 | partially applied | `lem:weight_contraction` now referenced twice; `prop:barycenter_existence` remains unreferenced (harmless). | 110 |
| D3e notation collision | applied | The support region, also written U_I in the original, renamed calligraphic U_I to free U_I for the parent frame (as used in Appendix I). | 68 |
| D3d | applied | ^T to ^\top in eq:meta_agent_sigma_impl; KL written D_KL throughout. | 117 |
| D2 | applied | "Level-3 interpretive commitment ... Epistemic Status taxonomy" replaced by status S and Table~\ref{tab:claim_status}; criterion status C, detector status S stated. | 74, 84, 103 |
| D4a | applied | "Renormalization-group construction", "rigorous RG construction", "renormalization-group covariance theorem" replaced by coarse-graining terminology. | 3, 84, 101, 110 |
| D4b | applied | Equivariance stated for one global g at the base point; "passive choices of frame"; frames removed from the slow channel. | 25-27, 74, 132 |
| D5 | applied | Theory cited by chapter with descriptive names (Ch. 9, Ch. 12, Supp. G Ch. G8); every cited statement read in the Theory tree. | 3, 34, 63, 88, 90 |
| D9 | applied | `\texttt` code path, "reference implementation" statements, strict-mode error, separate-weight-vector parenthetical, "No recoverable historical hierarchy artifact", dated "findings recorded in 2026" removed; detector constants presented as illustrative values. | 99, 110, 132, 143 |
| D1, D7 | moot | No "realizes" and no transformer material or deleted-label references in C06. | none |
| D13 | applied | Final grep: no banned words, no `\,` `\;` `\!`, no "Level", "fence", "realiz", "RG" (outside lowercase labels), "renormaliz", "transformer", `\texttt`; reduced "rather than" to zero occurrences. | whole chunk |

## 2. Labels removed

None.

## 3. Labels added

- `prop:parent_frame_gauge` (Proposition: the parent frame is pure gauge; no symmetric left-equivariant frame mean).

## 4. New bib keys needed

- `GroveKarcher1973`: K. Grove and H. Karcher, "How to conjugate C^1-close group actions," Math. Z. 132(1), 11-20 (1973), doi:10.1007/BF01214029 (verified on Crossref).
- `PennecArsigny2013`: X. Pennec and V. Arsigny, "Exponential Barycenters of the Canonical Cartan Connection and Invariant Means on Lie Groups," in F. Nielsen and R. Bhatia (eds.), Matrix Information Geometry, Springer, Berlin, Heidelberg, 2013, pp. 123-166, doi:10.1007/978-3-642-30232-9_7 (verified on Crossref; theorem numbers from G1's reading of the author preprint).
- Also used from the D12 list (bibliography agent adds): `Kendall1990`, `Afsari2011`, `Andruchow2014`; and the D5 keys `DennisGaugeVFE2026`, `DennisGaugeVFESuppG2026`. `BonnabelSepulchre2009` is no longer cited from C06.

## 5. Cross-chunk notes

- C14 (Appendix I, 3758-3812): replace the radius clause at 3762 by Afsari's r_cx (rotation angle below pi/2 for SO(3), d_G < pi/sqrt 2), delete "which also lies below the injectivity radius", change "locally unique" to "unique" (G1-1, G3-1); state `thm:rg_covariance` at one base point for one global g and note that equivariance of the map needs only a left-invariant metric (G2-6, L06-10a); the proposition in C06 cites this theorem for "one global g".
- C14 (3940): the Appendix I summary must say the strengthened detector with the gap condition is the sufficient-condition surrogate and the body detector is not covered (L05-5b). The C06 body now calls the detector a coherence filter of status S and removes it from the Definition of a meta-agent.
- C14 (3930, `thm:rg_detector_retention`): its hypothesis A_I > 0 has no identified source (L05-4); C06 now says so in the body.
- C07 (cross-scale prior, `eq:cross_scale_shadow`): C06's `prop:parent_frame_gauge` and its M-step paragraph reference this label; keep it. C06's random-effects reading (parent as point hyperparameter, Sigma_I population covariance) is the ELBO-exact reading L05-3 recommends for the shadow section.
- C07 (1692): "epistemic death" should become "pointwise consensus"; `sec:epistemic_collapse` is kept but retitled "The Consensus Foil: Pointwise Consensus".
- C07/C14/others that write U_I for the support region: C06 now writes calligraphic U_I for the support region of `eq:meta_agent_support`; U_I is the parent frame.
- C00 claim-status table: barycenter and M-step P; parent-frame proposition P; Karcher uniqueness P under the corrected radius (false as printed before); licensing criterion C (degenerate under exact parents); detector S; contraction lemma D (sketch) with rate O(epsilon); meta-agents as belief-bearing agents S.
- C00 / C02 / C10 / C13 (594, 2959, 2964, 3152, 1804, 3807, 3811): "forward KL" names both slot orders (L03-2); C06 has dropped the adjective.
- C11 or whichever chunk holds original line 2649: the first-order truncation exp(phi_i - phi_j) breaks the cocycle and introduces holonomy of order ||[phi_i, phi_j]|| (L01-10).
- C12 (2150, implementation register): the GL+ frame-mean item should be restricted to the choice of a gauge convention and describe the additive form as the first fixed-point iterate of the exponential barycenter (G1-3); C06 points to `sec:open_problems` for this.
- C09/C08 or the discussion (1804, 2154): the Part I summary should not call the barycenter "the correct coarse-graining target" nor the detector a validated formation rule.
- Appendix G (`app:augmented_joint`) is referenced from C06 as the single-parent-latent model; keep the label or redirect the reference if the appendix is replaced by a Theory citation.

## Integration pass

Integration editor: Opus 5.5. C06 went from 5,106 to 5,012 words (about 95 removed). The assembled document built in a private scratch copy with latexmk exit 0, no LaTeX errors, and no undefined references. Every reference in C06 resolves. Every citation key is in references.bib or on the allowed list (GroveKarcher1973, PennecArsigny2013).

### Notes applied

| Source | Disposition | Action |
| --- | --- | --- |
| C00 (supersession noted "at the construction") | applied | The section opening now says the companion theory supersedes both the barycenter and the detector. Its parents are exact pushforwards under declared coarse channels (Theory Chs. 9 and 11), and its formation results are witnesses for declared families (Ch. 13, checked against Theory c13 "Formation Witnesses"). The barycenter is retained here as a working construction. |
| C00 (statuses: Karcher P for angle < pi/2; licensing C; detector S) | applied | The opening now gives the codes C (criterion) and S (detector) at first statement. The redundant "(status S)" in the detector subsection was removed. "The criterion has status C for two reasons" is kept at its home. The Karcher radius text (r_cx = pi/sqrt2 in d_G, rotation angle pi/2 for SO(3)) already agreed with the table. |
| C14 (body V^{(s)}_I uses (s) only for the model channel) | applied | V^{(ell)}_I is now V^{(s)}_I, "the superscript labeling the model channel", matching Appendix I's V_I^{(q)}, V_I^{(s)}, C_s, tau_s. The sentence pointing to the appendix now says the appendix writes the detector with the barycenter-relative dispersions. The body uses pairwise means, so the two definitions are not identical. |
| C14 (Afsari/Kendall text; frame-radius condition or U_I as convention; detector not a sufficient surrogate; "frame-consistent") | already applied | Confirmed in the text (lines 59, 71, 103, 63). |
| C01 (parent frame cancels in Regime I; no O(norm phi^2) BCH claim) | already applied | Confirmed: prop:parent_frame_gauge and the gauge-consistency paragraph. No BCH-accuracy sentence remains. |
| C03 (orig. 1588: frames on the learning timescale) | already applied | The slow-channel paragraph assigns the learning timescale to the generative model s only. The frame is not part of the slow block. |
| C07 / C09 (keep eq:meta_agent_sigma_impl, eq:meta_agent_mu_impl, sec:meta_agent_variational, sec:meta_agent_state_construction, sec:meta_agent_threshold, sec:epistemic_collapse) | confirmed | All labels are kept. The M-step statement relied on by C07's random-effects reading is unchanged. |
| C12 (keep sec:meta_agent_definition; no "forward" on the barycenter KL) | confirmed | The label is kept. No "forward/reverse KL" occurs in C06. |
| C13 (barycenter exact M-step only in the random-effects model; parent a hyperparameter distinct from def:augmented_joint) | already applied | Confirmed in the M-step paragraph. app:augmented_joint resolves (C13). |
| C10 (GL+ frame-mean convention as a gauge choice) | applied on the C06 side | C06 states the gauge-choice reading in sec:meta_agent_definition (prop:parent_frame_gauge and the GL+ paragraph). See the C10 note below for the pointer. PennecArsigny2013 is used. |

### Notes rejected

None.

### Other edits

- The opening was tightened, and the supersession sentence was added there (see above).
- The following restatements were removed: "the two symbols are reserved to their respective roles"; "for two reasons that we now state"; the sentence repeating that the frame convention does not affect the parent laws, which the gauge-consistency paragraph directly above already states; the closing sentence of the frame-average paragraph that re-introduced the I-projection/product-of-experts aggregation already treated in sec:meta_agent_definition; and the open question of whether the criterion would reproduce the detector's organization, which is carried by the claim-status table and by the Scope section.
- Checks: the chunk has no spacing macros, no Level/fence/RG/transformer vocabulary, no banned words, and no "rather than". The only (s) superscripts left are model-channel labels.

### Cross-chunk notes from this pass

- C10 (open items, line 146): "What is open is the choice of convention, which Section (sec:meta_agent_variational) identifies as a gauge choice" points to the wrong subsection. The gauge-choice statement is in sec:meta_agent_definition (prop:parent_frame_gauge).
- C00 table, optional refinements: (a) the Karcher row states "rotation angles below pi/2" for SO(K_q). That value is exact for SO(3). For K_q >= 4 the condition is d_G < pi/sqrt2, where d_G^2 = 2 sum_k theta_k^2 over rotation planes. Suggested wording: "unique for frames within geodesic radius pi/sqrt2 (rotation angle pi/2 in SO(3))". (b) The row "Moment-projection barycenter: closed form and M-step reading" could add "(random-effects model)", since C06 and C13 restrict the exact M-step reading to that model. (c) The log's earlier suggestion of a row "meta-agents as belief-bearing agents, S" is not in the table. C06 states that status inline, so the row is optional.

## Consistency fixes

| Issue | Severity | Disposition | Description |
|---|---|---|---|
| Wrong cross-reference for the description-length retention rule (line 84, free-energy improvement criterion paragraph) | medium | applied | Confirmed: Section `sec:rg_status` (C07) contains no retention rule, net retention gain, or penalty choices; the rule is Eq. `eq:rg_retention_gain` in Appendix `sec:meta_agent_rg` (C14), which also states the penalty choices and the closure-ansatz discussion. Both pointers in the sentence now read Appendix~\ref{sec:meta_agent_rg} (the first with Eq.~\eqref{eq:rg_retention_gain}); the pointer to Appendix~\ref{app:rigorous_rg} is kept as the location of the statements and proofs. The separate reference to `sec:rg_status` at line 3 (exact coarse-graining step) is correct and unchanged. No labels added or removed. |
