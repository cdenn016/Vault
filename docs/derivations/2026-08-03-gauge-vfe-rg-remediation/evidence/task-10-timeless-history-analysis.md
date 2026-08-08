<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 10 route D: typed curves, vector-field semiconjugacy, and timeless Fisher duration

## 0. Scope, independence boundary, and source binding

### 0.1 What this route is

This is the dynamical-systems and timeless-history route for Task 10 of the
gauge-VFE-RG remediation. It reconstructs the Task 10 interface from typed
curve kinematics, ordinary-differential-equation flow theory on Banach
manifolds, and Riemannian arc length, and it does not reuse another Task 10
reconstruction. It consumes the Task 9 route-C evidence only as a prior
record whose Section 7 is compared against, never as authority.

Every positive statement below is either a derivation given in full or an
explicitly labeled open obligation. Numerical agreement, symbolic
simplification, figures, and prior project prose close nothing here. All
prose is American English.

### 0.2 Base revision and current input digests

Base revision `02d5d8f542cba2d92c6a430483b62155dd5f2db4` on branch
`codex/gauge-vfe-rg-task10-pullbacks-20260804`, working tree clean at the time
of hashing. SHA-256 of every consumed input, lowercase hexadecimal:

| Path | SHA-256 | Bytes |
|---|---|---|
| `manuscripts/gauge_vfe_rg/SPEC.md` | `3557038b57f008a1453f29f3abaa2b8c7ddea822bc610dd6945adc811b97bf2d` | 53361 |
| `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex` | `a87bc2b3d7d8d76412a299fbd3220464802bd1cc2d853f1f6c287f96e5a73279` | 37884 |
| `manuscripts/gauge_vfe_rg/05d_relational_inference.tex` | `138e4f86f107f5bd0307e049dc5368a6c36584a827bf98bf4eb396e30016d0a1` | 36841 |
| `manuscripts/gauge_vfe_rg/06_general_coarsegraining.tex` | `a6a60a19a7c263915e749787b12470a84d6fafcaf9d55c69b71c0490c45c064a` | 32058 |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `a3a7ae2fed2eb4a1ea4668393a69b4d56aa2c9dd071af06ddbcba717d7365797` | 43758 |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `148d9652229eb6d3c40a41b48c1eb938328ca697a37e8113111567c580cc61be` | 132334 |
| `manuscripts/gauge_vfe_rg/08_infogeometry.tex` | `55bfcdff0eebec24f2231852467255d13a0c02d1369621d04ede53cad3b7c31b` | 45106 |
| `manuscripts/gauge_vfe_rg/09_coarsegraining.tex` | `b8c7dc9dbc9392bb103aa6dd805712294c958e0faa6d34083c43d140f88fbf0d` | 42191 |
| `manuscripts/gauge_vfe_rg/appendix_notation.tex` | `d39936499c9673c1b4ed75ae31bf294f8d4df9fd1fd0cef1dae4a9ec5a572fa4` | 22658 |
| `manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex` | `bbb02a24ed0875ff287aa072fddae359f4ccd59058157503d4e93502a4e6b436` | 13989 |
| `manuscripts/gauge_vfe_rg/main.pdf` | `83b1d9b92f1cbbd9385e0b965448cefdf561021f8ee72763bf4be7fc0fac01de` | 1365110 |
| `sources/manuscripts/gauge-vfe-rg-pullback-geometry-2026-08-01.md` | `e9cb6e4cd360ee477f60459856a33fd76b1f7d17b32f65f7a1dee61345318c68` | — |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/problem-contract.json` | `7cba2e9bbfe34028d6a994359e53c761779bd255c5405bfa3996c50ca575bc22` | 11510 |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/claim-ledger.json` | `53d9a2ae2ceab6a20c0486facc68e07bfb66731ebdccdfcc7c87f9890357c5f7` | 83672 |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/dependency-dag.json` | `bb296da12424fdd766727f0236aa6b91b1cb8fcfb93e3016882532049a119c16` | 14538 |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/counterexample-register.md` | `c7e0fa8d576ab60c2d4060f423e4222e800116a0293e0097c8d38ab55e6b6853` | 21144 |
| `docs/superpowers/plans/2026-08-03-gauge-vfe-rg-review-remediation.md` | `9e3d0c64b81a27782729e62f9485ff17eea9e687d79cbdea7b7bed69e94bb36c` | 53693 |
| `docs/derivations/.../evidence/task-9-cocycle-beta-analysis.md` | `ad840517af9336f1bb27e7bf54955042293a3180d38152da193e35ac82efbc58` | 30512 |
| `docs/derivations/.../evidence/task-9-integrated-proof.md` | `d37c301b50f45ba283670535fbaccec23779f6090106756a302ee39edf5cc14f` | 51513 |

### 0.3 Recorded drift against the stale 2026-08-01 pullback record

`sources/manuscripts/gauge-vfe-rg-pullback-geometry-2026-08-01.md` is
immutable and is used here only as a stale construction to falsify or repair.
It binds itself to working-tree revision
`43eb7e74942a61d7874c271a4be57ab3c94722a4` and records load-bearing hashes.
Comparison with the digests of Section 0.2 gives three mechanical facts.

**D-1 (source drift, confirmed).** The record's
`05c_pullback_geometry.tex` hash `4C241C1A810DA739732E7201B6BC51FE1412D4FC00761B8019AD38A4B673A8E3`
and `05d_relational_inference.tex` hash
`6DF55B6C7F98EA0C0A3F959BE1BFC0988FD4667D315E5C10F8711495A2E0B61A`
both differ from the current bytes. The record therefore does not certify the
current chapters and may not be cited as evidence for them.

**D-2 (stale build artifact, confirmed).** The record's `main.pdf` hash
`83B1D9B92F1CBBD9385E0B965448CEFDF561021F8EE72763BF4BE7FC0FAC01DE`
is byte-identical to the `main.pdf` present at the current base revision.
Because the `.tex` inputs have since changed (D-1, and Tasks 7 through 9
modified `07_general_renormalization.tex`, `07b_agent_network_rg.tex`,
`08_infogeometry.tex`, and both appendices), the bundled PDF is the
2026-08-01 build and is **not** a build of the current sources. Any visual or
page-count claim read off that PDF is stale. This is a provenance finding
against `pullback-ledger-provenance`, not a mathematical one.

**D-3 (cited review path is live).** The record cites
`docs/reviews/gauge-vfe-rg-pullback-geometry-2026-08-01/`; that directory
exists at the base revision. This citation does not drift.

### 0.4 Recorded drift inside the Task 9 route-C evidence

**D-4 (evidence anchor drift, confirmed).**
`task-9-cocycle-beta-analysis.md` binds
`claim-ledger.json` at `16A1538C266D4490BDE6745B20C2F95BD363E88B5D4045AFEF1B711446ABDA30`
and cites ledger line anchors. The current ledger digest is
`53d9a2ae...`, and every cited anchor has moved by exactly five lines:
`exact-interaction-map` 65 to 70, `projected-interaction-residual` 66 to 71,
`generalized-modes` 69 to 74, `cocycle-law` 70 to 75, `fixed-objects` 71 to
76, `beta-functions` 72 to 77, `configuration-map` 80 to 85, and
`history-semiconjugacy` 82 to 87. The route-C conclusions are unaffected, but
its line anchors must be re-resolved before reuse. Its recorded
`05d_relational_inference.tex` hash `138E4F86...` is byte-identical to the
current file, so Chapter 5d has not changed since route C read it.

### 0.5 Standing hypotheses used throughout

**H-D1 (configuration tier).** For each admitted scale $\ell$ in a finite
scale poset, $\mathcal Q_\ell$ is a smooth Hausdorff Banach manifold (finite
dimensional in the finite-design tier), modeled on a Banach space, with a
declared strong Riemannian metric $\mathsf G_\ell$: strong meaning the musical
map $T_Q\mathcal Q_\ell\to T_Q^*\mathcal Q_\ell$ is a topological isomorphism,
so gradients of $C^1$ functionals exist and are unique. This is
`hyp:hist-regular-section-space` and `hyp:hist-regular-metric-domain` of
`05d_relational_inference.tex:91-97` and `:204-211`, and ledger assumption
`H-CONFIG`.

**H-D2 (fields and coarse maps).** $X_\ell$ is a locally Lipschitz vector
field on $\mathcal Q_\ell$ in charts, so Picard-Lindelof gives, for each
$Q\in\mathcal Q_\ell$, a unique maximal integral curve $\Phi_\bullet(Q)$ on an
open maximal interval $J_Q^{\max}\ni0$, and any integral curve through $Q$ is
its restriction. $\hat R_\ell:\mathcal Q_\ell\to\mathcal Q_{\ell+1}$ is $C^1$.
When $X_\ell=-\operatorname{grad}^{\mathsf G_\ell}\mathcal F_\ell$ with
$\mathcal F_\ell\in C^2$ and $\mathsf G_\ell$ at least $C^1$, local
Lipschitzness is automatic.

**H-D3 (no primitive time).** No element of any curve parameter interval is
declared physical, and no operational bridge from any construction below to a
clock reading is asserted. This is the ledger assumption `H-HISTORY` minus
its mathematical content, which Section 6 converts into theorems.

---

## 1. The typed curve taxonomy on a static base

Write $\varpi:E\to\mathcal C$ for one associated statistical bundle over the
fixed contextual base, $VE=\ker T\varpi$ for its vertical subbundle,
$E_c=\varpi^{-1}(c)$ for the fiber over $c$, $\omega$ for a chosen principal
connection with induced Ehresmann horizontal subbundle $H^\omega E$ and
vertical projector $\operatorname{ver}^\omega:TE\to VE$, and $H^\omega_e$ for
the horizontal lift $T_{\varpi(e)}\mathcal C\to H^\omega_eE$. Let
$\mathfrak S$ be a declared regular configuration space of sections in the
sense of H-D1. Fix a connected interval $J$.

### 1.1 The five typed objects

| Type | Object | Domain and codomain | Defining condition |
|---|---|---|---|
| **C1** vertical, fixed fiber | $\Gamma:J\to E_c$ | one fiber | $\varpi\circ\Gamma\equiv c$ |
| **C2** total-space curve over a base curve | $\Gamma:J\to E$ | total space | $\gamma:=\varpi\circ\Gamma$ nonconstant |
| **C3** $\omega$-horizontal lift | $\Gamma:J\to E$ | total space, connection-relative | $\operatorname{ver}^\omega\dot\Gamma\equiv0$ |
| **C4** mixed | $\Gamma:J\to E$ | total space, connection-relative | $\dot\gamma\ne0$ and $\operatorname{ver}^\omega\dot\Gamma\ne0$ at the point |
| **C5** configuration curve | $Q:I\to\mathfrak S$ | section manifold | evaluation $\widehat\Sigma(\lambda,c)=Q(\lambda)(c)$ |

C1 through C4 live in $E$ or in one of its fibers; **C5 does not live in $E$
at all**. Its target is the section manifold $\mathfrak S$, whose points are
global objects over $\mathcal C$. This is the first and most frequently
elided type distinction, and it is why the verticality statement about C5 is a
statement about the adjoint evaluation, not about the curve.

### 1.2 Pointwise trichotomy and the stationary case

**Theorem T1 (pointwise classification).** Fix $\omega$. For each
$\lambda\in J$ the velocity $\dot\Gamma(\lambda)\in T_{\Gamma(\lambda)}E$ falls
into exactly one of four classes:

1. **stationary**: $\dot\Gamma(\lambda)=0$;
2. **vertical**: $\dot\Gamma(\lambda)\in V_{\Gamma(\lambda)}E\setminus\{0\}$,
   equivalently $T\varpi\dot\Gamma(\lambda)=0$ and $\dot\Gamma(\lambda)\ne0$;
3. **horizontal**: $\dot\Gamma(\lambda)\in H^\omega_{\Gamma(\lambda)}E\setminus\{0\}$,
   equivalently $\operatorname{ver}^\omega\dot\Gamma(\lambda)=0$ and $\dot\Gamma(\lambda)\ne0$;
4. **mixed**: both $T\varpi\dot\Gamma(\lambda)\ne0$ and
   $\operatorname{ver}^\omega\dot\Gamma(\lambda)\ne0$.

*Proof.* The connection gives the direct sum $TE=VE\oplus H^\omega E$, so
every tangent vector has a unique decomposition
$\dot\Gamma=H^\omega_\Gamma(T\varpi\dot\Gamma)+\operatorname{ver}^\omega\dot\Gamma$.
The four cases are: both summands zero; the horizontal summand zero and the
vertical summand nonzero; the vertical summand zero and the horizontal
summand nonzero; both nonzero. Because $T\varpi$ restricts to an isomorphism
$H^\omega_eE\to T_{\varpi(e)}\mathcal C$, the horizontal summand vanishes if
and only if $T\varpi\dot\Gamma=0$. $\square$

**Corollary T1a (vertical and horizontal are disjoint off stationarity).** A
velocity is simultaneously vertical and $\omega$-horizontal if and only if it
is zero, because $V_eE\cap H^\omega_eE=\{0\}$. Consequently a curve is both
C1 and C3 if and only if it is constant.

**Attack A-1, sustained (minor).** `def:hist-curve-types` at
`05d_relational_inference.tex:42-63` defines the three labels at
*interval* scope: "It is mixed when $\dot\gamma$ and
$v_{\boldsymbol\omega_i}(\Gamma)$ both occur: equivalently, $\gamma$ is
nonconstant and $v_{\boldsymbol\omega_i}(\Gamma)$ is not identically zero."
Under that reading a curve that is genuinely vertical on $[0,\tfrac12]$ and
genuinely mixed on $[\tfrac12,1]$ receives the single global label "mixed",
and the stationary case is silently absorbed. The labels are therefore not a
partition. **Minimal repair R-1:** declare the pointwise trichotomy plus the
stationary case exactly as in T1, then define the interval-level labels as
"vertical/horizontal/mixed at every $\lambda$", and record that the three
interval labels are no longer exhaustive. This is a definitional repair; no
downstream theorem in Chapter 5d changes, because every downstream use is on
a subinterval of one pointwise type.

### 1.3 Separation theorems

**Theorem T2 (verticality is connection-free; horizontality is not).**
On a connected $J$, $\Gamma$ is of type C1 for some $c$ if and only if
$T\varpi\dot\Gamma\equiv0$; this condition mentions no connection. In
contrast, for every $C^1$ curve $\Gamma$ with $\dot\gamma$ nowhere zero on a
subinterval $J'$ on which $\gamma$ is an embedding, there exists a principal
connection making $\Gamma|_{J'}$ horizontal, and another making it mixed.

*Proof.* First claim: $T\varpi\dot\Gamma=\dot\gamma$, and $\dot\gamma\equiv0$
on a connected interval is equivalent to $\gamma$ constant. No splitting of
$TE$ is used. Second claim: over an embedded arc, choose a local
trivialization $E|_{\mathcal U}\cong\mathcal U\times F$ in which
$\Gamma(\lambda)=(\gamma(\lambda),f(\lambda))$. A local connection form is a
smooth field of vertical-valued one-forms $A$, and the horizontality equation
along $\Gamma$ reads $\dot f(\lambda)+A_{\gamma(\lambda)}(\dot\gamma(\lambda))\big|_{f(\lambda)}=0$.
Since $\dot\gamma(\lambda)\ne0$ and $\gamma|_{J'}$ is an embedding, the values
$A_{\gamma(\lambda)}(\dot\gamma(\lambda))$ may be prescribed independently at
each $\lambda$ and extended smoothly off the arc by a bump function; choose
them to solve the displayed equation. Adding any nonzero vertical-valued
one-form supported on the arc and not annihilating $\dot\gamma$ produces a
connection for which the same curve is mixed. $\square$

The manuscript already carries a two-line instance of the second claim at
`prop:hist-horizontal-connection-dependence`,
`05d_relational_inference.tex:75-86`. T2 upgrades it from one witness to the
general statement, which is what justifies the language "horizontality is
connection-relative" in full generality.

**Theorem T3 (a base curve has no verticality type).** Let
$\gamma:J\to\mathcal C$. The predicates vertical, horizontal, and mixed are
predicates on curves in $E$, defined through $VE$ and $H^\omega E\subset TE$.
No such predicate is defined for $\gamma$, because $T\mathcal C$ carries no
canonical splitting. The connection acts on $\gamma$ only through the
*horizontal lift operator* $H^\omega$, which produces a curve in $E$ from
$\gamma$ *and* an initial point $e_0\in E_{\gamma(0)}$; the lift is not a
property of $\gamma$.

**Attack A-2, rejected.** The manuscript was scanned for the error of calling
a base curve horizontal. The three uses of "horizontal lift" in
`02_geometry.tex:298`, `02_geometry.tex:363`, and
`05c_pullback_geometry.tex:624` are all the correct operator usage.
`SPEC.md:179` states the correct rule verbatim: "A base curve itself needs no
connection; its horizontal lift and the horizontal--vertical decomposition
do." `05c_pullback_geometry.tex:559-564` and `appendix_notation.tex:377-384`
repeat it. No instance of the error was found in the current sources. This
attack is rejected on the cited bytes; the falsifier for the rejection is any
future occurrence of "horizontal base curve" or a decomposition of
$\dot\gamma$ into vertical and horizontal parts.

**Theorem T4 (a nonconstant fixed-fiber curve is not section-induced over a
moving base).** If $\Gamma:J\to E_c$ is nonconstant and $s$ is any section,
there is no nonconstant $\gamma:J\to\mathcal C$ with $\Gamma=s\circ\gamma$.

*Proof.* $\varpi\circ s=\operatorname{id}$, so $\varpi\circ(s\circ\gamma)=\gamma$.
If $\Gamma=s\circ\gamma$ then $\gamma=\varpi\circ\Gamma\equiv c$, hence
$s\circ\gamma\equiv s(c)$ is constant, contradicting nonconstancy. $\square$

This is stated in prose at `05d_relational_inference.tex:196-199`; T4 records
the one-line proof. Its content is that C1 and the section-induced subclass of
C2 intersect only in constants: belief change at a fixed context can never be
manufactured by moving the context.

**Theorem T5 (C5 is pointwise vertical, and the converse needs regularity).**
Let $Q:I\to\mathfrak S$ be $C^1$ with differentiable evaluation, and set
$\widehat\Sigma(\lambda,c)=Q(\lambda)(c)$. Then for every fixed $c$,

$$
T\varpi\left(\partial_\lambda\widehat\Sigma(\lambda,c)\right)=0,
\qquad
\partial_\lambda\widehat\Sigma(\lambda,c)\in V_{Q(\lambda)(c)}E .
$$

Conversely, a family $\{\Gamma_c:I\to E_c\}_{c\in\mathcal C}$ of fixed-fiber
curves defines a curve in $\mathfrak S$ only if $c\mapsto\Gamma_c(\lambda)$ is
a section of the declared regularity for each $\lambda$ **and** the resulting
map $I\to\mathfrak S$ is $C^1$ for the declared manifold structure on
$\mathfrak S$. Neither follows from pointwise verticality.

*Proof.* Forward: $\varpi\circ\widehat\Sigma(\lambda,c)=c$ for all $\lambda$,
so the partial derivative in $\lambda$ of a constant map is zero; apply
$T\varpi$ and use $VE=\ker T\varpi$. Converse: pointwise data carry no
statement about $c$-regularity or about the topology of $\mathfrak S$; the
declared structure is `hyp:hist-regular-section-space`, which explicitly
warns that "No such structure follows merely from writing down all smooth
sections". $\square$

The forward direction is `eq:hist-pointwise-history-verticality`,
`05d_relational_inference.tex:110-119`. The converse direction is not stated
there and is the honest reason why C5 is a genuinely separate type rather
than a repackaging of C1.

**Theorem T6 (diagonal evaluation splits exactly).** With $\gamma:I\to\mathcal C$
and $\Gamma(\lambda)=Q(\lambda)(\gamma(\lambda))$,

$$
\operatorname{ver}^\omega\dot\Gamma(\lambda)
=\partial_\lambda\widehat\Sigma(\lambda,\gamma(\lambda))
+D^\omega Q(\lambda)\left(\dot\gamma(\lambda)\right),
$$

with the first term the history velocity at frozen context and the second the
vertical response of one frozen section to a moving probe. If $\gamma$ is
constant the diagonal curve is of type C1; if $Q$ is constant it is
section-induced.

*Proof.* Chain rule on $\widehat\Sigma$ in both slots, then apply
$\operatorname{ver}^\omega$; the first slot is already vertical by T5 and the
second contributes $\operatorname{ver}^\omega\circ TQ(\lambda)=D^\omega Q(\lambda)$
applied to $\dot\gamma$. $\square$

This is `eq:hist-diagonal-evaluation-velocity`,
`05d_relational_inference.tex:174-179`, and it is correct as written. T6
records it because it is the exact place where a mixed curve can be mistaken
for a history: the second term is *not* history change, and it vanishes
identically only when the section is $\omega$-parallel along $\gamma$.

### 1.4 The base is static, and no parameter is time

**Theorem T7 (parameter gauge).** Let $\mathcal G^+$ be the group of
orientation-preserving $C^1$ diffeomorphisms between intervals, acting on
$C^1$ curves by $\Gamma\mapsto\Gamma\circ\phi$. Then:

1. the four pointwise types of T1 are $\mathcal G^+$-invariant at
   corresponding points;
2. the base projection transforms by $\gamma\mapsto\gamma\circ\phi$, so the
   base point set and its traversal order are invariant while the base itself
   is never moved;
3. vertical Fisher length $L^\omega$ and configuration Fisher length $L_F$ are
   invariant on corresponding subarcs;
4. the elapsed parameter $b-a$, the velocity $\dot\Gamma$, the speed $\nu$,
   and every rate $d/d\lambda$ are **not** invariant.

*Proof.* (1) $\frac{d}{dr}(\Gamma\circ\phi)=\phi'(r)\dot\Gamma(\phi(r))$ with
$\phi'>0$, and each of $VE$, $H^\omega E$, and the zero vector is stable under
multiplication by a positive scalar. (2) $\varpi\circ\Gamma\circ\phi=\gamma\circ\phi$.
(3) Positive homogeneity of the square root turns $\phi'$ into the
one-dimensional change-of-variables Jacobian; this is the computation of
`prop:pb-curve-taxonomy` and `thm:hist-fisher-clock-invariance`. (4) Scale
$\phi$ by a constant $k>0$: the elapsed parameter scales by $1/k$ and the
speed by $k$. $\square$

**Corollary T7a (no cross-history simultaneity).** Two independent
parameterized histories $Q^{1}:I_1\to\mathcal Q$ and $Q^{2}:I_2\to\mathcal Q$
admit no invariant relation of the form "at the same parameter value", because
$\mathcal G^+$ acts independently on $I_1$ and $I_2$. Any statement that
compares $Q^{1}(\lambda)$ with $Q^{2}(\lambda)$ is a statement about a chosen
pair of representatives, not about the two histories.

**Corollary T7b (the base carries no history).** The base $\mathcal C$ is
never the domain or codomain of any of the parameter-carrying objects above:
$\gamma$ maps *into* $\mathcal C$, and $\mathcal C$ is the *second* slot of the
adjoint evaluation $\Sigma:\mathscr H\times\mathcal C\to E$ with
$\varpi\circ\Sigma(r,c)=c$. Therefore no construction in C1 through C5 induces
motion of a base point, and the base remains static.

**Witness W-1 (finite length, unbounded parameter).** In the unit-variance
normal location family, $\mu(t)=e^{-t}$ on $[0,\infty)$ has Fisher length
$\int_0^\infty e^{-t}dt=1$ while $t$ ranges over an unbounded interval. Length
and elapsed parameter are therefore not proportional and not even mutually
finite. This is `eq:hist-finite-length-infinite-parameter`,
`05d_relational_inference.tex:449-456`.

---

## 2. Vector-field semiconjugacy and the orbit reparameterization

### 2.1 The exact condition

**Definition D-SC.** Let $U\subseteq\mathcal Q_\ell$ be open. The pair
$(\hat R_\ell,a_\ell)$ is an **oriented semiconjugacy of $X_\ell$ onto
$X_{\ell+1}$ over $U$** when $a_\ell:U\to(0,\infty)$ is continuous and

$$
T_Q\hat R_\ell\, X_\ell(Q)
= a_\ell(Q)\, X_{\ell+1}\!\left(\hat R_\ell Q\right)
\qquad\text{for every }Q\in U .
\tag{SC}
$$

**Lemma L-1 (uniqueness and automatic regularity of the factor).** Fix
$Q\in U$.

1. If $X_{\ell+1}(\hat R_\ell Q)\ne0$, then any $a_\ell(Q)$ satisfying (SC) is
   unique and equals
   $$
   a_\ell(Q)
   =\frac{\mathsf G_{\ell+1}\!\left(T_Q\hat R_\ell X_\ell(Q),\,X_{\ell+1}(\hat R_\ell Q)\right)}
   {\left\|X_{\ell+1}(\hat R_\ell Q)\right\|^2_{\mathsf G_{\ell+1}}},
   $$
   hence $a_\ell$ is $C^k$ on the open set where $X_{\ell+1}\circ\hat R_\ell$
   is nonzero, whenever $\hat R_\ell$, $X_\ell$, $X_{\ell+1}$, and
   $\mathsf G_{\ell+1}$ are $C^k$.
2. If $X_{\ell+1}(\hat R_\ell Q)=0$, then (SC) forces
   $T_Q\hat R_\ell X_\ell(Q)=0$ and **every** positive number satisfies (SC) at
   $Q$. The factor is undetermined there.

*Proof.* (1) Pair (SC) with $X_{\ell+1}(\hat R_\ell Q)$ in $\mathsf G_{\ell+1}$
and divide by the nonzero squared norm; strong nondegeneracy of
$\mathsf G_{\ell+1}$ makes the denominator positive. (2) Substitute
$X_{\ell+1}(\hat R_\ell Q)=0$ into (SC). $\square$

Lemma L-1(2) is load bearing for Section 3 and is the precise sense in which
"$a_\ell>0$" is vacuous on the coarse critical set.

**Attack A-3, sustained (regularity).** `prop:hist-oriented-semiconjugacy`,
`05d_relational_inference.tex:723-751`, states (SC) with "$a(Q)>0$" and then
integrates $a$ along an orbit without declaring any regularity of $a$ and
without observing L-1. **Minimal repair R-2:** state (SC) with $a_\ell$
continuous, and add L-1 so that continuity is a consequence rather than an
assumption on the noncritical part.

### 2.2 The orbit reparameterization, derived

**Theorem T8 (local orbit reparameterization).** Assume H-D1, H-D2, and (SC)
on an open $U$. Fix $Q\in U$ and let $J_Q\subseteq J_Q^{\max}$ be the
connected component containing $0$ of
$\{t\in J_Q^{\max}:\Phi_s(Q)\in U\text{ for all }s\text{ between }0\text{ and }t\}$.
Define

$$
\sigma_Q(t)=\int_0^t a_\ell\!\left(\Phi_s(Q)\right)ds,
\qquad t\in J_Q .
$$

Then $\sigma_Q$ is $C^1$, $\sigma_Q(0)=0$, $\sigma_Q'=a_\ell\circ\Phi_\bullet(Q)>0$,
so $\sigma_Q$ is a strictly increasing $C^1$ diffeomorphism of $J_Q$ onto the
open interval $\Sigma_Q:=\sigma_Q(J_Q)\ni0$. Moreover

$$
\Sigma_Q\subseteq \bar J^{\max}_{\hat R_\ell Q},
\qquad
\hat R_\ell\!\left(\Phi_t(Q)\right)
=\bar\Phi_{\sigma_Q(t)}\!\left(\hat R_\ell Q\right)
\quad\text{for all }t\in J_Q ,
\tag{FSC}
$$

where $\bar\Phi$ is the maximal flow of $X_{\ell+1}$ and
$\bar J^{\max}_{\hat R_\ell Q}$ its maximal interval.

*Proof.* Set $c(t)=\hat R_\ell(\Phi_t(Q))$ for $t\in J_Q$. Since $\hat R_\ell$
is $C^1$ and $\Phi_\bullet(Q)$ is $C^1$, $c$ is $C^1$ with $c(0)=\hat R_\ell Q$
and, by the chain rule and (SC),

$$
\dot c(t)=T\hat R_\ell X_\ell(\Phi_tQ)
=a_\ell(\Phi_tQ)\,X_{\ell+1}(c(t)).
$$

The integrand $s\mapsto a_\ell(\Phi_sQ)$ is continuous and strictly positive,
so $\sigma_Q$ is $C^1$ with everywhere positive derivative, hence a strictly
increasing $C^1$ diffeomorphism onto its image, which is an open interval
because $J_Q$ is open and $\sigma_Q$ is a continuous strictly increasing map.
Let $\theta=\sigma_Q^{-1}:\Sigma_Q\to J_Q$; it is $C^1$ with
$\theta'(u)=1/a_\ell(\Phi_{\theta(u)}Q)>0$. Put $d(u)=c(\theta(u))$. Then

$$
d'(u)=\dot c(\theta(u))\,\theta'(u)
=a_\ell(\Phi_{\theta(u)}Q)X_{\ell+1}(d(u))\cdot\frac{1}{a_\ell(\Phi_{\theta(u)}Q)}
=X_{\ell+1}(d(u)),
$$

so $d$ is an integral curve of $X_{\ell+1}$ on the open interval $\Sigma_Q$
with $d(0)=\hat R_\ell Q$. Because $X_{\ell+1}$ is locally Lipschitz, the
maximal integral curve through $\hat R_\ell Q$ has a domain containing the
domain of every integral curve through that point and restricts to it. Hence
$\Sigma_Q\subseteq\bar J^{\max}_{\hat R_\ell Q}$ and $d=\bar\Phi_\bullet(\hat R_\ell Q)|_{\Sigma_Q}$.
Substituting $u=\sigma_Q(t)$ gives (FSC). $\square$

**Attack A-4, sustained (order of construction).** The manuscript proof at
`05d_relational_inference.tex:744-751` writes "the right side of
\eqref{eq:hist-oriented-flow-semiconjugacy} solves the same initial-value
problem after the stated time change" and then invokes flow uniqueness. This
presupposes that $\bar\Phi_{\sigma_Q(t)}(\hat R_\ell Q)$ is defined, which is
exactly what has to be proved. **Minimal repair R-3:** replace the proof by
the order used in T8: build $d$ on $\Sigma_Q$ first, verify it solves the
autonomous equation, and conclude the domain inclusion from maximality. The
repair costs three lines and yields the domain conclusion
$\Sigma_Q\subseteq\bar J^{\max}$ as a bonus, which the current proof does not
deliver.

### 2.3 Local, maximal, and global hypotheses

**Corollary T8a (maximal version).** If (SC) holds on all of $\mathcal Q_\ell$
then $J_Q=J_Q^{\max}$ and the conclusion of T8 holds on the full maximal fine
interval.

**Corollary T8b (completeness transfer).** Assume (SC) on $\mathcal Q_\ell$,
$J_Q^{\max}=\mathbb R$, and $\underline a:=\inf_{t\in\mathbb R}a_\ell(\Phi_tQ)>0$.
Then $\sigma_Q(t)\ge\underline a\,t$ for $t\ge0$ and
$\sigma_Q(t)\le\underline a\,t$ for $t\le0$, so $\Sigma_Q=\mathbb R$ and
$\bar J^{\max}_{\hat R_\ell Q}=\mathbb R$: the coarse orbit through
$\hat R_\ell Q$ is complete and is traversed in full.

**Counterexample CE-D1 (completeness does not transfer without a positive
infimum).** Take $\mathcal Q_\ell=\mathcal Q_{\ell+1}=\mathbb R$ with the
Euclidean metric, $X_\ell=\partial_x$, $X_{\ell+1}=\partial_y$, and
$\hat R_\ell(x)=\arctan x$. Then
$T\hat R_\ell\partial_x=\frac{1}{1+x^2}\partial_y$, so (SC) holds with
$a_\ell(x)=(1+x^2)^{-1}>0$, and $\hat R_\ell$ is an injective immersion, so no
collapse and no rank loss occurs. Both flows are complete, yet
$\sigma_0(t)=\arctan t$ has $\Sigma_0=(-\tfrac\pi2,\tfrac\pi2)\subsetneq\mathbb R$:
the whole fine history realizes only a bounded arc of the coarse orbit.
**Consequence:** the phrase "the coarse history *is* the fine history" is
false without a maximal-interval hypothesis, even under (SC), even with no
collapse, and even with both flows complete. The correct invariant statement
is the inclusion $\Sigma_Q\subseteq\bar J^{\max}$ of T8.

**Corollary T8c (limit-set transport).** Assume (SC) on $\mathcal Q_\ell$,
forward completeness of $\Phi_\bullet(Q)$, and
$\int_0^\infty a_\ell(\Phi_sQ)\,ds=\infty$. Then
$\hat R_\ell(\omega_{X_\ell}(Q))\subseteq\omega_{X_{\ell+1}}(\hat R_\ell Q)$.

*Proof.* If $y\in\omega_{X_\ell}(Q)$, pick $t_n\to\infty$ with
$\Phi_{t_n}Q\to y$. Continuity of $\hat R_\ell$ gives
$\bar\Phi_{\sigma_Q(t_n)}(\hat R_\ell Q)=\hat R_\ell(\Phi_{t_n}Q)\to\hat R_\ell y$,
and $\sigma_Q(t_n)\to\infty$ by the divergence hypothesis. $\square$

Under CE-D1's finite $\sigma_Q(\infty)$ the conclusion fails, so the
divergence hypothesis is not removable. This corollary is the exact statement
of "fine and coarse share asymptotics" and it is strictly weaker than an
equality of limit sets, for which properness of $\hat R_\ell$ and compactness
of the fine limit set would additionally be required.

### 2.4 The converse on regular orbit arcs

**Theorem T9 (converse).** Fix $Q_0$ with $X_\ell(Q_0)\ne0$ and suppose there
exist $\varepsilon>0$ and an orientation-preserving $C^1$ diffeomorphism
$\sigma$ of $(-\varepsilon,\varepsilon)$ onto an open interval containing $0$,
with $\sigma(0)=0$, such that

$$
\hat R_\ell\!\left(\Phi_t(Q_0)\right)
=\bar\Phi_{\sigma(t)}\!\left(\hat R_\ell Q_0\right),
\qquad |t|<\varepsilon .
$$

Then (SC) holds **along the orbit arc** with
$a_\ell(\Phi_tQ_0)=\sigma'(t)>0$.

*Proof.* Differentiate both sides in $t$. The left side is
$T\hat R_\ell X_\ell(\Phi_tQ_0)$ by the chain rule; the right side is
$\sigma'(t)X_{\ell+1}(\bar\Phi_{\sigma(t)}(\hat R_\ell Q_0))
=\sigma'(t)X_{\ell+1}(\hat R_\ell\Phi_tQ_0)$. A $C^1$ diffeomorphism with
$C^1$ inverse has nowhere-vanishing derivative, and orientation preservation
gives $\sigma'>0$. $\square$

**Theorem T10 (orbit-set version, and why the positive factor must be
declared).** Suppose only that $\hat R_\ell$ maps the fine orbit *set* through
$Q_0$ into a single $X_{\ell+1}$-orbit set, and that
$T\hat R_\ell X_\ell(Q_0)\ne0$. Then $T\hat R_\ell X_\ell(Q_0)$ is tangent to
that coarse orbit, so $T\hat R_\ell X_\ell(Q_0)=a\,X_{\ell+1}(\hat R_\ell Q_0)$
for a unique **real** $a\ne0$. Nothing in the hypothesis forces $a>0$.

**Counterexample CE-D2 (orientation reversal).** Let
$\mathcal Q_\ell=\mathcal Q_{\ell+1}=\mathbb R$ Euclidean,
$\mathcal F_\ell(x)=x^2/2$ and $\mathcal F_{\ell+1}(y)=-y^2/2$, so the
natural-gradient descent fields are $X_\ell=-x\,\partial_x$ and
$X_{\ell+1}=+y\,\partial_y$. Take $\hat R_\ell(x)=-x$. Then
$T\hat R_\ell X_\ell(x)=x\,\partial_y$ while
$X_{\ell+1}(\hat R_\ell x)=-x\,\partial_y$, so the tangent-line condition holds
with $a\equiv-1$. Orbit sets agree exactly; orientations are opposite. The
coarse "history" runs *up* its own free energy while the fine one runs down.
**Consequence:** dropping "$a_\ell>0$" from (SC) turns a descent history into
an ascent history. The positivity requirement is not decoration; it is the
entire orientation content, and it is *not* implied by orbit-set agreement.

The manuscript does carry the positivity in
`eq:hist-oriented-vector-field-semiconjugacy` and in
`07b_agent_network_rg.tex` equation (7.1) of route C, and the SPEC repeats it
at `SPEC.md:624`. **Attack A-5, rejected** for the current sources; CE-D2 is
recorded as the falsifier that keeps it there.

### 2.5 Composition across scales

**Theorem T11 (multiplicative scale cocycle for the factor, additive cocycle
for the time change).** Let (SC) hold for $(\hat R_\ell,a_\ell)$ and
$(\hat R_{\ell+1},a_{\ell+1})$ on compatible domains. Then
$\hat R_{\ell+1}\circ\hat R_\ell$ satisfies (SC) from $X_\ell$ to $X_{\ell+2}$
with factor

$$
a_{\ell\to\ell+2}=a_\ell\cdot\left(a_{\ell+1}\circ\hat R_\ell\right)>0 ,
$$

and the associated time changes compose as
$\sigma^{\ell\to\ell+2}_Q=\sigma^{\ell+1}_{\hat R_\ell Q}\circ\sigma^{\ell}_Q$.
Moreover, for fixed $\ell$ the time change is an additive cocycle over the
fine flow:

$$
\sigma_{\Phi_t Q}(s)=\sigma_Q(t+s)-\sigma_Q(t).
$$

*Proof.* First identity: apply $T\hat R_{\ell+1}$ to (SC) at level $\ell$,
use linearity to pull out the scalar $a_\ell(Q)$, and then apply (SC) at level
$\ell+1$ at the point $\hat R_\ell Q$. Second: substitute the first into the
defining integral and change variables by $u=\sigma^\ell_Q(s)$. Third:
$\sigma_{\Phi_tQ}(s)=\int_0^sa_\ell(\Phi_{u+t}Q)du=\int_t^{t+s}a_\ell(\Phi_vQ)dv$. $\square$

T11 is the exact typed statement of what $a_\ell$ is: a **multiplicative
cocycle in the scale index and an additive time-change cocycle over the
inference flow**. It is not a duration, not a scale ratio, and not a rate.
Section 4 shows it is invisible to duration. This complements, and is
independent of, the additive Fisher-defect cocycle
`thm:pb-fisher-defect-cocycle` at `05c_pullback_geometry.tex:779-808` and the
derivative cocycle of route C equation (1.2).

---

## 3. Noncollapse

### 3.1 The dichotomy

**Theorem T12 (collapse dichotomy).** Assume H-D1, H-D2, and (SC) on an open
$U$, with $a_\ell$ continuous and positive. Fix $Q\in U$ and let
$c(t)=\hat R_\ell(\Phi_tQ)$ on $J_Q$. Exactly one of the following holds.

1. **Regular image.** $X_{\ell+1}(\hat R_\ell Q)\ne0$. Then $\dot c(t)\ne0$ for
   every $t\in J_Q$, so $c$ is an immersed regular arc, and by T8 it is an
   orientation-preserving reparameterization of an arc of the maximal coarse
   orbit through $\hat R_\ell Q$.
2. **Total collapse.** $X_{\ell+1}(\hat R_\ell Q)=0$. Then
   $c(t)\equiv\hat R_\ell Q$ on all of $J_Q$: the entire fine orbit, however
   long and however nonconstant, maps to a single point.

In particular there is no partial collapse: $c$ cannot be constant on a
proper nondegenerate subinterval and nonconstant elsewhere.

*Proof.* By T8, $c(t)=\bar\Phi_{\sigma_Q(t)}(\hat R_\ell Q)$ with
$\sigma_Q$ a strictly increasing $C^1$ diffeomorphism onto $\Sigma_Q$. If
$X_{\ell+1}(\hat R_\ell Q)=0$ then $\hat R_\ell Q$ is an equilibrium of
$X_{\ell+1}$, and the constant map is an integral curve through it; local
Lipschitz uniqueness makes it the maximal one, so $\bar\Phi_u(\hat R_\ell Q)=\hat R_\ell Q$
for every $u$, giving case 2. If $X_{\ell+1}(\hat R_\ell Q)\ne0$ then
$\hat R_\ell Q$ is not an equilibrium, and by uniqueness no point of its orbit
is an equilibrium, so $X_{\ell+1}(c(t))\ne0$ for all $t$; then
$\dot c(t)=a_\ell(\Phi_tQ)X_{\ell+1}(c(t))\ne0$ because $a_\ell>0$. $\square$

**Corollary T12a (noncollapse is a one-point test).** Under (SC), the image of
a fine orbit is nonconstant if and only if its initial point maps outside the
zero set of $X_{\ell+1}$. When $X_{\ell+1}$ is a natural-gradient field this
reads: the image of the initial configuration is not a critical point of the
coarse objective.

**Corollary T12b (equivalent transversality form).** Under (SC) with
$a_\ell>0$ and $X_\ell(Q)\ne0$, the following are equivalent:
(i) $X_{\ell+1}(\hat R_\ell Q)\ne0$; (ii) $T_Q\hat R_\ell X_\ell(Q)\ne0$;
(iii) $X_\ell(Q)\notin\ker T_Q\hat R_\ell$. Form (iii) is the checkable
geometric condition: *the fine inference velocity must have a component
transverse to the fibers of the coarse-graining map.*

Corollary T12b matters because in the RG setting $\hat R_\ell$ is a
coarsening, so $\ker T\hat R_\ell$ is large by design. Noncollapse is
therefore not a technicality but the substantive requirement that the
variational motion be visible to the coarse description.

### 3.2 The collapse counterexample

**Counterexample CE-HISTORY-COLLAPSE (certified here; register entry
promoted from CANDIDATE).** Let $\mathcal Q_\ell=\mathbb R$ with the Euclidean
metric and $X_\ell=\partial_x$, the natural-gradient descent field of
$\mathcal F_\ell(x)=-x$. Let $\mathcal Q_{\ell+1}=\mathbb R$ with any metric,
$\mathcal F_{\ell+1}\equiv0$, hence $X_{\ell+1}\equiv0$. Let
$\hat R_\ell\equiv0$ be the constant map. Then $T\hat R_\ell\equiv0$ and

$$
T_Q\hat R_\ell X_\ell(Q)=0=a\cdot X_{\ell+1}(\hat R_\ell Q)
\quad\text{for every constant }a>0 ,
$$

so (SC) holds with, say, $a_\ell\equiv1$, and every hypothesis of
`prop:hist-oriented-semiconjugacy` other than an unstated noncriticality of
$X_{\ell+1}$ is met. The fine orbit $t\mapsto t$ is nonconstant with Fisher
duration $\tau^{(\ell)}(t)=t$ on every interval; its image is the single point
$0$ with duration identically zero. All objects are smooth, complete, and
real-analytic. The flow identity (FSC) is *true* here, since both sides equal
$\hat R_\ell Q$; what fails is every history-identification reading of it.

**Consequences, stated exactly.**

- (SC) with $a_\ell>0$ does **not** imply that the coarse object is a
  nonconstant history.
- (SC) with $a_\ell>0$ does **not** imply injectivity of $\hat R_\ell$ on the
  fine orbit, nor preservation of Fisher duration, nor preservation of the
  orbit's dimension.
- The manuscript's remark at `05d_relational_inference.tex:759-760`, "At a
  fine critical point, the same relation with $a>0$ also requires the image to
  be meta-critical", is correct but states the *harmless* direction
  ($X_\ell(Q)=0\Rightarrow X_{\ell+1}(\hat R_\ell Q)=0$). The damaging
  direction, $X_{\ell+1}(\hat R_\ell Q)=0\Rightarrow$ total collapse of a
  nonconstant fine orbit, is T12 and is absent.

**Attack A-6, sustained (this is the principal Task 10 finding).**
`prop:hist-oriented-semiconjugacy` opens with "On a noncritical domain", which
does not say noncritical *for which field*. Under the reading "$X_\ell\ne0$ on
the domain", CE-HISTORY-COLLAPSE satisfies every stated hypothesis and refutes
the informal conclusion "maps each fine integral curve to a meta integral
curve up to an orientation-preserving change of parameter" as a statement
about histories. Under the reading "$X_{\ell+1}\ne0$ on
$\hat R_\ell(\text{domain})$", the proposition is correct and, by T12, also
noncollapsing. The text does not disambiguate. **Minimal repair R-4:** state
the hypothesis as "$X_{\ell+1}$ is nonvanishing on $\hat R_\ell(U)$", add T12
as the dichotomy, and add T12b as the checkable transversality form.

### 3.3 The full noncollapse hypothesis set

For the language "the coarse history *is* the fine history, reparameterized",
the following are necessary and, taken together, sufficient. Each is
independent of the others: CE-HISTORY-COLLAPSE violates N1 only, CE-D1
violates N3 only, CE-D2 violates N0 only.

| Label | Condition | Role | Failure witness |
|---|---|---|---|
| **N0** | $a_\ell>0$, not merely $a_\ell\ne0$ | orientation | CE-D2 |
| **N1** | $X_{\ell+1}\ne0$ on $\hat R_\ell(\mathcal O)$, $\mathcal O$ the fine orbit; equivalently $X_\ell\notin\ker T\hat R_\ell$ | nonzero coarse speed, noncollapse | CE-HISTORY-COLLAPSE |
| **N2** | $X_\ell\ne0$ on $\mathcal O$ | the fine object is a nondegenerate history at all | a fine equilibrium; then both sides are points |
| **N3** | $\Sigma_Q=\bar J^{\max}_{\hat R_\ell Q}$; guaranteed by $J_Q^{\max}=\mathbb R$ together with $\inf_{\mathcal O}a_\ell>0$ | the *whole* coarse orbit is realized | CE-D1 |
| **N4** | $\hat R_\ell|_{\mathcal O}$ injective | traversal multiplicity is preserved | automatic under N1 when $X_{\ell+1}$ is gradient-like, by T13 |
| **N5** | $\ker T_Q\hat R_\ell$ closed and complemented in $T_Q\mathcal Q_\ell$ | needed in the Banach tier for the orthogonal splitting used in Section 5 | not needed in the finite-dimensional tier |

**Theorem T13 (gradient-like coarse fields have no closed orbits, hence N4 is
free).** Suppose $X_{\ell+1}=-M\operatorname{grad}^{\mathsf G_{\ell+1}}\mathcal F_{\ell+1}$
with $\mathcal F_{\ell+1}\in C^1$ and $M$ a field of $\mathsf G_{\ell+1}$-positive
(not necessarily symmetric, but with positive symmetric part) bounded
operators. Then along any nonconstant integral curve,

$$
\frac{d}{du}\mathcal F_{\ell+1}(\bar\Phi_u)
=-\mathsf G_{\ell+1}\!\left(\operatorname{grad}\mathcal F_{\ell+1},
M\operatorname{grad}\mathcal F_{\ell+1}\right)<0 ,
$$

so $\mathcal F_{\ell+1}$ is a strict Lyapunov function; the curve is injective
and no nonconstant periodic orbit exists. Consequently, under N1 the image
$c$ of T12 case 1 is injective and $\hat R_\ell|_{\mathcal O}$ is injective.

*Proof.* The displayed derivative is the chain rule; positivity of the
symmetric part of $M$ and $\operatorname{grad}\mathcal F_{\ell+1}\ne0$ (which
holds off equilibria, and by T12 case 1 the whole orbit is off equilibria)
make it strictly negative. A strictly monotone scalar along the curve
forbids equal values at distinct parameters. Injectivity of $c$ plus (FSC)
gives injectivity of $\hat R_\ell$ on $\mathcal O$. $\square$

---

## 4. Fine and coarse Fisher speeds and durations

### 4.1 Definitions with all three indices

**Definition D-TAU.** Let $r$ denote an admissible parameter on a fine orbit,
determined only up to $\mathcal G^+$ (Theorem T7). Along a representative
$r\mapsto Q^{(\ell)}(r)=\Phi_r(Q)$ define

$$
\nu_\ell(r)=\left\|X_\ell\!\left(Q^{(\ell)}(r)\right)\right\|_{\mathsf G_\ell},
\qquad
\tau^{(\ell)}(r)=\int_{r_0}^{r}\nu_\ell(u)\,du .
$$

For the *image* history at level $\ell+1$, written
$Q^{(\ell+1)}(r):=\hat R_\ell(Q^{(\ell)}(r))$ exactly as in
`eq:hist-levelwise-same-path-image`, define

$$
\nu^{\mathrm{img}}_{\ell+1}(r)
=\left\|\tfrac{d}{dr}Q^{(\ell+1)}(r)\right\|_{\mathsf G_{\ell+1}}
=\left\|T\hat R_\ell X_\ell\!\left(Q^{(\ell)}(r)\right)\right\|_{\mathsf G_{\ell+1}},
\qquad
\tau^{(\ell+1)}(r)=\int_{r_0}^{r}\nu^{\mathrm{img}}_{\ell+1}(u)\,du .
$$

### 4.2 Exact speed relation and the invisibility of the factor

**Theorem T14 (exact speeds; the positive factor cancels from duration).**
Under (SC),

$$
\nu^{\mathrm{img}}_{\ell+1}(r)
=a_\ell\!\left(Q^{(\ell)}(r)\right)
\left\|X_{\ell+1}\!\left(\hat R_\ell Q^{(\ell)}(r)\right)\right\|_{\mathsf G_{\ell+1}} ,
$$

and for every $r_0<r_1$ in $J_Q$,

$$
\tau^{(\ell+1)}(r_1)-\tau^{(\ell+1)}(r_0)
=\int_{\sigma_Q(r_0)}^{\sigma_Q(r_1)}
\left\|X_{\ell+1}\!\left(\bar\Phi_u(\hat R_\ell Q)\right)\right\|_{\mathsf G_{\ell+1}}du ,
$$

which is the intrinsic $\mathsf G_{\ell+1}$-arc length of the coarse orbit arc
between $\hat R_\ell Q^{(\ell)}(r_0)$ and $\hat R_\ell Q^{(\ell)}(r_1)$. In
particular $\tau^{(\ell+1)}$ depends on $a_\ell$ **not at all**: the factor is
a reparameterization datum, invisible to duration.

*Proof.* The first display is (SC) plus absolute homogeneity of the norm and
$a_\ell>0$. For the second, substitute (SC) and change variables
$u=\sigma_Q(s)$, whose Jacobian is $du=a_\ell(\Phi_sQ)ds$; the factor
$a_\ell$ appearing in the integrand cancels against the Jacobian. Positive
homogeneity is what makes the cancellation exact. $\square$

T14 is the precise reason why "$a_\ell$ is a rate" is a category error, and it
sharpens the SPEC rule at `SPEC.md:186`, "Any local parameter used to
calculate a path integral is auxiliary and must disappear from the final arc
length", into a theorem about the *coarse* level.

### 4.3 When durations agree, and when they differ by a factor

**Theorem T15 (duration comparison).** Under (SC), for all $r$ in the common
interval:

1. $\tau^{(\ell+1)}\equiv\tau^{(\ell)}$ (with the same origin $r_0$) if and
   only if
   $\left\|T\hat R_\ell X_\ell\right\|_{\mathsf G_{\ell+1}}
   =\left\|X_\ell\right\|_{\mathsf G_\ell}$ almost everywhere along the orbit.
2. $\tau^{(\ell+1)}\equiv\kappa\,\tau^{(\ell)}$ for a constant $\kappa>0$ if
   and only if
   $\left\|T\hat R_\ell X_\ell\right\|_{\mathsf G_{\ell+1}}
   =\kappa\left\|X_\ell\right\|_{\mathsf G_\ell}$ almost everywhere along the
   orbit.
3. $\tau^{(\ell+1)}$ has nonincreasing increments relative to $\tau^{(\ell)}$
   on every subinterval if and only if
   $\left\|T\hat R_\ell X_\ell\right\|_{\mathsf G_{\ell+1}}
   \le\left\|X_\ell\right\|_{\mathsf G_\ell}$ pointwise along the orbit.

None of (1), (2), (3) follows from (SC), and none follows from
$a_\ell\equiv1$.

*Proof.* Both durations are integrals of continuous nonnegative densities from
the common origin $r_0$; two such integrals coincide for all upper limits if
and only if the densities agree almost everywhere, by Lebesgue
differentiation, and analogously for the scaled and ordered versions. The
final sentence is CE-DURATION-MISMATCH below, in which $a_\ell\equiv1$ and
(SC) hold exactly while (3) fails. $\square$

Condition (3) is a statement about the triple
$(\mathsf G_\ell,\mathsf G_{\ell+1},T\hat R_\ell)$ evaluated on the single
direction $X_\ell$. It says nothing about statistical channels, and it is not
implied by any Markov contraction theorem in the manuscript.

### 4.4 The identity-map counterexample

**Counterexample CE-DURATION-MISMATCH (certified here; register entry
promoted from CANDIDATE).** Let both configuration manifolds be
$\mathcal Q=\mathbb R$, let $X_\ell=X_{\ell+1}=\partial_x$, and let
$\hat R_\ell=\operatorname{id}_{\mathbb R}$. Then (SC) holds exactly with
$a_\ell\equiv1$, no collapse occurs, N0 through N4 all hold, and the map is a
diffeomorphism. Declare

$$
\mathsf G_\ell=dx^2,
\qquad
\mathsf G_{\ell+1}=4\,dx^2 .
$$

Then $\nu_\ell\equiv1$, $\nu^{\mathrm{img}}_{\ell+1}\equiv2$, and

$$
\tau^{(\ell+1)}(r)=2\,\tau^{(\ell)}(r)\qquad\text{for every }r .
$$

Coarse duration is exactly twice fine duration: the comparison fails in the
*expanding* direction, and replacing $4$ by $\tfrac14$ makes it contract by
two. The sign of the comparison is decided entirely by the declared metrics.

**Both metrics are legitimate Fisher metrics, in two independent
realizations.**

*Realization (a), channel weights.* Take a one-point contextual domain
$\mathcal C_\ell=\mathcal C_{\ell+1}=\{c_1\}$, belief fiber
$\{\mathcal N(\mu,1):\mu\in\mathbb R\}$, and configuration manifold
$\mathcal Q=\mathbb R$ coordinatized by $\mu$. The manuscript's pointwise
clock `eq:hist-pointwise-clock-speed`,
`05d_relational_inference.tex:463-468`, is
$\nu_{i,c}^2=w_b(c)\,g_b^F(\partial_\lambda q_i(c),\partial_\lambda q_i(c))+\dots$
with *declared positive channel weights* $w_b,w_m$. Take $w_b^{(\ell)}=1$ and
$w_b^{(\ell+1)}=4$; the fiber map $\Psi$ is the identity, which is a
normalized, parameter-independent Markov kernel with vertical Fisher defect
$\Delta_F^\Psi=0$ exactly. **Information loss is exactly zero and duration
still doubles.**

*Realization (b), sharper fiber.* Take fine fiber $\{\mathcal N(\mu,1)\}$ with
Fisher metric $d\mu^2$ and coarse fiber $\{\mathcal N(\mu,\tfrac14)\}$ with
Fisher metric $4\,d\mu^2$, and let $\hat R_\ell$ be the identity on the
parameter $\mu$. Both are honest smooth statistical models with
positive-definite Fisher metrics; the parameter map is the identity.

**Consequences, stated exactly.**

- Fiberwise Markov Fisher contraction (`thm:pb-pullback-fisher-defect`,
  `thm:cg-fisher-contraction`, `thm:hist-record-clock-contraction`) constrains
  the *fiber* tensors $g^F$ and $(T^V\Psi)^*\bar g^F$. It says nothing about
  the *configuration* metrics $\mathsf G_\ell$ and $\mathsf G_{\ell+1}$, which
  by `configuration-fisher-metric` are separately declared objects assembled
  from a base measure $\mu_i$, design weights $\rho_a$, channel weights
  $w_b,w_m$, and a gauge-quotient rule
  (`05d_relational_inference.tex:458-536`).
- Realization (a) shows the failure is *not* about information loss: the
  defect is exactly zero and the durations still disagree.
- Therefore no duration comparison between levels follows from the contraction
  theorems alone, whether or not (SC) holds.

### 4.5 When the fiberwise contraction does lift

**Theorem T16 (configuration-level contraction under weight compatibility).**
Assume:

1. $\mathcal C_{\ell+1}=\mathcal C_\ell=:\mathcal C_i$ with the same declared
   finite positive base measure $\mu_i$ and the same measurable positive
   channel weights $w_x$;
2. $\hat R_\ell$ acts pointwise, $(\hat R_\ell Q)(c)=\Psi_c(Q(c))$, where each
   $\Psi_c$ is the pushforward of a normalized parameter-independent Markov
   kernel between the regular fine and coarse fibers at $c$, with vertical
   differential $T^V\Psi_c$;
3. both configuration metrics are the corresponding weighted integrals of the
   fiber Fisher metrics, that is
   $\|Z\|^2_{\mathsf G_\ell}=\int_{\mathcal C_i}\sum_x w_x(c)\,
   g^F_{x,\,Q(c)}(Z_x(c),Z_x(c))\,d\mu_i(c)$ and likewise at level $\ell+1$
   with $\bar g^F$;
4. every displayed integral is finite.

Then for every $Z\in T_Q\mathcal Q_\ell$,

$$
\left\|Z\right\|^2_{\mathsf G_\ell}-\left\|T\hat R_\ell Z\right\|^2_{\mathsf G_{\ell+1}}
=\int_{\mathcal C_i}\sum_x w_x(c)\,
\Delta_F^{\Psi_c}\!\left(Z_x(c),Z_x(c)\right)d\mu_i(c)
=\int_{\mathcal C_i}\sum_x w_x(c)\,
\mathbb E\operatorname{Var}\!\left(\ell_{Z_x(c)}\mid Y_c\right)d\mu_i(c)\;\ge 0 .
$$

Consequently $\nu^{\mathrm{img}}_{\ell+1}\le\nu_\ell$ pointwise and
$\tau^{(\ell+1)}\le\tau^{(\ell)}$ increment by increment, with equality on a
subinterval exactly when the fine score in the direction $Z_x(c)$ is
$Y_c$-measurable for $\mu_i$-almost every $c$ and every channel $x$, along
that subinterval.

*Proof.* Differentiate the pointwise action along a curve
$\lambda\mapsto Q_\lambda$ with $\dot Q_0=Z$: at each fixed $c$,
$\partial_\lambda\Psi_c(Q_\lambda(c))=T^V\Psi_c(Z_x(c))$, using T5 to know
$Z_x(c)$ is vertical. Insert into hypothesis 3 at level $\ell+1$ to get
$\|T\hat R_\ell Z\|^2_{\mathsf G_{\ell+1}}
=\int\sum_x w_x\,\big[(T^V\Psi_c)^*\bar g^F\big](Z_x(c),Z_x(c))\,d\mu_i$.
Subtract from hypothesis 3 at level $\ell$ and use the definition
$\Delta_F^{\Psi_c}=g^F-(T^V\Psi_c)^*\bar g^F$ of
`eq:pb-vertical-fisher-defect`. Nonnegativity of the integrand and the
conditional-variance identity are `eq:pb-fisher-defect-positive` and
`eq:pb-fisher-defect-score-variance`,
`05c_pullback_geometry.tex:687-720`, proved from the score-projection theorem
`thm:cg-fisher-contraction`, `06_general_coarsegraining.tex:190-199`.
Monotonicity of the integral, then monotonicity of the square root, gives the
speed inequality; integrating in $r$ gives the duration inequality; the
equality case is the pointwise equality case integrated against a positive
measure. $\square$

Hypothesis 1 is exactly what CE-DURATION-MISMATCH realization (a) violates.
Hypothesis 2 is exactly what `08_infogeometry.tex:505-527` says the
manuscript's Galerkin aggregation does **not** satisfy: by
`prop:ig-pullback-vs-pushforward` the coarse operator there is a restriction,
not a Markov pushforward, and the two differ by a positive-semidefinite Schur
term with the restriction *larger* in the Loewner order.

**Theorem T17 (contraction without semiconjugacy compares nothing).** Even
under all hypotheses of T16, the conclusion concerns the *image*
$\hat R_\ell\circ Q^{(\ell)}$, not the independently recomputed coarse
history.

**Counterexample CE-D3 (identity channel, different objectives).** Take
$\mathcal Q_\ell=\mathcal Q_{\ell+1}=\mathbb R^2$ Euclidean,
$\hat R_\ell=\operatorname{id}$, and $\Psi=\operatorname{id}$: hypotheses 1
through 4 of T16 hold with $\Delta_F^\Psi\equiv0$, so the contraction is an
equality and $\tau^{(\ell+1)}=\tau^{(\ell)}$ for the image. Now let
$\mathcal F_\ell(x,y)=\tfrac12(x^2+y^2)$ and
$\mathcal F_{\ell+1}(x,y)=\tfrac12(x^2+4y^2)$. From $Q_0=(1,1)$ the fine
history is the straight segment $(e^{-t},e^{-t})$ with total Fisher duration
$\sqrt2$; the independently recomputed coarse history is $(e^{-t},e^{-4t})$,
a curve from $(1,1)$ to $(0,0)$ that is not a straight segment, hence has
total duration strictly greater than the Euclidean distance $\sqrt2$. Also
(SC) fails: with $\hat R=\operatorname{id}$ it would require
$(-x,-y)=a\,(-x,-4y)$, which forces $a=1$ and then $y=4y$, false off the axis
$y=0$. **Consequence:** with perfect information preservation, a perfectly
compatible pair of configuration metrics, and no collapse, the independently
recomputed coarse duration still differs from the fine one, because the two
histories are different curves. Contraction alone compares nothing.

CE-D3 and CE-DURATION-MISMATCH together prove that the two conditions are
logically independent and that neither implies the other, which is the exact
content of the manuscript's sentence at
`05d_relational_inference.tex:753-759`, "Either condition without the other is
insufficient." That sentence is currently asserted without either witness.
**Minimal repair R-5:** attach CE-DURATION-MISMATCH and CE-D3 to it.

---

## 5. Natural-gradient semiconjugacy

Throughout this section $X_\ell=-\operatorname{grad}^{\mathsf G_\ell}\mathcal F_\ell$
and $X_{\ell+1}=-\operatorname{grad}^{\mathsf G_{\ell+1}}\mathcal F_{\ell+1}$
with $\mathcal F_\ell,\mathcal F_{\ell+1}\in C^2$ and both metrics strong.

### 5.1 Equality of objectives does not intertwine gradients

**Theorem T18 (diffeomorphic case, exact criterion).** Let $\hat R_\ell$ be a
$C^1$ diffeomorphism and let $\mathcal F_\ell=\mathcal F_{\ell+1}\circ\hat R_\ell$.
Write $\tilde{\mathsf G}:=(\hat R_\ell)_*\mathsf G_\ell$ for the pushforward
metric. Then (SC) holds at $Q$ with factor $a$ if and only if
$d\mathcal F_{\ell+1}$ at $\hat R_\ell Q$ is an eigencovector of the
endomorphism $\mathsf G_{\ell+1}\tilde{\mathsf G}^{-1}$ of the cotangent
space, with eigenvalue $a$; and then $a>0$ automatically.

*Proof.* $T\hat R_\ell\operatorname{grad}^{\mathsf G_\ell}(\mathcal F_{\ell+1}\circ\hat R_\ell)
=\operatorname{grad}^{\tilde{\mathsf G}}\mathcal F_{\ell+1}$ by naturality of
the gradient under a metric pushforward. So (SC) reads
$\tilde{\mathsf G}^{-1}d\mathcal F_{\ell+1}=a\,\mathsf G_{\ell+1}^{-1}d\mathcal F_{\ell+1}$,
that is $\mathsf G_{\ell+1}\tilde{\mathsf G}^{-1}d\mathcal F_{\ell+1}=a\,d\mathcal F_{\ell+1}$.
Both $\mathsf G_{\ell+1}$ and $\tilde{\mathsf G}$ are positive definite, so
$\mathsf G_{\ell+1}\tilde{\mathsf G}^{-1}$ is similar to a positive-definite
operator and its eigenvalues are positive. $\square$

**Counterexample CE-D4 (equal objectives, no intertwining).** Take
$\mathcal Q_\ell=\mathcal Q_{\ell+1}=\mathbb R^2$,
$\hat R_\ell=\operatorname{id}$, and the *same* objective
$\mathcal F(x,y)=\tfrac12(x^2+2y^2)$ at both levels. Let
$\mathsf G_\ell=\operatorname{diag}(1,1)$ and
$\mathsf G_{\ell+1}=\operatorname{diag}(1,\kappa)$ with $\kappa\ne1$, $\kappa>0$;
both are Fisher metrics of the location families
$\mathcal N((x,y),I)$ and $\mathcal N((x,y),\operatorname{diag}(1,\kappa^{-1}))$.
Then $\operatorname{grad}^{\mathsf G_\ell}\mathcal F=(x,2y)$ and
$\operatorname{grad}^{\mathsf G_{\ell+1}}\mathcal F=(x,2y/\kappa)$. (SC) would
require $(x,2y)=a\,(x,2y/\kappa)$; the first component forces $a=1$ wherever
$x\ne0$, and then the second forces $\kappa=1$. So (SC) fails on the dense
open set $\{xy\ne0\}$. **Consequence:** identical scalar objectives, an
identity coarse map, and both metrics positive definite are jointly
insufficient. The gradient is a metric-dependent object; only the
*differential* $d\mathcal F$ is metric-free, and (SC) is a condition on
gradients. This is the exact reason `08_infogeometry.tex:531-538` insists that
"an update is a natural gradient only when its metric is the Fisher metric of
the family being updated, in a named chart".

### 5.2 Functional compatibility: what it does and does not buy

**Definition D-FC.** $\hat R_\ell$ and the two objectives are **functionally
compatible** on $U$ when there is $\chi_\ell\in C^2(\mathbb R)$ with
$\chi_\ell'>0$ and

$$
\mathcal F_\ell=\chi_\ell\circ\mathcal F_{\ell+1}\circ\hat R_\ell
\qquad\text{on }U .
\tag{FC}
$$

**Theorem T19 (functional compatibility gives noncriticality transfer,
horizontality, and noncollapse, with no metric hypothesis).** Assume (FC) on
$U$, H-D1, and N5 ($\ker T_Q\hat R_\ell$ closed and complemented). Then for
$Q\in U$:

1. $d\mathcal F_\ell(Q)=\chi_\ell'(\mathcal F_{\ell+1}(\hat R_\ell Q))\cdot
   (\hat R_\ell^*d\mathcal F_{\ell+1})(Q)$; hence
   $d\mathcal F_\ell(Q)\ne0\Rightarrow d\mathcal F_{\ell+1}(\hat R_\ell Q)\ne0$.
   **A noncritical fine configuration has a noncritical coarse image.**
2. $\ker T_Q\hat R_\ell\subseteq\ker d\mathcal F_\ell(Q)$, hence
   $\operatorname{grad}^{\mathsf G_\ell}\mathcal F_\ell(Q)\perp_{\mathsf G_\ell}\ker T_Q\hat R_\ell$:
   the natural-gradient field is **horizontal** for the coarse-graining
   fibration, with no submersion or metric-compatibility hypothesis.
3. $T_Q\hat R_\ell X_\ell(Q)=0\iff X_\ell(Q)=0$. **Noncollapse is automatic.**

*Proof.* (1) Chain rule; $\chi_\ell'>0$ makes the scalar nonzero, and a
pullback of the zero covector is zero. (2) If $Z\in\ker T_Q\hat R_\ell$ then
$(\hat R_\ell^*d\mathcal F_{\ell+1})(Z)=d\mathcal F_{\ell+1}(T\hat R_\ell Z)=0$,
so $d\mathcal F_\ell(Z)=0$ by (1); by the definition of the gradient,
$\mathsf G_\ell(\operatorname{grad}\mathcal F_\ell,Z)=d\mathcal F_\ell(Z)=0$.
(3) By (2), $X_\ell(Q)\in(\ker T_Q\hat R_\ell)^{\perp_{\mathsf G_\ell}}$, and
$T_Q\hat R_\ell$ restricted to that complement has kernel
$\ker T_Q\hat R_\ell\cap(\ker T_Q\hat R_\ell)^{\perp}=\{0\}$, using N5 and
positive definiteness of $\mathsf G_\ell$. $\square$

T19 is the strongest result of this route. It says the entire noncollapse
problem is dissolved by a *functional* hypothesis and requires no statement
about the metrics at all. It also explains CE-HISTORY-COLLAPSE: there,
$\mathcal F_{\ell+1}$ is constant and $\hat R_\ell$ is constant, so (FC) would
force $\mathcal F_\ell$ constant and there would be no nonconstant fine
history to collapse.

**Theorem T20 (rank-one intertwining criterion, and automatic positivity).**
Assume (FC) on $U$ and $X_\ell(Q)\ne0$. Then (SC) holds at $Q$ with *some*
real factor if and only if

$$
T_Q\hat R_\ell\!\left(\operatorname{grad}^{\mathsf G_\ell}\mathcal F_\ell(Q)\right)
\in
\mathbb R\cdot\operatorname{grad}^{\mathsf G_{\ell+1}}\mathcal F_{\ell+1}\!\left(\hat R_\ell Q\right),
$$

and in that case the factor is automatically positive, namely

$$
a_\ell(Q)
=\frac{\left\|\operatorname{grad}^{\mathsf G_\ell}\mathcal F_\ell(Q)\right\|^2_{\mathsf G_\ell}}
{\chi_\ell'\!\left(\mathcal F_{\ell+1}(\hat R_\ell Q)\right)\,
\left\|\operatorname{grad}^{\mathsf G_{\ell+1}}\mathcal F_{\ell+1}(\hat R_\ell Q)\right\|^2_{\mathsf G_{\ell+1}}}
\;>\;0 .
$$

*Proof.* Write $u=\operatorname{grad}^{\mathsf G_\ell}\mathcal F_\ell(Q)\ne0$
and $w=\operatorname{grad}^{\mathsf G_{\ell+1}}\mathcal F_{\ell+1}(\hat R_\ell Q)$,
which is nonzero by T19(1). Suppose $T\hat R_\ell u=c\,w$. Pair with $w$:

$$
c\left\|w\right\|^2_{\mathsf G_{\ell+1}}
=\mathsf G_{\ell+1}(T\hat R_\ell u,w)
=d\mathcal F_{\ell+1}\!\left[T\hat R_\ell u\right]
=\left(\hat R_\ell^*d\mathcal F_{\ell+1}\right)[u]
=\frac{1}{\chi_\ell'}\,d\mathcal F_\ell[u]
=\frac{\left\|u\right\|^2_{\mathsf G_\ell}}{\chi_\ell'}
\;>\;0 ,
$$

using (FC) in the fourth equality and the definition of $u$ in the fifth.
Since $\|w\|^2>0$ and $\chi_\ell'>0$, we get $c>0$ and the displayed formula.
Negating both sides converts the gradient statement into the descent-field
statement (SC). $\square$

T20 is the precise decomposition asked for: **functional compatibility
supplies orientation and noncollapse for free; metric compatibility supplies
only the parallelism.** In particular, CE-D2's orientation reversal is
impossible under (FC), and CE-D4's failure is exactly a failure of the
rank-one condition, not of (FC).

### 5.3 Metric sufficient conditions

**Theorem T21 (Riemannian and horizontally conformal submersions).** Let
$\hat R_\ell$ be a surjective submersion with N5, let
$\mathcal H=(\ker T\hat R_\ell)^{\perp_{\mathsf G_\ell}}$, and assume (FC).

1. If $\hat R_\ell$ is a **Riemannian submersion**, that is
   $T\hat R_\ell|_{\mathcal H}$ is a linear isometry onto
   $T\mathcal Q_{\ell+1}$, then (SC) holds with $a_\ell=\chi_\ell'>0$;
   with $\chi_\ell=\operatorname{id}$, $a_\ell\equiv1$.
2. If $\hat R_\ell$ is **horizontally conformal with dilation
   $\varphi_\ell>0$**, that is
   $\mathsf G_{\ell+1}(T\hat R_\ell Z,T\hat R_\ell Z')=\varphi_\ell^2\,\mathsf G_\ell(Z,Z')$
   for all $Z,Z'\in\mathcal H$, then (SC) holds with
   $a_\ell=\chi_\ell'\,\varphi_\ell^2>0$.

*Proof.* By T19(2), $u:=\operatorname{grad}^{\mathsf G_\ell}\mathcal F_\ell\in\mathcal H$.
Let $w=\operatorname{grad}^{\mathsf G_{\ell+1}}\mathcal F_{\ell+1}\circ\hat R_\ell$.
For every $Z\in\mathcal H$,

$$
\mathsf G_{\ell+1}(T\hat R_\ell u,T\hat R_\ell Z)
=\varphi_\ell^2\,\mathsf G_\ell(u,Z)
=\varphi_\ell^2\,d\mathcal F_\ell[Z]
=\varphi_\ell^2\chi_\ell'\,d\mathcal F_{\ell+1}[T\hat R_\ell Z]
=\varphi_\ell^2\chi_\ell'\,\mathsf G_{\ell+1}(w,T\hat R_\ell Z).
$$

Since $\hat R_\ell$ is a submersion, $T\hat R_\ell(\mathcal H)$ is all of
$T\mathcal Q_{\ell+1}$, so nondegeneracy gives
$T\hat R_\ell u=\varphi_\ell^2\chi_\ell'\,w$. Negate for the descent fields.
Part 1 is part 2 with $\varphi_\ell\equiv1$. $\square$

**Sanity check.** $\mathcal Q_\ell=\mathcal Q_{\ell+1}=\mathbb R$ Euclidean,
$\hat R_\ell(x)=\lambda x$: then $\varphi_\ell=|\lambda|$, and
$\mathcal F_\ell=\mathcal F_{\ell+1}\circ\hat R_\ell$ gives
$\mathcal F_\ell'=\lambda\,\mathcal F_{\ell+1}'(\lambda x)$, hence
$T\hat R_\ell\operatorname{grad}\mathcal F_\ell=\lambda^2\mathcal F_{\ell+1}'$,
matching $a_\ell=\varphi_\ell^2=\lambda^2$.

### 5.4 Why the manuscript's coarse maps are not yet known to qualify

**Proposition P-1 (a Markov configuration map is a contraction, and is a
horizontally conformal submersion only on a sufficiency locus).** Under the
hypotheses of T16, the pointwise Markov configuration map satisfies
$\|T\hat R_\ell Z\|_{\mathsf G_{\ell+1}}\le\|Z\|_{\mathsf G_\ell}$ for every
$Z$, with the exact defect displayed in T16. Consequently:

1. $\hat R_\ell$ can be a Riemannian submersion only if $\Delta_F^{\Psi_c}$
   restricted to the horizontal space vanishes $\mu_i$-almost everywhere,
   that is only if the coarse channel is Fisher-sufficient for every
   horizontal direction;
2. $\hat R_\ell$ can be horizontally conformal with dilation
   $\varphi_\ell\in(0,1]$ only if
   $\Delta_F^{\Psi_c}\big|_{\mathcal H}=(1-\varphi_\ell^2)\,g^F\big|_{\mathcal H}$,
   that is only if the information loss on the horizontal space is a *constant
   multiple* of the metric there.

*Proof.* Immediate from T16 and the definitions in T21. $\square$

**Proposition P-2 (the exact-RG contracted functional gives (FC) only on its
attaining set).** Following the effective-theory audit, define the contracted
coarse functional
$\mathcal F_{\ell+1}[Q']:=\inf\{\mathcal F_\ell[q]:\hat R_\ell q=Q'\}$. Then

$$
\mathcal F_{\ell+1}\!\left(\hat R_\ell q\right)\le\mathcal F_\ell(q)
\qquad\text{for every }q ,
$$

with equality exactly on the attaining set
$\mathcal A_\ell=\{q:\mathcal F_\ell(q)=\min_{\hat R_\ell q'=\hat R_\ell q}\mathcal F_\ell(q')\}$.
Hence (FC) with $\chi_\ell=\operatorname{id}$ holds on $\mathcal A_\ell$ and
nowhere else, and its *differential* consequence T19 requires
$\mathcal A_\ell$ to have nonempty interior containing the fine orbit.

*Proof.* The inequality and the equality case are the definition of an
infimum. Differentiating an identity that holds only on a set requires the set
to be open. $\square$

**Consequence and the exact missing obligation.** For the manuscript's
independently recomputed RG histories, the minimal remaining obligation is:

> **O-SC.** Exhibit $\chi_\ell$ with $\chi_\ell'>0$ and an open set
> $U\supseteq\mathcal O$ containing the fine natural-gradient orbit on which
> (FC) holds — for the exact-RG contraction, prove
> $\mathcal O\subseteq\operatorname{int}\mathcal A_\ell$ — and then verify the
> rank-one condition of T20, for which P-1(2) (horizontal conformality of the
> declared configuration coarse map) is a sufficient metric hypothesis.

O-SC is strictly weaker than proving (SC) directly, and it is stated in terms
of objects the manuscript already declares. This is the minimal repair for
the standing `OPEN` at `05c_pullback_geometry.tex:832-842`,
`05d_relational_inference.tex:753-762`, and
`appendix_claim_ledger.tex:147-154`.

---

## 6. Three independent coordinates: depth, orbit position, and duration

### 6.1 The three coordinates, typed

| Symbol | Type | Domain | Determined up to |
|---|---|---|---|
| $\ell$ | scale depth | a finite ordered scale set; a discrete index on the RG diagram | nothing; it is an index, not a real coordinate |
| $r$ | auxiliary orbit position | an interval $J$, a chart on one oriented orbit | the full group $\mathcal G^+$ of orientation-preserving $C^1$ reparameterizations |
| $\tau^{(\ell)}(r)$ | accumulated Fisher duration at level $\ell$ | $[0,\infty)$-valued, nondecreasing in $r$ | a choice of origin $r_0$; *and* the declared metric $\mathsf G_\ell$ |

**Notation obligation.** The manuscript writes $Q^{(\ell)}(r)$ at
`eq:hist-rg-depth-index` and `eq:hist-levelwise-same-path-image`
(`05d_relational_inference.tex:764-786`) but writes the clock as
$\tau_{Q,\lambda_0}(\lambda)$ at `def:hist-fisher-clock`
(`05d_relational_inference.tex:360-376`), with no scale index. The levelwise
duration $\tau^{(\ell)}$ therefore does not exist in the current notation.
**Minimal repair R-6:** introduce $\tau^{(\ell)}(r)$ as in D-TAU and use all
three symbols together, which is what plan Task 10 Step 6 requires.

### 6.2 Exactly what is invariant

**Theorem T22 (invariance).** Let $\widetilde Q=Q\circ\phi$ with
$\phi\in\mathcal G^+$ and $\lambda_0=\phi(\widetilde\lambda_0)$. Then:

1. $\widetilde\nu_F=(\nu_F\circ\phi)\,\phi'$ — the speed is **not**
   invariant;
2. $L_F$ on corresponding subarcs is invariant;
3. $\tau_{\widetilde Q,\widetilde\lambda_0}=\tau_{Q,\lambda_0}\circ\phi$ — the
   clock is **equivariant as a function of the parameter and invariant as a
   function of the point on the oriented curve**;
4. consequently $\tau$ descends to a well-defined function on the oriented
   curve $\mathscr H$ (which retains traversal order and multiplicity), once
   an origin is chosen on $\mathscr H$.

*Proof.* (1) and (3) are the chain rule and the substitution $u=\phi(\cdot)$,
which is `thm:hist-fisher-clock-invariance`,
`05d_relational_inference.tex:378-418`. (4) By construction $\mathscr H$ is
the $\mathcal G^+$-orbit of parameterized representatives
(`def:hist-oriented-history`), and (3) says $\tau$ is a $\mathcal G^+$-invariant
section of that construction. $\square$

**What is not invariant, and must never be reported without its
declarations:** the origin $r_0$; the metric $\mathsf G_\ell$ (see T23); the
orientation, which comes from the descent ray and reverses under
$\mathcal F\mapsto-\mathcal F$; and the level $\ell$.

**Theorem T23 (duration is metric-relative, not just parameter-invariant).**
Replacing $\mathsf G_\ell$ by $\rho^2\mathsf G_\ell$ for a positive constant
$\rho$ multiplies every $\tau^{(\ell)}$ by $\rho$ while changing no orbit, no
orientation, and no parameterization class. Replacing $\mathsf G_\ell$ by a
nonconformal metric changes the ratios of durations of different subarcs.

*Proof.* Absolute homogeneity of the norm; and CE-DURATION-MISMATCH exhibits
the constant-$\rho$ case with $\rho=2$. For the second statement, in
$\mathbb R^2$ with $X=\partial_x+\partial_y$ compare
$\operatorname{diag}(1,1)$ with $\operatorname{diag}(1,4)$ on the two coordinate
sub-arcs. $\square$

T23 is the sharpest available statement against a physical reading: an
"emergent clock" whose readings scale by an arbitrary declared constant, and
whose subarc ratios change with a declared weighting, is not a clock in any
operational sense. This is the mathematical content behind the `OPEN`
"Physical-time identification" entry at
`appendix_claim_ledger.tex:235-241`, which currently lists only the
operational obligations and not this internal ambiguity. **Minimal repair
R-7:** add metric relativity to that entry.

### 6.3 Strict monotonicity versus regular coordinate

**Theorem T24 (monotonicity trichotomy).** Let $\nu_\ell\ge0$ be continuous on
an interval $I$ and $\tau^{(\ell)}(r)=\int_{r_0}^r\nu_\ell$.

1. $\tau^{(\ell)}$ is always nondecreasing and $C^1$ with
   $(\tau^{(\ell)})'=\nu_\ell$.
2. $\tau^{(\ell)}$ is **strictly increasing** on $I$ if and only if
   $\nu_\ell^{-1}(0)$ has empty interior in $I$; equivalently, every
   nondegenerate subinterval carries positive accumulated length.
3. $\tau^{(\ell)}$ is a **regular coordinate** on $I$ — a $C^1$ diffeomorphism
   onto its image with $C^1$ inverse — if and only if $\nu_\ell>0$ everywhere
   on $I$.

*Proof.* (1) Fundamental theorem of calculus for a continuous integrand.
(2) For continuous $\nu_\ell\ge0$, $\int_u^v\nu_\ell=0$ with $u<v$ if and only
if $\nu_\ell\equiv0$ on $[u,v]$; failure of strict monotonicity is exactly the
existence of such a pair. (3) Inverse function theorem in one dimension:
$(\tau^{(\ell)})'=\nu_\ell$ must be nonvanishing; conversely a positive
continuous derivative gives a $C^1$ diffeomorphism onto an open interval.
$\square$

**Witness W-2 (isolated zero: strictly increasing but not regular).** Use the
manuscript's own rank-jump section `eq:pb-rank-jump-example`,
`05c_pullback_geometry.tex:361-370`: the normal location family on
$\mathcal C=\mathbb R$ with $s(x)=\mathcal N(x^2,1)$ and the zero connection
gives $h_s=4x^2dx^2$, so $\nu=2|x|$. Then $\tau(r)=\int_0^r2|u|du=r^2$ for
$r\ge0$: strictly increasing on $[0,\infty)$ by T24(2) since $\{ \nu=0\}=\{0\}$
has empty interior, yet $\tau^{-1}(v)=\sqrt v$ is not differentiable at
$v=0$, so $\tau$ is not a regular coordinate at the origin, exactly as T24(3)
predicts. Both conclusions are needed and neither implies the other.

### 6.4 Zero-speed intervals, Fisher-null directions, singular strata, closed
histories

**(a) Zero-speed intervals.** By T24(2) these are exactly the intervals where
$\nu_\ell\equiv0$, and there $\tau^{(\ell)}$ stalls. Under a *strong* metric
and a natural-gradient field, $\nu_\ell=\|X_\ell\|_{\mathsf G_\ell}=0$ forces
$X_\ell=0$, so the configuration is at a critical point and, by uniqueness of
the flow, the whole orbit is that single point. **Therefore, on a strong
regular metric tier, a natural-gradient history has no nontrivial zero-speed
interval: it either moves at positive speed throughout or is stationary.**
Zero-speed intervals arise only in the degenerate cases (b) and (c).

**(b) Fisher-null directions.** If $\mathsf G_\ell$ is only positive
semidefinite, there can be $X_\ell(Q)\ne0$ with
$\mathsf G_\ell(X_\ell,X_\ell)=0$. Then the configuration genuinely changes
while accruing zero duration, so $\tau^{(\ell)}$ is constant along a
nonconstant history and is not a coordinate on it. Witness: on
$\mathbb R^2$ with $\mathsf G=dx^2$ and the declared field $X=\partial_y$,
every orbit $\{x=\text{const}\}$ is nonconstant with $\nu\equiv0$. This is
also the regime where `prop:hist-semidefinite-gradient-obstruction`
(`05d_relational_inference.tex:344-355`) shows the natural-gradient equation
can have no solution or infinitely many, so both the orientation and the
duration fail together. The declared remedy is the justified metric quotient
of `thm:pb-pullback-rank-quotient`, which requires constant rank, involutivity
(`eq:pb-null-involutivity`), a regular leaf space, and basicness
(`eq:pb-null-basicness`) — four separate obligations, with the constant-rank
contact witness `prop:pb-contact-null-counterexample` showing the second can
fail at constant rank.

**(c) Singular-stratum boundaries.** Two behaviors occur and must be
distinguished.

- *Blow-up of the metric.* In the normal family with Fisher metric
  $(d\mu^2+2\,d\sigma^2)/\sigma^2$, the path $\sigma(t)=e^{-t}$ at fixed $\mu$
  has $\nu\equiv\sqrt2$ and $\tau(t)=\sqrt2\,t\to\infty$: the degenerate
  stratum $\sigma=0$ is at *infinite* Fisher duration. Such a boundary is
  never reached in finite duration, so the duration coordinate extends
  without repair on the open regular stratum.
- *Rank drop of the pullback.* Witness W-2 above: the metric speed extends
  continuously to zero, $\tau$ remains strictly increasing but loses
  regularity at the crossing. Here duration survives as a strictly increasing
  scalar but not as a chart.

Neither behavior is covered by the smooth-stratum sufficient theorem, and each
requires its own pathwise argument. **Minimal repair R-8:** where the
manuscript writes "A null segment in a semimetric or a critical stationary
segment has $\nu_F=0$, so the cumulative clock stalls and cannot be used as a
coordinate there" (`05d_relational_inference.tex:423-425`), split the sentence
into T24(2) versus T24(3), because "cannot be used as a coordinate" is true in
both the stalling case and the isolated-zero case, but for different reasons
and with different consequences.

**(d) Closed histories.**

**Theorem T25 (no closed natural-gradient histories; $\tau$ is single-valued
on gradient orbits).** Under the hypotheses of T13 with
$M=\operatorname{id}$, $\mathcal F_\ell$ is a strict Lyapunov function along
every nonconstant integral curve, so no nonconstant periodic orbit exists,
every nonconstant orbit map is injective, and $\tau^{(\ell)}$ is a strictly
increasing single-valued function on the oriented orbit.

*Proof.* T13 with $M=\operatorname{id}$. $\square$

**Witness W-3 (closed history for a non-gradient declared field).** On
$\mathbb R^2$ Euclidean take the declared field $X=(-y,x)$. Its orbits are
circles of period $2\pi$; along the unit circle $\nu\equiv1$ and
$\tau(r)=r$ grows without bound while the configuration returns to its start
every $2\pi$. Thus $\tau$ is a function on the *universal cover* of the orbit,
not on the orbit point set: it is well defined on $\mathscr H$ (which retains
multiplicity, per `def:hist-oriented-history`) but multivalued modulo the
period on the image set. **Consequence:** the sentence in
`def:hist-oriented-history` that "With self-intersections, $\mathscr H_i$
retains traversal order and multiplicity and is not merely the set-theoretic
image" is exactly the hypothesis that keeps $\tau$ single-valued, and T25
records the separate fact that a *natural-gradient* history can never realize
this case. This distinction is currently absent and is worth one sentence.

### 6.5 The three coordinates are pairwise independent

**Theorem T26 (independence).**

1. **$\ell$ against $\tau$.** There is an admitted configuration for which
   $\ell$ increases through arbitrarily many levels while $\tau^{(\ell)}\equiv0$
   at every level: take $Q$ a critical point of $\mathcal F_\ell$ at every
   level (equivalently, the stationary history), so every fine and coarse
   orbit is a point and every duration is zero. Conversely, at fixed $\ell$,
   $\tau^{(\ell)}$ increases along any noncritical orbit. Hence neither
   determines the other, and $\ell$ is not a monotone function of $\tau$ or
   vice versa. Moreover, by CE-DURATION-MISMATCH, even along a *fixed* fine
   orbit, increasing $\ell$ by one can multiply the duration by any positive
   constant. **RG depth is therefore not a duration, not even up to a
   monotone reparameterization.**
2. **$r$ against $\tau$.** $r$ is defined only up to $\mathcal G^+$ (T7) while
   $\tau$ is $\mathcal G^+$-invariant (T22), so they are not the same
   coordinate; and W-1 gives a history on which $r$ ranges over $[0,\infty)$
   while $\tau$ ranges over $[0,1)$. Conversely W-3 gives a history on which
   $r$ ranges over $[0,2\pi]$ while $\tau$ returns no information about
   position.
3. **$\ell$ against $r$.** Under (SC), the coarse *flow* parameter
   corresponding to fine parameter $r$ is $\sigma_Q(r)\ne r$ in general (T8,
   with CE-D1 giving $\sigma_0=\arctan$). Therefore writing $Q^{(\ell)}(r)$ and
   $Q^{(\ell+1)}(r)$ at the same $r$, as in
   `eq:hist-levelwise-same-path-image`, is a **definition of the image
   parameterization**, not a synchronization of two independently
   parameterized histories; by Corollary T7a no such synchronization exists.

**Minimal repair R-9:** state item 3 explicitly at
`eq:hist-levelwise-same-path-image`, since that equation is exactly where a
reader may take "the same $r$" as a cross-level simultaneity.

### 6.6 $\tau$ is not a function on the contextual base, and not physical time

**Theorem T27 (no descent to $\mathcal C$).** $\tau^{(\ell)}$ is a function on
(an interval parameterizing) $\mathscr H_i$, a curve in the configuration
manifold. The adjoint evaluation has type
$\Sigma_i:\mathscr H_i\times\mathcal C_i\to\mathcal E_i$ with
$\varpi_i\circ\Sigma_i(r,c)=c$, so $\mathcal C_i$ occupies the *second* slot
and is never a domain of $\tau^{(\ell)}$. The pointwise clocks of
`eq:hist-pointwise-clock-speed` form a **family** $\{\tau_{i,c}\}_{c\in\mathcal C_i}$
indexed by context, not a single function of context, and the members
disagree.

**Witness W-4 (context-dependent disagreement).** Let $\mathcal C_i$ be an
open interval and let a section history change the belief only on a
neighborhood of $c_1$, being constant near $c_2$: for instance $q_i(\lambda)(c)
=\mathcal N(\lambda\,\psi(c),1)$ with $\psi$ a bump function supported near
$c_1$. Then $\tau_{i,c_1}>0$ while $\tau_{i,c_2}\equiv0$ on the same history.
A fortiori the finite-design clock of `eq:hist-finite-design-clock-speed`
assigns zero speed to any section variation vanishing on the design $D$, which
is the radical witness already recorded at
`05d_relational_inference.tex:485-489`.

**Theorem T28 (no clock potential in general).** Even on one configuration
manifold, the orbitwise clocks assemble into a global scalar $T$ with
$dT=\alpha_F$ only when $\alpha_F=-d\mathcal F_i/N$ is exact, that is closed
with vanishing periods (`thm:hist-global-clock-exactness`,
`05d_relational_inference.tex:554-581`), and the local obstruction is
$d\alpha_F=N^{-2}\,dN\wedge d\mathcal F_i$. The manuscript's witness
$\mathcal F=xy$ on the open first quadrant gives
$d\alpha_F=\frac{x^2-y^2}{(x^2+y^2)^{3/2}}dx\wedge dy\ne0$ on every open set.

**Summary of the four relativities of $\tau$.** Duration is relative to
(i) the chosen orbit, (ii) the chosen origin, (iii) the declared configuration
metric (T23), and (iv) the level $\ell$. It is invariant only under
orientation-preserving reparameterization (T22). No operational bridge to a
clock reading is declared anywhere in the current sources, and the contract
lists such an identification as a *separate modeling postulate outside the
theorem target* (`problem-contract.json`, `modeling_postulates[1]`). The
identification is therefore not merely unproved but out of scope.

---

## 7. Attack register against the current manuscript

Each attack states the target reading, the disposition, the artifact bytes it
was run against, and the falsifier that would reverse the disposition.

| ID | Attack | Disposition | Basis | Falsifier of this disposition |
|---|---|---|---|---|
| A-1 | Curve taxonomy is stated at interval scope and is not a partition; the stationary case is absorbed | **SUSTAINED (minor)** | `05d:42-63` | a pointwise trichotomy plus stationary case appears in the definition |
| A-2 | A base curve is called horizontal, or $\dot\gamma$ is split into vertical and horizontal parts | **REJECTED** | `02_geometry.tex:298,363`; `05c:559-564,624`; `SPEC.md:179`; `appendix_notation.tex:377-384` | any occurrence of "horizontal base curve" or a $VE\oplus H$ split of a base velocity |
| A-3 | (SC) is written with no regularity on $a_\ell$, then $a_\ell$ is integrated along an orbit | **SUSTAINED** | `05d:723-751` | $a_\ell$ declared continuous, or L-1 cited |
| A-4 | The flow-semiconjugacy proof presupposes that $\bar\Phi_{\sigma_Q(t)}$ is defined | **SUSTAINED** | `05d:744-751` | the proof builds the time-changed curve first and concludes the domain inclusion from maximality |
| A-5 | The positive factor is omitted, so orbit-set agreement is read as history agreement | **REJECTED** | `05d:726-731`; route-C eq. (7.1); `SPEC.md:624` | any statement of the criterion without $a_\ell>0$ |
| A-6 | Semiconjugacy is read as implying noncollapse; "noncritical domain" does not say for which field | **SUSTAINED (principal)** | `05d:723-762` | the hypothesis reads "$X_{\ell+1}$ nonvanishing on $\hat R_\ell(U)$" and T12 is present |
| A-7 | Maximal-interval bookkeeping is absent, so "the coarse history is the fine history" overreaches | **SUSTAINED** | `05d:723-762` | the inclusion $\Sigma_Q\subseteq\bar J^{\max}$ and condition N3 are stated |
| A-8 | Fiberwise Markov Fisher contraction is read as comparing configuration durations | **REJECTED for the current sources, SUSTAINED as a missing witness** | `05c:832-842`; `05d:753-762`; `06:201-212`; `08:505-527`; `appendix_claim_ledger:147-154` all fence it correctly, but no counterexample is attached | attaching CE-DURATION-MISMATCH and CE-D3 closes the gap; any unfenced duration comparison reopens the attack |
| A-9 | Pushed fine paths are conflated with independently optimized coarse histories | **REJECTED** | `05d:611-626` types `eq:hist-same-path-markov-image` as a HYPOTHESIS and says it "does not define a separately optimized record trajectory"; `fig:hist-markov-clock-and-semiconjugacy` separates the two arrows | any theorem applying `thm:hist-record-clock-contraction` to an independently recomputed flow |
| A-10 | RG depth is equated with duration | **REJECTED** | `05d:764-794`; `07_general_renormalization.tex:42`; `09_coarsegraining.tex:597-599`; `appendix_notation.tex:377-384`; `08:539-543` | any statement treating $\ell$ as a clock reading |
| A-11 | The levelwise duration $\tau^{(\ell)}$ is never defined, so the three-coordinate discipline of plan Step 6 is only two-thirds implemented | **SUSTAINED** | `05d:360-376` vs `:764-786` | $\tau^{(\ell)}(r)$ defined and used |
| A-12 | Writing $Q^{(\ell)}(r)$ and $Q^{(\ell+1)}(r)$ at equal $r$ smuggles a cross-level simultaneity | **SUSTAINED (notational)** | `05d:776-786` | a sentence saying $r$ at level $\ell+1$ is the transported fine parameter, related to the coarse flow parameter by $\sigma_Q$ |
| A-13 | The bundled `main.pdf` is presented as a build of the current sources | **SUSTAINED (provenance)** | D-2 of Section 0.3 | a fresh build whose hash differs from `83b1d9b9…` |
| A-14 | Route-C evidence line anchors resolve against the current ledger | **SUSTAINED (provenance)** | D-4 of Section 0.4 | anchors re-resolved at digest `53d9a2ae…` |

**Time smuggling: overall verdict.** No instance of an external time variable,
a primitive clock, a base-curve motion, or an identification of $\ell$ or $r$
with physical time was found in the current sources. The five defended
statements A-2, A-5, A-8, A-9, A-10 are the load-bearing ones and all hold.
The sustained findings are of three kinds: a definitional imprecision (A-1),
proof-level gaps in one proposition (A-3, A-4, A-6, A-7), and missing
notation, witnesses, and provenance (A-11 through A-14). None of them
requires retracting a theorem; each is closed by the corresponding repair.

---

## 8. Minimal repairs, consolidated

| ID | Target | Repair | Cost |
|---|---|---|---|
| R-1 | `def:hist-curve-types`, `05d:42-63` | pointwise trichotomy plus stationary case (T1); interval labels defined from it | one paragraph |
| R-2 | `prop:hist-oriented-semiconjugacy`, `05d:723-731` | declare $a_\ell$ continuous; add L-1 (uniqueness, automatic smoothness, and undeterminacy at coarse-critical images) | one lemma |
| R-3 | proof at `05d:744-751` | reorder the argument as in T8; state $\Sigma_Q\subseteq\bar J^{\max}$ | three lines |
| R-4 | `prop:hist-oriented-semiconjugacy` hypothesis | read "noncritical" as $X_{\ell+1}\ne0$ on $\hat R_\ell(U)$; add T12 dichotomy and T12b transversality form; cite CE-HISTORY-COLLAPSE | one proposition plus one counterexample |
| R-5 | `05d:753-759` | attach CE-DURATION-MISMATCH and CE-D3 to "Either condition without the other is insufficient" | two counterexamples |
| R-6 | `def:hist-fisher-clock`, `05d:360-376` | introduce $\tau^{(\ell)}(r)$ (D-TAU) so that all three coordinates carry their indices | notation only |
| R-7 | `appendix_claim_ledger.tex:235-241` | add metric relativity (T23) to the physical-time obligation list | one sentence |
| R-8 | `05d:423-425` | split into strict monotonicity (T24.2) and regular coordinate (T24.3); cite the isolated-zero witness W-2 | two sentences |
| R-9 | `eq:hist-levelwise-same-path-image`, `05d:776-786` | say that equal $r$ across levels is the image parameterization, not a synchronization (T26.3, T7a) | one sentence |
| R-10 | `05c:832-842`, `05d:753-762`, `appendix_claim_ledger:147-154` | replace the bare `OPEN` by obligation **O-SC** of Section 5.4, which names $\chi_\ell$, the attaining set, and horizontal conformality | one paragraph |
| R-11 | Chapter 5d, new results | add T19 and T20 as the sufficient-condition theorems; they are three-line proofs and they convert the OPEN from "prove a dynamical identity" into "declare a functional compatibility and check a rank-one condition" | two theorems |
| R-12 | provenance | rebuild `main.pdf` from the current sources before any visual audit; re-resolve route-C line anchors at ledger digest `53d9a2ae…` | mechanical |

---

## 9. Classification of every in-scope Task 10 claim

**Legend.** *PROVED* means a complete derivation is present in this document
or is cited to a completed derivation in the current sources with its
hypotheses checked. *REFUTED* means a scope-matched counterexample against the
stated universal reading is given here. *OPEN* means neither; the exact
missing obligation is named. Claims marked "inherited" are certified
elsewhere in this run and are not re-derived here; this route checks only
their interface.

| Ledger claim | Plan step | Route-D disposition | Basis / exact missing obligation |
|---|---|---|---|
| `score-action-compatibility` | 10.1 | **PROVED (inherited)** | Certified by the Task 7 and Task 9 score/DQM route; this route uses only the score-projection consequence, which is `thm:cg-fisher-contraction`, `06:190-199`. No route-D obligation. |
| `bundle-fisher-defect` | 10.2 | **PROVED (inherited, interface checked)** | `eq:pb-fisher-defect-positive` and `eq:pb-fisher-defect-score-variance`, `05c:687-720`. Route D uses it only inside T16; the hypotheses used are parameter independence, normalization, and the vertical tangent typing, all present. |
| `bundle-morphism-descent` | 10.2 | **PROVED (inherited)** | `07_general_renormalization.tex:180-195` supplies the intertwining condition `eq:rg-cross-intertwiner`; not exercised further by route D. |
| `bundle-scale-cocycle` | 10.2 | **PROVED (inherited)** | Route-C equations (1.1)–(1.3); route D adds the independent multiplicative scale cocycle T11 for the semiconjugacy factor, which is a *new* component of the same functoriality statement. |
| `horizontal-defect-anomaly` | 10.2 | **PROVED** | `thm:pb-covariant-jet-naturality`, `05c:604-631`, retains $(\mathcal D\Psi)_{s(c)}$ exactly; CE-HORIZONTAL-ANOMALY in the register is the matched witness. Route D confirms the type but adds nothing. |
| `pullback-compatibility` | 10.2–10.3 | **PROVED** | `thm:pb-pullback-fisher-defect` with $\mathcal D\Psi=0$ and `eq:pb-coarse-related-sections`, `05c:687-720`. Contravariance and the no-pushforward caveat at `05c:751-756` are correct. |
| `configuration-fisher-metric` | 10.3 | **PROVED, with a strengthening** | `05d:458-536` declares base measure, design weights, channel weights, gauge quotient, finiteness, and the infinite-dimensional submersion caveat. Route D adds T16 (the exact configuration-level defect identity) and T23 (metric relativity), both of which the claim's falsifier list should absorb. |
| `configuration-map` | 10.3 | **PROVED (typing) / OPEN (existence)** | The typing is separated at `07b` and route-C Section 7. **Missing obligation:** existence of a smooth $\hat R_\ell:\mathcal Q_\ell\to\mathcal Q_{\ell+1}$ for the manuscript's declared RG steps; route D assumes it (H-D2) and does not construct it. |
| `configuration-projectability` | 10.3 | **PROVED as a negative** | CE-SECTION-DESCENT ($S^1$ collapsed to a point, identity fiber map, $Q(x)=\sin x$) refutes automatic descent; the hypothesis `eq:pb-coarse-related-sections`, `05c:584-593`, is correctly declared as a HYPOTHESIS with the constancy-on-fibers obligation named. |
| **typed-curve taxonomy** (plan step 10.4; **no ledger claim exists**) | 10.4 | **PROVED here** | T1–T7 and W-1. **Ledger gap:** plan Task 10 Step 4 has no atomic ledger entry. Recommend adding `curve-typing` with falsifier "a curve label applied at interval scope where the pointwise type varies, or a verticality/horizontality predicate applied to a base curve". |
| `history-semiconjugacy` | 10.5 | **PROVED (sufficiency and converse), with hypotheses strengthened** | T8 (sufficiency, with the domain inclusion), T9 (converse on regular orbit arcs), T10 and CE-D2 (the positive factor is not free), T11 (composition). **Missing obligation for the manuscript's own RG maps:** O-SC of Section 5.4. |
| `history-noncollapse` | 10.5 | **PROVED, and the stated universal reading of the semiconjugacy conclusion is REFUTED** | T12 dichotomy, T12a, T12b, CE-HISTORY-COLLAPSE (certified here, promoted from CANDIDATE), N0–N5 table, T13, and T19(3). The refutation is scope-matched: it refutes "(SC) with $a>0$ implies a nonconstant shared history", not the flow identity (FSC), which remains true. |
| `history-duration-relation` | 10.6 | **PROVED, and the fiberwise-contraction reading is REFUTED** | T14 (factor invisibility), T15 (agreement, constant factor, ordering), T16 (when contraction does lift, with the exact defect), T17, CE-DURATION-MISMATCH (certified here, promoted from CANDIDATE, in two independent realizations), CE-D3. |
| **natural-gradient semiconjugacy sufficiency** (plan step 10.5; **no ledger claim exists**) | 10.5 | **PROVED here** | T18, CE-D4, T19, T20, T21, P-1, P-2. **Ledger gap:** recommend adding `natural-gradient-semiconjugacy` with falsifier "a claimed gradient intertwining from equality of objectives alone, or from a submersion without a metric-compatibility hypothesis". |
| **three-coordinate independence** (plan step 10.6; currently only the *assumption* `H-HISTORY`) | 10.6 | **PROVED here (mathematical part); the physical part remains a declared refusal** | T7, T7a, T22, T23, T24, T25, T26, T27, T28, W-1 through W-4. **Ledger recommendation:** split `H-HISTORY` into a theorem `coordinate-independence` (provable, and proved here) and a residual declared refusal covering only the physical-time identification. As written, a provable statement is carried as an assumption. |
| `pullback-ledger-provenance` | 10.7 | **OPEN** | **Missing obligation:** the bundled `main.pdf` at the base revision is byte-identical to the 2026-08-01 build (D-2) and therefore is not a build of the current sources; and the route-C line anchors do not resolve against the current ledger (D-4). Both must be regenerated before this claim can close. |
| `minor-emergent-time-keyword` | 11.7 (depends on `history-duration-relation`) | **OPEN** | **Missing obligation:** a metadata scan of a *freshly built* PDF. The current `main.pdf` predates the repairs, so a scan of it is not evidence about the released metadata. |

**Ledger-structure findings.** Three of the six substantive Task 10
obligations in the plan — typed curves (Step 4), natural-gradient
semiconjugacy sufficiency (Step 5), and three-coordinate independence
(Step 6) — have **no atomic claim** in `claim-ledger.json`. The
dependency DAG at lines 27–37 lists eleven Task 10 edges from `target`, none
of which covers them. Under the proof-obligation rule that a compound target
must atomize each conjunct before certification, this is a coverage gap in the
ledger, not merely in the manuscript. It is reported here rather than
repaired, because this route may create only its own evidence file.

---

## 10. Proposed counterexample-register entries

Existing entries `CE-HISTORY-COLLAPSE` and `CE-DURATION-MISMATCH` are
certified above and should move from `CANDIDATE` to `EVIDENCE_VERIFIED` with
this artifact as their evidence link. Four new entries are proposed.

| ID | Target claim if the hypothesis is dropped | Witness | Lesson |
|---|---|---|---|
| `CE-ORIENTATION-REVERSAL` | `history-semiconjugacy` if the factor is only required nonzero | $\mathcal Q=\mathbb R$, $\mathcal F_\ell=x^2/2$, $\mathcal F_{\ell+1}=-y^2/2$, $\hat R(x)=-x$: orbit sets agree, $a\equiv-1$, coarse descent becomes ascent | orbit-set agreement carries no orientation; $a_\ell>0$ is the whole orientation content |
| `CE-PARTIAL-TRAVERSAL` | `history-semiconjugacy` if "the coarse history is the fine history" is asserted without a maximal-interval hypothesis | $X_f=\partial_x$, $X_m=\partial_y$, $\hat R=\arctan$, $a=(1+x^2)^{-1}>0$: both flows complete, $\Sigma_0=(-\pi/2,\pi/2)\subsetneq\mathbb R$ | completeness does not transfer without $\inf a_\ell>0$; only $\Sigma_Q\subseteq\bar J^{\max}$ is free |
| `CE-INDEPENDENT-ORBIT` | `history-duration-relation` if Markov contraction is read as comparing independently recomputed flows | $\hat R=\operatorname{id}$ on $\mathbb R^2$, $\Delta_F\equiv0$, $\mathcal F_\ell=\tfrac12(x^2+y^2)$, $\mathcal F_{\ell+1}=\tfrac12(x^2+4y^2)$: contraction is an equality yet the two histories are different curves with different durations, and (SC) fails | zero information loss plus compatible metrics still compares nothing without (SC) |
| `CE-EQUAL-OBJECTIVE` | natural-gradient semiconjugacy inferred from equality of objectives | $\hat R=\operatorname{id}$ on $\mathbb R^2$, one objective $\tfrac12(x^2+2y^2)$, metrics $\operatorname{diag}(1,1)$ and $\operatorname{diag}(1,\kappa)$, $\kappa\ne1$: (SC) fails on a dense open set | the gradient is metric-dependent; only $d\mathcal F$ is metric-free |

---

## 11. Independent reconstruction, oracle erasure, and residual obligations

### 11.1 Independent reconstruction record

**Covered claims.** `history-semiconjugacy`, `history-noncollapse`,
`history-duration-relation`, `configuration-fisher-metric` (interface),
`pullback-compatibility` (interface), `pullback-ledger-provenance`, plus the
three unledgered obligations of Section 9.

**Method.** Every theorem in Sections 1 through 6 was derived from H-D1
through H-D3 and standard results with hypotheses mapped explicitly:
Picard-Lindelof existence, uniqueness, and maximality for locally Lipschitz
fields on Banach manifolds (T8, T12); the one-dimensional inverse function
theorem (T24); Lebesgue differentiation (T15); the Ehresmann splitting
$TE=VE\oplus H^\omega E$ (T1, T2); naturality of the gradient under a metric
pushforward (T18); and the Fisher score-projection theorem, which is used only
where the manuscript already cites it (T16). No step imports a manuscript
proof. Three manuscript results were re-derived from scratch and agree:
`prop:hist-horizontal-connection-dependence` (generalized to T2),
`eq:hist-pointwise-history-verticality` (T5), and
`thm:hist-fisher-clock-invariance` (T22).

**Discrepancies found and resolved.** Four, all recorded as sustained attacks
A-1, A-3, A-4, A-6, plus the provenance items A-13, A-14. None is a
contradiction with a manuscript theorem; each is a missing hypothesis, a
proof-order defect, or a missing witness.

**Result.** PASS with the six sustained findings above and the three ledger
coverage gaps of Section 9.

### 11.2 Oracle erasure

The affirmative-existence request is a search prior only. It does not appear
in any hypothesis, derivation, counterexample, disposition, or repair above.
Recomputing the dispositions with the prior removed changes nothing, because:

- every *positive* result (T1–T28, P-1, P-2) is a derivation from H-D1 through
  H-D3 with no existence assumption about the manuscript's RG maps; H-D2
  assumes $\hat R_\ell$ and $X_\ell$ *as data*, which is the contract's own
  `H-CONFIG`, not an affirmative conclusion;
- every *negative* result (CE-HISTORY-COLLAPSE, CE-DURATION-MISMATCH, CE-D1
  through CE-D4) is an explicit finite-dimensional witness that would be
  constructed identically under a negative prior;
- the two claims this route leaves OPEN (`configuration-map` existence,
  `pullback-ledger-provenance`) are left open *against* the prior, which is
  the direction erasure is designed to detect.

A paraphrase scan of this artifact for affirmative-existence language found no
occurrence in assumptions, evidence scopes, claim statements, dependency
roles, or dispositions.

### 11.3 Residual obligations, exactly stated

1. **O-SC.** For the manuscript's declared configuration coarse maps: exhibit
   $\chi_\ell$ with $\chi_\ell'>0$ and an open $U$ containing the fine orbit on
   which (FC) holds; for the exact-RG contracted functional this means proving
   $\mathcal O\subseteq\operatorname{int}\mathcal A_\ell$ (P-2). Then verify the
   rank-one condition of T20, for which horizontal conformality of $\hat R_\ell$
   with dilation $\varphi_\ell\in(0,1]$ (P-1(2)) is sufficient. Until then
   `history-semiconjugacy` holds as a *criterion* and not as a fact about the
   manuscript's flows.
2. **O-CONFIG.** Construct the smooth configuration coarse map itself; route D
   assumes it. Its projectability obligation is already fenced by
   CE-SECTION-DESCENT.
3. **O-QUOTIENT.** In the Fisher-null regime, discharge the four separate
   quotient obligations (constant rank, involutivity, regular Hausdorff leaf
   space, basicness) before any duration coordinate is asserted there; the
   contact witness `prop:pb-contact-null-counterexample` shows involutivity can
   fail at constant rank.
4. **O-INFDIM.** In an infinite-dimensional configuration tier, N5 (closed
   complemented $\ker T\hat R_\ell$) and the strong-metric hypothesis are used
   in T19 and T21 and must be declared; the manuscript already flags the
   analogous gauge-quotient issue at `05d:529-536`.
5. **O-PROVENANCE.** Rebuild `main.pdf` from the current sources and
   re-resolve the route-C ledger anchors before `pullback-ledger-provenance`
   or `minor-emergent-time-keyword` can close.
6. **O-LEDGER.** Add atomic claims for typed curves, natural-gradient
   semiconjugacy sufficiency, and three-coordinate independence, and split
   `H-HISTORY` into its provable mathematical part and its residual physical
   refusal.

### 11.4 Scope and limitations

- **Theorems.** T1–T28, L-1, P-1, P-2 are proved above under H-D1 through
  H-D3 and the hypotheses stated in each statement. They are statements about
  declared configuration manifolds, metrics, and vector fields; they are not
  statements that the manuscript's RG steps satisfy those hypotheses.
- **Constructions.** D-SC, D-FC, and D-TAU are typed definitions; nothing is
  proved by declaring them.
- **Counterexamples.** CE-HISTORY-COLLAPSE, CE-DURATION-MISMATCH, CE-D1
  through CE-D4 refute the stated universal readings and nothing broader. In
  particular CE-HISTORY-COLLAPSE does not refute the flow identity (FSC),
  which remains true in the collapsing case; it refutes the history
  identification only.
- **Modeling postulates.** None is introduced here.
- **Operational identifications.** None is made. Every duration statement is a
  statement about Riemannian arc length on a declared metric.
- **Physical interpretation.** None. T23 and T27 are the internal reasons why
  a physical reading would additionally need a calibration bridge, and the
  contract places that bridge outside the theorem target.
- **Numerical observations.** None; no computation was run and none would
  close any statement above.
- **Provenance.** D-1 through D-4 are mechanical hash and line comparisons.
  They establish drift; they establish nothing mathematical.
