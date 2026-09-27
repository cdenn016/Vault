# Stage 3 independent proof check: actual conditioned parent

The final conditional-information and parent-dynamics arguments are valid under the declared hypotheses. They establish an approximate parent after late restored equilibrium coherence, with actual prefix-conditioned activation and learning from its own law. They do not establish an exact autonomous quotient, activation at the original first contrast, or recursive formation. The derivations below are the evidence; investigator agreement and source hashes are not mathematical proofs.

## Target and source continuity

For each sufficiently small fixed T>0, fix the unchanged scalar shared-link four-cycle and its actual learned law from X_0~N(m_0,I_12), independent uniform assignments, and p_i(0)=1/2. The state is (X,S) in R^12 times sixteen assignments. The continuous generator on sheet S is -A_S X dot grad+T Delta, with A_S=H_S+T Omega, Omega=I+2D_ev^T D_ev, and D_ev X=k-m. A single rate-one clock redraws the whole assignment from product posterior receiver rows b_p(S'|X), including self-proposals. Native deterministic rows satisfy p_i'=epsilon[q_t(S_i=+)-p_i]. There is no discretization or base transport.

The supplied Stage 1 hypotheses are uniform on [s,2s], where s=2epsilon^(-1)log(1/epsilon): for one matching M,

    KL(q_t||mu_{T,p(t)})<=eta,
    TV(q_t,nu_T^M)<=delta,
    max_i |p_i(t)-p_i^M|<=delta.

Here mu_{T,p} is the complete frozen optimizer, and nu_T^M=N(0,T A_M^(-1)) times delta_M. Along the published implicit common schedules these hold eventually for almost every fixed initial mean m_0, with arbitrary prescribed positive tolerances and mobility caps. The matching can vary along the schedule. No power-law selection result or limiting matching is assumed.

Let a=T^(1/4), theta=s+1. The fixed actual event E requires S=M and the two internal stacked Euclidean residual norms at most a and the two exterior norms greater than a throughout [s,theta]. It is the exact published late coherence detector, measurable at theta. Stage 2 gives

    r=P(E^c)<=rho=3delta+b(T,a,1),
    b(T,a,h)=8sqrt(2/pi)a+(8+3400h)T/a^2.

Assume rho<1/2 and theta+h<=2s. For all later t in this window, q_t^E=Law(X_t,S_t|E) conditions on this same completed prefix. It does not condition on future success or recompute the native rows. The parent starts from exactly C#q_theta^E with p^C(0)=p(theta), then uses its own source marginals. The dynamic comparison is total variation of complete retained configuration/assignment paths, not of discarded coordinates or of paths augmented with different deterministic row trajectories.

Read-only source continuity was checked against live Research/manuscripts/pifb2/09_section.tex and 13_section.tex; Research/wiki/concepts/Meta-agents and hierarchical emergence.md; docs/derivations/2026-09-11-meta-agent-formation-frontier-and-locality/selective-interface-actual-parent.md; the scalar parent in Theory/c13_formation.tex, prop:rg-formation-endogenous-cycle(b-d), and its proof in ca_formation_proofs.tex; and the published ca_joint_selection.tex, ca_temperature_bounds.tex, and ca_selected_coherence.tex. Exact pushforward, evaluator tilt, and event-information transfer are prior constructions. This continuation applies them to late selected coherence and controls independently evolving parent rows. SPEC R15 classifies this event as restored equilibrium coherence, not formation.

## Channel and reference conditionals

For matching edges e,f, the hidden space Z_M has orthonormal basis (n_e^+-n_f^+)/sqrt(2), n_e^-, n_f^-. Its orthogonal complement W_M has dimension nine. The fixed channel C(X,S)=(S,P_{W_S}X) uses W_S=R^12 off the two matchings. Its target is a finite disjoint union of Euclidean strata, keeping all sixteen assignments. The loop covector sum_i omega_i and common fast normal lie in each W_M. The channel extends by the identity on observations and all evaluator samples.

H_M and Omega preserve W_M and Z_M. Their eigenvalues on Z_M are (8,4,4) and (1,5,5), respectively. Thus the optimizer hidden reference is

    nu_Z=N(0,T K_Z^(-1)),
    K_Z=diag(8+T,4+5T,4+5T).

The physical outer hidden reference is Pi_Z=N(0,T (K_Z^phys)^(-1)), with K_Z^phys=diag(8+T,4+T,4+T). The Gaussian precision is K_Z/T, whereas K_Z is the drift matrix. Both references are independent of retained y. Prior weights pi_S(p) cancel at fixed retained assignment S, so these hidden conditionals are independent of any strictly positive rows p. This extends to the full physical hidden conditional when evaluator samples are retained. Retained laws and proposal kernels still depend on p. Off matchings the channel discards nothing.

Each physical joint, physical posterior, optimizer, and actual recognition law is normalized by its own pushforward. These different laws are not identified. The channel is fixed on all sixteen sheets before conditioning or future source changes.

## Actual conditioned entropy

Put B=1_E and R_t=(X_t,S_t). Compute joint relative entropy against Bernoulli(1-r) times mu_{T,p(t)} in two orders:

    (1-r)KL(q_t^E||mu_{T,p(t)})
      +r KL(q_t^{E^c}||mu_{T,p(t)})
     =KL(q_t||mu_{T,p(t)})+I(B;R_t)
     <=eta+h_b(r).

The complement term is nonnegative. Since r<=rho<1/2, binary entropy is increasing on the relevant interval and 1-r>=1-rho. Hence

    KL(q_t^E||mu_{T,p(t)})<=kappa,
    kappa=[eta+h_b(rho)]/(1-rho).

For r=0 use only the first term. Absolute continuity and finiteness follow from the identity or q_t^E<=q_t/(1-r). The bound holds for every t in [theta,2s], with the same prefix event and uniform eta. Disintegration through C gives exactly

    KL(q_t^E||mu_{T,p(t)})
      =KL(C#q_t^E||C#mu_{T,p(t)})+H_opt(q_t^E).

Therefore H_opt(q_t^E)<=kappa. This averages over the actual complete retained law. It is not a pointwise fiber bound and does not infer entropy control from total variation. Alternative positive rows change the full retained reference but not the hidden conditional, so only the hidden bound transfers to them.

## Full physical evaluator calculation

Write v=1/2, d_y=D_ev y, d_z=D_ev F_M z. The identity R_ev=D_ev^T D_ev/v and preservation of W_M,Z_M give d_y dot d_z=0. The hidden eigenvalues of R_ev are (0,4,4).

At fixed configuration, the physical evaluator has m_ev~N(m,1/2 I) and independent increment k_ev-m_ev~N(0,vI). Recognition has the same first law and increment mean d_y+d_z. For fixed retained y, define

    Rbar_y(dz,dU)=Pi_Z(dz) P_ev(dU|y+F_M z)
       exp[(d_y dot (k_ev-m_ev)-|d_y|^2/2)/v].

The exponential has expectation one for every z by the Gaussian moment-generating formula. It shifts the increment mean to d_y and preserves the Pi_Z marginal. As the multiplier depends only on retained y and U, the hidden conditional of Rbar_y given U equals the physical posterior's hidden conditional. The recognition evaluator differs at fixed z by the additional increment shift d_z, whose KL is |d_z|^2/(2v).

The joint KL chain rule through z and through U, dropping the nonnegative evaluator-marginal term, yields

    H_phys(q|M,y)
      <=KL(q(dz|M,y)||Pi_Z)+E_q[|d_z|^2/(2v)|M,y].

The optimizer reference is the exact normalized tilt

    nu_Z=Pi_Z exp[-|d_z|^2/(2v)]/Z_tilt,
    Z_tilt=(4+T)/(4+5T).

The common hidden coordinate is unchanged. Each of the two discrepancy coordinates contributes the square root of (4+T)/(4+5T) to the normalizer. Consequently the preceding right side equals

    KL(q(dz|M,y)||nu_Z)+log[(4+5T)/(4+T)].

Integrating over retained states and assignments gives

    H_phys(q_t^E)<=kappa+log[(4+5T)/(4+T)]<=kappa+T,

because matching mass is at most one and log(1+4T/(4+T))<=4T/(4+T)<=T. The fine law has finite second moment, retained by conditioning on E of positive probability; reference log-density differences are quadratic. All integrals used here are therefore well-defined. The physical posterior still uses the original observed records, not a physical posterior conditioned on E.

The optimizer free-energy drop is exactly T H_opt. The unscaled physical negative-ELBO drop is H_phys, and its scaled drop is T H_phys. The upper bounds are T kappa and T kappa+T^2 for the two scaled losses.

## Own-law parent construction

For relative time u, the parent uses the projected OU on its stratum and kernel

    J_p((S,y),A)=integral kappa_S(dx|y)
         sum_{S'} b_p(S'|x) 1_A(S',P_{W_{S'}}x),

where kappa_S is the optimizer hidden conditional (a point mass off matchings). The target projection is that of S', not S. Self-proposals leave y unchanged. The parent learning equation is

    (p_i^C)'=epsilon[q_u^C(S_i=+)-p_i^C],
    q_0^C=C#q_theta^E, p^C(0)=p(theta).

For any prescribed continuous interior row path, there are finitely many Poisson rings on a finite interval. Concatenating the linear diffusions and finite Gaussian draws gives a nonexplosive law. A hidden draw has second moment at most T(1/8+1/4+1/4)=5T/8. It is orthogonal to y, and target projection contracts norm. The expected proposal increment of |y|^2 is at most 5T/8. Diffusion contributes at most 24T-2T|y|^2, giving the stated full-generator bound 25T-2T|y|^2. The actual activation law has finite second moment.

For p in [c,1-c], a receiver posterior f(p)=pA/[pA+(1-p)B] satisfies

    f'(p)=f(p)(1-f(p))/[p(1-p)]<=1/[4c(1-c)].

Couple two prescribed-row parent processes with common initial sample, Brownian noise, clocks, hidden draws, and receiver uniforms until the first differing proposal. Summing over four rows bounds

    TV(q_u^{C,p},q_u^{C,p_tilde})
      <=[c(1-c)]^(-1) integral_0^u ||p(v)-p_tilde(v)||_infinity dv.

The variation-of-constants row map has sup-norm Lipschitz constant at most epsilon u_*^2/[2c(1-c)] over an interval of length u_*. On a sufficiently short interval it contracts and stays in an interior cube, since its row speed is at most epsilon. Its solution obeys

    p_i^C(u)>=p_i^C(0)e^(-epsilon u),
    1-p_i^C(u)>=(1-p_i^C(0))e^(-epsilon u).

On each finite horizon these bounds give a common interior cube and positive contraction step length. Iteration gives unique global own-law evolution. Source marginals are continuous because the proposal rate is bounded; rows are continuously differentiable. Autonomy here refers to this closed coupled law-and-parameter system. The state process is Markov under its resulting deterministic row trajectory.

For frozen rows, C#mu_{T,p} is invariant and reversible. The diffusion follows from the reducing split. The fine flux mu_{T,p}(dx,S)b_p(S'|x) is symmetric in S,S'; pushing both endpoints through C proves the parent jump detailed balance. Disintegration and pushforward handle the different stratum dimensions without an unaccounted volume factor.

## Stopped path coupling

The parent nonpartner probabilities satisfy zeta_i^C(u)<=delta+epsilon u<=d=delta+epsilon h. For d<1/4 and 0<T<=1/100, the published determinant bounds give r_E,r_N<=5T/2 and r_C<=3T^(3/2)/2, all below the matching weight one. Hence, for any such row vector,

    mu_{T,p}(M)>=pi_M(p)>=1-sum_i zeta_i>=1-4d.

The retained conditional Gaussian nu_bar_T^M on M is row independent. Let k_p(y)=J_p((M,y),S'!=M). Frozen detailed balance bounds outward stationary flux by complementary stationary mass:

    integral k_p(y) nu_bar_T^M(dy)
      <=[1-mu_{T,p}(M)]/mu_{T,p}(M)
      <=4d/(1-4d).

This is an averaged hazard under a stationary held-M reference, not a pointwise cost gap or a claim about the surviving actual law.

Conditioning a probability law on E changes its total variation by at most r after any measurable projection. The published native path estimate and the activation marginal therefore give

    TV(P_fine,C(.|E),O_C)<=rho+(h+2)delta,
    TV(q_0^C,nu_bar_T^M times delta_M)<=rho+delta,

where O_C is the stationary projected held-M OU path law. Maximally couple this actual parent activation with the stationary law and use common retained Brownian noise and proposal randomness until the first departure. Paths agree before departure because the drift splits and self-proposals do not move y.

The constructed p^C(u) is deterministic. If Y is the whole stationary reference path, the probability of a parent departure while initially coupled is at most

    E integral_0^h 1_{initial agreement, no earlier departure}
                          k_{p^C(u)}(Y_u) du
      <=integral_0^h E k_{p^C(u)}(Y_u) du
      <=4hd/(1-4d).

Removing the stopped indicator before applying the stationary marginal is the load-bearing step. It does not assume stationary survival-conditioned distributions. Thus

    TV(P_parent,O_C)<=rho+delta+4hd/(1-4d),

and the triangle inequality proves

    TV(P_fine,C(.|E),P_parent)
      <=2rho+(h+3)delta+4hd/(1-4d).

Every retained continuous coordinate and the entire assignment path are included, hence the loop history as well. The Gaussian serves only as comparison; actual activation remains C#q_theta^E, and parent rows are not prescribed by the native process after activation.

## Limit and precise remaining scope

With eta,delta<=T, epsilon<=T^2, a=T^(1/4), h=T^(-1/4),

    rho<=3T+8sqrt(2/pi)T^(1/4)+3408T^(1/2)=O(T^(1/4)),
    kappa=O(T^(1/4)log(1/T)),
    d<=T+T^(7/4)<=2T,
    h delta=O(T^(3/4)), hd=O(T^(3/4)).

The path bound is O(T^(1/4)). Also theta+h<=2s eventually because epsilon<=T^2 makes s much larger than 1+T^(-1/4). These are valid upper bounds, not optimal exponents or numerical observations.

The high-probability prefix is essential to this conclusion. Under exact nu_T^M, z_1 is independent of the retained state. Conditioning on {z_1>0}, whose probability is 1/2, gives a hidden density ratio two on that half-space and discarded KL exactly log(2) for every T. Thus a probability merely bounded below does not imply vanishing hidden KL. Conditioning on an entire realized fine history fixes the hidden endpoint and instead gives a Dirac conditional with infinite KL against the nondegenerate Gaussian. Neither regime is claimed here.

The strongest supported result is therefore a normalized, source- and loop-retaining parent from the actual declared late prefix, with averaged conditional-information error O(T^(1/4)log(1/T)) and retained/source path error O(T^(1/4)) over a following T^(-1/4) interval, while its rows learn from its own law. The original early first-contrast conditioning, arbitrary-history closure, and a second native formation episode remain separate obligations. The next action that would change the formation conclusion is an event-specific hidden-information and path estimate for the original early prefix or a further native episode, not a stronger label-selection statement.

## Executed checks and final source binding

The verifier read the named live sources and reconstructed the displayed identities and bounds analytically. The root's stage3-projection-check.py/json records exact Fraction projector checks for both matchings. I read that script and saved output as supplementary algebraic evidence; I did not rerun or modify it. No new external theorem was needed. No stochastic experiment, GPU work, full suite, Lean, tamper check, or vault write was performed by this verifier.

Both final proof sources were read. SHA256 values obtained by Get-FileHash in the assigned worktree are:

| Final proof source | SHA256 |
| --- | --- |
| Theory/ca_parent_conditional.tex | AD1AFAEDE369185E9092C97511F3157610D0C00AA384EA777952F517A5EDF968 |
| Theory/ca_parent_dynamics.tex | 1EF901A0672BA84D937ED3B6DF9DCDC537AD8A4232A0648D27A5FCE7A0DAA533 |

The conditional TeX was checked after its final integration. The dynamics hash matches the checked final text, including the corrected phrase hidden drift matrix. These hashes bind this review to source revisions; the mathematical acceptance is the argument above. The first attempted report write was rejected when automatic approval review hit the account usage limit, so no report file was written then; after the user restored credits and authorized continuation, this final report was written without repeating completed reconstruction.

The bounded Exa Stage 3 intake is appended separately when its terminal output is available. A running result with an empty output is not research evidence.

## Model attribution and cross-model verification (added 2026-09-26 by Claude Opus 5.5)

Author model of both proofs: OpenAI gpt-6-astra (Codex root session and its research subagents). The reconstruction above was written by the Codex research-dynamics subagent "Russell", also gpt-6-astra, according to the Codex session metadata. It is therefore a same-model reconstruction. Under the user's cross-model rule it is not an independent verification.

Cross-model verification was then run as Claude workflow `wf_2c9097a7-db6`, orchestrated by Claude Opus 5.5 with four Claude Fable 5.1 (claude-fable-5-1) agents. The agents covered the conditional proposition, the dynamics proposition, manuscript and record integration, and an exact executed recomputation of the constants. They verified the source SHA256 values ad1afaed... and 1ef901a0... before and after reading. All four returned VALID_WITH_MINOR_ISSUES, and none found a mathematical defect. The exact recomputation built the twelve-dimensional cycle matrices from `c13_formation.tex`/`ca_formation_proofs.tex` and confirmed the following: the W_M/Z_M invariance; the hidden eigenvalues (8,4,4), (1,5,5), and (0,4,4); K_Z and K_Z^phys; Z_tilt=(4+T)/(4+5T); the moment constants; and the limit arithmetic. It also reran the projector check and obtained the committed JSON. Full structured results are in `stage3-crossmodel-verification.json`; executed scripts and outputs are in `stage3-crossmodel-scratch/`.

The verifiers found no mathematical defect. They did find exposition and hypothesis-restatement issues, and these edits address them:
- `rho<1/2` is now stated as an assumption, and the asymptotic remark notes that it holds for sufficiently small T. With delta<=T it first holds near T=1.58e-8, so both bounds are asymptotic statements.
- The dynamics statement now carries `0<T<=1/100`, defines b_p as the product receiver posterior, and cites `prop:phil-temperature-tracking` for the row-independent sheet-weight ordering.
- Both proofs now say that only the learned-arm conclusions of the Stage 2 persistence proposition are used. Its frozen-arm hypothesis is not needed.
- The hidden-sign example is now `rem:phil-conditioned-hidden-sign` with a status tag, as SPEC R2/R4 require.
- In c14, a missing paragraph break is restored and the summary names its schedule hypotheses.
- In STATUS.md and RG-COMPLETION.md, rho<1/2, d<1/4, and the meaning of eta are restored.

The edits change no bound or proof step.

Final bound sources after these edits (sha256):

| File | SHA256 |
| --- | --- |
| Theory/ca_parent_conditional.tex | ce41fd13dac20aa0b8c179c6b0dc1ad99f3afe5b2e26f0fb1626e303917fb39b |
| Theory/ca_parent_dynamics.tex | 51d25a3a598b0c5db240b342c6cfc226f1b51f88bfba8c1dc399bd53ea18ec6b |
| Theory/c14_interpretation.tex | ac2335b8049a6626ef7843bf63852a40d2a98e715d72af23170c8f9b8684d689 |

The Fable checks read the pre-edit hashes. Every post-edit change is the textual fix a verifier proposed, and no re-verification of the edited text was run. Rebuild in `C:/tmp/multiagentelbo-selection-stage3-build2`: for main, supplement_gaussian, and supplement_base, every local input's latexmk MD5 matches the final sources (35/35, 17/17, 19/19). The logs show 307, 118, and 187 pages, with zero undefined references, multiply-defined labels, rerun warnings, and overfull boxes. The main PDF sha256 is aaab5912...ba3c136; `compiled/stage3-main.pdf` is that build. Labelgraph (split mode, worktree paths) found 2632 labels, 0 multiply defined, and 0 violations.
