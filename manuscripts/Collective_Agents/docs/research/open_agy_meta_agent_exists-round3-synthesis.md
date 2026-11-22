# Round 3 synthesis (2026-11-22)

Produced by the synthesizer agent from eight investigator reports and the attacks; the research record states the adjudicated status.

# Round 3 synthesis: `open:agy-meta-agent-exists`

Round-3 scripts and outputs are in the session scratchpad, `C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round3\`. Below they are cited as `round3/<folder>/<file>`. The scratchpad is not durable; the folders were copied to `open_agy_meta_agent_exists-checks/round3_<folder>/`, so a citation `round3/<folder>/<file>` below resolves to `open_agy_meta_agent_exists-checks/round3_<folder>/<file>`.

## 1. Verdict

**The problem is settled at the computed level (form A), but only conditionally.** Under the record's locked reading and conventions, the audience instance P0 (new claim C15) meets every clause of `def:agy-meta-agent` at grade (r0, α_M, α_I, α_pr, Agency0) = (4.5, 0.071, 0.03, 0.01, 0.99) with n_null = 999. It meets the same grade with α_M = 0.03 if the noise-only stationary law is declared as the initial law of the input-conditional Markov defect.

- **Independent of the flagged readings.** P0 passes under every combination of O2(a), (e) and (f), and under both clause (c) baselines.
- **Attack result.** An independent-code attack reproduced every deciding number of P0. It found no failing clause beyond two undeclared items: the initial law above, and the selector output when the source belongs to no collective.
- **Fallback if P0's own declarations are rejected.** C13 still settles the problem at Agency0 = 0.074 over full policies (0.998 over sensors only). It is independent of (a) and (f), but it depends on O2(j) and on a memory supremum that is not certified.
- **What the flagged readings now decide.** O2(a), (e) and (f) no longer decide existence. They decide only the grades of C11 and C13.

**What the problem is not settled against.** Every construction rests on two readings that round 3 found decisive:

- **O2(h): relayed sensing noise.** The record's convention is that an agent's own sensing noise stays a private input when it is relayed. Conditioning on it instead gives r(A) = 1.000000 in P0 and 1.003 in C13, and C11's coupling needs the convention (R2).
- **O2(g): partner randomization redrawn every round.** The drawn-once variant fails or is undefined in every construction computed.

Further dependencies:

- **O2(i), for constructions without acts.** P0, C13, C14, and C11 unless opening a public slot is an act, also need the agency index to apply to a model whose only policies are attention sets.
- **O2(n), P0 only.** P0 needs a selector output that leaves the non-member source in no block.
- **O2(m), P0 only.** P0's members do not interact with one another: Ω_int(A|ζ_S) vanishes except on events of probability 2×10⁻¹⁴ per member-round. `05_agency.tex:380` asks only that this be reported.

**Grade frontier.** Each entry is the largest Agency0 at which every other clause holds at the construction's stated (r0, α_M, α_I, α_pr):

| Construction | (r0, α_M, α_I, α_pr) |
|---|---|
| C11 = I* | (3.5, 0.02, 0.09, 0.01) |
| C13 = I** | (7.9, 0.02, 0.09, 0.01) |
| C14 = D1 | (3.7, 0.02, 0.03, 0.01) |
| C15 = P0 | (4.5, 0.071, 0.03, 0.01) |
| C18 = CCP | (3.75, 0.02, 0.05, 0.01) |

| Readings | Best construction | Largest Agency0 | Status | Review |
|---|---|---|---|---|
| (a) any; (e) slot/act; (f) frozen (P4); clause (c) mechanism | C15 (also C11, C13) | P0 1−O(10⁻¹³), stated 0.99; C11 1−10⁻¹⁰ (needs (a2) or slot not an act); C13 0.998 (G1) | computed | fresh-context |
| as above, clause (c) mean coupling | C15 | P0, C13 unchanged (4.5 > 3.817; 7.9 > 7.37); C11 unchanged at r0 = 4.15, window (3.94, 4.43] | computed; C11's neighborhood by C19 | fresh-context |
| (a) any; (e) slot/act; (f) real time | C15 | P0, C13 unchanged (no deliberation chain); C11 0.99988 (G1) or 0.971 (G2) at the coarse decision state, 0.30–0.978 (G1) and 0.10–0.69 (G2) at finer declared states | computed | fresh-context |
| (a) any; (e) full policies; (f) either | C15 (P0, P1) | P0 1−O(10⁻¹³); P1 0.9967; C13 0.0748 (pinned slot preferences), 0.537 with outsider relays as slots carrying a free cost; C14 0.80 (needs R-outsider and padding); C11 0.0080 real time, ≈0.0074 frozen | computed (C11 frozen: hand arithmetic, not run) | fresh-context; P1 main quantities only |
| (a) opening a slot is an act, and strict typing | C15 | P0, C13, C14 unchanged (no acts, proved); C11 fails the differ clause (N_eff 4.41, N_inf 6.27 above the edge 2.94) | computed | fresh-context |
| clause (b): fixed schedule declared as an interaction graph (O2(c)) | C15 | P0 unchanged (the graph holds all 10 positively coupled pairs, so (b) equals mean coupling); C11, C13, C14 keep clause (c) (attention selected by expected free energy); C18 fails by I1 | interpretive | attack on C15 |
| O2(i): the index applies only to acts | C11 (opening a public slot read as an act, with (a2)) | C11 1−10⁻¹⁰; C9 0.94 (round 1, its own readings); C18 0.265 under strict typing (end-of-round belief; 0.128 start-of-round), needing O2(o) and clause (c); C13, C14, P0 lose the agency clause; nothing under (i) with strict typing and (b) | computed | fresh-context |
| O2(h) rejected | none | none established; C18 keeps a window (1.0039, 1.0058] with N_eff 1.0000, other clauses not computed | computed | fresh-context |
| O2(g): drawn-once N_pr also required | none | none established: C14 P(S ≥ S0) = 1/9 exactly; C18 17/81; P0 202/256 draws non-diffusive, substitute selector not computed; R3 p = 1; C11, C13, P1 not computed | computed | fresh-context |

Notes:
1. The slot-only values of C11 and C13 exclude attention to the other niche's relays. Under the literal η_C (`05_agency.tex:11`) those relays are slots, and neither index has been computed with them (O2(j), O8).
2. In C13, C14 and P0, each member's expected free energy ignores its co-members' simultaneous choices (proved). So (P4) at a frozen state and the per-round draws of `def:fw-system` give the same law, and (f) bears only on C11. Neither of C11's protocols is the literal per-round law: T-real redraws one member's slot per round, which the attack on C13 (its 3d) rules non-literal. The literal law's index is not computed (O8).
3. G2 is inadmissible under a scalar coarse variable (attack on C13, 3c; the same argument applies to C11). So G1, with a free constant belief variance, governs; G2 values are shown only for comparison.

## 2. Recommended readings

These come from the readings investigator. All are interpretive, and each confidence is that investigator's estimate of the author's intent.

- **(a2) N_eff and N_inf are typed as the table words them.** Confidence 0.8.
  - Quote: "D for collectives said to form by joint action" (`05_agency.tex:348`) and "D for collectives said to form by communication through acts" (`:349`). Every other row is typed unconditionally.
  - The literature agrees: a null removes the mechanism under test (Gotelli and Graves 1996, secondary).
  - Consequences: C11 passes, C8's premise fails for relay-formed collectives, and R5 is not decisive.
  - Amendment: "otherwise a diagnostic", with what the collective is said to form by declared with the grade.
- **(a1) Opening a public slot is not a performative act.** Confidence 0.55.
  - Quotes: the four active components of `def:fw-system` (`02_framework.tex:13`); "an intervention" versus "an epistemic slot choice" (`s05_agency.tex:147`).
  - The literature investigator disagrees and reads it as an act (Kirsh and Maglio 1994; Constant et al. 2018).
  - Moot under (a2), and moot for private sensors, which are attention to "world channels" (`02_framework.tex:13`).
- **(b) An index of one reached by habit does not count.** Confidence 0.85.
  - Quote: "agency holds only because the members act by habit" (`s05_agency.tex:296`).
  - Amendment: require Σ_X w_X KL(P(·|X)‖E) > 0. No construction relies on it.
- **(c) Fixed or scheduled attention is declared as an interaction graph.** Confidence 0.6.
  - Quote: "a model whose declared couplings contain a partition cannot claim to have found it" (`s04_collectives.tex:147`).
  - Only C18 is affected, and it fails under this reading.
- **(d) Filtered errors are admissible when declared (0.7); episodic worlds are outside the class (0.65).**
  - Quotes: "the prior error unless stated" (`appA_notation.tex:67`); "jointly stationary" (`04_collectives.tex:131`).
  - Consequence: C2 does not settle the problem.
- **(e) The index's joint policies are the exterior-facing components (slots and interventions); attention to members' own channels is protocol.** Confidence 0.75.
  - Quotes: "slots, exterior-facing sensory channels that a policy can open" (`05_agency.tex:157`); "the model has no acts, so (H-act), the agency index, N_eff and N_inf are inapplicable" (`ext2_rfm.tex:139`).
  - Literature on boundary outputs supports it (Waade et al. 2025; Jørgensen et al. 2026; Biehl and Virgo 2023). Against it: `02_framework.tex:17` and Sandved-Smith et al. 2021.
  - Round 3 adds two qualifications. The same ext2_rfm sentence can be read as making the index inapplicable to every attention-only model (O2(i)). And the literal η_C makes attention to a non-member's relay a slot (O2(j)).
- **(f) (P4) at a frozen decision state is admissible alongside one-round latency.** Confidence 0.8.
  - Quotes: "The deliberation protocol, at a decision state held fixed while the members deliberate" (`05_agency.tex:161`). The two-firm model "is declared at a decision state and is not the act rule of the dynamics" (`s10a_meta_agents.tex:143`) and still counts (`s05_agency.tex:267`).
  - Literature: the Gibbs law needs one-at-a-time revision on a fixed game (Blume 1993 §6.1). No such law is known when the state moves with play (Liu, Wang and Cheng, Thm 21).
- **Agency0: any positive declared value settles the problem as worded.** Confidence 0.85. Quote: "r_0>1 and Agency_0>0" (`s05_agency.tex:296`).
- **(g), proposed: must the drawn-once N_pr also be passed?** No confidence given.
  - Quotes: "once or every round" (`05_agency.tex:350`); "not covered" (`ext2_rfm.tex:140`).
  - The attack on C15 adds that every-round redraws keep the table's "participation ratio" only when it is read per round.
- **"Each constant of the selector"** means each r0 in the admissible window. Read over all constants, the clause fails for every population, because above r(C) the model and the null both select nothing (attack on C13).

Readings raised by the attacks, with no recommendation; the textual notes are mine:
- **(h)** Relayed own sensing noise treated as private.
  - For: sensing noise is a private input (`05_agency.tex:297`), and "the sender-side noise of a broadcast belongs to the active channel" (`04_collectives.tex:15`).
  - Against: "so that the remaining local noise is specific to each receiver" (`04_collectives.tex:131`), which is false in every construction.
- **(i)** Whether the index applies to attention-only models. For: `def:agy-group-model` is built on epistemic slots (`s05_agency.tex:144`). Against: `ext2_rfm.tex:139,167`.
- **(j)** The literal η_C, which includes "the active channels of non-members that they hear" (`05_agency.tex:11`).
  - Slot preferences are the controlling member's (`:161`).
  - Nothing fixes q_C on non-member content.
  - "likelihoods that every belief shares" (`:157`) fails where members ignore that content.
- **(k)** Padding. The index explains "departure from their habits" (`05_agency.tex:238`), "not efficacy" (`:251`). Read literally, costly components that are never used still count.
- **(l)** The memory clause.
  - The input-conditional form needs "a Gaussian initial law and a blanket input path that is known, deterministic or independent of (x_0, 𝔫)" (`05_agency.tex:20`).
  - Its value depends on that law (P0: 0.0257 to 0.0709).
  - `eq:agy-interior` assumes constant (A, B, Q^n).
- **(m)** Ω_int(C|ζ_{V\C}) > 0 is "the separate statement ... reported with the grade" (`05_agency.tex:380`), though `:294` motivates requiring it.
- **(n)** "a partition at level r0 is one whose blocks are all collectives" (`04_collectives.tex:219`) has no instance when an agent is in no collective.
- **(o)** Vector errors enter contrast only as Σ^sc ⊗ I_K (`04_collectives.tex:187`).
- **(p)** Clause (c)'s "exchangeable population" (`04_collectives.tex:202`) is undefined for distinct agent types. Moot under mean coupling.
- **(q)** q_C is "declared as a function of the collective's coarse state" (`05_agency.tex:157`). This excludes G2, and read at the start of the round it lowers C18 to 0.128.

## 3. Claim updates

### C13: Private-sensor niche under the strictest agency readings (instance I**)

- Statement:
  - Instance I** is C11's architecture with each public slot replaced by a private optional sensor (Rs = 2), read by its owner and relayed raw with one-round latency to every agent that attends the owner. Message attention is over sets of at most 3 of 7 relays, κ = 5. Slot cost ψ = 0.030; γ = 400; uniform product habits; structural speech.
  - Niche A is a meta-agent of grade (7.9, 0.02, 0.09, 0.01, 0.074), n_null = 999, under the per-round protocol. That protocol is the literal law of `def:fw-system` and here equals (P4) at a frozen state.
  - This uses the index over full policies, uniform habits fixed, class G1, and either clause (c) baseline. Over sensors only, the index is 0.998.
  - O2(a) and (f) are moot: there are no acts, and the law is a product law (proved).
- Status: computed
- Review: fresh-context
- Evidence:
  - r(A) 8.4207 ± 0.0031 (attack 8.4287 ± 0.0031); mechanism medium 6.006; mean coupling 7.361; other regions ≤ 2.30.
  - N_hab 2.383; annealed N_pr 2.844, test maximum 3.230 in 999 draws, p = 0.001; N_lp and N_fr diagonal (proved).
  - Inference 0.0594; exact Markov defect ≤ 0.0162 on every pattern searched; index 0.0748 full, 0.9979 sensors only.
  - Files: `round3/strict-construction/` (`lib3.py`, `instance3.py`, `d1_frozen_out.txt`, `d3_frozen_out.txt`, `d4_frozen_out.txt`, `d5_out.txt`, `d6_frozen_out.txt`); attack `round3/attack-strict-construction/` (`a1_frozen_out.txt` to `a3_frozen_out.txt`, `a5b_out.txt` to `a5h_out.txt`, `a6_out.txt`, `a7_frozen_out.txt`).
- Scope: one instance; exact second moments per pair of policy paths over 160 pairs; ±1% box over 8 parameters at 18 points; memory supremum by search only.
- Check: 2026-11-21. The attack, with independent code, reproduced every deciding number; the claim survives. Corrections:
  - The supremum of the exact defect lies in [0.0162, 0.0988], so α_M = 0.02 is consistent but not certified. The candidate's 0.11 came from d_cl.
  - G2 is inadmissible.
  - The 1/7 cap needs pinned slot preferences and a zero-variance belief on outsider content. Treating outsider relays as slots with a free cost gives 0.537.
  - The candidate's real-time protocol is not `def:fw-system`.
  - N_fg is not reported, and drawn-once N_pr is not computed.
- Depends on: C1, C12, O2(h) (fresh-relay control r = 1.003), O2(g), O2(i), O2(j)

### C14: Padding raises the full-policy index (design D1)

- Statement:
  - (Proposition P) With habits fixed and G_C depending on slots only, Agency = (KL_{s|a} − mis_s)/(KL_a + KL_{s|a}), where mis_s is the slot misfit. So components whose departure from habits the class explains drive the index to 1 at fixed KL_a.
  - (D1) Two niches of two agents (F = 0.9, Q = 0.05, R = 1, Rc = 0.1), message capacity 1 over {∅, mate, o1, o2}, eight private slots per member (Rs = 10, cost 0.06702, never opened), γ = 400.
  - Niche A meets every clause at (3.7, 0.02, 0.03, 0.01, 0.75), with full index 0.8000, provided three things hold: attention to non-members' relays counts as internal (R-outsider), or the group variance on their content is at most 1.2×10⁻³; costly components that are never used count; and N_pr is redrawn every round.
- Status: proved (Proposition P); computed (D1)
- Review: fresh-context
- Evidence:
  - r(A) 4.345220, mechanism medium 2.493156, mean coupling 3.230.
  - N_hab 1.346, N_pr 1.761, test p = 0.001; d_M 4.4×10⁻⁵; inference 0.0187.
  - KL_a = 2 ln 4, KL_{s|a} = 16 ln 2; ±5% box 17/17.
  - Files: `round3/agency-frontier/` (`flib.py`, `d1_contrast_out.txt`, `d1_npr_test_out.txt`, `d1_closure_out.txt`, `d1_agency_out.txt`, `d1_box_r37_out.txt`); attack `round3/attack-agency-frontier/a1_out.txt` to `a10_out.txt`.
- Scope: one instance, exact Lyapunov algebra.
- Check: 2026-11-21. The attack recomputed every deciding number.
  - Under the literal η_C, with group variance ≥ 0.5 on outsider content (≥ 0.2 under G2), the index is exactly 0.
  - Drawn-once N_pr fails exactly: P(S ≥ S0) = 1/9.
  - Theorem A (an attention-surprise floor from N_hab) holds only for n = 2 with symmetric habits, given a numerically monotone ρ. Its π* table omits the slots (D1's own π* is 0.880).
  - D5 (Rs = 1, habits concentrated on the mate) keeps N_hab at 1.247 by slot flooding and reaches index 0.99995. Only N_hab, memory and the index were computed for D5.
- Depends on: C12, C16, O2(j), O2(k), O2(g), O2(h)

### C15: Audience meta-agent formed through a non-member source (P0, P1)

- Statement:
  - Instance P0: one AR(1) component, F = 0.9, Q = 0.05. A non-member source S has its own sensor (R_S = 0.01) and attends nothing. Four audience members have R = 1. Every agent broadcasts its raw reading with one-round latency and receiver-specific Rc = 0.002. Each member draws one of {∅, {S}, {m1}, {m2}, {m3}} by expected free energy, with uniform habits and γ = 40. Filters on (η_t, η_{t−1}) are exact, qc = 10⁻⁴.
  - The audience A is a meta-agent of grade (4.5, 0.071, 0.03, 0.01, 0.99), n_null = 999. It is a meta-agent of grade (4.5, 0.03, 0.03, 0.01, 0.99) when the noise-only stationary law is the declared initial law of the memory clause.
  - Both grades hold under every combination of O2(a), (e) and (f), and under either clause (c) baseline.
  - P1 (message capacity 2) passes at (4.45, 0.03, 0.03, 0.01, 0.99), with Ω_int(A|ζ_S) > 0.
- Status: computed; closed form proved
- Review: fresh-context (P1: main quantities only)
- Evidence:
  - Proposition A (re-derived by the attack): r(A) = 1 − c/σ + nβ′/α with β′ = β − c²/σ, giving 5.384864. The best other region, A ∪ {S}, has 2.326.
  - Mean coupling 3.8167; mechanism media ≤ 3.9301.
  - N_hab 1.456; N_pr 1.541, test p = 0.002. N_lp, N_rn and N_fr are diagonal, and N_eff, N_inf and N_ex are inapplicable (proved).
  - Inference 0.02509. d_M is 0.025717, 0.037477 and 0.070909 for the noise-only stationary law, a deterministic start, and the members' stationary law respectively.
  - Index 1 − O(10⁻¹³); all 128 corners of a ±5% 2⁷ design pass every exact clause.
  - Files: `round3/audience/` (`aud.py`, `check1_out.txt` to `check9_test_out.txt`); attack `round3/attack-audience/` (`a1_out.txt`, `a4_out.txt` to `a9b_out.txt`).
- Scope: exact Lyapunov algebra for P0; nulls by pair algebra over 200 policy-path pairs; P1 by Monte Carlo.
- Check: 2026-11-21. The attack rebuilt P0 from its specification; it survives numerically.
  - The stated α_M = 0.03 needs the initial law declared.
  - S is in no collective, so no partition at level r0 exists.
  - Members interact only through S, and P1's links add no contrast (5.375 against 5.3849).
  - Conditioning on v_S gives r = 1.000000.
- Depends on: C1, C16, O2(h), O2(g), O2(i), O2(m), O2(n), O2(p)

### C16: Index of a deterministic joint policy

- Statement: Fix habits E and the belief, take γ_C ≥ 0, and let the actual law be δ_{π*}. Then f(γ_C) = ln P_g(π*) is concave with f′ = E_{P_g}[G_C] − G_C(π*).
  - (a) If π* uniquely minimizes G_C, the index tends to 1.
  - (b) If G_C(π*) ≥ E_E[G_C], the index is 0.
  - Under the literal η_C, case (b) covers members who avoid exterior channels whose content their own models ignore, when the group belief on that content has calibrated variance.
- Status: proved; instances computed
- Review: fresh-context
- Evidence: two-niche audience variant, index 0.0000 (`round3/audience/check12_out.txt`); D1, index 0 for outsider variance ≥ 0.5 (`round3/attack-agency-frontier/a4_out.txt`).
- Check: 2026-11-21. The attack on C15 re-derived f′ and f″ and agrees.
- Depends on: none

### C17: N_eff separates only explaining-away structure (Lemma M, Theorem O)

- Statement:
  - (Lemma M) N_eff keeps the members' act feedback and removes only what the world path tells about their private inputs: Σ^c_eff − Σ^c = S Cov(E[z_0|ỹ]) S^⊤ ⪰ 0.
  - (Theorem O) Let C (n ≥ 2, scalar coordinates) be uncorrelated with V\C and exchangeable under N_eff, with act loadings of disagreement rank below n − 1. Then either Π^c is not diffusive or r(C) ≤ r_eff(C), so C never differs from N_eff.
  - (Proposition E) Acts consistent with expected free energy under a common preference load all members' errors about one component with one sign.
  - (Proposition D) A null that keeps the acts gives uncorrelated interchangeable members with nonzero loadings Σ^c_ij < 0, so the null is not diffusive.
- Status: proved
- Review: self; fresh-context numerical test
- Evidence: `round3/performative-strict/check0_out.txt`, `check1_out.txt`, `check9_out.txt`; attack `round3/attack-performative-strict/a6_out.txt`.
- Scope: n = 2 with same-sign unequal loadings lies outside the theorem. It shows 0 gains in 280 and in 228 diffusive draws (conjecture).
- Check: 2026-11-21. The attack found no violation in 445 diffusive draws with n = 3, 4. The n = 2 mixed-sign control detects gains up to 16.8×. Lemma M holds on C18.
- Depends on: C1, C4, C7. C8 is the special case of setting P.

### C18: Correlated-component pair, a performative meta-agent under strict typing

- Statement:
  - Two firms with independent worlds. In each, member b senses η^a and member s senses η^b (AR(1), F = 0.9, Q = 0.05, innovation correlation 0.5, R = 1).
  - Both members model (η^a, η^b), read each other's raw reading (Rc = 0.1), and act by rule D2 on a renewed outcome η^Z_{t+1} = η^a_t − η^b_t + u_b + u_s + w^Z under a common preference (γ = 70, habits N(0, 1/30), act noise 0.01, κ = 0.7). Attention is fixed.
  - Contrast coordinate: each member's prior error on its own component; baseline: clause (c) mean coupling. Each firm is then a meta-agent of grade (3.75, 0.02, 0.05, 0.01, 0.25), with N_eff and N_inf of type D.
  - This holds with the group belief taken from the end-of-round coarse state (index 0.265). From the start-of-round state the index is 0.128.
- Status: computed
- Review: fresh-context
- Evidence:
  - r(pair) 4.3336, baseline 3.2224; N_eff = N_hab 1.809; N_lp, N_rn and N_fr ≤ 1.852 under every convention computed.
  - Annealed N_pr 2.049, test maximum 2.539 in 999 draws, p = 0.001; d_M ≤ 1.5×10⁻⁴; α_I 0.0317.
  - Files: `round3/performative-strict/` (`lgx2.py`, `check14_out.txt`, `check16_out.txt`); attack `round3/attack-performative-strict/a1_out.txt` to `a8_out.txt`.
- Scope: exact window conditioning. A 64-point ±1% Latin hypercube shares the window (3.3212, 4.1893]; there is no common level at ±5%.
- Check: 2026-11-21. The attack finds it survives under the candidate's readings, with margin 0.015. However:
  - Common coordinates fail (R8).
  - Drawn-once N_pr fails (17/81).
  - Read literally, `04_collectives.tex:187` leaves contrast undefined here, because the agent blocks deviate from a multiple of I₂ by 0.0237.
  - The prior-corrected log pool fails α_I (0.120).
- Depends on: C17, rule D2, the continuous-act extension of the index, O2(c), O2(o), O2(q), O2(g), O2(h) (window (1.0039, 1.0058] without it)

### C19: Continuity of I*'s stationary policy–covariance law (O6)

- Statement: Take the I* architecture with θ = (F, Q, R, Rc, Rs, ψ, γ, qc) in an open set with F < 1 and 0 ≤ γ < ∞, under T-fast and T-real, together with its mechanism medium and the nulls N_hab, N_pr (every round), N_lp = N_rn and N_fr. Then:
  - The chain (policy, Kalman covariance) has a unique stationary law. It is reached geometrically in a Wasserstein distance and is continuous in θ with modulus O(ω log(1/ω)).
  - Σ^c(θ) is continuous, Σ^c ⪰ qc·I, and Σ^c = blockdiag(αI₄ + β11^⊤, αI₄ + β11^⊤) exactly.
  - r(A), both clause (c) baselines, every null contrast, and the index at fixed declared decision states are continuous. So the sets on which the differ clause holds are open.
- Status: proved. That θ* lies inside these sets is numerical (smallest margin 77 SE).
- Review: self
- Evidence: Doeblin minorization on the finite policy component; Riccati contraction g′ ≤ (F/(1 + Q′/R))² = 0.7346; rank-one closed loop with factor ≤ 0.857. Files: `round3/continuity/check_a_out.txt`, `check_b_out.txt`, `check_c2_out.txt`, `check_c3_out.txt`.
- Scope:
  - I* only; uniqueness fails at γ = ∞.
  - Continuity of the index is not shown for quantile or event decision states.
  - N_fr under T-real needs a non-diffusive null to select nothing.
- Depends on: C1, C11

### Changes to existing claims

| Claim | Change | Why |
|---|---|---|
| C3a | Review → fresh-context. The parenthetical becomes "independent ancestries: no reads between them, directly or through chains, and no common ancestor". | One common source gives a positive contracted covariance in 105/200 draws. |
| C3b | Review → fresh-context. The "independent a priori" step holds for the η-free parts. With prediction noise, the rule survives when c₀,ₖ > 0 and φ₁φ₂ > 0 (proved). The remark that such noise changes only diag(V) is refuted (`round3/proofcheck-o3/c3b_noise_formula_out.txt`). The corollary assumes continuous Gaussian habits. | The rule fails in 57/300 draws, all with φ₁φ₂ < 0. |
| C3c | Review → fresh-context. Restrict to the marginal precision of the actors' and ancestors' coordinates, or forbid outside readers. | An outside listener gives a rank-two cross block, negative in 16/100 draws. |
| C4 | Review → fresh-context. Z1 to Z4 hold for every positive definite Z-matrix. | The row-sum hypothesis is unused, and C3a and C5(b) need this form. |
| C5 | Review → fresh-context. F-share needs G ≥ 0 or one-signed source columns; Theorem F(c)'s "iff" needs every factor loaded. | A mixed-sign G gives a diffusive precision with non-transitive sharing. |
| C12 | Review → fresh-context. The second part becomes KL_{s\|a} ≤ Σ_i max_{s_i} ln(1/E^s_i(s_i)), with a nonzero denominator. Add (literature investigator, proved): index/bound = 1 − (I + R)/(I + K) ≤ 1 − R/K, the slot-marginal index, with equality iff I(s; a) = 0. | Non-uniform slot habits give index 0.9525 while ln 2 < 4.14; C11 is unaffected. |
| C8 | Generalized beyond setting P by C17. | Theorem O. |
| C11 | Status unchanged. O6 is discharged by C19. Mean coupling admits r0 = 4.15 on a C19 neighborhood. Quote G1: 0.99988 (coarse state), 0.978 (median p-bin), 0.91 (p-bin and count), 0.30 (three p-bins). New dependencies O2(h) and (i). Not computed under (j), (l), drawn-once N_pr (p = 1 conjectured, as in R3), or the literal per-round law. | Round-3 continuity proof and attacks. |
| C2, C9 | Unchanged. C2 is excluded by recommended reading (d). C9's typing premise is the recommended (a2), and C9 has acts, so it survives O2(i). | Readings. |

## 4. Failed routes

### R7: Private sensors at C11's slot cost
- Tried: I** at ψ = 0.024.
- Failed because: the mechanism medium (8.16) exceeds r(A) (7.82) (`round3/strict-construction/d8_out.txt`).
- Reopen if: never; ψ = 0.030 passes (C13).

### R8: Common contrast coordinates for the correlated-component pair
- Tried: one shared direction of (η^a, η^b) for both members.
- Failed because: every direction either puts N_eff inside the window or empties the window. At 45°, N_eff 5.2605 lies in (4.5763, 6.3644] (`round3/attack-performative-strict/a1_out.txt`).
- Reopen if: O2(o) admits member-specific coordinates.

### R9: Opposite-preference pairs
- Tried: pairs acting on one component with opposite preference maps.
- Failed because: all nulls differ, but the index is 0 in three fixed-habit classes (`round3/performative-strict/check12_out.txt`; not attacked).
- Reopen if: classes without fixed habits are admitted.

### R10: Two-department firm
- Tried: two departments of two per firm with opposite outcome loadings.
- Failed because: its deletion nulls and annealed N_pr are non-diffusive (Proposition D). It passes only if such a null selects nothing, which R3 rejects (`round3/performative-strict/check4_out.txt`; not attacked).
- Reopen if: `open:col-non-diffusive` supplies a selector.

### R11: Pure-collider pair
- Tried: two single-agent departments without channels, acting on one outcome.
- Failed because: N_pr leaves the model unchanged, so no level α_pr can be stated, while the open problem asks for "partner randomization at a stated level". Also Ω_int(C|ζ_{V\C}) = 0 (attack, interpretive).
- Reopen if: the author rules that an inapplicable N_pr imposes no requirement.

### R12: Several ignored exterior options under the literal η_C
- Tried: members able to attend several non-member channels (D1's outsiders; a two-niche audience).
- Failed because: a calibrated group belief makes the group's expected free energy prefer the channels the members avoid, so the index is 0 (C16).
- Reopen if: O2(j) admits a zero-variance group belief, free slot preferences, or outsider relays as internal attention.

### R13: Drawn-once partner randomization in small populations
- Tried: drawn-once N_pr on C14, C15 and C18.
- Failed because: when the full attention pattern is itself a possible draw, P(S ≥ S0) is bounded below (C14: 1/9; C18: 17/81). Otherwise the draws are non-diffusive (P0: 202/256). Files: `round3/attack-agency-frontier/a5_out.txt`, `round3/attack-performative-strict/a7_out.txt`, `round3/audience/check11_out.txt`.
- Reopen if: populations grow (about 25 firms for C18, attack estimate).

### R14: Random-coefficient Riccati contraction for O6
- Tried: Bougerol (1993).
- Failed because: it needs nonsingular, exogenous coefficients. In I*, A_F is singular and the policies are fed back. C19 uses direct coupling instead.
- Reopen if: never for I*.

### R15: Certifying memory by the closure defect
- Tried: bounding d_M by the per-step d_cl.
- Failed because: d_cl overstates d_M by orders of magnitude. At I**'s worst pattern it is 2.66×10⁻² against an exact 2.4×10⁻⁵; for flooding at Rs = 1 it is 0.2017 against 4.78×10⁻³. Files: `round3/attack-strict-construction/a5_out.txt`, `round3/attack-agency-frontier/a9_out.txt`.
- Reopen if: never; compute the exact defect.

### R16: Deterministic best response in I*
- Tried: γ = ∞.
- Failed because: the one-slot profiles are absorbing and the stationary law is not unique (0/50 couplings, `round3/continuity/check_b_out.txt`).
- Reopen if: never; keep γ finite.

## 5. Open obligations (smallest first)

- [ ] O2 (sessions: 3; the author's rulings): (a) to (f) with Section 2's recommendations, and (g) to (q) of Section 2. (g) and (h) decide existence; (i) decides every construction without acts; (m) and (n) decide C15.
- [ ] O3 (sessions: 2): fresh-context checks of C6 and C10.
- [ ] O7 (sessions: 1): compute the input-conditional Markov defect of C11, C13, C14 and P1 under three initial laws: the noise-only stationary law, a deterministic start, and the members' stationary law. Certify C13's supremum, now in [0.0162, 0.0988], by interval arithmetic.
- [ ] O8 (sessions: 1): compute the indexes of C11 and C13 with the other niche's relays as slots, under pinned preferences (with zero-variance and with calibrated beliefs) and under free preferences. Compute C11 under the literal per-round law.
- [ ] O9 (sessions: 1):
  - drawn-once N_pr for C11, C13 and P1, and the substitute selector on P0's non-diffusive draws;
  - N_fg for C13;
  - independent recomputation of P0's media M-F, M-S and M-sym, and of P1's medium (4.112) and box.
- [ ] O10 (sessions: 1): verify (H1) to (H6) of C19 for C13, C15 and C18; obtain rigorous enclosures of C11's center values.
- [ ] O11 (sessions: 1): if O2(k) excludes padding, compute the frontier with used, relayed slots. Close Theorem A's step 3 for asymmetric habits, and prove H_mon for n ≥ 3.
- [ ] O12 (sessions: 1): build a C18 population of about 25 firms for drawn-once N_pr, and heterogeneous firms to escape clause (b).
- [ ] O4 (sessions: 1): extend C3a to stored acts and to act loadings of rank above one.
- [x] O5 (sessions: 3): discharged by C13 (full-policy 0.074) and C15 (1 − O(10⁻¹³)).
- [x] O6 (sessions: 3): discharged for C11 by C19; other constructions are in O10.

## 6. Literature

All read 2026-11-21.

| Claim | Source | Locator | Read depth | Verdict |
|---|---|---|---|---|
| The index's numerator equals maximum entropy goal-directedness | MacDermott, Fox, Belardinelli, Everitt, NeurIPS 2024, arXiv:2412.04758 | Def. 3.2, Props. 3.2–3.3, §7 | pp. 1–10 | closest prior art, uncited; MEG ignores irrelevant decisions, while the normalized index dilutes (C12) |
| KL fraction explained, nondecreasing in regressors | Cameron and Windmeijer, J. Econometrics 77 (1997), doi:10.1016/S0304-4076(96)01818-0 | eq. (5), Props. 1–2 | preprint, parts | precedent for the index's form |
| Rescaling by the attainable maximum | Nagelkerke, Biometrika 78 (1991), doi:10.1093/biomet/78.3.691 | eq. (3) | full | precedent for correcting C12's dilution |
| Gibbs law of asynchronous logit revision | Blume, Games Econ. Behav. 5 (1993), doi:10.1006/game.1993.1023 | §6.1, pp. 408–409 | page images | primary locator for `05_agency.tex:208`; supports (f) |
| The Gibbs form is specific to the revision protocol | Alós-Ferrer and Netzer, Games Econ. Behav. 68 (2010), doi:10.1016/j.geb.2009.08.004 | Prop. 1, Thms 1–2 | working paper, parts | other protocols give only stochastic stability |
| State-based games | Liu, Wang, Cheng, arXiv:1608.00192 | Defs. 18–20, Thm 21 | parts | no group-posterior law under real-time deliberation |
| The group agent's blanket is its members' sensory and active states | Waade et al., Entropy 27 (2025), doi:10.3390/e27020143 | §2.3 | pp. 5–10 | supports (e) |
| The collective decision is the actor's action, with the critic marginalized | Jørgensen, Weichwald, Hammond, CLeaR 2026, arXiv:2605.00248 | §4.3, Prop. 17 | §4.3 | supports (e) |
| The output map is the action | Biehl and Virgo, IWAI 2022, arXiv:2209.01619 | Defs. 2–3, 5 | pp. 1–8 | supports (e) |
| Behavior is action on the environment; conditioning on interventions | Bertschinger, Olbrich, Ay, Jost, BioSystems 91 (2008), doi:10.1016/j.biosystems.2007.05.018 | §2, eqs. (7), (9), (15) | parts | supports (e); precedent for conditioning Ω_int on the shared drive; in the bib but uncited |
| Attentional policies are covert actions | Sandved-Smith et al., Neurosci. Conscious. (2021), doi:10.1093/nc/niab018 | Fig. 4 | parts | against (e) at the member level |
| Epistemic actions modify the world to change input | Kirsh and Maglio, Cogn. Sci. 18 (1994), doi:10.1207/s15516709cog1804_1 | pp. 513–515 | parts | against (a1), interpretive |
| A null removes one mechanism | Gotelli and Graves, Null Models in Ecology (1996) | pp. 3–4 | secondary | supports (a2) |
| Segregation over any partition among identical Bayesian listeners | Sethi and Yildiz, Econometrica 84 (2016), doi:10.3982/ECTA13320 | Prop. 2(c) | parts | a route to partitions that N_w does not predict |
| Random-coefficient Riccati contraction | Bougerol, SIAM J. Control Optim. 31(4):942–959 (1993), doi:10.1137/0331041 | Thms 1.7, 2.4, 2.6 | pp. 942–953 | not applicable to I* (R14); the assignment's journal citation was wrong |
| Iterated function systems with place-dependent probabilities | Barnsley, Demko, Elton, Geronimo, Ann. IHP Probab. Stat. 24 (1988) | Thm 2.1 | abstract and statement | covers T-fast, not T-real; no continuity in parameters |

No prior statement of C12's bound was found.