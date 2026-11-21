# Conjecture `conj:sca-common-code`: Sharp Boundary of Common-Code Amplification at Level 1

- Status: active
- Opened: 2026-11-21
- Updated: 2026-11-21
- Sessions: 1

**Manuscript anchors:** `Collective_Agents/sections/s08_scale.tex` (`conj:sca-common-code`), `Collective_Agents/sections/08_scale.tex` (`prop:sca-sufficient`), `Collective_Agents/sections/09_minimal.tex` (`prop:min-common-code`), `Collective_Agents/sections/app09_minimal.tex`, `Collective_Agents/sections/02_framework.tex` (`def:fw-system`), `Collective_Agents/sections/chk08_scale.tex` (`chk:sca-common-code`).

## Target

- Locked statement: Settle `conj:sca-common-code` (`s08_scale.tex` line 12): *"At identity encodings with one modality and one channel noise, in an isotropic world $F = f I_K$ with $0 < f < 1$, every frozen or periodic attention profile of level-1 receivers at its covariance fixed point has a mean map over one period of length $p$ with spectral radius at most $f^p$. Such profiles then satisfy `(M)` in uniform form, and frozen ones satisfy `(C_\rho)` at every rate above $f$."*
- Falsifier: Any admissible frozen or period-$p$ attention profile of level-1 receivers with one common effective code $H_j = H$ (identity encodings, one modality, one channel noise $R_c \succ 0$) in an isotropic world $F = f I_K$ ($0 < f < 1$, $Q \succ 0$) whose converged periodic covariance orbit has period mean map $W^{(p)} = f^p W^{\mathrm{rec}}(p-1)\cdots W^{\mathrm{rec}}(0)$ with $\rho(W^{(p)}) > f^p$ (and even more strongly, $\rho(W^{(p)}) > 1$, violating the moment bound `(M)` itself).
- May assume: Level-1 reception equations (`def:fw-system`, `app09_minimal.tex` proof of `prop:min-common-code`): $B_j(t) = H^\top(R_c + H P_j(t) H^\top)^{-1} H$, $\Lambda_i^+(t) = \Lambda_i(t) + \Gamma_i(t) + \sum_{j \in J_i(t)} B_j(t)$, $P_i(t+1) = f^2 (\Lambda_i^+(t))^{-1} + Q$, and $(W^{\mathrm{rec}}(t) e)_i = (\Lambda_i^+(t))^{-1}[\Lambda_i(t) e_i + \sum_{j \in J_i(t)} B_j(t) e_j]$.
- Must not assume: Symmetry of the listening graph (except when constructing a symmetric counterexample); absence of sensing; rank-1 restriction on $H$ unless explicitly stated as the scope of a positive theorem.
- Alternative forms: Separate the conjecture cleanly along its exact mathematical boundary: (1) prove the maximal positive theorem (frozen rank-1 common code on arbitrary directed graphs with arbitrary sensing), (2) refute the general conjecture for both higher-rank frozen common codes ($r_c \ge 2$) and multi-channel periodic rank-1 profiles ($p = 2$), and (3) isolate any remaining open sub-regime (single-sensor-per-agent periodic rank-1 profiles).
- Test instance: `prop:min-common-code` / `chk:sca-common-code`: symmetric 2-agent reciprocal loop with rank-1 common code ($K = 2, F = f I_2, Q = I_2, R_c = 1$) must satisfy $\rho(W^{\mathrm{rec}}) \le 1$; two distinct rank-1 codes with $P_1 = \begin{pmatrix}10 & 3\\ 3 & 1\end{pmatrix}, P_2 = \begin{pmatrix}1 & 3\\ 3 & 10\end{pmatrix}$ violates $\rho(W^{\mathrm{rec}}) \le 1$ (`lem:min-disagreement`, giving $\rho = 1.18$).
- Out of scope: Non-isotropic world dynamics $F \ne f I_K$; sender-specific codes or multiple modalities (already known to amplify via `ex:sca-amplifying-profile`); exact-fusion receivers.
- Reading chosen: Literal reading of `conj:sca-common-code` under `def:fw-system` (where common code $H$ can have any rank $r_c \ge 1$, listening graphs can be directed, and an agent's periodic attention set $\mathcal{J}_i(t)$ selects among world channels and message channels).

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| Level-1 message precision | $B_j = H^\top(R_c + H P_j H^\top)^{-1} H \succeq 0$ (for rank-1 $H_j = \vartheta_j T_c$, $R_c = 1$: $B_j = \alpha_j T_c^\top T_c$ with $\alpha_j = \vartheta_j^2/(1 + \vartheta_j^2 T_c P_j T_c^\top)$) | For $H = (3, 0)$, $P = \operatorname{diag}(1, 1)$, $R_c = 1$: $\alpha = 9/10$, $B = \operatorname{diag}(0.9, 0)$ |
| Homogeneous reception map | $(W^{\mathrm{rec}} e)_i = (\Lambda_i^+)^{-1}[\Lambda_i e_i + \sum_{j \in J_i} B_j e_j]$, with $\Lambda_i = P_i^{-1}$, $\Lambda_i^+ = \Lambda_i + \Gamma_i + \sum_{j \in J_i} B_j$ | For $H = (3,0), H' = (0,3)$, $P_1 = \begin{pmatrix}10&3\\3&1\end{pmatrix}, P_2 = \begin{pmatrix}1&3\\3&10\end{pmatrix}$, $\Gamma=0$: $\rho(W^{\mathrm{rec}}) = 1.18$ |
| Periodic covariance orbit | $P_i(t+1) = f^2 (\Lambda_i^+(t))^{-1} + Q$, $t \bmod p$; period map $W^{(p)} = f^p W^{\mathrm{rec}}(p-1)\cdots W^{\mathrm{rec}}(0)$ | Conjecture claims $\rho(W^{(p)}) \le f^p$, i.e., $\rho_{\mathrm{rec}} := \rho(W^{(p)})/f^p \le 1$ |
| Listening digraph orientation | Edge $i \to j$ means $j \in J_i$ ($i$ listens to $j$); a sink SCC $C$ has no edge leaving $C$ ($i \in C \implies J_i \subseteq C$) | On an undirected graph, every connected component is a sink SCC |

## Claims

### C1: Literal `conj:sca-common-code` (no amplification for any frozen or periodic common-code profile)

- Statement: At identity encodings with one modality and one channel noise in an isotropic world $F = f I_K$ ($0 < f < 1$), every frozen or periodic attention profile of level-1 receivers at its covariance fixed point has a period-$p$ mean map with $\rho(W^{(p)}) \le f^p$ (and hence satisfies the moment bound `(M)`).
- Status: refuted
- Review: self
- Evidence: Refuted independently by both C3 (frozen symmetric 2-agent reciprocal loop with one common rank-2 code and one fixed rank-1 sensor per agent, giving $\rho(W) = 0.950184 > 0.95$ and $\rho(W) = 1.000129 > 1$ at $f = 0.9999$) and C4 (period-2 symmetric 2-agent profile with one common rank-1 code and two world channels per agent, giving $\rho(W^{(2)}) = 0.918584 > 0.95^2$ at $f=0.95$ and $\rho(W^{(2)}) = 1.006893 > 1$ at $f=0.995$), verified by both Riccati fixed-point eigendecomposition (residual $\le 8.9 \times 10^{-15}$) and direct time-domain propagation in `conj_sca_common_code-checks/verify_common_code.py` and `conj_sca_common_code-checks/verify_common_code_output.txt`.
- Depends on: C3, C4

### C2: Frozen rank-one common code never amplifies on any directed graph with arbitrary sensing (Theorem 1)

- Statement: Let the effective codes be positive multiples of one nonzero row vector $H_j = \vartheta_j T_c$ ($\vartheta_j > 0$, $T_c \in \mathbb{R}^{1 \times K} \setminus \{0\}$) with $R_c = 1$, arbitrary covariances $P_i \succ 0$, arbitrary sensing precisions $\Gamma_i = (H_i^s)^\top (R_i^s)^{-1} H_i^s \succeq 0$, and an arbitrary (possibly asymmetric/directed) listening relation $J_i \subseteq V \setminus \{i\}$. Then every eigenvalue of $W^{\mathrm{rec}}$ satisfies either $|\lambda| < 1$ or $\lambda = 1$; in particular $\rho(W^{\mathrm{rec}}) \le 1$, with strict inequality $\rho(W^{\mathrm{rec}}) < 1$ if and only if $\ker H_i^s \cap \ker T_c = \{0\}$ for every $i \in V$ and every sink strongly connected component of the listening digraph contains an agent with injective $H_i^s$. Consequently, in an isotropic world $F = f I_K$ ($0 < f < 1$), every frozen rank-one common-code profile at a covariance fixed point satisfies $\rho(W) = f\rho(W^{\mathrm{rec}}) \le f < 1$, hence `(M)` and `(C_\rho)` at every rate above $f$.
- Status: proved
- Review: fresh-context (2026-11-21: a step-by-step reconstruction of the Theorem 1 proof and a blind independent proof both confirm C2, 4000 + 3000 random directed instances with 0 eigenvalues outside the disk-or-1 set; only repair: state $R^s_i \succ 0$ so that $\ker \Gamma_i = \ker H^s_i$, or phrase the criterion with $\ker \Gamma_i$; checks in `conj_sca_common_code-checks/c2_reconstruct_*` and `c2_blind_*`; adopted as `prop:min-common-code`(d))
- Evidence: Complete self-contained 12-line proof in Section `Derivations` (Theorem 1) of this record via the Herglotz positivity $\operatorname{Re}(\lambda T_c(\lambda M_i - \Lambda_i)^{-1} T_c^\top) > 0$ on $\{|\lambda| \ge 1\} \setminus \{1\}$ and maximum-modulus contradiction; cross-checked on 1,500 random directed graphs ($N \in \{2..5\}, K \in \{2..4\}$, max $\rho(W^{\mathrm{rec}}) = 1.000000000000051$, max $|\lambda|$ for $\lambda \ne 1$ equal to $0.9999997798$) plus distinct-code negative control ($\rho = 1.18$) in `conj_sca_common_code-checks/verify_common_code.py` and `conj_sca_common_code-checks/verify_common_code_output.txt`.
- Depends on: none

### C3: Frozen symmetric rank-2 common-code counterexample (breaks both $\rho(W) \le f$ and `(M)`)

- Statement: For $N = 2$, $K = 2$, $F = f I_2$, $Q = I_2$, $R_c = I_2$, symmetric listening $J_0 = \{1\}, J_1 = \{0\}$, one common rank-2 code $H = \operatorname{diag}(10, 0.15)$, and one fixed rank-1 sensor per agent ($H_0^s = (0.5, 0.14)$, $H_1^s = (15, 4.6)$ with unit sensing noise), the converged covariance fixed point has $\rho(W^{\mathrm{rec}}) > 1$: specifically $\rho(W^{\mathrm{rec}}) = 1.000193192302$ ($\rho(W) = 0.950183532687 > f$) at $f = 0.95$, $\rho(W^{\mathrm{rec}}) = 1.000222083041$ ($\rho(W) = 0.990219862211 > f$) at $f = 0.99$, and $\rho(W^{\mathrm{rec}}) = 1.000228814026$ ($\rho(W) = 1.000128791144 > 1$, violating `(M)`) at $f = 0.9999$.
- Status: computed
- Review: self
- Evidence: Riccati fixed-point solve (residual $\le 8.9 \times 10^{-15}$ in $\le 103$ iterations) cross-checked against 400-round direct time-domain propagation (matching to 12 digits) plus parallel-sensor control ($\rho(W^{\mathrm{rec}}) = 1.000000000000$) in `conj_sca_common_code-checks/verify_common_code.py` and `conj_sca_common_code-checks/verify_common_code_output.txt`.
- Scope: Exact double-precision computation for the specified $N=2, K=2$ frozen system at $f \in \{0.95, 0.99, 0.9999\}$, fixed-point residual $\le 8.9 \times 10^{-15}$, time-domain propagation agreement $< 10^{-10}$.
- Depends on: none

### C4: Period-2 symmetric rank-1 common-code counterexample with 2 world channels per agent (breaks both $\rho(W^{(2)}) \le f^2$ and `(M)`)

- Statement: For $N = 2$, $K = 2$, $F = f I_2$, $Q = I_2$, $R_c = 1$, one common rank-1 code $H = (100, 0)$, and the mirror-symmetric period-2 attention profile under `def:fw-system` where at $t = 0$ both agents listen to each other ($J_0 = \{1\}, J_1 = \{0\}$) and sense $H_0^s(0) = 200(1, +0.3)$, $H_1^s(0) = 200(1, -0.3)$ while at $t = 1$ neither listens and they sense $H_0^s(1) = 100(1, +0.35)$, $H_1^s(1) = 100(1, -0.35)$ (unit sensing noise), the converged period-2 covariance orbit has $\rho(W^{(2)})/f^2 > 1.017$: specifically $\rho(W^{(2)}) = 0.918584264927 > 0.95^2$ at $f = 0.95$, $\rho(W^{(2)}) = 0.996992348180 > 0.99^2$ at $f = 0.99$, and $\rho(W^{(2)}) = 1.006892933019 > 1$ (per-round growth $1.0034405 > 1$, violating `(M)`) at $f = 0.995$.
- Status: computed
- Review: self
- Evidence: Periodic Riccati orbit solve (residual $0.0$ in $\le 58$ iterations) cross-checked against 300-period direct time-domain propagation (matching to 12 digits) plus no-listening control ($\rho_{\mathrm{rec}} = 0.922207 < 1$) in `conj_sca_common_code-checks/verify_common_code.py` and `conj_sca_common_code-checks/verify_common_code_output.txt`.
- Scope: Exact double-precision computation for the specified $N=2, K=2$ period-2 system at $f \in \{0.95, 0.99, 0.995\}$, orbit residual $0.0$, time-domain propagation agreement $< 10^{-10}$.
- Depends on: none

### C5: Periodic rank-1 common code with at most one fixed sensing channel per agent

- Statement: For a rank-1 common code $H = T_c$, $F = f I_K$ ($0 < f < 1$), $Q \succ 0$, and a period-$p$ ($p \ge 2$) attention profile in which each agent $i$ has at most one fixed sensing matrix $\Gamma_i$ (so $\Gamma_i(t) \in \{0, \Gamma_i\}$ at every round $t$), does every periodic covariance orbit satisfy $\rho(W^{(p)}) \le f^p$?
- Status: open
- Review: none
- Evidence: Open; none of our random sweeps or Nelder–Mead optimizations across 6 two-agent and 4 three-agent single-sensor schedules exceeded $\rho(W^{(p)})/f^p = 1.0000000000$, while C4 shows switching between two slightly non-parallel world channels per agent immediately breaks both $f^2$ and $1$.
- Depends on: C2, C4

## Failed routes

### R1: Mirror-symmetric equal-norm sensing for frozen rank-2 amplification

- Tried: Searched mirror-symmetric equal-strength sensors $g_1 = s(\cos\theta, \sin\theta)$, $g_2 = s(\cos\theta, -\sin\theta)$ on a $K=2$ symmetric 2-cycle with common rank-2 code $H = h I_2$ or $\operatorname{diag}(h_1, h_2)$ to induce level-1 header code splitting.
- Failed because: Under equal-strength mirror-symmetric sensing on $K=2$, mutual listening shrinks both agents' variances symmetrically enough that $\rho(W^{\mathrm{rec}})$ stayed $\le 0.9995$ across the grid; amplification ($\rho(W^{\mathrm{rec}}) > 1$) emerged only when the two agents had asymmetric sensing strengths ($|g_1| \gg |g_0|$) with a slight angle mismatch and strongly anisotropic rank-2 $H = \operatorname{diag}(10, 0.15)$ (C3).
- Reopen if: Tested on $K \ge 3$ or non-isotropic $Q$ with mirror-symmetric sensors.

### R2: Trying to extend `prop:min-common-code` to rank-2 via a block-diagonal inner product $\tilde M$

- Tried: Checked whether a symmetric listening graph with common rank-2 code $H$ admits a self-adjointness metric $\tilde M = \operatorname{diag}_i(M_i)$ making $W^{\mathrm{rec}}$ a contraction.
- Failed because: For $r_c \ge 2$, $B_j = H^\top(R_c + H P_j H^\top)^{-1} H$ varies in matrix direction (not just scalar weight) across senders $j$, so $W^{\mathrm{rec}}$ is genuinely non-self-adjoint and C3 proves $\rho(W^{\mathrm{rec}}) > 1$ even on a symmetric 2-cycle.
- Reopen if: All senders share identical coded covariance $H P_j H^\top$ (so $B_j$ is independent of $j$), in which case $W^{\mathrm{rec}}$ is self-adjoint in $\operatorname{diag}_i(\Lambda_i^+)$.

## Open obligations

- [ ] O1 (sessions: 1): Run a fresh-context proof reconstruction (`research-proof-checker`) on C2 (Theorem 1) and blind recomputation (`research-symbolic-numerics`) on C3 and C4 before updating `09_minimal.tex`, `s08_scale.tex`, and `app09_minimal.tex`.
- [ ] O2 (sessions: 1): Settle C5 (prove or refute $\rho(W^{(p)}) \le f^p$ for period-$p$ rank-1 common-code profiles when each agent has only one fixed world channel $\Gamma_i(t) \in \{0, \Gamma_i\}$).
- [ ] O3 (sessions: 1): Check whether the counterexamples C3 and C4 can be selected by expected free energy (strict best-response orbits at $\gamma = \infty$), paralleling `ex:sca-amplifying-profile`.

## Literature

| Claim | Source | Locator | Read depth | Date read | Verdict |
| --- | --- | --- | --- | --- | --- |
| Conjecture statement | `Collective_Agents/sections/s08_scale.tex` | `conj:sca-common-code` (lines 12–16) | full statement | 2026-11-21 | exact conjecture and scope verified |
| Existing rank-1 cases | `Collective_Agents/sections/09_minimal.tex` & `app09_minimal.tex` | `prop:min-common-code`, `lem:min-disagreement` | full proofs | 2026-11-21 | verified level-1 reception formulas and prior scope |
| World-channel attention | `Collective_Agents/sections/02_framework.tex` | `def:fw-system` (line 13) | full definition | 2026-11-21 | confirmed attention set $\mathcal{J}_i(t)$ selects among world channels and message channels |
| Prior numerical checks | `Collective_Agents/sections/chk08_scale.tex` | `chk:sca-common-code` (lines 25–27) | full check | 2026-11-21 | explains why random draws missed C3 (needs asymmetric norms + strongly anisotropic rank-2 $H$) and C4 (needs 2 world channels/agent) |

## Searches

| Query | Tool | Date | Not searched |
| --- | --- | --- | --- |
| none yet | — | 2026-11-21 | External literature on Herglotz/Nevanlinna spectral-radius bounds for block matrix consensus with rank-one couplings |

## Log

- 2026-11-21: Opened record from user request ("Write up a .MD and continue"). Proved Theorem 1 (C2): frozen rank-1 common code has $\sigma(W^{\mathrm{rec}}) \subset \{|\lambda| < 1\} \cup \{1\}$ on EVERY directed graph with arbitrary sensing and arbitrary covariances $P_i \succ 0$, with exact sink-SCC criterion for $\rho(W^{\mathrm{rec}}) < 1$ (eliminating the symmetric-listening restriction of `prop:min-common-code`(a)–(b)). Refuted literal `conj:sca-common-code` (C1) in BOTH directions beyond frozen rank-1: C3 (frozen symmetric 2-cycle, common rank-2 code, 1 fixed sensor/agent, $\rho(W) = 0.950184 > 0.95$ and $\rho(W) = 1.000129 > 1$ at $f=0.9999$) and C4 (period-2 symmetric 2-cycle, common rank-1 code, 2 world channels/agent, $\rho(W^{(2)}) = 1.006893 > 1$ at $f=0.995$). Reporting gate: (1) settles `conj:sca-common-code` by proving the maximal frozen rank-1 theorem and refuting both rank $\ge 2$ and multi-channel periodic extensions; (2) avoids claiming single-sensor-per-agent periodic rank-1 is settled (recorded as open C5) and avoids claiming EFE reachability of C3/C4 (recorded as O3); (3) strongest referee objections (whether $c_i(\lambda)$ can vanish on $|\lambda| \ge 1, \lambda \ne 1$; whether $\lambda=1$ eigenvector on a directed graph can vanish outside a sink SCC; whether C3/C4 are Riccati convergence artifacts) are discharged by explicit positivity $\operatorname{Re}(\lambda c_i(\lambda)) > 0$, block-lower-triangular spectral inclusion, and independent time-domain propagation matching eigenvalues to 12 digits with fixed-point residual $\le 8.9 \times 10^{-15}$; (4) review state is `self` only and no literature search was run; (5) obligations O1–O3 recorded. Next action: fresh-context verification (O1) and investigating C5/O3.

---

## Derivations

### Proof of Theorem 1 (C2)

Recall from `app09_minimal.tex` (proof of `prop:min-common-code`) that for effective codes $H_j = \vartheta_j T_c$ ($\vartheta_j > 0$, $T_c \in \mathbb{R}^{1 \times K} \setminus \{0\}$) and $R_c = 1$, we have $\alpha_j = \vartheta_j^2/(1 + \vartheta_j^2 T_c P_j T_c^\top) > 0$, $\bar\alpha_i := \sum_{j \in J_i} \alpha_j \ge 0$, $\Lambda_i = P_i^{-1} \succ 0$, $\Gamma_i = (H_i^s)^\top (R_i^s)^{-1} H_i^s \succeq 0$, $\Lambda_i^+ = \Lambda_i + \Gamma_i + \bar\alpha_i T_c^\top T_c$, and
$$(W^{\mathrm{rec}} e)_i = (\Lambda_i^+)^{-1}\Bigl[\Lambda_i e_i + \sum_{j \in J_i} \alpha_j T_c^\top (T_c e_j)\Bigr], \qquad i \in V.$$

**Step 1 (Exclusion of all eigenvalues in $\{|\lambda| \ge 1\} \setminus \{1\}$).**
Suppose $W^{\mathrm{rec}} e = \lambda e$ for some $\lambda \in \mathbb{C}$ with $|\lambda| \ge 1$, $\lambda \ne 1$, and $e = (e_1, \dots, e_N) \in (\mathbb{C}^K)^N$. Put $M_i := \Lambda_i + \Gamma_i \succ 0$ and $S_i := M_i^{-1/2} \Lambda_i M_i^{-1/2}$. Because $0 \prec \Lambda_i \preceq M_i$, the real symmetric matrix $S_i$ satisfies $0 \prec S_i \preceq I_K$, so every eigenvalue $s_{i,k}$ of $S_i$ lies in $(0, 1]$. Since $\lambda \notin (0, 1]$, the matrix $\lambda I_K - S_i$ is invertible, and hence $\lambda M_i - \Lambda_i = M_i^{1/2}(\lambda I_K - S_i)M_i^{1/2}$ is invertible for every $i \in V$.

Setting $x_i := T_c e_i \in \mathbb{C}$, the eigenvalue equation $\lambda \Lambda_i^+ e_i = \Lambda_i e_i + \sum_{j \in J_i} \alpha_j T_c^\top x_j$ rearranges to
$$(\lambda M_i - \Lambda_i) e_i = T_c^\top \Bigl(\sum_{j \in J_i} \alpha_j x_j - \lambda \bar\alpha_i x_i\Bigr).$$
Inverting $(\lambda M_i - \Lambda_i)$ and left-multiplying by $T_c$ gives
$$x_i = c_i(\lambda)\Bigl(\sum_{j \in J_i} \alpha_j x_j - \lambda \bar\alpha_i x_i\Bigr), \qquad c_i(\lambda) := T_c(\lambda M_i - \Lambda_i)^{-1} T_c^\top \in \mathbb{C}.$$
Let $u_i := M_i^{-1/2} T_c^\top \in \mathbb{R}^K \setminus \{0\}$ (nonzero because $T_c \ne 0$ and $M_i \succ 0$). Expanding $u_i$ in an orthonormal eigenbasis of $S_i$ with squared coordinates $w_{i,k} \ge 0$ ($\sum_{k=1}^K w_{i,k} = \|u_i\|_2^2 > 0$) yields
$$\lambda c_i(\lambda) = \sum_{k=1}^{K} \frac{w_{i,k} \lambda}{\lambda - s_{i,k}} = \sum_{k=1}^{K} w_{i,k} \frac{|\lambda|^2 - s_{i,k}\lambda}{|\lambda - s_{i,k}|^2},$$
and taking the real part gives
$$\operatorname{Re}\bigl(\lambda c_i(\lambda)\bigr) = \sum_{k=1}^{K} w_{i,k} \frac{|\lambda|^2 - s_{i,k}\operatorname{Re}(\lambda)}{|\lambda - s_{i,k}|^2}.$$
Because $s_{i,k} \in (0, 1]$ and $|\lambda| \ge 1$ with $\lambda \ne 1$, we have $\operatorname{Re}(\lambda) < |\lambda|^2$: if $\operatorname{Re}(\lambda) > 0$, then $|\lambda|^2 - s_{i,k}\operatorname{Re}(\lambda) \ge |\lambda|^2 - \operatorname{Re}(\lambda) > 0$; if $\operatorname{Re}(\lambda) \le 0$, then $|\lambda|^2 - s_{i,k}\operatorname{Re}(\lambda) \ge |\lambda|^2 \ge 1 > 0$. Since $\sum_k w_{i,k} > 0$, it follows that $\operatorname{Re}(\lambda c_i(\lambda)) > 0$ strictly, so $c_i(\lambda) \ne 0$ and
$$\operatorname{Re}\!\left(\frac{1}{\lambda c_i(\lambda)}\right) = \frac{\operatorname{Re}(\lambda c_i(\lambda))}{|\lambda c_i(\lambda)|^2} > 0 \qquad \text{for every } i \in V.$$

If $x = (x_1, \dots, x_N) = 0$, then $(\lambda M_i - \Lambda_i)e_i = 0$ for every $i$, forcing $e = 0$. Suppose $x \ne 0$ and choose $i^\star \in \arg\max_{i \in V} |x_i|$ with $|x_{i^\star}| > 0$. If $J_{i^\star} = \varnothing$, then $x_{i^\star} = 0$, contradiction; hence $\bar\alpha_{i^\star} > 0$. Rearranging the scalar equation at $i^\star$ and dividing by $|\lambda| |x_{i^\star}| > 0$ gives
$$\left|\frac{1}{\lambda c_{i^\star}(\lambda)} + \bar\alpha_{i^\star}\right| = \frac{1}{|\lambda| |x_{i^\star}|}\left|\sum_{j \in J_{i^\star}} \alpha_j x_j\right| \le \frac{1}{|\lambda|}\sum_{j \in J_{i^\star}} \alpha_j = \frac{\bar\alpha_{i^\star}}{|\lambda|} \le \bar\alpha_{i^\star}.$$
On the other hand, because $\bar\alpha_{i^\star} > 0$ and $\operatorname{Re}(1/(\lambda c_{i^\star}(\lambda))) > 0$,
$$\left|\frac{1}{\lambda c_{i^\star}(\lambda)} + \bar\alpha_{i^\star}\right| \ge \operatorname{Re}\!\left(\frac{1}{\lambda c_{i^\star}(\lambda)}\right) + \bar\alpha_{i^\star} > \bar\alpha_{i^\star},$$
a contradiction. Thus $e = 0$, proving $\sigma(W^{\mathrm{rec}}) \subset \{|\lambda| < 1\} \cup \{1\}$ and hence $\rho(W^{\mathrm{rec}}) \le 1$.

**Step 2 (Exact directed-graph criterion for $\rho(W^{\mathrm{rec}}) < 1$).**
By Step 1, $\rho(W^{\mathrm{rec}}) = 1$ if and only if $1 \in \sigma(W^{\mathrm{rec}})$, which (since $W^{\mathrm{rec}}$ is real) holds iff there is a nonzero real $e \in (\mathbb{R}^K)^N$ satisfying
$$\Gamma_i e_i + \sum_{j \in J_i} \alpha_j T_c^\top (x_i - x_j) = 0 \qquad \forall i \in V, \qquad x_i = T_c e_i \in \mathbb{R}.$$
- *Sufficiency of the strict-contraction condition:* Assume $\ker H_i^s \cap \ker T_c = \{0\}$ for all $i$ and every sink SCC of the listening digraph contains an agent with injective $H_i^s$. Let $e$ satisfy the equation above and put $m := \max_i |x_i|$. If $m = 0$, then $x_i = 0$ and $\Gamma_i e_i = 0$ for all $i$, so $e_i \in \ker H_i^s \cap \ker T_c = \{0\}$ for all $i$, hence $e = 0$. If $m > 0$, let $S := \{i \in V : |x_i| = m\} \ne \varnothing$. Dotting the equation at $i \in S$ with $e_i^\top$ yields
  $$e_i^\top \Gamma_i e_i + \sum_{j \in J_i} \alpha_j x_i (x_i - x_j) = 0.$$
  For every $j \in J_i$, $x_i(x_i - x_j) = m^2 - x_i x_j \ge 0$ (equality iff $x_j = x_i$), and $e_i^\top \Gamma_i e_i \ge 0$. Since every $\alpha_j > 0$, every $i \in S$ satisfies $H_i^s e_i = 0$ (hence $H_i^s$ is non-injective because $T_c e_i = x_i \ne 0 \implies e_i \ne 0$) and $x_j = x_i$ for all $j \in J_i$ (so $J_i \subseteq S$). Thus $S$ is a nonempty out-closed set in the finite listening digraph, so it contains at least one sink SCC $C \subseteq S$, every agent of which has non-injective $H_i^s$, contradicting the hypothesis. Hence $e = 0$ and $\rho(W^{\mathrm{rec}}) < 1$.
- *Necessity:* If some $i_0$ has a nonzero $v \in \ker H_{i_0}^s \cap \ker T_c$, placing $v$ at $i_0$ and $0$ elsewhere gives $W^{\mathrm{rec}} e = e$. Otherwise, if some sink SCC $C$ contains no agent with injective $H_i^s$, then for each $i \in C$ the nonzero subspace $\ker H_i^s$ meets $\ker T_c$ trivially and hence contains a vector $e_i$ with $T_c e_i = 1$. Because $C$ is a sink SCC ($i \in C \implies J_i \subseteq C$), ordering $C$ before $V \setminus C$ makes $W^{\mathrm{rec}}$ block lower triangular with top-left block $W^{\mathrm{rec}}_{CC}$ satisfying $W^{\mathrm{rec}}_{CC} e_C = e_C$, so $1 \in \sigma(W^{\mathrm{rec}}_{CC}) \subseteq \sigma(W^{\mathrm{rec}})$ and $\rho(W^{\mathrm{rec}}) = 1$.

Finally, in an isotropic world $F = f I_K$ ($0 < f < 1$) at a covariance fixed point of a frozen profile, $W = f W^{\mathrm{rec}}$, so $\rho(W) = f\rho(W^{\mathrm{rec}}) \le f < 1$, which gives `(C_\rho)` at every rate above $f$ and `(M)` in uniform form. $\square$
