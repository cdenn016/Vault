# C11 change log (original lines 2160-2661: Methods, Statements, Appendices A, B, C)

Editor model: Claude Opus 5.5. Numbers put into the text were re-run from the panel scripts (`L10_gradients_fd.py`, `L11_rock_backaction.py`, `L10_step_stability.py`) or from two new scratch checks of the group-variable frame gradient (relative FD error 1.2e-7 for one pair; 2.4e-9 for the complete canonical frame gradient, K in {2,3}, three agents, three draws, generic frames with norm 1.5). The chunk compiles in a minimal 11pt/1in wrapper with no errors and no overfull boxes.

## 1. Items

| Item | Disposition | Reason / description | New location or label |
| --- | --- | --- | --- |
| Spec: remove aggregate scaling analysis (2175-2182), all WikiText items (M18, L09-1 to L09-4, D7) | applied | Subsection "Aggregate Scaling Analysis", fit coefficients, CSV/generator names, and the WikiText sentence in the LLM paragraph deleted | `sec:methods_scaling` removed |
| L09-6, L19-5, spec "prospective procedure stays, consistent with C07" | applied (coordinated) | C07 now holds the single decision-grade protocol (arms A/B/C incl. frozen-attention-prior control, predeclared event, window, statistic, n = 20, pass rules, McNemar). To keep one copy, Methods is reduced to a pointer paragraph stating that no simulation result is claimed, that the protocol is in Section `sec:participatory`, that it is unexecuted, and that its claims have status C. The duplicate population identity display was deleted (C07 states it as a validity precondition) | `sec:methods_metagent` kept; `eq:prospective_population_identity` removed |
| D9, L17-8, L09-7, minor 2185 (seed paragraph describes current code) | applied | Computational Details rewritten without seeds, cuDNN/cuBLAS flags, codebase paths, `\texttt`, or the transformer mechanism; states that no result depends on simulation and points to the Appendix A FD check | Methods, Computational Details |
| LLM-assistance disclosure (L17-8) | applied | Kept; removed the WikiText/aggregate-fit sentence; added that Claude Opus 5.5 assisted the revision including numerical checks (see cross-chunk note 7) | Methods |
| Author Contributions | applied | Dropped "analyzed the recoverable aggregate scaling table" | Statements |
| Data Availability (L09-1, M18, L17-3 item 6) | applied | Now states that the paper reports no empirical dataset and no simulation output, and that the protocol is unexecuted, so no trajectories, snapshots, or simulation figures exist; no nonexistent files named | Statements |
| Code Availability | applied | One sentence; repository existence and public visibility confirmed with `gh repo view` | Statements |
| L17-11 (back-matter order) | not applied | Section order is an integration decision; Methods is now two short paragraphs plus the disclosure | none |
| D7/D10: transformer-only material in App. A | applied | Removed the transformer-implementation autodiff sentences (2185, 2370, 2459, 2514), the Rényi-order sentence citing `sec:transformers`, and the implementation mechanism comparisons | App. A |
| L04-9 (lead with canonical gradients; surrogate to one paragraph; beta dependence) | applied | New subsection "The Canonical Envelope Gradient": general envelope formula, self/receiver/sender building blocks, complete mean, covariance and frame gradients displayed. Surrogate subsections (receiver mean, covariance, frame, two-term "physical interpretation", model alignment, sender softmax cross-term, total surrogate mean gradient) replaced by one subsection built on the exact covariance identity, which contains every removed surrogate display as a special case. Attention row written with beta_ij({q},{U}) | `eq:canonical_gradient_general`, `eq:canonical_gradient_mu`, `eq:canonical_gradient_sigma`, `eq:canonical_gradient_frame`, `eq:surrogate_covariance_gap` added; `eq:sender_softmax_entry`, `eq:sender_autograd`, `eq:total_gradient_mu_complete` removed |
| G2-5 (Theory targets; cut surrogate; move retraction, Fréchet, complexity, fp32 out) | partially applied | Theory citations added (Ch. 6 attention-reduced potential proposition, Ch. 8 envelope identity, G5 Fisher moment chart, G8 orthogonal-reframing statement, Ch. 5 evidence identity, G4 Gaussian relative entropy). Surrogate cut. Retraction, Fréchet forms, complexity, and fp32 paragraphs kept because the spec lists corrections to them; they are corrected in place | App. A, App. C |
| New: frame gradient in the group variable | applied (D, verified) | nabla_{U_i}E_ij = N_ij U_i^{-T}, nabla_{U_i}E_li = -Omega_li^T N_li U_l^{-T}, derived from delta Omega and the unconstrained derivative; FD-verified (see header). Makes the Fréchet integrals optional and supplies the input of xi = U^{-1} grad_U F | `eq:canonical_gradient_frame` |
| L04-10, minor 2406-2414, L10 verified item 8 | applied | Uncentered split replaced by the centered row form; correct limits (kappa to infinity: pi-weighted mean gradient; kappa to 0 with unique minimizer: grad E_ij*, response bounded by (Delta/kappa)e^{-Delta/kappa}); agreement whenever Cov = 0; catastrophic cancellation of the uncentered pieces stated; "essential" deleted | App. A surrogate subsection |
| L02-10, minor 2328 (O(K) not SO(K); 2Sigma(.)Sigma belongs to a = 1/2) | applied | "g in O(K_q)"; Fisher member a = 1/2, b = 0 with gradient 2Sigma(.)Sigma, a = 1 would give Sigma(.)Sigma | Frame covariance paragraph |
| L10-7, minor 2328 (trace-free sector) | applied | "unit-determinant directions tr(Sigma^{-1}U) = 0, the sl(K_q) sector after whitening" | same |
| L14-7, minor 2328 (Pennec 2009) | applied | `\cite{Pennec2006, Amari2016, Bhatia2007}` replaced by `\cite{Pennec2009}` for the invariant family; G5 cited for the Fisher member | same |
| L10-2, minor 2497-2506 (normal-equations detour, O(K^6)) | applied | Update equations use xi_i = U_i^{-1} grad_{U_i} F_red, with the pushforward identity and a subalgebra qualifier (L02 verified note); text states that assembling G_pull costs O(K^6) and squares the condition number; complexity paragraph adds the same sentence; executable-table sentence removed | Complete Update Equations; Complexity |
| L01-8 (frame flow vs right redundancy; location 2372 and 2512) | applied | Update subsection states equivariance of the body-covector update (per-agent left translations with beliefs co-transformed; right translations only by orthogonal g) and of the ambient-pullback update (orthogonal only), that neither descends to the right quotient, and that no metric respects both (Milnor 1976). The original 2512 claim that the updates "transform covariantly so as to preserve the gauge invariance" was false and is replaced by a derivation (velocity maps to g^{-1} xi g^{-T}) | Complete Update Equations; "Right-translation redundancy" paragraph |
| L10-4, G3-3, minor 2510 | applied | Storage, not eigendecomposition, causes fp32 indefiniteness; cond(A_ij) <= cond(Omega_ij)^2 cond(Sigma_j) with frame-norm bound; Cholesky backward stable independent of conditioning (Higham Thm 10.3, componentwise bound stated); completion condition of Thm 10.7 with unit-diagonal scaling, implying cond_2(H) below about 1/(n(n+1)u), 1.5e5 for K_q = 10 (derived: lambda_max(H) >= 1) | Numerical Stability paragraph |
| L10-6a, minor 2512 | applied | Exact first-order chart action phi + psi(ad_phi)(zeta), psi(z) = z/(1 - e^{-z}); additive shift correct only to first order in both phi and zeta | "Right-translation redundancy" paragraph |
| L10-9, L04 notes, minor 2514 | applied | Gradient-verification sentence replaced by the executed check with its settings (float64, h = 1e-6, K in {2,3}, 3 agents, frame norm 1.5; <= 1e-7, directional derivative 2.3e-7); abelian-approximation error quantified (0.37 ||phi||_F; 1 percent at 0.03, 10 percent at 0.3, about 40 percent at 1.4), rerun of `L10_gradients_fd.py` | "Gradient verification" paragraph; chart-gradient paragraph |
| L10-8 (symbol collisions in App. A) | partially applied | kappa(Sigma) replaced by cond(.); eigenvalue matrix Lambda renamed D; duplication matrix renamed \mathcal{D}; Lambda for transported precision kept locally (defined where used); tau collisions outside chunk | App. A, App. C |
| L16-12 | applied | `\texorpdfstring` in the App. A title | `app:gradients` title |
| L16-9, D3d | applied | `^\top`/`^{-\top}` throughout, `D_{\mathrm{KL}}`, `\operatorname{tr}` | whole chunk |
| L16-6 (single-index Omega_i for the frame) | applied | Frame is U_i throughout; the sentences using Omega_i were removed with the software content | App. A |
| L16-5 (photon agent gamma) | applied | Photon channel renamed ph | App. B |
| L16-2, D3b | applied | tau_rock renamed vartheta_rock | App. B |
| D3a | applied | "scale-0/1" became "level-0/1"; SO(3) spin index renamed j (was l, which now denotes level); SO(3) structure constants indexed a, b, c | App. B, App. C |
| L02 verified note / L03-6 (telescoping on a subalgebra) | applied | Qualifier "when the generators span gl(K_q), and its tangent projection on a subalgebra" | Complete Update Equations |
| L08-3 | moot | Concerns the transformer, removed | none |
| L10-3 (dexp singular locus at pi) | not applicable here | Location 999 is C03; App. A no longer relies on the chart singular locus because the frame velocity is computed in the group variable | none |
| L11-5, M8, spec (Appendix B covariance back-action) | applied | Displays kept (verified); conclusion replaced: mean back-action O(eps) absolute and O(eps^{1/2}) in Fisher length; covariance back-action O(1) relative to Sigma_R; stationary precision Lambda_R* = (Lambda_p + beta Lambda_h)/(1 + beta), ratio to prior precision tends to 1/(1 + beta); Fisher-Rao distance tends to sqrt(K_q/2) log(1 + beta); cause (entropy reweighting) stated. Asymptotic-reading and final-readings paragraphs and the qualitative paragraph at 2533 corrected accordingly. Rerun of `L11_rock_backaction.py` reproduces every value | `sec:rock_derivations`, `eq:rock_back_sigma` (display extended with its exact value) |
| Spec: rock reading status S; D2 fences | applied | Opening paragraph now declares status S with pointer to `tab:claim_status`; "fence governs every paragraph" deleted; reference to `sec:scope_limitations` removed | `app:examples` |
| L11-11 | applied | "framework realization of" became "framework analog of" (three places) | App. B |
| L11-9(b) | applied | DeGroot pooling and quantum Darwinism (Zurek 2009) named as comparison classes after `eq:rock_consensus` | App. B |
| M17, D4d (precision as stiffness; relaxation rate independent of precision) | applied | "The rock exhibits slow dynamics" was false by the chunk's own Eq. rock_inertia (rate eta_q independent of epsilon); rewritten as insensitivity of the mean to low-precision neighbors; paragraph title "Inertia from precision" became "Insensitivity to low-precision neighbors" | App. B |
| M13 (parent frame) | applied | Collective frame U_rock stated to be a declared convention by `prop:parent_frame_gauge` | App. B |
| M14 (detector status) | applied | Detector called a proxy for the licensing criterion (App. B; Methods pointer defers to C07) | App. B |
| D4c | applied | "edge-relaxed Wilson-line transport" became "independent links on the interaction graph" | App. B |
| G2-5, spec (Appendix C citations) | applied, with one deviation | Ch. 5 (classical finite evidence identity) cited for the VFE preliminaries; G5 (Fisher metric in the moment chart, with GL affine isometry) cited for the Fisher display; the Gaussian KL is cited to Ch. G4 (Gaussian reverse relative entropy proposition), where it is stated, not G5 as the task text said (G5 contains only the equal-covariance case) | `app:variational_prelim`, `app:gaussian_kl`, `app:fisher_gaussian` |
| L01-10, minor 2649 | applied | BCH-truncated transport breaks the cocycle, has triangle holonomy of order ||[phi_i, phi_j]||, and is not right-invariant; vanishing field strength holds only for the exact product | App. C, SO(3) subsection |
| D9 in App. C (SO(3) software history, "public code repository") | applied | Historical/checked-in simulator sentences removed | App. C |
| L10-5, minor 2655-2660 | applied | "proved essential" deleted; derived model-problem stability (retraction eta < 1 independent of conditioning; Euclidean Sigma step eta < 2 lambda_min^2; Cholesky step of order lambda_min with lambda_max = 1, rerun of `L10_step_stability.py`); positive-definiteness, not step stability, is what Cholesky guarantees; conditioning-dependent relaxation rate noted | App. C, Cholesky subsection |
| L02-9 | applied | Absolute value declared inadmissible; stationarity equivalence stated for diffeomorphic maps (softplus, exp) | same |
| L10 verified item 16 addendum (softplus underflow) | not applied | Optional; the sentence now says "cannot cross zero in exact arithmetic" | none |
| G2-5 "cut 2637-2660" and REVIEW table "cut SO(3) and Cholesky" | not applied | The task text requires correcting 2649 and 2655-2660, so both subsections were kept, shortened, and corrected | none |
| D4b gauge vocabulary | applied | "Gauge Covariance" became "Frame covariance" (congruence action); "Gauge Orbit Preservation" became "Right-translation redundancy", referring to `sec:gauge_covariance_principle`; "gauge-equivalent" wording removed | App. A |
| D13 style | applied | No banned words, no horizontal rules, no `\,`, `\;`, `\!`, no "rather than" in the chunk; American spelling; display punctuation checked | whole chunk |

## 2. Labels removed

- `sec:methods_scaling`: no references anywhere in `PIFB2.orig.tex`.
- `eq:prospective_population_identity`: referenced only at original 2167, inside this chunk.
- `eq:sender_softmax_entry`: no references.
- `eq:sender_autograd`: referenced only at original 2476, inside this chunk.
- `eq:total_gradient_mu_complete`: referenced only at original 2489, inside this chunk.

## 3. Labels added

- `eq:canonical_gradient_general`
- `eq:canonical_gradient_mu`
- `eq:canonical_gradient_sigma`
- `eq:canonical_gradient_frame`
- `eq:surrogate_covariance_gap`

## 4. New bib keys needed

None outside the permitted sets. Keys used: `DennisGaugeVFE2026`, `DennisGaugeVFESuppG2026` (D5); `Zurek2009` (G3 list; the bibliography agent must add it); existing `Pennec2009`, `Higham2002`, `Absil2008`, `Milnor1976`, `degroot1974`, `Amari2016`, `Friston2010`, `parr2022active`. C11 no longer cites `Pennec2006` or `Bhatia2007`; a grep of the current chunks finds no other citation of either, so the bibliography agent may check whether they are now unused.

## 5. Cross-chunk notes

1. C07: Section `sec:participatory` is the single home of the prospective protocol. C11's Methods paragraph points there and states only that no simulation result is claimed, that the protocol is unexecuted, and that its claims have status C. C11 no longer displays the population identity. If C07 changes the arm names or pass rules, no C11 edit is needed.
2. C00 (abstract, contributions, scope, lines 61, 108, 116, 122 in the original that reference `sec:methods`): Methods now contains no empirical analysis, no WikiText material, and no scaling artifacts. Any front-matter sentence that points to Methods for the scaling fit, the bundled aggregate table, or fence F6 must be deleted.
3. C00 claim-status table: the row "Covariance back-action vanishes for the rock" should read that the mean back-action is suppressed (D), that the stationary rock precision is lowered by a factor tending to 1/(1 + beta) (D, corrected), and that the rock reading is S.
4. C10 (original 2079, "the rock appears certainly there"): must be weakened to match the corrected covariance back-action (L11-5): the rock's mean is insensitive to broad observers, its precision is not.
5. C03 (after `eq:gauge_group_retraction`): Appendix A now states the equivariance of the frame updates (L01-8) and uses xi = U^{-1} grad_U F directly. C03 should state the same result or refer to Appendix A, and must not claim trajectory covariance under the global right redundancy. The dexp-locus correction (L10-3) remains C03's.
6. C14 notation table: add cond(.) for condition numbers, \mathcal{D} for the duplication matrix, "ph" for the photon channel of Appendix B, and j for the SO(3) spin of Appendix C. The original notation sentence placing tau^{(q)}_{ij}, tau^{(s)}_{ij} "in Appendix app:gradients" was wrong (they are Appendix E couplings); check the new table.
7. Front matter or author: the LLM disclosure now says that Claude Opus 5.5 assisted with this revision, including numerical checks. The author should confirm or edit the model names.
8. C02/C05: Appendix A writes the observation term generically as F_obs,i and refers to `eq:total_gradient_mu` (C05) for the Gaussian identity readout. If C02's observation-term typing (registered defect D8a) changes that term, `eq:total_gradient_mu` must be updated consistently.
9. Removed reference to `tab:executable_contract` (C00 deleted the table) and to `sec:transformers`.
10. The right-translation paragraph now cites `sec:gauge_covariance_principle` (C01) because C14 no longer names "Action (a)".


## Integration pass (2026-09-24)

Editor model: Claude Opus 5.5. A wrapper build of C11 and C12 with the C00 preamble gives 0 errors and 0 overfull boxes. Every reference in the chunk resolves against the assembled chunk set, and every citation key is in references.bib or the round-two key list. Words: 6,293 before, 5,910 after (about 380 removed). No label was removed or added.

### Notes applied

| Source | Note | Action |
| --- | --- | --- |
| C00 | Rock covariance back-action has status D; the rock reading has status S | The App. B opening now states that the derivations have status D and their reading has status S, matching `tab:claim_status`. The precision statement keeps "a factor that tends to 1/(1+beta)" (see the table change below). |
| C02 | F is "the consensus free-energy functional", a composite potential; "variational free energy" is reserved for the single-agent bound | The App. A opening names the consensus free-energy functional of `sec:free_energy`. The App. B opening and the App. C Gaussian-KL sentence refer to the consensus functional. App. C "Variational Free Energy Preliminaries" keeps the term because it describes the single-agent bound. |
| C02 | tau_gamma for gamma rows; kappa is a declared constant, not trained; receiver-presence weighting; line 2239 per L04-8(c) | kappa_beta and kappa_gamma are replaced by tau and tau_gamma throughout App. A (C02 notation). The setup paragraph now says that kappa is a declared dimensionless constant, not a variational parameter of F, and that at c_* with all agents present every receiver-presence weight equals one. L04-8(c) was already applied: `eq:surrogate_covariance_gap` sums over every row and cites `sec:complete_free_energy`. |
| C05 | The rock precision scale is delta, not epsilon | epsilon is renamed delta throughout App. B, with the C05 definition (dimensionless, no physical units) at first use. The Fisher-length displacement is renamed Delta mu to avoid a collision. The "slow dynamics" wording, the "inertia" title, and the phrase "consensus term of sec:mass" were already gone (confirmed). |
| C10 | App. B carries L11-5's corrected covariance back-action | Confirmed present: stationary precision, Fisher-Rao distance, and cause. |

### Notes rejected or already handled

- C01 (`tab:executable_contract`): already removed in the chunk edit. No reference remains.

### Other edits

- Level-index collision (D3a; check-report item): App. A used ell as the sender-agent index, including the superscript on the transported precision, which read as a level index. In App. A only, the sender index is now k and the summation dummies are m. The pointer to `eq:total_gradient_mu` now says "relabeled k to j".
- Spacing: the double space in the App. C evidence integral is replaced by an upright differential.
- Tightening:
  - Methods: the pointer paragraph is shorter (the status restatement already carried by `tab:claim_status` is removed). Computational Details no longer repeats the Code Availability sentence.
  - Statements: the duplicate funding sentence is removed from Competing Interests (Funding keeps it). Data Availability is shorter, and "tensor snapshots" is removed.
  - Frame sector: the two repeated log-det justifications are cut to the one SO(K) sentence.
  - Natural gradients: the displays that duplicated App. C are folded into one inline sentence.
  - Frame covariance: the repeated covariance sentence and the repeated "not the unique invariant choice" sentence are merged.
  - The closing sentence on the exponential map is shorter.
  - Complexity: the duplicate O(K^6) sentence is removed. It stays in the update subsection with the condition-number remark.
  - App. B: the opening, the insensitivity paragraph, the bidirectionality paragraph, and the closing readings are condensed. The asymptotic reading drops the unsupported identification of the dimensionless scale with "thermal motion" and "finite temperature".
  - "Body" meaning the main text now reads "main text". The technical term "body covector" is kept.

### Cross-chunk notes

1. C00 table row "High-precision agent": the stationary precision is lowered by a factor that tends to 1/(1+beta) as delta goes to 0 (exact ratio (1 + delta beta Lambda_h)/(1+beta)), not by exactly that factor. Suggested wording: "reduced by a factor tending to 1/(1+beta)", and add "reading S".
2. C10 (line 81 of C10.tex) uses epsilon for the rock precision scale and says the precision is reduced by 1/(1+beta) "for every epsilon". At finite scale this is incorrect (see item 1). It should read "by a factor that tends to 1/(1+beta)", and the symbol should be delta to match C05 and App. B.
3. C14 notation appendix: the App. A sender index is k (dummies m); the attention temperatures are tau and tau_gamma (kappa_beta and kappa_gamma are retired); the App. B precision scale is delta.
4. C03 still uses ell as an agent index in four places, which collides with the level index.
5. Author: the LLM disclosure (Claude Opus 5.5 assisted this revision, including numerical checks) still needs confirmation.

## Consistency fixes

| Issue | Disposition | Reason / description |
|---|---|---|
| Computational Details mentions only the gradient checks (low) | Applied, adapted | Confirmed: the subsection names only the Appendix A finite-difference check. Added two sentences after it stating that several appendices and the binary-registration example report small deterministic numerical witnesses, each a direct double-precision evaluation of the stated closed forms or iterations on the stated instance, none a simulation of the multi-agent dynamics. The reader's appendix letters (A, C, E, G, I) were wrong: the cited witnesses sit in the gradient appendix (median 1.4 abelian error), the covariance-dynamics appendix (max lambda approximately 610), the conditional-representation appendix (2.59), the augmented-joint appendix (0.13, 12.98 nats, spectral radius 1.173), and the exact coarse-graining appendix (7.3e-3 Karcher gap), that is A, D, F, G, I. The sentence therefore uses `\ref{app:gradients}`, `\ref{app:covariance_dynamics}`, `\ref{app:conditional_representation}`, `\ref{app:augmented_joint}`, `\ref{sec:meta_agent_rg}` instead of letters, plus `\ref{sec:binary_registration}` for the main-text channel example in C09 (0.0145, 0.135, 0.962 bits). No labels added or removed. |
| "pan-agentic commitment" vocabulary drift (low) | Applied | Confirmed: "pan-agentic" appears only here and is undefined; C00's interpretive stance uses "the commitment to universal agency". Replaced with "the commitment to universal agency of Section~\ref{sec:cognitive_first}". |
