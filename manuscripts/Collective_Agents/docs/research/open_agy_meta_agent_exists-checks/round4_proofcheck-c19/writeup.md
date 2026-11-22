# Claim C19 and its argument (cleaned write-up for a reconstruction check)

## Claim (exact statement)

For the I* architecture (specified below) with $\theta=(F,Q,R,R_c,R_s,\psi,\gamma,q_c)$ in an open set with $F<1$ and $0\le\gamma<\infty$, under both deliberation protocols, together with its mechanism medium and the nulls $N_{\mathrm{hab}}$, $N_{\mathrm{pr}}$ (every round), $N_{\mathrm{lp}}=N_{\mathrm{rn}}$ and $N_{\mathrm{fr}}$: the chain (policy, Kalman covariance) has a unique stationary law, reached geometrically in a Wasserstein distance and continuous in $\theta$ with modulus $O(\omega\log(1/\omega))$; $\Sigma^c(\theta)$ is continuous, $\Sigma^c\succeq q_cI$, and $\Sigma^c=\mathrm{blockdiag}(\alpha I_4+\beta\mathbf 1\mathbf 1^\top,\alpha I_4+\beta\mathbf 1\mathbf 1^\top)$ exactly; $r(A)$, both clause (c) baselines, every null contrast and the index at fixed declared decision states are continuous, so the sets on which the differ clause holds are open.

## Specification of I*

Two niches of four agents; independent AR(1) world components with $F=0.9$, $Q=0.05$, no renewal; own sensor noise $R=1$; every agent relays its own raw reading to all others with literal one-round latency and receiver-specific noise $R_c=0.1$, no re-relaying; one optional slot per agent, a public world channel of its niche read by every niche member through its own read noise $R_s=2$; exact filters on $(\eta_t,\eta_{t-1})$ with computation noise $10^{-4}I_2$; capacity $\kappa=12$; one policy precision $\gamma=400$ for attention and slots; slot cost $\psi=0.024$ nats; uniform product habits; prior errors as contrast coordinates. These are the base-point values; the claim concerns an open set of $\theta$ around them. The two protocols: T-fast runs the deliberation protocol (P4) of `def:agy-group-model` at a frozen decision state, followed by Gibbs attention; T-real lets a uniformly chosen member revise its slot by a logistic flip once per round, followed by Gibbs attention. The implementation is `Collective_Agents/docs/research/open_agy_meta_agent_exists-checks/round2_epistemic_persistent/lib.py`; the line numbers below refer to it.

## Definitions (live source)

- `def:fw-system`, one policy precision: `Collective_Agents/sections/02_framework.tex`, lines 11-17.
- World-conditional law, diffusive class, contrast and the second-moment convention (line 187), baseline (clause (c) at line 202), collective: `Collective_Agents/sections/04_collectives.tex`, lines 130-221.
- Group model, (P4), agency index and its class restriction: `Collective_Agents/sections/05_agency.tex`, lines 156-260.
- Nulls and "differs" (open-subset clause at line 333): same file, lines 332-360; meta-agent: lines 379-381.

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| Second-moment convention | $\Sigma^c=\E[\Cov(e(t)\mid\eta)]$, estimable as $\tfrac12\E[(e^1-e^2)(e^1-e^2)^\top]$ from two replicas on one world path | |
| Contrast | $r(C)=\xi_{\mathrm{in}}/\xi_{\mathrm{out}}$; compound-symmetric block with no cut: $r=1+n\beta/\alpha$ | $\alpha=1,\beta=0.5,n=4$: $r=3$ |
| Relayed sensing noise | an agent's own sensing noise is a private input, not conditioned on, even when relayed | |
| Agency decision states | declared fixed covariance points; the decision law at $X$ is the protocol kernel at $X$ | |

## Argument

### Setting

One niche of $n$ members ($n=4$ in I*, $n=8$ with one component in the medium).
- Policy $\pi=(\sigma,J)$: $\sigma\in\{0,1\}^n$ is the slot profile and $J_i\subset$ mates are the attention sets; $\mathcal P$ is finite.
- Covariance state $p\in[0,\infty)^n$, with $p_i$ the posterior variance of $\eta$ after the last update.
- Riccati step (lib.py:56-71): $p_i\mapsto g_\theta(p_i;a,b_i)$, with $a=1/R+\lvert\sigma\rvert/R_s$ and $b_i=\lvert J_i\rvert/(R+R_c)$.
- Chain $Z_t=(p(t-1),\pi_t)$: $p(t)=G_\theta(p(t-1),\pi_t)$, and $\pi_{t+1}\sim k_\theta(p(t),\pi_t;\cdot)$.

### Hypotheses ($\theta$ in a compact set $U$)

- (H1) $G_\theta(\cdot,\pi)$ is jointly continuous, and a compact set $\mathcal K_U$ is invariant under all $G_\theta(\cdot,\pi)$.
- (H2) For every policy sequence, $\lvert G^{(t)}(p)-G^{(t)}(p')\rvert_\infty\le C_1\rho^t\lvert p-p'\rvert_\infty$ with $\rho<1$.
- (H3) $k_\theta(p,\pi;\cdot)$ is jointly continuous and Lipschitz in $p$ in total variation, with constant $L$.
- (H4) $\mathrm{supp}\,k_\theta(p,\pi;\cdot)=\mathcal S(\pi)$ does not depend on $(\theta,p)$. On the support $k_\theta\ge\kappa_0>0$. There are $m$ and $\pi^\star$ such that every $\pi$ reaches $\pi^\star$ in exactly $m$ support steps.
- (H5) Policy randomness is independent of the world and of all sensing, channel and computation noises.
- (H6) Given the policy paths, the stacked state $Y$ (world, errors, carried sensing noises; lib.py:381-467) satisfies $Y_{t+1}=A_\theta(z_t)Y_t+\xi_t$ with $\xi_t\sim\mathcal N(0,N_\theta(z_t))$ independent of the past, and $A_\theta$, $N_\theta$ continuous. Uniform exponential stability: $\lVert A(z_{t+k-1})\cdots A(z_t)\rVert\le C_2\lambda^k$ with $\lambda<1$. Every prior error contains a fresh private term of variance at least $\sigma_{\min}>0$.

### Verification for I*

- (H1) The Riccati map is a Möbius map with positive coefficients: $g=(c_1p+c_0)/(d_1p+d_0)$, where $Q'=Q+q_c$ and $K_1=F^2q_c+Q'$; $c_1=F^2+bK_1$ and $c_0=Q'(1+bq_c)$; $d_1=aF^2+b+abK_1$ and $d_0=(1+aQ')(1+bq_c)$. $g$ is increasing in $p$ and decreasing in $(a,b)$. So $[0,b_U]^n$ is invariant for any $b_U$ at least the largest own-sensor-only fixed point.
- (H2) $c_1d_0-c_0d_1=F^2(1+bq_c)^2$. Hence $g'(p)=F^2(1+bq_c)^2/(d_1p+d_0)^2\le F^2/(1+aQ')^2\le\bar\rho=(F/(1+Q'/R))^2$ for all $p\ge0$. So $C_1=1$. The bound needs $F<1$ and an own sensor read every round ($a\ge1/R$).
- (H3) The ingredients are all analytic in $(\theta,p)$: the expected free energy, the soft-min, the logistic and Gibbs weights, and the (P4) stationary law. The (P4) law is analytic because Cramer's rule applies to the system $T^\top-I$ with one row replaced by $\mathbf 1^\top$, which is nonsingular for an irreducible chain.
- (H4) $\gamma<\infty$ and full-support habits make every weight positive. T-fast: $\mathcal S=\mathcal P$ and $m=1$. T-real: $\mathcal S(\pi)=\{\text{profiles within one flip}\}\times\{\text{all attention sets}\}$, and $m=n$. $\kappa_0$ is positive but of order $\exp(-\gamma\cdot\text{gap})$.
- (H5) The expected free energy depends on beliefs only through covariances (lib.py:62-97), and $\psi$ is constant.
- (H6) The closed loop is rank one: $M=A_F(I-KH)=A_F(I+P^-D)^{-1}=uv^\top$ with $u=(F,1)^\top$. The scalar closed-loop factor is $\lambda=v^\top u=F(1+bq_c)/(d_1p+d_0)\le\bar\lambda=F/(1+Q'/R)$; also $\lambda^2=g'$. Products are $M_{t+k-1}\cdots M_t=u(\prod\lambda_j)v_t^\top$. The stacked $A$ is block lower-triangular: $A_F$ with $\lVert A_F^k\rVert=F^{k-1}\sqrt{1+F^2}$; the rank-one error blocks; and zero blocks for the carried noises. So uniform exponential stability holds with any $\lambda\in(F,1)$. $\sigma_{\min}=q_c$, because the computation noise $\xi_i(t-1)$ enters only $m^-_{i,0}(t)$ (lib.py:374).

The nulls and the medium satisfy the same hypotheses: $N_{\mathrm{hab}}$: $\gamma=0$, so $L=0$. $N_{\mathrm{pr}}$: uniform partners. $N_{\mathrm{lp}}$ and $N_{\mathrm{fr}}$: dead relays with claimed covariances kept; the Riccati maps and $M$ are unchanged, and $\eta_{t-1}$ enters the errors only as an input. Medium: 256 profiles.

### Theorem 1 (stationary policy-covariance law)

Assume (H1)-(H4) on a compact $U$. Use the metric $d(z,z')=\min(1,\lvert p-p'\rvert_\infty)+\mathbf 1\{\pi\ne\pi'\}$ on $X_U=\mathcal K_U\times\mathcal P$. For $\theta\in U$ there is a unique invariant law $\mu_\theta$, and:
- (a) $W_d(\delta_zP_\theta^t,\mu_\theta)\le C_3\beta^t$ for every $z$, with $C_3$ and $\beta<1$ uniform on $U$;
- (b) $W_d(\mu_\theta,\mu_{\theta'})\le(C_3+M)\omega+M\omega\ln(1/\omega)/\ln(1/\beta)$, where $\omega=\sup_zW_d(\delta_zP_\theta,\delta_zP_{\theta'})$ and $M=\max\{2,C_1(1+2L\rho/(1-\rho))\}$; in I*, $\omega=O(\lvert\theta-\theta'\rvert)$;
- (c) the stationary two-sided path laws are weakly continuous in $\theta$.

Proof.
0. Feller. $X_U$ is compact. $P_\theta f(z)=\sum_{\pi'}k_\theta(G_\theta(p,\pi),\pi;\pi')f(G_\theta(p,\pi),\pi')$ is continuous in $z$.
1. Synchronous phase. Start two copies with equal policies, and couple the next policies by maximal coupling at every step. While the policies agree, $\lvert p_t-p'_t\rvert\le C_1\rho^t\delta$, where $\delta=\lvert p_0-p'_0\rvert$. Given agreement so far, the probability that the policies split at step $t$ is $\mathrm{TV}(k(p_t,\pi;\cdot),k(p'_t,\pi;\cdot))\le\min\{1-\kappa_0,LC_1\rho^t\delta\}$. The first bound holds because the two laws share the support $\mathcal S(\pi)$ with mass at least $\kappa_0$ on it. Hence $P(\text{the policies never split})\ge q(\delta)=\prod_{t\ge1}\max\{\kappa_0,1-LC_1\rho^t\delta\}$. $q(D)>0$ for $D=\mathrm{diam}\,\mathcal K_U$: finitely many factors are at least $\kappa_0$, and the remaining product converges. Also $1-q(\delta)\le LC_1\rho\delta/(1-\rho)$.
2. Meeting phase. By (H4), $P_z(\pi_m=\pi^\star)\ge\kappa_0^m$ for every $z$. With independent moves, both copies are at $\pi^\star$ after $m$ steps with probability at least $\kappa_0^{2m}$.
3. Coupling time. Alternate a meeting phase with a synchronous phase, restarting after a split. Each cycle succeeds with probability at least $p^*=\kappa_0^{2m}q(D)$, whatever happened before. A failed cycle has length $m+S$, with $P(S>j,\text{fail})\le C'\rho^j$. So for small $s>0$, $\E[e^{s\cdot\text{length}};\text{fail}]\le r<1$, and the start $\tau$ of the successful cycle satisfies $P(\tau>t)\le e^{-st}/(1-r)$.
4. Contraction. $\E d(Z_t,Z'_t)\le2P(\tau+m>t/2)+C_1D\rho^{t/2}\le C_3\beta^t$ for all $z,z'$.
5. Existence and uniqueness. $(\delta_zP^t)_t$ is Cauchy in $W_d$. Its limit is invariant because $P_\theta$ is Feller. Two invariant laws satisfy $W(\mu,\nu)=W(\mu P^t,\nu P^t)\le C_3\beta^t\to0$.
6. Lipschitz in the initial law. If $\pi=\pi'$: $\E d(Z_t,Z'_t)\le C_1\lvert p-p'\rvert+2LC_1\rho\lvert p-p'\rvert/(1-\rho)$. If $\pi\ne\pi'$: $d\ge1$, so $W\le2\le2d$. Hence $W(\nu P^t,\nu'P^t)\le M\,W(\nu,\nu')$ for every $t$.
7. Continuity in $\theta$. Telescope: $W(\mu_\theta,\mu_{\theta'})\le W(\mu_\theta P_\theta^T,\mu_{\theta'}P_\theta^T)+\sum_{s<T}W(\mu_{\theta'}P_{\theta'}^sP_\theta P_\theta^{T-1-s},\mu_{\theta'}P_{\theta'}^{s+1}P_\theta^{T-1-s})\le C_3\beta^T+TM\omega$. Choose $T=\lceil\ln(1/\omega)/\ln(1/\beta)\rceil$. Also $\omega\to0$ as $\theta'\to\theta$ by uniform continuity on compact sets, and $\omega$ is Lipschitz in $\theta$ because the maps are analytic.
8. Path laws. The finite-dimensional laws $\mu_\theta\otimes P_\theta^{\otimes k}$ converge weakly by induction, using Feller kernels with $\sup_zW(\delta_zP_\theta,\delta_zP_{\theta'})\to0$. On the compact path space this gives weak convergence of the path laws. $\square$

### Theorem 2 (world-conditional second moment)

Under (H1)-(H6): the joint stationary law of (world, chain, errors) exists and is unique, with finite second moments; $\Sigma^c(\theta):=\E[\Cov(e(t)\mid\eta)]=\tfrac12\E[(e^a-e^b)(e^a-e^b)^\top]$, where $e^a$ and $e^b$ are two replicas that share $\eta$ and are conditionally i.i.d. given $\eta$; $\Sigma^c$ is continuous on $U$, satisfies $\Sigma^c\succeq\sigma_{\min}I$, and so $\Pi^c=(\Sigma^c)^{-1}$ is continuous; $\Sigma^c$ is invariant under every relabeling of agents that leaves the kernels and the noise law invariant.

Proof.
- Stationary solution. Given the stationary policy paths, $Y_t=\sum_{k\ge0}\Phi_{t,k}\xi_{t-1-k}$ converges in $L^2$ by (H6) and is the unique stationary solution: the homogeneous part $\Phi_{t,k}Y_{t-k}\to0$.
- Two-replica identity. By (H5) the pairs ($\pi^a$, private noises $a$) and ($\pi^b$, private noises $b$) are independent of each other and of $\eta$. So $e^a$ and $e^b$ are conditionally i.i.d. given $\eta$, which gives the identity.
- Representation. $\Sigma^c=\E_{\mathbf P_\theta\otimes\mathbf P_\theta}[\Psi_\theta]$, with $\Psi_\theta=\tfrac12J(\sum_k\Phi_kN_{t-1-k}\Phi_k^\top)J^\top$ and $J$ selecting $e^a-e^b$.
- Continuity. The $k$-th term of $\Psi_\theta$ is continuous in $\theta$ and finitely many coordinates, and is bounded by $\mathrm{const}\cdot\lambda^{2k}$ uniformly on $U$. So $\Psi$ is jointly continuous and bounded. Then $\lvert\Sigma^c(\theta_j)-\Sigma^c(\theta)\rvert\le\sup\lvert\Psi_{\theta_j}-\Psi_\theta\rvert+\lvert\E_{\theta_j}\Psi_\theta-\E_\theta\Psi_\theta\rvert\to0$ by Theorem 1(c).
- Lower bound. Total covariance plus the fresh private term gives $\Sigma^c\succeq\sigma_{\min}I$.
- Symmetry. Uniqueness gives $\tau_*\mu_\theta=\mu_\theta$ for every invariance $\tau$. $\square$

### Theorem 3 (I*: selection functionals and the open-subset clause)

Lemma 3.1. For every finite $\gamma$ and both protocols, $\Sigma^c=\mathrm{blockdiag}(\Sigma_A,\Sigma_A)$ with $\Sigma_A=\alpha(\theta)I_4+\beta(\theta)\mathbf 1\mathbf 1^\top$ exactly, and $\alpha\ge q_c$. The niches have independent world components, noises and policy chains (other-niche channels carry zero gain), so the cross-niche block is zero. $S_4$ acting within each niche and the niche swap are invariances of the model; by Theorem 2 and the commutant of $S_4$, $\Sigma_A$ has the stated form.

Contrast formulas (from C1: compound-symmetric blocks). Write $x=\beta/\alpha$. For $x>0$: $a/\varepsilon=x$ and cross couplings are zero; $r(A)=1+4x$; a $k$-subset of $A$ has $r=(1+kx)/(1+(4-k)x)$, which is 1 for $k=2$ and $(1+3x)/(1+x)$ for $k=3$; every region meeting both niches has $r\le1$, because $f=(1/k\text{ on }C\cap A,-1/l\text{ on }C\cap B)$ is orthogonal to $\mathbf 1_C$ with $L_Cf=0$, so $\xi_{\mathrm{in}}\le\varepsilon\le\xi_{\mathrm{out}}$; mean-coupling baseline: $\bar a=3a/7$ with uniform leak, so $\bar r_{\mathrm{hom}}=1+(24/7)x$; mechanism medium: by the same lemma ($n=8$), $r_M=1+8x_M$; nulls: $x_{\mathrm{hab}}$, $x_{\mathrm{pr}}$ and $x_{\mathrm{lp}}$ each come from their own exactly compound-symmetric $\Sigma^c$; $N_{\mathrm{fr}}$: $x_{\mathrm{fr}}\equiv0$ under T-fast (the members' policy chains and errors are independent given $\eta$); under T-real, $x_{\mathrm{fr}}$ is a mixture term from the shared reviser clock.

Statement.
- (a) $x$, $x_M$, $x_{\mathrm{hab}}$, $x_{\mathrm{pr}}$, $x_{\mathrm{lp}}$ and $x_{\mathrm{fr}}$ are continuous on $\Theta$ (Theorem 2). Hence $r(A)$, $r_M$, $\bar r_{\mathrm{hom}}$ and every null's maximal region contrast are continuous.
- (b) $U_{\mathrm{mech}}=\{x>2x_M>0,\ (1+3x)/(1+x)<1+8x_M,\ 0<x_\nu<2x_M\text{ for }\nu\in\{\mathrm{hab},\mathrm{pr},\mathrm{lp}\},\ 1+4x_{\mathrm{fr}}<1+8x_M\}$ is open; the $x_{\mathrm{fr}}$ condition holds identically under T-fast. For $\theta\in U_{\mathrm{mech}}$ and every $r_0\in(1+8x_M,1+4x]$, the collectives at level $r_0$ are exactly $A$ and $B$, and every D-null has none, so the selected partitions differ. For $N_{\mathrm{fr}}$ under T-real this uses the reading that a null whose precision is not diffusive contains no collective, if $x_{\mathrm{fr}}<0$. $U_{3.5}=U_{\mathrm{mech}}\cap\{1+8x_M<3.5<1+4x\}$ is open. Mean-coupling reading: $U_{\mathrm{mc}}=\{x>0,\ x_\nu<(6/7)x\}$ is open; that window is nonempty whenever $x>0$.

Proof. (a) follows from Theorem 2 and the formulas. (b): a finite intersection of strict inequalities between continuous functions is open. $\square$

### Proposition 4 (agency index)

Fix finitely many decision states $X\in\mathcal K$, declared as numbers, with weights; the protocol's decision law $P_\theta(\cdot\mid X)$, which under T-fast is the (P4) law at $X$, with or without the attention component; a class with habits fixed at $E$ and $\gamma_C\in[0,\infty)$, with $G_C(\theta,X)$ continuous and nonconstant (this includes $G_C=-\tfrac12\ln(1+\lvert\sigma\rvert v_C/R_s)+\psi\lvert\sigma\rvert$). If the denominator $\sum_Xw_X\KL(P_{\theta^*}(\cdot\mid X)\Vert E)>0$, then $\Agency(\theta)$ is continuous at $\theta^*$.

Proof. $P_\theta(\cdot\mid X)$ is analytic in $\theta$ and has full support. $\KL(P\Vert P_{\gamma_C})\ge P(\sigma_{\mathrm{off}})(\gamma_C\Delta-\ln(E(\sigma_{\mathrm{off}})/E(\sigma_{\min})))-\ln\lvert\mathcal P\rvert$, where $\sigma_{\mathrm{off}}$ is a profile outside $\arg\min G_C$ and $\Delta>0$ is the gap. So KL is coercive in $\gamma_C$, uniformly near $\theta^*$. The infimum is therefore taken over a compact interval $[0,\Gamma]$ and is continuous; the denominator is continuous and positive. $\square$
