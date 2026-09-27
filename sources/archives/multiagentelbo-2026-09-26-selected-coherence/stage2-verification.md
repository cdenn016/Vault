# Stage 2 independent verification

September 26, 2026. Worktree: `C:/tmp/multiagentelbo-selection-formation-20260926`, Item 2 branch. This check concerns selected-pair coherence/persistence and the first-block comparison only. It does not construct or activate a parent. Only this verification artifact was written.

## Verdict and target

The actual-path persistence comparison and the early first-block null are valid, with distinct time windows and detectors. The late selected pairing remains the Euclidean coherent partition for a growing following window along the implicit Stage 1 schedule. The original early-window first-block conditional laws agree asymptotically whenever epsilon_L=o(T^(1/4)). The original coupled choice epsilon_L=T^(1/8) remains unresolved by this estimate.

One detector defect was found in the first coherence draft: it reused the existing partition symbol with coordinatewise thresholds in place of the declared Euclidean residual-pair norm. For instance (r_b,r_m)=(a,a) meets the coordinatewise test but fails the original norm<=a test. The corrected version uses the original norm and enlarged constants as checked below. The first-block definition explicitly uses the infimum of qualifying completion times, with a common deterministic tie rule; it does not assume that a strict-inequality qualifying set attains its infimum.

## 1. Model, source contracts, and quantifiers

The state is (X,S) in R^12 times the sixteen assignments. There is one shared link translation per unoriented edge, identity mobility, Brownian covariance 2T I dt, no boundary on R^12, and one rate-one clock redrawing the complete assignment from the product posterior rows. Held drifts are -(H_S+T Omega)X. The actual learned rows satisfy

    p_i'=epsilon_L[q_t(S_i=+1)-p_i],  p_i(0)=1/2.

The frozen control keeps the original uniform rows. Both arms start from the same N(m_0,I_12) times uniform assignments. Comparisons of path laws concern the configuration and assignment; deterministic parameter paths are not appended as observed state coordinates.

The supplied inputs are the experiment, endogenous-cycle witness, and gated-family coherence convention in `Theory/c13_formation.tex`; the seeded-contrast proposition and fixed/joint selection results in `Theory/c14_interpretation.tex`; their current proof inputs; and SPEC R15. The relevant live PIFB2 formation section was read for scope. The existing Gaussian initial law and model are not replaced by a stationary start in any claim about the native process.

For late persistence, fix deterministic s,L>0 with [s,s+L] inside the selection window and a matching M. Assume

    sup_{s<=t<=s+L} TV(q_t^learn,nu_T^M)<=delta,
    TV(q_s^frozen,mu_{T,1/2})<=delta,

where nu_T^M=N(0,T A_M^(-1)) times delta_M. These are actual one-time hypotheses supplied by the preceding selection proof. The comparison O_{T,L}^M is a stationary OU path law with constant matching M. It is a reference used in a proved path coupling, not a conditioning assertion about an adaptive assignment history.

For the early comparison, the mean is fixed but arbitrary; the result holds for every such mean, independently of the late theorem's null exceptional set. Write xi=T^(1/8) and retain the original episode horizon H_T=2/xi, duration one, internal KL threshold xi^4=sqrt(T), exterior belief KL>1/2, and initial internal belief KL>1/4 eligibility clause. The independent learning mobility is epsilon_L. This separation of parameters is explicit and does not settle the old regime epsilon_L=xi.

## 2. One-time concentration to actual-path concentration

Let r(t)=q_t^learn(S!=M), and let b_notM(t,X_t) be the actual probability of proposing a non-M assignment. The bounded-indicator generator gives exactly

    r'(t)=E b_notM(t,X_t)-r(t).

For N_notM counting all proposals to non-M on [s,s+L], including proposals made while already off M, the rate-one compensator yields

    E N_notM=r(s+L)-r(s)+int_s^(s+L)r(t)dt.

A path ever off M either begins off M or has such a proposal. Thus

    P(exists t in [s,s+L]: S_t!=M)
    <=r(s)+E N_notM<= (L+1)delta.

Maximally couple the initial full state with nu_T^M and use the same future Brownian increments. The native process and held-M reference coincide until initial mismatch or a non-M proposal. Their full path total variation is consequently at most

    delta+E N_notM <=(L+2)delta.

This derivation uses the actual proposal probabilities and actual assignment occupation. It remains valid for the law-dependent deterministic learned rows; neither stationary native initialization nor a manually frozen native label has been inserted.

## 3. Frozen path comparison and the matching-to-matching flux

The normalized sheet weights obey, for 0<T<=1/100,

    r_E,r_N<=5T/2,  r_C<=3T^(3/2)/2.

The uniform-row invariant mass off the two matchings is

    kappa_T=(8r_E+4r_N+2r_C)/(2D_0)<=16T,
    D_0=1+4r_E+2r_N+r_C.

Conditional on either matching the invariant configuration is exactly its held-sheet Gaussian. Therefore its full one-time law is within kappa_T of the equal mixture of nu_T^{M_0} and nu_T^{M_1}.

Detailed balance bounds the stationary flux from M to all nonmatching assignments by kappa_T. This alone cannot bound flux to the other matching, whose stationary mass is not small. The separate geometric-mean estimate in the new proof is essential and correct:

    mu_M b_M' =mu_M mu_M'/(sum_S mu_S)
              <=sqrt(mu_M mu_M')/2.

The matching Hessians have complementary edge multiplicities two and zero, so

    (A_M+A_M')/2=A_cycle.

Gaussian integration gives int sqrt(mu_M mu_M')=mu(M) r_C. Dividing both flux bounds by mu(M)=1/(2D_0) gives

    E_{nu_T^M} b_notM<=8r_E+4r_N+(5/2)r_C
                      <=30T+(15/4)T^(3/2)<=31T.

The stationary expected number of departures from either currently occupied matching is at most 31TL. Couple the stationary native process initially to the equal matching mixture and use common Brownian increments until its first departure from the coupled matching. The probability of disagreement is at most 16T+31TL. A common path-transition kernel contracts the original frozen law's initial TV discrepancy delta. Consequently

    TV(P_frozen[s,s+L],(O_M0+O_M1)/2)<=delta+16T+31TL.

The proof does not condition a stationary diffusion on the future assignment path or presume a Gaussian law after such conditioning.

## 4. Corrected Euclidean coherence and all-time OU bounds

The original coherent edge condition is ||(r_b,r_m)||_2<=a. The corrected persistence event E_M(a,L) requires constant assignment M and this condition on both matching edges throughout the interval, with ||(r_b,r_m)||_2>a on both exterior edges. It therefore implies that the entire coherent partition remains the two pairs of M.

Let z_g^+,z_g^- be the four orthonormal normal coordinates of the matched edges. They have rates 8+T and 4+5T, stationary variances at most T/4, and

    r_g^b=sqrt2 z_g^+ + z_g^-,
    r_g^m=sqrt2 z_g^+ - z_g^-,
    (r_g^b)^2+(r_g^m)^2=4(z_g^+)^2+2(z_g^-)^2<=4|z|^2.

For a zero-start scalar OU convolution,

    Z_t=sqrt(2T)[W_t-lambda int_0^t e^(-lambda(t-u))W_u du].

It follows that sup|Z|<=2sqrt(2T)sup|W| and E sup_{t<=L}|Z_t|^2<=32TL. Splitting the stationary initial normal vector from its noise gives

    E sup_{t<=L}|z_t|^2<=2T+256TL.

The probability of any selected Euclidean residual norm exceeding a is therefore at most (8+1024L)T/a^2. This is the corrected coefficient; the previous coefficient based on a scalar residual did not by itself prove the declared pair-norm event.

Each exterior link is absent from H_M and decoupled in Omega, so it is an independent N(0,1) coordinate in the held stationary law. Each of the four exterior scalar channel residuals has variance at least one. A Gaussian density bound and a union bound give probability at most 8sqrt(2/pi)a that any initially has magnitude <=2a.

In an eigencoordinate with rate lambda, stationarity and the same noise estimate give

    E sup_{t<=L}|X_t-X_0|^2
    <=2T(1-e^(-lambda L))^2/lambda+64TL<=66TL,

using (1-e^(-v))^2<=v. Summing twelve coordinates yields E sup|X_t-X_0|^2<=792TL. All residual covectors have norm sqrt3. A single Markov bound therefore controls every exterior scalar increment by a except with probability 2376TL/a^2. On the remaining event, each exterior scalar magnitude stays >a, a sufficient condition for exterior pair norm>a.

Combining the estimates proves

    O_M(E_M^c)<=b(T,a,L)
       :=8sqrt(2/pi)a+(8+3400L)T/a^2,
    P_learn(E_M^c)<=(L+2)delta+b(T,a,L).

For a=T^(1/4), L=T^(-1/4), delta<=T, all terms tend to zero; the largest displayed order is T^(1/4). Taking s=t_L is legitimate along the joint schedule: its admissible mobility caps ensure L<=t_L eventually, so [s,s+L] remains inside [t_L,2t_L]. The same frozen path comparison proves convergence of its persistence-window label to the equal matching mixture.

At one time E|z|^2<=T, so internal failure is at most 4T/a^2, while the exterior scalar small-ball sum at radius a is at most 4sqrt(2/pi)a. Hence

    e(T,a)=4T/a^2+4sqrt(2/pi)a

bounds the chance that nu_T^M induces a different Euclidean coherent partition. Pushforward and the TV triangle inequality give exactly

    |TV(q_learn P_a,q_frozen P_a)-1/2|
    <=2delta+16T+2e(T,a).

The two matching partitions are distinct. This is a late coherent-partition comparison, not merely a label statement.

## 5. R15 restoring and horizon distinction

On E_M the native assignment is actually M throughout the interval, so the normal restoring rates are 8+T and 4+5T. The restoring ratio is at least 4a^2/T and tends to infinity at the declared resolution. This verifies restoration on the actual process with high probability.

It does not establish first formation. If the learned rows are delta-close to their matching vertex, then

    TV(mu_{T,p},nu_T^M)=1-mu_{T,p}(M)<=4delta.

Apply the same occupation and path-coupling argument to the genuine stationary process with those rows frozen. Its probability of the same persistence event is at least

    1-4(L+2)delta-b(T,a,L),

which also tends to one. The event is already typical at equilibrium for the selected rows. No entrance from an initially incoherent state or positive excess over that stationary event probability has been demonstrated. The name restored equilibrium coherence is therefore appropriate under R15. The different uniform-row control still has a late partition contrast; that contrast does not supply a first-formation claim.

The exterior pair-norm>a threshold in this late event must also remain distinct from the original early contrast detector's fixed boundary belief KL>1/2. No high-probability claim about that stronger early event is inferred from the late persistence estimate.

## 6. Early native-path comparison without a central-row restriction

At a common state, let A,B>0 be a receiver's likelihood factors. Direct subtraction gives

    |pA/[pA+(1-p)B]-A/(A+B)|
    =AB|2p-1|/[(pA+(1-p)B)(A+B)]<=|2p-1|,

because the denominator is pA^2+AB+(1-p)B^2>=AB. This global identity is valid; it strengthens the initially suggested local-derivative argument and needs no compact central row set.

With identical initial samples, Brownian motion, and rate-one clocks, the two native paths agree until a first different redraw. Independent common-uniform couplings for the four Bernoulli rows preserve each arm's product posterior. Their mismatch probability at time t is at most 4epsilon_L t, because |p_i(t)-1/2|<=epsilon_L t/2. The stopped compensator therefore proves

    TV(Law_learn(X_[0,H],S_[0,H]),Law_frozen(X_[0,H],S_[0,H]))
       <=min(1,2epsilon_L H^2)

for every finite H. Drift equality before the first mismatch is exact: the held-sheet drift has no prior-row dependence. The comparison uses neither an averaged field nor stationary initialization.

At the literal original observation horizon H_T=2T^(-1/8), put

    d_T=min(1,8epsilon_L T^(-1/4)).

The full finite histories have TV discrepancy at most d_T. Every common measurable detector on those histories inherits this bound.

## 7. First-block mark and conditioning

The original detector includes all eight proper connected blocks of size two or three. For each eligible block I let A_I(t) be the maximum internal belief/model KL over [t-1,t] and B_I(t) the minimum boundary belief KL there, t in [1,H_T]. Both are continuous functions of the continuous configuration path and of t. Initial eligibility is the original Borel condition that some internal belief KL exceeds 1/4 at time zero.

For each integer k>=1, the times satisfying

    A_I(t)<=sqrt(T),  B_I(t)>=1/2+1/k

form a closed subset of a compact interval. Their first time, or infinity for the empty set, is a measurable functional: existence before a fixed endpoint is tested by the minimum of the continuous maximum of the two constraint violations. Taking the infimum over k implements the original strict exterior inequality, because a continuous function strictly above 1/2 on a compact unit interval has a positive uniform margin. Comparing the finitely many block infima, with the same deterministic tie order in both arms and a cemetery mark on failure, gives a measurable K_T.

The infimum may fail to be attained. The agreed definition is the first-block mark ordered by these infima, not an assertion that the selected block has a qualifying interval completed exactly at that infimum. No probability-zero tie assumption is needed. This convention does not enter either dynamics.

Let E_T be the non-cemetery event. The existing frozen matching-seed witness is a subset of the full original contrast event and proves

    P_frozen(E_T)>=c(m_0)>0,
    c(m_0)=exp(-1/4)rho_0^12/737280
             *exp[-(|x_circ-m_0|+rho_0)^2/2],
    rho_0=1/100.

The seed is used only to lower-bound the probability of conditioning on the full event; it does not replace that conditioning event. The bound is temperature-independent for xi=T^(1/8)<=1/100 and is positive for each fixed mean. It is not uniform over all means.

The improved conditioning bound in the investigator's proof is correct. Let a_I,b_I be the non-cemetery mark probabilities, p=sum a_I and q=sum b_I, and d the TV distance of the cemetery-augmented laws. Then

    2d=sum_I|a_I-b_I|+|p-q|,  d<=d_T.

If p>=q>0, triangular comparison gives

    TV((a_I/p),(b_I/q))
       <=[sum_I|a_I-b_I|+(p-q)]/(2p)=d/p.

Exchange the arms if q>=p. Hence conditional TV is at most d/max(p,q)<=d_T/c(m_0). Moreover p>=c(m_0)-d_T, so both conditionals are defined when d_T<c(m_0). The usual extra factor two is unnecessary here because the cemetery-augmented comparison retains the success-probability discrepancy.

It follows that for every fixed mean,

    TV(Law_learn(K_T|E_T),Law_frozen(K_T|E_T))->0

whenever T->0 and epsilon_L T^(-1/4)->0. This includes every mobility below the Stage 1 caps T_n^a with a>7/2. The late learned/frozen matching and coherent-partition contrast can simultaneously tend to one-half on the much later selection window. These are distinct observables on distinct horizons.

## 8. Remaining obligations and validation scope

For epsilon_L=T^(1/8), the error bound is 8T^(-1/8) before clipping and yields no information. No positive or negative first-block result in that original coupled regime follows. Comparing different initial means, including a loop-coordinate change, is also outside this common-start coupling. The next result that would change the original first-block answer is a direct estimate in its actual regime or a stronger path comparison on that horizon, with its declared detector and conditioning probability preserved.

No unbounded first-ever stopping-time argument is used. In particular, the initial eligibility clause can fail at every block on a set of positive Gaussian probability; generic recurrence later in time does not repair it. The finite original-window argument avoids that obstruction and any unjustified conversion of stationary occupation into an entrance rate.

The proof check read the two Stage 2 investigator reports and their integrated manuscript sections, the source experiment/episode/gated-law definitions and proofs, the seeded probability floor, and SPEC R15. All new checks were analytical. No external literature, simulation, GPU work, symbolic run, Lean, tamper check, or full test suite was invoked. Compilation and label checks belong to the coordinating agent.

## Final source binding

The final `ca_selected_coherence.tex` was reread after its direct Euclidean-detector correction. Its event, partition, constants b=(8+3400L)T/a^2+8sqrt(2/pi)a and e=4T/a^2+4sqrt(2/pi)a, and the a=T^(1/4) invocation now agree with the original convention and the investigator report. `ca_first_block_comparison.tex` explicitly declares the infimum and nonattainment convention. No unresolved mathematical defect was found in these two proof files at the following revisions. The coordinating agent owns source-input integration, compilation, and the first-block report opening's wording alignment; the latter does not alter the already explicit manuscript convention.

| Proof file | SHA256 |
| --- | --- |
| Theory/ca_selected_coherence.tex | 5E83197DC279E2249B921D35DD955145C3C719501320FD84BD75BE4EB49A2255 |
| Theory/ca_first_block_comparison.tex | F7D4062633B71CA7B59760B8A2F9743D5CD759BE43DE6DC209DFFFAD1EA13C88 |

## Narrow intake of the completed Exa Stage 2 response

The completed `exa-stage2-result.md` was read after the local proofs. Its Section A occupation identity and native/held-path coupling agree with the independently checked argument in Sections 2–3 above. The local proof supplies complete explicit polynomial maximal bounds and the concrete a=T^(1/4), L=T^(-1/4) window. Exa's sharper exponential path bounds and its alternative growing-window formula are not dependencies of the manuscript and were not adopted or verified in this intake.

The local finite-horizon posterior identity is stronger than Exa's central-row derivative estimate: it gives the explicit bound min(1,2epsilon_L H^2) without an assumption epsilon_L H<=1/4. The original detector is already a measurable finite-history functional with a seeded probability floor c(m_0)>0, so the local proof applies directly on H_T=2T^(-1/8). It needs neither an almost-surely finite unbounded stopping rule nor Exa's newly defined hysteretic recurring detector. The proposed recurrence theorem, its target sets, and its R15 status remain unused and unverified here.

The generic caution about a conditioning denominator is resolved for the local original-window event by the existing seeded witness. In particular, the old seeded proposition also supplies its positive probability floor in the original coupled regime epsilon_L=T^(1/8). What this new estimate fails to settle in that regime is the learned/frozen first-block law, because the path-error bound is then vacuous; it is not absence of the established seed probability floor.

The response supplies no stronger proved conclusion for that original coupled regime. Its warnings distinguishing late coherence, first formation, and stationary recurrence are consistent with the local scope. No new source or theorem from this response was required or adopted. This intake changed only the verification report; neither manuscript proof nor the Research vault was edited.

Reviewed Exa output SHA256: `FF61849A1771357C0ECD7877A25462027E1957AE82FD080083AD3B955B683195`.
