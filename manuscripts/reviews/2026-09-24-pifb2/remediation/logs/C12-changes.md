# C12 change log (original lines 2662-3161: Appendices D, E, F)

All numbers placed in the chunk were confirmed by re-running `L07_appD_fixed_point.py`, `L10_appD_E.py`, `L03_representation_gap.py`, `G2_repr_crosswalk.py` and `G2_appD_crosswalk.py` (outputs matched the panel reports). Two statements added here beyond the panel text were checked numerically in a scratch script (deleted afterwards): the triangle threshold h^2 + h^-2 = 52 for rho(L) = 2 with orientation reversal (rho = 2.00004 at h = 7.21), and the flat-link high-coupling limit (per-edge misalignment 3e-5 at a = 1e5; the limit formula sum_k pi_k U_k^T A_k U_k reproduced to 1.2e-6 at a = 1e7). Theory statements cited were read in `MultiAgentELBO/Theory/` (g04 "Block optimum", g05 "Edge relative entropy at fixed covariance", c05 "Local Gibbs bound and the exact block E-coordinate", c06 "Exact receiver update in the comparison-record model", c12 "Transported divergences and row free energies"). A minimal-preamble pdflatex build of the chunk compiles with no errors.

## 1. Items

| Item | Disposition | Reason or description | New location / label |
| --- | --- | --- | --- |
| M21 / L07-6 (existence criterion) | applied | Old proposition (hypothesis lambda_max(C_i) < 2, Thompson sketch) replaced by the precision-linear proposition: 2 Lambda = A + L(Lambda); SPD fixed point iff rho(L) < 2, unique, Neumann series; simultaneous receiver-only natural-gradient flow stays SPD and converges globally at rate 2 eta (1 - rho/2); rho >= 2 gives precision divergence; bound rho <= max lambda_max(C_i); rho = 1 for links gauge equivalent to orthogonal ones (graph-flat included). Full proof given (order-unit norm for necessity; Vandergraft 1968 for the Perron eigenvalue used in the rate and in (iii)). | `prop:covariance_fixed_point`, `eq:precision_transport_map`, `eq:precision_linear`, `eq:precision_flow` |
| M21 / L07-6 (alignment-dominated limit) | applied | Added: SPD solution iff rho(L) < 1 + 1/a; limit a -> infinity exists only if rho(L) <= 1; for rho < 1 precision -> 0 like 1/a; boxed relation is the eigen-equation and has an SPD limit only when rho = 1 with SPD Perron eigenvector. Added the flat-link case (immediate from L07-6's similarity L ~ beta (x) id): limit precision sum_k pi_k U_k^T A_k U_k in the trivializing frames, exact per-edge alignment. Old "validity condition" sentence and the "consistency check" paragraph replaced. Coupling strength renamed A -> a (L10-8). | `eq:beta_weighted_precision` kept |
| M21 / L07-6 (stability) | applied | Euclidean flow display removed (it contradicted the natural-gradient caveat); joint stability now from Prop. (ii); own-block Hessian kept (verified) with its correct scope; one sentence that the Euclidean flow shares the fixed point without a general stability theorem. | "Stability" subsubsection |
| M21 / L10-1 | applied | "Frame dependence and holonomy" paragraph: lambda_max(C_i) is gauge dependent; flat GL example with max lambda_max(C_i) ~ 610 and rho = 1; two-agent K = 1 backtrack-holonomy obstruction h <= 1/2 (independent links per ordered pair); with orientation reversal imposed (D4c) the obstruction shown on a triangle, char. poly lambda^3 - 3/4 lambda - (h^2 + h^-2)/8, rho >= 2 iff h^2 + h^-2 >= 52. Deleted "for general GL+ transports it is a quantitative conditioning bound". | after the proposition |
| M21 / G2-3 (scope sentence) | applied | Scope paragraph now states the entropy weight 1 + B_i, the Gibbs temperature 2 relative to Bayesian updating, and the normalized-joint contrast (block optimum, Supplement G Ch. G4). | scope paragraph |
| M21 / G2-3 (homogeneous limit) | applied | Conclusion now attributes Sigma_inf = Sigma_0 to the doubled entropy weight and contrasts precision addition (Sigma_0/2) in a normalized joint. Assumption (ii) "Omega_ij ~ I" made exact ("links preserve Sigma_0"), with uniqueness from the proposition; the observation case states the extra link condition. Assumption list turned into one sentence. | homogeneous limit |
| G2-3 item 4 (message passing) | applied | "Collapse to attention-weighted message passing" rewritten as "Mean update where covariances align": reference to deleted `sec:transformers` and the transformer value aggregation sum alpha_ij V_j removed; now tied to the flat-link high-coupling limit, with the contrast to the exact receiver update of the comparison-record model (Theory Ch. 6), which keeps a Kalman-type gain. | paragraph at end of App. D |
| G2-3 placement (App. D to supplement) | not applied | No supplement exists in this remediation and SPEC says not to cut substantive content; App. D kept, corrected, and shortened. | |
| M15 / L03-9 (App. E direction) | applied | App. E opening no longer attributes the direction to Theorem F; the direction is attributed to building the coupling from the transported sender covariance, with the reverse choice W = c Sigma_i^{-1} giving KL(Omega q_j || q_i). "Trace and log-det terms approximately cancel" replaced by the exact identity, exact up to the single log-det term; the O(Delta) analysis kept, condensed. | `eq:quadratic_kl_identity` (new) |
| M15 / G2-3 item 5 (App. E, cite G5) | applied | Added the fixed-coupling statement (common-covariance relative entropy plus trace term), cited to Supplement G Ch. G5. The state-dependent identification kept as value-level matching. | App. E |
| App. E condensation ("one sentence") | partially applied | Kept the exact expansion, the identity and the raw-weight subsection (C13 line 3271 cites `sec:raw_alignment_weights` and the raw weights); removed the confusing "we take tau ... set to 1" sentence and the "uniform-coupling, no-entropy specialization" sentence. | |
| M15 / L03-1 (scope of Theorem F) | applied | Theorem retitled "for the frozen-neighbor best response" and stated with neighbors and weights explicitly fixed; appendix opening, the theorem, the pooling paragraph and the summary (orig. 2959, 3152, 3158) scoped; App. E invocation (orig. 2894) removed. New "Scope: the joint scalar functional" paragraph: second-slot derivative f(t) - t f'(t) (1 - t for KL), the affine-compatibility argument forcing f = 0, and the two-agent witness (pool q1 = N(2,1/2), q2 = N(8/3,1/3); joint-gradient norm 2.59; joint minimizer N(1.88,0.83), N(2.53,0.60)). Invocations at 528, 594, 678 are in C02 (cross-chunk note). | `thm:representation_app` |
| M15 / G2-2 (KL-sum identity, Theory declares divergence) | applied | Added the KL-sum identity as a lemma with proof; it gives Step 2, the minimizer and the minimum value -(1+B) log Z_g >= 0 (Hoelder). Added: the Theory declares the transported divergence (Chs. 6 and 12) and nothing here fixes the divergence of the joint functional; the normalized-joint unit-exponent sentence citing Ch. 5. No claim that the Theory fixes the direction. | `lem:kl_sum_identity`, `eq:kl_sum_identity` |
| G2-2 (move converse, lemma, corollary to supplement) | partially applied | No supplement; the converse proof, `lem:richness_app` and `cor:closure_forces_kl` are mathematics the review verified, so they are kept. Condensed instead: Intuition paragraph (Lambert W, chi^2, JS heuristics), the "pins forward KL" sentence, the long assumption paragraph, the H_i/S decomposition, and the duplicate "Forward KL and geometric-mean solution" subsection removed; `rem:analyticity_role` folded into the proof of `lem:richness_app`; Step 3 prose shortened. | |
| L03-2 ("forward KL") | applied | "Forward" removed throughout the chunk (title, statements, summary); the coupling is named with its slot order ("receiver law in the first slot, the variational or I-projection direction"). Proof-step headings renamed Sufficiency/Necessity. | App. F title changed |
| L03-4 (interpretation sentence) | applied | Replaced the false comparative with Amari 2009 (only Bregman f-divergence) plus the dually flat e/m structure, and the Fisher metric as the local Hessian of every smooth f-divergence up to f''(1). | new key `Amari2009alpha` |
| L03-5 (at 3158) | partially applied / moot | "alpha-divergences" -> "the Amari alpha-divergences". The Renyi, Bhattacharyya and variance-notation parts concern the deleted transformer section (moot under D7). | summary paragraph |
| L03-8 (opinion pooling) | applied | Barycenter is now the Gaussian M-projection of the linear pool; axiomatic properties belong to the pool; the dispersion-dropping form approximates the projection only at high coherence; "each the axiomatically appropriate choice" deleted. The wrong cross-reference `sec:participatory` (the prospective-validation section) replaced by `sec:meta_agent_definition`. | pooling paragraph |
| L10-5 (App. D Euclidean flow, 2855) | partially applied | Euclidean flow replaced by the natural-gradient flow and a sentence on the Euclidean flow; the main fix (2655-2660, Cholesky step stability) is in C11. | |
| L10-8 (symbol collisions) | applied (chunk part) | Coupling strength A -> a; quadratic-form matrix A -> M; coupling precisions Lambda_ij, Gamma_ij -> W^(q)_ij, W^(s)_ij (matches the Theory's edge weight W_ij); coupling strengths tau^(q)_ij, tau^(s)_ij -> c^(q)_ij, c^(s)_ij. Lambda_i := Sigma_i^{-1} introduced as belief precision, A_i as anchor. | |
| L16-2 (tau overload) | applied (chunk part) | tau in the chunk is now only the attention temperature. | |
| L16-5 (alpha_ij at 2890) | applied | Transformer alpha_ij removed with the message-passing rewrite. | |
| L16-6 (Gamma overload) | applied (chunk part) | Gamma_ij removed from App. E. | |
| D7 (transformer removal) | applied | Reference to `sec:transformers` and the value-aggregation analogy removed. | |
| D5 (Theory citations) | applied | Theory cited by chapter with descriptive names: Ch. 5, Ch. 6, Chs. 6 and 12, Supplement G Chs. G4 and G5; no Theory labels printed. | |
| D1, D2, D4, D6, D8 | moot | No Wheeler "realizes", Level/fence, RG/renormalization, gauge-vocabulary, or registered-defect text in this chunk (checked by grep after editing; the words "realized quadratic" and "renormalized pool" were also reworded). | |
| D9 / M10 (standalone) | applied | Removed the pointer to the in-preparation meta-entropy note (`Dennis2026metaentropy`) from the App. D proof sketch; it supported no statement. | |
| D13 (style) | applied | No banned words, no spacing macros, no "rather than" in the chunk; long identities split with `aligned`. | |

## 2. Labels removed

- `eq:collected_logs_app` (only reference: orig. 3105, inside this chunk; Step 2 now follows from `lem:kl_sum_identity`).
- `rem:analyticity_role` (only reference: orig. 3160, inside this chunk; content folded into the proof of `lem:richness_app`).

All other original labels of the chunk are kept, including `app:covariance_dynamics` (cited from C01, orig. 187), `sec:raw_alignment_weights` (C13, orig. 3271), `app:conditional_representation` and `thm:representation_app` (C02, orig. 594), and `eq:sigma_fixed_point_map`, `eq:beta_weighted_precision`, `eq:F_i_app`, `eq:geometric_mean_target_app`, `cor:closure_forces_kl`, `lem:richness_app`.

## 3. Labels added

`prop:covariance_fixed_point`, `eq:precision_transport_map`, `eq:precision_linear`, `eq:precision_flow`, `lem:kl_sum_identity`, `eq:kl_sum_identity`, `eq:quadratic_kl_identity`.

## 4. New bib keys needed

- `Vandergraft1968`: J. S. Vandergraft, "Spectral properties of matrices which have invariant cones," SIAM Journal on Applied Mathematics 16(6), 1208-1222 (1968). DOI: 10.1137/0116101. (Metadata confirmed by web search, ACM DL/SIAM listing and NASA NTRS record; used for: the spectral radius of a cone-preserving map is an eigenvalue with an eigenvector in the cone.)
- `Amari2009alpha`: S. Amari, "alpha-Divergence Is Unique, Belonging to Both f-Divergence and Bregman Divergence Classes," IEEE Transactions on Information Theory 55(11), 4925-4931 (2009). DOI: 10.1109/TIT.2009.2030485. (Metadata confirmed by web search; abstract content recorded by L03-4.)

Also used and assumed to exist: `DennisGaugeVFE2026`, `DennisGaugeVFESuppG2026` (D5), `AmariNagaoka2000`, `Amari2016`, `petersen2012matrix`, `nussbaum1988hilbert`, `lawson2001geometric`, `dietrich2016probabilistic`, `bordley1982multiplicative`, `GenestZidek1986` (all present in references.bib).

## 5. Cross-chunk notes

- C02 (orig. 528, 594, 678): scope every invocation of `thm:representation_app` to the frozen-neighbor best response (L03-1 replacement text at 594); delete or qualify "the geometric-mean Boltzmann belief ... follow exactly" at 678; do not claim the Theory fixes the divergence (it declares it, Ch. 12 "Transported divergences and row free energies"; Ch. 6). App. F is retitled "Conditional Representation Theorem for the Transported Relative Entropy"; drop "forward KL" there per L03-2.
- C02 or C00: the consensus potential weights each belief entropy by 1 + B_i (a Gibbs state at temperature 2 relative to Bayesian updating); App. D and App. F now state this. The definition site of the functional could state it once.
- C00 claim-status table: Theorem F is P for the frozen-neighbor best response and does not cover the joint scalar; the App. D covariance fixed point is P with the exact criterion rho(L) < 2 (proved in `prop:covariance_fixed_point`); the physical reading of Sigma_inf = Sigma_0 is S and traces to the entropy weight.
- C14 notation appendix (orig. 3952): the App. E coupling strengths are now c^(q)_ij, c^(s)_ij (in App. E, not `app:gradients`); coupling precisions W^(q)_ij, W^(s)_ij; App. D uses Lambda_i := Sigma_i^{-1}, anchor A_i, alignment coupling strength a, and the map L on Sym(K)^N.
- C06: App. F now cites `sec:meta_agent_definition` for the barycenter; keep that label. The barycenter lines there that call KL(Omega_Ii q_i || q_I) "forward" (L03-2) should drop the adjective.
- C13 (orig. 3271): `sec:raw_alignment_weights` and the raw weights beta-tilde, gamma-tilde are preserved; beta-tilde = c^(q)/2 now.
- C01 (orig. 187): `app:covariance_dynamics` preserved; that sentence's footnote contains `\texttt` identifiers (C01's responsibility under D9).
- `Dennis2026metaentropy` is no longer cited in this chunk; if no other chunk cites it the bibliography entry becomes unused.
- The G2 draft "Relation to the companion theory" appendix paragraph (panel G2, complementarity notes) summarizes the App. D and F relations now stated in the chunk; whoever writes the front-matter pairing paragraph can reuse it.


## Integration pass (2026-09-24)

Editor model: Claude Opus 5.5. After the overfull-box fix below, a wrapper build (with C11) gives 0 errors and 0 overfull boxes. All references resolve against the assembled chunk set, and all citation keys are available (`Vandergraft1968` and `Amari2009alpha` are in the round-two list). Words: 5,081 before, 4,982 after (about 100 removed). No label was removed or added.

### Notes applied or confirmed

| Source | Note | Action |
| --- | --- | --- |
| C00 | rho(L) < 2, status P | Confirmed: `prop:covariance_fixed_point` states and proves the criterion. No change. |
| C02 | App. F is scoped to the frozen-neighbor best response; no nonzero f-divergence gives free-form exponential-family closure of the joint functional | Confirmed present: the theorem title and statement, and the scope paragraph with the second-slot argument and the two-agent witness. No change. |

### Notes rejected

- C06 (orig. 2150 implementation register, GL+ frame-mean item): line 2150 is in C10's range (2015-2159), and C12 has no frame-mean or implementation-register text. The note is misaddressed; C10 should apply it.
- C07 (restate `lem:shadow_mf_optimum` in Appendix G): Appendix G is in C13, and C12 has nothing to change. Moot here.
- C09 (cite postulate P10 where shareability is invoked): C12 invokes no shareability. C10 (line 111) now cites register entry P10, so the entry is no longer uncited. Moot.

### Other edits

- Spacing macros from check-report (lines 2523 and 2611 of the assembly): removed from the variation-of-constants integral, which now has an upright differential with the map applied to (A), and from the Euclidean flow in the Stability subsection.
- Terminology (C02 naming decision):
  - The subsection "Covariance Gradient of the Generalized Free Energy" is retitled "Covariance Gradient of the Per-Agent Block", and its opening now calls F_i agent i's block of the consensus functional.
  - The subsubsection "Gaussian KL divergence" is retitled "Gaussian relative entropy".
  - The App. E title case is fixed, and "KL Divergences" is replaced by "Relative Entropies".
- Gauge vocabulary (D4b): proposition part (iv) now says "a change of frames makes every link orthogonal" in place of "gauge equivalent to orthogonal links".
- Notation: the App. F scope paragraph uses k for the sender index, matching App. A. The (s) superscripts in App. E are model-channel labels and are kept.
- Overfull box: a 19 pt overfull box in the Gaussian-derivative sentence is removed by rewording.
- Tightening:
  - The "two further caveats" sentence after the holonomy paragraph is deleted. The frozen-attention caveat is already in the scope paragraph and the flow caveat in part (ii).
  - The model-channel display in App. E is replaced by one substitution sentence.
  - The corollary proof sketch no longer repeats the degenerate-generator discussion from the statement.
  - The summary paragraph no longer restates Theorem F before its new content: the competing divergences are excluded on the attainable interval without using analyticity.

### Cross-chunk notes

1. C00 table row "Forward relative entropy is the unique f-divergence ...": the adjective "Forward" was dropped here per L03-2. Suggested claim wording: "The transported relative entropy, with the receiver law in the first slot, is the unique real-analytic, linearly coupled f-divergence giving the geometric-mean best response (frozen neighbors)". The "what would change it" entry can read "none; no nonzero f-divergence gives closure of the joint functional (Appendix `app:conditional_representation`)".
2. C10: apply the C06 note on the GL+ frame-mean open item at orig. 2150, which is in C10's range.
