---
type: manuscript
title: "Restructured Theory manuscript at 623e4fe, September 24, 2026"
aliases: ["Theory restructure September 2026", "MultiAgentELBO Theory at 623e4fe"]
tags: [cluster/multi-agent, cluster/vfe, cluster/gauge-theory, cluster/info-geometry, cluster/attention, project/multi-agent, field/mathematics, field/physics, field/statistics]
url: https://github.com/cdenn016/MultiAgentELBO/pull/81
created: 2026-09-24
updated: 2026-09-24
year: 2026
---

# Restructured Theory manuscript at 623e4fe, September 24, 2026

This note records the outcome of the streamlining that followed the September 23 review of the MultiAgentELBO `Theory/` manuscript ([[multiagentelbo-2026-09-23-theory-streamlining-review]]). At `59c1987` the manuscript was one 559-page document. At `623e4fef5404f5dc95dc615437e4e4504ab00492` (short `623e4fe`), the merge of [pull request #81](https://github.com/cdenn016/MultiAgentELBO/pull/81) into `main` on September 24, 2026, it is three documents built from one source directory: a main manuscript at one base point, Supplement G for the multivariate-Gaussian realization, and Supplement B for base transport, infinite networks and the lattice cluster ([the tree at that revision](https://github.com/cdenn016/MultiAgentELBO/tree/623e4fef5404f5dc95dc615437e4e4504ab00492/Theory)).

The records used here are committed at `623e4fe` under `docs/reviews/2026-09-23-theory-streamlining-review/`: `phase2/FINAL-REPORT.md` (the final state after the overnight polish), `phase2/CONDENSE-REPORT.md` (the condensation pass), `phase2/STAGE2-REPORT.md` (the split integration), `phase2/PLAN.md` (the split plan, its §1.1 outline and the author answers of §6.3) and `remediation/PHASE1-SUMMARY.md` (Phase 1), together with `Theory/SPEC.md` §0 and the `.tex` sources at that revision. The review folder was uncommitted when the September 23 note was written. Its `REPORT.md` and the nine findings files that note bound by SHA-256 are now committed, and all ten committed files match the recorded hashes (rechecked for this ingest).

The vault mirror `manuscripts/gauge_vfe_rg/` predates this restructure and was not updated. It still holds the pre-split files (`05d_relational_inference.tex`, `06_gaussian.tex`, `07b_agent_network_rg.tex`, `07j_finite_depth_adaptive_formation.tex`, `appendix_claim_ledger.tex` and the rest) and none of the new `c*`, `g*` or `b*` chapter files, and the verified ledger already records that it lagged `59c1987` on September 23. Read the restructured documents in the repository.

```bibtex
@misc{multiagentelbo2026theoryrestructure,
  author = {MultiAgentELBO research program},
  title = {Gauge-Covariant Variational Free Energy and Exact Coarse-Graining; Supplement G: The Multivariate-Gaussian Realization; Supplement B: Base Transport, Infinite Networks, and the Lattice Cluster},
  year = {2026},
  note = {Theory/ at commit 623e4fef5404f5dc95dc615437e4e4504ab00492, merged September 24, 2026 as pull request 81},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/81}
}
```

## Provenance and epistemic status

> [!warning] Agent-produced, one model, no cross-model check, not adjudicated
> Every edit, count, build and check recorded here was produced by Claude Opus 5.5 agents: the sixteen Phase 1 remediation groups, the Phase 2 planning, content, integration and back-matter packages, the thirteen condensers, the overnight proof-move, locator and glyph agents, and the serial owners who wrote the reports. The Fable cross-model check and repair stages were dropped at the author's request, so no cross-model verification, verifier panel or adjudication ran on any of it. The checks are the agents' own executed SymPy and NumPy scripts, their LaTeX builds, a mechanical label-graph check and textual comparisons. They support the instances they compute and the bookkeeping they count, and they are not independent confirmation. An ESTABLISHED tag below is the manuscript's own status claim for a proof written or edited by these agents. This ingest did not rebuild the documents or rerun the agents' scripts; besides reading the committed sources it rechecked the ten review hashes, the access-restriction value and the majority-rule witness of the Phase 1 corrections below, itself on the same model family. No tamper check ran, and the `Theory/verification/` harness was not run (open item five).

## Commit sequence

| Commit | Time (UTC−5) | Content |
|---|---|---|
| `2d012d1` | 2026-09-23 16:50 | Phase 1 remediation. Sixteen file-disjoint groups fixed 303 review items, deferred 216 to Phase 2 and rejected 5 on evidence, added 158 labels and 45 checked bibliography entries, and added the verified ledger at `docs/reviews/verified-ledger.md`. The single document grew from 559 to 649 pages. |
| `a9a0dcb` | 2026-09-23 21:05 | The three-document split under `PLAN.md`: 17 work packages, integration and the Stage 3 deletions. Pages 297 (main), 120 (G) and 188 (B). SPEC rewritten, `Theory/CONTENT.md` added, dated SPEC material moved to `docs/research-log/`, the grand-canonical note moved to `docs/research/program-notes/`. |
| `bfc195c` | 2026-09-23 22:21 | Condensation of the main manuscript by thirteen condensers under per-file page budgets, with no result cut: 297 to 246 pages, source words 109,577 to 95,680. |
| `6727af6` | 2026-09-24 00:09 | Deferred Proofs appendix (51 proofs from Chapters 6, 7, 9 and 11), citation-locator verification, one Gaussian proposition moved to Supplement G, notation renames and one proof-heading style. |
| `653f318` | 2026-09-24 00:10 | Appendix chapters and their sections named "appendix" in cross-references. |
| `623e4fe` | 2026-09-24 04:48 | Merge of pull request #81 into `main`. |

## Three-document architecture

`Theory/SPEC.md` §0 fixes the architecture. The main manuscript develops, at one fixed base point $c_*$, agents as local sections of belief and model associated bundles of one principal $G$-bundle, their independent dynamic interaction links, the normalized joint law and one collective evidence bound, attention and selective communication, fiber information geometry and inference histories, fast beliefs and slow models, exact coarse-graining of the pointwise agent network, and meta-agent formation. It must read on its own, contains no `\cref` into a supplement, and may name a supplement as a document. Supplement G cites only the main manuscript. Supplement B may cite the main manuscript and Supplement G, and it carries connections, covers and connection descent, base-direction pullbacks and section-space histories, multi-point designs, the relative-frame apparatus, the asymptotic Wilsonian apparatus (mode exponents, tempered comparisons, interaction beta functions, fixed points, scale connection) and the lattice cluster. No document contains repository paths, code modules, configuration keys, run records or hashes.

The main manuscript is titled *Gauge-Covariant Variational Free Energy and Exact Coarse-Graining*. The physical page counts of its final build are these; the last row runs to the end of the PDF and so includes the seven-page bibliography and the front-matter offset.

| Part | Chapter or appendix | Pages |
|---|---|---|
| I Single-Point Foundations | 1 Program, Scope, and Standing Conventions | 5 |
| | 2 Geometry at One Base Point | 9 |
| | 3 Probability Semantics at $c_*$ | 10 |
| | 4 The Fixed Normalized Generative Law | 6 |
| | 5 One Evidence Bound and Local-Collective Free Energy | 17 |
| | 6 Attention and Selective Communication | 16 |
| | 7 Fiber Information Geometry and Inference Histories | 22 |
| | 8 Two-Timescale Dynamics (with the Part II page) | 8 |
| II Exact Coarse-Graining at One Base Point | 9 Coarse Channels | 14 |
| | 10 Gauge-Retained Network State and Fixed Sectors | 15 |
| | 11 Exact Agent-Network Coarse-Graining | 20 |
| | 12 The Multiscale Graph VFE and Closing the Tower (with the Part III page) | 15 |
| III Formation and Interpretation | 13 Formation Witnesses | 16 |
| | 14 Interpretation and Its Limits | 4 |
| | 15 Related Work | 4 |
| Appendices | A Measure-Theoretic Lemmas and Integrability Witnesses | 5 |
| | B Deferred Proofs | 14 |
| | C Proofs for Finite-Depth Formation | 24 |
| | D Notation | 3 |
| | E Open Problems and Conjectures | 4 |
| | F Numerical Index, with the bibliography | 15 |
| Total | | 247 |

Chapters 1–15 come to about 181 pages. The main manuscript holds 352 numbered statements (87 definitions, 13 standing hypotheses, 114 propositions, 35 theorems, 22 lemmas, 30 corollaries, 27 remarks, 23 open problems and 1 conjecture) and 216 proofs, and none of its statements has status NUMERICAL.

Supplement G, *The Multivariate-Gaussian Realization* (118 pages; 147 numbered statements, 114 proofs), has the chapters G0 Introduction, G1 Exponential Families and the Operator Layer, G2 Gaussian Realization at $c_*$, G3 The Interaction Family, G4 Recognition Restrictions, G5 Fisher Geometry and Invariants, G6 Ambient Score Tangents and the Hermite Spectrum, G7 Coarse Maps I: Aggregation and Kron Closure, G8 Coarse Maps II: Nonflat Links, Relaxation, and Quotient Volume, G9 Operator Coarse-Graining and G10 Reciprocal Pairs, Anchored Stars, and Loop Holonomy, followed by the appendices GA Decision Metatheory and GB (notation, open problems and numerical index). Supplement B, *Base Transport, Infinite Networks, and the Lattice Cluster* (187 pages; 243 numbered statements, 160 proofs), has three parts. Part B-I, Base Transport and Multi-Point Designs, holds B0 Introduction, B1 Base Geometry and Multi-Point Designs, B2 Base-Direction Information Geometry, B3 Section-Space Histories and Base Averaging and B4 Covers and Connection Descent. Part B-II, Infinite Networks and Wilsonian Asymptotics, holds B5 Comparison Data, Modes, and Interaction Beta Functions and B6 Continuous Scale, Fixed Points, Spectra, and Two-Index Limits. Part B-III, The Lattice Cluster, holds B7 The Lattice Cluster: Typing Question and Constructive Spatial RG, B8 Transport, Label Pressure, and Specific VFE and B9 Thermodynamic Fisher Geometry of Retained Ensembles, followed by the proof appendices BA to BC and the back matter BD.

The page count went from 559 at `59c1987` to 649 after Phase 1, which corrected and added, then to 297, 120 and 188 after the split, to 246 for the main manuscript after condensation, and to 247, 118 and 187 at the end. The review had proposed 150–170, 40–50 and 60–80 pages, and the split plan estimated about 180, 61 and 116. Under decision D10 the author accepted the larger totals rather than cut results. Against the condensation budgets, Chapter 6 (16 pages against 14), Chapter 7 (22 against 19) and Chapter 11 (20 against 19) remain over; moving proofs into the Deferred Proofs appendix shifted pages between chapters without shortening the document.

## Author decisions D1–D13

D1–D9 were taken on September 23 before Phase 1, and D10–D13 answer the four questions of `PLAN.md` §6.2. `SPEC.md` builds all thirteen into its rules. They are stated here in the manuscript's vocabulary.

| Decision | Content |
|---|---|
| D1 | Status is shown once per numbered statement. Every theorem-type statement and claim-bearing remark carries exactly one tag: ESTABLISHED (proved in the manuscript), STANDARD (a known result cited to a checked primary source with a locator) or NUMERICAL (supported only by a named computation). NOT-CLAIMED appears once per scope paragraph. Definitions, standing hypotheses, conjectures and open problems carry their status in the heading type, and unnumbered text makes no new claim. |
| D2 | Belief and model channels use one common local frame $u_i$ per agent at $c_*$, a gauge choice rather than a hypothesis, because no energy, kernel or evaluator reads the relative frame. The relative frame $h_i$ lives in Supplement B and returns to the core only if frames become dynamical agent states. |
| D3 | The typing of the $\mathbb Z^2$ lattice (sites as agents at $c_*$ or as base points) is deferred as `open:rg-lattice-typing`, and the lattice cluster goes to Supplement B. The lattice-free finite-mixture Fisher theorems stay in Chapter 9. |
| D4 | Chapter 1 states the aim of the program in the manuscript's own typed vocabulary (agents as local sections, collectives formed through coupled inference, parents acting on children through normalized laws). It imports nothing from PIFB2 and does not cite it; a separate program paper comes later. |
| D5 | The single-point renormalization is the exact finite-step coarse-graining channel of the pointwise agent network (effective action, residual, finite-step multipliers and the native growth bound), called exact coarse-graining. Relevant, irrelevant, fixed point and beta function appear in the main manuscript only in one pointer to Supplement B and in Chapter 15 about other authors' constructions; the asymptotic apparatus is in Supplement B. |
| D6 | Coarse Gaussian families in Supplement G admit newly generated positive-semidefinite self terms; the strict no-new-anchor pair family is the named subfamily `def:cg-no-new-anchor-pair` of the main manuscript. |
| D7 | The finite-depth formation theorem and its proof appendix stay in the main manuscript, with the scope stated in the chapter. |
| D8 | The interaction graph at $c_*$ is the support of the source prior, a structural parameter that is complete unless masked. Attention weights are strictly positive on it, and dynamic structure is carried by attention weights and link values. Discrete edge creation and deletion is one open problem, `open:obs-edge-creation`, not part of the model, and coarse multigraphs are induced structure. The grand-canonical note left the manuscript for `docs/`. The handoff record says this default was taken after the author answered "not sure; beta_ij is real-valued and dynamic", to be confirmed if revisited. |
| D9 | The thermodynamic Fisher theorems are ESTABLISHED at their stated hypotheses. |
| D10 | The page estimates are accepted; prose, duplication and disclaimers are trimmed, and no result is cut beyond the plan's cut list. |
| D11 | Supplement G cites only the main manuscript; Supplement B may cite the main manuscript and Supplement G. |
| D12 | Meta-agent membership may be random: the finite partition catalog of the normalization models (hierarchical or global normalization), typed as the structural mark $R_\ell$, is intended at $c_*$ and enters Chapter 12, and it creates no edge. |
| D13 | Chapter 14 states exactly one numbered conjecture with its refuting observation and a ledger row: `conj:phil-contrast-formation`, contrast formation under source learning. |

## Verification facts, as reported

The final report states that the three documents build from a fresh scratch copy of the sources, in the order main, G, B, G, B, with no LaTeX error, no undefined reference or citation, no multiply defined label, no overfull box, and no LaTeX, package or BibTeX warning; three underfull boxes remain in the main bibliography. After the cross-reference addendum (`653f318`) the documents rebuild at 247, 118 and 187 pages with no error, undefined reference, multiply defined label or overfull box. The split-mode label check reports 2,537 labels, none multiply defined, no coverage deviation and zero violations, where a violation is a label in the wrong document or a reference that breaks the direction rules of D11 and SPEC §0.

Relative to `bfc195c`, the overnight polish kept the same 742 numbered statements and 490 proofs across the three documents. One proposition, `prop:hist-normal-barycenter-kernel` (normal barycenters and parameter-independent kernels), moved with its proof from Chapter 7 to Supplement G, Chapter G8, and one ESTABLISHED tag moved with it. Proof text changed beyond verbatim moves only by glyph renames, one renamed kernel, two binomials written in amsmath form and the recorded Stage A edits, each checked by a script, a diff reading or typesetting. The earlier steps removed material in two recorded ways only. The split cut the 90 units of the plan's cut list: 57 superseded by labels that survive in one of the documents, 30 by a cited primary source or by prose elsewhere, and 3 ledger rows, with every cut that would replace a proof by a citation conditional on a checked locator. The condensation cut no result but replaced one remark, `rem:cg-parameter-dependent-channel`, by a pointer to `thm:hist-record-clock-contraction`, which proves the same Bernoulli witness in another chart (open item two). The condensers also changed wording inside a few statements, each reported as equivalent or stronger and not checked further by the integrator; the most visible is that conclusion (a) of the formation theorem now states its remainder as $r_\epsilon=O(\epsilon^{2Q_1+20})$ uniformly in $L$.

The status-tag load fell sharply. At `59c1987` the one-tag-per-paragraph rule rendered 1,374 status tags against 489 numbered statements. Under D1 the final raw tag counts are ESTABLISHED 227, STANDARD 3, NUMERICAL 1 and NOT-CLAIMED 16 in the main manuscript, each including the one printed name in the Chapter 1 status table; ESTABLISHED 115, STANDARD 2 and NOT-CLAIMED 12 in Supplement G; and ESTABLISHED 160, NUMERICAL 3 and NOT-CLAIMED 9 in Supplement B. The numbered-statement totals grew because unnumbered claims were numbered or retyped (constructions became definitions and requirements became standing hypotheses), so totals before and after are not directly comparable. A final text scan of all 52 input files found no banned phrase, spacing macro, horizontal rule, repository path or hash, and no date other than the title-page dates and two random seeds.

A locator agent checked twelve assigned citation locators and one extra against primary sources. Two were corrected (Cencov, below, and Jona-Lasinio 2001 to the journal's "Sec. 2, Eq. (2.14)"), one bibliography entry was fixed (Lian and Lu 2010 as an article), and the rest were verified as printed. The report's caveats are that the Borgs–Kotecký theorem number was read in the authors' preprint, Kemeny–Snell in the 1960 text that the cited 1976 edition reprints, and several book locators through search snippets rather than full pages.

## The verified ledger

The review's verified ledger is `docs/reviews/verified-ledger.md` in the MultiAgentELBO repository, added in `2d012d1`. It binds its Theory entries to `59c1987` and treats labels as canonical, so its entries are read in the restructured documents by label; it has not been rebound to `623e4fe`. It marks the September 23 entries as investigator checks by Claude Opus 5.5, not adjudicated, and states that agreement between agents of one model family is not independent confirmation. It was first written to the vault path `manuscripts/verified-ledger.md` and then moved to the repository, because that vault path had held a GL(K) ledger the author deliberately deleted; this ingest does not restore that path.

## Where the September 23 findings now stand

Locations are labels in the committed sources; chapter numbers are those of the final build.

| Finding (investigator) | Status at `623e4fe` | Location |
|---|---|---|
| Native growth bound for exact interaction RG (X06) | Incorporated: the ordered product telescopes and $\lVert D_{n\leftarrow\ell}\rVert\le3^{\lvert V_n\rvert}-1$, independent of the number of steps. The companion finite-network obstruction (dimension 63 to 7 for six binary agents in three blocks; at most $\log_b\lvert V_\ell\rvert$ vertex-ratio steps) is a separate proposition. | Main, Ch. 11: `prop:rg-interaction-native-growth-bound`, `prop:rg-interaction-finite-network-obstruction` |
| Fixed measure pairs trivial under unique ergodicity (X06) | Incorporated, and moved with the Wilsonian apparatus (D5). | Supplement B, Ch. B6: `prop:rg-fixed-pair-unique-ergodicity` |
| Law coherence as a third agreement (C1, X01) | Incorporated, with the C1 witness inside the statement. | Main, Ch. 2: `def:geo-law-coherence`, `prop:geo-three-agreements` |
| Per-edge twist invariants; flat versus identity links (X01, E1) | Incorporated. | Main, Ch. 2: `prop:geo-edge-twist-invariance`, `def:geo-graph-flat-links`, `rem:geo-flatness-strictness` |
| Active gauge image at one point; common frame as a gauge choice (X01, E1) | Incorporated; the relative frame and its $G\times G$ apparatus moved out (D2). | Main, Ch. 2: `prop:geo-active-image-point`, `prop:geo-common-frame-gauge`; relative frame in Supplement B |
| Orbit Fisher form (X03) | Incorporated, with its proof in Appendix B.2. X03's cubic coefficient is stated for one-sided contrast expansions along base-direction curves. | Main, Ch. 7: `cor:pb-orbit-fisher-form`; Supplement B, Ch. B2: `prop:pb-divergence-cubic-coefficient` |
| $\Lambda$-dependent Galerkin pushforward (X11) | Incorporated in the Gaussian supplement, with the varying-precision case open; the main manuscript separates Markov pushforward, precomposition and Galerkin restriction. | Supplement G, Ch. G7: `prop:ig-galerkin-pushforward`; Ch. G9: `open:grg-galerkin-monotonicity`; main, Ch. 9: `sec:cg-three-operations` |
| Gauge absorption of the SPEC rotation witness (X11) | Incorporated: gain absorption with the orientation criterion $(-1)^K\det\Lambda_{12}>0$, the original witness absorbed, and chart-independent witnesses (an orientation-reversing gain; for odd $K$, a v-structure). | Supplement G, Ch. G3: `prop:gauss-gain-absorption`, `prop:gauss-law-level-witnesses` |
| Rate-separated clocks and the correlated slow-manifold shift (X04) | Incorporated in a new two-timescale chapter; the Tikhonov–Fenichel limit is an open problem, not a theorem. | Main, Ch. 8: `def:obs-fast-slow-blocks` (cited by Ch. 4), `lem:obs-envelope-slow-flow`, `prop:obs-rate-separated-flow`, `rem:obs-rate-separation-witnesses`, `open:obs-slow-manifold` |
| Attention-model mismatch between Chapters 7 and 13; reduced attention Hessian (X14) | Incorporated: one attention chapter declares both label models, the typed event law, the constant-row cost and the reduced Hessian; the occupancy results are split by model. | Main, Ch. 6: `def:obs-attention-label-model`, `hyp:rg-single-edge-attention`, `def:obs-attention-event-law`, `prop:obs-attention-constant-row-gap`, `prop:obs-attention-reduced-hessian`; Ch. 11: `prop:rg-attention-single-edge-weights`, `prop:rg-attention-per-receiver-collapse` |
| Undefined regeneration rule behind the 07b NUMERICAL readings (X14) | The dated readings left the manuscript for `docs/research-log/theory-verification-narratives.md`. Supplement B keeps one NUMERICAL remark that declares the rule an approximate channel whose error relative to the exact event-law pushforward is not bounded. | Supplement B, Ch. B6: `rem:rg-regenerated-attention-computation` |
| Scope of the finite-depth formation witness (X07) | Incorporated: theorem retitled, saturation and calibration stated, quantifiers reordered, the Gaussian-core loss and the sharpness question added, and the September 20 four-cycle witness brought into the manuscript. | Main, Ch. 13: `thm:finite-depth-adaptive-formation`, `rem:rg-formation-saturation`, `prop:rg-formation-gaussian-core`, `open:rg-formation-regime-sharpness`, `prop:rg-formation-endogenous-cycle`; Ch. 14: `conj:phil-contrast-formation` |
| 07c factorization omits the coarse graph datum (X01, E4) | Corrected in Phase 1 (next section). | Main, Ch. 12 |
| Contradictory thermodynamic Fisher status | Settled by D9 as ESTABLISHED. | Supplement B, Ch. B9, proofs in BC; lattice-free finite-mixture version in main, Ch. 9 |

The concept pages listed under "Relevance to this research" discuss these entries with their epistemic status.

## Phase 1 corrections worth banking

The 07c hierarchical factorization now conditions on the full next-depth state. At `59c1987` the depth-$\ell$ factors of the multiscale graph VFE read only the coarse configuration and the structural mark, which is not the disintegration the text claimed. Phase 1 conditioned every depth-$\ell$ factor on $Y_{\ell+1}=(Z_{\ell+1},\mathfrak N_{\ell+1})$, the coarse configuration together with the coarse graph datum, and on $R_\ell$. Chapter 12 now states this as the standing hypothesis `hyp:full-graph-depth-markov`, proves in `lem:full-graph-adaptive-reversal` that every adaptive tower satisfies it through its reversal (bridge) kernels, and computes the cost of dropping the graph datum in `prop:full-graph-dropped-datum`:
$$
\mathrm{KL}\bigl(\mathbb P^{\mathrm{tow}}\Vert\mathbb P^{\mathrm{red}}\bigr)=\sum_{\ell=0}^{L-1}I_{\mathbb P^{\mathrm{tow}}}\bigl(Y_\ell;\mathfrak N_{\ell+1}\mid Z_{\ell+1},R_\ell\bigr),
$$
which is $\log2$ in a four-vertex witness whose fine event law has two equally likely atoms pushed to different coarse event laws. The decomposition theorem `thm:full-graph-vfe-decomposition` is restated with these conditioning sets. The Phase 1 script recovered the witness exactly in rational arithmetic and, on 40 random depth-3 adaptive towers, matched the corrected factorization to $2.8\times10^{-17}$ and the divergence to the conditional mutual-information sum to $2.4\times10^{-15}$.

The access-restriction floor is the Chernoff information, 0.08850 nats, not 0.0889. In the two-agent binary witness of `prop:prob-access-restriction`(ii) in Chapter 3, the prior puts 0.45 on each agreeing pair and 0.05 on each disagreeing pair, each record reports its latent correctly with probability 0.8, and agent 1's recognition law reads only its own record, so it is the same $\mathrm{Ber}(t)$ at the observations $(1,0)$ and $(1,1)$, where the posterior marginals of $y_1$ are $(37/89,52/89)$ and $(13/161,148/161)$. Investigator X02 had proposed that the larger of the two relative entropies to the posterior is at least 0.0889 nats. Phase 1 rejected that number as an artifact of a grid of step 0.001: the exact minimax value is $\sup_{\xi\in[0,1]}(-\log Z_\xi)$ with $Z_\xi=\sum_{y_1}\Pi^{(0)}_1(y_1)^\xi\Pi^{(1)}_1(y_1)^{1-\xi}$, attained at $\xi\approx0.5483$ and reached by $\mathrm{Ber}(t)$ at $t\approx0.7834$, so the claimed floor was too large by about $4\times10^{-4}$. The manuscript prints $0.08849\ldots$ and states the bound is sharp. This ingest recomputed the marginals and both optimizations and obtained 0.08849703 at $\xi=0.54826$ and $t=0.78336$.

Nested partitions do not compose functorially under majority rule. Investigator X05 had written that deterministic nested partitions compose functorially automatically. Phase 1 found this true only for arrows that keep the complete block configuration or an additive block statistic such as block sums. Majority rule with ties resolved by the first block member fails on 16 of the 64 configurations of six binary sites when pairs-then-triples is compared with triples-then-pairs. Chapter 9's `prop:rg-scale-functoriality` states the dichotomy with the witness $(0,0,1,0,1,0)$, which goes to $1$ by pairs then triples and to $0$ by triples then pairs (checked by hand for this ingest). It adds that on a chain of resolutions functoriality imposes no condition, so its content lies in non-chain posets and in the semigroup law $K_{b_1b_2}=K_{b_1}K_{b_2}$ of a blocking rule, and that mutually inverse Markov kernels between finite spaces are permutation matrices. The same Phase 1 group corrected a depth bound: steps that each merge at least two agents give depth at most $\lvert V_0\rvert-1$, while depth at most $\log_2\lvert V_0\rvert$ needs every coarse agent to be a block of at least two agents.

The Cencov locator is Lemma 11.3, p. 161. The Fisher-uniqueness citation of `prop:ig-fisher-characterizations` in Chapter 7, which states that on the open simplex of positive laws on a finite set the Fisher metric is, up to a positive factor, the unique Riemannian metric invariant under congruent Markov embeddings, now reads `\citep[Lemma~11.3, p.~161]{Cencov1982}` in place of p. 156 ([[cencov-1982-statistical-decision-rules]]). The statement is tagged STANDARD. This is the locator agent's reading, and the report does not say whether this page was read in full or through a snippet.

## Left open for the author

The final report leaves eleven items open. First, an agent sharpened `conj:phil-contrast-formation` from positive formation probability, which the support theorem already gives at fixed $\epsilon$, to a positive lower bound uniform as $\epsilon\to0$ for Lebesgue-almost every initial mean on the four-cycle family with source-prior learning; the author must confirm this family. Second, the author must decide whether replacing `rem:cg-parameter-dependent-channel` by a pointer to a result that proves the same witness in another chart removes an exact duplicate (restoring it costs about four lines). Third, three Phase 1 anchor labels (`eq:rg-root-framed-child-tuple`, `eq:rg-feature-holonomy-fixed-space`, `eq:cg-cut-interval-width`) were cut with their formulas run inline, and restoring the displays would likely add a page to Chapter 10. Fourth, two random seeds in the Supplement G numerical index read as dates, against the no-dates rule. Fifth, the `Theory/verification/` harness still names the pre-split files and cannot run; it was left untouched and unrun because its tests include forged-input, corruption and tamper scenarios, so a repair must first separate the permitted checks. Sixth, Chapters 6, 7 and 11 remain over their page budgets, and meeting them needs statements moved. Seventh, cross-reference names: appendix naming was fixed after the report by `653f318`, and the lowercase later names in mixed `\Cref` lists remain as cleveref's default. Eighth, three cosmetic underfull boxes remain in the main bibliography. Ninth, glyphs are still reused outside the renamed list, within the main manuscript and across documents. Tenth, locator caveats and cuts not taken: the Bakry–Émery locator is now checked, so a semigroup proof could become a STANDARD citation, while Doob's maximal inequality, Giry 1982 and the measurability routes of Chapter 3 remain unchecked and their proofs stay. Eleventh, earlier items remain: an unproved sentence ("need not define any joint recognition law") was turned into a scope exclusion and needs a witness if the negative statement is wanted, a Supplement B proof could optionally be shortened, and some proof-length choices in Chapter 7 are borderline. The Stage 3 repository items the report also lists (removing the old chapter files, moving the program note, the provenance record) were done before the merge.

## Relevance to this research

The manuscript is now organized around the program's current phase, the theory at one base point, and most structural requests of the September 23 review are in place: typed fast and slow variables with a two-timescale chapter, one attention chapter that declares its label models, the orbit Fisher form, law coherence and per-edge twists as the single-point link content, exact coarse-graining in place of a Wilsonian reading at $c_*$, the corrected multiscale factorization, and a formation chapter whose theorem states its supplied-hierarchy scope next to an endogenous four-cycle witness. Delayed participatory feedback enters as an episode-indexed joint (`def:full-graph-episode-joint` and `prop:full-graph-episode-joint` in Chapter 12), with accounting across episodes left open (`open:full-graph-episode-accounting`). What formation needs next is recorded as open: the contrast-formation conjecture, the slow-manifold reduction, discrete edge creation, the sharpness of the doubly exponential regime and dynamic closure of the pointwise parent (`open:rg-pointwise-parent-dynamics`).

The architecture and a topic-to-location map are on [[Gauge-Theoretic Multi-Agent VFE Model]], and the synthesis is in [[Gauge-VFE RG research synthesis September 2026]]. The status of individual findings is recorded on [[Renormalization-group flow of beliefs]], [[Holonomy]], [[Agents as fibre-bundle sections|Agents as fiber-bundle sections]], [[Fisher information metric]], [[Geometric singular perturbation theory]], [[Coarse Graining]], [[Multi-agent variational free energy]], [[Meta-agents and hierarchical emergence]] and [[Staged hierarchy formation and RG composability]].
