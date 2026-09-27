# Editorial, notation, cross-reference, citation, and layout review: GL(K) v2 pair

**Lens:** editorial / notation / cross-reference / citation / layout. **Reviewer model:** Claude Opus 5.5 (author-side generator for this lens; no verifier role is claimed here). **Date:** 2026-09-23.

**Inputs (hash-checked, byte-identical to the brief):** main `GL(K)_attention_v2.tex` sha256 85b3918c...8f3f; supplement `GL(K)_supplementary_v2.tex` sha256 69607aed...4e44; `references.bib` sha256 6bc44049...97d9; `jmlr2e.sty` sha256 4a167d21...9462 (see `editorial_evidence/input_hashes.txt`). Nothing in the Research folder was written. All builds ran in `scratchpad/panel/build/` (faithful copy) and `scratchpad/panel/build_exp/` (a deliberately modified copy used only to test layout remedies).

**What was executed:** pdflatex/bibtex (TeX Live 2025) four passes per document with mutual `xr` resolution; page rendering at 60 and 150 dpi with visual inspection of every page; scripted extraction of all labels/references/citations (`labels.py`), all math-mode glyphs with their sub/superscripts and line numbers (`symbols.py`), display-equation terminal punctuation (`displaypunct.py`), per-section word/display counts (`wordcount.py`), sentence-level negation counts (`negations.py`), and mapping of underfull output pages (`underfull_pages.py`). Outputs are saved in `scratchpad/panel/editorial_evidence/`. Citation checks used the primary PDFs from arXiv, NeurIPS proceedings, IEEE Xplore (open access), Crossref metadata, the Matrix Cookbook, Boyd and Vandenberghe, and a hosted copy of Culver (1966); each check is listed in the citation section with its outcome. No Lean, no GPU, no tamper tests.

**Build result (confirms the prior review's compile facts):** main 31 pages, supplement 4 pages; no undefined references or citations; no multiply defined labels; no overfull boxes. Warnings: one `caption` package warning per document; five `Underfull \vbox ... while \output is active` in the main (pages 2, 3, 9, 24, 25); underfull `\hbox` in the main at source lines 989-990, 1005-1008, 1088 and in three bibliography entries.

Line numbers below are main-text lines unless prefixed `Supp`. Equation numbers are those of the compiled PDF.

## Ranked findings (one line each)

| ID | Severity | Finding | Prior review |
|---|---|---|---|
| E1 | high | `a`/`z`/`b` collide inside the core operator: head aggregate `a_i^(l,h)` (Sec 3.1, Alg 1) vs projected query mean `a_i` (Sec 4) vs ALiBi slope `a_h` (Alg 1); the same aggregate is renamed `z_i^(h)` in Eq (87); `z_i` is also the decoder logit; `b_j` key mean vs `b_ij^(h)` logit bias vs LayerNorm `b` vs MLP `b_1,b_2` vs counterexample keys `b_1,b_2` | new |
| E2 | high | Table 1 symbol `p_i` (local prior) is redefined as the local joint `p_i(j,y,z)` in Eq (71)-(73), which the supplement then cites; the same joint is `P_i` in Eq (44), colliding with the key precision `P_j` of Eq (81); recognition law is `Q_{i,beta}` in Eq (45) but `q_{i,beta}` in Eq (72) | new |
| E3 | medium | Section 2.8 inverts the paper's own roles: `pi_v` are Gaussian templates and `omega` the categorical prior, while elsewhere `pi` is the categorical prior; `pi_0, pi_1` in the worked example read as prior rows; `rho_i` (readout) reuses the representation `rho` | new |
| E4 | medium | `B_ij` is reused at line 594 for "endpoint-covariant edge matrices" in the loop product, 55 lines after `B_ij` was defined as the comparison tensor `E_j -> E_i^*`, for which products are not even type-correct | new |
| E5 | medium | 2.6.1 is a legacy block (imported from PIFB2.tex:596) with a stray period in Eq (51), five spurious indented paragraphs after displays, straight quotes, colons before displays, bare equation references, first-person generative language, and an internal contradiction ("unified derivation", "arises from" vs "rather than derived from first principles") | new |
| E6 | medium | Figure 2 is cited only from Figure 1's caption; Tables 2 and 3 and Lemma 1 are never cited; Proposition 2 has no label and is called a "theorem" three times | new |
| E7 | medium | Second-tier collisions across sections and across documents (gamma, epsilon_i, R/R_i/Q_i, H(q), X, S_i, r_j, E_12, block superscript (b), a basis-change vs a test vector, tau_i, LN naming, Tr/tr, log det vs log|.|, five meanings of an overbar) | new |
| E8 | medium | Standard citations missing for the experiment's own components: WikiText-103 (merity2017pointer is in the bib, unused), GELU (hendrycks2016gaussian in bib, unused), LayerNorm in the main text (ba2016layernorm cited only in the supplement), AdamW (absent from the bib) | new |
| E9 | medium | The latent-source/positional-prior construction (2.6, 2.6.1, Supp A) is presented without attribution to direct precedents already partly in the bib (Singh and Buckley 2023a geometric prior over adjacency; Deng et al. 2018 latent alignment) or verified L8 precedents (Niculae and Blondel 2017; Movellan and Gabbur 2020; Kim, Papamakarios, Mnih 2021) | extends R7 |
| E10 | medium | Document-level organization: Section 2 occupies pp. 3-17 with 52 of 70 display environments; three scope disclaimers recur five or six times each; the Gibbs lemma is derived four times; the three formal environments are not the central results | extends R2 |
| E11 | low | Wrong or imprecise internal pointers (l.879 -> 4.1 should be 4.2; l.660 passive action "of Section 2.4" is defined in 2.2; l.535/891 "Eq (18)" for objects in (16)-(17); roadmap cites "Section 5.2" because Section 5 has no label; "Appendix B" where B.2 is meant) | new |
| E12 | low | Label hygiene: 6 objects carry two labels; 12 legacy or misleading label names; 79 of 118 labels unused; 4 cross-document references depend on `xr` | new |
| E13 | low | Undefined acronyms, code names, and figure notation (VFE, ELBO, MLP, GELU, RoPE, ALiBi before expansion, HeadMixer, E-step, "prior-anchored natural-gradient update", "cognitive gauge frame", Figure 1's `G_K`) | new |
| E14 | low | Symbols used before definition or defined only inside a floating table (a_i, b_j at l.681; beta, pi, tau in Figures 1-2 and Table 1; A_{Q,i,h}, sans-serif S and R, G_i, Theta defined only in Table 1); Table 1 carries `tab:notation` but covers ~25 symbols | new |
| E15 | low | Heading capitalization (9 Title Case vs 18 sentence case subsection-level headings) and display punctuation (Eq (5) lacks its period) | new |
| E16 | low | Citation pinpoint error: Fuchs et al. "Sec. 2.3" does not contain invariant attention with equivariant values (that is Sec. 3.2, Eqs. 10-11); other load-bearing pinpoints verified; several pinpoints worth adding | new |
| E17 | low | Bibliography entry errors: Sengupta and Friston 2017 prints no identifier; "Mistral 7b"; ALiBi as @article; Blei missing issue 518; Nakahara missing edition; RoFormer author order differs from the journal record; missing NeurIPS pages; mixed initials/full names | new |
| E18 | low | Float/package layout: [H] figure/table and two \FloatBarrier produce stretched pages; unused `subcaption` causes the caption warning and replaces JMLR captions (tested); dead `\graphicspath` with two missing directories; ordinary float options alone do not fix pagination (tested) | extends C6, partly disagrees |
| E19 | low | Code-availability URL is invisible (white-border link, URL not printed), with no commit, tag, or archive identifier; four cross-PDF `GoToR` links depend on file names | new |
| E20 | low | Packaging: arXiv rejects the parentheses in `GL(K)_...` file names (verified on arXiv's help page); JMLR counts appendices toward length and describes online appendices as data/code, so merging the 3-page supplement as appendices removes the `xr` dependency | extends C8 |
| E21 | low | JMLR template usage: keywords environment, `\acks` (Acknowledgments and Disclosure of Funding), Code Availability as a subsection of the Conclusion, trailing "Supplementary Material" paragraph, supplement running head, preprint CC-BY footer, empty PDF metadata, keyword choice | new |
| E22 | low | Terminology drift for single objects (Omega_ij has five names; T and S_Q have four each; "processing defect" vs "composition defect"; "channel" in three senses; "link field(s)" undefined) | new |
| E23 | low | Index conventions verified consistent (receiver first, `ij` maps j to i, transposes, contragredient laws, row/column dictionary), with three presentational exceptions | new |

## Findings

### E1. Core-operator glyph collisions among `a`, `z`, and `b`

**Location:** Eq (68)-(69) at 884-885; Eq (80) at 973; Eq (87) at 1045; Algorithm 1 steps 2, 7, 8, 10, 14 at 1109, 1114, 1115, 1117, 1121; line 681; line 1020; Eq (76)-(77) at 930-934.

**Severity:** high

**Evidence:** Scripted glyph extraction (`editorial_evidence/symbols_by_glyph.txt`) and the compiled PDF (pp. 17-24). The head aggregate is defined as `a_i^{(\ell,h)}=\sum_j\beta_{ij}^{(\ell,h)}v_j^{(\ell,h)}` (Eq 68, p. 18; Algorithm 1 step 8, p. 24). Section 4.1 then states "suppress the layer and head indices" (l.971) and defines `a_i=S_Q\xi_i` (Eq 80, p. 20). After the announced suppression, the two definitions are the identical string `a_i` for objects in different spaces (`H_h^{val}=\mathbb R^{s_h}` versus `H_h^{cmp}=\mathbb R^{r_h}`). Algorithm 1 uses `a_h` for the ALiBi slope (step 2) six lines above `a_i^{(\ell,h)}` (step 8). The same aggregate reappears as `z_i^{(h)}` in Eq (87) (p. 22), so one object has two names; Algorithm 1 step 14 then uses `z_i` for decoder logits. For `b`: `b_j=S_K\xi_j` (Eq 80), `b_{ij}^{(h)}` the ALiBi logit bias (Alg 1 steps 2 and 7), `b` the LayerNorm shift (Eq 76, Alg 1 step 11), `b_1^{(\ell)},b_2^{(\ell)}` MLP biases (Eq 77), and "keys `b_1=0,b_2=1`" in the counterexample (l.1020). Line 681 (Sec 2.5) already writes `\|a_i-b_j\|^2/(2\sigma_h^2)`, 290 lines before `a_i,b_j` are defined.

**Fix:** (i) Rename the head aggregate to `z_i^{(\ell,h)}` in Eq (68)-(69) and Algorithm 1 steps 8 and 10, so Eq (87) and Section 3.1 agree. (ii) Rename the ALiBi slope to `\alpha_h` in Eq (54)-(55), line 775, and Algorithm 1 (the glyph alpha is unused in both documents), with "(the slope $m$ of \citet{press2022train})" once. (iii) In Algorithm 1, set the prior directly, which removes `b_{ij}^{(h)}` and aligns the algorithm with Eq (66): "Set $\pi_{ij}^{(h)}\propto e^{-\alpha_h(i-j)}$ for $j\le i$ and $\pi_{ij}^{(h)}=0$ otherwise" and step 7 "$\beta_{ij}^{(\ell,h)}=\operatorname{softmax}_j(\log\pi_{ij}^{(h)}-\bar D_{ij}^{(\ell,h)}/\tau_h)$". (iv) Drop the name `z_i` for decoder logits in step 14 by writing `p(y_i\mid x_{\le i})=\operatorname{softmax}(W_{\mathrm{out}}\mu_i^{(L)}+b_{\mathrm{out}}+\kappa_{\mathrm{uni}}\log p_{\mathrm{uni}})_{y_i}`. (v) At line 681 write `\|S_Q\xi_i-S_K\xi_j\|^2/(2\sigma_h^2)`. (vi) Rename the counterexample keys at l.1020 to `b_{(1)}=0,b_{(2)}=1` or state them as "key means 0 and 1".

**Falsifies:** The collision would be harmless only if `a_i` in Section 3.1 and in Section 4 were the same object; they are not: one is a `\beta`-weighted sum over sources in `H_h^{val}`, the other is the receiver's own projection `S_Q\xi_i` in `H_h^{cmp}`.

**Status:** Presentation only; no mathematical claim changes. The collision can make Algorithm 1, the paper's only complete statement of the operator, misread.

**Novelty vs prior review:** new

### E2. Joint laws, priors, and precisions share `P/p` and `Q/q`, and a Table 1 symbol is redefined

**Location:** Table 1 row "`q_i,p_i`: Full Gaussian state and local prior" (l.422); Eq (9) at 323; Eq (44)-(47) at 690-700; Eq (71)-(73) at 893-897; Eq (81) at 979-982; Eq (38) at 624; Supp 76.

**Severity:** high

**Evidence:** Eq (9) defines `p_i=\mathcal N(\mu_{p,i},\Sigma_{p,i})`, the local prior, and Table 1 fixes that meaning. Eq (71) defines `p_i(j,y,z)=\pi_{ij}p_{K,j}(y)r_j(z)`, a joint over label, comparison variable, and content variable, and Eq (73) is `D_{KL}(q_{i,\beta}\|p_i)`; the supplement (Supp 76) cites exactly this equation. Eq (44) names the analogous joint `P_i(y,J=j)`; Eq (81) names the projected key precision `P_j=V_{K,j}^{-1}` and line 537 the ambient version `P_{K,j}`. The recognition law is `Q_{i,\beta}` in Eq (45) and `q_{i,\beta}` in Eq (72); `Q_i` is the channel noise covariance in Eq (38).

**Fix:** Use blackboard letters for the two local joint laws in both places: `\mathbb P_i(y,J=j)`, `\mathbb Q_{i,\beta}(y,J=j)` in Eq (44)-(47), and `\mathbb P_i(j,y,z)`, `\mathbb Q_{i,\beta}(j,y,z)` in Eq (71)-(73). `P_j` then means only the key precision, `p_i` only the local prior, and `Q_i` only the channel covariance (or rename that to `\Lambda_i`, E7).

**Falsifies:** If the local prior `p_i` of Eq (9) were meant to be the `(y,z)`-marginal of the joint in Eq (71), the reuse would be intentional; it is not (Eq 9 is a law on `E_i`; Eq 71 is a law on `S_i\times H_h^{cmp}\times H_h^{val}`).

**Status:** Presentation only. The supplement's pointer to Eq (73) inherits the ambiguity.

**Novelty vs prior review:** new

### E3. Section 2.8 inverts the roles of `pi` and `omega`, and `rho` has two unrelated meanings

**Location:** 812-857 (Eq 59-64); Eq (2) at 281; Eq (40) at 646.

**Severity:** medium

**Evidence:** In Section 2.8 `\pi_v` is "a normalized class template on the same latent space" (a Gaussian density, `\pi_v=\mathcal N(\mu_{p,v},\Sigma_{p,v})`, l.832) and `\omega` is "a class prior" (l.819). Everywhere else `\pi_{ij}` is the categorical prior and the Gaussian laws are `q`/`p`. The worked example writes "templates `\pi_0=\mathcal N(0,1)`, `\pi_1=\mathcal N(2,1)`" (l.850), which is typographically the prior row `\pi_i` of receivers 0 and 1. The readout is `\rho_i`, `\rho_{iv}` (l.812-821) while `\rho` is the Gaussian action in Eq (2) and the defining representation in Eq (40) (itself two different maps: on `\mathcal B` and on `\mathsf V`). The template means carry the prior-bank subscript `p` (`\mu_{p,v}`), so the template is the prior-bank Gaussian of Section 2.7, which Section 2.7 writes `p_c=\mathcal N(\mu_p^c,\Sigma_p^c)` with a superscript index.

**Fix:** Write the templates as the prior-bank laws `p_v=\mathcal N(\mu_{p,v},\Sigma_{p,v})` (and `p_0,p_1` in the example), change Section 2.7 to the same subscript form with token index `v` (not `c`), and write the readout as `\hat p_i(v)`, which then contrasts directly with the posterior-predictive `\bar p_i(v)` in Eq (64). Keep `\omega` for the class prior. If Section 2.8 moves to the supplement (R2), apply the same renaming there.

**Falsifies:** None expected; this is a direct text comparison.

**Status:** Presentation only (the decoder is not used in the experiment, l.857).

**Novelty vs prior review:** new

### E4. The loop product reuses `B_ij` for a different, composable object

**Location:** line 594, Eq (33)-(35) at 595-600; Eq (25) at 539-540.

**Severity:** medium

**Evidence:** Eq (25) defines `B_{ij}=A_{Q,i}^\top P_{K,j}A_{K,j}` with law `B_{ij}'=g_i^{-\top}B_{ij}g_j^{-1}`, "It maps `E_j` to `E_i^*`" (l.543). Line 594 then says "For a declared closed walk ... and endpoint-covariant edge matrices `B_{ij}`, define `\mathcal H_\gamma(B)=B_{i_0i_1}\cdots`". A reader who applies Eq (33) to the `B_{ij}` just defined forms `B_{i_0i_1}B_{i_1i_2}` with `B_{i_1i_2}:E_{i_2}\to E_{i_1}^*` feeding `B_{i_0i_1}`, whose domain is `E_{i_1}`; the product is not type-correct and Eq (34) does not hold. The paper's own generic link symbol is `L_{ij}:E_j\to E_i` (l.335, Supp B.1).

**Fix:** Replace `B` by `L` in line 594 and Eq (33)-(35): "endpoint-covariant links `L_{ij}:E_j\to E_i`, define `\mathcal H_\gamma(L)=L_{i_0i_1}\cdots L_{i_{r-1}i_0}` and `\mathcal W_\gamma(L)=\operatorname{Tr}\mathcal H_\gamma(L)`". Add one clause fixing orientation: with the `ij`-means-`j\to i` convention this product transports around `\gamma` read right to left (from `i_0` to `i_{r-1}`, ..., to `i_1`, back to `i_0`); for the trace this is immaterial, for `\mathcal H_\gamma` it fixes which loop is meant.

**Falsifies:** If `\mathcal H_\gamma` were only ever evaluated on content or routed links, no reader error would follow; the defect is the stated generality "endpoint-covariant edge matrices `B_{ij}`" immediately after a non-composable `B_{ij}`.

**Status:** Presentation; the trace-invariance claim (derived) is unaffected for genuine links.

**Novelty vs prior review:** new

### E5. Section 2.6.1 is a legacy block with typographic and logical inconsistencies

**Location:** 726-792 (Eq 51-57); origin `Research/manuscripts/PIFB2.tex:596ff`.

**Severity:** medium

**Evidence:** Rendered at 150 dpi (p. 14-16). (a) Eq (51) ends each case row with a comma and then adds a period after the brace (l.735-737), so the display ends ",." and the sentence continues with lowercase "and substituting" (display-punctuation script flags PERIOD-BEFORE-LOWERCASE). (b) Every display in 2.6.1 is surrounded by blank lines (l.733/739, 741/746, 751/756, 762/767, 769/774, 779/784, 786/791); five lowercase continuation clauses ("and substituting", "which has", "produces", "where", "where") are therefore typeset as new indented paragraphs (visible on pp. 14-15), and the displays gain extra vertical space. (c) Straight double quotes at 757 and 775 render as closing quotes on both sides (” ”). (d) "we have:" (768) and "as:" (785) put colons before displays; nowhere else does the paper do this. (e) The five bare `\eqref` references in the whole main text are all here (729, 740, 768, 775, 792); every other reference is "Eq.~" or "Equation~". (f) "auto-regressive" (732) versus "autoregressive" (four other uses). (g) First-person generative language ("Within our generative model", 732; "In our gauge-theoretic framework, this encodes the prior belief that an agent's state was generated by a source", 757) contradicts the paper's scoping (l.1176, Supp 78). (h) Internal contradiction: "provides a unified derivation of several attention masks" (729) and "ALiBi arises from a prior belief" (775) versus "accommodated ... rather than derived from first principles" (792). (i) Priors are written `\pi_k` (729, 792), `\pi_j^{(\mathrm{causal})}`, `\pi_j^{(\mathrm{window})}`, `\pi_j` (735-781) although each depends on the receiver `i` (e.g. `1/(i+1)`); the rest of the paper writes `\pi_{ij}`. (j) Line 792 is a single 130-word sentence. The PIFB2 source of this subsection has none of (b)-(d); they were introduced in this copy.

**Fix:** Remove the blank lines around displays; change Eq (51) to end with a comma after the brace and drop the comma after the second case (or keep row commas and end with nothing); use ``` ``local neighborhood'' ``` and cite ALiBi without quotation marks; replace colons by "gives" or "we obtain"; write `Eq.~\eqref{...}`; use `\pi_{ij}`; rewrite 729 as "The general solution, Eq.~\eqref{eq:mixture_softmax_general}, accommodates several attention masks and positional preferences as choices of $\pi_{ij}$"; delete "arises from a prior belief" (775) or change to "corresponds to a prior under which"; replace "Within our generative model" with "In the source-selection objective"; split line 792 into two sentences.

**Falsifies:** A compiled PDF without the indented continuation paragraphs, or a version in which `pi_j` is declared to carry an implicit receiver index, would retire (b) and (i).

**Status:** The algebra (log-prior enters additively and untempered) is derived and settled. The prose "unified derivation"/"arises from" inflates it (the priors are chosen, not derived), and 792 already says so; the subsection currently contradicts itself.

**Novelty vs prior review:** new (prior C2-C4 concern ALiBi head counts, window radius, and causal-mask uniqueness; none of the items above)

### E6. Unreferenced floats and an unlabeled proposition called a theorem

**Location:** Figure 2 (l.476-525; only citation is Figure 1's caption, l.262); Table 2 (`tab:fep_nn_correspondence`, l.1071-1091); Table 3 (`tab:relational_run`, l.1140-1153); Lemma 1 (`thm:vanishing_holonomy`, l.581); Proposition 2 (l.913, no `\label`); lines 924, 939, 1009, 1171.

**Severity:** medium

**Evidence:** `labels.py` reference counts: `fig:comparison_content_interfaces` 1 reference (inside Figure 1's caption), `tab:fep_nn_correspondence` 0, `tab:relational_run` 0, `thm:vanishing_holonomy` 0. Proposition 2 ("Passive covariance of ideal predictive attention") carries no label and is referred to as "the attention covariance theorem" (939), "The covariance theorem" and "the attention theorem" (1171), and "The proposition" (924). Line 1009 says shared key covariance "satisfies the weaker proposition", meaning the weaker hypothesis of Proposition 3. Figure 2, which the prior review calls the clearer operational introduction (C5), is never pointed to by the running text; it floats to p. 9, past 2.4.1 where its content is developed.

**Fix:** Add `\label{prop:passive_covariance}` and write "Proposition~\ref{prop:passive_covariance}" at 924, 939, and 1171; at 1009 write "satisfies the hypothesis of Proposition~\ref{prop:projected_dot_product}". Cite Figure 2 in the body where the interfaces are introduced (e.g. l.411: "Figure~\ref{fig:comparison_content_interfaces} shows one head"). Cite Table 2 in the first paragraph of Section 4 or at l.1053, and Table 3 in the first paragraph of Section 5.2 or at l.1155. Cite Lemma 1 at l.1189 where the Conclusion contrasts link products with the flat transport.

**Falsifies:** A body-text `\ref` to any of these objects that the extraction missed (none was found in either document).

**Status:** Proposition 2 is proven (P); calling it a theorem slightly inflates its standing.

**Novelty vs prior review:** new (C6 checked unresolved references, not uncited objects)

### E7. Second-tier collisions across sections and across the two documents

**Location:** listed per item; full table in "Notation table" below.

**Severity:** medium (individually low; the volume is the problem)

**Evidence:** From `symbols_by_glyph.txt`, confirmed against the source:

- `\gamma`: closed walk (594-607) and LayerNorm gain in `\operatorname{LayerNorm}_{\gamma,b}` (930, Alg 1 step 11).
- `\varepsilon_i`: Gaussian channel noise (635) and key-norm bias bound (Eq 85, 1024); `\varepsilon` measurement noise (902).
- Noise covariances: `Q_i` (Eq 38), `R` (Eq 74), and Supp `R_i` (S6) are all Gaussian-record noise covariances with three names, while `R_i` in the main text is the RoPE rotation (1058) and `R_{Q,i}` the lift (547).
- `H`: number of heads (366), comparison/content spaces `H_h^{cmp},H_h^{val}` (368), and differential entropy `H(q_i)` (Eq 61, 829).
- `X`: token frame generator `X_{x_i}` (357, Alg 1) and the reference Gaussian random vector `X_i` (Eq 28, 554); also `X` (decoder integrals, 828), `X_j` (902), and Supp `X` (structural data).
- `S_i`: allowed support set (688, 945, 1017) beside comparison maps `S_Q,S_K` and the sans-serif endpoint `\mathsf S_{j,h}`.
- `r_j(z)`: content laws (891) beside dimensions `r_h` (368); `r` is also the walk length (594) and `r=r_h` in Section 4 (971).
- `E_{12},E_{21},E_{11},E_{22}`: matrix units (679) in the same subsection that uses fibers `E_i^{(b)}` (652).
- `a`: common reference-basis change `U_i\mapsto U_ia` (386) and, 14 lines later, the test vector "for `a\ne0`" (400).
- Parenthesized superscripts: `(b)` for blocks (`q_i^{(b)}`, `\Sigma_i^{(b)}`, `U_i^{(b)}`, `E_i^{(b)}`, 647-669) versus `(\ell)` for layers (`q_i^{(\ell)}`, 364) and `(h)` for heads; `q_i^{(1)}` is ambiguous.
- Initial state `q_i(0)=p_{\mathrm{token}(i)}` (804) versus `\mu_i^{(0)}` (Alg 1) and `q_i(c)` = section at context `c` (Figure 1).
- Prior bank `\mu_p^c,\Sigma_p^c,p_c` (801) versus `\mu_{p,v},\Sigma_{p,v}` (832); token-type index `c` (799) versus `v` (812, 953).
- Frame generators: `\phi_i` (580), `\phi_c` (801), `X_{x_i},Y_i` (357, Alg 1) for one parameterization.
- `V`: vocabulary size (799), random content vector `V=TX_j` (902), projected covariances `V_{Q,i},V_{K,j},V_*` (974), reference space `\mathsf V`; `d` (799) for the width called `K` everywhere else.
- Supplement versus main: per-row temperature `\tau_i` (Supp 68-74) versus per-head `\tau_h`; `\operatorname{LN}_\epsilon` (Supp 120) versus `\operatorname{LayerNorm}_{\gamma,b}`; `\Gamma` covariance (Supp 90) versus `\Gamma` sections (303); `\ell_a` kernels versus layer index `\ell`.
- Operators: `\operatorname{tr}` in Eq (62) versus `\operatorname{Tr}` elsewhere (Eq 35, 81, S6); `\log|\Sigma_{p,v}|` in Eq (62) versus `\log\det` in Eq (81), while `|\cdot|` is also absolute value (753, 764, 1025). The preamble macros `\KL` and `\Tr` are defined in both documents and never used.
- Overbar/overline has five meanings: capped cost `\bar D` (1114), predictive average `\bar p` (850), mixture mean `\bar v` (1069), block-restricted maps `\overline S,\overline T,\overline O` (654-657), residual mean `\bar e` (Supp 94).

**Fix:** See the renaming scheme below (items R10-R24). All are one-to-few-line substitutions.

**Falsifies:** Any item where a local redefinition sentence is present at the point of reuse would lower its tier; for the listed items none was found.

**Status:** Presentation only.

**Novelty vs prior review:** new

### E8. Missing standard citations for the experiment's dataset and components

**Location:** 1132-1138 (WikiText-103), 933 and 1132 (GELU), 930 and 1118 (LayerNorm), 1123 (AdamW), 1136 (PyTorch).

**Severity:** medium

**Evidence:** `labels.py` citation list: 33 keys in the main, 3 in the supplement; none for WikiText-103, GELU, LayerNorm (main), AdamW, or PyTorch. `references.bib` already contains `merity2017pointer` (Pointer Sentinel Mixture Models, the WikiText-103 source), `hendrycks2016gaussian` (GELUs), and `ba2016layernorm` (cited only at Supp 117). No AdamW entry exists (Loshchilov and Hutter, "Decoupled Weight Decay Regularization", ICLR 2019). JMLR's author information asks authors to "clearly acknowledge the contributions of their predecessors".

**Fix:** Cite `\citep{merity2017pointer}` at the first mention of WikiText-103 (1132), `\citep{hendrycks2016gaussian}` at Eq (77), `\citep{ba2016layernorm}` at Eq (76), and add and cite Loshchilov and Hutter (2019) at Algorithm 1 step 16 (and optionally PyTorch at 1136).

**Falsifies:** A citation to these works elsewhere in the pair; none found.

**Status:** Empirical methods reporting; no claim status change.

**Novelty vs prior review:** new (R3 concerns optimizer details, not citations)

### E9. Attribution of the latent-source and positional-prior constructions

**Location:** Section 2.6 (686-725), 2.6.1 (726-792), Proposition 3 (987-1007), Supp A (68-74); introduction citation list (67).

**Severity:** medium

**Evidence (primary sources read):** Singh and Buckley (NeurIPS 2023, abstract on proceedings.neurips.cc) "demonstrate that attention can be viewed as inference over an implicitly defined set of possible adjacency structures in a graphical model" and introduce "a geometric prior (with conjugate hyper-prior) over the adjacency structures" that "dynamically scales the context window"; this is the construction of 2.6.1 (priors over sources as masks and positional biases). They are cited only in the introduction's list (67). Deng et al. (NeurIPS 2018, arXiv 1807.03756) treat the attended source as a latent alignment variable with variational inference; also cited only at 67. Niculae and Blondel (NeurIPS 2017, arXiv 1705.07704, Sec. 3) obtain softmax from `\Omega(y)=\sum_iy_i\log y_i` regularization of the argmax over the simplex; Eq (48)-(50) cite only Boyd and Vandenberghe and Wainwright and Jordan. Kim, Papamakarios and Mnih (ICML 2021, arXiv 2006.04710) formulate L2 self-attention, whose logit expansion carries the key-norm term that Proposition 3 isolates. Movellan and Gabbur (arXiv 2010.15583) show attention "as performing MAP inference under a special case of the Probabilistic Transformer" (a Gaussian mixture). Pro-Attention (IEEE Access 2022, full text read) fits a univariate Gaussian to the components of each projected token vector (a scalar mean and standard deviation per token) and scores pairs by negative KL; the manuscript's contrast "Our Gaussian observables are multivariate" (67) is correct but would be sharper stated explicitly.

**Fix:** At Eq (44)-(50) add "The source-label reading of softmax attention is established \citep{Deng2018LatentAlignment,Singh2023ImplicitStructuralInference,Singh2023MarginalProbability}; the entropy-regularized form is that of \citet{niculae2017regularized}." At 2.6.1 add "Priors over sources as positional structure also appear in \citet{Singh2023ImplicitStructuralInference}." After Proposition 3 add a comparison with L2 self-attention \citep{kim2021lipschitz}. At line 67 state "Pro-Attention summarizes each projected token by the scalar mean and variance of its coordinates". Consider Movellan and Gabbur at 2.6. (Bibliography keys above are suggestions; only the Singh and Deng keys exist.)

**Falsifies:** If the manuscript's contribution statement already disclaimed the latent-source reading as prior work in 2.6 (it disclaims Gaussian-KL routing only, l.67), this would drop to low.

**Status:** The Gibbs optimizer is derived and settled; the prose does not claim priority for the latent-source reading, but its placement (only in an introduction list) under-attributes it.

**Novelty vs prior review:** extends R7 (R7 adds CRATE and Transformer-MGK; these are different precedents)

### E10. Document-level organization: where the operator lives, duplication, and the formal spine

**Location:** whole main text; Supp A-B.

**Severity:** medium

**Evidence:** `section_wordcounts.txt` and page mapping of the faithful build. Section 2 spans pp. 3-17 (about 14.5 of 27.5 body pages), holds about 4,250 of 8,600 prose words (math excluded) and 52 of 70 display environments; Section 3 has 780 words, Section 4 1,130, Section 5 790, Section 6 550. The operator's pieces first appear at: `D_{ij}` Eq (18) p. 6; `m_i` Eq (22) p. 8; Gibbs weights Eq (49) p. 14, restated as Eq (66) p. 17; aggregation Eq (67)-(70) p. 18; explicit Gaussian KL Eq (81) p. 20; the complete operator only in Algorithm 1, p. 24 (confirms R2). Repetition map: the Gibbs lemma is derived four times (Eq 48-50; Eq 59-60 for the decoder; Eq 65-66; Supp S3-S4); the normalized-mixture KL identity twice (Eq 46-47; Eq 71-73) plus Supp 76; passive covariance three times (l.347, l.466 which already states the proposition's conclusion, Proposition 2); "covariance passthrough is not uncertainty propagation" five times (637, 937, 1069, 1171, Supp 129); "LayerNorm/MLP/decoder need a separate symmetry analysis" five times (359, 617, 924, 939, 1171); "unit temperature is the joint's KL, general temperature changes the objective" six times (65, 721, 900, 1189, Supp 74, Supp 76). The value/output aggregation is stated twice with different symbols (Eq 67-70 with `a`; Eq 87-88 with `z`). The only formal environments are Lemma 1 (flat identification), Proposition 2 (passive covariance), and Proposition 3 (biased dot product); the Gibbs optimality and uniqueness, the link endpoint law, the rank bound Eq (23), block KL additivity Eq (42), and the bias bound Eq (86) are prose. Sentence-level count (`negation_sentences.txt`): 114 of 591 main-text sentences (19%) contain an explicit negation, concentrated in Contribution and Limits (7 of 13) and Section 5.2 (12 of 37).

**Fix:** (a) Number four to five statements and cite them by number: Proposition A, Gibbs optimality and uniqueness with value `-\tau\log Z_i` (Eq 48-50); Proposition B, endpoint covariance of content and routed links including Eq (20)-(22) and the current Proposition 2; Proposition C, rank bound and composition defect (Eq 23, 29-30); Proposition D, the current Proposition 3 with the bias bound Eq (86) as a corollary; Lemma 1 stays. Then state each disclaimer once, next to the statement it limits, and delete the other four or five copies. (b) Merge Eq (65)-(66) into a citation of Proposition A, and state the decoder readout (Eq 59-60) as an application of it. (c) Page budget for R2's move set, from the word counts: comparison lift Eq (26)-(28) about 200 words; Gaussian channels 2.4.4 about 160; most of 2.5 about 550; 2.6.1 beyond the causal prior about 350; Section 2.8 about 250; 4.4 about 270; Eq (74) paragraph about 90; total about 1,900 words and 20 displays, roughly 6 pages. That would give a main text of about 24-25 pages before results and a supplement of about 9-10 pages. Supplement B.3 (114 words) duplicates line 959 and can shrink to one sentence.

**Falsifies:** A reading test in which a referee can state the operator after p. 8 would weaken (a); the page estimate is falsified by recompiling the moved version.

**Status:** The prose deflates the positive content by restating limits; it does not inflate claims.

**Novelty vs prior review:** extends R2 (R2 gives the reorder; this adds the duplication map, the formal spine, and page arithmetic)

### E11. Wrong or imprecise internal pointers

**Location:** 879, 660, 535, 891, 73, 359, 939, Supp 76.

**Severity:** low

**Evidence:** Rendered text and the label map. (a) Line 879: "its relation to conventional attention scaling is considered in Section 4.1"; the scaling discussion is lines 1034-1036, in Section 4.2. (b) Line 660: "the passive site action of Section 2.4"; the action is defined in Section 2.2, Eq (11). (c) Lines 535 and 891 cite "Eq. (18)" for the Gaussian observables and comparison densities, which are Eq (16)-(17); the label sits on the `D_{ij}` row of the align block. (d) The roadmap (73) reads "Section 5.2 reports a language-model realization" because Section 5 has no label and `sec:relational_run` is on 5.2. (e) Lines 359 and 939 point to "Supplementary Appendix B" for the nonlinear-block limits, which are B.2 (`sec:nonlinear_gaussian_scope`, unused). (f) Supp 76 cites "Eq. (73)" without saying it is a main-text equation.

**Fix:** (a) Section~\ref{...} of 4.2 (label it); (b) "of Eq.~\eqref{eq:gauge_action_gaussians}"; (c) move the label to the `q_{Q,i}` row or cite "Eqs.~(16)-(17)"; (d) add `\label{sec:lm_realization}` to Section 5 and cite it in 73; (e) cite `sec:nonlinear_gaussian_scope`; (f) "main-text Eq.~\eqref{...}".

**Falsifies:** A version in which 4.1 contains the scale discussion, or 2.4 redefines the passive action.

**Status:** Presentation only.

**Novelty vs prior review:** new

### E12. Label hygiene

**Location:** see table.

**Severity:** low

**Evidence:** `labels_refs_cites.txt`.

| Issue | Labels (line) |
|---|---|
| Two labels on one object | `sec:construction_overview` + `sec:free_energy_section` (76-77); `fig:link_construction` + `fig:bundle_sections_surface` (263-264); `sec:projection_link_geometry` + `sec:matrix_link_fields` (406-407, both referenced, 1 and 3 times); `tab:link_conventions` + `tab:notation` (436-437); `sec:transformer_comparison_summary` + `sec:transformer_limit` (963-964); `sec:value_aggregation` + `sec:multihead` (1039-1040) |
| Legacy or misleading names | `sec:free_energy_section` on a section that disclaims a common free energy; `tab:fep_nn_correspondence` on the conditional transformer table (the paper disclaims FEP attribution, 1176); `sec:supp_decode_derivation` and `eq:supp_decode_canonical`, `eq:supp_kl_decomposition`, `eq:supp_expected_loglik`, `eq:supp_token_likelihood` on main-text Section 2.8; `sec:vanishing_holonomy`, `thm:vanishing_holonomy`, `eq:holonomy` on "Composition and the flat reference specialization" (the text stresses link products are not holonomy); `sec:transformer_limit` (not a limit); `sec:current_algorithm` on 3.4 (the algorithm is in Section 5); `eq:next_token_factorization_v2` (version suffix); `tab:notation` on a table that is not a notation table |
| Unused | 79 of 118 labels (both documents); 52 of 72 main-text equation labels (20 of 89 numbered main equations are cited by number); all supplement subsection labels |
| Cross-document (`xr`) | main 359, 939 -> `app:architecture_scope`; main 1176 -> `app:fixed_joint_bridge`; Supp 76 -> `eq:relational_normalized_model` |
| Multiply defined | none |

**Fix:** Delete the six secondary labels; rename the legacy ones (`sec:geometric_construction`, `tab:transformer_correspondence`, `sec:prior_bank_readout`, `sec:flat_identification`, `lem:flat_identification`, `sec:transformer_correspondence`, `sec:autoregressive_prediction`, `eq:next_token_factorization`). Unused labels on unnumbered-worthy displays can stay; they are invisible.

**Falsifies:** None; this is a mechanical inventory.

**Status:** Source-level only (invisible in the PDF), but visible in an arXiv source upload.

**Novelty vs prior review:** new (C6 reported only the absence of duplicate definitions)

### E13. Undefined acronyms, code names, and figure notation

**Location:** VFE (1176; Supp 51, 54), ELBO (Supp 74), MLP (359), GELU (933), RoPE (1058), ALiBi (759; expanded 775), HeadMixer (1185), E-step (1098), "prior-anchored natural-gradient update" (1053), "cognitive gauge frame" (409), Figure 1 label `\mathcal G_K` (164) and "Base manifold" (129).

**Severity:** low

**Evidence:** Fixed-string counts (first occurrence lines above); none of these terms is expanded or defined at first use. `HeadMixer` and `E-step` are code or companion-paper terms. `\mathcal G_K` labels the fibers in Figure 1 but the text uses `\mathcal G(E)` for the statistical bundle and `\mathcal G(E_i)` for its fiber; `G` is the group.

**Fix:** Expand at first use: "variational free energy (VFE)", "evidence lower bound (ELBO)", "multilayer perceptron (MLP)", "Gaussian error linear unit (GELU) \citep{hendrycks2016gaussian}", "rotary position embedding (RoPE)", ALiBi at 759. Replace "HeadMixer" by "the optional cross-block head-mixing layer (disabled here)" and "belief E-step" by "iterative belief update". Delete "cognitive" in 409. Relabel Figure 1's fiber `\mathcal G(E_c)` and its base "Contextual base `\mathcal C`".

**Falsifies:** A definition of these terms elsewhere in the pair; none found.

**Status:** Presentation only.

**Novelty vs prior review:** new

### E14. Symbols used before definition, or defined only inside a floating table

**Location:** 681; Figures 1-2 (257, 514); Table 1 (421-432).

**Severity:** low

**Evidence:** `a_i,b_j` at 681, defined at 973. `\beta_{ij}^{(h)}`, `\pi_{ij}^{(h)}`, `\tau_h` appear in Figure 1 (p. 3), Table 1 (p. 7), and Figure 2 (p. 9) before Section 2.6 (p. 13). `A_{Q,i,h},A_{K,i,h}`, `\mathsf S_{j,h},\mathsf R_{i,h}`, `G_i`, and `\Theta_{ij}` are defined only in Table 1, a `[t]` float, and then used in running text (444, 457, 531, 609). Table 1 carries `tab:notation` but lists about 25 symbols; it omits `D_{ij}`, `m_i`, `M_h`, `r_h,s_h` (only inside entries), `\ell,L`, `V_{Q,i},V_{K,j},V_*`, `a_i,b_j`, `P_j`, `\mathsf q_i,\mathsf k_j`, and all decoder and supplement symbols.

**Fix:** Define `A_{Q,i,h}`, `\mathsf S`, `\mathsf R`, and `G_i` in one sentence of 2.4 before first use; keep Table 1 as a summary. Add the complete notation table below (after renaming) to the supplement and caption Table 1 "Link conventions" only.

**Falsifies:** A text definition before first use for any listed symbol; none found.

**Status:** Presentation only.

**Novelty vs prior review:** new

### E15. Heading capitalization and display punctuation

**Location:** section headings; Eq (5) at 299-306; 2.6.1 paragraph headings.

**Severity:** low

**Evidence:** Subsection-level headings in Title Case: 2.5, 2.6, 2.6.1, 2.7, 2.8, 6.1, 6.3, 6.4, 7.1 (9); in sentence case: 2.1-2.4.4, 3.1-3.4, 4.1-4.4, 5.1, 5.2, 6.2, Supp B.1-B.3 (18). The 2.6.1 `\paragraph` headings are Title Case with periods; the only other `\paragraph` is "Supplementary Material." after the acknowledgments. `displaypunct.py` over all 77 display environments: Eq (5) ends without punctuation although the next sentence starts "Here"; Eq (51) is covered in E5; all others end with a period or comma consistent with the following text.

**Fix:** Choose one case for all subsection-level headings (JMLR papers commonly use Title Case) and apply it in both documents; add the period to Eq (5).

**Falsifies:** None.

**Status:** Presentation only.

**Novelty vs prior review:** new

### E16. Citation pinpoints: one error, verified pinpoints, and recommended additions

**Location:** 683 (Fuchs, He), 824 (Blei), 1036 and 1051 (Vaswani), 720 (Boyd; Wainwright and Jordan), 902 (Petersen), 635 and 841 (Bishop), Supp 66 (Blei), 355 (Amari).

**Severity:** low

**Evidence:** Primary sources read; see the citation audit table. The Fuchs et al. (NeurIPS 2020; arXiv 2006.10503) Section 2.3 "Equivariance" covers group representations and type-`\ell` vectors; the "invariant attention and equivariant values" construction is Section 3.2, Eqs. (10)-(11); Appendix D.3 does describe partitioning the channels of each feature type across heads, as claimed. All other bracketed pinpoints are correct (table).

**Fix:** At 683 write `\citep[Secs.~2.3 and 3.2, App.~D.3]{fuchs2020se3}`. Optional pinpoints: Boyd and Vandenberghe Example 3.25 (conjugate of log-sum-exp is the negative entropy on the simplex) at 720; Blei et al. Sec. 2.2, Eq. (14) at Supp 66; Petersen and Pedersen Sec. 8.1.3, Eq. (353) at 902 and Sec. 8.2.2, Eq. (380) for Eq (62) and Supp S6; Bishop Sec. 2.3.3 at 635; Amari Chapter 3 ("Invariant Geometry of Manifold of Probability Distributions") at 355.

**Falsifies:** A NeurIPS camera-ready version of Fuchs et al. with section numbering different from the current arXiv version (I read arXiv 2006.10503; the proceedings PDF was not compared).

**Status:** The claim at 683 is a sourced description (S); the pinpoint is wrong in part.

**Novelty vs prior review:** new

### E17. Bibliography entry errors

**Location:** `references.bib` entries used by the pair.

**Severity:** low

**Evidence:** Rendered `.bbl` plus Crossref and arXiv metadata. (1) `sengupta2017gauge` has `eprint = {1705.06614}` but plainnat ignores `eprint`, so the PDF prints only "arXiv preprint, 2017" (unrecoverable); arXiv confirms 1705.06614. (2) `jiang2023mistral` title renders "Mistral 7b" (unprotected case). (3) `press2022train` is `@article` with `journal = {International Conference on Learning Representations}`. (4) `Blei2017` lacks issue 518 (Crossref: 112(518):859-877). (5) `nakahara2003geometry` lacks "2nd edition" (the 2003 edition). (6) `su2024roformer` author order follows arXiv; the Neurocomputing record in Crossref lists Su, Ahmed (Murtadha), Lu, Pan, Bo (Wen), Liu; I could not determine which the publisher's PDF prints. (7) NeurIPS entries lack pages: He et al. 2021 pp. 27331-27343; Singh and Buckley 2023a pp. 24929-24946 (proceedings metadata). (8) Author names mix initials (Amari, Bishop, Blei et al., Boyd, Wainwright, Wilson) with full names. (9) `radford2019language` "OpenAI Blog 1(8):9" is a common but nonstandard form for a technical report. Verified correct: Bae et al. (IEEE Access 10:131192-131201, doi 10.1109/ACCESS.2022.3229055), Culver (PAMS 17(5):1146-1151), Wetterich (NPB 884:44-65), Wilson (PRD 10(8):2445-2459), Sengupta et al. 2016 (PLoS Biol 14(3):e1002400), Wainwright and Jordan (FnTML 1(1-2):1-305), RoFormer (Neurocomputing 568:127063), Cohen et al. 2019 (PMLR 97:1321-1330).

**Fix:** `journal = {arXiv preprint arXiv:1705.06614}`; `title = {Mistral 7{B}}`; `@inproceedings{press2022train, booktitle = {International Conference on Learning Representations}}`; add `number = {518}`; `edition = {2nd}, publisher = {Institute of Physics Publishing}`; add pages; normalize names.

**Falsifies:** A bibliography style that prints `eprint` (plainnat does not).

**Status:** n/a

**Novelty vs prior review:** new

### E18. Float and package layout; the prior remedy was tested

**Location:** Figure 1 `[H]` (81), Table 3 `[H]` (1140), `\FloatBarrier` (961, 1127), `\setcounter{algorithm}{0}` (1102), preamble 6-24 (main) and 6-20 (Supp).

**Severity:** low

**Evidence:** Faithful build: underfull output pages 2, 3, 9, 24, 25 (`underfull_pages.txt`); p. 3 shows a stretched gap of about 1.6 in between Section 2's first paragraph and Figure 1, and p. 24 a large gap between Algorithm 1 and 5.1. Test build (`build_exp`, a modified copy): removing `subcaption`, changing both `[H]` to `[tbp]`, and deleting both `\FloatBarrier` leaves 31 pages and moves the underfull pages to 2, 3, 23, 25, 27; Figure 1 then floats above the Section 2 heading. The residual cause is jmlr2e's `\widowpenalty=\clubpenalty=10000` together with display-dense pages. Removing the unused `subcaption` package eliminated the only package warning ("caption: Unknown document class") and restored jmlr2e's hanging-label captions (the `caption` package had replaced jmlr2e's `\@makecaption`). Unused packages: `subcaption`, `longtable`, `listings` (`\lstset` with no listing), `bbm` (no `\mathbbm`; the indicator uses `\mathbf{1}`), TikZ libraries `patterns`, `decorations.markings`, `decorations.pathmorphing`, `shapes.geometric`, `3d`; the supplement loads TikZ, xcolor, subcaption, listings, and tabularx without using them. `\graphicspath` (both documents) lists five directories for a pair with no `\includegraphics`; `./figs/` and `../../Transformer Manuscript/fig_transformer_validation/` do not exist (the latter also contains a space) and `../` points outside the manuscript folder. `\setcounter{algorithm}{0}` precedes the first algorithm and is redundant.

**Fix:** Remove the unused packages and `\graphicspath`; keep `[tbp]` floats; delete both `\FloatBarrier`; reduce Figure 1's height (it is scaled to `0.95\textwidth` and takes about 60% of p. 3). The pagination itself improves only with the R2 reorganization (E10), not with float options.

**Falsifies:** A float configuration that removes all underfull pages without reorganization would contradict the test result.

**Status:** n/a

**Novelty vs prior review:** extends C6 and partly disagrees: C6 says "ordinary float control should improve" pagination; the test shows float control alone does not, and identifies the unused `subcaption` package as the cause of the caption warning C6 left unexplained.

### E19. Code-availability link is invisible and unversioned

**Location:** 1194; jmlr2e.sty:63.

**Severity:** low

**Evidence:** jmlr2e loads hyperref with `colorlinks=false, allbordercolors={1 1 1}`; decompressing the PDF streams shows the GitHub URI only in a link annotation with border color `[1 1 1]` (white), and `pdftotext` shows the printed text "available at the V3 Transformer repository." with no URL. The main also contains three `GoToR` links (and the supplement one) that open `GL(K)_supplementary_v2.pdf` / `GL(K)_attention_v2.pdf` by file name.

**Fix:** "The reference implementation is available at \url{https://github.com/cdenn016/V3_Transformer} (tag ⟨name⟩, commit ⟨hash⟩; archived at ⟨DOI⟩)." Freeze the tag with the final runs (consistent with R3).

**Falsifies:** A printed URL elsewhere in the paper; none found.

**Status:** n/a

**Novelty vs prior review:** new (R3/R8 concern reproducibility and companion citations, not the invisible URL)

### E20. Packaging for arXiv and JMLR

**Location:** file names; `\externaldocument` lines (main 31, Supp 26).

**Severity:** low

**Evidence:** arXiv's submission help (fetched 2026-09-23) states that it "will accept only the following characters in file names: a-z A-Z 0-9 _ + - . , ="; the parentheses in `GL(K)_attention_v2.tex` and `GL(K)_supplementary_v2.tex` are outside that set, and the `\externaldocument{GL(K)_...}` arguments would have to change with the files. The `xr` references need the partner `.aux` at build time. JMLR's author information (fetched the same day) says page counts include appendices and describes "online appendices" as data, demonstrations, and source code.

**Fix:** Rename to e.g. `glk_attention_v2.tex` and `glk_supplement_v2.tex` and update both `\externaldocument` calls; for JMLR, merge the supplement as appendices of one PDF (removes `xr`, the `GoToR` links, and the separate bibliography).

**Falsifies:** An arXiv policy change allowing parentheses.

**Status:** n/a

**Novelty vs prior review:** extends C8 (venue rules)

### E21. JMLR template usage, acknowledgments, keywords, and metadata

**Location:** 36, 47, 55, 1193-1201; Supp 30, 42; jmlr2e.sty 221-223, 372-373.

**Severity:** low

**Evidence:** (a) Keywords are typed as `\noindent\textbf{Keywords:}` instead of jmlr2e's `keywords` environment, so they are not indented with the abstract. They omit "gauge" although the title begins "Gauge-Covariant", and two of five are paper-internal jargon ("sending and receiving geometry", "predictive content"); JMLR asks that new terminology be justified. (b) Acknowledgments use `\section*{Acknowledgments}`; jmlr2e's `\acks{}` prints "Acknowledgments and Disclosure of Funding", matching JMLR's funding-disclosure requirement (the text already declares no funding). (c) "Code Availability" is Subsection 7.1 of the Conclusion. (d) The closing `\paragraph{Supplementary Material.}` restates line 73 and Supp 44. (e) The supplement's running head drops "Gaussian" ("Gauge-Covariant Attention: Supplementary Material"). (f) In preprint mode `\jmlrheading` prints "©2026 Robert C. Dennis. License: CC-BY 4.0" on p. 1 of both documents; the empty volume/page/date/editor arguments are ignored, which is fine for a preprint, but the license statement is a legal declaration that should match the arXiv license chosen. (g) PDF metadata Title/Author/Keywords are empty (`pdfinfo`). (h) The AI-use sentence writes "Claude Opus 4.5/4.6" and "source inspection" (ambiguous: code or literature).

**Fix:** `\begin{keywords} gauge covariance, Gaussian attention, variational routing, matrix links, transformers \end{keywords}`; `\acks{The author used Claude Opus 4.5 and Claude Opus 4.6 (Anthropic) and OpenAI Codex for programming, figures, LaTeX, code inspection, and manuscript editing. The author remains responsible for the claims and computational record. The author received no funding and declares no conflicts of interest.}`; make Code Availability an unnumbered section before the acknowledgments; delete the closing "Supplementary Material" paragraph; set `\hypersetup{pdftitle=..., pdfauthor=..., pdfkeywords=...}`; align the supplement's `\ShortHeadings`.

**Falsifies:** None.

**Status:** n/a

**Novelty vs prior review:** new

### E22. Terminology drift for single objects

**Location:** throughout; counts from fixed-string search.

**Severity:** low

**Evidence:** `\Omega_{ij}` is the "flat identification" (63), "flat reference transport" (abstract), "reference identification" (574), "flat reference identification" (Lemma 1, Table 1), and "flat frame transport" (1189). `T_h` is a "sending map", "value map", "content map", and "content interface"; `S_{Q,h}` a "query map", "comparison map", "role map" (865), "role projection" (1134), and "role measurement". The intro's "processing defect" (71) is the body's "composition defect" (572). "Channel" means a head (Figure 1 caption), a Gaussian kernel (2.4.4), a comparison or content pathway (2.6 title), and a latent dimension (1053). "Link field(s)" (1169, 1189) is never defined.

**Fix:** Fix one name per object in Table 1 (for example "flat reference identification", "sending map `T_h` (value map)", "comparison map", "composition defect") and use it throughout; reserve "channel" for the Gaussian kernel of 2.4.4 and use "head" otherwise; define or drop "link field".

**Falsifies:** None.

**Status:** Presentation only.

**Novelty vs prior review:** new

### E23. Index and placement conventions: verified, with three exceptions

**Location:** all pairwise quantities.

**Severity:** low

**Evidence:** Checked every pairwise object: `\beta_{ij}`, `\pi_{ij}`, `D_{ij}`, `L_{ij}^{(h)}`, `\mathcal C_{ij}`, `A_{ij}`, `\Omega_{ij}`, `\Theta_{ij}`, `B_{ij}`, `\mathcal L_{ij}`, and Supp `L_{ij}`, `\Gamma_{ij}`, `V_{ij}`. The first index is always the receiver and `ij` always denotes a map from `j` to `i` (Eq 19, 21, 25, 29-32, 36-39; Supp S5). Transposes use `\top` throughout; the contragredient laws `B'_{ij}=g_i^{-\top}B_{ij}g_j^{-1}` and `G_i'=g_i^{-\top}G_ig_i^{-1}` are consistent with the definitions; the column/row dictionary `W_V^{(h)}=T_h`, `W_O^{(h)}=O_h` with transposes in the row convention matches Vaswani et al. Sec. 3.2.2. Exceptions: (i) 2.6.1 suppresses the receiver (`\pi_j`, `\pi_k`, E5); (ii) Eq (65) mixes `\beta_j` with `D_{ij}` and `\pi_{ij}` in one display; (iii) the loop product's orientation is right to left relative to the listed walk (E4). Head index is a subscript on maps, dimensions, and temperature and a parenthesized superscript on site and pair quantities; blocks also use a parenthesized superscript (E7).

**Fix:** State the convention once in 2.3 (it is partly stated at 384) including the head-index rule, and apply the E4, E5, and E7 fixes.

**Falsifies:** A pairwise symbol with the opposite convention; none found.

**Status:** Derived conventions are consistent.

**Novelty vs prior review:** new

## Notation table (both documents)

Legend: M = main line, S = supplement line; first line is the first occurrence of that meaning. Tier: T1 misleading collision in the core operator or with a Table 1 symbol; T2 collision across sections or documents; T3 locally scoped reuse, acceptable. Unmarked rows have a single meaning.

| Glyph | Meaning | First line | Tier |
|---|---|---|---|
| `A`, `A_*` | common invertible map and its pushforward (KL invariance) | M351 | T3 |
| `A_{Q,i,h}`, `A_{K,j,h}` | local comparison measurements `S U^{-1}` | M429 (Table 1), M531 | T2 vs `A_{ij}` |
| `A_{ij}` | reference routed operator `\sum_h\beta O_hT_h` | M601 | T2 |
| `\mathcal A_i` | tempered routing objective | M704 | |
| `B` | number of frame blocks | M421 | T3 |
| `B_{ij}` | comparison tensor `E_j\to E_i^*` | M539 | T1 |
| `B_{ij}` | generic edge matrices in the loop product | M594 | T1 |
| `\mathcal B` | space of nondegenerate Gaussians on `\mathsf V` | M279 | |
| `\mathcal C` | contextual base | M270 (Fig. M129) | T2 vs `\mathcal C_{ij}` |
| `\mathcal C_{ij}`, `\mathcal C_{ij}^{(h)}` | routed link (summed; per head) | M431/461; M911 | T2 |
| `C_i` | reference covariance `U_i^{-1}\Sigma_iU_i^{-\top}` | M330 | |
| `C` | shared reference covariance in an example | M1009 | T3 |
| `D_{\mathrm{KL}}` | KL divergence | M351 | |
| `D_{ij}`, `D_{ij}^{(\ell,h)}` | projected query-key KL cost | M396 | |
| `\bar D_{ij}^{(\ell,h)}` | bounded cost | M1114 | T2 (bar) |
| `D_{ij}(z)` | latent-dependent cost | S68 | T3 |
| `E` | associated vector bundle | M286 | |
| `E_c`, `E_{\mathcal I}`, `E_i`, `E_i^*` | fiber at context; pullback; token fiber; dual | M307, M312, M315, M543 | |
| `E_i^{(b)}` | block subspace `U_i\mathsf V_b` | M652 | T2 (superscript) |
| `E_{12}`, `E_{21}`, `E_{11}`, `E_{22}` | matrix units | M679 | T2 vs `E_i` |
| `\mathbb E` | expectation | M554 | |
| `e_{ij}`, `\bar e_{ij}` | link residual and its mean | S93-94 | T3 |
| `F_{i,h}` | processing factor `U_iO_hT_hU_i^{-1}` | M612 | |
| `\mathcal F_i` | row free energy | S70 | |
| `G` | structure group `\mathrm{GL}(K)`, later `\prod\mathrm{GL}(d_b)` | M270, M645 | T3 vs `G_i` |
| `G_i` | local metric `U_i^{-\top}U_i^{-1}` | M426 | |
| `\mathcal G(E)`, `\mathcal G(E_i)` | Gaussian statistical bundle and fiber | M288, M317 | |
| `\mathcal G_K` | Figure 1 fiber label, undefined | M164 | T2 |
| `H` | number of heads | M366 | T2 |
| `H_h^{\mathrm{cmp}}`, `H_h^{\mathrm{val}}` | comparison and content spaces | M368 | T3 |
| `H(q_i)` | differential entropy | M829 | T2 |
| `\mathcal H_\gamma` | ordered loop product | M596 | |
| `I_K`, `I_r`, `I_{r_h}`, `I_{s_h}`, `I` | identities | M547ff | |
| `\mathcal I` | token index set | M309 | |
| `J`, `J_i` | source label; label of receiver `i` | M690, S68 | |
| `\mathcal J_i^{(\ell,h)}`, `\mathcal J_{\mathrm{decode}}` | routing and readout objectives | M867, M814 | |
| `K` | state dimension; subscript: key role | M277; M377 | T3 |
| `L_{ij}` | generic link | M335, S92 | |
| `L_{ij}^{(h)}` | content link `U_iO_hT_hU_j^{-1}` | M62/444 | |
| `L_{ij}^{\mathrm{cmp}}` | comparison-induced link | M548 | |
| `L` | number of layers | M955 | T3 |
| `\mathcal L_{ij}` | declared link of a Gaussian channel | M622 | |
| `\mathcal L_\theta` | evidence lower bound | S61 | T3 |
| `M_h` | `O_hT_h` | M564 | |
| `N`; `\mathcal N` | number of positions; Gaussian | M309; M279 | |
| `O_h` | receiving (output) map | M381 | |
| `O` | concatenated output `[O_1\cdots O_H]` | M1051 | T3 |
| `o(\cdot)`; `o`, `o_a`, `o_i` | little-o; records | M1034; S56, S68 | T3 |
| `\mathcal P`, `\mathcal P_{\mathcal I}` | principal bundle; pullback | M272, M311 | |
| `P`, `Q` | generic laws in Eq (12) | M351 | T3 |
| `P_{K,j}` | key precision (ambient form) | M537 | |
| `P_i` | local source joint | M690 | T1 |
| `P_j` | projected key precision `V_{K,j}^{-1}` | M979 | T1 |
| `P_\theta(\cdot\mid o,X)`; `P_0` | posterior law; centering projector | S61; S117 | T3 |
| `Q_i` | channel noise covariance | M624 | T2 |
| `Q_{i,\beta}` | factorized recognition law | M691 | T1 |
| `Q`, `q`, `Q_Z` | recognition law, density, latent marginal | S61, S68 | |
| `R_{Q,i}` | Gaussian lift | M547 | |
| `R` | key-measurement noise covariance | M902 | T2 |
| `R_i`, `R_{j-i}` | RoPE rotations | M1058 | T2 |
| `R_i` | receiving covariance | S101 | T2 |
| `\mathsf R_{i,h}`, `\mathsf S_{j,h}` | receiving and sending endpoints | M430 | |
| `S_{Q,h}`, `S_{K,h}`; `S` | comparison maps; common map | M377; M400 | |
| `S_i` | allowed source support | M688 | T2 |
| `\overline S`, `\overline T`, `\overline O` | block-restricted maps | M654-657 | T2 (bar) |
| `\widetilde S_Q`, `\widetilde S_K` | whitened maps | M1009 | T3 |
| `T_h` | sending (value) map | M379 | |
| `U_i`, `U_i^{(b)}`, `U` | frame; block frame; generic frame | M62/307, M647, M681 | |
| `\mathcal U`, `\mathcal U_i` | contextual regions | M275, M298 | |
| `\mathsf V`, `\mathsf V_b` | reference space; block subspace | M277, M643 | |
| `V` | vocabulary size | M799 | T2 |
| `V` | random content `TX_j` | M902 | T2 |
| `V_{Q,i}`, `V_{K,j}`, `V_*` | projected covariances; shared key covariance | M974, M989 | |
| `V_{ij}` | residual covariance | S96 | T3 |
| `W_{\mathrm{embed}}`, `W_1`, `W_2`, `W_{\mathrm{out}}`, `W_V^{(h)}`, `W_O^{(h)}` | embedding, MLP, decoder, transformer matrices | M799, M933, M955, M1051 | |
| `W_j` | content-law covariances | M1069 | T3 |
| `\mathcal W_\gamma` | loop trace | M598 | |
| `X_{x_i}`, `Y_i` | token and positional frame generators | M357 | T2 |
| `X_i`; `X`; `X_j`; `X` | reference Gaussian vector; decoder latent; latent draw; structural data | M554; M828; M902; S54 | T2 |
| `Y` | noisy key measurement | M902 | T3 |
| `Z_i`; `Z` (in `p_\theta^Z`, `Q_Z`) | partition function; latent sector | M719; S54 | T3 |
| `a` | basis change | M386 | T2 |
| `a` | test vector | M400 | T2 |
| `a` | path length in `M_h^a` | M568 | T3 |
| `a_i` | projected query mean `S_Q\xi_i` | M681 (use), M973 (def) | T1 |
| `a_i^{(\ell,h)}` | head aggregate | M884 | T1 |
| `a_h` | ALiBi slope | M1109 | T1 |
| `a` | record index | S54 | T3 |
| `b` | point of `\mathcal B` in Eq (4); block index | M293; M643 | T3 |
| `b_\delta`, `b_{i-j}` | relative-position bias | M781 | T2 |
| `b`, `b_1^{(\ell)}`, `b_2^{(\ell)}`, `b_{\mathrm{out}}` | LayerNorm shift, MLP and decoder biases | M930, M933, M955 | T2 |
| `b_j` | projected key mean `S_K\xi_j` | M681 (use), M973 | T1 |
| `b_1`, `b_2` | counterexample key means | M1020 | T2 |
| `b_{ij}^{(h)}` | ALiBi logit bias | M1109 | T1 |
| `c`, `c^*`, `c_0` | context points | M307, M262, M309 | |
| `c` | correlation (examples); second block index; dilation scalar | M669, S110; M675; M681 | T3 |
| `c` | token type | M799 | T2 |
| `c_i` | row constant; label-independent factor | M1002; S68 | T3 |
| `d_b`; `d` | block dimension; transformer width | M643; M799 | T2 (`d` vs `K`) |
| `f` | f-divergence | M355 | |
| `g`, `g_i`, `g_b` | group element; site transformation; block factor | M281, M343, M646 | |
| `h`; `i,j,k`; `\ell` | head, site, and layer indices | M366; -; M364 | |
| `k_i`, `k_j` | latent vectors (channel, population) | M577, M624; S91 | T3 vs `\mathsf k_j` |
| `\ell_a` | record kernel density | S54 | T3 |
| `m_i`, `m_i^{(\ell)}` | routed message | M463 | |
| `m` | ALiBi slope | M764 | T1 |
| `n` | point of `\mathcal P` | M275 | |
| `p_i` | local prior | M303/323 | T1 |
| `p_i(j,y,z)` | local joint with content | M893 | T1 |
| `p_{K,j}` | key law | M393 | |
| `p_c` | prior-bank law of token type `c` | M801 | T2 |
| `p(v,x)`, `p(v\mid x)`, `\bar p_i` | decoder mixture, classifier, predictive average | M824, M845, M850 | |
| `p_\theta`, `p_{\mathrm{uni}}`, `p_{ij}` | sequence model; vocabulary prior; dot-product weights | M947, M956, M1026 | T3 |
| `p_\theta^Z`, `p_\theta(z,o\mid X)` | latent law; joint | S54, S56 | |
| `q_i`, `q_i^{(\ell)}`, `\widetilde q_i` | Gaussian state; per layer; reference form | M303, M364, M327 | |
| `q_{Q,i}` | query law | M390 | |
| `q_i^{(b)}` | block marginal | M665 | T2 |
| `q_i(0)` | initial state | M804 | T2 |
| `q_{i,\beta}` | recognition law with content | M894 | T1 |
| `r_h`; `r` | comparison dimension; walk length and `r=r_h` | M368; M594, M971 | T3 |
| `r_j(z)` | content laws | M891 | T2 |
| `s_h` | content dimension | M370 | |
| `u_i^{(\ell)}` | LayerNorm output | M930 | |
| `v`; `v`, `w` | vector in `\mathsf V`; vocabulary indices | M296; M812, M846 | T3 |
| `v_j^{(\ell,h)}`, `v_j`, `\bar v` | values; content means; mixture mean | M883, M1069 | |
| `w` | null vector; window size | M552; M750 | T3 |
| `x_i`; `x`; `x,y` | token; decoder latent point; metric vectors | M357; M824; M457 | T3 |
| `y`; `y_i` | comparison-space point; training target | M552; M1107 | T3 |
| `z` | content variable | M891 | T2 |
| `z_i^{(h)}` | head aggregate | M1045 | T1 |
| `z_i` | decoder logits | M1121 | T1 |
| `z`, `z_{\partial a}` | latent configuration | S54 | T3 |
| `\alpha` | unused | | available |
| `\beta_{ij}`, `\beta_{ij}^{(h)}`, `\beta_i`, `\beta_j`, `\beta^*` | routing probabilities | M257/424 | |
| `\gamma` | closed walk | M594 | T2 |
| `\gamma` | LayerNorm gain | M930 | T2 |
| `\Gamma` | smooth sections; population covariance | M303; S90 | T3 |
| `\delta`, `\delta_{ij}` | displacement; relative offset; logit perturbation | M552, M785, M1029 | T3 |
| `\varepsilon_i` | channel noise | M635 | T2 |
| `\varepsilon` | measurement noise | M902 | T2 |
| `\varepsilon_i` | bias bound | M1024 | T2 |
| `\epsilon` | LayerNorm regularizer | S119 | |
| `\eta,\zeta,\nu,\chi,\psi,\Lambda,\Xi,\Phi,\Psi` | unused | | available |
| `\iota`, `\iota_b` | constant map; block inclusion | M309, M652 | T3 |
| `\kappa_{\mathrm{uni}}`, `\lambda_i` | log-prior weight; multiplier | M956, M709 | |
| `\mu_i`, `\mu_{p,i}`, `\mu_i^{\mathrm{att}}`, `\boldsymbol\mu` | means; prior mean; residual; population mean | M322, M323, M886, S90 | |
| `\mu_p^c`; `\mu_{p,v}` | prior-bank mean, two index placements | M801; M832 | T2 |
| `\xi_i` | reference mean | M329 | |
| `\pi` | bundle projection; constant in `\log2\pi` | M272; M837 | T3 |
| `\pi_{ij}`, `\pi_i`, `\pi_{ij}^{(h)}`, `\pi^0_{ij}`, `\pi_i` (label prior) | source priors | M424/688, M1013, S68 | |
| `\pi_j`, `\pi_k` | source prior with receiver suppressed | M729, M735 | T1 |
| `\pi_v`, `\pi_w`, `\pi_0`, `\pi_1` | Gaussian class templates | M812, M850 | T1 |
| `\rho` | Gaussian action; defining representation | M281; M646 | T2 |
| `\rho_i`, `\rho_{iv}` | categorical readout | M812 | T1 |
| `\sigma_i`; `\sigma_h^2`; `\sigma^2` | local section; comparison variance; ambient variance | M298; M681; M1009 | T3 |
| `\Sigma_i`, `\Sigma_{p,i}`, `\Sigma_i^{(b)}` | covariances | M322, M323, M662 | |
| `\Sigma_p^c`; `\Sigma_{p,v}` | prior-bank covariance, two index placements | M801; M832 | T2 |
| `\tau`, `\tau_h`; `\tau_{\mathrm{dec}}`; `\tau_i` | routing temperature; readout temperature; per-row temperature | M424/702; M816; S68 | T2 (`\tau_i`) |
| `\phi_i`; `\phi_c` | single-exponential generator; token frame coefficients | M580; M801 | T2 |
| `\theta`; `\Theta_{ij}` | parameters; connection transport | M947; M432 | |
| `\Omega_{ij}`, `\Omega_{ij}^{(b)}` | flat reference identification | M63, M666 | |
| `\omega`, `\omega_v` | class prior | M816 | |
| `\mathfrak{gl}`, `\mathfrak{sl}`, `\mathfrak m` | Lie algebras; off-block complement | M671-677 | |
| `\mathsf q_i`, `\mathsf k_j` | whitened query and key | M989 | T3 |
| `\mathbf 1[\cdot]`; `\mathbf 1` | indicator; all-ones vector | M743; S117 | T3 |
| `\lvert\cdot\rvert` | absolute value; determinant | M753; M837 | T2 |
| `\operatorname{Tr}`; `\operatorname{tr}` | trace, two spellings | M598; M835 | T2 |
| `\operatorname{LayerNorm}_{\gamma,b}`; `\operatorname{LN}_\epsilon` | LayerNorm, two names | M930; S120 | T2 |
| `(\cdot)_*`, prime, tilde, star | pushforward; transformed quantity; reference/whitened; optimum, shared, dual, context | M327, M448, M327/1009, M712/989/543/262 | T3 |

## Collision list and proposed renaming scheme

The scheme keeps every symbol of Table 1 except `\mathcal C_{ij}`, keeps `\mathcal C` for the contextual base as in the broader theory (`gauge_vfe_rg/02_geometry.tex:17`), and uses only glyphs that are currently unused (`\alpha`, `\eta`, `\Lambda`, `\nu`, `\psi`) or unambiguous fonts (`\mathbb P`, `\mathbb Q`, `\mathbb H`, `\mathcal M`, `\mathcal S`).

Required (T1):

| # | Current | Where | Proposed | Reason |
|---|---|---|---|---|
| R1 | `a_i^{(\ell,h)}` (head aggregate) | Eq 68-69; Alg 1 steps 8, 10 | `z_i^{(\ell,h)}` | Eq 87 already uses `z_i^{(h)}`; frees `a_i` for Sec 4 |
| R2 | `m` (Eq 54-55, l.775), `a_h` (Alg 1) | 2.6.1, Alg 1 | `\alpha_h` | one name; frees `m` (message) and `a` |
| R3 | `b_{ij}^{(h)}` | Alg 1 steps 2, 7 | `\log\pi_{ij}^{(h)}` | the algorithm then uses Eq 66's object |
| R4 | `z_i` (logits) | Alg 1 step 14 | inline, no symbol | avoids clash with R1 |
| R5 | `P_i`, `Q_{i,\beta}`; `p_i(j,y,z)`, `q_{i,\beta}` | Eq 44-47; Eq 71-73 | `\mathbb P_i`, `\mathbb Q_{i,\beta}` in both | frees `p_i` (Table 1) and `P_j` |
| R6 | `\pi_v`, `\pi_w`, `\pi_0`, `\pi_1` | 2.8 | `p_v`, `p_w`, `p_0`, `p_1` (prior-bank laws) | `\pi` is the categorical prior elsewhere |
| R7 | `\rho_i`, `\rho_{iv}` | 2.8 | `\hat p_i(v)` | `\rho` is the representation; contrasts with `\bar p_i` |
| R8 | `B_{ij}` in `\mathcal H_\gamma(B)`, `\mathcal W_\gamma(B)` | l.594, Eq 33-35 | `L_{ij}` | `B_{ij}` is not composable |
| R9 | `\mathcal C_{ij}`, `\mathcal C_{ij}^{(h)}`; `A_{ij}` | Table 1, Eq 21-22, 36, 75 | `\mathcal M_{ij}`, `\mathcal M_{ij}^{(h)}`; `M_{ij}:=\sum_h\beta_{ij}^{(h)}M_h` | frees `\mathcal C` (base) and `A` (measurements); `\mathcal M_{ij}=U_iM_{ij}U_j^{-1}` (T2 by the legend; listed here because it edits a Table 1 row) |
| R10 | `\pi_j`, `\pi_k` | 2.6.1 | `\pi_{ij}`, `\pi_{ik}` | receiver dependence explicit |
| R11 | `a_i`, `b_j` at l.681 | 2.5 | `S_Q\xi_i`, `S_K\xi_j` | used before definition |

Recommended (T2):

| # | Current | Proposed |
|---|---|---|
| R12 | `H(q_i)` | `\mathbb H[q_i]` |
| R13 | `Q_i` (Eq 38), `R` (Eq 74), Supp `R_i` (S6) | `\Lambda_i`, `\Lambda`, `\Lambda_i` (noise covariances); keep `R_i` for RoPE and `R_{Q,i}` for the lift |
| R14 | `\varepsilon_i` (l.635), `\varepsilon` (Eq 74) | `\eta_i`, `\eta`; keep `\varepsilon_i` for the bias bound |
| R15 | LayerNorm `(\gamma,b)` | `(\gamma_{\mathrm{LN}},b_{\mathrm{LN}})`, and one operator name `\operatorname{LN}` in both documents; keep `\gamma` for walks |
| R16 | `X_{x_i}`, `Y_i`, `\phi_c`, `\phi_i` | `\phi_{x_i}`, `\psi_i` (token and position generators), `\phi_v` in the prior bank |
| R17 | token type `c`; `\mu_p^c,\Sigma_p^c,p_c`; `q_i(0)=p_{\mathrm{token}(i)}` | `v`; `\mu_{p,v},\Sigma_{p,v},p_v`; `q_i^{(0)}=p_{x_i}` |
| R18 | `S_i` (support) | `\mathcal S_i` |
| R19 | `r_j(z)` | `\nu_j(z)` |
| R20 | test vector `a` (l.400) | `y\in\mathbb R^{r_h}` |
| R21 | `E_{12}` etc. | `e_{12}` etc. (matrix units) |
| R22 | block superscripts `(b)` | `[b]`: `q_i^{[b]}`, `\Sigma_i^{[b]}`, `U_i^{[b]}`, `\Omega_{ij}^{[b]}`, `E_i^{[b]}` |
| R23 | vocabulary size `V`; width `d`; random `V=TX_j` | `\lvert\mathcal V\rvert`; `K`; write `\mathbb E[TX_j\mid Y=y,J=j]` |
| R24 | Supp `\tau_i`; `\operatorname{tr}`; `\log\lvert\Sigma\rvert`; Figure 1 `\mathcal G_K` | `\tau_h` (or say the row index includes the head); `\operatorname{Tr}`; `\log\det`; `\mathcal G(E_c)` |

Acceptable as is (T3): `\pi` bundle projection vs `\pi_{ij}` (2.1 only); `\sigma_i` section vs `\sigma_h^2`; `G` group vs `G_i`; local dummies `w`, `\delta`, `c` in examples, `a` path length; `k` summation vs `k_j` latent vs sans-serif `\mathsf k_j`; main `\Gamma` vs Supp `\Gamma`; `\ell` vs Supp `\ell_a`; `o(\cdot)` vs Supp `o`; `y` vs `y_i`.

## Citation audit

Main cites 33 keys, the supplement 3 (`Bishop2006`, `Blei2017`, `ba2016layernorm`); all exist in `references.bib` and BibTeX reports no warnings.

| Key (where) | Claim or pinpoint in the text | Primary source checked | Outcome |
|---|---|---|---|
| Blei2017 (824; Supp 66) | Sec. 2.4, Eqs. 17-18: expected-log coordinate update | arXiv 1601.00670 final version: Sec. 2.4 "Coordinate ascent mean-field variational inference", Eq. (17) and (18) are `q_j^*\propto\exp\{\mathbb E_{-j}\log p(\cdot)\}` | correct; add Sec. 2.2 Eq. (14) at Supp 66 |
| vaswani2017attention (1036, 1051) | Sec. 3.2.1 scale `\sqrt{d_k}`; Sec. 3.2.2 Concat and `W^O` | arXiv 1706.03762 | correct |
| fuchs2020se3 (683) | Sec. 2.3 and App. D.3: irreducible types, invariant attention, equivariant values, heads partition channels | arXiv 2006.10503 | App. D.3 correct; invariant attention and equivariant values are Sec. 3.2 (Eqs. 10-11), not 2.3 (E16) |
| He2021GaugeEquivariantTransformer (683) | Secs. 4.1-4.2: gauge-equivariant multi-head attention; regular fields and irrep decomposition | NeurIPS 2021 PDF: 4.1 "Gauge Equivariant Self-Attention Layers", 4.2 "Extension of Regular Representation" | correct |
| Wetterich2014LinearLattice (71, 615) | linear lattice gauge theory admits general matrix links | arXiv 1307.0722 abstract: links are "arbitrary complex or real N x N matrices"; gauge groups are SU(N) x U(1) or SO(N) | correct; line 615's "compact-group action" is accurate; line 71's "such covariant matrices" should add that the covariance group here is `\mathrm{GL}(K)`, not compact |
| Bae2022ProAttention (67) | Gaussian query/key statistics, negative KL, value aggregation | IEEE Access full text | correct; statistics are a univariate mean and standard deviation per projected token (E9) |
| culver1966existence (357) | real exp not a global chart; products need not have real logarithms | Culver (1966), Theorem 1 (real log iff nonsingular and each negative-eigenvalue Jordan block occurs an even number of times) | supports the criterion; the product statement follows from it. Recomputed example (`culver_check.py`): `e^{\pi J}e^{N}=\left(\begin{smallmatrix}-1&1\\0&-1\end{smallmatrix}\right)` with `J` the rotation generator and `N` a nilpotent, determinant 1, one Jordan block at -1, principal logarithm complex, hence no real logarithm |
| press2022train (775) | one-sided penalty `-m(i-j)`; slopes geometric with first term and ratio `2^{-8/H}` | arXiv 2108.12409, Sec. 3 | correct ("In general, for n heads ... starts at `2^{-8/n}` and uses that same value as its ratio") |
| Singh2023ImplicitStructuralInference (67) | attention as structural inference | NeurIPS 2023 abstract | correct; also a precedent for 2.6.1 (E9) |
| Singh2023MarginalProbability (67) | marginalization view | arXiv 2304.04556 abstract | correct |
| Kim2017StructuredAttention (67) | probabilistic inference in attention | arXiv 1702.00887 (ICLR 2017) | correct |
| Deng2018LatentAlignment (67) | latent alignment | arXiv 1807.03756 | correct; precedent for 2.6 (E9) |
| Bahuleyan2018VariationalAttention (67) | grouped with "latent-alignment methods" | arXiv 1712.08207 | the paper models the attention vector as a Gaussian latent variable; it is variational attention, not latent alignment; reword the grouping |
| Amari2016 (355) | KL invariance under invertible maps | Springer TOC: Ch. 3 "Invariant Geometry of Manifold of Probability Distributions" | topic confirmed; section-level pinpoint not verified (no full text) |
| petersen2012matrix (902) | Gaussian conditioning | Matrix Cookbook (Nov 15, 2012) Sec. 8.1.3, Eq. (353) | correct; Eq. (380) also supports Eq (62) and S6 |
| ba2016layernorm (Supp 117) | LayerNorm definition | arXiv 1607.06450, Sec. 3 | correct (the `\epsilon` term is the implementation variant) |
| Boyd2004, Wainwright2008 (720) | entropy-regularized value `-\tau\log Z` | Boyd and Vandenberghe Example 3.25 read; Wainwright and Jordan PDF not retrievable | Boyd correct (add Example 3.25); Wainwright and Jordan not verified |
| Bishop2006 (635, 841; Supp 108) | affine-Gaussian and cross-entropy identities | not re-read | standard; pinpoint Sec. 2.3.3 suggested |
| remaining keys (Wilson, Cohen, Bronstein, Tsai, Katharopoulos, Ramsauer, Sengupta x2, Nakahara, Frankel, Radford, Beltagy, Jiang, Raffel, Su) | general attributions | metadata via Crossref/proceedings where available | consistent; see E17 for entry errors. Raffel et al. (arXiv 1910.10683, Sec. 2.1) use 32 scalar logit biases with ranges "that increase in size logarithmically up to an offset of 128", so "a (learnable) bias for relative offset `\delta`" at 785 should read "a learned bias shared within logarithmic offset buckets" |

## Layout and document-organization metrics

| Quantity | Value |
|---|---|
| Pages | main 31 (body pp. 1-28, references pp. 28-31); supplement 4 (text pp. 1-3, references p. 4) |
| Section spans | Sec 2 pp. 3-17; Sec 3 pp. 17-20; Sec 4 pp. 20-23; Sec 5 pp. 23-26; Sec 6 pp. 26-27; Sec 7 pp. 27-28 |
| Prose words (math excluded) | front 219, Intro 599, Sec 2 about 4,250, Sec 3 782, Sec 4 1,129, Sec 5 788, Sec 6 548, Sec 7 196; supplement about 1,080 |
| Display environments | main 70 (Sec 2: 52), numbered equations 89, cited by number 20; supplement 7 environments, 8 numbered |
| Formal environments | Lemma 1 (p. 10, uncited), Proposition 2 (p. 19, unlabeled), Proposition 3 (pp. 20-21) |
| Floats | Figure 1 `[H]` p. 3; Table 1 `[t]` p. 7; Figure 2 `[htbp]` p. 9 (body-uncited); Table 2 `[t]` p. 23 (uncited); Algorithm 1 `[t]` p. 24; Table 3 `[H]` p. 25 (uncited) |
| Underfull pages | 2, 3, 9, 24, 25 (faithful); 2, 3, 23, 25, 27 with `[tbp]` and no barriers (test) |
| Negation sentences | main 114/591 (19%); Contribution and Limits 7/13; supplement 15/71 |

## Leads tested

**L9 (notation): CONFIRMED and extended.** Every collision listed in the lead exists as stated: `P_i` (Eq 44) vs `P_j` (Eq 81); `\mathcal C` base vs `\mathcal C_{ij}`; `R_{Q,i}`, RoPE `R_i`, Supp `R_i`, noise `R`, `\mathsf R_{i,h}`; `V`, `\mathsf V`, `V_{Q,i}`, `V_{ij}`, `V=TX_j`, `V_*`; `a_i` (query), `a_i^{(\ell,h)}` (aggregate), `a_h` (slope), `a` (basis change), `a` (path length); slope `m` vs `a_h`; `\pi_v` templates vs `\pi_{ij}`; `\rho` representation vs readout; `\sigma_i` vs `\sigma_h^2`. Two refinements: `\sigma_i`/`\sigma_h` and `a` (path length) are locally scoped and low risk (T3), while `\pi_v`/`\omega` is worse than stated because `\omega` takes over the categorical-prior role. New collisions not in the lead: `B_{ij}` composability trap (E4), `A_{ij}` vs `A_{K,j}`, Table 1's `p_i` redefined in Eq (71), aggregate renamed `z_i^{(h)}` and `z_i` logits, `b` family, `\gamma`, `\varepsilon_i`, `X`, `S_i`, `r_j`, `E_{12}`, block superscripts, `a` basis vs test vector within 14 lines, Supp `\tau_i`, `q_i(0)`, `\mu_p^c` vs `\mu_{p,v}`, `a_i,b_j` used before definition, and operator spellings. Renaming scheme R1-R24 above.

**L10 (organization/prose): MODIFIED.** Negations are frequent but do not dominate: 19% of main-text sentences contain an explicit negation and about 9% are negated scope disclaimers by a verb heuristic; the concentration is in Contribution and Limits (7 of 13) and Section 5.2. The actionable defect is repetition (three disclaimers restated five or six times each and the passive-covariance conclusion stated three times, E10) and the absence of numbered statements for the central results (the three formal environments are not the Gibbs optimality, endpoint law, rank bound, KL additivity, or bias bound). A theorem-first spine is supported as organization (E10). Whether the results are "individually elementary" is outside this lens and was not assessed.

**L8 (missing precedents): CONFIRMED at the bibliographic and content level.** Niculae and Blondel 2017 (arXiv 1705.07704; negative-entropy regularizer gives softmax), Martins and Astudillo 2016 (arXiv 1602.02068), Kim, Papamakarios and Mnih (arXiv 2006.04710; L2 self-attention), Movellan and Gabbur (arXiv 2010.15583; MAP inference in a Gaussian-mixture "Probabilistic Transformer"), Sukhbaatar et al. 2019 (arXiv 1907.01470), Geva et al. (arXiv 2012.14913) all exist with the stated authors and topics. Gabbur et al. 2021 (NeurIPS) was not fetched: could not verify. Singh and Buckley 2023a, already in the bibliography, is the closest precedent for 2.6.1 (E9).

**L2 (literature only, citation lens):** the dressing-field reference named in the brief is misattributed to J. Math. Phys. Crossref: Fournel, François, Lazzarini, Masson, "Gauge invariant composite fields out of connections, with examples", Int. J. Geom. Methods Mod. Phys. 11 (2014) 1450016, doi 10.1142/S0219887814500169. Verified: Attard, François, Lazzarini, Masson, "The Dressing Field Method of Gauge Symmetry Reduction, a Review with Examples", in Foundations of Mathematics and Physics One Century After Hilbert (Springer, 2018), pp. 377-415, doi 10.1007/978-3-319-64813-2_13; Norton, Rep. Prog. Phys. 56(7):791-858 (1993), doi 10.1088/0034-4885/56/7/001; Kretschmann, Ann. Phys. 358 (4th ser. 53):575-614, doi 10.1002/andp.19183581602 (Crossref issue date January 1918; conventionally cited 1917). The substance of L2 is outside this lens.

**L1, L3, L4, L5, L6, L7:** outside the editorial lens; not tested. For L7 only: `eq:projected_softmax_bound` is labeled but never cited, so a sharpened bound can replace it without breaking references.

## Reproduction

Scripts in `scratchpad/panel/`: `labels.py`, `symbols.py`, `displaypunct.py`, `wordcount.py`, `negations.py`, `underfull_pages.py`, `culver_check.py`; builds in `build/` (faithful) and `build_exp/` (layout test: `subcaption` removed, `[H]`->`[tbp]`, both `\FloatBarrier` removed); primary-source PDFs and text in `src/`; outputs in `editorial_evidence/`.
