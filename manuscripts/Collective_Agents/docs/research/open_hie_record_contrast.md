# Open Problem `open:hie-record-contrast`: Contrast with Record Nodes

- Status: active
- Opened: 2026-11-22
- Updated: 2026-11-22
- Sessions: 1

## Target

- Locked statement: Characterize the record noises for which the precision with a global record node is diffusive, for $\delta>0$ and with outsiders, where \cref{obs:hie-record-window} found only the reversible value; decide whether a contrast for records can be defined in the $\mathcal Q^{-1}$-weighted norm of \cref{rem:hie-memory-absent} without breaking the size bound; and declare a comparison medium for populations of agents and record nodes. (From `sections/s10b_hierarchy.tex`, `open:hie-record-contrast`, lines 304–306; also covering the agents' marginal precision with the record marginalized and discrete-time comparison per `prop:hie-record-contrast`.)
- Falsifier: Any admissible continuous-time instance with $\cut(C) > 0$ and $q_z > q_{\mathrm{rev}}$ whose stationary precision $\Pi(q_z)$ is diffusive; any $\delta > 0$ or $\cut(C) > 0$ instance with $q_z = 0$ whose $\Pi(0)$ is diffusive; any closed instance violating the exact interval $[\kappa_{\min}^{\mathrm{closed}}, \kappa_{\max}^{\mathrm{closed}}]$; any weighted diffusive medium violating the weighted size bound of C6; or any finite region of a translation-invariant fibered lattice $\Z^D \times \{A, Z\}$ exceeding the uniform baseline bound of C7(3).
- May assume: The continuous-time global record model `eq:hie-record` (`10b_hierarchy.tex`) and `prop:hie-record-contrast` (`s10b_hierarchy.tex`) with symmetric couplings $a_{ij} = a_{ji} \ge 0$, uniform agent leak $\varepsilon > 0$, read weight $\beta > 0$, write weight $\omega > 0$, record decay $\delta \ge 0$, noise $\mathcal Q = \diag(q I_N, q_z)$ ($q > 0, q_z \ge 0$), $n = |C| \ge 2$; the discrete-time model `def:fw-record-model` and `prop:hie-record-contrast(d)`; and the definitions of diffusivity (`eq:col-diffusive`), contrast (`def:col-contrast`), baseline (`def:col-baseline`), and size bound (`thm:col-contrast-size`) in `04_collectives.tex`.
- Must not assume: That $q_z = q_{\mathrm{rev}}$ is the unique diffusive noise with outsiders (must be tested and falsified where false); that a noiseless record always leaves the diffusive class; or that a closed collective's $2\times 2$ reduction carries over to open populations with outsiders.
- Alternative forms: Exact necessary and sufficient conditions for closed collectives and for $q_z = 0$, non-perturbative global upper barrier for $q_z > q_{\mathrm{rev}}$ with outsiders, non-perturbative rigidity for symmetric uncoupled pairs, and exact first-order necessary/sufficient criteria + explicit witnesses for $q_z < q_{\mathrm{rev}}$ with outsiders and for $\Pi_{\mathrm{marg}}(q_z)$, together with exact answers to the weighted-norm size bound and typed comparison medium clauses.
- Test instance: `obs:hie-record-window` and `chk:hie-record-precision`: ring of 8 members ($a = 1, \varepsilon = 0.02, \beta = 0.2, \omega = 0.1, q = 1, q_{\mathrm{rev}} = 0.0625$), closed or joined to a ring of 8 outsiders by cross-couplings $c = 0.05$ between matched pairs; must reproduce $r(C') = 12.950139$ at $q_z = q_{\mathrm{rev}}, \delta = 0$, and for closed ring at $\delta = 0.01$ must place the upper diffusivity boundary strictly between $2 q_{\mathrm{rev}}$ and $4 q_{\mathrm{rev}}$ (exact value $2.65 q_{\mathrm{rev}}$).
- Out of scope: Non-symmetric agent couplings $a_{ij} \neq a_{ji}$ (where no reversible $q_{\mathrm{rev}}$ exists), multiple interacting global records with distinct decay/noise ratios beyond the typed comparison medium definition, and endogenous attention dynamics (`open:col-non-diffusive`).
- Reading chosen: All three clauses of `open:hie-record-contrast` in the live manuscript notation: (1) full characterization of the diffusive set $\mathcal D = \{q_z \ge 0 : \Pi(q_z) \text{ is diffusive}\}$ (and marginal precision $\Pi_{\mathrm{marg}}(q_z)$, plus discrete-time comparison) for both closed and open ($\cut(C) > 0$) populations and all $\delta \ge 0$, without silently assuming $C$ is non-complete or symmetric; (2) explicit definition and exact size bound (plus failure modes) for the $\mathcal Q^{-1}$-weighted contrast $r_W$; (3) explicit typed comparison medium extending `def:col-baseline` with proved whole-population exclusion and finite lattice baseline.

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| Continuous-time Lyapunov eq. | $M\Sigma + \Sigma M^\top = 2\mathcal Q$, $\mathcal Q = \diag(qI_N, q_z)$ | $q_{\mathrm{rev}} = \omega q/(n\beta) = 0.0625$ on ring of 8 ($\beta=0.2, \omega=0.1, q=1$) |
| Diffusive precision (`eq:col-diffusive`) | $\Pi \succ 0$, $\Pi_{uv} \le 0$ ($u \neq v$), $(\Pi\one)_u \ge 0$ | Ring8+Ring8 ($c=0.05, q_z=q_{\mathrm{rev}}, \delta=0$): diffusive, $r(C') = 12.950139$ |
| Closed $\delta > 0$ upper threshold | $\kappa_{\max}^{\mathrm{closed}} = 1 + \delta T/(\varepsilon\omega)$, $T=\varepsilon+\beta+\omega+\delta$ | Closed ring of 8 at $\delta = 0.01$: $T = 0.33$, $\kappa_{\max}^{\mathrm{closed}} = 2.65$ |
| Symmetrized coordinates | $D = \mathcal Q_{\mathrm{rev}}^{1/2}$, $\mathbf d = D^{-1}\one$, $S = D^{-1} M D \succ 0$, $\tilde\Pi = D\Pi D$, $\eta = q_z/q_{\mathrm{rev}} - 1$ | At $\eta = 0$: $\tilde\Pi = S$, $S_{iz} = -\sqrt{\beta\omega/n}$ ($i \in C$), $S_{oz} = 0$ ($o \in O$), $S\mathbf d = D\Pi_{\mathrm{rev}}\one$ |
| $\mathcal Q^{-1}$-weighted inner product | $W = \mathcal Q^{-1} = \diag(w_v)$, $w_v = q_v^{-1}$, $\langle f,g\rangle_W = f^\top W g$ | Global record at $q_z = q_{\mathrm{rev}}$: $w_i = 1/q$, $w_z = n\mathcal R/q$, $W(C') = n(1+\mathcal R)/q$ |

## Claims

### C1: Closed collective exact precision and diffusivity interval

- Statement: For a closed collective $V = C$ ($|C| = n \ge 2$, or $\cut(C) = 0$) with symmetric $a_{ij} \ge 0$, $\varepsilon, \beta, \omega, q > 0$, $\delta \ge 0$, $q_z = \kappa q_{\mathrm{rev}} \ge 0$, $T = \varepsilon+\beta+\omega+\delta$, $D_2 = \varepsilon(\omega+\delta)+\beta\delta$, $P(\kappa) = \beta\omega(\kappa-1)^2 + T^2\kappa$, and $a_{\min} = \min_{i\neq j \in C} a_{ij}$: (1) $\Pi(\kappa)$ has the exact closed form $\Pi_{CC} = q^{-1}((\varepsilon+\beta)I_n + L_C) + \frac{\beta\omega(1-\kappa)[(\omega+\delta)+\kappa(\varepsilon+\beta)]}{nqP(\kappa)}\one_n\one_n^\top$, $\Pi_{Cz} = -\frac{\beta T[(\omega+\delta)+\kappa(\varepsilon+\beta)]}{qP(\kappa)}\one_n$, $\Pi_{zz} = \frac{n\beta T[(\omega+\delta)^2+D_2+\kappa\beta\omega]}{\omega q P(\kappa)}$, with member row sums $\frac{T[\kappa(\varepsilon T+\beta\delta)-\beta\delta]}{qP(\kappa)}$ and record row sum $\frac{n\beta T[\delta T+(1-\kappa)\varepsilon\omega]}{\omega q P(\kappa)}$; (2) $\Pi(\kappa)$ is diffusive iff $\kappa \in [\kappa_{\min}^{\mathrm{closed}}, \kappa_{\max}^{\mathrm{closed}}]$, where $\kappa_{\max}^{\mathrm{closed}} = 1 + \frac{\delta T}{\varepsilon\omega}$, $\kappa_{\min}^{\mathrm{closed}} = 1$ if $a_{\min} = 0$, and $\kappa_{\min}^{\mathrm{closed}} = \max\{\frac{\beta\delta}{\varepsilon T+\beta\delta}, \kappa_{\mathrm{off}}\} < 1$ if $a_{\min} > 0$ ($\kappa_{\mathrm{off}} = 0$ if $n a_{\min} \ge \omega+\delta$, else the unique root in $(0,1)$ of $\beta\omega(1-\kappa)[(\omega+\delta)+\kappa(\varepsilon+\beta)] = n a_{\min} P(\kappa)$), so at $q_z = 0$, $\Pi(0)$ is diffusive iff $\delta = 0$ and $a_{\min} \ge \omega/n$ (refining the unqualified prose on line 158 of `s10b_hierarchy.tex`); (3) the members' marginal precision $\Pi_{\mathrm{marg}}(\kappa) = (\Sigma_{CC}(\kappa))^{-1}$ is diffusive for every $\kappa \ge 0$, $\delta \ge 0$, and symmetric $a_{ij} \ge 0$.
- Status: proved
- Review: self
- Evidence: full proof in cleaned write-up (scratch); two-channel verification in `open_hie_record_contrast-checks/verify_hie_record_contrast.py` and captured output `open_hie_record_contrast-checks/verify_hie_record_contrast.txt` (SymPy exact symbolic residuals = 0; 200 random closed graphs max rel err $4.963 \times 10^{-12}$; exact SymPy witness W1 $K_2$ at $\delta=0, q_z=0$ diffusive with $\Pi_{01}=-19/20, (\Pi\one)_0=0, (\Pi\one)_z=4/5$; closed ring of 8 at $\delta=0.01$ gives exact $\kappa_{\max}^{\mathrm{closed}} = 2.65$; planted-error negative control caught).
- Depends on: none

### C2: Non-perturbative symmetrized identity and universal upper barrier ($q_z > q_{\mathrm{rev}}$)

- Statement: For any finite agent population $(V, a)$ with $C \subseteq V$ ($|C| = n \ge 2$), $a_{ij} = a_{ji} \ge 0$, $\varepsilon, \beta, \omega, q > 0$, $\delta \ge 0$, and $\eta = q_z/q_{\mathrm{rev}} - 1 \in [-1, \infty)$: (1) $R(\kappa) := S - \tilde\Pi(\kappa)$ satisfies $R\tilde\Pi + \tilde\Pi R = 2\eta(\tilde\Pi e_z)(\tilde\Pi e_z)^\top$ and hence $S - \tilde\Pi(\kappa) = 2\eta\int_0^\infty (\tilde\Pi e^{-t\tilde\Pi} e_z)(\tilde\Pi e^{-t\tilde\Pi} e_z)^\top\,\mathrm dt$; (2) whenever $\cut(C) > 0$ (at least one coupled outsider) and $\delta \ge 0$, for every $q_z > q_{\mathrm{rev}}$, $\Pi(q_z)$ is not diffusive (indeed not an M-matrix: it has at least one strictly positive off-diagonal entry), so $\mathcal D \subseteq [0, q_{\mathrm{rev}}]$; (3) whenever $\delta = 0$ (closed or open) and $q_z > q_{\mathrm{rev}}$, $\Pi(q_z)$ is not diffusive.
- Status: proved
- Review: self
- Evidence: full non-perturbative integration-by-parts proof in cleaned write-up (scratch); two-channel check in `open_hie_record_contrast-checks/verify_hie_record_contrast.py` and `open_hie_record_contrast-checks/verify_hie_record_contrast.txt` (Lyapunov identity max rel err $4.816 \times 10^{-13}$; 1200/1200 random open instances above $q_{\mathrm{rev}}$ have strictly positive off-diagonal entry; planted-error negative control dropping factor 2 caught with residual $1.4246 \times 10^{-2}$).
- Depends on: none

### C3: Exact noiseless-record characterization ($q_z = 0$)

- Statement: Under the standing continuous-time hypotheses ($\varepsilon, \beta, \omega, q > 0$, $\delta \ge 0$, $a_{ij} = a_{ji} \ge 0$, $n \ge 2$), at $q_z = 0$: (1) $(M\Sigma(0))_{zz} = 0$, $(M\Sigma(0))_{iz} > 0$ for all $i \in V_0$, $(M\Sigma(0))_{iz} = 0$ for all $i \in V \setminus V_0$, and the row sums $r = \Pi(0)\one$ obey $\sum_{i \in V_0} r_i (M\Sigma(0))_{iz} = -\delta$; (2) $\Pi(0)$ is diffusive if and only if $\cut(C) = 0$, $\delta = 0$, and $a_{ij} \ge \omega/n$ for all $i \neq j \in C$. In particular, whenever $\delta > 0$ or $\cut(C) > 0$, the noiseless record is never diffusive (even on a complete graph).
- Status: proved
- Review: self
- Evidence: full proof in cleaned write-up (scratch); checked in `open_hie_record_contrast-checks/verify_hie_record_contrast.py` and `open_hie_record_contrast-checks/verify_hie_record_contrast.txt` (300/300 random open instances obey the row-sum identity and fail diffusivity at $q_z = 0$; exact SymPy rational witnesses W1 closed $K_2$ diffusive and W2 open $K_3$ non-diffusive at $q_z = 0$ with $r_0 \approx -0.002849$ at $\delta=0$ and $-0.204279$ at $\delta=1/20$).
- Depends on: C1, C2

### C4: Below $q_{\mathrm{rev}}$ with coupled outsiders — symmetric rigidity vs. left-sided diffusivity windows

- Statement: Assume $\cut(C) > 0$ ($O_0 \neq \emptyset$) and let $Y$ solve $SY + YS = 2e_z e_z^\top$, with $\mathbf d = D^{-1}\one$. (1) If there exist $i \neq j \in V_0$ with $a_{ij} = 0$ in the same orbit of $\mathrm{Aut}(V, a, C)$ (covering every open instance of `obs:hie-record-window`), then $\Pi_{ij}(q_z) = -\frac{2\eta}{q}\int_0^\infty (w_i'(t))^2\,\mathrm dt > 0$ for every $0 \le q_z < q_{\mathrm{rev}}$, and hence (with C2) $\Pi(q_z)$ is diffusive iff $q_z = q_{\mathrm{rev}}$ for all $\delta \ge 0$. (2) Locally near $q_{\mathrm{rev}}$, $(SYS)_{oz} < 0$ for all $o \in O_0$ and $(SYS\mathbf d)_z > 0$; thus $(SYS)_{uv} < 0$ for all $\{u, v\} \in E_0^c$ is sufficient, and $(SYS)_{uv} \le 0$ for all $\{u, v\} \in E_0^c$ is necessary, for a left-sided diffusivity window $[q_{\min}, q_{\mathrm{rev}}]$ ($0 < q_{\min} < q_{\mathrm{rev}}$) to exist. (3) In particular, every complete graph on $V_0$ ($E_0^c = \emptyset$, e.g. $K_3$) has a nondegenerate left-sided diffusivity window $[q_{\min}, q_{\mathrm{rev}}]$ for every $\delta \ge 0$ (refuting any conjecture that $q_z = q_{\mathrm{rev}}$ is the unique diffusive noise with outsiders), and non-complete graphs can also possess one (exact rational witness W3 on $K_4 \setminus \{(0,3),(1,3)\}$ with $C = \{0,1\}, O = \{2,3\}$, strictly diffusive at $q_z = \frac{9}{10}q_{\mathrm{rev}}$).
- Status: proved
- Review: self
- Evidence: full proof in cleaned write-up (scratch); two-channel verification in `open_hie_record_contrast-checks/verify_hie_record_contrast.py` and `open_hie_record_contrast-checks/verify_hie_record_contrast.txt` (exact SymPy rational witnesses W2 on $K_3$ at $\delta=0$ and $\delta=1/20$, W3 on $K_4 \setminus \{(0,3),(1,3)\}$ at $\delta=8$ with $\Pi_{03} = \Pi_{13} = -4.271961 \times 10^{-5} < 0, \min r = +0.129556 > 0$; exact integral identity on $0\text{--}2\text{--}1$ verified to $6.94 \times 10^{-18}$; planted-error sign flip caught with error $1.8012 \times 10^{-2}$).
- Depends on: C2, C3

### C5: Agents' marginal precision $\Pi_{\mathrm{marg}}(q_z)$ with outsiders, and discrete-time contrast

- Statement: (1) For continuous-time coupled outsiders ($\cut(C) > 0$), $\Pi_{\mathrm{marg}}(q_{\mathrm{rev}})$ has strictly positive agent row sums and strictly negative off-diagonal entries on $V_0$ except on $E_{\mathrm{ext}}^c = \{\{u, v\} \in E_0^c : \{u, v\} \not\subset C\}$, where $\left.\frac{\mathrm d}{\mathrm d\eta}\Pi_{\mathrm{marg}, uv}\right|_{\eta=0} = -\frac{1}{q}(M_{\mathrm{schur}} Y_{VV} M_{\mathrm{schur}})_{uv}$. Hence whenever $E_{\mathrm{ext}}^c = \emptyset$ (even if $C$ has missing internal edges, e.g. $0\text{--}2\text{--}1$ where joint $\Pi$ is diffusive only at $q_{\mathrm{rev}}$), $\Pi_{\mathrm{marg}}(q_z)$ is strictly diffusive on a two-sided open interval $(q_{\min}^{\mathrm{marg}}, q_{\max}^{\mathrm{marg}}) \ni q_{\mathrm{rev}}$ (potentially including $q_z = 0$); when $E_{\mathrm{ext}}^c$ contains two edges of opposite derivative sign (as in `obs:hie-record-window` open16, where $\partial_\eta\Pi_{\mathrm{marg}, 0,9} = +7.445 \times 10^{-4}$ and $\partial_\eta\Pi_{\mathrm{marg}, 8,10} = -4.221 \times 10^{-4}$), $\Pi_{\mathrm{marg}}$ fails on both sides of $q_{\mathrm{rev}}$ locally. (2) In discrete time (`prop:hie-record-contrast(d)`), range-two reversible precision gives $\Pi_{\mathrm{rev}, oz}^{\mathrm{disc}} = -\frac{\beta}{q}\sum_{i \in C} a_{io} < 0$ for distance-1 outsiders and strictly positive record leak even at $\delta = 0$, permitting a two-sided diffusivity window around $q_{\mathrm{rev}}$ (including $q_z = 0$ and $q_z > q_{\mathrm{rev}}$, exact rational witness W6a on discrete $K_3$); conversely, any outsider $o \in O_0$ at distance $\ge 2$ from $C$ with $U = D^{-1} W D \succeq 0$ satisfies $\Pi_{\mathrm{rev}, oz}^{\mathrm{disc}} = 0$ and $\left.\frac{\mathrm d}{\mathrm d\eta}\Pi_{oz}^{\mathrm{disc}}\right|_{\eta=0} > 0$ strictly (summation by parts; exact rational witness W6b on $0\text{--}1\text{--}2\text{--}3$), restoring the local upper barrier.
- Status: proved
- Review: self
- Evidence: full proof in cleaned write-up (scratch); verified in `open_hie_record_contrast-checks/verify_hie_record_contrast.py` and `open_hie_record_contrast-checks/verify_hie_record_contrast.txt` (exact SymPy rational witnesses W4 on $0\text{--}2\text{--}1$ diffusive at $q_z/q_{\mathrm{rev}} \in \{0, 1/2, 1, 2\}$ and non-diffusive at $10$; open16 opposite derivatives; exact SymPy rational discrete witnesses W6a on $K_3$ and W6b on $0\text{--}1\text{--}2\text{--}3$; negative control rejecting continuous-time upper barrier in discrete time).
- Depends on: C4

### C6: $\mathcal Q^{-1}$-weighted contrast $r_W(C')$ and its exact weighted size bound

- Statement: On any diffusive positive definite precision $\Pi = \diag(\varepsilon^\Pi) + L^\Pi$ with diagonal noise $\mathcal Q = \diag(q_v)$ and weights $W = \mathcal Q^{-1}$, defining $r_W(C') = \xin^W(C')/\xout^W(C')$ in the $W$-weighted norm: (1) for $C' = C \cup \{z\}$ at $q_z = q_{\mathrm{rev}}$, $r_W(C') = \frac{(1+\mathcal R)\min\{\varepsilon+\beta+\lambda_2(L_C),\, \beta+\omega + (\varepsilon\mathcal R+\delta)/(1+\mathcal R)\}}{\varepsilon + \mathcal R\delta + \cut(C)/n}$, restoring the memory factor $1+\mathcal R$ of `rem:hie-memory-absent`; (2) $r_W(C')$ obeys the exact weighted size bound $r_W(C') \le \frac{\varepsilon_{\max}^M(C')}{\bar\varepsilon_{C'}^W} + \frac{\varsigma_{W,d}^2}{2\bar\varepsilon_{C'}^W \Var_{W,d}(C')}$ (and its metric analogue), reducing to `thm:col-contrast-size` when $W = q^{-1}I$ and bounding $\Var_{W,d}(C')$ whenever $r_0 > \varepsilon_{\max}^M(C')/\bar\varepsilon_{C'}^W$; (3) for a global record at $\delta < \varepsilon$, the admissibility floor $\varepsilon_{\max}^M/\bar\varepsilon_{C'}^W = (1+\mathcal R)\varepsilon/(\varepsilon+\mathcal R\delta)$ grows up to $1+\mathcal R$, placing $x_z = \bar x_C$ dilutes $\Var_{W,d}(C') = \Var_d(C)/(1+\mathcal R)$ (dropping this dilution breaks the bound even at $\delta = \varepsilon$), and the global coupling forces $\varsigma_{W,d}^2 \ge \beta\Var_d(C)$ (unbounded extent for global hubs), whereas local finite-range records ($\ell_r = 0, x_{z_i} = x_i$) preserve finite $\varsigma_{W,d}^2$ and $\Var_{W,d}(C') = \Var_d(C)$.
- Status: proved
- Review: self
- Evidence: full proof in cleaned write-up (scratch); checked in `open_hie_record_contrast-checks/verify_hie_record_contrast.py` and `open_hie_record_contrast-checks/verify_hie_record_contrast.txt` (100 random embedded systems $r_W$ formula max rel err $4.353 \times 10^{-14}$ and weighted size bound max ratio $0.3092$; global uncoupled $n=100$ and local path $n=30$ instances; planted-error negative control replacing $\Var_W$ by $\Var_C$ violates bound $11.00 > 6.0$ while obeying true weighted bound $506.0$).
- Depends on: none

### C7: Typed comparison medium for populations of agents and record nodes

- Statement: Declaring the typed comparison medium $\Pi_{\mathrm{hom}}$ on $V' = V \cup Z$ by averaging agent leaks on $V$ and record leaks on $Z$ separately and averaging couplings within each declared type-class $(V,V), (V,Z), (Z,Z)$ under fibered-lattice / global-record, typed-graph, or two-type-exchangeable clauses: (1) reduces identically to `def:col-baseline` when $Z = \emptyset$; (2) satisfies whole-population exclusion $r(V'; \Pi) \le r(V'; \Pi_{\mathrm{hom}}) \le \bar r_{\mathrm{hom}}$ and $r_W(V'; \Pi) \le r_W(V'; \Pi_{\mathrm{hom}}) \le \bar r_{W,\mathrm{hom}}$ whenever a type-preserving symmetry group $\mathsf G \le \mathrm{Sym}(V) \times \mathrm{Sym}(Z)$ acts transitively on $V$, $Z$, and each averaged edge class; (3) has a uniformly finite Euclidean baseline $\bar r_{\mathrm{hom}} \le \max\{3,\, 6\Delta_{\max}/a_{AZ}(0),\, 3^{(D-1)/D}2^{(D+2)/D}\Delta_{\max}/(D a_{\mathrm{nn}}),\, 3^{(D-1)/D}2^{2+2/D}\varsigma^2/a_{\mathrm{nn}}\}$ on any translation-invariant fibered lattice $\Z^D \times \{A, Z\}$, uniformly in $(\varepsilon_A, \varepsilon_Z) \in [0, \infty)^2$; (4) classifies the two-rings-of-8 + global-record instance of `chk:hie-record-precision` at $\varepsilon=0.02$ as below baseline ($12.9501 < 27.6403$), and on the 9-node two-4-cycles + global-record analogue (exhaustive over all 502 regions) identifies $C' = C \cup \{z\}$ as a collective at $\varepsilon = 0.20$ ($10.2000 > 9.9375$, significance $1.0264$) and $\varepsilon = 0.50$ ($4.7727 > 4.1750$, significance $1.1432$).
- Status: proved
- Review: self
- Evidence: full proof in cleaned write-up (scratch); checked in `open_hie_record_contrast-checks/verify_hie_record_contrast.py` and `open_hie_record_contrast-checks/verify_hie_record_contrast.txt` (100 random typed populations whole-population exclusion Euclidean & weighted; 300 random subsets on $\Z \times \{A, Z\}$ max ratio $0.0156$ against $B=64.00$; exhaustive 502-region 9-node baseline; negative control showing naive single-type leak pooling alters an already-homogeneous medium by $\|\Delta\Pi\|_F = 0.0894$).
- Depends on: C6

## Failed routes

### R1: Assuming $q_z = q_{\mathrm{rev}}$ is universally the unique diffusive noise whenever $\cut(C) > 0$

- Tried: Extrapolating `obs:hie-record-window` to conjecture $\mathcal D = \{q_{\mathrm{rev}}\}$ for all graphs with coupled outsiders.
- Failed because: Falsify-first testing on complete graph $K_3$ ($C=\{0,1\}, O=\{2\}$) and non-complete $K_4 \setminus \{(0,3),(1,3)\}$ showed strictly diffusive precisions on a nondegenerate left-sided interval $[q_{\min}, q_{\mathrm{rev}}]$ for both $\delta = 0$ and $\delta > 0$, because $(SYS)_{oz} < 0$ pushes $\Pi_{oz}$ strictly negative below $q_{\mathrm{rev}}$ while existing edges already start strictly negative.
- Reopen if: Never as a universal statement; replaced by the exact split in C2 (universal upper barrier $q_z \le q_{\mathrm{rev}}$) + C4 (rigidity for symmetric uncoupled pairs vs. left-sided window criterion $(SYS)_{uv} < 0$ on $E_0^c$).

### R2: Assuming $(SYS)_{ij} > 0$ for all direct neighbors $i, j$ of $z$ in an arbitrary symmetric M-matrix $S$

- Tried: Proving $(SYS)_{ij} > 0$ for arbitrary uncoupled $i, j \in C$ by viewing $S$ as a general symmetric M-matrix with $S_{iz} < 0, S_{jz} < 0$.
- Failed because: Random search over general symmetric M-matrices with unequal couplings $S_{iz} \neq S_{jz}$ immediately produced $214/5000$ counterexamples where $(SYS)_{ij} < 0$ (e.g. when $S_{0z} \ll S_{1z}$ so node $0$ is driven predominantly through a two-hop indirect path from $1$).
- Reopen if: One exploits the exact uniform-coupling and uniform-leak structure of the global record model ($S_{iz} = -\sqrt{\beta\omega/n}$ for all $i \in C$ and uniform $\varepsilon$), where 10,000+ numerical and exact SymPy tests found zero negative cases of $(SYS)_{ij}$ ($i, j \in C$) — left as an explicit open obligation O1 rather than claimed without proof.

### R3: Using a single-site midpoint local record to claim unweighted size-bound blowup at fixed $r_0 > 1$

- Tried: Attaching one record of weight $w_z = \mathcal R$ to the midpoint of an isolated path of $n$ agents to show $r_W(C')$ stays above $1 + \mathcal R$ as $n \to \infty$.
- Failed because: Numerical testing at $n = 51, 101$ showed $r_W(C')$ drops below $1$ ($0.9672, 0.5968$) since the record-vs-path mode has rate $\sim \omega < \varepsilon$ when $w_z = \mathcal R$ is fixed while $W(C) = n \to \infty$.
- Reopen if: Never needed; C6(3) instead establishes the exact obstructions via the global-record formula, the exact $C=\{0,1\}$ star witness where dropping the $1+\mathcal R$ dilution violates the bound ($11 > 6$), and the exact leak-heterogeneity floor $(1+\mathcal R)\varepsilon/(\varepsilon+\mathcal R\delta)$.

## Open obligations

- [ ] O1 (sessions: 1): Decide whether in the continuous-time global record model with uniform agent leak $\varepsilon$ and uniform record couplings ($S_{iz} = -\sqrt{\beta\omega/n}$ for all $i \in C$), an asymmetric graph with an uncoupled member pair $a_{ij} = 0$ ($i, j \in C$) can ever satisfy $(SYS)_{ij} \le 0$ or admit a diffusive $\Pi(q_z)$ at some $0 < q_z < q_{\mathrm{rev}}$ (10,000+ numerical trials and extreme cluster-dilution SymPy checks found zero counterexamples, while C4(1) settles all automorphism-symmetric pairs non-perturbatively).
- [ ] O2 (sessions: 1): Fresh-context proof verification of C1–C7 by `@verifier-2` from `cleaned_writeup_hie_record.md` and update of `Review:` / `Check:` fields.

## Literature

| Claim | Source | Locator | Read depth | Date read | Verdict |
| --- | --- | --- | --- | --- | --- |
| Live model & open problem | `sections/s10b_hierarchy.tex` | `prop:hie-record-contrast`, `rem:hie-memory-absent`, `ex:hie-noiseless-record`, `obs:hie-record-window`, `open:hie-record-contrast` | full | 2026-11-22 | matched |
| Live SDE & drift results | `sections/10b_hierarchy.tex`, `sections/app10b_hierarchy.tex`, `sections/chk10b_hierarchy.tex` | `eq:hie-record`, `chk:hie-record-precision` | full | 2026-11-22 | matched |
| Diffusivity, contrast, baseline, size bound | `sections/04_collectives.tex`, `sections/s04_collectives.tex`, `sections/app04_collectives.tex` | `eq:col-diffusive`, `def:col-contrast`, `def:col-baseline`, `thm:col-contrast-size`, `thm:col-lattice-contrast`, `open:col-records-baseline` | full | 2026-11-22 | matched |
| Discrete record model | `sections/02_framework.tex` | `def:fw-record-model` | full | 2026-11-22 | matched |

## Searches

| Query | Tool | Date | Not searched |
| --- | --- | --- | --- |
| none (internal manuscript open problem; no external novelty claim made) | n/a | 2026-11-22 | external literature not searched |

## Log

- 2026-11-22: Opened investigation of `open:hie-record-contrast`. Falsified naive extrapolation of `obs:hie-record-window` (discovered left-sided diffusivity windows on complete and non-complete graphs with outsiders, and closed-clique diffusivity at $q_z = 0, \delta = 0$). Proved C1–C7, wrote two-channel verification script `open_hie_record_contrast-checks/verify_hie_record_contrast.py` with captured output `verify_hie_record_contrast.txt` (all checks and negative controls pass), wrote `cleaned_writeup_hie_record.md`. Next action: lint record with `check_record.py` and hand off to `@verifier-2` for fresh-context proof check.
