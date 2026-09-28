# Stage 4, obligation 1: activation time and discarded information on the first contrast

Date: 2026-09-28. Author model: Claude Opus 5.5 (`claude-opus-5-5`). Verifier: Claude Fable 5.1 (`claude-fable-5-1`), cross-model, verdict VALID_WITH_MINOR_ISSUES with no critical or major defect; the report is [stage4-crossmodel-activation-time.md](stage4-crossmodel-activation-time.md). The minor and exposition fixes that report lists were applied afterwards by Claude Opus 5.5 and have not been re-verified. Scope: fixed base point c_*, no base transport, no Lean. The Research vault was read and not edited. The companion note [stage4-exact-checks.md](stage4-exact-checks.md), written in this round by another worker on the same author model, contains exact symbolic checks of the matching-sheet geometry used in Section 2; it is supporting computation, not verification.

## Verdict

The discarded optimizing conditional relative entropy of the type-(b) parent on the original early first contrast is controlled by the activation clock, and the source-learning mobility plays no role. Four statements are proved below for eps in (0,1/100], T=eps^8, and every mobility eps_L in [0,1/t*], which contains the original coupled mobility eps_L=eps=T^(1/8), every slow schedule, and the frozen arm.

First, on the seeded event the first qualifying completion time tau of the first-block mark satisfies, up to additive constants in [-0.07,0.15],

    tau - 1 = max{ L/4 , (1/4) log(v_min/eps^2) },    L = log(1/eps),

where v_min is the smaller of the two initial hidden belief-model discrepancies. The binding internal component is the hidden belief-model discrepancy n^- of the first pair to form (rate 4+5T) whenever v_min >= eps, which has seed probability tending to one; the common internal residual, dominated by the retained fast normal (rate 8+T), binds only when v_min < eps. In all cases tau <= L/2 + 0.03.

Second, the parent activated at tau diverges. On the seeded prefix the discarded conditional relative entropy is at least 1.44e-7 exp(-2 rho dbar) T^(-5/8)(1+o(1)), and at the explicit value eps=1/100 it is at least 1103 when m_0 = x_circ. The rate T^(-5/8) is larger than the T^(-1/2) of hypothesis H-b. It comes from seeds in which one pair forms early while the other pair's discrepancy, which the matching channel also discards, is still of order rho eps. Conditioning on the whole first-block event E_T keeps the divergence through the mixture bound, with a weight at least (1-p_hat) c(m_0), so it appears only below an m_0-dependent and very small eps.

Third, at a deterministic activation time t on the seeded prefix, the discarded conditional relative entropy equals Q(t)/2 to leading order, with Q(t) comparable to (4 rho^2/(7T)) e^{-8t}. It diverges when t - L tends to minus infinity, vanishes when t - L tends to plus infinity, and stays bounded when t - L is bounded. The threshold is t = log(1/eps) + O(1) = (1/8) log(1/T) + O(1), and hypothesis H-a's bound at t in [t_eps, t*] is confirmed.

Fourth, delaying activation after completion by h has a threshold at h = (5/8) log(1/eps) + O(1) on the seeded prefix. The error vanishes when h - (5/8)L tends to plus infinity and diverges when it tends to minus infinity. These are two one-directional implications, not an equivalence: on the window h - (5/8)L in [-2.06, O(1)] the error is bounded above but its positivity is not proved. Immediately after completion, at h=1, the divergence rate as eps -> 0 is T^(-5/8) from both sides.

The mixture inequality used to pass to E_T is exact: H(q) = sum_b w_b H(q_b) - I(B;Z|R), which lies between sum_b w_b H(q_b) - H(B) and sum_b w_b H(q_b). What remains open is an upper bound under conditioning on the whole contrast event E_T at a delayed activation time. It requires control of contrast histories that do not pass through a seed ball, and neither the seed argument nor event information alone supplies that control.

## 1. Target, quantifiers, and assumptions

**Model (supplied).** This is the homogeneous four-cycle of def:rg-formation-cycle-experiment. Its configurations are x=(kbar,mbar,omega) in R^12 and its assignments are S in J, a set of sixteen. The drift on sheet S is -K_S x with K_S=H_S+T(I+R_ev), the noise is sqrt(2T) dW, and one rate-one clock redraws the whole assignment from the product of posterior receiver rows. The generative prior is a product of receiver rows pi(t) that start uniform and learn by pi_ij' = eps_L (q_t(S_i=j) - pi_ij). The initial law is N(m_0,I_12) times uniform assignments, with m_0 fixed and arbitrary. Constants: eps in (0,1/100], T=eps^8, L=log(1/eps), t_eps=2L, t*=t_eps+1, rho=rho_circ=1/100, x_circ=(0,0,1_4), and delta_eps=eps^2/(8 sqrt3). The original coupled regime of prop:phil-seeded-contrast-formation is eps_L=eps. The slow schedules are eps_L=o(T^(1/4)), including eps_L <= T^2.

**Contrast event and mark (supplied).** Following prop:phil-early-block-null with its regime parameter equal to T^(1/8)=eps, an eligible proper connected block (the four pairs and four triples) has an internal belief relative entropy above 1/4 at time zero. It qualifies at completion time t in [1, H_T], H_T=2/eps, when on [t-1,t] all its internal belief and model relative entropies are at most sqrt T = eps^4 and all its boundary belief relative entropies exceed 1/2. K_T is the block with least infimum of qualifying completion times, ties broken by one fixed rule. tau is that infimum, with tau=+infinity off E_T={K_T is not the cemetery}. With sigma_ev^2=1/2, the belief relative entropy of residual r^b is (r^b)^2/2 and the model relative entropy is (r^m)^2, so the internal clause reads |r^b| <= sqrt2 eps^2 and |r^m| <= eps^2 on each internal edge.

**Parent and discarded information (supplied).** C(x,S)=(S,P_{W_S}x) is the channel of prop:rg-formation-endogenous-cycle(b): W_M=Z_M^perp on the two matchings and W_S=R^12 elsewhere. For a law q of (X,S), H(q)=H_opt(q) is the mean over C_#q of KL(q(dz|S,y) || kappa), where on a matching stratum z in Z_M are the hidden coordinates and kappa=N(0,T K_Z^{-1}) with K_Z=diag(8+T,4+5T,4+5T). Off the matchings the contribution is zero. H_phys is the analogous quantity against the physical posterior with evaluator samples retained, as in prop:phil-actual-conditioned-parent.

**Seeds and prefix events (supplied, with one introduced variant).** For sigma in {1,-1} and a matching M, B_{sigma,M} is the event that |X_0 - sigma x_circ| < rho, S_0=M, and no clock ring occurs on [0,1/4]. A_t is the prefix event of the source proof: the held-sheet noise stays within delta_eps on [0,t], and every proposal in [1/4,t] returns M. The notation fixes sigma=1 and M=S^(0), with selected edges e=e_0 and f=e_2. The other three seeds follow by the cycle automorphisms exactly as in the source proof, with sigma x_circ in place of x_circ. The introduced variant uses the stopped time

    t_1 = L/2 - (1/4) log 50,   tau_hat = min(tau, t_1 + 1),   G_h = B ∩ A_{tau_hat + h}  (h >= 0),

and D=G_0 is called the seeded prefix at completion. G_h is measurable at the optional time tau_hat+h. For h <= (3/2)L we have tau_hat+h <= t*, so A_{t*} ⊂ A_{tau_hat+h}.

**Introduced notation.** v = X_0 - x_circ is the seed offset. Its coordinates are v_+ along the common fast normal and v_1, v_2, v_3 along the hidden basis of Section 2, with v_min = min(|v_2|,|v_3|). We write lambda_1 = 8+T and lambda_2 = 4+5T, dbar = max(|x_circ - m_0|, rho), and

    p_hat = 73728 eps^4 t* + 18 t* e^{-1/T}    (p_hat < 0.0076 for eps <= 1/100, and p_hat -> 0),
    Phi(m) = (m-3)/2 - (3/2) log(m/3) for m >= 3,   Phi(m) = 0 for m < 3.

**Target.** (i) Two-sided bounds on tau on the seeded prefix, with the binding component identified. (ii) Lower bounds on H(Law(X_tau,S_tau | D)) and H(Law(X_tau,S_tau | E_T)) that diverge as eps -> 0 for each fixed m_0, with constants and rate. (iii) Two-sided bounds at deterministic activation times on the seeded prefix, with the threshold. (iv) The mixture inequality. (v) The consequences for activation conventions. (vi) Corrections to hypothesis H-b. The assignment adds the delayed clock tau + h to (v), and it is treated as a separate proposition.

## 2. Sheet coordinates and the held process

**Lemma 2.1 (sheet coordinates).** Let n^+_g = (a^b_g + a^m_g)/(2 sqrt2) and n^-_g = (a^b_g - a^m_g)/2 for g in {e,f}. The coordinates are

    z_+ = ((n^+_e + n^+_f)/sqrt2) . x,   z_1 = ((n^+_e - n^+_f)/sqrt2) . x,   z_2 = n^-_e . x,   z_3 = n^-_f . x.

Then (z_1,z_2,z_3) are the hidden coordinates of Z_{S^(0)}, and z_+ is a retained coordinate of W_{S^(0)}. The selected residuals are

    r^b_e = z_+ + z_1 + z_2,   r^m_e = z_+ + z_1 - z_2,   r^b_f = z_+ - z_1 + z_3,   r^m_f = z_+ - z_1 - z_3.

K_{S^(0)} has the eigenvector of z_+ with eigenvalue lambda_1, is diag(lambda_1, lambda_2, lambda_2) on Z, and preserves W. At the seed center, z(x_circ) = 0 and z_+(x_circ) = -1.

*Proof.* The residual identities follow from a^b_g = sqrt2 n^+_g + n^-_g, a^m_g = sqrt2 n^+_g - n^-_g, and n^+_{e,f} . x = (z_+ ± z_1)/sqrt2. The eigenstructure is the computation in the proof of prop:rg-formation-endogenous-cycle (H_M n^+ = 8 n^+, H_M n^- = 4 n^-, R_ev n^+ = 0, R_ev n^- = 4 n^-), and the value at x_circ is the center path at t=0. These identities are checked exactly in stage4-exact-checks.md, Task 1, and numerically to 1e-15 in the check of Section 11. ∎

Consequently the internal clause of block {0,1} at time s implies

    |z_2(s)| <= kappa_0 eps^2,   |z_+(s) + z_1(s)| <= kappa_0 eps^2,   kappa_0 = (1+sqrt2)/2 < 1.2072,

because z_2 = (r^b - r^m)/2 and z_+ + z_1 = (r^b + r^m)/2. Conversely, the clause holds whenever |z_+ + z_1| + |z_2| <= eps^2. The same holds for block {2,3} with z_3 and z_+ - z_1.

**Lemma 2.2 (held process and noise).** On B, let the held process be X~_t = e^{-K t} X_0 + Z_t with Z_t = sqrt(2T) ∫_0^t e^{-K(t-s)} dW_s. In the coordinates of Lemma 2.1,

    z_+(t) = e^{-lambda_1 t}(-1 + v_+) + xi_+(t),   z_1(t) = e^{-lambda_1 t} v_1 + xi_1(t),   z_k(t) = e^{-lambda_2 t} v_k + xi_k(t)  (k=2,3),

where the xi are independent scalar Ornstein-Uhlenbeck processes started at zero. They are independent of X_0, of the clock, and of the proposal uniforms, and they are independent of the retained noise. The following hold. (a) |xi_k(t)| <= |Z_t| <= delta_eps on the tube of A_t. (b) E xi_k(t)^2 = (T/lambda_k)(1 - e^{-2 lambda_k t}). (c) For every stopping time sigma <= t_max, E xi_k(sigma)^2 <= 2T E sigma. (d) For every stopping time sigma and deterministic h >= 0, xi_k(sigma+h) = e^{-lambda_k h} xi_k(sigma) + xi'_k with xi'_k independent of F_sigma, mean zero, and variance at most T/lambda_k. On B ∩ A_s the native process equals the held process on [0,s], and S ≡ S^(0) there.

*Proof.* K preserves the orthonormal decomposition, so the eigencoordinates decouple, and orthonormal components of a standard Brownian motion are independent. Item (a) holds because the coordinates are orthonormal components of Z_t. For (c), Ito's formula gives d(xi^2) = (2T - 2 lambda xi^2) dt + 2 sqrt(2T) xi dW. The stochastic integral stopped at a bounded stopping time has mean zero because E ∫_0^{t_max} xi^2 dt < infinity, so E xi(sigma)^2 = 2T E sigma - 2 lambda E ∫_0^sigma xi^2 <= 2T E sigma. Item (d) is the strong Markov property of W. The coincidence of the native and held processes is the construction of A_s in the proof of prop:rg-formation-endogenous-cycle(a), whose argument prop:phil-seeded-contrast-formation extends to learned rows. ∎

The optional-stopping bound (c) is the fine noise estimate. The Chebyshev tube delta_eps ~ eps^2 is used only to locate tau. The hidden noise enters the entropy bounds only through (b) to (d), at the thermal scale T.

**Lemma 2.3 (prefix failure at any mobility).** For eps_L in [0,1/t*], P(A_{t*}^c | B) <= p_hat, and hence P(G_h^c | B) <= p_hat for h <= (3/2)L.

*Proof.* By the row bound of prop:phil-seeded-contrast-formation(a), whose proof uses only 0 <= q <= 1 and so holds at any mobility, |pi_ij(t) - 1/2| <= (1 - e^{-eps_L t})/2. Every row entry on [0,t*] therefore lies in [e^{-1}/2, 1 - e^{-1}/2], and the ratio of the two entries of a row is at most 2e - 1 < 4.44. The episode paragraph of the source proof then applies line by line with the factor 1.23 replaced by 4.44: a proposal departs with probability at most 4(4.44) e^{-1/T} < 18 e^{-1/T}, and the tube fails with probability at most 73728 eps^4 t*. ∎

## 3. Entropy tools

**Lemma 3.1 (Donsker-Varadhan with a quadratic test).** For any law q of (X,S), put

    m(q) = E_q[ 1{S is a matching} Z^T K_Z Z ] / T.

Then H(q) >= Phi(m(q)).

*Proof.* The Donsker-Varadhan inequality KL(P||R) >= E_P f - log E_R e^f holds for nonnegative measurable f with E_R e^f < infinity, by monotone truncation of the bounded case. Take f = lambda z^T K_Z z / T with lambda in (0,1/2). Under kappa, z^T K_Z z / T is chi-square with three degrees of freedom, so log E_kappa e^f = (3/2) log(1/(1-2 lambda)) at every retained value. Apply the inequality fiberwise on the matching strata, average over C_#q, and use that the matching strata have total mass at most one: H(q) >= lambda m(q) - (3/2) log(1/(1-2 lambda)). The supremum over lambda is attained at 1 - 2 lambda = 3/m and equals Phi(m) for m >= 3. ∎

Phi is nondecreasing, and Phi(m) = m/2 - O(log m).

**Lemma 3.2 (mixture identity, item iv).** Let q be the law of R = (X_theta, S_theta) at any random time theta, let B be an event with P(B) = w in (0,1), and let q^B, q^{B^c} be the conditional laws. Then, in [0, infinity],

    w H(q^B) + (1-w) H(q^{B^c}) = H(q) + I(1_B ; Z | S, Y) ,   0 <= I(1_B; Z | S, Y) <= h_b(w) <= log 2,

so

    w H(q^B) + (1-w) H(q^{B^c}) - h_b(w)  <=  H(q)  <=  w H(q^B) + (1-w) H(q^{B^c}).

The same identity with h_b(w) replaced by the Shannon entropy of the label holds for any finite partition. The same identity holds for H_phys with retained variables (S, Y, U), because the evaluator lift of a mixture is the mixture of the lifts.

*Proof.* Let beta = 1_B and let P be the joint law of (beta, S, Y, Z) on the matching strata. Compute KL(P || P_{beta,S,Y} ⊗ kappa) in two ways. Disintegrating in (beta, S, Y) gives sum_b P(beta=b) H(q^{beta=b}), because P(dz | beta=b, S, Y) is the hidden conditional of q^{beta=b}. The chain rule in the order (S, Y, Z) then beta gives KL(P_{S,Y,Z} || P_{S,Y} ⊗ kappa) + E KL(P_{beta|S,Y,Z} || P_{beta|S,Y}) = H(q) + I(beta; Z | S, Y). All terms are nonnegative, so the identity holds in [0, infinity]. Finally I(beta; Z | S, Y) <= H(beta | S, Y) <= H(beta) = h_b(w). ∎

The orchestrator's inequality H(q) >= sum w_b H(q_b) - log 2 is therefore correct for a binary split, and the upper inequality is convexity. A second route avoids the log 2: since m is linear and nonnegative, m(q) >= w m(q^B), and Lemma 3.1 gives H(q) >= Phi(w m(q^B)).

**Lemma 3.3 (physical reference).** For every law q,

    H(q) - 3.5 E_q[ 1{S matching} |Z|^2 ] - T  <=  H_phys(q)  <=  H(q) + T.

*Proof.* The upper inequality is eq:phil-conditioned-physical-entropy. For the lower one, fix a matching fiber and retained y. Compute the relative entropy of the lifted recognition law against the tilted comparison law Pbar_y of eq:phil-conditioned-evaluator-tilt by the chain rule in both orders. With the source's tilt identity, this gives the following equality. The source drops the last term, which gives its upper bound.

    H_phys(q|y) = KL(q(dz|y) || nu_T) + log((4+5T)/(4+T)) - KL(q(dU|y) || Pbar_y(dU)).

The evaluator marginals are mixtures. Under recognition, U given z is P_z = N(mbar(y+Fz), 1/2) ⊗ N(d_y + d_z, 1/2); under the comparison, U given z' is P'_{z'} = N(mbar(y+Fz'), 1/2) ⊗ N(d_y, 1/2), with z distributed as q(dz|y) and z' as Pi_{T,Z}. Joint convexity under the product coupling gives

    KL(q(dU|y) || Pbar_y(dU)) <= ∫∫ KL(P_z || P'_{z'}) q(dz|y) Pi(dz'),

where KL(P_z || P'_{z'}) = |P_m F (z - z')|^2 + |d_z|^2. The model-mean readout satisfies ||P_m F|| = sqrt3/2, and |d_z|^2 = 2(z_2^2 + z_3^2), both checked numerically in Section 11. Hence KL(P_z || P'_{z'}) <= (3/2)|z|^2 + (3/2)|z'|^2 + 2|z|^2. Also E_Pi |z'|^2 = T(1/(8+T) + 2/(4+T)) <= 5T/8, and (3/2)(5T/8) < T. Average over the retained law. ∎

So H_phys and H diverge or vanish together whenever E|Z|^2 stays bounded, which holds for every law below.

**Lemma 3.4 (seed-law moments).** On B, the offset v has a density relative to the uniform law on the ball of radius rho. That density lies in [e^{-2 rho dbar}, e^{2 rho dbar}], because the Gaussian density on the ball varies by at most the factor exp(((d+rho)^2 - (d-rho)^2)/2). Under the uniform law on the 12-ball:

    E v_k^2 = rho^2/14   (each orthonormal coordinate),
    one-coordinate density <= c_12/rho,   c_12 = Gamma(7)/(sqrt(pi) Gamma(13/2)) = 46080/(10395 pi) < 1.4111,
    P(v_min <= y) <= 4 c_12 y / rho < 5.645 y / rho,
    E[ v_3^2 1{|v_2| <= a} ] >= 0.1427 rho a   for 0 < a <= rho/4.

*Proof of the last line.* Given v_2 = rho x, the remaining eleven coordinates are uniform on an 11-ball of radius rho sqrt(1-x^2), so E[v_3^2 | x] = rho^2 (1-x^2)/13. The expectation is therefore (rho^2 c_12/13) ∫_{|x| <= a/rho} (1-x^2)^{13/2} dx >= (rho^2 c_12/13) · 2(a/rho)(15/16)^{13/2} >= 0.1427 rho a. ∎

## 4. The first qualifying completion time on the seeded prefix (item i)

**Proposition 4.1.** Let eps in (0,1/100] and eps_L in [0,1/t*], and let s_flat = L/4 + 3/20. The seeded prefix D = B ∩ A_{tau_hat} satisfies P(D | B) >= 1 - p_hat and D ⊂ E_T. On D the following hold.

(a) K_T ∈ {{0,1},{2,3}}, tau_hat = tau <= t_1 + 1 = L/2 - (1/4) log 50 + 1 < L/2 + 0.03, and S ≡ S^(0) on [0, tau].

(b) tau - 1 <= max{ L/4, (1/4) log(v_min/eps^2) } + 3/20. In particular tau - 1 <= s_flat when v_min <= eps.

(c) With k* the discrepancy index of K_T (2 for {0,1}, 3 for {2,3}),

    e^{-lambda_1 (tau-1)} <= 1.33 eps^2,     |v_{k*}| e^{-lambda_2 (tau-1)} <= 1.28 eps^2,

so tau - 1 >= L/4 - 0.04 and tau - 1 >= (1/lambda_2) log(v_min/(1.28 eps^2)).

*Proof.* On B ∩ A_s and for t <= s, Lemma 2.2 gives for block {0,1}

    |r^b_e(t)|, |r^m_e(t)|  <=  (1 + sqrt2 rho) e^{-lambda_1 t} + |v_2| e^{-lambda_2 t} + eps^2/8,

because |v_+ ± v_1| <= sqrt2 rho, and |xi_+ ± xi_1| + |xi_2| <= sqrt3 |Z_t| <= sqrt3 delta_eps = eps^2/8. The same bound holds for block {2,3} with v_3.

For (a), at t >= t_1 we have e^{-8t} <= 2500 eps^4 <= eps^2/4 and rho e^{-4t} <= eps^2/2, so the right side is at most (0.2536 + 0.5 + 0.125) eps^2 < eps^2. Thus the internal clause holds for both matched pairs on [t_1, t_1+1], whenever the tube holds there. On [1/4, s] the exterior residuals exceed 13/10 and the exterior belief relative entropies exceed 0.845 > 1/2, by the source estimate (valid pointwise on the tube). The eligibility clause at time zero holds on B. If tau > t_1 + 1 on D, then tau_hat = t_1 + 1, the tube holds up to t_1 + 1, and [t_1, t_1+1] qualifies, a contradiction. So tau <= t_1 + 1 and tau_hat = tau. A block with an exterior edge among its internal edges (the pairs {1,2}, {3,0} and all four triples) cannot qualify at a completion time t <= tau_hat, because [t-1,t] meets [1/4, tau_hat], where that edge's belief relative entropy exceeds 0.845 > eps^4. Hence K_T is a matched pair. Also D ⊂ E_T because tau <= t_1 + 1 < H_T. The probability bound is Lemma 2.3.

For (b), let k be the index with |v_k| = v_min, and take t >= s := max{L/4, (1/4) log(v_min/eps^2)} + 3/20. Then e^{-8t} <= eps^2 e^{-6/5} and |v_k| e^{-4t} <= eps^2 e^{-3/5}. When v_min < eps the maximum is L/4, and |v_k| e^{-4t} <= v_min eps e^{-3/5} < eps^2 e^{-3/5}. The right side is therefore at most (1.0142 · 0.3012 + 0.5488 + 0.125) eps^2 < 0.98 eps^2. Moreover s <= t_1, since (1/4) log(rho/eps^2) + 3/20 = L/2 - 1.001 and L/4 + 3/20 <= L/2 - 0.978 for L >= log 100. The argument of (a) then shows that the pair with discrepancy index k qualifies at s + 1.

For (c), the internal clause holds at time tau - 1 <= tau_hat, so |z_{k*}| <= kappa_0 eps^2 and |z_+ ± z_1| <= kappa_0 eps^2 there. Subtract the noise, which is at most delta_eps for z_{k*} and at most sqrt2 delta_eps for z_+ ± z_1. This gives |v_{k*}| e^{-lambda_2(tau-1)} <= (1.2072 + 0.0722) eps^2 and (1 - sqrt2 rho) e^{-lambda_1(tau-1)} <= (1.2072 + 0.1021) eps^2. Divide by 1 - sqrt2 rho > 0.9858, and use |v_{k*}| >= v_min. ∎

**Which component binds.** Parts (b) and (c) sandwich tau - 1 between max{L/4, (1/4) log(v_min/eps^2)} - 0.07 and the same quantity + 0.15. When v_min >= eps, the first pair to qualify is held back by its hidden belief-model discrepancy n^- (a coordinate of Z_M, rate lambda_2 ≈ 4), and tau ≈ (1/4) log(v_min/eps^2) + 1. For v_min of order rho this is L/2 - 1.15 + (1/4) log(v_min/rho) + 1. When v_min < eps, the common internal residual z_+ ± z_1 binds at about L/4 + 1; its dominant part is the retained common fast normal z_+ (rate ≈ 8), since |z_1| <= sqrt2 rho e^{-8t}. By Lemma 3.4, P(v_min < eps | B) <= 5.645 e^{2 rho dbar} eps/rho, so the hidden discrepancy binds with probability tending to one. Hypothesis H-b's bound tau <= L/2 + 1 is correct. It exceeds the largest possible value, L/2 + 0.03, by about one, and the value for v_min of order rho by about 1.15.

## 5. Divergence at the completion time (item ii)

Write q^G_theta for Law(X_theta, S_theta | G). For h >= 0 define

    M_gen(h)  = 5000 e^{-8} rho^2 e^{-10T(t_1+1)} e^{-2 lambda_2 h} ( e^{-2 rho dbar}/7 - p_hat ) eps^{-4} - 16(1 + 5T/4) e^{-2 lambda_2 h}(t_1+1) - 2,
    M_rare(h) = 2 e^{-46/5} e^{-10T(s_flat+1)} e^{-2 lambda_2 h} ( 0.1427 e^{-2 rho dbar} rho a - rho^2 p_hat ) eps^{-6} - 8(1 + 5T/4) e^{-2 lambda_2 h}(t_1+1) - 1,
    a = min(eps, rho/4).

**Theorem 5.1 (lower bound at tau + h).** For eps in (0,1/100], eps_L in [0,1/t*], and 0 <= h <= (3/2)L,

    H(q^{G_h}_{tau+h})  >=  Phi( max{ M_gen(h), M_rare(h) } ),
    H_phys(q^{G_h}_{tau+h})  >=  Phi( max{ M_gen(h), M_rare(h) } ) - 3.5 (2 e^{-8} rho^2 + 12 T e^{-8h} (t_1+1) + 1.25 T) / (1 - p_hat) - T.

Because rho^2 (1 - 2 e^{-8}) > 0.999 rho^2 exceeds 12 T (t_1+1) + 1.25 T for every eps <= 1/100, the subtracted term is also at most the looser 3.5 (rho^2 + 2T(t_1+1+h) + T) / (1 - p_hat).

At h = 0 (activation at the first completion time, conditioned on the seeded prefix D = G_0), for eps <= 1/400 and as eps -> 0,

    H(q^D_tau)  >=  (1/2) · 2.884e-7 · e^{-2 rho dbar} · eps^{-5} (1 + o(1))  =  1.44e-7 e^{-2 rho dbar} T^{-5/8} (1 + o(1)).

At eps = 1/100 and m_0 = x_circ (dbar = rho), M_gen(0) >= 2230 and H(q^D_tau) >= Phi(2230) > 1103.

*Proof.* On G_h we have tau = tau_hat by Proposition 4.1(a), since G_h ⊂ D. The native process equals the held one on [0, tau+h], and S_{tau+h} = S^(0). Since P(G_h | B) <= 1,

    m(q^{G_h}_{tau+h})  >=  (lambda_2/T) E[ (z_2^2 + z_3^2)(tau_hat + h) 1_{G_h} | B ].

We use the inequality (x+y)^2 >= x^2/2 - y^2 with x = e^{-lambda_2(tau_hat+h)} v_k and y = xi_k(tau_hat+h). By Lemma 2.2(c,d), E xi_k(tau_hat+h)^2 <= 2T e^{-2 lambda_2 h}(t_1+1) + T/lambda_2. Multiplied by lambda_2/T, each subtracted noise coordinate therefore contributes at most 2 lambda_2 e^{-2 lambda_2 h}(t_1+1) + 1 = 8(1 + 5T/4) e^{-2 lambda_2 h}(t_1+1) + 1.

Generic seeds. Since tau_hat <= t_1 + 1, e^{-2 lambda_2(tau_hat+h)} >= e^{-2 lambda_2 h} e^{-8(t_1+1)} e^{-10T(t_1+1)}, and e^{-8(t_1+1)} = 2500 e^{-8} eps^4. Lemma 3.4 and P(G_h^c | B) <= p_hat give E[(v_2^2 + v_3^2) 1_{G_h} | B] >= rho^2 (e^{-2 rho dbar}/7 - p_hat). Collecting terms gives m >= M_gen(h).

Rare seeds. On G_h ∩ {|v_2| <= a}, Proposition 4.1(b) gives tau_hat <= s_flat + 1, where e^{-8(s_flat+1)} = eps^2 e^{-46/5}. Keep only z_3. Lemma 3.4 gives E[v_3^2 1{|v_2| <= a} 1_{G_h} | B] >= 0.1427 e^{-2 rho dbar} rho a - rho^2 p_hat. Collecting terms gives m >= M_rare(h).

Lemma 3.1 converts the two bounds into bounds on H. For H_phys, apply Lemma 3.3. With z^2 <= 2x^2 + 2y^2 and tau_hat >= 1, the second moment satisfies E[|Z|^2 | G_h] <= (2 rho^2 e^{-8} + 2 E |xi(tau_hat+h)|^2)/(1 - p_hat), and Lemma 2.2(c,d) gives 2 E |xi(tau_hat+h)|^2 <= 12 T e^{-8h}(t_1+1) + 2T(1/(8+T) + 2/(4+5T)) <= 12 T e^{-8h}(t_1+1) + 1.25 T. This is the displayed term. The asymptotic line takes a = eps, uses rho p_hat/eps -> 0 and T L -> 0, and evaluates 2 e^{-46/5} · 0.1427 · rho = 2.884e-7. The numerical line at eps = 1/100 uses p_hat < 0.00753 and t_1 + 1 < 2.325, which give M_gen(0) >= 1.6773e-4 · 0.1353 · 1e8 - 39.2 > 2230, where 16(1 + 5T/4)(t_1+1) + 2 < 39.2. ∎

**Why the rate is T^(-5/8).** The generic bound M_gen is of order eps^{-4} = T^{-1/2}. That is the size of the formed pair's own discrepancy at completion, about e^{-4} times the resolution eps^2. The mean is larger because the matching channel also discards the discrepancy of the other matched pair. On seeds with |v_2| <= eps, of probability of order eps/rho, the pair {0,1} qualifies at about L/4 + 1. At that time the other discrepancy is still v_3 e^{-4 tau}, of order rho eps. The per-sample statistic is then of order rho^2 eps^{-6}, and its average over these seeds is of order rho eps^{-5}. Section 7 gives the matching upper bound of the same order one unit after completion.

**Corollary 5.2 (whole first-block event).** Let w = P(G_h)/P(E_T). Then w >= (1 - p_hat) P(B_{sigma,M}) >= (1 - p_hat) c(m_0), where c(m_0) = e^{-1/4} rho^12/737280 · exp[-(|x_circ - m_0| + rho)^2/2] is the floor of prop:phil-early-block-null. For the activation law Law(X_{tau+h}, S_{tau+h} | E_T),

    H( q^{E_T}_{tau+h} )  >=  max{ w Phi(M(h)) - log 2 ,  Phi(w M(h)) },    M(h) = max{M_gen(h), M_rare(h)}.

Hence for every fixed m_0, H(q^{E_T}_tau) >= 1.44e-7 e^{-2 rho dbar} (1-p_hat) c(m_0) T^{-5/8}(1+o(1)) - log 2 -> infinity. The same holds for H_phys by Lemmas 3.2 and 3.3.

*Proof.* G_h ⊂ D ⊂ E_T, so q^{E_T} is the w-mixture of q^{G_h} and q^{E_T \ G_h}. Apply Lemma 3.2 and the linearity remark after it. ∎

The weight is astronomically small. For m_0 = x_circ, c(m_0) ≈ 1.06e-30, and the displayed E_T bound becomes positive only for eps below about 5e-8. The divergence under E_T conditioning is a statement about the limit, not about moderate eps. The seeded prefix bound is already large at eps = 1/100.

## 6. Deterministic activation times (item iii)

For deterministic t in [1, t*], let G(t) = B ∩ A_t, a_k = e^{-2 lambda_k t}, and

    Q(t) = (1/T) [ lambda_1 a_1 E(v_1^2|B) + lambda_2 a_2 E(v_2^2 + v_3^2 | B) ].

By Lemma 3.4,

    e^{-2 rho dbar} (lambda_2 rho^2/(7T)) e^{-2 lambda_2 t}  <=  Q(t)  <=  e^{2 rho dbar} (rho^2/(14T)) (2 lambda_2 e^{-2 lambda_2 t} + lambda_1 e^{-2 lambda_1 t}).

For t >= 1 the lambda_1 term is at most 2.3 e^{-8} times the lambda_2 term, so Q(t) = (4 rho^2/(7T)) e^{-8t} e^{±2 rho dbar}(1 + O(e^{-8})).

**Proposition 6.1 (two-sided bound).** For eps in (0,1/100], eps_L in [0,1/t*], t in [1,t*], and every theta in (0,1),

    Phi( (1-theta)(1 - 7 e^{2 rho dbar} p_hat) Q(t) - 3(1/theta - 1) )  <=  H(q^{G(t)}_t)  <=  [ Q(t)/2 + sum_k a_k^2/(4(1-a_k)) + h_b(p_hat) ] / (1 - p_hat).

The sum is at most (3/(4(1 - e^{-8}))) e^{-16t}. Taking theta = Q^{-1/2} gives, for large Q,

    H(q^{G(t)}_t) = (Q(t)/2)(1 + O(Q(t)^{-1/2}) + O(p_hat)) + O(h_b(p_hat)).

The union of the four seeded prefixes gives the mixture of the four conditional laws. Its upper bound is the maximum of the four upper bounds, by convexity. Its lower bound is Phi of the weighted mean of the four statistics, by linearity of m.

*Proof.* Upper bound. Let Qhat be the held law at t given B. Given the retained state Y_t, the hidden law is the mixture over Law(v_Z | Y_t) of product Gaussians N(e^{-lambda_k t} v_k, (T/lambda_k)(1-a_k)), because retained and hidden coordinates are driven by independent noises and v is independent of the noise. Each component has relative entropy (1/2) sum_k [-a_k - log(1-a_k) + lambda_k a_k v_k^2/T] to kappa. Convexity and -a - log(1-a) <= a^2/(2(1-a)) give H(Qhat) <= Q(t)/2 + sum_k a_k^2/(4(1-a_k)). The event-information identity of the source proof of part (c), applied to 1_{A_t} with R = Qhat_Y ⊗ kappa, gives (1-p) H(Qhat|A_t) <= H(Qhat) + h_b(p) with p = P(A_t^c|B) <= p_hat < 1/2. The last step uses KL(Qhat|A_t || R) >= H(Qhat|A_t), the monotonicity of h_b on [0,1/2], and the equality of Qhat|A_t with q^{G(t)}_t (Lemma 2.2).

Lower bound. By Lemma 2.2(b) and (x+y)^2 >= (1-theta)x^2 - (1/theta - 1)y^2,

    T · m(q^{G(t)}_t)  >=  E[ sum_k lambda_k z_k(t)^2 1_{A_t} | B ]  >=  (1-theta) [ T Q(t) - lambda_2 a_2 rho^2 p_hat ] - 3(1/theta - 1) T,

using sum_k lambda_k a_k E[v_k^2 1_{A_t^c} | B] <= lambda_2 a_2 rho^2 p_hat, since lambda e^{-2 lambda t} decreases in lambda >= 1/2 for t >= 1. The subtracted term is at most 7 e^{2 rho dbar} p_hat · T Q(t) by the lower bound on Q. Apply Lemma 3.1. ∎

**Threshold.** Write t = L + c with c possibly depending on eps. Then e^{-8t}/T = e^{-8c}(1 + o(1)) and Q(t) ≍ (4 rho^2/7) e^{-8c}. If c -> -infinity (with t >= 1), H -> infinity at the rate Q/2 ≍ (2 rho^2/7) e^{-8c}. If c -> +infinity, H -> 0. If c stays bounded, H stays bounded, with H <= (2 rho^2/7) e^{2 rho dbar} e^{-8c}(1 + o(1)) + o(1). These are two one-directional implications, not an equivalence. The lower bound of Proposition 6.1 is vacuous unless (1 - 7 e^{2 rho dbar} p_hat) Q(t) >= 12, because (1-theta) Q - 3(1/theta - 1) >= 3 requires Q >= 3/(theta(1-theta)) >= 12. Up to the factors e^{±2 rho dbar}, 1 - O(p_hat) and 1 + o(1), this is c <= -(1/8) log(21/rho^2) ≈ -1.53 at rho = 1/100. On the window c in [-1.53, O(1)] the error is therefore bounded above by the displayed expression, and its positivity is not proved. The value where H is of order one is t ≈ L - 1.3, which agrees with the Gaussian-surrogate curve in stage4-exact-checks.md, Task 2 (H = 1 at t - L ≈ -1.40 for the matched second moment). At t_eps = 2L the upper bound reduces to hypothesis H-a's (eta_eps + h_b(p_tilde))/(1 - p_tilde). Its terms are O(rho^2 T) + O(T^2) + O(h_b(p_hat)), so the bound is O(eps^4 L log(1/eps)). H-a is therefore confirmed at the original mobility: activation at any deterministic theta in [t_eps, t*] on the seeded prefix has vanishing discarded information.

The sibling note [stage4-seeded-hidden-information.md](stage4-seeded-hidden-information.md), written in this round on the same author model, derives the deterministic-time upper bound and a deterministic-time lower bound of order e^{8(L-theta)} independently. Its threshold agrees with Proposition 6.1. Agreement between the two notes is not verification.

The first qualifying completion time is at most L/2 + 0.03, well before the thermalization threshold L. This is why the completion clock of Section 5 diverges while the deterministic clock of prop:rg-formation-endogenous-cycle(c) does not.

## 7. Delayed activation after completion (part of item v)

**Proposition 7.1 (two-sided bound for tau + h).** For eps in (0,1/100], eps_L in [0,1/t*], and 0 < h <= (3/2)L, let a_k = e^{-2 lambda_k h} and

    Xi = 0.04474 e^{2 rho dbar} rho eps^{-5} + 4.40e-3 eps^{-4} + 2.69e-3 rho^2 p_hat eps^{-8} + 64.01 (t_1 + 1).

Then

    H(q^{G_h}_{tau+h})  <=  [ (e^{-2 lambda_2 h}/2) Xi + sum_k a_k^2/(4(1-a_k)) + h_b(p_hat) ] / (1 - p_hat),

and Theorem 5.1 gives the lower bound Phi(max{M_gen(h), M_rare(h)}) >= Phi(M_rare(h)). As eps -> 0, both bounds are of order e^{-8h} T^{-5/8} when that quantity is large. Consequently H(q^{G_h}_{tau+h}) -> 0 when h - (5/8)L -> +infinity, and H(q^{G_h}_{tau+h}) -> infinity when h - (5/8)L -> -infinity with h >= 0. These two implications are not an equivalence. Phi(M_rare(h)) is zero unless M_rare(h) >= 3, which asymptotically requires e^{-8h} eps^{-5} >= 4/2.884e-7 ≈ 1.39e7, that is h <= (5/8)L - 2.06. On the window h - (5/8)L in [-2.06, O(1)] the error is bounded above by 0.02237 e^{2 rho dbar} rho e^{-8(h - 5L/8)}(1 + o(1)) + o(1), and its positivity is not proved.

*Proof.* Held law at the optional time tau_hat + h. Given F_{tau_hat}, the future hidden and retained increments are independent Brownian motions. The hidden coordinates at tau_hat + h are therefore N(e^{-K_Z h} z(tau_hat), (T K_Z^{-1})(I - e^{-2 K_Z h})) given F_{tau_hat}, independent of the retained state at tau_hat + h. The hidden conditional given that retained state is a mixture of these Gaussians. Convexity bounds the held law's H by (e^{-2 lambda_2 h}/(2T)) E[sum_k lambda_k z_k(tau_hat)^2 | B] + sum_k a_k^2/(4(1-a_k)).

Bound on E[sum_k lambda_k z_k(tau_hat)^2 | B]. Use z^2 <= 2x^2 + 2y^2 with x the deterministic part and y the noise. The noise contributes at most 2(lambda_1 + 2 lambda_2) · 2T(t_1+1) by Lemma 2.2(c). On D^c, tau_hat >= 1 gives sum_k lambda_k v_k^2 e^{-2 lambda_k tau_hat} <= lambda_2 e^{-2 lambda_2} rho^2, with probability at most p_hat. On D, Proposition 4.1(c) gives three bounds. The own discrepancy satisfies lambda_2 v_{k*}^2 e^{-2 lambda_2 tau} <= lambda_2 e^{-2 lambda_2}(1.28 eps^2)^2. The z_1 term is at most 1.769 lambda_1 e^{-2 lambda_1} rho^2 eps^4. The other discrepancy satisfies

    lambda_2 v_{k'}^2 e^{-2 lambda_2 tau}  <=  lambda_2 e^{-2 lambda_2} rho^2 min{ 1.33 eps^2 , 1.6384 eps^4 / v_min^2 },

because e^{-2 lambda_2 (tau-1)} <= (1.33 eps^2)^{2 lambda_2/lambda_1} <= 1.33 eps^2 and |v_{k*}| >= v_min. By Lemma 3.4, for A, Bc > 0,

    E_B min{A, Bc/v_min^2} = ∫_0^A P(v_min < sqrt(Bc/s)) ds <= e^{2 rho dbar} (5.645/rho) · 2 sqrt(A Bc),

which is at most e^{2 rho dbar} 16.67 eps^3/rho for A = 1.33 eps^2 and Bc = 1.6384 eps^4. With lambda_2 e^{-2 lambda_2} <= 1.3420e-3 and 2 · 1.3420e-3 · 16.67 < 0.04474, the terms add up to at most T · Xi. The z_1 term, 3.54 lambda_1 e^{-2 lambda_1} rho^2 eps^4 < 4e-10 eps^4, is absorbed in the rounding of the eps^{-4} coefficient.

Transfer to the native law. G_h = B ∩ A_{tau_hat+h}, with P(G_h^c | B) <= p_hat by Lemma 2.3. On G_h the native path equals the held path through tau_hat + h, and tau_hat = tau (the native and held completion times agree because the paths agree up to that time). The event-information step of Proposition 6.1 applies verbatim.

Threshold. As eps -> 0, the leading upper term is 0.02237 e^{2 rho dbar} rho e^{-8h} eps^{-5}(1 + o(1)). This term leads only asymptotically. The p_hat term (e^{-2 lambda_2 h}/2) 2.69e-3 rho^2 p_hat eps^{-8}, with 2.69e-3 rho^2 p_hat eps^{-8} = 0.0198 t* eps^{-4}(1 + o(1)), exceeds the eps^{-5} term until eps t* < 0.0226, that is for eps above about 1.6e-3; the ratio of the two is 4.53 at eps = 1/100, 1.44 at eps = 2.5e-3 and 0.66 at eps = 1e-3. The remaining terms are o(1) once e^{-8h} eps^{-5} -> 0, because e^{-8h} L <= eps^5 L. The leading lower term is M_rare(h)/2 ≈ 1.44e-7 e^{-2 rho dbar} e^{-8h} eps^{-5}. The subtracted noise in M_rare(h) is 8(1 + 5T/4) e^{-2 lambda_2 h}(t_1+1) + 1 = O(e^{-8h} L) + 1, which is negligible when e^{-8h} eps^{-5} -> infinity. ∎

At h = 1 the two bounds give, as eps -> 0, c_- e^{-2 rho dbar} T^{-5/8}(1 + o(1)) <= H <= c_+ e^{2 rho dbar} T^{-5/8}(1 + o(1)), with c_- ≈ 4.8e-11 and c_+ ≈ 7.5e-8. Both constants are asymptotic only; at moderate eps, for example eps = 1/100, the p_hat term of Xi dominates the upper bound and c_+ does not bound H. The divergence rate just after completion is therefore exactly T^{-5/8} as eps -> 0, and the constants are far from sharp. At h = 0 only the lower bound is proved. The convexity upper bound needs a_k < 1, and the hidden conditional law at the optional time tau itself is not controlled.

## 8. Mobility (obligation 3 for this item)

Every statement above holds for every eps_L in [0,1/t*], with the single constant p_hat. The rows enter nothing but the departure probability of proposals, through the entry ratio bound 2e^{eps_L t*} - 1 <= 2e - 1, which multiplies e^{-1/T}. The configuration drift, the noise, the channel, the reference conditional kappa, the contrast event, and tau do not involve the rows. For larger mobilities one replaces 18 in p_hat by 4(2e^{eps_L t*} - 1). The original coupled mobility eps_L = eps = T^{1/8} satisfies eps t* <= 0.1022, and every slow schedule, including eps_L = o(T^{1/4}) and eps_L <= T^2, is covered. The activation-time dichotomy is therefore the same at eps_L = T^(1/8) and on slow schedules. The slow schedules add nothing for this obligation, and the original mobility loses nothing.

## 9. Consequences for "activated from the recognition law of the episode prefix" (item v)

The table lists each activation convention, the conditioning, the result, and its status. L = log(1/eps) = (1/8) log(1/T).

| Activation clock | Conditioning | Discarded conditional KL of the type-(b) parent | Status |
| --- | --- | --- | --- |
| first completion time tau of K_T | seeded prefix D | >= 1.44e-7 e^{-2 rho dbar} T^{-5/8}(1+o(1)), diverges | proved (Thm 5.1) |
| tau | whole first-block event E_T | >= (1-p_hat) c(m_0) · (same) - log 2, diverges | proved (Cor 5.2) |
| deterministic t | seeded prefix G(t) | about (2 rho^2/7) e^{-8(t-L)} (two-sided when large, an upper bound otherwise): diverges for t - L -> -inf, vanishes for t - L -> +inf; positivity not proved for t - L in [-1.53, O(1)] | two implications proved (Prop 6.1); positivity on the window OPEN |
| deterministic t in [t_eps, t*] | seeded prefix | O(eps^4 L log(1/eps)), vanishes (H-a) | proved (Prop 6.1) |
| tau + h | seeded prefix G_h | ≍ e^{-8h} T^{-5/8} for h >= 1 as eps -> 0: vanishes if h - (5/8)L -> +inf, diverges if h - (5/8)L -> -inf; on h - (5/8)L in [-2.06, O(1)] at most 0.02237 e^{2 rho dbar} rho e^{-8(h - 5L/8)}(1+o(1)) + o(1), positivity not proved | two implications proved (Prop 7.1); positivity on the window OPEN |
| tau + h | whole event E_T | diverges for h - (5/8)L -> -inf; upper bound unknown | lower bound proved; upper bound OPEN |
| deterministic t | {tau <= t}, t >= L + omega(1) | no lower bound, no upper bound | OPEN |
| realized fine history | Dirac hidden conditional | infinite | rem:phil-conditioned-hidden-sign |

Suppose the phrase in open:rg-formation-adaptive-family is read as activation at the moment the first block completes its qualifying interval, from the recognition law conditioned on contrast formation. Then no type-(b) parent has a vanishing conditional error, for any mobility, as soon as eps is below the m_0-dependent threshold of Corollary 5.2. That branch of the settling condition cannot then be met by type-(b) parents in any arm, independently of whether learning selects anything. The obstruction is dynamical, not an event-information artifact. Even the seeded prefix, whose failure probability given the seed is at most p_hat, diverges at tau. The contrast resolution eps^2 = T^{1/4} in the residual is far above the thermal scale T^{1/2}, and the qualifying window has length one, while the hidden discrepancies relax at rate about 4. At completion the formed pair's discrepancy is still about e^{-4} eps^2, and the other matched pair's discrepancy can be of order rho eps.

A heuristic remark, not proved here: no choice of internal resolution rescues activation at completion. A residual resolution r_res makes the formed pair's discarded information at completion of order e^{-8} r_res^2/T. A resolution of order sqrt T or below makes a unit-window clause a thermal event of probability bounded away from one, which is the situation of rem:phil-conditioned-hidden-sign.

A vanishing conditional error is available on the seeded prefix under two conventions: deterministic activation at t with t - L -> +infinity, including prop:rg-formation-endogenous-cycle(c,d)'s t_eps; and delayed activation at tau + h with h - (5/8)L -> +infinity. With the whole contrast event as conditioning, both conventions are open. They need a bound on the hidden coordinates, relative to the held matching at the activation time, over contrast histories that do not start in a seed ball. In those histories the pre-entrance hidden state need not be O(rho), and the assignment at activation need not be a matching. On a non-matching stratum the channel discards nothing and contributes zero. For R16, a nontrivial first branch of the settling condition should therefore declare its activation delay, together with a class of contrast histories on which the delayed error is proved. As written, the row does not fix the clock, and the completion-time reading makes that branch unattainable for type-(b) parents.

## 10. Status of the orchestrator hypotheses (item vi)

H-a is confirmed at deterministic activation theta in [t_eps, t*] at mobility eps, with the rows entering only through the ratio bound. The bound is the upper side of Proposition 6.1. Its mechanism is the forgetting of the seed offset by the held Ornstein-Uhlenbeck process, whose hidden rates are at least 4, together with event information conditioned on the seed, where the remainder A fails with probability at most p_hat. This avoids rem:phil-conditioned-hidden-sign, because the seed's own influence on the hidden coordinates is removed dynamically rather than by a high-probability argument.

H-b is correct in mechanism and incorrect in rate. The bound tau <= L/2 + 1 holds; the sharper statement is tau <= L/2 + 0.03 on the seeded prefix, with tau - 1 >= L/4 - 0.04 in all cases. The binding component is the hidden belief-model discrepancy n^- for seeds with v_min >= eps, and the common fast normal otherwise. The Donsker-Varadhan argument with f = lambda z^T K_Z z/T works, but the noise must be controlled by the optional-stopping moment bound of Lemma 2.2, not by the eps^2 tube. The resulting divergence is at least of order T^{-5/8}, which exceeds T^{-1/2}. The T^{-1/2} statement is a valid but non-sharp lower bound, namely M_gen. The transfer to E_T through H(q) >= sum w_b H(q_b) - log 2 is valid, with weight at least (1 - p_hat) c(m_0), and it holds only asymptotically because c(m_0) is of order 1e-30 or smaller. The threshold "t >= log(1/eps) + omega(1)" is correct for deterministic activation. For activation measured from tau the threshold is h >= (5/8) log(1/eps) + omega(1).

## 11. What ran

The CPU interpreter C:/Python314/python.exe (numpy 2.4.4, scipy 1.17.1) ran two scripts, whose durable copies are in C:\Users\chris and christine\Desktop\MultiAgentELBO\docs\derivations\2026-09-26-selection-to-formation\stage4-evidence\author-scratch\ (repository path `docs/derivations/2026-09-26-selection-to-formation/stage4-evidence/author-scratch/`). The first, stage4_activation_check.py, exited 0 with output in stage4_activation_check_output.json and ran in 81 s. The second, stage4_phys_const.py, printed its output, which was not saved to a file. They are numerical checks, not proofs. The load-bearing numbers are also recorded here. The verifier's scripts and outputs are in the sibling folder `stage4-evidence/fable-scratch/`.

The residual identities of Lemma 2.1 hold to 8.9e-16. The hidden projection of x_circ is zero, and z_+(x_circ) = -1. K restricted to Z equals diag(8+T, 4+5T, 4+5T) to 1.8e-15. ||P_m F^T|| = 0.866 = sqrt3/2, and |d_z|^2 - 2(z_2^2 + z_3^2) = 2e-16.

The constants evaluate to c_12 = 1.41104, E_unif min(v_2^2, v_3^2) = 0.02596 rho^2, and (15/16)^{13/2} = 0.65738. The margins of Proposition 4.1 are 0.8785 eps^2 for (a) at eps = 1/100, decreasing to 0.625 eps^2 as eps -> 0, and 0.9793 eps^2 for (b). p_hat = 0.00753 at eps = 1/100.

The Monte Carlo was noise-free. It drew 2e5 seeds uniform in the rho-ball, computed the first completion time on a 2e-3 grid, and computed the statistic m = E[z(tau)^T K_Z z(tau)]/T + 3. The table lists the results.

| eps | max tau | t_1 + 1 | min tau | L/4 + 1 | m eps^4 | m eps^5 | share of m from v_min <= eps |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1e-2 | 2.226 | 2.325 | 2.128 | 2.151 | 1.93e-4 | 1.93e-6 | 1.00 |
| 1e-3 | 3.186 | 3.476 | 2.704 | 2.727 | 7.60e-3 | 7.60e-6 | 0.60 |
| 1e-4 | 4.342 | 4.627 | 3.278 | 3.303 | 9.38e-2 | 9.38e-6 | 0.48 |
| 3e-5 | 4.940 | 5.229 | 3.580 | 3.604 | 3.15e-1 | 9.45e-6 | 0.49 |

The column m eps^5 levels off near 9.4e-6 while m eps^4 grows, consistent with the T^{-5/8} rate. The observed minimum of tau stays above L/4 + 1 - 0.04, as Proposition 4.1(c) requires. The proved lower bound 2.88e-7 eps^{-5} on m is about 33 times below the observed value. The proved upper bound on the corresponding mean, 0.0447 rho eps^{-5} = 4.5e-4 eps^{-5} in Proposition 7.1, is about 48 times above it. The numbers observe the rate and do not prove it.

## 12. Strongest supported result, open obligations, and next action

The strongest supported result is as follows. For the type-(b) parent on the original four-cycle regime (T = eps^8, N(m_0, I) initial law, learned product rows) and every mobility in [0, 1/t*], including the original T^{1/8}, the discarded optimizing and physical conditional relative entropies on the seeded early prefix satisfy three statements. At the first qualifying completion time they diverge at least like T^{-5/8}. At deterministic times t they diverge when t - (1/8) log(1/T) -> -infinity and vanish when t - (1/8) log(1/T) -> +infinity. At delayed times tau + h they diverge when h - (5/64) log(1/T) -> -infinity and vanish when h - (5/64) log(1/T) -> +infinity. Each pair is two one-directional implications, not an equivalence: on the windows t - L in [-1.53, O(1)] and h - (5/8)L in [-2.06, O(1)] the errors are bounded above by the displayed constants times e^{-8(t-L)} and e^{-8(h - 5L/8)} respectively, and their positivity is not proved. Under conditioning on the whole first-block event, divergence at completion is proved for every fixed m_0.

The first open obligation is an upper bound for Law(X_{tau+h}, S_{tau+h} | E_T) with h - (5/8)L -> +infinity, or a counterexample. This is the smallest missing step for a positive conditional error under the literal first-contrast conditioning. It needs a general-entrance version of Proposition 4.1: for a contrast history of E_T, bound the hidden coordinates relative to the assignment held at tau + h, with a pre-entrance hidden state that may be of order one rather than of order rho. It also needs a bound on the conditional weight of histories whose assignment at activation is a matching entered late. The second open obligation is an upper bound at h = 0, at the optional time tau itself. Only the lower bound is proved there. The two-sided rate is established from h = 1 on, as eps -> 0. The third open obligation is the positivity of the error on the windows h - (5/8)L in [-2.06, O(1)] and t - L in [-1.53, O(1)], where the displayed lower bounds are vacuous. Closing it needs a lower bound that does not pass through Phi at a mean statistic near 3, for example a lower bound on the rare-seed mixture component that keeps the displacement of z_3 relative to its thermal width. The fourth open obligation is the heuristic remark in Section 9, that no internal resolution rescues activation at completion, which is not proved.

The next action that would change the answer is to prove or refute the general-entrance bound. For E_T histories, the relevant object is the assignment process on [tau - 1, tau + h] and the hidden state at the last entrance into the held matching. If late entrances with O(1) hidden displacement have conditional probability bounded below in E_T, the whole-event delayed error does not vanish at h = (5/8)L, and the threshold for E_T moves to about h = L + O(1) or beyond. If such entrances have vanishing conditional weight, Proposition 7.1 extends to E_T.
