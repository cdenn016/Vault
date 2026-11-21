# Tier 1 verification: collated results

**What this collation ran.** I re-read CA/07_formation.tex:30, :53, :70, :92, :284 and :286, CA/13_discussion.tex:15 and :55, and CA/02_framework.tex:260. I also counted the lines of CA/s01_introduction.tex (158) and CA/01_introduction.tex (162). I used these reads to settle the two points where a verifier and a skeptic disagreed, in T1.7 and T1.8. I ran no scripts. Every other statement below comes from the verifier and skeptic outputs. The scripts they report running are scratchpad files t13.py, cw.py, cc.py, ctrl.py, sk.py and sk/sk.py, plus the skeptics' hand derivations. I did not re-run any of them.

## Summary table

| Issue | Final status | One line |
|---|---|---|
| T1.1 No inhabited central object (both) | Confirmed with correction | Neither the graded meta-agent of def:agy-meta-agent (CA) nor a recursive formation meeting (F1)-(F6) (MA) has an instance. H5a and MA's weaker selection classes are inhabited, so "H5 may be empty" is wrong. |
| T1.2 Interaction necessity fails in every formation model (both) | Partially confirmed | CA fails only the survive (type S) clause of (T4). MA ch.13 and ch.06 formally pass (F5). MA's threshold-selector result does not transfer to CA. |
| T1.3 MA gf:first-event corollary overclaims | Confirmed | The lemma is correct but the corollary does not follow. A two-agent Gaussian instance passes (F5) with one selection stage. |
| T1.4 CA conj:coh-walls false | Confirmed with correction | Domains minus switches can be 2 on open chains. thm:coh-domains-1d does not depend on the conjecture. |
| T1.5 CA conj:sca-common-code refuted | Confirmed with correction | Both counterexamples are real at high precision. (M) does not rest on the conjecture, and a "rank one" restatement is still refuted by C4. |
| T1.6 MA primary-objective contradiction | Confirmed with correction | The contradiction is a stale README, not the .tex. prop:dyn-no-global-vfe does not reach most formation chapters. |
| T1.7 CA EFE layer absent from collective theorems | Refuted (a narrower claim stands) | At least six collective-level results take EFE-selected attention as input. At γ=∞ the formation chain carries EFE attention through to contrast. |
| T1.8 Gauge structure has no dynamical role | Confirmed with correction (narrowed) | No curvature or holonomy drives formation in either manuscript. MA ch.15 and ch.17-18 give the gauge structure dynamical roles, and CA formation is driven by translation error. |

## T1.1 No inhabited central object (both)

**Final status:** confirmed with correction. The verifier and skeptic agree.

**Evidence.** CA defines the meta-agent at CA/05_agency.tex:379-381 and states at CA/s05_agency.tex:247 that "No population analyzed here, synthetic or empirical, is shown to meet every clause". The existence question stays open as open:agy-meta-agent-exists (s05_agency.tex:275-277). The ext2 superunit "is not a meta-agent at any grade" (ext2_rfm.tex:143). The ext2 verdict depends on a null trajectory that is computed but not proved.

H5a is a different matter. thm:met-h5a (10a_meta_agents.tex:244-264) is realized by ex:met-two-firms, and s10a_meta_agents.tex:143 states "Every property of H5a thus holds exactly for C_1". The firms example computes no contrast r0>1, no partner-randomization null and no agency index. rem:env-firm-meta-agent (s10d_environments.tex:182-183) reads the firm as a meta-agent only under def:met-coarse.

In MA, the standard is at MA/05_inheritance.tex:1812-1864 and the open problem is inh:formation-open (:2076-2111). Every construction fails or leaves open at least one of (F4), (F5) and (F6b), per :2040-2074, 06_fusion.tex:915-917 and 11_conditional_formation.tex:6. Item_7 is "undetermined" (:21, :334), it leaves the constant sets for both (F2) and (F5) open, and it sits outside the main manuscript (:11).

**Correction to the report.** Drop "H5" from "H1/H5 ... may be empty", because the structural H5a meta-agent is inhabited. Only the selected and graded object of def:agy-meta-agent lacks an instance. MA's two-stage and single-stage selections with exact inheritance are inhabited, so the missing object is one that passes (F4), (F5) and (F6b) together. inh:formation-open is stated under the global free energy (:2104), with the per-agent case added at :2109-2110. It is not stated universally.

**Smallest manuscript fix.** Add one sentence to rem:agy-h1-status, and optionally to rem:met-no-selection. It should name ex:met-two-firms as an unevaluated candidate for open:agy-meta-agent-exists and list the clauses not computed there: contrast, the partner-randomization null, exact-fusion survival and the agency grade.

## T1.2 Interaction necessity fails in every worked formation model (both)

**Final status:** partially confirmed. The verifier and skeptic agree.

**Evidence.** The CA definition of (T4) at CA/07_formation.tex:18 has two parts: the partition must differ from every type-D null, and it must survive every type-S null. Per :284, the differ part holds:

- by proof for the deletion and freezing nulls (Prop. frm-nulls, :198-205);
- by computation for partner randomization redrawn every round;
- not computed for partner randomization drawn once.

The survive part fails against N_ex (type S, CA/05_agency.tex:352). This is by proof in the translation-aware form from exchangeable starts (:273, :286) and heuristic for full N_ex (:280).

In MA, per chapter:

- ch.05 global fails (05_global_formation.tex:567-569, :737).
- ch.11 fails (:6, :437).
- ch.12 is not established (:530).
- ch.08 is undetermined (:272).
- ch.13 passes for the declared constants in (1/8,1/3) (13_per_agent_inheritance.tex:150, :212, :280). The frozen-environment control, which sits outside (F5), reproduces the partition.
- ch.06 passes for the exact-equality selector and fails only for a threshold family (06_fusion.tex:874-894).

The threshold result depends on three facts specific to the fusion model: pure e^{-κt} decay of the nulls, a normalized-centroid distance selector, and merge times that increase with linkage height (:882-889).

**Correction to the report.**

- **CA:** (T4) fails only in its survive clause.
- **MA:** no (F5) pass certifies interaction-driven grouping. It is wrong to say (F5) "fails or is unaddressed" everywhere.
- **Transfer claim:** delete "applies to CA's selector" (comparison report :87, :137). CA's contrast selector (CA/04_collectives.tex:214-219) separates the full model from the deletion nulls by proof. MA's result also concerns a differ clause, whereas CA fails a survive clause.
- **"(both)":** CA and MA fail different clauses, so "(both)" is an analogy, not a parallel.

**Smallest manuscript fix.** None is required. Optionally, at CA/07_formation.tex:286, write "(T4) fails in its survive clause" instead of "Clause (T4) fails".

## T1.3 Probable overclaim in MA gf:first-event corollary

**Final status:** confirmed. The verifier and skeptic agree, and the skeptic recomputed the example by hand.

**Evidence.** Lemma gf:first-event (MA/05_global_formation.tex:548-565) shows only that the full and label-preserving histories agree up to the first event. (F5) compares the histories on [0,∞) (MA/05_inheritance.tex:1840-1846), and no hypothesis prevents a later event in the null alone.

The counterexample is a Gaussian instance of gf:model:

- **Setup:** N=2, s²=1, ρ²=1/4, τ²=1/10, σ²=4, catalog {Π_⊥, Π_12} (admissible under gf:catalog, :45-48), d_o²∈(1.42, 2.02).
- **Full flow:** P=(⊥, Π_12), with one event.
- **Label-preserving null:** P⁰_lp=(⊥, Π_12, ⊥).
- **Renormalized null:** P⁰_rn=(⊥).
- **Robustness:** all inequalities are strict, so (F5) holds on an open set by the continuity argument at :632-638.

This is the mechanism that Remark gf:regrouping (:745-758) itself names. The verifier's caveat stands: with the full three-structure catalog these data are not one-stage. The declared-instance verdict (:696-702) is unaffected because it rests on direct computation.

**Correction to the report.** The diagnosis stands. The corollary needs an unstated hypothesis: neither flow has an event after n_1, or the horizon ends at n_1. Without it the statement is false, and it contradicts the chapter's own remark.

**Smallest manuscript fix.** At MA/05_global_formation.tex:567-569, replace "a construction of this class with one selection stage fails (F5)" with "the first event cannot witness (F5), and a construction of this class in which the full flow and the label-preserving null come to rest at the first-event structure without further events fails (F5) (cf. \cref{gf:regrouping})". At MA/05_inheritance.tex:2095, change "later stages" to "events after the first, of the full flow or of the null".

## T1.4 CA conj:coh-walls reported false

**Final status:** confirmed with correction. The verifier and skeptic agree.

**Evidence.** Take N=2, J=1, h=(0.6,−0.6) with Φ_code from CA/app06_coherence.tex:173. Then Φ(+,−)=−0.2 is the unique minimum, which gives 2 domains. The walk has range 0.6<J, so Ψ=0. The conjecture at app06:210-212 allows only {0,1}, so it fails.

Two independent exhaustive searches agree:

- 3000 instances: domains−Ψ ∈ {0,1,2} on chains, walls−Ψ ∈ {−1,0,1} on rings.
- 1500 instances: 62 chains with value 2, including an N=10, Ψ=1 case.

The mechanism is that each chain end needs an aligned sum of only J/2. The proof of thm:coh-domains-1d (app06:217-226) uses lem:coh-counting, lem:coh-drawdown and the renewal SLLN. It never uses the conjecture. The conjecture's asymptotic clause survives, since the discrepancy is O(1), but it remains unproved.

**Correction to the report.** Delete "thm:coh-domains-1d depends on it". The theorem's bounds 1/2 (J/h)² and 26(J/h)²+7 stand. Downgrade the issue from a theorem-level defect to a false side conjecture. Add that the main-text paraphrase at CA/06_coherence.tex:174 is also false on open chains. The ring range {−1,0,1} is supported only by sampling and the note's self-reviewed C2.

**Smallest manuscript fix.**

- At CA/app06_coherence.tex:211, state that the domain count lies in {Ψ, Ψ+1, Ψ+2}, because the two chain ends can each carry a domain of aligned sum J/2. Keep the asymptotic clause.
- At CA/06_coherence.tex:174, change "agree in number up to one" to "differ by at most two on open chains". Keep the ring statement labeled as a conjecture.

## T1.5 CA conj:sca-common-code reported refuted

**Final status:** confirmed with correction. The verifier and skeptic agree.

**Evidence.** The conjecture (CA/s08_scale.tex:12-14) restricts neither the code rank nor the number of world channels. CA/02_framework.tex:36 allows any full-row-rank T_c, and :13 allows several world channels per attention set. Two independent multiprecision reconstructions, at 50 digits and 40 digits, reproduce both counterexamples.

| Case | Code | f | Result | Margin over the conjecture's f^p |
|---|---|---|---|---|
| C3 (frozen) | rank-2, H=diag(10, 0.15) | 0.9999 | ρ(W)=1.00012879, violates (M) | ρ/f−1 ≈ 1.9e-4 to 2.3e-4 |
| C4 (period 2, two channels per agent) | rank-1, H=(100, 0) | 0.995 | ρ(W^(2))=1.00689293, violates (M) | ρ/f²−1 = 0.0178 at f=0.95 |

These margins are about 10^11 times larger than double-precision error. A rank-one frozen control reproduces prop:min-common-code (09_minimal.tex:20-24). (M) has independent proven sufficient conditions: prop:sca-sufficient (08_scale.tex:50-56) and prop:min-grounding-moment (09_minimal.tex:37-43). The conjecture is listed among results that are not established (08_scale.tex:396; 13_discussion.tex:19).

**Correction to the report.**

- Report margins as ρ/f^p − 1, not ρ − 1 = 1.3e-4.
- Replace "underpins the moment bound every collective needs" with: (M) is needed, it has proven sufficient conditions, and the conjecture was only the hoped-for extension to general level-1 codes.
- Drop the "restate as rank one" step, because C4 is a rank-one counterexample.
- Whether C3 and C4 are reachable under EFE selection is unverified, but the conjecture as worded does not require it.

**Smallest manuscript fix.**

1. Narrow the conjecture to frozen rank-one profiles (ρ(W) ≤ f). This becomes a proposition only after the note's C2 proof is independently checked; only its Step 1 has been spot-checked.
2. Alternatively, narrow it to periodic rank-one profiles with at most one sensing channel per agent.
3. Add a remark giving C3 and C4.
4. Revise the "one common code suffices" sentences at 08_scale.tex:61 and :396, 09_minimal.tex:35, s09_minimal.tex:133 and :181, 11_predictions.tex:13 and :152, 13_discussion.tex:19, and s01_introduction.tex:148.

## T1.6 MA primary-objective contradiction and weakest theory

**Final status:** confirmed with correction. The verifier and skeptic agree.

**Evidence.** README.md:18-20 ("Current state (2026-10-29)", "No objective is declared primary") was last edited in commit 4ca4e7a. Commit aecb3e0 (2026-10-30), "Make the global free energy primary for formation", changed AUTHORING.md:35, MA/03_dynamics.tex:6 and 06_outlook.tex:10, but not the README.

The objective each chapter uses, in the input order of MAgent_Theory_2.0.tex:25-36 (not main.tex):

- **05_global_formation:** the global free energy.
- **06:** a modified nonsmooth potential.
- **07:** the reciprocal potential, with law-dependent channels.
- **08, 09:** the Gibbs-reduced potential.
- **10:** identity channels, evolving rows, and a finite coin realization.
- **11:** Wishart laws.
- **12:** a bit × angle space.
- **13-14:** the per-agent objective.

prop:dyn-no-global-vfe (03_dynamics.tex:472-490) needs finite alphabets and fixed rows. In addition, part (a) needs an identity peer channel, and part (b) needs fixed input-dependent channels with product recognition. Both proofs were re-derived by hand. rem:dyn-no-global-scope (:495) excludes E_red, so none of the formation chapters 06-12 meets the hypotheses exactly, and 10 nearly does. op:dyn-three-pictures (:581-582) is open beyond the mean slice, the type lattice and fixed channels.

**Correction to the report.**

- Call the contradiction a stale status document, not a manuscript contradiction.
- Replace "which is not a global VFE" with the scoped hypotheses above. Chapters 06-12 fall outside the primary objective because the author declares it (AUTHORING.md:39 and the chapter intros), not because of the proposition.
- thm:dyn-registered applies only to the finite-alphabet settings (08 and the 10 coin realization), not to 07, 11 or 12.
- "Weakest theory" is evaluative but supported. The only construction under the primary objective is a two-stage selection in which (F5) is split and fails and (F6b) fails (06_outlook.tex:10).

**Smallest manuscript fix.** Update MAgent_Theory_2.0/README.md:18-20 to the 2026-10-30 standing. Optionally, add one sentence near MA/03_dynamics.tex:492 saying that no formation chapter meets the hypotheses of the proposition exactly. In the comparison report, change line 152 to "under its hypotheses".

## T1.7 CA EFE layer absent from collective theorems

**Final status:** refuted, with a narrower claim that stands. The skeptic labels the verifier's refutation "confirmed-with-correction", meaning the refutation is upheld with two corrections. I checked both corrections against the text.

**Evidence.** CA/02_framework.tex:260 (re-read) defines attention, addressing and content as policies selected by expected free energy. The verifier cited this as s01_introduction.tex:260, but that file has 158 lines. Collective-level results that take EFE selection as input, with γ or the γ=∞ argmax changing the conclusion:

- thm:agy-agency (05_agency.tex:189-210)
- thm:agy-heterogeneous (:214-235)
- thm:frm-formation, with thresholds γ_S, γ_M, γ_T (07_formation.tex:135-160; attention q ∝ exp(γV), :38)
- thm:coh-withdrawal (06_coherence.tex:48-62)
- prop:coh-code-potential and thm:coh-domains-1d (06:152-180). The skeptic checked the Ising mismatch formula ½(1−tanh^d(γJ/2)) by hand.
- prop:sca-routing (08_scale.tex:86-99)

CA/07_formation.tex:284 and :286 (re-read) state that at γ=∞ with σ_α²=0, clauses (T1)-(T3) and (T5) are theorems. The contrast clause (T3) holds via thm:frm-split-contrast under EFE attention. So the verifier's line "contrast under EFE-selected attention is open" is wrong at γ=∞. What remains open:

- finite-γ contrast (computed only);
- the stochastic-approximation step (open:frm-closure);
- Markov closure and agency of an EFE-formed collective;
- endogenous a, ε.

The quantitative level-0 theorems do assume fixed gains and exogenous attention (02_framework.tex:311-315). 01_introduction.tex:152 says "mostly". The cited 01_introduction.tex:312 does not exist (the file has 162 lines).

**Correction to the report.** Replace T1.7 with: "CA's quantitative level-0 theorems (contrast, closure, clustering, H1, H4, H5a) assume fixed or exogenous attention. EFE selection enters agency, withdrawal, formation, code domains and routing, at frozen decision or calibration states, at γ=∞, or through Lipschitz bounds. At γ=∞ in the two-group model, EFE attention is carried through to the world-conditional precision and contrast. No theorem gives Markov closure or agency for an EFE-formed collective, or contrast at finite γ." Closure is not only an OU result, because discrete-time results exist (thm:apx-level0, thm:apx-markov-discrete). Fix the citations to 01_introduction.tex:31,152 and 02_framework.tex:260 and :311-315.

**Smallest manuscript fix.** None is required. Optionally, add one sentence after def:fw-level0 (02_framework.tex:~315) listing the EFE-dependent results and their frozen-state or γ=∞ scope.

## T1.8 Gauge structure has no dynamical role

**Final status:** confirmed with correction, narrowed. The skeptic adds a correction to the verifier, and I adopted it after re-reading the text.

**Evidence.** For MA, the strongest support is MA/02_geometry.tex:7: no vector field in ch.3-12 depends on a connection, and "no selection or inheritance result there depends on a connection or a holonomy". MA/10_boundary_closure.tex:4 ("does no dynamical work") applies to that construction only. MA does give the gauge structure dynamical roles outside formation:

- In ch.15 the connection is an auxiliary field, with no kinetic term, that is eliminated into the contextual Fisher flow (15:4, :580, :629-633).
- In ch.17-18 the dictionaries are learned link variables, and a linearized-holonomy loop prior enters their flows (17:313, :330; 18:46-61, :139, :203-220).
- ch.19 does not select a partition (19:266).

For CA, the verifier's replacement wording fails. CA/07_formation.tex:30, :53, :70 and :92 (re-read) put Rot(φ) between the groups and learned translations Θ_ij = Rot(α̂_ij). The mistranslation Υ_ij = Rot(φ_ij) enters C1g calibration and drives the withdrawal-to-split chain (07:284, "once calibration registers mistranslation"). CA/13_discussion.tex:55 (re-read) states that true translations are flat, so holonomy measures learning or model error.

**Correction to the report.** Retitle the item "No connection curvature or holonomy drives formation in either manuscript". MA's gauge structure has dynamical roles in ch.15 and ch.17-18. CA's per-edge translation error, which is gauge-variant link data, drives its formation chain, but curvature does not because true translations are flat (prop:coh-flat-true). A unification therefore goes beyond kinematics: it includes link-learning dynamics (CA/app06_coherence.tex:87 imports MA's it1:learning). It is missing a curvature mechanism for formation.

**Smallest manuscript fix.** None. Edit the comparison report only, and cite MA/02_geometry.tex:7 as the primary citation.

## Re-ranking by importance after verification

1. **T1.1:** this is the program-level gap. Neither manuscript has an instance of its full central object, and verification only removed the H5 overstatement.
2. **T1.5:** this is a false conjecture that nine sites in CA present as the open remainder for (M). It has two high-precision counterexamples, and its natural restatement is also refuted.
3. **T1.3:** a stated corollary in MA is false, as a two-agent counterexample within the chapter's own model class shows. The fix is a one-sentence hypothesis.
4. **T1.2:** the failures are real, but CA fails a survive clause, MA has formal passes in ch.13 and ch.06, and the cross-manuscript transfer claim is wrong. The issue survives only as two separate limitations.
5. **T1.4:** the conjecture is false in two places in the text, but no theorem depends on it, so the damage is limited to wording.
6. **T1.8:** after narrowing, what is left is a framing point: curvature does not drive formation. The headline "no dynamical role" is false.
7. **T1.6:** the contradiction is a stale README. The substantive residue, the open op:dyn-three-pictures, is already declared open in MA.
8. **T1.7:** the headline is refuted. The surviving narrower gap (closure, agency and finite γ for EFE-formed collectives) is acknowledged in CA through open:frm-closure.
