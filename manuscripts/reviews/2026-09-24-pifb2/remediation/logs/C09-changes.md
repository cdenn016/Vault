# C09 change log (original lines 1809-2014)

Chunk file: `chunks/C09.tex` (CRLF preserved). A test build (original preamble + this chunk + `\end{document}`, pdflatex, two passes) gives 0 errors, 0 overfull boxes, and 0 hyperref bookmark warnings. The only undefined references point to labels owned by other chunks, plus `tab:claim_status` (C00). All environments balance.

## 1. Items

| Item | Disposition | Reason / description | New location or label |
| --- | --- | --- | --- |
| D2, M9, L17-5, L13-9 (Part II preamble status language) | applied | Levels, "Level-2/3", "fence F5", and "Outlook rather than Results" are removed. Part II claims now carry S or C and rest on postulates. Each piece of supporting mathematics carries its own P/D status. The pointer now goes to Table~\ref{tab:claim_status}. | `sec:part2_preamble`, para 1 |
| Retitle preamble | applied | "The Level-3 Status of the Speculative Program" becomes "Status of the Speculative Program". | `sec:part2_preamble` |
| L19-2 (declines, not refutes) | applied | New paragraph citing Theory Ch. 1 (scope: no Fisher duration as physical time, no Lorentzian base, agent as a naming decision, "Declining a claim is not refuting it") and Ch. 14 (VFE not a physical action). Both were verified in `c01_program_scope.tex` and `c14_interpretation.tex`. | preamble, para 2 |
| L16-8 (P1-P10 vs Postulate 1-8 collision) | applied | Register P1-P10 kept. The postulate environments are renumbered P4.1-P4.6 as sub-items of P4 via `\renewcommand{\thepostulate}{P4.\arabic{postulate}}` (the environment is used only in this chunk). P2 is now cited in the pullback section. P10 is cited only from C12's range (see cross-chunk notes). | before `post:noncompact` |
| REVIEW sec. 4 "dissolve P1-P10 into status table" | not applied | Spec D2 overrides it: C09 keeps the register. | - |
| Register entries P1, P2, P4, P5 | applied | P1: clock renamed ϑ_i; ordering comes from t; binary registrations carry Wheeler's bit. P2: horizontal block is κ tr(AA) with a declared κ, and the vertical block is the covariant pullback. P4: "on a declared reference section", with pointer to P4.1-P4.6. P5: τ → t, and h-ball isotropy added. | register |
| M7 / L07-7, L12-7, L13-7 (1830-1832 "time emerges") | applied | Replaced with L07-7's statement: t supplies order and orientation, and the clock is a reparameterization-invariant length proposed as internal time (P1). No physical time is presupposed, but an ordering is. Theory Ch. 7 is cited for invariance/unit speed, Ch. 1 for the declined identification. | `sec:time_info`, para 1 |
| L12-1 (1830 "realizes Wheeler's it from bit") | applied | Now reads "measures belief change in bits; it does not model Wheeler's elementary yes-no registration", with a pointer to the new registration subsection. | `sec:time_info`, para 2 |
| L03-7, L14-2, L15-3(c) (distinguishability unit) | applied | Calibrated form N g(δθ,δθ) ≳ 1, "squared Fisher-Rao length", citing Wootters1981 and BraunsteinCaves1994 (CoverThomas2006 dropped here). eq:kl_arclength is stated as exact, with ds² the constant-covariance mean path. The full-family distance can be shorter (Theory Ch. 7 remark, verified). | `eq:kl_arclength` |
| 1835 refinement non-additivity | applied | Numbers 0.7213 → 0.0072 bits over 100 substeps, re-run with `L12_bits_clock.py`. | `sec:time_info`, para 2 |
| L19-9 ("no absolute time") | applied | Replaced with the Theory Ch. 7 statements (verified in `c07_fiber_geometry.tex`): block-diagonal clock bounds, orthogonal-clock exactness criterion, cross-section unit-speed clocks, gauge invariance of the clock of an invariant F. | `sec:time_info`, para 3 |
| L15-3(a) (thermal time mischaracterized) / D6 | applied | Now "the modular flow of the system's own global statistical state". | para 3 |
| L15-3(b) (Caticha entropic time) | applied | Caticha2011entropic (new key) is cited as closest precedent, and the difference is stated. | para 3 |
| L11-12 (proper-time contrast; "runs backward") | applied | Proper time is maximal for an unaccelerated clock at rest; the Fisher clock is stationary for an unchanging belief. | `sec:fisher_arc_length` |
| L03-3, L07-7(b,c) (clock identity scope) | applied | The identity is restricted to an autonomous, single-rate Fisher natural-gradient flow. Added: the driven form (dϑ/dt)² = η(∂_tF − dF/dt); the rate-separated statement (block by block, rate-weighted metric ⊕G_b/η_b, and the unweighted bound citing Theory Chs. 7-8, `eq:hist-clock-metric-dissipation-bound` and `prop:obs-rate-separated-flow`, both verified); frame retraction is not an information clock; finite duration for analytic F (Theory Ch. 7, verified). "Emergent time is ..." now reads "On the P1 reading ...". | `eq:clock_dissipation`, new `eq:clock_driven` |
| L11-12, L15-3(d) (thermodynamic length precedents) | applied | Cites SalamonBerry1983, Crooks2007, and Ito2018 (new key). | after `eq:clock_dissipation` |
| L07-9 (ΔI = (η/2)|ΔF| units) | applied | η is now the dimensionless step of an explicit discrete update. | same paragraph |
| D3(b), L16-2 (τ collisions) | applied | Clock τ → ϑ throughout. P5/causal-route shared parameter τ → t. GL(2,C) and 4D base coordinates (τ,x) → (x^0,x^1,...). ψ_τ → ψ_0 and ψ_{x,y,z} → ψ_{1,2,3}. Curve parameter q(τ) → q(t). No τ remains in the chunk. | throughout |
| D6 (binary registration subsection) | applied | New subsection. Proposition (status D): E_O KL(p(x\|O)‖p(x)) = I(X;O) ≤ H(O) ≤ ln 2. Chain-rule additivity. Under conditional independence each term is ≤ I(X;O_k), with proof. Numerical illustration (0.135, 0.962, 0.0145 bits expected; 9.36 bits for one rare outcome) re-run with `L12_bits_clock.py`. Registration count contrasted with the Fisher clock. States what is not modeled (question choice, irreversibility, complementarity). | new `sec:binary_registration`, `prop:binary_registration`, `eq:registration_bound` |
| D8(c) registered defect (1861 square-root step) | applied | The square-root clause is deleted. √Z_I is stated to be the RMS Fisher-speed ratio, not an expected arc-length ratio. The arc-length ratio is cited as the Theory Ch. 7 open problem (verified text of `open:hist-meta-clock-ratio`), of which the proposition answers the relative-entropy version (L19-4). | after `prop:meta_clock_slowdown` |
| L19-4, L18-5 (1863 false beside record-clock contraction) | applied | 1863 replaced. Both covariance conventions are fixed-kernel Markov images. The contraction is cited as the Theory Ch. 7 same-path record-clock corollary (verified). Meta is never faster than the collective. Pooled/joint = f + (1−f)/N, averaging/joint = that value /N. Only the single-constituent comparison is convention-dependent (averaging Z_I; pooling Nf + (1−f)). Ratios re-run with `L19_meta_clock_markov.py` (agreement ≤ 3e-4 relative). The paper states them as consequences of the proof. | `sec:scale_dependent_time`, para 3 |
| Z_I exact form | applied | Z_I = f + (1−f)/N stated exactly with a two-line proof (verified by L18/L19). Hypotheses made explicit: ε_i uncorrelated with δc, common second moment. | `eq:bit_production_ratio` |
| Pointer "full spectral construction ... Appendix app:rigorous_rg" | not applied (removed) | Appendix I is being condensed (D10/M11), and the review did not confirm a spectral construction there. The Fiedler sentence is kept. | - |
| M1, L13-1, L11-11, L17-1 (1830, 1872, 1892 "realizes"/"precise sense") | applied | No "realiz" remains in the chunk. Now reads "classical information-geometric model", "has the structure Wheeler asks for at the level of metric data", with statuses stated. | `sec:pullback`, closing para of the Gaussian example |
| L12-10 (Wheeler paraphrase at 1872) | applied | Working hypothesis, binary yes-or-no indications elicited by devices, "even the spacetime continuum itself". | `sec:pullback`, para 1 |
| M1 / W2 centerpiece, L11-3, D4(h) (presupposed continuum) | applied | C is "a presupposed smooth index manifold carrying no physical metric". Only metric data are derived; "no continuum" is not modeled. HKM 1976, Malament 1977, and Bombelli et al. 1987 are cited as the route. Base construction is deferred to Supplement B. | `sec:pullback`, para 2 |
| M5, L02-1 (covariant derivative; observer-dependence from beliefs) | applied | New eq:covariant_jet, D_μq = ∂_μq − ρ_*(∂_μU U^{-1})q, with Gaussian form, the frame-stripped equivalence, and eq:induced_metric_full redefined as the covariant Fisher block. Passive gauge covariance cited to Supp. B Ch. B2 (theorem text verified, including "gauge invariant but connection relative"). Stated: invariant under passive re-expression, relative to the declared reference section; the ordinary pullback is not invariant, and the frame-twist block is invariant under neither local action. Differences G_i ≠ G_j at a fixed reference are belief differences. The regulator obstruction concerns only the frame-twist block. | `eq:covariant_jet`, `eq:induced_metric_full`, invariance paragraph |
| L02-2, M4 (coupling κ in combined tensor) | applied | G^(q) is reserved for the PSD Fisher block. The combined tensor is \widetilde G^(q) = κ tr(AA) + G^(q) (new label) with a declared κ. | new `eq:combined_tensor` |
| D9 (software) | applied | Deleted the `\texttt{include\_horizontal}` sentence and "implemented default ... not the training metric". | - |
| L11-7 (units) | applied | New units paragraph: dimensionless tensors (nats per squared base coordinate). A physical length scale L_0 is needed (L_0 chosen to avoid the level index ℓ). No constant speed exists on the algebraic route. | `sec:pullback` |
| L12-3 (loop open) | applied | The pulled-back tensors enter no free-energy term, so the geometry-to-participants arc is missing and is deferred to Supplement B. | `sec:pullback` |
| L15-4 / M3 prior art | applied | Caticha2005, Caticha2019spacetime, Matsueda2013, and the Wootters lineage near the pullback. ErdmengerGrosvenorJefferson2020 on generic hyperbolic Fisher geometry is in the Gaussian example. | `sec:pullback`; Gaussian example |
| D4(e), D3(a) (three tiers shadow; s → ℓ) | applied | The prior tier now uses the lagged predictive prior (transported-copy transition, previous episode), q_I^{(ℓ+1)}. It inherits the parent profile in covariant form (L02-1). | `sec:three_tiers` |
| L14-10 (Friston2017 at 1882) | applied | Attribution deleted; now "whereas predictive-processing accounts usually identify perceptual content with the posterior [Clark2016, Seth2021]". | `sec:three_tiers` |
| Three tiers lab-notebook sentence ("prospective ablation rather than retained historical evidence") | applied | Rewritten as a frozen-slow-channel control; no experiment reported. | `sec:three_tiers` |
| "noumenal" (Kantian register) | applied | Removed from the chunk; Kant is kept in one clause. | - |
| L02-7 (1888-1890 confident regions) | applied | Variable-σ form G = σ^{-2}[dμ·dμ + 2K_q dσ²] (derived; matches L02-7). σ^{-2} is a conformal factor on the mean term. The fiber metric is hyperbolic with curvature −1/(2K_q) (standard computation, stated). | Gaussian example |
| L16-12 (texorpdfstring) | applied | Gaussian example and GL(2,C) subsection titles. | titles |
| M4 / L01-2, L11-2 (1975 "observable") | applied | Now "a property of a declared reference section and has no gauge-invariant content". The pure-gauge mechanism (change of reference U_i → U_i g(c) keeps every Ω_ij and F, and sets tr(A^{(i)}A^{(i)}) = 0 for any agent; 1.90 → 2e-22 re-run with `L11_gl2c_signature.py`) is stated at the section head and after Prop. 4d. The relational invariant tr((A_i−A_j)(A_i−A_j)) is named only as deferred work (Supplement B). | `sec:signature_resolution` head; after `prop:4d_signature` |
| L11-1, M4 (one candidate tensor; 1994 false) | applied | L11-1 text inserted. Combined-tensor instance diag(−2κ + a²/σ², 2κ, 2κ, 2κ) is Riemannian when a²/σ² > 2κ (the script's κ²/σ² > 2 case with an explicit trace coupling). The 1994 sentence "reaches the same indefinite form" is deleted. eq:lor_belief_metric is declared an ansatz with no construction behind it. | after `prop:4d_signature`; temporal-direction subsection |
| L13-8, M4 ("settles signature availability") | applied | Now "exhibits". Availability is immediate from the trace form on gl(K,R), with signature (K(K+1)/2, K(K−1)/2) stated. The split is chosen by P4, and selection (C4) is open. | "Why the no-go..." paragraph; limits paragraph |
| M4 / L11-4(f) (K minimum not sharp) | applied | K ≥ 6 (traceless) and K ≥ 5 (general) hold under the proposition's disjoint-support hypothesis. Without it, K = 5 traceless and K = 4 general constructions exist (re-run). The proof now explains commutation correctly: S by disjoint support, T_a because they are diagonal. | `prop:4d_signature` proof and limits |
| M4 / L11-4(e) (factor 2 at 1962) | applied | Eigenvalues {−2(∂_0ψ_0)², 2Σ(∂_aψ_a)², 0, 0}, verified by the script. | `prop:rank_obstruction` |
| M4 / L11-4(a,b) (GL(2,C) postulates not independent) | applied | `post:regime1` (implied by the collapse) and `post:separable` (a chart choice) are removed as postulates, and the text states why. The general non-separable form Re G = 2(dψ_1⊗dψ_1 − dψ_0⊗dψ_0), det = −4𝒥², is added with the non-separable witness (−0.081, 7.901). `prop:conditional_signature` now uses P4.1-P4.5 and holds wherever dψ_0, dψ_1 are independent. | worked example |
| M4 / L11-4(c) (1910 compact generator) | applied | A compact generator exchanges the timelike direction; only a nilpotent generator removes the form. Postulate retitled "Generator with nonzero trace-square". | `post:noncompact`; worked example |
| L11-4(d) (circularity of the complex route) | applied | Re((ia+b)²) = b² − a², so placing i chooses the timelike direction. | after postulates |
| 1919 "Wick-like continuation" | applied | Now "imaginary coefficient in the Lie algebra; it is not a Wick rotation". | `post:imaginary` |
| Minor: SO⁺(1,1) as orthonormal-frame group | applied | Now "O(1,1), whose identity component is SO⁺(1,1)", and likewise O(1,3)/SO⁺(1,3). | props and example |
| M4 / L11-6, L15-2 (1980 Sylvester; h-isotropy; conformal class) | applied | "by inspection"; h-ball isotropy with Finsler alternative; preferred foliation and analog gravity (BarceloLiberatiVisser2011, new key); HKM 1976 and Malament 1977 for the conformal class, noting that they presuppose the signature; Bombelli et al. 1987 for the scale; c_I carries no units. | `sec:causal_cone_route` |
| G3-6 (parabolic tension only in continuum) | applied | Tension restricted to the continuum limit. Effective Lieb-Robinson-type cone on a bounded-degree graph, with the elementary series bound for linear dynamics (LiebRobinson1972, Marchioro1978). Relation to a base causal structure deferred to Supplement B. | `sec:causal_cone_route` |
| L15-2 (Greensite on dynamical signature selection) | applied | Cited at the section head. The signature section now has citations. | `sec:signature_resolution` head |
| M7, L07-7 (1986 Gram-Schmidt selects a line, not an orientation) | applied | Orientation is inherited from t (equivalently, decreasing F). The box is updated too. | temporal-direction subsection; box |
| Box (derived vs postulated) | applied (corrected, kept) | Line/orientation; declared background chart metric; (ii) marked as an ansatz; (iii) on a declared reference section; new item (v): no single tensor carries both the signature and the clock/sectors. "realized by" replaced. | box |
| D4(b) gauge vocabulary | applied | Uses "passive re-expression" and "change of reference". "Gauge group" → "structure group" in the sector-split paragraph. | pullback and signature sections |
| D13 style | applied | No banned words, no `\;` `\,` `\!` in the chunk, no "rather than" left, no horizontal rules, American spelling. | - |
| L19-7 (meta-agent geometry smoother, 1701) | moot | Location is in C07. | - |
| L11-8 (gravity), L11-7 table rows, L11-3 at 2042, L02-8 | moot for C09 | Locations are in C10. | - |
| G3-2, G3-3, G3-4, G3-5, G3-7, L07-3, L12-5 (81/102/120 parts), L13-2 (1727 part), L13-4, L13-10, L14-1/L15-5/L16-1, L14-4, L14-7, L14-8, L15-7, L16-6, L17-6, L17-9 | moot for C09 | These digest findings sit outside 1809-2014. Parts touching this chunk (Wootters at 1830, 1872 wording) are applied above. | - |
| L16-3 (s vs ℓ) | applied locally | The level superscript in the three-tier text is now ℓ. (s) remains the model channel (D3a). | `sec:three_tiers` |
| L16-10 (unreferenced props) | partially applied | `prop:meta_clock_slowdown` is now referenced. `prop:conditional_signature` and `prop:rank_obstruction` remain unreferenced; they are harmless. | - |

## 2. Labels removed

- `post:regime1`: no references outside C09 (grep of `PIFB2.orig.tex`). Removed because it is implied by `post:collapse` (L11-4b).
- `post:separable`: no references outside C09. Removed because separability is a chart choice (L11-4a).

## 3. Labels added

- `sec:binary_registration`, `prop:binary_registration`, `eq:registration_bound` (D6)
- `eq:clock_driven` (driven clock identity)
- `eq:covariant_jet` (Regime I covariant first jet)
- `eq:combined_tensor` (κ-weighted combined tensor)

Kept with changed meaning: `eq:induced_metric_full` now denotes the covariant Fisher block only. The frame-twist sum is `eq:combined_tensor`.

## 4. New bib keys needed

All three were verified against Crossref on 2026-09-24.

- `Caticha2011entropic`: A. Caticha, "Entropic dynamics, time and quantum theory," J. Phys. A: Math. Theor. 44(22), 225303 (2011), doi:10.1088/1751-8113/44/22/225303. (L15-3 also verified.)
- `Ito2018`: S. Ito, "Stochastic Thermodynamic Interpretation of Information Geometry," Phys. Rev. Lett. 121(3), 030605 (2018), doi:10.1103/PhysRevLett.121.030605. (L15-3 also verified.)
- `BarceloLiberatiVisser2011`: C. Barceló, S. Liberati, M. Visser, "Analogue Gravity," Living Rev. Relativ. 14(1), 3 (2011), doi:10.12942/lrr-2011-3. (L11 also checked.)

The other keys used in the chunk were confirmed present in `references.bib`: DennisGaugeVFE2026, DennisGaugeVFESuppB2026, Wootters1981, BraunsteinCaves1994, SalamonBerry1983, Crooks2007, Caticha2005, Caticha2019spacetime, Matsueda2013, ErdmengerGrosvenorJefferson2020, HawkingKingMcCarthy1976, Malament1977, BombelliLeeMeyerSorkin1987, Greensite1993, LiebRobinson1972, Marchioro1978, plus pre-existing keys.

## 5. Cross-chunk notes

- **C08:** The `\part*{Part II: Speculative Extensions and Outlook}` heading sits at orig 1808, in C08. Consider retitling it "Part II: The Speculative Program" to match the retitled preamble section.
- **C00 (claim-status table):** The Part II preamble points to `tab:claim_status`. Rows affected:
  - clock-dissipation identity: P, autonomous single-rate only, with driven form `eq:clock_driven`;
  - "time emerges": S under P1 (ordering presupposed);
  - meta-clock ratio: D, exact f + (1−f)/N; the arc-length ratio is open (Theory Ch. 7);
  - convention-free contraction: P via Theory Ch. 7;
  - binary registration bound: D (new row, W1/W5);
  - pullback: D (covariant form; passive invariance via Supp. B Ch. B2), with S reading;
  - signature: P under P4, "exhibits" not "settles", a property of a declared reference section with no gauge-invariant content, and not the tensor carrying the clock/sectors.
- **C00 (abstract, introduction):** The abstract (63) and introduction (102, 120, 124) should drop "settling signature availability" and "SO(1,1)-compatible", and should use "exhibits; selection (C4) is open" and the pure-gauge caveat.
- **Section retitles:**
  - `sec:time_info` is now "Time as Registered Change: The Information Clock" (W1).
  - `sec:it_from_bit` is now "Observer-Dependent Geometry: The Pullback Construction" (W2).
  - `sec:pullback` subsection is now "The Pullback Mechanism: From Belief Sections to Metric Data".
  - `sec:signature_resolution` postulates subsection is now "The Postulates for an Indefinite Frame-Twist Form".
  - All labels are unchanged.
- **Postulate numbering:** `\thepostulate` is redefined to `P4.\arabic{postulate}` in C09. No other chunk uses the `postulate` environment in the original. If one is added later, it inherits this numbering.
- **Notation appendix (orig 3952, C14 or the notation owner):** The Part II clock is ϑ_i (not τ_i). The shared update parameter of P5 is t. The signature examples use base coordinates x^0, ..., x^3 and frame components ψ_0, ..., ψ_3. τ remains the attention/entropy temperature only. G^(q) is the covariant Fisher block; \widetilde G^(q) = κ tr(AA) + G^(q) is the combined tensor with declared coupling κ. L_0 is the physical length scale.
- **C10 (collective geometry, consensus metric):**
  - `prop:regulator_obstruction` should be restricted to the frame-twist block, as C09 now states. It should cite the covariant Fisher block's passive invariance (Supp. B Ch. B2) and correct the compact-group argument (M5).
  - Sectors (2033) are eigen-directions of the covariant Fisher block relative to a declared background chart metric (the C09 box says so).
  - Uses of G^(q) at 2031-2042 now mean the Fisher block.
  - 2042's G_i ≠ G_j is now attributed to belief differences at a fixed reference.
- **C12 (gauge invariance as consensus, 2107-2132):** Register entry P10 is still never cited in the body; C12 should cite "postulate P10" where shareability is invoked, or the register entry can be dropped at integration.
- **C07:** C09's three-tier text refers to the lagged predictive prior of `sec:cross_scale_shadows` (transported-copy transition, previous episode). C07's rewrite should keep that label and that reading.
- **Appendix B (orig 2529):** It references `sec:fisher_arc_length` for the "rock near equilibrium" clock. The clock symbol there should be ϑ. C09 now states that the Fisher clock is stationary for an unchanging belief.
- **C13 (open problems):** C3/C4 at 2140-2141 say "the commuting case is settled". Change to "exhibited, as a property of a declared reference section with no gauge-invariant content".
- **C06:** It should keep `sec:meta_agent_threshold`, `sec:meta_agent_state_construction`, `eq:meta_agent_mu_impl`, and `eq:meta_agent_sigma_impl`, which C09 cites.
- **C01:** C09 cites `thm:glk_invariance` for Regime I frame removability. If C01 adds a dedicated removability proposition, integration may repoint the reference at the head of `sec:signature_resolution` to it.

## Integration pass

Words: 7641 to 7434 (about 210 removed). No labels removed or added. A scratch assembly of all chunks built with latexmk exit 0, no LaTeX errors, no undefined references, and no undefined citations.

Notes applied (each confirmed against the text first):

| Note (source) | Action |
| --- | --- |
| C00 status list: pullback D, covariant-block invariance P | The preamble and the opening of `sec:pullback` said that the pullback "and its gauge behavior" were D. Both now give D for the pullback and P for the invariance (Supp. B Ch. B2), matching `tab:claim_status` and W2. |
| C00 status list: regulator obstruction | The preamble's list of supporting mathematics now marks it D, as `tab:claim_status` does. |
| C00 W1-W5 labels | The openings of `sec:time_info` and `sec:pullback` now name W1 and W2 of `tab:wheeler_correspondence`. |
| C02 (F is "the consensus free-energy functional"; "variational free energy" is reserved for the single-agent bound) | Three uses changed. The preamble's list of Part I structures now says "the consensus free energy". The companion-theory sentence was deleted (see below). Box item (v) now says "free-energy minimization". |
| C01 (Regime I removability proposition `prop:regime1_removability` now exists) | The first caveat at the head of `sec:signature_resolution` now cites it beside `thm:glk_invariance`. |
| C10 (P6 requires dim C >= 4) | Added to register entry P6. |
| C10 (define the covariant derivative in `eq:induced_metric_full`; align orig 1877 and 1975 with prop. (b)-(d)) | Already done (`eq:covariant_jet`, the invariance paragraph, the section head). No change. |
| C10 (Part II preamble must use the new C1-C6 titles) | Moot: the preamble cites C1 to C6 by number only. |
| C01 (frame-twist form is "a property of a declared reference section"; O(1,1) identity component) | Already done. No change. |
| C03 (rate-separated flow; no slow frame block; frame metric not Fisher) | Already done. No change. |
| C05 (clock is vartheta) | Already done. No change. |
| C09 self-note (Part II heading, orig 1808) | The heading in C08 is still "Speculative Extensions and Outlook". C08 or the front-matter owner should retitle it "Part II: The Speculative Program". |

Notes rejected: none.

Tightening and other edits:
- Preamble paragraph 2 restated, in five clauses, what the companion theory declines, nearly verbatim from `sec:companion_theory` (C00). It is now one sentence that cites Theory Chs. 1 and 14 and points to that section.
- `sec:time_info` paragraph 1 stated P1 (the clock as internal time) twice, each time with the companion-theory citations. The two statements are merged into two sentences.
- The closing paragraph of `sec:scale_dependent_time` was deleted. It restated that the clock accumulates along the natural-gradient flow, which `sec:fisher_arc_length` already says with `eq:gauge_natural_gradient`.
- `sec:pullback`: "deferred ... and is not attempted here" was simplified. The closing clause "does not model discrete registration" was dropped because the section opening already says so.
- `sec:three_tiers`: a third restatement that differences between covariant pullbacks are belief differences was removed.
- `sec:signature_resolution`: the lab-notebook phrase "earlier versions listed as separate postulates" was rewritten. The "selection is open" sentence after the postulates was removed, because the section head, the limits paragraph, and C4 already state it. The worked example's Wick-rotation sentence duplicated Postulate P4.3 and was removed. In the paragraph after Prop. 4d, the restated pure-gauge argument became a pointer to the section head, and the restated Fisher-block caveat was folded into the combined-tensor sentence.
- `sec:causal_cone_route`: the HKM/Malament statement repeated `sec:pullback` and is now a pointer. It keeps the substantive point that these theorems presuppose the signature and fix the metric only up to a conformal factor. The citations are kept.
- Residual check-report items: no spacing macros, stray `^{(s)}` level superscripts, or Level, fence, RG, or transformer vocabulary remain. Every remaining `^{(s)}` in C09 is the model-channel label (`G^{(s)}`), per D3a. The check-report "UK spelling" hit at assembled line 1671 is a false positive ("surprising").

Table changes needed in C00: none for C09. After these edits the Part II rows agree with the chunk.

## Consistency fixes

| # | Issue | Disposition | Note |
|---|---|---|---|
| 1 | Regulator obstruction status "(D)" in Part II preamble | applied | Changed to "(P)", matching the claim-status table row ("P (obstruction)") and the proved Proposition `prop:regulator_obstruction` in C10. |
| 2 | Box item (i) "three large eigenvalues in D_obs" vs P6 and C10 (|D_obs| = 4) | applied | Now "four large eigenvalues in D_obs, one temporal and three spatial (register entry P6)"; added that R q-dot mirrors the temporal and V_obs the three spatial directions, so item (ii)'s R q-dot ⊕ V_obs stays four-dimensional. Kept the C10/P6 convention. |
| 3 | Self-contradictory "Third, for an autonomous flow that converges, the total clock reading is finite" | applied | Rewritten: finiteness holds for a real-analytic free energy; a smooth free energy admits a converging flow of infinite duration; both attributed to Theory Ch. 7. |
| 4 | Dangling "Why the no-go does not block the route" | applied | Retitled `\paragraph{Where an indefinite form can live.}`. |
| 5 | P4 register: complex variant said to add to the negative-trace temporal requirement | applied | Confirmed against P4.1 and the worked example (T = diag(1,-1), tr T^2 = 2 for both directions). P4 now marks the negative-trace set as the all-real route and says the complex route instead uses a single generator of nonzero trace-square plus pairing, imaginary coefficient, and real-part projection. |
| 6 | "bit count" for a quantity in nats | applied | Line after Eq. clock_dissipation now reads "the information gain of Eq. kl_arclength, in nats, is ΔI = (η/2)|ΔF|" (checked: ΔI = η²∇F^T G^{-1}∇F/2, |ΔF| ≈ η∇F^T G^{-1}∇F). Proposition meta_clock_slowdown now says "ΔI the information gain". The genuine bit statements (0.7213 bits, P1's fixed-granularity bit count, and "bit production" in the ratio, which is unit-free) were left unchanged. |
| 7 | Fisher step length written s (collides with model section) | applied | Now δϑ: "a step of Fisher length δϑ carries δϑ²/(2 ln 2) bits". |
| 8 | Ω_{i,I} comma subscript | applied | Now Ω_{iI}, matching C01, C02, C06. |
| 9 | Lab-notebook numeric aside "(numerically, from 1.90 to 2×10^{-22} ...)" | applied | Replaced with "(Proposition~\ref{prop:regulator_obstruction}(b))"; C10 part (b) proves g = U_i^{-1} gives T_i = 0 exactly. |

Counts: 9 applied, 0 skipped. No labels added or removed; no new bib keys. Checked afterward: the chunk has no spacing macros.
