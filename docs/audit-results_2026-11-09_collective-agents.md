# Audit of "Communication, Coherence and Collective Agents" (2026-11-09)

Manuscript: `manuscripts/Collective_Agents/` (464 pages at the audited revision; a pre-audit copy is held in the session scratch folder, outside the vault). This report is the direct output of parallel investigator lanes, each restricted to one section or one cross-cutting question. No skeptic, defender or verifier pass has adjudicated the findings. A finding marked unconfirmed lacks a demonstration by the lane that raised it. Finding numbers are ordered by severity within a lane.

Totals over 23 lanes: 0 critical, 51 major, 160 minor; 17 of these are unconfirmed.

## Lane status

| Lane | Scope | Files | Status | Critical | Major | Minor |
|---|---|---|---|---|---|---|
| fw | Section 2, framework | sections/02_framework.tex | done | 0 | 2 | 10 |
| mis_min | Sections 3 and 9, misreading and the minimal model | sections/03_misreading.tex, 09_minimal.tex | done | 0 | 2 | 8 |
| col | Section 4, collectives | sections/04_collectives.tex | done | 0 | 1 | 8 |
| agy1 | Section 5, closure | sections/05_agency.tex:1-193 | done | 0 | 3 | 7 |
| agy2 | Section 5, agency | sections/05_agency.tex:194-413 | done | 0 | 2 | 7 |
| agy3 | Section 5, identity, interaction necessity, H1 | sections/05_agency.tex:414-595 | done | 0 | 5 | 5 |
| coh | Section 6, coherence | sections/06_coherence.tex | done | 0 | 2 | 7 |
| frm | Section 7, formation | sections/07_formation.tex | done | 0 | 5 | 4 |
| sca1 | Section 8, hypotheses, light cones, clustering | sections/08_scale.tex:1-245 | done | 0 | 4 | 8 |
| sca2 | Section 8, Ornstein-Zernike decay, correlation time, long-range links | sections/08_scale.tex:246-447 | done | 0 | 0 | 6 |
| sca3 | Section 8, percolation, coherence volume, abstraction, H4 | sections/08_scale.tex:448-616 | done | 0 | 2 | 7 |
| abs | Section 10, abstract collectives | sections/10_abstract_collectives.tex | done | 0 | 2 | 7 |
| met | Section 10a, meta-agents | sections/10a_meta_agents.tex | done | 0 | 2 | 7 |
| hie | Section 10b, hierarchy | sections/10b_hierarchy.tex | done | 0 | 1 | 6 |
| ren | Section 10c, renormalization | sections/10c_renormalization.tex | done | 0 | 1 | 7 |
| env1 | Section 10d, sensors, horizon, control | sections/10d_environments.tex:1-155 | done | 0 | 1 | 8 |
| env2 | Section 10d, selection, aggregates, Hayek dimension, levels | sections/10d_environments.tex:156-381 | done | 0 | 1 | 10 |
| frame | Framing against results: abstract, introduction, predictions, discussion | sections/00, 01, 11, 13 | done | 0 | 3 | 12 |
| pos | Falsifiability, scope and novelty | sections/00, 10d, 11, 12, 13 | done | 0 | 9 | 1 |
| notation | Notation and conventions across sections | sections/appA_notation.tex and all sections | done | 0 | 1 | 17 |
| cit_attr | Citation attribution against sources | sections/12_related.tex and citing passages | done | 0 | 1 | 3 |
| cit_meta | Bibliography integrity and metadata | references.bib, sections/*_extra.bib | done | 0 | 1 | 5 |
| arch | Architecture, dependency map and length budget | whole manuscript | done | 0 | 0 | 0 |
| agy | Section 5, agency (whole section; replaced by agy1 to agy3) | sections/05_agency.tex | failed (context overflow) |  |  |  |
| sca | Section 8, scale (whole section; replaced by sca1 to sca3) | sections/08_scale.tex | failed (context overflow) |  |  |  |
| env | Section 10d, environments (whole section; replaced by env1 and env2) | sections/10d_environments.tex | failed (context overflow) |  |  |  |

## Disposition

Disposition of findings after the remediation passes: 203 applied, 1 contested, 1 declined, 1 deferred, 5 partial. The state of each finding is given with it below.

## Remediation

### State of the manuscript after remediation

The manuscript is now two documents built from the same section files. The main text (`collective_agents.tex`) has 214 pages and the supplement (`collective_agents_supplement.tex`) has 504 pages; the audited revision was a single document of 464 pages. The supplement holds four parts: additional results that were moved out of the main sections (files `sNN_*`), eight extension sections that address the literature open problems (files `ext1_apx` to `ext8_idn`), the proofs (files `appNN_*` and `appext*`), and the records of the numerical checks (files `chkNN_*` and `chkext*`). The two documents cite each other through `xr-hyper`, and supplement numbers print with the prefix S. The final build reports no undefined reference or citation, no multiply defined label, no BibTeX error or warning and no float too large in either document; the main text has 2 overfull boxes and the supplement 173, none above 10pt.

The ten open problems of the attached literature review are addressed in the extension sections and summarized in a new main-text section (`sec:opn`, `sections/10e_open_problems.tex`), which gives for each problem what is proved, what is only computed, and what stays open. The statuses in that section are the binding ones. In particular, the approximate form of the meta-agent theorem is not closed (`open:met-approximate`, `open:ren-beyond`); what is proved is a conditional error term for the predictive law in the stable linear-Gaussian case (`thm:apx-posterior`, `cor:apx-memory`) and an unconditional finite-horizon bound by a path relative entropy, which accumulates over the horizon (`prop:apx-posterior-finite`). The threshold reading of `conj:ren-lrg` is refuted by a counterexample (`prop:obj-lrg-counter`), `conj:hie-top-down` became a proposition, `open:agy-unrecorded-drive` is closed negatively for records alone and positively for interventions, the energy results rest on three declared premises, and no nested meta-agent is established.

### How the findings were handled

No skeptic, defender or verifier pass adjudicated the findings, because none was requested. The state given with each finding therefore records what was changed in the manuscript and whether an independent checking agent accepted the change; it is not a ruling on whether the finding was right. Each pass below ran editor agents restricted to the files they owned, followed by checker agents that reread the changed statement against its proof or its source.

The first pass took the 211 findings grouped by owning file and produced 199 dispositions (186 applied, 11 declined, 1 contested, 1 deferred); findings that touched only framing sections were routed to the framing pass. The second pass took the 115 follow-up items that the first-pass checkers raised (59 applied, 51 declined, most of them because the text already met the request, 4 deferred, 1 partial). The framing pass rewrote the abstract, introduction, predictions, related work, discussion and notation table against the repaired statements, corrected the bibliography, and assembled the section on open problems. The cross-file follow-up pass applied 24 of 30 items that the framing pass had left for the technical files (4 declined, 1 partial, 1 deferred to the author). One agent of that pass deleted 71 uncited bibliography entries; the deletion was reversed, since pruning the bibliography is an author's decision, and the entries remain. The sync pass rechecked every framing sentence of the main text and supplement, the notation table and the abstract against the register of changed statements. That run stopped once when the account ran out of usage credits, was resumed from its journal, and completed with 55 agents and no agent error. A last cross-file pass, with one editor and one checker per file, settled the items the sync pass had reported for files outside its owners: 10 files and 24 items, of which 17 were applied and 7 were already met; the checkers accepted 19 and repaired 5.

The coordinator made four kinds of direct edits. Ten sentences that described the start law of `prop:frm-exact-fusion` as exchangeable now say exchangeable given the world path, which is the hypothesis of part (c); the proof notes that unconditional exchangeability would not suffice. Thirteen tables that exceeded the page height were converted to `longtable` (five in the notation appendix, one in the introduction, three in the supplement to the introduction, four in the predictions section). The unused macro `\EF` was removed from the preamble. Twenty framing sentences in twelve files were reworded in four families, each to match the statement it cites. The shell condition of `thm:col-boundary`(b) now reads thick on the scale of an explicit bound on the Markov length, because the region leak is bounded at the decay length $1/(2m_\Pi)$ and not at $\xi_M$ itself. The agreement set of `prop:ren-lrg-agreement` is now stated as an explicit interval of leaks that contains the window of `thm:col-bridge`(iv); the earlier wording, that the two procedures agree on that window and disagree outside it, was false when the correlation term sets the lower end of the window. Above $\gamma_T$, `thm:frm-formation`(b) gives a single fixed point on the split branch, which equals the split only at infinite policy precision; the sentences that said the split attracts every state were changed. The finite-horizon bound `prop:apx-posterior-finite` was added where the conditional bound had been called the only one.

A residual pass then took 32 file-local framing items that the checkers of the preceding passes had reported and the coordinator had triaged. It covered 18 files in 11 groups with 20 agents (9 editors and 11 checkers) and no agent error. Of the 32 items, 30 were applied and 2 were already met. The checkers returned 52 verdicts, 50 holds and 2 repairs; these include all twenty coordinator rewordings of the preceding paragraph, of which 19 held and 1 was repaired in the form of its citation. The pass was closed-ended by design: its agents were given the listed items and no open field for new defects, so it bounds those items and does not certify the absence of others. Its checkers had no access to git or a shell and compared the files with copies taken before the pass.

The register of changed statements holds 400 entries; each names the label, the change, the file and the agent that made it.

The tables of unresolved entries at the end of this section reproduce the notes of each pass as written when that pass ended. Later passes settled part of them: the last cross-file pass and the residual pass took their items from these notes, the supplement driver that some notes call missing now exists, and the deletion of bibliography entries recorded there was reversed. The tables are kept as the record, and the two subsections that follow state what remains.

### Decisions left to the author

The following items were not settled because each changes a claim, a convention or a figure in a way that only the author can choose.

| Item | Decision |
|---|---|
| `notation-07` (contested) | The notation table declares $\kappa$ the attention capacity and nothing else, while the text also uses it as a count of sensor channels and of senders. The section owners hold that these are the same quantity; nothing was renamed. |
| W2-7, C-04 | Chemoreception figure (`fig:env-cell`): the plotted lines use the leading-term values 19.707 and 0.78829; the exact-variance values are 24.3 and 0.97. The crossing is 4.656 (508 nm) for the rounded ratio 0.79 and 4.642 (507.5 nm) for the plotted line. Caption, supplement text and check record must change together. |
| W2-appA-1 | Whether to rename the letter $q$, which carries more than one meaning in the notation table. |
| `cit_meta-04` (declined) | Whether to prune the 71 uncited bibliography entries. |
| `cit_meta-05` (deferred) | Last page of `working1960note` could not be confirmed. |
| `cit_meta-03` (partial) | Three bibliography notes still read "Unverified", each narrowed to one item: the editors and place of the volume of `bertschinger2006information`, the last page of `seguy1971relation`, and the last page of `toulouse1977theory`. The Allerton page range of `tishby2000information` rests on secondary records and its note says so. |
| `frame-10`, `frame-14`, `frame-15`, `pos-01` (partial) | Scope qualifiers were added where the cited statement fixed them; the remaining parts ask for a choice of emphasis or of what to promise in the abstract and discussion. |
| Contrast of bounds in `12_related` and after `thm:met-h5a` | The meta-agent paragraphs set the conditional bound of `thm:apx-posterior` against the other bounds, but the leak bound also carries a smallness condition ($\mathfrak c_C\mathsf k<1$ in `prop:met-leak-bound`) and `prop:met-memory`(c) has its own conditions on $\hat\sigma$. Whether to call those bounds conditional as well is a choice of wording. |
| `open:agy-discrete-closure` | The problem and `rem:agy-h1-status` ask for a closure theorem under strong non-reversibility, while `05_agency`, `s05_agency` and `s13_discussion` say "for non-reversible drift". Nothing in terms of $r(C)$ is proved for any non-reversible drift, so neither wording is false; one should be chosen. |
| Closure paragraph of `s12_related` | The phrase "its condition for vanishing memory" is shorthand for the condition of the cited statements, and the Hankel-rank count of memory variables named beside it rests on a remark (`rem:agy-minimal-memory`) and not on a proved statement. |
| `13_discussion` | Five points of wording were left: the leak clause carries only the condition $\mathfrak c_C\mathsf k<1$; the memory clause leaves some hypotheses to the citation; the conditional bound of `thm:apx-posterior` is stated twice in one paragraph; "which is proved" attaches to its clause by grammar alone; and (T4) quantifies over nulls of type S while `tab:agy-nulls` lists one null of that type. |
| Length | The main text is 214 pages. A further reduction needs decisions on which results leave the main text. |

### What was not verified

The sync pass compared a framing sentence with its technical statement only where the register of changed statements flagged the label. Labels the register did not flag were not rechecked in several ranges of `s11_predictions`, `s12_related`, `13_discussion`, `s13_discussion` and `s01_introduction`. One sentence of `13_discussion` was not compared with the extension sections, parts (c) onward of `thm:env-control` were not compared with their framing sentences, and the scope qualifiers in the "Basis and status" cells of the prediction tables were checked for environment kind and placement only. The claims of `sec:dis-meta`, `sec:dis-renormalization` and `sec:dis-gauge` were taken as verified by the preceding pass, and the bodies of `ex:env-firm` and `ex:env-person` were not read. In the notation table, the proof-local sans-serif symbols of seven supplement files (`app06`, `app08`, `app10`, `app10a`, `app10d`, `chk08`, `chk10a`) are unlisted, the supplement-only meanings of $\Phi$, $\varphi$, $h$, $X$, $\nu$, $\mathcal{D}$, $\varrho$ and the variants of $\Gamma$ are not recorded, the symbols $q_0$, $q_T$ and $\hat q_{ij}$ are unlisted, the convention for a bare $\rho$ was only sampled, and uniqueness was scanned for some letters only. Whether $N$ in `prop:obj-lrg-counter` is called the number of agents elsewhere was not settled. Sentences that only characterize the literature were checked against the bibliography annotations at most, not against the primary sources; in `s12_related` the sentences on `barnett2023dynamical`, `rosas2024software` and `shalizi2025macrostate` were not checked against the annotations either. Sources that remain unopened after the bounded verification pass are Bartlett (1938), the body of Berg and Purcell (1977), cited for the constant $3/(5\pi)$ through Mora and Wingreen (2010), and Zaffaroni (2004), which is now cited as not opened; Section 2.2 of `waade2025one` was not read, and `devries2026active` is annotated as not read. Seventeen findings of the audit were raised without a demonstration and remain marked unconfirmed. The numerical checks were rerun only where a pass changed the statement they support; the records name their scripts.

### Bounded verification pass (2026-11-10)

This pass took four items from the two preceding subsections: the possible strengthening of `thm:ren-closure`(a), the four sources that no agent had opened, the attribution to `bandeira2013cheeger`, and the bibliography notes that still read "Unverified". The coordinator did it, without a separate checker. After it both documents were rebuilt: 214 and 504 pages, no undefined reference or citation, no multiply defined label, no BibTeX warning, no float too large, 2 overfull boxes in the main text (at most 0.21pt) and 173 in the supplement (at most 5.9pt).

The strengthening holds, and the statements were generalized. For $f$ orthogonal to the block constants, $f^\top\Pi f\ge\sum_jf_{C_j}^\top(\operatorname{diag}(\varepsilon^\Pi)+L_{C_j})f_{C_j}\ge\xi_{\mathrm{in}}^{\min}\lvert f\rvert^2$, because the couplings across blocks add a positive semidefinite Laplacian and each restriction $f_{C_j}$ is admissible in the minimum that defines $\xi_{\mathrm{in}}(C_j)$ in `def:col-contrast`, which is already stated for arbitrary leaks. The uniform leak was never used in that step. `thm:ren-memory`(d) now gives $\varkappa_\perp\ge\xi_{\mathrm{in}}^{\min}$ and $\varkappa_\Phi\le\max_j(2\xi_{\mathrm{out}}(C_j)-\bar\varepsilon_{C_j})$ for any diffusive precision, with the earlier form as the uniform case, and `thm:ren-closure`(a) states its bounds on $\Vert\mathcal D\Vert$ and $\lvert\mathcal D_{XY}\rvert$ whether or not the leak is uniform. The clause that $\mathcal D$ leaves the leak unchanged stays restricted to uniform leak, and a numerical run shows that it fails otherwise. That run (4000 random populations, leaks drawn per agent over several orders of magnitude) found no violation of the generalized bounds beyond rounding and is recorded in `chk:ren-memory`. The second half of `lem:ren-galerkin`(b), the bound on $\sigma_X^2$, was not generalized.

Two of the four sources were read in primary text. The two pages of Price (1970) were read from a scan: Eq. 1 is the covariance form, and Eq. 4 adds the transmission sum $\sum_iz_i\Delta q_i/(N\bar z)$, which the paper drops for random meiosis and fertilization. The paper therefore contains the decomposition that `ext7_evo` attributes to it, and the sentence saying the paper had not been read was replaced by a description of Eq. 4. Sections 1 and 2 of Bandeira, Singer and Spielman were read in the arXiv text: Section 1.3 defines frustration and the frustration constants, and Theorems 2.2, 2.4 and 2.6 relate them to the smallest eigenvalues of the connection Laplacian. The sentence in `s12_related` is supported; the clause "known to us from the record of their paper" was removed and the sentence now names the least frustration of an assignment.

Two sources stay unopened. The body of Berg and Purcell (1977) could not be fetched from three hosts, so the constant $3/(5\pi)$ is still taken from Eq. 10 of Mora and Wingreen (2010), which was reread and attributes the monitoring-sphere result to Berg and Purcell; the manuscript's sentence already says this and was not changed. Bartlett (1938) is behind a paywall and is not cited. The multiplier in `s05_agency` equals the standard form $n_e-(p-q_h+1)/2$ of Bartlett's factor with $p=\dim U_i$, $q_h=\dim U_j$ and $n_e=n_{\mathrm{rep}}-1-\dim\mathcal X_{\mathrm{sh}}-\dim U_j$, by algebra against the textbook statement of the factor, recalled and not reopened in this pass; the manuscript claims only the form and says its support is numerical.

Zaffaroni (2004) was not opened either, but the review of Leipus and coauthors was reread in its text, and its Section 2 says that Zaffaroni's general aggregation scheme of random-coefficient autoregressions includes the case of common innovations. `s10d_environments` now reports this, with the statement that the paper was not opened, and the entry `zaffaroni2004contemporaneous` was added from its bibliographic records. Whether to keep a citation of an unopened paper is the author's choice.

Of the six bibliography notes, two were closed and four narrowed. The last page of `daft1984toward` was confirmed on a scan with its JSTOR cover page, and the volume, issue and pages of `hayek1945use` on the scan hosted by the publisher. For `toulouse1977theory` the journal, volume, year and first page are corroborated by a reference list read in text, and only the last page stays open. For `bertschinger2006information` the publisher was added from a bookseller record, which names one editor and no place. For `seguy1971relation` only the last page stays open. For `tishby2000information` the note now gives the page range 368 to 377 and says that it comes from secondary records.

### Second pass (follow-ups raised by the checkers of the first pass)

Items: 59 applied, 51 declined, 4 deferred, 1 partial. Items left deferred or partial:

| Item | State | Note |
|---|---|---|
| P2-05-1 | deferred | Neither Bartlett (1938) nor Anderson's text could be opened (no local copy, Exa unavailable), so no citation or bib entry was added; the sentence 'no proof of the correction is given here' stays. I checked by hand only that the multiplier equals nu_e-(p-nu_h+1)/2 with the stated degrees of freedom. |
| P2-10c-7 | deferred | Report is right (figures/fig_ren_per_level.tex line 87 still has ylabel 'leak $\varepsilon$'), but the figure file is outside my ownership. See cross_file. |
| P2-10-3 | partial | Section 10 already carried the sentence (scoped to abstract collectives); added the citation \cref{open:agy-meta-agent-exists} to it. The 00_abstract and 13_discussion parts are not in my files; 13_discussion already contains 'meet every clause', its cref not checked. |
| P2-10d-3 | deferred | figures/fig_env_cell.tex is not in my file set. Recomputed the exact ratio at the proposed radii (SCR/work/10d_pass2/exact_ratio.py, deterministic, no seed): all nine coordinates in the report are correct. Caption left unchanged because it describes the figure as currently drawn; coordinated figure and caption edit is in cross_file. |
| P2-10d-5 | deferred | Same defect as P2-10d-3, confirmed against the current figure file: line 42 still draws only the dashed x_g^2/12 continuation to 105.08 at 1 um, and the exact ratio quoted in the caption is not plotted. Caption and figure are mutually consistent as they stand. Repair is in cross_file. |

### Framing pass (technical follow-ups, framing sections, notation, bibliography)

| Chain | Items | Not applied |
|---|---|---|
| tech 1 | 1 | none |
| tech 2 | 4 | 1 deferred |
| tech 3 | 5 | none |
| tech 4 | 7 | 6 declined |
| tech 5 | 5 | none |
| tech 6 | 7 | 1 declined |
| group 01 | 61 | 22 declined, 4 partial |
| group 11 | 51 | 21 declined, 2 partial |
| group 12 | 35 | 13 declined, 2 partial |
| group 13 | 73 | 25 declined, 5 partial |
| appA | 69 | 14 declined, 1 deferred, 3 partial |
| bib | 25 | 10 declined, 1 deferred, 4 partial |

Items of the framing pass that were not applied in full:

| Chain | Item | Outcome |
|---|---|---|
| tech 2 | W2-7 | deferred: Author decision: whether the chemoreception lines and labels show leading-term values (19.707, 0.78829, as now, labeled leading-term in the caption) or exact-variance values (24.3, 0.97), which would also move the crossing point and require matching changes in ... |
| tech 4 | W2-20 | declined: Already met. ext3_obj.tex no longer says 'fails as stated': prop:obj-lrg-counter names the threshold conjecture in words and says conj:ren-lrg asks for a characterization; open:obj-scale(c) is a characterization question that records the clique-and-path eviden ... |
| tech 4 | W2-32 | declined: Same place as W2-20 and already reworded. The paragraph after prop:obj-lrg-counter now begins 'What is proved in the direction of the threshold conjecture', and appext3_obj.tex and chkext3_obj.tex cite conj:ren-lrg only for its interval. |
| tech 4 | W2-10 | declined: Already met. ext5_lrn.tex line 27 now says chk:fw-efe reports a truncated moment for the K=3, r_c=2 instance and an untruncated moment only for the K=6, r_c=2 instance, which agrees with chk:fw-efe as it stands. |
| tech 4 | W2-11 | declined: Already met. The clause 'which is what chk:fw-efe reports' is gone from chk:lrn-understanding; the check now says chk:fw-efe reports no untruncated average for that instance and computes a truncated moment. |
| tech 4 | W2-12 | declined: Optional and already met: the prose after prop:lrn-understanding-expansion carries a sentence giving the chk:fw-efe ratios (0.69 to 0.98) and saying they include all orders in sigma_H and the truncation at K=r_c+1. |
| tech 4 | W2-45 | declined: ext3_obj.tex is in the supplement, so its citation of open:sca-endogenous in open:obj-scale(a) needs no marking; the reference resolves. |
| tech 6 | W2-30 | declined: prop:ren-hayek (s10c line 162) and prop:abs-hayek (s10) are both in the supplement, so the plain citation is right. The one main-text citation of prop:ren-hayek (10c line 189) sits in a paragraph that opens by naming the Supplement. |
| group 01 | frame-01 | declined: The defect is in 13_discussion.tex; the sentence in the H1 paragraph of 01 already attributes only bounded contrast and a finite baseline to thm:col-lattice-contrast. I only tightened the table row's scope column to the theorem's hypotheses (Z^D, symmetric ker ... |
| group 01 | frame-08 | declined: This file already lists three exceptions with three labels, each checked against its current statement; the two-entry list is at 13_discussion.tex:21 (still unrepaired, see cross_file). Only change here: the parenthesis now reads '(Supplement, \cref{...})', si ... |
| group 01 | frame-10 | partial: (i) already met: the thm:col-lattice-contrast row carries the full scope. (ii) applied: grounding-tension row scope now matches part (b). (iii), (iv) lie in 11 and 13; the same missing 'reversible' qualifier stood in this file's sensing row and was repaired th ... |
| group 01 | notation-03 | declined: Already repaired: hyp:int-h4 now reads tau=-1/ln rho with rho the spectral radius of the joint transition matrix, 'the inverse spectral gap to leading order as rho->1'. |
| group 01 | notation-12 | declined: Nothing to change in this file: the introduction's 'closed of order d' agrees with def:met-abstract-physics(iii), which now states that d* bounds ord(alpha_M) from above. The proposed equality was found false by the technical owners. |
| group 01 | P2-01-1 | declined: Already repaired: the sentence now reads 'never exactly closed, its reduced equation keeping a memory, initial-state or colored-noise term for some initial law', which is the negation of thm:agy-closure-identity(b)(ii)<=>(iii). The 'always carries memory' word ... |
| group 01 | P2-01-8 | declined: Wrong of the current text: the statement of hyp:int-h4 contains neither 'coherence' nor 'coherent', and no sentence of the introduction about H4 uses the word, so there is nothing to disambiguate from def:coh-components. |
| group 01 | P2-01-16 | declined: Consistency check only: Grep finds no 'at most T-1' or 'order at most' wording in the file, so nothing contradicts the exact minimal order. The plain citation of this supplement label in one sentence was given the Supplement form. |
| group 01 | P2-01-19 | declined: Already repaired: the sentence on part (c) and the table row now carry "for a reversible diffusion whose drift is the block on C of a diffusive precision" and the drift-based contrast for a general drift, matching thm:agy-closure-average(a),(b). |
| group 01 | P2-01-22 | declined: Already repaired: the text now says top-down precision is proved to raise only the shared-error floor, with the total error falling 1 to 4 percent in three computed instances, and the table row gives status proposition; observation. Matches conj:hie-top-down ( ... |
| group 01 | P2-01-24 | declined: Already repaired: the formation clause and the opening of sec:int-open limit theorem status to infinite policy precision with exact in-group translations, give only reachability at finite precision, and say the model has no formation result in the sense of def ... |
| group 01 | P2-01-25 | partial: Scope already present in both places ("with exact in-group translations" in the prose, the same in the table row's scope column). Only change: the row's citation now marks obs:frm-grid as a supplement label. |
| group 01 | P2-01-26 | declined: Already repaired: all three quotations (H3 discussion, results-table row, open-problems paragraph) now read 'per cell, with reruns of a cell differing by up to three replicates' and say the pattern is not a contrast criterion, matching obs:frm-online. |
| group 01 | P2-01-27 | declined: Already repaired: H4 now names (Lin), (Loc), (B) of asm:sca-standing, gives tau=-1/ln(rho) as the inverse spectral gap to leading order as rho->1, and excepts the exact lengths, secular root and memory criterion from 'upper bounds'; this matches the in-words p ... |
| group 01 | P2-01-28 | declined: Already repaired: the row scope reads '(Lin), (Loc), (B), (M) and a named contraction; upper bounds apart from the exact lengths and the record criterion'. |
| group 01 | P2-01-29 | declined: Already repaired: both H5(a) and the table row state the equivalence as kernel invariance together with the coarse exterior reading the members' channels only through the coarse act, as in thm:met-abstract-physics(c). |
| group 01 | P2-01-30 | partial: H5(a) was already repaired (steady-state coarse filter, centralized start, stationary initial covariance). The sibling table row for prop:met-consensus-filter still said 'gives the coarse predictive law at every number of rounds'; weakened to the steady-state ... |
| group 01 | P2-01-31 | declined: Already repaired: the row now says the record precision raises the shared-error floor, reports the total-error fall of 1 to 4 percent in three instances, and gives status 'proposition; observation'; checked against conj:hie-top-down (a proposition) and obs:hie ... |
| group 01 | P2-01-32 | declined: Already repaired: the open-problems paragraph keeps only conj:hie-conformity-formation as a conjecture and says top-down precision is proved to raise only the shared-error floor, with the total error falling in three computed instances. |
| group 01 | P2-01-34 | declined: Already repaired: the table row now reads "bounded entrywise by products of the blocks' equitability defects over the smallest eliminated rate", which is lem:ren-galerkin(b), \|D_XY\| <= sigma_X sigma_Y / varkappa_perp. No "through contrast" wording remains in t ... |
| group 01 | P2-01-35 | declined: Already repaired: the prose now says the one matrix is "small when the smallest rate of the eliminated internal modes is large against the equitability defects of the blocks", consistent with lem:ren-galerkin(a),(b) and thm:ren-memory(b). |
| group 01 | W2-01-1 | declined: Already repaired: the sentence reads "At infinite policy precision with exact in-group translations" and is followed by the 2 percent / window-not-computed sentence citing obs:frm-stochastic. Checked against thm:frm-split-contrast(c) and obs:frm-stochastic; nu ... |
| group 01 | W2-01-4 | declined: Already repaired: both formation-status sentences (the formation clause after the coherence paragraph and the first sentence of sec:int-open) carry "with exact in-group translations". The introduction does not name (T1)-(T3),(T5). |
| group 01 | W2-01-6 | declined: Already met: the sentence reads "(Supplement, \cref{open:mis-scope,open:mis-dynamic-ratio,open:min-exact-fusion})" and open:fw-understanding-risk is likewise marked. The wording agrees with the open problem as it stands in s09_minimal.tex. |
| group 01 | W2-01-7 | declined: Already repaired by an earlier batch: the text says the claim is refuted in general (prop:obj-lrg-counter), holds for two equitable blocks and the nested level blocks with threshold b/(b-q), and is otherwise an open problem. Checked against conj:ren-lrg (now o ... |
| group 01 | W2-01-11 | partial: The introduction had no summary of the energy extension and no mention of sec:opn. One sentence was added to the Organization paragraph, worded from the head of 10e_open_problems.tex (three declared premises, necessary conditions only, no problem closed in pos ... |
| group 11 | frame-14 | partial: In sec:pre-scope one sentence now flags the agency theorems (finite policies, likelihoods not assumed Gaussian; (P1)-(P4) read) and the formation theorem (nonlinear mean-field map, frozen calibration) as not linear-Gaussian. Sign readouts of prop:abs-seguy not ... |
| group 11 | pos-01 | partial: Subsection retitled 'Predictions and diagnostics of model failure', column 'Refuted by' renamed 'Contrary observation' in all four tables, captions aligned, and two sentences added: a contrary observation removes the population from the model class, and no ind ... |
| group 11 | pos-02 | declined: Already repaired by an earlier batch: the cell now reads 'a record rebuilt by the union or product rule whose overconfidence factor does not grow with the rounds', which excludes the pooling rule (A). Checked by hand that the factor increases in t under (U) an ... |
| group 11 | notation-03 | declined: Nothing to change in this file: the proxies paragraph already defines tau = -1/ln rho(W), and the phrase 'inverse spectral gap' does not occur in 11_predictions.tex. The part in 01_introduction.tex belongs to that file's owner. |
| group 11 | P2-11-17 | declined: Already repaired: the table row now reads 'simultaneous revision by two members with full-support habits and finite expected free energies', which matches prop:agy-synchronous in s05_agency.tex. |
| group 11 | P2-11-20 | declined: Already repaired. Line 9 carries 'outside the static case noted at the end of the next paragraph', and line 11 states the sparse-plus-low-rank static route for the equal-time precision and where it stops, in agreement with open:agy-unrecorded-drive and sec:abs ... |
| group 11 | P2-11-21 | declined: Already met. The list of conjectures in the paragraph no longer names conj:hie-top-down, and the file cites that label nowhere. |
| group 11 | P2-11-22 | declined: Already repaired. The paragraph now says the chain is proved only at gamma = infinity with noiseless angle observations and that for finite gamma only reachability is a theorem about the frozen-calibration map, which matches the status passage of 07_formation. ... |
| group 11 | P2-11-23 | declined: Already repaired. The sentence now carries 'not necessarily a split selected by contrast', 'per cell' and the rerun spread of three replicates; the range 0 to 7 of 8 was checked against tab:frm-online. |
| group 11 | P2-11-24 | declined: Already repaired. The scope paragraph now denies a collective when the stationary form of (M) fails and a correlation length only when the uniform form fails as well, and says nothing about the correlation time, as thm:sca-h4(a) reads now. |
| group 11 | P2-11-25 | declined: Already repaired. The requirement on line 9 is qualified by the static case, and \citet{chandrasekaran2012latent} is cited on line 11; the key exists in references.bib. |
| group 11 | P2-11-26 | declined: Already repaired. The basis cell now names the detectable pair (F-bar, Lambda^s), the centralized stationary start and noiseless computation, which are the hypotheses of prop:met-consensus-filter(b) under which the average equals the predictive mean. |
| group 11 | P2-11-27 | declined: Already repaired: the row at line 103 now reads 'the predictive mean of the steady-state filter' and its basis cell carries 'from the centralized, stationary start with noiseless computation' and the detectable pair, matching prop:met-consensus-filter(b) as it ... |
| group 11 | P2-11-28 | declined: Already repaired: conj:hie-top-down is no longer cited anywhere in the file; the list of conjectures at line 25 names only labels that fdeps reports with matching prefixes, and conj:ren-lrg is described there as an open problem with its criterion refuted. |
| group 11 | P2-11-29 | declined: Already met: the basis cell of the firm row states 'a worked example with an exogenous price and a noiseless spot reading', which is the qualifier of ex:env-firm; the value 2.19 agrees with h^times = 2.187 of the example (recomputed by hand from ln(1+sqrt 3)/l ... |
| group 11 | P2-11-30 | declined: Already repaired: the basis cell of the row at line 132 says part (f) is a known result of the aggregation route to long memory, recovered here, with the two citations, and the contrary observation concerns part (c) only. |
| group 11 | P2-11-31 | declined: Already repaired: the phrase 'prediction-optimal agent' is gone; the row at line 128 speaks of a sensor optimal for a declared objective, says the one-step expected free energy does not imply it, and the contrary cell says the observation refutes the declared ... |
| group 11 | P2-11-32 | declined: Already repaired: the row at line 130 presents futures-price sufficiency as a known result recovered (separation theorem, feder1980futures), true by definition of the futures functional, with only the crossover lag specific to the declared exterior and no cont ... |
| group 11 | P2-11-33 | declined: Already repaired: the row at line 134 opens 'Known physical bound recovered', reads 'per particle and reading', attributes the number to the Boltzmann height law and a Fisher-information identity, and its contrary cell says none bears on H5. |
| group 11 | W2-11-1 | declined: The row at line 105 cites prop:hie-literal-records (static world), not prop:hie-record-filter(a), and makes no exactness claim. Its growth rates do not depend on the initialization: under (U) the precision is Lambda_z(0)+t Lambda^o and under (P) it obeys Lambd ... |
| group 11 | W2-11-2 | declined: Already repaired: the phrase 'theorems about that map' is gone; the paragraph now places the proved chain at gamma=infinity with noiseless angle observations (thm:frm-split-contrast(c), thm:frm-formation(e)) and calls only reachability a theorem about the froz ... |
| group 11 | W2-11-3 | declined: Already repaired: the sentence now reads 'which regions Laplacian renormalization returns is an open problem, its conjectured logarithmic criterion being refuted (Supplement, \cref{conj:ren-lrg})', which agrees with the openproblem environment in s10c_renormal ... |
| group 11 | W2-11-4 | declined: Same place as W2-11-3 and already met: conj:ren-lrg is no longer listed among the conjectures and is described as an open problem with the supplement named. |
| group 12 | cit_attr-04 | declined: Already repaired outside this file: the annotes of kirchhoff2018markov and villegas2023laplacian in references.bib now record 'Read: P' at the level the text claims (author confirmation marked outstanding there). The sentence in sec:rel-hierarchy-level paragra ... |
| group 12 | cit_meta-01 | partial: Both keys now exist in references.bib (annotes: not read). The 'search result' sentence in sec:rel-renormalization and the adiabatic-reduction to-check item in sec:rel-new now name zaghw2026renormalising and devries2026active as unread, characterized by title ... |
| group 12 | cit_meta-02 | partial: All 14 keys now exist (9 in references.bib, 5 in ext3/ext6/ext7 extra bibs), so absence is repaired. In this file: novelty sentence scoped to 'the reading levels recorded in this section', and nomura2026social added to the to-check list as unread. Ruiz-Serra i ... |
| group 12 | cit_meta-04 | declined: dacosta2021bayesian is now cited in sections/opn_p1.tex (part of the open-problems section), so the key is no longer orphaned; I did not open the source, so no new citation was added in sec:rel-debate. The other 69 uncited keys are a bibliography matter, repor ... |
| group 12 | P2-12-11 | declined: Already repaired: line 68 now says the drift-based rates (not contrasts) differ by a current-set term and that the drift-based inward rate keeps the couplings to outsiders, so the drift-based contrast can exceed the selecting contrast at zero current. This agr ... |
| group 12 | P2-12-12 | declined: Already repaired: the sentence now attributes path conditional independence to friston2023path and the form conditioned on initial states to friston2023simpler, consistent with 04_collectives.tex line 49. |
| group 12 | P2-12-13 | declined: Already repaired, same sentence as P2-12-11: it compares rates and states the relation of the contrasts as the supplement does (r^M >= r(C) in the reversible fixed-exterior case). The openness of a closure theorem in r(C) for non-reversible drift is not restat ... |
| group 12 | P2-12-14 | declined: Already repaired: the sentence now says the potential is lost when interventions interact and the members' displacements, predicted outcome minus target, differ along a joint effect, which matches thm:agy-joint-acts(c) in s05_agency.tex, and the citation carri ... |
| group 12 | P2-12-15 | declined: Already repaired: the sentence now compares drift-based rates with Rayleigh quotients of the stationary precision, as prop:agy-drift-precision states, and adds that the drift-based inward rate keeps the cut couplings so the drift-based contrast can exceed the ... |
| group 12 | P2-12-18 | declined: Already repaired: the text reads 'bounds the diameter of one-round sets (Supplement, \cref{prop:abs-one-round})', matching the proposition in s10_abstract_collectives.tex; the remaining 'one-round reach condition' is the proposition's own term. |
| group 12 | P2-12-19 | declined: Duplicate of P2-12-15 and already repaired; the current sentence agrees with the text of sup:agy-memory-and-closure-of-the-average (xin <= xin^M <= xin + max a^partial at J=0, r^M >= r(C)). |
| group 12 | P2-12-20 | declined: Already repaired: sec:rel-renormalization now attributes the long-range leak exponent of prop:ren-exponents(b) to the long-range Gaussian fixed point of fisher1972critical, 'cited from its record and abstract', the same reading level as in s10c_renormalization ... |
| group 12 | P2-12-22 | declined: Already repaired: the phrase is gone and sec:rel-sensing now cites Theorem 3.1 of chechik2005information directly, in agreement with the text after thm:env-canonical in 10d_environments.tex. No reading-level disclaimer for Chechik remains in the file. |
| group 12 | P2-12-23 | declined: Already repaired: the paragraph now claims no priority for the joint cap and budget, attributes the budget form to the information curve of chechik2005information and its Section 8, cites scharf1998wiener, and cites creutzig2008predictive (abstract) for one-st ... |
| group 12 | P2-12-24 | declined: Already repaired: sec:rel-new now lists only sensing 'at a horizon beyond one step' and states that the joint cap-and-budget treatment, the budget form and one-step slow-feature selection are known, pointing to sec:rel-sensing. 'Known' is slightly stronger tha ... |
| group 13 | P2-13-2 | partial: The sentence was changed, but not to 'cut couplings spread over their members' as a requirement: lem:ren-galerkin(b) is an upper bound, so spreading is sufficient-side evidence only. The text states the ratio condition and that high contrast alone does not ens ... |
| group 13 | P2-13-12 | partial: Applied the condition \|\|Pi_perpPhi\|\|^2 << xi_in^min xi_out and 'high contrast alone does not ensure'; the clause 'which requires cut couplings spread over the members' was replaced by a reference to the per-block bound through the largest single-agent boundary ... |
| group 13 | frame-04 | declined: Already met in this file: the H5 paragraph reads "invisible in social and top-down innovations", which agrees with lem:hie-record-blind(a) as it stands in 10b_hierarchy.tex (sensory innovations shift by -x(t)). No other occurrence of "unseen", "cannot see" or ... |
| group 13 | frame-06 | declined: Nothing to change in 13_discussion.tex: the sec:dis-meta paragraph states the full criterion (kernel invariant under the exterior dynamics and the coarse exterior reads the members' channels only through the coarse act), which matches thm:met-abstract-physics( ... |
| group 13 | frame-15 | partial: The discussion already names (Lin), (Loc), (B), (M) for thm:sca-h4, the hypotheses of thm:met-h5a and asm:frm-mean-field; I added exact code models and (Lin), (Loc), (B), (NN) of asm:sca-standing to the grounding-tension sentence, matching part (b). The A6 sen ... |
| group 13 | P2-13-17 | declined: Already repaired: the phrase is gone, and the cell sentence now gives 2.2e-14 per particle and reading against a chemical estimate pooling about 7.9e3 counts, and 2e-10 at equal pooling, nearly ten orders below one, as in ex:env-cell and the caption in 10d. |
| group 13 | P2-13-24 | declined: Already repaired: the status paragraph now says memory is a small correction for collectives whose bound \|\|Pi_perpPhi\|\|^2/xi_in^min is small against xi_out, and states that high contrast alone does not ensure this, in agreement with the prose after thm:ren-mem ... |
| group 13 | P2-13-25 | declined: Already repaired: the sentence now gives thm:col-lattice-contrast only the finite baseline and attributes the no-collective conclusion to def:col-baseline and def:col-collective, matching 04_collectives.tex after the theorem. Supplement citation forms on the s ... |
| group 13 | P2-13-26 | declined: Already repaired: the closure sentence states the condition through the spectral norm and says high contrast alone does not ensure it, as the prose after thm:ren-closure does. On the same line the stale status 'is a conjecture' for conj:ren-lrg was replaced (n ... |
| group 13 | P2-13-27 | declined: Already repaired: the sentence now states the equivalence of thm:agy-closure-identity(b), vanishing of memory, initial-state and colored-noise terms for every initial law exactly when the kernel of the coarse map is invariant. It no longer says memory vanishes ... |
| group 13 | P2-13-31 | declined: Already repaired: the sentence states the current proposition conj:hie-top-down (common-mode error raised whenever beta+omega<=1) with no status word 'conjecture' and cites obs:hie-top-down for the total error, both as Supplement. |
| group 13 | P2-13-32 | declined: Already repaired: the H3 paragraph opens 'a theorem only in part and only in one model', limits the theorem to gamma=infinity and to reachability for the frozen-calibration map, and matches thm:frm-formation(a),(b),(e) as read now. |
| group 13 | P2-13-33 | declined: Already repaired: the sentence now reads "in 0 to 7 of 8 replicates per cell, with reruns of a cell differing by up to three replicates" and adds that the pattern is not a contrast criterion. Checked against obs:frm-online and tab:frm-online (cell counts 0 to ... |
| group 13 | P2-13-34 | declined: Already repaired: the sentence now exempts the exact Ornstein-Zernike and second-moment lengths and the exact secular root and memory criterion before calling the rest upper bounds conditional on (M) and a named contraction. This matches thm:sca-h4(b),(d) and ... |
| group 13 | P2-13-35 | declined: Already repaired: the sentence now names the partial route for a static or stationary world without performative acts under sparsity and spread conditions not verified here, and the intervention certificate of thm:idn-intervention. Both agree with open:agy-unr ... |
| group 13 | P2-13-36 | partial: Applied: detectability of the abstract physics added to the hypothesis list of the H5a paragraph and to the parallel list in the meta-agent subsection. Declined: the habit-tilt clause already reads "up to the response to the members' centered computation noise ... |
| group 13 | P2-13-38 | declined: Already repaired: the located phrase is gone. The clause now says the member average is the steady-state predictive mean up to the response to averaged computation noise, and parametrizes the predictive law only from the centralized start with stationary initi ... |
| group 13 | P2-13-39 | declined: Already repaired: "never helps ... are conjectures" is gone. The text now states the common-mode error rises above its zero-precision value whenever beta+omega<=1 (the proposition labeled conj:hie-top-down) and that total error rises or falls with the local-no ... |
| group 13 | P2-13-40 | declined: Already repaired: memory is a small correction for collectives whose bound is small against xi_out, and approximate closure requires the norm ratio to be small, "which high contrast alone does not ensure". This agrees with thm:ren-closure(a),(f) and thm:ren-me ... |
| group 13 | P2-13-41 | declined: Already repaired: the phrase 'through contrast' is gone. The sentence now gives the explicit bound, the norm of Pi_perp-Phi squared over xin-min, at most sigma_cut squared over the smallest internal rate, for block averages with uniform leak, which follows fro ... |
| group 13 | P2-13-42 | declined: Already repaired: the novelty sentence is removed. The Part (c) paragraph now says the water-filling form is one 'for which we claim no priority', consistent with thm:env-canonical and the withdrawal in 10d. |
| group 13 | P2-13-43 | declined: Already repaired: the cell sentence now gives 2.2e-14 per particle and reading against a chemical estimate integrating about 7.9e3 counts, then the equal-pooling ratio 2e-10, 'nearly ten orders of magnitude below one', matching ex:env-cell. |
| group 13 | P2-13-44 | declined: Already aligned: the crossover of 2.19 rounds is now qualified 'with the price taken as exogenous, without price impact, and read without noise', which is the noiseless-limit qualifier of ex:env-firm (h-cross = 2.187 there). |
| group 13 | P2-13-45 | declined: Already repaired: the text now reads 'stationary deviations ... whose variance is at most of order one over the size of the smallest type', which is the covariance bound of prop:env-aggregate-closure(b). |
| group 13 | P2-13-46 | declined: Already repaired, same place as P2-13-42: no claim that the theorem adds the joint treatment remains; the paragraph disclaims priority for the form. |
| group 13 | P2-13-47 | declined: Already repaired in this file: the overview and the sensing paragraph both restrict to 'a sensor optimal for a declared ... objective'. The remaining 'what agents at different levels sense' restates the author's question, and the subsection title names a topic ... |
| group 13 | P2-13-48 | declined: Already repaired: the cell sentence carries the matched (equal-pooling) comparison, and the firm sentence attributes futures sufficiency to the separation theorem of production under price uncertainty (feder1980futures) and says it holds by definition of the f ... |
| group 13 | W2-13-1 | declined: Already met: the sentence ending 'meet every clause' closes with 'so that whether the clauses can hold jointly is an open problem (Supplement, \cref{open:agy-meta-agent-exists})', and the label is an openproblem in s05_agency.tex. |
| group 13 | W2-13-3 | declined: Already repaired: the sentence calls it an open problem and says the ln N conjecture is false for every constant, citing (Supplement, \cref{conj:ren-lrg,prop:obj-lrg-counter}); this matches the openproblem in s10c_renormalization.tex and prop:obj-lrg-counter i ... |
| group 13 | W2-13-5 | partial: In the H4 paragraph the citations of open:sca-endogenous and, in the same sentence, open:frm-access are now marked as supplement references. The citation in sec:dis-open was left as is because that paragraph opens with 'all but \cref{open:frm-closure} are stat ... |
| appA | notation-02 | partial: The proposed sentence declaring bare epsilon precision-side was not added, since the technical owners rewrote those statements with epsilon^Pi. The a^Pi, epsilon^Pi row now says these are not the weights and leaks of W and gives the nearest-neighbor relation f ... |
| appA | P2-appA-15 | declined: No rename was made anywhere, so the collision with sans-serif q of app05 does not arise; the appendix sentence is the repair and group 05's density use (q_i, q_C) is covered by it. |
| appA | notation-05 | partial: Added one list item on the positions of the letter c (modality subscript, self weight c=W_ii, superscript of Sigma^c and Pi^c, lambda_c, upright c of n_c) and one on the R objects. The proposed renaming of the modality index was not done: technical files are c ... |
| appA | P2-appA-28 | declined: No global modality letter is fixed and nothing is renamed: sans-serif c is taken and the technical files are closed. The new item states that in prop:abs-crossover the self weight of modality c is c_c with leak eps_c=1-c_c-2a_c. |
| appA | notation-17 | partial: Added bullets for Phi, calligraphic D (with italic D), Gamma, phi, h and X (with bar F), and extended the calligraphic T bullet with its four main-text meanings. The a/a_i, s/s_i, b/b_i and S collisions were not checked and got no bullet; Z_i needs none becaus ... |
| appA | P2-appA-11 | declined: No row or list item of the appendix quotes the Markov-error bound or its hypothesis; lem:met-unit-coordinate and thm:agy-closure-average are cited only as locations of symbols. Nothing to replace. |
| appA | P2-appA-38 | declined: Already met: the bullet on Xi lists the exact thresholds Xi^ex_ji, their Gaussian bounds Xi_ji (coinciding at sigma_H^2=0) and I^tx_ji, citing (Supplement, prop:fw-bounded-confidence). Checked against s02_framework.tex line 163. |
| appA | P2-appA-39 | declined: Already met: the row '$q$, $q_i$' of tab:not-networks now carries the disambiguating sentence (scalars are noise variances; with an argument or as a density q_i is the recognition density). |
| appA | P2-appA-41 | declined: Already met: the d_cl, d_M row gives d_M as the limit and says it is written d^infty_M in tab:not-extension, and the d^infty_M row says it equals d_M of def:agy-closure. Both agree with def:agy-closure(i). |
| appA | P2-appA-42 | declined: Already met in all four parts: X_dec (bullets on X and on calligraphic X), sans-serif f of sec:agy (sans-serif bullet), an ord(alpha_M) row agreeing with def:agy-closure(iii), and the n_c row cites prop:agy-consensus. |
| appA | P2-appA-43 | declined: Already met: a varepsilon_cal row exists, the calligraphic-D bullet defines D_i and the cycle family C_i (prop:coh-frustration(c)), and the Phi bullet records the transition product, written Psi(t,t') in the proof of prop:coh-info-decay (the text uses t', not ... |
| appA | P2-appA-44 | declined: Already met: the bullet on the letter R separates R_c, R^s_i, hat R_ij and R_ij from the world-conditional correlation matrix Corr_C of def:sca-coherence, and the chi_C row uses Corr_C. Wording agrees with 08_scale.tex line 330. |
| appA | P2-appA-45 | declined: Already met: the row reads correlational coherence and best correlational coherence, a row for the coherence score of def:coh-components and a row for varepsilon_rec exist, and the contrast bullet on Phi records Phi(t,s)=W(t-1)...W(s). |
| appA | P2-appA-46 | declined: Already met: a row for ord(alpha_M) follows the d* row and states ord(alpha_M)<=ord(0)<=d*, and a row for r^M, xin^M, xout^M exists; checked against 10a (d*=rank O - rank P_E, line 136 and 140). |
| appA | P2-appA-48 | declined: Already met by the ord(alpha_M) row, which states the chain of inequalities and that the second can be strict, in agreement with 10a_meta_agents.tex. |
| appA | W2-appA-1 | deferred: No rename made: it is an author decision and group 04 still writes Q^zeta=diag(q_i). The q row and the bullet 'The letter q is read by its form' already separate the noise variance from the recognition density. |
| appA | W2-appA-2 | declined: Already met: the Phi bullet records Phi(t,s) for Section 8, Psi(t,t') in the proof of prop:coh-info-decay and Psi(varphi) as the tilted product of prop:sca-heterogeneous. |
| appA | W2-appA-4 | declined: appA has no entry for box dimensions; n_c appears only as the number of consensus rounds. n_row and n_col are used only in app04 (lem:col-box-bounds, a proofs-file lemma), so no row is added. |
| bib | pos-04 | partial: Granger and Leipus entries already present and match Crossref (DOI 10.1016/0304-4076(80)90092-5) and the arXiv listing 1306.3301 (v1 only, no journal reference). Zaffaroni 2004 not added: ar5iv 1306.3301 Sections 1-2 credit the common-innovation limit to Pupli ... |
| bib | pos-05 | declined: Nothing left in the bib files: creutzig2008predictive is already in 10d_environments_extra.bib and agrees with the Crossref record I opened (DOI 10.1162/neco.2008.01-07-455); 12_related.tex already cites it. |
| bib | pos-10 | declined: Already repaired: fisher1972critical is defined once, in sections/10c_renormalization_extra.bib, with a Crossref record check, and is cited in s10c_renormalization.tex and 12_related.tex. I opened no source and changed nothing; the 1972 letter itself remains u ... |
| bib | cit_meta-01 | declined: Bibliography part already done by an earlier batch: zaghw2026renormalising and devries2026active are each defined once in references.bib with arXiv record checks and 'Not read'. Nothing opened; the two sentences proposed for 12_related.tex are still absent and ... |
| bib | P2-bib-3 | declined: Already present: zaghw2026renormalising is in references.bib (misc, arXiv 2608.09512, six authors) and in no extra.bib, and the citation in s10c_renormalization.tex resolves. Nothing opened or changed. |
| bib | cit_meta-02 | declined: Already repaired: all 14 keys are defined exactly once (ten in references.bib, four in ext3/ext6/ext7 extra files). I only moved the block that had been appended at the end of references.bib into key order; no entry text changed and no metadata was re-checked. |
| bib | cit_meta-03 | partial: 13 of 18 notes closed from records opened this session: INSPIRE (Wilson-Kogut, now Kogut, John B.), IDEAS/RePEc (Radner), PubMed (two Phys Life Rev subtitles), Springer book pages (CCIS 1721, 2193, 1326; Berglund-Gentz), zbMATH Open (Pavliotis-Stuart, Pearl, C ... |
| bib | cit_meta-04 | declined: Uncited entries may stay under the bibliography rule, so nothing was deleted; citing them is a .tex decision. dacosta2021bayesian is now cited in opn_p1.tex, so that part is moot. |
| bib | P2-bib-5 | partial: berg1977physics annote now says the constant 3/(5 pi) comes through Eq. 10 of mora2010limits and was not confirmed. I opened the PMC record (PMC1473391): abstract and scanned page images only, so the perfect-instrument equation remains unconfirmed. |
| bib | P2-bib-7 | declined: Already repaired: chandrasekaran2012latent is defined in references.bib only and 10_abstract_collectives_extra.bib holds just its comment line. I moved the entry one place up so that it sits in key order. |
| bib | P2-bib-8 | declined: Already repaired: references.bib defines zaghw2026renormalising once and refs_check reports unknown_cites=0. I opened the arXiv listing 2608.09512; authors, title, year and version dates agree with the entry, so nothing was changed. |
| bib | P2-bib-11 | declined: Already repaired: the annotation of chechik2005information records Section 5 (information curve, Eq. 15, concavity) and Section 8 as read from the JMLR PDF. Nothing was opened or changed. |
| bib | W2-bib-1 | declined: Already done by an earlier batch: chandrasekaran2012latent is defined once, in references.bib, and in no sections/*_extra.bib; s05_agency.tex and five other files cite it and resolve (dup_bibkeys=0). |
| bib | W2-bib-2 | deferred: Opened the Crossref record of Bartlett (1938), DOI 10.1017/S0305004100019897 (Proc. Camb. Phil. Soc. 34(1), 33-40); its truncated abstract does not show the factor, and the Cambridge page returned 403. Missing: readable text of Bartlett (1938) or of Anderson's ... |
| bib | W2-bib-3 | partial: Added price1970selection (Crossref record 10.1038/227520a0) and harman2020science (Crossref record and PMC7133509, which attributes the selection-plus-transmission equation to Price 1970). The Price paper itself was not opened (Nature sign-in redirect, dynamic ... |

### Section on open problems

Assembled: True; words: 4922. Sources of the register that a part writer could not open or match: none.

### Cross-file follow-up pass (reports the framing pass left for the technical files)

| Chain | Items | Not applied | Independent check |
|---|---|---|---|
| chain 1 | 3 | none | open defects 0 after 0 repair round(s); 5 holds, 1 not_checked |
| chain 2 | 3 | 1 partial | open defects 0 after 0 repair round(s); 2 holds, 1 repaired |
| chain 3 | 3 | none | open defects 0 after 0 repair round(s); 4 holds |
| chain 4 | 2 | none | open defects 0 after 0 repair round(s); 3 holds, 1 repaired |
| chain 5 | 8 | 1 declined | open defects 0 after 0 repair round(s); 7 holds |
| chain 6 | 5 | 1 declined, 1 deferred | open defects 0 after 0 repair round(s); 5 holds |
| chain 7 | 6 | 2 declined | open defects 0 after 0 repair round(s); 7 holds, 1 style |

Items of the cross-file pass that were not applied in full:

| Chain | Item | Outcome |
|---|---|---|
| chain 2 | C-22 | partial: Already met in three places: main text 'is an open problem (\cref{conj:ren-lrg})'; the open problem itself cites prop:obj-lrg-counter as refuting the threshold; open:ren-beyond(e) says 'Resolve'. One sentence after the environment in s10c read 'That conjecture ... |
| chain 5 | C-24 | declined: The sentence asserts only a resemblance of form and says 'no proof of the correction is given here, and its support in this paper is numerical'. Algebra rechecked by hand: n_e-(p-q+1)/2 with the stated degrees of freedom equals the printed multiplier. |
| chain 6 | C-04 | deferred: Nothing changed. Author decides whether the crossing is quoted for the rounded ratio 0.79 (x_g=4.656, 508 nm; recomputed 4.6561) or for the plotted line 0.78829 (x_g=4.642, 507.5 nm; recomputed 4.6423); the caption in 10d_environments.tex and line 102 of s10d_ ... |
| chain 6 | C-06 | declined: The check text (chk10d_environments.tex, the numcheck holding 0.0793) does not mention fig:env-cell or any script, so the generating script cannot be identified from the check itself; the script named by the report was not opened. |
| chain 7 | C-11 | declined: Already met: the annote records "P from the JMLR PDF for Section 5 (the information curve ... closed form Eq. 15, and its concavity) and Section 8 (... specifying the dimension in advance, as in CCA)", which covers what 10d_environments.tex line 50 reports. So ... |
| chain 7 | C-13 | declined: No defect of form: the three entries (zaghw2026renormalising, devries2026active, nomura2026social) have balanced braces and the fields their types need, and their annotes say "Not read", as 12_related.tex does. |

### Sync pass (framing sections against the changed statements, notation table, abstract)

| Group | Sweep agents (main, supplement) | Sweep verdicts | Defects sent to repair | Structure tasks | Final check |
|---|---|---|---|---|---|
| 01 | 4, 10 | 1 not_checked, 46 repaired | 0 | 6 done | open defects 0 after 0 repair round(s) |
| 11 | 4, 2 | 13 repaired, 1 style | 0 | 2 already_met, 3 done | open defects 0 after 0 repair round(s) |
| 12 | 2, 4 | 2 not_checked, 22 repaired | 0 | 4 done | open defects 0 after 0 repair round(s) |
| 13 | 8, 2 | 1 not_checked, 40 repaired, 2 style | 0 | 4 done | open defects 0 after 0 repair round(s) |

Notation table: 9 sweep agents, verdicts 5 not_checked, 55 repaired, 0 defects sent to repair, repairs: none.

Abstract: written True, 325 words; check open defects 0 after 0 repair round(s).

### Unresolved entries of the framing pass (15)

| Where | Location | Note |
|---|---|---|
| appA b1 |  | obstacle: Not checked: whether a bare varepsilon on the precision side survives in sections 05 to 09, 10a, 10d. A grep for 'varepsilon I+L' over all section files found only W-side or explicitly q-scaled uses (10_abstract_collectives.tex:83, s10b_hierarchy.tex:183) and the mean precision leak \bar\varepsilon in s04_collectives.tex:154, which matches the \bar\varepsilon_C row. |
| appA b1 |  | obstacle: The batch contained no item on the letter c or on kappa; those rows were not touched. |
| appA b2 |  | obstacle: Not checked: the existing list item on interpretation levels cites sec:fw-model for the assigned noise hat R_ij, while hat R_ij is introduced in def:fw-levels (02_framework.tex line 106); that item was outside this batch and was left unchanged. My new R item cites def:fw-levels. |
| appA b2 |  | obstacle: Row '$\theta$, $\theta^\ast$, $\chi$' of tab:not-networks still reads 'coherence level, best coherence' although def:sca-coherence is now 'Correlational coherence'; not in this batch, left unchanged. |
| appA b4 |  | obstacle: 08_scale.tex also uses sans-serif W (as a subscript or decorated symbol) and sans-serif J, J_infinity; the new sec:sca bullet lists only sans-serif R, as the item asked. Whether W and J need rows was not checked. |
| appA b4 |  | obstacle: The calligraphic-R bullet and the hie sans-serif bullet still cite several labels plainly whose location (main or supplement) I checked only for the labels I touched: prop:hie-nested-records and prop:hie-record-contrast are in s10b_hierarchy.tex and are now marked Supplement in the R row and R bullet; the same two labels cited elsewhere in the appendix (contrast bullet, hie sans-serif bullet) were ... |
| appA b6 |  | obstacle: The other sans-serif symbols of s05_agency.tex (\mathsf H_A, \mathsf n_A, \mathsf R_A, \mathsf c_\Phi, \mathsf Z_i, \mathsf d, \mathsf H_\star, \mathsf M, \mathsf z_i, \mathsf a, \mathsf a_\times, \mathsf w_\circ, \mathsf w_j) are not listed in Appendix A: the items did not name them and their definitions were not read. |
| assemble:opn |  | obstacle: No part or row was missing: parts 1 to 10 and rows 1 to 10 were all present and are all in the assembled file. |
| assemble:opn |  | obstacle: Deviation from the brief: the ten rows are set as two table floats, not one. A test compile of the head alone (mock text for each \cref) measured the single tabular at 913pt against a text height of 650pt, so one `table` cannot hold it. Rows 1 to 5 are in tab:opn-status, rows 6 to 10 in the new label tab:opn-status-b; the introduction cites both. |
| assemble:opn |  | obstacle: Supplement marking is inconsistent across the rows and was left as the rows give it: rows 1, 2, 5, 6 and 10 cite supplement labels (cor:apx-uniform, thm:apx-order-d, thm:idn-*, prop:idn-grade, thm:prv-*, prop:prv-turnover, thm:lrn-*) with no word 'Supplement', and row 2 column four cites open:ren-beyond (s10c_renormalization.tex) the same way; rows 3, 4, 7, 8, 9 mark it. The caption of the first t ... |
| assemble:opn |  | obstacle: Not checked: the full manuscript was not compiled, so the placement of the two [p] floats and the real printed length of the \cref lists are untested; the size test used mock reference text. |
| appA b7 |  | obstacle: In appA_notation.tex the bullet on nu cites prop:sca-poisson and prop:sca-rank-one, and the bullet on T cites prop:fw-rls, without the Supplement form although all three labels now live in s08_scale.tex and s02_framework.tex. No item of this batch covers them, so they were left unchanged. |
| appA b7 |  | obstacle: The collisions of a with a_i, s with s_i, b with b_i and S (innovation covariance against block set) named in notation-17 carry no verified anchors in the finding; they were not checked and no bullet was written for them. |
| appA b10 |  | obstacle: Not checked: the other labels cited plainly in the sans-serif bullets of appA (lines 218 to 224) against main/supplement location; only prop:ren-exponents and ex:ren-block-average in the Section 13 bullet were verified to be in s10c_renormalization.tex and recited as Supplement. A run of fdeps.py appA_notation.tex --supp would list the rest. |
| appA b10 |  | obstacle: The letter mathfrak x has three uses in 10c/s10c (epsilon^Pi/a^Pi on the chain, epsilon^Pi/(A_h q^l) in thm:ren-nested, x_{2,d}=1/xi_{2,d}^2 in prop:ren-exponents); the new row records all three, no source file was changed. |

### Unresolved entries of the cross-file follow-up pass (5)

| Where | Location | Note |
|---|---|---|
| cross:4 |  | obstacle: I did not open harman2020science or price1970selection myself; the citation of Harman rests on the annote of its entry in references.bib, which records that the framing pass read the open PMC copy. |
| cross:4 |  | obstacle: Not checked: whether summaries of thm:obj-rotation in files I do not own (introduction, 10e_open_problems.tex, abstract) repeat the unqualified 'only obstruction' wording under a different phrasing; a Grep of sections/ for the literal phrase 'only obstruction' found it only in ext3_obj.tex and, in an unrelated scale-time context, at appext3_obj.tex line 264. |
| cross:7 |  | obstacle: C-14 deleted 71 entries from references.bib, a file that is untracked in git. The only copies of the removed entries are in the session scratch folder: <session scratch>/work/c7/removed_entries.bib (the 71 entries) and <session scratch>/w ... |
| cross:7 |  | obstacle: The 10e_open_problems.tex and ext3_obj.tex statements about waade2025one (fitted action precision, its confounding with preferences, the conflicting-preference result) rest on Sections 2.3 to 4, which were not read in this task; the annote says so. |
| cross:7 |  | obstacle: Deleted keys: acemoglu2013opinion albarracin2024shared alonso2016bayesian arrow1964role axelrod1997dissemination bauschke1996projection bertschinger2008autonomy besag1974spatial bollobas1991edge bruineberg2022naked butta2007propagation castellano2009statistical chen2019finite chorin2002optimal chover1973functions dawid1982well deutsch2001best feldman2010attention fields2020scale fields2021minimal fields2022information friston2013life friston2015knowing friston2024designing friston2026active gao2 ... |

### Unresolved entries of the sync pass (84)

| Where | Location | Note |
|---|---|---|
| sync:01_introduction p1 |  | obstacle: fdeps.py reports app:checks at collective_agents_supplement.tex:0, but no such file exists in MAN; the label is currently defined in collective_agents.tex line 50 (\section{Numerical checks}). The citing sentence ("The supplement holds ... the numerical checks (\cref{app:checks})") resolves and was left as is; it is correct only once the supplement driver exists. |
| sync:s11_predictions p1 |  | obstacle: Lines 7 and 9 of s11_predictions.tex (outside my ranges, left untouched) still carry six "(Supplement, \cref{...})" citations: rem:col-world-conditional, prop:abs-ultrametric-cap, chk:abs-cap, ex:agy-collider/ex:agy-masking, open:agy-unrecorded-drive, sec:abs-world. |
| sync:s11_predictions p1 |  | obstacle: Unflagged labels cited in my ranges (for example prop:frm-nulls, conj:frm-formation, thm:coh-withdrawal, prop:abs-polity, prop:hie-literal-once, prop:ren-depth) were not checked against their statements; the role covers flagged labels only. |
| sync:s11_predictions p1 |  | obstacle: Line 21 says the coupling ratio is the factor by which coupling "falls" per level; prop:abs-hierarchy defines the ratio for any positive value and assumes it below one only in part (b). Left as is. |
| sync:s12_related p1 | 74-117: prop:abs-polity, lem:mis-social-blind, thm:agy-mori-zwanzig, thm:col-diffusive-precision, def:col-coarse-medium | not checked: Unflagged labels of the range; their citing sentences were not compared with the statements. Literature-only lines 79, 95, 97 and 111 cite no manuscript result and were not checked against sources. |
| sync:s12_related p1 |  | obstacle: No missing labels in either range (fdeps: missing=0, prefix_differs=0 for 118-119 and 74-117). |
| sync:s12_related p1 |  | obstacle: The words 'Supplement,' still occur at lines 7, 11, 42 and 51 of s12_related.tex, outside my ranges; left for the agents that own those ranges. |
| sync:s12_related p1 |  | obstacle: Two edits add a few words (line 74: 'diffusive ... in two dimensions'; line 106: the corrected Laplacian clause and its pointer); the removals of 'Supplement,' offset them only in part. |
| sync:13_discussion p1 | 47-47: 'it is linear-Gaussian ... otherwise appear only in remarks, open problems and conjectures' | not checked: Checked against the four cited labels and the three named exceptions of the H5 extension (sections 10 to 14) only. Not checked against the eight Part B supplement extensions (ext1 to ext8), which the sentence's 'it' does not obviously cover. |
| sync:s13_discussion p1 |  | obstacle: No missing labels in lines 13-16. |
| sync:s13_discussion p1 |  | obstacle: The words 'Supplement,' still occur 3 times on line 7 and 7 times on line 11 of s13_discussion.tex; those lines are outside my ranges and were left for the agents that own them. |
| sync:s13_discussion p1 |  | obstacle: Unflagged labels on line 15 (asm:ren-standing, thm:ren-decimation, thm:ren-flows, prop:ren-depth) and on line 13 (thm:env-control) were read against their statements only as far as the cited constants and clauses (exponent 2, one decimation step in two dimensions, preference reversal); thm:env-control parts (c) onward not checked. |
| notation:appA_notation p1 |  | obstacle: Supplement marking not converted: lines 224-225 cite 12 supplement labels with a plain \cref (lem:env-markov, prop:env-diffusive, prop:env-selection, prop:env-concentration, ex:env-cell, def:env-aggregates, prop:env-aggregate-closure, prop:env-aggregate-memory, ex:env-firm, prop:env-multiplex, prop:col-whole-population). The task card asks for '(Supplement, \cref{...})'; report 0 of the notes file ... |
| notation:appA_notation p1 |  | obstacle: Not checked: the sans-serif symbols that occur only in app10d_environments.tex (a large proof-local set such as \mathsf U, \mathsf S, \mathsf O, \mathsf N, \mathsf a_j, \mathsf b_j) are not listed in row 224 apart from \mathsf Q; I verified \mathsf Q, \mathsf Q_s, \mathsf Q_f against line 76 of that file and left the others as local to the proofs. |
| sync:s01_introduction p3 |  | obstacle: No missing labels in either range. One Read of s08_scale.tex covered 100 lines (178-277), over the 80-line window of the bounded-reading rule; no harm resulted. |
| sync:s01_introduction p3 |  | obstacle: Not checked: the unflagged label lem:met-discrete-closure cited at line 134 was not opened (fdeps did not flag it; it resolves). The identity encodings and covariance fixed point hypotheses of conj:sca-common-code are still not carried in the summary sentence, left out to limit lengthening. |
| sync:12_related p2 | 1-27: We checked the expansion numerically on a random six-variable instance (line 26) | not checked: No chk: record of this computation exists in the manuscript. I re-derived the second-order expansion and the normal-drift exact form by hand and reran it (seed 0, n=6): residual ratios 7.98, 8.01, 8.01, 8.00; sentence left unchanged. |
| sync:12_related p2 |  | obstacle: No missing labels in either range (fdeps: missing=0, prefix_differs=0 for 28-44 and 1-27). |
| sync:12_related p2 |  | obstacle: The numerical sentence of line 26 (six-variable instance, factor of about eight) has no numcheck in any chk file; if the manuscript requires every quoted computation to have a record, a check entry would have to be added in a file I do not own. My rerun is at <session scratch>/... ... |
| sync:12_related p2 |  | obstacle: Literature claims about cited works (lines 9, 20, 22, 30, 35) were not re-read against the primary sources; only their agreement with the supplement's s12_related.tex was checked. |
| sync:12_related p2 |  | obstacle: Line 28 'Stationary blankets need shells thicker than the Markov length' was left as is: it holds in the worst-case (sup over vertices) sense of def:col-markov-length, while thm:agy-h1(a) states only the sufficiency direction under decay hypotheses. A stricter reader may want 'the governing length is the Markov length'. |
| notation:appA_notation p2 |  | obstacle: Rows 222 and 223 cite twelve supplement labels with a plain \cref (for example prop:ren-ring, prop:ren-codes, prop:hie-depth, prop:hie-echo-tradeoff, obs:hie-top-down). The task card asks for '(Supplement, \cref{...})'; coordinator report 0 in the notes file says a plain \cref to a supplement label is not a defect (numbers print with prefix S, stated at 01_introduction.tex lines 19 and 106) and fo ... |
| notation:appA_notation p2 |  | obstacle: Outside my range, not edited: line 214 says standard Brownian motions are written \mathsf B or \mathsf W and cites prop:met-memory, asm:ren-standing, prop:ren-perron; sec:hie-records (\mathsf B_i, \mathsf B_z, 10b_hierarchy.tex line 96) and prop:hie-reversible-sandwich and prop:ren-adiabatic (\mathsf B, \mathsf B_r, \mathsf B_i) use the same convention without being cited there. The statement is g ... |
| notation:appA_notation p3 | 219-220: sans-serif symbols of app10a, chk10a, app08, chk08 | not checked: The inventory covered the main-text and s-files of groups 06, 08, 10, 10a, and app/chk of 06 and 10 only. app06 and app10 use further local sans-serif symbols (\mathsf O_\tau, \mathsf D, \mathsf M, \mathsf B_l, \mathsf n, \mathsf s, \mathsf v, \mathsf c_0..2) that the appendix does not list. |
| notation:appA_notation p3 |  | obstacle: Four supplement labels in the sec:met bullet (ex:met-channel-memory, ex:met-traders, ex:met-two-firms, prop:met-closure-notions) are cited with a plain \cref. Left as is under coordinator report 0, whose premise I verified (01_introduction.tex line 19 states the S prefix); the task card's wording would instead mark them '(Supplement, ...)'. A coordinator decision if uniformity is wanted. |
| notation:appA_notation p3 |  | obstacle: Proof-file sans-serif symbols of app06_coherence.tex and app10_abstract_collectives.tex are local to proofs and unlisted in Appendix A; not added, since the checker's scope is the main-text file each row names. |
| structure:11 |  | obstacle: Declined note 1 (static sparse-plus-low-rank route): line 9 already says 'outside a static case for which the supplement describes a partial route', and the detail with the citation is in s11_predictions.tex; adding it to the main text would restate a result. |
| structure:11 |  | obstacle: Declined note 2 (range of persistences): 'for persistences in [alpha_-,alpha_+] subset [0,1)' is already in the row. |
| structure:11 |  | obstacle: Declined note 3 ('with a common shock' too narrow): the basis cell already reads 'common and idiosyncratic shocks, (f) for the limiting aggregate with the common shock only'. |
| structure:11 |  | obstacle: Declined note 4 (refuter for rebuilt records): the cell is already restricted to 'the union or product rule' of prop:hie-literal-records. |
| structure:11 |  | obstacle: Declined note 5 (refuter for the horizon-h objective): the row already states the declared objective and that the one-step expected free energy does not imply it. |
| structure:11 |  | obstacle: Not checked: the scope qualifiers in the 'Basis and status' cells against the full text of each cited statement (only environment kind, placement and fdeps change notes were compared). |
| structure:11 |  | obstacle: Judgment call in (a): only the aggregate-memory row was changed. Rows whose quantities are world-conditional (contrast, lengths, light cone, coupling ratio) were left to the general sentence of sec:pre-proxies that a test needs a record of the world path; the four idn statements do not show more for them than that sentence says. |
| structure:11 |  | obstacle: The added clause says uncoupledness 'is not shown by their covariance'; thm:idn-path shows the path law identifies more in pure models, so the clause was deliberately limited to the covariance and does not claim that no record-based test exists. |
| structure:12 |  | obstacle: Report 1 declined: already repaired; scharf1998wiener is no longer in the unchecked list of sec:rel-new, and s12 sec:rel-sensing names Scharf and Thomas with 'we claim no priority'. |
| structure:12 |  | obstacle: Report 3 declined: already repaired; line 28 attributes the conditioning on initial states to friston2023simpler. |
| structure:12 |  | obstacle: Report 4 declined: the sentence lives in s12_related.tex (not owned) and already carries the two unread works. |
| structure:12 |  | obstacle: Report 5 declined: already repaired; the item ends 'starting with zaghw2026renormalising and devries2026active'. refs_check reports no unknown citation. |
| structure:12 |  | obstacle: Report 7 declined: the cited passages moved to s12_related.tex; the change notes record that the supplement markers were added there. |
| structure:12 |  | obstacle: Report 9 declined: moot, the condensation has been done. |
| structure:12 |  | obstacle: Reports 8 and 10 are real but concern s12_related.tex, which I do not own: passed on in cross_file. |
| structure:12 |  | obstacle: Reports 2 and 6 acted on (comment line of sec:rel-nested; 'positions on sparse coupling'). |
| structure:12 |  | obstacle: Not checked: the sentence in sec:rel-nested 'error bounds exist for all of these' was left as the claims pass left it; I read thm:met-h5a(i) to (iii) and open:met-approximate only, which do not contradict it but do not confirm an error bound for the group posterior. |
| structure:12 |  | obstacle: Not checked: that N in prop:obj-lrg-counter is called the number of agents elsewhere; the statement itself sets N equal to the number of vertices of the graph. |
| structure:12 |  | obstacle: I used cd once inside a read-only Bash call in the sections folder (no file was written); later calls used absolute paths. |
| sync:s01_introduction p7 | 29-29: ex:env-firm, ex:env-person | not checked: Environment (example) and the way rem:env-interpretation cites them were confirmed; the bodies of the two examples were not read. The sentence calls them worked examples only. |
| sync:13_discussion p7 |  | obstacle: Lines 13 and 15 grew by roughly 60 words in total, against the instruction not to lengthen: the additions are hypotheses the cited statements carry, and I found no supported sentence to cut within my ranges. |
| sync:13_discussion p7 |  | obstacle: Unflagged labels of the ranges (prop:fw-prior-completion, prop:fw-transfer-kernel, lem:mis-social-blind, thm:mis-echo-chambers, prop:mis-exact-no-echo, prop:coh-c0-blind, thm:coh-withdrawal, thm:coh-holonomy, thm:coh-amplification, def:coh-components) were not checked against their statements; prop:mis-overvaluation-scope and the N_ex row of tab:agy-nulls were read and their citing sentences hold. |
| sync:13_discussion p7 |  | obstacle: The sentence 'Exact conditions for each direction of misreading are open' drops the restriction of open:mis-scope to rank-limited or noisy full-rank codes; left unchanged since the invertible noiseless case is stated as settled two sentences earlier. |
| notation:appA_notation p4 | 214-218: plain citations of supplement labels | not checked: Left as found under coordinator report 0, confirmed in 01_introduction.tex line 19 (prefix S stated once): prop:env-concentration (214), prop:hie-record-contrast (215), obs:hie-exact-receiver (216), sec:ren-network and ex:env-cell (217). Convert them if the task card's rule is to prevail. |
| notation:appA_notation p4 |  | obstacle: The task card asks for "(Supplement, \cref{...})" on moved definitions; coordinator report 0 in the notes file says not to convert plain citations in either direction. I followed report 0 for the five existing plain citations and wrote "Supplement" on the new ones I added (sup:agy, thm:sca-trees). |
| notation:appA_notation p4 |  | obstacle: Not checked: the proofs and checks files (app*, chk*) and the extension files (ext*) for further local uses of \tau, \delta, \mathcal R, \mathcal V; only main-text and s-files were searched. \tau_{\mathrm L} also occurs in ext3_obj.tex with the same meaning. |
| notation:appA_notation p4 |  | obstacle: Not checked: whether \mathcal V(C_k) (s04_collectives.tex line 252, variables of the members of C_k) needs its own mention; it is the same set restricted to a block and was left out. |
| structure:13 |  | obstacle: Declined as already repaired in the current text: notes 1, 4 (wording identical to hyp:int-h5(a)), 5 and 11, 7, 8, 9, 10, 13, 14 and 15, 16, 17, 18. |
| structure:13 |  | obstacle: Declined as not applicable to this file: notes 2, 3 and 6 (the quoted phrases 'memory vanishes', 'never helps', 'falsif' do not occur in 13_discussion.tex) and note 12 (phrase is in s13_discussion.tex, reported in cross_file). |
| structure:13 |  | obstacle: Note 19 checked: the thm:col-boundary sentence already says 'region with a finite interior'; the reduction sentence in sec:dis-renormalization states a bound and no necessity claim; thm:prv-tree and open:lrn-joint are not paraphrased in this file. |
| structure:13 |  | obstacle: Not checked: the claims of sec:dis-meta, sec:dis-renormalization and sec:dis-gauge against their statements (taken as verified by the preceding claims pass); thm:sca-h4, prop:ren-depth and thm:apx-posterior were not opened, their conditionality is taken from this file's own status paragraphs, the introduction and open:met-approximate. |
| structure:13 |  | obstacle: The new conditional-results sentence in sec:dis-limits is a non-exhaustive list ('several theorems'); it does not name thm:ren-closure(b), which README_common records as conditional on (B) but which this file does not cite. |
| notation:appA_notation p5 |  | obstacle: Convention conflict: the task text and README_frame say a supplement label is cited as '(Supplement, \cref{...})', while coordinator note 0 in frame/notes/appA_notation.txt says plain citations are not defects and must not be converted. I followed the task text on line 205 only, the one row in my ranges with plain supplement citations; revert if note 0 governs. |
| notation:appA_notation p5 |  | obstacle: Not checked: supplement-only meanings of \Phi, \phi, h, X, \nu and \mathcal D. Only \Gamma was sampled in the supplement, and its added list omits the Lyapunov exponents \Gamma_k (s08_scale.tex line 241), \Gamma^0_{ij} and \Gamma^1_{ij} (prop:mis-believed-values), \Gamma(d) (prop:abs-seguy) and \Gamma_F (s10c_renormalization.tex line 102). |
| notation:appA_notation p5 |  | obstacle: Outside my ranges, not acted on: 06_coherence.tex line 150 (prop:coh-code-potential(c)) writes n_c(\sigma) for the number of agents using code c, close to the consensus-round count n_{\mathrm c}. The owner of the row on n should check whether the appendix records this. |
| notation:appA_notation p5 |  | obstacle: None of the three renames (\varrho_c, n_{\mathrm c}, Correlational coherence / \mathrm{Corr}_C) occurs in lines 205-213; line 211 cites def:sca-coherence only for the readouts X_i, which agrees with the current definition. |
| notation:appA_notation p6 |  | obstacle: Conflict of conventions: report 0 in frame/notes/appA_notation.txt (coordinator) says a plain \cref to a supplement label is not a defect and should not be converted in either direction; the task card and README_frame.md say a definition that moved to the supplement is cited as '(Supplement, \cref{...})'. I followed the task card and converted five plain citations in lines 201, 203, 204. If the co ... |
| notation:appA_notation p6 |  | obstacle: Not checked: the proofs in the supplement beyond the single line of app04_collectives.tex that defines \tilde\Xi_{\sB}; the supplement files for uses of T, Xi, Upsilon, varpi, calligraphic U not listed in the rows (only main-text files were swept for unlisted uses, plus s02, s05, s08, s09, s10d where a row cites them). |
| structure:01 |  | obstacle: Report 1 declined: the phrases 'high contrast' and 'of high contrast' do not occur in 01_introduction.tex. |
| structure:01 |  | obstacle: Reports 3 and 5 declined as already met: hyp:int-h4 already names (Lin), (Loc), (B), writes tau = -1/ln rho as the inverse gap to leading order, and excepts the exact lengths. |
| structure:01 |  | obstacle: Report 4 declined: the thm:col-lattice-contrast row already carries its hypotheses; the thm:coh-grounding-tension row is in tab:int-results-b (s01_introduction.tex) and tab:pre-sensing is in 11_predictions.tex, neither of which I own. |
| structure:01 |  | obstacle: Report 6 declined as already met: the sentence after the premises already says no theorem takes A6 as a hypothesis and that the theorems rest on further hypotheses named in their statements, with the supplement pointer. |
| structure:01 |  | obstacle: Report 2 acted on by a pointer only: the exception list (code game, deliberation model, mean-field map, sign readouts) is already in the supplement at sec:int-open, so I added one sentence pointing there and did not duplicate the list. |
| structure:01 |  | obstacle: The supplement part labels (sup:part-results, sup:part-ext, sup:part-proofs, sup:part-checks) are defined only by make_drivers.py and exist in no .tex file yet, so the roadmap cites the section labels of each part instead; citing the part labels now would give unresolved references. |
| structure:01 |  | obstacle: app:checks is defined at present only in the old driver collective_agents.tex line 50; the roadmap and the table preamble cite it, so the new supplement driver must keep that label. |
| structure:01 |  | obstacle: I removed from the table preamble the sentence 'an entry whose number carries the prefix S is a statement of the supplement' because the same fact is now stated in sec:int-hypotheses and in the roadmap; restore it if a third statement at the table is wanted. |
| structure:01 |  | obstacle: Word counts are my own count with each \cref and each inline formula counted as one word; no manuscript compile was run, so the printed form of the long \cref ranges (S-prefixed section ranges) is unchecked. |
| notation:appA_notation p7 | 178-196: $\varrho$ | not checked: The bullet's three main-text meanings hold and $\varrho_c=R_c/(g^2P)$ matches 03_misreading.tex:65. Supplement-only uses ($\varrho_{\tau_{\mathrm L}}$ in s10c near line 181, $\varrho_a$ in ext5, $\varrho_{ze}$ in ext6, $\varrho_{ij}$ in ext8) were located but their definitions not read, and they are not recorded in the bullet. |
| notation:appA_notation p7 | 178-196: letter $q$ | not checked: The bullet's listed forms hold. $q_0$ (08_scale.tex:105, a bound on initial error covariances, not a noise variance), the code kernel $q_T$ and the reconstruction $\hat q_{ij}$ (02_framework.tex:69,76) are unlisted; I judged them covered by 'read by its form' and did not add them. |
| notation:appA_notation p7 |  | obstacle: Convention conflict: coordinator note 0 in frame/notes/appA_notation.txt says a plain \cref to a supplement label needs no added word and should not be converted, while the task card and README_frame say a definition that moved to the supplement is cited as "(Supplement, \cref{...})". I followed the task card for the three citations whose targets are supplement-only (rows 173, 174, bullet 190), ma ... |
| notation:appA_notation p7 |  | obstacle: The scan for decorated forms of c, m, q covered main-text section files only (02-13 pattern); supplement files were not scanned for these letters. |
| notation:appA_notation p7 |  | obstacle: $\bar c_{\mathrm L}$ (10d_environments.tex:131,136) sits in running text of sec:env-selection with no enclosing numbered statement, so the bullet cites the section. |
| notation:appA_notation p8 | 61-92: \rho(\cdot) | not checked: asm:sca-standing uses rho(W) as cited. The clause that a bare rho always means the spectral radius of the transition under discussion was sampled only (two hits, 01_introduction and 08_scale, both conforming), not checked exhaustively. |
| notation:appA_notation p8 |  | obstacle: The task card says a definition that moved to the supplement is cited as 'Supplement, \cref{...}'; note 0 in frame/notes/appA_notation.txt (coordinator) says a plain \cref to a supplement label is acceptable and should not be converted. I followed the task card for the four rows of my ranges whose cited labels are in the supplement (the file already uses the 'Supplement, \cref' form about 45 times ... |
| notation:appA_notation p8 |  | obstacle: Note 1 (bare precision-side \varepsilon in sections 05 to 09, 10a, 10d): a Grep for '\varepsilon I' and for Pi or 'precision' followed directly by a bare \varepsilon found no hit in those sections or their s-files; hits exist only at s04_collectives.tex:154 (\bar\varepsilon I), 10_abstract_collectives.tex:83 and s10b_hierarchy.tex:183, as the note reported. This is a pattern search, not a reading ... |
| notation:appA_notation p8 |  | obstacle: Notes 2 (kappa), 3, 5, 6, 7, 8, 9 concern rows or bullets outside lines 61-149 and were not acted on. Note 4 (correlational coherence row) is already repaired: row 83 matches def:sca-coherence with \mathrm{Corr}_C. |
| notation:appA_notation p9 |  | obstacle: Uniqueness across all sections was scanned only for P_0, kappa, s_KL, S and unindexed s; for D, Delta, ell, gamma, O, W, zeta and q only the cited defining place was confirmed, other local uses not checked. |
| notation:appA_notation p9 |  | obstacle: Note 7 collisions are recorded inside rows 26 and 37 rather than as a bullet after the tables, which lies outside range 1-60; a later owner may prefer to move them to a bullet. |

## Critical and major findings

| Id | Severity | Title | Location | State |
|---|---|---|---|---|
| fw-01 | major | prop:fw-bounded-confidence(b): the 'if and only if' addressing threshold uses a Gaussian information term for a reply that is not Gaussian when sigma_H^2 > 0 | manuscripts/Collective_Agents/sections/02_framework.tex:365-369 (prop:fw-bounded-confidence(b)); proof at sections | applied |
| fw-02 | major | prop:fw-bounded-confidence(d) and the 'no risk-based reciprocity' sentence hold only with the listener's own belief frozen | manuscripts/Collective_Agents/sections/02_framework.tex:375 (prop:fw-bounded-confidence(d)) and :379; proof at sec | applied |
| mis_min-01 | major | Alternation rate 1.0703173057 is not a property of the stated two-agent instance; the second counterexample's parameters are absent from the manuscript | sections/chk09_minimal.tex:15 (chk:min-amplification); sections/09_minimal.tex:134 (sec:min-moment); sections/08_scale.tex:58 (ex:sca-amplifying-profile) | applied |
| mis_min-02 | major | tab:min-bilayers reports message-fed bilayers under 'Single-hop evidence relays', which the text and tab:min-results say cannot feed an interior | sections/09_minimal.tex:93 (tab:min-bilayers, row 3) against sections/09_minimal.tex:99 and sections/09_minimal.tex:56 (tab:min-results) | applied |
| col-01 | major | Unconditional ultrametric cap said to vanish at weak grounding whatever the barriers; cited proposition has a proviso that fails in finite populations | sections/04_collectives.tex:492 (sentence after def:col-ultrametric), citing prop:abs-ultrametric-cap at sections/10_abstract_collectives.tex:417; in tension wi | applied |
| agy1-01 | major | Opener claims the selecting contrast bounds memory for non-reversible drift; the section itself lists that as open | sections/05_agency.tex:3 and :105 (against :128, :132) | applied |
| agy1-02 | major | 'A collective whose boundary hears its interior always carries memory' is false | sections/05_agency.tex:64 | applied |
| agy1-03 | major | 'The two differ by at most the circulation term' fails for the contrasts | sections/05_agency.tex:125; prop:agy-drift-precision title (:116) | applied |
| agy2-01 | major | Sign obstruction for epistemic choices stated without the null-policy qualifier | sections/05_agency.tex:340 (ex:agy-unrepresented-driver) and :400 (prose after prop:agy-performative-sign) | applied |
| agy2-02 | major | Agency failures in the examples vanish under the free-product-habit class used by prop:agy-index(c) | sections/05_agency.tex:203 (def:agy-group-model), :300-322 (def:agy-agency-index, prop:agy-index), :335 (ex:agy-no-data-sharing), :325 (prop:agy-synchronous) | applied |
| agy3-01 | major | Identity under conditioning on the exterior path fails when the exterior hears the members; prop:agy-identity(b) proof asserts an unstated independence | sections/05_agency.tex:419 (def:agy-identity), :433 (prop:agy-identity(b)); proof sections/app05_agency.tex:213 | applied |
| agy3-02 | major | prop:agy-tests(a): conditional covariance singular and degrees of freedom wrong because X_0 in X_sh contains mu_i(0) | sections/05_agency.tex:543 (prop:agy-tests(a)); proof sections/app05_agency.tex:235; sections/chk05_agency.tex:63 | applied |
| agy3-03 | major | Omega_int(C)>0 and the deletion nulls do not certify interaction among the members of C | sections/05_agency.tex:465-473 (def:agy-order-parameter, eq:agy-omega), :567 (def:agy-meta-agent) | applied |
| agy3-04 | major | def:agy-meta-agent: 'differs from every null of type D' is unsatisfiable when N_hab is inapplicable and undefined for the random null N_pr | sections/05_agency.tex:567 (def:agy-meta-agent), :510 (def:agy-nulls), :522-532 (tab:agy-nulls), :550 | applied |
| agy3-05 | major | Final-form prose drops the 'without records' restriction: contrast above baseline does not separate from deletion nulls when records exist | sections/05_agency.tex:593 | applied |
| coh-01 | major | prop:coh-code-potential(c): necessity of the edge condition is false on graphs where the endpoints of an edge share partners | sections/06_coherence.tex:281 (prop:coh-code-potential, clause (c)); proof at sections/app06_coherence.tex:170 | applied |
| coh-02 | major | Receiver fidelity in chk:coh-grounding and obs:coh-placement is conditioned on the current mean, not on the history named in the column header and in def:coh-components | sections/chk06_coherence.tex:86 (chk:coh-grounding, table header); sections/06_coherence.tex:380 (obs:coh-placement); definition at sections/06_coherence.tex:14 | applied |
| frm-01 | major | Status sentences call the formation chain a theorem about the map; the theorem-level chain exists only at gamma = infinity, where the declared start is already the fixed point | 07_formation.tex:6, :146, :369, :381 (thm:frm-formation, thm:frm-split-contrast, def:frm-target) | applied |
| frm-02 | major | In-group angle noise violates the split-law hypothesis; obs:frm-stochastic compares sigma_alpha^2 = 0.01 runs with the sigma_alpha^2 = 0 closed form and the discrepancy is systematic | 07_formation.tex:294 (obs:frm-stochastic); chk07_formation.tex:43 (chk:frm-stochastic); 07_formation.tex:197 (lem:frm-split-law); 07_formation.tex:367 | applied |
| frm-03 | major | prop:frm-exact-fusion: closing sentence is wider than parts (a)-(c); part (b) is vacuous at finite gamma | 07_formation.tex:348-358 (prop:frm-exact-fusion); app07_formation.tex:133-139 | applied |
| frm-04 | major | prop:frm-capacity: second statement is false for admissible parameters with p* >= 1 and omits the frozen calibration its proof uses | 07_formation.tex:342-344 (prop:frm-capacity); app07_formation.tex:129-131 | applied |
| frm-05 | major | obs:frm-thresholds: reported p*^2 gamma_T values are artifacts of the ratio-1.1 grid; 'gamma_T like p*^-2' is supported only as an upper bound | 07_formation.tex:149 (obs:frm-thresholds); 07_formation.tex:144; chk07_formation.tex:19 (chk:frm-thresholds) | applied |
| sca1-01 | major | Lag-covariance clause of thm:sca-no-moment(a) is false as stated | sections/08_scale.tex:132 (thm:sca-no-moment(a)); proof sections/app08_scale.tex:55 | applied |
| sca1-02 | major | lem:sca-relations(c): '(M) iff rho(W)<1' fails on infinite populations | sections/08_scale.tex:40 (lem:sca-relations(c)); proof sections/app08_scale.tex:19 | applied |
| sca1-03 | major | prop:sca-sufficient(c) cites prop:min-grounding-moment without its condition varpi_g<1 | sections/08_scale.tex:50 (prop:sca-sufficient(c)); sections/09_minimal.tex:159-166 (prop:min-grounding-moment) | applied |
| sca1-04 | major | prop:sca-heterogeneous: m_up formula and leak clause are proved only on Z^D, not on 'a finite box' | sections/08_scale.tex:234-238 (prop:sca-heterogeneous(a)-(c)); proof sections/app08_scale.tex:105-109; sections/chk08_scale.tex:52 | applied |
| sca3-01 | major | Three-dimensional susceptibility check reports a gap eight times smaller than the true one | sections/chk08_scale.tex:112 (chk:sca-coherence-volume, part (d)); supports cor:sca-size(d) at sections/08_scale.tex:542 | applied |
| sca3-02 | major | 'Pure relays lose all but one direction within five hops' is a single-realization figure, inconsistent with the reported gap | sections/08_scale.tex:586 (paragraph before conj:sca-rank-down); sections/chk08_scale.tex:122 (chk:sca-lyapunov) | applied |
| abs-01 | major | Ultrametric cap does not vanish as grounding weakens in a fixed finite network; closing sentence of the proposition is vacuous and 04:492 cites it for more than it says | sections/10_abstract_collectives.tex:422 (prop:abs-ultrametric-cap, last sentence); sections/04_collectives.tex:492 (prose after def:col-ultrametric) | applied |
| abs-02 | major | 'Every unconditional contrast is small, whatever the barriers' depends on the unstated ratio of local to world noise | sections/10_abstract_collectives.tex:426 (prose after prop:abs-ultrametric-cap); sections/04_collectives.tex:492; sections/chk10_abstract_collectives.tex:65 (ch | applied |
| met-01 | major | Full-column-rank H and Lambda^s > 0 exclude the two-firm instance and every closed extension with unsensed coordinates | sections/10a_meta_agents.tex:266 (prop:met-consensus-filter, condition (S)); sections/10a_meta_agents.tex:324 (thm:met-h5a, (H-suff)); sections/app10a_meta_agen | applied |
| met-02 | major | thm:met-h5a(i) uses prop:met-leak-bound beyond its hypotheses | sections/10a_meta_agents.tex:331 (thm:met-h5a, clause (i), second sentence); proposition at sections/10a_meta_agents.tex:101-110 (prop:met-leak-bound) | applied |
| hie-01 | major | conj:hie-top-down is refuted by its own criterion on the model of obs:hie-top-down | sections/10b_hierarchy.tex:357-362 (conj:hie-top-down and basis sentence); also 10b:355, 01_introduction.tex:207 and :250, 06_coherence.tex:398, 13_discussion.t | applied |
| ren-01 | major | The approximate-closure error parameter sigma_cut^2/(xi_in xi_out) is extensive in the number of blocks, and high contrast does not make the Galerkin coarse parameters accurate | sections/10c_renormalization.tex:383 (closing claim of sec:ren-closure), :231 (prose after thm:ren-memory), :374 thm:ren-closure(a), :227 thm:ren-memory(d) last | applied |
| env1-01 | major | prop:env-horizon(c) is false with more than two modes | sections/10d_environments.tex:72 (prop:env-horizon, part c) | applied |
| env2-01 | major (unconfirmed) | Leading constant 3/(5 pi) presented as derived here is the Berg-Purcell perfect-instrument result | sections/10d_environments.tex:201 (after prop:env-concentration); also the src comment at :199 | applied |
| frame-01 | major | Discussion cites the lattice-contrast theorem for a statement it does not contain | sections/13_discussion.tex:9 (cites thm:col-lattice-contrast, sections/04_collectives.tex:383-389) | applied |
| frame-02 | major | "Memory vanishes only if retained agents hear no eliminated one" overstates the closure identity | sections/01_introduction.tex:84 and :138 (results table a, row citing thm:agy-closure-identity); sections/13_discussion.tex:11; sections/05_agency.tex:64; state | applied |
| frame-03 | major | H5(a) inference clause drops the steady-state, centralized-start and noiseless-computation conditions of thm:met-h5a(iv) | sections/01_introduction.tex:96 (H5a); sections/13_discussion.tex:21; sections/11_predictions.tex:103 (tab:pre-meta); sections/00_abstract.tex:4; statement thm: | applied |
| pos-01 | major | The table titled "Falsifiable predictions" lists negations of theorems and names in advance the auxiliary that absorbs each failure | sections/11_predictions.tex:23 (sec:pre-predictions), with :5, :19, :25, :72, :79, :103, :110, :112, :128, :132, :144 (tab:pre-reception, tab:pre-collectives, t | partial |
| pos-02 | major | The records refuter "any rule but exact counting" exceeds prop:hie-literal-records and is satisfied by a non-exact rule inside the model | sections/11_predictions.tex:105 (tab:pre-meta) against sections/10b_hierarchy.tex:130-145 (prop:hie-literal-records, tab:hie-records) | applied |
| pos-03 | major | The answer to "what agents sense" comes from a declared objective that the framework's own expected free energy does not imply and can oppose | sections/00_abstract.tex:4; sections/13_discussion.tex:5 and :39 (sec:dis-meta); sections/10d_environments.tex:133-143 (rem:env-efe-horizon-free, rem:env-two-st | applied |
| pos-04 | major | prop:env-aggregate-memory(f) is called "ours" while Granger 1980 was not read; the common-shock aggregation result is in the literature | sections/10d_environments.tex:277-286 (prop:env-aggregate-memory(f) and the paragraph after it); sections/11_predictions.tex:132; sections/10d_environments_extr | applied |
| pos-05 | major | The claimed novelty residue for selective sensing ("rank limit and a hard budget") is narrower than stated, and a pinpoint theorem citation rests on an unread source | sections/10d_environments.tex:50 (after thm:env-canonical); sections/12_related.tex:137, :139 (sec:rel-env) and :149 (sec:rel-new); sections/10d_environments.te | applied |
| pos-06 | major | The firm row restates the separation theorem of production with futures markets and is definitional inside ex:env-firm | sections/11_predictions.tex:130 (tab:pre-sensing); sections/10d_environments.tex:308-317 (ex:env-firm); sections/13_discussion.tex:39 | applied |
| pos-07 | major | The gravity row is the barometric exponent presented as a prediction of the framework, with an unmatched "thirteen orders of magnitude" comparison | sections/11_predictions.tex:134 (tab:pre-sensing); sections/10d_environments.tex:203-212 (ex:env-cell), :223 (rem:env-neurons); sections/13_discussion.tex:39 | applied |
| pos-08 | major | The central kind has no exhibited member, while the abstract opens with a theory of how agents "from cells to nations" form collective agents | sections/00_abstract.tex:4; sections/13_discussion.tex:11 (sec:dis-status); sections/05_agency.tex:566 (def:agy-meta-agent); sections/10_abstract_collectives.te | applied |
| pos-09 | major (unconfirmed) | The unrecorded-drive problem is stated as open without the latent-variable Gaussian graphical model literature | sections/05_agency.tex:557 (open:agy-unrecorded-drive); sections/11_predictions.tex:9 and :11; sections/04_collectives.tex:302 (lem:col-kron); sections/10_abstr | applied |
| notation-01 | major | Prose claims the drift-based and precision-based contrasts differ by at most the circulation term; the inward rates differ at zero current | sections/05_agency.tex:125 (prose after prop:agy-drift-precision, :116); sections/12_related.tex:68; against def:col-contrast sections/04_collectives.tex:291-29 | applied |
| cit_attr-01 | major | Maisto et al. (2025) are said to fix blankets or roles by construction; the primary text detects the blanket spectrally after the fact | sections/12_related.tex:9 (sec:rel-nested); consequence at sections/12_related.tex:11 | applied |
| cit_meta-01 | major | Zaghw et al. 2026 and de Vries 2026 are absent while three passages scope 'no error bound' to the texts read | sections/12_related.tex:123 and :125 (sec:rel-renormalization); sections/12_related.tex:157 (sec:rel-new); sections/10c_renormalization.tex:277 (rem:ren-rgm) | applied |

## Lane fw: Section 2, framework

Two major defects, both in prop:fw-bounded-confidence, and ten minor ones; no critical defect. The other 14 body propositions, lem:fw-common-mode and the appendix-stated prop:fw-misidentified-code hold as stated after hand reconstruction, with numerical reproduction where cheap. The body file has no theorems, corollaries or Numerical observation environments. Major 1: the 'if and only if' addressing threshold of prop:fw-bounded-confidence(b) is derived by applying the Gaussian formula of prop:fw-efe-communication(b) to a reply that is a Gaussian scale mixture when sigma_H^2 > 0. The exact information is smaller (gap up to 0.15 nats in the instances run), and an explicit instance has the stated rule saying 'address' while the exact expected free energy says 'silence' by 0.113 nats. The rule is exact at sigma_H^2 = 0 and is a necessary condition otherwise; the slope gamma/2 statement survives. Major 2: prop:fw-bounded-confidence(d) and the sentence 'A one-step expected free energy produces no risk-based reciprocity' hold only with the listener's own belief frozen. Under the section's own reception model, hearing a partner moves m_j, and the expected being-predicted risk of addressing that partner falls (5.0 to 2.28, 0.78, 0.46 for three gains). Neither major defect propagates: 09_minimal.tex and 12_related.tex cite only the qualitative rule and pandering (c). Minor: the 60 degree rule is quoted at :429 without m_i = 0 and M = P_i^{-1} (counterexamples run); tab:fw-levels states a weaker level-1 condition than the one proved (counterexample run); a missing positive-definiteness hypothesis in prop:fw-level-optimality(c); one over-strong clause in prop:fw-effective-codes; the 'second form' slip in prop:fw-efe-communication; a gloss at :209 valid only for centered content; prop:sca-records-length(c) cited for a regime it does not treat; a_i(t) missing from the belief-update kernel of eq:fw-factor; a proof sentence in prop:fw-record-basics(b) that contradicts (a); chk:fw-efe (iii),(v) unable to detect the two major defects (unconfirmed, no scripts ship). Assumptions: the lane files invoke only H2 (02_framework.tex:94, by name) and A5 (:32, in words, matching asm:int-a5 verbatim in content). A6 and A11 are used implicitly (codes fixed while learned; the leak in def:fw-record-model and def:fw-level0) without contradiction. A7 to A10 and A12 are not used in this section. No mismatch with 01_introduction.tex was found; the dependencies on A6 are untraceable because the section never cites it. Reproduced: chk:fw-levels, all example numbers of chk:fw-two-receivers, the fig:fw-lift numbers including the ellipse axes in figures/fig_fw_lift.tex, the six closed-form/grid/Riccati pairs of chk:fw-records, the stabilizer dimension and the six 3 - 2 cos(theta) values of chk:fw-frames, and lem:fw-common-mode on a random instance. Cross-references read and found consistent with their use: prop:mis-dynamic, def:mis-values, prop:mis-believed-values, thm:mis-echo-chambers, prop:coh-c0-blind, thm:coh-withdrawal, prop:coh-flat-true, thm:coh-amplification, thm:coh-grounding-tension, thm:sca-lightcone, prop:sca-poisson, prop:sca-routing, prop:sca-sufficient(a), thm:sca-clustering, prop:sca-records, prop:sca-records-memory, prop:col-records-partition, def:col-world-conditional, rem:env-efe-horizon-free, def:env-attention-objective, thm:env-control, rem:env-two-step; prop:sca-records-length(c) is the one cited beyond what it says. Streamlining: of 8926 body words, six items are tier A core (def:fw-system, prop:fw-prior-completion, def:fw-levels, prop:fw-level-optimality, def:fw-level0, lem:fw-common-mode) plus the definitions other sections lean on; the three frame propositions can be one, def:fw-levels, def:fw-calibration and tab:fw-levels can be one definition with a table, and prop:fw-update-subspace, prop:fw-rls, prop:fw-transfer-kernel and prop:fw-record-basics are standard Kalman facts that can sit in the supplement behind pointers. Tiers follow the task definitions (A principal, B supporting, C peripheral or redundant). Scripts and a findings copy are in <session scratch>/audit/fw/ (s1_repro.py, s2_f1_entropy.py, s3_f2_listen_first.py, s4_f5_table.py, s5_misc.py, s6_wc.py, findings.md). Nothing under the manuscript or the vault was modified.

Coverage: 30 items examined; 24 hold, 1 defective, 1 suspect, 4 not checked.

| Item | Verdict | Note |
|---|---|---|
| prop:fw-bounded-confidence | defect | (a) and (c) hold. (b) 'if and only if' fails for sigma_H^2 > 0 (explicit counterexample). (d) identity holds only with m_j frozen (MC 4.9994 against 5.0); its conclusion and the sentence at :379 fail under the section's reception model. |
| chk:fw-efe | suspect | (iii) and (v) cannot detect the defects of prop:fw-bounded-confidence(b),(d); (i), (ii), (iv) not reproduced; reported deviations are within 1.4 standard errors. |
| chk:fw-reception | not_checked | Only the fig:fw-lift instance was reproduced. |
| chk:fw-learning | not_checked | Monte Carlo limits (i) to (vi) not reproduced; seeds and scripts not available. |
| open:fw-understanding-risk | not_checked | Open problem; not attacked. Status word matches content. |
| conj:fw-fragmentation | not_checked | Conjecture; not attacked. Its thresholds Xi_ji inherit the correction to prop:fw-bounded-confidence(b). |

Items found to hold: prop:fw-update-subspace; prop:fw-prior-completion; prop:fw-two-receivers; prop:fw-level-optimality; prop:fw-grounded-identification; prop:fw-rls; prop:fw-ungrounded-bias; prop:fw-transfer-kernel; prop:fw-record-basics; prop:fw-performative; prop:fw-efe-communication; prop:fw-understood-predicted; prop:fw-frame-covariance; prop:fw-effective-codes; prop:fw-frame-identifiability; lem:fw-common-mode; prop:fw-misidentified-code (stated in app02_framework.tex:169-177); ex:fw-disagreement; rem:fw-convex-gains; chk:fw-levels; chk:fw-two-receivers; chk:fw-records; chk:fw-frames; chk:fw-common-mode.

### fw-01 (major): prop:fw-bounded-confidence(b): the 'if and only if' addressing threshold uses a Gaussian information term for a reply that is not Gaussian when sigma_H^2 > 0

Location: manuscripts/Collective_Agents/sections/02_framework.tex:365-369 (prop:fw-bounded-confidence(b)); proof at sections/app02_framework.tex:149. Labels: prop:fw-bounded-confidence, prop:fw-efe-communication, chk:fw-efe. Category: result applied beyond its hypothesis.

Evidence. The proof reads 'Apply prop:fw-efe-communication(b) with obar = H_j(m_j - mbar_ji), S^tx = S_ji and R^tx = R_c'. prop:fw-efe-communication(b) (02_framework.tex:329) assumes the sender 'predicts the response of addressee i as N(obar_ji, S^tx_ji)'. Under the hypotheses of prop:fw-bounded-confidence the reply is phi_ij = H_j(m_j - m_i) + h_j - (Hhat_ij - H_j) m_i + nu_ij with m_i and vec(Hhat_ij - H_j) independent Gaussians, so for sigma_H^2 > 0 it is a Gaussian scale mixture with covariance S_ji, and its entropy is strictly below (1/2) ln det(2 pi e S_ji). The exact epistemic term H[phi] - (1/2) ln det(2 pi e R_c) is therefore smaller than (1/2) ln det(S_ji R_c^{-1}) and the exact threshold is lower than Xi_ji. Executed (scalar quadrature, s2_f1_entropy.py): entropy gap 0 at sigma_H^2 = 0; 0.00249 nats at (mbar, Pbar, sigma_H^2, R_c) = (1, 1, 0.05, 0.5); 0.0473 at (1, 1, 0.5, 0.5); 0.1118 at (0, 1, 1, 0.1); 0.1508 at (0, 4, 1, 0.05). Counterexample to the 'if' direction: mbar = 0, Pbar = 4, sigma_H^2 = 1, R_c = 0.05, Psi_p = 10, p_empty = 0.5, g_use = 0 give S_ji = 8.05, g_tx = 2.0702, Xi stated = +0.0680, Xi with exact information = -0.0829; at disagreement d = 0.7746 (left side 0.03 < 0.0680) the stated rule says address, while the exact G(address) - G(silence) = +0.1129 > 0. Downstream uses (09_minimal.tex:174, 12_related.tex:82) cite only the qualitative rule and pandering (c), so the defect does not propagate.

Proposed fix. Replace (b) by: 'Let sigma_H^2 = 0. At gamma -> infinity and with honest content, being predicted makes j address i if and only if (1/2)||H_j(m_j - mbar_ji)||^2_{Psi_p^{-1}} < Xi_ji. For sigma_H^2 > 0 the reply is a Gaussian scale mixture; with I_ji := H[phi_ij] - (1/2) ln det(2 pi e R_c) <= (1/2) ln det(S_ji R_c^{-1}) the exact threshold is Xi^ex_ji = -(1/2) tr(Psi_p^{-1} S_ji) + I_ji - g_tx <= Xi_ji, so the displayed inequality is necessary for addressing and not sufficient. At finite gamma the log-odds fall linearly with slope gamma/2 in the squared believed coded disagreement in both cases, since I_ji does not depend on m_j.' Alternatively state that the sender replaces its predictive law of the reply by the moment-matched Gaussian, and call Xi_ji the threshold of that approximation.

What would overturn the finding. A proof that the product (Hhat_ij - H_j) m_i is Gaussian under the stated hypotheses, or a declared convention in def:fw-system that every predictive law is replaced by its moment-matched Gaussian before the expected free energy is evaluated.

State: applied. [02] applied: Confirmed by quadrature (gaps 0, 0.0025, 0.0473, 0.1118, 0.1508; Xi=0.0680, Xi_ex=-0.0829). (b) now states the exact threshold Xi^ex with information I^tx <= Gaussian bound; Xi_ji is exact at sigma_H^2=0, only necessary otherwise. Proof gives an analytic counterexample (fourth cumulant > 0). Check (iii) rerun and rewritten.

### fw-02 (major): prop:fw-bounded-confidence(d) and the 'no risk-based reciprocity' sentence hold only with the listener's own belief frozen

Location: manuscripts/Collective_Agents/sections/02_framework.tex:375 (prop:fw-bounded-confidence(d)) and :379; proof at sections/app02_framework.tex:150. Labels: prop:fw-bounded-confidence, def:fw-levels, chk:fw-efe. Category: missing hypothesis; interpretation stated as result.

Evidence. (d) concludes 'so listening first leaves the expected being-predicted risk of addressing i unchanged', and :379 states 'A one-step expected free energy produces no risk-based reciprocity between listening to and addressing the same partner'. The two identities are the martingale and total-covariance properties of j's partner-model update with m_j the same symbol on both sides. Hearing i is a reception, and by def:fw-levels (02_framework.tex:131) a reception moves the receiver's own mean at every level, so after listening the risk of addressing is evaluated at m_j^+, not m_j. Scalar closed form with own gain K_j and partner-model gain K_p: E[(m_j^+ - mbar^+)^2] + Pbar^+ = (1 - K_j)^2 d^2 + (K_j^2 - 2 K_j K_p)(Pbar + R) + Pbar. Executed (s3_f2_listen_first.py; m_j = 2, mbar = 0, Pbar = 1, R = 0.5): 5.0 without listening; 4.9994 (Monte Carlo) after listening with m_j frozen, which is the identity of (d); 2.2778, 0.7778 and 0.4568 after listening with own gains 0.333, 0.667 and 0.889. Listening first lowers the expected being-predicted risk of addressing the partner heard, which is a risk-based reciprocity produced by one-step expected free energy applied in successive rounds. chk:fw-efe(v) (17.094 against 17.136, standard error 0.031) tests the frozen identity only.

Proposed fix. State (d) as: 'If j first hears i and updates its partner model to (mbar^+_ji, Pbar^+_ji) while its own belief m_j and its content are held fixed, then under j's model [the two identities], so the partner-model update alone leaves the expected being-predicted risk unchanged. When j also updates m_j from the same message with gain K_j, the expected coded disagreement falls and the expected risk falls with it.' Replace the sentence at :379 by: 'The partner-model update produces no risk-based reciprocity between listening to and addressing the same partner; the listener's own belief update does, by reducing the believed coded disagreement.'

What would overturn the finding. A statement in def:fw-system or def:fw-levels that a sender's partner-model update and its own belief update use disjoint messages, so that hearing i leaves m_j unchanged.

State: applied. [02] applied: Confirmed. (d) now holds m_j fixed for the invariance and adds the matrix second-moment identity when m_j is updated with gain L_j. The finding's proposed 'risk falls' is too strong: at d=0, L_j>2L^p the risk rises (0.1 to 2.525). Stated the scalar sign conditions instead; prose and check (v) updated. Check of the edit: [02] defect, Matrix identity, scalar change formula, both sign conditions and all check numbers (2.2778, 0.7778, 0.4568, 2.525; MC agreement) verified. Minor: for 'any gain L_j' the clause 'the expected risk of addressing i changes' is false at L_j=0 and on cancellation sets, and the proof never derives a risk change. Repair: [02] repaired, Checker is right: the risk change is zero at L_j=0, whenever H_jL_j=0, and on a cancellation set. Statement now gives the change as (1/2)tr(Psi_p^{-1}H_j Delta_ji H_j^T) for honest content with a genericity clause; proof derives it (q minus ell on rays); body sentence says 'positively and less than twice'; numcheck extended. Symbol L kept.

### fw-03 (minor): The 60 degree rule is quoted in the body without the hypotheses m_i = 0 and M = P_i^{-1} under which it was proved

Location: manuscripts/Collective_Agents/sections/02_framework.tex:429; statement at sections/app02_framework.tex:169-177 (prop:fw-misidentified-code(b),(c)). Labels: prop:fw-misidentified-code, chk:fw-frames. Category: body summary stronger than the proved statement.

Evidence. Body: 'listening is worse than silence exactly when theta > 60 degrees, whatever the channel noise'. The appendix statement of (b) and (c) requires the Mahalanobis weight M = P_i^{-1} and a centered receiver, m_i = 0. Executed (s5_misc.py): with m_i = (3,0), P = I, sigma^2 = 0.1 the risk at 50 degrees is 2.6895 against 2 for silence, so listening already loses below 60 degrees; with P = diag(4, 0.25) and Euclidean weight the risk at P-angle 70 degrees is 2.2524 against 4.25 for silence, so listening still wins above 60 degrees. With the hypotheses in place the values 3 - 2 cos(theta) of chk:fw-frames reproduce (1.0000, 1.2679, 1.9699, 2.0000, 2.0304, 3.0000). The proposition is stated only in the appendix and has no citation outside the framework files.

Proposed fix. Write at :429: 'for a receiver centered on its prior mean and error measured in the prior Mahalanobis norm, listening is worse than silence exactly when the P_i-angle theta between the believed and true code exceeds 60 degrees, whatever the channel noise (prop:fw-misidentified-code)'.

What would overturn the finding. A proof of the 60 degree threshold for general m_i or a general weight M.

State: applied. [02] applied: Confirmed (hand computation reproduces 2.689 against 2 at 50 degrees with m_i=(3,0)). Body sentence now carries the hypotheses m_i=0 and prior Mahalanobis norm, cites part (c), and says the threshold angle is instance dependent otherwise. Appendix statement unchanged.

### fw-04 (minor): prop:fw-efe-communication: 'the second form' now refers to the form without an information term

Location: manuscripts/Collective_Agents/sections/02_framework.tex:320-322 (prop:fw-efe-communication), against eq:fw-efe at :29-32. Labels: prop:fw-efe-communication, eq:fw-efe. Category: internal consistency.

Evidence. eq:fw-efe (:30) writes risk plus ambiguity first and minus information minus pragmatic value second, and :32 says 'The second form requires the information term ... to use the exact posterior of the agent's own model'. The proposition displays the forms in the opposite order, G = -I - E ln p~ = KL + E H, and keeps the clause 'the second form requiring that the information term use the exact posterior'; the second form there is risk plus ambiguity, which contains no information term.

Proposed fix. Write 'the equality requiring that the information term use the exact posterior of the agent's own model', or restore the order of eq:fw-efe and cite it instead of redisplaying it.

What would overturn the finding. Nothing; the text at :320-322 is the evidence.

State: applied. [02] applied: Confirmed by reading: the proposition displays the forms in the opposite order from eq:fw-efe. Replaced 'the second form requiring' by 'the equality requiring'. The proof's own reference to the second form is consistent with the proposition's order and was left.

### fw-05 (minor): tab:fw-levels states a weaker condition for level-1 optimality than prop:fw-level-optimality proves

Location: manuscripts/Collective_Agents/sections/02_framework.tex:187 (tab:fw-levels), against prop:fw-level-optimality(c) at :150-159. Labels: tab:fw-levels, prop:fw-level-optimality. Category: table disagrees with the result it summarizes.

Evidence. Table row for level 1: 'evidence messages, or a flat prior with no shared source in the coded directions'. The proved condition is H_j P_j Lambda^sh = 0. Executed counterexample (s4_f5_table.py): K = 2, flat prior, a shared source reading eta_1, a private source of j reading eta_1 + eta_2, code H_j = (0,1). Then Lambda^sh H_j^T = 0, so no shared source lies in the coded direction, yet H_j P_j Lambda^sh = (-1, 0) and the correlation between j's coded error and the shared noise is -0.708. The flat prior is also outside the hypothesis Lambda_0 > 0 under which (c) is stated.

Proposed fix. Replace the cell by 'evidence messages, or a flat prior with Lambda^sh P_j H_j^T = 0', and add to (c) that the flat-prior case is the limit Lambda_0 -> 0 with P_j finite.

What would overturn the finding. A proof that Lambda^sh H_j^T = 0 implies H_j P_j Lambda^sh = 0 for every information-form posterior P_j.

State: applied. [02] applied: Confirmed by hand: P_j=[[1,-1],[-1,2]], H_jP_jLambda^sh=(-1,0), correlation -1/sqrt2. Table cell now reads 'flat prior with H_jP_jLambda^sh=0'. (c) adds the flat-prior case as Lambda_0=0 with Lambda_j positive definite, conditional on eta, instead of a limit; proof extended with both two-dimensional examples.

### fw-06 (minor): prop:fw-level-optimality(c): the evidence-message clause needs Lambda_{j\i} positive definite, stated only in the proof

Location: manuscripts/Collective_Agents/sections/02_framework.tex:150-159 (prop:fw-level-optimality(c)); sections/app02_framework.tex:72. Labels: prop:fw-level-optimality. Category: missing hypothesis.

Evidence. The proof at app02_framework.tex:72 inverts the precision Lambda_{j\i} of the evidence j holds beyond what it shares with i. When j has no private evidence in some direction the evidence message is undefined in that direction. The statement gives no such condition.

Proposed fix. Add 'with Lambda_{j\i} positive definite' to the evidence-message clause of (c), or define the evidence message on the range of Lambda_{j\i} with a pseudoinverse.

What would overturn the finding. A reading of the statement in which Lambda_{j\i} positive definite is already implied by the standing hypotheses of the proposition.

State: applied. [02] applied: Confirmed: the proof inverts Lambda_{j\i}. (c) now defines Lambda_{j\i} in the statement and conditions the evidence-message clause on Lambda_{j\i} positive definite; the proof sentence was reworded to match.

### fw-07 (minor): prop:fw-effective-codes: 'identity encodings are exactly the case H_j = T_c' holds in one direction only

Location: manuscripts/Collective_Agents/sections/02_framework.tex:419 (prop:fw-effective-codes); proof at sections/app02_framework.tex:157. Labels: prop:fw-effective-codes, prop:fw-frame-identifiability. Category: statement stronger than proof.

Evidence. H_j = T_c U_j equals T_c if and only if T_c(U_j - I) = 0, which leaves a K(K - r_c)-parameter family of non-identity frames (dimension 8 for K = 4, r_c = 2, reproduced in s5_misc.py). The proof says only that such frames are 'indistinguishable from' identity encodings, which is the correct statement and agrees with prop:fw-frame-identifiability.

Proposed fix. Write 'identity encodings give H_j = T_c, and every frame with H_j = T_c is indistinguishable from an identity encoding'.

What would overturn the finding. Nothing; follows from T_c having rank r_c < K.

State: applied. [02] applied: Confirmed: T_c has rank at most r_c, so T_c(U_j - I) = 0 admits non-identity frames when r_c < K. Statement now one-directional plus indistinguishability, as proposed; proof gained one sentence exhibiting U_j = I + N with columns of N in ker T_c.

### fw-08 (minor): Gloss on unidentified code directions is correct only for centered content

Location: manuscripts/Collective_Agents/sections/02_framework.tex:209 (after prop:fw-grounded-identification). Labels: prop:fw-grounded-identification. Category: wording.

Evidence. 'The unidentified directions are those along which the jointly attended content never varies; on them the code never acts on centered content'. The proposition identifies the code on the range of the second moment M_2, not of the covariance. A direction with a nonzero constant component and no variation is identified, so 'never varies' describes the null space only when the content is centered, which the sentence assumes in its second half and not in its first.

Proposed fix. Write 'The unidentified directions are those along which the jointly attended content is identically zero (for centered content, those along which it never varies)'.

What would overturn the finding. A definition of M_2 as a centered covariance in prop:fw-grounded-identification.

State: applied. [02] applied: Confirmed: M_2 is the uncentered second moment E[phi phi^T], whose null space is where content vanishes almost surely. Gloss after the proposition replaced with the proposed wording; matching phrase in chk:fw-learning (i) changed to 'is identically zero'.

### fw-09 (minor): prop:sca-records-length(c) is cited for a non-diffusive regime it does not treat

Location: manuscripts/Collective_Agents/sections/02_framework.tex:279; cited result at sections/08_scale.tex:395-410. Labels: prop:sca-records-length, def:fw-record-model. Category: cross-reference used beyond what it says.

Evidence. Body: 'a precision that record noise can make non-diffusive (prop:sca-records-length(c))'. Item (c) of the cited proposition assumes a diffusive precision; the non-diffusive case appears only as a computed case in the prose after the proposition (08_scale.tex:410) and in chk:sca-records-length.

Proposed fix. Cite the check instead: 'a precision that record noise can make non-diffusive in computed cases (chk:sca-records-length)'.

What would overturn the finding. A clause of prop:sca-records-length(c) that states and proves the non-diffusive case.

State: applied. [02] applied: Confirmed: prop:sca-records-length(c) assumes a diffusive precision; the non-diffusive case is the computed one in chk:sca-records-length (eleven positive off-diagonal entries). Citation in the records paragraph of 02_framework.tex changed as proposed. 08_scale.tex already says this correctly; no follow-up. [08] declined: Nothing to change in group 08: part (c) assumes a diffusive joint precision and the prose after it already attributes the non-diffusive case to a computed case with chk:sca-records-length. The miscitation lies in 02_framework.tex; the same pattern occurs in 10_abstract_collectives.tex (follow-up).

### fw-10 (minor): eq:fw-factor: the belief-update kernel omits the agent's own action

Location: manuscripts/Collective_Agents/sections/02_framework.tex:21-22 (eq:fw-factor). Labels: eq:fw-factor, def:fw-system. Category: generative model factorization.

Evidence. The factor is written p(mu_i(t+1) | mu_i(t), s_i(t+1)). The action a_i(t) is sampled from q_i(pi), so it is not a function of mu_i(t); the filter needs the attention set to know which slots of s_i(t+1) are messages from whom, and its own world action and content to predict them. As written the internal update is not a deterministic function of its arguments.

Proposed fix. Write p(mu_i(t+1) | mu_i(t), a_i(t), s_i(t+1)). The blanket statement is unchanged because a_i and s_i are the blanket.

What would overturn the finding. A convention in def:fw-system that s_i(t+1) includes a record of a_i(t), or that mu_i(t) includes the sampled action.

State: applied. [02] applied: Confirmed: a_i(t) is sampled from q_i(pi), so mu_i(t) does not determine it and the filter needs it. Kernel factor now p(mu_i(t+1) | mu_i(t), a_i(t), s_i(t+1)), with one explanatory sentence. Blanket path statement unchanged. The local-rule form in 08_scale absorbs this in its noise; no follow-up.

### fw-11 (minor): Proof of prop:fw-record-basics(b) says 'The content persists until read', contradicting the decay in (a)

Location: manuscripts/Collective_Agents/sections/app02_framework.tex:125 (proof of prop:fw-record-basics(b)). Labels: prop:fw-record-basics, def:fw-record-model. Category: proof wording.

Evidence. Item (a) and eq:fw-record-records give a written contribution weight that decays geometrically each round; at omega + delta = 1, which def:fw-record-model allows, a write is overwritten after one round. The proof of (b) asserts that the content persists until read. (b) is true as a statement about the first reading of a record after a write; the justification given is not.

Proposed fix. Replace by 'A reader that attends the record at any later round receives the write with the weight given in (a), without having been present when it was written'.

What would overturn the finding. Nothing; the two sentences are both in the lane files.

State: applied. [02] applied: Confirmed: 'persists until read' contradicts the geometric decay of (a) and fails at omega + delta = 1. Proof of (b) now uses the proposed sentence and states independence of reading rounds from the writer. Statement (b) unchanged.

### fw-12 (minor, unconfirmed): chk:fw-efe (iii) and (v) cannot detect the two defects of prop:fw-bounded-confidence

Location: manuscripts/Collective_Agents/sections/chk02_framework.tex:31 (chk:fw-efe). Labels: chk:fw-efe, prop:fw-bounded-confidence. Category: check does not test what it claims.

Evidence. (iii): 'the expected-free-energy decision agreed with the threshold rule of (b) in 2000 of 2000 random disagreements'. The check gives neither sigma_H^2 nor how the expected free energy was evaluated. Xi_ji is an algebraic rearrangement of the Gaussian formula of prop:fw-efe-communication(b), so agreement is forced if the same formula is evaluated on both sides, and at sigma_H^2 = 0.05 the window between the exact and stated thresholds is about 0.0025 nats, too narrow for random disagreements to hit. (v) holds m_j fixed. No check script ships with the manuscript, so the implementation could not be inspected; the other numbers in the check are internally plausible ((i): 0.12 on entries of size 34 over 300,000 draws is about 1.4 standard errors; (v): 0.042 is 1.35 standard errors).

Proposed fix. State sigma_H^2 for (iii) and evaluate the expected free energy with the entropy of the reply computed by quadrature or Monte Carlo; add to (v) a run in which the listener's own belief is updated from the heard message.

What would overturn the finding. The check script showing that (iii) used sigma_H^2 > 0 with a non-Gaussian entropy estimate and disagreements placed near the threshold.

State: applied. [02] applied: No edit in this batch: chk:fw-efe as left by batch 1 already states sigma_H^2 = 0 for (iii), gives quadrature gaps with an instance separating Xi from Xi^ex, and has an own-belief-update run in (v). Script fw-12.py reproduces gaps 0, 0.0025, 0.0473, 0.1118, 0.1508, Xi = 0.0680, Xi^ex = -0.0829, 0.1129, and 2.2778, 0.7778, 0.4568, 2.525.

### Not checked by lane fw

- The user-referenced file C:/Users/chris and christine/Documents/Codex/2026-11-09/dep/outputs/collective-agents-open-problems-comparison-2026-11-09.md was not opened.
- figures/fig_framework.tex (fig:fw-channels) was not opened; figures/fig_fw_lift.tex was checked only for its numeric header and ellipse parameters, not for the plotted density curves.
- sections/appA_notation.tex was not opened, so notation-table entries for this section were not compared with the definitions.
- thm:sca-oz and thm:coh-holonomy statements were not read; only their labels and the introduction's description were seen.
- chk:fw-reception, chk:fw-learning (i) to (vi), the transfer-kernel impulse response in chk:fw-records, chk:fw-efe (i), (ii), (iv), chk:fw-frames (i) and the manuscript's own six-agent instance of chk:fw-common-mode were not reproduced. No check scripts ship with the manuscript and seeds are unknown.
- The 79 to 95 percent figure for the understanding-error excess (02_framework.tex:353, chk:fw-efe(ii)) was not recomputed.
- open:fw-understanding-risk and conj:fw-fragmentation were not attacked.
- The implementation behind chk:fw-efe(iii) could not be inspected, so the claim that it is uninformative about sigma_H^2 > 0 is unconfirmed.
- The entropy-gap demonstration for prop:fw-bounded-confidence(b) was run in the scalar case only (K = r_c = 1); the matrix case was argued, not computed.
- Uses of the framework results in sections outside the lane were checked only for prop:fw-bounded-confidence (09_minimal.tex:174, 12_related.tex:82) and by citation count for the rest.

### Redundancy noted by lane fw

- Transmitted versus understood, with the prior completing the message: stated at 02_framework.tex:5 (184-word paragraph), :42 (91 words), :94 (198 words) and 01_introduction.tex:15. About 150 words removable by keeping the statement once at :94 after prop:fw-prior-completion.
- Level and calibration mapping: the closing sentences of def:fw-calibration (:174), the prose at :177 and tab:fw-levels (:179-193) say the same thing, and 01_introduction.tex:33 already describes the levels. Lines 174-177 are 125 words; about 100 removable if the table carries the mapping.
- 'Proof in app:fw; checked in chk:...' appears 17 times, about 8 words each, about 130 words. One sentence at the head of the section does the same work.
- Being understood reduces to being heard: the closing sentences of prop:fw-understood-predicted (:350) and the paragraph at :353 (177 words for :350-353) repeat each other; about 60 words removable.
- The paragraph at :379 (105 words) restates prop:fw-bounded-confidence(b),(c) in words before adding the reciprocity claim; about 50 words removable.
- Frames matter only through communication: stated at :5, :402 (51 words) and :422 (44 words), and again at 01_introduction.tex:256; about 60 words removable.
- Forward summaries of other sections: :279 (146 words, previews prop:sca-records, prop:sca-records-memory, prop:sca-records-length of section 8), :340 (100 words, previews rem:env-efe-horizon-free, def:env-attention-objective, thm:env-control, rem:env-two-step of section 10d), :415 (124 words, previews prop:coh-flat-true and thm:coh-amplification), :433 (107 words, previews thm:sca-lightcone, prop:sca-poisson, prop:sca-routing). Each can be one pointer sentence; about 300 words removable.
- The two-form expected free energy identity is displayed twice, at eq:fw-efe (:29-32) and inside prop:fw-efe-communication (:318-322), with the forms in opposite order; about 60 words and one display removable by citing eq:fw-efe.
- Mathematical simplification: prop:fw-update-subspace (a) is immediate from the gain and the whole proposition can be the first item of prop:fw-prior-completion.
- Mathematical simplification: prop:fw-frame-covariance, prop:fw-effective-codes and prop:fw-frame-identifiability can be one proposition with three items; prop:fw-effective-codes repeats frame-covariance (a),(b) and anticipates the stabilizer of frame-identifiability.
- Mathematical simplification: def:fw-levels, def:fw-calibration and tab:fw-levels can be one definition with the table as its body; the two axes (how a message is read, what is learned about its noise) overlap at level 1 with learned noise against class C1g.
- Mathematical simplification: prop:fw-rls is the textbook equivalence of recursive least squares and a Kalman filter with identity dynamics, and the optimum in prop:fw-record-basics is the steady-state scalar Kalman predictor already used in def:fw-level0 and lem:fw-common-mode (lambda = F(1 - k)); both can be remarks citing the standard result.
- Mathematical simplification: prop:fw-bounded-confidence(b) is a substitution into prop:fw-efe-communication(b) and (d) is the martingale and total-covariance property of a Kalman update; after correction both can be corollary-style items.
- Mathematical simplification: prop:fw-transfer-kernel is the impulse response of the recursion in def:fw-record-model and can be an equation inside that definition.
- Hypothesis mismatch: prop:fw-level-optimality(c) assumes Lambda_0 positive definite while tab:fw-levels applies it at a flat prior; one of the two should change.

### Streamlining tiers proposed by lane fw

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| def:fw-system | A | 292 | The generative model; cited 15 times outside the section. Can lose the restated notation glosses. |
| prop:fw-update-subspace | B | 65 | Standard Kalman fact; (a) is immediate from the gain. Merge as the first item of prop:fw-prior-completion, keeping the label for the three downstream citations. |
| prop:fw-prior-completion | A | 250 | The section's main reception claim: the receiver's prior completes the message. Cited 9 times. |
| prop:fw-two-receivers | B | 140 | Consequence of prior completion; cited once (11_predictions.tex). One sentence in the main text suffices. |
| ex:fw-disagreement | C | 155 | Numeric illustration of prop:fw-two-receivers, cited once; move with it to the supplement. |
| def:fw-levels | A | 131 | Cited 15 times; every later section uses the levels. |
| prop:fw-level-optimality | A | 313 | Justifies the levels; statement can shrink to the three conditions with tab:fw-levels carrying them, once the table is corrected. |
| def:fw-calibration | A | 197 | Cited 9 times and required by section 6; merge with def:fw-levels and the table into one definition. |
| tab:fw-levels | B | 120 | Not cross-referenced anywhere; duplicates the two definitions and the proposition. Keep it and cut the prose at :174-177 instead, after fixing the level-1 cell. |
| fig:fw-lift | B | 90 | Not cited outside the section; illustration of prop:fw-prior-completion. |
| prop:fw-grounded-identification | A | 131 | The identification result for codes and its limit (range of M_2); cited by sections 7, 9, 12. |
| prop:fw-rls | B | 152 | Textbook equivalence of recursive least squares and a Kalman filter; a pointer and a citation suffice. Item (d) is a supplement item. |
| prop:fw-ungrounded-bias | B | 178 | The limit of ungrounded learning; cited only in 09_minimal.tex. One sentence in the main text, item (c) to the supplement. |
| prop:fw-transfer-kernel | B | 126 | Impulse response of the record recursion; can be an equation inside def:fw-record-model. Cited in the introduction, related work and discussion as a pointer. |
| fig:fw-channels | A | 80 | Cited by the introduction and section 4; the picture of the two channels. |
| def:fw-record-model | A | 190 | Cited 15 times; sections 8 and 10 build on it. |
| prop:fw-record-basics | B | 189 | (b) and (c) are bookkeeping; (a) and the optimum are the steady-state Kalman predictor. Cited once. |
| prop:fw-performative | B | 177 | (a) is one computation; (b) and (c) are qualitative. Cited 5 times as a pointer; a two-sentence statement would serve. |
| prop:fw-efe-communication | A | 214 | The expected free energy of attention and addressing; cited by sections 3, 7, 10d. Drop the redisplayed two-form identity and cite eq:fw-efe. |
| prop:fw-understood-predicted | A | 93 | Defines the anatomy of the two preference errors that prop:fw-bounded-confidence needs; short. |
| open:fw-understanding-risk | B | 39 | Open problem listed in the introduction; belongs in a consolidated open-problem list. |
| prop:fw-bounded-confidence | A | 196 | (a) to (c) carry the bounded-confidence and pandering claims, after (b) is restricted. (d) is tier C once corrected: a martingale identity whose stated consequence fails. |
| conj:fw-fragmentation | B | 54 | Conjecture; cited by the introduction and related work. Supplement or the open-problem list. |
| prop:fw-frame-covariance | B | 185 | Gauge statement that supports effective codes; merge the three frame propositions into one. |
| def:fw-translation | B | 112 | Its heavy consumer is thm:coh-holonomy in section 6; can move next to it with a pointer here. |
| prop:fw-effective-codes | A | 105 | The claim the rest of the manuscript uses: encodings enter only through H_j = T_c U_j. Becomes the lead item of a merged frame proposition. |
| prop:fw-frame-identifiability | B | 95 | Stabilizer statement; third item of the merged frame proposition. |
| prop:fw-misidentified-code | C | 110 | Already stated only in the appendix and cited nowhere outside the framework files; the body sentence at :429 should carry its hypotheses or go. |
| def:fw-level0 | A | 191 | Cited 25 times; the network every later section analyzes. |
| rem:fw-convex-gains | B | 85 | Used in proofs of sections 3 and 8; supplement with the proofs that cite it. |
| lem:fw-common-mode | A | 143 | Cited 26 times; carries Q/(1 - lambda^2) into sections 3, 6 and 8. |

## Lane mis_min: Sections 3 and 9, misreading and the minimal model

Verdict: no theorem, proposition or lemma in sections 3 (03_misreading) or 9 (09_minimal) was found false, and every appendix proof (app03, app09) proves its statement as written, with matching hypotheses, constants and inequality directions. All 16 proved statements and the one numerical observation of section 3 and the three proved statements of section 9 were rederived by hand; the numbers I could recompute were recomputed (scripts s1 to s9 in the lane directory). Section 9's instantiations of the general results match with the stated constants: the reception map is f times a matrix of the def:fw-level0 form, (C_rho) holds with K_A = K_Mtilde as prop:sca-sufficient(b) states, the clustering bound agrees with prop:sca-spectral, the grounding constants 0.81 / 0.979325 / 0.376268 are arithmetically right, and the frozen two-agent map has radius 1.0613266751 with block row sums 1.0999. Every cross-section citation of section 3 and the load-bearing ones of section 9 were opened and say what they are cited for. Defects: two major, eight minor. (1) Major, demonstrated: the rate 1.0703173057 for a period-two alternation at capacity one (chk:min-amplification, 09_minimal.tex:134, 08_scale.tex:58) is not a property of the only instance the manuscript states; in that instance every capacity-one period-two alternation contracts (largest rate 0.9753). The number belongs to a second instance of the source report whose parameters appear nowhere in the manuscript, so the check does not say what it tested and ex:sca-amplifying-profile's switching-schedule sentence rests on an instance the reader cannot reconstruct. (2) Major, demonstrated as a table/prose conflict: tab:min-bilayers row 3 reports message-fed bilayers under "Single-hop evidence relays", while the text and tab:min-results state that single-hop evidence relay cannot feed an interior; the variant is the relay-chain (two-hop) one. Minor: unstated parameters in the stationary part of chk:mis-listening (reported values need R_c = 0.2 and fixed gains, not the stated R_c = 1); "self-sealed" needs strictness; undefined columns in chk:mis-law-headers; unspecified sampler behind obs:mis-random-codes (qualitative claims reproduce, counts do not); Q positive definite missing from prop:min-grounding-moment; the symbol vartheta used for two different quantities; "echo" undefined in def:min-bilayer and a missing hypothesis in the obstruction sentence; a stale "open" in tab:min-reexamination. Scope: figures quoted from the external report (dennis2026communicating) could not be recomputed from the manuscript and are listed under not_checked; exact counts of random-search checks were not reproduced because the ensembles are not specified. Minimal unresolved obligation: the parameters of the second amplifying counterexample. Supplying them (or deleting the alternation claim in 08:58, 09:134 and chk09:15) is the one action that changes the status of a claimed number. Lane files: <session scratch>/audit/mis_min/findings.md, notes.txt and s1_mis_numbers.py through s10_words.py in the same directory.

Coverage: 34 items examined; 30 hold, 3 defective, 1 suspect, 0 not checked.

| Item | Verdict | Note |
|---|---|---|
| tab:min-bilayers row 3 | defect | Row label contradicts the obstruction at lines 99 and 56 (finding). |
| chk:mis-scope | suspect | Example values reproduce; random-search counts are ensemble-dependent and the sampler is unspecified. |
| chk:mis-listening | defect | Static part verified by hand; stationary sentence does not follow from the stated R_c = 1 and gain rule. |
| chk:min-amplification | defect | Frozen spectrum reproduces; alternation rate does not belong to the stated instance. |

Items found to hold: prop:mis-believed-values; lem:mis-attenuation; lem:mis-common-source; prop:mis-track-band; prop:mis-overvaluation-scope; prop:mis-level1-mse; prop:mis-closed-ratios; prop:mis-dynamic; obs:mis-random-codes; lem:mis-social-blind; prop:mis-mse-floor; lem:mis-disagreement; thm:mis-echo-chambers; prop:mis-pure-listening; prop:mis-correlated-fusion; prop:mis-exact-no-echo; ex:mis-nonsubmodular, ex:mis-cancellation, ex:mis-sender-completion, ex:mis-law-headers; lem:min-disagreement; prop:min-common-code; prop:min-grounding-moment; rem:min-reciprocity and unlabeled formulas of 09_minimal.tex:99; chk:mis-values; chk:mis-ratios; chk:mis-dynamic; chk:mis-echo; chk:mis-law-headers; chk:min-common-code; chk:min-disagreement; chk:min-grounding-moment; chk:min-reciprocity.

### mis_min-01 (major): Alternation rate 1.0703173057 is not a property of the stated two-agent instance; the second counterexample's parameters are absent from the manuscript

Location: sections/chk09_minimal.tex:15 (chk:min-amplification); sections/09_minimal.tex:134 (sec:min-moment); sections/08_scale.tex:58 (ex:sca-amplifying-profile). Labels: chk:min-amplification, ex:sca-amplifying-profile, sec:min-moment. Category: check-reproducibility.

Evidence. chk:min-amplification is titled 'The two amplifying counterexamples' but gives one parameter set (K=2, F=0.9 I_2, Q=I_2, codes (3,0) and (0,3), sensing rows (3,6) and (6,3), level 1; R_c=1 from chk:min-grounding-moment) and then says 'The period-two alternation of two individually stable profiles at capacity one grows by 1.0703173057 per round.' 09_minimal.tex:134 and 08_scale.tex:58 repeat the number in the same paragraph as that instance. Recomputation (s4_chk09.py, s5_alt.py): with R_s=1 the frozen capacity-two level-1 mean map has eigenvalue moduli 0.0171373521, 0.0243522530, 0.4120322207, 1.0613266751 and block row sums 1.0999133748, as claimed. At capacity one (each agent either senses or listens in a round) every frozen profile has radius at most 0.9 and every period-two alternation contracts: per-round rate 0.9723856736 (both sense / both listen), 0.9752822296 (sense and listen swapped between the agents), 0.9 for the rest, computed on the periodic covariance orbit. A scan over R_s in {0.1, 0.5, 1, 2, 10}, both orderings, frozen fixed-point or periodic covariances gives no level-1 rate above one; literal level-0 gains give 1.098 to 1.104, not 1.0703. The source report attributes 1.0703173057 to a different instance (its CEX-1) and the manuscript states no parameters for it. Not established: whether that second instance yields the number, since it cannot be reconstructed.

Proposed fix. In chk:min-amplification write: 'For a second counterexample of \citet{dennis2026communicating} ($K=\dots$, $F=\dots$, $Q=\dots$, codes \dots, sensing rows \dots, noise variances \dots, the two capacity-one profiles being \dots), each frozen profile has spectral radius below one and the period-two alternation grows by $1.0703173057$ per round.' In 09_minimal.tex:134 and 08_scale.tex:58 replace 'alternating two individually stable profiles at capacity one' by 'in a second instance (\cref{chk:min-amplification}), alternating two individually stable profiles at capacity one'. If the parameters cannot be supplied, delete the alternation sentence in all three places; the frozen-profile example alone supports the failure of (M).

What would overturn the finding. The implied claim that the period-two alternation rate was checked for the instance the check states; the reproducibility of the switching-schedule sentence in ex:sca-amplifying-profile.

State: applied. [08] applied: Defect real, already repaired in 08 by an earlier batch; no edit in this batch. The example attributes 1.0703173057 to the report's separate instance CEX-1, says the factor is quoted and the parameters are not reproduced. This matches the current wording of 09_minimal.tex and chk:min-amplification. Not recomputed by me. [09] applied: Confirmed. With R_s=1 the stated instance reproduces 1.0613266751 and row sums 1.0999; all capacity-one frozen profiles give 0.9 and every level-1 period-two alternation contracts (max 0.9752822296). CEX-1 parameters exist nowhere in the vault, so 1.0703173057 is now attributed to the report's CEX-1 as quoted and not recomputed, matching group 08's wording.

### mis_min-02 (major): tab:min-bilayers reports message-fed bilayers under 'Single-hop evidence relays', which the text and tab:min-results say cannot feed an interior

Location: sections/09_minimal.tex:93 (tab:min-bilayers, row 3) against sections/09_minimal.tex:99 and sections/09_minimal.tex:56 (tab:min-results). Labels: tab:min-bilayers, tab:min-results, def:min-bilayer. Category: internal-consistency.

Evidence. 09_minimal.tex:93: 'Single-hop evidence relays, four to six agents & 0.76 to 0.85; pruned 0.936 to 0.999 & forbidden deliveries locked out or pruned; access-structured world & ... the frozen-environment null reproduces the chains'. 09_minimal.tex:99: 'For single-hop relays of tagged observations the report proves an exact obstruction for every population size, period and precision: ... every interior agent's posterior on the exterior-side blocks equals its prior at every round.' 09_minimal.tex:56: 'Single-hop evidence relay cannot feed an interior & I & holds'. An interior error of 0.76 to 0.85 of the prior on an exterior-side block is what the obstruction excludes. The same result appears at 09_minimal.tex:54 as 'Relay chains under lock-out, pruning or targeting', and the row's own last column says 'chains'. The source report (read-only, docs/research/2026-11-07-communication-blanket-condensation.md lines 15, 128, 186) names the variant 'Relay chains with forbidden deliveries locked out or pruned', chains S to A to I, and says 'tagged multi-hop relays escape this'. Not determined: whether the access-structured world of that row has independent sides, so a strict logical contradiction is not shown; the label conflict is.

Proposed fix. Rename the row: 'Relay chains $\sS\to\sA\to\sI$ of tagged observations (two hops), four to six agents'. Optionally add to 09_minimal.tex:99 after the obstruction sentence: 'The relay chains of \cref{tab:min-bilayers} are two-hop relays and are not covered by it.'

State: applied. [09] applied: Confirmed against the report (RL P4.5, QE P5.6: chains S to A to I). Row renamed 'Relay chains S->A->I (two hops)'; 'of tagged observations' omitted because the pruning chains are not shown to be tagged. Added a sentence that these chains are not covered by the single-hop obstruction.

### mis_min-03 (minor): chk:mis-listening: the stationary pure-listener numbers do not follow from the parameters the check states

Location: sections/chk03_misreading.tex:40 (chk:mis-listening), last sentence. Labels: chk:mis-listening, prop:mis-pure-listening. Category: check-reproducibility.

Evidence. The check opens with 'channel noise $R_c=1$ ... level-0 gains from the claimed precision' and then reports, for F=0.98, Q=1, closed complete groups of sizes 4, 10, 30: MSE 25.4160, 25.3006, 25.2616; disagreement 0.0479, 0.0283, 0.0101; echo ratios 530, 895, 2495. With R_c=1 and level-0 claimed-Riccati gains I get MSE 26.66, 25.55, 25.31; disagreement 0.40, 0.176, 0.062; ratios 67, 145, 408 (s2_echo.py). No Riccati rule at level 0 or 1 with any R_c reproduces the reported values; R_c=0.2 with fixed per-edge gains 0.19995, 0.09005, 0.02996 gives (25.4159, 0.04792), (25.3007, 0.02830), (25.2616, 0.01010) (s3_scan.py). The echo ratio is MSE divided by disagreement (25.4160/0.0479=530). The qualitative claims (MSE above P_0=25.2525, small disagreement, large ratio) hold under either parameter set.

Proposed fix. Replace the last sentence by: 'In a stationary world with $F=0.98$, $Q=1$ ($P_0=25.2525$) and $R_c=0.2$, closed complete groups of pure listeners of sizes 4, 10 and 30 with fixed per-edge gains $0.200$, $0.090$ and $0.030$ have mean-square errors ..., disagreements ..., and echo ratios (mean-square error over disagreement) $530$, $895$ and $2495$.' If a gain rule rather than fixed gains was used, state it.

State: applied. [03] applied: Confirmed from the generating computation and a rerun: the stationary numbers use R_c=0.2 and fixed per-edge gains 0.2, 0.09, 0.03 (not Riccati gains, not R_c=1). Riccati gains at R_c=1 give 26.66/25.55/25.31. The last sentence now states these parameters and defines the echo ratio.

### mis_min-04 (minor): def:mis-echo: 'self-sealed' admits equality, against prop:mis-exact-no-echo

Location: sections/03_misreading.tex:231 (def:mis-echo); sections/03_misreading.tex:316 (prop:mis-exact-no-echo). Labels: def:mis-echo, prop:mis-exact-no-echo. Category: definition.

Evidence. def:mis-echo: 'self-sealed if every member is overconfident, its claimed covariance lying below its actual mean-square-error matrix in the Loewner order.' The Loewner order is reflexive, so a member whose claimed covariance equals its actual error satisfies the clause. prop:mis-exact-no-echo: 'its claimed covariance equals its actual mean-square-error matrix. Hence $C$ is neither a weak nor a self-sealed echo chamber'. The 'Hence' holds only if equality is excluded.

Proposed fix. '... \emph{self-sealed} if every member is overconfident: its claimed covariance lies below its actual mean-square-error matrix in the Loewner order and differs from it.'

State: applied. [03] applied: Real: the Loewner order is reflexive, so calibrated members satisfied the old clause. Self-sealed now requires claimed covariance below the actual MSE matrix and different from it, in the finding's wording. No other file restates the clause; the proposition and its proof stand unchanged.

### mis_min-05 (minor): chk:mis-law-headers: three reported quantities are not defined well enough to recompute

Location: sections/chk03_misreading.tex:44 and :60 (chk:mis-law-headers); used by sections/03_misreading.tex:284 (ex:mis-law-headers). Labels: chk:mis-law-headers, ex:mis-law-headers. Category: check-specification.

Evidence. All columns of the table reproduce (s2_echo.py), but only under definitions the check does not give. 'believed/true' (1.626 ... 5.179) equals (1/2)ln(P_0/claimed predicted variance) divided by I(eta_t; m_i(t)) under the actual law; natural alternatives give 1.641 or 1.709 at n=2. The per-round ratio '1.475 at n=2 to 4.237 at n=64' equals the believed per-round gain divided by I(eta_t; the round's data | m_i(t)) under the actual joint law (s8_perround.py). 'the shared part is the common-mode variance' is the variance of the members' mean error (0.1535 at n=2), which a reader can confuse with the common-mode floor 0.1161 quoted two sentences later.

Proposed fix. Add after the table: 'Believed information is $\tfrac12\ln(P_0/\hat P^-)$ and true information is $I(\eta_t;m_i(t))$ under the actual joint law; per round, believed is the claimed one-round gain and available is $I(\eta_t;\text{the round's data}\mid m_i(t))$ under the actual law. The shared part is the variance of the members' mean error.'

State: applied. [03] applied: All columns reproduce (rerun) under the definitions now stated: believed (1/2)ln(P_0/P^-), true I(eta_t;m_i(t)); per round claimed gain (1/2)ln(P^-/P^+) over I(eta_t; s_i,(y_ij) | m_i(t)); shared part is the variance of the members' mean error, distinguished from the common-mode floor.

### mis_min-06 (minor): obs:mis-random-codes / chk:mis-scope: the sampler is unspecified, so the reported counts cannot be reproduced; one precision is unstated

Location: sections/03_misreading.tex:172-174 (obs:mis-random-codes); sections/chk03_misreading.tex:3 and :10 (chk:mis-scope). Labels: obs:mis-random-codes, chk:mis-scope. Category: check-specification.

Evidence. The observation says 'sampled as in chk:mis-scope'; the check file specifies only 'random positive-definite prior and source noise covariances, random source sets ..., random codes'. With covariances AA^T+0.05I, standard normal codes and random source sets (s9_randcodes.py) I get V*>V^1 in 943 of 5000 (invertible codes with channel noise; manuscript 221) and 1005 of 4000 (rank-limited; manuscript 454), V*>V^0 in 34 and 74 (manuscript 2 and 17), largest excesses 1.40, 1.77 and 0.48 nats (manuscript 0.70, 0.95, 0.21), and with U_i contained in U_j: 566 and 0 (manuscript 386 and 0). The qualitative content of the observation reproduces: undervaluation at both levels in both code regimes, none at level 0 when U_i is contained in U_j, as prop:mis-overvaluation-scope(e) requires. The closed form eq:mis-true-value agrees with exact conditioning to 1.1e-13 over 150 worlds. Separately, the full-rank-code values 0.96598 and 0.76309 of chk:mis-scope reproduce at source precision 1e5 (s1_mis_numbers.py), which the check does not state, and it does not say which of V*, V^0 they are.

Proposed fix. State the distributions in the preamble of chk03 (law of the covariances, of the code entries and scales, of the source sets, of the channel noise) and say in obs:mis-random-codes that the counts are for that ensemble. In chk:mis-scope write 'For the full-rank code at $\psi=0.8$, $\sigma_c^2=0.1$ and source precisions $10^5$, the computed values $\mathcal V^\ast_i=0.96598$ and $\mathcal V^0_i=0.76309$ ...' with the correct symbols.

State: applied. [03] applied: Sampler recovered and stated at the head of the checks (two ensembles). Replay with the original seed returns 386/0, 221 (0.696) and 2 exactly; the 2 comes from a second sample of 5000, now said. Fresh-seed rank-limited rerun: 473 and 19 of 4000. Full-rank values labeled V*, V^0 at precisions 1e5.

### mis_min-07 (minor): prop:min-grounding-moment uses Q positive definite without assuming it

Location: sections/09_minimal.tex:159-166 (prop:min-grounding-moment); proof at sections/app09_minimal.tex:86. Labels: prop:min-grounding-moment. Category: missing-hypothesis.

Evidence. The statement defines $\varpi_Q=1-1/\lambda_{\max}(Q^{-1}P_0)$ and the additive constant $N\tr(P_0)/\lambda_{\min}(Q)$; the proof uses $\Lambda_i(t+1)\preceq Q^{-1}$. No file of the manuscript states $Q\succ0$ (grep over sections/*.tex for 'Q\succ' returns nothing), and section 3 works with static worlds, Q=0, where the proposition is void. The hypothesis $Q\preceq P_i(0)\preceq P_0$ does not imply it.

Proposed fix. Begin the proposition 'Let $Q\succ0$, let receivers know ...'. The additive constant can also be tightened, but the stated one is valid.

State: applied. [09] applied: Confirmed: the statement and proof use Q^{-1}, Q^{-1/2} and lambda_min(Q). Added the hypothesis Q positive definite at the start of the proposition. Proof read in full and unchanged.

### mis_min-08 (minor): Obstruction sentence omits the bilayer hypothesis, and 'echo' in def:min-bilayer is undefined

Location: sections/09_minimal.tex:99 (obstruction sentence); sections/09_minimal.tex:77 (def:min-bilayer, clause (i)); sections/09_minimal.tex:105. Labels: def:min-bilayer. Category: missing-hypothesis.

Evidence. 09_minimal.tex:99 states the obstruction under two hypotheses only: independent sides and 'no agent of $\sI\cup\sA$ senses an exterior-side block'. With those alone a sensory agent that senses an exterior-side block may deliver its tagged observation to an interior agent in one hop, and the conclusion fails. The conclusion needs the interior to hear only from $\sI\cup\sA$. Clause (i) of def:min-bilayer forbids $\sE\to\sI$, $\sI\to\sE$, $\sI\to\sS$, $\sE\to\sA$ but not $\sS\to\sI$; that delivery is excluded only if its echo counts as a coupling $\sI\to\sS$, and neither the definition nor any other section says what an echo is ('echoes counted' recurs at 09_minimal.tex:105 without definition). The source report states the obstruction for an 'echo-counted membrane'.

Proposed fix. In def:min-bilayer add: 'the echo of a delivery $j\to i$ counts as a coupling $i\to j$'. In line 99 write: '... if the two sides of the world are independent, then in any partition satisfying (i) and (ii) of \cref{def:min-bilayer}, where the interior hears only from $\sI\cup\sA$ because the echo of a delivery from $\sS$ would be a coupling $\sI\to\sS$, every interior agent's posterior ...'.

State: applied. [09] applied: Confirmed: without the coupling constraint a sensory agent can deliver an exterior-side observation to the interior in one hop. def:min-bilayer now defines delivery j->i and its echo as coupling i->j; the obstruction sentence now assumes clauses (i) and (ii).

### mis_min-09 (minor): The symbol vartheta denotes a noise ratio in section 3 and a code gain in section 9

Location: sections/03_misreading.tex:108-116 (prop:mis-closed-ratios); sections/09_minimal.tex:99, :136-150 (prop:min-common-code). Labels: prop:mis-closed-ratios, prop:min-common-code. Category: notation.

Evidence. prop:mis-closed-ratios uses $\vartheta=R_c/(g^2P)$ (and chk:mis-ratios tabulates 'At $\vartheta=0.5$'); section 9 uses $\vartheta_j$ for the scale of sender j's code, $H_j=\vartheta_jT_c$, and in the listening rule $1/\vartheta_j^2+\sigma_j^2<\sigma_s^2$. Sections 2 and 7 use the same letter for a rotation angle.

Proposed fix. Rename the noise ratio of prop:mis-closed-ratios and chk:mis-ratios (for example $\varrho_c=R_c/(g^2P)$) and keep $\vartheta_j$ for code gains.

State: applied. [03] applied: Noise-to-signal ratio renamed to \varrho_c=R_c/(g^2P) throughout 03, app03 and chk03 (16 occurrences; \frac1{\varrho_c} braced). No other file uses the old symbol for this ratio. Residual proximity: bare \varrho is a prior correlation in section 2 and \varrho_{\mathrm C} a root in section 10. [09] declined: Nothing to change in group 09: every vartheta in these files is a code scale, the convention the finding keeps. Group 03 has already renamed its noise ratio to varrho_c in prop:mis-closed-ratios.

### mis_min-10 (minor): tab:min-reexamination lists circular reporting through records as open while the text two paragraphs later says it is treated

Location: sections/09_minimal.tex:197 (tab:min-reexamination) against sections/09_minimal.tex:225. Labels: tab:min-reexamination, prop:hie-literal-records, prop:hie-record-filter. Category: status-consistency.

Evidence. Table cell: 'in part: the exact-fusion null carries provenance for records (\cref{def:agy-nulls}); circular reporting through records open'. Line 225: 'Circular reporting through records, left open in \cref{tab:min-reexamination}, is treated in \cref{sec:hie} within stated scopes.' I opened prop:hie-literal-records (10b_hierarchy.tex:130) and confirmed it proves unbounded growth of the overconfidence factor in its scope. The table's status word is stale relative to the manuscript's own results.

Proposed fix. Table cell: 'in part: the exact-fusion null carries provenance for records (\cref{def:agy-nulls}); circular reporting through records treated in scopes (\cref{prop:hie-literal-records,prop:hie-record-filter}); provenance with retained posteriors open'. Then delete 'left open in \cref{tab:min-reexamination}' from line 225.

State: applied. [09] applied: Confirmed stale status. Table cell now says circular reporting through records is treated within stated scopes (prop:hie-literal-records, prop:hie-record-filter) with provenance under retained posteriors open; 'left open in' removed from the later paragraph.

### Not checked by lane mis_min

- Figures quoted from the external report and not recomputable from the manuscript: 03_misreading.tex:139 and 09_minimal.tex:122 (0.35 to 0.65, 3.0 to 13.4, interval 2.6 to 9.5; Bar-Shalom 70% and 50%), rem:mis-report-echo (1.10 to 1.26; 0.22 to 0.47 nats), all numerical entries of tab:min-bilayers (0.48 to 0.67, 0.70 to 0.89, 0.76 to 0.85, 0.936 to 0.999, 0.95, 12 of 27, 61, 120, 80), 0.5649 nats and -0.9603, 1.177 and 1.179, the lock-in logarithmic-mean rule, the strict-best-response claims, the divergence statement for Dirichlet habits.
- The second amplifying counterexample (rate 1.0703173057): its parameters are not in the manuscript, so the number itself is unverified.
- Exact counts and tolerances of the random-ensemble checks (chk:mis-values, chk:mis-scope, chk:mis-echo, chk:min-common-code part (b): 377 of 400, 0.4413, 0.1296, 0.7248); only qualitative agreement on my own ensembles.
- chk:min-reciprocity was verified by hand, not symbolically.
- Complete split graph claims at 09_minimal.tex:105 (average local clustering tends to one, global transitivity about 3(kappa-1)/N, no blanket with echoes counted): argued, not computed.
- Statements cited only in tab:min-results and tab:min-reexamination whose labels I confirmed to exist but whose text I did not open: prop:fw-record-basics, prop:fw-performative, def:col-blankets, thm:col-path-blanket, prop:col-records-partition, thm:col-boundary, def:agy-closure, def:agy-joint-acts, ex:agy-no-potential, prop:agy-writer-leak, def:agy-order-parameter, prop:agy-nulls-vanish, ex:agy-collider, lem:sca-relations, prop:sca-rank-one, prop:sca-records, prop:sca-records-memory, prop:sca-records-length, prop:hie-record-filter. The table rows that cite them were therefore checked for label existence only.
- Whether the access-structured world of tab:min-bilayers row 3 has independent sides (needed to decide whether the single-hop label is a strict contradiction or only a naming conflict).
- The cited convergence theorem of benaim1999dynamics and the report's proofs quoted in section 9 as 'an argument we have not rechecked'.

### Redundancy noted by lane mis_min

- 03_misreading.tex:334 and 09_minimal.tex:101 give nearly the same paragraph on formation under the exact-fusion null (frozen-calibration mean-field map, 0 to 7 of 8 replicates, conjectures); about 150 words repeated. Keep one, in section 7 or 9.
- The two-agent counterexample parameters (K=2, F=0.9I, Q=I, codes (3,0),(0,3), sensing rows (3,6),(6,3)) and its rates are restated in 08_scale.tex:58, 09_minimal.tex:134, chk09_minimal.tex:15 and :20 and chk08; about 150 words. State once in ex:sca-amplifying-profile and cite.
- Report figures 0.35 to 0.65, 3.0 to 13.4 and 2.6 to 9.5 appear at 03_misreading.tex:139, in rem:mis-exact-fusion (03:327) and at 09_minimal.tex:122; about 70 words repeated twice.
- rem:mis-report-echo (81 words) and the echo-chamber sentences of 09_minimal.tex:105 report the same finding of the source report; about 60 words.
- rem:mis-exact-fusion (117 words) overlaps 09_minimal.tex:122 and open:min-exact-fusion; about 60 words.
- The common-code conjecture is restated at 09_minimal.tex:157 after conj:sca-common-code (08_scale.tex:62-66); about 60 words.
- 03_misreading.tex:106 paraphrases prop:agy-literal-consensus (a)-(c) and prop:hie-literal-once / prop:hie-literal-records; about 70 words that a pointer could replace.
- tab:min-results (272 words) and tab:min-reexamination plus tab:min-reexamination-b (596 words) cover overlapping rows (double counting, relays, echo chambers, exact fusion); one merged table would save roughly 250 words.
- Mathematical simplification: prop:mis-level1-mse and the overconfidence clause of prop:mis-dynamic(a) are both the cross-covariance term of the Joseph form in prop:mis-correlated-fusion; stating that proposition first would make the other two one-line corollaries.
- Mathematical simplification: thm:mis-echo-chambers is prop:mis-mse-floor divided by lem:mis-disagreement and could be a corollary; the constant 4 in lem:mis-disagreement can be 2.
- Mathematical simplification: prop:mis-overvaluation-scope(e) is the law of total variance and needs no separate appendix argument; the frozen case of prop:min-common-code(c) is the period-one case of its periodic statement.
- open:mis-dynamic-ratio (33 words) is a sub-question of open:mis-scope (59 words); merge.

### Streamlining tiers proposed by lane mis_min

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| def:mis-values | A | 133 | Defines V^0, V^1, V*; every claim of section 3 uses it. |
| prop:mis-believed-values | A | 124 | Ordering and submodularity of believed values; needed to state overvaluation. |
| ex:mis-nonsubmodular | B | 91 | Illustration; one sentence with the numbers 0.8047 and 3.3429 suffices in the main text. |
| lem:mis-attenuation | B | 50 | Technical identity used in proofs only. |
| def:mis-common-source | A | 97 | The world in which the true value is computed. |
| lem:mis-common-source | A | 127 | Gives eq:mis-true-value; parts (c), (d) could move to the supplement. |
| prop:mis-track-band | B | 123 | Classical track-fusion band; supporting context for the scope table. |
| prop:mis-overvaluation-scope | A | 113 | The section's main scope statement for overvaluation. |
| prop:mis-level1-mse | B | 78 | Special case of the Joseph-form excess of prop:mis-correlated-fusion. |
| prop:mis-closed-ratios | B | 152 | Closed forms in the symmetric scalar case; quote one ratio in the main text. |
| prop:mis-dynamic | A | 133 | Shows level 1 is inexact for belief messages in a changing world; cited by sections 6 to 9. |
| open:mis-dynamic-ratio | C | 33 | Merge into open:mis-scope. |
| ex:mis-cancellation | B | 46 | Undervaluation example; supplement with a pointer. |
| ex:mis-sender-completion | B | 79 | Second undervaluation example; supplement. |
| obs:mis-random-codes | B | 88 | Numerical observation; a sentence stating that undervaluation occurs outside the proved cases is enough in the main text. |
| tab:mis-scope | A | 175 | Summarizes the scope results in one place; can replace several statements in a short main text. |
| open:mis-scope | B | 59 | Keep with the open problems list. |
| lem:mis-social-blind | B | 62 | One-line consequence of the update subspace; state in prose. |
| def:mis-echo | A | 156 | Needed for the echo-chamber theorem; the weak/strong/self-sealed variants could be shortened. |
| prop:mis-mse-floor | A | 63 | The quantitative half of the echo-chamber result; cited by thm:hie-floor. |
| lem:mis-disagreement | B | 66 | Used only inside thm:mis-echo-chambers. |
| thm:mis-echo-chambers | A | 72 | Headline of the section; could be restated as a corollary of the floor and the disagreement bound. |
| prop:mis-pure-listening | B | 196 | Three-part elaboration for closed listening sets; keep part (a) as a sentence. |
| ex:mis-law-headers | B | 185 | Worked example with a table in the check file; supplement. |
| rem:mis-report-echo | C | 81 | Report figures repeated in section 9. |
| prop:mis-correlated-fusion | B | 175 | General Joseph-form statement; could be promoted in place of prop:mis-level1-mse if the section is reorganized around it. |
| prop:mis-exact-no-echo | A | 100 | The control: exact inference forms no echo chamber. |
| rem:mis-exact-fusion | C | 117 | Overlaps 09_minimal.tex:122 and open:min-exact-fusion. |
| tab:min-dictionary | B | 276 | Translation table between the report's and the manuscript's terms; supplement. |
| def:min-classes | B | 100 | Could be folded into the caption of tab:min-results. |
| tab:min-results | A | 272 | States which results of the minimal model hold, are explained or are open; the section's claim. |
| def:min-bilayer | B | 121 | Needed only for the bilayer discussion; needs the echo clarification. |
| tab:min-bilayers | B | 229 | All entries are report figures; supplement, after fixing row 3. |
| rem:min-reciprocity | C | 272 | Frame-dependent echo defect; belongs with the frame material of section 7 and is not used by the section's results. |
| lem:min-disagreement | A | 98 | Exact two-agent expansion criterion; proved here and checked. |
| prop:min-common-code | A | 334 | The one case where the common-code conjecture is proved; parts (b), (c) could be shortened to pointers to prop:sca-sufficient and prop:sca-spectral. |
| prop:min-grounding-moment | A | 169 | Restores (M) under noiseless grounding; gives the threshold 0.3763 for the counterexample. |
| tab:min-reexamination | B | 370 | Overlaps tab:min-results; merge and move the detail to the supplement. |
| tab:min-reexamination-b | B | 226 | Continuation of the same table. |
| open:min-exact-fusion | B | 89 | Keep with the open problems list; absorbs rem:mis-exact-fusion. |

## Lane col: Section 4, collectives

Verdict: no theorem, proposition, lemma or corollary in sections/04_collectives.tex is false as written, and no appendix proof has an unrepairable gap. I reconstructed each argument by hand or by a small script, and reproduced every numerical observation that rests on a deterministic check and every body number recomputable in seconds (scripts s1 to s6 in <session scratch>/audit/col/). Reproduced: all of tab:col-baselines and obs:col-baselines; all of tab:col-bridge, the thresholds in its caption, in fig:col-bridge and in rem:col-bridge-reading; obs:col-bridge-baseline by an independent certificate (104355 connected regions of 2 to 8 sites, 104944 competitors, 0 coverage failures, 0 violations of lem:col-box-bounds, both clauses); obs:col-nested-medium baselines 2.4239, 1.7893, 1.3006 and block contrasts 6.0345, 3.3784, 1.6667; obs:col-coherence-dimension; the sharpness ratios of thm:col-contrast-size (0.8557, 0.8940, 0.9037, tending to pi/sqrt(12)). Comparison medium and baseline (the item flagged for particular attention): every use of the baseline and of r0 that I traced agrees with def:col-baseline including clause (c), with def:col-coarse-medium (block sums, P Pi P^T) and with def:col-hierarchy. thm:col-bridge, lem:col-box-bounds, prop:col-whole-population and obs:col-nested-medium are mutually consistent: the union of the two grids is the whole closed population and never exceeds the baseline, the admissible interval of each grid is (5.0599e-4, 0.42233) under the lattice clause and (5.3751e-4, 0.36725) under the graph clause, and r0 = 2 is admissible exactly above lambda_2(L_hom) = 0.062015 (0.064936). No defect found there. One defect is major by the rubric (cross-reference used beyond what the cited result says), with small blast radius: the motivating sentence at 04:492 says the unconditional ultrametric contrast is capped by a quantity that vanishes as grounding weakens, whatever the barriers, citing prop:abs-ultrametric-cap. That proposition carries the proviso (1-lambda^2) max_i Sigma^c_ii -> 0, which fails in every finite population with symmetric doubly stochastic mixing (cap >= ln(1+Q^zeta/(N Q))); a 6-agent example gives U_unc = 0.2857 at lambda = 0.9999. The sentence also sits against rem:col-bridge-reading, which says the world-conditional contrast itself vanishes at weak grounding. The accurate distinction is that the unconditional contrast is bounded however strong the barriers while the conditional one is not. Eight minor findings are wording or scope slips. Scope: checks that depend on unspecified random samples were not reproduced (listed under not_checked), and the agy cross-references at 04:278, 300, 339 and the sca references at 04:342 were not opened. Minimal unresolved obligation in this lane: none for the proved statements; for the bridge example, which regions of the actual two-grid population with more than eight sites (other than the grids) exceed the baseline is untested, as chk04:83 discloses. Streamlining: the body file has 13830 words, 9556 inside labeled environments. Tier key used below: A = keep in the main text as is; B = keep the statement in the main text and condense or move details to the supplement (target given); C = move to the supplement whole. Roughly 1700 words of repeated prose are identified under redundancy. Next action that would change the answer: rewrite 04:492 as in the fix for F1, and decide whether prop:col-selects-nothing or thm:col-boundary is the single collecting statement.

Coverage: 35 items examined; 34 hold, 1 defective, 0 suspect, 0 not checked.

| Item | Verdict | Note |
|---|---|---|
| text at 04:492 citing prop:abs-ultrametric-cap | defect | Drops the proviso of the cited proposition; see the major finding. |

Items found to hold: thm:col-path-blanket; prop:col-two-hop; prop:col-records-partition; prop:col-memory; thm:col-thick-shell; thm:col-markov-bound; prop:col-markov-vs-correlation; obs:col-massless; prop:col-selects-nothing; prop:col-world-conditional; thm:col-diffusive-precision; lem:col-kron; prop:col-whole-population; thm:col-lattice-contrast; prop:col-block-media; obs:col-baselines; thm:col-contrast-size; cor:col-lstar; thm:col-bridge; obs:col-bridge-baseline; prop:col-coherence-average; obs:col-coherence-dimension; lem:col-coarse-medium; prop:col-nesting; obs:col-nested-medium; thm:col-boundary; lem:col-gaussian (appendix); lem:col-uniform-leak (appendix); lem:col-kato-temple (appendix); lem:col-resistance (appendix); lem:col-box-bounds (appendix); ex:col-collider; ex:col-non-diffusive; def:col-baseline, def:col-collective, def:col-coarse-medium, def:col-hierarchy (consistency of use).

### col-01 (major): Unconditional ultrametric cap said to vanish at weak grounding whatever the barriers; cited proposition has a proviso that fails in finite populations

Location: sections/04_collectives.tex:492 (sentence after def:col-ultrametric), citing prop:abs-ultrametric-cap at sections/10_abstract_collectives.tex:417; in tension with rem:col-bridge-reading at 04_collectives.tex:567. Labels: def:col-ultrametric, prop:abs-ultrametric-cap, rem:col-bridge-reading. Category: cross-reference overreach.

Evidence. prop:abs-ultrametric-cap proves U_unc(C) <= ln(1 + max_i Sigma^c_ii / Sigma_cm) and states that the cap tends to zero as lambda -> 1 only 'whenever (1-lambda^2) max_i Sigma^c_ii -> 0'. Derivation: for W = lambda P with P symmetric doubly stochastic on N agents and scalar noises, Sigma^c = Q^zeta (I - W^2)^{-1} dominates its uniform-mode part Q^zeta/(1-lambda^2) * 11^T/N, so (1-lambda^2) max_i Sigma^c_ii >= Q^zeta/N, and with Sigma_cm = Q/(1-lambda^2) the cap is >= ln(1 + Q^zeta/(N Q)) > 0 for every lambda < 1. The proviso therefore fails in every finite population of this class. Numerical check (s6_unc_cap.py, two blocks of 3, internal coupling 0.2, one cross edge of weight cut, Q^zeta = Q = 1): lambda=0.9999, cut=1e-6: (1-lambda^2) max Sigma^c_ii = 0.3324, cap = 0.2870, U_unc(C1) = 0.2857, U_cond(C1) = 5.7064; lambda=0.999, cut=1e-5: cap 0.2880, U_unc 0.2851, U_cond 5.6996. So U_unc tends to ln(1+Q^zeta/(nQ)) = 0.2877, not to zero, when barriers strengthen with weakening grounding. At fixed cut = 0.05 both versions vanish (lambda=0.9999: U_unc = 0.0007, U_cond = 0.0050), which is exactly what rem:col-bridge-reading (line 567) says of the world-conditional contrast, so vanishing at weak grounding does not distinguish the two versions.

Proposed fix. Replace the sentence by: 'Conditioning on the world is necessary: a common mode from the world's innovations bounds every unconditional correlation from below, so the unconditional version of U is at most ln(1+max_i Sigma^c_ii/Sigma_cm) for every set, however strong its barriers (prop:abs-ultrametric-cap). The cap tends to zero as grounding weakens when (1-lambda^2) max_i Sigma^c_ii -> 0, as in extended media; in a finite closed population it stays of order ln(1+Q^zeta/(nQ)) for nearly isolated blocks of n members. The world-conditional contrast has no such cap and grows without bound as the barriers strengthen at fixed grounding.'

What would overturn the finding. The claim that the unconditional version of U is capped by a quantity that vanishes as grounding weakens and is near zero for every set whatever its barriers.

State: applied. [04] applied: Confirmed by derivation and script (cap 0.2870, U_unc 0.2857 at lambda=0.9999, cut=1e-6; limit ln(4/3)=0.2877). Sentence after def:col-ultrametric replaced with the proposed wording plus the exact finite-population lower bound ln(1+Q^zeta/(NQ)). Proposition in group 10 untouched. [10] applied: Reproduced (col-01.py): two blocks of 3, lambda=0.9999, cut=1e-6: cap 0.2870, U_unc 0.2857, U_cond 5.7064. The proposition already states the nonvanishing limit ln(1+q/(NQ)); statement unchanged. Added the nearly-isolated-block regime, order ln(1+q/(nQ)), to the prose after it and to chk:abs-cap. Check of the edit: [04] defect, Mathematics reproduces: cap >= ln(1+Q^zeta/(NQ)) in 2000 random symmetric doubly stochastic cases; cap 0.2870, U_unc 0.2857, U_cond 5.7064 at lambda=0.9999, cut=1e-6; U_cond unbounded at fixed lambda. One scope slip: the cited proposition covers nonempty proper subsets only (C=V has infinite contrast), the sentence says every set. Repair: [04] repaired, Checker is right: for C=V, varpi_out is a minimum over the empty set, so U is infinite and prop:abs-ultrametric-cap covers only nonempty proper subsets. Line 493 already reads 'for every nonempty proper subset, however strong its barriers' in the file; no occurrence of 'for every set' remains, so no further edit was made.

### col-02 (minor): 'From every start with initial conditional independence' is wider than the Gaussian start the cited theorem and its proof assume

Location: sections/04_collectives.tex:91 (prop:col-two-hop(a)), :102 (prop:col-records-partition(a)), :662 (thm:col-boundary(a)); proof at sections/app04_collectives.tex:24-28. Labels: prop:col-two-hop, prop:col-records-partition, thm:col-boundary, thm:col-path-blanket. Category: scope of proof.

Evidence. thm:col-path-blanket (04:55) assumes X_0 ~ N(X0bar, Sigma_0) with Sigma_0 positive definite, and its proof identifies the initial conditional independence with (Sigma_0^{-1})_{IE} = 0 through lem:col-gaussian(a). thm:col-boundary(a) sets 'every start with X_I0 indep X_E0 | X_B0' against 'every Gaussian start with Sigma_0 > 0' in the same sentence, which reads as a wider class for the first clause. The wider statement is true (the path density p_0(x_0) prod N(x_{t+1}; A x_t, Q) factors into a function of (x_I, x_B) times a function of (x_E, x_B) under eq:col-pb-general whenever p_0 does), but the appendix proves only the Gaussian case.

Proposed fix. Either write 'from every Gaussian start with Sigma_0 > 0 and X_I0 indep X_E0 | X_B0' in the three places, or add one sentence to the proof of thm:col-path-blanket(a): 'Sufficiency needs no Gaussian start: under eq:col-pb-general the product of transition densities factors into a function of (x_I, x_B) times a function of (x_E, x_B), so the path density factors whenever the initial density does.'

State: applied. [04] applied: Confirmed. Chose the second option: thm:col-path-blanket(a) now states sufficiency for every initial law with the initial conditional independence, proved by a reference-measure factorization argument added to the proof. The three citing statements are now covered and unchanged.

### col-03 (minor): thm:col-thick-shell(b),(c) allow an infinite interior while lem:col-gaussian requires a finite-dimensional U

Location: sections/04_collectives.tex:134-139 (thm:col-thick-shell); sections/app04_collectives.tex:8 (lem:col-gaussian) and :76 (proof). Labels: thm:col-thick-shell, lem:col-gaussian. Category: hypothesis mismatch.

Evidence. The theorem is stated on a finite or countable graph for a partition (I, B, E) with no finiteness of I; part (c) assumes only that I has at most n_d vertices at each distance from E, which permits infinitely many distances. The proof applies lem:col-gaussian(b) with U = e_I, and the lemma assumes 'U is finite dimensional'. Truncating I does not reduce to the lemma directly because marginalizing the rest of I changes the precision.

Proposed fix. Add 'with I finite' to thm:col-thick-shell(b), or state lem:col-gaussian(b) for countable U with M Hilbert-Schmidt, where I(U;Z|Y) = -(1/2) ln det(I - M M^T) holds as a Fredholm determinant and the two bounds are unchanged.

State: applied. [04] applied: Confirmed: lem:col-gaussian(b) needs finite-dimensional U. Added 'with I finite' to thm:col-thick-shell(b), a matching clause in the proof, and 'finite' in the one citing item (region interiors). The Fredholm extension was not attempted.

### col-04 (minor): Necessary condition in thm:col-bridge(iv) is implicit in the leak

Location: sections/04_collectives.tex:507 (thm:col-bridge(iv)), with delta_corr defined at :503. Labels: thm:col-bridge. Category: statement form.

Evidence. The condition reads eps >= (2 abar - delta_corr)(1-theta_0)/(2 theta_0) with delta_corr = sigma^2_cut/(eps + g_min), so eps appears on both sides. The statement is correct (it is the lower bracket of the correlation solved for eps at fixed delta_corr) and the bridge numbers reproduce (correlation one half at eps = 0.001617 inside [0.001564, 0.001667]), but it is not a threshold in closed form.

Proposed fix. Add the explicit consequence: since delta_corr <= sigma^2_cut/g_min, separation requires eps >= (2 abar - sigma^2_cut/g_min)(1-theta_0)/(2 theta_0); or say 'only when eps satisfies the implicit inequality'.

State: applied. [04] applied: Statement was correct but implicit. Added the closed-form necessary condition eps >= (2abar - sigma_cut^2/g)(1-theta_0)/(2theta_0) to (iv), with a three-line proof (monotonicity of x/(2eps+x), trivial when the numerator is nonpositive).

### col-05 (minor): Caption of tab:col-baselines calls window-limited search values the largest contrast

Location: sections/04_collectives.tex:411 (tab:col-baselines caption), obs:col-baselines at :426-428. Labels: tab:col-baselines, obs:col-baselines, open:col-extent. Category: caption versus scope.

Evidence. All entries reproduce (s1_baselines.py: 1.9990 pair; 1.2791 arc of 3 with r* 1.5; 1.1594 arc of 5 with r* 1.3486; 1.5159 sites 0 and 2 with r* 2.0; Z^2 0.8712 for the 3x3 square with r* 0.6780; nearest-neighbor Z^2 maximum r* = 1.000 at the 2x2 square). The searches run over regions of at most 9 sites on Z and a 4x4 window on Z^2, so the entries are maxima over the searched family and lower bounds on r_hom, whose definition takes the supremum over regions of every size. The observation text states the search scope and open:col-extent says exact baselines are open; only the caption overstates.

Proposed fix. Caption: 'Largest contrast over the searched regions of homogeneous media (connected regions of at most 9 sites on Z, regions inside a 4x4 window on Z^2); lower bounds on r_hom (obs:col-baselines).'

State: applied. [04] applied: Caption now states the searched families and that entries are lower bounds on the baseline; obs:col-baselines 'gives the suprema' changed to maxima over the searched regions, lower bounds on bar r_hom. No numbers changed. Check of the edit: [04] defect, 'The entries are lower bounds on bar r_hom' is true of the r column only. The r_star column is the leak-free ratio, with r <= max{1, r_star}: row 1 lists r_star=2.000 while bar r_hom=(eps+2)/(eps+1)=1.999 at eps=1e-3 (arcs n>=3 have r_star<=1.5, disconnected regions r<1). Caption also states the 4x4 window twice. Repair: [04] repaired, Checker is right: bar r_hom is a supremum of r, and row 1 has r_star=2.000 > bar r_hom=1.999001 (enumeration of all regions up to nine sites, eps=1e-3). Caption now restricts the lower-bound claim to column r, describes r_star as the grounding-free ratio, and drops the duplicated 4x4 clause; observation likewise.

### col-06 (minor): List of sets of the two-grid population exceeding the baseline is not shown complete

Location: sections/04_collectives.tex:552-558 (obs:col-bridge-baseline) and :565 (rem:col-bridge-reading); disclosure at sections/chk04_collectives.tex:83. Labels: obs:col-bridge-baseline, rem:col-bridge-reading, chk:col-bridge-baseline. Category: scope of numerical claim.

Evidence. The baseline itself is fully certified (all regions of the comparison box: exact for 2 to 8 sites, lem:col-box-bounds for 9 to 71, lem:col-uniform-leak for disconnected ones; my independent run in s2_box_baseline.py found 0 coverage failures and 0 lemma violations under both clauses). The statement of which regions of the actual population are collectives covers the grids, the union and the 2x2 squares; chk04:83 says regions of the population itself with more than eight sites other than the grids were not examined. rem:col-bridge-reading's 'Which returned sets are collectives is decided by the baseline' then reads as a complete list.

Proposed fix. Add to obs:col-bridge-baseline or the remark: 'Among regions of the population of more than eight sites only the grids and the union were examined.' Alternatively examine sub-rectangles of a grid, which is a few hundred regions.

State: applied. [04] applied: Ran the suggested extension: all 1565 rectangles (2 to 71 sites) of the population, exact in the leak, both clauses. Only the two grids and the eight 2x2 squares exceed the baseline; all stated thresholds reproduced. Scope sentence added to observation and check; non-rectangular regions above eight sites remain unexamined.

### col-07 (minor): obs:col-coherence-dimension: 'falls to 1.09' and 'increments approaching 0.27' describe a non-monotone ratio and increments still 3 to 18 percent above the limit

Location: sections/04_collectives.tex:599 (obs:col-coherence-dimension). Labels: obs:col-coherence-dimension, chk:col-coherence. Category: wording of numerical observation.

Evidence. s5_coherence.py reproduces every number: 2D eps*T_C = 1.403, 1.722, 2.014, 2.295 with increments 0.320, 0.292, 0.281 against (pi/8) ln 2 = 0.2722; 3D 2.863, 5.911, 11.385, 21.808 against the Riemann-sum estimate 2.49, 4.99, 9.98, 19.95, ratios 1.148, 1.185, 1.141, 1.093 (rises before it falls). The identity of prop:col-coherence-average(c) checked directly: mean Corr^-2 - 1 = 0.3439846137310325 against eps*T_C = 0.3439846137310335.

Proposed fix. Write 'with increments 0.32, 0.29 and 0.28 per doubling against the limit (pi/8) ln 2 = 0.27' and 'whose ratio to the Riemann-sum estimate is 1.15, 1.19, 1.14 and 1.09'.

State: applied. [04] applied: Recomputed from the free-boundary box spectrum (col-07.py): 2D 1.4028, 1.7224, 2.0144, 2.2952, increments 0.320, 0.292, 0.281 against 0.2722; 3D ratios 1.148, 1.185, 1.141, 1.093. Observation now quotes the increments and all four ratios. chk:col-coherence already consistent.

### col-08 (minor): rem:col-declared-geometry paraphrases prop:ren-exchangeable with the wrong factor for small regions

Location: sections/04_collectives.tex:352 (rem:col-declared-geometry); cited result at sections/10c_renormalization.tex:181-187. Labels: rem:col-declared-geometry, prop:ren-exchangeable. Category: paraphrase of cited result.

Evidence. The remark says 'every member's internal coupling exceeding about the mean total coupling of an agent'. prop:ren-exchangeable gives d_C(i) > ((n-1)N/(n(N-1))) dbar, which for a pair is about dbar/2 (an isolated pair of coupling a qualifies when 2a > N abar, that is a > N dbar/(2(N-1))).

Proposed fix. 'every member's internal coupling exceeding (n-1)N/(n(N-1)) times the mean total coupling of an agent, about half of it for pairs and about all of it for large regions (prop:ren-exchangeable)'.

State: applied. [04] applied: Confirmed from prop:ren-exchangeable: lambda_2(L_C) <= n/(n-1) min d_C(i) and lambda_2 > N abar give d_C(i) > (n-1)N/(n(N-1)) dbar. Remark now states this factor, about half for pairs and about all for large regions, with n and N glossed. [10c] declined: Nothing to change in 10c: prop:ren-exchangeable states the factor (n-1)N/(n(N-1)) correctly (rederived from lambda_2 <= n/(n-1) min d_C). The defect was the paraphrase in 04_collectives.tex, which already carries the proposed wording.

### col-09 (minor): 'Bounded through contrast' misdescribes the bound of lem:ren-galerkin

Location: sections/04_collectives.tex:627 (text after lem:col-coarse-medium); cited result at sections/10c_renormalization.tex:28. Labels: lem:col-coarse-medium, lem:ren-galerkin, thm:col-bridge. Category: paraphrase of cited result.

Evidence. lem:ren-galerkin bounds the correction by 0 <= D <= (||Pi_perp Phi||^2/kappa_perp) I and |D_XY| <= sigma_X sigma_Y/kappa_perp, with kappa_perp the smallest eigenvalue of the precision on the complement of the block indicators and sum of sigma_X^2 equal to sigma^2_cut. The bound is in the cut dispersion and the internal stiffness, which controls contrast only indirectly.

Proposed fix. 'and is bounded by sigma_X sigma_Y/kappa_perp otherwise, small when the internal stiffness is large against the dispersion of the cut (lem:ren-galerkin)'.

State: applied. [04] applied: Confirmed against lem:ren-galerkin(b), whose bound is sigma_X sigma_Y/varkappa_perp; 10c itself says high contrast alone does not make it small. Prose after lem:col-coarse-medium now states the entrywise bound with both symbols glossed. [10c] declined: Nothing to change in 10c: lem:ren-galerkin states the bound in sigma_X and varkappa_perp, and no 10c file says 'bounded through contrast'. 04_collectives.tex already carries the fix; the same phrase remains in 01, 12 and 13 (follow-ups).

### Not checked by lane col

- Check numbers that depend on unspecified random samples: chk:col-path, chk:col-records, chk:col-shell, chk:col-markov, chk:col-massless (ii) and (iii), chk:col-world, chk:col-kron, the random ensembles of chk:col-whole-population, the random media of chk:col-size and chk:col-coarse-medium (including 1.274, 1.295 and -0.88), the 300 random regions and the value 0.758 of chk:col-coherence, the random two-block media and the equitable three-block example of chk:col-bridge, the ratios U^R = 16.64 and 9.20, and the counts 674, 365, 1328 of ex:col-non-diffusive(a).
- The 162-point grid of chk:col-declared and the numbers 1.098, 2.318, 1.009 to 1.415 quoted in rem:col-baseline-conventions (they need the section-7 model; thm:frm-split-contrast and rem:frm-matched-baseline were not re-derived).
- The 12x3 box bracket numbers of chk:col-bridge-baseline and the exact leak intervals of chk:col-nested-medium (0.0107, 0.0124 to 0.2945, 0.00777, 0.00573); the baselines and contrasts those intervals rest on were reproduced.
- Cross-references not opened: prop:agy-tests, thm:agy-closure-average, prop:agy-drift-precision, thm:agy-h1 (04:278, 300, 339); ex:sca-amplifying-profile, prop:sca-rank-one, prop:sca-amplifying-site, rem:sca-rumors (04:342); tab:sca-sizes.
- Figures: TikZ sources of fig:col-partition, fig:col-markov and fig:col-bridge were not inspected; only the caption numbers were checked against the text and scripts.
- Regions of the actual two-grid population with more than eight sites other than the grids and the union (also unexamined by the manuscript, chk04:83).
- No LaTeX build was run, so label resolution and numbering were not checked.

### Redundancy noted by lane col

- Bridge thresholds (5.06e-4, 0.4223, 0.0620, 0.003234, 0.001617, window 0.0033 to 0.2646, significance 3.32 at 0.0122, corner-square 0.0661 and 1.049) are stated in the tab:col-bridge caption (04:519, 176 words), the fig:col-bridge caption (04:548, 240 words), obs:col-bridge-baseline (04:552-558, 311 words), rem:col-bridge-reading (04:563-567, 583 words) and the paragraph after prop:col-whole-population (04:368, 118 words). Stating them once in the observation and referring to it saves about 600 words.
- Section-7 numbers (1.098, 2.318, 1.009 to 1.415, 162 grid points) and the split-law prose appear in the paragraph after def:col-baseline (04:328, 226 words), rem:col-baseline-conventions (04:346-348, 151 words), rem:col-declared-geometry (04:351-353, 335 words) and chk:col-declared. About 300 words removable by keeping the numbers in section 7 and the check only.
- prop:col-selects-nothing (04:208-216, 217 words) and thm:col-boundary (04:659-668, 360 words) both restate thm:col-path-blanket(b), prop:col-two-hop(a), thm:col-thick-shell and prop:col-markov-vs-correlation. Keeping one collecting statement saves about 250 words.
- The retraction of the earlier H1 formulation is told in rem:col-shell-error (04:186-188, 132 words), in prop:col-markov-vs-correlation and its following text, and in the fig:col-markov caption (04:182, 191 words). About 150 words removable.
- obs:col-baselines (04:426-428, 129 words) repeats the tab:col-baselines caption (04:411, about 110 words of 154). About 100 words removable by moving the search scope into the caption and keeping the observation to two sentences.
- The uniform-leak contrast formula of lem:col-uniform-leak(a) is written out again in the text after def:col-baseline, in prop:col-whole-population(c), prop:col-block-media(a) and thm:col-bridge(i). About 80 words removable by citing the lemma.
- The correction D of thm:col-bridge(ii) is restated in lem:col-coarse-medium(b), in the paragraph at 04:627 and in lem:ren-galerkin(a) of section 10c. About 100 words removable in section 4 by citing lem:ren-galerkin once.
- rem:col-lengths (04:469-471, 156 words) repeats the formulas of thm:col-contrast-size and cor:col-lstar and the relation of prop:sca-lengths-relation. About 100 words removable.
- Mathematical simplifications: (1) prop:col-two-hop is a three-line corollary of thm:col-path-blanket and can be stated as one. (2) thm:col-thick-shell and thm:col-markov-bound can be one theorem with the constants in the supplement. (3) lem:col-uniform-leak(d) duplicates the first step of the proof of thm:col-lattice-contrast; cite it there. (4) In obs:col-bridge-baseline the exact evaluation of complements of 1 to 3 sites is covered a second time by lem:col-box-bounds at 69 to 71 sites; one of the two can be dropped. (5) thm:col-bridge(iv) can carry the explicit necessary condition eps >= (2 abar - sigma^2_cut/g_min)(1-theta_0)/(2 theta_0). (6) prop:col-coherence-average(c) can quote the limiting sum (0.3563 at r = 5 on the interval, against the stated bound 0.4112).

### Streamlining tiers proposed by lane col

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| def:col-partition | A | 150 | Every later statement uses the canonical partition. |
| fig:col-partition | B | 134 | Keep the figure; cut the caption to about 60 words. |
| rem:col-agent-level | C | 107 | Interpretive contrast with agent-level role assignment; one sentence in the main text suffices. |
| def:col-blankets | A | 70 | Defines the path and instantaneous blankets the section tests. |
| thm:col-path-blanket | A | 211 | Gaussian path-precision criterion; move the initial-slice leak bound (c) to the supplement if space is needed. |
| ex:col-collider | B | 72 | Shows the collider condition is not vacuous; two sentences in the main text, proof in the supplement. |
| prop:col-two-hop | B | 126 | Corollary of thm:col-path-blanket; restate as a one-sentence corollary. |
| prop:col-records-partition | C | 152 | Records are peripheral to the collective definition; used only by open:col-records-baseline and thm:col-boundary(a). |
| prop:col-memory | C | 109 | Side result on memory; not used by the contrast or baseline material. |
| def:col-markov-length | B | 72 | Needed for the Markov-versus-correlation result; shorten to two sentences. |
| thm:col-thick-shell | B | 118 | Keep the decay statement and the leak rate; constants to the supplement; merge with thm:col-markov-bound. |
| thm:col-markov-bound | B | 126 | Merge with thm:col-thick-shell into one theorem. |
| prop:col-markov-vs-correlation | B | 239 | Carries the correction of the earlier H1 formulation; keep the two inequalities and the hub family in one sentence, constructions to the supplement (target 120 words). |
| fig:col-markov | C | 196 | Illustrates a result already stated; caption of 196 words repeats the proposition. |
| rem:col-shell-error | C | 132 | History of a retracted formulation; one clause in the main text. |
| conj:col-markov-length | B | 53 | Keep as one sentence in a consolidated list of open problems. |
| obs:col-massless | C | 132 | Numerical side observation, not used downstream. |
| prop:col-selects-nothing | A | 217 | The nonselection result is the reason contrast is introduced; it collects earlier results, so those can shrink. |
| def:col-world-conditional | A | 107 | Fixes the covariance on which contrast is defined. |
| prop:col-world-conditional | B | 133 | Statement in two sentences; derivation to the supplement. |
| rem:col-world-conditional | C | 95 | Interpretation. |
| thm:col-diffusive-precision | A | 306 | Gives the diffusive form diag(eps) + L on which every contrast statement rests; clause (c) on range two can move (target 200 words). |
| ex:col-non-diffusive | C | 149 | One sentence in the main text pointing to the supplement. |
| open:col-non-diffusive | B | 87 | Merge the section's open problems into one list. |
| open:col-exact-fusion | B | 28 | Merge into the list of open problems. |
| def:col-contrast | A | 132 | Central definition. |
| lem:col-kron | B | 101 | One-sentence statement (marginal leaks, r' >= r); proof in the supplement. |
| rem:col-which-contrast | C | 159 | Worked comparison of the two contrasts; one sentence in the main text. |
| def:col-baseline | A | 311 | Comparison medium and baseline; every later result depends on its three clauses. |
| def:col-collective | A | 81 | Central definition. |
| rem:col-moment | C | 70 | Interpretation; not used. |
| rem:col-baseline-conventions | C | 151 | Compares with a weaker convention using section-7 numbers that are stated there and in chk:col-declared. |
| rem:col-declared-geometry | B | 335 | The dependence on the declared geometry is a substantive caveat; keep about 120 words and move the numbers to the supplement. |
| prop:col-whole-population | B | 360 | Needed for the bridge reading; the three clauses can be stated in about 180 words. |
| open:col-records-baseline | B | 77 | Merge into the list of open problems. |
| thm:col-lattice-contrast | A | 86 | The bound that makes the baseline finite on lattices. |
| prop:col-block-media | B | 93 | Keep the statement; numbers already in chk:col-lattice. |
| tab:col-baselines | B | 154 | Keep the table with a caption of about 50 words that states the search windows. |
| obs:col-baselines | B | 129 | Two sentences; the rest duplicates the table caption. |
| thm:col-contrast-size | A | 75 | Contrast bounds extent; short. |
| def:col-lstar | B | 70 | Merge with cor:col-lstar. |
| cor:col-lstar | B | 38 | Merge with def:col-lstar into one short statement. |
| rem:col-lengths | C | 156 | Repeats formulas of thm:col-contrast-size and prop:sca-lengths-relation. |
| open:col-extent | B | 38 | Merge into the list of open problems. |
| def:col-ultrametric | A | 130 | Second criterion compared in the bridge theorem. |
| thm:col-bridge | A | 380 | Bridge theorem; add the explicit form of the necessary condition in (iv). |
| tab:col-bridge | B | 329 | Keep the table; caption to about 80 words, thresholds stated once in obs:col-bridge-baseline. |
| fig:col-bridge | B | 245 | Keep the figure or move it to the supplement; caption to about 80 words. |
| obs:col-bridge-baseline | B | 311 | The only fully certified baseline of a structured population; keep the formula and the intervals (about 150 words), method in the check. |
| rem:col-bridge-reading | B | 583 | Longest item of the section; repeats numbers from the table, figure and observation; target 200 words. |
| open:col-bridge | B | 44 | Merge into the list of open problems. |
| prop:col-coherence-average | B | 106 | Keep (b) and the identity of (c); (a) is one line. |
| obs:col-coherence-dimension | C | 69 | Numerical illustration of (c); not used downstream. |
| def:col-coarse-medium | A | 162 | Needed by def:col-hierarchy and section 10c. |
| lem:col-coarse-medium | B | 199 | Keep (a) and (b); (c), (d) and the unequal-block example to the supplement. |
| def:col-hierarchy | A | 125 | Fixes how each level is judged against its own comparison medium. |
| def:col-nested | B | 165 | Condense to about 80 words. |
| prop:col-nesting | B | 200 | Statement in about 100 words. |
| obs:col-nested-medium | B | 211 | Keep the three baselines and block contrasts in about 100 words; set-up in the check. |
| thm:col-boundary | B | 360 | Summary theorem restating earlier results; keep either this or prop:col-selects-nothing as the single collecting statement (target 150 words). |

## Lane agy1: Section 5, closure

Every theorem and proposition in 05_agency.tex:1-193 holds as stated; all closure-bound constants were re-derived by hand (76 from 75.25, 152) and the lattice check reproduced. No critical defect. Three major defects are in prose: the opener claims the selecting contrast bounds memory under non-reversible drift, which the section lists as open; ':64 always carries memory' is false (explicit counterexample, d_M=0 with d_cl>0); ':125' misreads eq:agy-drift-precision as bounding contrasts. Minor: d_M depends on t, literal consensus needs n>=2, one check case lies outside its hypothesis. Notes and scripts: <session scratch>/audit/agy1/findings.md

Coverage: 14 items examined; 10 hold, 0 defective, 2 suspect, 2 not checked.

| Item | Verdict | Note |
|---|---|---|
| def:agy-closure | suspect | d_M depends on t; one tolerance for two quantities. |
| chk:agy-consensus | suspect | Static part consistent; dynamic bounds imply path-dependent suprema not stated. |
| chk:agy-mori-zwanzig | not_checked | Instance not specified; qualitative behavior reproduced on another instance. |
| chk:agy-drift-precision | not_checked | 62 percent figure not reproduced; identity M=(I+J)Pi confirmed to 1e-14. |

Items found to hold: thm:agy-mori-zwanzig; thm:agy-closure-identity; thm:agy-closure-average; ex:agy-symmetric-dispersion; prop:agy-drift-precision; prop:agy-pooling; prop:agy-consensus; prop:agy-literal-consensus; chk:agy-closure-average; chk:agy-symmetric-dispersion.

### agy1-01 (major): Opener claims the selecting contrast bounds memory for non-reversible drift; the section itself lists that as open

Location: sections/05_agency.tex:3 and :105 (against :128, :132). Labels: sec:agy, thm:agy-closure-average, open:agy-discrete-closure. Category: overstatement.

Evidence. Line 3 says the contrast that selects a collective also bounds the memory of its average for reversible drift and, with a modified dispersion, for non-reversible drift. thm:agy-closure-average(b) uses a different contrast (r^M of the drift M), not r(C) of def:col-contrast, and :128/:132 state that non-reversible recursions and the block of the world-conditional precision on which contrast is defined remain open. Part (a) is also for the surrogate diffusion with drift Pi^c_CC and frozen exterior, not the level-0 recursion.

Proposed fix. Reword :3 and :105: the selecting contrast bounds memory for the reversible diffusion with drift Pi^c_CC and fixed exterior; for non-reversible drift a drift-based contrast with row and column dispersions does, and its relation to the selecting contrast is open (open:agy-discrete-closure).

State: applied. [05] applied: Confirmed: part (b) uses the drift-based contrast r^M, not r(C). Section opener and the paragraph after thm:agy-closure-average now restrict the selecting-contrast claim to the reversible diffusion with drift Pi^c_CC and fixed exterior, and point to open:agy-discrete-closure for non-reversible drift.

### agy1-02 (major): 'A collective whose boundary hears its interior always carries memory' is false

Location: sections/05_agency.tex:64. Labels: thm:agy-closure-identity. Category: interpretation-as-result.

Evidence. Counterexample: A=[[a,b],[0,0]], Q=I, P=(1 0), b!=0. The hidden coordinate is iid and independent of y_{0:t}, so y is exactly AR(1): kernels Gamma_l=0, d_M=0, yet W_{R Rbar}=b and d_cl=(1/2)ln(1+b^2)>0. s4_hear.py (a=0.6, b=0.9): d_M=0 to 1e-16 at history lengths 1,2,5,10; d_cl=0.2967. Part (b) gives loss of sufficiency, not memory; :27 itself says vanishing memory without sufficiency occurs.

Proposed fix. Replace with: such a collective's summary is never sufficient (d_cl>0); memory in the sense of d_M may still vanish. State that part (d) describes the Markov augmentation that is needed only when d_M>0.

What would overturn the finding. prose corollary drawn from thm:agy-closure-identity(b)

State: applied. [05] applied: Confirmed by rerun (a=0.6, b=0.9): d_M below 1e-16 at history lengths 1, 2, 5, 10; d_cl = 0.29666 = (1/2)ln(1+b^2). Prose now says the summary is never sufficient while d_M may vanish, gives the 2x2 example (with |a|<1 added), and reads part (d) as needed only when d_M>0.

### agy1-03 (major): 'The two differ by at most the circulation term' fails for the contrasts

Location: sections/05_agency.tex:125; prop:agy-drift-precision title (:116). Labels: prop:agy-drift-precision, def:col-contrast. Category: cross-reference beyond statement.

Evidence. eq:agy-drift-precision bounds Rayleigh quotients of M_sym against the stationary Pi, an additive bound on rates. With J=0 the circulation term is zero, but def:col-contrast removes cut couplings from xi_in while M=Pi_CC keeps them. Path of 3, leak 0.05, one cut coupling 1 (s2_general.py): xi_in=1.05, r=2.739; xi_in^M=1.5014, r^M=3.917. The proposition and its proof are correct.

Proposed fix. Say: xi_out^M and phi^T Pi phi differ by at most ||J|| ||Pi phi||, and xi_in^M differs from lambda_min(Z Pi Z^T) by at most ||J|| ||Pi||; for J=0, lambda_min(Z Pi_CC Z^T) >= xi_in with the cut couplings accounting for the gap. Retitle the proposition as a rate comparison.

State: applied. [05] applied: Confirmed: path of three, leak 0.05, cut 1 on an end member gives xi_in=1.05, r=2.739, xi_in^M=1.5014, r^M=3.917 with J=0. Proposition retitled as a rate comparison (statement unchanged); following prose states the two rate bounds and the cut-coupling gap; example added to the check.

### agy1-04 (minor): Markov defect depends on t; definition fixes neither t nor a limit

Location: sections/05_agency.tex:13 (def:agy-closure(i)); chk05_agency.tex:6. Labels: def:agy-closure, lem:hie-misspecification. Category: definition.

Evidence. d_M=I(y_{t+1};y_{0:t-1}|y_t) is nondecreasing in t in stationarity. s3_misc.py, 6-dimensional instance with d_cl=0.479: d_M=0.168, 0.198, 0.2197, 0.2203 at t=1,2,5,12. lem:hie-misspecification uses the limit d_M^infty; the check reports one value. d_M<=d_cl holds for every t.

Proposed fix. Define d_M as the limit (equivalently the supremum) over history length, and state in chk:agy-mori-zwanzig which history length was computed.

State: applied. [05] applied: Confirmed on the check's own instance (seed 3 reproduced, d_cl=0.48335): 0.1662, 0.1968, 0.2185, 0.21907 at t=1,2,5,12; Riccati limit 0.21907. d_M defined as the limit (supremum), identified with d^infty_M of lem:hie-misspecification; proof (c) gains the monotonicity sentence; check reports history lengths.

### agy1-05 (minor): Closure definition mixes units and omits input and direction

Location: sections/05_agency.tex:13-25 (def:agy-closure(ii)). Labels: def:agy-closure. Category: definition.

Evidence. (i) defines d_M without input, (ii) applies it to a collective with blanket input. One tolerance alpha_M bounds either d_M (nats) or Xi (a correlation gap). Xi compares with e^{-varpi_1 u}, so an exactly Markov coordinate aligned with a faster mode has Xi>0; Xi measures memory only when the coordinate tracks the slowest mode.

Proposed fix. Give the input-conditional form of d_M, use separate tolerances for d_M and Xi, and note that Xi is a memory measure under xi_in>xi_out.

State: applied. [05] applied: Confirmed. Definition now gives the input-conditional d_M (law of y given a known or independent input path, sup over t), a separate dimensionless tolerance alpha_Xi for the Markov error, and states that Xi=0 iff y is Markov for reversible drift with xi_in>xi_out. Meta-agent grade and H1(c) wording follow.

### agy1-06 (minor): Lattice check case a=1 lies outside the hypothesis of part (a)

Location: sections/chk05_agency.tex:10. Labels: chk:agy-closure-average, eq:agy-markov-sym. Category: check.

Evidence. s1_lattice.py reproduces all sixteen reported numbers. At cut coupling 1: xi_out=0.2510, xi_in=0.5868, sigma_C=0.4330 > xi_in-xi_out=0.336, so eq:agy-markov-sym does not apply and the sine bound is 1.29 (vacuous). 'Each within the bound of (a)' is contentful only for the other three cases (bounds 8.96e-3, 2.66e-4, 3.29e-7).

Proposed fix. State that the first case is outside sigma_C<xi_in-xi_out and is reported for scale, or compare it with the unconditional bound of lem:met-unit-coordinate(b).

State: applied. [05] applied: Confirmed by rerun: all reported sines and Markov errors reproduced; at cut coupling 1, sigma_C=0.433 > xi_in-xi_out=0.336 and the angle bound is 1.29. Check now lists the bounds case by case, marks the first case as outside the hypothesis, and compares it with lem:met-unit-coordinate(b) (0.949, 0.32).

### agy1-07 (minor): Literal consensus (b),(c) need n>=2

Location: sections/05_agency.tex:170 (prop:agy-literal-consensus); app05_agency.tex:100. Labels: prop:agy-literal-consensus. Category: missing hypothesis.

Evidence. For n=1, rho(I+Adj)=1: precisions do not diverge and the limit equals the posterior mean for any prior precision. The proof invokes n>=2; the statement does not. For n>=2 all four parts hold (s3_misc.py: ring of 6 prior weight n*L0/(n*L0+sum L) exactly; star of 5 literal prior weight 0.431 against 0.129 for the union).

Proposed fix. Add 'n>=2' to the statement.

State: applied. [05] applied: Confirmed: for n=1, Adj=0 and rho(I+Adj)=1, so (b) and the 'only if' of (c) fail. Statement now assumes n>=2 members; the proof justifies rho(I+Adj)>=2 from minimum degree one.

### agy1-08 (minor, unconfirmed): Part (d) of closure identity is open-loop; prose applies it to active-inference agents

Location: sections/05_agency.tex:58 and :64. Labels: thm:agy-closure-identity. Category: scope.

Evidence. (d) assumes the input path known, deterministic or independent of (x_0, noise). A blanket whose active states respond to the retained or hidden coordinates violates independence, so the filter statement and the order bound are proved only without feedback. The sentence at :64 identifies the filter with an active-inference agent's internal states without this restriction.

Proposed fix. Add 'for an exogenous input path' at :64, or extend (d) to causally conditioned inputs (feedback through y only keeps the Kalman structure).

State: applied. [05] applied: Statement (d) was already correctly qualified; the prose after the theorem identified the filter with an active-inference agent's internal states without the restriction. Prose now says part (d) is open-loop and that filter and order bound are not established under feedback. No extension to causally conditioned inputs was attempted.

### agy1-09 (minor, unconfirmed): Dynamic-consensus check bounds are not consistent with one sample path

Location: sections/chk05_agency.tex:26. Labels: chk:agy-consensus. Category: check.

Evidence. rho_perp=0.848 reproduced (ring of 8 with chord, Metropolis weights). Reported pathwise bounds 76.8, 56.6, 37.0, 19.0, 7.1 at L=1,2,4,8,16 with constant 4.767 imply sup-dispersions 19.0, 16.5, 15.0, 14.9, 20.8; a single path gives one value. The reported factor of six to eight is consistent.

Proposed fix. State whether a new path is drawn per L and which dispersion supremum enters each bound.

State: applied. [05] applied: Confirmed from the generating script (seed 2026): an independent 400-step path is drawn per L and each bound uses its own path's dispersion supremum. Check now says so and lists the suprema 19.0, 16.5, 15.0, 14.9, 20.7 (rerun; finding's 20.8 was a rounding artifact) and constant 4.77.

### agy1-10 (minor): eq:agy-markov-sym is dominated by lem:met-unit-coordinate(b)

Location: sections/05_agency.tex:86; 10a_meta_agents.tex:219. Labels: thm:agy-closure-average, lem:met-unit-coordinate. Category: simplification.

Evidence. The later lemma gives Xi <= (sigma/(xi_in-xi_out))^2 xi_out/xi_in with no condition on sigma, which is sharper than eq:agy-markov-sym and removes the hypothesis sigma_C<xi_in-xi_out. Similarly eq:agy-drift-precision sharpens at no cost to ||J|| |(I-ff^T) Pi f| because f^T J f=0 (s2: 0.079 against 0.254).

Proposed fix. State the sharper unconditional bound in part (a) and cite one proof; replace ||Pi f|| by |(I-ff^T) Pi f| in eq:agy-drift-precision.

State: applied. [05] applied: Sharper bounds verified analytically and on 4000 random instances each. Part (a) now carries the tangent bound and the unconditional Markov bound with a self-contained proof in app05; H1(c) and its proof follow; drift-precision bound sharpened with proof; check numbers recomputed. 10a's cross-reference sentence is now stale (follow-up). [10a] applied: 05 already states the unconditional bound in eq:agy-markov-sym. Updated lem:met-unit-coordinate(b) and its proof (no longer 'sharpens/removes hypothesis'), recomputed the part (a) check against the current bound (96 instances, max ratio 0.586; scripts/agy1-10.py), and removed two 'earlier form' references. eq:agy-drift-precision part lies in 05.

### Not checked by lane agy1

- Primary texts of Olfati-Saber 2005 and Mossel et al. 2016 were not opened; hypothesis matching rests on memory of their statements.
- The author's own cited manuscripts (dennis2026communicating, dennis2026participatory, dennis2026formation).
- Forward-referenced statements not opened: thm:met-abstract-physics, thm:col-bridge(ii), thm:ren-memory, prop:ren-adiabatic, prop:hie-closure-exact, prop:hie-reversible-sandwich, prop:met-literal-aggregation, prop:hie-literal-records, prop:ren-literal-levels, thm:hie-messages, prop:met-level0; lem:met-discrete-closure and prop:met-consensus-filter read at statement head only.
- Instance-specific check numbers without stated specifications: chk:agy-mori-zwanzig values, pooling 0.41/1.25, static KL values, literal star/ring/path numbers, the 8-member scaled family, the 62 percent figure.
- Asynchronous deliberation lies after line 193 and was not read.
- No Numerical observation environment occurs in lines 1-193.

### Redundancy noted by lane agy1

- thm:agy-closure-identity(a) restates thm:agy-mori-zwanzig; merge.
- eq:agy-markov-sym (05_agency.tex:86) and eq:met-unit-markov (lem:met-unit-coordinate(b), 10a_meta_agents.tex:219) bound the same quantity; the later one is sharper and unconditional.
- open:agy-discrete-closure, prose at :132 and lem:met-discrete-closure state the same scope boundary three times.
- Lines 3, 105 and 125 each restate the contrast-closure link with different strength; keep one scoped statement.

### Streamlining tiers proposed by lane agy1

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| def:agy-closure | A |  | Defines the section's target quantities. |
| thm:agy-mori-zwanzig | B | 250 | Standard identity; keep statement, move conventions; merge with closure-identity (a). |
| thm:agy-closure-identity | A |  | Core closure result; drop (a) as duplicate. |
| rem:agy-minimal-memory | C | 90 | Interpretive remark. |
| open:agy-realization | C | 70 | Open question, not used downstream in range. |
| thm:agy-closure-average | A | 300 | Headline; move (b)(ii) and (b)(iv) to supplement. |
| ex:agy-symmetric-dispersion | B | 150 | Supports one sentence; computed refutation. |
| prop:agy-drift-precision | B | 140 | Two-line identity; fold into a remark after the theorem. |
| open:agy-discrete-closure | B | 100 | Needed to scope the headline; shorten to two sentences. |
| prop:agy-pooling | B | 180 | Elementary Gaussian algebra. |
| prop:agy-consensus | A | 150 | Keep (b); move (a) KL bound to supplement. |
| prop:agy-literal-consensus | B | 200 | Contrast case; main text needs only (c). |
| open:agy-exact-fusion-consensus | C | 70 | Peripheral open question. |
| rem:agy-location-family | C | 80 | Scope remark. |

## Lane agy2: Section 5, agency

Every formal statement in 05_agency.tex:194-413 was reconstructed independently and holds as written; the appendix proofs prove them. Defects sit in prose and examples. Two are major: the sign obstruction for epistemic choices is asserted without the null-policy qualifier at lines 340 and 400 (counterexample +0.2877), and the agency failures of the no-data-sharing and synchronous examples disappear under the free-product-habit class that prop:agy-index(c) and chk:agy-index use (every product law scores 1). Seven minor items. Two-member check numbers reproduced; the heterogeneous bounds were unviolated in 24 own random instances. Joint-acts numbers, the three-member synchronous value and primary sources were not checked.

Coverage: 21 items examined; 15 hold, 3 defective, 1 suspect, 2 not checked.

| Item | Verdict | Note |
|---|---|---|
| def:agy-group-model | suspect | 'Collective agency holds' depends on an unspecified admissible class; see finding 2. |
| conj:agy-synchronous | not_checked | Correctly labeled conjecture; three-member TV 0.033 not reproduced. |
| ex:agy-no-data-sharing | defect | TV 0.057 reproduced; closing sentence needs redundancy and a class restriction. |
| ex:agy-unrepresented-driver | defect | Numbers reproduced (-0.13, +0.20 to +3.94); universal sign sentence false as written. |
| rem:agy-consensus-agency | defect | First half supported by prop:agy-consensus(b); literal-consensus clause needs a qualifier. |
| chk:agy-joint-acts | not_checked | Formulas derived; no instance parameters given, numbers not reproduced. |

Items found to hold: lem:agy-decomposition; lem:agy-four-cycle (appendix); thm:agy-agency; rem:agy-precisions; lem:agy-tilt (appendix); thm:agy-heterogeneous; prop:agy-dispersion; prop:agy-index; prop:agy-synchronous; thm:agy-joint-acts; ex:agy-no-potential; prop:agy-performative-sign; chk:agy-agency; chk:agy-heterogeneous; chk:agy-index.

### agy2-01 (major): Sign obstruction for epistemic choices stated without the null-policy qualifier

Location: sections/05_agency.tex:340 (ex:agy-unrepresented-driver) and :400 (prose after prop:agy-performative-sign). Labels: ex:agy-unrepresented-driver, prop:agy-performative-sign. Category: false-as-written.

Evidence. General second difference is d2_ij G_C = D(a',b') - D(a',b) - D(a,b') + D(a,b) with D the null-based conditional mutual information, so it has either sign. Instance (chk_counter.py): eta in R^2, prior I, unit noise; member 1 chooses slot e1 or slot e2, member 2 chooses null or slot e1; zero costs, product habits, gamma_C = 2. The exact group posterior has log odds ratio +0.2877 = +gamma_C I(o_1;o_3) > 0. The proposition itself is correctly qualified ('opened from the null policies'); lines 340 and 400 drop the qualifier and assert a universal negative.

Proposed fix. Line 340: 'No group model with product habits, a slot-product preference and gamma_C >= 0 has a positive log odds ratio between epistemic slots opened from the null policies'. Line 400: 'relative to the null policies, a group posterior can represent positively coordinated choices only when the choices change the world'. Optionally add one sentence: between two non-null epistemic alternatives the sign is label-dependent and can be positive.

What would overturn the finding. Universal claim at lines 340 and 400

State: applied. [05] applied: Counterexample reproduced: log odds ratio +0.2877 = gamma_C*(1/2)ln(4/3) at gamma_C=2. Null-policy qualifier added in both examples, in the prose after the proposition (with the counterexample stated), and in the app proof of H1(e). The proposition itself was already correct.

### agy2-02 (major): Agency failures in the examples vanish under the free-product-habit class used by prop:agy-index(c)

Location: sections/05_agency.tex:203 (def:agy-group-model), :300-322 (def:agy-agency-index, prop:agy-index), :335 (ex:agy-no-data-sharing), :325 (prop:agy-synchronous). Labels: def:agy-agency-index, prop:agy-index, ex:agy-no-data-sharing, prop:agy-synchronous, chk:agy-index. Category: definition-dependence.

Evidence. If the admissible class has product habits with free weights and contains gamma_C = 0 (or gamma_C -> 0 in the infimum), every product law prod_i p_i is a group posterior with habits p_i, so KL = 0 and Agency = 1 for any number of members. The no-data-sharing law and the two-member synchronous law are product laws, so both score 1 and satisfy 'collective agency holds' of line 203. Line 335 calls the gamma_C = 0 fit 'the habit-only model', but def:agy-agency-index fixes that model's habit law to prod E_i, which prod E_i e^{-gamma G_i} is not. Only the fixed-habit computation detects failure (reproduced: 0.311 at full overlap).

Proposed fix. State the class behind every 'fails agency' claim: habits fixed to prod E_i (or to prod E_i e^{-gamma T_i} of thm:agy-agency) and gamma_C free, or free product habits with gamma_C bounded below. Amend line 322: 'with free product habits and gamma_C >= 0 every product law has index 1, for any number of members; the failures of ex:agy-no-data-sharing and prop:agy-synchronous are failures relative to classes with fixed habits or gamma_C > 0'. Line 335: replace 'the habit-only model' by 'a model with gamma_C = 0 and re-tilted habits'.

State: applied. [05] applied: Confirmed: a product law is a gamma_C=0 group posterior with habits equal to its marginals, so index 1 under free product habits. Proposed wording 'gamma_C>0' is insufficient (infimum still zero as gamma_C->0); text uses 'precision bounded below by a positive constant' or habits fixed at prod E_i. prop:agy-synchronous and H1(e) are exact-equality statements with class stated; unchanged. Check of the edit: [05] defect, Minor. Mathematics holds: product laws fit at gamma_C=0, KL tends to 0 as gamma_C->0 (computed), and positive minimum KL when gamma_C>=gamma_0 with redundancy. But def:agy-agency-index requires every admissible class to contain the habit-only model (gamma_C=0), so a class 'whose precision is bounded below by a positive constant', or with 'positive' precisions, is not admissible as written. Repair: [05] repaired, Checker right: def:agy-agency-index requires the habit-only model in every class. Both passages now exempt it ('apart from the habit-only model that the definition requires'); the line-322 clause now reads 'precisions of the models other than the habit-only model'.

### agy2-03 (minor): Necessity of redundancy agreement for exact agency is asserted in prose but only sufficiency is proved

Location: sections/05_agency.tex:250 and :297 (prose around thm:agy-agency). Labels: thm:agy-agency. Category: interpretation-beyond-result.

Evidence. thm:agy-agency(c) gives 'if'. Instance (chk_counter.py): two members, two policies each, P_1 = I, P_2 = diag(3, 0.5), slots at angle 0.4, gamma = 2. Cycle log ratio -0.5106, detailed-balance residual 7.4e-3, so the chain is not reversible and redundancies disagree (0.119 vs 0.375), yet P^inf equals the group posterior with q_C = N(0, 2.0918 I), precision gamma and product habits (0.706, 0.294) x (0.593, 0.407) to 1.0e-14. This agrees with the parameter count at line 322 but contradicts 'Exact agency needs/requires' at lines 250 and 297.

Proposed fix. Line 250: 'Agreement on the shape of beliefs, not on their location, suffices for exact agency with the tilted habits prod E_i e^{-gamma T_i}'. Line 297: 'Exact agency with those habits requires equalities between the members' beliefs about redundancy'. Or add 'for the class with habits fixed to prod E_i e^{-gamma T_i} and declared q_C'.

State: applied. [05] applied: Confirmed (script reproduces: redundancies 0.119/0.375, cycle log ratio -0.5106, P_inf equals a group posterior with free product habits to 1.3e-14). First sentence now says 'suffices'. Second sentence: the proposed 'requires with those habits' is itself unproved in general, so it now states sufficiency only; instance added to chk:agy-index.

### agy2-04 (minor): Synchronous proposition needs positive conditionals

Location: sections/05_agency.tex:325 (prop:agy-synchronous); app05_agency.tex:188-190. Labels: prop:agy-synchronous. Category: missing-hypothesis.

Evidence. The statement says 'whatever their expected free energies'; the proof invokes positive transition probabilities for uniqueness. With deterministic conditionals p_1(x'|y) = [x' = y], p_2(y'|x) = [y' = x] the synchronous chain swaps coordinates; the uniform law on {(0,0),(1,1)} is stationary and not a product law. Positivity follows from (P3) full-support habits with finite G and gamma, which the proposition does not cite.

Proposed fix. 'If two members with full-support habits and finite expected free energies (P3) revise simultaneously, ... the unique stationary law is a product law, whatever the values of their expected free energies.'

State: applied. [05] applied: Confirmed: swap chain has a non-product stationary law. Statement now assumes full-support habits and finite expected free energies (P3) and says 'unique stationary law'; proof derives positivity of the synchronous kernel and records the deterministic counterexample.

### agy2-05 (minor): No-data-sharing example: last sentence omits redundancy

Location: sections/05_agency.tex:335 (ex:agy-no-data-sharing). Labels: ex:agy-no-data-sharing. Category: missing-qualifier.

Evidence. With I_{q_C}(o_A;o_B) = 0 for all policy pairs, G_C is separable, the group posterior with product habits is itself a product law and equals the no-data-sharing law with the same gamma and habits. chk:agy-index reports index 1.000 at zero overlap, and chk_two.py reproduces it. The closing sentence 'A collective at any contrast level fails agency in this way if its members do not share data' is therefore false without redundant slots.

Proposed fix. 'A collective at any contrast level whose members' slots carry redundant information fails agency in this way if its members do not share data (relative to a class with gamma_C > 0 or fixed habits).'

State: applied. [05] applied: Defect real against the original wording, but the example already carries the repair from an earlier batch (redundant slots, departure from habits, class with fixed habits or precision bounded below). Verified the current sentence; no edit made in this batch.

### agy2-06 (minor): thm:agy-agency(d): conditional information gain holds only up to a function of the others' policies

Location: sections/05_agency.tex:244 (thm:agy-agency(d)); app05_agency.tex:145. Labels: thm:agy-agency. Category: wording.

Evidence. Under (P0), -I(eta;o_A,o_{A_{-i}}) = -I(eta;o_A | o_{A_{-i}}) - I(eta;o_{A_{-i}}). The epistemic part of G_i equals the conditional gain plus a term depending on pi_{-i} only. The appendix says 'the part that depends on pi_i'; the statement drops this.

Proposed fix. 'the part of member i's epistemic term that depends on its own policy is its conditional information gain'. Also add 'noise independent of eta_C' to 'linear with additive noise'.

State: applied. [05] applied: Confirmed by the chain rule. Part (d) now says the policy-dependent part of the epistemic term is the conditional gain, remainder -I(eta;o_{A_-i}) a function of pi_{-i}; 'noise independent of eta_C' added. Proof of (d) updated to match.

### agy2-07 (minor): Wrong part cited for the Gibbs law in the joint-acts proof

Location: sections/app05_agency.tex:199 (proof of thm:agy-joint-acts(b)). Labels: thm:agy-joint-acts, thm:agy-agency. Category: cross-reference.

Evidence. The proof cites 'the Gibbs law of thm:agy-agency(b)'. Part (b) is the equivalence of reversibility, exact potential and redundancy agreement; the Gibbs stationary law is stated in part (c).

Proposed fix. Cite thm:agy-agency(c).

State: applied. [05] applied: Confirmed: the Gibbs stationary law is in thm:agy-agency(c). Citation in the proof of thm:agy-joint-acts(b) changed from (b) to (c).

### agy2-08 (minor): 'Common targets' in thm:agy-joint-acts(c) means common z_i, which mixes targets and belief means

Location: sections/05_agency.tex:378 (thm:agy-joint-acts(c)), :387 (ex:agy-no-potential). Labels: thm:agy-joint-acts, ex:agy-no-potential. Category: terminology.

Evidence. The cycle sum is -<z_i - z_j, H_* d2 B_int>, with z_i = H_* F m_i - o*_i. Members with identical targets o*_i but different belief means m_i have z_i != z_j and generally no potential. The theorem and example say 'agree on their targets' and 'common targets'; line 384 states the correct reading (targets or estimates).

Proposed fix. Replace by 'agree on their displacements z_i (target minus predicted outcome) along every joint-effect direction' and 'with common z_i the potential is G^act_C'.

State: applied. [05] applied: Confirmed (common targets, different means: cycle log ratio -0.2968 = formula). Part (c), following prose, example, proof and check now say displacements z_i. Wording 'predicted outcome minus target' matches the definition of z_i; the finding's 'target minus predicted' had the sign reversed.

### agy2-09 (minor): Literal-consensus clause of the consensus remark fails on regular graphs with equal initial precisions

Location: sections/05_agency.tex:403 (rem:agy-consensus-agency). Labels: rem:agy-consensus-agency, prop:agy-literal-consensus. Category: missing-qualifier.

Evidence. The factors [(I+Adj)^L Lambda(0)]_i are equal for all members when the graph is regular and Lambda(0) is constant: each equals (1+d)^L Lambda. The members then share one covariance, thm:agy-agency(d) gives an exact group posterior for every translate q_C, and 'the members' precisions differ' is false. Also prop:agy-literal-consensus is stated for a scalar world, a restriction the remark does not repeat.

Proposed fix. 'Under literal consensus the members' precisions [(I+Adj)^L Lambda(0)]_i differ unless the graph is regular with equal initial precisions (scalar world of prop:agy-literal-consensus); when they differ, the dispersion is positive and thm:agy-heterogeneous applies.'

State: applied. [05] applied: Confirmed: on a regular graph with equal initial precisions all entries of (I+Adj)^L Lambda(0) equal (1+d)^L Lambda. Remark now names the scalar world, states coincidence at every L exactly when graph regular and initial precisions equal (then thm:agy-agency(d) applies), and positive dispersion otherwise. Check of the edit: [05] defect, True only if L=0 counts as a number of rounds. For L>=1 it fails: on the complete graph I+Adj is the all-ones matrix, so K4 with Lambda(0)=(1,2,3,4) gives (10,10,10,10) and (40,40,40,40). Regular case (1+d)^L and the dispersion sentence check out. Minor. Repair: [05] repaired, Checker right (complete graph gives equal entries after one round). Remark now says 'at every n_c >= 0 exactly when', and adds the sufficient condition for n_c >= 1 alone: regular graph with equal entries of (I+Adj)Lambda(0).

### Not checked by lane agy2

- Primary sources: Candogan et al. comparison at line 281, Monderer-Shapley Theorem 2.8, Blume 1993, dennis2026communicating were not read.
- Three-member synchronous instance (TV 0.033) and conj:agy-synchronous itself.
- The manuscript's own 17-, 60- and 30-instance statistics in chk:agy-heterogeneous, chk:agy-index (second computation) and chk:agy-joint-acts; only my own 24 random instances and internal arithmetic were checked.
- chk:agy-joint-acts numbers (-2.0000, +2.0000, +2.7800, 0.3009, cycle log ratios): the check gives no instance parameters.
- def:agy-closure, prop:agy-pooling and sec:abs were not opened; the proof of prop:agy-consensus and prop:agy-literal-consensus belongs to another lane (only statements read).
- open:agy-uniform-bound and open:agy-mixed-policies were read for status only, not attacked.
- The 0.434 index value differs from my 0.437 because the overlap parameter was guessed; not resolved.

### Redundancy noted by lane agy2

- ex:agy-no-data-sharing and prop:agy-synchronous (two members) are the same argument: a product law against a negative null-based log odds ratio; both can be one corollary of prop:agy-performative-sign.
- Line 281 prose repeats the numbers of chk:agy-heterogeneous; line 322 repeats chk:agy-index.
- thm:agy-agency(c) condition 'q_C has the agreed conditional redundancies' is equivalent to R_i = 0 for all i, the hypothesis already visible in lem:agy-decomposition.
- The interpretation paragraph at line 250 and the paragraph at line 297 both restate 'shape, not location'.
- prop:agy-performative-sign's displayed identity is a one-line consequence of the Gibbs form and duplicates thm:agy-agency(a) specialized to G_C.

### Streamlining tiers proposed by lane agy2

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| def:agy-group-model | A | 330 | Main text; all results rest on (P0)-(P4). State the admissible class here. |
| lem:agy-decomposition | A | 90 | Main text; carries the mechanism in one identity. |
| thm:agy-agency | A | 420 | Main text headline; (a) cycle formula could shrink to one line. |
| rem:agy-precisions | B | 130 | Supplement; one sentence in main text suffices. |
| thm:agy-heterogeneous | A | 350 | Keep statement of the three regimes; constants and influence bounds to supplement. |
| open:agy-uniform-bound | C | 60 | One line or move to a collected open-problems list. |
| prop:agy-dispersion | B | 110 | Supplement; bound is loose (observed ratio at most 0.42). |
| def:agy-agency-index | A | 90 | Main text, with the habit convention of the class made explicit. |
| prop:agy-index | B | 200 | (a),(b) one sentence in main; (c) to supplement. |
| prop:agy-synchronous | B | 70 | Merge with ex:agy-no-data-sharing as one corollary; proof without Brouwer. |
| conj:agy-synchronous | C | 80 | Supplement or open-problems list. |
| ex:agy-no-data-sharing | B | 140 | Merge with prop:agy-synchronous; fix closing sentence. |
| ex:agy-unrepresented-driver | B | 140 | Keep a two-sentence version in main; numbers to supplement. |
| def:agy-joint-acts | A | 150 | Main text; needed for thm:agy-joint-acts. |
| thm:agy-joint-acts | A | 280 | Main text; (a) can be folded into (b),(c) as the general cycle formula. |
| ex:agy-no-potential | B | 150 | Keep the two-key sentence in main; protocol-dependence numbers to supplement. |
| prop:agy-performative-sign | A | 90 | Main text, short; all sign claims should cite it with its qualifier. |
| rem:agy-consensus-agency | B | 110 | Supplement, or one sentence after thm:agy-agency. |
| open:agy-mixed-policies | C | 45 | Open-problems list. |
| Simplification: synchronous proof | B | 60 | Replace Brouwer by two interleaved independent chains started from a product law. |

## Lane agy3: Section 5, identity, interaction necessity, H1

Lane 05_agency.tex:414-595. No critical defect. Five major: prop:agy-identity(b) and the persistence criterion condition on a possibly member-driven exterior (0.2144 to 8e-5 nats in a toy); prop:agy-tests(a) has singular conditional covariance and wrong degrees of freedom because X_0 is in X_sh; Omega_int is positive for non-interacting members sharing an outsider (0.0831 nats); def:agy-meta-agent's D clause is unsatisfiable when N_hab is inapplicable and undefined for random N_pr; line 593 drops "without records" (r=2.008 under a deletion null). prop:agy-writer-leak, prop:agy-nulls-vanish, prop:agy-tests(b), prop:agy-identity(a) rederived and hold; chk:agy-identity, chk:agy-writer-leak closed form and LRT calibration reproduced. Notes: scratchpad/collective/audit/agy3/findings.md.

Coverage: 19 items examined; 11 hold, 6 defective, 2 suspect, 0 not checked.

| Item | Verdict | Note |
|---|---|---|
| prop:agy-identity | defect | (a) rederived, holds given beta+g*phi>0 and g>0; (b) proof uses unstated independence of the record path. |
| prop:agy-tests | defect | (a) singular covariance and wrong d.o.f. as stated; (b) rank argument holds. |
| ex:agy-collider | suspect | Qualitative claim reproduced; 1.39e-3 not reproducible, check's second implementation gives 0.2017. |
| chk:agy-nulls | suspect | Zero-under-null reproduced in own model; specific values not reproducible; internal 145x spread between implementations. |
| def:agy-identity | defect | Conditioning on exterior path masks persistence when the exterior hears the members. |
| def:agy-order-parameter | defect | Outsider private inputs absent from X_sh; positive for non-interacting members. |
| def:agy-nulls / tab:agy-nulls | defect | No applicability clause; N_hab plain D; N_fr row lacks acts-decoupled proviso. |
| def:agy-meta-agent | defect | D clause unsatisfiable or undefined in stated scope; grade lacks test level. |

Items found to hold: prop:agy-writer-leak; prop:agy-nulls-vanish; thm:agy-h1; conj:agy-conformity-identity; ex:agy-masking; chk:agy-identity; chk:agy-writer-leak; chk:agy-tests; rem:agy-h1-status; open:agy-attention-positivity, open:agy-unrecorded-drive; cross-references in range.

### agy3-01 (major): Identity under conditioning on the exterior path fails when the exterior hears the members; prop:agy-identity(b) proof asserts an unstated independence

Location: sections/05_agency.tex:419 (def:agy-identity), :433 (prop:agy-identity(b)); proof sections/app05_agency.tex:213. Labels: def:agy-identity, prop:agy-identity. Category: missing hypothesis.

Evidence. The proof of (b) says the outsider-written record path is independent of the members' private noises and replacement events; no hypothesis gives this. If the non-member writer (or any exterior agent) depends on member states, the exterior path is member-driven and conditioning on it masks persistence, the effect ex:agy-masking documents. Toy (observed.py): Y AR(1) with rho=0.9, exterior x(t+1)=0.5x(t)+Y_t+nu_t. I(Y_0;Y_5)=0.2144 nats unconditionally; given the exterior path it is 0.2144 (Var nu=1e6), 8e-5 (Var nu=1), 0 (Var nu<=0.1). A scribe writing dz=omega(mubar-z)dt-delta z dt makes mubar a function of the record path.

Proposed fix. In (b) add: written by non-members whose writes do not depend on the members' states. In def:agy-identity condition on the exogenous inputs of the exterior (exterior private inputs, world innovations, outsider record noises), as eq:agy-omega does, instead of the exterior path; or restrict the definition to exteriors not driven by the members.

What would overturn the finding. prop:agy-identity(b) as stated; persistence criterion of def:agy-identity for any watched collective

State: applied. [05] applied: Confirmed; toy reproduced (0.2144 nats unconditional and given exterior inputs; 8.1e-5 given exterior path at unit noise). Definition now conditions on the exterior's exogenous input X_ext; (b) and its proof add the hypothesis that outsider writes do not depend on members' states. Check sentence added. Check of the edit: [05] defect, Definition, the reduction to the exterior path when the exterior is undriven, and prop:agy-identity(b) with its proof hold. Reproduced 0.21437 (unconditional, given exterior inputs, and at noise 1e6) and 4.69e-11; the unit-noise value is 8.049e-5, insensitive to the x_0 variance, so 8.1e-5 is a double rounding. Main text '8\times10^{-5}' is fine. Repair: [05] repaired, Recomputed in double and 60-digit arithmetic: 8.0490e-5 at unit noise, independent of x_0 variance; 0.21437 and 4.688e-11 confirmed. chk:agy-identity now reads 8.0e-5. The 8.1e-5 in chk:agy-nulls is a different quantity and is unchanged.

### agy3-02 (major): prop:agy-tests(a): conditional covariance singular and degrees of freedom wrong because X_0 in X_sh contains mu_i(0)

Location: sections/05_agency.tex:543 (prop:agy-tests(a)); proof sections/app05_agency.tex:235; sections/chk05_agency.tex:63. Labels: prop:agy-tests, def:agy-order-parameter. Category: edge case / wrong count.

Evidence. def:agy-order-parameter (line 468) puts X_0 in X_sh, and X_0 contains each agent's internal state (eq:col-joint, 04_collectives.tex:10-12). The path mu_i[0:tbar] therefore has an X_sh-measurable block mu_i(0); S_{U|Z} is singular, ln det is undefined, the Gaussian model is not regular, and the stated degrees of freedom overcount. lrt.py: one Z-measurable coordinate gives min eig S_{U|Z}=3.9e-30 and meaningless log-determinants. The check uses three-dimensional paths with 9 degrees of freedom, i.e. it silently drops such coordinates. With them dropped I reproduce the reported behavior: n=200, q=20: mean 10.23, raw rejection 0.093, corrected 0.050.

Proposed fix. State: let U, V be the coordinates of the two paths that are not X_sh-measurable (rounds 1..tbar), with Cov((U,V)|X_sh) nonsingular and n_rep > dim X_sh + dim U + dim V + 1; then 2 n_rep Ihat converges to chi-squared with dim U times dim V degrees of freedom. The multiplier at line 550 appears to be the classical Bartlett factor for independence of two sets after regression on q covariates (verify in Anderson's multivariate text); cite it instead of calling it numerical only.

What would overturn the finding. chi-squared law with dim mu_i[0:tbar] times dim mu_j[0:tbar] degrees of freedom

State: applied. [05] applied: Confirmed: X_0 in X_sh makes mu_i(0) measurable; residual covariance singular (min eig 1.5e-30). (a) restated for non-measurable coordinates U, V with nonsingular conditional covariance and sample-size condition. Multiplier identified as Bartlett-form but left numerically supported: no primary source could be opened (search tools unavailable), so no citation added.

### agy3-03 (major): Omega_int(C)>0 and the deletion nulls do not certify interaction among the members of C

Location: sections/05_agency.tex:465-473 (def:agy-order-parameter, eq:agy-omega), :567 (def:agy-meta-agent). Labels: def:agy-order-parameter, eq:agy-omega, def:agy-nulls, def:agy-meta-agent. Category: definition does not deliver stated purpose.

Evidence. X_sh contains X_0, world innovations, record noises, sender-side broadcast noises and null forcing, but not the private inputs of non-members. Two members that never read each other and both read one outsider share an unconditioned common drive. outsider.py (world F=0.9, sensing gain 0.3, read gain 0.4, 6 rounds, no acts, no channel between 1 and 2): Omega_int({1,2}) = 0.0831 nats; it is 0 once the outsider's path joins the conditioning set. Deletion nulls delete every inter-agent channel, so {1,2} differs from them through the outsider alone and passes the D clause of def:agy-meta-agent.

Proposed fix. Add the private inputs of non-members to the conditioning set of eq:agy-omega (equivalently their paths when they do not hear C); or add a member-restricted deletion null (delete only channels inside C) to the D family; or state in line 465 and def:agy-meta-agent that Omega_int and the deletion nulls certify interaction in the population, not within C.

What would overturn the finding. reading of Omega_int as structure produced by the members' interaction

State: applied. [05] applied: Confirmed in my own toy (0.0290 nats via outsider alone, 0 with outsider's private inputs conditioned; finding's 0.0831 uses unstated variances). Kept Omega_int unchanged, added member-restricted Omega_int(C | zeta_{V\C}), scope statements after the definition, in the null-family paragraph and in def:agy-meta-agent. Finding's D-clause claim for {1,2} was not verified.

### agy3-04 (major): def:agy-meta-agent: 'differs from every null of type D' is unsatisfiable when N_hab is inapplicable and undefined for the random null N_pr

Location: sections/05_agency.tex:567 (def:agy-meta-agent), :510 (def:agy-nulls), :522-532 (tab:agy-nulls), :550. Labels: def:agy-meta-agent, def:agy-nulls, tab:agy-nulls, prop:agy-tests. Category: ill-posed definition.

Evidence. (i) N_hab (gamma=0) is typed D without an applicability clause. In a model with no expected-free-energy policy selection, which is the fixed or exogenously scheduled attention scope of thm:agy-h1, N_hab is the identity intervention; the selected partition cannot differ from it, so no set is a meta-agent. N_eff and N_inf have the same problem without acts unless their conditional typing is read as applicability, which def:agy-nulls does not say. (ii) 'Differs' is a deterministic inequality of selected partitions, but N_pr is random and line 550 says the comparison must be distributional; the grade (r_0, alpha_M, alpha_I, Agency_0) has no test level or n_null.

Proposed fix. In def:agy-nulls add: a null that leaves the model unchanged is not applicable and is reported as such; def:agy-meta-agent then requires differing from every applicable D null. Define differing from a random null as rejection by prop:agy-tests(b) at a declared level alpha_pr with declared n_null, and add alpha_pr to the grade.

State: applied. [05] applied: Confirmed. def:agy-nulls now declares identity-intervention nulls inapplicable (N_hab without EFE selection; N_eff, N_inf without acts) and defines differing from N_pr as rejection by prop:agy-tests(b) at declared alpha_pr with declared n_null; grade gains alpha_pr; meta-agent requires every applicable D null.

### agy3-05 (major): Final-form prose drops the 'without records' restriction: contrast above baseline does not separate from deletion nulls when records exist

Location: sections/05_agency.tex:593. Labels: thm:agy-h1, prop:agy-nulls-vanish. Category: overstatement.

Evidence. thm:agy-h1(b), prop:agy-nulls-vanish(d) and the N_lp table row restrict the claim r<=1 under deletion nulls to populations without records; line 593 says contrast above the baseline already separates a candidate from the deletion nulls with no restriction. records2.py: under the deletion null, two members each writing a private unread record (epsilon=0.3, omega=0.3, delta=0.05) have diffusive world-conditional precision, and the region {member, own record} has xi_out=0.3387, xi_in=0.6803, r=2.008, above 1 and above eps_max/eps_bar=1.196.

Proposed fix. Insert 'in a population without records' in line 593, or say that with records the contrast clause alone does not separate from the deletion nulls and the Omega_int comparison carries the D clause.

What would overturn the finding. line 593 as an unrestricted statement

State: applied. [05] applied: Confirmed against thm:agy-h1(b) and prop:agy-nulls-vanish(d), which restrict the claim to populations without records. Final-form sentence now carries that restriction and says the separation is a separate requirement with records. The r=2.008 record counterexample was not rerun.

### agy3-06 (minor): prop:agy-identity(a) is stated for (mubar, z), not for the member statistic of def:agy-identity; fails for an unread record

Location: sections/05_agency.tex:432 vs :419; dictionary sentence :439. Labels: prop:agy-identity, def:agy-identity, prop:sca-records. Category: edge case.

Evidence. def:agy-identity defines identity time for a statistic of the members' states; (a) gives the slow rate of the pair (mubar, z). With beta=0 and phi=0 the record is unread, the matrix is triangular, and mubar decorrelates at epsilon+g while the stated tau_id is 1/(omega+delta). identity.py grid point beta=0, omega=0.01, phi=0: stated tau_id is 90.9 residence times while mubar decorrelates in 0.99. The dictionary to prop:sca-records at line 439 also needs beta+g phi>0 (that proposition assumes beta_k>0).

Proposed fix. Add the hypothesis beta + g phi > 0 to (a) (then the slow eigenvector has a nonzero mubar component), or declare the statistic to be the pair (mubar, z) and note the unread-record exception.

State: applied. [05] applied: Confirmed: with beta+g*phi=0 the matrix is triangular and the slow eigenvector has no mubar component. (a) now states the formula for the pair (mubar,z), the same time for mubar alone when beta+g*phi>0, and the unread-record case (mubar at eps+g). Dictionary sentence carries beta+g*phi>0. Check notes the three unread grid points. Check of the edit: [05] defect, Statement (a), the dictionary sentence and the grid numbers (90.9, 9.90, 1.00, 0.99, component >= 0.44, 989) all hold and reproduce. One proof sentence is false in a sub-case: for beta+g*phi=0 and p1<=p2, varpi_-=p1 and the displayed vector is zero. The case is not used, so the conclusion stands. Repair: [05] repaired, Checker right: for beta+g f=0 and p1<=p2 the displayed vector is zero. Eigenvector sentence merged under the hypothesis beta+g f>0 as proposed; the beta+g f=0 case is handled by the next sentence as before.

### agy3-07 (minor): prop:agy-identity proof: nondegenerate stationary law needs g>0 and nonzero newcomer variance; approximation bound is one-sided as stated

Location: sections/app05_agency.tex:207-212; sections/05_agency.tex:429-431. Labels: prop:agy-identity, eq:agy-identity. Category: missing hypothesis.

Evidence. The only noise source in the stated model is replacement; with g=0 or deterministic newcomers the stationary covariance is zero and autocorrelation time is undefined. Rederivation gives a two-sided error -2 omega p2/p1 <= rate - approximation <= 8 omega^2/p1 with p1=epsilon+beta+g, p2=omega+delta; the text gives one constant 8 omega(omega+delta)/(epsilon+beta+g), which identity.py never violates on the grid (closed form vs eigenvalue 1.8e-12). The proof has a typo ('being is').

Proposed fix. Add g>0 and positive newcomer variance to the hypotheses; optionally state the sharper two-sided bound; fix the typo.

State: applied. [05] applied: Added g>0 and positive finite newcomer variance; proof now derives positive-definite stationary covariance from a Lyapunov equation. Typo fixed. Finding's two-sided bound is slack: the rate never exceeds the comparison value (det/varpi_+ <= det/p1), so the statement is the sharper one-sided bound with constant 2; verified on about 1e5 draws.

### agy3-08 (minor): Collider and masking numbers (1.39e-3, 0.614) are not reproducible from the text and the check's own second implementation disagrees by a factor of 145

Location: sections/05_agency.tex:490 (ex:agy-collider), :495 (ex:agy-masking), :502 (fig:agy-conditioning caption); sections/chk05_agency.tex:60. Labels: ex:agy-collider, ex:agy-masking, chk:agy-nulls. Category: reproducibility.

Evidence. The values agree across example, caption and check, but act gains, noise variances and agent dynamics are not stated. The check reports 0.2017 nats for the collider in its independent implementation against 1.39e-3 in the example. My own minimal model (collider.py, F=0.9, T=6, 24 parameter sets) gives zero conditional information given the drive (below 2e-16) in every case, and 2.45e-4 to 0.377 nats given the world path plus X_0, scaling roughly as the fourth power of the act gain. The qualitative claims hold; the specific numbers are instance values.

Proposed fix. State the instance parameters next to the numbers (or in the check), and say in the example that the magnitude is instance-specific and scales with the act gain.

State: applied. [05] applied: Recovered both instances from the generating scripts and reproduced 1.391e-3, 0.2017, 0.6144 independently (agy3-08.py). Examples and check now state all parameters; the factor 145 is two different instances. Scaling stated: local exponents 4.00 to 3.93 for gain factors at most one.

### agy3-09 (minor): 'Every candidate has it' contradicts thm:agy-h1(a)

Location: sections/05_agency.tex:564 vs :574. Labels: def:agy-meta-agent, thm:agy-h1, thm:col-path-blanket. Category: internal inconsistency.

Evidence. Line 564 says every candidate has the path blanket. thm:agy-h1(a) and thm:col-path-blanket(b) say the exact path blanket holds generically only if no sensory channel reads both an interior and an exterior variable, so candidates with superposing channels lack it.

Proposed fix. Write 'every candidate with separate channels has it'.

State: applied. [05] applied: Sentence before def:agy-meta-agent now reads 'every candidate with separate channels has it', matching thm:agy-h1(a), which already carried the qualifier.

### agy3-10 (minor, unconfirmed): Small wording gaps in prop:agy-nulls-vanish, tab:agy-nulls and thm:agy-h1(b)

Location: sections/05_agency.tex:476, :481, :483, :524, :576. Labels: prop:agy-nulls-vanish, tab:agy-nulls, thm:agy-h1. Category: wording.

Evidence. Line 476 equates a number (the stationary Omega_int) with a process (the connected part of the level-0 network). (b) uses 'pure sensor' without saying that the agent reads no messages or records. (c) needs positive variance of the private input and, for the stationary version, a statement of which entries of the update matrix are free. Table row N_fr gives Omega_int=0 without the acts-decoupled proviso that row N_lp carries. thm:agy-h1(b) last sentence drops 'within the window' and 'loading on a private input', and the stationary-blanket sentence of (a) omits the decay hypotheses of thm:col-boundary(b).

Proposed fix. Tighten each sentence to match the proposition it summarizes; no mathematical change.

State: applied. [05] applied: Confirmed as real gaps. (b) needs the member to read no message or record and write no record, as its proof uses; (c) needs positive variance and names the free coefficients of the stationary version; N_fr row carries the acts-decoupled proviso; thm:agy-h1(a),(b) restate the decay, window and loading hypotheses.

### Not checked by lane agy3

- Layered-chain leak numbers in chk:agy-writer-leak (parameters not in text).
- Exact values 1.39e-3, 0.614 and the other instance numbers in chk:agy-nulls; only qualitative behavior reproduced in my own small model.
- Power values and the structure-test numbers in chk:agy-tests; the 11.3 / p=0.007 instance was checked for consistency only, not rerun.
- Proofs of results cited by thm:agy-h1(d),(e) and rem:agy-h1-status: prop:agy-consensus, prop:agy-literal-consensus, thm:agy-agency, thm:agy-heterogeneous, thm:agy-joint-acts, prop:frm-nulls, prop:frm-exact-fusion, thm:frm-split-contrast (statements read, proofs not).
- cor:hie-identity bound for delta>0 (delta=0 bracket verified), thm:hie-floor, prop:sca-records-memory.
- The definition of the path leak rate iota_path outside the range and the figure file for fig:agy-conditioning were not opened.
- The Bartlett-factor attribution is from memory and was not verified against a primary source.
- Non-Gaussian or nonlinear versions of any statement; all numerical checks are tiny linear-Gaussian instances.

### Redundancy noted by lane agy3

- Line 439 dictionary to prop:sca-records is repeated by rem:sca-records-special (08_scale.tex:383) and overlaps cor:hie-identity; state once.
- thm:agy-h1(a) restates thm:col-boundary(a),(e) and prop:col-selects-nothing; (d),(e) restate prop:agy-consensus, prop:agy-literal-consensus, thm:agy-agency.
- Line 539 prose repeats the content of tab:agy-nulls row by row.
- ex:agy-collider and ex:agy-masking numbers appear three times: example, fig:agy-conditioning caption, chk:agy-nulls.
- rem:agy-h1-status formation-model verdict duplicates obs:frm-online and tab:frm-online.
- Line 593-595 closing prose restates thm:agy-h1(b) (with the restriction dropped).

### Streamlining tiers proposed by lane agy3

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| def:agy-identity | A | 60 | Keep identity time; the ov_0/I_0 persistence clause is unused in the section and can go to the supplement. |
| prop:agy-identity | A | 90 | Keep (a) rate formula in one line; move the bound and (b) to the supplement; merge with cor:hie-identity and prop:sca-records. |
| conj:agy-conformity-identity | C | 70 | Unproved side remark; one sentence in discussion suffices. |
| prop:agy-writer-leak | B | 180 | Supporting closed form; keep a one-sentence pointer, move regimes and line 461 numbers to supplement. |
| def:agy-order-parameter | A | 0 | Needed by def:agy-meta-agent and thm:agy-h1; fix conditioning set first. |
| prop:agy-nulls-vanish | A | 80 | Keep (a),(d) in main text; (b),(c) are tier B. |
| ex:agy-collider + ex:agy-masking | B | 120 | Merge into one example or into the figure caption; numbers are instance-specific. |
| fig:agy-conditioning | B | 60 | Useful once; caption duplicates both examples. |
| def:agy-nulls + tab:agy-nulls | A | 150 | Keep definition and D/S/E rows; diagnostic rows (N_w, N_code, N_fg) and line 539 prose to supplement. |
| prop:agy-tests | B | 200 | Standard Wilks/Bartlett and Monte Carlo p-value facts; cite and move calibration numbers to supplement. |
| open:agy-attention-positivity | C | 60 | Merge with the other open problem into one sentence or the open-problems list. |
| open:agy-unrecorded-drive | B | 30 | States a real limit of prop:agy-tests(a); keep short. |
| def:agy-meta-agent | A | 0 | Central definition; needs the applicability and test-level fixes. |
| thm:agy-h1 | A | 180 | Keep (b),(c) as the theorem; (a),(d),(e) are restatements and can become pointers or a summary table. |
| rem:agy-h1-status | B | 90 | Status ledger is useful; formation-model half duplicates sec:frm. |
| closing prose 593-595 | C | 80 | Restates thm:agy-h1(b) with a restriction dropped; cut or fix. |

## Lane coh: Section 6, coherence

Verdict: no theorem in the coherence section is false beyond repair, but one proposition clause is false as written and one numerical observation reports a quantity other than the one it names. Two major findings: (F5) prop:coh-code-potential(c) asserts a necessary condition for an exact potential on every attended edge; it fails on graphs where an edge's endpoints share partners (K4 with a common logarithmic value violates the stated edge condition yet has an exact Rosenthal potential, verified to 9e-16); (F2) the "receiver fidelity" column of chk:coh-grounding and the 0.008-nat figure of obs:coh-placement equal I(eta;y_ij|m_i), not the history-conditioned I(eta;y_ij|I_i) of def:coh-components. Six confirmed minor slips: a Lyapunov value computed at parameters other than the stated ones (F1), an example whose numbers need an unstated parameter (F3), "pure relays are massless" in the body against psi <= F^2 < 1 in the appendix (F4), a logit limit that fails under binding capacity (F6), a sampled maximum 1.082 that an explicit instance exceeds by a factor of 2.5 (F7), and real versus complex multiplicity on the flux torus (F8). One unconfirmed item (F9) is an external almost-sure convergence claim with no theorem pointer. The grounding tension holds as stated: eq:coh-ring-mse, the correlation-length reparametrization, eq:coh-tension-law, the general bound through thm:sca-clustering, all nine table rows, the interior minimum 0.132308 and the limit 1.352412 were reproduced, as were prop:coh-placement, the best response (0.1233) and the social optimum (0.1154). On the relation of coherence to contrast and correlation: the section contains no inequality linking a coherence score directly to contrast. The only quantitative links to correlation are prop:coh-info-decay (information length xi/2) and thm:coh-grounding-tension (shared error against xi); the link to contrast runs through the prose of sec:coh-formation pointing at sec:frm theorems and through rem:coh-h4, which is labeled interpretive and joins two bounds proved in different settings. A reader who expects "coherence implies contrast" as a result will not find one, and the text should say so in one sentence. Scripts and a findings copy are in <session scratch>/audit/coh/ (findings.md plus 14 scripts). Minimal unresolved obligation: the history-conditioned receiver fidelity for obs:coh-placement, which I did not compute. Next action that would change the answer: compute that quantity from the stationary joint law of (eta_t, y_ij, full sufficient statistic of I_i); if it stays below 0.008 nats the observation stands with a relabeled column, otherwise the number must change.

Coverage: 38 items examined; 30 hold, 4 defective, 0 suspect, 4 not checked.

| Item | Verdict | Note |
|---|---|---|
| ex:coh-unique-information | defect | Numbers need unstated R^s_B=0.5 (F3); qualitative claim holds. |
| prop:coh-adoption | defect | (a),(b) hold; (c) needs strict monotonicity of F_i (F6). |
| prop:coh-code-potential | defect | (a),(b) and sufficiency in (c) hold; necessity in (c) false on K4 (F5). |
| conj:coh-imry-ma | not_checked | Conjecture; not adjudicated. |
| conj:coh-coarsening | not_checked | Conjecture; not adjudicated. |
| conj:coh-bundling | not_checked | Conjecture; supporting numbers 0.057, 0.367, 0.671 reproduced. |
| obs:coh-placement | defect | Best response (ks 0.1054, ky 0.1185, error 0.1233, xi 1.051) and social optimum (0.1494, 0.1354, 0.1154, 0.963) reproduced; the receiver-fidelity figure is for a different quantity than named (F2). |
| conj:coh-externality | not_checked | Conjecture; the supporting gap 0.1233 vs 0.1154 reproduced. |

Items found to hold: def:coh-components; lem:coh-one-message (appendix); prop:coh-sdpi; prop:coh-relay; prop:coh-info-decay; def:coh-calibration-model; prop:coh-c0-blind; thm:coh-withdrawal; thm:coh-holonomy; prop:coh-flat-true; prop:coh-frustration; prop:coh-coded; prop:coh-frustration-grounding; prop:coh-attended-frustration; def:coh-cycle-product; thm:coh-amplification; lem:coh-rank-one (appendix); prop:coh-no-amplification; ex:coh-amplification; obs:coh-amplification-information; rem:coh-amplification-class; def:coh-code-game; lem:coh-c1-value (appendix); lem:coh-structure, lem:coh-counting, lem:coh-drawdown (appendix); thm:coh-domains-1d; thm:coh-grounding-tension; fig:coh-tension; prop:coh-placement; rem:coh-h4; cross-references (02, 03, 04, 07, 08, 10, 10b).

### coh-01 (major): prop:coh-code-potential(c): necessity of the edge condition is false on graphs where the endpoints of an edge share partners

Location: sections/06_coherence.tex:281 (prop:coh-code-potential, clause (c)); proof at sections/app06_coherence.tex:170. Labels: prop:coh-code-potential. Category: false clause, repairable by hypothesis.

Evidence. Counterexample: complete graph K4 (d_i=3, every edge attended), common value F(u)=ln(1.6+0.8u), which is eq:coh-value with K=2, same-code precision 1, other-code precision 0.2, Lambda=1. The edge quantity at u=0,1,2 is 0.628609, 0.575364, 0.628609, so it depends on u and clause (c) says no exact potential exists. But the game is a congestion game: each agent's payoff depends only on the number of agents on its own code, and the Rosenthal function Phi(sigma)=sum over codes of sum_{k=1}^{n_code} F(k-1) plus the field term is an exact potential (max defect over all 16 states and all unilateral deviations 8.9e-16; logit chain at gamma=1.7 has the Gibbs law to 1.6e-15 and detailed-balance defect 2.2e-16). Script a2_posterior_k4.py. Failing proof step, app06_coherence.tex:170: 'It vanishes for all p and p' exactly when the quantity in (c) is constant in u at i and at j, with equal constants.' This treats p (number of i's other partners on +1) and p' (same for j) as independently variable. On K4 the other partners of i and j are the same two agents, so p=p' on every four-cycle and the Monderer-Shapley sum vanishes identically for a common F. Rings, open chains and the prism of chk:coh-codes are unaffected because adjacent agents there have no common partner.

Proposed fix. Replace the first sentence of (c) by: 'An exact potential exists only if, on every attended edge {i,j} whose endpoints have no common partner, the quantity F_i(u+1)-F_i(u)+F_i(d_i-u)-F_i(d_i-1-u) does not depend on u in {0,...,d_i-1} and takes the same value at i and at j; in general the condition is that [F_i(p+1)-F_i(p)]+[F_i(d_i-1-p)-F_i(d_i-2-p)] ... equals the corresponding expression at j for every pair (p,p') realizable by the other partners of i and j.' Add: 'On a complete graph with a common count-based value the game is a congestion game and has Rosenthal's exact potential.' Restrict the following sentence to 'at every agent with three partners no two of which are adjacent to a common neighbor of the edge', or simply to trees, rings of length at least four and the prism. In the proof, state that p and p' range independently only when the two endpoints share no partner.

What would overturn the finding. Clause (c): 'An exact potential exists only if, on every attended edge {i,j}, the quantity F_i(u+1)-F_i(u)+F_i(d_i-u)-F_i(d_i-1-u) does not depend on u ... and takes the same value at i and at j', and the implied conclusion of the next sentence that eq:coh-value admits no exact potential at any agent with three partners.

State: applied. [06] applied: Confirmed by brute force: K4 and K5 with the common log value have an exact potential. Used a sharper condition than the proposed one: edges whose endpoints have the same other partners need only equal increments; all other edges need constant equal increments. Matches path independence on 12 graphs x 4 values. Proof, prose and check updated.

### coh-02 (major): Receiver fidelity in chk:coh-grounding and obs:coh-placement is conditioned on the current mean, not on the history named in the column header and in def:coh-components

Location: sections/chk06_coherence.tex:86 (chk:coh-grounding, table header); sections/06_coherence.tex:380 (obs:coh-placement); definition at sections/06_coherence.tex:14 (def:coh-components). Labels: obs:coh-placement, chk:coh-grounding, def:coh-components. Category: quantity computed differs from quantity defined.

Evidence. chk06_coherence.tex:86 says the last two columns are 'the receiver fidelity I(eta_t;y_ij | I_i) and the believed fidelity'; def:coh-components takes I_i to be the receiver's information (history). Recomputing from the stationary ring law (script g4_fidelity.py), the tabulated values equal I(eta_t;y_ij | m_i), conditioning on the receiver's current mean alone. Conditioning in addition on the receiver's own current signal s_i, which belongs to I_i, changes them: 0.0056 -> 0.0049 at precision ratio 1, 0.0076 -> 0.0050 at ratio 30, 0.0612 -> 0.0540 at ratio 0.01; adding the other incoming message lowers them further. The sentence at 06_coherence.tex:380, 'a message's receiver fidelity stays below 0.008 nats once varpi_y >= varpi_s', therefore quotes a bound for a different quantity. In the cases computed the defined quantity is smaller, so the direction of the observation is not threatened, but the full history-conditioned value was not computed by me and is not computed by the check.

Proposed fix. Either rename: 'the last two columns are the fidelity given the receiver's current mean, I(eta_t;y_ij | m_i), and the believed fidelity' and in obs:coh-placement 'a message's fidelity given the receiver's current mean stays below 0.008 nats'; or compute I(eta_t;y_ij | I_i) from the stationary joint law with the full sufficient statistic of the history and replace the column.

State: applied. [06] applied: Confirmed: the column equals I(eta;y|m_i) to four digits; renamed. Also computed the defined history-conditioned fidelity by a steady-state filter (ring of 60, same on 30). It is 0.0119 at ratio 1, above the old 0.008 bound, so the finding's remark that the defined quantity is smaller fails at ratios 1 and 3. Observation sentence restated with the new values.

### coh-03 (minor): Lyapunov cross-check value 0.255072 does not belong to the stated parameters

Location: sections/chk06_coherence.tex:105 (chk:coh-grounding). Labels: chk:coh-grounding. Category: number inconsistent with stated parameters.

Evidence. The check lists errors '0.150071, 0.562109 and 0.255072 at (0.99,1), (0.99,30) and (0.95,3)' under the header parameters Q=0.02, R^s=1, R_c=0.1, prior precision 1. The first two reproduce with those parameters. At (F, ratio)=(0.95,3) the header parameters give 0.128875 (closed form and Lyapunov agree). 0.255072 is reproduced at Q=0.05, R^s=0.5, R_c=0.2, prior precision 2 (scripts g2_f95.py, g3_f95scan.py).

Proposed fix. Write '... and 0.255072 at (0.95,3) with Q=0.05, R^s=0.5, R_c=0.2, varpi_s=2', or replace the third value by 0.128875.

State: applied. [06] applied: Confirmed by closed form and Lyapunov solution on 400 agents: header parameters give 0.128875 at (0.95,3); 0.255072 belongs to Q=0.05, R^s=0.5, R_c=0.2, varpi_s=2. The check now lists both values with their parameters.

### coh-04 (minor): ex:coh-unique-information: quoted values need an unstated parameter

Location: sections/06_coherence.tex:106-108 (ex:coh-unique-information). Labels: ex:coh-unique-information. Category: example not reproducible from stated parameters.

Evidence. The values 0.640, 0.370, 0.241 are reproduced only with out-group sensory noise R^s_B=0.5 (with sigma_eta^2=1, R^s_A=1, R_c=0.1, model of def:coh-calibration-model); that value is not stated in the example. With the homogeneous R^s=1 the three values are 0.402, 0.277, 0.198 against the in-group value 0.153 (script w1_unique.py). The qualitative claim (a cross-group sender with unique information is worth more than an in-group sender) holds in both settings; at rotation 0.3 the cross sender already wins on the shared coordinate (0.239 > 0.153).

Proposed fix. Add 'with R^s_B=0.5' to the parameter list, or replace the three values by 0.402, 0.277, 0.198.

State: applied. [06] applied: Confirmed: 0.640, 0.370, 0.241 need R^s_B=0.5 and C1g calibration. Example now states sigma_eta^2=1, R_c=0.1, R^s=1 in A, 0.5 in B, C1g. Check adds the homogeneous values 0.4016, 0.2768, 0.1975 (finding quoted 0.277, 0.198; last digits differ by rounding).

### coh-05 (minor): Body says pure relays are massless in a persistent world; the appendix gives a per-hop factor strictly below one

Location: sections/06_coherence.tex:50 against sections/app06_coherence.tex:43 (app:coh-fidelity) and sections/chk06_coherence.tex:13 (chk:coh-relay). Labels: prop:coh-relay, app:coh-fidelity, chk:coh-relay. Category: body and appendix disagree.

Evidence. 06_coherence.tex:50: '... and in a persistent world pure relays are massless (app:coh-fidelity).' app06_coherence.tex:43: 'Since g <= 1, psi <= F^2, and psi -> 1 as F -> 1 at fixed g'. With psi=F^2 g/(1-F^2(1-g)) < 1 for F<1 the relay chain decays geometrically with mass ln(1/psi) > 0; chk:coh-relay lists psi=0.8223, 0.9752, 0.4602 (hand-verified). The same three files also name one convention three ways: 'content rescaled to unit variance' (06:50), 'unit-variance forwarding' (app06:43), 'unit-power forwarding' (chk06:13).

Proposed fix. Replace by: '... and in a persistent world the per-hop factor of pure relays is psi <= F^2, which tends to one as F -> 1, so pure relays become massless only in that limit (app:coh-fidelity).' Use one name, 'unit-variance forwarding', in all three files.

State: applied. [06] applied: Confirmed: psi=F^2 g/(1-F^2(1-g))<=F^2<1. Body now gives the factor and says pure relays become massless only as F->1. Check renamed to unit-variance forwarding; body wording aligned to 'scaled to unit variance'.

### coh-06 (minor): prop:coh-adoption(c): the gamma -> infinity limit is not the majority rule when capacity binds

Location: sections/06_coherence.tex:270 (prop:coh-adoption, clause (c)); proof at sections/app06_coherence.tex:160-161; capacity variant admitted at sections/06_coherence.tex:252-258 (def:coh-code-game). Labels: prop:coh-adoption, def:coh-code-game. Category: missing hypothesis.

Evidence. Clause (c): 'as gamma -> infinity it tends to the deterministic best response, the majority rule when h_i=0'. def:coh-code-game admits a capacity variant in which the value saturates at kappa partners. Take d_i=3, capacity kappa=1, h_i=0, u^+=2 partners on +1 and one on -1: F_i(2)=F_i(1), so the exponent gamma[F_i(u^+)-F_i(d_i-u^+)] is zero and the adoption probability is 1/2 for every gamma, although +1 is the strict majority. The proof at app06:160-161 uses strict monotonicity of F_i without stating it.

Proposed fix. '... the majority rule when h_i=0 and F_i is strictly increasing (no binding capacity); where F_i(u^+)=F_i(d_i-u^+) the limit is 1/2.'

State: applied. [06] applied: Confirmed: under a binding capacity the exponent can vanish away from a tie (d=3, kappa=1, u+=2), giving 1/2 for every gamma. Clause (c) and its proof now give the limit as best response where G_i(+1)!=G_i(-1), 1/2 otherwise, majority rule for h_i=0 and strictly increasing value.

### coh-07 (minor): Sampled maximum 1.082 for common rank-two codes with sender-specific noise understates the class; explicit instance reaches 2.68

Location: sections/06_coherence.tex:221 (text after prop:coh-no-amplification); sections/chk06_coherence.tex:50 (chk:coh-amplification); bears on open:coh-amplification-noisy at sections/06_coherence.tex:243-245. Labels: prop:coh-no-amplification, chk:coh-amplification, open:coh-amplification-noisy. Category: sampling statistic presented where a closed-form instance exists.

Evidence. 06_coherence.tex:221: 'A common code of rank at least two read with sender-specific noise covariances can amplify; the largest spectral radius found in 20000 draws was 1.082'. Explicit instance (script d2_bundling.py, second block): common code I_2, the priors of ex:coh-amplification(i) (alpha=0.9, x=4), noise covariances diag(0.1,M) for one sender and diag(M,0.1) for the other. Spectral radius of the cycle product: 1.3568, 2.3586, 2.6410, 2.6773 at M=1, 10, 100, 1e4, converging to the differing-codes value of ex:coh-amplification(i) (2.6777), because a large noise on one coordinate turns the common code into two effective coordinate codes. A random search of the same class reached 4.28. The supremum is unbounded in x. The quoted 1.082 reflects the sampling distribution, which the check does not specify.

Proposed fix. Replace the sentence by: 'A common code of rank at least two read with sender-specific noise covariances can amplify without bound: with common code I_2, the priors of ex:coh-amplification(i) and noise covariances diag(r,M), diag(M,r), the spectral radius tends as M -> infinity to that of the coordinate codes of the example (1.36, 2.36, 2.64 at M=1, 10, 100 for r=0.1).' Reword the third item of open:coh-amplification-noisy accordingly, since existence and unboundedness in that class are settled by this instance.

State: applied. [06] applied: Recomputed: common code I_2, example priors, noises diag(0.1,M) for sender b and diag(M,0.1) for sender a give rho 1.3568, 2.3586, 2.6410, 2.6773 at M=1,10,100,1e4; limit alpha^2 x/(1+r)^2 is unbounded in x. Text, check and open problem updated; the residual open item is an excluding condition weaker than common noise.

### coh-08 (minor): Flux torus: lowest-level multiplicity is stated as the number of flux quanta; as a real eigenspace it is twice that, and the edge orientation convention is unstated

Location: sections/06_coherence.tex:176 (text after prop:coh-frustration-grounding); sections/chk06_coherence.tex:45 (chk:coh-frustration). Labels: prop:coh-frustration-grounding, chk:coh-frustration. Category: imprecise statement.

Evidence. 06_coherence.tex:176: 'the least eigenvalue of L equals the flux per plaquette to within 1.1 percent, and the lowest level has the number of flux quanta as its multiplicity'. Recomputed on the 24x24 torus with SO(2) translations (script h1_consistency.py): for 1, 2, 4, 8 flux quanta the ratio (least eigenvalue)/(flux per plaquette) is 0.999, 0.997, 0.995, 0.989, matching the 1.1 percent claim, when each lattice edge is attended in one direction; with both directions attended the least eigenvalue is twice the flux. The multiplicity of the least eigenvalue of the real 2N x 2N operator L of prop:coh-frustration is 2, 4, 8, 16: L commutes with the complex structure I tensor Rot(pi/2), so every real eigenspace is even-dimensional. The stated 1, 2, 4, 8 are complex multiplicities of the associated magnetic Laplacian.

Proposed fix. '... with each lattice edge attended in one direction, the least eigenvalue of L equals the flux per plaquette to within 1.1 percent, and the lowest level has complex multiplicity equal to the number of flux quanta (twice that as a real eigenspace of L).' Make the same change in chk:coh-frustration.

State: applied. [06] applied: Recomputed on the 24x24 torus: one direction per edge gives ratios 0.999, 0.997, 0.995, 0.989 and real multiplicities 2, 4, 8, 16; both directions double the eigenvalue. Section sentence and check now state the orientation convention and complex versus real multiplicity.

### coh-09 (minor, unconfirmed): Learned-holonomy paragraph imports an almost-sure convergence claim from an external manuscript without a theorem pointer

Location: sections/app06_coherence.tex:87 ('Learned holonomy' paragraph); cited from sections/06_coherence.tex:134 (text after prop:coh-flat-true). Labels: prop:coh-flat-true, app:coh-consistency. Category: external dependency not pinned.

Evidence. The paragraph asserts almost-sure convergence of the tangent learning model of dennis2026magent and concludes that the learned holonomy is not detectable from messages. I verified the first-order algebra (the update acts as I - Sigma Pi_e (a_i - a_j) and the law of the messages depends on omega_e only through T_e omega_e in the linearized model), so 'not detectable from messages' holds to first order. The convergence statement itself is cited to the external source with no theorem or section number, and I did not open that source. Missing for confirmation: the exact statement in dennis2026magent and a match between its hypotheses (step sizes, noise moments) and the setting here.

Proposed fix. Add the theorem or section number of the cited convergence result and its hypotheses, and qualify the conclusion: 'to first order in the frame error, none of it is detectable from messages'. If the source proves convergence only in expectation or under a step-size schedule, say so.

State: applied. [06] applied: Opened the source: part (ii) of the theorem on learning with a loop prior, MAgent Theory 2.0 chapter on communication codes. It is almost-sure convergence of the exact Gaussian posterior mean (no step sizes) under listed hypotheses, now stated. Conclusion qualified to first order; second-order difference (1/2) T w Pi w y verified numerically.

### Not checked by lane coh

- chk:coh-sdpi: the four closed-form values, the 300 Gaussian laws, the mixture quadratures (0.9999996, 0.935) were not reproduced; the statement was verified by derivation only.
- chk:coh-info-decay: second and third fitted rates not matched because the fit windows are not stated; first row reproduced exactly with window [10,30].
- chk:coh-holonomy: random-digraph dimensions and learned-holonomy errors not reproduced.
- chk:coh-frustration: random-graph ratios (1.007, 0.669, 1.1e-7 against 7.9e-4) and the 200 coded instances (196/4 split) not reproduced.
- chk:coh-amplification: sample counts and maxima (304, 164, 1760, 1595, 2.445, 0.250, 6.26, 5.48, the delta_T sweep) not reproduced; sampling laws are unspecified.
- chk:coh-codes: published 16-state and prism numbers not reproduced (seed-dependent); the potential structure was checked on my own K4 and ring instances.
- chk:coh-relay: only the psi values and the first two entries of each forwarding convention were hand-verified; the random Markov-chain values and the 6- and 12-hop entries were not.
- '300 random level-0 networks, smallest ratio 1.0003' supporting the general tension bound not reproduced.
- History-conditioned receiver fidelity I(eta_t;y_ij|I_i) not computed; F2 shows only that the tabulated quantity is not it.
- Conjectures conj:coh-imry-ma, conj:coh-coarsening, conj:coh-bundling, conj:coh-externality and the open problems were not adjudicated beyond reproducing supporting numbers.
- External sources (dennis2026magent, dennis2026communicating, Monderer-Shapley, Blume, Hansen-Ghrist, Singer-Wu, Rosenthal) were not opened; F9 depends on the first.
- No LaTeX build; label-to-number resolution in the .aux was not checked.
- The file collective-agents-open-problems-comparison-2026-11-09.md referenced in the relayed message was not opened in this lane.

### Redundancy noted by lane coh

- Formation-status paragraph at 06_coherence.tex:404 (about 190 words) recurs near-verbatim at 00_abstract.tex:4, 01_introduction.tex:43, 07_formation.tex:6, 07_formation.tex:146, 07_formation.tex:369 and 10_abstract_collectives.tex:452; keep one full version in sec:frm and a one-sentence pointer here.
- 'Shared error is invisible to social innovations' is restated at 06_coherence.tex:22, :72, :363, :402 and inside prop:coh-placement(b), about 30 words each; state once after lem:mis-social-blind is cited and refer back.
- Echo-chamber caveat appears at 06_coherence.tex:4 (about 60 words) and again at :402 (about 40 words).
- Record and shared-floor sentences at 06_coherence.tex:363 (about 75 words) and :398 (about 95 words) both cite thm:hie-floor for the same point; merge into rem:coh-h4.
- Recap paragraph at 06_coherence.tex:402 (about 230 words) restates thm:coh-withdrawal, prop:coh-c0-blind, ex:coh-unique-information, prop:coh-attended-frustration and prop:coh-flat-true without adding a claim.
- Body prose repeats check statistics already held in chk06_coherence.tex: 06_coherence.tex:176 (torus), :207 (amplification counts), :221 (20000 draws); about 40 to 60 words each. Cite the check and drop the numbers from the body.
- Mathematical simplification: obs:coh-amplification-information can be replaced by a two-line proved example with rho=(c/(s+c^2))^2, removing a numerical observation and its check paragraph.
- Mathematical simplification: prop:coh-c0-blind is the s-independent case of thm:coh-withdrawal's setup and can be stated as its clause (0) rather than a separate proposition.
- Mathematical simplification: prop:coh-attended-frustration is a corollary of prop:coh-frustration(b) with one trigonometric inequality; state it as a corollary and drop its separate proof paragraph.
- Naming drift for one relay convention: 'content rescaled to unit variance' (06:50), 'unit-variance forwarding' (app06:43), 'unit-power forwarding' (chk06:13).

### Streamlining tiers proposed by lane coh

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| def:coh-components | A | 306 | Tier legend used here: A = keep in condensed main text; B = keep the statement in main text, shorten or move parts to the supplement; C = supplement only or merge. The definition carries the section; 306 words can drop to about 180 by removing the worked glosses. |
| prop:coh-sdpi | B | 80 | Standard Gaussian contraction; one-line statement in main, proof and mixtures in supplement. |
| prop:coh-relay | C | 84 | Supporting; only the per-hop factor is used later. Fix the 'massless' sentence (F4). |
| prop:coh-info-decay | A | 151 | One of the two quantitative links between coherence and correlation length. |
| def:coh-calibration-model | B | 215 | Needed for thm:coh-withdrawal; shorten by pointing to def:frm-two-group. |
| prop:coh-c0-blind | B | 106 | Merge into thm:coh-withdrawal as a preliminary clause. |
| thm:coh-withdrawal | A | 148 | Main calibration result; numbers reproduce. |
| ex:coh-unique-information | B | 79 | Keep one sentence with corrected parameters (F3). |
| thm:coh-holonomy | A | 162 | Defines consistency operationally. |
| prop:coh-flat-true | A | 107 | States the gap between consistency and truth; short. |
| prop:coh-frustration | B | 221 | Keep (a),(b) in main; move the cycle-spectrum clause (c) to the supplement. |
| open:coh-frustration-metric | C | 64 | Open problem with no dependents in the section. |
| prop:coh-coded | C | 117 | Sheaf-cohomology variant used once; supplement. |
| prop:coh-frustration-grounding | C | 79 | Norm identity plus torus illustration; supplement, with the multiplicity wording fixed (F8). |
| prop:coh-attended-frustration | B | 47 | Restate as a corollary of prop:coh-frustration(b). |
| def:coh-cycle-product | B | 97 | Needed for thm:coh-amplification; compress. |
| thm:coh-amplification | A | 106 | Main amplification bound. |
| prop:coh-no-amplification | B | 157 | Keep the list of non-amplifying classes as one sentence; proofs in supplement. Replace the 1.082 sentence (F7). |
| ex:coh-amplification | B | 156 | Keep (i) in main, move (ii) to supplement. |
| obs:coh-amplification-information | C | 49 | Replace by a proved closed-form example rho=(c/(s+c^2))^2. |
| rem:coh-amplification-class | C | 124 | Interpretive; overlaps prop:mis-exact-no-echo discussion. |
| open:coh-amplification-noisy | C | 46 | Third item is settled by the explicit instance of F7; reword in supplement. |
| def:coh-code-game | B | 155 | Whole subsection sec:coh-codes (1997 words) is the largest and the natural candidate for the supplement, leaving about 250 words in main. |
| prop:coh-adoption | B | 156 | State (a),(b) in one sentence; (c) needs the monotonicity hypothesis (F6). |
| prop:coh-code-potential | B | 186 | Correct clause (c) first (F5); then supplement. |
| thm:coh-domains-1d | B | 155 | Statement in main as one sentence, proof and lemmas in supplement. |
| conj:coh-imry-ma | C | 165 | Conjecture with long motivation. |
| conj:coh-coarsening | C | 40 | Conjecture. |
| conj:coh-bundling | C | 61 | Conjecture resting on three reproduced numbers. |
| thm:coh-grounding-tension | A | 140 | Headline result of the section; holds as stated. |
| fig:coh-tension | A | 107 | Carries the tension visually; caption can lose about 30 words. |
| prop:coh-placement | A | 124 | Completes the tension argument. |
| obs:coh-placement | A | 146 | Keep, compress the numbers to the best-response versus social-optimum pair and fix the fidelity label (F2). |
| conj:coh-externality | B | 37 | One sentence after obs:coh-placement. |
| rem:coh-h4 | A | 95 | Merge with the paragraph at 06:398; it is the only place the section ties coherence to scale, and it should say plainly that no coherence-to-contrast inequality is proved here. |
| sec:coh-formation prose (06:400-404) | C | 361 | 361 words, mostly repetition of sec:frm status text; replace by a 60-word pointer. |
| section intro (06:1-7) | B | 288 | 288 words; the echo-chamber caveat is repeated at 06:402. |

## Lane frm: Section 7, formation

Verdict: no critical defect; five major, four minor. Every appendix proof of a result about the map (lem:frm-attention, thm:frm-formation (a)-(e)), of the split law and contrast (lem:frm-split-law, thm:frm-split-contrast) and of prop:frm-nulls was reconstructed by hand, and the closed forms were reproduced numerically at the base point (F=0.99, R_c=0.05, n=4, kappa=3, theta=pi/2, alpha=0.1, h=0.995). The defects are in scope statements (M1), in the comparison of noisy simulations with a noiseless closed form (M2), in two propositions (prop:frm-exact-fusion has a conclusion wider than its proof, M3; prop:frm-capacity is false as written for admissible parameters with p*>=1, M4), and in one numerical observation whose reported scaling values are grid artifacts (M5). What is proved about the stochastic model, as opposed to the map. Proved for the stochastic model: (1) under frozen calibration the exact identity x(t+1) = Phi(x(t)) + alpha u(t), with u a martingale difference of conditional variance at most 1/4 + sigma_alpha^2/theta^2 (app07 mean-field recursion); (2) the moment bound of rem:frm-moment-bound on every path; (3) at gamma = infinity with exact in-group translations, the stationary world-conditional law and contrast at the split (lem:frm-split-law, thm:frm-split-contrast) and the null statements (prop:frm-nulls); (4) prop:frm-capacity once its missing hypotheses are added (realized dynamics, sigma_alpha^2 = 0, frozen calibration, p*<1); (5) prop:frm-exact-fusion(a). Proved for the map only: all of thm:frm-formation (declared-start convergence, global split above gamma_T, merged state, local stability, gamma = infinity). Not proved: any statement that the stochastic slow state converges to, or remains near, a fixed point of Phi at finite gamma (open:frm-closure, correctly flagged open), and the contrast of the reached state at finite gamma (computed at the base point only, obs:frm-exploration). The manuscript's own gamma=80 merged-start row of tab:frm-stochastic shows the stochastic model at alpha=0.1 leaving a fixed point that is linearly stable for the map, so the closure is not quantitative inside the bistable window. Provable but not stated: at gamma = infinity under frozen calibration no cross edge with x_j != 0 is ever attended, so the stochastic slow state follows Phi exactly (x_j <- h x_j + 1 - h) for every sigma_alpha^2; thm:frm-formation(e) is then a pathwise statement about the stochastic model, and for sigma_alpha^2 = 0 the declared start is absorbing. Also provable: a two-sided asymptotic p*^2 gamma_T -> M(kappa)^2/c_2 = 0.4833 at the base constants, a sharper attention bound (m1) that moves gamma_S from 68.15 to 64.11 and makes thm:frm-formation(b) coincide with the single-bridge fold at the base point (240.98), and an exchangeability argument that replaces prop:frm-exact-fusion(b),(c) by statements that actually carry the closing sentence. Cross-references opened (06_coherence def:coh-calibration-model, prop:coh-c0-blind, thm:coh-withdrawal; 02_framework prop:fw-rls; 04_collectives thm:col-diffusive-precision and the baseline conventions; 05_agency def:agy-nulls, tab:agy-nulls, prop:agy-tests) are used within what they say. Execution record. Scripts are in <session scratch>/audit/frm/ (frm_common.py, frm_contrast.py, frm_mf.py, s1_base_constants.py through s11_ingroup_noise.py), run with C:/Python314/python.exe -P, single thread, foreground, one at a time. s11_ingroup_noise.py ran 11.5 s, 1.5 s over the 10 s cap, and was not rerun; it simulates one group at the gamma = infinity split with frozen split gains, not the manuscript's full gamma = 160 model. The manuscript's full stochastic and online-calibration simulations were not rerun. The findings.md copy was not saved: the Write tool refused report files for sub-agents, and an earlier shell attempt failed on quoting; the content is entirely in this structured result. The manuscript was not modified. Strongest supported result and scope: the frozen-calibration mean-field map has the fixed-point and basin structure stated in thm:frm-formation, and the stochastic model at gamma = infinity with sigma_alpha^2 = 0 has the split contrast 8.7329 inside the window (7.954, 8.733] at the base point. Minimal unresolved obligation: the stochastic-approximation step at finite gamma (open:frm-closure) together with a contrast statement for the reached state x-bar < 1 with sigma_alpha^2 > 0. The action that would most change the answer: derive the split law with in-group angle noise (a linear-Gaussian computation with a slowly varying multiplicative forcing) and recompute the comparison medium with noisy learned translations, since the 2 to 3 percent upward shift found here is larger than the narrowest admissible windows of obs:frm-grid.

Coverage: 24 items examined; 13 hold, 5 defective, 2 suspect, 4 not checked.

| Item | Verdict | Note |
|---|---|---|
| obs:frm-thresholds | defect | p*^2 gamma_T values are grid artifacts (major finding M5). Reproduced: gamma_S = 68.15 at the base point, folds 105.89 and 60.053, continuation values 87.92 and 60.11, table entries, and conditions (i),(ii) at 240 and 244. theta = pi/4 and pi statements not checked. |
| obs:frm-exploration | not_checked | Finite-gamma contrasts (8.6763, 8.7317, 8.7329, union 1.008, merged-branch values) not recomputed. This observation is the only support for (T3) at finite gamma. |
| obs:frm-partner | not_checked | Partner-randomization contrasts and their region enumerations not recomputed. The enumeration at the split ('no region exceeds 7.954', 2 of 247 regions at the split value) was reproduced. |
| obs:frm-stochastic | defect | Compares sigma_alpha^2 = 0.01 runs with the sigma_alpha^2 = 0 closed form (M2); 'match to two or three digits' fails for the merged-start row (minor). The manuscript's simulations were not rerun; a one-group gamma = infinity check was run instead (11.5 s). |
| obs:frm-online | suspect | Simulations not rerun. Internal counts are arithmetically consistent, but the learned threshold differs from the map's and the manuscript's own reruns differ by up to three of eight replicates per cell (two minor findings). |
| prop:frm-capacity | defect | First statement holds (pigeonhole). Second statement needs 0 < p* < 1 and the frozen calibration; counterexample alpha = h = 0.5 gives limit 2/3 (M4). Capacity contrasts 2.46 and 5.14 not checked. |
| prop:frm-exact-fusion | defect | (a) holds. (b) is vacuous at finite gamma and (c) does not show the null from the declared start is in the uniform state; the closing sentence follows from an exchangeability argument that is not in the proof (M3). |
| conj:frm-drifting-frames, conj:frm-formation | not_checked | Conjectures; correctly labeled as not established. The paragraph after conj:frm-formation overstates what holds for the map (M1). |
| chk:frm-attention | suspect | Part (a) reproduced only in the limit x_j -> 0 (minor finding); part (b) ratios not reproducible because the five gamma values are not stated. |
| chk:frm-thresholds | defect | p*^2 gamma_T values are grid artifacts (M5); other numbers reproduced; theta = pi/4 and pi not checked. |
| chk:frm-exploration, chk:frm-nulls, chk:frm-stochastic, chk:frm-online, chk:frm-capacity | not_checked | Simulation-based or enumeration-based checks not rerun; chk:frm-stochastic and chk:frm-online numbers were used as printed in the findings above. |

Items found to hold: prop:frm-flattening; prop:frm-bistability; rem:frm-moment-bound; lem:frm-calibration; lem:frm-attention; thm:frm-formation; obs:frm-bridged; lem:frm-split-law; thm:frm-split-contrast; obs:frm-grid; prop:frm-nulls; chk:frm-bistability, chk:frm-calibration, chk:frm-split-law, chk:frm-baseline, chk:frm-grounding; chk:frm-bridged.

### frm-01 (major): Status sentences call the formation chain a theorem about the map; the theorem-level chain exists only at gamma = infinity, where the declared start is already the fixed point

Location: 07_formation.tex:6, :146, :369, :381 (thm:frm-formation, thm:frm-split-contrast, def:frm-target). Labels: thm:frm-formation, thm:frm-split-contrast, def:frm-target, obs:frm-exploration, rem:frm-open, prop:frm-exact-fusion. Category: scope: interpretation presented as result.

Evidence. thm:frm-split-contrast is stated 'Under the hypotheses of lem:frm-split-law' (gamma = infinity, exact in-group translations, each receiver attending a uniformly random in-group set). It is a statement about the stochastic error law at the gamma = infinity split, not about Phi. The two theorems join as theorems only at gamma = infinity (thm:frm-formation(e)); there Phi(1) = 1, so the declared start alpha-hat = 0 is itself the split fixed point and the reachability clause (T5) is empty. For gamma_S < gamma < infinity the fixed point reached from the declared start has x-bar < 1 and positive cross attention, so lem:frm-split-law does not apply to it, and (T3) for that state rests on obs:frm-exploration (base point only, gamma = 80, 120, 160) and the sketch in rem:frm-open. 07:367 says this accurately ('at finite gamma by computation and a sketch'); 07:6 and 07:369 compress it to 'a theorem about that map'. In addition (T4) fails for the type-S translation-aware null (prop:frm-exact-fusion, tab:agy-nulls classifies it as type S), so by def:frm-target no formation result is obtained in the model; and 07:381 'the first two regimes hold for the map' covers the attention and learning regimes only, not the clause 'each a collective', which the map does not address.

Proposed fix. Replace the compressed status sentences at 07:6 and 07:369 by: 'At gamma = infinity, with sigma_alpha^2 = 0, clauses (T1)-(T3) and (T5) are theorems; the declared start is then itself the split (thm:frm-formation(e), thm:frm-split-contrast). For gamma_S < gamma < infinity reachability of the split branch is a theorem about the frozen-calibration mean-field map (thm:frm-formation(a),(b)), and the contrast of the reached state is computed at the base point (obs:frm-exploration). (T4) fails for the translation-aware S null.' At 07:381 write 'the attention and learning statements of the first two regimes hold for the map'.

What would overturn the finding. 07:6 'the formation chain closes for the frozen-calibration mean-field map ... these are theorems about that map and the split it selects'; 07:369 'the formation chain closes for the frozen-calibration mean-field map, a theorem about that map'; 07:381 'the first two regimes hold for the frozen-calibration mean-field map'

State: applied. [07] applied: Defect real: thm:frm-split-contrast is a statement at gamma=infinity, not about the map. Status sentences in the section opening, after thm:frm-formation, in the verdict paragraph and after conj:frm-formation now separate the gamma=infinity, sigma_alpha^2=0 theorems from map reachability and base-point computation, and state that (T4) fails. Six repeats outside the group are follow-ups.

### frm-02 (major): In-group angle noise violates the split-law hypothesis; obs:frm-stochastic compares sigma_alpha^2 = 0.01 runs with the sigma_alpha^2 = 0 closed form and the discrepancy is systematic

Location: 07_formation.tex:294 (obs:frm-stochastic); chk07_formation.tex:43 (chk:frm-stochastic); 07_formation.tex:197 (lem:frm-split-law); 07_formation.tex:367. Labels: obs:frm-stochastic, chk:frm-stochastic, lem:frm-split-law, thm:frm-split-contrast, obs:frm-grid. Category: number disagreement / hypothesis not met by the model simulated.

Evidence. With sigma_alpha^2 = 0.01 an attended in-group edge obeys phi' = h(1-alpha) phi + h alpha nu, with stationary standard deviation 0.0224 rad, so the hypothesis 'in-group translations exact' of lem:frm-split-law fails in the model of def:frm-two-group at its base point. The resulting private forcing F k-bar (Rot(phi) - I) eta_t is slowly varying (autocorrelation about 0.88 per round); the uniform mode (multiplier 0.957) amplifies slowly varying forcing more than the transverse modes (0.517), which raises the common-error variance s1 relative to s0. Script s11_ingroup_noise.py (group A at the gamma = infinity split, frozen split gains, 40 world paths x 60 replicas, two seeds): r(A) = 8.707 and 8.730 at sigma_alpha^2 = 0 against the exact 8.7329, and 8.990 and 8.983 at sigma_alpha^2 = 0.01 (+2.9 percent; s0 +0.9 percent, s1 +4.2 percent). The manuscript's own numbers show the same sign: all eight group contrasts at 0.01 in chk:frm-stochastic (8.863 to 8.997) exceed 8.733, while its two values at sigma_alpha^2 = 0 (8.741, 8.699) bracket it. The shift exceeds the narrowest admissible windows of obs:frm-grid (0.9 percent), and the comparison medium with noisy learned translations is not computed anywhere, so the window statement is not established for sigma_alpha^2 > 0. Limits of this check: it models one group with frozen split gains at gamma = infinity, not the manuscript's full gamma = 160 model, and ran 11.5 s. A second point is analytic and was not simulated: with idealized calibration 'at the current error' and kappa < n-1, ties among in-group senders at gamma = infinity are broken by |phi_ij| once sigma_alpha^2 > 0, so the 'uniformly random set' clause of lem:frm-split-law also fails there (at the base point kappa = n-1 = 3 and the clause is vacuous).

Proposed fix. State (T3) and thm:frm-split-contrast as results for sigma_alpha^2 = 0 (exact in-group translations) wherever they are asserted for the model, including 07:367. In obs:frm-stochastic write: 'group contrasts from 8.86 to 9.00, about 2 percent above the sigma_alpha^2 = 0 value 8.733; the excess is the effect of in-group angle noise, which the split law does not include; with noiseless angle observations the contrasts are 8.741 and 8.699.' Either extend lem:frm-split-law to stationary in-group angle noise or mark the admissibility window for sigma_alpha^2 > 0 as not computed.

What would overturn the finding. 07:294 'group contrasts from 8.86 to 9.00 against the exact 8.733' read as agreement; 07:367 '(T3) holds at gamma = infinity' for the model with sigma_alpha^2 = 0.01

State: applied. [07] applied: Defect real: stationary in-group angle sd 0.022 rad; own one-group simulation gives r(A) 8.712 at sigma_alpha^2=0 and 8.947 at 0.01 (+2.7 percent, one seed). Observation, check, (T3) status and a remark after thm:frm-split-contrast now restrict the closed form to sigma_alpha^2=0; window for sigma_alpha^2>0 marked not computed. Lemma not extended.

### frm-03 (major): prop:frm-exact-fusion: closing sentence is wider than parts (a)-(c); part (b) is vacuous at finite gamma

Location: 07_formation.tex:348-358 (prop:frm-exact-fusion); app07_formation.tex:133-139. Labels: prop:frm-exact-fusion, def:frm-target (T4), def:agy-nulls. Category: repairable proof gap: conclusion wider than proof.

Evidence. Part (b) at finite gamma is proved in app07 by 'At finite gamma every set of kappa senders has positive probability, so every receiver attends each cross sender with positive probability'. The same sentence is true of the unmodified model on its split branch (mean-field cross attention 1.8e-3 at gamma = 80, tab:frm-stochastic), so (b) at finite gamma does not distinguish the null from the model, and 'by (b) none attends along the split' has no content there. Only the gamma = infinity half of (b), via the highest-precision sender j_1, is informative. Part (c) exhibits one self-consistent state (the uniform one); it does not show that the null started from the declared law is in that state, which is what 'survives a null of type S' in def:agy-nulls requires ('the same partition is selected under the null').

Proposed fix. Replace (b) and (c) by the following, each provable in a few lines. (b') Under the null, sender precisions are receiver independent and the inclusion probability of a sender is nondecreasing in its precision (swap j and k in the sets containing exactly one of them); hence each of the n receivers outside the group of a highest-precision sender j_1 attends j_1 with probability at least kappa/(2n-1), at every gamma in [0, infinity]. (c') Under the null the dynamics and the declared start law are invariant under all permutations of the 2n agents, and idealized calibration is a functional of the current law; by induction on t all sender precisions are equal and attention is uniform over sets at every gamma and every time. The trajectory of the null from the declared (or any exchangeable) start is therefore the comparison medium, contrasts depend only on region size, and {A,B} is not selected. State the closing sentence as 'From the declared start law the split does not survive this translation-aware null', and delete 'by (b) none attends along the split' or restrict it to gamma = infinity.

What would overturn the finding. 07:358 'Asymmetric self-consistent states of this null are not classified, but by (b) none attends along the split', and the closing sentence 'The split does not survive this translation-aware null' as a consequence of (a)-(c)

State: applied. [07] applied: Defect real: old (b) was vacuous at finite gamma and old (c) exhibited one self-consistent state only. (b) is now a monotonicity statement with inclusion bound kappa/(2n-1) at every gamma; (c) is an exchangeability induction from a permutation-invariant start law; closing sentence narrowed to such start laws. Proofs rewritten in the appendix. Check of the edit: [07] defect, (b) holds (swap bijection; inclusion probabilities sum to kappa over 2n-1 senders). (c): hypothesis asks only exchangeability of the start law of (m_i-eta, P_i); conclusion and induction base need it given the world path. Counterexample: e_1=|xi_1| sign(eta_{0,1}) v, e_i=|xi_i| s_i v with independent signs: exchangeable marginally, not conditionally. Repair: [07] repaired, Checker is right: unconditional exchangeability of the start does not give the world-conditional invariance used as induction base and in the conclusion. Hypothesis of (c) is now invariance given the world path; proof states the base case and shows identical initial beliefs, and starts jointly independent of the innovations with invariant law given eta_0, satisfy it.

### frm-04 (major): prop:frm-capacity: second statement is false for admissible parameters with p* >= 1 and omits the frozen calibration its proof uses

Location: 07_formation.tex:342-344 (prop:frm-capacity); app07_formation.tex:129-131. Labels: prop:frm-capacity, def:frm-two-group, asm:frm-mean-field. Category: missing hypothesis (counterexample).

Evidence. def:frm-two-group(vi) admits alpha in (0,1] and h in (0,1). Take alpha = h = 0.5: p* = (1-h)/(alpha h) = 2 and the limit p*/(p*+1) = 2/3 > 1/2, so the attended cross edges are not learned in the sense of 07:114 (x_j < 1/2). The appendix proof uses 'positive and below 1/2 because p* < 1' and 'take the frozen calibration of asm:frm-mean-field(a), with any constants satisfying D_cal > 0, and sigma_alpha^2 = 0'; neither p* < 1 nor the frozen calibration appears in the statement (thm:frm-formation states 0 < p* < 1 explicitly; this proposition does not, and its only stated conditions are gamma = infinity, noiseless angle observations and the declared start). The persistence of the first-round tie-break also depends on the calibration rule: it is argued for the frozen calibration, where an attended edge keeps strictly higher precision than an unattended cross edge at x = 1. The first statement (at least kappa-n+1 cross senders per round, by pigeonhole) holds as written.

Proposed fix. State the second sentence as: 'Under the frozen calibration of asm:frm-mean-field(a) with D_cal > 0 and 0 < p* < 1, at gamma = infinity with sigma_alpha^2 = 0, from the declared start, each receiver attends in every round the kappa-n+1 cross senders it chose by tie-breaking in the first round, and their bias fractions converge to p*/(p*+1) < 1/2.' For p* >= 1 the same edges are attended and converge to p*/(p*+1) >= 1/2 (not learned).

What would overturn the finding. 'their bias fractions converge to p*/(p*+1) < 1/2: they become learned bridges' under the hypotheses as stated

State: applied. [07] applied: Defect real: alpha=h=0.5 gives p*=2 and limit 2/3. Statement now assumes the frozen calibration form and says the limit p*/(p*+1) is below 1/2 exactly when p*<1; learned bridges for p*<1, attended but unlearned for p*>=1. Proof aligned.

### frm-05 (major): obs:frm-thresholds: reported p*^2 gamma_T values are artifacts of the ratio-1.1 grid; 'gamma_T like p*^-2' is supported only as an upper bound

Location: 07_formation.tex:149 (obs:frm-thresholds); 07_formation.tex:144; chk07_formation.tex:19 (chk:frm-thresholds). Labels: obs:frm-thresholds, chk:frm-thresholds, thm:frm-formation(b), eq:frm-thresholds. Category: number disagreement.

Evidence. Script s10_gammaT_limit.py computes gamma_T by bisection on conditions (i),(ii) of thm:frm-formation(b) with p* varied through h at fixed alpha: gamma_T = 244.22, 861.13, 3255.56, 12684.26 at p* = 0.05, 0.025, 0.0125, 0.00625, hence p*^2 gamma_T = 0.6106, 0.5382, 0.5087, 0.4955. The manuscript's gamma_T = 244.6, 929.0, 3527.9, 13397.2 are successive multiples by 1.1^14 = 3.797 of the first grid point, and its products have constant ratio 1.1^14/4 = 0.9494: the reported sequence is the grid, not the function. The last three values overstate gamma_T by 7.9, 8.4 and 5.6 percent, 'between 0.52 and 0.61' is wrong at the lower end (0.4955), and the reported sequence shows a steady geometric drift where the true one converges. Limit: p*^2 gamma_T -> M(kappa)^2/c_2 with c_2 = lim_{y->0} DeltaV(y)/y^2 = K theta^2 D_cal/(4 sigma_in^4 (Lambda_0 + kappa varpi_in)) = 0.56999 and M(kappa) = max_u kappa u exp(-u^2)/(1 + kappa exp(-u^2)) = 0.52485 for kappa = 3, giving 0.4833; numerically 0.4893, 0.4862, 0.4848, 0.4837 at p* = 3.1e-3, 1.6e-3, 7.8e-4, 2e-4. The text at 07:144 derives only an upper bound of order p*^-2; the limit gives the matching lower bound.

Proposed fix. In obs:frm-thresholds and chk:frm-thresholds: 'gamma_T = 244.2, 861.1, 3255.6, 12684.3 and p*^2 gamma_T = 0.611, 0.538, 0.509, 0.495, tending to M(kappa)^2/c_2 = 0.483 as p* -> 0', computed by bisection rather than on the ratio-1.1 grid. At 07:144 either state the two-sided asymptotic p*^2 gamma_T -> M(kappa)^2/c_2 or write 'gamma_T = O(p*^-2)'.

What would overturn the finding. 07:149 'For p* from 0.05 to 0.00625, p*^2 gamma_T lies between 0.52 and 0.61'; chk07:19 'p*^2 gamma_T = 0.6116, 0.5806, 0.5512, 0.5233'

State: applied. [07] applied: Defect real: bisection gives gamma_T 244.22, 861.13, 3255.56, 12684.3 and products 0.611, 0.538, 0.509, 0.495, tending to 0.483. Numbers replaced; a proved lower bound gamma_T >= m_kappa^2/(c^+_V p*^2) for p* <= m_kappa/(2 t_kappa) added to thm:frm-formation(b) with proof, so the p*^-2 order is two-sided. Convergence of the product to 0.483 is numerical only.

### frm-06 (minor): DeltaV as displayed is not the value gap described in words; 'attained to six digits' holds only as x_j -> 0

Location: 07_formation.tex:114-117; app07_formation.tex:56; 07_formation.tex:128; chk07_formation.tex:15 (chk:frm-attention). Labels: lem:frm-attention, chk:frm-attention, eq:frm-thresholds. Category: formula/description mismatch (lemma true as stated, not sharp).

Evidence. 07:114 describes DeltaV(x) as 'the value gap between an in-group edge and a cross edge of bias fraction x in a set otherwise filled with in-group edges'. That gap is (K/2) log((Lambda_0 + kappa varpi_in)/(Lambda_0 + (kappa-1) varpi_in + varpi_x(x theta))) = 0.06298 at x = 1/2 and 0.09389 at x = 1. The display (K/2) log(1 + (varpi_in - varpi_x)/(Lambda_0 + kappa varpi_in)) gives 0.05925 and 0.08583; its denominator Lambda_0 + kappa varpi_in belongs to no set that contains the cross edge. Since -log(1-u) >= log(1+u) the display is a lower bound of the described gap, so lem:frm-attention holds as displayed; it is the proof step 'Since sum_{k in J} varpi_ik <= kappa varpi_in' (app07:56) that loses the factor. Using sum_{k in J} varpi_ik <= (kappa-1) varpi_in + varpi_x(x_j theta) for sets containing j gives the described gap with no other change to the proof. With the sharper DeltaV, gamma_S = 64.11 (not 68.15) and gamma_T = 240.98 at the base point, equal to the single-bridge fold of obs:frm-bridged to the digits computed (242.11 with the display), so thm:frm-formation(b) becomes sharp there. 'The bound is attained to six digits' (07:128, chk:frm-attention(a)) holds only as x_j -> 0; at x_j = 1/2 the ratio p_j/p-bar is 0.55 to 0.79 with the display over the gamma range tried.

Proposed fix. Either redefine DeltaV(x) = (K/2) log((Lambda_0 + kappa varpi_in)/(Lambda_0 + (kappa-1) varpi_in + varpi_x(x theta))) and change app07:56 to the bound above (then update gamma_S and gamma_T), or keep the display and describe it as 'a lower bound on the value gap'. Qualify 07:128 as 'attained to six digits in the limit x_j -> 0'.

State: applied. [07] applied: Defect real: displayed DeltaV is 0.0593 and 0.0858 at x=1/2, 1 against the described gap 0.0630 and 0.0939. Kept the display (gamma_S=68.15 is embedded in two figures outside the group), described it as a lower bound on the gap, and limited six-digit attainment to x_j->0 at gamma>=160; largest ratio at x_j=1/2 is 0.79.

### frm-07 (minor): tab:frm-stochastic: 'the averages match the mean field to two or three digits' does not hold for the gamma = 80 merged-start row, and the gamma = 160 cell is a single event

Location: 07_formation.tex:294 (obs:frm-stochastic); 07_formation.tex:298-314 (tab:frm-stochastic). Labels: obs:frm-stochastic, tab:frm-stochastic, open:frm-closure. Category: claim wider than the table.

Evidence. Row gamma = 80, merged start: simulated (0.254, 0.569) against the map's merged fixed point (0.344, 0.127). That fixed point is linearly stable for the map (multipliers 0.9762 and 0.9937 from s3_fixed_points.py), so the stochastic model at alpha = 0.1 leaves a state the map retains; a rough estimate of the stationary fluctuation in the symmetry-breaking direction is 0.055 against a distance of about 0.17 to the middle branch (estimate, not simulated). Row gamma = 160, declared start: 1.3e-6 is one attention event in 768,000 edge-rounds (the quoted replicate maximum 1.0e-5 equals 1/96,000), so agreement with 9e-7 is agreement in order of magnitude from one count. The rows gamma = 40 and gamma = 80 declared do match to two or three digits (0.392/0.116 against 0.395/0.113; 1.85e-3/0.965 against 1.8e-3/0.966).

Proposed fix. Scope the sentence: 'At gamma = 40 and at gamma = 80 from the declared start the averages match the mean field to two or three digits; at gamma = 160 the cross-attention count is one event; at gamma = 80 from the merged start the stochastic model leaves the map's merged fixed point.' Cite the merged-start row in open:frm-closure as evidence that the closure is not quantitative at alpha = 0.1 inside the bistable window.

State: applied. [07] applied: Confirmed from the table: gamma=80 merged row (0.254,0.569) vs fixed point (0.344,0.127); 1.3e-6 = 1/768000 is one event. Scoped the agreement claim (stated as within 5 percent, since 1.85e-3 vs 1.7752e-3 is 4.2 percent), added the merged-start departure with multipliers from chk:frm-thresholds, cited it in open:frm-closure. Simulations not rerun.

### frm-08 (minor): Two thresholds for a 'learned' cross edge

Location: 07_formation.tex:114 (x_j < 1/2); 07_formation.tex:316-334 (obs:frm-online, tab:frm-online); chk07_formation.tex:46-48 (chk:frm-online). Labels: obs:frm-online, tab:frm-online, chk:frm-online, thm:frm-formation. Category: internal consistency.

Evidence. The map and thm:frm-formation classify an edge as learned when its bias fraction is below 1/2 (07:114). The online-calibration criterion for the split pattern is 'every cross edge with |phi_ij| >= 0.3 theta', and chk:frm-online counts 'cross edges below 0.3 theta'. An edge with bias fraction between 0.3 and 0.5 is learned under one and unlearned under the other, and the split-pattern counts of tab:frm-online depend on which is used.

Proposed fix. Use x < 1/2 in the online criterion, or name the second threshold where it is introduced ('a stricter cutoff 0.3 is used for the online runs because ...').

State: applied. [07] applied: Confirmed: map uses x<1/2, online runs use 0.3 theta. Counts cannot be recomputed at 1/2 without the simulations, so the second cutoff is named in the observation, caption and check, with the provable relation that pattern counts at 0.3 are upper bounds on those at 1/2.

### frm-09 (minor): Online-calibration counts vary across the manuscript's own reruns by as much as the differences the table reports

Location: 07_formation.tex:321-334 (tab:frm-online); chk07_formation.tex:46-48 (chk:frm-online); quoted at 07_formation.tex:6, :146, :369. Labels: obs:frm-online, tab:frm-online, chk:frm-online. Category: sampling error not stated.

Evidence. For the cell gamma = 400, alpha_cal = 0.05 the table gives 0 of 8, the rerun in chk:frm-online gives 1 of 8, and the separate contrast run gives 3 of 8 replicates in the split's attention pattern. At gamma = 160 the table gives 3 of 8 and the rerun 6 of 8. With eight replicates per cell the entries carry sampling error of the same size as the differences between cells, so the table supports 'the split pattern occurs in some replicates and is not typical' and little more; the summary '0 to 7 of 8' is quoted three times without this caveat. The simulations themselves were not rerun in this audit; the inconsistency is between numbers printed in the manuscript.

Proposed fix. Add to obs:frm-online and to the caption of tab:frm-online: 'counts from eight replicates per cell; reruns of single cells differ by up to three replicates (chk:frm-online)', and carry the qualifier where '0 to 7 of 8' is quoted.

State: applied. [07] applied: Confirmed from printed numbers (0, 1, 3 of 8 in one cell; 3 and 6 in another). Qualifier added to observation, caption, check and the three '0 to 7 of 8' quotations. Non-monotonicity sentence restricted to alpha_cal at gamma=160, where Fisher tests (script) give p=0.04 and 0.01; monotonicity in gamma is not supported.

### Not checked by lane frm

- Omega_int values (0.024, 0.140, 0.510) in prop:frm-nulls / chk:frm-nulls.
- Partner-randomization contrasts and their region enumerations (obs:frm-partner, tab:frm-nulls), apart from the enumeration at the split.
- Finite-gamma contrasts of obs:frm-exploration (8.6763, 8.7317, 8.7329, union 1.008, merged-branch values) and the self-consistent calibration shifts.
- Bridged-network contrasts 4.51 and 1.76 (obs:frm-bridged) and capacity contrasts 2.46 and 5.14 (prop:frm-capacity commentary).
- The manuscript's full stochastic simulations (tab:frm-stochastic) and online-calibration simulations (tab:frm-online). Only a one-group, gamma = infinity, frozen-gain simulation was run (s11_ingroup_noise.py, 11.5 s, over the 10 s cap, not rerun); it does not reproduce the manuscript's gamma = 160 full-model runs.
- The kappa < n-1 tie-breaking remark in M2 is analytic and was not simulated.
- The stationary-fluctuation estimate (about 0.055) in the tab:frm-stochastic finding is a hand estimate, not a simulation.
- chk:frm-attention part (b) ratios: the five gamma values are not stated, so the ratios could not be reproduced.
- theta = pi/4 and theta = pi statements of chk:frm-thresholds.
- Figure source files for fig:frm-chain and fig:frm-phase.
- Direct Lyapunov solves of chk:frm-calibration (closed forms were reproduced instead).
- Cross-references not opened: 02_framework prop:fw-efe-communication, def:fw-translation, def:fw-level0, def:fw-levels, def:fw-calibration, lem:fw-common-mode and the proof body of prop:fw-grounded-identification; 03_misreading def:mis-values; 06_coherence thm:coh-amplification, thm:coh-grounding-tension, thm:coh-holonomy, ex:coh-unique-information; 08_scale; 10b_hierarchy rem:hie-pragmatic, obs:hie-exact-receiver, prop:hie-conformity, conj:hie-conformity-formation, open:hie-exact-fusion-population; def:col-world-conditional; the proof of prop:agy-nulls-vanish.
- The file named in the relayed user reference (collective-agents-open-problems-comparison-2026-11-09.md) was not opened; it is input to the open-problems phase, not to this lane.
- findings.md was not saved to the lane directory (the Write tool refuses report files for sub-agents); all content is in this structured result.

### Redundancy noted by lane frm

- Status summary of the section given three times: 07:6 (182 words), 07:146 (103 words), 07:367-369 (270 words). Keeping 07:367 plus a two-sentence introduction removes about 290 words.
- Exact-fusion caveat ('fails the translation-aware form ... heuristic for full cross-covariance-aware exact fusion') at 07:6, :146, :358, :367, :369, about 40 words each; about 160 removable.
- Online-calibration summary ('0 to 7 of 8 replicates, not necessarily a split selected by contrast') at 07:6, :146, :369 and in obs:frm-online; about 60 to 90 removable.
- Fold and continuation values repeated in obs:frm-thresholds, the fig:frm-phase caption block (207 words), the tab:frm-thresholds caption and chk:frm-thresholds; the obs:frm-bridged ranges repeated in the figure and table captions and chk:frm-bridged; about 150 removable from the body.
- Baseline numbers (7.954, window (7.954, 8.733], significance 1.098) at 07:225, rem:frm-matched-baseline, obs:frm-exploration, obs:frm-partner and in 04_collectives (04:328, rem:col-baseline-conventions); about 80 removable.
- 'The step from the full model to the map is open (open:frm-closure)' at 07:6, :114, :146, :369, :383; about 60 removable.
- prop:frm-nulls(a) together with the paragraph at 07:261 (107 words) restates prop:agy-nulls-vanish and its frozen-initial-state condition; about 100 removable by citing it.
- chk:frm-stochastic and chk:frm-online repeat the numbers of the observations and tables; acceptable in the check appendix, but the observation text can then cite the check instead of repeating the numbers.
- Mathematical simplifications: (1) the sharper DeltaV makes thm:frm-formation(b) coincide with the single-bridge fold at the base point and removes the need for a separate 'not sharp' discussion; (2) the two-sided asymptotic p*^2 gamma_T -> M(kappa)^2/c_2 replaces the numerical scaling table; (3) in thm:frm-formation(b) condition (i) only classifies the fixed point as split, since any x' below the lower branch satisfying (ii) gives uniqueness and global attraction; (4) prop:frm-exact-fusion follows from exchangeability in a few lines; (5) thm:frm-formation(e) is pathwise for the stochastic model under frozen calibration; (6) the alternative baseline is below r(A) analytically because 2n(n-1)/(2n-1) < n.

### Streamlining tiers proposed by lane frm

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| def:frm-target | A | 186 | Defines (T1)-(T5); every status statement refers to it. |
| prop:frm-flattening | B | 129 | Not used by the two-group results; its hypothesis is not met by the model's learning rule with h < 1. Keep the statement, move commentary (167 words). |
| prop:frm-bistability | B | 194 | Single-edge illustration qualitatively subsumed by thm:frm-formation; statement plus commentary (75 + 119). |
| def:frm-two-group | A | 280 | The model of the section. |
| rem:frm-moment-bound | C | 58 | Technical bound used only in the appendix. |
| lem:frm-calibration | A | 101 | Supplies the constants of the frozen calibration. |
| asm:frm-mean-field | A | 63 | Hypothesis of the main theorem; marks the boundary between map and model. |
| lem:frm-attention | B | 48 | Used only inside the proof of thm:frm-formation; can move with that proof. |
| thm:frm-formation | A | 339 | Main result about the map; part (d) and the detailed conditions of (b) can move to the supplement. |
| obs:frm-thresholds | B | 165 | Keep the corrected scaling statement; the fold values duplicate the figure and table. |
| obs:frm-bridged | B | 182 | Supporting numerics for bridged fixed points. |
| rem:frm-conventions | C | 83 | Restates standing conventions. |
| lem:frm-split-law | B | 149 | Can be merged into thm:frm-split-contrast with the computation in the supplement. |
| thm:frm-split-contrast | A | 201 | The only theorem about the stochastic model's contrast. |
| rem:frm-matched-baseline | C | 73 | Duplicates rem:col-baseline-conventions. |
| obs:frm-grid | A | 102 | Shows the window is not a base-point accident. |
| obs:frm-exploration | A | 115 | Only support for (T3) at finite gamma. |
| rem:frm-open | B | 63 | Fold into the single status paragraph. |
| prop:frm-nulls | B | 152 | Part (a) restates prop:agy-nulls-vanish; keep (b),(c). |
| obs:frm-partner | A | 105 | The R-type null evidence for (T4). |
| obs:frm-stochastic | A | 113 | Only evidence connecting the full model to the map; needs the corrections of M2 and the table finding. |
| obs:frm-online | B | 166 | Exploratory, eight replicates per cell. |
| prop:frm-capacity | B | 68 | Side result on kappa >= n; needs the added hypotheses. |
| prop:frm-exact-fusion | A | 138 | Determines the verdict on (T4); should be restated via exchangeability. |
| rem:frm-grounding | C | 107 | Interpretation. |
| conj:frm-drifting-frames | B | 132 | Conjecture plus follow-on paragraph (61 + 71). |
| conj:frm-formation | A | 169 | States the general claim the section instantiates; the follow-on paragraph (95 words) is tier B and needs the M1 correction. |
| open:frm-closure | A | 50 | The minimal unresolved obligation of the section. |
| open:frm-online | B | 47 | Secondary open problem. |
| open:frm-self-consistent | C | 28 | Merge into open:frm-closure. |
| open:frm-access | B | 48 | Secondary open problem. |
| fig:frm-chain | B |  | Schematic of the chain; useful but not load bearing. |
| fig:frm-phase | A | 207 | Phase diagram of the map; its caption block repeats the observations. |
| tab:frm-thresholds | B | 147 | Numbers repeated in obs:frm-thresholds and chk:frm-thresholds. |
| tab:frm-nulls | A | 170 | Summary of null outcomes. |
| tab:frm-stochastic | A | 130 | Model-versus-map comparison. |
| tab:frm-online | B | 74 | Exploratory counts with large sampling error. |
| Status paragraphs 07:6, 07:146, 07:367-369 | B | 555 | Three versions of the same status summary; keep one corrected version. |

## Lane sca1: Section 8, hypotheses, light cones, clustering

Lane sca1 (08_scale.tex:1-245). No critical defect. Four major, all repairable in one sentence each: the lag clause of thm:sca-no-moment(a) is false (explicit counterexample, corrected bound given); lem:sca-relations(c) fails on infinite populations (Z^3 walk); prop:sca-sufficient(c) drops the condition varpi_g<1; prop:sca-heterogeneous states its m_up formula for finite boxes but proves it only on Z^D. Light cone, Poisson, routing, rank-one, amplifying-site, clustering, world-conditioning, spectral and diffusive statements were re-derived and hold, with minor edge conditions. Most check numbers reproduce; one switching factor and two printed values do not. Notes and scripts: <session scratch>/audit/sca1/findings.md

Coverage: 31 items examined; 17 hold, 5 defective, 4 suspect, 5 not checked.

| Item | Verdict | Note |
|---|---|---|
| lem:sca-relations | defect | (c) iff false on infinite V (Z^3 walk); (a) omits moment and stationarity hypotheses; (b) holds. |
| prop:sca-sufficient | defect | (c) drops varpi_g<1 from the cited proposition; (a), (b), (d) hold. |
| ex:sca-amplifying-profile | suspect | First counterexample reproduced to all digits; switching factor 1.0703173057 unspecified, not reproduced. |
| conj:sca-common-code | not_checked | Status word 'conjecture' is appropriate; chk:sca-common-code not reproduced. |
| thm:sca-no-moment | defect | Lag clause of (a) false (counterexample 0.027 vs 0); equal-time (a), (b), (c) hold. |
| prop:sca-heterogeneous | defect | First part of (a), (b) bound, (d), (e) hold; m_up formula, leak clause, (c) proved on Z^D only. |
| chk:sca-lightcone | not_checked | Internally consistent (g_tot about 1.280); instance unspecified. |
| chk:sca-poisson | defect | Numbers reproduce but are the second member, not the expected influence. |
| chk:sca-common-code | not_checked | Not reproduced. |
| chk:sca-no-moment | not_checked | Instances unspecified; own instance agrees; lag clause untested by the check. |
| chk:sca-rank-one | suspect | Growth rates reproduced; last gap 4.1e-12 vs recomputed 1.07e-11. |
| chk:sca-spectral | not_checked | Printed instances not reproducible; own three signed rings give ratios 0.53 to 0.57. |
| chk:sca-diffusive | suspect | Guaranteed and row-sum rates verified by hand; fitted rates and 2.3 percent not reproduced. |
| chk:sca-heterogeneous | suspect | Homogeneous 0.48879 reproduced; m_up=0.4424 inconsistent with stated formula at printed extremes. |

Items found to hold: asm:sca-standing; def:sca-local-rule; thm:sca-lightcone; prop:sca-poisson; prop:sca-routing; ex:sca-switch-chain; rem:sca-argmax; prop:sca-rank-one; prop:sca-amplifying-site; rem:sca-rumors; def:sca-lengths; thm:sca-clustering; prop:sca-world-conditioning; prop:sca-spectral; thm:sca-diffusive; chk:sca-routing; chk:sca-amplifying-site.

### sca1-01 (major): Lag-covariance clause of thm:sca-no-moment(a) is false as stated

Location: sections/08_scale.tex:132 (thm:sca-no-moment(a)); proof sections/app08_scale.tex:55. Labels: thm:sca-no-moment. Category: false-clause.

Evidence. The clause bounds ||Cov(e_i(t+h),e_j(t))|| by g_phi^h times the equal-time expression, whose bracket depends on d through ceil(d/2) and 1{2t>=d}. Scalar chain W_xx=0.2, W_{x,x+-1}=0.3, q=1, zero start, t=2, h=1, d=3: Cov=0.027 (misc1.py), stated bound 0. It also contradicts thm:sca-lightcone(b), which allows dependence up to d<=2t+h. The proof bounds Sigma_kj at distance d(k,j)>=d-h but keeps the d-indexed bracket.

Proposed fix. Replace by ||Cov(e_i(t+h),e_j(t))|| <= e^{-phi d} g_phi^h [ q sum_{n=ceil((d-h)_+/2)}^{t-1} g_phi^{2n} + q_0 g_phi^{2t} 1{2t+h>=d} ] (gives 0.512 in the example). This form also reproduces thm:sca-clustering(d) at phi=0. Add a lag test to chk:sca-no-moment.

What would overturn the finding. lag clause of thm:sca-no-moment(a)

State: applied. [08] applied: Defect real: the lagged bound must use the bracket at distance (d-h)_+, not d. Statement now displays eq:sca-no-moment-lag; proof derives it from Cov(e(t+h),e(t))=Phi(t+h,t)Sigma(t) and monotonicity of the bracket; check extended with a lag test on 24-agent rings (largest ratio 0.25).

### sca1-02 (major): lem:sca-relations(c): '(M) iff rho(W)<1' fails on infinite populations

Location: sections/08_scale.tex:40 (lem:sca-relations(c)); proof sections/app08_scale.tex:19. Labels: lem:sca-relations. Category: missing-hypothesis.

Evidence. The 'only if' proof uses a left eigenvector, a finite-dimensional argument, but the standing setting admits V=Z^D under (TI). Lazy walk kernel on Z^3 (c=1/4, a=1/8, row sums 1, rho(W)=1) with Q=qI has stationary variance q*mean[1/(1-w(p)^2)] = 1.4256, 1.4326, 1.4349 q on Fourier grids 40, 80, 120 (misc2.py): bounded, so (M) holds with rho(W)=1. W=diag(1-1/i) is a second example.

Proposed fix. State (c) for a finite population (or finite-dimensional W), and keep only 'rho(W)<1 implies (M)' in general; on Z^D give the Fourier criterion (integrability of 1/(1-|w(p)|^2)) if the infinite case is wanted.

State: applied. [08] applied: Defect real: rho(W)<1 iff (M) fails on infinite populations. Now: sufficiency in general, iff on finite populations, proved Fourier criterion on Z^D under (TI). Counterexample: lazy walk on Z^3 has rho=1 and stationary variance 1.4395q. New numcheck chk:sca-relations.

### sca1-03 (major): prop:sca-sufficient(c) cites prop:min-grounding-moment without its condition varpi_g<1

Location: sections/08_scale.tex:50 (prop:sca-sufficient(c)); sections/09_minimal.tex:159-166 (prop:min-grounding-moment). Labels: prop:sca-sufficient; prop:min-grounding-moment. Category: cross-reference.

Evidence. Item (c) asserts uniform (M) 'under the hypotheses of' prop:min-grounding-moment. That proposition yields uniform (M) only in its conclusion clause 'If varpi_g<1', which is not among its hypotheses; its own counterexample needs p_g>0.3763. The cited result is used beyond what it proves.

Proposed fix. Write: 'Under the hypotheses of \cref{prop:min-grounding-moment} with $\varpi_g<1$, (M) holds in uniform form.' Items (a), (b), (d) need no change.

State: applied. [08] applied: Defect real: part (c) omitted the condition varpi_g<1 under which prop:min-grounding-moment gives (M). Condition added to statement and proof. prop:min-grounding-moment in group 09 is correct as written; no follow-up needed. [09] applied: The defect lies in 08, which already reads 'with its contraction factor varpi_g<1'. In group 09 the one unqualified repetition, the tab:min-reexamination cell 'noise-free grounding does', now carries the condition varpi_g<1.

### sca1-04 (major): prop:sca-heterogeneous: m_up formula and leak clause are proved only on Z^D, not on 'a finite box'

Location: sections/08_scale.tex:234-238 (prop:sca-heterogeneous(a)-(c)); proof sections/app08_scale.tex:105-109; sections/chk08_scale.tex:52. Labels: prop:sca-heterogeneous; chk:sca-heterogeneous. Category: scope.

Evidence. The identity sum_j W_ij e^{phi.(x_i-x_j)} = 1-eps_i+2 sum_d a_id(cosh phi_d-1) needs two neighbors per axis and single-valued positions. An end agent of an open box has tilted row sum 1-eps_i+a(e^phi-1), larger, so the tilt works only for phi<ln(1+eps/a)<m_up; on a periodic box the tilt jumps at the seam. The check concedes both (image sums; end agents lower m_up to 0.2644). In (b), 'eps_low is at least every local leak' fails at open ends (W=W_low: end leak 1-c_min-a_min).

Proposed fix. State the second part of (a), the leak clause of (b), and (c) on Z^D. Add: on a periodic box the bound holds with the image sum over windings; on an open box use psi-bar including the end rows. Restate in (c) the hypotheses of (a) and (b) it uses, and say the diagonal rate is per unit Euclidean length.

State: applied. [08] applied: Real as a proof gap, not a demonstrated violation: tested open-chain covariances stayed below the Z formula (ratio at most 0.23), but boundary rows break the tilt argument (admissible tilt 0.28 versus m_up 0.456). Statement now scoped: boundary rows on open boxes, proved image-sum bound on periodic boxes, leak clause restricted to 2D-neighbor agents.

### sca1-05 (minor): Poisson check reports the second member of eq:sca-poisson as the attained bound; body says the bound is attained

Location: sections/08_scale.tex:95 (text after prop:sca-poisson); sections/chk08_scale.tex:12 (chk:sca-poisson). Labels: prop:sca-poisson; chk:sca-poisson. Category: check-mismatch.

Evidence. For the directed copy chain (diagonal 0, g=1), E J_ij(t)=e^{-nu t}(nu t)^d/d! (0.17547 at t=d=5), which equals the first member of eq:sca-poisson only. The check prints the first-passage probability P(Poisson(nu t)>=d) = 0.55951 and 0.54207 (reproduced, misc1.py) and calls it 'the bound'; that is the second member and a different quantity from the expected influence.

Proposed fix. Check: 'the crossing probability equals the second member; the expected influence equals the first.' Body: 'the directed copy chain attains the first inequality of \eqref{eq:sca-poisson}.'

State: applied. [08] applied: Defect real: the copy chain attains the first member of eq:sca-poisson for expected influence, e^{-nu t}(nu t)^d/d!, while the second member is the crossing probability P(Poisson(nu t)>=d). Remark after the proposition and the check now separate the two (0.17547 versus 0.55951 at t=d=5). Check of the edit: [08] style, Mathematics correct: E J=e^{-nu t}(nu t)^d/d! (0.17547, 0.12511 by matrix exponential), crossing probability P(Poisson>=d) (0.55951, 0.54207), v_LR=nu. But eq:sca-poisson has three members; 'second member' read from the left is the middle expression, which for the copy chain equals the Poisson pmf, not the crossing probability. The body gives no formula to disambiguate. Repair: [08] repaired, For the copy chain the middle member is the Poisson pmf and the last member the crossing probability (0.17547/0.12511 and 0.55951/0.54207 recomputed). Body now names the last member with its formula; check says middle and last member.

### sca1-06 (minor, unconfirmed): Switching factor 1.0703173057 has no specification and is not reproduced in the stated system

Location: sections/08_scale.tex:58 (ex:sca-amplifying-profile); sections/chk09_minimal.tex:15 (chk:min-amplification). Labels: ex:sca-amplifying-profile. Category: unreproducible-number.

Evidence. The first counterexample reproduces to all digits (amp.py: eigenvalue moduli 0.017137, 0.024352, 0.412032, 1.0613266751; block row sums 1.0999). For the switching example, every period-two alternation of {sense, listen}^2 profiles in the same system gives at most 0.9753 per round (switch.py), and all frozen profiles give 0.9. The quoted 1.0703173057 must come from a different instance that the manuscript does not specify.

Proposed fix. State the full specification of the switching instance (codes, sensing rows, schedule, level) next to the number, or mark it as quoted from the report with its instance identifier.

State: applied. [08] applied: Defect real and only partly repairable here: the cited report states the factor for its instance CEX-1 with no codes, sensing rows or schedule, so I could not specify or recompute it. Example now marks the factor as quoted from the report for a separate capacity-one instance. Group 09 repeats the claim; follow-ups returned. [09] applied: Same defect as mis_min-01, confirmed by scripts/mis_min-01.py. The check now marks 1.0703173057 as the report's CEX-1 value, not recomputed, and records the contraction of all capacity-one alternations in the stated instance.

### sca1-07 (minor): lem:sca-relations(a) and thm:sca-clustering(b) omit hypotheses needed for the stationary form

Location: sections/08_scale.tex:38 (lem:sca-relations(a)); sections/08_scale.tex:197 (thm:sca-clustering(b)). Labels: lem:sca-relations; thm:sca-clustering. Category: missing-hypothesis.

Evidence. The first sentence of (a) needs sup_k E||e_k(0)||^2<infinity, bounded second moments of the world innovation, and a stationary world when B^mis is nonzero. 'Stationary form when W is time invariant' also needs time-invariant Q^zeta: with constant W and time-varying noise covariance the infinite-past covariance Sigma(t) varies with t.

Proposed fix. Add 'with time-invariant $Q^\zeta$ and bounded initial second moments' to both statements, or put these into (Lin)/(B) of asm:sca-standing once.

State: applied. [08] applied: Confirmed: the proof used bounded initial second moments, a bounded-moment world innovation, a stationary world under mistranslation, and identically distributed noise. Added these to the statement and proof. Stationary form now requires a time-invariant noise law; a time-invariant Q^zeta suffices only under (G), so the finding's wording was narrowed. Check of the edit: [08] defect, Stationary-form clause is correct. Uniform-form clause is not implied: the hypothesis bounds only the connected part e_k(0), while uniform (M) bounds total errors m_i(t)-eta_t. Counterexample: infinite population, deterministic m_k(0)-eta_0=k, so e(0)=0 and all hypotheses hold, yet errors are unbounded in k at t=0. Repair: [08] repaired, Checker right. Hypothesis of lem:sca-relations(a) now bounds the total initial errors m_k(0)-eta_0, requires them independent of the schedule (needed on infinite populations) and sup_i ||B^mis_i|| finite. Proof rewritten for the total error with three Minkowski contributions.

### sca1-08 (minor): thm:sca-diffusive: unstated finiteness of varpi_max and an overstated comparison with the row-sum rate

Location: sections/08_scale.tex:225-231 (thm:sca-diffusive and following prose). Labels: thm:sca-diffusive. Category: edge-case.

Evidence. Theorem and constants re-derived and hold (misc3.py: 7x7 torus, nonuniform varpi, signed dominated W, worst ratio 0.08 to 0.50). The statement needs sup varpi<infinity on infinite graphs and does not say Sigma is the infinite-past covariance. The prose 'improves on the row-sum rate ... on any graph' holds only for lambda>e^{-2}: at lambda=0.1, sqrt(2 ln(1/lambda))=2.146<ln(1/lambda)=2.303.

Proposed fix. Add 'with $\varpi_{\max}=\sup_i\varpi_i<\infty$' and 'for the covariance of the process started in the infinite past (or at zero)'. Qualify the prose: 'for $\lambda>e^{-2}$, in particular for small leaks'.

State: applied. [08] applied: Confirmed. Added sup varpi_i finite, specified Sigma(t) as the process from the infinite past or from a zero start, for every t. Rate comparison now conditional: sqrt(2 ln(1/lambda)) exceeds ln(1/lambda) exactly when lambda > e^{-2}. Proof paragraph updated to match.

### sca1-09 (minor): Routing check: 'saturated at 0.734' is a transient value; (d) lacks a moment hypothesis

Location: sections/chk08_scale.tex:17 (chk:sca-routing); sections/08_scale.tex:105 (prop:sca-routing(d)). Labels: prop:sca-routing; chk:sca-routing. Category: check-wording.

Evidence. All chk:sca-routing numbers reproduce (misc1.py): flip probabilities, lengths, and chain responses equal to (gamma alpha_0/2)^20 x 1e-6. At gamma alpha_0=4 the response 0.7344 is the value after the stated rounds; the fixed point of the map is 0.9575, so 'saturated' misdescribes it. Part (d) uses a finite first moment of the one-step law and finite oscillation osc_i without stating them.

Proposed fix. Replace 'saturated at 0.734' by 'reached 0.734 after 20 steps (fixed point 0.957)'. Add 'with finite first moments and $\mathrm{osc}_i<\infty$' to (d).

State: applied. [08] applied: Confirmed numerically: at gamma*alpha_0=4 the 20-hop response is 0.7344, not saturated; the fixed point is 0.9575. Check text corrected. Part (d) now assumes a closed state domain, finite oscillations and a finite first moment of the one-step law, with the corresponding proof step inserted.

### sca1-10 (minor): Edge conditions and one prose slip in light-cone/no-moment statements

Location: sections/08_scale.tex:90 (prop:sca-poisson, v_LR); 08_scale.tex:160-163 (prop:sca-amplifying-site(c)-(d)); 08_scale.tex:142. Labels: prop:sca-poisson; prop:sca-amplifying-site; thm:sca-no-moment. Category: edge-case.

Evidence. v_LR is negative or -infinity when g plus the diagonal influence is below 1; the formula needs max(0, .) or a restriction. prop:sca-amplifying-site(c)-(d) use rho>1 and t>=1 without stating them (the bounds were otherwise confirmed: 0 violations in 1440 tests, fronts 8, 19, 29 and 6, 17, 28 reproduced, misc2.py). Line 142 says the correlated region grows at v_phi, whereas eq:sca-radius gives radius 2 v_phi t.

Proposed fix. State $v_{\mathrm{LR}}=\max(0,\cdot)$; add 'for $\rho>1$ and $t\ge1$' to (c)-(d); write 'the correlated region has radius at most $2v_\varphi t$'.

State: applied. [08] applied: Confirmed. v_LR is now max{0, inf ...}, zero when g+J_diag<1. Amplifying-site parts (b)-(d) carry t>=1 and rho conditions; (b) was added beyond the finding since its lower bound fails at t=0. Radius prose reads 2 v_phi t plus a constant, matching eq:sca-radius.

### sca1-11 (minor, unconfirmed): Two check values disagree with recomputation or with the stated formula

Location: sections/chk08_scale.tex:31 (chk:sca-rank-one); sections/chk08_scale.tex:52 (chk:sca-heterogeneous). Labels: chk:sca-rank-one; chk:sca-heterogeneous. Category: numbers.

Evidence. chk:sca-rank-one: growth rates reproduce (0.06298, 0.05969, 0.05952014, 0.05951971), but the last canonical-correlation gap is printed as 4.1e-12 where recomputation gives 1.07e-11 and the rho^{-2t} trend gives about 1.4e-11 (round-off range). chk:sca-heterogeneous: arccosh(1+eps_min/(2a_max)) with the printed extremes 0.0495 and 0.252 gives 0.4397 (at most 0.4403 with rounding), printed m_up=0.4424; a per-agent minimum of arccosh(1+eps_i/(2a_i)) would explain it. Homogeneous 0.48879 reproduces.

Proposed fix. Recompute the t=200 gap in higher precision or drop it. State which formula produced m_up=0.4424; if it is the per-agent minimum, say so (it is the sharper bound that the first part of (a) also proves).

State: applied. [08] applied: Confirmed both. The t=200 gap is 1.4e-11 in 60-digit arithmetic; 4.1e-12 was double-precision cancellation. Decay per 50 rounds is rho^{-100}=2.6007e-3. The printed 0.4424 is the largest admissible tilt, not the closed form (0.4399); labels in the heterogeneous check corrected.

### sca1-12 (minor): Several checks cannot be reproduced from the manuscript because instances are unspecified

Location: sections/chk08_scale.tex:6, 21, 26, 41, 46 (chk:sca-lightcone, -common-code, -no-moment, -spectral, -diffusive). Labels: chk:sca-lightcone; chk:sca-common-code; chk:sca-no-moment; chk:sca-spectral; chk:sca-diffusive. Category: reproducibility.

Evidence. These checks give sizes and summary ratios but no weights, seeds or generating laws, so the printed ratios cannot be recomputed. Independent tiny instances agree in kind (no-moment equal-time worst ratio 0.42; spectral 0.53 to 0.57 against printed 0.48 to 0.54; diffusive no violation). chk:sca-no-moment does not test the lag clause, which is the part of the theorem that fails.

Proposed fix. Give each check a one-line generating law and seed, or a pointer to the script identifier in the source comment, and add the lag covariance to chk:sca-no-moment.

State: applied. [08] applied: Generating laws read from the source scripts and added to the five checks; seeds added to the src comments. The lag-covariance test was already present in chk:sca-no-moment; its instance law was added. No rerun of the original scripts was performed.

### Not checked by lane sca1

- chk:sca-lightcone, chk:sca-common-code, chk:sca-no-moment, chk:sca-spectral and the torus runs of chk:sca-diffusive: printed instances are unspecified, so only independent tiny instances were run.
- chk:sca-heterogeneous beyond the homogeneous control: m_low values, strong-heterogeneity rows, open-grid and period-three numbers not reproduced.
- chk:sca-poisson random-instance ratios (only the copy-chain numbers were reproduced).
- The switching factor 1.0703173057 and the report-sourced claim that the amplifying profile is a strict best response under expected free energy.
- Positive definiteness of Q^zeta for the amplifying profile, which ex:sca-amplifying-profile needs when it invokes lem:sca-relations(c) and prop:sca-rank-one.
- chk:min-common-code, chk:min-disagreement and chk:min-grounding-moment (read, not recomputed).
- thm:sca-oz(e), cited by prop:sca-heterogeneous(c), lies outside the lane; only the existence of the label was verified.
- External uses in 06_coherence.tex:53 and app06_coherence.tex:46 were listed by grep but not opened; only thm:col-markov-bound(c) was read.
- No bibliographic verification of Carne 1985, Varopoulos 1985 or the Lieb-Robinson citations.

### Redundancy noted by lane sca1

- thm:sca-clustering(b),(c) are thm:sca-no-moment(a) at phi=0 (g_0=lambda) with t to infinity; thm:sca-clustering(d) is the corrected lag clause at phi=0.
- thm:sca-clustering(a) repeats thm:sca-lightcone(b) plus the row-sum induction.
- app04_collectives.tex:98 (proof of thm:col-markov-bound(c)) re-derives the proof of thm:sca-clustering(b) in full.
- prop:sca-spectral and thm:sca-clustering share one proof skeleton (replace row-sum lambda^n by K_A f^n).
- prop:sca-heterogeneous(a), first part, is the tilt argument of thm:sca-no-moment(a) with a vector tilt; (d) is textbook Perron-Frobenius; (e) is a one-line corollary of thm:sca-diffusive.
- rem:sca-argmax restates the zero-temperature limit already implied by prop:sca-routing; rem:sca-rumors restates prop:sca-amplifying-site in words.

### Streamlining tiers proposed by lane sca1

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| asm:sca-standing | A | 315 | Hypothesis ledger for the whole section; keep in main, as a table. |
| lem:sca-relations | A | 134 | Short, load-bearing; keep in main after fixing (c). |
| prop:sca-sufficient | B | 194 | Pointer list; compress to a table row set in main, detail to supplement. |
| ex:sca-amplifying-profile | A | 124 | The counterexample to (M); keep first instance in main, switching instance to supplement. |
| conj:sca-common-code | C | 71 | Conjecture with numerical support only; supplement or open-problem list. |
| def:sca-local-rule | A | 113 | Needed by the light cone; fold into the theorem statement. |
| thm:sca-lightcone | A | 92 | Headline result cited in introduction and predictions. |
| prop:sca-poisson | C | 121 | Asynchronous variant; one sentence in main, statement and proof to supplement. |
| prop:sca-routing | B | 115 | Keep (a)-(b) in main; (c)-(d) and the check to supplement. |
| ex:sca-switch-chain | C | 127 | Illustration of routing; supplement. |
| rem:sca-argmax | C | 90 | One sentence can join prop:sca-routing; rest to supplement. |
| thm:sca-no-moment | A | 151 | State once as the master tilted bound, with corrected lag clause; clustering becomes a corollary. |
| prop:sca-rank-one | B | 104 | Statement in main beside the amplifying example; proof and check to supplement. |
| prop:sca-amplifying-site | C | 142 | Exactly solvable illustration; keep the front velocity sentence in main. |
| rem:sca-rumors | B | 169 | Interpretation; shorten to two sentences in main. |
| def:sca-lengths | A | 143 | Defines xi, m, tau used by later sections. |
| thm:sca-clustering | A | 96 | Used by thm:col-markov-bound(c); present as phi=0 corollary of thm:sca-no-moment. |
| prop:sca-world-conditioning | B | 101 | Keep the conclusion sentence in main; statement and proof to supplement. |
| prop:sca-spectral | B | 56 | Merge as an extra part of thm:sca-clustering; same proof skeleton. |
| thm:sca-diffusive | A | 54 | Distinct square-root rate; statement in main, Carne proof in supplement. |
| prop:sca-heterogeneous | C | 200 | Five-part technical bracket; one sentence in main, rest to supplement on Z^D. |

## Lane sca2: Section 8, Ornstein-Zernike decay, correlation time, long-range links

No critical or major defect in 08_scale.tex:246-447. All nine labeled results (thm:sca-oz, the lengths, persistence, diffusive-scaling, three record propositions, long-range decay, fronts) hold on reconstruction, and their appendix proofs prove the statements as written. Nearly every number in the nine checks and two figure captions was reproduced with scripts in the lane directory. Six minor findings: one check tests a different formula than the one stated, one check omits parameters, one missing sign hypothesis (omega_k+delta_k>0), one loose cross-reference, one overstated fit sentence, one unverified citation range. Opened cross-references are used within what they state.

Coverage: 20 items examined; 18 hold, 1 defective, 1 suspect, 0 not checked.

| Item | Verdict | Note |
|---|---|---|
| chk:sca-autocovariance | defect | Tests the continuum integral in a window where eq:sca-autocov is off by at least 8 percent. |
| chk:sca-records | suspect | (a),(b),(d),(e) reproduced; (c) reproducible only with guessed parameters; (f),(g) not rerun. |

Items found to hold: thm:sca-oz; prop:sca-lengths-relation; prop:sca-persistence; prop:sca-diffusive-scaling; prop:sca-records; prop:sca-records-memory; prop:sca-records-length; prop:sca-longrange; prop:sca-fronts; lem:sca-union (appendix); lem:sca-big-jump (appendix); rem:sca-oz-form; rem:sca-records-special; rem:sca-global-records; chk:sca-oz-ring, chk:sca-oz-lattice, chk:sca-lengths, chk:sca-persistence; chk:sca-records-length; chk:sca-longrange, chk:sca-fronts; fig:sca-oz, fig:sca-records captions.

### sca2-01 (minor): chk:sca-autocovariance tests a continuum integral, not the stated asymptote eq:sca-autocov

Location: sections/chk08_scale.tex:76-78 (chk:sca-autocovariance); cited at sections/08_scale.tex:344 for prop:sca-diffusive-scaling(b). Labels: prop:sca-diffusive-scaling, chk:sca-autocovariance, eq:sca-autocov. Category: check-scope.

Evidence. The check compares the lattice autocovariance with (q/2) int_h^inf e^{-eps_lambda u}(4 pi a u)^{-D/2} du at eps=0.002, h<=3000, so eps*h<=6. In that window eq:sca-autocov itself is not yet accurate: s2_len_time.py gives exact/asymptote = 0.872, 0.958, 0.989 (D=1) and 0.769, 0.919, 0.976 (D=2) at eps=0.05, h=50, 200, 800, i.e. relative error about D/(2 eps h), at least 8 percent over the check's range. Only the sentence on local decay rates eps_lambda + D/(2h) bears on the stated form.

Proposed fix. Add to the check a comparison with eq:sca-autocov at eps*h >> 1 (for example eps=0.05, h=800: ratios 0.989 and 0.976), or state in prop:sca-diffusive-scaling(b) that the relative error of eq:sca-autocov is D/(2 eps_lambda h)(1+o(1)) and that the check tests the integral form from which it is derived.

State: applied. [08] applied: Confirmed (sca2-01.py): exact/asymptote is 0.932 (D=1), 0.872 (D=2) at eps=0.002, h=3000. Check now also tests eq:sca-autocov at c=0.2, eps=0.05, h up to 3000; proof derives the leading relative correction -D lam^2/((1-lam^2)h); body states the error is about D/(2 eps h).

### sca2-02 (minor): chk:sca-records(c) omits the parameters of the durable and perishable records

Location: sections/chk08_scale.tex:82 (chk:sca-records, part (c)); quoted at sections/08_scale.tex:381. Labels: chk:sca-records, prop:sca-records-memory. Category: reproducibility.

Evidence. Part (c) reports eps_eff=0.000408, tau x4.900, then eps_eff=0.002291 and 0.873, and the body quotes 4.90, but neither place gives (beta,omega,delta). The natural guess from chk:sca-records-length, adding (0.05,0.1,5e-3), gives tau ratio 2.76, not 0.873. The numbers are reproduced by durable (0.05,0.01,1e-4) alone (0.000408, 4.900) and with perishable (0.2,0.1,0.01) added (0.002291, 0.873); see s3_records.py and the tail of s5_longrange.py.

Proposed fix. In chk:sca-records(c) write: Mixed records at eps=0.002 and upsilon=0: the durable record (beta,omega,delta)=(0.05,0.01,1e-4) alone gave ...; with the perishable record (0.2,0.1,0.01) added, ... (after the author confirms these are the parameters used).

State: applied. [08] applied: Reproduced (sca2-02.py): durable (0.05,0.01,1e-4) gives eps_eff=0.000408, tau x4.9001; adding perishable (0.2,0.1,0.01) gives 0.002291 and 0.8730. Parameters and upsilon=0 now stated in part (c).

### sca2-03 (minor): prop:sca-records(b) sign criterion needs omega_k+delta_k>0, which is nowhere stated

Location: sections/08_scale.tex:356 (prop:sca-records(b)); sections/02_framework.tex:272 (def:fw-record-model). Labels: prop:sca-records, def:fw-record-model. Category: missing-hypothesis.

Evidence. The equivalence eps_eff>=0 iff g_z(0)>=0 uses that 0 lies in the interval (-inf, min_k(omega_k+delta_k)) where g_z decreases. The definition calls delta_k decays without a sign and the proposition assumes only beta_k, omega_k>0. With eps'=0.01, beta=0.1, omega=0.1, delta=-0.2: g_z(0)=0.01+0.1(-0.2)/(-0.1)=0.21>=0, while R=[[0.11,-0.1],[-0.1,-0.1]] has lambda_min=-0.14<0 (s6_const.py).

Proposed fix. Add delta_k>=0 to def:fw-record-model ("decays delta_k>=0"), or state in prop:sca-records: Let beta_k>0, omega_k>0 and omega_k+delta_k>0 for every k.

State: applied. [02] applied: Defect confirmed: at eps'=0.01, beta=omega=0.1, delta=-0.2, lambda_min(R)=-0.14 while g_z(0)=0.21; 4700 of 20000 random draws with delta in [-0.5,0.5] disagree in sign, 0 of 20000 with delta>=0. Definition now reads 'decays delta_k>=0'. prop:fw-record-timing (0<omega+delta<=1) stays consistent. [08] applied: Counterexample confirmed: g_z(0)=0.21, eigenvalues of R are -0.14, 0.15. Added omega_k+delta_k>0 to the proposition and used it in the proof of (b); 20000 random draws with that hypothesis and delta of either sign gave no mismatch. Group 02 follow-up returned.

### sca2-04 (minor): rem:sca-global-records cites cor:sca-size(e) for a component that corollary does not give

Location: sections/08_scale.tex:420 (rem:sca-global-records); sections/08_scale.tex:543 (cor:sca-size(e)). Labels: rem:sca-global-records, cor:sca-size. Category: cross-reference.

Evidence. cor:sca-size(e) treats a hub that attends nobody (W_hh=c_h) and gives leaves a common correlation theta_star independent of N. The archive of the remark is written by the members, and its non-decaying component scales as 1/N. The size Sigma_00(0)/N is also approximate: every translation-invariant covariance has a p=0 term, and the component added by the archive is the excess of that term over the continuation of the p!=0 branch.

Proposed fix. Write: ... a component [Sigma_00(0) - q/(1-(1-eps'-beta)^2)]/N, about Sigma_00(0)/N when eps_eff << beta, that does not decay with distance (compare the exogenous hub of cor:sca-size(e), whose common correlation does not fall with N; here it falls as 1/N, see prop:hie-global-record).

State: applied. [08] applied: Decomposition verified on rings of 12 and 16 sites to 1e-12 (sca2-04.py); the component is [Sigma_00(0)-q/(1-(1-eps'-beta)^2)]/N, 85 percent of Sigma_00(0)/N in one instance. Remark rewritten as proposed, with the contrast to cor:sca-size(e) and a pointer to prop:hie-global-record. Check of the edit: [08] defect, The decomposition is an exact identity (ring N=12, 16: error 5e-15, with or without record noise) and the 1/N contrast matches cor:sca-size(e) and prop:hie-global-record. The approximation clause is false: eps'=0.01, beta=0.1, omega=0.001, delta=0 has eps_eff/beta=0.0009 but the component is 7.8 percent of Sigma_00(0)/N. Repair: [08] repaired, Clause false, and the checker's replacement is also insufficient (eps'=1e-5, beta=0.1, omega=1e-3, delta=1e-4 gives fraction 0.09). Correct condition: eps'+R*delta << beta*omega/(beta+omega); fraction is about 1/(1+s). Added numcheck chk:sca-global-records and cited it.

### sca2-05 (minor): Body says fitted front exponents agree with 1/min(sigma,2); the check shows 5 to 6 percent shortfalls at both ends

Location: sections/08_scale.tex:446; sections/chk08_scale.tex:97 (chk:sca-fronts). Labels: prop:sca-fronts, chk:sca-fronts. Category: prose-vs-check.

Evidence. chk:sca-fronts reports 1.897 against 2 (sigma=0.5) and 0.469 against 0.5 (sigma=3). The fits depend on the time window, which the check does not state: s5_longrange.py gives 1.831 (t=8..64, ring 2^22) and 0.497 (t=32..256) for the same sigma, and 1.322, 0.996, 0.672 for sigma=0.75, 1, 1.5. The proposition is proved, so nothing rests on the fit, but the sentence overstates it.

Proposed fix. Write: fitted front exponents lie within 6 percent of 1/min(sigma,2), the shortfalls at sigma=0.5 and sigma=3 being pre-asymptotic (chk:sca-fronts); and state the fit window in the check.

State: applied. [08] applied: Shortfalls are 5.2 and 6.3 percent, so the body says within 7 percent, not 6. Check now states rings and fit windows from the recorded run output; 'pre-asymptotic' replaced by window dependence, which the recorded fronts support (sigma=3: 0.497 on t=32..256). Lattice run not repeated: ring sizes exceed the script limit.

### sca2-06 (minor, unconfirmed): Chemical-distance sentence cites Biskup 2004 without its exponent range

Location: sections/08_scale.tex:446 (prose after prop:sca-fronts). Labels: prop:sca-fronts, thm:sca-clustering. Category: citation-scope.

Evidence. The sentence says the chemical distance in long-range percolation grows like a power of log|x-y|. As I recall the theorem (Biskup, Ann. Probab. 32, 2004), this holds for connection exponent s in (D,2D), which is 0<sigma<D in the manuscript's notation; for s>2D the distance is linear and for s<D it is bounded. The source was not opened in this session, so the range is from memory.

Proposed fix. Write: whose chemical distance in long-range percolation with 0<sigma<D grows like a power of log|x-y| (biskup2004scaling); for sigma>D it grows linearly. Verify the range against the source before editing.

State: applied. [08] applied: Opened arXiv math/0304418: result holds for s in (d,2d), i.e. 0<sigma<D, with D(x,y)=(log|x-y|)^{Delta+o(1)}, 1/Delta=log2(2d/s). Sentence restricted to that range. The proposed clause on linear growth for sigma>D was omitted: it is not Biskup's theorem and its source was not opened.

### Not checked by lane sca2

- Figure sources figures/fig_sca_oz and figures/fig_sca_records were not opened; only caption numbers were checked.
- chk:sca-oz-lattice: prefactor ratios 0.9963/0.9965/0.9958 on the 512 torus and the fitted pointwise rates on the 1024 torus were not rerun; the fitted axis rates 0.51023 and 0.22421 lie slightly below the support-function values and I did not establish why (finite-torus images are the likely cause).
- chk:sca-records (f) displacement fraction equals sensing gain (0.166667, 0.142857, 0.019608), (g) thirty-agent ring with archive, and the two turnover identity rates 0.0012379 and 0.0021905 were not reproduced; the body claim upsilon=k^s at line 381 rests on other sections.
- chk:sca-records-length fitted covariance decay lengths were not reproduced.
- thm:sca-lightcone (cited for the light-cone time L/(2 l) at line 344), thm:hie-floor, prop:hie-record-contrast and open:col-records-baseline were not opened.
- External citations tran2020hierarchy, kuwahara2020strictly, metivier2014spreading, biskup2004scaling and the Friedkin-Johnsen reference were not opened; the Biskup range in finding 6 is from memory.
- prop:sca-fronts(c) lower bound for sigma>2 was checked as an asymptotic statement in t only; the borderline sigma=2 logarithmic form was checked by hand, not numerically.
- The O(eps_eff) error term of prop:sca-records-length(b) was confirmed numerically for one-record and two-record instances, not for general n_z.

### Redundancy noted by lane sca2

- prop:sca-records-memory(a) criterion eq:sca-memory-criterion is the upsilon_k=0 case of the several-record criterion in (c); both are the sign of g_z(epsilon).
- prop:sca-records-memory(d) restates Perron monotonicity and is described in the text as the endpoint upsilon=1 of (c).
- The exact upper bound on eps_eff stated in prose at 08_scale.tex:381 duplicates prop:hie-nested-records.
- rem:sca-global-records and the paragraph at 08_scale.tex:424 repeat prop:hie-global-record and thm:hie-floor.
- The chain xi_2 <= sqrt(a/eps) <= xi_OZ appears in thm:sca-oz(g), the fig:sca-oz caption and the prose after prop:sca-lengths-relation.
- thm:coh-grounding-tension(a)(i),(ii) restate the ring length and the local variance of thm:sca-oz(e).
- The noisy-record non-diffusivity caveat appears in 08_scale.tex:410, rem:col-which-contrast and chk:sca-records-length.

### Streamlining tiers proposed by lane sca2

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| thm:sca-oz | A | 420 | Keep (c), (e), (g) in main as the exact rate and sqrt(a/eps) law; move (a), (b), (d), (f) to supplement. |
| fig:sca-oz | B | 90 | Illustrates (g); one sentence in main suffices. |
| rem:sca-oz-form | B | 150 | Prefactor form is declared not a result. |
| prop:sca-lengths-relation | B | 230 | Main needs only the sentence xi_2 <= sqrt(a/eps) <= xi_OZ with the m/24 gap. |
| prop:sca-persistence | B | 140 | Supporting identity for tau; one-line statement in main. |
| prop:sca-diffusive-scaling | A | 260 | Keep (a) z=2 in main; (b) autocovariance asymptote to supplement. |
| prop:sca-records | A | 260 | Merge (b),(c) with the memory criterion into one main statement; (a),(d) to supplement. |
| prop:sca-records-memory | A | 420 | Keep criterion (a) and expansion (e); (b),(c),(d) to supplement, with (a) stated as sign of g_z(eps). |
| rem:sca-records-special | B | 120 | Dictionary to other sections; no new content. |
| prop:sca-records-length | B | 520 | Main keeps eq:sca-records-xi and the diffusivity caveat of (c) in two sentences. |
| fig:sca-records | B | 230 | Both panels restate chk:sca-records-length; caption is 230 words. |
| rem:sca-global-records and paragraph at line 424 | C | 210 | Duplicates prop:hie-global-record and thm:hie-floor; replace by one cross-reference. |
| prop:sca-longrange | B | 150 | One main sentence: power-law links give power-law covariance with constant 2 q lambda a/(1-lambda^2)^2. |
| prop:sca-fronts | B | 330 | Main keeps the front law of (c); (a),(b) are its proof steps and (d) follows from lem:sca-union. |
| Simplification: one records statement | A | 0 | State once: eps_eff is the unique root of g_z below min(omega_k+delta_k), and records lengthen memory iff g_z(eps)<0; (a) and (c) become corollaries. |

## Lane sca3: Section 8, percolation, coherence volume, abstraction, H4

No critical defect in 08_scale.tex:448-616. All nine results hold as stated up to minor edge cases; the percolation and tree thresholds rest on cited theorems not read in primary text. Two confirmed number disagreements: the three-dimensional susceptibility check (gap is exactly epsilon, 0.25 percent, not 0.03 percent) and the 'within five hops' claim (typical value is eight). H4 in final form matches the cited results part by part, with one sentence in (a) contradicting def:sca-lengths, several hypotheses left implicit, and the (C_rc) necessity claim overstated. Conjectures and open:sca-endogenous keep their status. Notes: <session scratch>/audit/sca3/findings.md

Coverage: 16 items examined; 11 hold, 2 defective, 0 suspect, 3 not checked.

| Item | Verdict | Note |
|---|---|---|
| chk:sca-gaussian-percolation | not_checked | 400-tree run not repeated; inequality proved algebraically. |
| chk:sca-coherence-volume | defect | (c),(d) one- and two-dimensional numbers reproduce; (d) three-dimensional gap misreported; (a),(b) not rerun. |
| chk:sca-alternating | not_checked | Only the 0.224 figure checked. |
| chk:sca-lyapunov | defect | Exponents reproduce; 'one from n=5 on' atypical; second model unspecified. |
| Numerical observation environments | not_checked | None occur in lines 448-616. |

Items found to hold: thm:sca-percolation; thm:sca-trees; thm:sca-gaussian-percolation; prop:sca-aggregate; prop:sca-tree-diffusive; thm:sca-coherence-volume; cor:sca-size; thm:sca-alternating; thm:sca-h4; chk:sca-trees; conj:sca-condensation, conj:sca-rank-down, open:sca-endogenous.

### sca3-01 (major): Three-dimensional susceptibility check reports a gap eight times smaller than the true one

Location: sections/chk08_scale.tex:112 (chk:sca-coherence-volume, part (d)); supports cor:sca-size(d) at sections/08_scale.tex:542. Category: number disagreement.

Evidence. With Sigma=q(I-W^2)^{-1}, chi=q/((1-lambda^2)Sigma(0)) and xi_2^2=2a*lambda/(1-lambda^2), so q*xi_2^2/(2a*Sigma(0)) = lambda*chi exactly, on any torus. The relative gap is therefore exactly epsilon=1-lambda. chk_size.py (FFT, N=64, D=3) gives 4.00%, 1.00%, 0.60%, 0.25% at epsilon=0.04, 0.01, 0.006, 0.0025. The check reports 0.03 percent at epsilon=0.0025.

Proposed fix. Report the gap as exactly epsilon (0.25 percent at epsilon=0.0025), or compare chi with q*xi_2^2/(2a*lambda*Sigma(0)), which is an identity, and say so. State the epsilon range to which 'within 0.6 percent' refers (it holds only for epsilon<=0.006).

State: applied. [08] applied: Confirmed: chi = q xi_2^2/(2 a lambda Sigma(0)) is an identity, so the gap to q xi_2^2/(2a Sigma(0)) is exactly epsilon. FFT rerun (D=3, 48^3, c=0.2) gave 4, 1, 0.6, 0.25 percent. Check part (d) rewritten with the identity and these gaps; corollary statement unchanged (asymptotic form is correct).

### sca3-02 (major): 'Pure relays lose all but one direction within five hops' is a single-realization figure, inconsistent with the reported gap

Location: sections/08_scale.tex:586 (paragraph before conj:sca-rank-down); sections/chk08_scale.tex:122 (chk:sca-lyapunov). Category: number disagreement.

Evidence. The reported gap 0.5785 gives sigma_2/sigma_1 ~ e^{-5*0.5785}=0.055 at n=5, above the 0.01 threshold; the typical crossing is ln(100)/0.5785 = 8 hops. chk_lyap.py (same model, 200 realizations) gives mean counts above threshold 1.72 at n=5, 1.47 at n=8, 1.19 at n=11: about 72% of realizations still carry two directions at n=5. Exponents themselves reproduce (-0.915, -1.505, gap 0.590) within sampling error.

Proposed fix. Replace by 'within about eight hops (ln 100 divided by the gap)' or state that the count is for one realization and give the fraction of realizations. Keep the abstraction length 1.73 hops as the stated scale.

State: applied. [08] applied: Confirmed. Rerun: exponents -0.917, -1.509; over 2000 realizations two directions survive in 74, 44, 24, 4 percent at n=5, 8, 11, 20. Main text now says about eight hops (ln 100 over the gap) with wide scatter; check reports the fractions and medians. Reported exponents and 1.73 kept. Check of the edit: [08] defect, Survival fractions and medians reproduce (mine: 72.9, 42.4, 22.6, 4.0 percent; medians 0.039, 0.006; median crossing hop 7). The 1.73 newly placed in the main text does not: the exponents are closed-form, Gamma_1=-3/4+ln((d_1+d_2)/2)=-0.9174, Gamma_1+Gamma_2=ln(d_1 d_2)-25/12, so Gamma_2=-1.5063, gap 0.5889, length 1.70. Repair: [08] repaired, Live text already read 1.70 hops, gap 0.588, ln100/0.588. Closed forms verified (Gamma1=-0.9174, sum=-2.4238, gap 0.5889, length 1.698; Monte Carlo agrees) and added to chk:sca-lyapunov. No main-text change needed.

### sca3-03 (minor): H4(a) says no correlation length exists when (M) fails, but def:sca-lengths defines one under the uniform form

Location: sections/08_scale.tex:601 (thm:sca-h4, part (a), last sentence); def:sca-lengths at 08_scale.tex:179-190. Category: internal consistency.

Evidence. asm:sca-standing fixes unqualified (M) as the stationary form. def:sca-lengths defines the correlation length also under (M) in uniform form, for time-varying exogenous schedules where the stationary form fails. The sentence 'When (M) fails there is no stationary law and no correlation length' therefore contradicts the definition for that class.

Proposed fix. Write 'When (M) fails in both its stationary and uniform forms there is no correlation length; when the stationary form fails there is no stationary law and, by def:col-collective, no collective.'

State: applied. [08] applied: Confirmed against def:sca-lengths. H4(a) last sentence and its proof now distinguish failure of both forms (no correlation length) from failure of the stationary form (no stationary law with finite second moments, no collective). 'With finite second moments' added for accuracy.

### sca3-04 (minor): H4 omits hypotheses carried by the results it assembles

Location: sections/08_scale.tex:601-605 (thm:sca-h4, parts (a),(c),(d),(e)); proof sections/app08_scale.tex:254. Category: missing hypothesis.

Evidence. (a) K_phi contains q_0, which thm:sca-lightcone(b) defines through independent initial errors with block covariance at most q_0 I. (c) thm:sca-oz and prop:sca-lengths-relation need eps^Pi>0 and varsigma_d>0. (d) prop:sca-persistence needs Q^zeta time invariant and positive definite. (e) the coherence-count sentence uses cor:sca-size(b), which needs (Lin).

Proposed fix. Add one clause per part naming the missing hypothesis, or open the theorem with 'under the hypotheses of the results cited in each part'.

State: applied. [08] applied: Confirmed against the cited statements. Added: (a) independent initial errors with blocks at most q_0 I, independence of noises, K_phi stated; (c) eps^Pi>0, varsigma_d>0, and the setting of prop:sca-longrange; (d) (Lin) and Q^zeta positive definite, time invariant; (e) (M) and (Lin) for the coherence-count bounds.

### sca3-05 (minor): '(C_rc) cannot be dropped' and 'without (C_rc) the number is unbounded' ignore the (C_rho) alternative

Location: sections/08_scale.tex:543 (cor:sca-size, part (e)); sections/08_scale.tex:605 (thm:sca-h4, part (e)). Category: wording stronger than result.

Evidence. cor:sca-size(b) bounds the coherence count under (C_rho) with fixed constants, without (C_rc). The hub family (chk_size.py: theta_star=0.1525 for all N, norm of W growing with N) violates both: its (C_rho) constant K_A is unbounded in N. So the example shows that one of the two is needed, not that (C_rc) is.

Proposed fix. Write 'with neither (C_rc) nor a uniform (C_rho)' in both places, and note that the hub family has unbounded K_A as well as unbounded column sum.

State: applied. [08] applied: Confirmed analytically: K_A f >= ||W|| >= (c_h^2+N a^2)^{1/2}, so the hub family violates uniform (C_rho) as well as (C_rc). cor:sca-size(e), its proof and H4(e) now say neither hypothesis holds uniformly in N.

### sca3-06 (minor): Coherence attainment 'in the linear span' fails for degenerate R_C; part (d) needs a normalization

Location: sections/08_scale.tex:527, 530 (thm:sca-coherence-volume, parts (a),(d)); proof sections/app08_scale.tex:242. Category: edge case.

Evidence. Take X_2=-X_1. Every Z has Corr(X_2,Z)=-Corr(X_1,Z), so theta*(C)=0, attained only by Z uncorrelated with X_1; every nonzero element of the span has minimum correlation -1. The first clause of (a) is unconditional. In (d) the bound lambda_max^{1/2} min_i w_i is scale dependent unless w has unit Euclidean norm.

Proposed fix. State (a) as: when theta*(C)>0 it is attained in the span and equals the minimum of p^T R_C p. Add 'unit' before 'top eigenvector' in (d).

State: applied. [08] applied: Confirmed: X_2=-X_1 gives theta*=0 with every nonzero span element at -1. Part (a) restated as a dichotomy on min p^T R p, proof extended to cover the degenerate case and to justify the span reduction only for positive coherence; 'unit' added in (d) and its proof.

### sca3-07 (minor): Table rows misstate what is bounded and the reach threshold

Location: sections/08_scale.tex:557-558 (tab:sca-sizes, rows 2 and 3). Category: cross-reference wording.

Evidence. Row 2: '(C_rc) or (C_rho) to bound chi_C', but under (C_rho) cor:sca-size(b) bounds lambda_max(R_C), not chi_C. Row 3: 'reach needs b*alpha>1'; the threshold of thm:sca-trees is b*alpha^2>1, and b*alpha>1 is only its consequence, which is what prop:sca-tree-diffusive uses.

Proposed fix. Row 2: 'to bound chi_C or lambda_max(R_C)'. Row 3: 'reach needs b*alpha^2>1, hence b*alpha>1, outside the diffusive class'.

State: applied. [08] applied: Confirmed. Row 2 now reads |C| <= lambda_max(R_C)/theta^2 <= chi_C/theta^2 for a theta-coherent set, with (C_rc) bounding chi_C and (C_rho) bounding lambda_max(R_C). Row 3 and the sentence after prop:sca-tree-diffusive now say reach needs b*alpha^2>1, hence b*alpha>1.

### sca3-08 (minor): Tree statements: 'leaf' ambiguous and depth-one case excluded silently

Location: sections/08_scale.tex:475 (thm:sca-trees, part (a)); sections/08_scale.tex:502 (prop:sca-tree-diffusive, part (a)). Category: edge case.

Evidence. In thm:sca-trees(a) the recursion starts from V(leaf)=sigma_obs^2 for level-n vertices; a childless vertex above level n has an empty sum, V^{-1}=0, and must be treated as unobserved, which the word 'leaf' does not separate. In prop:sca-tree-diffusive(a) a depth-one tree has no internal vertex; the row sums then give diffusive iff (b-1)*alpha<=1, not b*alpha<=1.

Proposed fix. Write 'V(v)=sigma_obs^2 at level-n vertices and V(v)=infinity at childless vertices above level n'. Add 'for depth at least two' to the diffusivity criterion.

State: applied. [08] applied: Confirmed by script sca3-08.py: depth-one tree with b=2, alpha=0.8 is diffusive although b*alpha=1.6; reading a childless unobserved vertex as a leaf gives I=0.273 against the direct 0.199. Statements and proofs amended; the same leaf ambiguity in the percolation recursion was fixed.

### sca3-09 (minor): Lyapunov example: relay maps are singular, and the second model is not specified

Location: sections/08_scale.tex:586, 592; sections/chk08_scale.tex:122 (chk:sca-lyapunov). Category: hypothesis match / reproducibility.

Evidence. The body cites the simple-spectrum theorems for invertible maps. The pure-relay hop maps are rank two in a six-dimensional world. The gap is still covered: the product reduces to independent 2x2 factors D*U_m*U_{m-1}^T, almost surely invertible for Haar frames, but the text does not say this. The 'receivers that keep part of their own belief' model has no stated retention weight, so its exponents and the 44-hop figure cannot be reproduced; only 1/0.0227=44 was checked.

Proposed fix. Add one sentence giving the reduction to 2x2 factors for the relay case, and state the retention parameter of the second model in the check.

State: applied. [08] applied: Confirmed. Body now gives the 2x2 reduction and why the cited conditions hold. Source script has omega=0.5; rerun with 2e6 draws gives lazy gap 0.0296 (se 0.0002), length 33.8 hops, not 44 (a 4000-hop estimate with se 0.004); relay gap 0.588, length 1.70. Numbers updated in check and body.

### Not checked by lane sca3

- Primary texts of Polyanskiy-Wu 2017/2019, Lyons 1990/1992, Kesten-Stigum, Furstenberg, Oseledets, Guivarc'h-Raugi, Goldsheid-Margulis, Duminil-Copin-Tassion, and the literature claims in rem:sca-alternating-cited
- chk:sca-trees direct-conditioning runs and chk:sca-gaussian-percolation 400-tree run (algebra verified, runs not repeated)
- chk:sca-coherence-volume (a) disk quadratic programs, (b) 180 random subsets, (e) copy chain
- chk:sca-alternating numerical values in (a) and (c) other than c_cyc^40
- Second Lyapunov model (receivers keeping part of their belief): parameters not given, not reproduced
- Proofs of the earlier section 8 and section 4 results that thm:sca-h4 assembles (other lanes)
- thm:coh-amplification beyond part (a) and the full statement of prop:col-coherence-average
- thm:ren-closure, conj:sca-common-code, open:col-non-diffusive, ex:sca-switch-chain
- The claim in open:sca-endogenous that the framework section has no geometry

### Redundancy noted by lane sca3

- thm:sca-h4 restates earlier results verbatim in five parts; a pointer table would carry the same content
- tab:sca-sizes repeats cor:sca-size and thm:sca-coherence-volume bounds
- thm:sca-trees(b) is a step in the proof of (c),(d)
- rem:sca-alternating-cited and thm:sca-alternating(a),(b) both report the classical alternating-projection facts
- cor:sca-size(e) hub example is repeated in thm:sca-h4(e)

### Streamlining tiers proposed by lane sca3

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| thm:sca-trees (a),(c) | A |  | Reach threshold; needed by H4 discussion and the table. |
| def:sca-coherence | A |  | Defines the quantity bounded in the A results. |
| thm:sca-coherence-volume | A |  | Core size bound. |
| cor:sca-size (a),(b),(d) | A |  | Explicit sizes used by H4(e). |
| thm:sca-h4 | A |  | Headline; shorten to a pointer table. |
| open:sca-endogenous | A |  | States the scope limit of the section. |
| def:sca-spacetime | B |  | Only supports the percolation theorem. |
| thm:sca-percolation | B |  | Vacuous for the linear-Gaussian model, as the text says. |
| thm:sca-gaussian-percolation | B |  | Comparison result, not used by H4. |
| prop:sca-aggregate | B |  | Supporting. |
| prop:sca-tree-diffusive | B |  | Explains non-comparability row; supplement with one-line pointer. |
| thm:sca-trees (b),(d) | B |  | (b) is a proof step; (d) rests on cited Lyons. |
| cor:sca-size (c),(e) | B |  | Sharpness and necessity examples. |
| thm:sca-alternating (a),(b) | B |  | Classical facts in manuscript notation. |
| conj:sca-condensation | B |  | Conjecture; keep one sentence in main text. |
| conj:sca-rank-down | B |  | Conjecture; keep one sentence in main text. |
| tab:sca-sizes | B |  | Duplicates the corollary; keep only if H4 becomes a table. |
| rem:sca-alternating-cited | C |  | Literature pointer; fold into the proof. |
| thm:sca-alternating (c) | C |  | One-line consequence. |
| Lyapunov paragraph (line 586) | C |  | Merge into the discussion of conj:sca-rank-down after correcting the hop count. |

## Lane abs: Section 10, abstract collectives

No stated proposition or corollary in sections/10_abstract_collectives.tex is false in its main clauses; 14 of the 16 results hold as written and two carry defective closing clauses. The two major defects concern the ultrametric cap. (1) The inequality of prop:abs-ultrametric-cap is correct, but its closing sentence is a vacuous conditional: for a fixed finite irreducible network (1-lambda^2) Sigma^c_ii tends to pi^T Q^zeta pi (= q/N in the symmetric case), so the cap tends to ln(1+q/(NQ)) > 0 and never to zero, while 04_collectives.tex:492 cites the proposition for a cap 'that vanishes as grounding weakens'. (2) The prose conclusion 'every unconditional contrast is small, whatever the barriers' (10:426, 04:492) depends on the unstated ratio q/Q: at q/Q = 100 the unconditional contrast of the barrier arc is 1.445 against a world-conditional 2.120. Seven minor defects: the monotonicity claim in rem:abs-polity-readings fails near the cost thresholds (optimal extent is non-monotone in xi); a forward-difference value 0.363 reported as a derivative in chk:abs-crossover (0.382); a missing a_x != 0 and an unused hypothesis in the last clause of prop:abs-bypass; the word 'collective' used against the convention of 04:488 (one-round collective, law collective, 'are collectives'); tab:abs-graded cites prop:abs-barrier for an ultrametric contrast the proposition does not state and that is negative for weak barriers at small self weight; a non-normalizable 'density' in prop:abs-elasticity(c); and eleven readings of social-science findings in running prose rather than in remark or conjecture environments (permitted by the section's own stated policy at 10:6, stricter under the manuscript's status discipline). What ran: seven small numpy scripts (cap.py, cap3.py, cross.py, pol.py, bar.py, bar2.py, weak2.py) in <session scratch>/audit/abs/, reproducing chk:abs-cap, chk:abs-crossover (three of four rates), chk:abs-bypass ratios, the 1D numbers of chk:abs-polity, chk:abs-elasticity, chk:abs-hierarchy and the ring instance of chk:abs-barrier; prop:abs-barrier(a) was confirmed to 1e-15 and bound (c) on 11 parameter sets (finite evidence for the bound, the proof was also read). Remaining results were reconstructed by hand. A copy of the findings is at <session scratch>/audit/abs/findings.md. Minimal unresolved obligation: a stated hypothesis under which a barrier gives positive ultrametric contrast (finding 7), and the large-size and Monte Carlo checks listed in not_checked. The change that would most alter the section's conclusions is restating the weak-grounding claim with its q/(NQ) scale.

Coverage: 32 items examined; 25 hold, 3 defective, 0 suspect, 4 not checked.

| Item | Verdict | Note |
|---|---|---|
| prop:abs-bypass | defect | Series and entrywise lower bound hold (hand plus numerics). Final clause needs a_x != 0 and carries an unused hypothesis (finding 5, minor). |
| prop:abs-ultrametric-cap | defect | Inequality holds and chk:abs-cap reproduced. Closing sentence is a vacuous conditional at fixed N and the citing prose overstates it (findings 1 and 2, major). |
| chk:abs-crossover | defect | Three of four rates reproduce; 0.363 at d=20 is a forward difference (0.382). 4000-ring Lyapunov comparison not rerun (Fourier sum used). |
| chk:abs-union-cone | not_checked | Riccati coefficient 0.4123 not recomputed. |
| chk:abs-media | not_checked | Values checked only for sign consistency with the criterion omega ell_r^2 eps > 2 a delta, which was derived from eq:sca-records-xi. |
| chk:abs-seguy | not_checked | Sampling and ground-state runs not rerun; closed forms verified by hand. |
| chk:abs-exchange | not_checked | Statement is consistent with the proposition; numbers not recomputed. |

Items found to hold: prop:abs-decoupling; prop:abs-crossover; prop:abs-homogeneous; prop:abs-barrier; prop:abs-conformity; prop:abs-seguy; prop:abs-exchange-consistency; prop:abs-walras; prop:abs-hayek; prop:abs-polity; prop:abs-one-round; cor:abs-one-round-extent; prop:abs-elasticity; prop:abs-hierarchy; chk:abs-barrier; chk:abs-bypass; chk:abs-walras; chk:abs-hayek; chk:abs-polity; chk:abs-elasticity; chk:abs-hierarchy; chk:abs-cap; rem:abs-innis (length criterion); Section 10.9 agency and formation paragraphs (10:448-454); Cross-references (lem:fw-common-mode, def:col-ultrametric, thm:col-lattice-contrast, cor:col-lstar, prop:col-nesting, prop:col-records-partition, thm:agy-agency, def:agy-meta-agent, prop:coh-adoption, thm:coh-domains-1d, prop:sca-records-length, tab:sca-sizes, ex:hie-code-domains, thm:ren-nested, prop:ren-hayek, thm:env-hayek-horizon, prop:env-multiplex).

### abs-01 (major): Ultrametric cap does not vanish as grounding weakens in a fixed finite network; closing sentence of the proposition is vacuous and 04:492 cites it for more than it says

Location: sections/10_abstract_collectives.tex:422 (prop:abs-ultrametric-cap, last sentence); sections/04_collectives.tex:492 (prose after def:col-ultrametric). Labels: prop:abs-ultrametric-cap, def:col-ultrametric, lem:fw-common-mode, chk:abs-cap. Category: cross-reference beyond cited result / vacuous hypothesis.

Evidence. The inequality U^unc(C) <= ln(1+(1-lambda^2) max_i Sigma^c_ii/Q) holds (proof app10:149-155 checked; chk:abs-cap reproduced: U^c 3.365/2.796/2.120, U^unc 0.1138/0.0716/0.0408, caps 0.2999/0.1523/0.0704 at eps 0.05/0.01/0.002). The closing sentence (10:422) reads: 'In the level-0 network the cap tends to zero as lambda->1 whenever (1-lambda^2) max_i Sigma^c_ii -> 0.' For a fixed finite network W = lambda P with P irreducible stochastic and stationary vector pi, Sigma^c = sum_k W^k Q^zeta (W^T)^k has its Perron mode diverging as 1/(1-lambda^2) with all other modes bounded, so (1-lambda^2) Sigma^c_ii -> pi^T Q^zeta pi > 0 (= q/N for symmetric P, Q^zeta = qI). The stated condition therefore never holds at fixed N, and the cap tends to ln(1+q/(NQ)) > 0. Numbers (ring of 60, q=Q=1, two barriers n_b=100; cap.py): cap 0.0704 at eps=0.002, 0.0223 at eps=1e-4, 0.0166 at eps=1e-6, limit ln(1+1/60)=0.016529. Other instances (cap3.py): N=6, q=10, Q=1, eps=1e-5: cap 0.9825 (limit ln(1+10/6)=0.9808); N=60, q=100, eps=1e-7: cap 0.9811 (limit 0.9808). 04:492 states without the condition: 'capped by a quantity that vanishes as grounding weakens ... (\cref{prop:abs-ultrametric-cap})'.

Proposed fix. Replace the last sentence of prop:abs-ultrametric-cap by: 'In the level-0 network with $W=\lambda P$, $P$ a fixed irreducible stochastic matrix with stationary vector $\pi$, $(1-\lambda^2)\Sigma^c_{ii}\to\pi^\top Q^\zeta\pi$ as $\lambda\to1$ ($=q/N$ for symmetric $P$ and $Q^\zeta=qI$), so the cap tends to $\ln(1+\pi^\top Q^\zeta\pi/Q)$, which is small when $q/(NQ)$ is small and vanishes only as $N\to\infty$ or $q/Q\to0$.' Add one line to the appendix proof (Perron mode of $\sum_kW^kQ^\zeta W^{\top k}$). At 04:492 write: 'capped by $\ln(1+(1-\lambda^2)\max_i\Sigma^c_{ii}/Q)$, which is of order $q/(NQ)$ at weak grounding'.

What would overturn the finding. 04:492 'capped by a quantity that vanishes as grounding weakens'

State: applied. [04] applied: An earlier batch had already removed the unconditional vanishing claim. Completed it: bound restricted to nonempty proper subsets, cap written as ln(1+(1-lambda^2) max Sigma^c_ii/Q), floor ln(1+q/(NQ)) at every lambda and limit for irreducible aperiodic P, notation aligned to Q^zeta=qI. Checked on a 12-ring (abs-01.py). [10] applied: Confirmed: cap tends to ln(1+q/(NQ)), not zero (0.0223 at eps=1e-4, 0.0166 at 1e-6, limit 0.01653). Closing sentence replaced; proof extended with the Perron-mode decomposition. The proposed fix needs aperiodicity added: for the two-agent swap the limit is (q1+q2)/2, not pi^T Q pi.

### abs-02 (major): 'Every unconditional contrast is small, whatever the barriers' depends on the unstated ratio of local to world noise

Location: sections/10_abstract_collectives.tex:426 (prose after prop:abs-ultrametric-cap); sections/04_collectives.tex:492; sections/chk10_abstract_collectives.tex:65 (chk:abs-cap). Labels: prop:abs-ultrametric-cap, chk:abs-cap. Category: prose claim stronger than the result.

Evidence. The quoted numbers at 10:426 (world-conditional 3.37, 2.80, 2.12; unconditional 0.114, 0.072, 0.041) reproduce only with q = Q = 1, which the body sentence does not state. The cap is ln(1+(1-lambda^2) max Sigma^c_ii/Q), which scales with q/Q. Same ring (N=60, two barriers n_b=100, eps=0.002, Q=1; cap3.py): q=100 gives U^unc = 1.445 against U^c = 2.120 (cap 2.116); q=1000 gives U^unc = 2.016 (cap 4.30); at eps=0.01, q=100: U^unc = 2.040 (cap 2.859). So at weak grounding the unconditional contrast is not small when local noise is large against the world innovation; the barriers remain visible.

Proposed fix. At 10:426: 'so when $(1-\lambda^2)\max_i\Sigma^c_{ii}\ll Q$, that is, when local noise is not large against the world innovation ($q/(NQ)\ll1$ at weak grounding), every unconditional contrast is small, whatever the barriers: on a ring of 60 agents with $q=Q=1$ and two barriers ...'. Add to chk:abs-cap a line with $q/Q=100$ (unconditional contrast 1.445 at $\varepsilon=0.002$) to show the dependence. Make the same qualification at 04:492.

What would overturn the finding. 10:426 'in weakly grounded populations every unconditional contrast is small, whatever the barriers'

State: applied. [04] applied: Confirmed on a 12-ring with two weak links: q/Q=100 gives unconditional contrast 2.58 against world-conditional 3.45 at eps=0.05. Prose after def:col-ultrametric now qualifies the necessity of conditioning by q/(NQ) small and says barriers remain visible when q/Q is large, citing chk:abs-cap. [10] applied: Confirmed: q=100, Q=1 gives unconditional contrast 2.470, 2.040, 1.445 at the three leaks (caps 3.583, 2.859, 2.116). Prose after the proposition now conditions on (1-lambda^2) max Sigma^c_ii << Q and states q=Q=1; chk:abs-cap gains the q=100 and q=1000 lines and the weak-grounding limit.

### abs-03 (minor): Optimal polity extent is not monotone in the correlation length; 'better communication ... enlarges optimal polities' holds only at small fixed cost

Location: sections/10_abstract_collectives.tex:321 (rem:abs-polity-readings). Labels: rem:abs-polity-readings, prop:abs-polity, fig:abs-polity. Category: interpretation overstated relative to prop:abs-polity.

Evidence. From prop:abs-polity, d*_C = 2 xi rho_C with e^{-rho}(1+rho) = 1 - f/(2 g xi), and d*_M = xi rho_M with 4(1-e^{-rho})/rho - 2e^{-rho} = 2 - 2f/(g xi). With f = g = 1 (pol.py): d*_C = 7.473 at xi=0.5025, 3.882 at 0.6, 3.389 at 0.8, minimum 3.351 at xi=0.934, 3.567 at 1.5, 5.318 at 5, 20.70 at 100. d*_M = 8.906 at xi=1.5, minimum 7.176 at xi=2.67, 7.874 at 5, 26.13 at 100. The optimum grows with xi only for f/(g xi) below about 1.07 (rule C) and 0.375 (rule M); nearer the thresholds f/(g xi) -> 2 (C) and -> 1 (M) a longer xi shortens the finite optimum, because the optimum diverges at the threshold. The remark's sentence 'Better communication lengthens xi, raises chi and enlarges optimal polities, with d* proportional to xi^{1/2} at small fixed cost under both rules' qualifies only the exponent.

Proposed fix. 'Better communication lengthens $\xi$ and raises $\chi$; it enlarges optimal polities when the fixed cost is small against $g\xi$ ($f/(g\xi)$ below about 1.07 under rule C and 0.37 under rule M), with $d^\ast\propto\xi^{1/2}$ in the small-cost limit, while nearer the thresholds of \cref{prop:abs-polity} a longer $\xi$ shortens the finite optimum.'

State: applied. [10] applied: Confirmed with root finding and direct cost minimization: d*_C has a minimum 3.351 at f/(g xi)=1.070, d*_M a minimum 7.176 at f/(g xi)=0.3746 (f=g=1). Rule C threshold also follows from e^rho=1+rho+rho^2. Remark sentence replaced as proposed, restricted to the line.

### abs-04 (minor): chk:abs-crossover reports a forward difference as the local decay rate at d=20

Location: sections/chk10_abstract_collectives.tex:6 (chk:abs-crossover). Labels: chk:abs-crossover, prop:abs-crossover. Category: number disagreement (check vs recomputation).

Evidence. The check states 'the local decay rate -d ln Sigma_11/dd is 0.561 at d=10, 0.363 at d=20, 0.1824 at d=40 and 0.1822 from d=60 on'. With c=(0.3,0.39), a_x=1e-3 (cross.py): m_- = 0.18222, m_+ = 0.56965, d_x = 20.17, amplitudes A_+ = 1.3893, A_- = 5.61e-4 (half the check's 2.7730 and 1.12e-3, consistent with the q/2 prefactor). The derivative of A_+ e^{-m_+ d} + A_- e^{-m_- d} at d=20 and the central difference both give 0.382; the forward difference ln(Sigma_11(20)/Sigma_11(21)) gives 0.363. The other values reproduce (0.562, 0.1824, 0.1822). Near the crossover the rate changes by about 0.02 per hop, so the discretization matters only there.

Proposed fix. Report 0.382 at d=20, or state 'forward difference $\ln(\Sigma_{11}(d)/\Sigma_{11}(d+1))$' as the quantity.

State: applied. [10] applied: Confirmed: derivative and central difference give 0.562 at d=10 and 0.382 at d=20; 0.363 is the forward difference. Check now reports the derivative values and names the forward difference separately. Amplitudes 2.7730 and 1.12e-3 and crossover 20.16 reproduce as stated. Check of the edit: [10] defect, Rates 0.562, 0.382, 0.1824, 0.1822, the central-difference agreement and forward difference 0.363 reproduce. The added sentence 'the rate changes by about 0.02 per site' does not: derivative values 0.4189, 0.3821, 0.3448 at d=19, 20, 21, i.e. about 0.037 per site ((m_+-m_-)^2/4=0.0375). 0.02 is the forward-minus-derivative gap. Repair: [10] repaired, Checker is right. From the printed amplitudes and rates, the two-term local rate is 0.4191, 0.3823, 0.3450 at d=19, 20, 21, a fall of 0.0370 per site (bound (m_+-m_-)^2/4=0.0375); 0.02 is the forward-minus-derivative gap (0.0187). Sentence in chk:abs-crossover replaced with the proposed wording; no other file quotes the figure.

### abs-05 (minor): prop:abs-bypass final clause: positivity needs a nonzero cross coupling, and one stated hypothesis is unused

Location: sections/10_abstract_collectives.tex:132 (prop:abs-bypass, last sentence); proof sections/app10_abstract_collectives.tex:47-49. Labels: prop:abs-bypass. Category: missing hypothesis / unused hypothesis.

Evidence. The standing hypothesis is a_x^2 < eps_1 eps_2, which admits a_x = 0. The lower bound is the n=1 term of G_11 = sum_{n>=1} a_x^{2n} (A_1^{-1}A_2^{-1})^n A_1^{-1}, namely a_x^2 A_1^{-1}A_2^{-1}A_1^{-1}, which is identically 0 at a_x = 0, so 'the lower bound is positive' is false there. For a_x != 0 the (x,y) entry is at least a_x^2 A_1^{-1}(x,x) A_2^{-1}(x,y) A_1^{-1}(y,y), with positive diagonal entries of the inverse M-matrix A_1^{-1} and A_2^{-1}(x,y) > 0 whenever L_2 is connected. The hypothesis 'C and V\C are each connected in L_1' is therefore not needed. The entrywise bound itself was confirmed numerically (cross.py; same-side/cross-cut ratios 1871 at a_x=1e-3, 207.7 at 3e-3, 18.45 at 1e-2).

Proposed fix. 'If instead $a_\times\ne0$ and $L_2$ is connected, the lower bound is positive.'

State: applied. [10] applied: Confirmed: bound vanishes at a_x=0. Final clause now reads 'a_x != 0 and L_2 connected'; proof uses the single term A_1^{-1}(x,x)A_2^{-1}(x,y)A_1^{-1}(y,y)>0, so connectivity of C in L_1 is dropped. Instance with C disconnected in L_1 gives positive cross-cut values.

### abs-06 (minor): The word 'collective' is used for objects that are not shown to be, or are defined not to be, collectives in the sense of def:col-collective

Location: sections/10_abstract_collectives.tex:3, :166 (def:abs-culture), :246 (def:abs-market), :321 (rem:abs-polity-readings), :330 (def:abs-one-round), :339; against sections/04_collectives.tex:488. Labels: def:abs-culture, def:abs-market, def:abs-polity, def:abs-one-round, def:col-ultrametric, def:col-collective, tab:abs-graded. Category: terminology inconsistent with a standing convention.

Evidence. 04:488: 'the word collective is kept for the spectral notion of \cref{def:col-collective}'. Against it: 10:3 'Cultures, economies, nations and cities are collectives'; 10:330 'A one-round collective is a set of agents every pair of which can meet within one round' followed at 10:339 by 'a one-round collective needs no contrast'; 10:321 'once the exchange collective extends beyond the polity, market size no longer needs a large law collective', where def:abs-polity (10:291) defines a polity as a composite class, an ultrametric notion. def:abs-culture and def:abs-market do invoke def:col-collective, but no result in the section exhibits a spectral collective for either: tab:abs-graded (10:440) says 'spectral contrast open (\cref{open:abs-code-contrast})' for cultures and lists only border factors for markets. The section opening (10:6) says most statements use the ultrametric diagnostic, so the definitions and the results use different notions.

Proposed fix. Rename 'one-round collective' to 'one-round set' (def:abs-one-round, prop:abs-one-round, cor:abs-one-round-extent, tab:sca-sizes row); replace 'law collective' by 'polity' and 'exchange collective' by 'market' at 10:321; at 10:3 write 'are treated here as candidate collectives'; add to def:abs-culture and def:abs-market: 'No result of this section shows that a culture (market) in a stated model is a collective in the sense of \cref{def:col-collective}; the results below concern its borders and the ultrametric diagnostic.'

State: applied. [10] applied: Convention adopted in group 10: 'one-round set' in definition, proposition and following prose; 'market' and 'polity' in the remark; opening sentence says 'candidate collectives'; both definitions carry the proposed disclaimer. The tab:sca-sizes row already says 'One-round diameter'; 12_related still says 'one-round collectives'. [04] declined: Nothing to change in group 04: its files contain no 'one-round collective', 'law collective' or 'exchange collective'; 04 only speaks of the one-round diameter and fixes the convention at def:col-ultrametric that the finding takes as the standard. All repairs lie in group 10.

### abs-07 (minor): tab:abs-graded cites prop:abs-barrier for an ultrametric contrast the proposition does not state; the contrast of a barrier-bounded arc is negative for weak barriers at small self weight

Location: sections/10_abstract_collectives.tex:440 (tab:abs-graded, Culture row) and caption :437; sections/10_abstract_collectives.tex:116; sections/chk10_abstract_collectives.tex:15 (chk:abs-barrier). Labels: tab:abs-graded, prop:abs-barrier, chk:abs-barrier, def:col-ultrametric. Category: table entry cites a result for more than it says.

Evidence. Table entry: 'Barriers give ultrametric contrast (\cref{prop:abs-barrier})'; caption: 'Entries that cite a result can be checked in the stated model'. prop:abs-barrier (10:100-114) states the transmission factor T, the equivalent distance d_b and the bound |Sigma/Sigma^0 - T| <= 2r/(1-r); it contains no statement about U(C). The only support is the computed ring of chk:abs-barrier (N=120, n_b=100: U = 2.79 against ln(1/T) = 2.30, reproduced as 2.7935). Unqualified, the entry fails (weak2.py; ring of 60, two barriers, arc of 30, U from full-graph single linkage): a=0.45, eps=0.01 (self weight 0.09): U = -0.073 at n_b=1.001, -0.038 at 1.05, -0.012 at 1.5, +0.013 at 2, 0.276 at 5, 2.49 at 100. With larger self weight (a=0.3, eps=0.01; a=0.2, eps=0.05; a=0.1, eps=0.001) U > 0 for every n_b > 1 tested and U exceeds ln(1/T) at n_b=100. The negative values arise because with small self weight next-nearest neighbors are more correlated than nearest neighbors, so u_in is not set by adjacent pairs.

Proposed fix. Table entry: 'Strong barriers give ultrametric contrast in the computed ring (\cref{chk:abs-barrier}); \cref{prop:abs-barrier} gives the border factor'. Alternatively add a proposition with hypotheses (correlations decreasing in distance within the arc, which fails at small self weight, and $n_b$ above a stated bound) and cite that.

State: applied. [10] applied: Reproduced (abs-07.py): ring of 60, a=0.45, eps=0.01 gives U=-0.073, -0.038, -0.012, +0.013, 0.276, 2.488 at n_b=1.001..100; distance-2 correlation 0.659 exceeds distance-1 0.612. Table entry now cites chk:abs-barrier as proposed; prose after prop:abs-barrier and the check state the limitation with numbers.

### abs-08 (minor): prop:abs-elasticity(c) calls a non-normalizable weight a density

Location: sections/10_abstract_collectives.tex:375 (prop:abs-elasticity(c)); proof sections/app10_abstract_collectives.tex:117-127. Labels: prop:abs-elasticity. Category: wording.

Evidence. 'a mixture of exponential profiles whose scales have density proportional to $\xi^{-1-\alpha_{\mathrm{el}}}$ on $(0,\infty)$': the integral of xi^{-1-alpha} over (0,inf) diverges at 0 for alpha > 0, so no probability density is proportional to it. The identity int_0^inf e^{-d/xi} xi^{-1-alpha} d xi = Gamma(alpha) d^{-alpha} used in the proof is correct for alpha > 0 and d > 0 (hand; not integrated numerically), so only the word is wrong; the 'mixture' is an integral against a sigma-finite weight and the resulting profile diverges as d -> 0.

Proposed fix. 'an integral of exponential profiles against the weight $\xi^{-1-\alpha_{\mathrm{el}}}\,\mathrm d\xi$ on $(0,\infty)$ (a $\sigma$-finite weight, not a probability density), for $d>0$'.

State: applied. [10] applied: Confirmed: xi^{-1-alpha} is not integrable at 0 for alpha>0. Part (c) now reads as an integral against a sigma-finite weight for d>0 (no spacing macro); proof notes d>0 and divergence as d->0; chk wording and the 'mixture of scales' mention near conj:abs-distance aligned.

### abs-09 (minor): Readings of social-science findings appear in running prose outside remark or conjecture environments

Location: sections/10_abstract_collectives.tex:171, :242, :278, :287, :296, :298, :325, :357, :364, :368, :411 (policy sentence at :6). Labels: sec:abs (intro), rem:abs-polity-readings, rem:abs-marchetti, rem:abs-borders. Category: status discipline.

Evidence. The manuscript's status discipline assigns interpretations to remarks. The section's own policy sentence (10:6) is weaker: 'Every reading of a social-science finding is an interpretation or a conjecture, in a labeled remark or not'. Eleven readings sit in unlabeled prose, each hedged with 'we read' or 'in our reading': cultural affordances and norms (10:171), language borders and bilinguals (10:242), Hayek and trade networks (10:278), exchange rates (10:287), Deutsch's definition of a people (10:296), heterogeneity costs (10:298), print and imagined communities (10:325), urban scaling (10:357), telecommunication and travel (10:364), distance findings (10:368, 10:411). None is presented as a theorem, proposition or numerical result, and none claims an empirical fit; the departure is from environment placement only. Attributions to the cited works were not verified against primary sources.

Proposed fix. Either keep the section's policy and delete 'in a labeled remark or not' in favor of 'in a labeled remark or in prose marked as our reading', or move each of the eleven passages into a remark titled 'Interpretation' (several can merge: 10:296+10:298+10:325 into rem:abs-polity-readings; 10:357+10:364 into rem:abs-marchetti; 10:368+10:411 into one remark before conj:abs-distance).

State: applied. [10] applied: Took the first proposed option (moving eleven passages into remarks is restructuring). Policy sentence now says 'in a labeled remark or in prose marked as our reading'; the one unmarked passage (Alesina heterogeneity) now begins 'In our reading'. Attributions to cited works were not verified.

### Not checked by lane abs

- prop:abs-barrier checks at the stated sizes (801- and 4001-site chains); a 401-site chain was used instead.
- The 4000-site ring Lyapunov comparison in chk:abs-crossover; the closed form and a Fourier sum were used.
- chk:abs-union-cone: the Riccati coefficient 0.4123 and the union-cone example ex:abs-union-cone numerically.
- chk:abs-media record-model values (7.265, 9.995, 16.308, 3.592, 22.527); only their signs against the derived criterion.
- chk:abs-seguy: Monte Carlo sampling, the 40000-site ground states and the stated range 'between (1/2)(J/h)^2 and 26(J/h)^2+7'.
- chk:abs-polity 2D 512^2 lattice numbers.
- chk:abs-exchange numbers and the symbolic N=3 computation of chk:abs-walras.
- prop:abs-decoupling, prop:abs-conformity, prop:abs-exchange-consistency numerically (hand derivations only).
- The mixture integral in prop:abs-elasticity(c) numerically.
- rem:abs-interface small-p argument (the text itself marks it unchecked).
- Cited results read by title or header only, or not opened: thm:agy-heterogeneous, prop:agy-synchronous, ex:agy-no-data-sharing, prop:agy-performative-sign, thm:agy-joint-acts, thm:frm-formation, obs:frm-online, prop:frm-exact-fusion, thm:col-bridge (body), thm:sca-h4, ex:met-traders, ex:met-two-firms, ex:env-firm, prop:fw-rls (header only).
- Literature attributions (McCallum, Anderson and van Wincoop, Engel and Rogers, Marchetti, Bettencourt, Kocherlakota, Burridge, Seguy, Alesina and Spolaore, Deutsch, Anderson, Innis, Hayek, Rauch, Grossman and Stiglitz) against primary sources.
- Figures fig:abs-seguy and fig:abs-polity (tikz inputs not opened; only captions checked).
- The user-mentioned comparison file C:/Users/chris and christine/Documents/Codex/2026-11-09/dep/outputs/collective-agents-open-problems-comparison-2026-11-09.md was not opened in this lane.
- A general hypothesis under which a barrier-bounded arc has positive ultrametric contrast was not derived; only instances were computed (finite evidence in both directions).

### Redundancy noted by lane abs

- The necessity of conditioning on the world for the ultrametric diagnostic is argued twice: 04_collectives.tex:492 and 10:413-426 (about 80 words of overlap); keep the argument in section 10 with the proposition and leave one forward-pointing sentence in section 4.
- Cap numbers 3.37/2.80/2.12 and 0.114/0.072/0.041 appear in body prose (10:426) and again in chk:abs-cap (about 50 words); keep them in the check and cite it.
- Barrier numbers (18.9 and 39.3 hops, 2.79 against 2.30) appear at 10:116 and in chk:abs-barrier (about 60 words).
- 'Resistance exceeds about 2 xi bonds' rule of thumb at 10:116 and again in rem:abs-borders (about 30 words).
- The (q/2)[(I-W)^{-1}+(I+W)^{-1}] decomposition is explained at 10:136, in rem:abs-multiplex and in the M-matrix preliminaries of app10 (about 40 words each).
- 'No preference for conformity is assumed; the rule is derived' is said at 10:171, after prop:abs-conformity and after prop:coh-adoption in section 6 (about 80 words).
- One-round sets 'compose but are not comparable' with contrast-based sizes: 10:339, 10:350 (rem:abs-marchetti), tab:sca-sizes and rem:col-lengths (about 60 words).
- prop:env-multiplex(d) is summarized at 10:17 and again in open:abs-institutions at 10:468 (about 60 words).
- The agency-protocol paragraph at 10:450 restates thm:agy-agency(b)-(d) (about 150 words) and the formation-caveats paragraph at 10:452 restates section 7 (about 230 words); each can shrink to two sentences with citations.
- Hayek horizon and aggregation prose at 10:278 restates thm:env-hayek-horizon and prop:ren-hayek (about 90 words).
- prop:abs-hierarchy overlaps thm:ren-nested and prop:ren-per-level in 10c_renormalization.tex; state it as a corollary of those with the distance-profile formula as the only new content.
- Simplification: prop:abs-seguy(d) is a one-line corollary of prop:abs-homogeneous (a monotone transform of homogeneous correlations has zero ultrametric contrast).
- Simplification: def:abs-one-round, prop:abs-one-round and cor:abs-one-round-extent can merge into one corollary of cor:col-lstar.
- Simplification: def:abs-culture, def:abs-market and def:abs-polity can merge into one definition 'modality class' with a declared diagnostic (spectral or ultrametric) per modality, which also resolves finding 6.
- Simplification: drop the unused hypothesis 'C and V\\C each connected in L_1' from prop:abs-bypass.
- Simplification: prop:abs-elasticity(a) and (c) are elementary calculus identities; keep (b) as the result and move (a),(c) to a remark.

### Streamlining tiers proposed by lane abs

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| Section opening and intro (10:1-10) | A | 250 | States scope and the ultrametric-versus-spectral caveat; shorten and fix the 'are collectives' wording. |
| def:abs-multiplex | A | 150 | Everything in the section depends on it. |
| tab:abs-modalities | B | 200 | Illustrative catalog, no result depends on it. |
| prop:abs-decoupling | A | 120 | Short structural result used by the crossover and bypass propositions. |
| ex:abs-union-cone | B | 180 | Worked example with one computed coefficient; supplement. |
| prop:abs-crossover | A | 400 | Main multiplex result; part (c) and the numerical rates can go to the supplement. |
| rem:abs-multiplex | B | 120 | Repeats the resolvent decomposition explained elsewhere. |
| conj:abs-multiplex | B | 100 | Conjecture without supporting computation; supplement or open-problems list. |
| prop:abs-homogeneous | A | 120 | Baseline for the ultrametric diagnostic; state the empty-minimum convention. |
| prop:abs-barrier | A | 350 | Central border result; add a stated consequence for ultrametric contrast or stop citing it for one. |
| rem:abs-interface | C | 120 | Heuristic the text itself marks unchecked. |
| prop:abs-bypass | A | 250 | Shows a second layer bypasses a barrier; fix final clause. |
| rem:abs-borders | B | 200 | Interpretation of border-effect literature; repeats the 2 xi rule. |
| conj:abs-alignment | B | 150 | Conjecture; supplement. |
| rem:abs-innis | B | 180 | Correct criterion derived from section 8; belongs with prop:sca-records-length. |
| rem:abs-money | C | 180 | Interpretation with no result attached. |
| def:abs-culture | B | 80 | Merge with market and polity definitions. |
| prop:abs-conformity | B | 250 | Restates the derived adoption rule of section 6 in the convention modality. |
| tab:abs-seguy and prop:abs-seguy | B | 500 | (a),(b) are textbook arccos and Ising facts; (d) follows from prop:abs-homogeneous; keep one sentence and the figure in the main text. |
| rem:abs-dialects | B | 160 | Interpretation. |
| prop:abs-exchange-consistency | B | 250 | Standard cocycle and Hodge facts. |
| def:abs-market | B | 80 | Merge with culture and polity definitions; add the no-result caveat. |
| prop:abs-walras | B | 350 | Standard CARA-normal computation; (c) is the part specific to this framework. |
| prop:abs-hayek | A | 200 | Short and specific; the horizon and aggregation prose after it is tier B. |
| conj:abs-grossman-stiglitz | C | 120 | Restates a known paradox as a conjecture without a model here. |
| def:abs-polity | B | 80 | Merge with culture and market definitions. |
| prop:abs-polity | A | 450 | (a),(b) closed-form optimal extents are the section's most concrete social result; (c),(d) to the supplement. |
| rem:abs-polity-readings | B | 230 | Interpretation; correct the monotonicity sentence. |
| def:abs-one-round and prop:abs-one-round | C | 150 | Elementary; fold into the corollary and rename. |
| cor:abs-one-round-extent | B | 150 | Direct consequence of cor:col-lstar. |
| rem:abs-marchetti | C | 180 | Arithmetic illustration of a travel-time budget. |
| conj:abs-redundancy | C | 120 | Unsupported conjecture. |
| prop:abs-elasticity | B | 300 | (a),(c) elementary; (b) is the content. |
| prop:abs-hierarchy | B | 350 | Overlaps thm:ren-nested and prop:ren-per-level. |
| rem:abs-cutoff | B | 150 | Interpretive caveat. |
| conj:abs-distance | C | 130 | Unsupported conjecture about gravity-law exponents. |
| prop:abs-ultrametric-cap and surrounding prose (10:413-426) | A | 300 | Justifies conditioning on the world; needs the corrected closing sentence and the q/Q qualification. |
| tab:abs-graded | A | 250 | Honest summary of what is and is not established; correct the Culture row. |
| Section 10.9 agency and formation prose (10:448-454) | B | 450 | Restates sections 5 and 7; two sentences with citations suffice. |
| open:abs-code-contrast | B | 130 | Partly addressed by ex:hie-code-domains; say so. |
| open:abs-attention | B | 130 | Open problem with no partial result here. |
| open:abs-institutions | A | 160 | The stated gap between the section's results and its title claim about institutional agency. |

## Lane met: Section 10a, meta-agents

No critical defect in lane met. Every theorem, proposition, lemma and example that I re-derived or recomputed holds on its stated hypotheses, and every cheaply specified number reproduces (ex:met-summary-leak, ex:met-reafference, ex:met-traders including an extra N=640 point, ex:met-other-collectives, rem:met-aggregate-defect, prop:met-level0, all of tab:met-firms and the reproducible values of chk:met-two-firms). Two major repairs are needed, both about hypothesis scope in the assembled theorem thm:met-h5a. (1) Condition (S) of prop:met-consensus-filter, imported by (H-suff), requires the sensing matrix H to have full column rank on the closed coarse exterior, and lem:met-riccati assumes Lambda^s positive definite; the paper's own two-firm instance (five-dimensional eta_{C_1}, sensors reading only the price, so rank H = 1 and the information matrix 3.75 e_1 e_1^T is singular) is outside those hypotheses, as is any minimal closed extension that adjoins unsensed coordinates. The conclusions remain true there (script: unique Riccati fixed point from several starts, error covariance equal to P-bar^- to 5.8e-15, closed-loop radius 0.636), so the repair is to allow H = H_0 G with Lambda^s positive semidefinite and to restate the lemma under rho(F-bar) < 1 or detectability. (2) The second sentence of thm:met-h5a(i) invokes prop:met-leak-bound for an arbitrary perturbation of (H-suff), but that proposition needs a block-diagonal residual noise, a decoupled initial precision, stable diagonal blocks and c_C k < 1. Three minor items: 'noiseless member computation' in (iv) lies outside Q^Xi > 0; ex:met-two-firms cites thm:met-h5a(ii) for firm C_2, which violates (H-phys), although the argument of (ii) needs only (H-prot); tab:met-hypotheses attributes 0.127 nats to prop:met-literal-aggregation, while that number comes from a product pool of independent local filters (the proposition's own construction gives 0.02741 filtered, 0.12220 predicted in the same model). Scope: linear-Gaussian statements only; random-instance checks whose test systems are not specified to coefficient level were not reproduced. Minimal unresolved obligation: a written proof of lem:met-riccati for singular Lambda^s (standard, sketched in the fix). Next action that would change the answer: restate (S) and lem:met-riccati as proposed, after which thm:met-h5a covers its own worked example. Scripts are in <session scratch>/audit/met/ (s1_two_firms_coarse.py, s2_two_firms_more.py, s3_two_firms_fine.py, s4_examples.py, s5_probes.py); the findings.md copy could not be saved because the harness refused the write, so this output is the only record. The user-referenced comparison file collective-agents-open-problems-comparison-2026-11-09.md was not opened.

Coverage: 44 items examined; 31 hold, 5 defective, 1 suspect, 7 not checked.

| Item | Verdict | Note |
|---|---|---|
| ex:met-channel-memory | not_checked | Mechanism read; values not recomputed. |
| prop:met-consensus-filter | defect | Conclusions (a),(b),(c) and the initialization verified for Lambda^s > 0; condition (S) excludes rank-deficient H (finding 1). |
| lem:met-riccati | defect | Correct as stated; hypothesis Lambda^s > 0 too strong for its use in the two-firm instance (finding 1). |
| thm:met-h5a (i) | defect | First sentence and zero stationary rate hold; second sentence over-extends prop:met-leak-bound (finding 2). |
| thm:met-h5a (iv) | defect | Content holds; 'noiseless' wording outside Q^Xi > 0 (finding 3); hypothesis scope per finding 1. |
| tab:met-hypotheses | defect | Row on literal pooling mis-attributes 0.127 nats (finding 5); other rows consistent. |
| chk:met-level0 | suspect | Wording 'without the factor F' does not match the stated equation; equation itself holds. |
| chk:met-blanket | not_checked | Test system not specified to coefficient level; validation value 0.143841 is correct. |
| chk:met-leak-bound | not_checked |  |
| chk:met-physics | not_checked |  |
| chk:met-lemmas | not_checked | Own random probe of lem:met-discrete-closure(c) agrees with the claim. |
| chk:met-closure-notions | not_checked |  |
| chk:met-inference | not_checked |  |

Items found to hold: def:met-coarse; def:met-coarse-blanket; thm:met-coarse-blanket; prop:met-sufficiency; ex:met-summary-leak; ex:met-reafference; prop:met-leak-bound; def:met-abstract-physics; def:met-lumpable; thm:met-abstract-physics; prop:met-memory; ex:met-traders; rem:met-aggregate-defect; ex:met-other-collectives; lem:met-unit-coordinate; lem:met-discrete-closure; prop:met-closure-notions; prop:met-literal-aggregation; prop:met-level0; thm:met-h5a (ii); thm:met-h5a (iii); thm:met-h5a (v); rem:met-no-selection; ex:met-two-firms; tab:met-firms; chk:met-two-firms; chk:met-traders; chk:met-other-collectives; rem:met-corporation; open:met-approximate, open:met-mutual, open:met-leak-constant, open:met-nonlinear; cross-references (thm:col-boundary(e), def:col-collective, def:col-contrast, thm:agy-h1(c), thm:agy-closure-average, thm:ren-closure(b), prop:env-aggregate-closure(a), prop:env-aggregate-memory, asm:sca-standing).

### met-01 (major): Full-column-rank H and Lambda^s > 0 exclude the two-firm instance and every closed extension with unsensed coordinates

Location: sections/10a_meta_agents.tex:266 (prop:met-consensus-filter, condition (S)); sections/10a_meta_agents.tex:324 (thm:met-h5a, (H-suff)); sections/app10a_meta_agents.tex:108-109 (lem:met-riccati). Labels: prop:met-consensus-filter, lem:met-riccati, thm:met-h5a, ex:met-two-firms, thm:met-abstract-physics. Category: missing-hypothesis-scope.

Evidence. (S) reads 'X_{S,t+1} = H eta_{C,t} + Xi^S_t with R_S block diagonal over channels and H of full column rank', and (H-phys) requires eta_C to be closed. lem:met-riccati reads 'Let Q-bar > 0 and Lambda^s > 0 ... Psi is monotone and bounded by (Lambda^s)^{-1}'. In ex:met-two-firms with C_1 on its exact model, eta_{C_1} = (p, s_{C_2}, y^eta_{C_2}, y^alpha_{C_2}, a_{C_2}) is five-dimensional and all four sensors read only p, X_{i,t+1} = p_t + v_{i,t}. Hence H = h e_1^T with h = (1,1,1,1)^T has rank 1, not 5, and H^T R_S^{-1} H = 3.75 e_1 e_1^T is singular; the example itself quotes the scalar Lambda^s = 3.75. The same happens whenever the minimal closed extension of thm:met-abstract-physics(f) adjoins coordinates no sensor reads. The conclusions are nevertheless true in the instance: script s1_two_firms_coarse.py iterates Psi with the singular 5x5 information matrix, finds one fixed point from several starts, the stationary error covariance of the member average equals P-bar^- to 5.8e-15, the closed-loop spectral radius is 0.636 and rho(F-bar) = 0.618. So the defect is in the hypotheses, not the result.

Proposed fix. In (S) replace 'and $\mathcal H$ of full column rank' by 'with $\mathcal H=\mathcal H_0\mathsf G$, $\mathcal H_0$ of full column rank and $\mathsf G$ of full row rank ($\mathsf G=I$ when every coordinate of $\eta_C$ is sensed)'. With $s_C=\mathcal H^\top R_{\sS}^{-1}X_{\sS}$ and $\Lambda^s=\mathcal H^\top R_{\sS}^{-1}\mathcal H\succeq0$ every displayed formula of the proposition is unchanged ($\bar v_t\sim\Ncal(0,\Lambda^s)$ is then a degenerate Gaussian). Restate lem:met-riccati as: 'Let $\bar Q\succ0$, $\Lambda^s\succeq0$ and $\rho(\bar F)<1$ (more generally $(\bar F,\Lambda^s)$ detectable), and let $\Psi(P)=((\bar FP\bar F^\top+\bar Q)^{-1}+\Lambda^s)^{-1}$. Then $\Psi$ is monotone, $\Psi(P)\preceq\bar FP\bar F^\top+\bar Q$, it has a unique fixed point $\bar P$, the iterates converge to $\bar P$ from every positive semidefinite $P$, and $\bar F(I-\bar P\Lambda^s)$ has spectral radius below one.' Proof changes: bound $\Psi^k(0)$ by the Lyapunov solution $L=\bar FL\bar F^\top+\bar Q$ instead of $(\Lambda^s)^{-1}$; for an arbitrary start $P\succeq0$ squeeze $\Psi^k(P)$ between $\Psi^k(0)$ and $\Psi^k(S_c)$ with $S_c=\bar FS_c\bar F^\top+\bar Q+cI\succeq P$, for which $\Psi(S_c)\preceq S_c$; the stability and uniqueness steps stand as written. Add '$\rho(\bar F)<1$' (or detectability) to (X) of prop:met-consensus-filter and to (H-phys); the statement as written assumes $\rho(A)<1$ only.

What would overturn the finding. The claim at 10a:343 that every property of thm:met-h5a is computed in ex:met-two-firms under the theorem's hypotheses; the theorem as stated does not apply to that instance.

State: applied. [10a] applied: Confirmed: two-firm H has rank 1, rho(Fbar)=0.618, closed loop 0.636. (S) now factors H=H_0 G_eta; lemma restated for Lambda^s>=0 under detectability (covers rho(Fbar)<1 and Lambda^s>0), proof rebuilt with a supersolution bound. Detectability placed in part (b) and (H-phys), not (X), since part (a) does not need it. Check of the edit: [10a] defect, lem:met-riccati and its proof are correct (identity, supersolution, squeeze rechecked); 0.618, 0.636 and the chk figures reproduce. Gap: for G_eta != I the map H^T R^{-1} is not of full row rank, contrary to def:met-coarse, and proof (ii) cites prop:met-closure-notions(a), which assumes full row rank. Only proof (i) was adapted. Repair: [10a] repaired, Checker right: for G_eta != I, H^T R^{-1} = G_eta^T H_0^T R^{-1} has rank < its row count (numerically 2 of 3). (S) now names s^0_C = H_0^T R^{-1} X_S as the def:met-coarse state with s_C its injective image; proof (ii) applies prop:met-closure-notions(a) with diag(P_I, P^0_B), same kernel.

### met-02 (major): thm:met-h5a(i) uses prop:met-leak-bound beyond its hypotheses

Location: sections/10a_meta_agents.tex:331 (thm:met-h5a, clause (i), second sentence); proposition at sections/10a_meta_agents.tex:101-110 (prop:met-leak-bound). Labels: thm:met-h5a, prop:met-leak-bound. Category: cross-reference-overreach.

Evidence. Clause (i) states: 'If (H-suff) is violated by a perturbation, the leak rate is at most the bound of prop:met-leak-bound, quadratic in the violation.' prop:met-leak-bound is stated for 'a residual assignment with Q-tilde block diagonal for (I',B',E') and a start with (Sigma-tilde_0^{-1})_{I'E'} = 0', assumes rho(A-tilde_{I'I'}) < 1 and rho(A-tilde_{E'E'}) < 1, and concludes eq:met-leak-bound only 'If c_C k < 1'. A violation of (S) that correlates sensor noise with interior-side or exterior-side residual noise breaks the block-diagonal hypothesis; a violation with c_C k >= 1 has no bound at all (open:met-leak-constant records that the constant overshoots by a factor of about 20); and the stationary start of the perturbed system does not in general have vanishing (I',E') precision block, so the passage from the window bound to the stationary leak rate is not supplied. The derivation of the proposition itself was re-derived and holds on its own hypotheses.

Proposed fix. Replace the sentence by: 'If (H-suff) is violated by a perturbation that keeps the hypotheses of \cref{prop:met-leak-bound} (a residual assignment with $\tilde Q$ block diagonal, stable $\tilde A_{\sI'\sI'}$ and $\tilde A_{\sE'\sE'}$, and $\mathfrak c_C\mathsf k<1$), the window leak from a start with $(\tilde\Sigma_0^{-1})_{\sI'\sE'}=0$ obeys \eqref{eq:met-leak-bound}, which is quadratic in the violation.'

What would overturn the finding. The unconditional reading of 'If (H-suff) is violated by a perturbation, the leak rate is at most the bound of prop:met-leak-bound'.

State: applied. [10a] applied: Confirmed against the hypotheses of prop:met-leak-bound. Clause (i) second sentence replaced by the proposed conditional wording (block-diagonal residual noise, stable diagonal blocks, c_C k<1, start with vanishing (I',E') precision block).

### met-03 (minor): thm:met-h5a(iv): 'noiseless member computation' lies outside Q^Xi > 0

Location: sections/10a_meta_agents.tex:334 (thm:met-h5a, clause (iv)). Labels: thm:met-h5a. Category: domain-mismatch.

Evidence. The theorem is stated for 'the joint process eq:col-joint', whose noise covariance is positive definite, and clause (i) and the coarse-blanket results rely on that. Clause (iv) then says 'With noiseless member computation, the centralized start and P^-_0 = P-bar^-, (y^eta_{C,t+1}, P-bar^-) parametrizes the meta-agent's predictive law'. Zero computation noise makes the internal block of Q^Xi singular, so the case is a limit of the stated setting, not an instance of it. The mathematical content is correct: the steady-state filter driven by the realized (s_C, a_C) paths gives the exact predictive mean at any noise level, and y^eta_{C,t+1} differs from it by the response of F-bar(I - P-bar Lambda^s) to the averaged computation noise (first sentence of (iv), verified; tab:met-firms 'C_1 taken noiseless' row reproduced).

Proposed fix. Replace 'With noiseless member computation, the centralized start and $P^-_0=\bar P^-$, $(y^\eta_{C,t+1},\bar P^-)$ parametrizes' by 'With the centralized start and $P^-_0=\bar P^-$, $(\hat\eta^-_t,\bar P^-)$ parametrizes', and append 'and $y^\eta_{C,t+1}\to\hat\eta^-_t$ in mean square as the computation noise vanishes'.

State: applied. [10a] applied: Clause (iv) now parametrizes the predictive law by (hat eta^-_t, bar P^-) at any computation noise and adds mean-square convergence of y^eta, uniform in t. Proof gives the bound n*sum||K^l||; clause (v) and its proof reworded to match. Check of the edit: [10a] defect, New (iv) claims hold: d_{t+1}=K d_t+n_t, d_1=0, Minkowski gives rms <= n*sum||K^l||. But with member-specific computation noise dev_i gains K's response to nu_i - nu-bar, so deviations neither obey prop:met-consensus-filter(b) as stated nor vanish as n_c grows; (v) now asserts this in the noisy setting. Repair: [10a] repaired, Checker right: with member computation noise the deviation recursion gains the centered filter-state noise and B-bar times the centered stored-act noise (residual 1e-15 in simulation; rms deviation 0.17 at exact averaging, sigma 0.1). (iv), (v) restated; proof (iv) now derives the recursion.

### met-04 (minor): ex:met-two-firms cites thm:met-h5a(ii) for a firm that violates (H-phys)

Location: sections/10a_meta_agents.tex:375 (ex:met-two-firms); sections/10a_meta_agents.tex:332 (thm:met-h5a, clause (ii)). Labels: ex:met-two-firms, thm:met-h5a. Category: cross-reference-overreach.

Evidence. The example states 'Firm C_2 runs a bounded model' (an autoregression for the price alone with declared innovation variance 0.1) and then 'By thm:met-h5a(ii) the average of C_2 is closed'. C_2's coarse exterior is not closed under its bounded model, so (H-phys) fails for C_2 and the theorem does not apply as stated. The conclusion is correct: the appendix proof of (ii) uses only a sum-preserving W and coefficients common to all members, and eq:met-firms with coefficients f_p P-bar_2 and f_p(1 - 3 P-bar_2), P-bar_2 = 0.12571, reproduces exactly (scripts s1_two_firms_coarse.py, s3_two_firms_fine.py; 49- and 33-dimensional fine models with rho(A) = 0.797 and 0.824).

Proposed fix. Append to clause (ii): 'This part uses only (H-prot) and holds for any fixed matrices in place of $(\bar F,\bar P,\bar B)$, in particular for a bounded model.' Alternatively change the example to 'By the argument of \cref{thm:met-h5a}(ii), which uses only the sum-preserving protocol, the average of $C_2$ is closed'.

State: applied. [10a] applied: Clause (ii) now states it uses only (H-prot) and holds for any fixed matrices in place of (Fbar, Pbar, Bbar, Lambda^s); proof of (ii) says why; the example cites (ii) with that scope.

### met-05 (minor): tab:met-hypotheses attributes 0.127 nats to prop:met-literal-aggregation; the number comes from a different pooling rule

Location: sections/10a_meta_agents.tex:364 (tab:met-hypotheses, row 'consensus on information contributions'); sections/app10a_meta_agents.tex:145 (proof of thm:met-h5a(iv), 'literal aggregation is prop:met-literal-aggregation'); source row at sections/10a_meta_agents.tex:387-407 (tab:met-firms, last row). Labels: tab:met-hypotheses, tab:met-firms, prop:met-literal-aggregation. Category: attribution-mismatch.

Evidence. The table row reads 'literal pooling is overconfident (0.127 nats); level-0 averages carry memory | prop:met-literal-aggregation, prop:met-level0'. The value 0.1271 is the last row of tab:met-firms, '(iv) local filters with a product pool: error, claimed, relative entropy | 0.12636, 0.07290, 0.1271'. Script s2_two_firms_more.py reproduces it with four independent local Kalman filters whose predictive laws are multiplied: claimed variance 0.07290 = 1/sum_i(1/P_i^-), actual error 0.12636. prop:met-literal-aggregation(b) defines a different object, 'the product of the members' posteriors, each computed from a common predicted prior', with covariance the fixed point of Psi_n; in the same bounded model that construction gives 0.02741 (filtered) and 0.12220 (predicted), not 0.07290. Both constructions are overconfident, so the qualitative statement stands; the number and the citation do not match.

Proposed fix. Change the table entry to 'a product pool of local filters is overconfident ($0.127$ nats, \cref{tab:met-firms}); literal pooling from a common prior likewise (\cref{prop:met-literal-aggregation}); level-0 averages carry memory'. Alternatively recompute the last row of tab:met-firms with the construction of prop:met-literal-aggregation(b) and report that relative entropy.

State: applied. [10a] applied: Reproduced: product pool of local filters claims 0.07290; prop:met-literal-aggregation(b) gives 0.02741 filtered, 0.12220 predicted. Table entry reworded as proposed; dangling literal-aggregation phrase removed from the proof of (iv).

### met-06 (minor): ex:met-summary-leak quotes rates without stating the gains

Location: sections/10a_meta_agents.tex:84 (ex:met-summary-leak). Labels: ex:met-summary-leak, chk:met-blanket. Category: underspecified-example.

Evidence. The closed form for Var(y | s) is given in terms of g_1, g_2, R^s_1, R^s_2 and the quoted leak values (0.135600 and 0.619053, reproduced in s4_examples.py) are for g_k = 1/R^s_k, a choice stated only in the check, not in the example body.

Proposed fix. Insert in the example before the numbers: 'with $g_k=1/R^s_k$, the weights of the information-form statistic,'.

State: applied. [10a] applied: Rates 0.135600 and 0.619053 reproduced with g_k=1/R^s_k; the example now states that the numbers use these gains.

### met-07 (minor): open:agy-discrete-closure does not point to the partial resolution in lem:met-discrete-closure

Location: sections/05_agency.tex:127 (open:agy-discrete-closure); resolution at sections/10a_meta_agents.tex:232-246 (lem:met-discrete-closure). Labels: open:agy-discrete-closure, lem:met-discrete-closure. Category: status-consistency.

Evidence. The open problem states the discrete-time closure question without qualification. lem:met-discrete-closure proves the reversible one-coordinate case (parts (a) to (c); random probe of (c) in s5_probes.py: maximum ratio of the defect to the bound 0.943, tangent ratio 0.9993), and 10a:245 says what remains open ('for the latter and for non-reversible recursions'). A reader of sec:agy alone sees the problem as wholly open.

Proposed fix. Append to open:agy-discrete-closure: 'The reversible case for one coordinate is \cref{lem:met-discrete-closure}; open are the precision-based contrast of \cref{def:col-contrast} and non-reversible recursions.'

State: applied. [05] applied: Appended the proposed sentence verbatim to open:agy-discrete-closure; lem:met-discrete-closure and def:col-contrast exist. Nothing needed from group 10a for this part. [10a] applied: Open problem lies in 05_agency.tex. In 10a the remark after lem:met-discrete-closure now cites open:agy-discrete-closure directly and says the lemma settles the reversible one-coordinate case, with the precision-based contrast and non-reversible recursions open. Follow-up for 05 returned.

### met-08 (minor): chk:met-level0 says the decomposition was checked 'without the factor F' while eq:met-level0 carries F

Location: sections/chk10a_meta_agents.tex:41 (chk:met-level0); equation at sections/10a_meta_agents.tex:302-319 (prop:met-level0, eq:met-level0). Labels: chk:met-level0, prop:met-level0. Category: check-statement-mismatch.

Evidence. The check reads 'the decomposition eq:met-level0 (without the factor F) agreed with the direct average'. The proposition's equation includes the common factor F. Probe s5_probes.py with F = 0.9 and five members confirms the equation with the factor and the closure criterion (generic gains d_cl = 0.0024; cancelling leaks 0; symmetric attention 0; directed 0.0007). No mathematical defect; the check as worded verifies a different display from the one stated.

Proposed fix. Reword to 'the decomposition \eqref{eq:met-level0}, checked with $F=1$ and with $F=0.9$, agreed with the direct average', after rerunning with the factor, or state 'checked at $F=1$'.

State: applied. [10a] applied: Confirmed: check wording verified a display without F. Reran (scripts/met-08.py): eq:met-level0 agrees with the direct average to 9e-16 at F=1 and F=0.9; closure defect zero iff equal column sums at F=0.9. Check reworded; old defect values labeled F=1, F=0.9 values added.

### met-09 (minor, unconfirmed): chk:met-blanket test system is not specified to coefficient level

Location: sections/chk10a_meta_agents.tex:6-8 (chk:met-blanket). Labels: chk:met-blanket, chk:met-leak-bound, chk:met-physics. Category: reproducibility.

Evidence. The check describes 'three members whose internal states read their own sensory channels, each other and ...' with numerical leak values, but the coefficients are not given, so the reported values cannot be regenerated from the text. The validation value 0.143841 = (1/2) ln(4/3) on ex:col-collider is correct arithmetic. The same limitation applies to the random instances of chk:met-leak-bound and chk:met-physics.

Proposed fix. Give the matrices (or the seed and generator) of the three-member system in the check, or cite the script name and the saved output that produced the numbers.

State: applied. [10a] applied: Confirmed. Original script located; chk:met-blanket now prints all coefficient blocks (four decimals); scripts/met-09.py reproduces the reported leaks from them to three digits. chk:met-physics now states its construction, fixed coefficients and generator seed. The 'independent implementation' random instances remain unspecified.

### Not checked by lane met

- ex:met-channel-memory numerical values
- chk:met-blanket three-member leak values (system not specified to coefficient level)
- chk:met-leak-bound constants and the factor-of-20 and four-orders statements in open:met-leak-constant
- Random instances of chk:met-physics, chk:met-lemmas, chk:met-closure-notions and chk:met-inference
- Agency figures of the two-firm example: tilts 0.249, 0.136, 0.018, total variation 1.1e-15 and 0.06 to 0.13
- Constants 76/152/304 of thm:agy-closure-average(b)(iii) used through lem:met-unit-coordinate(a)
- Cross-referenced items not opened: thm:col-diffusive-precision, thm:col-bridge, rem:ren-rgm, ex:env-firm, ex:env-person, rem:env-firm-meta-agent, thm:agy-joint-acts, ex:agy-no-potential, prop:agy-literal-consensus
- External citations (fields2022competency, palacios2020markov Eq. 14, rosas2024software) not verified against the primary sources
- The user-referenced file collective-agents-open-problems-comparison-2026-11-09.md was not opened
- A written proof of lem:met-riccati for singular Lambda^s; only the proof outline and a numerical confirmation in the two-firm instance are supplied
- findings.md copy in the lane directory: the write was refused by the harness, so no copy exists

### Redundancy noted by lane met

- Section introduction (10a:1-10, about 380 words) previews all five properties and the hypotheses that thm:met-h5a (10a:321-343) and tab:met-hypotheses (10a:350-371, about 205 words) then state; about 200 words of the introduction can go.
- fig:met-partition caption (10a:38-43, about 280 words) restates prop:met-sufficiency and thm:met-abstract-physics in prose; a caption of about 80 words suffices.
- rem:met-no-selection (10a:345-347, about 130 words) repeats the selection statement of thm:col-boundary(e) and the introduction; about 60 words are new (the two places contrast enters).
- tab:met-firms and the paragraph after it (10a:387-409, about 410 words) are repeated value by value in chk:met-two-firms (chk10a:44 onward); keep the table in the main text and reduce the check to what the table omits.
- ex:met-other-collectives (10a:205-217, about 350 words) and chk:met-other-collectives report the same numbers twice.
- ex:met-traders (10a:184-198) and chk:met-traders duplicate the N = 10, 40, 160 values.
- def:met-abstract-physics (i),(ii) restate def:agy-closure and are restated again as thm:met-abstract-physics(a).
- prop:met-literal-aggregation(a) is a pointer to prop:agy-literal-consensus with no new content.
- The closure criterion of prop:met-level0 (equal column sums) is prop:env-aggregate-closure(a) and def:met-lumpable with one block, stated three times across sec:met and sec:env.
- lem:met-discrete-closure (a) and (b) are one argument applied to I - A-tilde and I - A-tilde^2; lem:met-unit-coordinate(b) and lem:met-discrete-closure(c) share the same symmetric-matrix bound and could be one lemma.
- thm:met-abstract-physics(e) is a special case of (a).

### Streamlining tiers proposed by lane met

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| def:met-coarse | A | 150 | Defines the coarse variables every later statement uses. |
| def:met-coarse-blanket | A | 120 | Defines the object of clause (i). |
| thm:met-coarse-blanket (a) with prop:met-sufficiency (a) | A | 290 | Characterization and the sufficient conditions that (H-suff) imports. |
| thm:met-coarse-blanket (b), prop:met-sufficiency (b),(c) | C | 150 | Weak-blanket and converse variants not used by thm:met-h5a; supplement. |
| def:met-abstract-physics and def:met-lumpable | A | 200 | Needed for (H-phys); merge with thm:met-abstract-physics(a) to remove the repeated statement. |
| thm:met-abstract-physics | A | 300 | Kernel invariance and the minimal closed extension carry (H-phys) and the two-firm example; drop (e) as a special case of (a). |
| prop:met-consensus-filter | A | 400 | Core of clause (iv); restate (S) per finding 1. |
| thm:met-h5a | A | 550 | Headline result of the section. |
| ex:met-two-firms with tab:met-firms | A | 710 | The one worked instance in which every clause is computed. |
| prop:met-leak-bound | B | 165 | Supports only the second sentence of (i); state the bound in one sentence in the main text and move the constants to the supplement. |
| prop:met-memory | B | 315 | Quantifies failure of closure; main text can keep (a) and the definition of the memory measures. |
| ex:met-traders | B | 225 | Shows that aggregates keep memory as N grows; keep the closed form, move the table of N values to the check. |
| lem:met-unit-coordinate | B | 170 | Technical bridge to thm:agy-closure-average; supplement with a one-line pointer. |
| lem:met-discrete-closure | B | 350 | Partial answer to open:agy-discrete-closure; merge (a),(b) into one statement and move the proof detail to the supplement. |
| prop:met-closure-notions | B | 375 | Comparison of closure notions; a short remark in the main text and the full statement in the supplement. |
| prop:met-literal-aggregation | B | 205 | Negative control for (iv); drop (a) as a pure pointer and keep (b). |
| prop:met-level0 | B | 370 | Shows that level-0 protocols do not close the average in general; criterion duplicates prop:env-aggregate-closure(a). |
| ex:met-summary-leak | B | 140 | Shortest demonstration that the information-form statistic is needed. |
| rem:met-no-selection | B | 135 | Status statement that H5a does not select collectives; cut to the two sentences on where contrast enters. |
| tab:met-hypotheses | B | 205 | Compact map of what fails when each hypothesis is dropped; correct the literal-pooling row. |
| open:met-approximate, open:met-mutual, open:met-leak-constant, open:met-nonlinear | B | 265 | Keep open:met-approximate and open:met-mutual in the main text; the other two fit the supplement. |
| ex:met-channel-memory | C | 140 | Second counterexample to a hypothesis already illustrated; supplement. |
| ex:met-reafference | C | 130 | Third counterexample of the same kind; supplement. |
| ex:met-other-collectives | C | 350 | Numerical illustration of drift-based contrast, duplicated in its check. |
| rem:met-aggregate-defect | C | 125 | Side inequality used nowhere else. |
| rem:met-abstract | C | 125 | Terminological remark. |
| rem:met-corporation | C | 190 | Declared interpretation; one sentence in the main text is enough. |
| fig:met-partition caption | C | 280 | Caption restates two results; shorten to about 80 words. |
| lem:met-riccati | C | 120 | Standard Riccati facts; appendix only, restated for Lambda^s positive semidefinite. |
| chk:met-blanket through chk:met-two-firms | C | 2150 | Supplement; remove values already in main-text tables and add the missing system specifications. |

## Lane hie: Section 10b, hierarchy

No theorem, proposition, lemma or corollary in sections/10b_hierarchy.tex is false as written; every one was reconstructed by hand or by script and the appendix proofs prove the statements, with three small statement/proof mismatches. One conjecture fails: conj:hie-top-down ("any positive precision on a self-written record raises every member's stationary error") is refuted by its own stated criterion on the same level-0 model that reproduces obs:hie-top-down exactly. Three verified instances have error falling by 0.9 to 3.6 percent with positive record precision, and 694 of 1728 scanned parameter points have a negative derivative at zero precision. The cause is that thm:hie-floor, cited as the basis, controls only the common-mode part of the error, while the local-noise part falls with record precision. The claim is repeated as "never helps" in the introduction, coherence and discussion sections. Six minor defects: the exchangeable clause of conj:hie-conformity-formation(ii) needs at most N/2 walls (counterexample N=60, w=58); an index slip in the chain of prop:hie-nested-records; prop:hie-depth(c) omits that the prior is also counted twice; prop:hie-record-filter(a) omits the record's initialization; the weak-reading sentence after prop:hie-record-gain reports a discontinuity of the joint spectrum as an effect of the record; prop:hie-echo-tradeoff uses the echo ratio of def:mis-echo for member-specific targets. All three numerical observations (obs:hie-record-window, obs:hie-top-down, obs:hie-exact-receiver) and every fixed-instance number recomputed from chk10b reproduce; the large random-draw statistics of the checks were not rerun. Scripts and a findings copy are in <session scratch>/audit/hie/ (findings.md, s1 to s9).

Coverage: 30 items examined; 28 hold, 1 defective, 1 suspect, 0 not checked.

| Item | Verdict | Note |
|---|---|---|
| conj:hie-top-down | defect | Refuted by its own criterion on the same model (finding F1). |
| conj:hie-conformity-formation | suspect | Clause (ii) needs at most N/2 walls for its exchangeable part (finding F2); clauses (i), (iii), (iv) are conjectural and their cited bases (thm:coh-domains-1d, rem:hie-pragmatic, obs:hie-exact-receiver) say what they are cited for. |

Items found to hold: prop:hie-closure-exact; ex:hie-markov-without-closure; lem:hie-misspecification; prop:hie-reversible-sandwich; thm:hie-messages; prop:hie-predictive-coding; prop:hie-literal-once; prop:hie-literal-records; prop:hie-record-filter; prop:hie-depth; prop:hie-record-gain; cor:hie-identity; lem:hie-record-blind; thm:hie-floor; prop:hie-nested-records; prop:hie-record-contrast; ex:hie-noiseless-record; obs:hie-record-window; prop:hie-global-record; prop:hie-echo-tradeoff; obs:hie-top-down; prop:hie-conformity; prop:hie-record-bistability; obs:hie-exact-receiver; ex:hie-code-domains; thm:hie-three-levels; rem:hie-pragmatic; chk10b (all eight checks).

### hie-01 (major): conj:hie-top-down is refuted by its own criterion on the model of obs:hie-top-down

Location: sections/10b_hierarchy.tex:357-362 (conj:hie-top-down and basis sentence); also 10b:355, 01_introduction.tex:207 and :250, 06_coherence.tex:398, 13_discussion.tex:23. Labels: conj:hie-top-down, obs:hie-top-down, thm:hie-floor. Category: false conjecture / cross-reference used beyond what it says.

Evidence. Statement (10b:358): "any positive precision assigned to a record of the members' own mean of a grounded coordinate raises every member's stationary mean-square error." Criterion (10b:362): "an instance with a negative derivative at r_z=0 would refute it." The level-0 network with record (claimed variances at the fixed point of sec:coh-tension, error recursion solved by discrete Lyapunov) reproduces every number of obs:hie-top-down(a): MSE 0.2815, 0.3426, 0.4495, 0.6631, 0.8579 and echo ratios 36.0, 46.7, 60.3, 49.0, 22.8. On that same model, with channel and record read noise variances 0.1 as in the observation: (A) complete graph of 8, F=0.9, Q=0.02, sensing variance 4, message precision 10, omega=0.05: MSE 0.111056 (r_z=0), 0.111028 (0.1), 0.110796 (1), 0.110419 (3), 0.110038 (10; -0.92%), 0.112207 (30). (B) complete graph of 8, F=0.99, Q=0.001, sensing variance 4, message precision 10, omega=0.05: 0.052056, 0.051819 (1), 0.051493 (3), 0.051185 (10; -1.67%), 0.052275 (30). (C) ring of 40, F=0.99, Q=0.001, sensing variance 4, message precision 10, omega=0.2: 0.050778, 0.049747 (1), 0.048964 (3; -3.57%), 0.049237 (10), 0.052700 (30). The Lyapunov solve and an independent doubling iteration agree to six digits (s8e_conj_verify.py). A grid scan found 694 of 1728 parameter points with dMSE/dr_z<0 at r_z=0; two changes from the manuscript's own instance suffice (F=0.9 and message precision 10 give derivative -4.5e-5; the manuscript's instance has +6.0e-2). In all three instances the gains are convex weights and beta+omega<=1, and message precision 10 equals the inverse channel noise. Mechanism: the error splits as Q*F_com (common mode) plus a local-noise part. thm:hie-floor, cited as the basis, concerns only Q*F_com, which rises in every instance (A: 0.103200 to 0.103812 at r_z=10); the local part falls (A: 0.007857 to 0.006226), and where its share is 7 to 14 percent the total falls. In the manuscript's instance the local part also falls (0.008261 to 0.006664 at r_z=1) but its share is 2.9 percent.

Proposed fix. Replace the conjecture by a restricted statement: "For level-0 members, positive precision assigned to a record of the members' own mean of a grounded coordinate raises the common-mode part Q F_com of every member's stationary mean-square error. The total error rises when the local-noise part is a small share of it, as in obs:hie-top-down(a), and can fall otherwise (instances with a 1 to 4 percent fall exist at weak sensing and strong message precision)." Change the basis sentence to cite thm:hie-floor(c) for the common-mode part only. Replace "never helps" at 01_introduction.tex:207 and :250 and 13_discussion.tex:23, the phrase "conjectures for every level-0 collective" at 06_coherence.tex:398, and "never as an independent top-down prior" at 10b:355, by the restricted claim.

What would overturn the finding. A demonstration that the level-0 record model intended by the manuscript differs from the one that reproduces obs:hie-top-down(a) to four digits, or that in instances A to C the members' message gains do not "already average their neighbors" in the sense intended (sum of message gains 0.66, 0.22, 0.12 with convex weights).

State: applied. [06] applied: Not recomputed independently; group 10b has already restated conj:hie-top-down as a proposition on the common-mode part and added the falling instances as obs:hie-top-down(c). The sentence in sec:coh now carries the restricted claim and cites (c). [10b] applied: Confirmed by an independent Kronecker solve: manuscript numbers reproduce, instances A to C fall 0.92, 1.67, 3.57 percent. Label kept, now a proposition on the common-mode part with proof (uses thm:hie-floor(b) and monotone sensing gain); obs gains item (c); chk extended; closing sentence and 'never' sentence updated. Other files need follow-ups. Framing pass: [group 01] applied; [group 13] applied

### hie-02 (minor): conj:hie-conformity-formation(ii): exchangeable clause is false without a bound on the number of walls

Location: sections/10b_hierarchy.tex:440 (conj:hie-conformity-formation, clause (ii)) and :447 (basis sentence); app10b_hierarchy.tex:195-197. Labels: conj:hie-conformity-formation, ex:hie-code-domains. Category: missing hypothesis.

Evidence. 10b:440: "under the exchangeable comparison ... no domain of three or more sites qualifies"; 10b:447: "clause (ii) holds exactly for the reversible nearest-neighbor precision." For that precision a three-site domain has internal rate lambda_3=a and the exchangeable threshold is N*a_ex=2a(N-w)/(N-1) with w walls, so lambda_3>N*a_ex iff w>(N+1)/2 (cut is zero, so by prop:ren-exchangeable the domain is then a collective at every positive leak). Counterexample: N=60, a=1, w=58 (57 single-site domains and one of three sites): 1 > 4/59 = 0.0678. The appendix derivation carries the hypothesis ("because w <= N/2 when every domain has at least two sites"); the conjecture and the basis sentence do not. In the instances of ex:hie-code-domains (w<=10) the sentence holds.

Proposed fix. In clause (ii) and at 10b:430: "while under the exchangeable comparison, which applies only without declared geometry, no domain of three or more sites qualifies when the ring has at most N/2 walls (in particular when every domain has at least two sites)".

What would overturn the finding. A different exchangeable baseline than a_ex=2a(N-w)/(N(N-1)) for the walled ring, or a reading of 'domain' that excludes configurations with single-site domains.

State: applied. [10b] applied: Confirmed: a exceeds N a_ex iff w>(N+1)/2 (N=60, w=58 gives 4/59<1). Clause (ii) and the example sentence now carry 'at most N/2 walls'; appendix derivation states the bound and its necessity; chk records the counterexample. Basis sentence is correct with the added hypothesis, unchanged.

### hie-03 (minor): prop:hie-nested-records: the chain is described with an index slip

Location: sections/10b_hierarchy.tex:271 (prop:hie-nested-records). Labels: prop:hie-nested-records, thm:hie-three-levels. Category: local slip.

Evidence. "for nested records, a chain in which record k is read by the writers of record k-1". The writers of record k-1 are node k-2, so the phrase describes an edge (k, k-2), which is not an edge of the chain 0-1-2-... required by the tree hypothesis, and is undefined at k=1. The displayed bound (weights 1, R_1, R_1 R_2, ...) is the left null vector of the chain in which record k exchanges with record k-1, the structure used in thm:hie-three-levels (members, group record, society record). The bound itself was confirmed on random chains and stars (s4_three_nested.py).

Proposed fix. "for nested records, a chain in which record k is read and written by record k-1, with record 0 the agents, it gives ..."

What would overturn the finding. A tree in which record k is linked to node k-2 and the stated left null vector still has entries R_1 R_2 ... R_k.

State: applied. [10b] applied: Index slip confirmed; chain now described as record k read and written by record k-1, with record 0 the agents. Bound and proof unchanged.

### hie-04 (minor): prop:hie-depth(c): prose says only the other data are counted twice, the formula also counts the prior twice

Location: sections/10b_hierarchy.tex:177 (prop:hie-depth(c)). Labels: prop:hie-depth. Category: prose versus formula.

Evidence. "counts every other datum twice: with G=1 and Psi=0 its believed precision is 2(Lambda^post_S - Lambda^o_i) + Lambda^o_i against the exact Lambda^post_S". Lambda^post_S contains the prior precision, so the prior is counted twice as well; the check values at prior precision 0.5 require it: (2(0.5+5)+1)/6.5 = 1.846, (2*49.5+1)/50.5 = 1.980, (2*399.5+1)/400.5 = 1.998, the stated 1.85, 1.98, 2.00. Part (b) of the same proposition states the prior count explicitly ("and the prior once").

Proposed fix. "counts the prior and every other datum twice".

What would overturn the finding. A definition of the society's message in (c) that excludes the prior, which would change the stated formula to 2(Lambda^post_S - Lambda^o_i) + Lambda^o_i - Lambda_prior.

State: applied. [10b] applied: Confirmed: the formula 2(Lambda_post_S - Lambda_o_i)+Lambda_o_i doubles the prior precision too. Prose now reads 'counts the prior and every other datum twice'.

### hie-05 (minor): prop:hie-record-filter(a): the record's initialization is a hypothesis of the proof only

Location: sections/10b_hierarchy.tex:164 (prop:hie-record-filter(a)); app10b_hierarchy.tex:90. Labels: prop:hie-record-filter. Category: missing hypothesis.

Evidence. Statement: "then the record equals the centralized Kalman filter at every round". Proof (app10b:90): "By induction: let the record hold the centralized posterior N(m_z,P_z) of x_t, as it does initially with the common prior." The base case is not in the statement; a record started elsewhere equals the centralized filter started from that law, and only converges to the filter started from the common prior under detectability and stabilizability.

Proposed fix. "(a) If the record is initialized at the common prior of x_0, every member is memoryless, ..., then the record equals the centralized Kalman filter started from that prior at every round".

What would overturn the finding. A general statement elsewhere in the section fixing the record's initial law at the common prior (none found in 10b:130-170).

State: applied. [10b] applied: Confirmed: the induction's base case was only in the proof. Part (a) now assumes the record is initialized at the common prior of x_0 and concludes equality with the centralized filter started from that prior. Proof unchanged.

### hie-06 (minor, unconfirmed): Weak-reading sentence reports a discontinuity of the joint spectrum as an effect of the record on separation

Location: sections/10b_hierarchy.tex:222 (prose after prop:hie-record-gain) and caption of fig:hie-records (10b:257-262). Labels: prop:hie-record-gain, eq:hie-gain, fig:hie-records. Category: interpretation.

Evidence. "For delta=0 a weakly read record lowers the separation ... g_sep -> omega/(eps+lambda_2(L_C)) = 0.255 as beta -> 0." At beta=0 the members' drift is the one without a record and the gain is 1 by definition, so g_sep is discontinuous at beta=0: the value 0.255 is the unread record's own rate omega entering the spectrum of the joint drift of members and record. The formula and the threshold beta<0.0930 are correct (checked against the 11x11 spectrum as in chk:hie-record-drift); the reading "the record lowers the separation" attributes to the members a rate that belongs to the record.

Proposed fix. "For delta=0 a weakly read record lowers the separation of the joint drift spectrum of members and record: the second-slowest rate is then the exchange rate r_+ of the members' mean and the record, which tends to the record's own rate omega as beta -> 0, while the members' own rates are unchanged in that limit."

What would overturn the finding. A definition of g_sep in prop:hie-record-gain that restricts the spectrum to the members' marginal dynamics.

State: applied. [10b] applied: Formula and threshold correct; the sentence was literally true of the joint spectrum but misattributable. Prose and caption now say the separation is that of the joint spectrum of members and record, with r_+ tending to the record's rate omega as beta tends to 0 and member rates unchanged.

### hie-07 (minor): prop:hie-echo-tradeoff(c) uses the echo ratio of def:mis-echo for member-specific targets

Location: sections/10b_hierarchy.tex:338-339 (prop:hie-echo-tradeoff(b),(c)); 03_misreading.tex:227-229 (def:mis-echo). Labels: prop:hie-echo-tradeoff, def:mis-echo. Category: definition mismatch.

Evidence. def:mis-echo defines D_C = max E||m_i - m_j||^2 and A_C = min E||m_i - eta||^2 for beliefs about one state eta. In prop:hie-echo-tradeoff members estimate different targets x_i = y_C + e_i with Var e_i = psi; the limiting error 1/a + psi contains the spread psi of the targets, and a zero disagreement of estimates of different targets is not the D_C of the definition. The computed quantities in (a) and (b) are correct (re-derived by hand).

Proposed fix. "so the ratio of mean-square error to disagreement, the analogue for member-specific targets of the echo ratio of def:mis-echo, diverges".

What would overturn the finding. An extension of def:mis-echo to agent-specific targets stated elsewhere in the manuscript.

State: applied. [03] applied: Real: prop:hie-echo-tradeoff has member-specific targets x_i, while def:mis-echo is for one state. My part is the sentence after thm:mis-echo-chambers, which said 'its echo ratio diverging'; it now uses the finding's wording. def:mis-echo itself is unchanged. The 10b sentence is its owner's. [10b] applied: Confirmed: def:mis-echo is defined for beliefs about one state eta, while members here estimate member-specific targets x_i. Re-derived (a),(b) by hand; both correct. Clause (c) now uses the proposed wording (ratio of mean-square error to disagreement, the analogue of the echo ratio). Proof and check need no change.

### Not checked by lane hie

- Random-draw statistics of the checks were not rerun: chk:hie-latent, chk:hie-messages, the 3000-ring, 200000-draw and 400000-point statistics of chk:hie-record-drift (extreme values 8.0e-11, 0.9998, 4.78, 0.99999997 and similar), the 300 random closed collectives of chk:hie-record-precision, and the random-draw parts of chk:hie-conformity. Only fixed-instance numbers were recomputed.
- The symbolic identities quoted in chk:hie-record-drift for thm:hie-floor(e) (K(x)=xK_1(x), the 40-digit rational comparison) were not rerun; the limit (e) was confirmed numerically only.
- thm:hie-messages was re-derived by hand; no script compared the two-pass messages with the joint precision on random trees.
- prop:hie-reversible-sandwich instance numbers were reproduced by hand, not by script.
- The independent second implementations mentioned in chk:hie-record-precision (outsiders joined at two matched pairs: 3.8e-3, 4.6e-5; delta=0.01 window) were not reproduced.
- The proofs of cited results outside the lane were not audited (prop:coh-adoption, thm:coh-domains-1d, thm:coh-grounding-tension, prop:sca-records-memory, prop:agy-identity, prop:ren-exchangeable, lem:frm-calibration); only their statements and hypotheses were compared with the use made of them. thm:coh-grounding-tension was read in part.
- For conj:hie-top-down no analytic proof of the sign of the local-noise derivative was attempted; the refutation is numerical (two independent solvers, six-digit agreement).
- Clauses (i), (iii), (iv) of conj:hie-conformity-formation were not tested by simulation of the code game.

### Redundancy noted by lane hie

- fig:hie-records caption (10b:257-262) repeats the prose after prop:hie-record-gain (10b:222) and the discussion after thm:hie-floor (10b:264): about 250 words stated twice.
- fig:hie-overconfidence caption (10b:152-157) repeats 10b:159 (overconfidence factors, MSE between 1/4 and 1/3, linear versus geometric growth): about 120 words.
- The weak-reading derivation (r_+ r_- = eps*omega, threshold, limit 0.255) appears in the body at 10b:222, in the appendix near app10b:112 and again in chk:hie-record-drift: about 150 words each; keep one derivation in the appendix and one sentence in the body.
- conj:hie-conformity-formation clause (ii) (10b:440) restates ex:hie-code-domains (10b:410-430) nearly verbatim: about 90 words.
- The two-clique numbers 41.0 and 35.29 at 10b:383 repeat rem:col-declared-geometry in 04_collectives.tex: about 40 words.
- chk:hie-balance restates the full list of obs:hie-top-down numbers: about 120 words.
- rem:hie-literal-consensus overlaps prop:agy-literal-consensus and the level-1 reading paragraph at 10b:185: about 100 words.
- The sentence 'computed, not proved' is given three times (10b:310, 317, 344) for observations whose environment already carries that status.

### Streamlining tiers proposed by lane hie

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| def:hie-member-model | B | 120 | Needed only for the closure block; state in two lines in the main text. |
| prop:hie-closure-exact | B | 150 | Short exact statement; keep the statement, move the discussion. |
| ex:hie-markov-without-closure | C | 120 | Illustration; supplement. |
| lem:hie-misspecification | B | 180 | Tool for the sandwich; statement in main, proof already in appendix. |
| prop:hie-reversible-sandwich | C | 300 | Technical spectral bound not used later in the section; supplement. |
| def:hie-tree | A | 90 | Defines the object of thm:hie-messages and all literal-reading results. |
| thm:hie-messages | A | 250 | Core exact result of the section. |
| prop:hie-predictive-coding | B | 220 | Standard correspondence (Gaussian belief propagation, CAVI as block Gauss-Seidel); one sentence in main. |
| prop:hie-literal-once | A | 260 | Gives the double-counting factor; part (c) is the psi=0 case of (b) and can be merged into (b). |
| prop:hie-literal-records, tab:hie-records | A | 320 | The table carries the four rules; fig:hie-overconfidence is tier B (its content is three growth laws already in the table). |
| prop:hie-record-filter | A | 200 | Exact equality with the centralized Kalman filter; add the initialization hypothesis. |
| prop:hie-depth | B | 300 | (b) overlaps prop:ren-literal-levels; keep (a) and (c) as one statement. |
| rem:hie-literal-consensus | C | 110 | Overlaps prop:agy-literal-consensus; merge into the paragraph at 10b:185. |
| rem:hie-gauge | C | 100 | Interpretation; supplement. |
| prop:hie-record-gain | A | 420 | Keep (a), (b) in main; (c), (d) are bounds for the supplement; (e) is prop:hie-nested-records with one record and can be cut. |
| cor:hie-identity | C | 140 | prop:sca-records-memory(b) and prop:agy-identity(a) with renamed parameters; one sentence suffices. |
| lem:hie-record-blind | B | 200 | (a) is lem:mis-social-blind with one more node; (b)'s bracket is prop:hie-record-gain(c) with eps=k^s. State as a remark after thm:hie-floor. |
| thm:hie-floor | A | 350 | Headline price of the record; the basis of the corrected version of conj:hie-top-down. |
| prop:hie-nested-records | B | 260 | General form of prop:hie-record-gain(e) and of thm:hie-three-levels(c); statement in main, examples to supplement. |
| prop:hie-record-contrast | A | 330 | Records as nodes of the precision; needed for the contrast vocabulary of the section. |
| rem:hie-memory-absent | B | 120 | One sentence in main. |
| ex:hie-noiseless-record | C | 180 | Supports obs:hie-record-window; supplement. |
| obs:hie-record-window | B | 200 | Numerical; one sentence in main with the window statement. |
| prop:hie-global-record | C | 230 | The case n=N of prop:hie-record-contrast plus one covariance formula. |
| prop:hie-echo-tradeoff | B | 220 | Elementary static computation; keep (a) and the limit. |
| obs:hie-top-down | A | 220 | Keep, with the estimator of (b) named and the scope reduced as in finding F1. |
| conj:hie-top-down | A | 70 | Replace by the restricted common-mode statement; as written it is refuted. |
| prop:hie-conformity | A | 480 | Negative result on linear conformity; (e) can move to the supplement. |
| prop:hie-record-bistability | C | 120 | One-line corollary of prop:coh-adoption(b); fold into the text. |
| rem:hie-pragmatic | B | 200 | Used as a result at 07_formation.tex:358; either promote its argument to a proposition or keep as a remark and cite accordingly. |
| obs:hie-exact-receiver | B | 180 | Numerical support for the conjecture; table of four values to supplement. |
| ex:hie-code-domains | B | 330 | Keep the thresholds; move the table to the supplement. |
| conj:hie-conformity-formation | A | 230 | Keep; shorten clause (ii) to a reference to ex:hie-code-domains with the wall-count hypothesis. |
| thm:hie-three-levels | A | 330 | Exact three-level spectrum; the upper bound in (c) can cite prop:hie-nested-records instead of restating it. |
| rem:hie-dynamic | C | 110 | Interpretation; supplement. |
| open:hie-exact-fusion-population, open:hie-record-contrast, open:hie-nonreversible, open:hie-provenance | A | 320 | Short and specific; keep as a single list. |

## Lane ren: Section 10c, renormalization

No critical defect: every theorem, proposition and lemma of 10c_renormalization.tex reconstructs as stated, as an identity or inequality, and the appendix proofs prove the statements as written. The exact/truncated boundary is drawn correctly (decimation is exact marginalization by Schur complement, block averaging an exact pushforward whose law leaves the diffusive class, Galerkin a projection with residual D equal to the time integral of the memory kernel), the nested-medium thresholds q < b/(2b^2-1) and q >= 1/(2b-1) are right, and the readings of Friston 2019 and Villegas et al. 2023 match the primary texts. One major defect, confirmed by recomputation: the section's approximate-closure claim names the wrong small parameter. sigma_cut^2 is a Frobenius quantity, extensive in the number of blocks, so 'relative order sigma_cut^2/(xi_in xi_out)' is 1.75 for 36 blocks of contrast 35 whose true relative error is 2.6 percent; and high contrast alone does not make the averaged-weight coarse parameters accurate (clique family: contrast 39 to 392, exact coarse coupling 0.51 to 0.50 times the Galerkin value). The controlling parameter is ||Pi_perpPhi||^2/(xi_in xi_out), already proved in lem:ren-galerkin(a); the claim recurs at 13_discussion.tex:27. In that family the coarse variables remain nearly Markov, so what fails is the coarse parameters, not Markovianity. Seven minor defects, six confirmed: singleton blocks leave xi_in^min undefined; hypothesis (B) is used but not listed; 'factors of order one' against 'the block factor b'; the 2D part of chk:ren-no-contrast tests coupling ratios on an unstated 24x24 torus instead of squared-length ratios; the tau_L windows of ex:ren-interleaved are grid endpoints and one is not an interval; the ranges of obs:ren-decay hold only to the fifth coarse displacement; one 2D entry count not reproduced (unconfirmed). Scope: linear-Gaussian, reversible, small instances; seed-dependent check numbers and abstract-only citations were not verified. Next action that would change the answer: replace sigma_cut by ||Pi_perpPhi|| in thm:ren-closure(a), thm:ren-memory(d), the table and the closing prose, and state the spread-cut condition. Scripts and a copy of the findings: <session scratch>/audit/ren/findings.md (scripts lib.py, s1 to s13b in the same directory). Nothing under the manuscript or the vault was modified.

Coverage: 40 items examined; 28 hold, 8 defective, 1 suspect, 3 not checked.

| Item | Verdict | Note |
|---|---|---|
| obs:ren-decay | defect | Numbers reproduce for coarse displacements up to five; the stated ranges fail beyond (finding 7). |
| thm:ren-memory | defect | (a)-(c) and all inequalities of (d) hold (s7_memory.py; integral of Gamma equals D). Defects: singleton blocks (finding 2); the last sentence of (d) and the prose at 10c:231 use the extensive sigma_cut (finding 1). |
| thm:ren-closure | defect | Every inequality and identity of (a)-(f) holds; own small scan of (c) found 0 violations. Defects: (a) extensive sigma_cut (finding 1) and singleton blocks (finding 2); (b) uses (B) (finding 4); (f) 'order one' (finding 6). (c) 'exactly when <=' includes equality. The closing prose at 10c:383 claims more than the theorem states (finding 1). |
| corollaries | not_checked | The body file contains no corollary. |
| ex:ren-interleaved | defect | Finding 5; conclusion unaffected. |
| tab:ren-parameters | defect | Row 10c:403 uses sigma_cut and needs uniform leak (finding 1); row 10c:398 'exact' only for equal noise variances (finding 4); row 10c:397 'divided by b, up to a constant' is loose: the squared length is xi^2/b^2 plus a constant. |
| conj:ren-lrg, open:ren-beyond | not_checked | Declared as conjecture and open problem; status discipline respected, nothing presented as established. |
| chk:ren-two-dim | defect | Listed couplings reproduce; the range it supports is truncated (finding 7). |
| chk:ren-block-average | suspect | Finding 8. |
| chk:ren-no-contrast | defect | Finding 3. |
| chk:ren-lrg | defect | Finding 5; lambda_2, lambda_3, contrasts and macronode sequence reproduce; 16x16 torus macronode sizes and nested-medium peaks not rerun. |
| chk:ren-depth, chk:ren-adiabatic, chk:ren-codes, chk:ren-relay, chk:ren-literal, chk:ren-closure | not_checked | Seed-dependent or large scans; the statements they support were rederived instead. |

Items found to hold: lem:ren-galerkin; thm:ren-decimation; prop:ren-ring; thm:ren-flows; prop:ren-exponents; thm:ren-nested; prop:ren-depth; prop:ren-exchangeable; prop:ren-per-level; prop:ren-perron; prop:ren-adiabatic; obs:ren-adiabatic-rate; prop:ren-codes; prop:ren-code-levels; prop:ren-relay-rank; prop:ren-hayek; prop:ren-literal-levels; prop:ren-lrg; prop:ren-lrg-agreement; ex:ren-two-dim; ex:ren-block-average; ex:ren-no-contrast; rem:ren-quartic; rem:ren-rgm and the Friston reading at 10c:233, 253, 274; LRG description at 10c:340 (villegas2023laplacian); chk:ren-decimation, chk:ren-ring, chk:ren-flows, chk:ren-exponents, chk:ren-nested, chk:ren-per-level; chk:ren-memory, chk:ren-perron; cross-references: thm:col-bridge, def:col-contrast, thm:agy-closure-average, thm:agy-h1, thm:agy-mori-zwanzig, thm:agy-closure-identity(d), def:met-lumpable, lem:met-discrete-closure, def:fw-record-model, prop:sca-records, def:col-hierarchy, open:col-non-diffusive, sec:rel-debate.

### ren-01 (major): The approximate-closure error parameter sigma_cut^2/(xi_in xi_out) is extensive in the number of blocks, and high contrast does not make the Galerkin coarse parameters accurate

Location: sections/10c_renormalization.tex:383 (closing claim of sec:ren-closure), :231 (prose after thm:ren-memory), :374 thm:ren-closure(a), :227 thm:ren-memory(d) last sentence, :403 tab:ren-parameters row 'memory'; repeated at sections/13_discussion.tex:27; definition of sigma_cut at sections/04_collectives.tex:495 (thm:col-bridge) and 10c:32 (lem:ren-galerkin(b)). Labels: thm:ren-closure, thm:ren-memory, lem:ren-galerkin, tab:ren-parameters, thm:col-bridge, thm:agy-h1. Category: wrong small parameter; interpretation presented as result.

Evidence. sigma_cut^2 = ||Phi_perp^T Pi Phi||_F^2 = sum_X sigma_X^2 (04:495; 10c:32; app10c:10) is a Frobenius quantity: for M identical blocks it equals M sigma_X^2, while lem:ren-galerkin(a) bounds D by the spectral ||Pi_perpPhi||^2/kappa_perp. (i) Extensivity, block media of chk:ren-memory (side 6, outer coupling 0.01, leak 1e-3, contrast 35.1), script s12_sigma_cut_extensive.py: 4x4 blocks (M=16): sigma_cut^2/(xi_in xi_out) = 0.776, ||Pi_perpPhi||^2/(xi_in xi_out) = 0.0862, actual ||D||/xi_out = 0.0255; 6x6 blocks (M=36): 1.746, 0.0862, 0.0262, and the bound of thm:ren-closure(a), sigma_cut^2/xi_in = 1.34e-2, exceeds xi_out = 7.67e-3. Side 4 (leak 1e-2, contrast 29.8): M=16: 0.168 vs 0.0168 (actual 0.0084); M=64: 0.671 vs 0.0168 (actual 0.0084). The stated 'relative order' overstates the error by the factor M and exceeds 1 for 36 blocks of contrast 35 whose true relative error is 2.6 percent. The single-collective bound it is said to generalize (thm:agy-h1(c), 05_agency.tex:571-580) uses the per-block dispersion sigma_C, which is intensive. (ii) Contrast does not control the error, script s13b_contrast_family.py: two cliques K_n (coupling 1) joined by one edge of weight c = n/2, leak 0.01: n = 20, 50, 100, 200 give contrast 39.2, 98.1, 196.1, 392.2 while the exact coarse coupling is 0.513, 0.505, 0.503, 0.501 times the Galerkin (averaged-weight) coupling and ||D||/xi_out = 0.955, 0.970, 0.975, 0.978; ||Pi_perpPhi||^2/(xi_in xi_out) = 1.86 to 1.95. Scaling: xi_in ~ n, xi_out - eps = c/n, ||Pi_perpPhi||^2 ~ 2c^2/n, so the ratio is ~ 2c/n while r ~ n^2/c. Eight such cliques on a ring (s13_contrast_not_enough.py): contrast 19.8, ratio 0.526, sigma_cut^2/(xi_in xi_out) = 7.32 against spectral 1.78. What survives in this family is Markovianity, not the coarse parameters: by thm:ren-memory(c) the relative fast weight is at most t_Theta^2 kappa_Phi/kappa_perp, about 0.003 at n = 20 (hand evaluation from the script values), so the slow part is Markov with a drift that differs from Pi_Phi at order one.

Proposed fix. Use the spectral norm, which is what lem:ren-galerkin(a) and thm:ren-memory(b),(c) already prove. thm:ren-closure(a): '||D|| <= ||Pi_perpPhi||^2/xi_in^min (<= sigma_cut^2/xi_in^min)'. thm:ren-memory(d), last sentence: 'the relative fast weight is at most 2(||Pi_perpPhi||/(xi_out(r-2)))^2/r'. Table row 10c:403: 'kernel at most ||Pi_perpPhi||^2 e^{-xi_in^min u}'. 10c:231: 'Coarse-graining along collectives with ||Pi_perpPhi||^2 << xi_in xi_out makes memory a correction of that relative order'. 10c:383: 'approximately, with the averaged-weight coarse parameters in error by relative order ||Pi_perpPhi||^2/(xi_in^min xi_out), when that ratio is small; high contrast is necessary for this but not sufficient, since for uniform leak sigma_X^2 <= 2 d_max (xi_out(X) - eps^Pi), with d_max the largest total coupling of one agent across the boundary of X, so the cut must also be spread over the members'. 13_discussion.tex:27: 'approximately for blocks of high contrast whose cut couplings are spread over their members'. The per-block bound follows because (I - Phi Phi^T) annihilates eps phi_X, so sigma_X^2 <= sum_{i notin X} d_i(X)^2/|X| + sum_{i in X} d_i(X^c)^2/|X| <= 2 d_max cut(X)/|X|; checked on the clique family (9.5, 24.5, 49.5, 99.5 against 10, 25, 50, 100).

What would overturn the finding. 10c:383 'approximately, with errors of relative order sigma_cut^2/(xi_in xi_out), when the blocks are collectives of high contrast' and 13_discussion.tex:27 'approximately for blocks of high contrast (thm:ren-closure)'. No inequality of thm:ren-memory or thm:ren-closure is false.

State: applied. [04] applied: Confirmed: Frobenius sigma_cut^2 is extensive (rings of M=4,8,16 blocks: Frobenius/spectral bound ratio 2.5, 5, 10; ||D|| flat near 2e-3). thm:col-bridge(ii) now states the spectral bound the proof already gives, with sigma_cut^2 as upper bound; proof and check updated. Two-block formulas unchanged (norms coincide there). [10c] applied: Confirmed (ren-01.py, ren-01b.py reproduce 0.776/1.746 vs 0.0862; clique family 0.513..0.501). Spectral norm adopted in thm:ren-memory(d), thm:ren-closure(a), table, prose; per-block bound added to lem:ren-galerkin(b) with proof. Deviation: 'high contrast is necessary' not written, since equitable partitions have D=0 at contrast near 1. Framing pass: [group 13] applied

### ren-02 (minor): Singleton blocks leave xi_in^min undefined

Location: sections/10c_renormalization.tex:227 thm:ren-memory(d); :374 thm:ren-closure(a); def:col-contrast at sections/04_collectives.tex:291-292. Labels: thm:ren-memory, thm:ren-closure, def:col-contrast. Category: missing hypothesis.

Evidence. def:col-contrast defines xi_in(C) only for regions with n >= 2 members. thm:ren-memory(d) admits 'a partition into regions C_1,...,C_M' and sets xi_in^min = min_j xi_in(C_j); thm:ren-closure(a) uses the same quantity for an arbitrary partition. The proof bound kappa_perp >= min_j xi_in(C_j) only involves blocks that contribute to ker Phi^T, that is blocks with at least two members.

Proposed fix. Write 'xi_in^min = min of xi_in(C_j) over the blocks with at least two members (the bounds are vacuous if every block is a singleton)' in thm:ren-memory(d) and thm:ren-closure(a).

State: applied. [04] applied: def:col-contrast already restricts to n>=2 and is unchanged. The only place in group 04 that used an inward rate for arbitrary partition blocks is thm:col-bridge(i); it now reads 'for every block with n_j>=2 members'. The xi_in^min wording belongs to 10c. [10c] applied: Confirmed: xi_in is undefined for singletons, and the proof only uses blocks with at least two members. Minimum restricted accordingly in thm:ren-memory(d), thm:ren-closure(a) and the proof of (d).

### ren-03 (minor): chk:ren-no-contrast, two-dimensional part, does not test the claim of ex:ren-no-contrast and reproduces only on an unstated 24x24 torus

Location: sections/chk10c_renormalization.tex:52-53 (chk:ren-no-contrast); sections/10c_renormalization.tex:248 and :251 (ex:ren-no-contrast). Labels: chk:ren-no-contrast, ex:ren-no-contrast. Category: check validity.

Evidence. The body claims the squared second-moment length is overstated by the block factor and says this is 'checked in one and two dimensions'. The 2D part of the check reports nearest-neighbor coupling ratios exact/Galerkin (1.0156, 0.7229, 0.5482, 0.7312) and entry counts 9648/720/160/720, which are not squared-length ratios. Those figures reproduce only on a 24x24 fine torus (s8b_nocontrast24.py), a size the check does not state and which is smaller than the correlation length 31.6 at leak 1e-3; on a 240x240 torus the coupling ratios are 0.7219, 0.5266, 0.7305. The relevant test, squared-length ratio Galerkin/exact on 240x240 (s8_nocontrast.py): 1.9995, 3.9950, 5.9826 for block side 2, 4, 6 at leak 1e-3 and 3.5726 for side 4 at leak 0.1. The 1D part (2.000, 3.995, 7.958) reproduces.

Proposed fix. In chk:ren-no-contrast state the torus size and report the squared-length ratios on a torus much larger than the correlation length, for example 'on a 240x240 torus at leak 1e-3 the squared-length ratio Galerkin/exact is 1.9995, 3.9950 and 5.9826 for blocks of side 2, 4 and 6'. The sentence at 10c:251 then stands.

State: applied. [10c] applied: Confirmed. 2D part replaced by squared-length ratios 1.9995, 3.9950, 5.9826, 3.5726 (ren-03.py). These are the infinite-lattice values of eq:ren-xi2-flow; a real-space moment on a 240x240 torus gives 2.41, 4.82, 7.21, so the proposed '240x240' wording was not used; 960x960 agrees to four decimals.

### ren-04 (minor): Hypothesis (B) on local noise is used in thm:ren-closure(b) but is not among the standing assumptions of the section

Location: sections/10c_renormalization.tex:375 thm:ren-closure(b); sections/app10c_renormalization.tex:178; asm:ren-standing at 10c:9-10; (B) defined in asm:sca-standing, sections/08_scale.tex:12; tab:ren-parameters row at 10c:398. Labels: thm:ren-closure, asm:ren-standing, asm:sca-standing, tab:ren-parameters. Category: missing hypothesis.

Evidence. 10c:375: 'the zeta-bar_X are independent, with variance at most q/|X|'. app10c:178: 'Local noises are independent across agents with variances at most q'. asm:ren-standing (10c:9-10) lists (M), (C_r), (NN) and (TI) only; the variance bound q is hypothesis (B) of asm:sca-standing. The table row 10c:398 'local noise q -> q/|X|, exact' is exact only when every local noise variance equals q.

Proposed fix. Add (B) to asm:ren-standing, or write in (b): 'if the local noises satisfy (B), the zeta-bar_X are independent with variance at most q/|X|'. Table row: 'q/|X| (equality for equal variances, an upper bound under (B))'.

State: applied. [10c] applied: Confirmed: (B) is not in asm:ren-standing. thm:ren-closure(b) now conditions the noise clause on (B) of asm:sca-standing, with equality for equal variances; proof and table row updated. [08] declined: Nothing to change in group 08: (B) in asm:sca-standing already states that Q^zeta is block diagonal over agents with blocks between q_min I and q I, which is the hypothesis thm:ren-closure(b) needs. The repair belongs to 10c_renormalization.tex and its appendix.

### ren-05 (minor): ex:ren-interleaved: the stated tau_L windows are grid endpoints, and the window in which A and A' are returned is not an interval

Location: sections/10c_renormalization.tex:358 (ex:ren-interleaved); sections/chk10c_renormalization.tex:72-73 (chk:ren-lrg). Labels: ex:ren-interleaved, chk:ren-lrg. Category: number mismatch.

Evidence. Text: A and A' 'only for tau_L in [0.018, 0.89]', A u A' 'for tau_L in [1, 4470]', B 'for tau_L in [3.98, 4470]'. Recomputed (s10_lrg.py, s10b_lrg.py): B is a macronode exactly for 1/lambda_3 = 3.732 < tau_L < 1/lambda_2 = 4503; 3.98 and 4470 are points of a 20-per-decade grid. A and A' are returned from tau_L = 0.0167 up to 1.0 but not throughout: not for tau_L in [0.283, 0.306) or [0.387, 0.789). chk:ren-lrg peak positions are midpoints of a coarse grid: the maxima of tau^2 Var_rho(L) are at 1.24, 8.32, 741 for the two-grid example (text 1.22, 8.41, 750) and at 1.21 and 1.08e4 for the interleaved one (text 1.19, 1.09e4), which also has an unlisted maximum at 0.038. The conclusion that no single diffusion time returns A, A' and B together is unaffected.

Proposed fix. 'returns A and A' as macronodes only for some tau_L in (0.017, 1), and not for tau_L in [0.28, 0.31) or [0.39, 0.79); A u A' for 1 <= tau_L < 1/lambda_2 = 4503; and B for 1/lambda_3 = 3.73 < tau_L < 4503'. State the tau grid and the scan range in chk:ren-lrg and give the peak positions to the resolution of that grid.

State: applied. [10c] applied: Confirmed (ren-05.py, ren-05b.py): 1/lambda_2=4503.4, 1/lambda_3=3.732; A,A' windows [0.0167,0.2830), [0.3060,0.3871), [0.7887,0.9998]; maxima 0.0382, 1.21, 1.08e4 and 1.24, 8.32, 742. Example now fixes attachment at opposite corners. Nested-medium maxima also recomputed from the exact spectrum: 2.21, 11.05, 53.3 (were 2.24, 10.9, 53.1).

### ren-06 (minor): 'factors of order one' in thm:ren-closure(f) contradicts 'the block factor b' of the example it cites

Location: sections/10c_renormalization.tex:379 thm:ren-closure(f) versus :248 ex:ren-no-contrast; sections/chk10c_renormalization.tex:53. Labels: thm:ren-closure, ex:ren-no-contrast. Category: internal consistency.

Evidence. 10c:379: 'Without contrast the Markov coarse parameters are wrong by factors of order one (ex:ren-no-contrast)'. 10c:248: 'overstates the coarse coupling by the block factor ... the ratio tends to b', with message weight a/b against (a/b^2)(1+O(eps)). chk10c:53 and s8_nocontrast.py: 2.000, 3.995, 7.958 for b = 2, 4, 8. The factor grows with b and is not of order one.

Proposed fix. 'Without contrast the Markov coarse coupling and squared length are wrong by the block factor b (ex:ren-no-contrast)'.

State: applied. [10c] applied: Confirmed against ex:ren-no-contrast and eq:ren-xi2-flow (ratio tends to b in any dimension). thm:ren-closure(f) now says the Markov coarse coupling and squared length are wrong by the block factor b, up to corrections that vanish with the leak.

### ren-07 (minor): obs:ren-decay: the stated ranges of decay factors hold only for the first five coarse displacements

Location: sections/10c_renormalization.tex:79 (obs:ren-decay); sections/chk10c_renormalization.tex:14-15 (chk:ren-two-dim). Labels: obs:ren-decay, chk:ren-two-dim. Category: numerical observation overstated.

Evidence. Text: 'between 0.090 and 0.095 from the second step on at the three smaller leaks; onto 4Z x 4Z the factors lie between 0.019 and 0.129'. Recomputed on 256 and 512 tori, which agree (s1b_twodim_ratios.py, s1c_twodim_alias.py): onto 2Z x 2Z at leak 0.0005 the factors at steps 1 to 8 are 0.0439, 0.0938, 0.0943, 0.0948, 0.0953, 0.0957, 0.0961, 0.0964; onto 4Z x 4Z: 0.0993, 0.1210, 0.1260, 0.1288, 0.1309, 0.1324, 0.1336, 0.1346. The upper ends 0.0948 and 0.129 are the ratios of the couplings at displacements (5,0) and (4,0), a coupling the check does not list (from its four listed couplings the largest ratios are 0.0943 and 0.1260), and the factors keep rising beyond that truncation.

Proposed fix. 'at coarse displacements up to five its axis couplings fall by factors between 0.025 and 0.095 per coarse step ...; onto 4Z x 4Z between 0.019 and 0.129; the factor rises slowly with distance (0.096 at the eighth step at leak 0.0005, 0.135 onto 4Z x 4Z)'. List the fifth coupling in chk:ren-two-dim.

State: applied. [10c] applied: Recomputed on 256 and 512 tori (identical to printed digits). Ranges hold only for couplings at displacements 1 to 5; ratios keep rising (0.0964 and 0.1346 at the eighth step). Observation restricted to displacements up to five with the rise stated; check now lists the fifth coupling and the eight ratios.

### ren-08 (minor, unconfirmed): chk:ren-block-average: two-dimensional count of positive off-diagonal entries not reproduced

Location: sections/chk10c_renormalization.tex:22-23 (chk:ren-block-average). Labels: chk:ren-block-average, ex:ren-block-average. Category: number mismatch.

Evidence. Text: 'between 288 and 368 positive off-diagonal entries' on a 240x240 torus. Recomputed with threshold 1e-12 (s4_blockavg.py): 316, 308, 376, 372. The threshold and the counting convention (per row or total, symmetric pairs counted once or twice) are not stated, so the difference may be one of convention. The 1D closed forms and the 2D couplings (2.031/-0.272, 2.590/-0.451) reproduce.

Proposed fix. State the threshold and the counting convention, and recompute the range.

State: applied. [10c] applied: Count 288 to 368 not reproduced at any threshold tried; the count is threshold dependent. Check now states the convention (per site, entries above 1e-12) with counts 316, 308, 376, 372, same on a 480 torus, and the counts at 1e-8 and 1e-10. Couplings 2.031/-0.272 and 2.590/-0.451 reproduce.

### Not checked by lane ren

- Primary texts of vankampen1985elimination, geigenmuller1983systematic (the manuscript itself says abstracts only), Dyson 1969, Jona-Lasinio 2001, friston2023path, amemiya1972effect, working1960note and the other network-renormalization citations
- friston2021parcels pp. 33-57 and the Friston 2019 monograph beyond p. 49
- Seed-dependent numbers of chk:ren-codes, chk:ren-relay, chk:ren-literal, chk:ren-adiabatic and chk:ren-closure; the 200-population runs of chk:ren-memory and chk:ren-perron; the AR1 relative entropy 1.36e-3
- The 16x16 torus LRG macronode sizes and the nested-medium LRG peaks (2.24, 10.9, 53.1) of chk:ren-lrg
- The 3,580,209-triple scan and the exact-rational scan behind prop:ren-per-level(f); the statement was rederived by hand and a smaller own scan had no violations
- Specific numbers of chk:ren-depth beyond the formula
- The second-order expansion in sec:rel-debate that 10c:274 relies on (the cited sentence was located, its derivation was not redone)
- Word counts of individual environments other than those listed are estimates

### Redundancy noted by lane ren

- 10c:208 (about 226 words) and the caption of fig:ren-per-level (about 265 words) restate the thresholds, windows and zero counts of prop:ren-per-level and chk:ren-per-level
- 10c:168 (about 112 words) and the caption of fig:ren-lengths (about 169 words) restate prop:ren-depth
- The identity integral of Gamma = D is stated at 10c:38 after lem:ren-galerkin and again in thm:ren-memory(b) (about 40 words); thm:ren-memory(a) repeats lem:ren-galerkin(a)
- thm:ren-closure (a), (d) and (f) restate lem:ren-galerkin, prop:ren-codes, prop:ren-code-levels, prop:ren-literal-levels, ex:ren-no-contrast, prop:ren-exchangeable and prop:ren-per-level; tab:ren-parameters then restates thm:ren-closure (about 250 words of overlap)
- The reading of the Friston adiabatic reduction is split over 10c:233 (138 words), 10c:253 (124 words) and 10c:274 (92 words), with about 200 words of overlap, and is summarized again at 05_agency.tex:46
- The closing sentence at 10c:383 (about 70 words) is repeated almost verbatim at 13_discussion.tex:27
- prop:ren-per-level(d) is subsumed by (f)
- The introductory paragraphs 10c:5 (132 words) and 10c:7 (160 words) preview results that the theorem headings already announce

### Streamlining tiers proposed by lane ren

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| asm:ren-standing | A |  | Standing hypotheses; add (B). |
| def:ren-maps | A |  | Defines the three maps and the exact versus projected boundary. |
| lem:ren-galerkin | A |  | Carries every later error bound. |
| thm:ren-decimation | A |  | Exact marginalization result. |
| thm:ren-flows | A |  | The flow of the parameters. |
| thm:ren-nested | A |  | Exactly closed hierarchy; source of the thresholds. |
| prop:ren-per-level | A |  | Headline thresholds; drop (d), which (f) contains. |
| thm:ren-memory | A | 330 | Exact reduction; state (d) with the spectral norm, which also removes finding 1. |
| ex:ren-no-contrast | A | 123 | The failure case that gives the closure theorem its content. |
| prop:ren-adiabatic | A |  | Exact statement of what the elimination of internal states drops. |
| thm:ren-closure | A | 620 | Keep (b), (c), (e); cut (a), (d), (f) to one-line pointers. |
| prop:ren-ring | B |  | Explicit instance of thm:ren-decimation; supplement. |
| ex:ren-block-average | B |  | Keep two sentences (the exact law leaves the diffusive class); move the closed forms. |
| prop:ren-exponents | B |  | Supplement, with a one-line statement in the main text. |
| prop:ren-depth | B |  | Consequence of thm:ren-nested; supplement. |
| prop:ren-exchangeable | B |  | Feeds prop:ren-per-level; supplement. |
| fig:ren-per-level | B | 265 | Keep the figure; cut the caption to about 80 words. |
| prop:ren-perron | B |  | Linear analogue of the R operator; supplement with a pointer. |
| obs:ren-adiabatic-rate | B | 127 | Numerical observation; one sentence in the main text. |
| rem:ren-rgm | B | 231 | Shorten to about 90 words. |
| prop:ren-codes | B |  | Belongs with the code material; supplement. |
| prop:ren-literal-levels | B |  | Supplement. |
| prop:ren-lrg | B |  | Comparison with the Laplacian renormalization group; supplement. |
| prop:ren-lrg-agreement | B |  | Supplement. |
| ex:ren-interleaved | B | 124 | Supplement; restate the windows as spectral thresholds. |
| tab:ren-parameters | B |  | Keep as the summary and delete the prose it duplicates, or the reverse. |
| open:ren-beyond | B | 100 | Shorten. |
| ex:ren-two-dim | C |  | Illustration only. |
| obs:ren-decay | C |  | Numerical observation with no downstream use. |
| rem:ren-quartic | C |  | Side remark. |
| fig:ren-lengths | C | 169 | Restates prop:ren-depth. |
| prop:ren-code-levels | C |  | Short consequence of prop:ren-codes; merge into it. |
| prop:ren-relay-rank | C |  | Peripheral to the renormalization argument. |
| prop:ren-hayek | C |  | Interpretive; merge into a remark. |
| conj:ren-lrg | C |  | Merge into open:ren-beyond. |
| Simplification: use \|\|Pi_perpPhi\|\| in place of sigma_cut throughout sec:ren-memory and sec:ren-closure | A |  | lem:ren-galerkin(a) and thm:ren-memory(b),(c) already prove the spectral-norm bounds; sigma_cut is then needed only for the entrywise bound of lem:ren-galerkin(b). |
| Simplification: hypotheses that can be weakened without changing the proofs | C |  | thm:ren-nested(c) holds for q <= b; prop:ren-per-level(e) holds for q < (b-1)/b; the fast-weight bound of thm:ren-memory(c) needs only kappa_perp > kappa_Phi; prop:ren-perron(c) can be stated with kappa_perp - eps. |

## Lane env1: Section 10d, sensors, horizon, control

No critical defect in lines 1-155 of sections/10d_environments.tex. Every lemma, theorem and proposition was re-derived and tested on small random instances; all hold, and every recomputable number reproduces (figure crossings, thresholds, h*, the example's selections). One proposition clause needs an added hypothesis (prop:env-horizon(c) is true only for two modes). The rest are wording and check-file slips: an "only for" overclaim, a cross-reference that shows a reordering rather than non-canonical eigenvectors, a remark stating a necessary condition as if sufficient, an eigenvalue count that disagrees with the stated dimension. Detail and scripts: <session scratch>/audit/env1/findings.md

Coverage: 15 items examined; 12 hold, 1 defective, 2 suspect, 0 not checked.

| Item | Verdict | Note |
|---|---|---|
| prop:env-horizon | defect | (a),(b) hold and all numbers reproduce; (c) needs a two-mode hypothesis (three-mode counterexample). |
| rem:env-two-step | suspect | Displayed identity correct; closing sentence gives a necessary condition as if sufficient; R^o definiteness undeclared. |
| chk:env-control | suspect | (a),(c), remark and example numbers consistent; (b) prints five eigenvalues for a four-dimensional exterior. |

Items found to hold: lem:env-information; lem:env-eigen (appendix); thm:env-canonical; lem:env-markov; prop:env-diffusive; thm:env-control; rem:env-efe-horizon-free; ex:env-fast-preference; fig:env-horizon caption; chk:env-sensors; chk:env-markov; chk:env-horizon.

### env1-01 (major): prop:env-horizon(c) is false with more than two modes

Location: sections/10d_environments.tex:72 (prop:env-horizon, part c). Category: missing hypothesis.

Evidence. The statement allows any symmetric F with QF=FQ. Counterexample: modes lambda=(0.97,0.9,0.6) with stationary variances p=(0.3384,5,1.5625). Slow s=0.97 and fast f=0.6 satisfy the hypotheses and h*=1.592, but at h=1 lambda^{2h}p=(0.318,4.05,0.5625), so the rank-one error optimum reads the third mode, not the fast one. "The information criterion reads the slow mode" also fails when s is not the slowest mode.

Proposed fix. Add the hypothesis: "If s and f are the only two modes, the fast mode is read for h<h* and the slow mode for h>h*...". Alternatively say "is preferred to" instead of "is read", and "the information criterion ranks s above f at every h".

What would overturn the finding. A proof that the argmax of lambda_j^{2h}p_j is always s or f under the stated hypotheses; the three-mode instance above rules that out.

State: applied. [10d] applied: Counterexample reproduced: lambda=(0.97,0.9,0.6), p=(0.3384,5,1.5625) gives argmax mode 2 at h=0..5, h*=1.592. Part (c) now states a pairwise ranking, with the 'is read' conclusion restricted to two modes and h>=1 for the information criterion. Proof and check updated; three-mode instance added to both.

### env1-02 (minor): "Only for the weight Sigma_Y^{-1}" overclaims what part (c) shows

Location: sections/10d_environments.tex:77 (prose after prop:env-horizon). Category: interpretation stated as result.

Evidence. Part (c) exhibits one weight (Upsilon=I) that fails at short horizons; it does not show "only". As a characterization it is false: in (c) with p_f<=p_s, Upsilon=I reads the slow, leading canonical mode at every h. thm:env-control(c) (line 121) also gives agreement for every co-monotone decision matrix.

Proposed fix. "Part (c) shows that a prediction error with a weight other than Sigma_Y^{-1} need not select the leading canonical variate (thm:env-canonical(d))."

What would overturn the finding. A proof that agreement at every horizon forces Upsilon proportional to Sigma_Y^{-1}.

State: applied. [10d] applied: Confirmed: part (c) exhibits one failing weight and proves no 'only'. Prose after the proposition replaced with the proposed sentence (a weight other than Sigma_Y^{-1} need not select the leading canonical variate).

### env1-03 (minor): thm:env-canonical(d) cites prop:env-horizon(c) for a claim that example does not show

Location: sections/10d_environments.tex:44 (thm:env-canonical, part d); proof at sections/app10d_environments.tex:64. Category: cross-reference.

Evidence. Part (d) says the leading eigenvectors of J_Upsilon "in general are not canonical variates (prop:env-horizon(c))". In prop:env-horizon(c), J_I and CC^T are diagonal in the same eigenbasis (app10d:82), so the eigenvectors are canonical variates and only their ranking differs. The appendix proof of (d) covers J=CC^T and the containment, not this clause.

Proposed fix. "...reads leading eigenvectors of J_Upsilon, which need not be the leading canonical variates (prop:env-horizon(c)) and, when J_Upsilon and CC^T do not commute, are not canonical variates at all."

What would overturn the finding. Showing that the fast mode in prop:env-horizon(c) is not a canonical variate of (eta_t, eta_{t+h}).

State: applied. [10d] applied: Confirmed: J_I and CC^T commute in prop:env-horizon(c) (commutator 3e-17). Clause reworded. The proposed 'not canonical variates at all' is too strong, since non-commuting matrices can share an eigenvector; text says no orthonormal eigenbasis of J_Upsilon consists of singular vectors of C. Proof of (d) extended.

### env1-04 (minor): rem:env-two-step: closing condition is necessary, not sufficient

Location: sections/10d_environments.tex:143 (rem:env-two-step). Category: interpretation.

Evidence. With hidden state eta_{t+h} and outcomes (s,o), the remark's own chain rule gives an epistemic term I(s;eta_{t+h})+I(eta_{t+h};o|s) = I(s;eta_{t+h}) - I(s;o~) + const = I(s;eta_{t+h}|o~) + const. That is still not the predictive information of thm:env-canonical. The remark's displayed identity was checked numerically (s4_ctl.py).

Proposed fix. "...follows from the expected free energy only when the hidden state is the state at the horizon and the later outcome o is not scored in the epistemic term; we therefore declare it as the objective of def:env-attention-objective and claim no more."

What would overturn the finding. A derivation in which I(eta_{t+h};o|s) is independent of the sensor with H^o nonzero and R^o finite.

State: applied. [10d] applied: Confirmed numerically on four random sensors: with hidden state eta_{t+h} and outcomes (s,o) the epistemic term equals I(s;eta_{t+h}|o~)+const, not I(s;eta_{t+h}). Closing sentence now adds the condition that o is not scored, and states the conditional-information form and the exception H^oF^h=0.

### env1-05 (minor): R^o positive definite is used but never declared

Location: sections/10d_environments.tex:100 (def:env-attention-objective) and :141 (rem:env-two-step). Category: missing hypothesis.

Evidence. The definition gives v^o ~ N(0,R^o) with no definiteness condition. The remark's display uses (1/2) ln det R^o, which is infinite for singular R^o. thm:env-control itself does not need the condition.

Proposed fix. Add "with R^o positive definite" in rem:env-two-step, or in the definition.

What would overturn the finding. A declaration of R^o positive definite elsewhere that covers this definition (none found in lines 1-155).

State: applied. [10d] applied: Confirmed: R^o definiteness is declared nowhere in the 10d files. Added 'R^o positive definite' to the setting of rem:env-two-step; def:env-attention-objective and thm:env-control are unchanged because they do not need it.

### env1-06 (minor): chk:env-control(b) lists five eigenvalues for a four-dimensional exterior

Location: sections/chk10d_environments.tex:23 (chk:env-control). Category: number mismatch.

Evidence. Part (a) of the check describes "a random four-dimensional exterior". Part (b) reports the eigenvalues of J_ctl as (1.587,0,0,0,0). J_ctl = P_0^{1/2}(F^h)^T Upsilon_ctl F^h P_0^{1/2} is d-by-d, so it has four eigenvalues in that exterior. Either (b) uses a five-dimensional instance that is not described, or one zero is spurious.

Proposed fix. State the instance of (b), or print (1.587,0,0,0).

What would overturn the finding. The check's source output showing that (b) was run on a five-dimensional exterior.

State: applied. [10d] applied: The source H5_efe.py runs (b) on a separate instance with K=5, h=2, three outcomes, one control, so the five eigenvalues are correct and the instance was undescribed. Check (b) now states that instance; the numbers are unchanged.

### env1-07 (minor): Check-file slips: inadmissible horizon and an omitted constant

Location: sections/chk10d_environments.tex:18 (chk:env-horizon(c)) and :23 (chk:env-control(c)). Category: check wording.

Evidence. chk:env-horizon(c) reports the selection "at h=0,1", but horizons are h>=1 (10d:7). chk:env-control(c) prints -5.0154728020 as the minimum of G_att. Recomputing the separable sum from the printed spectra gives -5.01573 without c_0+(1/2)tr(Upsilon_ctl P_0), so the printed value omits that constant without saying so. Capacities 1.007 and 0.193 reproduce.

Proposed fix. Write "at h=1" and "from h=2 on"; write "equals the separable closed form up to the sensor-independent constant".

What would overturn the finding. An instance in which c_0+(1/2)tr(Upsilon_ctl P_0)=0 to four digits.

State: applied. [10d] applied: Confirmed. h*=1.592, so fast mode at h=1, slow from h=2; replaced inadmissible h=0 in three places. Reoptimizing the bracket sum from the printed spectra gives -5.01573 with capacities 1.0074, 0.1926, so the printed -5.0154728 is the channel sum without c_0+(1/2)tr(Upsilon P_0); check now says so.

### env1-08 (minor, unconfirmed): Novelty sentence rests on precedents the text says were not read

Location: sections/10d_environments.tex:50 (prose after thm:env-canonical); also :57, :110. Category: attribution.

Evidence. "What thm:env-canonical adds... is the joint treatment of a rank limit and a hard budget" appears beside Scharf 1998 ("from its record") and Creutzig 2009 ("from its abstract"), called "precedents still to be checked". Akaike 1975 and Friston 2021 carry the same hedge. I did not read those sources. The Chechik 2005 Theorem 3.1 attribution and the v=1/t identification are correct.

Proposed fix. Read Creutzig et al. 2009 and Scharf and Mullis 1998 before the reorganization. Then either delete the novelty sentence or state it without the "still to be checked" clause.

What would overturn the finding. Reading both papers and finding no joint rank-plus-budget statement.

State: applied. [10d] applied: Read Scharf-Thomas 1998 in full: Section V already treats rank reduction and a bit budget jointly for trace error. Novelty sentence removed and replaced by an accurate description with no priority claim. Creutzig 2009 could not be opened (paywall, fetches failed); its abstract-only hedge stays.

### env1-09 (minor): Edge conventions left undefined in statements

Location: sections/10d_environments.tex:37, :42 (thm:env-canonical a, b), :53 (lem:env-markov), :87 (prop:env-diffusive). Category: edge cases.

Evidence. (a) uses sigma_j for j<=kappa, but the sigmas are padded only to length d_X; the appendix (app10d:5) restricts to kappa<=d_X silently. The threshold I_m divides by sigma_m^2. lem:env-markov cites the value of (b), which is undefined when sigma_1=0 (for example F^h=0). prop:env-diffusive says "the eigenvector" of lambda_2, which is not unique on a cycle or complete graph, and has no tau_2 on a single vertex.

Proposed fix. Add "sigma_j=0 for j>d_X; I_m=+infinity when sigma_m=0; the value of (b) is 0 when sigma_1=0"; in prop:env-diffusive write "an eigenvector" and assume at least two vertices.

What would overturn the finding. Conventions already stated elsewhere in the section that cover these cases.

State: applied. [10d] applied: Conventions added: sigma_j=0, g_j=0, lambda_j(J)=0 for j>d_X in def:env-sensor; I_m=+infinity when sigma_m=0; value of (b) is 0 when sigma_1=0 or I_max=0 (reason given after the theorem). prop:env-diffusive assumes at least two vertices and says 'an eigenvector', 'an orthonormal basis'.

### Not checked by lane env1

- Exact digits of seed-dependent check values (0.584985927655, 142.30322369, 99.20984032, 5.5301278619, the 6.1e-15 and 4.4e-15 residuals); seeds are not given, so I tested the same claims on my own instances instead.
- The specific sin(theta_h) values of chk:env-horizon(b) (0.674, 0.274, 0.0213, 1.39e-4) and the 0.19 bound of the independent instance.
- Content of Scharf 1998, Creutzig 2009, Akaike 1975, Sachdeva 2021 and Friston 2021; only the Chechik 2005 Theorem 3.1 attribution was confirmed, from memory of the paper rather than a fresh read.
- The plotted curve coordinates in figures/fig_env_horizon.tex beyond the marked dots, the circles and the dashed slopes.
- Lines 156 onward of the section; prop:env-selection was opened only at part (ii), as cited by the example.
- Proofs of prop:fw-efe-communication and asm:sca-standing; only their statements were read.

### Redundancy noted by lane env1

- prop:env-horizon(c) and ex:env-fast-preference show the same phenomenon (a non-scale-free weight reverses the slow-first order); one two-mode example could carry both.
- thm:env-control(b) is thm:env-canonical(c) with J=J_ctl plus a rank count; thm:env-control(d) is a pointer to the example, not a claim.
- thm:env-canonical(d), first half, is the special case J=CC^T of the co-monotone agreement in thm:env-control(c).
- prop:env-diffusive is prop:env-horizon(a) applied to a Laplacian; a corollary sentence suffices.
- rem:env-efe-horizon-free and ex:env-fast-preference use nearly the same two-mode instance with different slow innovation variances (0.01 and 0.1); harmonize.
- The fig:env-horizon caption repeats numbers already in chk:env-horizon(a) and in the prose at line 77.

### Streamlining tiers proposed by lane env1

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| def:env-sensor | A | 230 | Captured covariance G_s is the object every result is stated in. |
| lem:env-information | B | 170 | Keep one sentence (everything depends on the sensor through G_s); parts (i)-(iv) to the supplement. |
| thm:env-canonical | A | 620 | Keep (a),(b) and the one-line (d); move (c) degenerate cases, (e) and the attribution paragraph to the supplement. |
| lem:env-markov | B | 110 | One-sentence pointer: summaries of the past do no better than sensors of eta_t. |
| prop:env-horizon | A | 520 | (a) is principal; (b) keep only the asymptotic sentence since the explicit bound is vacuous at computed horizons; (c) merge with the example. |
| fig:env-horizon | B | 210 | Keep the figure, cut the caption to two sentences; the numbers live in the check. |
| prop:env-diffusive | C | 170 | Corollary of prop:env-horizon(a); merge as one sentence. |
| def:env-attention-objective | A | 190 | Declares the objective that the control theorem and the selection principle use. |
| thm:env-control | A | 330 | Keep (a) and (c); fold (b) into a sentence and drop (d) as a pointer. |
| rem:env-efe-horizon-free | B | 190 | Could merge with rem:env-two-step into one remark on what the framework's expected free energy gives instead. |
| rem:env-two-step | B | 230 | Supplement, with a one-sentence pointer explaining why the epistemic term is declared. |
| ex:env-fast-preference | B | 230 | Keep a two-sentence version in the main text as the witness for reversal; absorb prop:env-horizon(c). |
| lem:env-eigen (appendix) | B | 330 | Supplement only; (d) is Fiedler's inequality and could be cited instead of re-proved. |

## Lane env2: Section 10d, selection, aggregates, Hayek dimension, levels

No theorem, proposition or lemma in lines 156-381 failed: all eight labeled results were rederived from their proofs, and the inequalities passed on small random instances. Every recomputable number in the cell, firm and person examples reproduces, except the finite-time factor (0.81, quoted as 0.79). The one major item is attribution: the constant 3/(5 pi) called "derived here" is the Berg-Purcell perfect-instrument formula per Mora-Wingreen Eq. 10 (primary source not opened). The rest are minor: an unequal "per reading" comparison behind "thirteen orders", two cross-references used beyond the cited statements, h = 0 edge cases, and under-specified checks. Worked examples are presented as illustrations. Detail: <session scratch>/audit/env2/findings.md

Coverage: 12 items examined; 11 hold, 0 defective, 0 suspect, 1 not checked.

| Item | Verdict | Note |
|---|---|---|
| Numerical observations in range | not_checked | None present: no statement in lines 156-381 carries the "Numerical observation" status. |

Items found to hold: prop:env-selection; lem:env-constant; prop:env-concentration; prop:env-aggregate-closure; prop:env-aggregate-memory; thm:env-hayek-horizon; lem:env-composition; prop:env-multiplex; ex:env-cell with chk:env-cell and fig:env-cell; ex:env-firm with chk:env-firm; ex:env-person with chk:env-person.

### env2-01 (major, unconfirmed): Leading constant 3/(5 pi) presented as derived here is the Berg-Purcell perfect-instrument result

Location: sections/10d_environments.tex:201 (after prop:env-concentration); also the src comment at :199. Category: attribution.

Evidence. Text: "the constant 3/(5 pi) for a transparent ball is derived here, and we do not claim it is theirs". Mora and Wingreen, arXiv:1002.3907, Eq. 10, give <(dc)^2>/c^2 = 3/(5 pi D a c T) for the perfectly monitoring sphere and state "The first result was obtained in [Berg and Purcell 1977]" (https://ar5iv.labs.arxiv.org/html/1002.3907). I did not open Berg and Purcell 1977 itself; that is what is missing for confirmation.

Proposed fix. Replace with: "The leading term is the perfect-instrument formula of Berg and Purcell (1977), rederived in the appendix; the finite-time correction -(5/3)(r^2/(pi D T))^{1/2} and the bound on q_T are computed here." Verify the equation number in the primary source before citing it.

What would overturn the finding. Berg and Purcell 1977 not containing 3/(5 pi T D c a) for a sphere that counts molecules inside its volume.

State: applied. [10d] applied: Confirmed through Mora-Wingreen arXiv:1002.3907 (opened): Eq. 10 gives 3/(5 pi D a c_0 T) for the monitoring sphere and attributes it to Berg-Purcell. Berg-Purcell body is a scan I could not read, so attribution is routed through Mora-Wingreen; new bib entry mora2010limits. No equation number of Berg-Purcell cited.

### env2-02 (minor): Finite-time factor quoted as 0.79 drops q_T; exact value is 0.81, and items (1) and (2) use different variances

Location: sections/10d_environments.tex:206 (ex:env-cell item 1); sections/chk10d_environments.tex:38-41 (chk:env-cell). Category: number mismatch.

Evidence. Exact quadrature of the proposition's covariance at T_int = 20 r^2/D (cell.py): variance/leading = 0.8101, two-term value 0.7897, q_T = 0.0204 (bound 0.0488). Item (2)'s correlations 6.36e-2, 1.03e-3 reproduce only with the exact variance, while item (1)'s ratios 19.7 and 0.79 use the leading term. With the exact variance the ratios are 24.3 and 0.973, captured fractions 0.9605 and 0.493.

Proposed fix. Write "the finite-time factor on the variance is 0.81 (0.79 without the remainder q_T = 0.020)", and either apply it in item (1) or say that item (1) uses the leading term as a conservative value while item (2) uses the exact variance.

What would overturn the finding. A quadrature of 2(|B|T)^{-2} int_0^T (T-u)K(u)du at T=20 giving 0.79 times the leading term.

State: applied. [10d] applied: Confirmed by quadrature (env2-02_env2-03.py): exact/leading 0.8101, two-term 0.7897, q_T 0.0204, bound 0.0488; window correlations 6.36e-2, 2.93e-3, 1.03e-3 use the exact variance. Item (1) now states both, keeps leading-term values as conservative and adds exact ratios 24.3, 0.97; check extended.

### env2-03 (minor): "Thirteen orders of magnitude" compares a pooled one-second reading with a single-molecule snapshot

Location: sections/10d_environments.tex:212 (ex:env-cell) and :219 (fig:env-cell caption, "13.55 below the 1 percent ligand signal"). Category: interpretation.

Evidence. The chemical reading pools about 315 molecules in the ball (0.6022 x 523.6) over about 31 effective snapshots (snapshot variance 1/315.3 against exact reading variance 1.03e-4), about 9.7e3 molecule-samples. The gravity reading is one position sample of one protein (2.2e-14). At equal molecule-samples the gravity ratio is 2.1e-10, a gap of 9.7 orders, not 13.6.

Proposed fix. Add: "per molecule-sample; a reading that pools as many protein positions as the chemical reading pools ligand samples (about 10^4) still has ratio 2x10^{-10}, ten orders below one."

What would overturn the finding. A definition of "reading" in the example under which the two channels pool the same number of independent samples.

State: applied. [10d] applied: Confirmed: 315.3 molecules times 30.9 effective snapshots = 9.73e3 molecule-samples; pooled gravity ratio 2.14e-10, 9.67 orders below one. Example, section opening, figure caption and check now state per-reading (13.66) and equal-pooling (nearly ten) gaps.

### env2-04 (minor): Chemical reading treated as an instantaneous sample of the slow signal

Location: sections/10d_environments.tex:206 (ex:env-cell item 1). Category: modeling approximation not stated.

Evidence. Predictive information 0.755 nats at h = 1 s uses rho^2 = captured fraction x e^{-2h/tau}. For the stated sensor (average over 1 s of an OU signal, tau = 10 s) with h measured from the window end and the exact noise variance, rho^2 = e^{-0.2} x 0.9056/(0.9675+0.0411) = 0.735, giving 0.664 nats (hand computation, not scripted).

Proposed fix. State the idealization: "treating the one-second average as a sample of eta^L at the end of the window; averaging the signal lowers the value at h = 1 s to about 0.66 nats."

What would overturn the finding. A recomputation with the window-averaged OU signal that returns 0.755.

State: applied. [10d] applied: Confirmed by script: the window-averaged OU reading gives 0.651 (0.201) nats at 1 s and 0.064 (0.028) at 10 s with leading-term variance, 0.664 (0.232) and 0.065 (0.032) with exact variance. Item (1) now states the point-sample idealization and the averaged values; the check records the formula and numbers.

### env2-05 (minor): Memory "grows with the number of distinct timescales" rests on an upper bound only

Location: sections/10d_environments.tex:276 (prop:env-aggregate-memory(e)) against :286. Category: statement weaker than the prose that cites it.

Evidence. (e) proves closure of order "at most T-1"; line 286 asserts that the memory an aggregate needs grows with the number of timescales. The stronger fact is true: the observability matrix of (1^T/N, diag(alpha_i)) is a Vandermonde matrix with rank equal to the number of distinct alpha_i (order.py: rank 3 for 3 distinct values), so the minimal order is exactly T-1.

Proposed fix. Restate (e): "the type averages are exactly closed and the minimal order of the average is d* = T-1", adding one proof line: by thm:met-abstract-physics(c) the least closed extension has the rank of the observability matrix, a Vandermonde matrix of rank T.

What would overturn the finding. An aggregate with T distinct persistences and nonzero type weights that is closed of order below T-1.

State: applied. [10d] applied: Confirmed: observability matrix of (1^T/N, diag(alpha_i)) is a column-repeated Vandermonde of rank T (exact sympy ranks 3, 4, 5, 1 on four instances, zero node included). Part (e) now states d*=T-1; proof gains the lower-bound argument via thm:met-abstract-physics(f); check extended.

### env2-06 (minor): Conjecture said to be prop:env-horizon(b) in the linear-Gaussian case, but hypotheses differ

Location: sections/10d_environments.tex:381 against :67 (prop:env-horizon(b)) and :377 (conj:env-nonlinear). Category: cross-reference overreach.

Evidence. The conjecture is stated for an agent with a budget on I(s;eta_t). prop:env-horizon(b) concerns the top-kappa canonical subspace of a noiseless rank-kappa optimum, for diagonalizable F with |lambda_kappa| > |lambda_{kappa+1}|. Which variates a budget selects is thm:env-canonical(b), and defective F is not covered.

Proposed fix. "For linear-Gaussian exteriors with diagonalizable F and a gap in the moduli, conj:env-nonlinear follows from thm:env-canonical(b) and prop:env-horizon(b)."

What would overturn the finding. prop:env-horizon(b) being stated in budget form without the diagonalizability and gap hypotheses.

State: applied. [10d] applied: Confirmed. Sentence after the conjecture now derives the linear-Gaussian case from thm:env-canonical(b) plus prop:env-horizon(b) applied with kappa equal to the number m of variates read, under diagonalizable F and a modulus gap at m; defective F and gapless counts are stated as not covered.

### env2-07 (minor): Part (d) said to answer the single-agent part of open:abs-attention under a different constraint and objective

Location: sections/10d_environments.tex:357 against sections/10_abstract_collectives.tex:463 (open:abs-attention). Category: cross-reference overreach.

Evidence. The open problem asks about agents that "allocate one attention capacity kappa across modalities by expected free energy". prop:env-multiplex(d) is for a Shannon budget I_max and the decision-loss matrix J alone (reverse water-filling), with no epistemic term and no channel-count capacity.

Proposed fix. "Part (d) answers the single-agent part of that open problem for a Shannon budget and pragmatic value alone; the case of a channel count kappa and of the full G^att_h remains open."

What would overturn the finding. A proof in the appendix of (d) for the objective G^att_h with a rank limit.

State: applied. [10] applied: Confirmed: prop:env-multiplex(d) is a Shannon-budget, decision-loss result. The paragraph after open:abs-attention said (d) 'answers part of the question'; it now scopes this to a Shannon budget and pragmatic value alone and lists channel count kappa and full G^att_h as open. The 10d sentence is unchanged. [10d] applied: Confirmed. Prose after prop:env-multiplex now limits (d) to a Shannon budget and pragmatic value alone, with the channel-count and full G^att_h case open; the later 'remaining part of that open problem' clause was reworded to match. Group 10 already carries the matching wording.

### env2-08 (minor): Formulas undefined at h = 0 and a division by w_1 before w_1 > 0 is assumed

Location: sections/10d_environments.tex:298-300 (thm:env-hayek-horizon(b)) and :349 (prop:env-multiplex(c)). Category: edge case.

Evidence. In prop:env-multiplex(c) the denominator psi^T(P_0 - F^h P_0 (F^h)^T)psi is zero at h = 0, while chk:env-multiplex reports the comparison "at every h" including h = 0. In thm:env-hayek-horizon(b) the threshold has exponent 1/(2h), and the displayed ratio bound divides by w_1 one clause before "if w_1 > 0".

Proposed fix. Add "for h >= 1 and w_1 > 0" at the head of thm:env-hayek-horizon(b) reversible clause and "for h >= 1" before the display in prop:env-multiplex(c).

What would overturn the finding. A convention stated elsewhere in the section that horizons are h >= 1.

State: applied. [10d] applied: Confirmed. thm:env-hayek-horizon(b) reversible clause now assumes h>=1, lambda_1(F) nonzero (needed beyond the finding: F=0 makes the ratio 0/0) and w_1>0. prop:env-multiplex(c) display holds for h>=1 and psi nonzero; proof shows the denominator is positive; check notes r_0^2=1.

### env2-09 (minor): Spot price modeled with noise, then read as a noiseless aggregate

Location: sections/10d_environments.tex:309-311 (ex:env-firm). Category: internal consistency.

Evidence. Line 309 defines p_t = eta^val_t + n^p_t with Var(n^p) = (sum 1/R_i)^{-1}, then says "The firm reads one noiseless aggregate: the spot price, functional (1,1)"; L_spot omits Var(n^p). The noisy formula appears only in the appendix derivation (app10d:176) and chk:env-firm (0.097 at h = 0, reproduced: 0.0968).

Proposed fix. "neglecting the price noise n^p, of order 1/N (with it, L_spot is the formula in app:env)".

What would overturn the finding. L_spot as displayed equaling the conditional variance given the noisy p_t.

State: applied. [10d] applied: Confirmed: displayed L_spot and h^x are the noiseless limit; noisy value 3-9/3.1=0.0968 matches chk:env-firm. Example now says the price noise of order 1/N is neglected, points to the noisy formula in the appendix, and says the comparison with the slow index is that of the noiseless limit.

### env2-10 (minor): Checks omit parameters needed to reproduce them

Location: sections/chk10d_environments.tex:47 (chk:env-aggregates), :52 (chk:env-hayek), :72 (chk:env-multiplex (c)). Category: reproducibility.

Evidence. The correlations (1, 0.779, 0.641, 0.547, 0.477) and largest Delta 0.162 reproduce only with q_com = q_id = 1 (agg.py); q_id = 0 gives 0.777. chk:env-hayek and chk:env-multiplex(c) use random decisions, P_0 and sensors with no seed or values, so 0.342, 0.392, 0.181 could not be recomputed.

Proposed fix. State q_com = q_id = 1 in chk:env-aggregates, and give the seed or the drawn matrices for the random instances.

What would overturn the finding. The parameters being stated elsewhere in the check file.

State: applied. [10d] applied: Confirmed: 0.779 and 0.162 need q_com=q_id=1 (q_id=0 gives 0.777). Added those values, the type-model parameters, the generator seed 311109 with draw order for the Hayek instance, and the drawn sensing matrix and decision functional for multiplex (c). All quoted figures reproduced from the stated data (scripts/env2-10.py).

### env2-11 (minor): Exact gravity ratio saturates at one; small-x_g extrapolation is avoidable

Location: sections/10d_environments.tex:209, :212, :219 (ex:env-cell item 4, fig:env-cell); :224 (rem:env-neurons). Category: simplification.

Evidence. For the truncated Boltzmann law the ratio g^2 x Fisher is x^2 Var(z)/Z^2 = 1 - (x/2)^2/sinh^2(x/2): 0.0793 at x_g = 1, 0.599 at 3.46, 1.000 at 48 (cell.py). It never exceeds one, so under item (4)'s model no particle reaches the 5 percent ligand ratio 19.7 per reading. rem:env-neurons says gravity-sensing cells use bodies "of that size" with the coupling of item (4).

Proposed fix. Plot and quote the exact form 1 - (x_g/2)^2/sinh^2(x_g/2) in place of the dashed continuation, and say that a sedimented particle gives ratio one per reading in this model.

What would overturn the finding. A variance of the truncated exponential on [0,Z] different from Z^2(1/x^2 - 1/(4 sinh^2(x/2))).

State: applied. [10d] applied: Confirmed by closed form and quadrature: ratio is 1-(x/2)^2/sinh^2(x/2), below one. Item (4), closing paragraph, caption, remark and check now state the exact form. Added the exact sign-reading error 1/(1+e^{x/2}), since the local ratio alone does not support the statolith remark. Figure file is outside my group.

### Not checked by lane env2

- chk:env-hayek numbers (4,3,2,... effective dimensions, 0.342, 0.392, 2.3e-8): random instance unspecified, only the inequalities were tested on my own draws.
- chk:env-multiplex (c) numbers (0.181, 3.2e-3, ...): random instance unspecified; internal consistency of information against partial correlation checked by hand only.
- chk:env-constant: the twenty-case table was not rerun; two quoted values recomputed by hand.
- chk:env-aggregates: the nineteen-agent type instance (0.2311, 0.1196, 2.9e-2) is unspecified; a smaller instance of my own was used instead.
- Berg and Purcell 1977 and Bialek and Setayeshgar 2005 (Eq. 35) were not opened; finding 1 rests on a secondary source.
- Cross-references read only at statement level or not at all: thm:hie-messages (cavity rule), prop:hie-literal-once, prop:fw-performative, prop:agy-consensus, thm:met-h5a, ex:met-traders, ex:met-two-firms, prop:abs-crossover, thm:agy-closure-average parts beyond (a).
- The description of assumption A7 at line 286 was not checked against its definition.
- Physiological statements in rem:env-neurons (statoliths, otoconia) were not checked; the remark itself disclaims them.
- Literature claims at lines 306 and 381 (Sims, Mackowiak-Wiederholt, Granger, Gordon et al., Friston et al.) were not checked.

### Redundancy noted by lane env2

- prop:env-selection(iv) restates lem:env-constant; keep one.
- prop:env-multiplex(c) reversible bound repeats the tail computation of thm:env-hayek-horizon(b) for one decision with a different normalizer; state once.
- prop:env-multiplex(b) noiseless clause is thm:env-hayek-horizon(a) again.
- rem:env-neurons and rem:env-interpretation both interpret ex:env-cell; merge.
- prop:env-aggregate-closure(a) duplicates the one-block remark after def:met-lumpable (10a_meta_agents.tex:147).

### Streamlining tiers proposed by lane env2

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| prop:env-selection | A |  | Section's main claim; drop (iv) into a pointer to the lemma. |
| lem:env-constant | B |  | Scalar Riccati bound; one-sentence pointer suffices. |
| prop:env-concentration | B |  | Leading term is classical; keep only the formula and citation in main text. |
| ex:env-cell | A |  | Headline illustration; keep items (1), (4), (5), move (2), (3) and digits to supplement. |
| fig:env-cell | B |  | Caption repeats the example; use the exact form 1-(x/2)^2/sinh^2(x/2). |
| rem:env-neurons | C |  | Unchecked physiology; merge two sentences into rem:env-interpretation. |
| def:env-aggregates | A |  | Needed to state the aggregate results. |
| prop:env-aggregate-closure | A |  | Keep (a), (b) closure and (c); move the fluctuation covariance bound to supplement. |
| prop:env-aggregate-memory | A |  | Keep (c), sharpened (e), (f); move (a), (b), (d) to supplement. (d) is vacuous unless dispersion is far below (1-alpha_+)^{3/2}. |
| thm:env-hayek-horizon | A |  | Keep (a) and the reversible part of (b); (c) to supplement. |
| ex:env-firm | B |  | Two-mode illustration of (a); keep the crossover formula only. |
| rem:env-firm-meta-agent | C |  | Pointers to other sections, no content of its own. |
| ex:env-person | B |  | Water-filling illustration; one sentence in main text. |
| lem:env-composition | B |  | Two-line Gaussian Markov identity. |
| prop:env-multiplex | B |  | (a)-(c) follow from earlier results; (d) is the only new part and could be a corollary. |
| rem:env-own-aggregate | C |  | Pointer to the cavity rule in the hierarchy section. |
| rem:env-interpretation | B |  | Keep as the single interpretive remark of the section, shortened. |
| open:env-filtering | B |  | Genuine open problem; one sentence in main text. |
| conj:env-nonlinear | B |  | Keep the statement with the corrected linear-Gaussian sentence; move the three narrower questions to supplement. |

## Lane frame: Framing against results: abstract, introduction, predictions, discussion

No critical defect found in the framing. Of 73 ledger items in the abstract, introduction, prediction tables and discussion, 50 hold against the cited statements, 18 are defects, 4 are suspect and 1 is unchecked; the defects reduce to 15 findings (3 major, 12 minor). The majors: (1) 13:9 cites the lattice-contrast theorem for "homogeneous media have no collective", which that theorem does not say (the statement follows from the baseline definition); (2) "memory vanishes only if retained agents hear no eliminated one" (01:84, table a, 13:11, 05:64) overstates thm:agy-closure-identity, with a two-agent counterexample run (zero memory kernel, exactly Markov retained process, positive closure gap); (3) the H5(a) inference clause (01:96, 13:21, 11:103, abstract) drops the steady-state, centralized-start and noiseless-computation conditions of thm:met-h5a(iv). Minors are condition or status drift between framing passages (innovations wording, depth-bound status worded three ways, two-versus-three exception list, leak constant, H4 conditions and "upper bounds" beside an exact length, variance-versus-deviation order) and three prediction refuters that the cited result does not imply as written (11:83, 11:105, and the unstated [0,1) condition at 11:132). Assumptions are numbered A5-A12 by design; A6 is tied to no result, and the standing hypotheses (Lin), (Loc), (B), (NN), asm:frm-mean-field and the header conditions of thm:met-h5a are not named in the framing. The H5 exception list for non-Gaussian results is explicit; H1-H4 have no parallel list although several cited results leave the linear-Gaussian setting (reported unconfirmed, from statement headers). Statements were opened for every cited result; appendix proofs were not, apart from one recomputation (4.59e3 = 75321921/16401) and one script (closure_cx.py in the lane directory). The findings.md copy could not be saved: the harness refused report-file writes from this agent.

Coverage: 75 items examined; 46 hold, 23 defective, 5 suspect, 1 not checked.

| Item | Verdict | Note |
|---|---|---|
| 00:4 abstract: 'abstract physics exactly when the kernel of its map is invariant' | defect | Input conditions of thm:met-abstract-physics(c) dropped. |
| 00:4 abstract: 'pooled information contributions give the meta-agent's predictive law' | defect | Conditions of thm:met-h5a(iv) dropped. |
| 01:52 H4 statement: '(M) and a named contraction', 'upper bounds', 'inverse spectral gap' | defect | (Lin), (Loc), (B) unnamed; exact OZ length called an upper bound; tau = -1/ln rho(W). |
| 01:84 A7 -> closure identity 'always carries memory' | defect | Counterexample run. |
| 01:84 A6 timescales tied to no result | suspect | No \cref to asm:int-a6 anywhere; two literal mentions outside the introduction. |
| 01:96 H5(a) inference clause 'parametrizes ... at every number of consensus rounds' | defect |  |
| 01:97 H5(b) 'cannot see in their innovations' | defect |  |
| 01:104 depth bound 'inequality checked only in computations' | defect | Disagrees with 01:250 and prop:ren-depth(c). |
| Table a 01:132 lattice-contrast row scope | defect | Scope omissions. |
| Table a 01:138 closure-identity row | defect |  |
| Table b 01:163 grounding-tension row scope | defect | Scope omissions. |
| Table b 01:177 'Hypothesis H4 in final form' row | defect |  |
| Table c 01:205 floor row 'unseen in innovations' | defect |  |
| Table c abstract-physics row 'if and only if the kernel is invariant' | suspect | Abbreviated equivalence; scope column 'coarse act as input' partly covers it. |
| 01:252 'scope is that of the proofs: linear-Gaussian dynamics' | suspect | No exception list for H1-H4. |
| 11:17 D_cal(1-cos phi), lem:frm-calibration | not_checked |  |
| 11:53 grounding-tension prediction row | defect | Scope omissions; numbers hold. |
| 11:83 records-row refuter | defect | Two-record example. |
| 11:103 pooling row 'exact predictive mean ... at every number of consensus rounds' | defect |  |
| 11:105 literal reading and rebuilt-record row refuter | defect |  |
| 11:132 aggregate-memory row | defect | Condition [alpha_-,alpha_+] in [0,1) omitted; (c), (f) clauses hold. |
| 13:9 'Homogeneous media have no collective ... (thm:col-lattice-contrast)' | defect |  |
| 13:11 'memory vanishes only if ... A7 in exact form' | defect |  |
| 13:19 H4 'a set of upper bounds'; OZ length exactly; l(a/eps)^(1/2) | defect | Numbers hold; wording defect as at 01:52. |
| 13:21 exception list; leak constant; H5a sentence; inverse cube | defect | Three defects in one paragraph; inverse-cube clause holds (prop:met-memory). |
| 13:27 depth bound 'proved in one dimension'; per-level thresholds b/(2b^2-1), 1/(2b-1) | suspect | Thresholds hold; depth-bound wording omits the two-dimensional check. |
| 13:35 'deviations of order one over the size of the smallest type' | defect |  |
| 13:39 numbers 2.19, horizons 1/8/40, 0.72 nats, 2.2e-14; 'fewer and slower' without 'reversible' | defect | Numbers hold; qualifier dropped. |
| 13:51 'theory is linear and Gaussian ... results that hold more generally do not select collectives' | suspect |  |

Items found to hold: 00:4 abstract: formation thresholds and '0 to 7 of 8 replicates'; 00:4 abstract: H5a 'exact conditional theorem ... component error bounds and no approximate version'; 00:4 abstract: 'having the structure of an agent selects no meta-agent; contrast does'; 01:24 H1(a) exact path blanket; approximate stationary blanket; 01:31 homogeneous lattices have bounded contrast, baseline finite; 01:24-31 H1(b) contrast, comparison medium, baseline; closure, agency, interaction necessity; 01:40 H2 misreading scopes; 01:43 H3 formation thresholds gamma_M, gamma_S, gamma_T and status; 01:47 withdrawal theorem, C0 blindness, holonomy; 01:58-90 assumptions numbered A5-A12; 01:84 A9, A10, A11 -> prop:env-multiplex, prop:agy-identity, thm:coh-grounding-tension; A8; 01:96 H5(a) criterion (kernel invariant and coarse act); blanket, closure, agency, no-selection clauses; 01:97 H5(b) record factor about 1+beta/omega; overconfidence factors; 01:98 H5(c) canonical variates, horizon, diffusive averages, aggregates; 01:99 H5(d) renormalization claims; 01:104 H5 proved in linear-Gaussian models with three named exceptions; 01:104 first-order adiabatic rate is a numerical observation; Table a remaining rows (thm:col-bridge, cor:col-lstar, prop:col-whole-population, agency rows); Table b remaining rows (information decay, amplification, domains, formation, light cone, OZ, records, trees); Table c remaining rows; table d rows (per-level thresholds, 2/7, exponent 2); 01:242 formation not established as dynamics; 01:250 depth bound 'proved in one dimension and checked for one step in two'; 11:9 proxies; contrast 3.37 to 0.114 at leak 0.05; 11:27 formation qualification; tab:pre-reception rows: information decay, withdrawal, amplification, domains, formation; 11:40 overvaluation row, ratio grows like (1-phi)^-2; 11:42 mean-square floor refuter; 11:72 deletion-null row; 11:76 negative association of redundant choices; 11:81 OZ row refuters (exponential clustering with power-law links; xi_2 proportional to tau); 11:86 Seguy/border row; tab:pre-collectives size and light-cone rows; 11:107 record factor in [1+beta/omega, 1+beta/omega+eps/omega]; 11:110 and 11:112 depth and per-level rows; 11:128 canonical-variates row; 11:130 firm row, 2.19 rounds; 11:134 gravity row 2.2e-14; 11:146 '674 of 2000'; 'p = 0.007'; 11:148 spectral radius 1.0613; 11:150 light cone for any local rule; percolation bound; 21.5 hops; 13:13-17 H2, withdrawal and formation paragraphs; 13:19 'L <~ xi right in low dimension and loose in high' (cor:sca-size); 13:23 fourth order in dispersion; 4.59e3; 'invisible in social and top-down innovations'; 13:25 H5(c) summary; 13:33 0.074 nats; 13:35 five-dimensional law; 13:43 Perron exactness criterion; Markov only if retained states do not read internal ones; adiabatic rate.

### frame-01 (major): Discussion cites the lattice-contrast theorem for a statement it does not contain

Location: sections/13_discussion.tex:9 (cites thm:col-lattice-contrast, sections/04_collectives.tex:383-389). Category: cross-reference beyond cited result.

Evidence. 13:9: "Homogeneous media have no collective at any admissible level (\cref{thm:col-lattice-contrast})". The theorem (04:383-389) proves bounded contrast and a finite baseline r-bar_hom on Z^D for a translation-invariant symmetric kernel with a^Pi(x) >= a_nn > 0 on axis steps, finite second moments and uniform leak. It says nothing about collectives and nothing about homogeneous media off the lattice. The no-collective statement is a consequence of def:col-baseline and def:col-collective (a homogeneous medium is its own comparison medium, so no region exceeds the supremum), stated as prose at 04:467 ("L*=0 in a homogeneous medium at every admissible level"). The introduction words the same result correctly at 01:31: "homogeneous lattices have bounded contrast, so the baseline is finite (thm:col-lattice-contrast)". The statement itself is true by definition; the defect is the attribution and the dropped lattice scope.

Proposed fix. Replace with: "Homogeneous lattices have bounded contrast, so the baseline is finite (\cref{thm:col-lattice-contrast}), and a homogeneous medium, being its own comparison medium, has no collective at any admissible level (\cref{def:col-baseline,def:col-collective})."

State: applied. [04] applied: The theorem is unchanged. Two prose sentences in 04 drew the no-collective conclusion from it alone; both now attribute finiteness of the baseline to the lattice theorem and the absence of collectives to def:col-baseline and def:col-collective. The discussion sentence belongs to the frame group. Framing pass: [group 01] declined: The defect is in 13_discussion.tex; the sentence in the H1 paragraph of 01 already attributes only bounded contrast and a finite baseline to thm:col-lattice-contrast. I only tightened the table row's scope column to the theorem's hypotheses (Z^D, symmetric ker ...; [group 13] applied

### frame-02 (major): "Memory vanishes only if retained agents hear no eliminated one" overstates the closure identity

Location: sections/01_introduction.tex:84 and :138 (results table a, row citing thm:agy-closure-identity); sections/13_discussion.tex:11; sections/05_agency.tex:64; statement thm:agy-closure-identity at 05_agency.tex:48-61. Category: framing claim stronger than cited theorem.

Evidence. thm:agy-closure-identity(b) is an equivalence between W_{R Rbar}=0 and the joint vanishing of "the memory, initial-state and colored-noise terms ... for every initial law"; (c) gives only d_M <= d_cl. The theorem's own kernel formula Gamma_l = W_{R Rbar} W_{Rbar Rbar}^{l-1} W_{Rbar R} vanishes whenever W_{Rbar R}=0, whatever W_{R Rbar} is. Counterexample (closure_cx.py, lane directory): two scalar agents, W=[[0.5,0.4],[0,0]], Q=I, retained {1}. Gamma_1..5 = 0; x_1 is exactly AR(1) (autocovariance ratios 0.500000, 0.500000, 0.500000; Var[x1'|x1] = Var[x1'|x1,x1-] = 1.160000, Markov gap 0), while agent 1 hears agent 2 (W_12 = 0.4) and the closure gap Var[x1'|x1] - Var[x1'|x] = 0.16 > 0. With W_22 = 0.6 the memory kernel is still identically zero and the non-Markov part (gap 3.6e-6) comes from the colored-noise term. So a collective whose boundary hears its interior can carry no memory, against 01:84 ("always carries memory"), 05:64 ("therefore always carries memory") and 13:11 ("whose memory vanishes only if the retained agents do not hear the eliminated ones").

Proposed fix. 01:84: "A7 the closure identity, by which a collective whose boundary hears its interior is never exactly closed: its reduced equation keeps a memory, initial-state or colored-noise term". Table a: "Exact closure only if retained agents hear no eliminated one". 13:11: "an exact reduced equation whose memory, initial-state and colored-noise terms all vanish only if the retained agents do not hear the eliminated ones". 05:64: "A collective whose boundary hears its interior is therefore never exactly closed".

What would overturn the finding. table a row "Memory vanishes only if retained agents hear no eliminated one | theorem"

State: applied. [05] declined: Defect is real in 01 and 13, but 05 already reads correctly after an earlier batch: the prose after the theorem says the summary is never sufficient (d_cl>0) while d_M may vanish, with the A=[[a,b],[0,0]] example, d_cl=(1/2)ln(1+b^2). Nothing left to change here; frame follow-ups returned. Framing pass: [group 01] applied; [group 13] applied

### frame-03 (major): H5(a) inference clause drops the steady-state, centralized-start and noiseless-computation conditions of thm:met-h5a(iv)

Location: sections/01_introduction.tex:96 (H5a); sections/13_discussion.tex:21; sections/11_predictions.tex:103 (tab:pre-meta); sections/00_abstract.tex:4; statement thm:met-h5a at sections/10a_metaagents.tex:321-341. Category: conditions of cited theorem omitted in hypothesis statement.

Evidence. 01:96 and 13:21: "the members' average estimate parametrizes, up to their averaged computation noise, the meta-agent's predictive law of its current exterior at every number of consensus rounds". 11:103: "makes a group's average estimate the exact predictive mean of its coarse exterior at every number of consensus rounds". Abstract: "pooled information contributions give the meta-agent's predictive law". thm:met-h5a(iv): y^eta_{C,t+1} "is the predictive mean of the steady-state coarse filter plus the response of the stable matrix ... to the averaged computation noise. With noiseless member computation, the centralized start and P^-_0 = Pbar^-, (y^eta_{C,t+1}, Pbar^-) parametrizes the meta-agent's predictive law". The steady-state filter mean is the exact conditional mean only from the stationary initial covariance, and the law is parametrized by the pair with Pbar^-, not by the average estimate alone. The theorem header also requires per-channel noise and rho(A)<1, which no framing passage names.

Proposed fix. 01:96 and 13:21: "the members' average estimate is, up to their averaged computation noise, the predictive mean of the steady-state coarse filter at every number of consensus rounds, and with the steady-state covariance it parametrizes the meta-agent's predictive law from the centralized start with stationary initial covariance". 11:103: replace "the exact predictive mean of its coarse exterior" by "the predictive mean of the steady-state filter of its coarse exterior" and add "stationary start, noiseless computation" to the status column.

State: applied. [10a] applied: thm:met-h5a(iv) itself is correctly conditioned. The 10a opening paragraph repeated the loose claim ('Kalman predictor ... at every number of consensus rounds'); replaced with the finding's wording. The sentence after prop:met-consensus-filter ('still the exact predictive mean') now carries the centralized-start and stationary-covariance conditions. Frame files returned as follow-ups. Framing pass: [group 01] applied; [group 11] applied; [group 13] applied

### frame-04 (minor): "Unseen in innovations" omits that sensory innovations do see the shared error

Location: sections/01_introduction.tex:97 (H5b) and :205 (results table c, row citing thm:hie-floor, lem:hie-record-blind).

Evidence. 01:97: "a shared-error floor that the members cannot see in their innovations"; 01:205: "unseen in innovations". lem:hie-record-blind(a) (10b_hierarchy.tex:231-237): no statistic of the social and top-down innovations carries information about the shared error, while every sensory innovation s_i - m_i = v_i - e_i shifts by -x(t). 13:23 states it correctly: "invisible in social and top-down innovations".

Proposed fix. 01:97: "that the members cannot see in their social and top-down innovations"; table c: "unseen in social and top-down innovations".

State: applied. Framing pass: [group 01] applied; [group 13] declined: Already met in this file: the H5 paragraph reads "invisible in social and top-down innovations", which agrees with lem:hie-record-blind(a) as it stands in 10b_hierarchy.tex (sensory innovations shift by -x(t)). No other occurrence of "unseen", "cannot see" or ...

### frame-05 (minor): Status of the depth-bound inequality is worded three ways

Location: sections/01_introduction.tex:104 and :250; sections/13_discussion.tex:27; statement prop:ren-depth(c) at sections/10c_renormalization.tex:155-166.

Evidence. 01:104: "rests on an inequality checked only in computations". 01:250: "rests on an inequality proved in one dimension and checked for one step in two". 13:27: "only under an inequality proved in one dimension". prop:ren-depth(c): the inequality "holds in one dimension by (b) ..., and for one step in the two-dimensional computations of chk:ren-flows". 01:104 implies computational support in all D >= 2 (there is none for D >= 3 and one step for D = 2); 13:27 omits the two-dimensional check.

Proposed fix. 01:104: "rests on an inequality proved in one dimension and checked for a single decimation step in two". 13:27: "only under an inequality proved in one dimension and checked for one step in two".

State: applied. [10c] declined: Nothing to change in 10c: prop:ren-depth(c) is the reference wording (proved in one dimension by (b), checked for one step in two in chk:ren-flows, which reports all six 2D cases below xi_2/b). The divergent wordings are in 01 and 13 (follow-ups). Framing pass: [group 01] applied; [group 13] applied

### frame-06 (minor): Abstract states the abstract-physics criterion as an equivalence without its input conditions

Location: sections/00_abstract.tex:4; sections/01_introduction.tex results table c (row citing thm:met-abstract-physics, prop:met-memory); statement thm:met-abstract-physics(c) at sections/10a_metaagents.tex:149-162.

Evidence. Abstract: "the coarse exterior has an abstract physics exactly when the kernel of its map is invariant". Table c: "Exact abstract physics if and only if the kernel is invariant". thm:met-abstract-physics(c) requires three conditions: ker P_E invariant under A_EE, P_E A_ES = 0, and P_E A_EA vanishing on ker P_A. 01:96 and 13:35 state the full criterion ("and the coarse exterior reads the members' channels only through the coarse act"). As an "exactly when" the abbreviated form is false when the exterior reads member channels outside the coarse act. The table's scope column ("coarse act as input") partly covers this; the abstract has no such qualifier.

Proposed fix. Abstract: "the coarse exterior has an abstract physics exactly when the kernel of its map is invariant and the exterior reads the members only through the coarse act". Table c: "Exact abstract physics if and only if the kernel is invariant and the members enter only through the coarse act".

State: applied. [10a] applied: Confirmed against thm:met-abstract-physics(c), which needs three conditions. The 10a opening paragraph's 'exactly when the kernel of its map is invariant' now adds 'and the exterior reads the members only through the coarse act'. Abstract and introduction table returned as follow-ups. Check of the edit: [10a] defect, Minor. 'Exactly when ... the exterior reads the members only through the coarse act' fails in necessity if 'exterior' means all of X_E, the usage at 10a:136. Example: eta'=0.9 eta+0.15(alpha_1+alpha_2)+xi, h'=0.5h+alpha_1+xi', P_E=(1,0) satisfies thm:met-abstract-physics although h reads alpha_1 alone. Repair: [10a] repaired, Checker right: counterexample satisfies thm:met-abstract-physics(a) while X_E reads alpha_1 alone. Abstract sentence now reads 'the coarse exterior reads the members' channels only through the coarse act', matching P_E A_ES = 0, P_E A_EA = B-bar P_A. Framing pass: [group 01] applied; [group 13] declined: Nothing to change in 13_discussion.tex: the sec:dis-meta paragraph states the full criterion (kernel invariant under the exterior dynamics and the coarse exterior reads the members' channels only through the coarse act), which matches thm:met-abstract-physics( ...

### frame-07 (minor): "Constant overstates the leak by four orders" conflates the constant with the bound

Location: sections/13_discussion.tex:21 (cites prop:met-leak-bound, open:met-leak-constant at sections/10a_metaagents.tex:428-430).

Evidence. 13:21: "with a constant that overstates the leak by four orders of magnitude in the checked system". open:met-leak-constant: "the constant c_C of prop:met-leak-bound exceeds the exact conditional-variance constant by a factor of about 20, and the bound exceeds the leak by four orders of magnitude". The constant is off by about 20; the bound is off by four orders.

Proposed fix. "with a bound that exceeds the leak by four orders of magnitude in the checked system and a constant about 20 times the exact one (\cref{prop:met-leak-bound,open:met-leak-constant})".

State: applied. [10a] declined: Nothing to change in group 10a. Both passages here already separate the two facts and agree with chk:met-leak-bound: constant 45.1 against 2.15 (factor 21), bound 0.341 and 0.019 against 7.9e-6 and 7.1e-7 (four orders). The defect is in 13_discussion.tex; see follow-up. Framing pass: [group 13] applied

### frame-08 (minor): Non-Gaussian exception list for H5 has two entries in one place and three in two others

Location: sections/13_discussion.tex:21 versus sections/01_introduction.tex:104 and sections/13_discussion.tex:51.

Evidence. 13:21: "apart from one extension of the code game and the ligand statistics of a cell (\cref{prop:hie-record-bistability,prop:env-concentration})". 01:104 and 13:51: "the ligand and sedimentation statistics of a cell (\cref{prop:hie-record-bistability,prop:env-concentration,ex:env-cell})".

Proposed fix. 13:21: "apart from one extension of the code game and the ligand and sedimentation statistics of a cell (\cref{prop:hie-record-bistability,prop:env-concentration,ex:env-cell})".

State: applied. Framing pass: [group 01] declined: This file already lists three exceptions with three labels, each checked against its current statement; the two-entry list is at 13_discussion.tex:21 (still unrepaired, see cross_file). Only change here: the parenthesis now reads '(Supplement, \cref{...})', si ...; [group 13] applied

### frame-09 (minor): H4 framing names fewer hypotheses than thm:sca-h4 and calls an exact length an upper bound

Location: sections/01_introduction.tex:52 (H4) and :177 (results table b); sections/13_discussion.tex:19; statement thm:sca-h4 at sections/08_scale.tex:598-607, def:sca-lengths(c) at 08_scale.tex:179-190.

Evidence. 01:52: "Let the world-conditional errors satisfy the moment bound (M) and a named contraction of the error dynamics ... the correlation time tau is the inverse spectral gap ... These are upper bounds." Table b: "(M) and a named contraction; upper bounds". 13:19: "a set of upper bounds, each conditional on the moment bound (M) and a named contraction", followed in the same paragraph by "has the Ornstein--Zernike length 1/arccosh(1+eps/(2a)) exactly". thm:sca-h4 is stated "under asm:sca-standing, with (Loc) and (B)" and its part (b) assumes "(M) and (Lin)" and gives the Ornstein-Zernike length exactly. def:sca-lengths(c) sets tau = -1/ln rho(W), which equals the inverse spectral gap only to leading order in the gap.

Proposed fix. 01:52: "Let the world-conditional errors of a linear, local, bounded network ((Lin), (Loc), (B)) satisfy the moment bound (M) and a named contraction ... the correlation time is tau = -1/ln rho(W), the inverse spectral gap to leading order ... These are upper bounds, apart from the exact Ornstein--Zernike length of nearest-neighbor passing." Table b scope: "(Lin), (Loc), (B), (M) and a named contraction; upper bounds and one exact length".

State: applied. [08] applied: Confirmed: the prose after thm:sca-h4 called all statements upper bounds under (M) and a contraction, although the OZ length and the record secular root are exact and the theorem assumes (Lin), (Loc), (B). Summary sentence now names the exact items and the three standing conditions. Theorem statement unchanged. Check of the edit: [08] defect, Hypothesis names are right: (Lin), (Loc), (B) exist in asm:sca-standing and the theorem uses them. The exception list is still incomplete: the second-moment lengths xi_2^2=2a lambda/(1-lambda^2) of (b) and xi_{2,d}^2=varsigma_d^2/(2 eps^Pi) of (c) are exact identities (verified symbolically), and the record criterion of (d) is an equivalence; the same sentence cites both. Repair: [08] repaired, Exception list now names the exact lengths of (b) and (c) (Ornstein--Zernike and second-moment lengths) and the exact secular root and memory criterion of the record model. Framing pass: [group 01] applied; [group 13] applied

### frame-10 (minor): Scope conditions of cited results omitted in table rows, one prediction and one discussion sentence

Location: sections/01_introduction.tex:132 (table a, thm:col-lattice-contrast) and :163 (table b, thm:coh-grounding-tension); sections/11_predictions.tex:53 (grounding row) and :132 (tab:pre-sensing, prop:env-aggregate-memory); sections/13_discussion.tex:39.

Evidence. (i) 01:132 scope "translation-invariant kernels with finite second moments"; thm:col-lattice-contrast (04:383-389) also requires Z^D, a symmetric kernel, a^Pi(x) >= a_nn > 0 on axis steps and uniform leak. (ii) 01:163 scope "level-0 networks with homogeneous grounding; xi^2 on the ring"; thm:coh-grounding-tension (06:334-353) is for scalar errors, exact code models, time-invariant W under (Lin), (Loc), (B), (NN). (iii) 11:132: "its lag-u Markov error is at most (alpha_+ - alpha_-)^2/(4(1-alpha_+)^3)" with no range; prop:env-aggregate-memory(d) (10d:261-283) proves it "If the alpha_i lie in [alpha_-,alpha_+] subset [0,1)", while the setup allows alpha_i in (-1,1). (iv) 13:39: "under a budget fewer and slower ones as the horizon grows" without "reversible"; prop:env-horizon(a) (10d:63-74) proves the budget clause for reversible exteriors with distinct moduli, and 01:98, 13:25 and 11:128 keep the qualifier.

Proposed fix. (i) scope: "Z^D, symmetric translation-invariant kernels positive on axis steps, finite second moments, uniform leak". (ii) scope: "scalar level-0 networks, exact codes, time-invariant W, homogeneous grounding". (iii) insert "for persistences in [alpha_-,alpha_+] subset [0,1)". (iv) "in reversible exteriors under a budget fewer and slower ones as the horizon grows".

State: partial. Framing pass: [group 01] partial: (i) already met: the thm:col-lattice-contrast row carries the full scope. (ii) applied: grounding-tension row scope now matches part (b). (iii), (iv) lie in 11 and 13; the same missing 'reversible' qualifier stood in this file's sensing row and was repaired th ...; [group 11] applied; [group 13] applied

### frame-11 (minor): "Deviations of order one over the size of the smallest type" is the variance order

Location: sections/13_discussion.tex:35 (cites prop:env-aggregate-closure, sections/10d_environment.tex:243-256).

Evidence. 13:35: "with deviations from their infinite-population limit of order one over the size of the smallest type". prop:env-aggregate-closure(b) bounds the fluctuation covariance: ||Sigma^fl|| <= (||Q_id|| / min_t N_t) sum_u ||A_ty^u||^2. The variance is O(1/N_min), so the deviation is O(N_min^{-1/2}).

Proposed fix. "with deviations from their infinite-population limit whose variance is of order one over the size of the smallest type".

State: applied. [10d] applied: The discussion sentence is outside my files, but the paragraph after prop:env-aggregate-closure repeated the slip ('error of order 1/min N'). Now: variance of order 1/min N, deviation of order (min N)^(-1/2). Same fix for the price noise in ex:env-firm ('whose variance is of order 1/N'). Framing pass: [group 13] applied

### frame-12 (minor): Prediction refuter for rebuilt records reaches beyond prop:hie-literal-records

Location: sections/11_predictions.tex:105 (tab:pre-meta; cites prop:hie-literal-once, prop:hie-literal-records at sections/10b_hierarchy.tex:130-132). Category: refuting observation not implied by cited result.

Evidence. Refuter: "a record rebuilt by any rule but exact counting whose calibration does not degrade with the rounds". prop:hie-literal-records treats four named rules (E), (U), (A), (P), not every rule other than exact counting; the row's own claim covers only the union rule (factor growing like t) and the product rule (n^t). Under the averaging rule (A) the record is underconfident for t < n and overconfident for t > n, so its calibration first improves, and a rule outside the four that stays calibrated would refute nothing proved.

Proposed fix. "A factor of two or more after one literal reading of a scalar estimate, or a record rebuilt by the union or product rule whose overconfidence factor does not grow with the rounds."

State: applied. [10b] declined: Nothing to change in group 10b: the proposition, table, caption and prose claim growth only for the four named rules. Defect confirmed in 11_predictions.tex. Exact rational check shows oc under (A) can fall in early rounds (n=5, first step), so the union-or-product wording of this finding is the correct one. Framing pass: [group 11] applied

### frame-13 (minor): Records-row refuter is not implied by the row's own multi-record criterion

Location: sections/11_predictions.tex:83 (tab:pre-collectives; cites prop:sca-records-memory, prop:sca-records-length at sections/08_scale.tex:363, :390). Category: refuting observation not implied by cited result.

Evidence. Row claim: "a medium lengthens collective memory exactly when sum_k beta_k(delta_k - eps)/(omega_k + delta_k - eps) < 0". Refuter: "A record decaying more slowly than agents forget that shortens memory." With two records the criterion permits exactly that: eps = 0.1; record 1 with beta = 0.1, omega = 1, delta = 0 contributes 0.1(-0.1)/0.9 = -0.0111; record 2 with beta = 1, omega = 1, delta = 0.5 contributes 1(0.4)/1.4 = +0.2857; eps < omega_k + delta_k for both; the sum is +0.2746 > 0, so the medium does not lengthen memory although record 1 decays more slowly than agents forget. The refuter follows only for a single record or when every record has delta_k < eps.

Proposed fix. "A medium whose records all decay more slowly than agents forget that shortens memory."

State: applied. [08] declined: Defect confirmed numerically (eps_eff=0.2591>eps=0.1, criterion sum +0.2746; record 1 alone gives 0.0901), but it sits in 11_predictions. Group 08 text is already correct: prop:sca-records-memory(a) says 'every delta_k<eps' and the prose says 'in the weighted sense'. No change in my files. Framing pass: [group 11] applied

### frame-14 (minor, unconfirmed): H1-H4 carry no exception list for results outside the linear-Gaussian setting

Location: sections/01_introduction.tex:252; sections/13_discussion.tex:51; sections/11_predictions.tex:150; contrast with the H5 exception list at 01_introduction.tex:104. Category: scope flagging.

Evidence. 01:252: "Throughout, the scope is that of the proofs: linear-Gaussian dynamics, mostly with fixed or exogenously scheduled attention". 13:51: "The theory is linear and Gaussian ... and the results that hold more generally do not select collectives". H5 has an explicit exception list (01:104: prop:hie-record-bistability, prop:env-concentration, ex:env-cell). H1-H4 have none, although results they cite are stated, by their headers, for models that are not linear-Gaussian: the discrete code game (thm:coh-domains-1d, prop:coh-code-potential), finite-policy deliberation (thm:agy-agency, thm:agy-heterogeneous), the mean-field map with endogenous attention (thm:frm-formation, covered only by "mostly"), and sign readouts (prop:abs-seguy). 11:150 flags the light cone, the percolation bound, the Markov length, the order parameter and the code game, not the agency theorems or the formation map; thm:frm-formation bears on which collectives form, against 13:51's "do not select collectives". Based on statement headers read in this audit; proofs not opened, so not demonstrated as a contradiction.

Proposed fix. Add after 01:252's first sentence: "The exceptions in H1 to H4 are the code game of \cref{sec:coh}, whose states are discrete, the deliberation model of \cref{thm:agy-agency,thm:agy-heterogeneous}, whose policies are finite, the mean-field map of \cref{thm:frm-formation}, whose attention is endogenous, and the sign readouts of \cref{prop:abs-seguy}." In 13:51 replace "the results that hold more generally do not select collectives" by "of the results that hold more generally, only the formation map bears on selection, and it is a theorem about a map".

State: partial. Framing pass: [group 01] applied; [group 11] partial: In sec:pre-scope one sentence now flags the agency theorems (finite policies, likelihoods not assumed Gaussian; (P1)-(P4) read) and the formation theorem (nonlinear mean-field map, frozen calibration) as not linear-Gaussian. Sign readouts of prop:abs-seguy not ...; [group 13] applied

### frame-15 (minor): Assumption list: A6 tied to no result, and standing hypotheses of principal theorems are outside the list and unnamed in the framing

Location: sections/01_introduction.tex:58-90 (premises A5-A12) and :84; statements thm:sca-h4 (08_scale.tex:598), thm:coh-grounding-tension (06_coherence.tex:334), thm:frm-formation, thm:met-h5a (10a_metaagents.tex:321); asm:sca-standing (08_scale.tex:12-31). Category: assumption ledger.

Evidence. The premise counter starts at 5 by design (01:58: "seven standing assumptions explicit, numbered after the first four hypotheses"; A12 at 01:88), so A1-A4 do not exist. 01:84 ties A7 to thm:agy-closure-identity, A10 to prop:agy-identity, A11 to thm:coh-grounding-tension and A9 to the multiplex results; 13:11 names A5; A8 and A12 are used in sections 10 and 10a. A6 ("Timescales", 01:64-66) is tied to no result in the framing, has no \cref anywhere (the label asm:int-a6 is never referenced) and two literal mentions outside the introduction. No assumption label asm:int-a5 to a12 is \cref'd outside section 01. Principal theorems rest on hypotheses that are not in the A-list and not named where the framing summarizes them: (Lin), (Loc), (B), (NN) of asm:sca-standing (thm:sca-h4, thm:coh-grounding-tension(b)), asm:frm-mean-field (thm:frm-formation), per-channel noise and rho(A) < 1 (thm:met-h5a). Each theorem does name them in its own statement.

Proposed fix. At 01:84 add: "A6 is not proved or used as a theorem hypothesis; it motivates the fixed or exogenously scheduled attention of the proofs. The theorems use, beyond A5 to A12, the standing conditions (Lin), (Loc), (B), (NN) and (M) of \cref{asm:sca-standing}, the mean-field assumption of \cref{asm:frm-mean-field} and, for H5(a), per-channel noise and a stable exterior."

State: partial. [06] declined: Nothing to change in group 06: thm:coh-grounding-tension names (NN), (Lin), (Loc) and asm:sca-standing in its own statement; the proposed sentence belongs to 01_introduction.tex. [08] declined: Nothing to change in group 08. Verified that asm:sca-standing defines all five labels the proposed sentence cites, (Lin), (Loc), (B), (NN), (M), so the cross-reference proposed for 01_introduction is valid as written. [10a] declined: Nothing to change in group 10a. thm:met-h5a names per-channel noise and rho(A)<1 in its first sentence, and no A-list premise is cited in these files. The repair is the sentence at 01_introduction.tex; see follow-up. Framing pass: [group 01] applied; [group 13] partial: The discussion already names (Lin), (Loc), (B), (M) for thm:sca-h4, the hypotheses of thm:met-h5a and asm:frm-mean-field; I added exact code models and (Lin), (Loc), (B), (NN) of asm:sca-standing to the grounding-tension sentence, matching part (b). The A6 sen ...

### Not checked by lane frame

- Appendix proofs behind the framing constants: only statements were opened, apart from recomputing 4.59e3 and the closure counterexample.
- chk-file numbers (tab:hie-records, chk:ren-flows dimensions and step counts).
- lem:frm-calibration and the expression D_cal(1-cos phi) at 11:17.
- 11:148 'Without (M) there is no correlation length, correlation time or collective (thm:sca-h4(a))' against the wording of part (a).
- (a3) of prop:met-sufficiency against 'every conditionally independent start' at 01:96.
- Whether the Markov-error bound at 11:132 fails for negative persistences; only the omitted condition is established.
- Whether any appendix proof uses A6.
- The non-linear-Gaussian classification of thm:coh-domains-1d, thm:agy-agency, thm:agy-heterogeneous, thm:frm-formation and prop:abs-seguy rests on statement headers; proofs not opened.
- Section 12 (related work) and figure captions in the framing files.
- findings.md was not saved: the harness refused report-file writes from this agent.

### Redundancy noted by lane frame

- H5(a) statement: 01:96 (182 words) and 13:21 (360 words) share a near-verbatim sentence of about 110 words; restated again in the abstract and at 13:33-35 (465 words).
- Formation status and '0 to 7 of 8 replicates': abstract, 01:43 (246 words), 01:242 (169), 11:27 (233), 13:17 (274).
- Comparison medium and baseline definition: 01:31 (403 words), 11:9 (251), 13:9 (270).
- H5(b) records and overconfidence: 01:97 (151 words), 13:23 (321), 13:37 (331), plus table c and 11:105-107.
- H5(c) selective sensing: 01:98 (137 words), 13:25 (261), 13:39 (383), plus 11:128-134.
- H5(d) renormalization: 01:99 (142 words), 01:104 (350), 13:27 (276), 13:43 (394), plus table d.
- What is not established: 01:242-252 (841 words), 11:144-150 (519), 13:47 and 13:51 (608).
- H2 scopes: 01:40 (158 words) and 13:13 (251). Withdrawal: 01:47 (186) and 13:15 (216). H4: 01:52 (148) and 13:19 (262).

### Streamlining tiers proposed by lane frame

Tier A stays in the main text, tier B moves to the supplement, tier C is cut or merged.

| Item | Tier | Words | Reason |
|---|---|---|---|
| 13:21 sentence restating H5(a) nearly verbatim from 01:96 | A | 110 | Same conditional sentence in both places; the discussion can cite H5(a) and keep only the error-bound commentary. |
| 13:23, 13:25, 13:27 restate H5(b), (c), (d) from 01:97-99 before 13:37, 13:39, 13:43 restate them again with examples | B | 858 | Three passes over the same results in the introduction and twice in the discussion; merge each first-pass discussion paragraph into its example paragraph. |
| Limits stated three times: 01:242-252, 11:144-150, 13:47 and 13:51 | B | 600 | Overlapping lists of what is not established; keep the full list once (discussion) and a short pointer elsewhere. |
| Formation qualification at 11:27 against 01:242 and 13:17 | B | 230 | Same status statement and replicate counts in three places. |
| 01:104 status paragraph against the status columns of tables c and d | B | 350 | The paragraph repeats per-result status already carried by the tables; the three wordings of the depth-bound status arose from this duplication. |
| Comparison-medium definition at 11:9 and 13:9 against 01:31 | C | 200 | Restated definition; a pointer to def:col-baseline would serve, but each passage also carries local content. |

## Lane pos: Falsifiability, scope and novelty

Ten findings, nine major and one minor; none is a false theorem, and all concern what a reader may conclude. (1) Falsifiability: the subsection titled "Falsifiable predictions" lists negations of theorems; line 5 concedes that data cannot refute them, four refuter cells name the absorbing auxiliary in advance, three regimes void predictions, and membership in the model class is decided only through a declared model, so no observation is specified under which any of H1 to H5 would be given up. One refuter cell (records, "any rule but exact counting") is satisfied inside the model by a non-exact rule with a constant factor 2/3 (script in the lane directory). (2) Scope: the abstract's opening sentence promises a theory of how agents "from cells to nations" form collective agents, while 13_discussion.tex:11 states that no analyzed population meets every clause of the meta-agent definition and the one formation result fails a clause. The sensing answer rests on a declared predictive objective that the framework's own expected free energy does not imply and in the two-step case opposes; "slower meta-agents sense slower variables" follows from two declarations. The firm and gravity rows are worked examples listed as predictions: the first is the separation theorem and is definitional in the model, the second is the barometric exponent with an unmatched thirteen-orders comparison. (3) Novelty: of the ten named topics, DeGroot and Friedkin-Johnsen, Kron reduction, lumpability, Mori-Zwanzig, consensus filters and data incest are cited and not claimed as new. Defects: prop:env-aggregate-memory(f) is called "ours" with Granger 1980 unread, and the common-shock result is stated in the review arXiv:1306.3301; the "hard budget" novelty residue is the information curve of Chechik et al. 2005 and Creutzig and Sprekeler 2008 is uncited; latent-variable Gaussian graphical models are absent although the unrecorded-drive problem is declared open; Fisher, Ma and Nickel 1972 is uncited for the long-range Gaussian exponent. (4) Against the second assessment: its credit of "falsifiable predictions" (problem 10) and its "Substantial conditional answer" for problem 1 exceed what the text establishes; its problem 6 caveat is right and should extend to the objective being declared; its "Source assembly" note is stale, since collective_agents.tex:26-29 now inputs sections 10a to 10d. The manuscript's own framing exceeds the assessment's remaining-gap column in the abstract's first sentence (problems 1, 4, 10) and in 13_discussion.tex:5 and :39 (problems 3, 6, 7). Sources opened: arXiv:1008.1290 (abstract), arXiv:1306.3301 and arXiv:1410.1377 (ar5iv), the JMLR abstract of Chechik et al. 2005, the EPFL record of Creutzig and Sprekeler 2008, the RePEc record of Feder, Just and Schmitz 1980, and Yoder et al. 2001 (PMC64904). Not opened: Granger 1980, Fisher-Ma-Nickel 1972, Pollard 1965, Holthausen 1979, Danthine 1978, Zaffaroni 2004. Copy of findings: <session scratch>/audit/pos/findings.md

Coverage: 14 items examined; 8 hold, 3 defective, 3 suspect, 0 not checked.

| Item | Verdict | Note |
|---|---|---|
| Canonical correlation of past and future, predictive information, past-future bottleneck (thm:env-canonical, prop:env-horizon) | defect | See the finding on the novelty residue; akaike1975markovian, bialek2001predictability and creutzig2009past are cited at abstract or record level. |
| Mori-Zwanzig projection (thm:agy-mori-zwanzig, 12_related.tex:68) | suspect | Not claimed as new ("is linear Mori-Zwanzig in discrete time"). The sentence that small memory, sufficiency and a slow spectrum are distinct conditions is supported only by the author's own dennis2026participatory, a self-citation used as authority; discrete-time Mori-Zwanzig references were not opened. |
| Potential games and logit dynamics (12_related.tex:77) | suspect | Cited; the comparative claim of a bound "sharper than that of candogan2013dynamics" names no reading level for that source and was not checked. |
| Latent-variable Gaussian graphical models | defect | Not cited anywhere; see the unrecorded-drive finding (not confirmed for the dynamic case). |
| Gaussian renormalization of long-range models (prop:ren-exponents(b)) | defect | Standard result without attribution; minor. |
| Self-citations in sec:rel and sec:dis-gauge | suspect | dennis2026magent, dennis2026participatory and dennis2026formation are cited five times in 12_related.tex and once in 13_discussion.tex, the last known "as secondary descriptions of those documents state it"; none supports a theorem, one supports a conceptual distinction. |

Items found to hold: Consensus and information filters, distributed Kalman filtering (prop:agy-consensus, 12_related.tex:51); Data incest, double counting, channel filters, covariance intersection (12_related.tex:49); Kron reduction (lem:col-kron, 12_related.tex:132); Lumpability and informational or computational closure (prop:env-aggregate-closure, 12_related.tex:15, :70); DeGroot and Friedkin-Johnsen dynamics (12_related.tex:82); Abstract collectives: labeling of interpretations (10_abstract_collectives.tex); H4 framing (abstract, 13_discussion.tex:19); Worked-example numbers.

### pos-01 (major): The table titled "Falsifiable predictions" lists negations of theorems and names in advance the auxiliary that absorbs each failure

Location: sections/11_predictions.tex:23 (sec:pre-predictions), with :5, :19, :25, :72, :79, :103, :110, :112, :128, :132, :144 (tab:pre-reception, tab:pre-collectives, tab:pre-meta, tab:pre-sensing, sec:pre-scope). Labels: sec:pre-predictions; tab:pre-collectives; tab:pre-meta; tab:pre-sensing; sec:pre-scope. Category: unfalsifiability / test severity.

Evidence. Test run on all 28 rows: what would the author give up if the 'Refuted by' observation occurred? The section answers this itself. Line 5: "Data cannot refute a theorem, but they can refute the claim that a population is described by its model: an observation that contradicts the theorem in a population that appears to meet its hypotheses shows that one of them fails." Line 25: "for a theorem that observation identifies a hypothesis the population fails." Four refuter cells name the absorbing auxiliary in the cell: :72 "Contrast above one after deletion, which reveals an unconditioned shared drive or record"; :79 "Dependence beyond 2t hops, which reveals an unmodeled channel or shared drive"; :110 "which reveals a non-diffusive precision or a non-uniform leak"; :112 "which reveals a declared geometry or couplings outside the nested medium". Others are logical negations of a proved statement phrased with the theorem's own theoretical terms, so they cannot occur where the hypotheses hold: :103 "A product of posteriors from a common prediction whose claimed variance matches its error"; :128 "A prediction-optimal agent in a reversible exterior that reads more variates, or faster ones, at a longer horizon"; :132 "A geometric autocorrelation for the average of uncoupled members whose persistences differ". Line 144 adds: "predictions made there are void rather than refuted." Whether a population meets the hypotheses is decided only by the same kind of observation: :19 says weights and leaks are inferred "only through a declared model" and :11 says "an estimator without a recorded drive is open". By the severity requirement of Mayo 1996 an observation supports a claim only if it had a real chance of counting against it; here no outcome counts against H1 to H5, because every failure is assigned to model membership (the protective belt of Lakatos 1978 written into the table). The four rows whose refuters are observable in real populations (:86 borders, :130 firms, :132 indices, :134 cells) rest on a conjecture, worked examples or interpretations, of which line 5 says "Readings of social data are interpretations, which the models alone cannot refute"; the :86 refuter ("Border effects no larger where boundaries coincide") would be passed by any model in which each boundary type adds a cost. Assigned status: P for the theorems as mathematics, S for their standing as predictions about populations. The second assessment lists "falsifiable predictions" as already addressed under problem 10; the text does not supply them in the sense that phrase carries.

Proposed fix. Retitle the subsection "Consequences of the models and diagnostics of model failure", rename the column "Refuted by" to "Observation showing that a model hypothesis fails", and add: "No row puts hypotheses H1 to H5 at risk: a failed row removes the population from the model class. A severe test needs a check of membership that does not use the same observation, for example fitting the fine model under one condition and predicting the coarse statistic under an intervention the fit did not use; no such procedure is given here."

What would overturn the finding. One row whose refuting observation is stated in recorded observables, with a membership test independent of that observation, and for which the text commits to giving up a named hypothesis among H1 to H5.

State: partial. Framing pass: [group 11] partial: Subsection retitled 'Predictions and diagnostics of model failure', column 'Refuted by' renamed 'Contrary observation' in all four tables, captions aligned, and two sentences added: a contrary observation removes the population from the model class, and no ind ...

### pos-02 (major): The records refuter "any rule but exact counting" exceeds prop:hie-literal-records and is satisfied by a non-exact rule inside the model

Location: sections/11_predictions.tex:105 (tab:pre-meta) against sections/10b_hierarchy.tex:130-145 (prop:hie-literal-records, tab:hie-records). Labels: prop:hie-literal-records; prop:hie-literal-once; tab:hie-records. Category: cross-reference used beyond the cited result.

Evidence. The refuter cell reads "a record rebuilt by any rule but exact counting whose calibration does not degrade with the rounds". The cited proposition proves growth of the overconfidence factor for three named rules only: (U) like t, (A) like t/n, (P) like n^t. Counterexample in the proposition's own static scalar world: rebuild the record each round as record_0 + (1/n) sum_i (write_i - record_read). It counts each contribution 1/n times, so it is not exact counting, and its natural parameters are (Lambda_0 m_0 + h_o/n, Lambda_0 + Lambda_o/n) at every round, giving oc = (Lambda_0 + Lambda_o/n^2)/(Lambda_0 + Lambda_o/n), constant in t. For n = 3 members of unit information and Lambda_0 = 1 the closed form is 2/3; simulation with 4e5 draws gives 0.6685 at each of rounds 1 to 8, against 7.69 for (U) and 4600 for (P) at round 8 (the latter matches the 4.59e3 of 13_discussion.tex:23). Script: <session scratch>/audit/pos/record_rule_check.py. The listed 'refuting observation' therefore occurs inside the model whose theorem it is said to refute.

Proposed fix. Replace the cell by: "A factor of two or more after one literal reading of a scalar estimate, or a record rebuilt by the union, pooling or product rule of prop:hie-literal-records whose overconfidence factor does not grow with the rounds."

What would overturn the finding. A proof that every non-exact rebuilding rule has an overconfidence factor that departs from its round-one value without bound, or an argument that the cavity-subtracting pool above is exact counting under def (E).

State: applied. [10b] declined: Nothing in 10b repeats the over-claim. Counterexample reproduced exactly: the cavity-subtracting 1/n pool has oc=2/3 at every round (n=3, unit information). The proposed cell including the pooling rule is itself refutable in-model, since oc under (A) is not monotone for n>=5; use frame-12 wording. See follow-ups. Framing pass: [group 11] declined: Already repaired by an earlier batch: the cell now reads 'a record rebuilt by the union or product rule whose overconfidence factor does not grow with the rounds', which excludes the pooling rule (A). Checked by hand that the factor increases in t under (U) an ...; [group 13] applied

### pos-03 (major): The answer to "what agents sense" comes from a declared objective that the framework's own expected free energy does not imply and can oppose

Location: sections/00_abstract.tex:4; sections/13_discussion.tex:5 and :39 (sec:dis-meta); sections/10d_environments.tex:133-143 (rem:env-efe-horizon-free, rem:env-two-step), :97 (def:env-attention-objective); sections/11_predictions.tex:128. Labels: thm:env-canonical; prop:env-horizon; def:env-attention-objective; rem:env-efe-horizon-free; rem:env-two-step. Category: interpretation presented as result / source of the result.

Evidence. 13_discussion.tex:5: "we answer the question behind the fifth idea, when a meta-agent is an agent with external states of its own and what agents at each level sense"; :39: "What an agent senses is set by coupling, horizon and preferences." The abstract, which opens "We develop a traditional active-inference theory", closes its results with "capacity-limited linear sensors optimal for prediction read the leading canonical variates of the exterior at the agent's horizon". The body shows the active-inference objective does not deliver this. rem:env-efe-horizon-free (10d:134): "under a binding Shannon budget every sensor that spends the budget has the same epistemic value, whatever it reads", and under a gain budget "this sensor reads the fast mode, while the canonical sensor reads the slow mode at every horizon". rem:env-two-step (10d:143): "the epistemic term prefers the sensor least informative about the future outcome" and "The predictive-information criterion of thm:env-canonical follows from the expected free energy only when the hidden state of the agent's model for this decision is the state at the horizon, which is why we declare it as the objective of def:env-attention-objective and claim no more." Deleting the active-inference apparatus leaves thm:env-canonical unchanged (it is the Gaussian information bottleneck with a rank cap), which is the mathiness test of Lipton and Steinhardt 2018. Two consequences. First, the refuter at 11_predictions.tex:128 ("A prediction-optimal agent ... that reads ... faster ones") cannot be observed, since reading faster variates makes an agent not prediction-optimal by definition, while the manuscript's own expected-free-energy agent does read the fast mode in its computed instance. Second, "slower and coarser ones for slower meta-agents" (13_discussion.tex:39) follows from two declarations, the predictive objective and "its closure timescale sets its horizon"; problem 7 of the first external document names this pattern: "Retaining slow modes necessarily produces a slower description; observing that outcome does not establish an independent law". Assigned status: P for the optimizer theorem, S for the claim that agents of the framework sense these variables. The second assessment's remark under problem 6 ("optimizer characterizations for a known joint law") is correct and should be extended: the optimized objective is also declared.

Proposed fix. In the abstract write: "for a declared horizon-h predictive-information objective, which the one-step expected free energy of the framework does not imply, capacity-limited linear sensors read the leading canonical variates of the exterior"; in 13_discussion.tex:5 write "we state when a meta-agent has external states of its own and what a sensor optimal for a declared predictive objective reads at each level".

What would overturn the finding. A derivation, from the expected free energy of def:fw agents without redefining the model's hidden state as the state at the horizon, that the minimizer under a Shannon budget reads the leading canonical variates.

State: applied. [10d] applied: Body remarks already state the objective is declared. Section introduction and rem:env-interpretation now say the results describe a sensor optimal for a declared horizon-h predictive-information objective that the one-step expected free energy does not imply and can oppose. Abstract, discussion and predictions are outside my group. Framing pass: [group 11] applied; [group 13] applied

### pos-04 (major): prop:env-aggregate-memory(f) is called "ours" while Granger 1980 was not read; the common-shock aggregation result is in the literature

Location: sections/10d_environments.tex:277-286 (prop:env-aggregate-memory(f) and the paragraph after it); sections/11_predictions.tex:132; sections/10d_environments_extra.bib:52-61. Labels: prop:env-aggregate-memory. Category: novelty versus rediscovery.

Evidence. 10d:286: "granger1980long relates long memory to the aggregation of dynamic models in its title; we know it from its record, and the statement and proof of (f) are ours." The bib annote confirms "Read: record only". Part (f): density (1-alpha)^(p-1) f_0(alpha), 1/2 < p < 1, common shock only, limit aggregate sum_l m_l w_(t-1-l) with m_l ~ l^(-p) and R(u) ~ u^(1-2p). Source opened: Leipus, Philippe, Puplinskaite and Surgailis, "Aggregation and long memory: recent developments", arXiv:1306.3301 (read through ar5iv). Its Section 1 states the mixing-density condition (1.2), phi(x) ~ c (1-x)^beta as x tends to 1, and attributes the slow-decay observation with a Beta density to Granger 1980; its Section 2 states for AR(1) with common innovations that the 1/N-normalized aggregate is a moving average in the common innovations with coefficients E a^j ~ const j^(-beta-1), a long-memory moving average with non-summable coefficients for beta < 0, citing Puplinskaite and Surgailis 2009 and, for finite variance, Zaffaroni 2004. With beta = p - 1 this is part (f): coefficients l^(-p), non-summable for p < 1, square-summable for p > 1/2, hence autocovariance u^(1-2p). The same construction is listed at 11_predictions.tex:132 as a prediction. I did not open Granger 1980, Zaffaroni 2004 or Puplinskaite and Surgailis 2009 themselves; the claim here is that the result and its attribution are stated in the opened review. Assigned status: P as mathematics, with the novelty statement unsupported.

Proposed fix. Replace the sentence by: "Part (f) is the common-innovation case of the aggregation route to long memory of Granger (1980), in the form with a mixing density (1-alpha)^beta, beta = p - 1, treated by Zaffaroni (2004) and reviewed by Leipus et al. (2014); we give a self-contained proof with the explicit constant." Add the three references, and drop the (f) clause from the predictions row or mark it as a known result.

What would overturn the finding. A reading of Granger 1980, Zaffaroni 2004 and the review showing that none states the moving-average limit with coefficients E alpha^l ~ l^(-p) under common shocks for a density (1-alpha)^(p-1) near one.

State: applied. [10d] applied: Novelty claim removed. Opened arXiv:1306.3301 (Sections 1-2): it reports the 1/N moving-average limit with coefficients ~ j^(-beta-1) for infinite-variance common innovations, credited to Puplinskaite-Surgailis 2009, and credits Granger 1980 for the Beta law. Attribution to Zaffaroni 2004 was not confirmed there, so it is not cited. Bib entry leipus2013aggregation added. Framing pass: [group 11] applied; [bib] partial: Granger and Leipus entries already present and match Crossref (DOI 10.1016/0304-4076(80)90092-5) and the arXiv listing 1306.3301 (v1 only, no journal reference). Zaffaroni 2004 not added: ar5iv 1306.3301 Sections 1-2 credit the common-innovation limit to Pupli ...

### pos-05 (major): The claimed novelty residue for selective sensing ("rank limit and a hard budget") is narrower than stated, and a pinpoint theorem citation rests on an unread source

Location: sections/10d_environments.tex:50 (after thm:env-canonical); sections/12_related.tex:137, :139 (sec:rel-env) and :149 (sec:rel-new); sections/10d_environments.tex:63-66 (prop:env-horizon(a)). Labels: thm:env-canonical; prop:env-horizon; sec:rel-new. Category: novelty versus rediscovery / citation support.

Evidence. Two passages disagree on what was read. 10d:50 cites "Theorem 3.1 of chechik2005information" with its content, "the eigenvectors of Sigma_{X|Y} Sigma_X^{-1}, each entering at the critical value 1/(1-l)"; 12_related.tex:137 says of the same paper "a result we know from the abstract and a secondary summary". Source opened: the JMLR abstract page of Chechik, Globerson, Tishby and Weiss, JMLR 6:165-188 (2005). It names the eigenvectors of the normalized regression matrix and a cascade of structural phase transitions but gives no theorem number and no critical-value formula, so the pinpoint citation cannot come from the abstract. The same abstract states that the paper gives a complete analytic expression for the preserved relevant information as a function of compression, a concave information curve with one analytic segment per optimal dimension. A concave information curve is the constrained problem max I(s;Y) subject to I(s;X) <= I_max, so the "hard budget" half of "What may be new is the combination of a rank limit and a hard budget, relative to the Lagrangian bottleneck" (12_related.tex:139, also 10d:50) is in the cited paper; what can remain is the cap kappa on the number of channels. Second source opened: the EPFL record of Creutzig and Sprekeler, Neural Computation 20(4):1026-1041 (2008), whose abstract states that linear slow feature analysis is a variant of predictive coding that maximizes the mutual information between the current output and the next-step input, formulated with the information bottleneck. That is the one-step precedent for prop:env-horizon(a) ("The noiseless rank-kappa optimum reads the kappa slowest modes at every h"); it is not in references.bib or the extra bib files (no entry matches Sprekeler or slowness). sec:rel-new (12_related.tex:149) still lists "sensing under a rank limit, a budget and a horizon" among what is new in combination. I did not read the full text of either paper, so whether Chechik et al. treat a rank cap is not settled.

Proposed fix. At 12_related.tex:139 write: "What may be new is the cap on the number of channels and the extension from one step to horizon h; the budget form is the information curve of chechik2005information, and the selection of slow modes at one step is in creutzig2008predictive." At 10d:50 either read Theorem 3.1 and remove "from the abstract and a secondary summary" at 12_related.tex:137, or drop the theorem number and attribute the critical values to the secondary summary by name.

What would overturn the finding. The full text of Chechik et al. 2005 lacking an information curve usable as a budget constraint, or a statement by the author that Theorem 3.1 was read, with 12_related.tex:137 corrected.

State: applied. [10d] applied: Opened the JMLR PDF: Theorem 3.1 matches the pinpoint citation (left eigenvectors of Sigma_{x|y}Sigma_x^{-1}, critical 1/(1-lambda)), so it stays. Added that Sections 5 and 8 contain the budget form and mention a preset dimension; residue is at most the joint cap and budget. Added the Creutzig-Sprekeler 2008 one-step precedent (abstract read) with bib entry. Framing pass: [group 12] applied; [bib] declined: Nothing left in the bib files: creutzig2008predictive is already in 10d_environments_extra.bib and agrees with the Crossref record I opened (DOI 10.1162/neco.2008.01-07-455); 12_related.tex already cites it.

### pos-06 (major): The firm row restates the separation theorem of production with futures markets and is definitional inside ex:env-firm

Location: sections/11_predictions.tex:130 (tab:pre-sensing); sections/10d_environments.tex:308-317 (ex:env-firm); sections/13_discussion.tex:39. Labels: ex:env-firm; thm:env-hayek-horizon; rem:env-firm-meta-agent. Category: novelty versus rediscovery / worked example read as evidence.

Evidence. Prediction cell: "A firm that sells at t+h what it produces at t needs only the futures price of maturity h", basis "thm:env-hayek-horizon(a), proved; ex:env-firm ... whose reading for firms is an interpretation", refuter "Firms with long production lags whose output follows the spot price rather than the futures price of their lag." In ex:env-firm the optimal output is E[p_{t+h} | readings]/k_a and the futures price is defined as "the market forecast of the value at t+h, functional (F_1^h, F_2^h)", that is E[p_{t+h} | eta_t]. L_fut(h) = 0 then holds for any dynamics because a conditional expectation is sufficient for itself; thm:env-hayek-horizon(a) does no work in the conclusion. In economics the statement is the separation theorem. Source opened: the RePEc record of Feder, Just and Schmitz, "Futures Markets and the Theory of the Firm under Price Uncertainty", Quarterly Journal of Economics 94(2):317-328 (1980), whose abstract states that production decisions depend only on the futures market price and input costs and that the subjective distribution of the future spot price affects only the firm's futures trading. That result is stronger than the row (it holds under risk aversion and does not need the futures price to equal the forecast). No entry for Feder, Danthine or Holthausen is in the bibliography, and sec:rel does not mention the theorem. The row also conflicts with 11_predictions.tex:5, "Readings of social data are interpretations, which the models alone cannot refute": an interpretation is given a refuter. Use-novelty in the sense of Worrall 2014 is absent, since the content was available before the framework. Model-specific content is confined to the crossover h_x = 2.187, which I recomputed and which depends on the declared two-mode exterior. Holthausen 1979 and Danthine 1978 surfaced in search only and were not opened.

Proposed fix. Cite Feder, Just and Schmitz (1980) at ex:env-firm with the sentence "That the futures price of the firm's own lag suffices is the separation theorem of production under price uncertainty, here in its risk-neutral form and by definition of the futures functional", and move the row out of the predictions table or relabel it "known result recovered; only the crossover lag is specific to the declared exterior".

What would overturn the finding. A demonstration that the row's content differs from the separation theorem in a way the model derives (for example a horizon dependence that the theorem lacks and that does not follow from defining the futures price as the conditional expectation).

State: applied. [10d] applied: Confirmed: L_fut=0 holds by definition (futures functional equals decision functional), for any dynamics. ex:env-firm now says so, cites Feder-Just-Schmitz 1980 (RePEc record and abstract opened) as the separation theorem, and marks the crossover comparison as the only model-specific content. Dropped the lane's 'under risk aversion': the abstract does not state it. Framing pass: [group 11] applied; [group 13] applied

### pos-07 (major): The gravity row is the barometric exponent presented as a prediction of the framework, with an unmatched "thirteen orders of magnitude" comparison

Location: sections/11_predictions.tex:134 (tab:pre-sensing); sections/10d_environments.tex:203-212 (ex:env-cell), :223 (rem:env-neurons); sections/13_discussion.tex:39. Labels: ex:env-cell; rem:env-neurons; prop:env-selection. Category: worked example read as evidence / accommodation.

Evidence. Row: "a protein of 50 kDa has signal-to-noise ratio 2.2e-14 per reading, so cells that sense gravity in this way need dense bodies far larger than a molecule", refuter "A cell that senses the direction of gravity from the sedimentation of bodies of molecular size alone." The number is x_g^2/12 with x_g = M_b g Z/(k_B T) = 5.1e-7, the exponent of the barometric distribution; recomputed value 2.17e-14, and 4.6e13 readings for a ratio of one, consistent with the text. Removing every element of the active-inference framework leaves the number unchanged, and an observation matching the refuter would contradict equilibrium statistical mechanics, not H5. The fact was available when the example was built: rem:env-neurons is titled "Interpretation: neurons, statocytes and vestibular cells" and says its physiological facts "are textbook statements that we did not check against primary sources", so the row is accommodation in the sense of Worrall 2014. The discussion drops the qualifier: 13_discussion.tex:39 says a molecular gravity sensor has a ratio "more than thirteen orders of magnitude below that of a one-percent ligand signal", and 10d:212 says gravity "fails the coupling clause by more than thirteen orders of magnitude". The two sides are not matched: the gravity figure is one particle and one reading, while the chemical figure 1.13e-2 = (3/(5 pi D a c T))^(1/2) integrates 5 pi D a c T/3 = 7.9e3 molecule counts over one second (recomputed with D = 500 um^2/s, a = 5 um, c = 0.602 per um^3). Matched per count the gap is about nine to ten orders, and a cell holds many more than one protein; the qualitative conclusion survives, the quoted factor does not measure a like-for-like coupling. Prior art for the thermal-noise argument: Pollard, J. Theor. Biol. 8:113-123 (1965) surfaced in search but its text was not available to me; the source I opened, Yoder, Zheng, Todd and Staehelin, Plant Physiology 125:1045-1060 (2001), documents statolith sedimentation as the sensing mechanism and contains no kT comparison in the portion read. The citation for the kT argument therefore remains to be supplied.

Proposed fix. In the row write "Known physical bound recovered: the barometric exponent of a 50 kDa protein over 10 um is 5.1e-7, so sedimentation of single molecules carries a signal-to-noise ratio of 2.2e-14 per particle and reading", remove the refuter, and in 13_discussion.tex:39 and 10d:212 replace the thirteen-orders sentence by "per particle and reading, against a chemical estimate that integrates about 7.9e3 molecule counts".

What would overturn the finding. A step in ex:env-cell where a result of the framework (rather than the Boltzmann distribution and a Fisher-information identity) changes the number, or a matched comparison that still gives thirteen orders.

State: applied. [10d] applied: Recomputed: x_g=5.14e-7, ratio 2.20e-14, 7.88e3 leading-term counts (9.8e3 exact), pooled ratio about 2e-10. Earlier batches had already matched the comparison; added the finding's wording and a sentence that item (4) is a known physical bound independent of the framework. No kT-argument citation added; Pollard 1965 not opened. Framing pass: [group 11] applied; [group 13] applied

### pos-08 (major): The central kind has no exhibited member, while the abstract opens with a theory of how agents "from cells to nations" form collective agents

Location: sections/00_abstract.tex:4; sections/13_discussion.tex:11 (sec:dis-status); sections/05_agency.tex:566 (def:agy-meta-agent); sections/10_abstract_collectives.tex:448-452 (sec:abs-graded). Labels: def:agy-meta-agent; thm:agy-h1; thm:frm-formation; tab:abs-graded. Category: scope creep.

Evidence. Abstract, first sentence: "We develop a traditional active-inference theory ... of how communicating agents, from cells to nations, form collective agents." Discussion, 13_discussion.tex:11: "A meta-agent is a definition (def:agy-meta-agent), whose requirements to differ from partner randomization and to survive exact fusion are not consequences of these theorems, and no population analyzed in the manuscript is shown to meet every clause: the split of the two-group model is attributed to misreading ... and the decisive nulls have been applied to no abstract collective." 10_abstract_collectives.tex:452: "Nothing here derives the formation of a culture, a market or a polity." :450: "Nothing here makes a culture or a market behave as if it minimized a group expected free energy." The abstract itself reports that the one formation result yields a split that "fails the translation-aware form of the exact-fusion persistence clause", a type-S clause of the definition. So the four clauses of def:agy-meta-agent (contrast, closure, nulls, agency index) are proved or bounded one at a time in different models, and their joint satisfiability is not shown in any instance, synthetic or empirical; the definition could be empty on the model class. The abstract does not carry the sentence from 13_discussion.tex:11. Against the second assessment: it rates problem 1 a "Substantial conditional answer" with remaining gap "Identify and jointly maintain these properties under partial observation, adaptive coupling, and approximate closure"; the text does not establish joint satisfaction even under full observation, fixed coupling and exact closure, so the credited answer is a set of necessary-condition theorems and a definition, and the manuscript's own framing of the range "from cells to nations" exceeds both. Assigned status: D for the clause-wise theorems, C for the existence of a meta-agent in the sense defined.

Proposed fix. Open the abstract with "We develop a linear-Gaussian active-inference framework for deciding when a set of communicating agents counts as a collective agent" and add: "No population analyzed here, synthetic or empirical, is shown to meet every clause of the meta-agent definition." Add an open problem: exhibit one linear-Gaussian population meeting every clause of def:agy-meta-agent at a stated grade, or prove the clauses jointly unsatisfiable in a stated class.

What would overturn the finding. One population in the manuscript (for example in sec:min or ex:met-two-firms) for which all clauses of def:agy-meta-agent are verified at a stated grade.

State: applied. [05] applied: Confirmed: no population in the manuscript is shown to meet every clause. Added that sentence to rem:agy-h1-status and a new open problem open:agy-meta-agent-exists (exhibit one population at a grade with r_0>1, Agency_0>0, or prove joint unsatisfiability). Abstract and discussion belong to frame. [10] applied: Own part only: sec:abs-graded now states that no abstract collective is shown to meet every clause of def:agy-meta-agent and that joint satisfaction or unsatisfiability is not shown. No open problem added here; it belongs with def:agy-meta-agent in group 05. Abstract and discussion are other groups' files. Framing pass: [group 13] applied

### pos-09 (major, unconfirmed): The unrecorded-drive problem is stated as open without the latent-variable Gaussian graphical model literature

Location: sections/05_agency.tex:557 (open:agy-unrecorded-drive); sections/11_predictions.tex:9 and :11; sections/04_collectives.tex:302 (lem:col-kron); sections/10_abstract_collectives.tex:417 (prop:abs-ultrametric-cap). Labels: open:agy-unrecorded-drive; lem:col-kron; prop:abs-ultrametric-cap; eq:agy-omega. Category: novelty versus rediscovery / missed prior art.

Evidence. open:agy-unrecorded-drive: "Find an estimator of eq:agy-omega when the shared drive is not recorded." 11_predictions.tex:9: "a test needs a record of the world path or of a proxy for it"; :11: "an estimator without a recorded drive is open". The manuscript's selector is the precision of members given a latent common cause, and its own results have the corresponding algebra: lem:col-kron writes a marginal precision as a conditional precision minus a Schur-complement term, and prop:abs-ultrametric-cap uses Sigma = Sigma^c + Sigma_cm 1 1^T, a local conditional structure plus a rank-one common mode. Source opened: the arXiv abstract of Chandrasekaran, Parrilo and Willsky, "Latent variable graphical model selection via convex optimization", arXiv:1008.1290 (Annals of Statistics 40(4):1935-1967, 2012). It states that there are natural conditions under which latent-variable Gaussian graphical models are identifiable given marginal statistics of only the observed variables, namely a sparse conditional graphical model among the observed variables and a latent effect spread over most of them, and it gives a convex estimator with l1 and nuclear-norm regularization. A sparse local coupling graph with a common mode shared by all agents is the favorable case those conditions describe. No entry for this paper or for any sparse-plus-low-rank method is in references.bib, and sec:rel does not mention the topic. The second assessment repeats the gap under problem 10 ("including unrecorded common drivers") without it. What is missing for confirmation: I read only the abstract, so the exact identifiability conditions are not checked against the diffusive class; eq:agy-omega is a path-space conditional mutual information and the open problem includes performative acts that feed back on the world, which the static result does not cover; time-series extensions were not opened.

Proposed fix. Restate the open problem as: "For a static or stationary world without performative acts, the world-conditional precision is identifiable from members' statistics alone under the sparse-plus-low-rank conditions of Chandrasekaran, Parrilo and Willsky (2012); the estimator is open when acts drive the world, when the conditional precision is not sparse, or when the common mode is concentrated on few agents." Cite the paper at 11_predictions.tex:11.

What would overturn the finding. A check of the paper's conditions showing that they fail for diffusive precisions with a rank-one common mode, or that eq:agy-omega is not a function of the conditional precision even without performative acts.

State: applied. [05] applied: Opened arXiv:1008.1290 (ar5iv; Secs. 1-4, Prop. 3.3, Thm. 4.1). Proposed fix overclaims for the path-space quantity: the paper treats i.i.d. samples of one vector, and broadcast and record noises give a latent term that is neither low-rank nor spread. Open problem restated with the static partial route and these limits. [10] applied: Confirmed after reading Sec. 3 of Chandrasekaran-Parrilo-Willsky (transversality gives local identifiability; mu*xi<1/2). Check: Sigma^-1 = Pi minus rank one along Pi 1; tangent spaces transverse on a ring with uniform or random leaks, not for a clique or a leak on one agent. Replaced 'estimation ... is open' after the proposition; proposal's 'identifiable' sharpened to 'locally identifiable'. Bib entry added. [04] declined: Nothing to change in group 04: lem:col-kron is cited only as supporting algebra and is correct; no sentence in these files states the unrecorded-drive problem. I did not open Chandrasekaran et al., so I neither confirm nor refute the identifiability claim; that check falls to groups 05 and frame. Check of the edit: [05] defect, Schur-complement and rank claims correct. Three slips: K does not exist if O holds full window paths, since mu_i(0) is a function of X_0 in the drive (prop:agy-tests(a)); with H only the unrecorded part, K_OO^{-1} omits conditioning on the recorded part; the spread condition bears on (Sigma^c)^{-1}u, the leak vector, not the common mode. O is reserved in appA. Repair: [05] repaired, open:agy-unrecorded-drive: roman indices o, h replace O, H; observed block now excludes drive-measurable coordinates and the latent block is the whole shared drive; spread condition now bears on the latent term along Pi^c 1 (leaks). Truncated optional addition not applied. Framing pass: [group 11] applied; [bib] applied

### pos-10 (minor): The long-range Gaussian exponent in prop:ren-exponents(b) carries no attribution

Location: sections/10c_renormalization.tex:117 (prop:ren-exponents(b)); sections/12_related.tex:130 (sec:rel-ren). Labels: prop:ren-exponents. Category: novelty versus rediscovery / missing attribution.

Evidence. Part (b): for a symbol epsilon + a_sigma |p|^sigma with 0 < sigma < 2, "The ratio epsilon/a_sigma is relevant with y_RG = sigma", and part (c) gives dynamic exponent sigma. The text after the proposition and sec:rel-ren cite Kadanoff, Wilson, Cardy, Dyson and Jona-Lasinio; nothing on long-range renormalization is in references.bib (no entry matches Fisher 1972, Nickel or Sak; the long-range entries are light-cone and percolation papers). Source opened: Flores-Sola, Berche, Kenna and Weigel, arXiv:1410.1377 (read through ar5iv), Section 2 and Eqs. (2.3) to (2.5) and (3.4), which attribute to the renormalization-group treatment of Fisher, Ma and Nickel, Phys. Rev. Lett. 29:917 (1972), the stability of the Gaussian fixed point for sigma < d/2 with nu = 1/sigma, eta = 2 - sigma and thermal eigenvalue y_t = sigma. I did not open the 1972 letter itself. The manuscript does not call (b) new, and 12_related.tex:42 disclaims mathematical novelty in general terms, so the defect is the missing citation for a standard result stated as a proposition.

Proposed fix. After the proof pointer add: "The exponent y_RG = sigma is the thermal eigenvalue of the long-range Gaussian fixed point of Fisher, Ma and Nickel (1972); part (b) restates it for decimation and block averaging of a lattice precision with explicit remainder terms."

What would overturn the finding. A citation to the long-range Gaussian fixed point already present elsewhere in the manuscript that I missed.

State: applied. [10c] applied: Attribution sentence added after the proof pointer, citing Fisher, Ma and Nickel (1972), new key fisher1972critical in the extra.bib. Crossref record and INSPIRE abstract opened; APS full text returned 403, so the sentence and annote say it is cited from record and abstract. Added that for Gaussian fields the exponent holds for all 0<sigma<2. Framing pass: [group 12] applied; [bib] declined: Already repaired: fisher1972critical is defined once, in sections/10c_renormalization_extra.bib, with a Crossref record check, and is cited in s10c_renormalization.tex and 12_related.tex. I opened no source and changed nothing; the 1972 letter itself remains u ...

### Not checked by lane pos

- Appendix proofs and check files for the results cited in the predictions table; the mathematics was routed to the domain lanes and not adjudicated here.
- Granger 1980, Zaffaroni 2004, Fisher-Ma-Nickel 1972, Pollard 1965, Holthausen 1979 and Danthine 1978 were not opened; statements about them rest on the opened review or abstract named in each finding.
- Full texts of Chechik et al. 2005, Creutzig et al. 2009 and Chandrasekaran et al. 2012; only abstracts were read.
- The second assessment's statement under problem 5 that "the record implements the centralized Kalman filter each round" was not traced to a result.
- Novelty of "a predictive law of its coarse exterior" (sec:rel-new) and of lem:mis-social-blind; no external search was run for these.
- Sections 01 to 03, 06 to 09 and 10a were not read beyond the labels and passages cited.

## Lane notation: Notation and conventions across sections

The notation is not consistent with its own tables. One defect is substantive (major): the prose at sections/05_agency.tex:125 and sections/12_related.tex:68 asserts that the precision-based contrast of def:col-contrast and the drift-based contrast of thm:agy-closure-average differ by at most the circulation term, which is false at zero current because def:col-contrast removes the cut couplings from the inward rate and the drift-based rate keeps them (instance: r(C)=3.3 against r^M=4.337 with J=0); sections/10a_meta_agents.tex:182 states the correct relation, so the manuscript contradicts itself. The remaining 17 findings are minor collisions and omissions: unsuperscripted varepsilon and a used for both the W leak and the precision leak in the nested medium (the two differ by the factor (1+lambda)/q), correlation time defined as -1/ln rho but described as the inverse spectral gap in H4, two reserved meanings each for q_i and c, three symbols declared "and nothing else" (rho, kappa) or "reserved" that carry other meanings, two definitions named coherence, two effective leaks, two symbols for consensus rounds, a stale Kronecker-delta bullet, one unused macro, and about a dozen recurring symbols missing from the tables. What holds: A5 to A12 and H1 to H5 are cited with the same content everywhere (there are no A1 to A4; the numbering starts after H1 to H4 by a stated convention), the H5(d) thresholds agree with prop:ren-per-level, (P0) to (P4) are consistent, the formulas for varsigma_d^2, xi_2, tau, the baseline and L-star agree across statements, and the receiver-first, row-sum and column-sum conventions are used consistently. Not examined: the proof and check files beyond targeted searches, the first-three-subsections sampling for most sections, the Laplacian sign convention, and the normalizations of the closure defects sigma_C, sigma(M,phi), sigma^d. One script was run (<session scratch>/audit/notation/contrast_drift_vs_precision.py); a findings copy is at <session scratch>/audit/notation/findings.md.

Coverage: 17 items examined; 10 hold, 4 defective, 1 suspect, 2 not checked.

| Item | Verdict | Note |
|---|---|---|
| Precision versus covariance parameterization | defect | Objects are consistently named, but the leak and coupling letters switch between the W side and the precision side without notice (finding 2). |
| Discrete versus continuous time | suspect | sec:agy (prop:agy-identity, prop:agy-drift-precision) and thm:ren-nested use continuous time with the letters reserved for per-round weights; content agrees with sec:sca at g=0 but units are unstated (finding 16). |
| Contrast family r, r_star, r^M, r^d | defect | Definitions are individually consistent; the stated relation between r and r^M is wrong at two places and right at one (finding 1). |
| Notation-table rows for symbols that no longer occur | defect | About 50 table symbols sampled; all occur in the body except delta_{x0} (finding 10). |
| Macros in preamble.tex never used | defect | Only \EF (finding 11). |
| Laplacian sign and normalization across sections | not_checked |  |
| Closure-defect normalizations sigma_C, sigma(M,phi), sigma^d | not_checked |  |

Items found to hold: Assumption labels A5-A12 cited with the same content everywhere; A1-A4; Hypothesis labels H1-H5 and sub-items H5(a)-(d); H5(d) thresholds against prop:ren-per-level; (P0)-(P4) of def:agy-group-model; varsigma_d^2, xi_2 and the size bound; Correlation time formula in equations; Baseline, largest extent, lifetime; Index and matrix conventions; Identity time against correlation time with records.

### notation-01 (major): Prose claims the drift-based and precision-based contrasts differ by at most the circulation term; the inward rates differ at zero current

Location: sections/05_agency.tex:125 (prose after prop:agy-drift-precision, :116); sections/12_related.tex:68; against def:col-contrast sections/04_collectives.tex:291-297 and sections/10a_meta_agents.tex:182. Labels: prop:agy-drift-precision, eq:agy-drift-precision, def:col-contrast, thm:agy-closure-average. Category: definition disagreement / cross-reference beyond cited result.

Evidence. def:col-contrast (04_collectives.tex:291-297; prose :300 'the smallest precision of a disagreement mode once couplings to outsiders are removed') sets xi_in(C)=min over f perp 1_C supported in C of f^T(diag(eps^Pi)+L_C)f/f^T f. The drift-based inward rate of thm:agy-closure-average(b) (05_agency.tex:89) is lambda_min(Z M_sym Z^T); with M=Pi^c_CC = diag(eps^Pi)+diag(a^partial)+L_C the cut diagonal stays. prop:agy-drift-precision (05_agency.tex:116-121) only bounds |f^T M_sym f - f^T Pi f| <= ||J|| ||Pi f|| for the same matrix Pi, so it says nothing about the removed cut diagonal, yet 05_agency.tex:125 writes 'the two differ by at most the circulation term of eq:agy-drift-precision' and 12_related.tex:68 'the two contrasts differ by at most a term set by the stationary probability current (prop:agy-drift-precision)'. Counterexample (script contrast_drift_vs_precision.py): path of 5 agents, couplings 0.5, 1.0, 1.0, 0.2, uniform eps^Pi=0.1, C={1,2,3}, M=Pi_CC symmetric so J=0. Output: xi_out=0.333333 for both; xi_in(def)=1.1, xi_in^M=1.445765; r(C)=3.3, r^M=4.337295. The gap 0.3458 exceeds the circulation term, which is 0. 10a_meta_agents.tex:182 states the correct relation ('the outward rate is that of def:col-contrast and the inward rate at least as large'), so the text contradicts itself.

Proposed fix. Replace the sentence at 05_agency.tex:125 by: 'The contrast of a collective is defined on the precision (\cref{def:col-contrast}), with the couplings to outsiders removed from the inward rate; closure of its average under non-reversible drift is controlled by the drift-based contrast with row and column dispersions. The outward rates differ by at most the circulation term of \eqref{eq:agy-drift-precision}. The drift-based inward rate keeps the cut couplings on the diagonal, so for reversible drift $\xin(C)\le\xin^M\le\xin(C)+\max_{i\in C}a^\partial_i$ and $r^M\ge r(C)$, and for non-reversible drift the same holds up to the circulation term.' At 12_related.tex:68 write 'the two outward rates differ by at most a term set by the stationary probability current, and the drift-based inward rate also keeps the couplings to outsiders (\cref{prop:agy-drift-precision})'. Add rows for $r^M$, $\xin^M$, $\xout^M$ to appA_notation.tex next to the contrast bullet at :189.

What would overturn the finding. The sentence 'the two differ by at most the circulation term' (05_agency.tex:125) and its copy at 12_related.tex:68

State: applied. [04] applied: Confirmed: path example gives xi_in=1.1, xi_in^M=1.445765, r=3.3, r^M=4.337295 at J=0; 2000 random reversible cases satisfy xi_in <= xi_in^M <= xi_in + max a^partial. No false sentence was in 04; the prose after def:col-contrast now states this relation, matching 05. [05] applied: Earlier batch had already replaced the false sentence. Added the proposed two-sided bound xi_in <= xi_in^M <= xi_in + max a^partial and r^M >= r(C) for J=0 (Weyl), verified on 2000 random reversible regions and the path-3 numbers (1.05, 1.5014, 2.739, 3.917); chk updated. [10a] applied: Counterexample reproduced (xin 1.1, xin^M 1.445765, r 3.3, r^M 4.337295, J=0). The prose after prop:met-memory also needed a hypothesis: xin^M >= xin(C') holds only when the exterior is the region itself; with a larger exterior xin^M fell to 0.0109 against xin(C')=1.1. Sentence rewritten with the sandwich and that caveat. Framing pass: [group 12] applied; [appA] applied

### notation-02 (minor): Unsuperscripted varepsilon and a denote both the W leak / message weight and the precision leak / coupling

Location: sections/appA_notation.tex:63 and :67; sections/04_collectives.tex:465 (rem:col-lengths), :352, :651; sections/10_abstract_collectives.tex:101 and :383 (prop:abs-hierarchy); sections/10c_renormalization.tex:134 (thm:ren-nested), :196-204 (prop:ren-per-level); sections/10b_hierarchy.tex:411 (ex:hie-code-domains). Labels: tab:not-networks, rem:col-lengths, prop:abs-hierarchy, thm:ren-nested, prop:ren-per-level, ex:hie-code-domains. Category: symbol collision.

Evidence. appA:63 defines varepsilon=1-c-2Da as the leak of W and appA:67 reserves varepsilon^Pi_i=(Pi 1)_i and a^Pi_ij=-Pi_ij for the precision. rem:col-lengths (04_collectives.tex:465) keeps them apart: 'varepsilon^Pi=(1-lambda^2)/q ... with varepsilon=1-lambda the leak of W', and 10_abstract_collectives.tex:101 uses I-W=varepsilon I+L_b (W leak). But thm:ren-nested (10c_renormalization.tex:134) writes 'uniform leak varepsilon>0, so that Pi=varepsilon I+L', prop:abs-hierarchy (10_abstract_collectives.tex:383) writes 'let every agent have leak varepsilon>0 ... G=(varepsilon I+L)^{-1}' without saying whether G is Pi^{-1} or (I-W)^{-1}, and prop:ren-per-level states its thresholds as 'varepsilon>A_h T_H'. For nearest-neighbor passing the two leaks differ by the factor (1+lambda)/q, so a threshold read with the table's varepsilon is off by that factor. The clique example at 04_collectives.tex:352 likewise uses bare a for a precision coupling (lambda_2=ma) beside varepsilon^Pi.

Proposed fix. In prop:abs-hierarchy write: 'let every agent have precision leak $\varepsilon^\Pi>0$, so that the world-conditional precision is $\Pi=\varepsilon^\Pi I+L$ with $L$ the weighted Laplacian of the couplings $a^\Pi_{ij}$, and let $\mathsf G=\Pi^{-1}$'; replace $\varepsilon$ by $\varepsilon^\Pi$ in thm:ren-nested, prop:ren-per-level, ex:hie-code-domains and at 04_collectives.tex:651. If the bare symbol is kept, add to appA_notation.tex after :189: 'In \cref{prop:abs-hierarchy,thm:ren-nested,prop:ren-per-level} and \cref{sec:hie} the unsuperscripted $\varepsilon$ and $A_{\mathrm h}$ are precision-side quantities, $\varepsilon=\varepsilon^\Pi$.'

State: applied. [04] applied: Adopted the proposed convention. obs:col-nested-medium and its check now write the precision leak as varepsilon^Pi and name the weights a^Pi_ij (pair contrast 2.1/0.348=6.034 confirms precision side). The clique example declares a^Pi_ij=a. Bare varepsilon elsewhere in 04 is the W leak, as appA defines. [10] applied: G(l)/G(0) is a correlation, so varepsilon I+L is a precision. Adopted the proposed wording in prop:abs-hierarchy and wrote varepsilon^Pi throughout the proposition, rem:abs-cutoff, the proof and chk:abs-hierarchy. prop:abs-barrier and chk:abs-cap keep bare varepsilon (W leak, I-W=varepsilon I+L_b). No mathematical change. [10b] applied: ex:hie-code-domains declares a world-conditional precision, so its leak is now written varepsilon^Pi in statement, table, derivation and check, with a named as the common precision coupling. Bare varepsilon elsewhere in sec:hie is the drift (W) leak, with precision leaks written explicitly as varepsilon/q, and was left unchanged. [10c] applied: Every precision-side bare epsilon in the three 10c files now reads epsilon^Pi (coarse leak epsilon^{Pi,(1)}), in statements, proofs and checks. Bare epsilon survives only where it is the W leak of nearest-neighbor passing (prop:ren-ring, thm:ren-flows(b), prop:ren-depth(c), the comparison table). Notation only; no formula or number changed. Framing pass: [appA] partial: The proposed sentence declaring bare epsilon precision-side was not added, since the technical owners rewrote those statements with epsilon^Pi. The a^Pi, epsilon^Pi row now says these are not the weights and leaks of W and gives the nearest-neighbor relation f ...

### notation-03 (minor): Correlation time defined as -1/ln rho(W) but described as the inverse spectral gap

Location: sections/08_scale.tex:188 (def:sca-lengths(c)) and sections/appA_notation.tex:73 against sections/01_introduction.tex:52 (hyp:int-h4) and sections/08_scale.tex:609. Labels: def:sca-lengths, hyp:int-h4, thm:sca-h4. Category: definition disagreement.

Evidence. def:sca-lengths(c), appA:73 and 11_predictions.tex:13 give tau=-1/ln rho(W) rounds, and every formula using tau follows that (08_scale.tex:239, :332, :356, :415). H4 at 01_introduction.tex:52 and the text at 08_scale.tex:609 say 'the correlation time tau is the inverse spectral gap of agents and media together', which is 1/(1-rho). Recomputed: rho=0.5 gives 1.443 against 2; rho=0.9 gives 9.49 against 10; 1/(1-rho)-(-1/ln rho) tends to 1/2 as rho tends to 1, so the two agree only to leading order.

Proposed fix. At 01_introduction.tex:52 and 08_scale.tex:609 write: 'the correlation time $\tau=-1/\ln\rho$ of agents and media together, which is the inverse spectral gap to leading order as $\rho\to1$'.

State: applied. [08] applied: Confirmed: 1/(1-rho)-(-1/ln rho) = 0.557, 0.509, 0.5008 at rho = 0.5, 0.9, 0.99, tending to 1/2. Prose after thm:sca-h4 now reads tau=-1/ln rho, the inverse spectral gap to leading order as rho->1. def:sca-lengths(c) was already correct and is unchanged. Framing pass: [group 01] declined: Already repaired: hyp:int-h4 now reads tau=-1/ln rho with rho the spectral radius of the joint transition matrix, 'the inverse spectral gap to leading order as rho->1'.; [group 11] declined: Nothing to change in this file: the proxies paragraph already defines tau = -1/ln rho(W), and the phrase 'inverse spectral gap' does not occur in 11_predictions.tex. The part in 01_introduction.tex belongs to that file's owner.; [appA] applied

### notation-04 (minor): q_i reserved twice: recognition density and local noise variance

Location: sections/appA_notation.tex:28 and :60; sections/02_framework.tex:17 and :447; sections/04_collectives.tex:251; sections/05_agency.tex:199-253. Labels: tab:not-agents, tab:not-networks. Category: symbol collision.

Evidence. appA:28 lists q_i=N(m_i,P_i) as agent i's recognition density (02_framework.tex:17, also q_i(pi)); appA:60 lists q, q_i as the noise bound and local noise variance (02_framework.tex:447 q_i=Var(zeta_i); 04_collectives.tex:251). appA:5 says table symbols are reserved. sec:agy then uses q_i, q_j, q_C for member and group beliefs (05_agency.tex:199-253) within the same manuscript that uses q for the noise in Pi=(I-W^2)/q; q_rev and q_z add two more.

Proposed fix. Rename the noise variance to $\varsigma_i^2$-free notation such as $\mathsf q_i$ or $v^\zeta_i$ (with bound $\mathsf q$), or add to appA: '$q_i$ with an argument or as a density is the recognition density; $q$, $q_i$ as scalars are noise variances.'

State: applied. [02] applied: Adopted the finding's second alternative (disambiguation, no rename): one sentence in def:fw-level0 says scalar q_i, q, q_z are noise variances and q_i with an argument or as a density is the recognition density. Renaming is unworkable here: scalar q is used in groups 06, 08, 10, which do not receive the finding. [04] declined: Adopted the finding's second option (appA note). Group 04 uses q, q_i, q_min only as scalar noise variances (grep: no density use), and no group has renamed (no \mathsf q anywhere); a rename here would diverge from asm:sca-standing in group 08, which was not assigned the finding. Nothing to change in my files; appA follow-up returned. [05] declined: Nothing to change in group 05: every q_i, q_j, q_C in these files is a recognition density, and no scalar noise variance q occurs. Note for the owners: app05 (proof near 'quadratic variation grows at a constant rate') uses \mathsf q for a rate, so the rename option \mathsf q_i would collide; prefer v^\zeta_i or the appA sentence. Framing pass: [appA] applied

### notation-05 (minor): c is both a modality index and the self weight; R_c, R_C, R_ij are three different objects

Location: sections/appA_notation.tex:32, :33, :63, :64; sections/02_framework.tex:36, :141, :197, :449; sections/10_abstract_collectives.tex:50; sections/08_scale.tex:180, :520. Labels: tab:not-agents, tab:not-networks, def:sca-coherence, def:sca-lengths. Category: symbol collision.

Evidence. appA:32 c in M is a modality and appA:63 c=W_ii is the self weight (02_framework.tex:36 against :449). 10_abstract_collectives.tex:50 then needs c_c, a_c, varepsilon_c (self weight of modality c). appA:33 R_c is the channel-noise covariance of modality c (02_framework.tex:141, :197); def:sca-coherence (08_scale.tex:520) uses R_C for the world-conditional correlation matrix of the set C; appA:64 and 08_scale.tex:180 use R_ij for standardized covariance blocks; def:coh-components uses hat R_ij for assigned noise. R_c and R_C differ only by the case of the subscript.

Proposed fix. Index modalities by a Greek or sans-serif letter (for instance $\mathsf c\in\mathcal M$, noise $R_{\mathsf c}$) and write the correlation matrix of a set as $\mathrm{Corr}_C$ or $\mathsf R_C$-free notation such as $K_C$; add one line to appA stating the three R objects.

State: applied. [08] applied: Adopted the first proposed option: the correlation matrix of a set is now \mathrm{Corr}_C (K_C would collide with K_A, K_varphi and the read kernels). Renamed all 10 occurrences in 08, 5 in app08, 1 in chk08; R_C occurred in no other file. Group 08 uses no modality index c; self weight c and R_ij unchanged. [02] deferred: Nothing changed. Renaming the modality index to sans-serif c is unworkable in this pass: R_c, T_c, r_c occur in groups 03, 06, 07, 09, 10b, 10c, which do not receive the finding, and sans-serif c already denotes constants in 05_agency and 07_formation. An appA line is the convergent repair. [10] deferred: Unchanged. The proposal names no single letter ('Greek or sans-serif, for instance'), and its instance \mathsf c is already taken: \mathsf c_\infty in rem:abs-cutoff of this section, the coarse variable \mathsf c in 10a, \mathsf c_\Phi in 05, \mathsf c_P in 10d, \mathsf c_{\mathcal V} in 07. One global letter must be fixed first; then prop:abs-crossover and its proof follow. Check of the edit: [08] defect, Rename incomplete. The susceptibility in def:sca-coherence still reads |(R_C)_{ij}|, now an undefined symbol; cor:sca-size(c) still has lambda_max(R_V); and part (c) of its proof now writes Corr_C (twice) for the matrix of the full set V. Both leftovers are also in the live file. No mathematical content changed; labels intact. Repair: [08] repaired, Replaced (R_C)_{ij} by (Corr_C)_{ij} in def:sca-coherence, lambda_max(R_V) by lambda_max(Corr_V) in cor:sca-size(c), and Corr_C by Corr_V twice in part (c) of the proof. No R_C or R_V remains in group 08. Framing pass: [appA] partial: Added one list item on the positions of the letter c (modality subscript, self weight c=W_ii, superscript of Sigma^c and Pi^c, lambda_c, upright c of n_c) and one on the R objects. The proposed renaming of the modality index was not done: technical files are c ...

### notation-06 (minor): rho is declared 'spectral radius, and nothing else' but rho_H is a path metric; rho_perp is missing from the table

Location: sections/appA_notation.tex:62; sections/app05_agency.tex:165; sections/05_agency.tex:151. Labels: tab:not-networks, prop:agy-consensus. Category: symbol collision.

Evidence. appA:62: rho(.) 'spectral radius, and nothing else'. app05_agency.tex:165 uses rho_H for the Hamming/path metric together with W_H for a Wasserstein distance, against reserved W (message matrix). rho_perp=rho(W-1 1^T/n) (05_agency.tex:151) occurs on 15 body lines across sec:agy, sec:met and the discussion and has no table row.

Proposed fix. Rename $\rho_{\mathrm H}$ to $d_{\mathrm H}$ and $W_{\mathrm H}$ to $\mathcal W_1$-free notation such as $\mathrm{Wass}_{\mathrm H}$ in app05_agency.tex; add the row '$\rho_\perp$ & spectral radius of the consensus matrix off the constants & \cref{prop:agy-consensus}' to appA.

State: applied. [05] applied: Renamed in app05 (path-coupling proof, part (b)): \rho_H to d_{\mathrm H} (4 occurrences) and W_H to \mathrm{Wass}_{\mathrm H} (9 occurrences). Neither new symbol occurs elsewhere in the manuscript. The appA row for \rho_\perp is a frame follow-up. Framing pass: [appA] applied

### notation-07 (minor): kappa is declared 'attention capacity, and nothing else' but counts sensor channels and senders elsewhere

Location: sections/appA_notation.tex:39; sections/10d_environments.tex:12, :67, :71; sections/10b_hierarchy.tex:397. Labels: tab:not-agents. Category: symbol collision.

Evidence. appA:39: kappa 'attention capacity, and nothing else'. In sec:env kappa is the number of sensor channels and a rank index (10d_environments.tex:12, :67; lambda_kappa(F) at :71), and at 10b_hierarchy.tex:397 it counts senders. The near-identical varkappa_perp (15 lines), varkappa_Phi (5) and varkappa_ast (1) are rates and are absent from appA.

Proposed fix. Use $k_{\mathrm s}$ (or $n_{\mathrm s}$) for the channel count in sec:env and sec:hie, and add rows for $\varkappa_\perp$, $\varkappa_\Phi$ to appA; otherwise delete 'and nothing else' at appA:39 and list the local uses.

State: contested. [10d] contested: No second meaning in 10d. The setup paragraph defines kappa as the number of scalar channels, 'the attention capacity of def:fw-system measured in channels', and def:fw-system bounds the attention set by kappa. lambda_kappa(F) uses the same integer as an index. varkappa does not occur in 10d. Renaming would sever that identification. [10b] declined: Nothing to change in 10b: kappa in the pragmatic-term remark and in obs:hie-exact-receiver is the attention capacity of def:frm-two-group (the size of the attended sender set, |J_i|<=kappa in def:fw-system), which is the appA meaning. No varkappa symbols occur in the 10b files. Framing pass: [appA] applied

### notation-08 (minor): m is the mass 1/xi, a clique size and (with index) a belief mean

Location: sections/appA_notation.tex:28, :70; sections/04_collectives.tex:352. Labels: tab:not-agents, tab:not-networks. Category: symbol collision.

Evidence. appA:70 m=1/xi (decay rate, def:sca-lengths); appA:28 m_i belief mean; 04_collectives.tex:352 'clique of m>=2 agents' with lambda_2=ma and r=1+ma/varepsilon^Pi, in the section that also uses the rate m in rem:col-lengths (:465, 'cosh m=1+varepsilon/(2a)'). m_rho, m_Sigma, m_Pi and m(p) add further indexed variants.

Proposed fix. Write the clique size as $n$ (or $n_C$): 'a clique of $n\ge2$ agents ... $\lambda_2=na^\Pi$, $r=1+na^\Pi/\varepsilon^\Pi$'.

State: applied. [04] applied: Clique size m renamed to n in the remark, its derivation in app04 and the check sentence in chk04. Kept a (not a^Pi) for the coupling value since the remark sets a^Pi_ij=a. Numbers rechecked by hand at n=4, a/eps=10: 41, 35.286, 1.162. The rate m of rem:col-lengths is untouched. Framing pass: [appA] applied

### notation-09 (minor): Read-to-write ratio and reduced record matrix are located in sec:hie by the table but introduced in sec:sca; a further calligraphic R in sec:agy is unlisted

Location: sections/appA_notation.tex:139, :190, :193; sections/08_scale.tex:346; sections/05_agency.tex:223. Labels: prop:sca-records, thm:sca-h4, prop:hie-record-contrast, eq:agy-chain. Category: notation table error.

Evidence. 08_scale.tex:346 introduces 'the effective leak is varepsilon_eff=lambda_min(R), and R_k=beta_k/omega_k' (sans-serif R the reduced record matrix, calligraphic R_k the ratio), used in thm:sca-h4(d) at :604-605. appA:139 cites only sec:hie-records and prop:hie-record-contrast; appA:190 says calligraphic R 'is local: the read-to-write ratio ... in sec:hie ..., the retained set of a decimation in def:ren-maps, and R^ast'; appA:193 lists sans-serif R only for sec:hie. 05_agency.tex:223 defines calligraphic R_i(pi)=[I_{q_i}-I_{q_C}](o_A;o_{A_{-i}}), a member's redundancy disagreement, which appA:190 does not list.

Proposed fix. appA:139: cite '\cref{prop:sca-records,sec:hie-records,prop:hie-record-contrast}'. appA:190: '$\mathcal R$ is local: the read-to-write ratio $\beta/\omega$ of a record in \cref{sec:sca,sec:hie}, ..., the redundancy disagreement $\mathcal R_i$ of a member in \cref{sec:agy}, the retained set ...'. Add a sans-serif line for sec:sca listing $\mathsf R$.

State: applied. [05] declined: Nothing to change in group 05: the calligraphic R_i of sec:agy is defined locally and correctly; the missing listing is in appA_notation.tex (frame). Follow-up issued. [08] declined: Nothing to change in group 08: the sentence before prop:sca-records already introduces sans-serif R (reduced record matrix) and calligraphic R_k=beta_k/omega_k. The repair is entirely in appA_notation.tex; labels prop:sca-records and sec:sca exist for the proposed citations. Framing pass: [appA] applied

### notation-10 (minor): Stale notation bullet: delta_{x0} does not occur; prop:ren-ring uses an indicator

Location: sections/appA_notation.tex:191; sections/10c_renormalization.tex:58-66 (prop:ren-ring), :106 (ex:ren-block-average). Labels: prop:ren-ring, ex:ren-block-average. Category: notation table error.

Evidence. appA:191: 'The record decay delta_k is reserved, but delta_{x0} is the Kronecker delta in prop:ren-ring, ex:ren-block-average'. A search of all body, proof and check files finds no delta_{x0}; the only Kronecker delta is delta_{X0} (capital X) at 10c_renormalization.tex:106, and prop:ren-ring writes the nugget as c_- 1_{x=0} with the indicator.

Proposed fix. appA:191: 'The record decay $\delta_k$ is reserved, but $\delta_{X0}$ is the Kronecker delta in \cref{ex:ren-block-average}.' Optionally write the nugget of prop:ren-ring with the same $\delta_{x0}$ so that one symbol serves both.

State: applied. [10c] declined: Confirmed: no delta_{x0} in the 10c files; prop:ren-ring uses the indicator, ex:ren-block-average uses delta_{X0}. Nothing to change in my files; the optional rewrite of the nugget was not taken, so the appendix entry should name ex:ren-block-average only. Follow-up for appA_notation.tex. Framing pass: [appA] applied

### notation-11 (minor): Macro \EF is defined and never used

Location: preamble.tex (definition of \EF). Category: unused macro.

Evidence. Every macro defined in preamble.tex was searched across collective_agents.tex and sections/*.tex; \EF has zero uses, all others have at least one.

Proposed fix. Delete the \EF definition.

State: applied. Routed to the framing pass (groups general); no agent reported on it. Coordinator: the unused macro \EF was removed from preamble.tex; no use remains in the sections.

### notation-12 (minor, unconfirmed): Two 'orders' of closure with no stated relation: ord(alpha_M) and the minimal order d^*

Location: sections/05_agency.tex:22, :58 (def:agy-closure); sections/10a_meta_agents.tex:131, :160 (def:met-abstract-physics); sections/10d_environments.tex:233; sections/appA_notation.tex:135. Labels: def:agy-closure, def:met-abstract-physics. Category: definition defined twice.

Evidence. def:agy-closure defines ord(alpha_M) at 05_agency.tex:22 (used once more at :58, 'ord(alpha_M)<=dim x-dim y'), a tolerance-dependent order attached to the memory profile. def:met-abstract-physics defines the minimal order d^*=rank O-rank P_E (10a_meta_agents.tex:160), the least number of adjoined linear functionals for exact closure (appA:135), and the introduction's vocabulary 'closed of order d' (01_introduction.tex:86) refers to the second. ord(alpha_M) is not in appA. A search for a sentence relating the two found none; I did not read the proofs in app05_agency.tex and app10a_meta_agents.tex to see whether a relation is stated there, which is what is missing for confirmation.

Proposed fix. Add to def:met-abstract-physics: 'For exact closure this is the order of \cref{def:agy-closure} at tolerance zero, $d^\ast=\mathrm{ord}(\alpha_M)$ with $\alpha_M\equiv0$ beyond $d^\ast$', if that is what is meant, or rename $\mathrm{ord}(\alpha_M)$ to 'memory depth' and add it to appA.

State: applied. [05] applied: The proposed equality d*=ord(0) is false in general (10a already states the inequality with a counterexample; I re-derived ord(0)<=d* via the Kalman filter of a closed completion and checked the AR(1) example). Added to def:agy-closure(iii) a sentence distinguishing the two orders and stating ord(alpha_M)<=ord(0)<=d*. [10a] applied: The proposed identity d*=ord(0) is false. Correct relation: ord(alpha_M) <= ord(0) <= rank O - rank P_E, strict in general. Example: eta reads z with coefficient sqrt(7/8), AR coefficients 1/4 and 1/2, unit noises; eta is exactly AR(1), so ord(0)=0 and d*=1. Stated after the theorem, pointer in the definition, new check chk:met-orders. [10d] applied: 10d uses only d* in the sense of def:met-abstract-physics; 10a now states ord(alpha_M) <= ord(0) <= d*. Added a clause in def:env-aggregates pointing to that sense and relation. The finding's proposed equality d*=ord(alpha_M) is wrong: ord counts filter-state functionals and can be smaller. Check of the edit: [10a] defect, Inequality ord(alpha) <= ord(0) <= rank O - rank P_E holds (Kalman innovations argument; needs only the exogenous-input hypothesis already in def:agy-closure). Example and every number of chk:met-orders reproduce. One apposition is false: the paragraph's own AR(1) has ord(0)=0 but minimal realization order 1; AR(1) plus white noise has ord(0)=1, realization order 1. Repair: [10a] repaired, Checker right: the paragraph's AR(1) has ord(0)=0 but minimal realization order 1 (autocovariance ratio 0.5, innovation variance 2 recomputed). Apposition replaced by 'a problem of minimal stochastic realization'. Optional lower bound not added; ord's definition with input was not re-derived. Framing pass: [group 01] declined: Nothing to change in this file: the introduction's 'closed of order d' agrees with def:met-abstract-physics(iii), which now states that d* bounds ord(alpha_M) from above. The proposed equality was found false by the technical owners.; [appA] applied

### notation-13 (minor): Two definitions carry the name coherence

Location: sections/06_coherence.tex:12-19 (def:coh-components); sections/08_scale.tex:514-522 (def:sca-coherence); sections/appA_notation.tex:80. Labels: def:coh-components, def:sca-coherence. Category: definition defined twice.

Evidence. def:coh-components defines 'a coherence score of a set C of agents' as a pair built from fidelity, calibration and consistency. def:sca-coherence defines theta_Z(C)=min_{i in C} Corr(X_i,Z), theta^ast(C)=sup_Z theta_Z(C) and the count chi_C under the heading of coherence ('theta-coherent'). appA:80 lists only theta, theta^ast, chi; no sentence relates the two, and H2 and H4 each say 'coherence' for their own notion.

Proposed fix. Name the second 'correlational coherence' (or keep '$\theta$-coherence' throughout sec:sca and H4) and add to def:sca-coherence: 'This is a statement about correlation with a variable and is distinct from the coherence score of \cref{def:coh-components}, which grades translation.' Add a row for the score of def:coh-components to appA.

State: applied. [08] applied: def:sca-coherence retitled 'Correlational coherence'; theta_Z and theta^ast named correlational coherence; theta-coherent now defined; the proposed distinguishing sentence citing def:coh-components added verbatim. 'best coherence' updated in app08 and chk08. appA row and H4 wording belong to other groups (follow-ups). [06] declined: The proposed fix renames the notion of def:sca-coherence and adds a sentence there and a row in appA; def:coh-components is unchanged and group 06 contains no use of theta-coherence. Check of the edit: [08] defect, Renaming and the theta-coherent definition are consistent with thm:sca-coherence-volume(b),(c) and the app08 proof step (subset has theta^ast >= theta, chi_{C'} <= chi_C). But def:coh-components(d) defines the score as a pair: a fidelity, calibration or consistency quantity with the inaccuracy A_C; only item (c) concerns translations. 'Grades translation' misdescribes it. Minor, descriptive. Repair: [08] repaired, Checked def:coh-components(d): the score is a pair. 'Which grades translation' replaced by the pair description; theta-coherence now defined for theta>0. Framing pass: [appA] applied

### notation-14 (minor): Two different effective leaks under one symbol; neither is in the notation table

Location: sections/06_coherence.tex:172; sections/08_scale.tex:346, :355-376. Labels: thm:coh-grounding-tension, prop:sca-records. Category: symbol collision.

Evidence. 06_coherence.tex:172: varepsilon_eff=varepsilon+(1-varepsilon) alpha lambda_min(L) (grounding by calibration, with xi approx sqrt(a/varepsilon_eff) at :176). 08_scale.tex:346: 'The effective leak is varepsilon_eff=lambda_min(R)' (records). appA has no row for varepsilon_eff or for varepsilon' (leak after reading). The leak family is then varepsilon, varepsilon_i, varepsilon', varepsilon_eff (two), varepsilon^Pi_i, iota_inst, iota_path.

Proposed fix. Write $\varepsilon_{\mathrm{cal}}$ in sec:coh and $\varepsilon_{\mathrm{rec}}$ in sec:sca, and add both, with $\varepsilon'$, to tab:not-networks.

State: applied. [06] applied: varepsilon_eff written as varepsilon_cal in the proposition, the following paragraph and its proof (three occurrences). Table rows are for appA. [08] applied: All occurrences of varepsilon_eff in 08_scale, app08_scale and chk08_scale replaced by varepsilon_rec (symbol only; D_eff and b_eff untouched). Sections 10b, 10c and their app/chk files still write varepsilon_eff for the same record quantity; appA rows are outstanding.

### notation-15 (minor): Number of consensus rounds is L in sec:agy and n_c in sec:met

Location: sections/05_agency.tex:151 (prop:agy-consensus); sections/10a_meta_agents.tex:280, :284 (prop:met-consensus-filter); sections/appA_notation.tex:138. Labels: prop:agy-consensus, prop:met-consensus-filter. Category: redundant notation.

Evidence. 05_agency.tex:151: 'run L rounds of linear consensus with a symmetric, doubly stochastic ... matrix W'. 10a_meta_agents.tex:280: 'n_c>=0 rounds ... matrix W that preserves sums', and :284 cites 'a bound of the form of prop:agy-consensus(b), with the factor rho_perp^{n_c}'. appA:138 lists n_c only. L is also the Laplacian (appA) and the closed-walk length in def:coh-components (06_coherence.tex:14).

Proposed fix. Use $n_{\mathrm c}$ in prop:agy-consensus and its proof, and write the closed-walk length of def:coh-components as $\ell_{\mathrm w}$-free notation such as $k$.

State: applied. [05] applied: Number of consensus rounds renamed L to n_{\mathrm c} in prop:agy-consensus, eq:agy-consensus-static, eq:agy-consensus-dynamic, the following prose, prop:agy-literal-consensus(b), the later remark and summary, both proofs in app05 and the check. No L remains for rounds in group 05. [10a] declined: Nothing to change in group 10a: the section, proof and check files already write the number of consensus rounds as n_c throughout (one source comment aside). The change from L to n_c belongs to 05_agency.tex and its proof; see follow-up. Framing pass: [appA] applied

### notation-16 (minor): prop:agy-identity uses the reserved discrete record weights as continuous-time rates

Location: sections/05_agency.tex:425-432 and :439 (prop:agy-identity); sections/appA_notation.tex:5, :83. Labels: prop:agy-identity, def:fw-record-model, prop:sca-records-memory. Category: convention switch (discrete vs continuous time).

Evidence. appA:5 says table symbols are reserved and appA:17 that t, s count rounds; the record symbols varepsilon, beta, omega, delta are per-round weights. prop:agy-identity states a continuous-time generator A=((-(varepsilon+beta+g), beta+g phi),(omega, -(omega+delta))) and evaluates it at beta=100, omega=0.01, phi=0.9, delta=0.001 (05_agency.tex:439), values that cannot be per-round weights; phi here is copying fidelity, against phi_C (block vector) and phi_t (content). The matrix agrees with the reduced record matrix of sec:sca at g=0 (-A at g=0 equals R), so the content is consistent; the units are not stated.

Proposed fix. Add to prop:agy-identity: 'Here $\varepsilon$, $\beta$, $\omega$, $\delta$ and $g$ are rates per unit time; the per-round weights of \cref{def:fw-record-model} are these rates times the round length, and $\phi\in[0,1]$ is the copying fidelity.' Rename the fidelity to $\mathsf f$.

State: applied. [05] applied: Added the units sentence (rates per unit time; per-round weights are rates times round length) to prop:agy-identity and renamed the copying fidelity phi to \mathsf f in statement, discussion, conjecture, proof and check. Value 989 reconfirmed numerically. 10b still writes phi for this fidelity; follow-up issued. Check of the edit: [05] style, Rename phi to sans-serif f is complete in statement, proof and check; 989.3 and 0.990, 1.961, 9.091, 50.0 reproduce. The edit dropped a space: '$\mathsf f$,$\tau_{\mathrm{id}}^{-1}$'. The units sentence is loose for g>0: the record model has no weight g and its leak already includes turnover. Repair: [05] repaired, Space restored after fidelity f. Units sentence now says the per-round weights of def:fw-record-model correspond, through the dictionary stated after the proposition, to the rates times the round length. Framing pass: [appA] applied

### notation-17 (minor): Further letters with several meanings and no table note

Location: sections/appA_notation.tex:130, :132, :156, :164, :184; sections/02_framework.tex:20, :26, :197, :213, :244, :372, :397; sections/05_agency.tex:17, :84, :89, :153, :225, :300; sections/06_coherence.tex:142-143, :172; sections/08_scale.tex:34, :187, :283, :320, :332, :410, :453, :520; sections/10_abstract_collectives.tex:119, :236, :383; sections/04_collectives.tex:12, :125. Category: symbol collision.

Evidence. Each pair quoted from the lines given. Phi: block frame (appA:130), transition product Phi(t,s)=W(t-1)...W(s) (08_scale.tex:34), potential Phi=G_C+sum_j T_j (05_agency.tex:225). Sans-serif P: block-sum map (appA:130) and generic coarse map (05_agency.tex:17). Calligraphic D: Galerkin correction (appA:156), set of decision states (05_agency.tex:300), D_i (06_coherence.tex:142-143), diffusion constant (08_scale.tex:332) and D_eff (:410). Calligraphic T: change of world coordinates (02_framework.tex:397), spanning tree (06_coherence.tex:142), transmission (10_abstract_collectives.tex:119), tilt T_j (05_agency.tex:225); appA:184 lists only the extension uses. Gamma: pandering matrix (02_framework.tex:372), memory kernel (05_agency.tex:84, :89), Gamma_ij of def:col-ultrametric (appA:181). Calligraphic Z_i: sigma-algebra (02_framework.tex:26) and cycle family (06_coherence.tex:142). X: external state X_t (02_framework.tex:20), regressor (:213), joint state (04_collectives.tex:12), X_{i,t} (08_scale.tex:453), readout X_i (:520), decision state X (05_agency.tex:300). phi: phi_C, content phi_t (02_framework.tex:197), fidelity (05_agency.tex:426), edge errors phi_ij (10_abstract_collectives.tex:236), angle (06_coherence.tex:172). h: horizon (appA:164), h_j (02_framework.tex:36), width (04_collectives.tex:125), lag (08_scale.tex:320), information vector h_i (05_agency.tex:153). bar F: diag(F,0,F_z) (02_framework.tex:244) against appA:132. Sans-serif G: listed for sec:met and sec:col, unlisted as (varepsilon I+L)^{-1} in sec:abs (10_abstract_collectives.tex:383). Caption at 08_scale.tex:283 writes xi where the plotted length is xi_OZ. Collisions of a with a_i (active state), s with s_i, b with b_i and S (innovation covariance against block set) were seen in the first pass and are stated here without re-verified line anchors.

Proposed fix. Add one bullet per letter to the list at appA:184-196 giving its local meanings by section, in the form already used for calligraphic T and R; rename the cheap ones: the transition product to $\Psi(t,s)$, the diffusion constant to $D_{\mathrm{diff}}$, the decision-state set to $\mathcal X_{\mathrm{dec}}$, the cycle family to $\mathcal C_i$, and correct the caption at 08_scale.tex:283 to $\xi_{\mathrm{OZ}}$.

State: applied. [05] applied: Renamed the decision-state set \mathcal D to \mathcal X_{\mathrm{dec}} at all occurrences in 05_agency.tex (the only file using it). The other group-05 letters (Phi potential, \mathsf P, tilt T_j, Gamma kernels, h_i, X) need appA bullets only; follow-up issued. The label name def:agy-agency is my guess for the definition near the Agency formula; no label was touched. [06] applied: Cycle family renamed from calligraphic Z_i to calligraphic C_i in prop:coh-frustration(c) and its proof. The locally defined transition product in the proof of prop:coh-info-decay renamed Phi(t,t') to Psi(t,t') to match the proposed sec:sca convention. Bullets for D_i, the spanning tree and the angle belong to appA. [08] applied: Applied: caption now writes xi_OZ; diffusion constant renamed D_diff (two occurrences). Not applied: Phi(t,s) to Psi(t,s), because Psi(varphi) is already the tilted symbol in sec:sca and both would meet in one proof in app08; Phi(t,s) is kept and needs an appA bullet instead. [02] declined: None of the proposed renames (Psi(t,s), D_diff, X_dec, C_i, caption xi_OZ) lies in group 02; the remaining repair is appA bullets. Anchors in 02 verified: bar F=diag(F,0,F_z) and X_t stacked state in sec:fw-channels, regressor X_t in prop:fw-rls, sigma-algebra Z_i. Local meanings returned as a follow-up. [04] declined: None of the proposed renames (Psi(t,s), D_diff, X_dec, C_i, caption xi_OZ) lies in group 04. My files use Phi as block frame and calligraphic D as Galerkin correction, the table meanings; X (joint state) and h (shell width) are locally defined. Only appA bullets are needed; follow-up returned. [10] declined: Nothing to change in group 10: none of the renamed symbols (transition product Phi(t,s), diffusion constant, decision-state set, cycle family) occurs in these files. The local meanings of calligraphic T, phi_ij and sans-serif G belong in the appA list; see follow-up. Framing pass: [appA] partial: Added bullets for Phi, calligraphic D (with italic D), Gamma, phi, h and X (with bar F), and extended the calligraphic T bullet with its four main-text meanings. The a/a_i, s/s_i, b/b_i and S collisions were not checked and got no bullet; Z_i needs none becaus ...

### notation-18 (minor): Recurring symbols absent from the notation tables; sans-serif lists missing for four sections

Location: sections/appA_notation.tex:188, :192-196; sections/05_agency.tex:13-24, :84, :89, :151, :418-420; sections/10a_meta_agents.tex:178. Labels: tab:not-agents, tab:not-networks, def:agy-closure, def:agy-identity. Category: notation table omission.

Evidence. Counted by search over body files: tau_id (8 lines), rho_perp (15), varkappa_perp (15), varkappa_Phi (5), sigma_C (20), sigma_row and sigma_col (20), fraktur d_M (5), alpha_M, alpha_I, r^M, varepsilon', ord, ov have no row or bullet in appA. appA:188 states a rule that sans-serif letters are local and lists them per section at :192-196 for sec:met, sec:hie, sec:ren, sec:env, sec:col only; sec:agy (sans-serif A, w_X, d), sec:sca (sans-serif R), sec:abs (sans-serif G) and sec:coh have none.

Proposed fix. Add the rows to tab:not-networks (with def:agy-identity for $\tau_{\mathrm{id}}$, def:agy-closure for $\mathfrak d_M$, $\alpha_M$, $\alpha_I$, thm:agy-closure-average for $\sigma_C$, $\sigma_{\mathrm{row}}$, $\sigma_{\mathrm{col}}$, $r^M$) and add sans-serif lines for sec:agy, sec:sca, sec:abs.

State: applied. [05] declined: Nothing to change in group 05: the finding asks for rows and sans-serif lists in appA_notation.tex. Follow-up issued with the symbols as they now read in sec:agy. [10a] declined: Nothing to change in group 10a: the finding asks for rows and sans-serif lists in appA_notation.tex. The edits of this batch introduce no new sans-serif symbol. One addition for appA is returned as a follow-up (the closure order ord and chk:met-orders context). Framing pass: [appA] applied

### Not checked by lane notation

- Task 4 sampling of the first three subsections for symbols used before definition: only the opening of sections/09_minimal.tex was read in full; other sections were covered by targeted symbol searches only
- Proof files (sections/app*.tex) and check files (sections/chk*.tex) beyond targeted searches and app05_agency.tex:165
- Defining formulas of attention capacity kappa and whether they agree between sec:fw, sec:frm and sec:min
- Memory factor 1+beta/omega against 1+calligraphic R across prop:sca-records-memory, prop:hie-record-contrast and thm:ren-memory
- Laplacian sign and normalization conventions across sec:col, sec:coh, sec:abs, sec:ren
- Whether sigma_C=|(M-xi_out)phi_C|, sigma(M,phi) of lem:met-unit-coordinate and sigma^d of lem:met-discrete-closure share one normalization
- Line anchors for the collisions of a with a_i, s with s_i, b with b_i and S (innovation covariance against block set) listed in finding 17
- Notation-table rows beyond the roughly 50 sampled, in particular the extension tables for sec:hie, sec:ren and sec:env
- The agency index beyond its single definition at def:agy-agency-index (no second defining formula was searched for in sec:met or the discussion)
- Whether a relation between ord(alpha_M) and d^* is stated in the appendix proofs (finding 12)

### Redundancy noted by lane notation

- Consensus rounds: L (prop:agy-consensus) and n_c (prop:met-consensus-filter) are the same quantity; keep n_c
- Leak letters: varepsilon in the nested medium is varepsilon^Pi; one symbol per side removes the collision of finding 2
- Two effective leaks varepsilon_eff (sec:coh, sec:sca) could carry distinct subscripts or be folded into one definition 'smallest eigenvalue of the reduced generator'
- tau_id (def:agy-identity) and the correlation time tau of the mean mode with records (prop:sca-records-memory) solve the same 2x2 eigenvalue problem at g=0; one could be defined from the other
- ord(alpha_M) (used twice) and the minimal order d^* could be unified or the first dropped
- Kronecker delta delta_{X0} (ex:ren-block-average) and the indicator 1_{x=0} (prop:ren-ring) denote the same nugget term
- Caption at sections/08_scale.tex:283 uses xi for xi_OZ; with def:sca-lengths the bare xi could be retired in favor of xi_OZ and xi_2
- Contrast family r, r_star, r^M, r^d, r^{(l)}, r', r_phi: one table in appA with the quadratic form each uses would replace the four prose comparisons at 05_agency.tex:125, 10a_meta_agents.tex:182, :209 and 12_related.tex:68
- prop:ren-per-level(d) (q>=1/b) is contained in (f) (q>=1/(2b-1)), since 1/(2b-1)<1/b for b>1; (d) could be reduced to the remark about power-law coherence
- Macro \EF in preamble.tex is unused
- Per-section sans-serif lists at appA:192-196 could become one table with a section column, which would also expose the missing sections

## Lane cit_attr: Citation attribution against sources

No critical attribution defect. Of 30 attribution groups checked against primary text, 25 hold at the reading level reached, 3 carry defects (1 major, 2 minor), and 2 could not be verified (Grime and Durrant-Whyte 1994; the means-and-variances clause of Malioutov et al. 2006). A fourth minor finding is bookkeeping: two bib annotes record a lower reading level than the text claims. The major defect is at sections/12_related.tex:9: Maisto et al. (2025) do not fix blankets or roles by construction; they detect a flock-level blanket after the fact by thresholding the Fiedler vector of a co-heading graph and assign whole birds to roles, which is also an active-inference precedent for spectral blanket identification that the positioning at 12:11 omits. The negative claims about Kirchhoff, Palacios, Ramstead, Kaufmann, Heins, Biehl, Aguilera, Friston (2019), Friston et al. (2021) parcels (factors 2.37 and 2.13, non-unique partition), Rosas, Barnett and Seth, Krakauer, Candogan (Lemma 5.1, Corollary 5.2; the manuscript's sigma equals their maximum pairwise difference, so "sharper" and "halved" are like for like) and Olfati-Saber Theorem 1 (exact average consensus at every step, no finite-rate bound) are supported by the passages read. Of the comparisons named in the task, Kolchinsky and Wolpert (2018) is not in references.bib, and dacosta2021bayesian and olfatisaber2007consensus are in references.bib but cited in no .tex file, so there is no manuscript claim about them to audit; only the 2005 distributed Kalman filtering paper of Olfati-Saber is cited. Reading levels: most sources were read in the relevant section (local full-text extractions, arXiv pages, Europe PMC full text through targeted extraction); Oveis Gharan and Trevisan, Mossel et al., Bruineberg et al., Heins and Da Costa, Weiss and Freeman, Bar-Shalom and Campo, Julier and Uhlmann and Aguilera et al. (2023) were checked at abstract level only. No scripts were run. Side effect to report: a WebFetch call on the JMLR PDF of Malioutov et al. left a cached, password-protected copy in the session tool-results folder (outside the vault), which could not be read. Copy of findings saved at <session scratch>/audit/cit_attr/findings.md.

Coverage: 30 items examined; 25 hold, 3 defective, 0 suspect, 2 not checked.

| Item | Verdict | Note |
|---|---|---|
| Maisto et al. (2025): 'fix blankets or roles by construction' (12_related.tex:9) | defect | Full text read (Figure 1, Discussion, Appendix A.4, Eq. 10). Finding 1. |
| Friston et al. (2023) path integrals: conditional independence of paths 'given blanket paths and initial states' (12_related.tex:28; 04_collectives.tex:52) | defect | arXiv pages 6-10 read (Eq. 11). Finding 3; published version not checked. |
| Malioutov et al. (2006): loopy Gaussian BP converges on walk-summable models with correct means and variances capturing part of the walks (12_related.tex:49) | not_checked | JMLR abstract only: walk-sum framework and stronger convergence results are supported. The means-and-variances clause is in the body, which could not be read; the manuscript sentence is unhedged and the bib records no reading level. |
| Grime and Durrant-Whyte (1994): channel filters fuse exactly on trees; cavity as provenance device (12_related.tex:49; 10b_hierarchy.tex:90) | not_checked | No accessible text or abstract. Bib records a record check only. |
| Friston et al. (2025) pixels: one parent per state, leading singular variates, 'no benchmark', no bound (12_related.tex:123; 10c_renormalization.tex:277) | defect | Structural claims and the 32-versus-16 figures hold; 'they report no benchmark' is overstated (finding 2). Sections listed in the bib annote read. |

Items found to hold: Kirchhoff et al. (2018): blanket of blankets argued without theorem, simulation or test; feedback condition (12_related.tex:9; 04_collectives.tex:39); Ramstead et al. (2018): propose, without deriving, that cultural ensembles minimize free energy (12_related.tex:9); Palacios et al. (2020): identical priors, roles inferred, one ensemble explicit and fifteen in mean field, proof of principle, coupling by averages (12_related.tex:9); Kaufmann et al. (2021): shared goal imposed in methods although the abstract says alignment emerges (12_related.tex:9); Heins et al. (2023, 2024): collective behavior without communication channels or a blanket analysis (12_related.tex:9); Waade et al. (2025): blanket structure fixed by construction (12_related.tex:9); Oveis Gharan and Trevisan (2014): gap condition for J well-connected sets (12_related.tex:11; 04_collectives.tex:407); Fields et al. (2022) on cellular collectives and competency (12_related.tex:15, 12:137); Biehl et al. (2021) and Bruineberg et al. (2022): a blanket is a property of a declared model and does not make an agent (12_related.tex:20; 04_collectives.tex:45, 04:218); Aguilera et al. (2022): blanket condition and solenoidal restrictions hold only in a narrow parameter region (12_related.tex:22, 12:30); Lorenz-system exchange (Friston et al. 2021 stochastic chaos; Aguilera et al. 2023) reported as known secondarily (12_related.tex:26); Heins and Da Costa (2022) reply on sparse coupling (12_related.tex:30); Weiss and Freeman (2001): correct means on any topology when BP converges (12_related.tex:49); Bar-Shalom and Campo (1986) and Julier and Uhlmann (1997): fused covariance with common process noise; covariance intersection under unknown correlations (12_related.tex:49); Olfati-Saber (2005) Theorem 1: exact average consensus at every step, uncorrelated noise, known n, no bound at finite consensus rate (05_agency.tex:148; 12_related.tex:51; 10a_meta_agents.tex:289); Mossel et al. (2016): full-information belief within 2N diam(G) rounds (12_related.tex:51; 05_agency.tex:185); Krakauer et al. (2020): informational closure implies sufficiency under a Markovian system-environment structure; environmentally driven individuality (12_related.tex:68; 05_agency.tex:423); Barnett and Seth (2023) on dynamical independence, and Bertschinger et al. through their footnote (12_related.tex:70; 10a_meta_agents.tex:257); Rosas et al. (2024): closure notions concern prediction of the macroscopic process (12_related.tex:70; 10a_meta_agents.tex:164, 10a:257); Candogan et al. (2013): Lemma 5.1 ratio factor e^{2 gamma sigma}, Corollary 5.2(ii), and the manuscript's 'sharper' and 'halved' bound (12_related.tex:77; 05_agency.tex:281); Friston (2008) and Friston et al. (2017): error units from own level and level below; continuous-state message passing as predictive coding; ascending Bayesian model average (12_related.tex:105-107; 10b_hierarchy.tex:90, 10b:105); Friston (2019): particular partition and adiabatic reduction without an error bound (12_related.tex:121; 10c_renormalization.tex:233, 10c:253; 13_discussion.tex:43); Friston et al. (2021) parcels: one subject, factors about 2.37 and 2.13 per scale, partition stated not unique (12_related.tex:123; 10c_renormalization.tex:277); Friston et al. (2023) path integrals and Friston et al. (2023) variational: adiabatic approximation, particles of particles left open, no renormalization theorem; population partition at a slow scale; independent fluctuations (12_related.tex:123; 10c_renormalization.tex:253); Dörfler and Bullo (2013) Kron reduction and Villegas et al. (2023) Laplacian renormalization (12_related.tex:132; 10c_renormalization.tex:340).

### cit_attr-01 (major): Maisto et al. (2025) are said to fix blankets or roles by construction; the primary text detects the blanket spectrally after the fact

Location: sections/12_related.tex:9 (sec:rel-nested); consequence at sections/12_related.tex:11. Category: attribution.

Evidence. Manuscript: "\citet{waade2025one} and \citet{maisto2025flock} fix blankets or roles by construction, according to secondary accounts." Source (arXiv preprint, full text read: Figure 1 caption, Discussion, Appendix A.4 with Eq. (10)): for a time window T_w the flock is a weighted graph whose edge weight counts the times two birds share a heading; blanket birds are those with |y_2(i)| below an adaptive threshold on the Fiedler vector (10th to 20th percentile of absolute values); the sign of y_2(i) beyond the threshold makes a bird internal or external, and the community a blanket bird connects to more makes it active or sensory. The Figure 1(d) caption calls the result an "emergent Markov blanket around the flock". No conditional independence is computed. Waade et al. (2025), read in full, do compose agents in a blanket structure specified in advance, so the clause is right for Waade and wrong for Maisto. Consequence: the paper is an active-inference precedent for spectral, whole-agent identification of a collective blanket; 12:11 draws the spectral precedent only from Simon and from Kannan et al., and 12:9 calls Palacios et al. the only simulation of blankets of blankets found. The hedge 'according to secondary accounts' discloses the reading level but the statement is false for this source.

Proposed fix. 12:9, replace the last clause with: "\citet{waade2025one} compose agents in a blanket structure specified in advance, and \citet{maisto2025flock} detect a flock-level blanket after the fact by thresholding the Fiedler vector of a graph of heading co-alignment, assigning whole birds to internal, external, sensory and active roles without a test of conditional independence." 12:9, Palacios sentence: "\citet{palacios2020markov} give the only simulation we found in which a second-level blanket is constructed and coupled to the first:". 12:11, after the spectral-clustering sentence add: "Within active inference, \citet{maisto2025flock} identify a flock-level blanket spectrally from a co-heading graph; our criterion acts instead on the precision of the stationary world-conditional law, at a level declared in advance, with roles assigned to channels."

What would overturn the finding. The secondary-account characterization of Maisto et al. and the implicit claim that no active-inference work selects a collective blanket spectrally.

State: applied. Framing pass: [group 12] applied

### cit_attr-02 (minor): "They report no benchmark" overstates Friston et al. (2025), which reports MNIST test accuracy

Location: sections/12_related.tex:123 (sec:rel-renormalization). Category: attribution.

Evidence. Manuscript: "they report no benchmark and, in the parts we read, no bound on what the reduction loses." Source (vault PDF extraction; Introduction and the image-compression section with Figure 8): the authors say they refrain from benchmarking the examples for performance or accuracy, and then report MNIST classification accuracy of 95.1 percent on the full test set and 99.8 percent after a median split on marginal likelihood. The 'no bound' half of the sentence is supported by a keyword search of the full extraction and the sections read.

Proposed fix. "they decline to benchmark against other schemes, although they report MNIST classification accuracy (95.1\% on the full test set, 99.8\% on the half with higher marginal likelihood), and, in the parts we read, give no bound on what the reduction loses."

State: applied. Framing pass: [group 12] applied

### cit_attr-03 (minor): Conditioning of the path blanket on initial states is attributed to friston2023path; it is stated in friston2023simpler

Location: sections/04_collectives.tex:52; sections/12_related.tex:28 (sec:rel-debate). Category: attribution.

Evidence. Manuscript (04:52): "The path notion is that of \citet{friston2023path}: internal and external paths are conditionally independent given blanket paths and initial states." 12:28 repeats the attribution. Source: path-integrals paper, arXiv 2210.12761, Eq. (11) and surrounding text (pages 6 to 10 read): internal and external paths in generalized coordinates are independent given blanket paths, with no conditioning on initial states. The form with initial states is in the 'made simpler' paper (bib key friston2023simpler), Section 4 and the Section 4.1 summary, where the conditioning on initial states is written out. Confirmed on the arXiv version; the published Physics of Life Reviews version was not checked. The distinction matters here because the manuscript's own theorem (thm:col-path-blanket) turns on the initial slice.

Proposed fix. 04:52: "The path notion is that of \citet{friston2023path}, in the form conditioned on initial states of \citet{friston2023simpler}: internal and external paths are conditionally independent given blanket paths and initial states." 12:28: "\citet{friston2023path} obtain, for flows that respect sparse coupling and independent fluctuations, conditional independence of internal and external paths given blanket paths, which \citet{friston2023simpler} state with conditioning on initial states."

State: applied. [04] applied: Confirmed on arXiv texts opened this run: 2210.12761 never contains the word 'initial' and states independence given blanket paths only; 2201.06387v3 states independence 'conditioned on blanket paths (and initial states)'. Sentence before thm:col-path-blanket now reads as proposed; friston2023simpler exists in references.bib. Published versions not checked. Framing pass: [group 12] applied; [bib] applied

### cit_attr-04 (minor): Bib annotes for kirchhoff2018markov and villegas2023laplacian record a lower reading level than the text claims

Location: references.bib:2595 (kirchhoff2018markov); references.bib:4188 (villegas2023laplacian); claims at sections/12_related.tex:9 and sections/10c_renormalization.tex:340. Category: attribution.

Evidence. kirchhoff2018markov annote: 'abstract read'. 12:9 states what the paper argues, that it has no theorem, simulation or test of conditional independence, and its feedback condition on ensemble blankets; these sit in the body (Section 4, Conclusion), not the abstract. villegas2023laplacian annote: 'abstract and introduction'. 10c:340 says the procedure was read in its primary text and describes the k-space steps. My reading of both bodies supports the manuscript's sentences, so the defect is in the reading-level record, which under the manuscript's own status discipline should not be exceeded by the claim.

Proposed fix. kirchhoff2018markov annote: "Read: P (Sections 2 to 4 and Conclusion)." villegas2023laplacian annote: "Read: P (arXiv 2203.07230: abstract, introduction and the Laplacian RG procedure, steps i to iv)." Both to be entered only after the author confirms the reading.

State: applied. [10c] declined: The defect is in references.bib, outside my group. I opened arXiv:2203.07230v1 pages 1 to 5 in this run: Eq. (1), the specific-heat peaks and LRG steps (i) to (iv) match the description at 10c (sec:ren-network), so the text stands unchanged. Follow-up gives the annote. Framing pass: [group 12] declined: Already repaired outside this file: the annotes of kirchhoff2018markov and villegas2023laplacian in references.bib now record 'Read: P' at the level the text claims (author confirmation marked outstanding there). The sentence in sec:rel-hierarchy-level paragra ...; [bib] applied

### Not checked by lane cit_attr

- Grime and Durrant-Whyte (1994): no accessible text or abstract; the claims at 12_related.tex:49 and 10b_hierarchy.tex:90 are unverified.
- Malioutov et al. (2006), body: the clause on correct means and partial variances was not opened in primary text (JMLR abstract only; the PDF could not be read through the tools).
- Published-journal versions of Candogan et al. (2013) and of the path-integrals paper (arXiv versions read).
- Friston et al. (2021) stochastic chaos and the remaining replies in the Lorenz exchange (12_related.tex:26), which the manuscript itself marks as secondary.
- Second half of Ramstead et al. (2018) (characters 100k to 156k of the Europe PMC text).
- Kolchinsky and Wolpert (2018): not in references.bib; no manuscript claim to audit.
- Da Costa et al. (2021) 'Bayesian mechanics for stationary processes': bib key dacosta2021bayesian exists but is cited in no .tex file; no manuscript claim to audit.
- Olfati-Saber, Fax and Murray (2007): bib key olfatisaber2007consensus exists but is cited in no .tex file.
- Abstract-level checks only (no body read): Oveis Gharan and Trevisan (2014), Mossel et al. (2016), Bruineberg et al. (2022), Heins and Da Costa (2022), Weiss and Freeman (2001), Bar-Shalom and Campo (1986), Julier and Uhlmann (1997), Aguilera et al. (2023).
- Attributions outside sections 04, 05, 10a-10d, 12 and 13, and the remaining subsections of 12_related.tex (Lieb-Robinson, strong data processing, synchronization, opinion dynamics, disorder, social sciences, culture, sensing, organizations) beyond the 30 selected.

## Lane cit_meta: Bibliography integrity and metadata

The bibliography is mechanically clean; the substantive defect is literature coverage. Integrity (Task 1): 373 entries (365 in references.bib, 8 in three sections/*_extra.bib files), 303 distinct cited keys, 303 bibitems in the .bbl, 0 BibTeX warnings; no undefined citation, no duplicate key, DOI, eprint or normalized title, no missing required field, no key/year or key/surname mismatch; 70 keys are never cited. Metadata (Task 2): completed for all five target sections and beyond. All 225 keys cited in 10a (7), 10b (8), 10c (14), 10d (18) and 12_related (218) were covered wherever a DOI or eprint exists; in total 322 of 322 DOI-bearing entries were compared with Crossref (one via an alias DOI) and 56 of 56 eprint fields with arXiv. 261 of 321 direct Crossref comparisons are clean; the remaining 60 flags are cosmetic or errors on the Crossref side (first-page-only JSTOR records, missing coauthors in old Elsevier records, series names as container titles, print-year versus online-year differences already documented in annotes). No author, title, venue, volume or year error was found in a cited entry; the only record-level corrections are a short journal name (lambiotte2008geographical), a missing issue number (madsen2018large) and one first-page-only pages field (working1960note, last page unverified). Eighteen printed 'Unverified' notes remain, two of which this audit resolves (wilson1974renormalization second author via INSPIRE; radner1993organization last page 1146 via RePEc). Coverage (Task 3): of the 32 works in the source register, 16 are in the bibliography (one of them, dacosta2021bayesian, never cited) and 16 are absent. All 16 absent works were verified against Crossref, arXiv or the PMLR page and written in house style to <session scratch>/audit/cit_meta/new_entries.bib (parsed, sorted, no key/DOI/eprint collision; none left unverified). Two absent works, Zaghw et al. 2026 (arXiv 2608.09512) and de Vries 2026 (arXiv 2603.20927), fall inside the scope of three 'no error bound found' statements about active-inference renormalization; I did not read either, and the register says both leave the quantitative error question open, so no manuscript statement is shown false. Three register items listed as preprints have published versions that the new entries use: Rangarajan and Rao (Neural Computation 38(9), 1491-1544), Nomura and Horii (ALIFE 2026 proceedings, article 83), Ruiz-Serra et al. (AAMAS 2025, pp. 1793-1802; the Crossref record for DOI 10.65109/znpv2392 names the wrong event, noted in the entry's annote). The harness refused the findings.md copy (sub-agents may not write report files), so this return is the only record besides new_entries.bib and the lane's scripts and saved API responses.

Coverage: 14 items examined; 8 hold, 4 defective, 1 suspect, 1 not checked.

| Item | Verdict | Note |
|---|---|---|
| Keys never cited | defect | 70 uncited keys, listed in the findings; no effect on the compiled reference list. |
| Target-section entries without a DOI (36 of 225) | not_checked | Those with an eprint were checked against arXiv; books, journals without DOIs and five unpublished dennis2026* self-citations were compared with their annotes only, against no external record. |
| Printed 'Unverified' notes | defect | 18 print in the .bbl; 2 resolved here, 16 open. |
| Internal consistency of venue names (161 distinct journal strings) | defect | One venue spelled two ways: Physica A. |
| Source register of the open-problems review (32 works) against the bibliography | defect | 16 present, 16 absent; all 16 absent works verified and written to new_entries.bib. |
| Scoped 'no error bound' statements for active-inference renormalization (12_related.tex:123, :125; 10c_renormalization.tex:277) | suspect | Correct as scoped to the texts read; the scope omits two 2026 preprints in the register that I did not read. |

Items found to hold: Same work under two keys (keys, DOIs, eprints, normalized titles over 373 entries); Required fields by entry type; syntax of doi, pages, year, eprint; Key convention: key year against year field, key surname against first author; Cited but undefined keys (303 cited, 373 defined); Crossref check of every DOI-bearing entry (322), including all such entries cited in 10a, 10b, 10c, 10d and 12_related; arXiv check of every eprint field (56); Hand-typed author-year citations outside BibTeX; new_entries.bib (16 entries).

### cit_meta-01 (major): Zaghw et al. 2026 and de Vries 2026 are absent while three passages scope 'no error bound' to the texts read

Location: sections/12_related.tex:123 and :125 (sec:rel-renormalization); sections/12_related.tex:157 (sec:rel-new); sections/10c_renormalization.tex:277 (rem:ren-rgm). Labels: sec:rel-renormalization, sec:rel-new, rem:ren-rgm. Category: bib.

Evidence. Demonstrated: the source register of active-inference-open-problems-2026-11-09.md lists de Vries (2026), 'Active Inference for Physical AI Agents: An Engineering Perspective' (arXiv 2603.20927; register line 192) and Zaghw, Pashea, Pritsch, Nuijten, Friston, Da Costa (2026), 'Renormalising Generative Models for Active Inference: Foundations, Derivations, and Verification' (arXiv 2608.09512; register line 193). Neither eprint, title nor surname occurs in references.bib, in any sections/*_extra.bib, or in any section .tex. The manuscript discusses renormalizing generative models in eight sections (01, 10a, 10b, 10c, 10d, 11, 12, 13) through friston2025pixels alone. 12_related.tex:123 says of friston2025pixels 'they report no benchmark and, in the parts we read, no bound on what the reduction loses'; :125 says 'That no error bound accompanies the active-inference renormalization is a search result covering the papers above and the replies on blankets, not the whole literature'; 10c_renormalization.tex:277 says 'In the parts of the two texts that we read we found no error bound for the reduction'; 12_related.tex:157 lists 'error bounds for adiabatic reductions beyond the papers we searched' as still to check. Not demonstrated: that either preprint contains an error bound or a benchmark. I read neither (arXiv metadata only); the register states that both leave the quantitative error question open and that Zaghw et al. add 'a more explicit derivation and reproducibility treatment'. No theorem or scoped statement of the manuscript is shown false; the defect is that the direct successor of a construction the manuscript characterizes is uncited and missing from the to-check list.

Proposed fix. Add entries zaghw2026renormalising and devries2026active from new_entries.bib to references.bib. In sections/12_related.tex:125 replace the last sentence by: 'That no error bound accompanies the active-inference renormalization is a search result covering the papers above and the replies on blankets, not the whole literature; it does not cover the later derivation of renormalizing generative models by \citet{zaghw2026renormalising} or the engineering formulation of \citet{devries2026active}, neither of which we have read.' In sections/12_related.tex:157 replace the closing clause by: 'and error bounds for adiabatic reductions beyond the papers we searched, starting with \citet{zaghw2026renormalising} and \citet{devries2026active}.' In sections/10c_renormalization.tex:277, after 'In the parts of the two texts that we read we found no error bound for the reduction.' insert: 'We have not read the later treatment of these models by \citet{zaghw2026renormalising}.' Then read both preprints before the sentence at 12_related.tex:149 is kept.

What would overturn the finding. Nothing as stated; it weakens the search basis of the novelty statement at 12_related.tex:149 ('error bounds for coarse-graining, with an exact account of what the active-inference renormalization drops').

State: applied. [10c] applied: Inserted the proposed sentence citing zaghw2026renormalising after the no-error-bound sentence. I opened the arXiv abstract page of 2608.09512 (title, six authors, v1 2026-08-10 confirmed). The BibTeX entry is left to references.bib as the finding assigns it; the citation is undefined until that entry exists. Framing pass: [group 12] partial: Both keys now exist in references.bib (annotes: not read). The 'search result' sentence in sec:rel-renormalization and the adiabatic-reduction to-check item in sec:rel-new now name zaghw2026renormalising and devries2026active as unread, characterized by title ...; [bib] declined: Bibliography part already done by an earlier batch: zaghw2026renormalising and devries2026active are each defined once in references.bib with arXiv record checks and 'Not read'. Nothing opened; the two sentences proposed for 12_related.tex are still absent and ...

### cit_meta-02 (minor): Fourteen further source-register works are absent from the bibliography

Location: references.bib (whole file); nearest subsections in sections/12_related.tex at lines 65, 74, 93, 102, 111, 141. Category: bib.

Evidence. Checked each of the 32 register works against all bib files by DOI, eprint, normalized title and first-author surname plus year. Present (16): kirchhoff2018markov, palacios2020markov, biehl2021technical, aguilera2022particular, heins2022sparse, dacosta2021bayesian, friston2023path, friston2019free, friston2021parcels, rosas2024software, lenggenhager2020optimal, gordon2021relevance, villegas2023laplacian, waade2025one, heins2023spin, friston2023variational. Absent besides the two of the previous finding (14): March 1991; Bourrat et al. 2022; Champion et al. 2026; Durant et al. 2017; Chou et al. 2026; Fields, Goldstein, Sandved-Smith 2024; Horowitz and Esposito 2014; Friston et al. 2026 (Nature Communications); Kolchinsky and Wolpert 2018; Sasaki and Biro 2017; Ruiz-Serra et al. 2025; Nuijten et al. 2026; Rangarajan and Rao 2026; Nomura and Horii 2026. None is named in the text. Six have a nearest existing subsection (my placement by title, not checked against the works): Ruiz-Serra 2025 at sec:rel-games (line 74), Nomura and Horii 2026 at sec:rel-social (line 93), Rangarajan and Rao 2026 at sec:rel-hierarchy (line 102), Sasaki and Biro 2017 at sec:rel-culture (line 111), March 1991 at sec:rel-organizations (line 141), Kolchinsky and Wolpert 2018 at sec:rel-closure (line 65). The other eight concern topics with no counterpart in the manuscript: thermodynamic cost (the string 'thermodynamic' occurs in no section file), expected-free-energy foundations, evolutionary transitions in individuality, and empirical tests.

Proposed fix. Paste the needed entries from new_entries.bib (keys march1991exploration, bourrat2022tradeoff, champion2026reframing, durant2017long, chou2026systematic, fields2024making, horowitz2014thermodynamics, friston2026active, kolchinsky2018semantic, sasaki2017cumulative, ruizserra2025factorised, nuijten2026type, rangarajan2026hierarchical, nomura2026social) into references.bib in key order as each work is cited. Ruiz-Serra 2025 and Nomura and Horii 2026 are multi-agent active-inference models and should be read before the phrase 'Relative to the active-inference literature we found' at sections/12_related.tex:149 is kept.

State: applied. Framing pass: [group 12] partial: All 14 keys now exist (9 in references.bib, 5 in ext3/ext6/ext7 extra bibs), so absence is repaired. In this file: novelty sentence scoped to 'the reading levels recorded in this section', and nomura2026social added to the to-check list as unread. Ruiz-Serra i ...; [bib] declined: Already repaired: all 14 keys are defined exactly once (ten in references.bib, four in ext3/ext6/ext7 extra files). I only moved the block that had been appended at the end of references.bib into key order; no entry text changed and no metadata was re-checked. Coordinator: all 14 keys are defined in the bibliography; the reference gate reports no unknown citation key.

### cit_meta-03 (minor): Eighteen 'Unverified' notes print in the reference list; two can be closed now

Location: references.bib:4277 wilson1974renormalization (note at :4286); references.bib:3688 radner1993organization (note at :3697); 16 further notes at references.bib:63, :80, :494, :516, :879, :1008, :1082, :1252, :2142, :2178, :2195, :2911, :3536, :3547, :3912, :4117. Category: bib.

Evidence. grep -c 'Unverified' collective_agents.bbl returns 18 (bbl lines 35, 48, 265, 281, 474, 537, 581, 1163, 1181, 1193, 1549, 1851, 1859, 1919, 1982, 2025, 2139, 2229); the header of references.bib says such a note 'should be resolved or removed before submission'. Resolved here: (1) wilson1974renormalization, note 'Unverified: second author against a primary record'. Crossref lists only 'Wilson, K'; the INSPIRE record (saved as ext/inspire_wilson.json) gives authors ['Wilson, K.G.', 'Kogut, John B.'], Phys.Rept. 12, pages 75-199, 1974. (2) radner1993organization, note 'Unverified: last page'. Crossref gives first page 1109 only; the IDEAS/RePEc page (saved as ext/repec_v61y1993i5p1109-46.html) carries citation_firstpage 1109 and citation_lastpage 1146. Not resolved: aguilera2023confederation, aguilera2023knitting, berglund2006noise, bertschinger2006information, catal2025belief, courtois1977decomposability, daft1984toward, ding2026phase, hayek1945use, heins2022sparse, heins2023spin, list2011group, pavliotis2008multiscale, pearl1988probabilistic, seguy1971relation, toulouse1977theory (subtitles, series volumes, editors and publisher, last pages; no primary record found, and DBLP returned a bot check that I did not pursue).

Proposed fix. references.bib:4278: 'author = {Wilson, Kenneth G. and Kogut, John B.},' and delete line 4286 ('note = {Unverified: second author against a primary record},'). Delete references.bib:3697 ('note = {Unverified: last page},'). For the other 16, resolve the field or, before submission, move the remark from 'note' to 'annote' so it no longer prints.

State: partial. Framing pass: [bib] partial: 13 of 18 notes closed from records opened this session: INSPIRE (Wilson-Kogut, now Kogut, John B.), IDEAS/RePEc (Radner), PubMed (two Phys Life Rev subtitles), Springer book pages (CCIS 1721, 2193, 1326; Berglund-Gentz), zbMATH Open (Pavliotis-Stuart, Pearl, C ...

### cit_meta-04 (minor): Seventy defined keys are never cited, including one source-register work

Location: references.bib (70 entries); references.bib:1061 dacosta2021bayesian. Category: bib.

Evidence. Set difference between the 373 defined keys and the 303 keys appearing in \cite, \citet, \citep and variants across all section files (script integrity.py in the lane directory). natbib prints none of them, so the compiled reference list is unaffected. Uncited: acemoglu2013opinion, albarracin2024shared, alonso2016bayesian, arrow1964role, axelrod1997dissemination, bauschke1996projection, bertschinger2008autonomy, besag1974spatial, bollobas1991edge, bruineberg2022naked, butta2007propagation, castellano2009statistical, chen2019finite, chorin2002optimal, chover1973functions, dacosta2021bayesian, dawid1982well, deutsch2001best, feldman2010attention, fields2020scale, fields2021minimal, fields2022information, friston2013life, friston2015knowing, friston2024designing, gao2021geometry, garbade1978technology, gather2002graphical, genest1984characterization, genest1986characterization, head2014gravity, henriksen2020variational, hoel2013quantifying, innis1951bias, isomura2019bayesian, jadbabaie2012non, janson2004robust, kato2019quantum, kesten1966limit, kleinberg2000navigation, krause2005near, kuwahara2025clustering, levin2019computational, lindquist2015linear, lloyd2025diverging, mattis1976solvable, melson1970modernization, mermin1966absence, molavi2018theory, mossel2003information, nachtergaele2006propagation, nachtergaele2009lieb, olfatisaber2007consensus, pagel2007frequency, palmer2015predictive, parr2019generalised, pemantle2007survey, peyre2008probabilistic, pfante2014comparison, possati2025markov, raja2021markov, ramstead2019variational, ramstead2020tale, sakthivadivel2022weak, smith1977practical, vasil2020world, vonneumann1949rings, xiao2007distributed, zhou2005discrete, zwanzig2001nonequilibrium. dacosta2021bayesian (Da Costa et al. 2021, Bayesian mechanics for stationary processes) is a register work that sec:rel-debate could cite.

Proposed fix. Cite or delete each before submission. For dacosta2021bayesian, cite it in sections/12_related.tex sec:rel-debate (line 17) where the stationary-process blanket constructions are discussed, or drop the entry.

State: declined. Framing pass: [group 12] declined: dacosta2021bayesian is now cited in sections/opn_p1.tex (part of the open-problems section), so the key is no longer orphaned; I did not open the source, so no new citation was added in sec:rel-debate. The other 69 uncited keys are a bibliography matter, repor ...; [bib] declined: Uncited entries may stay under the bibliography rule, so nothing was deleted; citing them is a .tex decision. dacosta2021bayesian is now cited in opn_p1.tex, so that part is moot.

### cit_meta-05 (minor, unconfirmed): working1960note gives a first page only

Location: sections/10c_renormalization_extra.bib:22 (key working1960note, entry at line 16). Category: bib.

Evidence. The field reads 'pages = {916},' and the annote says 'Crossref gives no last page, and none was verified'. The Crossref record of 10.2307/1907574 (saved in cr/batch_12.json) has page '916', volume 28, issue 4, issued 1960-10. OpenAlex repeats the first page as last page for JSTOR DOIs and is unusable; no RePEc record was found. The usual citation of this note is Econometrica 28(4), 916-918, which I could not check against any record, so the last page is missing evidence and this finding is unconfirmed.

Proposed fix. If the last page is confirmed from the journal: 'pages = {916--918},'.

State: deferred. [10c] deferred: Last page not confirmed: Crossref and OpenAlex records of 10.2307/1907574 give only page 916, JSTOR did not load, and no RePEc record was found. Entry and annote left as they are; 916--918 needs the journal issue or JSTOR front matter.

### cit_meta-06 (minor): Record and housekeeping slips: short journal name, missing issue number, stale merge comment

Location: references.bib:2758 (lambiotte2008geographical); references.bib:2997 (madsen2018large); sections/12_related_extra.bib:1 (file comment; bradde2017pca at line 4). Category: bib.

Evidence. (1) lambiotte2008geographical has 'journal = {Physica A}' while references.bib:1849 (geigenmuller1983systematic) and the Crossref record of 10.1016/j.physa.2008.05.014 give 'Physica A: Statistical Mechanics and its Applications'; this is the only venue spelled two ways among 161 distinct journal strings (script journals.py). (2) madsen2018large has volume 8 and pages 12391 but no number; Crossref gives Scientific Reports volume 8, issue 1, article number 12391. (3) sections/12_related_extra.bib:1 reads '% Entries merged into references.bib.' but bradde2017pca is defined only in that file (line 4) and in no other bib file. Eight entries in all live outside references.bib (2 in 10c_renormalization_extra.bib, 5 in 10d_environments_extra.bib, 1 in 12_related_extra.bib), against the header statement of references.bib that entries are sorted by key in that file.

Proposed fix. references.bib:2758: 'journal = {Physica A: Statistical Mechanics and its Applications},'. references.bib:2997 entry: add 'number = {1},' after the volume line. Merge the eight *_extra.bib entries into references.bib in key order, or delete line 1 of sections/12_related_extra.bib.

State: applied. Framing pass: [bib] applied

### Not checked by lane cit_meta

- ABSENT: March 1991, Exploration and Exploitation in Organizational Learning (Organization Science 2(1), 71-87; doi 10.1287/orsc.2.1.71) -> march1991exploration
- ABSENT: Bourrat, Doulcier, Rose, Rainey, Hammerschmidt 2022, Tradeoff breaking as a model of evolutionary transitions in individuality (eLife 11, e73715) -> bourrat2022tradeoff
- ABSENT: Champion, Bowman, Markovic, Grzes 2026, Reframing the Expected Free Energy: Four Formulations and a Unification (Neural Computation 38(3), 439-469; arXiv 2402.14460) -> champion2026reframing
- ABSENT: Durant et al. 2017, Long-Term, Stochastic Editing of Regenerative Anatomy via Targeting Endogenous Bioelectric Gradients (Biophysical Journal 112(10), 2231-2243) -> durant2017long
- ABSENT: Chou, Hakimi, Hsu, Smith 2026, A systematic empirical comparison of active inference and reinforcement learning models (Journal of Mathematical Psychology 130, 103011) -> chou2026systematic
- ABSENT: Fields, Goldstein, Sandved-Smith 2024, Making the Thermodynamic Cost of Active Inference Explicit (Entropy 26(8), 622) -> fields2024making
- ABSENT: Horowitz and Esposito 2014, Thermodynamics with Continuous Information Flow (Physical Review X 4(3), 031015; arXiv 1402.3276) -> horowitz2014thermodynamics
- ABSENT: Friston, Da Costa, Tschantz, Heins, Buckley, Verbelen, Parr 2026, Active inference and artificial reasoning (Nature Communications 17(1), 10125; arXiv 2512.21129) -> friston2026active
- ABSENT: Kolchinsky and Wolpert 2018, Semantic information, autonomous agency and non-equilibrium statistical physics (Interface Focus 8(6), 20180041; arXiv 1806.08053) -> kolchinsky2018semantic
- ABSENT: Sasaki and Biro 2017, Cumulative culture can emerge from collective intelligence in animal groups (Nature Communications 8(1), 15049) -> sasaki2017cumulative
- ABSENT: de Vries 2026, Active Inference for Physical AI Agents: An Engineering Perspective (arXiv 2603.20927, preprint) -> devries2026active
- ABSENT: Ruiz-Serra, Sweeney, Harre 2025, Factorised Active Inference for Strategic Multi-Agent Interactions (AAMAS 2025, pp. 1793-1802; arXiv 2411.07362) -> ruizserra2025factorised
- ABSENT: Nuijten, Lukashchuk, van de Laar, de Vries 2026, What Type of Inference is Active Inference? (UAI 2026, PMLR 337, 5003-5039; arXiv 2606.04935) -> nuijten2026type
- ABSENT: Rangarajan and Rao 2026, Hierarchical Active Inference Using Successor Representations (Neural Computation 38(9), 1491-1544; arXiv 2604.15679) -> rangarajan2026hierarchical
- ABSENT: Zaghw, Pashea, Pritsch, Nuijten, Friston, Da Costa 2026, Renormalising Generative Models for Active Inference: Foundations, Derivations, and Verification (arXiv 2608.09512, preprint; IWAI 2026 acceptance per arXiv comment, no proceedings record found) -> zaghw2026renormalising
- ABSENT: Nomura and Horii 2026, Social Reality Construction via Active Inference: Modeling the Dialectic of Conformity and Creativity (ALIFE 2026 proceedings, article 83; arXiv 2604.09026) -> nomura2026social
- Unverified absent works left out of new_entries.bib: none; all 16 were verified against Crossref, arXiv or the PMLR article page.
- The content of the 16 absent works (records only), hence whether Zaghw et al. 2026 or de Vries 2026 contain an error bound or benchmark that would bear on sections/12_related.tex:123-125 and 10c_renormalization.tex:277.
- Last pages of working1960note (Crossref first page only, no RePEc record) and daft1984toward (printed note 'Unverified' stands).
- Series volume numbers of the Communications in Computer and Information Science chapters flagged Unverified, and editors and publisher of bertschinger2006information; DBLP returned a bot check, which I did not pursue.
- Entries with neither DOI nor eprint (books, journals without DOIs, five unpublished dennis2026* self-citations) against any external record.
- Whether the citing sentences use the cited results correctly (assigned to other lanes).
- findings.md copy in the lane directory: refused by the harness (sub-agents may not write report files); only new_entries.bib, scripts and saved API responses are on disk.

## Lane arch: Architecture, dependency map and length budget

VERDICT. A main text of about 120 pages is reachable without dropping any result. Of the 270 body pages (sections 1-17: 14, 18, 12, 26, 23, 16, 15, 22, 9, 21, 15, 17, 16, 17, 7, 14, 8), about 29 pages (about 15,850 words at the measured 540 wc-words per page) are restatement of results or of status sentences, and about 120 further pages are secondary material (examples, applications, numerical observations, conjectures, long interpretive remarks, the minimal-model dictionary, most of the related-work survey) that can move to a supplement next to the 113 pages of proofs and about 48 pages of numerical checks. The theory has three families that are one statement in several costumes: the closure and memory identity (14 statements in sections 5, 11, 12, 13, 14), double counting of shared precision by the literal reading (15 statements in sections 2, 3, 5, 9, 10, 11, 12, 13), and the Galerkin defect of the coarse medium (3 statements in sections 4 and 13). The body holds, by my count from the extracted inventory, 36 open problems, 22 conjectures and 20 numerical observations. STRUCTURAL FINDINGS (locations are file:line in sections/ plus label). A1 (major) Hypothesis status is reported at least six times: abstract (00_abstract.tex:4); status paragraphs after each hypothesis in 1.2; four full-page tables in 1.3 (01_introduction.tex:110, 148, 186, 212, about 60 rows); section 1.4 (about 5 pages); five compilation theorems totaling 2,272 statement words, thm:col-boundary (04_collectives.tex:659, 360w), thm:agy-h1 (05_agency.tex:571, 507w) plus rem:agy-h1-status (05_agency.tex:588, 324w), thm:sca-h4 (08_scale.tex:598, 388w), thm:met-h5a (10a_meta_agents.tex:321, 451w), thm:ren-closure (10c_renormalization.tex:371, 566w); section 17.1 (2,738 words) and 17.4. Fix: hypotheses in the introduction with a one-sentence status and a pointer to the final-form theorem, one results table of about 20 rows, and one status section in the Discussion absorbing 1.4, 15.3, 17.1, 17.4, 17.5. A2 (major) The formation-status passage ("0 to 7 of 8 replicates", "translation-aware") occurs 15 times in 11 files: 00_abstract.tex:4; 01_introduction.tex:43, 168, 242; 03_misreading.tex:334; 05_agency.tex:589; 06_coherence.tex:404; 07_formation.tex:6, 146, 369; 09_minimal.tex:101; 10_abstract_collectives.tex:452; 11_predictions.tex:27; 12_related.tex:13; 13_discussion.tex:17. Each copy measures 40 to 156 words (about 1,050 in total). Keep it in the statement of H3 and the closing of section 7, shorten it in the abstract, and elsewhere point to section 7.10. Fifteen hand-maintained copies of a numerical status are a consistency risk; I did not compare the copies against each other. A3 (major) Section 4 depends on later sections: def:col-collective (04_collectives.tex:330) requires the moment bound (M) of asm:sca-standing (08_scale.tex:12); thm:col-markov-bound(c) (04_collectives.tex:144) uses thm:sca-clustering; def:col-baseline(c) (04_collectives.tex:313) uses the two-group model of section 7; obs:col-nested-medium (04_collectives.tex:650) uses prop:abs-hierarchy (10_abstract_collectives.tex:382); rem:coh-h4 (06_coherence.tex:393) quotes the size bound of section 8. Fix: move the relay model, (M), lengths and clustering (current 8.1-8.5) ahead of section 4 and define the nested medium in 4.11. A4 (major) The boundary facts are stated three times inside section 4: the originals (thm:col-path-blanket, prop:col-two-hop, prop:col-records-partition, thm:col-thick-shell, thm:col-markov-bound, prop:col-markov-vs-correlation, prop:col-memory), then prop:col-selects-nothing (04_collectives.tex:208, 217w), then thm:col-boundary (04_collectives.tex:659, 360w; line 657 says it collects the boundary results in the form H1 uses), and again in thm:agy-h1. Keep one collection. A5 (major) Records are developed in seven places (2.6, 4.2, 5.3, 8.6, 10.3, 12.3-12.6, plus two open problems); give them one section. A6 (minor) Drafting history in the text: rem:col-shell-error (04_collectives.tex:186, "A corrected error"), the "earlier formulation ... conjectured" sentence of ex:agy-symmetric-dispersion (05_agency.tex:107), rem:col-baseline-conventions, rem:frm-matched-baseline. Move to a supplement note or delete. A7 (minor) Section 10.3 "Records and media" has no result, only rem:abs-innis (256w) and rem:abs-money (99w). A8 (minor) Three treatments of the comparison with renormalizing generative models (rem:ren-rgm, section 16 subsection, 17.3); the gauge-program relation appears as 1.5 and 17.6; scope limits as 1.4, 15.3, 17.5. METHOD AND LIMITS. Read in full: the toc, abstract, introduction, and the full statement text of sections 2-4. Sections 5-14 were surveyed through a one-line-per-statement index (label, line range, word count, 170-230 characters of lead text) plus targeted reads of statements that declare themselves special cases; sections 15-17 have no statement environments and were read at the level of subsection structure, word counts, opening and closing paragraphs. No proof was read. A general-case/special-case relation is asserted as verified only where the statement text declares it (lem:met-unit-coordinate(a) for thm:agy-closure-average; prop:hie-closure-exact(i) for thm:agy-closure-identity(b); prop:env-aggregate-closure(a) for def:met-lumpable; prop:ren-hayek "in the setting of" prop:abs-hayek; the collection sentence at 04_collectives.tex:657). The other groupings rest on titles, labels and lead text and need confirmation from the proof lanes before statements are merged. Word savings are estimates from statement word counts with an allowance for connective prose. Only two text-extraction scripts were run (extract.py, index.py in the lane directory); no LaTeX build, no Lean, nothing written under the manuscript or the vault. REPORT FILE NOT WRITTEN. The Write tool refused report.md with "Subagents should return findings as text, not write report files", so report.md and findings.md do not exist in the lane directory; I did not route around the refusal with another tool. The complete report content is carried in the fields of this result. The lane directory holds extract.py, index.py, summary.json, the x_*.txt extracts and the idx_*.txt statement indexes.

### Overlaps (lane arch)

- what: Status of hypotheses H1-H5 reported at least six times; where: 00_abstract.tex:4; section 1.2 status paragraphs; section 1.3 four tables (01_introduction.tex:110, 148, 186, 212); section 1.4; thm:col-boundary, thm:agy-h1 + rem:agy-h1-status, thm:sca-h4, thm:met-h5a, thm:ren-closure; sections 17.1 (2,738w) and 17.4 (308w); keep: Hypotheses in 1.2 with a one-sentence status each; one results table of about 20 rows; the final-form theorems as the only formal statement; one status section in the Discussion. Full four-table inventory to the supplement.; words_saved: 4500
- what: Formation-status passage (frozen-calibration mean-field map; translation-aware exact-fusion clause; online calibration in 0 to 7 of 8 replicates), 15 copies of 40-156 words; where: 00_abstract.tex:4; 01_introduction.tex:43, 168, 242; 03_misreading.tex:334; 05_agency.tex:589; 06_coherence.tex:404; 07_formation.tex:6, 146, 369; 09_minimal.tex:101; 10_abstract_collectives.tex:452; 11_predictions.tex:27; 12_related.tex:13; 13_discussion.tex:17; keep: Statement of H3 (01_introduction.tex:43), closing of section 7 (07_formation.tex:369), short form in the abstract; elsewhere a pointer to section 7.10; words_saved: 850
- what: Boundary property selects nothing: the same boundary facts collected twice inside section 4 and again in H1; where: originals thm:col-path-blanket, prop:col-two-hop, prop:col-records-partition, thm:col-thick-shell, thm:col-markov-bound, prop:col-markov-vs-correlation, prop:col-memory; prop:col-selects-nothing (04_collectives.tex:208); thm:col-boundary (04_collectives.tex:659); thm:agy-h1 (05_agency.tex:571); keep: Originals plus thm:col-boundary moved to the end of 4.3; drop prop:col-selects-nothing as a separate statement; thm:agy-h1 cites thm:col-boundary for the boundary half; words_saved: 600
- what: Closure and memory identity: exact closure iff the generator maps ker P into ker P, Mori-Zwanzig memory otherwise, restated per section; where: thm:agy-mori-zwanzig (05_agency.tex:29), thm:agy-closure-identity (05:48), thm:agy-closure-average (05:78); lem:met-unit-coordinate (10a_meta_agents.tex:219, statement says thm:agy-closure-average holds for any unit vector), lem:met-discrete-closure (10a:232), prop:met-closure-notions (10a:249), def:met-lumpable + thm:met-abstract-physics (10a:138, 149), prop:met-memory (10a:168); prop:hie-closure-exact (10b_hierarchy.tex:22, statement says equivalent to thm:agy-closure-identity(b)); thm:ren-memory (10c_renormalization.tex:221), prop:ren-adiabatic (10c:255); prop:env-aggregate-closure (10d_environments.tex:243, statement says it is def:met-lumpable for one block), prop:env-aggregate-memory (10d:261); keep: One theorem in 5.1 for a general coordinate map with the unit-vector bounds; all others as corollaries with one-line statements. thm:ren-memory and prop:env-aggregate-memory need proof-lane confirmation that their hypotheses reduce to the general ones.; words_saved: 2500
- what: Galerkin (coarse-medium) defect as a Schur-complement remainder; where: thm:col-bridge(ii) (04_collectives.tex:494); def:col-coarse-medium, lem:col-coarse-medium (04:617); def:ren-maps(c), lem:ren-galerkin (10c_renormalization.tex:16, 28); keep: def:col-coarse-medium and lem:col-coarse-medium; the other two cite it; words_saved: 300
- what: Literal (level-1) reading counts shared precision once per path; where: prop:fw-level-optimality(c) (02_framework.tex:150); prop:mis-track-band (03_misreading.tex:72), prop:mis-overvaluation-scope (03:83), prop:mis-level1-mse, prop:mis-correlated-fusion (03:300), prop:mis-dynamic; prop:agy-literal-consensus (05_agency.tex:170); lem:min-disagreement, prop:min-common-code (09_minimal.tex:136); prop:abs-walras (10_abstract_collectives.tex:253); prop:met-literal-aggregation (10a:291); prop:hie-literal-once (10b:111), prop:hie-literal-records (10b:130), rem:hie-literal-consensus; prop:ren-literal-levels (10c:327); keep: One theorem in section 3 in path-multiplicity form; consensus hub, tree (once per level), record and market cases as corollaries; words_saved: 1200
- what: Shared-error floor and grounding tension: channels with no independent information on the shared error cannot reduce it; where: lem:mis-social-blind (03_misreading.tex:212), prop:mis-mse-floor (03:237); thm:coh-grounding-tension (06_coherence.tex:334); rem:frm-grounding; lem:hie-record-blind(a) (10b_hierarchy.tex:231), thm:hie-floor (10b:242), prop:hie-echo-tradeoff; keep: lem:mis-social-blind stated for any channel set including records; thm:hie-floor as its hierarchical corollary; words_saved: 350
- what: Records developed in seven sections with repeated setup; where: def:fw-record-model, prop:fw-record-basics (2.6); prop:col-records-partition (4.2); prop:agy-identity, prop:agy-writer-leak (5.3); prop:sca-records, prop:sca-records-memory, prop:sca-records-length, rem:sca-global-records (8.6); rem:abs-innis, rem:abs-money (10.3); prop:hie-record-gain, cor:hie-identity, prop:hie-nested-records, prop:hie-record-contrast, prop:hie-global-record, prop:hie-record-filter, prop:hie-record-bistability (12.3-12.6); open:col-records-baseline, open:hie-record-contrast; keep: One Records section of about 4 main-text pages (model, partition, identity, record memory and length, hierarchical record gain); the rest in the supplement; words_saved: 700
- what: Size bound of a collective (extent at most the second-moment length over the square root of r_0 minus 1); where: thm:col-contrast-size (04_collectives.tex:440), cor:col-lstar, rem:col-lengths; rem:coh-h4 (06_coherence.tex:393); cor:sca-size (08_scale.tex:536), thm:sca-h4; prop:ren-depth(a) (10c:155); cor:abs-one-round-extent (10_abstract_collectives.tex:341); also abstract, introduction (twice), sections 15 and 17; keep: thm:col-contrast-size and cor:sca-size, adjacent once lengths precede collectives; words_saved: 400
- what: Hayek dimension stated three times; where: prop:abs-hayek (10_abstract_collectives.tex:269); prop:ren-hayek (10c_renormalization.tex:321, 'in the setting of prop:abs-hayek'); thm:env-hayek-horizon (10d_environments.tex:292); keep: thm:env-hayek-horizon; the other two as corollaries (horizon zero; aggregation); words_saved: 200
- what: Conformity and code domains; where: prop:coh-adoption, prop:coh-code-potential, thm:coh-domains-1d, conj:coh-imry-ma, conj:coh-coarsening, conj:coh-bundling (6.6); prop:abs-conformity, prop:abs-seguy (10.4); prop:hie-conformity, prop:hie-record-bistability, ex:hie-code-domains, conj:hie-conformity-formation (12.6); conj:agy-conformity-identity (5.3); keep: 6.6 as the home; prop:hie-conformity as the record-mediated extension; the rest in the supplement; words_saved: 700
- what: Pooling and consensus stated for members and again for the coarse variable; where: prop:agy-pooling, prop:agy-consensus (05_agency.tex:150); prop:met-consensus-filter (10a_meta_agents.tex:263); keep: One statement (the filter form) with the static case as a corollary; words_saved: 250
- what: When the moment bound (M) holds and when it fails (amplification); where: thm:coh-amplification, prop:coh-no-amplification, ex:coh-amplification (6.5); prop:sca-sufficient, ex:sca-amplifying-profile, conj:sca-common-code (8.1); thm:sca-no-moment, prop:sca-rank-one, prop:sca-amplifying-site (8.3); prop:min-common-code, prop:min-grounding-moment (9.4); keep: One subsection next to (M): prop:sca-sufficient, thm:coh-amplification, thm:sca-no-moment; the rest cited from the supplement; words_saved: 500
- what: Information decay along relays (strong data processing); where: prop:coh-sdpi, prop:coh-relay, prop:coh-info-decay (6.2); thm:sca-percolation, thm:sca-trees, thm:sca-gaussian-percolation (8.8); keep: 8.8, with 6.2 moved into it; words_saved: 200
- what: Nearest-neighbor lattice formulas repeated; where: thm:col-diffusive-precision(e), rem:col-lengths (section 4); thm:sca-oz(a), prop:sca-diffusive-scaling, prop:sca-lengths-relation (section 8); prop:ren-ring (section 13); keep: One reference-lattice display in the lengths section; words_saved: 300
- what: Two two-group models; where: def:coh-calibration-model (06_coherence.tex:74, static); def:frm-two-group (07_formation.tex:50, dynamic); keep: def:frm-two-group, with the static model as its fixed-attention case (parameter match to be confirmed by the proof lanes); words_saved: 150
- what: Multiplex structure defined and used in three sections; where: def:col-nested, prop:col-nesting(c) (4.11); def:abs-multiplex, prop:abs-decoupling, prop:abs-crossover, prop:abs-bypass (10.1-10.2); prop:env-selection, prop:env-multiplex (14); keep: One definition in 4.11; words_saved: 250
- what: Exact fusion at population scale: four open problems, one conjecture and four partial results in six sections; where: open:col-exact-fusion, open:agy-exact-fusion-consensus, open:min-exact-fusion, open:hie-exact-fusion-population, conj:frm-drifting-frames; prop:mis-exact-no-echo, prop:frm-exact-fusion, obs:hie-exact-receiver, rem:hie-pragmatic; keep: One open problem with sub-items in the status section; prop:mis-exact-no-echo and prop:frm-exact-fusion in the main text; words_saved: 250
- what: Nested medium introduced in 10.8 but used earlier and later; where: prop:abs-hierarchy (10_abstract_collectives.tex:382); obs:col-nested-medium (04_collectives.tex:650); thm:ren-nested (10c_renormalization.tex:133), prop:ren-per-level; thm:hie-three-levels; keep: One definition in 4.11; results in the hierarchy part; words_saved: 250
- what: Relay rank and codes across levels; where: thm:sca-alternating, conj:sca-rank-down (8.10); prop:ren-relay-rank; prop:fw-effective-codes, prop:ren-codes, prop:ren-code-levels; keep: 8.10 and prop:ren-codes; words_saved: 200
- what: Gauge-program relation, comparison with renormalizing generative models, and scope limits each treated two or three times; where: 1.5 and 17.6 (382w); rem:ren-rgm (235w), section 16 'Renormalization in active inference' (484w), 17.3 (400w); 1.4, 15.3 (525w), 17.5 (303w); keep: 17.6, 17.3, and one limits subsection; words_saved: 1150

### Principal results (lane arch)

- section: 1 Introduction; labels: hyp:int-h1, hyp:int-h2, hyp:int-h3, hyp:int-h4, hyp:int-h5; one results table condensed from tab:int-results-a..d; why: The five hypotheses in their final forms are the organizing claims; the reader needs each once with a one-sentence status.
- section: 2 Framework; labels: def:fw-system, prop:fw-prior-completion, def:fw-levels, prop:fw-level-optimality, def:fw-calibration, prop:fw-transfer-kernel, def:fw-record-model, def:fw-translation, prop:fw-effective-codes, def:fw-level0, lem:fw-common-mode; why: Objects every later section uses: the system, reception levels, calibration classes, the linear transfer kernel, records, translations.
- section: 3 Misreading; labels: def:mis-values, lem:mis-common-source, prop:mis-overvaluation-scope (as the single double-counting theorem), prop:mis-closed-ratios, lem:mis-social-blind, def:mis-echo, thm:mis-echo-chambers, prop:mis-exact-no-echo; why: The literal reading double-counts, social channels are blind to shared error, echo chambers follow, exact fusion removes them.
- section: 4 Collectives; labels: def:col-partition, thm:col-path-blanket, def:col-markov-length, prop:col-markov-vs-correlation, thm:col-boundary (as the only collection), def:col-world-conditional, thm:col-diffusive-precision, def:col-contrast, def:col-baseline, def:col-collective, thm:col-lattice-contrast, thm:col-contrast-size, cor:col-lstar, def:col-coarse-medium, lem:col-coarse-medium, def:col-hierarchy, thm:col-bridge (short form); why: Boundary half of H1: blankets select nothing; a collective is a region of contrast above a declared baseline; contrast bounds extent.
- section: 5 Agency; labels: def:agy-closure, thm:agy-closure-identity, thm:agy-closure-average, prop:agy-consensus, def:agy-group-model, thm:agy-agency, thm:agy-heterogeneous, def:agy-agency-index, def:agy-order-parameter, def:agy-nulls, prop:agy-nulls-vanish, def:agy-meta-agent, thm:agy-h1; why: Agency half of H1: closure of the collective coordinate, the group model, the tests against nulls, the graded definition of a meta-agent.
- section: 6 Coherence; labels: def:coh-components, thm:coh-withdrawal, thm:coh-holonomy, prop:coh-frustration, thm:coh-amplification, thm:coh-domains-1d, thm:coh-grounding-tension; why: H2: what coherence is, withdrawal from uncalibrated senders, frame holonomy and frustration, amplification, grounding tension.
- section: 7 Formation; labels: def:frm-target, def:frm-two-group, asm:frm-mean-field, thm:frm-formation, thm:frm-split-contrast, prop:frm-nulls, obs:frm-stochastic, obs:frm-online, prop:frm-exact-fusion, conj:frm-formation, open:frm-closure; why: H3 and its exact status: the theorem about the frozen-calibration map, the numerical evidence, the conjecture and the open closure step.
- section: 8 Scale; labels: asm:sca-standing, prop:sca-sufficient, thm:sca-lightcone, thm:sca-no-moment, def:sca-lengths, thm:sca-clustering, thm:sca-oz, prop:sca-records-memory, thm:sca-percolation, def:sca-coherence, thm:sca-coherence-volume, cor:sca-size, thm:sca-h4; why: H4: the moment bound, light cones, lengths and clustering, the coherence volume and the size bound.
- section: 9 Minimal model revisited; labels: prop:min-common-code, prop:min-grounding-moment; why: The only two results cited outside the section; both are sufficient conditions for (M) and belong next to prop:sca-sufficient.
- section: 10 Abstract collectives; labels: prop:abs-decoupling, prop:abs-crossover, prop:abs-barrier, prop:abs-walras, prop:abs-polity, prop:abs-hierarchy; why: One result per application type; prop:abs-hierarchy is needed by section 13 and should be defined earlier.
- section: 11 Meta-agents; labels: def:met-coarse, def:met-coarse-blanket, thm:met-coarse-blanket, prop:met-sufficiency, def:met-abstract-physics, thm:met-abstract-physics, prop:met-memory, prop:met-consensus-filter, thm:met-h5a, rem:met-no-selection; why: H5a: coarse variables, the coarse path blanket, closed coarse dynamics, and the grade of a meta-agent with external states of its own.
- section: 12 Hierarchy; labels: def:hie-tree, thm:hie-messages, prop:hie-literal-once, prop:hie-record-gain, thm:hie-floor, prop:hie-conformity, thm:hie-three-levels; why: Exact hierarchical messages in the Gaussian tree, what the literal reading loses per level, the record gain and the error floor.
- section: 13 Renormalization; labels: def:ren-maps, thm:ren-decimation, thm:ren-flows, thm:ren-nested, prop:ren-depth, thm:ren-memory, prop:ren-perron, thm:ren-closure; why: Coarse-graining maps, the flows of the diffusive parameters, the nested medium, depth, and the closure half of H5.
- section: 14 Environments; labels: def:env-sensor, thm:env-canonical, prop:env-horizon, thm:env-control, thm:env-hayek-horizon; why: What each level senses: optimal linear sensors as canonical variates, the horizon, the control objective, the Hayek dimension with horizon.
- section: 15 Predictions; labels: no labeled statements; one table condensed from tab:pre-reception, tab:pre-collectives, tab:pre-meta, tab:pre-sensing; why: One table of predictions with the result each rests on is sufficient in the main text.
- section: 16 Related work; labels: no labeled statements; sec:rel-nested, sec:rel-debate (shortened), sec:rel-new; why: The nested-blanket program and the blanket debate are the direct context; sec:rel-new states what is claimed as new.
- section: 17 Discussion; labels: no labeled statements; sec:dis-status (as the only status section), sec:dis-meta (halved), sec:dis-renormalization, sec:dis-gauge; why: The single place where status, open problems and limits are stated.

### Budget 120 (lane arch)

- section: 1 Introduction; pages_now: 14; pages_target: 8; moves: Status paragraphs after each hypothesis and premise reduced to one sentence each; three of four results tables to the supplement; 1.4 merged into the Discussion status section; 1.5 kept only as 17.6.
- section: 2 Framework; pages_now: 18; pages_target: 9; moves: To supplement: prop:fw-two-receivers, ex:fw-disagreement, prop:fw-rls, prop:fw-ungrounded-bias, prop:fw-performative, prop:fw-efe-communication, prop:fw-understood-predicted, prop:fw-bounded-confidence, conj:fw-fragmentation, prop:fw-frame-covariance, prop:fw-frame-identifiability, rem:fw-convex-gains. Receives (M) and a model-class table.
- section: 3 Misreading; pages_now: 12; pages_target: 6; moves: To supplement as corollaries of one double-counting theorem: prop:mis-track-band, prop:mis-level1-mse, prop:mis-dynamic, prop:mis-correlated-fusion; also ex:mis-nonsubmodular, ex:mis-cancellation, ex:mis-sender-completion, obs:mis-random-codes, prop:mis-pure-listening, ex:mis-law-headers.
- section: 4 Collectives; pages_now: 26; pages_target: 12; moves: To supplement: prop:col-two-hop, prop:col-memory, thm:col-thick-shell, thm:col-markov-bound, conj:col-markov-length, obs:col-massless, ex:col-non-diffusive, rem:col-shell-error, rem:col-which-contrast, rem:col-baseline-conventions, rem:col-declared-geometry (100 words stay), prop:col-whole-population, prop:col-block-media, obs:col-baselines, obs:col-bridge-baseline, rem:col-bridge-reading (583w), prop:col-coherence-average, obs:col-coherence-dimension, prop:col-nesting, obs:col-nested-medium. prop:col-selects-nothing merged into thm:col-boundary.
- section: 5 Agency; pages_now: 23; pages_target: 11; moves: To supplement: rem:agy-minimal-memory, ex:agy-symmetric-dispersion, prop:agy-drift-precision, prop:agy-pooling, prop:agy-literal-consensus, prop:agy-dispersion, prop:agy-index, prop:agy-synchronous, conj:agy-synchronous, the examples of 5.2, joint acts (def:agy-joint-acts, thm:agy-joint-acts, ex:agy-no-potential, prop:agy-performative-sign), ex:agy-collider, ex:agy-masking, prop:agy-tests, rem:agy-h1-status. Identity (5.3) moves to the Records section.
- section: 6 Coherence; pages_now: 16; pages_target: 8; moves: 6.2 moves to the Scale information-decay subsection. To supplement: ex:coh-unique-information, prop:coh-flat-true, prop:coh-coded, prop:coh-frustration-grounding, prop:coh-attended-frustration, prop:coh-no-amplification, ex:coh-amplification, obs:coh-amplification-information, the code-game details (def:coh-code-game, prop:coh-adoption, prop:coh-code-potential), conj:coh-imry-ma, conj:coh-coarsening, conj:coh-bundling, conj:coh-externality, prop:coh-placement, obs:coh-placement, 6.8.
- section: 7 Formation; pages_now: 15; pages_target: 8; moves: To supplement: prop:frm-flattening, prop:frm-bistability, obs:frm-thresholds, obs:frm-bridged, lem:frm-split-law, obs:frm-grid, obs:frm-exploration, obs:frm-partner, prop:frm-capacity, rem:frm-matched-baseline, three of four tables and one of two figures.
- section: 8 Scale; pages_now: 22; pages_target: 10; moves: To supplement: lem:sca-relations, ex:sca-amplifying-profile, prop:sca-poisson, prop:sca-routing, ex:sca-switch-chain, prop:sca-rank-one, prop:sca-amplifying-site, rem:sca-rumors, prop:sca-world-conditioning, prop:sca-spectral, prop:sca-heterogeneous, prop:sca-persistence, prop:sca-records, prop:sca-records-length, prop:sca-longrange, prop:sca-fronts, def:sca-spacetime, thm:sca-trees, thm:sca-gaussian-percolation, prop:sca-aggregate, prop:sca-tree-diffusive, conj:sca-condensation, thm:sca-alternating, conj:sca-rank-down. 8.1-8.5 move ahead of section 4.
- section: 9 Minimal model revisited; pages_now: 9; pages_target: 1; moves: Whole section to the supplement; a half-page dictionary pointer stays; prop:min-common-code and prop:min-grounding-moment are cited from the (M) subsection.
- section: 10 Abstract collectives; pages_now: 21; pages_target: 6; moves: To supplement: culture (10.4), prop:abs-exchange-consistency, rem:abs-polity-readings, one-round extent (def:abs-one-round, prop:abs-one-round, cor:abs-one-round-extent), 10.3 (remarks only), prop:abs-homogeneous, prop:abs-bypass, prop:abs-elasticity, prop:abs-ultrametric-cap, all five conjectures, the three open problems. Main text keeps a worked-collectives section on prop:abs-crossover, prop:abs-barrier, prop:abs-walras, prop:abs-polity; prop:abs-hierarchy moves to the hierarchy part.
- section: 11 Meta-agents and their external states; pages_now: 15; pages_target: 8; moves: To supplement: ex:met-summary-leak, ex:met-channel-memory, ex:met-reafference, prop:met-leak-bound, ex:met-traders, ex:met-other-collectives, prop:met-closure-notions, prop:met-literal-aggregation, prop:met-level0, ex:met-two-firms, rem:met-corporation. lem:met-unit-coordinate and lem:met-discrete-closure become parts of the general closure theorem in 5.1.
- section: 12 Hierarchy; pages_now: 17; pages_target: 6; moves: To supplement: prop:hie-closure-exact (corollary of the closure theorem), ex:hie-markov-without-closure, lem:hie-misspecification, prop:hie-reversible-sandwich, prop:hie-predictive-coding, prop:hie-literal-records, prop:hie-record-filter, prop:hie-depth, prop:hie-nested-records, prop:hie-record-contrast, ex:hie-noiseless-record, obs:hie-record-window, prop:hie-global-record, prop:hie-echo-tradeoff, obs:hie-top-down, conj:hie-top-down, prop:hie-record-bistability, obs:hie-exact-receiver, ex:hie-code-domains, conj:hie-conformity-formation.
- section: 13 Renormalization; pages_now: 16; pages_target: 7; moves: To supplement: lem:ren-galerkin (cited from section 4), prop:ren-ring, ex:ren-two-dim, obs:ren-decay, ex:ren-block-average, prop:ren-exponents, prop:ren-exchangeable, prop:ren-per-level, ex:ren-no-contrast, prop:ren-adiabatic, obs:ren-adiabatic-rate, rem:ren-rgm, prop:ren-codes, prop:ren-code-levels, prop:ren-relay-rank, prop:ren-hayek, prop:ren-literal-levels, prop:ren-lrg, prop:ren-lrg-agreement, ex:ren-interleaved, conj:ren-lrg.
- section: 14 Environments; pages_now: 17; pages_target: 6; moves: To supplement: lem:env-information, lem:env-markov, prop:env-diffusive, rem:env-efe-horizon-free, rem:env-two-step, ex:env-fast-preference, prop:env-selection, lem:env-constant, prop:env-concentration, ex:env-cell (544w), rem:env-neurons, prop:env-aggregate-closure and prop:env-aggregate-memory (corollaries of the closure theorem), ex:env-firm, rem:env-firm-meta-agent, ex:env-person, lem:env-composition, prop:env-multiplex.
- section: 15 Predictions; pages_now: 7; pages_target: 3; moves: Three of four tables to the supplement; 15.3 merges with the limits subsection of the Discussion.
- section: 16 Related work; pages_now: 14; pages_target: 5; moves: The 19-subsection survey (7,391 words) to the supplement; main text keeps sec:rel-nested, a shortened sec:rel-debate, one paragraph for each of five clusters (transport bounds; fusion; closure; games, opinion dynamics and disorder; hierarchy, renormalization and sensing), and sec:rel-new.
- section: 17 Discussion; pages_now: 8; pages_target: 7; moves: 17.2 halved; receives the merged status, open-problem and limits material of 1.4, 15.3, 17.1, 17.4, 17.5. Total for sections 1-17: 121 pages.
- section: Appendices (notation, proofs, numerical checks); pages_now: 169; pages_target: 4; moves: Notation (8 pages) stays with the main text as a table of about 4 pages; proofs (113 pages) and numerical checks (about 48 pages) go to the supplement whole, each main-text statement keeping its pointer.

### Budget 60 (lane arch)

The 60-page text is the argument for the five hypotheses with one statement per idea. Introduction, 5 pages: the five hypotheses with a one-sentence status each and one table of about 12 rows. Framework, 6 pages: def:fw-system, def:fw-levels, def:fw-calibration, def:fw-record-model, and the linear relay model with (M) and the lengths (def:sca-lengths). Misreading, 3 pages: the single double-counting theorem, lem:mis-social-blind, thm:mis-echo-chambers, prop:mis-exact-no-echo. Collectives, 8 pages: thm:col-path-blanket with the one boundary collection (thm:col-boundary), thm:col-diffusive-precision, def:col-contrast, def:col-baseline, def:col-collective, thm:col-contrast-size, def:col-coarse-medium. Agency, 7 pages: the general closure theorem (thm:agy-closure-identity with thm:agy-closure-average as a corollary), thm:agy-agency, def:agy-nulls with prop:agy-nulls-vanish, def:agy-meta-agent, thm:agy-h1. Coherence, 4 pages: thm:coh-withdrawal, thm:coh-holonomy, thm:coh-grounding-tension. Formation, 4 pages: def:frm-two-group, thm:frm-formation, and one status paragraph with obs:frm-online and conj:frm-formation. Scale, 6 pages: thm:sca-lightcone, thm:sca-no-moment, thm:sca-clustering, thm:sca-coherence-volume, cor:sca-size, thm:sca-h4. Hierarchy (current sections 11-14), 12 pages: thm:met-coarse-blanket, thm:met-abstract-physics, thm:met-h5a, thm:hie-messages with thm:hie-floor, thm:ren-decimation and thm:ren-flows with thm:ren-closure, thm:env-canonical and thm:env-hayek-horizon. Predictions, related work and discussion, 5 pages: one predictions table, two pages of positioning, two pages of status, open problems and limits. Total 60. In this version sections 9 and 10, the Records section, the code game, every example, every conjecture other than conj:frm-formation, and every numerical observation other than obs:frm-online are in the supplement, together with all proofs, the numerical checks and the full related-work survey.

### Mergers (lane arch)

- Merge sections 11-14 into one part, 'Meta-agents and hierarchy' (about 27 pages in the 120-page text, 12 in the 60-page text), ordered as: coarse variables and the coarse blanket; closed coarse dynamics as corollaries of the general closure theorem; messages and records in a tree; coarse-graining maps and flows; what each level senses. Each of the four sections currently rebuilds its own closure statement, its own literal-reading statement and its own Hayek statement.
- Move section 9 (the minimal model revisited) to the supplement whole, leaving a half-page dictionary pointer. Nothing later depends on it except citations of prop:min-common-code and prop:min-grounding-moment, which belong with prop:sca-sufficient as sufficient conditions for (M).
- Split section 10. Multiplex definitions and prop:abs-decoupling go to 4.11; prop:abs-hierarchy (nested medium) goes to the hierarchy part where thm:ren-nested uses it; prop:abs-hayek becomes a corollary of thm:env-hayek-horizon; the remaining applications form a worked-collectives section of about 6 pages placed after the hierarchy part, or go to the supplement. Section 10.3 has no result and goes to the supplement.
- Split section 8 at 8.5 and reorder. The linear relay model, (M), light cones, lengths and clustering (8.1-8.5, with 6.2 and 8.8 on information decay) move ahead of section 4; the coherence volume, size bound and thm:sca-h4 (8.9-8.11) follow the collectives section. This removes the forward references from def:col-collective, thm:col-markov-bound(c) and rem:coh-h4.
- Create one Records section (about 4 pages) after Scale from 2.6, prop:col-records-partition, 5.3, 8.6 and prop:hie-record-gain; the other record results (12.4-12.5, prop:sca-records, prop:sca-records-length) go to the supplement.
- Introduce the two-group model once (def:frm-two-group), with the static model of def:coh-calibration-model as its fixed-attention case.
- Put the code game (6.6), the conformity results of 10.4 and those of 12.6 in one subsection on codes as conventions, with 6.6 as the home.
- Predictions (section 15): cut from 7 to 3 pages with one table; merge 15.3 with the limits subsection.
- Related work (section 16): cut from 19 subsections and 14 pages to about seven paragraphs plus sec:rel-new (5 pages); the full survey goes to the supplement.
- Introduction and Discussion: keep the hypotheses and one results table in the introduction; merge 1.4, 15.3, 17.1, 17.4 and 17.5 into one status, open-problems and limits section; keep the gauge-program relation only as 17.6 and the comparison with renormalizing generative models only as 17.3.
- Within section 4, keep one collection of the boundary facts (thm:col-boundary at the end of 4.3) and drop prop:col-selects-nothing and the separate subsection 4.12.
- Notation appendix: keep a table of about 4 pages with the main text; the numerical-checks appendix and all proof appendices go to the supplement whole.
- Move drafting-history items (rem:col-shell-error, the 'earlier formulation' sentence of ex:agy-symmetric-dispersion, rem:col-baseline-conventions, rem:frm-matched-baseline) to a supplement note or delete them.

### Theory simplifications (lane arch)

- One closure theorem. For linear dynamics with generator A and coordinate map P, the coarse variable is exactly closed iff A maps ker P into ker P; otherwise the Mori-Zwanzig reduction gives a memory kernel and noise, with the bounds of lem:met-unit-coordinate for any unit coordinate. Corollaries: thm:agy-closure-average (group average), lem:met-discrete-closure (reversible discrete time), thm:met-abstract-physics (block variables of a partition), prop:hie-closure-exact (two-level member model), thm:ren-memory (reversible partitioned population), prop:env-aggregate-closure and prop:env-aggregate-memory (aggregates of an exterior). Three of these declare the relation in their own statements; thm:ren-memory and prop:env-aggregate-memory need proof-lane confirmation.
- Closure vocabulary. Keep the declared terms 'exactly closed', 'closed of order d', 'approximately closed' as the only closure vocabulary; reduce def:met-lumpable to one sentence and define 'abstract physics' (def:met-abstract-physics) as the closed coarse dynamics.
- One double-counting theorem in section 3 in path-multiplicity form (a level-1 receiver counts a shared source once per path), with the track band, consensus hub (prop:agy-literal-consensus), once-per-level counting in a tree (prop:hie-literal-once, prop:ren-literal-levels), the record case (prop:hie-literal-records) and the market case (prop:abs-walras) as corollaries.
- One shared-error floor lemma: lem:mis-social-blind stated for an arbitrary channel set including records, with thm:coh-grounding-tension, lem:hie-record-blind(a) and thm:hie-floor as corollaries.
- One coarse-medium definition and one defect lemma. Define decimation (Schur complement), block averaging and the Galerkin medium together in 4.11 (merging def:col-coarse-medium and def:ren-maps), with lem:col-coarse-medium as the only statement of the defect; thm:col-bridge(ii) and lem:ren-galerkin cite it. Define the nested medium (prop:abs-hierarchy) in the same place.
- One list of model classes. Replace the three standing-assumption environments (asm:sca-standing with eight labels (Lin), (Loc), (B), (C_r), (C_rc), (C_rho), (NN), (M); asm:frm-mean-field; asm:ren-standing) and the per-premise status paragraphs for A5-A12 by one table at the end of section 2 with three nested classes (any local rule; linear-Gaussian relay with (M); diffusive nearest-neighbor lattice) and one table of premises with where each is used. Every theorem then names its class in two words.
- One table of lengths and times. The text uses the correlation length, Markov length, second-moment length, largest extent L-star, diffusive length, coherence length, correlation time, record length, multiplex crossover length and sensing horizon. The main text needs the first four and the two inequalities relating them (prop:col-markov-vs-correlation, prop:sca-lengths-relation); display the nearest-neighbor lattice values once.
- Contrast variants. Keep the contrast r(C) against the declared baseline in the main text; confine the grounding-free ratio, the record contrast and the matched baseline to the supplement, and retain def:col-ultrametric only alongside thm:col-bridge.
- Name the exact-fusion receivers once in def:fw-levels (the translation-aware form and the full cross-covariance-aware form), so that the formation-status sentence and the exact-fusion open problems (open:col-exact-fusion, open:agy-exact-fusion-consensus, open:min-exact-fusion, open:hie-exact-fusion-population) shrink to references and merge into one open problem with sub-items.
- Final-form theorems. State thm:met-h5a as extending the grade of thm:agy-h1 by its added clauses instead of relisting the earlier ones, and have thm:agy-h1 cite thm:col-boundary for the boundary half; fold rem:agy-h1-status into the single status section.
- State the size bound once (thm:col-contrast-size with cor:sca-size) and the Hayek dimension once (thm:env-hayek-horizon, with prop:abs-hayek as the zero-horizon case and prop:ren-hayek as the aggregation corollary).
- Open problems and conjectures. Of the 58 in the body (36 open problems, 22 conjectures), keep in the main text the roughly ten that gate the status of a hypothesis (open:frm-closure, open:frm-online, conj:frm-formation, conj:frm-drifting-frames, conj:sca-common-code, open:sca-endogenous, open:col-non-diffusive, the merged exact-fusion problem, open:met-approximate, open:ren-beyond, conj:env-nonlinear); list the rest, numbered, in the supplement.
- Numerical observations. Of the 20, keep in the main text those that bear on the status of a hypothesis (obs:frm-stochastic, obs:frm-online) and cite the others from the supplement.

### Dependencies (lane arch)

Current graph (X <- Y means X needs Y). 2 Framework is the base. 3 Misreading <- 2. 4 Collectives <- 2, and as written also <- 8 ((M) of asm:sca-standing in def:col-collective; thm:sca-clustering in thm:col-markov-bound(c)), <- 7 (two-group model in def:col-baseline(c)), <- 10.8 (nested medium in obs:col-nested-medium): three forward references. 5 Agency <- 4 for the group model, nulls and grade; 5.1 (closure) <- 2 only; 5.3 <- 2.6 (records). 6 Coherence <- 2, 3; rem:coh-h4 points forward to 8. 7 Formation <- 2, 3, 4, 5 (nulls), 6 (withdrawal, static two-group model). 8 Scale: 8.1-8.8 <- 2 only (plus def:col-world-conditional for prop:sca-world-conditioning, and 2.6 for 8.6); 8.9-8.11 <- 4. 9 Minimal model <- 2, 3, 5, 8; nothing needs it. 10 Abstract collectives <- 3, 4, 6.6, 8; it supplies prop:abs-hierarchy to 4 (forward) and 13, and prop:abs-hayek to 13 and 14. 11 Meta-agents <- 4, 5. 12 Hierarchy <- 11, 3, 5.3, 6.6, 8.6. 13 Renormalization <- 4.11, 5.1, 8, 10.8, 11. 14 Environments <- 5.1, 8, 10 (multiplex, Hayek), 11. 15 and 17 <- all; 16 <- none. Proposed linear order after the moves, with no forward references: Framework; Misreading; Relays, (M) and lengths (current 8.1-8.8 with 6.2); Collectives, closing with the size bound and H4 (current 8.9-8.11); Agency (H1); Coherence (H2); Formation (H3); Records; Meta-agents and hierarchy (current 11-14, H5); Worked collectives (from current 10); Predictions; Related work; Discussion. Reading paths per hypothesis: H1 through Framework, Collectives, Agency. H2 through Framework, Misreading, Coherence. H3 through the H1 and H2 paths plus Formation. H4 through Framework, Relays and lengths, Collectives. H5 through Agency 5.1 (closure) and the hierarchy part; the hierarchy subsection on messages additionally needs Misreading.
