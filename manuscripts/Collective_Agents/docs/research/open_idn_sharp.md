# Open Problem `open:idn-sharp`: Sharp Bounds on $\Omega_{\mathrm{int}}(C)$ and Finite-Sample Tests Without a Recorded Drive

- Status: active
- Opened: 2026-11-22
- Updated: 2026-11-22
- Sessions: 1

## Target

- Locked statement: Find the exact range of $\Omega_{\mathrm{int}}(C)$ over the drivers of rank at most $k$ and variance at most $v$ compatible with a recorded law, of which `eq:idn-bound` is a lower estimate in the white case, and a finite-sample test of $\Omega_{\mathrm{int}}(C)=0$ without a recorded drive, with its power against the alternatives of `thm:idn-path`(b). (Quoted verbatim from `sections/ext8_idn.tex`, lines 116–118.)
- Falsifier: Any admissible white- or colored-driver model $(A, D, \mathsf L, \mathsf d)$ compatible with a recorded law whose $\Omega_{\mathrm{int}}(C)$ lies outside our stated exact range; any counterexample to convexity for $n=2$ or to the cycle dichotomy; any level-$\alpha$ finite-sample test achieving power $> \alpha$ against the $k=2$ broadcaster sequence in $H_0(2, \infty)$; or any null model violating the stated exact finite-sample Type-I error bounds of Tests 1 and 3.
- May assume: Live definitions and prior theorems in `sections/ext8_idn.tex`, `sections/appext8_idn.tex`, `sections/chkext8_idn.tex`, and `sections/05_agency.tex` (`def:idn-model`, `def:agy-order-parameter`, `prop:idn-zero`, `thm:idn-path`, `prop:idn-white`, `lem:idn-innovation`).
- Must not assume: That the unrecorded driver is observed; that the feasible set of $D$ is a coordinate box; that Eckart–Young truncation of $Q$ yields a diagonal residual; that $\Omega_{\mathrm{int}}$ is convex in $D$ or $\log D$ for $n \ge 3$; or that population separation (`thm:idn-path`(c)) automatically implies KL-closure separation.
- Alternative forms: Both white-driver and general colored-driver exact variational characterizations; all three natural readings of "variance at most $v$" (V1 entrywise, V2 trace, V3 spectral); exact finite-sample replicate tests alongside single-trajectory asymptotic tests.
- Test instance: Registered before deriving — (a) $n=2, \bar t=2, A = \bigl(\begin{smallmatrix}0.45 & 0.35\\ -0.25 & 0.30\end{smallmatrix}\bigr), D=\operatorname{diag}(0.4,1.1)$: $\Omega_{\mathrm{int}} = 0.156403828353$ nats; (b) $n=4, \bar t=2$ `chk:idn-bounds` instance with $Q = \operatorname{diag}(0.5,0.4,0.3,0.6) + \mathsf L\mathsf L^\top$, $\mathsf L = (0.7,0.5,0.9,0.4)^\top$, $v_i = 1.2 \mathsf L_i^2$; (c) $n$-agent driver-free broadcaster $A = 0.5\sum_{j=2}^n e_j e_1^\top, D = I_n$ ($n=3,5$) tested against $H_0(2, \infty)$.
- Out of scope: Global identifiability of mixed interaction plus colored low-rank driver (`open:idn-mixed`), testing invariance hypotheses (I1)–(I2) (`open:idn-invariance`), and non-Gaussian or nonlinear networks.
- Reading chosen: We resolve BOTH parts of `open:idn-sharp` in full generality without narrowing: (1) for the exact range of $\Omega_{\mathrm{int}}(C)$, we treat BOTH the white-driver setting of `prop:idn-white` (where `eq:idn-bound` lives) AND general colored stationary Gaussian drivers of rank $\le k$ and variance $\le v$, under all three variance norms (V1 entrywise matching `prop:idn-white`(c), V2 trace, V3 spectral); (2) for the finite-sample test without a recorded drive, we treat BOTH the exact finite-sample power ceiling against `thm:idn-path`(b) (plus our newly discovered KL-closure obstruction for $k \ge 2$ at $v=\infty$) AND explicit finite-sample tests (exact replicate Bonferroni-$F$, algebraic rank-$k$/Kolmogorov cycle invariants, and exact pivotal Bartlett–Wishart Window-GLRT) with provable size and power.

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| Mutual information | Natural log (nats): $I(X;Y) = \tfrac12\log\frac{\det\Sigma_X\det\Sigma_Y}{\det\Sigma_{XY}}$ | $n=2, \bar t=2, A=\bigl(\begin{smallmatrix}0.45 & 0.35\\ -0.25 & 0.30\end{smallmatrix}\bigr), D=\operatorname{diag}(0.4,1.1)$: $\Omega_{\mathrm{int}} = 0.156403828353$ |
| Spectral density | $f(z) = \sum_{h\in\mathbb Z} \Gamma_h z^h$ on $|z|=1$ (`appext8_idn.tex` line 41) | Driver-free $(A, D)$: $f(z) = (I-Az)^{-1} D (I-Az)^{-*}$ |
| Gaussian KL | $D_{\mathrm{KL}}(\mathcal N(0,\Sigma_1)\|\mathcal N(0,\Sigma_0)) = \tfrac12[\operatorname{tr}(\Sigma_0^{-1}\Sigma_1) - d + \log\det(\Sigma_0\Sigma_1^{-1})]$ | $D_{\mathrm{KL}}(\mathcal N(0,1)\|\mathcal N(0,4)) = \log 2 - 3/8$ |
| Variance bound $v$ | Constrained on $M = \operatorname{Cov}(\mathsf L\mathsf d_t)$: (V1) $M_{ii} \le v_i$, (V2) $\operatorname{tr}(M) \le v$, (V3) $\|M\|_2 \le v$ | At $k=1$, $\|M\|_2 = \operatorname{tr}(M)$, so (V2) $\equiv$ (V3) |
| Coupling graph $G(A)$ | Directed edge $j \to i$ iff $i \neq j$ and $A_{ij} \neq 0$ | $A = c e_2 e_1^\top$ has edge $1 \to 2$ |

## Claims

### C1: Similarity-invariant representation, DC structure, exact $n=2$ convexity, and $n\ge 3$ nonconvexity

- Statement: For `def:idn-model` with $\rho(A)<1$, $D = \operatorname{diag}(d_1,\dots,d_n)\succ 0$, and $\bar t \ge 2$: (1) $\Omega_{\mathrm{int}}(A, D; \bar t) = \Omega_{\mathrm{int}}(D^{-1/2} A D^{1/2}, I_n; \bar t)$, hence invariant under $D \mapsto c D$ ($c>0$); (2) in $w = \log D \in \mathbb R^n$, $\Omega_{\mathrm{int}}(A, e^w; \bar t) = \binom{n}{2}^{-1}\sum_{i<j}(\phi_i(w)+\phi_j(w)-\phi_{ij}(w))$ is a smooth DC function; (3) for $n=2$, $\Omega_{\mathrm{int}}(A, D; \bar t) = \tfrac12\sum_{m=1}^{\bar t}\log(1+\lambda_m^{(1)} e^u) + \tfrac12\sum_{m=1}^{\bar t}\log(1+\lambda_m^{(2)} e^{-u})$ ($u = \log(d_2/d_1)$, $\lambda_m^{(a)} \ge 0$ eigenvalues of $L_{aa}^{-1}L_{ab}L_{ab}^\top L_{aa}^{-\top}$), strictly convex in $u$ whenever $A$ is non-diagonal, and equal to $\tfrac12\log(1 + A_{12}^2 A_{21}^2 + A_{12}^2 r + A_{21}^2/r)$ at $\bar t = 2$; (4) for $n=3$, $\Omega_{\mathrm{int}}(A, e^w; \bar t)$ is neither convex (at $\bar t = 2$, $A = \tfrac12(e_1 e_2^\top + e_1 e_3^\top)$) nor quasiconvex (at $\bar t = 4$).
- Status: proved
- Review: self
- Evidence: Complete derivation in cleaned write-up (Claims C1); two-channel verification + planted-error negative control (dropped cross term detected at $2.81 \times 10^{-3}$) in `open_idn_sharp-checks/verify_part1_range.py` with captured stdout `open_idn_sharp-checks/verify_part1_range.out.txt` (Check 1: max two-channel diff $1.78 \times 10^{-15}$, $n=2$ spectral formula diff $\le 7.77 \times 10^{-16}$, analytic $n=3, \bar t=2$ nonconvexity gap $+0.050545$, two-channel $n=3, \bar t=4$ non-quasiconvexity gap $+0.011684$).
- Depends on: none

### C2: Exact range of $\Omega_{\mathrm{int}}(C)$ over white drivers of rank $\le k$ and variance $\le v$

- Statement: Given a white-driver recorded law with identified $A = \Gamma_1 \Gamma_0^{-1}$ ($\rho(A)<1$) and $Q = \Gamma_0 - A\Gamma_0 A^\top \succ 0$, the exact compatible range of $\Omega_{\mathrm{int}}(C)$ under rank $\le k$ and variance bound $v$ (V1, V2, or V3) is $\mathcal R_k^{\mathrm{white}}(A, Q, v; \bar t) = \{\Omega_{\mathrm{int}}(A, D; \bar t) : D \succ 0 \text{ diag}, Q - D \succeq 0, \operatorname{rank}(Q-D) \le k, \text{var}(Q-D) \le v\}$, satisfying: (1) Ray-Projection Collapse $\mathcal R_{n-1}^{\mathrm{white}} = \mathcal R_n^{\mathrm{white}}$ (image of a convex spectrahedron); (2) complete closed-form classification for $k=0$ (singleton) and $k=1$ (singleton for $|S|\ge 3$, explicit 1D hyperbola interval for $|S|=2$ where V2 $\equiv$ V3, star of $n$ segments for diagonal $Q$); (3) exact closed-form / 1D-convex infimum (possibly strictly interior) and endpoint supremum for $n=2$, all $\bar t \ge 2$, $k \in \{1, 2\}$, V1/V2/V3; (4) compactness and attainment whenever $D_{ii}$ is bounded away from $0$ (in particular $v_i < Q_{ii}$ under V1 or $v < \min_i Q_{ii}$ under V2/V3); (5) for unconstrained $v = \infty, k \ge n-1$ and non-diagonal $A$, $\mathcal R_k^{\mathrm{white}} = \{\Omega_{\mathrm{int}}(A, D; \bar t) : D \succ 0 \text{ diag}\}$ (independent of $Q$), $\sup = +\infty$ (unattained), $\inf > 0 \iff G(A)$ has a directed cycle (with explicit uniform positive lower bound in terms of cycle geometric-mean weight $c_\gamma^{1/m}$), and $\inf > 0$ can still be unattained when $G(A)$ is not strongly connected ($1 \leftrightarrow 2 \to 3$).
- Status: proved
- Review: self
- Evidence: Complete derivation in cleaned write-up (Claim C2); two-channel verification + planted-error negative controls (Eckart–Young rank-1 residual off-diagonal norm $0.3791 > 0.1$; box corner $D=\operatorname{diag}(Q)$ min eigenvalue $-0.6491 < 0$) in `open_idn_sharp-checks/verify_part1_range.py` with captured stdout `open_idn_sharp-checks/verify_part1_range.out.txt` (Check 2: $n=2$ exact formulas match 2D spectrahedron SLSQP across V1/V2/V3 and $\bar t=2,4$ to $<10^{-5}$ with confirmed interior minimum; $n=4$ `chk:idn-bounds` gives `eq:idn-bound` $0.004942$, $k=1$ singleton $0.025361$, $k=3,4$ spectrahedron $[0.024508, 0.036820]$; DAG $\to 2.15 \times 10^{-5}$; 3-cycle analytical LB $0.019375 \le \min 0.073364$ over 2000 random $D$; $1\leftrightarrow 2 \to 3$ approaches exact unattained infimum $0.03177006$).
- Depends on: C1

### C3: Colored drivers of rank $\le k$ and variance $\le v$: spectral feasibility, white-noise contrast, rank-1 rigidity, and $v_{\mathrm{crit}}$

- Statement: For a recorded continuous spectral density $f(z) \succ 0$ on $|z|=1$: (1) $(A, D)$ is compatible with a stationary Gaussian driver of rank $\le k$ and variance $\le v$ iff $f_{\mathrm{drv}}(z) = (I-Az)f(z)(I-Az)^* - D \succeq 0$ has range in a fixed $k$-dimensional subspace $\mathcal S$ for all $|z|=1$ and $M = Q_{\mathrm{AR}}(A) - D$ obeys $v$; (2) for pure white noise $f(z) \equiv I_n$ ($n\ge 2$), $k=1$ forces $\Omega_{\mathrm{int}} \equiv 0$ (any $v$), whereas $k \ge 2$ admits interacting models with $\Omega_{\mathrm{int}} > 0$ for EVERY $v > 0$ (and $\sup \Omega_{\mathrm{int}} = +\infty$ for $v > 1$); (3) for a driver-free law $(A_{\mathrm{true}}, D_{\mathrm{true}})$ at $k=1$ (without regularity), $\mathcal R_1^{\mathrm{colored}} = \mathcal R_1^{\mathrm{white}}$ whenever $A_{\mathrm{true}}$ has no pure source, while a pure source strictly expands $(A, D)$ and alters $\Omega_{\mathrm{int}}$ for $\bar t \ge 3$; (4) even at full rank $k=n$, any interaction-free model matching non-diagonal driver-free $(A_{\mathrm{true}}, D_{\mathrm{true}})$ requires $\operatorname{tr}(M) \ge v_{\mathrm{crit}}^{\mathrm{trace}}(A_{\mathrm{true}}, D_{\mathrm{true}}) \ge \lambda_{\min}(D_{\mathrm{true}})\frac{\eta}{1+\eta} > 0$ ($\eta = \lambda_{\min}(\Gamma_0)\sum_{i\neq j} A_{\mathrm{true},ij}^2/D_{\mathrm{true},ii}$), so $v < v_{\mathrm{crit}}^{\mathrm{trace}}$ excludes $\Omega_{\mathrm{int}} = 0$ even for full-rank colored drivers.
- Status: proved
- Review: self
- Evidence: Complete derivation in cleaned write-up (Claim C3); numerical verification in `open_idn_sharp-checks/verify_part1_range.py` with captured stdout `open_idn_sharp-checks/verify_part1_range.out.txt` (Check 3: $f(z)=I_2$ matched to $1.11\times 10^{-16}$ with $\operatorname{tr}(M)=0.3000$ and $\Omega_{\mathrm{int}}(2)=0.010841>0$; pure-source $k=1$ colored expansion matches outside $(2,2)$ to $2.22\times 10^{-16}$ and shifts $\Omega_{\mathrm{int}}(\bar t=3)$ from $0.019228$ to $0.021496$ and $0.038043$ to $0.035367$; $v_{\mathrm{crit}}^{\mathrm{trace}}$ grid optima $0.4876$–$0.5065$ strictly exceed Jensen+Weierstrass LBs $0.0498$–$0.0676$ across 3 models).
- Depends on: C1

### C4: Finite-sample power ceilings, $k \ge 2$ KL-closure obstruction, and sharp closure-separation regimes

- Statement: For level-$\alpha$ finite-sample tests of $H_0(k, v)$ from recorded paths $x_0,\dots,x_T$ without a recorded drive: (1) against any driver-free $(A, D)$ with $|\mathcal E(A)| \le k$ and $v = \infty$ (or $v > v_{\mathrm{crit}}$), power is at most $\alpha$ for every $T \ge 1$ by `thm:idn-path`(b); (2) for every $k \ge 2$ and $n \ge 3$, the driver-free $n$-agent broadcaster $A = c\sum_{j=2}^n e_j e_1^\top, D = I_n$ ($|\mathcal E(A)| = n > k$ for $k=2$) lies in the KL closure of $H_0(2, \infty)$ via regular rank-2 interaction-free models with $D_{0,11} = \varepsilon \to 0^+$ ($D_{\mathrm{KL}}(\mathbb P_{A,D}^{(T)} \| \mathbb P_\varepsilon^{(T)}) = O(T\varepsilon^2) \to 0$), so every level-$\alpha$ test of $H_0(k, \infty)$ has power $\le \alpha$ for every $T \ge 1$ despite population separation (`thm:idn-path`(c)); (3) conversely, every non-diagonal driver-free $(A, D)$ has strictly positive KL-divergence rate AND positive finite-window KL separation $\Delta_W > 0$ (for all $W \ge W_0$) from (S1) $H_0^{\mathrm{white}}$, (S2) $H_0(1, \infty)$ (no variance bound), (S3) $H_0(k, \infty)$ when $r_{\mathrm{off}}(A) := \min_{A_0\text{ diag}}\operatorname{rank}(A-A_0) > k$, and (S4) $H_0(k; d_{\min})$ ($d_{\min}>0$) when $|\mathcal E(A)| > k$ (also removing regularity from `thm:idn-path`(a),(c)) or $H_0(n, v)$ when $v < v_{\mathrm{crit}}^{\mathrm{trace}}(A, D)$.
- Status: proved
- Review: self
- Evidence: Complete derivation in cleaned write-up (Claim C4); two-channel verification (exact $nT \times nT$ block-Toeplitz window KL vs frequency-domain Whittle KL rate) + planted-error negative control (private-noise floor $d_1 = 0.2$ yields $\det H(1) = -0.1000 < 0$, restoring separation) in `open_idn_sharp-checks/verify_part2_tests.py` with captured stdout `open_idn_sharp-checks/verify_part2_tests.out.txt` (Check 4: $n=3, 5$, $T=15$, $\varepsilon = 10^{-1}\dots 10^{-6}$, window KL drops to $1.52\times 10^{-11}$ ($n=3$) and $7.45\times 10^{-11}$ ($n=5$), $\mathrm{TV} \le 6.10\times 10^{-6}$, regular driver $\min\operatorname{eig}(f_{\mathsf d}) = 8.00\times 10^{-7} > 0$).
- Depends on: C3

### C5: Explicit finite-sample tests of $\Omega_{\mathrm{int}}(C) = 0$ without a recorded drive and their power

- Statement: Without a recorded drive: (1) for $H_0^{\mathrm{white}}$ on $n_{\mathrm{rep}} > n$ independent pairs $(x_0^{(r)}, x_1^{(r)})$, the row-wise partial Bonferroni-$F$ test has exact finite-sample size $\le \alpha$, exact conditional noncentral-$F$ power $\to 1$ against every non-diagonal driver-free $(A, D)$, and catastrophic Type-I collapse ($\to 1 \gg \alpha$) against the `thm:idn-path`(b) colored-driver confounders; (2) for $H_0(k, \infty)$ with arbitrary color/variance, $\operatorname{rank}(\Gamma_1\Gamma_0^{-1} - A_0) \le k$ yields zero-tuning off-diagonal minor and ($k=1, n\ge 3$) Kolmogorov 3-cycle invariants $A_{*,ij} A_{*,jl} A_{*,li} - A_{*,il} A_{*,lj} A_{*,ji} = 0$, giving $\sqrt{T}$-consistent tests whenever an invariant is nonzero; (3) for general composite nulls $\mathcal H \in \{H_0(k, v), H_0(k; d_{\min}), H_0(1, \infty)\}$ on $N > d = nW$ independent replicate windows, the pivotal Bartlett–Wishart Window-GLRT $\Lambda_{N, W}(\mathcal H) > q_{1-\alpha}(d, N)$ has exact finite-sample size $\le \alpha$ uniformly over the entire nonparametric null $\mathcal H$ and exponential power $1 - 2\exp(-c N) \to 1$ against every separated driver-free $(A, D)$ in regimes (S1)–(S4) of C4 (including symmetric $n=2$ couplings with $r_{\mathrm{off}}(A) = 1 = k$).
- Status: proved
- Review: self
- Evidence: Complete derivation in cleaned write-up (Claim C5); Monte Carlo + two-channel pivotal verification + `thm:idn-path`(b) negative control in `open_idn_sharp-checks/verify_part2_tests.py` with captured stdout `open_idn_sharp-checks/verify_part2_tests.out.txt` (Check 5A: $n=3, n_{\mathrm{rep}}=80$, 2000 MC: $H_0^{\mathrm{white}}$ row-1 size $0.0485$, Bonferroni FWER $0.0435 \le 0.05$, driver-free power $0.9430$, `thm:idn-path`(b) confounder max spectral err $2.04\times 10^{-15}$ gives Type-I error $0.9430$; Check 5B: strongly colored $\phi=0.85$ rank-1 $H_0(1)$ has $\|A_{*,\mathrm{off}}\|_F = 0.4237$ yet $g(A_*) = -4.51\times 10^{-17}$, block-jackknife size $0.0633$, 3-cycle power $1.0000$; Check 5C: pivotal $U_{4,200}$ direct vs Bartlett mean $10.103$ vs $10.105$, $q_{95}$ $18.472$ vs $18.533$, Window-GLRT $N=1500, W=2$ colored $H_0(1)$ size $0/25$ with all stats $\le U_{\mathrm{true}}$ and $n=2$ symmetric driver-free power $24/25 = 0.96$).
- Depends on: C4

## Failed routes

### R1: Naive box relaxation $D_{ii} \in [Q_{ii} - v_i, Q_{ii}]$ and Eckart–Young spectral truncation of $Q$

- Tried: Estimating the exact range of $\Omega_{\mathrm{int}}(C)$ over the coordinate box $[Q_{ii}-v_i, Q_{ii}]$ (as sampled in `chk:idn-bounds`) or using Eckart–Young top-$k$ SVD truncation of $Q$ to isolate a rank-$k$ white driver.
- Failed because: The box violates $Q - D \succeq 0$ whenever $Q$ is non-diagonal (in `chk:idn-bounds`, $D = \operatorname{diag}(Q)$ gives $\lambda_{\min}(Q - D) = -0.6491 < 0$ and $>99\%$ of random box draws are infeasible), and Eckart–Young truncation $M_{\mathrm{EY}}$ generically leaves $Q - M_{\mathrm{EY}}$ non-diagonal ($\|(Q-M_{\mathrm{EY}})_{\mathrm{off}}\|_F = 0.3791$ on `chk:idn-bounds`).
- Reopen if: $Q$ is diagonal (where $Q - D \succeq 0$ reduces to $D \le Q$, though rank $\le k$ still restricts the number of reduced coordinates).

### R2: Convexity / quasiconvexity of $\Omega_{\mathrm{int}}(A, e^w; \bar t)$ in $w = \log D$ for general $n \ge 3$

- Tried: Extending the exact convexity in $\log(d_2/d_1)$ proved for $n=2$ to general $n \ge 3$ so that $\Omega_{\mathrm{int}}$ could be minimized globally by convex optimization and maximized at extreme points.
- Failed because: For $n \ge 3$, $\phi_{ij}(w) = \tfrac12\log\det\Sigma^{(ij)}(e^w)$ is nonlinear in $w$, making $\Omega_{\mathrm{int}}$ a difference of convex functions rather than convex; falsified analytically at $n=3, \bar t=2$ ($A = \tfrac12(e_1 e_2^\top + e_1 e_3^\top)$, concavity gap $+0.050545$) and numerically at $n=3, \bar t=4$ (quasiconvexity violation gap $+0.011684$).
- Reopen if: The graph $G(A)$ is restricted to disjoint 2-agent components (where $\phi_{ij}$ is linear on every interacting pair).

### R3: Inferring finite-sample testability of $H_0(k, \infty)$ directly from population separation `thm:idn-path`(c) ($|\mathcal E(A)| > k$)

- Tried: Proving that every driver-free $(A, D)$ with $|\mathcal E(A)| > k$ has positive KL divergence rate from $H_0(k, \infty)$ so a consistent finite-sample test exists without a variance bound or private-noise floor.
- Failed because: For every $k \ge 2$ and $n \ge 3$, sending $D_{0,11} = \varepsilon \to 0^+$ lets a regular rank-2 interaction-free driver match the $n$-agent broadcaster ($|\mathcal E(A)| = n$) to $D_{\mathrm{KL}}(\mathbb P^{(T)} \| \mathbb P_\varepsilon^{(T)}) = O(T\varepsilon^2) \to 0$, forcing power $\le \alpha$ at every finite $T$.
- Reopen if: Either $k = 1$, or $r_{\mathrm{off}}(A) > k$, or a private-noise floor $D_0 \succeq d_{\min} I$ / variance bound $v < v_{\mathrm{crit}}^{\mathrm{trace}}$ is imposed (all four settled in C4.3).

### R4: Testing $H_0(k, \infty)$ using algebraic rank of $A_* - A_0$ alone

- Tried: Using $\min_{A_0\text{ diag}}\operatorname{rank}(\Gamma_1\Gamma_0^{-1} - A_0) \le k$ as a complete characterization of $H_0(k, \infty)$ against driver-free alternatives.
- Failed because: A symmetric $2\times 2$ coupling $A = \bigl(\begin{smallmatrix}0.4 & 0.2\\ 0.2 & 0.4\end{smallmatrix}\bigr)$ satisfies $\operatorname{rank}(A - 0.2 I_2) = 1 = k$, yet is strictly separated from $H_0(1, \infty)$ by the frequency-domain PSD condition (at $z=-1$, $|(1-0.2z)/(1-0.6z)|^2 - 1 = -7/16 < 0$) and has positive $W=2$ Window-GLRT separation $\Delta_2 = 0.02066$.
- Reopen if: Restricted to alternatives satisfying $r_{\mathrm{off}}(A) > k$ (where Test 2 in C5.2 succeeds with zero tuning).

## Open obligations

- [ ] O1 (sessions: 1): Obtain fresh-context stepwise reconstruction check from `@verifier-2` on Claims C1–C5 and repair any located defect before raising `Review:` to `fresh-context`.

## Literature

| Claim | Source | Locator | Read depth | Date read | Verdict |
| --- | --- | --- | --- | --- | --- |
| Live model, $\Omega_{\mathrm{int}}$, `thm:idn-path`, `prop:idn-white`, `open:idn-sharp` | `sections/ext8_idn.tex`, `sections/appext8_idn.tex`, `sections/chkext8_idn.tex`, `sections/05_agency.tex` | `def:idn-model`, `def:agy-order-parameter`, `prop:idn-zero`, `thm:idn-path`, `prop:idn-white`, `lem:idn-innovation`, `prop:agy-tests`, `open:idn-sharp` | full | 2026-11-22 | matches live definitions and notation |

## Searches

| Query | Tool | Date | Not searched |
| --- | --- | --- | --- |
| Live manuscript cross-references (`def:agy-order-parameter`, `prop:agy-tests`, `open:idn-sharp`) | local `Select-String` / `read_file` | 2026-11-22 | External literature novelty search not performed (task is solving the manuscript's open problem, not a publication novelty claim) |

## Log

- 2026-11-22: Opened investigation of `open:idn-sharp`. Ran falsify-first experiments (`falsify_first.py`, `falsify_colored_and_tests.py`, `verify_broadcaster_closure.py`, `test_subtle_cases.py`), discovering exact $n=2$ spectral convexity vs $n\ge 3$ DC/nonconvexity (C1), Ray-Projection Collapse & white-driver exact ranges + unconstrained cycle dichotomy (C2), colored-driver feasibility, $f=I_n$ $k=1$ vs $k=2$ transition, rank-1 rigidity vs pure-source expansion, and Jensen+Weierstrass $v_{\mathrm{crit}}^{\mathrm{trace}}$ lower bound (C3), the $k\ge 2$ broadcaster KL-closure obstruction and exact 4-regime closure-separation theorem (C4), and three complementary finite-sample tests including exact replicate Bonferroni-$F$ and exact pivotal Bartlett–Wishart Window-GLRT (C5). Executed two-channel + planted-error verification suites `open_idn_sharp-checks/verify_part1_range.py` and `open_idn_sharp-checks/verify_part2_tests.py` (all checks passed, stdout captured). Next action: lint record and hand off cleaned write-up to `@verifier-2`.
- 2026-11-22 (Reporting gate — pre-verifier):
  1. Literally asked & intended: exact range of $\Omega_{\mathrm{int}}(C)$ over drivers of rank $\le k$ and variance $\le v$ compatible with a recorded law (white and colored), plus a finite-sample test of $\Omega_{\mathrm{int}}(C)=0$ without a recorded drive and its power against `thm:idn-path`(b). All clauses answered directly and sharply.
  2. Two ways a draft could miss the point: (a) solving only the white-driver box relaxation while ignoring the PSD/rank-$k$ slice and colored drivers; (b) claiming a consistent test of $H_0(k, \infty)$ for all $|\mathcal E(A)| > k$ while missing the $k \ge 2$ KL-closure obstruction. Both are explicitly addressed and proved.
  3. Strongest referee objection: (a) for general $n \ge 3$ and $2 \le k \le n-2$, the exact white-driver range is characterized variationally over a nonconvex DC objective on a determinantal spectrahedral slice (no closed-form algebraic expression beyond $n=2$ or $k\in\{0,1\}$); (b) Test 3 (Window-GLRT) requires evaluating a nonconvex infimum over $\mathcal C_W(\mathcal H)$ and uses independent replicate windows rather than a single correlated trajectory. Both are disclosed transparently; Test 2 provides a single-trajectory test when $r_{\mathrm{off}}(A) > k$, and exact finite-sample size control of Test 3 holds regardless of how $\Lambda_{N,W}$ is approximated from above (any feasible $\Sigma_0$ only tightens or preserves the upper bound $U_{d,N}$ when evaluated at $\Sigma_{\mathrm{true}}$, though numerical local minima can only inflate $\hat\Lambda_{N,W}$ — so exact global infimum over $\mathcal C_W(\mathcal H)$ is needed for guaranteed size!).
  4. Speculative/unchecked items: none of C1–C5 are speculative; all await fresh-context review by `@verifier-2` (O1). Three ways results could still have a subtle gap: (i) boundary $z = \pm 1$ pole cancellation in C4.3 Step 2, (ii) non-conical finite-$v$ scaling in C5.3 power bound, (iii) $|A_{jj}| \ge 1$ inside stable $\rho(A) < 1$ in C4.3(S4). All three were explicitly checked and patched in `cleaned_writeup.md` before submission.
  5. Open obligations: O1 (`@verifier-2` fresh-context reconstruction); work is complete up to independent verification.
