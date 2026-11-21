# Problem 8 (`open:nrg-rate`): Coarse Dissipation Rate, Second-Order Constant, and Optimal Descriptions

- Status: active
- Opened: 2026-11-21
- Updated: 2026-11-21
- Sessions: 1

**Manuscript anchors:** `Collective_Agents/sections/10e_open_problems.tex` (§10e.8, Energetic viability), `Collective_Agents/sections/ext6_nrg.tex` (`ass:nrg-setting`, `def:nrg-ep`, `thm:nrg-ep`, `thm:nrg-coarse`, `obs:nrg-spectral`, `open:nrg-rate`), `Collective_Agents/sections/appext6_nrg.tex`, `Collective_Agents/sections/chkext6_nrg.tex` (`chk:nrg-coarse`, `chk:nrg-indep`).

## Target

- Locked statement: Under Assumption `ass:nrg-setting` ($X_{t+1} = A X_t + \Xi_t$ on $\mathbb{R}^d$ with $\rho(A) < 1$, $Q^\Xi \succ 0$, stationary centered law $\mathcal{N}(0, \Sigma)$ where $\Sigma = A\Sigma A^\top + Q^\Xi$, all coordinates even under time reversal) and any real matrix $C \in \mathbb{R}^{m \times d}$ of full row rank $m$ ($1 \le m \le d$), with $Y_t = C X_t$ and $\mathsf{D}_n(C) = \mathrm{KL}(\mathrm{law}(Y_0,\dots,Y_n) \Vert \mathrm{law}(Y_n,\dots,Y_0))$: (1) prove that $\lim_{n\to\infty} \mathsf{D}_n(C)/n$ exists and equals $\bar{\mathsf{e}}(C) = \frac{1}{4\pi}\int_{-\pi}^{\pi}[\operatorname{tr}(\overline{S(\vartheta)}^{-1}S(\vartheta)) - m]\,d\vartheta$ where $S(\vartheta) = C(e^{i\vartheta}I - A)^{-1}Q^\Xi(e^{-i\vartheta}I - A^\top)^{-1}C^\top$; (1b) establish the second-order expansion $\mathsf{D}_n(C) = n\bar{\mathsf{e}}(C) - \mathsf{e}_0(C) + o(1)$ observed in `obs:nrg-spectral`; and (2) determine, for given $m$, the full-row-rank descriptions $C$ that retain the largest fraction $\bar{\mathsf{e}}(C)/\mathsf{ep}$ of the full entropy production $\mathsf{ep}$.
- Falsifier: Any admissible tuple $(A, Q^\Xi, C)$ satisfying $\rho(A) < 1$, $Q^\Xi \succ 0$, $\operatorname{rank}(C) = m$ for which $\mathsf{D}_n(C)/n$ fails to converge to $\bar{\mathsf{e}}(C)$, or $n\bar{\mathsf{e}}(C) - \mathsf{D}_n(C)$ fails to converge to the derived constant $\mathsf{e}_0(C)$; or any admissible $(A, Q^\Xi, C)$ violating $\bar{\mathsf{e}}(C) = \mathsf{ep} \iff \operatorname{row}(C) \supseteq \operatorname{range}((Q^\Xi)^{-1}A - A^\top(Q^\Xi)^{-1})$.
- May assume: Assumption `ass:nrg-setting`, Definition `def:nrg-ep`, Theorem `thm:nrg-ep`, Theorem `thm:nrg-coarse` (in particular $\mathsf{D}_n(C) = \tfrac{1}{2}[\operatorname{tr}(\widetilde{\mathsf{T}}_n^{-1}\mathsf{T}_n) - (n+1)m]$), and standard finite-dimensional matrix algebra and single-variable complex analysis (Cauchy integral estimates on an annulus).
- Must not assume: Unchecked external block-Toeplitz Szegő/Widom limit theorems (the open problem explicitly notes none was checked against a primary source); invertibility of $A$; normality or diagonalizability of $A$; observability of $(A, C)$; Markovianity of $Y_t = C X_t$.
- Alternative forms: For Part (2), an exact characterization on the full lossless regime $m \ge r_\Omega := \operatorname{rank}(A Q^\Xi - Q^\Xi A^\top)$ together with structural Grassmannian characterization and counterexamples to naive modal rules for $2 \le m < r_\Omega$ is accepted as partial progress, with closed-form global maximizers for $2 \le m < r_\Omega$ recorded as an open obligation.
- Test instance: Directed 3-ring (`ex:nrg-ring`, `chk:nrg-coarse`): $A = 0.3 I + 0.5 P$, $Q^\Xi = I$, $\mathsf{ep} = 25/27 \approx 0.92592593$; for $C = \begin{pmatrix}1 & 0 & 0\\ 0 & 1 & 0\end{pmatrix}$, manuscript records $\bar{\mathsf{e}} \approx 0.346653$ and $n\bar{\mathsf{e}} - \mathsf{D}_n(C) \approx 0.088436$ at $n = 16, 32, 64, 128$. Plus exact nilpotent $d=2, m=2$ check: $A = \begin{pmatrix}0 & a\\ 0 & 0\end{pmatrix}$, $Q^\Xi = I$, $C = I$ gives $\bar{\mathsf{e}} = a^2 = \mathsf{ep}$.
- Out of scope: Physical bridge premises (`open:nrg-tight`), agents with memory (`open:nrg-dynamic`), odd-parity coordinates and nonlinear chains (`open:nrg-parity`).
- Reading chosen: Full generality of `ass:nrg-setting` (allowing singular $A$, defective Jordan blocks, non-normal $A$, unobservable $(A,C)$, and arbitrary full-row-rank $C$), proving both the first-order limit and the second-order constant $\mathsf{e}_0(C)$ from scratch without black-box block-Toeplitz citations.

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| KL direction | $\mathrm{KL}(P \Vert Q) = \mathbb{E}_P[\ln(dP/dQ)]$ in nats | $\mathrm{KL}(\mathcal{N}(0,1)\Vert\mathcal{N}(0,4)) = \ln 2 - \tfrac{3}{8} \approx 0.318147$ |
| Window indexing | $Y_{0:n} = (Y_0,\dots,Y_n)$ has $N = n+1$ blocks of size $m$; $\mathsf{D}_n(C) = \tfrac{1}{2}[\operatorname{tr}(\widetilde{\mathsf{T}}_n^{-1}\mathsf{T}_n) - Nm]$ | For $C = I$, $\mathsf{D}_n(I) = n\,\mathsf{ep}$ (not $(n+1)\mathsf{ep}$), so $\mathsf{e}_0(I) = 0$ |
| Lag covariance | $\Gamma_k = \operatorname{Cov}(Y_{t+k}, Y_t) = C A^k \Sigma C^\top$ ($k \ge 0$), $\Gamma_{-k} = \Gamma_k^\top$; $(\mathsf{T}_n)_{s,t} = \Gamma_{s-t}$ | For $A = \begin{pmatrix}0 & 0.5\\ 0 & 0\end{pmatrix}$, $Q^\Xi = I$, $C = I$: $\Gamma_1 = \begin{pmatrix}0 & 0.5\\ 0 & 0\end{pmatrix} \ne \Gamma_{-1}$ |
| Spectral density & Fourier sign | $S(\vartheta) = C(e^{i\vartheta}I - A)^{-1}Q^\Xi(e^{-i\vartheta}I - A^\top)^{-1}C^\top = \sum_{k\in\mathbb{Z}}\Gamma_k e^{-ik\vartheta}$, $\Gamma_k = \frac{1}{2\pi}\int_{-\pi}^{\pi} S(\vartheta) e^{ik\vartheta}\,d\vartheta$ | For $A = \begin{pmatrix}0 & 0.5\\ 0 & 0\end{pmatrix}$, $Q^\Xi = I$, $C = I$: $S(\vartheta) = \begin{pmatrix}1.25 & 0.5 e^{-i\vartheta}\\ 0.5 e^{i\vartheta} & 1\end{pmatrix} = \Gamma_0 + \Gamma_1 e^{-i\vartheta} + \Gamma_{-1} e^{i\vartheta}$ |
| Reversed spectral density | $\overline{S(\vartheta)} = S(\vartheta)^\top = S(-\vartheta)$ (since $A, Q^\Xi, C$ are real and $S(\vartheta)^* = S(\vartheta)$) | For $m=1$, $\overline{S(\vartheta)} = S(\vartheta) > 0$, so $\bar{\mathsf{e}}(C) = 0$ |
| Second-order constant sign | $\mathsf{e}_0(C) := \lim_{n\to\infty}(n\bar{\mathsf{e}}(C) - \mathsf{D}_n(C))$ (matches `obs:nrg-spectral`: $\mathsf{D}_n(C) = n\bar{\mathsf{e}}(C) - \mathsf{e}_0(C) + o(1)$) | Directed 3-ring agents $(1,2)$: $\mathsf{e}_0 = +0.0884361144 > 0$ |
| Irreversibility operator | $\Omega := (Q^\Xi)^{-1}A - A^\top(Q^\Xi)^{-1} = (Q^\Xi)^{-1}(AQ^\Xi - Q^\Xi A^\top)(Q^\Xi)^{-1}$ (real skew-symmetric, even rank $r_\Omega$) | $S_{\mathrm{full}}(\vartheta)^{-1} - \overline{S_{\mathrm{full}}(\vartheta)}^{-1} = 2i\sin(\vartheta)\,\Omega$ |

## Claims

### C1: Coarse dissipation rate and exponential second-order expansion (Theorem 1)

- Statement: Under Assumption `ass:nrg-setting` and for every full-row-rank $C \in \mathbb{R}^{m \times d}$, $S(\vartheta) \succ 0$ uniformly on $[-\pi,\pi]$ with $0 < c_{\min} \le \lambda_{\min}(S(\vartheta)) \le \lambda_{\max}(S(\vartheta)) \le c_{\max} < \infty$; with $r_1 := \max(\{\rho(A)\} \cup \{|z| < 1 : \det S(z) = 0\}) < 1$, for every $\tau \in (r_1, 1)$ one has $\mathsf{D}_n(C) = n\bar{\mathsf{e}}(C) - \mathsf{e}_0(C) + O(\tau^n)$ as $n \to \infty$, where $\mathsf{e}_0(C) = -\bar{\mathsf{e}}(C) - \tfrac{1}{2}[-\operatorname{tr}(H G_2) + \operatorname{tr}(K^{-1} H G_3) - \operatorname{tr}(K^{-1} H G_4 H G_4^\top)]$ is given in terms of the $2d \times 2d$ boundary integrals $G_1,\dots,G_4$ and invertible $K = I_{2d} - H G_1$ ($\det K \ge (c_{\min}/c_{\max})^{2d} > 0$). In particular, $\lim_{n\to\infty} \mathsf{D}_n(C)/n = \bar{\mathsf{e}}(C)$ with $O(1/n)$ convergence rate.
- Status: proved
- Review: self
- Evidence: Complete self-contained proof in Section `Derivations` (Theorem 1) of this record; two-channel numerical verification (exact $2d \times 2d$ formula vs. brute-force $\mathsf{D}_{96}(C)$ across 6 cases including singular $A$, defective Jordan $3\times 3$, positive and negative $\mathsf{e}_0$, and $d=6, m=3$, max error $2.26 \times 10^{-11}$, plus 3 planted-error negative controls) in `problem_8-checks/verify_nrg_rate_theorems.py` and `problem_8-checks/verify_nrg_rate_theorems_output.txt`.
- Depends on: none

### C2: Exact characterization of lossless dissipation retention (Theorem 2)

- Statement: Under Assumption `ass:nrg-setting`, put $\Omega := (Q^\Xi)^{-1}A - A^\top(Q^\Xi)^{-1}$ and $r_\Omega := \operatorname{rank}(\Omega) = \operatorname{rank}(AQ^\Xi - Q^\Xi A^\top) \in \{0, 2, \dots, 2\lfloor d/2 \rfloor\}$. For every full-row-rank $C \in \mathbb{R}^{m \times d}$, $\bar{\mathsf{e}}(C) \le \bar{\mathsf{e}}(I) = \mathsf{ep}$, with equality if and only if $\ker(C) \subseteq \ker(\Omega)$, equivalently $\operatorname{row}(C) \supseteq \operatorname{range}(\Omega)$. Consequently, $100\%$ retention ($\bar{\mathsf{e}}(C) = \mathsf{ep}$) is attainable at dimension $m$ if and only if $m \ge r_\Omega$, with unique minimal-dimension lossless row space $\operatorname{row}(C) = \operatorname{range}(\Omega)$; in particular, every odd-dimensional system ($d = 3, 5, \dots$) admits a $(d-1)$-dimensional lossless linear description.
- Status: proved
- Review: self
- Evidence: Complete proof in Section `Derivations` (Theorem 2) of this record via the frequency-independent identity $S_{\mathrm{full}}(\vartheta)^{-1} - \overline{S_{\mathrm{full}}(\vartheta)}^{-1} = 2i\sin(\vartheta)\,\Omega$ and an exact pointwise Hermitian Schur-complement identity; verified numerically to $\le 1.60 \times 10^{-14}$ on a coupled $d=12$ network with $r_\Omega = 2$ (retaining $100\%$ with $m=2$ and $\mathsf{e}_0 = +3.792603 > 0$, dropping to $97.9\%$ under a $0.2\text{ rad}$ tilt) and generic odd $d \in \{3, 5\}$ in `problem_8-checks/verify_nrg_rate_theorems.py` and `problem_8-checks/verify_nrg_rate_theorems_output.txt`.
- Depends on: C1

### C3: Grassmannian descent and gradient for $2 \le m < r_\Omega$ (Proposition 3a)

- Statement: Under Assumption `ass:nrg-setting`, $\bar{\mathsf{e}}(MC) = \bar{\mathsf{e}}(C)$ for every $M \in \mathrm{GL}(m, \mathbb{R})$, so $\bar{\mathsf{e}}$ descends to a smooth functional on the compact Grassmannian $\mathrm{Gr}(m, d)$ and always attains its global maximum $R_m(A, Q^\Xi)\,\mathsf{ep}$, with Euclidean gradient $\nabla_C \bar{\mathsf{e}}(C) = \frac{1}{2\pi}\int_{-\pi}^{\pi} \operatorname{Re}[\overline{S(\vartheta)}^{-1} C S_{\mathrm{full}}(\vartheta) - \overline{S(\vartheta)}^{-1} S(\vartheta) \overline{S(\vartheta)}^{-1} C \overline{S_{\mathrm{full}}(\vartheta)}]\,d\vartheta$ satisfying $(\nabla_C \bar{\mathsf{e}}(C))C^\top = 0$.
- Status: proved
- Review: self
- Evidence: Derivation in Section `Derivations` (Proposition 3) of this record; central finite-difference check matches analytic gradient to $9.48 \times 10^{-9}$ and verifies $(\nabla_C \bar{\mathsf{e}})C^\top = 0$ to $1.64 \times 10^{-14}$ in `problem_8-checks/verify_nrg_rate_theorems.py` and `problem_8-checks/verify_nrg_rate_theorems_output.txt`.
- Depends on: C1

### C4: Invariant-subspace optimality and uniform sub-unity cap for $2 \le m < r_\Omega$

- Statement: For normal drift $A$ and isotropic noise $Q^\Xi = qI$ with $2 \le m < r_\Omega$, the global maximum of $\bar{\mathsf{e}}(C)$ over $\mathrm{Gr}(m, d)$ is attained by an $A$-invariant subspace (the top $\lfloor m/2 \rfloor$ circulation planes), and $R_m(A, Q^\Xi)$ is bounded away from $1$ uniformly over systems with $r_\Omega > m$.
- Status: refuted
- Review: self
- Evidence: Analytic counterexample in Section `Derivations` (Proposition 3(2)): for $d = 4$, $Q^\Xi = I_4$, $A = \operatorname{diag}(r R(\varepsilon), r R(\pi - \varepsilon))$ with $r \in (0, 1)$, $\varepsilon \in (0, \pi/2)$, one has $r_\Omega = 4$ and every $A$-invariant $2$-plane retains exactly $\frac{1}{2}\mathsf{ep}$, whereas the non-invariant tilted subspace $C_{\mathrm{mux}} = \frac{1}{\sqrt{2}}[I_2, I_2]$ satisfies $\lim_{r\to 1^-} \bar{\mathsf{e}}(C_{\mathrm{mux}})/\mathsf{ep} = (1 + \sin^2\varepsilon)^{-1} \to 1$ as $\varepsilon \to 0$. Checked numerically at $(\varepsilon, r) = (\pi/3, 0.99), (0.5, 0.995), (0.2, 0.998), (0.1, 0.999)$ giving retained fractions $0.570743, 0.811153, 0.960691, 0.989403$ against $(1+\sin^2\varepsilon)^{-1} = 0.571429, 0.813108, 0.962029, 0.990132$ in `problem_8-checks/verify_nrg_rate_theorems.py` and `problem_8-checks/verify_nrg_rate_theorems_output.txt`.
- Depends on: C1

### C5: Closed-form global maximizers on $\mathrm{Gr}(m, d)$ for general $2 \le m < r_\Omega$

- Statement: For general $(A, Q^\Xi)$ under `ass:nrg-setting` and $2 \le m < r_\Omega$, characterize the global maximizers $C^\star \in \mathrm{Gr}(m, d)$ of $\bar{\mathsf{e}}(C)$ in closed form (or give sharp computable upper bounds strictly below $\mathsf{ep}$ as a function of spectral separation).
- Status: open
- Review: none
- Evidence: Open after C2, C3, C4; frequency-multiplexing interference shows the optimization couples all frequencies nonlinearly through $\overline{S(\vartheta)}^{-1}S(\vartheta)$.
- Depends on: C2, C3, C4

## Failed routes

### R1: Modal / invariant-subspace optimality for normal $(A, qI)$

- Tried: Hypothesized that for normal $A$ and $Q^\Xi = qI$, selecting the $\lfloor m/2 \rfloor$ real invariant circulation planes with largest $\mathsf{ep}_j = 4(\operatorname{Im}\lambda_j)^2/(1 - |\lambda_j|^2)$ maximizes $\bar{\mathsf{e}}(C)$ over $\mathrm{Gr}(m, d)$.
- Failed because: Falsification sweep on $d = 4$ with equal-radius oscillators at distinct frequencies $(\pi/3, 2\pi/3)$ showed a tilted $m=2$ subspace mixing both planes achieves $3.150186 > 2.882353$ (both at $r=0.7$ and approaching $4/7 > 1/2$ as $r \to 1^-$), and $m=3$ achieves $3.356297 > 2.882353$.
- Reopen if: Restricted to the special case where all circulation planes share the same frequency $\phi$ (so $S_j(\vartheta)$ peaks overlap completely and frequency multiplexing yields no gain).

### R2: Arbitrary-frequency multiplexing achieving $R_2 \to 1$ for $p \ge 3$ oscillators

- Tried: Hypothesized that taking $p = 3$ decoupled $2\text{D}$ oscillators at arbitrary distinct frequencies $(\pi/5, 2\pi/5, 3\pi/5)$ with $C_{\mathrm{mux}} = \frac{1}{\sqrt 3}[I_2, I_2, I_2]$ would yield $\bar{\mathsf{e}}(C_{\mathrm{mux}})/\mathsf{ep} \to 1$ as $r \to 1^-$.
- Failed because: At each peak $\vartheta \approx +\phi_k$, the reversed spectral density $\overline{S(\phi_k)} = \frac{1}{p}\sum_j \overline{S_j(\phi_k)}$ receives $O(1)$ cross-interference $\frac{1}{4\sin^2((\phi_k+\phi_j)/2)}$ from every other oscillator $j \ne k$, which competes with oscillator $k$'s own $\frac{1}{4\sin^2\phi_k}$ denominator and caps the $p=3$ $(\pi/5, 2\pi/5, 3\pi/5)$ ratio near $0.35$. Achieving $\to 1$ requires $\sin^2\phi_k \ll \sin^2((\phi_k+\phi_j)/2)$ (e.g., $\phi_1 = \varepsilon, \phi_2 = \pi - \varepsilon$ with $\varepsilon \to 0$).
- Reopen if: Multi-oscillator families with separated small angles and matched/weighted couplings are constructed to test whether $p \ge 3$ equal-rank modes can also approach $1$ with $m=2$.

## Open obligations

- [ ] O1 (sessions: 1): Run a fresh-context proof reconstruction (`research-proof-checker`) and blind recomputation (`research-symbolic-numerics`) on C1–C4 to upgrade review state from `self` to `fresh-context` before patching `ext6_nrg.tex` and `appext6_nrg.tex`.
- [ ] O2 (sessions: 1): Run a literature search (block-Toeplitz Szegő/Widom trace asymptotics for state-space spectral densities, time-reversal KL rate of hidden linear-Gaussian / VARMA processes, and coarse-grained linear-Gaussian entropy production) before claiming novelty for Theorem 1 or Theorem 2.
- [ ] O3 (sessions: 1): Resolve C5 (either characterize the global maximizers / tight upper bounds for $2 \le m < r_\Omega$ in terms of spectral separation, or establish a clean structural negative result on non-convexity / multi-modality).

## Literature

| Claim | Source | Locator | Read depth | Date read | Verdict |
| --- | --- | --- | --- | --- | --- |
| Background setting | `Collective_Agents/sections/ext6_nrg.tex` | `ass:nrg-setting`, `thm:nrg-ep`, `thm:nrg-coarse`, `obs:nrg-spectral`, `open:nrg-rate` | full section | 2026-11-21 | exact conventions and open problem statements matched |
| Existing proofs | `Collective_Agents/sections/appext6_nrg.tex` | `lem:nrg-gauss`, `lem:nrg-facts`, `thm:nrg-ep`, `thm:nrg-coarse` | full section | 2026-11-21 | verified all dependencies used in C1–C3 |
| Existing numerical checks | `Collective_Agents/sections/chkext6_nrg.tex` | `chk:nrg-coarse`, `chk:nrg-indep` | full section | 2026-11-21 | reproduced directed ring $\bar{\mathsf{e}} = 0.346653$, $\mathsf{e}_0 = +0.088436$ |

## Searches

| Query | Tool | Date | Not searched |
| --- | --- | --- | --- |
| none yet | — | 2026-11-21 | External literature for novelty (block-Toeplitz trace asymptotics, hidden-Markov Gaussian entropy production rate, lossless coarse-graining criterion) |

## Log

- 2026-11-21: Opened record from user request ("lets try out the skill - look at C:\Users\chris and christine\Desktop\Research\manuscripts and find something important to run the research skill on"; "write this up as a problem_8.md and save in appropriate place in C:\Users\chris and christine\Desktop\Research\manuscripts"). Proved C1 (rate limit + exact $O(\tau^n)$ second-order expansion + $2d\times 2d$ formula for $\mathsf{e}_0$), C2 (exact lossless-retention theorem $\bar{\mathsf{e}}(C) = \mathsf{ep} \iff \operatorname{row}(C) \supseteq \operatorname{range}(\Omega)$), C3 (Grassmannian descent + gradient), and refuted C4 via frequency-multiplexing family. Reporting gate: (1) answers Part 1 of `open:nrg-rate` + `obs:nrg-spectral` identically and strengthens them; answers Part 2 completely for $m \ge r_\Omega$ and partially for $2 \le m < r_\Omega$; (2) avoids citing unchecked block-Toeplitz theorems and avoids overselling Part 2; (3) strongest referee objections (invertibility of limit $K$, zeros of $\det S(z)$ on $|z|=1$) discharged via uniform ellipticity and Sylvester determinant bound $\det K \ge (c_{\min}/c_{\max})^{2d} > 0$; (4) review state is `self` only and no literature novelty check has been run; (5) remaining obligations O1–O3 recorded. Next action: fresh-context verification (O1) and literature check (O2) prior to manuscript integration.

---

## Derivations

### Proof of Theorem 1 (C1)

Let $N = n + 1$. By `thm:nrg-coarse`(b), $\mathsf{D}_n(C) = \tfrac{1}{2}[\operatorname{tr}(\widetilde{\mathsf{T}}_n^{-1}\mathsf{T}_n) - Nm]$, where $(\mathsf{T}_n)_{s,t} = \Gamma_{s-t}$ and $(\widetilde{\mathsf{T}}_n)_{s,t} = (\mathsf{P}_n\mathsf{T}_n\mathsf{P}_n^\top)_{s,t} = \Gamma_{t-s} = \Gamma_{s-t}^\top$ for $0 \le s, t \le N - 1$.

**Step 1 (Uniform positive definiteness and annulus of holomorphy).**
Consider the rational matrix function
$$S(z) := C(zI - A)^{-1} Q^\Xi (z^{-1}I - A^\top)^{-1} C^\top, \qquad z \in \mathbb{C}\setminus\{0\}.$$
Its poles lie in $\sigma(A) \cup \{\lambda^{-1} : \lambda \in \sigma(A)\setminus\{0\}\}$, which is disjoint from $|z|=1$ because $\rho(A) < 1$. On $|z|=1$ ($z = e^{i\vartheta}$), $S(\vartheta) := S(e^{i\vartheta})$ is Hermitian positive semidefinite: for any $v \in \mathbb{C}^m$,
$$v^* S(\vartheta) v = \bigl\|(Q^\Xi)^{1/2}(e^{-i\vartheta}I - A^\top)^{-1} C^\top v\bigr\|_2^2 \ge 0.$$
If $v^* S(\vartheta) v = 0$, invertibility of $(Q^\Xi)^{1/2}$ ($Q^\Xi \succ 0$) and of $e^{-i\vartheta}I - A^\top$ ($\rho(A) < 1$) implies $C^\top v = 0$, hence $v = 0$ because $C$ has full row rank $m$. By continuity of eigenvalues on the compact circle $[-\pi, \pi]$,
$$0 < c_{\min} := \min_{\vartheta\in[-\pi,\pi]} \lambda_{\min}\bigl(S(\vartheta)\bigr) \le \max_{\vartheta\in[-\pi,\pi]} \lambda_{\max}\bigl(S(\vartheta)\bigr) =: c_{\max} < \infty.$$
Because $\det S(z)$ is rational in $z$, nonzero on $|z|=1$, and satisfies $S(1/\bar z) = S(z)^*$, its zeros are finite in number, disjoint from $|z|=1$, and symmetric under $z \mapsto 1/\bar z$. Setting
$$r_1 := \max\bigl(\{\rho(A)\} \cup \{|z| : |z| < 1,\; \det S(z) = 0\}\bigr) \in [0, 1),$$
the matrix functions $S(z)^{-1}$, $S(z^{-1})^{-1}$ (which coincides with $\overline{S(\vartheta)}^{-1}$ on $|z|=1$ because $A, Q^\Xi, C$ are real), and $f(z) := \operatorname{tr}(S(z^{-1})^{-1}S(z)) - m$ are holomorphic on the open annulus $\mathcal{A}_{r_1} := \{z \in \mathbb{C} : r_1 < |z| < r_1^{-1}\}$.

**Step 2 (Fourier expansion, spectral bounds, and block-circulant approximation).**
Because $\rho(A) < 1$, $(e^{i\vartheta}I - A)^{-1} = e^{-i\vartheta}\sum_{j=0}^\infty A^j e^{-ij\vartheta}$ converges absolutely, so
$$S(\vartheta) = \sum_{j,l=0}^{\infty} C A^j Q^\Xi (A^\top)^l C^\top e^{-i(j-l)\vartheta} = \sum_{k=-\infty}^{\infty} \Gamma_k e^{-ik\vartheta},$$
where we used absolute summability and $\Sigma = \sum_{l=0}^\infty A^l Q^\Xi (A^\top)^l$. Hence $\Gamma_{s-t} = \frac{1}{2\pi}\int_{-\pi}^{\pi} S(\vartheta) e^{i(s-t)\vartheta}\,d\vartheta$. For any $x = (x_0,\dots,x_{N-1}) \in \mathbb{C}^{Nm}$ with $\hat x(\vartheta) := \sum_{s=0}^{N-1} x_s e^{-is\vartheta}$, Parseval's identity gives
$$x^* \mathsf{T}_n x = \frac{1}{2\pi}\int_{-\pi}^{\pi} \hat x(\vartheta)^* S(\vartheta)\hat x(\vartheta)\,d\vartheta \in \bigl[c_{\min}\|x\|_2^2,\; c_{\max}\|x\|_2^2\bigr],$$
so $c_{\min} I \preceq \mathsf{T}_n, \widetilde{\mathsf{T}}_n \preceq c_{\max} I$ for every $n \ge 1$.

Define the block-circulant matrix $\mathsf{C}_N \in \mathbb{R}^{Nm \times Nm}$ with $(s,t)$ block
$$(\mathsf{C}_N)_{s,t} := \frac{1}{N}\sum_{k=0}^{N-1} S(\vartheta_k) e^{i(s-t)\vartheta_k}, \qquad \vartheta_k := \frac{2\pi k}{N},$$
and $\widetilde{\mathsf{C}}_N := \mathsf{P}_n \mathsf{C}_N \mathsf{P}_n^\top$. Since $S(-\vartheta) = \overline{S(\vartheta)}$ and $k \mapsto -k \pmod N$ permutes $\{0,\dots,N-1\}$,
$$(\widetilde{\mathsf{C}}_N)_{s,t} = (\mathsf{C}_N)_{N-1-s,N-1-t} = \frac{1}{N}\sum_{k=0}^{N-1} S(\vartheta_k) e^{i(t-s)\vartheta_k} = \frac{1}{N}\sum_{k=0}^{N-1} \overline{S(\vartheta_k)} e^{i(s-t)\vartheta_k}.$$
Under the unitary block-DFT $\mathsf{F}_N$ with $(k,s)$ block $N^{-1/2}e^{-is\vartheta_k}I_m$, $\mathsf{F}_N \mathsf{C}_N \mathsf{F}_N^* = \operatorname{diag}(S(\vartheta_k))_{k=0}^{N-1}$ and $\mathsf{F}_N \widetilde{\mathsf{C}}_N \mathsf{F}_N^* = \operatorname{diag}(\overline{S(\vartheta_k)})_{k=0}^{N-1}$. Thus $c_{\min}I \preceq \mathsf{C}_N, \widetilde{\mathsf{C}}_N \preceq c_{\max}I$, and
$$\mathsf{D}_n^{\mathrm{circ}}(C) := \frac{1}{2}\Bigl[\operatorname{tr}\bigl(\widetilde{\mathsf{C}}_N^{-1}\mathsf{C}_N\bigr) - Nm\Bigr] = \frac{1}{2}\sum_{k=0}^{N-1} f(\vartheta_k).$$
Expanding $f(\vartheta) = \sum_{\ell\in\mathbb{Z}} \hat f_\ell e^{i\ell\vartheta}$, Cauchy's integral estimate on $\mathcal{A}_{r_1}$ yields $|\hat f_\ell| \le M_f r^{|\ell|}$ for any fixed $r \in (r_1, 1)$. By discrete orthogonality,
$$\mathsf{D}_n^{\mathrm{circ}}(C) = \frac{N}{2}\sum_{q\in\mathbb{Z}} \hat f_{qN} = (n+1)\bar{\mathsf{e}}(C) + \frac{N}{2}\sum_{q\ne 0} \hat f_{qN} = (n+1)\bar{\mathsf{e}}(C) + O(N r^N).$$

**Step 3 (Exact rank-$\le 2d$ boundary factorization of $\Delta_N := \mathsf{C}_N - \mathsf{T}_n$).**
By discrete orthogonality applied to the absolutely convergent series $S(\vartheta) = \sum_{\ell\in\mathbb{Z}} \Gamma_\ell e^{-i\ell\vartheta}$, $(\mathsf{C}_N)_{s,t} = \sum_{q\in\mathbb{Z}} \Gamma_{s-t+qN}$. Subtracting $(\mathsf{T}_n)_{s,t} = \Gamma_{s-t}$ gives
$$(\Delta_N)_{s,t} = \sum_{q\ge 1} \Gamma_{s-t+qN} + \sum_{q\ge 1} \Gamma_{t-s+qN}^\top, \qquad 0 \le s, t \le N - 1.$$
For every $q \ge 1$ and $0 \le s, t \le N - 1$, $s - t + qN = s + (q-1)N + 1 + (N - 1 - t) \ge 1$. Because $\rho(A^N) = \rho(A)^N < 1$, $(I - A^N)$ is invertible and $\sum_{r=0}^\infty A^{rN} = (I - A^N)^{-1}$, yielding (without inverting $A$):
$$\sum_{q\ge 1} \Gamma_{s-t+qN} = (C A^s)\Bigl(\sum_{r=0}^{\infty} A^{rN}\Bigr) A \bigl(A^{N-1-t}\Sigma C^\top\bigr) = (C A^s) M_N \bigl(C\Sigma(A^\top)^{N-1-t}\bigr)^\top, \qquad M_N := (I - A^N)^{-1} A.$$
Define $L_1, L_2 \in \mathbb{R}^{Nm \times d}$ with blocks $(L_1)_s = C A^s$ and $(L_2)_s = C\Sigma(A^\top)^s$, $R_1 := \mathsf{P}_n L_1$, $R_2 := \mathsf{P}_n L_2$, $W_N := [L_1, R_2] \in \mathbb{R}^{Nm \times 2d}$, $\widetilde{W}_N := \mathsf{P}_n W_N = [R_1, L_2]$, and the real symmetric matrix $H_N := \begin{pmatrix}0 & M_N \\ M_N^\top & 0\end{pmatrix} \in \mathbb{R}^{2d \times 2d}$. Then
$$\Delta_N = W_N H_N W_N^\top, \qquad \widetilde{\Delta}_N := \mathsf{P}_n \Delta_N \mathsf{P}_n^\top = \widetilde{W}_N H_N \widetilde{W}_N^\top.$$

**Step 4 (Woodbury identity and uniform invertibility of $K_N$).**
Define the four $2d \times 2d$ real matrices
$$G_{1,N} := \widetilde{W}_N^\top \widetilde{\mathsf{C}}_N^{-1} \widetilde{W}_N, \quad G_{2,N} := W_N^\top \widetilde{\mathsf{C}}_N^{-1} W_N, \quad G_{3,N} := \widetilde{W}_N^\top \widetilde{\mathsf{C}}_N^{-1}\mathsf{C}_N \widetilde{\mathsf{C}}_N^{-1} \widetilde{W}_N, \quad G_{4,N} := \widetilde{W}_N^\top \widetilde{\mathsf{C}}_N^{-1} W_N,$$
and set $K_N := I_{2d} - H_N G_{1,N}$. With $X := \widetilde{\mathsf{C}}_N^{-1/2}\widetilde{W}_N$, one has
$$\widetilde{\mathsf{C}}_N^{-1/2}\widetilde{\mathsf{T}}_n\widetilde{\mathsf{C}}_N^{-1/2} = I_{Nm} - X H_N X^\top.$$
By Sylvester's determinant identity ($\lambda^q \det(\lambda I_p - PQ) = \lambda^p \det(\lambda I_q - QP)$ with $P = X$, $Q = H_N X^\top$), the multisets of eigenvalues of $I_{Nm} - X H_N X^\top$ and $K_N = I_{2d} - H_N X^\top X$ coincide away from $1$. Since $\widetilde{\mathsf{C}}_N^{-1/2}\widetilde{\mathsf{T}}_n\widetilde{\mathsf{C}}_N^{-1/2}$ is real symmetric with all eigenvalues in $[c_{\min}/c_{\max},\; c_{\max}/c_{\min}]$ (which contains $1$), every eigenvalue of $K_N$ is real and lies in $[c_{\min}/c_{\max},\; c_{\max}/c_{\min}]$. Hence $K_N$ is invertible with
$$\det K_N \ge \Bigl(\frac{c_{\min}}{c_{\max}}\Bigr)^{2d} > 0 \qquad \text{for every } N \ge 1.$$
Direct multiplication verifies the Woodbury formula (requiring invertibility only of $\widetilde{\mathsf{C}}_N$ and $K_N$, not $H_N$):
$$\widetilde{\mathsf{T}}_n^{-1} = (\widetilde{\mathsf{C}}_N - \widetilde{W}_N H_N \widetilde{W}_N^\top)^{-1} = \widetilde{\mathsf{C}}_N^{-1} + \widetilde{\mathsf{C}}_N^{-1}\widetilde{W}_N K_N^{-1} H_N \widetilde{W}_N^\top \widetilde{\mathsf{C}}_N^{-1}.$$
Multiplying on the right by $\mathsf{T}_n = \mathsf{C}_N - W_N H_N W_N^\top$, taking traces, and using cyclicity yields the exact finite-$N$ identity
$$2\bigl(\mathsf{D}_n(C) - \mathsf{D}_n^{\mathrm{circ}}(C)\bigr) = -\operatorname{tr}(H_N G_{2,N}) + \operatorname{tr}(K_N^{-1} H_N G_{3,N}) - \operatorname{tr}(K_N^{-1} H_N G_{4,N} H_N G_{4,N}^\top).$$

**Step 5 (Exponential convergence as $N \to \infty$).**
Fix any $r \in (r_1, 1)$. Then $\|M_N - A\|_2 = \|(I - A^N)^{-1}A^{N+1}\|_2 = O(r^N)$, so $H_N \to H := \begin{pmatrix}0 & A \\ A^\top & 0\end{pmatrix}$ at rate $O(r^N)$. For any block-circulant $\mathsf{B}_N$ with holomorphic symbol $B(z) = \sum_{\ell\in\mathbb{Z}} B_\ell z^{-\ell}$ on $\mathcal{A}_{r_1}$ (having $\|B_\ell\|_2 \le M_B r^{|\ell|}$) and any block-column matrices $L(F), L(G)$ with $\|F_s\|_2, \|G_t\|_2 \le M_0 r^s$ and generating functions $\widehat{F}(\vartheta) = \sum_{s\ge 0} F_s e^{-is\vartheta}$, $\widehat{G}(\vartheta) = \sum_{t\ge 0} G_t e^{-it\vartheta}$ (note $\widehat{F}(\vartheta)^* = \widehat{F}(-\vartheta)^\top$ for real $F_s$):
1. *Left–Left:*
   $$L(F)^\top \mathsf{B}_N L(G) = \sum_{s,t=0}^{N-1} F_s^\top \Bigl(\sum_{q\in\mathbb{Z}} B_{s-t+qN}\Bigr) G_t = \frac{1}{2\pi}\int_{-\pi}^{\pi} \widehat{F}(\vartheta)^* B(\vartheta)\widehat{G}(\vartheta)\,d\vartheta + O(N r^N),$$
   since the tail $\max(s,t) \ge N$ satisfies $s + |s-t| + t = 2\max(s,t)$ (contributing $O(N r^{2N})$) and aliasing $q \ge 1$ has $s + (qN + s - t) + t = qN + 2s$ (contributing $O(N r^N)$, and symmetrically for $q \le -1$).
2. *Right–Right:* Putting $u = N - 1 - s$, $v = N - 1 - t$ gives
   $$R(F)^\top \mathsf{B}_N R(G) = \frac{1}{2\pi}\int_{-\pi}^{\pi} \bigl(e^{i\vartheta}\widehat{F}(-\vartheta)\bigr)^* B(\vartheta)\bigl(e^{i\vartheta}\widehat{G}(-\vartheta)\bigr)\,d\vartheta + O(N r^N).$$
3. *Left–Right:* Putting $v = N - 1 - t$, the $q=1$ mode yields $\sum_{s,v\ge 0} F_s^\top B_{s+v+1} G_v = \frac{1}{2\pi}\int_{-\pi}^{\pi} \widehat{F}(\vartheta)^* B(\vartheta)(e^{i\vartheta}\widehat{G}(-\vartheta))\,d\vartheta$ with $O(r^{2N})$ tail; the $q=0$ aliasing mode obeys $s + v + |s+v+1-N| \ge N-1$ (contributing $O(N^2 r^N)$), and $q \notin \{0,1\}$ contributes $O(r^N) + O(N^2 r^{2N})$.
4. *Right–Left:* Symmetrically,
   $$R(F)^\top \mathsf{B}_N L(G) = \frac{1}{2\pi}\int_{-\pi}^{\pi} \bigl(e^{i\vartheta}\widehat{F}(-\vartheta)\bigr)^* B(\vartheta)\widehat{G}(\vartheta)\,d\vartheta + O(N^2 r^N).$$

Setting $\widehat{L}_1(\vartheta) = C(I - e^{-i\vartheta}A)^{-1}$, $\widehat{L}_2(\vartheta) = C\Sigma(I - e^{-i\vartheta}A^\top)^{-1}$, $\Phi_W(\vartheta) = [\widehat{L}_1(\vartheta),\; e^{i\vartheta}\widehat{L}_2(-\vartheta)]$, and $\Phi_{\widetilde{W}}(\vartheta) = [e^{i\vartheta}\widehat{L}_1(-\vartheta),\; \widehat{L}_2(\vartheta)]$, all four block pairings collapse into
$$G_1 = \frac{1}{2\pi}\int_{-\pi}^{\pi} \Phi_{\widetilde{W}}^* \overline{S}^{-1} \Phi_{\widetilde{W}}\,d\vartheta, \qquad G_2 = \frac{1}{2\pi}\int_{-\pi}^{\pi} \Phi_W^* \overline{S}^{-1} \Phi_W\,d\vartheta,$$
$$G_3 = \frac{1}{2\pi}\int_{-\pi}^{\pi} \Phi_{\widetilde{W}}^* \overline{S}^{-1} S \overline{S}^{-1} \Phi_{\widetilde{W}}\,d\vartheta, \qquad G_4 = \frac{1}{2\pi}\int_{-\pi}^{\pi} \Phi_{\widetilde{W}}^* \overline{S}^{-1} \Phi_W\,d\vartheta,$$
with $\|G_{j,N} - G_j\|_2 = O(N^2 r^N)$ for $j = 1, 2, 3, 4$. Therefore $K_N \to K := I_{2d} - H G_1$ at rate $O(N^2 r^N)$, and by continuity of the determinant $\det K = \lim_N \det K_N \ge (c_{\min}/c_{\max})^{2d} > 0$, so $K$ is invertible and $K_N^{-1} \to K^{-1}$ at rate $O(N^2 r^N)$. Combining Step 2 and Step 4 gives
$$\mathsf{D}_n(C) = (n+1)\bar{\mathsf{e}}(C) + \tfrac{1}{2}\Bigl[-\operatorname{tr}(H G_2) + \operatorname{tr}(K^{-1} H G_3) - \operatorname{tr}(K^{-1} H G_4 H G_4^\top)\Bigr] + O(n^2 r^n) = n\bar{\mathsf{e}}(C) - \mathsf{e}_0(C) + O(n^2 r^n).$$
Because $r \in (r_1, 1)$ is arbitrary, $O(n^2 r^n) = O(\tau^n)$ for every $\tau \in (r_1, 1)$. $\square$

---

### Proof of Theorem 2 (C2)

**Step 1 (Precision difference and direct proof of $\bar{\mathsf{e}}(I) = \mathsf{ep}$).**
Since $A, Q^\Xi$ are real,
$$S_{\mathrm{full}}(\vartheta)^{-1} = (e^{-i\vartheta}I - A^\top)(Q^\Xi)^{-1}(e^{i\vartheta}I - A) = (Q^\Xi)^{-1} + A^\top(Q^\Xi)^{-1}A - e^{-i\vartheta}(Q^\Xi)^{-1}A - e^{i\vartheta}A^\top(Q^\Xi)^{-1}.$$
Conjugating and subtracting gives
$$S_{\mathrm{full}}(\vartheta)^{-1} - \overline{S_{\mathrm{full}}(\vartheta)}^{-1} = (e^{i\vartheta} - e^{-i\vartheta})\bigl((Q^\Xi)^{-1}A - A^\top(Q^\Xi)^{-1}\bigr) = 2i\sin(\vartheta)\,\Omega.$$
Integrating $\overline{S_{\mathrm{full}}(\vartheta)}^{-1}S_{\mathrm{full}}(\vartheta) - I = -(e^{i\vartheta} - e^{-i\vartheta})\Omega S_{\mathrm{full}}(\vartheta)$ over $[-\pi,\pi]$ using $\frac{1}{2\pi}\int_{-\pi}^\pi e^{\pm i\vartheta}S_{\mathrm{full}}(\vartheta)\,d\vartheta = \Gamma_{\pm 1}^{\mathrm{full}}$ yields $\bar{\mathsf{e}}(I) = -\tfrac{1}{2}\operatorname{tr}(\Omega(A\Sigma - \Sigma A^\top)) = \operatorname{tr}((Q^\Xi)^{-1}\mathsf{J}A^\top) = \mathsf{ep}$ (also immediate from Theorem 1 at $C = I$ and `thm:nrg-ep`).

**Step 2 (Pointwise Hermitian Schur-complement identity).**
Fix $\vartheta \in [-\pi,\pi]$ and put $M_0 = S_{\mathrm{full}}(\vartheta) \succ 0$, $M_1 = \overline{S_{\mathrm{full}}(\vartheta)} \succ 0$. Complete $C$ to an invertible real matrix $G = \begin{pmatrix}C \\ D\end{pmatrix} \in \mathrm{GL}(d, \mathbb{R})$ and replace $M_k$ by $G M_k G^\top$ (preserving both traces and transforming $M_0^{-1} - M_1^{-1} \mapsto G^{-\top}(M_0^{-1} - M_1^{-1})G^{-1}$). In these coordinates $C = [I_m, 0]$ and $M_k = \begin{pmatrix}A_k & B_k \\ B_k^* & D_k\end{pmatrix}$ with Schur complements $S_k := D_k - B_k^* A_k^{-1} B_k \succ 0$. Because $G$ is real and $M_1 = \overline{M_0}$, we have $A_1 = \overline{A_0}$, hence $\det M_1 = \det M_0$, $\det A_1 = \det A_0$, and $\det S_1 = \det S_0$. Applying the block-LDU inverse
$$M_1^{-1} = \begin{pmatrix}A_1^{-1} & 0 \\ 0 & 0\end{pmatrix} + \begin{pmatrix}-A_1^{-1}B_1 \\ I_{d-m}\end{pmatrix} S_1^{-1} \begin{pmatrix}-B_1^* A_1^{-1} & I_{d-m}\end{pmatrix}$$
and substituting $D_0 = S_0 + B_0^* A_0^{-1} B_0$ gives
$$\bigl[\operatorname{tr}(M_1^{-1}M_0) - d\bigr] - \bigl[\operatorname{tr}(A_1^{-1}A_0) - m\bigr] = \bigl[\operatorname{tr}(S_1^{-1}S_0) - (d - m)\bigr] + \bigl\|S_1^{-1/2}(A_0^{-1}B_0 - A_1^{-1}B_1)^* A_0^{1/2}\bigr\|_F^2.$$
Because $\det(S_1^{-1/2}S_0 S_1^{-1/2}) = 1$, AM–GM implies $\operatorname{tr}(S_1^{-1}S_0) \ge d - m$ with equality iff $S_0 = S_1$. The Frobenius term is nonnegative with equality iff $A_0^{-1}B_0 = A_1^{-1}B_1$. Since $(M_k^{-1})_{22} = S_k^{-1}$ and $(M_k^{-1})_{12} = -A_k^{-1}B_k S_k^{-1}$, equality holds iff the last $d - m$ columns of $M_0^{-1} - M_1^{-1}$ vanish, i.e., iff $\ker(C) \subseteq \ker(M_0^{-1} - M_1^{-1})$.

**Step 3 (Integration over $\vartheta$).**
The nonnegative integrand $\Delta(\vartheta) := [\operatorname{tr}(\overline{S_{\mathrm{full}}}^{-1}S_{\mathrm{full}}) - d] - [\operatorname{tr}(\overline{S}^{-1}S) - m]$ is continuous on $[-\pi,\pi]$. Hence $\mathsf{ep} - \bar{\mathsf{e}}(C) = \frac{1}{4\pi}\int_{-\pi}^\pi \Delta(\vartheta)\,d\vartheta = 0$ iff $\Delta(\vartheta) = 0$ for all $\vartheta$, iff $\ker(C) \subseteq \ker(2i\sin(\vartheta)\Omega)$ for all $\vartheta \in (0,\pi)$, iff $\ker(C) \subseteq \ker(\Omega)$. Since $\Omega^\top = -\Omega$, $\ker(\Omega)^\perp = \operatorname{range}(\Omega)$, so $\ker(C) \subseteq \ker(\Omega) \iff \operatorname{row}(C) \supseteq \operatorname{range}(\Omega)$. Because every real skew-symmetric matrix has even rank $r_\Omega \le 2\lfloor d/2\rfloor$, odd $d$ satisfies $r_\Omega \le d - 1$. $\square$

---

### Proof of Proposition 3 (C3 and Refutation of C4)

**Part (1) (Grassmannian invariance and gradient).**
For real $M \in \mathrm{GL}(m, \mathbb{R})$, replacing $C$ by $MC$ maps $S(\vartheta) \mapsto M S(\vartheta) M^\top$ and $\overline{S(\vartheta)} \mapsto M \overline{S(\vartheta)} M^\top$, leaving $\operatorname{tr}(\overline{S}^{-1}S)$ invariant. Hence $\bar{\mathsf{e}}$ is a smooth function on the compact Grassmannian $\mathrm{Gr}(m, d)$ and attains its global maximum. Under a real perturbation $C \mapsto C + \varepsilon E$, $\delta S = E S_{\mathrm{full}} C^\top + C S_{\mathrm{full}} E^\top$ and $\delta\overline{S} = E\overline{S_{\mathrm{full}}}C^\top + C\overline{S_{\mathrm{full}}}E^\top$; using $\operatorname{tr}(X^\top) = \operatorname{tr}(X)$, $S_{\mathrm{full}}^\top = \overline{S_{\mathrm{full}}}$, and $(\overline{S}^{-1})^\top = S^{-1}$, the two pairs of terms are complex conjugates of one another, yielding
$$\nabla_C \bar{\mathsf{e}}(C) = \frac{1}{2\pi}\int_{-\pi}^{\pi} \operatorname{Re}\Bigl[\overline{S(\vartheta)}^{-1} C S_{\mathrm{full}}(\vartheta) - \overline{S(\vartheta)}^{-1} S(\vartheta) \overline{S(\vartheta)}^{-1} C \overline{S_{\mathrm{full}}(\vartheta)}\Bigr]\,d\vartheta,$$
and right-multiplying by $C^\top$ gives $\frac{1}{2\pi}\int_{-\pi}^\pi \operatorname{Re}[\overline{S}^{-1}S - \overline{S}^{-1}S]\,d\vartheta = 0$.

**Part (2) (Counterexample refuting C4).**
Take $d = 4$, $Q^\Xi = I_4$, $A = \operatorname{diag}(r R(\varepsilon),\, r R(\pi - \varepsilon))$ with $r \in (0, 1)$, $\varepsilon \in (0, \pi/2)$, and $R(\phi) = \begin{pmatrix}\cos\phi & -\sin\phi \\ \sin\phi & \cos\phi\end{pmatrix}$. Then $A$ is normal with eigenvalues $r e^{\pm i\varepsilon}$ and $r e^{\pm i(\pi-\varepsilon)}$, $r_\Omega = 4$, and by `thm:nrg-ep`, $\mathsf{ep} = 8 r^2 \sin^2\varepsilon / (1 - r^2)$. The only $A$-invariant $2$-dimensional subspaces are the two coordinate planes, each retaining $\frac{1}{2}\mathsf{ep}$.

Now take $C_{\mathrm{mux}} = \frac{1}{\sqrt 2}[I_2, I_2]$. In the constant unitary basis $e_\pm = \frac{1}{\sqrt 2}(1, \pm i)^\top$, $R(\phi)e_\pm = e^{\mp i\phi}e_\pm$, so both $S_1(\vartheta)$ and $S_2(\vartheta)$ are diagonal in $\{e_+, e_-\}$:
$$2 S(\vartheta) = S_1(\vartheta) + S_2(\vartheta) = \lambda_+(\vartheta) e_+ e_+^* + \lambda_-(\vartheta) e_- e_-^*,$$
where $\lambda_+(\vartheta) = g(\vartheta + \varepsilon) + g(\vartheta + \pi - \varepsilon)$, $\lambda_-(\vartheta) = \lambda_+(-\vartheta)$, and $g(\alpha) := (1 - 2r\cos\alpha + r^2)^{-1}$. Because $\overline{S(\vartheta)} = S(-\vartheta)$ swaps $\lambda_+$ and $\lambda_-$,
$$\operatorname{tr}\bigl(\overline{S(\vartheta)}^{-1} S(\vartheta)\bigr) - 2 = \frac{\lambda_+(\vartheta)}{\lambda_-(\vartheta)} + \frac{\lambda_-(\vartheta)}{\lambda_+(\vartheta)} - 2.$$
Let $\delta := 1 - r \to 0^+$ at fixed $\varepsilon \in (0, \pi/2)$, so $\delta\,\mathsf{ep} \to 4\sin^2\varepsilon$. By the symmetries $\vartheta \mapsto -\vartheta$ and $\vartheta \mapsto \vartheta + \pi$, the integrand has four identical resonance peaks at $\vartheta \in \{\pm\varepsilon, \pm(\pi-\varepsilon)\}$, and is uniformly bounded as $\delta \to 0^+$ outside fixed $\eta$-neighborhoods of those four points ($0 < \eta < \min(\varepsilon, \pi/2 - \varepsilon)/2$). On $[-\varepsilon - \eta, -\varepsilon + \eta]$, substitute $\vartheta = -\varepsilon + \delta u$ ($|u| \le \eta/\delta$):
$$\delta^2 g(\delta u) = \frac{\delta^2}{\delta^2 + 4r\sin^2(\delta u / 2)} \longrightarrow \frac{1}{1 + u^2}, \qquad \lambda_-(-\varepsilon + \delta u) \longrightarrow \frac{1}{4\sin^2\varepsilon} + \frac{1}{4} = \frac{1 + \sin^2\varepsilon}{4\sin^2\varepsilon},$$
with integrable dominating envelope $C(\varepsilon)/(1 + u^2)$ because $\sin^2(\delta u/2) \ge c_0 (\delta u)^2$ on $|u| \le \eta/\delta$ and $\lambda_- \ge c_1 > 0$. By dominated convergence and $\int_{-\infty}^\infty (1+u^2)^{-1}\,du = \pi$, the four peaks give
$$\lim_{\delta \to 0^+} \delta\,\bar{\mathsf{e}}(C_{\mathrm{mux}}) = \frac{4}{4\pi} \cdot \frac{4\sin^2\varepsilon}{1 + \sin^2\varepsilon} \cdot \pi = \frac{4\sin^2\varepsilon}{1 + \sin^2\varepsilon},$$
hence $\lim_{r\to 1^-} \bar{\mathsf{e}}(C_{\mathrm{mux}})/\mathsf{ep} = (1 + \sin^2\varepsilon)^{-1} \in (\tfrac{1}{2}, 1)$. Letting $\varepsilon \to 0^+$ drives the retained fraction arbitrarily close to $1$. $\square$
