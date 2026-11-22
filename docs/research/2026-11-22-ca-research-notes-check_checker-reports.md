# Checker reports: Collective_Agents research notes (appendix A, 2026-11-22)

This file is the rendered output of nine fresh-context proof checkers, one per group of notes under `manuscripts/Collective_Agents/docs/research/`. Each checker saw the finished notes and scripts and not the reasoning that produced them. The text is the checkers' own and has not been adjudicated; where the integration map (appendix B) or the main report disagrees with a checker, the main report says which reading the sources support. The checkers' own scripts and outputs are in `2026-11-22-ca-research-notes-check-artifacts/checker-scripts/`.

## Checker group `agy_synchronous`

No mathematical defect found in C1 to C4: each derivation was reconstructed and survived small, degenerate and extreme instances. The conjecture as it stood before the 2026-11-21 remaining-issue integration is the same-precision reading and is proved by C1 for all n>=2; the free-precision question is settled as the note says (impossible for binary policy sets, possible for three members with three policies). Three qualifications: the binary impossibility depends on which policy is designated null (my counter-instance with one null exchanged), the manuscript infers "agency index 1" from a computed instance and not from the proved existence statement, and the record itself is stale (status active, "not integrated") although C1, C2(1,2), C4 and the C3 instance entered s05/app05/chk05 in the 2026-11-21 remaining-issue integration. C2(3) and the C3 existence theorem are not in the manuscript.

Coverage. Checked by reconstruction plus my own computation: C1 (identity, iff, strict inequality), Harris lemma, C2(1), C2(2), C2(3), Peretto lemma, C3 Steps 1-3 and the computed instance, C4 both parts, the Gaussian remark: 11 items. Checked roughly: none. Not verified: the note's numerical search for non-product fixed points (no artifact) and the earlier fresh-context checker sessions named in its review log (not available). Not rechecked: the older numbers of chk:agy-agency that come from another script (0.033, 5.4e-4, two-member values). mpmath interval arithmetic was taken as correct. No literature lookup; Peretto and Harris are proved inside the note and I checked those proofs, not the sources.

### Note `conj_agy_synchronous.md`

Target: conj:agy-synchronous (label removed from the manuscript in the 2026-11-21 remaining-issue integration; now prop:agy-synchronous-exact and ex:agy-synchronous-cycle in s05_agency.tex:107-130)

Declared record status: active (all four claims 'proved', Review: fresh-context, 'Next: Ready for manuscript integration if requested')

Status justified? The locked statement asked (i) to settle the conjecture 'for three or more data-sharing members under (P0)-(P3) revising simultaneously with a redundant pair, the stationary law differs from prod_i E_i e^{-gamma G_C} for every gamma>0', and (ii) whether P_sync(gamma) can equal a group posterior at another precision gamma_C>0, with the same or another redundant model with product habits. Git history confirms (i) is the conjecture's literal text; C1 proves it, for n>=2, with no weakening. (ii) is answered: no for binary policy sets with the nulls fixed (C2), yes for n=3 with three policies (C3 existence for small delta, C4 closed form). Both parts are settled, so 'active' is justified only by the residual parallel-Gibbs question, which lies outside the locked statement. The lines 'Ready for integration' and 'No .tex files were modified' are false as of the 2026-11-21 remaining-issue integration.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C1 | proved | confirmed | For X~P_C and one synchronous step Y, P(Y_i=0,Y_j=0)-P(X_i=0,X_j=0) equals a sum over contexts c of P_C(c) p_c(0,0)[chi^2(p_c\|\|r_c x s_c) + sum_ab p_c(a,b)^2/(r_c(a)s_c(b)) (e^{gamma I_c(a,b)}-1)] >= 0. Hence P_sync=P_C iff all conditional redundancies vanish iff P_C is a product law, and P_sync != P_C for every gamma>0 when some pair has unconditional redundancy. | Reconstructed Steps 1-4 by hand (two-order expansion of I(o_A;(eta,o_B)\|o_O), residual identity, null-indicator specialization, telescoping to additivity). Exact rational check of the identity on 69 (law,pair) cases, n=2,3,4, arbitrary full-support laws: difference exactly 0; planted wrong weight p/(rs) differs in 69/69. Step 1 compared with conditional mutual information computed from the joint law of observations at 54 points (error 9e-16) and on XOR (ln 2). Extremes gamma=1e-4..40, n=2, zero redundancy (TV 4e-16). | The strict inequality is not uniform: TV(P_sync,P_C) was 4e-6 at gamma=1e-4 and 1e-8 at gamma=40 on a 3-member instance. No quantitative lower bound is claimed or available. |
| C2(1) | proved | confirmed | With binary policy sets the synchronous kernel is antitone and maps positively associated laws to positively associated laws, so P_sync is positively associated. | Reconstructed the log-odds step, the monotone coupling, the total-covariance step, the Harris induction and the limit. n=4, slot dimension 1 or 2, 40 random Gaussian models, all 166^2 pairs of nontrivial monotone Boolean functions: min covariance -1.6e-15 (roundoff); the same test rejects P_C in 40/40 models. Antitone conditional checked directly from K_i. |  |
| C2(2) | proved | confirmed-with-correction | On {0,1}^n, P_sync equals no group posterior prod E~_k e^{-gamma_C G~_C} with product habits, gamma_C>0, the same null policy 0, and a pair whose policy-1 slots are redundant: such a posterior has Cov(X_i, 1[X_{-i}!=0])<0, or lacks full support. | Reconstructed both cases (log-odds difference -gamma_C I(o_i; o_{A(c)}), averaging over c!=0, covariance formula, support mismatch). Probed the fixed-null hypothesis with a constructed instance. | Scope, not defect: the result fails if a member's null label may be exchanged. Binary chain 0-1-2 (member 1 reads both coordinates in separate slots, gamma=2): P_sync has log odds ratio +0.026281 between members 0 and 2 and 1e-14 on the other pairs; with member 0's policy 1 taken as null it is the group posterior of a model with redundancy J/gamma_C=0.037545 at gamma_C=0.7 and full-support product habits, TV 8.0e-16 (control with the original nulls: 4.2e-3). The note states 'same distinguished null policy 0'; the manuscript commentary does not. |
| C2(3) | proved | confirmed | For any finite policy sets, if all within-block conditional redundancies vanish for a bipartition C=U+W, then P_sync = mu_U x mu_W. | Reconstructed (K_i depends only on the other block, block-product map, Brouwer, uniqueness). n=4, shapes (3,2,3,2): TV to mu_U x mu_W 6e-15, to the full product 1.9e-3; planted within-block redundancy gives 7.7e-4. | Not in the manuscript. |
| C3 | proved (existence for delta<delta_0(eps)); instance at eps=0.05, delta=0.1 given as computed | confirmed | For every eps in (0,7-4sqrt3) and small delta there is a 3-member, 3-policy linear-Gaussian collective on 12 coordinates, with positive pairwise redundancies and common habits, whose synchronous law at gamma=1 equals P_C(gamma_C;E,G_C) for the same E and G_C with 0<gamma_C<1. | Peretto lemma: reconstructed, and exact rational detailed balance on three shapes (asymmetric V fails). Step 1: recomputed every Z(u,v) and the factorization by hand. Step 2: derived the delta->0 system by sympy series from the exact Z (orders 0,1 vanish; order 2 minus the note's F_k is 0), confirmed the root, det J0=-24 eps^2(1-eps)^2/(1+eps)^2 and kappa0=0 at eps=7-4sqrt3. Step 3: reconstructed slot bookkeeping and pragmatic terms; independent rebuild from 12x12 log-determinants (\|G - pairwise form\|<=6e-16, TV to P_C(gamma_C) 2.9e-15, to P_C(1) 6.786574e-3). Instance: 50-digit solve (gamma_C=0.010398019507780068..., stationarity residual 2e-51) and a Krawczyk interval test, K(X) inside X at radius 1e-12; displaced center not certified. | delta_0(eps) is not quantified, so the note's proof does not cover delta=0.1; my interval certificate does, but it is one unreviewed computation. Shown for n=3 and three policies only; 'once \|A_i\|>=3' needs a padding argument the note does not write, and mixed policy-set sizes are open. |
| C4 | proved | confirmed | For the clockwise 3-cycle with any gamma>0, habits and costs, P_sync equals in closed form the group posterior of the reversed-cycle model (redundancy J~/gamma_C>0, tilted product habits) for every gamma_C>0, and differs from P_C(gamma';E,G_C) for every gamma'>0. | Reconstructed Z_k, the identity Z(1,2)Z(0,0)-Z(1,0)Z(0,2)=-(1-alpha_i)(1-alpha_k)w_k(1)w_k(2), the factorization, h~_i and the conditional log odds ratio. Own implementation from the manuscript's formulas: 12 random instances with gamma_C != gamma and pragmatic terms, max TV 8e-15; extremes gamma=1e-3..30; planted pairing (policy 1 with policy 1) gives 3e-3; scan of gamma' in [0,3gamma] never closer than 2.5e-2 in the listed cases. |  |
| Scope remarks | remark / open question | not-verified | Gaussian residual identity Cov(Y)-Cov(X)=D^{-1}(Lambda-D)D^{-1}; numerical searches on {0,1}^3, {0,1}^2 x {0,1,2}, {0,1}^4 found no strictly positive non-product fixed point of parallel Gibbs. | Gaussian identity derived and evaluated (error 3e-17). The search claim was only read. | No script or output for the search exists in the checks folder. The same holds for the '40-digit' solve quoted in C3 Evidence, which I reproduced at 50 digits. |

Script audit. Rerun output equals the stored output after UTF-16 to UTF-8 conversion (61 lines, rc 0, 3 s; fixed seeds). Every number quoted in the note and in chk05_agency.tex:36 agrees with the output. Most blocks could fail: XOR identity (<1e-15), positive-association scan, P_C witness covariance, three-policy and collider controls, first-principles 12x12 construction against the pairwise form, TV, stationarity and detailed-balance assertions, perturbed-B12 control, reversed-cycle comparison. Weak points: the 60-pair Gaussian identity error is printed and never asserted (lines 220-227), and the accompanying 'tv_dist > 0.0' passes on roundoff; the 'GHZ' control prints a hard-coded 'True' and computes nothing (line 278); the symbolic block checks a hand-typed limit system and never derives it from Z (my series expansion closes that); check 4 tests only gamma_C=gamma. I added exact or high-precision checks with planted-error controls for each claim.

Remaining open:
- Note's own question: strictly positive non-product fixed points of parallel Gibbs with mixed-sign interactions, n>=3.
- Which redundant group posteriors in a declared class synchronous revision reproduces with three or more policies; mixed binary and ternary collectives; sizes beyond n=3, |A_i|=3 without padding.
- A quantified delta_0(eps) for C3, or an independent rerun of the interval certificate at (0.05, 0.1).
- Independent check of the null-exchange instance before it is used in the manuscript.
- Synchronous revision without (P0), heterogeneous beliefs: not addressed.
- Record housekeeping: close the record, log the integration, add the two missing artifacts.

### Findings

**agy_synchronous/F1** (minor, status-or-scope) at conj_agy_synchronous.md C2(2); s05_agency.tex:111 and commentary at :117

The binary impossibility (no redundant group posterior with product habits and gamma_C>0) holds only with the null policies fixed. With one member's null label exchanged, a binary chain of three reproduces such a posterior exactly.

Evidence: Chain 0-1-2, member 0 reads eta_a, member 2 reads eta_b, member 1 reads both in separate slots, gamma=2. Peretto form gives P_sync ~ prod f_i(pi_i) e^{+J pi_0 pi_2}, J>0 since Z_1(1,1)Z_1(0,0)-Z_1(1,0)Z_1(0,1)=w_1(0)w_1(1)(1-alpha_01)(1-alpha_12)>0. Computed J=0.026281; relabeled model with redundancy J/gamma_C=0.037545 at gamma_C=0.7 matches P_sync to TV 8.0e-16; original nulls give 4.2e-3 (c2_check.py block C).

Fix: Keep the proposition. In the sentence at s05_agency.tex:117 say the impossibility is relative to the declared null policies, pointing to the existing remark at :200. Have the instance rechecked first.

**agy_synchronous/F2** (minor, status-or-scope) at s05_agency.tex:128 (last sentence of ex:agy-synchronous-cycle); note C3

The manuscript concludes 'so it has agency index 1' from a total variation of 2.1e-16 at a computed point. The note's proof gives existence only for delta<delta_0(eps), unquantified, and the manuscript does not cite it.

Evidence: C3 Step 2 is an implicit-function argument at delta=0. Reported b, c, gamma_C are rounded irrationals. My Krawczyk test (mpmath interval arithmetic, c3_check.py block D) gives K(X) strictly inside X for radius 1e-12 around the 50-digit root, so an exact root with b,c>0 and 0<gamma_C<1 exists there; displaced center (1e-6) is not certified; interval Jacobian agrees with finite differences to 2e-21.

Fix: State the existence result for the exact claim and present the numbers as an instance, or cite an interval certificate at this point after an independent rerun.

**agy_synchronous/F3** (minor, status-or-scope) at conj_agy_synchronous.md Verdict, C3 heading, Scope section

'Fails as soon as |A_i|>=3' is shown only for three members with exactly three policies.

Evidence: Both constructions (C3, C4) have n=3 and A_i={0,1,2}. Larger sizes need a padding argument (a non-null policy opening no slots; an added member with own-policy expected free energy identically zero) that the note does not give. Collectives mixing binary and ternary members are covered by neither C2 nor C3.

Fix: Reword to 'there are collectives with three members and three policies each'; list mixed sizes as open.

**agy_synchronous/F4** (minor, integration) at conj_agy_synchronous.md lines 3, 10, 59, 71, 81, 94, 262

The record says it is active, ready for integration, and that no .tex file was modified; the manuscript has carried the results since the 2026-11-21 remaining-issue integration and the target label no longer exists.

Evidence: s05_agency.tex:107-130, app05_agency.tex:193-236, chk05_agency.tex:36, 05_agency.tex:251, s01_introduction.tex:146, ext3_obj.tex:165, 10e_open_problems.tex:80 all state the results; grep finds conj:agy-synchronous only in the note. Note last committed in the 2026-11-21 C2 adoption, before the 2026-11-21 remaining-issue integration.

Fix: Close the record, log which claims went where (C1, C2(1,2), C4, C3 instance) and which did not (C2(3), C3 existence theorem), and move the residual question to its own entry.

**agy_synchronous/S1** (minor, script) at conj_agy_synchronous-checks/verify_agy_synchronous.py:220-227

The 60-pair identity error for C1 is printed, never asserted; the paired assertion 'tv_dist(P_stat_eig, P_C) > 0.0' passes on roundoff.

Evidence: err only updates max_id_err, printed at line 227. Line 224 asserts lhs>0.0 and TV>0.0; the script's own zero-redundancy case has TV 9.0e-17>0.

Fix: Add 'assert max_id_err < 1e-13' and a TV threshold above roundoff. My exact rational check (c1_check.py) covers the identity meanwhile.

**agy_synchronous/S2** (minor, script) at verify_agy_synchronous.py:272-278; note C1 Evidence

The 'degenerate GHZ support' negative control computes nothing: it prints the literal 'fixed under sync = True'. The note cites it as confirming.

Evidence: Line 278 formats a constant string; no kernel is built for P_deg, which is outside the model class (conditionals undefined off the support).

Fix: Compute P T for a kernel defined from that law's conditionals, or delete the line and the citation in C1 Evidence.

**agy_synchronous/S3** (minor, script) at verify_agy_synchronous.py:538-553

The symbolic channel for C3 verifies a hand-typed limit system and never derives it from the exact Z(u,v).

Evidence: F1, F2, F3 are entered as formulas. My sympy series of the exact equations gives order-0 and order-1 coefficients 0 and order-2 coefficient equal to the note's F_k for k=1,2,3 (c3_check.py block B).

Fix: Add the series derivation to the script.

**agy_synchronous/S4** (minor, script) at conj_agy_synchronous.md C3 Evidence and Scope section

Two quoted computations have no artifact: the '40-digit' solve and the searches for non-product fixed points on {0,1}^3, {0,1}^2 x {0,1,2}, {0,1}^4.

Evidence: The checks folder holds one script and one output; neither contains these.

Fix: Add the scripts and outputs, or mark the statements as unrecorded.

**agy_synchronous/I1** (minor, integration) at s05_agency.tex:128; chk05_agency.tex:36

The twelve-coordinate construction cannot be reproduced from the manuscript: slot layout, common noise variance and preferences are given only in docs/research.

Evidence: The manuscript gives habits, four redundancies and gamma_C. The construction needs four slots per active policy on edge coordinates eta_{e,u,v}, R_s=e^{g*/2}/(2 pi e) and preferences N(0,R_s(1+S_s)) so that own-policy terms equal g*=ln(Z(1,0)Z(0,1))/(1-gamma_C).

Fix: Put the construction and the existence statement in app05_agency.tex.

**agy_synchronous/I2** (minor, integration) at 10e_open_problems.tex:21 (table row 'Conflicting objectives', Open column)

The table lists 'simultaneous moves' as open without qualification, while the section text and open:obj-strategic(c) say the shared-belief case is settled in part.

Evidence: 10e_open_problems.tex:80 and ext3_obj.tex:165 cite prop:agy-synchronous-exact and ex:agy-synchronous-cycle.

Fix: Qualify the entry, for example 'simultaneous moves beyond a shared belief and two policies'.

**agy_synchronous/I3** (minor, integration) at 10e_open_problems.tex:80

The summary 'with two policies per member reproduces no redundant group posterior' drops 'product habits' and 'gamma_C>0'.

Evidence: def:agy-group-model allows joint habits E_C on the profile set, and by prop:agy-index(a) free joint habits reproduce any full-support law. The proposition itself is stated correctly.

Fix: Insert 'with product habits and gamma_C>0'.

**agy_synchronous/E1** (minor, editorial) at s05_agency.tex:117

'is not a product law and lies at total variation 0.033 from it' reads as distance from the product law; the 0.033 is the distance from the group posterior.

Evidence: chk05_agency.tex:34: 'a law that is not a product law (deviation 5.4e-4) at distance 0.033 from the group posterior'.

Fix: Write 'from the group posterior'.

**agy_synchronous/E2** (minor, editorial) at verify_agy_synchronous_output.txt; verify_agy_synchronous.py docstring

The stored output is UTF-16 LE, which text tools treat as binary; the docstring cites s05_agency.tex lines 102-109, which moved.

Evidence: file(1) reports UTF-16 little-endian; diff succeeds only after iconv.

Fix: Store the output as UTF-8 and cite labels instead of line numbers.

### Collective_Agents touchpoints

| Location | Label | Relation | Detail |
|---|---|---|---|
| sections/s05_agency.tex:107-114 | prop:agy-synchronous-exact | integrated-matches | (a) equals C1(1),(2) with the same hypotheses ((P0)-(P3), finite expected free energies, n>=2). (b) equals C2(1),(2), fixed null included (policy 1 is named as the slot-opening policy). |
| sections/s05_agency.tex:117 | commentary after prop:agy-synchronous-exact | partially-integrated | 'No redundant group posterior ... at all' omits the null-policy qualifier (F1); 'from it' is ambiguous (E1). |
| sections/s05_agency.tex:119-129 | ex:agy-synchronous-cycle | integrated-matches | G_C, Z_k, J~ and the reversed-cycle model equal C4; my implementation of the manuscript's formulas reproduces P_sync to 8e-15. The last sentence uses the C3 computed instance, not the existence theorem (F2, I1). |
| sections/app05_agency.tex:193-224 | proof of prop:agy-synchronous-exact | integrated-matches | Same route as the note; hypotheses match. |
| sections/app05_agency.tex:226-236 | derivation for ex:agy-synchronous-cycle | integrated-matches | Peretto reversibility and reversed-cycle model as in the note's lemma and C4. |
| sections/chk05_agency.tex:36 | chk:agy-agency | integrated-matches | Every number agrees with the stored and rerun output. |
| sections/05_agency.tex:251 | main-text summary of sec:agy-agency | integrated-matches | Correct at summary level. |
| sections/s01_introduction.tex:146 | list of open items | integrated-matches | 'Settled at the members' own precision and for two policies per member'; cycle example cited. |
| sections/ext3_obj.tex:165 | open:obj-strategic (c) | integrated-matches | Shared-belief simultaneous revision recorded as settled in part. |
| sections/10e_open_problems.tex:80 | sec:opn-4 text | integrated-matches | Wording on simultaneous revision is right in substance; drops 'product habits, gamma_C>0' (I3). |
| sections/10e_open_problems.tex:21 | tab:opn-status, row 4 | stale-open-statement | 'Simultaneous moves' listed open without qualification (I2). |
| sections/11_predictions.tex:75 | prediction row on redundant choices | unaffected | Covers two members; the binary positive-association result could extend it. |
| sections/s12_related.tex:55; s13_discussion.tex:7; s10_abstract_collectives.tex:278; s05_agency.tex:144, :283 | citations of prop:agy-synchronous | unaffected | Two-member statements, still true. |
| sections/ (none) | C2(3) bipartite factorization | not-integrated | No manuscript statement. |
| sections/ (none) | C3 existence theorem | not-integrated | Only the computed instance appears. |

### Integration candidates

| Result | Target | Readiness | Why |
|---|---|---|---|
| conj_agy_synchronous.md C2(3): if I_{q_C}(o_{B_i(a)};o_{B_j(b)}\|o_{A_{-ij}(c)})=0 for all i,j in the same block of a bipartition C=U+W, then P_sync=mu_U x mu_W. | s05_agency.tex, part (c) of prop:agy-synchronous-exact or a remark after it; proof paragraph in app05_agency.tex | ready | Reconstructed and checked on a four-member non-binary instance with a planted control; it generalizes prop:agy-synchronous (two singletons). |
| conj_agy_synchronous.md C3: for every eps in (0,7-4sqrt3) and small delta, a three-member, three-policy collective has P_sync(1;E,G_C)=P_C(gamma_C;E,G_C) with 0<gamma_C<1. | s05_agency.tex ex:agy-synchronous-cycle, second construction; construction and proof in app05_agency.tex | ready-after-minor-fix | Proof reconstructed. The manuscript needs the construction stated and the proved existence separated from the computed instance (F2, I1). |
| Null-exchange instance (this check, F1): a binary chain of three with one null label exchanged reproduces a redundant group posterior with product habits and gamma_C>0. | s05_agency.tex:117, one qualifying sentence pointing to :200 | needs-fresh-proof-check | One derivation and one script by one checker. |
| conj_agy_synchronous.md C2(1) as a prediction: binary members revising simultaneously have Cov(f,g)>=0 for nondecreasing f,g, against the negative association of a redundant group posterior. | 11_predictions.tex:75, extension of the existing row | ready | Already proved in prop:agy-synchronous-exact(b); it supplies the sign the row's falsifier names. |
| Qualification of 'simultaneous moves' as partly settled. | 10e_open_problems.tex:21 table row; 10e_open_problems.tex:80 add 'product habits and gamma_C>0' | ready | Brings the table in line with the section text and ext3_obj.tex:165. |
| Residual open problem: which redundant group posteriors synchronous revision reproduces with three or more policies, mixed policy-set sizes, and beliefs that are not shared. | ext3_obj.tex open:obj-strategic(c) or a new open problem in s05_agency.tex | ready | The manuscript now states partial results and no statement of what is left. |
| conj_agy_synchronous.md Scope: fixed points of parallel Gibbs for general positive laws with mixed-sign interactions. | none | not-worth-integrating | Outside the group-model class and without a result; its supporting search has no artifact. |

### MAgent_Theory_2.0 bearing

None exact. Searched chapters/ and companion/ for synchronous, simultaneous, deliberation, group posterior, policy, expected free energy, potential game, logit, Glauber, heat bath, update order, redundancy, positive association. chapters/01_foundations.tex:208 states the MA models contain no action, policy or expected free energy, so the note's objects have no MA counterpart. chapters/05_global_formation.tex:95-98 ('their simultaneous update equals every sequential one' when agent blocks are conditionally independent given shared latents) shares a hypothesis shape with C1 and C2(3); the correspondence is interpretive only, since MA updates deterministic recognition laws and the note samples policies. chapters/03_dynamics.tex:346 and :467 (coordinate descent, Monderer-Shapley criterion) bear on thm:agy-agency, not on this note.

### To-do bearing

none. The results concern decision protocols under the agency clause; none of the five workstreams or the cautions of research_to_do.md refers to deliberation protocols or group posteriors.

### Checker scripts

NOT WRITTEN. The Write tool refused the report file ("Subagents should return findings as text, not write report files"), and I did not route around that; the full content is in this structured summary. Scripts and outputs I produced are in 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/agy_synchronous/ (c1_check.py, c2_check.py, c3_check.py, c4_check.py, each with a .out file).


## Checker group `walls_commoncode_nrg`

No mathematical defect found in any claim the three notes declare proved, computed or refuted; the defects are two small proof-text slips, the word "sharp", stale records, untraced numbers and integration state. conj_sca_common_code C2 and problem_8 C2 are integrated in the form proved (prop:min-common-code(d), prop:nrg-lossless). conj_coh_walls is integrated only as a counterexample and a widened conjecture: app06_coherence.tex still states as conj:coh-walls what C2 proves, and thm:coh-domains-1d(b) still carries the factor-52 bounds instead of lim = E T_J. problem_8 C1 passed this reconstruction (Step 5 error bounds only partly rederived) and an independent numerical test, but the manuscript still lists it as author-checked and open.

Coverage. 19 items across the three notes (14 claims, 5 failed routes). Reconstructed step by step: walls C2, C3, C4; common-code C2; problem_8 C2; problem_8 C1 Steps 1-4 fully and Step 5 for two of four pairings. Recomputed on the stated instance with my own code: walls C1; common-code C3, C4 (hence C1); problem_8 C4 and failed route R1. Checked roughly (derivation read plus numerics): problem_8 C3; walls R1. Open claims: common-code C5 probed by random search without a counterexample; problem_8 C5 not examined. Read only: common-code R1, R2; problem_8 R2. Not done: any literature lookup; reconstruction of lem:coh-structure, lem:coh-drawdown lower bound, thm:nrg-coarse(b), thm:nrg-ep and the level-1 reception model, all used as given; rerun of stored scripts (problem_8 fresh rerun file is missing).

### Note `conj_coh_walls.md`

Target: conj:coh-walls, lem:coh-counting, lem:coh-drawdown, thm:coh-domains-1d(b)

Declared record status: active; C1 refuted, C2-C4 proved, all Review: self; O1 (fresh-context check) and O2 (literature) open

Status justified? Justified on the mathematics. The locked statement asked to settle the two-value conjecture (domains in {Psi, Psi+1}), sharpen the wall count and sharpen the drawdown bound. Established: the two-value form is false; Psi-1 <= walls <= Psi+1 on chain and ring (upper bound for every minimizer, lower bound when no run of pulls sums to +-J); hence domains in {Psi, Psi+1, Psi+2} on the chain and lim mean domain length = E T_J a.s.; (J/h)^2 <= E T_J <= (J/h)^2 + 2.849 (J/h) + 2. The record is stale against the manuscript, which has since widened the conjecture; O1 is now discharged by this check, O2 is not.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C1 | refuted | confirmed | On an open chain the minimizer's domain count need not lie in {Psi_N, Psi_N+1}: N=2, J=1, h=(0.6,-0.6) has 2 domains with Psi=0; an N=5 instance has 3 domains with Psi=1. | Evaluated all four energies of the N=2 instance by hand (0, -0.2, 2.2, 0) and the walk and energies of the N=5 instance by hand; recomputed both with exact rationals in my own brute force (chk_walls.py): unique minimizers, gaps 0.2 and 0.36. | The manuscript's counterexample paragraph (app06_coherence.tex:215) matches. |
| C2 | proved | confirmed | For every J>0, real pulls and every minimizer on chain or ring: walls <= Psi_N+1; if no run of consecutive pulls sums to +-J then walls >= Psi_N-1; on the ring walls = Psi_N when Psi_N is even. | Reconstructed the Alternating-Jump Lemma step by step (base case with both positions of g_1, four induction cases), its application through lem:coh-structure(a), the lower bound through lem:coh-structure(c), and parity. Own exhaustive exact check with half-integer pulls including ties and all minimizers: 16,215 minimizer instances, 0 violations of the upper bound, 0 generic violations of the lower bound or of ring equality; planted bound walls <= Psi fails 157 times. | The no-tie hypothesis in the lower bound is needed: h=(-0.5,-1.5,1.0), J=1 on a ring has the all-minus minimizer with 0 walls and Psi=2. For the chain, C2 alone gives domains in {Psi, Psi+1, Psi+2}, the first clause of the manuscript's widened conj:coh-walls. |
| C3 | proved | confirmed-with-correction | Under generic pulls the open-chain minimizer has exactly Psi_N + s_flip + s_end domains (two boundary indicators) when Psi_N >= 1, and 1 or 2 domains when Psi_N = 0, read off the clipped walk D_i = clip(D_{i-1}, -J/2, J/2) + h_i. | Rederived the clipped recursion from the Viterbi recursions, the backtracking rule, the reflected-walk identity after a barrier hit, and each case (delta_1 = +-1, g_Psi < N or = N, Psi = 0). Own implementation against brute force on 3,060 random chains: 0 mismatches; dropping either indicator fails 276 and 306 times. | Line 140: for Psi=1, delta_1=+1, g_1=N, b_1<N the text asserts M_N=0 or sgn D_N = -s_last; actually M_N=1 and sgn D_N = s_last, and the count is still 1. Line 51: M_N, s_1, s_last, delta_1 are used in the statement but defined only in the proof and script. |
| C4 | proved | confirmed-with-correction | For Gaussian steps, (J/h)^2 <= E T_J <= (J/h)^2 + ((pi+4)/sqrt(2 pi)) (J/h) + 2, and the mean domain length of thm:coh-domains-1d(b) converges a.s. to E T_J on ring and chain. | Rederived the one-step expansion, g_1, g_2, H(0)=H(inf)=0, H'(0), the single sign change of H'', the overshoot moments and mu_1' = -Var, the optional-stopping limit, and the passage to the limit through C2 and the renewal law. 40-digit grid check of H>0 on (0,30]; own Nystrom solver for E T_J at J/h = 0.5..32 inside the bounds; Monte Carlo at J/h=1. | Line 162 writes the crossing event as Z_u >= r - B_{u-1}; under the stated recursion it is Z_u <= -(r - B_{u-1}) (same law by symmetry). 'Sharp' holds only for the leading term: numerically E T_J = (J/h + 1.1652)^2 to four digits for J/h >= 4, so the true linear coefficient is about 2.330, not 2.849. |
| R1 | failed route | confirmed | Failed route: the Psi+2 case does not disappear for large N; the two boundary indicators are asymptotically independent with joint probability about 6%. | Compared with stored and rerun output (72/1000 at N=400, J=4; marginals 0.262 and 0.231). Read only for the independence statement. | Asymptotic independence is a numerical observation, stated with an approximation sign; it is not proved. |

Script audit. verify_coh_walls.py exists; stored output (UTF-16) is line-for-line identical to the fresh rerun. Parts 1, 2, 3b, 3c can fail (asserts; three planted errors fail 231-479 times). Part 3a's test min_drift >= 1 - 1e-15 cannot detect a small negative H; the analytic argument and my 40-digit check carry it. The script draws only Gaussian pulls, so ties and non-unique minimizers were untested until chk_walls.py. E T_J at J/h = 4, 8, 16 quoted in the note's Test instance are not in the stored output; I reproduce 26.67916, 84.00079, 294.64390.

Remaining open:
- O2 of the note: literature on the 1D zero-temperature random-field chain and on Gaussian drawdown overshoot; not done here
- Attribution of the constant 1.1652 (true linear coefficient about 2.33) to a published corrected diffusion approximation is unchecked
- Asymptotic independence of the two boundary indicators (R1) is numerical only

### Note `conj_sca_common_code.md`

Target: conj:sca-common-code, prop:min-common-code

Declared record status: active; C1 refuted, C2 proved (fresh-context review recorded), C3 and C4 computed (Review: self), C5 open; O1-O3 unchecked

Status justified? Justified. The locked statement asked whether every frozen or periodic common-code profile of level-1 receivers in an isotropic world has period map of spectral radius at most f^p. Established: true for frozen rank-one codes on every directed listening graph with any sensing (C2); false for a frozen rank-two code and for a period-two rank-one profile with two sensing channels per agent (C3, C4, both also break (M)); open for periodic rank-one profiles with at most one sensing channel per agent (C5). The record's O1 box and the Review fields of C3 and C4 are stale against the manuscript.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C1 | refuted | confirmed | The literal conjecture (any rank, any periodic profile) is false. | Follows from C3 and C4, which I recomputed at 40 digits with my own code. |  |
| C2 | proved | confirmed | For codes H_j = theta_j T_c of rank one, any P_i > 0, any Gamma_i >= 0 and any directed listening relation, every eigenvalue of W^rec has modulus below 1 or equals 1; rho < 1 exactly when ker H^s_i and ker T_c meet trivially for every agent and every sink component contains an agent with injective sensing. Hence rho(W) <= f at a fixed point in the world F = f I. | Reconstructed both steps: reduction to scalar equations, Re(lambda c_i) > 0 off the point 1, the maximum-modulus contradiction, the lambda = 1 equation, the out-closed maximal set and sink component, and necessity through the block-triangular form. Own test at extreme scales (parameters over four decades, N up to 5, K up to 4): 4,000 instances, no eigenvalue of modulus >= 1 other than 1; distinct-code control reaches 1.086. | Requires R^s_i > 0 for ker Gamma_i = ker H^s_i (already in the manuscript form). The proof uses only Lambda_i > 0, Gamma_i >= 0, alpha_j > 0. The eigenvalue 1 may be defective, so '(C_rho) at every rate above f' is the correct form. The note's last line says '(M) in uniform form'; the supported wording is 'stationary form' as in the manuscript. In my extreme-scale run a rank-based criterion and a singular-value test for the eigenvalue 1 disagreed in 11 of 4,000 ill-conditioned instances; I did not resolve them individually. |
| C3 | computed | confirmed | Frozen, N=K=2, common rank-two code diag(10, 0.15), sensors (0.5, 0.14) and (15, 4.6): rho(W)/f - 1 is about 1.9e-4 to 2.3e-4, and rho(W) = 1.000129 at f = 0.9999. | Own 40-digit Riccati iteration and eigenvalues (chk_cc_mp.py): rho/f - 1 = 1.93192302147e-4, 2.22083041479e-4, 2.28814025797e-4 at f = 0.95, 0.99, 0.9999; fixed-point residual 0; parallel-sensor control gives 4.6e-40. | Scope stated in the note; not reported as a theorem. |
| C4 | computed | confirmed | Period two, N=K=2, common rank-one code (100, 0), sensors 200(1, +-0.3) while listening and 100(1, +-0.35) while not: rho(W^(2))/f^2 - 1 is about 0.017 and rho(W^(2)) = 1.00689 at f = 0.995. | Same script: rho/f^2 - 1 = 0.017821900195, 0.017235331272, 0.0170378859341 at f = 0.95, 0.99, 0.995; no-listening control 0.9222. Variants with one fixed sensor per agent give rho/f^2 - 1 below 1e-36. |  |
| C5 | open | not-verified | Open question: for a rank-one common code and a periodic profile in which each agent's sensing is 0 or one fixed Gamma_i, is rho(W^(p)) <= f^p? | Random search over about 16,000 converged profiles (N in {2,3}, K in {2,3}, p in {2,3}), half strictly inside the conjecture's hypotheses. Apparent excesses of 1e-10 to 1e-9, stable from 40 to 90 digits, were traced to rank-deficient float Gamma with a negative eigenvalue near -4e-12; with exactly PSD Gamma the excess is at most 1.6e-34. | No counterexample found; this is not evidence of truth beyond the sampled family. A frozen control showed the same spurious excess, which C2 forbids, and that located the artifact. |
| R1-R2 | failed routes | not-verified | Failed routes: mirror-symmetric equal-norm sensing for rank-two amplification; a block-diagonal inner product for rank two. | Read only. |  |

Script audit. verify_common_code.py, c2_blind_check.py, c2_reconstruct_check2.py: stored outputs identical to the fresh reruns; c2_reconstruct_check.py has a rerun but no stored output. Part 1 and the c2 scripts can fail (distinct-code controls 1.18 and 1.153; designed negative cases). The 'time-domain' channel in Parts 2-3 is power iteration on the same matrices, so it checks the eigen-solver, not the model. The single MISMATCH line is the conditioning artifact disclosed in chk09_minimal.tex:7. No multiprecision script is stored for the manuscript's '40 to 50 digits' statement; mine reproduces it. Numbers quoted in the note match the output.

Remaining open:
- C5 / O2: periodic rank-one profiles with one fixed sensing channel per agent
- O3: whether C3 and C4 are selected by expected free energy
- Store a multiprecision recomputation of C3 and C4 in the check folder
- Any further numerical search on C5 must build Gamma from its factor in the working precision

### Note `problem_8.md`

Target: open:nrg-rate, obs:nrg-spectral

Declared record status: active; C1-C3 proved, C4 refuted, C5 open, all Review: self; O1-O3 open

Status justified? Justified on the mathematics. The locked statement asked for (1) lim D_n(C)/n = ebar(C), (1b) D_n = n ebar - e_0 + o(1), (2) the descriptions that retain the most dissipation. Established: (1) and (1b) with an O(tau^n) remainder and an explicit e_0 (C1); (2) completely for m >= r_Omega (C2) and negatively for two natural guesses when 2 <= m < r_Omega (C4); the optimizer below r_Omega is open (C5). The Review fields are stale: C2 was already reconstructed once before this check and now twice; C1 now once.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C1 | proved | confirmed | For every full-row-rank C, S is uniformly positive definite on the circle and D_n(C) = n ebar(C) - e_0(C) + O(tau^n) for tau above r_1, with e_0 given by four 2d x 2d circle integrals and K = I - H G_1 invertible. | Reconstructed Steps 1-4 line by line (annulus of holomorphy, Fourier and Parseval bounds, circulant trace, exact rank-2d factorization of C_N - T_n without inverting A, Sylvester bound on K_N, Woodbury trace identity). In Step 5 I rederived the limit and the aliasing exponents for the left-left and left-right pairings and took right-right and right-left by symmetry. Implemented the e_0 formula from the note's text and compared with brute-force D_n: errors 7.8e-15, 6.1e-15, 1.0e-14 at n=16 on the ring pair, a non-normal d=4 system with full noise covariance, and a singular A; exponential decay visible at n=4, 8; two planted errors off by 0.05 to 10. | Residual: the O(N^2 r^N) estimates for the right-right and right-left pairings were not written out by me. Numerical agreement on three instances does not replace them. |
| C2 | proved | confirmed | ebar(C) <= ebar(I) = ep with equality iff ker C lies in ker Omega, Omega = Q^{-1}A - A^T Q^{-1}; full retention at dimension m iff m >= rank Omega; every odd-dimensional system has a lossless description of dimension d-1. | Reconstructed the precision-difference identity, the block-inverse trace identity, det equality of the Schur complements, the equality case and its translation back through the real completion G, and the integration step. Numerics: d=3 and d=5 random systems with full Q (ebar on range(Omega) equals D_1(I) to 10 digits; perturbed C strictly less; planted criterion range(A - A^T) gives 8.913 against 10.688), and a d=4 rank-two case. | For a lossless C, D_n(C) is still below n ep at finite n (e_0 > 0), as the note's script asserts. |
| C3 | proved | confirmed | ebar is invariant under C -> MC, attains its maximum on the Grassmannian, and has the stated gradient with grad C^T = 0. | Derivation read; finite differences on a random d=4, m=2 instance agree to 1.3e-11 and grad C^T = 2.3e-16. Checked roughly, not reconstructed line by line. |  |
| C4 | refuted | confirmed | For normal drift and isotropic noise the best m-plane need not be invariant, and the retained fraction is not bounded away from 1 when m < r_Omega: two oscillators at angles eps and pi - eps, C_mux retains a fraction tending to 1/(1 + sin^2 eps) as r -> 1. | Rederived the common eigenbasis, lambda_+-, the four resonance peaks and the limit; recomputed (eps, r) = (pi/3, 0.99) and (0.2, 0.998): invariant plane 0.500000, C_mux 0.570743 and 0.960691 against limits 0.571429 and 0.962029. | The fraction approaches 1 only in the double limit r -> 1, eps -> 0, and never equals 1 by C2. |
| C5 | open | not-verified | Open: closed-form maximizers of ebar on Gr(m, d) for 2 <= m < r_Omega. | Not examined. |  |
| R1 | failed route | confirmed | Failed route: top circulation planes are optimal for normal drift; a tilted plane achieves 3.150186 against 2.882353. | Recomputed 2.882353 and 3.150186; a random m=3 search reaches 3.3563 (note: 3.356297). | These numbers are not printed by the stored script. |
| R2 | failed route | not-verified | Failed route: arbitrary-frequency multiplexing of three oscillators does not approach full retention (ratio near 0.35). | Read only. | The value 0.35 has no stored output. |

Script audit. verify_nrg_rate_theorems.py and its stored output (UTF-16) exist. The fresh rerun file problem_8__verify_nrg_rate_theorems.rerun.txt is missing from the reruns folder and from _summary.txt; I did not rerun the stored script. By reading: the script compares the formula with brute force (asserts at 1e-9, 1e-12, 1e-8), has three planted errors with an assert, and checks admissibility of each instance, so it could fail. Numbers quoted in the note for C1, C2, C4 match the stored output and my own script (ebar 0.346653, e_0 +0.08843611, det K 2.403; 0.570743).

Remaining open:
- C5 / O3: maximizers for 2 <= m < r_Omega
- O2: literature on block-Toeplitz trace asymptotics and coarse-grained linear-Gaussian entropy production; not done here
- Write out the right-right and right-left error estimates of Step 5 of C1
- Fresh rerun of the stored script is missing

### Findings

**walls_commoncode_nrg/I1** (major, integration) at 06_coherence.tex:168 (thm:coh-domains-1d(b)); app06_coherence.tex:186-206, 220; 11_predictions.tex:46; s10_abstract_collectives.tex:108

The manuscript still states 1/2 (J/h)^2 <= liminf <= limsup <= 26 (J/h)^2 + 7 for the mean code-domain length, with lem:coh-counting (floor(Psi/2)-1 <= walls <= 2 Psi+4) and lem:coh-drawdown (E T_J <= 13 (J/h)^2 + 3.25). These are true but superseded by the note's C2 and C4, which give lim = E T_J almost surely with (J/h)^2 <= E T_J <= (J/h)^2 + 2.849 (J/h) + 2.

Evidence: C2 and C4 reconstructed step by step here. Exhaustive exact check: 16,215 minimizer instances including ties, 0 violations of walls <= Psi+1, 0 generic violations of walls >= Psi-1. Own Nystrom values E T_J = 4.74975, 10.00353, 26.67916, 84.00079, 294.64390 at J/h = 1, 2, 4, 8, 16, inside the new bounds and matching chk:coh-domains (4.71, 9.98, 26.75, 83.40, 306.5).

Fix: Replace lem:coh-counting by Psi-1 <= walls <= Psi+1 (upper bound unconditional, lower bound when no run sums to +-J); replace the upper bound of lem:coh-drawdown; restate (b) as an almost-sure limit; update the two table rows that quote 26 (J/h)^2 + 7.

**walls_commoncode_nrg/I2** (major, integration) at app06_coherence.tex:210-215 (conj:coh-walls); 06_coherence.tex:174

conj:coh-walls no longer states the refuted two-value form; it states the widened form (domains in {Psi, Psi+1, Psi+2}, mean length tending to E T_J) as a conjecture. The note's C2 proves the first clause for every pull sequence in which no run sums to +-J (probability one for Gaussian pulls), and the second clause follows with the renewal law already used in the proof of (b).

Evidence: On a chain domains = walls + 1 and C2 gives Psi-1 <= walls <= Psi+1. My brute-force histogram of domains - Psi over 3,060 random chains: {0: 1586, 1: 1334, 2: 140}, nothing outside.

Fix: After I1, promote the conjecture to a proposition with the no-tie hypothesis stated; keep the N=2 counterexample as the reason three values are needed; optionally add the exact identity of C3 as a remark.

**walls_commoncode_nrg/I4** (major, integration) at ext6_nrg.tex:59-66 (obs:nrg-spectral), 159-161 (open:nrg-rate), ext6_nrg.tex:3; 10e_open_problems.tex:41, 112

The rate limit lim D_n(C)/n = ebar and the constant e_0 are recorded as 'not proved here', 'derived, author-checked, used nowhere', and open:nrg-rate asks for an independently checked proof. This check supplies one independent reconstruction of problem_8 C1 and an independent numerical confirmation of its e_0 formula.

Evidence: Steps 1-4 reconstructed in full; Step 5 for two of four pairings. Own implementation of the 2d x 2d formula against brute-force D_n: |n ebar - D_n - e_0| = 7.8e-15, 6.1e-15, 1.0e-14 at n=16 on three instances (ring pair, non-normal d=4 with full noise covariance, singular A); planted errors off by 0.05 to 10.

Fix: Write out the right-right and right-left error estimates of Step 5, move the proof to appext6_nrg.tex, restate obs:nrg-spectral as a theorem, and narrow open:nrg-rate and the 10e row to the case 2 <= m < r_L. A second reader for Step 5 is advisable before the change of status.

**walls_commoncode_nrg/M1** (minor, mathematical) at conj_coh_walls.md:140 (proof of Theorem 2, case delta_1 = +1, g_Psi = N)

For Psi = 1, g_1 = N and first barrier hit b_1 < N, the proof says M_N = Psi-1 with sgn D_N = -s_last, or M_N = 0. The correct values are M_N = 1 and sgn D_N = s_last. The domain count 1 = Psi + s_end is unaffected.

Evidence: In that subcase the only barrier block in 1..N-1 is the positive one starting at b_1, and X_N is a new maximum so clip(D_N) = +J/2. Formula and brute force agree on 3,060 chains.

Fix: Treat g_Psi = N separately for Psi >= 2 and Psi = 1.

**walls_commoncode_nrg/M2** (minor, mathematical) at conj_coh_walls.md:162 (Theorem 3, Step 3)

The stopping event is written {Z_u >= r - B_{u-1}}, but with the note's recursion B_{u+1} = (B_u - Z_{u+1})_+ the drawdown crosses r when Z_u <= -(r - B_{u-1}).

Evidence: B_u = B_{u-1} - Z_u >= r iff -Z_u >= r - B_{u-1}. The overshoot law is that of -Z_u, which has the same distribution, so the bound is unchanged.

Fix: State the overshoot for -Z_u, or define the recursion with +Z.

**walls_commoncode_nrg/M3** (minor, mathematical) at conj_coh_walls.md:51 (statement of C3)

The statement uses M_N, s_1, s_last and delta_1 without defining them; they appear only in the proof and the script.

Evidence: M_N is the number of maximal same-sign blocks of indices i in 1..N-1 with |D_i| > J/2, s_1 and s_last the signs of the first and last block, delta_1 the direction of the first hysteresis switch.

Fix: Add these definitions to the statement before it is moved into the manuscript.

**walls_commoncode_nrg/S1** (minor, status-or-scope) at conj_coh_walls.md title, C4 heading, Log

The drawdown bound is called sharp. Only its leading term is sharp; the linear coefficient 2.849 exceeds the true one, about 2.330.

Evidence: Own values E T_J = 26.67916, 84.00079, 294.64390, 1099.93011 at J/h = 4, 8, 16, 32 equal (J/h + 1.1652)^2 to four digits; the upper bound gives 29.396, 88.793, 303.585, 1117.171.

Fix: Say 'sharp to leading order'. The source of the constant 1.1652 was not checked.

**walls_commoncode_nrg/S2** (minor, status-or-scope) at conj_coh_walls.md:3, 12, 75; conj_sca_common_code.md:3, 52, 61, 90; problem_8.md:47, 91

All three records are stale against the manuscript: status 'active' with the fresh-context obligation unchecked; the walls note quotes the superseded two-value conjecture; common-code C3 and C4 and problem_8 C2 are marked Review: self although the manuscript records independent recomputation or reconstruction.

Evidence: s08_scale.tex:19-21 ('recomputed independently at forty to fifty significant digits'); appext6_nrg.tex:106 ('reconstructed independently'); app06_coherence.tex:211 (three-value conjecture).

Fix: Update Review fields, obligations and the walls note's locked statement; no mathematical change.

**walls_commoncode_nrg/S4** (minor, status-or-scope) at conj_sca_common_code.md:150

The proof ends with '(M) in uniform form'. What follows from rho(W) <= f < 1 for a time-invariant W is (M) in stationary form.

Evidence: lem:sca-relations(c) in 08_scale.tex: for time-invariant W, rho(W) < 1 implies (M); prop:min-common-code(d) in 09_minimal.tex says 'stationary form'.

Fix: Change the note's wording to match the manuscript.

**walls_commoncode_nrg/X1** (minor, script) at reruns/problem_8__verify_nrg_rate_theorems.rerun.txt

The fresh rerun of the problem_8 script is missing; _summary.txt has no line for it. The stored output could not be compared with a rerun.

Evidence: Directory listing of the reruns folder; _summary.txt lists eight scripts, none from problem_8-checks.

Fix: Rerun verify_nrg_rate_theorems.py once and compare with the stored UTF-16 output.

**walls_commoncode_nrg/X2** (minor, script) at conj_sca_common_code-checks/ ; s08_scale.tex:19

The manuscript says both counterexamples were recomputed at 40 to 50 digits, but no multiprecision script or output is stored with the note.

Evidence: Search of docs/research for mpmath finds none in this check folder. My chk_cc_mp.py (40 digits) gives rho(W) = 1.00012879114439404 at f = 0.9999 and rho(W^(2)) = 1.0068929330219485 at f = 0.995, residuals 0.

Fix: Store a multiprecision script and its output in the check folder and cite it in the source comment.

**walls_commoncode_nrg/X3** (minor, script) at conj_coh_walls-checks/verify_coh_walls.py Parts 2, 3a

The script tests only Gaussian pulls, so the unconditional upper bound is never tried on ties or non-unique minimizers and the need for the no-tie hypothesis is never shown; the drift test min_drift >= 1 - 1e-15 cannot detect a slightly negative H.

Evidence: My exact check: 0 upper-bound violations in 16,215 minimizer instances with ties; 2,046 lower-bound failures when a run sums to +-J, for example h = (-0.5, -1.5, 1.0), J = 1 on a ring. 40-digit H: minimum 1.9e-199 on (0, 30], and H(0) = -0.0005 at 0.999 of the chosen alpha.

Fix: Add an exact-arithmetic tie block and a high-precision drift check to the stored script.

**walls_commoncode_nrg/X5** (minor, script) at conj_coh_walls.md:17; problem_8.md:80, 86; app06_coherence.tex:215

Several quoted numbers have no stored output: E T_J at J/h = 4, 8, 16; 3.150186, 3.356297 and 0.35 in problem_8's failed routes; and the manuscript's '5500 random rings of at most 11 agents' (the note's script runs 3,000 rings with N in {2,3,5,8,10}).

Evidence: Stored walls output lists J/h = 0.5, 1, 2, 5, 10, 20 only; stored problem_8 output Part 3 lists four C_mux cases only. I reproduce 26.67916, 84.00079, 294.64390, 2.882353, 3.150186 and 3.3563; not 0.35, not the 5500-ring run.

Fix: Add these cases to the stored scripts, or change app06_coherence.tex:215 to cite the stored 3,000-ring run.

**walls_commoncode_nrg/X6** (minor, script) at method note for any search on conj:sca-common-code (C5)

A rank-deficient sensing matrix formed in double precision as h^T h can have a slightly negative eigenvalue, which produces a spurious spectral radius above 1 that survives multiprecision if the float matrix is reused.

Evidence: In my search rho - 1 = 1.12e-10 was stable from 40 to 90 digits and also appeared for a frozen profile, where prop:min-common-code(d) forbids it; the float Gamma had smallest eigenvalue -4.3e-12; rebuilt from its factor, rho - 1 = 7.6e-36. Scaling that Gamma by 1e4 raised the spurious excess to 2.7e-6.

Fix: Build Gamma from its factor in the working precision and run a frozen control alongside every periodic search. The stored verify_common_code.py is unaffected at its scales.

**walls_commoncode_nrg/I5** (minor, integration) at chkext6_nrg.tex; 10e_open_problems.tex:41, 112

prop:nrg-lossless has no numerical check in chkext6_nrg.tex and is not cited in the open-problem register, which still lists the retained rate as open without the settled case m >= r_L.

Evidence: grep for nrg-lossless finds only appext6_nrg.tex:101 and ext6_nrg.tex:68. The note's script Part 2 and my chk_nrg.py both confirm the criterion (for example d=5: 10.6879855233 on range(L), 10.6788 perturbed).

Fix: Add a numcheck citing problem_8-checks Part 2 and cite prop:nrg-lossless in the 10e row and paragraph.

**walls_commoncode_nrg/I6** (minor, integration) at ext6_nrg.tex:159-161 (open:nrg-rate, last sentence)

The open problem asks for the best descriptions when 2 <= m < r_L. problem_8 C4 already rules out two natural answers and is not in the manuscript.

Evidence: Two oscillators at angles eps and pi - eps: every invariant plane keeps exactly half; C_mux keeps 0.570743 at (pi/3, 0.99) and 0.960691 at (0.2, 0.998), with limit 1/(1 + sin^2 eps).

Fix: Add a remark after open:nrg-rate stating that invariant planes are not optimal and that the retained fraction has no bound below 1 uniform over systems.

**walls_commoncode_nrg/E1** (minor, editorial) at conj_coh_walls.md:82-84; stored outputs in three check folders

The note's Literature table cites drifted line numbers and 'factor-of-52 bounds matched'; three stored outputs are UTF-16, which plain diff reports as binary.

Evidence: conj:coh-walls is at app06_coherence.tex:210-212 with new text; file(1) reports UTF-16 for verify_coh_walls_output.txt, verify_common_code_output.txt, verify_nrg_rate_theorems_output.txt.

Fix: Cite by label; store outputs as UTF-8.

### Collective_Agents touchpoints

| Location | Label | Relation | Detail |
|---|---|---|---|
| 06_coherence.tex:163-171 | thm:coh-domains-1d(b) | stale-open-statement | States 1/2 (J/h)^2 <= liminf <= limsup <= 26 (J/h)^2 + 7. Does not use the sharp bound. True but superseded by lim = E T_J in [(J/h)^2, (J/h)^2 + 2.849 (J/h) + 2]. |
| 06_coherence.tex:174 | text after thm:coh-domains-1d | partially-integrated | Says the constants are not sharp and conjectures at most two more domains than switches; the note proves this. |
| app06_coherence.tex:186-197 | lem:coh-counting | not-integrated | floor(Psi/2)-1 <= walls <= 2 Psi+4; the note's C2 gives Psi-1 <= walls <= Psi+1. |
| app06_coherence.tex:199-206 | lem:coh-drawdown | not-integrated | Upper bound 13 (J/h)^2 + 3.25; the note's C4 gives (J/h)^2 + 2.849 (J/h) + 2. |
| app06_coherence.tex:210-212 | conj:coh-walls | stale-open-statement | States the widened three-value form, not the refuted two-value form. Still a conjecture although C2 proves it under the no-tie hypothesis. |
| app06_coherence.tex:215 | paragraph after conj:coh-walls | partially-integrated | Counterexample equals C1; ring statement equals C2(3) with its hypothesis and is described as author-reviewed only; '5500 rings of at most 11 agents' has no stored artifact. |
| app06_coherence.tex:220 | proof of thm:coh-domains-1d(b) | not-integrated | Uses the old two lemmas and the factor 4. |
| chk06_coherence.tex:58-77 | chk:coh-domains | unaffected | Domain counts equal to Psi in four runs and Psi+1 in one agree with C3; measured means agree with E T_J. |
| 11_predictions.tex:46; s10_abstract_collectives.tex:108 | prediction and comparison tables | stale-open-statement | Both quote 1/2 (J/h)^2 and 26 (J/h)^2 + 7. |
| s01_introduction.tex:54; s11_predictions.tex:19; 12_related.tex:47; s10b_hierarchy.tex:288 | mentions of thm:coh-domains-1d | unaffected | Say 'of order (J/h)^2' or cite the theorem as a basis. |
| 09_minimal.tex:14-33 | prop:min-common-code(d) | integrated-matches | Equals the note's C2 with R^s_i > 0 and '(M) in stationary form'; hypotheses and criterion identical. |
| app09_minimal.tex:63-90 | proof of prop:min-common-code(d) | integrated-matches | Same argument as the note's Theorem 1. |
| chk09_minimal.tex:7-9 | chk:min-common-code, part (d) | integrated-matches | 4000 and 3000 instances, 1187/2813, 0.998551132517, 1.153 all equal the rerun outputs; the one threshold disagreement is disclosed. |
| s08_scale.tex:12-16 | conj:sca-common-code | integrated-matches | Narrowed to periodic rank-one profiles with sensing 0 or one fixed Gamma_i; equals the note's open C5. |
| s08_scale.tex:18-21 | rem:sca-common-code-counterexamples | integrated-matches | Values 1.9e-4, 2.3e-4, 1.00013, 0.018, 1.0069 confirmed at 40 digits here; the multiprecision claim has no stored artifact. |
| chk08_scale.tex:25-28; 08_scale.tex:59; 09_minimal.tex:36; s09_minimal.tex:133, 181; 11_predictions.tex:152; 13_discussion.tex:19; s01_introduction.tex:71, 148 | mentions of the common-code results | integrated-matches | All state: frozen rank-one proved on any listening graph, periodic with sensing conjectured, rank two and two sensing channels amplify. |
| appext6_nrg.tex:101-130 | prop:nrg-lossless | integrated-matches | Equals the note's C2, with the added lower bound 0 <= ebar(C); proof is the same Schur-complement argument. |
| ext6_nrg.tex:68 | summary of prop:nrg-lossless | integrated-matches | Ring example correct: two contrasts keep 25/27, a pair of agents 0.346653. |
| ext6_nrg.tex:59-66 | obs:nrg-spectral | partially-integrated | States the form of C1 (r_1, O(tau^n), 2d x 2d integrals) as derived and author-checked, 'not proved here', used nowhere. |
| ext6_nrg.tex:159-161 | open:nrg-rate | stale-open-statement | Asks for an independently checked proof of the limit and of e_0; this check gives one reconstruction. The part for 2 <= m < r_L stays open. |
| ext6_nrg.tex:3 | section abstract | partially-integrated | Lists the checked proof of the rate and the best low-dimensional descriptions as open. |
| 10e_open_problems.tex:41, 112 | register, energetic viability | stale-open-statement | Lists 'the rate retained by a coarse description' as open in full and does not cite prop:nrg-lossless. |
| chkext6_nrg.tex:30 | chk:nrg-indep | partially-integrated | ebar and e_0 values reproduced; no check of prop:nrg-lossless. |

### Integration candidates

| Result | Target | Readiness | Why |
|---|---|---|---|
| conj_coh_walls.md C2: for any minimizer of Phi_code on a chain or ring, walls <= Psi_N + 1; if no run of consecutive pulls sums to +-J, walls >= Psi_N - 1; on a ring walls = Psi_N when Psi_N is even. | app06_coherence.tex, lem:coh-counting: replace the statement and proof | ready | Short self-contained proof, reconstructed here; exact exhaustive check including ties and all minimizers found no violation, and shows the no-tie hypothesis is needed. |
| conj_coh_walls.md C4 (first half): E T_J <= (J/h)^2 + ((pi+4)/sqrt(2 pi)) (J/h) + 2 for Gaussian steps. | app06_coherence.tex, lem:coh-drawdown: replace the upper bound and its proof | ready-after-minor-fix | Proof reconstructed; fix the sign of the crossing event and describe the bound as sharp to leading order only. |
| conj_coh_walls.md C4 (second half): the mean domain length tends almost surely to E T_J on ring and chain, with (J/h)^2 <= E T_J <= (J/h)^2 + 2.849 (J/h) + 2. | 06_coherence.tex, thm:coh-domains-1d(b), and the rows at 11_predictions.tex:46 and s10_abstract_collectives.tex:108 | ready-after-minor-fix | Follows from the two lemma replacements and the renewal law already in the proof of (b). |
| conj_coh_walls.md C2 and C3: on an open chain with no run summing to +-J the minimizer has Psi_N, Psi_N+1 or Psi_N+2 domains; exactly Psi_N + s_flip + s_end. | app06_coherence.tex, conj:coh-walls: promote to a proposition; C3 as a remark | ready-after-minor-fix | The three-value statement needs only C2. C3 needs its symbols defined in the statement and one proof subcase corrected. |
| conj_sca_common_code.md C3, C4: multiprecision recomputation of the two counterexamples. | conj_sca_common_code-checks/ and the source comment at s08_scale.tex:21 (artifact only, no text change) | ready | The manuscript claims a 40 to 50 digit recomputation with no stored script; values reproduce. |
| problem_8.md C1: for full-row-rank C, D_n(C) = n ebar(C) - e_0(C) + O(tau^n) for every tau in (r_1, 1), with e_0 given by four 2d x 2d circle integrals. | ext6_nrg.tex obs:nrg-spectral restated as a theorem, proof in appext6_nrg.tex; narrow open:nrg-rate; update 10e_open_problems.tex:41, 112 and ext6_nrg.tex:3 | ready-after-minor-fix | Steps 1-4 reconstructed, formula confirmed on three instances to 1e-14 with planted errors. The right-right and right-left error estimates of Step 5 must be written out; a second reader for that step is advisable. |
| problem_8.md C4: with two planar oscillators at angles eps and pi - eps and unit noise, every invariant plane has ebar = ep/2 while C_mux has ebar/ep tending to 1/(1 + sin^2 eps) as r tends to 1. | ext6_nrg.tex, remark after open:nrg-rate | ready | Answers negatively two natural guesses for the open part; asymptotics rederived and two points recomputed. |
| problem_8.md C2 numerics: ebar(C) = ep on row(C) = range(L) and strictly less after perturbation. | chkext6_nrg.tex new numcheck for prop:nrg-lossless; citation in 10e_open_problems.tex | ready | The proposition is in the manuscript without a check; stored script Part 2 provides one. |
| problem_8.md C3: gradient of ebar on the Grassmannian. | none | not-worth-integrating | A tool for the open optimization, with no consequence stated in the manuscript. |

### MAgent_Theory_2.0 bearing

None found that is exact. Searched chapters 01-19 and the companion for common or shared code, rank one, Ising, domain wall, random field, hysteresis, spectral radius, amplification, Toeplitz, spectral density, reversal, entropy production, detailed balance, dissipation, Kalman, Riccati, coarse-graining. Interpretive contacts only: chapters/03_dynamics.tex:562-577 (thm:dyn-three-limits (iii)-(iv): directed per-agent rows are globally attracting without a global reading, the continuous-time analogue of prop:min-common-code(d); it breaks because MA has fixed rows on a mean slice and CA has covariance-dependent Kalman gains); chapters/17_communication_links.tex:214-223 (criterion for a common dictionary, which the common-code hypothesis presupposes but does not use); chapters/03_dynamics.tex:205-222 and 15_contextual_coupling.tex:270-287 ('dissipation' there is gradient-flow decrease, not the time-reversal relative entropy of problem_8); chapters/05_inheritance.tex:1413-1427 (an Ising chain used for partition discontinuity, unrelated to random-field domain counts). No MA statement is contradicted or sharpened.

### To-do bearing

No edit to research_to_do.md is forced by these three notes. Workstream 1: the common-code results show that a shared code excludes amplification only at rank one with frozen attention (rank two, or two alternating sensing channels, amplify), consistent with the status note that rank refined to transmissibility does not separate regimes; interpretive. Workstreams 2 and 4: the walls result gives a known-answer one-dimensional domain length, E T_J about (J/h + 1.165)^2, for a random-field Ising chain, usable as a calibration case for a dialect-atlas pilot or the Ising comparison; it yields no Markov length. Workstream 5 and the Landauer caution: prop:nrg-lossless states which linear coarse-grainings keep the spectral dissipation, in nats and without a temperature, in line with the caution. Workstream 3: none.

### Checker scripts

Not written: the Write tool refused report files for this agent, so the full report is carried in this structured output. Scripts and their logic are in 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/walls_commoncode_nrg/ (chk_walls.py, chk_drawdown.py, chk_cc_mp.py, chk_cc_rand.py, c5lib.py, c5search.py, c5verify.py, c5climb.py, c5scan.py, c5scan2.py, c5diag.py, c5fix.py, chk_cc_c5mp.py, chk_nrg.py, chk_nrg_r1.py).


## Checker group `meta_agent_rounds12`

The proved claims of rounds 1 and 2 (C1, C3a, C3b, C3c, C4, C5, C6, C7, C12 and the inequalities of C8) hold: each was rederived by hand and checked with an independent computation that carries a planted-error control. Two statements claim more than is proved: C8's consequence (no meta-agent in setting P under strict typing) depends on a baseline convention the record leaves open in O14 and fails in a computed instance under the other convention, and C6's "exactly when" needs the hypothesis that the all-ones vector is orthogonal to ker W^T. The computed claims C2, C9, C11 agree with their stored outputs (not rerun) and stand only under readings that the 2026-11-22 rulings exclude (C2) or leave undetermined (C9, C11). None of C3a-c, C6, C7, C8, C12 is in the manuscript, and three manuscript sentences about ex:met-two-firms are contradicted by outputs stored with the note.

Coverage. 15 claim headings (C1, C2, C3, C3a, C3b, C3c, C4-C12) and 7 failed routes. Checked by reconstruction plus an own computation: C1, C3, C3a, C3b, C3c, C4, C5 (statement parts), C6, C7, C8, C12, and C10 (I1, I2, I5). Checked only by comparing the note with stored outputs, not rerun: C2, C9, C11, R1-R7. Read only: Theorem F(c),(d),(e), Lemma C3-b and the mirror-group corollary of the obstruction report (not in the note's statements); the dynamic proposition S-dyn. Not checked: the exact model of ex:met-two-firms; the literature rows against their sources (none is load-bearing for a proof in scope); the correctness of the O2 rulings as readings of the manuscript. C13-C20 and R8-R16 belong to the second checker; C17-C17c were read only to compare with C8.

### Note `open_agy_meta_agent_exists.md (scope: C1-C12, R1-R7)`

Target: open:agy-meta-agent-exists (s05_agency.tex, now lines 313-315; main-text statement 05_agency.tex:403)

Declared record status: active

Status justified? Justified, with a stale Target. The locked statement asked for one linear-Gaussian population and set C meeting every clause of def:agy-meta-agent at a stated grade with r0>1 and Agency0>0, or a class-restricted impossibility proof. Rounds 1-2 established: class-restricted obstructions (C3a, C6, C8 inequalities, C10) and three computed candidates that pass only under named readings (C2 in an episode-clock model outside the time-invariant class; C9 under conditional typing of N_eff, an approximate baseline and a non-literal relay timing; C11 under five readings, with its agency index under the later ruling (j) not computed). No candidate of rounds 1-2 meets every clause under the ruled readings, so 'active' is right for this scope. The Target still quotes the open problem at lines 295-297 in its pre-narrowing wording; the manuscript problem now also requires a contrast produced by the members' interaction, and the note does not record that change of target in the Target section.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C1 | proved | confirmed | A block with world-conditional covariance alpha*I + beta*11^T (alpha>0, beta>=0), uncorrelated with the rest, is diffusive with coupling beta/(alpha(alpha+n beta)), leak 1/(alpha+n beta), r(C)=1+n beta/alpha; for -alpha/n<beta<0 the off-diagonals are positive. | Rederived by hand (Sherman-Morrison, xin=1/alpha, xout=1/(alpha+n beta)). Own exact check: symbolic for n=2,3,5; exact rational contrast on four instances embedded in a larger population incl. n=2 and beta=0; planted wrong formula 1+beta/alpha rejected; Conventions-row baseline 247/7 confirmed (chk1_exact.py). | No defect. The note's 'negative control beta=-0.1' is not in the stored output, which uses beta=-0.2. |
| C2 | computed | confirmed | Two niches of four in an episode-clock world (renewal every two rounds), single gamma=40: each niche is a meta-agent of grade (30, 0, 0.02, 0.01, 0.99) with every-round partner randomization under both clause-(c) baselines. | Compared every quoted number with stored outputs falsify_epistemic/check_B_out.txt (line B4, gamma=40), check_C_out.txt, check_D_out.txt. Not rerun, not reconstructed. | Numbers match (32.329, 7.653, 27.853, 2.774, 4.352, 4.308, 0.0151, 0.0130, 59/81 and 70/81). 'Open neighborhood of the center by continuity' is asserted without argument. Ruling O2(d) puts episodic worlds outside the admitted class, so C2 does not bear on the problem; the rulings' Consequences paragraph does not say so. |
| C3 | refuted | confirmed | (As first stated) one-signed act loadings of two non-communicating collectives on a conditioned world variable give positive Pi^c entries between every such pair. | Rebuilt counterexample E2 with own code from the specification (F=0.9, Q=0.05, R=1, Rc=0.02, b=0.2, n=4+4, g=(1.5,0.2), Kalman gains): cross entries -0.95605, Pi^c diffusive, r(C1)=10.8551, r(C2)=146.9612; control Rc=1 non-diffusive (chk2_settingP.py). | Refutation stands. The mechanism is that acts load on posterior means while contrast uses prior-mean errors, which inserts the factor phi1*phi2<0. |
| C3a | proved | confirmed | Two actor sets with disjoint ancestries acting with loading b on one conditioned scalar world direction have Cov(b1'x1, b2'x2 \| eta) = -(1/2pi) int beta1 beta2/(q+beta1+beta2+beta3) < 0; with one-signed loadings on the contrast coordinates some Sigma^c entry is negative, so Pi^c is not a Z-matrix and no collective exists. | Reconstructed every step (reduction to Cov(x~_0 \| y~), smoother symbol (J+bb'/q)^-1, Sherman-Morrison cross block, contraction, C4). Own brute-force conditioning with sensing feedback vs the spectral integral: max relative error 2.4e-15 over 30 signed non-normal draws; planted q->2q gives >=3e-2; negative in 30/30 (chk3_collider.py). | Scope to carry forward: the acts must load on the contrast coordinates at the same time index; this excludes the usual timing (acts from posterior means, contrast on prior errors) unless phi1*phi2>0, and it does not cover ex:met-two-firms (O4 open). beta_k and q are undefined in the note's statement. |
| C3b | proved | confirmed | For two exchangeable acting collectives the cross entries of Pi^c have the sign of phi1 kappa1 phi2 kappa2; for EFE-consistent acts with known effect sign the sign is positive; with prediction noise the rule holds when c0,k>0 and phi1 phi2>0. | Derived the posterior cross-spectrum, V_12, the EFE algebra (phi=a/(1+nc), phi*kappa=(b/bhat) a^2 c sqrt(n)/(1+nc)^2), the prediction-noise formula and the monotone-weight argument by hand. Own numerics: rule 120/120 (naive rule wrong 70/120), corollary 60/60 and 60/60, noise formula to 1.3e-15, rule 73/73 inside the noise condition and failing 65/77 outside (chk2_settingP.py). | No defect. The corollary uses continuous Gaussian habits, outside the finite act sets of def:agy-joint-acts; with prediction noise and a1*a2<0 the 'never diffusive' conclusion fails (stored 24/400), which the statement's noise condition covers. |
| C3c | proved | confirmed | Under C3a's hypotheses and eigen-loading J_k^-1 b_k = rho_k b_k (rho_k>0), every cross block of the precision of the actors' and ancestors' coordinates is kappa_kl bhat_k bhat_l' with kappa_kl>0; for the whole population when no outside agent reads them. | Reconstructed (Sigma^c = Phi(diag sigma - C)Phi' plus a block-diagonal complement; diag sigma - C is an irreducible PD Z-matrix). Own numerics: rank one and kappa>0 in 40/40, deviation 2.6e-15; generic loadings rank two in 40/40 (chk3_collider.py). | No defect. |
| C4 | proved | confirmed | For a positive definite Z-matrix Pi: Sigma>=0 entrywise, positive exactly within coupling components, Sigma_ij Sigma_jk <= Sigma_ik Sigma_jj, and every principal submatrix of Sigma has a Z-matrix inverse. | Neumann series, Schur complement and 3x3 cofactor rederived by hand; cofactor identity checked symbolically; 94 exact rational PD Z-matrices (50 with a negative row sum), no violation; control with one positive off-diagonal gives Sigma_12=-2/15 (chk1_exact.py). | No defect. Two of the four properties are already used in the manuscript (app10_abstract_collectives.tex:3, lem:col-kron). |
| C5 | proved | confirmed | For Sigma=D+GVG': explicit Woodbury formulas for Pi; nonpositive off-diagonals when G>=0 and V^-1+G'D^-1G is a Z-matrix; with independent sources and G>=0 diffusivity requires 'share a source' to be transitive. | Statement parts rederived by hand (Woodbury, sign via C4, transitivity via the support property); CE2 exact (8*Pi=[[5,1,-2],[1,5,-2],[-2,-2,4]]) and the mixed-sign control exact. Theorem F parts (c),(d),(e) of the report, which are not in the statement, were read only. | No defect in the statement. |
| C6 | proved (self-review) | confirmed-with-correction | For Y=WX+delta: Pi_Y = P_K/tau + R_tau with 0<=R_tau<=R_0; P_K is a Z-matrix exactly when W averages completely within blocks; lazy ring n=4 non-diffusive iff tau<sigma^2/2; one-shot lazy rings n>=6 non-diffusive at every tau; complete averaging diffusive. | Kernel decomposition, the characterization (with the Perron step), the n=4 closed form and threshold, and the n>=6 support argument rederived by hand; exact symbolic check Pi_13 = sigma2(sigma2-2tau)/(4tau(sigma2+tau)(sigma2+4tau)), values at tau=0.49, 0.5, 0.51, and n=5..8 (chk1_exact.py). | The 'exactly when' needs the hypothesis 1 perp ker W' (symmetric doubly stochastic W), which the investigator's proposition had and the note dropped: W=pp'/\|p\|^2 with p=(1,2) and W=diag(0,1,1) are exact counterexamples. The ring statements assume Sigma_X=sigma^2 I. The dynamic form (S-dyn, condition (I)) is absent from the statement and its threshold lacks a tau-uniform bound on the remainder; it rests on one computed instance (138.6 vs 150.8). |
| C7 | proved | confirmed | For one exchangeable collective that is the only actor on its scalar world component, r = r0*D_fb*D_coll in closed form and Pi^c is diffusive iff r>=1. | All five steps rederived by hand (sigma_xi^2, sigma_perp^2, decoupling of disagreement modes, two-sided smoothing integral, v and alpha). Own brute force with arbitrary fixed gains, signed F and g: 6.5e-15 over 40 draws, 'diffusive iff r>=1' 40/40, planted error (collider term dropped) >=1.6e-3 (chk2_settingP.py). | No defect. Edge case phi=0 gives a singular Sigma^c (no precision). r0 here is the no-act contrast, not the grade's level. |
| C8 | proved | status-overstated | In setting P, D_coll<=1 and D_fb<1 for EFE-consistent acts; hence if N_eff is type D for the collective, no collective in setting P is a meta-agent. | Inequalities rederived by hand and checked on 20000 draws. Consequence tested on an own exact instance under both baseline conventions (chk5_c8_baseline.py). | Inequalities proved. The consequence needs a comparison medium held fixed under the null and r0>=n-1, both stated by the investigator (reports line 371) and omitted in the note; C17b of the same record later says the conclusion fails with a recomputed baseline. Instance: r(A)=22.917, r_eff=42.630, baselines 19.786 (full) and 36.683 (null): under the recomputed baseline the null selects nothing at any admissible level and the collective differs. Earned status for the consequence: conditional on O14. |
| C9 | computed | confirmed-with-correction | The performative niche PN (two niches of four, F=0.9, Q=0.05, bgn=0.04, attention at gamma=300) meets every clause at r0 in (5.075, 24.4], alpha_I=5.61e-3, Agency0=0.94 under four readings. | Compared quoted numbers with stored outputs of two implementations (performative/check5,11,12,13_out.txt; attack-performative/a1,a4,a6,a8_out.txt). Not rerun. | Numbers match. Corrections: the headline grade uses within-step relays, not the one-round latency of the note's chosen reading (literal window (3.054, 6.169], with N_ex, alpha_I and agency not recomputed); the lower edge 5.075 and the annealed N_pr with acts use the approximation P(a\|eta)~P(a); Pi^c is for deterministic acts while agency uses a stochastic act law; the cited check8_out.txt was run at g=0.15, where the note says PN fails. |
| C10 | proved (self-review) | confirmed-with-correction | Impossibility classes I1 (own comparison medium), I2 (closed population under mean coupling; collective needs mean internal coupling above (N/n) abar), I3 (=C3a), I4 (C6 under condition (I)), I5 (same partition at gamma and gamma=0 fails the habit null). | I1, I2(a) (averaging over permutations), I2(b), I5 rederived by hand; I3 via C3a; I4 via C6. Stored impossibility_output.txt read. | I5 drops 'on the admitted class' (equality at one parameter point does not defeat an open-subset clause). I4 refers to a condition (I) that C6's statement does not contain, and inherits the unproved dynamic threshold. I1 and I2 restate manuscript results (rem:col-declared-geometry, prop:col-whole-population(b)). |
| C11 | computed | confirmed | In instance I* (two niches of four, persistent AR(1) world, raw relays with one-round latency, public optional slots, gamma=400) niche A is a meta-agent of grade (3.5, 0.02, 0.09, 0.01, 0.99) under five named readings. | Located every quoted number in stored outputs of the constructor and of the independent attack (round2_epistemic_persistent/main_real_out.txt, nulls_real_out.txt, agency_out.txt, box summaries; round2_attack_persistent/run2,3,4,6,9_out.txt). Not rerun. | Numbers match. Standing under the 2026-11-22 rulings is undetermined: agency under the literal eta_C (ruling j) is not computed (O8), nor the memory clause under the ruled initial law (O7). Agency 0.99 holds at one decision state under (P4); under the real-time protocol the stored box minimum for class G2 is 0.946. |
| C12 | proved | confirmed | With product habits E^a x E^s and G_C depending on the slot profile only, Agency <= KL_{s\|a}/(KL_a+KL_{s\|a}) and KL_{s\|a} <= sum_i max ln(1/E^s_i). | Chain-rule proof, second part and the ratio identity rederived by hand. Own numerics: 0/600 violations, superset infimum = KL_a + I(a;s) to 9e-16, attention-tilt control exceeds in 274/300, the superseded ln\|A\| bound reproduced as false (chk4_c12.py). | No defect. The 'coordinator check over 300 random laws' cited as evidence has no stored script or output. |
| R1-R7 | failed routes | confirmed-with-correction | Failed routes: two firms as a meta-agent; symmetric slot reading; quenched partner randomization scored by convention; two precisions with an episode clock; public slots as world channels; a two-dimensional coarse variable; private sensors at C11's slot cost. | Compared the quoted numbers with stored outputs (166.3 and -0.8215; 995/999 and 400/400; 6.513 vs 8.584; 0.171; 7.8176 vs 8.1577). Read only otherwise. | R1: 'mechanisms now proved in C3a to C3c and C6' overstates, since the example lies outside those classes (O4); the reopen condition needs three changes together, not one. R2: the reason covers a deterministic profile only; the stored value under random profiles is r(A)=17.40 with no baseline computed for that variant, so 'never' is unsupported. |

Script audit. No stored script was rerun and no fresh rerun was supplied. Obstruction-theory scripts compare numerical objects with independently derived expectations, print PASS or FAIL per block and carry negative controls: they could fail. Construction and attack scripts print numbers without assertions; decisions are made in prose. Attack libraries (win.py, fx.py, round2_attack_persistent/core.py) import nothing from the constructors. Monte Carlo scripts are seeded. All numbers the note quotes for C1-C12 were found in stored outputs except the C12 coordinator check (no stored output) and C1's beta=-0.1 control (stored: -0.2). performative/check8_out.txt, cited for C9, belongs to g=0.15. I wrote five checks with planted-error controls: chk1_exact.py, chk2_settingP.py, chk3_collider.py, chk4_c12.py, chk5_c8_baseline.py; my first chk3 had a transposition error that produced an order-one mismatch, so that comparison discriminates.

Remaining open:
- O3: fresh-context checks of C6 and C10; this check is one such reconstruction, with corrections (1 perp K hypothesis; dynamic threshold unproved; I5 wording)
- O4: extend C3a to stored acts used in filters and to act loadings of rank above one, so that it covers ex:met-two-firms
- O8 and O7 for C11 (agency under the literal eta_C; memory clause under the ruled initial law; literal per-round law)
- Added: restate C8 with its two conventions or tie its consequence to O14
- Added: recompute the cross-firm block of ex:met-two-firms at n_c=4 in the exact model
- Added: for C9, an exact mechanism baseline with the collider under random attention, and N_ex, alpha_I, agency under literal latency
- Added: a tau-uniform bound on the remainder for the dynamic form of C6
- Added: update the Target to the current open problem and line numbers; add C2 and C9 to the consequences of the rulings; store or replace the C12 coordinator check

### Findings

**meta_agent_rounds12/M1** (major, mathematical) at open_agy_meta_agent_exists.md, C8 Statement (line 131)

C8's consequence 'if N_eff is type D, no collective in setting P is a meta-agent' is stated without the two assumptions its proof uses (comparison medium held fixed under the null; r0>=n-1) and fails under the other baseline convention.

Evidence: Reports file line 371 states both assumptions. Own exact instance of setting P (two niches of four, Ks=Kc=0.2, F=0.9, b=0.2, g=0.125, Q=0.002, R=1, Rc=0.1): r(A)=22.9172, r_eff(A)=42.6304 (brute force = closed form); mean-coupling baseline 19.7862 from the full precision, 36.6832 from the null's. With the baseline recomputed, no level in (19.7862, 22.9172] is admissible under the null, so the null selects nothing and the collective differs at every admissible level. C17b of the same record concedes this dependence; C8 was not updated.

Fix: Limit C8's 'proved' to r <= r0*D_fb <= r0 and r <= r_eff; state the meta-agent consequence as conditional on the convention of O14 and on r0>=n-1 (or on the partition-level step C17b says is not made).

**meta_agent_rounds12/M2** (minor, mathematical) at open_agy_meta_agent_exists.md, C6 Statement (line 114)

'P_K is a Z-matrix exactly when W averages completely within the blocks of a partition' is false without the hypothesis that the all-ones vector is orthogonal to K=ker W'; the ring statements also assume Sigma_X=sigma^2 I.

Evidence: Exact counterexamples: W=pp'/|p|^2, p=(1,2) gives P_K=[[4/5,-2/5],[-2/5,1/5]], a Z-matrix with non-uniform weights; W=diag(0,1,1) gives P_K=diag(1,0,0). The investigator's S-char had the hypothesis '1 orthogonal to K (symmetric doubly stochastic W)'.

Fix: Add 'for symmetric doubly stochastic W' and 'Sigma_X=sigma^2 I' to the statement; read 'complete averaging within blocks' as columns constant on blocks with a nonsingular quotient.

**meta_agent_rounds12/M3** (minor, mathematical) at open_agy_meta_agent_exists.md, C10 (I4) and C6

C10 (I4) cites 'C6 under its condition (I)', which C6's statement does not contain; the dynamic non-diffusivity threshold is not proved.

Evidence: Proposition S-dyn proves only the decomposition Pi^c = vv'/Var(v'x') + (part on the complement). No bound on the remainder uniform in tau is given; support is one computed instance (Pi^c_13=138.6 vs kernel term 150.77) and the manuscript's 157, which the investigator did not recompute.

Fix: Add S-dyn and condition (I) to C6's statement with status 'decomposition proved, threshold computed on one instance', or supply the remainder bound.

**meta_agent_rounds12/S1** (minor, status-or-scope) at open_agy_meta_agent_exists.md, Target (line 10)

The locked statement quotes the open problem as worded before the manuscript narrowed it, with drifted line numbers.

Evidence: The note cites s05_agency.tex lines 295-297 and :296; the label open:agy-meta-agent-exists is now at lines 313-315 and additionally requires Omega_int(C|zeta_{V\C})>0 and r(C)<r0 with member channels deleted. The Log records the narrowing; the Target does not.

Fix: Restate the Target against the current label text, or add a dated line saying the original statement was answered by computation under declarations (C15) and the active target is the narrowed one.

**meta_agent_rounds12/S2** (minor, status-or-scope) at open_agy_meta_agent_exists.md, R1 (line 287) and C10 (I3)

R1 says the mechanisms of the two-firms failure are 'now proved in C3a to C3c and C6'; the example lies outside all of those classes.

Evidence: The obstruction report states that ex:met-two-firms stores acts and uses them in filters, so C3 'does not literally cover that example' (O4 open); C3b needs exchangeable firms (the example has heterogeneous noise); C6 covers it only through the unproved dynamic threshold. C3a also needs acts loading on the contrast coordinates at the same time index. R1's reopen condition 'one firm stops acting' is incomplete: performative/check7_out.txt shows the lazy ring alone still gives +168.1 (V3) and heterogeneous R a row sum of -7.74 (V4).

Fix: Write 'proved for neighboring classes; the example itself is covered by computation only (O4)', and list the three changes of the stored repair V1.

**meta_agent_rounds12/S3** (minor, status-or-scope) at open_agy_meta_agent_exists.md, C9 (lines 140-146)

C9's headline grade rests on a fifth, unlisted reading (relays delivered within the world step) and on an approximate baseline.

Evidence: attack-performative/a8_out.txt: with one-round latency r(A)=6.169, medium 3.054, N_hab 2.749, N_pr 2.238; N_ex, alpha_I and agency were not recomputed there. a6_out.txt labels the medium and annealed N_pr with acts as computed with P(a|eta)~P(a). The Scope line mentions neither.

Fix: List the timing convention among the readings, mark 5.075 and 3.67 as numerical approximations, and state which clauses are not computed under literal latency.

**meta_agent_rounds12/S4** (minor, status-or-scope) at open_agy_meta_agent_exists.md, O2 Rulings, 'Consequences' (line 401); C2 (line 53)

C2 and C9 are missing from the consequences of the rulings; C2's 'open neighborhood by continuity' is unproved.

Evidence: Ruling (d) places episodic worlds outside the class, which removes C2; C9's standing under rulings (a), (h) and literal latency is not stated. C19 proves continuity for I* only.

Fix: Add one sentence each for C2 and C9 to the Consequences paragraph; mark C2's neighborhood statement as an unproved remark or give the short argument.

**meta_agent_rounds12/S5** (minor, status-or-scope) at open_agy_meta_agent_exists.md, C10 (I5) (line 150) and R2 (lines 292-294)

I5 omits 'on the admitted class'; R2's 'never' is not supported by a computation.

Evidence: The differ clause asks for an open subset, so equality of partitions at one point is not a failure. epistemic_niche/nulls_out.txt line 11: the symmetric-owner variant has r(A)=17.40 under random profiles (policy-mixture coupling); it was compared with the baseline 18.598 of a different design.

Fix: Restore the phrase in I5; in R2 report the 17.40 and say no baseline was computed for the variant.

**meta_agent_rounds12/X1** (minor, script) at open_agy_meta_agent_exists-checks/performative/check8_out.txt; C12 and C1 Evidence lines

Three cited checks do not back the claims they are cited for.

Evidence: check8_nulls_pn.py lines 8 and 84 run at g=0.15 (S0=1.1560), while C9 is the g=0.05 instance and fails at g>=0.10. C12's 'coordinator check over 300 random laws, -4.8e-7, 24/300' and C1's 'negative control beta=-0.1' have no stored output (stored: c12_agency_out.txt 0/200 and 82/200; c1_factor_output.txt beta=-0.2).

Fix: Cite check12_out.txt for the g=0.05 quenched null; cite round3_proofcheck-o3/c12_agency_out.txt for C12; correct the beta value.

**meta_agent_rounds12/I1** (major, integration) at Collective_Agents/sections/s05_agency.tex:314 (last sentence of open:agy-meta-agent-exists)

The manuscript says the only variant of the two-firms example found to be diffusive has no consensus coupling and acts without effect on the price; outputs stored with the note contain other diffusive variants.

Evidence: performative/check7_out.txt V1 (homogeneous R, complete-graph consensus w=0.5, only C1 acting): diffusive, r(C1)=8.563 vs mean-coupling baseline 7.572 at n_c=1; 52.21 vs 45.44 at n_c=2; 140.8 vs 122.3 at n_c=4. obstruction-theory/impossibility_output.txt: complete averaging with opposite-sign acts is diffusive, contrasts 77.188 and 95.774 vs 75.074. Their other clauses are unchecked; V1's fixed protocol fails the habit null literally.

Fix: Qualify the sentence to the variants computed in chk:met-two-firms, or report the two further variants with their unchecked clauses.

**meta_agent_rounds12/I2** (major, integration) at Collective_Agents/sections/chk10a_meta_agents.tex:57 and s05_agency.tex:267

The manuscript states cross-firm precision entries 'about 0.03 at every n_c' and that the collider couples every member of C1 positively to every member of C2; the note's reconstruction gives mixed signs at n_c=4.

Evidence: performative/check6_out_latency.txt (bounded model, which reproduces the manuscript's 166.3 and -0.82 at n_c=1): cross entries in [0.0280, 0.0416] at n_c=0, [0.0241, 0.0447] at n_c=1, [-0.0164, 0.0891] at n_c=4, where 0.0891 is the largest off-diagonal entry; the manuscript's largest off-diagonal at n_c=4 in the exact model is 0.0895. The exact model was not recomputed by me.

Fix: Recompute the cross-firm block at n_c=4 in the exact model; if mixed in sign, restrict both sentences to n_c=0 and 1.

**meta_agent_rounds12/I3** (minor, integration) at Collective_Agents/sections/s05_agency.tex:314

The open problem says a commonly acted world variable and a singular consensus matrix 'both produce positive off-diagonal entries, so a solution needs a protocol and a conditioning world that avoid both'; as a general statement this is contradicted by C3, C3b and C6.

Evidence: E2 (reproduced): two collectives act on one conditioned variable, cross entries -0.95605, diffusive. C3b: sign is phi1 kappa1 phi2 kappa2. C6: complete averaging is singular and diffusive at every tau (exact: off-diagonal -sigma2/(4 tau (sigma2+tau)) for n=4). rem:agy-h1-status (line 267) says 'each destroy here', which is accurate.

Fix: Add 'in this example', or state the two conditions from C3b and C6.

**meta_agent_rounds12/I4** (minor, integration) at Collective_Agents/sections/s04_collectives.tex:272 (open:col-exact-fusion) and s05_agency.tex:313-315

Two results of the note that bear on open statements are absent from the manuscript: C5 partly answers open:col-exact-fusion, and C11 is the nearest candidate for the narrowed existence problem.

Evidence: CE2 (exact): raw-data fusion with sources shared non-transitively has Pi_12=+1/8, so exact fusion is not diffusive in general. C11: contrast produced by relays among members, deletion nulls give r(A)=1.0497 with a diffusive precision, every-round partner randomization 1.886 vs r0=3.5; blocked by O8 and O7.

Fix: Narrow open:col-exact-fusion to the dynamic and belief-message cases after stating the static result; mention the niche candidate and its blocking items in the open problem once O8 is computed.

**meta_agent_rounds12/E1** (minor, editorial) at open_agy_meta_agent_exists.md, C3a and C7 Statements

Symbols are used without definitions, and r0 has two meanings.

Evidence: C3a uses beta_k, q, beta_3; C7 uses r0, D_fb, D_coll with r0 the no-act contrast, while r0 elsewhere is the grade's level.

Fix: Define the symbols in the statements and rename the no-act contrast.

### Collective_Agents touchpoints

| Location | Label | Relation | Detail |
|---|---|---|---|
| s05_agency.tex:313-315 | open:agy-meta-agent-exists | contradicted-by-note | The narrowing is the work of rounds 3-4. Two sentences conflict with round 1-2 evidence: 'the only variant found to have a diffusive precision' (check7 V1 and the opposite-sign control are diffusive) and the general claim that a commonly acted world variable and a singular consensus matrix both produce positive entries (C3, C3b, C6). |
| s05_agency.tex:266-268 | rem:agy-h1-status | partially-integrated | Reports the collider and the singular lazy ring as computed causes with a heuristic sign argument; C3a-c and C6 are theorems for neighboring classes and are not cited. 'Couples every member of C1 positively to every member of C2' is in doubt at n_c=4. |
| chk10a_meta_agents.tex:57 | chk:met-two-firms | contradicted-by-note | 166.3 and -0.82 at n_c=1 (bounded) are reproduced by the note. 'Entries between the two firms about 0.03 at every n_c' conflicts with the stored reconstruction at n_c=4: [-0.0164, 0.0891]. |
| 10a_meta_agents.tex:271 | sec:met (status of ex:met-two-firms) | integrated-matches | Names the price collider and the singular lazy ring as the computed reasons C1 fails the collective clause in this example; consistent with R1. |
| 05_agency.tex:401,403; 00_abstract.tex:4; 01_introduction.tex:152; s01_introduction.tex:146; 13_discussion.tex:11; s13_discussion.tex:7 | status sentences on def:agy-meta-agent | unaffected | They report the audience (C15) and the narrowed problem; none cites a round 1 or 2 result. Consistent with C11 being undetermined under the rulings. |
| s05_agency.tex:240-242 | ex:agy-collider | integrated-matches | Reproduced by the note (1.391e-3 vs 1.39e-3 nats); C3a is its general form and is not stated. |
| s04_collectives.tex:272 | open:col-exact-fusion | stale-open-statement | Asks whether exact-fusion precisions are diffusive; C5 (F-share, CE2) answers no in general for one-shot raw-data fusion with independent sources, and gives transitivity of source sharing as a necessary condition. |
| s04_collectives.tex:267 | open:col-non-diffusive | unaffected | Still open. C4 supplies necessary conditions testable on Sigma^c; R3 and ruling (g) depend on this problem. |
| app07_formation.tex:104; chk05_agency.tex:70 | proof of lem:frm-split-law; chk:agy-audience | integrated-matches | Same Sherman-Morrison computation as C1 (off-diagonal -a, row sum 1/(s0+n s1)); there is no standalone lemma. |
| app10_abstract_collectives.tex:3; s04_collectives.tex:279 | M-matrix facts; lem:col-kron | partially-integrated | Entrywise nonnegative inverse and the Schur-complement property of C4 are already used; the path-product inequality and the support test are not stated. |
| s04_collectives.tex:146,153 | rem:col-declared-geometry; prop:col-whole-population | integrated-matches | C10 (I1) and (I2) restate these, including the two-cliques baseline 1+2n(n-1)a/((2n-1)eps) and significance 1.162. |
| 05_agency.tex:348 | tab:agy-nulls (N_eff row) | not-integrated | C7 and the C8 inequalities quantify what the effect null removes in setting P (r <= r_eff); the manuscript has the typing only. |
| 05_agency.tex:240-251; s05_agency.tex:88 | def:agy-agency-index; prop:agy-index | not-integrated | C12 (index diluted by internal attention, bound KL_{s\|a}/(KL_a+KL_{s\|a})) and ruling (e) on which policy components the index ranges over are not in the manuscript. |
| 05_agency.tex:333 | def:agy-nulls | integrated-matches | N_hab inapplicable without selection by expected free energy, as C10 (I5a) reads it. 'For each constant of the selector' has no declared constant set, which C8 and I5 are sensitive to. |
| 10e_open_problems.tex:15,56; 11_predictions.tex | tab:opn-status; sec:opn | unaffected | The register does not cite the label; 'No observed population is shown to meet the combined requirements' concerns observed populations. No prediction depends on the label. |

### Integration candidates

| Result | Target | Readiness | Why |
|---|---|---|---|
| open_agy_meta_agent_exists.md C1: a block with Sigma^c_CC = alpha I + beta 11^T, beta>=0, uncorrelated with the rest, has a^Pi = beta/(alpha(alpha+n beta)), eps^Pi = 1/(alpha+n beta), r(C)=1+n beta/alpha. | s04_collectives.tex, new lemma near lem:col-kron, cited from the proof of lem:frm-split-law and from chk:agy-audience | ready | Proved independently four times including this check; removes two repeated computations. |
| C12: with habits E^a x E^s and G_C depending on slots only, Agency <= KL_{s\|a}/(KL_a+KL_{s\|a}). | s05_agency.tex:88 prop:agy-index, new part; one sentence in def:agy-agency-index on which policy components the index ranges over | ready | Proved, checked three times; gives the reason for ruling (e), which is otherwise only in the record. |
| C3b: for two exchangeable acting collectives without communication, sign Pi^c_ij = sign(phi1 kappa1 phi2 kappa2); positive for EFE-consistent acts with known effect sign. | s05_agency.tex, proposition after ex:agy-collider; replaces 'heuristic sign argument' in rem:agy-h1-status for the exchangeable case | ready-after-minor-fix | State setting P, the prediction-noise condition, and that continuous Gaussian habits lie outside def:agy-joint-acts. |
| C3a: Cov(b1'x1, b2'x2 \| eta) = -(1/2pi) int beta1 beta2/(q+sum beta) < 0 for actor sets with disjoint ancestries. | s05_agency.tex, same proposition, as the general form of ex:agy-collider | ready-after-minor-fix | State the full setting (omega independent of xi, Q_w>0, rank-one loading, acts on the contrast coordinates at the same time) and that ex:met-two-firms is not covered (O4). |
| C6: Pi_Y = P_K/tau + R_tau; lazy ring n=4 non-diffusive iff tau<sigma^2/2; complete averaging diffusive. | s05_agency.tex, remark supporting rem:agy-h1-status and correcting the wording at line 314 | ready-after-minor-fix | Add the hypotheses 1 perp K and Sigma_X=sigma^2 I; keep the dynamic case as computed. |
| C7 and the C8 inequalities: in setting P, r = r0 D_fb D_coll with D_coll<=1 and D_fb<=1 iff phi^2<=F^2, so r <= r_eff. | s05_agency.tex, proposition near the discussion of tab:agy-nulls | ready-after-minor-fix | Proved; define the factors. Do not include the meta-agent consequence. |
| C8 consequence: no collective in setting P is a meta-agent when N_eff is type D. | none until O14 is settled | needs-repair | Depends on the baseline convention under a null; fails in a computed instance under the recomputed baseline. |
| C5 (F-share, CE2): one-shot exact fusion of raw data with independent sources is diffusive only if source sharing is transitive. | s04_collectives.tex:272, narrow open:col-exact-fusion | ready-after-minor-fix | Write out the map from exact fusers to D+GVG' and state G>=0; dynamic and belief-message fusion stay open. |
| C4: path-product inequality and support test as necessary conditions for a diffusive precision. | s04_collectives.tex, remark after ex:col-non-diffusive | ready-after-minor-fix | Classical; state for PD Z-matrices and point to the facts already in app10_abstract_collectives.tex:3. |
| C11 (I*): epistemic two-niche population whose contrast is produced by relays among members. | s05_agency.tex:313-315, one sentence in the open problem naming the candidate and what blocks it | needs-fresh-proof-check | Agency under the literal eta_C (O8), memory under the ruled initial law (O7) and the literal per-round law are not computed. |
| Corrections to s05_agency.tex:314 ('only variant found'; general wording on collider and singular consensus). | s05_agency.tex:314, text edits | ready | Contradicted by stored outputs and by C3, C3b, C6. |
| Correction to chk10a_meta_agents.tex:57 and s05_agency.tex:267 (cross-firm entries at n_c=4). | chk10a_meta_agents.tex:57; s05_agency.tex:267 | needs-fresh-proof-check | Requires one recomputation of the exact model at n_c=4. |
| C2, C9; C10 (I1), (I2). | none | not-worth-integrating | C2 is outside the admitted class (ruling d); C9 rests on an approximate baseline and non-literal latency; I1 and I2 are already in the manuscript. |

### MAgent_Theory_2.0 bearing

Searched MAgent_Theory_2.0/chapters and companion for: meta-agent, partner randomization, null, (F5), collider, explaining away, M-matrix, diffusive, agency index, group posterior, exchangeable, compound, world-conditional, world path. No chapter mentions meta-agents, world-conditional laws, colliders, diffusive precisions or an agency index, so no MA statement is contradicted, sharpened or instantiated by C1-C12. One definitional link is real: CA's differ clause (05_agency.tex:333) says it is clause (F5) of the formation standard, and MA's (F5) (chapters/05_inheritance.tex:1840-1846) quantifies over a constant set that (F2) requires to be declared in advance with nonempty interior (:1825-1832). CA's def:agy-nulls says 'for each constant of the selector' with no declared set, which is why the record adopted the reading 'each r0 in the admissible window' and why C8 and C10 (I5) are sensitive to which constants count. The correspondence is exact in form and breaks in two places: MA compares partition histories of deterministic flows against two named nulls, and MA's selector has no baseline, so the question behind O14 has no MA counterpart. The MA section on architectures whose selection cannot see the interaction (chapters/05_inheritance.tex:1504-1511) is analogous to C8 only in intent.

### To-do bearing

No result of rounds 1-2 advances one of the five workstreams. Two bear on the Cautions and on workstream 2, both interpretively. The caution that the world-conditional construction separates a shared driver from coupling holds only for an exogenous world: C3a and C3b show that when agents act on the conditioned variable, conditioning creates dependence of definite sign between agents that never interact, and the abstract pilot named in workstream 2 (regional price panels) is of this kind. C4 gives necessary conditions for a diffusive precision that can be tested on an estimated world-conditional covariance (entrywise nonnegativity, path-product inequality) before any contrast is computed. No edit to research_to_do.md is required by this scope; a one-line caution on agent-driven conditioning variables would be accurate.

### Checker scripts

Not written: the harness refused creation of report.md ("Subagents should return findings as text, not write report files"), so this structured summary is the full report. Scripts and outputs written for the check are in 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/meta_agent_rounds12/ : chk1_exact.py, chk2_settingP.py, chk3_collider.py, chk4_c12.py, chk5_c8_baseline.py, each with a matching *_out.txt.


## Checker group `meta_agent_rounds34`

The integrated construction P0 (C15) is numerically correct wherever I rebuilt it from the results-free specification (covariance, r(A)=5.384864, baselines, attention law, Markov defects, frozen null 7.2338, N_hab 1.456, N_pr 1.542, 128 corners, all C20 counts), and the proved claims C16, C17a, C17b (inequalities), C17c, C20(iii) and the algebraic core of C19 survive step-by-step reconstruction; the round-4 refutations of Theorem O and Proposition D are correct. The manuscript states the result at the status the record supports (observation, by computation, at computed points, open-subset clause not proved), with minor qualifier drift in five summary sentences. The record itself overstates slightly (C15 and the synthesis verdict omit the unproved open-subset clause, O10), is partly stale against the manuscript, and leaves one consequential status undecided: whether the non-interacting collider pair R11 meets every clause under the adopted rulings.

Coverage. Scope: 11 claim headings (C13-C20 with C17a-c), 9 failed routes, the obligations, the rulings, and the synthesis. Reconstructed step by step or rebuilt with own code: C14 Proposition P, C15 P0 (exact clauses, memory, attention law, frozen null, corners, N_hab and N_pr by Monte Carlo), C16, C17 counterexamples, C17a, C17b, C17c, C20 (i)-(iv), R13 for P0. Partly reconstructed: C19 (Moebius algebra, Theorem 1 logic, Theorem 3 formulas; H3-H6 and Theorem 2 read only). Stored-output comparison only: C13, C14 D1, C15 P1, C18, R8-R12, R14-R16. Not checked: P0 inference relative entropy, index at gamma 10/4/2, 999-draw test, mechanism media, 17-point design, Omega_int values, literature table. Compute note: my Monte Carlo script ran 211 s in total (above the 60 s limit; the harness moved it to the background and I let it finish with nothing else running), and a first attempt of the P1 enumeration was stopped at about 90 s and rerun in 2.6 s.

### Note `open_agy_meta_agent_exists.md`

Target: open:agy-meta-agent-exists

Declared record status: active (4 sessions); O2 ticked as ruled on the author's delegation; O1, O5, O6 discharged

Status justified? Partly. The locked statement asked for one linear-Gaussian population and set C meeting every clause of def:agy-meta-agent at a stated grade, or an impossibility proof in a class. Established: P0 meets every pointwise clause at the base point and (exact clauses) at 128 corners, nulls and index at 17 design points, under four conventions written into the definitions in the same sessions (O2 g, h, l, r) and one analyst declaration (unassigned source, O2 n). Not established: the open-subset part of 'differs' for P0 (O10 open; C19 covers I* only). 'Active' is right, but the Target still quotes the original open problem at stale line numbers (label now at s05_agency.tex:313 with a narrowed statement about interaction-produced contrast), so the record has no locked statement for the problem that is actually open.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C13 | computed, fresh-context | not-verified | Instance I** (private optional sensors, relays among two niches of four) is a meta-agent of grade (7.9,0.02,0.09,0.01,0.074) over full policies, 0.998 over sensors only. | Compared every quoted number with stored outputs (d1_frozen_out, d3_frozen_out, d6_frozen_out, attack a6_out, a7_frozen_out); all trace. No reconstruction. | Under rulings (e) and (j) its index is not computed (O8); status line should say undetermined under the rulings. |
| C14-P | proved (synthesis) | confirmed | With fixed product habits and G_C depending on slots only, Agency = (KL_{s\|a} - mis_s)/(KL_a + KL_{s\|a}). | Rederived by the chain rule: P_g = E^a x P^s_g gives KL(P\|\|P_g) = KL_a + E KL(P_{s\|a}\|\|P^s_g). |  |
| C14-D1 | computed | not-verified | Design D1 (two niches of two, eight never-opened slots) meets every clause at (3.7,0.02,0.03,0.01,0.75) with index 0.8. | Compared with d1_contrast_out, d1_npr_test_out, d1_agency_out, attack a4_out, a5_out; 0.8 = 16 ln2/(2 ln4 + 16 ln2) by hand. | Fails under ruling (k) (unused components excluded); Statement not marked superseded. |
| C15-P0 | computed, fresh-context | confirmed-with-correction | Audience of four attending a non-member source is a meta-agent of grade (4.5,0.071,0.03,0.01,0.99), or (4.5,0.03,...) with the noise-only stationary initial law; N_fr differs only under reading O2(r). | Independent rebuild from the results-free spec (own Riccati, stacked error recursion, exact Lyapunov): four covariance entries, precision, closed form (with planted-wrong control), all 26 regions, both baselines, attention probabilities, Markov defect from two initial laws, frozen null (g=0.741107, 7.2338), F=1, 128 corners; N_hab and N_pr by own two-replica Monte Carlo. Not rebuilt: inference relative entropy, index at gamma 10/4/2, 999-draw test, mechanism media, 17-point design. | Statement (line 198) still leads with the 0.071 grade from the members' stationary law, which lies outside the proviso of def:agy-closure(i); and it omits that the open-subset clause of 'differs' is supported at sampled points only (O10). |
| C15-P1 | computed, two implementations | not-verified | Variant with two channels per member passes at (4.45,0.03,0.03,0.01,0.99) at the base point and 17 design points, Omega_int(A\|zeta_S)>0, member channels lower the contrast. | Compared record and manuscript numbers with round4_p1-blind outputs, s5_box JSON and r1_out; all trace. Rebuilt only the 6^4 fixed-pattern enumeration. | 128 corners and the rate-matched N_pr at the 17 points are not computed (disclosed). |
| C16 | proved | confirmed | For a deterministic joint policy pi*, f(gamma_C)=ln P_g(pi*) is concave with f'=E_{P_g}[G_C]-G_C(pi*); unique minimizer gives index 1, G_C(pi*)>=E_E[G_C] gives index 0. | Derived f' and f''=-Var_{P_g}(G_C) and both cases; numerical check on 400 random instances with a control (strict reverse inequality gives index>0 in all 993 cases). |  |
| C17 | refuted (Theorem O and Proposition D as stated) | confirmed | Lemma M, Theorem O, Propositions E and D as first stated. | Re-derived by hand the n=2 sign-flip counterexample (Sigma^c=[[2/3,1/3],[1/3,2/3]], r=3 against r_eff=1) and the Proposition D counterexample (Sigma^c_12=+1/12, Pi=[[8,-4],[-4,8]]); stored output agrees. | Refutation is correct; the round-3 random search (445 draws, no violation) could not have detected it. |
| C17a | proved | confirmed-with-correction | Lemma M with hypotheses (beta conditioned and independent, stationary null): Sigma_eff - Sigma^c = S Cov(E[z_0\|ytilde]) S^T >= 0; Proposition E weight formulas under rules D1, D2. | Rederived sigma(eta,beta)=sigma(ytilde,beta), total covariance, order reversal; rederived D2 weights (Gaussian tilt) and D1 weights (potential plus Sherman-Morrison). Read lemma_m_check.py: it compares two different computations and can fail. | 'F has no eigenvalue on the unit circle' admits expanding F, for which the null's stationary law is anticipating and unreachable; state rho(F)<1. |
| C17b | proved (inequalities); corollary refuted with recomputed baseline | confirmed-with-correction | Under joint exchangeability (O2'), isolation (O1) and rank (O3): xi_out >= xi_out^eff and, if Pi^c is diffusive, xi_in <= 1/alpha, so r(C) <= r_eff(C). 'Never differs' holds only with the baseline held at its full-model value. | Rederived steps 1 to 5 (commutant, independence of the f-copy, Rayleigh bound, null block structure, Lemma M); verified the baseline-shift counterexample by hand (r=2/baseline 1.222 against r_eff=5/baseline 1.444); static random check with two (O3)-violating controls that do produce violations. | W is used but not defined in the record's Statement (line 236); definition is only in round4_proofcheck-c17bc/writeup.md. |
| C17c | proved | confirmed | Under swap invariance of (z, ytilde) with ytilde fixed and uncorrelated private laws, Sigma^c_ij = -M_ii < 0, so the null's precision is not diffusive. | Rederived m_i=m_j, M_ii=M_jj=M_ij, factor independence, and proved inverse-nonnegativity of positive definite Z-matrices by Neumann series. |  |
| C18 | computed, fresh-context | not-verified | Correlated-component pair is a performative meta-agent of grade (3.75,0.02,0.05,0.01,0.25) under strict typing. | Compared with check14_out, check16_out, attack a3_out, a4_out, a5_out, a7_out; all trace. | Fails under rulings (o) and (q); Statement not marked superseded. |
| C19 | proved; membership of theta* numerical | confirmed-with-correction | I*'s policy-covariance chain has a unique stationary law, continuous in parameters; Sigma^c, contrasts, baselines, null contrasts and the index (positive denominator) are continuous; the sets on which the differ clause holds are open. | Rederived the Moebius coefficients, c1 d0 - c0 d1 = F^2(1+b q_c)^2, the bound 0.7346, the coupling and telescoping logic of Theorem 1, and every formula of Theorem 3. Hypotheses (H3) to (H6) against lib.py and Theorem 2: read only. | Proposition 4 proves continuity only for a class where gamma_C alone varies; with a free belief variance (class G1) the index is lower semicontinuous, which still gives the open sets. |
| C20 | computed; (iii) proved | confirmed | Drawn-once partner randomization for P0 (256 patterns) and P1 (1296 patterns) under four scorings; closed form and bound 3/2 for the substitute selector. | Own enumeration of both families: 54 and 162 diffusive, 1 and 81 selecting {A}, 4.8870, six values 5.1186 to 5.3541, 1.472394, 53 infinite, 1251 with nine ties, multi-information 0.665899/0.572622/0.438239 and 60 patterns/0.892695. Rederived (iii) by pair counting, with a planted-wrong control; checked 0.993 and E p=0.0049 by hand. | The full-model P1 values 5.3723 and 0.663833 are taken from stored outputs. |
| R11 | failed route | not-verified | Pure-collider pair without channels: grade (2.29,0.02,0.01,inapplicable,0.50) under three readings; filed as failed. | Numbers traced to check7_out and check9b_out (one implementation, not attacked). The collective-clause mechanism is the hand-verified C17 counterexample. | Its verdict under the adopted rulings is not stated (finding F1). |
| R13 | failed route | confirmed | Drawn-once partner randomization fails or is undefined in small populations (C14 1/9, C18 17/81, P0 202/256 non-diffusive). | P0 count reproduced; the other two traced to stored outputs. |  |
| R8-R10,R12,R14-R16 | failed routes | not-verified | Failed routes for common coordinates, opposite preferences, two departments, several exterior options, Bougerol, closure-defect certification, gamma=infinity. | Read; cited numbers found in the cited outputs for R8, R15, R16; R12 follows from C16(b); R10 correctly re-attributed to C17c. |  |

Script audit. No fresh rerun was supplied and no stored script was rerun. Every quoted number I looked up is in the stored outputs (including 0.027596, 0.034917, 4.420). The audited checks can fail: lemma_m_check compares two independent computations, blind recomputations were written from results-free specs, negative controls exist. Weaknesses: verdicts are printed, not asserted (0 to 8 assert/raise per folder); round3_audience/check11_out.txt, cited by R13, ends in a ZeroDivisionError traceback after printing the cited count; the 999-draw N_pr test samples estimator noise of a deterministic null. My own scripts (p0_rebuild, p0_memory_fg, p0_corners, p0_nulls_mc, p1_patterns, small_checks) reproduce the stored P0 and C20 values to the printed digits.

Remaining open:
- O3, O4, O7, O8, O10, O11, O13 (128 corners of P1; a source with its own collective), O14 as listed; O9 reduced to C11/C13 drawn-once, N_fg for C13, P0's mechanism media; O12 moot under rulings (o), (q)
- R11: state its verdict under the rulings and recompute its grade independently
- Open-subset clause of 'differs' for P0 (O10 for C15); the C19 machinery appears to transfer but this was not carried out
- Rate-matched N_pr at P1's 17 design points
- n=2 same-sign case of Theorem O in Setting G: reduces to M_12 >= -(q/2p)(M_11+M_22) for M = L^T Cov(ytilde|z_0)^{-1} L (my derivation, static case proved, dynamic case open)
- Lock a Target for the narrowed manuscript problem

### Note `open_agy_meta_agent_exists-round3-synthesis.md`

Target: open:agy-meta-agent-exists

Declared record status: dated round-3 snapshot; header says the research record states the adjudicated status

Status justified? As a snapshot it matches the round-3 outputs I compared, but it now contradicts the record in five places (C17 proved, C8 generalized by Theorem O, C19 self-reviewed and unnarrowed, O2 open, drawn-once substitute selector not computed) and its verdict sentence omits the unproved open-subset clause for P0.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| S1-verdict | computed, conditional | status-overstated | The problem is settled at the computed level (form A), conditionally on O2(g), (h), (i), (m), (n). | Compared with def:agy-nulls and with O10; rebuilt P0. | Earned status: every pointwise clause computed at the base point, exact clauses at 128 corners, nulls and index at 17 points; the open-subset clause is numerical support only. |
| S1-matrix | computed/interpretive | not-verified | Reading-by-grade matrix of the constructions. | Read; P0 entries agree with my rebuild; other entries traced only where they repeat C13, C14, C18 numbers. | Row 'O2(g) drawn-once' is superseded by C20. |
| S2-readings | interpretive | not-verified | Recommended readings (a) to (q) with confidence estimates. | Read; checked the four that entered the definitions against the manuscript text. | Not mathematical claims; later ruled in the record. |
| S3-C17 | proved | defect | C17 (Lemma M, Theorem O, Propositions E, D): Status proved, review self. | Counterexamples re-derived by hand. | Theorem O and Proposition D are false as stated; the main record says so, the synthesis was not updated. |
| S6-literature | read 2026-11-21 | not-verified | Literature table with locators and verdicts. | Not checked against the sources. |  |

Script audit. Cites round3/<folder>/<file>, which resolve to the copied round3_<folder> directories; files exist. No scripts of its own.

Remaining open:
- Add a superseded banner naming the round-4 changes

### Findings

**meta_agent_rounds34/F1** (major, status-or-scope) at open_agy_meta_agent_exists.md, R11 (lines 344-348) and the 'Consequences' sentence of the O2 rulings (line 401)

The verdict of the pure-collider pair under the adopted rulings is not stated. Two of its three reopen conditions are met (inapplicable N_pr imposes no requirement, def:agy-nulls; Omega_int only reported, ruling m); ruling (c) covers 'a fixed attention schedule', which the pair does not have. If it passes, a pair of agents that never interact is a meta-agent by explaining away.

Evidence: check7_out.txt: r(pair)=2.57395, baseline 2.04930, N_eff and N_hab r=1, d_M=0, index 0.5152; check9b_out.txt: box intersection (2.1559, 2.4265]. One implementation, not attacked. Mechanism verified by hand on C17's counterexample: two agents without channels, Sigma^c=[[2/3,1/3],[1/3,2/3]], r=3, collective at r_0=2.

Fix: Rule whether act-effect structure is declared geometry under def:col-baseline(b); state R11's verdict; recompute its grade independently before any manuscript use.

**meta_agent_rounds34/F2** (minor, status-or-scope) at open_agy_meta_agent_exists.md C15 Statement (line 198); round3-synthesis Section 1

'A is a meta-agent of grade ...' and 'settled at the computed level' omit that the open-subset part of 'differs' is unproved for P0, and the Statement leads with a grade (alpha_M=0.071) from an initial law outside the proviso of def:agy-closure(i).

Evidence: def:agy-nulls requires a nonempty open subset; C19 covers I* only and O10 lists C15 as open; s05_agency.tex:307 says 'supported at these points and not proved'; s05_agency.tex:301 places the 0.0709 value outside the proviso.

Fix: State one grade (4.5,0.03,0.03,0.01,0.99) 'at the computed points; open-subset clause supported at 128 corners and 17 design points, O10'.

**meta_agent_rounds34/F3** (minor, status-or-scope) at open_agy_meta_agent_exists.md Target (line 10)

The locked statement quotes the original open problem at s05_agency.tex:295-297; that label now sits at line 313 with a different, narrowed statement. The record is active without a locked statement for the open problem.

Evidence: s05_agency.tex:313-315 asks for Omega_int(C|zeta_{V\C})>0 and r(C)<r_0 after deleting member channels; def:agy-meta-agent is at 05_agency.tex:379, def:agy-nulls at :332.

Fix: Close the original target with verdict and conditions; lock the narrowed statement in a new Target or successor record; update line references.

**meta_agent_rounds34/F4** (minor, status-or-scope) at open_agy_meta_agent_exists.md C13, C14, C18 status lines

Each construction is conditional on readings the rulings reject or leave uncomputed, and the status lines do not say so.

Evidence: Ruling (k) excludes never-used components (C14); (o) and (q) exclude member-specific coordinates and end-of-round belief (C18); C13's index under (e), (j) is O8.

Fix: Annotate each with 'superseded by ruling' or 'undetermined under rulings, O8'.

**meta_agent_rounds34/F5** (minor, integration) at 01_introduction.tex:152; s01_introduction.tex:146; 10a_meta_agents.tex:271; s13_discussion.tex:7; s10_abstract_collectives.tex:276

Summaries say the audience is 'shown to meet every clause' without the sampled-points qualifier that obs:agy-audience, the abstract, 05_agency.tex:401 and 13_discussion.tex:11 carry; s10:276 also drops 'by computation under stated declarations'.

Evidence: obs:agy-audience: 'at the points computed ... supported at these points and not proved'. The four sentences attach 'at the points computed' only to the variant.

Fix: Add 'at sampled points of its admitted class' in the five places, and 'by computation under stated declarations' at s10:276.

**meta_agent_rounds34/F6** (minor, mathematical) at open_agy_meta_agent_exists.md C17a (line 227)

Lemma M's stationarity hypothesis 'F has no eigenvalue on the unit circle' admits expanding F, for which the null world has only an anticipating stationary solution that its dynamics never reach.

Evidence: With |F|>1 and acts stabilizing the full loop, eta' = F eta + B a~ + w diverges from every initial state; the stationary solution depends on future forcing.

Fix: State rho(F)<1, or say explicitly that the null's law is the anticipating stationary one.

**meta_agent_rounds34/F7** (minor, editorial) at open_agy_meta_agent_exists.md C17b Statement (line 236)

W appears in (O2') and (O3) without definition.

Evidence: Definition (span of projections onto 1-perp of the agent-coefficient vectors of ytilde's loadings on (z_C, xi_C)) is only in round4_proofcheck-c17bc/writeup.md.

Fix: Define W in the Statement.

**meta_agent_rounds34/F8** (minor, mathematical) at C19, Proposition 4 (round4_proofcheck-c19/writeup.md lines 99-103)

Index continuity is proved for a class in which only gamma_C varies; for class G1 with a free belief variance the infimum is only upper semicontinuous, so the index is lower semicontinuous.

Evidence: The coercivity argument compactifies gamma_C only. Lower semicontinuity still makes {index > A_0} open, so the claimed open sets stand.

Fix: Say 'continuous for fixed group belief, lower semicontinuous with a free variance' in the Statement.

**meta_agent_rounds34/F9** (minor, integration) at 05_agency.tex:245 (def:agy-agency-index); 04_collectives.tex:219 (def:col-collective); 05_agency.tex:333

Rulings (b) and (n) give different answers from the manuscript's definitions on some populations; (c), (e), (k), (o), (p), (q) exist only in the record.

Evidence: def:agy-agency-index sets the index to 1 when the denominator vanishes, ruling (b) says that does not count; def:col-collective defines a partition as blocks that are all collectives, while the audience needs an output with an unassigned agent, declared inside the observation.

Fix: Author decision: write (b) into def:agy-meta-agent and (n) into def:col-collective or def:agy-nulls, or state in the record that they stay analyst declarations.

**meta_agent_rounds34/F10** (minor, script) at open_agy_meta_agent_exists-checks/round3_*, round4_*

Checks print their verdicts instead of asserting them.

Evidence: 0 to 8 assert/raise statements per folder; lines such as 'must lie in (0.05, 0.95)' are text.

Fix: Turn stated expectations into assertions with tolerances.

**meta_agent_rounds34/F11** (minor, script) at round3_audience/check11_out.txt (cited by R13)

The stored output ends in a ZeroDivisionError traceback.

Evidence: The F=1 block divides by 1-F^2; the cited count (54 diffusive of 256) is printed before it; F=1 values are in check11b_out.txt. I reproduced 54, 5.9403 and 2.5810.

Fix: Cite check11b_out.txt for F=1 and regenerate or annotate check11_out.txt.

**meta_agent_rounds34/F12** (minor, script) at round3_audience/check5b_npr_test.py; grade entries alpha_pr, n_null

The 999 'null draws' are finite-sample estimates of one deterministic second moment, so p measures estimator noise.

Evidence: p=0.002 arises from one non-diffusive estimate; the deciding comparison is 5.385 against 1.541 (my Monte Carlo: 1.5416 +- 0.0006).

Fix: None needed in the manuscript (def:agy-nulls says so); the record's grade lines could drop the p-values for the redrawn null.

**meta_agent_rounds34/F14** (minor, integration) at 10e_open_problems.tex:15 and :54-56

The open-problems register does not mention obs:agy-audience or open:agy-meta-agent-exists.

Evidence: 'No observed population is shown to meet the combined requirements' remains true; the register is the one summary the integration did not touch.

Fix: Add one clause and cross-reference in the table row and in sec:opn-1.

**meta_agent_rounds34/F15** (minor, editorial) at open_agy_meta_agent_exists-round3-synthesis.md Sections 1, 3, 5

The synthesis contradicts the record after round 4.

Evidence: C17 'Status: proved'; C8 'generalized by Theorem O'; C19 'Review: self'; O2 open; drawn-once 'substitute selector not computed'.

Fix: Add a superseded banner listing these items.

**meta_agent_rounds34/F16** (minor, editorial) at open_agy_meta_agent_exists.md lines 389, 391, 406

O2(g), O2(i) and O9 text predates the rulings, the ext2_rfm edit and C20.

Evidence: The open problem no longer mentions drawn-once scoring; ext2_rfm.tex:139 now reads 'declares no decision states and no admissible class'; drawn-once for P1 and the substitute selector for P0 are computed.

Fix: Update the three items.

**meta_agent_rounds34/F17** (minor, editorial) at s05_agency.tex:252; chk05_agency.tex:74

'Mean within-block' in the substitute selector is ambiguous between pooling within-block pairs and averaging per block.

Evidence: Pooled reading gives the stated closed form (verified, max error 6.7e-16); per-block reading gives exactly 1 for both bipartition types. The conclusion that the selector cannot select A holds under both.

Fix: Say 'pooled over within-block pairs'.

**meta_agent_rounds34/F18** (major, integration) at manuscripts/research_to_do.md, Cautions

The sentence that the world-conditional construction 'already separates a blanket produced by a shared driver from one produced by coupling' is contradicted by the audience.

Evidence: Under def:col-world-conditional a broadcasting non-member's sensing noise is not conditioned on: four members who never hear one another have r(A)=5.38 with Omega_int(A|zeta_S)=0 up to probability 1.9e-14; conditioned on, r(A)=1.000000 (my rebuild).

Fix: Qualify: the world-conditional law removes the common mode of an exogenous world only; a common non-member source and, with acts, collider coupling remain, and the member-restricted order parameter is what separates them.

### Collective_Agents touchpoints

| Location | Label | Relation | Detail |
|---|---|---|---|
| s05_agency.tex:295-309 | obs:agy-audience | integrated-matches | Grade (4.5,0.03,0.03,0.01,0.99), items (a)-(f), 'at the points computed', openness 'supported ... not proved'. Equals C15 under rulings g, h, l, n, r. |
| s05_agency.tex:311 | paragraph after obs:agy-audience | integrated-matches | Four conventions, one analyst declaration, drawn-once scorings (C20), P1; every exact number reproduced or traced. |
| s05_agency.tex:313-315 | open:agy-meta-agent-exists | integrated-matches | Narrowed to interaction-produced contrast. Does not mention that the relay niche C13 has such contrast and stalls on agency under the literal eta_C. |
| s05_agency.tex:250, 252, 267 | sup:agy-interaction-order-parameter-and-tests; rem:agy-h1-status | integrated-matches | Freezing-null qualifier, drawn-once relabeled as reported variant, audience sentence in the H1 status remark. |
| chk05_agency.tex:69-86 | chk:agy-audience | integrated-matches | Every exact P0 number reproduced by my rebuild; P1 numbers trace to round4_p1-blind outputs. |
| 05_agency.tex:20 | def:agy-closure | integrated-matches | Ruling (l): initial law is the stationary law of the noise-driven part. |
| 05_agency.tex:333, 347, 350 | def:agy-nulls, tab:agy-nulls | integrated-matches | Rulings (g) and (r) written in. |
| 04_collectives.tex:131 | def:col-world-conditional | integrated-matches | Ruling (h): broadcast sensing noise is a private input. |
| 05_agency.tex:401, 403 | sec:agy-h1 | integrated-matches | 'by computation at sampled points of its admitted class, under declarations that the definition leaves open'. |
| 00_abstract.tex:4 | abstract | integrated-matches | 'by computation at sampled parameter points under stated declarations'. |
| 13_discussion.tex:11 | sec:dis-status | integrated-matches | Carries 'at sampled parameter points'. |
| 01_introduction.tex:152 | introduction, what is not established | integrated-mismatch | No sampled-points qualifier for P0 (minor). |
| s01_introduction.tex:146 | sec:int-open | integrated-mismatch | Same drift (minor). |
| 10a_meta_agents.tex:271 | sec:met | integrated-mismatch | 'The only populations that the Supplement shows to meet every clause' without sampled-points qualifier (minor). |
| s13_discussion.tex:7 | sup:dis-other-clauses-of-h1 | integrated-mismatch | Same drift (minor). |
| s10_abstract_collectives.tex:276 | sec:abs-graded | integrated-mismatch | Drops 'by computation under stated declarations' as well as the sampled-points qualifier. |
| 05_agency.tex:245 | def:agy-agency-index | not-integrated | Ruling (b) (index of one by habit does not count) is not in the definition. |
| 04_collectives.tex:219 | def:col-collective | not-integrated | Ruling (n) (unassigned agents) is declared in the observation, not in the definition of the selector output. |
| 10e_open_problems.tex:15, 54-56 | sec:opn-1, tab:opn-status | not-integrated | Register silent on the audience and the narrowed problem; its existing sentences remain true. |
| ext2_rfm.tex:139-140, 167 | prop:rfm-verdict items, open:rfm-agent | integrated-matches | Ruling (i) and drawn-once wording; the record's O2(i) text is the stale side. |
| 11_predictions.tex:150 | predictions, substitutes | unaffected | Drawn-once example relabeled as the reported variant. |
| app05_agency.tex | app:agy | unaffected | No proof attaches to the observation. |

### Integration candidates

| Result | Target | Readiness | Why |
|---|---|---|---|
| open_agy_meta_agent_exists.md C16: for actual law delta_{pi*} and fixed habits and belief, the index is 1 if pi* uniquely minimizes G_C and 0 if G_C(pi*) >= E_E[G_C]. | s05_agency.tex, sup:agy-commentary-on-agency: new short proposition, cited from the paragraph after obs:agy-audience. | ready | Three-line proof (f''=-Var), reconstructed and checked; explains P0's index and the zero index of designs with several ignored exterior options. |
| C17a-C17c: Sigma_eff - Sigma^c = S Cov(E[z_0\|ytilde]) S^T >= 0; under joint exchangeability and rank below n-1, r(C) <= r_eff(C); under swap invariance a null keeping the acts has Sigma^c_ij<0. | s05_agency.tex, sup:agy-interaction-order-parameter-and-tests: lemma plus two propositions; proofs in app05_agency.tex. | ready-after-minor-fix | Two fresh reconstructions agree. Fixes: write Setting G in manuscript notation, rho(F)<1, define W, omit the 'never differs' corollary until O14 fixes the baseline convention under a null. |
| R11 and C17's counterexample: with performative acts, a pair without channels has explaining-away contrast (r=3 in the two-agent example) and can meet the grade. | s05_agency.tex, remark near ex:agy-collider or after obs:agy-audience. | needs-fresh-proof-check | Collective-clause mechanism is verified by hand, but R11's full grade has one implementation and its verdict under ruling (c) is undecided (F1). |
| C19 extended to P0 (O10): open-set form of the differ clause for the audience. | s05_agency.tex:307 and chk:agy-audience: replace 'supported at these points and not proved'. | needs-fresh-proof-check | Not carried out. P0's Riccati map is the same Moebius family and its attention kernel has full support, so (H1)-(H4), (H6) look routine. |
| C13: relay niche with interaction-produced contrast meeting the other clauses by computation; agency under the literal eta_C not computed. | s05_agency.tex:314, one sentence in open:agy-meta-agent-exists. | needs-repair | O8 must be computed first; C16 suggests the index falls to 0. |
| Rulings (b) and (n). | 05_agency.tex def:agy-meta-agent or def:agy-agency-index; 04_collectives.tex def:col-collective or 05_agency.tex def:agy-nulls. | ready-after-minor-fix | Author decision; these are the two rulings on which definitions and record can disagree. |
| C15/obs:agy-audience and the narrowed open problem. | 10e_open_problems.tex: table row 'Collective agency' and sec:opn-1, one clause each. | ready | Consistency with abstract, introduction and discussion. |
| C13, C14 (D1), C18 as constructions. | none | not-worth-integrating | C14 fails ruling (k), C18 fails (o) and (q), C13 is undetermined under (j). |

### MAgent_Theory_2.0 bearing

Searched MAgent_Theory_2.0/chapters/*.tex for meta-agent, audience, partner, randomiz, null, (F5), common source, shared drive, broadcast, world-conditional, agency index, explaining away, collider, and README.md and future_TODO.md for meta-agent, audience, Collective_Agents. MA has no world-conditional law, contrast, agency index, partner randomization or collider statement. Two interpretive bearings through the formation standard that def:agy-nulls cites: (1) chapters/05_inheritance.tex:1840-1846, clause (F5), quantifies over a declared constant set and an open subset with P(x) != P^0(x) at every point; the record's reading 'each r_0 in the admissible window' has that form if the window is the declared set, and under MA's rule at 05_inheritance.tex:1859-1865 P0's open-subset clause would count as undetermined. Breaks: (F5) concerns partition histories of deterministic flows. (2) chapters/05_inheritance.tex:1676-1705: the frozen-environment control (N3) freezes other agents' laws and is a control, not a null that (F5) must hold against; ruling (r) makes Collective_Agents' freezing null behave like it. Breaks: MA has no sensing noise to freeze. No MA statement is contradicted, sharpened or instantiated.

### To-do bearing

One real bearing, on the Cautions paragraph: its sentence that the world-conditional construction already separates a shared-driver blanket from a coupling blanket is too strong. P0 is a collective at r(A)=5.38 produced entirely by a common non-member source, with no interaction among members, and with acts the same conditioning creates collider coupling between non-interacting agents (C17 counterexample, R11). The member-restricted order parameter is the separating statistic and is only reported by def:agy-meta-agent. No bearing on workstreams 1, 2, 4, 5; nothing new for workstream 3.

### Checker scripts

NOT WRITTEN. The harness refused the write of 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/meta_agent_rounds34/report.md (subagent report files are blocked), and I did not route around it. The detail is in this structured output; my scripts and their outputs are in 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/meta_agent_rounds34/ (p0_rebuild.py, p0_rebuild_out.txt, p0_memory_fg.py, p0_memory_fg_out.txt, p0_corners.py, p0_corners_out.txt, p0_nulls_mc.py, p0_nulls_mc_out.txt, p1_patterns.py, p1_patterns_out.txt, small_checks.py, small_checks_out.txt).


## Checker group `agy_uniform_bound`

Claims C1 to C4 hold as written in their claim blocks: I reconstructed each derivation and recomputed each on its smallest instance, including an exact matrix-tree evaluation of the C3 factorization at m=2 (n=7, 128 profiles). The Verdict Summary overstates them: the Class 2 lower bound needs an independent-block declared belief (a weakly correlated declared belief on the same slots reproduces the limit law, TV 3e-23 to 3e-5 at m=2), the factor proved is |A|^(1/8) and not |A|-1, and the "no polynomial bound" sentence needs a qualifier. Nothing from the note is in the manuscript, where four sentences still pose the problem as fully open; the stored script cannot fail on the load-bearing statements of C3 and C4.

Coverage. Claim headings C1-C4 (12 sub-claims): all reconstructed step by step and recomputed with my own code on the smallest instance (n=2; m=2, n=7), with planted-error controls; C2 topology also enumerated at m=3 and counted at m=4,5; C3 identity at m=3,4,5 and a truncated m=3 chain; C4 bookkeeping at m=3,4. Verdict Summary compared sentence by sentence and found overstated in three places. Failed routes: R1 consistent with C1/C3 (read), R4 rederived roughly, R2 and R3 read only. Open obligations O1-O3 listed; O2 superseded for this family by finding M1. Skipped: full 32768-state chain at m=3 (too large for an exact computation within the compute limits); numerical value of the 4-checkpoint factorization constant beyond m=2; primary sources (Anantharam-Tsoucas not read, the tree theorem was instead confirmed on these instances by matrix-tree versus elimination agreement to 1e-34; Candogan-Menache-Ozdaglar-Parrilo 2011 arXiv listing only). The stored script was not rerun by me; the coordinator's rerun was compared with the stored output.

### Note `open_agy_uniform_bound.md`

Target: open:agy-uniform-bound

Declared record status: active (Review: self on all claims; O1, O2, O3 unchecked)

Status justified? Active is justified. The locked statement asks for either (i) a bound on the distance from the deliberation law to a group posterior, uniform in gamma and polynomial in n, or (ii) a family showing the tree-bound factor |A|-1 is needed for perturbations without a potential part. Established: no gamma-uniform bound to P_Phi(q_C) for any declared belief (n=2); none to the Gibbs law of the Hodge potential part (n=2); none to group posteriors with product habits, free precision and an independent-block declared belief (n=7); a factor 2^((n+9)/8) on gamma*sigma_max is necessary for a harmonic perturbation. Not established: (i) for the nearest group posterior over all declared beliefs (the family gives no lower bound there, see finding M1), and (ii) in its literal form (exponent 1/8, not 1). The Verdict line 'completely refuted for both Class 1 and Class 2' holds only under the note's restricted definition of Class 2.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C1 | proved | confirmed | n=2 binary linear-Gaussian instance with redundancy beliefs I_C +- delta: as gamma grows, P^inf(0,1) -> 1 with ratio ~ e^{gamma(2delta-eps)}, while P_Phi(q_C)(0,1) -> 0 for every declared belief and the Gibbs law of the Hodge potential Phi + (delta/2)(pi_1 - pi_2) also puts vanishing mass there; both TV limits equal 1. | Reconstructed step by step: the eight transition asymptotics, all 16 rooted trees of the 4-cycle, and Phi(q_C) = sum c_j pi_j + M_{q_C} with c_j independent of q_C. Recomputed at 40 digits with my own code (ratio/e^{gamma(2delta-eps)} = 1.0000000000 at gamma=100..2e5; TV 0.4400210516 and 0.2449072516 at gamma=100). Computed the Hodge projection by least squares instead of taking it as given. | Editorial only: the raw n=2 perturbation has divergence (0,+delta,-delta,0), so it has a potential part for every q_C; only part 3 is a statement about the harmonic part (size delta/2). The script header and Verdict item 1 call the whole of C1 'pure non-potential'. |
| C2 | proved | confirmed | Gear-train graph on n=8m-9 binary members with one Gaussian coordinate per edge: R_u = delta*pi_u(pi_{u+1}-pi_{u-1}) on gear 0 and zero elsewhere (exactly harmonic, sigma_max=delta); the zero-energy profiles and their bridges form an induced path in the hypercube with 3*2^m-5 profiles and 2^m clockwise motor steps; stated energy gaps for uniform and 4-checkpoint costs. | Reconstructed the redundancy formula, the cyclic cancellation, the induction (I1),(I2) including slice endpoints and absence of cross edges, the top-gear assembly, and the per-gear energy minima. Own enumeration from hypercube energies at m=2,3 (path, degrees, monotone motor count, checkpoints, shared lower subset, 'at most 5' count = 3 and 5); tuple counts 43, 91 and edge counts 134, 202 at m=4,5; R computed from mutual informations on all 128 profiles at m=2 (max \|div R\| = 3.3e-39, control 0.08). | Bounds are conservative: the least energy increase from a bridge into V_1 is 0.9 at m=2,3, not Delta=0.1, because two gears cannot be doubly occupied without a wall. |
| C3 | proved | confirmed-with-correction | Along delta = lambda/(2^m gamma): the tree weight of each valley profile factors as C_out times the in-path tree weight up to 1 + (2n)^{\|V0\|} e^{-gamma(Delta-(6*2^m-8)delta)}; path-tree weights have ratio exp(2 lambda (s_b-s_a)/2^m); hence P^inf -> mu_lambda, the endpoint log-ratio against P_Phi tends to 2 lambda = 2^{m+1} gamma sigma_max, and TV to P_Phi(q_C) is bounded below uniformly over independent-block q_C. | Reconstructed the (tau_0,tau_1) decomposition, uniqueness of the in-path tree, per-vertex ratio bounds, tree count, the telescoping identity and the use of the manuscript tree bound for mass off P_m. Exact check at m=2 by matrix-tree theorem with subtraction-free elimination at 34 to 1500 digits: rho = W/(C_out w_path) satisfies 0 < rho-1 <= bound in five (lambda,gamma) cases (3.75e-13 at gamma=40, 4.9e-206 at gamma=600, 3.9e-694 at gamma=2000); identity holds to 1e-30; ln-ratio 2.0 and 8.0 to 12 digits; TV 0.23781848 and 0.69529809. Identity verified at m=3,4,5; truncated 466-state chain at m=3 agrees with mu_lambda to 1e-15. Planted errors (wrong exponent, potential control, wrong split) all detected. | Correction: part 1 needs delta(gamma) < Delta/2 (gamma > 2 lambda/(2^m Delta)), used in the proof (note line 213) and missing from the statement (line 74). The proved bound is vacuous at every gamma the stored script uses (2.7e11 to 4.3e16 at gamma=120); the measured rate is about e^{-0.8 gamma}. The full m=3 chain was not computed. |
| C4 | proved | confirmed | 4-checkpoint gear model: P^inf -> P_lambda on {A,B,C,D}; every group posterior with product habits, any precision and an independent-block declared belief satisfies P(A)P(D)=P(B)P(C), hence TV >= 2sqrt(p_lambda)-1 (-> sqrt2-1); for correlated beliefs TV >= R(2sqrt p - R) with R = exp(gamma_C sigma_max(q_C)/2) when R <= 2 sqrt p; at m=2 and fixed small delta the limit law is (delta_B+delta_C)/2. | Reconstructed the excess-action count Delta-6b-(6*2^m-10)delta, the mass bound off {A,B,C,D}, the cancellation of single-site terms, the chain-rule reduction, and the constrained optimization. Full m=2 chain in mpmath: TV(P^inf,P_lambda) = 3.7e-5 (gamma=1000), 3.4e-18 (gamma=4000); fixed delta=2e-5 gives P(B)=P(C)=0.499832 at gamma=1e5. Generic log-det cross-ratio over 40 random independent-block beliefs: 1.1e-13. Numerical minimum of TV under the constraint equals the bound for kappa=1 and exceeds it for kappa<1; planted wrong bound violated. | The independent-block restriction is essential and the trade-off bound is vacuous once gamma_C*sigma_max(q_C) >= ln(4 p_lambda) <= ln 2. See finding M1 for a correlated-belief group posterior on the same slots at TV 3e-23 to 3e-5. |
| Verdict Summary (lines 24-31) | proved (headline) | status-overstated | No gamma-uniform and no polynomial-in-n bound exists; the first alternative is completely refuted for Class 1 and Class 2; an exponential factor is needed for harmonic perturbations. | Compared each sentence with the claim blocks and with the manuscript statement at s05_agency.tex:70-74; built and computed a counter-construction to the unrestricted reading at m=2. | Earned status: proved for the reference law P_Phi(q_C) and for group posteriors with independent-block (or fixed) declared belief; not shown for the nearest group posterior over all declared beliefs; second alternative shown with exponent 1/8 instead of 1; 'no polynomial bound as a function of (n, gamma sigma_max)' is true only for bounds of the form e^{o(n)}(gamma sigma_max)^a, a>0. |
| R4 | failed route | confirmed | Strict Nash equilibria of the binary epistemic game form an antichain, so two comparable profiles cannot both carry limit mass. | Rederived in three lines: G_i(pi+i)-G_i(pi) = c_i + I_{q_i}(o_i;o_pi) is nondecreasing in pi. | Checked roughly; habits assumed uniform. |
| R2, R3 | failed routes | not-verified | A reflected Gray code cancels the line integral; 4-to-4 escapement and even-state locking create shortcuts or branch points. | Read only. | The quoted 'other = 21' at m=3 was not reproduced. |

Script audit. Rerun and stored output agree on all 60 non-empty lines except last digits of nine solver-agreement or residual figures (e.g. 1.53e-13 vs 1.54e-13); the stored file is UTF-16. Every number quoted in the note matches the stored output. Section 1 (C1) is a real two-derivation check; Section 2b/2c (topology counts, dropped-wall control) are real. Section 3 cannot fail on the claims it is cited for: ln_ratio, TV_Phi, mass and the checkpoint probabilities are printed and not asserted against the limits, the C_out factorization and path-tree identity are never computed, and the 'two channels' are two linear solvers of one matrix. The C4 runs stop at gamma=180 where mass on {A,B,C,D} is 0.77-0.91 and TV to P_lambda is 0.09-0.12; the fixed-delta regime of C4(3) is not run. Harmonicity is tested on the closed formula over 16 states, the checkpoint landscape check omits the tilt and the 'at most 5' count, and the trade-off table only evaluates a formula. My scripts gear.py, chk1_c1_c2.py, chk2_c3_tree.py, chk3_c4_scope.py, chk4_c3_more.py, chk5_c4_m34.py (outputs chk1_out.txt to chk5_out.txt, same folder) supply these checks with planted-error controls; total run time under 30 s.

Remaining open:
- O1 (note): sharp exponent theta* in [1/8, 1] for the factor |A|^theta gamma sigma_max.
- New, replacing O2: is the distance from the deliberation law to the nearest group posterior over all declared beliefs on the collective's slot model (product habits, free precision) bounded uniformly in gamma and polynomially in n? The gear family gives no lower bound there.
- Written general-m proof and check of the correlated-belief construction (computed here at m=2; pair bookkeeping for general m checked by hand only).
- Exact stationary law at m>=3 has not been computed by anyone; exponential growth in m rests on the reconstructed proof, exhaustive m=3 topology and landscape, the path-tree identity at m=3,4,5 and a truncated m=3 chain.
- Script repairs: assert the limits, add a tree-weight computation, run C4 in the asymptotic regime.

### Findings

**agy_uniform_bound/M1** (major, status-or-scope) at open_agy_uniform_bound.md lines 17, 28, 30, 31, 317 (Class 2 definition, Verdict items 1-3, O2)

The lower bound against 'all Class 2 group posteriors' holds only for independent-block declared beliefs. On the note's own slot model a group posterior with product habits and a weakly correlated declared belief reproduces the limit law, so the first alternative is not 'completely refuted' and O2 (invented slots) is moot for this family.

Evidence: m=2, declared Gaussian belief equal to q_C^* plus correlation rho between eta_(0,1),eta_(4,5) and between eta_(2,3),eta_(5,6): M(A)=M(D)=J'>0, M(B)=M(C)=3.6e-15. With gamma_C*J' = lambda and tuned product habits: fixed delta=2e-5, gamma=4e5, gamma_C=gamma: sigma_max(q_C')=8.29 delta, TV(P^inf,Q)=3.3e-23 (independent-block bound 0.41421); lambda=4, gamma=4000, gamma_C=20 gamma: sigma_max(q_C')=1.21 delta, TV=2.7e-12 (bound 0.40144). Consistent with C4(2), whose trade-off bound is vacuous once gamma_C*sigma_max(q_C) >= ln 2. Manuscript s05_agency.tex:70 allows minimizing over the declared belief. Script chk3_c4_scope.py.

Fix: State the Class 2 result for independent-block (or fixed closure-model) beliefs in the Verdict and in any manuscript statement; add the correlated-belief construction as a claim with a general-m proof; replace O2 by the question of a gamma-uniform bound on the distance to the nearest group posterior over all declared beliefs.

**agy_uniform_bound/S2** (minor, status-or-scope) at open_agy_uniform_bound.md lines 24, 31, 316

The open problem's second alternative asks for a family showing the factor |A|-1 is needed; the note proves 2^((n+9)/8), of order |A|^(1/8). Disclosed in O1, but the headline 'Negative answer ... proved' does not say which alternative and which reading was answered.

Evidence: C3(3): limit of max |ln(P^inf/P_Phi)| >= 2^m gamma sigma_max with n=8m-9; at m=2 the tree bound is 63.5 lambda against a realized 1.175 lambda (lambda=1) and 6.23 (lambda=4).

Fix: Reword the Verdict headline: exponential factor with exponent at least 1/8 is necessary for the reference law; the exponent 1 of the tree bound is not shown necessary.

**agy_uniform_bound/S3** (minor, status-or-scope) at open_agy_uniform_bound.md line 29

'No bound polynomial (or sub-exponential) in n exists, even as a function of (n, gamma sigma_max)' is false without a qualifier (the bound 1 is polynomial).

Evidence: What C3 gives is F(8m-9, lambda 2^-m) >= TV(mu_lambda, Unif(P_m)) for every valid bound F; TV(mu_1,Unif) = 0.2378 at m=2 and 0.2417 at m=3. This excludes F = e^{o(n)}(gamma sigma_max)^a with a>0 and does not exclude, for example, n/ln(1/(gamma sigma_max)).

Fix: State the exclusion in that form.

**agy_uniform_bound/S4** (minor, editorial) at open_agy_uniform_bound.md lines 26-27, 50; verify_uniform_bound.py line 387

C1 is labeled 'pure non-potential', but the raw n=2 perturbation has a potential part under every declared belief; only C1(3) concerns the harmonic part.

Evidence: Divergence of the n=2 flow computed directly: (0, +0.01, -0.01, 0) at delta=0.01; least-squares potential part (0, 0.005, -0.005, 0); residual divergence zero. For two binary members harmonicity forces R_1=R_2=0.

Fix: In Verdict item 1 list inf over q_C of TV to P_Phi as a Class 1 statement and reserve 'without a potential part' for the Hodge comparison; rename the script section.

**agy_uniform_bound/M2** (minor, mathematical) at open_agy_uniform_bound.md line 74 (C3 part 1) and line 213 (proof)

The factorization inequality is stated for every gamma on the schedule but the proof needs delta(gamma) < Delta/2; the bound is also vacuous at all gamma used in the stored numerics.

Evidence: Proof Step 2 begins 'for delta < Delta/2'. Right side minus one: 7.9e14 (lambda=1, gamma=40), 2.7e11 (lambda=1, gamma=120), 4.3e16 (lambda=4, gamma=120), 6.2e-5 (lambda=4, gamma=600). Measured rho-1: 3.75e-13, 5.8e-41, 2.9e-39, 4.9e-206; rate -ln(rho-1)/gamma = 0.72 to 0.80.

Fix: Add 'for gamma > 2 lambda/(2^m Delta)' to C3(1). Optionally sharpen the exponent to h-Delta using the fact that exits from bridges cost at least h.

**agy_uniform_bound/X1** (major, script) at open_agy_uniform_bound-checks/verify_uniform_bound.py lines 590-666

The script cannot fail on C3(1), C3(2), C3(3) or C4(1): limit values are printed and never asserted, the tree-weight factorization and path-tree identity are never computed, and the two 'channels' are two solvers of one transition matrix.

Evidence: Only assertions in Section 3a/3b: ch_diff and residual tolerances (lines 628, 660), decomposition and sigma (618-620), lb_num >= lb_analytic (665). ln_ratio, TV_Phi, mass_P, pA..pD appear only in print statements.

Fix: Assert |ln_ratio - 2 lambda| and |TV_Phi - tv_lim| at the largest gamma; add a matrix-tree computation of W(x), C_out and w_path with a planted wrong exponent as control (chk2_c3_tree.py in the scratch folder does this in 3 s).

**agy_uniform_bound/X2** (minor, script) at verify_uniform_bound.py lines 639-666; stored output Section 3b

The C4 runs are pre-asymptotic and the fixed-delta regime of C4(3) is not run; the stored numbers show a trend toward P_lambda, not the limit.

Evidence: At gamma=180: sum of P(A..D) = 0.8821, 0.8878, 0.9065; my recomputation gives TV(P^inf,P_lambda) = 0.1179 (lambda=1) and 0.0935 (lambda=4). With subtraction-free elimination in mpmath: 3.7e-5 at gamma=1000, 3.4e-18 at gamma=4000; fixed delta=2e-5, gamma=4e5: P(B)=P(C)=0.5, P(A)=6.3e-15.

Fix: Replace the float64 LU solve by a subtraction-free (GTH) elimination in mpmath and run gamma up to 4000 and the fixed-delta case; assert TV to P_lambda.

**agy_uniform_bound/X3** (minor, script) at verify_uniform_bound.py lines 497-508, 535-572, 668-676

Harmonicity is tested on the closed formula for R, not on R computed from the linear-Gaussian model; the checkpoint landscape check omits the tilt, the energies of A,B,C,D and the 'at most 5' count; the trade-off table evaluates a formula.

Evidence: Section 2a builds R_vals from delta*b_i*(b_{i+1}-b_{i-1}) directly. My LG-model computation over all 128 profiles gives max |div R| = 3.3e-39 and sigma = (delta x4, 0 x3); 'at most 5' count is 3 (m=2) and 5 (m=3).

Fix: Compute div R from R_mem in the harmonic case (the code already does so for the control at line 691) and add the missing assertions.

**agy_uniform_bound/E1** (minor, editorial) at open_agy_uniform_bound.md lines 20, 53, 111, 324; Collective_Agents/references.bib

The Hodge decomposition of games is attributed to 'Candogan-Ozdaglar-Parrilo' and tied to the 2013 near-potential paper; the decomposition is due to Candogan, Menache, Ozdaglar and Parrilo (2011), which has no bib entry.

Evidence: arXiv:1005.2405 listing: 'Flows and Decompositions of Games: Harmonic and Potential Games', Candogan, Menache, Ozdaglar, Parrilo, Math. Oper. Res. 36(3), 474-503, 2011 (listing read; body not read). references.bib has only candogan2013dynamics (Games Econ. Behav. 82).

Fix: Cite the 2011 paper for the potential/harmonic decomposition and add the bib entry; keep candogan2013dynamics for the tree bound comparison. No proof depends on the source because the note defines harmonicity directly as div R = 0.

**agy_uniform_bound/I1** (major, integration) at Collective_Agents/sections: s05_agency.tex:72-74, 05_agency.tex:236, 13_discussion.tex:43, s01_introduction.tex:146

The note is untracked, cited by no .tex, and none of its results is in the manuscript; four sentences still pose the uniform agency bound as fully open.

Evidence: grep for open_agy_uniform in the manuscript tree returns only the note; git status shows the note and its check folder as untracked. 05_agency.tex:236: 'a bound that is uniform in gamma and polynomial in the number of members is open'.

Fix: After the fixes above, add the n=2 proposition, the exponential-factor proposition and the restricted Class 2 proposition to the supplement with proofs and a check entry, and narrow the open problem to the exponent and to the nearest group posterior over all declared beliefs.

### Collective_Agents touchpoints

| Location | Label | Relation | Detail |
|---|---|---|---|
| sections/s05_agency.tex:72-74 | open:agy-uniform-bound | stale-open-statement | Posed in full. Settled by the note: no gamma-uniform bound to P_Phi(q_C) or to the Hodge-potential Gibbs law (n=2), none to group posteriors with independent-block belief (n=7), exponential factor 2^((n+9)/8) necessary. Still open: exponent between 1/8 and 1; nearest group posterior over all declared beliefs. |
| sections/s05_agency.tex:70 | paragraph before open:agy-uniform-bound | not-integrated | 'No bound uniform in gamma can be linear in sigma_max alone' is argued only for members who agree with one another. C1 extends it to members who disagree and to the harmonic part. The sentence stays true; it also says every bound may be minimized over the declared belief, which is the reading finding M1 addresses. |
| sections/05_agency.tex:236 | text after thm:agy-heterogeneous | stale-open-statement | 'a bound that is uniform in gamma and polynomial in the number of members is open (open:agy-uniform-bound)'. |
| sections/13_discussion.tex:43 | open problems paragraph | stale-open-statement | 'an agency bound uniform in policy precision (open:agy-uniform-bound) ... are open'. |
| sections/s01_introduction.tex:146 | list of open problems | stale-open-statement | 'a uniform agency bound ... are open'. |
| sections/05_agency.tex:214-233 | thm:agy-heterogeneous | unaffected | Used by the note as a hypothesis (P1 to P4 hold in the family). No conflict: the tree bound is 63.5 lambda at m=2 against a realized log-ratio of 1.18 lambda. The note shows the factor cannot be polynomial in n for the reference law. |
| sections/05_agency.tex:212 | sentence introducing thm:agy-heterogeneous | unaffected | 'It stays close to a group posterior when the disagreement is small' is correct only with 'small relative to 1/gamma'; worth a clause if C1 enters. |
| sections/s05_agency.tex:88-99 | prop:agy-index | not-integrated | Part (c) bounds 1-Agency from above. C4 gives an obstruction for classes with a fixed or independent-block belief: by Pinsker inf KL >= 2(sqrt2-1)^2 = 0.343 against KL(P^inf\|\|E) -> 6 ln 2, so 1-Agency >= about 0.08 at n=7 for arbitrarily small sigma_max (my arithmetic, not in the note). |
| sections/chk05_agency.tex:41-47 | chk:agy-heterogeneous, chk:agy-index | not-integrated | No check entry for the note's results. Existing entries unaffected; chk:agy-index's 1-Agency <= 3.8e-3 with free habits and precision in small instances is consistent with C1 at n=2. |
| sections/app05_agency.tex:164 | proof of thm:agy-heterogeneous(a) | integrated-matches | Markov chain tree theorem used in the note in the same form (stationary weight proportional to the sum over in-trees of products of off-diagonal transition probabilities). |
| sections/05_agency.tex:395; s13_discussion.tex:7; s01_introduction.tex:7; s09_minimal.tex:137; s10_abstract_collectives.tex:278; s12_related.tex:55; 10e_open_problems.tex:78; 11_predictions.tex:154; 02_framework.tex:334; ext3_obj.tex:3 | summary citations of thm:agy-heterogeneous | unaffected | 'within explicit distances of a group posterior / Gibbs law' remains true as written. 10e_open_problems.tex status tables do not list this open problem. |
| references.bib | candogan2013dynamics | not-integrated | No entry for Candogan, Menache, Ozdaglar, Parrilo (2011), needed if the Hodge-harmonic formulation is used. |

### Integration candidates

| Result | Target | Readiness | Why |
|---|---|---|---|
| open_agy_uniform_bound.md C1: two members, binary policies, redundancy beliefs I_C +- delta, costs c_1=-h-eps, c_2=-h with delta<eps<2delta: P^inf -> delta_(0,1) as gamma -> infinity while P_Phi(q_C)(0,1) <= e^{-gamma eps} for every declared q_C and the Gibbs law of the Hodge potential part gives at most e^{-gamma(eps-delta)}. | s05_agency.tex after line 70 (new proposition in sup:agy-bounds-on-the-agency-defect), proof in app05_agency.tex, entry in chk05_agency.tex | ready-after-minor-fix | Derivation reconstructed and recomputed. Fix: separate the with-potential and harmonic statements, cite the 2011 decomposition paper. |
| open_agy_uniform_bound.md C2+C3: linear-Gaussian family on n=8m-9 binary members, four heterogeneous, harmonic perturbation with sigma_max=delta; along delta=lambda/(2^m gamma), max \|ln(P^inf/P_Phi)\| >= 2^((n+9)/8) gamma sigma_max in the limit and TV(P^inf,P_Phi) -> TV(mu_lambda, Unif) > 0. | s05_agency.tex new proposition next to open:agy-uniform-bound; construction and proof in app05_agency.tex; chk entry; one sentence at 05_agency.tex:236 | ready-after-minor-fix | Proof reconstructed; exact m=2 tree computation, identity at m=3-5 and m=3 truncated chain agree. Fix the missing threshold in C3(1) and the wording of the polynomial claim. The construction is long, so it belongs in the appendix. |
| open_agy_uniform_bound.md C4: for the 4-checkpoint family, every group posterior with product habits, any precision and a declared belief independent across the edge coordinates has TV(P^inf, P_C) >= 2 sqrt(p_lambda) - 1 in the limit, and >= sqrt2 - 1 at n=7 as gamma -> infinity at fixed small delta. | s05_agency.tex new proposition or part (b) of the previous one; remark after prop:agy-index | ready-after-minor-fix | Correct as stated in the claim block; the independent-block (or fixed-belief) restriction must appear in the statement itself, since it is essential (finding M1). |
| Checker's construction (finding M1): on the same slot model a Gaussian declared belief with two weak cross-coordinate correlations, product habits and precision gamma_C with gamma_C*J' = lambda gives a group posterior at TV -> 0 from P^inf, with sigma_max(q_C') = 1.2 to 8.3 delta at m=2. | s05_agency.tex remark or example beside the Class 2 proposition; it also fixes the wording of the narrowed open problem | needs-fresh-proof-check | Computed at m=2 only; general m argued by hand in this check. It is new and has had no independent review. |
| Narrowed open problem: (a) the sharp exponent theta in [1/8,1] of the necessary factor \|A\|^theta gamma sigma_max; (b) a gamma-uniform, polynomial-in-n bound on the distance to the nearest group posterior over all declared beliefs on the collective's slot model. | s05_agency.tex:72-74 (rewrite open:agy-uniform-bound); 05_agency.tex:236; 13_discussion.tex:43; s01_introduction.tex:146 | ready-after-minor-fix | Follows once the three propositions are in; the four stale sentences then need one clause each. |
| Agency-index corollary: for classes with product habits, free precision and a fixed independent-block belief, 1-Agency >= 2(2 sqrt(p_lambda)-1)^2 / KL(P^inf\|\|E), about 0.08 at n=7. | s05_agency.tex after prop:agy-index | needs-fresh-proof-check | Three-line consequence of C4 and Pinsker written by the checker, not in the note and not checked by anyone else. |
| open_agy_uniform_bound.md R4: strict Nash equilibria of the binary epistemic game form an antichain. | none | not-worth-integrating | Side remark from a failed route; the manuscript does not use it. |

### MAgent_Theory_2.0 bearing

None exact. Searched chapters/, companion/, README.md, future_TODO.md for: expected free energy, deliberat, potential game, group posterior, Markov chain tree, Hodge, redundan, logit, policy precision, habit, Gibbs, detailed balance, reversib, non-reciprocal, spanning tree, harmonic, metastab. chapters/01_foundations.tex:208 states the MA models contain no action, policy or expected free energy, so the note's objects are outside MA's scope. Interpretive parallels only: chapters/03_dynamics.tex:446 (prop:dyn-nonreciprocal) and :467 (Monderer-Shapley cross-derivative remark) describe the same absence of an exact potential for deterministic per-agent flows, but there the dynamics is a contraction with a strict Lyapunov function, whereas the note's stochastic logit chain accumulates the non-potential part along an exponentially long valley; chapters/19_curvature_hierarchy.tex:88 uses a harmonic representative of a Hodge decomposition on the communication graph, while the note's harmonic cochain lives on the hypercube of policy profiles. No MA statement is contradicted, sharpened or instantiated.

### To-do bearing

None. The note concerns the agency theorem's error bound for deliberating members and touches none of the five workstreams of research_to_do.md (channel class, Markov length, timescale separation, universality classes, categorical formulation) or its cautions. No change to that file follows from this note.

### Checker scripts

NOT WRITTEN: the harness refused the Write call for report.md ("Subagents should return findings as text, not write report files"), and I did not route around it; the full content is in this structured output. Scripts and their outputs are in 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/agy_uniform_bound/ (gear.py, chk1_c1_c2.py, chk2_c3_tree.py, chk3_c4_scope.py, chk4_c3_more.py, chk4_helpers.py, chk5_c4_m34.py; chk1_out.txt to chk5_out.txt).


## Checker group `coh_amplification_noisy`

No mathematical defect found in C1 to C7 as stated: every derivation was reconstructed and tested against world-coordinate operators with planted-error controls, and the necessity of proportional noise for cycles of three or more agents (the step s06 flags as unchecked) is confirmed to 1.4e-13 on 1500 non-commuting instances. The defects are of scope: C4 to C7 and the manuscript's exclusions bound the cycle product A_c, while the note's own C3 shows that for noisy codes rho(A_c) does not decide growth under persistent circulation (the dynamics of thm:coh-amplification(b) and W of def:fw-level0), so the C4 witness and the level-1 instance C1(a') both grow (rho(T_seq) = 1.084 and 1.085). Integration is partial: part (c) is in s06 with stale hedges, parts (a) and (b) are not integrated, and five manuscript sentences saying level-1 reading of posted priors excludes growth are contradicted for persistent noisy circulation. The uncommitted note changes no claim, status or number that s06 cites.

Coverage. Checked by step-by-step reconstruction plus my own numerical test with a planted-error control: C1, C2, C3(1), C3(2), C4, Lemma 1, C6, C7(1), C7(2), the N = 2 supremum (11 items). Reconstructed with a lighter numerical check: C5. Failed routes R1 to R3 confirmed (R3 by hand). Not verified: O1 (the recorded @verifier reviews). Not done: rerun of the stored script (the coordinator's rerun was compared and is identical to the stored output), external literature (no cited theorem carries weight), the K >= 2 record model of MAgent chapter 18. Suprema for N = 2 and N = 3 were probed by finite searches only.

### Note `open_coh_amplification_noisy.md`

Target: open:coh-amplification-noisy

Declared record status: active (all seven claims marked proved or refuted, Review: fresh-context; O1 closed; no pending obligation listed)

Status justified? Status active is correct, but the record does not say why. The locked statement asks to settle three parts: (a) characterize amplification under noisy circulation, (b) under posted posterior covariances, (c) find a condition on sender-specific noise covariances for a common code of rank >= 2. Established: (c) is settled for the cycle product (proportional noises are necessary and sufficient for exclusion over all priors, any N; exact supremum for N = 2). (a) is partial: the formal round-trip identity fails, a bound holds, and for persistent circulation there is a sufficient stability condition plus a rank-one criterion that omits tau < -1. (b) is answered only for the frozen cycle product of one round; by C3 this does not exclude growth under persistent circulation, and time-varying gains are untreated. The locked statement also quotes the open problem as it read before the 2026-11-21 narrowing.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C1 (Proposition 1) | refuted (the naive extension), fresh-context | confirmed | For noisy codes rho(bar A_c) = max{rho(A_c),1} and base-point invariance fail; rank-one eigenvalue on V_1 is (1 - s_1N) + tr A_c; three rational counterexamples in K = N = 2. | Reconstructed the block-triangular decomposition and the rank-one formula step by step; recomputed all three instances exactly in SymPy from the edge-map definition in my own script (check_a.py). | Reproduced spec values 1/2, 7/6, 5/6; 75/1717, 1775/1717; -6/5, -7/10. Note that bar A_c is not the n-circulation map once A_1N is not idempotent; the true dynamics is C3. |
| C2 (Theorem 1) | proved, fresh-context | confirmed-with-correction | spec(bar A_c) = spec(M_rt) plus 1 with multiplicity K - r_N, and rho(bar A_c) <= max{1, \|\|C~\|\|} <= max{1, (r°_{N->1})^{1/2} prod_{e != N->1} (r_e snr_e/(1+snr_e))^{1/2}}; hence rho <= 1 under a common prior. | Reconstructed steps 1 to 3 (similarity, two-term Cauchy-Schwarz, telescope). Ran 4000 random cycles including r_N = K, unequal ranks, zero and singular noises: spectrum identity to 2.9e-11, 0 violations of either inequality; two planted errors violated 114 and 1005 times. | "Sharp" in the header is not proved: no attainment argument, best observed ratio 0.998 (0.9976 in the note). In rank one equality above 1 needs s_1N = 1. |
| C3(1) (Theorem 2, part 1) | proved, fresh-context | confirmed | On the invariant subspace the coded step obeys two exact dissipation identities; if r°_e <= 1 on every edge (e.g. common prior) quadratic energies are nonincreasing and rho(T_sync), rho(T_seq) <= 1 for any noise. | Rederived both identities and both telescopes by hand; identities hold to 7.7e-14 on 2000 random draws; 1500 heterogeneous-prior cycles with all r°_e <= 1 built in world coordinates: restricted spectral radius at most 0.9887. | One raw eigenvalue 1.0000003 in my run is rounding on the unit-eigenvalue cluster, not a violation. |
| C3(2) (Theorem 2, part 2) | proved, fresh-context | confirmed-with-correction | Rank-one codes: characteristic polynomials prod(lambda - (1 - s_k)) - tau° prod s_k (sync) and with lambda^{N-1} on the second term (seq); \|tau°\| <= 1 gives rho <= 1, tau° > 1 gives rho > 1 for every finite noise. | Rederived both determinants and both cases; compared all coefficients with numpy.poly of the world operators for N = 2..6 on 3000 draws (6.4e-15; planted lambda^{N-2} error gives 4.9); 219 draws with tau° > 1 all unstable, 2732 with \|tau°\| <= 1 all stable. | tau° < -1 is not covered and is noise and operator dependent: C1(b) has tau° = -4, rho(T_seq) = 1.000000, rho(T_sync) = 1.183216. Codes of rank above one have no criterion. The log's word "characterization" is too strong. |
| C4 (Theorem 3) | proved, fresh-context | confirmed-with-correction | rho(A_c) <= prod_e (r_e^+ snr_e/(1+snr_e))^{1/2} with r^+ the posterior edge ratio; if each header covers the sender's post-reception posterior covariance then rho(A_c) < 1, also with external sensing. | Rederived the gain identity, the telescope and both bracket norms; recomputed the rational witness by hand (79/110, 8/11, 440/91, 79/80, 8209/9100, 171/910); 4000 random cycles with arbitrary noises and unequal ranks: 0 violations, max ratio 0.9995; two planted errors violated 1735 and 562 times. | The exclusion is for the frozen cycle product only. Header "unconditional exclusion" and the multi-round clause overstate: the witness itself has tau° = 1.71, rho(T_sync) = 1.0709, rho(T_seq) = 1.0842. |
| C5 (Proposition 2) | proved, fresh-context | confirmed | With receivers using predicted priors and senders posting lagged filtered covariances, r^+ can exceed 1 whenever F P^+ F^T + Q is not below P^+, and rho(A_c) can grow without bound; instance gives 324/169. | Rederived step 1 and the instance (det Q_a = 0.5125, rho = 1.917160); step 1 succeeded in 473 of 473 admissible random draws. | Existence statement. The lagged header does not match the message of def:fw-level0, which carries the predicted mean; with the matching header prop:coh-no-amplification(c) applies. |
| Lemma 1 | proved (inside C6) | confirmed | \|\|M^{-1} E M\|\| <= s (kappa(M)^2 + 1)/(2 kappa(M)) for 0 <= E <= sI, with equality at a stated rank-one E. | Rederived the Abel summation, the reduction to unit vectors and the Kantorovich step; 20000 random draws, 0 violations, max ratio 1.000000; equality case to 1.5e-14; planted constant violated 16307 times. |  |
| C6 (Theorem 4) | proved, fresh-context | confirmed | Common code of rank >= 2: rho(A_c) <= exp(S_c/2) prod snr/(1+snr) with S_c the cyclic noise spread, and rho(A_c) <= prod snr/(1+snr) cosh(d_H(R_{j-1},R_*)/2) for any reference R_*. | Rederived both bounds including the polar-decomposition step; 3000 random cycles with non-commuting noises and an arbitrary reference: 0 violations of either. | R_0 is used both as cyclic index zero and as the reference matrix. |
| C7(1) | proved, fresh-context | confirmed | Proportional noises R_i = alpha_i R_0 give rho(A_c) <= prod snr/(1+snr) < 1 and rho(bar A_c) <= 1 for all priors; amplification is excluded for all priors iff the noises are proportional. | Rederived sufficiency and the round-trip part; 3000 random cycles: 0 violations. Necessity is C7(2). |  |
| C7(2) | proved, fresh-context | confirmed | For any non-proportional pair a, b and any N, a rank-one-limit family of priors reaches cosh^2(d_H(R_a,R_b)/4) > 1; for N = 2 this is the exact supremum. | Rederived the trace product, the arc assignment and the four inner products; 1500 random instances with non-commuting noises, N = 3..6, r_c = 2..4, any a < b: relative error 1.4e-13; finite s = 1e9 in world coordinates within 4.3e-3; exchanged orientation never reproduces the value, shifted arc differs in 1500 of 1500. N = 2 supremum rederived; 200 noise pairs times 300 priors stay below it (max 0.9989). | For N >= 3 the pair value is only a lower bound for the supremum: on the note's instance diag(4,1), I, diag(3,2) a search gives 1.131733 against 9/8, with the C6(2) bound 1.132466. |
| R1, R2, R3 | failed routes | confirmed | Failed routes: prior edge ratio under posterior headers; equal trace or determinant; max-norm contraction. | R1 count 4544/5000 compared with output and the witness recomputed; R2 follows from C7; R3 counterexample recomputed by hand (0.9 + sqrt(0.09) = 6/5). |  |
| O1 | closed | not-verified | Fresh-context verification by @verifier completed on all claims. | Read only; the reviews cannot be checked and are not evidence. |  |

Script audit. Stored output (UTF-16) and the coordinator's rerun are identical after decoding; seeded and deterministic; every number quoted in the note matches. Every asserting block can fail, and NC1 and NC2 show power. Weak points: dead code at lines 270-274 (unused z_init, a branch that is only pass), which also shifts downstream random counts relative to HEAD; SymPy exact channel only for C1 and the C4 witness, although the header says two channels throughout; C4 witness ratios printed, not asserted; "multi-round Riccati evolution" is a header iteration at fixed priors; tau° > 1 instability tested on one instance only; energy check on the reduced model with a common prior only; C7 checks use commuting diagonal noises; r < K always in the C2 block; NC3 is a counterexample check, not a planted error. My scripts cover these gaps with planted controls.

Remaining open:
- The note lists no open obligation.
- Criterion for persistent circulation when tau° < -1 and for codes of rank above one (I derived and numerically checked det(I - T) = prod det(Sigma_k) det(I - A_c^noiseless) on the invariant subspace, which gives instability when the noiseless cycle product has an odd number of real eigenvalues above one; this needs its own check).
- Relation between cycle-product amplification and growth under persistent circulation, and which one the manuscript means for noisy codes.
- Posterior posting with covariances updated between rounds (time-varying gains) and with a world transition F.
- Supremum over priors for N >= 3 under non-proportional noises.
- Stability of persistent circulation under a common code with common or proportional noise (0 unstable in 4000 draws each at rank two; numerical only).
- Attainment of the C2 bound.

### Findings

**coh_amplification_noisy/F1** (major, status-or-scope) at open_coh_amplification_noisy.md: C4 header and statement, Theorem 3 step 3, log entry of 2026-11-21

C4 (and C5 to C7) bound the spectral radius of the cycle product A_c of one frozen round. The note words C4 as an unconditional exclusion of amplification, including multi-round filtering, although its own C3 shows that for noisy codes rho(A_c) < 1 does not prevent growth under persistent circulation with retained own terms.

Evidence: C4 witness (P_1 = [[1,1.9],[1.9,4]], P_2 = [[0.1,0.09],[0.09,0.1]], R_2 = 1/10, R_1 = 8/11): rho(A_c) = 0.187912, tau° = 1.71, rho(T_sync) = 1.070875, rho(T_seq) = 1.084231. Over 3000 random rank-one cycles with posterior headers at the header fixed point, rho(A_c) < 1 in all and rho(T_sync) > 1 in 292 (largest 1.168). With covariances updated between rounds the gains vary in time and per-round spectral radii do not control the product.

Fix: State C4 as a bound on the frozen cycle product; drop "unconditional" and the multi-round clause; add an open obligation for persistent and time-varying circulation.

**coh_amplification_noisy/F2** (major, integration) at Collective_Agents/sections: 11_predictions.tex:44, s01_introduction.tex:53, s03_misreading.tex:167, 13_discussion.tex:15, s06_coherence.tex:139, 06_coherence.tex:127

The manuscript says level-1 reading of posted prior covariances excludes growth around a cycle and that amplification needs miscalibrated reading. That holds for rho(A_c) but is contradicted by C3(2) for persistent circulation with noisy codes, which is the dynamics of the proof of thm:coh-amplification(b) and, synchronously, W of def:fw-level0 with F = I, one sender per agent and no sensing.

Evidence: C1(a'): P_1 = [[1,3],[3,10]], P_2 = [[100,25],[25,7]], coordinate codes, R_i = X_ii exactly; edge ratios 10/17 and 100/101, rho(A_c) = 75/1717, tau° = 75/7; world-coordinate rho(T_sync) = 1.079089, rho(T_seq) = 1.085456; simulated story growth 1.085461 per circulation. Over 4000 random rank-one cycles with headers H_i P_i H_i^T + R_c: rho(A_c) < 1 in all, rho(T_sync) > 1 in 340 (largest 1.139). A common prior does exclude growth at any noise (C2, C3(1)), the reverse of the last sentence of rem:coh-amplification-class.

Fix: Owner decision: either scope these sentences to the cycle product (single pass or noiseless codes), or add C3(2) as a proposition and reword them. The prediction row's status "proved" should name the cycle product.

**coh_amplification_noisy/F3** (minor, status-or-scope) at open_coh_amplification_noisy.md: C3 statement (2), Theorem 2, log ("characterization")

C3 does not characterize persistent circulation: tau° < -1 is uncovered and behaves differently for the two operators, and codes of rank above one have only a sufficient condition.

Evidence: C1(b): tau° = -4, rho(A_c) = 6/5, rho(T_seq) = 1.000000, rho(T_sync) = 1.183216. Of 49 random draws with tau° < -1, both operators were stable in 40 and at least one unstable in 9.

Fix: Record both gaps as open obligations and call C3 a partial result.

**coh_amplification_noisy/F4** (minor, status-or-scope) at open_coh_amplification_noisy.md: C2 header, Theorem 1 title

The bound of C2 is called sharp on a numerical ratio only.

Evidence: No attainment argument in Theorem 1; best ratio 0.9976 in the note's run and 0.998 in mine. In rank one the eigenvalue is 1 - s + sC against the bound max{1,|C|}, so equality above one needs s = 1.

Fix: Say "attained to 0.998 in random cycles" or prove attainment in the noiseless-return limit.

**coh_amplification_noisy/F5** (minor, status-or-scope) at open_coh_amplification_noisy.md: Target (locked statement), Open obligations

The locked statement quotes the open problem before it was narrowed on 2026-11-21, and the record lists no remaining obligation although parts (a) and (b) are not fully settled.

Evidence: s06_coherence.tex:144 now ends with the request for an independent check of the proportionality answer; the note's Target still ends with the search for a condition weaker than common noise. Open obligations contains only O1, checked.

Fix: Requote the label and list the remaining obligations given in this result.

**coh_amplification_noisy/F6** (minor, status-or-scope) at open_coh_amplification_noisy.md C7(2); s06_coherence.tex:151

For three or more agents the two-sender value cosh^2(d_H(R_a,R_b)/4) is a lower bound for the supremum over priors, not the supremum.

Evidence: Note's instance R = diag(4,1), I, diag(3,2): best pair value 9/8 = 1.125; rank-one-limit search 1.131733, reproduced as rho(A_c) in world coordinates at s = 1e8; C6(2) bound minimized over the reference 1.132466. On 40 random triples the searched value exceeded the best pair value in all 40.

Fix: Keep the wording "reaches" and state that the supremum for N >= 3 is open; do not write "the same supremum".

**coh_amplification_noisy/F7** (minor, script) at open_coh_amplification_noisy-checks/verify_coh_amplification_noisy.py (lines 270-274, 423-427, 429, 322-335, 276-313, 653-705)

The script passes and can fail where it asserts, but it has dead code, single-channel checks described as two-channel, printed-only witness values, and narrow instances for the C3 instability, the energy check and C7.

Evidence: Lines 270-274 draw z_init and end in pass; the C4 ratios 440/91, 79/80, 171/910 are printed without assert; C7 instances use diagonal commuting noises; tau° > 1 is tested only on ex:coh-amplification(i).

Fix: Remove the dead block, assert the witness values, add random non-commuting C7 instances and a random tau° > 1 test. My scripts check_a.py and check_bc.py show the form.

**coh_amplification_noisy/F8** (minor, integration) at s06_coherence.tex:149-153

The remark's hedges and the source comment are stale against the working-tree note, and the uncommitted note changes nothing that s06 cites.

Evidence: Line 153 says "self-reviewed" and "C7(2) for N>=3 sketched only"; the working-tree note has Review: fresh-context and a repaired derivation (HEAD had a wrong index in the trace product and a wrong arc orientation, same final expression). The cited file 2026-11-21-remaining-issues-investigation.md is at the vault root docs/research, not under Collective_Agents/docs/research. Changed numbers (1.80e-13 to 1.02e-13, 4537 to 4544, 3986 to 3978, 2451 to 2465, 3476 to 3501) are not cited in the manuscript.

Fix: After the note is committed, update the comment and remove "that step has not been checked independently"; give the full path.

**coh_amplification_noisy/F9** (minor, editorial) at open_coh_amplification_noisy.md C5, C6, C7 evidence; chk06_coherence.tex

Notation and wording slips: R_0 has two meanings; C5's lagged header is not the protocol of def:fw-level0; "exact rational SymPy attainment" is floating point; rem:coh-proportional-noise has no numerical-check entry.

Evidence: C6 uses R_0 = R_N as a cyclic index and R_i = alpha_i R_0 as a reference. def:fw-level0 messages carry the predicted mean with covariance P^-(t). The C7 attainment is computed at s = 1e7 to 1e-5. chk06_coherence.tex has no line for 3.025 or the cosh^2 formula.

Fix: Rename the reference matrix, state the C5 protocol, correct the evidence line, add a chk06 entry when the script is registered.

### Collective_Agents touchpoints

| Location | Label | Relation | Detail |
|---|---|---|---|
| s06_coherence.tex:143-145 | open:coh-amplification-noisy | partially-integrated | Part (c) narrowed to C7. Parts (a) and (b) still read as fully open; C1 to C5 are not reflected. The independent check of N >= 3 necessity that the last sentence asks for is supplied by this review. |
| s06_coherence.tex:148-152 | rem:coh-proportional-noise | integrated-matches | Hypotheses and forms equal C7(1), the N = 2 supremum and C7(2); (10M+1)^2/(40M) = 3.025 at M = 1 is right. The hedges are stale and the N >= 3 value should stay worded as reached, not as the supremum. |
| s06_coherence.tex:146,153 | source comments | stale-open-statement | "self-reviewed" and "C7(2) for N>=3 sketched only" no longer describe the working-tree note; path to the F2 record is ambiguous. |
| s06_coherence.tex:110-118 | prop:coh-no-amplification | not-integrated | Correct as stated for rho(A_c). (d) could carry proportional noises (C7(1)); (c) does not exclude growth under persistent circulation (C1(a')). |
| s06_coherence.tex:121 | instance after prop:coh-no-amplification | unaffected | 1.36, 2.36, 2.64 match the script's block 0. |
| s06_coherence.tex:138-140 | rem:coh-amplification-class | contradicted-by-note | "Assigned noise covering the sender's coded uncertainty excludes it ... the remedy is calibrated reading, not common priors" is reversed for persistent noisy circulation: C3(2) with C1(a') grows at level-1 calibration, a common prior never does. |
| 06_coherence.tex:115-124 | thm:coh-amplification | unaffected | (b) is scoped to noiseless codes; C1 shows the identity fails outside that scope and C3 gives the noisy counterpart. |
| 06_coherence.tex:127 | paragraph after thm:coh-amplification | contradicted-by-note | "A cycle can amplify only where the receiver's assigned precision does not account for the sender's own uncertainty" holds for A_c, not for story growth under noisy persistent circulation. |
| 06_coherence.tex:131 | pointer to the open case | stale-open-statement | "the open case of noisy circulation" now has partial answers (C1 to C3). |
| 11_predictions.tex:44 | prediction row on cycle growth | contradicted-by-note | "level-1 reading of posted prior covariances excludes growth", status proved: true for rho(A_c); 340 of 4000 random level-1 cycles grow under persistent circulation. |
| s01_introduction.tex:53 | status table row | contradicted-by-note | "excluded by a common prior or level-1 reading of posted priors": the second half fails for persistent noisy circulation. |
| s01_introduction.tex:148 | list of open items | stale-open-statement | "Amplification under noisy circulation is not characterized" is still literally true and can be narrowed to tau° < -1, higher rank and time-varying gains. |
| s03_misreading.tex:167 | summary of amplification | contradicted-by-note | The noiseless clause is correctly scoped; "so does assigned noise that covers the sender's coded uncertainty" needs the cycle-product scope. |
| 13_discussion.tex:15 | discussion of H3 | contradicted-by-note | "Amplification around cycles needs miscalibrated reading of senders' uncertainty": C1(a') has both edge ratios below one and grows. |
| chk06_coherence.tex:48-51 | chk:coh-amplification | unaffected | Instance values 1.3568, 2.3586, 2.6410, 2.6773 match; there is no entry for the remark's numbers or for any C1 to C7 check. |
| app06_coherence.tex:111-142 | proofs and lem:coh-rank-one | unaffected | Used by the note as stated. |
| 09_minimal.tex:14; s08_scale.tex:12 | prop:min-common-code, conj:sca-common-code | unaffected | Consistent with C3(2): a common rank-one code has \|tau°\| <= 1. |
| 03_misreading.tex:204; s07_formation.tex:169; s08_scale.tex:229,252; 10e_open_problems.tex; 00_abstract.tex | other mentions | unaffected | No statement depends on the note; 10e and the abstract do not mention amplification. |

### Integration candidates

| Result | Target | Readiness | Why |
|---|---|---|---|
| open_coh_amplification_noisy.md C7(1): for a common code H of full row rank >= 2 read with R_i = alpha_i R_0, rho(A_c) <= prod_e snr_e/(1+snr_e) < 1 for all priors. | s06_coherence.tex prop:coh-no-amplification(d): extend the clause from common noise to proportional noises; proof line in app06_coherence.tex. | ready | Rederived here and by the earlier check; 3000 random cycles, 0 violations. |
| C7(2) and Theorem 5(3): non-proportional noises admit amplification for every N (value cosh^2(d_H(R_a,R_b)/4) reached for any non-proportional pair), and for N = 2 this is the supremum. | s06_coherence.tex rem:coh-proportional-noise: promote to a proposition, remove the hedges, narrow the last sentence of open:coh-amplification-noisy to the supremum for N >= 3. | ready-after-minor-fix | N >= 3 step confirmed to 1.4e-13 on 1500 non-commuting instances. Fix: commit the repaired derivation and say "at least" for N >= 3, since the supremum is larger (1.1317 against 1.125 on the note's instance). |
| C6 with Lemma 1: rho(A_c) <= exp(S_c/2) prod snr/(1+snr) and rho(A_c) <= prod snr/(1+snr) cosh(d_H(R_{j-1},R_*)/2). | New proposition in s06_coherence.tex after the proportional-noise statement; proof and lemma in app06_coherence.tex. | ready | Self-contained proof rederived; lemma checked on 20000 draws with a planted control. |
| C1: for noisy codes rho(bar A_c) need not equal max{rho(A_c),1}; instance (a') with R_i = X_ii has rho(A_c) = 75/1717 and rho(bar A_c) = 1775/1717. | Remark after thm:coh-amplification in 06_coherence.tex or in s06_coherence.tex before the open problem. | ready | Exact rational instances recomputed independently. |
| C3(2): for rank-one codes the persistent sequential and synchronous circulation operators have characteristic polynomials prod(lambda - (1 - s_k)) - lambda^{N-1} tau° prod s_k and prod(lambda - (1 - s_k)) - tau° prod s_k; stable for \|tau°\| <= 1, unstable for tau° > 1 at every finite noise. | New proposition in s06_coherence.tex narrowing part (a) of the open problem; rewording of 11_predictions.tex:44, s01_introduction.tex:53, s03_misreading.tex:167, 13_discussion.tex:15, rem:coh-amplification-class. | ready-after-minor-fix | Proof rederived and all coefficients checked for N = 2..6. Fix: state the tau° < -1 gap and decide which notion the manuscript calls amplification. |
| C2 and C3(1): a common prior, or r°_e = lambda_max(X_ji^{-1} X_ii) <= 1 on every edge, gives rho(bar A_c) <= 1 and rho(T_sync), rho(T_seq) <= 1 at any assigned noise. | New clause or proposition next to prop:coh-no-amplification(a); proof in app06_coherence.tex. | ready-after-minor-fix | Rederived; identities exact to 7.7e-14. Fix: drop "sharp". |
| C4: rho(A_c) <= prod_e (r_e^+ snr_e/(1+snr_e))^{1/2} with r_e^+ = lambda_max(R_i^{-1} H_i P~_i^+ H_i^T); headers covering the post-reception posterior covariance give rho(A_c) < 1. | New proposition in s06_coherence.tex answering part (b) of the open problem for the cycle product. | ready-after-minor-fix | Rederived with two planted controls. Fix: scope to the frozen cycle product and note that persistent circulation can still grow (the witness has tau° = 1.71). |
| C5: with lagged headers H_i P_i^+(t-1) H_i^T + R_c against predicted priors, rho(A_c) = 100 alpha^2 x/169, unbounded in x. | Example or remark after the C4 proposition in s06_coherence.tex. | ready-after-minor-fix | Correct, but the header does not match the message of def:fw-level0; the protocol must be stated. Low priority. |
| Numerical checks of C1 to C7 (stored script) and the reviewer checks. | chk06_coherence.tex chk:coh-amplification: new sentences for the proportional-noise values and for any adopted proposition. | ready-after-minor-fix | The remark's numbers have no registered check; the script needs the cleanups of F7 first. |

### MAgent_Theory_2.0 bearing

Searched chapters and companion for amplification, cycle products, Kalman gain, spectral radius, projective metrics, headers, loops and rings. (1) chapters/17_communication_links.tex:89-128 (it1:kalman, it1:gain, it1:gaussian-reconstruction, mean update): the single-edge objects are identical, O A being the gain-code map and C4 step 1 the gain form of the stated posterior precision; exact at one edge, and the chapter has no loop-product statement. (2) chapters/18_link_dynamics.tex:158-170 (it2:ring): for K = 1 and c = 0, w = q/(p+q) equals the note's s = snr/(1+snr), and the law-level q = (R + Sigma)^{-1} is level-1 reading of a posted posterior variance, the C4 setting; exact for K = 1. For K >= 2 C4 would give stability at the law-level covariance fixed point and ex:coh-amplification(i) an unstable plug-in two-cycle, but that depends on the K >= 2 record model, which I did not verify, so it is interpretive there. MA claims stability only for K = 1, so nothing is contradicted; its flow anchors to a fixed mean, so C3 does not transfer. (3) chapters/18_link_dynamics.tex:203-220 (it2:echo): variance double counting on a loop, a different object; interpretive only. "Amplifying grade" in chapters 05, 06, 11 to 14 is unrelated.

### To-do bearing

Workstream 1 only, and modestly: the note studies products of the projector O∘T in the receiver's metric (first bullet) and exhibits a loop effect that exists only for rank-deficient or noisy codes read in heterogeneous receiver metrics, which is material for the bullets on the residual of non-invertible codes and on an observable separating the regimes. Nothing bears on workstreams 2 to 5 or on the cautions. No change to research_to_do.md is required by this note.

### Checker scripts

Not written: the harness refused the Write call for report.md ("Subagents should return findings as text, not write report files"), and I did not route around it; the full content is in this structured result. Reviewer scripts and their outputs are in 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/coh_amplification_noisy/ (check_a.py, check_bc.py, check_c7_followup.py, check_persistent.py, check_det.py, each with a matching *_out.txt).


## Checker group `record_contrast_lrn`

No mathematical defect located in either note; every load-bearing claim I reconstructed came out as stated. open_lrn_noncentral: the r_c=1 closed forms are correct (coefficients rederived, symbolic difference 0; independent quadrature agrees to 1e-12 at three points), but "closed" overstates against the manuscript problem: a closed form exists only for r_c=1, P=pI, the rest is an integral representation plus a proof of non-elementarity, so the open problem should be narrowed, not removed. open_hie_record_contrast: "active" is right; closed collectives, q_z>q_rev with outsiders, q_z=0 and symmetric uncoupled pairs are settled, general open populations below q_rev are not (O1), and the comparison medium is a proposal awaiting the author's decision. Nothing from either note is in the manuscript; the hie note exposes one false manuscript sentence (s10b_hierarchy.tex:158), and both notes' proofs live only in an agent scratch folder outside the repository.

Coverage. lrn (5 claims, 14 sub-claims): reconstructed step by step C1(1)-(3), C2 at r_c=1, C3(a), C3(b), C4(1) given C3, the C4(2) linear-combination identity, the C4(3) limit integral, C5(a); confirmed numerically by my own code C3(a), C3(b) (three points plus MC), C4(2) (four points); read and step-checked C2 general r_c and C5(c); checked roughly C5(b) (one point); not rederived: C4(2) series resummation, C4(3) Carlson reduction, C5(b) Vitali argument; Liouville criterion not checked against a source. hie (7 claims, about 20 sub-claims, plus Lemma P1): reconstructed C1, C2, C3, C4(1),(2), C5(1),(2), C6(1)-(3), C7(2); read line by line C7(3) and Lemma P1; recomputed witnesses W1-W4, W6a, W6b, the manuscript instance, 27.6403 and the 9-node baselines; taken from stored output only: open16 marginal derivative signs, R2's 214/5000 count. Failed routes and obligations of both notes listed and assessed. Stored scripts were not rerun by me; coordinator reruns compared (identical). No external literature opened.

### Note `open_lrn_noncentral.md`

Target: open:lrn-noncentral (ext5_lrn.tex:143-145); duplicates first half of open:fw-understanding-risk (s02_framework.tex:151-154)

Declared record status: closed (all claims proved, Review: fresh-context by an earlier verifier #39)

Status justified? Partly. The manuscript asks: for K>=r_c+2 find E[psi psi^T] in closed form as a function of sigma_H. Established: a closed form in one confluent hypergeometric function for r_c=1, P=pI (elementary for even K); a 1D integral for r_c=1, general P; an r_c(r_c+1)/2-dimensional cone integral for general r_c (integrand polynomial not written out); proof that no elementary form exists in general. Closure is justified for the record's own reading (which asked to decide elementary versus special-function form) and overstated against the manuscript problem: non-elementarity does not show an integral is the best form, and the note's Searches table says Hillier-Kan and Letac-Massam were not opened, so a matrix-argument hypergeometric form for r_c>=2 is neither given nor excluded. Earned status: resolved for r_c=1 isotropic; reduced and shown non-elementary otherwise.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C1 | proved | confirmed | psi=psi_0+HO nu; I-E[HO]=sigma_H^2 E[tr(P^+)S^{-1}-O^T O] (so E[HO] symmetric; =sigma_H^2(K-r_c-1)E[(Hhat Hhat^T)^{-1}] for P=pI); E[psi psi^T]=R_c+sigma_H^2 E[W mhat mhat^T W^T - tr(P^+)(R_c S^{-1}+S^{-1}R_c)+R_c O^T O+O^T O R_c]. | Reconstructed all three parts step by step: dO=P^+ dHhat^T S^{-1}-O dHhat O, Stein's identity entrywise, and psi=nu-sigma_H W mhat (from Hhat mhat=y). Isotropic reduction by hand. Did not rerun the stored MC check. | Stein needs E\|\|S^{-1}\|\|<infinity, i.e. d=K-r_c+1>=3, which is the stated hypothesis; the manuscript version should state this step. |
| C2 | proved | confirmed | E[psi psi^T\|m,u] equals c_0 c_0^T plus two absolutely convergent integrals over the cone S_{r_c}^{++} of Gamma_{r_c}(m_j)^{-1}(det T)^{m_j-(r_c+1)/2}Z(T) times polynomial expectations under tilted Gaussian columns. | r_c=1: rederived and compared with my own direct 3D quadrature of the definition at two anisotropic points (diff 1.2e-15, 1.1e-15). General r_c: read the write-up proof (Siegel integral by Cholesky Jacobian, column tilting, Tonelli plus Cauchy-Schwarz) and checked each step; not evaluated numerically by me for r_c=2. | The note does not state the formula; it is only in the external write-up. The polynomial E_T[.] is not written out, so this is a representation, not a closed form. |
| C3 | proved | confirmed | r_c=1,K>=3: (a) general P: c_0^2 plus a 1D integral over t of Z(t) times bivariate-Gaussian moments; (b) P=pI: E[psi^2]=c_R R_c+c_u u^2+c_par (Hm)^2+c_perp \|H\|^2\|m_perp\|^2+2c_paru (Hm)u with coefficients rational in lambda=\|H\|^2/(2 sigma_H^2) and f_0=f_{K/2-1}(lambda); Dawson at K=3, elementary for even K. | Derived the five coefficients independently (moments of A=h g_1/S and B=g_1^2/S); SymPy difference with the note's formulas is identically 0. Quadrature of the defining expectation in spherical coordinates (not the Schwinger integral): K=3 registered instance closed=quad=0.559329501770; K=4 0.790061867155 both (diff 1.4e-13); K=5 0.6788280837 both, MC from definitions 0.679269+/-3.9e-4 (z=+1.14). C3(a): direct 3D vs 1D integral, diff<=1.3e-15 at two points. Planted errors detected (gaps 0.12, 2e-3, 6e-3; z=-10.4). K=3 Dawson and K=4 elementary forms checked. | Coefficient formulas appear only in the script function rc1_isotropic_closed, not in the note: c_R=(lambda/2)((K-1)f_1-(K-3)f_0), c_u=c_R-2 lambda f_1+1, c_par=((K^2-1)/4)(f_1-f_2), c_perp=((K+1)/4)f_2-((K-1)/4)f_1, c_paru=((K-1)(K-2)/4)(f_1-f_0), f_{j+1}=(1-(K/2-1+j)f_j)/lambda. |
| C4 | proved | confirmed-with-correction | No elementary closed form in general: (1) odd K, r_c=1, P=pI gives R_1+R_2 f_{1/2} with R_2 not identically 0; (2) r_c=2,K=4,HH^T=s^2 I: sigma_H^2 E[(Hhat Hhat^T)^{-1}]=[(1-e^{-2 lambda})/(4 lambda)+((1+lambda)/(2 lambda))e^{-lambda}Shi(lambda)]I; (3) anisotropic P, r_c=1,K=3: the sigma_H->infinity coefficient is a Carlson R_F,R_D combination. | (1) R_2 not 0 follows from my form of c_R and the recurrence; Liouville criterion read, not checked against a source. (2) Own route (condition on one row; inverse noncentral chi-square_3 is a Dawson function; 3D Gauss quadrature) agrees with the Shi formula to 1e-6 to 3e-6 at lambda=0.3,1,1.7,3.5; Shi->sinh/lambda is off by 4e-2 to 1.1; linear-combination identity rederived; series resummation not rederived by hand. (3) Rederived the limit integral; Carlson reduction rests on the stored script (diff<=1.6e-15). | Correction of wording only: (3) is non-elementarity of a sigma_H-independent coefficient in (p_1,p_2,p_3), not an obstruction in sigma_H. C4 excludes elementary forms; it does not support the Reporting-gate phrase that an integral is structurally optimal. |
| C5 | proved | confirmed | (a) small sigma_H: C1(3) reproduces prop:lrn-understanding-expansion; for r_c=1,P=pI the sigma_H^4 coefficient is explicit and the (R_c,u^2) series terminates at K=4; (b) large sigma_H limits; (c) for r_c<=K<=r_c+1 and Pr(y!=0)>0, E[(v^T psi)^2]=infinity for every v!=0; finite if y=0 a.s. | (a) SymPy series of C3(b): order 0 is R_c, order 2 equals the proposition's bracket, order 4 equals the note's coefficient (difference 0); K=4 termination checked. (b) checked roughly: one point r_c=1,K=3,sigma_H=60 (0.84646 vs limit 0.84650); Vitali argument read only. (c) read and checked each step against lem:lrn-schur and lem:lrn-inverse-norm(c). | (b) and the general-r_c Haar-moment formulas are partial coverage. No numerical check of (c) for r_c>=2 exists anywhere. |

Script audit. verify_open_lrn_noncentral.py: rerun (rc=0, 40 s) identical to stored output after decoding (51 lines, 0 differing; stored file is UTF-16). All numbers quoted in the note match the output. Checks 1, 2, 3, 6 can fail and have real planted-error controls. Check 4's control compares the formula with a modified copy of itself (vacuous), and the K=3,4 closed forms and the Shi formula (check 5) are tested only against other consequences of the same derivation chain; my quadratures of the definitions close that gap. The earlier verifier's script and numbers cited in the Check fields are not in the repository.

Remaining open:
- Closed form in named special functions for r_c>=2 (at least P=pI), or a reason none exists; Hillier-Kan and Letac-Massam unread.
- Primary-source locator for the Liouville criterion and for non-elementarity of Shi.
- Proof text (cleaned_writeup.md) and the C2, C3 formulas are not in the repository.
- Truncated moments and regularized gains for K<=r_c+1 (second half of open:fw-understanding-risk) are out of the note's scope and stay open.

### Note `open_hie_record_contrast.md`

Target: open:hie-record-contrast (s10b_hierarchy.tex:304-306); related open:col-records-baseline (s04_collectives.tex:165-167)

Declared record status: active (C1-C7 proved, Review: self; O1 and O2 open)

Status justified? Yes, active is right, and the locked statement quotes the manuscript correctly. Clause 1 (which record noises give a diffusive precision): settled exactly for closed collectives (interval [kappa_min,kappa_max] q_rev), for every population with coupled outsiders above q_rev (never), at q_z=0 (iff closed, delta=0, a_ij>=omega/n), and for populations with an automorphism-related uncoupled pair (only q_rev), which covers every open instance of obs:hie-record-window. Not settled for general open populations below q_rev: first-order criterion and witnesses only, q_min not determined, O1 open. The note's 'Reading chosen: full characterization' is therefore not met for open populations. Clause 2: answered (weighted contrast definable; weighted size bound holds but gives no extent bound for a global record and the admissibility floor rises to 1+R). Clause 3: a declaration is proposed with proved properties; adoption is the author's decision.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C1 | proved | confirmed | Closed collective: exact Pi(kappa), q_z=kappa q_rev; diffusive iff kappa in [kappa_min,kappa_max], kappa_max=1+delta T/(eps omega), kappa_min=1 if some member pair is uncoupled, else max{beta delta/(eps T+beta delta),kappa_off}<1; members' marginal precision diffusive for every kappa>=0. | Rederived the reduction to span{1_C/sqrt n,e_z} and the interval logic, including a proof that n a_min>=omega+delta gives kappa_off=0 (concave quadratic with g(0)<=0 and g'(0)<0). Own code: closed form vs Lyapunov inverse on 400 random closed graphs incl. n=2, max rel err 1.1e-11; interval prediction matched on 2930 decided (instance,kappa) pairs; W1 recomputed exactly (rows sums 0,0,4/5; Pi_01=-19/20). | Matches eq:hie-noiseless at kappa=0, delta=0. Refutes the unqualified sentence at s10b_hierarchy.tex:158. |
| C2 | proved | confirmed | (1) R=S-Pi~ solves R Pi~+Pi~ R=2 eta (Pi~ e_z)(Pi~ e_z)^T; (2) with cut(C)>0, any delta>=0, every q_z>q_rev gives a strictly positive off-diagonal entry; (3) with delta=0, closed or open, q_z>q_rev is not diffusive. | Derived (1) and (2) myself before reading the write-up (same integration by parts: R_oz=-2 eta int w_o w_z'' <0 for an outsider, S_oz=0); (3) read and checked. Own code: 2400 open instances at ratios 1.02 to 30, all with a positive off-diagonal entry (smallest relative size 3e-8). | Uses only S_oz=0, a coupled outsider, and Sigma_oz>0; delta is not used in (2). |
| C3 | proved | confirmed | At q_z=0: (M Sigma)_zz=0, (M Sigma)_iz>0 on agents connected to C, sum_i r_i (M Sigma)_iz=-delta; Pi(0) is diffusive iff cut(C)=0, delta=0 and a_ij>=omega/n for all member pairs. | Derived the identity (Pi M Sigma=2 Pi Q-M^T), the sign of (M Sigma)_iz, and the delta=0, cut>0 contradiction (Sigma e_z constant forces Pi_oz=0 against R_oz>0) independently. Own code: 300 open instances, identity holds, none diffusive; threshold checked on closed K_2 at a=0.049 and 0.051 (omega/n=0.05). |  |
| C4 | proved | confirmed | With coupled outsiders: (1) an uncoupled pair related by an automorphism preserving C has Pi_ij>0 for all q_z<q_rev, so diffusive iff q_z=q_rev; (2) near q_rev, (SYS)_oz<0 and (SYS d)_z>0, so (SYS)_uv<0 on missing agent edges is sufficient and <=0 necessary for a left window; (3) complete graphs on V_0 always have a left window; a non-complete witness W3 exists. | Rederived (1) and (2). Own code: open16 instance has Pi_02>0 at ratios 0, 0.5, 0.99 for delta=0 and 0.01; finite-difference check of dPi~/d eta=-SYS (err 1.4e-10); W2 (K_3) diffusive at ratios 0.1 to 1.0 (delta=0) and 0.25 to 1.0 (delta=0.05), not at 0 or 1.1; W3 diffusive at 0.9 and 0.99, not at 0.5, 0.8, 1.1. | Existence only: q_min is not determined and the diffusive set below q_rev is not shown to be an interval. O1 (asymmetric uncoupled member pairs) stays open; my 4000-instance probe found no case of (SYS)_01<=0, a numerical observation only. |
| C5 | proved | confirmed | (1) With outsiders the agents' marginal precision at q_rev is M_schur/q, strictly diffusive except zeros on uncoupled pairs not both in C, with derivative -(1/q)M_schur Y_VV M_schur; two-sided window when no such pair exists. (2) Discrete time: Pi_rev,oz=-(beta/q)sum_{i in C}a_io<0 for distance-1 outsiders (two-sided windows possible); for outsiders at distance>=2 with U psd the derivative of Pi_oz is >0. | Rederived (Sigma~=S^{-1}+eta Y is exact; summation by parts for the discrete case, using both U psd and W>=0). Own code: Schur form (err 4e-15), derivative formula (err 7e-11), W4, W6a, W6b recomputed in floating point. Open16 derivative signs taken from the stored output. | The discrete barrier is first order only, as the note says. |
| C6 | proved | confirmed | Weighted contrast r_W with W=Q^{-1}: at q_rev, r_W(C')=(1+R)min{eps+beta+lambda_2(L_C), beta+omega+(eps R+delta)/(1+R)}/(eps+R delta+cut(C)/n); weighted size bound r_W<=eps_max^M/eps_bar^W+varsigma_W^2/(2 eps_bar^W Var_W); for a global record the floor is (1+R)eps/(eps+R delta), Var_W=Var/(1+R), varsigma_W^2>=beta Var(C). | Rederived formula, bound (test function x-xbar_W) and the three scope statements. Own generalized-eigenvalue code on 200 random instances: rel err 3e-14; dropping the 1+R factor gives 16% error. | The bound is an inequality (header says 'exact'). It holds but does not bound the extent of a collective with a global record. |
| C7 | proved | status-overstated | Typed comparison medium (leaks averaged per type, couplings per declared type class): (1) reduces to def:col-baseline without records; (2) whole-population exclusion under a transitive type-preserving symmetry group; (3) uniform finite baseline on Z^D x {A,Z} with an explicit constant; (4) the two-rings-of-8 instance is below baseline (12.9501<27.6403); a 9-node analogue is a collective at eps=0.20 and 0.50. | (2) rederived (group average, concavity of xi_in, invariance of xi_out). (3) read line by line, both cases and both size ranges, constant 3^{(D-1)/D}2^{2+2/D} confirmed; own exhaustive check at D=1 (4083 regions, 7 leak pairs, 3 coupling ratios): max r 1.33, 10.0, 1.90 against bounds 32, 56, 246. (4) recomputed: 27.6403 and the three 9-node rows reproduced; the 9-node baseline is attained by the whole population. | (1)-(3) are theorems about a proposed definition; (4) is computed, not proved; 27.6403 is absent from the stored script. Earned status: proposal with proved properties plus computed instances. (2) does not apply to the 17-node prism instance (not edge-transitive), and the note does not claim it does. |

Script audit. verify_hie_record_contrast.py: rerun (rc=0, 137 s) identical to stored output after decoding (61 lines, 0 differing; stored file is UTF-16). When I started the rerun file was empty; it arrived later. Quoted numbers match the output except 27.6403 (C7(4)), which the script never computes. Residual checks of the defining Lyapunov equation, the exact rational witnesses and the random-instance assertions can fail. Vacuous or weak: the C1 control compares two numbers (1.5 vs 2.65); the C5 control only prints; the C7 control measures a difference built in by construction; the C6 n=100 'instance' evaluates the formula; the C7(3) test uses 32 varsigma^2/a_nn where the claim gives 16 and reaches max r=1.0 against B=64, so it cannot detect a wrong constant.

Remaining open:
- O1: asymmetric graphs with an uncoupled member pair below q_rev (sign of (SYS)_ij).
- O2: independent proof check; this review is one fresh-context reconstruction.
- q_min and interval structure of the diffusive set for open populations with a left window.
- Author's decision on the typed comparison medium, including averaging a record of C over V x {z} or over C x {z}; under the proposal C' of chk:hie-record-precision is not a collective at eps=0.02.
- Proof text (cleaned_writeup_hie_record.md) is not in the repository.

### Findings

**record_contrast_lrn/F1** (major, status-or-scope) at open_lrn_noncentral.md lines 3 and 122-128, against ext5_lrn.tex:143-145

Record status 'closed/resolved' overstates what was established for the manuscript's open problem.

Evidence: The problem asks for E[psi psi^T] in closed form as a function of sigma_H for K>=r_c+2. Delivered: closed form only for r_c=1, P=pI (C3b); 1D integral for r_c=1 general P; cone integral with unwritten integrand polynomial for r_c>=2. C4 excludes elementary forms only. The Searches table states Hillier-Kan (2022) and Letac-Massam (2008) were not opened. The Reporting gate calls the integral 'structurally optimal', which C4 does not support.

Fix: Record a residual obligation (special-function closed form for r_c>=2, at least P=pI) or reopen; in the manuscript replace open:lrn-noncentral by a narrowed problem instead of deleting it.

**record_contrast_lrn/F2** (major, status-or-scope) at Evidence lines of every claim in both notes

The proofs of both notes are not in the repository; lrn formulas and the earlier verifier's evidence are not reproducible from it.

Evidence: Evidence points to C:\Users\chris and christine\.gemini\antigravity\brain\2b88195c-...\scratch\swarm_lrn_noncentral\cleaned_writeup.md and swarm_hie_record\cleaned_writeup_hie_record.md (they exist today, 65 KB and 68 KB). The lrn Check fields cite verify_lrn_noncentral.py and numbers (1.18e-14; 0.474591 vs 0.472560 +/- 0.014039; 5.83e-16) found in no repository file. The lrn note states neither the C2 integrand nor the C3 coefficients; the latter exist only in rc1_isotropic_closed of the script.

Fix: Copy the write-ups (or their proofs) into docs/research next to the notes and write the C3 coefficient formulas into the note before any manuscript text cites these results.

**record_contrast_lrn/F3** (major, integration) at Collective_Agents/sections/s10b_hierarchy.tex:158 and :165

The manuscript says a noiseless record always leaves the diffusive class; this is false.

Evidence: Closed K_2, a_01=1, eps=1/10, beta=1/5, omega=1/10, delta=0, q=1, q_z=0: exact Pi=[[27/20,-19/20,-2/5],[-19/20,27/20,-2/5],[-2/5,-2/5,8/5]], row sums 0,0,4/5: diffusive (recomputed in SymPy). Threshold confirmed numerically: diffusive at a=0.051, not at a=0.049 (omega/n=0.05). Line 165 concludes 'is not diffusive' without assuming some pair has a_ij<omega/n.

Fix: State: Pi(0) is diffusive iff the collective is closed, delta=0 and a_ij>=omega/n for every member pair; otherwise it is not (note C3).

**record_contrast_lrn/F4** (minor, status-or-scope) at open_hie_record_contrast.md line 17 (Reading chosen) and line 129 (Log)

The note announces a full characterization of the diffusive set for open populations; the result is partial.

Evidence: With outsiders: D is contained in (0,q_rev] (C2, C3); D={q_rev} under an automorphism-related uncoupled pair (C4(1)); otherwise only a first-order criterion and witnesses (C4(2),(3)); O1 open; q_min not determined.

Fix: Qualify the Log and Reading lines; when narrowing the manuscript problem keep the general open-population case below q_rev as open.

**record_contrast_lrn/F5** (minor, status-or-scope) at open_hie_record_contrast.md C7

One status 'proved' covers a proposed definition, theorems about it and computed instances.

Evidence: C7(4) values are computations; the medium averages the record's couplings over all of V x {z}, a modeling choice. Under it r_hom(V u {z})=27.6403>r(C')=12.9501 at eps=0.02 (reproduced), so the manuscript's own instance is not a collective.

Fix: Split the status (proposal; proved (1)-(3); computed (4)) and put the consequence for chk:hie-record-precision in front of the author with the definition.

**record_contrast_lrn/F6** (minor, script) at open_hie_record_contrast-checks/verify_hie_record_contrast.py lines 639-767; note C7(4)

The 17-node baseline 27.6403 quoted in C7(4) is not computed by the stored script.

Evidence: Section title says '9-node / 17-node baselines' but the loop runs only the 9-node medium at eps=0.05,0.20,0.50; no output line contains 27.6403. My hie_check.py gives '17-node medium: r_hom(V u {z}) = 27.6403'.

Fix: Add the 17-node computation (prism graph, abar=41/60, bbar=0.1, eps=0.02) to the script and regenerate the output.

**record_contrast_lrn/F7** (minor, script) at verify_hie_record_contrast.py line 734 against note C7(3)

The fibered-lattice test uses a weaker constant than the claim and cannot discriminate.

Evidence: Claim at D=1: 2^{2+2/D} varsigma^2/a_nn=16 varsigma^2/a_nn; script: 32.0*varsigma_sq/a_nn. Observed max r/B=0.0156 with B=64, i.e. max r=1.0 over random scattered subsets. My exhaustive window test: max r 1.33, 10.0, 1.90 against bounds 32, 56, 246.

Fix: Use the claimed constant, test contiguous regions exhaustively, and say in the note that the bound is far from sharp.

**record_contrast_lrn/F8** (minor, script) at verify_hie_record_contrast.py lines 279-281, 540, 598-603, 769-783; verify_open_lrn_noncentral.py lines 512-523 and CHECK 5

Several 'negative controls' cannot fail, and some lrn checks compare one derived formula with another from the same chain.

Evidence: hie C1 control asserts |1.5-2.65|>1; hie C5 control is a print; hie C7 control compares two matrices built to differ; hie C6 n=100 case evaluates the formula only; lrn CHECK 4 control subtracts a term from the formula and asserts the result changed; lrn K=3,4 closed forms and the Shi formula are tested against the Schwinger integral, a Poisson series and the matrix-Laplace integral, never against the definition.

Fix: Replace each by a run of the actual check on the planted-wrong formula; add a definition-level quadrature or MC for K=3,4 and for the Shi formula (my lrn_c3_check.py and lrn_sym_check.py do this).

**record_contrast_lrn/F9** (minor, integration) at s10b_hierarchy.tex:169, :171-173, :176; 10b_hierarchy.tex:168

The manuscript presents as computed-only what the hie note now proves for the stated instances.

Evidence: obs:hie-record-window: closed delta=0 gives only q_rev and closed delta=0.01 gives [1,2.65] q_rev by C1 (my recomputation: diffusive at 1,1.01,1.1,2,2.6; not at 0.99,2.7,4); with outsiders only q_rev by C2 and C4(1) (uncoupled ring members related by a rotation or reflection).

Fix: After a proof check, restate the observation as a proposition for these instances and drop 'computed, not proved'.

**record_contrast_lrn/F10** (minor, integration) at ext5_lrn.tex:4; s02_framework.tex:149 and :151-154; 10e_open_problems.tex:96; s10b_hierarchy.tex:151; 10b_hierarchy.tex:222; 04_collectives.tex:227; s04_collectives.tex:165-167; 13_discussion.tex:43; s01_introduction.tex:150

Status summaries still describe both problems as fully open.

Evidence: Each line names the closed form of the second moment, or contrast and comparison media with record nodes, as open without qualification.

Fix: Update together with the integration of the results; the hie summaries only if the author adopts C6 and C7.

**record_contrast_lrn/F11** (minor, editorial) at both -checks folders; open_lrn_noncentral.md C4; open_hie_record_contrast.md C6

Encoding and wording slips.

Evidence: Stored outputs are UTF-16 (diff reports binary); lrn C4 is headed 'in sigma_H' while item (3) concerns elementarity in (p_1,p_2,p_3); hie C6 calls an inequality an 'exact' size bound; hie script comment says 1500 solves where 1200 are run; the lrn note embeds an absolute path into another tool's scratch folder.

Fix: Re-save outputs as UTF-8 and correct the wording.

### Collective_Agents touchpoints

| Location | Label | Relation | Detail |
|---|---|---|---|
| ext5_lrn.tex:143-145 | open:lrn-noncentral | stale-open-statement | Settled in closed form for r_c=1, P=pI; reduced to integrals and shown non-elementary otherwise. Should be narrowed, not removed. |
| ext5_lrn.tex:4 | section summary | stale-open-statement | 'Left open are the closed form of the second moment where it is finite'. |
| s02_framework.tex:149, 151-154 | open:fw-understanding-risk | stale-open-statement | First half duplicates open:lrn-noncentral; second half (truncated moment, regularized gain for K<=r_c+1) is outside the note and stays open. |
| 10e_open_problems.tex:96 | sec:opn-6 text | stale-open-statement | Lists the understanding error's exact second moment as open. The table row at line 37 does not list it and is unaffected. |
| ext5_lrn.tex:29-40 | prop:lrn-understanding-expansion | not-integrated | Manuscript form equals the note's orders 0 and 2 (my SymPy check: difference 0 for r_c=1, P=pI). The exact Stein form and the sigma_H^4 coefficient are not in the manuscript. |
| ext5_lrn.tex:12-27 | thm:lrn-understanding-moment | not-integrated | Consistent; note C5(c) sharpens part (a) at p=2 to divergence in every direction. |
| chkext5_lrn.tex:4-11, 36 | chk:lrn-understanding, chk:lrn-expansion | unaffected | No conflict with the note's numbers. |
| s10b_hierarchy.tex:304-306 | open:hie-record-contrast | stale-open-statement | Clause 1 partly settled, clause 2 answered, clause 3 proposed; general open populations below q_rev remain open. |
| s10b_hierarchy.tex:158 | sentence before ex:hie-noiseless-record | contradicted-by-note | 'for a noiseless record it always does' is false for closed collectives with delta=0 and all a_ij>=omega/n (exact witness K_2). |
| s10b_hierarchy.tex:160-166 | ex:hie-noiseless-record | integrated-matches | eq:hie-noiseless equals note C1 at kappa=0, delta=0 (checked by substitution). The sentence at line 165 needs the hypothesis that some pair has a_ij<omega/n. |
| s10b_hierarchy.tex:169 | text after the example | stale-open-statement | 'Near the reversible noise the sign pattern was computed, not proved' is superseded by C2 and C4; 'safe substitute only in closed collectives' is refined by C5(1). |
| s10b_hierarchy.tex:171-173 | obs:hie-record-window | not-integrated | Every statement follows from C1, C2, C4(1); my recomputation reproduces the pattern. |
| s10b_hierarchy.tex:176 | sentence after the observation | partially-integrated | True of the computed instances and now proved for them; not universal (complete graphs have a left window, C4(3)). |
| s10b_hierarchy.tex:136-151 | prop:hie-record-contrast | unaffected | Used as input; r(C')=12.950139 reproduced. The remark at line 151 that a comparison medium is missing becomes stale if C7 is adopted. |
| s10b_hierarchy.tex:153-155 | rem:hie-memory-absent | not-integrated | Note C6 defines the weighted contrast the remark points to; the remark's (eps+R delta)/(1+R) is xi_out^W of a closed collective. |
| 10b_hierarchy.tex:166-168, 222, 224 | main-text summaries | stale-open-statement | Cite the numerical observation and the missing declared geometry. |
| 04_collectives.tex:227; s04_collectives.tex:165-167 | open:col-records-baseline | stale-open-statement | Note C7 proposes what the problem asks for (types, declared positions, averaging classes); pending the author's decision. |
| 04_collectives.tex:197-209 | def:col-baseline | not-integrated | C7 would add typed clauses and reduces to this definition when there are no records. |
| 04_collectives.tex:237-243, 276-282 | thm:col-lattice-contrast, thm:col-contrast-size | unaffected | Used by C6 and C7 in the form stated. |
| 13_discussion.tex:43; s01_introduction.tex:150 | status summaries | stale-open-statement | Describe contrast and comparison media with record nodes as open. |
| chk10b_hierarchy.tex:38-42; app10b_hierarchy.tex:155-171 | chk:hie-record-precision, proofs | unaffected | Numbers and derivations agree with the note and with my recomputation. |
| 00_abstract.tex; 11_predictions.tex; 10e_open_problems.tex tables | none | unaffected | No mention of either problem found by label or key-term grep. |

### Integration candidates

| Result | Target | Readiness | Why |
|---|---|---|---|
| open_lrn_noncentral C3(b): for r_c=1, P=pI_K, K>=3, E[psi^2\|m_i,u]=c_R R_c+c_u u^2+c_par (Hm_i)^2+c_perp \|H\|^2\|m_perp\|^2+2c_paru (Hm_i)u with coefficients rational in lambda=\|H\|^2/(2 sigma_H^2) and f_{K/2-1}(lambda). | ext5_lrn.tex after prop:lrn-understanding-expansion (new proposition), proof in appext5_lrn.tex, one line in chkext5_lrn.tex | ready-after-minor-fix | Coefficients rederived independently (symbolic difference 0) and checked against the definition at three points; the formulas and proof must first be written into the repository. |
| open_lrn_noncentral C1: I-E[HO]=sigma_H^2 E[tr(P^+)S^{-1}-O^T O] and the exact form E[psi psi^T]=R_c+sigma_H^2 E[...] for K>=r_c+2. | appext5_lrn.tex, new lemma before the proof of prop:lrn-understanding-expansion | ready-after-minor-fix | Reconstructed in full; the integrability step for Stein's identity on a function singular on the rank-drop set should be written out. |
| open_lrn_noncentral C3(a) and C2: integral representations (1D for r_c=1; cone integral for general r_c). | ext5_lrn.tex, remark after the new proposition | needs-fresh-proof-check | r_c=1 confirmed against the definition; for general r_c the integrand polynomial is not written out and I only read the proof. |
| open_lrn_noncentral C4: no elementary closed form in sigma_H for odd K at r_c=1, nor at r_c=2, K=4 (Shi). | ext5_lrn.tex:143-145 (narrowed open problem); s02_framework.tex:149-154; ext5_lrn.tex:4; 10e_open_problems.tex:96 | ready-after-minor-fix | Argument sound given C3(b); Shi formula confirmed numerically by an independent route; a primary source for the Liouville criterion must be read and cited. |
| open_lrn_noncentral C5(a): sigma_H^4 coefficient [(K-4)(3K-8)R_c+(K-4)^2u^2+(K^2-1)(Hm)^2-(2K-1)\|H\|^2\|m_perp\|^2-2(K-1)(K-2)(Hm)u]/\|H\|^4 for r_c=1, P=pI. | ext5_lrn.tex, sentence after prop:lrn-understanding-expansion | ready | Confirmed symbolically from the closed form; orders 0 and 2 agree with the proposition. |
| open_lrn_noncentral C5(c): for r_c<=K<=r_c+1 and Pr(y!=0)>0, E[(v^T psi)^2]=infinity for every v!=0. | ext5_lrn.tex thm:lrn-understanding-moment(a), added clause; proof in appext5_lrn.tex | ready-after-minor-fix | A two-line variant of the manuscript's own proof; each step checked. |
| open_hie_record_contrast C3 with witness W1: Pi(0) is diffusive iff cut(C)=0, delta=0, a_ij>=omega/n for all member pairs. | s10b_hierarchy.tex:158 and :165 (correction of a false sentence), ex:hie-noiseless-record | ready | The manuscript sentence is false as written; the correction is confirmed exactly and numerically. |
| open_hie_record_contrast C1: closed collective, exact Pi(kappa) and diffusivity interval [kappa_min,kappa_max] with kappa_max=1+delta T/(eps omega). | s10b_hierarchy.tex, new proposition next to ex:hie-noiseless-record; proof in app10b_hierarchy.tex | ready-after-minor-fix | Reconstructed and checked on 400 instances; needs the proof text in the repository. |
| open_hie_record_contrast C2: with coupled outsiders, Pi(q_z) has a positive off-diagonal entry for every q_z>q_rev; with delta=0 no q_z>q_rev is diffusive. | s10b_hierarchy.tex, new proposition replacing the 'computed, not proved' remark at line 169 | ready-after-minor-fix | Derived independently by the same short argument; 2400 instances agree. |
| open_hie_record_contrast C4: only q_rev is diffusive when an uncoupled pair is related by an automorphism preserving C; first-order criterion and left windows otherwise. | s10b_hierarchy.tex obs:hie-record-window (upgrade to proposition for its instances), remark for C4(2),(3), narrowed open:hie-record-contrast | ready-after-minor-fix | Reconstructed; the remaining general case (O1, q_min) must stay in the open problem. |
| open_hie_record_contrast C5: marginal precision with outsiders (two-sided window when no uncoupled pair lies outside C x C) and discrete-time comparison. | s10b_hierarchy.tex:169 (amended sentence) and a remark; prop:hie-record-contrast(d) discussion | ready-after-minor-fix | Reconstructed; state W>=0 and U psd explicitly in the discrete part. |
| open_hie_record_contrast C6: weighted contrast r_W and weighted size bound; r_W(C')=(1+R)min{...}/(eps+R delta+cut/n). | s10b_hierarchy.tex after rem:hie-memory-absent (definition and proposition); answers clause 2 of the open problem | ready-after-minor-fix | Mathematics confirmed; adopting a second contrast is the author's decision, and the text must say the bound gives no extent bound for a global record. |
| open_hie_record_contrast C7: typed comparison medium, whole-population exclusion, finite baseline on Z^D x {A,Z}. | 04_collectives.tex def:col-baseline (typed clauses), s04_collectives.tex prop:col-whole-population and open:col-records-baseline, thm:col-lattice-contrast extension | needs-fresh-proof-check | I found the proofs correct, but this changes a main-text definition, is the author's declaration to make, makes the manuscript's instance C' fall below baseline at eps=0.02, and the stored script neither computes 27.6403 nor tests the claimed constant. |

### MAgent_Theory_2.0 bearing

Searched MAgent_Theory_2.0/chapters/*.tex, companion/c04_interacting_memory.tex, companion/c17_communication_links.tex, README.md and future_TODO.md for: record, memory, contrast, comparison medium, baseline, diffusive, M-matrix, Stieltjes, reversib, Lyapunov, Wishart, noncentral, inverse moment, understanding, misunderstand, code error, dictionary uncertainty, second moment. lrn, exact shared object: chapters/17_communication_links.tex:104 and :124-128 define the receiving map as the gain O=Sigma_p A^T(A Sigma_p A^T)^{-1} fixed by the receiver's model A of the sender's code; this is the note's O with A=Hhat. MA makes no statement about a random code model, so nothing is contradicted or sharpened. lrn, interpretive only: chapters/18_link_dynamics.tex:170 ('uncertainty about the dictionary acts in the mean equations as additional record noise of variance c^2/s') and chapters/19_curvature_hierarchy.tex:25 (tangent approximation drops second and higher orders); the note shows that beyond that order the plug-in gain has a second moment only for K>=r_c+2 and is not an additive-noise term. The correspondence breaks because MA's uncertain object is the dictionary theta in GL(K) in a tangent Gaussian model with known codes, while CA's is the code model Hhat with independent Gaussian entries inside the inverse. MA chapter 11 uses central Wishart laws only. hie: none found; MA's 'record' is an agent's observation record (01_foundations.tex:139) and its 'contrast' (12_open_formation.tex:96) is a routing margin.

### To-do bearing

Workstream 1 (channel class with sender code T and receiver lift O; residual for non-invertible codes): the lrn result is a caution and an instance. With a Gaussian-uncertain code model inside the lift O the understanding error has a finite second moment only for K>=r_c+2 and an invertible (square) code has an infinite first moment, so a limit 'code learning converges to an invertible identification' cannot be stated in mean square for the plug-in lift under Gaussian code error; it needs a regularized gain, a truncation, or convergence in probability. For r_c=1, P=pI the residual is now an explicit function of |H|^2/(2 sigma_H^2). The mapping to the workstream's invertibility parameter is interpretive. Workstream 3 (timescale separation): hie C6 gives a contrast in which record memory counts, r_W(C')=(1+R)(1+beta/(eps+lambda_2))r(C) for delta=0 and omega>=lambda_2+eps/(1+R); an instance of a mixing-to-persistence ratio, not a derived threshold. Workstreams 2, 4, 5 and the cautions: none.

### Checker scripts

Not written: the Write tool refused 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/record_contrast_lrn/report.md ("Subagents should return findings as text, not write report files"), and I did not bypass it; the full content is carried in this structured output. Supporting scripts and outputs are in 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/record_contrast_lrn/ : lrn_c3_check.py/.out, lrn_c3a_check.py/.out, lrn_sym_check.py/.out, hie_check.py/.out, hie_check2.py/.out.


## Checker group `obj_strategic_a`

No mathematical defect located in C1 to C7 after a step-by-step reconstruction of every derivation and independent exact and numerical checks with failing planted-error controls. The "exact breakdown of lem:obj-moments" (C5) is a scope statement only: the lemma at appext3_obj.tex:32-38 carries the qualifier "with finite second moments" and is correct as stated. C1 invokes no external theorem (it proves both directions itself); its threshold is the known Bougerol-Picard criterion, whose bibliographic data I confirmed but whose theorem numbers I could not check against the source. Nothing is integrated: four manuscript statements still list open:obj-strategic(a) as open, and after integration the problem should be narrowed (the sign of a Lyapunov exponent is not a criterion computable from K), not deleted. I also answer the note's open obligation O2 affirmatively with an explicit 3x3 example.

Coverage. Claims checked by full step-by-step reconstruction: 7 of 7 (C1 to C7, all sub-parts), with independent exact algebra for C3(3), C5(1)-(2), C7 and independent numerics for C3, C4, C6 and C1(2). Checked roughly: 0. Failed routes: R1 and R2 confirmed consistent with C6 and C4; R3 skipped (fourth-moment radii not recomputed, not load-bearing). Obligations: O1 not auditable (cited files absent); O2 answered by my own example (single derivation). Not checked: Bougerol-Picard theorem numbers and hypotheses against the source text (bibliographic data and abstract-level claim confirmed by search; two fetches of the publisher page returned empty content); the stored script was not rerun by me (coordinator's rerun compared, identical); appext3_obj.tex lines 151-266 not read (scale-selection proofs, unrelated).

### Note `open_obj_strategic_a.md`

Target: open:obj-strategic(a) (ext3_obj.tex:164-166); also prop:obj-protocol (ext3_obj.tex:34-40), lem:obj-moments (appext3_obj.tex:32-38), thm:obj-rotation (ext3_obj.tex:15-30). The note's line references have not drifted.

Declared record status: Status: active (line 3); all seven claims 'proved', Review 'fresh-context'; Log line 415 reports the work as complete with only optional O2 open.

Status justified? The locked statement asked for (i) the exact iff threshold with no moment assumption for all n>=2 and d_i>=1, (ii) uniqueness, convergence, representation and (non-)Gaussianity of the law, (iii) comparison with rho(T)<1, rho(barA)<1 and Langevin stability, (iv) counterexamples. All four are established and I found no silent weakening: the header, claims and proofs use the same quantifiers (K not assumed invertible or symmetric, no moment assumption). 'Proved' is earned for C1 to C7. Two qualifications: the threshold is 'lambda_1<0', a characterization with closed forms only for n=2 (C3) and directed cycles (C6), so the manuscript problem is narrowed rather than exhausted; and 'active' contradicts the Log's 'complete'. The Review entries cite cleaned_writeup_obj_heatbath.md and verify_obj_heatbath.py, which are not in the repository, so the earlier review rounds cannot be audited.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C1 | proved | confirmed | For quadratic heat-bath deliberation with any n>=2, d_i>=1, K_d>0, arbitrary K, h, gamma: a stationary law exists iff the top Lyapunov exponent lambda_1 of the backward products of A_i is negative; then K is invertible, the law is unique, attracts every initial law weakly, equals E_omega N(u^N, Sigma(omega)) with Sigma>0 a.s., is symmetric about u^N and equivalent to Lebesgue measure. | Reconstructed Steps 1 to 4 line by line: Fekete with -infinity values; block SLLN with truncation; index reversal for forward and backward iterates; Sigma(omega) recursion and invariance; hitting-time induction for Sigma>0; small-ball bound giving tr Sigma_infinity finite; stopped conditional Borel-Cantelli (4a); greedy covering with Birkhoff and Fatou (4b). Checked irreducibility of the recursion by hand. Monte Carlo test of the invariance identity phi_mu(t)=(1/3)sum_i exp(-t_i^2/2)phi_mu(A_i^T t) on K(2) and on my O2 example (residual 0.0012 and 0.0003 against MC error 0.0026; control with the k=0 term dropped 0.0128 and 0.0441). | No external theorem is invoked; Bougerol-Picard 1992 is listed as context read 'via web summary only'. The paper exists (Ann. Probab. 20(4), 1714-1730) and its abstract-level claim matches; Theorem 2.5 and Lemma 3.4 numbering not checked against the source (two fetches returned empty pages). 'Gaussian scale mixture' (lines 39-40) should be 'mixture over a random covariance'. |
| C2(1) | proved | confirmed | A heat-bath stationary law is Gaussian iff K is symmetric positive definite; it is then N(u^N,(gamma K)^-1), unique and reversible. | Reconstructed the moment-generating-function argument (a Gaussian equal to an equal mixture of n Gaussians forces mu T_i = mu for every i), the conditional-law step and the reduction to thm:obj-rotation(b); checked that the manuscript proof of (b) (appext3_obj.tex:21-25) needs only swap invariance of mu x T, which is what the note supplies. | None. |
| C2(2) | proved | confirmed | If a centered Gaussian variance mixture E N(0,V) equals a finite Gaussian mixture with M components, all component means vanish and law(V) has at most M atoms; hence infinite support of v^T Sigma(omega) v excludes every finite Gaussian mixture. | Reconstructed the induction: bottom-variance peeling, dominated convergence, Bohr mean, the sigma_j^2=0 case, mass bookkeeping for the restricted measure. Read and re-derived only; no numerical check exists or is needed. | None. |
| C3(1) | proved | confirmed | For n=2 and any d_1,d_2 with M=K_11^-1 K_12 K_22^-1 K_21: lambda_1=(1/4)ln rho(M) and rho(T)=(1+rho(M))/2, so the law exists iff rho(M)<1 iff rho(T)<1. | Re-derived the block form of T, the eigenvalue bound and the attaining eigenvector, the four block-power identities (verified exactly in SymPy for d=(2,3), m<=4). rho(T) formula on 40 random instances (18 with rho(M)>1, 3 with complex top eigenvalue) to 3e-14 and on a nilpotent M. lambda_1 via the exact finite-t expectation (binomial sum over run counts): slope +0.30316502 against +0.30316502, and -0.71515596 against -0.71515596; control with factor 1/2 fails. | Reduces to prop:obj-protocol at d_1=d_2=1. |
| C3(2) | proved | confirmed | For rho(M)<1 the law is the equal mixture of N(u^N,Sigma^(1)) and N(u^N,Sigma^(2)) with S_1 solving S_1 - M S_1 M^T = gamma^-1(K_11^-1 + A_12 K_22^-1 A_12^T); Gaussian iff K_12=K_21^T. | Re-derived mu_mix T_i = N(u^N,Sigma^(i)), the Schur complements, and K>0 from K_12=K_21^T with rho(M)<1. Closure identities to 6e-17 on an admissible instance (rho(M)=0.057, both components positive definite); control with a perturbed marginal gives 5e-2. | None. |
| C3(3) | proved | confirmed | K_(2,2) (d_1=d_2=2) has rho(M)=1/2, rho(T)=3/4, so the heat bath has a stationary law with all moments, while K has eigenvalues with negative real part, so Langevin deliberation has none. | Exact SymPy by my own code: A_12, A_21, M=[[1/2,0],[3/4,1/2]], det(-zI-K)=z^4+22z^3+(73/2)z^2-25z+25, charpoly of T on Sym_4 = lam^4(4lam-3)^3(4lam-1)^3/4096, eigenvalues -0.34723156 +- 0.60188388i. Checked the coefficient-sign argument. | None. |
| C4 | proved | confirmed | For all n, d_i, K with K_d>0: rho(T)>=(n-1)/n, 2 lambda_1 <= ln rho(T), rho(barA)^2 <= rho(T); hence rho(T)<1 implies existence and Re eig(K_d^-1 K)>0. | Re-derived all three inequalities (trace bound, E[P_t P_t^T]=T^t(I), Jensen). 300 random instances with mixed block dimensions: minimum slack 1.0e-4 and 6.7e-5, never negative. Consistent with the radii reported in chkext3_obj.tex:8 and :12. | Evidence line 85 ('verified numerically across all test families') overstates the stored script, which asserts two of the three inequalities on two cycle instances only. |
| C5(1)-(2) | proved | confirmed-with-correction | For K(c)=[[1,-c,c],[-1,1,0],[-1,0,1]]: all eigenvalues of K equal 1, A_2A_3A_1A_2A_3=0 so lambda_1=-infinity and a unique stationary law exists for every c; rho(T)<1 iff \|c\|<1, so for \|c\|>=1 the law has infinite second moment. | Exact SymPy with symbolic c: charpoly of K(c), the zero word, the full factorization of det(lam I - T), det(I-T)=(8/729)(1-c^2), the closed form of S_inf(c) substituted into S=T(S)+I/3, the three minors, the sum-of-squares identity; control with an altered entry fails. rho(T)=0.841280, 0.967071, 1.000000, 1.033759, 1.375253, 2.259784 at c=1/2, 9/10, 1, 11/10, 2, 4. Re-derived the Krein-Rutman pairing and the intermediate-value step. | Correction of wording only: the heading 'Exact Breakdown of lem:obj-moments' (line 88) misdescribes the result. The lemma is true as stated; what fails for n>=3 is the converse 'a stationary law has finite second moments'. |
| C5(3)-(4) | proved | confirmed | E\|u_1\|^p is infinite whenever \|c\|^p>=4 (no first moment for \|c\|>=4); for \|c\|>=1 Sigma_11 is unbounded, so the law is not sub-Gaussian and not a finite Gaussian mixture. | Re-derived the law of the collapsed word, P(H_m)=(1/6)4^-m, (A_1A_2)^r e_1=(c^r,c^(r-1),0) (exact, r<=5), the lower bound Sigma_11>=sum_r c^(2r) (exact on sample words for m=1,2,3) and the divergent series. Divergence itself cannot be tested numerically. | Line 96: 'the finite-first-moment hypothesis in prop:obj-identification(b) is necessary' should read 'cannot be dropped under heat-bath deliberation for n>=3'. |
| C5(5) | proved | confirmed | For \|c\|>1 a neighborhood of K(c) in R^(3x3) has K_d>0, lambda_1<0 and rho(T)>1, so the heavy-tailed stationary regime has nonempty interior. | Re-derived the bound lambda_1(K)<=(242/243)ln M_0+(1/1215)ln\|\|P_5(K;w*)\|\| and the continuity of rho(T). The stored script tests one random perturbation. | None. |
| C6(1) | proved | confirmed | Directed n-cycle of scalar members with gains a_i and chi=prod a_i: lambda_1=ln\|chi\|/n^2 and rho(T)=(n-1+\|chi\|^(2/n))/n; the law exists iff \|chi\|<1 iff rho(T)<1. | Re-derived the diagonal reduction, both spectral inclusions, the counter invariant L(j)<=L(j+1)+1 and E S_t=t. For n=3,4,5 with unequal a_i and K_ii: rho(T) agrees to 8 digits (control with exponent 1 differs in the second digit), the deterministic bound on ln\|\|Q_t\|\| - S_t ln\|chi\|/n^2 holds along 30000 steps, max L - min L <= n-1. | Agrees with C3 at n=2. |
| C6(2)-(3) | proved | confirmed | For \|chi\|<1 every Sigma_ii(omega) is the constant s_i, so each one-dimensional marginal is exactly Gaussian; for n=3 and 0<\|chi\|<1 the joint law is not a finite Gaussian mixture. | Re-derived the row dynamics of the backward product and the six-step trace. \|Sigma_ii - s_i\|<=4e-15 on 30 random schedules with unequal parameters and gamma=0.8; cylinder formula Sigma_12=a_1 s_2 chi^(2m) to 4e-15 for m<=4 (control chi^m off by 2.2). | None. |
| C7 | proved | confirmed-with-correction | K_(3)=diag(1,1,1/100) M_(3) has rho(T)<1 (finite-variance heat-bath law) although its (1,2) pair has chi=1.21>1, while K_(3) has eigenvalues 21/10 and (-9+-sqrt 21)/200, so Langevin deliberation has no stationary law. | Exact SymPy by an independent code path: gamma S_inf, minors 2125/294, 27550/3087, 228950/7203, charpoly (10 lam-21)(2000 lam^2+180 lam+3)/20000, eigenvalues -0.067912878, -0.022087122, 2.1; rho(T)=0.908764; with D=I the eigenvalues are 0.2209, 0.6791, 2.1. | Clarity only (lines 126, 389-391): the displayed S_inf solves the equation with source I/(3 gamma), valid as a certificate of rho(T)<1, but it is not the stationary second moment for K_(3), whose source is diag(1,1,100)/(3 gamma) (minors 18800/147, 4820800/3087, 668288000/2401). |
| R1 | failed route | confirmed | Failed route: the cyclic family I + c*cycle cannot separate lambda_1<0 from rho(T)<1. | Checked against C6(1) with chi=(-c)^3 and the kernel vector (1,-1,1) at c=1 by hand. | None. |
| R2 | failed route | confirmed-with-correction | Failed route: with K_d=I and rho(T)<1 no heat-bath-stable, Langevin-unstable instance exists (by C4). | Follows from C4. Its reopen question is O2, which I answer with an explicit example. | With K_d=I and rho(T)>=1 such instances exist: see O2. |
| R3 | failed route | not-verified | Failed route: a=6/5 has rho(T)=0.96016<1 but fourth-moment radius 1.03081>1; a=11/10 has 0.93628. | Read only; the fourth-moment radii were not recomputed. | Not load-bearing. |
| O1 | closed | not-verified | Fresh-context proof check by a verifier of C1 to C7, completed with one repair (admissible rescalings in C1(1)). | Searched the Research folder for the two files the Review Log cites; neither exists. Checked the repaired wording of C1(1) myself: correct. | The review trail cannot be audited from the repository. |
| O2 | open, optional | confirmed-with-correction | Open: is there K with K_d=I and lambda_1<0 while rho(barA)>=1 or min Re eig(K)<=0? | Constructed and verified exactly (SymPy) K_o=[[1,-1,0],[-7,1,-7],[1,0,1]]: A_2A_3A_1A_2A_3=0, charpoly lam^3-3lam^2-4lam-1, eigenvalues -0.69202, -0.35690, 4.04892, rho(barA)=1.2307, rho(T)=2.781; control with entry -6 breaks the zero word. | Answer: yes. Single reviewer derivation; needs an independent check before it is recorded as a claim. |

Script audit. One script (491 lines, fixed seeds). The coordinator's rerun (rc 0, 13 s) matches the stored output on all 48 lines, and every number quoted in the note matches. Blocks 0, 1, 3, 4 compare independently computed quantities and could fail; no formula is compared with itself. Weak points: block 2 prints the minors of S_inf(c) without asserting them, and neither the closed form of S_inf(c) nor the full charpoly factorization of T is tested (I confirmed all three exactly); C4 is asserted on two cycle instances only and rho(T)>=(n-1)/n never; negative control 3 uses a 0.05 threshold against an exact gap of 0.0585; the s_i formula is tested at one symmetric instance; open-set persistence on one perturbation. The forward-against-backward quantile test for K(2) (tolerances 8 and 10 percent, observed 1.7 and 0.6 percent) is the only stored test of C1(2) under heavy tails and can fail. My scripts, each under 20 s with planted-error controls: check_a_exact.py, check_b_numeric.py, check_c_supp.py in 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/obj_strategic_a/ (outputs alongside as .out). The 'det Sigma min' numbers printed by check_b_numeric.py are overflow artifacts and test nothing.

Remaining open:
- A criterion for lambda_1(K)<0 computable from K for general n>=3; closed forms exist only for n=2 and directed cycles.
- Tail index of the stationary law and exact moment thresholds (for K(c): infinite variance iff |c|>=1 and infinite p-th moment for |c|^p>=4 are proved; the exact p-threshold is not).
- Classification of finite against infinite Gaussian mixtures in general (for example K(c) with |c|<1).
- Rate and mode of convergence beyond weak convergence.
- Independent check of the reviewer's O2 example K_o and of the remark that, for scalar acts, a finite first moment forces rho(barA)<=1.
- Source read of Bougerol and Picard (1992) for statement and numbering; a literature pass on random-scan samplers with incompatible conditionals and on Kesten-type tails.
- The regime of R3 (finite variance, infinite fourth moment).

### Findings

**obj_strategic_a/M1** (minor, mathematical) at open_obj_strategic_a.md line 157 (O2) and line 146 (R2 reopen condition)

Not a defect: O2 has an affirmative answer. With K_d=I a heat-bath stationary law can exist while K has negative eigenvalues and rho(barA)>1.

Evidence: K_o=[[1,-1,0],[-7,1,-7],[1,0,1]]: A_2A_3A_1A_2A_3=0 exactly, so lambda_1=-infinity and C1 gives a unique stationary law; charpoly lam^3-3lam^2-4lam-1 with roots -0.69202, -0.35690, 4.04892; rho(barA)=1.2307. Family: K=I-N with N_32=0 and N_12(N_21+N_23 N_31)+N_13 N_31=0 kills the word (2,3,1,2,3) and gives charpoly(N)=x^3+gx-g, g=N_12 N_23 N_31, with a real root above 1 when g<-27/4. Control with N_23=6: word nonzero. Script check_a_exact.py.

Fix: After an independent check, record K_o as a claim, close O2 and update R2. Optional remark to verify: for scalar acts a finite first moment forces barA power bounded, so lambda_1<0 with rho(barA)>1 implies no first moment.

**obj_strategic_a/S1** (minor, status-or-scope) at open_obj_strategic_a.md line 88 (C5 heading), lines 95 and 408; manuscript appext3_obj.tex:32-38

'Exact breakdown of lem:obj-moments' is a scope statement. The manuscript lemma is correct as stated; no manuscript defect.

Evidence: Lemma text: 'A stationary law with finite second moments exists if and only if the spectral radius of T is below one.' C5 exhibits a stationary law with rho(T)>=1 and infinite second moment, which the lemma permits. ext3_obj.tex:165 already says the lemma 'gives only the second-moment criterion'.

Fix: Retitle C5 'The second-moment criterion is not the existence threshold for n>=3' and state that lem:obj-moments is unaffected.

**obj_strategic_a/S2** (minor, status-or-scope) at open_obj_strategic_a.md lines 33-41 (C1) and 411-415 (reporting gate)

The 'exact threshold' is the sign of a top Lyapunov exponent, a characterization and not a criterion computable from K for general n>=3; the manuscript problem is narrowed, not exhausted.

Evidence: Closed forms only in C3 (n=2) and C6 (directed cycles); otherwise the sufficient conditions rho(T)<1 (C4) and a vanishing word (C5). The note's own gate item 3 concedes this.

Fix: When integrating, restate open:obj-strategic(a) as: find a criterion for lambda_1<0 computable from K beyond two members and directed cycles, and the tail index of the law.

**obj_strategic_a/S3** (minor, status-or-scope) at open_obj_strategic_a.md lines 163 and 414 (Literature, gate item 4)

C1(1) is the specialization of a known theorem (Bougerol and Picard 1992); the note proves it itself and lists the paper as context read 'via web summary only'.

Evidence: Citation is real: Ann. Probab. 20(4), 1714-1730, DOI 10.1214/aop/1176989526; abstract-level claim (necessary and sufficient condition for a strictly stationary solution independent of the future) matches. Irreducibility, needed for necessity there, holds here: an invariant affine subspace must contain range E_i for every i. Theorem 2.5 and Lemma 3.4 numbering not checked against the source (Project Euclid returned empty content twice).

Fix: Read the source, record the locator and hypotheses, and attribute the threshold in any manuscript text; the self-contained proof can stay.

**obj_strategic_a/S4** (minor, status-or-scope) at open_obj_strategic_a.md line 3 against line 415; Review Log lines 401-404

Record status 'active' contradicts the Log's 'complete', and the cited review artifacts are absent.

Evidence: cleaned_writeup_obj_heatbath.md and verify_obj_heatbath.py are not found anywhere under the Research folder.

Fix: Set one status; add the cited files or cite this check as the review of record.

**obj_strategic_a/P1** (minor, script) at verify_open_obj_strategic_a.py lines 260-278

The minors of S_inf(c) are printed but never asserted; the closed form of S_inf(c) (note line 330) and the full charpoly factorization of T (note line 327) are untested.

Evidence: Only the value at lam=1 is asserted (line 260). My exact check: 'charpoly(T) equals note's factorization: True', 'note's S_inf(c) solves S = T(S) + I/3 : True', 'minors M1,M2,M3 match the note: True'; control with an altered entry: False.

Fix: Add three assertions comparing the solved minors, the closed-form matrix and the factorization with the note's expressions.

**obj_strategic_a/P2** (minor, script) at open_obj_strategic_a.md line 85; verify_open_obj_strategic_a.py lines 354-357

C4's evidence line ('verified numerically across all test families') overstates the script.

Evidence: The script asserts 2 lambda_1<=ln rho(T) (with the predicted lambda_1) and rho(barA)^2<=rho(T) on the two cycle instances only, and never rho(T)>=(n-1)/n. My check on 300 random instances: minimum slack 9.97e-5 and 6.67e-5.

Fix: Either add a random-instance block for the three inequalities or reword the evidence line to name the two instances.

**obj_strategic_a/P3** (minor, script) at verify_open_obj_strategic_a.py lines 471, 372, 328

Thin or narrow checks: control 3 threshold 0.05 against an exact gap 0.0585; s_i formula tested only at a_i=-1/2, K_ii=1; one perturbation for open-set persistence.

Evidence: Stored output: mix 122.07, gauss 115.32, empirical 122.45. My checks cover unequal a_i, K_ii and gamma for C6(2)-(3).

Fix: Use an exact fourth-moment comparison for control 3 and one generic cycle instance for s_i.

**obj_strategic_a/I1** (minor, integration) at ext3_obj.tex:165, ext3_obj.tex:3, 10e_open_problems.tex:21, 10e_open_problems.tex:80

Nothing from the note is in the manuscript. These four statements are accurate today and become stale once C1 to C7 are integrated.

Evidence: All four say the heat-bath stationary law for nonsymmetric interaction beyond two scalar members is open; no .tex cites the note; note and check folder are untracked.

Fix: Integrate (see candidates), then narrow the open problem as in S2 at all four places.

**obj_strategic_a/I2** (minor, integration) at open_obj_strategic_a.md lines 165-170 (Searches)

Prior literature on the specific setting was not searched; novelty wording in the manuscript would be unsupported.

Evidence: The Searches table lists forward citations on Gibbs or heat-bath samplers with nonsymmetric Gaussian conditionals as 'not searched'. Leads I did not check against sources: samplers with incompatible conditionals (dependency networks, pseudo-Gibbs), Kesten-type tails for random affine recursions.

Fix: One literature pass before integration; phrase C1 as an application of the known criterion.

**obj_strategic_a/I3** (minor, integration) at ext3_obj.tex:93-97 (prop:obj-identification(b) and the paragraph after it)

Two manuscript sentences admit a sharpening from the note: the mean-response test presumes a first moment that can fail under heat-bath deliberation for n>=3, and under declared heat-bath deliberation a Gaussian cross-section does certify a potential game.

Evidence: C5(3): no first moment for |c|>=4 although K is Langevin stable; C1(2): every heat-bath law is symmetric about u^N=-K^-1 h, so the center responds as K^-1 without moments; C2(1): Gaussian iff K symmetric positive definite. The manuscript sentence 'A stationary cross-section ... can thus never certify' is justified there by Langevin deliberation only.

Fix: Add a qualifier or a part (d) to prop:obj-identification stating both facts for heat-bath deliberation.

**obj_strategic_a/E1** (minor, editorial) at open_obj_strategic_a.md lines 126 and 389-391

The displayed gamma S_inf for C7 is the fixed point with source I/(3 gamma), not the stationary second moment for K_(3).

Evidence: For K_(3) the source is diag(1,1,100)/(3 gamma); my exact minors are 18800/147, 4820800/3087, 668288000/2401. The stored script uses the correct source for its simulation check (line 436).

Fix: Add one clause saying the matrix is a certificate of rho(T)<1 for M_(3) with unit noise.

**obj_strategic_a/E2** (minor, editorial) at open_obj_strategic_a.md lines 39-40, 96, and the Derivations section

Terminology and style: 'Gaussian scale mixture' for a covariance mixture; 'necessary' at line 96; horizontal rules and bold run-in headings.

Evidence: A scale mixture has a scalar mixing variable; Sigma(omega) is a random matrix.

Fix: Use 'mixture of centered Gaussian laws over a random covariance'; reword line 96 as in S1; remove rules if the text is reused in the manuscript.

### Collective_Agents touchpoints

| Location | Label | Relation | Detail |
|---|---|---|---|
| ext3_obj.tex:164-166 | open:obj-strategic(a) | stale-open-statement | Accurate today (nothing integrated). The note settles existence (iff lambda_1<0), uniqueness, convergence and the mixture form for all n and d_i; after integration narrow to a computable criterion for lambda_1<0 and the tails. |
| ext3_obj.tex:3 | sec:obj introduction ('Left open ... heat-bath stationary law for nonsymmetric interaction beyond two scalar members') | stale-open-statement | Same narrowing after integration. |
| 10e_open_problems.tex:21 | tab:opn-status row 'Conflicting objectives', column Open | stale-open-statement | 'Nonsymmetric heat-bath laws beyond two scalar members' would need the narrowed wording; the Established and Where columns could cite the new statements. |
| 10e_open_problems.tex:80 | sec:opn-4 text | stale-open-statement | Lists the heat-bath stationary law beyond two scalar members as open. |
| ext3_obj.tex:34-40; appext3_obj.tex:44-60 | prop:obj-protocol | not-integrated | C3 reduces to it exactly at d_1=d_2=1 (rho(M)=\|chi\|, same two components, Gaussian iff K_12=K_21). The implication 'heat-bath law exists implies Langevin law exists', true for two scalar members, fails for two vector members (C3(3)) and three scalar members (C7; K_o with K_d=I). |
| appext3_obj.tex:32-42 | lem:obj-moments | unaffected | Correct as stated, hypotheses included (K invertible, finite second moments). C5 concerns its scope. C4 would add rho(T)>=(n-1)/n and rho(barA)^2<=rho(T); C1(2) gives symmetry about u^N without a moment hypothesis. |
| ext3_obj.tex:23; appext3_obj.tex:15-25 | thm:obj-rotation(b) | unaffected | Used by C2(1) with matching hypotheses; C2(1) strengthens 'reversible stationary law' to 'Gaussian stationary law'. |
| ext3_obj.tex:93-95; appext3_obj.tex:123 | prop:obj-identification(b) | unaffected | True as stated. Under heat-bath deliberation with n>=3 the first moment can be infinite (C5(3)), so the mean-response test can be undefined; the center of symmetry still responds as K^-1. |
| ext3_obj.tex:97 | paragraph after prop:obj-identification | not-integrated | 'A stationary cross-section ... can thus never certify that its members pursue one objective' holds for unknown or Langevin protocol; under declared heat-bath deliberation a Gaussian cross-section certifies K symmetric positive definite (C2(1)). |
| chkext3_obj.tex:8 and :12 | chk:obj-potential-type checks and chk:obj-protocol | unaffected | Reported radii obey C4: 0.9016^2=0.8129<=0.8253; 0.5590^2<=0.6250; 1.1180^2<=2.5000; rho(T)>=(n-1)/n in each. |
| 10e_open_problems.tex:78 | sec:opn-4 established results | unaffected | The negative results quoted concern two scalar members and Langevin deliberation. |
| 00_abstract.tex; 01_introduction.tex:162; 11_predictions.tex; 13_discussion.tex; s13_discussion.tex | front and back matter | unaffected | No statement about heat-bath laws for nonsymmetric K; the introduction only lists sec:obj among the extensions. |

### Integration candidates

| Result | Target | Readiness | Why |
|---|---|---|---|
| open_obj_strategic_a.md C1: for every n and d_i, heat-bath deliberation has a stationary law iff the top Lyapunov exponent lambda_1 of the products of the A_i is negative; the law is then unique, attracts every initial law weakly, equals E_omega N(u^N,Sigma(omega)) and is symmetric about u^N. | ext3_obj.tex, new proposition after prop:obj-protocol; proof in appext3_obj.tex after lem:obj-moments. | ready-after-minor-fix | Proof reconstructed in full with no defect. Fix: attribute the threshold to Bougerol and Picard (1992) after a source read, and replace 'scale mixture'. |
| C3(1)-(2): for n=2 and any d_1,d_2 the law exists iff rho(K_11^-1 K_12 K_22^-1 K_21)<1 iff rho(T)<1, with lambda_1=(1/4)ln rho(M), and is the stated equal mixture of two Gaussian laws; Gaussian iff K_12=K_21^T. | ext3_obj.tex, vector-act extension of prop:obj-protocol (new part or sibling proposition). | ready | Exact algebra and the Lyapunov formula confirmed independently; reduces to the existing proposition for scalar acts. |
| C2(1): a heat-bath stationary law is Gaussian iff K is symmetric positive definite. | ext3_obj.tex, corollary of thm:obj-rotation(b) or new part of prop:obj-identification with the qualifier at line 97. | ready | Short proof resting on a manuscript theorem whose hypotheses match. |
| C4: rho(T)>=(n-1)/n, 2 lambda_1<=ln rho(T), rho(barA)^2<=rho(T). | appext3_obj.tex, two sentences appended to lem:obj-moments. | ready | Elementary, confirmed by reconstruction and on 300 random instances; consistent with the numbers already in chkext3_obj.tex. |
| C5: for K(c) a stationary law exists for every c, has finite variance iff \|c\|<1, no first moment for \|c\|>=4, and the regime lambda_1<0<ln rho(T) is open in K. | appext3_obj.tex, example after lem:obj-moments; one sentence in ext3_obj.tex near prop:obj-identification(b). | ready-after-minor-fix | All parts confirmed. Fix: present it as the limit of the lemma's scope, not as a breakdown of the lemma. |
| C6(1)-(2): directed n-cycle with gains a_i: lambda_1=ln\|chi\|/n^2, rho(T)=(n-1+\|chi\|^(2/n))/n, exactly Gaussian one-dimensional marginals with variance s_i; C6(3) with C2(2): for n=3 the joint law is not a finite Gaussian mixture. | ext3_obj.tex or appext3_obj.tex, proposition; C6(3) and the identifiability lemma as a remark. | ready | Formulas confirmed for n=3,4,5 with unequal parameters; C6(3) is optional detail. |
| C3(3) and C7: K_(2,2) and K_(3) have a finite-variance heat-bath law and no Langevin law; reviewer's K_o=[[1,-1,0],[-7,1,-7],[1,0,1]] does the same with K_d=I (infinite variance). | ext3_obj.tex, example after prop:obj-protocol stating that the two protocols' existence regions are incomparable beyond two scalar members. | ready-after-minor-fix | K_(2,2) and K_(3) confirmed exactly; fix the C7 clarity point (E1). K_o is a single reviewer computation and needs an independent check before use. |
| Narrowed open problem: a criterion for lambda_1<0 computable from K beyond two members and directed cycles, and the tail index of the stationary law. | ext3_obj.tex:165 and :3; 10e_open_problems.tex:21 (table row) and :80. | ready-after-minor-fix | Depends on the items above being integrated first; the wording must not claim the problem closed. |
| Numerical check entry from verify_open_obj_strategic_a.py. | chkext3_obj.tex, new numcheck after chk:obj-protocol. | ready-after-minor-fix | Rerun reproduces exactly; add the assertions of P1 and P2 and place the script with the manuscript's check scripts. |

### MAgent_Theory_2.0 bearing

One interpretive bearing, none exact. MAgent_Theory_2.0/chapters/03_dynamics.tex:446-457 (prop:dyn-nonreciprocal) and :459-465 (prop:dyn-per-agent-contraction): a directed three-ring with convex weights is not a gradient flow yet contracts because each agent keeps a positive self weight. The note's C6 is the sampled quadratic counterpart on a directed n-cycle with arbitrary gains (law exists iff prod|a_i|<1); convex weights give |a_i|=w/(1+w)<1, inside that region, so the statements agree where they overlap. The correspondence breaks at: MA is a deterministic continuous-time flow on belief tables with probability weights and no sampling noise or existence question; CA is random sequential resampling of acts with unconstrained gains. 03_dynamics.tex:467 (Monderer-Shapley criterion) shares the hypothesis 'no exact potential' with C2(1). companion/c03_dynamics.tex:8 uses 'heat-bath move' as an analogy only. Nothing in the note contradicts an MA statement. Searched chapters, companion, future_TODO.md and Item files for: heat bath, Gibbs sampling, Glauber, Lyapunov exponent, random matrices, potential game, deliberation, nonreciprocal, antisymmetric part, asynchronous, Langevin, stationary law.

### To-do bearing

None on the five workstreams of manuscripts/research_to_do.md. Workstream 4 concerns distance laws of coupling, not the distribution of acts, so the heavy tails of C5 are not evidence for it and should not be listed there. No caution in the file is touched, and no change to the to-do file follows from this note.

### Checker scripts

NOT WRITTEN. The Write tool refused the report file ('Subagents should return findings as text, not write report files') and I did not work around the refusal, so 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/obj_strategic_a/report.md does not exist; this structured output carries the full content. Scripts and outputs that do exist in that folder: check_a_exact.py, check_a_exact.out, check_b_numeric.py, check_b_numeric.out, check_c_supp.py, check_c_supp.out.


## Checker group `prv_aware_minimal`

open_prv_aware: all seven claims hold as literally stated (derivations reconstructed, deciding instances reproduced exactly), but "closed" and "complete characterization for arbitrary schedules" are overstated: the per-window rank r*(E_i) is not jointly achievable when evidence about a window arrives after the member's next report (exact instance: per-window sum 3, transcript needed 4, single-transmission 5). open_prv_minimal: "active" is right; the block-table upper bound C1 and the cycle lower bound C2 are correct, C3 has a repairable defect when the last path is the direct edge (constant theta-1 becomes theta-2), and upper and lower bounds bracket the minimal storage without determining it, agreeing up to constants only on cycles, complete graphs, K_{2,k} and G_k. Neither note is cited by any .tex; every manuscript mention of the two problems still states them as fully open.

Coverage. 17 items in all. open_prv_aware: 7 claims (C1 split into two parts); 6 checked by step-by-step reconstruction plus my own exact computation (C1a, C1b, C3, C4, C5, C6), 2 by reconstruction only (C2, C7); 3 failed routes checked roughly (R2 recomputed by hand). open_prv_minimal: 5 claims; C1, C2, C3, C4 by reconstruction plus independent simulation or exhaustive check, C5 by reconstruction with invariants read; R1 rough, R2 not examined. Not done: stored scripts were read and their outputs compared with the coordinator's reruns, not rerun by me; aware C4(ii) and multi-member C5 re-derived but not recomputed; treewidth and feedback-vertex values of G_k taken from the note; no external source read (Charron-Bost 1991 is a lead only); the windmill bound is my own sketch without a second reader.

### Note `open_prv_aware.md`

Target: open:prv-aware (ext4_prv.tex:117-119; also prop:prv-aware, thm:prv-window)

Declared record status: closed (opened and closed 2026-11-22, one session)

Status justified? Partly. The locked statement asks for the least message dimension for exact fusion, between d (prop:prv-aware) and k rank H_i (thm:prv-window), when encoders know the model but reports are asynchronous or random; the note's locked statement equals the manuscript text. Established: d numbers fail off schedule (C3, exact); a per-window lower bound r*(E_i) for continuous or linear encoders with hub feedback allowed; an exact value for encoders that send each window once; closed forms under the hypotheses of C4, C5(a)(b), C6; both ends min(d, k r_i) and k r_i occur. Not established: the least per-contact dimension when a member may spread a window over several reports and deliveries arrive later than its next report (per-window numbers are then not jointly achievable), and a closed form for partial-rank sensing with pre-window variation. 'Closed' should be 'closed for single-transmission encoders and for schedules whose late deliveries precede the next report', with one residual obligation.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C1(a) | proved | confirmed | For Q_x>0, P_0>0: M_{D,t} = Cov(x_t,x_b\|o_D) Phi(D_<b), with Phi depending only on observations before b; the covariance factor is invertible when A is. | Reconstructed the block elimination and Woodbury step line by line. Exact rational check of my own (d=2, a=2, b=5, other members rank 1 and 2, t=5,6,7) holds exactly; planted error (dropping A^T Q^-1 A at b-1) is detected. |  |
| C1(b) | proved | confirmed-with-correction | Every exact star protocol with continuous window encoder has message dimension >= r*(E_i) = rank of the stacked sensitivities over reachable evaluations before the member's next report; a linear encoder of that dimension is exact on E_i. | Reconstructed the factorization-through-the-message argument and the invariance-of-domain step; computed an exact instance where the per-window numbers cannot be met jointly. | True as a per-window statement. The header 'Exact Least Message Dimension', the Alternative-forms line and the record status present it as the least dimension of an exact protocol. Instance (d=1, unit parameters; member 1 reports {1,2,3} at 3 and {4,5,6} at 6; member 2's observations at times 1, 2 arrive at 7, 8): r*(W1 before next report)=1, r*(W2)=2, total transcript needed 4, single-transmission total 5. |
| C2 | proved | confirmed | r* <= min(s_Phi d, d + sum q_tau, r_i + d + sum_{tau<=b-2} q_tau, k r_i), with corollaries for one configuration, bounded delay, causal broadcast and pre-window-only late evidence. | Reconstructed the resolvent decomposition, the cancellation in the pre-window term and bounds 2 and 3; corollaries follow by counting. No separate numerics; my Parts 3-5 respect the bound and attain it in one case. |  |
| C3 | refuted | confirmed | The claim that d numbers per contact suffice for model-aware members on a known asynchronous schedule is false (d=1, n=2, unit parameters, reports at t=2 and t=3). | Recomputed by covariance conditioning in exact rationals: weights (1/4,5/8) and (2/45,7/45), variances 5/8 and 26/45, determinant 1/90; synchronized control (2/19,7/19) gives determinant 0. | In this instance the value 2 equals the blind bound k rank H_i. |
| C4 | proved | confirmed | With full-rank proportional sensing and s configurations differing by distinct scalar multiples of I (x) Lambda, the least dimension is min(s,k) d; specializations to staggered schedules and aligned random delays. | Reconstructed the polynomial clearing and block-tridiagonal support argument (subdiagonal block -Q^-1 A invertible). Exact check d=2, k=4, non-scalar proportional sensing, s=1..5: ranks [2,4,6,8,8]; repeated configuration gives 4, not 6. | Specialization (ii) re-derived, not recomputed. |
| C5 | proved | confirmed-with-correction | Under decentralized random schedules containing a chain of single-observation increments: (a) r* >= d + sum q_tau for full-rank H_i, with equality absent other variation; (b) r* = k rank H_i when late evidence spans R^d at every interior step; (c) strict inequality can occur for partial rank. | Reconstructed the rank-r_j Woodbury increment, the induction V_m = W_m and parts (a)-(c). Exact instance of my own with pre-window variation. | Equality in (a) needs no pre-window variation, as stated; the Target summary ('exact closed-form evaluations across all canonical off-schedule regimes') does not carry that condition. d=2, rank H_1=2, rank H_2=1, a=3, k=4: rank 6 over all last-report times, 5 when restricted to {a..b-1}. |
| C6 | proved | confirmed | Steady-state round-robin with heterogeneous full-rank sensing: least dimension (p+1)d, p the number of members with phase <= k-2; (k-1)d when n=k. | Reconstructed the echelon argument. Recomputed from the actual periodic schedule in the second period (a=k): d=1,k=4 phases (1,2,4),(1,3,4),(3,4),(1,2,3,4) give 3,2,1,3; d=2,k=3,n=3 gives 4. | The stored script uses hand-built lists for the first period only. |
| C7 | proved | confirmed | For Q_x=0 with A invertible, d numbers suffice on any schedule; for A=0 with Q_x>0, rank H_i numbers suffice. | Read and re-derived (two lines each); no computation of my own. | Already contained in rem:prv-window-scope for the blind case. |
| R1-R3, O1-O2 | failed routes recorded; obligations complete | status-overstated | Three failed routes; obligations O1 (determine the least dimension) and O2 (fresh-context review) both ticked. | R2's figures 3/7 and 5/13 recomputed by hand; R1 and R3 follow from C2 and C5(c). Looked for the review artifacts cited in the log. | O1 is not fully discharged (see C1(b)). The files cited for O2 (cleaned_writeup.md, explore_prv_aware.py, check_test5_sympy.py, explore_regimes.py) are not in the check folder. |

Script audit. verify_prv_aware.py: two-channel (information form against brute-force covariance conditioning), exact rationals for C3, C4, C6, three working planted-error controls; checks 1, 2, 3, 6 can fail. Gaps: every Bernoulli instance (5A) uses the first window a=0, so pre-window variation is never exercised; round-robin ranks (4A/4B) come from hand-built information lists, not a steady-state schedule. Rerun output identical to stored, line for line (58 lines; stored file is UTF-16). All numbers quoted in the note match the output.

Remaining open:
- Least per-contact message dimension for encoders that may spread a window over several reports, on known schedules with deliveries later than the member's next report (a set of achievable dimension vectors, not one number per window).
- Closed form of r* for partial-rank sensing with pre-window variation (steady-state Bernoulli); whether the C2 upper bound is always attained there.
- Statement for arbitrary encoders in the form of thm:prv-window: 'B_i l_i is a function of the message'.

### Note `open_prv_minimal.md`

Target: open:prv-minimal (ext4_prv.tex:113-115; also prop:prv-clock, thm:prv-tree)

Declared record status: active (one session, 2026-11-21)

Status justified? Yes. The locked statement (least storage of an exact protocol for Q_x=0 on a graph with cycles under arbitrary schedules, as a function of n and the cycle structure, and whether growth with n is necessary) equals the manuscript text. Established: growth with n is necessary on long cycles for continuous protocols (C2); an upper bound by block tables (C1); a qualitative O(1)-against-unbounded dichotomy under two restrictions (C4). Minimal storage is bracketed, not determined: Omega(d max(circ, theta)) against O(d |V(B)|) on a two-connected block, which can be exponentially apart; the bounds agree up to a constant factor on C_n (about dn/4 against dn data-dependent reals), K_n, K_{2,k} and G_k, and by a further factor of order d if a pair is counted as d(d+3)/2 numbers.

| Claim | Declared | Verdict | Statement | Check done | Detail |
|---|---|---|---|---|---|
| C1 | proved | confirmed | Block-cut channel protocol: exact for Q_x=0 under arbitrary schedules, one pair per bridge, sum over two-connected blocks B containing v of (\|V(B)\|-1) extra pairs and \|V(B)\| counters at v. | Reconstructed the three invariants event by event. Re-implemented from the note's text with exact integer multiplicity vectors: 8 graphs including a windmill, two K_4 sharing a vertex with bridge and C_5, Petersen, K_{2,4}; 4 schedules of 1500 events each, exact after every event; three planted errors detected. | Unstated: nodes must know the block of each incident edge and that block's vertex set; a report inside a block carries \|V(B)\| pairs. On a two-connected graph this is prop:prv-clock. |
| C2 | proved | confirmed-with-correction | On a cycle of length l>=6 with rank-d sensing, any exact protocol with continuous node states has adjacent u,v with a_u + a_v >= d(m-1)^2/m, m=floor((l-2)/2); hence Omega(d n) per node on C_n. | Reconstructed the information sets, both causal-independence claims, the grid membership and the four-point difference. Checked independence on full local views (sender updates and global timestamps included) for lengths 6,7,8,9,10,12; control with 2k rounds shows dependence. | Unstated hypotheses that are used: states depend on local history only; link state is touched only by reports over that link (the claim says 'unbounded link storage'); discrete metadata is independent of the data; a_v is the whole state, output included, uniform over schedules. Nontrivial beyond the outputs only for length >= 10. 'Theta(dn) necessary' should read 'at least about dn/4 at one endpoint of every cycle edge'. |
| C3 | proved | defect | With k+1 internally disjoint u-v paths, C^1 protocols satisfy a_v + a_r >= ceil(d k 2^(k-1)/(2^k-1)) > dk/2; hence max a_w > d(theta-1)/4 on any graph with theta >= 3. | Reconstructed the constant-rank and cross-intersection counting argument (correct). Simulated the asynchronous schedule on local views for r != u and r = u, with and without step (2), with and without a clock; tested the lemma on admissible subspace families with an inadmissible control. | When P_{k+1} is the edge uv (r=u), step (2) delivers every item to u, so Psi_T is not a function of x_T (my run: D_u=[k], not T); dropping step (2) makes Phi_S depend on T when a path has length 2. The Menger corollary uses this case. Repair: take P_{k+1} with an internal vertex, k = theta-2, giving max a_w > d(theta-2)/4; theta-1 survives for nonadjacent pairs or when the other paths have length >= 3. |
| C4 | proved | confirmed-with-correction | For two-connected B: diam <= floor(C/2), Delta <= 1+theta^(ceil(C/2)-1), \|V\| <= 1+Delta^floor(C/2). Hence, with bounded block-degree, O(1) storage suffices among C^1 protocols iff block size is bounded. | Reconstructed the three inequalities; verified all three on all 538 two-connected graphs with at most 7 vertices (the stored script never tests the degree inequality). | The 'only if' half inherits C3's class: C^1 and, for paths of length 2, no shared sub-event clock; the statement omits the clock restriction. The block-degree hypothesis is needed for the 'if' half and its necessity is not addressed by the note. |
| C5 | refuted | confirmed | Per-node storage cannot be bounded by a function of feedback vertex number, treewidth, maximum degree or circumference alone. | Checked that G_k uses the clock variant of C3 with gate vertices (sound in my view simulation) and that C_n uses C2; invariants of G_k and C_n read, not recomputed. | 'requires > dk/2' is a bound on a_v + a_u; per node it is > dk/4. |
| R1, R2, O1, O2 | recorded; O1 open, O2 complete | not-verified | Failed routes (invariant-based upper bounds; an O(log n) dyadic protocol on C_n); O1 open (tighten to block size); O2 ticked (fresh-context review). | R1 follows from C2 and C3. R2's assertion of an O(log n) bound for one observation per node was read only. Looked for O2's artifacts. | cleaned_writeup_prv_minimal.md is absent. The figure quoted for the verifier's 'independent' C1 check (6.22e-15, 10 nodes) equals the stored script's barbell_K4 line. |

Script audit. verify_prv_minimal.py: check 1 (protocol against information-form and covariance-form truth, two planted errors) and check 2 (set simulation, leak flags, exact incidence rank) can fail. Check 3 cannot fail on C3's content: it verifies set bookkeeping that holds by construction with a separate relay r, never tests r=u or local transcripts, counts basis vectors it has just built, and its negative control compares the constants 30 and 32. Check 4 does not test the degree inequality. Rerun differs from stored in three Channel B figures (tree_8 1.21e-10 to 2.24e-10, cactus_3tri 9.95e-11 to 9.62e-11, multi_block 2.76e-12 to 1.75e-12), roundoff in an ill-conditioned inverse; all asserts pass. The note's '<= 1.21e-10 (Channel B)' is a figure of one run. Other quoted numbers match.

Remaining open:
- Repair C3 for r=u and restate the constant.
- Note's O1: on two-connected graphs the bracket Omega(d max(circ,theta)) to O(d|V|) can be exponentially wide.
- Lower bound in the shared-clock model when local connectivity is carried by paths of length 2 (K_{2,k}).
- Whether the block-degree hypothesis of C4 is necessary (reviewer's windmill sketch says yes: hub state >= d m; needs an independent check).
- Accounting of a pair as d(d+3)/2 numbers against d data-dependent reals; the constant between dn/4 and dn on cycles.
- Literature check on lower bounds for version vectors and vector clocks before C2 is presented as new.

### Findings

**prv_aware_minimal/M1** (major, mathematical) at open_prv_minimal.md C3, proof lines 137-141 and 153

The asynchronous schedule fails when the last path is the direct edge uv (r = u): step (2) sends every remaining item to u, so the state called Psi_T depends on all of x and the counting argument does not apply. The Menger corollary max a_w > d(theta-1)/4 uses exactly this case.

Evidence: check_minimal.py B3: 'r == u, steps 1-4, no clock: Phi_S indep of T=True, Psi_T indep of S=True, D_v=S=True, D_r=T=False'. Dropping step (2): 'Phi_S indep of T=False', because a length-2 middle vertex has or has not sent to u before sending to v.

Fix: Take P_{k+1} to be a path with an internal vertex and never fire uv: k = theta-2 and max a_w > d(theta-2)/4 (K_n: a_v + a_r > d(n-3)/2). Keep theta-1 for nonadjacent maximizing pairs or when all other paths have length >= 3 (gate vertex). Asymptotics, C4 and C5 are unaffected.

**prv_aware_minimal/M4** (major, mathematical) at open_prv_aware.md C1(b), Target 'Alternative forms', Open obligation O1

r*(E_i), with E_i cut at the member's next report, is a valid per-message lower bound, but the encoder attaining it is exact only until that report. With evidence about a window's interior delivered later, the per-window numbers are not jointly achievable, so the note does not determine the least message dimension of an exact protocol on such schedules.

Evidence: check_aware.py Part 6 (exact rationals, d=1, unit parameters; member 1 reports {1,2,3} at t=3 and {4,5,6} at t=6; member 2's observations at times 1 and 2 arrive at t=7 and t=8): r*(W1 before next report)=1, r*(W1 over all t)=3, r*(W2)=2, rank of all required rows on the six observations = 4. So 1+2=3 < 4 <= 3+2=5.

Fix: Split C1(b) into a lower bound per contact and an exact value for encoders that send each window once (E_i over all later times). Add the cross-window case as an open obligation and remove 'complete exact characterization for arbitrary schedule families'.

**prv_aware_minimal/S1** (major, status-or-scope) at open_prv_aware.md header 'Status: closed'

Closure is justified for the qualitative question and for the regimes with exact formulas, not as a determination of the least message dimension for every asynchronous or random schedule.

Evidence: M4 (3 < 4 <= 5) and M5 (steady-state Bernoulli gives 6 where the first-window formula gives 5).

Fix: Set status to closed with stated scope (single-transmission encoders; schedules whose late deliveries precede the next report; decentralized random schedules) or reopen with the residual obligations listed.

**prv_aware_minimal/S2** (major, status-or-scope) at open_prv_minimal.md C4 statement

The 'only if' half of the dichotomy relies on C3, which for paths of length 2 holds only without a shared sub-event clock; C4 states the C^1 restriction and omits the clock restriction. With a clock, K_{2,k} is covered by neither C2 nor C3.

Evidence: check_minimal.py B3: 'r != u, steps 1-4, CLOCK on: Phi_S indep of T=False'; circ(K_{2,k}) = 4, so C2 gives nothing.

Fix: Add 'without a shared sub-event clock' to C4, or state the clock version only for families whose divergence comes from circumference or from disjoint paths of length >= 3.

**prv_aware_minimal/M5** (minor, mathematical) at open_prv_aware.md C5(a) and Target summary

The closed form d + (k-1) rank H_2 is exact only for the first window or when the other member is known to be current at the window start; in a steady-state Bernoulli schedule the value is larger and is known only through the rank formula.

Evidence: check_aware.py Part 5 (d=2, rank H_1=2, rank H_2=1, a=3, k=4): rank 5 for last-report times in {a..b-1}, rank 6 for {0..b-1}; C2 upper bound 6, blind bound 8.

Fix: State the condition in the Target summary and list the steady-state partial-rank value as open (bracketed by C5(a) and C2).

**prv_aware_minimal/M2** (minor, mathematical) at open_prv_minimal.md C2 and C3 statements

The lower bounds use four hypotheses that are not stated: local causality of node states, link state touched only by reports over that link, discrete metadata independent of the data, and a_v meaning the whole state (output included) bounded uniformly over schedules.

Evidence: C2's last step makes node 0's output a function of sigma_0, the message and the untouched link e*; with link state readable by an endpoint at any event the bound is void. The bound exceeds the 2d reals of the two outputs only when (m-1)^2/m > 2, i.e. cycle length >= 10.

Fix: Put the four hypotheses in the protocol-class sentence of C2 and C3 and state the length-10 threshold.

**prv_aware_minimal/M3** (minor, mathematical) at open_prv_minimal.md C4 (block-degree hypothesis) and O1

Reviewer's sketch, not independently checked: bounded block size alone does not give O(1) storage. On a windmill of m triangles any exact C^1 protocol with state dimensions bounded uniformly over schedules has hub state of dimension at least d m.

Evidence: Leaf b_i observes q times and sends to a_i after each; a_i -> c fires once after the j_i-th send; then b_i -> c. b_i's view is independent of j. Exactness makes the prefix sum Y_i^{j_i} a function of (hub state, b_i state); at a constant-rank point the prefix covector lies in C_j + B_i with dim B_i <= a_b; for q > a_b some j_i gives d independent vectors of C_j inside block i, for every i.

Fix: Have the argument checked by a second reader; if it stands, restate the dichotomy as: O(1) storage iff sup_v sum over two-connected blocks B containing v of (|V(B)|-1) is bounded.

**prv_aware_minimal/S3** (minor, status-or-scope) at open_prv_minimal.md C2 statement; C5 evidence; storage accounting

Quantitative wording is loose: 'Theta(dn) per node' is a bound at one endpoint of each edge; C5's '> dk/2' is a pair sum; the lower bounds count data-dependent reals (d per pair) while the manuscript counts d(d+3)/2 per pair.

Evidence: C2 proves a_0 + a_{k+1} >= d(m-1)^2/m; C3 proves a_v + a_r > dk/2. Against the manuscript's count the bracket on C_n is Omega(dn) to O(d^2 n).

Fix: State bounds as pair sums with the per-node consequence, and say which count of a pair is used.

**prv_aware_minimal/P1** (minor, script) at open_prv_minimal-checks/verify_prv_minimal.py, check_c3_subset_union

No block of the C3 check can fail on the claim's content, and the note describes the partition construction as a 'matching' upper bound although it is k+2 against about k/2 and is a solution of the linear relaxation, not a protocol.

Evidence: Channel A asserts D['v']==S and D['r']==T with a separate relay (true by construction); Channel B asserts max_a <= k//2+1 on lists it just built and never tests 1_{S u T} in L_S + R_T; the negative control asserts 30 < 32.

Fix: Replace with a local-view simulation covering r=u and the clock case, and a test of the lemma on admissible families with an inadmissible control (check_minimal.py B3, B4 do this).

**prv_aware_minimal/P2** (minor, script) at verify_prv_minimal.py check 4; verify_prv_aware.py checks 4A/4B and 5A

The degree inequality of C4 is never tested; the aware script tests Bernoulli and round-robin claims only on the first window.

Evidence: Only 'diam <= circ//2 and b <= bound_v' is asserted. In 5A W1 = range(1, k+1); in 4A/4B the information lists are written by hand for a=0.

Fix: Add the degree inequality (my B5: 538 two-connected graphs up to 7 vertices, 0 violations) and steady-state instances (my Parts 4 and 5).

**prv_aware_minimal/P4** (minor, script) at open_prv_minimal.md C1 Evidence; verify_prv_minimal_stdout.txt

The Channel B error quoted as a bound is not reproduced on rerun.

Evidence: Stored tree_8 err_ChB=1.21e-10; rerun 2.24e-10 (also cactus_3tri 9.95e-11 to 9.62e-11, multi_block 2.76e-12 to 1.75e-12). verify_prv_aware rerun is identical to stored.

Fix: Quote the assert threshold (1e-9) instead of a run-specific maximum, or condition the covariance-form reference better.

**prv_aware_minimal/I1** (major, integration) at sections/ext4_prv.tex:3, 113-119; appext4_prv.tex:224, 290; 10e_open_problems.tex:23, 88; s10b_hierarchy.tex:315

Neither note is cited by any .tex, and the manuscript still presents both problems as fully open. Two sentences will be wrong once results enter: appext4_prv.tex:290 ('every exact scheme for graphs with cycles in this section stores an amount that grows with n or with the diameter') and :224 ('whether growth with n is necessary ... is open').

Evidence: grep for open_prv, block-cut and circumference in sections/ returns nothing; the quoted sentences are at the cited lines.

Fix: Integrate the ready results (see candidates), narrow both open problems to the residuals, and revise the status table and the two sentences together.

**prv_aware_minimal/E1** (minor, editorial) at both notes: Check fields, Review Log, Log

Review provenance cannot be reproduced: the cleaned write-ups, exploration scripts and 'independent' verifier checks cited in the logs are not in the folders.

Evidence: Check folders contain only verify_*.py and its stdout. The 'independent 1,000-event simulation on 10-node 3-block/2-bridge graph (max error 6.22e-15)' matches the stored barbell_K4 line (10 nodes, 2 blocks, 3 bridges, 240 events, 6.22e-15).

Fix: Store the artifacts or mark the Review fields as self-reported.

**prv_aware_minimal/E2** (minor, editorial) at open_prv_minimal.md Searches table

No literature search was made, yet per-source counters are version vectors and size lower bounds for vector clocks are classical; novelty of C2 is undetermined.

Evidence: Searches row: 'none (no novelty claim made)'. The usual citation for the vector-clock size bound is Charron-Bost 1991; not checked against the source by me.

Fix: Read the primary source and compare hypotheses (causality characterization against exact fusion) before integrating C2 as a theorem.

### Collective_Agents touchpoints

| Location | Label | Relation | Detail |
|---|---|---|---|
| sections/ext4_prv.tex:117-119 | open:prv-aware | stale-open-statement | Still asks for the least dimension between d and k rank H_i. The note shows d fails off schedule and gives the per-window rank with three closed forms. Narrow to the cross-window residual; do not delete. |
| sections/ext4_prv.tex:113-115 | open:prv-minimal | not-integrated | 'Whether growth with n is necessary' is answered for long cycles by C2 (continuous protocols); 'least storage as a function of the cycle structure' is bracketed only. Narrow, do not close. |
| sections/ext4_prv.tex:3 | sec:prv opening paragraph | stale-open-statement | Lists both problems as left open without qualification. |
| sections/ext4_prv.tex:37 | text after thm:prv-window | not-integrated | 'Blindness is what it prices: on a common schedule ...' stays true; the complementary fact (off schedule the saving can vanish: C3, C5(b)) is absent. |
| sections/ext4_prv.tex:43 | text after thm:prv-cover | not-integrated | 'No summary of bounded size can be exact on a cycle is false once members carry identifiers' is true for storage bounded in elapsed time; by C2 it must grow with the cycle length under arbitrary schedules. Needs that qualifier once C2 enters. |
| sections/ext4_prv.tex:93-109 | tab:prv-memory | not-integrated | No row for block tables; the 'Model-aware summary' row is right for the common schedule and has no off-schedule counterpart. |
| sections/appext4_prv.tex:123-133 | prop:prv-aware | unaffected | Hypotheses and form equal what the note recovers as C2(i) (one configuration gives at most min(d, k rank H_i)). |
| sections/appext4_prv.tex:120 | rem:prv-window-scope | unaffected | Its A=0 and Q_x=0 cases agree with aware C7. |
| sections/appext4_prv.tex:212-224 | prop:prv-clock and following sentence | stale-open-statement | Line 224: 'Whether growth with n is necessary on graphs with cycles is open:prv-minimal.' The proposition itself is unaffected; block tables reduce to it on a two-connected graph. |
| sections/appext4_prv.tex:290 | rem:prv-memory | not-integrated | 'Every exact scheme for graphs with cycles in this section stores an amount that grows with n or with the diameter' would be false after the block-table scheme is added (bounded on bounded-block families). |
| sections/10e_open_problems.tex:23 | status table row, problem 5 | stale-open-statement | Remaining-open column lists 'least storage on graphs with cycles' and has no entry for off-schedule encoders. |
| sections/10e_open_problems.tex:88 | sec:opn-5 | stale-open-statement | Names open:prv-minimal and open:prv-aware as open. |
| sections/s10b_hierarchy.tex:315 | open:hie-provenance | stale-open-statement | 'with a matching lower bound only for intermittent reports from blind encoders' and 'the least storage on a graph with cycles ... remain open'. |
| sections/chkext4_prv.tex:28, 68 | chk:prv-window, chk:prv-independent | unaffected | Checks of thm:prv-window and prop:prv-aware; consistent with the notes. No check file covers either note. |
| sections/13_discussion.tex:45; 01_introduction.tex:36,162; 02_framework.tex:165,192; 00_abstract.tex; 11_predictions.tex | general mentions of provenance | unaffected | No statement about the two problems; abstract and predictions do not mention provenance. |

### Integration candidates

| Result | Target | Readiness | Why |
|---|---|---|---|
| open_prv_aware C3: on the star with d=1, A=Q_x=P_0=H=R=1, member 1 reporting {1,2} at t=2 and member 2 reporting {1,2,3} at t=3, the hub's required weight vectors (1/4,5/8) and (2/45,7/45) are independent, so no linear or continuous one-number message of member 1 is exact. | appext4_prv.tex, remark or proposition after prop:prv-aware; one sentence at ext4_prv.tex:37 | ready | Exact and two lines long; reproduced by two independent exact computations. |
| open_prv_aware C1: M_{D,t} = Cov(x_t,x_b\|o_D) Phi(D_<b), and a window sent once needs exactly rank of the stacked Phi(U) numbers over the reachable sets U of earlier evidence. | appext4_prv.tex, new proposition after prop:prv-aware | ready-after-minor-fix | Proof reconstructed and checked exactly; must state the single-transmission scope with the evaluation set over all later times, and give the 'function of the message' form used by thm:prv-window. |
| open_prv_aware C5(b): if late evidence of the other members spans R^d at every interior step and its arrival is unknown to the encoder, a model-aware member needs k rank H_i numbers. | remark after thm:prv-window (ext4_prv.tex:37 or appext4_prv.tex after its proof) | ready-after-minor-fix | Shows the blind bound returns off schedule; state the chain hypothesis explicitly. |
| open_prv_aware C4 and C6: min(s,k)d for proportional full-rank sensing with s distinct configurations; (p+1)d for steady-state round-robin. | appext4_prv.tex, propositions or one worked example; optional row in tab:prv-memory | ready-after-minor-fix | Proofs reconstructed, exact instances agree; hypotheses must appear in the statements. Lower priority than C1 and C3. |
| open_prv_aware C2 (four-way upper bound) and C7 (boundary regimes). | C2 as a remark with the C1 proposition; C7 nowhere | ready | C2 is elementary and used by C5, C6. C7 is already in rem:prv-window-scope and is not worth a separate statement. |
| Narrowed open:prv-aware: least per-contact dimension when a window may be spread over several reports and deliveries can be later than the next report; closed form for partial-rank sensing with pre-window variation. | ext4_prv.tex:117-119 and :3; 10e_open_problems.tex:23, 88 | ready-after-minor-fix | Residual identified by the instances 3 < 4 <= 5 and 6 against 5. |
| open_prv_minimal C1: block tables, exact for Q_x=0 under any schedule with sum over two-connected blocks B containing v of (\|V(B)\|-1) extra pairs per node and one pair per bridge. | appext4_prv.tex, proposition after prop:prv-clock; row in tab:prv-memory; revise appext4_prv.tex:290 | ready-after-minor-fix | Invariants reconstructed; independent exact simulation passed; add the topology knowledge and the message size. |
| open_prv_minimal C2: on a cycle of length l>=6 adjacent node states satisfy a_u + a_v >= d(m-1)^2/m, m=floor((l-2)/2), for exact protocols with continuous states. | ext4_prv.tex theorem or appext4_prv.tex proposition; revise ext4_prv.tex:43 and appext4_prv.tex:224 | ready-after-minor-fix | Fully reconstructed; add the four protocol-class hypotheses and do the vector-clock literature check before claiming novelty. |
| open_prv_minimal C3: with k+1 internally disjoint u-v paths, C^1 protocols need a_v + a_r > dk/2. | appext4_prv.tex proposition | needs-repair | The r=u case of the asynchronous schedule is wrong; restate with theta-2 or restrict the case. |
| open_prv_minimal C4 and C5: block-size dichotomy and the failure of bounds by feedback vertex number, treewidth, degree or circumference alone. | remark after the C2 and C3 statements in appext4_prv.tex | ready-after-minor-fix | Graph inequalities verified on 538 graphs; needs the clock restriction, the block-degree hypothesis and the repaired C3. |
| Reviewer's windmill bound: hub state >= d m for exact C^1 protocols with uniformly bounded states on m triangles sharing a vertex. | would remove the block-degree hypothesis from the dichotomy | needs-fresh-proof-check | My derivation only; no second reader. |
| Narrowed open:prv-minimal: constants on cycles; two-connected graphs with small circumference and local connectivity; clock model with short paths. | ext4_prv.tex:113-115; 10e_open_problems.tex:23, 88; s10b_hierarchy.tex:315 | ready-after-minor-fix | Follows from the bracket once C1 and C2 are in. |

### MAgent_Theory_2.0 bearing

One interpretive bearing, none exact. Searched chapters/, companion/, README.md, future_TODO.md and Item_*.tex for provenance, double count, channel filter, Kalman, ledger, asynchronous, common information, message dimension, sufficient statistic, biconnected, circumference, echo, incest, cavity. chapters/18_link_dynamics.tex:203-220 (it2:echo) computes the double counting of a per-agent exchange around one loop factor and shows that removing the recipient's contribution (cavity rule, item iv) restores the exact marginal, noting at line 220 that this is belief propagation on a tree and not an exactness theorem for overlapping loops; chapters/18_link_dynamics.tex:693-694 (it2:open-messages) leaves open what an echo-free protocol must exchange and when. The provenance results say, for a different model, that recipient-removal is exact on trees only and that on a cycle with asynchronous exchange exact fusion needs node memory growing with the cycle length (minimal C2). The correspondence breaks at the variables and the timing: MA couples one dictionary variable per edge through a single factor (a star factor graph, simultaneous fixed point); the notes have one shared state and arbitrary schedules. Nothing in MA is contradicted or sharpened. chapters/17_communication_links.tex:89-101 (it1:kalman) shares only the Gaussian conditioning formula.

### To-do bearing

None on the five workstreams of research_to_do.md. Workstream 1 concerns the code of a single reception and the gauge limit, not de-duplication of repeated receptions; workstreams 2-4 concern the Markov length, timescale separation and distance laws; workstream 5 is categorical. No edit to the to-do file follows from these two notes.

### Checker scripts

Not written: the harness refused the write of 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/prv_aware_minimal/report.md (subagents may not write report files), so the full content is in this structured return. Scripts and outputs of this check: 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/prv_aware_minimal/check_aware.py, 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/prv_aware_minimal/check_aware_output.txt, 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/prv_aware_minimal/check_minimal.py, 2026-11-22-ca-research-notes-check-artifacts/checker-scripts/prv_aware_minimal/check_minimal_output.txt

