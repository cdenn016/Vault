<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 10 — independent mechanism audit (Fable pass): horizontal-defect Fisher comparison and configuration coarse-graining

**Terminal status of this pass: `INCONCLUSIVE`** (Section 6). Mechanism I is
verified in full, with one displayed identity in the prior bundle evidence
corrected and one ledger clause refuted as worded. Mechanism II's reported
counterexample is reproduced exactly (ratio $2/(1+\delta)^2$, $=1.96059\ldots$
at $\delta=10^{-2}$), a nonempty noncircular finite-dimensional configuration
construction is supplied together with the proved exclusion under which
averaging *is* contractive, and two of the six in-scope ledger claims remain
`OPEN`, which blocks an affirmative terminal for the audited claim set.

---

## 0. Provenance, binding, and independence boundary

### 0.1 Revision binding

Branch `codex/gauge-vfe-rg-task10-pullbacks-20260804`; session-start HEAD
`02d5d8f542cba2d92c6a430483b62155dd5f2db4` ("docs: derive RG modes beta
functions and fixed objects"), with the four Task 10 evidence files untracked.
Git invocations were unavailable inside this sandboxed pass (read-only
`git rev-parse` was denied), so the revision is bound two ways: by the harness
snapshot above, and — decisively — by byte-exact SHA-256 agreement of **every**
shared input below with the digests recorded at base `02d5d8f5…` by the three
route reports. No input drift exists against any of them.

This pass created exactly one file, this one. It ran no Git mutation, no TeX
build, and no ledger, register, control, or manuscript write. It executed three
Python sessions (SymPy exact rational/symbolic arithmetic plus one NumPy
quadrature), recorded in Sections 1.8 and 2.7; per the protocol, computation
corroborates arithmetic and closes no theorem.

### 0.2 Input digests (SHA-256 of working-tree bytes, recomputed by this pass)

| Path | SHA-256 |
| --- | --- |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/problem-contract.json` | `7cba2e9bbfe34028d6a994359e53c761779bd255c5405bfa3996c50ca575bc22` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/claim-ledger.json` | `53d9a2ae2ceab6a20c0486facc68e07bfb66731ebdccdfcc7c87f9890357c5f7` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/dependency-dag.json` | `bb296da12424fdd766727f0236aa6b91b1cb8fcfb93e3016882532049a119c16` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/counterexample-register.md` | `c7e0fa8d576ab60c2d4060f423e4222e800116a0293e0097c8d38ab55e6b6853` |
| `.../evidence/task-10-bundle-pullback-analysis.md` | `124010f91e7bc2a7569d5d85bc9dcf5ba44581da508eb246a836ca222b00e63b` |
| `.../evidence/task-10-score-configuration-analysis.md` | `9161b0f0941ed7b2061ba1102b2a5df5acbe318a8c2d57fc391003f7a782de4f` |
| `.../evidence/task-10-preintegration-adversarial.md` | `ff81719406628644a3cde746cb88dc91ca7c282ab1eed51a217cf1b584abf44c` |
| `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex` | `a87bc2b3d7d8d76412a299fbd3220464802bd1cc2d853f1f6c287f96e5a73279` |
| `manuscripts/gauge_vfe_rg/05d_relational_inference.tex` | `138e4f86f107f5bd0307e049dc5368a6c36584a827bf98bf4eb396e30016d0a1` |
| `manuscripts/gauge_vfe_rg/06_general_coarsegraining.tex` | `a6a60a19a7c263915e749787b12470a84d6fafcaf9d55c69b71c0490c45c064a` |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `a3a7ae2fed2eb4a1ea4668393a69b4d56aa2c9dd071af06ddbcba717d7365797` |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `148d9652229eb6d3c40a41b48c1eb938328ca697a37e8113111567c580cc61be` |
| `manuscripts/gauge_vfe_rg/08_infogeometry.tex` | `55bfcdff0eebec24f2231852467255d13a0c02d1369621d04ede53cad3b7c31b` |
| `manuscripts/gauge_vfe_rg/04_generative.tex` | `e4837a9d241c12dc1b11e5997dee3bd4616ac6f6e0d472c6a724aa81ad0f5b3d` |
| `manuscripts/gauge_vfe_rg/appendix_notation.tex` | `d39936499c9673c1b4ed75ae31bf294f8d4df9fd1fd0cef1dae4a9ec5a572fa4` |

The two route-report digests (`124010f9…`, `9161b0f0…`) match the values the
pre-integration adversarial pass recorded for the same files, so all three
passes and this one read identical bytes.

### 0.3 Independence boundary

Read in full: the frozen problem contract, the Task 10 claims and assumptions
of `claim-ledger.json`, `dependency-dag.json`, `05c_pullback_geometry.tex`,
the relevant sections of `05d_relational_inference.tex`, the counterexample
register, and the three commissioned reports
(`task-10-bundle-pullback-analysis.md`,
`task-10-score-configuration-analysis.md`,
`task-10-preintegration-adversarial.md`). **Not read:** any
task-10-interface-reconciliation artifact (none was opened; per the
commissioning instruction it would not have been read had it appeared) and
`task-10-timeless-history-analysis.md` (present on disk; deliberately not
opened, so no route-D content is inherited here). Order of work, stated
because it bears on independence: the Mechanism I formulas of Section 1 —
the anomaly sign convention, chain rule, signed comparison, ordered
composition law, and the base-cocycle correction — were derived by this pass
from the definitions in `05c_pullback_geometry.tex` **before** the three
reports were opened; in particular the defect in the bundle report's R4.3(3)
(finding F-I-1 below) was derived independently and only afterwards found to
coincide with the adversarial pass's M-1. Route agreement is not used as
evidence anywhere below; every load-bearing identity carries its own
derivation or executed check.

The affirmative-existence instruction attached to the commissioning brief is
a search prior. It allocated effort. It appears in no premise, hypothesis,
proof, counterexample, or disposition below; Section 5 records the erasure
audit.

---

## 1. Mechanism I — composable bundle morphisms, horizontal defects, and the signed base Fisher comparison

### 1.1 Typed data

For $j\in\{0,1,2\}$: smooth finite-dimensional bases $\mathcal C_j$; principal
$G_j$-bundles $\pi_j:P_j\to\mathcal C_j$; represented sample actions inducing
law actions $\widehat\rho_j$ on smooth parametrized-measure fibers
$\mathcal B_j$ satisfying the regular-model hypothesis
(`hyp:pb-regular-models` at both scales: DQM, square-integrable scores,
positive-definite $g_j^F$, invariance of $g_j^F$ under the represented
action); associated bundles $E_j=P_j\times_{\widehat\rho_j}\mathcal B_j$ with
projections $\varpi_j$, vertical bundles $VE_j=\ker T\varpi_j$; principal
connections $\omega_j$ with horizontal lift operators
$H^{\omega_j}:\varpi_j^*T\mathcal C_j\to TE_j$ and vertical projectors
$\operatorname{ver}^{\omega_j}:TE_j\to VE_j$.

Scale arrows for $(jk)\in\{(01),(12)\}$: base maps
$f_{jk}\in C^\infty(\mathcal C_j,\mathcal C_k)$; Lie-group homomorphisms
$\kappa_{jk}:G_j\to G_k$; $\kappa_{jk}$-equivariant principal maps
$\mathcal P_{jk}:P_j\to P_k$ over $f_{jk}$ (declared data; existence is the
separate topological condition $P_j\times_{\kappa_{jk}}G_k\cong f_{jk}^*P_k$);
sample-space Markov kernels $N_{jk}:\mathsf K_j\rightsquigarrow\mathsf K_k$,
normalized at **every** point, parameter independent; law-fiber maps
$q_{jk}=(N_{jk})_\star|_{\mathcal B_j}:\mathcal B_j\to\mathcal B_k$ under the
family-closure hypothesis $(N_{jk})_\star(\mathcal B_j)\subseteq\mathcal B_k$
and smoothness of $q_{jk}$ between the declared models; the intertwining
relation $q_{jk}\circ\widehat\rho_j(g)=\widehat\rho_k(\kappa_{jk}(g))\circ
q_{jk}$; the induced associated-bundle morphisms
$\Psi_{jk}:E_j\to E_k$, $\Psi_{jk}[u,\beta]=[\mathcal P_{jk}(u),q_{jk}(\beta)]$,
smooth, covering $f_{jk}$, with vertical differentials
$T^V\Psi_{jk}:VE_j\to VE_k$; and related smooth sections
$s_j\in\Gamma(\mathcal U_j,E_j)$ with
$\Psi_{01}\circ s_0=s_1\circ f_{01}$ and $\Psi_{12}\circ s_1=s_2\circ f_{12}$.
Covariant vertical first jets
$D^{\omega_j}s_j:=\operatorname{ver}^{\omega_j}\circ Ts_j
:T\mathcal U_j\to s_j^*VE_j$; base pullbacks
$h_j:=(D^{\omega_j}s_j)^*g_j^F\in\Gamma(\operatorname{Sym}^2T^*\mathcal U_j)$.
Quantifiers below: every $c$ in the fine domain, every
$X,Y\in T_c\mathcal C_0$, every finite composable sequence of such arrows,
each channel separately.

### 1.2 The horizontal defect: definition and sign convention

**Definition 1.1.** For a smooth bundle morphism $\Psi:E\to\bar E$ over $f$
between connected data $(\omega,\bar\omega)$, the **horizontal defect**
(anomaly) at $e\in E$, $X\in T_{\varpi(e)}\mathcal C$, is
$$
A_\Psi(e;X)\;:=\;\operatorname{ver}^{\bar\omega}\!\Big(T_e\Psi\big(H^\omega_eX\big)\Big)
\;=\;T_e\Psi\big(H^\omega_eX\big)\;-\;H^{\bar\omega}_{\Psi(e)}\big(T_cfX\big)
\;\in\;V_{\Psi(e)}\bar E .
$$
**Sign convention:** transported fine horizontal **minus** coarse horizontal
lift. Verticality: $T\bar\varpi\,T\Psi(H^\omega_eX)=Tf\,T\varpi(H^\omega_eX)
=T_cfX=T\bar\varpi\,H^{\bar\omega}(T_cfX)$, so the difference lies in
$\ker T\bar\varpi$; the two displayed forms agree because the
$\bar\omega$-horizontal part of $T\Psi(H^\omega_eX)$ is exactly
$H^{\bar\omega}(T_cfX)$. Type:
$A_\Psi\in\Gamma\big(E;\varpi^*T^*\mathcal C\otimes\Psi^*V\bar E\big)$; along
a section, $A_\Psi(s;\cdot)\in\Gamma\big(\mathcal U;T^*\mathcal U\otimes
f^*\bar s^*V\bar E\big)$. This is `eq:pb-coarse-horizontal-defect`
($\mathcal D\Psi$) with its sign made explicit.

### 1.3 Chain rule and the one-step signed comparison with every cross term

**Theorem 1.2 (covariant first-jet chain rule).** If $\Psi\circ s=\bar s\circ f$,
then for every $c$, $X$:
$$
D^{\bar\omega}\bar s\big(T_cfX\big)
=T^V\Psi\big(D^\omega sX\big)+A_\Psi\big(s(c);X\big).
$$
*Proof.* Split $T_cs\,X=H^\omega_{s(c)}X+D^\omega sX$ and apply $T\Psi$; the
vertical summand maps to $T^V\Psi(D^\omega sX)$ (bundle morphisms preserve
verticality), the horizontal summand to
$H^{\bar\omega}(TfX)+A_\Psi(s(c);X)$ by Definition 1.1. Differentiating the
relation gives $T\Psi(TsX)=T\bar s(TfX)
=H^{\bar\omega}_{\bar s(f(c))}(TfX)+D^{\bar\omega}\bar s(TfX)$ with
$\Psi(s(c))=\bar s(f(c))$; the horizontal terms cancel and the vertical parts
match. $\square$

**Theorem 1.3 (one-step signed base Fisher comparison).** Define the vertical
Fisher defect $\Delta_F^\Psi:=g^F-(T^V\Psi)^*\bar g^F
\in\Gamma(E;\operatorname{Sym}^2V^*E)$ and, along $s$, writing
$u_X=D^\omega sX$, $a_X=A_\Psi(s(c);X)$, $L=T^V\Psi$:
$$
\delta_\Psi(X,Y):=\Delta_F^\Psi(u_X,u_Y),\qquad
\mathcal X_\Psi(X,Y):=\bar g^F(Lu_X,a_Y)+\bar g^F(a_X,Lu_Y),\qquad
\mathcal Q_\Psi(X,Y):=\bar g^F(a_X,a_Y).
$$
Then, **with no compatibility hypothesis whatsoever**,
$$
\boxed{\;h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}
=\delta_\Psi-\mathcal X_\Psi-\mathcal Q_\Psi\;}
$$
as symmetric $2$-tensors on the fine domain; $\mathcal X_\Psi$ is symmetric
and sign-indefinite, $\mathcal Q_\Psi\succeq0$.
*Proof.* By Theorem 1.2, $f^*\bar h(X,Y)=\bar g^F(Lu_X+a_X,\;Lu_Y+a_Y)
=\bar g^F(Lu_X,Lu_Y)+\mathcal X_\Psi(X,Y)+\mathcal Q_\Psi(X,Y)$, and
$\bar g^F(Lu_X,Lu_Y)=g^F(u_X,u_Y)-\Delta_F^\Psi(u_X,u_Y)$. Subtract from
$h(X,Y)=g^F(u_X,u_Y)$. $\square$

Every cross term is displayed: the two polarized mixed terms
$\bar g^F(Lu_X,a_Y)$, $\bar g^F(a_X,Lu_Y)$ enter with sign $-1$, and the pure
anomaly quadratic $\bar g^F(a_X,a_Y)$ enters with sign $-1$.

### 1.4 Ordered composition law for horizontal defects

**Theorem 1.4.** For composable $\Psi_{01},\Psi_{12}$ with
$\Psi_{02}:=\Psi_{12}\circ\Psi_{01}$, $f_{02}:=f_{12}\circ f_{01}$, and for
every $e\in E_0$ over $c$, $X\in T_c\mathcal C_0$:
$$
\boxed{\;A_{\Psi_{02}}(e;X)
=T^V\Psi_{12}\big|_{\Psi_{01}(e)}\Big(A_{\Psi_{01}}(e;X)\Big)
+A_{\Psi_{12}}\Big(\Psi_{01}(e);\,T_cf_{01}X\Big).\;}
$$
*Proof.* $T\Psi_{01}(H^{\omega_0}_eX)=H^{\omega_1}_{\Psi_{01}e}(Tf_{01}X)
+A_{\Psi_{01}}(e;X)$ by Definition 1.1. Apply $T\Psi_{12}$: the horizontal
summand yields $H^{\omega_2}_{\Psi_{02}e}(Tf_{02}X)
+A_{\Psi_{12}}(\Psi_{01}e;Tf_{01}X)$, the vertical summand yields
$T^V\Psi_{12}(A_{\Psi_{01}}(e;X))$. Subtract
$H^{\omega_2}(Tf_{02}X)$. $\square$

The law is ordered and typed: the earlier defect is **pushed forward by the
later vertical differential**, and the later defect is evaluated **at the
image point on the pushed base tangent**. Writing $A_{02}=A_{01}+A_{12}$ is a
type error ($A_{01}$ is $VE_1$-valued, $A_{12}$ is $VE_2$-valued). The
executed check in Section 1.8 confirms that both "wrong variants" (dropping
$T^V\Psi_{12}$, or dropping $Tf_{01}$) fail identically. Identity arrows have
zero defect, so the family $(f,\kappa,\mathcal P,q,\Psi)$ with these ordered
laws is a functor on the thin category of the finite scale set — the content
of `bundle-scale-cocycle` — with $q_{02}=q_{12}\circ q_{01}
=(N_{01}N_{12})_\star|_{\mathcal B_0}$ by Chapman–Kolmogorov and
$\Psi_{02}[u,\beta]=[\mathcal P_{12}\mathcal P_{01}u,\;q_{12}q_{01}\beta]$
well defined because the composite data are
$\kappa_{12}\kappa_{01}$-equivariant and intertwining. (Descent itself: two
representatives of one point of $E_0$ are $(u,\beta)$ and
$(ug,\widehat\rho_0(g)^{-1}\beta)$; equivariance of $\mathcal P$ and
intertwining of $q$ send both to one class in $E_1$; and conversely, given a
declared equivariant $\mathcal P$, well-definedness forces intertwining.)

### 1.5 Exact two-step comparison and its stagewise decomposition

Notation: $\delta_{jk}:=(D^{\omega_j}s_j)^*\Delta_F^{\Psi_{jk}}$, and
$\mathcal X_{jk},\mathcal Q_{jk}$ the stage tensors of Theorem 1.3.

**Theorem 1.5.** With related sections at both stages:

1. **(Unconditional telescoping.)**
   $h_0-f_{02}^*h_2=\big[h_0-f_{01}^*h_1\big]+f_{01}^*\big[h_1-f_{12}^*h_2\big]$,
   i.e., the two instances of Theorem 1.3 add:
   $h_0-f_{02}^*h_2=(\delta_{01}+f_{01}^*\delta_{12})
   -(\mathcal X_{01}+f_{01}^*\mathcal X_{12})
   -(\mathcal Q_{01}+f_{01}^*\mathcal Q_{12})$. This is algebra and tests
   nothing about the composition mechanism.
2. **(Sharp composite form.)** The same difference equals the one-step
   formula of Theorem 1.3 applied to the composite arrow:
   $h_0-f_{02}^*h_2=\delta_{02}-\mathcal X_{02}-\mathcal Q_{02}$, where
   $\delta_{02}=(D^{\omega_0}s_0)^*\Delta_F^{\Psi_{02}}$ with
   $$
   \Delta_F^{\Psi_{02}}
   =\Delta_F^{\Psi_{01}}+(T^V\Psi_{01})^*\Delta_F^{\Psi_{12}}
   \tag{vertical Markov Fisher-defect cocycle}
   $$
   (contravariance of pullback; each summand $\succeq0$ when each arrow is a
   parameter-independent Markov coarse map with family closure), and
   $A_{\Psi_{02}}$ is given by the ordered law of Theorem 1.4. Consistency of
   (1) and (2) is a nontrivial identity precisely because
   $\Delta_F^{\Psi_{02}}$, $A_{\Psi_{02}}$ mix the stagewise objects through
   $T^V\Psi_{01}$, $T^V\Psi_{12}$, and $Tf_{01}$.
3. **(Base-cocycle correction, exact.)** Without any compatibility
   hypothesis, with $L_{01}=T^V\Psi_{01}$, $u=D^{\omega_0}s_0$,
   $a=A_{\Psi_{01}}(s_0;\cdot)$, and
   $v:=D^{\omega_1}s_1\circ Tf_{01}=L_{01}u+a$:
   $$
   \delta_{02}-\delta_{01}-f_{01}^*\delta_{12}
   =-\Big[\Delta_F^{\Psi_{12}}\big(L_{01}u_X,\,a_Y\big)
   +\Delta_F^{\Psi_{12}}\big(a_X,\,L_{01}u_Y\big)\Big]
   \;\mathbf{-}\;\Delta_F^{\Psi_{12}}\big(a_X,a_Y\big)
   $$
   $$
   \phantom{\delta_{02}-\delta_{01}-f_{01}^*\delta_{12}}
   =-\Big[\Delta_F^{\Psi_{12}}\big(v_X,\,a_Y\big)
   +\Delta_F^{\Psi_{12}}\big(a_X,\,v_Y\big)\Big]
   \;\mathbf{+}\;\Delta_F^{\Psi_{12}}\big(a_X,a_Y\big).
   $$
   The two forms are equal (substitute $v=L_{01}u+a$); the **sign of the
   quadratic term is coupled to the choice of mixed-term argument**. In
   particular $\delta_{02}=\delta_{01}+f_{01}^*\delta_{12}$ holds whenever
   $A_{\Psi_{01}}(s_0;\cdot)=0$; no hypothesis on the second arrow's defect
   and no relation to $s_2$ enters.
4. **(Zero-anomaly specialization.)** If $A_{\Psi_{01}}(s_0;\cdot)=0$ and
   $A_{\Psi_{12}}(s_1;\cdot)=0$ on the relevant image, then
   $A_{\Psi_{02}}(s_0;\cdot)=0$ by Theorem 1.4 and
   $$
   h_0-f_{02}^*h_2=\delta_{02}
   =\delta_{01}+f_{01}^*\delta_{12}\;\succeq\;0,
   $$
   each stage term positive semidefinite with
   $\Delta_F^{\Psi_{jk}}(w,w)=\mathbb E\operatorname{Var}(\ell_w\mid Y)$
   (conditional score variance under the joint law
   $\beta(dx)N_{jk}(x,dy)$; DQM pushforward of the score is its conditional
   expectation — the transfer from the canonical quadratic path to an
   arbitrary DQM path is required here and is supplied by the Hellinger
   contraction/DQM-rigidity argument of the score route's Theorem A, which
   this pass accepts after re-derivation of its two lemmas). Equality in a
   direction $X$ holds exactly when the fine score in direction
   $D^{\omega_0}s_0X$ is a.s. equal to a coarse-measurable function.

*Proof of 3 (the load-bearing part).* Pull the vertical cocycle back by
$D^{\omega_0}s_0$: $\delta_{02}=\delta_{01}
+\Delta_F^{\Psi_{12}}(L_{01}u_X,L_{01}u_Y)$. Substitute $L_{01}u=v-a$ and
expand the bilinear form: the pure $v$ term is $f_{01}^*\delta_{12}$; the
remaining terms are the second displayed form. Substituting back $v=L_{01}u+a$
gives the first form. $\square$

**Finding F-I-1 (defect in the prior bundle evidence, independently derived
here, confirming the adversarial pass's M-1).**
`task-10-bundle-pullback-analysis.md` Theorem R4.3(3) prints the correction
with mixed arguments $L_{01}D^{\omega_0}s_0$ **and** sign $+$ on the quadratic
term. That combination is wrong: with $L_{01}u$ arguments the quadratic sign
is $-$; with $v$ arguments it is $+$. The printed right-hand side exceeds the
true value by $2\Delta_F^{\Psi_{12}}(a_X,a_Y)$. Executed confirmation in
Section 1.8: the generic symbolic residual is
$-2\,\tau_1^2\,\big(c_1\alpha_1(c_1x)-\lambda_0\alpha_0(x)\big)^2/(v_1v_2)\ne0$,
and at the numeric instance the true correction is $-496/77$ against the
printed formula's $-80/77$.

**Finding F-I-2 (mislabeled executed verification in the prior bundle
evidence, independently established, confirming M-2).** The same report's
"Block C — the base cocycle (R4.3)" evaluates quantities
$\delta_{jk}=h_j-f_{jk}^*h_k$ (checkable: its displayed $\delta_{01}$ depends
on the middle connection coefficient $a_1$, which the R3.3 object
$(D^{\omega_0}s_0)^*\Delta_F^{\Psi_{01}}$ cannot, since $A_{\omega_0}=0$ and
$\Delta_F^{\Psi_{01}}$ are $a_1$-independent) and therefore verifies only the
unconditional telescoping of Theorem 1.5(1) — an identity true for arbitrary
tensors — not the sharp base cocycle. The check in Section 1.8 is designed so
that this failure mode cannot recur: it evaluates the R3.3 $\delta$'s, and it
numerically separates the correct correction from the printed one.

### 1.6 Exact signed positivity criterion (anomaly nonzero)

**Theorem 1.6.** Assume the Markov, closure, and invariance hypotheses, so
$\Delta_F^\Psi\succeq0$ and $\delta_\Psi\succeq0$. Then at $c$:

1. **(Exact criterion.)** $h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}\succeq0$
   at $c$ **iff** for every $X\in T_c\mathcal C$
   $$
   \big\|T^V\Psi\,D^\omega sX+A_\Psi(s(c);X)\big\|_{\bar g^F}
   =\big\|D^{\bar\omega}\bar s(T_cfX)\big\|_{\bar g^F}
   \;\le\;\big\|D^\omega sX\big\|_{g^F},
   $$
   equivalently $\delta_\Psi(X,X)\ge\mathcal X_\Psi(X,X)+\mathcal Q_\Psi(X,X)$.
2. **(Sufficient margin, not necessary.)**
   $\|A_\Psi(s(c);X)\|_{\bar g^F}\le\sqrt{h(X,X)}-\sqrt{h(X,X)-\delta_\Psi(X,X)}$
   implies positivity in direction $X$ (triangle inequality); it is not
   necessary (witness below).
3. **(Zero defect is sufficient, not necessary.)** $A_\Psi(s;\cdot)=0$ gives
   $h-f^*\bar h=\delta_\Psi\succeq0$. Nonzero anomaly with strictly positive
   comparison is realizable, so **zero defect is not necessary for
   positivity** — the ledger clause of `horizontal-defect-anomaly`,
   "positivity follows only when that defect vanishes," is **refuted as a
   necessity claim**. Witness (re-derived and executed here): fine fiber
   $\{\mathcal N(\mu,1)\}$, kernel $N(x,\cdot)=\mathcal N(x,1)$ (so
   $\bar{\mathcal B}=\{\mathcal N(\mu,2)\}$, $\bar g^F=\tfrac12$,
   $\Delta_F^\Psi=\tfrac12$), $f=\operatorname{id}$, section $s(x)=x$, source
   connection $0$, target local connection contributing anomaly $b\,\partial_\mu$:
   comparison $=1-\tfrac12(1+b)^2$, which at $b=\tfrac1{10}$ equals
   $\tfrac{79}{200}>0$ with $A_\Psi\ne0$; at $b=\tfrac12$ it equals
   $-\tfrac18<0$; and at $b=-\tfrac35$ it equals $\tfrac{23}{25}>0$ while the
   margin of item 2 is violated ($\|A_\Psi\|_{\bar g^F}=\tfrac{3}{5\sqrt2}
   \approx0.424>1-\tfrac1{\sqrt2}\approx0.293$), so the margin is sufficient
   but not necessary.
4. **(Strict negativity is realizable with a genuine Markov arrow —
   `CE-HORIZONTAL-ANOMALY` reconstructed.)** Identity kernel
   ($\Delta_F^\Psi=0$), related constant sections, source horizontal field
   $\partial_x$, target horizontal field $\partial_x+a\,\partial_\mu$,
   $a\neq0$: then $u=0$, $a_X=-a\,\partial_\mu$, and
   $h-f^*\bar h=0-0-a^2\,dx^2\prec0$. The register row is hereby
   independently reconstructed with the same sign and coefficient; positivity
   fails although the fiber map is Markov, sections are exactly related, and
   both Fisher metrics are positive definite.

### 1.7 What the mechanism needs, exactly

Hypotheses that are load-bearing and must be carried by any integration:
family closure $(N)_\star(\mathcal B)\subseteq\bar{\mathcal B}$; smoothness of
$q$ between the declared models; the coarse-scale instance of
`hyp:pb-regular-models` (in particular $\bar G$-invariance of $\bar g^F$,
which cancels the frame factor $\widehat{\bar\rho}(\varsigma(c))$ in the
local representative of $\Psi$); everywhere-normalization of $N$; the DQM
transfer step (canonical path to arbitrary DQM family); and, for base
positivity, $A_\Psi(s;\cdot)=0$ along the section or the exact criterion of
Theorem 1.6(1). The phrase "connection-compatible," used at five manuscript
sites (Section 3), has no definition in the source; the exact usable
condition is $A_\Psi(s;\cdot)=0$ along the section (equivalently, for induced
morphisms, the isotropy condition on the scale-connection defect form).

### 1.8 Executed algebraic check (sharp, not telescoping)

Design: a two-stage affine-Gaussian realization with **every structural
element nontrivial and generic**, so that each candidate formula is separated
from its neighbors. Fibers: Gaussian location families with variances
$v_0$, $v_1=\lambda_0^2v_0+\tau_0^2$, $v_2=\lambda_1^2v_1+\tau_1^2$
(Chapman–Kolmogorov consistent: the composite kernel has
$\lambda_{02}=\lambda_0\lambda_1$, $\tau_{02}^2=\lambda_1^2\tau_0^2+\tau_1^2$,
$v_2=\lambda_{02}^2v_0+\tau_{02}^2$); Fisher metrics $g_j=1/v_j$; fiber maps
$\mu\mapsto\lambda_j\mu+\beta_j$ induced by the parameter-independent Markov
kernels $y=\lambda_jx+\beta_j+\varepsilon_j$, so $T^V\Psi_{jk}=\lambda_j\ne1$;
base maps $f_{01}(x)=c_1x$, $f_{12}(y)=c_2y$ with $c_1,c_2\ne1$; generic
symbolic connection functions $\alpha_0(x),\alpha_1(y),\alpha_2(z)$; generic
symbolic fine section $\mu_0(x)$; related sections
$s_1(y)=\lambda_0\mu_0(y/c_1)+\beta_0$,
$s_2(z)=\lambda_1s_1(z/c_2)+\beta_1$. Anomalies:
$a_{01}=-\lambda_0\alpha_0(x)+c_1\alpha_1(c_1x)$,
$a_{12}(y)=-\lambda_1\alpha_1(y)+c_2\alpha_2(c_2y)$,
$a_{02}=-\lambda_0\lambda_1\alpha_0(x)+c_1c_2\alpha_2(c_1c_2x)$ — all
generically nonzero, with the middle-connection cancellation in the ordered
law being the sharp content.

SymPy results (exact, symbolic in
$\lambda_0,\lambda_1,v_0,\tau_0,\tau_1,c_1,c_2,\beta_0,\beta_1$ and the three
generic functions):

| Check | Result |
| --- | --- |
| chain rule, stages 01, 12, and composite 02 | PASS (identically zero) |
| one-step signed comparison (Theorem 1.3), both stages | PASS |
| ordered anomaly law (Theorem 1.4) | PASS |
| wrong variants of the ordered law (drop $T^V\Psi_{12}$; drop $Tf_{01}$) | both nonzero (test has teeth) |
| two-step sharp composite formula (Theorem 1.5(2)) | PASS |
| unconditional telescoping (Theorem 1.5(1)) | PASS |
| vertical defect cocycle $\Delta^{02}=\Delta^{01}+\lambda_0^2\Delta^{12}$ | PASS |
| base-cocycle correction, $L_{01}u$-form with $-$ quadratic | PASS |
| base-cocycle correction, coarse-jet form with $+$ quadratic | PASS |
| printed R4.3(3) form ($L_{01}u$ args, $+$ quadratic) | residual $-2\tau_1^2\big(c_1\alpha_1(c_1x)-\lambda_0\alpha_0(x)\big)^2/(v_1v_2)\ne0$ |
| numeric instance ($\lambda_0=\tfrac32,\lambda_1=\tfrac12,v_0=\tau_0=1,\tau_1=2,c_1=2,c_2=3,\mu_0=x^2,\alpha_0=x,\alpha_1=2y,\alpha_2=z/3$, $x=\tfrac12$) | true correction $-496/77$; printed $-80/77$ |
| zero-anomaly specialization ($\alpha_1,\alpha_2$ chosen to kill both anomalies) | PASS; $\Delta^{01}=\tfrac{\tau_0^2}{v_0v_1}>0$, $\Delta^{12}=\tfrac{\tau_1^2}{v_1v_2}>0$ |
| DQM pushed score $=$ conditional expectation (joint-Gaussian regression) | PASS |
| positivity with nonzero anomaly ($b=\tfrac1{10}$: $\tfrac{79}{200}>0$); negativity ($b=\tfrac12$: $-\tfrac18$) | PASS |

The check is sharp in the required sense: it evaluates the R3.3-typed
$\delta$'s (not base comparisons), its parameters make every cross term,
every pushforward factor, and every base-map derivative act nontrivially,
and it numerically separates the correct correction from the previously
printed one.

---

## 2. Mechanism II — configuration-manifold coarse graining

### 2.1 The reported counterexample, reproduced

**Statement under audit** (pre-integration adversarial pass, finding M-5): on
a two-point base with uniform probability measure $\kappa$, coarse base a
point with $\bar\kappa=f_\#\kappa$, unit channel weights, centered-Gaussian
belief fiber $\{\mathcal N(0,\Sigma):\Sigma>0\}$ in the moment chart,
configuration $(\Sigma_1,\Sigma_2)=(1,\delta)$, tangent
$Z=(\dot\Sigma_1,\dot\Sigma_2)=(1,0)$, barycentric coarse map
$\bar\Sigma=(\Sigma_1+\Sigma_2)/2$: the coarse-to-fine ratio of integrated
configuration Fisher energies is about $1.96$ at $\delta=10^{-2}$.

**Reproduction (this pass, independent computation).** The fiber Fisher form
of $\mathcal N(\mu,\Sigma)$ was recomputed by direct integration (SymPy):
$I_{\mu\mu}=1/\Sigma$, $I_{\Sigma\Sigma}=1/(2\Sigma^2)$, $I_{\mu\Sigma}=0$.
Then
$$
\|Z\|^2_{\mathsf G_0}
=\tfrac12\cdot\tfrac{1}{2\cdot1^2}+\tfrac12\cdot0=\tfrac14,
\qquad
\|T\mathsf{Avg}\,Z\|^2_{\mathsf G_1}
=\frac{(1/2)^2}{2\big(\tfrac{1+\delta}2\big)^2}
=\frac1{2(1+\delta)^2},
\qquad
\text{ratio}=\frac{2}{(1+\delta)^2}.
$$
At $\delta=\tfrac1{100}$ the exact ratio is
$\tfrac{20000}{10201}=1.96059209881\ldots$, matching the reported $1.96059$;
the ratio increases to $2$ (the block size) as $\delta\to0^+$ and is $<2$ for
every $\delta>0$. **Verdict: the counterexample is REPRODUCED and valid.** It
contradicts no proved theorem: the related-sections identity behind the
pointwise contraction is deliberately violated (the fine configuration is not
projectable), and the map is not a related-sections descent. What it refutes
is the narrative claim that fiberwise averaging "loses information" at the
configuration tier — under precisely the base-measure matching
$f_\#\kappa=\bar\kappa$ that the score route's Theorem E advertises as the
correct cross-scale condition.

**Sharpened diagnosis (new in this pass).** Two independent facts localize
the failure exactly.

1. *The blockwise map is Markov-realizable here, so data processing is not
   the obstruction.* For centered Gaussians, $z=(x_1+x_2)/\sqrt2$ pushes
   $\mathcal N(0,\Sigma_1)\otimes\mathcal N(0,\Sigma_2)$ to
   $\mathcal N\big(0,\tfrac{\Sigma_1+\Sigma_2}2\big)$ — a parameter-independent
   deterministic Markov kernel realizing the variance barycenter with family
   closure. Fisher data processing therefore bounds the coarse form by the
   **block-sum** $\sum_{i\in J}I_i$, verified here:
   $\tfrac1{2(1+\delta)^2}\le\tfrac12$ for all $\delta>0$. With **counting
   weights** ($w_i=\bar w_J=1$) the same map, same configuration, same
   tangent **contracts** ($0.4903\le0.5$ at $\delta=10^{-2}$).
2. *The increase is manufactured entirely by the probability-normalized
   weights.* Probability base measures force $\bar w_J=\sum_{i\in J}w_i$
   (pushforward of mass), so the coarse site carries weight $1$ against fine
   per-site weight $\tfrac12$; data processing bounds the coarse form by the
   block-sum, which is $|J|$ times the block-average, so the ratio is bounded
   by the block size $b=2$ and the witness saturates it as $\delta\to0^+$.
   Sector dependence: for a fiber-metric coefficient homogeneous of degree
   $-p$ in $\Sigma$, the concentrated-tangent ratio supremum is $b^{\,p-1}$ —
   $1$ for the location sector ($p=1$: probability-weight averaging is
   non-expansive there, by the same Cauchy–Schwarz certificate as below), $b$
   for the variance sector ($p=2$: the $1.96$ witness). The adversarial
   pass's convexity diagnosis (joint non-convexity of
   $(\Sigma,A)\mapsto A^2/(2\Sigma^2)$, Hessian determinant
   $-4A^2\Sigma^{-6}<0$) is correct as the reason the Jensen route fails; the
   weight bookkeeping above is the reason no other route rescues the
   probability-normalized statement.

### 2.2 A nonempty, noncircular finite-dimensional construction

**Construction 2.1 (configuration manifold, strong Gram/Fisher metric,
distinctly named smooth coarse configuration map).** Fix the fine vertex set
$V_0=\{1,2,3,4\}$, the coarse vertex set $V_1=\{J_1,J_2\}$, and the block map
$B:V_0\to V_1$, $B^{-1}(J_1)=\{1,2\}$, $B^{-1}(J_2)=\{3,4\}$. Belief fiber:
the full Gaussian family $\Theta=\{(\mu,\Sigma)\in\mathbb R\times
\mathbb R_{>0}\}$.

* **Configuration manifolds.**
  $\mathcal Q_0:=\Theta^{V_0}=(\mathbb R\times\mathbb R_{>0})^4$, an open
  subset of $\mathbb R^8$, hence a smooth $8$-manifold; nonempty
  (e.g. $(\mu_i,\Sigma_i)=(0,1)$ for all $i$). Likewise
  $\mathcal Q_1=\Theta^{V_1}$, a smooth $4$-manifold. These are section
  spaces of the trivial associated bundle over the finite discrete base; no
  infinite-dimensional topology is invoked.
* **Strong Gram/Fisher metric.** With declared site weights $w_i>0$
  ($i\in V_0$) and $\bar w_J>0$ ($J\in V_1$):
  $$
  \mathsf G_0\big|_\theta(\delta,\delta)
  =\sum_{i\in V_0}w_i\Big[\frac{\delta\mu_i^2}{\Sigma_i}
  +\frac{\delta\Sigma_i^2}{2\Sigma_i^2}\Big],
  \qquad
  \mathsf G_1\ \text{analogously with}\ \bar w_J .
  $$
  The Gram matrix is
  $\operatorname{diag}\big(w_i/\Sigma_i,\;w_i/(2\Sigma_i^2)\big)_{i\in V_0}$:
  smooth in $\theta$, positive definite for every $\theta\in\mathcal Q_0$,
  hence a Riemannian metric, and **strong** because in finite dimensions
  every positive-definite form makes the musical map a linear isomorphism.
  Noncircularity: the fiber Fisher matrix
  ($1/\Sigma$, $1/(2\Sigma^2)$, cross term $0$) is *computed* by integration
  in Section 2.7, not assumed via `H-CONFIG`; the construction instantiates
  the hypothesis class rather than quoting it.
* **Coarse configuration map, distinctly named.** Define the blockwise
  barycenter
  $$
  \mathsf{Avg}_B:\mathcal Q_0\to\mathcal Q_1,
  \qquad
  \mathsf{Avg}_B(\theta)_J
  =\Big(\tfrac1{|B^{-1}(J)|}\textstyle\sum_{i\in B^{-1}(J)}\mu_i,\;
  \tfrac1{|B^{-1}(J)|}\textstyle\sum_{i\in B^{-1}(J)}\Sigma_i\Big).
  $$
  $\mathsf{Avg}_B$ is the restriction of a linear map of $\mathbb R^8$ to an
  open set, with image in $\Theta^{V_1}$ by convexity of
  $\mathbb R\times\mathbb R_{>0}$; hence smooth with constant surjective
  differential. The symbol $\mathsf{Avg}_B$ collides with none of the
  manuscript's coarse arrows ($K_\ell$, $\mathcal R^H$, $\mathcal R_b$,
  $M_\ell$, $C_{\ell,s}$, $\widehat{\mathcal R}_\ell$, or the overloaded
  $\mathcal R$; Section 3). Under the diagonal congruence gauge action with a
  block-constant gauge element, $\mathsf{Avg}_B$ is equivariant (a linear map
  commuting with the blockwise-identical linear action); site-dependent gauge
  changes do not commute with averaging, and no such equivariance is claimed.

This discharges the "nonempty, noncircular" existence demand: manifold,
metric, and map are exhibited with explicit formulas, and each regularity
claim is proved from the displayed data.

### 2.3 Compatibility with the fiber Markov map: theorem versus assumption

**Theorem 2.2 (what is a theorem).**

1. *(Blockwise Markov contraction against the block-sum.)* If for a block $J$
   the coarse belief equals the pushforward of the block product belief
   under a parameter-independent Markov kernel
   $N_J:\prod_{i\in J}\mathsf K_i\rightsquigarrow\bar{\mathsf K}_J$ with
   family closure, then the pushed tangent is the conditional expectation of
   the block score (DQM pushforward), and
   $$
   I^{\mathrm{coarse}}_{\mathsf{Avg}_B(\theta)_J}\big(T\phi_J\,\delta_J,\;T\phi_J\,\delta_J\big)
   \;\le\;\sum_{i\in J}I_{\theta_i}(\delta_i,\delta_i),
   $$
   by Fisher data processing on the product experiment (product-family
   Fisher additivity plus the conditional-variance identity).
2. *(Weight-dominated contraction, no Markov hypothesis needed.)* For the
   Gaussian moment-chart barycenter $\mathsf{Avg}_B$ of Construction 2.1, if
   $$
   \bar w_J\;\le\;\min_{i\in B^{-1}(J)}w_i
   \qquad\text{for every }J\in V_1,
   $$
   then $\mathsf G_1\big(T\mathsf{Avg}_B\,\delta,\;T\mathsf{Avg}_B\,\delta\big)
   \le\mathsf G_0(\delta,\delta)$ for every $\theta$ and $\delta$. Proof, per
   block of size $b$ with $\bar\mu,\bar\Sigma$ the block means: the location
   sector uses the Cauchy–Schwarz certificate
   $$
   \Big(\sum_i\delta\mu_i\Big)^2
   \le\Big(\sum_i\Sigma_i\Big)\Big(\sum_i\frac{\delta\mu_i^2}{\Sigma_i}\Big)
   \;\Longrightarrow\;
   \frac{\big(\tfrac1b\sum_i\delta\mu_i\big)^2}{\bar\Sigma}
   \le\sum_i\frac{\delta\mu_i^2}{\Sigma_i},
   $$
   whose $b=2$ form has the exact sum-of-squares identity
   $\big(\tfrac{\delta\mu_1^2}{\Sigma_1}+\tfrac{\delta\mu_2^2}{\Sigma_2}\big)
   (\Sigma_1+\Sigma_2)-(\delta\mu_1+\delta\mu_2)^2
   =\big(\delta\mu_1\sqrt{\Sigma_2/\Sigma_1}-\delta\mu_2\sqrt{\Sigma_1/\Sigma_2}\big)^2$;
   the variance sector uses
   $$
   \Big(\frac{\delta\Sigma_1^2}{\Sigma_1^2}+\frac{\delta\Sigma_2^2}{\Sigma_2^2}\Big)
   (\Sigma_1+\Sigma_2)^2-(\delta\Sigma_1+\delta\Sigma_2)^2
   =\Big(\frac{\delta\Sigma_1\Sigma_2}{\Sigma_1}-\frac{\delta\Sigma_2\Sigma_1}{\Sigma_2}\Big)^2
   +\frac{2\,\delta\Sigma_1^2\,\Sigma_2}{\Sigma_1}
   +\frac{2\,\delta\Sigma_2^2\,\Sigma_1}{\Sigma_2}\;\ge\;0,
   $$
   both verified exactly in Section 2.7; summing the blockwise inequalities
   with $\bar w_J\le\min_iw_i$ gives the claim. (The probability-weight
   location-sector inequality reduces to the same location certificate, so
   the location sector is non-expansive even under probability weights.)
3. *(Ratio bound.)* Under item 1's hypotheses with probability-normalized
   weights, the coarse-to-fine energy ratio is bounded by the block size,
   and the bound is sharp (the $1.96$ witness saturates $b=2$ as
   $\delta\to0^+$).

**Lemma 2.3 (what must be assumed, and what is refuted).** There is **no**
parameter-independent Markov kernel $T:\mathbb R^2\rightsquigarrow\mathbb R$
with
$\big(\mathcal N(\mu_1,\Sigma_1)\otimes\mathcal N(\mu_2,\Sigma_2)\big)T
=\mathcal N\big(\tfrac{\mu_1+\mu_2}2,\tfrac{\Sigma_1+\Sigma_2}2\big)$ for all
$(\mu,\Sigma)\in\mathbb R^2\times\mathbb R_{>0}^2$. Hence the joint
$(\mu,\Sigma)$ barycenter of Construction 2.1 is **not** Markov-realizable,
and Markov compatibility for it must be *assumed away* (restricted) rather
than invoked.

*Proof.* Suppose $T$ exists. For $t\in\mathbb R$ set
$g_t(x)=\int e^{itz}\,T(x,dz)$, bounded and measurable on $\mathbb R^2$. The
requirement at $\Sigma_1=\Sigma_2=\sigma^2$ reads
$\big(P_{\sigma^2}g_t\big)(\mu)=e^{it(\mu_1+\mu_2)/2}\,e^{-t^2\sigma^2/2}$,
where $P_{\sigma^2}$ is coordinatewise Gaussian smoothing with variance
$\sigma^2$ (the heat semigroup). Let $\sigma^2\to0^+$: the left side
converges in $L^1_{\mathrm{loc}}$ to $g_t$, the right side locally uniformly
to $e^{it(\mu_1+\mu_2)/2}$; hence $g_t(x)=e^{it(x_1+x_2)/2}$ for a.e. $x$.
Substituting back, the heat semigroup multiplies $e^{it(x_1+x_2)/2}$ by
$e^{-t^2\sigma^2(\frac14+\frac14)/2}=e^{-t^2\sigma^2/4}$, while the
requirement demands $e^{-t^2\sigma^2/2}$. For $t\ne0$, $\sigma^2>0$ these
differ. $\square$

Restrictions that **are** Markov-realizable (each verified in Section 2.7):
the centered-Gaussian variance barycenter, via $z=(x_1+x_2)/\sqrt2$; and the
fixed-common-variance location barycenter, via $z=(x_1+x_2)/2+\eta$,
$\eta\sim\mathcal N(0,\Sigma_0/2)$ (parameter-independent because $\Sigma_0$
is a family constant), with family closure in both cases. The deterministic
$z=(x_1+x_2)/2$ produces variance $(\Sigma_1+\Sigma_2)/4$, and
$z=(x_1+x_2)/\sqrt2$ produces mean $(\mu_1+\mu_2)/\sqrt2$ — each wrong for
the joint map, which is what Lemma 2.3 makes unconditional.

**Determination.**

| Item | Status |
| --- | --- |
| Pushed score $=$ conditional expectation; blockwise Fisher $\le$ block-sum | **Theorem**, given blockwise Markov realizability with family closure and DQM |
| Configuration-level contraction $\mathsf G_1\!\circ T\mathsf{Avg}_B\le\mathsf G_0$ | **Theorem** under the weight domination $\bar w_J\le\min_{i\in J}w_i$ (Theorem 2.2(2), no Markov needed for the Gaussian barycenter); also follows from Theorem 2.2(1) + the same weight condition when Markov-realizable |
| Markov realizability of a given parameter map | **Must be checked per map**: holds for the centered-variance and fixed-variance-location restrictions; **refuted** for the joint $(\mu,\Sigma)$ barycenter (Lemma 2.3) |
| Family closure $(N)_\star(\mathcal B)\subseteq\bar{\mathcal B}$ | **Assumption** (fails, e.g., for the context-forgetting mixture: a Gaussian mixture is not Gaussian — which is also why the mixture map and the barycenter map are distinct; Section 2.7 confirms mixture Fisher $\approx0.5504\ne1$) |
| Contraction under probability-normalized (pushforward-matched) weights | **False**: the reproduced $1.96$ counterexample; ratio supremum $=$ block size in the variance sector |
| "Generic averaging is contractive" | **Not assertable.** The proved exclusion of the counterexample is exactly the weight-domination hypothesis of Theorem 2.2(2) (the witness violates it: $\bar w=1>\tfrac12=\min_iw_i$); absent that hypothesis (or item 1 + weights), no contraction statement may be attached to averaging or variational coarse maps |

### 2.4 Projectability context (for the disposition in Section 4)

The averaging construction is the "separately supplied smooth
gauge-equivariant averaging" branch of `configuration-projectability`; it is
not a descent. The descent mechanism itself is reconstructed as: for a
surjective submersion $f$ with connected fibers and smooth $\Psi$ over $f$,
a fine section $Q$ descends ((P1): $\exists\,\bar Q$ with
$\Psi\circ Q=\bar Q\circ f$) iff $\Psi\circ Q$ is fiber-constant (P2), iff
(P3) $T^V\Psi(D^\omega Q(X))+A_\Psi(Q(c);X)=0$ for every $X\in\ker T_cf$;
under (P2) the descended $\bar Q$ is unique, automatically a smooth section
(smooth-quotient theorem for surjective submersions — smoothness is a
theorem, not an obligation). `CE-SECTION-DESCENT` is reconstructed exactly:
$\mathcal C=S^1\to\{\ast\}$ (a surjective submersion), identity fiber map,
$Q(x)=\mathcal N(\sin x,1)$: $\Psi\circ Q$ is not fiber-constant, so no
coarse section exists; equivalently (P3) fails since
$T^V\Psi(D^\omega Q(\partial_x))=\cos x\,\partial_\mu\not\equiv0$ on
$\ker Tf=TS^1$ with $A_\Psi=0$. Without the submersion hypothesis smoothness
of the descent can fail ($f(x)=x^3$, $\bar Q(y)=\mathcal N(y^{1/3},1)$ is not
$C^1$ at $0$).

### 2.7 Executed verification record (Mechanism II)

SymPy exact arithmetic plus one NumPy quadrature:

| Check | Result |
| --- | --- |
| Fisher of $\mathcal N(\mu,\Sigma)$ by integration | $I_{\mu\mu}=1/\Sigma$, $I_{\Sigma\Sigma}=1/(2\Sigma^2)$, $I_{\mu\Sigma}=0$ |
| counterexample energies | fine $=\tfrac14$; coarse $=\tfrac1{2(1+\delta)^2}$; ratio $=2/(1+\delta)^2$ |
| ratio at $\delta=1/100$ | $\tfrac{20000}{10201}=1.96059209881384$ (reported: $1.96059$) — **REPRODUCED** |
| ratio bound | $2-2/(1+\delta)^2>0$ for $\delta>0$; $\to2$ as $\delta\to0^+$ |
| probability-weight violation window | fine $-$ coarse $=\tfrac14-\tfrac1{2(1+\delta)^2}<0$ exactly for $\delta<\sqrt2-1$; value $-\tfrac{9799}{40804}$ at $\delta=\tfrac1{100}$ |
| location-sector SOS certificate (counting and probability weights) | exact (PASS) |
| variance-sector SOS certificate (counting weights) | exact (PASS) |
| random search for counting-weight violations, both sectors, $2\times10^4$ points, $\Sigma\in[10^{-4},10^3]$ | none found (corroboration only) |
| centered-variance Markov realization $z=(x_1+x_2)/\sqrt2$ | variance $(\Sigma_1+\Sigma_2)/2$ (PASS); data processing instance $\tfrac1{2(1+\delta)^2}\le\tfrac12$ (PASS) |
| deterministic $z=(x_1+x_2)/2$ | variance $(\Sigma_1+\Sigma_2)/4\ne(\Sigma_1+\Sigma_2)/2$; $z=(x_1+x_2)/\sqrt2$ mean $(\mu_1+\mu_2)/\sqrt2\ne\bar\mu$ (Lemma 2.3 boundary data) |
| fixed-variance location kernel with compensating noise | output variance $=\Sigma_0$ (family closure PASS) |
| barycenter-vs-mixture separation (M-4) | mixture Fisher $I_{\bar P}(0)=0.5504$ at two independent discretizations ($h=10^{-4}$, $n=6\times10^5$; $h=10^{-5}$, $n=1.2\times10^6$), against barycenter-image metric $1.0$; the two coarse maps are distinct — confirmed |

---

## 3. Byte-level verifications on the current sources (independent of the route reports)

1. **"connection-compatible" is used and never defined.** Grep over
   `manuscripts/gauge_vfe_rg/*.tex`: `05c_pullback_geometry.tex:15`,
   `05c:652` (figure caption), `05c:791` ("If the connections are
   compatible", inside `thm:pb-fisher-defect-cocycle`),
   `06_general_coarsegraining.tex:202`, `08_infogeometry.tex:512`. No
   definition anywhere. The usable replacement is $A_\Psi(s;\cdot)=0$ along
   the section (Theorem 1.6(3) direction), stage-scoped per Theorem 1.5(3):
   the base cocycle needs only the first arrow's defect to vanish; the
   reading of $\delta_{12}$ as $h_1-f_{12}^*h_2$ needs the second's.
2. **The configuration-map symbol collision is live.** $\mathcal R$ denotes:
   the root-vertex set (`04_generative.tex:22`); the VFE descent ray
   (`05d_relational_inference.tex:287`); the configuration coarse map
   $\mathcal R:\mathcal Q_f\to\mathcal Q_m$ and $\mathcal R_\ell$
   (`05d:700,719,745,746,769,780,783`); the nonlinear action map
   $\mathcal R^H$ (`07b_agent_network_rg.tex:185-186`); the block
   measure-pair maps $\mathcal R_b$, $\mathcal R_b^\rho$, $\mathcal R_b^H$
   (`07b:2074,2079,2088`); and the reference-space endomorphism
   $\widehat{\mathcal R}_\ell$ differs only by a hat
   (`07_general_renormalization.tex:45-48`). `appendix_notation.tex` has no
   row of type $\mathcal Q_\ell\to\mathcal Q_{\ell+1}$ (searched; no match).
   The ledger falsifier for `configuration-map` is met in substance.
3. **A type conflation at `05d_relational_inference.tex:783`.** The clause
   "and $\mathcal R_\ell$ is a parameter-independent Markov map" attaches a
   kernel-tier predicate to a map of configuration manifolds without
   declaring the realization ($N_J$, closure) that would give it content;
   Lemma 2.3 shows the predicate can be unsatisfiable for natural averaging
   maps, so the clause is a substantive hypothesis, not a typing remark.

---

## 4. Atomic dispositions

| Claim (`claim-ledger.json`) | Disposition of this pass | Basis |
| --- | --- | --- |
| `horizontal-defect-anomaly` | **Mechanism PROVED; one ledger conjunct REFUTED as worded.** The chain rule, the retained vertical defect term, the exact composition law, and every signed cross term are Theorems 1.2–1.5 with the executed sharp check of Section 1.8. The clause "positivity follows only when that defect vanishes" is refuted as a necessity claim by Theorem 1.6(3) ($A_\Psi\ne0$ with comparison $\tfrac{79}{200}>0$, and $\tfrac{23}{25}>0$ beyond the margin). Cannot close as written; closes affirmatively once restated as sufficiency plus the exact criterion of Theorem 1.6(1). |
| `pullback-compatibility` | **PROVED as a conditional theorem; the unconditional order relation REFUTED.** Under related sections, $A_\Psi(s;\cdot)=0$, parameter-independent Markov fiber map with family closure, smooth $q$, and the coarse regular-model instance: $h-f^*\bar h=(D^\omega s)^*\Delta_F^\Psi\succeq0$ with conditional-score-variance identity (Theorem 1.5(4)). Without the first-jet square, the retained terms are exactly $-\mathcal X_\Psi-\mathcal Q_\Psi$ (Theorem 1.3), and strict negativity is realizable (`CE-HORIZONTAL-ANOMALY`, reconstructed at Theorem 1.6(4) — register row ready for promotion). |
| `bundle-scale-cocycle` | **PROVED (conditional, as stated).** Ordered identity and composition hold at each typed level (base, group, principal, law-fiber via Chapman–Kolmogorov, associated morphism) given the componentwise laws; the horizontal-defect ordered law (Theorem 1.4) and the vertical defect cocycle (Theorem 1.5(2)) compose consistently. Executed check: composite anomaly, composite comparison, and cocycle verified generically with non-identity fiber and base maps; wrong variants fail. The correct base-cocycle correction replaces the prior report's printed formula (finding F-I-1). |
| `configuration-fisher-metric` | **OPEN.** The existence half is discharged constructively (Construction 2.1: explicit nonempty finite-dimensional manifold, explicit positive-definite smooth Gram/Fisher metric, strong in finite dimensions, with the fiber Fisher matrix computed rather than assumed). The ledger claim, however, quantifies over every scale at which a natural-gradient field or Fisher duration is asserted, and the manuscript exhibits no configuration manifold for its declared recognition family, performs no strong-metric verification, and the weak-metric falsifier branch is live in the $H^s$ tier. Remaining obligation: exhibit the declared family's manifold and either the joint-law pullback identification or the labeled weighted-product data with the block-orthogonality condition. |
| `configuration-map` | **OPEN.** The symbol collision named in the claim's falsifier is live on the current bytes (Section 3, item 2), the notation appendix carries no configuration-arrow row, and `05d:783` attaches an untyped Markov predicate to the configuration arrow (Section 3, item 3) that Lemma 2.3 shows is refutable for natural instances. Construction 2.1 exhibits a valid, distinctly named, smooth instance ($\mathsf{Avg}_B$), so the model class is nonempty; the manuscript-level typing and the smooth-structure lemma for pointwise-induced maps (the projectable set as a manifold with a smooth induced arrow) remain unsupplied. |
| `configuration-projectability` | **PROVED, with the averaging branch fenced.** (P1) $\Leftrightarrow$ (P2) $\Rightarrow$ (P3), converse under connected fibers, automatic smoothness of the descent under a surjective submersion; `CE-SECTION-DESCENT` reconstructed exactly (register row ready for promotion); nonsubmersive smoothness failure witnessed. The separately supplied averaging construction exists and is smooth (Construction 2.1) but **may not be called contractive**: the $1.96$ counterexample is reproduced, and contraction is restored exactly under Theorem 2.2's weight-domination (or blockwise-Markov plus weights) hypotheses — the proved exclusion the claim's narrative requires. |

---

## 5. Oracle erasure, independent reconstruction, limitations

**Oracle erasure.** The affirmative-existence instruction was removed from the
working context before the dispositions of Section 4 were fixed, and this
artifact was rescanned for direct or paraphrased dependence. It appears in no
premise, hypothesis, proof, counterexample, or disposition. The outcome
distribution is inconsistent with a prior-driven pass: one prior-evidence
identity is corrected (F-I-1), one prior executed-verification block is found
vacuous for its stated purpose (F-I-2), one ledger clause is refuted as
worded, the flagship counterexample against the constructive repair is
reproduced rather than explained away, and two claims close `OPEN`. Passing
erasure shows only that the prior was unnecessary; it proves nothing.

**Independent reconstruction.** The Mechanism I formulas were derived from
the frozen contract and `05c_pullback_geometry.tex` definitions before the
route reports were read (Section 0.3), then compared: agreement with the
bundle route's R3.2/R3.3/R4.1/R4.2-consistent objects and with the score
route's (7.1), except where F-I-1 records the disagreement, which the
executed check adjudicates in this pass's favor (and in agreement with the
adversarial pass's M-1, reached independently). The Mechanism II
counterexample was recomputed from the fiber Fisher matrix upward, including
the integral computation of the matrix itself; the sharpened weight/sector
diagnosis, the block-size ratio law, the two SOS certificates, and Lemma 2.3
are new to this pass.

**Limitations, by kind.** *Theorems:* 1.2–1.6, 2.2, and Lemma 2.3 are proved
above from the displayed hypotheses; scope is the finite-dimensional smooth
regular tier of `hyp:pb-regular-models` and, for Mechanism II, the Gaussian
moment chart on finite discrete bases. The DQM-transfer step inside
Theorem 1.5(4) is used as re-derived from the score route's Lemmas 1.1–1.2
(Hellinger contraction is the $f$-divergence data-processing inequality with
$f(u)=(\sqrt u-1)^2$); it is the one external input and is hypothesis-mapped
there. *Constructions:* Construction 2.1 is an exhibited instance discharging
nonemptiness; it is not claimed canonical, and it does not instantiate the
manuscript's declared recognition family. *Counterexamples:* Theorem 1.6(4),
the $1.96$ reproduction, and the realizability boundary data are typed
witnesses with displayed computations; each refutes exactly the stated
reading. *Numerical observations:* the mixture-Fisher quadrature (0.5504)
and the $2\times10^4$-point random search corroborate; they close nothing.
*Modeling postulates and operational identifications:* none made; no
duration, clock, or physical-time statement is touched. *Not adjudicated:*
`bundle-morphism-descent`, `bundle-fisher-defect`,
`score-action-compatibility`, the three history claims, and all non-Task-10
ledger claims; the release artifact's terminal status is not this pass's to
set.

---

## 6. Terminal status for the audited mechanisms

* **Mechanism I** (bundle pullbacks, horizontal defects, signed base Fisher
  comparison, ordered composition, zero-anomaly cocycle): **verified in
  full** at the stated hypotheses, with the corrected base-cocycle
  correction of Theorem 1.5(3) replacing the prior printed formula, and with
  the ledger clause of `horizontal-defect-anomaly` requiring the
  sufficiency-plus-exact-criterion restatement before that claim can close.
  Standing alone this mechanism would release affirmatively after those two
  text repairs.
* **Mechanism II** (configuration coarse graining): the reported
  counterexample is **reproduced and valid** (ratio $2/(1+\delta)^2$,
  $1.96059\ldots$ at $\delta=10^{-2}$, supremum $=$ block size); a nonempty
  noncircular construction with a strong Gram/Fisher metric and a distinctly
  named smooth coarse configuration map is supplied; the exact
  theorem-versus-assumption boundary for fiber-Markov compatibility is
  determined, including the nonrealizability of the joint barycenter
  (Lemma 2.3) and the proved weight-domination exclusion under which
  averaging is contractive. `configuration-fisher-metric` and
  `configuration-map` nonetheless remain **OPEN** at the manuscript level.

Because the audited claim set contains two `OPEN` members and one claim whose
recorded wording is refuted, no affirmative terminal is available for the
mechanisms jointly, and nothing at the mechanism core is refuted, so the
negative terminal is unavailable as well.

**`INCONCLUSIVE`** — strongest verified result: Theorems 1.2–1.6 with the
executed sharp composition check, plus Theorem 2.2 / Lemma 2.3 with the
reproduced counterexample and its proved exclusion. Minimal unresolved
obligations: (i) restate the `horizontal-defect-anomaly` positivity clause as
sufficiency plus the exact criterion; (ii) correct the prior evidence's
R4.3(3) display and retitle its Block C; (iii) exhibit a configuration
manifold with verified strong metric for the manuscript's declared
recognition family (`configuration-fisher-metric`); (iv) perform the
configuration-arrow rename/typing with a notation-appendix row and type the
Markov predicate at `05d:783` (`configuration-map`).
