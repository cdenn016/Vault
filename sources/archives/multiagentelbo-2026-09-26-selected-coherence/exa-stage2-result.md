## Conclusion

**Yes: on a refinement of your implicit slow-learning schedule, late selected-pair persistence and an asymptotically unchanged first-episode law coexist.** The first-law assertion is a theorem for any common, path-measurable marked stopping rule that is almost surely finite under the frozen process. It does not require assuming that the adaptive stopping time is almost surely finite.

There are two important limits:

- Late selected-pair coherence is **restored equilibrium coherence**, in your R15 terminology—not, by itself, formation.
- Applying the first-law theorem to **genuine contrast formation** requires validating that event and its conditioning probability. Neither stationary matching masses nor generic recurrence supplies those validations. The original regime \(T=\epsilon^8\), mobility \(\epsilon\), horizon \(2/\epsilon\) remains unresolved.

I take your corrected ranks, determinant powers, and fixed-temperature selection results as inputs; no determinant calculation is changed below.

## A. Coherent partitions and actual-path persistence

Write
\[
R_e x=(r_{b,e}(x),r_{m,e}(x)),\qquad
\mathcal C_a^M=
\left\{\|R_e x\|\le a\ (e\in M),\quad
\|R_e x\|>a\ (e\notin M)\right\}.
\]
Here \(M\) denotes both the selected matching assignment and its two undirected edges. Put
\[
s=t_L=2\varepsilon^{-1}\log(1/\varepsilon),\qquad
A_M=H_M+T\Omega.
\]
Constants below can be chosen uniformly over the two matchings and sufficiently small \(T\).

### A1. The precise late-law estimate used

For a matching \(M\) fixed throughout the late interval, use the supplied convergence in the form
\[
\sup_{s\le t\le2s}
 d_{\rm TV}(q_t,\nu_T^M)\le\delta,
\qquad
\nu_T^M=N(0,TA_M^{-1})\otimes\delta_M. \tag{1}
\]
Only the initial-time TV bound and uniform assignment occupation bound are needed below. If the inputs are expressed as entropy and row convergence instead, they give (1), at fixed \(T\), through
\[
d_{\rm TV}(q_t,\nu_T^M)
\le \sqrt{\tfrac12 H(q_t\mid\mu_{p(t)})}
       +1-\mu_{p(t)}(\sigma=M).
\]
The second term tends to zero as the rows approach the matching vertex: the conditional Gaussian on sheet \(M\) is exactly the Gaussian in \(\nu_T^M\). The implicit thresholds can therefore be refined to achieve any specified \(\delta\).

### A2. One-time coherence

Under \(\nu_T^M\), the selected normal modes have the given drift rates
\[
8+T,\qquad 4+5T,
\]
and stationary variances of order \(T\). Thus
\[
\Pr_{\nu_T^M}\!\left(\exists e\in M:\|R_eX\|>a\right)
 \le C e^{-c a^2/T}. \tag{2}
\]
For each exterior edge, use a unit scalar projection \(Z_e\) of its residual vector whose variance is bounded below by a positive constant. The stated nondegenerate exterior components supply this. Gaussian anti-concentration gives
\[
\Pr_{\nu_T^M}(\|R_eX\|\le a)
\le \Pr(|Z_e|\le a)\le Ca. \tag{3}
\]
This deliberately uses only one nondegenerate component; it does not assume an unproved two-dimensional density bound.

Consequently, throughout the late interval,
\[
\boxed{\quad
\Pr_q\{X_t\in\mathcal C_a^M,\ \sigma_t=M\}
\ge 1-\delta-Ca-Ce^{-c a^2/T}.
\quad} \tag{4}
\]
Hence \(\sqrt T\ll a(T)\ll1\) gives the desired matching partition with probability tending to one.

For comparison, your frozen equilibrium masses imply
\[
\mu(\mathcal C_a^M)
=\frac1{2D_0}+O\!\left(T+a+e^{-c a^2/T}\right).
\tag{5}
\]
Indeed, the conditional law on each matching sheet has the preceding coherence property, while the total nonmatching-sheet mass is \(O(T)\). Thus frozen late coherence splits asymptotically equally between the two matching partitions; learned late coherence selects one. **Equation (5) says nothing about which block appears first.**

### A3. Actual posterior redraws: the occupation identity

The essential point is not to treat \(\nu_T^M\) as the actual process, or to identify assignment occupation with a pointwise posterior hazard.

Let \(K_{p(t)}(x,\cdot)\) be the actual conditional Gibbs redraw kernel, and define
\[
f(t)=\Pr_q(\sigma_t\ne M),\qquad
g(t)=\mathbb E_q K_{p(t)}(X_t,M^c).
\]
Because the entire assignment is redrawn at rate one,
\[
f'(t)=g(t)-f(t) \quad\text{a.e.} \tag{6}
\]
The expected number of redraws into \(M^c\) on \([s,s+W]\) is therefore
\[
\int_s^{s+W}g(t)\,dt
=f(s+W)-f(s)+\int_s^{s+W}f(t)\,dt.
\]
It follows that
\[
\begin{aligned}
&\Pr_q\{\sigma_s\ne M\text{ or a redraw into }M^c
                   \text{ occurs before }s+W\}\\
&\hspace{12mm}\le f(s+W)+\int_s^{s+W}f(t)\,dt
\le (W+1)\delta,
\qquad W\le s. \tag{7}
\end{aligned}
\]
This is an **unconditional actual-law estimate**, not a bound on every trajectory's conditional hazard. It uses the actual posterior redraw mechanism exactly. In particular, no separate entropy-to-posterior approximation is needed for this step.

Maximally couple \(q_s\) to \(\nu_T^M\), with initial failure probability at most \(\delta\). From the coupled Gaussian state run
\[
dY_u=-A_MY_u\,du+\sqrt{2T}\,dW_u
\]
with the same Brownian motion as the adaptive process. Until an actual redraw leaves \(M\), the paths agree. Equations (1) and (7) give the safe bound
\[
d_{\rm TV}\!\left(
\mathcal L_q((X_{s+u},\sigma_{s+u})_{0\le u\le W}),
\mathcal L((Y_u,M)_{0\le u\le W})\right)
\le (W+2)\delta. \tag{8}
\]
The held-sheet process is therefore a **controlled path comparison**, not a silent replacement of the dynamics.

### A4. Gaussian path bounds, including exterior bridges

For the selected residuals, apply a Gaussian initial tail and a Brownian maximal bound on each unit interval. The two specified normal rates are bounded above and away from zero. Stationarity of \(Y\) then gives
\[
\Pr\!\left(\sup_{0\le u\le W}\max_{e\in M}\|R_eY_u\|>a\right)
\le C(1+W)e^{-c a^2/T}. \tag{9}
\]
Those rates are **not** assigned to the exterior residuals.

For the exterior edges, the relevant control is their small displacement on windows short compared with \(T^{-1}\). Since \(A_M\) is symmetric and \(A_M\ge TI\), diagonalize it. In an eigenmode of eigenvalue \(\lambda\), the initial part of the stationary increment has variance
\[
\frac{T}{\lambda}(1-e^{-\lambda W})^2\le TW.
\]
For its stochastic part, integration by parts yields
\[
\sup_{u\le W}\left|\int_0^u e^{-\lambda(u-v)}\,dB_v\right|
\le 2\sup_{u\le W}|B_u|.
\]
Gaussian tails, Brownian reflection, and a finite-dimensional union bound consequently give
\[
\Pr\!\left(\sup_{u\le W}\|Y_u-Y_0\|>b\right)
\le C\exp\!\left(-\frac{cb^2}{TW}\right), \tag{10}
\]
with adjusted constants for any of the residual projections. The bound is useful when \(b^2\gg TW\).

If initially \(|Z_e(0)|>a+b\) and its displacement stays below \(b\), that exterior edge never becomes coherent. Combining (3), (8)–(10) gives
\[
\boxed{
\begin{aligned}
&\Pr_q\!\left\{
  \sigma_{s+u}=M,\ X_{s+u}\in\mathcal C_a^M
  \text{ for every }0\le u\le W\right\}\\
&\quad\ge 1-(W+2)\delta
-C(1+W)e^{-c a^2/T}
-C(a+b)-C e^{-cb^2/(TW)},
\qquad 1\le W\le s.
\end{aligned}} \tag{11}
\]
This proves persistence of the **entire partition**, not merely continued coherence of the selected edges while ignoring exterior bridges.

For a unit interval, take \(W=1\), \(b=T^{1/4}\), and \(\delta\to0\). Every error in (11) vanishes under the requested resolution separation.

A rigorously quantified growing window is
\[
\boxed{\quad
W(T)=\min\!\left\{T^{-1/2},\,
                \exp\!\left(\frac{c a(T)^2}{2T}\right)\right\},
\qquad b(T)=(TW(T))^{1/4}.
\quad} \tag{12}
\]
Here \(W(T)\to\infty\), \(TW(T)\to0\), and all intrinsic Gaussian/exterior errors in (11) tend to zero. Refine the learning schedule so that
\[
(W(T)+2)\delta(T)\to0,
\qquad W(T)\le t_L.
\]
Then the actual learned partition persists on \([t_L,t_L+W(T)]\) with probability \(1-o(1)\).

The bare condition \(a/\sqrt T\to\infty\) does not justify an arbitrary prescribed polynomial window. For example, \(a^2/T=\log\log(1/T)\) supplies no polynomial margin against the selected-mode maximum in (9). Formula (12) avoids imposing an unstated logarithmic separation.

These are probability statements for the actual late law, not uniform survival estimates from every point of \(\mathcal C_a^M\). Conditional persistence given the late partition also follows: divide the failure bound in (11) by the initial partition probability, which tends to one by (4).

## B. A first-mark null theorem

### B1. Finite-horizon coupling, uniformly in temperature and mean

Let \(Z=(X,\sigma)\), and distinguish adaptive and frozen laws by \(A\) and \(F\). The rows are deterministic law-level quantities. Their equation and common initialization imply
\[
|p_i(t)-\tfrac12|\le\varepsilon t.
\]
Thus, if \(\varepsilon H\le1/4\), all rows on \([0,H]\) lie in \([1/4,3/4]\).

Write the posterior as
\[
K_p(\sigma\mid x)=
\frac{L_\sigma(x,T)\rho_p(\sigma)}
     {\sum_\tau L_\tau(x,T)\rho_p(\tau)},
\quad
\rho_p(\sigma)=\prod_{i=1}^4
 p_i^{1_{\{\sigma_i=+\}}}(1-p_i)^{1_{\{\sigma_i=-\}}}.
\]
The positive likelihoods \(L_\sigma\) do not depend on the rows. If
\(\theta_i=K_p(\sigma_i=+\mid x)\), differentiation gives
\[
\partial_{p_i}K_p(\sigma\mid x)
=K_p(\sigma\mid x)
\frac{1_{\{\sigma_i=+\}}-\theta_i}{p_i(1-p_i)}.
\]
In particular,
\[
\frac12\sum_\sigma|\partial_{p_i}K_p(\sigma\mid x)|
=\frac{\theta_i(1-\theta_i)}{p_i(1-p_i)}
\le\frac43.
\]
Therefore
\[
d_{\rm TV}(K_p(\cdot\mid x),K_{1/2}(\cdot\mid x))
\le C\sum_i|p_i-\tfrac12|
\le C\varepsilon t, \tag{13}
\]
**uniformly in \(x,T,m\)**. No lower bound on a temperature-dependent partition function is required.

Couple the initial state and assignment identically, use common Brownian motion and the same rate-one clock, and maximally couple the redraws. Until the first mismatched redraw, the continuous states coincide exactly. Integrating (13) over the clock compensator yields
\[
\boxed{\quad
\Pr\{Z^A\ne Z^F\text{ somewhere on }[0,H]\}
\le C_0\varepsilon H^2=:e_H,
\qquad \varepsilon H\le\tfrac14.
\quad} \tag{14}
\]
This compares the \((X,\sigma)\)-paths. It does **not** compare augmented paths that include the unequal deterministic rows.

### B2. Stopping rules, truncation, and conditional probabilities

Fix \(T\). Let \((\tau,L)\) be a **common measurable marked stopping rule** on the \((X,\sigma)\)-path, with the mark measurable at \(\tau\). The rule may depend on \(T\), and on common auxiliary randomness, but must be the same in both arms and fixed as \(\varepsilon\downarrow0\) at fixed \(T\). An \(\varepsilon\)-dependent diverging rule needs its own uniform truncation estimate. It cannot distinguish the arms by inspecting their slightly different row trajectories.

For a detector requiring a subsequent persistence window, its stopping time is the **completion time** of that check—not its retrospectively identified entrance time. The mark can record the earlier entrance and block label.

Give nontermination the mark \(\partial\). Let
\[
b_{T,m}(H)=\Pr_F^{T,m}(\tau>H).
\]
Whenever the frozen rule has completed by \(H\) and the coupled paths agree through \(H\), both arms have the same stopping time and mark. Hence
\[
\boxed{\quad
 d_{\rm TV}(\mathcal L_A(\tau,L),\mathcal L_F(\tau,L))
 \le e_H+b_{T,m}(H).
\quad} \tag{15}
\]
Also,
\[
\Pr_A(\tau>H)\le b_{T,m}(H)+e_H, \tag{16}
\]
and, for every measurable marked event \(B\),
\[
\left|\Pr_A((\tau,L)\in B,\tau\le H)
      -\Pr_F((\tau,L)\in B,\tau\le H)\right|
\le e_H. \tag{17}
\]
If \(\tau<\infty\) frozen-almost-surely, first choose \(H\) to make its tail small, and then let \(\varepsilon\downarrow0\). Equations (15)–(16) prove
\[
\boxed{\quad
 d_{\rm TV}(\mathcal L_A(L),\mathcal L_F(L))\longrightarrow0
 \qquad(T,m\text{ fixed}).
\quad} \tag{18}
\]
Adaptive nontermination has probability tending to zero by the same argument; assuming its almost-sure absence is unnecessary.

For conditioning, let \(E\) be a common event recognized at the stopping time, and put
\[
D_H=e_H+b_{T,m}(H),\qquad \beta=\Pr_F(E).
\]
Apply (15) with the mark augmented by the indicator of \(E\). If \(D_H<\beta\), then
\[
\boxed{\quad
 d_{\rm TV}(\mathcal L_A(L\mid E),\mathcal L_F(L\mid E))
 \le\frac{2D_H}{\beta-D_H}.
\quad} \tag{19}
\]
For the explicitly truncated event \(E\cap\{\tau\le H\}\), use \(e_H\) instead of \(D_H\), and \(\Pr_F(E,\tau\le H)\) in the denominator. Its event probabilities differ by at most \(e_H\), by (17).

Thus a denominator bounded below gives conditional convergence. If that denominator vanishes, the errors must be made smaller than it; unconditional TV convergence alone is insufficient.

### B3. A precise recurring contrast detector is frozen-a.s. finite

Here is a detector whose mark is an individual **pair block**, rather than a late matching label.

Fix \(T>0\), a small \(a>0\), a holding time \(h>0\), and a fixed \(b>2a\). Choose:

- A compact source set \(U\), with nonempty interior, where all four residual norms exceed \(b\).
- For each edge \(e\), a compact target \(K_e\), with nonempty interior, lying strictly inside the open region
  \[
  V_e=\{\|R_e x\|<a,\ \|R_f x\|>b/2\text{ for every }f\ne e\}.
  \]

These sets are nonempty in the stated shared-link model: for example, set the vertex coordinates equal and choose the edge links to make either all residuals large or precisely one residual small. The \(V_e\)'s are disjoint.

Define the common hysteretic detector as follows:

1. Wait for a visit to \(U\), thereby recording an incoherent precursor.
2. Wait for the first subsequent visit to \(\bigcup_e K_e\), and record its unique edge \(e\).
3. If the path stays in \(V_e\) for the next \(h\) units, complete the episode and return mark \(e\). If it exits earlier, reset and wait for a new visit to \(U\).

The first completed successful episode is a marked stopping time. It requires an actual entry from an incoherent precursor into a contrasting one-pair region, followed by a coherence window. It is not a generic coherence first hit.

For completeness, the frozen recurrence argument has concrete ingredients. With \(V(x)=\|x\|^2\),
\[
\mathcal LV(x,\sigma)
=-2x^T(H_\sigma+T\Omega)x+24T
\le-2T\|x\|^2+24T. \tag{20}
\]
Every held-assignment transition has a nondegenerate Gaussian covariance
\[
2T\int_0^u e^{-2A_\sigma v}\,dv.
\]
On compact sets, these transition densities have positive local lower bounds. A prescribed clock ring has positive probability, and all frozen Gibbs assignment probabilities have positive compact-set lower bounds. These are exactly the drift and local minorization ingredients of the existing Harris proof. Consequently the frozen process reaches \(U\) and each target of positive volume almost surely from every starting state.

At a target visit, there is a uniform positive chance of a successful holding window. Indeed,
\[
\gamma_T
=e^{-h}\min_{e,\sigma}\inf_{x\in K_e}
 \Pr_x^{\text{held }\sigma}\{Y_u\in V_e\text{ for all }0\le u\le h\}
>0. \tag{21}
\]
The factor \(e^{-h}\) explicitly pays for **no clock rings during the holding window**. The remaining positivity is the finite-time Gaussian path-tube property of a nondegenerate OU process; compactness and the strict inclusion \(K_e\Subset V_e\) make it uniform over the target and the finitely many assignments. This lower bound is a subevent of success under the actual frozen redraw dynamics, not an assumption that assignments are held fixed.

After a failed attempt, recurrence supplies another attempt. By the strong Markov property, the probability that the first \(k\) attempts all fail is at most \((1-\gamma_T)^k\). Therefore
\[
\Pr_F^{T,m}(\tau<\infty)=1
\]
for every mean \(m\). Matching-partition targets can be used instead if that is the desired episode mark.

Crucially, \(\gamma_T\) need not be bounded below as \(T\downarrow0\), and this proof supplies no temperature-uniform entrance-time estimate. It establishes a recurring contrast/restoration detector, **not automatically an R15 formation detector**: the required comparison with stationary entrance recurrence, or positive excess over the stationary benchmark, remains to be proved.

## C. Full slow-diagonal quantifiers

Let \(T_n\to0\), \(\eta_n\to0\), and \(a_n=a(T_n)\) be arbitrary, with
\[
a_n\to0,\qquad a_n/\sqrt{T_n}\to\infty.
\]
For each \(n\), fix a common marked rule \(\tau_n\) that is frozen-a.s. finite for almost every mean. The preceding detector is one concrete example. No uniform-in-\(T\) recurrence estimate is assumed.

Set
\[
\zeta_n=\min\{\eta_n,2^{-n}\},
\qquad W_n=W(T_n),
\qquad \delta_n=\frac{\zeta_n}{10(W_n+2)}.
\]
Choose a probability measure \(\Gamma\) on \(\mathbb R^{12}\) with an everywhere-positive density. By dominated convergence, choose deterministic finite \(H_n\ge n\) such that
\[
\int \Pr_F^{T_n,m}(\tau_n>H_n)\,\Gamma(dm)
\le\zeta_n2^{-n}. \tag{22}
\]
The exceptional mean sets where this tail exceeds \(\zeta_n\) have \(\Gamma\)-measure at most \(2^{-n}\). Borel–Cantelli therefore gives, for Lebesgue-a.e. fixed mean, eventually
\[
\Pr_F^{T_n,m}(\tau_n>H_n)\le\zeta_n. \tag{23}
\]

Use the supplied selection-threshold construction with accuracy \(\delta_n\), taking summable mean exceptions as well. Shrink the resulting positive thresholds to \(d_n<e^{-1}\) so that also
\[
d_nH_n\le\tfrac14,\qquad
C_0d_nH_n^2\le\zeta_n,\qquad
2d_n^{-1}\log(1/d_n)\ge H_n+W_n. \tag{24}
\]
All these are compatible by decreasing \(d_n\).

The resulting statement is:

> There are deterministic thresholds \(d_n>0\), independent of the mean, and a Lebesgue-full set of means such that, for every mean in that set, there is an \(n_0(m)\) for which **every** \(n\ge n_0(m)\) and **every** \(0<\varepsilon\le d_n\) satisfy both conclusions below.

**Late persistence.** There is a matching \(M=M_{n,\varepsilon}(m)\), fixed over the relevant late interval, for which (11) holds on \([t_L,t_L+W_n]\), with learning error at most \(\zeta_n/10\) and intrinsic coherence error tending to zero. The matching need not stabilize across \(n\), or across \(\varepsilon\).

**First-mark null.** With cemetery marks included,
\[
 d_{\rm TV}(\mathcal L_A(\tau_n,L_n),\mathcal L_F(\tau_n,L_n))
 \le2\zeta_n. \tag{25}
\]
Under the coupling, with probability at least \(1-2\zeta_n\), the first episode completes by \(H_n\le t_L\), and its time and mark are identical in the two arms. Thus the null is about the **actual first detected episode**, not a late selected label.

Because \(\sum_n\zeta_n<\infty\), along any chosen sequence \(\varepsilon_n\le d_n\) these paired first marks can even be coupled to agree eventually almost surely. This is not an assertion that the late selected matchings stabilize.

For common conditioning events of frozen probability at least \(\beta_*>0\), (19) gives conditional first-mark convergence as well. More generally, if the lower bounds are \(\beta_n\downarrow0\), choose the tail and coupling budgets to be \(o(\beta_n)\). Such lower bounds must be established; the diagonal construction does not invent them. The probability errors intrinsic to finite-resolution coherence are those in (11), not arbitrarily small solely because the learning tolerance was made small.

## D. What this settles—and what it does not

1. **A is a theorem from the stated inputs.** Selected pairs form the coherent partition with high probability and retain it for a unit interval, indeed for (12), under the actual adaptive redraw process. Its interpretation is late restored equilibrium coherence.

2. **The first-mark null is a theorem on the refined schedule.** It applies to any fixed common detector satisfying frozen a.s. finiteness, including the explicit recurring contrast detector above. It says slow learning does not change that first marked law; it does not say that no transient formation occurs.

3. **Late selection cannot establish first-formation bias.** A selected late matching and asymptotically identical early first-mark laws coexist here. This rules out the inference “late learned selection entails a changed first-block law.” A stronger claim that the late selected matching disagrees with the first mark with probability bounded below requires an additional nondegeneracy estimate for the relevant frozen first-mark law. The stationary masses \(1/(2D_0)\) are not that estimate.

4. **Genuine R15 formation still has explicit obligations.** One must specify the entering-contrast event, validate its restoring/observation horizon against stationary entrance recurrence or prove a positive stationary excess, and establish a usable conditioning probability. Once those are supplied for a common finite-horizon event, (17)–(19) give its learned/frozen first-block comparison; frozen a.s. finiteness of an unlimited-horizon detector is not needed for that truncated comparison. Recurrence alone does not discharge them.

5. **The original adaptive-family problem is not settled.** At \(T=\epsilon^8\) and \(H=2/\epsilon\), the coupling control is not small: \(\epsilon H^2=4/\epsilon\), and even the row-interiority cap used above fails. The slow diagonal supplies neither the needed original-regime horizon estimate nor the positive contrast-formation denominator. Nothing here turns the tracking condition \(\varepsilon=T^a\), \(a>3.5\), into an explicit power-selection theorem.

