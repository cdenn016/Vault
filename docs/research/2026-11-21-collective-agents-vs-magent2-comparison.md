# Collective_Agents and MAgent_Theory_2.0: status, relation, unification, open problems

Paths are relative to `Research/manuscripts/`. The prefix `CA/` stands for `Collective_Agents/sections/` and `MA/` for `MAgent_Theory_2.0/chapters/` unless another directory is given. In this pass I re-read the passages marked "spot-checked". Everything else comes from the four analyses and the 14 reader reports behind them, and is labeled "per analyses" where it matters.

> [!warning] Post-verification corrections (2026-11-21)
> Each Tier 1 item below was later checked by an independent verifier and a skeptic; see `2026-11-21-tier1-verification.md`. Where this report and that one disagree, the verification report governs. In summary:
> - **T1.1** confirmed with correction: H5a is inhabited (`ex:met-two-firms`); only the graded meta-agent of `def:agy-meta-agent` and an MA construction passing (F4), (F5) and (F6b) together lack instances. Drop "H5" from "H1/H5 may be empty".
> - **T1.2** partially confirmed: CA fails only the survive clause of (T4); MA ch. 13 and ch. 06 formally pass (F5); the claim that MA's threshold-selector result applies to CA's selector is wrong. "(both)" is an analogy, not a parallel.
> - **T1.3** confirmed: a two-agent Gaussian counterexample exists. Fixed in MA.
> - **T1.4** confirmed with correction: `thm:coh-domains-1d` does not depend on the conjecture; the correct range is {Ψ, Ψ+1, Ψ+2}. Fixed in CA.
> - **T1.5** confirmed with correction: margins are ρ/f^p − 1 (about 2e-4 and 1.8e-2), not ρ − 1; (M) has proven sufficient conditions and does not rest on the conjecture; "restate as rank one" is also refuted for periodic profiles with two sensing channels. Narrowed in CA.
> - **T1.6** confirmed with correction: the contradiction is a stale README; `prop:dyn-no-global-vfe` does not reach most formation chapters under its hypotheses. Fixed in MA.
> - **T1.7** refuted: at least six CA collective-level results take EFE-selected attention as input; what remains open is closure and agency of an EFE-formed collective and contrast at finite γ. Citations `CA/01_introduction.tex:312` (nonexistent) and the `s01` attribution of `02_framework.tex:260` were wrong.
> - **T1.8** narrowed: no curvature or holonomy drives formation in either manuscript, but MA ch. 15 and ch. 17–18 give the gauge structure dynamical roles, and CA's formation is driven by translation error. A unification is therefore more than kinematic. Primary citation: `MA/02_geometry.tex:7`.

## 1. Verdict

Collective_Agents (CA) is a linear-Gaussian active-inference theory of collectives in one physical world. Its kinematic and coherence results are proved, but its central object, a meta-agent, has no exhibited instance (CA/s05_agency.tex:275-277, spot-checked). Its only formation model fails the translation-aware exact-fusion null, so "from such a start the model yields no formation result" (CA/07_formation.tex:286, spot-checked). MAgent_Theory_2.0 (MA) is a general-law, purely perceptual gauge-bundle theory. It has a large body of exact inheritance and identifiability results, no construction that meets its formation standard (F1)-(F6), and a gauge structure that it says does no dynamical work in the formation chapters (MA/10_boundary_closure.tex:4, spot-checked). The two can be unified only partially. CA's code, frame, translation, holonomy and code-sheaf kinematics embed exactly into MA's code/dictionary sector as the flat, linear-Gaussian, one-world special case. The objectives and dynamics do not embed: CA uses per-agent EFE and Kalman filtering, while MA uses three perceptual objectives with no action. The formation standards differ in their clauses and their nulls. Neither manuscript has a formation that its own standard accepts.

## 2. Current status of each manuscript

### Collective_Agents

The following are proved inside linear-Gaussian models:
- The update subspace and the prior-completion/meaning-lost identity, imported from MA and reproved (CA/02_framework.tex:52-85).
- The reception identity and the communication energy (CA/02_framework.tex:109-118).
- The full-rank, noiseless consensus form of the energy, together with its failure on every other channel class (CA/02_framework.tex:290-303; prop:fw-consensus-form, prop:fw-noisy-energy).
- The parabolic sender-side symmetry GL(K)_{ker T_c}, of dimension K²−r_c(K−r_c), with kernel of dimension K(K−r_c) (CA/s02_framework.tex:283-289, spot-checked).
- The holonomy criterion, extended to weakly connected graphs, and the frustration bounds (CA/06_coherence.tex:72-95).
- The flatness of true translations (prop:coh-flat-true).
- The double-counting and echo results for literal reading (CA/10b_hierarchy.tex:43-58).
- The prior-corrected logarithmic pool (CA/05_agency.tex:110-118).

The following are conditional or partial:
- H3 formation holds only for a two-group mean-field map at γ=∞ with σ_α²=0, from a declared start that is already the split. The step from the stochastic model to the map is open, and T4 fails against the type-S null (CA/07_formation.tex:284-286, spot-checked).
- Closure is proved for a continuous-time OU surrogate with the exterior held fixed (CA/05_agency.tex:68-95, per analyses).
- Every network-level theorem uses fixed or exogenous gains, so the EFE layer does not enter the collective theorems (CA/02_framework.tex:315; CA/01_introduction.tex:312, per analyses).
- The H5a approximate bounds are loose by 10³ to 10¹¹ (CA/ext1_apx.tex:125,828, per analyses).

The following are conjectured:
- conj:coh-walls (CA/app06_coherence.tex:212-214, spot-checked).
- conj:sca-common-code (CA/s08_scale.tex:12-16).
- conj:agy-synchronous (CA/s05_agency.tex:107).
- conj:frm-drifting-frames (CA/07_formation.tex:288).

The untracked research notes in `Collective_Agents/docs/research/` report refutations of the first three. Those notes are self-reviewed, and I did not check them. CA has no meta-agent instance (open:agy-meta-agent-exists, CA/s05_agency.tex:275-277, spot-checked).

Maturity: the proofs are dense and the status annotations are explicit. Several headline claims, however, are graded "theorem" while depending on definitions, computations, or conjectures that are reported false.

### MAgent_Theory_2.0

The following are proved:
- Identifiability up to the code stabilizer, dim Stab = K(K−r), under the hypothesis that the receiver knows the sender's code. MA itself calls that hypothesis essential (MA/17_communication_links.tex:143-160, spot-checked).
- it1:loss, the consensus criterion, frustration, and the code sheaf (MA/17_communication_links.tex:67-73, 238-252, 420-434).
- prop:dyn-no-global-vfe (MA/03_dynamics.tex:472-492).
- gf:top-down: the mean-field top-down factor gives the same posterior mean as the cavity prior and a variance no larger than the exact one (MA/05_global_formation.tex:476-509, spot-checked).
- Exact inheritance constructions without selection, for example ch. 10, where (F1), (F3) and (F4) hold and (F2), (F5) and (F6) are not addressed (MA/10_boundary_closure.tex:4, spot-checked).
- Lumpability and the canonical-parent results (MA/05_inheritance.tex:439-627, per analyses).

The following are conditional or computational:
- The classification of the global-formation instance rests on double-precision computation at a single point (MA/05_global_formation.tex:631-660).
- The sign of the ch. 18 pitchfork depends on a 0.2% cancellation (MA/18_link_dynamics.tex:591-630).
- The ch. 12 routing theorem is nonconstructive (MA/12_open_formation.tex:250-256). All three are per analyses.

The following are open: op:dyn-three-pictures (MA/03_dynamics.tex:581-582), inh:formation-open, and gf:open.

Maturity: the hypotheses are stated with care. The author notes contradict each other on which objective is primary. README.md:20 says "No objective is declared primary", while AUTHORING.md:35 says "the global free energy is primary for formation" (both spot-checked).

## 3. Similarities

| Object | CA | MA | Relation |
|---|---|---|---|
| Public code, frame, effective code | CA/02_framework.tex:36-40; Ĥ_ij=T_cΘ_ij^{-1}U_i at CA/s02_framework.tex:280 | Â_ij=T̄θ̄_ij^{-1}, MA/17_communication_links.tex:24-48 | Exact (Ĥ=ÂU_i) |
| Translation / dictionary | Θ_ij, with true value U_iU_j^{-1}, CA/02_framework.tex:270-277 | Receiver-owned θ̄_ij, MA/17_communication_links.tex:34-50 | Exact when MA's truth is a coboundary |
| Meaning lost | CA/02_framework.tex:64-85 (attributed to MA) | it1:loss, MA/17_communication_links.tex:67-73 | Identical |
| Frame non-identifiability | {X: T_cX=0}, kernel of GL(K)_{ker T_c}, CA/s02_framework.tex:286 (spot-checked) | Stab_G(T̄), dim K(K−r), MA/17_communication_links.tex:143-158 (spot-checked) | Same subgroup. CA's symmetry group is the larger parabolic group. |
| Communication energy vs coded cost | E_ij=KL(Ĥ#q_i‖H_j#q_j), CA/02_framework.tex:109-118 | D^cod=KL(ν_iC_ij‖ν_jT_j), MA/02_interactions.tex:162-168 | Exact with C_ij=Ĥ_ij and noiseless channels. Stated in neither manuscript. |
| Holonomy criterion | thm:coh-holonomy, CA/06_coherence.tex:72-80 | it1:consensus, MA/17_communication_links.tex:238-244 | Same theorem. CA adds the weakly connected case. |
| Frustration | CA/06_coherence.tex:86-95 | MA/17_communication_links.tex:246-252 | Same quadratic form. CA adds a metric M_i. |
| Code sheaf H⁰ | prop:coh-coded, CA/s06_coherence.tex:79-85 | MA/17_communication_links.tex:420-434 | Same family of sheaves |
| Lumpability / minimal closed extension | CA/10a_meta_agents.tex:114-138 | MA/05_inheritance.tex:439-450, 543-627 | CA's version is the linear-Gaussian case |
| Gaussian-only pooled closure | rem:agy-location-family, cited at CA/13_discussion.tex:53 (spot-checked) | it7:characterization, Item_7_formation_feedback.tex:210-214 | Imported |
| Null-based formation standard | (T1)-(T5), CA/07_formation.tex:10-20 | (F1)-(F6), MA/05_inheritance.tex:1812-1936 | Partial overlap (see §4) |
| Double counting repaired by the cavity prior | thm:hie-messages; CA/10b_hierarchy.tex:43-58 | it2:echo, MA/18_link_dynamics.tex:203-217 | Same structure, over different variables |
| Shared error invisible to records | lem:mis-social-blind, CA/03_misreading.tex:120-125 | it2:gauge, MA/18_link_dynamics.tex:66-84 | Analogous invariance statements. Neither implies the other. |
| Negative formation verdict | CA/07_formation.tex:286 (spot-checked) | MA/05_global_formation.tex:548-569, 662-743; MA/13_per_agent_inheritance.tex:202-212 | Both fail interaction necessity |

## 4. Differences

The substantive differences are these:
- **World.** CA has one physical world, and true translations are flat (CA/13_discussion.tex:55, spot-checked). MA has no world, and its dictionaries may carry holonomy as an "additional edge field" (MA/17_communication_links.tex:53).
- **Agency.** CA uses per-agent EFE, with action and attention. MA has no action and no EFE (MA/01_foundations.tex:208).
- **Law class.** CA is linear-Gaussian. MA uses general laws on standard Borel spaces.
- **Time.** CA runs in discrete rounds. MA uses continuous Fisher flows.
- **Collective.** CA defines a collective by spectral contrast above a declared baseline (CA/04_collectives.tex:214-220). MA defines it by exact retention graded by (F1)-(F6).
- **Geometry.** MA has a context base with curved connections (MA/16_link_base_transport.tex:225-362). CA has no counterpart.
- **Formation standards.** CA lacks MA's (F3) inheritance, (F4) compression and (F6) recursion. MA lacks CA's type-S exact-fusion null and partner randomization. The null families also share names without being the same interventions. CA's lp null delivers pure noise while keeping the assigned precisions (CA/05_agency.tex:345). MA's N1 deletes the peer costs (MA/05_inheritance.tex:1676-1706, per analyses). Verdicts under one family do not transfer to the other.
- **Selector.** CA uses a contrast threshold. MA ch. 06 shows that a threshold selector can reproduce the null tree (MA/06_fusion.tex:876-894, per analyses). That result bears on CA's (T4).

The two manuscripts do not contradict each other on any mathematical fact. There are two clashes:
- **C1: a stale description, not a mathematical contradiction.** CA describes MA's top-down action as a child prior "with a blend factor" and a parent that is a "barycenter", "as secondary descriptions of those documents state it" (CA/s10b_hierarchy.tex:117 and CA/13_discussion.tex:53, both spot-checked). A grep of MA/ for "blend" and "barycent" returns nothing. MA's actual mechanism is gf:top-down (spot-checked). This defect bears on CA's open question, which MA's text answers in part.
- **C2: curvature semantics.** The word "true" means different things in the two texts (CA/13_discussion.tex:55 vs MA/17_communication_links.tex:53). A unification has to fix one meaning.

The cosmetic differences are notational: Θ vs θ̄; T_c vs T̄^c; fixed ϖ vs Gibbs β rows; CA's Ω_int against MA's Ω_ij; and symbols overloaded inside each manuscript (ϖ, Φ, Ψ, 𝒱, 𝖢). The word "gauge" also has two senses. CA's thm:lrn-gauge matches MA's observable-algebra sense (MA/17_communication_links.tex:160, spot-checked) and not its structure group, and MA uses both senses itself.

## 5. Unification

**Proposed framework.** Take MA's code/dictionary sector as the base, and add one ingredient MA lacks: a common world latent η with dynamics F and Q in a global generative model. Embed CA through the following map:
- G=GL(K), with Gaussian laws;
- reference coordinates are CA's internal coordinates;
- MA's θ̄_ij is CA's Θ_ij, with the true value U_iU_j^{-1} (a coboundary);
- T̄^c=T_c for every sender, which is MA's shared-language hypothesis;
- exact fusion is posterior inference in the global model;
- CA's level-0 and level-1 receivers are misspecified per-agent likelihoods.

**Exact under this map** (kinematics):
- the effective codes;
- the stabilizer, which equals the kernel of the parabolic group;
- the meaning-lost identity;
- the energy as coded cost;
- holonomy and frustration;
- the code sheaf.

One consequence follows directly. CA's prop:fw-energy-symmetry(b) is a theorem about MA's coded cost: below full rank, the invariance group of a coded-channel reciprocal potential is a product of parabolic stabilizers, not GL(K)^V. MA states only the observable-algebra form of this fact (MA/17_communication_links.tex:160).

**Interpretive only:**
- CA's EFE attention as a counterpart of MA's Gibbs rows. CA's value is submodular mutual information, while MA's cost is a per-source KL.
- CA's statement that E has "the argument order of the complexity term" (CA/02_framework.tex:129). MA's prop:dyn-no-global-vfe rules out an exact reading of the reciprocal potential as a global VFE under its hypotheses.

**Must be proved before the unification is exact:**
1. CA's exact fusion equals the posterior of an MA global VFE with a world latent. Mean messages and posterior-sample messages need separate statements, and MA's imem:scalar-calibration shows that the two differ in cross-covariance.
2. CA's level-0 recursion is the explicit-Euler discretization of MA's per-agent mean flow with F=I and Q=0. Otherwise the difference must be stated. With F≠I, MA has no counterpart.
3. An action/EFE layer in MA, or a variational flow in CA.
4. Invariance of contrast r(C) under the embedded frame action. CA's own ext2 result shows that the level-2 event depends on the representation unless the default translation transforms with the frames (CA/ext2_rfm.tex:113-120, per analyses).
5. One merged formation standard: the union of the nulls, plus (F3), (F4) and (F6).

Under any such merged standard, every existing construction in both manuscripts fails at least one clause.

## 6. Ranked open problems and issues

### Tier 1: blocks a core thesis or the unification, or is a probable error

1. **No inhabited central object (both).**
   - Location: CA/s05_agency.tex:275-277 (spot-checked); MA/05_inheritance.tex:2040-2111.
   - Why this rank: H1/H5 and (F1)-(F6) may be empty definitions.
   - Next step: build one joint linear-Gaussian witness. Use MA's gf model with block-dependent priors (escape route gf:open, MA/05_global_formation.tex:760-773), scored by CA's contrast and by the union of the null families.
2. **Interaction necessity fails in every worked formation model (both).**
   - Location: CA/07_formation.tex:286 (spot-checked); MA/05_global_formation.tex:548-569; MA/13_per_agent_inheritance.tex:202-212; MA/06_fusion.tex:876-894 (the threshold-selector result, which applies to CA's selector).
   - Next step: state one combined null family and re-grade both models against it.
3. **Probable overclaim in MA's gf:first-event corollary.**
   - Location: MA/05_global_formation.tex:548-569 (spot-checked).
   - Problem: the lemma proves only that the full and null histories agree for n≤n₁. The corollary then concludes that a one-stage construction "fails (F5)". (F5) compares the histories on [0,∞) (MA/05_inheritance.tex:1840-1847, spot-checked). The label-preserving null can produce later events, so P≠P⁰ is not excluded.
   - Next step: add the hypothesis that the null has no event after n₁, or restrict the corollary to finite horizons that end at the first event.
4. **conj:coh-walls stated but reported false (CA).**
   - Location: the text is at CA/app06_coherence.tex:212-214 (spot-checked) and CA/06_coherence.tex:174. The counterexample is in `Collective_Agents/docs/research/conj_coh_walls.md:33-39` (N=2, h=(±0.6), J=1).
   - Status: unverified by me. thm:coh-domains-1d depends on the conjecture.
   - Next step: recheck the counterexample by hand and restate the conjecture as the range {Ψ, Ψ+1, Ψ+2}.
5. **conj:sca-common-code reported refuted but still stated as open (CA).**
   - Location: CA/s08_scale.tex:12-16, cited at CA/08_scale.tex:61,396 and CA/09_minimal.tex:35. The counterexamples are in `docs/research/conj_sca_common_code.md:32-64`, with a thin margin of ρ−1≈1.3e-4.
   - Why this rank: the conjecture underpins the moment bound that every collective needs.
   - Next step: recompute independently, then restate the conjecture as rank one.
6. **MA's primary objective has the weakest theory.**
   - Location: README.md:20 contradicts AUTHORING.md:35 (both spot-checked). The formation chapters 06-12 are posed in the reciprocal potential, which is not a global VFE (MA/03_dynamics.tex:472-492). The bridge op:dyn-three-pictures is open (MA/03_dynamics.tex:581-582).
   - Next step: fix the README, then transfer one construction (ch. 11) to the global VFE.
7. **CA's EFE layer is absent from its collective theorems.**
   - Location: closure is proved only for an OU surrogate with the exterior held fixed (CA/05_agency.tex:68-95; CA/02_framework.tex:315; CA/01_introduction.tex:312, per analyses).
   - Next step: a discrete-time, non-reversible thm:agy-closure-average.
8. **The gauge structure has no dynamical role.**
   - Location: MA/10_boundary_closure.tex:4 (spot-checked) and MA/15_contextual_coupling.tex:633 (per analyses). CA treats true translations as flat (CA/13_discussion.tex:55, spot-checked).
   - Why this rank: any "gauge" unification is currently kinematic only.
   - Next step: decide between a gauge-fixed theory and adding a connection kinetic term (open:geo-gauged-flow).

### Tier 2: major gaps in stated results

All Tier 2 items are per analyses unless marked otherwise.

1. **CA contrast undefined in common regimes.** It is undefined for non-reciprocal attention, record nodes and exact fusion (CA/04_collectives.tex:174-188; CA/s04_collectives.tex:267-274). Hierarchies are judged in a Galerkin ansatz rather than in the exact coarse law (CA/10c_renormalization.tex:38,201).
2. **CA verdicts depend on declared geometry and on baselines that cannot be certified** (CA/s04_collectives.tex:147,285).
3. **CA formation scaffolding.**
   - Calibration is frozen at its split values but also used on the merged branch (CA/07_formation.tex:106-111).
   - The learning input is unsupported off the split (CA/07_formation.tex:104).
   - The calibration root is used as unique, but only its existence is proved (CA/app07_formation.tex:114,144).
   - The step from the stochastic model to the mean-field map is open (CA/07_formation.tex:296-298).
4. **CA H5a is disconnected from contrast selection** (CA/10a_meta_agents.tex:244-272), and its bounds are very loose (CA/ext1_apx.tex:125,828).
5. **CA's H5c sensing objective is declared, not derived** (CA/10d_environments.tex:5; CA/s10d_environments.tex:25-36).
6. **CA conj:agy-synchronous is still listed as open** (CA/s05_agency.tex:107), although a self-reviewed note refutes it for |A_i|≥3 (`docs/research/conj_agy_synchronous.md:18-22`). Unverified.
7. **MA's global-VFE classification rests on unvalidated numerics.**
   - The classification uses double-precision values with no interval arithmetic and no tail certificate (MA/05_global_formation.tex:631-660, 712-715).
   - The sign of the ch. 18 pitchfork depends on a 0.2% cancellation (MA/18_link_dynamics.tex:591-630).
   - Next step: interval arithmetic at the single classification point.
8. **MA grades (F4) inconsistently across chapters.**
   - Ch. 12 obtains (F4) through an external probe that is then withdrawn (MA/12_open_formation.tex:415,513,530).
   - Ch. 13 declines the same device (MA/13_per_agent_inheritance.tex:358).
   - Ch. 10 declares no probe class B_I (MA/10_boundary_closure.tex:4).
9. **MA's known-code hypothesis.** All identifiability results assume the receiver knows the sender's code (MA/17_communication_links.tex:144-160, spot-checked). CA's grounded code identification and ext5 thm:lrn-gauge are a partial route around it. In addition, the λ>0 loop model needs channels between agents that no edge joins (MA/18_link_dynamics.tex:58-61).
10. **MA ch. 19 intro overstates the weak-anchor result** (MA/19_curvature_hierarchy.tex:5 vs :130-137).
11. **MA ch. 12 is nonconstructive.** T is unquantified, and (F2), (F5) and (F6b) are undetermined (MA/12_open_formation.tex:250-256).
12. **CA ext8: the meta-agent grade is not a functional of the recorded law** (CA/ext8_idn.tex:96-100).

### Tier 3: cross-references, labels, notation

1. **C1, the stale description of MA's top-down action.** Update CA/s10b_hierarchy.tex:117, CA/13_discussion.tex:53 and CA/12_related.tex:63 against gf:top-down. Under gf:top-down the means are exact and the variance is understated. CA's literal reader is a misspecified likelihood, and its MSE is biased (CA/10b_hierarchy.tex:43-58). The two mechanisms differ and are consistent in the direction of overconfidence. Part of CA's open question ("not settled here") is answered by MA in the Gaussian global-VFE case. CA's bib annotation records that it read only MA chs. 17 and 19 (Collective_Agents/references.bib:1250-1256, per analyses).
2. **Back-ports.** Back-port CA's weakly connected holonomy and frustration bounds into MA ch. 17. CA should cite MA's covariance-dressed defect Q(H;Σ) (MA/02_interactions.tex:272-283; MA/17_communication_links.tex:254-263) for open:coh-frustration-metric (CA/s06_coherence.tex:72-74). CA should cite MA/15_contextual_coupling.tex:633 at conj:frm-drifting-frames.
3. **The formation standard is cited but altered.** CA cites dennis2026formation as the source of its standard (CA/07_formation.tex:10) while dropping (F3), (F4) and (F6). Either reconcile the two or state that they are distinct standards.
4. **Overstated CA labels.**
   - H1 is called a "theorem" although it contains a definition (CA/01_introduction.tex:305 vs :191).
   - "Echo chambers need misspecification" is broader than prop:mis-exact-no-echo (CA/03_misreading.tex:192-200).
   - Main text says "exactly" for a numerical certificate (CA/04_collectives.tex:387).
   - The labels conj:hie-top-down and conj:ren-lrg are stale.
5. **Reproducibility.** CA's check scripts are outside the manuscript folder (CA/chkext1_apx.tex:8), and its research notes are untracked and self-reviewed.
6. **Notation.** Run a cross-manuscript notation pass before any merge.

## 7. Coverage notes

**Spot-checked against the .tex in this pass:**
- MA/05_global_formation.tex:476-512 and :540-575;
- MA/05_inheritance.tex:1838-1870;
- MA/17_communication_links.tex:140-162;
- MA/10_boundary_closure.tex:4;
- MA README.md:18-22 and AUTHORING.md:33-36;
- CA/s10b_hierarchy.tex:114-119;
- CA/app06_coherence.tex:205-214;
- CA/s05_agency.tex:273-278;
- CA/07_formation.tex:284-288;
- CA/13_discussion.tex:53-55;
- CA/s02_framework.tex:283-290;
- a grep of MA for "blend" and "barycent".

**Not verified:**
- the arithmetic of every `docs/research` counterexample;
- all numerical claims (the 674/2000 count, the 10³ to 10¹¹ looseness, ρ−1≈1.3e-4, the 0.2% cancellation);
- MA/15_contextual_coupling.tex:633;
- MA/18_link_dynamics.tex:621-630;
- the ch. 12 and ch. 13 (F4) passages;
- MA it1:learning's describer-level standing (MA/17_communication_links.tex:311,507).

**Not read by any analyst, as far as the reports show:**
- MA `companion/`, `supplements/`, and Item drafts other than Item 7;
- most of CA's ext3, ext4, ext6 and ext7 and their appendices;
- the active note `Collective_Agents/docs/research/problem_8.md`, opened 2026-11-21, which concerns open:nrg-rate in CA/ext6_nrg.tex. Its status is unknown.

**Analyst disagreements and how I resolved them:**
- **(a)** The CA-RG reader said MA reaches a "different verdict" on top-down double counting. Three analyses reject that, and I agree after reading both passages. MA's result is mean-field inference in a correctly specified model, CA's is a misspecified literal reading, and the two are consistent in sign.
- **(b)** The differences analysis called C1 the one claim pair that "cannot both hold". More precisely, it is a misdescription of MA by CA, not a contradiction between theorems.
- **(c)** Readers said CA's 𝔑_lp, 𝔑_rn and 𝔑_fr "are" MA's N1-N3. The similarities analysis showed they are different interventions (CA/05_agency.tex:345-346 vs MA/05_inheritance.tex:1676-1706). I kept that correction but did not re-read those lines.
- **(d)** The CA-ext2-8 reader set CA's "gauge freedom" against MA's gauge. It is consistent with MA's observable-algebra sense (MA/17_communication_links.tex:160, spot-checked). The conflict is only with MA's structure group.
- **(e)** The gf:first-event overclaim was raised by one analysis only. The definition of (F5) supports it. I rank it "probable": a one-stage construction in which the null also has no later event would make the corollary true, and the text states no such hypothesis.
