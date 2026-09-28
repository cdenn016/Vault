# Stage 4, obligation 1: hidden information of the seeded early prefix

Author model: Claude Opus 5.5 (claude-opus-5-5). Verifier model: Claude Fable 5.1 (claude-fable-5-1), verdict VALID_WITH_MINOR_ISSUES with no critical or major defect; report `stage4-crossmodel-hidden-info.md` in this folder. The defect fixes listed in that report were applied afterwards by Claude Opus 5.5 and have not been re-verified. Date: 2026-09-28. Scope: fixed base point c_*, no base transport, no Lean. Sources read: c14_interpretation.tex (prop:phil-seeded-contrast-formation), c13_formation.tex (def:rg-formation-cycle-experiment, prop:rg-formation-endogenous-cycle, open:rg-formation-adaptive-family), ca_formation_proofs.tex (proofs of both propositions), ca_parent_conditional.tex, ca_parent_dynamics.tex, ca_first_block_comparison.tex, SPEC.md R13 to R16, and the Stage 3 records in this folder.

## Result

The event-specific bound holds at the original mobility eps_L = eps = T^(1/8), and no slow schedule is needed. Condition the actual learned recognition law on the seeded first-contrast prefix E_theta (initial configuration in one of the two seed balls about +x_circ or -x_circ, initial assignment a perfect matching M, silent clock on [0,1/4], a noise tube and no change of assignment on [0,theta]). At a deterministic activation time theta, the mean discarded conditional relative entropy against the restricted optimizer satisfies

    H_opt(Law(X_theta,S_theta | E_theta)) <= kappa(theta) = [eta(theta) + h_b(p_theta)] / (1 - p_theta),
    eta(theta) = 9 rho_circ^2 e^(-8 theta) / (2T) + 3 e^(-16 theta) / (4 (1 - e^(-8 theta))),

and the evaluator-retaining physical one is at most kappa(theta) + log((4+5T)/(4+T)) <= kappa(theta) + T. Here p_theta bounds the failure of the remainder given the seed, and the seed probability, which is only bounded below, does not enter. The bound is uniform in the Gaussian mean m_0. It tends to zero exactly on the activation range theta - log(1/eps) -> infinity, theta = o(eps^(-4)). On the source window [t_eps, t_star] it is O(T^(1/2) log^2(1/T)) with the source's Chebyshev tube, and at most (9/2) rho_circ^2 T (1 + o(1)) with the sub-Gaussian tube proved below (with equality in the leading term at theta = t_eps). The source rows enter only through the ratio 2e^(eps_L theta) - 1, which is at most 1.215 at the original data, so the bound holds for every mobility with eps_L theta <= 1/(2T).

The activation time matters in the opposite direction as well. For theta = log(1/eps) - s the same conditional law has discarded relative entropy at least a positive constant (depending on m_0) times e^(8s), minus log 2; at theta = (1/2)log(1/eps) + 1, near the first qualifying completion time, the lower bound is (rho_circ^2/7) e^(-8) e^(-2 rho_circ (|m_0| + 2 + rho_circ)) T^(-1/2) (1 + O(T log(1/T))) - log 2, which is of order T^(-1/2) only as eps -> 0. Its constant is about 4.6e-9 at m_0 = 0, so at eps = 1/100 the bound is vacuous (about -0.23) at that theta and turns positive only for eps <= 0.009, while at theta = (1/2)log(1/eps) + 0.2, closer to the first qualifying completion, it is about 276 at eps = 1/100. The threshold log(1/eps) = (1/8)log(1/T) is therefore sharp up to an additive O(1). The bound also holds for the native future marginals under the fixed prefix, with an additional term that tends to zero (super-polynomially in T for t <= eps^(-4)/log^2(1/eps)), and for a path-observable version of the prefix.

## 1. Setting and definitions

### 1.1 The learned four-cycle at mobility eps_L

Use the homogeneous four-cycle of def:rg-formation-cycle-experiment. A configuration is x = (kbar, mbar, omega) in R^12, with residuals r^b_i = kbar_{i+1} - kbar_i - omega_i and r^m_i = mbar_{i+1} - mbar_i - omega_i, residual covectors a^b_i, a^m_i of norm sqrt(3) and Gram matrix [[3,1],[1,3]], and edge cost D_{e_i} = [(r^b_i)^2 + (r^m_i)^2]/2. An assignment is S in J = prod_i {i-1, i+1}. Then

    V_S(x) = sum_i D_{e(i,S_i)}(x) = x^T H_S x / 2,     H_S = sum_i (a^b a^bT + a^m a^mT)_{e(i,S_i)},
    U_S(x) = x^T K_S x / 2,                             K_S = H_S + T (I + R_ev),     R_ev = 2 D^T D,

where D x = kbar - mbar, 0 < eps <= 1/100, and T = eps^8. Each summand of H_S has norm 4 and ||R_ev|| = 4, so ||K_S|| <= 16 + 5T for every S. The receiver rows pi_ij(t) form the product prior pi_S = prod_i pi_{i,S_i}; the posterior rows are

    beta_ij(x; pi) = pi_ij e^(-D_{e(i,j)}(x)/T) / sum_{j'=i+-1} pi_ij' e^(-D_{e(i,j')}(x)/T).

The kinetics are dX = -K_{S_t} X dt + sqrt(2T) dW between the rings of a rate-one clock; at a ring tau the complete assignment is redrawn, receiver i taking source i+1 exactly when a fresh uniform variable U_{tau,i} is at most beta_{i,i+1}(X_{tau-}; pi(tau)). The rows learn by pi_ij' = eps_L (q_t(S_i=j) - pi_ij) from pi_ij(0) = 1/2, where q_t = Law(X_t, S_t). The initial law is N(m_0, I_12) times the uniform law on J. The original regime of prop:phil-seeded-contrast-formation is eps_L = eps.

Part (a) of prop:phil-seeded-contrast-formation gives existence and uniqueness of the rows; its contraction argument uses the mobility only as a positive constant, so it holds for every eps_L > 0 (and trivially for eps_L = 0). The rows are deterministic and continuous, and the variation-of-constants formula with 0 <= q <= 1 gives

    |pi_ij(t) - 1/2| <= (1 - e^(-eps_L t)) / 2.                                                   (1.1)

The restricted optimizer at rows p is mu_{T,p}(dx, S) proportional to pi_S(p) e^(-U_S(x)/T) dx. For fixed rows the kinetics leave it invariant (proof of prop:phil-seeded-contrast-formation(b)).

### 1.2 Driving data and filtration

The initial data (X_0, S_0), a twelve-dimensional Brownian motion W, a rate-one Poisson clock with ring times tau_1 < tau_2 < ..., and independent uniform variables U_{k,i} are mutually independent. Let F_t be generated by (X_0, S_0), W on [0,t], the clock on [0,t], and the uniforms of rings in [0,t]. The pair (X,S) is F-adapted, and given F_s its future is a measurable function of (X_s, S_s) and the driving increments after s, which are independent of F_s.

### 1.3 Matching geometry

The perfect matchings are S^(0) = (1,0,3,2), selecting edges e_0, e_2, and S^(1) = (3,2,1,0), selecting e_1, e_3. For an edge g put n^+_g = (a^b_g + a^m_g)/(2 sqrt 2) and n^-_g = (a^b_g - a^m_g)/2. For a matching M with edges e, f let F_M have the orthonormal columns (n^+_e - n^+_f)/sqrt 2, n^-_e, n^-_f, and put Z_M = im F_M and W_M = Z_M^perp, of dimension nine. The source (proof of prop:rg-formation-endogenous-cycle, paragraphs Matching sector and Parent channel) and the exact check stage3-projection-check.py establish that K_M preserves W_M and Z_M, with

    K_M F_M = F_M K_Z,     K_Z = diag(8+T, 4+5T, 4+5T).

Write x = y + F_M z with y = P_{W_M} x and z = F_M^T x. The selected covectors satisfy a^b_g = sqrt 2 n^+_g + n^-_g and a^m_g = sqrt 2 n^+_g - n^-_g, so they lie in the span of eigenvectors of K_M with eigenvalues 8+T and 4+5T, all at least 4.

Let x_circ = (0, 0, 1_4). Every residual of x_circ equals -1, so

    F_M^T x_circ = 0   and   F_M^T (-x_circ) = 0   for both matchings,                           (1.2)

because the three columns of F_M evaluate to ((r^b_e + r^m_e) - (r^b_f + r^m_f))/4, (r^b_e - r^m_e)/2, and (r^b_f - r^m_f)/2 at x_circ. This was also checked in exact rational arithmetic (Section 12). The held path from x_circ is, by eq:rg-formation-cycle-center for S^(0) and by the rotation i -> i+1, which fixes x_circ and maps S^(0) to S^(1),

    e^(-K_M t) x_circ = e^(-Tt) [x_circ + (1 - e^(-8t)) p_M / 4],
    selected residuals = -e^(-(8+T)t),     exterior residuals = e^(-Tt) (-3/2 + e^(-8t)/2),       (1.3)

in both channels, where p_M is the sum of a^b_g + a^m_g over the edges of M. By linearity the path from -x_circ is the negative of (1.3). A floating-point check of (1.3) for all sixteen residual evaluations (four edges, two channels, two matchings) at both signs agrees to 1.6e-15.

### 1.4 Held process, seeds, remainder, and prefix

For a matching M define the held process and its noise

    Xtilde^M_t = e^(-K_M t) X_0 + Z^M_t,     Z^M_t = sqrt(2T) int_0^t e^(-K_M (t-u)) dW_u,

and the tube event N^M_t = {sup_{u<=t} |Z^M_u| <= delta_eps} with delta_eps = eps^2/(8 sqrt 3). Put rho_circ = 1/100, t_eps = 2 log(1/eps), and t_star = t_eps + 1. For sigma in {1,-1} and a matching M define

    B_{sigma,M} = { |X_0 - sigma x_circ| < rho_circ, S_0 = M, no ring in [0,1/4] },
    A^M_t       = N^M_t  intersect  { S_u = M for all u in [0,t] },
    E_theta     = disjoint union over (sigma,M) of B_{sigma,M} intersect A^M_theta.

The four seeds are disjoint because |x_circ| = 2 > rho_circ and S_0 distinguishes the matchings. Every E_theta is in F_theta. Independence of the initial data and the clock gives

    P(B_{sigma,M}) = (e^(-1/4)/16) N(m_0, I_12){|x - sigma x_circ| < rho_circ},
    b(m_0) := P(union of the four seeds) = (e^(-1/4)/8) sum_{+-} N(m_0, I_12){|x -+ x_circ| < rho_circ} >= 2 c(m_0),

with c(m_0) the floor of prop:phil-early-block-null. On B_{sigma,M} intersect {S_u = M for u <= t} the native configuration equals Xtilde^M on [0,t]: both solve the same linear equation with the same Brownian path between rings, and configurations are continuous at rings.

For t >= theta write q^{E_theta}_t = Law(X_t, S_t | E_theta). This conditions on one completed prefix; the deterministic native row path is not recomputed from the conditioned law. The parent activation law is mu_act = C_# q^{E_theta}_theta, with C below.

### 1.5 Channel and hidden functionals

The channel of prop:rg-formation-endogenous-cycle(b) is C(x,S) = (S, P_{W_S} x), with W_S = W_M on the two matchings and W_S = R^12 otherwise. Its target is the disjoint union Y of the strata {S} x W_S. On a matching stratum the reference hidden kernel is

    kappa_S = nu_{T,Z} = N(0, T K_Z^(-1))   on the coordinates z = F_S^T x,

and off the matchings nothing is discarded. For every strictly positive row vector p, mu_{T,p} has hidden conditional kappa_S at every retained point, because the prior factor pi_S(p) cancels at fixed S and K_S preserves W_S and Z_S. For a law q on R^12 x J define

    H_opt(q) = int C_#q(dS,dy) KL(q(dz | S,y) || kappa_S),

the zero contribution off the matchings included. This is the mean discarded conditional relative entropy against the restricted optimizer of ca_parent_conditional.tex, for every positive choice of rows.

For H_phys lift q by the recognition evaluator of eq:rg-formation-evaluator-lift: at configuration x, m = mbar + xi and k = kbar + xi + xi' with xi, xi' independent N(0, I_4/2), so that the evaluator sample U = (m,k) has law nu*_x(dU) = N(m; mbar, 1/2) N(k-m; D x, 1/2). The physical joint of the four-cycle has configuration prior N(0, I_12), record likelihoods (1/2) e^(-D/T), prior rows, and evaluator N(m; mbar, 1/2) N(k-m; 0, 1/2), so its posterior given the observed records is proportional to pi_S e^(-(V_S(x) + T|x|^2/2)/T) N(m; mbar, 1/2) N(k-m; 0, 1/2). Then H_phys(q) is the mean, over the retained variables (S, y, U) of the lifted law qbar = q(dx,S) nu*_x(dU), of KL(qbar(dz | S,y,U) || Pi^phys(dz | S,y,U)). The prior rows cancel in these hidden conditionals as well.

## 2. Entropy calculus

The one standard fact used is the chain rule for relative entropy: for laws P, Q on a product of standard Borel spaces with regular conditional laws, KL(P_{AB} || Q_{AB}) = KL(P_A || Q_A) + int P_A(da) KL(P_{B|a} || Q_{B|a}) in [0, infinity]. Its specialization to C is thm:rg-exact-coarse-vfe. Applying it in the other order and dropping the nonnegative conditional term gives data processing under marginalization.

**Lemma 1.** Let kappa be a kernel from Y to the hidden space, and for a law q on Y x Z set H(q) = int q_Y(dy) KL(q(.|y) || kappa_y).

(a) For every law lambda on Y, KL(q || lambda (x) kappa) = KL(q_Y || lambda) + H(q). Hence H(q) = min over lambda of KL(q || lambda (x) kappa), attained at lambda = q_Y.

(b) Let B be a random variable with finitely many values, jointly distributed with R = (R_Y, R_Z) of law q, and let q_b = Law(R | B=b) with weights w_b = P(B=b). Then

    sum_b w_b H(q_b) = H(q) + I(B; R | R_Y),     0 <= I(B; R | R_Y) <= H(B).

For binary B with P(B=0) = r this is (1-r) H(q_1) + r H(q_0) = H(q) + I, with I <= h_b(r).

(c) H is convex: H(sum_b w_b q_b) <= sum_b w_b H(q_b).

(d) If (Y, V, Z) are jointly distributed with Y in the retained space, then H(Law(Y,Z)) <= E KL(Law(Z | Y,V) || kappa_Y).

(e) If H(q) <= eta, P(B=0) = r <= pbar < 1/2, then H(q_1) <= (eta + h_b(pbar))/(1 - pbar).

(f) For laws P, Q and measurable f >= 0 with E_Q e^f < infinity, KL(P || Q) >= E_P f - log E_Q e^f.

Proof. (a) is the chain rule through Y, since lambda (x) kappa has conditional kappa_y.

(b) Let J = Law(B, R) and let Jhat be the law obtained by drawing (B, R_Y) from its actual joint law and then R_Z from kappa_{R_Y}. The chain rule through (B, R_Y) gives KL(J || Jhat) = E KL(Law(R_Z | B, R_Y) || kappa_{R_Y}) = sum_b w_b H(q_b). The R-marginal of Jhat is q_Y (x) kappa, and under Jhat the variable B is conditionally independent of R_Z given R_Y, so Jhat(B | R) = Law(B | R_Y). The chain rule through R therefore gives KL(J || Jhat) = H(q) + E KL(Law(B | R) || Law(B | R_Y)). For discrete B the tower property gives E KL(Law(B|R) || Law(B|R_Y)) = H(B | R_Y) - H(B | R), which lies in [0, H(B | R_Y)] because conditional entropies of a discrete variable are nonnegative, and H(B | R_Y) <= H(B). The identity holds in [0, infinity]; when H(q) is finite every term is finite.

(c) follows from (b) because the information term is nonnegative.

(d) By the chain rule, KL(Law(Y,V,Z) || Law(Y,V) (x) kappa) = E KL(Law(Z|Y,V) || kappa_Y). Marginalizing V maps the reference to Law(Y) (x) kappa, so data processing and (a) with lambda = Law(Y) bound the left side below by H(Law(Y,Z)).

(e) By (b), (1-r) H(q_1) <= eta + h_b(r) <= eta + h_b(pbar), since h_b increases on [0,1/2], and 1 - r >= 1 - pbar. For r = 0 the claim is H(q) <= eta.

(f) If KL(P||Q) is infinite there is nothing to prove. Otherwise let Q_f = e^f Q / E_Q e^f; then log(dP/dQ) = log(dP/dQ_f) + f - log E_Q e^f. Since P << Q_f and the negative part of a log-likelihood ratio has P-integral at most 1/e, the bound f <= (log(dP/dQ))^+ + (log(dP/dQ_f))^- + log E_Q e^f and KL(P||Q) < infinity give E_P f < infinity, so every term below is finite (and KL(P||Q_f) >= 0), and integration against P gives KL(P||Q) = KL(P||Q_f) + E_P f - log E_Q e^f >= E_P f - log E_Q e^f. QED.

## 3. Deterministic geometry of a held seed

**Lemma 2.** Let sigma in {1,-1}, M a matching, |X_0 - sigma x_circ| < rho_circ, and suppose sup_{u<=s} |Z^M_u| <= delta_eps. Write Xtilde = Xtilde^M. For all u in [0,s]:

(i) |F_M^T X_0| < rho_circ.

(ii) Every selected residual r (either edge of M, either channel) satisfies |r(Xtilde_u)| <= e^(-(8+T)u) + sqrt3 rho_circ e^(-4u) + sqrt3 delta_eps, and every exterior residual satisfies |r(Xtilde_u)| >= e^(-Tu)(3/2 - e^(-8u)/2) - sqrt3 (rho_circ + delta_eps).

(iii) If u >= 1/4 and Tu <= 1/12, selected residuals are below 1/5 and exterior ones above 13/10 in magnitude, so each receiver's exterior cost exceeds its partner cost by more than 169/100 - 4/100 > 1.

(iv) If u >= (1/2) log(1/eps), selected residuals are at most 0.143 eps^2, so internal belief and model relative entropies are at most eps^4.

(v) At u = 0 the internal belief relative entropy of each matched pair exceeds (1 - sqrt3 rho_circ)^2/2 > 0.48; if Tu <= 1/12, every exterior belief relative entropy exceeds 0.48 on [0,s], and exceeds 1/2 on [1/4, s].

Proof. (i) follows from (1.2): |F_M^T X_0| = |F_M^T (X_0 - sigma x_circ)| <= |X_0 - sigma x_circ|. For (ii) write r(Xtilde_u) = sigma a.e^(-K_M u) x_circ + (e^(-K_M u) a).(X_0 - sigma x_circ) + a.Z_u, with a the residual covector. The first term is given by (1.3). For a selected covector |e^(-K_M u) a| <= sqrt3 e^(-4u), because a lies in the span of eigenvectors with eigenvalues at least 4; for an exterior covector |e^(-K_M u) a| <= sqrt3 because K_M is positive semidefinite. The third term is at most sqrt3 delta_eps. (iii): e^(-2) + sqrt3 (rho_circ + delta_eps) = 0.1527 < 1/5, and e^(-1/12)(3/2 - e^(-2)/2) - sqrt3 (rho_circ + delta_eps) = 1.30048 > 13/10. The internal cost [(r^b)^2 + (r^m)^2]/2 is then below 1/25 and the exterior one above (13/10)^2. (iv): with u = (1/2)log(1/eps) + v, v >= 0, the bound of (ii) equals eps^2 [eps^2 e^(-8v - Tu) + sqrt3 rho_circ e^(-4v) + 1/8] <= 0.143 eps^2; the belief relative entropy is (r^b)^2/2 and the model one is (r^m)^2/(2 sigma_ev^2) = (r^m)^2. (v): the entrance value follows from (ii) at u = 0, where selected residuals are within sqrt3 rho_circ of -sigma; on [0,1/4] the exterior bound of (ii) is at least e^(-T/4) - 0.0174 > 0.98, and on [1/4,s] it exceeds 13/10. QED.

**Consequence for the contrast event.** Let theta >= (1/2)log(1/eps) + 1 and T theta <= 1/12. On B_{sigma,M} intersect A^M_theta both matched pairs of M enter the contrast at time zero, have internal belief and model relative entropies at most eps^4 on the completed interval [(1/2)log(1/eps), (1/2)log(1/eps)+1], which lies inside [0, 2/eps], and have boundary belief relative entropies above 1/2 there. Hence E_theta is contained in the contrast-formation event of prop:phil-seeded-contrast-formation and in the event E_T of prop:phil-early-block-null (same resolution sqrt T = eps^4 and horizon 2 T^(-1/8) = 2/eps). Every other eligible block (a non-matched pair, or a path of three vertices) contains an edge exterior to M, whose belief relative entropy exceeds 0.48 > eps^4 on [0, theta]; so on E_theta the first-block mark K_T is one of the two pairs of M, its least qualifying completion time is at most (1/2)log(1/eps) + 1 <= theta, and the mark is determined by the path on [0, theta].

## 4. Rows at mobility eps_L and the remainder probability

**Lemma 3.** For every eps_L >= 0, every receiver i with sources j, k, and every t >= 0,

    pi_ik(t)/pi_ij(t) <= r(t) := 2 e^(eps_L t) - 1,
    beta_ik(x; pi(t)) <= r(t) exp(-(D_{e(i,k)}(x) - D_{e(i,j)}(x))/T),
    beta_ij(x; pi(t)) / beta_ij(x; 1/2) <= r(t).

At eps_L = eps and t <= t_star, r(t) <= 2 e^(0.10211) - 1 = 1.2150 < 1.23.

Proof. By (1.1) every entry lies in [e^(-eps_L t)/2, 1 - e^(-eps_L t)/2], whose endpoint ratio is 2e^(eps_L t) - 1. The second inequality drops the partner term from the denominator of beta_ik. For the third, with A and B the two likelihood factors and p the row entry, beta(p)/beta(1/2) = p(A+B)/(pA + (1-p)B) <= max(1, p/(1-p)), because pA + (1-p)B >= min(p, 1-p)(A+B). The value eps t_star <= 0.10211 at eps = 1/100 is the source's monotonicity bound. QED.

**Lemma 4.** Let theta >= 1/4 with T theta <= 1/12. For every seed,

    P((A^M_theta)^c | B_{sigma,M}) <= p_theta := tau_theta + 4 r(theta) (theta - 1/4) e^(-1/T),
    tau_theta := P(sup_{u<=theta} |Z^M_u| > delta_eps) <= min{ 73728 eps^4 theta, 24 exp(-eps^(-4)/(36864 theta)) }.

At eps_L = eps and theta <= t_star, 4 r(theta) <= 4.86, so p_theta <= ptilde_eps = 73728 eps^4 t_star + 5 t_star e^(-1/T) of the source.

Proof. Tube. The tube event depends only on W, which is independent of the seed, so its conditional failure equals tau_theta. The Chebyshev bound is the source's (Doob's L^2 inequality and 384 T theta / delta_eps^2 = 73728 eps^4 theta). For the sub-Gaussian bound, take an orthonormal eigenbasis v_k of K_M with eigenvalues lambda_k >= 0; the W^k = v_k.W are independent standard Brownian motions and, by integration by parts,

    Z^k_t = sqrt(2T) [ W^k_t - lambda_k int_0^t e^(-lambda_k (t-u)) W^k_u du ],   so   sup_{t<=theta} |Z^k_t| <= 2 sqrt(2T) sup_{u<=theta} |W^k_u|.

Since |Z| <= sqrt12 max_k |Z^k|, the tube can fail only if some sup |W^k| exceeds a = delta_eps/(4 sqrt(6T)), with a^2 = eps^(-4)/18432. The reflection principle and P(N(0,1) >= x) <= e^(-x^2/2)/2 give P(sup_{u<=theta} |W^k_u| > a) <= 4 P(W^k_theta > a) <= 2 e^(-a^2/(2 theta)), and the union over twelve coordinates gives 24 exp(-eps^(-4)/(36864 theta)).

Departures. Let D_t count the rings tau in [1/4, t] at which the process is in the good state at tau- (seed occurred, S = M on [0,tau), X = Xtilde on [0,tau), tube held on [0,tau)) and the redraw differs from M. In the good state Lemma 2(iii) holds at X_{tau-}, and the redraw leaves M only if some receiver takes its exterior source, which by Lemma 3 has conditional probability at most sum_i beta_{i,ext} <= 4 r(theta) e^(-1/T); the uniforms of the ring are independent of F_{tau-}. Hence the F-compensator of D is at most 4 r(theta) e^(-1/T) times elapsed time on [1/4, theta]. Since the seed is F_{1/4}-measurable and the clock after 1/4 is independent of F_{1/4}, E[D_theta | F_{1/4}] <= 4 r(theta) (theta - 1/4) e^(-1/T) on the seed. The event that the tube holds and S leaves M before theta is contained in {D_theta >= 1}, because the first departure occurs from the good state; there is no ring on [0,1/4]. Markov's inequality completes the bound. QED.

## 5. Hidden information of the held seed law

**Lemma 5.** Fix a seed (sigma, M) and theta > 0, and let Qhat_theta = Law((Xtilde^M_theta, M) | B_{sigma,M}). For every law of X_0 carried by the seed ball and independent of W,

    H_opt(Qhat_theta) <= eta(theta) = 9 rho_circ^2 e^(-8 theta)/(2T) + 3 e^(-16 theta) / (4 (1 - e^(-8 theta))).

For theta >= t_eps, eta(theta) <= eta_eps = (9/2) rho_circ^2 eps^8 + 3 eps^32/(4 (1 - e^(-8))), the constant of eq:rg-formation-cycle-constants.

Proof. The seed involves only (X_0, S_0) and the clock, so under P(. | B) the Brownian motion keeps its law and is independent of X_0. Since K_M preserves the orthogonal splitting W_M + Z_M, the projections of W onto the two subspaces are independent Brownian motions, and

    ytilde_theta = e^(-K_M theta) y_0 + P_W Z_theta,     ztilde_theta = e^(-K_Z theta) z_0 + xi_theta,
    xi_theta ~ N(0, T K_Z^(-1) (I - e^(-2 K_Z theta))),

with xi_theta independent of (y_0, z_0, P_W Z_theta). Apply Lemma 1(d) with Y = ytilde_theta and V = z_0: the conditional law of ztilde_theta given (ytilde_theta, z_0) is N(e^(-K_Z theta) z_0, T K_Z^(-1)(I - e^(-2K_Z theta))). For one coordinate with rate lambda, a = e^(-2 lambda theta), and initial value z_0k,

    KL( N(e^(-lambda theta) z_0k, (T/lambda)(1-a)) || N(0, T/lambda) ) = (1/2) [ -a - log(1-a) + lambda a z_0k^2 / T ],

verified symbolically (Section 12). The rates lie in [4, 9], so lambda_k a_k <= 9 e^(-8 theta), and |z_0| < rho_circ by Lemma 2(i); the mean terms sum to at most 9 rho_circ^2 e^(-8 theta)/(2T). The series -a - log(1-a) = sum_{n>=2} a^n/n <= a^2/(2(1-a)) with a <= e^(-8 theta) gives the second term for three coordinates. For theta >= t_eps, e^(-8 theta) <= eps^16 = T^2 and 1 - e^(-8 theta) >= 1 - e^(-8). QED.

The only property of the seed used here is |F_M^T X_0| < rho_circ; the Gaussian mean m_0 and the seed probability do not enter.

## 6. The activation bound

**Theorem 1.** Let 0 < eps <= 1/100, T = eps^8, eps_L >= 0, m_0 in R^12, and theta >= 1/4 with T theta <= 1/12 and p_theta < 1/2. Then P(E_theta) >= (1 - p_theta) b(m_0) > 0 and

    H_opt(q^{E_theta}_theta) <= kappa(theta) = [eta(theta) + h_b(p_theta)] / (1 - p_theta),
    H_phys(q^{E_theta}_theta) <= kappa(theta) + log((4+5T)/(4+T)) <= kappa(theta) + T.

The activation law mu_act = C_# q^{E_theta}_theta is a normalized law carried by the two matching strata. For every theta in [t_eps, t_star] and eps_L = eps, kappa(theta) <= kappa_eps := [eta_eps + h_b(ptilde_eps)]/(1 - ptilde_eps).

The hypothesis T theta <= 1/12 is fixed by the 13/10 exterior margin of Lemma 2(iii), not by the tube: the exact threshold for that margin is T theta <= 0.08369 (stage4-evidence/fable-scratch/fable_lemma_checks_output.txt), so 1/12 is admissible with about 0.4 percent to spare, and T theta = 0.09 would fail it.

Proof. Fix a seed and write B = B_{sigma,M}, A = A^M_theta. On B intersect A the native state at theta is (Xtilde^M_theta, M), so q^{sigma,M} := Law(X_theta, S_theta | B intersect A) = Law((Xtilde_theta, M) | B intersect A). Under P(. | B) apply Lemma 1(b) and (e) to the binary variable 1_A and the random element (Xtilde_theta, M), whose law is Qhat_theta: by Lemma 5, H_opt(Qhat_theta) <= eta(theta), and by Lemma 4, P(A^c | B) <= p_theta < 1/2. Hence H_opt(q^{sigma,M}) <= kappa(theta). The prefix law is the mixture q^{E_theta}_theta = sum w_{sigma,M} q^{sigma,M} with w_{sigma,M} = P(B_{sigma,M} intersect A^M_theta)/P(E_theta), and convexity (Lemma 1(c)) gives the first bound. The physical bound follows from Lemma 6 below, because on E_theta the hidden coordinates are bounded, |z_theta| <= rho_circ + delta_eps, and all mass is on matching strata. The last statement uses eta(theta) <= eta_eps and p_theta <= ptilde_eps on that window together with monotonicity of h_b on [0,1/2]. QED.

**Lemma 6 (evaluator tilt).** For every law q on R^12 x J whose hidden coordinates on matching strata have finite second moment,

    H_phys(q) <= H_opt(q) + q(S is a matching) log((4+5T)/(4+T)).

Proof. Fix a matching M and a retained point y, write v = 1 - sigma_ev^2 = 1/2, d_y = D y and d_z = D F_M z; d_y.d_z = 0 because R_ev = 2 D^T D preserves Z_M, so d_y.d_z = (1/2) y.R_ev F_M z = 0. On the fiber the physical energy V_M + T|x|^2/2 has Hessian H_M + T I, which preserves the splitting, so the physical hidden conditional given (M, y) is Pi_{T,Z} = N(0, T (K^phys_Z)^(-1)), K^phys_Z = diag(8+T, 4+T, 4+T), and given (M, y, U) it is proportional to Pi_{T,Z}(dz) P_ev(U | y + F_M z), where P_ev(dU | x) = N(m; mbar, 1/2) N(k-m; 0, 1/2). Form the probability law

    Pbar_y(dz, dU) = Pi_{T,Z}(dz) P_ev(dU | y + F_M z) exp[ (d_y.(k-m) - |d_y|^2/2) / v ].

The multiplier depends only on (y, U) and turns N(k-m; 0, v) into N(k-m; d_y, v), so Pbar_y has total mass one and its conditional law of z given U is the physical hidden conditional. The recognition lift at fixed z has increment law N(k-m; d_y + d_z, v) and the same m-law. Computing the relative entropy of q(dz|M,y) nu*_{y+F_M z}(dU) against Pbar_y first through z and then through U, and dropping the nonnegative U-marginal term,

    H_phys contribution at (M,y) <= KL(q(dz|M,y) || Pi_{T,Z}) + E_q[ |d_z|^2/(2v) | M, y ].

Now |d_z|^2/(2v) = z^T F_M^T D^T D F_M z = z^T diag(0,2,2) z, and the precision matrices differ by K_Z/T - K^phys_Z/T = diag(0,4,4); hence nu_{T,Z}(dz) = Pi_{T,Z}(dz) e^(-|d_z|^2/(2v)) / Z_tilt with Z_tilt = (4+T)/(4+5T), the product of the two square-root determinant factors (checked symbolically). Therefore KL(q || Pi_{T,Z}) + E_q |d_z|^2/(2v) = KL(q || nu_{T,Z}) + log((4+5T)/(4+T)); all terms are finite by the moment assumption. Integrate over C_#q; off the matchings nothing is discarded. Finally log(1 + 4T/(4+T)) <= 4T/(4+T) <= T. QED.

The full-law relative entropy KL(q^{E_theta}_theta || mu_{T,p(theta)}) is not small and is not claimed. Its retained term is of order one, because in the eight slow retained directions the conditioned law is concentrated within rho_circ + delta_eps of e^(-T theta) sigma (x_circ + p_M/4), a point at distance sqrt3 from the origin, while the stationary retained law has order-one variance there. This is the expected state of an early prefix and not a parent error.

## 7. The activation time: a matching lower bound

**Proposition 2.** Let theta in [1/4, log(1/eps)] with T theta <= 1/12 and p_theta < 1/2. Then

    H_opt(q^{E_theta}_theta) >= ((4+5T)/(4T)) [ (rho_circ^2/7) exp(-2(4+5T) theta - 2 rho_circ (|m_0| + 2 + rho_circ)) - 3 rho_circ^2 p_theta^(1/2) ] - log 2.

With the sub-Gaussian part of p_theta, and theta = log(1/eps) - s with s in [0, (1/2) log(1/eps)], the bracket times (4+5T)/(4T) equals (rho_circ^2/7) e^(8s) exp(-10 T theta - 2 rho_circ (|m_0| + 2 + rho_circ)) (1 + O(T)) minus a super-polynomially small term. Hence the discarded information diverges when log(1/eps) - theta -> infinity, and at theta = (1/2) log(1/eps) + 1 the bound equals (rho_circ^2/7) e^(-8) e^(-2 rho_circ (|m_0| + 2 + rho_circ)) T^(-1/2) (1 + O(T log(1/T))) - log 2 up to the super-polynomially small tube term, which is of order T^(-1/2) as eps -> 0. The constant is small, about 4.6e-9 at m_0 = 0: at eps = 1/100 (T = 1e-16) the bound at that theta is about -0.23 and therefore vacuous, it is positive only for eps <= 0.009 and exceeds 1 only for eps <= 0.0072, whereas at theta = (1/2) log(1/eps) + 0.2, near the first qualifying completion of Lemma 2(iv), it is about 276 at eps = 1/100. The conclusion that activation near the first completion carries large discarded information therefore survives at eps = 1/100, but only for theta close to that completion.

Proof. Let z_perp = (z_2, z_3) be the two hidden coordinates with rate 4+5T. For each matching stratum and retained point apply Lemma 1(f) with f(z) = (4+5T) |z_perp|^2/(4T); under nu_{T,Z} each of z_2, z_3 is N(0, T/(4+5T)), so E e^f = (1 - 1/2)^(-1) = 2. Averaging gives H_opt(q) >= ((4+5T)/(4T)) E_q |z_perp|^2 - log 2 whenever q is carried by matching strata.

Fix a seed and use the held process under P(. | B). Since xi_theta is centered and independent of z_0, E[|z_perp,theta|^2 | B] >= e^(-2(4+5T)theta) E[|z_perp,0|^2 | B]. On the seed ball the density of N(m_0, I_12) varies by a factor at most exp(2 rho_circ (a + rho_circ)), where a = |sigma x_circ - m_0| <= |m_0| + 2, so E[|z_perp,0|^2 | B] >= exp(-2 rho_circ(a + rho_circ)) times its value for the uniform law on the ball. For the uniform law on a twelve-dimensional ball of radius rho_circ, the squared norm of a two-dimensional orthogonal projection divided by rho_circ^2 has the Beta(1,6) law, with mean 1/7 and upper tail (1-x)^6. Next, |z_theta| <= rho_circ + |xi_theta| with Cov(xi_theta) <= (T/4) I_3, so E[|z_theta|^4 | B] <= 8 rho_circ^4 + 8 (15/16) T^2 <= 9 rho_circ^4, and Cauchy-Schwarz with Lemma 4 gives E[|z_perp,theta|^2 1_{A^c} | B] <= 3 rho_circ^2 p_theta^(1/2). Therefore

    E_{q^{E_theta}_theta} |z_perp|^2 >= min over seeds of E[|z_perp,theta|^2 1_A | B]
                                     >= (rho_circ^2/7) e^(-2(4+5T)theta - 2 rho_circ (|m_0| + 2 + rho_circ)) - 3 rho_circ^2 p_theta^(1/2),

because the conditioned law is a mixture of the seed laws with weights summing to one and P(A|B) <= 1. Combine with the first paragraph. For the asymptotic statements, e^(-8 theta)/T = e^(8s) at theta = log(1/eps) - s, and p_theta^(1/2)/T is super-polynomially small for theta <= log(1/eps) by Lemma 4. QED.

Together with Theorem 1 this fixes the admissible activation range for the seeded prefix. The bound kappa(theta) tends to zero if and only if theta - log(1/eps) -> infinity and the tube failure tends to zero, that is theta = o(eps^(-4)) = o(T^(-1/2)); the actual discarded information tends to infinity when log(1/eps) - theta -> infinity. In the window theta = log(1/eps) + O(1) both bounds are of order one (the upper bound is at most (9/2) rho_circ^2 e^(-8(theta - log(1/eps))) + o(1)), and this derivation does not decide whether the actual value tends to zero there. The upper limit o(eps^(-4)) is intrinsic to this event: beyond it the delta_eps-tube fails with probability tending to one in the eight slow directions, and E_theta ceases to be a high-probability refinement of the seed. The delta_eps-tube is needed only for the eps^4 contrast clause on [(1/2)log(1/eps), (1/2)log(1/eps)+1]; departure suppression needs only the margins of Lemma 2(iii), so a prefix with an order-one tube after that interval extends the range toward c/T, which is not pursued here.

The source window [t_eps, t_star] = [(1/4) log(1/T), (1/4) log(1/T) + 1] lies well inside the admissible range, since t_eps - log(1/eps) = log(1/eps). Activation at a deterministic time in [(1/2) log(1/eps) + 1, log(1/eps) - s], after the first qualifying completion but before hidden thermalization, fails asymptotically, in the sense that the lower bound diverges as eps -> 0 with s -> infinity; at eps = 1/100 the lower bound is vacuous on this whole interval, since it decreases in theta and is already negative at the left end. Activation at the random first qualifying completion time is not treated here.

## 8. Future marginals under the fixed prefix

For t >= theta, E_theta intersect A^M_t = B intersect A^M_t on each seed because A^M_t is contained in A^M_theta. Hence the moving-prefix statement, H_opt(q^{E_t}_t) <= kappa(t), is Theorem 1 at time t. The fixed-prefix law q^{E_theta}_t additionally contains the histories G_t = E_theta minus E_t that fail after activation, and their conditional hidden information needs an a priori estimate.

Let F^b_t be generated by (X_0, S_0), W and the clock on [0,t], and the source choices at rings in [0,t]; the configuration-assignment path on [0,t] is a fixed measurable function of these data. Let Q be the law of the same data for the frozen-row kinetics with rows 1/2 started from mu_{T,1/2}; under Q the time-t law is mu_{T,1/2} by invariance.

**Lemma 7.** For every G in F^b_t with P(G) > 0, writing q^G_t = Law(X_t, S_t | G),

    P(G) H_opt(q^G_t) <= P(G) log(1/P(G)) + P(G)^(1/2) Lambda_t,
    Lambda_t = 17 (|m_0|^2 + 14) / (2T) + 4 (log 2 + eps_L t) (t + t^2)^(1/2).

Proof. Under both P and Q, W and the clock have the same laws and are independent of the initial data, and each source choice at a ring is a conditionally independent Bernoulli variable given everything before it, with probability beta(X_{tau-}; pi(tau)) under P and beta(X_{tau-}; 1/2) under Q. Hence on F^b_t

    L_t = log dP/dQ = log (dP_0/dQ_0)(X_0, S_0) + sum over rings tau <= t and receivers i of log [ P-probability / Q-probability of the realized choice ].

By Lemma 1(a) with lambda = C_# mu_{T,1/2}, whose hidden kernel is kappa, H_opt(q^G_t) <= KL(q^G_t || mu_{T,1/2}). Data processing through the common path map gives KL(q^G_t || mu_{T,1/2}) <= KL(P(. | G) || Q) = log(1/P(G)) + E_P[1_G L_t]/P(G). Now dP_0/dQ_0(x,S) = (2 pi)^(-6) e^(-|x-m_0|^2/2) e^(U_S(x)/T) Z_Q with Z_Q = (1/16) sum_S int e^(-U_S/T) dx <= (2 pi)^6, because U_S >= T|x|^2/2; so its logarithm is at most U_S(x)/T <= (16+5T)|x|^2/(2T) <= 17|x|^2/(2T). Each choice ratio is at most r(t) < 2e^(eps_L t) by Lemma 3. Thus L_t^+ <= 17|X_0|^2/(2T) + 4 N_t (log 2 + eps_L t), with N_t the number of rings. With E|X_0|^4 = (|m_0|^2 + 12)^2 + 24 + 4|m_0|^2 <= (|m_0|^2 + 14)^2 and E N_t^2 = t + t^2, Minkowski's inequality gives ||L_t^+||_2 <= Lambda_t, and Cauchy-Schwarz gives E[1_G L_t] <= P(G)^(1/2) Lambda_t. QED.

**Proposition 3.** Let theta <= t with T t <= 1/12 and p_t < 1/2. Then

    H_opt(q^{E_theta}_t) <= kappa(t) + [ p_t log(1/(p_t b(m_0))) + p_t^(1/2) b(m_0)^(-1/2) Lambda_t ] / (1 - p_theta),

and H_phys(q^{E_theta}_t) is at most the same quantity plus T. For each fixed m_0 and eps_L <= 1 (the original eps_L = eps included), the bracket tends to zero as eps -> 0, uniformly for theta <= t <= eps^(-4)/(663552 log(1/eps)), and it is super-polynomially small in T uniformly for theta <= t <= eps^(-4)/log^2(1/eps). These limits hold at each fixed m_0 and are not uniform in m_0, because the bracket carries the factors b(m_0)^(-1/2) and log(1/b(m_0)).

Proof. Decompose E_theta = E_t union G_t disjointly. Convexity (Lemma 1(c)) gives H_opt(q^{E_theta}_t) <= [P(E_t) H_opt(q^{E_t}_t) + P(G_t) H_opt(q^{G_t}_t)] / P(E_theta). The first part is at most kappa(t) by Theorem 1 at time t. For the second, G_t is in F^b_t, and Lemma 7 applies. By Lemma 4, P(G_t) <= p_t b(m_0), while P(E_theta) >= (1 - p_theta) b(m_0); the function x log(1/x) increases on (0, 1/e] and p_t b(m_0) <= 1/8. The physical statement follows from Lemma 6; the native second moments are finite and conditioning multiplies them by at most 1/P(E_theta). For the rate statement, Lemma 4 gives tau_t^(1/2) <= 5 exp(-eps^(-4)/(73728 t)), and the departure part of p_t is at most 8 t e^(eps_L t - 1/T), negligible for eps_L <= 1 and t <= eps^(-4). For t >= 1, Lambda_t <= 17(|m_0|^2 + 14)/(2T) + 8 (log 2 + t) t, which is O(eps^(-8)) on the first range. On that range the exponent eps^(-4)/(73728 t) is at least 9 log(1/eps), so p_t^(1/2) Lambda_t = O(eps); on the second range the exponent is at least log^2(1/eps)/73728, which beats every power of eps. The term p_t log(1/(p_t b(m_0))) is smaller still. QED.

The Chebyshev tube does not suffice for Proposition 3: with p_t of order T^(1/2) t, the term p_t^(1/2) Lambda_t is of order T^(-3/4), which diverges. The sub-Gaussian estimate of Lemma 4 is what closes the fixed-prefix statement.

The range in Proposition 3 is asymptotic and is numerically much smaller at the boundary regime. At eps = 1/100 and m_0 = 0, evaluated with b(m_0) replaced by its floor 2c(m_0), about 2.8e-31 (which can only enlarge the bracket), the factor (2c(0))^(-1/2) is about 1.9e15; the bracket is about 2.2e-24 on the source window [t_eps, t_star], falls below 1 only for t <= 17.3, and at the first-range endpoint t = eps^(-4)/(663552 log(1/eps)), about 32.7, it is about 1.1e16 (stage4-evidence/fable-scratch/fable_lemma_checks_output.txt). Since b(0) is roughly twice its floor, these figures are conservative, but not by enough to change their orders. At eps = 1/100 the proposition therefore certifies the fixed-prefix future on the source window and for t up to about 17, and only asymptotically beyond.

## 9. A path-observable prefix

The clock clause of B_{sigma,M} is not a function of the configuration-assignment path, because self-proposals are invisible. The following prefix is path-measurable and contains E_theta:

    E^pi_theta = disjoint union over (sigma,M) of { |X_0 - sigma x_circ| < rho_circ, S_u = M for u in [0,theta], sup_{u<=theta} |X_u - e^(-K_M u) X_0| <= delta_eps }.

On {S = M on [0,u]} one has X_u - e^(-K_M u) X_0 = Z^M_u, so each piece is the intersection of the seed B^pi = {ball, S = M on [0,1/4], tube on [0,1/4]} in F_{1/4} with the remainder A^pi = {S = M on (1/4, theta], tube on [0,theta]}.

**Proposition 4.** Under the hypotheses of Theorem 1 with theta > 1/4 and

    p^pi_theta = e^(1/4) tau_theta / (1 - tau_theta) + 4 r(theta) theta e^(-1/T) < 1/2,
    eta^pi(theta) = 9 (rho_circ + delta_eps)^2 e^(-8(theta - 1/4)) / (2T) + 3 e^(-16(theta-1/4)) / (4 (1 - e^(-8(theta-1/4)))),

one has H_opt(Law(X_theta, S_theta | E^pi_theta)) <= [eta^pi(theta) + h_b(p^pi_theta)] / (1 - p^pi_theta), and the physical bound adds at most T.

Proof. On B^pi the process is held on [0,1/4], so z_{1/4} = e^(-K_Z/4) F_M^T X_0 + F_M^T Z_{1/4} has norm at most rho_circ + delta_eps. The held continuation from 1/4 is e^(-K_M(u-1/4)) X_{1/4} plus noise increments after 1/4, which are independent of F_{1/4}; Lemma 5, started at 1/4 with this bound on z_{1/4}, gives eta^pi(theta), and on B^pi intersect A^pi the native process equals this continuation. For the remainder, P(B^pi) >= P(ball, S_0 = M) e^(-1/4) (1 - tau_theta), since the clock-based seed intersected with the tube on [0,1/4] lies in B^pi; the tube failure satisfies P(B^pi and failure on [0,theta]) <= P(ball, S_0 = M) tau_theta, because W is independent of (X_0, S_0); and departures in (1/4, theta] contribute at most 4 r(theta) theta e^(-1/T) by the compensator argument of Lemma 4 applied after the F_{1/4}-measurable seed. On the tube the total noise has norm at most delta_eps, so Lemma 2 applies unchanged. Lemma 1(e) and convexity finish the proof. QED.

The price of path observability is the factor e^2 (1 + delta_eps/rho_circ)^2 in the memory term and e^(1/4)/(1 - tau_theta) in the tube term.

**Generalized seeds.** Beyond S_0 = M and the silent clock on [0,1/4], Lemmas 4 and 5 use only two properties of a seed: every held path from it that stays in the tube keeps the exterior-minus-partner cost gap above one on [1/4, theta], and the hidden component satisfies |F_M^T X_0| <= R. For any Borel set of initial configurations with these properties, the proof of Theorem 1 gives the same bound with rho_circ replaced by R in eta. This indicates how a larger part of the contrast event could be covered; it does not cover histories in which M is first entered at a random positive time.

## 10. Mobility, orders, and numbers

Rows enter at exactly two places: the departure probability in Lemma 4, through r(theta) = 2 e^(eps_L theta) - 1, and the choice likelihood ratio in Lemma 7, through log 2 + eps_L t. The drift, the clock, the initial law, the held-law bound, the reference kernels, and both hidden conditionals are row-free. At the original mobility eps_L = eps = T^(1/8) and theta <= t_star, r(theta) <= 1.215. For any eps_L with eps_L theta <= 1/(2T), the departure term is at most 8 theta e^(-1/(2T)). Theorem 1 therefore holds at eps_L = T^(1/8) and at every mobility up to eps_L = 1/(2 T theta); Proposition 3, as stated, uses eps_L <= 1, which includes the original mobility. Slow schedules such as eps_L = o(T^(1/4)) or eps_L <= T^2 are not required for obligation 1.

Asymptotic orders in T, with eps = T^(1/8):

    general theta:      kappa(theta) = [ (9/2) rho_circ^2 e^(-8(theta - log(1/eps))) + O(e^(-16 theta)) + h_b(p_theta) ] (1 + O(p_theta)),
    theta in [t_eps, t_star], Chebyshev tube:
                        p = 73728 T^(1/2) theta + O(theta e^(-1/T)) = O(T^(1/2) log(1/T)),
                        kappa = O(T^(1/2) log^2(1/T)),
    theta = t_eps, sub-Gaussian tube:
                        tau <= 24 exp(-T^(-1/2) / (9216 log(1/T))),
                        kappa = (9/2) rho_circ^2 T + O(T^4) + O(X e^(-X)) + O(e^(-1/(2T))),   X = T^(-1/2)/(9216 log(1/T)),
                        H_phys <= kappa + T = O(T).

The corresponding scaled optimizer free-energy loss is at most T kappa, and the unscaled physical negative-ELBO loss at most kappa + T, as in ca_parent_conditional.tex.

Values at eps = 1/100 (T = 1e-16, t_eps = 9.2103, t_star = 10.2103, eps_L = eps), computed by the scratch script of Section 12:

| quantity | theta = t_eps | theta = t_star |
| --- | --- | --- |
| eta(theta) | 4.50e-20 | 1.51e-23 |
| p_theta, Chebyshev tube | 6.79e-3 | 7.53e-3 |
| kappa(theta), Chebyshev tube | 4.09e-2 | 4.46e-2 |
| log tau_theta, sub-Gaussian tube | -291.3 | -262.5 |
| kappa(theta), sub-Gaussian tube | 4.50e-20 | 1.51e-23 |

With the source's Chebyshev tube the bound at eps = 1/100 is about 0.04, dominated by h_b(p); the sub-Gaussian tube removes that term, leaving the physical bound dominated by the evaluator term T.

## 11. Why rem:phil-conditioned-hidden-sign does not obstruct the bound

The remark conditions the stationary matching Gaussian on {z_1 > 0}, an event of probability 1/2 that is a function of the hidden coordinate at the evaluation time, and obtains discarded information log 2. The general principle is Lemma 1(b): conditioning on an event of probability 1 - r costs at most h_b(r)/(1-r) plus the prior information, so an event whose probability is only bounded below, such as the seed or the whole contrast event, gives an order-one bound and nothing better.

The prefix E_theta is conditioned at two different times with two different mechanisms. The seed B_{sigma,M}, whose probability is only bounded below (and numerically tiny, of order 1e-31 at m_0 = 0), is a function of the time-zero data and the clock on [0,1/4]. The argument never pays log(1/P(B)). It computes the B-conditioned held law exactly: the seed constrains the hidden state only through |z_0| < rho_circ, and the held flow contracts that imprint by e^(-K_Z theta), leaving eta(theta), which is small once e^(-8 theta)/T is small. The part of the prefix that is correlated with the hidden path up to activation, the remainder A_theta (tube and no departures), has conditional probability at least 1 - p_theta given the seed, so event information charges it only h_b(p_theta)/(1-p_theta). The remark's phenomenon reappears exactly when the imprint has not been dissipated: Proposition 2 shows divergence for theta <= log(1/eps) - s, which is a stronger form of the remark (order e^(8s) instead of log 2), since the seed constrains the hidden coordinates to a ball of radius rho_circ, far outside the thermal scale sqrt T.

For the future marginals the same structure persists under the fixed prefix (Proposition 3). On the range of that proposition, histories that fail after activation have probability small enough that p_t^(1/2)/T tends to zero, and Lemma 7 bounds their hidden information by log(1/P(G)) and a likelihood-ratio moment of order 1/T, so their contribution vanishes. The remark would obstruct only a statement that conditioned on a future event correlated with the hidden state at the evaluation time, which no statement here does.

## 12. Relation to the working hypotheses and checks

H-a is confirmed with four refinements. The bound holds for every deterministic theta with theta - log(1/eps) -> infinity and theta = o(eps^(-4)), not only on [t_eps, t_star]. The rows enter only through r(theta) <= 1.215 at the original data, and the union over seeds uses convexity alone, with no symmetry transfer. The sub-Gaussian tube improves the order from O(T^(1/2) log^2(1/T)) to O(T). The fixed-prefix future marginals need Lemma 7 and the sub-Gaussian tube.

H-b is confirmed for deterministic activation times by Proposition 2, including the order T^(-1/2) near (1/2) log(1/eps) + 1 as eps -> 0 (with the small constant recorded in Section 7, so that at eps = 1/100 the bound is informative only for theta close to the first qualifying completion) and the threshold log(1/eps) + O(1). This derivation does not treat the random first qualifying completion time or conditioning on the whole contrast event; the mixture transfer proposed in H-b is the lower half of Lemma 1(b), H(q) >= w H(q_seed) - h_b(w), which is valid but carries the seeded weight w.

H-c (path coupling) is outside this obligation. Section 6 records one fact relevant to it: the retained activation law is concentrated at scale rho_circ around a point at distance sqrt3 from the origin in the slow retained directions, so its total-variation distance from the stationary retained Gaussian is close to one, and item 3's stationary coupling cannot be reused unchanged.

Scratch checks were run with C:/Python314/python.exe (numpy 2.4.4, scipy 1.17.1, sympy 1.14.0; no GPU involved). Script and output: C:\Users\chris and christine\Desktop\MultiAgentELBO\docs\derivations\2026-09-26-selection-to-formation\stage4-evidence\author-scratch\stage4_seeded_checks.py and stage4_seeded_checks_output.txt. The verifier's rerun of that script (fable_rerun_stage4_seeded_checks_output.txt, identical printed values) and its independent checks (fable_hidden_info_check.py, fable_lemma_checks.py, and their outputs) are in stage4-evidence\fable-scratch\ in the same folder. The author script verifies in exact rational arithmetic that F_M^T(+-x_circ) = 0 for both matchings and that every residual of x_circ is -1; numerically that ||R_ev|| = 4, that the largest eigenvalue of H_S over all sixteen assignments is 8.83 (below the bound 16 used), and formula (1.3) for all residuals, signs, and matchings to 1.6e-15; symbolically the per-coordinate Gaussian relative entropy, Z_tilt = (4+T)/(4+5T), and the moment generating value used in Proposition 2; the constants 73728 and 36864; the margins 0.1527, 1.30048, 0.98, and 0.4828 of Lemma 2; the row ratio 1.2150; the table of Section 10; and, by Monte Carlo with 400000 samples, the Beta(1,6) tail and mean (0.1774 against 0.1780, and 0.1428 against 1/7). These are consistency checks of constants, not substitutes for the proofs.

## 13. Scope

Theorem 1 and Propositions 3 and 4 bound the discarded conditional information of the actual learned recognition law conditioned on the seeded sub-event of the original first-contrast event, at deterministic activation times theta with log(1/eps) + omega(1) <= theta <= o(eps^(-4)), for every Gaussian mean, at the original coupled mobility (Theorem 1 at every mobility with eps_L theta <= 1/(2T), Proposition 3 for eps_L <= 1). They do not bound the full-law relative entropy, which is of order one because the retained state of an early prefix is far from equilibrium. The seeded sub-event has probability at least c(m_0) in every arm, uniformly in eps, but it is not the whole contrast event E_T. Its probability is of order 1e-31 at m_0 = 0, nothing here bounds P(E_T) from above, and the hidden information of non-seeded contrast histories is not controlled here, so no bound for the conditional law given E_T follows. By SPEC R15 the sub-event is a coherence episode with a restoring clause and a margin over its stationary probability (prop:phil-seeded-contrast-formation(b)), but the bound says nothing about which block the law selects, and so nothing under R13 about learning-driven selection. Parent path coupling (obligation 2) and the parent's own rows are not treated.

The minimal unresolved obligation for this line is a hidden-information bound for the conditional law given the whole contrast event E_T, or given the first-block mark, at a deterministic activation time: histories that enter the matching at a random positive time, or start outside the seed balls, need a strong-Markov restart at the entry time together with a held-law memory estimate there. The generalized-seed remark of Section 9 supplies the second ingredient for time-zero entries; the next action is to prove the restart version for entry at a stopping time and to bound the non-seeded weight of E_T from above.
