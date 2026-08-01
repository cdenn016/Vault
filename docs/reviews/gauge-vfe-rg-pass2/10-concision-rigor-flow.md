# Pass 2, memo 10 — concision, rigor, and publication flow

## Disposition

The manuscript has a publishable mathematical spine, but the current 255-page artifact presents that spine in the wrong order and repeats its audit apparatus at chapter scale. The decisive revision is architectural:

1. state the independent belief and model gauge systems before any Gaussian coordinates;
2. separate normalized-law coarse maps from energy precomposition and from Gaussian parameter aggregation;
3. define an RG scale diagram before discussing fixed rays, spectra, or universality;
4. move the multivariate-Gaussian construction after those general results;
5. replace thirteen chapter-end registers by one compact ledger and one numerical-provenance appendix.

At the current revision, the chapter source contains 5,950 lines and the rendered PDF has 255 pages. The thirteen repeated status registers occupy 586 source lines; the adjacent RG numerical-evidence block adds 39, for 625 chapter-end register/provenance lines and approximately 33 rendered pages. A conservative editorial target is **730–845 fewer source lines** and **37–42 fewer rendered pages**, yielding approximately **213–218 pages** before any bibliography change. This is a 12.3–14.2% source-line reduction and a 14.5–16.5% page reduction. The estimate assumes a six-to-eight-page centralized ledger plus numerical appendix, retains every theorem domain and qualifier, and does not count further prose polishing.

The revision should not shorten the work by deleting hypotheses, counterexamples, or negative results. It should shorten it by giving each result one canonical home.

## Evidence base and closure status

The present artifact and pass-2 specialist memos 01–09 were checked against the executable LaTeX source. The rendered artifact is `manuscripts/gauge_vfe_rg/main.pdf` (255 pages); `main.tex:53-73` supplies the current chapter order. The structural claims below have the following evidence status under the verification vocabulary.

| Claim | State | Current evidence |
|---|---|---|
| The current book has four parts but puts the introduction outside them and places general coarse theory after the Gaussian realization. | EVIDENCE_VERIFIED | `main.tex:53-73` |
| Repeated chapter-end audit apparatus is the largest safe cut. | EVIDENCE_VERIFIED | Thirteen status-register ranges totaling 586 lines plus the 39-line RG numerical-evidence block; approximately 33 rendered pages in `main.pdf` |
| The present single-principal-bundle formulation does not express the required independent belief/model gauge systems. | REFUTED as a general formulation | `02_geometry.tex:44-140`, especially `:106-140`; pass-2 memos 05, 07, and 08 |
| The same normalized coarse law can have exactly the same evidence after a Markov pushforward, so different latent inventory alone does not imply incomparable evidence. | REFUTED as currently stated | `07_restrictions.tex:304-342`; `09_coarsegraining.tex:797`; exact marginalization already proved at `09_coarsegraining.tex:42-81`; pass-2 memos 04 and 07 |
| The present aggregation recursion is a changing-space coarse diagram, not yet a general RG endomorphism. | EVIDENCE_VERIFIED | `10_renormalization.tex:102-179`, especially `:144-154` and `:177-179`; pass-2 memo 08 |
| The page-reduction target can be achieved without deleting a theorem or counterexample. | EVIDENCE_VERIFIED for the enumerated cuts; final pagination remains CANDIDATE until recompilation | The range-level cut ledger below |

The current PDF/text artifacts agree on the macrostructure. The rendered spans are approximately:

| Material | Current PDF pages |
|---|---:|
| Front matter and introduction | 1–12 |
| Geometry, probability, generative law, ELBO, exponential families | 13–100 |
| Gaussian model, restrictions, information geometry | 101–140 |
| Coarse-graining and RG | 141–224 |
| Obstructions and interpretation | 225–250 |
| Bibliography | 251–255 |

This distribution explains the reading problem: the general coarse-map layer does not begin until page 141, after 40 pages of Gaussian specialization, while audit/provenance blocks recur through page 250.

## Exact target table of contents

The body should have exactly four parts. Appendices follow the four parts and are not a fifth conceptual layer.

### Part I — General Gauge-Variational Foundations

1. **Scope, claims, and reading map**
2. **Independent gauge systems and associated statistical bundles**
3. **Probability kernels and one normalized joint**
4. **The exact ELBO and variational restrictions**
5. **Statistical fibers and exponential families**

### Part II — General Coarse Maps and Renormalization

6. **Markov coarse maps: data processing, equality, recovery, and Fisher contraction**
7. **Energy precomposition and graph-exponential closure**
8. **Scale diagrams, rescaling, and RG semantics**
9. **Projective laws, thermodynamic limits, and continuum obligations**

### Part III — Multivariate-Gaussian Realization

10. **Linear-Gaussian joint and the interaction cone**
11. **Gaussian recognition restrictions and information geometry**
12. **Gaussian aggregation, Kron reduction, holonomy, and quotient closure**
13. **Gaussian RG: fixed rays, spectra, and numerical gates**

### Part IV — Boundaries, Evidence, and Interpretation

14. **Obstructions, admissible repairs, and theorem boundaries**
15. **Empirical commitments and interpretation**

Appendices:

- **A. Notation and type contracts**
- **B. Central claim and status ledger**
- **C. Numerical protocols and artifact provenance**
- **D. Long finite-dimensional witnesses** only if the journal format requires them out of the main line

This order gives the reader one progression:

\[
\text{typed objects}
\longrightarrow
\text{normalized laws}
\longrightarrow
\text{ELBO}
\longrightarrow
\text{coarse maps}
\longrightarrow
\text{scale comparison}
\longrightarrow
\text{Gaussian realization}
\longrightarrow
\text{dynamics and evidence}.
\]

## SPEC reconciliation

The current `SPEC.md` already states the correct ambient theory at `:9-13`, the required independent-bundle notation at `:113-131`, the general-to-Gaussian hierarchy at `:368-398`, and the centralized-ledger rule at `:92-98`. Those clauses should govern the rewrite; the manuscript source, not the SPEC, is lagging on those points.

Three SPEC repairs remain:

- At `SPEC.md:152-161`, relabel \(\Lambda^{(\ell+1)}=\zeta_\ell^{-1}S_\ell^\top\Lambda^{(\ell)}S_\ell\) as the **MVG operator component** of the scale diagram. Add the general state object, coarse arrows, comparison/rescaling maps, law/reference-measure rule, and autonomous/cocycle distinction before it.
- At `SPEC.md:163-166`, add semantic theorem/open-problem/claim label prefixes and require `\Cref`; chapter-number literals are not stable under the mandated reorder.
- At `SPEC.md:292-294`, replace `R15` by the semantic label for physical-law identification while retaining its `OPEN/INCONCLUSIVE` status and all listed obligations.

## Prioritized keep/move/merge/cut map

“Cut” below means removal from that location after preserving any unique content in the named canonical home. It never means deleting a theorem hypothesis or an unresolved obligation.

| Priority | Current location | Action | Canonical destination and reason |
|---:|---|---|---|
| 1 | `main.tex:53-73` | **REORDER** | Put `01_introduction` inside Part I; move general coarse-map and RG chapters before all Gaussian chapters; use the exact four-part order above. |
| 1 | `02_geometry.tex:1-43` | **REWRITE, KEEP** | Part I, Chapter 2. Replace the single principal bundle by independent belief/model principal gauge systems and their associated bundles. |
| 1 | `02_geometry.tex:44-140` | **REWRITE, KEEP** | Part I, Chapter 2. Replace “two representations of one group element” by the typed product action below. The principal-bundle map currently denoted `\Phi` at `:115-140` must not occupy the symbol reserved for the cross-associated-bundle morphism. |
| 2 | `02_geometry.tex:142-159` | **MOVE** | Part III, Chapter 10. These are Gaussian coordinates, not general geometry. |
| 2 | `02_geometry.tex:161-612` | **KEEP, SPLIT** | Keep general agents, bundle topology, gauge automorphisms, and smooth connection transport in Part I. Move any matrix-Gaussian specialization to Part III. Keep smooth parallel transport distinct from graph links. |
| 1 | `02_geometry.tex:613-677` | **MERGE/CUT** | Appendix B. Replace 65 source lines of chapter register by inline status tags and central ledger rows. |
| 2 | `03_probability.tex:1-296` | **KEEP** | Part I, Chapter 3. This is the general normalized probability layer. |
| 1 | `03_probability.tex:297-324` | **MERGE/CUT** | Appendix B. Remove the 28-line duplicate register. |
| 2 | `04_generative.tex:1-210` | **KEEP** | Part I, Chapter 3. Retain the fixed normalized joint and typed kernel construction. |
| 2 | `04_generative.tex:211-294` | **MOVE** | Part III, Chapter 10. This is the linear-Gaussian realization. |
| 1 | `04_generative.tex:295-436` | **SPLIT/REWRITE** | Put the abstract product-gauge pushforward theorem in Part I; put coordinate Gaussian formulas in Part III. The present same-\(g\) rule is only a diagonal/shared-frame specialization. |
| 1 | `04_generative.tex:437-462` | **MERGE/CUT** | Appendix B. Remove the 26-line duplicate register. |
| 2 | `05_elbo.tex:1-438` | **KEEP, TIGHTEN** | Part I, Chapter 4. State one exact ELBO against one fixed normalized joint; move family-specific examples to the corresponding realization chapter. |
| 1 | `05_elbo.tex:439-465` | **MERGE/CUT** | Appendix B. Remove the 27-line duplicate register. |
| 2 | `05a_expfamily.tex:1-244` | **KEEP** | Part I, Chapter 5. This is the general statistical-fiber and exponential-family layer. |
| 1 | `05a_expfamily.tex:245-363` | **MOVE, CANONICAL HOME** | Part II, Chapter 7. This becomes the single statement of graph-exponential identification, energy restriction, and coarse normalizer behavior. |
| 2 | `05a_expfamily.tex:365-386` | **SPLIT/CLOSE** | Put the finite quadratic quotient theorem in Part III, Chapter 12; keep only the genuinely open projective-law limit in Part II, Chapter 9. State the Jacobian and distinguish normalized laws from raw normalizers. |
| 2 | `05a_expfamily.tex:387-398` | **MOVE** | Part II, Chapters 8–9. This is a scale-program obligation, not part of the exponential-family definition. |
| 2 | `05a_expfamily.tex:400-460` | **MOVE** | Part III, Chapter 10. This is the Gaussian instance. |
| 1 | `05a_expfamily.tex:461-518` | **MERGE/CUT** | Appendix B. Remove the 58-line duplicate register. |
| 2 | `06_gaussian.tex:1-298` | **KEEP** | Part III, Chapter 10. Preserve the interaction cone and exact matrix conditions. |
| 1 | `06_gaussian.tex:299-343` | **KEEP, CANONICAL HOME** | Part III, Chapter 12. This is the single home for Kron reduction and its precise closure domain. At `:328-342`, replace the open “larger family” question by memo 09’s fixed-congruence-diagonal closure theorem and its qualified maximality result; retain correlated, nonconvex, variable-chart, and nonflat families as open. |
| 1 | `06_gaussian.tex:344-384` | **MERGE/CUT** | Appendix B. Remove the 41-line duplicate register. |
| 2 | `07_restrictions.tex:1-303` | **KEEP** | Part III, Chapter 11. Preserve recognition-family domains and optimized-gap qualifications. |
| 1 | `07_restrictions.tex:304-342` | **REPLACE/MOVE** | Replace Proposition 8.18 by the general normalized Markov-pushforward theorem in Part II, Chapter 6. Move the narrower “arbitrary separately declared models need not be ordered” boundary to Part IV. Do not retain “different inventory” as the criterion. |
| 1 | `07_restrictions.tex:344-382` | **MERGE/CUT** | Appendix B. Remove the 39-line duplicate register. |
| 2 | `08_infogeometry.tex:1-291` | **KEEP** | Part III, Chapter 11. Keep Fisher/Hessian results with their Gaussian and regularity domains. |
| 1 | `08_infogeometry.tex:292-320` | **MERGE/CUT** | Appendix B. Remove the 29-line duplicate register. |
| 1 | `09_coarsegraining.tex:1-95` | **MOVE, KEEP** | Part II, Chapters 6–7. Lead with the distinction among Markov pushforward, energy precomposition, and exact Gaussian marginalization. |
| 1 | `09_coarsegraining.tex:96-194` | **MERGE/CUT** | Merge unique corollaries into the canonical theorem at `05a_expfamily.tex:245-363`; replace this 99-line repetition by a short specialization pointer. |
| 2 | `09_coarsegraining.tex:195-205` | **KEEP/TIGHTEN** | Part II, Chapter 7. Retain only the affine-closure corollary not already proved in the canonical theorem. |
| 2 | `09_coarsegraining.tex:208-255` | **MERGE** | Part III, Chapter 12. State the interaction/flatness assumptions once, adjacent to the interaction cone in `06_gaussian.tex:90-147`; retain an eight-line dependency summary here. |
| 2 | `09_coarsegraining.tex:256-318` | **KEEP/MERGE** | Part III, Chapter 12. Keep aggregation-specific material; merge the repeated Kron statement with `06_gaussian.tex:299-343`. At `:303`, replace “of course symmetric” by the proved reason: “the full Schur complement is symmetric.” |
| 2 | `09_coarsegraining.tex:319-479` | **KEEP** | Part III, Chapter 12. This contains the unique nonflat witness, coarsenability condition, and cut criterion. |
| 1 | `09_coarsegraining.tex:480-570` | **REWRITE, KEEP** | Part III, Chapter 12. State the closed rectangular endpoint-map/cellular-sheaf category; leave only compression to one invertible link and the probability/RG lift open. |
| 2 | `09_coarsegraining.tex:571-670` | **KEEP, TIGHTEN** | Part III, Chapter 12. Separate frame agreement from closure selection; do not imply that exact closure selects a partition. |
| 1 | `09_coarsegraining.tex:671-707` | **MOVE/REPAIR** | Part II, Chapter 7. Positivity plus finite additivity on the PSD cone already forces the required linearity; do not make measurability the load-bearing hypothesis. |
| 2 | `09_coarsegraining.tex:708-791` | **MERGE/TIGHTEN** | Part III, Chapter 12. Keep the unique hard-identification divergence. Move the general affine Bregman projection theorem to Chapter 5 or 7 and close attainment under its stated Legendre/closed-affine/feasible hypotheses. |
| 1 | `09_coarsegraining.tex:792-821` | **REWRITE** | Part II, Chapters 6 and 8. Replace the blanket evidence-incomparability objection at `:797` by the Markov-channel/arbitrary-model boundary. |
| 2 | `09_coarsegraining.tex:823-855` | **KEEP** | Part II, Chapter 8, with an explicit permutation- and product-gauge-natural partition-selector obligation. |
| 1 | `09_coarsegraining.tex:857-874` | **MERGE/CUT** | Appendix B. Give each surviving open problem one row; remove repeated prose about the same coarse-link obstruction. |
| 1 | `09_coarsegraining.tex:875-943` | **MERGE/CUT** | Appendix B/C. Remove the 69-line duplicate register; retain seed, tolerance, and artifact identifiers once in Appendix C. |
| 2 | `10_renormalization.tex:1-53` | **KEEP/MOVE** | Part III, Chapter 13. These are MVG scope assumptions, not the definition of general RG. |
| 1 | `10_renormalization.tex:54-100` | **MERGE/CUT** | Replace the third copy of graph-exponential aggregation by an assumption-and-dependency box pointing to Part II, Chapter 7. |
| 1 | `10_renormalization.tex:102-180` | **REWRITE/MOVE** | Part II, Chapter 8. Define a typed scale category, coarse arrows, comparison/rescaling maps, reference-measure rule, and autonomous/periodic/cocycle branch before using “fixed point” or “basin.” |
| 2 | `10_renormalization.tex:181-268` | **KEEP** | Part III, Chapter 13. Preserve bi-additive closure and boundary-ray qualifications. |
| 1 | `10_renormalization.tex:269-392` | **KEEP/RENAME** | Part III, Chapter 13. Rename the aggregation operator `\Phi_S` at `:275-350` to `A_S`, `C_S`, or `\mathcal A_S`; `\Phi` is reserved for \(E_b\to E_m\). Preserve the full-cone no-go and autonomous scalarized conjecture. |
| 2 | `10_renormalization.tex:393-448` | **KEEP** | Part III, Chapter 13. This is the substantive numerical gate; move protocol metadata, not the results, to Appendix C. |
| 2 | `10_renormalization.tex:449-560` | **KEEP** | Part III, Chapter 13. Preserve regular-pencil and spectral-domain qualifiers. |
| 1 | `10_renormalization.tex:562-611` | **SPLIT/REWRITE** | Put the two-index thermodynamic/RG-limit obligations in Part II, Chapter 9; put empirical interpretation in Part IV. Replace raw running couplings by scheme-dependent diagnostics and invariant candidate observables. |
| 1 | `10_renormalization.tex:612-644` | **DISTRIBUTE/CUT** | Put each literature comparison at the theorem or definition it actually supports. Remove the end-loaded survey after those citations are placed locally. |
| 1 | `10_renormalization.tex:102-122`, `:643`, `:721` | **SPLIT/CLOSE** | Put the general “stochastic right section is not an inverse” result in Part II, Chapter 6. Put Wishart’s full-rank no-go, matrix-Gamma existence, and the congruence-diagonal Gamma/Dirichlet finite refinement theorem in Part III, Chapter 13. Leave graph-level priors and an infinite projective hierarchy open. |
| 1 | `10_renormalization.tex:645-724` | **MERGE/CUT** | Appendix B. Remove the 80-line status register. Replace `R15` at `:718` by a semantic label. |
| 1 | `10_renormalization.tex:725-763` | **MOVE/TIGHTEN** | Appendix C. Preserve reproducible numerical evidence once, keyed to claim labels and artifact hashes. |
| 2 | `11_obstructions.tex:1-341` | **KEEP/UPDATE** | Part IV, Chapter 14. Convert repaired conjectures to theorems where pass 2 closes them; title the holonomy statement by what it proves—transport dependence factors through holonomy—not “a function of holonomy alone.” |
| 1 | `11_obstructions.tex:342-388` | **MERGE/CUT** | Appendix B. Remove the 47-line duplicate register. |
| 2 | `12_philosophy.tex:1-132` | **KEEP/TIGHTEN** | Part IV, Chapter 15. Preserve the explicit distinction between mathematical constraint and empirical confirmation. |
| 1 | `12_philosophy.tex:133-171` | **MERGE/CUT** | Appendix B. Remove the 39-line duplicate register and replace `R15` at `:164` by a semantic label. |
| 1 | `01_introduction.tex:1-115` | **KEEP/REWRITE LAST** | Part I, Chapter 1. Rewrite only after the new architecture is stable; its job is to state the object, exact claims, and reading paths, not preview every audit row. |
| 1 | `01_introduction.tex:116-153` | **MERGE/CUT** | Appendix B. Remove the 38-line duplicate register and replace `R15` at `:150` by a semantic label. |

## Duplication clusters and their one canonical home

### 1. Status and audit registers

- **Repeated:** the endings of all thirteen chapters, from `01_introduction.tex:116-153` through `12_philosophy.tex:133-171`.
- **Canonical home:** Appendix B, with inline status tags at the actual statement.
- **Safe saving:** the 586 register lines plus the 39-line RG evidence block become approximately 120–180 centralized ledger/provenance lines, saving 445–505 source lines and approximately 25–27 rendered pages after allowing six to eight pages for Appendices B–C.

### 2. Graph-exponential identification and aggregation

- **Repeated:** `05a_expfamily.tex:245-363`, `09_coarsegraining.tex:96-194`, and `10_renormalization.tex:54-100`.
- **Canonical home:** Part II, Chapter 7, based on `05a_expfamily.tex:245-363`.
- **Safe saving:** replace the later copies by a 12-line Gaussian specialization and an 8-line RG dependency box; approximately 125–140 source lines and five to six rendered pages.

### 3. Kron reduction

- **Repeated:** `06_gaussian.tex:299-343` and `09_coarsegraining.tex:281-318`.
- **Canonical home:** Part III, Chapter 12, retaining the exact closure domain, counterexample, and the pass-2 congruence-diagonal positive theorem together.
- **Safe saving:** 30–35 source lines and approximately one to one-and-a-half pages.

The integrated section should strengthen, not merely compress, the result. A fixed cone
\(\mathcal C_H=\{HDH^\top:D\succeq0\text{ diagonal}\}\) is closed under every defined node-block Schur elimination. This strictly extends the common-orthogonal-eigenbasis family because congruence-diagonal matrices need not commute. The maximality statement must retain memo 09’s richness, independence, convexity, SPD-order-unit, and one-node-elimination assumptions.

### 4. Interaction and flatness assumptions

- **Repeated:** the interaction-cone definitions near `06_gaussian.tex:90-147` and the coarse chapter’s restatement at `09_coarsegraining.tex:208-255`.
- **Canonical home:** Part III, Chapter 10 for the cone; Chapter 12 receives only an explicit dependency box.
- **Safe saving:** approximately 35–40 source lines and one-and-a-half pages.

### 5. Variational restriction costs

- **Repeated or separated from their general theorem:** `07_restrictions.tex:58-262` and `09_coarsegraining.tex:708-791`, with the affine Bregman issue also at `05a_expfamily.tex:368-385`.
- **Canonical home:** the general affine Bregman projection theorem in Part I, Chapter 5; Gaussian and hard-identification corollaries in Part III, Chapters 11–12.
- **Safe saving:** approximately 45–55 source lines and two pages.

### 6. Coarse-link and holonomy obstruction

- **Repeated:** `09_coarsegraining.tex:566-569`, `:857-873`; `10_renormalization.tex:34-45`, `:639-643`; `11_obstructions.tex:335-336`.
- **Canonical home:** the rectangular endpoint-map/cellular-sheaf closure theorem in Part III, Chapter 12, followed by one open problem for invertible-link compression and probability/RG lifting.
- **Safe saving:** approximately 25–30 source lines and one page.

### 7. Infinite divisibility and stochastic refinement

- **Repeated or left as an undifferentiated open question:** `10_renormalization.tex:102-122`, `:643`, and `:721`, with inverse language also discussed in the network-RG comparison.
- **Canonical homes:** the general noninvertibility/right-section distinction in Part II, Chapter 6; matrix-valued constructions in Part III, Chapter 13.
- **Required result split:** full-rank central Wishart is not infinitely divisible; matrix-Gamma laws exist on \(\PSD^K\); on a fixed congruence-diagonal cone, channelwise Gamma addition and Dirichlet bridges give an exact finite-hierarchy stochastic right section. Internal edges require a declared prior. An infinite graph/projective-limit RG remains open.

### 8. Different-inventory/evidence claim

- **Repeated:** `07_restrictions.tex:304-342` and `09_coarsegraining.tex:792-821`.
- **Canonical home:** the normalized Markov coarse-map theorem in Part II, Chapter 6; the arbitrary-model nonordering caveat in Part IV, Chapter 14.
- **Repair, not merely a cut:** exact marginalization at `09_coarsegraining.tex:42-81` is already a counterexample to the blanket formulation.

### 9. “Physical law” audit label

- **Repeated:** `01_introduction.tex:150`, `10_renormalization.tex:718`, `12_philosophy.tex:164`, and `SPEC.md:277`.
- **Canonical home:** one semantic claim row in Appendix B, referenced by label from the introduction and interpretation chapter.
- **Safe saving:** small in lines but large in editorial clarity; remove the revision-bound token `R15`.

## Corrected notation and type contract

The following box should appear in Part I, Chapter 2 and be reproduced compactly in Appendix A.

Let

\[
P_b\to C,\qquad P_m\to C
\]

be independent principal gauge systems with structure groups \(G_b\) and \(G_m\), representations \(\rho_b,\rho_m\), and associated bundles

\[
E_b=P_b\times_{\rho_b}V_b,\qquad
E_m=P_m\times_{\rho_m}V_m.
\]

The principal bundles supply the group actions and connections. The cross-channel maps are **associated-bundle morphisms covering \(\operatorname{id}_C\)**:

\[
\Phi:E_b\to E_m,\qquad
\widetilde\Phi:E_m\to E_b.
\]

They are not principal-bundle morphisms, are not assumed inverse, and are not assumed connection-parallel.

Use separate product-gauge automorphisms

\[
U^b:E_b\to E_b,\qquad U^m:E_m\to E_m
\]

or local symbols \(g_i^b,g_i^m\). Their action is

\[
\Phi_i' = U_i^m\Phi_i(U_i^b)^{-1},\qquad
\widetilde\Phi_i' = U_i^b\widetilde\Phi_i(U_i^m)^{-1}.
\]

Reserve connection-induced same-channel parallel transports for

\[
\Omega_{ij}:E_{b,j}\to E_{b,i},\qquad
\widetilde\Omega_{ij}:E_{m,j}\to E_{m,i},
\]

with

\[
\Omega_{ij}'=U_i^b\Omega_{ij}(U_j^b)^{-1},\qquad
\widetilde\Omega_{ij}'=U_i^m\widetilde\Omega_{ij}(U_j^m)^{-1}.
\]

Connection parallelity of the cross maps is an optional theorem hypothesis,

\[
\widetilde\Omega_{ij}\Phi_j=\Phi_i\Omega_{ij},\qquad
\Omega_{ij}\widetilde\Phi_j=\widetilde\Phi_i\widetilde\Omega_{ij},
\]

not a definition. Without it, retain the corresponding covariant defects rather than declaring the expressions ill typed.

Graph-edge links are a third object. Denote them, for example,

\[
\Theta^b_{ij}:E_{b,j}\to E_{b,i},\qquad
\Theta^m_{ij}:E_{m,j}\to E_{m,i}.
\]

They may be compared with \(\Omega,\widetilde\Omega\) only after a curve assignment and a link-to-parallel-transport rule. Do not use the connection symbols for arbitrary graph links.

Two immediate collision repairs follow:

- rename the principal-bundle map currently called `\Phi` in `02_geometry.tex:115-140`; if a principal morphism remains necessary, use a symbol such as \(F_P\);
- rename the aggregation map `\Phi_S` in `10_renormalization.tex:275-350` to \(A_S\), \(C_S\), or \(\mathcal A_S\).

The current same-\(g\) diagonal action at `02_geometry.tex:106-140` and `04_generative.tex:295-436` may remain only as an explicitly labeled shared-frame/MVG specialization. It cannot define the general theory.

## Hard-coded result-number repair

Manual result names are already out of semantic and numerical order. For example, `10_renormalization.tex:186-386` runs from Proposition 11.4 to Proposition 11.16, Open Problem 11.17, Open Problem 11.5, Proposition 11.6, Proposition 11.22, Proposition 11.23, Open Problem 11.7, and Conjecture 11.8. Later, `:458-587` returns to Proposition 11.9 and then jumps among 11.18–11.21 and 11.10–11.15. Reordering the book while retaining these literals will make the cross-references unmaintainable.

Repair:

1. define real theorem environments sharing one chapter-scoped counter;
2. give every theorem, proposition, definition, conjecture, and open problem a semantic `\label`;
3. cite with `\cref`/`\Cref`, never literal “Proposition 11.6” in prose;
4. use a distinct semantic claim ID in Appendix B, such as `claim:physical-law-identification`, rather than `R15`;
5. keep numerical protocol IDs such as `CHK-RG-*` in Appendix C, not in theorem numbering;
6. generate one migration table from old displayed number to new semantic label during revision, then remove that table before submission.

This is a mechanical repair, but theorem names and statuses must be migrated before any content is moved so that no qualifier is lost.

## Centralized status-ledger design

The present seven manuscript statuses can remain, but they should not be copied into thirteen chapter tables. Use one longtable in Appendix B:

| Claim ID | Semantic label | Layer/domain | Hypotheses | Manuscript status | Closure evidence | Open obligation | Artifact/revision |
|---|---|---|---|---|---|---|---|

Rules:

- one row per nontrivial claim, not one row per paragraph;
- theorem statements retain a short inline `\status{...}` marker;
- “Layer/domain” must distinguish general probability, general coarse map, exponential family, MVG, graph, and interpretation;
- “Hypotheses” contains the shortest lossless domain statement and points to the theorem;
- “Closure evidence” points to a proof, counterexample, primary citation, or reproducible artifact;
- “Open obligation” is blank for closed claims and concrete for every open claim;
- “Artifact/revision” prevents numerical evidence from floating free of its seed, input, code revision, and hash;
- verification closure (`EVIDENCE_VERIFIED`, `REFUTED`, or `INCONCLUSIVE`) is a separate column or companion field and must not be confused with the manuscript’s epistemic status.

Appendix C should contain a second compact table keyed by the same claim ID:

| Protocol ID | Claim ID | Seed/input | Control | Metric/tolerance | Artifact hash |
|---|---|---|---|---|---|

The body then says only what the numerical result shows and what it does not show. It does not repeat seeds, protocol prose, and status rows in three places.

## Citation-placement repairs

1. **Markov coarse maps:** place the data-processing and equality/recovery citations at the new theorem in Part II, Chapter 6. The theorem must distinguish deterministic statistics, general kernels, equality/recovery, and arbitrary model replacement.
2. **Affine Bregman projection:** at `05a_expfamily.tex:368-385` and `09_coarsegraining.tex:750-768`, cite the convex-duality/exponential-family result at the theorem that closes existence and uniqueness under Legendre, closed-affine, and feasible-interior hypotheses. Do not leave those sources in a later survey paragraph.
3. **Galerkin and Kron reduction:** place algebraic-multigrid and matrix-weighted Laplacian citations at the first definition/theorem of \(S^\top\Lambda S\), currently near `09_coarsegraining.tex:256-318`; place the scalar Kron citation next to the positive scalar theorem and the matrix counterexample next to its exact domain.
4. **Rectangular coarse links:** cite cellular-sheaf/endpoint-map literature where the closed rectangular category is introduced, replacing the repeated open-problem tails at `09_coarsegraining.tex:566-569`, `:857-873`, `10_renormalization.tex:34-45`, and `11_obstructions.tex:335-336`.
5. **Bayesian RG:** repair `10_renormalization.tex:619-625` by citing each actual step—centered-KL posterior flow, late-time Gaussian approximation, inverse problem, posterior predictive, and Fisher-cometric pushforward—at the sentence that uses it. Do not identify the Fisher metric itself with a diffusion tensor and do not transfer “stiff/sloppy” directions to the manuscript’s self/coupling sectors without a bridge theorem.
6. **Laplacian RG:** at `10_renormalization.tex:629-633`, cite the heat-kernel definition next to the scalar construction, call its real-space blocker heuristic, and use \(C=-dS/d\log\tau\). The generalized spectrum is gauge invariant; an entrywise heat-kernel blocker still requires a gauge-invariant replacement.
7. **Network RG:** at `10_renormalization.tex:635-643`, cite the independent-edge result for exact additive hidden-variable closure and stochastic refinement in distribution. Cite the interacting-network extension where interaction closure is discussed. Do not call refinement a two-sided inverse.
8. **Matrix infinite divisibility:** at the revised finite-refinement theorem replacing the broad question at `10_renormalization.tex:643`, cite Mayerhofer for the rank-one-only central Wishart result and Pérez-Abreu–Stelzer for matrix-Gamma convolution semigroups. Keep the finite Gamma/Dirichlet bridge proof adjacent to the theorem and the projective-limit obligation adjacent to the open problem.
9. **Graph ML:** place the Mehta–Schwab comparison after the general RG definition and state the trace-condition scope. Do not relabel exact Galerkin restriction as message passing or a GNN.
10. **Interpretation:** retain the philosophy citations near the claims they constrain; do not repeat them in the central ledger. The ledger points back to the labeled statement.

## Rigor and flow repairs

- State types before formulas. Every coarse arrow should display its domain, codomain, measure rule, and whether it is a kernel, energy precomposition, parameter aggregation, or scale identification.
- State the general theorem once, then give an MVG corollary. Do not infer a general probability theorem from a Gaussian matrix identity.
- Keep two limits visible: system size \(n\) and RG depth \(\ell\). Use \(X_{n,\ell}\) before claiming an infinite-volume fixed object or spectral exponent.
- Reserve “fixed point” and “fixed ray” for an endomorphism or a declared monodromy. For a nonautonomous scheme use “cocycle,” “invariant section,” or “attracting cycle.”
- Distinguish scheme-dependent running coordinates from candidate invariant observables such as projective eigenvalue ratios, block-normalized scaling dimensions, and matched IDS/heat exponents.
- Replace the blanket “posterior excluded implies positive optimized gap” by the correct attained/nonattained distinction; a family can exclude the posterior while having KL infimum zero.
- Replace “different latent inventories imply different incomparable evidences” by the exact boundary: a normalized Markov pushforward preserves evidence and contracts KL; arbitrary separately declared models need not share evidence or an order.
- Close the finite-dimensional quotient/aggregation statement at the normalized-law level and retain the Jacobian for raw normalizers. Keep the projective continuum law open.
- Close the fixed-congruence-diagonal Kron family under its exact hypotheses. Do not weaken it back to common orthogonal diagonalization, and do not promote its qualified maximality beyond rich independently parameterized convex cones with an SPD order unit.
- Narrow infinite-divisibility language: stochastic refinement is a prior-dependent right section, not recovery. Separate finite hierarchy, graph-level prior, and infinite projective-limit claims.
- In Appendix C, relabel `CHK-GAUSS-CONDITIONING` as descriptive unless its executable `PASS` predicate acquires a justified condition-number statistic and threshold; positivity alone does not test conditioning.
- Replace `09_coarsegraining.tex:303`’s “of course symmetric” with its one-line proof. The rigor sweep found 702 lexical candidates across generated and source artifacts, but that count is not a defect count; only load-bearing instances should be edited.
- Preserve every theorem domain in headings and summaries. In particular, retain “regular pencil,” “scalarized coupling cone,” “hierarchical family,” “finite-dimensional quadratic quotient,” “hard partition,” and “fixed graph” wherever those are hypotheses.

## Physicist reading path

The revised introduction should offer a named fast path that can be read without the measure-theoretic proofs:

1. Chapter 1: the claims map and one-page object diagram.
2. Chapter 2: the independent \(E_b/E_m\) type-contract box and product-gauge transformation laws.
3. Chapters 3–4: the normalized joint and exact ELBO identities only.
4. Chapters 6–8: the three-operation distinction, Markov coarse theorem, graph-exponential closure, and typed RG diagram.
5. Chapters 10 and 12: the MVG interaction cone, Gaussian aggregation, congruence-diagonal Kron closure, holonomy closure map, and exact counterexample.
6. Chapter 13: the positive-cone dynamics, fixed-ray qualifications, generalized spectrum, finite stochastic-refinement boundary, and numerical gate.
7. Chapters 14–15: one obstruction table and the empirical commitments.

Detailed bundle transitions, disintegration proofs, convex-duality proofs, exact rational witnesses, ledger rows, and protocol metadata can be skipped on first reading and recovered through semantic cross-references. With the cuts above, this route should occupy approximately 45–60 body pages even if the full monograph remains approximately 213–218 pages.

## Quantified safe-cut budget

| Cut cluster | Current extent | Replacement | Safe net saving |
|---|---:|---:|---:|
| Thirteen status registers plus the RG evidence block | 586 + 39 = 625 source lines; approximately 33 pages | 120–180 lines; 6–8 pages | 445–505 lines; 25–27 pages |
| Triple aggregation theorem | approximately 266 lines across three locations | one canonical theorem plus 20 lines of pointers | 125–140 lines; 5–6 pages |
| Kron duplication | approximately 83 lines across two locations | one integrated theorem/counterexample section | 30–35 lines; 1–1.5 pages |
| Repeated interaction/flatness assumptions | approximately 106 lines across two locations | one definition plus dependency box | 35–40 lines; approximately 1.5 pages |
| Repeated restriction/Bregman treatment | dispersed across approximately 285 lines | one general theorem plus two short corollaries | 45–55 lines; approximately 2 pages |
| Repeated coarse-link/open-problem prose | approximately 35–45 lines | one theorem and one open row | 25–30 lines; approximately 1 page |
| End-loaded literature survey and repeated transitions outside the 625-line block | approximately 50–75 lines | point-of-use citations plus short cross-references | 25–40 lines; 1.5–3 pages |
| **Conservative total** |  |  | **730–845 lines; 37–42 pages** |

Assumptions behind the page estimate:

- the bibliography and front matter are unchanged;
- all unique proofs, witnesses, theorem hypotheses, and numerical result tables are retained;
- the central ledger occupies four to six pages and the tightened numerical-provenance appendix two pages;
- the paragraph-level source-line count is only a secondary measure because longtable rows render disproportionately;
- final page closure requires a fresh compile and page-by-page comparison, so 213–218 pages is a target interval, not a verified final count.

## Revision sequence

1. Introduce theorem environments and semantic labels before moving text.
2. Establish the two-bundle/product-gauge notation and rename both `\Phi` collisions.
3. Move the general coarse-map/RG material ahead of the MVG realization.
4. Merge the three aggregation statements and the two Kron statements.
5. Repair the evidence-comparison theorem and typed RG definition.
6. Centralize status and numerical provenance.
7. Rewrite the introduction, transitions, and philosophy chapter against the finished architecture.
8. Recompile, validate every cross-reference, compare theorem/status counts, and recount pages.

This sequence preserves the theorem graph while removing the manuscript’s audit-history scaffolding from the reader’s main path.
