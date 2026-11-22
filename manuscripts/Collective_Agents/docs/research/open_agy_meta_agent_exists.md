# Existence of a meta-agent (`open:agy-meta-agent-exists`)

- Status: active
- Opened: 2026-11-21
- Updated: 2026-11-22
- Sessions: 3

## Target

- Locked statement: Settle `open:agy-meta-agent-exists` (`Collective_Agents/sections/s05_agency.tex`, lines 295-297): "Exhibit one linear-Gaussian population and one set $C$ of its agents that meets every clause of `def:agy-meta-agent` at a stated grade with $r_0>1$ and $\Agency_0>0$, that is, a collective at level $r_0$ that is closed at stated tolerances for a declared coarse variable, differs from every applicable null of type D, including partner randomization at a stated level, survives exact fusion and has agency index at least $\Agency_0$; or prove that the clauses are jointly unsatisfiable in a stated class of populations." The clauses are those of `def:agy-meta-agent` (`05_agency.tex:379-381`) with `def:col-collective` (`04_collectives.tex:214-221`), `def:col-contrast` (`:182-188`), `def:col-baseline` (`:197-209`), the diffusive class (`:147-151`), `def:col-world-conditional` (`:130-132`), `def:agy-closure` (`05_agency.tex:13-24`), `def:agy-group-model` and (P0)-(P4) (`:156-169`), `def:agy-agency-index` (`:240-246`), `def:agy-nulls` with `tab:agy-nulls` (`:332-360`).
- Falsifier: for the existence direction, any clause of `def:agy-meta-agent` that the exhibited population fails at the stated grade, under the manuscript's own definitions read literally; for an impossibility direction, one population in the stated class that meets every clause.
- May assume: the linear-Gaussian framework of `def:fw-system`; any declared population, protocol, admitted class, coarse variable, decision states, selector and grade, provided each is declared before the analysis as the definitions require; computation for clauses that are statistical (partner randomization) or tolerances.
- Must not assume: that contrast is defined for non-diffusive precisions (`open:col-non-diffusive`); that a null is inapplicable unless its intervention leaves the model literally unchanged; that agreement with an explanation null (type E) is a failure (it restricts the claim only); that the closure, agency or interaction theorems of `thm:agy-h1` apply outside their stated hypotheses; that an agency index of one reached only because the members act by habit counts (the open problem's own wording excludes it, `s05_agency.tex:296`).
- Alternative forms: (A) a computed instance that meets every clause at a stated grade, with each clause's margin; (B) an existence theorem on a nonempty open subset of a declared admitted class; (C) a proof that the clauses are jointly unsatisfiable in a stated class, which settles the problem only for that class.
- Test instance: `ex:met-two-firms` at its declared settings must come out non-diffusive at $n_{\mathrm c}=0,1,4$ under any route's computation of $\Pi^c$ (`rem:agy-h1-status`, `chk:met-two-firms`). Passed by the performative route's reconstruction (largest off-diagonal 166.3, smallest row sum $-0.8215$ at $n_{\mathrm c}=1$, bounded model).
- Out of scope: defining contrast for non-diffusive precisions; the H5a abstract-physics structure, which `def:agy-meta-agent` does not require; MAgent_Theory_2.0's formation standard (F1)-(F6).
- Reading chosen: the literal reading of `def:agy-meta-agent` with the null types of `tab:agy-nulls`, including the open-subset and every-selector-constant reading of "differs" in `def:agy-nulls`, inside the time-invariant framework of `def:fw-system` (one-round message latency, one policy precision $\gamma$). Results obtained under other declarations are recorded with those declarations named. Where the definitions leave a reading open, every construction is reported across the readings of O2, and the reading-by-grade matrix in the round-3 synthesis (`open_agy_meta_agent_exists-round3-synthesis.md`, Section 1) is the summary.

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| World-conditional law | conditional law of the agents' errors given the whole world path and the sender-side broadcast noises (`def:col-world-conditional`); an agent's own sensing noise is a private input and is not conditioned on, even when relayed | level-0 scalar network: $\Sigma^c=\sum_nW^nQ^\zeta W^{n\top}$ |
| Diffusive precision | $\Pi=\diag(\varepsilon)+L$, couplings $a_{ij}=-\Pi_{ij}\ge0$, leaks $\varepsilon_i=(\Pi\one)_i\ge0$ | $\Pi=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$: $a_{12}=1$, $\varepsilon=(1,1)$ |
| Contrast | $r(C)=\xin/\xout$, $\xout=\phi_C^\top\Pi\phi_C$, $\xin=\min_{f\perp\one_C}f^\top(\diag(\varepsilon)+L_C)f/f^\top f$; vector errors only through $\Sigma^{\mathrm{sc}}\otimes I_K$ or a declared scalar coordinate | compound-symmetric block $\Sigma=\alpha I_n+\beta\one\one^\top$ with no cut: $r=1+n\beta/\alpha$; at $\alpha=1,\beta=0.5,n=4$, $r=3$ |
| Baseline clause (c), mean coupling | exchangeable medium, coupling $\bar a$, leak $\bar\varepsilon$; $\bar r_{\mathrm{hom}}=1+N\bar a/\bar\varepsilon$ with uniform leak | two disjoint cliques of size $n$, coupling $a$, leak $\varepsilon$: $\bar r_{\mathrm{hom}}=1+\frac{2n(n-1)}{2n-1}\frac a\varepsilon$, clique $r=1+\frac{na}{\varepsilon}$ |
| Baseline clause (c), mechanism | exchangeable state of the declared coupling mechanism (`04_collectives.tex:202`), precedent `lem:frm-split-law` | computed per instance |
| Second-moment convention | with attention or slots drawn at random each round, $\Sigma^c=\E[\Cov(e(t)\mid\eta)]$, estimable as $\frac12\E[(e^1-e^2)(e^1-e^2)^\top]$ from two replicas on one world path | epistemic instance: $\beta=0.200540$ including policy-mixture part $0.009889$ |
| Agency index | `def:agy-agency-index`, KL(actual ‖ model), class containing the habit-only model, habits fixed or $\gamma_C$ bounded below | exact group posterior in the class: index 1 |
| Relayed sensing noise | an agent's own sensing noise stays a private input when the agent relays its reading; basis: `04_collectives.tex:15` assigns to the active channel only the sender-side noise of a broadcast, so the content a sender writes, its reading included, belongs to the conditioned process, and the level-0 law `prop:col-world-conditional` (`04_collectives.tex:135-141`) leaves $F\Kg^s_iv_i$ inside $\zeta_i$ and propagates it to listeners through $W$ (reading O2(h)) | conditioning on it instead: C13 gives $r=1.003$, P0 gives $r=1.000000$ |
| Partner randomization | the every-round variant of `tab:agy-nulls` (`05_agency.tex:350`), declared with the grade; the drawn-once variant is reported separately (reading O2(g)) | C13: annealed contrast 2.844, $p=0.001$ with 999 draws |
| Selector output | contrast at level $r_0$; the output is the set of collectives at that level, and an agent in no collective is left unassigned (reading O2(n)) | P0: output $\{A\}$, source unassigned |
| Group belief class | G1: the declared belief is a translate with a free constant variance; G2 (variance from the members' current state) is inadmissible under a scalar coarse variable, `05_agency.tex:157` (reading O2(q)) | C11: G1 0.99988, G2 0.971 at the coarse decision state |
| KL direction | $\KL(p\Vert q)=\E_p[\ln p-\ln q]$ | $\KL(\Ncal(0,1)\Vert\Ncal(0,4))=\ln2-3/8$ |

## Claims

### C1: Exchangeable blocks are diffusive

- Statement: If the world-conditional errors of a set $C$ of $n$ scalar agents have covariance $\alpha I_n+\beta\one\one^\top$, $\alpha>0$, $\beta\ge0$, and are uncorrelated with every other agent's, and the rest of the population's precision is diffusive, then $\Pi^c$ is diffusive, with coupling $\beta/(\alpha(\alpha+n\beta))$ and leak $1/(\alpha+n\beta)$ on $C$, no cut, and $r(C)=1+n\beta/\alpha$; for $-\alpha/n<\beta<0$ the off-diagonal entries are positive.
- Status: proved
- Review: fresh-context
- Evidence: Sherman-Morrison, derived independently by three contexts (obstruction theory Theorem C1, performative route Lemma E via the commutant of the permutation representation, literature D1); coordinator check $r=3.000000000000$ at $\alpha=1,\beta=0.5,n=4$ with negative control $\beta=-0.1$ non-diffusive; `open_agy_meta_agent_exists-checks/obstruction-theory/c1_factor.py`. The sign part is classical: positive one-factor models have complete M-matrix precisions (Wermuth and Marchetti 2014, Lemma 1).
- Check: 2026-11-21, three agents (obstruction theory, performative route, literature) each derived the formula from the statement alone, without another's argument; all agree.
- Depends on: none

### C2: Epistemic niche meta-agent in an episode-clock model

- Statement: Two niches of $n=4$ agents with independent world components, each component renewed every two rounds (one sensing round, one delivery round), every agent modeling only its niche's component; each agent opens an exterior slot by deliberation (P1)-(P4) with epistemic preferences and uniform product habits, relays its raw reading to the niche-mates it attends, chosen by expected free energy with capacity $\kappa=3$, and fuses exactly; one precision $\gamma=40$ for slots and attention; errors are the end-of-episode filtered errors. With $P_0=1$, $R^s=1$, $R_c=0.1$, each niche is a meta-agent of grade $(r_0,\alpha_{\mathrm M},\alpha_{\mathrm I},\alpha_{\mathrm{pr}},\Agency_0)=(30,0,0.02,0.01,0.99)$ with partner randomization redrawn every round, under both the mechanism and the mean-coupling baseline.
- Status: computed
- Review: fresh-context
- Evidence: construction run (`open_agy_meta_agent_exists-reports.md`, section construct-epistemic) and an independent attack with its own code (section attack: construct-epistemic, attack 6): $r(A)=32.329$; mechanism baseline 7.653, mean-coupling baseline 27.853; other regions at most 2.774; $N_{\mathrm{hab}}$ 4.352, annealed $N_{\mathrm{pr}}$ 4.308, $p=1/(n_{\mathrm{null}}+1)$; $\alpha_{\mathrm I}=0.0151$ (variance read from the blanket path), 0.0130 (constant variance); agency index at least 0.9999995; Markov defect zero (degenerate, world renewed); $N_{\mathrm{ex}}$ inapplicable because receivers already fuse raw data exactly; deletion and freezing nulls diagonal. Holds on a ±5% box at 59/81 (mean coupling) and 70/81 (mechanism) points and on an open neighborhood of the center by continuity. Scripts: `open_agy_meta_agent_exists-checks/epistemic_niche/run_main.py`, `open_agy_meta_agent_exists-checks/epistemic_niche/main_out.txt`, `open_agy_meta_agent_exists-checks/epistemic_niche/nulls_out.txt`, `open_agy_meta_agent_exists-checks/epistemic_niche/robust_out.txt`; the attack's `open_agy_meta_agent_exists-checks/falsify_epistemic/fx.py`, `open_agy_meta_agent_exists-checks/falsify_epistemic/check_F_out.txt` (single-$\gamma$ repair) and the other `check_*` files in that folder.
- Scope: one instance, $n=4$ per niche, $P_0=1$, $R^s=1$, $R_c=0.1$, computation noise $10^{-3}$, $\gamma=40$; exact Gaussian linear algebra for $\Sigma^c$, contrast and baselines (double precision), exact deliberation chain, Monte Carlo cross-checks with 200k and 300k episodes, partner randomization redrawn every round, $n_{\mathrm{null}}=999$; a ±5% grid of 81 points.
- Check: 2026-11-21, an attack agent recomputed every deciding number with independent code; verdict: the original grade fails the inference clause at $\alpha_{\mathrm I}=0.02$ under the literal reading (0.0236 needed), the single-$\gamma$ repair at $\gamma=40$, $r_0=30$ passes every clause.
- Depends on: C1, the episode-clock declaration, the filtered-error convention

### C3: Collider obstruction (as first stated)

- Statement: When members of two collectives that do not communicate both act on a world variable that the world-conditional law conditions on, with act loadings of one sign, $\Pi^c$ has positive entries between every such pair.
- Status: refuted
- Review: fresh-context
- Evidence: counterexample E2 (performative route, recomputed by the attack): loadings of one sign, no channel, overshooting acts $\varphi=(-0.30,0.74)$, all cross entries $-0.956$, $\Pi^c$ diffusive; 13 of 2531 random draws with nonnegative dynamics have an acting cross pair with $\Pi^c_{ij}\le0$ (obstruction theory). The corrected forms are C3a to C3c. Scripts: `open_agy_meta_agent_exists-checks/performative/check3_sign_rule.py`, `open_agy_meta_agent_exists-checks/performative/check3_out.txt`, `open_agy_meta_agent_exists-checks/obstruction-theory/collider_conj_output.txt`.
- Check: 2026-11-21, the attack on the performative route recomputed E2 with its own code (cross entries $-0.95605$, $\Pi^c$ diffusive, $r(C_1)=10.8551$, $r(C_2)=146.9612$); verdict: refuted.
- Depends on: none

### C3a: Aggregate collider theorem

- Statement: If two actor sets with disjoint ancestries (no reads between the two ancestries, directly or through chains, no common ancestor, private noise block diagonal) act with loading $b$ on one conditioned scalar world direction, then $\Cov(b_1^\top x^{1}_t,b_2^\top x^{2}_t\mid\eta)=-\frac1{2\pi}\int\beta_1\beta_2/(q+\beta_1+\beta_2+\beta_3)\,d\theta<0$; if the loadings are of one sign and load on the coordinates on which contrast is computed, some world-conditional covariance is negative, so by C4 $\Pi^c$ is not a Z-matrix and the population contains no collective and no meta-agent.
- Status: proved
- Review: fresh-context
- Evidence: obstruction theory, Theorem C3 with Lemmas C3-a (path precision gains $B^\top Q_w^{-1}B$) and C3-b (one-time identity $\Pi^c=\Pi_0+B^\top Q_w^{-1}B+I_{\mathrm{other}}$, $I_{\mathrm{other}}\succeq0$); spectral integral matches the steady-state smoother to $2\times10^{-14}$; reproduces `ex:agy-collider` (1.391e-3 nats); proof check `open_agy_meta_agent_exists-checks/round3_proofcheck-o3/c3a_collider_out.txt`.
- Check: 2026-11-21, a proof-check agent rebuilt every step from the statement and the finished argument; correct with the wording repair now in Statement (one common source gives a positive contracted covariance in 105/200 draws).
- Depends on: C4

### C3b: Sign rule for exchangeable acting collectives

- Statement: For two exchangeable collectives acting on one variable without communicating, the cross entries of $\Pi^c$ have the sign of $\varphi_1\kappa_1\varphi_2\kappa_2$, with $\varphi_k$ the closed-loop factor and $\kappa_k=bg_k\sqrt{n_k}$; for acts that are group-posterior means of a one-step quadratic expected free energy with continuous Gaussian habits, and members who know the sign of their effect, the sign is positive, so two such collectives are never diffusive. With noise on the predictions the rule holds when $c_{0,k}>0$ and $\varphi_1\varphi_2>0$.
- Status: proved
- Review: fresh-context
- Evidence: performative route, Proposition S and its corollary; 11 computed instances; the attack re-derived the sign argument; proof check `open_agy_meta_agent_exists-checks/round3_proofcheck-o3/c3b_noise_formula_out.txt`.
- Check: 2026-11-21, a proof-check agent rebuilt the argument; correct within setting P; its side remark that prediction noise changes only $\mathrm{diag}(V)$ is refuted, and the noise condition in Statement replaces it (the rule fails in 57/300 draws, all with $\varphi_1\varphi_2<0$).
- Depends on: C7

### C3c: Pairwise collider under eigen-loading

- Statement: Under the hypotheses of C3a, if $J_k(\theta)^{-1}b_k=\rho_k(\theta)b_k$ with $\rho_k>0$, every cross block of the world-conditional precision of the coordinates of the actors and their ancestors is $\kappa_{kl}\hat b_k\hat b_l^\top$ with $\kappa_{kl}>0$; for the whole population's precision this holds when no agent outside those sets reads them.
- Status: proved
- Review: fresh-context
- Evidence: obstruction theory, Theorem C3-pair; 300 draws rank one to $3\times10^{-14}$; proof check `open_agy_meta_agent_exists-checks/round3_proofcheck-o3/c3c_listener_one_group_out.txt`.
- Check: 2026-11-21, a proof-check agent rebuilt the argument; correct with the scope repair now in Statement (an outside listener gives a rank-two cross block, negative in 16/100 draws).
- Depends on: C3a

### C4: Tests for diffusivity

- Statement: If $\Pi$ is a positive definite Z-matrix (diffusive or not; the row sums are not used), then $\Sigma=\Pi^{-1}\ge0$ entrywise, $\Sigma_{ij}>0$ exactly within connected components of the coupling graph, $\Sigma_{ij}\Sigma_{jk}\le\Sigma_{ik}\Sigma_{jj}$, and every principal submatrix of $\Sigma$ has a Z-matrix inverse.
- Status: proved
- Review: fresh-context
- Evidence: obstruction theory, Lemma Z (Neumann series and Schur complements); 300 diffusive draws without violation, random positive covariances violate the third property in 276/300; proof check `open_agy_meta_agent_exists-checks/round3_proofcheck-o3/c4_lemma_z_out.txt` (300 Z-matrices with a negative row sum, no violation).
- Check: 2026-11-21, a proof-check agent rebuilt every step; correct as stated, and the stronger form in Statement holds with the same proof.
- Depends on: none

### C5: Factor model and raw-data sharing

- Statement: For $\Sigma=D+GVG^\top$ with $D>0$ diagonal, explicit formulas give $\Pi$; with $G\ge0$ and $V^{-1}+G^\top D^{-1}G$ a Z-matrix the off-diagonals are nonpositive; with independent sources ($V$ diagonal) and $G\ge0$ (or one-signed source columns), diffusivity requires the relation "share a source" to be transitive, so raw-data sharing in which two members share no source while both share one with a third is never diffusive.
- Status: proved
- Review: fresh-context
- Evidence: obstruction theory, Theorem F and Corollary F-share; counterexamples CE1 to CE4 with $G\ge0$; proof check `open_agy_meta_agent_exists-checks/round3_proofcheck-o3/c5_factor_out.txt`.
- Check: 2026-11-21, a proof-check agent rebuilt the argument; correct with the sign hypothesis now in Statement (with mixed signs the transitivity clause is false, exact counterexample); Theorem F(c)'s "iff", not part of this statement, also needs every factor loaded.
- Depends on: C4

### C6: Singular consensus

- Statement: For $Y=WX+\delta$, $\delta\sim\Ncal(0,\tau I)$, $\Pi_Y=\tau^{-1}P_{\ker W^\top}+R_\tau$ with $0\preceq R_\tau\preceq R_0$; $P_K$ is a Z-matrix exactly when $W$ averages completely within the blocks of a partition; the lazy ring with $n=4$ is non-diffusive iff $\tau<\sigma^2/2$, and one-shot lazy rings with $n\ge6$ are non-diffusive at every $\tau$; complete averaging is diffusive at every $\tau$.
- Status: proved
- Review: self
- Evidence: obstruction theory, Propositions S, S-char, S-dyn; a one-firm lazy-ring analogue gives $\Pi^c_{13}=138.6$ against a kernel term of 150.8.
- Depends on: C4

### C7: Closed form for a single acting exchangeable collective

- Statement: For one exchangeable collective that is the only actor on its scalar world component (setting P of the performative route), $r=r_0D_{\mathrm{fb}}D_{\mathrm{coll}}$ in closed form, and $\Pi^c$ is diffusive iff $r\ge1$.
- Status: proved
- Review: fresh-context
- Evidence: performative route, Proposition P; windowed conditioning matches to $2.7\times10^{-15}$ (`open_agy_meta_agent_exists-checks/performative/check1_out.txt`); the attack re-derived steps 1-5 and recomputed $r(A)=24.49892604$ with its own code (`open_agy_meta_agent_exists-checks/attack-performative/a1_reconstruct_and_nex.py`).
- Check: 2026-11-21, attack agent re-derived Proposition P by hand and matched the closed form to $1.5\times10^{-15}$ with independent code; agrees.
- Depends on: C1

### C8: Acts never raise contrast in setting P

- Statement: In setting P, $D_{\mathrm{coll}}\le1$, and $D_{\mathrm{fb}}<1$ for acts consistent with expected free energy; hence if $N_{\mathrm{eff}}$ is a null of type D for the collective, no collective in setting P is a meta-agent.
- Status: proved
- Review: fresh-context
- Evidence: performative route, Proposition N; the attack re-derived the inequalities by hand.
- Check: 2026-11-21, attack agent re-derived $D_{\mathrm{coll}}\le1$ and $D_{\mathrm{fb}}<1$ for consistent acts by hand; agrees.
- Depends on: C7

### C9: Performative niche candidate

- Statement: The performative niche population PN (two niches of four, $F=0.9$, $Q=0.05$, raw data sharing, attention at $\gamma=300$, acts as group-posterior means with $bgn=0.04$) meets every clause at grade $r_0\in(5.075,24.4]$, $\alpha_{\mathrm M}=0$, $\alpha_{\mathrm I}=5.61\times10^{-3}$, $\alpha_{\mathrm{pr}}=0.01$, $\Agency_0=0.94$, under four readings: $N_{\mathrm{eff}}$ and $N_{\mathrm{inf}}$ are type D only for collectives said to form by joint action or by communication through acts; deliberation act randomness read by several members is conditioned; the mechanism medium is declared and held fixed under the nulls; agency is evaluated on the act component, extended to continuous acts or through a declared discrete model.
- Status: computed
- Review: fresh-context
- Evidence: performative route and its attack: $N_{\mathrm{ex}}$ is applicable (members ignore the message content of the acts) and survived with $r_{\mathrm{ex}}=6756.48$; agency 0.966 with $\gamma_C\in[0,\infty)$, 0.039 with the declared $\gamma_C\in[0,6]$; annealed $N_{\mathrm{hab}}$ 4.37 and $N_{\mathrm{pr}}$ 3.67 below the baseline 5.075; with the literal one-round latency of `def:fw-system` the window is $(3.054,6.169]$ with both nulls below its lower edge (attack A8, numerical). Fails at $g\ge0.10$. Scripts: `open_agy_meta_agent_exists-checks/performative/check5_out.txt`, `open_agy_meta_agent_exists-checks/performative/check8_out.txt`, `open_agy_meta_agent_exists-checks/performative/check12_out.txt`, `open_agy_meta_agent_exists-checks/performative/check13_out.txt`; attack `open_agy_meta_agent_exists-checks/attack-performative/a4_out.txt`, `open_agy_meta_agent_exists-checks/attack-performative/a6_out.txt`, `open_agy_meta_agent_exists-checks/attack-performative/a8_out.txt`.
- Scope: one instance (two niches of four, $F=0.9$, $Q=0.05$, $R=1$, $R_c=0.2$, $b=0.2$, $g=0.05$); exact Gaussian conditioning on 30- to 160-round world windows (converged to $10^{-14}$); annealed nulls and the mechanism baseline by second moments over 1500 sampled attention sequences per seed; agency over 200 decision states.
- Check: 2026-11-21, attack agent reconstructed $\Pi^c$ and recomputed the nulls, $N_{\mathrm{ex}}$, agency and the latency variant with its own code; verdict: survives with the corrections listed in Evidence, and depends on the first reading.
- Depends on: C7, C8, the four readings

### C10: Impossibility classes

- Statement: (I1) a population whose diffusive $\Pi^c$ equals its own comparison medium contains no collective; (I2) in a closed population under the mean-coupling clause the whole population is never a collective, and a collective with uniform leak needs mean internal coupling above $(N/n)\bar a$; (I3) C3a; (I4) C6 under its condition (I); (I5) if some policy is selected by expected free energy and the selected partition at some selector constant is the same at $\gamma$ and at $\gamma=0$, the collective fails the differ clause against $N_{\mathrm{hab}}$.
- Status: proved
- Review: self
- Evidence: obstruction theory, Part 4; all 247 regions enumerated for I1.
- Depends on: C3a, C4, C6

### C11: Epistemic meta-agent in the time-invariant framework

- Statement: In instance I* (two niches of four agents; independent AR(1) world components with $F=0.9$, $Q=0.05$, no renewal; own sensor noise $R=1$; every agent relays its own raw reading to all others with literal one-round latency and receiver-specific noise $R_c=0.1$, no re-relaying; one optional slot per agent, a public world channel of its niche read by every niche member through its own read noise $R_s=2$; exact filters on $(\eta_t,\eta_{t-1})$ with computation noise $10^{-4}I_2$; capacity $\kappa=12$; one policy precision $\gamma=400$ for attention and slots; slot cost $\psi=0.024$ nats; uniform product habits; prior errors as contrast coordinates), niche A is a meta-agent of grade $(r_0,\alpha_{\mathrm M},\alpha_{\mathrm I},\alpha_{\mathrm{pr}},\Agency_0)=(3.5,0.02,0.09,0.01,0.99)$ with $n_{\mathrm{null}}=999$, under five readings: (i) the clause (c) mechanism baseline; (ii) partner randomization redrawn every round; (iii) the declared coarse variable is the scalar collective average of the members' prior means; (iv) deliberation follows (P4) at a decision state held fixed while the members deliberate; (v) the index's "joint policies" are the slot policies of `def:agy-group-model`, and $N_{\mathrm{eff}}$, $N_{\mathrm{inf}}$ are typed as `tab:agy-nulls` words them (D only for collectives said to form by joint action or by communication through acts), or slot opening is not an act.
- Status: computed
- Review: fresh-context
- Evidence: constructor: $r(A)=4.4319\pm0.0075$ (real-time protocol) and $4.3912\pm0.0044$ ((P4) protocol); mechanism baseline $2.9417\pm0.0072$; other regions at most 1.924; $N_{\mathrm{hab}}$ 1.741, $N_{\mathrm{pr}}$ 1.886, $N_{\mathrm{lp}}$ 1.050, $N_{\mathrm{fr}}$ diagonal; $N_{\mathrm{ex}}$ inapplicable; agency $1-10^{-10}$ at the symmetric decision state under (P4), departure from habits 0.124 nats, not a product law; Markov defect of the scalar average at most $1.38\times10^{-2}$ on the worst explored path and $10^{-4}$ in the stationary state; inference 0.0810 (best constant encoding). Full grade on a ±1% box at 17/17 points, differ clause on a ±5% box at 17/17. Scripts: `open_agy_meta_agent_exists-checks/round2_epistemic_persistent/run_main.py`, `open_agy_meta_agent_exists-checks/round2_epistemic_persistent/main_out.txt`, `open_agy_meta_agent_exists-checks/round2_epistemic_persistent/nulls_out.txt`, `open_agy_meta_agent_exists-checks/round2_epistemic_persistent/agency_out.txt`, `open_agy_meta_agent_exists-checks/round2_epistemic_persistent/box_hw0.01_summary.txt`; attack `open_agy_meta_agent_exists-checks/round2_attack_persistent/run2_out.txt`, `open_agy_meta_agent_exists-checks/round2_attack_persistent/run3_out.txt`, `open_agy_meta_agent_exists-checks/round2_attack_persistent/run9_out.txt`.
- Scope: one instance and a 17-point ±1% box (and ±5% for the differ clause) over $F,Q,R,R_c,R_s,\psi,\gamma$ and the computation noise; second moments by exact two-replica algebra per pair of policy paths, Monte Carlo over 160 pairs (standard errors stated), cross-checked by sampled-noise Monte Carlo; partner randomization with 999 independent draws; agency over declared decision states.
- Check: 2026-11-21, an attack agent rebuilt the model from the specification with its own code and reproduced every deciding number ($r(A)=4.4185\pm0.0112$, medium $2.9477\pm0.0081$, $N_{\mathrm{hab}}$ 1.733, $N_{\mathrm{pr}}$ 1.886, inference 0.0810, $p=0.001$ with 999 draws); verdict: survives under the readings named in Statement; fails if the index's joint policies include attention (C12) or if slot opening is an act and $N_{\mathrm{eff}}$, $N_{\mathrm{inf}}$ are type D for every collective whose members act; the constructor's $\mathbb R^2$ coarse variable is not a permitted declaration, and the scalar repair passes.
- Round-3 notes: the open-neighborhood part is discharged by C19, and under the mean-coupling baseline $r_0=4.15$ works on a C19 neighborhood (window $(3.94,4.43]$); the group-belief class G2 is inadmissible, so G1 values govern (0.99988 at the coarse decision state); the real-time protocol is not the literal per-round law of `def:fw-system`, whose index is not computed; not computed under O2(j), O2(l) or drawn-once partner randomization; fails under strict typing with opening a slot read as an act (R5).
- Depends on: C1, C19, readings (i)-(v), O2(h), O2(i)

### C12: Agency bound when formation runs through internal attention

- Statement: Let each member's policy be a pair (internal attention $a_i$, slot policy $s_i$) with product habits $E=E^a\otimes E^s$, and let every group model of the admissible class keep these habits and have $G_C$ depending on the slot profile only. Then at every decision state $\Agency\le\KL_{s\mid a}/(\KL_a+\KL_{s\mid a})$, with $\KL_a=\KL(\mathbb P_a\Vert E^a)$ and $\KL_{s\mid a}=\E_{\mathbb P_a}\KL(\mathbb P_{s\mid a}\Vert E^s)$, the denominator being nonzero; and $\KL_{s\mid a}\le\sum_i\max_{s_i}\ln(1/E^s_i(s_i))$, which is $\sum_i\ln\lvert\mathcal A_i\rvert$ for uniform slot habits, so an index of at least $\Agency_0$ needs $\sum_i\max_{s_i}\ln(1/E^s_i(s_i))\ge\frac{\Agency_0}{1-\Agency_0}\KL_a$.
- Status: proved
- Review: fresh-context
- Check: 2026-11-21, a proof-check agent rebuilt the bound; the first part is correct; the earlier second part ($\sum_i\ln\lvert\mathcal A_i\rvert$) is false for non-uniform slot habits (index 0.9525 with $\ln2<4.14$, `open_agy_meta_agent_exists-checks/round3_proofcheck-o3/c12_agency_out.txt`) and is replaced by the form in Statement; C11 declares uniform habits and is unaffected. The literature investigator adds that the ratio of the index to this bound is at most the index of the slot marginal, with equality iff the slot and attention components are independent.
- Evidence: every model of the class factorizes as $\mathbb P_g=E^a\otimes\mathbb P^s_g$, so by the chain rule $\KL(\mathbb P\Vert\mathbb P_g)\ge\KL_a$ while $\KL(\mathbb P\Vert E)=\KL_a+\KL_{s\mid a}$. Coordinator check over 300 random laws: no violation, maximum of index minus bound $-4.8\times10^{-7}$; negative control with attention tilts allowed exceeds the bound in 24/300. In I*, uniform attention habits give $\KL_a=16.63$ nats against $\KL_{s\mid a}\approx0.14$, index 0.008; habits concentrated enough for index 0.9 make $N_{\mathrm{hab}}$ select niche A (`open_agy_meta_agent_exists-checks/round2_attack_persistent/run7_out.txt`).
- Depends on: none

### C13: Private-sensor niche under the strictest agency readings (instance I**)

- Statement: Instance I** is C11's architecture with each public slot replaced by a private optional sensor ($R_s=2$) that its owner reads and relays raw with one-round latency to every agent attending the owner; message attention is over sets of at most 3 of the 7 relays, $\kappa=5$, slot cost $\psi=0.030$, $\gamma=400$, uniform product habits. Under the per-round law of `def:fw-system`, which here equals (P4) at a frozen state because each member's expected free energy ignores its co-members' simultaneous choices (proved), niche A is a meta-agent of grade $(7.9,0.02,0.09,0.01,0.074)$ with $n_{\mathrm{null}}=999$, with the index over full policies (attention and sensors), uniform habits held fixed, class G1, and either clause (c) baseline; over sensors only the index is 0.998. There are no acts, so O2(a) and O2(f) do not bear on it.
- Status: computed
- Review: fresh-context
- Evidence: $r(A)=8.4207\pm0.0031$; mechanism medium 6.006, mean coupling 7.361; other regions at most 2.30; $N_{\mathrm{hab}}$ 2.383; annealed $N_{\mathrm{pr}}$ 2.844 with test maximum 3.230 over 999 draws, $p=0.001$; $N_{\mathrm{lp}}$ and $N_{\mathrm{fr}}$ diagonal (proved); inference 0.0594; exact Markov defect at most 0.0162 on every pattern searched; index 0.0748 (full), 0.9979 (sensors). Files: `open_agy_meta_agent_exists-checks/round3_strict-construction/lib3.py`, `open_agy_meta_agent_exists-checks/round3_strict-construction/d1_frozen_out.txt`, `open_agy_meta_agent_exists-checks/round3_strict-construction/d6_frozen_out.txt`; attack `open_agy_meta_agent_exists-checks/round3_attack-strict-construction/a5_out.txt`, `open_agy_meta_agent_exists-checks/round3_attack-strict-construction/a6_out.txt`.
- Scope: one instance; exact second moments per pair of policy paths over 160 pairs; a ±1% box over 8 parameters at 18 points; memory supremum by search only.
- Check: 2026-11-21, an attack agent reproduced every deciding number with independent code ($r(A)=8.4287\pm0.0031$); survives; corrections: the supremum of the exact Markov defect lies in $[0.0162,0.0988]$, so $\alpha_{\mathrm M}=0.02$ is consistent but not certified; G2 is inadmissible; the full-policy value 0.0748 needs pinned slot preferences and a zero-variance group belief on outsider content (outsider relays treated as slots with a free cost give 0.537); $N_{\mathrm{fg}}$ and drawn-once partner randomization are not computed.
- Depends on: C1, C12, O2(g), O2(h), O2(i), O2(j)

### C14: Components whose departure the class explains raise the full-policy index (design D1)

- Statement: (Proposition P) With habits fixed and $G_C$ depending on slots only, $\Agency=(\KL_{s\mid a}-\mathrm{mis}_s)/(\KL_a+\KL_{s\mid a})$, with $\mathrm{mis}_s$ the slot misfit, so components whose departure from habits the class explains drive the index toward 1 at fixed $\KL_a$. (D1) Two niches of two agents ($F=0.9$, $Q=0.05$, $R=1$, $R_c=0.1$), message capacity 1 over $\{\varnothing,\text{mate},o_1,o_2\}$, eight private slots per member ($R_s=10$, cost 0.06702, never opened), $\gamma=400$: niche A meets every clause at $(3.7,0.02,0.03,0.01,0.75)$ with full-policy index 0.8000, provided attention to non-members' relays counts as internal (or the group variance on their content is at most $1.2\times10^{-3}$), costly components that are never used count (O2(k)), and partner randomization is redrawn every round.
- Status: computed
- Review: fresh-context
- Evidence: $r(A)=4.345220$, mechanism medium 2.493156, mean coupling 3.230; $N_{\mathrm{hab}}$ 1.346, $N_{\mathrm{pr}}$ 1.761, $p=0.001$; Markov defect $4.4\times10^{-5}$; inference 0.0187; $\KL_a=2\ln4$, $\KL_{s\mid a}=16\ln2$; ±5% box 17/17. Files: `open_agy_meta_agent_exists-checks/round3_agency-frontier/d1_contrast_out.txt`, `open_agy_meta_agent_exists-checks/round3_agency-frontier/d1_npr_test_out.txt`, `open_agy_meta_agent_exists-checks/round3_agency-frontier/d1_agency_out.txt`; attack `open_agy_meta_agent_exists-checks/round3_attack-agency-frontier/a4_out.txt`, `open_agy_meta_agent_exists-checks/round3_attack-agency-frontier/a5_out.txt`.
- Scope: one instance, exact Lyapunov algebra; Proposition P proved by the chain rule as in C12.
- Check: 2026-11-21, an attack agent recomputed every deciding number; under the literal $\eta_C$ with group variance at least 0.5 on outsider content the index is exactly 0 (C16); drawn-once partner randomization fails exactly, $P(S\ge S_0)=1/9$; the attention-surprise floor (Theorem A of the frontier report) holds only for $n=2$ with symmetric habits.
- Depends on: C12, C16, O2(g), O2(h), O2(j), O2(k)

### C15: Audience meta-agent formed through a non-member source (P0, P1)

- Statement: Instance P0: one AR(1) component ($F=0.9$, $Q=0.05$); a non-member source $S$ with its own sensor ($R_S=0.01$) that attends nothing; four audience members with $R=1$; every agent broadcasts its raw reading with one-round latency and receiver-specific $R_c=0.002$; each member draws one of $\{\varnothing,\{S\},\{m_1\},\{m_2\},\{m_3\}\}$ by expected free energy with uniform habits and $\gamma=40$; exact filters on $(\eta_t,\eta_{t-1})$ with computation noise $10^{-4}$. The audience $A$ is a meta-agent of grade $(4.5,0.071,0.03,0.01,0.99)$ with $n_{\mathrm{null}}=999$, and of grade $(4.5,0.03,0.03,0.01,0.99)$ when the noise-only stationary law is declared as the initial law of the memory clause; both hold under every combination of O2(a), (e), (f) and under either clause (c) baseline. P1 (message capacity 2, so members also hear one another) passes at $(4.45,0.03,0.03,0.01,0.99)$ with $\Omega_{\mathrm{int}}(A\mid\zeta_S)>0$, main quantities only.
- Status: computed
- Review: fresh-context
- Evidence: closed form (Proposition A, re-derived by the attack) $r(A)=1-c/\sigma+n\beta'/\alpha$, $\beta'=\beta-c^2/\sigma$, giving 5.384864; the best other region, $A\cup\{S\}$, has 2.326; mean coupling 3.8167, mechanism media at most 3.9301; $N_{\mathrm{hab}}$ 1.456; $N_{\mathrm{pr}}$ 1.541 with $p=0.002$; $N_{\mathrm{lp}}$, $N_{\mathrm{rn}}$, $N_{\mathrm{fr}}$ diagonal and $N_{\mathrm{eff}}$, $N_{\mathrm{inf}}$, $N_{\mathrm{ex}}$ inapplicable (proved); inference 0.02509; Markov defect 0.025717 (noise-only stationary initial law), 0.037477 (deterministic start), 0.070909 (members' stationary law); index $1-O(10^{-13})$; all 128 corners of a ±5% $2^7$ design pass every exactly computed clause. Files: `open_agy_meta_agent_exists-checks/round3_audience/aud.py`, `open_agy_meta_agent_exists-checks/round3_audience/check1_out.txt`, `open_agy_meta_agent_exists-checks/round3_audience/check9_test_out.txt`; attack `open_agy_meta_agent_exists-checks/round3_attack-audience/a1_out.txt`.
- Scope: exact Lyapunov algebra for P0; nulls by pair algebra over 200 policy-path pairs; P1 by Monte Carlo.
- Check: 2026-11-21, an attack agent rebuilt P0 from its specification and reproduced every deciding number; survives; the stated $\alpha_{\mathrm M}=0.03$ needs the initial law declared; the source is in no collective (O2(n)); the members interact only through $S$, $\Omega_{\mathrm{int}}(A\mid\zeta_S)$ vanishing except on events of probability $2\times10^{-14}$ per member-round (O2(m)); P1's member links add no contrast (5.375 against 5.3849); conditioning on the source's sensing noise gives $r=1.000000$ (O2(h)).
- Depends on: C1, C16, O2(g), O2(h), O2(i), O2(m), O2(n)

### C16: Index of a deterministic joint policy

- Statement: Fix habits $E$ and the group belief, take $\gamma_C\ge0$, and let the actual law be $\delta_{\pi^\ast}$. Then $f(\gamma_C)=\ln\mathbb P_g(\pi^\ast)$ is concave with $f'=\E_{\mathbb P_g}[G_C]-G_C(\pi^\ast)$; (a) if $\pi^\ast$ uniquely minimizes $G_C$ the index tends to 1; (b) if $G_C(\pi^\ast)\ge\E_E[G_C]$ the index is 0. Under the literal $\eta_C$ (`05_agency.tex:11`), case (b) covers members who avoid exterior channels whose content their own models ignore when the group belief on that content has calibrated variance.
- Status: proved
- Review: fresh-context
- Evidence: two-niche audience variant, index 0.0000 (`open_agy_meta_agent_exists-checks/round3_audience/check12_out.txt`); D1 with outsider variance at least 0.5, index 0 (`open_agy_meta_agent_exists-checks/round3_attack-agency-frontier/a4_out.txt`).
- Check: 2026-11-21, the attack on C15 re-derived $f'$ and $f''$; agrees.
- Depends on: none

### C17: The effect null separates only explaining-away structure (Lemma M, Theorem O)

- Statement: (Lemma M) $N_{\mathrm{eff}}$ keeps the members' act feedback and removes only what the world path tells about their private inputs: $\Sigma^c_{\mathrm{eff}}-\Sigma^c=S\Cov(\E[z_0\mid\tilde y])S^\top\succeq0$. (Theorem O) If $C$ ($n\ge2$, scalar coordinates) is uncorrelated with $V\setminus C$ and exchangeable under $N_{\mathrm{eff}}$, with act loadings of disagreement rank below $n-1$, then either $\Pi^c$ is not diffusive or $r(C)\le r_{\mathrm{eff}}(C)$, so $C$ never differs from $N_{\mathrm{eff}}$. (Proposition E) Acts consistent with expected free energy under a common preference load all members' errors about one component with one sign. (Proposition D) A null that keeps the acts gives uncorrelated interchangeable members with nonzero loadings $\Sigma^c_{ij}<0$, so that null is not diffusive.
- Status: proved
- Review: self
- Evidence: `open_agy_meta_agent_exists-checks/round3_performative-strict/check9_out.txt`; attack `open_agy_meta_agent_exists-checks/round3_attack-performative-strict/a6_out.txt` (no violation in 445 diffusive draws with $n=3,4$; the $n=2$ mixed-sign control detects gains up to 16.8 times; Lemma M holds on C18). The case $n=2$ with same-sign unequal loadings lies outside the theorem (0 gains in 280 and 228 diffusive draws, conjecture).
- Depends on: C1, C4, C7 (C8 is the special case of setting P)

### C18: Correlated-component pair, a performative meta-agent under strict typing

- Statement: Two firms with independent worlds; in each, member $b$ senses $\eta^a$ and member $s$ senses $\eta^b$ (AR(1), $F=0.9$, $Q=0.05$, innovation correlation 0.5, $R=1$); both model $(\eta^a,\eta^b)$, read each other's raw reading ($R_c=0.1$), and act by rule D2 on a renewed outcome $\eta^Z_{t+1}=\eta^a_t-\eta^b_t+u_b+u_s+w^Z$ under a common preference ($\gamma=70$, habits $\Ncal(0,1/30)$, act noise 0.01, $\kappa=0.7$), with fixed attention. With each member's prior error on its own component as contrast coordinate and the clause (c) mean-coupling baseline, each firm is a meta-agent of grade $(3.75,0.02,0.05,0.01,0.25)$ with $N_{\mathrm{eff}}$ and $N_{\mathrm{inf}}$ of type D, taking the group belief from the end-of-round coarse state (index 0.265; 0.128 from the start-of-round state).
- Status: computed
- Review: fresh-context
- Evidence: $r(\text{pair})=4.3336$, baseline 3.2224; $N_{\mathrm{eff}}=N_{\mathrm{hab}}$ 1.809; $N_{\mathrm{lp}}$, $N_{\mathrm{rn}}$, $N_{\mathrm{fr}}$ at most 1.852 under every convention computed; annealed $N_{\mathrm{pr}}$ 2.049, test maximum 2.539 over 999 draws, $p=0.001$; Markov defect at most $1.5\times10^{-4}$; inference 0.0317. Files: `open_agy_meta_agent_exists-checks/round3_performative-strict/lgx2.py`, `open_agy_meta_agent_exists-checks/round3_performative-strict/check14_out.txt`, `open_agy_meta_agent_exists-checks/round3_performative-strict/check16_out.txt`; attack `open_agy_meta_agent_exists-checks/round3_attack-performative-strict/a1_out.txt`, `open_agy_meta_agent_exists-checks/round3_attack-performative-strict/a7_out.txt`.
- Scope: exact conditioning on world-path windows; a 64-point ±1% Latin hypercube shares the window $(3.3212,4.1893]$; no common level on ±5%.
- Check: 2026-11-21, an attack agent found that it survives under the candidate's readings with margin 0.015; common contrast coordinates fail (R8); drawn-once partner randomization fails (17/81); read literally, `04_collectives.tex:187` leaves contrast undefined here because the agent blocks deviate from a multiple of $I_2$ by 0.0237 (O2(o)); the prior-corrected log pool fails $\alpha_{\mathrm I}$ (0.120).
- Depends on: C17, rule D2, the continuous-act extension of the index, O2(c), O2(g), O2(h), O2(o), O2(q)

### C19: Continuity of I*'s stationary policy-covariance law

- Statement: For the I* architecture (specified in C11; C19 uses the specification, not C11's result) with $\theta=(F,Q,R,R_c,R_s,\psi,\gamma,q_c)$ in an open set with $F<1$ and $0\le\gamma<\infty$, under both deliberation protocols, together with its mechanism medium and the nulls $N_{\mathrm{hab}}$, $N_{\mathrm{pr}}$ (every round), $N_{\mathrm{lp}}=N_{\mathrm{rn}}$ and $N_{\mathrm{fr}}$: the chain (policy, Kalman covariance) has a unique stationary law, reached geometrically in a Wasserstein distance and continuous in $\theta$ with modulus $O(\omega\log(1/\omega))$; $\Sigma^c(\theta)$ is continuous, $\Sigma^c\succeq q_cI$, and $\Sigma^c=\mathrm{blockdiag}(\alpha I_4+\beta\one\one^\top,\alpha I_4+\beta\one\one^\top)$ exactly; $r(A)$, both clause (c) baselines, every null contrast and the index at fixed declared decision states are continuous, so the sets on which the differ clause holds are open.
- Status: proved
- Review: self
- Evidence: Doeblin minorization on the finite policy component; Riccati contraction with derivative at most $(F/(1+Q'/R))^2=0.7346$; rank-one closed loop with factor at most 0.857; that $\theta^\ast$ lies inside these sets is numerical (smallest margin 77 standard errors). Files: `open_agy_meta_agent_exists-checks/round3_continuity/check_b_out.txt`, `open_agy_meta_agent_exists-checks/round3_continuity/check_c3_out.txt`.
- Depends on: C1

## Failed routes

### R1: The two-firms example as a meta-agent

- Tried: `ex:met-two-firms`, which meets `thm:met-h5a`.
- Failed because: its world-conditional precision is not diffusive (price collider between the two firms; singular lazy-ring consensus matrix), so contrast is undefined and the collective clause fails (`rem:agy-h1-status`, computed; mechanisms now proved in C3a to C3c and C6).
- Reopen if: one firm stops acting on the price, the firms act with opposite signs (diffusive with collectives at 77.19 and 95.77 against a baseline of 75.07, other clauses unchecked), or contrast is defined for non-diffusive precisions.

### R2: Symmetric slot reading through channels

- Tried: every member, the owner included, reads each slot through a receiver-specific channel, so that every realization is symmetric.
- Failed because: the slot's noise is then a channel noise shared by several receivers, which `def:col-world-conditional` conditions on; at a deterministic profile $r=1$.
- Reopen if: never under the current definition; the coupling needs an agent's own sensing noise as a relayed private input.

### R3: Quenched partner randomization scored by convention

- Tried: partner randomization drawn once, scoring non-diffusive draws as selecting nothing.
- Failed because: quenched draws are non-diffusive (995/999, and 400/400 in the attack), contrast is then undefined, and the manuscript's substitute selector for undefined contrast (ratio of within- to between-block mutual information, `s05_agency.tex:252`) gives $+\infty$ in the full model and every draw, so $p=1$.
- Reopen if: a selector for non-diffusive precisions is defined (`open:col-non-diffusive`); meanwhile partner randomization redrawn every round, which `tab:agy-nulls` permits, is used.

### R4: Two precisions and the episode clock

- Tried: attention at $\gamma_{\mathrm{att}}=\infty$ with slots at $\gamma=4$, in a world renewed every two rounds.
- Failed because: `def:fw-system` draws all active states with one $\gamma$; with $\gamma=4$ for both the window is empty ($r(A)=6.513$ against 8.584). The single-$\gamma$ repair (C2) passes, but the episode clock remains outside the time-invariant framework, and under the default prior-error convention $\Sigma^c$ is diagonal at every round.
- Reopen if: the author admits episodic worlds; otherwise O1.

### R5: Public slots as world channels

- Tried: optional slots made public world channels read by every niche member (C11), so that every realization is exchangeable.
- Failed because: opening a channel for others is none of attention, speech or record writing in `def:fw-system` (`02_framework.tex:13`), so it reads as a performative act; then $N_{\mathrm{eff}}$ and $N_{\mathrm{inf}}$ are applicable, and C11 passes only under the conditional typing of `tab:agy-nulls`.
- Reopen if: the author rules that opening an instrument is not an act; otherwise use private slots (the owner senses, then relays), at the cost of exchangeability in each realization.

### R6: A two-dimensional coarse variable

- Tried: the average of the members' prior-mean vectors on $(\eta_t,\eta_{t-1})$, which is exactly closed.
- Failed because: $\eta_C$ is the exterior variable the sensory states read, $\eta_t$ (`05_agency.tex:11`), so `def:agy-closure`(ii) admits only scalar declarations; the vector average is the $A^\top$-invariant summary that the constraint excludes (`05_agency.tex:27`), and against the union posterior on $(\eta_t,\eta_{t-1})$ its inference defect is 0.171.
- Reopen if: never; the scalar average passes (C11).

### R7: Private sensors at C11's slot cost

- Tried: I** at $\psi=0.024$.
- Failed because: the mechanism medium (8.16) exceeds $r(A)$ (7.82) (`open_agy_meta_agent_exists-checks/round3_strict-construction/d8_out.txt`).
- Reopen if: never; $\psi=0.030$ passes (C13).

### R8: Common contrast coordinates for the correlated-component pair

- Tried: one shared direction of $(\eta^a,\eta^b)$ as both members' contrast coordinate in C18.
- Failed because: every direction either puts $N_{\mathrm{eff}}$ inside the window or empties it; at 45 degrees $N_{\mathrm{eff}}=5.2605$ lies in $(4.5763,6.3644]$.
- Reopen if: O2(o) rules out member-specific coordinates and a third coordinate choice appears.

### R9: Opposite-preference pairs

- Tried: pairs acting on one component with opposite preference maps.
- Failed because: every null differs, but the index is 0 in three fixed-habit classes (`open_agy_meta_agent_exists-checks/round3_performative-strict/check12_out.txt`; not attacked).
- Reopen if: classes without fixed habits are admitted.

### R10: Two-department firm

- Tried: two departments of two members per firm with opposite outcome loadings.
- Failed because: its deletion nulls and annealed partner randomization are non-diffusive (C17, Proposition D), so it passes only if such a null selects nothing, which R3 rejects (`open_agy_meta_agent_exists-checks/round3_performative-strict/check4_out.txt`; not attacked).
- Reopen if: `open:col-non-diffusive` supplies a selector.

### R11: Pure-collider pair

- Tried: two single-agent departments without channels acting on one outcome.
- Failed because: partner randomization leaves the model unchanged, so no level $\alpha_{\mathrm{pr}}$ can be stated, while the open problem asks for partner randomization at a stated level; $\Omega_{\mathrm{int}}(C\mid\zeta_{V\setminus C})=0$.
- Reopen if: the author rules that an inapplicable partner randomization imposes no requirement, that $\Omega_{\mathrm{int}}$ is only reported (O2(m)), and that the fixed within-firm couplings are not a declared interaction graph (O2(c)). The first ruling is already written in `def:agy-nulls` (`05_agency.tex:333`): a null whose intervention leaves the model unchanged "imposes no requirement", while `def:agy-meta-agent` names $N_{\mathrm{pr}}$ apart from "every applicable null". Under all three readings the round-3 investigator computed the grade $(2.29,0.02,0.01,\text{inapplicable},0.50)$ with a ±1% box (`open_agy_meta_agent_exists-checks/round3_performative-strict/check7_out.txt`, `open_agy_meta_agent_exists-checks/round3_performative-strict/check9b_out.txt`): $r(\text{pair})=2.574$ against the mean-coupling baseline 2.049, $N_{\mathrm{eff}}$ and $N_{\mathrm{hab}}$ at $r=1$, $d_M=0$, index 0.515 under rule D2, every other null inapplicable. The investigator called it a definitional loophole, since the two members never interact; the attack disputed only the $N_{\mathrm{pr}}$ reading and did not recompute it.

### R12: Several ignored exterior options under the literal $\eta_C$

- Tried: members able to attend several non-member channels whose content their models ignore (D1's outsiders; a two-niche audience).
- Failed because: a calibrated group belief makes the group's expected free energy prefer the channels the members avoid, so the index is 0 (C16).
- Reopen if: O2(j) admits a zero-variance group belief, free slot preferences, or outsider relays as internal attention.

### R13: Drawn-once partner randomization in small populations

- Tried: drawn-once partner randomization on C14, C15 and C18.
- Failed because: when the full attention pattern is itself a possible draw, $P(S\ge S_0)$ is bounded below (C14: 1/9; C18: 17/81), and otherwise the draws are non-diffusive (P0: 202/256) (`open_agy_meta_agent_exists-checks/round3_attack-agency-frontier/a5_out.txt`, `open_agy_meta_agent_exists-checks/round3_attack-performative-strict/a7_out.txt`, `open_agy_meta_agent_exists-checks/round3_audience/check11_out.txt`).
- Reopen if: populations grow (about 25 firms for C18, attack estimate).

### R14: Random-coefficient Riccati contraction for the continuity proof

- Tried: Bougerol (1993).
- Failed because: it needs nonsingular, exogenous coefficients, while in I* the transition matrix is singular and the policies are fed back; C19 uses direct coupling instead.
- Reopen if: never for I*.

### R15: Certifying memory by the closure defect

- Tried: bounding the Markov defect by the per-step closure defect.
- Failed because: the closure defect overstates the Markov defect by orders of magnitude (I**'s worst pattern: $2.66\times10^{-2}$ against an exact $2.4\times10^{-5}$) (`open_agy_meta_agent_exists-checks/round3_attack-strict-construction/a5_out.txt`, `open_agy_meta_agent_exists-checks/round3_attack-agency-frontier/a9_out.txt`).
- Reopen if: never; compute the exact defect.

### R16: Deterministic best response in I*

- Tried: $\gamma=\infty$.
- Failed because: the one-slot profiles are absorbing and the stationary law is not unique (0/50 couplings, `open_agy_meta_agent_exists-checks/round3_continuity/check_b_out.txt`).
- Reopen if: never; keep $\gamma$ finite.

## Open obligations

- [ ] O2 (sessions: 3): reading decisions that belong to the author. (g) and (h) decide existence; (i) decides every construction without acts; (m) and (n) decide C15. The recommendations are interpretive, and each confidence is the round-3 readings investigator's estimate of the author's intent.
  - (a) The type of $N_{\mathrm{eff}}$ and $N_{\mathrm{inf}}$ for a collective said to form by communication whose members also act (decides C8 against C9, and R5). Recommended (a2), confidence 0.8: typed as the table words them (`05_agency.tex:348-349`), with what the collective is said to form by declared with the grade; C11 then passes and R5 is not decisive. Opening a public slot is not an act (0.55; the literature investigator disagrees).
  - (b) Whether an index of one reached because no policy is selected by expected free energy counts. Recommended: it does not (`s05_agency.tex:296`, 0.85); requiring $\sum_X\mathsf w_X\KL(\mathbb P(\cdot\mid X)\Vert E)>0$ excludes it, and no construction relies on it.
  - (c) Whether a fixed attention schedule declares an interaction graph. Recommended: it does (`s04_collectives.tex:147`, 0.6); among the constructions it affects C18, which fails, and the pure-collider pair of R11, whose fixed within-firm couplings make the clause (b) medium equal to the model, so its window is empty.
  - (d) Whether episodic worlds and filtered errors are admissible. Recommended: filtered errors when declared (0.7), episodic worlds outside the class (0.65); C2 then does not settle the problem.
  - (e) Whether "the members' joint policies" in `def:agy-agency-index` include attention to internal channels. Recommended: the exterior-facing components only, slots and interventions (`05_agency.tex:157`, 0.75). Under full policies C15 still passes (C13 0.074, C11 about 0.008).
  - (f) Whether (P4) at a frozen decision state is admissible alongside one-round latency. Recommended: admissible (`05_agency.tex:161`, `s10a_meta_agents.tex:143`, 0.8). It bears only on C11, since in C13, C14 and C15 each member's expected free energy ignores its co-members' simultaneous choices (proved), so the two protocols give one law.
  - (g) Whether drawn-once partner randomization must also be passed (R13; no construction passes it). The text does not decide it: the table offers "once or every round" (`05_agency.tex:350`) and `def:agy-nulls` speaks of "the random null", which reads as a declared choice, while `ext2_rfm.tex:140` records the drawn-once variant as "not covered" after passing the every-round one.
  - (h) Whether an agent's relayed own sensing noise stays private (Conventions; rejecting it leaves no construction with relays established). Lead agent's textual reading (2026-11-22, interpretive): private, by `04_collectives.tex:15` and `prop:col-world-conditional` (Conventions row). The purpose clause "so that the remaining local noise is specific to each receiver" (`04_collectives.tex:131`) then holds, because a sensing noise enters only its owner's sensory state and reaches listeners through the channel content it writes.
  - (i) Whether the index applies to models whose only policies are attention sets (`def:agy-group-model` against `ext2_rfm.tex:139,167`); rejecting it removes C13, C14, C15, and C11 unless opening a slot is an act. Lead agent's textual reading (interpretive): it applies, since `def:agy-group-model` defines policies as slot openings and `ex:agy-no-data-sharing` and `ex:agy-unrepresented-driver` apply the index to epistemic slots. `ext2_rfm.tex:139` declares the index inapplicable to a model whose readers choose attention sets by a $\gamma$-softmax (`ext2_rfm.tex:11`) on the ground that it has no acts, while `def:agy-nulls` names only $N_{\mathrm{eff}}$ and $N_{\mathrm{inf}}$ as inapplicable without acts; the manuscript contradicts itself here, and one of the two statements must change whichever way the author rules.
  - (j) The literal $\eta_C$, which includes the active channels of non-members that the members hear (`05_agency.tex:11`); see C16, R12, O8.
  - (k) Whether costly components that are never used count in the index (C14).
  - (l) The initial law of the memory clause's input-conditional form (C15: 0.0257 to 0.0709; O7).
  - (m) Whether $\Omega_{\mathrm{int}}(C\mid\zeta_{V\setminus C})>0$ is required or only reported (`05_agency.tex:380` against `:294`); C15's members interact only through the source. The definition's text reports it only. Requiring it removes the pure-collider pair of R11 (members causally separated) and leaves P0 only through events of probability about $2\times10^{-14}$ per member-round; a requirement of substantive interaction makes P1 the candidate (O13).
  - (n) The selector output when an agent belongs to no collective (`04_collectives.tex:219`); C15's source does not.
  - (o) Whether member-specific contrast coordinates are admissible for vector errors (`04_collectives.tex:187`; C18, R8).
  - (p) Clause (c)'s exchangeable population for distinct agent types (`04_collectives.tex:202`); moot under mean coupling.
  - (q) Whether the declared group belief may read the coarse state at the end of the round (`05_agency.tex:157`; C18 falls from 0.265 to 0.128 at the start of the round).
  - Two readings the round settled as recommendations: any positive declared $\Agency_0$ settles the problem as worded (`s05_agency.tex:296`, 0.85), and "each constant of the selector" means each $r_0$ in the admissible window, since read over all constants the differ clause fails for every population (above $r(C)$ the model and the null both select nothing).
- [ ] O3 (sessions: 2): fresh-context checks of C6 and C10, which are self-reviewed.
- [ ] O7 (sessions: 1): compute the input-conditional Markov defect of C11, C13, C14 and P1 under three initial laws (the noise-only stationary law, a deterministic start, the members' stationary law), and certify C13's supremum, now in $[0.0162,0.0988]$, by interval arithmetic.
- [ ] O8 (sessions: 1): compute the indexes of C11 and C13 with the other niche's relays as slots, under pinned preferences (with zero-variance and with calibrated beliefs) and under free preferences; compute C11 under the literal per-round law.
- [ ] O9 (sessions: 1): drawn-once partner randomization for C11, C13 and P1, and the substitute selector on P0's non-diffusive draws; $N_{\mathrm{fg}}$ for C13; independent recomputation of P0's mechanism media and of P1's medium (4.112) and box.
- [ ] O10 (sessions: 1): verify the hypotheses (H1) to (H6) of C19 for C13, C15 and C18, and obtain rigorous enclosures of C11's center values.
- [ ] O11 (sessions: 1): if O2(k) excludes components that are never used, compute the frontier with used, relayed slots; close step 3 of the frontier report's Theorem A for asymmetric habits and prove its monotonicity hypothesis for $n\ge3$.
- [ ] O12 (sessions: 1): build a C18 population of about 25 firms for drawn-once partner randomization, and heterogeneous firms that escape clause (b).
- [ ] O13 (sessions: 1): certify every clause of P1, whose members also hear one another ($\Omega_{\mathrm{int}}>0$) and which carries existence if O2(m) requires substantive member interaction; give the source a collective of its own (for example two sources that read each other) so that O2(n) no longer bears on the audience construction.
- [ ] O4 (sessions: 2): extend C3a to stored acts used in filters and to act loadings of rank above one, so that it covers `ex:met-two-firms` literally.
- [x] O1 (sessions: 2): exhibit the epistemic construction in the time-invariant framework. Done under readings (C11).
- [x] O5 (sessions: 3): construct niches under the strictest readings (O2(a) strict, O2(e) full policies). Discharged by C13 (full-policy index 0.074) and C15 ($1-O(10^{-13})$), both under O2(g), O2(h), O2(i).
- [x] O6 (sessions: 3): continuity of the stationary policy and covariance law for C11. Discharged by C19; the other constructions are in O10.

## Literature

| Claim | Source | Locator | Read depth | Date read | Verdict |
| --- | --- | --- | --- | --- | --- |
| Gaussian MTP2 iff the precision is an M-matrix | Karlin and Rinott, Linear Algebra Appl. 52-53 (1983), doi:10.1016/0024-3795(83)80027-5 | abstract | abstract | 2026-11-21 | supports C1, C4 (sign part) |
| MTP2 closed under conditioning and marginalization; independence model upward-stable | Fallat, Lauritzen, Sadeghi, Uhler, Wermuth, Zwiernik, Ann. Statist. (2017), doi:10.1214/16-AOS1478 | Prop. 3.4, Thm 5.3, Sec. 4.1 | full text (arXiv v2) | 2026-11-21 | structural form of C3a |
| Positive one-factor model has a complete M-matrix precision | Wermuth and Marchetti, Electron. J. Statist. 8 (2014), doi:10.1214/14-EJS884 | Lemma 1, eq. (6) | pages 1-8 | 2026-11-21 | prior art for the sign part of C1 |
| Signed MTP2 iff every cycle is balanced | Lauritzen, Uhler, Zwiernik, Ann. Statist. 47 (2019), doi:10.1214/17-AOS1668 | Thm 5.2, p. 22 | pages 1-8, 19-28 | 2026-11-21 | no sign gauge rescues `ex:met-two-firms` (D2) |
| Schur complements of M-matrices are M-matrices | Carlson and Markham, Czech. Math. J. 29 (1979) | Sec. 2, Thm 1 | full text | 2026-11-21 | supports C4 |
| Kron reduction preserves loopy Laplacians | Dörfler and Bullo, IEEE TCAS-I 60 (2013), doi:10.1109/TCSI.2012.2215780 | Lemma 2.1 (arXiv) | pages 1-6 | 2026-11-21 | prior art for `lem:col-kron` |
| Conditioning on a common child induces covariance $-ab$ | Chen and Pearl, UCLA TR R-432 (2014) | Fig. 6a discussion | partial | 2026-11-21 | static sign of C3 |
| Common effects give edges of unexpected sign | Epskamp, Waldorp, Mõttus, Borsboom, Multivariate Behav. Res. 53 (2018), doi:10.1080/00273171.2018.1454823 | note on common effects | partial | 2026-11-21 | static sign of C3 |
| Conditional mutual-information utilities form an exact potential game | Choi and Lee, IEEE Trans. Control Syst. Technol. (2015), doi:10.1109/TCST.2015.2403475 | Lemma 1 | Secs. II-A, IV-A | 2026-11-21 | prior art for the epistemic part of `thm:agy-agency`(d), not cited in the manuscript |
| Blanket existence as the criterion of collective agency | Kirchhoff, Parr, Palacios, Friston, Kiverstein, J. R. Soc. Interface 15 (2018), doi:10.1098/rsif.2017.0792 | Secs. 3-5 | full text | 2026-11-21 | prior art; weaker criterion |
| Group agency as a non-trivial agent in a causal abstraction | Jørgensen, Weichwald, Hammond, CLeaR 2026, arXiv:2605.00248 | Defs. 11-12, Prop. 16 | Secs. 1-4.2 | 2026-11-21 | closest graded, class-restricted test |
| Information choices inherit the complementarity of actions | Hellwig and Veldkamp, Rev. Econ. Stud. 76 (2009), doi:10.1111/j.1467-937X.2008.00515.x | Prop. 1 | abstract and Prop. 1 | 2026-11-21 | prior art for the remark after `prop:agy-performative-sign` |
| The index's numerator equals maximum entropy goal-directedness | MacDermott, Fox, Belardinelli, Everitt, NeurIPS 2024, arXiv:2412.04758 | Def. 3.2, Props. 3.2-3.3, Sec. 7 | pages 1-10 | 2026-11-21 | closest prior art, uncited; MEG ignores irrelevant decisions, while the normalized index dilutes (C12) |
| KL fraction explained, nondecreasing in regressors | Cameron and Windmeijer, J. Econometrics 77 (1997), doi:10.1016/S0304-4076(96)01818-0 | eq. (5), Props. 1-2 | preprint, parts | 2026-11-21 | precedent for the index's form |
| Rescaling by the attainable maximum | Nagelkerke, Biometrika 78 (1991), doi:10.1093/biomet/78.3.691 | eq. (3) | full text | 2026-11-21 | precedent for correcting C12's dilution |
| Gibbs law of asynchronous logit revision | Blume, Games Econ. Behav. 5 (1993), doi:10.1006/game.1993.1023 | Sec. 6.1, pp. 408-409 | page images | 2026-11-21 | primary locator for `05_agency.tex:208`; supports O2(f) |
| The Gibbs form is specific to the revision protocol | Alós-Ferrer and Netzer, Games Econ. Behav. 68 (2010), doi:10.1016/j.geb.2009.08.004 | Prop. 1, Thms 1-2 | working paper, parts | 2026-11-21 | other protocols give only stochastic stability |
| State-based games | Liu, Wang, Cheng, arXiv:1608.00192 | Defs. 18-20, Thm 21 | parts | 2026-11-21 | no group-posterior law under real-time deliberation |
| The group agent's blanket is its members' sensory and active states | Waade et al., Entropy 27 (2025), doi:10.3390/e27020143 | Sec. 2.3 | pages 5-10 | 2026-11-21 | supports O2(e) |
| The collective decision is the actor's action, with the critic marginalized | Jørgensen, Weichwald, Hammond, CLeaR 2026, arXiv:2605.00248 | Sec. 4.3, Prop. 17 | Sec. 4.3 | 2026-11-21 | supports O2(e) |
| The output map is the action | Biehl and Virgo, IWAI 2022, arXiv:2209.01619 | Defs. 2-3, 5 | pages 1-8 | 2026-11-21 | supports O2(e) |
| Behavior is action on the environment; conditioning on interventions | Bertschinger, Olbrich, Ay, Jost, BioSystems 91 (2008), doi:10.1016/j.biosystems.2007.05.018 | Sec. 2, eqs. (7), (9), (15) | parts | 2026-11-21 | supports O2(e); precedent for conditioning $\Omega_{\mathrm{int}}$ on the shared drive; in the bibliography but uncited |
| Attentional policies are covert actions | Sandved-Smith et al., Neurosci. Conscious. (2021), doi:10.1093/nc/niab018 | Fig. 4 | parts | 2026-11-21 | against O2(e) at the member level |
| Epistemic actions modify the world to change input | Kirsh and Maglio, Cogn. Sci. 18 (1994), doi:10.1207/s15516709cog1804_1 | pp. 513-515 | parts | 2026-11-21 | against O2(a1), interpretive |
| A null removes one mechanism | Gotelli and Graves, Null Models in Ecology (1996) | pp. 3-4 | secondary | 2026-11-21 | supports O2(a2); secondary, not read in the primary |
| Segregation over any partition among identical Bayesian listeners | Sethi and Yildiz, Econometrica 84 (2016), doi:10.3982/ECTA13320 | Prop. 2(c) | parts | 2026-11-21 | a route to partitions that $N_{\mathrm w}$ does not predict |
| Random-coefficient Riccati contraction | Bougerol, SIAM J. Control Optim. 31 (1993), doi:10.1137/0331041 | Thms 1.7, 2.4, 2.6 | pages 942-953 | 2026-11-21 | not applicable to I* (R14) |
| Iterated function systems with place-dependent probabilities | Barnsley, Demko, Elton, Geronimo, Ann. Inst. H. Poincaré Probab. Statist. 24 (1988) | Thm 2.1 | abstract and statement | 2026-11-21 | covers the fast protocol, not real time; no continuity in parameters |

## Searches

| Query | Tool | Date | Not searched |
| --- | --- | --- | --- |
| Gaussian MTP2, M-matrix precision, closure under conditioning | Exa web search, scholar read_paper | 2026-11-21 | Karlin and Rinott 1980 full text, Crabtree 1966 |
| Gaussian explaining away, collider sign | Exa web search | 2026-11-21 | Berkson 1946, Pearl 1988, Wellman and Henrion 1993 |
| collective agency, blanket of blankets, active inference 2018-2026 | Exa web search and fetch, scholar | 2026-11-21 | Heins 2026 Appendix C, Bertschinger and Pfante on informational closure |
| group agency criteria (List and Pettit, Pettit 2014) | Exa web search | 2026-11-21 | body of List and Pettit 2011 |
| mutual-information sensor potential games, wonderful-life utility | Exa web search | 2026-11-21 | Marschak and Radner team theory |
| goal-directedness measures, KL fraction explained, logit revision and Gibbs laws, group agents' blankets, attention as covert action, null-model design, Riccati contraction with random coefficients | Exa research agent (ultra, 67 leads; credits then exhausted), scholar search and read_paper | 2026-11-21 | Gotelli and Graves 1996 in the primary, Constant et al. 2018 full text, Heins 2026 Appendix C |

## Log

- 2026-11-21: opened from the user's request to research and investigate the meta-agent existence problem, after `ex:met-two-firms` was found non-diffusive. Next action: parallel construction (epistemic, performative), obstruction theory and literature, then a clause-compliance attack on each construction.
- 2026-11-21: round 1 done (six agents; raw reports in `open_agy_meta_agent_exists-reports.md`). C1 proved; C2 computed in an episode-clock model after the attack's single-$\gamma$ repair; C3 refuted as stated and replaced by C3a to C3c; C4 to C10 added. Existence is computed only under declarations that leave the time-invariant framework (C2) or depend on how $N_{\mathrm{eff}}$ is typed (C9). Next action: O1, the epistemic construction in the time-invariant framework.
- 2026-11-21: round 2 done (constructor and an independent-code attack; reports appended to `open_agy_meta_agent_exists-reports.md`, scripts in `open_agy_meta_agent_exists-checks/round2_*`). C11 computed in the time-invariant framework under five named readings; C12 proved (chain rule, coordinator check with negative control). Under the strictest readings the problem stays open (O5). Next action: the author's reading decisions O2(a), O2(e), O2(f); then O5 or a fresh-context check (O3).
- 2026-11-22: round 3 done (eight investigators, each followed by an independent-code attack, and a synthesizer; reports appended to `open_agy_meta_agent_exists-reports.md`, synthesis in `open_agy_meta_agent_exists-round3-synthesis.md`, scripts in `open_agy_meta_agent_exists-checks/round3_*`). C13 to C19 added; C3a, C3b, C3c, C4, C5 and C12 repaired and raised to fresh-context review; O5 and O6 discharged. Existence is computed by C15 under every combination of O2(a), O2(e), O2(f) and either clause (c) baseline, conditional on O2(g), O2(h), O2(i), O2(m), O2(n). On rereading the manuscript, the lead agent finds (h) and (i) supported by the text (with `ext2_rfm.tex:139` contradicting `def:agy-group-model` on (i)), (m) settled as report-only by `def:agy-meta-agent`, and (g) undecided; the pure-collider pair of R11 passes the literal text only if its fixed couplings are not declared as an interaction graph. Next action: the author's ruling on O2(g) and on whether to require member interaction; then O13 and O7 to O9.
- 2026-11-22: on the author's request ("Yes, integrate P0"), C15 (P0) entered the manuscript as `obs:agy-audience` with `chk:agy-audience` in the supplement, and `open:agy-meta-agent-exists` was narrowed to a meta-agent whose contrast the members' interaction produces or that differs from drawn-once partner randomization. Main-text and supplement statements that no population meets every clause were revised (abstract, introductions, `05_agency.tex`, `10a_meta_agents.tex`, discussions, `s10_abstract_collectives.tex`), and `ext2_rfm.tex` (iii) and `open:rfm-agent` now give missing decision states and admissible class, not missing acts, as the reason the agency index is not evaluated, which resolves the (i) conflict in favor of `def:agy-group-model`. A fresh-context review of the edit (two agents, number fidelity and definitions) led to these corrections: the co-member reading probability is 1.9e-14 (2.1e-14 is not reading the source); the grade from the members' stationary law (alpha_M 0.071) lies outside the independence proviso of `def:agy-closure`(i), so the manuscript states 0.038 from the deterministic start instead; the admitted class is declared as the 5 percent box and openness of the differ clause is stated as supported at sampled points, not proved; the agency dependence on near-deterministic attention at gamma=40 (no data sharing, so `thm:agy-h1`(e) gives no exact agency) is stated; N_fr carries the initial-content proviso of `prop:frm-nulls`(a); under the second-moment convention the every-round N_pr contrast is deterministic and p=0.001 is reported beside the finite-sample p=0.002. Both PDFs build with no errors or undefined references. O2(g) and member interaction (O13) remain open.
