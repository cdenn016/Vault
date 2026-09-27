# Stage 1: explicit temperature bounds for the unchanged four-cycle

September 26, 2026. This note reconstructs the temperature dependence needed to continue the fixed-temperature selection proof. It establishes one-time entropy contraction, actual-law tracking, and quantitative initial-layer estimates. It does not infer pairing selection from tracking or assert a temperature-uniform lower bound on the matching imprint.

The supplied model and existing proof are in `Theory/ca_selection_proofs.tex`, especially “Entropy contraction at frozen rows” and “Tracking, escape, and selection.” The earlier calculation is `docs/derivations/2026-09-11-meta-agent-formation-frontier-and-locality/evidence/2026-09-24-p11-adiabatic-selection/P11-dyn/P11-dyn-report.md`. The current scope is recorded in `docs/STATUS.md`. The live continuity sources `Research/manuscripts/pifb2/13_section.tex` and `09_section.tex` separate fixed-temperature selection from coherence, persistence, and parent autonomy. No new external reference is used here. The constant below is deliberately weaker than the earlier interval-based numerical constant; its elementary bounds are displayed in full.

## 1. Target and model

For every temperature $0<T\le 1/100$, every interior product prior $p\in(0,1)^4$, and every probability density relative to the frozen invariant law, obtain an explicit entropy-production inequality. Then apply it to the actual coupled law with source-learning mobility $\epsilon>0$, initial rows $p(0)=\mathbf 1/2$, and initial law $\mathcal N(m,I_{12})$ times uniform assignments. For the joint-limit statements, $T$ and $\epsilon$ both tend to zero and the initial means remain in a fixed bounded set. The intended comparison is total variation of one-time laws, uniformly on specified time intervals. No path-law or conditioned-history equivalence is claimed.

The state is $(X,\sigma)\in\mathbb R^{12}\times\{\pm1\}^4$ at a single base point. A shared scalar link belongs to each undirected edge. Put $\Omega=I+R_{\rm ev}$, $A_\sigma=H_\sigma+T\Omega$, and $B_\sigma=A_\sigma/T$. Between rings of a rate-one clock,

$$
dX_t=-A_{\sigma_t}X_tdt+\sqrt{2T}dW_t.
$$

At a ring the complete assignment is redrawn from its conditional Gibbs law. The clock redraws the entire assignment, not one receiver at a time. The deterministic rows satisfy

$$
\dot p_i=\epsilon\{q_t(\sigma_i=+1)-p_i\}.
$$

There is no boundary on the continuous state. The initial law is smooth and has finite entropy, and the positive-temperature coupled dynamics is the globally well-posed system of the existing proof. Its finite-horizon entropy identity is already established there. In particular, no new regularity assumption is introduced in this note. Rows remain interior at every finite time and

$$
p_{\min}(t):=\min_i\{p_i(t),1-p_i(t)\}\ge\tfrac12e^{-\epsilon t},
\qquad
\|p(t)-\mathbf1/2\|_\infty\le\epsilon t/2.
$$

The invariant density at frozen rows is

$$
\mu_p(x,\sigma)=\frac{\pi_\sigma(p)}{(2\pi)^6 Z(p)}
\exp(-x^TB_\sigma x/2),
\qquad
\pi_\sigma(p)=\prod_i p_i^{1_{\{\sigma_i=+1\}}}(1-p_i)^{1_{\{\sigma_i=-1\}}}.
$$

All further restrictions, such as a bounded mean, a specified joint scale, or an imprint lower bound, are stated as additional assumptions rather than attributes of the supplied model.

## 2. An exact seven-dimensional reduction for the entropy estimate

Let $D$ be the cyclic difference matrix and introduce orthogonal coordinates $u=(k+m)/\sqrt2$, $v=(k-m)/\sqrt2$, and $\omega$. For the edge-multiplicity matrix $C_\sigma=\operatorname{diag}(m_e(\sigma))$, with $0\le m_e\le2$, the held energy is

$$
V_\sigma=\tfrac12(Du-\sqrt2\omega)^TC_\sigma(Du-\sqrt2\omega)
          +\tfrac12(Dv)^TC_\sigma Dv.
$$

Set $R=[D,-\sqrt2 I]$. The common passive space is

$$
K=\ker R\oplus\ker D,
\qquad \dim K=4+1=5,
$$

and $N=K^\perp$ has dimension seven. Every $H_\sigma$ vanishes on $K$. The matrix $\Omega$ is the identity on $(u,\omega)$ and $5I$ on $v$, so it preserves $K$ and $N$. Thus the passive factor is an independent Ornstein–Uhlenbeck process with four drift rates $T$ and one rate $5T$. The active pair $(P_NX,\sigma)$ is autonomous because the jump probabilities depend only on the residuals and hence only on $P_NX$. This is an exact decomposition of this specific model, not a proposal to discard active variables in a parent construction.

The matrix $H_{\rm all}=R^TR\oplus D^TD$ has operator norm six: $RR^T=DD^T+2I$ has eigenvalues $2,4,4,6$, and $D^TD$ has eigenvalues $0,2,2,4$. Since $C_\sigma\preceq2I$,

$$
0\preceq H_\sigma\preceq2H_{\rm all},
\qquad \|H_\sigma\|\le12,
\qquad T I\preceq A_\sigma\preceq(12+5T)I\preceq13I.
$$

For $\xi=P_NX/\sqrt T$, the active diffusion has unit diffusion coefficient and drift $-A_\sigma|_N\xi$. Write $a_\sigma=A_\sigma|_N$ and $w_\sigma=\det(a_\sigma)^{-1/2}$. Its invariant law is

$$
\mu_p^N(\xi,\sigma)=\frac{\pi_\sigma(p)}{(2\pi)^{7/2}Z_N(p)}
\exp(-\xi^Ta_\sigma\xi/2),
\qquad Z_N=\sum_\sigma\pi_\sigma w_\sigma.
$$

The active and twelve-dimensional sheet weights differ by an assignment-independent factor, so they produce identical assignment marginals and identical $\nabla_p\log Z$.

The four active determinant classes, obtained by dividing the existing full determinants by $5T^5$, are

$$
\begin{aligned}
d_M&=5T^3(T+8)^2(5T+4)^2,\\
d_E&=T(T^3+16T^2+77T+112)(125T^3+200T^2+85T+8),\\
d_N&=T(T+4)(5T+2)(T^2+12T+28)(25T^2+30T+4),\\
d_C&=(T+2)(T+4)^2(T+6)(5T+2)^2(5T+4).
\end{aligned}
$$

For $0<T\le1/100$, their positive coefficients give the elementary bounds

$$
5120T^3\le d_M\le5262T^3,
\quad896T\le d_E\le1017T,
\quad896T\le d_N\le2175T,
\quad3072\le d_C<5120.
$$

For example, the two factors of $d_E/T$ are less than $113$ and $9$; the four factors of $d_N/T$ are less than $5,3,29,5$. The upper bound on $d_M/T^3$ follows from its value $4209544161/800000<5262$ at $T=1/100$. The exact value of $d_C$ there is $2644916750113761/800000000000<5120$. Monotonicity proves each bound on the whole interval. In particular, $w_M$ is the largest and $w_C$ the smallest sheet weight, and

$$
w_M\le\frac{T^{-3/2}}{\sqrt{5120}},
\qquad \frac{w_C}{w_M}\ge T^{3/2}.
$$

## 3. Explicit entropy contraction

Define the absolute constant

$$
K_0=210\sqrt{2\pi/5},
\qquad
c_* =\min\left\{\frac{2}{1+4K_0 e^{13/8}},\frac{1}{K_0e^{13/4}}\right\}>0.
$$

Its numerical value is approximately $1.6470952\times10^{-4}$; only the exact formula is used in the inequalities.

**Proposition 1.** For every $0<T\le1/100$, every $p\in(0,1)^4$, and every probability density $f$ with respect to the full frozen law $\mu_p$, its entropy production satisfies

$$
\mathcal D_p(f)\ge
\lambda_c(T,p)\operatorname{Ent}_{\mu_p}(f),
\qquad
\lambda_c(T,p)=\frac{c_*T^{5/2}}{4+3\log(1/T)+8\log(1/p_{\min})}.
$$

The inequality is understood on the entropy-production form domain; an infinite production makes it immediate. This is a lower bound, not an assertion that the optimal contraction rate has exponent $5/2$.

**Proof.** Work first in the seven active unit-diffusion coordinates. Write $q_\sigma=\mu_p^N(\sigma)$ and $\gamma_\sigma=\mathcal N(0,a_\sigma^{-1})$. For $u\ge0$ normalized by $\int u^2d\mu_p^N=1$, let $z_\sigma=(\gamma_\sigma u_\sigma^2)^{1/2}$. The Gaussian entropy and Poincaré inequalities, proved from the explicit Ornstein–Uhlenbeck kernel in the existing selection proof, apply because $a_\sigma\succeq TI$:

$$
\operatorname{Ent}_{\gamma_\sigma}(u_\sigma^2)\le\frac2T\gamma_\sigma|\nabla u_\sigma|^2,
\qquad
\operatorname{Var}_{\gamma_\sigma}(u_\sigma)\le\frac1T\gamma_\sigma|\nabla u_\sigma|^2.
$$

The entropy chain rule and its elementary finite-label estimate give

$$
\operatorname{Ent}_{\mu_p^N}(u^2)
\le\frac2T\mathcal E_c(u)+L_p\operatorname{Var}_{q}(z),
\qquad L_p=4+2\log(1/\min_\sigma q_\sigma).
$$

Here $\mathcal E_c=\sum_\sigma\int\mu_{p,\sigma}^N|\nabla u_\sigma|^2$ and $\mathcal E_j=\frac12\sum_{\sigma,\eta}\int\mu_{p,\sigma}^Nb_\eta(u_\sigma-u_\eta)^2$. To check the finite-label estimate directly, put $R_q=(\min q_\sigma)^{-1/2}$ and use

$$
z^2\log z^2-z^2+1\le2(1+\log R_q)(z-1)^2,
\quad0\le z\le R_q,
\qquad \sum q_\sigma(z_\sigma-1)^2\le2\operatorname{Var}_{q}(z).
$$

Choose the ball $B_{1/2}\subset\mathbb R^7$, whose volume is $\pi^3/840$. Let $m_\sigma$ be the uniform-ball mean of $u_\sigma$ and $m_*=\sum_\sigma\pi_\sigma m_\sigma$. The variance split is

$$
\operatorname{Var}_{q}(z)\le2\sum_\sigma q_\sigma(z_\sigma-m_\sigma)^2
  +2\sum_\sigma q_\sigma(m_\sigma-m_*)^2.
$$

The first sum is at most $B_T\mathcal E_c/T$, where

$$
B_T=\max_\sigma(1+\sqrt{X_\sigma})^2,
\qquad
X_\sigma=\left[\frac{(2\pi)^{7/2}w_\sigma e^{\|a_\sigma\|/8}}{|B_{1/2}|}-1\right]_+.
$$

This follows by subtracting the Gaussian mean, applying Cauchy–Schwarz to the ball/Gaussian density ratio, and using the Gaussian Poincaré inequality. The bound on the Gaussian-to-ball comparison is an upper bound on its chi-squared divergence, so no reverse absolute-continuity assumption is needed.

For the second sum, Jensen's inequality and detailed balance give

$$
\sum_\sigma q_\sigma(m_\sigma-m_*)^2
\le\frac{w_M}{Z_N|B_{1/2}|}\sum_{\sigma,\eta}\pi_\sigma\pi_\eta
\int_{B_{1/2}}(u_\sigma-u_\eta)^2
\le\frac{2(2\pi)^{7/2}w_Me^{13/4}}{|B_{1/2}|}\mathcal E_j.
$$

The last step uses, on this ball,

$$
\mu_{p,\sigma}^N b_\eta
\ge\frac{\pi_\sigma\pi_\eta e^{-13/4}}{(2\pi)^{7/2}Z_N}.
$$

Thus the normalizer cancels instead of creating an inverse-prior power. Since

$$
\frac{(2\pi)^{7/2}}{|B_{1/2}|\sqrt{5120}}=K_0,
$$

we have $B_T\le4K_0e^{13/8}T^{-3/2}$. Consequently

$$
\operatorname{Ent}_{\mu_p^N}(u^2)\le C_c\mathcal E_c+C_j\mathcal E_j,
$$

with

$$
C_c\le(2+8K_0e^{13/8})L_pT^{-5/2},
\qquad C_j\le4K_0e^{13/4}L_pT^{-5/2}.
$$

These displayed upper bounds only use $T\le1$ and $L_p\ge1$ when enlarging powers. For $u=\sqrt f$, the diffusion production is $4\mathcal E_c$, while the jump production is at least $4\mathcal E_j$ because $(a-b)(\log a-\log b)\ge4(\sqrt a-\sqrt b)^2$. This proves active entropy contraction with rate at least $c_*T^{5/2}/L_p$. The cutoff, positive-regularization, and form-domain extensions are exactly those of the existing entropy-contraction proof and apply to the present positive Gaussian sheets.

The assignment masses obey

$$
\min q_\sigma\ge p_{\min}^4w_C/w_M\ge p_{\min}^4T^{3/2}.
$$

Therefore $L_p\le4+3\log(1/T)+8\log(1/p_{\min})$.

Finally the passive five-dimensional Gaussian factor has entropy-production rate at least $2T$. The product entropy inequality follows by decomposing entropy over that factor and the active law; for the entropy of a marginal, the gradient of the square root of the integrated square is bounded by the integrated gradient norm, by Cauchy–Schwarz. Thus the full rate is at least the minimum of the active rate and $2T$. Since $c_*<1$, $T\le1$, and the displayed denominator is at least four, our stated rate is smaller than $2T$. This proves the full-state claim, not merely a marginal entropy estimate. ∎

## 4. Fitness and its central derivatives

Put $F_i(p)=\mu_p(\sigma_i=+1)$ and $g_i(p)=\partial_{p_i}\log Z(p)$. The exact identity is $F_i-p_i=p_i(1-p_i)g_i$.

**Proposition 2.** For all interior rows and $0<T\le1/100$,

$$
\|g(p)\|_1\le4/T.
$$

On the central cube $Q=[1/4,3/4]^4$, independently of temperature,

$$
\|g(p)-g(p')\|_1\le150\|p-p'\|_\infty,
\qquad g(\mathbf1/2)=0.
$$

**Proof.** A single receiver flip joins only classes $M$ and $E$, $N$ and $E$, or $C$ and $E$. This also follows immediately from the normalized evidence representation: matching corners have subset cardinalities zero and four, end paths one and three, and the two classes of cardinality-two vertices are $N$ and $C$. The determinant bounds in Section 2 give, for either direction of any such neighboring-weight ratio, a bound $1/T$. For $M$–$E$, the potentially large ratio is at most $\sqrt{1017/5120}/T<1/T$. For $N$–$E$, both ratios are less than two. For $E$–$C$, the potentially large ratio is at most $\sqrt{5120/896}/\sqrt T<3/\sqrt T\le1/T$.

Writing $Z=p_iZ_i^++(1-p_i)Z_i^-$, each $Z_i^\pm$ is a positive sum with identical other-row coefficients, so $Z_i^+/Z_i^-$ lies between the smallest and largest neighboring-sheet ratios. It follows that $|g_i|\le1/T$.

For the central derivative bound, $|g_i|\le1/\min(p_i,1-p_i)\le4$. Multilinearity gives $\partial_i g_i=-g_i^2$, hence $|\partial_i g_i|\le16$. If $i\ne j$, direct differentiation of the assignment marginal yields

$$
\partial_jF_i=\frac{\operatorname{Cov}_{\mu_p}(1_{\{\sigma_i=+1\}},1_{\{\sigma_j=+1\}})}{p_j(1-p_j)},
\qquad |\partial_jg_i|\le\frac{1/4}{p_i(1-p_i)p_j(1-p_j)}\le\frac{64}{9}.
$$

Integrating along the line segment in the convex cube gives the constant $4\cdot16+12\cdot64/9=448/3<150$. The uniform-prior value vanishes by reflection symmetry. ∎

Uniform bounds on any fixed order of local reduced-field derivatives also follow directly on this cube. Normalize $w_M=1$. All vertex weights lie in $(0,1]$ and the two matching monomials imply $Z\ge2(1/4)^4=1/128$, while each derivative of its finite multilinear polynomial is uniformly bounded. This observation does not supply a temperature-uniform nonzero initial imprint.

## 5. Initial entropy and global actual-law tracking

For the initial mean $m\in\mathbb R^{12}$, direct integration gives

$$
H_0:=\operatorname{KL}(q_0\|\mu_{1/2})
=\log Z(1/2)-6+\frac1{32}\sum_\sigma\{\operatorname{tr}B_\sigma+m^TB_\sigma m\}.
$$

Because $B_\sigma\succeq I$, all full-state sheet weights are at most one and $Z\le1$. Also $B_\sigma\preceq13I/T$. Hence

$$
0\le H_0\le\overline H(T,m):=\frac{13(12+|m|^2)}{2T}.
$$

Let $H(t)=\operatorname{KL}(q_t\|\mu_{p(t)})$ and $h(t)=\sqrt{H(t)/2}$. The already established entropy identity, using the learning equation, gives exactly

$$
H'=-\mathcal D_p(f)-\epsilon\sum_i g_i(p)\Delta_i
-\epsilon\sum_i\frac{\Delta_i^2}{p_i(1-p_i)},
\qquad \Delta_i=q_t(\sigma_i=+1)-F_i(p).
$$

The last term is nonpositive. Pinsker's inequality and Proposition 1 therefore give, with $\Lambda(t)=\int_0^t\lambda_c(T,p(s))ds$,

$$
h(t)\le e^{-\Lambda(t)/2}\sqrt{H_0/2}
+\frac\epsilon4\int_0^te^{-(\Lambda(t)-\Lambda(s))/2}\|g(p(s))\|_1ds.
$$

Fix a constant $C>0$, define $t_L=C\epsilon^{-1}\log(1/\epsilon)$ for $0<\epsilon<1$, and put

$$
D_{T,\epsilon,C}=4+3\log(1/T)+8\log2+16C\log(1/\epsilon),
\qquad \ell=\frac{c_*T^{5/2}}{D_{T,\epsilon,C}}.
$$

On $0\le t\le2t_L$, the row lower bound gives $\lambda_c(T,p(t))\ge\ell$. Thus

$$
\boxed{\quad
\operatorname{TV}(q_t,\mu_{p(t)})\le h(t)
\le e^{-\ell t/2}\sqrt{\overline H(T,m)/2}
+\frac{2\epsilon D_{T,\epsilon,C}}{c_*T^{7/2}}.
\quad}
$$

This bound compares the actual recognition law with its instantaneous frozen invariant law. It does not replace the actual law in the learning equation.

**Joint-limit corollary.** If $T\to0$, $\epsilon\to0$, $|m|\le M$, and

$$
\epsilon T^{-7/2}D_{T,\epsilon,C}\longrightarrow0,
$$

then $\sup_{t_L\le t\le2t_L}\operatorname{TV}(q_t,\mu_{p(t)})\to0$.

To check the initial term, write $r=\epsilon D_{T,\epsilon,C}/T^{7/2}\to0$. Then $\ell t_L=(c_*C/(rT))\log(1/\epsilon)$, which dominates $\log(1/T)$, whereas $\log\overline H=O(1)+\log(1/T)$ for bounded means. This proves uniform decay of that term. A simple explicit sufficient family is $\epsilon=T^a$ with any fixed $a>7/2$, equivalently $T=\epsilon^b$ with $0<b<2/7$. These exponents certify one-time tracking only. In particular, the earlier prescribed scaling $T=\epsilon^8$ does not satisfy this sufficient condition; failure of a sufficient condition does not refute that scaling.

## 6. Quantitative initial imprint and refined central tracking

Define the frozen uniform-row imprint

$$
I_i(T,m)=\int_0^\infty\{q_s^0(\sigma_i=+1)-1/2\}ds,
\qquad j(T,m)=(1,-1,1,-1)\cdot I(T,m).
$$

Set

$$
\lambda_Q=\frac{c_*T^{5/2}}{4+3\log(1/T)+8\log4},
\quad A=\sqrt{\overline H(T,m)/2},
\quad B=\frac{2A}{\lambda_Q},
\quad L=150.
$$

Uniform rows belong to $Q$, so frozen contraction proves absolute convergence and $\|I(T,m)\|_\infty\le B$. For bounded means, $B=O(T^{-3}[1+\log(1/T)])$.

For any initial-layer duration $\tau>0$ with $\epsilon\tau\le1/10$, the actual rows stay in $[0.45,0.55]^4$. A coupling of common clocks and Gaussian noise, up to the first distinct assignment redraw, gives

$$
\|q_s^\epsilon-q_s^0\|_{\rm TV}
\le\frac{\epsilon s^2}{2c_0},\qquad c_0=0.45,\quad0\le s\le\tau.
$$

Indeed, while assignments and configurations coincide, each posterior receiver probability is Lipschitz in its prior with derivative at most $1/(2c_0)$. Summing four rows, integrating the mismatch intensity, and using $\|p(r)-1/2\|_\infty\le\epsilon r/2$ proves the bound. Variation of constants in the learning equation then yields the fully quantitative estimate

$$
\boxed{\quad
\left\|\frac{p(\tau)-\mathbf1/2}{\epsilon}-I(T,m)\right\|_\infty
\le B e^{-\lambda_Q\tau/2}+\epsilon\tau B+\frac{\epsilon\tau^3}{6c_0}.
\quad}
$$

The three terms are, respectively, the frozen tail after $\tau$, the exponential-learning-kernel error on the frozen bias, and the common-clock coupling error. This derivation needs no frozen Harris constant whose temperature dependence is unknown.

On the same layer, Proposition 2 gives $\|g(p(s))\|_1\le L\epsilon s/2$. Integrating the entropy comparison gives

$$
\boxed{\quad
h(\tau)\le A e^{-\lambda_Q\tau/2}+\frac{L\epsilon^2\tau}{4\lambda_Q}.
\quad}
$$

If the rows stay in $Q$ throughout $[\tau,t]$, integrating with the local Lipschitz bound and $|\dot p_i|\le\epsilon$ gives

$$
h(t)\le e^{-\lambda_Q(t-\tau)/2}h(\tau)
+\frac{\epsilon}{2\lambda_Q}\|g(p(t))\|_1
+\frac{L\epsilon^2}{\lambda_Q^2}.
$$

Since $|\Delta|_2\le2h$ and $g(1/2)=0$, the resulting relative-plus-absolute perturbation bound is

$$
\boxed{\quad
|\Delta(t)|_2\le\frac{L\epsilon}{\lambda_Q}|p(t)-\mathbf1/2|_2
+2e^{-\lambda_Q(t-\tau)/2}h(\tau)
+\frac{2L\epsilon^2}{\lambda_Q^2}.
\quad}
$$

This supplies the actual temperature dependence of the perturbation entering the saddle calculation. The estimate is valid until exit from the central cube and makes no claim about the sign of the matching component.

For example, suppose an additional lower bound $|j(T,m)|\ge j_*(T)>0$ is supplied. A sufficient set of conditions for the imprint approximation error to be $o(j_*)$ and the absolute central perturbation to be $o(\epsilon j_*)$ is

$$
\epsilon\tau\le1/10,
\quad\frac{B e^{-\lambda_Q\tau/2}+\epsilon\tau B+\epsilon\tau^3}{j_*}\to0,
\quad\frac{A e^{-\lambda_Q\tau/2}}{\epsilon j_*}\to0,
\quad\frac{\epsilon\tau}{\lambda_Qj_*}\to0,
\quad\frac{\epsilon}{\lambda_Q^2j_*}\to0,
\quad\frac\epsilon{\lambda_Q}\to0.
$$

These explicit conditions are stronger than global tracking. They are sufficient input estimates for a subsequent quantitative saddle argument, not a theorem that such an imprint floor holds. With a logarithmic mixing layer $\tau\asymp\lambda_Q^{-1}\log(1/\epsilon)$, the crude coupling contribution $\epsilon\tau^3$ carries $\epsilon T^{-15/2}$ times logarithmic factors. This identifies where the existing initial-layer proof loses powers of temperature.

## 7. Scope, checks, and remaining obligation

The analytic result is an explicit, polynomial-temperature, logarithmically prior-dependent entropy contraction inequality and its actual-law consequences. It certifies a nonempty joint regime for one-time tracking, for example $\epsilon=T^a$ with $a>7/2$, uniformly over bounded initial means on the logarithmic selection window. The central derivatives are uniform in temperature, while the explicit initial-layer bounds expose the stronger constraints needed to preserve an imprint.

The existing theorem proves $j(T,\cdot)$ is nonzero analytic at each fixed positive $T$. It does not prove $\inf_{0<T<T_0}|j(T,m)|>0$, a polynomial lower envelope for fixed $m$, or a temperature-uniform ratio of the transverse imprint to the matching imprint. A quantitative selection theorem still needs either such estimates or a rigorously stated diagonal construction that avoids asserting a power law. Tracking alone supplies none of them. No claim about coherence, persistence, activation conditioning, or parent path laws is made here.

The only new executed computation was a CPU-only standard-library `Fraction` calculation under `C:/Python314/python.exe`. It evaluated $d_C(1/100)=2644916750113761/800000000000$ and $d_M(1/100)/(1/100)^3=4209544161/800000$ exactly, and printed a floating-point evaluation of $K_0$ and $c_*$. Those exact fractions are reproduced in Section 2 and prove the two endpoint comparisons by integer arithmetic; the decimal value of $c_*$ is illustrative. The determinant formulas themselves were read from, and their active-space reduction checked against, the existing proof. No scientific simulation, GPU computation, Lean proof, tamper check, or broad test suite ran for this note.

The next mathematical action that changes the selection answer is to combine these explicit bounds with quantitative control of the moving-temperature imprint, or to state and prove a narrower diagonal theorem with its quantifiers intact.

