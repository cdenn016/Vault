# Philosophy-of-science and framing report: GL(K) attention v2 pair (2026-09-23)

Lens: claims, framing, and argument structure of `GL(K)_attention_v2.tex` (Main) and `GL(K)_supplementary_v2.tex` (Supp), line numbers as in the brief. Author model of this report: Claude Opus 5.5 (investigator role; no verification verdict is claimed).

Inputs read in full: both targets; the prior review (`review.md`, `investigators/framing.md`, `investigators/gauge.md`, `figure-data-plan.md`); the extension (`GL(K)_extension.tex`: abstract, scope, gauge section, architectural consequences); the gradients companion (front matter and section plan); the treatise `main.tex` and the sheaf passage of `09_coarsegraining.tex`; the vault GL(K) concept page, the September matrix-link source note, and the philosophy theme page; the featured run’s `config.json`, `research.json`, `parameter_motion.json`; the block-MLP registry in `vfe3/model/block_mlp.py`. `Research/manuscripts/verified-ledger.md` does not exist (the prior framing investigator found the same); the brief’s settled list was used, and nothing below disputes a settled identity. Every finding concerns how strongly or how accurately a correct result is framed.

## Verdict

The mathematics is sound and the text is careful about scope, but the paper frames the wrong things as its results. Its title-level property, gauge covariance, holds for every operator built from the frame-invariant reference moments, whatever the routing rule and whatever the learned maps. In Kretschmann’s and François’s sense it is artificial, and it constrains nothing. The frames do computational work only in the components that break that covariance. Those components hold 90% of the parameters and make the imported LayerNorm, MLP, and decoder token- and position-specific. The conclusion’s “lattice-gauge structure” has no invariant content beyond the standard value/output operator, because causal support admits only self-loops.

Meanwhile the paper’s genuinely informative results stay out of the abstract, introduction, and conclusion. The first is the key-norm penalty that survives concentration, which makes the shared-covariance limit L2 attention. The others are the reference-moment normal form and the link rank and composition algebra. The main text is 2.4 times as negation-dense as comparable published papers, and six scope disclaimers are restated 2 to 8 times each. The hedging is misallocated: the body is over-hedged, the headline under-hedged.

As a step toward “no neural architectures” the paper contributes a characterized Gaussian comparison rule. It derives none of the neural processing, and the prior review’s motivation paragraph credits it with a property every attention operator already has.

## Findings (strongest first)

### F1. “Gauge-covariant” names a dressing (Stueckelberg-type) covariance that every operator of this form has, independent of the Gaussian choice
**Location:** Title (Main 38); Abstract 50 (“compose into matrix-valued communication links with a local endpoint covariance law”); Intro 59 (“these operations require compatible transformations of both its mean and covariance”); 466 (“The projected Gaussian routing below supplies the required scalar invariance”); Proposition “Passive covariance of ideal predictive attention” (913-924); Conclusion 1189 (“Full multivariate Gaussian states support the exact covariance law”); 757, 775, 799 (“In our/the gauge-theoretic framework, ...”).
**Severity:** critical
**Evidence:**

(1) *What the proof uses.* The proof at 922 uses only ξ′=ξ and C′=C and nothing specific to the Gaussian KL. I checked this with `philo/kretschmann_checks.py`: a tiny model of Algorithm 1 with N=6, K=4, block frames GL(2)², 2 heads, 2 layers, run on CPU in float64. Passive-action residuals were:
- Gaussian-KL routing: 5.0e-16 on the weights and 5.3e-15 on the messages.
- Plain dot-product routing on dressed means, with no covariance at all: 4.4e-16 and 3.6e-15.
- An arbitrary nonlinear dressed map m_i = U_i F(U_i⁻¹μ_i): 1.2e-15.

So the covariance neither depends on the Gaussian family nor constrains S_Q, S_K, T, O. The paper concedes the second point once (660: “Its endpoint covariance follows from the transforming frames, without requiring the fixed reference maps to be group intertwiners”) but never draws the consequence for the title, abstract, or conclusion.

(2) *Primary sources.*
- **Kretschmann, via Norton 1993** (Rep. Prog. Phys. 56, §5.1, pp. 817-819), text checked. Kretschmann: “By means of a purely mathematical reformulation of the equations representing the theory ... any physical theory can be brought into agreement with any, arbitrary relativity postulate ... and this without modifying any of its content that can be tested by observation.” Norton: “In brief, general covariance is physically vacuous,” and the argument covers “formulations of any theory of arbitrary covariance,” not only the general group.
- **Anderson 1967, via Norton §8.1** (pp. 843-846). Substantive content lies in the absence of absolute objects, where “an absolute object affects the behaviour of other objects but is not affected by these objects in turn” (Anderson and Gautreau 1969). Here the absolute objects are the shared reference maps and reference metric in V, and the LayerNorm, GELU basis, decoder, and diagonal storage basis in E_i.
- **François 2019** (Phil. Sci. 86:472-496; arXiv:1801.00678 §2.2), text checked. Criterion (C1): “A local dressing field in a gauge theory signals that its gauge symmetry is artificial.” The dressing field “must be constructed out of the space of primary gauge variables of the theory,” and the Stueckelberg trick is the reciprocal operation.

U_i is exactly such a field. It is local (site i only), a primary learned variable, and transforms as U_i → g_iU_i, so that ξ_i=U_i⁻¹μ_i and C_i are invariant local composites. The dressing-field method is due to Fournel, François, Lazzarini, Masson (Int. J. Geom. Methods Mod. Phys. 11:1450016, 2014, arXiv:1212.6702; the brief’s “J. Math. Phys.” attribution is incorrect) and is reviewed in Attard et al. 2018. Executed check: the fully dressed stack equals a frame-free reference stack to 3.6e-15.

(3) *Contrast with substantive gauge equivariance.* Weiler, Forré, Verlinde, Welling 2021 (arXiv:2106.06020, abstract): “A simultaneous demand for coordinate independence and weight sharing is shown to result in a requirement on the network to be equivariant under local gauge transformations.” Their constraint arises because shared kernels are applied in frames that have no canonical choice. Here the learned U_i supply a canonical frame at every site, and the shared maps act in a global reference space, so no constraint arises. CASK (Nagai, Ohno, Tomiya 2025, arXiv:2501.16955; in `references.bib` as `he2025cask` but uncited) makes gauge invariance constrain attention: scores are Frobenius products of given link variables and staples. L-CNN (Favoni, Ipp, Müller, Schuh, PRL 128:032003, 2022) works the same way.

(4) *Why the construction had to be artificial.* `philo/schur_check.py` gives:
- dim{S : Sg=S for all g ∈ GL(4)} = 0;
- dim{S : Sg=S for all g ∈ GL(2)×GL(2)} = 0;
- the commutant of the defining action is the scalars (dim 1).

Undressed local GL equivariance with a trivially acting comparison space would therefore force S_Q=S_K=T=0, or scalar maps. Learned rectangular interfaces exist only through dressing. The dressing is the price of learned interfaces, and it is what empties the covariance of constraint.

(5) *The genuine redundancies are unnamed, and the principal gauge freedom is broken.* Executed:
- Global block re-basing (U→Ua, S→Sa, T→Ta, O→a⁻¹O) is an exact redundancy of the reported full stack: 2.3e-14.
- The cogredient per-head map (S_Q,S_K)→(AS_Q,AS_K) leaves Gaussian routing invariant (3.0e-15). Dot-product routing instead requires the contragredient map: 2.2e-16 under it, versus a 0.44 change under the cogredient one.
- The principal-bundle right action U_i→U_ih_i (change of section, μ fixed, site-dependent h_i) changes the logits by 7.63.

So the local group the paper calls “gauge” is not a redundancy of the reported model, and the redundancies it does have are global and per-head.

The program already states this bound elsewhere. PIFB2.tex:2113-2116 has a Remark “Kretschmann bound” citing `Kretschmann1917` and `Norton1993`, both in the shared bib. The extension concedes that carrying the reference law as geometric data “makes the rule covariant,” while fixing it restricts the symmetry to a stabilizer (GL(K)_extension.tex:341). The attention paper applies neither.

(6) *Overloaded term.* This is Lipton and Steinhardt 2018 (arXiv:1807.03341) failure mode (iv). In the works cited at 69 (Cohen 2019; He 2021), “gauge-equivariant attention” means equivariance to a transformation of the input. Tokens carry no GL(K) action, so an ML reader will infer an inductive bias the model does not have. Lines 757, 775, and 799 credit mixture-prior semantics to “the gauge-theoretic framework”; they come from the categorical source model and read identically without frames.
**Fix:**
- **Title.** Retitle to name the substantive content, for example “Gaussian-KL Attention on Framed States: Exact Routing Reductions and Matrix-Valued Content Links”. If “gauge” stays, the abstract must say what the covariance is. Proposed abstract sentence: “All routing and content computations depend on the states only through frame-invariant reference moments; the operator is therefore covariant under independent changes of site frames, a consistency property that any operator built this way shares and that places no constraint on the learned interface maps.”
- **Line 466.** Replace with “Because every comparison law is a function of the invariant reference moments, the routing weights are unchanged.”
- **Line 1189.** Replace with “Covariance holds for any operator built from the reference moments; full Gaussian storage is needed only to keep the stored covariance family closed under site-frame changes.”
- **Lines 757, 775, 799.** Delete “gauge-theoretic”.
- **Citations.** After the Proposition, add one paragraph citing Kretschmann1917/Norton1993 and weiler2021coordinate (all already in the bib) and François 2019.
**Falsifies:** Any one of the following would retract this finding:
- an operator in the paper’s class (routing and content computed from reference moments, with learned rectangular S_Q, S_K, T, O) that violates the Proposition;
- a group action on token sequences under which the model is equivariant;
- a step of the proof at 922 that uses more than the dependence on (ξ, C).
**Status:** P, true by construction. The prose inflates it into a headline property and misattributes it to Gaussianity (466, 1189).
**Novelty vs prior review:** Extends R1 and disagrees with R1’s proposed contribution wording (“a typed, frame-covariant organization of Gaussian communication”), which keeps an automatic property as the headline. Also disagrees with the prior framing investigator’s conclusion that no high or critical philosophy finding exists.

### F2. The learned frames act only where the covariance fails, and the construction that restores covariance is one line and already implemented
**Location:** 939 (“These nonlinear state maps require a separate equivariance construction if the complete predictor is to have that symmetry”); the same scope at 359, 617, 924, 1171; Algorithm 1 (1117-1121); 1132-1136 (reported architecture; 90.16% of parameters in token frames); 1183 (proposed frame ablation).
**Severity:** high
**Evidence:**

*What the frames do in the reported stack.* In reference coordinates the reported stack is (lead L1):
- ξ⁽⁰⁾ = U_i⁻¹μ_p(x_i);
- C_i = U_i⁻¹Σ_p(x_i)U_i⁻ᵀ;
- ξ⁽ℓ⁺¹⁾ = U_i⁻¹G(U_iξ^att), with G=(id+MLP)∘LN;
- logits = W_outU_iξ⁽ᴸ⁾.

The executed check reproduces this. The reported stack changes its logits by up to 6.48 under the passive action. The dressed stack, with G replaced by U_iG(U_i⁻¹·) and the decoder by W_outU_i⁻¹, is covariant to 1.1e-14. It also coincides with a frame-free stack whose only frame dependence is the initial state (3.6e-15).

The frames therefore act through four channels:
- a multiplicative (token, position) map on the embedding;
- a static (token, position) routing covariance;
- a (token, position)-specific conjugation of the shared LayerNorm and MLP;
- a (token, position)-specific decoder.

The last two exist only because covariance is broken.

*What the run and the code record.* The run’s own build metadata records this class: `executable_build.block_mlp.gauge_class = coordinate_nonintertwiner`, `intertwiner_compatible = False` (config.json of 31.04_...). The reference implementation registers two alternatives (`vfe3/model/block_mlp.py:425-463`):
- `canonical_frame`, labeled `left_equivariant_right_fixed`: exactly the dressed U G(U⁻¹·).
- `gauge_gate`, labeled `invariant_scalar_intertwiner`: one gate per frame block driven by the Mahalanobis invariants μ_hᵀΣ_hh⁻¹μ_h. This is the genuinely constrained, Schur-limited option.

So line 939 presents as open a construction that is trivial (canonical_frame), and does not mention one that is substantive (gauge_gate). Both are implemented.

*Capacity and severity.* The frame table holds 411,705,344 of 456,654,162 parameters. Sparse per-token tables improve LM loss on their own: Lample et al. 2019 (NeurIPS, arXiv:1907.05242) use product-key memory of up to a billion parameters at negligible compute, and Huang et al. 2025 (ICML, arXiv:2501.16975) report a log-linear gain from larger input-vocabulary tables. In Mayo’s (1996) terms, the 31.04 PPL pass therefore has no severity against the alternative “frames supply 412M parameters of token- and position-conditioned neural capacity.” That alternative predicts the same pass.

*Standing rule.* This is not a finding against the coordinate default. The pure paths exist and are reachable by toggle. The finding is that the manuscript describes them as missing and does not report which class it ran.
**Fix:** After the Proposition, state the normal form and its consequence (Rewrite R-d below) and name the class run (“coordinate, non-intertwiner”). Add the coordinate / canonical_frame / gauge_gate comparison and a capacity-matched identity-frame arm to 1183 and to the placeholders (T3 below).
**Falsifies:** Either of the following would retract this finding:
- evidence that the executed code applied LayerNorm, MLP, and decoder in reference coordinates (the reported model would then be the dressed stack, and the frames would reduce to state parametrization);
- a demonstration that U_i⁻¹G(U_i·) is frame-independent at the trained parameters.
**Status:** D. The normal form follows from the paper’s own 1042-1049. The prose turns a positive structural result into a scope disclaimer, and by calling the construction open it inflates the difficulty and significance of the gauge constraint.
**Novelty vs prior review:** Extends R1, which says frames “affect the admitted effective states and the complete computation” but neither locates the effect in the symmetry-breaking components nor identifies the dressed and intertwiner modes. Not covered by R6 or by placeholders F2/F4.

### F3. “A lattice-gauge structure at the level of link fields” names no invariant content beyond the standard value/output operator
**Location:** Conclusion 1189 (“their composition and invariant loop traces extend the communication description beyond the flat frame transport. This identifies a lattice-gauge structure at the level of link fields”); Intro 71; Abstract 50 (“loop traces”); Lemma thm:vanishing_holonomy (581-591); 594-607.
**Severity:** high
**Evidence:**

*No nontrivial loops.* On the causal support S_i={0,...,i}, every closed product L_{i0 i1}...L_{i_{r-1} i0} requires i₀ ≥ i₁ ≥ ... ≥ i₀, so the walk is constant. Executed enumeration at N=5 (`philo/loops_and_records.py`): all 20 closed walks of lengths 1-4 visit a single site. The only loop observables are self-loop traces Tr((Σ_h β_ii⁽ʰ⁾ O_hT_h)^r). These equal the traces of the standard multi-head operator Σ_h β W_O^h W_V^h (residual 8.9e-16). The paper states the frame-free form at 604 and concedes the absence of cycles at 607, then asserts the structure at 1189 anyway.

*The link field is pure gauge over the transformer operator.* The field is L_ij = U_iA_ijU_j⁻¹: gauge-equivalent to the frame-free A_ij, i.e. a pure-gauge dressing of the transformer’s value/output operator. Lattice gauge theory has three defining features, and all three are absent:
- independent link variables (here the links are composite);
- a gauge-invariant action (none; the paper concedes this at 617 and 1189);
- Wilson loops with content (the only loops are trivial).

This is the reading in Wilson 1974, and in Wetterich 2014 §2, where arbitrary matrix links carry a separately specified action; the prior gauge investigator verified that primary source. The Lemma is a telescoping identity: Ω is pure gauge by definition.

*Where the terms carry content.* A gauge-covariant transformer with lattice link fields has content when the links are given data: CASK (Nagai, Ohno, Tomiya 2025) and L-CNN (Favoni et al. 2022, whose layers form “arbitrarily shaped Wilson loops” and approximate “any gauge covariant function on the lattice”).

*The right counterpart.* For learned, possibly singular edge maps factored through an edge space, the counterpart is the cellular sheaf:
- Hansen and Ghrist 2019 (arXiv:1808.01513, in the bib as `HansenGhrist2019`);
- Hansen and Gebhart 2020, sheaf neural networks;
- Bodnar et al. 2022 (NeurIPS, arXiv:2202.04579): “assigning vector spaces and linear maps to nodes and edges,” with sheaves “learned from data”;
- with attention, Barbero, Bodnar, Sáez de Ocáriz Borde, Liò 2022, “Sheaf Attention Networks” (NeurIPS 2022 NeurReps workshop).

The comparison cospan E_i → H^cmp ← E_j (529-535) is literally a pair of restriction maps into an edge stalk. The treatise already classifies the program’s general links this way: “This is the degree-zero cellular-sheaf Laplacian category ... It is gauge covariant and strictly larger than the fixed-K group-link family” (gauge_vfe_rg/09_coarsegraining.tex:2340-2344).

*Deletion test* (Lipton and Steinhardt iii): removing “lattice-gauge structure” from 1189 changes no stated result.
**Fix:**
- **Line 1189.** Replace the last two sentences with: “The routed links are frame-dressed copies of the value/output operator Σ_h β_ij⁽ʰ⁾O_hT_h; on causal support their only closed products are self-loops, whose traces are frame-independent. A lattice-gauge interpretation would require independent invertible edge variables Θ_ij with nontrivial holonomy (Section 2.4.3), which the present model does not contain.”
- **Line 71.** Replace “connects this formulation to lattice gauge geometry” with one positioning sentence citing Hansen and Ghrist 2019, Bodnar et al. 2022, and CASK.
- **Lemma.** Demote it to a remark.
- **If a lattice claim is wanted:** make it falsifiable. Train independent invertible Θ_ij, measure holonomy on undirected triangles using Θ⁻¹ on reversed edges, and show that forcing Θ to pure gauge degrades held-out loss.
**Falsifies:** Any one of the following would retract this finding:
- a closed directed walk through distinct positions on causal support;
- a routed-link loop observable that differs from its frame-free trace;
- an explicit link action used in the paper.
**Status:** S (an analogy) presented as D (“identifies”); the prose inflates it.
**Novelty vs prior review:** New. Disagrees with the prior framing investigator, who graded 1189 as “D/S with limitations at 607 and 615; no realized connection-holonomy claim.”

### F4. Canonical counterparts are missing for four component claims; the natural transformer limit of the Gaussian router is L2 attention
**Location:** 804 (“a prior bank, which is the generalization of the embedding matrix”); Proposition prop:projected_dot_product (987-1007) and Abstract 52 (“conditional correspondence with transformer attention”); 65 and 686-721 (Gibbs routing); 67 and 683 (novelty sentences); 71 and 405-617 (matrix links); 79 (“A token in a language model is one finite-dimensional realization of an agent”).
**Severity:** high
**Evidence:** Each counterpart below was checked against its primary record.

*Prior bank.* Vilnis and McCallum 2015 (ICLR; arXiv:1412.6623) learn per-word Gaussian embeddings with a mean and a diagonal or spherical covariance, and score word pairs with “−E(P_i,P_j) = D_KL(N_j‖N_i)” (§5.2, text checked). The prior bank’s (μ_p^c, Σ_p^c) with KL scoring between token Gaussians is that construction plus frame coefficients. It is not cited.

*Isotropic reduction.* The stronger clause of Proposition 2, D_ij = ‖a_i−b_j‖²/(2σ²), is L2 self-attention: P_ij ∝ exp(−‖x_iᵀW^Q − x_jᵀW^K‖²/√(D/H)) (Kim, Papamakarios, Mnih 2021, ICML, §3, source checked; they tie W^Q=W^K only for their Lipschitz theorem). The shared-anisotropic case is the same thing after whitening. There D_ij = c_i + ½‖k_j‖² − q_iᵀk_j equals ½‖q_i−k_j‖² plus a row constant, so it is Mahalanobis L2 attention.

The key-norm bias the paper derives is exactly what separates L2 attention from dot-product attention. The natural transformer limit of Gaussian-KL routing is therefore L2 attention. Dot-product attention is reached only with constant or compensated key norms, which the paper itself shows are not supplied by concentration or LayerNorm (1034).

*Gibbs routing in attention.* The paper cites Boyd and Wainwright, which is correct but does not position the result within attention. The attention-specific precedents are:
- softmax as the entropy-regularized argmax, in a framework that includes softmax and sparsemax as special cases: Niculae and Blondel 2017 (NeurIPS; arXiv:1705.07704);
- attention as MAP inference in a Gaussian mixture: Movellan and Gabbur 2020 (arXiv:2010.15583: “Transformers are Maximum Posterior Probability estimators for Mixtures of Gaussian Models”).

*Matrix links.* The counterpart is cellular sheaves and sheaf neural networks; see F3.

*Agents.* TarMAC (Das et al. 2019, ICML; arXiv:1810.11187, text checked) implements agent communication as “signature-based soft attention.” Each message carries a signature (a key) and a value, and receivers attend with a query. That is the comparison/content split, in an explicitly multi-agent setting. CommNet precedes it.

*What checks out.* Pro-Attention (Bae, Cheon, Kim 2022, IEEE Access 10:131192; abstract via Semantic Scholar) treats the components of a token vector as samples from a token-specific distribution and scores with KL at a cost independent of feature dimension. The paper’s distinction at 67 (“multivariate, retain their full reduced covariance”) is therefore accurate.

*Documented search.* I found no prior instance of KL routing between full-covariance projected Gaussians in learned comparison spaces. Queries: “attention mechanism KL divergence between Gaussian query and key distributions full covariance learned projection transformer”; “Pro-Attention Bae 2022 probabilistic attention Gaussian query key KL divergence”. Transformer-MGK (Nguyen et al. 2022) uses Gaussian-mixture keys and is already in prior R7. The combination claim at 683 stands as stated.
**Fix:**
- **Line 804.** Cite Vilnis and McCallum 2015 and replace “the generalization of the embedding matrix” with “a Gaussian embedding table in the sense of Vilnis and McCallum (2015), extended by frame coefficients”.
- **After Proposition 2.** Add: “With shared projected key covariance the routing is L2 attention in whitened coordinates; under the stronger isotropic hypothesis it is the L2 self-attention of Kim et al. (2021). Dot-product attention is recovered only when projected key norms are constant or compensated.”
- **Lines 65 and 720.** Cite Niculae and Blondel 2017 and Movellan and Gabbur 2020.
- **Line 79.** Cite TarMAC.
- **Line 71.** Cite the sheaf papers.
**Falsifies:** Either of the following would change this finding:
- a reading of Vilnis and McCallum or Kim et al. that differs from the quoted definitions;
- evidence that the full combination at 683 appears in prior work, which would upgrade this finding to a priority issue.
**Status:** The combination claim at 683 is D and accurate. The words “the generalization” (804) and the abstract’s “correspondence with transformer attention” are S/D claims with an existing canonical counterpart; the prose inflates them by omission.
**Novelty vs prior review:** Extends R7 (CRATE, MGK) with different counterparts. Overlaps lead L8: Niculae-Blondel, Kim et al., and Movellan-Gabbur are verified here. Martins and Astudillo 2016 and Gabbur et al. 2021 were not checked in this lens.

### F5. As a step toward “no neural architectures,” the paper adds a characterized comparison rule but derives none of the neural processing, and the prior review’s motivation paragraph credits it with a property every attention operator has
**Location:** Abstract 52; 79; 926-939; 1132-1136; 1169-1176. Prior review §1, motivation paragraph (“Here we construct Gaussian comparison and predictive communication independently of a neuron-level description”).
**Severity:** high
**Evidence:**

*What the paper derives and what it imports.* It derives Gibbs routing, which is classical (F4), and a Gaussian-KL cost with exact reductions (D). It does not derive:
- the content maps (900 concedes the joint “does not select its means, T_h, O_h, or the residual”);
- the residual (1053);
- LayerNorm;
- the GELU MLP with 8× expansion;
- the linear decoder;
- the depth.

All of these are imported from the transformer (Algorithm 1). In the narrow sense that matters to the program, the reported model is as neural as a standard transformer: coordinatewise nonlinear units and backpropagated weights.

*The prior review’s motivation paragraph.* It credits the paper with constructing comparison and communication “independently of a neuron-level description”. Every attention operator already is: attention is linear algebra and a softmax on vectors, with no neuron in it. Renaming “hidden vector” to “Gaussian state” and “token” to “agent” (79) is a relabeling unless an agent-level principle forbids or predicts something. Lakatos (1978) calls a problemshift theoretically progressive only when it yields excess empirical content. The object that matters to the program is the processing rule, and the MLP is the part that is neural in the narrow sense. The extension attacks it (GL(K)_extension.tex:637: “prescribed neuron layers are unnecessary for existence of these roles”) but reports no language-model test (674).

*Where the realization pulls against the program.*
- 90.16% of the parameters are token frames whose role in this model is to make the imported neural block and decoder token- and position-specific (F2). If the frames are what make the model work, the gain comes from enriching the neural block.
- The stored covariance is static and nearly uniform (F8), so an agent’s “uncertain state” never responds to communication.

*What the framework forbids that a plain transformer does not* (the Lakatosian test):
- (i) with shared projected key covariance, a sign-definite penalty on whitened key norm at a fixed cross term, removable only by a state-dependent prior;
- (ii) a cogredient rather than contragredient GL(r_h) redundancy of the comparison maps (executed, F1(5));
- (iii) in gauge_gate mode, any non-intertwiner nonlinear processing.

Items (i) and (ii) are testable structural consequences. Item (iii) is a substantive constraint whose empirical viability is unknown. None of the three is currently stated or tested.
**Fix:** Adopt the contribution statement and the predictions P1-P5 in “The paper within the program” below. In the introduction, state three things:
- attention is the one transformer component already defined as a communication operator;
- this paper characterizes it for framed Gaussian states;
- the coordinatewise processing retained here is the target of the companion extension.

Do not claim the construction is neuron-free in any sense in which standard attention is not.
**Falsifies:** Either of the following would retract this finding:
- an agent-level principle in the paper that selects T, O, the residual, or the nonlinear block;
- a matched experiment in which gauge_gate or an inference-derived update replaces the MLP without loss (this would move the program claim from S to E).
**Status:** S (program framing). The prior review’s paragraph would inflate it.
**Novelty vs prior review:** Disagrees with the prior review’s §1 motivation paragraph and with the prior framing investigator’s sentence “This construction requires no prescribed neuron layer,” both of which credit a non-distinguishing property. Extends the prior review’s “Optional later milestone”.

### F6. Hedging is misallocated: the body repeats scope disclaimers, the front matter announces results without stating them, and the headline claims carry no hedge
**Location:** Whole main text; Abstract 50-52; Intro 57-73; Discussion 1164-1185; Conclusion 1187-1191; Supp 78.
**Severity:** medium
**Evidence:**

*Negation rate.* Method: `philo/negcount.py`, with floats, display math, and TikZ removed, inline math tokenized, and abbreviations protected. In the main text, 114 of 514 prose sentences (22.2%; 23.3% of prose words) contain a core negation (not, no, neither, nor, cannot). By section:
- Realization: 30.6%
- Discussion: 30.3%
- Transformer correspondence: 27.7%
- Geometric construction: 21.5%
- Predictive communication: 17.0%
- Introduction: 15.0%
- Abstract: 9.1%
- Conclusion: 8.3%
- Supplement: 23.8%

*Baseline.* The same script on six published attention and equivariance papers:
- Nguyen et al. 2022: 3.2%
- Vaswani et al. 2017: 3.4%
- Niculae and Blondel 2017: 8.3%
- Cohen et al. 2019: 10.3%
- Tsai et al. 2019: 10.9%
- Kim et al. 2021: 15.5% (a paper whose main theorem is itself a negative result)

The median is 9.3%. The v2 main text runs at 2.4 times the median and above the maximum.

*Repetition.* Six scope disclaimers recur (line numbers in the census section below):
- covariance does not extend to LayerNorm, MLP, or decoder: 6 times;
- no common free energy or population model: 8;
- one seed or feasibility only: 8;
- passthrough is not propagation: 5;
- unit temperature only: 6;
- no priority claim: 2.

*Manual classification.* I classified the 98 sentences in the brief’s scope ranges; criteria and assignments are in the census section:
- 7 state a positive result with its content;
- 7 announce a result without stating it (“We characterize their rank, restricted flatness, loop traces ...”; “The contribution is the explicit organization of ...”);
- 8 inflate (F1, F3);
- 17 are necessary scope statements;
- 18 are redundant disclaimers or rebuttals of claims the paper never makes (the FEP at 52 and 65; “a measured cognitive faculty” and “a channel capacity” at 1179; “an autonomous lattice action” at 71).

The lexical count understates the front matter. The Conclusion has no lexical negation, yet 3 of its 9 sentences repeat scope. The abstract carries its scope through “may have low rank ... and fail” rather than through negation.

*What never reaches the front matter.* The paper’s strongest content-bearing results do not appear in the abstract, introduction, or conclusion:
- the key-norm bias survives high-dimensional concentration and is not removed by LayerNorm (1034);
- the composition defect O_h(T_hO_h − I)T_h and its converse (564-572);
- the rank bound, under which rank-deficient heads can sum to full rank (468-474);
- the reference-moment normal form (1042-1049).

*Who the negations address.* They largely rebut claims made by earlier versions of the program (the FEP and cognitive readings). They are therefore aimed at a reader who has not seen those versions and has no reason to hold those claims.
**Fix:** State each scope once, in one “Scope” paragraph after the contribution statement, and delete the repeats. Move the positive results into the abstract and conclusion. Drop-in text is in “Rewrites” below (R-a to R-e, plus the Scope paragraph).
**Falsifies:** Either of the following would retract this finding:
- a baseline of comparable theory-heavy ML papers whose median negation rate is at or above 22%;
- a reclassification showing that most of the 18 repeats are needed where they stand.
**Status:** The prose deflates D and P results in the front matter while inflating S claims in the headline.
**Novelty vs prior review:** New. R2 concerns section order, not the balance of positive statements and disclaimers.

### F7. The content-side “correspondence” is definitional, and the correspondence table mixes derived, definitional, and non-correspondence rows
**Location:** Abstract 52 (“the content links reproduce value and output aggregation exactly”); 966; 1042-1053; Table tab:fep_nn_correspondence (1071-1091).
**Severity:** medium
**Evidence:**

*Why the content correspondence is definitional.* T_h and O_h are introduced as the value and output maps (375-384), and 1051 sets W_V⁽ʰ⁾=T_h and W_O⁽ʰ⁾=O_h. That the content links “reproduce” value/output aggregation is therefore true by construction. Its use-novelty is zero: evidence supports a theory only insofar as the theory was not built to fit it (Worrall 2014). Only the routing side is a derived conditional reduction.

*Why the table overcounts.* All eight rows are labeled “correspondences”, but they are of three kinds:
- rows 1-3 and 6 are derived conditional equalities;
- rows 4-5 are identities by construction;
- rows 7-8 record non-correspondences (“Explicit architecture”; “Separate processing choices outside the attention-operator correspondence”).

The table’s label (fep_nn_correspondence) is invisible to readers and is not a finding.
**Fix:**
- **Abstract.** Use: “...shared projected key covariance produces a whitened dot-product score with a key-norm penalty; the content maps are the value and output maps of standard attention written in local frames.”
- **Table.** Split it into three labeled groups: “Derived under stated conditions”, “Identical by construction”, “Not derived (architectural choices)”.
**Falsifies:** A derivation in which T_h and O_h are selected by the variational construction rather than declared; the paper itself denies this at 900.
**Status:** A definitional identity presented as a derived correspondence; the prose inflates it.
**Novelty vs prior review:** New. The prior review’s §4 lists “Value/output aggregation equals concatenated head output: Exact algebra” without noting that the equality holds by construction.

### F8. The routing covariance is a static lookup per (token, position); the run’s own covariance-diversity gate failed; the “uncertainty” motivation has no counterpart in the realization
**Location:** 59 (“When a representation also carries uncertainty and a local coordinate frame, these operations require compatible transformations of both its mean and covariance”); 937; 1108, 1119, 1134 (“The covariance and frame are held fixed through the stack”); 1159.
**Severity:** medium
**Evidence:**

*The covariance is a lookup, not a state.* Σ is initialized from the token prior (1108) and passed through unchanged (1119). The config agrees: `cg_covariance_mode = passthrough`, `block_mlp_covariance = passthrough`, `skip_belief_sigma_update = True`, `content_covariance_contract = frozen_receiver_bookkeeping_not_predictive_covariance`. The frames are fixed per (token, position). Hence C_i⁽ℓ⁾ = U_i⁻¹Σ_p(x_i)U_i⁻ᵀ at every layer and in every context. The covariance-dependent parts of D_ij (trace, log-determinant, and the source precision P_j in the quadratic and cross terms) are then learned static pair biases plus a per-source metric in comparison space (lead L3). None of them responds to the sequence.

*The run’s own gate failed.* `research.json` records `sigma_trace_cv = 0.0474` with `sigma_trace_cv_gate_pass = False`; the gate in the current `vfe3/run_artifacts.py:2965` requires CV > 0.10. It also records a Spearman correlation of 0.145 between tr Σ and per-token cross-entropy. The manuscript reports conditioning and repair diagnostics (1159) but not this failed gate.

*Why it matters.* The paper never claims calibrated uncertainty (the prior review’s C7 asks it to say so). But its motivating sentence (59) and the word “belief” invite the reading that the run tests uncertainty-aware routing. It does not. An agent whose covariance never changes in response to messages is not revising uncertainty, which matters for the program’s agent reading (F5).
**Fix:**
- **Line 1134.** Add: “Because covariance and frames are fixed through the stack, C_i is a static function of token type and position; its contributions to D_ij act as learned pair biases and a per-source metric in comparison space. The run’s covariance-diversity diagnostic (coefficient of variation of tr Σ = 0.047, below its 0.10 gate; Spearman correlation with per-token cross-entropy 0.145) shows no calibrated uncertainty signal.”
- **Line 59.** Either remove “uncertainty” from the motivation, or add a context-dependent covariance update and test it. The paper already has two candidates: the Gaussian channel marginal Q_i + L_ijΣ_jL_ijᵀ (633) and the mixture covariance (1069).
**Falsifies:** Either of the following would retract this finding:
- a forward-pass path in the executed configuration that modifies Σ as a function of context;
- a recomputation of the gate on the stored checkpoint showing CV > 0.10.
**Status:** S (the motivation) with no matching E. In the realization, the covariance is a parameter, not a state.
**Novelty vs prior review:** Extends C7, which asks only that covariance be named an operational state, with the static-lookup consequence and the failed gate. The static-covariance point is the framing consequence of lead L3.

### F9. “Exact variational” status can be had at every temperature, so the temperature hedges aim at the wrong target; the fixed-joint bridge credits a textbook identity to the program’s own theory
**Location:** 65, 721, 900, 1189 (unit temperature); Supp 51-78, in particular 54 (“A broader gauge-VFE theory begins with...”), 68 (“Normalization over all possible records is an additional hypothesis”), and 78 (“The broader construction provides a consistent setting for the missing identification”); Main 1176.
**Severity:** medium
**Evidence:**

*The construction.* Take a binary compatibility record P(o_i=1 | z, J_i=j) = exp(−D_ij(z)/τ). This lies in (0,1] because D_ij ≥ 0, and the capped cost also qualifies. The joint p(z)π(J)P(o|z,J) is normalized over o ∈ {0,1}, and the posterior over the source label equals softmax(log π − D/τ) for every τ > 0. Executed (`philo/loops_and_records.py`): |posterior − Gibbs| ≤ 1.1e-16 for τ ∈ {0.3, 1, √32}, capped and uncapped. This is lead L6; its probabilistic adjudication belongs to the probability investigator.

*The framing consequence, which belongs to this lens.* For any nonnegative cost, some normalized model makes the Gibbs row an exact posterior. That status is therefore available to every routing rule of the form softmax(log π − c) with c ≥ 0. It carries no evidence that attention “is” inference: the model is chosen by requiring the rule, so its use-novelty is zero (Worrall 2014). The project’s own record concedes the same point for Gaussian links: “The uniqueness result that does hold ... is a statement about the target rule, since the model was selected by requiring it” (wiki page “GL(K) gauge-equivariant attention”, 2026-07-27 section).

The paper spends six hedges restricting a status that extends to all τ and carries no evidential weight. It never asks the informative question: is the generative model that makes routing exact independently motivated?

*The fixed-joint bridge.* Supp App A presents the ELBO identity as the start of “a broader gauge-VFE theory” (54). Its only gauge-specific content is one clause (66), and the identity is the standard one, as the supplement’s own citation of Blei et al. 2017 acknowledges. Main 1176 and Supp 78 rely on the program’s unpublished treatise for “one population joint and one exact evidence bound” and for “a consistent setting”. That is a project document cited as authority. Citing the treatise, as R8 proposes, would assert the same claim twice without adding warrant.
**Fix:**
- **Supp 68 and the unit-temperature caveats.** Replace the hypothesis sentence and the caveats with one statement of the binary-record construction, if the probability investigator confirms it, and add: “This representation exists for any nonnegative cost; it shows that Gibbs routing is consistent with exact inference, not that attention must be inference.”
- **Supp App A.** Retitle it “Relation to a normalized latent-source model” and cite Blei et al. for the identity.
- **Supp 78.** Delete “The broader construction provides a consistent setting for the missing identification” unless a specific theorem of the treatise is stated and proved in the supplement.
**Falsifies:** Either of the following would retract this finding:
- a probability-lens refutation of the binary-record construction (for example, a normalization failure for capped costs);
- a specific statement of what the treatise contributes to App A that is not a textbook identity.
**Status:** The bridge identities are D; the “consistent setting” claim is S. The temperature prose deflates a restriction that can be removed, and the attribution inflates textbook content.
**Novelty vs prior review:** Extends R8: citation access alone does not supply warrant. Differs from R5, which concerns the product label prior, not the evidential weight of exactness.

### F10. The smooth-bundle apparatus does no inferential work for this paper’s results, and the four-document series lacks one thesis per paper
**Location:** Main 75-335 (Sec. 2.1 and Fig. 1), 73, 1200-1201; Supp 44; GL(K)_gradients.tex:45-47; GL(K)_extension.tex:27-45; gauge_vfe_rg/main.tex.
**Severity:** medium
**Evidence:**

*Deletion test* (Lipton and Steinhardt iii). Sec. 2.1 introduces a smooth contextual base, local sections over overlapping neighborhoods U_i ∩ U_j, and an associated statistical bundle. The finite construction needs only vector spaces E_i ≅ R^K, frames U_i ∈ GL(K), and states. No derivation, bound, or measurement uses the smooth base, the overlaps, or local sections, and Fig. 1’s own caption says “The finite token construction requires no smooth contextual base”. Fig. 1 depicts sections q_i(c), q_j(c) over overlapping contexts, which have no referent in the language model.

*The bundle advertises a freedom the model lacks.* The bundle’s own gauge group, the right action (293-296), is broken to a global group by the shared interface maps (executed: a site-dependent right action changes the logits by 7.63). The principal-bundle picture therefore advertises a local gauge freedom the model does not have.

*The series.*
- The gradients companion develops “optional” belief-revision objectives on the full-state flat transport Ω_ij (GL(K)_gradients.tex:45-47, 56). The v2 predictor does not use them.
- The extension is the paper that addresses the program’s aim, but its subtitle frames it as “A Conditional Extension of Gauge-Covariant Gaussian Attention”.
- The treatise is cited as authority (F9).

The same negation-heavy style runs through the series: extension 19.2%, gradients 26.2%.
**Fix:** Give each document one thesis, as laid out in “Series organization” below. For this paper:
- a theorem-first spine of four named results replaces the present one lemma and two propositions;
- keep one typed paragraph describing E_i and the frames;
- move the smooth-bundle construction and Fig. 1 to the supplement or the treatise.
**Falsifies:** Either of the following would retract this finding:
- a result in the main text whose proof uses the smooth base, overlapping neighborhoods, or local sections;
- use of the gradients companion by the v2 predictor.
**Status:** Organization. The bundle material is decorative for this paper (S) and inflates its apparent geometric content.
**Novelty vs prior review:** Agrees with R2 on reordering. Disagrees with R2’s “Preserve the principal/associated-bundle foundation” in the main text. Extends R8.

## Claim-status table (Task 1)

Status codes: P proven (by the stated proof or elementarily); D derived here; S suggested/structural; E empirical; Def true by definition or construction. The “Prose” column records whether the wording inflates, deflates, or accurately reflects the status assigned from the evidence present in the pair.

| # | Location | Claim (quoted or condensed) | Status | Prose | See |
|---|---|---|---|---|---|
| 1 | 38 | Title “Gauge-Covariant Gaussian Attention through Projected Matrix Links” | P (automatic) | inflates | F1 |
| 2 | 50 | “an entropy-regularized categorical objective determines source weights” | P (classical) | accurate | F4 |
| 3 | 50 | links “with a local endpoint covariance law” | P (automatic) | inflates (listed as a finding) | F1 |
| 4 | 50 | “These links may have low rank, mix frame blocks, and fail the composition identity” | P | deflates (possibilities in place of the rank bound and defect formula) | F6 |
| 5 | 50 | “We characterize their rank, restricted flatness, loop traces, and compatibility ...” | P; “loop traces” S | deflates (announced, not stated); “loop traces” inflates | F3, F6 |
| 6 | 52 | “shared projected key covariance produces a dot-product score with a key-norm bias” | P (conditional) | accurate but undersold (L2 limit and concentration failure omitted) | F4, F6 |
| 7 | 52 | “the content links reproduce value and output aggregation exactly” | Def | inflates | F7 |
| 8 | 52 | “We distinguish communication heads from irreducible frame blocks ...” | P | accurate, announced | — |
| 9 | 52 | “a common variational free energy for the entire language model is not established” | scope | rebuts an unmade claim | F6 |
| 10 | 52 | “records test perplexity 31.04 under its stated single-seed evaluation protocol” | E | accurate; no severity for any Gaussian or gauge claim | F2, F5 |
| 11 | 59 | “these operations require compatible transformations of both its mean and covariance” | S (normative) | inflates (Kretschmann) | F1 |
| 12 | 67 | “Our Gaussian observables are multivariate, retain their full reduced covariance, and transform with explicitly declared token frames” | D (novelty) | accurate against Pro-Attention; last clause automatic | F4 |
| 13 | 71 | “connects this formulation to lattice gauge geometry” | S | inflates | F3 |
| 14 | 73 | “The contribution is the explicit organization of ...” | S (vague) | deflates | F5, F6 |
| 15 | 79 | “A token in a language model is one finite-dimensional realization of an agent” | S (interpretive) | uncited precedent (TarMAC) | F4, F5 |
| 16 | 466 | “The projected Gaussian routing below supplies the required scalar invariance” | P, misattributed | inflates the Gaussian role | F1 |
| 17 | 581 | Lemma thm:vanishing_holonomy (closed Ω products equal I) | P (telescoping) | accurate; “Lemma” overweights a definitional identity | F3, F10 |
| 18 | 913 | Proposition, passive covariance | P (automatic) | statement accurate; inflated as a headline | F1 |
| 19 | 939 | “require a separate equivariance construction” | construction is one line and already implemented | inflates difficulty | F2 |
| 20 | 987 | Proposition prop:projected_dot_product | P (conditional) | accurate; undersold (L2 attention) | F4 |
| 21 | 1031 | Bound e^{2ε}−1 | P | accurate (sharpness is lead L7, another lens) | — |
| 22 | 1034 | “High-dimensional relative concentration alone is insufficient ... LayerNorm ... does not impose ...” | P (content-bearing negative result) | deflated by placement | F6 |
| 23 | 1071 | Table tab:fep_nn_correspondence | mixed P / Def / non-correspondence | inflates the count of correspondences | F7 |
| 24 | 1157 | Frozen-batch interventions show reliance on routing and prior | E (16 sequences) | accurate and scoped | — |
| 25 | 1161 | “supports feasibility of the combined architecture” | E | accurate | — |
| 26 | 1169 | “... together with its factorization into covariant matrix link fields” | S (vague) | deflates results; “covariant” inflates | F1, F6 |
| 27 | 1176 | “The general gauge-VFE construction supplies ... one population joint and one exact evidence bound” | S (project document as authority) | inflates attribution | F9 |
| 28 | 1189 | “Full multivariate Gaussian states support the exact covariance law” | P, misattributed | inflates | F1 |
| 29 | 1189 | “This identifies a lattice-gauge structure at the level of link fields” | S presented as D | inflates | F3 |
| 30 | Supp 68 | “Normalization over all possible records is an additional hypothesis” | removable (binary record) | deflates | F9 |
| 31 | Supp 78 | “The broader construction provides a consistent setting for the missing identification” | S (unsupported here) | inflates | F9 |

Net pattern: 15 rows inflate in whole or in part (1, 3, 5, 7, 11, 13, 16, 18, 19, 23, 26, 27, 28, 29, 31), mostly in the title, abstract, introduction, headline results, and conclusion. 7 rows deflate in whole or in part (4, 5, 9, 14, 22, 26, 30), mostly where the content-bearing results should be stated. Rows 5 and 26 do both.

## Negation census (Task 1, lead L10)

**Instrument.** `philo/negcount.py` works on prose only:
- it removes comments, TikZ, figure/table/algorithm floats, and all display-math environments;
- it replaces inline math with a token and citations and references with a token;
- it protects abbreviations (Eq., Sec., e.g., i.e., et al.);
- it splits sentences at terminal punctuation followed by a capital, digit, or math token.

The core negation set is exactly the brief’s: not, no, neither, nor, cannot (so “need not” and “does not” are covered). The extended set adds never, none, without, unless, nothing, alone, merely, automatically, generally, necessarily, “by itself”, and “in general”. The segmentation was spot-checked on the Introduction (40 sentences, all correctly split).

**Main text by section:**

| Section | Sentences | With core negation | Share | Word share | Extended share |
|---|---|---|---|---|---|
| Abstract | 11 | 1 | 9.1% | 10.1% | 9.1% |
| Introduction | 40 | 6 | 15.0% | 14.5% | 15.0% |
| Geometric Construction | 251 | 54 | 21.5% | 23.2% | 23.9% |
| Covariant Predictive Communication | 47 | 8 | 17.0% | 19.4% | 17.0% |
| Transformer Correspondence | 65 | 18 | 27.7% | 28.8% | 33.8% |
| Language-Model Realization | 49 | 15 | 30.6% | 31.4% | 30.6% |
| Discussion | 33 | 10 | 30.3% | 29.1% | 36.4% |
| Conclusion (with code availability) | 12 | 1 | 8.3% | 8.3% | 8.3% |
| **Main total** | **514** | **114** | **22.2%** | **23.3%** | **24.5%** |
| Supplement total | 63 | 15 | 23.8% | 21.5% | 27.0% |

**Baseline (same script, arXiv LaTeX sources in `philo/baseline/`):**

| Paper | Sentences | Core share |
|---|---|---|
| Nguyen et al. 2022, Transformer-MGK (main sections) | 221 | 3.2% |
| Vaswani et al. 2017 | 177 | 3.4% |
| Niculae and Blondel 2017 | 180 | 8.3% |
| Cohen et al. 2019, gauge CNN (main) | 243 | 10.3% |
| Tsai et al. 2019, kernel attention | 193 | 10.9% |
| Kim et al. 2021, Lipschitz constant of self-attention | 207 | 15.5% |
| **Baseline median** | | **9.3%** |
| Program companions: GL(K)_extension / GL(K)_gradients | 381 / 149 | 19.2% / 26.2% |

**Repeated scope disclaimers (main unless marked):**

| Disclaimer | Occurrences |
|---|---|
| Covariance does not extend to LayerNorm, MLP, or decoder | 359, 617, 924, 939, 1086, 1171 (6) |
| No common free energy, population model, or FEP | 52, 65, 617, 637, 721, 1171, 1176, Supp 78 (8) |
| One seed, feasibility only, no matched baseline | 52, 1132, 1151, 1157, 1161, 1173, 1183, 1191 (8) |
| Passthrough is not propagation of uncertainty | 637, 937, 1069, 1171, Supp 129 (5) |
| Unit temperature only | 65, 721, 900, 1189, Supp 68, Supp 74 (6) |
| No priority claim | 67, 1169 (2) |

**Manual classification of the 98 sentences in the brief’s scope.** The ranges are the Abstract (11), Introduction (40), Discussion (33), Conclusion 1187-1191 (9), and Supp 78 (5). Categories:
- **P:** states a positive result with its content.
- **A:** announces a result without stating it.
- **I:** an inflated claim.
- **S:** a necessary scope or hypothesis statement.
- **R:** a redundant disclaimer, or a rebuttal of a claim the paper never makes.
- **N:** a content-bearing negative result. None falls in these ranges; the one in the paper sits at 1034.
- **E:** an empirical record.
- **F:** future work.
- **C:** context, definition, roadmap, or precedent.

Sentence indices follow `negcount.py` segmentation:

| Range | P | A | I | S | R | E | F | C |
|---|---|---|---|---|---|---|---|---|
| Abstract | 3 (s3, s4, s7) | 3 (s5, s6, s8) | 0 | 0 | 1 (s10) | 1 (s11) | 0 | 3 |
| Introduction | 3 (s13, s23, s28) | 1 (s34) | 3 (s3, s29, s31) | 6 (s9, s10, s15, s16, s22, s32) | 3 (s11, s14, s33) | 0 | 0 | 24 |
| Discussion | 0 | 2 (s1, s2) | 1 (s14) | 8 (s3, s4, s6, s12, s16, s20, s21, s22) | 10 (s5, s7-s11, s13, s17, s19, s23) | 0 | 10 (s24-s33) | 2 |
| Conclusion | 0 | 1 (s1) | 3 (s3, s4, s5) | 2 (s2, s7) | 2 (s8, s9) | 1 (s6) | 0 | 0 |
| Supp 78 | 1 (s1) | 0 | 1 (s5) | 1 (s2) | 2 (s3, s4) | 0 | 0 | 0 |
| **Total** | **7** | **7** | **8** | **17** | **18** | **2** | **10** | **29** |

This classification is a judgment call. The criteria above and the listed indices make it checkable, and it should be read together with the lexical counts, not in place of them.

**Where the hedges hide the positive contribution.** Five results with real content are either absent from the front matter or appear there only as possibilities:
- The key-norm penalty survives high-dimensional concentration at τ=√r and is not supplied by LayerNorm (1034). This is the paper’s one content-bearing negative result; it sits mid-section and is never mentioned in the front matter.
- The shared-covariance limit is L2 attention in whitened coordinates (987-1007). The abstract instead says “dot-product score with a key-norm bias”.
- The composition defect O_h(T_hO_h−I)T_h, with flatness if and only if T_hO_h=I under rank conditions (564-572). The abstract says only “fail the composition identity”.
- Rank-deficient heads can sum to an invertible routed link (468-474). The abstract says “may have low rank”.
- The reference-moment normal form (1042-1049), which determines exactly where frames can matter. The paper presents it as a “correspondence”.

The necessary scope statements are few. The covariance theorem is for full Gaussian states. The content maps, residual, normalization, MLP, and decoder are declared, not derived. The stored covariance is a static routing state. The run is a single-seed feasibility record. Each can be said once.

## Rewrites (positive result first, scope once)

**R-a. Abstract, sentences 4-6 (line 50).** “Sending and receiving maps compose into matrix-valued links. A routed link has rank at most min(K, Σ_h s_h), so rank-deficient heads can sum to an invertible link; a head composes flatly exactly when T_hO_h=I under the stated rank conditions; and a link of any rank defines a normalized Gaussian channel.”

**R-b. Abstract, sentences 7 and 10 (line 52).** “When projected key covariances are shared, Gaussian-KL routing equals whitened dot-product routing with a key-norm penalty, which is L2 attention in the isotropic case; the penalty is removable only by a state-dependent prior, and neither LayerNorm nor high-dimensional concentration removes it at the conventional temperature. The content maps are the value and output maps of standard attention written in local frames.” Move the free-energy disclaimer to the Scope paragraph.

**R-c. Introduction, line 65.** “The KL divergence between projected query and key Gaussians is the routing cost, and Gibbs routing is its exact entropy-regularized minimizer. The objective selects the routing weights only; the content maps, residual, normalization, MLP, and decoder are architectural choices, listed once in the Scope paragraph below.” If the probability investigator confirms L6, add: “For every temperature, the same weights are the exact posterior of the source label in a normalized model with a binary compatibility record.”

**R-d. After the covariance Proposition, replacing 924 and 939 and consolidating 359, 617, 1171.** “The proof uses only the fact that routing and content depend on the states through the frame-invariant reference moments (ξ_i, C_i). Any operator with this property is covariant in the same sense, including dot-product attention and any coordinate map applied as U_iG(U_i⁻¹·); the covariance is a consistency property of the frame parametrization and does not constrain S_Q, S_K, T, or O. The reported architecture instead applies its normalization, MLP, and decoder in stored coordinates, and that is where the learned frames act: through the token- and position-dependent conjugation U_i⁻¹G(U_i·) and the decoder W_outU_i.”

**R-e. Conclusion (line 1189).** “Gaussian-KL routing between framed Gaussian states is the exact minimizer of an entropy-regularized source-selection objective. With shared projected key covariance it equals whitened dot-product routing with a key-norm penalty that neither LayerNorm nor high-dimensional concentration removes; with source-dependent covariance it adds a per-source metric and pair biases. The attention operator factors through frame-invariant reference moments, so frames affect computation only through the state parametrization and the frame-dependent normalization, MLP, and decoder. Whether those roles improve prediction is an empirical question that the matched comparisons in Section X can decide.”

**Scope paragraph, stated once after the contribution statement.** “Scope. The results concern the attention operator for full Gaussian states. The content maps, residual, normalization, MLP, and decoder are taken from the transformer rather than derived; the stored covariance is a static routing state, not propagated uncertainty; no common free energy is claimed for the whole predictor; and the language-model result is a single-seed feasibility record without a matched baseline.”

## Novelty versus rediscovery (Task 4)

| Component | Canonical counterpart (checked) | Verdict |
|---|---|---|
| Gibbs/softmax as entropy-regularized argmin, prior entering additively | Jaynes-style max-entropy; Boyd; Wainwright (cited); in attention, Niculae and Blondel 2017; as mixture inference, Movellan and Gabbur 2020 | Rediscovery. The paper says so for the calculation but not for attention. |
| Gaussian-KL scoring of token Gaussians | Vilnis and McCallum 2015 (KL energy between learned Gaussian word embeddings, diagonal or spherical); Pro-Attention 2022 (per-token scalar statistics, cited); MGK 2022 (Gaussian-mixture keys) | Precedented in kind. Full reduced covariance under learned, distinct S_Q ≠ S_K appears new (documented search, F4). |
| Shared-covariance reduction to dot product plus key-norm bias | Kim et al. 2021 L2 self-attention (the isotropic case exactly; the anisotropic case after whitening) | The endpoint is a known attention variant. The compensation prior, the perturbation bound, and the concentration counterexample (1034) are useful and, as far as I found, new as explicit statements. |
| Gauge-equivariant attention | Cohen 2019; He 2021 GET (cited); CASK 2025 and L-CNN 2022 (lattice); canonicalization and frame averaging (Kaba et al. 2023; Puny et al. 2022) | The covariance here is the dressing/canonicalization kind (F1), not the constraint kind. No priority is possible or claimed, and the headline should not suggest one. |
| General matrix links, possibly singular, factored through an edge space | Cellular sheaves (Hansen and Ghrist 2019), sheaf neural networks (Hansen and Gebhart 2020; Bodnar et al. 2022), Sheaf Attention Networks (Barbero et al. 2022); Wetterich 2014 (cited) | Sheaves are the closer counterpart, and the program’s own treatise says so. The composition-defect algebra O(TO−I)T is a small new observation. |
| Heads versus irreducible frame blocks | SE(3)-Transformer; GET (cited) | Incremental and correctly positioned. |
| Attention as agent communication | TarMAC 2019; CommNet 2016 | Uncited precedent for the agent reading. |
| Per-token frame tables (90% of parameters) | Sparse per-token capacity: Lample et al. 2019; Huang et al. 2025 | An unusual parametrization. Its value is untested against capacity-matched controls (F2). |

**What is genuinely new, stated narrowly:**
- the full-reduced-covariance projected Gaussian-KL router with distinct comparison maps, and its exact decomposition into a whitened L2 term, a per-source metric, and pair biases;
- the explicit compensation prior, and the demonstration that concentration does not justify dropping the key-norm term at τ=√r;
- the normal form: frames matter only through state parametrization and symmetry-breaking components (derivable from the paper, but not drawn out in it);
- the cogredient comparison-space redundancy, which is not stated in the paper but follows from its own KL invariance (eq. glk_invariance), where that identity carries weight, alongside the complete-state alignment case at 723;
- the rank and composition algebra of O_hT_h links;
- the realization itself, as a feasibility record.

## The paper within the program (Task 3)

**Advances the program.**
- A typed comparison/content decomposition for uncertain framed states, with exact characterization of what Gaussian comparison adds over L2 and dot-product comparison.
- An explicit ledger of what the variational objective selects (routing) and what it does not (content maps, residual, normalization, MLP, decoder). This is a research map of the derivation targets the program still owes.
- If L6 is adopted, an exact probabilistic status for routing at every temperature, stated without overclaiming (F9).
- A codebase that already contains the substantive gauge-constrained alternative (gauge_gate), which the manuscript could turn into a genuine test.

**Undercuts the program.**
- A headline property (covariance) that is automatic (F1).
- Learned frames that do their work inside the imported neural block and decoder, holding 90% of the parameters (F2).
- A static, near-uniform covariance, so agents never revise uncertainty (F8).
- Neural components imported unchanged (F5).
- An empirical record with no severity for any Gaussian- or gauge-specific claim (F2).

**What the framework forbids that a plain transformer does not.**
- (i) Under shared projected key covariance, a sign-definite whitened key-norm penalty at a fixed cross term.
- (ii) Cogredient comparison-space redundancy, where dot-product attention has a contragredient one.
- (iii) In gauge_gate mode, any non-intertwiner nonlinear block.

These are the program’s candidate excess content in Lakatos’s sense. None is currently stated as a prediction or tested.

**Proposed contribution statement (drop-in, falsifiable).** “We characterize Gaussian-KL attention between framed Gaussian states.
(i) The operator depends on the states only through frame-invariant reference moments. It is therefore covariant under independent site-frame changes for any choice of interface maps, and frames can influence computation only through the state parametrization and through components applied in stored coordinates.
(ii) With shared projected key covariance, routing equals whitened dot-product routing with a key-norm penalty, which is L2 attention in the isotropic case. The penalty is removable only by a state-dependent prior and survives high-dimensional concentration at τ=√r. Source-dependent covariance adds a per-source metric and pair biases.
(iii) The Gibbs row is the exact minimizer of an entropy-regularized objective and, at every temperature, the exact source posterior of a normalized binary-record model.
(iv) Routed content links have rank at most min(K, Σ_h s_h), compose flatly exactly when T_hO_h=I under rank conditions, and carry no loop invariants on causal support beyond frame-free self-loop traces.
A four-layer realization reaches 31.04 test perplexity (one seed) as a feasibility record. We specify the matched comparisons that would show whether covariance-aware routing and learned frames improve prediction, and whether frames act through the gauge structure or through symmetry-breaking capacity.”
Item (iii)’s second clause is conditional on the probability investigator confirming L6.

**Predictions, each with a pre-declared failure condition.** Each test is chosen so that it could fail (Mayo 1996 severity).
- **P1. Reduction fidelity (checkpoint-only, cheap).** On rows where projected key covariances are nearly shared, the rowwise L1 distance between Gaussian routing and its whitened-L2 reduction is at most the bound computed from measured key-norm dispersion: e^{2ε}−1, or 2tanh(ε/2) if lead L7 is confirmed. *Fails if* measured distances exceed the bound on uncapped rows. That outcome would show the implementation departs from the theory.
- **P2. Gauge structure or symmetry breaking?** Retrain the coordinate, canonical_frame, and gauge_gate modes at matched tokens, with at least three paired seeds, and declare a margin δ in advance.
  - The gauge-structure reading predicts that canonical_frame is not worse than coordinate by more than δ.
  - The capacity reading predicts that coordinate beats canonical_frame by more than δ.
  - The gauge_gate arm tests whether a substantively constrained nonlinearity is viable at all.
  Every outcome is informative.
- **P3. Frames versus capacity.** Compare learned frames against identity frames plus a capacity-matched sparse per-token table (for example, per-token low-rank adapters or a product-key memory of about 412M parameters) at matched compute, in the spirit of Kapoor and Narayanan 2023. *Fails for the frame reading if* the matched table equals or beats the frames.
- **P4. Covariance-aware routing.** Compare Gaussian-KL routing, L2 routing (mean-only; Kim et al. 2021), and dot-product routing with all else identical, plus a dot-product arm with a learned per-source diagonal key metric. The last arm controls for the static per-source metric the Gaussian router has. *Fails for the Gaussian reading if* the metric-matched arm equals Gaussian-KL routing.
- **P5. The program test.** Replace the GELU MLP by an inference-derived update (the extension’s source/reliability construction, or gauge_gate) at matched compute. The program predicts degradation no larger than a pre-declared margin. *Fails if* the degradation is larger.

## Series organization and the prior review’s R1, R2, R8 (Task 5)

**One thesis per document.**
- **(A) This paper.** Retitle along the lines of “Gaussian-KL Attention on Framed States: Exact Routing Reductions and Matrix-Valued Content Links”. Build a theorem-first spine of four named results, replacing one telescoping Lemma and two Propositions:
  - Theorem 1, the reference-moment normal form, with covariance and self-loop-only loop invariants as corollaries;
  - Theorem 2, the shared-covariance reduction to whitened L2 attention, with the compensation prior, the perturbation bound, and the concentration counterexample;
  - Theorem 3, the exact probabilistic status of the Gibbs row;
  - Proposition 4, link rank and composition plus the cogredient comparison-space redundancy.
  Keep one paragraph typing E_i and U_i. Move the smooth-bundle construction, Fig. 1, the optional prior-bank decoder, and the representation-block detail to the supplement, and merge the duplicated derivations in 2.6 and 3.1 (as R2 also asks).
- **(B) Extension.** Present it as the program paper, “Agent networks without prescribed neuron layers,” with P5 as its empirical claim. Remove “Gauge-Covariant Gaussian Attention” from its subtitle: its covariance (Prop. “Covariance of the complete coordinate construction”) is obtained the same way, by co-transforming the reference law, as its own line 341 concedes. So it gains nothing from the attention paper’s title.
- **(C) Gradients.** Fold it into (B)’s appendix or a technical report. It develops optional full-state belief revision on flat Ω, which the v2 predictor does not use (GL(K)_gradients.tex:45-47), so it should not be presented as the companion of (A).
- **(D) Treatise.** Cite it with a stable identifier, but never as the warrant for a result in (A) or (B). Each paper must prove or externally cite what it uses.

**Verdicts on the prior review.**
- **R1: correct in direction, wrong in headline.** Stating the reference-coordinate identity is right. Keeping “a typed, frame-covariant organization of Gaussian communication” as the contribution is wrong, because covariance is automatic (F1). R1’s frame-attribution caution (an identity-frame ablation changes the effective state family) is right. It misses the decisive arms: dressed versus coordinate versus intertwiner (P2), and capacity-matched tables (P3).
- **R2: agree to reorder; disagree with preserving the principal/associated-bundle foundation in the main text.** The deletion test finds that the foundation does no inferential work here, and it advertises a local gauge freedom the model lacks (F10). R2 also omits the theorem-first spine.
- **R8: agree on accessibility, but insufficient.** A citation to the treatise asserts the same claim twice. The bridge should either cite the textbook source (Blei et al.) or state and prove the treatise theorem it relies on (F9).

**What the prior review missed.**
- the Kretschmann/dressing diagnosis and the Schur reason it is unavoidable (F1);
- the location of the frames’ computational role in the symmetry-breaking components, with the implemented canonical_frame and gauge_gate modes (F2);
- the vacuity of the lattice-gauge conclusion on causal support, and the sheaf counterpart the program’s own treatise uses (F3);
- the L2-attention identity of the reduction, and the Vilnis, Niculae-Blondel, Movellan-Gabbur, and TarMAC precedents (F4);
- the non-distinguishing “neuron-free” claim in its own motivation paragraph (F5);
- quantified misallocated hedging (F6);
- the definitional content correspondence (F7);
- the static covariance and the failed diversity gate (F8, extending C7);
- the evidential weightlessness of exactness at any temperature, and the textbook attribution (F9, extending R5 and R8).

## Placeholders to add or re-prioritize

**T3 (new): retraining arms that test the gauge reading.** Rows:
- coordinate (reported);
- canonical_frame (dressed);
- gauge_gate (intertwiner);
- identity frames plus a capacity-matched sparse per-token table.

Columns: trainable parameters by role, training tokens, measured compute, seeds (paired), test CE per seed, paired CE difference against coordinate with its interval, and the pre-declared margin δ. No values should be entered until the runs exist. T3 carries predictions P2 and P3 and should rank above the optional identity-frame arm in the prior F4/T2.

**F7 (new figure): where frames enter the computation.** Two rows in reference coordinates. The first shows the reported stack, with the four insertion points marked: embedding U⁻¹μ_p, static covariance U⁻¹Σ_pU⁻ᵀ, conjugated block U⁻¹G(U·), and decoder W_outU. The second shows the dressed stack, where only the first two remain. No data are needed. It belongs next to Rewrite R-d.

**Re-prioritize P1 (checkpoint-only) ahead of any retraining.** It is cheap and severe against implementation drift, and it can be added to the prior F3 panel C.

## Leads tested

**L1 (unitary-gauge normal form; lattice-gauge framing): CONFIRMED, and sharpened.** All four roles (a)-(d) are reproduced numerically:
- the reported stack is not covariant (Δlogit up to 6.48);
- the dressed stack is covariant (1.1e-14) and equals a frame-free stack with frames only in the initial state (3.6e-15), so roles (c) and (d) exist only because covariance is broken.

On causal support, all 20 closed walks of length at most 4 (N=5) are constant. Loop invariants therefore reduce to self-loop traces of the standard value/output operator (8.9e-16). “Lattice-gauge structure at the level of link fields” overstates (F3).

**L2 (Kretschmann-type objection): CONFIRMED, and sharpened.** Covariance holds identically for Gaussian-KL routing, plain dot-product routing, and an arbitrary nonlinear dressed map (all ≤5.3e-15). Its content is:
- vacuous in Kretschmann’s sense (Norton 1993 §5.1);
- artificial by François’s criterion (C1), since U_i is a local dressing field built from primary variables;
- unavoidable if the interfaces are to be learned: undressed GL equivariance forces the interfaces to zero or scalars (Schur check: dim 0 and 1).

The principal right action is not a symmetry (7.63). The model’s genuine redundancies are global re-basing (2.3e-14) and per-head cogredient comparison maps (3.0e-15), and neither is named. What the title and abstract can honestly claim is given in the F1 Fix and the proposed contribution statement.

**L3 (static covariance, pair biases): CONFIRMED as to framing.** Static per (token, position) follows from the text (1108, 1119, 1134) and the config. The run’s diversity gate failed (CV 0.047 < 0.10; ρ = 0.145). The quantitative size of the trace and log-determinant contributions was not measured here; that belongs to another lens.

**L5 (parameter redundancy): framing consequence CONFIRMED.** The cogredient GL(r_h) redundancy of Gaussian routing versus the contragredient one of dot-product routing was executed (3.0e-15 against 0.61 for Gaussian; 2.2e-16 against 0.44 for dot product). It is the model’s genuine “gauge” redundancy and is unstated. The conditioning consequences are outside this lens.

**L6 (general temperature via a binary record): framing consequence CONFIRMED numerically** (≤1.1e-16 at τ ∈ {0.3, 1, √32}, capped and uncapped). The probabilistic adjudication is the probability lens’s. The consequence here is that exactness is purchasable for any nonnegative cost and so carries no evidential weight (F9).

**L8 (missing precedents): MODIFIED.**
- Verified against primary records: Niculae and Blondel 2017, Kim et al. 2021 (whose isotropic case is exactly the paper’s Prop. 2 clause), Movellan and Gabbur 2020, Sukhbaatar et al. 2019, Geva et al. 2021.
- Added: Vilnis and McCallum 2015, TarMAC 2019, cellular sheaves (Hansen and Ghrist 2019; Bodnar et al. 2022; Barbero et al. 2022), CASK 2025, L-CNN 2022, Kaba et al. 2023, Puny et al. 2022, Lample et al. 2019, Huang et al. 2025.
- The Pro-Attention distinction at line 67 is accurate.
- Martins and Astudillo 2016 and Gabbur et al. 2021 were not checked in this lens.
- Correction to the brief: Fournel, François, Lazzarini, Masson 2014 is Int. J. Geom. Methods Mod. Phys. 11:1450016 (arXiv:1212.6702), not J. Math. Phys.

**L10 (negations bury the contribution; theorem-first spine): MODIFIED.** “Dominated” is too strong: 77.8% of main-text prose sentences carry no core negation. The rate is nonetheless 22.2%, 2.4 times the median of six published comparators and above their maximum (15.5%). Six disclaimers are repeated 2 to 8 times. The front matter’s deflation takes a different form: it announces results without stating them (7 of 98 sentences in scope), so its lexical rate understates it. Hedging is misallocated: the body is over-hedged while the title and conclusion carry inflated, unhedged claims (F1, F3). The theorem-first spine is supported; four named results are proposed in the series section.

**L4, L7, L9:** outside this lens; no verdict.

## Evidence and reproducibility

All scripts are in `scratchpad/panel/philo/`. They are CPU-only, use `C:/Python314/python.exe` (numpy 2.4, scipy 1.17), and did no GPU work, no Lean, and no tamper tests.
- `negcount.py`: the negation census.
- `baseline/`: arXiv LaTeX sources for the six comparators.
- `kretschmann_checks.py`: the tiny Algorithm-1 model. It covers passive covariance for three operator classes, reported versus dressed stacks, the frame-free equivalence, global re-basing, the local right action, and cogredient versus contragredient comparison maps.
- `loops_and_records.py`: causal closed-walk enumeration, self-loop traces, and the binary-record posterior.
- `schur_check.py`: the dimensions of undressed equivariant interfaces.
- `norton1993.txt`, `francois2019.txt`, `tarmac.txt`, `vilnis.txt`, `arxiv_meta.xml`: primary-source extracts used for quotations.

Data records read, not modified: `D:/DATA_KEEP/31.04_wikitext-103_K256_4-layer_noHM/{config.json, research.json, parameter_motion.json}`. Code read, not modified: `C:/Users/chris and christine/Desktop/VFE_3.0/vfe3/model/block_mlp.py`, `block.py`, `model.py`, `run_artifacts.py`, `viz/extract.py`. The 0.10 threshold of the covariance-diversity gate comes from the current code copy; the archived `research.json` records the failed gate flag itself.
