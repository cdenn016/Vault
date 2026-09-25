# Findings digest for GLOBAL

[L01-gauge] ### L01-6: RoPE is attributed to the wrong structural property
**Location:** PIFB2.tex:1274-1280 (eq:rope_apply and following)  1131-1132.
**Severity:** medium
**Evidence:** The identity $R(\theta_m)^\top R(\theta_n)=R(\theta_{n-m})$ checks (`L01_rope_heads.py` P1  $1.1\times10^{-16}$). The paper then says the relative-position property "is specific to the abelian rotation sector" and that "a non-abelian $\mathrm{GL}(d_k)$ lift ... loses the exact $f(i-j)$ dependence." The actual condition is that the position frames form a one-parameter subgroup  $U_m=\exp(mX)$  i.e. a homomorphism from the translation group into $G$; then $U_m^{-1}U_n=U_{n-m}$ for any $X\in\mathfrak{gl}(d_k)$  however non-normal. Executed with a random $X\in\mathfrak{gl}(4)$  $|[X X^\top]|=5.7$ (P2): residual $7.7\times10^{-12}$  and kernels at $(0 3)$ and $(4 7)$ agree to $1.8\times10^{-10}$. Abelianness is not sufficient: an $\mathrm{SO}(2)$ frame with phase $\sqrt{m+1}$ fails (P3  discrepancy 0.29). Compactness is not needed. Commuting generators are required only for multi-dimensional positions (P4  noncommuting two-dimensional generators: discrepancy 69.7). In gauge language RoPE is a translation-invariant flat connection on the position lattice  link $U_{m+1}U_m^{-1}=\exp X$ constant. Also $R_i^\top R_j=U_i^{-1}U_j$ is the right-convention transporter $h$ of L01-3; it equals $\Omega_{ij}^{-1}$ only in the abelian case  as the paper notes.
**Fix:** Replace the last three sentences of the RoPE paragraph with: "The relative-position form holds exactly when the frames are a one-parameter subgroup $U_m=\exp(mX)$  for any generator $X\in\mathfrak{gl}(d_k)$; RoPE is the compact block-diagonal choice  and multi-dimensional positions additionally require commuting generators. Equivalently  RoPE is a translation-invariant flat connection on the position lattice."
**Falsifies:** A generator $X$ with $\exp(-mX)\exp(nX)\neq\exp((n-m)X)$  which is impossible since $mX$ and $nX$ commute.
**Status:** The RoPE identity is P; the "abelian sector" explanation is incorrect.

[L01-gauge] ### L01-7: The trivial-frame route has residual symmetry Stab$(M_h)$  not $\mathrm{GL}(d_{\mathrm{head}})$  and Vaswani heads are not block-diagonal
**Location:** PIFB2.tex:1086  1210 ("its only gauge content is the block-diagonal restriction")  1266-1272 (eq:multihead_gauge_group).
**Severity:** medium
**Evidence:** Under the belief action $\mu\mapsto g\mu$ on both query and key sides  a fixed learned $M_h$ is invariant only if $g^\top M_hg=M_h$. Executed (P5): for a generic $M$  the stabilizer algebra has dimension 1  1  2  3 for $k=2 3 4 6$ (that is $\lfloor k/2\rfloor$)  against $k^2$ for $\mathfrak{gl}(k)$; for the symmetric part it is $\mathfrak{so}(k)$  dimension $k(k-1)/2$. The $\mathrm{GL}(d_{\mathrm{head}})$ that does survive in standard attention is the factorization redundancy $(A_Q A_K)\mapsto(A_QG A_KG^{-\top})$ of 1212  which acts contragrediently on queries and keys  not by the fundamental action on a belief. Separately  Vaswani heads apply $W_Q^h\in\mathbb R^{d_{\mathrm{model}}\times d_{\mathrm{head}}}$ to the full embedding (P6: all 6 of 6 rows populated)  so the "partition of the embedding dimension" and "no cross-head mixing under transport" at 1267 describe the gauge-VFE architecture  not Vaswani et al.
**Fix:** At 1210 say that (R3) introduces a fixed fiber tensor that breaks the belief gauge group to Stab$(M_h)$; at 1267 attribute the block-diagonal structure to the gauge-VFE architecture and identify the standard-attention $\mathrm{GL}(d_{\mathrm{head}})^H$ as the factorization redundancy.
**Falsifies:** A transformation law under which $M_h$ transforms (for example $M_h\mapsto g^{-\top}M_hg^{-1}$ as a field)  which the paper does not state.
**Status:** eq:multihead_gauge_group as a subgroup statement is P; its identification as the symmetry of the recovered attention is incorrect.

[L02-geometry] ### L02-9: Absolute value is not an admissible positive map for the Cholesky diagonal
**Location:** PIFB2.tex:2660.
**Severity:** low
**Evidence:** Line 2660 says "reparameterizing the diagonal through a positive map (softplus or absolute value) so that ... the realized diagonal entries cannot cross zero", and later "the map `L -> LL^T` is a diffeomorphism onto the SPD cone, so ... share stationary points". Softplus is a diffeomorphism from R onto the positive half-line, so both claims hold for it. The absolute value vanishes at 0, so `Sigma` can become singular. It is not differentiable at 0, and it is two-to-one, so the stored-parameter-to-SPD map is not a diffeomorphism. Stationary points of the parameter objective then include `Sigma` on the boundary, and duplicate interior points.
**Fix:** Drop "or absolute value", or state that the stationarity equivalence holds only for a diffeomorphic positive map such as softplus or exp.
**Falsifies:** A demonstration that the implementation never reaches zero there, which would still leave the diffeomorphism claim false.
**Status:** D, a minor misstatement.

[L08-transformer] ### L08-2: Hypothesis (N) as stated in Theorem `thm:transformer_recovery` does not remove the bias the proof actually produces
**Location:** PIFB2.tex:1144 (hypothesis (N)), 1172-1188 (key-bias analysis), 1226 ("Under hypothesis (N) in its exact pre-projection form").
**Severity:** medium
**Evidence:** Under (R1)-(R3) the surviving key term is $-\|\mu_j\|^2/(2\sigma^2)$ on the raw means (1164-1170; recomputed, query-norm cancellation residual 1.1e-16). The theorem's (N) reads "$\|K_j\|$ is constant in $j$", with $K_j=\mu_j^\top W_K$ (1146). The two conditions differ whenever $W_K$ is not a scaled orthogonal matrix. In `L08_kl_expansion.py` (e), keys with $\|K_j\|=1$ for all $j$ (spread 2.2e-15) and $\|\mu_j\|$ spread 34.4 give $\max_j|\beta^{\mathrm{model}}_{ij}-\beta^{\mathrm{Vaswani}}_{ij}|=0.997$; with $\|\mu_j\|$ constant the difference is 1.1e-16. The proof concedes that post-projection normalization works "along the present route only when the Gaussian beliefs are taken over the projected key coordinates" (1183) and then invokes (N) "in its exact pre-projection form" (1226), which is not the form stated in the theorem.
**Fix:** Restate (N) as "$\|\mu_j\|$ is constant in $j$ (for example, exact pre-projection normalization without a learned gain), or the residual $-\|\mu_j\|^2/2\sigma^2$ is absorbed into a learned per-key bias." Alternatively, put the query and key maps inside the divergence, as the Theory's comparison maps $S^Q_{\mathrm{ref}},S^K_{\mathrm{ref}}$ do (`cor:obs-selective-softmax`, `eq:obs-selective-dot-product`). On that route the bias is the whitened projected key norm, the current wording of (N) becomes correct, and (R3) becomes a choice of comparison record instead of a replacement of the cross term.
**Falsifies:** A reading under which $K_j$ in (N) denotes the unprojected mean, or a hypothesis elsewhere in the theorem that forces $W_K$ to be scaled orthogonal.
**Status:** P claimed ("proving Theorem"), but the stated hypotheses do not entail the conclusion; the corrected statement is P.

[L08-transformer] ### L08-6: At a point in Regime I every frame is pure gauge, so "gauge-fixed", the untied route, and RoPE-as-gauge-frame need a gauge-invariant restatement for a physics referee
**Location:** PIFB2.tex:1008 ("gauge-fixed"), 1098-1135 (untied route: "retains $\Omega_{ij}=U_iU_j^{-1}$ non-trivially", "$M_{ij}$ ranges over all of $\mathrm{GL}(d_k)$", "genuinely untied"), 1274-1280 (RoPE), 1771.
**Severity:** medium
**Evidence:** The manuscript's own KL invariance gives $\mathrm{KL}(q_i\|\Omega_{ij}q_j)=\mathrm{KL}(\mathcal N(x_i,P_i)\|\mathcal N(x_j,P_j))$ with $x=U^{-1}\mu$ and $P=U^{-1}\Sigma U^{-\top}$ (residual 2.7e-10), and the untied objects are $H_j=P_j^{-1}$ and $k_j=P_j^{-1}x_j$ (residuals 2.1e-15, 1.0e-15). In gauge-invariant variables the transport is the identity, the query-key bilinear is the SPD precision $P_j^{-1}$, and the untiedness comes entirely from the key covariance. The $\mathrm{GL}(d_k)$ range of $M_{ij}$ (1126) is a property of writing the same bilinear against local-frame means, that is, of a gauge choice. (R2) is correctly called gauge fixing only because Regime I at a point is flat, so the per-agent gauge $h_i=UU_i^{-1}$ sets $\Omega_{ij}=I$. For RoPE the transport is a constant $\mathrm{U}(1)^{d_k/2}$ potential on a one-dimensional lattice, which has no plaquettes and is pure gauge. Its physical content is that the content vector (and, in the implementation, the token priors) are held position-independent in the local frame, so the frame field acts as a fixed background section, not a dynamical gauge field. The manuscript's treatment of explicit symmetry breaking (735-928) is the natural home for this reading.
**Fix:** Add one paragraph at the start of `sec:untied_qk`: "In Regime I at a single point the frames are pure gauge, and by the KL invariance theorem the attention depends only on the common-frame data $(x_i,P_i)$ with trivial transport. The frame dependence below is therefore a statement about which quantities the model holds fixed in local frames (content means, token priors), that is, about an explicit background section rather than a dynamical gauge field. In common-frame variables $Q_i=x_i$ and $K_j=P_j^{-1}x_j$." Recast "RoPE is the position-dependent gauge specialization" as "RoPE is a constant pure-gauge $\mathrm{U}(1)^{d_k/2}$ background on the token chain."
**Falsifies:** A gauge-invariant quantity at a single point in Regime I (a holonomy, an invariant of $(x_i,P_i)$) that depends on the $U_i$ beyond the common-frame beliefs.
**Status:** D algebra, S interpretation; "captures the rotary positional structure" and "genuinely untied" inflate a parameterization statement into structure.

[L08-transformer] ### L08-7: RoPE paragraph: inconsistent sign convention and a too-narrow statement of when the relative-position property holds
**Location:** PIFB2.tex:1131-1135 (untied-route rotary identification), 1274-1280 (RoPE paragraph).
**Severity:** low
**Evidence:** The untied route gives $Q_i=U_i^\top\mu_i$, which matches Su et al.'s $R_{\Theta,m}W_qx_m$ (Eq. 16) only for $U_i=R(\theta_i)^{-1}$; the RoPE paragraph sets $U_i=R(\theta_i)$. With $U_i=R(\theta_i)$ the KL cross term is $\mu_i^\top R_{i-j}\mu_j$ (residual 2.2e-16), the transpose of the RoPE kernel $R_{j-i}$ (difference 0.335 on a random draw). Both are relative, so nothing breaks, but the two paragraphs use opposite identifications. Second, "the relative-position-only property is therefore specific to the abelian rotation sector" is too narrow for the gauge-KL score. With $U_m=\exp(mA)$ for any $A\in\mathfrak{gl}(d_k)$, including non-antisymmetric (noncompact) $A$, and a position-independent $C$, the full energy is relative: $E(3,1)-E(6,4)=-1.1\times10^{-12}$, while non-commuting frames give 3009. Orthogonality is forced only in the dot-product form, where $R_m^\top R_n=R_{n-m}$ at $m=n$ gives $R_m^\top R_m=I$. Linearity of $\phi_m$ in $m$ is also required and is not stated.
**Fix:** Write $U_i=R(\theta_i)^{-1}$ in both places (or note the frequency sign flip once), and replace the sentence by: "The relative-position property of the gauge score requires the position-to-frame map to be a one-parameter subgroup, $U_m=\exp(mA)$; in the transported-KL score $A$ may be any element of $\mathfrak{gl}(d_k)$, while the dot-product form additionally requires $A^\top=-A$."
**Falsifies:** An $A\in\mathfrak{gl}(d_k)$, not antisymmetric, for which the transported KL with fixed $C$ fails to depend only on $i-j$.
**Status:** D; minor imprecision.

[L09-empirical] ### L09-7: The computational-details paragraph mixes two codebases and cannot apply to the only reported experiment
**Location:** PIFB2.tex:2185.
**Severity:** low
**Evidence:** "The run entry point synchronizes the Python standard-library, NumPy, PyTorch, and CUDA random-number-generator seeds, enables deterministic cuDNN mode" does not say which entry point, MAgent or vfe3. The paragraph then ends "The recoverable scaling artifact does not identify the original training environment, hardware, seed identities, or per-run hyperparameters". The seed-control description therefore describes current code, not the sweep. The sentence on the error of the abelian approximation is appropriately hedged.
**Fix:** Prefix the seed paragraph with "In the current MAgent_Model code (commit X)" and state explicitly that it is not known to describe the sweep runs.
**Falsifies:** Evidence that the sweep ran from the entry point described.
**Status:** E (code description), with ambiguous scope.

[L09-empirical] ### L09-8: Figure and notation mismatches in the sweep
**Location:** PIFB2.tex:1316-1321 (`fig:scaling_main`) and 61.
**Severity:** low
**Evidence:** The rendered figure has the axis label "Belief dimension K", while the text uses $K_q$ and the abstract says "embedding dimensions". The x-axis has ticks only at 10, 30, 50, 70, 90, and 120, so the K_q = 20, 40, 60, 80, and 100 points sit at unlabeled positions, and the 90-to-120 gap hides where the 100 point is. The error bars are SDs over n = 2 or 3, which a reader may take for standard errors unless they read the caption closely (the caption does say SD).
**Fix:** Label the axis "$K_q$" with a tick at every sampled value, and use one name ("belief dimension $K_q$") throughout.
**Falsifies:** Not applicable (presentation).
**Status:** Presentation.

## Verified, no defect

- **The aggregate fit reproduces exactly.** Method: means and SDs reconstructed from the PDF vector stream, then `scipy.optimize.curve_fit` of PPL = a K^b + c. The result, a = 1805.5529, b = -1.048919, c = 61.1699, R^2 = 0.99981995, matches lines 1310-1313 and 2180 to every printed digit. Residual: calibration error of 6e-7 PPL. Script: `L09_scaling_recon.py`.
- **PPL at K_q = 120 is 72.71.** The reconstructed value is 72.708 (line 1323). Same script.
- **Run counts.** Ten points at n = 3 plus K_q = 90 at n = 2 gives 32 runs, consistent across the abstract, the text, the caption, and the figure annotation. Method: arithmetic.
- **Degrees of freedom of the historical test.** With 11 aggregate means, 3 parameters, and 1 restriction, the test is F(1,8), and p(F >= 9.73) = 0.01424. The reconstruction gives F = 9.727, p = 0.0143. Script: `L09_scaling_recon.py`. Residual: none, but the value is not in the current bytes (see L09-3).
- **Token arithmetic at line 126.** 30,000 x 4,096 = 60,000 x 2,048 = 22,500 x 5,461.33 = 122,880,000. Script: `L09_scaling_recon.py`. Residual: the underlying per-row compute field could not be inspected because the CSV is absent.
- **Retired Ouroboros run numbers are absent.** A grep of the current bytes finds no "173", no 13-scale run, and no single-seed emergence figure. Lines 108, 122, 1734, 2164, and 2200 consistently say that no historical emergence trajectory is analyzed. The retrospective emergence claim of earlier versions has been removed, and the current text is consistent with fence F2. Method: grep. Residual: none.
- **No "deferred release" promise.** The Data and Code statements promise nothing beyond the named aggregate artifacts, and no claim in the manuscript depends on unreleased raw runs. The defect is that the named artifacts themselves are missing (L09-1), not an inconsistency with deferred releases. Method: grep, plus reading 2197-2204.
- **The non-equilibrium statement at 1729 is hedged correctly as written.** It rests on convergence to stationary points by the Lojasiewicz inequality under real-analyticity and precompact orbits, with observation injection as the only exogenous drive. The cited source (`absil2005convergence`: Absil, Mahony and Andrews 2005, SIAM J. Optim. 16) is the standard reference for this result, but I did not open the primary source in this session. Status: not re-verified.

## Physics-audience and standalone notes

The manuscript itself says that the language-model experiments "test the architecture and not the participatory reading" (line 102). The thesis of the paper is a formal realization of the participatory "it from bit" of Wheeler, so for a physics referee the WikiText-103 sweep carries no evidential weight for that thesis. The abstract spends four sentences on fit coefficients (a to four decimals, b to six, R^2 to five), which will read as belonging to a machine-learning venue.

I recommend three cuts. First, reduce the sweep sentences of the abstract to one clause: "the general architecture trains as a working language model; its descriptive behavior is reported in the companion". Second, reduce Section `sec:scaling_validation` to two or three sentences in the Discussion, or to a short appendix carrying the eleven-row table. Third, cite the ML companion that owns these runs (the GL(K) attention manuscript in `Research/manuscripts`, or the vfe3 paper) for the full sweep, the schedule confound, and the statistics of L09-3.

If the section is kept, a physicist will need perplexity defined (L09-5) and will expect a fitted exponent reported with an uncertainty and no more than two significant figures. That reader will also ask why a power law with offset is the model. Nothing in the manuscript predicts the functional form or the exponent, so the fit is a phenomenological summary and should be called one.

"Iso-token", "optimizer step", "batch", "layer normalization", "output projection", "MLP", and "activation" are undefined for this audience. If the section is condensed, all of them can go. The keyword "Transformer architectures" (line 66) signals the wrong venue for the stated goal of the paper.

The prospective protocol (1732-1750 and 2162-2172) is also unusual for a physics journal: it is a two-page statement, written twice, of an experiment not yet run. The standalone reader would be better served by one paragraph naming the predicted observable (persistent multi-child clusters under an active, untied slow channel) and its refutation, with the operational details in supplementary material.

## Complementarity notes

The Theory has no empirical content: `ca_numerical_index.tex` (`tab:numerical-index`) states that no main-manuscript statement has NUMERICAL status. The sweep and protocol of PIFB2 are therefore the only empirical material in the pair. They belong naturally to the ML companion and to a MAgent simulation paper rather than to either theory document.

The prospective protocol tests the discrete detector and barycenter of PIFB2. The successor construction in the Theory is the normalized marked parent (`c13_formation.tex`: `sec:rg-formation-parents`, `eq:rg-formation-marked-channel`, `eq:rg-formation-parent-vfe`). PIFB2 should say which of the two a future run would validate. If the pair adopts the crosswalk framing, PIFB2 should also point to the formation chapter of the Theory (`ch:finite-depth-formation`) as the rigorous version of what the protocol would probe. No Theory change is needed.

## Not covered

Several code-level claims in my scope require the MAgent_Model repository: `max_scales=25` for the historical preset and `max_scales=5` for the active CONFIG (line 1709), and the function and file references `gauge_agent/full_vfe.py::hyperprior_term`, `ouroboros.py::_propagate_hyperpriors`, `agents.py`, `dynamics.py`, and `lie_groups.py` (lines 1711 and 2185). That repository is not present on this host (neither on the Desktop nor in `D:/Codebases_9-24-2026`), so these claims were not checked. The LLM-assistance statement (2189) was not checked against any record. The non-equilibrium score definitions at 1729 were read but not tested, and the Lojasiewicz citation was not opened.

[L14-citations-a] ### L14-11: "Standard active inference arrives at natural-gradient descent" is cited only to Amari
**Location:** PIFB2.tex:1761.
**Severity:** low.
**Evidence:** Amari 1998 defines natural gradient. The claim that active-inference belief updates are natural-gradient descent comes from Da Costa, Parr, Sengupta and Friston, Entropy 23, 454 (2021), which the Crossref record says shows the dynamics "approximate natural gradient descent". Friston 2017 describes plain gradient descent.
**Fix:** "…the route by which neuronal dynamics under active inference approximate first-order natural-gradient descent [DaCosta2021], an intrinsic Riemannian gradient flow in the sense of Amari [Amari1998]…"
**Falsifies:** A standard-AIF source stating an exact natural-gradient scheme.
**Status:** S/E in the source. Slightly inflated ("arrives at").

[L15-citations-b] ### L15-8: Rovelli's relational quantum mechanics is described as relativizing states "to observers"; its defining move is that states are relative to any physical system
**Location:** PIFB2.tex:1767.
**Severity:** low
**Evidence:** The Rovelli 1996 abstract (quant-ph/9609002) says the theory describes "only the information that systems have about each other", and the paper denies any observer-observed distinction. For a foundations audience, "relative to observers" suggests the observer-privileging reading RQM rejects. It also misses a point in PIFB2's favor: RQM is itself an informational, it-from-bit-like theory.
**Fix:** "Rovelli's relational quantum mechanics [Rovelli1996] holds that quantum states, and the values of variables, are relative to other physical systems, any system serving as an observer, and describes only the information systems have about each other."
**Falsifies:** Not applicable; the abstract quotation settles it.
**Status:** S.

[L15-citations-b] ### L15-10: Minor attribution and metadata items
**Location:** various.
**Severity:** low
**Evidence and fixes:**
(a) At 3902, "canonical Pinsker constant $1/\sqrt2$ [CoverThomas2006]" is right for total variation ($\mathrm{TV} \le \sqrt{\mathrm{KL}/2}$, script `L15_pinsker.py`: supremum ratio 0.7071064 against 0.7071068, tight at $p=1/2$). Cover and Thomas state Pinsker in the $L^1$ form ($\|P-Q\|_1 \le \sqrt{2 \mathrm{KL}}$ in nats, supremum ratio 1.4142128), so name the norm: "Pinsker's inequality in total-variation form". Pointer to the result: Cover and Thomas, Lemma 11.6.1 (verify).
(b) At 2105, Tononi2004 and Dehaene2014 are cited for integrating modalities "through free-energy minimization". Neither IIT nor global workspace theory uses free-energy minimization. Move the citations before "through".
(c) At 130, "Swingle ... and others show that tensor-network states model the AdS/CFT correspondence" inflates a proposal (MERA as discretized AdS). Use "propose".
(d) At 86, Umegaki relative entropy is named without a citation (Umegaki, Kodai Math. Sem. Rep. 14, 59, 1962, verify). At 2142, the Petz family is correctly attributed [Petz1996]. Its minimal member, the Bures-Uhlmann metric, has a bib entry `Uhlmann1976` that is never cited; add it there. Shannon entropy is named at 1729 and 2992 while `Shannon1948` sits in the bib uncited.
(e) The title (45) and the Wheeler quotations at 75 use straight ASCII double quotes. Under `inputenc` with the default font encoding, a straight `"` typesets as a closing quote on both sides, so "It From Bit" and "How come existence?" print with backward opening quotes. Use ``` `` ''' as the rest of the file does (for example 1830, 1872).
(f) `Wheeler1990` is correct: the chapter starts on p. 3 of Zurek's volume (SFI press listing), and the bib gives 3-28. Add `series = {Santa Fe Institute Studies in the Sciences of Complexity}, volume = {VIII}`. The research wiki's source note `wheeler-1990-it-from-bit.md` gives pp. 309-336, which are the page numbers of the 1999 reprint in *Feynman and Computation* (ed. Hey, Perseus), per Fuchs 2017's reference [105]. That is a wiki error, not a PIFB2 error; I offer it for wiki correction and have not edited the vault. The same Fuchs reference list confirms the `Wheeler1983` pagination (Princeton UP 1983, pp. 182-213, ref. [79]).
(g) "In 1990 John Archibald Wheeler asked "How come existence?"" is accurate for the cited publication; the search result confirms the abstract frames the essay around that question. The talk was given in 1989 (Tokyo and Santa Fe), and Wheeler had posed the question before that. "In 1989-1990" or "In his 1990 essay" is safer.
(h) The `Chalmers2016` editor field holds a raw UTF-8 "ü" (Brüntrup). It is valid UTF-8, but classic BibTeX tolerates it poorly; use `Br{\"u}ntrup`.
**Falsifies:** Per item.
**Status:** Not applicable.

## Verified, no defect

The following attributions were checked. For each I give the PIFB2 wording in brief, the method, and the residual (what I did not check).

- **Wheeler1990** metadata (Zurek ed., Addison-Wesley 1990, chapter from p. 3). PIFB2:75, 1767, 1835, 1872. Method: web (SFI volume listing; Fuchs 2017 reference list for the other two printings). Residual: the end page 28 was not seen on a scan.
- **Wheeler1983** "Law without law", Wheeler and Zurek eds., Princeton UP 1983, pp. 182-213. PIFB2:75, 1705, 1767. Method: Fuchs 2017 ref. [79]. The paraphrase at 1767 ("dynamical laws arise") matches the "law without law" passage Fuchs quotes ("The laws must have come into being"). Residual: 1705's attribution of the feedback or self-excited-circuit figure to the 1983 text is from memory (L12's scope).
- **Fuchs2014** (AJP 82, 749), **DeBrotaFuchsSchack2020** (Found. Phys. 50, 1859), **Brukner2018** (Entropy 20, 350), **frauchiger2018quantum** (Nat. Commun. 9, 3711), **AdlamRovelli2022** (Phil. Phys. 1, 4, 2023). Metadata and use at 1767 and 2042 are consistent with the works as known. Method: bib inspection plus Fuchs 2017 text. Residual: the DeBrota paper was not re-read.
- **Rovelli1996** metadata (IJTP 35, 1637). Method: arXiv abstract. See L15-8 for the wording.
- **PageWootters1983** (PRD 27, 2885), "entangled clock subsystem". Characterization correct. Method: bib and standard content.
- **ConnesRovelli1994** metadata correct (CQG 11, 2899). The characterization is defective (L15-3).
- **VanRaamsdonk2010** (GRG 42, 2323), **MaldacenaSusskind2013** (Fortschr. Phys. 61, 781), **Swingle2012** (PRD 86, 065007), **Jacobson1995** (PRL 75, 1260; "derived Einstein's field equations from the thermodynamics of local causal horizons" is accurate), **Padmanabhan2010** (Rep. Prog. Phys. 73, 046901), **Verlinde2011** (JHEP 04 (2011) 029), **Zurek2003** (RMP 75, 715; "environment-induced superselection" correct), **Bousso2002**, **Maldacena1999** (ATMP 2, 231, 1998), **Cao2017**, **Deutsch2015**. Metadata and one-line characterizations are acceptable, apart from L15-10(c). Method: bib inspection against known publication data. Residual: no page-level re-reading.
- **Tononi2008** (Biol. Bull. 215, 216), **Tononi2016** (Nat. Rev. Neurosci. 17, 450), **Tononi2004**, **Tononi2015**, **Chalmers1995** (JCS 2, 200; hard problem), **Chalmers1996**, **Chalmers2013consciousness** (Alter and Nagasawa eds., OUP 2015, pp. 246-276, noted as circulated 2013), **Chalmers2016** (Brüntrup and Jaskolla eds., OUP 2016, pp. 179-214). The panprotopsychism labels at 2101 match Chalmers's taxonomy. **Strawson2006**, **Russell1927**, **Goff2017**. Method: bib inspection; taxonomy from the wiki source notes `chalmers-2013-panpsychism.md` and `chalmers-2016-combination-problem.md`. Residual: page-level quotations not checked, and none are quoted.
- **Seth2021** (Faber and Faber 2021), **Clark2016** (OUP 2016), **Hoffman2019** (Norton 2019). "Controlled hallucination" and "selected for fitness rather than veridicality" are faithful summaries. Method: bib and known content.
- **LahavNeemeh2022** (Front. Psychol. 12, 704270, doi 10.3389/fpsyg.2021.704270) and **LahavNeemeh2025** (arXiv:2502.07247, "shortened version"). The claim at 81 and 2091, that they write the inter-frame law only for functionally identical systems, is supported: the transformation is developed for the equivalent Alice/ALICE pair, and the paper says "Different dynamics means different cognitive frames of reference" without supplying the law between them. Method: web (Frontiers full text; arXiv abstract) and the wiki note. Residual: I did not see the delta-function display myself.
- **Kant1781** (Guyer and Wood translation, CUP 1998), with space and time as forms of intuition. **Helmholtz1867** (Handbuch, Voss), unconscious inference. **Whitehead1929** (corrected edition 1978), extensive continuum. **Cassirer1923**, **Worrall1989** (Dialectica 43, 99; epistemic SR), **Ladyman2007** (metadata correct; see L15-9), **Friedman2001**, **Nagel1986**, **Wigner1960**, **Bateson1972** ("a difference which makes a difference"), **Kretschmann1917**, **Norton1993** (the Kretschmann summary is accurate; see L15-6 for the tail). Method: bib and standard content.
- **CoverThomas2006** (2nd ed.) metadata correct. The uses at 1830 and 3902 are covered in L15-3 and L15-10(a). Script `L15_pinsker.py`, residual $4\times10^{-7}$ (sampling).
- **Petz1996** (LAA 244, 81), monotone metrics. Attribution at 2142 correct.
- **Cencov1982** plus **AyJostLeSchwachhofer2017**. The attribution at 178 (finite sample spaces, then the parametric extension) is correct.
- **giacomini2019qrf** (Nat. Commun. 10, 494; frame-relativity of entanglement), **BartlettRudolphSpekkens2007** (RMP 79, 555), **Vanrietvelde2020** (Quantum 4, 225), **DonnellyFreidel2016**. Used correctly at 198 as precedents, explicitly "motivation rather than proof".
- **Fuchs2017** metadata (Durham and Rickles eds., Springer 2017, pp. 113-134) is consistent with the arXiv version. Its engagement is inadequate (L15-1).
- **Caticha2019** (Entropy 21, 943), **reginatto1998derivation** (PRA 58, 1775; the Fisher term added to Hamilton-Jacobi gives Schrödinger, correctly summarized), **frieden1998physics** (CUP 1998).
- The clock-dissipation identity at 1840: $(d\tau/dt)^2 = \eta(-d\mathcal{F}/dt)$ holds exactly (residual 0.0), $\Delta I = (\eta/2)|\Delta\mathcal{F}|$ holds to leading order with relative error $O(\eta)$, and the Gaussian mean-step KL equals $\tfrac12\delta\mu^\top\Lambda\delta\mu$ exactly (residual 0.0). Script `L15_clock_identity.py` (random SPD metric, $n=4$). Ledger candidate. Residual: checked only for the quadratic-$\mathcal{F}$ discrete case.
- Bib hygiene: no duplicate keys and no case collisions among the 493 entries (`L15_cite_extract.py`). There are 3 undefined keys (L15-5).

## Missing-citation table (ranked by how likely a physics referee is to demand each)

"In bib" means present in `Research/manuscripts/references.bib`. "Cited" means cited in PIFB2.

| Rank | Work | PIFB2 site | Why a physics referee would demand it | In bib / cited |
|---|---|---|---|---|
| 1 | Hawking, King, McCarthy, J. Math. Phys. 17, 174 (1976); Malament, J. Math. Phys. 18, 1399 (1977) (verify) | 1979 | The "fixes $g$ only up to a conformal factor" statement is their theorem | no / no |
| 2 | Informational reconstructions: Zeilinger, Found. Phys. 29, 631 (1999); Hardy, quant-ph/0101012; Chiribella-D'Ariano-Perinotti, PRA 84, 012311 (2011); Masanes-Müller, NJP 13, 063001 (2011) (verify); Höhn, Quantum 1, 38 (2017) (verified) | 81, 102, 134 | These are the physics formalizations of it-from-bit; "remained a slogan" cannot stand without them | no / no |
| 3 | Fuchs, "On participatory realism" (2017) | 1767, 81 | Claims Wheeler's participatory program for QBism; PIFB2's central competitor | yes / cited only as a tag |
| 4 | Caticha, "Entropic dynamics, time and quantum theory", J. Phys. A 44, 225303 (2011) (verified) | 1835 | Closest precedent for time as information bookkeeping with an arrow | no / no |
| 5 | Caticha, "The information geometry of space and time", AIP Conf. Proc. 803, 355 (2006); "The information geometry of space-time", arXiv:1909.09657 (both verified) | 1872, 1979 | Earlier proposal of physical space (and spacetime) as Fisher geometry; same positive-definite-space-plus-evolution structure as P5 | no / no |
| 6 | Wootters, "Statistical distance and Hilbert space", PRD 23, 357 (1981) (verify) | 1830 | Operational source of distinguishability as distance; a Wheeler-school result | no / no |
| 7 | Salamon-Berry, PRL 51, 1127 (1983); Crooks, PRL 99, 100602 (2007) (verify); Ito, PRL 121, 030605 (2018) (verified) | 1840 | The clock-dissipation identity is the natural-gradient analog of thermodynamic length and Fisher-speed relations | no / no |
| 8 | Zurek, "Quantum Darwinism", Nature Phys. 5, 181 (2009) (verify) | 2078, 2084 | Standard physics account of objectivity by consensus of many observers | no / no |
| 9 | Carlip, "Challenges for emergent gravity" (2014) | 2072 | Obstructions any emergent-gravity reading must meet | yes / no |
| 10 | Erdmenger, Grosvenor, Jefferson, SciPost Phys. 8, 073 (2020) (verified); Matsueda, arXiv:1310.1831 (verified) | 1872-1893 | Fisher geometry and emergent spacetime in physics; AdS genericity warns against over-reading the hyperbolic Gaussian metric | no / no |
| 11 | Müller, "Law without law", Quantum 4, 301 (2020) (verified) | 1767, 2042, 2129 | Observer-first derivation of emergent objective reality, named after Wheeler | no / no |
| 12 | Bombelli, Lee, Meyer, Sorkin, PRL 59, 521 (1987) (verify) | 1980 | Supplies the conformal scale PIFB2 lists as open | no / no |
| 13 | Greensite, Phys. Lett. B 300, 34 (1993) (verified) | 1894-1900 | Prior work on dynamical selection of Lorentzian signature, singling out D = 4 | no / no |
| 14 | Lavis and Streater, Stud. Hist. Phil. Mod. Phys. 33, 327 (2002) (verified); Frieden, *Science from Fisher Information* (CUP 2004) | 2084 | The standard critique behind the stance PIFB2 takes on Frieden | no / no |
| 15 | Höhn, Smith, Lock, PRD 104, 066001 (2021) (verify) | 1835 | Unifies Page-Wootters with relational and QRF dynamics | no / no |
| 16 | Barbour and Bertotti, Proc. R. Soc. A 382, 295 (1982); Barbour, CQG 11, 2853 (1994) (verify) | 1828-1835 | Time abstracted from change. Best matching (minimizing a discrepancy over a group action) is structurally close to frame alignment by minimizing $\mathrm{KL}(q_i\|\Omega_{ij}q_j)$ (analogy, S) | no / no |
| 17 | Brody and Hughston, J. Geom. Phys. 38, 19 (2001); Goyal, PRA 78, 052120 (2008) (verify) | 2142 (C5), 1894 (complexification) | Geometric QM and information-geometric reconstruction: the tools the density-operator fiber and the GL($K_q$,C) route would need | no / no |
| 18 | Lieb and Robinson, Commun. Math. Phys. 28, 251 (1972) (verify) | 1979-1980 | Standard emergent finite speed from local dynamics; bears on the parabolic-flow tension | no / no |
| 19 | Anandan and Aharonov, PRL 65, 1697 (1990); Braunstein and Caves, PRL 72, 3439 (1994) (verify) | 1840 | Time and evolution speed as Fubini-Study or Fisher arc length in quantum physics | no / no |
| 20 | Giacomini et al. 2019; Bartlett, Rudolph, Spekkens 2007 | 1767, 2042 | Already cited at 198. Also cite where agents are said to be comparable only after transport, since QRFs are the physics model of that | yes / yes (198 only) |
| 21 | Ladyman 1998; French and Ladyman 2003; Floridi 2008 (verify) | 1800, 79 | Origin of OSR; nearest named informational structuralism | no / no |
| 22 | Umegaki 1962; Uhlmann 1976 | 86, 2142 | Primary sources for quantum relative entropy and the Bures-Uhlmann metric | Uhlmann yes / no |
| 23 | Deutsch, "It from qubit" (2004, in *Science and Ultimate Reality*, CUP) (verify) | 75 | The standard quantum update of Wheeler's slogan | no / no |

## Physics-audience and standalone notes

The reference list is thin at exactly the points where physicists will look hardest, and full where they will look least. Part II's physical claims, Lorentzian signature (1894-2014), gravity (2072-2076), and the causal cone, carry almost no physics citations. Meanwhile the consciousness section (2086-2106) cites fifteen or more philosophy and neuroscience works (Bayne, Cleeremans, Dehaene, Carhart-Harris, Millière, Swanson, Goff, Strawson, and others). For a foundations-of-physics venue, I recommend compressing 2086-2106 to one paragraph that keeps Chalmers1995, Chalmers2013consciousness (panprotopsychism), Tononi2016, and LahavNeemeh2022, and moving the rest to a philosophy-of-mind companion. The same reallocation should add rows 1-13 of the table to the physics sections. For the author's first goal, the paper stands alone better if the introduction's genealogy (75-81) runs Wheeler, then Wootters, then Zeilinger and Brukner, then the informational reconstructions, then QBism and RQM, then this paper. At present it runs Wheeler, Kant, Helmholtz, Friston, then spacetime emergence. A physics reader expects the first sequence, and the second reads as a cognitive-science paper borrowing physics vocabulary. Keep Kant and Helmholtz as one clause each. The keyword "Transformer architectures" and the ML and neuroscience citation cluster (Friston and coauthors, parr2022active) are not errors, but a physics editor will ask why they sit in the abstract-level keywords. "Quantum foundations" or "Relational physics" would signal the venue better.

## Complementarity notes

The Theory's interpretation chapter (`MultiAgentELBO/Theory/c14_interpretation.tex`, `\label{sec:phil-participatory}`, lines 150-160) says the participatory loop "resembles Wheeler's participatory proposal \citep{Wheeler1990} without being derived from it or evidence for it", and that "None of these separates the program from a hierarchical model with learned priors; formation could." PIFB2:1677 ("this bidirectional coupling realizes Wheeler's participatory loop") and 1727 ("This realizes the formal feedback structure of Wheeler's self-excited circuit") make the stronger verb claim. PIFB2 should adopt the Theory's calibration ("instantiates a feedback structure resembling") and may cite `sec:phil-participatory` as the rigorous statement. L12 owns the Wheeler reading; I record only the citation-status mismatch. The Theory's structural-realism citations (`c14_interpretation.tex:103-106`: Worrall1989, esfeld2008moderate, Ladyman2007, Ladyman2014) are a superset of PIFB2's and would repair part of L15-9. The Theory uses the key `DorflerBullo2013Kron` and proves the scalar-Laplacian statement with a matrix-weighted regime table (`g07_coarse_maps.tex`, `\label{sec:cg-kron}`, `\label{tab:cg-kron-regimes}`, `\label{eq:cg-kron-witness}`). PIFB2:1685, which says the matrix-weighted case "is not covered by those" references, can cite `sec:cg-kron` directly once the key is fixed (L15-5). The Theory's related-work chapter (`c15_related_work.tex`) cites no foundations-of-physics literature, so the foundations citation apparatus in the missing-citation table belongs to PIFB2. There is no conflict, and SPEC section 0 is not touched.

## Not covered

I did not audit the attribution of the gauge-theory, lattice, and RG citations (Wilson, Kogut-Susskind, Creutz, Cardy, Faddeev-Popov, Cornwall-Jackiw-Tomboulis, Abbott), the ML citations, or the active-inference and Bayesian-mechanics cluster (Friston, parr2022active, Bruineberg, Aguilera, Biehl) beyond reading 132. I did not check the Karcher-radius constant itself (L15-5 residual), or the quotation-level wording of Tononi, Chalmers, Seth, Clark, and Hoffman (PIFB2 paraphrases and does not quote them). I did not reach the consciousness-adjacent citations at 2121 beyond metadata (Carhart-Harris, Swanson, hohwy2013predictive), the body text of 136-1800 (other citations there were checked only for resolution by script), or appendices A-I apart from 3762 and 3895-3902. Wheeler's deeper reading is L12's.

[L16-notation-build] ### L16-7: Remaining single-letter collisions not declared in the notation appendix
**Location and evidence** (all from `L16_symbols.py` plus contexts):
chi: presence/support $\chi_i$ (132, 680-711); Gaussian conditional factors $\chi^{(s)}_{i,\pi(i)}$ (3175-3260); complex combination $\chi = i\psi_\tau+\psi_x$ (1960); susceptibility $\chi$ (2148) and $\chi_N$ (3937); $\chi^2$ divergence (2964, 3160).
Phi versus phi: frame $\phi_i$; Gaussian CDF $\Phi$ in GELU (1288); IIT integrated information $\Phi$ (2099); bundle morphisms $\Phi,\tilde\Phi$ (2146); $\Phi_E,\Phi_I$ (1729); $\Phi_s$ (3856); scaling functions $\Phi_M,\Phi_\chi$ (3937).
kappa: attention-temperature scalar (declared); condition number $\kappa(\Sigma_i)$ (2510); an undefined proportionality constant in $M_{\mathrm{eff}} = \kappa\,\mathrm{tr}(\Sigma_{p,i}^{-1})$ (2075); conductances $\kappa_{ij}$ (declared).
M: declared overloads are fine, but $M_{\mathrm{eff}}$ is first used at 1763 and 2056 and only defined at 2075; the table at 2056 pairs "Mass $m$" with "Fisher information $\mathrm{tr}(\mathcal{M})$" while $m$ is the generative-model parameter (152-176), the internal gap $m_I$ (3861-3913), and the observation locations $m_k$ (897). (The unbound $m_i$ of 669/689 is registered (ledger), not re-raised.)
G: structure group $G$; generators $G_a$ (252, 377, 2365-2514), $G$ as a generator at 416, $G_x,G_y,G_z$ (2639-2649); metrics $G_i^{(q)}$ etc. (1874-2095), $G_{\mu\nu}$ (1922-1972), $G_\phi$ (1523), $G_{\mathrm{slow}}$ (3704-3934), $G^{AB}$ (3536-3542). The notation appendix lists only "the group $G$".
K: fiber dimensions $K_q,K_m$; key matrix $K$, $K_j$ (1008-1233); horizontal form $\mathcal{K}(A_\mu,A_\nu)$ (P2, 1817); $K_{AB}$ (3556). The recovery section also writes the dimension as $d_k$ ($\tau = \kappa\sqrt{d_k}$ at 1231 versus $\tau=\kappa\sqrt{K_q}$ at 673).
c: base point $c$; propagation speed $c_\mathcal{I}$ (1820, 1980), which a physicist reads as the speed of light; hyperparameter $c_0$ (453-829, 2232); constant $c$ (3294).
I: cluster index $I$; information gain $\Delta I_i$ and $\Delta I_I$ (1830, 1856); identity matrix $I$ (e.g. 316, 405); agent set $I_s$ (3169, 3634).
Z: partition functions $Z_i$, $Z_s$, $Z_I^{\mathrm{exact}}$ (722, 3634, 3648) versus the meta-clock ratio $Z_I := \mathbb{E}[\Delta I_I]/\mathbb{E}[\Delta I_i]$ (1856).
r: hyper-prior $r_i$; residual $r := \mu_i - \Omega_{ij}\mu_j$ (2375-2385); ratio argument $r_{ij}$ (3062-3130); $r_j$ in the untied score (1098).
g and h: Fisher metric $g_{\mathcal{B}}$, gauge element $g$ (194, 653), scalar $g_{ij}$ (3293), spacetime metric $g_{\mu\nu}$ (1980, 2075), control parameter $g$ (3937); spatial information metric $h_{ab}$ (1980), first fundamental form $h$ (2075), human observers $h_k$ (2561-2567), head index $M_h$ (1086-1212).
**Severity:** medium (individually low; collectively they make the notation appendix's promise at 92 and 3946, "every later use refers back to this section rather than redefining a symbol locally," untrue).
**Fix:** Either rename (preferred: $\chi_i \to$ keep; susceptibility $\to \chi_{\mathrm{sus}}$; Gaussian factors $\to \varphi_{i,\pi(i)}$; condition number $\to \operatorname{cond}(\Sigma_i)$; $c_\mathcal{I} \to v_\mathcal{I}$; $\Delta I_i \to \Delta\mathcal{I}_i$; meta-clock ratio $Z_I \to \zeta_I$; residual $r \to \delta\mu$; human observers $h_k \to o_k$ or $H_k$) or replace the prose appendix by a symbol table, as the Theory does (`ca_notation.tex`, `tab:notation`), listing every overload with its scope.
**Falsifies:** Scoped local redefinitions at each listed line; I found them only for $\kappa_{ij}$, $M$ decorations, $\rho$, $\pi$, $w$, which the appendix does declare.
**Status:** notational.

[L17-editor-venue] ### L17-4: A concrete restructure into a physics-journal paper of about 16,500 words

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
