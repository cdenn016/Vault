# Stage 2: coherent selected pairs and their following persistence window

September 26, 2026. This note proves a late coherent-partition contrast and persistence for the unchanged shared-link four-cycle. It controls the actual rate-one assignment redraws before using a held-matching Gaussian comparison. The result concerns restored equilibrium coherence on the selected late window. It neither identifies the first block formed nor activates a parent.

The manuscript artifact is `Theory/ca_selected_coherence.tex`, containing `prop:phil-selected-pair-persistence` and its proof. Source continuity was checked against `Theory/c13_formation.tex`, specifically `def:rg-formation-cycle-experiment`, `prop:rg-formation-endogenous-cycle`, and `prop:rg-gated-depth-one`; `Theory/SPEC.md`, including R15; the prior `p15-restoring-vs-recurrence.md`; and the live `Research/manuscripts/pifb2/09_section.tex` and `13_section.tex`. The new proof uses the current selection theorem, elementary Gaussian estimates, and the proposal compensator. It does not adopt the prior P-15 capacity-to-recurrence conversion hypothesis or any unverified sharp rate. No new external reference is used.

## Contract and quantifiers

Fix one base point, a temperature $0<T\le1/100$, the original twelve-dimensional configuration $X=(k,m,\omega)$, and one assignment in $\{\pm1\}^4$. Both directions of an undirected edge use the same link translation. The diffusion between proposals is

$$
dX=-A_S Xdt+\sqrt{2T}dW,\qquad A_S=H_S+T\Omega,\quad\Omega=I+R_{\rm ev}.
$$

The clock has rate one and redraws the complete assignment from its conditional Gibbs law. Learned rows evolve deterministically from the actual recognition law. The frozen arm holds the original uniform rows. There is no boundary in $\mathbb R^{12}$; the smooth positive-temperature dynamics and finite-horizon moment estimates are those of the existing well-posed system.

Let $M$ be one matching and

$$
\nu_T^M=\mathcal N(0,T A_M^{-1})\otimes\delta_M.
$$

Choose a deterministic handoff-free start time $s$ and a following duration $L>0$, with the whole interval $[s,s+L]$ contained in the Stage 1 selection window. Assume

$$
\sup_{s\le t\le s+L}\operatorname{TV}(q_t^{\rm learn},\nu_T^M)\le\delta,
\qquad \operatorname{TV}(q_s^{\rm frozen},\mu_{T,1/2})\le\delta.
$$

These are supplied by the established diagonal selection result with an arbitrarily small tolerance. The matching may depend on temperature and initial mean; this note does not assume its eventual constancy. The extra choices $L(T)$, resolution $a(T)$, and tolerance $\delta(T)$ below are stated rather than silently imposed on the original first-formation regime.

Write $O_{T,L}^M$ for the stationary held-$M$ Ornstein–Uhlenbeck path law, including its constant assignment. All path total variations below compare laws on the same continuous configuration and right-continuous assignment path space over $[0,L]$.

## 1. One-time label concentration controls actual departures

For the learned process put $r(t)=q_t(S\ne M)$. If $b_{\ne M}(t,x)$ is the conditional probability that a proposal returns another assignment, the forward equation for this bounded indicator gives

$$
r'(t)=\mathbb E b_{\ne M}(t,X_t)-r(t).
$$

Let $N_{\ne M}$ count proposals to non-$M$ assignments on $[s,s+L]$, including proposals made while already off $M$. The rate-one compensator therefore gives exactly

$$
\mathbb E N_{\ne M}=r(s+L)-r(s)+\int_s^{s+L}r(t)dt.
$$

A path that is ever off $M$ either starts off $M$ or has such a proposal. Consequently

$$
\Pr(\exists t\in[s,s+L]:S_t\ne M)
\le r(s)+\mathbb E N_{\ne M}\le(L+1)\delta.
$$

Maximally couple the initial complete state with $\nu_T^M$, and use the same Brownian increments for the native dynamics and a held-$M$ comparison. Their configuration and assignment paths agree until an initial mismatch or a proposal away from $M$. This proves

$$
\boxed{\operatorname{TV}(P^{\rm learn}_{s,L},O_{T,L}^M)\le(L+2)\delta.}
$$

The comparison thus follows from a bound on actual departures. It does not assume that a law conditional on an adaptive assignment history is Gaussian. The estimate is uniform in the learned prior because it uses the actual assignment marginal and the fixed rate-one clock.

## 2. The stationary frozen path is close to an equal matching mixture

Use normalized determinant weights $1,r_E,r_N,r_C$ for matching, end-path, middle-path, and oriented-cycle assignments. The Stage 1 determinant bounds give

$$
r_E,r_N\le\tfrac52T,\qquad r_C\le\tfrac32T^{3/2}.
$$

With $D_0=1+4r_E+2r_N+r_C$, the stationary nonmatching mass is

$$
\kappa_T=\frac{8r_E+4r_N+2r_C}{2D_0}\le16T.
$$

Conditional on either matching, the stationary configuration is exactly its Gaussian $\nu_T^M$. Thus the stationary one-time law is within $\kappa_T$ of $(\nu_T^{M_0}+\nu_T^{M_1})/2$.

For a matching $M$, detailed balance bounds its stationary flux to all nonmatching assignments by $\kappa_T$. For the other matching $M'$, write $\mu_M(x)$ for the joint sheet density. Pointwise,

$$
\mu_Mb_{M'}=\frac{\mu_M\mu_{M'}}{\sum_S\mu_S}
\le\tfrac12\sqrt{\mu_M\mu_{M'}}.
$$

The average matrix $(A_M+A_{M'})/2$ equals the oriented-cycle matrix because the two matchings have complementary multiplicities two and zero. Gaussian integration yields

$$
\int\sqrt{\mu_M\mu_{M'}}dx=\mu_{T,1/2}(M)r_C.
$$

Divide the flux bounds by $\mu_{T,1/2}(M)=1/(2D_0)$. The mean proposal probability away from $M$ under its stationary Gaussian is at most

$$
\mathbb E_{\nu_T^M}b_{\ne M}
\le8r_E+4r_N+\tfrac52r_C
\le30T+\tfrac{15}{4}T^{3/2}\le31T.
$$

Hence the combined stationary flux out of the two matching sheets is at most $31T$. Couple the stationary native process initially to the equal matching mixture, then use common Brownian increments until the first departure from the initially coupled matching. The expected number of such native departures on the interval is at most $31TL$, without conditioning its future on its initial sheet. Therefore

$$
\operatorname{TV}(P^{\rm stationary}_{T,L},\tfrac12O_{T,L}^{M_0}+\tfrac12O_{T,L}^{M_1})\le16T+31TL.
$$

The frozen native process has the same time-homogeneous transition law as this stationary process. Its initial total-variation error contracts under the common path kernel, giving

$$
\boxed{\operatorname{TV}(P^{\rm frozen}_{s,L},\tfrac12O_{T,L}^{M_0}+\tfrac12O_{T,L}^{M_1})\le\delta+16T+31TL.}
$$

## 3. Coherence and persistence under the stationary matching comparison

For $a>0$, let $E_M(a,L)$ require that throughout $[s,s+L]$ the assignment is $M$, the Euclidean stacked residual norm $\sqrt{(r^b)^2+(r^m)^2}$ on its edges is at most $a$, and that norm on each exterior edge is greater than $a$.

This is the existing Euclidean coherence criterion. The coherent-component partition at resolution $a$ is exactly the two pairs of $M$. The proof below uses stronger componentwise exterior separation as a sufficient condition for the stated exterior stacked-norm inequality.

The four orthonormal selected normal coordinates $z_g^\pm=n_g^\pm\cdot X$, $g\in M$, have rates $8+T$ and $4+5T$ and stationary variances at most $T/4$. The two channel residuals satisfy

$$
r_g^b=\sqrt2z_g^++z_g^-,\qquad r_g^m=\sqrt2z_g^+-z_g^-.
$$

For any scalar rate $\lambda>0$, the zero-start stochastic convolution can be written

$$
Z_t=\sqrt{2T}\left[W_t-\lambda\int_0^te^{-\lambda(t-u)}W_u du\right].
$$

Thus $\sup_{t\le L}|Z_t|\le2\sqrt{2T}\sup_{t\le L}|W_t|$. The Brownian maximal bound $\mathbb E\sup_{t\le L}|W_t|^2\le4L$, already proved in the existing episode argument, gives $\mathbb E\sup|Z_t|^2\le32TL$. For the four normal coordinates, split stationary initial value and zero-start noise and sum the resulting bounds:

$$
\mathbb E\sup_{t\le L}|z_t|^2\le2T+256TL.
$$

Each selected stacked norm is at most $2|z_t|$, because $(r_g^b)^2+(r_g^m)^2=4(z_g^+)^2+2(z_g^-)^2$. Thus internal coherence fails with probability at most $(8+1024L)T/a^2$.

Every exterior link coordinate is absent from $H_M$ and decoupled in $\Omega$. In the stationary Gaussian it is therefore an independent $\mathcal N(0,1)$ coordinate. Each exterior belief or model residual has variance at least one. The Gaussian density bound gives $\Pr(|r|\le2a)\le2\sqrt{2/\pi}a$ for each of these four residuals, hence an initial exterior failure bound $8\sqrt{2/\pi}a$. Independence between different residuals is not assumed.

To propagate exterior separation, diagonalize $A_M$. For a stationary scalar eigencoordinate of rate $\lambda>0$,

$$
\begin{aligned}
\mathbb E\sup_{t\le L}|X_t-X_0|^2
&\le\frac{2T}{\lambda}(1-e^{-\lambda L})^2+64TL\\
&\le66TL,
\end{aligned}
$$

because $(1-e^{-v})^2\le v$ for $v\ge0$. Summing the twelve eigencoordinates gives

$$
\boxed{\mathbb E\sup_{t\le L}|X_t-X_0|^2\le792TL.}
$$

This is linear in $L$; bounding drift by a time integral and obtaining an unnecessary $L^2$ is avoided. Each residual covector has norm $\sqrt3$. All exterior increments are consequently at most $a$ except on an event of probability at most $2376TL/a^2$. Combining these estimates proves

$$
O_{T,L}^M(E_M(a,L)^c)\le b(T,a,L),
\quad b(T,a,L)=8\sqrt{2/\pi}a+(8+3400L)T/a^2.
$$

The native learned process therefore satisfies

$$
\boxed{\Pr_{\rm learn}(E_M(a,L)^c)\le(L+2)\delta+b(T,a,L).}
$$

In particular, $\sqrt T\ll a\ll1$, $TL/a^2\to0$, and $L\delta\to0$ suffice. Fixed unit windows require only the first resolution condition and $\delta\to0$. A growing example is

$$
a=T^{1/4},\qquad L=T^{-1/4},\qquad\delta\le T,
$$

for which the failure bound is $O(T^{1/4})$. The constants are intentionally nonoptimal. The Stage 1 schedule accepts the tolerance $T$ and mobility cap $\epsilon_L\le T^2$. With $s=t_L=2\epsilon_L^{-1}\log(1/\epsilon_L)$, these caps ensure $s+L\le2t_L$ for all sufficiently small temperatures, including every mobility below the selected threshold.

Define the persistence-window label to be $M_j$ on $E_{M_j}(a,L)$ and an additional symbol otherwise. Under the matching comparison its error from $\delta_{M_j}$ is at most $b$. The native learned label law is therefore within $(L+2)\delta+b$ of $\delta_M$, and the native frozen label law is within $\delta+16T+31TL+b$ of the equal matching mixture. Along the displayed scaling, their total-variation distance tends to $1/2$.

## 4. The contrast is also present in the one-time coherent partition

Let $\mathfrak P_b(X)$ be the partition into connected components of edges satisfying the existing stacked residual condition $\sqrt{(r^b)^2+(r^m)^2}\le b$. At a single time under $\nu_T^{M_j}$, the normal second moment is at most $T$, while each exterior residual has variance at least one. Hence

$$
\Pr_{\nu_T^{M_j}}(\mathfrak P_a\ne\mathfrak P_j)
\le e(T,a):=4T/a^2+4\sqrt{2/\pi}a.
$$

The learned partition law is within $\delta+e$ of its matching partition. At any time when the frozen one-time tracking error is also at most $\delta$, its partition law is within $\delta+16T+e$ of the equal mixture of the two distinct matching partitions. Therefore

$$
\boxed{\left|\operatorname{TV}(q_t^{\rm learn}\mathfrak P_a,q_t^{\rm frozen}\mathfrak P_a)-\tfrac12\right|\le2\delta+16T+2e(T,a).}
$$

This uniform one-time partition statement follows throughout the selected window. It is stronger than an assignment-label comparison and remains a late-window statement.

## 5. R15 classification and the unresolved first-formation question

On the native event just proved, the attended normal restoring rates are $8+T$ and $4+5T$. At Euclidean stacked resolution $a$ the least restoring ratio is at least $4a^2/T\to\infty$. The restoring clause is thus checked on a high-probability event of the actual sheet process, not solely on a manually held sheet.

If the learned rows at the start also satisfy $\max_i|p_i-p_i^M|\le\delta$, the corresponding frozen invariant law has

$$
\operatorname{TV}(\mu_{T,p},\nu_T^M)=1-\mu_{T,p}(M)\le4\delta.
$$

Apply the same actual-proposal occupation bound to that stationary process, whose rows are held at those learned values. Its probability of $E_M(a,L)$ is at least $1-4(L+2)\delta-b(T,a,L)$, which also tends to one. The persistence event is already typical at equilibrium for the learned rows. This supplies no first entrance from an initially incoherent state and no excess over the stationary event probability for those parameters. Under R15 it is restored equilibrium coherence, not first formation. The comparison with frozen *uniform* rows nevertheless records a real late coherent-partition difference; it does not convert that difference into a first-formation result.

The prior P-15 record warned that stationary coherence and recurrence cannot be interpreted as formation without the restoring and horizon clauses. Its capacity-to-transit hypothesis is not needed here. The original first-block problem additionally concerns the first qualifying block on its original horizon and a conditioning event of probability bounded below. None of the late-window estimates establishes that target. The independent early-time comparison belongs to a separate assigned artifact; this note does not infer its conclusion from equilibrium behavior.

No parent activation, conditional discarded free-energy bound, or inherited-parent path law is asserted. Those are Item 3, after publication of Item 2.

## Executed work and checkable artifact

This work read the sources named above and wrote only this report and the assigned manuscript section `Theory/ca_selected_coherence.tex`. The proof reconstructed the normal-coordinate rates and the matching/cycle average identity from the displayed residual covectors and multiplicities. It used the exact Stage 1 determinant bounds, rather than a new numerical experiment, for $16T$ and $31T$. No simulation, symbolic program, GPU computation, Lean work, tamper check, or broad test suite was run. The parent is responsible for the manuscript's label and compilation checks after integration.

The strongest supported result is a growing following persistence window $T^{-1/4}$ for the selected coherent partition at Euclidean stacked resolution $T^{1/4}$, with actual proposals controlled and a learned/frozen coherent-partition total-variation contrast tending to $1/2$. Its scope is the existing implicit joint schedule and a late selection window. The next action that would change the first-formation answer is a comparison of first-event path functionals on the original formation horizon, with their conditioning probabilities controlled.

