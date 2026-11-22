# Exact Second Moment of the Understanding Error (`open:lrn-noncentral`)

- Status: closed
- Opened: 2026-11-22
- Updated: 2026-11-22
- Sessions: 1

## Target

- Locked statement: From `sections/ext5_lrn.tex` (`open:lrn-noncentral`, lines 143-145): "For $K \ge r_c + 2$, find $\mathbb{E}[\psi\psi^\top]$ in closed form as a function of $\sigma_H$. `prop:lrn-understanding-expansion` gives it to second order and `eq:lrn-understanding-bound` bounds it; neither is sharp at moderate $\sigma_H$." Specifically, derive the exact closed form of $\mathbb{E}[\psi\psi^\top]$ as a function of $\sigma_H$ and all model parameters $(K, r_c, P, H, m_i, u, R_c)$, check its asymptotics against `prop:lrn-understanding-expansion`, check exact edge cases ($K = r_c + 2$, $\sigma_H \to 0$, $\sigma_H \to \infty$, $r_c = 1$), determine whether an elementary closed form or hypergeometric/special-function representation is exact, and verify whether $\mathbb{E}[\psi\psi^\top]$ diverges for $K \le r_c + 1$.
- Falsifier: Any admissible instance ($K \ge r_c + 2$, $P \in \mathcal{S}_K^{++}$, full-row-rank $H \in \mathbb{R}^{r_c \times K}$, $R_c \in \mathcal{S}_{r_c}^{+}$, $\sigma_H > 0$, finite second moments for $(m_i, u)$) where the derived exact formula disagrees with direct evaluation of $\mathbb{E}[\psi\psi^\top]$ beyond numerical/Monte Carlo tolerance, fails to reproduce `prop:lrn-understanding-expansion` as $\sigma_H \to 0$, or where an elementary closed form is constructed for an instance claimed to be non-elementary.
- May assume: Definitions and proved lemmas/theorems in `sections/ext5_lrn.tex`, `sections/appext5_lrn.tex` (`lem:lrn-inverse-norm`, `lem:lrn-schur`, `lem:lrn-isserlis`, `thm:lrn-understanding-moment`, `prop:lrn-understanding-expansion`), and `sections/s02_framework.tex` (`eq:fw-two-errors`).
- Must not assume: An elementary closed form exists; $P = p I_K$ when making general-$P$ claims; $r_c = 1$ when making general-$r_c$ claims; perturbative expansions as exact identities; unchecked literature formulas for noncentral Wishart inverse moments.
- Alternative forms: (1) Exact elementary/hypergeometric closed form where one exists (isotropic $r_c = 1$: single ${}_1F_1$ function, elementary for even $K \ge 4$ and Dawson integral for odd $K \ge 3$); (2) Exact finite-dimensional closed-form integral representation over $\mathcal{S}_{r_c}^{++}$ of dimension $r_c(r_c+1)/2$ independent of $K$ (1D integral for $r_c = 1$, general $P \succ 0$; 3D for $r_c = 2$, general $P \succ 0$); (3) Exact non-perturbative Stein representation; (4) Rigorous proof of non-elementarity obstructions explaining why no general elementary formula exists.
- Test instance: Registered before deriving full general-$r_c$ theory: (a) $r_c = 1, K = 3$, isotropic $P = 1.9 I_3$, $H = (1.1, -0.85, 0.6)$, $m_i = (0.6, 0.3, 0.0)^\top$, $u = -0.75$, $R_c = 0.42$, $\sigma_H = 0.58$ (exact $\mathbb{E}[\psi^2] = 0.559329501770$); (b) $r_c = 2, K = 6$, generic non-diagonal anisotropic $P = L L^\top$, non-symmetric $H$, nonzero $(m_i, u, R_c)$, $\sigma_H = 0.6$ (exact $\mathbb{E}[\psi\psi^\top] = [[1.707475, -0.580748], [-0.580748, 0.811520]]$).
- Out of scope: Truncated moments on $\{\sigma_H \|W\|_F \le \rho\}$ for $K \le r_c + 1$; regularized gains $\hat{\mathsf{K}} = P \hat H^\top (\hat H P \hat H^\top + \hat R)^{-1}$ (mentioned in `open:fw-understanding-risk`, not `open:lrn-noncentral`); non-Gaussian code errors $W$.
- Reading chosen: Full exact characterization of $\mathbb{E}[\psi\psi^\top]$ for all $K \ge r_c + 2$, all $r_c \ge 1$, and all $P \succ 0$ (both conditional on fixed $(m_i, u)$ as in `prop:lrn-understanding-expansion` and unconditional via $\mathbb{E}_{(m_i,u)}$ as in `thm:lrn-understanding-moment`), including both exact closed-form/integral representations and rigorous non-elementarity obstructions, rather than restricting silently to $r_c = 1$ or $P = p I_K$.

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| Lebesgue measure on $\mathcal{S}_r^{++}$ | $dT = \prod_{1 \le i \le j \le r} dT_{ij}$ | $\int_{T \succ 0} (\det T)^{m-(r+1)/2} e^{-\operatorname{tr}(T)}\,dT = \Gamma_r(m)$ |
| Multivariate gamma $\Gamma_r(m)$ ($m > \frac{r-1}{2}$) | $\pi^{r(r-1)/4} \prod_{i=1}^r \Gamma(m - \frac{i-1}{2})$ | $\Gamma_2(1) = \pi = 3.141592653590$, $\Gamma_2(2) = \pi/2 = 1.570796326795$ |
| Confluent hypergeometric function $f_\alpha(\lambda)$ | $f_\alpha(\lambda) = \int_0^1 (1-v)^{\alpha-1} e^{-\lambda v}\,dv = \frac{1}{\alpha}\,{}_1F_1(1; \alpha+1; -\lambda)$ | $f_1(1) = 1 - e^{-1} = 0.632120558829$, $f_{1/2}(1) = 2 F(1) = 1.076159013826$ |
| Dawson's integral $F(x)$ | $F(x) = e^{-x^2}\int_0^x e^{t^2}\,dt$ | $F(1) = 0.538079506913$ |
| Hyperbolic sine integral $\operatorname{Shi}(x)$ | $\operatorname{Shi}(x) = \int_0^x \frac{\sinh t}{t}\,dt$ | $\operatorname{Shi}(1) = 1.057250875355$ |
| Carlson elliptic integrals ($x, y, z > 0$) | $R_F(x,y,z) = \frac{1}{2}\int_0^\infty [(t+x)(t+y)(t+z)]^{-1/2}\,dt$, $R_D(x,y,z) = \frac{3}{2}\int_0^\infty [(t+x)(t+y)(t+z)^3]^{-1/2}\,dt$ | $R_F(1,1,1) = 1$, $R_D(1,1,1) = 1$ |
| `prop:lrn-understanding-expansion` bracket $B_{\mathrm{prop}}$ | $\mathbb{E}\|\hat m_0\|^2 I_{r_c} - \operatorname{tr}(P_0^+)(R_c S_0^{-1} + S_0^{-1} R_c) + R_c O_0^\top O_0 + O_0^\top O_0 R_c$ | At $r_c=1, K=4, P=pI_4, \|H\|=1, m_i=0, u=0, R_c=1$: $B_{\mathrm{prop}} = 5 - 2K = -3.0$ |

## Claims

### C1: Exact non-perturbative Stein identity and $\mathbb{E}[\psi\psi^\top]$ representation

- Statement: For all $K \ge r_c + 2$, $r_c \ge 1$, $P \in \mathcal{S}_K^{++}$, full-row-rank $H \in \mathbb{R}^{r_c \times K}$, $R_c \in \mathcal{S}_{r_c}^{+}$, $\sigma_H > 0$, and fixed $(m_i, u)$ (or random $(m_i, u)$ with finite second moments independent of $(W, \nu)$), with $\psi_0 = H(I_K - O\hat H)m_i + (HO - I_{r_c})u$, $S = \hat H P \hat H^\top$, and $P^+(\hat H) = P - O\hat H P$: (1) $\mathbb{E}[\psi\psi^\top \mid m_i, u] = \mathbb{E}_W[\psi_0\psi_0^\top] + \mathbb{E}_W[H O R_c O^\top H^\top]$; (2) $I_{r_c} - \mathbb{E}[HO] = \sigma_H^2 \mathbb{E}[\operatorname{tr}(P^+(\hat H)) S^{-1} - O^\top O]$, so $\mathbb{E}[HO]$ is always symmetric and reduces to $I_{r_c} - \mathbb{E}[HO] = \sigma_H^2 (K - r_c - 1)\mathbb{E}[(\hat H\hat H^\top)^{-1}]$ when $P = p I_K$; (3) $\mathbb{E}[\psi\psi^\top \mid m_i, u] = R_c + \sigma_H^2 \mathbb{E}[W\hat m\hat m^\top W^\top - \operatorname{tr}(P^+(\hat H))(R_c S^{-1} + S^{-1} R_c) + R_c O^\top O + O^\top O R_c \mid m_i, u]$.
- Status: proved
- Review: fresh-context
- Check: verifier (#39), 2026-11-22, fresh-context reconstruction from `cleaned_writeup.md` + independent verification script, no defect located.
- Evidence: Complete derivation via regularized gain $O_\delta$ and Dominated Convergence in `C:\Users\chris and christine\.gemini\antigravity\brain\2b88195c-b147-483c-a266-afea6a54c14c\scratch\swarm_lrn_noncentral\cleaned_writeup.md` (Claim C1); two-channel verification in `open_lrn_noncentral-checks/verify_open_lrn_noncentral.py` and `open_lrn_noncentral-checks/verify_open_lrn_noncentral.txt` (CHECK 2, anisotropic $K=6, r_c=2$, 250k draws: Stein identity max $|z|=1.05$, $\max|\mathbb{E}[HO]-\mathbb{E}[HO]^\top|=3.96\times 10^{-4}$, full Stein form max $|z|=0.94$; negative control flipping $-O^\top O \to +O^\top O$ fails with gap $0.2819 > 0.05$).
- Depends on: none

### C2: Exact Matrix-Laplace (Schwinger) integral representation for general $r_c \ge 1, K \ge r_c + 2, P \succ 0$

- Statement: For all $K \ge r_c + 2$, $r_c \ge 1$, $P = Q_P \operatorname{diag}(p_1, \dots, p_K) Q_P^\top \in \mathcal{S}_K^{++}$, full-row-rank $H \in \mathbb{R}^{r_c \times K}$, $R_c \in \mathcal{S}_{r_c}^{+}$, $\sigma_H > 0$, and fixed $(m_i, u)$, setting $s_k = \sigma_H^2 p_k$, $\bar H = H P^{1/2} Q_P$, $\bar z = Q_P^\top P^{-1/2} m_i$, $c_0 = Hm_i - u$, $m_1 = \lceil r_c/2 \rceil$, and $m_2 = \max(2, \lceil r_c/2 \rceil)$, $\mathbb{E}[\psi\psi^\top \mid m_i, u]$ equals $c_0 c_0^\top$ plus the sum of two absolutely convergent integrals over the $\frac{r_c(r_c+1)}{2}$-dimensional cone $\mathcal{S}_{r_c}^{++}$ (dimension independent of $K$) with weights $\Gamma_{r_c}(m_j)^{-1} (\det T)^{m_j - (r_c+1)/2} Z(T)$ multiplying explicit polynomial expectations $\mathbb{E}_T[\cdot]$ of $K$ independent tilted Gaussian columns $\bar g_k \sim \mathcal{N}((I_{r_c} + 2 s_k T)^{-1}\bar h_k,\, s_k(I_{r_c} + 2 s_k T)^{-1})$.
- Status: proved
- Review: fresh-context
- Check: verifier (#39), 2026-11-22, fresh-context reconstruction from `cleaned_writeup.md` + independent verification script, no defect located.
- Evidence: Complete self-contained derivation (including proof of the Siegel multivariate gamma identity and Tonelli/Fubini justification) in `C:\Users\chris and christine\.gemini\antigravity\brain\2b88195c-b147-483c-a266-afea6a54c14c\scratch\swarm_lrn_noncentral\cleaned_writeup.md` (Claim C2); two-channel verification in `open_lrn_noncentral-checks/verify_open_lrn_noncentral.py` and `open_lrn_noncentral-checks/verify_open_lrn_noncentral.txt` (CHECK 3, deterministic spectral quadrature vs 300k-draw direct MC: at anisotropic $K=6, r_c=2$, quad conv $2.27\times 10^{-7}$, max $|z|=0.66$; at edge anisotropic $K=4, r_c=2$, quad conv $5.15\times 10^{-8}$, rel diff $0.0129$; negative control doubling $\Gamma_2(2)$ fails with gap $1.8854 > 0.2$).
- Depends on: C1

### C3: Exact $r_c = 1$ closed forms (general $P \succ 0$ 1D integral and isotropic $P = p I_K$ single-${}_1F_1$ / elementary formula)

- Statement: For $r_c = 1$, $K \ge 3$, $P \in \mathcal{S}_K^{++}$, $H \neq 0$, $R_c \ge 0$, $\sigma_H > 0$, and fixed $(m_i, u)$: (a) for general $P \succ 0$, $\mathbb{E}[\psi^2 \mid m_i, u]$ equals $c_0^2$ plus an explicit 1D Schwinger integral over $t \in (0, \infty)$ of $Z(t)$ times explicit bivariate-Gaussian moment polynomials $(E_X, E_{XY}, E_{X^2}, E_{X^2 Y}, E_{X^2 Y^2})$; (b) for isotropic $P = p I_K$, $\mathbb{E}[\psi^2 \mid m_i, u]$ is independent of $p$ and equals $c_R(\lambda) R_c + c_u(\lambda) u^2 + c_\parallel(\lambda)(Hm_i)^2 + c_\perp(\lambda)\|H\|^2\|m_\perp\|^2 + 2 c_{\parallel u}(\lambda)(Hm_i)u$ with $\lambda = \|H\|^2/(2\sigma_H^2)$, where all five coefficients are explicit rational functions of $\lambda$ and the single confluent hypergeometric function $f_0 = f_{K/2-1}(\lambda) = \frac{1}{K/2-1}\,{}_1F_1(1; K/2; -\lambda)$ (via $f_1 = (1 - (K/2-1)f_0)/\lambda$, $f_2 = (1 - (K/2)f_1)/\lambda$). At edge $K = 3$, $f_0 = \frac{2}{\sqrt{\lambda}} F(\sqrt{\lambda})$, $c_R(\lambda) = 1 - F(\sqrt{\lambda})/\sqrt{\lambda} \in (0, 1)$, and $c_u(\lambda) = 1 - c_R(\lambda)$; for every even $K = 2m + 2 \ge 4$, $f_0$ and hence $\mathbb{E}[\psi^2 \mid m_i, u]$ are elementary (at $K = 4$, $c_R = 1 + \frac{1}{2}e^{-\lambda} - \frac{3(1-e^{-\lambda})}{2\lambda}$, $c_u = \frac{1}{2}e^{-\lambda} + \frac{1-e^{-\lambda}}{2\lambda}$).
- Status: proved
- Review: fresh-context
- Check: verifier (#39), 2026-11-22, fresh-context reconstruction + independent SymPy and quadrature check (`K=3` diff `1.18e-14`), no defect located.
- Evidence: Complete derivation (Isserlis specialization of C2 + independent Poisson-Beta mixture derivation) in `C:\Users\chris and christine\.gemini\antigravity\brain\2b88195c-b147-483c-a266-afea6a54c14c\scratch\swarm_lrn_noncentral\cleaned_writeup.md` (Claim C3); multi-channel verification in `open_lrn_noncentral-checks/verify_open_lrn_noncentral.py` and `open_lrn_noncentral-checks/verify_open_lrn_noncentral.txt` (CHECK 4: isotropic closed form vs independent 1D Schwinger quadrature agrees to $1.34\times 10^{-14}$ ($K=3$), $0.00$ ($K=4$), $4.44\times 10^{-16}$ ($K=5$, MC $z=+1.01$), $3.33\times 10^{-16}$ ($K=6$, MC $z=-0.94$); anisotropic $P$ 1D Schwinger vs MC agrees with rel diff $0.0124$ at edge $K=3$ and $z=+1.25$ at $K=5$ while isotropic formula misses by $> 0.11$; negative control flipping $c_{\parallel u}$ fails with gap $0.15555 > 0.01$).
- Depends on: C2

### C4: Non-elementarity obstructions and exact special-function hierarchy

- Statement: No general elementary closed form in $\sigma_H$ exists for $\mathbb{E}[\psi\psi^\top]$ on $K \ge r_c + 2$: (1) for $r_c = 1$, $P = p I_K$, every odd $K = 2m + 1 \ge 3$, $m_i = 0, u = 0, R_c > 0$, $\mathbb{E}[\psi^2] = R_c(R_1(\lambda) + R_2(\lambda) f_{1/2}(\lambda))$ with rational $R_2 \not\equiv 0$, which is provably non-elementary in $\sigma_H$ by Liouville's theorem; (2) for even $K = 4$, $r_c = 2$, $P = p I_4$, $H H^\top = s^2 I_2$, $\lambda = s^2/(2\sigma_H^2)$, $\mathbb{E}[(\hat H \hat H^\top)^{-1}] = \sigma_H^{-2}[\frac{1 - e^{-2\lambda}}{4\lambda} + \frac{1+\lambda}{2\lambda} e^{-\lambda} \operatorname{Shi}(\lambda)] I_2$ and $M(e_1, 0) + M(e_2, 0) - M(0, I_2) = I_2 - 2\mathbb{E}[HO] = [\frac{1 - e^{-2\lambda}}{2\lambda} + \frac{1+\lambda}{\lambda} e^{-\lambda}\operatorname{Shi}(\lambda) - 1] I_2$, proving $\mathbb{E}[\psi\psi^\top]$ is non-elementary in $\sigma_H$ even for even $K$ and isotropic $(P, HH^\top)$; (3) for anisotropic $P = \operatorname{diag}(p_1, p_2, p_3)$ at $r_c = 1, K = 3, H = (1, 0, 0), m_i = 0, u = 0, R_c = 1$, $\lim_{\sigma_H \to \infty} \sigma_H^2 \mathbb{E}[\psi^2] = \frac{1}{2\sqrt{p_1 p_2 p_3}}[p_1 R_F(1/p_1, 1/p_2, 1/p_3) - \frac{1}{3} R_D(1/p_2, 1/p_3, 1/p_1)]$, a complete elliptic integral for distinct $p_k$.
- Status: proved
- Review: fresh-context
- Check: verifier (#39), 2026-11-22, fresh-context reconstruction + independent SymPy ($C_0$-$C_8$), MC (`0.474591` vs `0.472560 +/- 0.014039`), and Carlson (`diff = 5.83e-16`) checks, no defect located.
- Evidence: Complete self-contained proofs (Liouville rational-solution obstructions, Schur + Poisson-Beta + Cauchy beta integral derivation of $\operatorname{Shi}(\lambda)$, and Carlson $R_F/R_D$ differentiation) in `C:\Users\chris and christine\.gemini\antigravity\brain\2b88195c-b147-483c-a266-afea6a54c14c\scratch\swarm_lrn_noncentral\cleaned_writeup.md` (Claim C4); three-channel verification in `open_lrn_noncentral-checks/verify_open_lrn_noncentral.py` and `open_lrn_noncentral-checks/verify_open_lrn_noncentral.txt` (CHECK 5: $\operatorname{Shi}(\lambda)$ formula vs Schur Poisson-${}_2F_2$ series agrees to $\le 2.22\times 10^{-16}$ at $\lambda \in \{0.3, 1.0, 1.7, 3.5\}$, and 3rd-channel 3D Matrix-Laplace quadrature of $M(e_1,0)+M(e_2,0)-M(0,I_2)$ agrees to $2.44\times 10^{-15}$ at $\lambda=1.7$; negative control replacing $\operatorname{Shi}(\lambda) \to \sinh(\lambda)/\lambda$ fails with gap $0.06406 > 0.05$; Carlson formula vs 1D quadrature agrees to $\le 1.55\times 10^{-15}$).
- Depends on: C1, C2, C3

### C5: Exact asymptotics ($\sigma_H \to 0$ and $\sigma_H \to \infty$) and full matrix-directional divergence for $K \le r_c + 1$

- Statement: (a) As $\sigma_H \to 0$ ($K \ge r_c + 2$), C1(3) reproduces `prop:lrn-understanding-expansion` for general $(r_c, P)$, and for $r_c = 1, P = p I_K$ expanding C3(b) yields the exact $O(\sigma_H^4)$ coefficient (whose $(R_c, u^2)$ perturbative series terminates at $O(\sigma_H^2)$ for $K = 4$ with purely non-perturbative $O(e^{-\|H\|^2/(2\sigma_H^2)})$ remainder). (b) As $\sigma_H \to \infty$ ($K \ge r_c + 2$), $\mathbb{E}[\psi\psi^\top \mid m_i, u] \to \mathbb{E}[(H(I_K - O_\infty W)m_i - u)(\cdots)^\top]$ and $\sigma_H^2 \mathbb{E}[H O R_c O^\top H^\top] \to H \mathbb{E}[O_\infty R_c O_\infty^\top] H^\top$ ($O_\infty = P W^\top(WPW^\top)^{-1}$), with exact elementary closed forms for isotropic $P = p I_K$ and all $r_c \ge 1, K \ge r_c + 2$ (noise leading term $\frac{\operatorname{tr}(R_c)}{\sigma_H^2 K(K - r_c - 1)} H H^\top$). (c) For $r_c \le K \le r_c + 1$ ($d \in \{1, 2\}$): if $\Pr(y \neq 0) > 0$, then $\mathbb{E}[(v^\top \psi)^2] = \infty$ for every $v \in \mathbb{R}^{r_c} \setminus \{0\}$; if $y = 0$ a.s., then $\mathbb{E}\|\psi\|^2 \le \|H\|^2 \kappa(P) \mathbb{E}\|m_i\|^2 < \infty$ for all $K \ge r_c$.
- Status: proved
- Review: fresh-context
- Check: verifier (#39), 2026-11-22, fresh-context reconstruction + independent SymPy fourth-order check, no defect located.
- Evidence: Complete derivation (integration by parts for $f_\alpha$, Dominated Convergence + Vitali's convergence theorem via $L^{5/4}$ uniform integrability from `lem:lrn-inverse-norm`(a), Haar projector Beta moments, and directional divergence via `lem:lrn-schur` + `lem:lrn-inverse-norm`(c)) in `C:\Users\chris and christine\.gemini\antigravity\brain\2b88195c-b147-483c-a266-afea6a54c14c\scratch\swarm_lrn_noncentral\cleaned_writeup.md` (Claim C5); two-channel verification in `open_lrn_noncentral-checks/verify_open_lrn_noncentral.py` and `open_lrn_noncentral-checks/verify_open_lrn_noncentral.txt` (CHECK 6: $\sigma_H \to 0$ remainder ratios $15.986$-$15.994$ vs $16$ and $c_4$ rel diff $\le 2.88\times 10^{-4}$ for $K=3,4,5$, anisotropic $K=3$ ratio $15.938$, negative control dropping noise-correlation terms gives ratio $4.030$; $\sigma_H \to \infty$ at $K=6, r_c=2$ gives max $|z|=1.28$ and noise rel diff $0.0103$; $K=2, r_c=1$ log-pole coefficient $0.04889496$ vs exact $0.04889482$, and $y=0$ finite value $0.16151784$ vs MC $0.16156452$, $z=+0.06$).
- Depends on: C1, C3

## Failed routes

### R1: Direct elementary closed form for general $(r_c, K, P)$

- Tried: Reducing $\mathbb{E}[\psi\psi^\top]$ to elementary functions of $(\sigma_H, H, P, m_i, u, R_c)$ for all $K \ge r_c + 2$.
- Failed because: Provably impossible (Claim C4): Dawson's integral $F(\sqrt{\lambda})$ appears with nonzero rational coefficient for every odd $K \ge 3$ at $r_c = 1, P = p I_K$; the hyperbolic sine integral $\operatorname{Shi}(\lambda)$ appears at even $K = 4, r_c = 2, P = p I_4, H H^\top = s^2 I_2$; and complete Carlson elliptic integrals $R_F, R_D$ appear in the $\sigma_H \to \infty$ coefficient for anisotropic $P$ at $r_c = 1, K = 3$.
- Reopen if: Never for general parameters; elementary closed forms exist only on restricted slices such as $r_c = 1$, isotropic $P = p I_K$, even $K \ge 4$ (Claim C3(b)).

### R2: Naive Cholesky-coordinate Gauss-Legendre quadrature for the 3D Matrix-Laplace integral

- Tried: Integrating over $T = L L^\top \in \mathcal{S}_2^{++}$ using $a = s u/(1-u)$, $c = s v/(1-v)$, $b = s \tan(\pi(w - 1/2))$.
- Failed because: Algebraic tail decay and boundary pinching at $(a, b) \to \infty$ slowed convergence to $2.4\times 10^{-4}$ at $n_{\mathrm{GL}} = 20$; replaced by compactified trigonometric spectral coordinates $T = Q(\theta)\operatorname{diag}(t_1, t_2)Q(\theta)^\top$ with $v_1 = \sin^2 \alpha_1$, $v_2 = v_1 \sin^2 \alpha_2$, $t_j = v_j / (2\bar s(1-v_j))$, which converged to $5.15\times 10^{-8}$ (edge $K = 4$) and $2.44\times 10^{-15}$ (symmetric $K = 4, m_i = 0$).
- Reopen if: Extending numerical quadrature to $r_c \ge 3$ where spectral Vandermonde Jacobians become higher dimensional.

### R3: Pointwise Dominated Convergence for $\lim_{\sigma_H \to \infty} \sigma_H^2 \mathbb{E}[H O R_c O^\top H^\top]$

- Tried: Constructing a single $\sigma_H$-independent random variable dominating $\sigma_H^2 \|H O\|^2$ pointwise in $W$.
- Failed because: The rank-drop singularity of $W + \sigma_H^{-1} H$ translates with $\sigma_H$, so no fixed $L^1(W)$ function dominates $\sigma_H^2 \|O(W + \sigma_H^{-1} H)\|^2$ pointwise across all $\sigma_H > 0$. Replaced by uniform $L^{5/4}$-boundedness of $\sigma_H^2 \|O\|^2$ via `lem:lrn-inverse-norm`(a) with $p = 5/2 < 3 \le d$ and Vitali's convergence theorem (Claim C5(b)).
- Reopen if: Not needed; Vitali's theorem closes the step unconditionally for all $K \ge r_c + 2$.

## Open obligations

- [x] O1 (sessions: 1): Complete fresh-context reconstruction proof check of Claims C1-C5 via `@verifier` from `cleaned_writeup.md`, repair any located defects, update `Review:` / `Check:` fields, and re-lint. (Completed 2026-11-22: `@verifier` #39 returned `no defect located` on all 5 claims C1-C5.)

## Review Log

- 2026-11-22 (`@verifier`, board #39): Fresh-context reconstruction of Claims C1-C5 from `cleaned_writeup.md` + cited `.tex` files + independent SymPy/numerical verification script (`verify_lrn_noncentral.py`). Verdicts: C1 `no defect located`, C2 `no defect located`, C3 `no defect located` (quadrature vs closed form at $K=3$ diff `1.18e-14`), C4 `no defect located` (SymPy $C_0$-$C_8$, $\operatorname{Shi}$ MC `0.474591` vs `0.472560 +/- 0.014039`, Carlson diff `5.83e-16`), C5 `no defect located` (SymPy 4th-order expansion and $K=4$ exact remainder). Zero defects; all 5 claims promoted to `Review: fresh-context`.

## Literature

| Claim | Source | Locator | Read depth | Date read | Verdict |
| --- | --- | --- | --- | --- | --- |
| Live model, `thm:lrn-understanding-moment`, `prop:lrn-understanding-expansion`, `open:lrn-noncentral` | `sections/ext5_lrn.tex`, `sections/appext5_lrn.tex`, `sections/chkext5_lrn.tex`, `sections/s02_framework.tex` | `sec:lrn-understanding`, `lem:lrn-inverse-norm`, `lem:lrn-schur`, `lem:lrn-isserlis`, `eq:fw-two-errors` | Full read | 2026-11-22 | Exact match with conventions and hypotheses |

## Searches

| Query | Tool | Date | Not searched |
| --- | --- | --- | --- |
| `"noncentral Wishart" inverse moment expectation "exact" closed form Hillier Kan Letac Massam` | `search_web` | 2026-11-22 | Full text of Hillier & Kan (2022) and Letac & Massam (2008) not opened; no results imported from them |
| `"expectation of the inverse" "noncentral Wishart" confluent hypergeometric OR Shi OR zonal` | `search_web` | 2026-11-22 | No external result cited; all claims proved self-contained |

## Log

- 2026-11-22: Opened investigation on `open:lrn-noncentral`. Derived Claims C1-C5, caught and fixed a missing $-I_2$ in the C4(2) linear-combination identity via the 3rd-channel Matrix-Laplace check (discrepancy `1.0000000000000024` reduced to `2.44e-15`), captured full two-channel verification + negative controls in `open_lrn_noncentral-checks/verify_open_lrn_noncentral.txt`.
- 2026-11-22: Fresh-context reconstruction by `@verifier` (#39) confirmed `no defect located` across all 5 claims C1-C5. Promoted all claims to `Review: fresh-context`, closed O1, and closed record.
- 2026-11-22 (Reporting gate):
  1. Literally asked & intended: exact closed form of $\mathbb{E}[\psi\psi^\top]$ for $K \ge r_c + 2$ as a function of $\sigma_H$ and all parameters, asymptotics vs `prop:lrn-understanding-expansion`, edge cases ($K = r_c + 2$, $\sigma_H \to 0$, $\sigma_H \to \infty$, $r_c = 1$), elementary vs special-function exactness, and divergence for $K \le r_c + 1$. Answered completely: exact closed-form single-${}_1F_1$ / elementary formula for isotropic $r_c = 1$ (C3(b)), exact 1D Schwinger integral for general-$P$ $r_c = 1$ (C3(a)), exact $\frac{r_c(r_c+1)}{2}$-dimensional Matrix-Laplace integral over $\mathcal{S}_{r_c}^{++}$ for all $(r_c, K \ge r_c+2, P \succ 0)$ (C2), exact non-perturbative Stein representation (C1), rigorous Liouville + $\operatorname{Shi}$ + Carlson elliptic non-elementarity obstructions (C4), and exact $\sigma_H \to 0, \infty$ asymptotics and matrix-directional divergence for $K \le r_c + 1$ (C5).
  2. Two ways a draft could satisfy the letter while missing the point: (i) proving only the $r_c = 1, P = p I_K$ case and silently claiming it solves the general problem — avoided by C1, C2, C3(a), C4(2,3), C5(b,c) covering general $r_c \ge 1$ and anisotropic $P \succ 0$; (ii) writing an implicit integral over $W$ and calling it a "closed form" — avoided by reducing the $K$-dependent $r_c K$-dimensional expectation to an explicit $K$-independent $\frac{r_c(r_c+1)}{2}$-dimensional cone integral (1D for $r_c=1$, single-${}_1F_1$ for isotropic $r_c=1$, exact $\operatorname{Shi}(\lambda)$ for symmetric $K=4, r_c=2$) and proving via Liouville's theorem why no general elementary expression exists.
  3. Strongest referee objection: For $r_c \ge 2$ with arbitrary anisotropic $P \succ 0$, Claim C2 is an explicit $\frac{r_c(r_c+1)}{2}$-dimensional cone integral (whose integrand $\mathbb{E}_T[\cdot]$ is a rational function of $T$ computable via Isserlis contractions), rather than a single named univariate special function. Answered & disclosed directly: Claim C4 proves that even at isotropic $r_c = 2, K = 4, H H^\top = s^2 I_2$, $\operatorname{Shi}(\lambda)$ is unavoidable, and even at $r_c = 1, K = 3$ with anisotropic $P$, complete elliptic integrals $R_F, R_D$ appear already in the $\sigma_H \to \infty$ limit; hence an integral / multivariate special-function representation is structurally optimal.
  4. Speculative claims / unrun checks / three remaining error modes & exclusions: Zero speculative claims; no external papers cited as premises (all proofs self-contained). Three error modes excluded: (a) missing constant/sign in matrix algebra — excluded by two/three-channel checks and negative controls (which caught and fixed the missing $-I_2$ in C4(2) to `2.44e-15`); (b) unjustified limit/integral interchanges at the singular rank-drop locus — excluded by regularized Stein + $L^1$ bounds (C1), Tonelli/Fubini via `thm:lrn-understanding-moment` (C2), and Vitali's theorem via $L^{5/4}$ uniform integrability (C5(b)), all checked in fresh context by `@verifier`; (c) infinite-variance MC noise masking an error at $d = 3$ — excluded by using deterministic quadrature channels (`diff <= 1.34e-14` for $r_c=1$, `2.44e-15` for $r_c=2, K=4$) plus finite-fourth-moment ($d=5$) CLT tests (`max |z| <= 1.28`).
  5. Remaining obligations: None (O1 closed). Work is reported as complete (`open:lrn-noncentral` resolved).
