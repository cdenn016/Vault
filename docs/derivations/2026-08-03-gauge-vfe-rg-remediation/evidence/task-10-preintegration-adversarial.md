<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# INCONCLUSIVE — Task 10 pre-integration adversarial falsification

**Terminal status of this pass: `INCONCLUSIVE`.**

The portfolio is **not** ready for integration as it stands, and it is **not** refuted.
No load-bearing theorem mechanism in any of the three routes was shown to be false, even
conditionally, so this pass does not return `FAIL`. But five recomputed defects survive
adversarial attack — one wrong displayed identity, one mislabeled "executed verification"
block, one broken counterexample restatement, one false bridge attachment, and one
counterexample that refutes the portfolio's own proposed constructive repair — and two of
the twelve in-scope ledger claims are closed `OPEN` by two routes and `PROVED` by the
third on circular grounds. The exact missing lemmas are named in Part D
(**L-CM**, **L-CFM**, **L-AVG**, **L-JDQM**, **L-CONFIG-NONEMPTY**), and **L-AVG** is the
one that did not previously exist anywhere in the run: it is created by the refutation in
finding **M-5** below.

A careful integration can proceed only after the Part D lemmas are supplied or the affected
text is fenced, and after the Part A repairs are applied. Part F lists the explicit
hypothesis set under which the *rest* of the portfolio is integrable today.

---

## 0. Binding, scope, and method

### 0.1 Input digests

Base revision `02d5d8f542cba2d92c6a430483b62155dd5f2db4`, branch
`codex/gauge-vfe-rg-task10-pullbacks-20260804`. All digests are SHA-256 of the
**working-tree** bytes (this checkout carries `core.autocrlf=true`; the LF-normalized
committed-content digests are those tabulated in
`evidence/task-10-score-configuration-analysis.md` §0.2 and are not recomputed here).

| Path | SHA-256 (working tree) |
| --- | --- |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/problem-contract.json` | `7cba2e9bbfe34028d6a994359e53c761779bd255c5405bfa3996c50ca575bc22` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/claim-ledger.json` | `53d9a2ae2ceab6a20c0486facc68e07bfb66731ebdccdfcc7c87f9890357c5f7` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/dependency-dag.json` | `bb296da12424fdd766727f0236aa6b91b1cb8fcfb93e3016882532049a119c16` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/approach-registry.json` | `73c9cc54e9626750547d7e8eea530a9367b9c29f813621cdde7b408f75b9f891` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/adversarial-report.json` | `3375941d44dc67addc1b9eb95868ab27b4f430639a40357f4f2d3f09d8e3073f` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/release.json` | `9feffe38dfc0d9935e27189d63601846ffb55b92e2c502b843d5561028b79a3a` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/counterexample-register.md` | `c7e0fa8d576ab60c2d4060f423e4222e800116a0293e0097c8d38ab55e6b6853` |
| `.../evidence/task-10-bundle-pullback-analysis.md` | `124010f91e7bc2a7569d5d85bc9dcf5ba44581da508eb246a836ca222b00e63b` |
| `.../evidence/task-10-score-configuration-analysis.md` | `9161b0f0941ed7b2061ba1102b2a5df5acbe318a8c2d57fc391003f7a782de4f` |
| `.../evidence/task-10-timeless-history-analysis.md` | `e1bbfa7c32dbcae010e4e2f62e5a8e356907c4ecabf0e604ae4a461e3f57f7f4` |
| `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex` | `a87bc2b3d7d8d76412a299fbd3220464802bd1cc2d853f1f6c287f96e5a73279` |
| `manuscripts/gauge_vfe_rg/05d_relational_inference.tex` | `138e4f86f107f5bd0307e049dc5368a6c36584a827bf98bf4eb396e30016d0a1` |
| `manuscripts/gauge_vfe_rg/06_general_coarsegraining.tex` | `a6a60a19a7c263915e749787b12470a84d6fafcaf9d55c69b71c0490c45c064a` |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `a3a7ae2fed2eb4a1ea4668393a69b4d56aa2c9dd071af06ddbcba717d7365797` |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `148d9652229eb6d3c40a41b48c1eb938328ca697a37e8113111567c580cc61be` |
| `manuscripts/gauge_vfe_rg/08_infogeometry.tex` | `55bfcdff0eebec24f2231852467255d13a0c02d1369621d04ede53cad3b7c31b` |
| `manuscripts/gauge_vfe_rg/04_generative.tex` | `e4837a9d241c12dc1b11e5997dee3bd4616ac6f6e0d472c6a724aa81ad0f5b3d` |
| `manuscripts/gauge_vfe_rg/05_elbo.tex` | `a4aa559cc160ae0a2547f8f2b0d929b4e1c51bf2a7c0831e1eb34d2ef3bcf3a4` |
| `manuscripts/gauge_vfe_rg/appendix_notation.tex` | `d39936499c9673c1b4ed75ae31bf294f8d4df9fd1fd0cef1dae4a9ec5a572fa4` |

The three route reports' own binding tables agree with these bytes for every file they
share, so no input drift is reported against them.

### 0.2 Independence boundary

This pass received the frozen contract, the twelve in-scope ledger claims
(`claim-ledger.json:78-89`), the current source, and all three route reports. It was **not**
told which route is favored, and no route is treated as authority. Every identity a route
uses to close a claim was re-derived or re-evaluated here from the route's own declared
data; where a route's arithmetic was checkable, it was recomputed in exact rational and
symbolic form (Part E). Route agreement is nowhere used as evidence, and where the three
routes agree on a disposition the disposition is still stated only as strong as the weakest
supporting derivation.

The affirmative-existence instruction attached to the commissioning brief is a search prior.
It allocated effort. It appears in no premise, hypothesis, counterexample, disposition, or
severity assignment. Part G records the erasure audit.

### 0.3 What this pass created and did not do

It created exactly one file, this one. It ran no Git mutation, no TeX build, and no ledger
or register write. It executed one symbolic/numerical verification session, recorded
verbatim in Part E; that session corroborates arithmetic and closes no theorem.

---

## 1. Cross-route disposition map

The twelve in-scope claims are `claim-ledger.json:78-89`, reached by the twelve
`target -> …` edges at `dependency-dag.json:26-37`.

| Ledger claim | Bundle route | Score/config route | Timeless-history route | This pass |
| --- | --- | --- | --- | --- |
| `score-action-compatibility` (`:78`) | out of scope | **PROVED** | PROVED *(inherited)* | PROVED, with a broken supporting witness (**M-3**) |
| `bundle-fisher-defect` (`:79`) | **PROVED** + 2 extra hypotheses | **PROVED** under (H1)–(H5) | PROVED *(inherited)* | PROVED under the Part F hypothesis set; ledger `assumption_ids` incomplete (**N-6**) |
| `bundle-morphism-descent` (`:80`) | **PROVED** + existence obstruction R7 | **PROVED** | PROVED *(inherited)* | PROVED, conditional on a *declared* $\mathcal P_\ell$ whose existence can fail |
| `bundle-scale-cocycle` (`:81`) | **PROVED** | **PROVED** (conditional) | PROVED *(inherited)* + new factor cocycle T11 | PROVED; its "executed verification" is mislabeled (**M-2**) |
| `horizontal-defect-anomaly` (`:82`) | **PROVED**, one ledger clause **REFUTED** | PROVED | PROVED, "adds nothing" | Ledger clause false on its strict reading (**M-6**); mechanism sound |
| `pullback-compatibility` (`:83`) | PROVED conditionally; unconditional order relation **REFUTED** | **PROVED** under stated hypotheses | **PROVED** | PROVED conditionally; displayed correction wrong (**M-1**) |
| `configuration-fisher-metric` (`:84`) | **OPEN** (Missing Lemma CFM) | **OPEN** | **PROVED** | **OPEN** — route D's closure is circular (**M-7**) |
| `configuration-map` (`:85`) | **OPEN** (Missing Lemma CM) | **OPEN** (symbol collision) | PROVED (typing) / OPEN (existence) | **OPEN** — route D's "PROVED (typing)" is contradicted on the bytes (**M-8**) |
| `configuration-projectability` (`:86`) | **PROVED**; universal strengthening REFUTED | **PROVED** | PROVED as a negative | PROVED; §5.3's generalization overreaches (**N-3**) |
| `history-semiconjugacy` (`:87`) | out of scope | **PROVED** | **PROVED** (sufficiency + converse) | PROVED as a *criterion*, not as a fact about the manuscript's flows (O-SC stands) |
| `history-noncollapse` (`:88`) | out of scope | **PROVED** | **PROVED** | PROVED |
| `history-duration-relation` (`:89`) | out of scope | **PROVED** | **PROVED** | PROVED; the portfolio's repair path is holed (**M-4**, **M-5**) |

Two claims are `OPEN`. Under `proof-obligations.md` no terminal affirmative status is
available while a dependency ancestor is `OPEN`, and `dependency-dag.json:106-111` routes
`configuration-map` and `history-semiconjugacy` through both open nodes. That alone forces
`INCONCLUSIVE`; the substantive reasons are Part A.

---

## Part A — Mathematical findings

Severity scale: **BLOCKER** (integration must not proceed), **MAJOR** (integration must not
copy the affected text), **MODERATE** (repair before citing), **MINOR** (repair in place).

### M-1. The displayed base-cocycle correction term is wrong as printed

**Anchor.** `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/evidence/task-10-bundle-pullback-analysis.md:976-983`
(Theorem R4.3, part 3, "Explicitly, without that hypothesis, …").

**Claim under attack.** With $L_{01}=T^V\Psi_{01}$ and $A:=A_{\Psi_{01}}(s_0;\cdot)$, the
report prints
$$
\delta_{02}-\delta_{01}-f_{01}^*\delta_{12}
=-\big[\Delta_F^{\Psi_{12}}(L_{01}D^{\omega_0}s_0,\;A)+\Delta_F^{\Psi_{12}}(A,\;L_{01}D^{\omega_0}s_0)\big]
\;{\color{red}+}\;\Delta_F^{\Psi_{12}}(A,A).
$$

**Recomputation.** From the report's own proof step
$T^V\Psi_{01}\circ D^{\omega_0}s_0=D^{\omega_1}s_1\circ Tf_{01}-A$, expanding
$f_{01}^*\delta_{12}=\Delta_F^{\Psi_{12}}(L_{01}Ds_0+A,\;L_{01}Ds_0+A)$ gives

$$
\delta_{02}-\delta_{01}-f_{01}^*\delta_{12}
=-\big[\Delta_F^{\Psi_{12}}(L_{01}Ds_0,A)+\Delta_F^{\Psi_{12}}(A,L_{01}Ds_0)\big]
\;{\color{green}-}\;\Delta_F^{\Psi_{12}}(A,A).
$$

The printed identity therefore overstates the right-hand side by
$2\,\Delta_F^{\Psi_{12}}(A,A)$.

**Concrete counterexample (the report's own Block B/C data).** Three levels,
$f_{01}(x)=2x$, $f_{12}(y)=3y$; translation group; fibers $\mathcal N(\mu,1)$,
$\mathcal N(\mu,2)$, $\mathcal N(\mu,3)$ so $g_0^F=1$, $g_1^F=\tfrac12$, $g_2^F=\tfrac13$;
sections $\sigma_0(x)=x$, $\sigma_1(y)=y/2$, $\sigma_2(z)=z/6$; local connection forms
$A_{\omega_0}=0$, $A_{\omega_1}=a_1dy$, $A_{\omega_2}=a_2dz$. Then
$A_{\Psi_{01}}(\partial_x)=2a_1$ and, with $\delta$ the R3.3 object
$\delta_{jk}=(D^{\omega_j}s_j)^*\Delta_F^{\Psi_{jk}}$,

$$
\delta_{02}-\delta_{01}-f_{01}^*\delta_{12}=-\tfrac23a_1^2-\tfrac23a_1,
\qquad
\text{printed RHS}=+\tfrac23a_1^2-\tfrac23a_1 .
$$

At $a_1=1/10$, $a_2=0$: true value $-11/150$, printed value $-3/50$; difference
$4a_1^2/3=1/75$. Verified in exact rational arithmetic (Part E, Block 1).

**Diagnosis.** The sign and the cross-term argument are coupled. The printed `+` is correct
**only if** the cross terms carry the *coarse* jet $D^{\omega_1}s_1\circ Tf_{01}$ rather
than $L_{01}D^{\omega_0}s_0$; with the coarse jet the identity checks exactly (Part E,
Block 1, `LHS-altcross = 0`). As literally printed, with $L_{01}D^{\omega_0}s_0$ in the
cross slots and `+` on the quadratic, it is false.

**Severity.** MODERATE. The theorem's `if and only if` and the exact identity (R3.3) are
unaffected; only the quantitative correction is wrong. It becomes MAJOR if the formula is
transcribed into `05c_pullback_geometry.tex` next to `thm:pb-fisher-defect-cocycle`, which
is exactly what the route's own anchor list at `:1017-1036` recommends.

**Minimal repair.** Replace `+` by `−` on the quadratic term, or replace both cross-term
arguments $L_{01}D^{\omega_0}s_0$ by $D^{\omega_1}s_1\circ Tf_{01}$. Add the one-line
consistency check that both forms agree.

**What would falsify this attack.** A derivation in which
$f_{01}^*\delta_{12}$ is defined with the *fine* pushed jet rather than the coarse jet, or a
worked instance in which the printed formula reproduces
$\delta_{02}-\delta_{01}-f_{01}^*\delta_{12}$ with $A_{\Psi_{01}}\neq0$.

---

### M-2. "Executed verification" Block C verifies a trivial telescoping identity, not the base cocycle it is labeled with

**Anchors.** `task-10-bundle-pullback-analysis.md:1925-1956` (Block C) against the same
file's `:611` (definition $\delta_\Psi:=(D^\omega s)^*\Delta_F^\Psi$) and `:955-963`
(R4.3 part 1, unconditional telescoping) and `:968-975` (R4.4, the sharp base cocycle).

**Claim under attack.** Block C is titled "the base cocycle (R4.3) and its identification"
and asserts $\delta_{02}-(\delta_{01}+4\delta_{12})=0$ **identically in $(a_1,a_2)$**.

**Recomputation.** Block C's symbols are not R3.3's. Its displayed values are exactly
$$
\delta_{01}=h_0-f_{01}^*h_1,\qquad
\delta_{12}=h_1-f_{12}^*h_2,\qquad
\delta_{02}=h_0-f_{02}^*h_2,
$$
with $h_j=g_j^F(D^{\omega_j}s_j)^2$: I reproduced all three displayed polynomials from
those definitions exactly (Part E, Block 2). Under that reading the asserted identity is
the *unconditional telescoping* R4.3(1) with the $\mathcal X$ and $\mathcal Q$ terms
already absorbed — a tautology, true for every $(a_1,a_2)$, and not a test of anything.

Under the report's own R3.3 definition, the same symbols take different values:
$\delta_{\Psi_{01}}=(D^{\omega_0}s_0)^*\Delta_F^{\Psi_{01}}=\tfrac12$, independent of
$a_1$, whereas Block C's $\delta_{01}$ at $a_1=1/10$ is $7/25=0.28$. And the sharp
cocycle R4.4 **fails** on exactly this data: the residual is
$-\tfrac23a_1(a_1+1)$, equal to $-11/150$ at $a_1=1/10$, vanishing only at
$a_1\in\{0,-1\}$.

**Diagnosis.** A live symbol collision inside the section that is presented as the pass's
executed verification record. Read literally, Block C's headline contradicts R4.3(3) of the
same document and (1.5) of `task-10-score-configuration-analysis.md:377-383`, both of which
state that R4.4 needs $A_{\Psi_{01}}(s_0;\cdot)=0$.

**Severity.** MAJOR. A careful integrator reading Block C as executed evidence for the base
cocycle would import the false statement "the base cocycle holds identically" into
`05c_pullback_geometry.tex`. This is precisely the failure mode the protocol's
"numerical agreement closes no theorem" rule exists to catch: here the numerical agreement
is real but is agreement with a different proposition.

**Minimal repair.** Rename Block C's quantities to $\mathcal E_{jk}:=h_j-f_{jk}^*h_k$,
retitle it "unconditional telescoping (R4.3(1))", and add a second block that evaluates the
R3.3 $\delta_{\Psi_{jk}}$ and exhibits the nonzero R4.4 residual $-\tfrac23a_1(a_1+1)$ at
$a_1\neq0,-1$. Note in passing that $a_1=-1$ is an instance where R4.4 holds with
$A_{\Psi_{01}}\neq0$, so the sufficient condition in R4.3(3) is not necessary.

**What would falsify this attack.** A definition of $\delta_{jk}$ in Block C that coincides
with `:611` and still yields the displayed polynomials, or a demonstration that
$(D^{\omega_0}s_0)^*\Delta_F^{\Psi_{01}}$ depends on $a_1$ under the Block B data.

---

### M-3. The `CE-ACTION-LP` restatement used to fence `score-action-compatibility` is false

**Anchors.** `task-10-score-configuration-analysis.md:432-436`, against the register entry
`counterexample-register.md:11` and the report's own citation at `:444-448`.

**Claim under attack.** "for $\pi=N(0,1)$ and $\varphi(x)=-x^2\in L^2(\pi)$, the normalizer
$\pi(e^{-t\varphi})=\pi(e^{tx^2})$ is infinite for every $t\ge1/2$, **and no two-sided
neighborhood exists**".

**Recomputation.** $\pi(e^{tx^2})=(1-2t)^{-1/2}$, finite for every $t<1/2$ and in
particular on the two-sided neighborhood $(-1/2,1/2)$ of the origin (Part E, Block 4). The
exponential-action path $t\mapsto\widehat\pi^{t\varphi}$ is therefore perfectly well
defined for $|t|<1/2$; the second clause is false. The report contradicts itself nine lines
later at `:444-448`, where it correctly cites `prop:ig-hermite-exponential-domain`:
$N_2(t)=e^t(1+2t)^{-1/2}$, finite for every $t>-\tfrac12$, i.e. on a two-sided
neighborhood. $\varphi=-x^2$ is the $\mathrm{He}_2$ direction.

The register entry `counterexample-register.md:11` is **not** at fault: it says only that
$e^{-\varphi}=e^{x^2}$ is nonintegrable, which is the statement at $t=1$ and is true. The
defect is the report's strengthening from "the chart does not contain $\varphi$" to "no
two-sided path neighborhood exists".

**Correct witness.** Any odd $\mathrm{He}_k$ with $k\ge3$, e.g. $\varphi=x^3-3x\in L^2(\gamma)$,
for which $N_k(t)=+\infty$ for **every** $t\neq0$ — exactly the case the report's own cited
proposition supplies.

**Severity.** MODERATE. The conclusion the witness is asked to support — that the
$L^2/\mathbb R\mathbf 1$ score isometry is a strictly different object from the nonlinear
bounded-action chart — survives via the odd-Hermite witness, so
`score-action-compatibility` is not endangered. But the fence recommended for
`07b_agent_network_rg.tex` at `task-10-score-configuration-analysis.md:1296` cites this
witness by name.

**Minimal repair.** Swap the witness to odd $\mathrm{He}_k$, $k\ge3$, and restate the
$\mathrm{He}_2$ case correctly as "finite exactly on $t>-1/2$, hence a one-sided-unbounded
but two-sided-nonempty domain".

**What would falsify this attack.** A value $t\in(-1/2,1/2)$ at which $\pi(e^{tx^2})=\infty$.

---

### M-4. Theorem G is attached to the wrong coarse map

**Anchors.** `task-10-score-configuration-analysis.md:1019-1020` ("what makes the averaging
coarse map of §5.4 amenable to Theorem B after all") and `:1054-1059` ("the correct
statement to attach to the averaging coarse map (5.1)"), against Construction 5.2 at
`:957-982` and Theorem G at `:1022-1052`.

**Claim under attack.** That Theorem G's defect
$\mathsf G^{\kappa}(\dot\theta,\dot\theta)-I_{\bar P}(\theta)
=\mathbb E\operatorname{Var}(\ell_{s_\theta(C)}(Y)\mid Y)$
is the information loss of the fiberwise averaging map (5.1).

**Recomputation.** They are different maps into different spaces.

* (5.1) is a **fiberwise barycenter in the convex chart of $\bar{\mathcal B}$**:
  $(\widehat Rs)(\bar c)=\int_{f^{-1}(\bar c)}\Psi(s(c))\,\kappa_{\bar c}(dc)$, whose value
  is a point of $\bar{\mathcal B}$.
* Theorem G's coarse object is the **mixture law**
  $\bar P_\theta=\int p_{s_\theta(c)}\,\kappa(dc)$, obtained by the context-forgetting
  kernel. For $\bar{\mathcal B}$ a Gaussian family the mixture is not Gaussian, so
  $\bar P_\theta\notin\bar{\mathcal B}$ and hypothesis **(H5)** — the report's own family
  closure, `:158-170` — fails for it. The report itself cites
  `07_general_renormalization.tex:872-874` for exactly this.

**Concrete counterexample.** Two contexts, $\kappa$ uniform, unit-variance Gaussian
location fiber, $m_1(\theta)=\theta+1$, $m_2(\theta)=\theta-1$, so $\dot m=(1,1)$ at
$\theta=0$.

| quantity | value |
| --- | --- |
| integrated fine configuration metric $\mathsf G^\kappa$ | $1$ |
| metric of the (5.1) barycenter image ($\bar m=\theta$) | $1$ |
| **defect of the averaging map (5.1)** | $\mathbf 0$ |
| $I_{\bar P}(0)$ for $\bar P_\theta=\tfrac12\mathcal N(\theta+1,1)+\tfrac12\mathcal N(\theta-1,1)$ | $0.550401$ |
| **Theorem G defect** | $\mathbf{0.449599}$ |

(Part E, Block 5.) The two numbers differ, so the identification is false. A second
witness with $\dot m=(2,0)$ happens to make both equal $1$, which is why the conflation is
easy to miss: at that point the two Gaussian components coincide at $\theta=0$ and the
mixture Fisher form degenerates to the marginal one.

**Severity.** MAJOR. Construction 5.2 is one of the two "valid alternatives" the score
route offers as the constructive repair for `configuration-map` and
`configuration-projectability` (`:1304`, repair item 3 at `:1397-1399`). Attaching a false
contraction statement to it is worse than attaching none.

**Minimal repair.** Detach Theorem G from (5.1). State Theorem G as what it is — the exact
defect of the **context-forgetting mixture** map, whose codomain is outside
$\bar{\mathcal B}$ unless the coarse family is closed under $\kappa$-mixtures — and record
that no contraction statement is currently available for (5.1). See **M-5** and **L-AVG**.

**What would falsify this attack.** A proof that the barycenter of $\{\Psi(s(c))\}$ in the
declared convex chart and the mixture $\int p_{s(c)}\kappa(dc)$ carry the same Fisher form,
or a declaration that $\bar{\mathcal B}$ is closed under $\kappa$-mixtures and that (5.1) is
defined as the mixture rather than the chart barycenter.

---

### M-5. The averaging coarse map is not a contraction: it can strictly increase the integrated configuration Fisher metric

**Anchors.** `task-10-score-configuration-analysis.md:966-982` (Construction 5.2) and
`:1054-1059` ("This is the precise sense in which averaging over the base loses
information"), and the same file's Theorem E/(6.3) at `:1070-1093`.

**Claim under attack.** That the gauge-equivariant fiberwise averaging map "loses
information", i.e. contracts the integrated configuration Fisher metric.

**Counterexample (new; created by this pass).** Base $\mathcal C=\{c_1,c_2\}$ with $\kappa$
uniform, coarse base $\bar{\mathcal C}=\{\ast\}$ with $\bar\kappa=f_\#\kappa$ (so Theorem E's
condition $f_\#\mu=\bar\mu$ holds), unit channel weights, $\Psi=\mathrm{id}$ on fibers so
$\Delta_F^\Psi\equiv0$ exactly. Belief fiber the centered Gaussians
$\{\mathcal N(0,\Sigma):\Sigma>0\}$ in the moment chart, with fiber Fisher form
$g^F(A,A)=A^2/(2\Sigma^2)$ — the $K=1$ case of `prop:ig-fisher-moment-chart`, and the
chart in which the score route's own Lemma 3.1 (`:522-539`) declares the fiber convex.

Take the configuration $(\Sigma_1,\Sigma_2)=(1,\delta)$ and the tangent
$Z=(\dot\Sigma_1,\dot\Sigma_2)=(1,0)$. Then

$$
\|Z\|^2_{\mathsf G_\ell}=\tfrac12\cdot\tfrac{1^2}{2\cdot1^2}+\tfrac12\cdot 0=\tfrac14,
\qquad
\bar\Sigma=\tfrac{1+\delta}2,\quad \dot{\bar\Sigma}=\tfrac12,
\qquad
\|T\widehat R\,Z\|^2_{\mathsf G_{\ell+1}}=\frac{(1/2)^2}{2\big(\tfrac{1+\delta}{2}\big)^2}
=\frac{1}{2(1+\delta)^2}\ \xrightarrow[\delta\to0^+]{}\ \tfrac12 .
$$

At $\delta=10^{-2}$ the ratio coarse/fine is $1.96059$ (Part E, Block 3). The averaging map
**doubles** the configuration Fisher speed in the limit, with matched base measures, unit
weights, and zero fiberwise defect.

The witness is not an artifact of a zero-dimensional base: replacing $\{c_1,c_2\}$ by $S^1$
with normalized arclength and a smooth $\Sigma(\cdot)$ equal to $1$ with $\dot\Sigma=1$ on
one half and $\delta$ with $\dot\Sigma=0$ on the other, smoothed on a set of measure
$\varepsilon$, gives the same numbers up to $O(\varepsilon)$ and preserves the strict
inequality $\tfrac12>\tfrac14$.

**Why no theorem is contradicted.** Theorem E/(6.3) presupposes the *related-sections*
identity $\Psi\circ s=\bar s\circ f$, which the averaging map deliberately violates — that
violation is the entire point of §5.4. Route D's T16 presupposes
$\mathcal C_{\ell+1}=\mathcal C_\ell$ (hypothesis 1) and a pointwise Markov fiber map
(hypothesis 2), both false here. The refuted object is the portfolio's *narrative* claim,
not any of its theorems.

**Mechanism.** The integrated Fisher form
$(\Sigma,A)\mapsto A^2/(2\Sigma^2)$ is **not jointly convex**: its Hessian determinant is
$-4A^2\Sigma^{-6}<0$ for $A\neq0$. Jensen therefore does not apply in the moment chart of
the covariance directions. It *does* apply in the location directions, where
$(m,u)\mapsto u^\top\Sigma^{-1}u$ is jointly convex — which is why the location-only
coherence check at `:1002-1011` succeeds and hides the failure.

**Severity.** BLOCKER for the averaging branch. §5.4 and §5.5 are the portfolio's only
constructive answer to `configuration-projectability`'s negative result, and they are
offered as inputs to `history-duration-relation`. With M-4 and M-5 together, the portfolio
currently has *no* valid information-contraction statement for either alternative coarse
map, in the covariance sector.

**Minimal repair.** (i) Delete the "loses information" reading. (ii) State the exact
averaging defect where it is available: in the **location sector with a fixed fiber metric**
it is the Jensen gap $\int g^F(\dot s,\dot s)\,d\kappa-g^F(\int\dot s\,d\kappa,\int\dot
s\,d\kappa)=\operatorname{Var}_\kappa$ of the velocity, which is $\ge0$. (iii) Fence the
covariance sector explicitly with this witness, or restrict Construction 5.2 to fiber
charts in which $(\beta,\dot\beta)\mapsto g^F_\beta(\dot\beta,\dot\beta)$ is jointly convex
— which the law-simplex barycenter satisfies (Fisher information is jointly convex in
$(p,p')$) but the moment chart does not. (iv) Note that (ii) and (iii) are inequivalent
constructions, so the coherence check at `:1002-1011` does not extend.

**What would falsify this attack.** A joint-convexity proof for
$(\Sigma,A)\mapsto\operatorname{Tr}(\Sigma^{-1}A\Sigma^{-1}A)$ on $\operatorname{Sym}^{++}$,
or a demonstration that Construction 5.2 is defined as a law-simplex barycenter rather than a
chart barycenter — in which case Lemma 3.1's convexity hypothesis must be re-established for
the law simplex and family closure re-argued, since a mixture of Gaussians is not Gaussian.

---

### M-6. The ledger clause of `horizontal-defect-anomaly` is false on its strict reading

**Anchor.** `claim-ledger.json:82`, clause "positivity follows **only when** that defect
vanishes"; against `task-10-bundle-pullback-analysis.md:1842-1896` (Proposition R11).

**Recomputation.** The strict reading is "base positivity $\Rightarrow$ $A_\Psi=0$".
Recomputing R11's witness from its declared data — $\mathcal C=\mathbb R$,
$f=\mathrm{id}$, $\mathcal B=\{\mathcal N(\mu,1)\}$ with $g^F=1$, kernel
$N(x,\cdot)=\mathcal N(x,1)$ so $\bar{\mathcal B}=\{\mathcal N(\mu,2)\}$ with
$\bar g^F=\tfrac12$ and $\Delta_F^\Psi=\tfrac12$, section $\sigma(x)=mx$, $A=0$,
$\bar A=b\,dx$ — gives $h-f^*\bar h=m^2-\tfrac12(m+b)^2$ and, at $m=1$:

| $b$ | $h-f^*\bar h$ | $\delta-\mathcal X-\mathcal Q$ | $\|A_\Psi\|_{\bar g^F}$ | margin (R3.5) | margin met | positive |
| --- | --- | --- | --- | --- | --- | --- |
| $0$ | $1/2$ | $1/2$ | $0$ | $0.2929$ | yes | yes |
| $1/10$ | $79/200$ | $79/200$ | $0.0707$ | $0.2929$ | yes | **yes** |
| $-1/10$ | $119/200$ | $119/200$ | $0.0707$ | $0.2929$ | yes | **yes** |
| $1/2$ | $-1/8$ | $-1/8$ | $0.3536$ | $0.2929$ | no | no |
| $-3/5$ | $23/25$ | $23/25$ | $0.4243$ | $0.2929$ | **no** | **yes** |

Every row reproduces exactly in rational arithmetic, and both columns of the comparison
agree, confirming (R3.3) (Part E, Block 3). Rows 2, 3, 5 have $A_\Psi\neq0$ with strictly
positive base comparison: the strict reading is refuted. Row 5 additionally shows the
margin (R3.5) is sufficient but **not** necessary.

**Status across routes.** The bundle route found and stated this
(`task-10-bundle-pullback-analysis.md:1887-1896`). The score route
(`task-10-score-configuration-analysis.md:1300`) and the timeless route
(`task-10-timeless-history-analysis.md:1537`) both close `horizontal-defect-anomaly`
`PROVED` without adjudicating the clause. Two of three routes therefore closed a ledger
claim one of whose conjuncts is false as written.

**Severity.** MODERATE for the mathematics (the mechanism R3.3 + R3.4(1) is correct and
gives the exact criterion), MAJOR for the ledger (a conjunct of a `UNIVERSAL` target claim
is refuted by a scope-matched counterexample, which under
`problem-contract.json` `falsification_criterion` blocks affirmative release for that
conjunct until the wording is repaired).

**Minimal repair.** Restate as: "vanishing of the horizontal defect is **sufficient** for
base positivity; the exact criterion is
$\|D^{\bar\omega}\bar s(T_cfX)\|_{\bar g^F}\le\|D^\omega sX\|_{g^F}$ for every $X$; the
pointwise margin (R3.5) is sufficient and not necessary."

**What would falsify this attack.** A reading of the clause under which "positivity
follows only when" is not the material implication "positivity $\Rightarrow$ defect
vanishes" — in which case the clause should be reworded anyway, since the refutation
otherwise stands on the recomputed table.

---

### M-7. Route D closes `configuration-fisher-metric` by assuming it

**Anchors.** `task-10-timeless-history-analysis.md:1539` (disposition **PROVED, with a
strengthening**) against the same file's H-D1 at `:94-102`, and against
`task-10-score-configuration-analysis.md:505-518` and
`task-10-bundle-pullback-analysis.md:1454`.

**Claim under attack.** Route D's closure, whose stated basis is that
`05d_relational_inference.tex:458-536` "declares base measure, design weights, channel
weights, gauge quotient, finiteness, and the infinite-dimensional submersion caveat".

**Attack.** Route D's own standing hypothesis H-D1 reads: "$\mathcal Q_\ell$ is a smooth
Hausdorff Banach manifold … with a **declared strong Riemannian metric** $\mathsf G_\ell$
… This is `hyp:hist-regular-section-space` and `hyp:hist-regular-metric-domain` … and
ledger assumption `H-CONFIG`." The ledger claim `claim-ledger.json:84` asks that each
configuration manifold **be** an explicitly selected manifold whose strong Fisher metric is
either a declared joint-law pullback or a labeled weighted product with base measure,
channel weights, gauge quotient, finiteness, and nondegeneracy data. Closing that claim on
the strength of H-D1 is closing it on the strength of itself.

**Independent contradiction on the bytes.** The score route records, and I confirm by
inspection, that the manuscript exhibits no configuration manifold and performs no
strong-metric verification: the phrase "strong metric" occurs only inside the hypothesis
itself, and the only nonemptiness result in the source
(`prop:gauss-interaction-nonempty`) concerns the Gaussian *interaction* family, a different
object. Furthermore the claim's own falsifier list at `:84` includes "a weak metric with no
gradient", and the score route's Counterexample 3.5
(`task-10-score-configuration-analysis.md:652-667`) realizes exactly that branch:
$\mathcal Q=H^1(S^1)$ with the integrated $L^2$ Fisher metric and
$\mathcal F=\tfrac12\int|Q'|^2$ has no gradient at
$Q=\sum_{k\ge1}k^{-2}\sin k\theta\in H^1\setminus H^2$. I verified the Sobolev arithmetic:
$\|Q\|_{H^1}^2\asymp\sum k^{-2}<\infty$ while $-Q''=\sum\sin k\theta\notin L^2$.

**Severity.** BLOCKER for that disposition. It must not be carried into the integration as a
third-route confirmation.

**Minimal repair.** Restate route D's row as "assumed (H-D1), not established"; adopt the
`OPEN` disposition of the other two routes with Missing Lemma **L-CFM** (Part D).

**What would falsify this attack.** A location in `05d_relational_inference.tex` that
exhibits a configuration manifold and verifies strongness of its metric, rather than
declaring both.

---

### M-8. Route D's "PROVED (typing)" for `configuration-map` is contradicted on the bytes

**Anchors.** `task-10-timeless-history-analysis.md:1540` against
`task-10-score-configuration-analysis.md:874-900` and the source.

**Attack.** Route D asserts the typing "is separated at `07b` and route-C Section 7". I
searched the current sources. The symbol $\mathcal R$ carries **at least five** distinct
assignments, plus a sixth that differs only by a hat:

| Object | Anchor |
| --- | --- |
| root-vertex set $\mathcal R=\{r:\operatorname{pa}(r)=\varnothing\}$ | `04_generative.tex:22`; used at `05_elbo.tex:388,395,400,404,409,434` |
| VFE descent ray $\mathcal R^-_{\mathcal F_i}$ | `05d_relational_inference.tex:287` |
| **configuration coarse map** $\mathcal R:\mathcal Q_f\to\mathcal Q_m$, $\mathcal R_\ell$ | `05d_relational_inference.tex:700,719,720,724,727,728,734,735,745,746,769,780,783` |
| nonlinear action map $\mathcal R^H$ | `07b_agent_network_rg.tex:185,186` |
| block measure-pair map $\mathcal R_b$, $\mathcal R_b^\rho$ | `07b_agent_network_rg.tex:2074,2079` |
| reference-space endomorphism $\widehat{\mathcal R}_\ell$ | `07_general_renormalization.tex:45-48` |

and `appendix_notation.tex` contains **no** row of type
$\mathcal Q_\ell\to\mathcal Q_{\ell+1}$ (searched; no match). The ledger falsifier for
`configuration-map` at `claim-ledger.json:85` — "a configuration symbol already assigned to
a reference-space endomorphism" — is met in substance, and $\mathcal R_b$ at
`07b:2074` makes the collision one worse than the score route reported.

**Severity.** MAJOR. `configuration-map` is an ancestor of `history-semiconjugacy`
(`dependency-dag.json:109`), so a spurious `PROVED (typing)` propagates.

**Minimal repair.** Adopt `OPEN`. Perform the rename to $\widehat R_\ell$ recommended at
`task-10-score-configuration-analysis.md:1303` and add the notation-appendix row with the
explicit non-identifications against $K_\ell$, $\mathcal R^H$, $\mathcal R_b$, $M_\ell$,
$C_{\ell,s}$, and $\widehat{\mathcal R}_\ell$.

**What would falsify this attack.** A notation-appendix row typing the configuration coarse
map, or a rename already applied in the current bytes.

---

### M-9. Theorem G's joint DQM step is not justified by fiberwise DQM

**Anchor.** `task-10-score-configuration-analysis.md:1022-1052`, proof at `:1048-1052`.

**Attack.** The proof writes "The joint density with respect to $\kappa\otimes\nu$ is
$p_{s_\theta(c)}(y)$, whose logarithm has $\theta$-derivative $\ell_{s_\theta(c)}(y)$;
… Squaring and integrating gives (6.1)." That is a pointwise-in-$c$ derivative followed by
an integration over $c$. Joint differentiability in quadratic mean requires

$$
\int_{\mathcal C}\Big(\int\big[\sqrt{p_{s_{\theta+u}(c)}}-\sqrt{p_{s_\theta(c)}}-\tfrac12u^{\!\top}\ell\sqrt{p_{s_\theta(c)}}\big]^2d\nu\Big)\kappa(dc)=o(\|u\|^2),
$$

which does **not** follow from the inner integral being $o(\|u\|^2)$ for each $c$. The
standard obstruction applies: with $\kappa(\{n\})=2^{-n}$ and inner remainders
$r_n(u)=u^2\cdot 2^{n}\mathbf 1\{|u|\in(2^{-n-1},2^{-n}]\}$ one has $r_n(u)=o(u^2)$ for
every $n$ while $\sum_n\kappa_nr_n(u)/u^2\equiv1$ on a sequence $u\to0$. This is exactly the
interchange that §1.2 of the same report goes to great lengths to avoid in §1
("no differentiation under an integral sign is performed anywhere in §1", `:174-177`);
§6 reintroduces it silently.

**Severity.** MODERATE. The conclusion is true under a mild uniformity hypothesis and is
routine for the finite- and compact-base tiers actually used.

**Minimal repair.** Add to Theorem G the hypothesis "$\kappa$-uniform DQM": the family of
Hellinger remainders admits a $\kappa$-integrable dominating envelope, or $\mathcal C$ is
finite / the remainder is uniform in $c$. Alternatively declare "DQM family of sections" to
mean DQM of the joint experiment, in which case (6.1) is immediate and nothing is proved by
the displayed argument.

**What would falsify this attack.** A theorem asserting that fiberwise DQM plus
$\kappa$-measurability implies joint DQM without a uniformity or domination hypothesis.

---

### M-10. Bundle-route R3.5 asserts the DQM-transfer step that the score route proves

**Anchors.** `task-10-bundle-pullback-analysis.md:748-758` and its external-theorem entry at
`:1498-1507`, against `task-10-score-configuration-analysis.md:205-267` (Theorem A,
especially Step 4 at `:259-264`).

**Attack.** R3.5's proof says "the family $t\mapsto q(\beta_t)=\beta_tN$ is DQM with score
$\bar\ell_w(y)=\mathbb E[\ell_w(X)\mid Y=y]$ **because $N$ carries no parameter
dependence**". That is the conclusion, not an argument. The score route identifies the
missing link precisely — "Step 4 is the step that is silently skipped whenever a proof
computes the score of one convenient path and asserts it for the family" — and supplies it
via Hellinger contraction (Lemma 1.2) plus DQM rigidity (Lemma 1.1). §12 item 6 of the
bundle route names Ay–Jost–Lê–Schwachhöfer and Chentsov as primary sources but gives no
theorem number and no hypothesis-by-hypothesis mapping, which
`proof-obligations.md` requires of an `APPLICABLE_THEOREM`.

**Severity.** MODERATE, and route-internal only: the portfolio as a whole has the proof.

**Minimal repair.** In the bundle route, cite `task-10-score-configuration-analysis.md`
Theorem A (or the primary theorem with its hypothesis mapping) at `:750`. In the
manuscript, the same gap exists at `thm:cg-fisher-contraction`
(`06_general_coarsegraining.tex:190-199`) and should be closed the same way.

**What would falsify this attack.** A one-line proof that pushforward under a
parameter-independent kernel preserves DQM for an arbitrary DQM family, not merely for the
canonical quadratic path.

---

### M-11. The bundle route's "missing coarse $\bar G$-invariance" finding is over-claimed

**Anchors.** `task-10-bundle-pullback-analysis.md:760-769` and `:1405` (attack row
"Missing $\bar G$-invariance of the coarse Fisher metric … **SUSTAINED**"), against
`05c_pullback_geometry.tex:25-37` (`hyp:pb-regular-models`) and `:54-58`
(`prop:pb-statistical-tensor-descent`).

**Attack.** The bundle route is mathematically right that the cancellation of the
$c$-dependent factor $\widehat{\bar\rho}(\varsigma(c))$ in the local representative
$\psi_c=\widehat{\bar\rho}(\varsigma(c))\circ q$ needs $\bar G$-invariance of $\bar g^F$.
But the manuscript already needs and asserts that invariance for a prior reason: the
statement $h^{\bar\omega}_{\bar s}=(D^{\bar\omega}\bar s)^*\bar g^F$ presupposes that
$\bar g^F$ **is** a vertical tensor on $\bar E$, and `prop:pb-statistical-tensor-descent`
delivers exactly that from `hyp:pb-regular-models`, whose text
(`05c_pullback_geometry.tex:32-34`) reads "Assume also that the represented action
$\widehat\rho_x(g)$ is induced by a parameter-independent bimeasurable change of sample
coordinates and preserves $\mathcal B_x$". Applied at the coarse scale, that is precisely
$\widehat{\bar\rho}(\bar G)$-invariance.

**Disposition.** PARTIALLY SUSTAINED, severity downgraded from "missing hypothesis" to
**MINOR / cross-reference**. The genuine residue is that
`05c_pullback_geometry.tex:675-690` never instantiates `hyp:pb-regular-models` at the
coarse scale, so a reader cannot see where the invariance comes from.

**Minimal repair.** At `sec:pb-fisher-defect`, cite the coarse instance of
`hyp:pb-regular-models` explicitly rather than adding a new hypothesis.

**What would falsify this downgrade.** A demonstration that the coarse model
$\bar{\mathcal B}$ is admitted anywhere in Chapters 5c/7 without an instance of
`hyp:pb-regular-models` — in which case the bundle route's original SUSTAINED verdict
stands at full severity.

---

### M-12. Hypothesis gaps in three secondary statements

| # | Anchor | Gap | Severity | Repair |
| --- | --- | --- | --- | --- |
| a | `task-10-score-configuration-analysis.md:821-827` (C4) | "Nonunit weights are incompatible with exactness" needs the two marginal Fisher forms to be *independently excitable*: if a one-dimensional parameter moves both marginals together, $(w_b-1)\|L_b\|^2+(w_m-1)\|L_m\|^2=0$ has a one-parameter family of solutions and $w_b=w_m=1$ does not follow. | MINOR | Add "there exist tangent directions with $L_b\neq0,L_m=0$ and with $L_b=0,L_m\neq0$", which holds in the report's own Gaussian instance. |
| b | `task-10-score-configuration-analysis.md:1077` (Theorem E) | "**if and only if** $f_\#\mu=\bar\mu$" is a biconditional only when quantified over all admissible $\bar h,\bar V$; for a fixed instance it is sufficient, not necessary. | MINOR | Quantify, or state as "sufficient, and necessary if the identity is required for every $f$-related field and every coarse section". |
| c | `task-10-bundle-pullback-analysis.md:1136-1137` (Theorem R5.2) | "Pick any $Q_0\in\Gamma(\mathcal C,E)$ and, adjusting inside $\mathcal U$ if necessary, arrange $Q_0(c_0)=e_0$" needs $\mathcal B$ connected (or a global section through $e_0$); with a disconnected fiber $e_0$ may be unreachable. Local flow completeness of $W$ for the required times is likewise assumed. | MINOR | Add "$\mathcal B$ connected", which holds for every model the manuscript uses. |
| d | `task-10-score-configuration-analysis.md:966-976` (Construction 5.2) | Bochner *integrability* is needed, not merely measurability of the disintegration, and for a non-closed convex $\bar{\mathcal B}$ such as $\operatorname{Sym}^{++}_K$ the barycenter lies in the set only by the strict-positivity argument $v^\top(\int\Sigma\,d\kappa)v=\int v^\top\Sigma v\,d\kappa>0$. | MINOR | State both. |
| e | `task-10-timeless-history-analysis.md:710` (N5) | "closed **and complemented**" is redundant in the strong-metric tier: a strong metric makes each $T_Q\mathcal Q$ Hilbertable, so closed subspaces are automatically complemented. | MINOR | Note the redundancy, or reserve N5 for the weak-metric Banach tier where it bites. |

---

## Part B — Notation, disposition, and provenance findings

These do not touch a theorem's truth. They block a *clean* integration.

**N-1. Two routes did not adjudicate a refuted ledger conjunct.** See **M-6**. Neither the
score route (`:1300`) nor the timeless route (`:1537`) recorded the strict-reading failure of
`claim-ledger.json:82`. Ledger text must be repaired before any route's `PROVED` for that
claim is entered.

**N-2. "Inherited" closures are not independent evidence.** Route D closes five of the
twelve claims `PROVED (inherited)` (`task-10-timeless-history-analysis.md:1533-1538`):
`score-action-compatibility`, `bundle-fisher-defect`, `bundle-morphism-descent`,
`bundle-scale-cocycle`, and — by deference to the register —
`horizontal-defect-anomaly` ("Route D confirms the type but adds nothing"). Under
`adversarial-verification.md`, "confidence and role agreement are not evidence". These rows
must not be counted as three-route corroboration; the effective route count for those five
claims is two, and for `score-action-compatibility` it is one.

**N-3. An unscoped generalization in the score route.**
`task-10-score-configuration-analysis.md:953-955` upgrades the register entry to "on a
genuinely infinite-dimensional configuration manifold it induces one nowhere". False in
general: if $f$ is a diffeomorphism, every section descends. The scoped statement — for the
total collapse $S^1\to\{\ast\}$ in the $L^2$ tier, the descendable set is the constants, of
infinite codimension and empty interior — is correct and is what should be carried.
Severity MINOR; MAJOR if transcribed into `05c_pullback_geometry.tex` unscoped.

**N-4. A witness typed on a zero-dimensional base.**
`task-10-score-configuration-analysis.md:1095-1104` (Counterexample 6.1) takes
$\mathcal C=\bar{\mathcal C}=\{1,2\}$ "with the discrete structure" and then evaluates $h$
"on the relevant tangent direction". A discrete two-point set is a $0$-manifold with
$\operatorname{Sym}^2T^*\mathcal C=0$, so no such direction exists and $h\equiv0$. The
intended content is correct and survives on the disjoint union of two copies of
$\mathbb R$ with $\mu$ and $\bar\mu$ point masses on different components. Severity MINOR;
repair is one line. (I flag this against my own **M-5** witness too: that one is stated on
$\{c_1,c_2\}$ for exactness of the arithmetic and re-typed on $S^1$ in the same finding.)

**N-5. Symbol collision inside a route's verification record.** See **M-2**; also recorded
here because the fix is notational.

**N-6. Ledger `assumption_ids` are incomplete for the bundle claims.**
`claim-ledger.json:79` gives `bundle-fisher-defect` the assumptions `[H-GAUGE, H-DQM]`.
The union of what the three routes actually use is strictly larger: family-level domination
(H1), normalization $K(x,\mathsf Y)=1$ for **every** $x$ rather than almost every $x$
(H3, `task-10-score-configuration-analysis.md:147-150`), **family closure**
$N_\star(\mathcal B)\subseteq\bar{\mathcal B}$ (H5), smoothness of the law-fiber map $q$
between the declared parametrized-measure models
(`task-10-bundle-pullback-analysis.md:294-303`), the coarse instance of
`hyp:pb-regular-models` (**M-11**), and a jointly measurable $\theta$-smooth version
selection for $p\mapsto T^V_p\Psi$
(`task-10-score-configuration-analysis.md:347-353`). The same is true of
`pullback-compatibility` (`:83`) and `configuration-fisher-metric` (`:84`). Integration
that carries the ledger's shorter list will under-fence the theorems.

**N-7. Two declaration-compatibility conditions live in no claim.** The cross-scale channel
weight condition $\bar w_x\le w_x$ (`task-10-bundle-pullback-analysis.md:1192-1206`,
`CE-COARSE-WEIGHTS`) and the base-measure condition $f_\#\mu=\bar\mu$
(`task-10-score-configuration-analysis.md:1077`) are both required for any cross-scale
comparison of integrated metrics, and neither appears in any of the twelve claims or in
`hyp:pb-weighted-product-geometry`.

**N-8. Ledger coverage gap, independently confirmed.** Route D reports
(`task-10-timeless-history-analysis.md:1551-1559`) that three plan obligations — typed
curves, natural-gradient semiconjugacy sufficiency, three-coordinate independence — have no
atomic ledger claim. I confirm: `dependency-dag.json:26-37` carries no such edge and
`claim-ledger.json` no such id. Under `proof-obligations.md` ("For a compound target,
atomize each conjunct before certification") this is a certification-blocking gap, not a
cosmetic one.

**N-9. Provenance items, confirmed mechanically.** The bundled `main.pdf` at `02d5d8f` is
byte-identical to the 2026-08-01 build while nine `.tex` inputs changed in the Task 5–9
commits, so it does not render the current sources
(`task-10-score-configuration-analysis.md:97-104`,
`task-10-timeless-history-analysis.md:63-71`). Route-C evidence line anchors have shifted by
five lines against the current ledger digest (`task-10-timeless-history-analysis.md:79-90`).
`pullback-ledger-provenance` and `minor-emergent-time-keyword` cannot close until both are
regenerated. The three routes agree and I did not re-derive this; it is mechanical.

**N-10. "connection-compatible" remains undefined, and the count is five.** I searched the
current sources: `05c_pullback_geometry.tex:15`, `:652` (the
`fig:pb-pullback-naturality` caption), `:791` (inside `thm:pb-fisher-defect-cocycle`, as
"If the connections are compatible"), `06_general_coarsegraining.tex:202`, and
`08_infogeometry.tex:512`. No definition occurs anywhere. The bundle route's count of five
sites and its verdict SUSTAINED (`task-10-bundle-pullback-analysis.md:1401`) are confirmed
on the bytes; the exact criterion it supplies is Theorem R4.2(3), the isotropy condition
$\mathfrak A_{\mathcal P}(X)\in\bar{\mathfrak g}_{\bar s(f(c))}$.

---

## Part C — Attacks run and rejected, with the basis for rejection

Recording these matters: an adversarial pass that reports only its hits is not auditable.

| Attack | Verdict | Basis (recomputed, not deferred) |
| --- | --- | --- |
| Associated-bundle descent fails for differing groups/representations | **REJECTED** | Theorem R1 part 1 (`task-10-bundle-pullback-analysis.md:189-208`) is a biconditional given a declared $\kappa$-equivariant $\mathcal P$; I re-ran the two-representative computation. Lemma 8.1 of the score route (`:1254-1269`) is an independent derivation of the same. The isotropy caveat is handled: with $\bar{\mathcal B}$ a $\bar G$-fixed point, (I) is vacuous rather than necessary, which R1.6(a) states. |
| Sample-level and law-level equivariance are conflated | **REJECTED** | Lemma 2.1 (`:142-166`) separates $N$, $N_\star$, $\Psi$ with a witness; Proposition R9 (`:1751-1778`) supplies the one-way twisted implication with a minimal converse witness. Both re-checked. |
| The horizontal defect's tensor type or composition law is wrong | **REJECTED** | (R3.1)–(R3.2) re-derived; $A_\Psi\in\Gamma(E;\varpi^*T^*\mathcal C\otimes\Psi^*V\bar E)$, and the ordered law (R4.1) is not an unweighted sum. I re-ran Block B's three-level instance: $2a_1+2(3a_2-a_1)=6a_2$ identically. |
| The sign of the exact signed comparison (R3.3) is wrong | **REJECTED** | Verified in exact arithmetic on five parameter values (Part E, Block 3): $h-f^*\bar h$ and $\delta-\mathcal X-\mathcal Q$ agree identically in $(m,b)$. |
| Passive gauge invariance is conflated with connection independence or with active-gauge invariance | **REJECTED for the source, SUSTAINED as naming** | `05c_pullback_geometry.tex:133-136` explicitly separates them; the bundle route's Proposition R2.2(ii) witness (trivial $\mathbb R$-bundle, $h=0$ becomes $h=dx^2$ under $F(u(x)g)=u(x)(x+g)$) is correct and shows only that the theorem's *title* invites a false reading. |
| Global triviality is smuggled into the descent of $g^F$ and $\mathcal T$ | **REJECTED** | `prop:pb-statistical-tensor-descent` descends pointwise from $G$-invariance alone (Lemma R2.3). The genuine globality overstatement is in `SPEC.md` §5e and is refuted by `CE-NO-GLOBAL-SECTION` (Hopf bundle, von Mises fiber, $E\cong P$, $\pi_2(S^3)=0\neq\pi_2(S^2\times S^1)$) — a `SPEC.md` finding, not a chapter finding. |
| Conditional-expectation score identities are used at null sets | **REJECTED** | `task-10-score-configuration-analysis.md:304-313` states the three qualifications (a.s. not pointwise; directional; local not sufficiency) and the `CE-FISHER-EQUALITY` witness is correct: with $\Pr_\theta(B=1)=\tfrac12+\tfrac{\theta^2}4$ the $B$-score vanishes at $\theta=0$, giving equality without sufficiency. Re-derived. |
| Parameter-dependent kernels break the contraction | **REJECTED as an attack, SUSTAINED as a fence** | A-7 (`:1206`): the Bernoulli-$\sigma(\lambda)$ channel has zero fine speed and output Fisher $\sigma(1-\sigma)>0$, since $\sigma'=\sigma(1-\sigma)$. Re-derived. (H3) is load-bearing. |
| Joint Fisher and weighted marginal Fisher are ordered | **REJECTED (no ordering exists)** | Theorem C (4.1) re-derived from idempotence of $\Pi_b,\Pi_m$; the correlated Gaussian witness recomputed: with precision $\Lambda=\binom{1\ \rho}{\rho\ 1}$, $\Lambda-(1-\rho^2)I_2=\binom{\rho^2\ \rho}{\rho\ \rho^2}$, $\det=\rho^2(\rho^2-1)<0$, with $+2\rho(1+\rho)$ along $(1,1)$ and $2\rho(\rho-1)$ along $(1,-1)$. Indefinite in both directions. |
| Normalized Markov contraction is confused with the extensive replication norm $\sqrt b$ | **REJECTED** | Both routes separate them correctly (`task-10-score-configuration-analysis.md:1157-1165`; `task-10-timeless-history-analysis.md:857-892`). The four-fold replication $\{\mathcal N(x\mathbf 1_4,I_4)\}$ has Fisher $4\,dx^2$ and is *not* a Markov pushforward of $\{\mathcal N(x,1)\}$ — a kernel raising Fisher information from $1$ to $4$ would violate data processing. $\sqrt b=2$ matches the speed ratio. |
| Semiconjugacy necessity, positivity, maximal intervals, collapse, converse | **REJECTED** | T8 (with the domain inclusion $\Sigma_Q\subseteq\bar J^{\max}$), T9 (converse on regular arcs), T10 + CE-D2 (orientation), T12 (collapse dichotomy), CE-D1 (partial traversal, $\sigma_0=\arctan$) all re-derived. CE-D2's arithmetic re-checked: $T\hat R X_\ell=x\partial_y$ versus $X_{\ell+1}(\hat Rx)=-x\partial_y$, so $a\equiv-1$. |
| Natural-gradient intertwining follows from equality of objectives | **REJECTED (it does not)** | T18's criterion re-derived from naturality of the gradient under metric pushforward; CE-D4 re-checked: $(x,2y)=a(x,2y/\kappa)$ forces $a=1$ then $\kappa=1$, so (SC) fails on $\{xy\neq0\}$. T19/T20 (functional compatibility gives orientation and noncollapse for free) re-derived; T21's sanity check $a=\varphi^2=\lambda^2$ verified. |
| Fisher duration is not reparameterization invariant, or a parameter is smuggled in as time | **REJECTED** | T7, T22, T24 re-derived; the isolated-zero witness $h_s=4x^2dx^2$, $\tau(r)=r^2$, $\tau^{-1}=\sqrt v$ non-differentiable at $0$ separates strict monotonicity from regularity exactly. T28's clock-potential obstruction recomputed: for $\mathcal F=xy$, $\alpha_F=-(y\,dx+x\,dy)/\sqrt{x^2+y^2}$ gives $d\alpha_F=\frac{x^2-y^2}{(x^2+y^2)^{3/2}}dx\wedge dy$, matching the reported value; it vanishes only on the diagonal, so it is not identically zero on any open set, which is the claim made. No time smuggling was found in the current sources. |
| The manuscript claims base positivity without the zero-defect guard | **REJECTED** | `05c_pullback_geometry.tex:687-700` carries `$\mathcal D\Psi=0$ along $s$` explicitly in `thm:pb-pullback-fisher-defect`, and `cor:pb-coarse-null-map` at `:658-672` is likewise guarded. Verified on the bytes. |
| The existence of the principal scale map $\mathcal P_\ell$ is asserted without an obstruction | **SUSTAINED, but not a defect of any theorem** | Theorem R7 (`task-10-bundle-pullback-analysis.md:1613-1653`) is correct: $\mathcal P$ exists iff $P\times_\kappa\bar G\cong f^*\bar P$, with `CE-NO-PRINCIPAL-MAP` (Hopf vs trivial over $S^2$) showing failure. This is a scope note on a *declared* datum admitted by `H-GAUGE`, not a refutation. It should be stated at `07_general_renormalization.tex` `eq:rg-principal-scale-map`. |

---

## Part D — The exact missing lemmas

`INCONCLUSIVE` requires naming them. These are stated so that a single certified proof of
each would move the affected claims.

**L-CM (owned by `configuration-map`; from `task-10-bundle-pullback-analysis.md:1453`).**
Under stated hypotheses on $(f,\Psi,E,\bar E)$, the projectable set
$\Gamma_{\mathrm{proj}}(\Psi)\cap\mathcal Q_\ell$ — the zero set of the first-order operator
$Q\mapsto\big(T^V\Psi\circ D^\omega Q+A_\Psi(Q;\cdot)\big)\big|_{\ker Tf}$ — is a smooth
submanifold of the declared configuration manifold, and the induced map
$Q\mapsto\bar Q$ into $\mathcal Q_{\ell+1}$ is smooth with a well-defined tangent map.
Needs a transversality or elliptic-regularity hypothesis making the operator a submersion
onto its image. *Status:* not supplied by any route. The score route's §5.3 shows the set can
have empty interior in the infinite-dimensional tier, which makes the lemma harder, not
easier.

**L-CFM (owned by `configuration-fisher-metric`; from `task-10-bundle-pullback-analysis.md:1454`).**
On the declared section manifold, the weighted integral $\mathsf G^F$ is a **strong**
Riemannian metric under explicit hypotheses on $\mu$, $w$, $\mathcal B$, and the topology;
and either $\mathsf G^F=\iota^*G^F_{\mathfrak R}$ for a declared joint-law lift, or the
block-orthogonality hypothesis of Theorem C(C3) holds. *Status:* the score route discharges
the *existence* half in two tiers (finite-dimensional Construction 3.2 with the exact
nondegeneracy criterion; the $L^2$ tier with two-sided bounds on $w$ and $\Sigma_0^{-1}$),
and supplies the exact joint-versus-marginal criterion (independence plus unit weights). It
does **not** discharge either half for the manuscript's declared recognition family, and
`hyp:hist-exact-vfe-lift`'s existence obligation remains `OPEN`
(`appendix_claim_ledger.tex:50-56`).

**L-AVG (new, created by finding M-5; owned jointly by `configuration-map` and
`history-duration-relation`).** For the gauge-equivariant fiberwise averaging map (5.1) and
the variational map (5.3), state and prove the exact configuration-metric defect
$$
\Delta_{\mathrm{avg}}(Z):=\int_{\mathcal C}w\,g^F_{s(c)}(Z(c),Z(c))\,\mu(dc)
-\int_{\bar{\mathcal C}}\bar w\,\bar g^F_{(\widehat Rs)(\bar c)}\big(T\widehat R Z,T\widehat RZ\big)\,\bar\mu(d\bar c),
$$
together with the exact condition on the fiber chart under which $\Delta_{\mathrm{avg}}\ge0$.
*Known:* $\Delta_{\mathrm{avg}}\ge0$ in the fixed-metric location sector, where it equals the
Jensen gap $\operatorname{Var}_\kappa$ of the velocity; $\Delta_{\mathrm{avg}}$ can be
**strictly negative** in the covariance sector of the Gaussian moment chart (M-5, with
$\Delta_{\mathrm{avg}}\to-\tfrac14$ at $\delta\to0^+$ for the displayed data), because
$(\Sigma,A)\mapsto\operatorname{Tr}(\Sigma^{-1}A\Sigma^{-1}A)$ is not jointly convex.
*Status:* absent. Until it exists, no duration or metric comparison may be asserted through
an averaging or variational coarse map.

**L-JDQM (owned by Theorem G; from finding M-9).** Fiberwise DQM of $\theta\mapsto
s_\theta(c)$ plus $\kappa$-measurability implies joint DQM of
$\mathbb P_\theta(dc,dy)=\kappa(dc)p_{s_\theta(c)}(dy)$ **under a stated $\kappa$-uniform
remainder bound**; state the bound. *Status:* the hypothesis is missing, the conclusion is
true under it.

**L-CONFIG-NONEMPTY (owned by `H-CONFIG`, hence by all three history claims).** Exhibit a
single **composite** witness: two adjacent configuration manifolds
$\mathcal Q_\ell,\mathcal Q_{\ell+1}$, each with a strong Fisher metric, each carrying a
locally existing unique VFE vector field, together with a smooth coarse map
$\widehat R_\ell$ between them. *Status:* the score route supplies manifolds with strong
metrics (§3) and, separately, coarse maps on section spaces (§5.4, §5.5); no route exhibits
the triple at once. Because `H-CONFIG` is a `DECLARED_ASSUMPTION`, a nonempty model class is
required for the history theorems to be non-vacuous. The $L^2$ tier with
$\mathcal Q_\ell=L^2(S^1;\mathbb R)$, $\mathcal Q_{\ell+1}=\mathbb R$, and $\widehat R$ the
mean is the most likely candidate and needs only a $C^1$-on-$L^2$ objective to complete;
that completion is a one-page obligation, not a research problem.

---

## Part E — Executed verification record

Exact rational and symbolic arithmetic (SymPy) plus one numerical quadrature, run at the
base revision inside this pass. Agreement corroborates the arithmetic of the witnesses; it
closes no theorem.

**Block 1 — bundle-route R4.3(3).** Block B/C data. First-jet chain rule verified at both
stages. With $\delta_{jk}=(D^{\omega_j}s_j)^*\Delta_F^{\Psi_{jk}}$:
`LHS = -2*a1**2/3 - 2*a1/3`; `printed = +2*a1**2/3 - 2*a1/3`;
`LHS - printed = -4*a1**2/3`; `LHS - (minus-sign version) = 0`;
`LHS - (coarse-jet cross terms) = 0`. At $a_1=1/10$, $a_2=0$: `LHS = -11/150`,
`printed = -3/50`. Zero set of the residual: $a_1\in\{-1,0\}$.

**Block 2 — bundle-route Block C.** Reproduced all three displayed polynomials from
$h_j-f_{jk}^*h_k$ exactly:
$1-\tfrac12(2a_1+1)^2$, $\tfrac18(2a_1+1)^2-\tfrac1{12}(6a_2+1)^2$,
$1-\tfrac13(6a_2+1)^2$; telescoping residual identically $0$. Under R3.3's definition,
$\delta_{\Psi_{01}}=1/2$ against Block C's $7/25$ at $a_1=1/10$.

**Block 3 — R11 table and (R3.3).** `identity (R3.3) exact: True`. Rows:
$b=0\Rightarrow 1/2$; $b=1/10\Rightarrow 79/200$ (positive, $\|A\|=0.07071$, margin
$0.2929$, met); $b=-1/10\Rightarrow 119/200$; $b=1/2\Rightarrow -1/8$ (margin not met, not
positive); $b=-3/5\Rightarrow 23/25$ (margin **not** met, **positive**).

**Block 4 — Gaussian witnesses.** $\Lambda-(1-\rho^2)I_2$ has
$\det=\rho^2(\rho-1)(\rho+1)$; quadratic forms $2\rho^2+2\rho$ along $(1,1)$ and
$2\rho^2-2\rho$ along $(1,-1)$. $\pi(e^{tx^2})=(1-2t)^{-1/2}$ for $t<1/2$; at $t=-1/4$ the
value is $\sqrt6/3$.

**Block 5 — averaging map.** Covariance sector: fine $\|Z\|^2=1/4$, coarse
$\|T\widehat RZ\|^2=\tfrac1{2(1+\delta)^2}\to\tfrac12$; ratio $1.96059$ at
$\delta=10^{-2}$. Location sector, $\dot m=(1,1)$: integrated fine metric $1$, image metric
$1$, averaging defect $0$; $I_{\bar P}(0)=0.550401$ (trapezoid on
$[-30,30]$, $6\times10^5$ nodes, central difference $h=10^{-3}$), Theorem G defect
$0.449599$.

**Byte-level checks.** `connection-compatible` / "the connections are compatible": five
sites, no definition. `appendix_notation.tex`: no row of type
$\mathcal Q_\ell\to\mathcal Q_{\ell+1}$. `\mathcal R`: six distinct assignments enumerated
in **M-8**. `prop:hist-oriented-semiconjugacy` (`05d_relational_inference.tex:723-751`):
hypothesis reads "On a noncritical domain" with no field named, and the proof asserts the
right-hand side of `eq:hist-oriented-flow-semiconjugacy` "solves the same initial-value
problem" before establishing that $\bar\Phi_{\sigma_Q(t)}$ is defined — both route-D attacks
A-6 and A-4 confirmed on the bytes.

---

## Part F — Hypotheses under which the rest of the portfolio is integrable today

If the Part A repairs are applied and the Part D lemmas are either supplied or the affected
text explicitly fenced, the following is integrable, under exactly this hypothesis set.

1. **Standing regularity.** `hyp:geo-smooth-tier` and `hyp:pb-regular-models` in full, at
   **both** the fine and coarse scales, including positive definiteness of $g^F$ and
   $\bar g^F$ and their invariance under the represented actions.
2. **Channel hypotheses.** (H1) one $\sigma$-finite family-level dominating measure with a
   fixed jointly measurable density version; (H2) DQM with centered finite-$L^2$ scores;
   (H3) a normalized parameter-independent Markov kernel with $K(x,\mathsf Y)=1$ for
   **every** $x$; (H4) the joint law and its reverse conditioning; **(H5) family closure**
   $N_\star(\mathcal B)\subseteq\bar{\mathcal B}$; smoothness of $q$ between the declared
   parametrized-measure models; and a jointly measurable $\theta$-smooth version selection
   for $p\mapsto T^V_p\Psi$.
3. **Bundle hypotheses.** A declared $\kappa$-equivariant $\mathcal P$ over $f$ — whose
   existence is the topological condition $P\times_\kappa\bar G\cong f^*\bar P$ (R7), to be
   stated, not assumed away — the law-fiber intertwining (I), and, for base positivity,
   $A_\Psi(s;\cdot)=0$ along the section, equivalently the isotropy condition
   $\mathfrak A_{\mathcal P}(X)\in\bar{\mathfrak g}_{\bar s(f(c))}$ that replaces the
   undefined phrase "connection-compatible".
4. **Section descent.** $f$ a surjective submersion with connected fibers; then
   (P1) $\Leftrightarrow$ (P2) $\Leftrightarrow$ (P3), the descended section is
   automatically smooth, and the descendable set is a proper subset whenever a collapsed
   direction meets a non-annihilated vertical direction.
5. **Cross-scale declaration compatibility.** $f_\#\mu=\bar\mu$ and $\bar w_x\le w_x$ for
   both channels. Neither is currently in any claim (**N-7**), and without them no
   integrated-metric comparison across scales is available even with zero fiberwise defect.
6. **Configuration tier.** Either the $L^2$ tier with two-sided bounds on $w$ and on the
   fiber Fisher form (strong metric, unconditional gradients, objective required $C^1$ on
   $L^2$), or the $H^s$ tier with the Riesz hypothesis stated as a standing assumption and
   its failure witness recorded. There is no third option.
7. **History tier.** $a_\ell$ continuous and strictly positive; "noncritical" read as
   $X_{\ell+1}\neq0$ on $\widehat R_\ell(U)$; the maximal-interval condition
   $\Sigma_Q\subseteq\bar J^{\max}$, upgraded to equality only under
   $J_Q^{\max}=\mathbb R$ and $\inf a_\ell>0$; and the duration criterion
   $\widehat R_\ell^{\,*}\mathsf G_{\ell+1}\preceq\mathsf G_\ell$ along the orbit, which
   does **not** follow from any fiberwise contraction theorem.
8. **Refusals retained.** No operational bridge from Fisher duration to a clock reading; RG
   depth $\ell$, orbit coordinate $r$, and duration $\tau^{(\ell)}$ kept as three distinct
   coordinates; and the metric relativity of $\tau$ (scaling $\mathsf G_\ell$ by $\rho^2$
   scales every duration by $\rho$) recorded alongside the operational obligations.

---

## Part G — Oracle erasure, independent reconstruction, limitations

**Oracle erasure.** The affirmative-existence instruction was removed from the working
context before any disposition in Parts A–D was fixed, and this artifact was rescanned for
direct and paraphrased dependence. It occurs in no hypothesis, counterexample, severity
assignment, or disposition. The distribution of outcomes is inconsistent with a
prior-driven pass: the terminal status is `INCONCLUSIVE` rather than affirmative; five
findings are recorded **against** route conclusions that were already affirmative; one
finding (**M-11**) is recorded **in favor of** the manuscript and **against** a route's
sustained attack, which a uniformly negative prior would also not produce; and one new
missing lemma (**L-AVG**) was created by a counterexample rather than inherited. Passing
this audit shows only that the prior was unnecessary; it proves nothing.

**Independent reconstruction.** Every identity on which a Part A finding rests was
re-derived here from the frozen contract's declared types and the route's own declared data,
without reusing the route's algebra: the exact signed comparison (R3.3), the base-cocycle
correction (R4.3(3)), the ordered composition law (R4.1) on the three-level instance, the
Fisher-defect telescoping, the joint-versus-marginal identity (4.1) and its Gaussian
witness, the DQM/normalizer domain for $\mathrm{He}_2$, the semiconjugacy time change and
its cocycle, the $\arctan$ partial-traversal witness, the orientation-reversal witness, the
gradient criteria T18/T20/T21 and their sanity check, the monotonicity trichotomy and its
isolated-zero witness, and the clock-potential obstruction for $\mathcal F=xy$. Three
manuscript locations were read directly rather than through a route
(`05c_pullback_geometry.tex:25-37,54-58,645-700`,
`05d_relational_inference.tex:720-762`, `appendix_notation.tex`). Result: **PASS**, with
the findings above.

**Limitations, separated by kind.**

* *Theorems.* This pass proves no new theorem. **M-1** and **M-9** are derivations of a
  correction and of a missing hypothesis; **M-5** is a counterexample.
* *Counterexamples.* The averaging witness of **M-5** and the mixture/barycenter separation
  of **M-4** are typed witnesses with displayed computations. Each refutes exactly the
  stated reading and nothing broader: **M-5** does not contradict Theorem E, T16, or
  `thm:pb-pullback-fisher-defect`, all of which carry hypotheses it violates.
* *Numerical observations.* Part E, Block 5's $I_{\bar P}(0)=0.550401$ is a quadrature, used
  only to separate two quantities that a symbolic argument already shows are different maps;
  it closes nothing. Every other value in Part E is exact.
* *Modeling postulates and operational identifications.* None made.
* *Provenance.* **N-9** and the byte-level checks in Part E are mechanical facts about the
  repository. They establish drift and text presence; they establish nothing mathematical.
* *Not adjudicated.* The forty-odd non-Task-10 ledger claims; the Task 5–9 evidence
  artifacts except where a Task 10 route cites them; the release artifact's terminal status,
  which is not this pass's to set.
