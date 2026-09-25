# C00 change log (original lines 1-135: preamble, abstract, introduction, status and scope, related work)

Chunk file: `chunks/C00.tex` (174 lines after revision, CRLF preserved). Test build of the chunk followed by `\end{document}` with pdflatex: 0 errors, 0 overfull and 0 underfull boxes; only references to labels in other chunks and not-yet-built citations are undefined.

## 1. Items

| Item | Disposition | Reason or description | New line or label |
| --- | --- | --- | --- |
| M1 (thesis at 81) | applied | Organizing claim rewritten as the Wheeler correspondence (L12 thesis statement: three strands, with participation across scales as the fourth part and coarse-graining as its mechanism); no "realizes" anywhere in the chunk; "slogan", "doctrine without mathematics", "informal philosophy" (81, 102, 120) deleted | intro para 3 (line 68) |
| M1 (keep-and-drop paragraph) | applied | New paragraph after the organizing claim: kept (observer-relativity, one world out of many, derived metric and duration, participation of collectives in priors); dropped (registration with complementarity and question choice, no continuum, law without law, self-excited circuit, open loop through induced geometry deferred to Supp. B) | line 70 |
| M1 (W1-W5 table) | applied | Correspondence table with status column | `tab:wheeler_correspondence` (lines 72-88) |
| M1 (F5 rewrite, L19-5 wording) | applied | Testability paragraph in Scope: decidable conjecture about the formalism (Theory Ch. 14), not observational; participatory-physics reading possibly unfalsifiable | Scope para 4 |
| M2 (C described four ways; 77, 79) | applied (chunk sites) | C is "a presupposed smooth manifold of contexts carrying no physical metric", "noumenal by analogy only"; "common noumenal substrate" and regress-blocking floor reworded; departure from "no continuum" declared | intro para 2, keep-and-drop, stance |
| M3 (positioning, L12-5/L15-1/L13-3/L14-3) | applied | Intro para 1 now runs Wheeler, Wootters, Zeilinger, Hardy, Chiribella-D'Ariano-Perinotti, Masanes-Mueller, Hoehn, Mueller 2020, Fuchs 2017 (participatory realism by name), RQM, Caticha; states the framework is not a reconstruction and supplies transport law and consensus functional | line 64 |
| M3 (related work rebalanced) | applied | Physics paragraph expanded: thermodynamic length (Salamon-Berry, Crooks), Wootters, Caticha 2005/2019 spacetime, Erdmenger-Grosvenor-Jefferson caution, Zurek 2009, Fields 2022; FEP/Bayesian-mechanics paragraph condensed; observer-first paragraph gives Fuchs 2017 its own sentence | lines 169-173 |
| M4 ("settles signature availability", 63) | applied (chunk sites) | Abstract no longer mentions signature; Scope says "exhibits ... under postulate P4 ... a property of a declared reference section with no gauge-invariant content; selection open" | Scope para 1 |
| M5 ("only/sole candidate gauge-invariant observable", 63, 124) | applied (chunk sites) | Covariant Fisher block invariant without orbit average (Supp. B Ch. B2, "Passive gauge covariance of the covariant pullbacks", verified in `b02_base_direction_geometry.tex`); regulator only for frame-twist block, obstructions are continuum limit and noncompact Haar volume | Scope para 1 |
| M9 (Levels 1-3, F1-F6) | applied | Retired; status codes P, D, S, E, C plus "postulate" defined once; P-code vs P1-P10 distinction stated | `sec:epistemic_status` retitled "Claim Status and Scope" |
| M9 (claim-status table) | applied | Built from REVIEW section 6 with corrected statuses; transformer and WikiText rows dropped (D7); added rows for D6/D11 statements (registration channel, Bianchi parallel, removability, rho(L) < 2, stiffness/friction, declared root) | `tab:claim_status` (longtable) |
| M9 (abstract) | applied | New 230-word single-paragraph abstract; opens with Wheeler's question and the thesis; no citations, no section references, no code, no fit coefficients | lines 51-53 |
| M9 (template comments 21, 50) | applied | Natbib/cite option comments and ORCID comment removed; `\usepackage{cite}` kept | preamble |
| M9 (venue class/template, REVTeX port) | not applied | Venue choice is the author's (REVIEW Q1); article class kept so the preamble keeps working | - |
| M10 (implementation statements in abstract) | applied | "checked-in multi-agent implementation", "executable research program", "working architecture/implementation", "computationally implemented", "reference repository", "checked-in active configuration" removed from the chunk | - |
| M10 (Relation to the companion theory, L19-1) | applied | New subsection citing DennisGaugeVFE2026 by chapter (5, 6, 7, 9, 11, 12, 13; 1 and 14 for declined identifications), DennisGaugeVFESuppG2026, DennisGaugeVFESuppB2026; vocabulary translation; one sentence naming DennisGLKAttention2026 as home of the transformer limit | `sec:companion_theory` (line 163) |
| M11 / L06-1 / D4(a) at 81 | applied | "RG spine" removed; one sentence states the construction is an exact block-variable pushforward in Kadanoff's sense plus truncation, with no rescaling, coupling-space flow, or fixed point, citing kadanoff1966scaling, Kadanoff1975, KadanoffHoughtonYalabik1976 and Theory Ch. 11 (finite-network obstruction verified in `c11_network_coarsegraining.tex`) | line 68 (the one intended "renormalization-group" occurrence) |
| M18, L09-1 to L09-5 (sweep in abstract, 98, 116, 126) | moot | Transformer and WikiText material removed from the paper (D7); the RoPE/diagonal-covariance caveat and schedule-confound paragraph at 126 deleted with it | - |
| M19 (transformer section) | moot | D7 | - |
| D7 (no attention recovery or WikiText in abstract/intro) | applied | Abstract, intro contributions, Level 1, F1, F6, scope para 126, related-work "computational instantiation recovering transformer attention" and "analytic recovery of transformer attention" all removed; references to `sec:transformers`, `sec:scaling_validation`, `thm:transformer_recovery` removed; O1 pointer to `sec:transformers` removed | - |
| D2 (Part I title) | applied | "Part I: Defensible Core" -> "Part I: The Construction" | line 60 |
| D3(a) level index | applied | "scale s+1 / scale-s" -> level-$(\ell+1)$ / level-$\ell$; "scale-0" -> "level zero" | - |
| D3(d) typography | applied | $D_{\mathrm{KL}}(q_i\|\Omega_{ij}q_j)$ in table; $^\top$ in covariance action | - |
| D4(b)/(c) gauge vocabulary | applied (chunk) | Table rows state one active global G and passive frames; "independent links on the interaction graph" | `tab:claim_status` |
| D4(f) declared root, "no tower of turtles" | applied (chunk) | W4 row and keep-and-drop paragraph | - |
| D4(h) base manifold | applied | "presupposed smooth manifold of contexts carrying no physical metric" | intro para 2 |
| D9 software | applied | See M10 row; no `\texttt` in chunk | - |
| D13 style | applied | 0 banned words, 0 `\,` `\;` `\!`, 0 "rather than" in chunk (was many), American spelling | - |
| Minor 45, 75 (ASCII quotes, L15-10e) | applied | Title and Wheeler quotations use `` '' | lines 38, 64 |
| Minor 75 (working hypothesis, 1989 essay; L12-10, L15-10g) | applied | "In an essay delivered in 1989 and published in 1990 ... offered as a working hypothesis ... binary yes-or-no indications" | line 64 |
| Minor 79, 1800 (PPC, L13-10c, L15-9) | applied (79 site) | "inverts the Primacy of Physics Constraint of Ladyman and Ross's naturalized metaphysics [Ladyman2007] while sharing the relational emphasis of ontic structural realism [Ladyman1998]" | stance paragraph |
| Minor 81 (three names for one ontology, L17-9) | applied | One name kept: "cognitive-first structural monism" | stance paragraph |
| Minor 66 (keywords, L17-9) | applied | Participatory realism, It from bit, Gauge theory, Information geometry, Variational free energy, Multi-agent inference ("Transformer architectures", "Active inference", "Emergent spacetime" dropped) | line 55 |
| Minor 130 (Swingle "show", L15-10c) | applied | "Tensor-network proposals read the geometry ... off entanglement" | line 169 |
| Minor 132 (Tononi, Dehaene not FEP) | moot | The comment concerns line 2105; neither is cited in the chunk | - |
| L12-1 (bit semantics) | partially applied | Chunk-level: keep-and-drop paragraph states KL-in-bits is not refinement additive and points to the binary registration channel of Section `sec:time_info` (C09 adds it per D6); sites 1830, 1872 belong to C09 | line 70 |
| L12-6 (floor vs loop) | applied (chunk) | Departure declared in keep-and-drop | line 70 |
| L12-8 (no question selection, no complementarity) | applied | Keep-and-drop paragraph | line 70 |
| L12-9 (RQM cross-perspective links) | applied (related-work site) | Network holonomy with independent links as belief-level counterpart of the Adlam-Rovelli question; the 2042 site is C10 | line 173 |
| L13-1 (realization voice) | partially applied | No realization voice in chunk; F5 rewritten; other sites belong to C07, C09, C10 | - |
| L13-2 | applied | Keep-and-drop paragraph | line 70 |
| L13-4 (O1-O4 vacuity) | applied | O1-O4 enumerate dissolved into one "Interpretive stance" paragraph with status S, stating that universal agency and transport exclude no system (Kretschmann1917, Norton1993); moving the ontology to a philosophy venue not applied (author decision; D10 keeps the consciousness section) | `sec:cognitive_first` paragraph |
| L13-6 | applied (chunk sites 77, 79) | One status for C | - |
| L13-8 | applied (63 site) | See M4 row | - |
| L13-9 | applied | Level taxonomy retired | - |
| L14-6 (connection/sheaf Laplacians, gauge-equivariant nets) | applied | SingerWu2012, HansenGhrist2021Discourse, cohen2019gauge; He2021GaugeEquivariantTransformer omitted as transformer material (D7) | line 171 |
| L15-8 (RQM wording) | applied (related-work site) | "relative to other physical systems, any system serving as an observer" | line 173 |
| L15-10(d) (Umegaki citation) | not applied | No verified bib entry for Umegaki 1962; the original also named it without citation | - |
| L15-9 (Floridi 2008, French-Ladyman 2003) | partially applied | Ladyman1998 added; Floridi 2008 and French-Ladyman 2003 not added (metadata not verified in L14/L15/G3) | - |
| L16-4 | partially applied | Template comments removed; abstract one paragraph without citation; `\date{\today}` and article class kept (venue decision) | - |
| L16-9 | partially applied | KL typography in chunk uses $D_{\mathrm{KL}}$; `\KL` and `\softmax` macros kept in preamble for other chunks | - |
| L17-1 | applied | See M1 | - |
| L17-2 (venue) | not applied | Author decision (REVIEW Q1, Dennis2025it outcome unknown) | - |
| L17-3 items 1-2 | applied (chunk) | Abstract implementation sentence removed; companion paragraph added; the 678 citation itself is C02's | - |
| L17-4 (restructure) | partially applied | Chunk-level only: Levels/fences replaced, related work rebalanced, title shortened ("Mathematical Foundations and Computational Implementation" dropped), Part I retitled | - |
| L17-5 | applied | One status system and one table | - |
| L17-6 | partially applied | Part I retitled; moving O1-O4 into Part II not done (stance paragraph now carries status S explicitly) | - |
| L17-9 | applied | One ontology name, keywords, title, ML jargon removed from intro; physics definition of variational free energy given | - |
| L19-1 | applied | See M10 row | `sec:companion_theory` |
| L19-2 (63, 124 sites) | applied | See M5 row; Part II preamble sentence belongs to C09 | - |
| L19-5 | applied | F5 rewrite and frozen-attention-prior control in Scope (Theory Ch. 14, `prop:phil-seeded-contrast-formation`, verified) | Scope paras 2 and 4 |
| L19-8 | applied | Kernel-equivalence sentence (Theory Ch. 5, "Observation-interaction kernel equivalence", verified) | stance paragraph |
| G3-8 (metadata) | moot for chunk | Bibliography agent | - |
| G3-2, G3-3, G3-6, G4-8, L01 notes, L05/L06 notes, L10-4, L12-10 (1705, 1872 parts), L19-3, L19-4, L19-6, L19-7, L19-9 | moot for chunk | Locations fall in C01, C07, C09, C11, C14 (digest carries them for cross-reference only) | - |
| L08-5 | moot | Transformer codebase sentence at 418 is C01 and removed by D7 | - |
| GLOBAL L01-6, L01-7, L08-2, L08-6, L08-7, L09-8 | moot | Transformer and sweep material deleted (D7) | - |
| GLOBAL L02-9, L09-7 | moot for chunk | Lines 2660, 2185 (C11) | - |
| GLOBAL L14-11, L15-8 (1767 site) | moot for chunk | Line 1761/1767 (C08); the related-work RQM wording was fixed here | - |
| GLOBAL L15-10 (a, b, f, h) | moot for chunk | Other chunks or bib | - |
| GLOBAL L16-7 (notation collisions) | moot for chunk | Notation appendix (C14); intro now only points to Appendix `sec:notation` | - |
| GLOBAL L17-4 | partially applied | See L17-4 row | - |
| GLOBAL physics notes (sweep cuts, prospective protocol) | applied (chunk) / moot | Sweep gone; protocol referred to only by one sentence with its control arm | - |

## 2. Labels removed

None. All five original labels (`sec:introduction`, `sec:cognitive_first`, `sec:epistemic_status`, `sec:scope_limitations`, `sec:related_work`) are kept. `sec:cognitive_first` now sits on the "Interpretive stance" paragraph (referenced from 2527, C11).

## 3. Labels added

- `tab:wheeler_correspondence` (W1-W5 correspondence table)
- `tab:claim_status` (claim-status longtable, required by D2)
- `sec:companion_theory` (subsection "Relation to the Companion Theory")

Preamble addition: `\usepackage{longtable}` (loaded before hyperref).

## 4. New bib keys needed

None beyond the D5 and D12 lists. Keys used from those lists: DennisGaugeVFE2026, DennisGaugeVFESuppG2026, DennisGaugeVFESuppB2026, DennisGLKAttention2026, Wootters1981, Zeilinger1999, Hardy2001, ChiribellaDArianoPerinotti2011, MasanesMueller2011, Hoehn2017, Mueller2020, Caticha2005, Caticha2019spacetime, SalamonBerry1983, Crooks2007, Zurek2009, ErdmengerGrosvenorJefferson2020, Fields2022, SingerWu2012, HansenGhrist2021Discourse, Ladyman1998, Kadanoff1975, KadanoffHoughtonYalabik1976. Existing keys newly cited in PIFB2: kadanoff1966scaling, Kretschmann1917, Norton1993, cohen2019gauge, Caticha2019. At check time every cited key resolved in `references.bib`.

## 5. Cross-chunk notes

- Status system: `tab:claim_status` is the canonical home. Every "Level 1/2/3", "fence Fk", and "(fence Fk; Section~\ref{sec:epistemic_status})" pointer elsewhere should become plain status language or `Table~\ref{tab:claim_status}`. The table asserts the corrected statuses below; chunks owning these claims must make their text agree: removability of Regime I frames and one active global G (C01, P); cocycle/Bianchi parallel to "boundary of a boundary" (C01, P identities, S parallel); observations break the diagonal left action, not U_i -> U_i g (C03, P); adaptive precision a declared penalty (C03, D); adiabatic hierarchy C (C03); stiffness/friction tensor, unit frequency under the kinetic postulate (C05); Karcher uniqueness for rotation angle < pi/2 (C06, P); licensing C and detector S (C06); shadow as one-episode-lagged predictive prior (C07, D), same-time form S; exact coarse-graining with no rescaling/flow/fixed point (C07, C14); declared root P and apex has the feedback structure of the self-excited circuit S (C07); clock-dissipation identity restricted to autonomous single-rate flow (C09, P); binary registration proposition (C09, D; the keep-and-drop paragraph and the W1 row point to it inside `sec:time_info`); meta-clock ratio D, contraction P, arc-length ratio C (C09); covariant Fisher block invariant (C09/C10, P via Supp. B Ch. B2); signature P under P4, pure gauge in Regime I, selection C (C09); consensus-metric obstruction restricted to frame-twist block, continuum and noncompact limits (C10); gravity S (C10); rock covariance reduced by 1/(1+beta) (C11 App. B, D); rho(L) < 2 (C12 App. D, P); Banach contraction only for isotropic couplings (C13, P).
- The abstract no longer mentions attention recovery, WikiText, the Lahav-Neemeh section, the meta-agent threshold, the signature constructions, or the consensus-metric regulator; conclusions (C08 `sec:conclusion`, C10 `sec:global_conclusion`) should not reintroduce them as contributions.
- Part titles: Part I is now "Part I: The Construction" (C00). C08 should retitle the Part II heading at 1808 to "Part II: The Speculative Program" (D2); C09 owns `sec:part2_preamble`, which the status paragraph cites as the register of P1-P10.
- Ontology: the enumerated O1-O4 are dissolved into one "Interpretive stance" paragraph (label `sec:cognitive_first`); no other chunk references O1-O4 by token. The single name is "cognitive-first structural monism"; C08 (1800), C10 (consciousness, 2101), and the Lahav section should use it in place of "information-geometric structuralism" and "pan-agentic structuralism". "Scale-0 agent" is now "agent at level zero".
- Section `sec:epistemic_status` is retitled "Claim Status and Scope"; the fence register F1-F6 no longer exists, so pointers "(fence F1)" to F6 elsewhere have no target text.
- The introduction states that the discrete detector section is `sec:meta_agent_threshold` and cites `sec:participatory` for the prospective protocol with a frozen-attention-prior control arm (C07 should add that arm per L19-5).
- The introduction and scope now say the gauge-curvature conjecture is not listed among falsifiable claims (it was language material removed under D7); C08/C10 should not cite `sec:scope_limitations` for it.
- `sec:companion_theory` claims the paper says "at the construction" where the companion supersedes the consensus functional, barycenter and detector, same-time shadows, and self-closing apex; C02, C06, C07 should carry those one-line pointers.
- The Kadanoff block-variable citations (kadanoff1966scaling, Kadanoff1975, KadanoffHoughtonYalabik1976) are now introduced at the organizing claim; C07 (1679-1702) and C14 may reuse them.

## Integration pass (2026-09-24)

Scope: C00 and C01 were integrated together by one editor, so table changes requested of C00 were applied directly. Private assembly and build of all fourteen current chunks (scratchpad copy of `assemble_and_check.py`, shared `check-report.md` not overwritten): latexmk exit 0, 0 errors, 0 undefined references, 0 undefined citations; the four overfull boxes lie in later chunks. C00 pattern scan: 0 banned words, 0 spacing macros, 0 "rather than", 0 `^{(s)}`, 0 transformer hits; the one "renormalization-group" occurrence is the intended Kadanoff sentence. CRLF restored.

### Notes applied

| Source | Note | Action |
| --- | --- | --- |
| C01 | Delete "zero-dimensional GL(K) gauge theory" row; add P row for Regime I removability; S row for boundary-of-a-boundary; abstract/intro must not call the construction a gauge theory on a point | Row was already absent; removability row now cites Theorem thm:glk_invariance and Proposition prop:regime1_removability; active-group row points to sec:gauge_covariance_principle; Bianchi row points to sec:boundary_of_boundary. Abstract and intro contain no gauge-theory-on-a-point claim. |
| C02 | F is "the consensus free-energy functional", a composite potential, not a bound; abstract must not call F a variational free energy | Abstract and intro para 3 now say "consensus free-energy functional"; intro para 2 adds one clause that the consensus functional has the energy-minus-entropy form but is a declared composite potential, not the single-agent bound. |
| C02 | L12-8 scope statement (agents receive, do not select, observations) relies on C00 | Confirmed present in the keep-and-drop paragraph; no change. |
| C03 | Symmetry row becomes "observations explicitly break the global belief-rotation symmetry" (D; invariances P); adaptive precision D; environmental-agent equivalence D (Gaussian) with kernel version from Theory Ch. 5; adiabatic hierarchy C | Symmetry row rewritten (invariance under change of reference and, without observations, under global belief rotation: P; explicit breaking by a fixed kernel: D; location sec:symmetry_breaking). Other three rows already agreed. |
| C05 | Replace stiffness row by "Hessian = stiffness, Fisher = friction tensor" (D, sec:stiffness_friction) and "kinetic-metric postulate M_K = M" (postulate; unit frequency) | Row split into two rows with those statuses and locations (sec:stiffness_friction, sec:velocity_quadratic). |
| C06 | Barycenter P, parent frame P, Karcher P under corrected radius, licensing C and degenerate under exact parents (Theory Ch. 9), detector S, contraction lemma D (sketch), meta-agents as belief-bearing agents S | Licensing row now names the exact-parent degeneracy, the belief-bearing reading (S), and points to sec:meta_agent_variational and sec:meta_agent_threshold; new row for lem:weight_contraction (D, sketch). Karcher row already states rotation angle below pi/2, matching C14's r_cx. |
| C07 | Apex = energy-level closure; top prior a declared root; lagged shadow D, same-time S; declared root P; sustained non-stationarity under observation drive C; meta-agent geometry smoothing P only with zero horizontal defect (Supp. B Ch. B2) | Abstract and intro para 3 now say the hierarchy "closes by an energy-level apex whose top-level prior is a declared root". New rows: non-stationarity (C sustained, P relaxation, test = prospective protocol) and meta-agent geometry domination (P conditional, deferred base-direction work). |
| C08 | Do not cite the deleted gauge-curvature conjecture; drop attention recovery, WikiText, working transformer, RG spine, toy spacetime; define W1-W5 in the intro; attribute the PPC to Ladyman and Ross; one status for C | Confirmed none of the dropped claims remain. Intro para 2 now reads "a presupposed smooth index manifold of contexts carrying no physical metric, called noumenal by analogy only". PPC attribution already correct. |
| C09 | Clock identity P (autonomous single-rate) with driven form eq:clock_driven; "time emerges" S with ordering presupposed; meta-clock D/P/C; binary registration D; pullback D with invariance via Supp. B Ch. B2; signature P under P4, "exhibited", property of a declared reference section | Clock row now cites Eq. eq:clock_driven; clock-as-time row states the ordering parameter is presupposed; signature row says "exhibited under P4 ... with no gauge-invariant content". Others already agreed. |
| C09 | Abstract/intro must drop "settling signature availability" and "commuting case is settled" | Confirmed absent; Scope now says the construction "exhibits ... but selects nothing". |
| C10 | sec:collective_geometry is the W3 home; drop "only candidate gauge-invariant observable"; regulator obstruction P restricted to frame-twist block; physical-correspondences table S; C1-C5 mathematical, C6 a derivation target; gravity S placeholder; intro "level-0" | Consensus row status changed from D to P (obstruction) with prop:regulator_obstruction; gravity row now also covers tab:physical_correspondences and says "placeholder"; open-problems row now says C1-C5 mathematical problems and C6 a derivation target. W3 row already points to sec:collective_geometry; "level zero" already used. |
| C11 | Methods has no scaling or WikiText; rock row: mean back-action suppressed (D), precision lowered by a factor tending to 1/(1+beta) (D), rock reading S | No Methods pointer remains in C00. Rock row now says "a factor tending to 1/(1+beta)" and adds S for the reading. |
| C12 | Theorem F P for the frozen-neighbor best response only; rho(L) < 2 P; Sigma_inf = Sigma_0 as population equilibrium S (doubled entropy weight) | App. F row now says "P (best response only)"; covariance row adds the S reading. |
| C13 | Same-time shadow S and not a message of the augmented joint; mean-field result P; Banach contraction isotropic only; nested bound P; 1PI/2PI C | Shadow row adds "not a message of the augmented joint"; new row for the nested bound (P) and the fluctuation program (C), located at sec:beyond_mean_field_gauge_vfe. |
| C14 | Mean-sector Schur lemma P; residual bound C; detector retention conditional P (A_I source unidentified; body detector not covered); one-loop entropy shift D; force residual only against the zero-temperature profile; covariance theorem P, extends to left-invariant metrics; Karcher radius | Four appendix rows added (covariance and Schur lemma P; one-loop shift and force residual D; schematic residual bound C; detector retention P conditional). |
| GENERAL (C06) | Drop "forward/reverse KL" | App. F row rewritten: "the relative entropy with the receiver law in the first slot", restricted to real-analytic f-divergences as in thm:representation_app. |
| GENERAL (C00) | tab:claim_status canonical | Unchanged. |

### Notes rejected or not applied in C00

- C12 "state the 1 + B_i entropy weight once at the functional's definition site": the definition site is in C02, not C00; C00 does not restate it. Recorded for C02.
- C14 "move the notation table to the front": not applied; the intro's pointer to Appendix sec:notation is adequate and moving it would cross chunk boundaries.
- C13 "the T_cfg -> 0 limit is data-blind": a caveat, not a load-bearing claim; not given a table row.
- C00's related-work sentence on connection and sheaf Laplacians duplicates C02's first subsection; C00 keeps it (related work is the canonical home) and C02 may cut its copy.

### Other edits (tightening)

- Intro para 3: the three-strand paragraph no longer repeats the abstract's wording sentence by sentence (about 60 words shorter).
- Scope para 1: deleted the restatement of intro para 1's novelty sentence and the caveats already carried by table rows (signature section-dependence, continuum and Haar obstructions); kept one sentence on the covariant Fisher block.
- Scope para 2: "The historical simulation records ... are unavailable" (lab-notebook phrasing) replaced by one clause; the sentence duplicating the E-code definition removed.
- Scope para 3: quantum-extension sentence compressed; "Critical open problems" changed to "The open problems".
- Companion paragraph: machine-learning pointer shortened, "transformer" wording dropped (C02 carries the D7 remark).
- Related work: final summary sentence (restated the intro) deleted.
- Table row wording: "The softmax attention row" changed to "The attention row, a softmax over transported divergences" (removes a pattern-check false positive).

Word count: 4,949 before the pass, 5,138 after. Prose removed about 150 words; the nine new table rows and row extensions requested by other chunks added about 340.

### Cross-chunk notes from this pass

- C02 (line 90): calls the simultaneous right translation U_i -> U_i g(c) a "passive re-expression"; C01, C03, and the Theory call it a change of reference, and passive re-expression is U_i -> g_i U_i. C02 should say "change of reference".
- C05 (line 3): says the flow descends "the variational free energy F"; per C02's naming rule it should be "the consensus free-energy functional".
- C08: the Part II heading reads "Speculative Extensions and Outlook"; D2 and the C00 status paragraph call Part II "the speculative program". Retitle optional.

## Consistency fixes

| # | Issue (reader quote) | Disposition | Description |
|---|---|---|---|
| 1 | "the hierarchy closes by an energy-level apex whose top-level prior is a declared root" (abstract, intro) | applied | Confirmed against C07 line 71 (the pooled prior reads current beliefs and is not a factor of one joint). Both places now read "the hierarchy is closed by a declared root, a fixed top-level prior acting as its boundary condition, together with an energy-level apex for the belief channel that pools current beliefs and is not a generative factor". The reader's word "optional" was not adopted because C07 does not call the apex optional. |
| 2 | "Participation across scales, the fourth part of the correspondence" (W-label mismatch) | applied | Intro now models "four parts ... labeled W1--W4": observer-relative description underlies all four and makes W2 observer-dependent; derived duration and geometry are W1 and W2; one world is W3; participation is W4. The abstract was reorganized into the same four parts in W1--W4 order, with observer-relative description stated as the common basis. |
| 3 | kinetic-metric row status "postulate" | applied | Row status is now "S (declared postulate, not among P1--P10)". Section 2 gained one sentence: Part I declares one further postulate outside the register, the kinetic metric, used by no other result, whose inertial reading has status S. C05 line 216 already says "has status S", so C05 is consistent and needs no change. |
| 4 | "Part II ... its claims carry status S or C" | applied | Merged with issue 10: physical readings carry S or C and rest on the postulates; the mathematical results used (clock--dissipation identity, registration proposition, pullback and invariance, signature constructions) carry P or D. |
| 5 | Ladyman1998 pointer to sec:gauge_invariance_consensus | applied (merged with 16) | Pointer changed to Section~\ref{sec:discussion}, which contains the "Kantian and Structural-Realist Positioning" subsection (C08 line 23). A dedicated label cannot be added from C00; see cross-chunk note. |
| 6 | "tested only by the prospective protocol" | applied | E definition now reads "its multi-scale claims are tested by the companion's pairing-selection conjecture and by the prospective protocol of Section~\ref{sec:participatory}, its finite-sample counterpart". |
| 7 | W3 status "D (consensus geometry)" | applied (merged with 13) | W3 status is now "P (rows, regulator obstruction), S (reading as one world), C (regulated metric)", matching the claim-table row and C08. |
| 8 | scaled dot-product sentence in companion paragraph | applied | Sentence deleted; D7 places the single remark in C02. |
| 9 | duplicate of issue 1 | applied | See issue 1. |
| 10 | duplicate of issue 4 | applied | See issue 4. |
| 11 | W1 "at most one bit per registration" | applied | Now "whose expected information gain is at most one bit per registration". |
| 12 | "the continuous variational criterion it approximates" | applied | Now "the continuous variational criterion, from which the detector is not derived,". |
| 13 | duplicate of issue 7 | applied | See issue 7. |
| 14 | non-stationarity row, "what would change it" cell | applied | Cell now "a proof that observation injection sustains non-stationarity, or a counterexample"; the C07 protocol has no non-stationarity arm. |
| 15 | abstract pullback scope | applied | Abstract adds "a step that uses base derivatives and so goes beyond the single-point construction (it is treated in the companion base-transport supplement)"; the intro's W2 sentence adds the matching clause with a pointer to Section~\ref{sec:it_from_bit}. |
| 16 | duplicate of issue 5 | applied | See issue 5. |
| 17 | self-excited circuit row | applied | Row now reads "... self-excited circuit, without its self-excitation (W5)". |

Counts: 17 reader items (12 distinct issues, 5 duplicates); 17 applied (one with a minor wording adaptation), 0 skipped.

Labels removed: none. Labels added: none.

### Cross-chunk notes from the consistency pass

- C08: optionally add `\label{sec:kant_structural}` to the "Kantian and Structural-Realist Positioning" subsection (line 23); C00's Ladyman1998 pointer could then target it instead of `sec:discussion`.
- C02: `DennisGLKAttention2026` is no longer cited in C00; the single scaled-dot-product remark required by D7 must carry the citation.
