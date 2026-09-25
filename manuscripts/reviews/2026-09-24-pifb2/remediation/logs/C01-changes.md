# C01 change log (original lines 136-515)

Scope: `chunks/C01.tex` rewritten in place (CRLF preserved). Standalone build of the chunk with the original preamble: 0 LaTeX errors (16 pages; undefined references are expected outside the full document). Script re-run to confirm the one number-bearing new statement: `scripts/L01_gauge_laws.py` (3e) lattice Bianchi residual 4.7e-14, single plaquette 2.6; (1a)-(1c) overlap-relation checks 1.4e-10; `scripts/L02_fisher_curvature.py` random-plane maximum 0.2601 at Sigma = I (so +1/4 is not the supremum). No numbers were inserted into the paper; the new identities carry algebraic proofs. Theory statements cited were read in `Theory/c01_program_scope.tex` (160-161), `c02_geometry.tex` (1-420), `c08_two_timescales.tex` (86-98), `c12_multiscale_vfe.tex` (666-830), `b02_base_direction_geometry.tex` (77-84).

## (1) Items

| Item | Disposition | Reason / description | New location or label |
| --- | --- | --- | --- |
| M4 | partially applied | Added the Regime I removability proposition with proof directly after `thm:vanishing_holonomy`; stated that frame content at a point is relative to fields held fixed (observation likelihood, fixed-frame environmental agents, frozen priors), with the dressing-field method (`Fournel2014Dressing`) and Francois's artificial-versus-substantial criterion (`Francois2019Artificial`) as precedent; added the pointer from `thm:glk_invariance` to the proposition. The 1975 "observable", coupling kappa, K minimum, and signature parts of M4 lie in C09; (R2) relabel is moot (transformer removed). | `prop:regime1_removability`, `eq:regime1_removability`; paragraph after it; sentence after the f-divergence extension |
| M16 | partially applied | Trichotomy paragraph (passive re-expression, change of reference, active group = one copy of G, Theory Ch. 2); 353-358 interpretation replaced per L01-3; orientation reversal imposed; Regime II subsubsection retitled "Independent Links on the Interaction Graph" citing the Theory's graph-link definition (Ch. 2); 368 "required by signature" removed; Yang-Mills vocabulary either removed or cited to `Yang1954`, `Utiyama1956`, `WuYang1975`. Parts at 925-927 and the frame-flow equivariance (C03), 2090 (C10), 3801 (C14), 1780 (C08) are outside the chunk. | `sec:gauge_covariance_principle` (retitled), `sec:connection_forms`, `sec:discrete_regime_ii` (retitled), `eq:orientation_reversal` |
| M2 / D4(h) (146-153) | applied | One status for C: "presupposed smooth index manifold carrying no physical metric", noumenal by analogy only; "derived from agentic structure" and "logically prior" removed; added the explicit departure from Wheeler (loop versus index floor, "no continuum"; W5). | base-manifold subsection |
| M5 (385) | applied | Per-edge twist `U_i^{-1} Omega_ij U_j = exp(delta_ij . G)` and its conjugacy class stated as invariants at one point (Theory Ch. 2, per-edge twist-invariance proposition); loop holonomies carry the remaining invariant content. | `sec:discrete_regime_ii`, paragraph after `eq:omega_gauge_law` |
| 373 | applied | Graph links are not base transport (Theory Ch. 1); not a discretization of a connection on C; only holonomy available in the zero-dimensional limit. | opening of `sec:discrete_regime_ii`; Regime convention paragraph |
| D6 boundary of a boundary (L01 verified item 19) | applied | New paragraph: Regime I cocycle as delta-of-a-coboundary, lattice Bianchi identity on a 3-simplex with orientation reversal (algebraic proof in one line), no conservation law claimed (status S). | `sec:boundary_of_boundary`, `eq:lattice_bianchi` |
| 418 (causal mask, V3_Transformer, multi-head, f_W bilinear) | applied | Removed; kept one general sentence that a state-dependent link must satisfy orientation reversal and the vertex law, and that an ambient-frame input breaks the latter unless re-expressed. | end of `sec:discrete_regime_ii` |
| L08-4 (causal triples) | moot | Transformer material removed; no general causal sentence kept. | none |
| L08-1, L08-5 (418 per-head holonomy; stale codebase) | moot | Sentences deleted with the transformer material. | none |
| 449 executable table (D9) | applied | `table*` deleted with its software content. | `tab:executable_contract` removed |
| 509 flat background measure | applied | Stated that every integral uses the Lebesgue density dc of the flat chart and the sector thresholds use its metric; the pullbacks enter no term, so the geometry-to-agents arc of Wheeler's loop is not constructed (L12-3; W5; deferred to Supplement B); rank of a pullback at most dim C, so at most two nonzero eigenvalues on R^2 (L02-5). | "Flat base manifold" paragraph |
| Minor 316 | applied | Image of a single exponential = matrices with a real logarithm, containing a neighborhood of the identity, proper for K_q >= 2. | `sec:transport`, `sec:local_trivialization` |
| Minor 343 | applied | "Baker-Campbell-Hausdorff expansion" renamed Zassenhaus formula. | `sec:gauge_covariance_principle` |
| Minor 380 | applied | "left-conjugation ... right-conjugation" replaced by left multiplication by g_i and right multiplication by g_j^{-1}. | before `eq:omega_gauge_law` |
| Minor 385 (G3-2) | applied | Wilson locator now `Eqs.~(3.27)--(3.28)`; Creutz cited without locator (G3 could not verify the equation, and Ch. 5 is "Fermions"). | after `eq:omega_gauge_law` |
| Minor 403-405 (L16-5) | applied | Wilson coupling beta -> beta_W; the beta_W -> infinity limit moved out of the display and restricted to compact G. | `eq:wilson_action` |
| Minor 429 (L02-4) | applied | Noncommutativity separated from curvature; group curvature metric dependent, no bi-invariant metric on GL+(K_q) (Milnor 1976); +1/4 stated as not the supremum; base-curvature and gravity reading reduced to status C pointer. | "Curvature Structure: Four Notions" (retitled) |
| Minor "identity component of O(1,1)" | moot for C01 | Occurs at original line 1974, in C09; not in this chunk. | none |
| L01-1 | applied | See M4. | `prop:regime1_removability` |
| L01-2 | partially applied | Residual-subgroup claim replaced: frame-twist form invariant under constant per-agent actions but not under the local change of reference U_i(c) -> U_i(c) g(c), which leaves every link and the functional invariant and can zero any one agent's form; "property of a declared reference section, not an observable". The 1976 sentence is in C09. | `sec:dual_role_rigor` (retitled "Precedents and the frame-twist form") |
| L01-3 | applied | Replacement text: standard law for a right principal action with h = U_j^{-1} U_i; right Maurer-Cartan form obeys the displayed law with g = Omega_ij. | after `eq:theta_overlap_relation` |
| L01-4 | applied | delta_ji = -delta_ij imposed with the Theory's definition cited; backtrack remark. | `eq:orientation_reversal` |
| L01-5 | partially applied | Three actions named once in the chunk; "the version we use throughout the body" and "only the base-local action is the physical gauge group" deleted; 2090, 925, 3801 are other chunks. | `sec:gauge_covariance_principle` |
| L01-9 | applied | "natural discrete realization" replaced; "signature-related" requirement removed; north-pole illustration relabeled as base holonomy, distinct from graph holonomy. | `sec:field_strength`, `sec:discrete_regime_ii` |
| L01-10 | partially applied | Transport-hierarchy BCH accuracy pointer removed; parent frame called a gauge convention by the removability proposition. 1573, 1644, 2649 are other chunks. | `sec:transport_hierarchy` |
| L02-1 | partially applied | "Gauge-invariant observables are recovered by averaging over the gauge orbit" removed; covariant Fisher pullback stated as passively gauge invariant without orbit averaging (Supplement B, Ch. B2). The regulator proposition is in C10. | "Two roles" and `sec:dual_role_rigor` paragraphs |
| L02-4 | partially applied | 429 part applied; 1526 is C05. | curvature subsection |
| L02-5 | partially applied | 146-153, 429, 508-509 applied; 2033-2042 in C10. | base-manifold subsection, flat-base paragraph |
| L12-3 | partially applied | Missing arc stated at 509; 1677 is C07. | flat-base paragraph |
| L12-6 | applied | Departure from Wheeler stated; 146 versus 153 resolved. | base-manifold subsection |
| L13-6 | partially applied | 146 fixed ("noumenal by analogy only"); 77, 79, 1800, 2125, 2129 are other chunks. | base-manifold subsection |
| L14-4 | applied (chunk sites) | 142 and 418 Yang-Mills uses removed; 353/358 cite `Yang1954`, `Utiyama1956`, `WuYang1975`, `Nakahara2003`; Wilson paragraph cites `Yang1954`; 214 bundle dictionary cites `WuYang1975`; 225 cites `Kobayashi1963`. | throughout |
| L16-3 | applied | scale index s -> l in the Agent definition, transport hierarchy, l_max; SO(3) spin label l_k -> j_k to avoid the collision. | `sec:agent_definition`, `sec:transport_hierarchy`, `sec:gauge_group_choice` |
| L16-5 | applied | beta_W; relaxation alpha -> epsilon_rel. | `sec:discrete_regime_ii` |
| L16-6 | applied (chunk) | Omega_gamma path-ordered formula removed (base connection deferred); Omega_{i,I} -> Omega_{iI}. Gamma_gamma at 653 is C02. | Regime convention, `sec:transport_hierarchy` |
| L16-9 | applied | `\mathrm{KL}` -> `D_{\mathrm{KL}}`; `\mathrm{tr}/\mathrm{Tr}` in the Gaussian formulas -> `\operatorname{tr}` (Wilson trace keeps `\operatorname{Tr}`). | throughout |
| L16-10 | not applied | `thm:vanishing_holonomy` prefix kept (D14: no renaming unless required; the PDF prints "Lemma" correctly). | none |
| L16-4, L17-3, L17-8 | applied (chunk) | All `\texttt` identifiers, the two KL_REGULARISER_EPS footnotes, the SO(7)/GL+(7) checked-in path, the Agent constructor, ym_bounded/ym_action_form, init_twist_scale, loader normalization, and the executable table removed. | throughout |
| L18-3 | applied | Twist classes (385) and the single-point emptiness of Role B beyond fixed-frame pairings (194) stated, with Theory Ch. 2. | "Two roles" paragraph, `sec:discrete_regime_ii` |
| L18-4 | partially applied | 373 text and retitle applied; 1780 restatement is C08. | `sec:discrete_regime_ii` |
| D1 | applied | No "realiz*" remains; W5 cited at the base-manifold departure and the missing loop arc. | - |
| D2 | applied | Two "fence F2; Section epistemic_status" pointers and the closing Level-1/2/3 sentence replaced by status language and `Table~\ref{tab:claim_status}`. | Agent definition; last paragraph |
| D3 | applied | (a) l for levels; (b) no clock symbol in the chunk; (c) beta_W; (d) `D_{\mathrm{KL}}`, `^\top`. | - |
| D4 | applied | (a) "renormalization-group spine" -> hierarchical coarse-graining; (b) trichotomy, "zero-dimensional gauge theory" and "unreduced GL(K_q) gauge theory on a single point" deleted; (c) Regime II as independent graph links with orientation reversal; (e) priors as one-episode-lagged predictive priors (Theory Ch. 12), never a same-time posterior read; (f) top prior as a declared root; (g) orbit-average claim replaced; (h) C status. | - |
| D5 | applied | Theory cited by chapter: Ch. 1 (graph links are not base transport), Ch. 2 (frames, agents, active group, graph links, twist invariance, trivializing criterion), Ch. 8 (fast/slow typing), Ch. 12 (episode joint, declared root), Supplement B (base connection) and B Ch. B2 (covariant pullback). No Theory label printed. | - |
| D7 | applied | Removed refs to `sec:transformers` (4) and `sec:scaling_validation` (1); PriorBank, "transformer limit", "validated as a working language model", bilinear-attention justification of GL(K_q), and multi-head aside removed; figure caption says "zero-dimensional limit". | - |
| D9 | applied | See L17-8 row; "no artifact-backed run" and prospective zero-dimensional arm sentence replaced by the Theory's single-point setting. | flat-base paragraph |
| D13 | applied | No banned words, no spacing macros, zero "rather than" left; American spelling. | - |
| Lahav-Neemeh subsection (sec:cognitive_reference_frames) | applied (condensed) | Kept as structural correspondence (status S); added that in Regime I the residual equals the divergence of frame-stripped laws; pointer changed from `sec:lahav_convergence` to `sec:consciousness`; the Alice/Bob composition sentence (which relied on additive per-agent shifts) deleted. | `sec:cognitive_reference_frames` |
| Other deletions | applied | "pan-agentic ontology contemplates density-operator fibers" aside; the Nickel 2017 hyperbolic-embedding citation (machine learning); "slowly varying frames so first-order BCH averaging is accurate" assumption (not needed; L01-10). | - |

## (2) Labels removed

- `tab:executable_contract` (the executable-contract table). Referenced once in `PIFB2.orig.tex` at line 2502 (chunk C11).

## (3) Labels added

- `prop:regime1_removability`, `eq:regime1_removability` (Regime I removability proposition)
- `eq:orientation_reversal` (delta_ji = -delta_ij)
- `sec:boundary_of_boundary` (paragraph), `eq:lattice_bianchi` (lattice Bianchi identity)

All other original labels of the chunk are kept, including `sec:regime_convention`, `sec:dual_role_rigor`, `sec:local_trivialization`, `sec:cognitive_reference_frames`, `sec:field_strength`, `sec:discrete_regime_ii`, `eq:connection_form`, `eq:theta_overlap_relation`, `eq:field_strength`, `eq:edge_relaxed_omega`, `eq:omega_gauge_law`, `eq:discrete_holonomy`, `eq:wilson_observable`, `eq:wilson_action`, `thm:glk_invariance`.

## (4) New bib keys needed

None. Keys used beyond the original chunk: `Yang1954`, `Kobayashi1963`, `Milnor1976`, `Wheeler1990`, `Fournel2014Dressing`, `Francois2019Artificial` (all already in references.bib), `WuYang1975`, `Utiyama1956` (G3 list; present in references.bib at check time), `DennisGaugeVFE2026`, `DennisGaugeVFESuppB2026` (D5). The Attard-Francois-Lazzarini-Masson dressing-field review named by L01 is not cited; the existing `Fournel2014Dressing` carries the precedent.

## (5) Cross-chunk notes

1. C00: the chunk references `tab:claim_status` and the label W5. Status changes for the table: "the framework is a zero-dimensional GL(K) gauge theory" is deleted (at a point the active group is one global G; frames removable in Regime I); new P row "Regime I frames removable at a point" (`prop:regime1_removability`); new S row "boundary-of-a-boundary parallel" (`sec:boundary_of_boundary`, no conservation law). The abstract and introduction should not call the construction a gauge theory on a point.
2. C11 (original 2502) cites `tab:executable_contract`, which is deleted; drop that reference.
3. C10 (original 2024) cites `sec:dual_role_rigor` for "the residual-subgroup statement" and `sec:cognitive_reference_frames` for the "genuine non-invariance". Both now live in `sec:dual_role_rigor`, which states that the frame-twist form is invariant under constant per-agent actions but changes under the local change of reference U_i(c) -> U_i(c) g(c), a symmetry of the functional; the regulator proposition should be restricted to that block (M5) and cite the covariant Fisher pullback (Supplement B, Ch. B2), as this chunk does.
4. C10 (original 2090): the additive per-agent shift phi_i -> phi_i + xi_i should read U_i -> g_i U_i (the chunk states the Zassenhaus restriction). The chunk no longer references `sec:lahav_convergence`; C10 may drop or keep that label.
5. C09: the frame-twist form is now declared "a property of a declared reference section, not an observable" in C01; the 1976 sentence and "observable" must agree. The minor comment "identity component of O(1,1)" (original 1974) belongs to C09.
6. C03 (925-927): C01 states the functional is invariant under change of reference with the observation term included, and that passive re-expression fails only when a fixed field is exempted; C03's symmetry-breaking paragraph should match (L04-1). C01 cites `sec:timescales` for "the functional contains no frame-gradient term"; C03 must keep the statement that no frame regularizer is included (original 958). C01 cites `sec:symmetry_breaking` for fixed-frame environmental agents. The frame-flow equivariance of L01-8 is C03's.
7. C08 (1780-1796): "Regime II" now means independent links on the interaction graph with orientation reversal; an independent base connection is deferred to Supplement B. The gauge-curvature conjecture must be stated in graph-holonomy terms or removed with the language material (D7); C01 no longer mentions it.
8. C06: C01 states that the parent frame cancels from every constituent prior in Regime I (removability proposition) and calls its choice a gauge convention; it no longer asserts an O(||phi||^2) BCH accuracy for the frame average.
9. C07: the Agent definition now reads the priors as one-episode-lagged predictive priors under a transported-copy transition (Theory Ch. 12) and the top prior as a declared root; `eq:cross_scale_shadow` and `sec:cross_scale_shadows` are referenced and must survive.
10. C02: `eq:connection_form` and `eq:field_strength` are kept. C01 no longer defines the path-ordered symbol Omega_gamma, so C02's Gamma_gamma at 653 (L16-6) should be defined locally or dropped, since base transport is deferred.
11. C10 (2033-2042): C01 now states that C carries a background Lebesgue density and a fiducial flat chart metric used for integration and sector thresholds, and that a pullback has rank at most dim C (at most two nonzero eigenvalues on R^2).
12. Bibliography agent: add DOI 10.1103/PhysRevD.10.2445 to `WilsonConfinement1974` (G3-2).
13. Retitled headings: "Passive Re-expression, Change of Reference, and the Active Group" (`sec:gauge_covariance_principle`), "Independent Links on the Interaction Graph" (`sec:discrete_regime_ii`), "Precedents and the frame-twist form" (`sec:dual_role_rigor`), "Curvature Structure: Four Notions", "Gauge group: GL(K_q) and its compact subgroups" (`sec:gauge_group_choice`).

## Integration pass (2026-09-24)

C01 was integrated together with C00 by one editor. Build and pattern checks as recorded in the C00 log: private full build with 0 errors, 0 undefined references, 0 undefined citations; C01 has 0 banned words, 0 spacing macros, 0 "rather than", 0 `^{(s)}`, 0 transformer, 0 Level, 0 fence, 0 RG hits. CRLF preserved.

### Notes applied

| Source | Note | Action |
| --- | --- | --- |
| C00 | Corrected statuses the owning chunks must match (Regime I removability P, one active global G P, cocycle/Bianchi P identities with S parallel, gravity S) | Confirmed in text. The curvature subsection's "whether induced curvature can be identified with physical gravity is an open program, status C" contradicted the table's gravity row (S); now "a structural placeholder of Part II (Section sec:speculative_physics)". |
| C02 | Labels sec:discrete_regime_ii, sec:connection_forms, eq:connection_form, eq:field_strength, thm:vanishing_holonomy, thm:glk_invariance, eq:transport_def, sec:gauge_group_choice, sec:agents_as_sections, sec:one_rung must survive | All present. |
| C03 | C03 cites thm:glk_invariance and sec:transport; removability proposition available | No C01 change needed. C01's citation of sec:timescales for "no frame-gradient term" repointed to sec:frame_evolution, where C03 now states that no frame regularizer is included. |
| C05 | Line-429 part of L02-4 (group curvature metric dependent; noncommutativity separate) | Confirmed already applied in "Curvature Structure: Four Notions". |
| C07 | C01 must supply the Regime I removability proposition | Present (prop:regime1_removability). |
| C09 | Repoint removability citation if C01 adds a proposition | Proposition exists; the repoint is C09's. |
| C09 (GENERAL) | G^(q) now denotes the covariant Fisher block only | The Role A/B and frame-twist paragraphs called "the ordinary pullbacks G_i^(q)" frame dependent, which contradicts C09's invariant G^(q). Now "the ordinary fixed-frame pullbacks", and the covariant pullback is named G^(q)_i of sec:pullback, "formed with covariant derivatives, passively gauge invariant without any orbit average, relative to the chosen connection" (C09's wording; the earlier "each agent's own Regime I connection" dropped). |
| C10 | Role A/B paragraph must not claim invariants come from orbit averaging | Confirmed already corrected. |
| C11 | Right-translation paragraph cites sec:gauge_covariance_principle | Label present. |
| C12 | texttt footnote at app:covariance_dynamics pointer | Confirmed no texttt remains in C01. |
| C14 | beta_W and vartheta match the notation table; table references eq:transport_def | beta_W matches tab:notation; C01 has no clock symbol. The table defines Omega_Ii as child-to-parent transport U_I U_i^{-1}; C01 called Omega_iI "the constituent-to-parent transport" and said it was used in the bottom-up aggregation. Rewritten: Omega_iI is the parent-to-constituent transport for top-down priors, and its inverse Omega_Ii carries constituent beliefs into the parent frame for the aggregation. |
| GENERAL (C07) | C07's base-measure paragraph points to sec:transport for the background density | That density is declared in C01's "Flat base manifold" paragraph, not in sec:transport. Added label sec:flat_base to that paragraph (and the base-manifold subsection now points to it); C07 should repoint. |

### Notes rejected

None rejected. The C00 note's shorthand "rock covariance reduced by 1/(1+beta)" (in its note list addressed to C01) has the direction wrong relative to C11 (precision is reduced); C01 does not discuss the rock, and the C00 table row states the precision correctly.

### Other edits (tightening, no result, proof, or citation removed)

- Regime convention paragraph: dropped the restatement that Maurer-Cartan flatness is established once elsewhere and compressed the forward pointer on the frame-twist form (the full statement stays in sec:dual_role_rigor).
- Two-roles paragraph: dropped the repeated "active group is one copy of G" sentence (kept in sec:gauge_covariance_principle and the zero-dimensional paragraph) and the base-transport deferral already stated in the regime convention.
- Real-exponential non-surjectivity was stated three times; the two earlier statements (local-trivialization caveat, transport paragraph) now point to the canonical statement after Theorem thm:glk_invariance.
- Statistical manifolds: dimension sentence compressed; "We state that caveat once here" and the later Gaussian-paragraph repetition of the Gaussian-choice caveat, curvature citation, and dimension removed.
- After Proposition prop:regime1_removability: the sentence repeating the proposition's list of fixed fields removed.
- Passive re-expression paragraph: repeated invariance of every relative-entropy term (stated in the preceding paragraph) removed.
- Field-strength and Regime II paragraphs: repeated deferrals to Supplement B and the repeated "graph links are not discretizations" sentence removed (both stay in the regime convention).
- Working framework: opening merged; matched-bundles paragraph no longer restates the structural fact at length; zero-dimensional paragraph no longer repeats the transported-Gaussian formula from sec:transport.
- Flat base: "with periodic boundary conditions to avoid edge effects" deleted; it is simulation bookkeeping and contradicted the same paragraph's statement that compact base manifolds without boundary are given up.
- Closing paragraph: dropped "the dimensional decomposition" (no such construction remains in the paper); the last sentence now names the consensus free-energy functional, matching C02's opening.
- Cognitive-frames paragraph: two sentences on the frame as a field merged.

Labels added: sec:flat_base. Labels removed: none.

Word count: 8,968 before the pass, 8,589 after (about 380 words removed).

## Consistency fixes

| Issue | Disposition | Description |
|---|---|---|
| "At the top level the prior $r_i^{(\ell_{\max})}$ is a declared root" (line 118) | applied | Confirmed: the Agent definition names $r_i$ the hyper-prior and $p_i$ the prior. Changed "the prior" to "the hyper-prior" in that sentence. |
| "in the language of Section~\ref{sec:introduction}, $\mathcal{C}$ is a domain of inquiry, not a thing" (line 11) | applied | Confirmed: "domain of inquiry" appears in no chunk; C00's interpretive-stance paragraph (`\label{sec:cognitive_first}`, C00 line 90) says "The base $\mathcal{C}$ is an index manifold of contexts, not a physical thing." Replaced with "as stated in the interpretive stance (Section~\ref{sec:cognitive_first}), $\mathcal{C}$ is an index manifold of contexts, not a physical thing." |
| Base-point symbol $c^*$ in the overlap figure and caption (lines 144-165) | applied | Confirmed: all seven $c^*$ occurrences were in the figure (node label, $q_i(c^*)$, $q_j(c^*)$, $\Omega_{ij}(c^*)$) and its caption, while C00 and the flat-base paragraph of C01 use $c_*$. All changed to $c_*$. The reader's statement that C02 uses $c_*$ could not be confirmed (C02 contains no base-point symbol of either form); the fix stands on C00 and C01 alone. |

Labels added or removed by this pass: none.
