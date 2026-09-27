# A joint selection limit by a diagonal mobility schedule

This note treats Stage 1 only, in the unchanged homogeneous shared-link four-cycle at one base point. It proves existence of a deterministic schedule independent of the initial mean. It does not supply a computable power law, identify a temperature-independent matching, or prove a coherent-block or parent-dynamics statement.

## Inputs and target

The model and initial law are those in Theory/ca_selection_proofs.tex: the Gaussian N(m,I_12) times uniform assignments, fixed mean m in R^12, source-learning mobility epsilon, and temperature T. The auxiliary Gaussian measure on the space of means below is only a proof device. It neither randomizes the physical preparation nor changes the model.

Write q^{T,epsilon,m}_t and p^{T,epsilon,m}(t) for the learned recognition law and rows, q^{T,0,m}_t for the frozen-uniform-row law, and mu_{T,p} for the frozen invariant law at rows p. The existing proof gives selection at each fixed 0<T<=T_0 for every mean with j_T(m)!=0. Its unstable eigenvalue satisfies alpha(T)>=7/5, and any C_T>1/alpha(T) is valid independently of the mean. Hence C=2 works at all these temperatures. Put

    t_L(epsilon)=2 epsilon^{-1} log(1/epsilon),
    W_epsilon=[t_L(epsilon),2t_L(epsilon)],  0<epsilon<e^{-1}.

Let M_T(m) be the matching selected by sign(j_T(m)); choose either matching on its null zero set. Define

    nu_T^M=N(0,T A_M(T)^{-1}) tensor delta_M,
    A_M(T)=H_M+T Omega,
    mu_T=mu_{T,1/2}.

The covariance exists because A_M(T)>=T I>0. The relevant equivalence is total variation of the complete one-time configuration-assignment law, uniformly on W_epsilon. It is not path-law equivalence.

At each fixed T, the existing proof actually implies that the following five errors tend to zero as epsilon->0, for almost every fixed mean:

1. The maximum row distance to the selected matching vertex, uniformly on W_epsilon.
2. TV(q^{T,epsilon,m}_t,nu_T^{M_T(m)}), uniformly on W_epsilon.
3. KL(q^{T,epsilon,m}_t || mu_{T,p(t)}), uniformly on W_epsilon.
4. TV(q^{T,0,m}_t,mu_T), uniformly on W_epsilon.
5. KL(q^{T,0,m}_t || mu_T), uniformly on W_epsilon.

The supremum in the first entry includes the four rows. The learned entropy convergence follows directly from the existing square-root entropy tracking estimate; the frozen entropy decays exponentially at fixed T by the entropy identity and contraction at uniform rows. Frozen convergence holds for every mean.

For the full learned law in item 2, conditional on assignment M the law mu_{T,p} is exactly nu_T^M's Gaussian factor, independently of p. With zeta_i=|p_i-p_i^M|, all normalized sheet weights are at most the matching weight one, so

    mu_{T,p}(M)>=pi_M>=1-sum_i zeta_i,
    TV(mu_{T,p},nu_T^M)=1-mu_{T,p}(M)<=sum_i zeta_i.

Combine this with the established learned tracking in total variation. No Gaussian law conditional on an adaptive assignment history is assumed.

### Explicit entropy majorants

No entropy-continuity assertion is needed in the diagonal construction. Let G_T=sup_{p in [0,1]^4} ||g_T(p)||_1, which is finite at each fixed temperature, and choose the positive frozen-rate constants c_T,K_T from the established entropy bound. On the entire selection horizon t<=4 epsilon^{-1}log(1/epsilon), the row lower bound gives

    ell_T(epsilon)=c_T/[K_T+8log 2+32log(1/epsilon)].

This is a lower bound for the frozen entropy rate along the learned rows. Put lambda_u(T)=c_T/[K_T+8log 2]. The shared initial entropy is the explicit continuous function

    H_0(T,m)=log Z_T(1/2)-6
             +(tr A_bar(T)+m^T A_bar(T)m)/(2T),
    A_bar(T)=(1/16) sum_sigma A_sigma(T).

To verify it, the log density ratio at uniform rows is log Z_T(1/2)-|x-m|^2/2+x^T A_sigma x/(2T), and the initial Gaussian has E|X-m|^2=12. It is nonnegative because it equals a relative entropy.

For all times in W_epsilon, the existing tracking and frozen contraction estimates imply

    H_learn(t)<=B_L(T,epsilon,m)
       =[exp(-ell_T(epsilon)t_L/2) sqrt(H_0)
          +epsilon G_T/(sqrt(2) ell_T(epsilon))]^2,
    H_frozen(t)<=B_F(T,epsilon,m)
       =exp(-lambda_u(T)t_L) H_0.

At each fixed T and m these explicit upper bounds tend to zero as epsilon->0. They are continuous in positive epsilon and m, so they can replace actual entropy in the diagonal error functional without an additional entropy-continuity argument.

## Quantified diagonal theorem

Fix any positive temperature sequence T_n decreasing to zero within (0,T_0]; the geometric choice T_n=T_* 2^{-n}, with 0<T_*<=min(T_0,1), is one example. Let eta_n in (0,1) tend to zero, let b_n>0 have finite sum, and let h_n>0 be any prescribed mobility caps.

There exist deterministic d_n>0, independent of the initial mean, and a Lebesgue-null set N, such that

    d_n<=min(e^{-1},2^{-n},h_n,d_{n-1}/2),

with the last condition omitted at n=1. For every fixed m outside N, eventually in n, **all five errors above at T_n are at most eta_n for every 0<epsilon<=d_n**. Their matching is M_{T_n}(m), independent of the mobility chosen below d_n.

Thus every choice epsilon_n<=d_n gives a joint vanishing-temperature and vanishing-mobility limit for almost every fixed mean. Both the temperatures and thresholds are common to the means. The selected matching can depend on n.

The tolerances may decay arbitrarily rapidly, for example eta_n=T_n^r for any fixed r>0. Likewise h_n=T_n^a imposes any chosen exponent a>0, including a>7/2; h_n=T_n^n imposes epsilon_n/T_n^a->0 for every fixed a>0. These are additional upper caps, not certified equalities. The result does not certify epsilon=T^a or any other prescribed explicit curve.

### Proof

Let rho be the standard Gaussian probability measure on R^12. Its density is strictly positive. Define E_n(epsilon,m) as the minimum of one and the maximum of the row error, learned and frozen total-variation errors above, and the two explicit entropy majorants B_L(T_n,epsilon,m), B_F(T_n,epsilon,m). Set

    F_n(r,m)=sup_{0<epsilon<=r} E_n(epsilon,m).

At each fixed n, E_n(epsilon,m)->0 for rho-almost every m by the fixed-temperature proof. Therefore F_n(r,m)->0 for almost every m as r->0, and 0<=F_n<=1.

Here the envelope is measurable. At a fixed positive temperature, restrict epsilon to a compact interval bounded away from zero and m to a compact set. The associated horizons are finite and bounded. All rows then remain uniformly inside the open cube. The posterior redraw kernel is uniformly Lipschitz in those rows, and all held drifts are fixed linear maps. Maximal coupling of initial laws, common Brownian motions and clocks, and coupling until the first different redraw give a bound for differences of the laws by the initial total variation plus an integral of row differences. Differences of the learning equations are bounded by the integral of law and row differences and the mobility difference. Gronwall's inequality gives continuous dependence in total variation on positive mobility and mean. The positive forward-kernel formula gives continuity in time.

Each row or total-variation window supremum, parametrized by t=u t_L(epsilon) for u in [1,2], is consequently continuous in positive mobility. The explicit entropy majorants are continuous by their displayed formulas. The sign-defined matching is Borel in the mean because j_T is analytic. A supremum over positive rational mobilities equals the displayed envelope, proving measurability. No continuity uniform as epsilon->0 is used.

Dominated convergence now gives

    integral F_n(r,m) rho(dm)->0 as r->0.

Construct d_n=2^{-k_n} recursively, where k_n is the smallest positive integer satisfying the cap restrictions and

    integral F_n(2^{-k_n},m) rho(dm)<=eta_n b_n.

Such an integer exists. This is a deterministic mathematical definition in terms of the exact laws; it is not a computed or numerically certified mobility threshold.

Define B_n={m:F_n(d_n,m)>eta_n}. Markov's inequality gives rho(B_n)<=b_n. For every N,

    rho(union_{n>=N} B_n)<=sum_{n>=N} b_n ->0.

Hence rho(limsup_n B_n)=0. No independence is required. Add the countable union of imprint zero sets. The resulting set is rho-null and therefore Lebesgue-null. Outside it, eventually F_n(d_n,m)<=eta_n. Since eta_n<1, clipping has no effect on that inequality: the row and total-variation errors and both entropy majorants are at most eta_n. The latter bound the actual entropies, so all five claimed errors are at most eta_n. This proves the theorem.

For eta_n=b_n=2^{-n}, the Gaussian measure of means for which any estimate fails at some n>=N and some epsilon<=d_n is at most 2^{1-N}. On a Euclidean ball of radius R its Lebesgue measure is at most (2 pi)^6 exp(R^2/2) 2^{1-N}. This is an explicit exceptional-set estimate for the defined schedule, not an explicit numerical schedule.

### One parameter path

Set T(epsilon)=T_n whenever d_{n+1}<epsilon<=d_n. Then T(epsilon)->0, and all five errors vanish as epsilon->0 for almost every fixed mean. This gives all sufficiently small mobilities on one deterministic stepwise parameter path. It is not a uniform result for every (T,epsilon) below a known curve or for an arbitrary continuum of prescribed temperatures.

## Frozen labels and the law-level contrast

The exact determinant calculation gives normalized weights one for each matching, r_E for eight end paths, r_N for four middle paths, and r_C for two cycles. Consequently

    mu_T(M)=1/[2+8r_E+4r_N+2r_C]=1/(2D_0),
    D_0=1+4r_E+2r_N+r_C,
    0<=1/2-mu_T(M)=(4r_E+2r_N+r_C)/(2D_0).

The established expansions r_E,r_N=O(T) and r_C=O(T^{3/2}) imply mu_T(M)=1/2+O(T), with a nonpositive correction. The frozen assignment law tends to the equal mixture of the two matching labels, whereas the learned arm tends to its selected label. On the diagonal schedule, uniformly over the selection window,

    |TV(q_learn^S,q_frozen^S)-[1-1/(2D_0(T_n))]|<=2 eta_n.

Indeed TV(delta_M,mu_T^S)=1-mu_T(M); replacing either law changes a total-variation distance by at most its total-variation error. Therefore the assignment-law distance tends to 1/2. This is not yet a comparison of first coherent-block events.

## The missing quantitative imprint statement

The actual imprint is entire and nonzero as a function of m at every fixed T. Its large-amplitude lower bound takes amplitude to infinity at fixed T and has an uncontrolled temperature-dependent remainder. Neither fact bounds its magnitude or sign at a fixed mean as T->0.

For any nonzero analytic Q(m), the hypothetical family exp(-1/T) Q(m) satisfies fixed-temperature analytic nonvanishing but is smaller than every power of T at fixed Q(m)!=0. The prefactor exp(-exp(1/T)) defeats a much smaller prescribed scale as well. These logical examples are **not counterexamples for the actual four-cycle**. They show that the hypotheses alone do not imply a power bound.

The linearized slow saddle escape from amplitude epsilon |j_T(m)| takes approximately alpha(T)^{-1} log(1/[epsilon |j_T(m)|]). The fixed-temperature proof absorbs log(1/|j_T(m)|) into a finite mean-dependent remainder. A joint explicit regime must control that term and the tracking remainder relative to the imprint.

Likewise fixed-temperature analytic nonvanishing does not imply eventual sign stability. For independent analytic functions Q_1,Q_2, the family

    Q_1(m) cos(log T)+Q_2(m) sin(log T)

is nonzero and analytic at each fixed T, while its sign oscillates as T->0 whenever (Q_1(m),Q_2(m))!=(0,0). One may preserve evenness and the matching-exchanging rotation character by taking Q_1 and Q_2 to be the alternating edge sums of squared common-channel and discrepancy-channel residuals. These quadratics are independent and both change sign under a one-edge rotation. This is a logical example, not a claim about the actual imprint.

A zero first-order imprint only defeats the present sufficient criterion: its nonvanishing is not known necessary for selection. The minimal unresolved step for an explicit power schedule is a quantitative estimate of the actual j_T(m) on a stated class of fixed means, together with the temperature dependence of the error constants. A fixed matching throughout the joint limit additionally requires eventual sign stability or another label-identification argument.

## Suggested chapter statement

**Joint selection along a deterministic schedule.** In the preceding four-cycle, take any positive T_n decreasing to zero within (0,T_0], and any eta_n in (0,1) tending to zero. Given any positive caps h_n, there exist decreasing d_n<=h_n, independent of the mean, and a Lebesgue-null set N such that for every m_0 outside N and all sufficiently large n, every 0<epsilon_L<=d_n has, uniformly on [2epsilon_L^{-1}log(1/epsilon_L),4epsilon_L^{-1}log(1/epsilon_L)], row distance, learned full-law total variation from its selected matching Gaussian, learned relative entropy from its instantaneous frozen law, and frozen total variation and relative entropy from its uniform-row invariant law at most eta_n. The matching may depend on n. The actual assignment-law total-variation contrast between learned and frozen arms tends to 1/2. The thresholds are obtained by an existence construction, not an explicit power law.

This statement should be followed by the scope boundary: the result controls one-time laws along a common joint schedule, not complete histories, conditional first-formation events, or inherited parent dynamics.

## Evidence and scope

Analytical proof only; no simulation, symbolic calculation, new external reference, or path-law approximation was used. Sources read were the complete current selection proof, its c14 statement, docs/STATUS.md, the historical P-11 note with its September 26 correction, and live PIFB2 pifb2/13_section.tex and pifb2/09_section.tex. The current small-fixed-temperature proof is the authority; the old all-temperature P-11 claim is not promoted. No stage after Stage 1 was investigated.




