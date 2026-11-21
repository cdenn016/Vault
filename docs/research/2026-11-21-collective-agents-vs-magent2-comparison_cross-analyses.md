# Cross-cutting analyses (workflow intermediate)

## ANALYSIS: similarities

# Correspondence map: Collective_Agents (CA) and MAgent_Theory_2.0 (MA)

Paths are relative to `Research/manuscripts/`. CA files are in `Collective_Agents/sections/` and MA files in `MAgent_Theory_2.0/chapters/` unless another directory is given. Every item marked "verified" was read in the .tex this session. Items marked "per dossier" come from a reader's summary and were not re-read.

## 0. How the two manuscripts relate (verified)

The dependency runs one way. CA cites MA as `dennis2026magent`, and its bib annote says only ch. 17 and ch. 19 were read (`Collective_Agents/references.bib:1250-1256`). CA cites Item 7 as `dennis2026formation` (`references.bib:1234-1240`). MA cites no CA result. CA states exactly what it imports (13_discussion.tex:53): the update subspace, the meaning-lost decomposition, the holonomy criterion, the frustration corollary, the tangent learned-holonomy model, the declared-selection clauses of the formation standard, and the location-family characterization from Item 7. It also states that "It does not take the geometry" (13_discussion.tex:55).

The two manuscripts are built on different ontologies:
- **CA** has one physical world η. Agents hold Kalman beliefs and select policies by expected free energy. Frames U_i ∈ GL(K) are optional encodings, and true translations are flat.
- **MA** is perceptual only, with no EFE or action. It works with general laws on a context base, and dictionaries are receiver-owned hypotheses whose truth may itself carry holonomy (17_communication_links.tex:53, per dossier).

Most of the overlap below is therefore exact on the linear-code, single-context slice and only analogous elsewhere.

## 1. Same object under different names or notation

| Object | CA location | MA location | Status and notes |
|---|---|---|---|
| Public lossy code; frame; effective code | T_c, U_j, H_j = T_cU_j (02_framework.tex:36-40) | T̄_j^c, U_j, Â_ij = T̄θ̄^{-1} (17:24-48) | Same object. CA's code model Ĥ_ij = T_cΘ_ij^{-1}U_i (s02_framework.tex:280) is MA's effective code read in internal coordinates. |
| Translation / dictionary | Θ_ij ∈ GL(K), receiver's model, true value U_iU_j^{-1} (02:270-277) | θ_ij = U_iθ̄_ijU_j^{-1}, receiver-owned, opposite edges independent (17:34-50) | Same object. In MA the truth may be non-flat. In CA the truth is flat (s06_coherence.tex:69, prop:coh-flat-true). |
| Meaning lost through a code | prop:fw-prior-completion(c): KL(q_j‖q̂)=KL(q_j‖q_i)−KL(T#q_j‖T#q_i) (02:64-83; attributed to MA at 02:85) | it1:loss (17:67-73), noisy bound it1:noisy (17:77-85) | Identical identity, imported and proved in both. |
| Gaussian reception and update subspace | prop:fw-update-subspace (02:52-60), O_ij as a Λ_i-orthogonal projector (02:64-83) | it1:kalman, it1:gaussian-reconstruction oblique projector (17:89-121) | Same computation. CA's attribution at 02:62 is verified. CA's added rank claim "exactly r_c directions" needs Ĥ of full row rank (dossier defect, confirmed at 02:62). |
| Consensus via holonomy | thm:coh-holonomy(a) (06_coherence.tex:72-79, credited to MA; src comment at 06:80) | it1:consensus (17:238-244) | Same theorem. MA states it at law level for bimeasurable bijections. CA restates it linearly. |
| Frustration operator | prop:coh-frustration(a), F(μ)=Σϖ‖μ_i−Θμ_j‖²_{M_i} (06:86-95) | it1:frustration, E(μ)=Σw‖μ_i−θ̄μ_j‖² (17:246-252) | Same quadratic form. CA adds a metric M_i. The acyclic counterexample is shared. |
| Coded consensus sheaf | prop:coh-coded, stalks R^K / R^{r_c}, restrictions T_cΘ^{-1} and T_c (s06:79-85) | Code sheaf H^0 = {u: T̄_e(u_i−u_j)=0} (17:420-434) | Same sheaf family. MA's version is the Lie-algebra (tangent) one with both restrictions equal to T̄_e. CA's carries the translation on the receiver side. |
| Coded comparison cost, receiver-first | Edge energy 𝔈_ij = KL((T_cΘ^{-1})#q^U_i ‖ (T_c)#q^U_j) (s02:281) | def:int-coded-cost, KL(ν_iC_ij ‖ ν_jT_j) (02_interactions.tex:162-168) | Same functional with the same argument order. CA's form is the special case C_ij = T_cΘ^{-1}. |
| GL(K) defect with no conjugation invariant | s06:73 (cites MA) | Covariance-dressed defect Q(H;Σ) (02_interactions.tex:272-283; 17:254-263) | CA leaves a GL(K) frustration metric open. MA already supplies one. |
| Lumpability | def:met-lumpable, thm:met-abstract-physics(e) (10a_meta_agents.tex:114-138) | inh:finite-lumpability (05_inheritance.tex:439-450) | Both are Kemeny–Snell strong lumpability, P A = Ā P. |
| Minimal closed extension / coarsest exact parent | thm:met-abstract-physics(f): row space of the observability matrix (10a:136) | inh:canonical-parent: π(x)=(Q(F^n x))_n, Hermann–Krener (05_inheritance:543-627, per dossier) | Same idea. CA's version is the linear-Gaussian special case. |
| Mean-pool closure only for Gaussian families | rem:agy-location-family (cited at 13_discussion:53) | it7:characterization (Item_7_formation_feedback.tex:210-214) | Imported result. |

## 2. Analogous but not identical

**Code stabilizer vs. energy symmetry group.** MA's Stab_G(T̄) = {g: T̄g = T̄} has dimension K(K−r) (it1:identifiability, 17:143-158). This is exactly the kernel subgroup in CA's prop:fw-energy-symmetry(c) (s02:286). CA's sender-side symmetry of the energy is the larger parabolic group GL(K)_{ker T_c}, of dimension K²−r_c(K−r_c), which maps onto GL(r_c) as public recoding. So MA's identifiability group sits inside CA's symmetry group: the extra GL(r_c) acts on public coordinates and changes nothing MA identifies. CA's prop:fw-frame-identifiability gives the matching count K(K−r_c) for frames (s02:208) and credits the pooled-modality refinement to MA (s02:210). MA's result assumes the receiver knows the sender's reference code (17:144). CA's counts concern the sender's frame given T_c, which is a different unknown with the same dimension.

**Pair energy vs. communication energy.**
- CA proves 𝔈 = Σϖ KL(q^U_i ‖ Θ#q^U_j) only at full rank on noiseless channels, and shows it is not of that form on any other channel class (prop:fw-full-rank-energy, 02:290-301; prop:fw-consensus-form). CA identifies this with the pair energy of `dennis2026participatory` (02:303), not of MA.
- MA's analogue is the peer term β_ij KL(q_i ‖ q_jK_ij) of the reciprocal potential, with Gibbs rows as weights (03_dynamics.tex:42-56, per dossier).
- Differences: CA uses fixed weights ϖ, not Gibbs rows. CA's energy is not an objective (13_discussion:55), whereas MA flows down its potential. CA's q̂_ij depends on q_i, so it is not the prior of a fixed model (dossier defect, 02:129).

**Learned holonomy.** CA's frustration comes only from learned-translation error (prop:coh-flat-true). MA's it1:learning separates detectable dissonance ‖Q_D Bω‖² from dissonance hidden in N∩ker B (17:292-403, per dossier). CA imports part (ii) of it1:learning (app06_coherence.tex:87) without carrying over MA's describer-level, global-posterior standing (per dossier, 17:311, 507).

**Hub/flat translations vs. pure gauge.** CA's ext5 thm:lrn-path(c) hub design Θ = g_ig_j^{-1} is flat and gives the frames U_iΥ_i. MA calls links of this form pure gauge (06_fusion.tex:142-144, per dossier), and in MA's tangent theory flat truths are identified up to sections of H^0 (it1:exact-flat). CA's "gauge freedom" in thm:lrn-gauge is G_F = {T ∈ O(K): TF=FT}, an identifiability symmetry of the content law. It is not MA's structure group. Same word, different object.

**Blindness to common error.** CA's lem:mis-social-blind (03_misreading.tex:120-125, verified) says a shared additive error is invisible to social innovations. MA's it2:gauge (18_link_dynamics.tex:66-84, verified) says records cannot separate belief change from reinterpretation: the null space 𝒢 projects onto all belief displacements. Both are invariance statements of comparison records. CA's is a translation along the diagonal at correct codes. MA's mixes beliefs and dictionaries. Neither proves the other.

**Double counting and echo.**
- CA counts double-counting in literal reading: prop:hie-literal-once has overconfidence factor below 2 and MSE ratio at most 9/8 (10b_hierarchy.tex:43-58, verified). Recirculation through records gives growth like t, t/n or n^t (tab:hie-records). There is also the overvaluation family of §3.
- MA's it2:echo (18:203-217, verified) compares four recognitions on a loop. Per-agent law-level recognition over-counts loop information, and cavity recognition equals the exact posterior.
- The structure is the same in both: the cavity / leave-one-out prior is the exact repair (CA thm:hie-messages; MA it2:echo(iv)). The settings differ: CA's message passing is Gaussian belief propagation on trees over the world state, while MA's loop is over dictionary coordinates.

**Top-down action.** MA's gf:top-down (05_global_formation.tex:476-509, verified) proves the following for the global VFE. The mean-field top-down factor uses o_i, so it is not the cavity prior. At the Gaussian fixed point the posterior means are exact and the variance is under-estimated. CA's rem:hie-gauge (s10b_hierarchy.tex:116-118, verified) asks whether MA's top-down feedback removes the child's own contribution. See §4 for why CA's question rests on a description that does not match MA.

**Pooling.**
- CA's prop:agy-pooling (05_agency.tex:110-118, verified): the exact union is the prior-corrected logarithmic pool. A product of posteriors counts the prior n times.
- MA's it3:rigid (19_curvature_hierarchy.tex:205-224, verified): the parent self density is p_A ∏p_i, a logarithmic pool with unit weights, P_A' = P_A + ΣP_i.
- MA pools self densities and keeps the records as separate bridge factors, so CA's prior-overcount criticism applies only if MA's p_i already contain each child's evidence. MA does not say whether they do. This is a concrete reconciliation point.
- Item 7's shared label is a Gibbs row at temperature T/n of the linear pool (it7:pool, Item_7:128-147, verified). That is a linear pool, not CA's logarithmic one.

**Attention.**
- CA attention is a softmax over κ-sets at policy precision γ of the epistemic EFE (07_formation.tex; prop:mis-believed-values).
- MA routing uses Gibbs source rows over KL costs at temperature T, and T = 1/n appears as a message-count posterior (it1:bandwidth, 17:270-281, verified; thm:dyn-registered).
- These are analogous selection mechanisms with different objectives. Neither manuscript derives one from the other.

**Formation standard** (verified at CA 07_formation.tex:10-20 and MA 05_inheritance.tex:1676-1690, 1812-1936):
- CA (T1)-(T3) correspond to MA (F1)-(F2): the selection chain and admissible levels.
- CA (T4) "differs from type-D nulls" corresponds to MA (F5).
- CA (T4) "survives type-S" (exact fusion) and partner randomization have no MA counterpart.
- CA (T5) (reached from the declared start) is close to MA's persistence clause in (F2).
- MA (F3) inherited parent, (F4) compression and (F6a/b) recursion with a counterfactual class have no CA counterpart. CA's meta-agent clauses (closure, agency) are graded separately (def:agy-meta-agent).

## 3. Where one manuscript proves what the other assumes or leaves open

- **MA proves, CA lists as open:**
  - A GL(K) loop-defect metric: MA prop:int-loop-defect vs. CA open:coh-frustration-metric (s06:72-74).
  - The top-down mechanism under a global VFE: MA gf:top-down vs. CA rem:hie-gauge "not settled".
  - The Gaussian-only characterization of pooled closure: it7:characterization, which CA imports.
- **CA proves, MA lacks:**
  - The weakly connected / spanning-tree extension of the holonomy criterion: thm:coh-holonomy(b).
  - Cycle spectra and two-sided frustration bounds: prop:coh-frustration(b,c).
  - A counterexample showing that holonomy does not characterize coded consensus: prop:coh-coded(b), three-cycle with Cons=0 and dim H^0=3.
  - That the consensus-form energy exists only on noiseless full-rank channels, with a rate on noisy ones (prop:fw-consensus-form, prop:fw-noisy-energy). MA's coded cost (prop:int-coded-cost) gives only the bound and the conditional gap.
- **MA assumes, CA proves conditionally:** MA's identifiability assumes a known reference code (17:144, "essential", per dossier). CA's grounded code identification (prop:fw-grounded-identification) gives a limit for least-squares code estimates under content calibration, and ext5 thm:lrn-gauge gives the orbit H·G_F for ungrounded learning. Together these give a partial route to the shared-language hypothesis that MA calls open (17:515-516).
- **Both open, both negative:**
  - Neither manuscript exhibits a formation that meets its own standard.
  - CA: the split fails the translation-aware exact-fusion null (prop:frm-exact-fusion); no meta-agent instance exists (open:agy-meta-agent-exists).
  - MA: no construction meets (F1)-(F6) (inh:formation-open). Global formation fails (F5) (split) and (F6b).
  - Both identify interaction necessity as the weakest link. CA's frozen control and MA's ch13 frozen control both reproduce the grouping (MA pa:selector-threshold, per dossier).

## 4. Reader errors and cross-manuscript defects found while verifying

1. **The null families do not match, despite shared names.** Two readers (CA-collectives-agency, MA-formation-inheritance) say CA's 𝔑_lp, 𝔑_rn, 𝔑_fr "are the N1/N2/N3" of MA. They are not the same interventions.
   - CA 𝔑_lp: "each inter-agent channel delivers pure noise; slots, capacities and assigned precisions kept" (05_agency.tex:345). 𝔑_rn reassigns the deleted capacity (05_agency.tex:346).
   - MA N1 deletes every peer cost and keeps labels, priors and temperatures. N2 also removes the labels, so the self weight is 1 (05_inheritance.tex:1676-1706).
   - CA's noise channel keeps assigned precisions, so receivers still fuse noise. MA's deletion removes the cost term.
   - The intent is analogous, but verdicts under one family do not transfer to the other.
2. **CA describes a mechanism that MA's text does not contain.** CA rem:hie-gauge (s10b:116) and 13_discussion.tex:53 describe MA's top-down feedback as a child prior set from the parent's transported belief "with a blend factor", with the parent a "barycenter" of children. A grep of `MAgent_Theory_2.0/chapters/` and Item 7 finds neither "blend" nor "barycent". MA 2.0's top-down action is the mean-field factor of a hierarchical global VFE (gf:top-down). CA's own text says the description comes from "secondary descriptions". The comparison targets a construction outside MA 2.0, possibly VFE_3.0 code; I did not check where it comes from.
3. **The CA-RG reader's claim of a "different verdict" needs qualifying.** The reader says MA's gf:top-down gives "a different verdict" from CA's literal reading. The two results concern different objects:
   - CA's literal reader reuses the parent's full posterior as an independent prior, which is a misspecified update.
   - MA's factor is a coordinate-descent step of one normalized VFE, whose fixed-point means are exact.
   - They do not contradict each other. MA's result shows that its mechanism is not CA's literal reading, at least in the means.
4. **The pair energy is not MA's.** CA's full-rank identity is attributed to `dennis2026participatory`, not MA (02:303, verified). The CA-framework reader's gloss "pair energy of the author's gauge manuscripts" is loose. MA's matching term is the reciprocal-potential peer cost and the coded cost (02_interactions:162-168), which share the receiver-first order.
5. **Argument orders differ by role.** MA's it1:loss is KL on the sender's law (information lost). CA's 𝔈_ij is KL(q_i‖q̂_ij) on the receiver's law, an energy. Both appear in CA (prop:fw-prior-completion(c) vs. def:fw-comm-energy), so the identification with MA must state which one is meant.
6. **Imported theorem with a different standing.** CA's learned-holonomy invisibility uses MA it1:learning(ii), which MA frames at the describer level (per dossier; I did not re-read 17:311, 507).

## 5. Unification hooks, with locations

- **(a) Parabolic reduction of the structure group.** Below full rank, CA's proved sender-side symmetry GL(K)_{ker T_c} (s02:277-289) is the natural reduced structure group for MA's code sheaf. MA's Stab(T̄) is its kernel. A gauge-theoretic CA would use the parabolic group, not GL(K).
- **(b) Exact pooling at the parent.** CA's information-form, prior-corrected pool (prop:agy-pooling; prop:met-consensus-filter) and MA's ch19 rigid restriction and Item 7 linear pool should be reconciled through it7:characterization. Exact closure forces the Gaussian family, which is where CA lives.
- **(c) A common null family.** Unifying the two formation standards requires one null family. CA's type-S exact-fusion null is the clause MA lacks, and MA's (F3), (F4) and (F6) are the clauses CA lacks.
- **(d) Drifting frames.** CA names "drifting frames" (conj:frm-drifting-frames, 13_discussion:55) as the meeting point. MA ch15 proves that no locally gauge-invariant contextual energy diffuses frames (15_contextual_coupling.tex:633, per dossier). That result bears directly on the conjecture and is currently uncited by CA.


## ANALYSIS: differences

# Collective_Agents (CA) vs MAgent_Theory_2.0 (MA): substantive differences and incompatibilities

**Verdict.** The two manuscripts make different modeling commitments: a world, a gauge reading, an objective and an ontology. They are not two versions of one theory. I found one place where their claims cannot both hold as written: a stale cross-reference (C1 below). A second clash looks like a contradiction but is a difference of definitions, not of facts (C2). Everything else is a difference of scope or definition, and none of it is a logical conflict. I checked the key dossier claims against the .tex directly. The reader summaries are accurate except for one overstatement, about the meaning of "gauge" (section 5).

Path prefixes: `CA/` is `Collective_Agents/sections/`, `MA/` is `MAgent_Theory_2.0/chapters/`.

## 1. Modeling commitments

| Axis | CA | MA |
|---|---|---|
| World | One shared physical world η, which every generative model describes (CA/13_discussion.tex:55) | No physical world. Contents are represented possibilities over a supplied context base (MA/01_foundations.tex:18-25) |
| Law class | Linear-Gaussian throughout. Only the prior-completion and reception identities are stated on general Borel spaces (CA/02_framework.tex:64-127) | General laws on standard Borel spaces with DQM or chart hypotheses. Gaussian laws are only a computational case (AUTHORING.md:29) |
| Time | Discrete rounds. A Kalman/level-0 recursion e(t+1)=We+ζ | Continuous-time Fisher (Shahshahani) gradient flows. Records arrive as discrete assimilation events. Ch. 05_global_formation uses discrete coordinate-descent sweeps |
| Objective | Per-agent one-step expected free energy, with no team objective (assumption A5, CA/01_introduction.tex:218). Beliefs update by exact or misspecified filtering. The communication energy is explicitly not an objective (CA/13_discussion.tex:55) | Three separate perceptual objectives: global VFE (declared primary, MA/03_dynamics.tex:6), per-agent mixture-source VFE, and the reciprocal law potential. There is no action, policy or EFE (MA/01_foundations.tex:208) |
| Agent | A Markov-blanket node: sensory, active (attention, speech, records, performative acts) and internal states | A section ζ_i of an associated statistical bundle: belief and model laws, frame, records, source rows |
| Message | Coded noisy linear read H_j m_j+ν, with H_j=T_cU_j, received at level 0, level 1 or by exact fusion | A communicated law ν_jK_ij through a normalized Markov channel, or a sampled posterior predictive (interacting_memory appendix) |
| Collective | A region of spectral contrast r(C) on the world-conditional precision above a declared baseline (CA/04_collectives.tex:214-220). A meta-agent adds closure, null and agency clauses (CA/05_agency.tex:379-381) | A retention R_I that inherits laws, dynamics, responses and channels (the inherited-parent clauses L, D, B, C, G), graded by (F1)-(F6) (MA/05_inheritance.tex:1812ff.) |

CA's active-inference identity enters none of its proved collective theorems except the formation mean-field map. Every network result assumes fixed or exogenously scheduled gains (CA/02_framework.tex:315; CA/01_introduction.tex:312). MA has no actions at all. So neither manuscript proves anything about collectives under endogenous policy selection. In CA the gap sits between the definitions and the theorems; in MA it is absent from the model.

## 2. Gauge structure

The two manuscripts interpret the same symbols differently.

- **CA.** Frames U_i∈GL(K) are optional private encodings. A translation Θ_ij is the receiver's model of U_iU_j^{-1}. The true translations are flat, so "holonomy measures learning or model error, not the curvature of a connection" (CA/13_discussion.tex:55; CA/06_coherence.tex:84, prop:coh-flat-true). Nonzero frustration therefore always signals an error.
- **MA.** Frames act as a dressing field. Passive covariance constrains nothing, and the real symmetry is active equivariance under a common reference change (MA/01_foundations.tex:87). Dictionaries θ̄_ij are receiver-owned hypotheses. Identifying the bundle frames sets θ̄=I, and "a dictionary with nontrivial holonomy is an additional edge field rather than a relation between frames" (MA/17_communication_links.tex:53). Nothing forces the true dictionaries to be flat. Ch. 17 separates detectable from undetectable dissonance by code stabilizers.
- **Base connection.** MA ch. 15-16 build curved base connections over a context base: the R² witness, link-only SO(3) curvature, and an orthogonal-holonomy corollary (MA/16_link_base_transport.tex:225-274, 339-362). CA has no context base, so it has nothing that corresponds.
- **What the gauge structure does.** In MA it does no dynamical work in the formation chapters (MA/10_boundary_closure.tex:4). No locally gauge-invariant contextual energy diffuses frames (MA/15_contextual_coupling.tex:633). In CA, frames matter only through mistranslation Υ_ij and the sender-specific codes T_cU_j.

**Shared core (proved in CA).** At full rank on noiseless channels, CA's communication energy equals Σϖ_ij KL(q^U_i‖(Θ_ij)_#q^U_j), the pair energy of the participatory manuscript (CA/02_framework.tex:290-303, verified). Below full rank, or on any noisy channel, the energy has no such form, and the local symmetry at the senders reduces to the stabilizer GL(K)_{ker T_c} (CA/s02_framework.tex:223-289). MA reaches the same algebraic fact from the identifiability side: a code identifies a dictionary only modulo Stab_G(T̄) (MA/17_communication_links.tex:143-160).

## 3. Rigor and scope

- **CA.** Most explicit theorems are proved inside linear-Gaussian models. The headline hypotheses are mixed. H1 is assembled from clauses proved under separate hypotheses, and no instance of a meta-agent exists (CA/00_abstract.tex:4; CA/s05_agency.tex:275). H3 is proved only for a two-group mean-field map at γ=∞ from a start that is already the split (CA/07_formation.tex:145, 286). H4 consists mostly of upper bounds.

  Several conclusions rest on numerics or self-reviewed notes that the .tex does not include:
  - a false conjecture stated in the text, conj:coh-walls (CA/app06_coherence.tex:210-212);
  - conj:sca-common-code and conj:agy-synchronous, which `docs/research/` notes claim are resolved or refuted;
  - extension-1 check scripts that are not in the manuscript folder (CA/chkext1_apx.tex:8).

- **MA.** Many results are classical criteria restated with exact hypotheses, in a broader law class. The constructive formation results are weaker than CA's:
  - The Ch. 12 routing theorem is nonconstructive, with T unquantified (MA/12_open_formation.tex:250-256).
  - The classification of the global-formation instance rests on unvalidated double-precision computation at one point (MA/05_global_formation.tex:631-660).
  - The subcritical-pitchfork sign depends on a 0.2% cancellation with no check artifact (MA/18_link_dynamics.tex:621-630).
  - The README still says "no objective is primary" (README.md:20), against MA/03_dynamics.tex:6.

- **Formation verdicts.** Both manuscripts reach the same negative result. CA's split fails the translation-aware exact-fusion null and is attributed to misreading (CA/07_formation.tex:286). MA's global construction fails (F5) because the label-preserving null reproduces its sequence, and also fails (F6b) (MA/05_global_formation.tex:662-743). The Ch. 13 grouping is reproduced by the frozen-environment control (MA/13_per_agent_inheritance.tex:202-212). Neither manuscript proves that interaction is necessary for formation.

## 4. Incompatibilities and contradictions

**C1. Top-down feedback: the cross-references disagree (a real staleness defect).**
- CA says the gauge program sets "a child's prior … from the parent's belief transported into the child's frame with a blend factor", "as secondary descriptions of those documents state it" (CA/s10b_hierarchy.tex:117). It leaves open whether the double count persists (CA/12_related.tex:63; CA/13_discussion.tex:53).
- MA's current text gives a different mechanism. In gf:top-down the parent acts through the mean-field geometric-mean factor, which uses o_i, not a blend factor. Its Gaussian posterior mean equals the cavity mean at the fixed point, and only the variance is understated (MA/05_global_formation.tex:476-509, verified).
- CA's literal-reading analogue predicts a biased MSE and an overconfidence factor below 2 (prop:hie-literal-once).
- So CA's description of MA's mechanism does not hold for current MA. The question CA marks open is answered for the Gaussian global-VFE case, with a different verdict: no mean bias, only variance underestimation. The CA bib annotation shows that only MA ch. 17 and 19 were read (references.bib:1255). This explains the drift.

**C2. Status of curvature (a clash of definitions, not of fact).** CA's claim that "true translations are flat" (CA/13_discussion.tex:55) and MA's claim that dissonant dictionaries are a legitimate edge field (MA/17_communication_links.tex:53) assign different meanings to "true". In CA the truth is U_iU_j^{-1} for encodings of one world. In MA nothing supplies a ground-truth dictionary beyond the bundle identification. The two claims cannot both serve as the semantics of one unified theory, and a unification has to choose one. CA's reading is the special case in which a common world fixes the truth.

**C3. Coherence of the null families.** CA reuses MA's N_lp, N_rn and N_fr (CA/07_formation.tex:201, verified) and adds partner randomization and an exact-fusion "survive" null. MA has neither. CA's (T1)-(T5) drop MA's (F3) inherited parent, (F4) compression and (F6) recursion (CA/07_formation.tex:12-20 vs MA/05_inheritance.tex:1812-1936).
- Consequence 1: a "formation result" in CA is not an "inherited recursive formation" in MA, and the reverse also holds.
- Consequence 2: CA selects by a contrast threshold at a declared r_0. MA ch. 06 shows that a threshold selector can reproduce the null tree, while exact equality passes (F5) trivially (MA/06_fusion.tex:876-894). That threatens CA's (T4) more than CA acknowledges.

**C4. Frame representation and covariance.** CA's level-2 formation event exists or not depending on whether the default translation is shifted along with the frames. With the default held at 0, the relabeling δ_c=−θ_c removes the event (CA/ext2_rfm.tex:113-120, verified). In MA's terms (MA/01_foundations.tex:87), this is a rule not written in reference laws, so it is not actively equivariant. The two manuscripts do not contradict each other here, but CA's mechanism fails MA's covariance standard unless the default transforms.

**C5. Pooling and exact closure.** These agree, and the agreement is a bridge. MA Item 7's characterization (it7:characterization) states that universal pooled closure forces a Gaussian sufficient statistic. CA imports this result (CA/13_discussion.tex:53, "rem:agy-location-family") and builds H5a on sum-preserving consensus. That consistency also confirms that CA's exact meta-agent results cannot extend beyond Gaussian location families in this form.

## 5. Shared terms used inconsistently

- **"Meta-agent" / "parent".** In CA this is a five-clause graded definition (contrast, closure, D-nulls, S-nulls, agency index). In MA it is a retention that satisfies L, D, B, C, G plus (F1)-(F6). The two definitions share no clause one for one. CA's closure clause (a Mori-Zwanzig memory defect) and MA's (D) (exact intertwining) come closest, but CA grades closure by a tolerance, while MA requires exactness, and its graded notion is still open (MA/05_inheritance.tex:1891-1894).
- **"Gauge".** *Reader error:* the CA-ext2-8 dossier says the ext5 "gauge freedom" G_F is "distinct from MAgent's structure-group gauge". MA in fact defines "gauge" relative to an observable algebra (MA/01_foundations.tex:91-94), and uses exactly that sense for code-stabilizer non-identifiability (MA/17_communication_links.tex:160, verified). CA's thm:lrn-gauge (CA/ext5_lrn.tex:72-76) is therefore consistent with MA's observable-algebra usage. The clash is only with the structure group G of MA's bundle. MA itself overloads the word in both senses, so the inconsistency sits inside MA.
- **"Collective".** CA uses it for a contrast-selected region. MA uses it for the n-tuple at a context, or for the "collective connection" (MA/02_geometry.tex:194-260). The term is not interchangeable.
- **"Receiver map".** CA takes the name from MA but factors it as lift×decode, with O_ij as its noiseless limit (CA/02_framework.tex:85). This is a cosmetic difference.
- **Communication energy vs reciprocal potential.** CA's E_ij=KL(q_i‖q̂_ij) is in receiver order, and its reconstruction depends on q_i. MA's ch. 17 loss is KL(q‖q̂) on the sender's law. The argument order and the role differ.

## 6. Cosmetic (notation) differences

Θ_ij (CA translation) vs θ̄_ij / Θ_ij / Ω_ij (MA dictionary, link, reciprocal part). T_c vs T̄_j^c. ϖ_ij as fixed weights vs β_ij Gibbs rows. Ω_int (CA interaction order parameter) collides with MA's Ω_ij transport. Both manuscripts overload symbols internally (ϖ, Φ, Ψ, h, 𝒱, B, 𝒞). These collisions are cosmetic but block a merged notation table.

## 7. Is unification feasible?

A unification is feasible only as an embedding, with CA as a special case of MA's descriptive layer.

**What maps across:**
- Fix one world, take flat true dictionaries, and use linear-Gaussian laws.
- The per-agent VFE of MA's discrete-time variant would then correspond to CA's filters.
- CA's full-rank communication energy would equal MA's reciprocal pair term with fixed rows.

**What does not:**
- MA has no action or EFE, so CA's H2 ("communication as action") has no MA counterpart.
- CA has no context base, so MA ch. 15-16 have no CA counterpart.

**Concrete hooks, with proofs on at least one side:**
1. The Stab_G(T̄) / GL(K)_{ker T_c} identification above.
2. MA's covariance-dressed loop defect Q(H;Σ) (MA/17_communication_links.tex:272-283), which could fill CA's open GL(K) frustration metric (CA/s06_coherence.tex:72-74).
3. Gaussian pooled closure (C5).
4. The cavity vs mean-field top-down comparison (C1).
5. MA's Gaussian information-form product-tilt closure (interacting_memory appendix) next to CA's double-counting results.

The obstacles are the incompatible formation standards (C3) and the semantics of curvature (C2). A unified paper would have to adopt a single null family, a single selector rule (threshold vs exact), and a single definition of true transport.

**Priority of fixes:**
1. C1: update CA's description of MA's top-down action against gf:top-down.
2. Reconcile (T1)-(T5) with (F1)-(F6), or state explicitly that they are distinct standards. CA currently cites dennis2026formation as its source (CA/07_formation.tex:10) while dropping three of its clauses.
3. Record the flat-vs-dissonant truth convention (C2) in both texts.
4. Propagate the untracked `docs/research` resolutions (conj:coh-walls, conj:sca-common-code, conj:agy-synchronous) and fix MA's README primacy statement.


## ANALYSIS: unification

# Can Collective_Agents and MAgent_Theory_2.0 be unified?

## Verdict

**They unify as a special case, but only partly exactly.** Take MAgent_Theory_2.0 (MA) as the base. Collective_Agents' (CA) kinematics then embeds into MA's code/dictionary sector exactly. That covers codes, frames, translations, the communication energy, identifiability, holonomy and the code sheaf. Under the embedding CA is the specialization with linear-Gaussian laws, G = GL(K), one shared world latent and a flat (coboundary) true dictionary. The dynamics and objectives do not unify exactly:
- CA's agents filter with Kalman updates and choose attention by one-step expected free energy (EFE).
- MA's agents are purely perceptual, following Fisher flows of three free-energy/potential objectives, with no actions and no EFE.

Of those, only the per-agent and global-VFE pictures on the static linear-Gaussian mean slice can be matched exactly, and that match still has to be proved. The two formation programs share a negative verdict and part of their null family. They can be merged into a common standard, but neither supplies a construction that the other would accept as a formation.

I did not use the reverse direction (CA as base) because CA has no group action on beliefs, has no counterpart of MA's non-flat true dictionaries, and treats holonomy only as error (13_discussion.tex:55). It cannot express MA's general-law, non-Gaussian, dissonant-truth content.

## 1. Exact correspondences, checked against the .tex

| CA object | MA object | Status |
|---|---|---|
| Public code T_c, frame U_i, effective code H_j = T_cU_j; code model Ĥ_ij = T_cΘ_ij^{-1}U_i (02_framework.tex:270-277) | Reference code T̄_j^c, receiver-owned dictionary θ̄_ij, effective code Â_ij = T̄θ̄_ij^{-1}, displayed form Â U_i^{-1} (17_communication_links.tex:24-48) | **Exact.** Identify CA's internal coordinates μ = Uη with MA's reference coordinates, Θ_ij with θ̄_ij, and the true translation U_iU_j^{-1} with a coboundary truth θ̄*_ij. Then Ĥ_ij = Â_ij U_i. |
| Frames are identifiable only modulo {X: T_cX = 0}, of dimension K(K−r_c) (prop:fw-frame-identifiability); kernel of GL(K)_{ker T_c} → GL(r_c) (s02_framework.tex:277-289, part c) | Stab_{GL}(T̄), dimension K(K−r) (17:143-158, part iii) | **Exact.** The same subgroup {g: T_c g = T_c}. |
| Meaning lost: KL(q_j‖q̂) = KL(q_j‖q_i) − KL(T#q_j‖T#q_i) (02_framework.tex:78-82) | it1:loss (17:67-73); cor:pythagorean | **Exact.** CA attributes it to MA (02_framework.tex:85). |
| Communication energy E_ij = KL(q_i‖q̂_ij) = KL(Ĥ#q_i‖H_j#q_j) (lem:fw-reception-identity, 02_framework.tex:109-118) | Coded comparison cost D^cod_ij = KL(ν_i C_ij‖ν_j T_j) (def:int-coded-cost, 02_interactions.tex:162-168) | **Exact, and stated in neither manuscript.** Set C_ij = Ĥ_ij and T_j = H_j with noiseless channels. CA's prop:fw-full-rank-energy (consensus form at full rank) is then the equality case of MA's prop:int-coded-cost(ii) bound D^cod ≤ KL(ν_i‖Θ#ν_j). |
| Consensus ⇔ holonomy invariance; frustration (thm:coh-holonomy, prop:coh-frustration) | it1:consensus, it1:frustration (17:238-252) | **Exact.** CA imports these and extends them to weakly connected graphs. MA has not taken the extension back. |
| Coded consistency = H^0 of a cellular sheaf (prop:coh-coded) | Code sheaf H^0 (17:422-434); H^1 quotient (ch19) | **Exact.** Same sheaf. |
| Hub translations g_ig_j^{-1} are flat (thm:lrn-path(c), ext5) | Pure-gauge links (06_fusion.tex:142-145) | **Exact.** |

**Consequence.** CA's below-full-rank symmetry result (prop:fw-energy-symmetry(b): the local symmetry breaks at senders to the parabolic subgroup GL(K)_{ker T_c}) is a theorem about MA's coded cost. It says the gauge group of MA's reciprocal potential with coded channels is not GL(K)^V but a product of parabolic stabilizers. MA currently states only the observable-algebra form of this point ("gauge relative to coded messages", 17:160).

## 2. Correspondences that hold only on a slice, or need a proof

1. **CA exact fusion vs MA global VFE.** CA's exact Bayesian inference on full data (prop:mis-exact-no-echo, 03_misreading.tex:192-197) should coincide with the posterior of an MA global model in which a single world latent η plays the role of gf's block latent (05_global_formation.tex:52-90) and each agent's sensory and message records are single-agent records ℓ_i. In the static Gaussian case this is very likely exact, since both are Lindley-Smith/Kalman posteriors, but no theorem states it. Two cases need care:
   - Messages that carry posterior means, which is CA's attenuated code, lem:mis-attenuation.
   - MA's protocol, where messages are posterior samples rather than means (interacting_memory, imem:protocol).

   Under MA's protocol the exact receiver likelihood differs from CA's. MA's own example shows that posterior samples and direct sensors share marginal variance but differ in cross-covariance (imem:scalar-calibration).
2. **CA literal receivers vs MA per-agent picture.** In a static world with frozen rows, MA's per-agent mean flow has fixed point (I+L̃^out)μ = a, and it equals a global posterior mean iff the rows are reversible (thm:dyn-three-limits(iii)-(iv), 03_dynamics.tex:562-577, verified). CA's literal level-1 consensus gives eigenvector-centrality weighting and is exact iff the prior is flat and the graph regular (prop:agy-literal-consensus). Both say that dropping the source back-action misweights evidence unless a symmetry condition holds. The mapping is exact only if CA's level-0 fixed-gain recursion is shown to be the explicit-Euler discretization of MA's per-agent Fisher flow on the mean slice with F = I and Q = 0. That is plausible but unproved. With F ≠ I and process noise, MA has no counterpart at all, because MA has no exogenous world dynamics.
3. **Attention.** CA attention is a softmax over κ-subsets of the epistemic EFE, with value −I(η; y_J) (prop:fw-efe-communication). MA rows are Gibbs in KL costs at temperature T, and T = 1/n is derived from message counts (it1:bandwidth; thm:dyn-registered). The two differ: CA's value is submodular mutual information, while MA's cost is a per-source divergence. The relation is interpretive only.
4. **Reciprocal potential vs CA energy.** CA says explicitly that E is not an objective (13_discussion.tex:55). MA's reciprocal potential is that energy (receiver-first KL, def:dyn-potential, 03_dynamics.tex:42-56) used as a gradient-flow objective. MA proves it is not a finite global VFE under fixed positive rows (prop:dyn-no-global-vfe). CA's remark (02_framework.tex:129) that E has "the argument order of the complexity term" is therefore at most an analogy. MA's result shows it is not exact.

## 3. Proposed common framework

**Base (MA).** Agents are sections of P ×_G Prob(V × M), with G ⊆ GL(K). Communication uses MA's code/dictionary sector:
- receiver-owned θ̄_ij;
- codes T̄^c, with a shared-language hypothesis;
- the coded cost D^cod;
- the code sheaf.

Add one ingredient MA lacks: a **common world latent** η with exogenous dynamics F, in a global generative model. MA's content-law and global-formation machinery admits this latent (prop:content-law; gf:model).

**Embedding Φ of CA into the base:**
- G = GL(K), with all laws Gaussian;
- reference coordinates = CA internal coordinates, with true θ̄* = U_iU_j^{-1} (flat);
- CA's Θ_ij becomes MA's θ̄_ij, and CA's T_c becomes T̄ for every sender (a shared language);
- the world latent is CA's η, with CA's F and Q;
- CA's exact fusion becomes posterior inference in the global model;
- CA's levels 0 and 1 become misspecified per-agent likelihoods: level 0 ignores cross-covariances, and level 1 widens noise by the header H P H^T, which matches MA's law-level widened noise R̃_e = R_e + T̄Σ_jT̄^T in ch18:24-56.

**Free transfers, MA → CA, once Φ is proved:**
- it1:compact-stabilizer: an SO(K) dictionary is fully identified by a rank-(K−1) code. This bears on CA's SO(2) formation model and frame identifiability.
- The tangent learning theorem with a loop prior (it1:learning) and detectable dissonance ‖Q_D Bω‖², which answers part of CA's open:coh-frustration-metric, together with MA's covariance-dressed defect Q(H;Σ) (02_interactions.tex:272-283).
- The induced H^1 action of ch19, with its stated weak-anchor caveat.
- The interpretation gauge (it2:gauge): records cannot separate belief change from reinterpretation. This is the dictionary-side counterpart of CA's lem:mis-social-blind.
- it2:echo, where the per-agent loop model double counts. This is a fourth exact instance of CA's H2 (overvaluation).

**Free transfers, CA → MA:**
- The parabolic structure-group reduction (prop:fw-energy-symmetry) and the non-consensus form below full rank (prop:fw-consensus-form).
- Theorems on double counting and echo chambers for literal fusion, which apply to MA's per-agent picture on the Gaussian slice.
- thm:lrn-path(d): independently learned pairwise translations almost surely have trivial consensus space. This bears directly on whether MA's per-edge dictionaries are generically dissonant.
- The world-conditional common-mode split (lem:fw-common-mode), which MA has no analogue of because it has no world.
- Weakly connected holonomy.

**What must be proved for the unification to be exact:**
1. CA's exact fusion equals the posterior of an MA global VFE with a world latent, for both mean messages and posterior-sample messages. Static and dynamic cases are separate theorems.
2. CA's level-0 recursion is a discretization of MA's per-agent flow on the Gaussian mean slice, or a precise statement of where it is not.
3. CA's EFE attention as a Gibbs or softmax row in MA's sense. This needs MA to add an action and policy layer; MA currently has no EFE (01_foundations.tex:208).
4. Gauge covariance of CA's selection statistic. The world-conditional precision Π^c, and hence contrast, must be shown invariant under the embedded frame action. CA-ext2's prop:rfm-representation already shows the level-2 formation event depends on representation unless the default translation transforms with the frames (ext2_rfm.tex:113-120).

## 4. Structural differences that block a full merge (ranked)

1. **Objective and agency (most important).** CA is active inference with no team objective. MA is perceptual inference under three distinct objectives, and declares the global VFE primary for formation (AUTHORING.md:35; 03_dynamics.tex:6; but README.md:20 still says no objective is primary, a stale note). No unified framework exists until MA has actions, or CA has a variational flow. CA's open problem of collective theory under EFE-selected attention (03_misreading.tex:208; 01_introduction.tex:312) meets MA's absence of EFE at this point.
2. **Ontology of the world.** CA has one physical world and flat true translations. MA has no physical world, and its true dictionaries may be dissonant (17:53). Under Φ, CA is exactly MA's coboundary sector (it1:exact-flat). CA can never reach MA's curved sector, so "gauge" content in CA reduces to learning error.
3. **Selection criteria.** CA selects by spectral contrast of Π^c, a threshold-type selector with a declared baseline. MA ch06 shows that threshold selectors can reproduce the null dendrogram (06_fusion.tex:876-894), and MA ch11 shows coupling-independent UPGMC selection under receiver-independent targets. Neither manuscript tests CA's contrast selector against MA's renormalized null and frozen control. CA's own frozen-null results (prop:agy-nulls-vanish) are the nearest check.
4. **Formation standards.** CA has (T1)–(T5) with type-D and type-S nulls. MA has (F1)–(F6) with label-preserving and renormalized nulls, a frozen control, (F3) inheritance, (F4) compression and (F6) recursion. A merged standard is straightforward: take the union of nulls and add CA's exact-fusion null and partner randomization to MA. Under it, every construction in both manuscripts fails at least one clause:
   - CA's two-group split fails T4 and holds trivially at γ = ∞ (07_formation.tex:145, 286);
   - MA's global formation fails (F5) with a split verdict, and fails (F6b);
   - MA ch13's verdict is reproduced by the frozen control.

## 5. Reader errors and corrections

- **CA-RG-env slice.** It says MA's gf:top-down answers CA's double-count question "with a different verdict". Having read 05_global_formation.tex:476-509 and s10b_hierarchy.tex:116-118, I find **no contradiction**. MA's top-down factor is a mean-field update in a correctly specified global model: means are exact and variances overconfident, the standard mean-field Gaussian result. CA's literal top-down reading is a misspecified likelihood. These are different constructions. MA's gf result is the counterpart of CA's mean-field pooling overconfidence (P_b ⪯ P̄, prop:met-literal-aggregation), not of literal reading. CA's rem:hie-gauge describes MA "as secondary descriptions … state it" (barycenter plus blend factor). That description does not match gf, so CA's remark is stale against MA's primary text. That part of the reader's claim is correct.
- **MA-links slice.** It says CA's energy differs in argument order from ch17's loss. That is correct but incomplete. CA contains both: the sender-first identity in prop:fw-prior-completion(c) matches it1:loss, and the receiver-first E_ij matches MA's coded cost and reciprocal potential, as the exact identification in §1 shows.
- **CA-framework slice.** Its stabilizer dimension K² − r_c(K−r_c) and kernel dimension K(K−r_c) are confirmed (s02_framework.tex:285-286).

## 6. Open problems that block exact unification (ranked)

1. An EFE/policy layer in MA, or a variational belief flow in CA, so that both share one objective.
2. Theorem: CA's exact fusion equals MA's global-VFE posterior with a world latent, for mean messages and for sampled messages.
3. Gauge invariance of contrast r(C) under the embedded GL(K) frame action, plus a contrast selector tested against MA's renormalized null and frozen control.
4. A dynamic structure-group theory below full rank. CA's parabolic reduction should replace GL(K) in MA's reciprocal potential with coded channels. MA ch15's branch hypothesis already fails at GL(K) consensus for K ≥ 3 (15_contextual_coupling.tex:197).
5. Drifting frames: whether dynamical frames (MA) produce formation that survives exact fusion (CA conj:frm-drifting-frames, 13_discussion.tex:55). MA ch15:633 proves that no locally gauge-invariant contextual energy diffuses frames, which constrains how drifting frames could arise.
6. Bookkeeping: back-port CA's weakly connected holonomy into MA ch17. Update CA's rem:hie-gauge, 12_related.tex:63 and 13_discussion.tex:53 against MA gf:top-down. CA's bib annotation says only MA chapters 17 and 19 were read (references.bib:1250-1256).

Key files (absolute):
- C:/Users/chris and christine/Desktop/Research/manuscripts/Collective_Agents/sections/02_framework.tex
- C:/Users/chris and christine/Desktop/Research/manuscripts/Collective_Agents/sections/s02_framework.tex
- C:/Users/chris and christine/Desktop/Research/manuscripts/Collective_Agents/sections/13_discussion.tex
- C:/Users/chris and christine/Desktop/Research/manuscripts/Collective_Agents/sections/s10b_hierarchy.tex
- C:/Users/chris and christine/Desktop/Research/manuscripts/MAgent_Theory_2.0/chapters/02_interactions.tex
- C:/Users/chris and christine/Desktop/Research/manuscripts/MAgent_Theory_2.0/chapters/03_dynamics.tex
- C:/Users/chris and christine/Desktop/Research/manuscripts/MAgent_Theory_2.0/chapters/05_global_formation.tex
- C:/Users/chris and christine/Desktop/Research/manuscripts/MAgent_Theory_2.0/chapters/17_communication_links.tex

## ANALYSIS: open-problems

# Ranked open problems and defects: Collective_Agents (CA) and MAgent_Theory_2.0 (MA)

Paths are relative to `Research/manuscripts/`. I re-read the load-bearing lines myself where the result is marked "verified". Everything else comes from the dossier and is labeled "dossier". I did not run, build or edit anything.

## Verdict

Neither manuscript proves its central object exists.
- **CA:** no population is shown to be a meta-agent (`CA/sections/s05_agency.tex:275-277`).
- **MA:** no construction meets (F1)-(F6) (`MA/chapters/05_inheritance.tex:2076-2111`).

Both fail interaction necessity in the same way. In their only worked formation models, the groups that form are explained by a null or control:
- **CA:** the split fails the translation-aware exact-fusion null (`CA/sections/07_formation.tex:286`).
- **MA:** the label-preserving null or the frozen control reproduces the partition sequence. Examples are `MA/chapters/05_global_formation.tex:548-569`, `MA/chapters/11_conditional_formation.tex:325-346` and `MA/chapters/13_per_agent_inheritance.tex:202-212`.

The two can be unified, but only partly and only in a linear-Gaussian common core: Gaussian information-form closure, pooled block means, and holonomy and code sheaves. They share no theorem about formation dynamics or gauge geometry. CA explicitly refuses the geometry (`CA/sections/13_discussion.tex:55`). MA shows its gauge structure does no dynamical work (`MA/chapters/10_boundary_closure.tex:4`, verified).

## Similarities, differences, unification hooks

**Shared ground**
- Lossy public codes over private frames: CA's `H_j=T_cU_j` corresponds to MA's `Â=T̄θ̄^{-1}`.
- The same reconstruction and meaning-loss identity, which CA imports.
- The holonomy criterion for consensus, imported by CA from MA ch.17 (`CA/sections/06_coherence.tex:72,80`) and extended by CA to weakly connected graphs.
- Code-sheaf `H^0`.
- The formation-standard null family (label-preserving, renormalized, frozen), which CA takes from MA Item 7 (`CA/sections/07_formation.tex:10,201`).
- Concern with double counting and provenance.
- The Gaussian location family as the closure class for pooled means. CA cites MA's characterization at `CA/sections/13_discussion.tex:53`; MA has it as `it7:characterization`.

**Differences**

| | CA | MA |
|---|---|---|
| World | One physical world `η`; Markov blankets | Represented contents over a context base; no physical world |
| Objective | Per-agent one-step EFE with action and attention; no team objective | Perceptual only: no action, no EFE (`MA/chapters/01_foundations.tex:208`). Three objectives: global VFE (primary for formation per `MA/AUTHORING.md:35`), per-agent mixture VFE, reciprocal potential |
| Time | Discrete rounds, linear-Gaussian | Continuous Fisher flows, general laws on standard Borel spaces |
| Collective | Contrast on world-conditional precision above a declared baseline | Exact retention (inherited parent) graded by (F1)-(F6) |
| Holonomy | True translations flat; holonomy is learning error | Dictionaries are receiver hypotheses whose truth may be dissonant |

**Unification hooks**, from most to least concrete:
1. The linear-Gaussian bridge: MA `imem:gaussian-closure` and `imem:product-tilt` (`MA/appendices/interacting_memory.tex:581-601,220-232`), CA's consensus filter `prop:met-consensus-filter`, and MA's `gf:inheritance`, whose sum retention `(λ_B, m̂_B, ô_B)` is CA's information-form pool.
2. Top-down feedback: CA `rem:hie-gauge` against MA `gf:top-down`.
3. The reduced structure group `GL(K)_{ker T_c}` below full rank (CA `prop:fw-energy-symmetry`) against MA's code stabilizer `Stab_G(T̄)` (`MA/chapters/17_communication_links.tex:143-158`). These are the same object and give a direct gauge-theoretic reading of rank-limited codes.
4. Drifting frames (CA `conj:frm-drifting-frames`). This is blocked by MA's no-frame-diffusion lemma (`MA/chapters/15_contextual_coupling.tex:633`).

## Tier 1: blocks a core thesis or a unification, or is a probable error

**1.1 No inhabited central object (CA and MA)**
- Where: `CA/sections/05_agency.tex:379-403`; `CA/sections/s05_agency.tex:275-277`; `MA/chapters/05_inheritance.tex:2040-2111`.
- Why Tier 1: H1/H5 and the formation standard may both be empty definitions.
- Next step: look for a joint witness in the linear-Gaussian consensus-filter class where both standards are computable: MA's `gf` model with block-dependent priors (escape route in `gf:open`, `MA/chapters/05_global_formation.tex:760-773`) scored by CA's contrast and nulls.

**1.2 Interaction necessity fails in every worked formation model (CA and MA)**
- CA: the declared start is already the split at γ=∞, and the translation-aware null kills it (`CA/sections/07_formation.tex:6,145,286`).
- MA: selection is coupling-independent in the Wishart model (`form:kappa-independence`); the frozen control reproduces the per-agent grouping (`pa:selector-threshold`); `gf:first-event` makes the first event a null event.
- MA ch.06 also shows that threshold selectors reproduce the null tree (`MA/chapters/06_fusion.tex:876-894`). CA's contrast selector is a threshold selector, so the same risk applies to it.
- Next step: state one combined null family (MA's N1-N3 plus CA's partner randomization and exact-fusion type-S) and re-grade both formation models against it.

**1.3 Probable error: `gf:first-event` corollary overclaims (MA)**
- Verified. The lemma (`MA/chapters/05_global_formation.tex:548-556`) proves only that the full and null histories agree up to and including the first event.
- Lines 567-569 conclude that any one-stage construction of this class "fails (F5)". The null can still produce later events, so `P≠P^0` is not excluded.
- Next step: add the hypothesis "the null has no further event", or weaken the corollary to a statement about the first event only.

**1.4 False conjecture stated in CA main text and appendix**
- Verified statement: `CA/sections/app06_coherence.tex:210-212`; also `CA/sections/06_coherence.tex:174`.
- Evidence: an N=2 counterexample (h=(0.6,-0.6), J=1, two domains, Ψ=0), reported by `docs/research/conj_coh_walls.md:33-39` and hand-recomputed by the dossier reader. I verified the conjecture text, not the potential arithmetic.
- The `thm:coh-domains-1d` limit also depends on this conjecture.
- Next step: replace the conjecture with the range {Ψ, Ψ+1, Ψ+2} and recheck the note's Theorems 1-3 independently.

**1.5 `conj:sca-common-code` reported refuted but still stated as open (CA)**
- Verified text: `CA/sections/s08_scale.tex:12-16`, with no rank restriction. It is cited at `CA/sections/08_scale.tex:61,396` and `CA/sections/09_minimal.tex:35`.
- The untracked note `docs/research/conj_sca_common_code.md:32-64` reports a rank-2 frozen counterexample and a period-2 rank-1 counterexample.
- The margins are thin: `ρ-1≈1.3e-4` for C3, and C4 uses sensing gain 200. One unreviewed script supports both.
- It ranks Tier 1 because it is the claimed mechanism by which identity encodings, the gauge-trivial case, protect the moment bound (M), which is a precondition for every collective.
- Next step: recompute C3 independently, then restate the conjecture as rank one with at most one fixed sensor per agent.

**1.6 MA's primary objective has the weakest theory, and the formation results live in a different objective (MA)**
- Verified: `MA/README.md:20` says "No objective is declared primary", while `MA/AUTHORING.md:35` makes the global free energy primary. This is a reader-confirmed contradiction.
- The global VFE has only coordinate descent in the `gf` chapter. Chs. 06-12 are posed in the reciprocal potential, which `prop:dyn-no-global-vfe` shows is not a global VFE (`MA/chapters/03_dynamics.tex:472-492`).
- `op:dyn-three-pictures` (`MA/chapters/03_dynamics.tex:581-582`) is the bridge, and it is open.
- Next step: fix the README, then transfer one reciprocal construction (Wishart ch.11) to the global VFE.

**1.7 Collective-level theorems omit the EFE policy layer (CA)**
- Network, echo-chamber, scale and closure theorems use fixed or exogenous gains (`CA/sections/02_framework.tex:315`; `CA/sections/01_introduction.tex:312`; `CA/sections/08_scale.tex:19`).
- Closure by contrast is proved for a continuous-time OU surrogate with the exterior held fixed, not for the agents' discrete non-reversible recursion (`CA/sections/05_agency.tex:68-95`). The surrogate and held-exterior wording appears there 10 times.
- Together this makes the "active inference" content of the collective layer definitional.
- Next step: a discrete-time, non-reversible `thm:agy-closure-average`. `thm:apx-markov-discrete` already gives the one-coordinate case.

**1.8 Gauge structure has no dynamical role (MA, and therefore any gauge unification)**
- Verified: `MA/chapters/10_boundary_closure.tex:4` ("does no dynamical work").
- Further evidence: the fusion links are pure gauge (`MA/chapters/06_fusion.tex:144-167`); locally gauge-invariant energies produce no frame diffusion (`MA/chapters/15_contextual_coupling.tex:633`); curvature in chs.11-14 is prepared in the initial section and is an artifact of tying the belief and model groups (`MA/chapters/11_conditional_formation.tex:589`; `MA/chapters/14_collective_local_parent.tex:329-330`).
- CA, for its part, treats true translations as flat.
- Next step: decide whether the unified theory is gauge-fixed (CA's stance) or adds a connection kinetic term (`open:geo-gauged-flow`).

## Tier 2: major gaps in stated results

1. **CA, contrast undefined in common regimes.** Contrast needs a diffusive precision, which fails for non-reciprocal attention (674 of 2000 random draws), record nodes, and exact fusion (`CA/sections/04_collectives.tex:174-188`; `CA/sections/s04_collectives.tex:267-274`). Hierarchies are judged in the Galerkin ansatz `PΠP^T`, not in the exact coarse law (`CA/sections/10c_renormalization.tex:38,201`).
2. **CA, verdicts depend on declared geometry, and the baselines cannot be certified** (`CA/sections/s04_collectives.tex:147,285`; `CA/sections/04_collectives.tex:204-266`).
3. **CA formation scaffolding.** Calibration is frozen at its split values but also used on the merged branch (`CA/sections/07_formation.tex:106-111`; `CA/sections/chk07_formation.tex:19`). The learning input is unsupported off the split (`07_formation.tex:104`). The step from the stochastic model to the mean-field map is open (`07_formation.tex:296-298`). The calibration root is used as unique, but only its existence is proved (`CA/sections/app07_formation.tex:114,144`).
4. **CA, H5a disconnected from selection.** It grants the members the full coarse model and contrast enters none of its clauses (`CA/sections/10a_meta_agents.tex:244-272`). The approximate bounds are loose by 10^3 to 10^11 and the coarse-blanket leak is unbounded (`CA/sections/ext1_apx.tex:125,828`; `CA/sections/chkext1_apx.tex:39`).
5. **CA, H5c sensing objective is declared, not derived from EFE**, and the one-step EFE can oppose it (`CA/sections/10d_environments.tex:5`; `CA/sections/s10d_environments.tex:25-36`).
6. **CA, synchronous deliberation.** The note `docs/research/conj_agy_synchronous.md:18-22` (self-reviewed) refutes the free-precision reading of `conj:agy-synchronous` for |A_i|≥3, which `CA/sections/s05_agency.tex:107` still lists as open.
7. **MA, unvalidated numerics carry the only global-VFE classification.** Double-precision values only, no interval arithmetic, and no tail certificate for the frozen control (`MA/chapters/05_global_formation.tex:631-660,712-715`). The pitchfork sign in ch.18 rests on a 0.2% cancellation with no check artifact (`MA/chapters/18_link_dynamics.tex:591-630`).
8. **MA, compression (F4) graded inconsistently across chapters.**
   - Ch.12 obtains (F4) through an external absolute-angle probe that is withdrawn at the handoff (`MA/chapters/12_open_formation.tex:415,513,530`). Ch.13 declines the same device (`MA/chapters/13_per_agent_inheritance.tex:358`, verified that the passage exists).
   - Ch.10 claims (F4) with no declared probe class `B_I` (`MA/chapters/10_boundary_closure.tex:4`, verified), while the same line calls the discarded data invisible.
9. **MA, the known-code hypothesis and non-local dictionary exchange.** All identifiability results assume the receiver knows the sender's code (`MA/chapters/17_communication_links.tex:32,160`). The λ>0 per-agent loop model needs channels between agents that no edge joins (`MA/chapters/18_link_dynamics.tex:58-61`).
10. **MA ch.19 intro overstates the weak-anchor result.** Verified at `MA/chapters/19_curvature_hierarchy.tex:5`. The chapter's own remark (`:130-137`) says the omitted log-determinant dominates in that limit.
11. **MA ch.12 is nonconstructive.** T is unquantified, and the written route needs about T<1e-21 (`MA/chapters/12_open_formation.tex:250-256`). (F2), (F5) and (F6b) are undetermined.
12. **CA identifiability (ext8): the meta-agent grade is not a functional of the recorded law** (`CA/sections/ext8_idn.tex:96-100`). Empirical claims therefore need interventions under the untested invariances (I1)-(I3).

## Tier 3: generalizations, polish, notation

- **Stale cross-manuscript claim.** CA says MA's top-down feedback is known only through "secondary descriptions" (verified, `CA/sections/13_discussion.tex:53`; also `CA/sections/12_related.tex:63`). MA `gf:top-down` (`MA/chapters/05_global_formation.tex:476-509`, verified) answers part of the question.
  - **Reader error in the dossier.** The CA-RG slice says MA reaches a "different verdict" from CA. That is not correct. MA's result is mean-field VI with exact child likelihoods, not literal reading of the parent's belief. Its means agree at the fixed point and its variance is at most the exact variance, so it is also overconfident. The two results are consistent in sign and differ in mechanism. Next step: cite `gf:top-down` in `rem:hie-gauge` and compare overconfidence factors.
- **Back-port and status fixes.**
  - Back-port CA's weakly connected holonomy and frustration extension into MA ch.17.
  - Update MA companions c05, c17 and c18.
  - Add `gf:open` to the MA outlook table (`MA/chapters/06_outlook.tex:18-49`).
  - Add the 05_global_formation chapter to the README.
- **Overstated status labels in CA.**
  - "theorem" for H1, which contains a definition (`CA/sections/01_introduction.tex:305` vs `:191`).
  - "echo chambers need misspecification" is broader than `prop:mis-exact-no-echo` supports (`CA/sections/03_misreading.tex:192-200`).
  - Stale labels `conj:hie-top-down` and `conj:ren-lrg`.
  - Main-text "exactly" for a numerical certificate (`CA/sections/04_collectives.tex:387`).
- **Reproducibility (CA).** Check scripts are outside the manuscript folder (`CA/sections/chkext1_apx.tex:8`). The research notes are untracked and self-reviewed.
- **Notation drift across both manuscripts.**
  - CA: ϖ, Φ, Ψ, h, κ are overloaded, and `Ω_int` clashes with MA's `Ω_ij`.
  - MA: 𝒱 means the vertex set in one chapter and an operator in another; 𝖢 is both the structure catalog and the selector-constant set.
  - A cross-manuscript consistency pass is warranted before any unification.
- **Generalizations listed as open by the authors.** Nonlinear and discrete-state settings (both), RG beyond equitable cases (CA), and frustration under GL(K) (CA `open:coh-frustration-metric`; MA's dressed defect `Q(H;Σ)` at `MA/chapters/17_communication_links.tex:254-263` is a ready candidate).

## Smallest next steps, in order

1. Fix the two verified probable errors: the `gf:first-event` corollary and `conj:coh-walls`.
2. Independently recompute the refutation of `conj:sca-common-code`, then restate the conjecture in the .tex.
3. Reconcile MA's README with AUTHORING and the outlook table.
4. Write one joint linear-Gaussian test model: MA's `gf` with block-dependent priors, scored by CA's contrast plus the union of both null families. This is the cheapest single object that could inhabit both standards or show that it cannot.
