# Open Problem `open:coh-amplification-noisy`: Amplification Beyond Noiseless Circulation

- Status: active
- Opened: 2026-11-21
- Updated: 2026-11-21
- Sessions: 1

**Manuscript anchors:** `Collective_Agents/sections/s06_coherence.tex` (`open:coh-amplification-noisy`, line 143; `prop:coh-no-amplification`, line 110; `ex:coh-amplification`, line 123; `obs:coh-amplification-information`, line 133), `Collective_Agents/sections/06_coherence.tex` (`def:coh-cycle-product`, line 108; `thm:coh-amplification`, line 115), `Collective_Agents/sections/app06_coherence.tex` (proofs of `thm:coh-amplification` and `prop:coh-no-amplification`, lines 111–127; `lem:coh-rank-one`, line 131), `Collective_Agents/sections/chk06_coherence.tex` (`chk:coh-amplification`, line 48), `Collective_Agents/sections/02_framework.tex` (`prop:fw-update-subspace`, line 52; `prop:fw-prior-completion`, line 64; `def:fw-levels`, line 135; `def:fw-level0`, line 313).

## Target

- Locked statement: Settle all three parts of `open:coh-amplification-noisy` (`s06_coherence.tex` line 143): *"Characterize amplification for noisy circulation, where $A_{1N}$ in the round-trip map is not idempotent, and for dynamic cycles in which senders post posterior rather than prior covariances. For a common code of rank at least two read with sender-specific noise covariances, amplification occurs and is unbounded (the instance following `\cref{prop:coh-no-amplification}`); what remains open there is a condition on the assigned noise covariances, weaker than the common noise of `\cref{prop:coh-no-amplification}`(d), that excludes it."*
- Falsifier: (a) For the natural generalization $\rho(\bar A_{\mathfrak c}) = \max\{\rho(A_{\mathfrak c}), 1\}$ of `thm:coh-amplification`(b) to noisy circulation: any noisy cycle where $\rho(A_{\mathfrak c}) < 1 < \rho(\bar A_{\mathfrak c})$ or $\rho(A_{\mathfrak c}) > 1 = \rho(\bar A_{\mathfrak c})$, or where $\rho(\bar A_{\mathfrak c})$ depends on the base agent; for the replacement return-noiseless bound (C2) and full $N$-agent circulation characterization (C3): any admissible cycle violating $\rho(\bar A_{\mathfrak c}) \le \max\{1, (\mathfrak r_{N\to 1}^\circ)^{1/2}\prod_{e\neq(N\to 1)}(\mathfrak r_e \frac{\mathrm{snr}_e}{1+\mathrm{snr}_e})^{1/2}\}$ or the characteristic equations of $\mathcal T_{\mathrm{seq}}, \mathcal T_{\mathrm{sync}}$. (b) For the Posterior Edge-Ratio Theorem (C4): any cycle violating $\rho(A_{\mathfrak c}) \le \prod_{e\in\mathfrak c}(\mathfrak r_e^+ \frac{\mathrm{snr}_e}{1+\mathrm{snr}_e})^{1/2}$ with $\mathfrak r_{i\to j}^+ = \lambda_{\max}(\hat R_i^{-1} H_i \widetilde P_i^+ H_i^\top)$, or any cycle with post-reception posterior headers $P_i^+ \succeq \widetilde P_i^+$ where $\rho(A_{\mathfrak c}) \ge 1$. (c) For common codes of rank $r_c \ge 2$ with sender-specific noises $\hat R_1,\dots,\hat R_N \succ 0$ (C6–C7): any tuple of priors and proportional noises $\hat R_i = \alpha_i \hat R_0$ with $\rho(A_{\mathfrak c}) \ge 1$, any non-proportional tuple $(\hat R_1,\dots,\hat R_N)$ where $\sup_{P_1,\dots,P_N\succ 0}\rho(A_{\mathfrak c}) \le 1$, or any cycle violating the cyclic noise-spread bound or the Kantorovich projective-distance bound.
- May assume: Linear-Gaussian reception definitions and propositions of `02_framework.tex` (`prop:fw-update-subspace`, `prop:fw-prior-completion`, `def:fw-levels`, `def:fw-level0`) and Section 6 (`def:coh-cycle-product`, `thm:coh-amplification`, `prop:coh-no-amplification`, `lem:coh-rank-one`).
- Must not assume: Idempotence of $A_{ji}$ when $\hat R_i \neq 0$; commutativity of $X_j$ and $\hat R_i$; unproven matrix inequalities without self-contained derivations; equality of prior covariance $P_i$ and posterior covariance $P_i^+$.
- Alternative forms: Where natural generalizations fail (the noiseless round-trip formula $\rho(\bar A_{\mathfrak c}) = \max\{\rho(A_{\mathfrak c}), 1\}$ under noisy codes, the prior edge-ratio condition $\hat R_i \succeq X_{ii}$ under posted posterior headers, and equal-trace/equal-determinant sender noises under a common code of rank $\ge 2$), construct exact rational counterexamples and prove sharp replacement theorems.
- Test instance: Registered instance following `prop:coh-no-amplification` (`s06_coherence.tex` line 121, `chk06_coherence.tex` line 50): $K=2, N=2$, common code $H = I_2$, priors $P_a = \bigl(\begin{smallmatrix}1 & 1.8\\1.8 & 4\end{smallmatrix}\bigr)$, $P_b = \bigl(\begin{smallmatrix}4 & 1.8\\1.8 & 1\end{smallmatrix}\bigr)$ ($\alpha=0.9, x=4$), assigned noises $\hat R_b = \operatorname{diag}(0.1, M)$ and $\hat R_a = \operatorname{diag}(M, 0.1)$, giving $\rho(A_{\mathfrak c}) = 1.356779, 2.358566, 2.640995, 2.677313$ at $M = 1, 10, 100, 10^4$ against the $M\to\infty$ limit $\alpha^2 x/(1+r)^2 = 3.24/1.21 = 2.677686$ (and exact supremum $(10M+1)^2/(40M)$ over all priors $P_a, P_b \succ 0$ at fixed $M$).
- Out of scope: Non-Gaussian or nonlinear observation channels; code-learning dynamics (`sec:fw-learning`); multi-cycle overlapping graph topologies beyond directed cycles $\mathfrak c$.
- Reading chosen: We treat all three parts in full generality: for (a), both the single-agent round-trip map $\bar A_{\mathfrak c} = (I - A_{1N}) + A_{\mathfrak c}$ literally named in `open:coh-amplification-noisy` and the full $N$-agent persistent sequential (Gauss--Seidel) and synchronous (Jacobi) circulation operators on $(\mathbb R^K)^N$; for (b), both post-reception posterior headers $P_i^+ = \widetilde P_i^+$ (within-round sequential or multi-round Riccati filtering, with or without private sensing) and lagged pre-prediction filtered posterior headers $P_i^+(t-1)$ vs predicted reception priors $P_i^-(t) = F P_i^+(t-1) F^\top + Q_i$; for (c), both finite-SNR noise-spread conditions and the necessary and sufficient prior-free condition on $(\hat R_1,\dots,\hat R_N)$.

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| Edge gain-code map | $A_{ji} = \mathrm K_{ji} H_i = P_j H_i^\top S_{ji}^{-1} H_i$, $S_{ji} = X_{ji} + \hat R_i$, $X_{ji} = H_i P_j H_i^\top$, $X_{ii} = H_i P_i H_i^\top$ (`def:coh-cycle-product`) | For $P_j = \bigl(\begin{smallmatrix}1 & 3/2\\3/2 & 4\end{smallmatrix}\bigr)$, $H_i = (1\ 0)$, $\hat R_i = 2$: $S_{ji} = 3$, $A_{ji} = \bigl(\begin{smallmatrix}1/3 & 0\\1/2 & 0\end{smallmatrix}\bigr)$ |
| Cycle product and round-trip map | $A_{\mathfrak c} = A_{1N} A_{N,N-1}\cdots A_{21}$, $\bar A_{\mathfrak c} = (I - A_{1N}) + A_{\mathfrak c}$ (`def:coh-cycle-product`, `thm:coh-amplification`(b)) | In Counterexample C1(a): $\operatorname{spec}(A_{\mathfrak c}) = \{1/2, 0\}$, $\operatorname{spec}(\bar A_{\mathfrak c}) = \{7/6, 1\}$ |
| Edge SNR and prior edge ratio | $\frac{\mathrm{snr}_e}{1+\mathrm{snr}_e} = \lambda_{\max}(S_{ji}^{-1} X_{ji})$, $\mathfrak r_e = \lambda_{\max}(S_{ji}^{-1} X_{ii})$, noiseless ratio $\mathfrak r_e^\circ = \lambda_{\max}(X_{ji}^{-1} X_{ii})$ (`thm:coh-amplification`(a)) | For $X_{12} = 1, X_{22} = 4, \hat R_2 = 2$: $\frac{\mathrm{snr}}{1+\mathrm{snr}} = \frac{1}{3}$, $\mathfrak r_{2\to 1} = \frac{4}{3}$, $\mathfrak r_{2\to 1}^\circ = 4$ |
| Post-reception posterior covariance & ratio | $\widetilde P_i^+ = P_i - P_i H_{i^-}^\top S_{i,i^-}^{-1} H_{i^-} P_i = (P_i^{-1} + H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-})^{-1}$, $\widetilde X_{ii}^+ = H_i \widetilde P_i^+ H_i^\top$, $\mathfrak r_{i\to j}^+ = \lambda_{\max}(\hat R_i^{-1} \widetilde X_{ii}^+)$ | For $P_1 = \bigl(\begin{smallmatrix}1 & 19/10\\19/10 & 4\end{smallmatrix}\bigr)$, $H_2 = (1\ 0)$, $H_1 = (0\ 1)$, $\hat R_2 = \frac{1}{10}$, $\hat R_1 = \frac{8}{11}$: $\widetilde X_{11}^+ = \frac{79}{110}$, $\mathfrak r_{1\to 2}^+ = \frac{79}{80} < 1$ |
| Asymmetric spread, Thompson & Hilbert metrics | $\operatorname{sp}(A\Vert B) = \ln\lambda_{\max}(B^{-1}A)$, $\operatorname{dist}_{\mathrm T}(A,B) = \max\{\operatorname{sp}(A\Vert B),\operatorname{sp}(B\Vert A)\}$, $\kappa(B^{-1}A) = \frac{\lambda_{\max}(B^{-1}A)}{\lambda_{\min}(B^{-1}A)}$, $d_{\mathrm H}(A,B) = \ln\kappa(B^{-1}A) = \operatorname{sp}(A\Vert B)+\operatorname{sp}(B\Vert A)$ | For $A = \operatorname{diag}(3,1), B = \operatorname{diag}(1,3)$: $\operatorname{sp}(A\Vert B) = \ln 3$, $\kappa(B^{-1}A) = 9$, $d_{\mathrm H}(A,B) = \ln 9$, $\frac{(\sqrt{\kappa}+1)^2}{4\sqrt{\kappa}} = \frac{4}{3}$ |

## Claims

### C1: Failure of the noiseless round-trip identity and base-point invariance under noisy circulation

- Statement: The noiseless round-trip relation $\rho(\bar A_{\mathfrak c}) = \max\{\rho(A_{\mathfrak c}), 1\}$ of `thm:coh-amplification`(b) for $\bar A_{\mathfrak c} = (I - A_{1N}) + A_{\mathfrak c}$ (with $\operatorname{rank} H_N < K$) and the base-point invariance of round-trip amplification both fail when $\hat R_N \neq 0$: there exist noisy cycles with $\rho(A_{\mathfrak c}) < 1 < \rho(\bar A_{\mathfrak c})$ (even when $\hat R_i \succeq X_{ii}$ on every edge as in `prop:coh-no-amplification`(c)), noisy cycles where $\bar A_{\mathfrak c}$ amplifies at base agent $1$ but not at base agent $2$, and noisy cycles with $\rho(A_{\mathfrak c}) > 1 = \rho(\bar A_{\mathfrak c})$.
- Status: refuted
- Review: self
- Evidence: Complete derivation of the rank-1 eigenvalue $\lambda_{\mathrm{rt}}^{(1)} = (1 - s_{1N}) + \operatorname{tr}(A_{\mathfrak c})$ in Section `Derivations` (Proposition 1) and three exact rational counterexamples in $K=2, N=2$ with $\bm h_1 = (0\ 1), \bm h_2 = (1\ 0)$: (a) $P_1 = \bigl(\begin{smallmatrix}1 & 3/2\\3/2 & 4\end{smallmatrix}\bigr)$, $P_2 = \bigl(\begin{smallmatrix}4 & 3/2\\3/2 & 1\end{smallmatrix}\bigr)$, $\hat R_1 = 1/2, \hat R_2 = 2$ gives $\rho(A_{\mathfrak c}) = 1/2 < 1$, $\rho(\bar A_{\mathfrak c}^{(1)}) = 7/6 > 1$, $\rho(\bar A_{\mathfrak c}^{(2)}) = 1$; (a') $P_1 = \bigl(\begin{smallmatrix}1 & 3\\3 & 10\end{smallmatrix}\bigr)$, $P_2 = \bigl(\begin{smallmatrix}100 & 25\\25 & 7\end{smallmatrix}\bigr)$, $\hat R_1 = 10 = X_{11}$, $\hat R_2 = 100 = X_{22}$ gives $\rho(A_{\mathfrak c}) = 75/1717 < 1$ and $\rho(\bar A_{\mathfrak c}^{(1)}) = 1775/1717 > 1$; (b) $P_1 = \bigl(\begin{smallmatrix}1 & 2\\2 & 5\end{smallmatrix}\bigr)$, $P_2 = \bigl(\begin{smallmatrix}5 & -2\\-2 & 1\end{smallmatrix}\bigr)$, $\hat R_1 = 2/3, \hat R_2 = 1$ gives $\rho(A_{\mathfrak c}) = 6/5 > 1$ and $\rho(\bar A_{\mathfrak c}^{(1)}) = 1$; verified in `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy.py` and `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy_output.txt`.
- Depends on: none

### C2: Exact coded reduction and sharp return-noiseless edge-ratio bound for the noisy round-trip map

- Statement: For any cycle $\mathfrak c$ with $P_j \succ 0$, full-row-rank codes $H_i \in \mathbb R^{r_i\times K}$, and $\hat R_i \succeq 0$ ($S_{ji} \succ 0$), $\mathbb R^K = V_1 \oplus \ker(H_N)$ with $V_1 = \operatorname{col}(P_1 H_N^\top)$, $\operatorname{spec}(\bar A_{\mathfrak c}) = \operatorname{spec}(M_{\mathrm{rt}}^{(1)}) \cup \{1\text{ (mult.\ }K-r_N)\}$ where $M_{\mathrm{rt}}^{(1)} = (I_{r_N} - \Sigma_{1N}) + \Sigma_{1N}\tilde{\mathcal C}_{\mathfrak c}$, $\Sigma_{1N} = X_{1N}^{1/2} S_{1N}^{-1} X_{1N}^{1/2}$, $\tilde{\mathcal C}_{\mathfrak c} = X_{1N}^{-1/2} H_N A_{N,N-1}\cdots A_{21} P_1 H_N^\top X_{1N}^{-1/2}$, and
  $$\rho(\bar A_{\mathfrak c}) \le \max\bigl\{1,\;\|\Sigma_{1N}^{-1/2} M_{\mathrm{rt}}^{(1)}\Sigma_{1N}^{1/2}\|_2\bigr\} \le \max\bigl\{1,\;\|\tilde{\mathcal C}_{\mathfrak c}\|_2\bigr\} \le \max\Biggl\{1,\;(\mathfrak r_{N\to 1}^\circ)^{1/2}\prod_{e\in\mathfrak c\setminus\{N\to 1\}}\Bigl(\mathfrak r_e\frac{\mathrm{snr}_e}{1+\mathrm{snr}_e}\Bigr)^{1/2}\Biggr\},$$
  with $\mathfrak r_{N\to 1}^\circ = \lambda_{\max}(X_{1N}^{-1}X_{NN})$. In particular, $\rho(\bar A_{\mathfrak c}) = 1$ whenever $P_j = P$ is a common prior (for any $\hat R_i \succeq 0$) or $\sum_{(i\to j)\in\mathfrak c}\operatorname{sp}(P_i\Vert P_j) \le 2\sum_{e\neq(N\to 1)}\ln(1+\mathrm{snr}_e^{-1})$.
- Status: proved
- Review: self
- Evidence: Complete proof in Section `Derivations` (Theorem 1); verified with 0 violations and max spectral discrepancy $4.99\times 10^{-13}$ across 5,000 random cycles (attained to ratio $0.997602$), plus planted-error negative control NC1 (violated in $54/4000$ heterogeneous trials) in `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy.py` and `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy_output.txt`.
- Depends on: none

### C3: Full $N$-agent persistent noisy circulation (sequential Gauss--Seidel and synchronous Jacobi dynamics)

- Statement: In full $N$-agent persistent circulation on $(\mathbb R^K)^N$ where every agent $k \in \{1,\dots,N\}$ updates by $x_k^+ = (I - A_{k,k-1})x_k + A_{k,k-1}x_{k-1}$ sequentially along $k=2,\dots,N,1$ (operator $\mathcal T_{\mathrm{seq}}$) or synchronously (operator $\mathcal T_{\mathrm{sync}}$): (1) on the invariant subspace $\bigoplus_{k=1}^N V_k$ ($V_k = \operatorname{col}(P_k H_{k-1}^\top)$), in coordinates $z_k = X_{k,k-1}^{-1/2} H_{k-1} x_k$, each step is $z_k^+ = (I_{r_{k-1}} - \Sigma_{k,k-1})z_k + \Sigma_{k,k-1}\tilde C_{k,k-1} z_{k-1}$ where $\tilde C_{k,k-1} = X_{k,k-1}^{-1/2} H_{k-1} P_{k-1} H_{k-2}^\top X_{k-1,k-2}^{-1/2}$ is the noiseless coded edge map ($\|\tilde C_{k,k-1}\|_2 \le (\mathfrak r_{k-1\to k}^\circ)^{1/2}$), so $\mathfrak r_e^\circ \le 1$ on all edges (in particular, a common prior $P_j = P$) forces $\rho(\mathcal T_{\mathrm{seq}}) \le 1$ and $\rho(\mathcal T_{\mathrm{sync}}) \le 1$ in the block norm $\max_k \|\Sigma_{k,k-1}^{-1/2} z_k\|_2$ for any $\hat R_i \succeq 0$; (2) for rank-1 codes ($r_i = 1$), the non-unit eigenvalues of $\mathcal T_{\mathrm{seq}}$ and $\mathcal T_{\mathrm{sync}}$ solve $\prod_{k=1}^N(\lambda - (1 - s_{k,k-1})) = \lambda^{N-1}\tau^\circ\prod_{k=1}^N s_{k,k-1}$ and $\prod_{k=1}^N(\lambda - (1 - s_{k,k-1})) = \tau^\circ\prod_{k=1}^N s_{k,k-1}$ respectively, where $\tau^\circ = \operatorname{tr}(A_{\mathfrak c}^{\mathrm{noiseless}}) = \prod_{j=1}^N\cos_{P_j}(\bm h_j,\bm h_{j^-})\,\mathfrak M_{\mathfrak c}$; hence $|\tau^\circ| \le 1$ implies $\rho(\mathcal T_{\mathrm{seq}}) \le 1$ and $\rho(\mathcal T_{\mathrm{sync}}) \le 1$ for all $\hat R_i \ge 0$, whereas $\tau^\circ > 1$ implies $\rho(\mathcal T_{\mathrm{seq}}) > 1$ and $\rho(\mathcal T_{\mathrm{sync}}) > 1$ for all finite $\hat R_1,\dots,\hat R_N \ge 0$.
- Status: proved
- Review: self
- Evidence: Complete proof in Section `Derivations` (Theorem 2); characteristic equations verified to $1.80\times 10^{-13}$ across 1,000 random 3-cycles and persistent instability at $\tau^\circ = 3.24 > 1$ confirmed for $R_c \in \{0.1, 1, 4, 10, 100\}$ in `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy.py` and `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy_output.txt`.
- Depends on: C2

### C4: Posterior Edge-Ratio Theorem and unconditional exclusion of amplification under post-reception posterior headers

- Statement: For any cycle $\mathfrak c$ with reception priors $P_1,\dots,P_N \succ 0$, codes $H_1,\dots,H_N$, and assigned noises $\hat R_1,\dots,\hat R_N \succ 0$, let $\widetilde P_i^+ = P_i - P_i H_{i^-}^\top S_{i,i^-}^{-1} H_{i^-} P_i = (P_i^{-1} + H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-})^{-1}$ be agent $i$'s post-reception posterior covariance after reading predecessor $i^-$, let $\widetilde X_{ii}^+ = H_i \widetilde P_i^+ H_i^\top$, and define the posterior edge ratio $\mathfrak r_e^+ = \lambda_{\max}(\hat R_i^{-1}\widetilde X_{ii}^+)$ on $e=(i\to j)$. Then $\mathrm K_{i,i^-} = P_i H_{i^-}^\top S_{i,i^-}^{-1} = \widetilde P_i^+ H_{i^-}^\top \hat R_{i^-}^{-1}$ and
  $$\rho(A_{\mathfrak c}) \le \prod_{e\in\mathfrak c}\Bigl(\mathfrak r_e^+\frac{\mathrm{snr}_e}{1+\mathrm{snr}_e}\Bigr)^{1/2} \le \prod_{e\in\mathfrak c}(\mathfrak r_e^+)^{1/2}.$$
  Consequently, whenever each sender $i$ posts a covariance header $P_i^+ \succeq \widetilde P_i^+$ (in particular, its exact post-reception posterior covariance $P_i^+ = \widetilde P_i^+$ in single-pass or multi-round dynamic filtering), level-1 reception $\hat R_i = H_i P_i^+ H_i^\top + R_{c,i}$ satisfies $\mathfrak r_e^+ \le 1$ on every edge and $\rho(A_{\mathfrak c}) \le \prod_{e\in\mathfrak c}(\frac{\mathrm{snr}_e}{1+\mathrm{snr}_e})^{1/2} < 1$, even when $\hat R_i \not\succeq X_{ii}$ and the prior edge ratio $\mathfrak r_e = \lambda_{\max}(S_{ji}^{-1}X_{ii})$ exceeds $1$. The same contraction $\rho(A_{\mathfrak c}^{\mathrm{post}}) < 1$ holds when agent $i$ also fuses an external/sensory observation of precision $\Gamma^{\mathrm{ext}}_i \succeq 0$ during the round, for the actual posterior mean transfer $A_{i,i^-}^{\mathrm{post}} = P_i^+ H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-}$ with $P_i^+ = (P_i^{-1} + H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-} + \Gamma^{\mathrm{ext}}_i)^{-1}$.
- Status: proved
- Review: self
- Evidence: Complete proof in Section `Derivations` (Theorem 3); exact rational SymPy witness ($r_{1\to 2} = 440/91 > 1$ while $r_{1\to 2}^+ = 79/80 < 1, \rho(A_{\mathfrak c}) = 171/910 < 1$), 5,000 random cycles (0 violations, $4537/5000$ having prior $r_e > 1$), and planted-error negative control NC2 (violated in $3986/5000$ trials) in `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy.py` and `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy_output.txt`.
- Depends on: none

### C5: Amplification in dynamic cycles with lagged pre-prediction filtered posterior headers

- Statement: In a dynamic world $\eta_{t+1} = F\eta_t + w_t$ where receiver $j$ forms its round-$t$ gain $\mathrm K_{ji} = P_j^-(t) H_i^\top S_{ji}^{-1}$ from its predicted prior covariance $P_j^-(t) = F P_j^+(t-1) F^\top + Q_j$ (`def:fw-level0`) while sender $i$ posts its pre-prediction filtered posterior covariance $H_i P_i^+(t-1) H_i^\top$ (so $\hat R_i = H_i P_i^+(t-1) H_i^\top + R_{c,i}$), the posterior edge ratio $\mathfrak r_e^+ = \lambda_{\max}(\hat R_i^{-1} H_i \widetilde P_i^+(t) H_i^\top)$ can exceed $1$ whenever $F P_i^+(t-1) F^\top + Q_i \not\preceq P_i^+(t-1)$, and $\rho(A_{\mathfrak c})$ can exceed $1$ and grow without bound with the prediction innovation $Q_i$.
- Status: proved
- Review: self
- Evidence: Explicit construction in Section `Derivations` (Proposition 2) with $F = \frac{1}{2}I_2$, $P_a^+ = P_b^+ = \frac{1}{5}I_2$, $R_c = \frac{1}{10}$ ($\hat R_i = \frac{3}{10}$), and $Q_a, Q_b \succ 0$ producing the predicted priors $P_a^-, P_b^-$ of `ex:coh-amplification`(i), yielding $\rho(A_{\mathfrak c}) = \frac{3.24}{1.69} \approx 1.917160 > 1$ (and $\frac{\alpha^2 x}{(1 + H_i P_i^+ H_i^\top + R_c)^2} \to \infty$ as $x \to \infty$); verified in `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy.py` and `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy_output.txt`.
- Depends on: C4

### C6: Cyclic noise-spread bound and Kantorovich projective-distance bound for a common code of rank $\ge 2$

- Statement: Let all senders share a common code $H_i = H \in \mathbb R^{r_c\times K}$ of full row rank $r_c \ge 2$, read with sender-specific assigned noise covariances $\hat R_1,\dots,\hat R_N \in \mathbb S_{++}^{r_c}$. Then $\operatorname{spec}(A_{\mathfrak c})\setminus\{0\} = \operatorname{spec}(B_N\cdots B_1)\setminus\{0\}$ with $B_j = X_j(X_j + \hat R_{j-1})^{-1} = \hat R_{j-1}^{1/2} E_j \hat R_{j-1}^{-1/2}$ ($X_j = H P_j H^\top$, $E_j = Y_j(I+Y_j)^{-1}$, $\|E_j\|_2 = \frac{\mathrm{snr}_{j-1\to j}}{1+\mathrm{snr}_{j-1\to j}}$), and for all priors $P_1,\dots,P_N \succ 0$:
  1. The cyclic noise spread $\mathcal S_{\mathfrak c}(\hat R) = \sum_{j=1}^N \operatorname{sp}(\hat R_{j-1}\Vert\hat R_j)$ satisfies $\mathcal S_{\mathfrak c}(\hat R) \ge 0$ (with equality if and only if $\hat R_i = \alpha_i \hat R_0$ for some $\alpha_i > 0, \hat R_0 \succ 0$), and $\rho(A_{\mathfrak c}) \le \exp(\frac{1}{2}\mathcal S_{\mathfrak c}(\hat R))\prod_{e\in\mathfrak c}\frac{\mathrm{snr}_e}{1+\mathrm{snr}_e}$, which is $\le 1$ whenever $\mathcal S_{\mathfrak c}(\hat R) \le 2\sum_{e\in\mathfrak c}\ln(1+\mathrm{snr}_e^{-1})$.
  2. For every $M \in \mathbb S_{++}^{r_c}$ and $0 \preceq E \preceq s I_{r_c}$, $\|M^{-1} E M\|_2 \le s\frac{\kappa(M)^2+1}{2\kappa(M)}$ where $\kappa(M) = \lambda_{\max}(M)/\lambda_{\min}(M)$. Consequently, for any reference covariance $\hat R_\ast \in \mathbb S_{++}^{r_c}$, with $d_{\mathrm H}(\hat R_i,\hat R_\ast) = \ln\kappa(\hat R_\ast^{-1}\hat R_i)$,
     $$\rho(A_{\mathfrak c}) \le \prod_{j=1}^N \frac{\mathrm{snr}_{j-1\to j}}{1+\mathrm{snr}_{j-1\to j}}\,\frac{\kappa(\hat R_\ast^{-1}\hat R_{j-1})+1}{2\sqrt{\kappa(\hat R_\ast^{-1}\hat R_{j-1})}} = \prod_{j=1}^N \frac{\mathrm{snr}_{j-1\to j}}{1+\mathrm{snr}_{j-1\to j}}\cosh\Bigl(\frac{1}{2}d_{\mathrm H}(\hat R_{j-1},\hat R_\ast)\Bigr),$$
     which is $\le 1$ whenever $\sum_{j=1}^N \ln\cosh(\frac{1}{2}d_{\mathrm H}(\hat R_{j-1},\hat R_\ast)) \le \sum_{e\in\mathfrak c}\ln(1+\mathrm{snr}_e^{-1})$.
- Status: proved
- Review: self
- Evidence: Complete proof in Section `Derivations` (Lemma 1 and Theorem 4); verified across 5,000 random non-proportional cycles (0 violations of either bound; 2,451 draws meeting C6(1) and 3,476 draws meeting C6(2), with 0 amplifying draws among them) in `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy.py` and `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy_output.txt`.
- Depends on: none

### C7: Proportional-noise characterization and exact worst-case spectral radius for a common code of rank $\ge 2$

- Statement: For a common code $H_i = H \in \mathbb R^{r_c\times K}$ of full row rank $r_c \ge 2$ and sender-specific assigned noise covariances $\hat R_1,\dots,\hat R_N \in \mathbb S_{++}^{r_c}$:
  1. Amplification is excluded for all priors ($\sup_{P_1,\dots,P_N\succ 0}\rho(A_{\mathfrak c}) \le 1$) if and only if the assigned noise covariances are proportional across senders, $\hat R_i = \alpha_i \hat R_0$ ($\alpha_i > 0, \hat R_0 \in \mathbb S_{++}^{r_c}$). Under proportionality, $\rho(A_{\mathfrak c}) \le \prod_{e\in\mathfrak c}\frac{\mathrm{snr}_e}{1+\mathrm{snr}_e} < 1$ and $\rho(\bar A_{\mathfrak c}) = 1$ for every tuple of priors $(P_1,\dots,P_N)$.
  2. Whenever $(\hat R_1,\dots,\hat R_N)$ are not proportional, for every pair of senders $a \neq b$ with $\kappa_{ab} = \kappa(\hat R_a^{-1}\hat R_b) = \lambda_{\max}(\hat R_a^{-1}\hat R_b)/\lambda_{\min}(\hat R_a^{-1}\hat R_b) > 1$, there exists an explicit rank-1-limit family of priors $P_1(s,\varepsilon),\dots,P_N(s,\varepsilon) \succ 0$ achieving $\lim_{s\to\infty}\lim_{\varepsilon\to 0^+}\rho(A_{\mathfrak c}) = \frac{(\sqrt{\kappa_{ab}}+1)^2}{4\sqrt{\kappa_{ab}}} = \cosh^2(\frac{1}{4}d_{\mathrm H}(\hat R_a,\hat R_b)) > 1$. For $N=2$, choosing $\hat R_\ast$ in C6(2) as the metric geometric mean $\hat R_1\#\hat R_2 = \hat R_1^{1/2}(\hat R_1^{-1/2}\hat R_2\hat R_1^{-1/2})^{1/2}\hat R_1^{1/2}$ yields the exact supremum
     $$\sup_{P_1,P_2\succ 0}\rho(A_{\mathfrak c}) = \frac{\bigl(\sqrt{\kappa(\hat R_1^{-1}\hat R_2)}+1\bigr)^2}{4\sqrt{\kappa(\hat R_1^{-1}\hat R_2)}} = \cosh^2\Bigl(\frac{1}{4}d_{\mathrm H}(\hat R_1,\hat R_2)\Bigr).$$
- Status: proved
- Review: self
- Evidence: Complete proof in Section `Derivations` (Theorem 5); verified on 5,000 random proportional-noise cycles (0 amplifying for $A_{\mathfrak c}$ or $\bar A_{\mathfrak c}$), exact rational SymPy and floating-point attainment of $\frac{(\sqrt{\kappa}+1)^2}{4\sqrt{\kappa}}$ across $\sqrt{\kappa} \in \{11/10, 3/2, 2, 3, 5, 10\}$, and planted-error negative control NC3 (equal-trace/equal-determinant non-proportional noises amplify in $6/6$ test cases) in `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy.py` and `open_coh_amplification_noisy-checks/verify_coh_amplification_noisy_output.txt`.
- Depends on: C2, C6

## Failed routes

### R1: Extending the prior edge-ratio bound $\hat R_i \succeq X_{ii}$ of `prop:coh-no-amplification`(c) directly to posted posterior headers

- Tried: Checked whether posting the post-reception posterior covariance $\widetilde P_i^+ = P_i - P_i H_{i^-}^\top S_{i,i^-}^{-1} H_{i^-} P_i$ leaves the prior edge ratios $\mathfrak r_e = \lambda_{\max}(S_{ji}^{-1} X_{ii})$ of `thm:coh-amplification`(a) bounded by $1$ around the cycle.
- Failed because: When agent $i$'s incoming code $H_{i^-}$ and outgoing code $H_i$ are strongly correlated under $P_i$, reading $i^-$ collapses $\widetilde X_{ii}^+ = H_i \widetilde P_i^+ H_i^\top \ll X_{ii} = H_i P_i H_i^\top$, so $\hat R_i = \widetilde X_{ii}^+ + R_{c,i} \ll X_{ii}$ and $\mathfrak r_e > 1$ occurs in $4537/5000$ random trials (and $\mathfrak r_{1\to 2} = 440/91 > 4.83$ in our rational witness). The telescope had to be re-indexed at the posterior covariance $(\widetilde P_i^+)^{\pm 1/2}$ via the Kalman posterior-gain identity $\mathrm K_{i,i^-} = \widetilde P_i^+ H_{i^-}^\top \hat R_{i^-}^{-1}$ (C4).
- Reopen if: Senders post prior covariances $P_i$ instead of posterior covariances $P_i^+$, which reduces back to `prop:coh-no-amplification`(c).

### R2: Equal-trace or equal-determinant normalization of sender-specific noise covariances under a common code of rank $\ge 2$

- Tried: Tested whether requiring $\operatorname{tr}(\hat R_i) = \text{const}$ or $\det(\hat R_i) = \text{const}$ (so that no sender claims uniformly higher precision than another) suffices to exclude prior-free amplification under a common code $H$ of rank $r_c \ge 2$.
- Failed because: Amplification under a common code is driven by directional anisotropy between $\hat R_a$ and $\hat R_b$ (measured by the generalized condition number $\kappa(\hat R_a^{-1}\hat R_b) = \exp d_{\mathrm H}(\hat R_a,\hat R_b)$), not by scalar volume or trace: equal-trace, equal-determinant noises $\hat R_1 = \operatorname{diag}(m,1)$ and $\hat R_2 = \operatorname{diag}(1,m)$ have $\kappa(\hat R_2^{-1}\hat R_1) = m^2 > 1$ for every $m > 1$ and amplify with exact supremum $(m+1)^2/(4m) > 1$ (C7, NC3). Conversely, arbitrary scalar multiples $\hat R_i = \alpha_i \hat R_0$ with wildly different traces and determinants have $\kappa(\hat R_a^{-1}\hat R_b) = 1$ and never amplify.
- Reopen if: The priors $P_1,\dots,P_N$ are constrained to commute with $\hat R_1,\dots,\hat R_N$ in the coded coordinates, or the edge SNRs are bounded so that the Kantorovich projective-distance condition of C6(2) holds.

## Open obligations

- [ ] O1 (sessions: 1): Dispatch fresh-context verification to `@verifier` on the cleaned write-up of C1–C7 and record the verdict.

## Literature

| Claim | Source | Locator | Read depth | Date read | Verdict |
| --- | --- | --- | --- | --- | --- |
| Live cycle definitions and edge-ratio theorem | `Collective_Agents/sections/06_coherence.tex` | `def:coh-cycle-product`, `thm:coh-amplification` (lines 108–127) | full subsection | 2026-11-21 | exact definitions of $A_{ji}, A_{\mathfrak c}, \bar A_{\mathfrak c}, \mathfrak r_e, \mathrm{snr}_e$ matched |
| Live amplification exclusions, examples, and open problem | `Collective_Agents/sections/s06_coherence.tex` | `prop:coh-no-amplification`, `ex:coh-amplification`, `obs:coh-amplification-information`, `open:coh-amplification-noisy` (lines 110–146) | full subsection | 2026-11-21 | all four clauses of `prop:coh-no-amplification` and open problem statement matched |
| Live proofs and rank-1 factorization lemma | `Collective_Agents/sections/app06_coherence.tex` | `app:coh-amplification`, `lem:coh-rank-one` (lines 109–145) | full proof section | 2026-11-21 | exact proofs of `thm:coh-amplification`, `prop:coh-no-amplification`, and `lem:coh-rank-one` verified |
| Live reception and level-0/level-1 definitions | `Collective_Agents/sections/02_framework.tex` | `prop:fw-update-subspace`, `prop:fw-prior-completion`, `def:fw-levels`, `def:fw-level0` (lines 46–85, 135–145, 313–330) | full subsections | 2026-11-21 | posterior covariance update $P_i^+ = P_i - \mathrm K\hat H P_i$ and level-1 law headers matched |

## Searches

| Query | Tool | Date | Not searched |
| --- | --- | --- | --- |
| Internal manuscript search for `coh-amplification`, `A_{1N}`, `law header`, `posted covariance` | `Select-String` across `Collective_Agents/sections/*.tex` | 2026-11-21 | External literature on Kantorovich inequalities and distributed Kalman cycles (all linear-algebra lemmas proved self-contained here) |

## Log

- 2026-11-21: Opened record for `open:coh-amplification-noisy`. Investigated all three parts (a), (b), and (c): refuted the naive extension of `thm:coh-amplification`(b) to noisy round-trip maps and proved the exact coded reduction and return-noiseless bound for $\bar A_{\mathfrak c}$ (C1, C2) as well as the full $N$-agent sequential and synchronous circulation characterization (C3); proved the Posterior Edge-Ratio Theorem resolving dynamic/sequential posterior covariance posting and identified the exact lag mechanism by which pre-prediction filtered posterior headers can still amplify in dynamic worlds with process noise (C4, C5); proved the cyclic noise-spread bound, the Kantorovich projective-distance bound, the necessary and sufficient proportional-noise characterization $\hat R_i = \alpha_i \hat R_0$, and the exact $N=2$ supremum $\cosh^2(\frac{1}{4}d_{\mathrm H}(\hat R_1,\hat R_2))$ for a common code of rank $\ge 2$ with sender-specific noise covariances (C6, C7). Executed two-channel verification script `verify_coh_amplification_noisy.py` with three planted-error negative controls (NC1–NC3) and captured output in `verify_coh_amplification_noisy_output.txt`. Reporting gate: (1) answers all three parts of `open:coh-amplification-noisy` literally and in their intended generality; (2) avoids treating only the single-agent round-trip map $\bar A_{\mathfrak c}$ without full $N$-agent circulation (C3), and avoids treating only finite-SNR noise-spread conditions without characterizing prior-free universal exclusion (C7); (3) strongest referee objections (why $\hat R_N$ cancels in $\bar A_{\mathfrak c}$, why $\mathrm K_{i,i^-} = \widetilde P_i^+ H_{i^-}^\top \hat R_{i^-}^{-1}$ holds and why its norm is $\mathrm{snr}/(1+\mathrm{snr})$, and why Kantorovich's bound extends from rank-1 projections to all $0 \preceq E \preceq s I_{r_c}$) are proved step-by-step from elementary linear algebra without external black boxes; (4) no unapproved approximations or uncertain citations; (5) obligation O1 (fresh-context check by `@verifier`) ready to dispatch. Next action: lint record, write cleaned write-up in scratch folder, and request fresh-context proof check from `@verifier`.

---

## Derivations

### Part (a): Noisy Circulation — Single-Agent Round-Trip Map $\bar A_{\mathfrak c}$ and Full $N$-Agent Persistent Circulation (Claims C1, C2, C3)

#### Proposition 1 (Direct-sum decomposition and rank-1 spectrum of the noisy round-trip map — Claim C1)

Let $\mathfrak c = (1 \to 2 \to \dots \to N \to 1)$ be a directed cycle of $N \ge 2$ agents with prior covariances $P_j \in \mathbb S_{++}^K$, effective codes $H_i \in \mathbb R^{r_i \times K}$ of full row rank $r_i \le K$, and assigned noise covariances $\hat R_i \in \mathbb S_+^{r_i}$ such that $S_{ji} = X_{ji} + \hat R_i \in \mathbb S_{++}^{r_i}$, where $X_{ji} = H_i P_j H_i^\top$ and $X_{ii} = H_i P_i H_i^\top$. Let $A_{ji} = \mathrm K_{ji} H_i = P_j H_i^\top S_{ji}^{-1} H_i$ be the edge gain-code map, $A_{\mathfrak c} = A_{1N} A_{N,N-1} \cdots A_{21}$ the cycle product, and
$$\bar A_{\mathfrak c} = (I_K - A_{1N}) + A_{\mathfrak c}$$
the round-trip map at base agent $1$ (`thm:coh-amplification`(b)).

1. (**Invariant subspace and unit eigenvalues** — Identity): Define $V_1 := \operatorname{col}(P_1 H_N^\top) \subseteq \mathbb R^K$. Since $H_N$ has full row rank $r_N$ and $P_1, S_{1N} \succ 0$, $\dim V_1 = r_N$ and $\dim \ker(H_N) = K - r_N$. If $v \in V_1 \cap \ker(H_N)$, then $v = P_1 H_N^\top u$ for some $u \in \mathbb R^{r_N}$ and $0 = H_N v = H_N P_1 H_N^\top u = X_{1N} u$; since $X_{1N} \succ 0$, $u = 0$ and $v = 0$. Hence
   $$\mathbb R^K = V_1 \oplus \ker(H_N).$$
   Because $A_{1N} = P_1 H_N^\top S_{1N}^{-1} H_N$ and $A_{\mathfrak c} = A_{1N}(A_{N,N-1}\cdots A_{21})$, every vector $x \in \mathbb R^K$ satisfies $A_{1N} x \in V_1$ and $A_{\mathfrak c} x \in V_1$, so $\bar A_{\mathfrak c}(V_1) \subseteq V_1$, while for $w \in \ker(H_N)$, $(I_K - A_{1N})w = w$ and $A_{\mathfrak c} w \in V_1$. In any basis adapted to $V_1 \oplus \ker(H_N)$, $\bar A_{\mathfrak c}$ is block upper triangular with diagonal blocks $\bar A_{\mathfrak c}\big|_{V_1} = (I_{V_1} - A_{1N}\big|_{V_1}) + A_{\mathfrak c}\big|_{V_1}$ on $V_1$ and $I_{\ker(H_N)}$ on $\ker(H_N)$. Consequently,
   $$\operatorname{spec}(\bar A_{\mathfrak c}) = \operatorname{spec}\bigl(\bar A_{\mathfrak c}\big|_{V_1}\bigr) \cup \{1\text{ with algebraic multiplicity }K - r_N\}.$$

2. (**Exact rank-1 formula** — Identity): When all codes have rank $r_i = 1$, write $H_i = \bm h_i^\top$ ($\bm h_i \in \mathbb R^K \setminus \{0\}$). Then $V_1 = \operatorname{span}(P_1 \bm h_N)$ is one-dimensional. On $V_1$:
   - $A_{1N}(P_1 \bm h_N) = P_1 \bm h_N (\bm h_N^\top P_1 \bm h_N + \hat R_N)^{-1} (\bm h_N^\top P_1 \bm h_N) = s_{1N} (P_1 \bm h_N)$, where
     $$s_{1N} := \frac{\|\bm h_N\|_{P_1}^2}{\|\bm h_N\|_{P_1}^2 + \hat R_N} = \frac{\mathrm{snr}_{N\to 1}}{1 + \mathrm{snr}_{N\to 1}} \in (0, 1].$$
   - Since $\operatorname{ran}(A_{\mathfrak c}) \subseteq V_1$ and $\dim V_1 = 1$, $A_{\mathfrak c}$ acts on $V_1$ as multiplication by its trace $\operatorname{tr}(A_{\mathfrak c})$.
   Therefore $\bar A_{\mathfrak c}\big|_{V_1}$ is multiplication by the scalar
   $$\lambda_{\mathrm{rt}}^{(1)} = (1 - s_{1N}) + \operatorname{tr}(A_{\mathfrak c}).$$
   When $K > 1$, $\operatorname{spec}(\bar A_{\mathfrak c}) = \{\lambda_{\mathrm{rt}}^{(1)}, 1,\dots,1\}$, so $\rho(\bar A_{\mathfrak c}) = \max\{|\lambda_{\mathrm{rt}}^{(1)}|, 1\}$, and $\rho(\bar A_{\mathfrak c}) > 1$ if and only if
   $$\operatorname{tr}(A_{\mathfrak c}) > s_{1N} \qquad \text{or} \qquad \operatorname{tr}(A_{\mathfrak c}) < -(2 - s_{1N}).$$
   By `lem:coh-rank-one`, $\operatorname{tr}(A_{\mathfrak c}) = \tau^\circ \prod_{i=1}^N s_{i^+,i}$ where $\tau^\circ := \prod_{j=1}^N \cos_{P_j}(\bm h_j, \bm h_{j^-}) \cdot \mathfrak M_{\mathfrak c}$ and $\mathfrak M_{\mathfrak c} = \prod_{i=1}^N \frac{\|\bm h_i\|_{P_i}}{\|\bm h_i\|_{P_{i^+}}}$, so the threshold $\operatorname{tr}(A_{\mathfrak c}) > s_{1N}$ is equivalently
   $$\frac{\operatorname{tr}(A_{\mathfrak c})}{s_{1N}} = \tau^\circ \prod_{i=1}^{N-1} s_{i+1, i} > 1,$$
   which is independent of $\hat R_N$.

3. (**Exact rational counterexamples refuting $\rho(\bar A_{\mathfrak c}) = \max\{\rho(A_{\mathfrak c}), 1\}$ and base-point invariance** — Proposition):
   Take $K = 2, N = 2$, $\bm h_1 = (0, 1)^\top$, and $\bm h_2 = (1, 0)^\top$.
   - *Counterexample C1(a) ($\rho(A_{\mathfrak c}) < 1 < \rho(\bar A_{\mathfrak c}^{(1)})$ and base-point asymmetry $\rho(\bar A_{\mathfrak c}^{(2)}) = 1$)*:
     Let $P_1 = \begin{pmatrix} 1 & 3/2 \\ 3/2 & 4 \end{pmatrix} \succ 0$ ($\det P_1 = 7/4$), $P_2 = \begin{pmatrix} 4 & 3/2 \\ 3/2 & 1 \end{pmatrix} \succ 0$, $\hat R_1 = 1/2$, and $\hat R_2 = 2$. Then $\|\bm h_1\|_{P_2}^2 = (P_2)_{22} = 1$, $\|\bm h_2\|_{P_1}^2 = (P_1)_{11} = 1$, so $s_{21} = \frac{1}{1 + 1/2} = \frac{2}{3}$ and $s_{12} = \frac{1}{1 + 2} = \frac{1}{3}$. By `lem:coh-rank-one`,
     $$\operatorname{tr}(A_{\mathfrak c}) = \frac{(P_1)_{21}(P_2)_{12}}{(1 + \hat R_1)(1 + \hat R_2)} = \frac{(3/2)(3/2)}{(3/2)(3)} = \frac{1}{2},$$
     so $\rho(A_{\mathfrak c}) = 1/2 < 1$. At base agent $1$, $\lambda_{\mathrm{rt}}^{(1)} = (1 - s_{12}) + \operatorname{tr}(A_{\mathfrak c}) = \frac{2}{3} + \frac{1}{2} = \frac{7}{6} > 1$, so $\rho(\bar A_{\mathfrak c}^{(1)}) = 7/6 > 1$. At base agent $2$, $\lambda_{\mathrm{rt}}^{(2)} = (1 - s_{21}) + \operatorname{tr}(A_{\mathfrak c}) = \frac{1}{3} + \frac{1}{2} = \frac{5}{6} < 1$, so $\rho(\bar A_{\mathfrak c}^{(2)}) = 1$.
   - *Counterexample C1(a') ($\rho(A_{\mathfrak c}) < 1 < \rho(\bar A_{\mathfrak c}^{(1)})$ even when $\hat R_i \succeq X_{ii}$ on every edge as in `prop:coh-no-amplification`(c))*:
     Let $P_1 = \begin{pmatrix} 1 & 3 \\ 3 & 10 \end{pmatrix} \succ 0$ ($\det P_1 = 1$), $P_2 = \begin{pmatrix} 100 & 25 \\ 25 & 7 \end{pmatrix} \succ 0$ ($\det P_2 = 75$), $\hat R_1 = 10 = X_{11}$, and $\hat R_2 = 100 = X_{22}$. Then $s_{21} = \frac{7}{7+10} = \frac{7}{17}$, $s_{12} = \frac{1}{1+100} = \frac{1}{101}$, and $\operatorname{tr}(A_{\mathfrak c}) = \frac{3 \times 25}{17 \times 101} = \frac{75}{1717} < 1$, yet $\lambda_{\mathrm{rt}}^{(1)} = \frac{100}{101} + \frac{75}{1717} = \frac{1775}{1717} > 1$.
   - *Counterexample C1(b) ($\rho(A_{\mathfrak c}) > 1 = \rho(\bar A_{\mathfrak c}^{(1)})$)*:
     Let $P_1 = \begin{pmatrix} 1 & 2 \\ 2 & 5 \end{pmatrix} \succ 0$ ($\det P_1 = 1$), $P_2 = \begin{pmatrix} 5 & -2 \\ -2 & 1 \end{pmatrix} \succ 0$ ($\det P_2 = 1$), $\hat R_1 = 2/3$, and $\hat R_2 = 1$. Then $s_{21} = \frac{1}{1 + 2/3} = \frac{3}{5}$, $s_{12} = \frac{1}{1 + 1} = \frac{1}{2}$, and $\operatorname{tr}(A_{\mathfrak c}) = \frac{(2)(-2)}{(5/3)(2)} = -\frac{6}{5}$, so $\rho(A_{\mathfrak c}) = 6/5 > 1$. Yet $\lambda_{\mathrm{rt}}^{(1)} = (1 - \frac{1}{2}) - \frac{6}{5} = -\frac{7}{10} \in (-1, 1)$, so $\rho(\bar A_{\mathfrak c}^{(1)}) = 1$ and $\bar A_{\mathfrak c}^{(1)}$ has a simple spectrum on the unit circle, so $\|(\bar A_{\mathfrak c}^{(1)})^n\|$ remains bounded as $n \to \infty$. $\square$

*Checkpoint 1 (after Proposition 1)*:
1. Signs: $(I - A_{1N}) + A_{\mathfrak c}$ adds positive retention $1 - s_{1N} \in [0, 1)$ to $\operatorname{tr}(A_{\mathfrak c})$, shifting positive eigenvalues upward and negative eigenvalues toward zero.
2. Factors: No factors of 2 or $\pi$; $s_{1N}$ divides out of $\operatorname{tr}(A_{\mathfrak c})$ in the ratio $\operatorname{tr}(A_{\mathfrak c})/s_{1N}$.
3. Conventions: Matches `thm:coh-amplification`(b) at $\hat R_N = 0$, where $s_{1N} = 1$ gives $\lambda_{\mathrm{rt}}^{(1)} = \operatorname{tr}(A_{\mathfrak c})$.
4. Type: $\bar A_{\mathfrak c} \in \mathbb R^{K \times K}$ is a linear operator on world-coordinate belief perturbations; $\lambda_{\mathrm{rt}}^{(1)} \in \mathbb R$ is its eigenvalue on $V_1$.

---

#### Theorem 1 (Exact coded reduction and sharp return-noiseless bound for $\bar A_{\mathfrak c}$ — Claim C2)

Under the hypotheses of Proposition 1, define $\Phi_1 := P_1 H_N^\top X_{1N}^{-1/2} \in \mathbb R^{K \times r_N}$ and $\Phi_1^+ := X_{1N}^{-1/2} H_N \in \mathbb R^{r_N \times K}$, where $X_{1N} = H_N P_1 H_N^\top \in \mathbb S_{++}^{r_N}$.

1. (**Exact coded similarity on $V_1$** — Identity): Direct multiplication gives
   $$\Phi_1^+ \Phi_1 = X_{1N}^{-1/2} (H_N P_1 H_N^\top) X_{1N}^{-1/2} = I_{r_N}, \qquad \Phi_1 \Phi_1^+ = P_1 H_N^\top X_{1N}^{-1} H_N = \mathcal P_{1N},$$
   where $\mathcal P_{1N}$ is the noiseless projector onto $V_1 = \operatorname{col}(P_1 H_N^\top)$ along $\ker(H_N)$. Thus $\Phi_1 : \mathbb R^{r_N} \to V_1$ is a linear isomorphism with inverse $\Phi_1^+\big|_{V_1}$. Moreover,
   $$\Phi_1^+ A_{1N} = X_{1N}^{-1/2} (H_N P_1 H_N^\top) S_{1N}^{-1} H_N = (X_{1N}^{1/2} S_{1N}^{-1} X_{1N}^{1/2})(X_{1N}^{-1/2} H_N) = \Sigma_{1N} \Phi_1^+,$$
   where $\Sigma_{1N} := X_{1N}^{1/2} S_{1N}^{-1} X_{1N}^{1/2} \in \mathbb S_{++}^{r_N}$. Since $S_{1N} = X_{1N} + \hat R_N \succeq X_{1N} \succ 0$, we have $X_{1N}^{-1/2} S_{1N} X_{1N}^{-1/2} = I_{r_N} + X_{1N}^{-1/2}\hat R_N X_{1N}^{-1/2} \succeq I_{r_N}$, and inverting gives $0 \prec \Sigma_{1N} \preceq I_{r_N}$. Conjugating $\bar A_{\mathfrak c}\big|_{V_1}$ by $\Phi_1$ yields
   $$M_{\mathrm{rt}}^{(1)} := \Phi_1^+ \bar A_{\mathfrak c}\big|_{V_1} \Phi_1 = I_{r_N} - \Sigma_{1N} + \Sigma_{1N} \tilde{\mathcal C}_{\mathfrak c},$$
   where
   $$\tilde{\mathcal C}_{\mathfrak c} := \Phi_1^+ A_{N,N-1}\cdots A_{21} \Phi_1 = \Phi_1^+ \bigl(\mathcal P_{1N} A_{N,N-1}\cdots A_{21}\bigr) \Phi_1.$$

2. (**Cauchy--Schwarz matrix-convexity bound** — Proposition): Conjugate $M_{\mathrm{rt}}^{(1)}$ by $\Sigma_{1N}^{-1/2}$:
   $$\widehat M_{\mathrm{rt}}^{(1)} := \Sigma_{1N}^{-1/2} M_{\mathrm{rt}}^{(1)} \Sigma_{1N}^{1/2} = (I_{r_N} - \Sigma_{1N}) + \Sigma_{1N}^{1/2} \tilde{\mathcal C}_{\mathfrak c} \Sigma_{1N}^{1/2}.$$
   Since $0 \prec \Sigma_{1N} \preceq I_{r_N}$, both $I_{r_N} - \Sigma_{1N} \succeq 0$ and $\Sigma_{1N} \succ 0$ have symmetric square roots. For any vectors $u, v \in \mathbb R^{r_N}$,
   $$\begin{aligned}
   \bigl|u^\top \widehat M_{\mathrm{rt}}^{(1)} v\bigr| &\le \bigl|u^\top (I_{r_N} - \Sigma_{1N}) v\bigr| + \bigl|(\Sigma_{1N}^{1/2} u)^\top \tilde{\mathcal C}_{\mathfrak c} (\Sigma_{1N}^{1/2} v)\bigr| \\
   &\le \|(I_{r_N} - \Sigma_{1N})^{1/2} u\|_2 \, \|(I_{r_N} - \Sigma_{1N})^{1/2} v\|_2 + \|\tilde{\mathcal C}_{\mathfrak c}\|_2 \, \|\Sigma_{1N}^{1/2} u\|_2 \, \|\Sigma_{1N}^{1/2} v\|_2 \\
   &\le \max\bigl\{1, \|\tilde{\mathcal C}_{\mathfrak c}\|_2\bigr\} \sqrt{\|(I_{r_N} - \Sigma_{1N})^{1/2} u\|_2^2 + \|\Sigma_{1N}^{1/2} u\|_2^2} \sqrt{\|(I_{r_N} - \Sigma_{1N})^{1/2} v\|_2^2 + \|\Sigma_{1N}^{1/2} v\|_2^2} \\
   &= \max\bigl\{1, \|\tilde{\mathcal C}_{\mathfrak c}\|_2\bigr\} \|u\|_2 \|v\|_2,
   \end{aligned}$$
   where the third line uses the two-term Cauchy--Schwarz inequality $a_1 b_1 + a_2 b_2 \le \sqrt{a_1^2 + a_2^2}\sqrt{b_1^2 + b_2^2}$ and the last line uses $\|(I_{r_N} - \Sigma_{1N})^{1/2} u\|_2^2 + \|\Sigma_{1N}^{1/2} u\|_2^2 = u^\top (I_{r_N} - \Sigma_{1N} + \Sigma_{1N}) u = \|u\|_2^2$. Taking the supremum over $\|u\|_2 = \|v\|_2 = 1$ gives
   $$\rho(M_{\mathrm{rt}}^{(1)}) \le \|\widehat M_{\mathrm{rt}}^{(1)}\|_2 \le \max\bigl\{1, \|\tilde{\mathcal C}_{\mathfrak c}\|_2\bigr\}.$$

3. (**Return-noiseless edge-ratio bound** — Proposition): Insert $P_k^{1/2} P_k^{-1/2} = I_K$ between consecutive factors of $\tilde{\mathcal C}_{\mathfrak c} = X_{1N}^{-1/2} H_N A_{N,N-1}\cdots A_{21} P_1 H_N^\top X_{1N}^{-1/2}$:
   $$\tilde{\mathcal C}_{\mathfrak c} = \bigl[X_{1N}^{-1/2} H_N P_N^{1/2}\bigr] \tilde A_{(N-1\to N)} \cdots \tilde A_{(1\to 2)} \bigl[P_1^{1/2} H_N^\top X_{1N}^{-1/2}\bigr],$$
   where $\tilde A_e = P_j^{-1/2} A_{ji} P_i^{1/2}$ is the scaled edge map of `thm:coh-amplification`(a), satisfying $\|\tilde A_e\|_2 \le \bigl(\mathfrak r_e \frac{\mathrm{snr}_e}{1+\mathrm{snr}_e}\bigr)^{1/2}$. The right-hand bracket $U_{1N} := P_1^{1/2} H_N^\top X_{1N}^{-1/2}$ satisfies $U_{1N}^\top U_{1N} = X_{1N}^{-1/2} (H_N P_1 H_N^\top) X_{1N}^{-1/2} = I_{r_N}$, so $\|U_{1N}\|_2 = 1$. The left-hand bracket has squared spectral norm
   $$\bigl\|X_{1N}^{-1/2} H_N P_N^{1/2}\bigr\|_2^2 = \lambda_{\max}\bigl(X_{1N}^{-1/2} H_N P_N H_N^\top X_{1N}^{-1/2}\bigr) = \lambda_{\max}\bigl(X_{1N}^{-1} X_{NN}\bigr) = \mathfrak r_{N\to 1}^\circ.$$
   Submultiplicativity of $\|\cdot\|_2$ yields $\|\tilde{\mathcal C}_{\mathfrak c}\|_2 \le (\mathfrak r_{N\to 1}^\circ)^{1/2} \prod_{e\neq(N\to 1)} \bigl(\mathfrak r_e \frac{\mathrm{snr}_e}{1+\mathrm{snr}_e}\bigr)^{1/2}$, and combining with Proposition 1(1) proves C2. Under a common prior $P_j = P$, $\mathfrak r_{N\to 1}^\circ = 1$ and $\mathfrak r_e = \frac{\mathrm{snr}_e}{1+\mathrm{snr}_e} \le 1$, so $\rho(\bar A_{\mathfrak c}) = 1$; under heterogeneous priors, $X_{ii} \preceq e^{\operatorname{sp}(P_i\Vert P_j)} X_{ji}$ gives $\mathfrak r_{N\to 1}^\circ \le e^{\operatorname{sp}(P_N\Vert P_1)}$ and $\mathfrak r_e \le e^{\operatorname{sp}(P_i\Vert P_j)} \frac{\mathrm{snr}_e}{1+\mathrm{snr}_e}$, so $\rho(\bar A_{\mathfrak c}) = 1$ whenever $\sum_{(i\to j)\in\mathfrak c}\operatorname{sp}(P_i\Vert P_j) \le 2\sum_{e\neq(N\to 1)}\ln(1+\mathrm{snr}_e^{-1})$. $\square$

---

#### Theorem 2 (Full $N$-agent persistent noisy circulation — Claim C3)

Consider the $N$-agent state $x = (x_1,\dots,x_N) \in (\mathbb R^K)^N$ updated along the cycle $\mathfrak c$ by $x_k^+ = (I_K - A_{k,k-1})x_k + A_{k,k-1} x_{k-1}$ (indices modulo $N$), either synchronously ($x_k(t+1) = (I_K - A_{k,k-1})x_k(t) + A_{k,k-1}x_{k-1}(t)$, operator $\mathcal T_{\mathrm{sync}}$) or sequentially in the sweep order $k = 2, 3, \dots, N, 1$ ($x_k^{(n)} = (I_K - A_{k,k-1})x_k^{(n-1)} + A_{k,k-1}x_{k-1}^{\mathrm{curr}}$, operator $\mathcal T_{\mathrm{seq}}$).

1. (**Coded dynamics and multi-agent contraction under $\mathfrak r_e^\circ \le 1$** — Proposition): For each $k \in \{1,\dots,N\}$, decompose $\mathbb R^K = V_k \oplus \ker(H_{k-1})$ with $V_k = \operatorname{col}(P_k H_{k-1}^\top)$, $\Phi_k = P_k H_{k-1}^\top X_{k,k-1}^{-1/2}$, and $\Phi_k^+ = X_{k,k-1}^{-1/2} H_{k-1}$. On $\ker(H_{k-1})$, $I_K - A_{k,k-1}$ acts as the identity and $A_{k,k-1}$ maps all of $\mathbb R^K$ into $V_k$. On the invariant subspace $\bigoplus_{k=1}^N V_k$, setting $z_k = \Phi_k^+ x_k \in \mathbb R^{r_{k-1}}$ ($x_k = \Phi_k z_k$) and using $\Phi_k^+ A_{k,k-1} = \Sigma_{k,k-1} \Phi_k^+$ from Theorem 1(1) gives
   $$z_k^+ = (I_{r_{k-1}} - \Sigma_{k,k-1}) z_k + \Sigma_{k,k-1} \tilde C_{k,k-1} z_{k-1},$$
   where $\Sigma_{k,k-1} = X_{k,k-1}^{1/2} S_{k,k-1}^{-1} X_{k,k-1}^{1/2}$ ($0 \prec \Sigma_{k,k-1} \preceq I_{r_{k-1}}$) and
   $$\tilde C_{k,k-1} := \Phi_k^+ \Phi_{k-1} = \bigl[X_{k,k-1}^{-1/2} H_{k-1} P_{k-1}^{1/2}\bigr]\bigl[P_{k-1}^{1/2} H_{k-2}^\top X_{k-1,k-2}^{-1/2}\bigr].$$
   The right factor of $\tilde C_{k,k-1}$ is an isometry ($\|P_{k-1}^{1/2} H_{k-2}^\top X_{k-1,k-2}^{-1/2}\|_2 = 1$) and the left factor has norm $(\mathfrak r_{k-1\to k}^\circ)^{1/2} = \lambda_{\max}(X_{k,k-1}^{-1} X_{k-1,k-1})^{1/2}$, so $\|\tilde C_{k,k-1}\|_2 \le (\mathfrak r_{k-1\to k}^\circ)^{1/2}$.
   Changing variables to $\hat z_k := \Sigma_{k,k-1}^{-1/2} z_k$ gives
   $$\hat z_k^+ = (I_{r_{k-1}} - \Sigma_{k,k-1}) \hat z_k + \Sigma_{k,k-1}^{1/2} \tilde C_{k,k-1} \Sigma_{k-1,k-2}^{1/2} \hat z_{k-1}.$$
   For any unit vector $u \in \mathbb R^{r_{k-1}}$, the exact same two-term Cauchy--Schwarz inequality as in Theorem 1(2) gives
   $$\begin{aligned}
   \bigl|u^\top \hat z_k^+\bigr| &\le \|(I - \Sigma_{k,k-1})^{1/2} u\|_2 \, \|(I - \Sigma_{k,k-1})^{1/2} \hat z_k\|_2 + \|\tilde C_{k,k-1}\|_2 \, \|\Sigma_{k,k-1}^{1/2} u\|_2 \, \|\Sigma_{k-1,k-2}^{1/2} \hat z_{k-1}\|_2 \\
   &\le \sqrt{\|(I - \Sigma_{k,k-1})^{1/2} \hat z_k\|_2^2 + \|\tilde C_{k,k-1}\|_2^2 \, \|\hat z_{k-1}\|_2^2} \\
   &\le \max\bigl\{\|\hat z_k\|_2,\; (\mathfrak r_{k-1\to k}^\circ)^{1/2} \|\hat z_{k-1}\|_2\bigr\},
   \end{aligned}$$
   since $\|\Sigma_{k-1,k-2}^{1/2} \hat z_{k-1}\|_2 \le \|\hat z_{k-1}\|_2$ and $\|(I - \Sigma_{k,k-1})^{1/2}\hat z_k\|_2^2 + \|\Sigma_{k,k-1}^{1/2}\hat z_k\|_2^2 = \|\hat z_k\|_2^2$. Therefore, if $\mathfrak r_e^\circ \le 1$ on every edge $e \in \mathfrak c$ (in particular, when $P_j = P$ is a common prior), $\|\hat z_k^+\|_2 \le \max\{\|\hat z_k\|_2, \|\hat z_{k-1}\|_2\}$ at every step, so $\max_{1\le k\le N} \|\hat z_k\|_2$ is nonincreasing under both $\mathcal T_{\mathrm{sync}}$ and $\mathcal T_{\mathrm{seq}}$, proving $\rho(\mathcal T_{\mathrm{sync}}) \le 1$ and $\rho(\mathcal T_{\mathrm{seq}}) \le 1$.

2. (**Exact rank-1 characteristic equations and noise-invariance of instability** — Proposition): When $r_i = 1$ ($H_i = \bm h_i^\top$), $\Sigma_{k,k-1} = s_{k,k-1} \in (0, 1]$ and $\prod_{k=1}^N \Sigma_{k,k-1}\tilde C_{k,k-1} = \operatorname{tr}(A_{\mathfrak c}) = \tau^\circ \prod_{k=1}^N s_{k,k-1}$ with $\tau^\circ = \operatorname{tr}(A_{\mathfrak c}^{\mathrm{noiseless}})$.
   - Under $\mathcal T_{\mathrm{sync}}$, an eigenvector $z \neq 0$ with eigenvalue $\lambda$ satisfies $(\lambda - (1 - s_{k,k-1})) z_k = s_{k,k-1} \tilde C_{k,k-1} z_{k-1}$ for all $k = 1,\dots,N$. Multiplying these $N$ scalar equations around the cycle gives
     $$P_{\mathrm{sync}}(\lambda) := \prod_{k=1}^N \bigl(\lambda - (1 - s_{k,k-1})\bigr) - \tau^\circ \prod_{k=1}^N s_{k,k-1} = 0.$$
   - Under $\mathcal T_{\mathrm{seq}}$ (sweep order $k = 2, 3, \dots, N, 1$), at step $k = 2$ agent 2 reads agent 1's old state $z_1$, whereas at steps $k = 3,\dots,N, 1$ agent $k$ reads agent $k-1$'s newly updated state $\lambda z_{k-1}$. Hence $(\lambda - (1 - s_{21})) z_2 = s_{21} \tilde C_{21} z_1$ and $(\lambda - (1 - s_{k,k-1})) z_k = \lambda s_{k,k-1} \tilde C_{k,k-1} z_{k-1}$ for $k \in \{3,\dots,N, 1\}$. Multiplying the $N$ equations around the cycle gives
     $$P_{\mathrm{seq}}(\lambda) := \prod_{k=1}^N \bigl(\lambda - (1 - s_{k,k-1})\bigr) - \lambda^{N-1} \tau^\circ \prod_{k=1}^N s_{k,k-1} = 0.$$
   - *Case $|\tau^\circ| \le 1$*: For any $\lambda \in \mathbb C$ with $|\lambda| > 1$ and any $s_k \in (0, 1]$, since $1 - s_k \ge 0$, the reverse triangle inequality gives
     $$|\lambda - (1 - s_k)| \ge |\lambda| - (1 - s_k) > 1 - (1 - s_k) = s_k > 0, \qquad \left|\frac{\lambda - (1 - s_k)}{\lambda}\right| \ge 1 - \frac{1 - s_k}{|\lambda|} > s_k > 0.$$
     Multiplying over $k=1,\dots,N$ yields $\prod_{k=1}^N |\lambda - (1 - s_k)| > \prod_{k=1}^N s_k \ge |\tau^\circ|\prod_{k=1}^N s_k$ and $|\lambda|^{-(N-1)}\prod_{k=1}^N |\lambda - (1 - s_k)| > \prod_{k=1}^N s_k \ge |\tau^\circ|\prod_{k=1}^N s_k$. Thus neither $P_{\mathrm{sync}}$ nor $P_{\mathrm{seq}}$ has any root with $|\lambda| > 1$, so $\rho(\mathcal T_{\mathrm{sync}}) \le 1$ and $\rho(\mathcal T_{\mathrm{seq}}) \le 1$.
   - *Case $\tau^\circ > 1$*: At $\lambda = 1$, both polynomials evaluate to
     $$P_{\mathrm{sync}}(1) = P_{\mathrm{seq}}(1) = \prod_{k=1}^N \bigl(1 - (1 - s_{k,k-1})\bigr) - \tau^\circ \prod_{k=1}^N s_{k,k-1} = (1 - \tau^\circ)\prod_{k=1}^N s_{k,k-1} < 0,$$
     because every $s_{k,k-1} > 0$ and $\tau^\circ > 1$, whereas $\lim_{\lambda\to+\infty} P_{\mathrm{sync}}(\lambda) = \lim_{\lambda\to+\infty} P_{\mathrm{seq}}(\lambda) = +\infty$. By the intermediate value theorem, both $P_{\mathrm{sync}}$ and $P_{\mathrm{seq}}$ have a real root $\lambda > 1$ for every choice of finite assigned noises $\hat R_1,\dots,\hat R_N \ge 0$. $\square$

*Checkpoint 2 (after Theorems 1 and 2)*:
1. Signs: $P_{\mathrm{sync}}(1) = P_{\mathrm{seq}}(1) = (1 - \tau^\circ)\prod_k s_{k,k-1}$ flips sign from $\ge 0$ to $< 0$ as $\tau^\circ$ crosses $1$.
2. Factors: All $N$ noise factors $\prod_{k=1}^N s_{k,k-1}$ cancel at $\lambda = 1$ in $N$-agent persistent circulation, whereas only the single return factor $s_{1N}$ cancels in the single-agent round-trip map $\bar A_{\mathfrak c}$.
3. Conventions: At $\hat R_i = 0$, $s_{k,k-1} = 1$, so $P_{\mathrm{seq}}(\lambda) = \lambda^N - \lambda^{N-1}\tau^\circ = \lambda^{N-1}(\lambda - \tau^\circ)$, recovering the noiseless eigenvalue $\lambda = \tau^\circ$.
4. Type: $\mathcal T_{\mathrm{sync}}, \mathcal T_{\mathrm{seq}} \in \mathbb R^{NK \times NK}$ act on stacked world-coordinate perturbations $(x_1,\dots,x_N)$.

---

### Part (b): Dynamic Cycles with Posted Posterior Covariances (Claims C4 and C5)

#### Theorem 3 (Posterior Edge-Ratio Theorem — Claim C4)

Let $\mathfrak c$ be a directed cycle of $N \ge 2$ agents with reception prior covariances $P_1,\dots,P_N \in \mathbb S_{++}^K$, codes $H_i \in \mathbb R^{r_i \times K}$, and assigned noise covariances $\hat R_i \in \mathbb S_{++}^{r_i}$. For each agent $i$, let $i^-$ be its predecessor and $i^+$ its successor on $\mathfrak c$, and let
$$\widetilde P_i^+ := P_i - P_i H_{i^-}^\top S_{i,i^-}^{-1} H_{i^-} P_i, \qquad \widetilde X_{ii}^+ := H_i \widetilde P_i^+ H_i^\top, \qquad \mathfrak r_{i\to i^+}^+ := \lambda_{\max}\bigl(\hat R_i^{-1} \widetilde X_{ii}^+\bigr)$$
be agent $i$'s post-reception posterior covariance after reading $i^-$ (`prop:fw-update-subspace`), its coded posterior covariance along its outgoing code $H_i$, and the posterior edge ratio on $e = (i \to i^+)$.

1. (**Kalman posterior-gain identity** — Identity): Define $\Lambda_i^+ := P_i^{-1} + H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-} \in \mathbb S_{++}^K$. Multiplying $\Lambda_i^+$ on the left by $P_i$ and on the right by $H_{i^-}^\top$ gives
   $$P_i \Lambda_i^+ P_i H_{i^-}^\top = P_i H_{i^-}^\top + P_i H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-} P_i H_{i^-}^\top = P_i H_{i^-}^\top \hat R_{i^-}^{-1} \bigl(\hat R_{i^-} + H_{i^-} P_i H_{i^-}^\top\bigr) = P_i H_{i^-}^\top \hat R_{i^-}^{-1} S_{i,i^-}.$$
   Also,
   $$\begin{aligned}
   \widetilde P_i^+ \Lambda_i^+ P_i &= \bigl(P_i - P_i H_{i^-}^\top S_{i,i^-}^{-1} H_{i^-} P_i\bigr)\bigl(I_K + H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-} P_i\bigr) \\
   &= P_i + P_i H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-} P_i - P_i H_{i^-}^\top S_{i,i^-}^{-1} \bigl(I_{r_{i^-}} + H_{i^-} P_i H_{i^-}^\top \hat R_{i^-}^{-1}\bigr) H_{i^-} P_i \\
   &= P_i + P_i H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-} P_i - P_i H_{i^-}^\top S_{i,i^-}^{-1} \bigl(S_{i,i^-} \hat R_{i^-}^{-1}\bigr) H_{i^-} P_i = P_i,
   \end{aligned}$$
   so $\widetilde P_i^+ = (\Lambda_i^+)^{-1} \in \mathbb S_{++}^K$. Multiplying $P_i \Lambda_i^+ P_i H_{i^-}^\top = P_i H_{i^-}^\top \hat R_{i^-}^{-1} S_{i,i^-}$ on the left by $\widetilde P_i^+ P_i^{-1}$ and on the right by $S_{i,i^-}^{-1}$ yields the exact identity
   $$\mathrm K_{i,i^-} = P_i H_{i^-}^\top S_{i,i^-}^{-1} = \widetilde P_i^+ H_{i^-}^\top \hat R_{i^-}^{-1}.$$

2. (**Coded posterior telescope and norm factorization** — Proposition): Write each edge map as $A_{i,i^-} = \mathrm K_{i,i^-} H_{i^-}$. Because $\operatorname{spec}(UV)\setminus\{0\} = \operatorname{spec}(VU)\setminus\{0\}$, the cycle product $A_{\mathfrak c} = A_{1N} \cdots A_{21} = \mathrm K_{1N} B_{N,N-1} \cdots B_{21} H_1$ has the same nonzero spectrum as the coded cycle product $B_{\mathfrak c} := B_{1N} B_{N,N-1} \cdots B_{21}$, where $B_{i,i^-} := H_i \mathrm K_{i,i^-} = H_i P_i H_{i^-}^\top S_{i,i^-}^{-1}$. Conjugating $B_{i,i^-}$ on the left by $\hat R_i^{-1/2}$ and on the right by $\hat R_{i^-}^{1/2}$ gives
   $$\widehat B_{i,i^-} := \hat R_i^{-1/2} B_{i,i^-} \hat R_{i^-}^{1/2} = \Bigl[\hat R_i^{-1/2} H_i (\widetilde P_i^+)^{1/2}\Bigr]\Bigl[(\widetilde P_i^+)^{-1/2} \mathrm K_{i,i^-} \hat R_{i^-}^{1/2}\Bigr].$$
   Around the cycle $\mathfrak c$, the factors $\hat R_i^{\pm 1/2}$ telescope: $\hat R_1^{-1/2} B_{\mathfrak c} \hat R_1^{1/2} = \widehat B_{1N} \widehat B_{N,N-1} \cdots \widehat B_{21}$.
   - The first bracket of $\widehat B_{i,i^-}$ has squared spectral norm
     $$\bigl\|\hat R_i^{-1/2} H_i (\widetilde P_i^+)^{1/2}\bigr\|_2^2 = \lambda_{\max}\bigl(\hat R_i^{-1/2} H_i \widetilde P_i^+ H_i^\top \hat R_i^{-1/2}\bigr) = \lambda_{\max}\bigl(\hat R_i^{-1} \widetilde X_{ii}^+\bigr) = \mathfrak r_{i\to i^+}^+.$$
   - For the second bracket $W_i := (\widetilde P_i^+)^{-1/2} \mathrm K_{i,i^-} \hat R_{i^-}^{1/2}$, using $\mathrm K_{i,i^-} = P_i H_{i^-}^\top S_{i,i^-}^{-1}$ in $W_i^\top$ and $\mathrm K_{i,i^-} = \widetilde P_i^+ H_{i^-}^\top \hat R_{i^-}^{-1}$ in $W_i$ gives
     $$\begin{aligned}
     W_i^\top W_i &= \hat R_{i^-}^{1/2} S_{i,i^-}^{-1} H_{i^-} P_i (\widetilde P_i^+)^{-1} \bigl(\widetilde P_i^+ H_{i^-}^\top \hat R_{i^-}^{-1}\bigr) \hat R_{i^-}^{1/2} \\
     &= \hat R_{i^-}^{1/2} S_{i,i^-}^{-1} X_{i,i^-} \hat R_{i^-}^{-1/2} = (I_{r_{i^-}} + Y_{i,i^-})^{-1} Y_{i,i^-},
     \end{aligned}$$
     where $Y_{i,i^-} := \hat R_{i^-}^{-1/2} X_{i,i^-} \hat R_{i^-}^{-1/2} \succeq 0$. Since $\lambda_{\max}(Y_{i,i^-}) = \mathrm{snr}_{i^-\to i}$, we have
     $$\|W_i\|_2^2 = \lambda_{\max}(W_i^\top W_i) = \frac{\mathrm{snr}_{i^-\to i}}{1 + \mathrm{snr}_{i^-\to i}} < 1.$$
   Multiplying the bounds over $i = 1,\dots,N$ gives
   $$\rho(A_{\mathfrak c}) = \rho(B_{\mathfrak c}) \le \prod_{i=1}^N \|\widehat B_{i,i^-}\|_2 \le \prod_{e\in\mathfrak c}\Bigl(\mathfrak r_e^+ \frac{\mathrm{snr}_e}{1+\mathrm{snr}_e}\Bigr)^{1/2} \le \prod_{e\in\mathfrak c}(\mathfrak r_e^+)^{1/2}.$$

3. (**Exclusion of amplification under post-reception posterior headers, with or without external sensing** — Corollary):
   - When sender $i$ posts a covariance header $P_i^+ \succeq \widetilde P_i^+$ (in particular, its exact post-reception posterior covariance $P_i^+ = \widetilde P_i^+$) and receiver $i^+$ reads at level 1 with $\hat R_i = H_i P_i^+ H_i^\top + R_{c,i}$ ($R_{c,i} \succeq 0, \hat R_i \succ 0$), we have $\hat R_i \succeq \widetilde X_{ii}^+$, so $\mathfrak r_{i\to i^+}^+ = \lambda_{\max}(\hat R_i^{-1}\widetilde X_{ii}^+) \le 1$ on every edge (with $\mathfrak r_{i\to i^+}^+ < 1$ whenever $R_{c,i} \succ 0$) and $\rho(A_{\mathfrak c}) \le \prod_{e\in\mathfrak c}\bigl(\frac{\mathrm{snr}_e}{1+\mathrm{snr}_e}\bigr)^{1/2} < 1$.
   - If agent $i$ also fuses an external/sensory signal of precision $\Gamma^{\mathrm{ext}}_i \succeq 0$, let $P_i^{\mathrm{ext}} := (P_i^{-1} + \Gamma^{\mathrm{ext}}_i)^{-1} \preceq P_i$ be its prior covariance after the external signal alone. Then its full posterior precision after both the external signal and predecessor $i^-$'s message is $(P_i^+)^{-1} = P_i^{-1} + \Gamma^{\mathrm{ext}}_i + H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-} = (P_i^{\mathrm{ext}})^{-1} + H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-}$, and the linear response of its full posterior mean $m_i^+$ to $m_{i^-}^+$ is $A_{i,i^-}^{\mathrm{post}} = P_i^+ H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-} = P_i^{\mathrm{ext}} H_{i^-}^\top (H_{i^-} P_i^{\mathrm{ext}} H_{i^-}^\top + \hat R_{i^-})^{-1} H_{i^-}$. Applying Part 2 with $P_i^{\mathrm{ext}}$ in place of $P_i$ shows that $\widetilde P_i^+ = P_i^+$, so posting $H_i P_i^+ H_i^\top$ again gives $\rho(A_{\mathfrak c}^{\mathrm{post}}) \le \prod_{e\in\mathfrak c}\bigl(\frac{\mathrm{snr}_e^{\mathrm{ext}}}{1+\mathrm{snr}_e^{\mathrm{ext}}}\bigr)^{1/2} < 1$. $\square$

---

#### Proposition 2 (Amplification under lagged pre-prediction filtered posterior headers in a dynamic world — Claim C5)

In the dynamic world $\eta_{t+1} = F\eta_t + w_t$ (`def:fw-level0`), suppose each agent $i$ starts round $t$ with predicted prior covariance $P_i^-(t) = F P_i^+(t-1) F^\top + Q_i$, forms its reception gain $\mathrm K_{i,i^-} = P_i^-(t) H_{i^-}^\top (H_{i^-} P_i^-(t) H_{i^-}^\top + \hat R_{i^-})^{-1}$ using $P_i^-(t)$, and reads sender $i^-$ with the lagged filtered posterior header $\hat R_{i^-} = H_{i^-} P_{i^-}^+(t-1) H_{i^-}^\top + R_{c,i^-}$ from the filtering step of round $t-1$ (before the prediction step $P_{i^-}^-(t) = F P_{i^-}^+(t-1) F^\top + Q_{i^-}$).
Take $K = 2, N = 2$, $F = \frac{1}{2} I_2$, $P_a^+(t-1) = P_b^+(t-1) = \frac{1}{5} I_2$, $R_c = \frac{1}{10}$, $\bm h_a = (0, 1)^\top$, $\bm h_b = (1, 0)^\top$, and process noise covariances
$$Q_a = P_a^- - \frac{1}{20} I_2 = \begin{pmatrix} 19/20 & \alpha\sqrt{x} \\ \alpha\sqrt{x} & x - 1/20 \end{pmatrix}, \qquad Q_b = P_b^- - \frac{1}{20} I_2 = \begin{pmatrix} x - 1/20 & \alpha\sqrt{x} \\ \alpha\sqrt{x} & 19/20 \end{pmatrix}.$$
For any $x \ge 1$ and $\alpha \in (0, \sqrt{\frac{19}{20}(1 - \frac{1}{20x})})$, both $Q_a \succ 0$ and $Q_b \succ 0$, while the predicted priors are $P_a^-, P_b^-$ of `ex:coh-amplification`(i) and the posted filtered posterior headers give $\hat R_a = \hat R_b = \frac{1}{5} + \frac{1}{10} = \frac{3}{10}$. By `lem:coh-rank-one`, the cycle product has spectral radius
$$\rho(A_{\mathfrak c}) = \frac{\alpha^2 x}{(1 + 3/10)^2} = \frac{100\,\alpha^2 x}{169},$$
which equals $\frac{324}{169} \approx 1.917160 > 1$ at $\alpha = 0.9, x = 4$ (where $\det Q_a = \det Q_b = \frac{19}{20}\cdot\frac{79}{20} - 3.24 = 0.5125 > 0$) and grows without bound as $x \to \infty$. $\square$

*Checkpoint 3 (after Theorem 3 and Proposition 2)*:
1. Signs: $\widetilde P_i^+ = P_i - P_i H_{i^-}^\top S_{i,i^-}^{-1} H_{i^-} P_i \preceq P_i$ has a minus sign from precision addition, which cancels against $+H_{i^-}^\top \hat R_{i^-}^{-1} H_{i^-}$ in $\Lambda_i^+$.
2. Factors: Both brackets of $\widehat B_{i,i^-}$ carry exponent $1/2$, matching the exponent $1/2$ in `eq:coh-edge-ratio` of `thm:coh-amplification`(a).
3. Conventions: When $\hat R_i = X_{ii} + R_{c,i} \succeq X_{ii} \succeq \widetilde X_{ii}^+$, $\mathfrak r_e^+ \le 1$ recovers `prop:coh-no-amplification`(c).
4. Type: $\widetilde P_i^+ \in \mathbb S_{++}^K$ is a state-space covariance; $\widehat B_{i,i^-} \in \mathbb R^{r_i \times r_{i^-}}$ is a dimensionless coded transfer operator.

---

### Part (c): Common Code of Rank $\ge 2$ with Sender-Specific Noise Covariances (Claims C6 and C7)

#### Lemma 1 (Self-contained Kantorovich dilation bound for $0 \preceq E \preceq s I_{r_c}$)

For every symmetric positive-definite matrix $M \in \mathbb S_{++}^{r_c}$ with condition number $\kappa(M) = \lambda_{\max}(M)/\lambda_{\min}(M) \ge 1$ and every symmetric matrix $E \in \mathbb S^{r_c}$ satisfying $0 \preceq E \preceq s I_{r_c}$ ($s > 0$),
$$\|M^{-1} E M\|_2 \le s\,\frac{\kappa(M)^2 + 1}{2\kappa(M)},$$
with equality attained when $E = s\,u u^\top$ for $u = \frac{1}{\sqrt{2}}(e_{\max} + e_{\min})$, where $e_{\max}, e_{\min}$ are orthonormal eigenvectors of $M$ corresponding to $\lambda_{\max}(M)$ and $\lambda_{\min}(M)$.

*Proof*:
1. (**Reduction from $0 \preceq E \preceq s I_{r_c}$ to orthogonal projections via Abel summation** — Identity): Let $E = \sum_{k=1}^{r_c} \lambda_k u_k u_k^\top$ be an eigendecomposition of $E$ with $0 =: \lambda_0 \le \lambda_1 \le \dots \le \lambda_{r_c} \le s$ and orthonormal eigenvectors $u_1,\dots,u_{r_c}$. For each $m \in \{1,\dots,r_c\}$, define the orthogonal projection $\Pi_m := \sum_{k=m}^{r_c} u_k u_k^\top$ ($\Pi_m^2 = \Pi_m = \Pi_m^\top$). Summation by parts gives
   $$E = \sum_{m=1}^{r_c} (\lambda_m - \lambda_{m-1}) \Pi_m, \qquad \lambda_m - \lambda_{m-1} \ge 0, \qquad \sum_{m=1}^{r_c} (\lambda_m - \lambda_{m-1}) = \lambda_{r_c} \le s.$$
   By the triangle inequality for $\|\cdot\|_2$,
   $$\|M^{-1} E M\|_2 \le \sum_{m=1}^{r_c} (\lambda_m - \lambda_{m-1}) \|M^{-1} \Pi_m M\|_2 \le s \max_{\Pi^2 = \Pi = \Pi^\top} \|M^{-1} \Pi M\|_2.$$

2. (**Reduction from arbitrary-rank orthogonal projections to unit vectors** — Proposition): Let $\Pi \in \mathbb S^{r_c}$ be any orthogonal projection ($\Pi^2 = \Pi = \Pi^\top$) and let $v \in \mathbb R^{r_c}$ with $\|v\|_2 = 1$. If $\Pi M v = 0$, then $\|M^{-1} \Pi M v\|_2 = 0$. Otherwise, define the unit vector $u := \frac{\Pi M v}{\|\Pi M v\|_2} \in \operatorname{ran}(\Pi)$ ($\|u\|_2 = 1$). Since $\Pi u = u$, we have $\|\Pi M v\|_2 = u^\top (\Pi M v) = (\Pi u)^\top M v = u^\top M v \le \|M u\|_2 \|v\|_2 = \|M u\|_2$. Therefore,
   $$\|M^{-1} \Pi M v\|_2 = \bigl\|M^{-1} \bigl(\|\Pi M v\|_2 u\bigr)\bigr\|_2 = \|\Pi M v\|_2 \, \|M^{-1} u\|_2 \le \|M u\|_2 \, \|M^{-1} u\|_2 = \sqrt{(u^\top M^2 u)(u^\top M^{-2} u)}.$$

3. (**Two-line proof of the Kantorovich inequality** — Proposition): Put $A := M^2 \in \mathbb S_{++}^{r_c}$, whose eigenvalues lie in $[a, b]$ with $a = \lambda_{\min}(M)^2 > 0$, $b = \lambda_{\max}(M)^2$, and $b/a = \kappa(M)^2$. Since every eigenvalue $\nu \in [a, b]$ of $A$ satisfies $(b - \nu)(\nu - a) \ge 0$, i.e., $\nu + ab\nu^{-1} \le a + b$, functional calculus on the diagonalized matrix $A$ gives $A + ab A^{-1} \preceq (a + b) I_{r_c}$. For any unit vector $u \in \mathbb R^{r_c}$, taking the quadratic form and applying the arithmetic-geometric mean inequality gives
   $$\sqrt{(u^\top A u)(u^\top A^{-1} u)} = \frac{1}{\sqrt{ab}}\sqrt{(u^\top A u)(ab\,u^\top A^{-1} u)} \le \frac{u^\top A u + ab\,u^\top A^{-1} u}{2\sqrt{ab}} \le \frac{a + b}{2\sqrt{ab}} = \frac{\kappa(M)^2 + 1}{2\kappa(M)}.$$
   At $u = \frac{1}{\sqrt{2}}(e_{\max} + e_{\min})$ and $E = s\,u u^\top$, $u^\top A u = \frac{a+b}{2}$ and $u^\top A^{-1} u = \frac{a^{-1}+b^{-1}}{2} = \frac{a+b}{2ab}$, attaining equality. $\square$

---

#### Theorem 4 (Cyclic noise-spread bound and Kantorovich projective-distance bound — Claim C6)

Let all senders on the cycle $\mathfrak c$ share a common code $H_i = H \in \mathbb R^{r_c \times K}$ of full row rank $r_c \ge 2$, read with sender-specific assigned noise covariances $\hat R_1,\dots,\hat R_N \in \mathbb S_{++}^{r_c}$ (indices modulo $N$, with $\hat R_0 \equiv \hat R_N$). Set $X_j = H P_j H^\top \in \mathbb S_{++}^{r_c}$ and $B_j = X_j(X_j + \hat R_{j-1})^{-1} \in \mathbb R^{r_c \times r_c}$. As in the proof of `prop:coh-no-amplification`(d), $H A_{j,j-1} = B_j H$, so $\operatorname{spec}(A_{\mathfrak c})\setminus\{0\} = \operatorname{spec}(B_{\mathfrak c})\setminus\{0\}$ where $B_{\mathfrak c} = B_N B_{N-1} \cdots B_1$. Moreover,
$$B_j = \hat R_{j-1}^{1/2} E_j \hat R_{j-1}^{-1/2}, \qquad E_j := Y_j(I_{r_c} + Y_j)^{-1}, \qquad Y_j := \hat R_{j-1}^{-1/2} X_j \hat R_{j-1}^{-1/2} \in \mathbb S_{++}^{r_c},$$
so $E_j \in \mathbb S_{++}^{r_c}$ satisfies $0 \prec E_j \preceq s_j I_{r_c}$ with $s_j := \|E_j\|_2 = \frac{\mathrm{snr}_{j-1\to j}}{1 + \mathrm{snr}_{j-1\to j}} < 1$.

1. (**Cyclic noise-spread bound** — Proposition): Write $\hat R_N^{-1/2} B_{\mathfrak c} \hat R_N^{1/2}$ by inserting $\hat R_{j-1}^{-1/2} \hat R_{j-1}^{1/2} = I_{r_c}$:
   $$\hat R_N^{-1/2} B_{\mathfrak c} \hat R_N^{1/2} = \bigl(\hat R_N^{-1/2} \hat R_{N-1}^{1/2}\bigr) E_N \bigl(\hat R_{N-1}^{-1/2} \hat R_{N-2}^{1/2}\bigr) E_{N-1} \cdots \bigl(\hat R_1^{-1/2} \hat R_N^{1/2}\bigr) E_1.$$
   Since $\|\hat R_j^{-1/2} \hat R_{j-1}^{1/2}\|_2 = \lambda_{\max}(\hat R_j^{-1}\hat R_{j-1})^{1/2} = \exp\bigl(\frac{1}{2}\operatorname{sp}(\hat R_{j-1}\Vert\hat R_j)\bigr)$, submultiplicativity gives
   $$\rho(A_{\mathfrak c}) = \rho(B_{\mathfrak c}) \le \exp\Bigl(\frac{1}{2}\mathcal S_{\mathfrak c}(\hat R)\Bigr) \prod_{e\in\mathfrak c}\frac{\mathrm{snr}_e}{1+\mathrm{snr}_e}, \qquad \mathcal S_{\mathfrak c}(\hat R) := \sum_{j=1}^N \operatorname{sp}(\hat R_{j-1}\Vert\hat R_j).$$
   For each $j$, $\lambda_{\max}(\hat R_j^{-1}\hat R_{j-1}) \ge (\det(\hat R_j^{-1}\hat R_{j-1}))^{1/r_c}$, with equality if and only if all eigenvalues of $\hat R_j^{-1}\hat R_{j-1}$ are equal ($\hat R_{j-1} = \alpha_{j-1,j}\hat R_j$). Taking the logarithm and summing over $j = 1,\dots,N$ gives $\mathcal S_{\mathfrak c}(\hat R) \ge \frac{1}{r_c}\ln\prod_{j=1}^N \det(\hat R_j^{-1}\hat R_{j-1}) = 0$, with $\mathcal S_{\mathfrak c}(\hat R) = 0$ if and only if $\hat R_i = \alpha_i \hat R_0$ for all $i$.

2. (**Kantorovich projective-distance bound** — Proposition): Fix any reference matrix $\hat R_\ast \in \mathbb S_{++}^{r_c}$ and conjugate $B_{\mathfrak c}$ by $\hat R_\ast^{-1/2}$:
   $$\hat R_\ast^{-1/2} B_{\mathfrak c} \hat R_\ast^{1/2} = \prod_{j=1}^N \bigl(\hat R_\ast^{-1/2} B_j \hat R_\ast^{1/2}\bigr) = \prod_{j=1}^N \bigl(L_{j-1} E_j L_{j-1}^{-1}\bigr), \qquad L_{j-1} := \hat R_\ast^{-1/2} \hat R_{j-1}^{1/2}.$$
   Take the polar decomposition $L_{j-1} = U_{j-1} M_{j-1}^{-1}$, where $U_{j-1} \in \mathrm O(r_c)$ is orthogonal and $M_{j-1} := (L_{j-1}^\top L_{j-1})^{-1/2} = (\hat R_{j-1}^{1/2} \hat R_\ast^{-1} \hat R_{j-1}^{1/2})^{-1/2} \in \mathbb S_{++}^{r_c}$. The eigenvalues of $M_{j-1}^2 = (\hat R_{j-1}^{1/2} \hat R_\ast^{-1} \hat R_{j-1}^{1/2})^{-1}$ are the eigenvalues of $\hat R_\ast \hat R_{j-1}^{-1}$, so $\kappa(M_{j-1})^2 = \kappa(\hat R_\ast^{-1}\hat R_{j-1}) = \exp d_{\mathrm H}(\hat R_{j-1}, \hat R_\ast)$. By orthogonal invariance of $\|\cdot\|_2$ and Lemma 1,
   $$\bigl\|L_{j-1} E_j L_{j-1}^{-1}\bigr\|_2 = \bigl\|U_{j-1} M_{j-1}^{-1} E_j M_{j-1} U_{j-1}^\top\bigr\|_2 = \bigl\|M_{j-1}^{-1} E_j M_{j-1}\bigr\|_2 \le s_j\,\frac{\kappa(\hat R_\ast^{-1}\hat R_{j-1}) + 1}{2\sqrt{\kappa(\hat R_\ast^{-1}\hat R_{j-1})}} = s_j \cosh\Bigl(\frac{1}{2} d_{\mathrm H}(\hat R_{j-1}, \hat R_\ast)\Bigr).$$
   Multiplying over $j = 1,\dots,N$ yields C6(2). $\square$

---

#### Theorem 5 (Proportional-noise characterization and exact worst-case spectral radius — Claim C7)

Under the hypotheses of Theorem 4:

1. (**Sufficiency of proportional noises for $A_{\mathfrak c}$ and $\bar A_{\mathfrak c}$** — Proposition): If $\hat R_i = \alpha_i \hat R_0$ ($\alpha_i > 0, \hat R_0 \in \mathbb S_{++}^{r_c}$), then choosing $\hat R_\ast = \hat R_0$ gives $d_{\mathrm H}(\hat R_{j-1}, \hat R_0) = 0$ for every $j$, so Theorem 4(2) gives $\rho(A_{\mathfrak c}) \le \prod_{e\in\mathfrak c}\frac{\mathrm{snr}_e}{1+\mathrm{snr}_e} < 1$ for all priors $P_1,\dots,P_N \succ 0$. Moreover, for the noisy round-trip map $\bar A_{\mathfrak c} = (I_K - A_{1N}) + A_{\mathfrak c}$, on $V_1 = \operatorname{col}(P_1 H^\top)$ the map $\hat R_0^{-1/2} H \bar A_{\mathfrak c}\big|_{V_1} P_1 H^\top X_1^{-1} \hat R_0^{1/2}$ equals $(I_{r_c} - E_1) + E_1 E_N E_{N-1}\cdots E_2$ where $E_j = \hat R_0^{-1/2} B_j \hat R_0^{1/2} \in \mathbb S_{++}^{r_c}$ satisfies $0 \prec E_j \preceq s_j I_{r_c} \prec I_{r_c}$. Conjugating by $E_1^{-1/2}$ gives $(I_{r_c} - E_1) + E_1^{1/2}(E_N\cdots E_2)E_1^{1/2}$, whose spectral norm is at most $\max\{1, \prod_{j=2}^N s_j\} = 1$ by the Cauchy--Schwarz bound of Theorem 1(2), so $\rho(\bar A_{\mathfrak c}) = 1$.

2. (**Necessity of proportional noises and explicit amplifying family when proportionality fails** — Proposition): Suppose $(\hat R_1,\dots,\hat R_N)$ are not all proportional to a single matrix. Fix any pair of distinct senders $a, b \in \{1,\dots,N\}$ with $\kappa_{ab} := \kappa(\hat R_a^{-1}\hat R_b) > 1$. Because $H$ has full row rank $r_c$, it has a right inverse $H^+ = H^\top(H H^\top)^{-1}$, and for any $X_j \in \mathbb S_{++}^{r_c}$ the prior $P_j := H^+ X_j (H^+)^\top + (I_K - H^+ H) \in \mathbb S_{++}^K$ satisfies $H P_j H^\top = X_j$.
   For any vectors $u_1,\dots,u_N \in \mathbb R^{r_c}\setminus\{0\}$ and parameters $s > 0, \varepsilon > 0$, choose $X_j(s,\varepsilon) := s\,u_j u_j^\top + \varepsilon I_{r_c} \in \mathbb S_{++}^{r_c}$. As $\varepsilon \to 0^+$, by the Sherman--Morrison formula,
   $$\lim_{\varepsilon\to 0^+} B_j(s,\varepsilon) = s\,u_j u_j^\top \bigl(s\,u_j u_j^\top + \hat R_{j-1}\bigr)^{-1} = \frac{s\,u_j u_j^\top \hat R_{j-1}^{-1}}{1 + s\,u_j^\top \hat R_{j-1}^{-1} u_j},$$
   and then taking $s \to \infty$ gives the rank-1 operator $B_j^\infty := \lim_{s\to\infty}\lim_{\varepsilon\to 0^+} B_j(s,\varepsilon) = \frac{u_j u_j^\top \hat R_{j-1}^{-1}}{u_j^\top \hat R_{j-1}^{-1} u_j}$. The product $B_{\mathfrak c}^\infty = B_N^\infty \cdots B_1^\infty$ has rank at most $1$, and its trace is
   $$\operatorname{tr}(B_{\mathfrak c}^\infty) = \prod_{j=1}^N \frac{u_{j+1}^\top \hat R_{j-1}^{-1} u_j}{u_j^\top \hat R_{j-1}^{-1} u_j} = \prod_{i=1}^N \frac{u_{i+2}^\top \hat R_i^{-1} u_{i+1}}{u_{i+1}^\top \hat R_i^{-1} u_{i+1}} \qquad (\text{setting } i = j-1 \bmod N).$$
   Set $u_{i+1} := v_1$ for all $i$ on the directed cycle arc from $a$ to $b-1$ (so $u_{a+1} = \dots = u_b = v_1$) and $u_{i+1} := v_2$ for all $i$ on the return arc from $b$ to $a-1$ (so $u_{b+1} = \dots = u_a = v_2$). Then at every sender $i \notin \{a, b\}$, $u_{i+2} = u_{i+1}$, so the factor $\frac{u_{i+2}^\top \hat R_i^{-1} u_{i+1}}{u_{i+1}^\top \hat R_i^{-1} u_{i+1}} = 1$. Only the two boundary senders $i = a$ (where $u_{a+1} = v_1, u_{a+2} = v_2$ if $b = a+1$, or at the two arc endpoints $i = b-1$ and $i = a-1$, which we label $a$ and $b$) survive:
   $$\operatorname{tr}(B_{\mathfrak c}^\infty) = \frac{(v_2^\top \hat R_b^{-1} v_1)(v_1^\top \hat R_a^{-1} v_2)}{(v_1^\top \hat R_b^{-1} v_1)(v_2^\top \hat R_a^{-1} v_2)}.$$
   Let $w_1, w_2 \in \mathbb R^{r_c}$ be generalized eigenvectors of $(\hat R_a, \hat R_b)$ corresponding to $\mu_{\max} = \lambda_{\max}(\hat R_b^{-1}\hat R_a)$ and $\mu_{\min} = \lambda_{\min}(\hat R_b^{-1}\hat R_a)$, normalized so that $w_p^\top \hat R_b^{-1} w_q = \delta_{pq}$; then $w_1^\top \hat R_a^{-1} w_1 = \mu_{\max}^{-1}$, $w_2^\top \hat R_a^{-1} w_2 = \mu_{\min}^{-1}$, $w_1^\top \hat R_a^{-1} w_2 = 0$, and $\mu_{\max}/\mu_{\min} = \kappa_{ab}$. Setting $m := \sqrt{\kappa_{ab}} > 1$ (so $\mu_{\min}^{-1} = \kappa_{ab}\mu_{\max}^{-1} = m^2\mu_{\max}^{-1}$), choose
   $$v_1 := w_1 + w_2, \qquad v_2 := m\,w_1 + w_2.$$
   Then:
   - $v_1^\top \hat R_b^{-1} v_1 = 1 + 1 = 2$,
   - $v_2^\top \hat R_b^{-1} v_1 = m + 1$,
   - $v_2^\top \hat R_a^{-1} v_2 = m^2\mu_{\max}^{-1} + \mu_{\min}^{-1} = m^2\mu_{\max}^{-1} + m^2\mu_{\max}^{-1} = 2 m^2\mu_{\max}^{-1}$,
   - $v_1^\top \hat R_a^{-1} v_2 = m\mu_{\max}^{-1} + \mu_{\min}^{-1} = m\mu_{\max}^{-1} + m^2\mu_{\max}^{-1} = m(m + 1)\mu_{\max}^{-1}$.
   Substituting these four exact values into $\operatorname{tr}(B_{\mathfrak c}^\infty)$ gives
   $$\operatorname{tr}(B_{\mathfrak c}^\infty) = \frac{(m + 1) \cdot m(m + 1)\mu_{\max}^{-1}}{2 \cdot 2 m^2\mu_{\max}^{-1}} = \frac{(m + 1)^2}{4m} = \frac{(\sqrt{\kappa_{ab}} + 1)^2}{4\sqrt{\kappa_{ab}}} = \cosh^2\Bigl(\frac{1}{4} d_{\mathrm H}(\hat R_a, \hat R_b)\Bigr) > 1.$$
   By continuity of eigenvalues, for sufficiently small $\varepsilon > 0$ and sufficiently large $s > 0$, $\rho(A_{\mathfrak c}) > 1$.

3. (**Exact closed-form supremum for $N = 2$** — Corollary): When $N = 2$, let $\hat R_\ast = \hat R_1 \# \hat R_2 := \hat R_1^{1/2}(\hat R_1^{-1/2}\hat R_2\hat R_1^{-1/2})^{1/2}\hat R_1^{1/2}$ be the metric geometric mean of $\hat R_1$ and $\hat R_2$. Then $\hat R_\ast^{-1}\hat R_2 = \hat R_1^{-1/2}(\hat R_1^{-1/2}\hat R_2\hat R_1^{-1/2})^{1/2}\hat R_1^{1/2}$ and $\hat R_\ast^{-1}\hat R_1 = \hat R_1^{-1/2}(\hat R_1^{-1/2}\hat R_2\hat R_1^{-1/2})^{-1/2}\hat R_1^{1/2}$ both have condition number $\sqrt{\kappa(\hat R_1^{-1}\hat R_2)}$. Substituting $\hat R_\ast$ into Theorem 4(2) gives $\rho(A_{\mathfrak c}) \le s_1 s_2 \frac{(\sqrt{\kappa(\hat R_1^{-1}\hat R_2)} + 1)^2}{4\sqrt{\kappa(\hat R_1^{-1}\hat R_2)}} < \frac{(\sqrt{\kappa(\hat R_1^{-1}\hat R_2)} + 1)^2}{4\sqrt{\kappa(\hat R_1^{-1}\hat R_2)}}$, and Part 2 attains this upper bound in the limit $\varepsilon \to 0^+, s \to \infty$. $\square$

*Checkpoint 4 (after Lemma 1 and Theorems 4 and 5)*:
1. Signs: $d_{\mathrm H}(\hat R_a, \hat R_b) = \operatorname{sp}(\hat R_a\Vert\hat R_b) + \operatorname{sp}(\hat R_b\Vert\hat R_a) \ge 0$ is symmetric and vanishes iff $\hat R_a = \alpha \hat R_b$.
2. Factors: The factor $1/4$ in $\cosh^2(\frac{1}{4}d_{\mathrm H}(\hat R_1,\hat R_2))$ arises because the geometric mean $\hat R_1\#\hat R_2$ splits $d_{\mathrm H}(\hat R_1,\hat R_2)$ in half ($1/2$) and Lemma 1 takes $\cosh(\frac{1}{2} d_{\mathrm H}(\hat R_i, \hat R_\ast))$.
3. Conventions: At $\sqrt{\kappa} = 3$ ($\kappa = 9$), $\frac{(\sqrt{\kappa}+1)^2}{4\sqrt{\kappa}} = \frac{16}{12} = \frac{4}{3} = 1.33333333$, matching `verify_coh_amplification_noisy_output.txt`.
4. Type: $\mathcal S_{\mathfrak c}(\hat R)$ and $d_{\mathrm H}(\hat R_a, \hat R_b)$ are dimensionless projective invariants on the cone $\mathbb S_{++}^{r_c}$.
