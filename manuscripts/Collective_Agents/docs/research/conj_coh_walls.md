# Conjecture `conj:coh-walls` & `thm:coh-domains-1d`(b): Exact 1D Domain-Wall Count and Sharp Drawdown Bound

- Status: active
- Opened: 2026-11-21
- Updated: 2026-11-21
- Sessions: 1

**Manuscript anchors:** `Collective_Agents/sections/06_coherence.tex` (`thm:coh-domains-1d`), `Collective_Agents/sections/app06_coherence.tex` (`lem:coh-structure`, `lem:coh-counting`, `lem:coh-drawdown`, `conj:coh-walls`, proof of `thm:coh-domains-1d`), `Collective_Agents/sections/chk06_coherence.tex` (`chk:coh-domains`).

## Target

- Locked statement: (1) Settle `conj:coh-walls` (`app06_coherence.tex` line 210): *"On an open chain the number of domains of the minimizer of the pairwise potential equals the number of switches of the greedy $J$-hysteresis or exceeds it by one, so that the mean domain length tends almost surely to $\mathbb{E} T_J$ of `lem:coh-drawdown`."* (2) Sharpen `lem:coh-counting` (currently $\lfloor\Psi_N/2\rfloor - 1 \le \#\mathrm{walls}(\sigma^\ast) \le 2\Psi_N + 4$, a factor-of-4 gap) on both open chains and rings. (3) Sharpen `lem:coh-drawdown` (currently $(J/h)^2 \le \mathbb{E} T_J \le 13(J/h)^2 + 3.25$) and the resulting main-text bound in `thm:coh-domains-1d`(b) (currently $\tfrac{1}{2}(J/h)^2 \le \liminf \bar\ell_N \le \limsup \bar\ell_N \le 26(J/h)^2 + 7$).
- Falsifier: For literal `conj:coh-walls`: any real sequence $(h_1, \dots, h_N)$ and $J > 0$ whose unique open-chain minimizer $\sigma^\ast$ has $\#\mathrm{domains}(\sigma^\ast) \notin \{\Psi_N, \Psi_N + 1\}$. For the replacement theorems: any admissible $(h_1, \dots, h_N)$ violating $\Psi_N - 1 \le \#\mathrm{walls}(\sigma^\ast) \le \Psi_N + 1$ (with no run summing to $\pm J$), or any $J/h > 0$ where exact $\mathbb{E} T_J$ exits $[(J/h)^2, (J/h)^2 + \frac{\pi+4}{\sqrt{2\pi}}(J/h) + 2]$.
- May assume: `lem:coh-structure` (`app06_coherence.tex`), finiteness and lower bound $\mathbb{E} T_J \ge (J/h)^2$ of `lem:coh-drawdown`, and the renewal strong law of large numbers $\Psi_N/N \to 1/\mathbb{E} T_J$ a.s. from the proof of `thm:coh-domains-1d`(b).
- Must not assume: `conj:coh-walls` itself; unproven Brownian approximations or external Spitzer–Siegmund Wiener–Hopf asymptotics; uniqueness of minimizers where not stated.
- Alternative forms: If literal `conj:coh-walls` is false, exhibit explicit minimal counterexamples, establish the exact range of $\#\mathrm{domains}(\sigma^\ast) - \Psi_N$, and prove the asymptotic conclusion $\lim_{N\to\infty}\bar\ell_N = \mathbb{E} T_J$ a.s. on both open chains and rings.
- Test instance: `chk:coh-domains` (`chk06_coherence.tex` lines 66–70): at $J/h \in \{1, 2, 4, 8, 16\}$ with $4\times 10^5$ agents, measured mean domain lengths $4.71, 9.98, 26.75, 83.40, 306.5$; exact Fredholm values $\mathbb{E} T_J = 4.7498, 10.0035, 26.6792, 84.0008, 294.6439$.
- Out of scope: Higher-dimensional random-field Ising domains (`conj:coh-imry-ma`), finite-$\gamma$ coarsening (`conj:coh-coarsening`), and non-Gaussian pulls (though Theorems 1 and 2 are deterministic and apply to arbitrary real pulls $h_1,\dots,h_N$).
- Reading chosen: Literal reading of `conj:coh-walls` tested first (refuted), followed by exact deterministic wall-count theorems on both open chains and rings and a self-contained martingale/overshoot proof of the sharp Gaussian drawdown bound.

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| Pairwise potential | $\Phi_{\mathrm{code}}(\sigma) = J\sum_e \mathbf{1}[\sigma_i \ne \sigma_j] - \sum_{i=1}^N h_i\sigma_i$, $J > 0$, $\sigma_i \in \{-1,+1\}$ | For $N=2, J=1, h=(0.6,-0.6)$ on open chain: $\Phi(+,+)=0$, $\Phi(+,-)=-0.2$ |
| Field walk | $X_0 = 0$, $X_i = h_1 + \dots + h_i$ ($1 \le i \le N$) | For $h=(0.6,-0.6)$: $X = (0, 0.6, 0.0)$, range $= 0.6$ |
| Greedy $J$-hysteresis | First switch $g_1 = \min\{i : \max_{u\le i} X_u - \min_{u\le i} X_u \ge J\}$; subsequent switches on reversal $\ge J$ from running extreme since last switch; count $\Psi_N$ in $\{1,\dots,N\}$ | For $h=(0.6,-0.6), J=1$: $\Psi_2 = 0$; for $h=(0.76,-1.13,-0.90,0.89,-0.21), J=1$: $\Psi_5 = 1$ at $g_1 = 2$ (DOWN) |
| Viterbi DP gap | $D_i = \frac{1}{2}(V_-(i) - V_+(i))$, $D_0 = 0$, $D_i = \operatorname{clip}(D_{i-1}, -J/2, J/2) + h_i$ | For $h=(0.6,-0.6), J=1$: $D_1 = +0.6 > 0.5$, $D_2 = 0.5 - 0.6 = -0.1 < 0$ |
| Drawdown stopping time | $B_0 = 0$, $B_{u+1} = (B_u - h_{u+1})_+$ with $h_u \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0, h^2)$, $T_J = \min\{u : B_u \ge J\}$ | At $J/h = 2$: exact Fredholm $\mathbb{E} T_2 = 10.003527$, inside $[4, 11.6982]$ |

## Claims

### C1: Literal `conj:coh-walls` (open-chain domains in $\{\Psi_N, \Psi_N + 1\}$)

- Statement: On an open chain of $N \ge 2$ agents with $J > 0$ and pulls $(h_1, \dots, h_N)$, the number of domains of the minimizer $\sigma^\ast$ of $\Phi_{\mathrm{code}}$ equals $\Psi_N$ or $\Psi_N + 1$.
- Status: refuted
- Review: self
- Evidence: Minimal $N=2$ counterexample $J=1, h=(0.6,-0.6)$ (unique minimizer $(+1,-1)$, gap $0.20$, $\#\mathrm{domains}=2, \Psi_2=0$) and $N=5$ counterexample with $\Psi_5=1$, $h=(0.76,-1.13,-0.90,0.89,-0.21)$ (unique minimizer $(+1,-1,-1,+1,+1)$, gap $0.360$, $\#\mathrm{domains}=3, \Psi_5=1$); also occurs in $72/1000$ Gaussian chains at $N=400, J=4.0$; verified by exhaustive $2^N$ search in `conj_coh_walls-checks/verify_coh_walls.py` and `conj_coh_walls-checks/verify_coh_walls_output.txt`.
- Depends on: none

### C2: Exact deterministic wall-count bounds on open chains and rings (Theorem 1)

- Statement: For any $J > 0$, $(h_1, \dots, h_N) \in \mathbb{R}^N$, and any global minimizer $\sigma^\ast$ of $\Phi_{\mathrm{code}}$ on either the open chain or the ring: (1) $\#\mathrm{walls}(\sigma^\ast) \le \Psi_N + 1$ unconditionally; (2) if no run of consecutive pulls sums to $\pm J$, then $\#\mathrm{walls}(\sigma^\ast) \ge \Psi_N - 1$; (3) consequently, on the ring under (2), $\#\mathrm{walls}(\sigma^\ast_{\mathrm{ring}}) = \Psi_N$ exactly whenever $\Psi_N$ is even, and $\#\mathrm{walls}(\sigma^\ast_{\mathrm{ring}}) \in \{\Psi_N - 1, \Psi_N + 1\}$ whenever $\Psi_N$ is odd.
- Status: proved
- Review: self
- Evidence: Complete self-contained proof in Section `Derivations` (Theorem 1) of this record (Alternating-Jump Lemma + alternating-spin lower bound); verified with 0 violations against exhaustive $2^N$ brute-force search on 3,000 open chains and 3,000 rings ($N \in \{2,3,5,8,10\}$) in `conj_coh_walls-checks/verify_coh_walls.py` and `conj_coh_walls-checks/verify_coh_walls_output.txt`.
- Depends on: none

### C3: Exact open-chain domain identity via Viterbi clipped walk (Theorem 2)

- Statement: With $D_0 = 0$, $D_i = \operatorname{clip}(D_{i-1}, -J/2, J/2) + h_i$ ($1 \le i \le N$) and generic non-degeneracy ($|D_i| \ne J/2$ for $1 \le i \le N-1$, $D_N \ne 0$, no run sums to $\pm J$), the unique open-chain minimizer $\sigma^\ast_{\mathrm{open}}$ satisfies $\#\mathrm{domains}(\sigma^\ast_{\mathrm{open}}) = \Psi_N + \sigma_{\mathrm{flip}} + \sigma_{\mathrm{end}} \in \{\Psi_N, \Psi_N + 1, \Psi_N + 2\}$ whenever $\Psi_N \ge 1$ (where $\sigma_{\mathrm{flip}} = \mathbf{1}[\delta_1 = -\operatorname{sgn}(X_{b_1})]$, $b_1 = \min\{i \ge 1 : |X_i| > J/2\}$, and $\sigma_{\mathrm{end}} = \mathbf{1}[g_{\Psi_N} < N \text{ and } \operatorname{sgn}(D_N) = -s_{\mathrm{last}}]$), and $\#\mathrm{domains}(\sigma^\ast_{\mathrm{open}}) = 1 + \mathbf{1}[M_N = 1 \text{ and } \operatorname{sgn}(D_N) = -s_1] \in \{1, 2\}$ when $\Psi_N = 0$.
- Status: proved
- Review: self
- Evidence: Complete proof in Section `Derivations` (Theorem 2) of this record; verified with 0 mismatches against exhaustive $2^N$ search (3,000 instances) and Viterbi DP (1,000 chains at $N=400, J=4.0$), plus 3 negative controls (`wrong_clip_J`: 479/1000 fail, `drop_flip`: 262/1000 fail, `drop_end`: 231/1000 fail) in `conj_coh_walls-checks/verify_coh_walls.py` and `conj_coh_walls-checks/verify_coh_walls_output.txt`.
- Depends on: none

### C4: Sharp two-sided Gaussian drawdown bound and exact almost-sure limit in `thm:coh-domains-1d`(b) (Theorem 3)

- Statement: For a random walk with i.i.d. $\mathcal{N}(0, h^2)$ steps ($h > 0$), $B_u = \max_{u'\le u} X_{u'} - X_u$, and $T_J = \min\{u : B_u \ge J\}$, one has $(J/h)^2 \le \mathbb{E} T_J \le (J/h)^2 + \frac{\pi + 4}{\sqrt{2\pi}}(J/h) + 2$. Consequently, in `thm:coh-domains-1d`(b), the mean domain length $\bar\ell_N$ satisfies $\lim_{N\to\infty}\bar\ell_N = \mathbb{E} T_J \in [(J/h)^2, (J/h)^2 + \frac{\pi + 4}{\sqrt{2\pi}}(J/h) + 2]$ almost surely on both the ring and the open chain.
- Status: proved
- Review: self
- Evidence: Complete proof in Section `Derivations` (Theorem 3) of this record via the submartingale $(B_u + \sqrt{\pi/8}\,h)^2 - u h^2$ and exact Gaussian overshoot bounds $\mathbb{E}[Z - a \mid Z \ge a] < \sqrt{2/\pi}$, $\mathbb{E}[(Z - a)^2 \mid Z \ge a] = 1 - a\mu_1(a) < 1$; checked against exact Gauss–Legendre Fredholm integral equation for $J/h \in \{0.5, 1, 2, 5, 10, 20\}$ (relative quadrature error $< 10^{-11}$), independent 20k-sample Monte Carlo at $J/h=2$ ($9.9710 \pm 0.0568$ vs. $10.003527$, $z = -0.57$), and a negative control at $\alpha = 0.9\sqrt{\pi/8}$ (drift $0.95 < 1$) in `conj_coh_walls-checks/verify_coh_walls.py` and `conj_coh_walls-checks/verify_coh_walls_output.txt`.
- Depends on: C2

## Failed routes

### R1: Direct boundary-only repair of `conj:coh-walls` to $\{\Psi_N, \Psi_N + 1\}$ for large $N$

- Tried: Checked whether $\#\mathrm{domains}(\sigma^\ast_{\mathrm{open}}) = \Psi_N + 2$ was solely a small-$N$ / $\Psi_N = 0$ artifact that disappears once $\Psi_N \ge 1$ or $N$ is large.
- Failed because: By C3, $\sigma_{\mathrm{flip}}$ depends only on the initial excursion near $i = 0$ and $\sigma_{\mathrm{end}}$ depends only on the terminal reflected position near $i = N$, so they become asymptotically independent as $N \to \infty$ with strictly positive joint probability $\approx 0.25 \times 0.25 \approx 6\%$ ($72/1000$ at $N=400, J=4.0$).
- Reopen if: Open-chain boundary fields are clamped or modified (e.g., pinned boundary spins $\sigma_0 = \sigma_{N+1}$), which changes the potential $\Phi_{\mathrm{code}}$.

## Open obligations

- [ ] O1 (sessions: 1): Run a fresh-context proof reconstruction (`research-proof-checker`) on C1–C4 before patching `06_coherence.tex` and `app06_coherence.tex`.
- [ ] O2 (sessions: 1): Check 1D zero-temperature RFIM domain-wall literature and Gaussian drawdown/Spitzer–Siegmund overshoot literature before making any novelty claim or adding citations.

## Literature

| Claim | Source | Locator | Read depth | Date read | Verdict |
| --- | --- | --- | --- | --- | --- |
| Main-text theorem | `Collective_Agents/sections/06_coherence.tex` | `thm:coh-domains-1d` (lines 163–171) | full theorem | 2026-11-21 | exact statement and factor-of-52 bounds matched |
| Lemmas and conjecture | `Collective_Agents/sections/app06_coherence.tex` | `lem:coh-structure`, `lem:coh-counting`, `lem:coh-drawdown`, `conj:coh-walls` (lines 173–223) | full proof section | 2026-11-21 | exact definitions of greedy $J$-hysteresis and `lem:coh-structure` verified |
| Numerical table | `Collective_Agents/sections/chk06_coherence.tex` | `chk:coh-domains` (lines 58–70) | full check | 2026-11-21 | empirical means $4.71, 9.98, 26.75, 83.40, 306.5$ consistent with exact Fredholm $\mathbb{E} T_J$ |

## Searches

| Query | Tool | Date | Not searched |
| --- | --- | --- | --- |
| none yet | — | 2026-11-21 | External literature on 1D zero-temperature RFIM domain counting and Spitzer–Siegmund drawdown asymptotics |

## Log

- 2026-11-21: Opened record from user request ("find another problem to solve/research"; "Write up a .MD and continue"). Refuted literal `conj:coh-walls` (C1), proved exact deterministic wall bounds $\Psi_N - 1 \le \#\mathrm{walls}(\sigma^\ast) \le \Psi_N + 1$ with exact even-$\Psi_N$ ring equality (C2), proved exact Viterbi open-chain domain identity $\Psi_N + \sigma_{\mathrm{flip}} + \sigma_{\mathrm{end}}$ (C3), and proved the sharp drawdown upper bound $(J/h)^2 + \frac{\pi+4}{\sqrt{2\pi}}(J/h) + 2$ closing the factor-of-52 gap in `thm:coh-domains-1d`(b) to an exact almost-sure limit $\mathbb{E} T_J$ (C4). Reporting gate: (1) settles `conj:coh-walls` and upgrades `lem:coh-counting`, `lem:coh-drawdown`, and `thm:coh-domains-1d`(b); (2) avoids silently fixing `conj:coh-walls` without flagging that its literal two-value claim is false; (3) strongest referee objections (tie-handling in upper/lower bounds, uniform integrability in optional stopping, Mills-ratio monotonicity without external theorems) discharged directly in `Derivations`; (4) review state is `self` only and no literature search was run; (5) obligations O1–O2 recorded. Next action: fresh-context verification (O1) and literature check (O2) prior to editing `06_coherence.tex` and `app06_coherence.tex`.

---

## Derivations

### Proof of Theorem 1 (C2)

**Part (1) — Alternating-Jump Lemma and upper bound.**
We first prove: *if $1 \le x_1 < x_2 < \dots < x_L \le N$ ($L \ge 2$) and alternating signs $\sigma_2, \dots, \sigma_L \in \{+1, -1\}$ ($\sigma_{\alpha+1} = -\sigma_\alpha$) satisfy $\sigma_\alpha(X_{x_\alpha} - X_{x_{\alpha-1}}) \ge J$ for $\alpha = 2, \dots, L$, then $\Psi_N \ge L - 1$.*

We prove by induction on $\alpha \in \{2, \dots, L\}$ the stronger claim:
$$(\star_\alpha) \qquad \text{either } c(x_\alpha) \ge \alpha, \quad \text{or } \bigl(c(x_\alpha) = \alpha - 1 \;\text{ and }\; \delta(x_\alpha) = \sigma_\alpha\bigr),$$
where $c(t) = |\{k : g_k \le t\}|$ and $\delta(t) = \delta_{c(t)}$ for $c(t) \ge 1$.

*Base case $\alpha = 2$:* By symmetry $X \leftrightarrow -X$, assume $\sigma_2 = +1$, so $X_{x_2} - X_{x_1} \ge J$. Then $\max_{[0, x_2]} X - \min_{[0, x_2]} X \ge J$, so $c(x_2) \ge 1$. Suppose for contradiction that $c(x_2) = 1$ and $\delta_1 = -1$ (a single DOWN switch at $g_1 \le x_2$).
- If $g_1 \le x_1$, after $g_1$ greedy hysteresis tracks $\min_{[g_1, i]} X \le X_{x_1}$; at $i = x_2$, $X_{x_2} - \min_{[g_1, x_2]} X \ge X_{x_2} - X_{x_1} \ge J$, forcing a second switch in $(x_1, x_2]$, contradicting $c(x_2) = 1$.
- If $x_1 < g_1 \le x_2$, let $u \in [0, g_1 - 1]$ attain $\max_{[0, g_1 - 1]} X$, so $X_u - X_{g_1} \ge J$. Because $g_1$ is the first switch, the range of $X$ on $[0, g_1 - 1]$ is strictly less than $J$; since $u, x_1 \in [0, g_1 - 1]$, $X_u - X_{x_1} < J$. Combining these gives
  $$X_{x_2} - X_{g_1} = (X_{x_2} - X_{x_1}) + (X_u - X_{g_1}) - (X_u - X_{x_1}) > J + J - J = J.$$
  Hence $g_1 < x_2$ and $X_{x_2} - \min_{[g_1, x_2]} X \ge X_{x_2} - X_{g_1} > J$, forcing a second switch in $(g_1, x_2]$, contradicting $c(x_2) = 1$.
This establishes $(\star_2)$.

*Inductive step $\alpha \to \alpha + 1$:* Assume $(\star_\alpha)$ holds, and by symmetry suppose $\sigma_\alpha = +1$, $\sigma_{\alpha+1} = -1$, so $X_{x_{\alpha+1}} - X_{x_\alpha} \le -J$.
- If $c(x_\alpha) \ge \alpha + 1$, then $c(x_{\alpha+1}) \ge \alpha + 1$.
- If $c(x_\alpha) = \alpha$ and $\delta(x_\alpha) = -1 = \sigma_{\alpha+1}$, then either $c(x_{\alpha+1}) \ge \alpha + 1$, or $c(x_{\alpha+1}) = \alpha$ with $\delta(x_{\alpha+1}) = \delta(x_\alpha) = \sigma_{\alpha+1}$.
- If $c(x_\alpha) = \alpha$ and $\delta(x_\alpha) = +1$, the phase at $x_\alpha$ tracks the running maximum $\ge X_{x_\alpha}$; since $X_{x_{\alpha+1}} \le X_{x_\alpha} - J$, a new switch occurs in $(x_\alpha, x_{\alpha+1}]$, giving $c(x_{\alpha+1}) \ge \alpha + 1$.
- If $c(x_\alpha) = \alpha - 1$ and $\delta(x_\alpha) = +1$, the phase at $x_\alpha$ tracks the running maximum $\ge X_{x_\alpha}$, so $X_{x_{\alpha+1}} \le X_{x_\alpha} - J$ forces at least one switch in $(x_\alpha, x_{\alpha+1}]$; thus $c(x_{\alpha+1}) \ge \alpha$, and if $c(x_{\alpha+1}) = \alpha$ its last switch is that single new switch, of direction $-\delta(x_\alpha) = -1 = \sigma_{\alpha+1}$.
This proves $(\star_{\alpha+1})$. At $\alpha = L$, $\Psi_N = c(N) \ge c(x_L) \ge L - 1$.

Now let $L = \#\mathrm{walls}(\sigma^\ast)$. If $L \le 1$, then $L \le \Psi_N + 1$ trivially. If $L \ge 2$, list the wall indices in increasing order $1 \le x_1 < \dots < x_L \le N$ ($x_L \le N - 1$ on the open chain; $x_L = N$ denotes the edge $(N, 1)$ on the ring). For each $\alpha = 2, \dots, L$, the run $\{x_{\alpha-1}+1, \dots, x_\alpha\}$ is a domain of $\sigma^\ast$ with walls on both sides (strictly smaller than the ring since $L \ge 2 \implies x_1 < x_L$), so `lem:coh-structure`(a) gives $\sigma_\alpha(X_{x_\alpha} - X_{x_{\alpha-1}}) \ge J$ with alternating signs $\sigma_\alpha$. The Alternating-Jump Lemma gives $\Psi_N \ge L - 1$, i.e., $L \le \Psi_N + 1$.

**Part (2) — Lower bound.**
If $\Psi_N \le 1$, then $\#\mathrm{walls}(\sigma^\ast) \ge 0 \ge \Psi_N - 1$ trivially. Assume $\Psi_N \ge 2$ and no run of consecutive pulls sums to $\pm J$. Put $g_0 := 0$. For each $k = 1, \dots, \Psi_N$, let $p_k \in [g_{k-1}, g_k)$ attain the running extreme reversed at $g_k$. Then $\delta_k(X_{g_k} - X_{p_k}) > J$ (strictly, by the no-tie hypothesis, and $p_k < g_k$ since $J > 0$). By `lem:coh-structure`(c), no $(-\delta_k)$-domain contains a run whose aligned sum is $< -J$; hence $\{p_k + 1, \dots, g_k\} \subseteq \{g_{k-1} + 1, \dots, g_k\}$ contains at least one site $u_k$ with $\sigma^\ast(u_k) = \delta_k$. Thus $1 \le u_1 < u_2 < \dots < u_{\Psi_N} \le N$ have strictly alternating spins $\sigma^\ast(u_k) = \delta_k = (-1)^{k-1}\delta_1$, forcing at least one wall in each of the $\Psi_N - 1$ disjoint intervals $[u_k, u_{k+1})$, so $\#\mathrm{walls}(\sigma^\ast) \ge \Psi_N - 1$.

**Part (3) — Ring parity.**
On a ring, every configuration has an even number of walls. Between $\Psi_N - 1$ and $\Psi_N + 1$, the unique even integer when $\Psi_N$ is even is $\Psi_N$; when $\Psi_N$ is odd, the even integers are $\Psi_N - 1$ and $\Psi_N + 1$. $\square$

---

### Proof of Theorem 2 (C3)

From the Viterbi recursions $V_+(i+1) = \min(V_+(i), V_-(i) + J) - h_{i+1}$ and $V_-(i+1) = \min(V_-(i), V_+(i) + J) + h_{i+1}$, subtracting and dividing by $2$ gives $D_{i+1} = \operatorname{clip}(D_i, -J/2, J/2) + h_{i+1}$ with $D_0 = 0$. For $1 \le i \le N - 1$: when $|D_i| < J/2$, both predecessor edges into $i+1$ are parallel (no wall); when $|D_i| > J/2$, both states at $i+1$ take $(i, \operatorname{sgn}(D_i))$ as their unique optimal predecessor, forcing $\sigma^\ast_i = \operatorname{sgn}(D_i)$ and placing a wall on $(i, i+1)$ iff the optimal path continues to $-\operatorname{sgn}(D_i)$. Tracing backward from $\sigma^\ast_N = \operatorname{sgn}(D_N)$ places exactly $M_N - 1$ walls between consecutive alternating barrier blocks (for $M_N \ge 1$) plus one final wall iff $\operatorname{sgn}(D_N) = -s_{\mathrm{last}}$, yielding $\#\mathrm{domains}(\sigma^\ast_{\mathrm{open}}) = 1$ if $M_N = 0$ and $M_N + \mathbf{1}[\operatorname{sgn}(D_N) = -s_{\mathrm{last}}]$ if $M_N \ge 1$.

Before $b_1 := \min\{i \ge 1 : |X_i| > J/2\}$, no clipping occurs, so $D_i = X_i$ for $0 \le i \le b_1$. After any hit of $+J/2$ at $t_0$, induction gives $\operatorname{clip}(D_i, -J/2, J/2) = J/2 - (\max_{t_0 \le u \le i} X_u - X_i)$ until $D_i < -J/2$, which occurs precisely when $\max_{t_0 \le u \le i} X_u - X_i > J$ (and symmetrically after $-J/2$).
- If $\Psi_N = 0$, the range of $X$ on $[0, N]$ is $< J$, so after $b_1$ (if $b_1 \le N - 1$) $D$ cannot hit the opposite barrier; hence $M_N \le 1$ and $\#\mathrm{domains}(\sigma^\ast_{\mathrm{open}}) = 1 + \mathbf{1}[M_N = 1 \text{ and } \operatorname{sgn}(D_N) = -s_1] \in \{1, 2\}$.
- If $\Psi_N \ge 1$, assume $X_{b_1} > J/2$ by symmetry:
  - When $\delta_1 = +1$ ($\sigma_{\mathrm{flip}} = 0$), $X$ attains a new running maximum at $g_1$ without dropping by $J$ on $[b_1, g_1]$, so $D$ does not hit $-J/2$ on $[b_1, g_1]$ and satisfies $\operatorname{clip}(D_{g_1}, -J/2, J/2) = +J/2$. From $g_1$ onward the alternating barrier hits of $D$ on $[g_1 + 1, N]$ coincide with $g_2, \dots, g_{\Psi_N}$. Counting hits in $\{1, \dots, N-1\}$ gives $M_N = \Psi_N$ if $g_{\Psi_N} < N$ and $M_N = \Psi_N - 1$ (with $\operatorname{sgn}(D_N) = -s_{\mathrm{last}}$ when $M_N \ge 1$, or $M_N = 0$ if $\Psi_N = 1, g_1 = N$) if $g_{\Psi_N} = N$; in every case $\#\mathrm{domains}(\sigma^\ast_{\mathrm{open}}) = \Psi_N + \sigma_{\mathrm{end}}$.
  - When $\delta_1 = -1$ ($\sigma_{\mathrm{flip}} = 1$), since $|X_u| < J/2 < X_{b_1}$ for $u < b_1$, $\max_{0 \le u \le i} X_u = \max_{b_1 \le u \le i} X_u$ for $i \ge b_1$, so $g_1$ is the exact second alternating barrier hit of $D$ (hitting $-J/2$, with $b_1 < g_1$). Thereafter the alternating hits coincide with $g_2, \dots, g_{\Psi_N}$, giving $M_N = \Psi_N + 1$ if $g_{\Psi_N} < N$ and $M_N = \Psi_N$ (with $\operatorname{sgn}(D_N) = -s_{\mathrm{last}}$) if $g_{\Psi_N} = N$; in both cases $\#\mathrm{domains}(\sigma^\ast_{\mathrm{open}}) = \Psi_N + 1 + \sigma_{\mathrm{end}}$. $\square$

---

### Proof of Theorem 3 (C4)

By scaling $B_u / h$, take $h = 1$ and write $r := J/h > 0$, $B_{u+1} = (B_u - Z_{u+1})_+$ with $Z_{u+1} \sim \mathcal{N}(0, 1)$. The lower bound $\mathbb{E} T_J \ge r^2$ and finiteness $\mathbb{E} T_J < \infty$ are given by `lem:coh-drawdown`.

**Step 1 (Submartingale at $\alpha = \sqrt{\pi/8}$).**
Using $(b - Z)_+ = (b - Z) + (Z - b)_+$, direct expansion yields
$$\bigl((b - Z)_+ + \alpha\bigr)^2 - (b + \alpha)^2 = -2(b + \alpha) Z + Z^2 + 2\alpha(Z - b)_+ - (Z - b)_+^2.$$
Taking expectation over $Z \sim \mathcal{N}(0, 1)$ gives $\Delta_\alpha(b) := \mathbb{E}[((b - Z)_+ + \alpha)^2] - (b + \alpha)^2 = 1 + 2\alpha g_1(b) - g_2(b)$, where $g_1(b) = \mathbb{E}[(Z - b)_+] = \varphi(b) - b\bar\Phi(b)$ and $g_2(b) = \mathbb{E}[(Z - b)_+^2] = (1 + b^2)\bar\Phi(b) - b\varphi(b)$. Put $2\alpha = \sqrt{\pi/2}$ ($\alpha = \sqrt{\pi/8}$) and $H(b) := \sqrt{\pi/2}\,g_1(b) - g_2(b)$. Then $H(0) = \sqrt{\pi/2}(2\pi)^{-1/2} - \tfrac{1}{2} = 0$, $H(\infty) = 0$, $H'(b) = -\sqrt{\pi/2}\,\bar\Phi(b) + 2g_1(b)$ with $H'(0) = (4 - \pi)/(2\sqrt{2\pi}) > 0$, and $H''(b) = \varphi(b)[\sqrt{\pi/2} - 2m(b)]$, where Mills' ratio $m(b) := \bar\Phi(b)/\varphi(b)$ is strictly decreasing on $[0, \infty)$ ($m'(b) = bm(b) - 1 < 0$ since $\bar\Phi(b) < b^{-1}\varphi(b)$ for $b > 0$) from $m(0) = \sqrt{\pi/2}$ to $0$. Hence $H''$ changes sign once on $(0, \infty)$ (from $-$ to $+$), so $H'$ changes sign at most once (from $+$ to $-$); since $H(0) = H(\infty) = 0$ and $H'(0) > 0$, $H(b) \ge 0$ for all $b \ge 0$. Thus $\Delta_\alpha(b) \ge 1$ for all $b \ge 0$, and $M_u := (B_u + \alpha)^2 - u$ is a submartingale.

**Step 2 (Gaussian overshoot bounds).**
For any $a > 0$, let $O(a)$ have the law of $(Z - a) \mid (Z \ge a)$, with mean $\mu_1(a) = r(a) - a > 0$ where $r(a) = \varphi(a)/\bar\Phi(a) = 1/m(a)$. Direct integration gives
$$\mathbb{E}[O(a)^2] = \frac{(1 + a^2)\bar\Phi(a) - a\varphi(a)}{\bar\Phi(a)} = 1 - a\mu_1(a) < 1.$$
Since $r'(a) = r(a)(r(a) - a) = \mu_1(a)^2 + a\mu_1(a)$,
$$\mu_1'(a) = r'(a) - 1 = -\bigl(1 - a\mu_1(a) - \mu_1(a)^2\bigr) = -\operatorname{Var}(O(a)) < 0 \qquad (a \ge 0),$$
so $\mu_1(a) < \mu_1(0) = \sqrt{2/\pi}$ for all $a > 0$.

**Step 3 (Optional stopping and almost-sure limit).**
On $\{T_J = u\} = \{T_J > u - 1\} \cap \{Z_u \ge r - B_{u-1}\}$, $Z_u$ is independent of $\mathcal{F}_{u-1}$ and $a := r - B_{u-1} > 0$, so Step 2 yields
$$\mathbb{E}\bigl[(B_{T_J} + \alpha)^2 - \alpha^2 \mid \mathcal{F}_{u-1}, T_J = u\bigr] = r^2 + 2r(\alpha + \mu_1(a)) + \mathbb{E}[O(a)^2] + 2\alpha\mu_1(a) < r^2 + \frac{\pi + 4}{\sqrt{2\pi}}\,r + 2,$$
using $2(\sqrt{\pi/8} + \sqrt{2/\pi}) = (\pi + 4)/\sqrt{2\pi}$ and $1 + 2\sqrt{\pi/8}\sqrt{2/\pi} = 2$. Summing over $u \ge 1$ gives $\mathbb{E}[(B_{T_J} + \alpha)^2] - \alpha^2 \le r^2 + \frac{\pi + 4}{\sqrt{2\pi}} r + 2 < \infty$. Optional stopping on $M_{T_J \wedge n}$ yields
$$\mathbb{E}[T_J \wedge n] \le \mathbb{E}\bigl[(B_{T_J \wedge n} + \alpha)^2\bigr] - \alpha^2 \le \mathbb{E}\bigl[(B_{T_J} + \alpha)^2\mathbf{1}[T_J \le n]\bigr] + (r + \alpha)^2\Pr(T_J > n) - \alpha^2.$$
Letting $n \to \infty$ (monotone convergence on the left, dominated convergence and $\Pr(T_J > n) \to 0$ on the right) gives the upper bound on $\mathbb{E} T_J$.

Finally, by Theorem 1, with probability one (no run sums to $\pm J$) the number of domains $K_N$ satisfies $\Psi_N - 1 \le K_N \le \Psi_N + 2$ on both the ring and the open chain. Since $\Psi_N / N \to 1/\mathbb{E} T_J > 0$ almost surely by the renewal strong law of large numbers (as in `app06_coherence.tex`, proof of `thm:coh-domains-1d`(b)), $\bar\ell_N = N/K_N \to \mathbb{E} T_J$ almost surely. $\square$
