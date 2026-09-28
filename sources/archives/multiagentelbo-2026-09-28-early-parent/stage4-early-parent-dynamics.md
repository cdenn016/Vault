# Stage 4, obligations 2 and 3: parent path coupling after the seeded early first-contrast prefix

Date: September 28, 2026. Author model: Claude Opus 5.5 (`claude-opus-5-5`). Verifier: Claude Fable 5.1 (`claude-fable-5-1`), verdict VALID_WITH_MINOR_ISSUES with no critical or major defect, recorded in `stage4-crossmodel-parent-dynamics.md`. The fixes listed there (D1 to D5) were applied afterwards by Claude Opus 5.5 and have not been re-verified. Scope: fixed base point $c_*$, no base transport, no Lean, no tamper or integrity work, and no edit of the Research vault, which was read only. This note covers obligation 2, the parent path coupling on the window after activation, and obligation 3, the mobility question, of the item-4 continuation. Obligation 1, the event-specific hidden-information bound at activation, has its own record, `stage4-seeded-hidden-information.md`, by a separate worker; it is neither assumed nor reproved here.

Sources read: `c14_interpretation.tex` (`prop:phil-seeded-contrast-formation`), `c13_formation.tex` (`def:rg-formation-cycle-experiment`, `prop:rg-formation-endogenous-cycle`, `open:rg-formation-adaptive-family`), `ca_formation_proofs.tex` (proofs of both propositions, in particular the paragraphs *Episode*, *Parent channel*, *Parent dynamics*, *Rows*, *Seed events*, *The other seeds*), `ca_parent_conditional.tex`, `ca_parent_dynamics.tex`, `ca_first_block_comparison.tex`, `SPEC.md` (R13 to R16), and in this folder `STAGE3.md`, `stage3-verification.md`, `stage3-parent-dynamics.md`, and `stage2-first-block-comparison.md`.

**Verdict.** The coupling holds at the original mobility $\epsilon_L=\epsilon=T^{1/8}$ and at every mobility $\epsilon_L\in[0,1]$; no slow schedule is needed. Activate the own-law parent at a deterministic time $\theta\in[1/4,t^\circ_*]$, which contains the assigned range $[t_\epsilon,t^\circ_*]$, from $C_\#\mathrm{Law}(X_\theta,S_\theta\mid E_\theta)$ with rows $p(\theta)$. For every window $h>0$ with $T(\theta+h)\le1/10$, the complete retained configuration/assignment path law of this parent on $[0,h]$ is within total variation

$$
\min\{73728 \epsilon^4h, 24\exp[-1/(76800 Th)]\}
+4\bigl(1+\sqrt{8/3}\bigr)\bigl(2e^{\epsilon_L(\theta+h)}-1\bigr)h e^{-1/T}
$$

of the native retained path conditioned on $E_\theta$. Here $E_\theta$ is the seeded sub-event of `prop:phil-seeded-contrast-formation`(b), the event on which part (d) of the source activates; it is not the contrast-formation event $E_T$ or the first-block mark $K_T$ on which `open:rg-formation-adaptive-family` conditions (Section 12). The bound is uniform in the Gaussian mean $m_0$, and neither the seeded floor $c(m_0)$ nor any other prefix probability enters it. It tends to zero for every window with $Th\to0$, for example $h=T^{-1+\gamma}$ with $\gamma\in(0,1)$, and faster than any power of $T$ in that case. Item 3's route through the stationary held-matching path law fails here for two quantified reasons (Section 3). The mobility enters only as the factor $2e^{\epsilon_L(\theta+h)}-1$, multiplied by $e^{-1/T}$.

## 1. Model, quantifiers, and assumptions

Fix $\epsilon\in(0,1/100]$ and put

$$
T=\epsilon^8,\quad t_\epsilon=2\log(1/\epsilon),\quad t^\circ_*=t_\epsilon+1,\quad \varrho_\circ=1/100,\quad x^\circ=(0,0,\mathbf 1_4),\quad \delta_\epsilon=\epsilon^2/(8\sqrt3),
$$

as in `eq:rg-formation-cycle-regime` and the proof of `prop:rg-formation-endogenous-cycle`. The state is $(X,S)\in\mathbb R^{12}\times\mathcal J$, with $\mathcal J=\prod_i\{i-1,i+1\}$ of size sixteen. On sheet $S$ the configuration solves

$$
dX_t=-K_SX_t dt+\sqrt{2T} dW_t,\qquad K_S=H_S+T(I+R_{\rm ev}),\qquad R_{\rm ev}=2\mathfrak D^\top\mathfrak D,
$$

where $H_S$ is the Hessian of $V_S=\sum_i\mathcal D_{e(i,S_i)}$ and $W$ is a standard Brownian motion on $\mathbb R^{12}$; $K_S$ is the matrix $\mathsf A_S$ of `prop:phil-actual-parent-dynamics`. A rate-one Poisson clock rings at $\tau_1<\tau_2<\cdots$. At ring $k$, independent uniforms $U_{k,0},\dots,U_{k,3}$ redraw the complete assignment: receiver $i$ takes source $i+1$ exactly when $U_{k,i}\le\beta_{i,i+1}(X_{\tau_k-};p_i(\tau_k))$, where

$$
\beta_{ij}(x;p_i)=\frac{\pi_{ij}e^{-\mathcal D_{e(i,j)}(x)/T}}{\sum_{j'=i\pm1}\pi_{ij'}e^{-\mathcal D_{e(i,j')}(x)/T}},\qquad \pi_{i,i+1}=p_i,\quad \pi_{i,i-1}=1-p_i .
$$

The product of these rows is $b_p(S'\mid x)$. Self-proposals are allowed and never move $X$. The rows start at $1/2$ and follow $\dot p_i=\epsilon_L (q_t(S_i=i+1)-p_i)$, where $q_t$ is the unconditioned law of $(X_t,S_t)$. The initial law is $\mathcal N(m_0,I_{12})\otimes\mathrm{Unif}(\mathcal J)$, independent of $W$, the clock, and the uniforms. Time is continuous. There is no discretization and no implementation; every statement concerns this continuous-time model. Native rows exist uniquely for every $\epsilon_L\ge0$, by the fixed-point argument in the proof of `prop:phil-seeded-contrast-formation`(a), which uses the mobility only as a positive constant.

Let $\mathcal F_t$ be generated by $(X_0,S_0)$, by $W$ and the clock on $[0,t]$, and by the uniforms of rings in $[0,t]$. Given $\mathcal F_\theta$, the future after the deterministic time $\theta$ is a measurable function of $(X_\theta,S_\theta)$, the deterministic row path, and the driving inputs after $\theta$, which are independent of $\mathcal F_\theta$.

**Seeds and prefix.** The notation follows the obligation-1 record. For a matching $M\in\{S^{(0)},S^{(1)}\}$ and $\sigma\in\{1,-1\}$, put

$$
Z^M_t=\sqrt{2T}\int_0^te^{-K_M(t-v)}dW_v,\qquad
B_{\sigma,M}=\{|X_0-\sigma x^\circ|<\varrho_\circ, S_0=M,\text{ no ring in }[0,1/4]\},
$$

$$
A^M_t=\{\sup_{v\le t}|Z^M_v|\le\delta_\epsilon\}\cap\{S_v=M\text{ for all }v\le t\},\qquad
E_\theta=\bigsqcup_{\sigma,M}\bigl(B_{\sigma,M}\cap A^M_\theta\bigr)\in\mathcal F_\theta .
$$

On $B_{\sigma,M}$, the event $\{S_v=M, v\le\theta\}$ is the same as the source's requirement that every proposal in $[1/4,\theta]$ return $M$. The four seeds are disjoint. The held center path of seed $(\sigma,M)$ is $\bar x^{\sigma,M}(t)=\sigma e^{-K_Mt}x^\circ$.

**Channel and parent.** The channel is $C(x,S)=(S,P_{W_S}x)$, with $W_M=Z_M^\perp$ on the matchings and $W_S=\mathbb R^{12}$ otherwise. It takes values in the disjoint union $\mathcal Y=\bigsqcup_S\{S\}\times W_S$. The parent is exactly the type-(b) parent of `prop:phil-actual-parent-dynamics`, with a different activation:

$$
\mu_{\rm act}=C_\#q^E_\theta,\qquad q^E_\theta=\mathrm{Law}(X_\theta,S_\theta\mid E_\theta),\qquad p^C(0)=p(\theta).
$$

On stratum $S$ the parent's continuous generator is $-K_Sy\cdot\nabla_{W_S}+T\Delta_{W_S}$. Its rate-one proposal kernel is `eq:phil-actual-parent-kernel`,

$$
J_p((S,y),\cdot)=\int\kappa_S(dx\mid y)\sum_{S'}b_p(S'\mid x) \delta_{(S',P_{W_{S'}}x)},
$$

where $\kappa_M(\cdot\mid y)$ is the law of $y+F_Mz$ with $z\sim\mathcal N(0,TK_Z^{-1})$ and $K_Z=\mathrm{diag}(8+T,4+5T,4+5T)$, and $\kappa_S$ is the point mass at $y$ off the matchings. The parent's rows follow `eq:phil-actual-parent-learning`, $\frac{d}{du}p^C_i=\epsilon_L(q^C_u(S_i=i+1)-p^C_i)$, where $q^C_u$ is the parent's own one-time law.

**Compared laws.** $\mathsf P^{\rm fine}_{\theta,h}$ is the law of $(C(X_{\theta+u},S_{\theta+u}))_{0\le u\le h}$ conditioned on $E_\theta$ only, with the native rows continuing on their own deterministic path. $\mathsf P^C_h$ is the parent path law on $[0,h]$. Both are laws on the Skorokhod space $D([0,h];\mathcal Y)$. The comparison is total variation of complete retained paths: all nine or twelve retained coordinates, the complete assignment path, and hence the loop coordinate $\sum_i\omega_i$, whose covector annihilates $Z_M$.

**Assumption ledger.** The orchestrator task supplied the regime ($\epsilon\le1/100$, $T=\epsilon^8$, initial law, learned product rows), the deterministic activation time $\theta\in[t_\epsilon,t^\circ_*]$, the prefix $E_\theta$ as a union over four seeds, the parent (activation law, kernel, own-law rows), and the target comparison. This note introduces the following. The mobility range is $\epsilon_L\in[0,1]$, which contains the original $\epsilon_L=\epsilon$ and every slow schedule. The activation range is enlarged to $\theta\in[1/4,t^\circ_*]$. There are two tube radii ($\delta_\epsilon$ and $1/20$). The window restriction $T(\theta+h)\le1/10$ keeps the exterior-residual drift controlled. No assumption about the native hidden coordinates, the Stage 1 selection tolerances, or a stationary reference is used.

## 2. Statement

**Theorem S4.1 (early seeded parent path coupling).** Let $\epsilon\in(0,1/100]$, $T=\epsilon^8$, $\epsilon_L\in[0,1]$, $m_0\in\mathbb R^{12}$, $\theta\in[1/4,t^\circ_*]$, and $h>0$ with $T(\theta+h)\le1/10$. Put $\Lambda(t)=2e^{\epsilon_Lt}-1$.

(a) *Prefix.* $P(E_\theta)\ge(1-\tilde p) \frac{e^{-1/4}}8\sum_\pm\mathcal N(m_0,I_{12})\{|x\mp x^\circ|<\varrho_\circ\}>0$, where $\tilde p=73728 \epsilon^4t^\circ_*+4\Lambda(t^\circ_*) t^\circ_*e^{-1/T}<0.008+10^{-14}$. For $\epsilon_L\le\epsilon$, $\tilde p$ is at most the source constant $\tilde p_\epsilon=73728 \epsilon^4t^\circ_*+5t^\circ_*e^{-1/T}$. The law $q^E_\theta$ is carried by the bounded set $\mathcal T_\theta=\bigcup_{\sigma,M}\{(x,M):|x-\bar x^{\sigma,M}(\theta)|\le\varrho_\circ+\delta_\epsilon\}$.

(b) *Parent.* The own-law parent from $(\mu_{\rm act},p(\theta))$ exists and is unique on $[0,\infty)$. Its rows satisfy $p^C_i(u)\in[e^{-\epsilon_L(\theta+u)}/2, 1-e^{-\epsilon_L(\theta+u)}/2]$.

(c) *Path coupling.*

$$
\mathrm{TV}\bigl(\mathsf P^{\rm fine}_{\theta,h},\mathsf P^C_h\bigr)
\le\min\bigl\{73728 \epsilon^4h+\mathcal H(1.60), 24e^{-1/(76800 Th)}+\mathcal H(1.39)\bigr\},
\qquad
\mathcal H(g)=4\bigl(1+\sqrt{8/3}\bigr)\Lambda(\theta+h) h e^{-g/T}.
$$

Since $\mathcal H$ decreases in $g$, this implies the weaker but simpler bound $\min\{73728 \epsilon^4h, 24e^{-1/(76800 Th)}\}+\mathcal H(1.39)$, and a fortiori the form with $\mathcal H(1)$ displayed in the verdict above. The right side does not depend on $m_0$, on $P(E_\theta)$, or on $c(m_0)$.

**Corollary S4.2 (windows and mobility).** Under the hypotheses of the theorem, $4(1+\sqrt{8/3})\Lambda(\theta+h)\le21.1 e^{1/(10T)}$, so

$$
\mathrm{TV}\le\min\bigl\{73728 T^{1/2}h, 24e^{-1/(76800 Th)}\bigr\}+21.1 h e^{-9/(10T)} .
$$

(i) With the $\epsilon^2$ Chebyshev tube alone, the error vanishes whenever $T^{1/2}h\to0$, that is for $h=o(T^{-1/2})$.

(ii) With the order-one tube, take $h=T^{-1+\gamma}$ with $\gamma\in(0,1)$. For $\epsilon$ small enough that $T^\gamma+Tt^\circ_*\le1/10$, $\mathrm{TV}\le24\exp(-T^{-\gamma}/76800)+21.1 T^{-1+\gamma}e^{-9/(10T)}$, which tends to zero faster than every power of $T$.

(iii) The convergence is uniform in $\theta\in[1/4,t^\circ_*]$, $\epsilon_L\in[0,1]$, and $m_0$. It includes the original mobility $\epsilon_L=T^{1/8}$ and every slow schedule.

(iv) If $Th$ does not tend to zero, the bound does not tend to zero, and the method gives no conclusion for windows of order $1/T$ or longer.

The proof occupies Sections 4 to 10. Section 3 explains why item 3's argument cannot be reused.

## 3. Why item 3's stationary comparison fails here (requirement i)

`prop:phil-actual-parent-dynamics` bounds the path error by the triangle inequality through $\mathsf O^C$. That law is the stationary held-$M$ projected Ornstein–Uhlenbeck path law, with time-zero law $\bar\nu^M_T\otimes\delta_M$ and $\bar\nu^M_T=(P_{W_M})_\#\mathcal N(0,TK_M^{-1})$. The proof has two inputs: $\mathrm{TV}(q^C_0,\bar\nu^M_T\otimes\delta_M)\le\rho+\delta$, and the averaged hazard $\int k_p d\bar\nu^M_T\le(1-\mu_{T,p}(M))/\mu_{T,p}(M)\le4d/(1-4d)$, where $d<1/4$ bounds every row's nonpartner mass. Both inputs fail on the early window.

*The row hypothesis and the flux bound.* By Lemma S4.4 below, every native row entry lies in $[e^{-\epsilon_Lt}/2,1-e^{-\epsilon_Lt}/2]$. For $\epsilon_L\le\epsilon$ and $t\le t^\circ_*$, every nonpartner mass is at least $0.4489>1/4$, so the hypothesis $d<1/4$ is false. The optimizer sheet weights are $\mu_{T,p}(S)=\pi_S(p)w_S/\sum_{S'}\pi_{S'}(p)w_{S'}$, with $w_S=\int e^{-U_S/T}dx\propto\det(K_S)^{-1/2}$. The two matchings have $\det K_{S^{(0)}}=\det K_{S^{(1)}}$, by the rotation $i\mapsto i+1$; this was also checked exactly (Section 13). Hence

$$
\mu_{T,p}(M)\le\frac{\pi_M(p)}{\pi_M(p)+\pi_{M'}(p)}=\Bigl(1+\prod_i\frac{p_{i,M'_i}}{p_{i,M_i}}\Bigr)^{-1}<\frac{1.23^4}{1+1.23^4}<0.696,
$$

because every ratio of the two entries of a row is below $1.23$ on $[0,t^\circ_*]$ when $\epsilon_L\le\epsilon$. Thus $(1-\mu)/\mu>1.23^{-4}>0.4369$. The item-3 averaged departure bound over $[0,h]$ is then at least $0.4369h$, and it exceeds one once $h>2.29$. At uniform rows (the frozen arm, or $t=0$), $\mu_{T,1/2}(M)=(2+\sum_{S\notin\{M,M'\}}w_S/w_M)^{-1}\le1/2$. The executed determinant computation gives $w_S/w_M\approx2.39 T$ for twelve nonmatching sheets and $\approx1.29 T^{3/2}$ for the two cyclic sheets, so $\mu_{T,1/2}(M)=1/2-O(T)$. The flux estimate is therefore of order one. Its size comes from the stationary mass of the other matching, which the estimate charges in full as potential departure flux; the actual stationary averaged hazard is neither needed nor computed here.

*The activation law is nearly singular to the stationary retained law.* By Lemma S4.3, $\mu_{\rm act}$ is carried by the set $G=\bigcup_{\sigma,M}\{M\}\times\{y\in W_M:|y-P_{W_M}\bar x^{\sigma,M}(\theta)|\le R_0\}$, where $R_0=\varrho_\circ+\delta_\epsilon\le0.010008$. Under $\mathcal N(0,TK_M^{-1})$ the eight slow coordinates, those of $\ker H_M\subset W_M$, are independent of the rest. Their covariance is $T [T(I+R_{\rm ev})|_{\ker H_M}]^{-1}=(I+R_{\rm ev}|_{\ker H_M})^{-1}$, whose eigenvalues are $1$ (six times) and $1/5$ (twice), because $R_{\rm ev}$ has eigenvalue $4$ with multiplicity two on $\ker H_M$ (exact check). The slow density is therefore at most $(2\pi)^{-4}\cdot5$, and the orthogonal projection of each ball in $G$ onto $\ker H_M$ is a ball of radius $R_0$. Summing over the two signs,

$$
(\bar\nu^M_T\otimes\delta_M)(G)\le2\cdot\frac{5}{(2\pi)^4}\cdot\frac{\pi^4R_0^8}{4!}=\frac{10}{384}R_0^8<3\times10^{-18},
\qquad
\mathrm{TV}(\mu_{\rm act},\bar\nu^M_T\otimes\delta_M)>1-3\times10^{-18},
$$

for either matching $M$, every $\theta$, $\epsilon\le1/100$, $\epsilon_L$, and $m_0$. The activation slow part sits within $R_0$ of $\pm e^{-T\theta}(x^\circ+n_c)$, at distance $\sqrt3 e^{-T\theta}$ from the origin. The stationary slow part has spread of order one around zero. Both $\mathsf P^{\rm fine}_{\theta,h}$ and $\mathsf P^C_h$ have time-zero law $\mu_{\rm act}$. Both legs of item 3's triangle inequality are therefore larger than $1-3\times10^{-18}$, and the route yields nothing.

The failure is structural, not a matter of constants. Early departures are rare because the exterior common residuals are near $3/2$ while the partner costs are thermal. A stationary average cannot see this, since under it the slow coordinates are centered at zero with order-one spread and the exterior residuals pass near zero with positive probability. A sharper stationary hazard estimate would not repair the activation mismatch. The direct coupling below uses the mechanism pointwise.

## 4. Matching-sector facts used

Take $M=S^{(0)}$, with selected edges $e=e_0$, $f=e_2$ and exterior edges $e_1,e_3$; the other matching and the negative seed follow by the signed-permutation symmetries in the paragraph *The other seeds* of the seeded proof, which preserve every magnitude below. Write $P_g=a^b_g+a^m_g$ and use the orthonormal vectors

$$
n_c=\tfrac14(P_e+P_f),\quad \hat z_1=\tfrac14(P_e-P_f),\quad \hat z_2=\tfrac12(a^b_e-a^m_e),\quad \hat z_3=\tfrac12(a^b_f-a^m_f),
$$

which equal $(n^+_e+n^+_f)/\sqrt2$, $(n^+_e-n^+_f)/\sqrt2$, $n^-_e$, $n^-_f$ in the notation of `eq:rg-formation-cycle-normals`. Put $z_+=n_c\cdot x$ and $z_k=\hat z_k\cdot x$, so $Z_M=\mathrm{span}(\hat z_1,\hat z_2,\hat z_3)$ and $W_M=\ker H_M\oplus\mathrm{span}(n_c)$. Every item below was verified in exact rational arithmetic (Section 13); items (F1), (F2), (F4) restate the source proof.

(F1) The four vectors span $\mathrm{range} H_M$, with $H_M$-eigenvalues $8,8,4,4$ and $R_{\rm ev}$-eigenvalues $0,0,4,4$. $R_{\rm ev}$ preserves $\ker H_M$, on which it has eigenvalue $4$ with multiplicity two and $0$ with multiplicity six. Hence $K_M$ preserves $\ker H_M$, $\mathrm{span}(n_c)$, and $Z_M$, with rates $T$ or $5T$, $8+T$, and $K_Z$, and it commutes with $P_{W_M}$.

(F2) $\mathcal D_e=(z_++z_1)^2+z_2^2$ and $\mathcal D_f=(z_+-z_1)^2+z_3^2$.

(F3) For an exterior edge $g$, $\mathcal D_g=c_g^2+d_g^2$, with $c_g(x)=\tfrac12P_g\cdot x$ and $d_g=\tfrac12(a^b_g-a^m_g)\cdot x$. The covector of $c_g$ has norm $\sqrt2$ and annihilates $Z_M$, so $c_g$ is a function of the retained coordinate. Moreover $c_g\cdot n_c=-1/2$.

(F4) $x^\circ+n_c\in\ker H_M\cap\ker R_{\rm ev}$, and $K_Mn_c=(8+T)n_c$. Hence $\bar x(t)=e^{-K_Mt}x^\circ=e^{-Tt}(x^\circ+n_c)-e^{-(8+T)t}n_c$, and $|x^\circ+n_c|^2=3$. Along $\bar x(t)$, every exterior residual satisfies $r^b_g=r^m_g=c_g=e^{-Tt}(-\tfrac32+\tfrac12e^{-8t})$. Also $z_+=-e^{-(8+T)t}$, $z_1=z_2=z_3=0$, and $|P_{\mathrm{range}H_M}\bar x(t)|=e^{-(8+T)t}$.

(F5) $\det K_{S^{(0)}}=\det K_{S^{(1)}}$.

For $x$ on the stratum of $M$, define

$$
c_M(x)=\min_{g\text{ exterior}}|c_g(x)|,\qquad \zeta_M(x)=|P_{\mathrm{range}H_M}x|,\qquad G_M(x)=c_M(x)^2-2\zeta_M(x)^2 .
$$

Both $c_M$ and $z_+$ depend only on $y=P_{W_M}x$. $c_M$ is $\sqrt2$-Lipschitz and $\zeta_M$ is $1$-Lipschitz.

## 5. Prefix localization; no conditional floor enters

**Lemma S4.3.** For $\theta\ge1/4$, on $B_{\sigma,M}\cap A^M_\theta$ one has $S_v=M$ for $v\le\theta$, $X_\theta=e^{-K_M\theta}X_0+Z^M_\theta$, and $|X_\theta-\bar x^{\sigma,M}(\theta)|\le R_0=\varrho_\circ+\delta_\epsilon$. Hence $q^E_\theta(\mathcal T_\theta)=1$. For $\theta\le t^\circ_*$ and $\epsilon_L\in[0,1]$, part (a) of the theorem holds.

*Proof.* On the seed there is no ring in $[0,1/4]$, and the assignment equals $M$ on $[0,\theta]$. A proposal of the current assignment does not move $X$, so $X$ solves the held linear equation throughout. Since $K_M\succeq TI$, $\|e^{-K_Mt}\|\le1$, and $|X_\theta-\sigma e^{-K_M\theta}x^\circ|\le|X_0-\sigma x^\circ|+|Z^M_\theta|\le\varrho_\circ+\delta_\epsilon$. For the probability bound, the *Episode* paragraph of the source proof shows the following on the seed and the tube: on $[1/4,t^\circ_*]$ each receiver's exterior cost exceeds its partner cost by more than one, and this uses $Tt^\circ_*<1/100$ but not the rows. Each departing receiver choice then has probability at most $\Lambda(t)e^{-1/T}$ (Lemma S4.4). The expected number of departing rings up to $t^\circ_*$ is at most $4\Lambda(t^\circ_*)t^\circ_*e^{-1/T}$, and Chebyshev's inequality bounds the tube failure by $73728 \epsilon^4t^\circ_*$. The symmetry argument of *The other seeds* transfers this to all four seeds, because the bound $\Lambda$ is invariant under relabeling. For $\epsilon_L\le1$, $\Lambda(t^\circ_*)\le2e \epsilon^{-2}$, and $4\Lambda t^\circ_*e^{-1/T}<10^{-14}$. The first term is below $0.008$ by the source's monotonicity bound. For $\epsilon_L\le\epsilon$, $\Lambda<1.23$ gives $4\Lambda<5$. Summing $P(B_{\sigma,M})=\frac{e^{-1/4}}{16}\mathcal N(m_0,I_{12})\{|x-\sigma x^\circ|<\varrho_\circ\}$ over the four disjoint seeds gives (a). $\square$

**Floor handling (requirement iv).** Two different floors appear in the sources. The seeded floor $c(m_0)\le P(E_\theta)$ is independent of $\epsilon$ but tiny, of order $10^{-31}$ at $m_0=0$. The per-seed prefix floor $P(A^M_\theta\mid B_{\sigma,M})\ge1-\tilde p$ is close to one. Part (d) of `prop:rg-formation-endogenous-cycle` divides tube failure by the second floor, because it uses the tube on all of $[0,t^\circ_*]$. The present proof divides by neither. After activation it uses only the future noise $Z'_u=\sqrt{2T}\int_0^ue^{-K_{M_0}(u-v)}dW'_v$, with $W'_v=W_{\theta+v}-W_\theta$. By Lemma S4.3 and $\bar x(\theta+u)=e^{-K_Mu}\bar x(\theta)$, the widened tube $|X_{\theta+u}-\bar x(\theta+u)|\le R_0+|Z'_u|$ holds up to the first departure. The process $W'$ is independent of $\mathcal F_\theta\ni E_\theta$, and the tube bounds of Lemma S4.9 hold for either matching. Hence $P(\sup_{u\le h}|Z'_u|>\delta'\mid\mathcal F_\theta)$ is bounded by the unconditional estimate on $E_\theta$. The smallness of $c(m_0)$ matters only for obligation 1 (`rem:phil-conditioned-hidden-sign`). The dynamical estimate never pays it.

## 6. Rows, and existence and uniqueness of the own-law parent (requirement vi)

**Lemma S4.4 (row ratios).** For every $\epsilon_L\ge0$ and $t\ge0$, every native row entry lies in $[e^{-\epsilon_Lt}/2,1-e^{-\epsilon_Lt}/2]$. Every solution of the parent row equation satisfies

$$
p^C_i(u)\in\bigl[p_i(\theta)e^{-\epsilon_Lu}, 1-(1-p_i(\theta))e^{-\epsilon_Lu}\bigr]\subset\bigl[e^{-\epsilon_L(\theta+u)}/2, 1-e^{-\epsilon_L(\theta+u)}/2\bigr].
$$

Consequently, at absolute time $t=\theta+u$, every ratio of the two entries of a row is at most $\Lambda(t)=2e^{\epsilon_Lt}-1$, for the native and the parent rows alike. If $\epsilon_Lt\le0.1022$, the sharper bound $|p-1/2|\le\epsilon_Lt/2$ holds for both and gives a ratio below $1.23$.

*Proof.* Variation of constants: $p_i(t)=\frac12e^{-\epsilon_Lt}+\epsilon_L\int_0^te^{-\epsilon_L(t-s)}q_s(\cdot) ds$ with $q_s\in[0,1]$. Likewise $p^C_i(u)=p_i(\theta)e^{-\epsilon_Lu}+\epsilon_L\int_0^ue^{-\epsilon_L(u-v)}q^C_v(\cdot) dv$. For the sharper bound, $|p^C_i(u)-\frac12|\le|p_i(\theta)-\frac12|e^{-\epsilon_Lu}+\frac12(1-e^{-\epsilon_Lu})\le\frac{\epsilon_L(\theta+u)}2$. $\square$

**Lemma S4.5 (own-law parent).** For the activation $(\mu_{\rm act},p(\theta))$ and every $\epsilon_L\ge0$, the coupled system of the parent process and its own-law rows has exactly one solution on $[0,\infty)$. Its rows are continuously differentiable and satisfy Lemma S4.4.

*Proof.* The argument is that of `prop:phil-actual-parent-dynamics`, written with iterated Volterra estimates instead of short steps. That argument uses neither the selection tolerances nor $d<1/4$. Its only inputs are an activation probability law on $\mathcal Y$ and interior initial rows. Here $\mu_{\rm act}$ is a probability law carried by the bounded set $C(\mathcal T_\theta)$, so every moment is finite, and $p(\theta)$ is interior by Lemma S4.4.

Fix $u_1>0$ and put $c_1=e^{-\epsilon_L(\theta+u_1)}/2$. Let $\mathscr P$ be the set of continuous row paths on $[0,u_1]$ lying in the intervals of Lemma S4.4. It is closed in the supremum norm, and all its entries lie in $[c_1,1-c_1]$. For $p\in\mathscr P$, the parent with prescribed rows $p$ is built pathwise: linear diffusions on strata between rings, and at each ring a fresh hidden draw, fresh uniforms, and the projection to the target stratum. There are finitely many rings on $[0,u_1]$, so the construction does not explode. Let $\Gamma p$ be the right side of the variation-of-constants formula with $q^C_v=q^{C,p}_v$; then $\Gamma$ maps $\mathscr P$ into itself.

Now couple two prescribed-row parents $p,\tilde p\in\mathscr P$ through the same initial sample, Brownian motion, clock, hidden draws, and uniforms. They agree until a ring at which some uniform falls between the two posterior probabilities at the common point $\tilde x=y+F_M\zeta$. Since $\partial_p\beta=\beta(1-\beta)/(p(1-p))\le1/(4c_1(1-c_1))$, this happens at a ring with probability at most $\|p-\tilde p\|_\infty/(c_1(1-c_1))$. The rate-one compensator then gives $\mathrm{TV}(q^{C,p}_v,q^{C,\tilde p}_v)\le L_1\int_0^v\|p-\tilde p\|_\infty$, with $L_1=1/(c_1(1-c_1))$. Therefore

$$
\|\Gamma p(u)-\Gamma\tilde p(u)\|_\infty\le\epsilon_L\int_0^u\mathrm{TV}_v dv\le\epsilon_LL_1u_1\int_0^u\|p-\tilde p\|_\infty(w) dw .
$$

The $n$th iterate contracts the supremum distance by $(\epsilon_LL_1u_1^2)^n/n!$, so $\Gamma$ has exactly one fixed point in $\mathscr P$. Every solution lies in $\mathscr P$ by Lemma S4.4, solutions on nested horizons agree, and $u_1$ is arbitrary. Because the clock has rate one, $|q^{C,p}_v-q^{C,p}_{v'}|\le|v-v'|$, so the fixed point is $C^1$ and solves the row equation. For $\epsilon_L=0$ the rows stay at $p(\theta)$ and only the prescribed-row construction is needed. $\square$

For fixed rows, the reversibility and detailed balance of $C_\#\mu_{T,p}$ proved in `prop:phil-actual-parent-dynamics` hold unchanged. They are not used below.

## 7. Direct stopped coupling (requirement ii)

On one probability space, take independent objects: $\xi=(X_\theta,S_\theta)\sim q^E_\theta$; a standard Brownian motion $W'$ on $\mathbb R^{12}$; a rate-one Poisson clock with rings $\tau_1<\tau_2<\cdots$; i.i.d. uniforms $U_{k,i}$; and i.i.d. $\zeta_k\sim\mathcal N(0,TK_Z^{-1})$ on $\mathbb R^3$.

*Native.* Set $(X^N_0,S^N_0)=\xi$. Between rings, $dX^N=-K_{S^N}X^N du+\sqrt{2T} dW'_u$. At ring $k$, receiver $i$ takes $i+1$ exactly when $U_{k,i}\le\beta_{i,i+1}(X^N_{\tau_k-};p_i(\theta+\tau_k))$. By the Markov property of the driving construction at the deterministic time $\theta$ (Section 1), the law of $(X^N_u,S^N_u)_{u\ge0}$ is the law of $(X_{\theta+u},S_{\theta+u})_{u\ge0}$ given $E_\theta$. Hence $\mathrm{Law}((C(X^N_u,S^N_u))_{u\le h})=\mathsf P^{\rm fine}_{\theta,h}$.

*Parent.* Set $(S^C_0,Y^C_0)=C(\xi)$, so the activation is common and has law $\mu_{\rm act}$. Between rings, on stratum $S$, $dY^C=-K_SY^C du+\sqrt{2T} P_{W_S}dW'_u$; since $P_{W_S}W'$ is a standard Brownian motion on $W_S$, this is the parent diffusion. At ring $k$, put $\tilde x=Y^C_{\tau_k-}+F_{S^C}\zeta_k$ on a matching stratum ($\tilde x=Y^C_{\tau_k-}$ otherwise). Receiver $i$ takes $i+1$ exactly when $U_{k,i}\le\beta_{i,i+1}(\tilde x;p^C_i(\tau_k))$, and the new state is $(S',P_{W_{S'}}\tilde x)$. The draw $\zeta_k$ has law $\kappa$ and the uniforms are fresh, so this is the rate-one kernel $J_{p^C}$. The own-law row path $p^C$ is deterministic by Lemma S4.5, so the parent marginal is exactly $\mathsf P^C_h$.

*Departure.* Let $M_0=S_\theta$ and $\sigma_D=\inf\{\tau_k:S^N_{\tau_k}\ne M_0\text{ or }S^C_{\tau_k}\ne M_0\}$.

**Lemma S4.6 (agreement).** For $u<\sigma_D$, $S^N_u=S^C_u=M_0$ and $Y^C_u=P_{W_{M_0}}X^N_u$. Consequently $\mathrm{TV}(\mathsf P^{\rm fine}_{\theta,h},\mathsf P^C_h)\le P(\sigma_D\le h)$.

*Proof.* The proof is by induction over rings before $\sigma_D$. On an inter-ring interval with both processes on $M_0$, (F1) gives $d(P_WX^N)=-K_{M_0}P_WX^N du+\sqrt{2T} P_WdW'$, the parent's equation with the same noise and the same starting value, so the two agree by pathwise uniqueness of the linear equation. At a ring before $\sigma_D$ both propose $M_0$: $X^N$ does not move, and the parent state becomes $P_W(Y^C+F\zeta_k)=Y^C$ since $F\zeta_k\in Z_{M_0}$. The retained paths therefore coincide on $[0,h]$ whenever $\sigma_D>h$, and the coupling inequality gives the bound. $\square$

The coupled proposals share uniforms, but only the marginal correctness of each ring's randomness is used. The hidden coordinates, whether the native actual ones or the parent's fresh draws, enter only through the departure probabilities, never through the retained path before $\sigma_D$.

## 8. Pointwise departure hazards (requirement iii)

**Lemma S4.7.** Let the common pre-ring state be $(M_0,x)$ with $x=X^N_{u-}$ and $y=P_Wx=Y^C_{u-}$, at relative time $u$. Then

$$
P(\text{native departs at the ring}\mid\text{past})\le4\Lambda(\theta+u) e^{-G_{M_0}(x)/T},\qquad
k_{p^C(u)}(y)\le4\sqrt{8/3} \Lambda(\theta+u) e^{-[c_{M_0}(y)^2-\frac43z_+(y)^2]/T}.
$$

Since $\frac43z_+^2\le2\zeta^2$, the conditional probability that a ring at $u$ is a departure of either process is at most $4(1+\sqrt{8/3})\Lambda(\theta+u)e^{-G_{M_0}(x)/T}$.

*Proof.* Receiver $i$ has partner $j$ on a selected edge $e(i)\in\{e,f\}$ and exterior source $k$ on an exterior edge $g(i)$; the two exterior edges are each used by two receivers. A departure requires some receiver to choose its exterior source, and

$$
\beta_{ik}(x;p)=\frac{p_{ik}e^{-\mathcal D_{g}/T}}{p_{ij}e^{-\mathcal D_{e}/T}+p_{ik}e^{-\mathcal D_{g}/T}}\le\frac{p_{ik}}{p_{ij}}e^{-(\mathcal D_g(x)-\mathcal D_e(x))/T}.
$$

*Native.* By (F3), $\mathcal D_g\ge c_g^2\ge c_{M_0}^2$. By (F2), $\mathcal D_e\le2z_+^2+2z_1^2+z_2^2\le2\zeta^2$. Summing four receivers with the ratio bound of Lemma S4.4 at the native rows gives the first display.

*Parent.* At $\tilde x=y+F\zeta$, (F3) gives $\mathcal D_g(\tilde x)\ge c_g(y)^2$. By (F2), $\mathcal D_e(\tilde x)=(z_+(y)+z_1)^2+z_2^2$ with independent $z_1\sim\mathcal N(0,T/(8+T))$ and $z_2\sim\mathcal N(0,T/(4+5T))$. The Gaussian identity $\mathbb E e^{(a+Z)^2/T}=(1-2s^2/T)^{-1/2}\exp[a^2/(T(1-2s^2/T))]$, valid for $Z\sim\mathcal N(0,s^2)$ with $s^2<T/2$, gives factors $((8+T)/(6+T))^{1/2}\le\sqrt{4/3}$ and $((4+5T)/(2+5T))^{1/2}\le\sqrt2$, and an exponent at most $\frac43z_+^2/T$. The same holds for $\mathcal D_f$ by the symmetry $z_1\mapsto-z_1$. Integrating over $\zeta$ and summing four receivers, with the ratio bound at the parent rows, gives the second display. This is the part-(d) computation of the source, with the row ratio now carried explicitly. $\square$

## 9. The retained tube after activation, and the drift of exterior residuals (requirement iv)

**Lemma S4.8 (tube and gap).** Let $\theta\ge1/4$, $\delta'>0$, $R=R_0+\delta'$, and $\tau_\Gamma=\inf\{u:|Z'_u|>\delta'\}$. For $u<\sigma_D\wedge\tau_\Gamma$, $|X^N_u-\bar x^{\sigma,M_0}(\theta+u)|\le R$, and

$$
G_{M_0}(X^N_u)\ge g(\theta,h,R):=\Bigl[e^{-T(\theta+h)}\bigl(\tfrac32-\tfrac12e^{-8\theta}\bigr)-\sqrt2R\Bigr]_+^2-2\bigl(e^{-8\theta}+R\bigr)^2\qquad(u\le h).
$$

*Proof.* Before $\sigma_D$ the native is held at $M_0$, so $X^N_u=e^{-K_{M_0}u}X_\theta+Z'_u$ and $\bar x(\theta+u)=e^{-K_{M_0}u}\bar x(\theta)$. Contraction and Lemma S4.3 give the radius bound. By (F4), $|c_g(\bar x(t))|=e^{-Tt}(\frac32-\frac12e^{-8t})\ge e^{-T(\theta+h)}(\frac32-\frac12e^{-8\theta})$ for $t\in[\theta,\theta+h]$, and $\zeta(\bar x(t))=e^{-(8+T)t}\le e^{-8\theta}$. The Lipschitz constants $\sqrt2$ and $1$ of (F3) and Section 4 finish the proof. $\square$

The factor $e^{-T(\theta+h)}$ is the long-window drift: along the center path the exterior residuals decay at the slowest kernel rate $T$, since $x^\circ+n_c$ is a $K_M$-eigenvector with eigenvalue $T$, and they approach the thermal region only on times of order $1/T$. Two tube choices give the following gaps (computed in Section 13), for $\theta\ge1/4$ and $T(\theta+h)\le1/10$.

| Tube | $\delta'$ | $R$ | $g$ for $\theta\ge1/4$ | $g$ for $\theta\ge t_\epsilon$ | largest $T(\theta+h)$ with $g\ge1$ |
| --- | --- | --- | --- | --- | --- |
| Chebyshev | $\delta_\epsilon$ | $\varrho_\circ+2\delta_\epsilon$ | $1.6009$ | $1.8037$ | $0.3248$ |
| order one | $1/20$ | $\varrho_\circ+\delta_\epsilon+1/20$ | $1.3906$ | $1.6118$ | $0.2439$ |

These values use the single conservative partner-cost bound $\mathcal D_e\le2\zeta^2$ of Lemma S4.7, which loses a factor two in the $z_+^2$ term. A sharper accounting, noted by the verifier (defect D3 of `stage4-crossmodel-parent-dynamics.md`), uses the exact decomposition $\mathcal D_e=2(n^+_e\cdot x)^2+(n^-_e\cdot x)^2$ with orthonormal $n^\pm_e$. Since $|n^+_e\cdot\bar x(t)|=a_0:=e^{-(8+T)t}/\sqrt2$ and $n^-_e\cdot\bar x(t)=0$, maximizing $2(a_0+\delta_1)^2+\delta_2^2$ over $\delta_1^2+\delta_2^2\le R^2$ (the maximum is at $\delta_1=R$) gives $\mathcal D_e\le2(a_0+R)^2\le(e^{-8\theta}+\sqrt2R)^2$ on the tube, and separate native and parent gaps then give $1.416$ for the order-one tube and $1.615$ for the Chebyshev tube (both limited by the parent term), for $\theta\ge1/4$. This sharpening is optional. The theorem keeps the conservative values of the table, which are valid lower bounds.

**Lemma S4.9 (tube exit, conditional on $E_\theta$).** For either matching,

$$
P\bigl(\sup_{u\le h}|Z'_u|>\delta_\epsilon\bigr)\le\frac{384 Th}{\delta_\epsilon^2}=73728 \epsilon^4h,\qquad
P\bigl(\sup_{u\le h}|Z'_u|>\delta'\bigr)\le24\exp\Bigl[-\frac{\delta'^2}{192 Th}\Bigr],
$$

and the second equals $24e^{-1/(76800 Th)}$ at $\delta'=1/20$. Since $W'$ is independent of $\mathcal F_\theta$, the same bounds hold for the conditional probabilities given $E_\theta$.

*Proof.* In an orthonormal eigenbasis of $K_{M_0}$ with eigenvalues $\lambda_k\ge0$, $Z'^k_u=\sqrt{2T}\int_0^ue^{-\lambda_k(u-v)}dB^k_v$ with independent standard Brownian motions $B^k$. Integration by parts gives $|Z'^k_u|\le2\sqrt{2T}\sup_{v\le u}|B^k_v|$. For the first bound, Doob's $L^2$ inequality gives $\mathbb E\sup_{u\le h}|Z'_u|^2\le12\cdot8T\cdot4h$, and Chebyshev's inequality with $\delta_\epsilon^2=\epsilon^4/192$ finishes. For the second, require each coordinate to be at most $a=\delta'/\sqrt{12}$. The reflection principle and $P(N(0,1)>x)\le\frac12e^{-x^2/2}$ give $P(\sup_{v\le h}|B^k_v|>a/(2\sqrt{2T}))\le2e^{-a^2/(16Th)}$, and the union over twelve coordinates gives the bound. $\square$

## 10. Proof of Theorem S4.1(c) (requirement v)

Parts (a) and (b) are Lemmas S4.3 and S4.5. For (c), fix a tube $\delta'$. Let $N_D$ count the rings in $[0,h\wedge\sigma_D\wedge\tau_\Gamma]$ at which either process proposes an assignment other than $M_0$. The ring marks $(U_k,\zeta_k)$ are independent of the pre-ring history, and the clock is Poisson of rate one. The compensator of $N_D$ is therefore $\int_0^{h\wedge\sigma_D\wedge\tau_\Gamma}\lambda_D(u) du$, where $\lambda_D(u)$ is the conditional departure probability of Lemma S4.7 at the pre-ring state. For $u<\sigma_D\wedge\tau_\Gamma$, Lemmas S4.7 and S4.8 give $\lambda_D(u)\le4(1+\sqrt{8/3})\Lambda(\theta+h)e^{-g/T}$. If $\sigma_D\le h$, then either $\tau_\Gamma\le\sigma_D\le h$, or the departure ring lies in $[0,h\wedge\tau_\Gamma]$ and $N_D\ge1$. Hence, by Lemma S4.6,

$$
\mathrm{TV}(\mathsf P^{\rm fine}_{\theta,h},\mathsf P^C_h)\le P(\sigma_D\le h)\le P(\tau_\Gamma\le h)+\mathbb EN_D\le P(\tau_\Gamma\le h)+4\bigl(1+\sqrt{8/3}\bigr)\Lambda(\theta+h) h e^{-g/T}.
$$

Insert Lemma S4.9 and the gaps of the table, which are at least $1.60$ for the Chebyshev tube and $1.39$ for the order-one tube when $T(\theta+h)\le1/10$ and $\theta\ge1/4$. This gives $73728 \epsilon^4h+\mathcal H(1.60)$ with the first tube and $24e^{-1/(76800 Th)}+\mathcal H(1.39)$ with the second; the total variation is at most the smaller of the two complete bounds. $\square$

*Proof of Corollary S4.2.* For $\epsilon_L\le1$ and $T(\theta+h)\le1/10$, $\Lambda(\theta+h)\le2e^{1/(10T)}$ and $4(1+\sqrt{8/3})\cdot2=21.06$. For (i), $73728 \epsilon^4h=73728 T^{1/2}h$. For (ii), $Th=T^\gamma$. For (iv), if $Th\to c>0$ along a subsequence, the order-one entry tends to $24e^{-1/(76800c)}>0$ and the Chebyshev entry diverges. $\square$

**Consistency with part (d) of the source.** With frozen rows ($\epsilon_L=0$, $\Lambda=1$), $\theta=t_\epsilon$, and $h=1$, the theorem gives at most $73728 \epsilon^4+10.54 e^{-1.6/T}$. Part (d) gives $2p_\epsilon/(1-p_\epsilon)+4\sqrt{8/3} e^{-1/T}$, whose leading term is about $2\cdot73728 \epsilon^4t^\circ_*$. The present bound is smaller by a factor of about $2t^\circ_*$, because the post-activation tube is independent of the prefix and needs no division by the per-seed floor.

**Numbers at $\epsilon=1/100$** ($T=10^{-16}$). The order-one entry governs the minimum. It satisfies $24e^{-1/(76800Th)}\le24e^{-10}\approx1.1\times10^{-3}$ for every $h\le1.3\times10^{10}$, and at $h=1$ it is $24\exp(-1.3\times10^{11})$, so the bound there is astronomically small; the hazard term is below $10^{-(10^{15})}$ on the whole range. The Chebyshev entry, $7.4\times10^{-4}$ at $h=1$, would govern only when $h$ is so small that $73728 \epsilon^4h<24e^{-1/(76800Th)}$, which at $\epsilon=1/100$ never happens for $h\ge1$. In fact it happens for no $h>0$ and no $\epsilon\le1/100$: with $y=1/(76800Th)$ one has $73728 \epsilon^4h=0.96 \epsilon^{-4}/y\ge9.6\times10^7/y$, and $9.6\times10^7/y>24e^{-y}$ for every $y>0$. The Chebyshev entry is therefore kept only for the elementary statement of Corollary S4.2(i). At this value of $\epsilon$ the theorem thus covers windows up to about $10^{10}$, compared with $1/\epsilon=100$ and $1/T=10^{16}$.

## 11. Mobility (requirement vii)

The coupling holds at the original mobility $\epsilon_L=\epsilon=T^{1/8}$, uniformly over $\epsilon_L\in[0,1]$. Rows enter in exactly two places: the ratio $\Lambda(\theta+h)$ in the departure hazards, and the prefix failure $\tilde p$ in part (a). Both are multiplied by $e^{-1/T}$ or smaller. For $\epsilon_L\le1$ and $T(\theta+h)\le1/10$, the product is at most $2e^{-9/(10T)}$. The proof of part (c) extends verbatim to any $\epsilon_L$ with $\epsilon_L(\theta+h)\le(g-1)/T$, provided $P(E_\theta)>0$. The hazard estimates themselves never need $\epsilon_L$ small; the theorem stops at $\epsilon_L\le1$ only because part (a) gives an explicit prefix bound in that range. The native rows are learned from the unconditioned law and the parent rows from the parent's own law. Both start at $p(\theta)$ and move at speed at most $\epsilon_L$, so they can separate by up to $\min\{1,2\epsilon_Lu\}$ after activation. This difference is invisible to the bound, because rows affect the retained path only at departures, and departures are exponentially rare on the tube.

Item 3 needed slow schedules ($\epsilon_L\le T^2$) for two independent reasons. First, its activation event and its hypotheses $\delta,\eta\le T$ come from the Stage 1 selection theorem at the late time $t_L\sim2\epsilon_L^{-1}\log(1/\epsilon_L)$, which requires slow learning. Second, its departure control came from concentration of the rows on the selected matching, through $d=\delta+\epsilon_Lh<1/4$ and the term $4hd/(1-4d)$, so row motion at speed $\epsilon_L$ over the window cost directly. In the early seeded regime the departure control comes instead from the energy gap between exterior and partner costs, $g\ge1$ in units where the hazard is $e^{-g/T}$, and the rows appear only as a bounded-exponent prefactor.

This does not transfer to the first-block learned/frozen comparison of `prop:phil-early-block-null`. That comparison couples ring choices along all histories, including those in which receivers are near indifference, where a row difference of size $\epsilon_Lt$ changes the choice with probability of the same order. Hence its bound $2\epsilon_LH_T^2=8\epsilon_LT^{-1/4}$ is vacuous at $\epsilon_L=T^{1/8}$. The parent coupling here compares two processes on one seeded tube where every ring is decided with exponentially small error, whatever the rows.

## 12. What this does not settle (requirement viii)

The theorem is the dynamical half of a parent statement. A parent in the sense of `open:rg-formation-adaptive-family` needs separately vanishing conditional and dynamical errors. The conditional error is obligation 1. According to `stage4-seeded-hidden-information.md` (Opus-authored, cross-model verified by Claude Fable 5.1 with verdict VALID_WITH_MINOR_ISSUES in `stage4-crossmodel-hidden-info.md`), two one-directional statements are proved: the upper bound tends to zero when $\theta-\log(1/\epsilon)\to\infty$ (with $\theta\le o(\epsilon^{-4})$), and the lower bound diverges when $\log(1/\epsilon)-\theta\to\infty$. The window $\theta=\log(1/\epsilon)+O(1)$ is undecided by those bounds. The present path bound holds for every $\theta\ge1/4$, including activation near the first qualifying completion time, which is at most $(1/2)\log(1/\epsilon)+1$, where the native hidden coordinates still carry an $e^{-4\theta}\varrho_\circ$ imprint far above the thermal scale $\sqrt T$. The retained path law does not detect this before a departure, because the drift splits and self-proposals discard the hidden draw. Any restriction of the activation time to $\theta\ge\log(1/\epsilon)+\omega(1)$ therefore comes from the static half alone. The two halves combine where the admissible activation times of that record overlap $[1/4,t^\circ_*]$, that is on $[\log(1/\epsilon)+\omega(1),t^\circ_*]$, which contains the assigned range $[t_\epsilon,t^\circ_*]$.

Several further items are not settled. The native hidden conditional law during the window, $H_{\rm opt}(q^E_{\theta+u})$, is not bounded here. The comparison is of retained paths only; the obligation-1 record treats fixed-prefix future marginals separately. Conditioning is only on $E_\theta$ or on any $\mathcal F_\theta$-measurable sub-event of it, since the proof uses only the support property of Lemma S4.3. It is not on the whole contrast event $E_T$, on the first-block mark $K_T$, or on non-seeded contrast histories, whose states are not certified to lie in a tube. The Stage 4 exact-checks record (`stage4-exact-checks.md`) also finds that $E_T$ reads hidden coordinates and is not a retained-path event. Activation at the random first qualifying completion time is not treated. The strong Markov property would give the same coupling pathwise for a stopping time with values in $[1/4,t^\circ_*]$ and tube support, but the own-law parent would then need to be defined as a family indexed by the activation value, with its regular conditional activation laws; that construction is not written out.

Windows of order $1/T$ or longer are outside the method. Heuristically, and without proof here, the slow retained coordinates move by order one on that time scale, the exterior residuals then reach the thermal region with positive probability, and departures cease to be rare. After a departure the parent draws fresh hidden coordinates while the native keeps its own, and the native can enter a matching stratum with non-thermal hidden coordinates. A coupling beyond $1/T$ would need a departure-level estimate of the native hidden conditional law given the retained path, which is a filtering statement not attempted here. No lower bound on the total variation is claimed for such windows.

The following questions are also untouched. The learned/frozen first-block comparison at $\epsilon_L=T^{1/8}$ is not addressed: the coupling holds equally in both arms and says nothing about which block forms. The loop-mean comparison between initial means differing in $\sum_i\omega_i$ is not addressed. Recursion (R14) is not addressed: the parent's own dynamics over $h=o(1/T)$ are the held projected diffusion with exponentially rare departures, and no second-stage event or handoff class is analyzed. On R15: the seeded sub-event is a coherence episode with restoring clause and stationary margin (`prop:phil-seeded-contrast-formation`(b)). The one-time configuration that the parent maintains over the following window, a matching with thermal partner costs and exterior common residuals above $13/10$, has stationary probability bounded below in $T$, because under $\mathcal N(0,TK_M^{-1})$ each exterior $c_g$ is a centered Gaussian with variance of order one. Part (a) of `prop:rg-formation-endogenous-cycle` needs its entrance clause for exactly this reason. A claim built only on the parent path over $[0,h]$ would state persistence of a formed block, not a new formation, and the window $h\gg H_T=2T^{-1/8}$ lies beyond the first-block horizon.

## 13. Executed checks

These computations are algebraic and numerical supplements, not proofs. They ran with the default CPU interpreter `C:\Python314\python.exe` (sympy 1.14.0, mpmath, scipy 1.17.1) as `python stage4_checks.py`, exit 0, in about one second. The script and its output are archived at `C:\Users\chris and christine\Desktop\MultiAgentELBO\docs\derivations\2026-09-26-selection-to-formation\stage4-evidence\author-scratch\stage4_checks.py` and `stage4_checks_output.txt`; the earlier condensed block and its output are archived in the same folder as `stage4_checks_condensed.py` and `stage4_checks_condensed_output.txt`. The block below is a condensed form of that script. It now also carries the constant arithmetic of Section 3 (the row ratio, the matching-mass bound $0.696$, the ratio bound $0.4369$, the slow-ball mass with the exact factor $5$) and the quadrature check of the Gaussian identity, which were previously only in the scratch script (verifier defect D5). The extended block was extracted from this file and run with the same interpreter on 2026-09-28 (exit 0, about 1.4 s); its output is not archived separately. It reproduced the exact assertions, the sheet-weight fits, and the gaps, and it printed row ratio $1.2274$, $\mu(M)<0.69594$, $(1-\mu)/\mu>0.43690$, slow-ball mass $2.619\times10^{-18}$ (both forms), $4(1+\sqrt{8/3})=10.532$, $73728$, $76800$, and quadrature against closed form $1.1795731674$ at rate $8+T$ and $1.4592314013$ at rate $4+5T$, agreeing to the last printed digit. An earlier version that used symbolic square roots and 12-by-12 symbolic determinants did not finish within ten minutes and was stopped; the version below uses the rational normals of Section 4 and high-precision numerical determinants.

The exact assertions passed for both matchings. The residual covectors have $|a^b|^2=3$, $a^b\cdot a^m=1$ on a common edge, and $|\frac12(a^b+a^m)|^2=2$. The four normals are orthonormal eigenvectors with $H_M$-eigenvalues $8,8,4,4$ and $R_{\rm ev}$-eigenvalues $0,0,4,4$. $R_{\rm ev}$ preserves $\ker H_M$, and its eigenvalues there are $\{4:2, 0:6\}$; the printed multiset $\{4:2,0:10\}$ includes the four zero directions of the range. The exterior $c_g$ annihilate $Z_M$, with $c_g\cdot n_c=-1/2$, and the loop covector annihilates $Z_M$. Also $(z_+,z_1,z_2,z_3)(x^\circ)=(-1,0,0,0)$, $x^\circ+n_c\in\ker H_M\cap\ker R_{\rm ev}$, $p/4=n_c$, and $|x^\circ+n_c|^2=3$. The exterior residuals of both channels equal $-3/2$ at $x^\circ+n_c$ and $-1/2$ at $n_c$, which gives (F4), and the selected ones equal $0$ and $1$. The identities $\mathcal D_e=(z_++z_1)^2+z_2^2$, $\mathcal D_f=(z_+-z_1)^2+z_3^2$, and $\mathcal D_g=c_g^2+d_g^2$ hold as polynomial identities. For the sheet weights, a two-point fit at $T=10^{-10}$ and $10^{-20}$ (60 digits) gives $w_S/w_M\approx2.3905 T$ for twelve nonmatching sheets, $\approx1.2910 T^{3/2}$ for $(1,2,3,0)$ and $(3,0,1,2)$, and exactly $1$ for the two matchings. The numerical values: row ratio $0.5511/0.4489=1.2277$; $1.23^4=2.2889$; $\mu(M)<0.6960$; $(1-\mu)/\mu>0.4369$; $4(1+\sqrt{8/3})=10.532$; $384\cdot192=73728$; $192\cdot400=76800$; $\delta_\epsilon(1/100)=7.2169\times10^{-6}$; the gaps of the table; and the slow-ball mass $\frac{10}{384}R_0^8=2.6\times10^{-18}$ (the archived scratch script prints the looser $1.31\times10^{-17}$, computed with the factor $5^2$ in place of the exact $5$; the block below uses the exact $5$). A quadrature check of the Gaussian identity at $T=10^{-3}$, $a=0.004$ agrees with the closed form to $10^{-15}$ for both rates.

```python
"""Exact algebra and constant checks for the Stage 4 early-parent path coupling."""
import itertools, math
import sympy as sp
import mpmath as mp

def residual(edge, channel):
    a = sp.zeros(12, 1); a[channel + edge] = -1; a[channel + (edge + 1) % 4] = 1; a[8 + edge] = -1
    return a
ab = [residual(e, 0) for e in range(4)]; am = [residual(e, 4) for e in range(4)]
I12 = sp.eye(12); Dmat = sp.zeros(4, 12)
for i in range(4): Dmat[i, i] = 1; Dmat[i, 4 + i] = -1
Rev = 2 * Dmat.T * Dmat
def edge_of(i, j): return i if (i + 1) % 4 == j else j
def H_of(S):
    H = sp.zeros(12, 12)
    for i, j in enumerate(S):
        g = edge_of(i, j); H += ab[g] * ab[g].T + am[g] * am[g].T
    return H
def dot(u, v): return (u.T * v)[0]
xcirc = sp.Matrix([0] * 8 + [1] * 4); loop = sp.Matrix([0] * 8 + [1] * 4)
S0, S1 = (1, 0, 3, 2), (3, 2, 1, 0)
for M, (e, f), ext in [(S0, (0, 2), (1, 3)), (S1, (1, 3), (0, 2))]:
    H = H_of(M); Pe, Pf = ab[e] + am[e], ab[f] + am[f]
    nc, z1, z2, z3 = (Pe + Pf) / 4, (Pe - Pf) / 4, (ab[e] - am[e]) / 2, (ab[f] - am[f]) / 2
    rng = [nc, z1, z2, z3]
    assert sp.Matrix([[dot(u, v) for v in rng] for u in rng]) == sp.eye(4)
    for u, lam in zip(rng, [8, 8, 4, 4]): assert H * u == lam * u
    assert H.rank() == 4 and Rev * nc == sp.zeros(12, 1) and Rev * z1 == sp.zeros(12, 1)
    assert Rev * z2 == 4 * z2 and Rev * z3 == 4 * z3
    Prng = sum((u * u.T for u in rng), sp.zeros(12, 12)); Pker = I12 - Prng
    assert Pker * Rev * Prng == sp.zeros(12, 12)
    print("eigenvalues of Pker Rev Pker:", (Pker * Rev * Pker).eigenvals())
    for g in ext:
        c = (ab[g] + am[g]) / 2
        assert all(dot(c, u) == 0 for u in (z1, z2, z3)); print("c_g.n_c =", dot(c, nc))
    assert all(dot(loop, u) == 0 for u in (z1, z2, z3))
    print("(z+,z1,z2,z3)(xcirc) =", [dot(u, xcirc) for u in rng])
    v0 = xcirc + nc
    assert H * v0 == sp.zeros(12, 1) and Rev * v0 == sp.zeros(12, 1) and (Pe + Pf) / 4 == nc
    for g in ext:
        assert dot(ab[g], v0) == dot(am[g], v0) == sp.Rational(-3, 2)
        assert dot(ab[g], nc) == dot(am[g], nc) == sp.Rational(-1, 2)
    for g in (e, f): assert dot(ab[g], v0) == 0 and dot(ab[g], nc) == 1 and dot(am[g], nc) == 1
    X = sp.Matrix(sp.symbols("x0:12")); zp_, z1_, z2_, z3_ = [dot(u, X) for u in rng]
    De = (dot(ab[e], X) ** 2 + dot(am[e], X) ** 2) / 2; Df = (dot(ab[f], X) ** 2 + dot(am[f], X) ** 2) / 2
    assert sp.expand(De - (zp_ + z1_) ** 2 - z2_ ** 2) == 0 and sp.expand(Df - (zp_ - z1_) ** 2 - z3_ ** 2) == 0
    for g in ext:
        Dg = (dot(ab[g], X) ** 2 + dot(am[g], X) ** 2) / 2
        assert sp.expand(Dg - (dot(ab[g] + am[g], X) / 2) ** 2 - (dot(ab[g] - am[g], X) / 2) ** 2) == 0
mp.mp.dps = 60
Hn = {S: mp.matrix(H_of(S).tolist()) for S in itertools.product(*[((i + 1) % 4, (i - 1) % 4) for i in range(4)])}
Revn = mp.matrix(Rev.tolist())
logdet = lambda S, Tv: mp.log(mp.det(Hn[S] + Tv * (mp.eye(12) + Revn)))
for S in Hn:
    r1 = (logdet(S0, mp.mpf("1e-10")) - logdet(S, mp.mpf("1e-10"))) / 2
    r2 = (logdet(S0, mp.mpf("1e-20")) - logdet(S, mp.mpf("1e-20"))) / 2
    slope = (r2 - r1) / (mp.log(mp.mpf("1e-20")) - mp.log(mp.mpf("1e-10")))
    print(S, "w_S/w_M ~", float(mp.e ** r1 / mp.mpf("1e-10") ** slope), "* T^", float(slope))
def gap(th, x, R):
    c = math.exp(-x) * (1.5 - math.exp(-8 * th) / 2) - math.sqrt(2) * R
    return max(c, 0.0) ** 2 - 2 * (math.exp(-8 * th) + R) ** 2
d = 1e-4 / (8 * math.sqrt(3))
for R in (0.01 + 2 * d, 0.01 + d + 0.05):
    print(R, gap(0.25, 0.1, R), gap(2 * math.log(100), 0.1, R))
# Section 3 constants: row ratio at eps_L t <= eps t* = (1 + 4 ln 10)/100, matching-mass bound, slow-ball mass.
up = 0.5 + (1 + 4 * math.log(10)) / 200
print("row ratio", up / (1 - up), "mu(M) <", 1.23 ** 4 / (1 + 1.23 ** 4), "(1-mu)/mu >", 1.23 ** -4)
R0 = 0.01 + d
print("slow-ball mass", 2 * 5 * (2 * math.pi) ** -4 * math.pi ** 4 * R0 ** 8 / 24, 10 / 384 * R0 ** 8)
print("4(1+sqrt(8/3))", 4 * (1 + math.sqrt(8 / 3)), "384*192", 384 * 192, "192*400", 192 * 400)
# Quadrature check of E exp[(a+Z)^2/T] = (1-2s^2/T)^(-1/2) exp[a^2/(T(1-2s^2/T))], Z ~ N(0, s^2), s^2 = T/rate.
import scipy.integrate as si
Tv, a = 1e-3, 0.004
for rate in (8 + Tv, 4 + 5 * Tv):
    s2 = Tv / rate
    val = si.quad(lambda z: math.exp(-z * z / (2 * s2) + (a + z) ** 2 / Tv) / math.sqrt(2 * math.pi * s2), -1, 1, limit=400)[0]
    print("Gaussian identity", rate, val, (1 - 2 * s2 / Tv) ** -0.5 * math.exp(a * a / (Tv * (1 - 2 * s2 / Tv))))
```

## 14. Strongest supported result, minimal open obligation, next action

The strongest supported result is Theorem S4.1 with Corollary S4.2. Take the four-cycle at $T=\epsilon^8$, $\epsilon\le1/100$, with any Gaussian mean, learned product rows at any mobility $\epsilon_L\in[0,1]$ (including the original $T^{1/8}$), and the seeded early prefix $E_\theta$ at any deterministic $\theta\in[1/4,t^\circ_*]$. This prefix is the seeded sub-event of `prop:phil-seeded-contrast-formation`(b), not the contrast-formation event $E_T$ or the first-block mark $K_T$, so the result is not activation on the first-contrast event itself. The own-law type-(b) parent activated from the actual conditioned law $C_\#q^E_\theta$ with rows $p(\theta)$ exists uniquely. Its complete retained configuration/assignment path law stays within total variation $\min\{73728 \epsilon^4h+\mathcal H(1.60), 24e^{-1/(76800 Th)}+\mathcal H(1.39)\}$ of the conditioned native retained path whenever $T(\theta+h)\le1/10$, and this error vanishes on every window with $Th\to0$, up to $h=T^{-1+\gamma}$ for any $\gamma\in(0,1)$, with an error independent of $m_0$ and of the seeded floor. The ingredients are the direct stopped coupling of the two processes and pointwise hazard control from the exterior/partner cost gap. The stationary held-matching reference of item 3 is not used; its route fails here with an activation total variation above $1-3\times10^{-18}$ and a flux bound above $0.4369$ per unit time.

The static half, the obligation-1 bound on discarded conditional information at activation, is recorded in `stage4-seeded-hidden-information.md` and cross-model verified (`stage4-crossmodel-hidden-info.md`). It constrains the admissible activation times through two one-directional statements: the conditional error vanishes when $\theta-\log(1/\epsilon)\to\infty$, the lower bound diverges when $\log(1/\epsilon)-\theta\to\infty$, and the window $\theta=\log(1/\epsilon)+O(1)$ remains undecided. The two halves combine on $[\log(1/\epsilon)+\omega(1),t^\circ_*]$, for windows $h=o(1/T)$ and on the seeded sub-event only. Beyond the parent, the learned/frozen first-block comparison at $\epsilon_L=T^{1/8}$ and the loop-mean comparison remain open, and this result does not bear on them. The next action that would change the answer is to extend the conditioning from the seeded sub-event $E_\theta$ to the first-block mark, which is the object `open:rg-formation-adaptive-family` actually conditions on and which the exact checks show is not a retained-path event.
