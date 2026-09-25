# L17: Editor and program-architect review of PIFB2.tex (venue, standalone test, thesis, length)

**Lens:** L17, senior editor at a foundations-of-physics journal and program architect. Architecture-level review: abstract, introduction, section openings and closings, the fence register, the Part I and Part II split, the conclusions, and the statements.

**Author model:** Claude Opus 5.5. Investigator output only; no adjudication or verifier pass was run.

**Target:** `PIFB2.tex`, SHA-256 `f80e6dabd9e5485649066e227e80beff1dd2b1082cf786bcdaeedb8cbd080ec4` (verified with `sha256sum`), 3956 lines, 79,455 words (`wc -w`).

**Lines read verbatim (long lines unfolded with `sed | fold`):** 1-143; 431-436; 516-529; 678; 735-738; 929-934; 1006-1013; 1304-1330; 1533-1536; 1570-1580; 1657-1827; 1828-1893; 1896; 2017; 2109; 2133-2211; 3939-3956. Single lines read for dependency evidence: 206-210, 416-418, 441, 447, 1476, 1613. The remainder of the file was covered only by the whole-file scripts below (section structure, word counts, vocabulary and phrase distributions); I did not read the body of the bundle section (144-430), the free-energy derivations (530-734), precision and environment (739-928), the transformer derivation (1014-1303), the mass section (1331-1532), most of Part II (1897-2132), or the appendices (2212-3938) as prose.

**Executed (all in `reviews/2026-09-24-pifb2/scripts/`):**
- `L17_wordcount.py`: raw and prose word counts by part, section, and subsection; block aggregates on the brief's line map; environment counts.
- `L17_architecture.py`: abstract word count; thesis vocabulary (Wheeler, it from bit, participat*) versus machine-learning vocabulary versus implementation vocabulary by block; repeated-disclaimer phrase counts with line numbers; hedge density.
- `L17_sentences.py`: sentence-length statistics by block with math stripped.
- `L17_line1575_checks.py`: float64 checks of the two "findings recorded in 2026" at line 1575.
- Web: current author guidelines or scope pages for Foundations of Physics, Entropy, Journal of Physics: Complexity, Physical Review Research, Journal of Physics A, and Studies in History and Philosophy of Science (details and verification level under L17-2).

**Headline numbers.** Part I body (136-1807) is 43,000 raw words, Part II (1808-2159) is 10,341, appendices and notation are 24,287. The "It From Bit: The Pullback Construction" section (1867-1893) is 715 words, 0.9 percent of the manuscript. The abstract is 530 words and never mentions Wheeler or "it from bit". Between line 128 and line 1676 (33,692 words) the name Wheeler does not occur. Across the whole file, thesis vocabulary scores 79 hits against 548 for machine-learning vocabulary and 257 for implementation vocabulary.

## Findings

### L17-1: The Wheeler realization is not the organizing thesis; the manuscript's own abstract, introduction, and conclusion name other theses

**Location:** PIFB2.tex:58-64 (abstract), 81 ("The organizing claim of the paper is ..."), 1804-1806 (`sec:conclusion`), 1810-1812 (`sec:part2_preamble`), 1867-1893 (`sec:it_from_bit`), 2152-2159 (`sec:global_conclusion`).

**Severity:** critical. The author's first goal is a standalone realization of Wheeler's participatory "it from bit". As built, the manuscript does not argue that thesis. It places the thesis in a part it labels speculative and asks the reader to treat that part "as Outlook rather than as Results" (1812).

**Evidence.** Script output (`L17_architecture.py`):
- The abstract has 530 words. Wheeler occurs 0 times, "it from bit" 0 times, "participat*" once, transformer or attention 5 times, WikiText once. Keywords (66): gauge theory, active inference, free energy principle, information geometry, emergent spacetime, transformer architectures. Neither "participatory" nor "it from bit" appears.
- Line 81 states the paper's organizing claim in these words: "this single-scale construction is one rung of a renormalization-group spine". The three "central contributions" listed there are the multi-agent functional, the attention recovery, and the WikiText sweep. Wheeler enters the same paragraph only as a slogan the framework supplies objects for. The paragraph then says "It derives neither Wheeler's physics nor Kant's idealism" and calls the physical reading "the Level-3 speculative payoff of Part II".
- The Part I conclusion at 1806 reads: "The framework's most concrete contribution is this recovery", meaning the attention recovery, together with the WikiText transformer.
- Wheeler occurs on 16 source lines: 75, 81, 83, 92, 102, 120, 1677, 1705, 1727, 1767, 1806, 1812, 1830, 1835, 1872, 1882. No mention falls in 136-1676. "It from bit" occurs on 7 lines: 45 (title), 75, 81, 1830, 1867, 1872, 1892.
- Word budget by block: bundle kinematics 9,647; transformer recovery 5,535; mass 4,164; coarse-graining I-IV 7,926; RG appendix 6,884. The it-from-bit pullback section has 715.
- The global conclusion (2152-2159) never names Wheeler.

In substance the "it" of it-from-bit is `eq:induced_metric_full` at 1873-1876, the ordinary pullback of the Gaussian Fisher-Rao metric along a section, plus an optional trace block. That construction occupies one boxed equation and one Gaussian example. The "participatory" half is the cross-scale shadow and apex loop at 1662-1731, which the paper itself classifies as a prospective, unvalidated program (fence F2).

**Fix.** Re-found the paper on Wheeler's own questions. Wheeler 1990 asks "How come existence?", "How come the quantum?", and "How come 'one world' out of many observer-participants?", and posits the self-excited circuit. A physics paper realizing the program should state early what a formal participatory model must supply. It should then deliver each item with its status, in order:
- (W1) registered bits as the unit of change: the information clock, 1828-1866.
- (W2) observer-dependence of the "it": the pullback geometry, 1867-1893.
- (W3) one world out of many observer-participants: consensus, the collective free energy, the consensus metric and its regulator obstruction, 2015-2043.
- (W4) participation back onto the participants: cross-scale shadows and the apex loop, 1662-1731.
- (W5) what is not delivered: the quantum, signature selection, units.

The wiki note on Wheeler 1990 records that an earlier version of this manuscript carried a Wheeler-versus-framework correspondence table. Restore such a table in the introduction, with a status column (P, D, S, C) per row, and make it the paper's table of contents in prose. The abstract's first sentence should state the Wheeler question and the answer offered. Transformer material drops to one sentence (see L17-4).

Rewrite line 81 so that the organizing claim is the Wheeler correspondence and the RG spine becomes one mechanism under W4. A suggested opening: "We construct a multi-agent variational model in which Wheeler's participatory 'it from bit' acquires four precise ingredients: an agent-relative clock counted in bits, an agent-relative geometry obtained by pullback of Fisher information, consensus as the stationary point of a collective free energy, and a feedback loop through which collectives become the priors of their members. The model does not derive quantum theory, Lorentzian signature, or physical units; we state exactly which ingredients are theorems, which are postulates, and which remain conjectures."

On the realization voice, see L13-1 and L13-2. "Formal model of" is the defensible verb, not "realization of". This finding is architectural and does not repeat those.

**Falsifies:** A reading in which the abstract, the stated organizing claim at 81, and the conclusions at 1806 and 2154 name Wheeler's participatory it-from-bit as the thesis, with the RG, attention, and scaling material presented as means to it. That is not what the text says.

**Status:** The Wheeler correspondence is S (structural analogy) with some D ingredients: the clock identity and the pullback tensor are D; the participatory loop is C/prospective. The prose at 1872 ("given a precise fixed-gauge realization") and 1727 ("This realizes the formal feedback structure of Wheeler's self-excited circuit") inflates S to realization.

### L17-2: At 79,455 words and a 530-word abstract, the manuscript is outside every candidate physics venue's norms; recommended primary venue is Foundations of Physics, backup Entropy

**Location:** Whole manuscript; abstract 58-64.

**Severity:** high. This is not a correctness defect. It is a certain desk rejection at every physics venue considered.

**Evidence.** From `L17_wordcount.py`: total 79,455 raw words, of which the main text through the statements (1-2211) is about 55,200 and the appendices are 24,287. The document has 295 equation environments, 12 theorems, 10 propositions, 8 postulates, and 2 figures. Venue norms found on 2026-09-24:

| Venue | Scope fit for the Wheeler thesis | Length and abstract norms found | Verification level |
| --- | --- | --- | --- |
| Foundations of Physics (Springer) | Best fit. Aims and scope: "conceptual bases and fundamental theories of modern physics"; lists information theory and statistical mechanics; forum for "scientists, mathematicians and philosophers" | Abstract 150-250 words; no hard article length limit found | Aims page via search index; abstract rule via search snippet of the submission-guidelines page (the page itself redirected to a login and could not be fetched) |
| Entropy (MDPI) | Good fit for information geometry, free energy, and information-theoretic foundations; physics referees rate it below FoP | Abstract about 200 words maximum, single paragraph; no maximum length found | Search snippet of the instructions page (direct fetch returned HTTP 403); APC not verified |
| Journal of Physics: Complexity (IOP) | Fits the multi-agent network, formation, and ML material, not the foundations thesis | Research papers of unlimited length; letters about 4,500 words; APC £1985 / €2355 / $2730 | Fetched from the IOP publishing-support page |
| Physical Review Research (APS) | Poor fit for Level-3 material. The editorial bar requires significance with a connection to physics; the manuscript declares no quantitative physics predictions (125) | No length limit for regular articles; abstract under 500 words (APS guidance) | Search snippets only; APS pages returned HTTP 403 |
| Journal of Physics A (IOP) | Mathematical physics, theorem-proof; interpretive thesis out of scope | Abstract normally at most 300 words; longer abstracts may be returned | Fetched from IOP publishing support |
| Studies in History and Philosophy of Science (Elsevier) | Philosophy venue; fits the ontology O1-O4, Kant, and consciousness material, not the mathematics | At most 12,000 words including abstract, notes, references; double-anonymized review | Search snippet of the guide for authors |

Two further facts bear on the choice. `references.bib` entry `Dennis2025it` (1821-1826) records an earlier version of this paper, with the same title, as "Submitted to Foundations of Physics". I do not know that submission's outcome. A resubmission of a substantially overlapping manuscript to the same journal must be disclosed to the editor as such, and a prior rejection changes the calculus. Second, in my editorial experience, not from a stated rule, FoP research articles are typically 8,000-15,000 words. A 55,000-word main text would be returned before review even without a formal cap.

**Fix.** Primary venue: Foundations of Physics, as a paper of about 13,000 words of main text plus about 3,500 words of appendices (about 16,500 raw words, about 21 percent of the current length), with an abstract of 200-230 words. Entropy is the backup; it tolerates a somewhat longer version (up to about 20,000) and the same abstract discipline. Physical Review Research and Journal of Physics A are not recommended for the Wheeler paper. Either could take a later narrow mathematical result, but the Theory manuscript is the natural home for that. Journal of Physics: Complexity suits a separate formation or network paper, not this one. Studies in History and Philosophy of Science suits a separate philosophy paper carrying O1-O4, the Kantian positioning, and the consciousness section, if the author wants those published. The concrete outline is under L17-4. Before choosing FoP, the author should check the status of the `Dennis2025it` submission.

**Falsifies:** A current FoP or Entropy statement allowing 50,000-word research articles or 500-word abstracts. I could not fetch the full FoP guideline page.

**Status:** Not a claim-status item.

### L17-3: The standalone test fails on four dependencies on unpublished material; two are fatal as written

**Location:** 59 (abstract), 100 (Level-2 definition), 436-455 (`table*`, executable contract), 678 (`Status of the functional`), 1575, 1613, 1692, 1705, 1712, 2138, 2148, 2165-2203 (Methods and statements), 2768.

**Severity:** high overall. Two items are fatal for a standalone paper.

**Evidence and classification.**
1. **Uncited companion result used to bound claims (fatal).** At 678, the text says the ELBO status of the functional "is a separate question taken up in the companion exact-ELBO treatment". It then states: "That treatment has since settled the attention row". It reports that result's content, namely exactness only at link covariance tied to the transported sender covariance and τ = 1, and uses it to conclude that "The row at the operating temperature ... is therefore not the exact coordinate of any model in that family." No citation, no bibkey, and no proof are given. A referee cannot check a limitation the paper imports from an invisible document. This is almost certainly the Theory manuscript (`Theory/c05_evidence_bound.tex`, `thm:obs-collective-vfe`; `c06_attention.tex`, `sec:local-attention-elbo`), which PIFB2 never cites. `grep` finds 0 hits for "Theory manuscript" and no bibkey for it. L04-2 raises the missing citation from the variational side. The architectural point here is that the claim-bounding role makes the gap fatal, not cosmetic.
2. **Status defined by code behavior (fatal in the abstract, non-fatal elsewhere).** The abstract's third sentence group reads: "The checked-in multi-agent implementation differentiates this scalar total, so its active update is potential descent rather than a nonintegrable softmax-response field" (59). Level 2 is defined as "constructed and computationally implemented" (100). The paper carries 24 "checked-in", 29 "reference implementation", and 39 `\texttt` items. There are code paths in the body (1476 `gauge_agent/mass.py`; 1613 `MAgent_Model/gauge_agent/meta_agents.py::ConsensusDetector`; 1692; 1712) and configuration names (1705: `max_scales=25` versus `max_scales=5`). There is a full "Executable contract" table (436-455) stating which flags are "Active" in "the checked-in `CONFIG` after loader normalization". A physics reader cannot see the code and has no reason to care which loader normalization is active. Statements about what the code does are not physics claims and cannot be refereed. In the abstract, such a statement displaces the thesis.
3. **Companion note in preparation carrying results.** `Dennis2026metaentropy` ("Companion manuscript, in preparation") supplies an analytic result, "the consensus susceptibility is χ = 1/α and diverges only in the decoupling limit" (2148). It also supplies an open-problem framing (2768) and a "conjectured residual meta-entropy" test anchor (2138). Not fatal, because the claims are peripheral, but a standalone paper must either prove χ = 1/α in an appendix or drop it. The ML companion (`Dennis2025trans`, JMLR, in preparation) is in the bibliography but never cited, although the transformer recovery is its subject (L08-9).
4. **The 2026 findings near 1575.** "Two findings recorded in 2026 sharpen the status of this subsection". These are parent-frame non-identifiability and the non-existence of a left-equivariant permutation-symmetric map GL⁺(K)ⁿ → GL⁺(K). Both are proved inline, and I checked both numerically (Verified, below), so they do not depend on outside material. They are presented in lab-notebook voice, though, and they contradict the preceding and following sentences (see L17-7). Not fatal; they need integration.
5. **Simulation runs.** The historical emergence runs are unavailable (108, 122, 1734, 2200). The paper handles this honestly with fences F2 and F6 and a prospective protocol (1732-1750, 2162-2174). For a theory paper, this is not fatal provided no claim leans on the runs. The global conclusion at 2154 still says "The tower machinery is implemented", which is a code claim, not physics.
6. **Data and code availability.** The data statement (2200) names `Manuscripts-Theory/data/...` paths. L09-1 reports that these files do not exist in any available artifact. The code statement (2203) points to a public `MAgent_Model` repository and an unlinked `V3_Transformer`/`vfe3` repository. Registered (L09-1); not re-raised.

**Fix.** For item 1, cite the Theory manuscript, which must first be posted (arXiv) so that it is citable. Name the theorem, for example "[Theory, Thm. `thm:obs-collective-vfe`, §`sec:local-attention-elbo`]". Alternatively, state and prove the tie condition in a short appendix. For item 2, delete the implementation sentence from the abstract. Replace the Level-2 definition with a claim-status column (L17-5). Move the executable-contract table, all code paths, configuration names, and CUDA and seed statements to a repository README or supplementary file, and keep one sentence in the main text: "A reference implementation is available at [URL]; it is not needed to follow any argument in this paper." For item 3, prove or drop χ = 1/α, and cite the ML companion once, at the attention remark. For item 4, see L17-7. Replacing sections by citations to the Theory manuscript (L17-4) creates a new dependency. It is acceptable only if the Theory manuscript is publicly posted before PIFB2 is submitted, and each citation must name a specific result.

**Falsifies:** A bibkey or explicit citation for the "companion exact-ELBO treatment" that I missed. `grep -n 'exact-ELBO'` finds only line 678.

**Status:** Item 1 imports an unproved-here restriction (status P elsewhere, per the ledger's framing, but unavailable to this paper's reader). Item 2 statements are E about software, not physics claims.

### L17-4: A concrete restructure into a physics-journal paper of about 16,500 words

**Location:** Whole manuscript.

**Severity:** high. This is the required remedy for L17-1 and L17-2.

**Evidence.** Word counts are from `L17_wordcount.py`, in raw LaTeX words; prose words run 85-90 percent of raw. The disposition vocabulary is: keep, condense, move to supplement (online supplementary material of the same paper), replace by citation to the Theory manuscript (posted first; see L17-3), move to the ML companion (`GL(K)_attention_v2.tex`, "Gauge-Covariant Gaussian Attention through Projected Matrix Links", 18,364 words, which already carries WikiText material), or cut.

**Current section, words, disposition:**

| Current section (lines) | Words | Disposition |
| --- | --- | --- |
| Abstract (58-64) | 530 | Rewrite around Wheeler; 200-230 |
| Introduction incl. O1-O4 (73-93) | 1,200 | Rewrite (new §1); O1-O4 compressed to one paragraph, full ontology to a philosophy companion (L13-4) |
| Epistemic status, F1-F6, scope (94-127) | 1,367 | Replace by one claim-status table and one paragraph (new §2) |
| Related work (128-135) | 740 | Condense and rebalance toward physics (informational reconstructions, Fuchs, Caticha, Wootters; see L14-3, L15-1); fold into §1 and §8 |
| One rung: bundles, transport, Regime I/II, Wilson, four curvatures, working simplifications (136-515) | 9,647 | Condense to about 1,800 (new §3); Wilson/lattice and Regime II detail to Theory Supplement B citation or cut; executable table to repository |
| Single-scale free energy (516-734) | 4,010 | Condense to about 1,500 (new §4); masking, ALiBi, relative position to ML companion; ELBO status replaced by Theory citation |
| Precision, envelope, environmental agents, symmetry breaking (735-928) | 3,103 | Keep environmental agents as "registered bits" (about 500, in §4); state-dependent precision and envelope to supplement |
| Timescales, natural gradient (929-1005) | 1,844 | Condense to about 500 (in §5) |
| Transformer recovery (1006-1303) | 5,535 | Move to ML companion; one 150-word remark in §4 citing it |
| WikiText sweep (1304-1324) | 324 | Move to ML companion |
| Precision as stiffness, mass (1325-1532) | 4,164 | Move to supplement or cut; one sentence in §8 (F4, L02-3, L11-7) |
| Coarse-graining I (1533-1661) | 4,546 | Condense to about 1,300 (§6): barycenter, the two 1575 propositions, licensing criterion; detector to supplement |
| Coarse-graining II, shadows (1662-1678) | 691 | Keep, about 500 (§6, the participatory loop) |
| Coarse-graining III, RG status (1679-1702) | 1,153 | Condense to about 250 and cite Theory `c11_network_coarsegraining.tex` (`ch:agent-network-rg`); rename per L06-1 |
| Coarse-graining IV, Ouroboros and apex (1703-1731) | 1,536 | Condense to about 500 (§6); cut NE score (L06-9) and code fields; state the apex status against Theory `c12_multiscale_vfe.tex` `sec:full-graph-closing-tower` |
| Prospective validation (1732-1750) | 518 | Move to supplement or repository; one sentence |
| Discussion (1751-1801) | 2,485 | Keep "participatory approaches" (expand, about 600); kinetic-term and transformer implications cut; language and cognition plus gauge-curvature conjecture to ML companion; Kant about 200 |
| Conclusion to Part I (1802-1807) | 372 | Merge into one conclusion |
| Part II preamble and P1-P10 (1810-1827) | 612 | Dissolve into the claim-status table |
| Time as information flow (1828-1866) | 923 | Keep, about 800 (§5), with the ledger fix at 1861 |
| It from bit pullback (1867-1893) | 715 | Expand to about 1,300 (§7, the centerpiece) |
| Lorentzian signature (1894-2014) | 2,392 | Condense to about 700 (§7): one worked example stated as postulated input (L13-8, L11-4); GL(2,C) and causal routes to supplement |
| Collective geometry, sectors, physical quantities (2015-2069) | 1,752 | Condense to about 800 (§8: one world out of many; regulator obstruction; keep the short correspondence table) |
| Gravity, macroscopic objects, measurement (2070-2085) | 623 | Condense to about 200 or cut (L11-8, L11-9) |
| Consciousness (2086-2106) | 1,029 | Cut; philosophy companion |
| Gauge invariance as consensus, philosophy of science (2107-2132) | 971 | Condense to about 250 in §9 |
| Open problems C1-C6 (2133-2151) | 1,102 | Condense to about 450 in §9 |
| Conclusion (2152-2159) | 222 | Rewrite, about 300 |
| Methods and statements (2160-2211) | 898 | Statements about 250; methods to repository |
| App. A gradients (2212-2515) | 3,923 | Move to ML companion or code documentation |
| App. B rock example (2516-2591) | 1,271 | Cut (L11-5 reports its back-action claim false) |
| App. C mathematical details (2592-2661) | 847 | Keep Gaussian KL and Fisher, about 600 |
| App. D covariance dynamics (2662-2891) | 1,838 | Supplement |
| App. E quadratic forms (2892-2955) | 726 | Condense to about 300 in appendix |
| App. F representation theorem (2956-3161) | 2,686 | Supplement (its scope issue is L03-1) |
| App. G augmented joint (3162-3412) | 3,282 | Replace by Theory citation (`c04_generative.tex` `sec:gen-typing`; `c12_multiscale_vfe.tex` `sec:full-graph-vfe-downward`); keep a 300-word statement of the rigid-link lemma |
| App. H beyond mean field (3413-3568) | 2,185 | Replace by Theory citation (`c12_multiscale_vfe.tex` `sec:full-graph-vfe-global`) |
| App. I RG construction and theorems (3569-3941) | 6,884 | Replace by Theory citation (`c09_coarse_channels.tex`, `c11_network_coarsegraining.tex`); keep the covariance theorem statement, about 500 |
| Notation (3942-3953) | 645 | About 400 |

**Proposed outline** (title suggestion: "A Participatory It-from-Bit Model: Agents as Sections, Consensus, and Induced Geometry"):

| New section | Content | Target words |
| --- | --- | --- |
| Abstract | Wheeler question, the four ingredients, what is proved, postulated, and open | 220 |
| 1. Introduction | Wheeler's questions and self-excited circuit; requirements W1-W5 with a correspondence table and status column; relation to informational reconstructions, QBism, RQM, participatory realism; ontology in one paragraph | 1,300 |
| 2. Status conventions | One claim-status table (P/D/S/C/postulate) replacing Levels 1-3, F1-F6, and P1-P10 | 400 |
| 3. Agents as sections at a point | Principal bundle, associated belief and model bundles, frames, transport, KL invariance; Regime I in one paragraph, Regime II as one sentence with a pointer | 1,800 |
| 4. Registered bits and consensus: the collective free energy | Consensus functional as a declared ansatz; softmax rows and −τ log Z; environmental agents as observations (the bit input); state-level ELBO no-go; one-paragraph attention remark with ML-companion citation; exact-ELBO status by Theory citation | 2,000 |
| 5. An agent-relative clock | Natural-gradient flow and imposed timescales; Fisher arc length; clock-dissipation identity; bits per update; meta-clock ratio (with the registered RMS correction) | 1,300 |
| 6. Participation across scales | Meta-agent barycenter; parent-frame non-identifiability and the equivariance no-go as propositions; shadow priors as the top-down leg; licensing criterion; coarse-graining status by Theory citation; the apex loop and its status | 2,200 |
| 7. It from bit: induced geometry | Pullback tensor, three tiers, observer-dependence; signature as postulated input with one worked example | 2,000 |
| 8. One world out of many: consensus geometry | Why averaging fails the gauge test; regulator obstruction; within-species agreement; the short physical-quantities table | 900 |
| 9. Discussion and open problems | What is not claimed (quantum, units, predictions); falsifiability stated once; C1-C6 compressed | 1,000 |
| 10. Conclusion | | 300 |
| Appendix A | Gaussian KL, Fisher, pullback formulas | 800 |
| Appendix B | Proofs: KL invariance, 1575 propositions, clock identity, covariance theorem statement | 2,300 |
| Appendix C | Notation | 400 |
| **Total** | | **about 16,900** (main text about 13,400) |

The online supplement is capped at about 10,000 words. It takes the detector, state-dependent precision, covariance dynamics, the representation theorem, the GL(2,C) and causal signature routes, the mass and kinetic-metric postulate, and the prospective protocol.

**Fix:** Adopt the outline, or one that satisfies the same constraints: Wheeler first, one status table, no code in the main text, the ML material in the ML paper, and the Theory cited for everything it develops further. This is Option C of the 2026-09-23 program-alignment review (C1-pifb2-program-alignment.md, section (e)), seen from the PIFB2 side. The choice among options A-C remains the author's; the word targets above work under options A and C.

**Falsifies:** A demonstration that the removed material is needed for a W1-W5 argument. For example, if the transformer recovery were the only evidence that the consensus functional is physically meaningful. The manuscript itself says the language-model experiments "test the architecture and not the participatory reading" (102), so the recovery carries no weight for the thesis.

**Status:** Not a claim-status item.

### L17-5: The fence register creates the repetition it was designed to prevent

**Location:** 96 (the register's contract), 104-116 (F1-F6), 1810-1827 (P1-P10); restatements listed below.

**Severity:** medium.

**Evidence.** Line 96 promises: "Each caveat has a single home section ... every other site gives at most one clause plus a pointer". `L17_architecture.py` counts:
- The F1 content (recover, limit, not a derivation) appears on 15 lines: 61, 81, 98, 106, 512, 522, 1008, 1034, 1132, 1262, 1615, 1804, 2079, 2197, 2954. "Recovery in a limit" appears 6 times and "separately introduced" (the bilinear M) 6 times. Several restatements run to full sentences, for example 61, 98, and 1804.
- "fence F1-F5" pointers appear 26 times. F6 has no pointer.
- "Regulator" (the F3 theme) is on 17 lines.
- "Prospective" (F2) is on 26 lines.
- The schedule and iso-token caveat for the sweep is stated at 124 (in Scope), 1306, and 2178.
- The Level taxonomy, the F register, and the P1-P10 register are three overlapping status systems.
- "Rather than" occurs 256 times. The hedge density (`rather than|not a derivation|is not|does not|...` per 1,000 words) is highest where a physicist reads first: 13.5 in Related work, 12.4 in Epistemic status, 10.7 in the abstract. The body runs 3.3-5.8.

To a physics referee, such density reads as defensive. It also makes the positive claims hard to find.

**Fix.** Replace Levels 1-3, F1-F6, and P1-P10 by one table in §2 with columns "claim, where, status (P/D/S/C/postulate), what would falsify it". Each caveat then appears once, in its row. In the body, a claim carries its status letter in parentheses at first statement and nothing thereafter. Delete every pointer of the form "(fence Fn; Section ...)".

**Falsifies:** A count showing the restatements are pointer-length (one clause). Lines 61, 98, 1008, 1262, and 1804 each restate F1 in one or more full sentences.

**Status:** Not a claim-status item; see L13-9 on the taxonomy's logic.

### L17-6: The Part I and Part II split sorts by subject, not by epistemic grade, contrary to its own statement

**Location:** 71 ("Part I: Defensible Core"), 83-92 (O1-O4), 1773-1800, 1808, 1812, 2156.

**Severity:** medium.

**Evidence.** The global conclusion states: "What separates the two parts is epistemic grade rather than subject matter" (2156). Yet Part I, the "Defensible Core", contains the following:
- the Level-3 ontology O1-O4 (83-92; "This paragraph states the Level-3 ontological framing");
- the panprotopsychist placement (92);
- the language-and-cognition section (1773-1797) with conjectures on garden-path sentences, creolization, and "Einstein's summation convention and Dirac's bra-ket notation" as curvature-reducing conventions;
- the Kantian metaphysical postulate (1800, "a metaphysical postulate, not a derived result");
- the meta-agents-as-agents reading, which line 102 itself calls Level-3.

Meanwhile, Part II's preamble declares its mathematics Level-2 (1812): the pullback decomposition, the worked signature constructions, the clock identity, and the regulator obstruction. So the split puts the paper's Wheeler-relevant theorems under a speculative banner and puts speculation in the core.

**Fix.** Drop the two-part architecture. Organize by Wheeler requirement (L17-4) and carry the grade in the status table (L17-5). If the author keeps two parts, sort strictly by grade: move O1-O4, language and cognition, and Kant to Part II, and move the clock identity, pullback tensor, and regulator obstruction to Part I.

**Falsifies:** A reading of 83-92 and 1773-1800 as Level-1 or Level-2 content. The text labels them otherwise.

**Status:** Not a claim-status item; overlaps L13-9, which treats the taxonomy's logic. This finding adds the architectural consequence for the thesis.

### L17-7: Lab-notebook insertions at 678, 1575, and 1685 contradict the text around them

**Location:** 1570-1578 (`eq:meta_agent_frame_barycenter` and following), 678, 1685.

**Severity:** medium.

**Evidence.**
- At 1573 the Lie-algebra-additive frame is "accurate to O(‖φ_i‖²) when constituent frames are close". At 1575 the text says: "the O(‖φ_i‖²) accuracy claim above names the wrong controlling parameter". At 1577 it says the barycenter and Karcher frame "are the correct coarse-graining target" by `thm:rg_covariance`. Line 1575 has just shown that the parent frame is pure gauge and "any convention fixing U_I is a gauge choice to be declared rather than defended". The three paragraphs therefore state, retract, and re-assert.
- Line 678 has the same pattern ("That treatment has since settled ...").
- Line 1685 opens "That open question now has a partial answer".

Dated discovery narratives ("recorded in 2026", "has since settled", "now has") are appropriate in a research log, not in a journal article, where the reader expects the current state.

I checked both 1575 results in float64 (`L17_line1575_checks.py`). Non-identifiability holds: moving U_I along its orbit at fixed (m, S) changes the constituent shadow by at most 3.3e-16 (mean) and 5.3e-15 (covariance). The equivariance witness also holds: for (K, n) in {(2,2), (2,3), (3,2), (4,5)}, left multiplication by v cyclically permutes (I, v, ..., v^{n−1}), and dim ker(v − I) = K − 2 < K, so (v − I)M = 0 forces rank M ≤ K − 2. The mathematics is sound. The problem is presentation.

**Fix.** State the two 1575 results as a proposition with proof (Appendix B of the new outline). Delete the O(‖φ_i‖²) sentence and the "correct coarse-graining target" sentence, or restate the latter as "equivariant after a declared frame convention". Rewrite 678 and 1685 in timeless voice with a citation.

**Falsifies:** A reading on which the 1573 accuracy claim and the 1575 retraction concern different quantities. Line 1575 names the same claim ("the O(‖φ_i‖²) accuracy claim above").

**Status:** Both 1575 results are P (proved inline; numerically confirmed). The surrounding 1573 and 1577 sentences are superseded by them.

### L17-8: Software-assurance content occupies physics-paper space

**Location:** 436-455 (executable contract table), 1732-1750 (`sec:participatory`), 2160-2186 (`sec:methods`), 1705, 2185.

**Severity:** medium.

**Evidence.** The prospective protocol requires "the repository commit and source-diff hash, a dependency and CUDA manifest, the exact plot generator, and a file-hash manifest" (1744). It also requires "Figures derived only from synthetic plotting fixtures do not satisfy this requirement." Methods discusses `torch.use_deterministic_algorithms` and `CUBLAS_WORKSPACE_CONFIG` (2185) and which codebase parameterizes the frame by which mechanism. By `L17_architecture.py`, implementation vocabulary scores 32 hits in 898 words of Methods and statements, 38 in Appendix H, and 33 in the bundle section. None of this bears on any physics claim in the paper, and a foundations referee will read it as a sign that the paper's evidence base is software.

**Fix.** Move all of it to the repository or the online supplement. Keep in the main text one statement that no multi-agent simulation result is claimed. The LLM-assistance statement stays: journals now require it. It should name the current model versions used, which I cannot verify.

**Falsifies:** A physics claim in the paper whose support requires the CUDA, seed, or hash apparatus. None exists, since no simulation result is claimed (2165).

**Status:** Not a claim-status item.

### L17-9: Macro-level prose and vocabulary problems for physicists

**Location:** Whole manuscript. Examples at 45, 66, 75-92, 1812, 2091.

**Severity:** medium.

**Evidence.**
- **Paragraph and sentence length.** From `L17_sentences.py`, the median sentence runs 33 words in the introduction and 36.5 words in Part II. In Part II, 33 percent of sentences exceed 50 words, with a maximum of 270. Source paragraphs are single lines of up to 425 words (132, 429, 418).
- **Three names for one ontology.** Line 81 introduces "cognitive-first structural monism", "information-geometric structuralism", and "pan-agentic structuralism" for one position.
- **Title and keywords signal ML.** The title ends "Mathematical Foundations and Computational Implementation", and the keywords include "Transformer architectures" (66).
- **ML and neuroscience jargon without definition for physicists.** W_Q, W_K, W_V, W_O; RoPE; ALiBi; GLU; LayerNorm; PriorBank (1775); perplexity; iso-token; causal masking. This vocabulary accounts for 548 hits, 139 of them in the transformer section. L09-5 notes that perplexity is never defined.
- **Physics words in non-physics senses.** "Renormalization group" for a block-variable coarse-graining (L06-1); "mass" for a Hessian with a postulated kinetic metric (L02-3); "equilibrium" and "non-equilibrium" (L06-9); "Lorentzian" for a pure-gauge trace form (L11-1, L11-2); "Yang-Mills" without a gauge-theory citation (L14-4). Each is registered by another lens.
- **No base units anywhere** (L11-7).

**Fix.** Split every paragraph over about 180 words. Target a median sentence of about 25 words. Choose one name for the ontology. Retitle without "Computational Implementation". Replace the transformer keyword with "participatory realism" and "it from bit". Define each remaining ML term at first use, or move it to the ML companion with the transformer material. Where a physics word is used in an extended sense, say so once in the status table.

**Falsifies:** Sentence statistics on the rendered PDF differing materially from the source-level count. The script strips math and citations, so I expect agreement within a few words.

**Status:** Not a claim-status item.

### L17-10: Complementarity: PIFB2 never cites the Theory manuscript, and its conclusions still assert constructs the Theory replaces

**Location:** 678, 1703-1731, 2154; bibliography.

**Severity:** medium.

**Evidence.** `grep` finds no citation of the Theory manuscript ("Gauge-Covariant Variational Free Energy and Exact Coarse-Graining", `Theory/main.tex`). The only trace is the anonymous "companion exact-ELBO treatment" at 678. The global conclusion lists "apex closure" among what "Part I established" (2154). The ledger's framing decisions record that the Theory replaces the self-closing apex by a declared root and the barycenter and detector by normalized marked parents. That is registered (ledger) and not re-litigated here. The architectural consequence: a reader of both documents meets the same author asserting incompatible constructions, with no pointer between them.

**Fix (PIFB2-side only).** Once the Theory manuscript is posted, add one paragraph at the end of §1. It should state that the Theory develops the single-point mathematics further and that, where the constructions differ, the Theory's supersedes. Add a three-column crosswalk table (PIFB2 construction, Theory result, relation: supplied, generalized, superseded) in an appendix, taken from section (b) of the 2026-09-23 C1 review with labels re-mapped. Label pointers verified by `grep` today: `c05_evidence_bound.tex` `thm:obs-collective-vfe`; `c06_attention.tex` `sec:selective-transformer` and `eq:obs-selective-dot-product`; `c07_fiber_geometry.tex` `sec:hist-fisher-duration`; `c11_network_coarsegraining.tex` `thm:rg-complete-effective-theory`; `c12_multiscale_vfe.tex` `sec:full-graph-closing-tower` and `sec:obs-participatory`; `c13_formation.tex` `ch:finite-depth-formation`; `c14_interpretation.tex` `sec:phil-participatory`; Supplement B `b02_base_direction_geometry.tex` `ch:pullback-geometry`. The earlier label names in C1 (for example `def:pb-informational-pullbacks`, `prop:obs-declared-root-unavoidable`, `def:hist-fisher-clock`) no longer exist in the current files. Rewrite 2154 so that the apex is "proposed", not "established". This respects `Theory/SPEC.md` section 0, which forbids only the Theory citing PIFB2.

**Falsifies:** A citation of the Theory in PIFB2 under another name that my grep for "Theory", "exact-ELBO", and Dennis bibkeys missed.

**Status:** The apex closure is C/prospective (fence F2), so "established" at 2154 inflates it.

### L17-11: Three conclusions and an interleaved back matter

**Location:** 1802-1807, 2152-2159, 2160-2211, 3939-3941.

**Severity:** low.

**Evidence.** The paper has a "Conclusion to Part I", a "Conclusion", and an Appendix I "Summary". Methods and Statements sit between the conclusion and the appendices. The global conclusion restates Part II's contents rather than the result.

**Fix.** One conclusion. Statements go after it, and methods go to the repository (L17-8).

**Falsifies:** Venue style permitting this order. Springer and MDPI templates place declarations after the conclusion and before references, and neither has a Methods section after the conclusion for a theory paper.

**Status:** Not a claim-status item.

## Verified, no defect

- **Parent-frame non-identifiability (PIFB2.tex:1575).** Method: float64, K = 3, random U_i, U_I, μ_I, Σ_I; U_I moved to U_I g at fixed m = U_I⁻¹μ_I and S = U_I⁻¹Σ_I U_I⁻ᵀ. Residual: shadow mean 3.3e-16, covariance 5.3e-15. Script `L17_line1575_checks.py`. Status P (algebraic identity).
- **No left-equivariant permutation-symmetric map GL⁺(K)ⁿ → GL⁺(K), K ≥ 2, n ≥ 2 (PIFB2.tex:1575).** Method: witness check for (K, n) ∈ {(2,2), (2,3), (3,2), (4,5)}. det v = 1; left multiplication permutes the tuple (True in all cases); dim ker(v − I) = K − 2 < K, so (v − I)M = 0 excludes invertible M. Script `L17_line1575_checks.py`. Residual: exact (rank computations). The proof as written holds for K > 2 via the rank bound, which the text's "M cannot be invertible" covers. Status P.
- **Word-count bookkeeping.** Section-level raw counts sum to exactly the `wc -w` total of 79,455 (`L17_wordcount.py`). The brief's figure is confirmed.
- **Manuscript bytes.** SHA-256 matches the brief (`f80e6dab…080ec4`).

## Physics-audience and standalone notes

A physics referee at FoP will look for three things in the first two pages: the question, the answer, and what is proved. The question should be Wheeler's. Today the first page is a 530-word abstract whose headline results are an attention recovery, a WikiText fit, and a statement about "the checked-in multi-agent implementation". That reader will classify the paper as machine learning with philosophical framing before reaching the pullback construction, which begins after about 36,000 words of text.

Standalone reading requires that the reader never needs the code, the ML companion, the meta-entropy note, or the Theory manuscript to check a claim. Line 678 fails this outright. Lines 59, 100, 436-455, 1613, 1692, 1705, 1712, and 2185 fail it in spirit. The remedy in L17-3 and L17-4 makes the Theory manuscript a citation target, so it must be posted first.

Material a physicist will not miss if moved: the transformer recovery, WikiText, RoPE and ALiBi, masking, the gradients appendix, the executable table, and the prospective protocol. Material a physicist will object to in place: "renormalization group" without a flow, "mass" by postulate, "Lorentzian" from a pure-gauge form, and consciousness. Material a physicist will value if foregrounded: the clock-dissipation identity, the pullback tensor with its gauge behavior, the equivariance no-go and parent-frame non-identifiability, the regulator obstruction, and a plain statement of what the model does not deliver (quantum, units, signature selection).

## Complementarity notes

The Theory manuscript should be cited, once posted, for the exact evidence-bound status of the consensus row (678; `c05_evidence_bound.tex` `thm:obs-collective-vfe`, `c06_attention.tex` `sec:local-attention-elbo`). It should also be cited for coarse-graining beyond the covariance theorem (Appendix I; `c11_network_coarsegraining.tex` `thm:rg-complete-effective-theory`), the downward kernels that replace the transported-posterior shadow (Appendix G; `c12_multiscale_vfe.tex` `sec:full-graph-vfe-downward`, `c04_generative.tex` `sec:gen-typing`), the tower closure (1725-1727; `c12_multiscale_vfe.tex` `sec:full-graph-closing-tower`), the Fisher clock (1837-1848; `c07_fiber_geometry.tex` `sec:hist-fisher-duration`), and the participatory reading (`c14_interpretation.tex` `sec:phil-participatory`, which cites Wheeler 1990 at line 154). The pullback geometry that is PIFB2's "it" is developed in Theory Supplement B (`b02_base_direction_geometry.tex`, `ch:pullback-geometry`). That supplement is deferred base-transport work under the repository's scope gate, so PIFB2's §7 remains the only place the "it" is argued for readers, and it should be kept, not replaced. Division of labor for the pair: the Theory carries proofs at one base point; PIFB2 carries the Wheeler argument, cites the Theory for each formal claim, and keeps only the proofs a physicist needs in hand (Appendix B of the outline). No Theory change is required by these recommendations.

## Not covered

- Prose-level correctness of the unread body ranges listed in the header; other lenses cover them.
- The outcome of the `Dennis2025it` Foundations of Physics submission.
- Full-text verification of FoP, Entropy, and PRR author guidelines. The pages returned login redirects or HTTP 403, so the abstract limits rest on search-engine snippets of the official pages. The J Phys Complexity and J Phys A figures were fetched directly.
- Whether journals will accept citations to the Theory manuscript as an arXiv preprint for the replaced sections; this depends on the Theory being posted.
- Rendered-PDF page count (not compiled).
