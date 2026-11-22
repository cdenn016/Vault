# Raw investigator reports for open_agy_meta_agent_exists.md (2026-11-21)

Single-investigator outputs and adversarial attacks, unedited. Statuses are the investigators' own; the record states the adjudicated status.


## construct-epistemic

## Verdict

I constructed an instance and checked it against every clause of def:agy-meta-agent (05_agency.tex:379-381), read literally. Two declarations carry the result, and the coordinator should accept them explicitly before using it:

1. **Episode clock.** The world is held fixed for one sensing round and one delivery round, then renewed. This is how the one-round message lag of eq:fw-world (02_framework.tex:15) is handled.
2. **Attention at infinite precision.** Attention is selected at γ_att = ∞ with uniform tie-breaking.

The grade is (r0, α_M, α_I, α_pr, Agency0) = (36, 0, 0.02, 0.01, 0.99), with n_null = 999. Collective agent A (and B by symmetry) passes every clause, using baseline clause (c) with a declared mechanism.

- **Status:** existence is **computed** at a declared instance (form (A)). The open subset is **proved** by continuity, because every clause is a strict inequality between continuous functions at the instance. Its extent is **numerical** (an 81-point box).
- **Reading dependence:** under clause (c) with the mean coupling, the window at the instance is (46.50, 54.09]. So r0 = 36 is inadmissible there and r0 = 50 is needed.

## Declared specification

**Population**
- N = 8 agents in two niches: A = {1..4}, B = {5..8}.
- World η = (η_A, η_B), independent components, each N(0, P0) and renewed every episode.
- Each agent of niche X models only η_X. This exact marginal model is correct because the components are independent.
- **Slots:** each agent has one exterior slot. If open, it reads s_i = η_X + v_i with Var v_i = R^s. v_i is the agent's private sensing noise (a private input, not a broadcast noise).
- **Messages:** an open agent broadcasts its raw reading, with no sender-side noise. Receiver l reads it with receiver-specific noise ν_li, Var = R_c, in the delivery round.
- **Attention:** capacity κ = 3, chosen by expected free energy at γ_att = ∞. Each agent attends its 3 niche co-members; cross-niche messages carry no information under its model.
- **Fusion:** an exact Gaussian posterior, plus computation noise of variance 10⁻³ on the belief mean.
- **Slots by deliberation:** within each niche, slot profiles are chosen by (P1)–(P4) (05_agency.tex:156-169) at each episode start. Preferences are epistemic only (ψ ≡ 0), habits are a uniform product, and γ = 4. The owner reads its own slot directly.
- **Errors:** e_i = m_i − η_X at the end of each episode.
- **Instance:** P0 = 1, R^s = 1, R_c = 0.1. No records, no acts, no consensus.

**Selector and baseline**
- Contrast at level r0 (def:col-collective, 04_collectives.tex:214-221).
- Comparison medium, clause (c) with the declared mechanism (04_collectives.tex:202): the same 8 agents sharing one world component, with the same noises, capacity and γ. Slot deliberation runs among all 8. Attention is uniform over the open others, up to κ. The precedent is lem:frm-split-law (07_formation.tex:173).
- Statistic for the partner-randomization test: S = min(r(A), r(B)) when Π^c is diffusive, else 0 (no region selected).
- Admitted class: (P0, R^s, R_c, γ) ∈ (0,∞)⁴, with n = 4, κ = 3, σ² = 10⁻³ and γ_att = ∞ fixed.

**Closure and agency declarations**
- Coarse variable: y = mean of the members' belief means. The belief it encodes is N(y, P̄(π)), where P̄ is the members' average claimed variance.
- Decision states: {episode start}, weight 1.
- Agency class: belief N(·, P0), slot likelihood N(η, R^s), ψ ≡ 0, habits uniform product, γ_C ∈ [0, 200]. This contains the habit-only model and has no free joint habits.

## Clause by clause

| Clause (definition, file:line) | Result | Margin | Status |
|---|---|---|---|
| Moment bound (M) (08_scale.tex:23) | Episodes are i.i.d. with finite second moments | – | proved |
| Diffusive Π^c of the whole population (04_collectives.tex:147-151); second-moment convention (04_collectives.tex:187) | Σ^c = blockdiag(αI+β11ᵀ, same) with α = 0.015111 and β = 0.200540 (sensing-noise part 0.190651 plus policy-mixture part 0.009889); coupling 16.2388 within niches, 0 across; uniform leak 1.223585 | min row sum 1.22 | exchangeability proved; values computed |
| Monte Carlo cross-check of Σ^c (200k episodes) | β = 0.19994 against exact 0.20054 (z = −0.58); dropping the policy-mixture term gives z = 8.9 | – | numerical |
| Contrast and admissible level | r(A) = r(B) = 54.0861 = 1 + nβ/α; every other region ≤ 2.860; regions meeting both niches ≤ 1; leak ratio 1 | r0 = 36 sits 18.09 below r(A) | computed (C1 proved) |
| Baseline, clause (c) with mechanism (04_collectives.tex:197-209) | Medium is diffusive; supremum 18.5982, attained by the whole medium; window (18.598, 54.086] | 17.40 below r0 | computed |
| Baseline, alternative readings | (c) mean coupling = (b) complete graph: 46.502, window (46.50, 54.09]. (b) niche graph declared: window empty | – | computed |
| Selected partition at r0 | Exactly {A, B} | – | computed |
| Closure, memory part (05_agency.tex:13-24) | Closure defect and Markov defect are both 0, because A = 0 at the episode clock and policies and noises are fresh each episode. This is degenerate. | – | proved |
| Closure, inference part | Expected relative entropy to the union-model posterior is 0.007655 nats | 0.012 below α_I | computed |
| Deletion nulls N_lp, N_rn | Every inter-agent channel, including announced intentions, carries pure noise, so the null is causally separating; Σ^c is diagonal (off-diagonal 2e-16) and r ≤ 1; nothing is selected | – | proved (prop:agy-nulls-vanish(a),(d), 05_agency.tex:311-314) + computed |
| Freezing null N_fr | Initial message content declared deterministic; Σ^c diagonal | – | proved + computed |
| N_eff, N_inf | Not applicable: no acts | – | proved |
| Habit null N_hab | Applicable: attention and slots are both selected by expected free energy. r(A) = 4.352, below every admissible level | – | computed |
| Partner randomization N_pr, redrawn every round | r(A) = 4.140 with the slot law kept; 4.315 with all slots open; 4.352 with uniform slots | – | computed |
| Partner randomization N_pr, drawn once; test of prop:agy-tests(b) (05_agency.tex:367) | 999 draws: 995 non-diffusive (directed attention produces common-listener positive entries); the largest S among the rest is 3.29; p = 0.001, which rejects at 0.01 | p = 0.001 vs 0.01 | numerical |
| N_ex, type S (tab:agy-nulls 05_agency.tex:352; exact fusion 02_framework.tex:145) | Not applicable: receivers already condition exactly on all retained data, so the model is unchanged. If counted as applicable, it is trivially survived. | – | proved |
| Agency index (05_agency.tex:240-246) | 0.999891 (fitted γ_C = 4.192, minimum KL 2.23e-5, KL to habits 0.2044); log odds ratio between two members −0.544, so the law is not a product law | 0.0099 above Agency0 | computed |
| Type E nulls N_w, N_code | Both predict {A, B}. Agreement is reported: the support of the partition is explained by access and codes, so what is attributed to interaction is the contrast level only | – | interpretive |
| Member-restricted order parameter Ω_int(A∣ζ_B) | Positive, because β > 0 implies conditional dependence and A's members do not depend on B's private inputs. Gaussian pair MI given η at the all-open profile is 0.972 nats | – | proved; value computed |
| N_fg (diagnostic) | No forgetting term, so the null changes nothing | – | – |

**Agency detail.** Each member has an exact potential g(S), with g(S+1) − g(S) = f(1/R^s + S/(R^s+R_c)) − f(S/(R^s+R_c)) and f(x) = −½ln(1 + P0x). The stationary law is P^∞ ∝ exp(−γg(S)) (proved). The deliberation chain reproduces it to 1e-16. A negative control with heterogeneous own-slot precision breaks detailed balance (3.1e-4).

**Robustness box** (P0, R^s, R_c, γ each at ×0.8, ×1, ×1.2; numerical):
- Diffusive with β > 0 at all 81 points.
- r(A) ∈ [36.66, 80.03]; mechanism baseline ≤ 22.89; subset contrast ≤ 2.90; N_hab ≤ 4.62; N_pr ≤ 4.49.
- r0 = 36 is admissible and selects {A, B} at 81/81 points. The smallest window width is 19.66.
- Agency ≥ 0.99970; α_I ≤ 0.0132.
- Corners, partner randomization drawn once: 3184 draws, 5 diffusive, the largest S among them 4.97.
- Under the mean-coupling clause the window is nonempty at all 81 points, but its position moves with the parameters.

## Proved pieces

- **C1.** For Σ = αI + β11ᵀ with α > 0 and β ≥ 0, the precision is Π = (I − β/(α+nβ)·11ᵀ)/α. The coupling is β/(α(α+nβ)), the leak is 1/(α+nβ), the cut is 0, ξ_in = 1/α, and r = 1 + nβ/α.
  - Checks: α = 1, β = 0.5, n = 4 gives r = 3; α = 0.3, β = 2, n = 6 gives r = 41.
  - Negative control: β = −0.2 gives a positive off-diagonal entry, so the precision is not diffusive.
- **Closed form with all slots open and σ² = 0:** r = 1 + n(n+2ρ)/(ρ(n−1+ρ)) with ρ = R_c/R^s. At n = 4, ρ = 0.1 this is 55.19355; the code matches to 1e-13.
- **Exchangeability within a niche.** The law is invariant under relabeling a member together with its slot: P^∞ depends on S only, the noises are i.i.d., and attention is equivariant.
- **Regions meeting both niches** have r ≤ 1, and proper subsets have r(S) = (ε + |S|a)/(ε + (n−|S|)a). This is the argument of thm:frm-split-contrast(a) (07_formation.tex:182).
- **Exact closure:** A = 0. In the persistent-world extension below, A = I ⊗ A_f, which preserves the kernel of the averaging map.

## Checks of the coordinator's hypotheses

- **(h1) Supported here.** With no acts and no consensus there is no collider. Two other sources of non-diffusivity appear:
  - directed attention, which makes 995 of 999 quenched partner-randomization draws non-diffusive;
  - policy mixing.

  The full model avoids both through reciprocal attention to all co-members (κ = n − 1).
- **(h2) Proved** (C1 above).
- **(h3) Confirmed.** Exact fusion leaves the model unchanged, so N_ex is not applicable.
- **(h4) Confirmed in sharper form.** With attention held at its selected pattern and only slots drawn from habits, r(A) = 60.29, which is above r0. So if attention were exogenous, the differ clause against N_hab would fail. The result therefore rests on attention being selected by expected free energy. Declaring the niche graph empties the window.
- **Suggested symmetric design fails.** If every member, the owner included, reads the slot through a receiver-specific channel, the slot noise becomes a channel noise shared by several receivers. def:col-world-conditional (04_collectives.tex:131) conditions on it.
  - At a deterministic profile this gives r = 1 (computed).
  - With random profiles the only coupling is the policy-mixture common term, giving r = 17.40.

  The owner-direct design is still an exact potential game, so the symmetry was not needed.

## Sensitivity, weakest clause and open obligations

**Sensitivity** (computed)
- **Finite attention precision γ_att:** r(A) = 7.26 / 11.79 / 24.39 / 47.53 at γ_att = 5 / 10 / 20 / 40. So r0 = 36 needs roughly γ_att ≥ 30; the comparison medium at finite γ_att was not computed.
- **Second moment conditioned on the policies:** r(A) = 51.57 and the baseline is 18.68, so r0 = 36 is still admissible.
- **Persistent world at the round clock** (constant F, one-round message lag, all slots open, exact delayed Kalman filter):

  | F | 0.5 | 0.9 | 0.95 | 0.99 |
  |---|---|---|---|---|
  | r(A) | 1.22 | 3.77 | 6.01 | 11.74 |
  | Medium baseline | 1.21 | 2.99 | 3.97 | 5.40 |

  - Closure of the average is exact, with spectral radius of A_f up to 0.76.
  - The inference tolerance is 0.097 at F = 0.99, the cost of the lag.
  - Nulls and finite-γ agency were not computed in this model.

**Weakest clause:** the collective clause at the declared level.
- Its margin over the box is thin at the worst corner: r(A) = 36.66 against r0 = 36.
- It depends on the baseline reading (the mean-coupling clause needs r0 ≈ 50).
- It depends on γ_att = ∞.
- Separately, the memory part of closure holds only degenerately (A = 0, renewed world).

**Minimal unresolved obligation:** a single instance with a persistent world at constant F, finite-γ slot policies and all clauses checked. That needs second moments of the switching Kalman filters, plus the nulls in that model.

**Not done:**
- The test against partner randomization under the substitute mutual-information selector (s05_agency.tex:252) is uninformative: the niches stay exactly independent under every null draw, so the between-block mutual information is 0 in both models.
- No fresh-context review was run; review state is self only.

**Next action:**
1. A blind recomputation of r(A), the mechanism baseline and the agency index at the declared instance.
2. The persistent-world, finite-γ instance, estimating E[Cov(e∣η)] as ½E[(e¹ − e²)(e¹ − e²)ᵀ] from two replicas run on the same world path.

## Files

All in C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\epistemic_niche\

- Library: core.py
- Deciding scripts and outputs: run_main.py → main_out.txt; run_nulls.py → nulls_out.txt; run_robust.py → robust_out.txt; run_dynamic.py → dynamic_out.txt; run_sens.py → sens_out.txt
- explore.py and explore2.py are design exploration only.
- explore_out_STALE_prefix_bool_bug.txt is stale. It was produced before a numpy bool-sum bug was fixed in core.py (the bug undercounted the shared-noise term); do not use it.

No repository or vault file was edited.

## attack: construct-epistemic

## Verdict

**The candidate fails the inference part of closure at the stated grade α_I = 0.02 under the literal reading of def:agy-closure(ii) (05_agency.tex:21).** Every other clause survives, and every computation in the report is correct.

- **What the clause asks.** "The belief that y encodes" must be within α_I of the union-model posterior.
- **Why the reported value does not meet it literally.** The declared y is the scalar mean of the belief means. The reported 0.00765 uses the encoded belief N(y, P̄(π)), whose variance comes from the slot profile π, and π is not part of y.
- **Best achievable from y alone.** The best belief that is a function of y has expected relative entropy (KL):
  - 0.023620 at the instance, forward direction (the direction of the precedent at s10a_meta_agents.tex:143);
  - 0.025836 in the reverse direction, best Gaussian belief;
  - 0.0170 to 0.0323 over the 81-point box, above 0.02 at 70 of 81 points.
  - Status: computed.
- **When it passes.** Only if the encoded variance may be read off the blanket path. def:agy-closure grants that input-conditional form to the memory clause (05_agency.tex:20-21), but does not state it for the inference clause.
- **Repairs (computed).** Either α_I ≥ 0.026 at the instance, or the single-precision variant of attack 6, which passes under both readings.
- **What the rest of the grade rests on.** The declarations in attacks 3 to 8, which the definitions permit but do not force. The episode clock (attack 4) is the one that no computed variant removes.

## Attacks tried

### 1. Blind recomputation
Status: computed. Outcome: no error.

My code is independent: fx.py does not import core.py. It builds Σ^c from noise-coefficient vectors, contrast from a Helmert basis, and the slot law from the (P4) transition matrix. It reproduces every deciding number to at least 9 digits:

- **Slot law:** P(S=0..4) = (0.0059, 0.0950, 0.3310, 0.4051, 0.1629). The chain equals the Gibbs law to 1e-16. Negative control: a heterogeneous own precision breaks detailed balance (3.1e-4).
- **Σ^c:** α = 0.0151105, β = 0.2005401 (0.1906513 without the mean-variation term).
- **Precision:** uniform leak 1.2235845, coupling 16.238842, cross coupling 0.
- **Contrast:** r(A) = r(B) = 54.08613. Every other region ≤ 2.85986; regions meeting both niches ≤ 1. Control: a β = 0 block gives r = 1.
- **Monte Carlo** (new seed, 300k episodes): β = 0.20086, z = 0.37; dropping the mean-variation term gives z = 12.0.
- **Baselines:** mechanism medium 18.59819 (attained by the whole medium); mean coupling 46.50240.
- **Nulls:** N_hab 4.35231; annealed N_pr 4.13990; diagnostic with attention kept 60.29197.
- **Agency:** 0.9998909 at γ_C = 4.1921.
- **Inference:** α_I = 0.0076548 with the investigator's encoding.
- **Finite γ_att:** r(A) = 7.257 / 11.793 / 24.392 / 47.534.
- **Box:** the 81-point extremes match robust_out.txt exactly.

### 2. Inference clause read literally
Status: computed. Outcome: fails at 0.02.

- **Optimum is over all encodings.** In the forward direction the optimum over all beliefs that are functions of y is Gaussian, because the expected log-loss is quadratic. So 0.023620 is a minimum over every encoding of y. Its irreducible part, E[Var(m*|y,π)/(2P*)], is 0.006747.
- **Controls.** The same integrator returns 0.0076548 for N(y, P̄(π)). Monte Carlo (200k episodes) returns 0.007658 for the π-dependent encoding and 0.024145 for the constant-variance encoding.
- **P̄ cannot be added to y.** P̄ carries no internal noise, so Q^n ≻ 0 of eq:agy-interior (05_agency.tex:16) fails, and it is not linear in the blanket.
- **A pathwise reading fails every encoding** because of Gaussian tails. The expected-KL reading follows the two-firms precedent.

### 3. Partner randomization and the S = 0 convention
Status: proved (structural) and computed.

- **The quenched test is decided by a convention.** Quenched draws were non-diffusive in 400 of 400 of my draws (γ = 4) and 200 of 200 at γ = 40. The test therefore rests on scoring undefined contrast as 0, which no definition states.
- **The manuscript's own substitute does not reject.** When directed attention leaves contrast undefined, the manuscript names a substitute selector: the ratio of mean within-block to mean between-block world-conditional mutual information (MI) over balanced bipartitions (s05_agency.tex:252; open:col-non-diffusive, s04_collectives.tex:268).
  - Given η, A's errors depend only on A's private inputs and B's only on B's. This holds in the full model and in every N_pr draw, because exact receivers give cross-niche messages zero weight.
  - So the between-block MI of {A, B} is exactly 0, and its ratio is +∞ in the full model and in every draw.
  - Then S_0 = S_l = +∞, p = (1+999)/1000 = 1, and every draw selects the same bipartition.
  - What the report calls "uninformative" is a failure to differ under that selector.
- **Outcome:** passes cleanly if N_pr is declared redrawn every round (tab:agy-nulls, 05_agency.tex:350). The second-moment precision is then diffusive (exchangeable), the contrast selector applies without any convention, r(A) = 4.1399 and p = 1/(n_null+1) = 0.001.

### 4. Episode clock and error convention
Status: proved and interpretive. Not repaired.

- **What the framework says.** eq:fw-world (02_framework.tex:15) has time-invariant F and Q and a one-round message lag. def:col-world-conditional (04_collectives.tex:131) requires e(t) and η_t to be jointly stationary.
- **What the construction does.** It uses a period-two world: F = 1, Q = 0 within an episode; F = 0, Q = P0 at renewal. This is cyclostationary at the round clock. It then samples the filtered error at the end of the delivery round.
- **Under the default error the structure vanishes.** The manuscript's default error is the prior error (appA_notation.tex:67; def:fw-level0, 02_framework.tex:315). Under it Σ^c is diagonal at every round:
  - renewal makes every prediction of a new world the prior mean;
  - the delivery round's prior error contains only the agent's own reading;
  - message content enters only the posterior, which renewal discards.
  - So no region has r > 1.
- **Two coupled declarations are needed:** periodic renewal, and the stated end-of-episode filtered error. The notation's "unless stated" permits the second. def:fw-system does not place the first inside the framework.
- **The time-invariant fallback is incomplete.** dynamic_out.txt gives r(A) = 11.74 against a medium of 5.40 at F = 0.99, but nulls and agency were not computed there.

### 5. Per-agent error coordinates
Status: interpretive; repaired (computed).

- **The issue.** q_i is a belief over η ∈ R^K (02_framework.tex:17). With K = 2 the errors are 2-vectors.
  - Their Σ^c is not of the form Σ^sc ⊗ I_2, which is the only case in which def:col-contrast defines vector-error contrast (04_collectives.tex:187).
  - Without computation noise on the non-niche component, Σ^c is singular.
  - The reported 8×8 Σ^c mixes A's η_A-errors with B's η_B-errors.
- **Repair.** Put computation noise on every belief component, and compute contrast for C = A on the η_A coordinate. This follows the "price coordinates" precedent (s05_agency.tex:267).
- **Computed result:**
  - diffusive;
  - r(A) = 54.0861, unchanged;
  - every other region ≤ 2.8599; leak ratio on A = 1;
  - mean-coupling baseline 1.056; mechanism medium unchanged.
  - The claim becomes one about A alone.

### 6. Two precisions
Status: interpretive; repaired (computed).

- **The issue.** def:fw-system draws all active states from one posterior with one γ (02_framework.tex:17), and attention sets include world channels (:13). The candidate uses γ = 4 for slots and the limit γ_att = ∞ for message attention.
- **With one γ = 4 for both,** r(A) = 6.513 is below the mechanism baseline of 8.584, so the window is empty.
- **One γ for slots and attention** (medium at the same γ):

  | γ | r(A) | mechanism | mean coupling | annealed N_pr | Agency |
  |---|---|---|---|---|---|
  | 10 | 9.657 | 9.145 | 8.420 | 4.166 | 0.99998 |
  | 20 | 14.783 | 8.370 | 12.814 | 4.254 | 0.999996 |
  | 40 | 32.329 | 7.653 | 27.853 | 4.308 | ≥0.9999995 |
  | 60 | 47.157 | 7.573 | 40.563 | 4.314 | ≥0.9999995 |

  N_hab is 4.352 throughout.
- **Result at γ = 40 with r0 = 30.** Every clause passes under both baseline readings and both inference readings:
  - other regions ≤ 2.774;
  - α_I = 0.0151 (variance from the blanket path), 0.0130 (constant variance), 0.0129 in the reverse direction; Monte Carlo standard error about 5e-5.
- **N_pr must be the annealed version here:** quenched draws were non-diffusive in 200 of 200.
- **Neighborhood.** On a ±5% grid around (P0, R^s, R_c, γ) = (1, 1, 0.1, 40), r0 = 30 is admissible with A selected at 70/81 points (mechanism) and 59/81 (mean coupling). At the center it holds on an open neighborhood by continuity.
- **Margins at the center:** 2.33 below r(A); 2.15 above the mean-coupling baseline.

### 7. Comparison medium
Status: computed. Survives.

- **Reading.** Once a mechanism is declared, clause (c) makes its exchangeable state the comparison medium (04_collectives.tex:202). The precedent lem:frm-split-law (07_formation.tex:173) removes the asymmetry that defines the groups and keeps the medium's own leak, as this candidate does.
- **Alternatives computed; both leave r0 = 36 admissible:**
  - slot EFE in the medium read literally under (P2), expecting all opened slots: 20.030;
  - mechanism couplings with the population's mean leak: 14.525.
- **Mean-coupling reading.** The window at the instance is (46.502, 54.086], so r0 = 50 works under both readings at the instance. Two equal disjoint cliques always leave a window: 1 + (24/7)a/ε < 1 + 4a/ε.

### 8. Agency scope
Status: proved (index 0 at the attention state). Literal pass.

- **The asymmetry.**
  - N_hab needs message attention to be selected by EFE: with attention kept, r(A) = 60.292 ≥ r0 (reproduced), so the differ clause would fail.
  - Yet the declared decision states contain only the slot decision.
- **Why including attention breaks the index.**
  - Co-member channels are internal (def:col-partition, 04_collectives.tex:18-25).
  - Cross-niche channels carry no information about η_A.
  - So every group model of def:agy-group-model (05_agency.tex:159) assigns the same G_C to every attention pattern.
  - At an attention decision state the fitted law equals the habits E for every γ_C, and the index there is exactly 0.
- **Outcome.** def:agy-agency-index lets decision states be declared, so the clause holds on the declared set. It fails with any positive weight on the attention decision.
- **Missing declaration.** The attention habits that decide N_hab (uniform over the 35 κ-subsets, att_random in run_nulls.py) are not in the declared specification. At γ_att = ∞ they are invisible in the full model, so they must be declared.

### 9. Other clauses: no failure found
- Moment bound at the episode clock (08_scale.tex:23).
- C1 and diffusivity: proved and recomputed.
- Selected partition is exactly {A, B}.
- "For each constant of the selector" must range over the window, since for r0 > r(A) every model selects nothing. This restriction applies to any candidate.
- Open subset by continuity (strict inequalities; cross-niche zeros are structural).
- Deletion and freezing nulls: diagonal to 2e-16 with intentions deleted (prop:agy-nulls-vanish(a),(d), 05_agency.tex:311,314).
- N_eff and N_inf: inapplicable.
- N_ex: inapplicable, because level 0 with learned noise R^s+R_c is the true likelihood of a raw-reading message (prop:fw-level-optimality(b), 02_framework.tex:159).
- Second-moment convention (04_collectives.tex:187): triggered only if slot choices count as world-channel attention. Without it Σ^c is undefined, because Cov(e|η) depends on η².
- Memory clause: holds, degenerately (A = 0).
- Deliberation must be declared to run to stationarity each episode.
- Theorem thm:agy-agency does not apply: received slot copies have receiver-specific likelihoods, against def:agy-group-model's premise. This does no harm, because the potential and the index were computed directly.

## Corrections to the investigator's report
1. The α_I pass uses π in the encoded variance. Under the literal reading the instance needs α_I ≥ 0.0237 (0.0259 reverse), and the whole box needs 0.0323.
2. Under the mutual-information substitute selector, N_pr gives p = 1, a failure to differ, not "uninformative". Declare N_pr redrawn every round as the decisive version.
3. Add the error-convention dependence: under the default prior error, Σ^c is diagonal.
4. Declare the attention habits.
5. Suggested grade, which removes three dependencies at once (γ_att, the baseline reading and the inference reading): single γ = 40 for slots and attention, r0 = 30, α_I = 0.02, annealed N_pr. The episode clock and the filtered-error convention remain.

## Weakest point
The episode clock together with the end-of-episode filtered error. The instance lies outside the time-invariant def:fw-system, and it has no world-conditional structure under the manuscript's default error.

The thinnest clause margins are:
- the inference clause under the literal reading, at the declared instance;
- the 2.15 margin above the mean-coupling baseline in the single-γ variant.

## Files
All are in C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\. No repository or vault file was edited. Review state: self only.

- Library: C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\fx.py
- Scripts and outputs (each check_X.py writes check_X_out.txt in the same folder):
  - C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_A.py → C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_A_out.txt
  - C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_B.py → C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_B_out.txt
  - C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_C.py → C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_C_out.txt
  - C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_D.py → C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_D_out.txt
  - C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_E.py → C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_E_out.txt
  - C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_F.py → C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_F_out.txt
  - C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_G.py → C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\falsify_epistemic\check_G_out.txt

## construct-performative

VERDICT (construct-performative). Performative acts do not rule out a meta-agent. A collective that is the only actor on the world component it acts on (route a) has a diffusive world-conditional precision exactly when its contrast r = v/α ≥ 1. I derived a closed form for this (proved) and checked it against direct conditioning on the world path to 1e-15.

The performative niche population PN below meets every clause of def:agy-meta-agent (05_agency.tex:379-381) at grade (r0 ∈ (5.075, 24.499], αM = 0, αI = 5.61e-3, αpr = 0.01 with n_null = 99, A0 = 0.94). The grade is computed and holds only under the readings R1-R4 listed below. The decisive reading is R1: N_eff and N_inf (05_agency.tex:348-349) are type D only "for collectives said to form by joint action" and "by communication through acts". Under the strict reading, where N_eff is type D whenever members act, the clauses cannot all hold in the exchangeable single-actor class (proved, Prop N below).

C3 is false as literally stated: there is a computed counterexample. It holds in corrected form. For two exchangeable collectives acting on one conditioned variable, the cross entries of Π^c have the sign of φ1κ1φ2κ2 (proved). That product is positive for every pair of collectives that choose their acts optimally by EFE ("EFE-consistent") and know the sign of their own effect (proved). So the two-firms obstruction is generic for EFE-chosen acts. Only route (a) or cross-communication (route b, computed) removes it.

All scripts and outputs are in C:/Users/CHRISA~1/AppData/Local/Temp/claude/63c81c17e87f0010/34faeca5-ea90-45d1-8cc4-412bdf898c58/scratchpad/metaagent/performative/. Library: pc.py and pcg.py. Checks: check1..check13*.py, each with a matching *_out.txt. Each check declares its expected outcome and includes a negative control. Every run was single-threaded and under one minute.

CONVENTIONS. Π^c is computed by exact Gaussian conditioning on a two-sided window of the whole world path, per def:col-world-conditional (04_collectives.tex:130-132). The world innovation is not conditioned separately. Windows were checked for convergence: L=30 vs 60 differ by 1e-14, L=60 vs 160 by 1e-15. For errors e_i = m_i − η, Cov(e|η) = Cov(m|η).

Validation on the test instance. I reconstructed ex:met-two-firms (s10a_meta_agents.tex:108-118), bounded model for both firms, with the latency of eq:met-firms. Results: ρ(A) = 0.824. At n_c=1, the largest off-diagonal entry is 166.3 and the smallest row sum −0.8215; chk10a_meta_agents.tex:57 reports 166.3 and −0.82. Cross-firm entries are 0.024–0.045. At n_c=0 the largest off-diagonal is 0.0416; at n_c=4 the smallest row sum is −15.99. It is non-diffusive at n_c = 0, 1, 4, as the record requires. Negative control: with the acts' price effect removed, the cross entries vanish (2e-12) while the singular-consensus entry 166.3 persists (check6). C1's exact model was not rebuilt.

RESULTS

R1. Lemma E (record claim C1): proved.
- Hypotheses: Σ^c_CC is invariant under permutations of C, and Cov(e_C, e_rest | η) = 0.
- Then Σ^c_CC = α(I−J/n) + vJ/n, because the commutant of the permutation representation is span{I, J}.
- Π^c_CC = α⁻¹(I−J/n) + v⁻¹J/n, with coupling (α⁻¹−v⁻¹)/n, leak v⁻¹ and cut 0.
- Diffusive iff v ≥ α. x_out = 1/v and x_in = 1/α, so r = v/α.
- Writing v = α + nβ gives C1 exactly: coupling β/(α(α+nβ)), leak 1/(α+nβ), r = 1 + nβ/α.
- β < 0 gives positive off-diagonal entries. This negative control was confirmed in check1 (points 4-5: r = 0.025 and 0.114, entries +3218 and +63.6).

R2. Prop P (performative exchangeable niche): proved; computed.
Setting:
- One collective C of n agents and a scalar component η, with η' = Fη + bΣ_C u_j + w and Var w = Q > 0. No other agent acts on η.
- Each member senses s_i = η + v_i (variance R) and receives every niche-mate's raw observation through receiver-specific noise Rc.
- Gains K_s, K_c are fixed and identical across members; c0 = 1 − K_s − (n−1)K_c.
- Acts are deterministic: u_j = −g m_j^+.
- Members read the realized total act, so m_i' = F m_i^+ + bU.
- There is no channel between C and V∖C. Stationarity requires |Fc0| < 1 and |F − bgn| < 1.

Result. With σ_ξ² = (K_s+(n−1)K_c)²R + (n−1)K_c²Rc, σ_⊥² = (K_s−K_c)²R + (n−1)K_c²Rc, φ = F−bgn, ρ = c0φ and s = nb²g²σ_ξ²/Q:
- α = F²σ_⊥²/(1−F²c0²)
- v = φ²σ_ξ²/√((1+ρ²+s)²−4ρ²)
- r = r0·D_fb·D_coll, where r0 = σ_ξ²/σ_⊥², D_fb = (φ²/F²)(1−F²c0²)/(1−φ²c0²), and D_coll = (1−ρ²)/√((1+ρ²+s)²−4ρ²).
- For Kalman gains, r0 = ((n+ρc)² + (n−1)ρc)/(ρc(n−1+ρc)) with ρc = Rc/R, independent of F and Q.

Proof:
1. (private noises, w) ↦ (private noises, η-path) is triangular with unit Jacobian. So the conditional density of the private noises given the path is ∝ prior × Π_t φ_Q(w_t), where w_t = η_{t+1} − Fη_t − bΣu_j(t).
2. Given the path, m' = (FI − bgJ)m^+ + (path terms), and m^+ = c0 m + ζ + (path terms). Cov(ζ) is permutation-invariant, so the projections onto 1 and 1^⊥ are uncorrelated.
3. The likelihood depends only on z^+ = φ_C^T m^+, through o_t = bg√n z^+(t) + w_t. So the disagreement modes keep their prior law, which gives α.
4. z^+ is an AR(1) process (ρ, σ_ξ²) observed in white noise. Its two-sided smoothing variance is (2π)⁻¹∫[|1−ρe^{iω}|²/σ_ξ² + nb²g²/Q]⁻¹dω = σ_ξ²/√((1+ρ²+s)²−4ρ²). Since z(t) = φz^+(t−1) + (path terms), this gives v.
5. Apply Lemma E. Cross-covariance with outsiders is 0 by step 1.

Check (check1): windowed conditioning matches the closed form to ≤ 2.7e-15 relative at five points, including two non-diffusive ones.

Insight: the dominant performative effect is the closed-loop factor D_fb, not the collider. Given the path, the members' own read act damps their collective mode.

R3. Prop N (acts never raise contrast in setting P): proved.
- D_coll ≤ 1, because (1+ρ²+s)²−4ρ² ≥ (1−ρ²)².
- D_fb ≤ 1 iff φ² ≤ F². For EFE-consistent acts with a correct model, φ = F/(1+nc), so D_fb < 1.
- Consequence for N_eff, assuming a comparison medium declared with the model and held fixed under nulls, and r0 ≥ n−1. N_eff is setting P with s = 0 and unchanged gains. Each block then has r_eff ≥ r ≥ r0; sub-blocks have ((n−1)r+1)/(r+n−1) < n−1; regions meeting two blocks have r ≤ 1. The same blocks are selected at every level.
- Hence if N_eff is D for C, C is not a meta-agent: an obstruction in setting P.
- For N_inf, contrast also rises (computed: 28.09 and 27.87 at g=0.15; 28.43 at g=0.05), but this is not proved in general because the gains change.

R4. Prop S (sign rule): proved; computed in 11 instances (check3, check9).
Setting:
- Two collectives, each as in P, both acting on the same η with gains g_k of any sign.
- Members of C_k read C_k's realized act with believed effect b̂_k and predict m_i' = a_k m_i^+ + b̂_k U_k. a_k includes any model of the other firm's act as a multiple of m_i^+.
- Gains are identical within each firm; there is no channel between the firms.

Result:
- With φ_k = a_k − b̂_k g_k n_k and κ_k = b g_k √n_k, for i ∈ C1 and j ∈ C2: Π^c_ij = (V⁻¹)_12/√(n1 n2), with sign(Π^c_ij) = sign(φ1κ1φ2κ2).
- Proof: X = z1^+ and Y = z2^+ are independent AR(1) processes a priori. Their posterior cross-spectral density, −κ1κ2 S_X S_Y/(κ1²S_X + κ2²S_Y + Q), has one sign at every frequency. Then use z_k(t) = φ_k z_k^+(t−1) + (path terms), (V⁻¹)_12 = −V_12/det V, and independence of the 1^⊥ parts.
- Computation noise on predictions changes only diag(V), so the rule is unchanged.

Corollary (EFE). If acts are the mean of the group posterior for a one-step quadratic EFE with Gaussian habits (thm:agy-joint-acts(b), s05_agency.tex:169-173, extended to continuous acts):
- b̂_k g_k n_k = a_k n_k c_k/(1+n_k c_k) with c_k = σ_E²γΛ*b̂_k², so φ_kκ_k = (b/b̂_k)a_k²c_k√n_k/(1+n_k c_k)², and sign(φ_kκ_k) = sign(b·b̂_k).
- Two EFE-consistent firms that know the sign of their own effect therefore have positive cross entries and are non-diffusive, whatever their world models.
- Checked: correct models give +0.0548; a firm that believes F̂ = −0.5 gives +0.0199; mutual modeling gives +0.0507.
- A misjudged effect sign gives −0.0548 and a diffusive Π^c (check9).

C3 as stated: refuted. Counterexample (check3, case E2, Rc=0.02): g = (1.5, 0.2), both loadings of one sign, no channel, φ = (−0.30, +0.74). All cross entries are −0.956 and Π^c is diffusive, with r(C1) = 10.86 and r(C2) = 146.96. The overshooting rule (bg1n1 = 1.2 > F) is not EFE-consistent. The corrected C3 is the Corollary.

Heterogeneous instances, not covered by the theorem:
- check2 (noise 0.5,1,2,4 | 1,1,2,2): all cross entries positive, 0.068–0.082.
- Two-firms model at n_c=4: mixed signs, −0.016 to +0.089.
- The general non-exchangeable case and three or more firms are open.

R5. Routes, all computed:
- (a) single actor. Two firms, only C1 acts: cross entries ≤ 7e-14, diffusive, r(C1) = 5.93, 4.26, 2.58 at g = .05, .15, .3.
- (b) within a collective: diffusive iff r ≥ 1 (Prop P). It fails under strong feedback or collider (check1).
- (b) across collectives. Two EFE-consistent firms (φ = 0.66) on one price, every member also reading the other firm's raw data with noise Rcx:
  - cross sign flips between Rcx = 300 (+0.0169) and 100 (−0.085);
  - at Rcx = 100: r(C1) = 16.18 against a mean-coupling baseline of 14.19, a collective;
  - at Rcx = 30: 13.77 against 12.78, a collective;
  - at Rcx ≤ 10: not collectives (check4).
  - Caveats: under an EFE attention budget, cross reads are dropped; the members' competitor model is bounded, so N_ex becomes applicable.
- (c) delegate. One acting delegate per variable: diffusive, r = 5.94, 4.31, 2.67 at g_D = 0.2, 0.6, 1.2. One delegate in each of two firms on one variable: delegate–delegate entry +0.115, +1.23, +8.56, non-diffusive (check2).
- (d) acts on an unsensed component.
  - Each collective on its own component: cross 0, r = 28.50, 27.80, 22.71 at g = 0, 0.15, 0.5.
  - Both on a common component: cross +0.0058 to +0.50, non-diffusive (check4).
  - def:col-world-conditional conditions on the whole world path regardless of who senses it. The only extra conditioning it allows is sender-side broadcast noise.
  - Acts written into records escape conditioning but are stigmergic, not performative, and records leave the baseline undefined (s04_collectives.tex:165-167). So (d) reduces to (a).

R6. Repair inside the two-firms model class (check7):
- Settings: homogeneous R=1; complete-graph consensus w=0.5 (eigenvalues 1 and 1/3, nonsingular); only C1's acts enter the price.
- Result at n_c=1: diffusive, r(C1) = 8.563, r(C2) = 8.775, mean-coupling baseline 7.572, next-best regions 2.32. C1 is a collective at levels in (7.572, 8.563].
- n_c=2: 52.2 vs 45.4. n_c=4: 140.8 vs 122.3. n_c=0: 1.0046 vs 1.0145, not a collective.
- Controls:
  - both firms acting gives +0.0285;
  - the singular lazy ring gives +168.1;
  - heterogeneous R with complete consensus has no positive entry but a row sum of −7.74. This negative leak is a third obstruction source.
- Because the consensus protocol is fixed, this repair fails N_hab literally (trap h4).

R7. PN candidate (check5, check8, check10-13).

Population:
- Eight agents in two niches, A = {0..3} and B = {4..7}, with world components η^A and η^B independent; F = 0.9, Q = 0.05.
- Members of niche k sense η^k (R = 1) and receive raw observations from all three niche-mates (Rc = 0.2).
- Attention is EFE-selected at γ = 300, where P(all three niche-mates) = 0.9998; this residual is ignored in Π^c.
- Filters are exact steady-state Kalman filters.
- Acts on η^k are group-posterior means: Λ* = 4, σ_E² = 2.4e-4, b = 0.2, giving bgn = 0.04 (g = 0.05). Members read their niche's realized act.

Clause verdicts for C = A (B is symmetric):

| Clause | Result | Status |
| --- | --- | --- |
| Collective | Π^c block-diagonal and compound-symmetric. r(A) = 24.4989, equal to the closed form. Baseline is the mechanism's exchangeable state M1 (all 8 agents on one component, 3 uniformly random partners each round, same act rule): ≈ 5.075 by a Gaussian second-moment approximation of the collider part. r_sub = 2.709, ε-ratio = 1. Enumerating all 247 regions, the collectives at any r0 ∈ (5.075, 24.499] are exactly A and B. The mean-coupling alternative is (21.14, 24.50]. | computed; baseline approximate |
| Closure | The collective average is exactly closed: equal column sums, by thm:agy-closure-identity(b), 05_agency.tex:52, so d_cl = d_M = 0. αI = 5.61e-3 nats (E KL from N(m̄, P⁻) to the union model; reverse 5.41e-3). | d_cl = 0 proved; αI computed |
| N_lp, N_rn (with N_eff) | Π^c diagonal (prop:agy-nulls-vanish(d), 05_agency.tex:314). | proved |
| N_fr | Same as above, provided the frozen initial observations are deterministic or conditioned (as in prop:frm-nulls(a)). | proved under that condition |
| N_pr | Quenched: 0/99 draws diffusive, so contrast is undefined, no collective is selected, and p = 0.01. Annealed: ≤ 3.70 (Monte Carlo, collider ignored), below 5.075. | quenched computed; annealed numerical |
| N_hab | Quenched: 0/99 diffusive. Annealed: 4.409 (Monte Carlo with exact time-varying filters; control 28.56 vs exact 28.5), below 5.075, so no collective at any admissible level. | quenched computed; annealed numerical |
| N_eff | Not differed: r_eff = 24.56 (Prop N). | proved |
| N_inf | Not differed: 28.43. | computed |
| N_eff, N_inf types | Both are diagnostics under R1. Prop N supports attributing formation to data sharing: acts only lower contrast. | per R1 |
| N_ex | Inapplicable. The literal relay likelihood is the exact one (fresh noise, prop:fw-level-optimality(b), 02_framework.tex:159), and the filters are exact with known acts, so the model is unchanged. | proved |
| Agency | Class: belief at the members' average, true effect, Λ*, habits fixed, one γ_C ∈ [0,6]. Over 200 equally weighted decision states (m_C = 0.3, stationary deviations): index 0.947 in the discrete declared model (U = {−1,0,1}); 0.967 with continuous Gaussian acts consistent with the dynamics, invariant in γ (0.967, 0.966, 0.966 at γ = 2, 20, 100). Negative control (30× disagreement): median 0.084. Exact group posterior with tilted habits by thm:agy-joint-acts(b) and thm:agy-agency(d), 05_agency.tex:202. | index computed; group-posterior form proved under hypotheses |
| Ω_int(A \| ζ_B) | 4.08 nats over six rounds; 0 across niches. | computed |
| Explanation nulls | N_w predicts {A,B}, which restricts the claim to communication within access groups. | — |

Gain dependence: at g = 0.10 and 0.15 the M1 baseline (3.74, 2.73) falls below the annealed N_hab contrast (4.41), so PN fails N_hab on (3.74, 4.41] and (2.73, 4.41] respectively. This trap is specific to acts: joint feedback lowers the baseline, and N_hab removes it. A by-product for C2: without acts, M1 = 6.86 > 4.41.

Readings required:
- R1: conditional types for N_eff and N_inf.
- R2: deliberation act randomness read by several members counts as sender-side broadcast noise and is conditioned (04_collectives.tex:131). The alternative reading was not computed.
- R3: the comparison medium M1 is declared and held fixed under the nulls, as in 07_formation.tex:209. Under a mean-coupling baseline recomputed per null, the verdicts can flip perversely.
- R4: decision states fix attention, and agency is evaluated on the act component.

HYPOTHESES h1-h4
- h1 confirmed and refined. The collider and the singular consensus each produce positive entries, separable as in the check6 negative control. The collider's sign is given by φκ (R4). Heterogeneous sensing noise adds negative leaks. The agency clause extends to joint acts through def:agy-joint-acts (s05_agency.tex:146-152).
- h2 proved (Lemma E), and its negative control is confirmed.
- h3 confirmed for PN. It fails when members use a bounded model of a competitor.
- h4 confirmed:
  - a fixed protocol fails N_hab;
  - mechanism-generated attention requires the M1 baseline;
  - under the every-constant reading, PN passes the annealed N_hab only at g = 0.05.

STRONGEST SUPPORTED RESULT. In setting P, Π^c is diffusive iff r = r0·D_fb·D_coll ≥ 1 (proved), and acts never raise contrast (proved). PN meets every clause at the stated grade under R1-R4 (computed; baseline approximate; annealed nulls numerical). For two EFE-consistent collectives acting on one variable without communication, Π^c is never diffusive in the exchangeable class (proved). Not independently checked: Props P, S and N are self-checked only.

MINIMAL UNRESOLVED OBLIGATIONS
1. The type of N_eff and N_inf for a performative collective said to form by communication. Under the strict reading, setting P is closed negatively.
2. An exact second moment, including the collider, for the M1 baseline and the annealed N_pr. The margin over annealed N_hab is 0.67 (15%).
3. The sign rule for non-exchangeable firms or for three or more firms.

NEXT ACTION. The coordinator decides R1. If the strict reading is chosen, the search moves to collectives whose partition is created by the acts' physical effect; in the exchangeable class that requires φκ of opposite signs, which EFE-consistent firms that know the sign of their effect never have. If R1 stands, compute M1 exactly (mixture conditional covariance) and run a fresh-context reconstruction of Props P and S.

## attack: construct-performative

VERDICT: survives, with corrections. No clause of def:agy-meta-agent (05_agency.tex:379-381) fails once the grade and declarations below are corrected. Three items in the investigator's output are wrong as written:
(i) "N_ex inapplicable (proved)" is false. N_ex is applicable, and PN survives it by computation.
(ii) The declared agency class "one γ_C ∈ [0,6]" gives index 0.039 at the population's own precision γ = 300.
(iii) The window's upper endpoint 24.499 is not reached once Q^n ≻ 0 is imposed.

The candidate still depends on R1, as the investigator says. R3 (M1 declared and held fixed under the nulls) carries more weight than reported: it now decides two clauses, the N_hab margin and N_ex survival. Statuses below are self-review only; none of this is independently checked.

ATTACKS (evidence → outcome)

A1. Independent reconstruction of Π^c.
- Method: my own coefficient-row code, written from scratch (not pc.py/pcg.py), with exact conditioning on a 71-round η path.
- Result at g = 0.05: r(A) = 24.49892604, closed form 24.49892604, relative difference 1.5e-15. At g = 0: 28.5.
- Π^c is diffusive and compound symmetric (deviation 2e-13). α = 4.2026e-3, v = 0.102959.
- Negative control: the closed form at g = 0.06 gives 23.76, so the check can fail.
- I also re-derived Prop P (steps 1-5) and the Prop N inequalities by hand.
- Selected regions, analytically: sub-blocks have r = (ε+ma)/(ε+(4−m)a), which is 1 or 2.709. Regions meeting both niches have r ≤ 1, using the niche-indicator difference as test vector.
- Outcome: confirmed (computed; proved for Prop P).

A2. Is N_ex applicable?
- prop:fw-performative(b) (s02_framework.tex:101) says an act set from beliefs is both a message and an intervention, and "the correct receiver uses both terms." PN members use only the intervention term.
- In the base process: the member's estimate has MSE 0.0832089, equal to P^+. The exact Var(η_t | the member's own information set, past U included) is 0.0815477. Adding U(t) gives 0.0791596.
- U(t) = −gn·m̄^+(t), so it reveals the niche-average posterior.
- Negative control at g = 0: the three numbers agree.
- Outcome: the investigator's "N_ex inapplicable, proved" is refuted (computed). The members' filters are exact only under a model in which the acts are exogenous.

A3. Survival under N_ex.
- Method: members' beliefs are exact conditional means given all their data, U included, under the true joint law (sequential exact conditioning).
- Π^c is diffusive and compound symmetric with r_ex(A) = 6756.48. Windows with T = 70 and T = 80 agree to 1e-9.
- Negative control at g = 0 reproduces 28.5.
- Sub-blocks are at about 3.0, below 5.075, so {A,B} is selected at every r0 in the window.
- Outcome: PN survives the S clause (computed), under R3.
- Risk (conjecture, not computed): if the null's own baseline were recomputed, the exact-fusion M1 would very likely also be far above 24.5. No declared r0 would then be admissible.

A4. Agency index at the population's precision.
- Check13 sets one precision γ = 300 for attention and acts (σ_E² = 2.4225e-4).
- With the declared class γ_C ∈ [0,6]: index 0.0391, which fails A0 = 0.94.
- With γ_C ∈ [0,1500]: 0.9658.
- Using PN's stated act rule (mean −g m_j^+) as the actual law: 0.9687.
- Decision states with m_C drawn from its stationary law (sd 0.357): 0.9639.
- Negative control with deviations ×30: 0.030.
- Discrete declared model recomputed: pooled index 0.94737 (matches), per-state median 0.961, minimum 0.819.
- Literal issue: def:agy-group-model (05_agency.tex:157) and def:agy-joint-acts (s05_agency.tex:147) define group models over finite policy sets. PN's acts are continuous, so the continuous index is an extension (interpretive).
- The discrete figure concerns a declared model, not PN's own act law. The manuscript says this of the two-firms example (s10a_meta_agents.tex:143), and rem:agy-h1-status (s05_agency.tex:267) accepts that practice.
- Outcome: the clause passes only after the class is re-declared with unbounded γ_C, or under the discrete-model precedent with margin 0.0074 over A0.

A5. Closure and Q^n ≻ 0.
- In the canonical channel-level partition (def:col-partition, 04_collectives.tex:17-24), the relay channels are internal variables and the beliefs are noiseless. So Q^n ≻ 0 (05_agency.tex:16) fails, PN does not fit eq:agy-interior, and d_cl > 0 (infinite with noiseless beliefs).
- d_M = 0 still holds, and the clause needs only d_M (05_agency.tex:21).
- In the agent-level description, where relay noise counts as internal noise, Q^n ≻ 0 and d_cl = 0.
- Adding explicit belief noise q_int: r(A) = 24.4895 at 1e-6, 23.590 at 1e-4, 17.754 at 1e-3.
- α_I recomputed independently: 5.6079e-3 forward, 5.4050e-3 reverse. Matches.
- Outcome: closure passes. The upper endpoint 24.499 is not robust.

A6. The numbers behind the every-constant differ clause.
- Method: exact error rows, with the second moment averaged over sampled attention sequences.
- N_hab annealed: 4.372 and 4.346 (1500 sequences per seed; this is exact for N_hab). Investigator: 4.409.
- M1 with acts: 5.0775 and 5.0746, approximating P(a|η) by P(a). Investigator: 5.0754.
- M1 without acts: 6.861. Investigator: 6.8586.
- N_pr annealed with acts: 3.666. Investigator: ≤ 3.70.
- Negative control with fixed attention gives 28.5.
- Margin of M1 over N_hab: about 0.70-0.73.
- Outcome: passes (numerical).

A7. Quenched N_pr.
- Scoring non-diffusive draws as −∞ is a convention. For undefined contrast, the manuscript prescribes the MI-ratio selector (s05_agency.tex:252).
- Under that selector, the full model and every quenched draw have zero between-niche world-conditional MI, because exact filters give zero gain across niches. Every ratio is +∞, so p = 1 without a tie-break.
- Outcome: the quenched verdict is undetermined. Declare the annealed version instead ("every round" is allowed, 05_agency.tex:350). It passes: 3.666 < 5.075, p = 0.01.

A8. Literal channel latency.
- In def:fw-system (02_framework.tex:15), a relay of s_j(t) is read at round t+1. PN instead uses the within-world-step convention of prop:agy-consensus(b) (05_agency.tex:132) and ex:met-two-firms.
- With one-round-stale relays and exact 2-dimensional filters:
  - r(A) = 6.1690 (agreed by two methods); 7.4259 without acts.
  - N_hab 2.749, N_pr 2.238, M1 3.054 (4.413 without acts), r_sub 2.128.
  - Window (3.054, 6.169], with both nulls below its lower edge (margin 0.31).
- Outcome: PN survives under this reading as well (numerical). N_ex under latency was not computed.

A9. C3 counterexample.
- Case E2 recomputed independently: cross entries −0.95605, Π^c diffusive, r(C1) = 10.8551, r(C2) = 146.9612.
- E1: +0.26804, not diffusive.
- Negative control (E2 with Rc = 1): not diffusive.
- Outcome: C3 as stated is refuted (computed). The sign argument of Prop S and the EFE-corollary algebra re-derive (self-check).

A10. Other checks.
- R1 is a literal reading: tab:agy-nulls rows 348-349 make N_eff and N_inf type D only conditionally.
- N_fr gives a diagonal Π^c only when combined with N_eff (row 348). On its own, the collider remains; it still differs (heuristic).
- PN's dynamics rule u_j = −g m_j^+ differs from the group-posterior mean −g m̄ − g(1+nc)d_j. Π^c is unaffected, since only U enters it.
- Under the alternative to R2, where act randomness is left unconditioned, r rises slightly (heuristic, not computed). The 2e-4 attention residual lowers r slightly (not computed).

CORRECTIONS
1. Replace "N_ex inapplicable" with: N_ex is applicable, and PN survives it with r_ex = 6756.48 (computed, requires R3).
2. Declare the agency class with γ_C ∈ [0,∞) and habits fixed. Report 0.966 at γ = 300 as a continuous-act extension, or the discrete declared model at 0.947. State that the policy sets are infinite.
3. State the grade as r0 ∈ (5.075, 24.4]. Report d_M = 0 rather than d_cl = 0, or name the agent-level description.
4. Declare annealed N_pr.
5. Declare the admitted class. The open subset is numerical only: it holds for g below about 0.075, since at g = 0.10 the clause fails.
6. Add the within-world-step relay convention as a reading, with the latency result from A8.

WEAKEST POINTS
- R1: under the strict reading, Prop N makes PN fail N_eff.
- R3/M1: it changes the world (two components merged into one) and now decides both the N_hab margin and N_ex survival.
- Agency rests on either a declared model or a continuous extension.

FILES (scratch only; no repository or vault edits)
Folder: C:/Users/CHRISA~1/AppData/Local/Temp/claude/63c81c17e87f0010/34faeca5-ea90-45d1-8cc4-412bdf898c58/scratchpad/metaagent/attack-performative/
- Libraries: win.py, win2.py
- Checks, each with its output file: a1_reconstruct_and_nex.py (a1_out.txt), a4_agency.py (a4_out.txt), a5_timing_noise.py (a5_out.txt), a6_mixtures.py (a6_out.txt), a7_two_firms_discrete.py (a7_out.txt), a8_delay.py (a8_out.txt), a9_alphaI.py (a9_out.txt)
- All runs were single-threaded and under 10 s each.

## obstruction-theory

OBSTRUCTION THEORY FOR open:agy-meta-agent-exists (label: obstruction-theory)

VERDICT
1. C1 (coordinator's h2) is true: proved exactly (Theorem C1).
2. C3 as recorded ("Pi^c has positive entries between them") is false as a statement about every same-sign cross pair. Computed counterexamples exist, including ones with nonnegative dynamics. The obstruction C3 was meant to carry is proved in a stronger form. In the stated class the world-conditional covariance has a negative cross entry, so Pi^c is not a Z-matrix. Contrast is then undefined for every region, and the population contains no collective and no meta-agent. This is alternative form (C) of the locked target, for that class only. Pairwise positivity is proved under one explicit extra hypothesis (eigen-loading).
3. Singular consensus: I proved an exact kernel decomposition and a complete characterization of when the kernel term has positive off-diagonals.
   - Lazy ring, n=4: non-diffusive iff tau < sigma^2/2 (closed form).
   - One-shot consensus of i.i.d. inputs: every lazy ring with n>=6 is non-diffusive at every tau (support obstruction).
4. Impossibility classes I1-I5 are proved. All are class-restricted, and none settles the open problem in general.
5. None of I1-I5 obstructs the epistemic-niche route (C2), provided raw-data sharing within a niche is "transitive" (for example all-to-all). A new combinatorial obstruction (Corollary F-share) rules out non-transitive sharing patterns.

READINGS CHOSEN
- R1. Diffusive is read as in 04_collectives.tex:147-151. Contrast exists only when the whole population's Pi^c is diffusive (def:col-contrast, 04:183). So a non-diffusive Pi^c means no collective anywhere (def:col-collective, 04:215). I3 and I4 depend on this literal reading.
- R2. The world-conditional law is read as in 04:130-132. It conditions on the whole world path and on sender-side broadcast noises. Private inputs and unstored act noises are not conditioned on.
- R3. Acts follow a_j(t) = -g_j m_j(t) + nu_j, with nu_j not stored, entering eta_{t+1} (task wording).
- R4. N_hab applicability is read from def:agy-nulls (05_agency.tex:333).

0. TOOL: Lemma Z (diffusivity tests). Status: proved.
Statement. If Pi is PD and diffusive, then Sigma = Pi^{-1} satisfies:
- (Z1) Sigma >= 0 entrywise.
- (Z2) Sigma_ij > 0 iff i and j lie in one connected component of the coupling graph {a_ij > 0}.
- (Z3) Sigma_ij Sigma_jk <= Sigma_ik Sigma_jj for all distinct i, j, k.
- (Z4) Every principal submatrix of Sigma has a Z-matrix inverse.
Proof.
- Write Pi = sI - B with s = max Pi_ii and B >= 0 symmetric. PD gives rho(B) = lambda_max(B) = s - lambda_min(Pi) < s.
- Then Sigma = sum_k B^k / s^{k+1} >= 0, positive exactly on the components of B's graph. This gives Z1 and Z2.
- A Schur complement Pi_SS - Pi_SR Pi_RR^{-1} Pi_RS of a PD Z-matrix is again a PD Z-matrix, because Pi_SR <= 0 and Pi_RR^{-1} >= 0 by Z1. It equals (Sigma_SS)^{-1}, which gives Z4.
- For S = {i,j,k}, (Sigma_SS^{-1})_ik = (Sigma_ij Sigma_jk - Sigma_ik Sigma_jj)/det <= 0, which gives Z3.
Use. Any negative world-conditional covariance makes Pi^c non-diffusive. So does a zero covariance between two agents that are both positively correlated with a third.
Check: support_test.py. 300 diffusive draws gave 0 violations of Z1-Z3. Negative control: random positive covariances violate Z3 in 276/300 draws.

1. PART (1): EXCHANGEABLE BLOCKS AND D + G V G^T

Theorem C1. Status: proved.
Hypotheses: Sigma_CC = alpha I_n + beta 11^T, alpha > 0, beta >= 0, Sigma_{C, V\C} = 0.
Conclusions:
- Pi_CC = alpha^{-1} (I - beta/(alpha + n beta) 11^T), and Pi_{C, V\C} = 0.
- Every pair in C has coupling a = beta/(alpha(alpha + n beta)); every member has leak eps = 1/(alpha + n beta).
- If (Sigma_{V\C, V\C})^{-1} is diffusive, then Pi^c is diffusive and r(C) = 1 + n beta/alpha.
Proof:
- The formula for Pi_CC is Sherman-Morrison.
- cut(C) = 0, so xout = mean leak = 1/(alpha + n beta) (04:185).
- On 1_C^perp, diag(eps) + L_C = (eps + n a) I = alpha^{-1} I, so xin = 1/alpha.
Negative control: beta in (-alpha/n, 0) gives off-diagonal -beta/(alpha(alpha + n beta)) > 0.
Baseline (clause (c), mean coupling, 04:202), k equal blocks:
- The baseline 1 + k n (n-1) beta / ((k n - 1) alpha) is attained by the whole comparison population, because regions of size m < N have (eps + m a)/(eps + (N - m) a) < 1 + N a/eps.
- For k = 2 each block is a collective at every beta > 0. The significance tends to (2n-1)/(2(n-1)) as beta/alpha grows.
Computed (c1_factor.py), alpha=1, beta=0.5, n=4: coupling 1/6, leak 1/3, r = 3.000000000000. With two such blocks the baseline is 2.714286 and the significance 1.105.

Theorem F (factor model). Status: proved.
Setup: Sigma = D + G V G^T with D = diag(d) > 0 and V > 0 (m x m). Let g_i be the rows of G and K = (V^{-1} + G^T D^{-1} G)^{-1}.
- (a) Exact formulas: Pi_ij = -g_i^T K g_j / (d_i d_j) for i != j, and D Pi 1 = 1 - G K G^T D^{-1} 1 (Woodbury).
- (b) If G >= 0 and V^{-1} + G^T D^{-1} G is a Z-matrix, then off-diag(Pi) <= 0. Reason: K >= 0 by Z1. This covers m = 1 with any one-signed G.
- (c) Disjoint supports (each agent loads on at most one factor, positive loadings): off-diag(Pi) <= 0 at every loading scale s iff V^{-1} is a Z-matrix (the factor law is MTP2; Karlin and Rinott 1983 give the Gaussian characterization). Necessity: K = s^{-2} S~^{-1} - s^{-4} S~^{-1} V^{-1} S~^{-1} + O(s^{-6}) with S~ diagonal positive.
- (d) If G c = 1 for some c, then D Pi 1 = G K V^{-1} c, since G K G^T D^{-1} G c = G K (K^{-1} - V^{-1}) c. Hence unit indicator loadings with a diffusive V^{-1} give a diffusive Pi.
- (e) Single factor (m = 1, G >= 0): off-diag(Pi) <= 0 always. Leaks are >= 0 iff max_i g_i <= (1/v + S2)/S1, where S1 = sum_j g_j/d_j and S2 = sum_j g_j^2/d_j. Equal loadings always satisfy this.

Corollary F-share (independent sources, raw-data sharing). Status: proved, via Z2.
- Setting: V diagonal and G >= 0. Let S_i be the set of sources agent i loads on.
- Diffusivity requires the relation "S_i and S_k intersect" to be transitive.
- Application to raw-data sharing without relaying: if members i and k share no source while both share a source with some j, then Pi^c is not diffusive.
- All-to-all sharing within a niche makes the block exchangeable with beta >= 0, so it is diffusive by C1.
- Diffusivity persists on an open neighborhood of any strictly diffusive point, within the class that keeps classes independent (continuity of matrix inversion).

Counterexamples with G >= 0 (exact values, c1_factor.py):
- CE1 (single factor, row-sum failure): g = (1, 0.1), d = (1, 1), v = 20. Leak of agent 1 = -0.0377.
- CE2 (overlap collider): V = I_2, g1 = (1,0), g2 = (0,1), g3 = (1,1), D = I. Pi = (1/8)[[5,1,-2],[1,5,-2],[-2,-2,4]], so Pi_12 = +1/8. Negative control: removing agent 3 gives a diffusive Pi.
- CE3: disjoint supports with V_12 = -0.5. Pi_13 = +0.0625.
- CE4: disjoint supports, V tridiagonal with off-diagonal 0.6. V >= 0 entrywise but (V^{-1})_13 = 1.286 > 0. With loadings 3I, Pi_13 = +0.070.
- The sufficient conditions (b), (c) and (d) gave 0 violations in 500, 300 and 500 random draws.

2. PART (2): COLLIDER

Setting LG-act.
- Agents, given the conditioning set: x_{t+1} = A x_t + u_t + xi_t, where u_t is conditioning-measurable and xi ~ N(0, Q), Q > 0.
- World: eta_{t+1} = F eta_t + B x_t + omega_t, where B is the act loading (for a_j = -g_j m_j + nu_j, B = -[B_j g_j]), and omega ~ N(0, Q_w) > 0 collects the world innovation plus unstored act noise, independent of xi.
- The closed loop is stable, and the act-free dynamics are stable on the actors and their ancestors.

Lemma C3-a (path precision). Status: proved.
- Statement: given x_0 and eta_{0:T}, the path x_{1:T} is Gaussian with precision P = J_{1:T} + sum_{t=1}^{T-1} E_t^T B^T Q_w^{-1} B E_t.
- J_{1:T} is the precision of the act-free chain: diagonal blocks Q^{-1} + A^T Q^{-1} A, lag blocks -Q^{-1} A and -A^T Q^{-1}.
- Proof: as a function of x, the conditional density is the joint density, and the world transition contributes -1/2 |eta_{t+1} - F eta_t - B x_t|^2 in the Q_w^{-1} metric.
- The added term is PSD and time-local. For one conditioned direction (B = e b^T, q = 1/(e^T Q_w^{-1} e)) its equal-time entries are b_i b_j / q.
- In the bi-infinite case P is the Laurent operator with symbol J(theta) + B^T Q_w^{-1} B, where J(theta) = (e^{i theta} - A)^H Q^{-1} (e^{i theta} - A).
- J itself is not a Z-matrix: the common-listener entries (A^T Q^{-1} A)_ij are >= 0. So no M-matrix argument on paths transfers to one time. This is exactly where time-marginalization changes signs.

Lemma C3-b (one-time identity). Status: proved.
- Statement: Pi^c = Pi_0 + B^T Q_w^{-1} B + I_other, with I_other PSD. Here Pi_0 is the world-conditional precision with the acts' effect on eta removed, which equals Pi^c under N_eff (05:348).
- Reduction: let x~ be the act-free process driven by xi alone, and y~_t = B x~_t + omega_t. A stable closed loop gives sigma(eta_Z) = sigma(y~_Z), so Sigma^c = Cov(x~_0 | y~_Z).
- Finite windows W containing 0: Cov(x~_0 | y~_W)^{-1} = Sigma_0^{-1} + G_W^T Cov(y~_W | x~_0)^{-1} G_W. Cov(y~_W | x~_0) is block diagonal between time 0 and the rest, because omega_0 is independent of everything else. That isolates B^T Q_w^{-1} B.
- Limit: let W increase to Z (L^2 martingale convergence).
- Computed: the smallest eigenvalue of I_other over 200 signed draws is 1.05e-10.

Theorem C3 (collider obstruction). Status: proved.
Hypotheses:
- One conditioned direction (B = e b^T).
- Null independence: U = U1 ⊔ U2 ⊔ U3 (actors plus their ancestries), where no agent of one U_k reads an agent of another, directly or through chains, and Q is block diagonal across the U_k.
- b restricted to U1 and to U2 is nonzero.
Conclusion:
  Cov(b1^T x^{U1}_t, b2^T x^{U2}_t | eta) = -(1/2pi) ∫ beta1 beta2 / (q + beta1 + beta2 + beta3) dtheta < 0,
  where beta_k(theta) = b_k^T J_k(theta)^{-1} b_k > 0.
If in addition b >= 0 on U1 ∪ U2 (one sign) and b loads on the coordinates on which contrast is computed:
- some entry Sigma^c_ij < 0 with i in U1 and j in U2;
- by Lemma Z, Pi^c is not a Z-matrix (it has a positive off-diagonal entry);
- so no set of agents of the population is a collective or a meta-agent.
Proof:
- The smoothing-error spectral density, S_x~ - S_x~y~ S_y~^{-1} S_y~x~ (orthogonal projection onto the closed span of the y~ path), equals (J + b b^T / q)^{-1} by Woodbury.
- J is block diagonal by null independence. Sherman-Morrison gives the cross block -J1^{-1} b1 b2^T J2^{-1} / (q + sum_k beta_k).
- Contracting with b1 and b2 leaves a real integrand. The one-time covariance is the frequency average.
Why the aggregate works and the pair does not: beta_k is the real spectral density of group k's scalar act output, while a pairwise entry involves complex cross-spectra of non-act coordinates with that output.

Corollary (mirror groups). Status: proved. If U1 and U2 are isomorphic (same J, b and contrast functional f >= 0), then Cov(f^T x^1, f^T x^2 | eta) = -∫ |f^T J^{-1} b|^2 / D < 0, whatever coordinates the acts load on (for example stored acts).

Theorem C3-pair (eigen-loading). Status: proved.
Hypothesis: J_k(theta)^{-1} b_k = rho_k(theta) b_k with rho_k > 0. For example, b_k is a joint eigenvector of A_k, A_k^T and Q_k with a real eigenvalue, as for homogeneous groups with uniform acts or with complete-averaging consensus.
Conclusion: every cross block is Pi^c_{U_k U_l} = kappa_kl bhat_k bhat_l^T with kappa_kl > 0.
Proof:
- S - S_0 = -Phi omega omega^T Phi^T / D, with Phi = [bhat_k] orthonormal and omega_k = rho_k |b_k|.
- So Sigma^c = [diag(sigma) - C] on span(Phi), plus Sigma_0 restricted to span(Phi)^perp, where C = (1/2pi) ∫ omega omega^T / D is entrywise positive.
- diag(sigma) - C is a PD irreducible Z-matrix, so its inverse is entrywise positive. The complement part is block diagonal across groups.
Special cases: non-communicating scalar actors (Sigma^c is then itself an M-matrix and all actor pairs are positive), and N = 2.
Computed (eigenload.py, 300 draws): rank-one cross blocks to 3e-14 with kappa > 0. Negative control (generic loadings): sigma2/sigma1 up to 0.54, so the cross blocks are not rank one.

Refutation of pairwise C3 without eigen-loading. Status: refuted, computed.
- collider_conj.py, 2531 draws with A >= 0 within groups, one-sign b and null independence: 13 draws have an acting cross pair with Pi^c_ij <= 0.
- Worst instance: 8 agents in groups {0,1,2}, {3,4,5,6}, {7}. Pi^c_{2,5} = -1.859 with b_2 = 0.377 and b_5 = 0.306.
- With signed A: 23 of 343 draws, for example Pi^c_{1,3} = -0.146.
- In every draw (3537 in total) the proved part held and the cross block contained a positive entry.
- b1^T Pi^c_12 b2 > 0 held in 2531/2531 draws. Status: conjecture, unproved.

Need for null independence. Status: computed.
- A common source (agent 0 read by actors 1 and 2) restores diffusivity. Instance: (Pi_0)_12 = -0.177 (attractive) and Pi^c_12 = -0.019.
- Whether "no attractive coupling", (Pi_0)_ij = 0, suffices without null independence: open. A search over 2943 reversible chain draws (actors at distance 3, (Pi_0)_03 = 0) found no diffusive instance.

Validation.
- The spectral integral equals the steady-state RTS smoother covariance to 2e-14.
- ex:agy-collider (s05_agency.tex:240-242) is reproduced: window MI 1.391e-3 nats (manuscript 1.39e-3); stationary Pi^c_12 = +0.102.

Scope. ex:met-two-firms stores each firm's order flow and uses it in the filter, so xi and omega are correlated and the acts load on lagged coordinates. The firms are not mirror images, so C3 does not literally cover that example; the manuscript's computation remains the evidence there. My complete-averaging two-firm analogue (unstored, same-round acts) gives cross entries +0.0385, comparable to the manuscript's 0.03.

3. PART (3): SINGULAR CONSENSUS

Proposition S. Status: proved.
- Setup: Y = W X + delta with Sigma_X > 0 and delta ~ N(0, tau I) independent. Let K = ker W^T and P_K its orthogonal projector.
- Statement: Pi_Y = tau^{-1} P_K + R_tau, where R_tau = [(W Sigma_X W^T + tau I) restricted to range W]^{-1} (zero on K), 0 <= R_tau <= R_0, and ||R_tau|| <= 1/(s_min^2 lambda_min(Sigma_X)).
- Consequence: Pi_Y,ij > 0 whenever (P_K)_ij > 0 and tau < (P_K)_ij s_min^2 lambda_min(Sigma_X).
- Proof: R^n = ker W^T ⊕ range W orthogonally. Cov(Y) equals tau I on ker W^T and maps range W into itself.

Proposition S-char. Status: proved.
- General statement: P_K is a Z-matrix iff K = ⊕_c (p_c^perp within block c) ⊕ span{e_i : i in S}, for a partition into blocks, positive weight vectors p_c, and a set S of singletons.
- If 1 is orthogonal to K (symmetric doubly stochastic W): P_K is a Z-matrix iff K is the direct sum of the zero-sum spaces of the blocks of a partition, that is, W does complete averaging within blocks.
- A one-dimensional kernel spanned by v ⊥ 1 gives a positive entry iff v has at least three nonzero entries.
- Proof: a PSD idempotent Z-matrix splits into irreducible parts. An irreducible part with a zero eigenvalue is I - p p^T/|p|^2 with p > 0 (Perron); otherwise it is I, possible only for singletons.
- Checked on 300 + 300 random draws.

Lazy ring W = 1/2 I + 1/4 (S + S^{-1}), with Sigma_X = sigma^2 I.
- The kernel is nontrivial iff n is even: v_i = (-1)^i and (P_K)_ij = (-1)^{i-j}/n.
- n = 4 (proved): Pi_13 = (1/4)[1/(sigma^2 + tau) - 2/(sigma^2/4 + tau) + 1/tau], which is positive iff tau < sigma^2/2. Pi_12 < 0 and row sums are 1/(sigma^2 + tau), so the output is diffusive iff tau >= sigma^2/2. At tau = 1e-3, Pi_13 = 248.26.
- n >= 6 (proved): Sigma_Y vanishes at ring distance >= 3 but is positive at distance <= 2, so Z2 gives non-diffusive at every tau > 0.
- n = 5 (numerical, grid): non-diffusive at tau = 1e-3, diffusive above tau ≈ 0.81 sigma^2.
- n = 3: diffusive at every tau.
- Negative controls: complete averaging 11^T/n, (1-w)I + w 11^T/n, and the pair 11^T/2 are diffusive at every tau. Complete averaging gives an exchangeable block with contrast 1 + sigma^2/tau (1001 at tau = 1e-3).

Proposition S-dyn. Status: proved.
- Statement: suppose that in the world-conditional law the component v^T x' of the members' consensus states is independent of every other coordinate of the one-time vector. Then Pi^c on those coordinates is v v^T / Var(v^T x') plus a part supported on v^perp and the other coordinates.
- Sufficient conditions (I):
  - (I-a) every member applies the same update map, with symmetric W;
  - (I-b) data enter only through W, so P_K W = 0;
  - (I-c) every other variable, the world included, reads member states only through functionals vanishing on K (for example sums).
- Under (I), Var(v^T x') = tau/(1 - a_K^2).
- Computed: one firm of 4 members with a lazy ring and a_K = 0.63 gives Pi^c_13 = 138.6, against a kernel term of 150.8. Under complete averaging the firm is diffusive.
- The consensus filter of prop:agy-consensus(b) (05:132) as used in ex:met-two-firms (s10a_meta_agents.tex:109) satisfies (I) for n_c >= 1: F, Pbar and Lambda^s are common, and the order flow is a sum. The value 157 was not recomputed.

4. PART (4): IMPOSSIBILITY CLASSES

I1 (own comparison medium). Status: proved.
- Statement: if Pi^c is diffusive and equals its comparison medium (couplings constant on each averaging class, uniform leak), no region is a collective.
- Proof: r_hom_bar is the supremum over regions of the population, so it is >= r(C), while 04:217 requires r(C) >= r0 > r_hom_bar.
- Covers: equal cliques with equal couplings under the graph clause (s04_collectives.tex:147), permutation-invariant closed populations under clause (c), and translation-invariant tori.
- Computed over all 247 regions (n=4, a=1, eps=0.1):
  - clause (b): baseline 41 equals the clique contrast, and no region exceeds it;
  - clause (c): baseline 35.286, both cliques are collectives with significance 1.162, matching s04:147.
- Negative control: couplings 1.5 and 0.5 under clause (b) give r = 61 > 41 for the stronger clique.

I2 (closed populations, clause (c) mean coupling).
- (a) The whole population is never a collective: prop:col-whole-population(b) (s04:157). Cited, re-checked on 150 draws.
- (b) Necessary condition. Status: proved. If C is a collective then (eps_max_C + lambda2(L_C))/epsbar_C > 1 + N abar/epsbar. With uniform leak this means lambda2(L_C) > N abar, hence mean internal coupling abar_C > (N/n) abar.
- Proof: xin <= eps_max + lambda2, xout >= epsbar_C, and lambda2 <= tr L_C/(n-1) = n abar_C.
- Checked: 9 collectives found, 0 violations.

I3 (performative populations). Status: proved (Theorem C3).
- Class: two null-independent actor sets that act with one sign on one conditioned scalar direction. The acts load on contrast coordinates in the same round (or the groups are mirror images), and noise is private per agent.
- Conclusion: no collective, hence no meta-agent.
- The sets need not be collectives. Two independent same-sign single actors suffice, even inside one candidate.
- Negative control, opposite signs (buyer/seller): two firms with complete averaging and opposite-sign acts give a diffusive Pi^c. Firm contrasts are 77.19 and 95.77 against a clause-(c) baseline of 75.07, so both are collectives. Their other meta-agent clauses are unchecked.
- Negative control, no acts: diffusive.

I4 (singular consensus). Status: proved (Propositions S, S-char, S-dyn).
- Under (I), a group whose W-kernel contains a vector with two same-sign entries (for example a lazy ring with n even >= 4) is non-diffusive below an explicit threshold in tau.
- One-shot lazy rings with n >= 6 are non-diffusive at every tau.

I5 (habit dichotomy). Status: proved from 05:333, 05:240-246 and tab:agy-nulls (05:351).
- (a) If no policy is selected by EFE: N_hab is inapplicable, members act by habit, the denominator of the agency index vanishes, and the index is 1 for every admissible class.
- (b) If some policy is selected by EFE: N_hab applies. If at some selector constant the partition is the same at gamma and at gamma = 0 on the admitted class (for example Pi^c does not depend on the selected policies), C fails the differ clause.
- Illustration (mean-field attention; interpretive): EFE-selected in-niche attention gives pairs {0,1} and {2,3}; the habit null gives none.
- Interpretive flag: (a) is a degenerate literal pass of the agency clause. The wording at s05:296 ("agency holds only because the members act by habit") suggests the author does not count it, but the locked target does not exclude it. If exclusion is intended, add the condition sum_X w_X KL(P(.|X) || E) > 0.

5. COORDINATOR HYPOTHESES (h1)-(h4)
- (h1) Confirmed as a reading.
  - def:agy-meta-agent (05:379-381) requires neither acts nor consensus.
  - The agency index (05:240-246) uses group models whose policies open "exterior-facing sensory channels" (05:157); acts enter only via def:agy-joint-acts (s05:146-152).
  - The two firms' failure mechanisms are general: I4 covers the consensus mechanism; I3 covers the collider only in its clean form.
- (h2) Proved (Theorem C1).
- (h3) Confirmed.
  - Exact fusion is defined as the conditional law of the message given (eta, Z_i) (02_framework.tex:141). For fresh raw data read with the true code and noise R_j + R_c, it equals the literal level-0 likelihood, so N_ex leaves the model literally unchanged.
  - N_ex is then inapplicable (05:333), or trivially survived if read as applicable. The verdict is the same under either reading.
  - Caveat: this fails if the same datum reaches a receiver by two routes (relaying).
  - Theorem F and Corollary F-share answer open:col-exact-fusion for raw-data fusion; CE2 shows such fusion can be non-diffusive.
- (h4) Confirmed and formalized as I5 and I1. On "for each constant of the selector": if the null selects C at any admissible constant, the differ clause fails at that constant. Records are not used anywhere here.

6. WHAT RAN
- Python 3.14, single-threaded, each script under one minute, no background runs. Every check declared its expected outcome; none differed.
- Directory: C:/Users/CHRISA~1/AppData/Local/Temp/claude/63c81c17e87f0010/34faeca5-ea90-45d1-8cc4-412bdf898c58/scratchpad/metaagent/obstruction-theory/
- Scripts: common.py, c1_factor.py, collider.py, collider_conj.py, chain_test.py, consensus.py, ring_threshold.py, impossibility.py, eigenload.py, support_test.py.
- Outputs: *_output.txt for each script, plus common_source_null.txt.
- No repository or vault file was edited.

7. STRONGEST RESULT, OPEN OBLIGATIONS, NEXT ACTION
- Strongest result. Lemma Z together with Theorem C3 is a proved impossibility of form (C) for class I3. Two independent same-sign actors on one conditioned scalar world direction make Pi^c non-diffusive, so no meta-agent exists anywhere in such a population.
- Constructive by-products: C1, Theorem F, the overlap/support criterion, the opposite-sign escape from I3, and the observation that complete averaging is diffusive.
- Open, needed to cover ex:met-two-firms literally:
  - extend C3 to correlated act noise (stored acts used in filters);
  - extend C3 to act loadings of rank greater than one.
- Open, secondary:
  - b1^T Pi^c_12 b2 > 0 (conjecture);
  - whether (Pi_0)_ij = 0 can replace null independence.
- Reading decision needed: the habit degenerate pass (I5a).
- For the open problem, the next action that would most change the answer is on the construction side: compute the clause-(c) mechanism baseline and the N_pr test for an all-to-all two-niche C2 instance. That design avoids I1-I5 when all of the following hold:
  - no same-sign actors with independent ancestries;
  - no kernel-mixing consensus;
  - transitive sharing (attention budget kappa >= niche size - 1);
  - an EFE-selected structure.

## literature

## Verdict

I found no source that settles open:agy-meta-agent-exists (s05_agency.tex:295-297). No source uses criteria equivalent to def:agy-meta-agent (05_agency.tex:379-381), and none exhibits a meta-agent in its sense.

Two of the record's claims are partly known already:
- **C1.** The M-matrix (MTP2) part is a special case of the classical one-factor result (Wermuth & Marchetti 2014, Lemma 1; Fallat et al. 2017, Sec. 1).
- **C3.** The static mechanism is Gaussian explaining away (Chen & Pearl; Epskamp et al.). Fallat et al. 2017, Thm 5.3 (upward stability) excludes it from MTP2 laws.

The single-time dynamic form of C3 that the two-firms example needs is not in the literature I read. The M-matrix closure results prove it only under a hypothesis that fails whenever members of one collective share a listener or act with one sign (D3).

The epistemic mechanism behind C2 is also prior art. In thm:agy-agency(d) under (P0) (05_agency.tex:202), the epistemic part coincides with Choi & Lee 2015, Lemma 1: conditional mutual-information utilities form an exact potential game whose potential is the joint mutual information. The manuscript does not cite this paper.

No scripts were run. Hand derivations are labeled below. No repository or vault file was touched.

## Flags (prior art for C1, C3 and the agency clause)

- **F1 (C1).** Compound symmetry αI+β11ᵀ with β>0 is the equal-loading case of a positive one-factor model.
  - Its precision is a complete M-matrix (Wermuth & Marchetti Lemma 1; Fallat et al. Sec. 1; LUZ 2019 p. 22).
  - The leak (row-sum) part and the value r=1+nβ/α are not stated in the sources found, but each is a one-line Sherman–Morrison computation (D1).
  - The diffusive class itself is known as DDGL (Egilmez et al. 2017) or as the loopy Laplacian (Dörfler & Bullo 2013). Its closure under marginalization (lem:col-kron, s04_collectives.tex:279-283) is Dörfler–Bullo Lemma 2.1, already in references.bib.
- **F2 (C3).** The static sign rule is classical. Conditioning on a common child with path coefficients a, b induces conditional covariance −ab (Chen & Pearl).
  - So same-sign loadings give a positive precision entry, and opposite signs give an attractive one.
  - MTP2 laws are upward-stable (Fallat Thm 5.3), so no law with this collider pattern is MTP2.
  - Status: known for the static case. The dynamic single-time case is open (D3).
- **F3 (agency).** Choi & Lee Lemma 1 equals the epistemic potential of thm:agy-agency(d) under (P0); Marden et al. 2009 give the general marginal-contribution version.
  - Krause & Guestrin 2005 (Cor. 4: information gain is submodular under conditional independence given the state) gives the ≤0 epistemic sign of prop:agy-performative-sign (s05_agency.tex:191-197). This uses the slot assumption at 05_agency.tex:157.
- **F4 (group-agency definitions).**
  - Recent formal tests use weaker criteria and certify none of the manuscript's clauses:
    - blanket existence (Kirchhoff 2018, Palacios 2020, Maisto 2025);
    - a fitted group model (Waade 2025, Heins 2026);
    - causal abstraction with "non-trivial" agents (Jørgensen et al. 2026).
  - Heins et al. 2023 and Jørgensen et al. 2026 (Prop. 16) are the only fragility or non-emergence results found, each under its own definition.

## Sources

Read depth: F = full main text; P = the sections or pages named; A = abstract only; N = not read. "New" means the source is not in Collective_Agents/references.bib.

### (i) M-matrix precision (MTP2), closure under marginalization and conditioning, Schur complements

1. **Fallat, Lauritzen, Sadeghi, Uhler, Wermuth, Zwiernik, "Total positivity in Markov structures", Ann. Statist. (2017).** DOI 10.1214/16-AOS1478; arXiv:1510.01290. Read: F (arXiv v2; reference list truncated). New.
   - Sec. 4.1: a Gaussian law is MTP2 iff its precision K has k_vv>0 and k_uv≤0 (attributed to Karlin–Rinott 1983).
   - Prop. 3.4: MTP2 is closed under conditioning (a.e.) and under marginalization (the latter credited to Karlin–Rinott 1980, Prop. 3.2).
   - Thm 5.3: the independence model of any MTP2 law is upward-stable (u⊥v|C ⇒ u⊥v|C∪{w}) and singleton-transitive.
   - Sec. 1: single-factor models with positive dependence on the factor are MTP2.
   - Bearing: supports proof steps (closure, C1 sign part). Gives the structural form of the C3 obstruction.
2. **Karlin & Rinott, Linear Algebra Appl. 52–53 (1983) 419–438.** DOI 10.1016/0024-3795(83)80027-5. Read: A. New.
   - Statement: N(0,Σ) is MTP2 iff Σ⁻¹ is an M-matrix; equivalent partial-correlation characterizations.
   - Bearing: primary source for that characterization.
3. **Karlin & Rinott, J. Multivariate Anal. 10 (1980) 467–498.** DOI 10.1016/0047-259X(80)90065-2. Read: N (no access); cited only through Fallat Prop. 3.4.
4. **Lauritzen, Uhler, Zwiernik, Ann. Statist. 47(4) (2019).** DOI 10.1214/17-AOS1668; arXiv:1702.04031. Read: P (pp. 1–8, 19–28). New.
   - Secs. 1–2: Gaussian MTP2 iff K is a symmetric M-matrix; MTP2 Gaussian graphical models sit inside non-frustrated ones, which sit inside walk-summable ones.
   - Sec. 5, Thm 5.2: a law is signed MTP2 iff every cycle of G(K) satisfies (−1)^k K_{i1i2}⋯K_{iki1}>0 (balance).
   - Thm 5.4: hidden-variable Gaussian trees are signed MTP2.
   - p. 22: the one-factor model is a star tree with hidden center; its MTP2 members are Spearman models.
   - Bearing: supplies the balance test used in D2 and a sign-gauge tool for C3.
5. **Carlson & Markham, "Schur complements of diagonally dominant matrices", Czech. Math. J. 29 (1979) 246–251** (dml.cz/dmlcz/101601). Read: F. New.
   - Sec. 2: for a Z-matrix, A is an M-matrix iff A[α] and A/A[α] are (the Schur-complement direction is credited to Crabtree 1966, not read).
   - Thm 1: principal submatrices and Schur complements of strictly diagonally dominant matrices are diagonally dominant.
   - Bearing: supports proof steps (D3, D4).
6. **Dörfler & Bullo, IEEE TCAS-I 60(1) (2013) 150–163.** DOI 10.1109/TCSI.2012.2215780; arXiv:1102.2950. Read: P (pp. 1–6). Already in references.bib (dorfler2013kron).
   - Lemma 2.1 (arXiv numbering): the Schur complement of an irreducible loopy Laplacian is a loopy Laplacian.
   - Bearing: prior art for the diffusive part of lem:col-kron.
7. **Egilmez, Pavez, Ortega, IEEE JSTSP 11(6) (2017).** DOI 10.1109/JSTSP.2017.2726975; arXiv:1611.05181. Read: P (pp. 1–4). New.
   - Sec. II-B: L_d = {L⪰0, L_ij≤0, L1≥0}, the "attractive diagonally dominant GMRF" class (Fig. 1).
   - Bearing: naming. The positive definite case of "diffusive" (04_collectives.tex:147-151) is this class, strictly inside MTP2.

### (ii) Explaining away for Gaussian common effects

8. **Chen & Pearl, "Graphical tools for linear SEM", UCLA TR R-432 (2014; DTIC ADA609131).** Read: P (d-separation passage). New.
   - Fig. 6a discussion: σ_XY·Z = σ_XY − σ_XZσ_ZY/σ²_Z = −ab for uncorrelated parents with unit variances.
   - Bearing: gives the static C3 sign.
9. **Epskamp, Waldorp, Mõttus, Borsboom, Multivariate Behav. Res. 53(4) (2018) 453–480.** DOI 10.1080/00273171.2018.1454823; arXiv:1609.04156. Read: P (the "note on common effects"). New.
   - Statement: two positive effects on a conditioned common child yield a negative partial correlation, i.e., an edge of unexpected sign in the graphical model.
   - Bearing: same rule, stated in graphical-model terms.
   - The manuscript already has this mechanism in ex:col-non-diffusive(a) (s04_collectives.tex:124) and ex:agy-collider (s05_agency.tex:240-242).

### (iii) One-factor models, compound symmetry and the sign of precision off-diagonals

10. **Wermuth & Marchetti, Electron. J. Statist. 8 (2014).** DOI 10.1214/14-EJS884; arXiv:1307.5396. Read: P (pp. 1–8 of 21). New.
    - Eq. (6): P = Δ+λλᵀ and P⁻¹ = Δ⁻¹−δδᵀ.
    - Lemma 1: with proper positive loadings, P⁻¹ is a complete M-matrix (all off-diagonal entries negative).
    - Lemma 2 (after Ostrowski): inverses of all principal submatrices are complete M-matrices.
    - Lemma 3: all partial correlations are positive for every conditioning set.
    - Bearing: prior art for the sign part of C1.

### (iv) Collective agency in active inference and the free energy principle

11. **Kirchhoff, Parr, Palacios, Friston, Kiverstein, J. R. Soc. Interface 15 (2018) 20170792.** DOI 10.1098/rsif.2017.0792. Read: F. Already cited.
    - Sec. 3.1: any system with a blanket performs "mere" active inference.
    - Sec. 3.2: "adaptive" active inference needs a temporally deep generative model.
    - Sec. 4: an ensemble that has its own blanket and is operationally closed and adaptive is autonomous.
    - Sec. 5: the authors state that they have not shown such nesting emerges.
    - Bearing: prior art only. Its criterion is blanket existence, which selects nothing (prop:col-selects-nothing, s04_collectives.tex:110-114).
12. **Ramstead, Badcock, Friston, Phys. Life Rev. 24 (2018) 1–16.** DOI 10.1016/j.plrev.2017.09.001. Read: P (Secs. 2.2, 3.1, 3.2). Already cited.
    - Sec. 3.1: the sparsity of exchanges among cells' blankets induces a blanket of blankets. This is asserted, not proved.
13. **Palacios, Razi, Parr, Kirchhoff, Friston, J. Theor. Biol. 486 (2020) 110089.** DOI 10.1016/j.jtbi.2019.110089. Read: P (pp. 1–6). Already cited.
    - Abstract and Sec. 1: nested blankets emerge in simulation when elements hold priors that they belong to a macroscopic blanket. The authors say hierarchy is not generic.
    - Bearing: existence by simulation under a weaker criterion, with the structure written into priors.
    - Since every null keeps priors (05_agency.tex:333), this is the "declared, not found" case of rem:col-declared-geometry (interpretive).
14. **Friston, Levin, Sengupta, Pezzulo, J. R. Soc. Interface 12 (2015) 20141383.** DOI 10.1098/rsif.2014.1383. Read: A plus introduction. Already cited.
    - Statement: cells self-assemble when they share a model of the target form.
    - Bearing: prior art for coordination through a shared model (the (P0) analog); no group-agency test.
15. **Heins, Millidge, Da Costa, Mann, Friston, Couzin, PNAS 121 (2024) e2320239121.** DOI 10.1073/pnas.2320239121. Read: A plus introduction. Already cited.
    - Statement: collective motion emerges from individual surprise minimization.
    - Bearing: no group-level model is tested.
16. **Heins, Klein, Demekas, Aguilera, Buckley, "Spin glass systems as collective active inference", IWAI 2022, CCIS 1721 (2023).** DOI 10.1007/978-3-031-28719-0_6; arXiv:2207.06970. Read: F (main text). Already cited.
    - Sec. 5: the exact equivalence with Glauber sampling needs symmetric mutual precisions γ(i,j)=γ(j,i) (detailed balance), a specific generative model, and asynchronous updates. Parallel updates change the stationary law.
    - Sec. 6: the higher level is a passive sampler, not an active-inference agent.
    - Bearing: closest formal precedent. It mirrors thm:agy-agency(b), (P4) and prop:agy-synchronous.
17. **Waade, P. T. et al., "As one and many", Entropy 27(2) (2025) 143.** DOI 10.3390/e27020143. Read: P (abstract, Sec. 2.3, discussion). Already cited.
    - Statement: a group is an agent if it maintains a group blanket; the method fits a POMDP model to the group's blanket states. The blanket architecture is fixed by hand.
    - Bearing: prior art for a fitted group model; this is the exogenous-structure trap of h4.
18. **Maisto, Nuzzi, Pezzulo, arXiv:2511.10835 (2025, v2 2026).** Read: A plus introduction. Already cited.
    - Criterion: an emergent flock-level blanket plus synergistic information.
19. **Heins, arXiv:2610.04415 (2026).** Read: A plus introduction. Already cited.
    - Statement: a school-level posterior is fitted from outside, with patches pooled by a natural-parameter sum. Appendix C (the expected-free-energy form of the heading) was not read.
20. **Friston et al., "Federated inference and belief sharing", Neurosci. Biobehav. Rev. 156 (2024) 105500.** DOI 10.1016/j.neubiorev.2023.105500. Read: P (belief-sharing section). Already cited.
    - Statement: gaze is driven by expected information gain; receivers add others' likelihood and prior messages.
    - Bearing: in the manuscript's terms this is literal pooling (prop:agy-pooling(b)), so N_ex would apply to it.
21. **Jørgensen, Weichwald, Hammond, "Causal foundations of collective agency", CLeaR 2026, PMLR 323; arXiv:2605.00248.** Read: P (Secs. 1–4.2, opening of Sec. 5). New.
    - Collective agency is defined through a mechanized causal abstraction in which the group is one rational agent.
    - Defs. 11–12: every mechanism is an agent under a constant utility, so only "non-trivial" agents count.
    - Prop. 16: a high-level node is not a non-trivial agent when the value map is injective and the low-level mechanisms are independent.
    - Sec. 5: voting mechanisms are graded by how well the abstraction fits (mean squared error).
    - Bearing: closest recent prior art for a graded, class-restricted test. It parallels 05_agency.tex:249-251.
22. **Orseau, McGill, Legg, arXiv:1805.12387 (2018).** Read: A plus introduction. New.
    - Statement: Bayes' rule over "agent" (described by the function it optimizes) versus "device" (an input-output map), computed from behavior.
    - Bearing: prior art for agency by model comparison, analogous to the index's comparison with the habit-only model.

### (v) Group agency in philosophy (operational criteria only)

23. **List & Pettit, *Group Agency* (OUP 2011), Ch. 1.** DOI 10.1093/acprof:oso/9780199591565.003.0002. Read: A of the chapter, plus Tuomela's review (NDPR 2011.11.38); the book itself not read. Already cited.
    - Criteria: representational states, motivational states, and a capacity to process them and intervene; rationality as consistency and effectiveness.
24. **List & Pettit, "Group agency and supervenience"** (author version dated 11 Jan 2006, LSE site; journal details not verified). Read: P (Sec. 2). New.
    - Four conditions: representational and goal states; theoretical rationality; acting on those states; holding across a class of relevant possible conditions, which the authors call robustness.
    - Bearing (interpretive): that last condition matches the open-subset, every-selector-constant reading of "differs" (05_agency.tex:333).
25. **Pettit, "How to tell if a group is an agent", in Lackey (ed.), *Essays in Collective Epistemology*, OUP 2014, 97–121.** DOI 10.1093/acprof:oso/9780199665792.003.0005. Read: A plus Sec. 4.1. New.
    - Criteria: robustness over internal realizers and over situations (his terms); exclusion of external rigging; for groups, only evidence of interpersonal interaction warrants ascribing agency.
    - Bearing (interpretive): parallels interaction necessity (05_agency.tex:294) and the h4 exogenous-structure trap.

### (vi) Epistemic group agency (the group's acts are information-gathering choices)

26. **Choi & Lee, IEEE Trans. Control Syst. Technol. (2015).** DOI 10.1109/TCST.2015.2403475; arXiv:1403.0811. Read: P (Secs. II-A, IV-A). New.
    - Lemma 1: the utilities U_i = I(V; Z_{s_i} | Z_{s_−i}) form an exact potential game with potential I(V; Z_{s_1:N}).
    - Bearing: this is the epistemic part of thm:agy-agency(d) under (P0). It should be cited beside wolpert2001optimal at s12_related.tex:55.
27. **Marden, Arslan, Shamma, IEEE Trans. SMC-B 39(6) (2009) 1393–1407.** DOI 10.1109/TSMCB.2009.2017273. Read: P (Sec. II: Def. 2.1, Claim 2.1). New.
    - Statement: marginal-contribution ("wonderful life") utilities give a potential game whose potential is the global objective.
28. **Krause & Guestrin, UAI 2005, 324–331; arXiv:1207.1394.** Read: P (Secs. 2–3). Already in references.bib (krause2005near).
    - Prop. 2 and Cor. 4: information gain is monotone and submodular when observations are conditionally independent given the hidden variables.
    - Bearing: supports a proof step for the sign in prop:agy-performative-sign.
29. **Hellwig & Veldkamp, Rev. Econ. Stud. 76(1) (2009) 223–251.** DOI 10.1111/j.1467-937X.2008.00515.x. Read: A plus Prop. 1 (author PDF). New.
    - Prop. 1: information choices inherit the complementarity or substitutability of actions.
    - Bearing: prior art for the remark after prop:agy-performative-sign that positive coordination needs world-changing acts.

## Derived results and checks of h1–h4 (hand derivations, no scripts)

**D1 (C1/h2). Proved.**
- For Σ_C = αI+β11ᵀ with α>0 and α+nβ>0, Sherman–Morrison gives:
  - off-diagonal entries −β/(α(α+nβ)), so coupling β/(α(α+nβ));
  - leak 1/(α+nβ);
  - x_out = 1/(α+nβ) and x_in = 1/α (cut = 0);
  - r = 1+nβ/α = λ_max(Σ_C)/λ_min(Σ_C).
- Negative control: β<0 gives positive off-diagonal entries, so the block is not diffusive.
- Literal-reading caveat: def:col-contrast (04_collectives.tex:183) and def:col-collective (04_collectives.tex:215) require the whole population's Π^c to be diffusive. So r(C) is defined only if every other block is diffusive too.
- Exchangeability matters for the leak. For a one-factor block D+λλᵀ, row i of the precision sums to d_i⁻¹[1−λ_iS₁/(1+S₂)], with S₁ = Σλ_k/d_k and S₂ = Σλ_k²/d_k. At D=I and λ=(1,1,1,10), row 4 sums to −0.25: the block is MTP2 but not diffusive.

**D2 (two firms). Proved, conditional on the signs reported in rem:agy-h1-status (s05_agency.tex:267).**
- A positive within-firm entry between opposite members, together with positive cross-firm entries, forms a 3-cycle with negative signed product.
- By LUZ Thm 5.2 the law is therefore not even signed MTP2: no diagonal sign change makes Π^c an M-matrix.
- Interpretive bearing on open:col-non-diffusive (out of scope): a sign-gauge extension of contrast would not rescue this instance.

**D3 (C3).**
- Static case, proved: Π(e|η) = Π_e + bbᵀ/q_w, so cross-collective entries are b_ib_j/q_w (positive for same-sign loadings).
- Dynamic single-time case, proved under two hypotheses:
  - (A) the only cross-collective entries of the precision of the members' error paths given the world path are the collider terms Σ_t b_i b_j/q_w ≥ 0;
  - (B) all within-collective off-diagonal entries of that path precision are ≤ 0.
- Under (A) and (B), flipping the sign of C₂ gives an M-matrix. Schur complements of M-matrices are M-matrices (Carlson–Markham Sec. 2), and the subtracted term is nonnegative entrywise. Hence Π^c_ij ≥ b_i(t)b_j(t)/q_w > 0 across the two collectives.
- (B) fails generically: same-time path entries contain +Σ_k W_kiW_kj/q_k for members sharing a listener (consensus), and +b_ib_k/q_w for same-sign acts within a collective.
- Status: open in general.

**D4 (route check). Proved, and a negative result.**
- If the path-level precision given the world is diffusive, then Π^c is diffusive (Kron closure).
- The level-0 network's path precision has same-time block Q⁻¹+WᵀQ⁻¹W, whose off-diagonal entries Σ_k W_kiW_kj/q_k are positive. Yet thm:col-diffusive-precision(a) (04_collectives.tex:156-160) gives a diffusive Π^c there.
- The sufficient condition therefore fails in the basic network and is not a useful construction route.

**D5 (C2 niche). Proved by hand.**
- Setup: n members sense s_j = η+v_j (variance σ²) and receive the others' raw data through receiver-specific channels (noise variance τ²), fused exactly.
- World-conditional covariance: Σ^c = αI+β11ᵀ with
  - β = [2w_o w_x + (n−2)w_x²]σ² > 0,
  - α = σ²(w_o−w_x)² + (n−1)w_x²τ².
- α = 0 iff τ² = 0. Noiseless sharing makes Σ^c singular, matching rem:col-world-conditional (s04_collectives.tex:119).
- Dynamic AR(1) world with steady-state exact filters and same-round reading: r = 1 + nσ²(nσ²+2τ²)/(τ²(τ²+(n−1)σ²)). At σ² = τ² this is r = n+3.
- With the framework's one-round message delay (02_framework.tex:15), the sign of β is not established (open).
- The result depends on a reading. The sender's sensing noise is a private input (05_agency.tex:297), not channel noise, so def:col-world-conditional (04_collectives.tex:131) does not condition on it. If it were conditioned on, Σ^c would be diagonal and no block would have contrast above 1.
- Baseline: under clause (c) with the mean coupling, two equal niches give r̄_hom = 1+2n(n−1)β/((2n−1)α), which is below the niche contrast for every n. Under an attention mechanism, clause (c) instead needs that mechanism's exchangeable state (04_collectives.tex:202), which I did not compute.

**h1. Consistent.**
- 05_agency.tex:379-381 requires neither performative acts nor consensus.
- Group models are defined on slot policies (05_agency.tex:156-169). The joint-acts extension (s05_agency.tex:146-152) can also enter the admitted class, and the two-firms agency computation used it (s10a_meta_agents.tex:143).

**h3. Consistent with 05_agency.tex:333 and 05_agency.tex:352.**
- With exact fusion of raw data and no records, N_ex is the identity, so it is reported inapplicable and imposes no requirement.
- Traps: τ² = 0 and the noise-reading issue, both in D5.

**h4. Correct, with two refinements.**
- (a) The graph clause averages over the declared edge set (04_collectives.tex:201). Declaring the complete graph reproduces clause (c)'s mean medium, under which equal cliques are collectives. Only declaring the cliques' own edge set kills them.
- (b) Besides free joint habits, free product habits (or γ_C not bounded below) give index 1 to every product law (05_agency.tex:251; s05_agency.tex:283). The class must hold habits fixed at ∏E_i or bound γ_C away from zero. This matters for C2, whose epistemic substitutes may be close to a product law.

## Not found or not read

- Not found: any source stating C1's leak or contrast value, the dynamic single-time C3, or a population that meets every clause of def:agy-meta-agent.
- Not read:
  - Berkson 1946; Pearl 1988; Wellman & Henrion 1993;
  - the full text of Karlin–Rinott 1980; Crabtree 1966; Ostrowski;
  - Kenton et al. 2023; Marschak–Radner team theory;
  - Lackey and Tollefsen on group epistemology;
  - Bertschinger et al. / Pfante et al. on informational closure;
  - the body of List–Pettit 2011; Heins 2026 Appendix C.
- The Exa research agent was not used.

## Searches (2026-11-21; the record's Searches table needs these)

- **Exa web search:**
  - Karlin–Rinott 1983 abstract;
  - Gaussian collider and explaining-away formula;
  - Ramstead 2018;
  - Waade 2025;
  - List–Pettit criteria;
  - Marden wonderful-life utility;
  - mutual-information sensor potential games;
  - Krause–Guestrin;
  - Hellwig–Veldkamp;
  - formal collective-agency criteria (2023–2026);
  - Carlson–Markham;
  - Pettit 2014 details;
  - federated inference.
- **Exa fetch:** Fallat (arXiv full text); Heins 2024; Friston 2015; Heins 2026; Heins 2022; Jørgensen 2026; Orseau 2018; Maisto 2025; Pettit PDF; Egilmez abstract.
- **Scholar read_paper:** LUZ (pp. 1–8, 19–28); Wermuth–Marchetti (pp. 1–8); Dörfler–Bullo (pp. 1–6); Kirchhoff (full); Palacios (pp. 1–6); Heins spin glass (pp. 9–16); Egilmez (pp. 1–4).
- **Scholar paper_info:** DOIs checked for LUZ, Dörfler–Bullo, Epskamp, Egilmez, Heins 2024, Heins 2023, Choi–Lee, Wermuth–Marchetti.
- **Local grep:** checked which of these keys are already in Collective_Agents/references.bib.

Only an empty scratch folder was created: C:/Users/CHRISA~1/AppData/Local/Temp/claude/63c81c17e87f0010/34faeca5-ea90-45d1-8cc4-412bdf898c58/scratchpad/metaagent/literature/

# Round 2 (2026-11-21)

## construct-epw

## Verdict

I found an instance that meets every clause of `def:agy-meta-agent` (05_agency.tex:379-381) inside the time-invariant `def:fw-system` (02_framework.tex:11-17). The world is persistent (F=0.9, Q=0.05, no renewal), every message has literal one-round latency, the contrast coordinates are prior errors, filters are exact, and one γ=400 governs every policy component.

- **Grade.** With the literal real-time deliberation protocol (T-real, below), niche A (and B, by symmetry) is a meta-agent of grade (r0, α_M, α_I, α_pr, Agency0) = (3.5, 0.02, 0.09, 0.01, 0.9). This uses the clause (c) mechanism baseline and n_null = 999.
- **Status.** Computed (numerical). The structural pieces are proved. The full grade holds at 17/17 points of a ±1% box.
- **Readings it rests on.** Four, flagged below as R-act, R-dec, R-class and R-mem.
- **Where it fails.** If a slot switch counts as an act *and* N_eff/N_inf are typed D whenever members act, the construction fails both nulls. Under the act reading they give r = 4.41 and 6.27, above the window's lower edge.
- **Weakest clause.** Inference closure: strict α_I = 0.0812, margin 0.009. This is the structural cost of the one-round lag. Next weakest is agency's dependence on how decision states are declared under T-real.

## Declared specification (instance I*)

**Population**
- N=8 in two niches, A={1..4} and B={5..8}.
- World η=(η^A, η^B), independent AR(1) components: η^X_{t+1} = 0.9 η^X_t + w, Q=0.05, stationary.
- Each agent models only its own niche's component, on the state x_t = (η_t, η_{t-1}). This marginal model is exact.

**Channels**
- Own sensor s_i(t) = η_t + v_i, R=1.
- Raw relay: each agent broadcasts u_i(t) = s_i(t) to all 7 others. Receiver l reads y_li(t+1) = s_i(t) + ν_li, with Rc=0.1 receiver-specific. One-round latency; no re-relaying.
- One slot per agent: a public world channel of its niche, carrying η_t when open. Every niche member reads it through its own private read noise, Rs=2. There is no shared instrument noise; the variant with shared noise raised the medium baseline above r(A) (explore4_out).

**Capacity and policies**
- κ=12 for the whole attention set: own sensor plus all 8 slot channels (structural, i.e. habit support), plus at most 3 message channels chosen by EFE.
- Attention habits are uniform over the 64 message sets. B's channels have zero gain for A.
- Slot opening is the owner's active component for the next round: π_k ∈ {0,1}, uniform product habits.
- Slot preference: cost ψ = 0.024 nats per open slot. This is slot-product, (P1), in the "atom at the empty slot" form of prop:fw-efe-communication(a), s02_framework.tex:120.
- EFE: G_i = −I(x_{t+1}; o_{t+1}) + ψ·n_open, with information about the model state x_{t+1}=(η_{t+1}, η_t).
- Computation noise qc = 1e-4·I_2 on the predicted means, included in P^-, so Q^n ≻ 0. Exact Kalman filters.

**Deliberation protocols**
- T-real (primary, literal): one (P4) event per round. A uniformly chosen reviser draws its slot from its marginal policy posterior (soft-min of its full EFE over attention sets), given the others' slots, which it sees on the slot channels. No intention messages. All members then draw attention from their conditional posterior.
- T-fast (variant): (P4) runs to stationarity at a frozen decision state. This needs intention exchange inside a round, so it is faster than the one-round latency.

**Remaining declarations**
- Contrast coordinate e_i = m^-_{i,0}(t) − η^X_t.
- Selector: contrast at level r0.
- Baselines: clause (c) mechanism medium (one component, 8 agents of one type, same κ/γ/ψ/habits, slots read by all, deliberation among 8); also clause (c) mean coupling.
- Coarse variable y = average of the members' prior-mean vectors (in R²).
- Agency class G2: belief is a translate of the members' anticipated belief (variance v* of η_{t+1} after own sensor and 3 relays); slot likelihood N(η, Rs); preference ψ; uniform product habits fixed; γ_C ∈ [0,∞).
- Agency decision state (T-real): the coarse state "a deliberation round at a symmetric covariance state". T-fast: the symmetric state at the median p.

## Per-clause table (T-real; T-fast in brackets)

| Clause (file:line) | Result | Margin | Status |
|---|---|---|---|
| (M), 08_scale.tex:23 | With an exact filter, Var(e_i \| policy path) = P^-_00, bounded by the own-sensor-only Riccati bound | – | proved (uniform form); stationary law numerical |
| Σ^c, 04_collectives.tex:187 | Second moment: exact two-replica algebra per pair of policy paths, Monte Carlo over 160 pairs. α=0.0160364, β=0.0137587 (SE 1.7e-5); mixture part of β 9.9e-5; deviation from compound symmetry 1.2e-7. [0.0161143 / 0.0136617] | – | compound symmetry and zero cross-niche block proved; values numerical |
| Diffusive, :147-151 | Leak 14.07, coupling 12.07, cross 0 (C1) | min row sum 14.07 | proved given β>0 |
| Collective, :214-221 | r(A) = 4.4319±0.0075 [4.3912±0.0044]. Other regions ≤1.924; regions meeting both niches ≤1; leak ratio 1 | r(A)−r0 = 0.93 | numerical |
| Baseline, mechanism, :202 | 2.9417±0.0072, attained by the whole medium [2.9386]. Window (2.94, 4.43] | r0−baseline = 0.56 | numerical |
| Baseline, mean coupling | 3.9416 [3.9067]. Window (3.94, 4.43]; r0 = 4.15 under this reading | ±0.24 | numerical |
| Closure, memory, 05_agency.tex:13-24 | Per-step d_cl: exactly 0 on every deviation-free stretch (equal gains, so A(t) preserves ker P). Stationary mean 3.7e-8. Single-round deviations 2.2e-4 to 3.0e-3; worst explored path 1.0e-2. d_M ≤ d_cl pathwise | α_M=0.02: margin 0.01 | zero and bound proved; values computed |
| Closure, inference | Expected KL to the union-model predictive belief: strict reading (best constant encoding) 0.0812; claimed-variance encoding 0.0979; reverse direction 0.075 [0.0811/0.0980] | α_I=0.09: margin 0.009 (strict); needs 0.1 for the claimed-variance reading | numerical |
| N_hab, γ=0 | 1.7412 [1.7149] | 1.20 below lower edge | numerical |
| N_pr, redrawn every round | 1.8858 [1.8695]; replicates 1.866–1.888; S0 = 4.43, p = 1/(n_null+1) = 0.001 ≤ 0.01 | 1.06 | numerical |
| N_lp; N_rn = N_lp | 1.0497 (slot common mode only) [1.032] | 1.89 | numerical |
| N_fr | β = −5e-7 ± 1.3e-6, r ≈ 1 [exactly diagonal] | 1.94 | numerical |
| N_eff, N_inf | Inapplicable: no act enters η (reading R-act) | – | reading |
| N_ex (type S) | Inapplicable (fusion already exact). If computation noise is removed: 4.4627, same partition survives | – | proved / numerical |
| Agency, :240-246 | Coarse decision state, G2: 0.971 (G1: 0.99988). Departure from habits KL(P‖E) = 0.137; log odds ratio −0.46, so not a product law. [T-fast at X*: 1 − 1e-10; KL(P‖E) 0.124; log odds −0.34; product-law control 0.806] | 0.07 | T-fast exactness proved (identical-interest potential); values numerical |
| Ω_int(A\|ζ_B) | Positive: E[Cov(e_i, e_j \| η)] = β > 0 excludes conditional independence; A does not depend on ζ_B | – | proved given computed β |
| Type E nulls | N_w predicts {A,B} (access), which restricts the claim to the contrast level. N_code predicts nothing. N_fg not computed | – | interpretive |

The checks that decide these numbers, each with a negative control declared before running:
- **Validation.** Fixed attention, no slots, qc=0 reproduces the round-1 A8 value 7.425938. Controls: Rc=1 gives 3.78; dead relays give a diagonal Σ^c.
- **Chain = Gibbs.** At a symmetric state the (P4) law matches the Gibbs law to 1e-16. Control: an asymmetric state breaks detailed balance by 2e-4.
- **Sampled-Gaussian two-replica Monte Carlo against the exact algebra.** At I*, z = 0.2 / −0.44. At a high-mixture variant, dropping the mixture term is rejected (z = 3.15). Treating the relayed noise as fresh is rejected (446 SE).
- **Main-run control.** Rc=1e6 gives r ≈ 1 and an empty window.

## Robustness box (2^(8−4) design plus centre, over F, Q, R, Rc, Rs, ψ, γ, qc)

| Box | Grade (3.5, 0.02, 0.09, 0.01, 0.9) under the mechanism reading | Differ clause | Other |
|---|---|---|---|
| ±1%, T-real | 17/17 | nulls ≥0.94 below local lower edges | α_I ≤ 0.0847; agency ≥ 0.946 |
| ±5%, T-real | r0=3.5 admissible 15/17 | 17/17 local windows, nulls ≥0.675 below | α_I > 0.09 at 7/17; agency ≥ 0.923 |
| Mean coupling | No single r0 even on ±1% (lower edges up to 4.20 against r(A) down to 4.14) | local windows nonempty with nulls below at 17/17 | – |

T-fast boxes match: 17/17 at ±1%; 15/17 at ±5%. The sensitivity runs mainly through γψ, which sets the open-slot rate (0.15 to 0.64 across the ±5% box). The open neighborhood rests on these points plus continuity of the stationary policy/covariance law in the parameters, which I did not prove.

## Readings the verdict depends on

- **R-act.** A slot switch is not an "act" in tab:agy-nulls, which speaks of an act's effect on η. If it is an act, N_eff and N_inf are applicable. Under the table's conditional types (D only for collectives said to form by joint action or by communication through acts) they are diagnostics here, because this collective forms through message relays. Under strict D typing it fails both: diagnostics give 4.41 and 6.27 under T-real [4.38 and 3.95 under T-fast].
- **R-dec.** Under T-real, a covariance state records the recent slot profile, and the profile changes by one member per round. Declaring covariance states as decision states therefore lowers the index:
  - median p-bin: G1 0.978, G2 0.69;
  - three p-bins with one belief: G1 0.30, G2 0.11;
  - p-bin plus current count: 0.91–0.97.

  All of these are still positive, so the clause holds at a lower Agency0; the stated 0.9 needs the coarse declaration.
- **R-class.** If the group belief is the members' current predictive covariance (it ignores redundancy with the same-round relays and sensor), the index is 0 under T-fast.
- **R-mem.** α_M bounds the worst per-step d_cl over the explored reachable paths. A supremum over all reachable paths is not proved. The stationary-expectation reading gives about 4e-8.
- **Not computed.** The EFE reading with information about η_{t+1} only; it would weaken attention concentration at γ=400. The 0.0812 inference value could perhaps be lowered with a better pooled statistic; this was not explored.

## Strongest supported result, open obligation, next action

- **Result.** Form (A), computed: niche A of I* is a meta-agent at grade (3.5, 0.02, 0.09, 0.01, 0.9) under T-real, and (3.5, 0.02, 0.09, 0.01, 0.99) under T-fast, with the readings above. The full grade holds on a ±1% box; the differ clause holds on a ±5% box.
- **Minimal unresolved obligation.** Author decisions on (i) whether a slot switch is an act and how N_eff/N_inf are typed, and (ii) which decision states count under real-time deliberation. The continuity of the stationary law in the parameters is also open.
- **Next action.** Settle (i) and (ii). Then run a fresh-context recomputation of r(A), the medium baseline and the coarse-state agency index from the specification alone.

## Files

All runs were single-threaded, sequential, each under about 100 s; T-real runs used PROTO=real. No repository or vault file was edited. Everything is in C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round2\epistemic_persistent\

| Script | Output |
|---|---|
| lib.py (library), instance.py (I*) | – |
| run_main.py | main_out.txt, main_real_out.txt |
| run_nulls.py | nulls_out.txt, nulls_real_out.txt |
| run_closure.py, run_closure2.py, run_closure3.py | closure_out.txt, closure_real_out.txt, closure2_out.txt, closure3_out.txt |
| run_agency.py | agency_out.txt |
| run_agency_real.py, run_agency_real2.py | agency_real_out.txt, agency_real2_out.txt |
| run_diag_acts.py | diag_acts_out.txt, diag_acts_real_out.txt |
| run_box.py | box_*chunk*.txt, box_summary.txt, box_hw0.01_summary.txt, box_real_summary.txt, box_hw0.01_real_summary.txt |
| check0_validate.py, check1_chain.py, check2_mc.py, check3_fr_real.py | check0_out.txt to check3_out.txt |

explore*.py and their outputs are design exploration only, not deciding.

## attack: construct-epw

## Verdict

The candidate survives my attempt at its stated grade (r0, α_M, α_I, α_pr, Agency0) = (3.5, 0.02, 0.09, 0.01, 0.9) under T-real, but only under more readings than the constructor names. I found no numerical error: independent code reproduces every deciding number.

Where it breaks:
- **R-act is not available.** Under a literal reading of def:fw-system, the "no acts" reading fails. N_eff and N_inf are therefore applicable, not inapplicable. The verdict rests only on the conditional D-typing in tab:agy-nulls.
- **The closure clause as declared passes only under a mixed reading of η_C.** Under a single reading it fails:
  - either the R² coarse variable is not a permitted declaration,
  - or the inference KL is 0.171 > 0.09.
  - **Repair (computed):** declaring the scalar collective average passes both tolerances.
- **Agency at 0.9 needs two readings at once.**
  - The first, slot-only evaluation, is not flagged by the constructor. With attention included and the declared class G2, the index is 0.008.
  - No fixed attention habit reconciles Agency0 = 0.9 with differing from N_hab.

**Weakest point:** the agency clause. It needs slot-only evaluation and the lumped coarse decision state together, and each alternative fails. The thinnest numerical margin is the inference clause: 0.009 after the scalar repair, with the best-constant encoding.

## Method (my own code, not the constructor's)

I simulated the actual Kalman filters by direct Monte Carlo with sampled noises, two replicas per world path, using Σ^c = ½E[(e¹−e²)(e¹−e²)ᵀ] (def:col-contrast, 04_collectives.tex:187). The model was written from the declared specification only.

Validation, run before anything else:
- My own exact Lyapunov solve gives r = 7.425938 in the A8 setting (Rc = 0.2, fixed attention, no slots, qc = 0). This equals round-1 A8. Monte Carlo gives 7.399 ± 0.051.
- With two slots open and qc = 1e-4, Monte Carlo agrees with the exact value at z = −0.71.
- Negative controls:
  - Independent worlds per replica give r = 42.6, so the estimator does condition on the world.
  - Dead relays give β = 1.8e-5 ± 5.4e-5.

All runs were single-threaded and sequential, each under 60 s. No repository or vault file was edited.

## Recomputed deciding numbers (computed, numerical)

| Quantity | Constructor (T-real) | Mine |
|---|---|---|
| r(A) | 4.4319 ± 0.0075 | 4.4185 ± 0.0112; fresh seed 4.4167 ± 0.0149 |
| α, β | 0.0160364, 0.0137587 | 0.016080, 0.013743 |
| Open rate; attention deviation rate | 0.391; 8.2e-5 | 0.392; 6.2e-5 |
| Other regions; regions meeting both niches | ≤ 1.924; ≤ 1 | ≤ 1.922; 1.000 |
| Mechanism medium | 2.9417 ± 0.0072 | 2.9477 ± 0.0081 |
| Mean-coupling baseline | 3.9416 | 3.9302 |
| N_hab / N_pr / N_lp | 1.741 / 1.886 / 1.050 | 1.733 / 1.886 / 1.049 |
| Inference, η_t marginal: best constant / claimed variance / reverse | 0.0812 / 0.0979 / 0.075 | 0.0810 / 0.0976 / 0.0748 |
| Agency, slot component, coarse state, G2 / G1 | 0.971 / 0.99988 | 0.9744 / 0.99995 |
| Agency, median p-bin, G2 / G1 | 0.69 / 0.978 | 0.690 / 0.977 |
| Agency, three p-bins, G2 / G1 | 0.11 / 0.30 | 0.103 / 0.289 |

Negative control: Rc = 1e6 gives r = 1.022 ± 0.010.

## Findings

### 1. N_eff and N_inf are applicable (interpretive, definitional; numbers computed)

The argument:
- def:fw-system (02_framework.tex:13) gives active states four components:
  - attention (what the agent itself reads);
  - a speech act (a content u chosen by the sender, delivered as u+ν one round later);
  - record writes;
  - a performative component a^e that enters the world's dynamics.
- A slot switch makes a channel carrying η+ρ available to the other members in the next round. That is none of the first three.
- So it can only be a^e acting on a world state (an instrument). The model has acts, and the "inapplicable" entries for N_eff and N_inf are wrong (def:agy-nulls, 05_agency.tex:333).
- The verdict then rests on tab:agy-nulls 05_agency.tex:348-349: N_eff is type D "for collectives said to form by joint action", N_inf "by communication through acts".
- Contrast here comes from relayed sensing noise. Reading others' slots lowers it (constructor's N_inf diagnostic 6.27; my no-slot value 8.80 at Rc = 0.1, qc = 0). So under the conditional typing both are non-D diagnostics, and under strict typing the construction fails. This is the record's O2(a).

Side consequence: if slot statuses are world states, def:col-world-conditional conditions on them.
- r(A) = 4.398 ± 0.016 and the medium is 2.916 ± 0.014; the window stays nonempty.
- Interpretive: the slot channel is σ_k·η_t + ρ, bilinear in world states. The population is linear-Gaussian only conditionally on the slot path, the same status as EFE-selected attention.

### 2. Closure (computed; the declaration argument is interpretive)

The pass mixes two readings of η_C:
- **η_C as defined.** η_C is "the exterior variables that S reads" (05_agency.tex:11), here η_t. def:agy-closure(ii) (05_agency.tex:21) then permits only:
  - the pooled statistics of beliefs about η_t, or
  - the collective average of the contrast coordinate.
  
  Both are scalar. The declared R² average, which includes the lag coordinate, is neither. It is the A^T-invariant summary that 05_agency.tex:27 says the constraint exists to exclude. Its d_cl = 0 for exactly that reason.
- **η_C including η_{t−1}.** This reading would admit the R² pooled statistic, but then the encoded belief must be compared with the union posterior on (η_t, η_{t−1}):
  - best constant 0.1712; mean term alone 0.168;
  - claimed variance 0.2336;
  - reverse direction 0.1462;
  - 0.169–0.174 at four ±1% points.
  
  All are above α_I = 0.09.

The constructor uses the second reading for the declaration and the first for the inference.

**Repair, declare the scalar collective average** (computed, run3 and run6):

| Quantity | Value |
|---|---|
| d_cl per symmetric step | 2.5e-3 to 2.9e-3 (not 0) |
| Sampled T-real paths, maximum | 2.89e-3 |
| Worst explored sequence | 1.38e-2 |
| Exact stationary d_M | 7e-5 to 1.0e-4 |
| Inference (best constant) | 0.0810 |

So (α_M, α_I) = (0.02, 0.09) holds with the scalar declaration.

Also: for the constructor's own R² variable, the worst explored per-step d_cl is 1.58e-2, not 1.0e-2. It occurs with (2,3,3,3) sustained for 30 rounds, then (3,0,0,0), at 0 open slots, a reachable sequence. The R-mem margin is 0.004.

### 3. Agency (computed; an unflagged reading, which I call R-pol)

**The reading.** def:agy-agency-index (05_agency.tex:241) uses "the members' joint policies". In def:fw-system a policy fixes every active-state component, here the slot and the attention set. The constructor marginalizes attention.

**With attention included and the declared class G2** (habits fixed and uniform over the 64 message sets):
- P(all three mates) = 0.99994, so attention departs from its habits by 16.632 nats over four members.
- G_C counts only exterior-facing slots, and internal relays carry nothing beyond the union data, so no group model in the class can fit this.
- Index 0.0078 (G1: 0.0080).

**Changing the attention habits does not help** (run7). ε is the habit mass off the all-mates set:

| ε | N_hab r(A) | Full-policy G2 index |
|---|---|---|
| 63/64 (declared uniform) | 1.756 | 0.008 |
| 0.3 | 3.073 | 0.083 |
| 0.05 | 3.830 | 0.384 |
| 0.01 | 3.977 | 0.748 |
| 0.0028 | 4.003 | 0.899 |
| 0.0005 | 4.011 | 0.960 |

- Agency0 = 0.9 needs ε ≤ 0.0028, where N_hab selects A (4.00 is above the lower edge of about 2.95).
- N_hab falls below that edge only near uniform habits, where the index is at most about 0.08.

Repair only by a class with free attention habits, or free product habits with γ_C bounded below (05_agency.tex:251). There the index is about 1, but it credits to free habits 99.2% of the members' departure from their habits (16.63 of 16.77 nats), which no collective EFE explains.

**R-dec** is confirmed. New: at the decision state (median p, current count 2), the declared class G2 gives 0.294; the constructor reported only G1 (0.91) there.

### 4. Partner randomization, run literally

The constructor's output computed 5 replicate estimates and asserted that 99 draws would give p = 0.01, exactly at α_pr. The stated grade says n_null = 999. Run with 999 independent draws: maximum 2.070 against S_0 = 4.4185, p = 0.001. The full-model control gives p = 0.485, so the test can accept.

### 5. Readings checked that do not break it (computed)

- **EFE about η_{t+1} only** (the constructor did not compute this). Attention deviation is 2.9% per member-round, r(A) = 4.373, medium 2.946, N_pr 1.881. The window (2.946, 4.373] is nonempty.
- **Four ±1% box points** (my own design): r(A) 4.406–4.614, medium 2.946–3.035, N_hab ≤ 1.748, N_pr ≤ 1.926. η_t-marginal inference is 0.079–0.084, and coarse G2 agency is 0.969–0.983.

Still open:
- continuity of the stationary law in the parameters, which the open subset relies on;
- the supremum over all reachable paths for the memory clause.

## Readings I chose, and whether the verdict depends on them

| Reading | Verdict depends? |
|---|---|
| The relayed own sensing noise is not conditioned on (record convention) | No: same convention as the constructor |
| The four active-state components of def:fw-system are exhaustive | Only through the D-typing |
| "Each constant of the selector" means each r0 in the admissible window | No: the nulls are below 2.1 |
| η_C as defined at 05_agency.tex:11 | Yes, for the R² declaration; no, after the scalar repair |
| "Joint policies" are full policies | Yes |

## Files

All scripts and outputs are in C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round2\attack_persistent\

- Library: C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round2\attack_persistent\core.py
- Validation: run1_validate.py → run1_out.txt
- Main recomputation: run2_main.py → run2_out.txt
- Closure defects: run3_closure.py → run3_out.txt
- Nulls and reading variants: run4_nulls.py → run4_out.txt
- Agency decision states: run5_agency.py → run5_out.txt
- Worst-sequence search: run6_seq.py → run6_out.txt
- Attention habits vs N_hab: run7_tension.py → run7_out.txt
- Box points: run8_box.py → run8_out.txt
- Partner-randomization test: run9_npr_test.py → run9_out.txt

Each script and output listed is in that same folder; for example, the main output is C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round2\attack_persistent\run2_out.txt.

# Round 3 raw reports (2026-11-22)


## round3: readings

## Verdict

On every O2 item that matters for C11, the manuscript's own text favors the reading C11 uses. Under these readings C11 meets every clause at grade (3.5, 0.02, 0.09, 0.01, 0.99). Those numbers were computed in round 2; the readings they rest on are my interpretation. C11 fails the differ clause only if two disfavored readings hold together: the slot switch is an act, and N_eff and N_inf are type D for every collective whose members act.

If the agency index is taken to cover internal attention (the full reading of (e)), C11 still settles the open problem as worded, but only at Agency0 ≈ 0.007–0.008.

Recommended readings, with my confidence that each is the author's intent:
- **(a2)** N_eff and N_inf are type D only as the table words them: for collectives said to form by joint action, or by communication through acts. Confidence 0.8.
- **(a1)** Opening I*'s public slot is an epistemic slot, not a performative act. Confidence 0.55. C11 does not depend on (a1) once (a2) is adopted.
- **(b)** An index of 1 reached because members act by habit does not count. Confidence 0.85. C11 does not use it.
- **(c)** A fixed attention schedule that contains the partition should be declared as an interaction graph. Confidence 0.6. This does not affect C11.
- **(d)** Filtered errors are admissible when stated (0.7); episodic worlds are outside the intended class (0.65). This rules out C2 and does not affect C11.
- **(e)** The index is evaluated on the exterior-facing components of def:agy-group-model (slots and interventions). Attention to the members' own channels is protocol under (P2). Confidence 0.75.
- **(f)** (P4) at a frozen decision state is the protocol as defined, and it is admissible alongside one-round message latency. Confidence 0.8.
- **Agency0:** a declared grade. Any positive value settles the problem as worded. Confidence 0.85.

Everything below is interpretive (reading of the text). I ran no scripts and wrote no files. All numbers are the round-2 values, except one marked as hand arithmetic.

## (a) Is the slot switch an act, and how are N_eff and N_inf typed?

### (a2) Typing: conditional, as the table words it (0.8)

Text:
- **The table.** N_eff is "D for collectives said to form by joint action; makes the three nulls above separating" (05_agency.tex:348). N_inf is "D for collectives said to form by communication through acts" (:349). Every other row has an unconditional type (:345-355).
- **Types are declared.** Nulls are "declared as one the structure must differ from, one it must survive, an explanation ..., or a diagnostic" (:330). They "remove interaction in declared ways" (:294).
- **N_eff's unconditional role.** It is combined with the deletion nulls "when members act" (:314, :388). This is how it enters for every acting population.
- **H1(c).** Its differ list is the nulls that "delete, freeze or randomize communication or remove selection by expected free energy" (01_introduction.tex:26).
- **The decisive tests** are named as partner randomization and exact fusion (s10_abstract_collectives.tex:276).

Precedent:
- In ex:met-two-firms the members' acts drive the price (s10a_meta_agents.tex:109).
- The author's clause-by-clause verdict lists closure, N_pr and agency as passing (s05_agency.tex:267; 10a_meta_agents.tex:271). It never mentions N_eff or N_inf.
- Under strict typing the firm would owe N_eff, and N_eff leaves its consensus untouched.

Counter-evidence: s07_formation.tex:123 labels N_eff and N_inf as "nulls of type D" without the qualifier. That sentence is about a model without acts, so the label decides nothing.

Rationale: a D null tests the mechanism the collective is said to form by. Strict typing would require a collective formed by messages to depend on acts as well. That asks more than H1's "its structure should come from the members' communication" (05_agency.tex:3).

Consequences:
- C8's conditional premise is not met for collectives said to form by communication.
- C9's first reading is the table's own wording.
- R5 is not decisive.

### (a1) Is opening I*'s public slot a performative act? Probably not (0.55)

For "act":
- def:fw-system lists four components of active states (02_framework.tex:13): attention (what the agent itself reads), speech (content the sender writes), record writes, and a^e.
- Making a world-reading channel available to others is none of the first three.

Against "act":
- a^e enters η's dynamics through B^η (02_framework.tex:15). I*'s switch leaves η^X_{t+1}=0.9η^X_t+w unchanged. It is a^e only on a world extended by an instrument state, read bilinearly.
- The agency section, which supplies the nulls and the index, separates an "epistemic slot choice" from an "intervention" (s05_agency.tex:147). It contrasts policies that "only gather information" with active states that "change the world" (s05_agency.tex:144).
- Slots are "exterior-facing sensory channels that a policy can open" (05_agency.tex:157). Under (P2) every member receives every opened slot (05_agency.tex:165). A public slot is (P2) realized by the medium.
- N_eff is defined through "each act's effect on η" (05_agency.tex:348).
- Channel types are distinguished by "latency, persistence and whether they move resources" (02_framework.tex:229). A one-round, non-persistent, non-rival channel is of the direct type, not performative.

### Consequence for C11

C11 does not depend on (a1) once (a2) is adopted:
- I* is said to form by raw relays. The N_inf diagnostic of 6.27 shows the structure does not come through the slots.
- I* differs from N_lp+N_eff (N_lp gives 1.050).
- Even conditioning on slot status as world states leaves the window nonempty (attack: 4.398 against a medium of 2.916).

Under act plus strict typing, C11 fails: N_eff gives 4.41/4.38 and N_inf 6.27/3.95, against a lower edge of 2.94.

### Amendment

- In tab:agy-nulls: "otherwise a diagnostic; N_eff is combined with the deletion and freezing nulls".
- Declare what the collective is "said to form by" together with the grade.
- In def:agy-nulls: an act is an active state with an effect in η's dynamics. Opening a slot of def:agy-group-model, including one every member reads, is not an act.

## (b) An index of 1 reached by acting on habit does not count (0.85)

Text:
- The index is set to 1 "when the members act by habit" (05_agency.tex:245).
- The open problem dismisses the only diffusive two-firm variant because "agency holds only because the members act by habit" (s05_agency.tex:296).
- N_hab is inapplicable without selection by expected free energy (05_agency.tex:333). The habit null and the index therefore become vacuous together (I5a).
- The index asks what share of the members' "departure from their habits" a group model explains (05_agency.tex:238).

C11: not affected. The departure from habits is 0.124 nats (T-fast) and 0.137 (T-real), or 16.77 under the full reading.

Amendment to def:agy-meta-agent: add "with Σ_X w_X KL(P(·|X)‖E) > 0".

## (c) A fixed attention schedule should be declared as an interaction graph (0.6); C11 unaffected

Text:
- The comparison medium is "declared with the model" (04_collectives.tex:198).
- Clause (b) applies only "if the model declares" an interaction graph (:201). Clause (c) covers "a declared mechanism, as attention under a budget" (:202).
- Equal cliques give opposite verdicts under the two declarations (:225; s04_collectives.tex:147). The remark adds: "a model whose declared couplings contain a partition cannot claim to have found it".
- "Conformity amplifies a partition that attention and readership already declare" (10b_hierarchy.tex:193). With exogenous attention the structure "agrees with the explanation null" (:188).

Precedent: sec:frm uses clause (c) for attention selected by expected free energy (07_formation.tex:173).

C11: attention in I* is selected by expected free energy (N_hab gives 1.741), so the mechanism clause applies. Niche access lives in the world model, where N_w agrees; that restricts the claim (type E) and is not a failure.

Amendment to clause (b): a fixed or exogenously scheduled pattern declares as interaction graph the pairs that share a listener or a source in it (thm:col-diffusive-precision(c), 04_collectives.tex:166).

## (d) Filtered errors are allowed if stated (0.7); episodic worlds are outside (0.65)

Text:
- "e_i=m_i−η ... the prior error unless stated" (appA_notation.tex:67).
- The world has time-invariant F and Q, with one-round message latency (02_framework.tex:15).
- The errors and the world path must be "jointly stationary" (04_collectives.tex:131). An episode clock is cyclostationary at the round clock.
- Every worked example uses an AR(1) world and prior errors (02_framework.tex:315; 07_formation.tex:53).

Consequence: C2 does not count. C11 is unaffected.

Amendment to def:col-world-conditional: "stationary at the round clock of def:fw-system; prior errors of def:fw-level0 unless declared otherwise."

## (e) The members' joint policies are the exterior-facing components (0.75)

Text:
- Slots are exterior-facing (05_agency.tex:157), and G_C depends on the profile only through slots (:159).
- (P2) makes internal data sharing a hypothesis, not a choice (:165).
- The index compares laws on the profile set A with group models whose habits live on A (:241).
- Agency is "the law that one agent would produce by minimizing a collective expected free energy" (:154). One agent holding the union data has no attention to co-members, so internal attention has no counterpart in the comparison.
- The class should be restricted to "the belief and slot model of the collective's closure model" (s05_agency.tex:90).

Precedents:
- **Nested model.** Its only policies are attention sets selected by expected free energy (ext2_rfm.tex:11). The author writes "the model has no acts, so (H-act), the agency index, N_eff and N_inf are inapplicable" (ext2_rfm.tex:139). Applying the index would need "acts and decision states" to be added (:167). N_hab is applied to the same attention (:140).
- **Culture row of tab:abs-graded:** "Not claimed: no collective active states" (10_abstract_collectives.tex:203).
- **Two firms.** Agency is evaluated on the acts u_i only; consensus is a fixed protocol (s10a_meta_agents.tex:143; chk10a_meta_agents.tex:55,57).
- **Two-group model.** Attention is a policy (07_formation.tex:38) and N_hab applies (s07_formation.tex:123). Yet rem:agy-h1-status never evaluates the split's agency (s05_agency.tex:267), and 02_framework.tex:334 lists "the agency of a collective formed by such attention" as open.

Against:
- Active states are drawn from one policy posterior (02_framework.tex:17).
- "Attention, addressing and content are policies" (02_framework.tex:260; s02_framework.tex:110).
- N_hab's "policies drawn from habits" (05_agency.tex:351) covers attention.

Resolution: in the author's practice, N_hab has population-wide scope ("act on the whole population", 05_agency.tex:380), while the index has the group model's profile scope. The asymmetry comes from the author's own usage, not from C11.

Consequences:
- C11's reading (v) is the author's.
- C12 is correct, but its policy set (a_i, s_i) is not the author's index. C12 also argues against the full reading: that reading would cap near zero the index of every collective formed by internal attention under diffuse habits, while N_hab forbids concentrating those habits (run7).
- Under the full reading, C11 still holds at Agency0 ≤ 0.0078.

Amendment to def:agy-agency-index: P(·|X) is the law of the profiles in A=∏A_i of def:agy-group-model or def:agy-joint-acts (slot and intervention components), marginal over the selection of the members' own channels.

## (f) Frozen-state (P4) deliberation is admissible (0.8)

Text:
- "The deliberation protocol, at a decision state held fixed while the members deliberate" (05_agency.tex:161).
- "We write P^∞ for the stationary law of the chain (P4)" (:176).
- thm:agy-h1(e) holds "under the deliberation protocol" (:395).

Precedents:
- (H-act) (10a_meta_agents.tex:250) says the theorem "does not derive them from messages"; members "announce their interventions, by (P2)" (:268). Announcements sit outside the message latency.
- The two firms have one-round latency. Their deliberation model "is declared at a decision state and is not the act rule of the dynamics" (s10a_meta_agents.tex:143). The author still counts it: "agency passes for any declared Agency0 below 0.715" (s05_agency.tex:267).

Against: one-round latency and one policy draw per round (02_framework.tex:15,17), and "actual conditional laws" (05_agency.tex:241). The precedent overrides this, and more strongly for T-fast, where the dynamics actually use P^∞.

Consequence: C11's reading (iv) holds, at 1−1e-10 at X* (constructor's number; exactness proved). Real-time deliberation is not required.

Amendment to def:agy-group-model: at X the actual law is P^∞ of (P4) at X. The announcements under (P2) are not messages of def:fw-system.

## Agency0: any positive declared value (0.85)

Text:
- Agency0 is a component of the grade (05_agency.tex:380), a "declared lower bound" (appA_notation.tex:107).
- The open problem asks for "r_0>1 and Agency0>0" (05_agency.tex:403; s05_agency.tex:296).
- The author writes "any declared Agency0 below 0.715, none being declared" (s05_agency.tex:267).
- "To the degree that" (01_introduction.tex:26).

No passage names a substantive minimum. The values r=1 and Agency=0 are the trivial ends of each scale: r=1 is what causally separating nulls give (05_agency.tex:314).

Amendment: none is needed. If a threshold is intended, the open problem must state it.

## Grade frontier for C11

Largest Agency0 at which every clause holds, with (r0, α_M, α_I, α_pr) = (3.5, 0.02, 0.09, 0.01):

| Readings | Largest Agency0 | Status |
|---|---|---|
| Recommended: (a2) conditional, (e) slot/act, (f) frozen | 1−1e-10 (stated 0.99) | computed |
| (e) slot/act, real-time, coarse decision state | 0.971 (attack 0.974) | computed |
| (e) slot/act, real-time, finer declared states | 0.69 / 0.294 / 0.10 | computed |
| (e) full, real-time, coarse | 0.0078 | computed |
| (e) full, frozen | ≈0.0074 = 0.124/(16.63+0.124) | hand arithmetic, C12 at equality; not run |
| (a1) act and strict typing | no grade (differ clause fails) | computed |

Raising the full-reading frontier with an intermediate habit concentration, while N_hab stays below 2.94, is open.

## A reading outside O2 that C11 rests on

C11's reading (ii) is partner randomization redrawn every round:
- The table permits "once or every round" (05_agency.tex:350).
- The author nevertheless lists the drawn-once variant as "not computed" or "not covered" (07_formation.tex:284; s07_formation.tex:123; ext2_rfm.tex:140).

If the drawn-once variant must also be passed, I*'s random directed draws would likely need the substitute selector (s05_agency.tex:252). That selector's between-niche mutual information is exactly zero in the full model and in every draw, so p=1, as in R3. This is a conjecture for I*; I did not compute it. I suggest adding it to O2 as (g).

## Textual controls (what would have contradicted the readings)

I grepped all sections for:
1. Any agency index computed over attention policies: none found.
2. A statement typing N_eff or N_inf as D for every acting collective: none, apart from the unqualified label at s07_formation.tex:123 in a model without acts.
3. A substantive Agency0 value: none found.
4. Agency computed under real-time deliberation: none found.

## round3: strict-construction

VERDICT: Yes: I built I** and it meets every clause of def:agy-meta-agent under the strictest reading combination. I** is instance I* with the public slots replaced by private optional sensors (read by the owner, relayed raw with one-round latency to every agent that attends it) and the sensor cost psi raised from 0.024 to 0.030. At psi = 0.024 the mechanism-baseline window is empty: the medium scores 8.16 against r(A) = 7.82. The strictest combination is: agency over full policies (attention and sensors) with uniform habits held fixed and gamma_C in [0, inf); exact covariance decision states; a declared group belief; both clause (c) baselines; the scalar collective average with Q^n > 0; and partner randomization redrawn every round with 999 draws. The grade is (r0, alpha_M, alpha_I, alpha_pr, Agency0) = (7.9, 0.02, 0.09, 0.01, 0.066) under real-time asynchronous deliberation and (7.9, 0.02, 0.09, 0.01, 0.074) under (P4) at a frozen decision state. Status: computed (numerical), with proved structural pieces. Readings (a) and (f) are removed by construction. No component of any active state is an act, so N_eff and N_inf are inapplicable. Each member's expected free energy is independent of its co-members' simultaneous choices, so (P4) at a frozen state is a product law realizable within the one-round latency. Reading (e) is not removed. Under full policies the C12 cap is 1/7 for this policy set, and the frontier is about 0.07 (0.123 at psi = 0.035, checked only for the collective clause, N_hab, N_pr and agency). Counting sensor choices only, it rises to 0.59 to 0.998. Two declarations carry the result. First, the record's convention that relayed sensing noise is a private input (if it were conditioned on, r(A) would be about 1). Second, alpha_M = 0.02 holds on typical paths (largest per-step defect 5.2e-3) but not under the literal supremum over all reachable paths, which lies in [0.0266, 0.0988] by a grid bound, so that reading needs alpha_M = 0.11. The open neighborhood (a 1% box in eight parameters where one r0 works for both baselines) is numerical; continuity (O6) is not proved.
POSITIVE: True

## Result

Instance I** meets every clause of `def:agy-meta-agent` (05_agency.tex:379-381) under the strictest readings requested (computed; structural pieces proved). The grades are:

| Protocol | Grade (r0, alpha_M, alpha_I, alpha_pr, Agency0) |
|---|---|
| Real-time asynchronous | (7.9, 0.02, 0.09, 0.01, 0.066) |
| (P4) at a frozen decision state | (7.9, 0.02, 0.09, 0.01, 0.074) |

These use n_null = 999 and the memory clause read on typical paths. Under the literal supremum over all reachable paths, alpha_M must be 0.11.

All scripts and outputs are in `C:\Users\chris and christine\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round3\strict-construction\`. No repository or vault file was edited. Every run was single-threaded, one at a time, and under 2 minutes.

## 1. Target, quantifiers and readings

**Target.** `open:agy-meta-agent-exists` (s05_agency.tex:295-297): exhibit one linear-Gaussian population and a set C, with r0 > 1 and Agency0 > 0, meeting every clause of the definition. The clauses are:
- Collective at level r0: `def:col-collective` 04_collectives.tex:214-221, with `def:col-contrast` :182-188 including the second-moment convention at :187, `def:col-baseline` :197-209, the diffusive class :147-151, and `def:col-world-conditional` :130-132.
- Closed at (alpha_M, alpha_I) for a declared coarse variable (`def:agy-closure` 05_agency.tex:13-24).
- Differs from every applicable type-D null, on a nonempty open subset and for each selector constant, with N_pr tested at alpha_pr with n_null draws (`def:agy-nulls` :332-334, `tab:agy-nulls` :337-360, `prop:agy-tests`(b) :367).
- Survives every type-S null.
- Agency index at least Agency0 (`def:agy-agency-index` :240-246, group models `def:agy-group-model` :156-169).

**Supplied by the task.** The specification of I** follows I* of record C11 with private optional sensors. The strictest reading combination:
- agency over full policies, with uniform habits held fixed and gamma_C in [0, inf);
- decision states equal to covariance states, under both real-time and (P4) frozen deliberation;
- both baselines, with an explicit open neighborhood for the mean-coupling baseline;
- the scalar collective average, with Q^n > 0;
- N_pr redrawn every round, with 999 draws.

**Introduced by me** (declared before the deciding runs):
- psi = 0.030 instead of 0.024.
- Speech is structural (one option): every agent writes its raw readings, a presence flag and its intention to all others.
- The intention header gives members their mates' current statuses. Attention deficits occur in 1.2e-5 of member-rounds, so this matters only under nulls. Removing it under N_pr changes nothing (2.850 against 2.844).
- The mechanism medium has 8 agents on one world component with the same mechanism. Under the real-time protocol it has 2 revisers per round, the same per-agent rate as the population. With 1 reviser the medium is 6.023 against 5.959.
- Group classes: G1 has a free constant belief variance; G2 has the declared anticipated variance (strict).
- The coarse variable is y = (1/4) sum of the members' prior means of eta_t.

**Convention kept from the record (load-bearing).** An agent's own sensing noise is a private input and is not conditioned on, even when relayed. This agrees with the classification of sensing noise as private in `def:agy-order-parameter` 05_agency.tex:297. Under the alternative, the shared-noise coupling disappears: the fresh-relay control gives r(A) = 1.003.

## 2. Specification of I**

**State space and dynamics.**
- Two niches, A = {0..3} and B = {4..7}, each with an independent stationary AR(1) world component: eta_{t+1} = 0.9 eta_t + w, with Q = 0.05.
- Each agent models its own niche's component on x_t = (eta_t, eta_{t-1}) with an exact Kalman filter. The prediction carries computation noise qc I_2 with qc = 1e-4, included in P^-.
- P^-(t+1) depends on P^+ only through p = P^+_00.

**Channels in round t.**
- Own sensor, always read: s_i = eta_t + v_i, with R = 1.
- Private sensor, read only by its owner and only when sigma_i(t) = 1: o_i = eta_t + rho_i, with Rs = 2.
- Messages from each attended mate j: s_j(t-1) + nu_ij, plus o_j(t-1) + nu'_ij if sigma_j(t-1) = 1, with receiver-specific noise Rc = 0.1.
- Channels of the other niche carry zero information for the receiver (zero gain).

**Policy and capacity.**
- A policy is pi_i = (sigma_i, M_i), with M_i a set of at most 3 of the 7 message channels.
- kappa = 5: own sensor, private sensor, three messages.
- Habits are uniform over the 2 x 64 policies. One precision gamma = 400.
- G_i = -I(x_{t+1}; round-(t+1) observations) + psi * sigma_i, with psi = 0.030.
- G_i depends on the mates' current statuses sigma_j(t), not on their round-(t+1) choices.

**Protocols.**
- Real-time asynchronous ("real"): one uniformly chosen reviser per niche per round redraws its status from the marginal policy posterior. Every member redraws attention every round.
- Frozen ("frozen"): (P4) at the frozen decision state, which by P4 below means every member draws from its own policy posterior every round.

**Time and noise.** Discrete rounds; Gaussian noises independent across agents and rounds.

**Implementation.**
- Exact Gaussian second moments per pair of independent policy paths that share the world path, with Monte Carlo over the policy paths: `lib3.pair_moments`, `lib3.sigma_c`.
- An independent sampled-noise simulator of the actual filters, two replicas per world path: `mc3.run`.
- Exact policy laws at each decision state: `agency3.py`.
- Declared instance: `instance3.py`.

## 3. Proved pieces

**P1. No acts (proved, definitional).**
- Each agent's active states are an attention set (own sensor, private sensor and message channels, all channels read) and a speech act with one option. There are no record writes and the performative component is zero.
- Opening the private sensor is attention to a world channel (`def:fw-system` 02_framework.tex:13).
- Every model is therefore "a model without acts", and N_eff and N_inf leave it unchanged. Both are inapplicable (05_agency.tex:333; `tab:agy-nulls` :348-349).
- The verdict does not depend on reading (a) or on the conditional typing in the table.

**P2. Exchangeability in law (proved).**
- Claim: from the symmetric start, at every t and for every permutation tau of A, the pair (eta, e(t)) has the same law as (eta, P_tau e(t)).
- Argument. The update is equivariant under relabeling of members: each member's EFE depends on its own covariance and on the count of its open mates; the attention law is uniform within each count cell; the reviser is uniform; the start is symmetric. The inputs are i.i.d. across members and independent of eta.
- Consequence. Cov(e(t)|eta) commutes with every P_tau almost surely. The commutant of the permutation representation of S_4 is span{I, 11^T} (trivial plus standard representation, by Schur's lemma). Hence Sigma^c_AA = E Cov(e|eta) = alpha I + beta 11^T, and the same holds for time averages.
- Zero cross block. e_A is a function of (eta^A, A's private inputs, A's clock) only, because B channels have zero gain and zero expected information. Given eta, e_A and e_B are functions of independent inputs, so Sigma^c_AB = 0 exactly.
- Niche-swap symmetry gives Sigma^c_BB = Sigma^c_AA.
- Per realization the covariance is not compound symmetric: with the fixed profile (1,0,1,0) it deviates by 8.3e-4 (V1b).

**P3. Closed forms (proved; C1).**
- With b = beta/alpha: Pi_A = (alpha I + beta 11^T)^{-1}, with coupling b * eps and leak eps = 1/(alpha + 4 beta). It is diffusive iff beta >= 0.
- An m-subset of A has r = (1 + m b)/(1 + (4 - m) b); r(A) = 1 + 4b.
- Any region meeting both niches has r <= 1.
- Mean-coupling baseline: 1 + (24/7) b = 1 + (6/7)(r(A) - 1).
- The medium is compound symmetric over 8 by the same argument, so its sup over regions is 1 + 8 b_M.

**P4. Frozen (P4) is a product law (proved).**
- With a one-step horizon, G_i does not depend on pi_{-i}(t+1): co-members' round-(t+1) readings reach i only at round t+2.
- The (P4) chain is therefore a product chain with unique stationary law prod_i q_i. It is reached by one draw per member, with no intra-round messages.
- (P2) of `def:agy-group-model` fails, so `thm:agy-agency` does not apply. The index is computed directly.

**P5. Agency cap (proved from C12).**
- Every admissible group model has the form U64^4(M) x P^s_g(sigma). Attention to internal channels opens no slot, and channels of the other niche carry no information about eta_C.
- Hence the index is at most KL_{s|a}/(KL_a + KL_{s|a}).
- In I**, KL_a = 16.6348 (computed; 4 ln 64 = 16.6355) and KL_{s|a} <= 4 ln 2, so the index is at most 0.1429. This equals ln 2 / ln 128 = 1/7 when attention is deterministic.

**P6. Memory reduction (proved; uses a grid).**
- Given the policy path, x_{t+1} = A(t) x_t + B x_B + n_t with A(t) and Q^n(t) block diagonal and Q^n >= qc I > 0.
- By data processing, I(y_{t+1}; y_{0:t-1} | y_t, x_B) <= d_cl(t), so d_M <= sup_t d_cl(t).
- Sigma = Cov(x | blanket path) is block diagonal.
- Sigma -> Sigma_{x|y} is Loewner-monotone, because v^T Sigma_{x|y} v = min_c (v - P^T c)^T Sigma (v - P^T c).
- With blocks bounded by Sbar: d_cl <= (1/2) ln(1 + f), where f = [sum c_i - (sum b_i)^2/(4s)] / sum q_i, with c_i = a_i^T Sbar a_i, b_i = e1^T Sbar a_i, s = Sbar_00, q_i = (Q_i)_00, and a_i the first row of A_i.
- The reachable p-range [0.0890, 0.1413] is invariant by Riccati monotonicity. The condition Sbar - A Sbar A^T >= Q is verified on an 81-point grid of p.

**P7. Interaction among members (proved given beta > 0).** Omega_int(A | zeta_B) = Omega_int(A), because A's process does not depend on zeta_B. It is positive, because beta > 0 excludes conditional independence given the shared drive (eta is exogenous).

**P8. Moment bound (M) (proved; one step numerical).** Given the policy path, P^-_00 is at most the own-sensor-only Riccati bound, and the actual error covariance converges to the claimed one. The uniform contraction this needs was verified numerically, with a common quadratic Lyapunov function on the grid (D5c). A stationary law exists by Krylov-Bogolyubov on the compact state space with a Feller kernel.

**P9. N_lp and N_fr under the frozen protocol (proved).** Both nulls are causally separating, so Sigma^c is exactly diagonal and r = 1 (`prop:agy-nulls-vanish` (a),(d)). Under the real-time protocol a shared reviser clock remains; the estimates are beta = 1.1e-6 ± 1.1e-6 (N_lp) and 3.3e-7 ± 1.0e-6 (N_fr). If the true beta were negative, Pi^c would not be diffusive and no region would qualify. Either way, no region is selected at any admissible r0.

## 4. Per-clause results (computed unless marked)

| Clause (file:line) | Real-time | Frozen | Margin |
|---|---|---|---|
| Sigma^c_A (:187), 160 pairs | alpha = 0.01040183, beta = 0.01932437; deviation from compound symmetry 1.35 SE; mixture part of beta 2.2e-5 | alpha = 0.01040742, beta = 0.01930762; deviation 1.64 SE | |
| Diffusive (:147-151) | coupling 21.18, leak 11.40, cross block 0 | 21.17, 11.41 | beta > 0, proved (C1) |
| r(A) | 8.4311 ± 0.0025 | 8.4207 ± 0.0031 | r(A) - r0 = 0.531 / 0.521 |
| Other regions | at most 2.3002 (closed form); regions meeting both niches at most 1 | 2.2995 | 5.6 below r0 |
| Mechanism medium (:202) | 5.959 ± 0.016 | 6.006 ± 0.010 | r0 - medium = 1.94 / 1.89 |
| Mean-coupling baseline | 7.3695 | 7.3606 | r0 - baseline = 0.53 / 0.54 |
| Leak ratio | 1 | 1 | |
| Memory, typical paths (25 paths x 320 steps) | largest d_cl 4.70e-3 | 5.20e-3 | 0.015 below alpha_M = 0.02 |
| Memory, exact stationary d_M at fixed profiles | 7.1e-5 to 1.3e-4 | same | |
| Memory, literal supremum over reachable paths | at least 0.0266 (explored); at most 0.0988 (grid bound) | same | needs alpha_M = 0.11 |
| Inference (best constant encoding) | 0.0593 (claimed variance 0.0671, reverse 0.0560) | 0.0594 | 0.031 below alpha_I = 0.09 |
| N_hab | 2.379 | 2.383 | 3.58 below the medium edge, 4.99 below the mean-coupling edge |
| N_pr, annealed | 2.844 | 2.844 | 3.11 / 4.53 |
| N_pr test, 999 draws | largest draw 3.202, p = 0.001 | 3.230, p = 0.001 | S0 - largest draw = 5.23 / 5.19 |
| N_lp = N_rn | 1.0001 | 1.0000 (exact, P9) | |
| N_fr | 1.0001 | 1.0000 (exact, P9) | |
| N_eff, N_inf | inapplicable (P1) | inapplicable | |
| N_ex (type S) | inapplicable (fusion already exact); variant with qc = 0 gives 8.599, same partition | 8.589 | |
| Open neighborhood | B_1% (±1% in F, Q, R, Rc, Rs, psi, gamma, qc): r(A) between 8.198 and 8.670 | corners 8.193 and 8.656 | r0 = 7.9 works iff r in [7.9, 9.05) |
| Agency, strict, full policy | G2 0.069 ± 0.001; G1 0.071 to 0.073 | G2 0.0746; G1 0.0747 | equals the frontier |

Further details:
- The N_pr test's negative control (199 draws of the full model through the same estimator) gives p = 0.450 (real-time) and 0.515 (frozen).
- On B_1%, the medium stays at or below 6.00 and N_hab, N_pr at or below 2.88. The first-order model is accurate to 0.024.
- Type-E nulls: N_w agrees with {A, B} (access groups), which restricts the claim to communication within access groups. N_code predicts nothing. N_fg was not computed.

## 5. Grade frontier: largest Agency0 at which every clause holds

The other clauses hold at (7.9, 0.02 or 0.11, 0.09, 0.01) independently of Agency0, so the frontier equals the agency index. Each conservative frontier lies at or below the lowest point estimate in its row. "Strict" means decision states are the exact covariance states; the p-vector determined sigma(t) in all 18,000 sampled states.

| Protocol | Policy scope | Decision states | G2 (declared belief) | G1 (free belief variance) | C12 cap | Conservative frontier |
|---|---|---|---|---|---|---|
| Real-time | Full | strict | 0.0679; 0.0694 ± 0.0009 | 0.0714; 0.0729 ± 0.0009 | 0.1107 | 0.066 (G2), 0.069 (G1) |
| Real-time | Full | five count states | 0.0695 | 0.0730 | | |
| Real-time | Full | one coarse state | 0.0742 | 0.0743 | | 0.072 |
| Real-time | Sensors only | strict | 0.613; 0.625 ± 0.007 | 0.645; 0.657 ± 0.007 | | 0.59 |
| Real-time | Sensors only | five count states | 0.770 | 0.810 | | |
| Real-time | Sensors only | one coarse state | 0.9988 | 0.9995 | | |
| Frozen | Full | strict | 0.0746 | 0.0748 | 0.0749 | 0.074 |
| Frozen | Sensors only | strict | 0.9961 | 0.9979 | | 0.995 |

In the strict real-time rows the first estimate uses 18,000 states; the second is the mean ± SE over five independent paths of 4,000 rounds.

**Reading dependence.** The verdict (Agency0 > 0) holds in every combination. The frontier depends on (e) and, to a lesser degree, on the protocol and on the declaration of decision states. Reading (a) is moot (P1). Reading (f) is moot for the frozen protocol (P4).

**Frontier on the box.** At the corners of B_1% the real-time G2 index is 0.0616 and 0.0731. The agency clause is evaluated at the instance only.

**psi family (partial: collective clause, N_hab, N_pr and agency; closure and the N_pr test not run).**
- psi = 0.035: open rate 0.019, r(A) 8.598, medium 4.962, mean-coupling baseline 7.512, N_hab 2.376, N_pr 2.909, strict full-policy agency 0.123 (G2), cap 0.1355.
- psi = 0.045: open rate 3e-4, agency 0.1427, equal to the cap. The sensors are then essentially never opened.

## 6. Checks run (expectation declared before each run; negative controls)

**V1, exact algebra.** It reproduces the round-1 A8 value r = 7.425938 exactly. With fresh relays r = 1.0000000000. The covariance at a fixed asymmetric profile is not compound symmetric. Monte Carlo agrees within |z| <= 1.19. Independent worlds per replica inflate the off-diagonal 6.5x. Output: `v1_out.txt`.

**D2, random policies.** Exact algebra against Monte Carlo: z_alpha 1.26 and z_beta -0.06 (real-time); 0.03 and 0.70 (frozen). Negative control: fresh relays collapse beta to the mixture part (z = -478 and -368); the Monte Carlo with fresh relays gives r = 0.998. Output: `d2_out.txt`.

**V2, agency law.** The grouped attention law and its KL equal explicit enumeration of all 64 sets to 4e-14. The control with wrong gains is off by 3.6 nats. Output: `v2_out.txt`.

**Deciding outputs.**
- `d1_real_out.txt`, `d1_frozen_out.txt`: collective clause and baselines.
- `d3_real_out.txt`, `d3_frozen_out.txt`: null family (the full-model control does not differ).
- `d4_real_out.txt`, `d4_frozen_out.txt`: N_pr test.
- `d5_out.txt`, `d5b_out.txt`, `d5c_out.txt`: closure (the reduction reproduces 0.026644).
- `d6_real_out.txt`, `d6_frozen_out.txt`, `d6b_out.txt`: agency (habit-only model gives index 0; free attention habits exceed the cap: 0.957 and 0.9997; empirical against computed count law p = 0.925 and 0.284).
- `d7a_out.txt`, `d7b_out.txt`, `d7c_out.txt`: open neighborhood (at 3% the lower corner falls to 7.713 < r0; a sign-flipped model misses by 0.38).
- `d8_out.txt`: variants (psi = 0.024 gives an empty window).
- Files named `explore*` are design exploration only, not deciding.

**Expectations that failed (reported, not deciding).**
- Sensitivities of r(A) are larger than declared: the sum of |dr/dln theta| is 23.8, not below 12. Individual values: F +7.25, Q -5.82, R +5.05.
- The declared "worst single round below 0.02" failed: 0.0266 over reachable patterns (0.0316 when unreachable patterns are included).
- The mismatched-protocol control in D6b was badly designed. It gives 0.0691, the real-time value: both protocols visit similar states, so it tested the state distribution rather than the law kernel.

## 7. Weakest point

**Reading (e).** Under full policies with uniform habits, attention concentrates on all three mates (16.63 nats of departure from habits). No group model can explain this, so the index is capped at 1/7 (C12) and is about 0.07 in I**. This matches what the record calls the habit surprise N_hab requires.

**Next weakest: the memory clause.** On typical paths it passes with margin 0.015. Under the literal supremum over reachable paths, the worst pattern (three members attending nobody while the fourth opens its sensor) needs alpha_M of about 0.03 to 0.1. The upper end is a grid bound, not interval arithmetic.

**Thinnest margin.** On B_1%, r(A) - r0 drops to 0.298.

## 8. Strongest supported result, unresolved obligations, next action

**Result.** Form (A), computed. Niche A of I** is a meta-agent at (7.9, 0.02, 0.09, 0.01, 0.066) under real-time asynchronous deliberation and at (7.9, 0.02, 0.09, 0.01, 0.074) under frozen (P4). This holds under the strictest agency readings and both baselines, with alpha_M = 0.11 required under the literal supremum memory reading. This discharges the record's O5 at a low grade: the C12 condition 4 ln 2 >= (A0/(1 - A0)) x 16.63 holds for A0 up to 1/7.

**Minimal unresolved obligations.**
- O6: continuity in the parameters, which the open subset rests on. B_1% is supported by 18 evaluated points and a first-order model, not a proof.
- A proof-grade bound on the supremum memory defect (the current upper bound uses a grid).
- The author's rulings on (e) and on the memory reading.

**Next action that would change the answer.** The author's decision on (e). Under sensor-only agency the frontier rises to 0.59 to 0.998. If full policies are intended, a larger strict frontier needs a different policy set, because the cap is ln|A^s|/ln|A|. For example, L private sensors per member give a cap of L ln 2/(ln 64 + L ln 2), which is 0.4 at L = 4. That instance would then have to be rerun through the full clause set.

## round3 attack: strict-construction

## Verdict

**The candidate survives.** Under the readings it declares, I found no clause of `def:agy-meta-agent` (05_agency.tex:379-381) that I** fails at either stated grade. No null it calls inapplicable turned out to be applicable. My own code reproduces every deciding number.

Two of its subsidiary claims are wrong, and both errors cut in its favor:
- **Memory concession.** The claim that the literal-supremum reading needs alpha_M = 0.11 rests on the closure defect d_cl. That is only an upper bound on the Markov defect d_M, which is the quantity the clause uses.
- **Agency cap.** The cap of 1/7 holds only under a reading of the group model that the candidate does not state.

**Weakest point:** the convention that relayed own-sensing noise is a private input. The verdict depends on it.

## 1. Independent recomputation (computed)

My code is written from the report's specification; I did not import or copy the candidate's code. The method also differs:
- all 2 × 64 policies are enumerated explicitly, with no count cells;
- Sigma^c is assembled from a per-replica private-noise recursion plus a separate world-innovation (common-mode) recursion for the pair;
- the exact d_M uses a Kalman filter on the coarse path;
- the inference defect uses an exact joint covariance per policy path, not Monte Carlo.

| Quantity | Candidate | Mine |
|---|---|---|
| r(A), real-time (160 pairs) | 8.4311 ± 0.0025 | 8.4302 ± 0.0027 |
| r(A), frozen (160 pairs) | 8.4207 ± 0.0031 | 8.4287 ± 0.0031 |
| mixture part of beta, real / frozen | 2.15e-5 / 1.47e-5 | 2.16e-5 / 1.42e-5 |
| mean-coupling baseline, real / frozen | 7.3695 / 7.3606 | 7.3688 / 7.3675 |
| largest sub-region (3 of 4) | 2.3002 | 2.3001 |
| mechanism medium, real (2 revisers) | 5.959 ± 0.016 | 5.943 ± 0.016 |
| mechanism medium, real (1 reviser) | 6.023 ± 0.031 | 5.953 ± 0.025 |
| mechanism medium, frozen | 6.006 ± 0.010 | 6.005 ± 0.009 |
| N_hab, real / frozen | 2.379 / 2.383 | 2.382 / 2.372 |
| N_pr (redrawn every round), real / frozen | 2.844 / 2.844 | 2.848 / 2.850 |
| inference, best constant / claimed variance / reverse | 0.0593 / 0.0671 / 0.0560 | 0.0593 / 0.0671 / 0.0560 |
| agency, G1 full policy, real | 0.0714 (one run); 0.0729 ± 0.0009 | 0.0725 |
| agency, G1 full policy, frozen | 0.0748 | 0.0748 |
| agency, sensors only, real / frozen | 0.645 / 0.998 | 0.654 / 0.998 |
| C12 cap, real / frozen | 0.1107 / 0.0749 | 0.1109 / 0.0749 |
| lower corner of the ±1% box: r(A) / medium | 8.198 / 6.002 | 8.192 ± 0.003 / 5.978 |
| exact stationary d_M at fixed profiles | 7.055e-5 to 1.309e-4 | same to 4 digits, by a different method |

**Negative controls (all behaved as required):**
- Fresh relays (independent copies of the relayed noise): r = 1.0029 (real) and 1.0020 (frozen).
- Rc = 1e6: r = 1.0002.
- Habit-only agency model: index exactly 0.
- One member's mean in place of the average: inference 0.0943, above 0.0593.
- Exact I_t never exceeds d_cl(t): 0 violations across all searches.
- My first fresh-relay control wrongly gave 2.80. The bug was in the control: it kept the cross-receiver blocks of the relayed-noise covariance. I fixed it and reran; the main computation was unaffected.

## 2. Attacks that failed

1. **N_eff and N_inf are inapplicable (proved).**
   - The active states are an attention set of world and message channels plus a single-option speech act (def:fw-system, 02_framework.tex:13). The performative component is zero.
   - def:agy-nulls (05_agency.tex:333) declares these two nulls inapplicable "in a model without acts".
   - The private sensor is read only by its owner, so opening it creates no channel for others. This is what separates I** from failed route R5.

2. **Mechanism medium (interpretive; the verdict does not depend on it).**
   - The medium places all 8 agents on one world component under the same mechanism. This follows the precedent at 07_formation.tex:173: remove the structural difference, keep the attention mechanism.
   - For two equal niches the mean-coupling baseline is 1 + (24/7)b. That is always below r(A) = 1 + 4b, so only the mechanism medium can close the window, and it sits 1.9 below r0.

3. **"For each constant of the selector" (05_agency.tex:333) (interpretive).**
   - Taken literally over every r0, the clause is unsatisfiable for every population: above r(A), both the model and the null select nothing.
   - Read as "each admissible r0", every r0 in (7.37, 8.43] has the nulls selecting nothing, since their largest contrasts are at most 2.85.

4. **N_lp and N_fr under the real-time protocol.**
   - The shared reviser clock leaves beta = 1e-6 ± 1e-6.
   - Under the declared contrast selector, no region qualifies whatever the sign: r ≈ 1.0001 if beta > 0, a non-diffusive precision and so no collective if beta < 0.
   - A negative beta would matter only if the mutual-information substitute (s04_collectives.tex:268) were the declared selector. It is not.

5. **Moment bound (M) (08_scale.tex:23): holds, by a simpler argument than P8 (proved).**
   - Each member's filter is correctly specified for its own data: the relayed v_j(t-1) is independent of the receiver's prior error.
   - So the actual prior error covariance equals the claimed P^-, which the own-sensor Riccati bound controls.
   - P8's numerically verified contraction step is therefore not needed.

6. **Inference clause.** It also holds under the fully pre-declared claimed-variance encoding (0.0671 < 0.09), so the post-hoc "best constant" choice is not load-bearing.

## 3. Corrections to the candidate

### 3a. Memory clause

**The concession's evidence is the wrong quantity (computed).**
- "The literal supremum lies in [0.0266, 0.0988]" is wrong at the lower end. The 0.0266 is d_cl, and data processing makes d_cl only an upper bound: d_M ≤ d_cl.
- At the candidate's worst pattern (base 1110 sustained, then ((0,0,0),(0,0,0),(0,0,0),(1,3,3))), my d_cl is 2.6644e-2, reproducing the candidate's. The exact I(y_{t+1}; y_{0:t-1} | y_t) there is **2.4e-5**, and over the following 21 rounds it is at most 1.0e-3.

**Searches for the largest exact d_M (computed; numerical search, not a proof):**

| Search | Largest exact d_M |
|---|---|
| Exhaustive single-round switches from 5 bases | 2.74e-3 |
| Beam search, depth 12 | 1.10e-2 |
| Periodic hill-climb, periods 2 / 4 / 8 / 16 | 1.12e-2 / 1.38e-2 / 1.58e-2 / **1.62e-2** |
| Simulated annealing over aperiodic 24-round sequences | 1.62e-2 |
| Statuses held fixed (attention only; reachable under real-time) | 6.8e-3 |

All witnesses are frozen-reachable. They need several status flips per round, so they are not reachable in real time.

**So the strict status is open, not refuted:**
- sup d_M lies in [0.0162, 0.0988]. The upper end is the candidate's grid bound, which is not interval arithmetic.
- alpha_M = 0.02 is consistent with every pattern found, with a margin of 0.0038, but it is not certified.
- alpha_M = 0.11 is shown sufficient only by that grid bound, and not shown necessary.

**"Typical paths" is not a reading of the stationary supremum.**
- Proved: habits have full support, gamma is finite and the decision states are bounded, so every finite policy pattern has probability bounded below from any state. Almost every infinite path therefore realizes every reachable finite pattern infinitely often.
- Numerical: the d_M values computed for those patterns after a 120-round warm-up.
- Consequently sup_t along almost every path is at least the pattern supremum. A 320-step window does not estimate it.

**The clause is applied by extension (interpretive).**
- eq:agy-interior (05_agency.tex:14-17) is stated with constant (A, B, Q^n). In I**, A(t) and Q^n(t) depend on the attention path.
- The input-conditional form's assertion that "this value does not depend on the input path" (05_agency.tex:20) is false for I**.

### 3b. The agency cap of 1/7 is reading-dependent (computed)

P5 claims "every admissible group model has the form U64^4(M) x P^s_g(sigma)" because "channels of the other niche carry no information about eta_C". That justification is not right as stated:
- Under 05_agency.tex:11, eta_C includes "the active channels of non-members that they hear".
- The other niche's channels into A are exterior-facing sensory channels that a policy can open, so they are slots (05_agency.tex:157).

Two readings follow:
- **(i) Pinned preferences:** each slot's pragmatic term is the controlling member's own (05_agency.tex:161; supported by eq:agy-member-efe and lem:agy-decomposition). Members of I** have no pragmatic term on message channels, so the group's information term can only favor those slots. The best admissible model removes it with a degenerate belief on their contents. **The candidate's class and cap stand.**
- **(ii) Free preferences:** the slot-product preference is a free component of the declared class. A cost on those slots explains the avoidance of the other niche's channels, which is half of the attention surprise (4 ln 8 of 4 ln 64). **Full-policy index: 0.517 (real), 0.537 (frozen).** The control at zero cost reproduces K1.

The verdict Agency0 > 0 holds under both readings.

### 3c. Class G2 is not admissible under the declared coarse variable

G2's belief variance depends on the covariance state. def:agy-group-model (05_agency.tex:157) requires q_C "declared as a function of the collective's coarse state", and here the coarse state is the scalar mean average. G1 gives a higher index, so the frontier should be quoted from G1: at least 0.069 (real) and 0.0748 (frozen), not 0.066.

### 3d. Only the frozen protocol is def:fw-system literally

- The real-time protocol is not def:fw-system as written: the non-revisers do not redraw sigma (02_framework.tex:17, "Active states are drawn from the policy posterior").
- Its shared reviser clock is neither shared drive nor a private input in def:agy-order-parameter (05_agency.tex:297).
- The frozen protocol is def:fw-system literally, with simultaneous per-round draws, and in I** it coincides with the (P4) stationary law. The literal-framework grade is therefore the frozen one.

### 3e. Two items not addressed

- The N_fg diagnostic is not reported, although def:agy-nulls says "diagnostics are reported beside the verdict".
- The "once" variant of N_pr that tab:agy-nulls permits is covered only by failed route R3, from an earlier instance, not computed for I**.

## 4. Weakest point (interpretive; the verdict depends on it)

The whole coupling rests on not conditioning on v_j(t) and rho_j(t) after they are relayed.

**The literal text supports the candidate:**
- 04_collectives.tex:15 puts "the sender-side noise of a broadcast" in the active channel. A relayed raw reading is speech content, not channel noise.
- def:agy-order-parameter lists sensing noise as a private input.
- The level-0 network (02_framework.tex:323) likewise carries the sender's sensing noise to receivers through local noise that is not conditioned on.

**The definition's purpose clause does not:** def:col-world-conditional (04_collectives.tex:131) conditions "so that the remaining local noise is specific to each receiver". That fails in I**: each v_j(t) enters, as fresh noise, the updates of its sender and of every receiver. Under that reading r(A) ≈ 1; both independent-copy variants give 1.002 to 1.003.

**Next weakest:** the open subset (O6). It rests on box evaluations; continuity is not proved.

## 5. Grade I would stand behind (computed)

**Frozen protocol** (the literal def:fw-system):

| Grade (r0, alpha_M, alpha_I, alpha_pr, Agency0) | Holds when |
|---|---|
| (7.9, 0.02, 0.09, 0.01, 0.074) | alpha_M = 0.02 read on typical paths |
| same grade, alpha_M = 0.02 | open under the strict supremum (best exact witness 0.0162) |
| (7.9, 0.11, 0.09, 0.01, 0.074) | strict supremum, relying on the candidate's grid bound |
| Agency0 frontier 0.0748 | pinned slot preferences |
| Agency0 frontier about 0.54 | free slot preferences |

**Real-time:** Agency0 frontier 0.069 to 0.0725 (G1) under pinned preferences, 0.517 under free preferences. The same memory caveat applies.

All grades hold only under the relayed-noise convention.

## Files

Everything is in `C:\Users\chris and christine\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round3\attack-strict-construction\`:
- Libraries: `mylib.py`, `memlib.py`
- Collective clause: `a1_collective.py`, `a1b_nc1.py`
- Mechanism medium: `a2_medium.py`
- Nulls: `a3_nulls.py`
- Memory: `a5_memory_exact.py` and `a5b`–`a5h`
- Inference: `a6_inference.py`, `a6b_inference_claimed.py`
- Agency: `a7_agency.py`
- Box corner: `a8_corner.py`
- Each script's output is the matching `*_out.txt`.

No repository or vault file was edited. Every run was single-threaded, one at a time, and under two minutes.

## round3: agency-frontier

VERDICT: Under the full-policy reading (O2(e) answered yes), the agency clause does not block existence in the private-slot niche class. I computed a design (D1) that meets every clause of def:agy-meta-agent, with full-policy index 0.8000. D1 has two niches of two agents, message capacity 1, uniform habits on the four message sets of size at most 1, eight costly private world slots per member at Rs = 10, and one precision gamma = 400. Its grade is (r0, alpha_M, alpha_I, alpha_pr, Agency0) = (3.7, 0.02, 0.03, 0.01, 0.75). The grade holds at 17/17 points of a ±5% box under both the mechanism and the mean-coupling baseline. N_eff and N_inf are inapplicable under every typing, because the model has no acts. The deliberation reading O2(f) has no effect, because each member's choice depends only on its own state. Two bounds are proved. First, with habits held fixed the index equals KL_s|a/(KL_a+KL_s|a) minus the slot misfit. Second, the N_hab and collective clauses force KL_a >= n·d(1-delta||pi*): exactly for n = 2 given a numerically monotone rho, and for n >= 3 conditional on the numerically supported hypothesis H_mon. On the computed grid pi* ranges from 0.46 to 0.75. The resulting cap per member with m binary slots is m ln2/(m ln2 + d(1-delta||pi*)). The bound is attained to within 1e-8, so the frontier's supremum is 1, which no design attains. Four levers approach it: enlarging the slot array gives m/(m+2) for D1; shrinking the support to two sets gives m/(m+1); soft attention gives KL_a = 0.20 nats per member and index 0.965 at m = 8 with window margin 0.86; precise slots that flood N_hab give pi* = 1 but conflict with the worst-path memory reading. The weakest point is that the index gets there by padding: it is the KL-weighted average of an attention component the class cannot explain and a slot component whose departure from habits (never opening costly slots) the group EFE explains trivially. Whether such components count is an author decision that the literal definition does not settle.
POSITIVE: True

## 0. Verdict

**D1 is a meta-agent of grade (3.7, 0.02, 0.03, 0.01, 0.75) under the full-policy reading** (computed). The full-policy index is 0.8000 and the grade holds at 17/17 points of a ±5% box under both baseline readings. The frontier's supremum is 1 and no design attains it:
- **Proved bound.** Under N_hab plus the collective clause the attention surprise satisfies KL_a ≥ n·d(1−δ‖π*). This is exact for n = 2 given a numerically monotone ρ, and conditional on H_mon (numerical) for n ≥ 3.
- **Cap and attainment.** Combined with C12, Agency ≤ m ln2/(m ln2 + d(1−δ‖π*)) per member with m binary slots. D1-type designs attain the cap to within 10⁻⁸.

**Weakest point (interpretive).** The index reaches these values by padding with costly slots that the members never open. The group EFE explains that departure from habits through the members' own slot cost, with no redundancy or coordination term involved.

## 1. Target, readings, conventions

**Target.** open:agy-meta-agent-exists (s05_agency.tex:295-297) asks for a population and a set C meeting every clause of def:agy-meta-agent (05_agency.tex:379-381) with r0 > 1 and Agency0 > 0. Here O2(e) is answered yes: "the members' joint policies" in def:agy-agency-index (05_agency.tex:240-246) include attention to internal channels.

**Definitions used.**
- def:col-world-conditional (04_collectives.tex:130-132)
- diffusive class (04_collectives.tex:147-151)
- def:col-contrast with the second-moment convention (04_collectives.tex:182-188, at :187)
- def:col-baseline clause (c) (04_collectives.tex:197-209, at :202)
- def:col-collective (04_collectives.tex:214-221)
- def:agy-closure (05_agency.tex:13-24; constraint remark at :27)
- def:agy-group-model with (P0)-(P4) (05_agency.tex:156-169)
- def:agy-nulls and tab:agy-nulls (05_agency.tex:332-360)
- prop:agy-tests(b) (05_agency.tex:367)
- def:fw-system: attention set, speech act, records and performative component at 02_framework.tex:13; policy posterior at :17
- expected free energy eq:fw-efe (02_framework.tex:29-31)

**Readings adopted** (each is marked with whether the verdict depends on it).
- **R-e (premise):** policy = (message-set attention, slot pattern), habits fixed and uniform. If the slot-only reading is used instead, D1's index is 1.0000. Depends: no.
- **R-outsider:** reading a non-member's relay counts as internal attention, which is the conservative choice. If such channels are counted as slots, the admissible class is larger and the index is ≥ 0.8 (index is nondecreasing in the class, 05_agency.tex:249). Not computed. Depends: no.
- **R-base:**
  - Clause (c) mechanism medium: one world component, N = 4 agents, the support's exchangeable closure (every 1-set), the same slots, γ and ψ.
  - Mean-coupling clause (c): checked too.
  - Clause (b) on the potential communication graph: that graph is complete (K4), so (b) coincides with the mean-coupling value.
  - Both pass at r0 = 3.7. Depends: no.
- **R-pr:** partner randomization redrawn every round. Quenched draws were not computed (record R3). Depends: yes.
- **R-diff:** "differs" holds for every constant of the selector in the window, which requires null contrast ≤ the window's lower edge. Depends: no for D1, since all nulls are ≤ 2.06 against 2.49. Theorem A uses this reading; under a single declared r0, b is replaced by r0 and the bound weakens.
- **R-mem:** both the stationary Markov defect and the worst reachable per-step d_cl pass. For the worst-path reading, single- and two-round deviations and a 60-round stretch without a relay were explored; the supremum over all paths is not proved. Depends: no at the explored depth.
- **R-inf:** best-constant, claimed-variance and reverse-direction KL all pass at α_I = 0.03. Depends: no.
- **O2(a):** moot, because there are no acts. A private slot is a world channel in the attention set (02_framework.tex:13) and relays are speech acts, so N_eff and N_inf are inapplicable by 05_agency.tex:333 ("in a model without acts"). Depends: no.
- **O2(f):** moot by Lemma 1. Depends: no.
- **R-pad (new):** costly slots that are never opened are admissible policy components of the index. Depends: yes. This is the weakest point.

**Conventions.** These follow the record:
- Σ^c is computed as E[Cov(e|η)] by two replicas sharing w.
- The contrast coordinate is the prior error of η_t.
- KL(p‖q) = E_p ln(p/q).
- Closure is computed in the attack's convention (round2_attack_persistent/run3_closure.py): interior = members' prior means; blanket = own sensors, slots and the senders' sensings carried by relays; interior noise = relay read noise plus computation noise.

## 2. Class NC and design D1 (declared before the deciding runs)

**Class NC** (one niche shown; there are K independent niches):
- World: η_{t+1} = F η_t + w with F = 0.9 and Q = 0.05.
- Own sensor: s_i = η_t + v_i with R = 1, read every round.
- Raw relays: the own reading is relayed to every other agent with one-round latency, delivered as s_j(t−1) + ν_ij with receiver-specific noise Rc = 0.1.
- Filters: exact filters on (η_t, η_{t−1}) with computation noise q_c = 10⁻⁴ I₂.
- Private slots: m binary world slots per member, each reading η_t + ρ with noise Rs, read by the owner only and not relayed. Slot habits are uniform on {0,1}^m and each open slot costs ψ.
- Attention: message sets of size ≤ κ_msg from a declared support S with uniform habits.
- Policy: G = −I(x_{t+1}; own sensor + k slots + c relays) + ψk, with one γ for attention and slots.

**D1.**
- n = 2 and K = 2, so N = 4.
- κ_msg = 1, with the canonical support {∅, {mate}, {o1}, {o2}}, so |S| = 4.
- m = 8 slots at Rs = 10.
- ψ = g_max + 0.06 = 0.06702, where g_max = 0.00702 is the largest single-slot gain over reachable states.
- γ = 400.
- Coarse variable: the scalar collective average of the members' prior means.
- Agency class G2: q_C is a translate of the member's anticipated belief (v* = 0.12216), slot likelihood N(η, Rs), cost ψ, habits fixed, γ_C ∈ [0, ∞). Class G1 frees v_C.
- Decision state: the stationary state X*.

**Revision.** Rs was changed from 1 to 10 after d1_memory_worst showed a reachable all-slots-open deviation with d_cl = 0.20 at Rs = 1. Every clause other than N_hab is unchanged by the revision, because slots stay closed.

## 3. Per-clause table for D1 (center point; box column = ±5%, 17-point 2^(8−4) design plus center)

| Clause (file:line) | Value | Margin | Status | ±5% box |
|---|---|---|---|---|
| Σ^c structure, :130-132, :187 | α = 0.0134391, β = 0.0224783. Cross-niche block exactly 0. MC check 4.339 ± 0.020 (z = −0.32). | – | structure proved (Lemma 1, C1); values computed (exact Lyapunov) | – |
| Diffusive, :147-151 | Coupling 28.643, leak 17.125. | – | proved given β > 0 | – |
| Collective, :214-221 | r(A) = 4.345220. Spanning regions: 0.374 (size 2), 0.642 (size 3), 1.000 (size 4). Leak ratio 1. | r(A) − r0 = 0.645 | computed | min r(A) 3.837 |
| Mechanism baseline, :202 | 2.493156 exact (MC 2.502 ± 0.013). Window (2.493, 4.345]. | r0 − b = 1.21 | computed | max 2.611 |
| Mean-coupling baseline | 1 + (2/3)(r(A) − 1) = 3.230. | r0 − b = 0.47 | computed | max 3.585 (r0 = 3.5 failed at 2/17 points; re-declared 3.7) |
| N_hab (D) | 1.346 ± 0.007 (mate read 1/4 of rounds, slots open with probability 1/2). | 1.15 below b | numerical | ≤ 1.387 |
| N_pr (D) | 1.761 ± 0.007. Test with 999 draws: max 2.058 against S0 = 4.345, p = 0.001. Full-model control p = 0.56. | 0.73 | numerical | ≤ 1.851 |
| N_lp, N_rn, N_fr (D) | β = 0 exactly (MC 1.006 ± 0.004). | – | proved (Lemma 1c) | – |
| N_eff, N_inf | Inapplicable: no performative component. | – | proved by 05_agency.tex:333 under every typing | – |
| N_ex (S) | Fusion of raw readings is already exact, so the model is unchanged: inapplicable, and trivially survived at 4.345. | – | proved | – |
| Type E | N_w predicts {A, B} from access, so the claim is restricted, as in C11. N_code makes no prediction. N_fg not computed. | – | interpretive | – |
| Memory, :20-21 | Stationary d_M = 4.37e-5. Per-step d_cl = 8.91e-4. Worst reachable single-round deviation 9.1e-3 (one member opens all 8 slots). Two-round 2.9e-3. 60 rounds without a relay: 2.7e-3. | 0.011 under worst path | computed | worst d_cl ≤ 0.0181 |
| Inference | Best-constant 0.01867 (exact equals MC). Claimed-variance 0.02043. Reverse 0.01885. | 0.011 | computed | ≤ 0.0228 |
| Agency, :240-246 | KL_a = 2.772588 = 2 ln 4. KL_s\|a = 11.090355 = 16 ln 2. Slot misfit 1e-16. Index 0.800000 (G2 = G1). Slot-only index 1.0. | 0.05 | computed | 0.8000 at all 17 points |
| Ω_int(A\|ζ_B) | Positive: β > 0, and A does not depend on ζ_B. | – | proved given β | – |
| Choice determinism | P(attention reads mate) = 1 − 1.18e-8. P(any slot open per member-round) = 2.07e-10. EFE gaps 0.0484 nats (attention) and 0.0609 nats (slots), so γ·gap = 19.3 and 24.4. | – | computed | – |

The full grade holds at 17/17 box points under both baselines (d1_box_r37_out.txt). The negative control at the center with Rc = 2 gives r(A) = 1.907 and fails the collective clause, as required.

## 4. Proofs

**Lemma 1 (proved).** In NC, member i's round-(t+1) observations are its own sensor, its own slots and the mates' round-t own readings. None of these depends on another member's round-(t+1) policy. Consequences:
- (a) G_i(π) = G_i(π_i). The members' policy law at a decision state is the product of their posteriors, and (P4) and the synchronous rule share that law.
- (b) The niches share no inputs, so the cross-niche blocks of Σ^c vanish. Exchangeability makes each niche block compound symmetric, so C1 applies.
- (c) Under N_lp, N_rn and N_fr, relays carry noise independent of v_j or deterministic content. Each member's claimed covariance, and hence its policy path, depends only on its own history. So e_i and e_k are independent given η, and β = 0.
- (d) A region meeting both niches has r ≤ 1. Take f = |C∩B|·1_{C∩A} − |C∩A|·1_{C∩B}, which is orthogonal to 1_C. Then L_C f = 0, so ξ_in ≤ ε ≤ ξ_out.

**Lemma 2 (C12 identity, proved).** When the class holds habits fixed and G_C depends on slots only, every model factors as P_g = E^a ⊗ P^s_g. By the chain rule,

  Agency = 1 − [KL_a + inf_g E_{P_a} KL(P_{s|a}‖P^s_g)] / [KL_a + KL_s|a].

**Proposition P (padding, proved).** By Lemma 2, Agency = (KL_s|a − mis_s)/(KL_a + KL_s|a), where mis_s = inf_g E_{P_a} KL(P_{s|a}‖P^s_g) is the slot misfit. If the slot policy sets grow while mis_s = o(KL_s|a), then Agency → 1 for any fixed KL_a. So with fixed habits the index is not invariant under adding policy components whose departure from habits the class explains.

**Theorem A (attention surprise).** Setting:
- Let X* be the event that a member's message set contains all n − 1 mates. When κ_msg = n − 1 this is the single set x*.
- Let ρ(π) be N_hab's contrast when attention is drawn i.i.d. per round from π·δ_{x*} + (1 − π)·δ_zero (δ_zero is a zero-informative set) and slots follow the design's habits.
- Let b be the window's lower edge and π* = sup{π : ρ(π) ≤ b}.

Hypotheses:
- (i) The differ clause holds against N_hab in reading R-diff, so r_hab(A) ≤ b.
- (ii) H_mon: moving habit mass to a message set with at least as many informative channels does not lower N_hab's contrast.
- (iii) ρ is strictly increasing.

Conclusion: if the full model's attention at decision state X has P(X*|X) ≥ 1 − δ ≥ π*, then

  KL(P_a(·|X) ‖ E^a) ≥ n·d(1 − δ ‖ π*), with d(p‖q) = p ln(p/q) + (1 − p) ln((1 − p)/(1 − q)).

With C12 and KL_s|a ≤ Σ_i ln|A^s_i|:

  Agency ≤ Σ_i ln|A^s_i| / (Σ_i ln|A^s_i| + n·d(1 − δ‖π*)).

Proof.
1. Since E^a is a product, KL(P‖∏E_i) = Σ_i KL(P_i‖E_i) + TC(P) ≥ Σ_i KL(P_{a_i}‖E_i).
2. Data processing on the indicator of X* gives KL(P_{a_i}‖E_i) ≥ d(P(X*)‖E(X*)).
3. By (ii), move all non-X* habit mass down to zero-informative sets. Then r_hab(E) ≥ ρ(E(X*)). By (i) this is ≤ b, so E(X*) ≤ π* by (iii).
4. d is increasing in p on [q, 1], since ∂_p d = ln(p/q) − ln((1−p)/(1−q)) ≥ 0. It is decreasing in q on [0, p], since ∂_q d = (q − p)/(q(1 − q)) ≤ 0. Hence d(P(X*)‖E(X*)) ≥ d(1 − δ‖π*).
5. Sum over members. The map x ↦ x/(x + a) is increasing in x and decreasing in a, which gives the agency bound. ∎

For n = 2, every message set except {mate} is zero-informative, so (ii) is vacuous and the bound needs only (iii). Status: proved given (iii) for n = 2; for n ≥ 3, conditional on (ii) and (iii).
- (iii) monotone: 12/12 rows (pistar_out.txt).
- (ii) holds at all 10 comparisons. n = 4: π = 0.3 gives 2.102 < 3.476 < 5.503; π = 0.5 gives 3.07 < 4.42 < 6.16; π = 0.7 gives 4.486 < 5.657 < 6.910. n = 3: π = 0.3 gives 1.853 < 3.592; π = 0.7 gives 3.789 < 4.890.

**Corollary (uniform habits on a support).** With κ_msg = n − 1, |S ∩ X*| ≤ 1, so E(X*) = 1/|S|. Hence |S| ≥ 1/π* and KL_a ≥ Σ_i d(P(x*)‖1/|S|).

**Infimum (proved from the theorem's structure).** Let p_full* be the concentration at which r(A) = b. In the slot-neutral class p_full* = π*, so the clause-forced KL_a can be made arbitrarily small (P(X*) ↓ π* and E(X*) ↑ π*) when habits are general and γ is free. With uniform habits on a support, the infimum per member is d(π*‖1/⌈1/π*⌉), for example 0.012 at n = 2, K = 2.

## 5. Frontier against the levers

**Threshold π* (κ_msg = n − 1).** Numerical; ρ has standard error ≤ 0.07. Columns give π* at K = 2, 3, 4.

| n | Rc = 0.05 | Rc = 0.1 | Rc = 0.2 | Rc = 0.4 |
|---|---|---|---|---|
| 2 | 0.574, 0.501, 0.465 | 0.577, 0.506, 0.471 | 0.580, 0.503, 0.469 | 0.591, 0.519, 0.488 |
| 3 | 0.687, 0.604, 0.571 | 0.692, 0.612, 0.580 | 0.685, 0.607, 0.575 | 0.701, 0.625, 0.593 |
| 4 | 0.724, 0.657, 0.625 | 0.724, 0.655, 0.624 | 0.734, 0.670, 0.638 | 0.748, 0.688, 0.656 |

So ln(1/π*) per member lies in [0.29, 0.78]. It grows with K (the baseline falls), falls with n, and depends weakly on Rc. A second run gave π*(2, 3) = 0.493, so |S| = 2 is marginal at n = 2, K = 3; at n = 2, K = 4 the slot-neutral class needs |S| ≥ 3. Weak slots rescue |S| = 2 there: D2's N_hab of 1.76 is independent of K, against b = 2.135.

**Index against m (exact computation equals the formula to 4 digits; d1_agency_out.txt).**

| Design | Formula | m = 1 | m = 2 | m = 3 | m = 8 | m = 18 | m = 50 |
|---|---|---|---|---|---|---|---|
| n = 2, canonical support (\|S\| = 4) | m/(m+2) | 0.333 | 0.500 | 0.600 | 0.800 | 0.900 | 0.962 |
| n = 2, \|S\| = 2 | m/(m+1) | 0.500 | – | – | 0.889 | 0.947 | 0.980 |
| n = 4, canonical support (\|S\| = 64) | m/(m+6) | 0.143 | – | – | 0.571 | 0.750 | 0.893 |
| n = 4, \|S\| = 2 | m/(m+1) | – | – | – | 0.889 | – | – |

Theorem A cap at n = 2, K = 2: 0.693m/(0.693m + 0.545), which needs m ≥ 1, 4 and 8 for Agency0 = 0.5, 0.8 and 0.9.

**Other designs.**
- **D2** (n = 2, support {{mate}, {o1}}; numerical): N_hab 1.760. N_pr is 1.746 over all others and 2.204 ± 0.015 over the support's potential partners, against b = 2.493. Index 0.889 at m = 8.
- **D3** (n = 4, |S| = 2, m = 8; computed and numerical): r(A) = 8.628, b = 4.754, N_hab 2.442, N_pr 2.927, d_M = 7.1e-5, d_cl = 2.9e-3, inference 0.058, index 0.889. Not done for D3: the N_pr test, the worst-path memory scan, and a box.
- **D4** (soft attention, γ = 29, ψ = g_max + 20/γ, |S| = 2; numerical):
  - P(mate) = 0.807; r(A) = 3.358 ± 0.012 against b = 2.493 and a mean-coupling baseline of 2.572.
  - N_hab 1.738; N_pr 1.762 over all others and 2.239 over the support's potential partners; inference 0.0215.
  - KL_a = 0.203 per member-round; index 0.773 at m = 1 and 0.965 at m = 8. The γ = 400 control returns 0.5 and 0.8889.
  - Not done for D4: the memory clause and the N_pr test.

**Soft-attention curve** (n = 2, K = 2, |S| = 2). Margin is r(A) − b.

| P(x*) | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
|---|---|---|---|---|---|
| Window margin | 0.06 | 0.40 | 0.86 | 1.33 | 1.85 |
| KL_a per member | 0.020 | 0.082 | 0.193 | 0.368 | 0.693 |
| Index, m = 1 | 0.972 | 0.894 | 0.782 | 0.653 | 0.500 |

**κ lever (computed).** At κ_msg = n the window closes only at (n, K) = (2, 2), where the medium gives 4.611 against 4.345. It stays open elsewhere, for example (4, 2): 6.570 against 8.628. Ties then lower ln(|S|/|S*|) under the canonical support, for example ln(99/5) = 2.99 against ln 64 = 4.16 at n = 4.

**Flooding lever (numerical).** Under N_hab, private slots raise each member's own precision and push its contrast down, even with attention pinned on the mate (ρ_flood(1)). Against b = 2.493 at n = 2:

| Rs | 1 | 2 | 3 | 5 | 10 |
|---|---|---|---|---|---|
| ρ_flood(1) | 1.253 | 1.524 | 1.778 | 2.186 | 2.775 |
| Worst single-round d_cl | 0.202 | 0.101 | 0.060 | 0.0275 | 0.0091 |

At n = 4 (Rs = 1): ρ_flood(1) = 1.797 against b = 4.754. So precise slots set π* = 1 and remove the N_hab bound on attention, but they conflict with the worst-path memory reading at α_M = 0.02. At Rs = 5 both hold at α_M = 0.03.

## 6. Scripts and deciding outputs

All files are in `C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round3\agency-frontier\`. Runs were single-threaded, one at a time, each under 30 s. No repository or vault file was edited.

**Library and declarations.** flib.py (exact Lyapunov, exact medium recursion, vectorized two-replica Monte Carlo, closure, agency), design.py, agency_lib.py.

**Validation.** v1_validate.py → v1_out.txt:
- A8 exact = 7.425938, matching round 1.
- Medium: exact 2.4932 against MC 2.5045 (z = 1.62).
- Negative controls: dead relays give 1.000; independent worlds give 43.3.

**Exploration (not deciding).** x1_explore.py, x2_explore.py.

**Deciding runs.**
- d1_contrast.py → d1_contrast_out.txt, plus the Rs = 1 output.
- d1_npr_test.py → d1_npr_test_out.txt.
- d1_closure.py → d1_closure_out.txt.
- d1_memory_worst.py → d1_memory_worst_out.txt.
- d1_agency.py → d1_agency_out.txt.
- pistar.py → pistar_out.txt.
- d23_and_tension.py → d23_and_tension_out.txt.
- d4_soft.py → d4_soft_out.txt.
- frontier_table.py → frontier_table_out.txt.
- d1_box.py → d1_box_out.txt (r0 = 3.5: 15/17 under mean coupling).
- d1_box_r37.py → d1_box_r37_out.txt (17/17).

**Calibration.**
- v2_d3_diag.py: spectral radius 0.63, no bias.
- v3_se_calib.py: empirical SD / batch SE = 0.93 (D1) and 0.91 (D3).

**Expectations that failed.**
- The r0 = 3.5 box: the mean-coupling baseline reached 3.585.
- ⌈1/π*⌉ = 2 at n = 2, K = 3: π* came out at 0.493 in one run.
- The D1 memory clause at Rs = 1, which led to the redesign at Rs = 10.

## 7. Weakest point and unresolved obligations

**Weakest point (interpretive).** By Proposition P, D1's index is 0.8 because 80% of the members' departure from habits is the closure of 16 costly slots. The group EFE explains that closure through the members' own costs (G_C contains Σψ). The law is a product law, with no redundancy or coordination term involved. The literal definition counts it; 05_agency.tex:251 calls the index as-if representability, not efficacy. Under a rule that excludes padding (for example, restricting the index to components the collective structure depends on), the frontier is the open problem below.

**Unresolved obligations, in order.**
1. **Author decision R-pad:** do never-used or cost-closed policy components count? A related question: should the index be normalized per component?
2. **No-padding frontier:** the frontier when only slots used with positive probability count. Deterministic epistemic slots on one η have diminishing returns, roughly at most 3 slots per member at γ = 400. A heuristic estimate gives a cap near 0.8 at n = 2; it is not computed.
3. **H_mon for n ≥ 3:** a proof (currently numerical).
4. **Continuity (O6) for the open subset:** the box is numerical only.
5. **Quenched N_pr:** reading R-pr is still needed.
6. **Memory supremum:** the supremum over all reachable multi-round paths.
7. **Unrun checks on D3 and D4:** D3's N_pr test and memory scan; D4's memory clause.
8. **Relayed-slot variant:** the variant in which slot readings are relayed was not computed.

## 8. Strongest supported result and next action

**Result.** Form (A), computed: D1 meets every clause at (3.7, 0.02, 0.03, 0.01, 0.75) under the full-policy reading. It is independent of O2(a), O2(c) at the baseline level, and O2(f). It needs R-pr and R-pad. The frontier's supremum is 1, and the cap is proved.

**Next action that would change the answer.** The author rules on R-pad. If padding is excluded, compute the no-padding frontier: slots that are used and relayed, so that G_C's redundancy term is active and the slot law is not a product law.

## round3 attack: agency-frontier

# Attack on agency-frontier's D1 (round 3)

## 0. Verdict

**Under the readings the candidate states, D1 holds at grade (3.7, 0.02, 0.03, 0.01, 0.75).** I rebuilt the model from the written specification with my own code, using different numerical methods, and every deciding number matches to the printed digits (computed). Two of the candidate's reading claims are wrong, however, and each one decides a clause. Three frontier claims are also wrong.

1. **The claim "R-outsider … Depends: no" is refuted (computed; the reading is interpretive but literal).**
   - **Why outsider channels are slots.** 05_agency.tex:11 defines η_C to include "the active channels of non-members that they hear". Under def:col-partition (04_collectives.tex:17-26), a member's channel y_{i,o} reads o's speech channel, which is not a collective variable (y_ij is "the component of i's sensory states that reads the channel written by j", 02_framework.tex:17). So attending o1 or o2 opens an exterior-facing sensory channel, which is a slot of def:agy-group-model (05_agency.tex:157). That slot carries G_C term −I_{q_C}(η_C; o) = −½ln(1 + n_o V_o/R_c), and it has no pragmatic term, because each slot's pragmatic term is that of the member who controls it (:161) and D1 puts no cost on relays.
   - **The class is not specified on these channels.** The declared class G2 (a translate of a belief about η^A) never says what V_o is, that is, q_C's variance for a non-member's message.
   - **Calibrated beliefs give index 0.** Any q_C with V_o ≥ R = 1 (the non-member's own sensing noise, which nothing in A observes; prior value 1.263) makes the misfit increase in γ_C from γ_C = 0. The infimum is then the habit-only model, so **D1's index is exactly 0** and the agency clause fails for every Agency0 > 0.
   - **What the stated grade needs.** An index of at least 0.75 requires V_o ≤ about 1.2e-3 under G2, or about 1.4e-3 under G1 with v_C free. That is a belief about the non-members' messages that is overconfident by a factor of roughly 800.
   - **The supporting argument is invalid.** The candidate argued "the admissible class is larger and the index is ≥ 0.8 (nondecreasing in the class, :249)". Reclassifying channels changes G_C for every model in the class; it does not add models. Counterexample: V_o = 1 gives index 0.
2. **Partner randomization drawn once fails (computed exactly).** tab:agy-nulls (05_agency.tex:350) allows the redraw "once or every round".
   - **The quenched law of D1 is exact and well defined.** All four niche configurations are diffusive, so the record's reason R3 for discarding the quenched variant (non-diffusive draws) does not carry over to D1.
   - **The full model is one of the null's draws.** The mutual configuration is the full model itself, so P(S ≥ S_0) = 1/9 exactly.
   - **Test outcome.** With n_null = 999, E[p] = 0.112 and Pr(p ≤ 0.01) = 1.7e-38. D1 passes N_pr only because the every-round variant is declared. The candidate's own label for this reading (R-pr: "Depends: yes", "not computed") understated it: the dependence decides the N_pr clause.

**Weakest point of D1: the agency clause.** At 0.8 it rests on padding, as the candidate itself says (R-pad), and it is 0 under the literal η_C with any calibrated group belief (new).

## 1. Readings I adopt, and whether my findings depend on them

| Reading | Depends? |
|---|---|
| Record conventions (own sensing noise private even when relayed; second-moment Σ^c; prior-error coordinate; closure convention of round2 run3) | No. Inherited from the record, not attacked. |
| Literal η_C (05_agency.tex:11) with channel roles from def:col-partition | Yes, for finding 1. |
| Calibrated q_C on non-member channels (V_o ≥ R) | Yes, for "index exactly 0". The full V_o curve is given in §3. |
| The quenched variant of N_pr binds (rather than being an optional alternative) | Yes, for finding 2. |
| Memory clause read as d_M, the definition's quantity (05_agency.tex:20-21), rather than the d_cl certificate | Yes, for the flooding-lever correction (§5). No, for D1 itself, which passes either way. |
| Worst-path reading over explored paths only; the supremum over all paths is not proved | Yes, for the memory statements. |

## 2. Independent recomputation: what survived (computed)

My methods differed from the candidate's in four ways:
- Gains: sequential scalar covariance-form updates (Joseph form) instead of the information form.
- Stationary covariances: fixed-point iteration of the augmented second-moment map instead of scipy's Lyapunov solver.
- Mechanism medium: exact average over all 81 attention configurations per round instead of a hand-reduced 2×2 recursion.
- Markov defect: a zero-noise Kalman filter on y instead of Toeplitz conditioning.

| Quantity | Candidate | Mine |
|---|---|---|
| g_max / ψ | 0.00702 / 0.06702 | 0.007016 / 0.06701573 |
| EFE gaps (attention / slot) | 0.04837 / 0.06094 | 0.04837 / 0.06094 |
| P(not mate) / P(any slot open) | 1.18e-8 / 2.07e-10 | 1.185e-8 / 2.070e-10 |
| α, β, r(A) (exact) | 0.0134391, 0.0224783, 4.345220 | same; diffusive; cross-niche block 0 |
| Spanning regions (size 2, 3, 4) | 0.374, 0.642, 1.000 | same |
| Mechanism medium | 2.493156 | 2.493156 |
| Mean-coupling baseline | 3.2301 | 3.230147 |
| N_hab | 1.3461 ± 0.0066 | 1.3503 ± 0.0051; fresh seed 1.3494 ± 0.0031 |
| N_pr (every round) | 1.7612 ± 0.0074 | 1.7403 ± 0.0061 (2.2 SE low); fresh seed 1.7596 ± 0.0043 |
| N_lp (dead relays) | r = 1 | exact r = 1; MC 1.0049 ± 0.0068 |
| Stationary d_cl / d_M | 8.906e-4 / 4.368e-5 | 8.9057e-4 / 4.3684e-5 |
| Worst single-round d_cl | 9.1242e-3 | 9.1242e-3 |
| Inference: U, E(y−u)² | 0.137207, 5.123596e-3 | same |
| Inference: best-constant / claimed / reverse | 0.01867 / 0.02043 / 0.01885 | same |
| Agency: KL_a, KL_s\|a, index (G2) | 2.772588, 11.090355, 0.800000 | same; γ_C* = 400 |

Controls, each behaving as required:
- R_c = 1e6 gives r = 1.000002.
- Independent worlds per replica give r = 21.15.
- Full-model MC gives 4.3714 ± 0.0146 and, with a fresh seed, 4.3370 ± 0.0068, against the exact 4.3452.
- The R² average gives d_cl = 0.
- Encoding one member's mean gives an inference defect of 0.04316 > 0.01867.
- γ_C = 0 gives misfit = KL(P‖E) = 13.862943.

N_ex variant with computation noise removed (q_c = 0): r(A) = 4.4068 ≥ 3.7, so D1 survives under that reading too (computed).

## 3. Attack A: literal external states (computed; reading interpretive)

D1's index under the literal η_C as a function of V_o:

| V_o | 1e-6 | 1e-4 | 1e-3 | 3e-3 | 1e-2 | 3e-2 | 0.1 | 0.2 | ≥ 0.5 (incl. 1, 1.263) |
|---|---|---|---|---|---|---|---|---|---|
| G2 | 0.7999 | 0.7949 | 0.7599 | 0.6937 | 0.5129 | 0.2281 | 0.0149 | 0 | 0 |
| G1 (v_C free) | 0.7999 | 0.7953 | 0.7632 | 0.7023 | 0.5339 | 0.2579 | 0.0240 | 0.0002 | 0 |

- **Derivative criterion.** At γ_C = 0 the misfit's slope is E_E[I] − ψE_E[K]. With V_o = 1, E_E[I_att] = 1.0895, against ψE_E[K] = 8ψ = 0.536 (E_E[K] = 8 open slots over both members under habits), so the slope is positive. The misfit is convex in γ_C, so its minimum is at γ_C = 0.
- **The padding lever still works under the literal reading, but only at very large m.** I scaled R_s = 10m/8 so that the memory and N_hab profiles stay at D1's values. At V_o = 1 the index is 0 at m ≤ 18, then 0.003 (m = 24), 0.125 (m = 64), 0.381 (m = 128), 0.606 (m = 256) and 0.861 (m = 1024). An Agency0 of 0.75 needs m of order 500 slots per member.
- **Repair (index only; the other clauses not re-verified).** Put a pragmatic cost c_o ≥ 2 nats on reading a non-member's relay, shared by members and the group model.
  - D1' (support {∅, mate, o1, o2}) gives an index of 0.9000; the part left unexplained is mate versus ∅.
  - D1'' (support {mate, o1, o2}) gives 1.0000.
  - At c_o = 1 the index falls to 0.044 and 0.031.
  - This is padding again, now through costly outsider channels. Classification of channels moves the index in both directions, so "the conservative choice" is not a fixed direction.
- **Also open: def:agy-group-model's shared-likelihood assumption fails.** That definition assumes slot likelihoods "that every belief shares" (:157), but D1's members do not model u_o at all. If they did, their own EFE would value outsider relays (about 1.3 nats, against 0.048 for the mate) and the collective would dissolve. Under the literal η_C, D1 therefore sits outside the setting of def:agy-group-model unless the class is completed by declaration.

## 4. Attack B: N_pr drawn once (computed exactly)

| Niche-A configuration | Σ_A | Diffusive | r(A) |
|---|---|---|---|
| Neither member reads the other | diagonal | yes | 1.000000 |
| One-directional (either way) | [[0.035917, 0.015506], [0.015506, 0.040406]] | yes | 2.368840 |
| Mutual (equals the full model) | [[0.035917, 0.022478], [0.022478, 0.035917]] | yes | 4.345220 = S_0 |

- With S = r(A): P(S ≥ S_0) = 1/9, E[p] = 0.1120, Pr(p ≤ 0.01) = 1.67e-38.
- With S = the maximum over regions: P = 17/81 and E[p] = 0.2107.
- The result is structural: for n = 2, κ_msg = 1 and N = 4, the null reproduces the full model with probability 1/9 at every parameter point.

## 5. Attack C: frontier claims

- **The π* grid does not fit Theorem A's own definition (refuted).** Theorem A defines ρ with "slots follow the design's habits", but pistar.py computes ρ with m = 0 ("slot-neutral").
  - D1's own ρ at π = 0.577, 0.7, 0.8, 0.9, 0.95 and 1 is 1.880, 2.132, 2.330, 2.533, 2.650 and 2.762, so **π*_D1 = 0.880**, not 0.577. For comparison, my slot-free ρ(0.577) is 2.472.
  - With π*_D1, Theorem A's cap at m = 8 is 0.9775, not 0.9098.
  - The quoted caps, including "m ≥ 1, 4, 8 for Agency0 = 0.5, 0.8, 0.9", are therefore not caps for designs that have slots. They understate what is attainable.
- **"D1-type designs attain the cap to within 1e-8" is refuted.** D1's KL_a = 2.773, against Theorem A's floor 2d(1‖0.88) = 0.255. What is attained to 1e-16 is C12's identity (slot misfit about 0), not Theorem A's cap.
- **The flooding lever is not blocked by memory under d_M (computed, explored paths).** The candidate reports a conflict with the worst-path memory reading, but that conflict comes from using the d_cl upper bound. Worst values, over every pattern pair held for 1, 4 or 30 rounds:

  | R_s | 1 | 2 | 3 | 5 | 10 |
  |---|---|---|---|---|---|
  | Worst d_cl | 0.2017 | 0.1009 | 0.0596 | 0.0275 | 0.0091 |
  | Worst exact I(y_{t+1}; y_{0:t−1} \| y_t, path) | 4.78e-3 | 2.51e-3 | 1.19e-3 | 4.6e-4 | 4.6e-4 |

  **Design D5** is D1 with R_s = 1 and attention habits E(mate) = 1 − 3ε. Its N_hab with attention pinned on the mate is 1.2466 ± 0.0041 (below b = 2.493). Its index under R-outsider is 0.994537 at ε = 0.01, 0.999946 at ε = 1e-4 and 1.000000 at ε = 1e-8. I computed only N_hab, memory and the index; the other clauses carry over from D1 by construction (slots stay closed) and were not recomputed. This sharpens R-pad: the index can be pushed toward 1 with every other clause unchanged.
- **Padding lever at fixed R_s = 10.** The d_cl certificate fails at m = 18 (0.0222) and m = 50 (0.0835). The exact defect is ≤ 1.3e-3, so the clause itself holds. With R_s ∝ m the profile is identical to D1's.
- **Theorem A step 3 has a proof gap; no violation found.** The step assumes one habit mass E(X*) shared by all members, which ρ requires. I tested asymmetric habits at equal product 0.774 = π*_D1²: symmetric 2.520 ± 0.010, (0.999, 0.775) 2.540 ± 0.010, (0.95, 0.815) 2.527 ± 0.010. Asymmetry raised contrast at fixed product, so I found no counterexample (numerical). The gap is still unproved for general product habits.

## 6. Attacks that failed

- **Memory under the worst-path reading holds (computed).** Sustained deviations included one member opening all slots, with or without the relay, paired with a mate that reads nothing, for L ≤ 80 rounds; alternating patterns; and out-of-phase patterns. The exact Markov defect stays ≤ 4.6e-4 and d_cl ≤ 9.12e-3, so the clause has more margin than the candidate's certificate shows.
- **N_eff and N_inf are inapplicable.** Private slots are world channels in the attention set (02_framework.tex:13), and there is no performative component.
- **O2(f) does not matter.** Each member's EFE depends only on its own policy (Lemma 1(a) checked).
- **Lemma 1(d) is correct.** Under uniform leaks, regions that span niches have r ≤ 1.
- **Numerics.** No numerical error found anywhere.

## 7. Files

All my files are in `C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round3\attack-agency-frontier\`. Runs were single-threaded and sequential, each under 30 s. No repository or vault file was edited.

- **Library:** mylib.py.
- **Deciding numbers and controls:** a1_deciding.py → a1_out.txt.
- **N_hab, N_pr and Theorem A asymmetry:** a2_nulls.py → a2_out.txt.
- **Closure, inference and sustained paths:** a3_closure.py → a3_out.txt, and a3b_paths.py → a3b_out.txt.
- **Agency under the literal η_C:** a4_agency.py → a4_out.txt.
- **Quenched N_pr and π*_D1:** a5_quenched_pistar.py → a5_out.txt.
- **Cost repair, N_ex at q_c = 0 and fresh seeds:** a6_repair_misc.py → a6_out.txt.
- **Padding under the literal reading:** a7_literal_frontier.py → a7_out.txt.
- **Asymmetric habits:** a8_thmA_asym.py → a8_out.txt.
- **Flooding memory:** a9_flood_memory.py → a9_out.txt.
- **Design D5:** a10_flood_design.py → a10_out.txt.

## round3: audience-route

VERDICT: Computed existence, and the verdict does not depend on the three readings the user flagged. In instance P0, a non-member source S broadcasts its raw sensor reading. Four audience members each choose, by expected free energy, one channel among S, their three mates and nothing. The setting has one world component in the time-invariant framework, literal one-round latency and γ=40. The audience A is a meta-agent of grade (r0, α_M, α_I, α_pr, Agency0) = (4.5, 0.03, 0.03, 0.01, 0.99) with n_null=999, and this grade holds at all 17 points of a ±5% box over seven parameters (numerical). Three features remove the flagged dependence. P0 has no performative acts, so N_eff and N_inf are inapplicable under either typing (O2(a)). The only chosen policy component is attention, whose exterior part is the slot, and the full-policy agency index is 1−O(1e−13) (O2(e)). Members decide independently, with no deliberation chain, so the real-time and frozen-state readings coincide (O2(f)). The source does not join the selected block: r(A∪{S})=2.326 against r(A)=5.3849, with source coupling 5.6 against internal coupling 58.0 (computed exactly, with a proved closed form). The admissible window (3.930, 5.385] is nonempty under the mean-coupling baseline (3.817) and under four declared mechanism media, the largest of which is 3.930. The cost is that the audience's coherence is borrowed from a common outsider. Ω_int(A|ζ_S) is zero except through attention events of probability 2.1e−14 per member-round. The relay variant P1 (message capacity two) has Ω_int(A|ζ_S)>0, with conditional error correlation 0.011. P1 passes at (4.45, 0.03, 0.03, 0.01, 0.99), with full-policy index 0.9967, on its ±5% box (17/17). Both instances still rest on three conventions shared with C11: a relayed own sensing noise is a private input, partner randomization is redrawn every round, and continuity of the null laws is shown only numerically. Under the literal η_C, adding a second niche with cross-niche exterior options drives the full-policy index to 0 (proved lemma plus computation). Single-exterior-option designs are therefore required.
POSITIVE: True

The audience route gives a computed meta-agent whose verdict does not depend on readings (a), (e) or (f). Readings (e) and (f) are decided in the agency section below. For instance P0, every type-D null computed (N_hab, N_pr) falls below the window, the deletion and freezing nulls are diagonal (proved), and the other two type-D nulls, N_eff and N_inf, are inapplicable, so (a) never bites. Agency is 1−O(1e−13) under the full-policy reading. The admissible window is nonempty under every baseline variant computed. The construction depends on three readings it shares with C11: the source's sensing noise is a private input when relayed, partner randomization is redrawn every round, and continuity of the null laws is shown only numerically. It also exposes a new reading question (g): whether a meta-agent's members must interact with one another. P0's members do not interact, up to events of probability 2e−14 per member-round. The variant P1 interacts and passes with agency 0.9967.

## 1. Specification (declared before the deciding runs)

**Status.** Setting: finite population, equilibrium (stationary) statistics, discrete rounds, time-invariant framework of `def:fw-system` (02_framework.tex:11-17).

**World.** One scalar AR(1) component, η_{t+1}=Fη_t+w_t, with w~N(0,Q), stationary and never renewed.

**Population V={S}∪A.** A={1..4} is the audience. The source S is not a member.

**Model state.** Every agent filters x_t=(η_t,η_{t-1}) exactly. Computation noise qc·I_2 is added to the predicted means and included in P^-, the I* convention.

**Sensors.** S has an own sensor with noise R_S. Each audience member has an own sensor with noise R. Own sensors are structural: they are read every round.

**Broadcasts.** Every agent writes its raw reading u_a(t)=s_a(t) every round. This is a fixed speech act, not a choice.

**Channels.** A message arrives as y_ij(t+1)=u_j(t)+ν_ij with ν~N(0,R_c), receiver-specific. Latency is literally one round. The channel informs η_t with claimed noise R_j+R_c, which is exact.

**Attention.**
- S reads nothing except its own sensor (message capacity zero).
- In P0, member i chooses one set J from {∅, {S}, {m1}, {m2}, {m3}} (κ_msg=1) from its policy posterior ∝ E(J)·exp(−γG_i(J)), with uniform habits.
- The members' expected free energy is G_i=−I(x_{t+1}; own sensor, channels in J), with no pragmatic term.
- There is one precision, γ=40.

**Contrast coordinates.** Prior errors e_a(t)=m^-_{a,0}(t)−η_t for every agent, S included (`def:fw-level0`, 02_framework.tex:315).

**P0 parameters.** F=0.9, Q=0.05, R=1, R_S=0.01, R_c=0.002, qc=1e-4, n=4, κ_msg=1, γ=40, ψ=0.

**P1 parameters.** As P0, but κ_msg=2: the sets are all subsets of size at most 2 of {S, m1, m2, m3}, eleven policies.

**Conventions and readings adopted** (each is marked "verdict depends: yes/no" in section 7):
- R0: the world-conditional law (`def:col-world-conditional`, 04_collectives.tex:130-132) conditions on the world path and on channel noise shared by receivers. It does not condition on an agent's own sensing noise, even when that noise is broadcast. This is the record's convention and is shared with C11.
- Second-moment convention for random attention (`def:col-contrast`, 04_collectives.tex:187).
- N_pr is redrawn every round. Each receiver gets κ_msg uniform partners among the n other agents. S keeps attention rate zero.
- The coarse variable is the scalar collective average y=(1/n)Σ_{i∈A} m^-_{i,0}, which 05_agency.tex:21 permits.
- η_C follows 05_agency.tex:11 literally: η_C=(η_{t+1}, u_S(t)). Slot outcomes are o_i=u_S(t)+ν_i, conditionally independent given η_C.
- The selector is contrast at level r0. "Each constant of the selector" is read as each r0 in the admissible window.

## 2. Answers to the assignment's questions

### 2.1 Does the source join the selected block?

No, in the regime where any window exists.

**P0 world-conditional covariance (computed).** Exact Lyapunov solution:

| Entry | Value |
|---|---|
| Var e_S, σ | 6.07184e-3 |
| Cov(S,i), c | 6.5888e-4 |
| Var e_i | 7.5547e-3 |
| Cov(i,j), β | 4.03044e-3 |
| α = Var e_i − β | 3.52426e-3 |

**P0 precision.**
- Π^c is diffusive: largest off-diagonal entry 0, smallest row sum 46.0.
- Couplings: audience pair 58.024, source to audience 5.605.
- Leaks: audience 46.048, source 144.707.
- cut(A)=22.42.

**P0 contrasts.**
- r(A)=5.384864.
- r(A∪{S})=2.325959. It is the best region containing S and the best region other than A.

The source forgets its own noise quickly (gain ≈0.85). Its error at time t is therefore dominated by v_S(t−1), which the audience has not received yet. This makes its coupling to the audience weak.

**Proved decomposition (Prop. A).** r(A)=1+nβ/α−c/σ−nc²/(σα) = 5.5745 − 0.1085 − 0.0811. The cut costs 0.19.

**Scan over R_S and R_c (check 13).**
- S joins (best region containing S exceeds r(A)) only at R_S ≥ 0.2 ≈ 4Q. There the mean-coupling baseline (≥5.2) exceeds every region, so no collective exists at all.
- The mean-coupling window exists for R_S up to about Q (for example R_S=0.05, R_c=0.002: r(A)=8.01 against 7.66) and closes by R_S=0.1.
- My declared expectation "never joins" was wrong at R_S ≥ 0.2.

### 2.2 Contrast against both baselines

All baselines use clause (c), 04_collectives.tex:202.

| Baseline | P0 | P1 | Status |
|---|---|---|---|
| Mean coupling (whole comparison medium, all 26 regions enumerated) | 3.8167 | 3.8128 | computed exact (P1: from Monte Carlo Σ^c) |
| Mechanism M-F: N=5 agents of the audience type, EFE attention | 2.400±0.008 | 4.112 | numerical |
| Mechanism M-S: all agents of the source type | 1.019 | – | numerical |
| Mechanism M-perm: full Σ^c averaged over relabelings | 3.9301 | 3.919 | computed |
| Mechanism M-sym: agents kept, attention in its uniform state (= N_pr) | 1.541 | 1.766 | numerical |

- Leak heterogeneity on A is 1, by exchangeability.
- Significance against mean coupling: 1.41.
- Admissible windows: P0 (3.930, 5.385]; P1 (4.112, 5.372].
- My declared expectations for M-F (<1.6) and M-perm (<3.817) were both missed (2.400 and 3.930). The windows survive.

### 2.3 Type-D nulls (`def:agy-nulls`, `tab:agy-nulls`, 05_agency.tex:332-360)

P0 values below are exact pair algebra over 200 Monte Carlo policy-path pairs, with standard errors from 20 batches.

**N_hab (γ=0).**
- P0: r(A)=1.456±0.004; every region is at most 1.456 (numerical).
- P1: 1.550.
- This is 2.47 below the lower edge.

**N_pr (redrawn every round).**
- P0: r(A)=1.541±0.004 (numerical).
- Test of `prop:agy-tests`(b) (05_agency.tex:367) with 999 independent draws of 80 world paths each:
  - all 998 defined draws are at most 1.635;
  - one draw was non-diffusive and is scored conservatively as ≥S_0;
  - p=0.002 ≤ α_pr=0.01.
- First run, at 20 world paths per draw: 72 undefined draws, max 1.732. That run is superseded.
- Negative control: 199 full-model draws give p=0.515.
- P1: 999 draws, all defined, max 1.877, p=0.001; negative control p=0.500.

**Quenched N_pr (supplementary, check 11; all 4^4 draws enumerated exactly).**
- Only 54 of 256 draws are diffusive, as Corollary F-share predicts.
- Only the all-source draw (probability 1/256) selects A.
- The quenched reading inherits R3's undefined-contrast issue.

**N_lp and N_rn (proved, Prop. C(iii)).** Σ^c is diagonal and r≤1 (computed check: r(A)=1.000000).

**N_fr (proved).** Σ^c is diagonal: frozen channels carry initial content in X_sh.

**N_eff and N_inf: inapplicable (proved, Prop. C(i)).** No agent has a performative component, writes a record or acts. Attention is the first active component in 02_framework.tex:13. This holds under both the strict and the conditional typing.

### 2.4 Survival null N_ex

Inapplicable (proved, Prop. C(ii)). Every channel carries a fresh raw datum, read once per receiver with its true noise, so literal fusion is exact fusion.

### 2.5 Closure (`def:agy-closure`, 05_agency.tex:13-24)

**Memory, P0.**
- The internal dynamics is block-diagonal, with M=A_F P^+(P^-)^{-1} of rank one and Q^𝔫=qc·I_{2n}≻0.
- Markov defect d_M=0.0257, exact and independent of qc.
- Per-step bound d_cl=0.251.

**Inference, P0.** Expected KL of N(y,v) against the union-model predictive of η_t:
- best constant encoding: 0.02509 (exact); sampled check 0.02514;
- claimed variance: 0.0266;
- reverse direction: 0.0245.

**P1.** d_M=0.0256; inference 0.0249.

**Expectation miss.** I declared d_M ≤ 1e-3 and d_cl ≤ 1e-2. The lagged channel creates the memory (Prop. E).

### 2.6 Agency index, full-policy reading (`def:agy-agency-index`, 05_agency.tex:240-246)

**Setup.**
- Members' joint policy: the whole attention choice, 5^4 profiles in P0 and 11^4 in P1.
- Decision state X*: the stationary covariance state, weight 1.
- The actual law is a product, because members decide independently.

**Class G2.**
- Habits fixed at uniform.
- G_C=−½ln(1+kV_u/R_c), where k is the number of members reading S and V_u=P^-_{11}+R_S.
- Reading a mate opens no slot.
- γ_C ∈ [0,∞).

**Class G1.** As G2 with V_u free.

**Reading W (not the definition).** η_C = world only.

**P0 results (computed exactly).**

| Member precision γ | KL(P‖E) | G2 index | G1 index | W index |
|---|---|---|---|---|
| 40 | 6.4378 (= 4 ln 5) | 1−O(1e−13) | 1−O(1e−13) | 1−O(1e−13) |
| 10 | – | 0.999994 | – | – |
| 4 | – | 0.9857 | 0.99988 | 0.9345 |
| 2 | – | 0.761 | 0.9997 | – |

Negative controls:
- a law in which every member reads one mate: index 0;
- an all-or-none law: 0.31, against 0.88 for the product law with the same marginals.

**P1 results.**
- Member law: {S}: 0.2154; each {S, m_j}: 0.2615.
- KL(P‖E)=4.0596; inf KL=0.0132 at γ_C=229; index 0.99675 at both decision states.
- Under the slot-only reading the index is ≈1.

### 2.7 Ω_int(A|ζ_{V\A})

**P0.**
- Ω_int(A)>0: the common drive from S enters through v_S ∈ ζ_S, which X_sh does not contain.
- Ω_int(A|ζ_S) is zero except through attention events in which a member reads a mate. These have probability 2.1e−14 per member-round.
- It is exactly 0 in the deterministic-attention limit (Prop. B).
- Computed check: with S's private inputs conditioned on, the members' error covariance has off-diagonal exactly 0.

**P1.** Ω_int(A|ζ_S)>0 (computed). E[Cov(e_i,e_j|X_sh,ζ_S,routing)]=3.8e−5, against variance 3.55e−3 (correlation 0.011). Positivity follows because the routing-mean term vanishes for independent routings.

## 3. Per-clause table (P0 center; P1 center in brackets)

| Clause (file:line) | Value | Grade or criterion | Margin | Status |
|---|---|---|---|---|
| Moment bound (M), stationarity | stable exact filters | – | – | proved |
| Diffusive Π^c (04_collectives.tex:147-151) | min row sum 46.0 [46.4]; off-diagonal ≤0 | – | – | computed [numerical] |
| r(C)≥r0 (04_collectives.tex:214-221) | 5.3849 [5.3724±0.0001] | r0=4.5 [4.45] | 0.885 [0.92] | computed [numerical] |
| r0 > max baseline | max 3.930 [4.112] | – | 0.57 [0.34] | computed and numerical |
| r0 > leak ratio | 1 | – | 3.5 | proved |
| Other regions | ≤2.326 [2.317] | <r0 | 2.17 | computed |
| Memory d_M ≤ α_M | 0.0257 [0.0256] | 0.03 | 0.004 | computed |
| Inference ≤ α_I (best constant) | 0.0251 [0.0249] | 0.03 | 0.005 | computed, cross-checked by sampling |
| N_hab | 1.456 [1.550] | below lower edge | ≥2.4 | numerical |
| N_pr (every round), test | p=0.002 [0.001], n_null=999 | α_pr=0.01 | – | numerical |
| N_lp, N_rn, N_fr | diagonal, r≤1 | – | – | proved |
| N_eff, N_inf | inapplicable | – | – | proved |
| N_ex (type S) | inapplicable | – | – | proved |
| Agency, full policy (G2) | 1−O(1e−13) [0.99675] | Agency0=0.99 | 0.01 [0.007] | computed |
| Ω_int(A|ζ_S), reported | ≈0, events at 2e−14 [>0] | reported, not required | – | proved [computed] |
| N_w, N_code (type E) | N_code predicts nothing (identity codes). N_w predicts nothing from access by world component; if sensor type counts as access it predicts {A,{S}} and restricts the claim | – | – | interpretive |
| N_fg (diagnostic, F=1) | r(A)=5.94 | – | – | computed |

**±5% box over (F, Q, R, R_S, R_c, qc, γ).** The design is center plus a 2^(7−3) fractional factorial.
- P0 passes the full grade (4.5, 0.03, 0.03, 0.01, 0.99) at 17/17 points.
  - r(A) ranges over 4.574–6.310.
  - The largest lower edge is 4.431.
  - N_hab ≤ 1.487 and N_pr ≤ 1.579.
  - d_M ≤ 0.0276.
  - The best-constant KL is at most 0.0291, a margin of only 0.0009 at the box edge.
  - Agency is 1−O(1e−13) everywhere.
- P1 at r0=4.5 passes 16/17. Point 5 has r(A)=4.542±0.017, which fails my 3-SE rule. At r0=4.45 it passes 17/17.
- P1's inference is at most 0.0288; with the claimed-variance encoding it reaches 0.0308, so α_I=0.035 is needed there.
- Negative control: R_c×100 fails the collective clause (r(A)=1.075).

## 4. Grade frontier by reading combination

The frontier is the largest Agency0 at which every clause holds.

| (a) N_eff/N_inf typing | (e) policies | (f) deliberation | P0 | P1 | C11 (record) |
|---|---|---|---|---|---|
| strict | full | real-time | 1−O(1e−13) | 0.9967 | fails |
| strict | full | frozen | 1−O(1e−13) | 0.9967 | fails |
| strict | slot | either | 1−O(1e−13) | ≈1 | fails (acts) |
| conditional | full | either | 1−O(1e−13) | 0.9967 | 0.008 (C12) |
| conditional | slot | frozen | 1−O(1e−13) | ≈1 | 0.99 |
| conditional | slot | real-time | 1−O(1e−13) | ≈1 | 0.9 (coarse decision state) |

The other grade components at the center:
- P0: r0 ∈ (3.930, 5.385], α_M ≥ 0.0257, α_I ≥ 0.0251, p ≤ 0.002.
- P1: r0 ∈ (4.112, 5.372], α_M ≥ 0.0256, α_I ≥ 0.0249, p = 0.001.

These hold under every baseline variant. If reading (g) demands Ω_int(C|ζ_{V\C})>0 beyond technical positivity, only P1 qualifies.

## 5. Proofs

### Prop. A (source plus exchangeable audience), proved

**Statement.** Let Σ=[[σ, c1ᵀ],[c1, αI_n+β11ᵀ]] with σ, α>0, and set β′=β−c²/σ. Then:
1. Σ≻0 if and only if α+nβ′>0.
2. The precision blocks are
   - Π_AA=α⁻¹(I−β′/(α+nβ′)·11ᵀ);
   - Π_SA=−c/(σ(α+nβ′))·1ᵀ;
   - Π_SS=1/σ+nc²/(σ²(α+nβ′)).
3. Π is diffusive if and only if β′≥0, 0≤c≤σ and ε_S=Π_SS−nc/(σ(α+nβ′))≥0. The audience leak is ε_A=(1−c/σ)/(α+nβ′).
4. r(A)=1−c/σ+nβ′/α.
5. r(A∪{S})=min(1/α, R_f)/((ε_S+nε_A)/(n+1)), where R_f=(nΠ_SS+2n·a_SA+1/(α+nβ′))/(n+1).
6. The mean-coupling baseline is 1+(n+1)ā/ε̄.

**Proof.**
- Schur complement and Sherman–Morrison give part 2.
- ξ_out(A)=φᵀΠ_AAφ=1/(α+nβ′).
- On 1_A^⊥, diag(ε)+L_A=(ε_A+n·a_AA)I.
- Π restricted to 1^⊥ splits into audience differences (eigenvalue 1/α) and f=(n,−1_A), because fᵀΠg=0 for audience differences g.

**Check.** 300 random structures agree with direct inversion to 3.4e−15 (check 13b). The negative control β′<0 is non-diffusive in both computations.

### Prop. B (member-restricted order parameter of a pure audience), proved

**Statement.** Suppose no member reads, with positive probability, a channel written by another member, whether directly, through a record or act, or through a relay by non-members. Then every μ_i is a measurable function of (X_sh, ζ_{V\A}, ζ_i), and Ω_int(A|ζ_{V\A})=0.

**Proof.** This is the independence argument of s05_agency.tex:291, with prop:agy-nulls-vanish(a), applied to independent inputs.

**Application.** In P0 the hypothesis fails only on events of probability 2.1e−14 per member-round.

### Prop. C (inapplicable and diagonal nulls), proved

1. The active states of every agent are attention and a fixed broadcast. There is no a^e and no record write (02_framework.tex:13). N_eff and N_inf therefore leave the model unchanged and are inapplicable (05_agency.tex:333).
2. Each channel delivers η_t+v_j(t)+ν with v_j(t) unseen by the receiver, read once with claimed noise R_j+R_c. The literal likelihood is therefore the exact conditional law of the message, and N_ex leaves the model unchanged.
3. Under N_lp, N_rn and N_fr, the only noises reaching a receiver beyond its own are receiver-specific. Members' errors given X_sh are then independent, so Σ^c is diagonal and r≤1 (prop:agy-nulls-vanish(a),(d)).

### Lemma D (index of a deterministic joint policy), proved

**Setting.** P=δ_{π*}. Habits are fixed at E, the belief is fixed, and γ_C≥0. Let f(γ_C)=ln P_g(π*). Then f′=E_{P_g}[G_C]−G_C(π*) and f″=−Var_{P_g}(G_C)≤0.

**Statement.**
- (a) If π* is the unique minimizer of G_C, then f increases to 0 and the index tends to 1.
- (b) If G_C(π*) ≥ E_E[G_C], then by concavity the maximum of f is at γ_C=0, inf KL = KL(P‖E), and the index is 0.

**Application.**
- P0 is case (a). Its law is 1−2e−14 close to δ, and the computed index is 1−O(1e−13).
- The two-niche audience under the literal η_C is case (b), with computed index 0.0000. The group EFE's minimizer has all four members reading B's members, G_C=−12.79, against −2.44 for all reading S_A (check 12).

### Prop. E (memory structure), proved structure; values computed

**Structure.** M=v·wᵀ with v=(F,1)ᵀ and wᵀ=(1−aP⁺₀₀, −bP⁺₀₁). With isotropic internal noise, y_{t+1}=F·s_t+𝔫_{t,0} and s_{t+1}=λs_t+wᵀ𝔫_t, where λ=wᵀv. This is ARMA(1,1). The Markov defect of the average equals that of one member's coordinate.

**When y is Markov.** If w₁=0 (no lagged channel), then s=w₀y and y is AR(1), so Markov. The converse direction was not proved.

**Value.** d_M=0.0257 (computed). Negative control: an eigen-coordinate gives 0 to 2e−16, and a mixed coordinate gives 5.4e−3.

## 6. Class results and obstructions

1. **Literal η_C obstruction for multi-niche audiences (proved through Lemma D(b), computed).**
   - When members can open exterior slots whose contents their own models ignore, the literal η_C (05_agency.tex:11) makes G_C value information about those contents, sender noise included.
   - The group posterior then prefers the noisiest irrelevant channels, and the full-policy index is 0.
   - Designs must make the relevant source the only exterior option; P0 and P1 do this.
   - The same mechanism bears on I*. Its members can attend niche B's relay channels, which are exterior to A. Treated as slots under the full-policy reading, each is worth about ½ln(1+(V0+R)/R_c) ≈ 1.3 nats to G_C. The attack's 0.008 treated them as internal. This is interpretive and not recomputed; by Lemma D(b) the index would fall to about 0.
2. **Band of source precision (computed, check 13).** A window exists only for R_S below roughly Q. For R_S ≳ 4Q the source joins the block, but no region beats the mean-coupling baseline.
3. **C12 does not apply to P0 or P1.** The policy sets are not products of (internal attention) × (slot), because capacity couples them. In P1 the internal component costs 0.013 of 4.06 nats.

## 7. Readings the verdict depends on

| Reading | Depends? |
|---|---|
| (a) typing of N_eff and N_inf | No. Inapplicable in both instances. |
| (e) full versus slot policies | No (P0); P1 gives 0.9967 against ≈1. |
| (f) real-time versus frozen deliberation | No. There is no deliberation chain. |
| Baseline: mean coupling versus mechanism (five media) | No. The window is nonempty under all. The manuscript does not define the mechanism medium for heterogeneous populations, so this question goes to the author. |
| R0: relayed own sensing noise is a private input | Yes. If v_S is conditioned on, Σ^c is diagonal and r=1. Shared with C11. |
| N_pr redrawn every round versus quenched | Yes. Quenched: 202/256 draws are non-diffusive. Shared with C11 (R3). |
| (g) whether Ω_int(C|ζ_{V\C})>0 is required | P0 fails it (it is positive only through events of probability 2e−14); P1 passes. The literal definition only reports it (05_agency.tex:380). |
| Literal η_C | No for P0 and P1 (reading W also gives ≈1). Yes for multi-niche designs (index 0). |
| Coarse variable | No. The scalar average is permitted (05_agency.tex:21). |

## 8. Scripts and deciding outputs

All scripts are in C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round3\audience\. Every run was single-threaded, sequential and under 70 s. Every script states its expectation before running and includes a negative control. No repository or vault file was edited.

**Libraries.**
- aud.py: exact pair algebra, Lyapunov solutions, contrast.
- sim.py: independent sampled-noise Monte Carlo of the same model.

**Validation (check0_out.txt).**
- The two implementations agree within 2.2 SE.
- Negative control, independent worlds: +372 SE.
- Negative control, dead channels: covariance 0.

**Deciding checks.**

| Check | Script | Output | Deciding content |
|---|---|---|---|
| 1 | check1_main.py | check1_out.txt | full model, N_hab, N_pr, N_lp |
| 2 | check2_mechanism.py | check2_out.txt | mechanism media |
| 3 | check3_agency.py | check3_out.txt | agency, P0 |
| 4 | check4_closure.py | check4_out.txt | closure, P0 |
| 5b | check5b_npr_test.py | check5b_out.txt | N_pr test, P0 |
| 6 | check6_box.py | check6_hw05_c0.txt to c3.txt | P0 box |
| 7 | check7_relay.py | check7_out.txt | P1 main quantities |
| 8 | check8_inference_mc.py | check8_out.txt | inference, sampled |
| 9 | check9_relay_test_box.py | check9_test_out.txt, check9_box_c0.txt to c2.txt | P1 test and box |
| 10 | check10_relay_inference_box.py | check10_out.txt | P1 inference on the box |
| 11 | check11_quenched_fg.py | check11_out.txt | quenched N_pr |
| 11b | check11b_fg.py | check11b_out.txt | N_fg |
| 12 | check12_twoniche_obstruction.py | check12_out.txt | two-niche obstruction |
| 13 | check13_scan.py | check13_out.txt | R_S and R_c scan |
| 13b | check13b_closed_form.py | check13b_out.txt | closed forms |

explore1.py and explore1_out.txt are design exploration only.

**Expectations missed (reported as such).**
- M-F and M-perm were above my declared bounds.
- d_M and d_cl were far above my declared bounds.
- check5 had 72 undefined draws, so I reran it as 5b.
- P1's r(A)=5.372 fell just below my declared band of 5.4–7.
- P1 box at r0=4.5: 16/17.
- check 13: the source joins at R_S ≥ 0.2.
- check11 part (b) crashed at F=1 and was rerun as 11b.

## 9. Weakest point, open obligation, next action

**Weakest point.** The construction's coherence is borrowed from a common outsider. P0's members do not interact. P1's interaction is weak (correlation 0.011) and is not what produces the contrast. Numerically, the thinnest margin is α_I at the edge of the box (0.0291 against 0.03); a stated α_I=0.035 removes it. The null laws are continuous only by numerical evidence (O6-type). A candidate proof route, uniform contraction of random Riccati maps, is unverified, and no source was read for it.

**Strongest supported result.** Form (A), computed with proved components. P0 and P1 are meta-agents at the stated grades inside the time-invariant framework. This holds under every combination of O2(a), (e) and (f), and under every baseline variant computed. It relies on R0 and the every-round N_pr.

**Minimal unresolved obligations.**
- Author rulings on (g), R0 and the every-round N_pr.
- A definition of the mechanism medium for heterogeneous populations.
- A proof of continuity of the null second moments.

**Next action.** An independent-code attack that rebuilds P0 from section 1 alone. It should recompute σ, c, α, β, N_hab, N_pr and the full-policy index. The author should rule on (g) at the same time.

## round3 attack: audience-route

# Attack on the audience route (P0, P1)

## Verdict

P0 survives the numerical attack. I rebuilt it from Section 1 of the candidate alone, with my own code, and every deciding number I recomputed agrees. The exact quantities agree to the digits reported.

It does not survive the claim that every clause holds at the stated grade under the stated declarations. The memory clause at α_M = 0.03 depends on something the specification never declares: the Gaussian initial law of the input-conditional Markov defect (def:agy-closure(i), 05_agency.tex:20).
- Noise-only stationary law (the candidate's implicit choice): d_M = 0.025717. Passes.
- Deterministic start, which is the framework's own start (rounds t ∈ ℕ with declared initial priors, 02_framework.tex:13, 26): d_M = 0.037477. Fails.
- Members' own stationary law used as the initial law: d_M = 0.070909. Fails.
- The literal formula applied to the stationary process, with the blanket path starting at round 0: d_M = 0.070515. Fails.

The three flagged readings, (a) the typing of N_eff and N_inf, (e) full versus slot policies and (f) real-time versus frozen deliberation, do not bite, as the candidate says.

The weakest point is this memory clause: its margin is 0.0043 even under the best case. Next:
- P0's coherence comes entirely from an outsider's sensing noise. If that noise v_S is conditioned on, r(A) = 1.000000 exactly.
- P1 does not repair reading (g) in substance. The links between members add no contrast.

## 1. Deciding numbers recomputed (P0)

Exact rows come from Lyapunov solves and Gaussian conditioning (computed). MC rows come from two-replica Monte Carlo on a shared world path (numerical, batch standard errors).

| Quantity | Candidate | Mine | Status |
|---|---|---|---|
| σ, c, Var e_i, β, α | 6.07184e-3, 6.5888e-4, 7.5547e-3, 4.03044e-3, 3.52426e-3 | 6.071841e-3, 6.588816e-4, 7.554695e-3, 4.030445e-3, 3.52425e-3 | computed, agrees |
| Π^c | diffusive; a_AA 58.024, a_SA 5.605, leaks 46.048 / 144.707 | largest off-diagonal −5.6051, smallest row sum 46.0477; same couplings and leaks; cut(A) 22.4203 | computed, agrees |
| r(A); best other region | 5.384864; 2.325959 (A∪{S}) | 5.384864; 2.325959 | computed, agrees |
| Mean-coupling baseline; M-perm | 3.8167; 3.9301 | 3.816704; 3.930115 | computed, agrees |
| Probability of reading a mate or nothing, per member-round | 2.1e-14 | 1.88e-14 (mate) + 2.25e-15 (nothing) | computed, agrees |
| Prop. A closed form | 5.384864 | 5.384864; re-derived by hand | proved and computed |
| N_hab (γ = 0) | 1.456 ± 0.004 | 1.4519 ± 0.0029; diffusive; A is the best region | numerical, agrees |
| N_pr, redrawn every round | 1.541 ± 0.004 | 1.5384 ± 0.0024 | numerical, agrees |
| N_pr, drawn once (quenched) | 54/256 diffusive; only the all-source draw selects A | 54/256; 1 | computed, agrees |
| d_M, noise-only stationary law; d_cl | 0.0257 (independent of qc); 0.251 | 0.025717 (same at qc = 1e-2); 0.251231 | computed, agrees |
| Inference, exact union model (best constant / claimed variance / reverse) | 0.02509 / 0.0266 / 0.0245 | 0.02509 / 0.02662 / 0.02448 | computed, agrees |
| Agency index, full policy, class G2 (γ = 40 / 10 / 4 / 2) | 1−O(1e−13) / 0.999994 / 0.9857 / 0.761 | 1−9e−16 / 0.999994 / 0.98566 / 0.76135 | computed (50-digit), agrees |
| Agency index, class W, γ = 4 | 0.9345 | 0.93452 | computed, agrees |
| ±5% box over 7 parameters | 17/17 points (fractional design) | full 2^7 design: 128/128 corners pass every exact clause. r(A) ∈ [4.5744, 6.3100]; lower edge ≤ 4.4312; other regions ≤ 2.4781; d_M ≤ 0.02764; KL ≤ 0.02908; S is chosen at every corner | computed |

Controls:
- Unit tests pass: C1 test value r = 3; diffusive test value; β = −0.1 is non-diffusive.
- Each negative control fails as it must:
  - Channel noise R_c × 100 gives r(A) = 1.0746 against a baseline of 1.1016.
  - Conditioning on v_S gives Σ^c diagonal and r = 1.000000.
  - Independent worlds in the two replicas give "r" = 39.3.
  - Dead channels give r = 0.9997.
  - In the agency index, a law in which every member reads a mate gives 0.
  - In the inference check, one member alone gives 0.0402, which fails α_I = 0.03.

The MC for the full model matches the exact covariance entries within 1.5 standard errors.

**Inference under other readings of the union model** (computed). All pass at 0.03.
- With computation noise in the union model: 0.02625 / 0.02770 / 0.02558.
- With the literal product of the members' likelihoods (which counts v_S four times): 0.02323 / 0.02618 / 0.02270.

**P1** (my general engine, numerical). All agree with the candidate within error.
- Member law: {S} 0.2154; each {S, m_j} 0.2614–0.2618.
- r(A) = 5.3752 ± 0.0072 against the candidate's 5.3724; diffusive.
- Mean-coupling baseline 3.8197 (candidate 3.8128).
- E[Cov(e_i, e_j | η, ζ_S)] = 3.83e−5 ± 1.5e−6, correlation 0.0108 (candidate 3.8e−5, 0.011).
- Engine check: on P0, one of six runs was 4.5 batch-SE low (5.3463), while its covariance entries agreed with the exact ones within 2 SE. The batch SE of the ratio is therefore optimistic, and the exact values are the reference.

## 2. Attempts that did not falsify

- **Collective clause** (04_collectives.tex:214-221): diffusive, r(A) ≥ 4.5 > 3.930, leak ratio 1. Holds at all 128 box corners.
- **Type-D nulls** (05_agency.tex:332-360):
  - N_hab and N_pr: every region is at most 1.54, against a lower window edge of 3.930.
  - N_lp, N_rn and N_fr: diagonal. I agree with Prop. C(iii).
  - N_eff and N_inf: inapplicable. There is no performative component a^e, record or act (02_framework.tex:13, 05_agency.tex:333).
- **N_ex**: inapplicable. Each relayed reading's noise is white, and each receiver sees it once, so the literal likelihood is already exact.
- **Agency**: the δ-like law is the G_C-minimizing profile. I re-derived f′ and f″ of Lemma D. The index is high for a reason that does not involve habit (P(S) = 1 − 2e−14 by expected free energy). C12 does not apply, because members never use internal attention.
- **(f)**: no deliberation chain exists, because each member's expected free energy ignores the others' policies.
- **O2(c)**: an interaction graph would have to contain all 10 positively coupled pairs, so clause (b) of the baseline reduces to the mean-coupling value, 3.817.

## 3. Weak points

**3.1 Memory clause depends on an undeclared initial law (new; computed values, interpretive reading).** Clause (ii) requires the input-conditional form whenever the blanket carries input, and P0's blanket does. That form is defined "with a Gaussian initial law" under the hypothesis that the input path is independent of (x_0, 𝔫). P0's stationary x_0 is not independent of its sensory inputs, because the world is persistent.

| Initial law | sup_t I(y_{t+1}; y_{0:t−1} \| y_t, ·) | Passes 0.03? |
|---|---|---|
| Noise-only stationary law (equivalently, the blanket path from round −5 or earlier) | 0.025717 | yes |
| Deterministic start, or qc·I | 0.037477 (at t = 2, or t = 1 for qc·I) | no |
| Members' full stationary law, noise-only dynamics | 0.070909 (t = 1) | no |
| Literal formula on the stationary process, blanket path from round 0 | 0.070515 (t = 1) | no |

The candidate's value is the most defensible one, since (i) opens with "evolve linearly given the blanket path". The grade still needs the initial law declared, or α_M ≥ 0.0375 to cover the framework's start. The same question applies to C11's memory clause; I did not compute that.

**3.2 Reading (g): the members do not interact, and P1 does not change that in substance (computed; interpretive).** 05_agency.tex:380 only reports Ω_int(C | ζ_{V∖C}), so P0 passes the letter. However, 05_agency.tex:294 says that "a structure should be called a collective only if it is produced by the members' interaction". In P1, deleting the links between members returns P0, whose r(A) = 5.3849 is not below P1's (candidate 5.3724; mine 5.375 ± 0.007). P1 meets only technical positivity of Ω_int(A | ζ_S).

Interaction-produced contrast is not excluded in this class. In quenched draws, a pair of members relaying to each other reaches r = 4.8870 (9 of 256 draws, computed).

**3.3 Participation ratio in N_pr (new angle; interpretive).** "Participation ratio" appears only in tab:agy-nulls (05_agency.tex:350). A P0 member's partner distribution has inverse-Simpson participation ratio 1.000000. Redrawing every round makes it 4, and only the drawn-once (quenched) null keeps it at 1. The quenched null is non-diffusive in 202/256 draws, which is R3's undefined-contrast problem. The verdict depends on reading the participation ratio per round.

**3.4 Selected partition when an agent belongs to no collective (new reading (h); interpretive).** 04_collectives.tex:219 defines a partition at level r0 as one whose blocks are all collectives. No block containing S qualifies (at most 2.326). P0 therefore has no partition at level r0, so "the selected partition" (05_agency.tex:333) is undefined in the full model and under every null. The candidate must declare a selector output that leaves agents unassigned, for example the collectives plus singletons. C11's two niches cover V and do not need this.

**3.5 R0, shared with C11 (computed).** If v_S is conditioned on, Σ^c is exactly diagonal and r(A) = 1.000000, so the dependence is total.
- Under R0, the purpose clause of 04_collectives.tex:131, "so that the remaining local noise is specific to each receiver", is false in P0.
- On the other side, 05_agency.tex:297 classes sensing noise as a private input, separately from sender-side broadcast noise. That supports R0 literally.

**3.6 Mechanism medium (interpretive).** Clause (c) at 04_collectives.tex:202 is undefined for heterogeneous types. I found no plausible medium above 5.385, but I recomputed only the mean-coupling and M-perm media. I did not recompute M-F, M-S or M-sym.

**Not checked:** the two-niche obstruction (check 12), the R_S scan (check 13), N_fg, P1's box and its M-F baseline 4.112, and the candidate's remark on I*'s index.

## 4. Readings and dependence

| Reading | Candidate | Verdict depends |
|---|---|---|
| (a), (e), (f) | as stated | no (confirmed) |
| Initial law of d_M | undeclared (noise-only stationary used) | yes (3.1) |
| R0 | adopted | yes, totally |
| N_pr redrawn every round; participation ratio per round | adopted / implicit | yes |
| Selector output when an agent is in no collective | undeclared | yes (3.4) |
| (g) | reported only | letter: no; substance: P0 and P1 both fail |
| Union-model reading | exact union | no (all three readings pass) |
| Coarse variable = scalar average | adopted | no |

## 5. Files

All files are in `C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round3\attack-audience\`. Every run was single-threaded and finished in under 45 s. No repository or vault file was edited.

- Libraries: `alib.py` (exact model), `amc.py` (MC engine for κ = 1), `amc2.py` (general MC engine).
- Exact quantities and controls: `a1_exact.py` → `a1_out.txt`.
- Quenched N_pr: `a2_quenched.py` → `a2_out.txt`; `a2b_quenched_regions.py` → `a2b_out.txt`.
- MC validation: `a3_mc_validate.py` → `a3_out.txt`.
- N_hab and N_pr: `a4_nulls.py` → `a4_out.txt`.
- Closure and inference: `a5_closure_inference.py` → `a5_out.txt`.
- Agency: `a6_agency.py` → `a6_out.txt`.
- P1: `a7_p1.py` → `a7_out.txt`; engine check `a7b_engine_check.py` → `a7b_out.txt`.
- Box and initial laws: `a8_box_transient.py` → `a8_out.txt`; `a9_inputcond_defect.py` → `a9_out.txt`; `a9b_fullinit.py` → `a9b_out.txt`.

## round3: performative-strict

VERDICT: Under strict typing (N_eff and N_inf of type D for every collective whose members act), the C8 obstruction extends to a broad class but not to every performative collective. Proved: (Lemma M) N_eff keeps the members' own act feedback and removes only the information the world path carries about their private inputs, so Sigma^c <= Sigma^c_eff in Loewner order. (Theorem O) A collective that is isolated and exchangeable under N_eff, and whose act information has disagreement rank below n-1, never has contrast above its N_eff contrast, so it never differs from N_eff. This covers equal loadings, heterogeneous or mixed-sign gains with n >= 3, members who sense the variable they act on, and any latency, memory or act noise. (Proposition E) Acts consistent with expected free energy under a common preference load every member's errors about one world component with one sign. Computed exhibit: a correlated-component pair (CCP) is a performative meta-agent under strict typing at grade (r0, alpha_M, alpha_I, alpha_pr, Agency0) = (3.75, 0.02, 0.05, 0.01, 0.25). Its two members sense correlated 'revenue' and 'cost' components, relay raw readings to each other, and regulate a common outcome with a common preference. r(pair) = 4.334 against a mean-coupling baseline of 3.222. Every applicable null is diffusive and selects nothing: N_eff and N_hab 1.809, N_lp 1.240, annealed N_pr 2.02-2.10. N_inf and N_ex are inapplicable; d_M = 5.1e-5, alpha_I = 0.032, agency 0.277; a common level holds at 17/17 points of a +-1% box. Neither mechanism forms the pair alone. The exhibit rests on four readings: (1) the D2 act rule; (2) the continuous-act agency extension; (3) clause (c), with the fixed relay schedule not declared as an interaction graph; (4) a declared contrast coordinate (each member's own sensed component, or a common direction near eta^a+eta^b). It fails under the coordinates eta^a, eta^b and eta^a-eta^b. By Lemma M, what separates any performative collective from N_eff is explaining-away structure created by conditioning on an outcome path its members steer. Strict typing therefore does not exclude such collider artifacts; it requires them. A pure-collider pair with no message channels meets every clause literally, with Omega_int(C|zeta_{V\C}) = 0. The author may want to exclude that case.
POSITIVE: True

## Performative-strict (round 3): can a performative collective differ from N_eff?

### Verdict

C8 extends to a proved obstruction, Theorem O, covering isolated collectives that are exchangeable under N_eff and whose act information has low rank. It does not extend to all performative collectives. I exhibit a performative meta-agent under strict typing, the correlated-component pair (CCP, computed), with every applicable null diffusive and differing. Three further constructions locate the boundary:
- **TDF** (two-department firm): needs reading (h).
- **Pure pair:** a definitional loophole, with no message channels and Omega_int = 0.
- **OPP** (opposite-preference pairs): agency index 0.

By Lemma M, under the world-conditional law every structure that differs from N_eff is an explaining-away (collider) structure. Under strict typing, collider artifacts are therefore required, not excluded.

### 1. Specification

**Target.** The target is open:agy-meta-agent-exists (s05_agency.tex:295-297), read under strict typing: N_eff and N_inf are type D for every collective whose members act. The table's wording, tab:agy-nulls 05_agency.tex:348-349, is replaced by this.

**Definitions used, read literally:**
- def:agy-meta-agent 05_agency.tex:379-381
- def:col-world-conditional 04_collectives.tex:130-132
- diffusive 04:147-151
- def:col-contrast 04:182-188 (second-moment convention :187)
- def:col-baseline 04:197-209 (clause (c) :202)
- def:col-collective 04:214-221
- def:agy-closure 05_agency.tex:13-24 (eta_C :11; constraint :27)
- def:agy-group-model 05:156-169
- def:agy-agency-index 05:240-246 (classes :251)
- def:agy-nulls 05:332-334 and tab:agy-nulls 05:337-360
- prop:agy-tests(b) 05:367
- prop:agy-nulls-vanish 05:309-317
- def:agy-order-parameter 05:296-302
- def:agy-joint-acts and thm:agy-joint-acts s05_agency.tex:146-181
- substitute selector s05:252
- def:fw-system 02_framework.tex:11-17
- def:fw-level0 02:313-328

**Conventions.** These follow the record:
- World-conditional law: condition on the whole world path, every component, including acted ones. Relay noise is receiver-specific. An agent's own sensing noise is private even when relayed.
- Contrast coordinates are prior errors, as in I*.
- Literal one-round latency.
- Exact steady-state Kalman filters with computation noise qc in P^-.
- Baseline: clause (c), mean coupling, comparison medium declared with the model.
- Annealed N_pr second moment as in round-1 attack A8, with P(seq | eta) approximated by P(seq).
- KL(encoded || union predictive) with the best constant encoding, the union filter using the members' own sensors (the round-2 convention).
- Agency index: habits fixed at the members' habits, gamma_C >= 0, belief pooled.

**Readings I adopt.** The column says whether the verdict depends on each.

| Label | Reading | Matters for |
|---|---|---|
| strict | N_eff, N_inf type D whenever members act | premise |
| rules | N_eff keeps every agent's update rule, including the use of acts it knows | Lemma M; irrelevant to TDF, pair, OPP, CCP (no member uses an act) |
| R3 | comparison medium held fixed under nulls | no construction's verdict changes (nulls fall far below) |
| D2 | each member draws its act from its own policy posterior, treating the other members' acts as habit draws (no intention sharing) | all constructions; makes N_inf inapplicable |
| cont | agency index in the continuous Gaussian extension of def:agy-joint-acts | agency numbers |
| (c) | clause (c) mean coupling; a fixed relay schedule does not declare an interaction graph (O2(c)) | all constructions: identical blocks fail under clause (b) by I1 |
| coord | declared scalar contrast coordinate for vector beliefs | CCP only (section 4) |
| (h) | a null whose world-conditional precision is not diffusive has no collective, so its selection is empty and differs | TDF only |
| inap | a null that leaves the model unchanged is inapplicable and imposes no requirement, including N_pr when no message channel exists | pure pair only |
| Omega | Omega_int(C\|zeta_{V\C})>0 is reported, not required (05:380) | pure pair only |

Readings (a), (e) and (f) of the task do not bear on the CCP:
- (a): its acts are genuinely performative.
- (e): attention is fixed, so the policy is the act alone and C12 does not apply.
- (f): under D2 there is no deliberation among members.

All differ verdicts below hold under both the C-specific reading (C is not a block of the null's selection) and the population-level reading (the whole selected partition differs).

### 2. Proved results

**Setting G.** World: eta' = F eta + B a + w. Agents' stacked internal state x' = A x + (terms in the conditioned path) + E xi, where xi collects the private inputs: sensing noise, receiver-specific channel noise, computation noise, and act noise read by the actor itself. Acts: a = Gamma x + (path terms) + Gamma_xi xi + nu, with nu read by no filter. All noises are Gaussian and independent across rounds. A and the full closed loop are stable. Let z be the stationary solution of z' = A z + E xi, and let ytilde_t = B Gamma z_t + B Gamma_xi xi_t + B nu_t + w_t.

**Lemma M (proved).** Sigma^c = S Cov(z_0 | ytilde_Z) S^T and Sigma^c_eff = S Cov(z_0) S^T. Hence

Sigma^c_eff - Sigma^c = S Cov(E[z_0|ytilde]) S^T >= 0, and Pi^c >= Pi^c_eff.

*Proof.* By superposition, x = xbar + z, with xbar a causal linear functional of the conditioned path. In the full model, ytilde_t = eta_{t+1} - F eta_t - B(Gamma xbar_t + path terms) is a causal function of the path. Conversely, eta is the stationary solution of the closed loop driven by ytilde, so the two generate the same sigma-algebra. Since xbar_0 is conditioned on, Cov(x_0|eta) = Cov(z_0|ytilde). Under N_eff, eta is a function of inputs independent of xi, and z is the same process (same A, E, xi), so Cov(x_0|eta) = Cov(z_0). The Gaussian law of total covariance finishes the proof. ∎

Consequences:
- All act feedback on the members given the path (D_fb of C7) lies in A, so it is present in both laws.
- N_eff removes exactly the explaining-away correction, which vanishes iff Cov(z_0, ytilde) = 0.
- Under the alternative reading (members re-derive their filters under N_eff), D_fb also differs. For EFE-consistent acts in setting P this still lowers the full model's contrast (Prop N).

Checks (check0):
- Sigma_eff by window conditioning equals the private Lyapunov covariance to 3.7e-15.
- min eig(Sigma_eff - Sigma_full) = -5.0e-16; the reversed order fails (-1.64e-4).
- Round-1 values reproduced: 7.425938378 without acts, 6.169015189 with acts. Under N_eff the latter becomes 6.183069.

**Theorem O (proved).** Let C have n >= 2 members with scalar contrast coordinates, and assume:
- **(O1) isolation:** C is uncorrelated with V\C under N_eff.
- **(O2) exchangeability:** the law of z is invariant under the action of each permutation of C on its agents' local states.
- **(O3) rank:** ytilde loads on (z_C, xi_C) through coefficient vectors kappa^(r) applied to agent-canonical patterns, and W = span{P_{D_C} kappa^(r)} has dim W < n-1. Equal loadings give W = {0}.

Then x_out(C) >= x_out^eff(C), and if Pi^c is diffusive then x_in(C) <= x_in^eff(C). Hence either Pi^c is not diffusive or r(C) <= r_eff(C). If Pi^c_eff is diffusive, C is a collective under N_eff at every level at which it is one in the full model (leak ratio 1, baseline fixed), so C never differs from N_eff.

*Proof.* By Schur's lemma for S_n on R^n ⊗ R^d, the standard component D_C ⊗ R^d evolves as i.i.d. copies along any orthonormal basis of D_C, independent of the trivial part and, by (O1), of V\C. For a unit f in D_C orthogonal to W, the f-copy enters ytilde through neither states nor noises. For the noise terms, equivariance gives Cov((f⊗I)z_t, m^T xi_s) = (h_0 - h_1)(kappa^T f) = 0. The f-copy is therefore independent of ytilde and of every other direction, so f is an eigenvector of both Sigma^c and Sigma^c_eff with the same eigenvalue alpha. Then:
- x_in(C) <= f^T Pi^c f - sum_i a^∂_i f_i^2 <= alpha^{-1} = x_in^eff when Pi^c is diffusive.
- x_out = phi^T Pi^c phi >= phi^T Pi^c_eff phi by Lemma M. ∎

Coverage (candidates (b) and (d) of the task, and (a) inside an exchangeable block):
- setting P, generalized to latency, memory, act noise and feedback;
- members who sense the acted variable;
- heterogeneous or mixed-sign gains with n >= 3;
- other acting groups with independent ancestry.

Each hypothesis is needed (computed): EXP-c violates (O1) (gains up to 11%); NEG-a and NEG-b violate (O3) and (O2) respectively.

Checks: check1 O1-family 0 violations in 131 diffusive draws; O2-family 0 in 169. The disagreement eigenvalue is equal in both laws to 8.3e-14.

**n = 2, same sign, unequal loadings: not covered.** Numerically 0 gains in 280 diffusive draws (check10). This is a conjecture; the one-shot static case is proved, since (c_1-c_2)^2 < (c_1+c_2)^2.

**Proposition E (proved).** Setting: def:agy-joint-acts with additive effects on a scalar acted component, a common outcome map h, common Lambda, true effect models and Gaussian habits. The world's mean act input is -sum_j w_j z_j / h_Z with weights w_j >= 0, where z_j = h^T F m_j + (terms without m_j):
- D2: w_j = gamma Lambda mu_j^2 s_j^2.
- D1: w_j = gamma Lambda sigma_j^2 mu_j^2 / (1 + gamma Lambda sum_k sigma_k^2 mu_k^2), from Sherman-Morrison on the tilted-habit group posterior.

So member j's belief about component k loads with sign -sign(h_Z (h^T F)_k), common to all members. Opposite loadings therefore need one of:
- different components entering the outcome with opposite signs (TDF, CCP);
- opposite preference maps (OPP, where agency is lost);
- misjudged effect signs.

**Proposition D (proved).** Under a null that keeps the acts, let members i and j be uncorrelated and interchangeable in the private law, with k_i ≠ 0. Then Sigma^c_ij = -|k_i|^2 < 0. By C4 (Z1), the null's precision is then not diffusive.

Check: TDF N_lp gives Sigma_ij = -5.662315e-3, equal to minus the correction's diagonal; the full-model value is +1.121942e-2 (check9).

**Proposition T (proved).** In the TDF, consider the group generated by within-department swaps and the exchange B<->S with eta^1<->eta^2, eta^Z -> -eta^Z, w^Z -> -w^Z and a_B <-> -a_S. It preserves the law and the conditioning. Hence on each firm Sigma^c = alpha P_w + v P_c + v_d P_d, with alpha and v at their N_eff values and v_d <= v. It follows that:
- r(C) = v·min(alpha^{-1}, v_d^{-1}) <= v/alpha = r_eff(B), and r_eff(C) = 1;
- the firm stays diffusive iff 1/v_d <= 2/alpha - 1/v (n_d = 2).

Check: check2, where only the d-mode changes, to 1e-13.

### 3. Candidates of the task

All values use exact window conditioning, L = 40-60, converged.

| Candidate | Result | Status |
|---|---|---|
| (a) opposite-sign sub-groups inside one exchangeable block, n >= 3 | never differs from N_eff | proved (Thm O) |
| (a) opposite-sign pair, no channel | r 2.574 vs N_eff 1 | computed (pure pair) |
| (a) opposite-sign pair with relays (same component) | gains in 245/292 draws (up to 63%); OPP instance passes every null but agency index 0 | computed |
| (b) members sensing the acted variable (setting P, latency, feedback) | never differs: e.g. PN-latency 6.169 vs N_eff 6.183 | proved and computed |
| (c) acts on an outcome coupling different components (TDF, CCP) | differs | computed |
| (d) heterogeneous gains, n >= 3 | never differs | proved |
| (d) n = 2, same sign | 0/280 | numerical |
| decoupling (C communicating with outsiders, same-sign acts) | contrast up by at most 10.8% | computed, not developed |

### 4. Exhibit: the correlated-component pair (CCP)

**Specification.**
- Two firms, independent worlds. Firm f has b_f sensing eta^a and s_f sensing eta^b: AR(1) components with F = 0.9, Q = 0.05 and innovation correlation rho = 0.5.
- Sensors have R = 1. Each member models (eta^a, eta^b) jointly on (eta_t, eta_{t-1}) with an exact Kalman filter and qc = 1e-4.
- Each member reads the other's raw reading with one-round latency and Rc = 0.1.
- The outcome is renewed: eta^Z_{t+1} = (eta^a_t - eta^b_t) + (u_b + u_s) + w^Z, with QZ = 0.05.
- Common preference N(0,1) on eta^Z. D2 act rule: u_j ~ N(-kappa(m_j^a - m_j^b), s2), with gamma = 70, habits N(0, 1/30), s2 = 0.01, kappa = 0.7.
- Attention is fixed. No member reads an act or senses the outcome.

**Clauses**, with the 'own' coordinate (each member's prior error about its sensed component):

| Clause | Value | Grade | Margin | Status |
|---|---|---|---|---|
| diffusive Pi^c | pair block (52.976, -33.111), cross-firm 0 | - | - | computed |
| collective | r(pair) = 4.3336; leak ratio 1; other regions <= 1.000 | r0 = 3.75 | 0.58 | computed |
| baseline (c) | 3.2224 at centre; ±1% box lower edge 3.3575 | r0 > | 0.39 | computed |
| memory (2-d pooled average of current prior means, eta_C = (eta^a, eta^b)) | d_M = 5.1e-5 | 0.02 | 0.02 | computed |
| inference | alpha_I = 0.0317 | 0.05 | 0.018 | computed |
| N_eff (D) | diffusive, r 1.809, selects nothing | differs | 1.94 | computed, exact |
| N_hab (D) | 1.809 (equals the N_eff law) | differs | 1.94 | computed |
| N_lp (D) | diffusive, 1.240 | differs | 2.51 | computed |
| N_rn, N_fr (D) | no relay information, as N_lp | differs | - | structural, not computed |
| N_pr (D), every round, zero-gain | diffusive; 2.016, 2.097, 2.042 in 3 annealed estimates | p = 1/(n_null+1) = 0.001 | 2.2 | numerical; 999 draws not run |
| N_inf (D) | inapplicable: no channel reads an act | - | - | proved |
| N_ex (S) | inapplicable: filters exact | - | - | proved |
| agency | 0.277 | 0.25 | 0.027 | computed (cont) |
| Omega_int(C\|zeta_{V\C}) | >0: relays carry each member's sensing noise to the other | reported | - | generic positivity (prop:agy-nulls-vanish(c)); not computed |
| N_w (E) | within-firm components correlated, so it predicts the firms | restricts the claim | - | interpretive |

**Robustness.** On a ±1% box (17-point resolution-IV design over F, Q, R, Rc, qc, kappa, s2, QZ) the common level is r0 = 3.749, inside (3.3575, 4.1411], with every verdict holding at 17/17. Alpha_I and agency were computed at the centre only.

**Coordinate dependence (check15, check15b, check16).**
- Coordinates eta^a and eta^b fail: N_eff 5.731 > full 5.384.
- Coordinate eta^a - eta^b fails: N_eff 7.821 > full 1.786.
- The common sum coordinate (45°) passes: r 6.364, baseline 4.576, N_eff 5.261, N_lp 1.007 (diffusive), N_pr 2.21-2.33. The ±1% box has a common level r0 = 5.78 at 17/17.
- N_lp stays diffusive only for directions in [35°, 55°].

### 5. Other constructions

**TDF** (two departments of two per firm; scalar beliefs; κ* = 0.68). Grade (4.06, 0.02, 0.05, 0.01, 0.10) on a ±1% box (r0 window (4.0066, 4.1161], 17/17); at the centre, window (3.8747, 4.3452].
- The firm is a near-uniform clique (couplings 14.21 and 14.43, leak 17.12).
- N_eff and N_hab select the four departments (exact); N_inf and N_ex are inapplicable.
- d_M = 8.7e-5, alpha_I = 0.037, agency 0.138.
- N_lp, N_rn and N_fr are non-diffusive at every κ ≠ 0 (Prop D). Annealed N_pr is non-diffusive (largest positive entry +9.3 to +11.3).
- It therefore passes only under (h), or under the substitute selector (s05:252) with the kept-gain convention. It fails under the substitute selector with the zero-gain convention (p = 1).
- At ±2% every local window is nonempty but there is no common level; at ±5%, 2 of 17 local windows are empty.

**Pure-collider pair** (single-agent departments, no message channel). Grade (2.29, 0.02, 0.01, vacuous, 0.50) on a ±1% box (17/17).
- r 2.574 vs baseline 2.049; N_eff and N_hab give r = 1.000000000000.
- d_M = 0 exactly; alpha_I = 1.5e-3.
- N_lp, N_rn, N_fr, N_pr, N_inf and N_ex are inapplicable.
- Omega_int(C|zeta_{V\C}) = 0 by causal separation.
- It meets every clause literally under readings inap and Omega. This is a definitional loophole.

**OPP** (same-component pairs, opposite preference maps). All nulls are diffusive and differ:
- window (4.278, 5.916];
- N_eff 3.605, N_lp 3.265;
- N_pr 4.37-4.49 (zero-gain) and 3.26-3.31 (kept-gain), so r0 > 4.49 is needed for the per-level comparison;
- ±1% box common level at r0 = 5.06, 17/17;
- closure passes (d_M = 7.9e-6, alpha_I = 0.021).

Agency index is 0.0000 for three declared fixed-habit classes, so it fails at every Agency0 > 0.

**Delegates** (one actor per department): N_lp stays diffusive, but no window exists.

### 6. Grade frontier by reading combination (strict typing throughout)

| Construction | Extra readings needed | Largest Agency0 | Breaks under |
|---|---|---|---|
| CCP | D2, cont, (c), coord ∈ {own, common directions 35°-55°} | 0.277 | coordinates eta^a, eta^b, eta^a-eta^b; relay schedule declared as a graph |
| TDF | + (h) | 0.138 | substitute selector with zero-gain N_pr; graph declaration |
| Pure pair | + inap, Omega | 0.515 | applicable N_pr or Omega_int > 0 required |
| OPP | none beyond D2, cont, (c) | 0 | agency |

### 7. Scripts and deciding outputs

Folder: C:/Users/CHRISA~1/AppData/Local/Temp/claude/63c81c17e87f0010/34faeca5-ea90-45d1-8cc4-412bdf898c58/scratchpad/metaagent/round3/performative-strict/

- **Libraries:** lgx.py, lgx2.py (multi-component beliefs; reproduces lgx to 0.0), tdf.py.
- **Scripts, each with its *_out.txt:** check0_validate, check1_obstruction, check2_tdf_scan, check3_instance, check4_npr, check5_closure_agency, check6_delegates, check7_pair, check8_box, check9_pair_box_propD, check9b_pair_box1, check10_n2, check11_opp, check12_opp_instance, check13_ccp_scan, check14_ccp_instance, check15_ccp_coords, check15b_directions, check16_ccp_sum.
- **Extra outputs:** check8_out_hw0.01.txt and check8_out_hw0.02.txt.
- **Run conditions:** all runs single-threaded, each under 20 s. No repository or vault file was edited.

Every check declared its expectation before running. Expectations that failed:
- check4 E1: kept-gain N_pr turned out non-diffusive.
- check8 E1 at ±5%: no common level; at ±5%, 14/17 points have agency >= 0.1 (minimum 0.097).
- check7 E4: the pair's alpha_I is 1.5e-3, not below 1e-3.
- check9(i): no common level at ±5% for the pair.
- check12 E4: agency came out 0, not small and positive.

### 8. Weakest point, open obligations, next action

**Weakest points.**
- The CCP's verdict depends on the declared contrast coordinate, and the most natural common coordinates fail.
- If a fixed relay schedule declares an interaction graph, clause (b) makes identical pairs their own comparison medium (I1).
- The cross-member glue that N_eff detects is explaining-away from conditioning on an agent-driven outcome. This is the dependence ex:agy-collider (s05:240-242) warns against.
- Agency rests on the continuous extension, with a margin of 0.027 at Agency0 = 0.25.
- The open subset rests on a ±1% box; continuity is unproved (O6).

**Minimal unresolved obligation.**
- Author rulings on coord, (c)/(b) and (h).
- Whether Omega_int(C|zeta_{V\C}) > 0 should be a clause rather than a report.

**Next action.**
- Run a fresh-context attack on the CCP with independent code.
- Run the N_pr test with 999 annealed draws and compute N_rn and N_fr explicitly.
- Build a heterogeneous-firm CCP to remove the clause-(b) dependence.

## round3 attack: performative-strict

# Attack on 'performative-strict' (round 3)

## Verdict

**The CCP exhibit survives at its stated grade, (r0, αM, αI, αpr, Agency0) = (3.75, 0.02, 0.05, 0.01, 0.25), under the candidate's own readings.** Its footing is narrower, and its agency margin thinner, than the report says.

I rebuilt the model from the report's specification with my own code, without using the candidate's scripts:
- Every deciding contrast number reproduces to the printed digits.
- The nulls the candidate left uncomputed (N_fr, N_rn, kept-gain N_pr) all fall below the window's lower edge.
- The literal partner-randomization test with 999 draws gives p = 0.001 (computed).
- Theorem O survives an independent numerical test (numerical): no violations in 445 diffusive draws with n = 3 or 4.

Four defects. None overturns the exhibit under its stated readings; two of them break the stated grade under readings the candidate did not flag.

1. **Refuted (computed): the claim that common contrast coordinates (35° to 55°, including the sum at 45°) also pass.**
   - The candidate applied a declared-level test here.
   - Under the record's locked every-selector-constant reading, the claim fails at 45°: N_eff = 5.2605 lies inside the window (4.5763, 6.3644]. So at every level in (4.576, 5.261], N_eff selects the same pairs.
   - Every common direction from 0° to 180° fails the same way, either with N_eff above the baseline or with an empty window.
   - The exhibit therefore rests on the member-specific 'own' coordinate alone.

2. **Unflagged reading (computed): partner randomization must be redrawn every round.**
   - tab:agy-nulls also permits drawing partners once (05_agency.tex:350).
   - Exact enumeration of all 3^4 = 81 assignments gives P(S ≥ S0) = 17/81 = 0.210 under zero gain. Under kept gain it is 1/81 = 0.012, with 70 of 81 assignments non-diffusive, scored as not exceeding S0.
   - The reason is that a firm whose two members draw each other reproduces S0 exactly, which happens with probability 1/9 per firm.
   - So the test of prop:agy-tests(b) (05_agency.tex:367) does not reject at αpr = 0.01. It would need αpr of about 0.24 (zero gain) or about 0.02 (kept gain).

3. **Unflagged reading (computed): the agency belief is not a function of the declared coarse variable.**
   - The class sets z_C to the mean of the members' posterior z (check14_ccp_instance.py:91).
   - Closure is declared on the average of the members' current prior means.
   - def:agy-group-model requires the belief to be "declared as a function of the collective's coarse state" (05_agency.tex:157).
   - With the belief a function of the start-of-round coarse state y(t), the index is 0.1283, below 0.25.
   - Two repairs pass. Using the end-of-round state y(t+1)/F gives 0.2647. Re-declaring closure on posterior means gives αI = 0.0452 (margin 0.005) and d_M = 3.0e-6.

4. **Margin correction (computed): the stationary-law agency index is 0.2654, not 0.2772.**
   - 0.2772 reproduces exactly on the candidate's own declared set of 300 states (seed 7).
   - That set has mean KL(P‖E) = 1.474, below the minimum (1.480) of 60 independently drawn 300-state sets. Their indices span 0.254 to 0.276, with mean 0.266.
   - The margin over Agency0 is 0.015, not 0.027.

**Weakest point: the contrast coordinate.**
- def:col-contrast (04_collectives.tex:187, appA_notation.tex:221) admits vector errors only in the form Σsc⊗I_K. The CCP's 2×2 agent blocks deviate from scalar·I_2 by 0.0237, against entries of 0.017 to 0.031 (computed). Read literally, contrast is undefined for the CCP's errors.
- The record's "declared scalar coordinate" convention was set in I*, where every member of a candidate collective shared one coordinate. 'own' assigns different world components to the two members of one collective, and no shared coordinate passes (item 1).

## Definitions used, and readings I adopt

**Definitions.** All read literally:
- def:agy-meta-agent, 05_agency.tex:379-381
- def:col-world-conditional, 04_collectives.tex:130-132
- diffusive class, 04:147-151
- def:col-contrast, 04:182-188 (vector clause at :187)
- def:col-baseline, 04:197-209 (clause (b) at :201, clause (c) at :202)
- def:col-collective, 04:214-221
- rem:col-declared-geometry, s04_collectives.tex:146-147
- def:agy-closure, 05:13-24 (η_C at :11; memory form (i) at :20; declaration (ii) at :21)
- prop:agy-pooling(a), 05:113
- def:agy-group-model, 05:156-169
- def:agy-agency-index, 05:240-246
- def:agy-nulls, 05:332-334
- tab:agy-nulls, 05:337-360
- prop:agy-tests(b), 05:367
- def:fw-system, 02_framework.tex:11-17 (factorization at :22)
- def:fw-level0, 02:313-328
- def:agy-joint-acts, s05_agency.tex:146-152
- ex:agy-collider, s05:240-242
- open:agy-meta-agent-exists, s05:295-297

**Readings.**

| Reading | Choice | Does the verdict depend on it? |
|---|---|---|
| Act timing | D2 act on the posterior m⁺(t); this reproduces r(pair) to 1e-8 | No |
| Relayed sensing noise | An agent's own sensing noise stays private when relayed (the record's convention) | Yes. Conditioning on it as a noise shared by several receivers shrinks the window to (1.0039, 1.0058], with N_eff 1.0000 and other nulls not computed (computed, a8) |
| Every selector constant | Every level in the full model's admissible window (r̄_hom, r(C)], comparing with the medium held fixed (R3) and with the null's own mean-coupling medium | Same verdict both ways for 'own'; decides the common coordinates |
| Memory clause | Input-conditional form, because the blanket carries sensory input | See closure below |
| Inference clause | Best-constant encoding against the union-model predictive | See closure below |
| Agency | D2, continuous-act extension, habits fixed at N(0, 1/30), γ_C ≥ 0 | Yes (items 3, 4) |
| Comparison medium | Clause (c) mean coupling | Yes. Under clause (b), I1 removes every collective; this is the record's O2(c). rem:col-declared-geometry's last sentence ("a model whose declared couplings contain a partition cannot claim to have found it") applies, because the CCP's relays and outcomes are declared per firm (interpretive) |

## Deciding numbers recomputed with independent code

My implementation passes two cross-checks:
- Window conditioning matches an independent frequency-domain Wiener smoother to 3.5e-15.
- Monte Carlo reproduces the Lyapunov covariances, with |z| < 1.6.

| Quantity | Candidate | Mine | Status |
|---|---|---|---|
| Π^c pair block; r(pair) | (52.976, −33.111); 4.3336 | (52.976081, −33.111044); 4.33360 | computed |
| Mean-coupling baseline; other regions | 3.2224; ≤ 1.000 | 3.22240; 1.00000 | computed |
| N_eff = N_hab | 1.809 | 1.80926 | computed |
| N_lp | 1.240 | 1.7311 (pure noise of variance Rc); 1.2397 (variance R+Rc, the candidate's unstated convention); 1.1893 (matched marginal variance) | computed |
| N_fr | not computed | 1.7311 (fresh receiver noise; identical to N_lp at Rc); 1.8521 (relay frozen with its noise) | computed |
| N_rn | not computed | 1.5335 (own sensor only); 1.4005 (own sensor read twice) | computed |
| N_pr, every round, zero gain | 2.016 to 2.097 (3 estimates) | 2.0487 from 2000 sequences, halves 2.0512 and 2.0463 | numerical |
| N_pr, every round, kept gain | not computed | diffusive; firm pairs 1.612 and 1.604; whole population 1.535 | numerical |
| Literal N_pr test, n_null = 999 | not run | maximum 2.539 against S0 = 4.3336; p = 0.001. Control (mate always read) equals S0 to 4e-9 | numerical |
| Every-constant test for 'own' | claimed | 0 of 401 levels in the window select the same partition for all 8 null variants; the control (full model as its own null) gives 401/401 | computed |
| d_M | 5.112e-5 | 5.1122e-5. This is the stationary law of y given the whole sensory path (input-free internal process) | computed |
| α_I (plain average of prior means) | 0.0317 | 0.03165, with union P⁻ diagonal 0.159088 | computed |
| Agency on the candidate's 300-state set | 0.2772, KL(P‖E) 1.474 | 0.2772, 1.4737 | computed |
| Agency at the stationary law | not reported | 0.2654. Closed form agrees with a brute-force check (0.2658), and the negative control gives 1.0000000000 | computed |

## Further findings

**Closure depends on the declaration.**
- The memory clause passes under every input-conditional form:
  - The input-free form gives 5.11e-5.
  - The literal form in the actual joint law, conditioning on the blanket path from 0 to t, gives a supremum of 1.53e-4 on sensors alone and 1.29e-4 with acts included.
  - The unconditional stationary law of y gives 0.360. That is not the definition's form for a blanket that carries input, but it fails αM = 0.02 if the author intended it.
- The inference clause:
  - The plain average passes: 0.0317 with a best-constant encoding, 0.0338 encoding the average of the members' P⁻.
  - The prior-corrected logarithmic pool fails αI = 0.05: 0.120 with a best-constant encoding, 0.142 encoding Λpool⁻¹. This is the manuscript's own union-posterior pooling rule (prop:agy-pooling(a)); it fails because the relays make the members' data overlap.

**The agency frontier depends on the declared belief (computed).**

| Group belief z_C | Index |
|---|---|
| Start-of-round coarse state D y(t) | 0.128 |
| End-of-round coarse state | 0.265 |
| Union posterior | 0.292 |
| Log pool of posteriors | 0.730 |
| λ·D y(t), scale λ declared in advance | 0.639 |
| λ·(mean posterior z), scale declared in advance | 0.800 |

So Agency0 = 0.25 is neither the frontier nor stable under declaration. Agency0 > 0 holds under every declaration I tried.

**Open neighborhood (numerical).** My own Latin-hypercube design over 9 parameters, including ρ, which the candidate's box held fixed:
- **±1% box (64/64 points):**
  - The common window is (3.3212, 4.1893], which contains 3.75.
  - The every-constant test holds everywhere: largest null 1.940, smallest local baseline 3.126.
  - d_M and αI pass everywhere.
  - Agency is at least 0.25 at only 62 of 64 points (minimum 0.2479). The definition asks for agency only at the instance.
- **±5% box:**
  - There is no common level: the intersection of windows is empty, (3.7174, 3.6083].
  - Agency falls below 0.25 at 23 of 64 points, and posterior-average αI exceeds 0.05 at 17 of 64.
- Continuity of the stationary law in the parameters (O6) is still unproved.

**Nulls called inapplicable.** I confirm that N_inf (no channel reads an act) and N_ex (the filters already fuse exactly; nothing reaches members through acts) leave the model unchanged. No inapplicability claim fails.

## The candidate's proved claims, tested

**Lemma M** is consistent with the CCP (computed). Σ_eff − Σ^c = 0.008104·[[1,−1],[−1,1]], which is positive semidefinite.

**Theorem O** survives (numerical). Setup: an exchangeable isolated niche with raw relays and mixed-sign heterogeneous act gains on a renewed outcome nobody senses.

| Case | Diffusive draws | Draws with r > r_eff | Largest r/r_eff − 1 |
|---|---|---|---|
| n = 3, mixed signs | 231 | 0 | −1.9e-5 |
| n = 4, mixed signs | 214 | 0 | −3.5e-5 |
| n = 2, mixed signs (control; not covered by the theorem) | 366 | 229 | gains up to 16.8× |
| n = 2, same sign | 228 | 0 | consistent with the candidate's conjecture |

The n = 2 mixed-sign control shows the test can detect gains.

## Other constructions

- **Pure-collider pair.** "Meets every clause literally" holds only under the candidate's 'inap' reading for N_pr (interpretive). def:agy-meta-agent names "N_pr at level α_pr with the declared number n_null of null draws" as a requirement in its own right, and the open problem asks for "partner randomization at a stated level". With no message channel, N_pr leaves the model unchanged, so every draw ties S0 and p = 1. The grade's αpr is "vacuous", so no level is stated.
- **TDF and OPP.** Not recomputed.

## Expectations declared before running that failed

- a1 E1: N_lp = 1.2397 under my default convention. It came out 1.7311. The candidate's value corresponds to pure noise of variance R+Rc (a5).
- a2b: I expected kept-gain annealed N_pr to be non-diffusive. It is diffusive, at 1.61.
- a3 E2: I expected the unconditional d_M to be about 5e-5. It is 0.360; the candidate's number is the input-free form.
- a3b E3: I expected a declared belief scale to keep the start-of-round index below 0.25. It reaches 0.639.
- a4 E1: I expected agency at least 0.25 at every ±1% point. It holds at 62 of 64.
- a5 E2: the control's tie tolerance (1e-9) was too tight. a5b shows the control equals S0 to 4e-9.

## Minimal unresolved obligations, and next action

**Author rulings needed:**
1. Whether def:col-contrast admits member-specific declared coordinates. This decides the CCP outright, since no shared coordinate passes.
2. Whether both forms of N_pr (redrawn every round, or drawn once) must be passed.
3. Whether the agency belief must be a function of the coarse state at the start of the decision round.
4. The existing readings O2(c), D2 and the continuous-act extension.

**Next action.** Build a larger CCP population with k firms. Drawing partners once then reproduces a firm's pair with probability about 1/(4k), so p < 0.01 needs about 25 firms. More firms also lower the mean-coupling baseline toward 1 + a/ε = 2.667. This addresses item 2. Item 1 cannot be repaired inside this construction.

## Files

All runs were single-threaded, one at a time, each under 70 s. No repository or vault file was edited.

Folder: C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round3\attack-performative-strict\

- **Libraries:** ccp_lib.py, ccp_full.py
- **Scripts:** a0_validate.py, a1_nulls_coords.py, a2_npr.py, a2b_npr_kept.py, a3_closure_agency.py, a3b_agency_variants.py, a3c_posterior_closure.py, a3d_seed7.py, a4_box.py, a5_npr_test_and_conventions.py, a5b_control.py, a6_theoremO.py, a7_npr_quenched.py, a8_shared_sensing_noise.py
- **Outputs:** each script has a matching a*_out.txt in the same folder, for example C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round3\attack-performative-strict\a7_out.txt

## round3: continuity

# O6 (continuity): stationary policy–covariance law, Σ^c and the selection functionals of I*

Label: continuity. Output folder (scripts and outputs): C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round3\continuity\

No repository or vault file was edited.

## 1. Verdict

**O6 is proved for I*** (record C11). The proof covers:
- both deliberation protocols: T-fast, which runs (P4) at a frozen decision state, and T-real, with one revision per round;
- the clause (c) mechanism medium;
- the nulls N_hab, N_pr (redrawn every round), N_lp = N_rn and N_fr;
- every finite precision 0 ≤ γ < ∞.

**What is proved.**
- **(i)** The chain (policy, Kalman covariance) has a unique stationary law μ_θ. Every initial law converges to it geometrically in a Wasserstein distance. Convergence is not in total variation.
- **(ii)** θ ↦ μ_θ is continuous, with modulus O(ω log(1/ω)).
- **(iii)** Σ^c(θ) = E[Cov(e(t)|η)] (04_collectives.tex:187) exists, is unique, is continuous and satisfies Σ^c ⪰ q_c I. It is exactly blockdiag(αI₄ + β11ᵀ, αI₄ + β11ᵀ).
- **(iv)** The following are continuous: r(A), the mechanism baseline, the mean-coupling baseline, every null contrast, and the agency index at fixed declared decision states.

**What this gives the differ clause.** The open-subset clause of "differs" (05_agency.tex:333) holds on an explicit open set U of the admitted parameter family as soon as finitely many strict inequalities hold at one point. At θ* the round-2 numbers satisfy them. The smallest margin is 0.558 contrast units, 77 SE, for r0 = 3.5 against the T-real medium; the margin over the whole window is at least 1.056 (140 SE). These center values are numerical. The open neighborhood in C11 therefore rests on proved continuity plus numerical center values, no longer on the box.

**Where it fails.** Uniqueness fails at γ = ∞ (computed, check B2), so the admitted class must keep γ finite.

**The citation in the assignment is wrong.**
- The paper is P. Bougerol, "Kalman filtering with random coefficients and contractions", SIAM J. Control Optim. 31(4):942–959 (1993), doi:10.1137/0331041. It is not in Ann. Appl. Probab.
- I read pp. 942–953: Theorem 1.7 (Riccati maps contract the Riemannian metric), Theorem 2.4 (stationary solution) and Theorem 2.6 (filter stability).
- Its hypotheses fail for I* in two ways:
  - It assumes nonsingular A_n; p. 942: "our approach does not apply in the singular case". In I*, A_F = [[F,0],[1,0]] is singular.
  - It assumes an exogenous stationary ergodic parameter process. In I* the policy process is generated by feedback from the covariance.
- The proof below therefore does not use Bougerol.

**I\*\* is not defined** anywhere in the record, the reports or the round-3 folders (strict-construction/ was empty). Section 8 gives the hypotheses to check for it.

## 2. Target and readings

**Target.** Record O6 (open_agy_meta_agent_exists.md:207): continuity in θ of the quantities the open-subset part of "differs" rests on. These are:
- the stationary law of the chain under EFE policies, and its uniqueness;
- Σ^c under the second-moment convention;
- r(A);
- the clause (c) baselines;
- the null contrasts;
- the agency index.

**Definitions used.**
- def:fw-system, one γ: 02_framework.tex:11-17.
- def:col-world-conditional: 04_collectives.tex:130-132.
- Diffusive class: :147-151.
- def:col-contrast: :182-188; second-moment convention :187.
- def:col-baseline: :197-209; clause (c) :202.
- def:col-collective: :214-220.
- (P4): 05_agency.tex:167.
- def:agy-agency-index: :240-246; class restriction :249-251.
- def:agy-nulls and tab:agy-nulls: :332-360.
- def:agy-meta-agent: :379-381.
- Record C1: :34-41. Record C11: :146-154.

**Readings adopted, and whether the verdict depends on each.**

| Reading | Content | Verdict depends? |
|---|---|---|
| R1 | Admitted class = the I* architecture with θ = (F,Q,R,R_c,R_s,ψ,γ,q_c) in an open subset of (0,1)×(0,∞)⁴×ℝ×(0,∞)×(0,∞) (the round-2 box family); n = 4, κ = 12 and the two niches fixed. | No: the result holds for any admitted class that contains this family as an open subset. |
| R2 | "Each constant of the selector" read both as every r0 in the local window and as the declared r0 = 3.5. | No |
| R3 | Σ^c by the second-moment convention, conditioning on the world path. Own sensing noise is private even when relayed (record convention). | No: same as round 2. |
| R4 | Protocols as implemented: T-fast lib.py:239-259, T-real lib.py:265-345. | No |
| R5 | A null whose world-conditional precision is not diffusive contains no collective (def:col-collective needs diffusivity, 04_collectives.tex:215). | Only for N_fr under T-real, whose β is −4.4e−6 ± 2.7e−6 (nulls_real_out.txt) and −5.2e−7 ± 1.3e−6 (check3_out.txt): sign unresolved, numerical. |
| R6 | Agency decision states are declared fixed covariance points. The decision law at X is the protocol kernel at X. | Only Proposition 4 uses it. |

## 3. Setting, hypotheses, verification for I*

**Setting.** One niche of n members: n = 4 in I*, n = 8 with one component in the medium.
- Policy π = (σ, J): σ ∈ {0,1}ⁿ is the slot profile and J_i ⊂ mates are the attention sets; 𝒫 is finite.
- Covariance state p ∈ [0,∞)ⁿ, with p_i the posterior variance of η after the last update.
- Riccati step (lib.py:56-71): p_i ↦ g_θ(p_i; a, b_i), with a = 1/R + |σ|/R_s and b_i = |J_i|/(R+R_c).
- Chain Z_t = (p(t−1), π_t): p(t) = G_θ(p(t−1), π_t), and π_{t+1} ~ k_θ(p(t), π_t; ·).
- T-fast kernel: the (P4) stationary law at the frozen state p(t), using the soft-min slot EFEs, followed by Gibbs attention.
- T-real kernel: a uniform reviser makes a logistic flip, followed by Gibbs attention.

**Hypotheses** (θ in a compact set U):
- **(H1)** G_θ(·,π) is jointly continuous, and a compact set 𝒦_U is invariant under all G_θ(·,π).
- **(H2)** For every policy sequence, |G^{(t)}(p) − G^{(t)}(p′)|_∞ ≤ C₁ρᵗ|p − p′|_∞ with ρ < 1.
- **(H3)** k_θ(p,π;·) is jointly continuous and Lipschitz in p in total variation, with constant L.
- **(H4)** supp k_θ(p,π;·) = 𝒮(π) does not depend on (θ,p). On the support k_θ ≥ κ₀ > 0. There are m and π★ such that every π reaches π★ in exactly m support steps.
- **(H5)** Policy randomness is independent of the world and of all sensing, channel and computation noises.
- **(H6)** Given the policy paths, the stacked state Y (world, errors, carried sensing noises; lib.py:381-467) satisfies Y_{t+1} = A_θ(z_t)Y_t + ξ_t with ξ_t ~ N(0, N_θ(z_t)) independent of the past, and A_θ, N_θ continuous.
  - Uniform exponential stability: ‖A(z_{t+k−1})⋯A(z_t)‖ ≤ C₂λᵏ with λ < 1.
  - Every prior error contains a fresh private term of variance at least σ_min > 0.

**Verification for I\*** (proved; the algebra is re-verified symbolically in check A, which passes):

- **(H1)** The Riccati map is a Möbius map with positive coefficients:
  - g = (c₁p + c₀)/(d₁p + d₀), where Q′ = Q + q_c and K₁ = F²q_c + Q′;
  - c₁ = F² + bK₁ and c₀ = Q′(1 + bq_c);
  - d₁ = aF² + b + abK₁ and d₀ = (1 + aQ′)(1 + bq_c).
  - g is increasing in p and decreasing in (a,b). So [0, b_U]ⁿ is invariant for any b_U at least the largest own-sensor-only fixed point; p_hi(θ*) = 0.141304.
- **(H2)** c₁d₀ − c₀d₁ = F²(1+bq_c)². Hence g′(p) = F²(1+bq_c)²/(d₁p+d₀)² ≤ F²/(1+aQ′)² ≤ ρ̄ = (F/(1+Q′/R))² for all p ≥ 0.
  - So C₁ = 1 and ρ̄(θ*) = 0.734554.
  - The bound needs F < 1 and an own sensor read every round (a ≥ 1/R).
- **(H3)** The ingredients are all analytic in (θ, p): the EFE, the soft-min, the logistic and Gibbs weights, and the (P4) stationary law. The (P4) law is analytic because Cramer's rule applies to the system Tᵀ − I with one row replaced by 1ᵀ, which is nonsingular for an irreducible chain.
- **(H4)** γ < ∞ and full-support habits make every weight positive.
  - T-fast: 𝒮 = 𝒫 and m = 1.
  - T-real: 𝒮(π) = {profiles within one flip} × {all attention sets}, and m = n.
  - κ₀ is positive but of order exp(−γ·gap), so the theorem is qualitative at γ = 400.
- **(H5)** The EFE depends on beliefs only through covariances (lib.py:62-97), and ψ is constant.
- **(H6)** The closed loop is rank one: M = A_F(I − KH) = A_F(I + P⁻D)⁻¹ = uvᵀ with u = (F,1)ᵀ.
  - The scalar closed-loop factor is λ = vᵀu = F(1+bq_c)/(d₁p+d₀) ≤ λ̄ = F/(1+Q′/R). λ̄ = 0.857 at θ*, and 0.808 on the invariant interval. Also λ² = g′.
  - Products are M_{t+k−1}⋯M_t = u(∏λ_j)v_tᵀ.
  - The stacked A is block lower-triangular: A_F with ‖A_Fᵏ‖ = F^{k−1}√(1+F²); the rank-one error blocks; and zero blocks for the carried noises.
  - So uniform exponential stability holds with any λ ∈ (F, 1).
  - σ_min = q_c, because the computation noise ξ_i(t−1) enters only m⁻_{i,0}(t) (lib.py:374).

**The nulls and the medium** satisfy the same hypotheses:
- N_hab: γ = 0, so L = 0.
- N_pr: uniform partners.
- N_lp and N_fr: dead relays with claimed covariances kept. The Riccati maps and M are unchanged, and η_{t−1} enters the errors only as an input.
- Medium: 256 profiles.

## 4. Theorem 1 (stationary policy–covariance law)

**Statement.** Assume (H1)–(H4) on a compact U. Use the metric d(z,z′) = min(1,|p−p′|_∞) + 1{π≠π′} on X_U = 𝒦_U × 𝒫. For θ ∈ U there is a unique invariant law μ_θ, and:
- **(a)** W_d(δ_z P_θᵗ, μ_θ) ≤ C₃βᵗ for every z, with C₃ and β < 1 uniform on U;
- **(b)** W_d(μ_θ, μ_θ′) ≤ (C₃+M)ω + Mω ln(1/ω)/ln(1/β), where ω = sup_z W_d(δ_zP_θ, δ_zP_θ′) and M = max{2, C₁(1+2Lρ/(1−ρ))}; in I*, ω = O(|θ−θ′|);
- **(c)** the stationary two-sided path laws are weakly continuous in θ.

**Proof.** (proved)

**0. Feller.** X_U is compact. P_θf(z) = Σ_{π′} k_θ(G_θ(p,π),π;π′) f(G_θ(p,π),π′) is continuous in z.

**1. Synchronous phase.** Start two copies with equal policies, and couple the next policies by maximal coupling at every step.
- While the policies agree, |p_t − p′_t| ≤ C₁ρᵗδ, where δ = |p₀ − p′₀|.
- Given agreement so far, the probability that the policies split at step t is TV(k(p_t,π;·), k(p′_t,π;·)) ≤ min{1−κ₀, LC₁ρᵗδ}. The first bound holds because the two laws share the support 𝒮(π) with mass at least κ₀ on it.
- Hence P(the policies never split) ≥ q(δ) = ∏_{t≥1} max{κ₀, 1−LC₁ρᵗδ}.
- q(D) > 0 for D = diam 𝒦_U: finitely many factors are at least κ₀, and the remaining product converges.
- Also 1 − q(δ) ≤ LC₁ρδ/(1−ρ).

**2. Meeting phase.** By (H4), P_z(π_m = π★) ≥ κ₀ᵐ for every z. With independent moves, both copies are at π★ after m steps with probability at least κ₀^{2m}.

**3. Coupling time.** Alternate a meeting phase with a synchronous phase, restarting after a split.
- Each cycle succeeds with probability at least p* = κ₀^{2m}q(D), whatever happened before.
- A failed cycle has length m + S, with P(S > j, fail) ≤ C′ρʲ.
- So for small s > 0, E[e^{s·length}; fail] ≤ r < 1, and the start τ of the successful cycle satisfies P(τ > t) ≤ e^{−st}/(1−r).

**4. Contraction.** E d(Z_t, Z′_t) ≤ 2P(τ+m > t/2) + C₁Dρ^{t/2} ≤ C₃βᵗ for all z, z′.

**5. Existence and uniqueness.**
- (δ_zP^t)_t is Cauchy in W_d. Its limit is invariant because P_θ is Feller.
- Two invariant laws satisfy W(μ,ν) = W(μPᵗ,νPᵗ) ≤ C₃βᵗ → 0.

**6. Lipschitz in the initial law.**
- If π = π′: E d(Z_t,Z′_t) ≤ C₁|p−p′| + 2LC₁ρ|p−p′|/(1−ρ).
- If π ≠ π′: d ≥ 1, so W ≤ 2 ≤ 2d.
- Hence W(νPᵗ, ν′Pᵗ) ≤ M W(ν,ν′) for every t.

**7. Continuity in θ.** Telescope:

W(μ_θ, μ_θ′) ≤ W(μ_θP_θᵀ, μ_θ′P_θᵀ) + Σ_{s<T} W(μ_θ′P_θ′^s P_θ P_θ^{T−1−s}, μ_θ′P_θ′^{s+1} P_θ^{T−1−s}) ≤ C₃β^T + TMω.

Choose T = ⌈ln(1/ω)/ln(1/β)⌉. Also ω → 0 as θ′ → θ by uniform continuity on compact sets, and ω is Lipschitz in θ because the maps are analytic.

**8. Path laws.** The finite-dimensional laws μ_θ ⊗ P_θ^{⊗k} converge weakly by induction, using Feller kernels with sup_z W(δ_zP_θ, δ_zP_θ′) → 0. On the compact path space this gives weak convergence of the path laws. ∎

**Remark on why contraction is essential (interpretive).** Given the policy, the covariance moves deterministically, so P_θ(z,·) has at most |𝒫| atoms. A total-variation Doeblin minorization of the joint chain that is uniform in z is therefore not available in general. The proof uses Doeblin only for the finite policy component, and contraction for the covariance.

**Relation to prior art.** Barnsley–Demko–Elton–Geronimo, Ann. IHP Probab. Stat. 24(3):367–394 (1988), with erratum 25(4):589–590 (1989); I read the abstract and the statement of Theorem 2.1.
- It covers T-fast. The maps (p,π) ↦ (G(p,π),π′) contract d_λ = λ|p−p′| + 1{π≠π′} for λ < 1/diam 𝒦, and the probabilities are Lipschitz and at least κ₀.
- It does not cover T-real, whose one-step probabilities vanish off 𝒮(π).
- It gives no continuity in parameters.

## 5. Theorem 2 (world-conditional second moment)

**Statement.** Under (H1)–(H6):
- The joint stationary law of (world, chain, errors) exists and is unique, with finite second moments.
- Σ^c(θ) := E[Cov(e(t)|η)] = ½E[(e^a−e^b)(e^a−e^b)ᵀ], where e^a and e^b are two replicas that share η and are conditionally i.i.d. given η.
- Σ^c is continuous on U, satisfies Σ^c ⪰ σ_min I, and so Π^c = (Σ^c)⁻¹ is continuous.
- Σ^c is invariant under every relabeling of agents that leaves the kernels and the noise law invariant.

**Proof.** (proved)
- **Stationary solution.** Given the stationary policy paths, Y_t = Σ_{k≥0} Φ_{t,k}ξ_{t−1−k} converges in L² by (H6) and is the unique stationary solution: the homogeneous part Φ_{t,k}Y_{t−k} → 0.
- **Two-replica identity.** By (H5) the pairs (π^a, private noises a) and (π^b, private noises b) are independent of each other and of η. So e^a and e^b are conditionally i.i.d. given η, which gives the identity.
- **Representation.** Σ^c = E_{𝐏_θ⊗𝐏_θ}[Ψ_θ], with Ψ_θ = ½ J (Σ_k Φ_kN_{t−1−k}Φ_kᵀ) Jᵀ and J selecting e^a − e^b.
- **Continuity.** The k-th term of Ψ_θ is continuous in θ and finitely many coordinates, and is bounded by const·λ^{2k} uniformly on U. So Ψ is jointly continuous and bounded. Then |Σ^c(θ_j) − Σ^c(θ)| ≤ sup|Ψ_{θ_j} − Ψ_θ| + |E_{θ_j}Ψ_θ − E_θΨ_θ| → 0 by Theorem 1(c).
- **Lower bound.** Total covariance plus the fresh private term gives Σ^c ⪰ σ_min I.
- **Symmetry.** Uniqueness gives τ_*μ_θ = μ_θ for every invariance τ. ∎

## 6. Theorem 3 (I*: selection functionals and the open-subset clause)

**Lemma 3.1** (proved). For every finite γ and both protocols, Σ^c = blockdiag(Σ_A, Σ_A) with Σ_A = α(θ)I₄ + β(θ)11ᵀ exactly, and α ≥ q_c.
- The niches have independent world components, noises and policy chains (other-niche channels carry zero gain), so the cross-niche block is zero.
- S₄ acting within each niche and the niche swap are invariances of the model; by Theorem 2 and the commutant of S₄, Σ_A has the stated form.
- So the compound projection used in round 2 (lib.compound) is exact in the population limit.

**Contrast formulas** (C1, proved). Write x = β/α. For x > 0:
- a/ε = x and cross couplings are zero;
- r(A) = 1 + 4x;
- a k-subset of A has r = (1+kx)/(1+(4−k)x), which is 1 for k = 2 and (1+3x)/(1+x) for k = 3;
- every region meeting both niches has r ≤ 1, because f = (1/k on C∩A, −1/l on C∩B) is orthogonal to 1_C with L_Cf = 0, so ξ_in ≤ ε ≤ ξ_out;
- mean-coupling baseline: ā = 3a/7 with uniform leak, so r̄_hom = 1 + (24/7)x;
- mechanism medium: by the same lemma (n = 8), r_M = 1 + 8x_M;
- nulls: x_hab, x_pr and x_lp each come from their own exactly compound-symmetric Σ^c;
- N_fr: x_fr ≡ 0 under T-fast (proved: the members' policy chains and errors are independent given η). Under T-real, x_fr is a mixture term from the shared reviser clock (numerical, ≈ 0).

**Statement.**
- **(a)** x, x_M, x_hab, x_pr, x_lp and x_fr are continuous on Θ (Theorem 2). Hence r(A), r_M, r̄_hom and every null's maximal region contrast are continuous.
- **(b)** U_mech = {x > 2x_M > 0, (1+3x)/(1+x) < 1+8x_M, 0 < x_ν < 2x_M for ν ∈ {hab, pr, lp}, plus 1+4x_fr < 1+8x_M} is open. Here the x_fr condition holds identically under T-fast.
  - For θ ∈ U_mech and every r0 ∈ (1+8x_M, 1+4x], the collectives at level r0 are exactly A and B, and every D-null has none. So the selected partitions differ.
  - For N_fr under T-real this uses R5 if x_fr < 0.
  - U_{3.5} = U_mech ∩ {1+8x_M < 3.5 < 1+4x} is open.
  - Mean-coupling reading: U_mc = {x > 0, x_ν < (6/7)x} is open; that window is nonempty whenever x > 0.
- **(c)** θ* belongs to all three sets (numerical; round-2 values):

| Protocol | x | 2x_M | max null x | (1+3x)/(1+x) | 1+8x_M | Margins |
|---|---|---|---|---|---|---|
| T-fast | 0.8478 | 0.4847 | 0.2174 (N_pr) | 1.918 | 2.939 | r(A)−r_M 1.453 (264 SE); r_M−N_pr 1.069; 3.5−r_M 0.561 |
| T-real | 0.858 | 0.485 | 0.2215 (N_pr) | 1.924 | 2.942 | 1.490 (143 SE); 1.056 (140 SE); 0.558 (77 SE) |

**Proof.** (a) follows from Theorem 2 and the formulas. (b): a finite intersection of strict inequalities between continuous functions is open. ∎

**Consistency.** The round-2 box results are consistent with this: 17/17 points at ±1%, and r0 = 3.5 admissible at 15/17 points at ±5%. So U_{3.5} contains the ±1% box but not all of the ±5% box.

## 7. Proposition 4 (agency index)

**Statement** (proved). Fix:
- finitely many decision states X ∈ 𝒦, declared as numbers, with weights;
- the protocol's decision law P_θ(·|X), which under T-fast is the (P4) law at X, with or without the attention component;
- a class with habits fixed at E and γ_C ∈ [0,∞), with G_C(θ,X) continuous and nonconstant. This includes G1 and G2 of round 2, where G_C = −½ln(1+|σ|v_C/R_s) + ψ|σ|.

If the denominator Σ w_X KL(P_θ*(·|X)‖E) > 0, then Agency(θ) is continuous at θ*.

**Proof.**
- P_θ(·|X) is analytic in θ and has full support.
- KL(P‖P_{γ_C}) ≥ P(σ_off)(γ_CΔ − ln(E(σ_off)/E(σ_min))) − ln|𝒫|, where σ_off is a profile outside argmin G_C and Δ > 0 is the gap. So KL is coercive in γ_C, uniformly near θ*.
- The infimum is therefore taken over a compact interval [0, Γ] and is continuous; the denominator is continuous and positive. ∎

**At θ\*** (T-fast, X* = 0.09163): the denominator is 0.1237 and the G2 index is 1 − 1e−10 (agency_out.txt). So the index stays above 0.99 on a neighborhood: continuity proved, value computed.

**Not covered (open).**
- Decision states declared as θ-dependent quantiles, such as "the median p" (run_box.py:107-114). This needs a continuous, strictly increasing stationary distribution function at the median.
- T-real coarse events such as "a deliberation round at a symmetric covariance state", computed as ptp < 1e−12 (run_box.py:69). Conditioning on an event E is weakly continuous only if μ_θ(∂E) = 0, which is not established. The exact symmetric set is closed with empty interior.

## 8. Limits, failed routes, I** checklist

**γ = ∞ (computed).**
- At p*(1) = 0.095508 under T-real best response, the owner of the single open slot gains 0.02447 > ψ from keeping it, and a closed member gains 0.02332 < ψ from opening (explore_efe_out.txt). So the four one-slot profiles are absorbing.
- Check B2: 0/50 couplings and 0 slot changes, so μ is not unique. At γ = 400 the same starting states couple 100/100.
- The modulus in Theorem 1 degenerates as γ → ∞, since κ₀ ~ e^{−γ·gap}.

**Bougerol 1993: not applicable as stated** (singular A_F, feedback parameters), as explained in Section 1.

**I\*\* checklist** (Theorems 1–4 transfer if these hold):
1. The own sensor is read every round, and the member state is (η_t, η_{t−1}) under A_F with observation rows [1,0] or [0,1]. Then (H2) holds with ρ̄ = (F/(1+Q′/R))². Otherwise, q_c > 0 plus the Riccati difference identity P_{t+1}−P′_{t+1} = A(I−KH)(P_t−P′_t)(I−K′H)ᵀAᵀ plus the Lyapunov bound Aᵀ(AP⁺Aᵀ+Q̃)⁻¹A ⪯ ν/(1+ν)·(P⁺)⁻¹ give a k-step contraction of the form in (H2), with C₁ρ^k.
2. Gibbs kernels at finite γ with full-support habits, data-independent pragmatic terms, and a support 𝒮(π) that does not depend on the covariance.
3. q_c > 0 in every prior error.
4. Permutation-equivariant kernels within each niche. Then Σ^c is exactly compound symmetric by uniqueness even when realizations are not exchangeable, as with private slots.
5. Channel noises shared by several receivers are conditioned on, per def:col-world-conditional.

## 9. Numerical checks (all single-threaded, sequential, each under 70 s)

| Check | Declared expectation | Result | Label |
|---|---|---|---|
| A (check_a_algebra.py → check_a_out.txt) | Möbius form; determinant; rank-one M; λ² = g′; closed form matches lib.posterior to 1e−12 | All PASS: max relative error 8e−15; sup g′ = 0.734554 = ρ̄; sup λ = 0.857061 | computed |
| A, negative controls | X1: perturbed formula must disagree. X2: F = 1.2 with no structural sensor must exceed 1 | Both fail as expected: X1 error 0.26; X2 sup g′ = 1.44 | computed |
| B0 (check_b_coupling.py → check_b_out.txt) | sim_core (sim_core.py) agrees with lib within 4 SE | PASS, \|z\| ≤ 0.70 | numerical |
| B1 | ≥ 99% coupled from extreme starts; post-coupling ratio ≤ ρ̄ | PASS: 200/200 (T-fast) and 200/200 (T-real); median τ 4 and 10; max ratio 0.443 | numerical |
| B2 (negative control) | γ = ∞: 0/50 couple | Fails as expected: 0/50, 0 slot changes | computed |
| B2+ | γ = 400 from the same starts couples | PASS: 100/100 | numerical |
| C (check_c_continuity.py → check_c_out.txt) | C0: r(A) = 4.391 ± 0.04. C1–C3: CRN slope and SE criteria | C0 PASS (4.3822 ± 0.0088). C1–C3 FAIL as declared, and the negative control was UNEXPECTED (SE ratio 18 < 20). The criteria were ill-posed: CRN differences come from rare policy flips, so the SE scales like √h while the signal scales like h. | numerical |
| C2 (check_c2_linear_response.py → check_c2_out.txt; new seed; declared before running) | ψ: L1, L2, L3 | PASS: z = −0.47 and −0.25; SE factors 2.22 and 4.02; \|Δr(1e−4)\| = 6.8e−4 | numerical |
| C2, negative control | Independent streams must not shrink | Fails as expected: SE factor 0.88 | numerical |
| C2, direction R_c | L1 and L3 | L1 FAIL (z = +76 at h = 1e−4); L3 PASS (5.2e−5) | numerical |
| C3 (check_c3_fixed_policy.py → check_c3_out.txt) | Fixed-path slope constant across h, and equal to −0.5241 | F1 and F2 PASS (−0.52329, −0.52404, −0.52412). The R_c L1 failure is explained: no policy flip occurred among the 32 pairs at h = 1e−4. It is not a jump. | numerical |
| C3, negative control | Holding the gains fixed should change the slope by more than 5% | UNEXPECTED: only 2.1%, so this control does not discriminate | numerical |

**What check C shows:** no jump in r(A) larger than 3e−3 within relative 1e−4 in ψ or R_c. It is an illustration only; the theorem does not rest on it.

## 10. Bottom line

**Strongest supported result.** Theorems 1–3 and Proposition 4 (proved):
- the stationary policy–covariance law of I* is unique and depends continuously on θ;
- Σ^c, r(A), the baselines and the null contrasts are continuous;
- the differ clause holds on the open sets U_mech, U_{3.5} and U_mc.

**Scope.** I*, its mechanism medium and its nulls, both protocols, 0 ≤ γ < ∞. The same proof covers any I** that passes the checklist in Section 8.

**Minimal unresolved obligations.**
- θ* ∈ U is numerical: Monte Carlo with margins of 77 SE or more, confirmed by two independent codes. A proof would need rigorous enclosures of x, x_M and x_ν at θ*.
- Under T-real the N_fr verdict depends on R5.
- Agency continuity is open for quantile or event-type decision states.

**Next action.** Have the coordinator record O6 as proved conditional on the numerical center values. Declare agency decision states as fixed points. Run the Section 8 checklist on I** once it is declared.


## round3: proof-check

O3 proof-check (fresh context) of C3a, C3b, C3c, C4, C5 and C12 for open_agy_meta_agent_exists. Every step was rebuilt from the claim statements and the finished arguments.

**Verdicts**
- **C4 (Lemma Z): correct as stated.** Proved. The hypothesis of nonnegative row sums is never used, so Z1 to Z4 hold for every positive definite Z-matrix. C3a's phrase "not a Z-matrix" and C5(b) both need this stronger form, and the given proof already covers it.
- **C3a: correct as stated, with one wording repair.** Proved. The parenthetical "no agent of one reads an agent of the other, private noise block diagonal" is weaker than what the proof uses. The proof needs disjoint ancestries: no reads between the two ancestries, directly or through chains, and no common ancestor. With one common source, the contracted covariance is positive in 105/200 computed draws.
- **C3b: correct as stated, within setting P.** Proved and computed. One side remark in the finished argument is refuted: "computation noise on predictions changes only diag(V), so the rule is unchanged". A corrected statement is given below.
- **C3c: correct with a scope repair.** The result holds for the world-conditional precision of the coordinates of U (the actors and their ancestors). It does not hold for the precision of a population with an agent outside U that reads members of U, which C3a's hypotheses allow. Computed counterexample below.
- **C5: correct with a wording repair.** Parts (a), (b), (d), (e) and F-share are correct when G≥0. The F-share clause must state G≥0, or one-signed source columns, itself; the record attaches G≥0 only to the clause before it, and with mixed signs the clause is false (exact counterexample). Separately, Theorem F(c)'s "iff" (not in the record statement) needs every factor to be loaded by some agent (computed counterexample).
- **C12: correct with a repair.** The index bound is proved. The second part, KL_{s|a} ≤ Σ ln|A_i| and the condition derived from it, is false for non-uniform slot habits (counterexample below). Repaired bound: KL_{s|a} ≤ Σ_i max_{s_i} ln(1/E^s_i(s_i)). I* declares uniform product habits (C11), so C12's use there is unaffected.

**Definitions used**
- diffusive: 04_collectives.tex:147-151
- def:col-world-conditional: 04_collectives.tex:130-132
- def:col-contrast, including that it requires a diffusive Π^c of the whole population: 04_collectives.tex:182-188
- def:col-collective: 04_collectives.tex:214-221
- def:agy-group-model: 05_agency.tex:156-169
- def:agy-agency-index: 05_agency.tex:240-246, with the remark at :249-251
- tab:agy-nulls, N_eff row: 05_agency.tex:348
- def:agy-order-parameter, private inputs: 05_agency.tex:296-302
- def:fw-system: 02_framework.tex:11-17
- def:fw-level0: 02_framework.tex:313-328
- def:agy-joint-acts: s05_agency.tex:146-152; eq:agy-act-efe: s05_agency.tex:156-158; thm:agy-joint-acts(b): s05_agency.tex:169-173

**C4: step check**
- Write Π = sI − B with s = max Π_ii > 0. B ≥ 0 uses only the sign of the off-diagonal entries.
- Since B is symmetric and nonnegative, ρ(B) = λ_max(B) = s − λ_min(Π) < s. The Neumann series Σ = Σ_k B^k/s^{k+1} then gives Z1, and Z2 follows because walks in the graph of B join exactly the vertices of one component.
- Z4: Σ_SS^{-1} = Π_SS − Π_SR Π_RR^{-1} Π_RS. Here Π_RR^{-1} ≥ 0 by Z1 for a positive definite Z-matrix, and Π_SR ≤ 0.
- Z3: by the 3×3 cofactor, (Σ_SS^{-1})_ik = (Σ_ij Σ_jk − Σ_ik Σ_jj)/det, with det > 0.
- Numerical:
  - 300 positive definite diffusive draws, 1 to 3 components: 0 violations.
  - 300 positive definite Z-matrices, each with a negative row sum: 0 violations.
  - Negative controls: one positive off-diagonal entry makes Z4 (S=V) fail 300/300 and Z1 or Z3 fail 286/300; Wishart covariances violate Z3 300/300.

**C3a: step check**
1. Reduction. Write x = x̃ + x^η, where x^η is a stable causal function of η. Then ỹ_t := η_{t+1} − Fη_t − Bx^η_t = Bx̃_t + ω_t, and closed-loop stability gives σ(η) = σ(ỹ). Hence Σ^c = Cov(x̃_0 | ỹ_Z).
2. With B = e bᵀ, ỹ reaches x̃ only through bᵀx̃_t plus noise of variance q = 1/(eᵀQ_w^{-1}e).
3. The two-sided smoother's error spectral density is (J + bbᵀ/q)^{-1}, by Woodbury, with S_z ≥ q > 0.
4. J is block diagonal, so the contracted integrand is −β1β2/(q+Σβ_k), which is negative at every frequency because J_k^{-1} ≻ 0.
5. With one-signed b, some Σ^c_ij < 0. Σ^c ≻ 0, so Π^c is not a Z-matrix.
6. Lemma C3-b checks: Cov(ỹ_W | x̃_0) is block diagonal because ω_0 is independent of everything else; the remainder is PSD; take the monotone limit.
- How each hypothesis is used: Q≻0 defines J (it could be relaxed to bᵀS_k b ≢ 0); block-diagonal A and Q in step 4; ω independent of ξ in C3-b; stability for stationarity and the reduction; rank-one B in step 3; one sign and contrast coordinates in step 5. Lemma C3-a contributes only the symbol J.
- Side note on the report's mirror-group corollary (not part of the record statement): "<0" needs fᵀJ^{-1}b ≢ 0.
- Numerical, by an independent method: Lyapunov plus exact conditioning on a ±110 window, with sensing feedback included; window converged to 1.6e-12.
  - Σ^c equals the spectral formula to 9.2e-14 over 60 draws.
  - The contracted formula matches to 3.9e-13 and is negative in 60/60.
  - A negative cross entry occurs in 60/60.
  - λ_min of the C3-b remainder is ≥ −2.8e-13 relative.
  - With a 2-d world and correlated Q_w, the result matches to 3.0e-14.
- Negative controls:
  - Filtering (conditioning on η up to time 0) breaks the C3-b bound in 60/60.
  - Using q' = eᵀQ_w e instead mismatches (error ≥ 9.2e-3).
  - A common source gives a positive contracted covariance in 105/200.
  - Opposite-sign actors give a diffusive Π^c in 83/100.

**C3b: step check**
- Cov(ζ) = αI + βJ, so the collective and disagreement modes decouple, and the disagreement modes never enter η.
- The finished argument says "z1+, z2+ independent AR(1) a priori". That is literally false, since both are driven by η. Replacing them by their η-free parts, via Prop P step 1 or C3a's reduction, closes the gap.
- The posterior cross-spectrum −κ1κ2 S_X S_Y / (κ1²S_X + κ2²S_Y + Q) has one sign. Since z_k(t) = φ_k z_k+(t−1), sign(Π^c_ij) = sign(φ1κ1φ2κ2), with Π^c_ij = (V^{-1})_12/√(n1n2).
- Corollary algebra checked with sympy: g_k = c_k a_k/(b̂_k(1+n_k c_k)) and φ_kκ_k = (b/b̂_k)a_k²c_k√n_k/(1+n_k c_k)².
- Interpretive scope: the corollary uses continuous Gaussian habits, while def:agy-joint-acts has finite act sets (s05_agency.tex:147).
- Numerical (direct conditioning):
  - Sign rule agrees in 150/150 draws with random signs.
  - Cross entries match (V^{-1})_12/√(n1n2) to 5.4e-13·max|Π^c|.
  - Corollary cross entries are positive in 100/100.
  - Controls: the naive rule sign(κ1κ2) is wrong in 75/150; a misjudged effect sign gives negative cross entries in 100/100.
- Refuted remark (computed). Reading: prediction noise ε_i ~ N(0, σε²) is added to m_i(t+1) and propagates into the act. Then V_12 changes in 300/300 draws and the rule fails in 57/300, all with φ1φ2 < 0.
- Corrected formula, matching direct computation to 5.9e-13:
  V_12 = −κ1κ2 (1/2π) ∫ |h1h2|² Re[(c0,1σε² + φ1 s1 e^{−iω})(c0,2σε² + φ2 s2 e^{iω})] / S_o dω,
  where h_k = (1 − ρ_k e^{−iω})^{-1}, ρ_k = c0,k φ_k, s_k = (K_s + (n_k−1)K_c)²R + (n_k−1)K_c²R_c, and S_o = Σ_k κ_k²|h_k|²(c0,k²σε² + s_k) + Q.
- Proved repair: if c0,k > 0 and φ1φ2 > 0, the weight |h1h2|²/S_o is monotone on [0, π], so the rule survives prediction noise.
- Consequence for the corollary: with a1a2 > 0, 0/150 sign flips. With a1a2 < 0, cross entries turn negative in 112/150, and Π^c is diffusive in 7/400 draws with both firms active. Example: n=(2,2), a=(−0.608, 0.708), σε²=0.865; cross entry −1.27e-4, smallest row sum 0.803; without noise the cross entry is +9.99e-3.

**C3c: step check**
- J^{-1}b = Φω and Σ_0 leaves span Φ invariant. Hence Σ^c = Φ(diag σ − C)Φᵀ ⊕ (a part on the complement that is block diagonal over groups), and diag σ − C is an irreducible positive definite Z-matrix.
- Marginalizing to any coordinate set that contains supp b leaves the cross blocks unchanged (proved via Σ_0 b̂_k = σ_k b̂_k; computed 2.5e-14).
- Numerical, 40 eigen-loading draws: σ2/σ1 ≤ 2.0e-13; blocks equal κ b̂ b̂ᵀ to 2.8e-13, with κ from the spectral formula; positive in 120/120.
- Controls:
  - Generic loadings: rank two in 200/200.
  - A non-acting agent reading one member of each group: the population cross block is rank two in 100/100, with a negative entry in 16/100.
  - A listener to one group only: the block stays rank one, but its left factor deviates from b̂_1 (1 − |cos| up to 8.4e-2).
- Repair: state C3c for the marginal precision of U's coordinates, or require that no agent outside U reads an agent of U.

**C5: step check**
- Numerical checks:
  - (a): Woodbury formulas exact to 1.8e-14.
  - (b): uses Z1 for K^{-1}, a positive definite Z-matrix whose row sums may be negative (the stronger C4); 0/300 violations.
  - (d): identity holds to 4.4e-16; indicator loadings with diffusive V^{-1} give 0/300 failures.
  - (e): the leak formula holds; CE1 leak = −0.0377; CE2 reproduced exactly.
  - F-share with G≥0: 0/712 non-transitive draws diffusive.
- Mixed-sign counterexample to the F-share clause:
  - G rows (1,1,0), (1,−1,1), (0,0,1), with D = I and V = I.
  - Σ = [[3,0,0],[0,4,1],[0,1,2]] and Π = (1/3) ⊕ (1/7)[[2,−1],[−1,4]], which is diffusive.
  - Sharing is non-transitive: agents 1 and 2 share {a,b}, agents 2 and 3 share {c}, agents 1 and 3 share nothing.
- Theorem F(c) counterexample:
  - V = [[1,.5,.6],[.5,1,0],[.6,0,1]], so (V^{-1})_23 = 0.769 > 0 and V^{-1} is not Z.
  - Agents load only on factors 1 and 2.
  - The largest off-diagonal entry of Π over scales 1e-3 to 1e3 is −1.3e-7, so off-diagonals stay nonpositive.
  - Repair: replace V by the covariance of the loaded factors.
- Raw-data application: it needs one-signed source columns. This holds when every c0,i > 0 (for example Kalman gains), for either sign of F. With overshooting gains it is unchecked.

**C12: step check**
- Every model factorizes as P_g = E^a ⊗ P^s_g. By the chain rule, KL(P‖P_g) ≥ KL_a, while KL(P‖E) = KL_a + KL_{s|a}. The weighted version over decision states follows term by term.
- Exclude the case where the denominator is 0: the index is then 1 by definition and the bound is undefined.
- Numerical: 0/200 violations; the numerical infimum equals KL_a + I(a;s) to 5.3e-15; weighted version 0/100; the second part with uniform slot habits 0/200.
- Control: allowing attention tilts exceeds the bound in 82/200.
- Counterexample to the second part:
  - Attention: habit uniform over 3 options, actual law (0.8, 0.1, 0.1).
  - Slots: E^s = (1−1e-4, 1e-4), actual law (1e-4, 1−1e-4).
  - KL_a = 0.460 and KL_{s|a} = 9.208, so the index is 0.9525 ≥ 0.9, yet ln 2 < 0.9/0.1 × 0.460 = 4.14.

**Readings adopted, and whether a verdict depends on them**
- (R1) The conditioning set of the world-conditional law follows 04_collectives.tex:131 and the record's conventions: sensing noise (even when relayed) and receiver-specific channel noise are not conditioned on. The C3a and C3b verdicts and the C5 application depend on this.
- (R2) A non-diffusive Π^c means no collective (04:183, 04:215). C3a's "no collective, no meta-agent" depends on this; its covariance statements do not.
- (R3) In C3c, "Π^c" is the precision of U's coordinates; under the population reading the claim is wrong without the repair.
- (R4) Prediction noise propagates into m+ and the act. The refutation of the remark depends on this.
- (R5) Continuous Gaussian habits in the C3b corollary (interpretive).
- (R6) Every model in C12's class has habits E^a ⊗ E^s. The second part's verdict depends on whether the slot habits are uniform.

**Files**
All runs used bare python, single thread, each under 2 seconds. Every script and its *_out.txt are in C:/Users/CHRISA~1/AppData/Local/Temp/claude/63c81c17e87f0010/34faeca5-ea90-45d1-8cc4-412bdf898c58/scratchpad/metaagent/round3/proofcheck-o3/. The scripts are c4_lemma_z.py, c5_factor.py, c3a_collider.py, c3a_vector_world.py, c3c_eigen.py, c3c_listener_one_group.py, c3b_sign.py, c3b_s1_precision.py, c3b_noise_formula.py, c3b_efe_noise.py, c3b_efe_noise_diffusive.py and c3b_efe_noise_diffusive2.py. No repository or vault file was edited.

**Where this leaves O3**
- Strongest supported result: all six claims hold in their stated scopes. The defects are wording and scope, plus one refuted side remark.
- None of the defects reaches a recorded verdict:
  - C10 (I3) and R1 use only C3a's negative covariance.
  - C11 uses C12 only through the index bound under uniform habits.
  - I found no recorded result that relies on the prediction-noise remark.
- Still unresolved: C6 and C10 remain unchecked for O3. There is no sign criterion for the prediction-noise case with φ1φ2 < 0 beyond the integral formula (open). The F-share application with overshooting gains is unchecked.
- Next action: put the five repairs into the record (C3a parenthetical, C3c scope, C5 G≥0 and F(c) condition, C3b remark, C12 slot-habit bound), mark these six claims as fresh-context checked, then run the same check on C6 and C10.

## round3: literature

## Verdict

No source settles the author's reading decisions. The literature and the manuscript's own usage lean the same way on two of them:

- **(a) Slot as act.** Opening a public slot that others read is an act (interpretive). The table's mechanism-relative typing of N_eff and N_inf is the standard null-model logic.
- **(e) What "joint policies" means.** The as-if, group-agency and active-inference group-model literature evaluates the group's outputs at its boundary. On that reading the index's "joint policies" are slot/act policies, and internal attention is excluded. This is interpretive: the active-inference literature does count attention as covert action at the member level.
- **(f) Frozen-state deliberation.** It is a two-time-scale idealization that def:agy-group-model itself adopts. No source gives a Gibbs or group-posterior law when the decision state moves on the deliberation time scale.

Under every reading combination except one, I* settles the open problem with r0 = 3.5 > 1 and Agency0 > 0. The exception is "N_eff/N_inf are type D for every collective whose members act", and the literature does not support it as methodology.

On novelty:
- The agency index has close prior art that the manuscript does not cite: maximum entropy goal-directedness (MEG, 2024), the KL-based R², and Schneidman's I2/IN.
- C12 is an elementary chain-rule corollary. I found no prior statement of it; the dilution it describes has a precedent in Nagelkerke 1991.
- Community formation by EFE- or Bayes-selected attention is prior art.
- No source exhibits a population meeting all clauses of def:agy-meta-agent.

## Readings, evidence and grade frontier

Frontier values below are from the record (C11, C12 and the attack, open_agy_meta_agent_exists.md:146-162, reports.md:1229-1323). They were not recomputed here.

| Reading combination | Agency0 frontier for I* | Status |
|---|---|---|
| (a) conditional typing or slot not an act; (e) slot-only; (f) (P4) frozen | 0.99 (index 1−1e-10 at the symmetric state) | computed (record) |
| same, (f) real time | 0.90 with the coarse decision state (G2 0.971–0.974). Finer declarations give G2 0.69 (median p-bin), 0.29 (median p and count 2), 0.10–0.11 (three p-bins) | computed (record); positive in every declaration explored |
| (e) full policies, any (f) | ≤ C12 bound 0.14/16.77 ≈ 0.0083; computed 0.0078 (G2), 0.0080 (G1) | computed (record) |
| (a) strict (D whenever members act) | none: N_eff gives 4.41 and N_inf 6.27, both above the window's lower edge, so the differ clause fails | computed (record) |

### (a) Is slot opening an act, and how are N_eff and N_inf typed?

**Act status (interpretive).** The literature supports treating slot opening as an act:
- Kirsh–Maglio: epistemic actions are physical actions that change the agent's input by modifying the world.
- Constant et al. 2018: niche construction is any modification of niche states "that they and others inhabit".
- Heylighen 2016: a trace of an action left on a medium that stimulates later actions is stigmergy. Opening a channel that niche-mates read is such a trace, i.e. communication through acts.

The manuscript's own usage points the same way:
- s07_formation.tex:123 and ext2_rfm.tex:139 call models whose only EFE-selected component is attention models with "no acts".
- ext2_rfm.tex:139 also declares the agency index inapplicable in such a model; ext2_rfm.tex:167 asks for "acts and decision states so that the agency index, N_eff and N_inf apply".
- So the index presupposes acts. Its objects are slot-opening policies (05_agency.tex:157), so the branch of C11 reading (v) "slot opening is not an act" sits uneasily with the index being applicable at all.

**Caveat (interpretive).** def:fw-system lists channel states separately from η (02_framework.tex:13), and a^e enters η's dynamics (02_framework.tex:15). If the slot is a channel state rather than part of η, N_eff ("each act's effect on η", 05_agency.tex:348) leaves I* unchanged and is inapplicable by 05_agency.tex:333. N_inf (05_agency.tex:349) still applies. Under strict typing I* fails either way, because N_inf gives 6.27.

**Typing (interpretive).** Gotelli & Graves 1996 (pp. 3–4) define a null as producing "the pattern expected in the absence of a particular ecological mechanism". Diamond & Gilpin, via Zhang 2020, require a null to exclude only the tested factor. On this logic N_eff and N_inf are decisive only for claims that name act mechanisms, which is the table's wording.
- For the claim "formed by relays", the I* values (4.41 and 6.27, both ≥ r0 = 3.5) show the act channels do not produce the structure. That supports the claim rather than refuting it.
- Strict typing would require a relay-formed collective to be formed by acts, which contradicts the claim. The index measures as-if agency, not efficacy (05_agency.tex:251).
- Verdict on C11 depends on this reading: yes.

### (e) Does "the members' joint policies" include internal attention?

**For inclusion:**
- def:fw-system draws all four active-state components from the policy posterior (02_framework.tex:13, 17).
- Active inference makes attention a control factor or covert action: Sandved-Smith et al. 2021, Fig. 4 ("attentional policies … mental (covert) actions"); Albarracin et al. 2022 §2.5.2 (u^Who, with habits E^Who).
- Team theory makes the information structure part of the chosen "organizational form" (η, α): Marschak–Radner, Ch. 2 §3 of the 1958/59 Cowles draft.

**For exclusion:**
- As-if agency attaches to the causal effects of X on its environment (McGregor 2017; McGregor, timorl & Virgo 2024 §2).
- In Bertschinger et al. 2008 §2, M is "the actions or the behavior of the system in its environment".
- Biehl & Virgo 2023, Def. 5: the output map is the action; internal transitions are belief updates. Virgo et al. 2021: interpretations depend only on internal dynamics.
- Albantakis et al. 2021: actions are motor outputs.
- Waade et al. 2025 §2.3: the observations of sensory agents and the actions of active agents "comprise the blanket states of the group agent". Internal votes are aggregated, and the group POMDP is fitted to the blanket.
- Jørgensen, Weichwald & Hammond 2026 §4.3, Prop. 17: the actor-critic collective agent's decision is the actor's action; the critic is "marginalized out".
- List & Pettit 2012: judging roles (organizational structure) are distinct from executive action in the group's name.
- Pettit 2014 §4.3.2: patterns intelligible from members' group-independent profiles give no reason to posit a group agent. In I*, attention is explained by each member's own EFE.

**Neutral but relevant:** MEG treats the decision set as a declared hypothesis (Def. 4.4; §7 "Choice of variables"). Abel et al. 2025 call agency frame-dependent, with the boundary a frame commitment.

**Strongest evidence of intent:** the usage at ext2_rfm.tex:139,167 and s07_formation.tex:123 (interpretive, textual). The verdict's grade depends on this reading; existence (Agency0 > 0) does not.

**Derived (proved, elementary).** Take C12's hypotheses, with P_g = E^a ⊗ P_g^s. Let K = KL(P_s||E^s), R = inf_g KL(P_s||P_g^s) and I = I_P(s;a), per decision state. Then:
- The full-policy index divided by its C12 bound equals 1 − (I+R)/(I+K).
- This is at most the slot-marginal index 1 − R/K, with equality iff I = 0. Proof: E_a KL(P_{s|a}||Q) = I + KL(P_s||Q), so (I+R)/(I+K) ≥ R/K because I(K−R) ≥ 0.
- Nagelkerke 1991 (eq. 3, R̄² = R²/max R²) is the precedent for rescaling by the attainable maximum.
- Arithmetic on the record's rounded numbers gives 0.0078/0.00835 ≈ 0.93 and 0.0080/0.00835 ≈ 0.96, consistent with the bound against the slot-only 0.971 and 0.99988. This is not a computation of this round.

### (f) Real-time versus frozen-state deliberation

- **Frozen state.** The Gibbs law is a property of one-at-a-time logit revision on a fixed game:
  - Blume 1993 §6.1, eq. (6.2), pp. 408–409: a Gibbs state requires switching-order consistency for every two players; Appendix 2 gives sufficiency (not read).
  - Alós-Ferrer & Netzer, Prop. 1 calls this a "knife-edge technical fact". Under other revision processes only stochastic stability is characterized (their Thm 1; Marden & Shamma 2012).
- **Real time.** When the payoff-relevant state moves with play, the game is a state-based game (Marden 2012; Liu, Wang & Cheng 2016, Def. 20, eqs. (33)–(34)).
  - Per-state alignment (33) needs an added transition condition (34).
  - Their Thm 21 gives convergence of better reply with inertia to recurrent state equilibria. No finite-precision group-posterior law is given.
- **Reading.** The frozen-state law is the fast-deliberation limit of two-time-scale dynamics (Borkar 1997, via Borkar's own restatement). def:agy-group-model adopts it verbatim: "at a decision state held fixed while the members deliberate" (05_agency.tex:161). The open issue is consistency with one-round speech latency (02_framework.tex:15). Interpretive; the grade depends on it, existence does not.

## Topic (ii): when distributed epistemic choices equal a planner's

- **The planner's law at finite precision.** Ortega & Braun 2013, Cor. 3: p ∝ p0 e^{βU} maximizes E_qU − β⁻¹KL(q||p0). So P_C is the bounded-rational planner with reference E_C (interpretive identification).
- **Equality in law.** It holds with an exact potential plus one-at-a-time logit revision (Blume; Alós-Ferrer & Netzer, Prop. 1). Conditional-MI utilities supply that potential (Choi & Lee, Lemma 1, per round 1). This matches thm:agy-agency(c),(d) (05_agency.tex:197-202).
- **Equality of optima.** Concave differentiable payoff: stationary implies optimal (Marschak–Radner Ch. 5 §2.3 Thm 1, 1959 draft; Radner 1962 Thm 1, via secondary accounts). For discrete teams this fails, and deciding team optimality is NP-hard (Tsitsiklis & Athans 1985 §IV, Cor. 4.1).
- **Approximation.** Valid utility systems with monotone submodular welfare have every pure Nash equilibrium ≥ OPT/(1+curvature) ≥ OPT/2 (Vetta 2002, Thm 5). With slot costs ψ the welfare is non-monotone and Thm 3's additive-term form applies.
- **Economics.** Decentralized acquisition is efficient only if information use is efficient and u_σσ = 0 (Colombo, Femminis & Pavan 2014, Cor. 2).

## Topic (iii): prior art for the index and for C12

- **Identity (proved, by definition).** Index = sup_g E_P[log(P_g/E)] / KL(P||E). With E uniform and the soft-optimal family of one utility, the numerator is MEG (MacDermott et al. 2024, Def. 3.2). MEG allows β ∈ ℝ; the manuscript has γ_C ≥ 0.
- **MEG and irrelevant decisions (proved, elementary).** MEG is unchanged when decisions the utility cannot depend on are added: they cancel, since the maximum-entropy policy is uniform on them (cf. Prop. 3.3). The normalized index is diluted by them, which is the content of C12.
- **Fraction-explained precedents.**
  - Cameron & Windmeijer: R²_KL = 1 − K(y,μ̂)/K(y,μ̂₀) (eq. 5). Prop. 1: lies in [0,1] and is nondecreasing as regressors are added. Prop. 2: for canonical links it equals the Pythagorean "fraction explained".
  - Schneidman et al.: I2/IN = 1 − KL(P||P2)/KL(P||P1).
  - Amari 2001, Thm 5: Pythagorean decomposition. If the class is an exponential family through E with moment matching, index = KL(P_ĝ||E)/KL(P||E).
- **C12 status.** I found no prior statement of the C12 bound. It is new as stated but elementary.

## Topic (iv): formation by selective attention, and novelty

Prior art for formation by attention or partner choice:
- Albarracin et al. 2022: EFE-selected whom-to-attend with habits. Already cited at s12_related.tex:11 and 12_related.tex:35.
- Sethi & Yildiz 2016, Prop. 2(c): segregation over any partition into groups of at least two arises with positive probability among ex ante identical Bayesian listeners. That partition is not predicted by access.
- Baumann et al. 2020: homophilic partner choice, eq. (2); β = 0 is a uniform-partner null.
- Sasahara et al. 2021: unfollowing alone segregates.
- Che & Mierendorff 2019, Thm 1: optimal own-biased "information diets" for a single decision maker.

I*'s partition coincides with its access niches (N_w predicts {A,B}), which restricts the claim. A Sethi–Yildiz-type symmetry breaking would avoid that restriction. This is a pointer, not a result.

**Other uncited or secondarily cited items:**
- bertschinger2008autonomy and pfante2014comparison are in references.bib but cited in no section.
- Bertschinger et al. 2008, Eq. (15), conditions on interventions on the environment to remove the system's control of it. This is a precedent for conditioning Ω_int on the shared drive.
- The manuscript cites Blume secondarily (05_agency.tex:208). Primary locators are now available (§6.1, pp. 408–409).

## Sources (read in this round unless marked R1 = round 1, from the record)

Read depth: F = full text; P = the parts named; A = abstract; S = secondary account; V = page images. "bib" = already in references.bib.

**Topic (i)**
- MacDermott, Fox, Belardinelli & Everitt, NeurIPS 2024, arXiv:2412.04758. Def. 3.2, Props. 3.2–3.3, Thm 5.1, §7 and fn. 7. P (pp. 1–10). Closest precedent for the index's numerator. Not in bib.
- Krakauer, Bertschinger, Olbrich, Flack & Ay, Theory Biosci. 139:209 (2020), doi:10.1007/s12064-020-00313-7. A* = I(S_{n+1};S_n), A = I(S_{n+1};S_n|E_n), nC; pp. 214–216. P (pp. 209–216). Internal coordination counts toward temporal integrity, not toward a policy. bib.
- Bertschinger, Olbrich, Ay & Jost, BioSystems 91:331 (2008), doi:10.1016/j.biosystems.2007.05.018. §2 (M is behavior), Eqs. (7), (9), (15). P (author version). bib, uncited.
- Biehl & Virgo, IWAI 2022 (CCIS 1721, 2023), arXiv:2209.01619. Defs. 2–3, 5; eq. (6). P (pp. 1–8). Not in bib.
- Virgo, Biehl & McGregor 2021, arXiv:2112.13523. Def. 1 and §2.2. P (pp. 1–4). Not in bib.
- McGregor, Adaptive Behavior 25:72 (2017), doi:10.1177/1059712317700501. A.
- McGregor, timorl & Virgo, arXiv:2405.16490v2. Abstract (triviality and uniqueness), §§2–3.2. P.
- Albantakis, Massari, Beheler-Amass & Tononi 2021, arXiv:2004.00058. Actions are motor outputs. P (pp. 1–8).
- Hoel 2018, doi:10.1007/978-3-319-75726-1_6. EI definition, App. A.2. P.
- Kenton et al., Artif. Intell. 322:103963 (2023), arXiv:2208.08345. Abstract and §1. A/P.
- Jørgensen, Weichwald & Hammond, CLeaR 2026, arXiv:2605.00248. Defs. 13–15, Prop. 16, §4.3 and Prop. 17 (critic marginalized). P (adds §4.3 to R1). Not in bib.
- Waade et al., Entropy 27:143 (2025), doi:10.3390/e27020143. §2 conditions (i)–(iii); §2.3 blanket states and votes. P (pp. 5–10). bib.
- List & Pettit, Episteme 9(3):293–309 (2012), LSE eprint 46881. Judging roles versus executive roles. P. Ch. 3 of Group Agency (2011): A.
- Pettit 2014, in Lackey (ed.), doi:10.1093/acprof:oso/9780199665792.003.0005. §4.3.2. P.
- Maisto, Nuzzi & Pezzulo, arXiv:2511.10835. §2 (active states). P. bib.
- Riedl, arXiv:2510.05174. A.
- Abel et al., arXiv:2502.04403. A.
- Xu & Rivera, arXiv:2410.04683. §3. P.
- Sandved-Smith et al., Neurosci. Conscious. niab018 (2021), doi:10.1093/nc/niab018. Fig. 4 and §"Formalizing…". P.

**Topic (ii)**
- Blume, GEB 5:387 (1993), doi:10.1006/game.1993.1023. Defs. 6.1–6.3, eqs. (6.1)–(6.2), pp. 408–409. V. bib.
- Alós-Ferrer & Netzer, GEB 68:413 (2010), doi:10.1016/j.geb.2009.08.004. Prop. 1, Cor. 1, Def. 1, Thms 1–2. P (working paper). bib.
- Marden & Shamma, GEB 75:788 (2012), doi:10.1016/j.geb.2012.03.006. A.
- Marden, Automatica 48:3075 (2012), doi:10.1016/j.automatica.2012.08.037. A. Definitions read in Li & Marden, CDC 2011, §II.B (P) and Liu, Wang & Cheng, arXiv:1608.00192, Defs. 18–20 and Thm 21 (P).
- Borkar, Syst. Control Lett. 29:291 (1997), doi:10.1016/S0167-6911(97)90015-3. S.
- Marschak & Radner, Cowles DP drafts 1958–59 (Ch. 2 §3; Ch. 5 §§2.1–2.3, Thm 1). P (poor OCR). bib (book).
- Radner, Ann. Math. Stat. 33:857 (1962), doi:10.1214/aoms/1177704455. S. bib.
- Tsitsiklis & Athans, IEEE TAC 30(5):440 (1985). §IV, Cor. 4.1. P.
- Vetta, FOCS 2002, doi:10.1109/SFCS.2002.1181966. Thms 3 and 5. P.
- Colombo, Femminis & Pavan, RES 81:1438 (2014), doi:10.1093/restud/rdu015. Props. 4–5, Cors. 2–3. P (working paper).
- Ortega & Braun, Proc. R. Soc. A 469:20120683, arXiv:1204.6481. Cor. 3. P.
- Choi & Lee; Krause & Guestrin; Hellwig & Veldkamp; Marden, Arslan & Shamma: R1.

**Topic (iii)**
- Cameron & Windmeijer, J. Econometrics 77:329 (1997), doi:10.1016/S0304-4076(96)01818-0. Eq. (5), Props. 1–2. P (1995 preprint). Not in bib.
- Schneidman, Berry, Segev & Bialek, Nature 440:1007 (2006), doi:10.1038/nature04701, arXiv:q-bio/0512013. §§II–III. P. Not in bib.
- Amari, IEEE TIT 47:1701 (2001), doi:10.1109/18.930911. Thms 5 and 8. P (equations garbled). Not in bib.
- Nagelkerke, Biometrika 78:691 (1991), doi:10.1093/biomet/78.3.691. Eq. (3). F. Not in bib.

**Topic (iv) and reading (a)**
- Albarracin, Demekas, Ramstead & Heins, Entropy 24:476 (2022), doi:10.3390/e24040476. §§1–2.6. P. bib.
- Sethi & Yildiz, Econometrica 84:2029 (2016), doi:10.3982/ECTA13320. Eqs. (5)–(6), Props. 1–2. P.
- Baumann, Lorenz-Spreen, Sokolov & Starnini, PRL 124:048301 (2020), arXiv:1906.12325. Eq. (2). P.
- Sasahara et al., J. Comput. Soc. Sci. 4:381 (2021), doi:10.1007/s42001-020-00084-7. P.
- Che & Mierendorff, AER 109:2993 (2019), doi:10.1257/aer.20171000. Thm 1. P.
- Constant et al., J. R. Soc. Interface 15:20170685 (2018), doi:10.1098/rsif.2017.0685. Intro and Fig. 1. P. bib.
- Kirsh & Maglio, Cognitive Science 18:513 (1994), doi:10.1207/s15516709cog1804_1. Abstract, pp. 513–515, Discussion. P.
- Heylighen, Cogn. Syst. Res. 38:4 (2016), doi:10.1016/j.cogsys.2015.12.002. pp. 6–7. S. bib.
- Gotelli & Graves 1996, pp. 3–4. S, via Gotelli & McGill, Ecography 29:793 (2006) and Zhang, Biol. Philos. 35:31 (2020).

## Not read (Exa leads only, unverified)

Calvó-Armengol, de Martí & Prat 2015; Angeletos & Pavan 2007; Parr & Friston 2017; Limanowski & Friston 2018; Friston 2013; Friston et al. 2023; Oizumi, Tsuchiya & Amari 2016; Ay 2015; McFadden 1977; the primary texts of Radner 1962 and Monderer & Shapley 1996 (no access); Golub & Jackson 2012; Juel et al. 2019; Rosas et al. 2020 and 2024; Cover & Thomas Thm 2.5.3 (the chain rule is used as standard, not cited).

## Process and files

- One Exa ultra run (agent_run_254ba13d803349c983b3e4a761572547): completed, $10.50, 67 leads. Exa credits were exhausted afterwards (HTTP 402), so later reads used the scholar tools.
- I ran one non-numerical text-extraction script, with `python -I` and the standard library only, because it read downloaded tool output.
- No repository or vault file was edited.

Files:
- C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round3\literature\exa_condensed.txt
- C:\Users\CHRISA~1\AppData\Local\Temp\claude\63c81c17e87f0010\34faeca5-ea90-45d1-8cc4-412bdf898c58\scratchpad\metaagent\round3\literature\dump_exa.py
- Raw Exa output: C:\Users\chris and christine\.claude\projects\C--Users-chris-and-christine-Desktop-Research\34faeca5-ea90-45d1-8cc4-412bdf898c58\tool-results\mcp-1fe2ed52-a65d-40a5-b569-e2ccd38c28d8-agent_run-1795321004218-8pwrdx.txt