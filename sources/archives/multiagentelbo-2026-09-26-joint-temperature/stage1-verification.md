# Stage 1 independent proof check

September 26, 2026. Worktree: `C:/tmp/multiagentelbo-selection-formation-20260926`. This check concerns Stage 1 only: continuation of the established fixed-temperature four-cycle selection result to a joint temperature–mobility schedule. The configuration, shared unoriented links, initial law, and source-learning equation are unchanged. No later formation stage was investigated.

## Verdict and exact scope

The diagonal selection construction and the explicit temperature-dependent entropy/tracking bounds are mathematically valid on their stated domains. They prove existence of a deterministic joint schedule, common to almost every fixed initial mean. They also prove a power-law regime for one-time tracking. They do not prove selection on an explicit power law, stabilization of the selected matching as temperature vanishes, or a path-law statement.

The integrated corollary's tolerance must be strictly positive; the first draft allowed the literal reading eta_n=0. This was corrected to eta_n in (0,1). The proof's initial label/sequence/cap mismatch was corrected by its owner. The final integrated corollary, joint proof, and compressed temperature proof are accepted within the scope stated here; their reviewed hashes appear below.

## 1. Target, model, and assumptions

The state is (X,sigma) in R^12 times {+1,-1}^4. The four unoriented edges each have one shared translation. At temperature T>0 the held-sheet dynamics is

    dX=-(H_sigma+T Omega)X dt+sqrt(2T)dW,

with a standard twelve-dimensional Brownian motion, no continuous-state boundary, and a rate-one clock that redraws the complete assignment from the conditional Gibbs law. The deterministic rows solve

    dp_i/dt=epsilon [q_t(sigma_i=+1)-p_i],  p_i(0)=1/2.

The supplied initial law is N(m,I_12) times uniform assignments, with a fixed mean m. The positive-temperature well-posedness, interior-row bound, finite-horizon entropy identity, and fixed-temperature selection theorem are inputs already proved in `Theory/ca_selection_proofs.tex`. This check reconstructed the new use of those inputs; it did not reopen every earlier lemma.

For a prescribed countable sequence 0<T_n<=T_0 with T_n decreasing to zero, strictly positive tolerances eta_n<1 tending to zero, and optional positive mobility caps h_n, the target is:

    There exist deterministic d_n decreasing to zero and a Lebesgue-null N
    such that for every fixed m outside N there is n_0(m), and for every
    n>=n_0(m) and every 0<epsilon<=d_n the stated errors are <=eta_n
    on [2 epsilon^(-1)log(1/epsilon),4 epsilon^(-1)log(1/epsilon)].

The thresholds are independent of m; the onset index can depend on m. The selected matching M_n(m) is independent of epsilon within each threshold interval but may depend on n. The exceptional set may depend on the prescribed countable sequence and tolerances. The equivalence controlled here is total variation of complete one-time laws, with relative entropy measured against the nonsingular instantaneous frozen law. It is not equivalence of complete histories.

The auxiliary standard Gaussian measure on the space of means is introduced only to construct thresholds. It is not an additional randomization of the physical initial mean. Its everywhere positive density makes its null sets exactly the Lebesgue-null sets.

## 2. Common window and fixed-temperature consequences

The earlier proof permits any C_T>1/alpha(T), independently of the mean. Its normalized weights satisfy 0<r_E,r_N,r_C<=1/8, so

    alpha=(3-2r_N-r_C)/(1+4r_E+2r_N+r_C)
         >=(21/8)/(15/8)=7/5.

Consequently C=2 is a valid common window coefficient. This does not make the mean-dependent escape radius or mobility threshold uniform in temperature or mean; the diagonal argument supplies the needed threshold quantifiers separately.

Write mu_{T,p} for the frozen invariant law and nu_T^M for its conditional Gaussian on matching M, tensored with delta_M. Conditional on a fixed assignment, that Gaussian is independent of p. Since each normalized sheet weight is at most the matching weight one,

    mu_{T,p}(M)>=pi_M>=1-sum_i |p_i-p_i^M|,
    TV(mu_{T,p},nu_T^M)=1-mu_{T,p}(M).

The fixed-temperature row convergence and tracking therefore imply convergence of the full learned one-time law to nu_T^{M_T(m)}. The actual learned entropy tends to zero as well: apply the square-root entropy tracking estimate itself, rather than trying to infer relative entropy from total variation. Frozen entropy decays exponentially at fixed T because its moving-reference term is absent and its entropy-production rate at p=1/2 is positive. Its initial entropy is finite for every fixed m.

Thus all five errors in the diagonal investigator's note tend to zero at each fixed T outside the imprint zero set: row distance, learned full-law total variation, learned relative entropy to mu_{T,p(t)}, frozen total variation, and frozen relative entropy to mu_{T,1/2}. Relative entropy to nu_T^M is not claimed; it would be infinite at finite time because the actual law still gives positive mass to other assignments.

## 3. Measurability and uniformity over every small mobility

This is the load-bearing point in upgrading separate fixed-temperature limits to one threshold valid for all real mobilities below it.

Fix T>0, a finite horizon H, a compact set of means, and a compact interval of positive mobilities. The row bound gives a common delta>0 such that all rows lie in [delta,1-delta]. Each receiver's posterior probability is uniformly Lipschitz in its prior row on this set, independently of X. For two coupled processes at the same T, let D(t) denote a total-variation upper bound for their laws and P(t) the maximum row difference. Maximal coupling of their initial Gaussian laws, then shared Brownian motion and clocks until the first different redraw, gives

    D(t)<=D(0)+L int_0^t P(s) ds.

Subtracting the learning equations gives, with epsilon_* the maximum mobility,

    P(t)<=H |epsilon-epsilon'|+epsilon_* int_0^t[D(s)+P(s)] ds.

Gronwall therefore proves finite-horizon continuity in mean and positive mobility. The initial Gaussian total variation is continuous in its mean. Time continuity of the full laws follows from strong L1 continuity of each Gaussian OU semigroup and the forward integral formula; the source is L1-integrable. This continuity can also be checked first on compactly supported smooth densities and extended by the L1 contraction of the Markov kernels.

Relative entropy is continuous on the same compact parameter sets. The earlier proof's upper and positive lower Gaussian envelopes are uniform there. They bound the logarithms of both densities by C(1+|X|^2), while the upper envelope supplies an integrable Gaussian-times-polynomial bound for the entropy integrand. An L1-convergent density sequence has an almost-everywhere convergent subsequence; dominated convergence proves entropy convergence on that subsequence. Applying the argument to every subsequence proves continuity of the full sequence. The frozen reference density varies continuously with the rows.

Parametrize each window as t=u t_L(epsilon), u in [1,2]. Its error supremum is consequently continuous in positive epsilon. The matching is Borel in m because it is selected by the sign of the analytic imprint, with any fixed convention on its zero set. Hence the error is Borel in m and its supremum over 0<epsilon<=r equals the supremum over rational epsilon in that interval. Continuity from below includes an irrational right endpoint. There is no need for uniform continuity as epsilon approaches zero.

The final integrated proof uses a simpler route for entropy measurability: replace the two actual entropy suprema by their explicit continuous upper bounds. With G_T=sup_p ||g(p)||_1, ell_T(epsilon)=c_T/[K_T+8log2+32log(1/epsilon)], and lambda_u=c_T/[K_T+8log2], these are B_L=[exp(-ell_T t_L/2)sqrt(H_0)+epsilon G_T/(sqrt2 ell_T)]^2 and B_F=exp(-lambda_u t_L)H_0. Direct integration of the square-root entropy comparison proves both bounds. H_0 is the continuous quadratic expression in Section 5 below, and both bounds tend to zero at fixed T and m. Thus the final proof does not depend on the separate entropy-continuity argument reconstructed above.

Let E_n(epsilon,m) be min(1, the maximum of the row error, two total-variation errors, and B_L,B_F), and F_n(r,m)=sup_{0<epsilon<=r}E_n(epsilon,m). These functions are measurable, bounded by one, and F_n(r,m) tends to zero for almost every m at each fixed n. Dominated convergence under rho=N(0,I_12) gives int F_n(r,m)rho(dm)->0.

Choose dyadic d_n=2^(-k_n), recursively, satisfying

    d_n<=min(e^(-1),2^(-n),h_n,d_{n-1}/2),
    int F_n(d_n,m)rho(dm)<=eta_n 2^(-n).

The preceding limit proves that such an integer k_n exists. No computability of the threshold is inferred. With B_n={m:F_n(d_n,m)>eta_n}, Markov's inequality gives rho(B_n)<=2^(-n), and

    rho(union_{n>=N}B_n)<=2^(1-N)->0.

Therefore only finitely many B_n occur for almost every fixed m. Removing also the countable union of imprint zero sets proves the target quantifiers. Because eta_n<1, an upper bound on the clipped error bounds the row and total-variation errors and both entropy majorants, hence each original error. Independence of the events is unnecessary.

This proof does not require geometric temperatures. The geometric sequence in the first investigator draft can be replaced verbatim by any prescribed countable positive T_n->0 within the fixed-temperature theorem's interval. It also accepts arbitrary positive caps; choosing h_n=T_n^a only imposes epsilon<=T_n^a and does not establish the equality epsilon=T_n^a.

## 4. Explicit temperature constants and full-state tensorization

The active/passive reduction is exact. With u=(k+m)/sqrt2, v=(k-m)/sqrt2, and R=[D,-sqrt2 I], the common passive space K=ker R direct-sum ker D has dimension five. Every H_sigma vanishes on K; Omega preserves K and K-perp. The passive drift rates are T four times and 5T once. Costs and redraw probabilities depend only on the seven-dimensional active complement. Rescaling active coordinates by T^(-1/2) gives unit diffusion and precision a_sigma=(H_sigma+T Omega)|_{K-perp}. Relative entropy is unchanged by this invertible coordinate transformation at fixed T.

Since RR^T has eigenvalues 2,4,4,6, while D^TD has eigenvalues 0,2,2,4, multiplicities at most two give ||H_sigma||<=12. Thus, for 0<T<=1/100,

    T I<=a_sigma<=13 I.

Dividing the full determinant table by the common passive determinant 5T^5 yields active determinant bounds

    5120T^3<=d_M<=5262T^3,
    896T<=d_E<=1017T, 896T<=d_N<=2175T,
    3072<=d_C<5120.

All polynomial coefficients are positive. Endpoint evaluation at T=1/100 proves the upper bounds; constant terms prove the lower bounds. These imply the claimed class ordering, w_M<=T^(-3/2)/sqrt5120 and w_C/w_M>=T^(3/2).

The radius-one-half ball in R^7 has volume pi^3/840, and

    K_0=(2pi)^(7/2)/[(pi^3/840)sqrt5120]=210sqrt(2pi/5).

The Gaussian-to-ball comparison and the prior-weighted jump comparison give the continuous and jump form coefficients

    C_c<=(2+8K_0 exp(13/8)) L_p T^(-5/2),
    C_j<=4K_0 exp(13/4) L_p T^(-5/2),
    L_p=4+2log(1/q_min)<=4+3log(1/T)+8log(1/p_min).

Diffusion production equals four times its quadratic form; jump production is at least four times its quadratic form. Therefore

    c_*=min{2/[1+4K_0 exp(13/8)],1/[K_0 exp(13/4)]}

is the claimed valid constant. The passive Gaussian entropy contraction is at least 2T. Tensorize entropy over the independent invariant factors; Cauchy–Schwarz bounds the energy of each marginal by the corresponding integrated energy. The full rate is at least the minimum of the active rate and 2T. Since c_*<1, T<=1, and the denominator is at least four, the displayed active lower bound is below 2T. The result therefore controls full-state entropy, not merely the active marginal.

No issue was found in this part of either the detailed report or its compressed manuscript proof. The argument is for the rate-one complete-assignment redraw generator actually specified by the model.

## 5. Fitness, tracking, and initial-layer scope

A one-receiver flip connects only M–E, N–E, or C–E determinant classes. The above bounds put each ratio, in either direction, below 1/T. Comparing the two positive evidence sums in one row gives |g_i|<=1/T and ||g||_1<=4/T.

On the central cube [1/4,3/4]^4, multilinearity gives |partial_i g_i|<=16. For i!=j,

    partial_j g_i=Cov(1_{sigma_i=+},1_{sigma_j=+})/
                   [p_i(1-p_i)p_j(1-p_j)],

so |partial_j g_i|<=64/9. Summing the four diagonal and twelve off-diagonal entries gives 448/3<150, the claimed temperature-independent Lipschitz constant.

The initial relative entropy satisfies

    H_0=log Z-6+(1/32)sum_sigma[tr B_sigma+m^TB_sigma m]
       <=13(12+|m|^2)/(2T).

Writing h=sqrt(H/2), the actual-law entropy identity gives

    h(t)<=exp(-Lambda(t)/2)sqrt(H_0/2)
          +(epsilon/4)int_0^t exp(-(Lambda(t)-Lambda(s))/2)||g(p(s))||_1 ds.

For C=2 the row bound on the entire horizon t<=2t_L gives

    D=4+3log(1/T)+8log2+32log(1/epsilon),
    ell=c_*T^(5/2)/D.

Integration proves exactly the manuscript bound

    TV(q_t,mu_{p(t)})
    <=exp(-ell t/2)sqrt[13(12+|m|^2)/(4T)]
      +2epsilon D/[c_*T^(7/2)].

For epsilon=T^a with a>7/2, the second term is O(T^(a-7/2)log(1/T)) and the initial exponential dominates the T^(-1/2) factor uniformly for bounded m. Thus the power-law tracking statement is valid.

The detailed investigator report's quantitative initial-layer estimates were also checked. Frozen contraction gives ||I||_infty<=B=2A/lambda_Q; the three errors in the imprint expansion are bounded respectively by the frozen tail B exp(-lambda_Q tau/2), the exponential learning-kernel correction epsilon tau B, and the clock-coupling integral epsilon tau^3/(6c_0). The entropy layer bound A exp(-lambda_Q tau/2)+L epsilon^2 tau/(4lambda_Q), and the subsequent relative-plus-absolute error bound, follow by direct integration of the displayed h inequality. Their proposed additional conditions suffice for those error estimates relative to an assumed imprint floor. The report does not assert that this floor holds or that these estimates alone prove joint selection.

## 6. Frozen matching weights and contrast

At uniform frozen rows each matching has the exact stationary mass

    1/[2+8r_E+4r_N+2r_C]=1/(2D_0(T)).

It is generally below one-half at positive T. Since r_E,r_N=O(T) and r_C=O(T^(3/2)), this tends to one-half. The diagonal's uniform frozen-law convergence transfers the limit to the actual frozen process on its growing windows.

The five-error construction also proves a one-time assignment-law contrast. Pushing the two total-variation estimates to the assignment space yields

    |TV(q_learn^S,q_frozen^S)-[1-1/(2D_0(T_n))]|<=2eta_n.

Hence the contrast tends to one-half even if the chosen matching varies with n. This is neither a first-entrance probability nor a conditional formation event.

## 7. Corrections, executed check, and unresolved obligation

The initial integrated corollary needed strictly positive tolerances; zero tolerance cannot hold at finite mobility and finite time because the Gaussian initialization, positive rows, and positive redraw probabilities preserve positive mass on all assignments. That correction is already visible in the current c14 source. The initial proof referred to a theorem label not defined by the corollary and specialized the temperature sequence without stating the additional cap variable. The final proof now refers to `cor:phil-joint-selection`, uses the arbitrary prescribed sequence in the corollary, and defines h_n=T_n^a while explicitly proving the stronger arbitrary-positive-cap construction. These integration defects are corrected.

One new tiny exact calculation was executed with `C:/Python314/python.exe` using only `fractions.Fraction`. It checked the determinant endpoint fractions and inequalities, class ordering bounds, alpha>=7/5, and 448/3<150. Output:

    Exact endpoint determinant bounds, class ordering inequalities,
    alpha >= 7/5, and central derivative constant checked.
    dM/T^3 = 4209544161/800000
    dC = 2644916750113761/800000000000

The calculations support the finite algebra; the arguments above establish the general inequalities and quantifiers. No new external source, simulation, GPU work, Lean, tamper check, or broad test suite was used. The live `Research/manuscripts/pifb2/13_section.tex` was read for the existing scope distinction; it was not edited. Only this assigned verification artifact was written.

The remaining mathematical obligation for explicit power-law selection is quantitative control of the actual fixed-mean temperature-dependent imprint and the error terms relative to it, including any transverse-to-matching imprint ratio needed by the escape proof. A fixed limiting matching additionally requires eventual sign control or another label-identification argument. Fixed-temperature analytic nonvanishing does not supply either result. The next action that would change the explicit-selection answer is to prove those model-specific bounds; stages about coherence or parents are outside this proof check.

## Final integrated-source binding

The final files were read after the tolerance, label, temperature-sequence, mobility-cap, and entropy-majorant changes. `ca_selection_proofs.tex` includes both new proof inputs. No unresolved mathematical defect was found in the Stage 1 statements at these revisions. SHA256 values identify the reviewed sources; they are revision metadata, not substitutes for the derivations above.

| Reviewed file | SHA256 |
| --- | --- |
| Theory/ca_selection_proofs.tex | 4D0EB4116F5ED79912972E54D415C7481A9CF92464CEE8180E8A665854DB3B76 |
| Theory/ca_joint_selection.tex | 2675DFCDCDE62C13122600D36EF9294A72C5B150AE7340AFC009FFB8AB8D2122 |
| Theory/ca_temperature_bounds.tex | 97BFAED049848F99A908CD368D0D607D091FA6385308513BA73903490CDAAC88 |
| Theory/c14_interpretation.tex | 4F9CB19B2AFE798BE9EB017A3AFE63D999909787AD674D1422F0F65FAB121214 |
| docs/derivations/2026-09-26-selection-to-formation/stage1-temperature-bounds.md | 4406C545C29B1061A8DD222B9F3FC4FBE20A92F97C6974CCB32F83710D48E587 |
| docs/derivations/2026-09-26-selection-to-formation/stage1-diagonal-selection.md | 95DBE66202E524B1E38F7F59C090AAB3F54EF248E498D1FCD831A031DE7C78C9 |