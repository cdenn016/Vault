# Uniform Agency Bound (`open:agy-uniform-bound`)

- Status: active
- Opened: 2026-11-22
- Updated: 2026-11-22
- Sessions: 1

## Target

- Source: `Collective_Agents/sections/s05_agency.tex` (`open:agy-uniform-bound`, lines 70–75; `prop:agy-dispersion`, lines 77–83; `prop:agy-index`, lines 88–99), `Collective_Agents/sections/05_agency.tex` (`def:agy-group-model`, lines 156–176; `lem:agy-decomposition`, lines 178–184; `thm:agy-agency`, lines 189–205; `thm:agy-heterogeneous`, lines 214–236; `def:agy-agency-index`, lines 240–249), `Collective_Agents/sections/app05_agency.tex` (proofs of `lem:agy-decomposition`, `thm:agy-agency`, `thm:agy-heterogeneous`, lines 105–175), and `Collective_Agents/sections/chk05_agency.tex` (`chk:agy-heterogeneous`, `chk:agy-index`, lines 41–47).
- Locked statement: Settle `open:agy-uniform-bound` (`s05_agency.tex`, lines 72–74): *"Find a bound on the distance between the deliberation law and a group posterior that is uniform in $\gamma$ and polynomial in the number of members for weak redundancy disagreement, or a family showing that the factor $|\mathcal{A}|-1$ of the tree bound is needed for perturbations without a potential part."*
- Falsifier: Either (i) an explicit family of heterogeneous-belief deliberation models under `(P1)`–`(P4)` with pure non-potential (exact Hodge-harmonic, $\delta^\ast\mathcal{R}\equiv 0$) weak redundancy disagreement $\sigma_{\max}$ showing that no bound uniform in $\gamma$ exists and that an exponential-in-$n$ factor multiplying $\gamma\sigma_{\max}$ is required (refuting the uniform/polynomial bound), or (ii) a proof of a bound on $\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_C)$ uniform in $\gamma$ and polynomial in $n$ for all perturbations without a potential part (refuting exponential necessity).
- May assume: `(P1)`–`(P4)` of `def:agy-group-model`, `lem:agy-decomposition`, `thm:agy-agency`, `thm:agy-heterogeneous` (in particular the tree bound of part (a)), and the Markov chain tree theorem (Anantharam & Tsoucas 1989, as cited in `app05_agency.tex` line 164).
- Must not assume: Any bound uniform in $\gamma$ or polynomial in $n$; any non-epistemic / performative interaction terms; any violation of conditional independence of slots given $\eta_C$; any potential-only perturbation (where members agree with one another and only disagree with $q_C$, already ruled out in `s05_agency.tex` line 70).
- Alternative forms:
  - Reading 1 (Class 1 — `thm:agy-heterogeneous` reference law): Distance $\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_\Phi)$ (or $\inf_{q_C}\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_\Phi(q_C))$, and $\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_{\Phi_{\mathrm{Hodge}}})$ to the exact Hodge potential projection) and log-ratio $\max_\pi |\ln(\mathbb{P}^\infty(\pi)/\mathbb{P}_\Phi(\pi))|$.
  - Reading 2 (Class 2 — `prop:agy-index`(c) fixed-slot-model group posteriors): Distance $\inf_{\mathbb{P}_C \in \mathfrak{G}_{\mathrm{fixed}}} \mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_C)$ over all group posteriors $\mathbb{P}_C(\pi) \propto (\prod_u \tilde{E}_u(\pi_u)) e^{-\gamma_C G_C(\pi)}$ on the collective's slot model $\mathfrak{B}$ with arbitrary full-support product habits $\tilde{E}_u$, arbitrary precision $\gamma_C \ge 0$, and arbitrary independent-block belief $q_C$ (or arbitrary correlated belief $q_C$ with bounded $\gamma_C \sigma_{\max}(q_C)$).
- Test instance: $n = 2$ binary linear-Gaussian double-well ($I_C = 0.5, \delta = 0.01, h = 0.4, \varepsilon = 0.015$, $\gamma = 100$): $\mathbb{P}^\infty(0,1) = 0.62243033$, $\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_\Phi) = 0.44002105$, $\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_{\Phi_{\mathrm{Hodge}}}) = 0.24490725$; and $m = 2$ ($n = 7$, $|\mathcal{A}| = 128$) binary linear-Gaussian gear train ($I_{\mathrm{adj}} = 1, I_{\mathrm{wall}} = 5, h = 0.9, \Delta = 0.1, b = 0.01, \lambda = 4.0, \gamma = 120$): uniform-cost $\ln\frac{\mathbb{P}^\infty(v_L)/\mathbb{P}_\Phi(v_L)}{\mathbb{P}^\infty(v_0)/\mathbb{P}_\Phi(v_0)} = 8.000000 = 2^{m+1}\gamma\sigma_{\max}$ and $\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_\Phi) = 0.695298$.
- Out of scope: Performative acts (`def:agy-joint-acts`), synchronous deliberation (`prop:agy-synchronous-exact`), and unrestricted Class 3 models where the approximating group posterior may invent arbitrary new slots unrelated to the collective's actual slot model $\mathfrak{B}$ (discussed transparently in Open Obligations).
- Reading chosen: Both Reading 1 (Class 1) and Reading 2 (Class 2) are addressed directly and rigorously, with the strongest Notion of "without a potential part": exact Candogan–Ozdaglar–Parrilo Hodge harmonicity $(\delta^\ast\mathcal{R})(\pi) \equiv 0$ at every profile $\pi \in \{0,1\}^n$ (zero potential component in $\ell^2(E(Q_n))$), realized by explicit linear-Gaussian slot models with $\dim \eta_C = O(n)$ and only 4 heterogeneous members.

## Verdict Summary

**Negative answer to the uniform/polynomial bound; explicit exponential-in-$n$ linear-Gaussian counterexample family constructed and proved.**

1. **No bound uniform in $\gamma$ exists**, even for perturbations without a potential part and arbitrarily small fixed $\sigma_{\max} > 0$:
   - At $n = 2$ (1 scalar Gaussian coordinate), $\lim_{\gamma\to\infty} \inf_{q_C}\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_\Phi(q_C)) = 1$ and $\lim_{\gamma\to\infty}\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_{\Phi_{\mathrm{Hodge}}}) = 1$ (`C1`).
   - At $m = 2$ ($n = 7$ binary members, exact Hodge-harmonic $\delta^\ast\mathcal{R}\equiv 0$), even minimizing over **all** Class 2 group posteriors (arbitrary independent-block belief $q_C$, arbitrary precision $\gamma_C \ge 0$, arbitrary full-support product habits $\tilde{E}_u$), $\lim_{\gamma\to\infty} \inf \mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_C) \ge \sqrt{2} - 1 \approx 0.414214$ (`C4`).
2. **No bound polynomial (or sub-exponential) in $n$ exists**, even as a function of $(n, \gamma\sigma_{\max})$ and even for exact Hodge-harmonic ($\delta^\ast\mathcal{R}\equiv 0$) linear-Gaussian perturbations with only 4 heterogeneous members ($\sum_u \sigma_u = 4\sigma_{\max}$) and $\dim\eta_C = O(n)$:
   - The $m$-gear linear-Gaussian family ($n = 8m - 9$ binary members, $|\mathcal{A}| = 2^n$, $m \ge 2$) amplifies $\gamma\sigma_{\max}$ by **$2^{m+1} = 2\cdot 2^{(n+9)/8} = \Theta(|\mathcal{A}|^{1/8})$**: along the scaling $\gamma\sigma_{\max} = \lambda \cdot 2^{-m}$ (exponentially small in $n$), $\max_\pi |\ln(\mathbb{P}^\infty/\mathbb{P}_\Phi)| \ge \lambda = 2^m\gamma\sigma_{\max}$, $\inf_{q_C \in \mathcal{Q}_{\mathrm{diag}}} \mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_\Phi) \to 1 - \frac{m-1}{3\cdot 2^m - 5}$ as $\lambda \to \infty$ (`C3`), and $\inf_{\mathbb{P}_C \in \mathfrak{G}_{\mathrm{diag}}} \mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_C) \ge 2\sqrt{p_\lambda} - 1 \to \sqrt{2}-1$ (with an explicit trade-off bound $R(2\sqrt{p_\lambda}-R)$ for arbitrarily correlated $q_C$, `C4`).
3. **Statement comparison with `open:agy-uniform-bound`**: The first alternative (a bound uniform in $\gamma$ and polynomial in $n$) is **completely refuted** for both Class 1 and Class 2. For the second alternative, we prove an explicit exponential factor $\Omega(2^{n/8}) = \Omega(|\mathcal{A}|^{1/8})$ is needed for exact Hodge-harmonic linear-Gaussian perturbations; narrowing the optimal exponent $\theta^\ast \in [1/8, 1]$ in $|\mathcal{A}|^{\theta^\ast}\gamma\sigma_{\max}$ (between our $|\mathcal{A}|^{1/8}$ lower bound and the tree upper bound $|\mathcal{A}| - 1$) remains a fine open refinement (`O1`), as does Class 3 with invented slot models (`O2`).

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| Mutual information units | Natural logarithm $\ln$ (nats) | $I(o_1; o_2) = \frac{1}{2}\ln\frac{(1+v)^2}{1+2v}$; at $v=1$, $\frac{1}{2}\ln(4/3) = 0.143841036225890$ |
| Gaussian variance inverse $v(I)$ | $v(I) = (e^{2I}-1) + \sqrt{e^{2I}(e^{2I}-1)}$ for $I > 0$ | $v(\frac{1}{2}\ln(4/3)) = 1.000000000000000$ |
| Total variation distance | $\mathrm{TV}(P, Q) = \frac{1}{2}\sum_{\pi\in\mathcal{A}} |P(\pi) - Q(\pi)| = \sum_{\pi} (P(\pi)-Q(\pi))_+$ | $\mathrm{TV}((0.8, 0.2), (0.3, 0.7)) = 0.500000000000000$ |
| Binary deliberation chain `(P4)` | $\mathsf{T}(\pi, \pi\oplus e_u) = \frac{1}{n}\frac{E_u(1-\pi_u)e^{-\gamma G_u(\pi\oplus e_u)}}{E_u(0)e^{-\gamma G_u(\pi^{(u\leftarrow 0)})} + E_u(1)e^{-\gamma G_u(\pi^{(u\leftarrow 1)})}}$ | Uniform $E_u$, $\Delta G_u = 0 \implies \mathsf{T}(\pi,\pi\oplus e_u) = \frac{1}{2n}$ |
| Decomposition `lem:agy-decomposition` | $G_u(\pi) = \Phi(\pi) + \mathcal{R}_u(\pi) + f_u(\pi_{-u})$, $\mathcal{R}_u(\pi) = [I_{q_u}-I_{q_C}](o_{\mathfrak{B}_u(\pi_u)}; o_{A_{-u}})$ | On $n=2$ test instance: residual $< 10^{-14}$ |
| Redundancy disagreement $\sigma_{\max}$ | $\sigma_u = \max_{\pi_{-u}} \operatorname{osc}_{\pi_u} \mathcal{R}_u(\pi_u, \pi_{-u})$, $\sigma_{\max} = \max_u \sigma_u$ | For $\mathcal{R}_u(\pi) = \delta\pi_u(\pi_{u+1}-\pi_{u-1})$ on gear 0: $\sigma_u = \delta$ ($u\le 3$), $0$ ($u\ge 4$) |
| Hodge divergence $\delta^\ast\mathcal{R}$ | $(\delta^\ast\mathcal{R})(\pi) = \sum_{u=1}^n [\mathcal{R}_u(\pi\oplus e_u) - \mathcal{R}_u(\pi)]$ on $Q_n = \{0,1\}^n$ | On 4-cycle motor $\mathcal{R}_u = \delta\pi_u(\pi_{u+1}-\pi_{u-1})$: $\delta^\ast\mathcal{R} \equiv 0$ identically |
| Multi-information $M_{q_C}$ | $M_{q_C}(\pi) = \sum_u \pi_u I_{q_C}(\eta_C; o_{\mathfrak{B}_u(1)}) - I_{q_C}(\eta_C; o_{\mathfrak{B}(\pi)}) \ge 0$ | $M_{q_C}(\pi) = 0$ on every profile with $\le 1$ active member |

## Claims

### C1: Minimal $n = 2$ Non-Uniformity in $\gamma$ Against $\inf_{q_C}\mathbb{P}_\Phi$ and $\mathbb{P}_{\Phi_{\mathrm{Hodge}}}$

- Statement: Let $n = 2$ with binary policy sets $\mathcal{A}_1 = \mathcal{A}_2 = \{0, 1\}$, scalar external state $\eta_C \in \mathbb{R}$, linear-Gaussian slots $o_i = \lambda(\eta_C + \nu_i)$ ($\nu_1, \nu_2 \sim \mathcal{N}(0,1)$ independent, $\lambda > 0$), uniform habits $E_1 = E_2 = (\frac{1}{2}, \frac{1}{2})$, and member beliefs $q_1 = \mathcal{N}(0, v(I_C + \delta))$, $q_2 = \mathcal{N}(0, v(I_C - \delta))$ with $I_C > 0$ and $0 < \delta < I_C$. Choose Gaussian slot preferences realizing own-policy costs $c_1 = -h - \varepsilon$ and $c_2 = -h$ with $\frac{1}{2}I_C < h < I_C - \delta$ and $\delta < \varepsilon < \min(2\delta, I_C - h + \delta)$. Under `(P1)`–`(P4)`, with midpoint belief $q_C^\ast = \mathcal{N}(0, v(I_C))$ we have $\sigma_{\max}(q_C^\ast) = \delta$, $\mathcal{R}_1 + \mathcal{R}_2 \equiv 0$, and as $\gamma \to \infty$ (with fixed arbitrarily small $\delta > 0$):
  1. $\mathbb{P}^\infty(0, 1) \to 1$ with $\mathbb{P}^\infty(0,1)/\mathbb{P}^\infty(1,0) \sim e^{\gamma(2\delta - \varepsilon)}$;
  2. for every declared belief $q_C$ on $\mathbb{R}$ (arbitrary, not restricted to Gaussian), $\mathbb{P}_\Phi(q_C)(0, 1) \to 0$, so $\lim_{\gamma\to\infty}\inf_{q_C}\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_\Phi(q_C)) = 1$;
  3. for the exact Candogan–Ozdaglar–Parrilo Hodge potential projection $\Phi_{\mathrm{Hodge}}(\pi) = \Phi(q_C^\ast)(\pi) + \frac{\delta}{2}(\pi_1 - \pi_2)$, $\mathbb{P}_{\Phi_{\mathrm{Hodge}}}(0, 1) \to 0$ and $\lim_{\gamma\to\infty}\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_{\Phi_{\mathrm{Hodge}}}) = 1$.
- Status: proved
- Review: self
- Evidence: Complete derivation in `## Derivations` (Proof of `C1`); two-channel check in `open_agy_uniform_bound-checks/verify_uniform_bound.py` and `open_agy_uniform_bound-checks/verify_uniform_bound_stdout.txt` (Section 1): at $I_C = 0.5, \delta = 0.01, h = 0.4, \varepsilon = 0.015$, Channel 1 (explicit linear-Gaussian slot model + dense LU) and Channel 2 (80-digit Decimal exact 4-spanning-tree formula) agree to $5.55\times 10^{-17}$ ($\gamma=1$) and $9.90\times 10^{-13}$ ($\gamma=100$), reaching $\mathbb{P}^\infty(0,1) = 0.99995460$, $\mathrm{TV}(\Phi) = 0.99995460$, $\mathrm{TV}(\Phi_{\mathrm{Hodge}}) = 0.99990920$ at $\gamma = 2000$; negative control $\varepsilon = 0.025 > 2\delta$ gives $\mathrm{TV}(\Phi) = 4.5398\times 10^{-5}$ at $\gamma = 2000$.
- Depends on: none

### C2: Explicit Pairwise Linear-Gaussian $m$-Gear Train — Induced 1D Path, Energy Landscape, and Exact Hodge Harmonicity

- Statement: For every integer $m \ge 2$, define the graph $G_m = (V_m, E_{\mathrm{adj}} \sqcup E_{\mathrm{wall}})$ on $n = 8m - 9$ binary members partitioned into $m$ gears: gear $0$ (4-cycle $V_0 = \{0,1,2,3\}$ with clockwise motor edges $u \to (u+1)\bmod 4$), gears $1, \dots, m-2$ (8-cycles $V_g$), and top gear $m-1$ (open 3-path $0-1-2$, $V_{m-1}$), with intra-gear non-adjacent pairs in $E_{\mathrm{wall}}$ and inter-gear escapement wall edges between gear $g$ and gear $g+1$ allowing $V_g$'s first half-arc on $r \in \{0, 4\}$, locking to $a_{\mathrm{hi}}$ on $r \in \{1, 5\}$, allowing the second half-arc on $r \in \{2, 6\}$, and locking to $a_{\mathrm{lo}}$ on $r \in \{3, 7\}$ (where $(a_{\mathrm{lo}}, a_{\mathrm{hi}}) = (0, 2)$ for $g = 0$ and $(1, 5)$ for $g \ge 1$). Associate one independent scalar Gaussian coordinate $\eta_e$ to each edge $e \in E_{\mathrm{adj}} \sqcup E_{\mathrm{wall}}$ ($\dim\eta_C = 14$ for $m=2$, $68m - 138 = O(n)$ for $m \ge 3$), unit-SNR scaled slots $o_{u,e} = \lambda(\eta_e + \nu_{u,e})$, base redundancies $I_{\mathrm{adj}} = 1$, $I_{\mathrm{wall}} = 5$, and motor beliefs $v_{u,e} = v(1+\delta)$ on $u$'s outgoing motor edge and $v(1-\delta)$ on $u$'s incoming motor edge ($0 < \delta < 1$), with $q_u = q_C^\ast$ for all $u \notin V_0$. Then:
  1. **(Exact Hodge harmonicity)** Under $q_C^\ast$, $\mathcal{R}_u(\pi) = \delta\pi_u(\pi_{(u+1)\bmod 4} - \pi_{(u-1)\bmod 4})$ for $u \in V_0$ and $\mathcal{R}_u \equiv 0$ for $u \notin V_0$, satisfying $\sigma_{\max}(q_C^\ast) = \delta$, $\sum_u \sigma_u = 4\delta$, $\sum_u \mathcal{R}_u(\pi) \equiv 0$, and $(\delta^\ast\mathcal{R})(\pi) \equiv 0$ identically at all $2^n$ profiles $\pi \in \{0,1\}^n$.
  2. **(Induced 1D path of exponential motor length)** Let $\mathcal{P}_m$ be the set of wall-free one-hot profiles (one active member per gear, no edge of $E_{\mathrm{wall}}$) and $\mathcal{B}_m$ the set of bridges $v_k \cup v_{k+1}$ between consecutive profiles in $\mathcal{P}_m$. The induced subgraph of the hypercube $Q_n$ on $V_0 = \mathcal{P}_m \cup \mathcal{B}_m$ is an unbranched 1D path $v_0 - u_0 - v_1 - \dots - u_{L-1} - v_L$ with $|\mathcal{P}_m| = 3\cdot 2^m - 5$ valid profiles, $L = 3\cdot 2^m - 6$ bridges, and every gear-0 step along $v_0 \to v_L$ clockwise with exact cumulative motor-step count $s(v_L) = 2^m$ (and exactly $m - 1$ profiles attaining $s(v) = 2^m$). The four checkpoint profiles $A, B, D, C \in \mathcal{P}_m$ with $g_{m-1} \in \{0, 2\}$ and $g_{m-2} \in \{a_{\mathrm{lo}}, a_{\mathrm{hi}}\}$ are unique in $\mathcal{P}_m$, share the identical active subset on gears $0, \dots, m-3$, and satisfy $(s(A), s(B), s(D), s(C)) = (0, 2^{m-1}, 2^{m-1}, 2^m)$.
  3. **(Energy landscape)** With uniform own-policy costs $c_u = -h$ ($h = 0.9$, $\Delta = 1 - h = 0.1$) and $E_0 = -mh$, $\Phi(\pi) = E_0$ iff $\pi \in \mathcal{P}_m$, $\Phi(\pi) = E_0 + \Delta$ iff $\pi \in \mathcal{B}_m$, and $\Phi(\pi) \ge E_0 + 2\Delta$ for all $\pi \in V_1 := \{0,1\}^n \setminus V_0$; every edge from $\mathcal{P}_m$ to $V_1$ increases $\Phi$ by at least $h$, and every edge from $\mathcal{B}_m$ to $V_1$ increases $\Phi$ by at least $\Delta$. With 4-checkpoint costs ($c_u$ lowered by $b = \Delta/10 = 0.01$ on the 4 checkpoint nodes of gears $m-2, m-1$, plus $+2^m\delta$ on $u_{m-1,2}$ with $2^m\delta < b/2$), $\Phi(A) = \Phi(B) = E_0 - 2b$, $\Phi(D) = \Phi(C) = E_0 - 2b + 2^m\delta$, every $\pi \in \mathcal{P}_m \setminus \{A, B, C, D\}$ has $\Phi(\pi) \ge E_0 - b$, every edge from $\mathcal{P}_m$ to $V_1$ increases $\Phi$ by at least $h - 2^m\delta$, every edge from $\mathcal{B}_m$ to $V_1$ increases $\Phi$ by at least $\Delta - b$, and at most $5$ profiles in $\mathcal{P}_m$ have a bridge neighbor turning on a $-b$-bonus node. All own-policy costs are realized by explicit normalized Gaussian slot-product preferences.
- Status: proved
- Review: self
- Evidence: Complete inductive proof in `## Derivations` (Proof of `C2`); verified in `open_agy_uniform_bound-checks/verify_uniform_bound.py` and `open_agy_uniform_bound-checks/verify_uniform_bound_stdout.txt` (Section 2): exact Hodge harmonicity $\max|\delta^\ast\mathcal{R}| = 0.0$ on all $16$ gear-0 states; exact path topology, $|\mathcal{P}_m| = 3\cdot 2^m - 5$, $s(v_L) = 2^m$, checkpoint steps $[0, 2^{m-1}, 2^{m-1}, 2^m]$, $n_{\mathrm{top}} = m-1$, and $\dim\eta_C$ confirmed for $m = 2, 3, 4, 5, 6$ ($n = 7, 15, 23, 31, 39$); exhaustive energy landscape verified over all $2^7 = 128$ states ($m=2$) and all $2^{15} = 32768$ states ($m=3$); negative control dropping 1 wall edge on $m = 2$ breaks 1D-path topology (`max_deg = 3`, 8 valid states).
- Depends on: none

### C3: Exponential-in-$n$ Blowup Against $\mathbb{P}_\Phi$ via Exact $C_{\mathrm{out}}$-Factorization of the Markov Chain Tree Theorem

- Statement: For every $m \ge 2$ ($n = 8m - 9$ binary members, $|\mathcal{A}| = 2^n$) and every $\lambda > 0$, consider the uniform-cost $m$-gear linear-Gaussian deliberation model of `C2` (exact Hodge-harmonic $\delta^\ast\mathcal{R} \equiv 0$, uniform habits $E_u = (\frac{1}{2}, \frac{1}{2})$) along the exponentially small coupling schedule $\sigma_{\max}(q_C^\ast) = \delta(\gamma) = \lambda / (2^m \gamma)$ (so $\gamma\sigma_{\max}(q_C^\ast) = \lambda\cdot 2^{-m} = \lambda\cdot 2^{-(n+9)/8}$ is held fixed as $\gamma \to \infty$). Then:
  1. For every $x \in \mathcal{P}_m$, the Markov chain tree weight $W(x) = \sum_{\tau\in\mathcal{T}(x)} w(\tau)$ factors as
     $$1 \le \frac{W(x)}{C_{\mathrm{out}}\, w(\tau_0^{\mathrm{path}}(x))} \le 1 + (2n)^{|V_0|}\exp\Bigl(-\gamma\bigl(\Delta - (6\cdot 2^m - 8)\delta(\gamma)\bigr)\Bigr),$$
     with $C_{\mathrm{out}} = \sum_{\tau_1 \in \mathcal{F}(V_1\to V_0)} w(\tau_1)$ independent of $x \in \mathcal{P}_m$, and $w(\tau_0^{\mathrm{path}}(v_b))/w(\tau_0^{\mathrm{path}}(v_a)) = \exp(2\lambda (s(v_b) - s(v_a))/2^m)$ identically.
  2. Consequently, $\lim_{\gamma\to\infty}\mathbb{P}^\infty(\mathcal{P}_m) = 1$ and $\lim_{\gamma\to\infty}\mathbb{P}^\infty = \mu_\lambda$ on $\mathcal{P}_m$, where $\mu_\lambda(v_k) \propto \exp(2\lambda s(v_k)/2^m)$.
  3. At the endpoints $v_0, v_L$,
     $$\lim_{\gamma\to\infty}\ln\frac{\mathbb{P}^\infty(v_L)/\mathbb{P}_\Phi(v_L)}{\mathbb{P}^\infty(v_0)/\mathbb{P}_\Phi(v_0)} = 2\lambda = 2^{m+1}\gamma\sigma_{\max}(q_C^\ast) = 2\cdot 2^{(n+9)/8}\gamma\sigma_{\max}(q_C^\ast),$$
     so $\lim_{\gamma\to\infty}\max_\pi |\ln(\mathbb{P}^\infty(\pi)/\mathbb{P}_\Phi(\pi))| \ge 2^{(n+9)/8}\gamma\sigma_{\max}(q_C^\ast)$. At $q_C = q_C^\ast$, $\lim_{\gamma\to\infty}\mathbb{P}_\Phi(q_C^\ast) = \mathrm{Unif}(\mathcal{P}_m)$ and $\lim_{\gamma\to\infty}\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_\Phi(q_C^\ast)) = \mathrm{TV}(\mu_\lambda, \mathrm{Unif}(\mathcal{P}_m))$; moreover, for **every** independent-block belief $q_C \in \mathcal{Q}_{\mathrm{diag}}$ (arbitrary diagonal variances $v_{C,e} \ge 0$), $\liminf_{\gamma\to\infty}\inf_{q_C\in\mathcal{Q}_{\mathrm{diag}}}\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_\Phi(q_C)) \ge \mu_\lambda(S_{\mathrm{top}}) - \frac{m-1}{3\cdot 2^m - 5} \to 1 - \frac{m-1}{3\cdot 2^m - 5} \ge \frac{6}{7}$ as $\lambda \to \infty$.
- Status: proved
- Review: self
- Evidence: Complete self-contained proof in `## Derivations` (Proof of `C3`); two-channel verification on the full $2^7 = 128$-state explicit linear-Gaussian $m=2$ chain in `open_agy_uniform_bound-checks/verify_uniform_bound.py` and `open_agy_uniform_bound-checks/verify_uniform_bound_stdout.txt` (Section 3a): Channel 1 (explicit LG model + dense LU) and Channel 2 (repeated matrix squaring $\mathsf{T}^{2^k}$) agree to $3.59\times 10^{-10}$–$9.92\times 10^{-10}$ at $\gamma = 120$ across $\lambda \in \{1, 2, 4\}$, reproducing $\ln\text{-ratio} = 2.000000, 4.000000, 8.000000$ and $\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_\Phi) = 0.237818, 0.456896, 0.695298$ to all 6 printed digits of the theoretical limit; negative control replacing harmonic $(+\delta,-\delta)$ by potential $(+\delta,+\delta)$ gives $\max|\delta^\ast\mathcal{R}| = 0.0800 \ne 0$, detailed-balance residual $2.34\times 10^{-17}$, and $\ln(\mathbb{P}^\infty(v_L)/\mathbb{P}^\infty(v_0)) = 3.26\times 10^{-11}$.
- Depends on: C2

### C4: Exponential-in-$n$ and Non-$\gamma$-Uniform Lower Bound Against All Class 2 Group Posteriors (Free Product Habits, Free Precision)

- Statement: For every $m \ge 2$ ($n = 8m - 9$ binary members, $|\mathcal{A}| = 2^n$) and every $\lambda > 0$, consider the 4-checkpoint $m$-gear linear-Gaussian model of `C2` ($b = \Delta/10 = 0.01$, tilt $+2^m\delta$ on $u_{m-1,2}$, exact Hodge-harmonic $\delta^\ast\mathcal{R} \equiv 0$, uniform habits $E_u = (\frac{1}{2}, \frac{1}{2})$) with $\sigma_{\max}(q_C^\ast) = \delta(\gamma) = \lambda/(2^m\gamma)$ as $\gamma \to \infty$. Then:
  1. $\lim_{\gamma\to\infty} \mathbb{P}^\infty = P_\lambda := \frac{1}{2(1+e^\lambda)}(\delta_A + e^\lambda\delta_B + e^\lambda\delta_C + \delta_D)$.
  2. For every Class 2 group posterior $\mathbb{P}_C(\pi) \propto (\prod_{u=1}^n \tilde{E}_u(\pi_u)) e^{-\gamma_C G_C(\pi)}$ on the collective's slot model $\mathfrak{B}$ with arbitrary full-support product habits $\tilde{E}_u$, arbitrary precision $\gamma_C \ge 0$, and arbitrary belief $q_C$ on $\eta_C$, write $p_\lambda = \frac{e^\lambda}{2(1+e^\lambda)} \in (\frac{1}{4}, \frac{1}{2})$ and $R = \exp(\frac{1}{2}\gamma_C\sigma_{\max}(q_C)) \ge 1$. Then:
     - Whenever $q_C$ is any independent-block belief ($R = 1$, with $\gamma_C \ge 0$ and $\tilde{E}_u$ completely unrestricted),
       $$\lim_{\gamma\to\infty}\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_C) \ge 2\sqrt{p_\lambda} - 1,$$
       which satisfies $2\sqrt{p_\lambda} - 1 = \frac{\lambda}{4} + O(\lambda^2) = 2^{m-2}\gamma\sigma_{\max}(q_C^\ast) + O((2^m\gamma\sigma_{\max}(q_C^\ast))^2)$ for small $\lambda$ and $\to \sqrt{2} - 1 \approx 0.414214$ as $\lambda \to \infty$.
     - For **arbitrarily correlated** (possibly non-Gaussian) $q_C$, whenever $R \le 2\sqrt{p_\lambda}$,
       $$\lim_{\gamma\to\infty}\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_C) \ge R(2\sqrt{p_\lambda} - R).$$
       In particular, at $\gamma_C = \gamma$ and $q_C = q_C^\ast$ (or any $q_C$ with $\sigma_{\max}(q_C) = O(\sigma_{\max}(q_C^\ast))$), $R = \exp(O(\lambda\cdot 2^{-m})) \to 1$ as $m \to \infty$, recovering the same $\sqrt{2}-1$ lower bound.
  3. **(Fixed-$\delta$ non-uniformity in $\gamma$ at $m = 2$, $n = 7$)** For any fixed $\delta \in (0, \frac{b}{3\cdot 2^7}) = (0, 2.6\times 10^{-5})$ (arbitrarily weak exact Hodge-harmonic redundancy disagreement $\sigma_{\max}(q_C^\ast) = \delta > 0$), sending $\gamma \to \infty$ yields $\lim_{\gamma\to\infty}\mathbb{P}^\infty = \frac{1}{2}\delta_B + \frac{1}{2}\delta_C$ and $\lim_{\gamma\to\infty}\inf_{q_C\in\mathcal{Q}_{\mathrm{diag}},\, \gamma_C\ge 0,\, \tilde{E}}\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_C) \ge \sqrt{2} - 1 \approx 0.414214$.
- Status: proved
- Review: self
- Evidence: Complete self-contained proof in `## Derivations` (Proof of `C4`); two-channel verification on $m = 2$ ($n = 7$, $N = 128$) in `open_agy_uniform_bound-checks/verify_uniform_bound.py` and `open_agy_uniform_bound-checks/verify_uniform_bound_stdout.txt` (Section 3b–3c): at $\lambda = 4.0, \gamma = 180$ ($\sigma_{\max} = 0.005556$), Channel 1 and Channel 2 agree to $2.21\times 10^{-6}$ (`cond = 1.6e12`), giving $p(A,B,C,D) = (0.0082, 0.4451, 0.4451, 0.0082)$, analytic bound $2\sqrt{p}-1 = 0.33432 \le 0.36391$ (numerical optimization over all rank-1 $2\times 2$ matrices, approaching limiting $0.401438$); correlated-$q_C$ trade-off bound evaluated at $m = 3, 4, 5, 6$ ($\lambda = 4.0$) gives $0.15076, 0.30401, 0.35867, 0.38143$; negative control with planted wrong bound $2\sqrt{p}-0.5$ at $p=0.45$ is violated by explicit rank-1 $Q$ ($\mathrm{TV} = 0.341641 = 2\sqrt{0.45}-1 < 0.841641$).
- Depends on: C2, C3

## Derivations

### Proof of C1 ($n = 2$ Minimal Non-Uniformity in $\gamma$)

**Step 1 (Linear-Gaussian realization and Hodge decomposition).**
Let $\eta_C \in \mathbb{R}$ be scalar, $\mathcal{A}_1 = \mathcal{A}_2 = \{0, 1\}$, $\mathfrak{B}_i(0) = \varnothing$, and $\mathfrak{B}_i(1) = \{o_i\}$ with $o_i = \lambda(\eta_C + \nu_i)$, $\nu_1, \nu_2 \sim \mathcal{N}(0, 1)$ independent of each other and of $\eta_C$. Under $q = \mathcal{N}(0, v)$ with $v > 0$, mutual information is scale-invariant ($\lambda > 0$), so $I_q(\eta_C; o_i) = \frac{1}{2}\ln(1+v)$ and $I_q(o_1; o_2) = \frac{1}{2}\ln\frac{(1+v)^2}{1+2v} =: f(v)$. Setting $K = e^{2I} > 1$, the equation $(1+v)^2/(1+2v) = K$ rearranges to $v^2 - 2(K-1)v - (K-1) = 0$, whose unique positive root is $v(I) = (K-1) + \sqrt{K(K-1)} > 0$. Setting $q_1 = \mathcal{N}(0, v(I_C+\delta))$, $q_2 = \mathcal{N}(0, v(I_C-\delta))$, and $q_C^\ast = \mathcal{N}(0, v(I_C))$ ($0 < \delta < I_C$) gives $I_{q_1}(o_1; o_2) = I_C + \delta$, $I_{q_2}(o_1; o_2) = I_C - \delta$, and $I_{q_C^\ast}(o_1; o_2) = I_C$.

Choose $\lambda = [2\pi e (v(I_C+\delta)+1)]^{-1/2}$. For Gaussian slot preference $\tilde{p}_i(o_i) = \mathcal{N}(\mu^\star_i, \tau_i^2)$ with $\tau_i^2 = \lambda^2(v_i+1)$, we have $\psi^{(i)}_{\{o_i\}}(q_i) = \frac{1}{2}\ln(2\pi e \tau_i^2) + (\mu^\star_i)^2/(2\tau_i^2)$ where $\frac{1}{2}\ln(2\pi e \tau_i^2) \le 0$. Since $I_{q_i}(\eta_C; o_i) - I_{q_i}(o_1; o_2) = \frac{1}{2}\ln\frac{1+2v_i}{1+v_i} > 0$, we have $I_{q_i}(\eta_C; o_i) > I_C - \delta > h + \varepsilon$ whenever $h + \varepsilon < I_C - \delta$, or for arbitrary real $c_i$ we simply choose $\lambda > 0$ small enough that $\frac{1}{2}\ln(2\pi e \lambda^2(v_i+1)) \le c_i + I_{q_i}(\eta_C; o_i)$ and tune $(\mu^\star_i)^2 \ge 0$ so that $c_i := \psi^{(i)}_{\{o_i\}}(q_i) - I_{q_i}(\eta_C; o_i)$ takes the exact values $c_1 = -h - \varepsilon$ and $c_2 = -h$.

By `lem:agy-decomposition`, under $q_C^\ast$, $\Phi(\pi) = c_1\pi_1 + c_2\pi_2 + I_C\pi_1\pi_2$, $\mathcal{R}_1(\pi) = +\delta\pi_1\pi_2$, and $\mathcal{R}_2(\pi) = -\delta\pi_1\pi_2$, so $\mathcal{R}_1 + \mathcal{R}_2 \equiv 0$ and $\sigma_1 = \sigma_2 = \sigma_{\max}(q_C^\ast) = \delta$. On the 4-cycle $(0,0)\to(1,0)\to(1,1)\to(0,1)\to(0,0)$, the edge-difference cochain of $\mathcal{R}$ is $(0, -\delta, -\delta, 0)$, which decomposes orthogonally in $\ell^2(E(Q_2))$ as $(-\delta/2, -\delta/2, -\delta/2, -\delta/2) + (+\delta/2, -\delta/2, -\delta/2, +\delta/2)$, the second term being the discrete gradient of $\Delta\Phi(\pi) = \frac{\delta}{2}(\pi_1 - \pi_2)$. Thus the exact Candogan–Ozdaglar–Parrilo Hodge potential projection of $G$ is $\Phi_{\mathrm{Hodge}}(\pi) = \Phi(\pi) + \frac{\delta}{2}(\pi_1 - \pi_2)$.

**Step 2 (Exact 4-spanning-tree asymptotics).**
With uniform habits $E_i = (\frac{1}{2}, \frac{1}{2})$, every off-diagonal transition probability of $\mathsf{T}$ on $\{0,1\}^2$ is $\frac{1}{2}$ times a logistic probability $\mathrm{sig}(-\gamma\Delta G_i) = (1 + e^{\gamma\Delta G_i})^{-1}$. Under the hypotheses $\frac{1}{2}I_C < h < I_C - \delta$ and $\delta < \varepsilon < \min(2\delta, I_C - h + \delta)$, we have $c_1 = -h - \varepsilon < 0$, $c_2 = -h < 0$, $c_2 + I_2 = I_C - h - \delta > 0$, and $c_1 + I_1 = I_C - h - \varepsilon + \delta > 0$. Writing $a \sim b$ for $\lim_{\gamma\to\infty} a/b = 1$, the eight off-diagonal factors $2\mathsf{T}(\pi, \pi')$ satisfy:
- $00 \to 10$: $\sim 1$; $\quad 10 \to 00$: $\sim e^{-\gamma(h+\varepsilon)}$;
- $00 \to 01$: $\sim 1$; $\quad 01 \to 00$: $\sim e^{-\gamma h}$;
- $10 \to 11$: $\sim e^{-\gamma(I_C - h - \delta)}$; $\quad 11 \to 10$: $\sim 1$;
- $01 \to 11$: $\sim e^{-\gamma(I_C - h - \varepsilon + \delta)}$; $\quad 11 \to 01$: $\sim 1$.

Each vertex of the 4-cycle $Q_2$ has exactly 4 directed spanning trees rooted at it (one for each deleted edge), and the common factor $(1/2)^3$ cancels across all roots. Computing the 4 tree weights (times $8$) for each root:
- Root $(0, 1)$: two trees ($10\to 11\to 01, 00\to 01$ and $00\to 10\to 11\to 01$) have weight $\sim e^{-\gamma(I_C - h - \delta)}$, and two trees ($10\to 00\to 01, 11\to 01$ and $11\to 10\to 00\to 01$) have weight $\sim e^{-\gamma(h+\varepsilon)}$. Since $h > I_C/2$ implies $I_C - h - \delta < h + \varepsilon$, $W(0, 1) \sim 2e^{-\gamma(I_C - h - \delta)}$.
- Root $(1, 0)$: two trees have weight $\sim e^{-\gamma(I_C - h - \varepsilon + \delta)}$ and two have weight $\sim e^{-\gamma h}$. Since $h > I_C/2$ and $\varepsilon > \delta$ imply $I_C - h - \varepsilon + \delta < h$, $W(1, 0) \sim 2e^{-\gamma(I_C - h - \varepsilon + \delta)}$.
- Root $(0, 0)$: the four trees have exponents $2h+\varepsilon$, $2h+\varepsilon$, $I_C-\delta$, and $I_C+\delta$, all strictly exceeding $I_C - h - \delta$ by at least $h > 0$.
- Root $(1, 1)$: the four trees have exponents $2(I_C-h)-\varepsilon$, $2(I_C-h)-\varepsilon$, $I_C+\delta$, and $I_C-\delta$, all strictly exceeding $I_C - h - \delta$ by at least $\min(I_C - h - \varepsilon + \delta, h) > 0$.

By the Markov chain tree theorem,
$$\frac{\mathbb{P}^\infty(0,1)}{\mathbb{P}^\infty(1,0)} = \frac{W(0,1)}{W(1,0)} \sim e^{\gamma(2\delta - \varepsilon)} \to \infty \quad (\text{since } \varepsilon < 2\delta),$$
while $\mathbb{P}^\infty(0,0)/\mathbb{P}^\infty(0,1) \to 0$ and $\mathbb{P}^\infty(1,1)/\mathbb{P}^\infty(0,1) \to 0$. Hence $\mathbb{P}^\infty(0,1) \to 1$.

**Step 3 (Comparison with $\inf_{q_C}\mathbb{P}_\Phi(q_C)$ and $\mathbb{P}_{\Phi_{\mathrm{Hodge}}}$).**
For **any** declared belief $q_C$ on $\mathbb{R}$ (with finite mutual informations), `lem:agy-decomposition` gives $\Phi(q_C)(\pi) = \sum_{j=1}^2 c_j\pi_j + M_{q_C}(\pi)$ where $M_{q_C}(1,0) = M_{q_C}(0,1) = 0$. Therefore $\Phi(q_C)(1,0) = c_1 = -h - \varepsilon < -h = c_2 = \Phi(q_C)(0,1)$ independently of $q_C$, whence $\mathbb{P}_\Phi(q_C)(0,1) \le \mathbb{P}_\Phi(q_C)(0,1)/\mathbb{P}_\Phi(q_C)(1,0) = e^{-\gamma\varepsilon}$ for **every** $q_C$. Thus $\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_\Phi(q_C)) \ge \mathbb{P}^\infty(0,1) - \mathbb{P}_\Phi(q_C)(0,1) \ge \mathbb{P}^\infty(0,1) - e^{-\gamma\varepsilon}$ uniformly in $q_C$, so $\lim_{\gamma\to\infty}\inf_{q_C}\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_\Phi(q_C)) = 1$.

For $\Phi_{\mathrm{Hodge}}$, $\Phi_{\mathrm{Hodge}}(1,0) = -h - \varepsilon + \delta/2 < -h - \delta/2 = \Phi_{\mathrm{Hodge}}(0,1)$ (since $\varepsilon > \delta$), so $\mathbb{P}_{\Phi_{\mathrm{Hodge}}}(0,1) \le e^{-\gamma(\varepsilon-\delta)} \to 0$ and $\lim_{\gamma\to\infty}\mathrm{TV}(\mathbb{P}^\infty, \mathbb{P}_{\Phi_{\mathrm{Hodge}}}) = 1$. $\square$

---

### Proof of C2 ($m$-Gear Train: Harmonicity, Topology, Landscape)

**Step 1 (Edge count, linear-Gaussian realization, and exact Hodge harmonicity).**
Gear $0$ has $4$ nodes ($\binom{4}{2} = 6$ intra-gear edges: $4$ adjacent, $2$ wall); each middle gear $1 \le g \le m-2$ has $8$ nodes ($\binom{8}{2} = 28$ intra-gear edges: $8$ adjacent, $20$ wall); top gear $m-1$ has $3$ nodes ($\binom{3}{2} = 3$ intra-gear edges: $2$ adjacent, $1$ wall). For inter-gear walls between $g$ and $g+1$: each even $r \in \{0,2,4,6\}$ allows $\frac{|V_g|}{2}+1$ nodes of $V_g$ and forbids $\frac{|V_g|}{2}-1$; each odd $r \in \{1,3,5,7\}$ allows $1$ node and forbids $|V_g|-1$. Thus for $m=2$, $|E| = 6 + 3 + (1 + 3 + 1) = 14$; for $m \ge 3$, $|E| = 6 + 28(m-2) + 3 + (4\cdot 1 + 4\cdot 3) + (m-3)(4\cdot 3 + 4\cdot 7) + (3 + 7 + 3) = 68m - 138 = O(n)$.

Each coordinate $\eta_e$ ($e \in E$) is independent under $q_C^\ast$ and under every $q_u$, so $I_{q_u}(\eta_C; o_{\mathfrak{B}(\pi)}) = \sum_{e=\{x,y\}\in E} \frac{1}{2}\ln(1 + (\pi_x+\pi_y)v_{u,e})$, and therefore the redundancy perceived by $u$ on active profile $\pi$ is
$$I_{q_u}(o_{\mathfrak{B}_u(\pi_u)}; o_{A_{-u}}) = \pi_u \sum_{e=\{u,y\}\ni u} \pi_y f(v_{u,e}),$$
where $f(v) = \frac{1}{2}\ln\frac{(1+v)^2}{1+2v}$. For $u \notin V_0$, $q_u = q_C^\ast$, so $\mathcal{R}_u \equiv 0$ and $\sigma_u = 0$. For $u \in V_0 = \{0, 1, 2, 3\}$, $v_{u,e} = v_{C,e}$ on every edge except the two incident motor edges $(u, u+1)$ (variance $v(1+\delta)$, giving $f(v) = 1+\delta$) and $(u-1, u)$ (variance $v(1-\delta)$, giving $f(v) = 1-\delta$), indices mod $4$. Subtracting $f(v_{C,e}) = 1$ gives
$$\mathcal{R}_u(\pi) = \delta\pi_u(\pi_{(u+1)\bmod 4} - \pi_{(u-1)\bmod 4}) \qquad (u \in V_0).$$
Since $\pi_{u+1} - \pi_{u-1} \in \{-1, 0, 1\}$, $\sigma_u = \max_{\pi_{-u}}|\mathcal{R}_u(1,\pi_{-u}) - 0| = \delta$ for $u \in V_0$, hence $\sigma_{\max}(q_C^\ast) = \delta$ and $\sum_u \sigma_u = 4\delta$. Moreover, at every $\pi \in \{0,1\}^n$,
$$\sum_{u=0}^3 \mathcal{R}_u(\pi) = \delta \sum_{u=0}^3 (\pi_u \pi_{u+1} - \pi_u \pi_{u-1}) = 0,$$
and since $\mathcal{R}_u(\pi\oplus e_u) - \mathcal{R}_u(\pi) = (1 - 2\pi_u)\delta(\pi_{u+1} - \pi_{u-1})$ for $u \in V_0$ (and $0$ for $u \notin V_0$),
$$(\delta^\ast\mathcal{R})(\pi) = \delta\sum_{u=0}^3 (\pi_{u+1} - \pi_{u-1}) - 2\delta\sum_{u=0}^3 (\pi_u\pi_{u+1} - \pi_u\pi_{u-1}) \equiv 0.$$
Every member $u \in V_m$ is incident to at least one edge of $E$ (in fact at least one adjacent edge of $I_{\mathrm{adj}} = 1$ or wall edge of $I_{\mathrm{wall}} = 5$), so $I_{q_u}(\eta_C; o_{\mathfrak{B}_u(1)}) > 1 > |c_u|$ for every $u$. Choosing uniform scale $\lambda = [2\pi e(\max(v(5), v(1+\delta))+1)]^{-1/2}$ and slot preferences $\mathcal{N}(\mu^\star_{u,e}, \tau_{u,e}^2)$ with $\tau_{u,e}^2 = \lambda^2(v_{u,e}+1)$ makes $\sum_{e\ni u}\frac{1}{2}\ln(2\pi e\tau_{u,e}^2) \le 0 < c_u + I_{q_u}(\eta_C; o_{\mathfrak{B}_u(1)})$, so tuning $(\mu^\star_{u,e})^2 \ge 0$ realizes every target own-policy cost $c_u$ exactly with positive $\psi^{(u)}_{\mathfrak{B}_u(1)}(q_u) > 0$.

**Step 2 (Inductive proof of 1D-path topology and motor-step count).**
For $k \ge 1$, let $\mathcal{V}_k$ be the graph of wall-free one-hot tuples $(x_0, \dots, x_{k-1})$ on the closed-gear chain of gears $0, \dots, k-1$ (gear $0$: 4-cycle; gears $1, \dots, k-1$: 8-cycles), with edges connecting tuples that differ in one gear $g$ by an adjacent step of $E_{\mathrm{adj}}$. Set $(a_{\mathrm{lo}}(1), a_{\mathrm{hi}}(1)) = (0, 2)$ and $(a_{\mathrm{lo}}(k), a_{\mathrm{hi}}(k)) = (1, 5)$ for $k \ge 2$. Let $\mathrm{Arc}_1(k)$ be the induced subgraph of $\mathcal{V}_k$ where $x_{k-1}$ lies in $\{a_{\mathrm{lo}}(k), \dots, a_{\mathrm{hi}}(k)\}$ (clockwise half-arc of length $\frac{|V_{k-1}|}{2} + 1$), and $\mathrm{Arc}_2(k)$ the complementary half-arc $\{a_{\mathrm{hi}}(k), \dots, a_{\mathrm{lo}}(k)\}$.

We prove by induction on $k \ge 1$ that:
- (I1) For $k \ge 2$, each odd state $r \in \{1, 3, 5, 7\}$ of gear $k-1$ has a unique tuple $L_k(r) \in \mathcal{V}_k$ with $x_{k-1} = r$ (for $k = 1$, denote $L_1(r) = (r)$).
- (I2) $\mathrm{Arc}_1(k)$ is an induced unbranched 1D path of $N_k = 3\cdot 2^k - 3$ vertices from $L_k(a_{\mathrm{lo}}(k))$ to $L_k(a_{\mathrm{hi}}(k))$, along which every gear-0 step is clockwise with total motor-step count $S_k = 2^k$; symmetrically, $\mathrm{Arc}_2(k)$ is an induced 1D path of $N_k$ vertices from $L_k(a_{\mathrm{hi}}(k))$ to $L_k(a_{\mathrm{lo}}(k))$ with $S_k = 2^k$ clockwise motor steps.

*Base case $k = 1$:* $\mathrm{Arc}_1(1)$ is $0 - 1 - 2$ ($N_1 = 3 = 3\cdot 2^1 - 3$, $S_1 = 2 = 2^1$ clockwise steps); $\mathrm{Arc}_2(1)$ is $2 - 3 - 0$ ($N_1 = 3$, $S_1 = 2$ clockwise steps).

*Inductive step $k \to k+1$:* By definition of the inter-gear walls between gear $k-1$ and gear $k$:
- $x_k \in \{1, 5\}$ forces $x_{k-1} = a_{\mathrm{hi}}(k)$, and $x_k \in \{3, 7\}$ forces $x_{k-1} = a_{\mathrm{lo}}(k)$. Since $a_{\mathrm{lo}}(k), a_{\mathrm{hi}}(k)$ are odd for $k \ge 2$ (and singletons for $k = 1$), (I1) at level $k$ uniquely determines $(x_0, \dots, x_{k-1})$ as $L_k(a_{\mathrm{hi}}(k))$ or $L_k(a_{\mathrm{lo}}(k))$. This proves (I1) at level $k+1$.
- For $\mathrm{Arc}_1(k+1)$ ($x_k \in \{1, 2, 3, 4, 5\}$), partition the vertices by $x_k$:
  - $x_k = 1$: the unique vertex $L_{k+1}(1) = (L_k(a_{\mathrm{hi}}(k)), 1)$;
  - $x_k = 2$: the allowed $(x_0, \dots, x_{k-1})$ are precisely $\mathrm{Arc}_2(k)$, an induced 1D path of $N_k$ vertices from $(L_k(a_{\mathrm{hi}}(k)), 2)$ to $(L_k(a_{\mathrm{lo}}(k)), 2)$ with $S_k$ clockwise motor steps;
  - $x_k = 3$: the unique vertex $L_{k+1}(3) = (L_k(a_{\mathrm{lo}}(k)), 3)$;
  - $x_k = 4$: precisely $\mathrm{Arc}_1(k)$, an induced 1D path of $N_k$ vertices from $(L_k(a_{\mathrm{lo}}(k)), 4)$ to $(L_k(a_{\mathrm{hi}}(k)), 4)$ with $S_k$ clockwise motor steps;
  - $x_k = 5$: the unique vertex $L_{k+1}(5) = (L_k(a_{\mathrm{hi}}(k)), 5)$.
  Between distinct values of $x_k \in \{1, 2, 3, 4, 5\}$, only consecutive values are adjacent in $E_{\mathrm{adj}}$, and each consecutive pair has one odd value ($1, 3,$ or $5$) whose slice is a singleton sharing the exact endpoint of the adjacent even slice ($x_k = 2$ or $4$). Hence there are no cross-edges other than the four unique concatenating edges $1-2$, $2-3$, $3-4$, $4-5$. Thus $\mathrm{Arc}_1(k+1)$ is an induced 1D path from $L_{k+1}(1)$ to $L_{k+1}(5)$ of $N_{k+1} = 2N_k + 3 = 3\cdot 2^{k+1} - 3$ vertices and $S_{k+1} = 2S_k = 2^{k+1}$ clockwise motor steps. The exact same argument (shifting $x_k$ by $+4\bmod 8$) establishes $\mathrm{Arc}_2(k+1)$, completing the induction.

Now for $m \ge 2$, the top gear $g_{m-1}$ is the open 3-path $0 - 1 - 2$ coupled to $\mathcal{V}_{m-1}$. Partitioning $\mathcal{P}_m$ by $x_{m-1} \in \{0, 1, 2\}$:
- $x_{m-1} = 0$: $\mathrm{Arc}_1(m-1)$ ($N_{m-1}$ vertices, from $A = (L_{m-1}(a_{\mathrm{lo}}), 0)$ to $B = (L_{m-1}(a_{\mathrm{hi}}), 0)$, $S_{m-1} = 2^{m-1}$ motor steps);
- $x_{m-1} = 1$: the unique vertex $M := (L_{m-1}(a_{\mathrm{hi}}), 1)$ (0 motor steps);
- $x_{m-1} = 2$: $\mathrm{Arc}_2(m-1)$ ($N_{m-1}$ vertices, from $D = (L_{m-1}(a_{\mathrm{hi}}), 2)$ to $C = (L_{m-1}(a_{\mathrm{lo}}), 2)$, $S_{m-1} = 2^{m-1}$ motor steps).
Since $(0, 2) \in E_{\mathrm{wall}}$, the only edges between slices are $B - M$ and $M - D$. Thus $\mathcal{P}_m$ is a 1D path of $|\mathcal{P}_m| = 2N_{m-1} + 1 = 3\cdot 2^m - 5$ vertices from $v_0 = A$ to $v_L = C$, with total motor steps $s(v_L) = 2S_{m-1} = 2^m$ and checkpoint step counts $(s(A), s(B), s(D), s(C)) = (0, 2^{m-1}, 2^{m-1}, 2^m)$. By (I1), $A, B, D, C$ are the unique elements of $\mathcal{P}_m$ with $g_{m-1} \in \{0, 2\}$ and $g_{m-2} \in \{a_{\mathrm{lo}}, a_{\mathrm{hi}}\}$; moreover for $m \ge 3$, since the escapement rule between gear $m-3$ and gear $m-2$ locks $x_{m-3} = a_{\mathrm{hi}}(m-2)$ for **both** $x_{m-2} = 1$ and $x_{m-2} = 5$, $L_{m-1}(1)$ and $L_{m-1}(5)$ share the exact same lower-gear tuple $L_{m-2}(a_{\mathrm{hi}}(m-2))$ on gears $0, \dots, m-3$ (and for $m = 2$, the lower-gear set is empty). Thus $A, B, D, C$ share the identical active subset $S_{\mathrm{low}}$ on gears $0, \dots, m-3$.

Also, to count trailing states with $s(v) = 2^m$: after the last gear-0 move in $\mathrm{Arc}_2(m-1)$, each gear $g = 1, \dots, m-2$ takes one final closing step to its odd endpoint $a_{\mathrm{lo}}(g+1)$, giving $m - 2$ zero-motor-step transitions at the end of the path, hence exactly $m - 1$ states in $\mathcal{P}_m$ with $s(v) = 2^m$.

Finally, check that the induced subgraph of the hypercube $Q_n$ on $V_0 = \mathcal{P}_m \cup \mathcal{B}_m$ is the exact unbranched 1D path $v_0 - u_0 - v_1 - \dots - u_{L-1} - v_L$: all profiles in $\mathcal{P}_m$ have Hamming weight $m$ (so pairwise $d_H \ge 2$), all profiles in $\mathcal{B}_m$ have weight $m+1$ (so pairwise $d_H \ge 2$), and a bridge $u_k = v_k \cup v_{k+1}$ has $k_{g^\ast}(u_k) = 2$ in one gear $g^\ast$ and $k_g(u_k) = 1$ in all other gears, so removing one active bit to obtain a one-hot profile in $\mathcal{P}_m$ must remove one of the two bits in $g^\ast$, leaving only $v_k$ and $v_{k+1}$.

**Step 3 (Energy landscape on all $2^n$ profiles).**
Write $\Phi(\pi) = \sum_{g=0}^{m-1} \Phi_g(\pi_g) + \sum_{g=0}^{m-2} \Phi_{g, g+1}(\pi_g, \pi_{g+1})$, with $\Phi_{g, g+1} \ge 0$ (counting inter-gear wall edges with weight $I_{\mathrm{wall}} = 5$). In the uniform-cost case ($c_u = -h = -0.9$, $I_{\mathrm{adj}} = 1$, $\Delta = 1 - h = 0.1$), inside each gear $g$ with $k_g$ active bits:
- $k_g = 0 \implies \Phi_g = 0 = (-h) + h$;
- $k_g = 1 \implies \Phi_g = -h$;
- $k_g = 2$ (adjacent) $\implies \Phi_g = -2h + 1 = (-h) + \Delta$;
- $k_g = 2$ (non-adjacent) $\implies \Phi_g = -2h + 5 = (-h) + 4.1$;
- $k_g \ge 3$: inside a 4-cycle, 8-cycle, or 3-path, any $k_g \ge 3$ vertices contain at least one wall edge (for $k_g = 3$: $-3h + 2\cdot 1 + 5 = (-h) + 5.2$; for $k_g \ge 4$: $-k_g h + \binom{k_g}{2} \cdot 1 \ge (-h) + \frac{k_g(k_g - 3)}{2} + 0.1 k_g + 0.9 \ge (-h) + 3.3$).

Hence $\Phi(\pi) \ge E_0 = -mh$ everywhere, with equality iff $k_g = 1$ for all $g$ and no inter-gear wall edge is active ($\pi \in \mathcal{P}_m$). Next, $\Phi(\pi) = E_0 + \Delta$ iff exactly one gear $g^\ast$ has $k_{g^\ast} = 2$ with an adjacent pair $\{p, q\}$, all other gears have $k_g = 1$, and zero inter-gear wall edges are active; removing $p$ or $q$ then yields two adjacent profiles $v_k, v_{k+1} \in \mathcal{P}_m$, so $\pi = v_k \cup v_{k+1} \in \mathcal{B}_m$. Every $\pi \in V_1 = \{0,1\}^n \setminus (\mathcal{P}_m \cup \mathcal{B}_m)$ either has at least two gears with $k_g \ge 2$ ($\Phi \ge E_0 + 2\Delta$), or some $k_g = 0$ ($\Phi \ge E_0 + h$), or an active wall edge ($\Phi \ge E_0 + 4.1$), so $\Phi(\pi) \ge E_0 + 2\Delta$. From any $v \in \mathcal{P}_m$, a single-bit flip leaving $V_0$ either turns off an active bit ($\Delta\Phi = +h$) or turns on a bit creating at least one wall edge ($\Delta\Phi \ge I_{\mathrm{wall}} - h = 4.1 > h$). From any $u \in \mathcal{B}_m$, a single-bit flip leaving $V_0$ goes from $\Phi(u) = E_0 + \Delta$ to $\Phi(w) \ge E_0 + 2\Delta$, so $\Delta\Phi \ge \Delta$.

In the 4-checkpoint case ($b = 0.01 = \Delta/10$ subtracted from the 4 nodes $u_{m-2, a_{\mathrm{lo}}}, u_{m-2, a_{\mathrm{hi}}}, u_{m-1, 0}, u_{m-1, 2}$, plus $\eta := 2^m\delta < b/2$ added to $u_{m-1, 2}$):
- On $\mathcal{P}_m$, a profile gets bonus $-2b$ iff both its gear-$(m-2)$ and gear-$(m-1)$ active nodes are among the 4 checkpoint nodes, which by Step 2 holds precisely for $\{A, B, C, D\}$. Thus $\Phi(A) = \Phi(B) = E_0 - 2b$, $\Phi(D) = \Phi(C) = E_0 - 2b + \eta$, and every $\pi \in \mathcal{P}_m \setminus \{A, B, C, D\}$ has $\Phi(\pi) \ge E_0 - b$.
- For any single-bit flip $v \to w$ from $v \in \mathcal{P}_m$ to $w \in V_1$: turning off an active bit $i$ gives $\Delta\Phi = -c_i \ge h - \eta$ (or $h + b - \eta$); turning on a bit creating a wall edge gives $\Delta\Phi \ge I_{\mathrm{wall}} - h - b = 4.09 > h$.
- For any single-bit flip $u \to w$ from $u \in \mathcal{B}_m$ to $w \in V_1$: turning off a bit in a gear $g \neq g^\ast$ gives $\Delta\Phi \ge h - \eta$; turning on a bit creating a wall edge gives $\Delta\Phi \ge I_{\mathrm{wall}} - h - b = 4.09$; turning on a bit creating an adjacent pair in a second gear gives $\Delta\Phi = c_i + I_{\mathrm{adj}} \ge \Delta - b$. Hence $\Delta\Phi \ge \Delta - b$ on every edge from $\mathcal{B}_m$ to $V_1$.
- For any bridge-to-path edge $u \to v$ ($u \in \mathcal{B}_m, v \in \mathcal{P}_m$), the removed bit $i$ has $c_i \in [-h-b, -h]$, so $\Delta\Phi = -c_i - I_{\mathrm{adj}} \le -\Delta + b = -0.09 < 0$.
- Finally, a path profile $v \in \mathcal{P}_m$ has a bridge neighbor turning on one of the 4 checkpoint nodes iff $v$ is adjacent on $\mathcal{P}_m$ to one of $A, B, C, D$ (since turning on $u_{m-1,0}$ or $u_{m-1,2}$ from $\mathcal{P}_m$ can only happen from $M$, turning on $u_{m-2, a_{\mathrm{lo}}}$ only from the unique neighbors of $A$ and $C$ on $\mathcal{P}_m$, and turning on $u_{m-2, a_{\mathrm{hi}}}$ only from the neighbors of $B$ and $D$ inside $x_{m-1} \in \{0, 2\}$). That is at most $5$ profiles in $\mathcal{P}_m$. $\square$

---

### Proof of C3 ($C_{\mathrm{out}}$-Factorization and Exponential Blowup for $\mathbb{P}_\Phi$)

**Step 1 (Exact factorization of spanning-tree weights).**
Fix $m \ge 2$ ($n = 8m - 9$), $\lambda > 0$, and $\delta = \delta(\gamma) = \lambda/(2^m\gamma)$. Let $V_0 = \mathcal{P}_m \cup \mathcal{B}_m$ ($|V_0| = 6\cdot 2^m - 11$) and $V_1 = \{0,1\}^n \setminus V_0$. By the Markov chain tree theorem (`app05_agency.tex` line 164), $\mathbb{P}^\infty(x) \propto W(x) := \sum_{\tau \in \mathcal{T}(x)} w(\tau)$ where $w(\tau) = \prod_{(a, b) \in \tau} \mathsf{T}(a, b)$.

Fix any $x \in \mathcal{P}_m$ and decompose every $\tau \in \mathcal{T}(x)$ into $\tau_0 = \tau|_{V_0 \setminus \{x\}}$ and $\tau_1 = \tau|_{V_1}$. Because $\tau$ is an acyclic spanning tree directed to $x \in V_0$, $\tau_1$ has no cycles inside $V_1$ and every $w \in V_1$ follows a directed path in $\tau_1$ to its first hitting vertex in $V_0$; hence $\tau_1 \in \mathcal{F}(V_1 \to V_0)$, the set of directed spanning forests of $V_1$ rooted in $V_0$ (a set completely independent of $x \in \mathcal{P}_m$). Conversely, let $\tau_0^{\mathrm{path}}(x)$ be the unique directed spanning tree of the 1D path $V_0$ rooted at $x$; for every $\tau_1 \in \mathcal{F}(V_1 \to V_0)$, $\tau_0^{\mathrm{path}}(x) \cup \tau_1$ is in $\mathcal{T}(x)$ (out-degree $1$ off $x$, every vertex reaches $V_0$ via $\tau_1$ and then $x$ via $\tau_0^{\mathrm{path}}(x)$). Thus
$$W(x) = C_{\mathrm{out}}\, w(\tau_0^{\mathrm{path}}(x)) + \sum_{\tau_1 \in \mathcal{F}(V_1 \to V_0)} w(\tau_1) \sum_{\substack{\tau_0 \ne \tau_0^{\mathrm{path}}(x) \\ \tau_0 \cup \tau_1 \in \mathcal{T}(x)}} w(\tau_0), \qquad C_{\mathrm{out}} := \sum_{\tau_1 \in \mathcal{F}(V_1 \to V_0)} w(\tau_1).$$

**Step 2 (Domination of $\tau_0^{\mathrm{path}}(x)$ over all $\tau_0 \ne \tau_0^{\mathrm{path}}(x)$).**
By `C2`(2), the induced subgraph of $Q_n$ on $V_0$ is the 1D path $v_0 - u_0 - \dots - v_L$, which has a unique spanning tree rooted at $x$. Therefore any $\tau_0 \ne \tau_0^{\mathrm{path}}(x)$ with $\tau_0 \cup \tau_1 \in \mathcal{T}(x)$ cannot stay inside $V_0$: at least one vertex $a^\ast \in V_0 \setminus \{x\}$ must have $\tau_0(a^\ast) \in V_1$.

For every single-bit transition $a \to b = a \oplus e_i$, $\mathsf{T}(a, b) = \frac{1}{n}(1 + e^{\gamma(G_i(b)-G_i(a))})^{-1}$ satisfies
$$\frac{1}{2n} e^{-\gamma [G_i(b)-G_i(a)]_+} \le \mathsf{T}(a, b) \le \frac{1}{n} e^{-\gamma [G_i(b)-G_i(a)]_+}.$$
By `C2`(1) and `C2`(3), for $\delta < \Delta/2$:
- Every $u \in \mathcal{B}_m$ has $[G_i(\tau_0^{\mathrm{path}}(u)) - G_i(u)]_+ = 0$ (since $\Delta\Phi = -\Delta$ and $|\Delta\mathcal{R}_i| \le \delta < \Delta$), whereas if $\tau_0(u) \in V_1$ then $\Delta\Phi \ge \Delta$ and $|\Delta\mathcal{R}_i| \le 2\delta$, giving $[G_i(\tau_0(u)) - G_i(u)]_+ \ge \Delta - 2\delta$.
- Every $v \in \mathcal{P}_m \setminus \{x\}$ has $[G_i(\tau_0^{\mathrm{path}}(v)) - G_i(v)]_+ \le \Delta + \delta$, whereas if $\tau_0(v) \in \mathcal{B}_m$ then $[G_i(\tau_0(v)) - G_i(v)]_+ \ge \Delta - \delta$, and if $\tau_0(v) \in V_1$ then $\Delta\Phi \ge h$ and $|\Delta\mathcal{R}_i| \le \delta$, giving $[G_i(\tau_0(v)) - G_i(v)]_+ \ge h - \delta$.

Multiplying the ratio $\mathsf{T}(a, \tau_0(a))/\mathsf{T}(a, \tau_0^{\mathrm{path}}(a))$ over all $a \in V_0 \setminus \{x\}$ (noting $h - \Delta = 0.8 > \Delta = 0.1$ and at most $|\mathcal{P}_m| - 1$ vertices in $\mathcal{P}_m \setminus \{x\}$ can gain at most $2\delta$ each):
$$\frac{w(\tau_0)}{w(\tau_0^{\mathrm{path}}(x))} \le 2^{|V_0|-1}\exp\Bigl(-\gamma\bigl(\Delta - 2\delta - 2(|\mathcal{P}_m| - 1)\delta\bigr)\Bigr) \le 2^{|V_0|}\exp\Bigl(-\gamma\bigl(\Delta - (6\cdot 2^m - 8)\delta\bigr)\Bigr).$$
Since each vertex in $V_0 \setminus \{x\}$ has $n$ neighbors in $Q_n$, there are at most $n^{|V_0|}$ choices of $\tau_0$. Summing over $\tau_0$ and factoring out $C_{\mathrm{out}}$ yields the claimed inequality
$$1 \le \frac{W(x)}{C_{\mathrm{out}}\, w(\tau_0^{\mathrm{path}}(x))} \le 1 + (2n)^{|V_0|}\exp\Bigl(-\gamma\bigl(\Delta - (6\cdot 2^m - 8)\delta\bigr)\Bigr).$$
With $\delta(\gamma) = \lambda/(2^m\gamma)$, $(6\cdot 2^m - 8)\delta(\gamma) \le 6\lambda/\gamma \to 0$, so the right-hand side converges to $1$ as $\gamma \to \infty$ for every $x \in \mathcal{P}_m$.

**Step 3 (Exact path-tree ratio and limit distribution).**
For any $v_a, v_b \in \mathcal{P}_m$ ($a < b$), $\tau_0^{\mathrm{path}}(v_a)$ and $\tau_0^{\mathrm{path}}(v_b)$ agree outside the subpath $v_a - u_a - \dots - v_b$ and reverse every edge on it:
$$\frac{w(\tau_0^{\mathrm{path}}(v_b))}{w(\tau_0^{\mathrm{path}}(v_a))} = \prod_{k=a}^{b-1} \frac{\mathsf{T}(v_k, u_k)\mathsf{T}(u_k, v_{k+1})}{\mathsf{T}(v_{k+1}, u_k)\mathsf{T}(u_k, v_k)}.$$
At bridge $u_k = v_k \cup \{j_k\} = v_{k+1} \cup \{i_k\}$, the resampling normalizers cancel identically in each single-member ratio:
$$\frac{\mathsf{T}(v_k, u_k)}{\mathsf{T}(u_k, v_k)} = e^{-\gamma[\Phi(u_k)-\Phi(v_k)+\mathcal{R}_{j_k}(u_k)]}, \qquad \frac{\mathsf{T}(u_k, v_{k+1})}{\mathsf{T}(v_{k+1}, u_k)} = e^{+\gamma[\Phi(u_k)-\Phi(v_{k+1})+\mathcal{R}_{i_k}(u_k)]}$$
(using uniform habits and $\mathcal{R}_{j_k}(v_k) = \mathcal{R}_{i_k}(v_{k+1}) = 0$ since $v_k, v_{k+1}$ contain no active motor edge!). Multiplying cancels $\Phi(u_k)$ identically:
$$\frac{\mathsf{T}(v_k, u_k)\mathsf{T}(u_k, v_{k+1})}{\mathsf{T}(v_{k+1}, u_k)\mathsf{T}(u_k, v_k)} = \exp\Bigl(-\gamma[\Phi(v_{k+1}) - \Phi(v_k)] + \gamma[\mathcal{R}_{i_k}(u_k) - \mathcal{R}_{j_k}(u_k)]\Bigr).$$
On a clockwise motor step $(i_k, j_k) \in E_{\mathrm{motor}}$, $\mathcal{R}_{i_k}(u_k) = +\delta$ and $\mathcal{R}_{j_k}(u_k) = -\delta$, giving $+2\gamma\delta$; on any non-motor step, $\mathcal{R}_{i_k} = \mathcal{R}_{j_k} = 0$. Since $\Phi(v_k) = E_0$ is constant on $\mathcal{P}_m$ and $2\gamma\delta = 2\lambda/2^m$,
$$\frac{w(\tau_0^{\mathrm{path}}(v_b))}{w(\tau_0^{\mathrm{path}}(v_a))} = \exp\Bigl(2\lambda\frac{s(v_b) - s(v_a)}{2^m}\Bigr).$$

For the mass outside $\mathcal{P}_m$, `thm:agy-heterogeneous`(a) gives $\mathbb{P}^\infty(w) \le e^{2(2^n-1)\gamma\sigma_{\max}}\mathbb{P}_\Phi(w) = e^{2(2^n-1)\lambda\cdot 2^{-m}}\mathbb{P}_\Phi(w)$ for every $w \notin \mathcal{P}_m$. Since $\Phi(w) - E_0 \ge \Delta$ for all $w \notin \mathcal{P}_m$, $\mathbb{P}_\Phi(w) \le e^{-\gamma\Delta}$, so $\mathbb{P}^\infty(\{0,1\}^n \setminus \mathcal{P}_m) \le 2^n e^{2(2^n-1)\lambda\cdot 2^{-m}} e^{-\gamma\Delta} \to 0$ as $\gamma \to \infty$. Combining this with Step 2 yields $\mathbb{P}^\infty \to \mu_\lambda$ with $\mu_\lambda(v_k) \propto \exp(2\lambda s(v_k)/2^m)$.

Finally, for every independent-block belief $q_C \in \mathcal{Q}_{\mathrm{diag}}$ (even with arbitrary diagonal variances $v_{C,e} \ge 0$), no two active nodes in any $v_k \in \mathcal{P}_m$ share a coordinate of $\eta_C$, so $M_{q_C}(v_k) = 0$ and $\Phi(q_C)(v_k) = E_0$ is constant on $\mathcal{P}_m$. Hence $\mathbb{P}_\Phi(q_C)(v_k) = \frac{1}{|\mathcal{P}_m|}\mathbb{P}_\Phi(q_C)(\mathcal{P}_m) \le \frac{1}{|\mathcal{P}_m|}$ for every $v_k \in \mathcal{P}_m$. For the top set $S_{\mathrm{top}} = \{v_k \in \mathcal{P}_m : s(v_k) = 2^m\}$ of size $|S_{\mathrm{top}}| = m - 1$, $\mathbb{P}_\Phi(q_C)(S_{\mathrm{top}}) \le \frac{m-1}{3\cdot 2^m - 5}$ uniformly over all $q_C \in \mathcal{Q}_{\mathrm{diag}}$. Therefore
$$\inf_{q_C \in \mathcal{Q}_{\mathrm{diag}}} \mathrm{TV}\bigl(\mathbb{P}^\infty, \mathbb{P}_\Phi(q_C)\bigr) \ge \mathbb{P}^\infty(S_{\mathrm{top}}) - \frac{m-1}{3\cdot 2^m - 5} \xrightarrow{\gamma\to\infty} \mu_\lambda(S_{\mathrm{top}}) - \frac{m-1}{3\cdot 2^m - 5} \xrightarrow{\lambda\to\infty} 1 - \frac{m-1}{3\cdot 2^m - 5},$$
with exact limit $\mathrm{TV}(\mu_\lambda, \mathrm{Unif}(\mathcal{P}_m))$ at $q_C = q_C^\ast$ (where $\lim_{\gamma\to\infty}\mathbb{P}_\Phi(q_C^\ast) = \mathrm{Unif}(\mathcal{P}_m)$). Also at $q_C = q_C^\ast$, $\mathbb{P}_\Phi(v_L) = \mathbb{P}_\Phi(v_0)$ for all $\gamma$, so $\lim_{\gamma\to\infty}\ln\frac{\mathbb{P}^\infty(v_L)/\mathbb{P}_\Phi(v_L)}{\mathbb{P}^\infty(v_0)/\mathbb{P}_\Phi(v_0)} = 2\lambda = 2^{m+1}\gamma\sigma_{\max}(q_C^\ast)$, and by the triangle inequality $\max_\pi |\ln(\mathbb{P}^\infty(\pi)/\mathbb{P}_\Phi(\pi))| \ge \frac{1}{2}|\ln\frac{\mathbb{P}^\infty(v_L)/\mathbb{P}_\Phi(v_L)}{\mathbb{P}^\infty(v_0)/\mathbb{P}_\Phi(v_0)}| \to \lambda = 2^m\gamma\sigma_{\max}(q_C^\ast)$. $\square$

---

### Proof of C4 (Class 2 Lower Bound and Correlated-$q_C$ Trade-Off)

**Step 1 (Limiting distribution $P_\lambda$ on $\{A, B, C, D\}$).**
Consider the 4-checkpoint $m$-gear model of `C2`(3) with $b = \Delta/10 = 0.01$ and tilt $\eta = 2^m\delta$ on $u_{m-1, 2}$. Repeat the $C_{\mathrm{out}}$-factorization of `C3` for any $x \in \mathcal{P}_m$:
- Every $u \in \mathcal{B}_m$ has $[G_i(\tau_0^{\mathrm{path}}(u)) - G_i(u)]_+ = 0$ (since $\Delta\Phi \le -\Delta + b = -0.09 < -\delta$), while any $\tau_0(u) \in V_1$ has $\Delta\Phi \ge \Delta - b$ (`C2`(3)) and $|\Delta\mathcal{R}_i| \le 2\delta$, giving $[G_i(\tau_0(u)) - G_i(u)]_+ \ge \Delta - b - 2\delta$.
- Every $v \in \mathcal{P}_m \setminus \{x\}$ leaving $V_0$ to $V_1$ has $\Delta\Phi \ge h - \eta$ (`C2`(3)), an excess over any bridge edge ($\Delta\Phi \le \Delta + \eta$) of at least $h - \Delta - 2\eta - 2\delta > \Delta - b - 2\delta$.
- For vertices $v \in \mathcal{P}_m \setminus \{x\}$ switching from one bridge neighbor to the other, by `C2`(3) at most $5$ vertices in $\mathcal{P}_m$ have a bridge neighbor turning on a $-b$-bonus node (saving at most $b$ each), while all other vertices can save at most $\eta$ (for the single vertex turning on $u_{m-1,2}$, already counted) plus $2\delta$ on motor steps.
Hence any $\tau_0 \ne \tau_0^{\mathrm{path}}(x)$ has excess action at least
$$(\Delta - b - 2\delta) - 5b - (2|\mathcal{P}_m| - 2)\delta = \Delta - 6b - (6\cdot 2^m - 8)\delta = 0.04 - (6\cdot 2^m - 8)\delta,$$
so
$$1 \le \frac{W(x)}{C_{\mathrm{out}}\, w(\tau_0^{\mathrm{path}}(x))} \le 1 + (2n)^{|V_0|}\exp\Bigl(-\gamma\bigl(0.04 - (6\cdot 2^m - 8)\delta\bigr)\Bigr).$$
Both along $\delta(\gamma) = \lambda/(2^m\gamma)$ ($\gamma \to \infty$) and for any fixed $\delta \in (0, \frac{0.04}{2(6\cdot 2^m - 8)})$, the right-hand side converges to $1$ as $\gamma \to \infty$.

By the exact telescoping ratio of `C3` Step 3, for all $x, y \in \{A, B, C, D\}$,
$$\frac{w(\tau_0^{\mathrm{path}}(y))}{w(\tau_0^{\mathrm{path}}(x))} = \exp\Bigl(-\gamma[\Phi(y) - \Phi(x)] + 2\gamma\delta[s(y) - s(x)]\Bigr).$$
Substituting $\Phi(A) = \Phi(B) = E_0 - 2b$, $\Phi(D) = \Phi(C) = E_0 - 2b + 2^m\delta$, and $(s(A), s(B), s(D), s(C)) = (0, 2^{m-1}, 2^{m-1}, 2^m)$, with $\lambda := 2^m\gamma\delta$:
- $B/A$: $e^{0 + 2\gamma\delta \cdot 2^{m-1}} = e^\lambda$;
- $D/A$: $e^{-\gamma\cdot 2^m\delta + 2\gamma\delta \cdot 2^{m-1}} = e^{-\lambda + \lambda} = 1$;
- $C/A$: $e^{-\gamma\cdot 2^m\delta + 2\gamma\delta \cdot 2^m} = e^{-\lambda + 2\lambda} = e^\lambda$.

For mass outside $\{A, B, C, D\}$, every $w \in \mathcal{P}_m \setminus \{A, B, C, D\}$ satisfies $\Phi(w) \ge E_0 - b = \Phi(A) + b$, and every $w \notin \mathcal{P}_m$ satisfies $\Phi(w) \ge E_0 + \Delta - 2b = \Phi(A) + \Delta > \Phi(A) + b$ (since adding $-b$ on at most $4$ checkpoint nodes can lower any state outside $\mathcal{P}_m$ by at most $2b$ on bridges, and by at most $4b$ on $V_1$ where $\Phi_{\mathrm{unif}} \ge E_0 + 2\Delta$ so $\Phi \ge E_0 + 2\Delta - 4b = \Phi(A) + 2\Delta - 2b > \Phi(A) + b$!). Hence $\Phi(w) - \Phi(A) \ge b$ for every $w \notin \{A, B, C, D\}$. By `thm:agy-heterogeneous`(a),
$$\mathbb{P}^\infty(w) \le e^{2(2^n - 1)\gamma\delta}\mathbb{P}_\Phi(w) \le e^{2(2^n - 1)\gamma\delta} e^{-\gamma b}$$
for all $w \notin \{A, B, C, D\}$. Both when $\gamma\delta = \lambda\cdot 2^{-m}$ is fixed ($\gamma \to \infty$) and when $\delta \in (0, \frac{b}{3\cdot 2^n})$ is fixed ($\gamma \to \infty$, since $b - 2(2^n-1)\delta > b/3 > 0$), $\sum_{w \notin \{A, B, C, D\}} \mathbb{P}^\infty(w) \to 0$. Therefore $\mathbb{P}^\infty \to P_\lambda = \frac{1}{2(1+e^\lambda)}(\delta_A + e^\lambda\delta_B + e^\lambda\delta_C + \delta_D)$ (and $\to \frac{1}{2}\delta_B + \frac{1}{2}\delta_C$ in the fixed-$\delta$ regime where $\lambda = 2^m\gamma\delta \to \infty$).

**Step 2 (Cross-ratio identity for all Class 2 group posteriors).**
Let $\mathbb{P}_C(\pi) \propto (\prod_{u=1}^n \tilde{E}_u(\pi_u)) e^{-\gamma_C G_C(\pi)}$ be any Class 2 group posterior on the collective's slot model $\mathfrak{B}$ with arbitrary full-support product habits $\tilde{E}_u$, $\gamma_C \ge 0$, and arbitrary belief $q_C$ on $\eta_C$. Write $G_C(\pi) = \sum_{u=1}^n \pi_u [\psi^{(u)}_{\mathfrak{B}_u(1)}(q_C) - I_{q_C}(\eta_C; o_{\mathfrak{B}_u(1)})] + M_{q_C}(\pi)$. By `C2`(2), the 4 checkpoints have the rectangle structure $A = S_{\mathrm{low}} \cup \{u_1, w_1\}$, $B = S_{\mathrm{low}} \cup \{u_2, w_1\}$, $C = S_{\mathrm{low}} \cup \{u_1, w_2\}$, $D = S_{\mathrm{low}} \cup \{u_2, w_2\}$ with $u_1 = u_{m-2, a_{\mathrm{lo}}}$, $u_2 = u_{m-2, a_{\mathrm{hi}}}$, $w_1 = u_{m-1, 0}$, $w_2 = u_{m-1, 2}$. Every single-member term cancels identically in the alternating sum:
$$\ln \frac{\mathbb{P}_C(A)\mathbb{P}_C(D)}{\mathbb{P}_C(B)\mathbb{P}_C(C)} = -\gamma_C\bigl[M_{q_C}(A) + M_{q_C}(D) - M_{q_C}(B) - M_{q_C}(C)\bigr].$$
Set $T_1 = S_{\mathrm{low}} \cup \{u_1\}$ and $T_2 = S_{\mathrm{low}} \cup \{u_2\}$. By the chain rule (`eq:agy-chain`), $M_{q_C}(T_k \cup \{w_j\}) - M_{q_C}(T_k) = I_{q_C}(o_{\mathfrak{B}_{w_j}(1)}; o_{\mathfrak{B}(T_k)})$, so the $M_{q_C}(T_1)$ and $M_{q_C}(T_2)$ terms cancel identically:
$$M_{q_C}(A) - M_{q_C}(B) - M_{q_C}(C) + M_{q_C}(D) = \bigl[I_{q_C}(o_{w_1}; o_{T_1}) - I_{q_C}(o_{w_1}; o_{T_2})\bigr] - \bigl[I_{q_C}(o_{w_2}; o_{T_1}) - I_{q_C}(o_{w_2}; o_{T_2})\bigr].$$
- If $q_C \in \mathcal{Q}_{\mathrm{diag}}$ (independent coordinates $\eta_e$), then because $A, B, C, D$ are independent sets of $G_m$, no slot of $w_1$ or $w_2$ shares a coordinate with any slot of $T_1$ or $T_2$; hence all four mutual informations vanish and $\mathbb{P}_C(A)\mathbb{P}_C(D) = \mathbb{P}_C(B)\mathbb{P}_C(C)$ ($\kappa = 1$).
- For arbitrary (possibly correlated, non-Gaussian) $q_C$: under member $w_j$'s own belief $q_{w_j} = q_C^\ast \in \mathcal{Q}_{\mathrm{diag}}$, $I_{q_{w_j}}(o_{w_j}; o_{T_k}) = 0$, so $I_{q_C}(o_{w_j}; o_{T_k}) = -\mathcal{R}_{w_j}(T_k \cup \{w_j\}) \in [0, \sigma_{w_j}(q_C)]$. The difference of two numbers in $[0, \sigma_{w_j}(q_C)]$ has modulus at most $\sigma_{w_j}(q_C)$, so
$$\bigl|M_{q_C}(A) + M_{q_C}(D) - M_{q_C}(B) - M_{q_C}(C)\bigr| \le \sigma_{w_1}(q_C) + \sigma_{w_2}(q_C) \le 2\sigma_{\max}(q_C),$$
yielding $\mathbb{P}_C(A)\mathbb{P}_C(D) \ge \kappa\,\mathbb{P}_C(B)\mathbb{P}_C(C)$ with $\kappa := e^{-2\gamma_C\sigma_{\max}(q_C)} \in (0, 1]$.

**Step 3 (Elementary total-variation lower bound).**
Let $Q$ be any probability distribution on $\{0,1\}^n$ satisfying $Q(A)Q(D) \ge \kappa Q(B)Q(C)$ with $\kappa \in (0, 1]$, and set $u = Q(B)$, $v = Q(C)$, $x = \sqrt{u}$, $y = \sqrt{v}$, and $R = \kappa^{-1/4} \ge 1$. By AM-GM, $Q(A) + Q(D) \ge 2\sqrt{Q(A)Q(D)} \ge 2\sqrt{\kappa}\sqrt{uv}$. Since $0 < \sqrt{\kappa} \le 1$,
$$\sqrt{\kappa}(x + y)^2 = \sqrt{\kappa}(u + v) + 2\sqrt{\kappa}\sqrt{uv} \le u + v + Q(A) + Q(D) \le 1 \implies x + y \le R.$$
Now let $P = P_\lambda$ with $p := p_\lambda = \frac{e^\lambda}{2(1+e^\lambda)} \in (\frac{1}{4}, \frac{1}{2})$ (so $P(B) = P(C) = p$), and assume $R \le 2\sqrt{p}$. Then
$$\mathrm{TV}(P, Q) = \sum_\pi (P(\pi) - Q(\pi))_+ \ge (p - u)_+ + (p - v)_+ = 2p - \bigl[\min(p, x^2) + \min(p, y^2)\bigr].$$
Set $g(x, y) := \min(p, x^2) + \min(p, y^2)$ on $\{x, y \ge 0 : x + y \le R\}$. Since $g$ is nondecreasing in $(x, y)$, its maximum is attained on $x + y = R$. By symmetry assume $x \ge y$, i.e., $x \in [R/2, R]$. Since $R/2 \le \sqrt{p}$:
- For $x \in [R/2, \sqrt{p}]$: both $x \le \sqrt{p}$ and $R - x \le R/2 \le \sqrt{p}$, so $g(x, R-x) = x^2 + (R-x)^2$, which is convex in $x$ and maximized on $[R/2, \sqrt{p}]$ at the endpoint $x = \sqrt{p}$, giving $p + (R - \sqrt{p})^2$.
- For $x \in [\sqrt{p}, R]$: $x \ge \sqrt{p}$ and $R - x \le R - \sqrt{p} \le \sqrt{p}$, so $g(x, R-x) = p + (R-x)^2$, which is nonincreasing in $x$ and maximized at $x = \sqrt{p}$, again giving $p + (R - \sqrt{p})^2$.

Therefore $\max g = p + (R - \sqrt{p})^2$, and
$$\mathrm{TV}(P_\lambda, Q) \ge 2p - \bigl[p + (R - \sqrt{p})^2\bigr] = 2R\sqrt{p} - R^2 = R(2\sqrt{p} - R).$$
Setting $R = 1$ gives $2\sqrt{p_\lambda} - 1$ for every $q_C \in \mathcal{Q}_{\mathrm{diag}}$ (and any $\gamma_C \ge 0$, any $\tilde{E}_u$). For fixed $\delta \in (0, \frac{b}{3\cdot 2^7})$ at $m = 2$, $n = 7$, note $\frac{b}{3\cdot 2^7} = \frac{0.01}{384} < \frac{0.04}{2(6\cdot 4 - 8)} = 0.00125$, so both error bounds in Step 1 vanish as $\gamma \to \infty$, yielding $\lim_{\gamma\to\infty}\mathbb{P}^\infty = \frac{1}{2}\delta_B + \frac{1}{2}\delta_C$ ($p = \frac{1}{2}$) and $\lim_{\gamma\to\infty}\inf \mathrm{TV} \ge \sqrt{2} - 1$. $\square$

## Failed routes

### R1: Uniform-in-$\gamma$ bound via non-potential / Hodge-harmonic perturbation theory

- Tried: Checking whether removing the potential component ($\delta^\ast\mathcal{R} \equiv 0$) prevents large-$\gamma$ metastability amplification between degenerate minima of $\Phi$.
- Failed because: Even a pure cyclic perturbation $(\mathcal{R}_1, \mathcal{R}_2) = (+\delta, -\delta)$ shifts the activation barriers across the lower saddle $(1,1)$ in opposite directions for the two transition directions $(1,0) \to (1,1) \to (0,1)$ vs $(0,1) \to (1,1) \to (1,0)$, tilting the stationary ratio by $e^{+2\gamma\delta}$ regardless of $\delta^\ast\mathcal{R} = 0$ (`C1`, `C3`).
- Reopen if: An additional structural hypothesis excludes degenerate or near-degenerate minima / slow saddles (e.g., uniform log-Sobolev or Dobrushin condition independent of $\gamma$, which is already stronger than the contraction/spectral hypotheses of `thm:agy-heterogeneous`(b)–(c)).

### R2: Standard binary Gray code as an exponential-length accumulator

- Tried: Using a standard reflected binary Gray code on $\{0,1\}^m$ to accumulate work along an exponentially long 1D valley.
- Failed because: In a reflected Gray code, the orientation of the $(x_1, x_2)$ 4-cycle reverses whenever $x_3$ flips ($0 \to 1$), causing the discrete line integral $\sum \Delta\mathcal{R}$ to cancel instead of accumulate.
- Reopen if: Replaced by a unidirectional cyclic rotor coupled via an escapement (succeeded in `C2`–`C4`).

### R3: 4-state-gear-to-4-state-gear escapement and even-state locking for $m \ge 3$

- Tried: (a) Coupling two 4-state gears directly without odd buffer states; (b) locking gear $g$ at even states $\{0, 4\}$ when gear $g+1$ moves for $m \ge 3$.
- Failed because: (a) Created direct adjacency shortcuts $(0,0) \leftrightarrow (0,1)$ bypassing gear 1's half-turn; (b) allowed gear $g-1$ and gear $g+1$ to move simultaneously at $(0, 4, 0)$, creating degree-3 branch points (`other = 21` on $m = 3$).
- Reopen if: N/A — completely resolved by using 8-cycles for middle gears with **odd-state locking** $a_{\mathrm{lo}} = 1, a_{\mathrm{hi}} = 5$ (`C2`).

### R4: Class 3 violation via two comparable strict Nash equilibria on $\{0, 1\}^n$

- Tried: Seeking a binary deliberation chain putting mass $\frac{1}{2}$ on each of two comparable profiles $a < b$ in $\{0,1\}^n$ to violate log-submodularity (`prop:agy-performative-sign`) against all Class 3 models (even with invented slot models).
- Failed because: For every belief $q_i$, $I_{q_i}(o_i; o_j \mid o_S) \ge 0$, so $G_i(b) - G_i(b\setminus\{i\}) \ge G_i(a\cup\{i\}) - G_i(a)$ whenever $a < b$ and $i \in b \setminus a$; hence strict Nash equilibria on $\{0,1\}^n$ always form an antichain.
- Reopen if: Using non-Nash limit cycles or $|\mathcal{A}_i| \ge 3$ policies (`O2`).

## Open obligations

- [ ] O1 (sessions: 1): Determine the sharp optimal exponent $\theta^\ast \in [1/8, 1]$ in the exponential factor $|\mathcal{A}|^{\theta^\ast}\gamma\sigma_{\max}$ for exact Hodge-harmonic epistemic perturbations (between our explicit binary linear-Gaussian lower bound $\Theta(|\mathcal{A}|^{1/8})$ and the tree upper bound $|\mathcal{A}| - 1$ of `thm:agy-heterogeneous`(a)).
- [ ] O2 (sessions: 1): Settle whether a pure non-potential heterogeneous-belief deliberation family can remain bounded away from **Class 3** (all epistemic group posteriors allowing arbitrary invented slot models $\tilde{\mathfrak{B}}$ unrelated to the collective's physical slots $\mathfrak{B}$) at large $\gamma$ and small $\sigma_{\max}$.
- [ ] O3 (sessions: 1): Fresh-context reconstruction check of `C1`–`C4` by `@verifier-2`.

## Literature

| Claim | Source | Locator | Read depth | Date read | Verdict |
| --- | --- | --- | --- | --- | --- |
| Tree bound & near-potential games | Candogan, Ozdaglar, Parrilo (2013), cited in `s05_agency.tex` | `s05_agency.tex` line 70; `app05_agency.tex` line 164 | Secondary (manuscript citation only) | 2026-11-22 | Matches manuscript's reference to tree bound and Hodge decomposition |
| Markov chain tree theorem | Anantharam & Tsoucas (1989), cited in `app05_agency.tex` | `app05_agency.tex` line 164 | Secondary (used in `thm:agy-heterogeneous`(a)) | 2026-11-22 | Matches exact statement used in `app05_agency.tex` |

## Searches

| Query | Tool | Date | Not searched |
| --- | --- | --- | --- |
| none (pure construction/proof problem grounded in live manuscript `05_agency.tex` / `s05_agency.tex`) | N/A | 2026-11-22 | External literature on optimal snake-in-the-box / reconfiguration constants |

## Log

- 2026-11-22: Opened investigation on `open:agy-uniform-bound`. Falsified uniformity in $\gamma$ first on $n=2$ (`C1`), discovered the exact Hodge-harmonic pairwise linear-Gaussian $m$-gear train (`C2`), proved exponential-in-$n$ amplification $\Omega(2^{n/8}) = \Omega(|\mathcal{A}|^{1/8})$ via exact $C_{\mathrm{out}}$-factorization of the Markov chain tree theorem against both $\mathbb{P}_\Phi$ (`C3`) and all Class 2 group posteriors (`C4`), and ran two-channel verification with planted-error negative controls (`open_agy_uniform_bound-checks/verify_uniform_bound.py`, exit code 0).
- 2026-11-22 (Reporting gate self-audit):
  1. Literally asked: find a bound uniform in $\gamma$ and polynomial in $n$ for weak redundancy disagreement, OR a family showing the $|\mathcal{A}|-1$ factor of the tree bound is needed for perturbations without a potential part. Intended: settle whether weak pure non-potential redundancy disagreement admits a uniform/polynomial bound or genuinely suffers exponential-in-$n$ / $\gamma$-unbounded blowup. Our result answers the intended question decisively in the negative (refuting any uniform-in-$\gamma$ or polynomial-in-$n$ bound for exact Hodge-harmonic linear-Gaussian perturbations).
  2. Two ways a draft could satisfy the letter while missing the point: (a) using a perturbation with a hidden potential part (excluded by proving exact Hodge harmonicity $\delta^\ast\mathcal{R}\equiv 0$ on all $2^n$ states); (b) only comparing against fixed-habit $\mathbb{P}_\Phi$ while free product habits absorb the shift (excluded by `C4`, which proves $\mathrm{TV} \ge 2\sqrt{p_\lambda}-1 \to \sqrt{2}-1$ against all Class 2 group posteriors with arbitrary product habits and precision).
  3. Strongest referee objection: (i) What if $q_C$ correlates distinct coordinate blocks? Answered explicitly in `C4`(2) via the trade-off bound $R(2\sqrt{p_\lambda}-R)$ with $R = e^{\frac{1}{2}\gamma_C\sigma_{\max}(q_C)}$. (ii) Our factor is $|\mathcal{A}|^{1/8} = \Theta(2^{n/8})$ rather than $|\mathcal{A}| - 1 = 2^n - 1$: disclosed honestly in Verdict Summary and `O1`.
  4. Speculative claims: none; citations are strictly to the live manuscript; all numerical checks executed and captured. Three ways it could still be wrong, excluded by checks: (a) hidden shortcuts or spurious edges in $V_0$ (excluded by inductive proof + exhaustive verification on all $128$ and $32768$ states for $m=2, 3$); (b) Gaussian preferences unable to realize negative $c_u$ (excluded by explicit scale $\lambda$ and Channel 1 full-LG computation); (c) switching bridges at $-b$-bonus nodes canceling the $V_0 \to V_1$ barrier (excluded by choosing $b = \Delta/10$, leaving $\Delta - 6b = 0.4\Delta > 0$).
  5. Remaining obligations: `O1` (sharp exponent $\theta^\ast \in [1/8, 1]$), `O2` (Class 3 with invented slots), `O3` (fresh-context verification by `@verifier-2`).
- Next action: Write cleaned write-up in scratch folder, lint record with `check_record.py`, and hand off to `@verifier-2` for fresh-context reconstruction check.
