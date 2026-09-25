# L14 panel report: citations and literature (PIFB2.tex, 2026-09-24)

**Lens:** L14, citation and literature audit (bibliographic integrity, attribution fidelity, missing prior art).
**Model:** Claude Opus 5.5 (investigator; no adjudication run).
**Target:** `Research/manuscripts/PIFB2.tex`, SHA-256 `f80e6dab…080ec4` (confirmed), with `Research/manuscripts/references.bib` (5041 lines).
**Lines read:** every line carrying a `\cite` (extracted by script, 284 uses of 186 keys), with the enclosing sentence; in full: 128-135 (related work), 380-386, 1195-1213, 1304-1324, 1573, 1681-1685, 1759-1762, 3262-3270, 3762. Bib entries for all load-bearing keys were read directly.
**Executed:** `scripts/L14_cites.py` (key extraction, resolution, duplicates, prior-art lookup; writes `L14_cites.json`), `scripts/L14_contexts.py` (sentence extraction per key), `scripts/L14_checks.py` (three numerical checks of cited content), `scripts/L14_annotate.py` (adds verdicts to `L14_cites.json`); a scratch `pdflatex -draftmode` + `bibtex` build of PIFB2 in the session scratchpad (not in the review tree). Primary records checked on the web: Crossref (Ramstead et al. 2020, Bény-Osborne 2015, Bonnabel-Sepulchre, Afsari 2011, Kendall 1990, Da Costa et al. 2021), PLoS Biology full text (Sengupta et al. 2016), arXiv (Millidge et al. full PDF text searched; Sengupta-Friston 1705.06614; Thanwerdas-Pennec 1906.01349), and search records for Skovgaard 1984, Caticha 2012, Machta et al. 2013, Fields et al. 2022, Pinchetti et al. 2022, Andruchow et al. 2014, Friston et al. 2017.

Summary numbers: 186 distinct keys, 284 citation uses. 3 keys are unresolved; there are no duplicate keys and no case collisions among keys. BibTeX confirms exactly those three warnings and emits 183 bibitems.

## Findings (ranked)

### L14-1: Three citation keys do not resolve; the Karcher-mean uniqueness radius and the Kron-reduction claim print as "[?]"
**Location:** PIFB2.tex:1573 and 3762 (`Kendall1990`, `Afsari2011`, cited for the uniqueness radius under `eq:meta_agent_frame_barycenter`, and again in App. I); PIFB2.tex:1685 (`DorflerBullo2013`).
**Severity:** high (submission blocker: the cited load-bearing hypothesis of the frame barycenter shows unresolved references).
**Evidence:** `L14_cites.py` reports `missing: ['Afsari2011', 'DorflerBullo2013', 'Kendall1990']`. The scratch BibTeX run prints `Warning--I didn't find a database entry for "Kendall1990"`, the same for `"Afsari2011"` and `"DorflerBullo2013"`, and "(There were 3 warnings)". The bib holds the Dörfler-Bullo paper under `DorflerBullo2013Kron` (line 4350). None of the three keys is in `Theory/references.bib` either.
**Fix:** Change `DorflerBullo2013` to `DorflerBullo2013Kron` at 1685. Add two entries (both verified on Crossref): Kendall, W. S., "Probability, convexity, and harmonic maps with small image I: uniqueness and fine existence," Proc. London Math. Soc. s3-61(2), 371-406 (1990), doi 10.1112/plms/s3-61.2.371; Afsari, B., "Riemannian L^p center of mass: existence, uniqueness, and convexity," Proc. Amer. Math. Soc. 139(2), 655-673 (2011), doi 10.1090/S0002-9939-2010-10541-5. The content of the sentence matches these sources as I know them: Kendall gives uniqueness on regular geodesic balls of radius below pi/(2 sqrt(Delta)), and Afsari gives r_cx = (1/2) min{inj, pi/sqrt(Delta)}. Both equal pi/2 at unit curvature when inj is at least pi. I did not re-read either paper.
**Falsifies:** A build that uses a different .bib containing these keys.
**Status:** P by citation once the entries exist. Not inflated.

### L14-2: The distinguishability route to "it from bit" omits Wootters, whose result Wheeler's 1990 paper itself quotes, and "precise realization" overstates it
**Location:** PIFB2.tex:1830 (Fisher-Rao distinguishability unit, cited to Cover-Thomas and Amari-Nagaoka); PIFB2.tex:1872 ("Wheeler's 'it from bit' … is given a precise fixed-gauge realization as the ordinary pullback of the Gaussian Fisher-Rao metric").
**Severity:** medium (thesis-bearing for goal 1; a quantum-foundations referee will spot the omission at once).
**Evidence:** Wootters (Phys. Rev. D 23, 357, 1981) defines statistical distance through the number of samples N needed to distinguish two states, and shows it is proportional to Hilbert-space angle. Wheeler 1990 quotes this result as a candidate link between information and quantum geometry (confirmed from search records that describe the Wheeler paper). Braunstein and Caves (PRL 72, 3439, 1994) is the standard physics reference for the Fisher metric as statistical distance. Neither paper is in references.bib (`grep "Wootters, W"` finds only Page-Wootters). The sentence at 1830 is a heuristic single-sample threshold (g delta theta^2 of order 1); Wootters' N-sample form, N g delta theta^2 of order 1, is the calibrated statement. At 1872 the pullback of a Fisher metric is a structural reading of Wheeler's yes/no-registration thesis, not a derivation of it. That is status S, but the prose calls it a "precise realization".
**Fix:** At 1830 cite Wootters 1981 and Braunstein-Caves 1994 and state the N-sample form: "two beliefs are reliably distinguishable from N independent observations when N g_B(delta theta, delta theta) is at least of order one [Wootters1981, BraunsteinCaves1994]." At 1872 write: "…here that proposal receives a concrete classical-statistical model, the pullback of the Gaussian Fisher-Rao metric, in the lineage of Wootters' statistical distance, which Wheeler cited as a candidate link between information and geometry."
**Falsifies:** If Wheeler 1990 does not discuss Wootters' distinguishability result, the "Wheeler quotes it" clause falls, but the prior-art gap remains.
**Status:** S. Inflated at 1872 ("precise realization").

### L14-3: Related work leaves out the physics side of the it-from-bit program and the quantum free-energy-principle paper
**Location:** PIFB2.tex:128-135 (Related Work); 1767 (participatory traditions); 2142 (C5, density-operator scale-0 fiber).
**Severity:** medium (goal 2: physics venue; goal 1: standalone thesis).
**Evidence:** The related work cites the thermodynamic, holographic and entanglement programs, constructor theory, relational QM and QBism. It cites none of the informational reconstructions of quantum theory, which are the literature a foundations-of-physics referee reads as "it from bit" today. The same set is absent from references.bib (grep for Zeilinger, Chiribella, Hardy and Höhn: 0 hits each). Fields, Friston, Glazebrook and Levin, "A free energy principle for generic quantum systems," Prog. Biophys. Mol. Biol. 173, 36-59 (2022), doi 10.1016/j.pbiomolbio.2022.05.006, is also absent. It is the closest published attempt to put the FEP on quantum systems with holographic-screen observers, which is exactly the C5 extension PIFB2 lists as open.
**Fix:** Add one paragraph to Section 3. Cite Zeilinger (Found. Phys. 29, 631, 1999), Chiribella, D'Ariano and Perinotti (Phys. Rev. A 84, 012311, 2011), and Höhn (Quantum 1, 38, 2017) as the physics lines of "it from bit". State that PIFB2 does not reconstruct quantum theory, and cite Fields et al. 2022 at C5 (2142) as the existing quantum-FEP precedent. I did not verify the metadata of the three reconstruction papers online (known records).
**Falsifies:** An argument that the paper targets a venue where quantum reconstructions are out of scope. But Part II's quantum-foundations claims (1767, 2042, 2084) put them in scope.
**Status:** Positioning. The novelty statements at 134 and 522 are narrower once these are acknowledged.

### L14-4: "Yang-Mills" appears about ten times with no gauge-theory primary citation
**Location:** PIFB2.tex:142, 353, 358 (the "standard Yang-Mills gauge-transformation law"), 418, 429, 713, 920, 1796, 1898, 2146.
**Severity:** medium (physics audience).
**Evidence:** `Yang1954` (Phys. Rev. 96, 191) is in references.bib but not cited. `kobayashi1963foundations` and `Kobayashi1963` are in the bib and not cited. Wu and Yang, "Concept of nonintegrable phase factors and global formulation of gauge fields," Phys. Rev. D 12, 3845 (1975), is absent. That paper is the physics dictionary between gauge potentials and bundle connections that the bundle language of 136-515 relies on. Utiyama (Phys. Rev. 101, 1597, 1956), for gauge fields of a general Lie group, is absent. Only Nakahara and Frankel carry the bundle formalism.
**Fix:** Cite Yang1954 at the first "Yang-Mills" (142) and at 358. Cite Wu-Yang 1975 with Nakahara at 214 for the associated-bundle and connection dictionary. Optionally cite Kobayashi-Nomizu at 225 for the convention.
**Falsifies:** None. This is a presence check.
**Status:** P facts cited to textbooks. The issue is missing primary sources.

### L14-5: RG prior art missing or uncited, including a literature the text names without citing
**Location:** PIFB2.tex:1685 ("the rigorous non-Gibbsianness literature", uncited); 1681-1683 (RG status); 3490 and 3516 ("Kikuchi" regions); 3723 (retention principles).
**Severity:** medium (physics audience; the RG section is where a statistical-physics referee will concentrate).
**Evidence:** Several relevant works are absent from references.bib. Van Enter, Fernández and Sokal (J. Stat. Phys. 72, 879-1167, 1993) is the rigorous non-Gibbsianness reference that 1685 alludes to. Machta, Chachra, Transtrum and Sethna (Science 342, 604-607, 2013) trace effective theories to compression of Fisher-information eigenvalues under coarse-graining; this is the information-geometric counterpart of the relevance criterion at 3723 and of the threshold detector. Kikuchi (Phys. Rev. 81, 988, 1951) is the primary source for the cluster-variation method named at 3490 and 3516. Koch-Janusz and Ringel (Nat. Phys. 14, 578, 2018) give mutual-information RG. Four others are in the bib but uncited: `BermanKlingerStapleton2023` (Bayesian renormalization, Mach. Learn.: Sci. Technol. 4, 045011), `kadanoff1966scaling` (block spins, the natural reference for meta-agents as block variables), `villegas2023laplacian` (Laplacian RG for networks, Nat. Phys. 19, 445), and `HansenGhrist2019`. Bény-Osborne 2015, Mehta-Schwab 2014 and Wilson's lattice action are present and cited. Bény-Osborne's metadata is verified on Crossref: PRA 92, 022330.
**Fix:** At 1685 cite van Enter-Fernández-Sokal. At 1683, after Bény-Osborne, add Machta et al. 2013 and Berman et al. 2023, with one clause each: Fisher-eigenvalue compression, and Bayesian updating read as an RG flow on the Fisher manifold. At 1685 cite Villegas et al. 2023 with Loukas for network coarse-graining. At 3490 cite Kikuchi 1951. Cite Kadanoff 1966 at the first block-variable description of the barycenter (1533ff).
**Falsifies:** An explicit author decision to confine RG positioning to the Theory's Supplement B.
**Status:** The text already fences RG as "RG-inspired" (1681), which is correct. The omissions are positional.

### L14-6: Closest mathematical precedents for transport-coupled consensus with holonomy are uncited (sheaf and connection Laplacians; gauge-equivariant networks)
**Location:** PIFB2.tex:134 ("distinguishing features … explicit gauge structure with section fields and inter-agent transport"); 522 (novelty of the KL(q_i || Omega_ij q_j) coupling).
**Severity:** medium (novelty claim, and the paper's pairing with the Theory).
**Evidence:** Singer and Wu, "Vector diffusion maps and the connection Laplacian," CPAM 65, 1067 (2012), has O(d) transports on graph edges whose non-flatness is holonomy. Hansen and Ghrist, "Opinion dynamics on discourse sheaves," SIAM J. Appl. Math. (2021), doi 10.1137/20M1341088, has consensus under edge restriction maps. The discrete PIFB2 structure (Omega_ij on edges, gauge law `eq:omega_gauge_law`, loop holonomy) is the probabilistic analog of both, and neither is in the Research bib. They are in `Theory/references.bib` and cited in `Theory/c15_related_work.tex`. `cohen2019gauge` (ICML 2019) and `He2021GaugeEquivariantTransformer` (NeurIPS 34) are in the Research bib and uncited. The gauge-equivariant transformer is the obvious comparison for a paper that recovers attention as a gauge-fixed limit. The novelty sentence at 522 is limited to "closed variational form with an inter-frame transport law," and that limit is defensible. The contrast has to be stated against these works, not left implicit.
**Fix:** Add one sentence to Section 3: "Transport-coupled consensus on graphs with edge maps is studied as the connection Laplacian [SingerWu2012] and sheaf-Laplacian opinion dynamics [HansenGhrist2021Discourse]; gauge-equivariant networks [cohen2019gauge, He2021GaugeEquivariantTransformer] impose frame covariance on learned features. The present construction differs in coupling probability laws through a KL functional with state-dependent attention weights." Copy the two entries from the Theory bib.
**Falsifies:** Showing that one of these works already writes a KL-coupled Gaussian consensus with GL(K) transports. In that case the novelty claim at 522 must shrink further.
**Status:** Novelty claim, S-level positioning.

### L14-7: Misattributed source for the two-parameter congruence-invariant metric family on SPD matrices
**Location:** PIFB2.tex:2328 (`\cite{Pennec2006, Amari2016, Bhatia2007}`).
**Severity:** low (the mathematics is correct; the cited sources are not where it is stated).
**Evidence:** `L14_checks.py` (a): congruence invariance residual 2.29e-14. The Gram matrix on Sym(4) has minimum eigenvalue +4.0e-3 at a+Kb = +0.004 and -4.0e-3 at a+Kb = -0.004, and is negative for a = -0.1. So the condition "a > 0 and a + Kb > 0" is exact. Thanwerdas and Pennec (arXiv:1906.01349, Sec. 2.1) attribute the family to Pennec, "Statistical Computing on Manifolds," LNCS 5416 (2009). That is the bib's `Pennec2009`, already cited at 1573. Pennec 2006 (JMIV) is a general intrinsic-statistics paper. As far as I know, Bhatia 2007 uses the single metric tr(A^-1 dA A^-1 dA). I did not re-read Bhatia or Amari 2016 for the family, so this is a residual.
**Fix:** Replace the cite with `Pennec2009`. Optionally add Thanwerdas and Pennec, GSI 2019, LNCS 11712.
**Falsifies:** A page in Pennec 2006, Amari 2016 or Bhatia 2007 stating the two-parameter family.
**Status:** P. Not inflated.

### L14-8: Bonnabel-Sepulchre cited for left-invariant metrics on GL(K); the paper concerns fixed-rank PSD matrices
**Location:** PIFB2.tex:1573 ("the left-invariant metric induced by a fixed inner product on gl(K_q)~\cite{BonnabelSepulchre2009}").
**Severity:** low.
**Evidence:** Crossref record: "Riemannian Metric and Geometric Mean for Positive Semidefinite Matrices of Fixed Rank," SIAM J. Matrix Anal. Appl. 31(3), 1055-1070. The abstract describes a quotient geometry on rank-p PSD matrices, not left-invariant metrics on GL(n).
**Fix:** Cite Andruchow, Larotonda, Recht and Varela, "The left invariant metric in the general linear group," J. Geom. Phys. 86, 241-257 (2014). Milnor 1976, already cited in the same sentence, also covers left-invariant metrics.
**Falsifies:** A section of Bonnabel-Sepulchre constructing left-invariant GL metrics. The abstract gives no sign of one.
**Status:** Attribution only.

### L14-9: Millidge et al. 2021 does not supply a "predictive-coding reading" of transformer attention
**Location:** PIFB2.tex:1771 ("kernel, modern-Hopfield, and predictive-coding readings~\cite{tsai2019transformer, ramsauer2021hopfield, millidge2021predictive}").
**Severity:** low.
**Evidence:** I searched the full arXiv:2107.12979 text (v4 PDF, scripted in the scratchpad). "transformer" gets 5 hits, all as ML context or an open question ("the degree to which … transformers can be straightforwardly integrated into the predictive coding paradigm"). "self-attention" and "Hopfield" get 0 hits. Tsai 2019 (kernel reading) and Ramsauer 2021 (Hopfield reading) are correctly attributed.
**Fix:** Cite Pinchetti, Salvatori, Yordanov, Millidge, Song and Lukasiewicz, "Predictive coding beyond Gaussian distributions," NeurIPS 35, 1280-1293 (2022), which trains transformers under predictive coding. Or say "and predictive-coding approaches to training such architectures."
**Falsifies:** A section of the review deriving attention from predictive coding. Text search found none.
**Status:** Attribution only.

### L14-10: Friston et al. 2017 carries claims about hierarchical active inference that it does not make
**Location:** PIFB2.tex:1675, 3165, 3265 ("the standard scheme … level-l prior derived from p(s_l | s_{l+1})"); 1882 ("…rather than the moment-to-moment posterior as the hierarchical active-inference literature does~\cite{Friston2017}").
**Severity:** low.
**Evidence:** Friston et al. 2017's abstract (search record) describes a process theory for "a standard (Markov decision process) generative model" and gradient descent on free energy. It is a single-level scheme. `friston2008hierarchical` ("Hierarchical models in the brain," PLoS Comput. Biol. 4, e1000211) is in the bib and uncited. The claim at 1882, that the hierarchical literature places the perceptual "interface carrier" in the posterior, is not a claim Friston 2017 makes.
**Fix:** At 1675, 3165 and 3265 cite `friston2008hierarchical` together with `parr2022active`. At 1882 delete the attribution clause, or rephrase as the author's contrast: "whereas predictive-processing accounts usually identify perceptual content with the posterior [Clark2016, Seth2021]."
**Falsifies:** A section of Friston 2017 on hierarchical conditional priors. None appears in the abstract, and I did not read the full text.
**Status:** Attribution only.

### L14-11: "Standard active inference arrives at natural-gradient descent" is cited only to Amari
**Location:** PIFB2.tex:1761.
**Severity:** low.
**Evidence:** Amari 1998 defines natural gradient. The claim that active-inference belief updates are natural-gradient descent comes from Da Costa, Parr, Sengupta and Friston, Entropy 23, 454 (2021), which the Crossref record says shows the dynamics "approximate natural gradient descent". Friston 2017 describes plain gradient descent.
**Fix:** "…the route by which neuronal dynamics under active inference approximate first-order natural-gradient descent [DaCosta2021], an intrinsic Riemannian gradient flow in the sense of Amari [Amari1998]…"
**Falsifies:** A standard-AIF source stating an exact natural-gradient scheme.
**Status:** S/E in the source. Slightly inflated ("arrives at").

### L14-12: Bibliographic metadata errors in cited entries
**Location:** references.bib entries `Ramstead2019`, `Caticha2015`, `Sonderby2016`, and DOI coverage.
**Severity:** low.
**Evidence:** (i) Crossref gives Ramstead, Kirchhoff and Friston, Adaptive Behavior **28**(4), **225-239** (print 2020, online 21 July 2019), doi 10.1177/1059712319862774. The bib has vol. 27, pp. 369-385, 2019. (ii) `Caticha2015` is recorded as "AIP Conference Proceedings … 2015". The work titled "Entropic Inference and the Foundations of Physics" is Caticha's 2012 monograph for EBEB-2012, USP Press, São Paulo. (iii) `Sonderby2016` has no pages (NeurIPS 29, 3738-3746). (iv) Most load-bearing physics entries lack DOIs, including Wilson1971 (10.1103/PhysRevB.4.3174), WilsonConfinement1974 (10.1103/PhysRevD.10.2445), Wilson-Kogut (10.1016/0370-1573(74)90023-4) and Friston2010 (10.1038/nrn2787). Physics journals usually require DOIs. (v) Cosmetic: key `Dehaene2014` points to the 2011 Neuron paper, and key `Maldacena1999` points to the 1998 ATMP paper. Under `unsrt` these do not print. Hygiene outside PIFB2's cited set: the bib holds the same work under two keys for Mehta-Schwab, Karcher, Kobayashi-Nomizu, Bronstein, and Fuchs et al. (`Fuchs2013`/`Fuchs2014`). The Theory cites Mehta-Schwab as `MehtaSchwab2014`; PIFB2 cites `mehta2014exact`.
**Fix:** Correct (i)-(iii) and add DOIs. Pick one key per work across the pair.
**Falsifies:** A differently paginated print record for (i). Crossref shows none.
**Status:** Metadata.

### L14-13: Ladder-VAE comparison overstated; enactive-inference attribution inflated
**Location:** PIFB2.tex:3267 ("The relationship to ladder VAEs … becomes precise"); 1775 ("the multi-agent realization, on a transformer architecture, of the enactive-inference reading … of Ramstead, Kirchhoff and Friston").
**Severity:** low.
**Evidence:** The top-down Gaussian conditional p(z_l | z_{l+1}) that PIFB2 compares with is common to every hierarchical VAE. What distinguishes the ladder VAE is its inference path, a precision-weighted merge of bottom-up and top-down statistics. Sønderby et al. use diagonal, not isotropic, variances. Ramstead et al. treat a single embodied organism coupled through action. A transformer in the zero-dimensional limit has no action channel, so "realization" is status S dressed as P.
**Fix:** At 3267: "The Gibbs factor is a special case of the top-down Gaussian conditional of hierarchical VAEs [Sonderby2016]…" At 1775: "…is compatible with the enactive reading of active inference advanced by Ramstead, Kirchhoff and Friston [Ramstead2019]…" For a physics venue, consider cutting the ladder-VAE paragraph.
**Falsifies:** If PIFB2's parent message used the LVAE precision-weighted merge, "precise" would be closer. I did not check the barycenter formula against the LVAE merge.
**Status:** S. Inflated ("precise", "realization").

## Verified, no defect

1. Bibliographic integrity beyond L14-1. 186 distinct keys and 284 uses. No duplicate keys, no case-insensitive collisions, and all other keys resolve. Method: `L14_cites.py` plus the scratch BibTeX run (183 bibitems, exactly 3 warnings). Residual: the regex covers `\cite`, `\citep`, `\citet` and similar forms; a grep for cite commands spanning line breaks found none.
2. Du-Hu-Lee balancedness in PIFB2's convention (1212). For M_h = A_Q A_K^T, gradient flow conserves A_Q^T A_Q - A_K^T A_K: drift 3.6e-13 over a flow that cut the loss from 16.7 to 0.36. The other ordering, A A^T, drifts by 5.3, so PIFB2's index placement is the correct one. Script: `L14_checks.py` (b).
3. Two-parameter SPD metric family and its positivity condition (2328). Invariance residual 2.3e-14, and the eigenvalue sign flips exactly at a+Kb = 0. Script: `L14_checks.py` (a). The attribution is in L14-7.
4. ALiBi slopes m_h = 2^(-8h/H) (633). For H = 8 this gives 1/2 … 1/256, matching Press et al.'s schedule. Script: `L14_checks.py` (c). Residual: checked against my knowledge of the paper; I did not re-read it.
5. Sengupta et al. 2016 (132). The characterization (prediction errors as local forces, compensatory top-down fields, attention tied to precision and gauge fields) matches the PLoS Biology 14(3) e1002400 text. The paper treats single systems, which is consistent with PIFB2's "multi-agent extension" contrast. Method: primary full text via WebFetch.
6. Skovgaard 1984 mixed-sign curvature (429, 462). Some sectional curvatures are positive for K >= 2. Method: secondary statement of Skovgaard's result (Nielsen 2023, PMLR v221). Residual: primary not read.
7. Bény-Osborne 2015 metadata (PRA 92, 022330) is verified on Crossref. The characterization at 1683 (coarse-graining channels, pulled-back Fisher metric, contraction) is consistent with the paper as I know it. Residual: full text not re-read.
8. Wilson-Kogut is correctly dated 1974 (Phys. Rep. 12, 75-199). The task text's "1975" is not the publication year. `WilsonConfinement1974` (PRD 10, 2445) supports the link-variable law at 380. Residual: the pin-cite "Eq. 12" was not checked.
9. Chentsov (finite sample spaces) and Ay-Jost-Lê-Schwachhöfer (general parametrized models) at 178 are correctly split. Method: knowledge of both texts; not re-read.
10. Friston 2010, Parr et al. 2022, Kirchhoff et al. 2018, Sakthivadivel 2022, Reginatto 1998 and Caticha 2019 (at 2084), and Vaswani, Tsai, Ramsauer, RoFormer, Longformer, Mistral and T5 all support the sentences that cite them. Metadata is consistent with the known records; Friston et al. 2017 was checked by search. Residual: knowledge-based except where noted.
11. Nakahara's associated-bundle convention (225): (u g, f) ~ (u, g f) is equivalent to Nakahara's (u, f) ~ (u g, g^-1 f).
12. Milnor 1976, Lemma 7.5 (1573), stating bi-invariant metric iff compact times abelian. Residual: from memory, not re-read.

## Physics-audience and standalone notes

The reference list is weighted toward ML and cognitive science. Part II's consciousness section (2086-2106) alone carries about 20 keys, including psychedelic-pharmacology sources (Swanson 2018, Millière 2018, Carhart-Harris 2014 and 2019). The transformer sections cite GPT-2, Longformer, Mistral, T5, ALiBi and three BERTology papers. A Foundations of Physics or J. Phys. A referee will read these as belonging to a different venue. Two moves serve goal 2: condense the transformer-recovery citations into one appendix paragraph, and replace the pharmacology references with a single pointer. Findings L14-2 through L14-6 add the physics primary sources such a referee expects: Wootters and Braunstein-Caves, the informational reconstructions of quantum theory, Yang-Mills and Wu-Yang, van Enter-Fernández-Sokal, Machta et al., and Kikuchi. That shifts the balance at little cost in length.

At 380 the phrase "left-conjugation at the source and right-conjugation at the target" describes g_i Omega g_j^-1. That is left and right multiplication, not conjugation, and a gauge theorist will flag the wording. Physics venues generally expect DOIs (L14-12). `unsrt` is acceptable for Springer journals; a revtex or iopart target needs a style change. No citation to Hoffmann et al. (Chinchilla) is needed, since the WikiText section already disclaims scaling-law claims. For a physics venue that section is a candidate for supplementary material.

## Complementarity notes

The Theory's related work (`Theory/c15_related_work.tex`) already cites `SingerWu2012`, `HansenGhrist2019`, `HansenGhrist2021Discourse`, `cohen2019gauge`, `He2021GaugeEquivariantTransformer`, `BermanKlingerStapleton2023`, `villegas2023laplacian`, `beny2015information` and `MehtaSchwab2014`. PIFB2 can adopt the same set (L14-5, L14-6) and the same key for Mehta-Schwab. Where PIFB2 disclaims a Wilsonian analysis (1681) it can point forward to the Theory. Candidates are the law-level coarse-graining of `Theory/c09_coarse_channels.tex` (`\label{ch:coarsegraining}`, `\label{sec:rg-law-level-vfe}`) and, for fixed points and the relevance criterion of 3723, Supplement B `b06_wilsonian_limits.tex` (`\label{ch:wilsonian-limits}`, `\label{sec:rg-fixed-points}`). Supplement B's spatial and lattice RG (`b07_lattice_rg.tex`, `\label{ch:constructive-spatial-rg}`) is base-transport content and should be cited as deferred work, not summarized. None of this needs a Theory change.

## Not covered

- Pin-cites not checked against the page: Wilson 1974 Eq. 12 and Creutz ch. 5 Eq. 5.1 (385); Lauritzen §3.2 and Wainwright-Jordan Prop. 4.1 (3265); Milnor Lemma 7.5 (from memory only).
- Attribution fidelity for the philosophy, consciousness, holography and quantum-reference-frame citations (75, 130, 198, 1767, 1800, 2091-2129), apart from the Wheeler, Rovelli, QBism and Caticha uses read above. Aguilera et al. 2022's characterization at 132 was not checked.
- Yedidia et al. 2005's non-monotonicity statement (3490) was not re-read.
- Metadata for the 100-plus non-load-bearing entries was not checked against primary records.
- The three quantum-reconstruction references proposed in L14-3 and Wu-Yang 1975 are given from known records without online verification.
