# First-block comparison on the original episode window

The learned and frozen arms have the same limiting first-block law on the original contrast window whenever the source-learning mobility is o(T^(1/4)). This includes the joint slow schedules proved in Stage 1. The result concerns the first-block mark defined by the infimum of qualifying completion times in that window, conditioned on a qualifying interval existing. The infimum need not itself be a qualifying completion time. It neither replaces that event by a late observation nor settles the original coupled regime epsilon_L=T^(1/8).

## Target, conventions, and source boundary

Use the unchanged scalar shared-link four-cycle at one base point, with configuration X=(k,m,omega), actual rate-one redraw of the complete assignment, drift -A_S X, and noise sqrt(2T)dW. Both arms start from N(m_0,I_12) times uniform assignments. The learned rows solve p_i'=epsilon_L[q_t(S_i=+1)-p_i]; the frozen rows stay at 1/2. The same fixed Gaussian mean and all other data are used in both arms.

Separate the two parameters. Write xi=T^(1/8), so the existing definition of contrast formation retains its exact resolution and horizon:

    internal belief and model KL <=xi^4=sqrt(T),
    boundary belief KL >1/2,
    episode duration 1,
    total observation horizon H_T=2/xi=2T^(-1/8),
    at least one internal belief KL >1/4 at time zero.

The mobility epsilon_L is independent of xi in this comparison. The original problem instead fixes epsilon_L=xi; it is not silently changed into the present regime.

For each of the eight connected proper blocks with two or three vertices, consider the completion times of all duration-one intervals satisfying these conditions. The first block minimizes the infimum of its completion times. Fix one deterministic order to break ties, used identically in both arms. A block's completion time is its interval-start time plus one, so this selects the same chronological first block as ordering the interval starts. No assumption that ties have probability zero is needed. The tie rule is an observation convention and does not enter the dynamics.

Let K_T be the resulting finite-valued mark, with a cemetery value if no contrast occurs by H_T, and let E_T={K_T is not cemetery}. The statement below concerns TV of the laws of K_T conditional on E_T. It applies equally to any other common measurable first-block convention and to additional prefix-measurable admissibility conditions whose frozen success probability has a positive lower bound.

This construction preserves the original threshold and initial entrance clauses. It does not assert that every event admitted by the broad contrast definition satisfies R15. The supplied matching-seed sub-event already has the actual-sheet restoring rates and stationary comparison proved in the existing witness. Any qualification retaining that sub-event keeps the probability floor needed below.

## Proposition: an explicit early-window null

For every T>0, fixed initial mean, mobility epsilon_L>=0, and deterministic H<infinity, the complete configuration-assignment path laws satisfy

    TV(Law_learn((X_t,S_t)_{0<=t<=H}),
       Law_frozen((X_t,S_t)_{0<=t<=H}))
    <=delta_H:=min(1,2epsilon_L H^2).

For 0<xi<=1/100, the existing frozen seeded witness gives

    P_frozen(E_T)>=c(m_0)>0,

where one permissible temperature-independent value is

    c(m_0)= exp(-1/4) rho_0^12 /737280
             *exp[-(|x_circ-m_0|+rho_0)^2/2],
    rho_0=1/100,  x_circ=(0_4,0_4,1_4).

Consequently P_learn(E_T)>=c(m_0)-delta_T, where

    delta_T=min(1,8epsilon_L T^(-1/4)).

Whenever delta_T<c(m_0), both conditional laws are defined and

    TV(Law_learn(K_T|E_T),Law_frozen(K_T|E_T))
       <=delta_T/c(m_0).

Therefore, for every fixed Gaussian mean, this conditional TV tends to zero along every parameter regime with T->0 and epsilon_L T^(-1/4)->0. The claim is pointwise in the fixed mean; c(m_0) is not bounded below over all means.

### Proof of the full-path estimate

The learned rows are deterministic and satisfy the exact bound

    |p_i(t)-1/2|<=epsilon_L t/2.

At a common state x and a proposal time t, let A,B>0 be a receiver's two likelihood factors. Its learned and frozen probabilities of choosing the positive neighbor are

    beta(p)=pA/[pA+(1-p)B],    beta(1/2)=A/(A+B).

Direct subtraction gives

    |beta(p)-beta(1/2)|
      =AB|2p-1|/[(pA+(1-p)B)(A+B)]
      <=|2p-1|<=epsilon_L t,

because the denominator is pA^2+AB+(1-p)B^2>=AB. This is uniform in x, T, and the likelihood ratio; no lower bound on a likelihood and no compact-interior row assumption is needed.

Couple the two processes with identical initial samples, the same Brownian motion, and the same rate-one proposal clock. Until the first different redraw, their assignments and configurations coincide because the drift and noise on a common assignment do not depend on the learned rows. Couple each pair of posterior receiver Bernoulli choices maximally at a ring. The probability of any mismatch among the four receivers is at most

    sum_i |beta_i(p_i(t))-beta_i(1/2)|<=4epsilon_L t.

The expected number of mismatches up to H, stopped at the first one, is at most the rate-one compensator integral

    integral_0^H 4epsilon_L t dt=2epsilon_L H^2.

The probability of a mismatch is no larger. On its complement the entire paths agree. The coupling inequality proves the complete-path TV bound. Taking H=H_T gives delta_T. This is a pathwise coupling of the two native processes, not a Gaussian approximation conditional on an adaptive assignment history.

### First-block measurability

For a block I and end time t, define A_I(t) as the maximum of all internal belief and model KL values on [t-1,t], and B_I(t) as the minimum boundary belief KL there. Configuration paths are continuous, so both functions are continuous in t and in the configuration path under the uniform topology on [0,H_T]. For each positive integer k, the set

    {t in [1,H_T]: A_I(t)<=sqrt(T), B_I(t)>=1/2+1/k}

is closed and compact. Its first time is a measurable path functional: the event that it is at most s is expressed by the minimum on [1,min(s,H_T)] of
max(A_I(t)-sqrt(T),1/2+1/k-B_I(t)) being nonpositive. Taking the infimum over k implements the strict boundary inequality exactly. Initial eligibility is a Borel condition on X_0. The finite minimum over blocks, common tie rule, and cemetery convention therefore give a measurable K_T. The first infimum need not itself be an attained endpoint of the strict-inequality set; it still orders the first occurring blocks, and this boundary convention is identical in both arms.

The estimate would hold for any measurable convention without this construction, since a measurable map of complete paths cannot increase total variation.

### Conditioning without an avoidable factor of two

Let a_I and b_I be the learned and frozen probabilities of each non-cemetery block mark, and let p=sum_I a_I, q=sum_I b_I be their success probabilities. Write d for the TV distance of the two cemetery-augmented mark laws. Then

    2d=sum_I|a_I-b_I|+|p-q|,     d<=delta_T.

Assume p>=q>0. The triangle inequality gives

    sum_I|a_I/p-b_I/q|
      <=[sum_I|a_I-b_I|+(p-q)]/p
      =2d/p.

Exchange the arms if q>=p. Thus the conditional TV is at most d/max(p,q), which is at most delta_T/c(m_0) because the frozen success probability is at least c(m_0). The same augmented-law comparison gives |p-q|<=delta_T, so p>0 when delta_T<c(m_0).

The probability floor comes directly from the existing frozen matching-seed sub-event in prop:phil-seeded-contrast-formation. Its prescribed unit interval is inside [0,H_T] for the stated range of xi and its block satisfies the original contrast definition. No new uniform-in-mean lower bound is asserted.

## Consequence for the Stage 1 schedules

Stage 1 permits thresholds d_n<=T_n^a for any prescribed a>7/2, while ensuring late-time matching selection for almost every fixed mean and every epsilon_L<=d_n. For the same mobilities,

    delta_{T_n}<=8T_n^(a-1/4)->0.

Hence the original-window first-block conditional laws in the two arms agree asymptotically for every fixed mean. For almost every fixed mean the same process family nevertheless has learned-versus-frozen assignment-law TV tending to 1/2 on the much later selection window

    [2epsilon_L^{-1}log(1/epsilon_L),
     4epsilon_L^{-1}log(1/epsilon_L)].

These statements concern different random variables. The late assignment law need not preserve the block that appeared first on the original observation window. The result does not prove a positive first-block selection mechanism from the late matching theorem.

The null does not require taking epsilon_L exactly at a diagonal threshold, nor any special sign or lower bound for the imprint. It follows directly from the explicit inequality for every joint regime epsilon_L=o(T^(1/4)).

## Restoring and horizon clauses

For the known seeded matching sub-event, the internal normal restoring rates are 8+T and 4+5T. At residual resolution a=xi^2=T^(1/4), the restoring ratio is at least 4a^2/T=4T^(-1/2)->infinity. The assignment is actually held by posterior proposals on this event; it is not frozen by the analyst.

The seeded sub-event also carries the previously proved stationary comparison: at every fixed row configuration its stationary probability is at most 4exp[-1/(4T)], whereas its frozen probability from the supplied Gaussian start is at least c(m_0). Its learned probability is at least c(m_0)-delta_T by the present path comparison. Thus the existing seeded witness retains a positive transient margin for each fixed mean in this slow regime. This checks that the probability floor can be carried by a genuine previously established episode.

The broad original contrast detector can include other histories. This note does not certify those histories as formation under R15 or turn equilibrium recurrence into formation. If a declared common admissibility rule retains the seeded sub-event, the same path estimate and conditioning calculation apply to its first mark as well. A rule that examines the full law rather than the observed episode prefix is outside this path-functional statement unless separately encoded.

## What is not settled

In the original open-problem regime epsilon_L=xi=T^(1/8), the bound becomes 8T^(-1/8) and is vacuous after clipping at one. No negative or positive conclusion for that coupled regime follows. An estimate beyond the elementary perturbative horizon, or a direct analysis on times of order 1/epsilon_L, is still needed.

Only the learned-versus-frozen arm was compared. Two Gaussian initial means differing in their loop coordinate need not have nearby initial laws; this result does not settle that separate comparison. No conditional parent loss, parent activation, or parent dynamical error was analyzed.

A first-ever stopping-time argument at each fixed T was considered but is unnecessary for the proved result and is not claimed. It would require a careful eligibility event: some Gaussian starts have no internal belief KL above 1/4 initially, making the original entrance detector impossible forever. Extending the observation horizon through recurrent late contrasts would also need an independent R15 horizon check. The finite original-window estimate avoids both issues.

## Evidence and next obligation

This is an analytical coupling proof. No external reference, simulation, symbolic calculation, heavy test, or later-stage construction was used. The source checks were the exact contrast definition and seeded probability floor in Theory/c14_interpretation.tex; open:rg-formation-adaptive-family and prop:rg-formation-endogenous-cycle in Theory/c13_formation.tex; R13 and R15 of Theory/SPEC.md; p15-restoring-vs-recurrence.md with its stated recurrence limitations; and live PIFB2 sections 09_section.tex and 13_section.tex, which separate coherence, persistence, selection, and autonomy.

The supported result is an explicit early-window first-block null coexisting with the late selection theorem. To change the answer for the original adaptive-family target, the next load-bearing obligation is the first-block law in its actual regime epsilon_L=T^(1/8), with a precise common episode detector and its conditioning probabilities. Late one-time selection does not supply that law.

