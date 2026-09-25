# C10 change log (original lines 2015-2159)

Chunk file: `chunks/C10.tex` (rewritten in place, CRLF preserved, 154 lines). A standalone compile of the chunk under the original preamble ran with 0 LaTeX errors (undefined references to other chunks expected). Final scans: no "Level", "fence", "realiz", "RG", "renormaliz", "transformer", "\texttt", "Yang-Mills", banned phrases, or `\;` `\,` `\!` in the chunk; no reference to any D7 deleted label, to `sec:epistemic_status`, `sec:scope_limitations`, or `sec:gauge_curvature_conjecture`. Lowercase "level" occurs only as the hierarchy index (D3a). Consciousness section: 510 words.

## 1. Item table

| Item | Disposition | Reason or description | New location or label |
|---|---|---|---|
| M5 / L19-2 (2022 "only candidate gauge-invariant observable") | applied | Replaced by the covariant-Fisher-block statement: invariant without orbit average, relative to connections; further invariants cited (Theory Ch. 14, Ch. 7); orbit average needed only for the frame-twist block | `sec:consensus_metric`, new Eq. `eq:consensus_metric_covariant` |
| M5 / L02-1 (restrict `prop:regulator_obstruction`) | applied | Proposition retitled "Regulator obstruction for the frame-twist block", four parts (a)-(d) with a short proof; label kept | `prop:regulator_obstruction` |
| M5 / L11-10 (2024 compact-G reasoning) | applied | Finite product Haar measure is normalizable for compact G; obstructions are the continuum limit (maps C to G not locally compact; lattice average grows as eps^-2) and infinite Haar volume for noncompact GL(K_q), SO(1,3) | prop. parts (c), (d) |
| M5 / L11-9(e) (2042 G_i != G_j partly gauge artifact) | applied | Observer-dependence attributed to differences of frame-stripped beliefs only; ordinary pullback difference partly gauge artifact | `sec:observer` para 1 |
| M5 / L02-1 (define nabla^(i) in `eq:induced_metric_full`) | partially applied | Covariant derivative defined and used inside C10, with the derivation d q-hat = rho(U^-1) nabla q; the display itself lives in C09 | cross-chunk note |
| L11-2 (frame-twist pure gauge) | applied | Prop. part (b): c-dependent right translation preserves every transport and belief and sets tr(A A) = 0 for any agent | prop. (b); C3 |
| L11-1 (Lorentzian tensor vs carrier tensor) | partially applied | Sectors paragraph: PSD G_i has no temporal direction, Lorentzian reading needs P4/P5; C3: no tensor shown both Lorentzian and carrier of clock and sectors. Main fix belongs to C09 | `sec:observable_sectors`; C3 |
| M8 / L11-3 / L02-5 (2033 g_0 vs 2042 "no intrinsic metric") | applied | g_0 declared a computational background; C is a presupposed smooth index manifold carrying no physical metric, with background density and fiducial chart metric; dimension, topology, smooth structure are inputs; departure from "no continuum" stated | `sec:observable_sectors`, `sec:observer` para 3 |
| M8 / L02-5 (rank G_i <= dim C; abs D_obs = 4 unrealizable on R^2) | applied | P6 requires dim C >= 4 and the hierarchy much larger; no instance on the working base | `sec:observable_sectors` para 3 |
| L02-8 (2033 operational pencil generically singular) | applied | Declared map through the means, J^(o) = dmu^T Lambda_o dmu; singularity stated; well-posed version on a complement of ker J^(o) | `sec:observable_sectors` para 2 |
| L11-7 (units paragraph) | applied | Both tensors dimensionless (nats); external length scale L_* and constant speed required; algebraic route supplies neither, causal route postulates speed without units; P7 "territory into map" sentence removed | `sec:phenomenological_interpretation` para 1-2 |
| L11-7 (entropy row) | applied | Missing ingredient now: identification with physical ensemble, k_B, phase-space measure (Jaynes 1957); differential entropy is coordinate dependent | `tab:physical_correspondences` |
| M8 / L11-7 (alpha and m_e/m_p paragraph) | applied (cut) | Paragraph cut; its advance-specification criteria moved into C6 with a stated momentum-transfer scale (1/137 Thomson limit to 1/128 at M_Z); m_e/m_p dropped | C6 |
| M8 / L11-8 (gravity) | applied | Reduced to four sentences: P8 reading (S), exact constant-conformal curvature statement, explicit list of what is not derived (no field equation, source, Newtonian limit, G; Riemannian; no gravitational mass, equivalence principle cannot be posed), contrast with Jacobson 1995 and Carlip 2014; M_eff contrast deleted | `sec:gravity_pullback` |
| L11-9(a)(b) / M8 (measurement analogy) | applied | Classical comparison class DeGroot 1974 and Aumann 1976; quantum Darwinism (Zurek 2009) as the quantum relative; einselection contrast kept | `sec:measurement_analogy` |
| L11-9(c) (2042 "structurally relational and QBist") | applied | "closest to the relational type; with QBism shares only the personalist starting point" | `sec:observer` para 2 |
| L11-9(f) / L12-9 (2042 "meets the quantum-foundations standard") | applied | L12-9 replacement adopted (observer-dependent representation and belief only; holonomy obstruction as counterpart of cross-perspective links, Adlam-Rovelli) | `sec:observer` para 2 |
| L11-9(d) / L12-4 (1767 vs 2028 gauge invariance) | applied (C10 side) | 2028 statement ("consistency requirement consensus must respect, not a symmetry consensus generates") retained and moved to the gauge-invariance section; the 1767 deletion belongs to C08 | `sec:gauge_invariance_consensus` |
| L15-6 (2113 physics list) | applied | Replaced by "constraining the form of the action, for example by forbidding explicit gauge-boson mass terms and fixing the universality of gauge couplings" | model-alignment subsection |
| L15-4 (Zurek 2009, Carlip 2014, Mueller 2020 in range) | applied | Zurek 2009 at macroscopic objects and measurement; Carlip at gravity; Mueller 2020 at observer-dependent reality | several |
| L15-7 / minor 2084 (Lavis-Streater; Born rule built in) | applied | "derives Schrodinger evolution with the Born rule built into the representation"; Lavis-Streater 2002 cited for the Frieden critique. Caticha2015 and JohnsonCaticha2011 metadata are bib-agent items | `sec:measurement_analogy` |
| L11-5 (2079 "rock appears certainly there") | applied | Mean back-action suppressed (O(eps), O(eps^1/2) Fisher), precision back-action not suppressed (factor 1/(1+beta) for every eps); "rock" generalized to a high-precision agent | macroscopic-objects subsection |
| W3 (one world out of many; Wheeler's third question; Follesdal dictum) | applied | New opening paragraph of the section: third question, Follesdal quotation via Wheeler 1990, "checked with one's fellows" paraphrase, consensus stationary point as formal counterpart (D for stationarity, S for reading), three departures stated | `sec:collective_geometry` intro; section retitled |
| D10 / L13-4 (consciousness) | applied | Condensed to 510 words; status S or C declared at the top; panprotopsychism stated as the author's interpretive stance; combination problem as status C; Tononi/Dehaene free-energy attribution removed | `sec:consciousness` retitled "Consciousness: An Interpretive Stance" |
| L13-1 / D1 (2091 "realization" of the Lahav-Neemeh law) | applied | "proposes an explicit candidate"; scope narrowed using Regime I removability (Theorem glk_invariance) | `sec:lahav_convergence` retitled |
| L01-5 (2090 per-agent shift phi_i -> phi_i + xi_i) | applied | Removed; qualia paragraph now uses a passive re-expression of one agent's frame, which changes no invariant | qualia subsection |
| L16-3 / D3a (2095 phi^(s), phi^(s+1); scale-N) | applied | Superscripts removed with the rewrite; "scale" replaced by "level" (level-0 agents, cross-level coupling) | consciousness, C5 |
| M1 / L19-3 / L17-10 (2154 apex closure in the defensible core) | applied | Conclusion: "an energy-level apex that is, in any generative reading, a declared root, the formal residue of ... no tower of turtles" | `sec:global_conclusion` |
| M1 / M9 / L13-9 (2156 "epistemic grade rather than subject matter") | applied (deleted) | Sentence and the fence-register clause removed | `sec:global_conclusion` |
| M1 / L11-11 / L13-1 (2158 C1-C6 into decidable problems) | applied | C1-C5 mathematical problems, C6 a derivation target; solving them decides questions about the formalism, not the participatory reading | open-problems intro, C6, conclusion |
| L13-8 / M4 (2140, 2156 "settles") | applied | "exhibits"; availability immediate from the indefinite trace form; selection (C4) open | C3, conclusion |
| L19-6 (C1 as an estimator problem) | applied, adapted | L19-6 text without the transformer-limit framing: operational loop-holonomy theorem cited (Theory Ch. 10); estimator for a named target system with noise model, held-out statistic, tolerance, and a frozen-link control arm; base-connection version deferred to Supplement B | C1 |
| L13-5 / 2138 ("principal experimental anchor", gauge curvature conjecture, meta-entropy anchor) | moot / applied | Pointer to the language gauge-curvature conjecture removed (D7 removes that material); meta-entropy frustrated-lattice anchor removed (in-preparation note) | C1 |
| G3-7 (2146 "abelian RG group") | applied | Coarse-graining steps compose as a one-parameter semigroup; the cross-level object would pair that semigroup with G; no construction attempted; "Yang-Mills" removed | physical-content cluster |
| M10 / L17-3 (2148 chi = 1/alpha) | applied (dropped) | Not provable here without the in-preparation note's model; replaced by pointers to Theory open problems (Ch. 12 persistent hierarchy, Ch. 13 adaptive family) | scale-question cluster |
| L19-5 (decidable conjecture; frozen-prior arm) | applied | Pairing-selection conjecture (Theory Ch. 14) cited as the one decidable test of the participatory reading of the formalism; frozen-attention-prior arm named for the prospective study | scale-question cluster; conclusion |
| C5 / L14-3 (quantum fiber; Fields 2022) | applied | Kept as the "how come the quantum" pointer (W5); Fields et al. 2022 cited; "electromagnetic phase factor" aside dropped | C5 |
| L13-6 / M2 (2121 Friedman vs 1800) | applied | "constitutive but revisable constraint ... in Friedman's relativized sense; what the Discussion disavows is the apodictic a priori" | altered-states subsection |
| L13-10(a) (2127 Laudan-Leplin) | applied | "break ties pragmatically; whether such criteria are evidential (Laudan-Leplin 1991) or pragmatic (van Fraassen 1980) is left open"; "over convergent realism" removed | scientific-knowledge subsection |
| L13-10(b) / minor 2125 (Laudan 1977) | applied | Laudan1984 replaced by Laudan1977 | scientific-knowledge subsection |
| L12-6 / L13-6 (2125 "noumenal manifold", 2129 continuum status) | applied | C described once as a presupposed smooth index manifold carrying no physical metric; departure from Wheeler's loop answer to regress stated | scientific-knowledge subsection |
| G1-3 (2150 GL+ frame mean) | applied | Afsari 2011 (left-invariant metric, only left-equivariant) and Pennec-Arsigny 2013 exponential barycenter (bi-invariant); additive form is the first fixed-point iterate; open item restricted to the choice of convention (a gauge choice) | open mathematical items |
| M17 (implementation register: kinetic-metric test) | applied | Postulate needs its own second-order equation of motion; dynamics are first order with Fisher friction; table mass row rewritten as stiffness | open mathematical items; table |
| D9 / L17-3 (implementation register software items) | applied | Removed: top-down measure emission, autograd regression guard, off-diagonal assembler, untied model frames, computational overhead versus dot-product attention; "recoverable evidence" and "simulations do not instantiate" wording removed | open-problems cluster 3 |
| D7 (2154-2155 transformer recovery, WikiText sweep; K_q = 768) | applied | References to `thm:transformer_recovery` and `sec:scaling_validation` removed; K_q = 768 example replaced by general K_q(K_q+3)/2 | conclusion; sectors |
| L09-2 (2154 architecture claim) | moot | Transformer and sweep material removed (D7) | none |
| L08-9 (transformer prior art) | moot | Transformer removal | none |
| L17-1 (global conclusion never names Wheeler) | applied | Conclusion rewritten around W1-W5 with statuses and the Theory's "declines, not refutes" sentence | `sec:global_conclusion` |
| L17-11 (three conclusions) | partially applied | Global conclusion rewritten as the single conclusion; merging the Part I conclusion is C08's, moving Methods is C11's | cross-chunk note |
| L19-2 class B, L17-10 (Theory citations in range) | applied | Theory cited by chapter with D5 keys: Supp. B Ch. B2, Ch. 2, 7, 10, 12, 13, 14 | several |
| L19-7 (meta-agent geometry smoothing prediction) | not applied | The prediction sits at 1701 (C07); C10 contains no smoothing prediction | none |
| L14-7, L14-9, L14-10, L14-12, L16-1, L16-5 | moot | Locations outside C10 or bibliography metadata; L16-5's alpha at 2148 is gone with chi = 1/alpha; Afsari2011 now resolves in the bib | none |
| Minor 2025 (tr(F F) raises indices with no metric) | applied | Display removed; "every curvature invariant vanishes, since F = 0" | `sec:consensus_metric` |
| Minor 2033, 2084, 2125, 2127, 2146 | applied | See rows above | |
| D2 (status language) | applied | All "Level-2/3" and "fence F2/F3/F5" removed; statuses P/D/S/C and Table `tab:claim_status` used | throughout |
| D3 (notation) | applied | Clock in table as vartheta_i; D_KL typography; level index | throughout |
| D4 (b),(d),(g),(h) | applied | Passive re-expression and change of reference named; mass as stiffness with Fisher friction; consensus metric not the only invariant; C as presupposed index manifold | throughout |

## 2. Labels removed

None. All original labels in the chunk are kept: `sec:collective_geometry`, `sec:consensus_metric`, `prop:regulator_obstruction`, `sec:observable_sectors`, `sec:observer`, `sec:phenomenological_interpretation`, `tab:physical_correspondences`, `sec:speculative_physics`, `sec:gravity_pullback`, `sec:measurement_analogy`, `sec:consciousness`, `sec:lahav_convergence`, `sec:gauge_invariance_consensus`, `rem:kretschmann`, `sec:open_problems`, `sec:global_conclusion`.

## 3. Labels added

- `eq:consensus_metric_covariant` (presence-weighted average of covariant Fisher pullbacks).

## 4. New bib keys needed

- `Aumann1976`: R. J. Aumann, "Agreeing to Disagree", The Annals of Statistics 4(6), 1236-1239 (1976), doi:10.1214/aos/1176343654.
- `Jaynes1957`: E. T. Jaynes, "Information Theory and Statistical Mechanics", Physical Review 106(4), 620-630 (1957), doi:10.1103/PhysRev.106.620.
- `PennecArsigny2013`: X. Pennec and V. Arsigny, "Exponential Barycenters of the Canonical Cartan Connection and Invariant Means on Lie Groups", in F. Nielsen and R. Bhatia (eds.), Matrix Information Geometry, Springer, Berlin, Heidelberg (2013), pp. 123-166. Title, book, and pages as verified by panel G1; DOI believed to be 10.1007/978-3-642-30232-9_7 (bibliography agent to confirm).

Keys used that the bibliography already holds: DennisGaugeVFE2026, DennisGaugeVFESuppB2026, Afsari2011, Fields2022, Mueller2020, Zurek2009, LavisStreater2002, Carlip2014, Jacobson1995, degroot1974, Laudan1977, AdlamRovelli2022. `Laudan1984` is no longer cited from C10.

## 5. Cross-chunk notes

- C00 (front matter): Section `sec:collective_geometry` is retitled "One World out of Many: Collective Geometry, Observable Sectors, and Observer-Dependent Reality" and is the W3 home; the conclusion refers to W1-W5 through `sec:introduction`. The abstract and intro (orig. 63, 124) must drop "only (sole) candidate gauge-invariant observable" and "settles signature availability". Claim-status table rows to update: consensus metric "only candidate" is false and replaced; `prop:regulator_obstruction` is P, restricted to the frame-twist block; the physical-correspondences table is S; C1-C5 are mathematical problems (C), C6 is a derivation target; gravity is S placeholder; the rock covariance back-action is not suppressed. Intro O1 "scale-0 agent" should read "level-0" for consistency with C10.
- C01: the Role A/Role B paragraph (orig. 194) says gauge-invariant observables are recovered from Role-B quantities by orbit averaging (pointing to `sec:collective_geometry`); this is now false for the Fisher block. C10 uses Theorem `thm:glk_invariance` for Regime I removability; if C01 adds a separate removability proposition, the integration pass may point `sec:lahav_convergence` to it.
- C09: `eq:induced_metric_full` must define nabla^(i) as the Regime I covariant derivative, D q_i = dq_i - rho_*(dU_i U_i^{-1}) q_i, and cite Supp. B Ch. B2; C10's consensus metric, sectors, observer-dependence, and qualia text assume this. Orig. 1877 ("the local-gauge Haar orbit average ... would require a regulator") and 1975 must be aligned with prop. (b)-(d). The conclusion cites the binary registration proposition "in Section `sec:time_info`". Part II preamble mentions of C1-C6 must use the new titles: C1 estimating loop holonomy; C2 consensus geometry; C3 four-generator construction beyond the commuting case; C4 selection of the 1+3 split; C5 density-operator level-0 fiber; C6 dimensionless-ratio derivation (a derivation target). P6 now carries the realizability condition dim C >= 4.
- C07: the conclusion uses "one-episode-lagged predictive prior" and "declared root, the formal residue of no tower of turtles"; C07's rewrite must supply both. `sec:cross_scale_shadows` and `sec:ouroboros` are referenced.
- C08: C10's Friedman sentence assumes the Discussion (orig. 1800) disavows the apodictic a priori, not the constitutive one (L13-6), and C10 relies on the 1767 gauge-invariance clause being deleted. C10 no longer references `sec:gauge_curvature_conjecture`. The Part I conclusion should merge into `sec:global_conclusion` (L17-11) without attention-recovery claims. C10 references `sec:discussion` for the Kantian analogy.
- C11: Appendix B (`app:examples`) must carry L11-5's corrected covariance back-action; C10 now states precision reduced by 1/(1+beta) for every eps and mean back-action O(eps) (O(eps^1/2) in Fisher length).
- C05: the table's mass row points to `sec:mass` (first-order flow, Fisher metric as friction tensor) and the open items point to `sec:velocity_quadratic` (postulate needs its own second-order equation of motion).
- C06: G1-3 conventions for the GL+ frame mean are stated in C10's open items; `sec:meta_agent_variational` should identify the convention as a gauge choice. `PennecArsigny2013` is a shared new key.
- C12: C10's W3 paragraph cites `thm:representation_app` for the fixed-neighbor (frozen-neighbor) best response only, consistent with the M15 scoping.
- Bibliography: add the three keys above; `Caticha2015` and `JohnsonCaticha2011` metadata corrections (L15-7) remain bib-agent items.

## Integration pass

Words: 5909 to 5717 (about 190 removed). No labels were removed or added. A scratch assembly of all chunks built with latexmk exit 0, with no LaTeX errors, undefined references, or undefined citations.

Notes applied (each confirmed against the text first):

| Note (source) | Action |
| --- | --- |
| C00 (O1-O4 dissolved into the "Interpretive stance" paragraph `sec:cognitive_first`; "agent at level zero") | "stated as O4 in Section sec:introduction" now points to the interpretive stance of `sec:cognitive_first`, and "level-0 agents" now reads "agents at level zero". The C5 item title "density-operator level-0 fiber" is kept because other notes cite it by that name. |
| C00 (single ontology name) | Neither "information-geometric structuralism" nor "pan-agentic structuralism" occurs in C10; no change. |
| C00 W1-W5 table | The W3 opening and the conclusion now cite `tab:wheeler_correspondence` directly, no longer "the correspondence table of Section sec:introduction". |
| C09 (G^(q) is now the covariant Fisher block; the combined tensor is `eq:combined_tensor`) | `sec:consensus_metric` spoke of "which block of Eq. induced_metric_full is averaged" and defined its own symbol G^F_i with its own nabla^(i). C09 now makes `eq:induced_metric_full` the Fisher block alone and writes the covariant derivative D_mu q_i in `eq:covariant_jet`, so the two chunks clashed. C10 now refers to the blocks of `eq:combined_tensor`, writes G^(q)_i, and points to `eq:covariant_jet` and `sec:pullback`. The duplicated derivation of the frame-stripped identity and of passive invariance is removed, since C09 carries it. The sectors subsection defines G_i := G^(q)_i. |
| C09/C10 notation (physical length scale L_0) | C10's L_* is now L_0, matching C09 and the notation note. |
| C01 (Regime I removability proposition `prop:regime1_removability`) | The Lahav-Neemeh subsection now cites it instead of `thm:glk_invariance`. Its restatement of the frame/transport/residual dictionary is compressed to a pointer to `sec:cognitive_reference_frames` (C01). |
| C08 (relational/QBist wording; Brukner, Frauchiger-Renner, Adlam-Rovelli) | `sec:observer` paragraph 2 read "closest to the relational type; with QBism shares only the personalist starting point". It now matches C08: the framework is of the relational and QBist type only in sharing QBism's personalist starting point and RQM's comparison between perspectives, and it departs from QBism by having no quantum content and by adding a transport law and a consensus functional (pointer to `sec:discussion`). The L12-9 sentence on facts versus representation is kept. |
| C08 (C described once; "noumenal by analogy only") | The two mentions of "noumenal" (in `sec:observer` and `sec:phenomenological_interpretation`) are merged into one, which points to `sec:discussion`. |
| C02 ("variational free energy" reserved for the single-agent bound) | In the P7 paragraph, "information, the variational free energy and relative entropies measured in nats" now reads "information, measured in nats by the free energy and the relative entropies". |
| C09 (the conclusion cites the binary registration proposition) | The conclusion's W1 sentence now also cites `prop:binary_registration`. |
| C09 (restrict `prop:regulator_obstruction`; cite Supp. B Ch. B2) | Already done; no change. |
| C01 (sec:dual_role_rigor residual subgroup; additive shift; background density and rank bound) | Already done; no change. |
| C05 (delete the autocorrelation-omega and assembler items) | Already absent; no change. |
| C07 (apex wording; lagged prior) | Already done in the conclusion; no change. |
| C08 (no gauge-curvature conjecture in C1; mass row as stiffness) | Already done; no change. |
| C11 (weakened rock back-action) | Already done; no change. |

Notes rejected: none.

Tightening and other edits:
- The first paragraph of `sec:phenomenological_interpretation` nearly repeated C09's units paragraph (`sec:pullback`); it is now two sentences pointing there.
- In the measurement analogy, the description of quantum Darwinism repeated the macroscopic-objects paragraph above it and C08. It is now a back-reference, and Zurek2009 is still cited.
- In the scale cluster of the open problems, the pairing-selection conjecture was stated a third time in the paper (C00 scope, here, and the conclusion). It is now a pointer to `sec:scope_limitations` that keeps the Ch. 14 citation.
- In C3, the relational trace-form display duplicated C09; it is now a pointer to `sec:signature_resolution`.
- In the time row of the physical-correspondences table, the presupposed ordering parameter belongs to register entry P1 (which supplies order and orientation), not P5; corrected.
- "rather than supply structural analogies" now reads "not merely supply structural analogies".
- Residual check-report items: none present (spacing macros, `^{(s)}` used as a level superscript, and Level, fence, RG, or transformer vocabulary). `G^{(s)}_i` in the gravity subsection is the model-channel label (D3a). The check-report "UK spelling" hit at assembled line 1947 is a false positive ("arising").

Table changes needed in C00 (C00 is not in this group):
1. Consider adding a Part II row for `sec:gauge_invariance_consensus`: "the gauge structure of physics reflects cognitive architecture", status C, possibly unfalsifiable. C10 states this thesis and the C00 scope paragraph points to it, but no row records it.
2. Consider adding a Part II row for the observable, subthreshold, and internal sectors: they are defined relative to a declared background chart metric, and P6 requires dim C >= 4, so it has no instance on the working base R^2. Status: postulate P6 (S).
3. The row "Orbit-averaged consensus metric ..." could state that the presence-weighted covariant consensus metric (`eq:consensus_metric_covariant`) is gauge invariant with no orbit average (P, via Supp. B Ch. B2). At present this is only implicit in the pullback-invariance row.

## Consistency fixes

| # | Reader issue | Disposition | Description |
|---|---|---|---|
| 1 | Rock precision factor "1/(1+beta) for every epsilon"; epsilon vs delta | Applied | Confirmed against C11 (`sec:rock_derivations`, stationary precision delta^{-1}(I + delta beta Lambda)/(1+beta)) and C05 (delta is the precision scale of `sec:mass`). Now reads "reduced by a factor that tends to 1/(1+beta) as delta -> 0 and stays away from one at every delta"; the object's precision scale epsilon is renamed delta throughout the paragraph, with a pointer to `sec:mass`. The lattice spacing varepsilon in `prop:regulator_obstruction` is a different symbol and was left unchanged. |
| 2 | Nonexistent "frame regularizer ||grad phi||^2" | Applied | No such term appears in any chunk. The parenthetical now reads "(alignment, simplicity, unification)". |
| 3 | Frame-mean convention cross-reference | Applied | The gauge-choice identification is `prop:parent_frame_gauge` in C06 (`sec:meta_agent_definition`). Now reads "which Proposition~\ref{prop:parent_frame_gauge} (Section~\ref{sec:meta_agent_definition}) identifies as a gauge choice". |
| 4 | C1 stated as an empirical protocol but classed as mathematical | Applied (restate option) | C1 now states a mathematical problem: a consistent estimator of loop-holonomy conjugacy classes from finitely many normalized population records under a stated noise model, with a finite-sample error bound. The target-system protocol (held-out statistic, pre-fixed tolerance, frozen-link control arm) follows as its empirical application. The section opening, the Conclusion, and the C00 table row ("C1--C5 are mathematical problems") are therefore consistent, and none of them needs to change. |
| 5 | "No multiscale result is available" | Applied | Now reads "No result on how the hierarchy behaves with growing agent count or depth is available; the exact coarse-graining statements and the nested bound (Table~\ref{tab:claim_status}) hold at fixed finite size." |
| 6 | Duplicated relational, QBism, and Mueller paragraph in `sec:observer` | Applied (adapted) | Cut to two sentences. The first sentence states the classical, global-frame scope and keeps the Brukner and Frauchiger-Renner citations. The second points to `sec:discussion` for Brukner's theorem, the cross-perspective-links question (AdlamRovelli2022), QBism (Fuchs2017, DeBrotaFuchsSchack2020), and Mueller2020. Frauchiger-Renner stays cited locally because C08 does not cite it, so the pointer claims only what the Discussion contains. The reciprocal pointer is in C08 and cannot be edited from this chunk; see the cross-chunk note. |

Cross-chunk note (C08): C08 line 17 ("it is of the relational and QBist type (Section~\ref{sec:observer})") now points to a section that defers back to the Discussion for this comparison. Drop that "(Section~\ref{sec:observer})" pointer so that only the C10 -> C08 direction remains.

Labels added or removed: none. New bib keys: none.
