# Open Problem `open:col-extent`: Sharp Constant, Exact Homogeneous Baselines, and Diameter

- Status: active
- Opened: 2026-11-22
- Updated: 2026-11-22
- Sessions: 1

## Target

- Locked statement: Resolve all three clauses of `open:col-extent` (`sections/s04_collectives.tex`, lines 289–291): "Decide whether $\pi/\sqrt{12}$ is the supremum of $\operatorname{sd}_d(C)(r(C)-1)^{1/2}/\xi_{2,d}$ over regions and media, compute exact homogeneous baselines beyond finite searches, and bound the diameter of contrast-selected regions, which the root-mean-square extent does not control."
- Falsifier: (Clause 1) Any diffusive medium with uniform leak $\varepsilon^\Pi > 0$ and finite region $C$ ($|C| \ge 2$, $\operatorname{Var}_d(C) > 0$, $r(C) > 1$) with $Q_d(C) := \operatorname{sd}_d(C)(r(C)-1)^{1/2}/\xi_{2,d} > \pi/\sqrt{12}$ refutes $\sup Q_d = \pi/\sqrt{12}$. (Clause 2) Any finite region $C \subset \mathbb{Z}^D$ ($|C| \ge 2$) exceeding a proposed exact baseline $\bar r_{\mathrm{hom}}$, or a sequence with $\limsup r(C_k) > \bar r_{\mathrm{hom}}$, refutes that baseline. (Clause 3) Any diffusive medium and region $C$ violating a proposed diameter bound, or a family showing $\operatorname{diam}_d(C)/(\xi_{2,d}/\sqrt{r(C)-1}) \to \infty$ (refuting any $n$-independent bound), refutes the corresponding diameter claim.
- May assume: Live definitions and proved theorems in `sections/04_collectives.tex`, `sections/s04_collectives.tex`, and `sections/app04_collectives.tex` (`eq:col-diffusive`, `thm:col-diffusive-precision`, `def:col-contrast`, `def:col-baseline`, `def:col-collective`, `eq:col-second-moment`, `thm:col-lattice-contrast`, `eq:col-xi2`, `thm:col-contrast-size`, `cor:col-lstar`, `lem:col-uniform-leak`, `lem:col-box-bounds`), plus standard linear algebra (Courant–Fischer, Cauchy–Schwarz, discrete Loomis–Whitney, Stirling's lower bound).
- Must not assume: That $\pi/\sqrt{12}$ is or is not sharp; that finite-search maxima in `tab:col-baselines` equal the global suprema; that diameter is controlled by a universal constant times $\xi_{2,d}/\sqrt{r(C)-1}$; any unproved continuum limit.
- Alternative forms: (Clause 1) If $\pi/\sqrt{12}$ is refuted globally, determine the exact global supremum (and equality cases), determine whether it is attained by collectives and level-0 world-conditional precisions and by large uniform nearest-neighbor lattice regions, and identify the exact restricted class where $\pi/\sqrt{12}$ is sharp. (Clause 2) Exact global baselines for nearest-neighbor $\mathbb{Z}^D$ ($D \ge 1$) and exact global certification of all five kernels in `tab:col-baselines`. (Clause 3) Sharp universal diameter bound (both coordinate and general metric, uniform and heterogeneous leaks) plus a size-free $\mathbb{Z}^D$ lattice diameter bound and matching lower-bound families.
- Test instance: Isolated 4-site unit-weight nearest-neighbor path $C = \{0,1,2,3\} \subset \mathbb{Z}$ with uniform leak $\varepsilon^\Pi = 0.1$: $\operatorname{Var}(C) = 5/4$, $\lambda_2(L_C) = 2 - \sqrt{2} \approx 0.5857864376$, $\varsigma^2 = 2$, $\xi_2 = \sqrt{10}$, $r(C) = 1 + 10(2-\sqrt{2}) \approx 6.857864376$, and $Q(C) = \sqrt{\frac{5}{4}(2-\sqrt{2})} \approx 0.8557061686 < \pi/\sqrt{12} \approx 0.9068996821$.
- Out of scope: Non-diffusive precisions (`open:col-non-diffusive`), exact-fusion singular precisions (`open:col-exact-fusion`), record-node comparison media (`open:col-records-baseline`), and multi-block bridge brackets (`open:col-bridge`).
- Reading chosen: All three clauses are resolved at full generality over all finite regions $C$ ($|C| \ge 2$) of diffusive media (`eq:col-diffusive`) as stated in `thm:col-contrast-size`, `def:col-baseline`, and `open:col-extent`. Because $\xi_{2,d}$ is defined only for uniform leak $\varepsilon^\Pi > 0$ (`04_collectives.tex`, eq. `eq:col-xi2`), Clause 1 is evaluated in the uniform-leak class first (matching the literal formula in `open:col-extent`) and the heterogeneous-leak analogue from `thm:col-contrast-size` is also resolved explicitly in C2(4).

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| Variance normalization | Population variance $\operatorname{Var}_d(C) = \frac{1}{n}\sum_{i\in C}(x_{i,d}-\bar x_{C,d})^2$ (`app04_collectives.tex` line 206) | $C=\{0,1,2,3\}$: $\operatorname{Var}(C) = 5/4$ (sample variance $5/3$ differs by $5/12$) |
| Second moment $\varsigma_d^2$ | Global max over $V$: $\max_{i \in V}\sum_{j \in V} a^\Pi_{ij}(x_{j,d}-x_{i,d})^2$ (`eq:col-second-moment`) | Isolated $4$-site unit path: $\varsigma^2 = 2$; isolated $2$-site unit pair: $\varsigma^2 = 1$ |
| Second-moment length $\xi_{2,d}$ | Uniform leak $\varepsilon^\Pi > 0$: $\xi_{2,d}^2 = \varsigma_d^2/(2\varepsilon^\Pi)$ (`eq:col-xi2`) | Isolated $4$-site unit path, $\varepsilon^\Pi = 0.1$: $\xi_2 = \sqrt{10}$, $Q = \sqrt{\frac{5}{4}(2-\sqrt{2})} \approx 0.855706$ |
| Contrast $r(C)$ and $r_\star(C)$ | $r(C) = \varkappa_{\mathrm{in}}(C)/\varkappa_{\mathrm{out}}(C)$, $r_\star(C) = \lambda_2(L_C)/(\operatorname{cut}(C)/n)$ (`def:col-contrast`) | $\mathbb{Z}$ nn pair $\{0,1\}$, $a=1, \varepsilon^\Pi=10^{-3}$: $r = 2001/1001 \approx 1.999001$, $r_\star = 2$ |
| Level-0 passing kernel on $\mathbb{Z}^D$ | `thm:col-diffusive-precision`(e): $a_{\mathrm{ax1}} = 2ca/q$, $a_{\mathrm{ax2}} = a^2/q$, $a_{\mathrm{diag}} = 2a^2/q$, $\varepsilon^\Pi = (1-\lambda^2)/q$ | $D=2, (c,a,q)=(0.2,0.15,0.7)$: $a_{\mathrm{ax1}}=\frac{6}{70}, a_{\mathrm{ax2}}=\frac{9}{280}, a_{\mathrm{diag}}=\frac{9}{140}, \varepsilon^\Pi=\frac{18}{35}$ |

## Claims

### C1: Refutation of $\pi/\sqrt{12}$ as global supremum of $Q_d(C)$

- Statement: The constant $\pi/\sqrt{12}$ is the supremum of $Q_d(C) = \operatorname{sd}_d(C)(r(C)-1)^{1/2}/\xi_{2,d}$ over all finite regions $C$ ($|C| \ge 2$, $\operatorname{Var}_d(C) > 0$, $r(C) > 1$) and all diffusive media with uniform leak $\varepsilon^\Pi > 0$.
- Status: refuted
- Review: self
- Evidence: Counterexamples attaining $Q_d(C) = 1 > \pi/\sqrt{12} \approx 0.906900$ (isolated pair $n=2$ on $\mathbb{Z}$, $n=3$ range-2 on $\{-1,0,1\}$, hypercubes $Q_m$ for all $m \ge 1$ including exact level-0 world-conditional precisions, and a level-0 collective on a $6$-site box) and 2D isotropic uniform nearest-neighbor Gaussian spindles on $\mathbb{Z}^2$ attaining $Q_1 = 0.9463$ ($n=138$), $0.9716$ ($n=1304$) and converging to $1$; verified by two channels and negative control in `open_col_extent-checks/verify_open_col_extent.py` with captured output `open_col_extent-checks/verify_open_col_extent_output.txt`.
- Depends on: none

### C2: Exact global supremum $1$, equality characterization, and realizability

- Statement: Over all diffusive media with uniform leak $\varepsilon^\Pi > 0$ and all finite regions $C$ ($|C| \ge 2$, $\operatorname{Var}_d(C) > 0$, $r(C) > 1$), $\sup Q_d(C) = 1$. Equality $Q_d(C) = 1$ holds if and only if (i) $\operatorname{cut}(C) = 0$, (ii) $f_i = x_{i,d} - \bar x_{C,d}$ satisfies $L_C f = \lambda_2(L_C) f$, and (iii) $\sum_{j \in C} a^\Pi_{ij}(x_{i,d}-x_{j,d})^2 = \varsigma_d^2$ for every $i \in C$. Equality $Q_d(C) = 1$ is attained at $n=2$ on $\mathbb{Z}$, at $n=3$ on $\{-1,0,1\}$ with $a_{-1,0}=a_{0,1}=4, a_{-1,1}=1$, for every $n=2^m$ ($m \ge 1$) on the hypercube $Q_m$ (both for the unit nearest-neighbor Laplacian along axes and diagonal, and for the exact level-0 world-conditional precision $\Pi^c = (I-W^2)/q$ with $c \ge a > 0$ along any axis), and by a genuine collective ($r(C) = 100/19 > \bar r_{\mathrm{hom}} = 704/461$) in a reversible level-0 network on a $6$-site box. Even on $\mathbb{Z}^2$ with isotropic uniform nearest-neighbor couplings ($a^\Pi = 1$, $\varsigma_1^2 = 2$), the Gaussian-profile spindle family $C_\sigma$ ($H_0 = \lfloor \sigma^{1/2} \rfloor$, $M = \lfloor \sigma^{1/4} \rfloor$, $H_\sigma(x) = \lfloor (H_0 + \frac{1}{2})e^{-x^2/(2\sigma^2)} \rfloor$) has $|C_\sigma| \to \infty$, $\operatorname{sd}_1(C_\sigma) \sim \sigma \to \infty$, and $\lim_{\sigma \to \infty} Q_1(C_\sigma) = 1$. For heterogeneous leaks, $\sup \operatorname{sd}_d(C)(r(C)\bar\varepsilon_C - \varepsilon^{\max}_C)^{1/2}/(\varsigma_d/\sqrt{2}) = 1$, whereas replacing $\varepsilon^{\max}_C$ by $\bar\varepsilon_C$ yields an unbounded ratio already on $n=5$ vertices.
- Status: proved
- Review: self
- Evidence: Complete self-contained proof (Courant–Fischer equality audit, explicit witnesses, Thomson's principle + discrete Barta inequality on $C_\sigma$, and $n=5$ heterogeneous witness) in scratch write-up; symbolic, Lyapunov-solve, sparse 2D eigensolve, and Barta checks in `open_col_extent-checks/verify_open_col_extent.py` and `open_col_extent-checks/verify_open_col_extent_output.txt`.
- Depends on: none

### C3: Sharp supremum $\pi/\sqrt{12}$ on 1D nearest-neighbor media on $\mathbb{Z}$ with $n \ge 3$

- Statement: On $V \subseteq \mathbb{Z}$ ($x_i = i$) with arbitrary nonnegative nearest-neighbor couplings ($a^\Pi_{ij} = 0$ for $|i-j| > 1$) and uniform leak $\varepsilon^\Pi > 0$, every finite region $C \subseteq V$ with $n = |C| \ge 3$ and $r(C) > 1$ is a contiguous interval and satisfies $\lambda_2(L_C) \le \varsigma^2(1 - \cos(\pi/n))$ and $Q(C) \le \sqrt{\frac{n^2-1}{6}(1-\cos(\pi/n))} < \pi/\sqrt{12}$, with $\sup_{|C| \ge 3} Q(C) = \pi/\sqrt{12}$ approached by uniform isolated intervals as $n \to \infty$. The same strict bound $Q_d(C) < \pi/\sqrt{12}$ holds for every rectangular box $\prod_{j=1}^D \{1, \dots, \ell_j\} \subset \mathbb{Z}^D$ with $\ell_d \ge 3$ and uniform nearest-neighbor couplings.
- Status: proved
- Review: self
- Evidence: Complete 5-line LP-dual proof via $y_i = \sin(\frac{\pi(i-1)}{n})\sin(\frac{\pi i}{n})/(2\cos(\pi/n))$ ($y_1=y_n=0$, $y_k+y_{k+1}=\sin^2(\frac{\pi k}{n})$, $\sum y_i = n/4$) and Courant–Fischer on $u_i = \cos(\frac{\pi(i-1/2)}{n})$; exact symbolic verification of the dual identity ($n=3..6$), 1000 random/extreme 1D weighted path checks ($n \in [3,40]$, max $Q/Q_{\mathrm{bound}}(n) = 0.9893 \le 1$), and negative control breaking $n \ge 3$ at $n=2$ in `open_col_extent-checks/verify_open_col_extent.py` and `open_col_extent-checks/verify_open_col_extent_output.txt`.
- Depends on: none

### C4: Exact homogeneous baselines on $\mathbb{Z}^D$ for nearest-neighbor couplings, all $D \ge 1$

- Statement: (1) For any translation-invariant symmetric kernel $a^\Pi \ge 0$ on $\mathbb{Z}^D$ with finite first moment $\sum_x a^\Pi(x)\|x\|_1 < \infty$ and uniform leak $\varepsilon^\Pi > 0$, $\bar r_{\mathrm{hom}} \ge 1$, so $\bar r_{\star,\mathrm{hom}} \le 1$ implies $\bar r_{\mathrm{hom}} = 1$. (2) For nearest-neighbor coupling $a^\Pi(\pm e_d) = a > 0$ on $\mathbb{Z}^D$ with uniform leak $\varepsilon^\Pi > 0$: in $D = 1$, $\bar r_{\star,\mathrm{hom}} = 2$ and $\bar r_{\mathrm{hom}} = (\varepsilon^\Pi + 2a)/(\varepsilon^\Pi + a)$ (attained uniquely up to shift by an adjacent pair); in $D = 2$, $\bar r_{\star,\mathrm{hom}} = 1$ (attained uniquely up to shift by the $2 \times 2$ square) and $\bar r_{\mathrm{hom}} = 1$; in every $D \ge 3$, $r_\star(C) < 1$ for every finite $C \subset \mathbb{Z}^D$ ($|C| \ge 2$), so $\bar r_{\star,\mathrm{hom}} < 1$ and $\bar r_{\mathrm{hom}} = 1$ (unattained by any finite region, approached by $L^D$ boxes as $L \to \infty$).
- Status: proved
- Review: self
- Evidence: Complete analytical proof for all $D \ge 1$ via hyperplane-splitting edge-isoperimetric bound $\bar d_C \le \log_2 n$, discrete Loomis–Whitney, $D$-dimensional bathtub inertia bound $\mathsf J_C \ge \frac{D}{D+2}\omega_D^{-2/D} n^{1+2/D} - \frac{D}{12} n$, and Stirling lower bound $A_D > (2\pi e)^{-1}$ ($D \ge 3$); verified across $D=1$ ($n \le 200$, 5 leaks), all 5 free tetrominoes in $D=2$, and $D \in \{3,4,5,6,500\}$ in `open_col_extent-checks/verify_open_col_extent.py` and `open_col_extent-checks/verify_open_col_extent_output.txt`.
- Depends on: none

### C5: Exact global homogeneous baselines for all five kernels of `tab:col-baselines`

- Statement: Over all finite regions $C \subset \mathbb{Z}^D$ ($|C| \ge 2$), the exact global baselines for the five homogeneous media of `tab:col-baselines` are: (1) $\mathbb{Z}$ nn $a^\Pi = 1, \varepsilon^\Pi = 10^{-3}$: $\bar r_{\star,\mathrm{hom}} = 2$, $\bar r_{\mathrm{hom}} = 2001/1001 \approx 1.99900100$ at $\{0,1\}$; (2) $\mathbb{Z}$ passing $(0.3, 0.3), q = 1, \varepsilon^\Pi = 0.19$: $\bar r_{\star,\mathrm{hom}} = 3/2 = 1.5$, $\bar r_{\mathrm{hom}} = 55/43 \approx 1.27906977$ at $\{0,1,2\}$; (3) $\mathbb{Z}$ passing $(0.1, 0.4), q = 1, \varepsilon^\Pi = 0.19$: $\bar r_{\star,\mathrm{hom}} = (9 - \sqrt{13})/4 \approx 1.34861218$, $\bar r_{\mathrm{hom}} = (55 - 4\sqrt{13})/35 \approx 1.15936557$ at $\{0,1,2,3,4\}$; (4) $\mathbb{Z}$ passing $(0, 0.45), q = 1, \varepsilon^\Pi = 0.19$: $\bar r_{\star,\mathrm{hom}} = 2$, $\bar r_{\mathrm{hom}} = 238/157 \approx 1.51592357$ at $\{0,2\}$; (5) $\mathbb{Z}^2$ passing $(0.2, 0.15), q = 0.7, \varepsilon^\Pi = 18/35 \approx 0.51428571$: $r_\star(C) \le 0.8846 < 1$ for every finite $C \subset \mathbb{Z}^2$, hence $\bar r_{\mathrm{hom}} = 1$ (unattained by any finite region; strictly above the $4 \times 4$ search value $0.871$).
- Status: computed
- Review: self
- Scope: Rows (1) and (4) are purely analytical from C4. Rows (2) and (3) combine proved analytic tail bounds ($n \ge 7$ for $(0.3,0.3)$ giving $r_\star \le 1.3125 < 1.5$ and $r < 1.110 < 55/43$; $n \ge 9$ for $(0.1,0.4)$ giving $r_\star \le 1.215 < 1.3486$ and $r < 1.069 < 1.159$) with two-channel exhaustive enumeration of all 62 range-2 connected sets ($n \le 6$) and 254 range-2 connected sets ($n \le 8$) in float64 (tolerance $10^{-13}$) plus exact SymPy diagonalization of the maximizers. Row (5) combines the proved analytic tail bound ($n \ge 36$, $r_\star \le 0.845939 < 1$) with an exact $4$-parity composition certificate over all 82,246 compositions $(n_{00}, n_{01}, n_{10}, n_{11})$ of $2 \le n \le 35$ (integer edge bounds, float64 ratio max $0.884537 < 1$) plus a negative control on $\mathbb{Z}^2$ nearest-neighbor at $n=4$ (bound $1.0639 > 1$).
- Evidence: Analytic cutoffs + two-channel finite certificates and negative control in `open_col_extent-checks/verify_open_col_extent.py` and `open_col_extent-checks/verify_open_col_extent_output.txt`.
- Depends on: C4

### C6: Universal sharp diameter bound, sharpness of $\ln n$, and $\mathbb{Z}^D$ lattice diameter bound

- Statement: Let $\Pi = \operatorname{diag}(\varepsilon^\Pi) + L^\Pi$ be any diffusive medium (arbitrary coupling range), and let $C \subseteq V$ be a finite region with $n = |C| \ge 2$ and $\lambda_2(L_C) > 0$. (1) For every coordinate $d$ and every $u \in (0, 1)$, $\operatorname{diam}_d(C) \le \min\{\sqrt{2n},\, (\ln n + \Phi(u))/u\}\,\varsigma_d/\sqrt{2\lambda_2(L_C)}$ with $\Phi(u) = \sum_{k=0}^\infty 2^k \ln(1/(1 - u^2 4^{-k}))$, and in closed form $\operatorname{diam}_d(C) \le \sqrt{1 + 1/\ln n}\,(\ln n + \ln(1 + \ln n) + 4/3)\,\varsigma_d/\sqrt{2\lambda_2(L_C)}$; with uniform leak $\varepsilon^\Pi > 0$ and $r(C) > 1$, $\varsigma_d/\sqrt{2\lambda_2(L_C)} \le \xi_{2,d}/\sqrt{r(C)-1}$, and with heterogeneous leaks and $r(C) > \varepsilon^{\max}_C/\bar\varepsilon_C$, $\varsigma_d/\sqrt{2\lambda_2(L_C)} \le \varsigma_d/\sqrt{2(r(C)\bar\varepsilon_C - \varepsilon^{\max}_C)}$. The identical inequalities hold for $\operatorname{diam}_{\mathrm{dist}}(C)$ with $\varsigma_{\mathrm{dist}}$ in place of $\varsigma_d$ for any metric $\operatorname{dist}$ on $V$. (2) No $n$-independent bound $\operatorname{diam}_d(C) \le K\,\xi_{2,d}/\sqrt{r(C)-1}$ holds; the leading constant $1$ on $\ln n$ is sharp, approached as $\alpha \downarrow 0$ by the double exponential horn $w_k = \lfloor M e^{\alpha(R-|k|)} \rfloor$ ($M = \lceil \alpha^{-3} \rceil$, $R = \lceil \alpha^{-2} \rceil$, $\varsigma_x^2 = 2$). (3) On $\mathbb{Z}^D$ with uniform leak and $r(C) > 1$, the $D$-dimensional bathtub inertia bound gives $n \le \omega_D \bigl(\frac{D+2}{D}(\sum_{d'} \sigma_{d'}^2 + \frac{D}{12})\bigr)^{D/2}$ ($\sigma_d = \xi_{2,d}/\sqrt{r(C)-1}$), yielding the size-free lattice diameter bound $\operatorname{diam}_d(C) = O((D\ln(1 + \bar\sigma) + D\ln D)\sigma_d)$; in $D = 1$ with nearest-neighbor couplings this tightens to $\operatorname{diam}(C) < \pi \sigma_1$ ($n \ge 3$), whereas even on $\mathbb{Z}^2$ with isotropic uniform nearest-neighbor couplings $a^\Pi = 1$, the 2D exponential horn $H(x) = \lfloor (H_0 + \frac{1}{2}) e^{-\alpha|x|} \rfloor$ ($H_0 = \lfloor (4\alpha)^{-1} \rfloor$) achieves $\operatorname{diam}_1(C_\alpha) = \Theta(\sigma_1 \ln \sigma_1)$.
- Status: proved
- Review: self
- Evidence: Complete self-contained proof via $1 - 1/\cosh\Delta \le \Delta^2/2$ and Aida–Stroock MGF iteration (Part 1), Thomson + discrete Barta on the integer double exponential horn (Part 2), and bathtub inertia + 4-line summation-by-parts discrete Hardy inequality on the 2D isotropic horn (Part 3); verified on 500 diverse random/extreme graphs (coordinate, metric, heterogeneous leaks), large double horns (ratio up to $0.8637$ at $\alpha=0.02$), 2D sparse horn eigensolves vs Hardy lower bound, and planted-error negative controls ($0.49\Delta^2$ failure and 1D $\pi\sigma_1$ breakdown on 2D horn: $4.6912 > \pi$) in `open_col_extent-checks/verify_open_col_extent.py` and `open_col_extent-checks/verify_open_col_extent_output.txt`.
- Depends on: C3, C4

## Failed routes

### R1: Parabolic 1D nearest-neighbor weights $a_k = k(n-k)$ to beat $\pi/\sqrt{12}$ on $\mathbb{Z}$

- Tried: Choosing $a_k = \frac{\lambda}{2} k(n-k)$ on $\{1, \dots, n\} \subset \mathbb{Z}$ so that $f_i = i - \frac{n+1}{2}$ is an exact Fiedler eigenvector of $L_C$.
- Failed because: $\varsigma^2 = \max_i(a_{i-1} + a_i) \sim n^2/2$ is attained at the midpoint while the average $n^{-1}\sum_i (a_{i-1} + a_i) \sim n^2/3$, giving $Q(C)^2 \to 2/3 < \pi^2/12$. Indeed C3 subsequently proved that NO nearest-neighbor weight profile on $\mathbb{Z}$ ($n \ge 3$) can beat $\pi/\sqrt{12}$.
- Reopen if: The definition of $\varsigma_d^2$ is changed from $\max_i$ to the mean over $i \in C$.

### R2: Unshifted floor $H(x) = \lfloor H_0 e^{-x^2/(2\sigma^2)} \rfloor$ in the 2D Gaussian spindle Barta proof

- Tried: Defining $H(x) = \lfloor H_0 e^{-x^2/(2\sigma^2)} \rfloor$ with integer $H_0 = \lfloor \sigma^{1/2} \rfloor$ in C2(3).
- Failed because: Because $H_0$ is an exact integer, $H(1) = H_0 - 1 < H_0 = H(0)$, creating a height drop right at $x = 0 \to 1$; the Thomson step penalty $3/5$ at $y = 1$ pushed $\phi(1)/\sigma^2$ up to $1.4027 > 1$ and ruined the Barta bound at $x = 1$. Fixed by shifting to $H(x) = \lfloor (H_0 + \frac{1}{2}) e^{-x^2/(2\sigma^2)} \rfloor$, which keeps $H(x) = H_0$ flat on $[0, x_1)$ with $x_1 = \Omega(\sigma^{3/4})$.
- Reopen if: Not needed; the shifted construction resolves the issue completely.

### R3: Pointwise $(A+B)^2 \ge (1-\delta)A^2 - (\delta^{-1}-1)B^2$ reduction on 2D spindles

- Tried: Lower-bounding $E_{\mathrm{horiz}}(f)$ on a 2D spindle by expanding $((\bar f(x+1)-\bar f(x)) + (\tilde f(x+1,y)-\tilde f(x,y)))^2$ pointwise with Young's inequality.
- Failed because: It produced a negative term $-4(\delta^{-1}-1)\|\tilde f\|^2$ of order $\delta^{-1} \to \infty$ that swamped the vertical spectral gap $\lambda_2(P_{H_0}) = O(H_0^{-2}) \to 0$. Replaced by exact orthogonality on flat columns (zero loss) plus an explicit telescoping flow (Thomson's principle) on drop columns (constant factor $3/5$, using $\frac{1}{2} E_{\mathrm{vert}}$).
- Reopen if: Not needed; Thomson's principle gives an exact constant-factor reduction.

### R4: Unsplit sublattice cut bound on $\mathbb{Z}^2$ passing kernel $(c, a) = (0.2, 0.15)$

- Tried: Bounding $B_1, B_2, B_d$ independently by $\max(4\sqrt{n}, 4n - n\log_2 n)$ without tracking the $4$-parity partition $(n_{00}, n_{01}, n_{10}, n_{11})$.
- Failed because: It left 19 sizes $n \in [4, 22]$ above $r_\star = 1$ (max $1.4994$ at $n=8$), because it allowed a set to simultaneously saturate $E_1$, $E_2$, and $E_d$. Splitting into the four parity classes $(x \bmod 2, y \bmod 2)$ and bounding horizontal/vertical axis-1 edges separately dropped $\max r_\star^{\mathrm{ub}}$ to $0.8845 < 1$ for all $n \ge 2$ with zero shape enumeration.
- Reopen if: Extending C5 to small $c/a < 0.6$ on $\mathbb{Z}^2$, where parity-split sets (all sites in one parity class) require bounding single-sublattice shapes explicitly.

## Open obligations

- [ ] O1 (sessions: 1): Complete fresh-context proof verification of Claims C1–C6 by `@verifier` using the cleaned write-up, repair any located defects, and update `Review:` / `Check:` fields.

## Literature

| Claim | Source | Locator | Read depth | Date read | Verdict |
| --- | --- | --- | --- | --- | --- |
| C4 (Loomis–Whitney) | `sections/app04_collectives.tex` (citing Loomis & Whitney 1949) | Proof of `thm:col-lattice-contrast`, lines 189–191 | Exact lines | 2026-11-22 | Matches hypothesis and inequality $n^{D-1} \le \prod_d |\operatorname{pr}_d(C)|$ |
| C4, C5 (2D bathtub inertia) | `sections/app04_collectives.tex` | Proof of `lem:col-box-bounds`(U1), line 268 | Exact lines | 2026-11-22 | Matches $E_{\mathrm{h}} + E_{\mathrm{v}} \le 2n - \lceil 2\sqrt{n}\rceil$ and $\mathsf J_S \ge n^2/(2\pi) - n/6$; generalized to all $D \ge 1$ here |
| C6 (exponential MGF iteration from spectral gap) | Aida & Stroock (1994) / Bobkov & Ledoux (1997) technique | Self-contained proof derived here in C6(1) | Derived here | 2026-11-22 | Not cited as an external theorem; completely proved from elementary $1 - 1/\cosh\Delta \le \Delta^2/2$ |

## Searches

| Query | Tool | Date | Not searched |
| --- | --- | --- | --- |
| None (no novelty claims made; all results proved from first principles against manuscript definitions) | — | 2026-11-22 | External literature novelty search not required |

## Log

- 2026-11-22: Opened record for `open:col-extent`. Read `04_collectives.tex`, `s04_collectives.tex`, `app04_collectives.tex`, `chk04_collectives.tex`. Refuted $\pi/\sqrt{12}$ as global supremum (C1); proved exact supremum $1$, equality characterization, level-0/collective realizability, and 2D isotropic uniform nearest-neighbor Gaussian spindle convergence to $1$ (C2); proved exact $\pi/\sqrt{12}$ sharp supremum for 1D nearest-neighbor media on $\mathbb{Z}$ with $n \ge 3$ via LP dual (C3); proved exact nearest-neighbor baselines on $\mathbb{Z}^D$ for all $D \ge 1$ (C4) and certified exact global baselines for all 5 rows of `tab:col-baselines` (C5); proved universal sharp Aida–Stroock coordinate/metric diameter bound with exact constant $1$ on $\ln n$ (matching double exponential horn) and size-free $\mathbb{Z}^D$ lattice diameter bound with matching 2D isotropic horn (C6). Ran two-channel verification suite + planted-error negative controls (`open_col_extent-checks/verify_open_col_extent.py` -> `verify_open_col_extent_output.txt`, all passed). Next action: lint record with `check_record.py` and dispatch cleaned write-up to `@verifier` for fresh-context proof check.
