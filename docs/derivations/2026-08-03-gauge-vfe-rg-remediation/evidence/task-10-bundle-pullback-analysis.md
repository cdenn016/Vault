<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 10 independent differential-geometric route: bundle descent, covariant vertical jets, horizontal defect, and section projectability

## 0. Provenance binding

**Base revision.** Commit `02d5d8f542cba2d92c6a430483b62155dd5f2db4` (`docs: derive
RG modes beta functions and fixed objects`) on branch
`codex/gauge-vfe-rg-task10-pullbacks-20260804`, working tree clean at the start
of this pass. This pass ran no Git mutation, no TeX build, and no numerical
program. It created exactly one file, this one. It read but did not modify every
path listed below.

**SHA-256 of every source read and used by this pass**, computed from the bytes
on disk at the base revision:

| Path | SHA-256 |
| --- | --- |
| `manuscripts/gauge_vfe_rg/SPEC.md` | `3557038B57F008A1453F29F3ABAA2B8C7DDEA822BC610DD6945ADC811B97BF2D` |
| `docs/superpowers/plans/2026-08-03-gauge-vfe-rg-review-remediation.md` | `9E3D0C64B81A27782729E62F9485FF17EEA9E687D79CBDEA7B7BED69E94BB36C` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/problem-contract.json` | `7CBA2E9BBFE34028D6A994359E53C761779BD255C5405BFA3996C50CA575BC22` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/claim-ledger.json` | `53D9A2AE2CEAB6A20C0486FACC68E07BFB66731EBDCCDFCC7C87F9890357C5F7` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/dependency-dag.json` | `BB296DA12424FDD766727F0236AA6B91B1CB8FCFB93E3016882532049A119C16` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/counterexample-register.md` | `C7E0FA8D576AB60C2D4060F423E4222E800116A0293E0097C8D38AB55E6B6853` |
| `manuscripts/gauge_vfe_rg/02_geometry.tex` | `C3657CF5A1B2A9C99471F1FCAE922135E6C934E3EC7308A927C42AB91D510F08` |
| `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex` | `A87BC2B3D7D8D76412A299FBD3220464802BD1CC2D853F1F6C287F96E5A73279` |
| `manuscripts/gauge_vfe_rg/05d_relational_inference.tex` | `138E4F86F107F5BD0307E049DC5368A6C36584A827BF98BF4EB396E30016D0A1` |
| `manuscripts/gauge_vfe_rg/06_general_coarsegraining.tex` | `A6A60A19A7C263915E749787B12470A84D6FAFCAF9D55C69B71C0490C45C064A` |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `A3A7AE2FED2EB4A1EA4668393A69B4D56AA2C9DD071AF06DDBCBA717D7365797` |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `148D9652229EB6D3C40A41B48C1EB938328CA697A37E8113111567C580CC61BE` |
| `manuscripts/gauge_vfe_rg/08_infogeometry.tex` | `55BFCDFF0EEBEC24F2231852467255D13A0C02D1369621D04EDE53CAD3B7C31B` |
| `manuscripts/gauge_vfe_rg/appendix_notation.tex` | `D39936499C9673C1B4ED75AE31BF294F8D4DF9FD1FD0CEF1DAE4A9EC5A572FA4` |
| `manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex` | `BBB02A24ED0875FF287AA072FDDAE359F4CCD59058157503D4E93502A4E6B436` |
| `sources/manuscripts/gauge-vfe-rg-pullback-geometry-2026-08-01.md` | `E9CB6E4CD360EE477F60459856A33FD76B1F7D17B32F65F7A1DEE61345318C68` |
| `sources/refs/kobayashi-nomizu-1963-foundations.md` | `F3659F9C8ACD576867B005A424D9044F7350C9BCE98D5CFC00A68EC1ECAC8ACD` |
| `sources/refs/ay-2017-information-geometry.md` | `659B3901EB2E0E5AE0DD04E30DDC6826F2372430E3ECF131428AD0C9288AEC32` |
| `sources/refs/cencov-1982-statistical-decision-rules.md` | `CD5D8C51DEBA6840E008FCEA58759AA9BE1F12FD2842EC21371FF985F1E75F66` |

The immutable note `sources/manuscripts/gauge-vfe-rg-pullback-geometry-2026-08-01.md`
was read **only as a stale prior construction to attack**. It is nowhere treated
as authority in this record. Section 10.2 records the two places where its prose
is refuted or narrowed by the constructions below.

**Reference-note scope.** The three `sources/refs/*` notes were opened only to
confirm which primary monograph carries each external theorem. No mathematical
step below rests on their vault prose, and Section 12 records one place where a
framing sentence in `cencov-1982-statistical-decision-rules.md` is explicitly
**not** used. Every external theorem invoked is named with its standard statement
in Section 12 so that an independent reconstructor can check it against the
primary monographs rather than against this vault.

## 1. Scope

This record covers the differential-geometric conjuncts of Task 10 that the plan
assigns to `05c_pullback_geometry.tex`, `05d_relational_inference.tex`,
`07_general_renormalization.tex`, and `08_infogeometry.tex`, and it discharges
the six items of the commissioning brief. The claim-ledger identifiers in scope
are

`bundle-morphism-descent`, `bundle-fisher-defect`, `bundle-scale-cocycle`,
`horizontal-defect-anomaly`, `pullback-compatibility`, `configuration-map`,
`configuration-projectability`, `configuration-fisher-metric`.

Out of scope and not adjudicated here: `score-action-compatibility` (an
action-quotient/probability claim, not a bundle claim), and the three history
claims `history-semiconjugacy`, `history-noncollapse`, `history-duration-relation`,
which belong to the dynamical-systems route. Where a bundle result bounds one of
those, the bound is stated and labeled as a bound, not as a disposition.

The affirmative-existence instruction attached to the commissioning brief is a
search prior. It allocated effort to this route. It appears in no premise, no
assumption, no proof step, no evidence line, and no disposition below. Section 13
records the erasure check.

Every result is given as: **types**, **quantifiers**, **assumptions**, **proof**,
**falsification condition**, **source anchors needing repair**.

## 2. Typed foundations

### 2.1 Standing objects

Fix throughout, for one channel at a time (the two-channel version is Section 7):

* **Bases.** $\mathcal C$, $\bar{\mathcal C}$ finite-dimensional smooth,
  second-countable, Hausdorff manifolds; $f\in C^\infty(\mathcal C,\bar{\mathcal C})$.
* **Groups.** Lie groups $G$, $\bar G$; a Lie-group homomorphism
  $\kappa:G\to\bar G$ with differential $d\kappa:\mathfrak g\to\bar{\mathfrak g}$.
* **Principal bundles.** $\pi:P\to\mathcal C$ principal right $G$-bundle;
  $\bar\pi:\bar P\to\bar{\mathcal C}$ principal right $\bar G$-bundle.
* **Principal scale map.** $\mathcal P\in C^\infty(P,\bar P)$ with
  $\bar\pi\circ\mathcal P=f\circ\pi$ and
  $\mathcal P(p\cdot g)=\mathcal P(p)\cdot\kappa(g)$ for all $p\in P$, $g\in G$.
* **Sample spaces.** $(\mathsf K,\mathscr K)$, $(\bar{\mathsf K},\bar{\mathscr K})$
  standard Borel.
* **Represented sample actions.** $\rho:G\to\operatorname{Aut}(\mathsf K)$ and
  $\bar\rho:\bar G\to\operatorname{Aut}(\bar{\mathsf K})$ by bimeasurable
  bijections, with induced law actions
  $\widehat\rho(g)\beta=\rho(g)_\#\beta$, $\widehat{\bar\rho}(\bar g)\bar\beta=\bar\rho(\bar g)_\#\bar\beta$.
* **Law fibers.** $\mathcal B\subseteq\mathcal P(\mathsf K)$ and
  $\bar{\mathcal B}\subseteq\mathcal P(\bar{\mathsf K})$, each a smooth
  finite-dimensional parametrized-measure model in the sense of
  `hyp:geo-smooth-tier` and `hyp:pb-regular-models`, each invariant under its
  represented action, each differentiable in quadratic mean with
  square-integrable scores and positive-definite Fisher form $g^F$, $\bar g^F$.
* **Associated bundles.** $E=P\times_{\widehat\rho}\mathcal B$,
  $\bar E=\bar P\times_{\widehat{\bar\rho}}\bar{\mathcal B}$, with the manuscript's
  quotient convention `eq:geo-quotient-convention`, $[u\cdot g,\beta]=[u,\widehat\rho(g)\beta]$;
  projections $\varpi$, $\bar\varpi$; vertical bundles $VE=\ker T\varpi$,
  $V\bar E=\ker T\bar\varpi$.
* **Connections.** Principal connections $\omega\in\Omega^1(P,\mathfrak g)$,
  $\bar\omega\in\Omega^1(\bar P,\bar{\mathfrak g})$, with induced Ehresmann
  horizontal distributions $H^\omega\subset TE$, $H^{\bar\omega}\subset T\bar E$
  and vertical projectors $\operatorname{ver}^\omega$, $\operatorname{ver}^{\bar\omega}$.
* **Infinitesimal fiber action.** $\zeta:\mathfrak g\to\mathfrak X(\mathcal B)$,
  $\zeta_\xi(\beta)=\frac{d}{dt}\big|_{0}\widehat\rho(\exp t\xi)\beta$, and
  $\bar\zeta:\bar{\mathfrak g}\to\mathfrak X(\bar{\mathcal B})$ likewise. The
  frame-free version is the fundamental vertical map
  $\vartheta_e:\operatorname{Ad}(P)_{\varpi(e)}\to V_eE$ of
  `eq:pb-connection-difference-vertical`.

### 2.2 The three typed objects that must never be identified

The brief requires that a sample-space Markov kernel, its induced law map, and
the associated-bundle map be kept distinct. They are:

$$
N:\mathsf K\rightsquigarrow\bar{\mathsf K},
\qquad
N_\star:\mathcal P(\mathsf K)\to\mathcal P(\bar{\mathsf K}),
\qquad
\Psi:E\to\bar E .
$$

* $N$ is a map $\mathsf K\times\bar{\mathscr K}\to[0,1]$, a probability measure in
  its second argument and measurable in its first, with $N(x,\bar{\mathsf K})=1$.
* $N_\star$ is the affine map $(N_\star\beta)(B)=\int_{\mathsf K}N(x,B)\,\beta(dx)$.
  Its restriction $q:=N_\star|_{\mathcal B}$ is the **law-fiber map**; it exists
  as a map into $\bar{\mathcal B}$ only under the **family-closure** hypothesis
  $N_\star(\mathcal B)\subseteq\bar{\mathcal B}$.
* $\Psi$ is a smooth fiber-preserving map covering $f$, i.e.
  $\bar\varpi\circ\Psi=f\circ\varpi$.

**Lemma 2.1 (strictness of the three types).**
(i) $N$ determines $N_\star$ and hence $q$; the converse fails.
(ii) Sample-level $\kappa$-equivariance of $N$, namely
$N(\rho(g)x,B)=N(x,\bar\rho(\kappa g)^{-1}B)$ for all $g,x,B$, implies the
law-level intertwining relation
$q\circ\widehat\rho(g)=\widehat{\bar\rho}(\kappa g)\circ q$ on $\mathcal B$; the
converse fails.
(iii) $\Psi$ does not determine $q$ unless the represented action is free on the
relevant fiber orbits, and never determines $N$.

*Proof.* (ii) forward: for $B\in\bar{\mathscr K}$,
$(N_\star\widehat\rho(g)\beta)(B)=\int N(y,B)(\rho(g)_\#\beta)(dy)=\int N(\rho(g)x,B)\beta(dx)=\int N(x,\bar\rho(\kappa g)^{-1}B)\beta(dx)=(\widehat{\bar\rho}(\kappa g)N_\star\beta)(B)$.

(i) and (ii) converse, one witness for both: $\mathsf K=\mathbb R^2$,
$\bar{\mathsf K}=\mathbb R$, $G=SO(2)$ acting by rotation, $\bar G=\{e\}$,
$\kappa$ trivial, $\mathcal B=\{\mathcal N(0,\sigma^2I_2):\sigma>0\}$. The action
fixes every point of $\mathcal B$, so the law-level intertwining relation holds
for every kernel whatsoever. Take $N_1(x,\cdot)=\delta_{x_1}$,
$N_2(x,\cdot)=\delta_{x_2}$, $N_3(x,\cdot)=\delta_{(x_1+x_2)/\sqrt2}$. All three
push $\mathcal N(0,\sigma^2I_2)$ to $\mathcal N(0,\sigma^2)$, so
$q_1=q_2=q_3$ on $\mathcal B$ while $N_1\ne N_2\ne N_3$ as kernels; and none of
them is $SO(2)$-equivariant as a kernel, although each satisfies the law-level
relation. (iii) follows because $\Psi[u,\beta]=[\mathcal P(u),q(\beta)]$
determines $q(\beta)$ only up to the isotropy group of the point in
$\bar{\mathcal B}$, and because $q$ determines $N$ only under (i). $\square$

**Consequence used repeatedly below.** The Fisher-monotonicity input is a
statement about $q$ and the joint law $\beta(dx)N(x,d\bar y)$, not about $\Psi$;
the descent statement is about $\Psi$ and $\mathcal P$, not about $N$; and the
Ehresmann statement is about $\omega,\bar\omega$ and involves neither $N$ nor $q$.

## 3. Result R1 — exact descent of a principal map to an associated-bundle morphism

### R1.1 Statement

**Theorem R1 (descent).** Assume the standing data of Section 2.1, family
closure $N_\star(\mathcal B)\subseteq\bar{\mathcal B}$, and write
$q=N_\star|_{\mathcal B}$. Consider the assignment on representatives

$$
\widetilde\Psi:P\times\mathcal B\longrightarrow\bar E,
\qquad
\widetilde\Psi(u,\beta)=[\mathcal P(u),\,q(\beta)] .
$$

Then:

1. **(Quotient / well-definedness.)** $\widetilde\Psi$ factors through the
   quotient $P\times\mathcal B\twoheadrightarrow E$ **if and only if** the
   law-fiber intertwining relation
   $$
   q\circ\widehat\rho(g)=\widehat{\bar\rho}(\kappa(g))\circ q
   \qquad\text{on }\mathcal B,\text{ for every }g\in G
   \tag{I}
   $$
   holds. The resulting map $\Psi:E\to\bar E$, $\Psi[u,\beta]=[\mathcal P(u),q(\beta)]$,
   then satisfies $\bar\varpi\circ\Psi=f\circ\varpi$.
2. **(Smoothness.)** If in addition $q:\mathcal B\to\bar{\mathcal B}$ is smooth
   as a map of the two declared parametrized-measure models, then $\Psi$ is
   smooth, and $T\Psi$ carries $VE$ into $V\bar E$; write $T^V\Psi$ for the
   restriction.
3. **(Vertical differential in a frame.)** For $u\in P_c$ and $\beta\in\mathcal B$,
   under the identification of $V_{[u,\beta]}E$ with $T_\beta\mathcal B$ supplied
   by $u$ and of $V_{[\mathcal P(u),q\beta]}\bar E$ with $T_{q\beta}\bar{\mathcal B}$
   supplied by $\mathcal P(u)$, one has $T^V\Psi=T_\beta q$.
4. **(Equivariance of the differential.)** Under (I), $T q\circ\zeta_\xi=\bar\zeta_{d\kappa(\xi)}\circ q$
   for every $\xi\in\mathfrak g$.

### R1.2 Types

$f:\mathcal C\to\bar{\mathcal C}$ smooth; $\kappa:G\to\bar G$ Lie-group
homomorphism; $\mathcal P:P\to\bar P$ smooth $\kappa$-equivariant over $f$;
$N:\mathsf K\rightsquigarrow\bar{\mathsf K}$ Markov kernel;
$q=N_\star|_{\mathcal B}:\mathcal B\to\bar{\mathcal B}$ smooth;
$\Psi:E\to\bar E$ smooth bundle morphism over $f$;
$T^V\Psi:VE\to V\bar E$ vector-bundle morphism over $\Psi$.

### R1.3 Quantifiers

For every $u\in P$, every $g\in G$, every $\beta\in\mathcal B$, every $c\in\mathcal C$,
and for both channels $x\in\{b,m\}$ independently.

### R1.4 Assumptions

(A1) $\mathcal P$ is smooth and $\kappa$-equivariant over $f$ — declared data,
not derived. (A2) family closure. (A3) intertwining (I). (A4) smoothness of $q$
between the declared models. (A5) $\mathcal B$ and $\bar{\mathcal B}$ are
invariant under their represented actions.

### R1.5 Proof

*Part 1, sufficiency.* Two representatives of one point of $E$ are exactly
$(u,\beta)$ and $(u g,\widehat\rho(g)^{-1}\beta)$ for $g\in G$, because $G$ acts
freely and transitively on each principal fiber and the equivalence is generated
by $[ug,\beta]=[u,\widehat\rho(g)\beta]$. Then
$$
\widetilde\Psi\big(ug,\widehat\rho(g)^{-1}\beta\big)
=\big[\mathcal P(ug),\,q\widehat\rho(g)^{-1}\beta\big]
=\big[\mathcal P(u)\kappa(g),\,\widehat{\bar\rho}(\kappa(g))^{-1}q\beta\big]
$$
using $\kappa$-equivariance of $\mathcal P$ for the first slot and (I) at $g^{-1}$
for the second, together with $\kappa(g^{-1})=\kappa(g)^{-1}$. Applying the
target quotient convention $[\bar u\bar g,\bar\beta]=[\bar u,\widehat{\bar\rho}(\bar g)\bar\beta]$
with $\bar u=\mathcal P(u)$, $\bar g=\kappa(g)$, $\bar\beta=\widehat{\bar\rho}(\kappa g)^{-1}q\beta$
gives $[\mathcal P(u),q\beta]=\widetilde\Psi(u,\beta)$.

*Part 1, necessity.* Run the same computation without assuming (I):
$$
\widetilde\Psi\big(ug,\widehat\rho(g)^{-1}\beta\big)
=\big[\mathcal P(u),\;\widehat{\bar\rho}(\kappa(g))\,q\,\widehat\rho(g)^{-1}\beta\big].
$$
This equals $[\mathcal P(u),q\beta]$ for all $u$ exactly when
$\widehat{\bar\rho}(\kappa g)\,q\,\widehat\rho(g)^{-1}\beta=q\beta$ for all
$\beta\in\mathcal B$ and $g\in G$, which after the substitution $g\mapsto g^{-1}$
is precisely (I). Hence, **given** an equivariant $\mathcal P$, condition (I) is
necessary as well as sufficient.

*Part 1, projection.* $\bar\varpi\Psi[u,\beta]=\bar\pi(\mathcal P(u))=f(\pi(u))=f(\varpi[u,\beta])$.

*Part 2.* The quotient map $\varkappa:P\times\mathcal B\to E$ is a surjective
smooth submersion, because the $G$-action on $P\times\mathcal B$,
$(u,\beta)\cdot g=(ug,\widehat\rho(g)^{-1}\beta)$, is smooth, free (freeness on
the $P$ factor suffices) and proper (properness of the principal action on $P$).
The composite $\widetilde\Psi=\varkappa_{\bar E}\circ(\mathcal P\times q)$ is
smooth by (A1) and (A4). A smooth map constant on the fibers of a surjective
submersion descends to a unique smooth map on the quotient. Verticality
preservation: if $T\varpi(v)=0$ then $T\bar\varpi(T\Psi v)=Tf(T\varpi v)=0$.

*Part 3.* In the trivialization induced by a local section $u$ of $P$ over
$\mathcal U$ and the local section $\bar u$ of $\bar P$ obtained by any choice
over $f(\mathcal U)$, the fiber identification supplied by $u$ sends
$\beta\mapsto[u(c),\beta]$; by construction $\Psi[u(c),\beta]=[\mathcal P(u(c)),q\beta]$,
so in the pair of frames $(u(c),\mathcal P(u(c)))$ the fiber representative of
$\Psi$ is literally $q$, whence $T^V\Psi=Tq$.

*Part 4.* Differentiate (I) at $g=\exp(t\xi)$, $t=0$, applied to a fixed $\beta$:
$Tq(\zeta_\xi(\beta))=\bar\zeta_{d\kappa(\xi)}(q\beta)$. $\square$

### R1.6 Two scope corrections that the source needs

**(a) The manuscript's necessity phrasing is correct only relative to a declared
equivariant $\mathcal P$.** `07_general_renormalization.tex`
`eq:rg-scale-intertwiner` says a fiber map "descends to a bundle map only if"
the intertwining relation holds. That reading is exactly Theorem R1 part 1
*given* `eq:rg-principal-scale-map`. Detached from that hypothesis it is false:
if $\bar{\mathcal B}$ is a single $\bar G$-fixed point then every $q$ and every
$\mathcal P$ (equivariant or not) give a well-defined $\Psi$, while (I) is
vacuous rather than necessary in any informative sense. The repair is to state
the necessity as a biconditional under the declared $\mathcal P$, and to supply
the two-line quotient computation above, which the manuscript does not give at
either `prop:geo-intertwining-cross-map` or `eq:rg-scale-intertwiner`.

**(b) Family closure and smoothness of $q$ are two unstated hypotheses.** Neither
`eq:rg-scale-intertwiner` nor `sec:pb-fisher-defect` names them.
`sec:pb-fisher-defect` writes "the fiber map underlying $\Psi$ is the pushforward
of a parameter-independent Markov kernel between the two regular statistical
experiments", which presupposes both. Affinity of $N_\star$ on the cone of
measures does **not** give smoothness of $q$ as a map between the declared
parametrized-measure models: smoothness requires that the coarse model be
identifiable enough for $\theta\mapsto N_\star p_\theta$ to factor through a map
of parameters, and that this factorization be smooth. A Markov kernel is a
measure-theoretic object; a smooth map of statistical manifolds is not.

### R1.7 Falsification condition

Exhibit an equivariant $\mathcal P$ over $\kappa$, a $q$ violating (I) at some
$(g,\beta)$, and two representatives $(u,\beta)$, $(ug,\widehat\rho(g)^{-1}\beta)$
of one point of $E$ whose images agree in $\bar E$; or exhibit $q$ satisfying (I)
and family closure for which the descended set map is not smooth **although** $q$
is smooth between the declared models and $\mathcal P$ is smooth. Either refutes
R1.

### R1.8 Source anchors needing repair

`manuscripts/gauge_vfe_rg/07_general_renormalization.tex`
`eq:rg-scale-intertwiner`, `eq:rg-associated-scale-map` (add the biconditional and
the quotient proof; add family closure and smoothness of $q$);
`manuscripts/gauge_vfe_rg/02_geometry.tex` `prop:geo-intertwining-cross-map`
(the proof sentence "The quotient representatives ... have the same image ...
exactly when the corresponding equality holds" asserts the biconditional without
displaying the substitution; supply it);
`manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex` `sec:pb-fisher-defect`
(name family closure and smoothness of the law-fiber map as hypotheses).

## 4. Result R2 — covariant vertical first jet, passive covariance, radical, rank, quotients

### R2.1 The local formula and its exact sign

**Lemma R2.1 (local representative of the covariant vertical jet).** Let
$u:\mathcal U\to P$ be a local principal section, $A=u^*\omega$, and let $s_u$ be
the representative of a section $s$ of $E$, so $s(c)=[u(c),s_u(c)]$. Then
$$
\big(D^\omega s\big)_u(X)
=ds_u(X)+\zeta_{A(X)}\big(s_u(c)\big)
\in T_{s_u(c)}\mathcal B .
\tag{R2.1}
$$
Under a passive reframing $u'=u\cdot a$, $a:\mathcal U\to G$, one has
$s_{u'}=\widehat\rho(a)^{-1}s_u$, $A'=\operatorname{Ad}_{a^{-1}}A+a^{-1}da$, and
$$
\big(D^\omega s\big)_{u'}(X)=T\widehat\rho(a)^{-1}\big[\big(D^\omega s\big)_u(X)\big].
\tag{R2.2}
$$

*Proof.* Write $\Lambda_g=\widehat\rho(g)$ acting on $\mathcal B$ and use the
identity $\zeta_{\operatorname{Ad}_{g^{-1}}\xi}(\Lambda_{g^{-1}}\beta)=T\Lambda_{g^{-1}}\zeta_\xi(\beta)$,
obtained by differentiating
$\Lambda_{g^{-1}}\Lambda_{\exp t\xi}\beta=\Lambda_{\exp(t\operatorname{Ad}_{g^{-1}}\xi)}\Lambda_{g^{-1}}\beta$
at $t=0$. Put $F(c)=\Lambda_{a(c)^{-1}}(s_u(c))$. Differentiating along a curve
with $\dot c_0=X$ and writing $b=a^{-1}$, $b^{-1}\dot b=-\,da(X)a^{-1}$, gives
$$
dF(X)=T\Lambda_{a^{-1}}\Big(ds_u(X)+\zeta_{-\,da(X)a^{-1}}(s_u)\Big).
$$
For the connection term, the identity above gives
$\zeta_{\operatorname{Ad}_{a^{-1}}A(X)}(\Lambda_{a^{-1}}s_u)=T\Lambda_{a^{-1}}\zeta_{A(X)}(s_u)$
and, since $\operatorname{Ad}_{a^{-1}}\big(da(X)a^{-1}\big)=a^{-1}da(X)$,
$\zeta_{a^{-1}da(X)}(\Lambda_{a^{-1}}s_u)=T\Lambda_{a^{-1}}\zeta_{da(X)a^{-1}}(s_u)$.
Adding, the two $da(X)a^{-1}$ contributions cancel and (R2.2) follows. Verifying
that (R2.1) is the vertical part of $Ts$ for the Ehresmann connection induced by
$\omega$ is the same computation read at $a=e$. $\square$

**Two corrections this forces on the source.** First,
`05c_pullback_geometry.tex` fixes its sign by "the local formula
$D_A=d+\widehat\rho_{x*}(A)$" (the paragraph introducing
`eq:pb-connection-difference-vertical`). The symbol $\widehat\rho_{x*}(A)$ is a
*linear* representation of $\mathfrak g$ on a vector space and is not defined for
a nonlinear law fiber $\mathcal B\subseteq\mathcal P(\mathsf K)$; the correct
object is the fundamental vector field $\zeta_{A(X)}$, exactly as the
frame-free `eq:pb-connection-difference-vertical` already uses $\vartheta$. This
is a type defect in the convention sentence, not in the conclusion. Second, with
the corrected object the manuscript's sign is **verified correct**: from (R2.1),
$\omega'=\omega+a$ gives $A'=A+u^*a$ and hence
$D^{\omega'}s=D^\omega s+R_a^s$ with $R_a^s(X)=\vartheta_{s(c)}(a_c(X))$, which is
`eq:pb-jet-connection-change` with the manuscript's stated convention.

### R2.2 Passive covariance is not a theorem about gauge invariants

**Proposition R2.2.** (i) $D^\omega s=\operatorname{ver}^\omega\circ Ts$,
$h^\omega_s=(D^\omega s)^*g^F$, and $c^\omega_s=(D^\omega s)^*\mathcal T$ are
defined without reference to any local frame; consequently their invariance
under passive reframing is a consistency property of the local formulas (R2.1),
(R2.2), not an independent invariance theorem. (ii) These tensors are **not**
invariant under the active gauge group $\mathcal G(P)$ at fixed connection.

*Proof.* (i) Immediate from the definitions, once $g^F$ and $\mathcal T$ descend
to well-defined vertical tensors on $E$; that descent is exactly
`prop:pb-statistical-tensor-descent`, whose proof we verify in R2.3 below.
(ii) Witness. $\mathcal C=\mathbb R$, $G=(\mathbb R,+)$, $P=\mathbb R\times\mathbb R$
trivial, $\mathcal B=\{\mathcal N(\mu,1):\mu\in\mathbb R\}$ with $G$ acting by
$\mu\mapsto\mu+t$, $\omega$ the flat connection $A=0$, and $s$ the section
$\mu\equiv0$. Then $D^\omega s=0$ and $h^\omega_s=0$. The bundle automorphism
$F(u(x)\cdot g)=u(x)\cdot(x+g)$ is an element of $\mathcal G(P)$; it carries $s$
to the section $\mu(x)=x$, for which $D^\omega(F\!\cdot\!s)=dx\otimes\partial_\mu$
and $h^\omega_{F\cdot s}=dx^2\ne0$. $\square$

**Reading.** The manuscript's `thm:pb-pullback-gauge-invariance` transforms the
connection *and* the section together, which is the passive statement, and its
following remark correctly separates passive invariance from connection
independence. What the theorem's title and its `ESTABLISHED` status invite is the
stronger and false reading refuted by R2.2(ii). This is a status and naming
defect, not a mathematical error.

### R2.3 Descent of the statistical tensors — verified

**Lemma R2.3.** Let $\tau$ be a covariant tensor field on $\mathcal B$ invariant
under $\widehat\rho(G)$. Then $\tau$ induces a well-defined vertical tensor field
on $E$, smooth whenever $\tau$ is smooth.

*Proof.* For $u\in P_c$ let $\iota_u:\mathcal B\to E_c$, $\iota_u(\beta)=[u,\beta]$;
this is a diffeomorphism onto the fiber. From the quotient convention,
$\iota_{ug}=\iota_u\circ\widehat\rho(g)$. Setting $\tau^u:=(\iota_u^{-1})^*\tau$
gives $\tau^{ug}=(\iota_u^{-1})^*\big(\widehat\rho(g)^{-1}\big)^*\tau=(\iota_u^{-1})^*\tau=\tau^u$
exactly when $\widehat\rho(g)^*\tau=\tau$. Smoothness follows by using local
sections of $P$. $\square$

This is the content the manuscript's `prop:pb-statistical-tensor-descent` states;
its proof paragraph ends with the single sentence "An invariant tensor on the
fiber descends through the associated-bundle quotient", which is the assertion,
not the argument. The two-line argument above should replace it. The statistical
half of that proof — that a parameter-independent bimeasurable sample
re-coordinatization preserves the second and third score moments — is correct as
written and rests on the Chentsov-type invariance of $g^F$ and $\mathcal T$ under
sufficient statistics.

### R2.4 When the Fisher pullback is a global connection-relative base semimetric

**Theorem R2.4.** Under the standing hypotheses, let $\mathcal U\subseteq\mathcal C$
be open and $s\in\Gamma(\mathcal U,E)$ smooth. Then:

1. $h^\omega_s\in\Gamma(\operatorname{Sym}^2T^*\mathcal U)$ is smooth and positive
   semidefinite, and is defined on exactly the domain of $s$.
2. It is **global** — that is, $\mathcal U=\mathcal C$ is attainable — if and only
   if $E$ admits a global smooth section. This is a topological condition on
   $(P,\rho,\mathcal B)$ and is **not** supplied by the principal bundle. A
   sufficient condition is that $\mathcal B$ be smoothly contractible, since then
   all obstruction groups $H^{k+1}(\mathcal C;\pi_k(\mathcal B))$ with local
   coefficients vanish.
3. $\operatorname{rad}h^\omega_s=\ker D^\omega s$ and
   $\operatorname{rank}h^\omega_s=\operatorname{rank}D^\omega s$ pointwise,
   provided $g^F$ is positive definite on $V_{s(c)}E$.
4. If $D^\omega s$ has constant rank $r$ on $\mathcal U$, then
   $K^\omega_s=\ker D^\omega s$ and $\operatorname{im}D^\omega s$ are smooth
   subbundles, the quotient vector bundle $Q^\omega_s=T\mathcal U/K^\omega_s$
   carries the well-defined positive-definite metric
   $\bar h^\omega_s([X],[Y])=h^\omega_s(X,Y)$, and
   $Q^\omega_s\to\operatorname{im}D^\omega s$ is an isometric vector-bundle
   isomorphism.
5. $\bar h^\omega_s$ is the metric of a **quotient manifold** if and only if, in
   addition, (a) $K^\omega_s$ is involutive, (b) its foliation is simple with a
   smooth Hausdorff leaf space $\varrho:\mathcal U\to\mathcal U/\mathcal F$, and
   (c) $h^\omega_s$ is basic, i.e. $\mathcal L_Zh^\omega_s=0$ for every
   $Z\in\Gamma(K^\omega_s)$. Condition (c) has the equivalent connection-free
   form: choosing any metric connection $\nabla$ on $(s^*VE,g^F)$ and setting
   $\mathcal L_Z(D^\omega s)(X):=\nabla_Z\!\big(D^\omega s\,X\big)-D^\omega s\,[Z,X]$,
   condition (c) holds if and only if
   $$
   g^F\big(\mathcal L_Z(D^\omega s)X,\;D^\omega sY\big)
   +g^F\big(D^\omega sX,\;\mathcal L_Z(D^\omega s)Y\big)=0
   \quad\text{for all }X,Y\text{ and }Z\in\Gamma(K^\omega_s),
   \tag{R2.4}
   $$
   and the left side of (R2.4) does not depend on the choice of metric $\nabla$.

*Proof.* 1 is immediate. 2: sections of $E$ correspond bijectively to
$G$-equivariant maps $P\to\mathcal B$, and a fiber bundle over a smooth
paracompact base with fiber having vanishing homotopy groups admits a section by
the standard obstruction argument. 3: $h^\omega_s$ is positive semidefinite, so
$X\in\operatorname{rad}h^\omega_s\iff h^\omega_s(X,X)=0\iff g^F(D^\omega sX,D^\omega sX)=0\iff D^\omega sX=0$
by positive definiteness of $g^F$; the rank statement follows since
$h^\omega_s=(D^\omega s)^*g^F$ with $g^F$ nondegenerate. 4: $D^\omega s$ is a
smooth vector-bundle morphism $T\mathcal U\to s^*VE$ over $\mathcal U$; a
vector-bundle morphism of locally constant rank has smooth kernel and image
subbundles. Well-definedness of $\bar h^\omega_s$ is 3. 5: for a simple foliation,
$h=\varrho^*\hbar$ for a unique $\hbar$ if and only if $h$ is basic, and basicness
for a symmetric $2$-tensor means $\iota_Zh=0$ and $\mathcal L_Zh=0$; the first
holds by 3. Positive definiteness of $\hbar$ follows because
$\dim(\mathcal U/\mathcal F)=\dim\mathcal U-\operatorname{rank}K=r$ equals
$\operatorname{rank}h$. For the equivalent form, expand
$\mathcal L_Zh(X,Y)=Z\,h(X,Y)-h([Z,X],Y)-h(X,[Z,Y])$ with $h(X,Y)=g^F(D^\omega sX,D^\omega sY)$
and use metricity of $\nabla$ to kill the $(\nabla_Zg^F)$ term; the resulting
expression is exactly the left side of (R2.4). Independence of $\nabla$: two metric
connections differ by a $g^F$-skew endomorphism-valued one-form $\Theta$, and the
induced change in the left side of (R2.4) is
$g^F(\Theta_ZD^\omega sX,D^\omega sY)+g^F(D^\omega sX,\Theta_ZD^\omega sY)=0$. $\square$

**Sharpness witnesses (both already in the source; both verified here).**
* *Rank jump.* $\mathcal C=\mathbb R$, flat connection, $s(x)=\mathcal N(x^2,1)$
  gives $D^\omega s=2x\,dx\otimes\partial_\mu$ and $h_s=4x^2dx^2$, rank one off
  the origin and rank zero at it, so no vector-bundle quotient exists across
  $x=0$. This confirms `eq:pb-rank-jump-example`.
* *Constant rank, nonintegrable radical.* $\mathcal C=\mathbb R^3$, trivial
  translation bundle, $\mathcal B$ the unit-variance normal location family,
  $s\equiv\mathcal N(0,1)$, $A=\alpha=dz-x\,dy$. Then by (R2.1),
  $D^\omega s=\alpha\otimes\partial_\mu$ and, since the Fisher information of the
  location family is $1$, $h^\omega_s=\alpha^2$ of constant rank one, while
  $\alpha\wedge d\alpha=(dz-x\,dy)\wedge(-dx\wedge dy)=-\,dz\wedge dx\wedge dy\ne0$,
  so $\ker\alpha$ is a contact distribution. This confirms
  `prop:pb-contact-null-counterexample`, including the exact sign of the
  Frobenius obstruction.

**New witness — no global section, hence no global base semimetric.** Let
$\mathcal C=S^2$, $G=U(1)$, and $P=S^3\to S^2$ the Hopf bundle. Let
$\mathcal B=\{\mathrm{vM}(\mu,\kappa_0):\mu\in S^1\}$ be the von Mises family on
$S^1$ at fixed concentration $\kappa_0>0$, a one-dimensional smooth
parametrized-measure model with positive Fisher information
$I=\kappa_0^2\,\mathbb E[\sin^2(\theta-\mu)]>0$, on which $U(1)$ acts by rotation
of the sample circle, simply transitively on $\mathcal B$. Then
$E=P\times_{\widehat\rho}\mathcal B\cong P$ as a bundle over $S^2$, because the
associated bundle for a simply transitive action is the principal bundle itself.
The Hopf bundle admits no section: a section would trivialize it, forcing
$S^3\cong S^2\times S^1$, contradicted by $\pi_2(S^3)=0\ne\mathbb Z=\pi_2(S^2\times S^1)$.
Hence there is **no** global agent section, and no global $h^\omega_s$, although
every hypothesis of `hyp:pb-regular-models` holds. Register this as
`CE-NO-GLOBAL-SECTION`.

### R2.5 Types, quantifiers, assumptions, falsification, anchors

**Types.** $D^\omega s\in\Gamma(\mathcal U;T^*\mathcal U\otimes s^*VE)$;
$h^\omega_s\in\Gamma(\operatorname{Sym}^2T^*\mathcal U)$;
$K^\omega_s\subseteq T\mathcal U$ a distribution; $Q^\omega_s$ a quotient vector
bundle over $\mathcal U$; $\hbar$ a Riemannian metric on the leaf space, a
different manifold from $\mathcal U$.

**Quantifiers.** For every open $\mathcal U$, every smooth $s\in\Gamma(\mathcal U,E)$,
every principal connection $\omega$, every $c\in\mathcal U$, and every
$X,Y,Z\in T_c\mathcal C$.

**Assumptions.** `hyp:geo-smooth-tier` and `hyp:pb-regular-models` in full,
including positive definiteness of $g^F$ and invariance of $g^F$ under a
parameter-independent bimeasurable represented sample action; smoothness of $s$;
constant rank for 4; involutivity, simplicity, and basicness for 5.

**Falsification.** Exhibit a smooth $s$ and $\omega$ with $g^F\succ0$ for which
$\operatorname{rad}h^\omega_s\ne\ker D^\omega s$; or a constant-rank $D^\omega s$
whose kernel fails to be a smooth subbundle; or an involutive constant-rank
radical with a simple foliation and a smooth Hausdorff leaf space for which
$h^\omega_s$ descends to a leaf-space tensor although (R2.4) fails.

**Anchors needing repair.** `05c_pullback_geometry.tex`: the convention sentence
"$D_A=d+\widehat\rho_{x*}(A)$" preceding `prop:pb-pullback-connection-change`
(replace the linear representation by the fundamental vector field, or restrict
the sentence to a linear associated-vector-bundle realization);
`prop:pb-statistical-tensor-descent` proof (supply the $\iota_{ug}=\iota_u\circ\widehat\rho(g)$
computation); `thm:pb-pullback-gauge-invariance` (retitle to passive covariance
and record R2.2(ii), so the `ESTABLISHED` tag does not read as an active-gauge
invariance claim); `thm:pb-pullback-rank-quotient` (cite the constant-rank
theorem *for vector-bundle morphisms*, not the constant-rank theorem for smooth
maps); the paragraph containing `eq:pb-null-basicness` (add the checkable
criterion (R2.4) and its $\nabla$-independence); and `SPEC.md` section 5e, whose
sentence "Then `(D^{\omega_x}\sigma)^*g_x^F` and the analogous cubic tensor are
global and gauge invariant" is unsupported without a section-existence hypothesis
and is refuted as an unconditional claim by `CE-NO-GLOBAL-SECTION`.

## 5. Result R3 — the horizontal defect and the exact signed Fisher comparison

### R3.1 Definition and equivalence with the source object

**Definition.** For a smooth bundle morphism $\Psi:E\to\bar E$ over $f$, define
$$
A_\Psi(e;X):=\operatorname{ver}^{\bar\omega}\Big(T_e\Psi\big(H^\omega_eX\big)\Big)
\in V_{\Psi(e)}\bar E,
\qquad e\in E,\;X\in T_{\varpi(e)}\mathcal C .
\tag{R3.1}
$$

**Lemma R3.1.** $A_\Psi(e;\cdot)$ is linear in $X$, and
$$
A_\Psi(e;X)=T_e\Psi\big(H^\omega_eX\big)-H^{\bar\omega}_{\Psi(e)}\big(T_cfX\big),
$$
which is the manuscript's `eq:pb-coarse-horizontal-defect`. In particular
$A_\Psi=\mathcal D\Psi$, and the manuscript's assertion that the difference is
vertical is correct.

*Proof.* Linearity is inherited from $H^\omega_e$ and $T_e\Psi$. For the second
claim, $T\bar\varpi\big(T\Psi(H^\omega_eX)\big)=Tf\big(T\varpi(H^\omega_eX)\big)=T_cfX$,
so $T\Psi(H^\omega_eX)$ projects onto $T_cfX$; its $\bar\omega$-horizontal part is
therefore $H^{\bar\omega}_{\Psi(e)}(T_cfX)$ and its vertical part is the stated
difference. $\square$

### R3.2 The exact first jet

**Theorem R3.2 (exact covariant first-jet chain rule).** Let $s\in\Gamma(\mathcal U,E)$
and $\bar s\in\Gamma(f(\mathcal U),\bar E)$ satisfy $\Psi\circ s=\bar s\circ f$ on
$\mathcal U$. Then, for every $c\in\mathcal U$ and $X\in T_c\mathcal C$,
$$
D^{\bar\omega}\bar s\big(T_cfX\big)
=T^V\Psi\big(D^\omega sX\big)+A_\Psi\big(s(c);X\big).
\tag{R3.2}
$$

*Proof.* Split $T_csX=H^\omega_{s(c)}X+D^\omega sX$ and apply $T\Psi$. Since
$D^\omega sX$ is vertical and $T\Psi$ preserves verticality, the second summand
maps to $T^V\Psi(D^\omega sX)$. By Lemma R3.1 the first maps to
$H^{\bar\omega}_{\Psi(s(c))}(TfX)+A_\Psi(s(c);X)$. On the other side,
$\Psi\circ s=\bar s\circ f$ gives
$T\Psi(T_csX)=T\bar s(T_cfX)=H^{\bar\omega}_{\bar s(f(c))}(TfX)+D^{\bar\omega}\bar s(TfX)$.
Since $\Psi(s(c))=\bar s(f(c))$, the two horizontal terms coincide and cancel,
and comparing vertical parts gives (R3.2). $\square$

This is `eq:pb-covariant-jet-chain-rule`. It is **correct as written in the
source** and is certified here.

### R3.3 The exact signed Fisher comparison

**Theorem R3.3 (exact signed comparison).** In the setting of Theorem R3.2, with
$\bar g^F$ a $\bar G$-invariant positive-definite vertical Fisher metric on
$\bar E$, define on $\mathcal U$

$$
\delta_\Psi:=(D^\omega s)^*\Delta_F^\Psi,
\qquad
\Delta_F^\Psi:=g^F-(T^V\Psi)^*\bar g^F ,
$$
$$
\mathcal X_\Psi(X,Y):=\bar g^F\big(T^V\Psi D^\omega sX,\;A_\Psi(s;Y)\big)
+\bar g^F\big(A_\Psi(s;X),\;T^V\Psi D^\omega sY\big),
$$
$$
\mathcal Q_\Psi(X,Y):=\bar g^F\big(A_\Psi(s;X),\;A_\Psi(s;Y)\big).
$$
Then $\mathcal X_\Psi$ and $\mathcal Q_\Psi$ are symmetric, $\mathcal Q_\Psi\succeq0$,
and **without any compatibility hypothesis**
$$
\boxed{\;
h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}
=\delta_\Psi-\mathcal X_\Psi-\mathcal Q_\Psi \;}
\tag{R3.3}
$$
as an identity of symmetric $2$-tensors on $\mathcal U$. The analogous exact
identity for the Amari–Chentsov pullbacks is
$$
c^\omega_s-f^*\bar c^{\bar\omega}_{\bar s}
=\Delta_{\mathcal T}^\Psi\big(D^\omega s\,\cdot,D^\omega s\,\cdot,D^\omega s\,\cdot\big)
-\sum_{\text{seven mixed terms}}\bar{\mathcal T}\big(\bullet,\bullet,\bullet\big),
\tag{R3.4}
$$
where each of the seven mixed terms carries at least one and at most three
occurrences of $A_\Psi(s;\cdot)$ and the remaining slots carry
$T^V\Psi D^\omega s(\cdot)$, and $\Delta_{\mathcal T}^\Psi=\mathcal T-(T^V\Psi)^*\bar{\mathcal T}$.

*Proof.* Write $u=D^\omega sX$, $v=D^\omega sY$, $a_X=A_\Psi(s(c);X)$,
$a_Y=A_\Psi(s(c);Y)$, $L=T^V\Psi$. By Theorem R3.2,
$D^{\bar\omega}\bar s(TfX)=Lu+a_X$. Hence
$$
\big(f^*\bar h^{\bar\omega}_{\bar s}\big)(X,Y)
=\bar g^F(Lu+a_X,\;Lv+a_Y)
=\bar g^F(Lu,Lv)+\bar g^F(Lu,a_Y)+\bar g^F(a_X,Lv)+\bar g^F(a_X,a_Y).
$$
Subtracting this from $h^\omega_s(X,Y)=g^F(u,v)$ and using
$\bar g^F(Lu,Lv)=\big((T^V\Psi)^*\bar g^F\big)(u,v)=g^F(u,v)-\Delta_F^\Psi(u,v)$
gives (R3.3). Symmetry of $\mathcal X_\Psi$ follows from symmetry of $\bar g^F$;
$\mathcal Q_\Psi\succeq0$ because $\bar g^F$ is positive definite. (R3.4) is the
same expansion for the trilinear $\bar{\mathcal T}$: the eight terms of
$\bar{\mathcal T}(Lu+a_X,Lv+a_Y,Lw+a_Z)$ split into the pure term, which combines
with $\mathcal T$ into $\Delta_{\mathcal T}^\Psi$, and seven mixed terms. $\square$

### R3.4 Positivity fails when the horizontal defect is nonzero

**Theorem R3.4 (exact positivity criterion and margin).** In the setting of
Theorem R3.3, and assuming in addition that the fiber map underlying $\Psi$ is
$q=N_\star|_{\mathcal B}$ for a parameter-independent Markov kernel $N$ with
family closure, so that $\Delta_F^\Psi\succeq0$ and hence $\delta_\Psi\succeq0$:

1. **Exact criterion.**
   $h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}\succeq0$ at $c$ if and only if
   $$
   \big\|D^{\bar\omega}\bar s(T_cfX)\big\|_{\bar g^F}\le\big\|D^\omega s\,X\big\|_{g^F}
   \qquad\text{for every }X\in T_c\mathcal C .
   $$
2. **Sufficient margin.** A sufficient condition is the pointwise bound
   $$
   \big\|A_\Psi(s(c);X)\big\|_{\bar g^F}
   \;\le\;
   \sqrt{h^\omega_s(X,X)}-\sqrt{h^\omega_s(X,X)-\delta_\Psi(X,X)} ,
   \tag{R3.5}
   $$
   whose right-hand side is the Fisher-loss margin of the channel in the
   direction $X$. In particular, in any direction where the channel is lossless
   ($\delta_\Psi(X,X)=0$) the margin is zero, and then
   $$
   h^\omega_s(X,X)-f^*\bar h^{\bar\omega}_{\bar s}(X,X)
   =-2\,\bar g^F\big(T^V\Psi D^\omega sX,\;A_\Psi(s;X)\big)-\big\|A_\Psi(s;X)\big\|^2_{\bar g^F},
   $$
   which is negative for every $A_\Psi(s;X)\ne0$ satisfying
   $2\,\bar g^F(T^V\Psi D^\omega sX,A_\Psi(s;X))>-\|A_\Psi(s;X)\|^2$.
3. **Strict negativity is attainable.** There is an instance with a genuine
   parameter-independent Markov fiber map, exactly related sections, positive
   definite fine and coarse Fisher metrics, and a smooth bundle morphism, for
   which $h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}$ is negative definite.

*Proof.* 1 is a restatement of (R3.3) using $h^\omega_s(X,X)=\|u\|^2_{g^F}$ and
$f^*\bar h(X,X)=\|Lu+a_X\|^2_{\bar g^F}$. 2: by the triangle inequality
$\|Lu+a_X\|\le\|Lu\|+\|a_X\|$ and $\|Lu\|^2=h^\omega_s(X,X)-\delta_\Psi(X,X)$,
so (R3.5) gives $\|Lu+a_X\|\le\sqrt{h^\omega_s(X,X)}=\|u\|$; the lossless case is
(R3.3) with $\delta_\Psi(X,X)=0$.

3, witness (`CE-HORIZONTAL-ANOMALY`, reconstructed exactly). Take
$\mathcal C=\bar{\mathcal C}=\mathbb R$ with coordinate $x$, $f=\operatorname{id}$,
$G=\bar G=(\mathbb R,+)$, $\kappa=\operatorname{id}$, $P=\bar P=\mathbb R\times\mathbb R$
trivial, $\mathcal P=\operatorname{id}$, $\mathsf K=\bar{\mathsf K}=\mathbb R$,
$\rho=\bar\rho$ the translation action, $\mathcal B=\bar{\mathcal B}=\{\mathcal N(\mu,1)\}$,
and $N(x,\cdot)=\delta_x$ the identity kernel, which is Markov,
parameter-independent, and equivariant, so $q=\operatorname{id}$,
$T^V\Psi=\operatorname{id}$, $\Delta_F^\Psi=0$. Take the source connection $A=0$
and the target connection $\bar A=-a\,dx$ with $a\ne0$; by (R2.1) the target
horizontal lift of $\partial_x$ is $\partial_x+a\partial_\mu$. Take $s$ the
section $\mu\equiv0$ and $\bar s=s$; then $\Psi\circ s=\bar s\circ f$ holds
exactly. Now $D^\omega s=0$, so $h^\omega_s=0$, while
$D^{\bar\omega}\bar s=\bar A\otimes\partial_\mu=-a\,dx\otimes\partial_\mu$, so
$\bar h^{\bar\omega}_{\bar s}=a^2dx^2$ and $f^*\bar h^{\bar\omega}_{\bar s}=a^2dx^2$.
Therefore
$$
h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}=-a^2\,dx^2\prec0 .
$$
Cross-check against (R3.3):
$\operatorname{ver}^{\bar\omega}(\partial_x)=\partial_x-(\partial_x+a\partial_\mu)=-a\partial_\mu$,
so $A_\Psi(s;\partial_x)=-a\partial_\mu$, $\delta_\Psi=0$, $\mathcal X_\Psi=0$
because $D^\omega s=0$, and $\mathcal Q_\Psi=a^2dx^2$; (R3.3) returns
$0-0-a^2dx^2$. $\square$

**Reading.** Theorem R3.4(3) shows that a normalized parameter-independent Markov
fiber map together with exactly related sections does **not** imply base Fisher
positivity. The horizontal-defect hypothesis is indispensable, and is not
implied by the Markov hypothesis, by relatedness, or by any amount of
equivariance.

### R3.5 The $A_\Psi=0$ theorem

**Theorem R3.5 (positive base Fisher defect).** Assume: (i) the data of
Theorem R1 with (A1)–(A5); (ii) $\bar g^F$ positive definite and
$\widehat{\bar\rho}(\bar G)$-invariant, so that it descends to a vertical tensor on
$\bar E$; (iii) $\Psi\circ s=\bar s\circ f$ with $\bar s$ smooth; (iv)
differentiability in quadratic mean of $\mathcal B$ and of the pushed family, with
square-integrable scores; and (v) $A_\Psi(s(c);X)=0$ for every $c\in\mathcal U$
and $X\in T_c\mathcal C$. Then
$$
h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}=\delta_\Psi=(D^\omega s)^*\Delta_F^\Psi\succeq0,
\qquad
\Delta_F^\Psi(w,w)=\mathbb E_\beta\operatorname{Var}_\beta\big(\ell_w(X)\mid Y\big)\ \ge 0 ,
$$
where $\ell_w$ is the score of the fine direction $w\in T_\beta\mathcal B$ under
the joint law $\beta(dx)N(x,d\bar y)$. Equality at $X$ holds if and only if the
fine score $\ell_{D^\omega sX}$ is $\sigma(Y)$-measurable $\beta$-almost surely.

*Proof.* By (R3.3) with $\mathcal X_\Psi=\mathcal Q_\Psi=0$, the base identity is
$\delta_\Psi$. For the vertical statement, fix $c$ and work in the pair of frames
$(u(c),\mathcal P(u(c)))$, in which $T^V\Psi=Tq$ by Theorem R1(3). For a
DQM curve $t\mapsto\beta_t$ in $\mathcal B$ with $\dot\beta_0=w$, the family
$t\mapsto q(\beta_t)=\beta_tN$ is DQM with score
$\bar\ell_w(y)=\mathbb E[\ell_w(X)\mid Y=y]$ because $N$ carries no parameter
dependence; the corresponding Fisher informations satisfy
$\mathbb E[\bar\ell_w^2]=\mathbb E\big[\mathbb E[\ell_w\mid Y]^2\big]$ and the law
of total variance gives
$\mathbb E[\ell_w^2]-\mathbb E[\bar\ell_w^2]=\mathbb E\operatorname{Var}(\ell_w\mid Y)\ge0$,
with equality exactly on the range of the conditional expectation. That is
$g^F(w,w)-\bar g^F(Tq\,w,Tq\,w)=\Delta_F^\Psi(w,w)\ge0$. Pulling back by
$D^\omega s$ preserves positive semidefiniteness. $\square$

**Why hypothesis (ii) is not redundant.** In a frame $u$, the local
representative of $\Psi$ is $\psi_c=\widehat{\bar\rho}(\varsigma(c))\circ q$, where
$\varsigma:\mathcal U\to\bar G$ is defined by
$\mathcal P(u(c))=\bar u(f(c))\cdot\varsigma(c)$. The representative therefore
carries a $c$-dependent gauge factor, and
$(T\psi_c)^*\bar g^F=(Tq)^*\big(\widehat{\bar\rho}(\varsigma)^*\bar g^F\big)$. That
factor cancels **only** because $\bar g^F$ is $\bar G$-invariant. Fine-side
invariance of $g^F$ together with (I) does not imply coarse-side invariance of
$\bar g^F$, in particular when $\kappa$ is not surjective. Coarse invariance is an
independent hypothesis and must be declared with the coarse model.

### R3.6 Types, quantifiers, falsification, anchors

**Types.** $A_\Psi\in\Gamma\big(E;\varpi^*T^*\mathcal C\otimes\Psi^*V\bar E\big)$;
along $s$, $A_\Psi(s;\cdot)\in\Gamma\big(\mathcal U;T^*\mathcal U\otimes f^*\bar s^*V\bar E\big)$;
$\Delta_F^\Psi\in\Gamma(E;\operatorname{Sym}^2V^*E)$;
$\delta_\Psi,\mathcal X_\Psi,\mathcal Q_\Psi\in\Gamma(\operatorname{Sym}^2T^*\mathcal U)$.

**Quantifiers.** For every $c\in\mathcal U$, every $X,Y\in T_c\mathcal C$, every
smooth $\Psi$ over $f$, every pair of connections, and every pair of related
sections.

**Falsification.** Exhibit a smooth $\Psi$ over $f$ and related sections for
which (R3.2) or (R3.3) fails at some $(c,X,Y)$; or exhibit an instance with
$A_\Psi(s;\cdot)=0$, a genuine parameter-independent Markov fiber map with family
closure, and $\bar G$-invariant $\bar g^F\succ0$, for which
$h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}$ has a negative eigenvalue; or
exhibit an instance satisfying the margin (R3.5) for which positivity fails.

**Anchors needing repair.** `05c_pullback_geometry.tex`
`thm:pb-pullback-fisher-defect` and `cor:pb-meta-perceived-geometry` are both
correctly guarded by `\mathcal D\Psi=0` and are certified; what is missing is the
**quantified** statement of what is retained when the guard is dropped. The
manuscript's figure caption at `fig:pb-pullback-naturality` says
"\eqref{eq:pb-covariant-jet-chain-rule} records the missing vertical term rather
than suppressing it", but the missing *tensor* terms $-\mathcal X_\Psi-\mathcal Q_\Psi$
never appear. Add (R3.3), (R3.4), Theorem R3.4 and the strict-negativity witness
to `sec:pb-fisher-defect`. Add hypothesis (ii) of Theorem R3.5 explicitly, since
`sec:pb-fisher-defect` currently derives its Markov positivity without declaring
$\bar G$-invariance of $\bar g^F$, which the frame computation above needs.

## 6. Result R4 — ordered composition of horizontal defects and the base defect cocycle

### R4.1 The ordered composition law

**Theorem R4.1.** Let
$E_0\xrightarrow{\ \Psi_{01}\ }E_1\xrightarrow{\ \Psi_{12}\ }E_2$ be smooth
bundle morphisms over $f_{01}:\mathcal C_0\to\mathcal C_1$ and
$f_{12}:\mathcal C_1\to\mathcal C_2$, with connections $\omega_0,\omega_1,\omega_2$.
Put $\Psi_{02}=\Psi_{12}\circ\Psi_{01}$, $f_{02}=f_{12}\circ f_{01}$. Then, for
every $e\in E_0$ over $c$ and every $X\in T_c\mathcal C_0$,
$$
\boxed{\;
A_{\Psi_{02}}(e;X)
=T^V\Psi_{12}\big|_{\Psi_{01}(e)}\Big(A_{\Psi_{01}}(e;X)\Big)
+A_{\Psi_{12}}\Big(\Psi_{01}(e);\,T_cf_{01}X\Big).\;}
\tag{R4.1}
$$

*Proof.* Expand $T\Psi_{01}(H^{\omega_0}_eX)=H^{\omega_1}_{\Psi_{01}e}(Tf_{01}X)+A_{\Psi_{01}}(e;X)$
by Lemma R3.1. Apply $T\Psi_{12}$. On the horizontal summand, Lemma R3.1 at the
second stage gives
$H^{\omega_2}_{\Psi_{02}e}(Tf_{12}Tf_{01}X)+A_{\Psi_{12}}(\Psi_{01}e;Tf_{01}X)$.
On the vertical summand it gives $T^V\Psi_{12}(A_{\Psi_{01}}(e;X))$, since
$T\Psi_{12}$ preserves verticality. Applying $\operatorname{ver}^{\omega_2}$ kills
the $H^{\omega_2}$ term and fixes the other two, which are already vertical. $\square$

**Order and domain.** The law is **not** symmetric and **not** an unweighted sum:
the earlier defect is pushed forward by the *later* vertical differential, and
the later defect is evaluated at the *image point* $\Psi_{01}(e)$ and on the
*pushed base vector* $T f_{01}X$. Writing $A_{02}=A_{01}+A_{12}$ is a type error,
since $A_{01}$ takes values in $V\bar E_1$ and $A_{12}$ in $VE_2$. The
corresponding domain refinement: for the composite defect to vanish it suffices
that $A_{\Psi_{01}}=0$ on $T_c\mathcal C_0$ and $A_{\Psi_{12}}=0$ on the
**sub-bundle** $Tf_{01}(T\mathcal C_0)\subseteq T\mathcal C_1$, at the points
$\Psi_{01}(e)$ only. Vanishing of $A_{\Psi_{12}}$ on all of $T\mathcal C_1$ at all
points of $E_1$ is stronger than needed.

### R4.2 The frame-twist representation and its exact cocycle

**Theorem R4.2 (frame-twist form).** Suppose $\Psi$ is induced as in Theorem R1
by $(\mathcal P,\kappa,q)$ with $q$ intertwining. Define the
**scale-connection defect form**
$$
\mathfrak A_{\mathcal P}:=\mathcal P^*\bar\omega-d\kappa\circ\omega
\;\in\;\Omega^1\big(P,\bar{\mathfrak g}\big).
$$
Then:

1. $\mathfrak A_{\mathcal P}$ is horizontal and $\operatorname{Ad}\circ\kappa$-equivariant,
   hence descends to
   $\mathfrak A_{\mathcal P}\in\Omega^1\big(\mathcal C;P\times_{\operatorname{Ad}\kappa}\bar{\mathfrak g}\big)$,
   and the map $[u,\xi]\mapsto[\mathcal P(u),\xi]$ identifies that bundle with
   $f^*\operatorname{Ad}(\bar P)$.
2. **The horizontal defect is a fundamental vertical field:**
   $$
   A_\Psi(e;X)=\vartheta_{\Psi(e)}\Big(\mathfrak A_{\mathcal P}(X)\Big),
   \qquad e\in E,\;X\in T_{\varpi(e)}\mathcal C .
   \tag{R4.2}
   $$
   In a frame $u$ with comparison function $\varsigma$ defined by
   $\mathcal P(u(c))=\bar u(f(c))\varsigma(c)$, the local generator is
   $$
   \mathfrak a(X)=\bar A\big(T_cfX\big)+\theta_R(X)-\operatorname{Ad}_{\varsigma(c)}\big(d\kappa(A(X))\big),
   \qquad
   \theta_R(X)=d\varsigma(X)\,\varsigma(c)^{-1},
   $$
   and $\mathfrak a=\operatorname{Ad}_{\varsigma}\big(u^*\mathfrak A_{\mathcal P}\big)$.
3. **Exact vanishing criterion.** $A_\Psi$ vanishes along $s$ if and only if
   $$
   \mathfrak A_{\mathcal P}(X)\in\bar{\mathfrak g}_{\,\bar s(f(c))}
   \qquad\text{for every }c,\,X,
   $$
   where $\bar{\mathfrak g}_{\bar\beta}$ is the isotropy subalgebra of $\bar\beta$
   under $\widehat{\bar\rho}$. The principal-level identity
   $\mathcal P^*\bar\omega=d\kappa\circ\omega$ is the special case
   $\mathfrak A_{\mathcal P}=0$; it is sufficient and, when the represented action
   is infinitesimally effective at $\bar s(f(c))$, also necessary.
4. **Exact ordered cocycle.** For composable scale maps,
   $$
   \mathfrak A_{\mathcal P_{02}}
   =\mathcal P_{01}^*\,\mathfrak A_{\mathcal P_{12}}
   +d\kappa_{12}\circ\mathfrak A_{\mathcal P_{01}} ,
   \tag{R4.3}
   $$
   which descends to $\mathfrak a_{02}=f_{01}^*\mathfrak a_{12}+d\kappa_{12}\circ\mathfrak a_{01}$
   and is consistent with (R4.1) via
   $T^V\Psi_{12}\circ\vartheta=\vartheta\circ d\kappa_{12}$.
5. The quadratic anomaly is the pullback of a Killing-type form:
   $$
   \mathcal Q_\Psi=\mathfrak a^*\,\mathfrak k_{\bar s(f(c))},
   \qquad
   \mathfrak k_{\bar\beta}(\xi,\eta):=\bar g^F\big(\bar\zeta_\xi(\bar\beta),\bar\zeta_\eta(\bar\beta)\big),
   $$
   so $\mathfrak k\succeq0$ with radical exactly $\bar{\mathfrak g}_{\bar\beta}$.
6. For a **general** bundle morphism over $f$, not induced by a single fiber map
   and a principal map, $A_\Psi$ need not be of fundamental type; its local form is
   $A_\Psi(X)=\partial_c\psi_c(\beta)[X]-T\psi_c\big(\zeta_{A(X)}(\beta)\big)+\bar\zeta_{\bar A(TfX)}\big(\psi_c\beta\big)$
   for the local representative $\psi_c$, and only the induced case collapses this
   to (R4.2).

*Proof.* 1: on a fundamental field $\zeta_\xi$ of $P$,
$\mathcal P^*\bar\omega(\zeta_\xi)=\bar\omega(\bar\zeta_{d\kappa\xi})=d\kappa\xi=d\kappa(\omega(\zeta_\xi))$,
so the difference annihilates vertical vectors; equivariance uses
$R_g^*\mathcal P^*\bar\omega=\operatorname{Ad}_{\kappa(g)^{-1}}\mathcal P^*\bar\omega$
and $d\kappa\circ\operatorname{Ad}_{g^{-1}}=\operatorname{Ad}_{\kappa(g)^{-1}}\circ d\kappa$.
Horizontal plus equivariant descends. The stated identification is well defined
because $[ug,\operatorname{Ad}_{\kappa(g)^{-1}}\xi]\mapsto[\mathcal P(u)\kappa(g),\operatorname{Ad}_{\kappa(g)^{-1}}\xi]=[\mathcal P(u),\xi]$.

2: in the trivializations, $\Psi(c,\beta)=(f(c),\psi_c(\beta))$ with
$\psi_c=\widehat{\bar\rho}(\varsigma(c))\circ q$. Using $H^\omega_{(c,\beta)}X=(X,-\zeta_{A(X)}(\beta))$
from (R2.1), the target horizontal lift $(TfX,-\bar\zeta_{\bar A(TfX)}(\psi_c\beta))$,
and Lemma R3.1,
$$
A_\Psi(X)=\partial_c\psi_c(\beta)[X]-T\psi_c\big(\zeta_{A(X)}(\beta)\big)+\bar\zeta_{\bar A(TfX)}\big(\psi_c\beta\big).
$$
Now $\partial_c\psi_c(\beta)[X]=\bar\zeta_{\theta_R(X)}(\psi_c\beta)$ by the
right-logarithmic-derivative computation of Lemma R2.1; Theorem R1(4) gives
$Tq\,\zeta_\xi=\bar\zeta_{d\kappa\xi}\circ q$; and the $\operatorname{Ad}$-identity
gives $T\widehat{\bar\rho}(\varsigma)\bar\zeta_{d\kappa\xi}(q\beta)=\bar\zeta_{\operatorname{Ad}_\varsigma d\kappa\xi}(\psi_c\beta)$.
Collecting, $A_\Psi(X)=\bar\zeta_{\mathfrak a(X)}(\psi_c\beta)$ with $\mathfrak a$ as
displayed. For the last identity, the principal-bundle transformation
$v=\bar u\circ f\cdot\varsigma$ gives
$u^*\mathcal P^*\bar\omega=\operatorname{Ad}_{\varsigma^{-1}}(\bar A\circ Tf)+\varsigma^{-1}d\varsigma$
and $u^*(d\kappa\circ\omega)=d\kappa\circ A$, whence
$u^*\mathfrak A_{\mathcal P}=\operatorname{Ad}_{\varsigma^{-1}}\mathfrak a$.

3: $\bar\zeta_{\mathfrak a(X)}(\bar\beta)=0$ if and only if $\mathfrak a(X)$ lies in
the isotropy subalgebra at $\bar\beta$; along $s$ the relevant point is
$\Psi(s(c))=\bar s(f(c))$. Conjugating by $\operatorname{Ad}_{\varsigma}$ moves the
statement between $\mathfrak a$ and $u^*\mathfrak A_{\mathcal P}$ and moves the
isotropy algebra correspondingly.

4: $\mathcal P_{02}^*\omega_2=\mathcal P_{01}^*\mathcal P_{12}^*\omega_2
=\mathcal P_{01}^*\big(\mathfrak A_{\mathcal P_{12}}+d\kappa_{12}\circ\omega_1\big)
=\mathcal P_{01}^*\mathfrak A_{\mathcal P_{12}}+d\kappa_{12}\circ\big(\mathfrak A_{\mathcal P_{01}}+d\kappa_{01}\circ\omega_0\big)$,
and $d\kappa_{02}=d\kappa_{12}\circ d\kappa_{01}$; subtracting
$d\kappa_{02}\circ\omega_0$ gives (R4.3). Consistency with (R4.1) uses Theorem R1(4)
at the second stage.

5 is (R4.2) substituted into the definition of $\mathcal Q_\Psi$, plus positive
definiteness of $\bar g^F$. 6 is the displayed local formula, which was derived
without assuming the induced form. $\square$

**Consistency check on the strict-negativity witness.** In Theorem R3.4(3),
$\kappa=\operatorname{id}$, $A=0$, $\bar A=-a\,dx$, $\varsigma\equiv e$, so
$\mathfrak a(\partial_x)=-a$ and $\bar\zeta_{-a}=-a\partial_\mu$, reproducing
$A_\Psi(s;\partial_x)=-a\partial_\mu$ and $\mathcal Q_\Psi=a^2dx^2$ exactly.

### R4.3 The induced base Fisher-defect cocycle

**Theorem R4.3.** With $\Psi_{01},\Psi_{12}$ as in Theorem R4.1, sections
$s_0,s_1,s_2$ satisfying $\Psi_{01}\circ s_0=s_1\circ f_{01}$ and
$\Psi_{12}\circ s_1=s_2\circ f_{12}$, and $h_j:=h^{\omega_j}_{s_j}$:

1. **Unconditional telescoping.** With the notation of Theorem R3.3 at each stage,
   $$
   h_0-f_{02}^*h_2
   =\big(\delta_{01}+f_{01}^*\delta_{12}\big)
   -\big(\mathcal X_{01}+f_{01}^*\mathcal X_{12}\big)
   -\big(\mathcal Q_{01}+f_{01}^*\mathcal Q_{12}\big).
   $$
   This requires no compatibility hypothesis; it is the sum of the two instances
   of (R3.3).
2. **Vertical cocycle (algebraic).** $\Delta_F^{\Psi_{12}\circ\Psi_{01}}
   =\Delta_F^{\Psi_{01}}+(T^V\Psi_{01})^*\Delta_F^{\Psi_{12}}$, by contravariance
   of tensor pullback alone. This is `eq:pb-fisher-defect-cocycle` and is
   certified.
3. **Base cocycle (sharp hypothesis).**
   $$
   \delta_{02}=\delta_{01}+f_{01}^*\delta_{12}
   \tag{R4.4}
   $$
   holds **if and only if**
   $\Delta_F^{\Psi_{12}}$ vanishes on the mixed and quadratic contributions of
   $A_{\Psi_{01}}$, and in particular it holds whenever $A_{\Psi_{01}}(s_0;\cdot)=0$.
   Explicitly, without that hypothesis,
   $$
   \delta_{02}-\delta_{01}-f_{01}^*\delta_{12}
   =-\Big[\Delta_F^{\Psi_{12}}\big(L_{01}D^{\omega_0}s_0\,\cdot,\;A_{\Psi_{01}}(s_0;\cdot)\big)
   +\Delta_F^{\Psi_{12}}\big(A_{\Psi_{01}}(s_0;\cdot),\;L_{01}D^{\omega_0}s_0\,\cdot\big)\Big]
   +\Delta_F^{\Psi_{12}}\big(A_{\Psi_{01}}(s_0;\cdot),A_{\Psi_{01}}(s_0;\cdot)\big),
   $$
   where $L_{01}=T^V\Psi_{01}$.
4. **Interpretation requires more.** The identification
   $\delta_{12}=h_1-f_{12}^*h_2$ additionally requires $A_{\Psi_{12}}(s_1;\cdot)=0$.
   Thus (R4.4) and its reading as an additive decomposition of base information
   loss have **different** hypotheses: the cocycle needs only stage-one
   compatibility, the reading needs stage-two compatibility as well.

*Proof.* 1: add the two instances of (R3.3), the second pulled back by $f_{01}$,
and use $f_{02}^*=f_{01}^*f_{12}^*$. 2: expand
$g_0^F-(T^V\Psi_{01})^*(T^V\Psi_{12})^*g_2^F$ by adding and subtracting
$(T^V\Psi_{01})^*g_1^F$. 3: apply $(D^{\omega_0}s_0)^*$ to 2, obtaining
$\delta_{02}=\delta_{01}+(D^{\omega_0}s_0)^*(T^V\Psi_{01})^*\Delta_F^{\Psi_{12}}$,
then substitute $T^V\Psi_{01}\circ D^{\omega_0}s_0=D^{\omega_1}s_1\circ Tf_{01}-A_{\Psi_{01}}(s_0;\cdot)$
from (R3.2) and expand the resulting bilinear form; the pure term is
$f_{01}^*\delta_{12}$ and the remaining three terms are displayed. 4 is
Theorem R3.3 applied at stage two. $\square$

### R4.4 Types, quantifiers, falsification, anchors

**Types.** $\mathfrak A_{\mathcal P}\in\Omega^1(\mathcal C;f^*\operatorname{Ad}(\bar P))$;
$\mathfrak k_{\bar\beta}\in\operatorname{Sym}^2\bar{\mathfrak g}^*$;
$\delta_{jk},\mathcal X_{jk},\mathcal Q_{jk}\in\Gamma(\operatorname{Sym}^2T^*\mathcal C_j)$;
$A_{\Psi_{jk}}$ as in R3.6.

**Quantifiers.** For every finite composable sequence of scale arrows, for both
channels independently, for every point of the fine total space, and for every
fine base tangent vector.

**Falsification.** Exhibit composable $\Psi_{01},\Psi_{12}$ for which (R4.1) or
(R4.3) fails; or exhibit an instance with $A_{\Psi_{01}}(s_0;\cdot)=0$ for which
(R4.4) fails; or exhibit an instance with $A_{\Psi_{01}}(s_0;\cdot)\ne0$ and
$\Delta_F^{\Psi_{12}}\ne0$ for which (R4.4) nevertheless holds while the displayed
correction is nonzero.

**Anchors needing repair.** `05c_pullback_geometry.tex`
`thm:pb-fisher-defect-cocycle`: (a) its statement never declares the base maps,
connections, or sections of the two arrows, so "composable smooth statistical
bundle morphisms" is untyped; (b) its final sentence, "If the connections are
compatible and the sections are related at each scale, pulling
\eqref{eq:pb-fisher-defect-cocycle} back by the fine covariant jet gives the
corresponding additive decomposition of information loss on the base", uses the
phrase **connection-compatible / compatible connections**, which is used at four
places in the manuscript — `05c` lines near the chapter opening, the caption of
`fig:pb-pullback-naturality`, the sentence in `thm:pb-fisher-defect-cocycle`,
`06_general_coarsegraining.tex` after `thm:cg-fisher-contraction`, and
`08_infogeometry.tex` in the "what is not claimed" section — and is **never
defined anywhere in the manuscript**. Replace it by the exact criterion of
Theorem R4.2(3) and, in `thm:pb-fisher-defect-cocycle`, by the two distinct
hypotheses of Theorem R4.3(3) and R4.3(4). Also add (R4.1) and (R4.3), which the
manuscript does not state at all: `eq:rg-cross-morphism-defects` and
`eq:rg-cross-connection-defects` in `07_general_renormalization.tex` record
cross-scale defects as *ordered pairs of maps to be compared*, and
`eq:rg-principal-connection-naturality` gives only the sufficient principal-level
condition; neither supplies a composition law or the sharp isotropy criterion.

## 7. Result R5 — the two-channel meta-agent version and sharp projectability

### R7.0 Note on the two channels

A meta-agent over $\bar{\mathcal C}$ is the section-bearing object
$\bar{\mathcal A}=\big(\bar{\mathcal C};\bar q,\bar s,\bar u^b,\bar u^m\big)$ in
the sense of `def:geo-agent`. It requires **two** morphisms
$\Psi_b:\mathcal E_b\to\bar{\mathcal E}_b$ and
$\Psi_m:\mathcal E_m\to\bar{\mathcal E}_m$ over the **same** base map $f$ and, in
the common-principal setting, over the **same** $(\mathcal P,\kappa)$, but with
**different** sample kernels $N_b$, $N_m$, different intertwining conditions,
different family-closure conditions, and different horizontal defects
$A_{\Psi_b}$, $A_{\Psi_m}$ computed against $\omega_b,\bar\omega_b$ and
$\omega_m,\bar\omega_m$ respectively. Nothing in Section 3–6 couples the two
channels: the common principal bundle supplies the same $\mathcal P$ and hence a
common $\mathfrak A_{\mathcal P}$ **only** when the two channels use the same
connections; with $\omega_b\ne\omega_m$ or $\bar\omega_b\ne\bar\omega_m$ the two
scale-connection defect forms are different elements of
$\Omega^1(\mathcal C;f^*\operatorname{Ad}(\bar P))$.

### R7.1 Sharp projectability

**Theorem R5 (projectability).** Let $f:\mathcal C\to\bar{\mathcal C}$ be a
surjective smooth submersion, $\Psi:E\to\bar E$ a smooth bundle morphism over
$f$, $\omega,\bar\omega$ connections, and $Q\in\Gamma(\mathcal C,E)$. Consider:

* **(P1)** There exists $\bar Q\in\Gamma(\bar{\mathcal C},\bar E)$ with
  $\Psi\circ Q=\bar Q\circ f$.
* **(P2)** $\Psi\circ Q$ is constant on each fiber of $f$.
* **(P3)** $T^V\Psi\big(D^\omega Q(X)\big)+A_\Psi\big(Q(c);X\big)=0$ for every
  $c\in\mathcal C$ and every $X\in\ker T_cf$.

Then (P1) $\Leftrightarrow$ (P2) $\Rightarrow$ (P3), and if the fibers of $f$ are
connected then (P3) $\Rightarrow$ (P2). Under (P2), $\bar Q$ is unique, is
automatically **smooth**, and is automatically a section, i.e.
$\bar\varpi\circ\bar Q=\operatorname{id}_{\bar{\mathcal C}}$.

*Proof.* (P1)$\Rightarrow$(P2): $\Psi Q(c)=\bar Q(f(c))$ depends on $c$ only
through $f(c)$. (P2)$\Rightarrow$(P1) with smoothness: a surjective smooth
submersion is a smooth quotient map, and a smooth map constant on its fibers
descends uniquely to a smooth map on the quotient. Uniqueness holds because $f$
is surjective. Section property:
$\bar\varpi\bar Q f=\bar\varpi\Psi Q=f\varpi Q=f$, and surjectivity of $f$ gives
$\bar\varpi\bar Q=\operatorname{id}$.

(P2)$\Rightarrow$(P3): differentiate along a fiber direction. For $X\in\ker T_cf$,
split $T_cQ\,X=H^\omega_{Q(c)}X+D^\omega Q(X)$ and apply $T\Psi$; by Lemma R3.1,
$$
T(\Psi\circ Q)(X)
=H^{\bar\omega}_{\Psi Q(c)}\big(T_cfX\big)+A_\Psi\big(Q(c);X\big)+T^V\Psi\big(D^\omega Q(X)\big)
=A_\Psi\big(Q(c);X\big)+T^V\Psi\big(D^\omega Q(X)\big),
$$
because $T_cfX=0$. Constancy along the fiber forces the left side to vanish.

(P3)$\Rightarrow$(P2) under connected fibers: the same computation shows that
$T(\Psi\circ Q)$ annihilates $\ker Tf$; the fibers of a submersion are connected
embedded submanifolds when assumed connected, and a smooth map with vanishing
derivative along a connected submanifold is constant on it. $\square$

**Smoothness is a theorem, not an obligation.** `05c_pullback_geometry.tex`, in
the paragraph declaring `eq:pb-coarse-related-sections`, writes: "For a
surjective submersion $f$, this excludes fine sections whose $\Psi$-images vary
along a fiber of $f$; constancy on those fibers and smoothness of the descended
factor are the corresponding descent obligations." Under the stated submersion
hypothesis, smoothness of the descended factor is **not** an open obligation; it
follows from constancy by the quotient theorem for surjective submersions. This
hedge should be discharged rather than carried.

**Submersion is load-bearing, and there is a witness.** Drop the submersion
hypothesis. Take $\mathcal C=\bar{\mathcal C}=\mathbb R$, $f(x)=x^3$ (a smooth
bijection, not a submersion at $0$), trivial bundles with fiber
$\mathcal B=\{\mathcal N(\mu,1)\}$ and trivial group action,
$\Psi(x,\beta)=(x^3,\beta)$, and the fine section $Q(x)=(x,\mathcal N(x,1))$.
Then $\Psi\circ Q$ is trivially constant on the singleton fibers, the unique
descended factor is $\bar Q(y)=(y,\mathcal N(y^{1/3},1))$, and $\bar Q$ is
continuous but **not** differentiable at $y=0$. So under a nonsubmersive base
map, "constant on fibers" gives a unique set-theoretic descent that need not be a
smooth section. Register this as `CE-NONSMOOTH-DESCENT`.

### R7.2 A pointwise bundle morphism does not define a map on section configurations

**Theorem R5.2 (non-functoriality on section spaces).** Let $f$ be a surjective
submersion, let $c_0\in\mathcal C$ with $\ker T_{c_0}f\ne 0$, and suppose there
exist $e_0\in E_{c_0}$ and $w\in V_{e_0}E$ with $T^V\Psi(w)\ne0$. Assume
$\Gamma(\mathcal C,E)\ne\varnothing$. Then the set
$$
\Gamma_{\mathrm{proj}}(\Psi):=\big\{Q\in\Gamma(\mathcal C,E):\ Q\text{ satisfies (P2)}\big\}
$$
is a **proper** subset of $\Gamma(\mathcal C,E)$. Consequently the assignment
$Q\mapsto\bar Q$ is a partial map on section configurations, not a map defined on
all of $\Gamma(\mathcal C,E)$, and $\Psi$ alone does not induce a configuration
coarse map.

*Proof.* Since $f$ is a submersion, $\ker Tf$ is an involutive constant-rank
distribution (the tangent distribution of the fibers), so by Frobenius there is a
chart $\mathcal U\ni c_0$ with coordinates $(x^1,\dots,x^n)$ in which
$\ker Tf=\operatorname{span}\{\partial_1,\dots,\partial_k\}$, $k\ge1$; shrink
$\mathcal U$ so that $E|_{\mathcal U}$ is trivialized by a local section $u$ of
$P$. Pick any $Q_0\in\Gamma(\mathcal C,E)$ and, adjusting inside $\mathcal U$ if
necessary, arrange $Q_0(c_0)=e_0$. If $Q_0\notin\Gamma_{\mathrm{proj}}(\Psi)$ we
are done. Otherwise, let $W$ be a smooth vector field on $\mathcal B$ with
$W(\beta_0)=w$ in the trivialization, with local flow $\Phi^W_t$, and let
$\chi\in C^\infty_c(\mathcal U)$ satisfy $\chi(c_0)=0$ and
$\partial_1\chi(c_0)\ne0$. Define $Q_\epsilon$ by the representative
$\beta_\epsilon(c)=\Phi^W_{\epsilon\chi(c)}\big(\beta_0(c)\big)$, extended by
$Q_0$ outside $\operatorname{supp}\chi$; each $Q_\epsilon$ is a smooth global
section. Because $\chi(c_0)=0$, we have $Q_\epsilon(c_0)=e_0$ for every
$\epsilon$, so both $A_\Psi(Q_\epsilon(c_0);\partial_1)$ and the value of
$T^V\Psi$ at that point are independent of $\epsilon$. Differentiating the
left side of (P3) at $\epsilon=0$ in the direction $X=\partial_1\in\ker T_{c_0}f$
gives
$$
\frac{d}{d\epsilon}\Big|_{0}\Big[T^V\Psi\big(D^\omega Q_\epsilon(\partial_1)\big)+A_\Psi\big(Q_\epsilon(c_0);\partial_1\big)\Big]
=\partial_1\chi(c_0)\;T^V\Psi(w)\ \ne 0 ,
$$
since the connection term $\zeta_{A(\partial_1)}(\beta_\epsilon(c_0))$ is also
$\epsilon$-independent at $c_0$. Hence (P3) fails for all sufficiently small
$\epsilon\ne0$, and by Theorem R5 so does (P2). $\square$

**Concrete witness (`CE-SECTION-DESCENT`, reconstructed exactly).**
$\mathcal C=S^1$, $\bar{\mathcal C}=\{\ast\}$, $f$ the constant map — a surjective
submersion with connected fiber $S^1$. Trivial bundles with fiber the unit-variance
normal location family and trivial group action, $\Psi$ the identity on fibers.
Fine section $Q(x)=\mathcal N(\sin x,1)$. Then $A_\Psi=0$, $\ker Tf=TS^1$, and
$T^V\Psi(D^\omega Q(\partial_x))=\cos x\,\partial_\mu$, which is not identically
zero; (P3) fails, so no coarse section over the point exists. This confirms the
register entry, and Theorem R5 explains it: the obstruction is exactly the
nonvanishing of the coarse-channel image of the fine covariant vertical jet along
collapsed directions.

### R7.3 The two channels are independent

**Proposition R5.3.** Projectability in one channel neither implies nor is
implied by projectability in the other.

*Proof.* Use the $S^1$ collapse of R7.2 for both channels. Belief channel: let
$N_b$ send every sample to a single point, so $\bar{\mathcal B}_b$ is a singleton,
$T^V\Psi_b=0$, and every fine belief section is projectable. Model channel: let
$N_m$ be the identity kernel and let $s(x)=\mathcal N(\sin x,1)$; by R7.2 it is
not projectable. Exchanging the roles of the two channels gives the converse
witness. $\square$

**Consequence for the meta-agent.** A meta-agent
$\bar{\mathcal A}=(\bar{\mathcal C};\bar q,\bar s,\bar u^b,\bar u^m)$ exists only
when **both** channel conditions (P2) hold. Under those two conditions, and if in
addition $A_{\Psi_b}(q;\cdot)=0$ and $A_{\Psi_m}(s;\cdot)=0$ and both channels
carry parameter-independent Markov fiber maps with family closure and
$\bar G$-invariant coarse Fisher metrics, then Theorem R3.5 applies channelwise:
$$
h^{\omega_b}_{q}-f^*\bar h^{\bar\omega_b}_{\bar q}\succeq0,
\qquad
h^{\omega_m}_{s}-f^*\bar h^{\bar\omega_m}_{\bar s}\succeq0 .
$$

**A cross-scale weight hypothesis the source does not state.** If a single base
tensor is formed by `hyp:pb-weighted-product-geometry`,
$h^{\mathrm{prod}}=w_bh^{\omega_b}_q+w_mh^{\omega_m}_s$ at the fine scale and
$\bar h^{\mathrm{prod}}=\bar w_b\bar h^{\bar\omega_b}_{\bar q}+\bar w_m\bar h^{\bar\omega_m}_{\bar s}$
at the coarse scale, then
$$
h^{\mathrm{prod}}-f^*\bar h^{\mathrm{prod}}
=\sum_{x\in\{b,m\}}\Big[w_x\big(h_x-f^*\bar h_x\big)+(w_x-\bar w_x)\,f^*\bar h_x\Big],
$$
which is positive semidefinite under the channelwise hypotheses **only if in
addition** $\bar w_x\le w_x$ for both channels. Independently declared coarse
weights with $\bar w_x>w_x$ break positivity even with zero horizontal defect and
genuine Markov channels. The manuscript declares weights at one scale
(`hyp:pb-weighted-product-geometry`) and never addresses cross-scale weight
consistency.

### R7.4 Types, quantifiers, falsification, anchors

**Types.** $\Gamma(\mathcal C,E)$ a set of smooth sections, not a priori a
manifold; $\Gamma_{\mathrm{proj}}(\Psi)\subseteq\Gamma(\mathcal C,E)$ the zero set
of the nonlinear first-order differential operator
$Q\mapsto\big(T^V\Psi\circ D^\omega Q+A_\Psi(Q;\cdot)\big)\big|_{\ker Tf}$;
$\ker Tf\subseteq T\mathcal C$ an involutive constant-rank distribution;
$\bar Q\in\Gamma(\bar{\mathcal C},\bar E)$.

**Quantifiers.** For every surjective submersion $f$, every smooth $\Psi$ over
$f$, every $Q\in\Gamma(\mathcal C,E)$, every $c\in\mathcal C$, and every
$X\in\ker T_cf$; and, in R7.3, for both channels independently.

**Assumptions.** $f$ a surjective submersion; connected fibers for
(P3)$\Rightarrow$(P2); $\Psi$ smooth; $Q$ smooth; existence of at least one global
section for R7.2.

**Falsification.** Exhibit a surjective submersion $f$ with connected fibers, a
smooth $\Psi$ over it, and a smooth $Q$ satisfying (P3) for which no smooth
coarse section exists; or exhibit a nonvanishing $T^V\Psi$ on a collapsed
direction for which every global fine section is projectable.

**Anchors needing repair.** `05c_pullback_geometry.tex`, the paragraph declaring
`eq:pb-coarse-related-sections`: (a) discharge the smoothness hedge by Theorem R5;
(b) add the connection-relative criterion (P3), which the manuscript does not
have and which is what makes the descent obligation checkable; (c) add the
non-functoriality Theorem R5.2, so that `eq:pb-coarse-related-sections` is
visibly a hypothesis on the *pair* $(\Psi,s)$ and not a property of $\Psi$;
(d) add the connected-fiber hypothesis, without which (P3) is only necessary.
`07_general_renormalization.tex`, the passage beginning "When levelwise agent or
meta-agent sections and regular vertical Fisher tensors are also declared":
add that the *existence* of the coarse sections is itself conditional on (P2) in
each channel separately, which the passage presently presupposes.
`hyp:pb-weighted-product-geometry`: add the cross-scale weight condition
$\bar w_x\le w_x$ wherever the weighted product is compared across scales.

## 8. Result R6 — three separated geometries, the frame-twist term, and the supplied-versus-chosen inventory

### R6.1 The three geometries

**(G1) Contextual base geometry.** $h^\omega_s\in\Gamma(\operatorname{Sym}^2T^*\mathcal U)$,
a symmetric $2$-tensor on the finite-dimensional base $\mathcal C$, depending on
the triple $(s,\omega,g^F)$. It is generically degenerate; its radical is
$\ker D^\omega s$ (Theorem R2.4). It **requires a connection**. It is invariant
under passive reframing and covariant under active gauge transformations of the
pair $(\omega,s)$, but not invariant under active gauge transformations of $s$
alone (Proposition R2.2).

**(G2) Configuration-space geometry.** A metric $\mathsf G^F$ on a declared
section manifold $\mathcal Q\subseteq\Gamma(\mathcal C,E)$. At
$Q\in\mathcal Q$, $T_Q\mathcal Q\subseteq\Gamma(Q^*VE)$ consists of **vertical**
fields along $Q$ by `eq:hist-pointwise-history-verticality`, and the natural
candidate is
$$
\mathsf G^F_Q(\dot Q,\dot Q)=\int_{\mathcal C}w(c)\,g^F\big(\dot Q(c),\dot Q(c)\big)\,\mu(dc),
$$
which requires a **base measure** $\mu$, **channel weights** $w$, integrability,
a manifold topology on $\mathcal Q$, and a gauge-quotient rule. It requires **no
connection**. It is a metric on a different manifold, of different dimension,
than (G1). Nothing identifies (G1) and (G2): $h^\omega_s$ is a tensor field on
$\mathcal C$ attached to one section; $\mathsf G^F$ is a single tensor at one
point of $\mathcal Q$.

**(G3) Frame twist.** Two structurally identical objects, one within a scale and
one across scales, both obtained by applying the fundamental vertical map to an
$\operatorname{Ad}$-type one-form on the base:
$$
\text{within a scale:}\quad
R_a^s(X)=\vartheta_{s(c)}\big(a(X)\big),
\qquad a=\omega'-\omega\in\Omega^1\big(\mathcal C;\operatorname{Ad}(P)\big);
$$
$$
\text{across scales:}\quad
A_\Psi(e;X)=\vartheta_{\Psi(e)}\big(\mathfrak A_{\mathcal P}(X)\big),
\qquad \mathfrak A_{\mathcal P}\in\Omega^1\big(\mathcal C;f^*\operatorname{Ad}(\bar P)\big).
$$
The first is `eq:pb-connection-difference-vertical` and drives the connection
change formulas `eq:pb-jet-connection-change`, `eq:pb-fisher-connection-change`;
the second is Theorem R4.2 and drives $\mathcal X_\Psi$ and $\mathcal Q_\Psi$ in
(R3.3). In both cases the induced quadratic contribution is the pullback of the
same Killing-type form $\mathfrak k_\beta(\xi,\eta)=g^F(\zeta_\xi(\beta),\zeta_\eta(\beta))$
along the relevant one-form, and in both cases it is invisible exactly on the
isotropy subalgebra of the section value. In particular:

* If $D^\omega s=0$ and $\omega'=\omega+a$, then $h^{\omega'}_s=a^*\mathfrak k_{s(c)}$
  is a **pure frame-twist semimetric** on the base, with radical
  $a^{-1}(\mathfrak g_{s(c)})$. Setting $\dim\mathcal C=1$, $G=(\mathbb R,+)$,
  $\mathcal B$ the normal location family and $a=a_0dx$ reproduces
  `eq:pb-connection-dependence-example`, $h^{A'}=a_0^2dx^2$, with the correct
  coefficient.
* If $s(c)$ is a $G$-fixed point, all within-scale frame twist vanishes; if
  $\bar s(f(c))$ is a $\bar G$-fixed point, all cross-scale frame twist vanishes,
  hence $\mathcal X_\Psi=\mathcal Q_\Psi=0$ and base Fisher positivity is restored
  without any condition on the connections.
* For a **general** bundle morphism not induced by $(\mathcal P,\kappa,q)$, the
  horizontal defect is **not** a frame twist; only the induced case admits the
  representation (R4.2) (Theorem R4.2(6)).

### R6.2 What the principal bundle supplies, and what needs an extra choice

**Supplied by $(\pi:P\to\mathcal C,G)$ alone.** The set of local principal
sections and their transition cocycle $T^x_{ij}$ with `eq:geo-cech-cocycle`; the
single nonabelian Čech class `eq:geo-cech-class`; the relative principal-frame
field $h_i$ of `eq:geo-relative-frame` for any two chosen local sections; the
adjoint bundle $\operatorname{Ad}(P)$; the gauge group $\mathcal G(P)$; and the
fact that the space of principal connections is a **nonempty** affine space over
$\Omega^1(\mathcal C;\operatorname{Ad}(P))$.

**Not supplied, and each an independent declaration.**
1. The representations $\rho_b,\rho_m$ and the invariant law fibers
   $\mathcal B_b,\mathcal B_m$, hence the associated bundles themselves.
2. A **choice** of connection. The affine space of connections is nonempty but has
   no canonical point, so $D^\omega s$, $h^\omega_s$, $c^\omega_s$, horizontality,
   and $\mathfrak A_{\mathcal P}$ are all connection-relative. This is the exact
   content that passive gauge invariance does **not** supply.
3. A **global** section. `CE-NO-GLOBAL-SECTION` shows the Hopf bundle with a
   von Mises fiber has none, although every regularity hypothesis holds.
4. The Fisher metric and Amari–Chentsov tensor on the fiber: these need the
   smooth parametrized-measure-model tier, differentiability in quadratic mean,
   integrability, nondegeneracy, and invariance of the represented action under a
   bimeasurable sample re-coordinatization.
5. A cross-channel morphism $\Phi$ or $\widetilde\Phi$: the relative frame field
   $h_i$ produces $\widehat\rho_b(h_i)$ and $\widehat\rho_m(h_i)$ on two different
   fibers and no map between them (`02_geometry.tex`, the paragraph after
   `eq:geo-quotient-convention`). Certified.
6. Channel weights $w_b,w_m$ and their coarse counterparts, needed for any single
   base tensor and, across scales, subject to $\bar w_x\le w_x$ (R7.3).
7. A base measure $\mu$ on $\mathcal C$ and a manifold topology on the section
   space, needed for (G2).
8. The scale datum $(f,\kappa,\mathcal P,N_b,N_m)$ and the coarse connections; the
   pair $(\omega,\bar\omega,\mathcal P)$ then determines $\mathfrak A_{\mathcal P}$
   but no choice makes it canonically zero.
9. A reference identification $i_\ell:\mathcal C_\ell\to\mathcal C_\star$ before
   any difference of levelwise base tensors is formed
   (`eq:pb-metric-beta-reference`). Certified.
10. An objective and a mobility before any orbit or duration is selected. This
    lies in the history route and is not adjudicated here.

### R6.3 Types, quantifiers, falsification, anchors

**Types.** As displayed in R6.1. Note in particular that $h^\omega_s$ and
$\mathsf G^F$ are tensors on manifolds of different dimension and that
$R^s_a$ and $A_\Psi$ are vertical-vector-valued one-forms on $\mathcal C$ with
values in **different** pulled-back vertical bundles.

**Quantifiers.** For every connection pair, every section, every scale map, and
every choice of the listed extra data.

**Falsification.** Exhibit a canonical connection, a canonical global section, a
canonical pair of channel weights, or a canonical base measure determined by
$(P,G,\mathcal C)$ alone; any one of these refutes the inventory.

**Anchors needing repair.** `SPEC.md` section 5e "global" wording, as in R2.5.
`05d_relational_inference.tex`, `eq:hist-continuum-clock-speed` and its
surrounding paragraph, already state that $\mu$, the weights, and the topology
are not selected; that paragraph is certified and should be cross-referenced
from `05c` so that the (G1)/(G2) separation is visible at the point where
`def:pb-informational-pullbacks` is introduced.
`08_infogeometry.tex`, the "three typed uses of pullback" paragraph, correctly
separates the connection-relative base pullback, the parameter-space restriction,
and the pullback attractor; it should be extended by the (G1)/(G2)/(G3)
separation, since the frame-twist object appears in none of its three.

## 9. New counterexample-register candidates produced by this route

These are offered for the register maintainer; this pass does not edit the
register.

| ID | Claims attacked | Typed witness and decisive equation | Assumption boundary | Proposed status |
| --- | --- | --- | --- | --- |
| `CE-NO-GLOBAL-SECTION` | `SPEC.md` §5e "global"; any unconditional globality of $h^{\omega}_s$ | Hopf bundle $S^3\to S^2$ with $G=U(1)$ and von Mises fiber at fixed $\kappa_0$; $E\cong P$, and a section would force $S^3\cong S^2\times S^1$, contradicting $\pi_2(S^3)=0\ne\pi_2(S^2\times S^1)$. | Every hypothesis of `hyp:pb-regular-models` holds; only section existence fails. Globality needs a separate topological hypothesis. | CANDIDATE |
| `CE-NONSMOOTH-DESCENT` | `configuration-projectability` smoothness clause; any descent argument without a submersion | $f(x)=x^3$, trivial bundles, $\Psi(x,\beta)=(x^3,\beta)$, $Q(x)=\mathcal N(x,1)$; unique descent $\bar Q(y)=\mathcal N(y^{1/3},1)$ is continuous, not $C^1$ at $0$. | Under a **surjective submersion**, smoothness is automatic; without it, it can fail even for a bijection. | CANDIDATE |
| `CE-ACTIVE-GAUGE-PULLBACK` | any reading of `thm:pb-pullback-gauge-invariance` as active-gauge invariance | Trivial $\mathbb R$-bundle over $\mathbb R$, normal location fiber, $A=0$, $s\equiv\mathcal N(0,1)$ gives $h=0$; the automorphism $F(u(x)g)=u(x)(x+g)$ gives $h_{F\cdot s}=dx^2$. | The theorem's own hypothesis transforms $\omega$ **and** $s$; the witness transforms $s$ at fixed $\omega$. | CANDIDATE |
| `CE-COARSE-WEIGHTS` | positivity of the weighted product defect across scales | Zero horizontal defect, identity Markov channel, $\delta=0$, $\bar w_b=2w_b$: then $h^{\mathrm{prod}}-f^*\bar h^{\mathrm{prod}}=-w_bf^*\bar h_b\preceq0$ and is nonzero wherever $D^{\omega_b}q\ne0$. | `hyp:pb-weighted-product-geometry` declares weights at one scale only. | CANDIDATE |
| `CE-LAW-VS-KERNEL-EQUIVARIANCE` | any identification of sample-level and law-level equivariance | $\mathsf K=\mathbb R^2$, $G=SO(2)$, $\mathcal B$ the isotropic centered Gaussians, $N(x,\cdot)=\delta_{x_1}$: law-level intertwining holds vacuously while the kernel is not rotation-equivariant; $N_1,N_2,N_3$ of Lemma 2.1 induce one $q$ from three kernels. | Law-level intertwining constrains $N$ only on the supports of $\mathcal B$ and only up to the $G$-action on $\mathcal B$. | CANDIDATE |

The register's existing `CE-HORIZONTAL-ANOMALY` and `CE-SECTION-DESCENT` rows are
reconstructed exactly in Theorem R3.4(3) and Section R7.2 respectively, with all
signs and coefficients recomputed independently of the register's phrasing. On
this route they are ready to move from `CANDIDATE` to `EVIDENCE_VERIFIED`; that
promotion is a ledger action and is not performed here.

## 10. Attacks run against the current source, with verdicts

### 10.1 Attacks against `manuscripts/gauge_vfe_rg`

| Attack | Verdict | Basis |
| --- | --- | --- |
| Hidden global triviality in the descent of $g^F$ and $\mathcal T$ to the associated bundle | **REJECTED** | Lemma R2.3 descends the tensors pointwise from $G$-invariance alone; no trivialization, no global section, no cover condition. `hyp:geo-common-trivializations` is declared where used and is not smuggled. |
| Hidden global triviality in `thm:pb-pullback-gauge-invariance` and `def:pb-informational-pullbacks` | **REJECTED** | Both are stated over an open $\mathcal U$. The globality overstatement is in `SPEC.md` §5e and in the 2026-08-01 note, not in the chapter. |
| Unproved smooth descent of the coarse section | **PARTIALLY SUSTAINED** | The manuscript lists smoothness as an obligation when, under its own surjective-submersion hypothesis, it is a theorem (Theorem R5). Separately, smoothness of the **law-fiber map** $q$ is a genuine unstated hypothesis (R1.6(b)), and the manuscript does not have the connection-relative criterion (P3) that makes the constancy obligation checkable. |
| Incorrect positivity claim when the horizontal defect is nonzero | **REJECTED as an error, SUSTAINED as a gap** | `thm:pb-pullback-fisher-defect` and `cor:pb-meta-perceived-geometry` both carry the guard $\mathcal D\Psi=0$; `06_general_coarsegraining.tex` and `07_general_renormalization.tex` and `08_infogeometry.tex` all guard their cross-references. No unguarded positivity assertion was found. What is missing is the quantified retained terms $-\mathcal X_\Psi-\mathcal Q_\Psi$ of (R3.3), the exact criterion and margin of Theorem R3.4, and the strict-negativity witness. |
| Untyped composition | **SUSTAINED** | `thm:pb-fisher-defect-cocycle` declares neither base maps, nor connections, nor sections for its two arrows, and its concluding base-cocycle sentence uses an undefined hypothesis. The horizontal-defect composition law (R4.1) and the scale-connection cocycle (R4.3) are absent from the manuscript entirely. |
| Undefined load-bearing hypothesis "connection-compatible" | **SUSTAINED** | The phrase occurs at five places (`05c` chapter opening, `fig:pb-pullback-naturality` caption, `thm:pb-fisher-defect-cocycle`, `06_general_coarsegraining.tex` after `thm:cg-fisher-contraction`, `08_infogeometry.tex` "what is not claimed") and is defined nowhere. Theorem R4.2(3) supplies the exact criterion. |
| Conflation of passive gauge invariance with connection independence | **REJECTED** | `sec:pb-connection-dependence`, the remark after `thm:pb-pullback-gauge-invariance`, `eq:pb-connection-dependence-example`, and the `appendix_notation.tex` entry all separate them explicitly and correctly. |
| Residual conflation of passive covariance with active gauge invariance | **SUSTAINED (naming and status)** | Proposition R2.2(ii) and `CE-ACTIVE-GAUGE-PULLBACK`. The theorem's hypothesis is correct; its title and `ESTABLISHED` tag invite the stronger false reading, and the theorem's mathematical content is a consistency check on the local formulas rather than an independent invariance result. |
| Type defect in the connection convention $D_A=d+\widehat\rho_{x*}(A)$ for nonlinear law fibers | **SUSTAINED** | Lemma R2.1. The **sign** the convention fixes is independently verified correct; only the object is mistyped. |
| Missing $\bar G$-invariance of the coarse Fisher metric in the Markov positivity proof | **SUSTAINED** | R3.5, "Why hypothesis (ii) is not redundant": the local representative of $\Psi$ carries a $c$-dependent gauge factor whose cancellation requires coarse invariance, which is not implied by (I) plus fine invariance. |
| Missing family closure | **SUSTAINED (minor)** | `sec:pb-fisher-defect` presupposes $N_\star(\mathcal B)\subseteq\bar{\mathcal B}$ without naming it. |
| Missing cross-scale channel-weight condition | **SUSTAINED** | R7.3 and `CE-COARSE-WEIGHTS`. |
| Loose citation of the constant-rank theorem | **SUSTAINED (minor)** | `thm:pb-pullback-rank-quotient` cites "the constant-rank theorem"; the result used is the constant-rank theorem for **vector-bundle morphisms**, a different statement from the constant-rank theorem for smooth maps. |
| Correctness of `eq:pb-covariant-jet-chain-rule` | **REJECTED (the equation is correct)** | Theorem R3.2. |
| Correctness of `eq:pb-fisher-defect-cocycle` (the vertical algebraic cocycle) | **REJECTED (the equation is correct)** | Theorem R4.3(2). |
| Correctness of `prop:pb-contact-null-counterexample` and `eq:pb-rank-jump-example` | **REJECTED (both witnesses are correct)** | R2.4 sharpness witnesses, recomputed with exact signs. |
| Correctness of `cor:pb-coarse-null-map` | **REJECTED (the corollary is correct)** | Set $D^\omega sX=0$ in (R3.2) with $A_\Psi=0$. |

### 10.2 Attacks against the stale prior note `sources/manuscripts/gauge-vfe-rg-pullback-geometry-2026-08-01.md`

The note is treated as a target, never as authority.

1. **"Under the stated equivariance hypotheses these tensors are global and
   invariant under passive gauge changes."** The globality half is **refuted as
   stated** by `CE-NO-GLOBAL-SECTION`: equivariance hypotheses do not produce a
   global section, and without a global section there is no global base tensor.
   The correct statement is that the tensors are defined exactly on the domain of
   the chosen section, and are global precisely when $E$ admits a global section,
   which is a topological condition on $(P,\rho,\mathcal B)$.
2. **"Under related sections and compatible connections, the corresponding typed
   base identity is $\delta_{02}=\delta_{01}+f_{01}^*\delta_{12}$."** **Narrowed.**
   By Theorem R4.3, the cocycle (R4.4) requires only stage-one compatibility
   $A_{\Psi_{01}}(s_0;\cdot)=0$, while the reading of $\delta_{12}$ as
   $h_1-f_{12}^*h_2$ additionally requires stage-two compatibility. The note's
   single undifferentiated phrase "compatible connections" merges two hypotheses
   with different domains, and the note supplies no definition of the phrase.
3. **"Without those hypotheses the exact formula retains a vertical mismatch
   term."** **Narrowed and quantified.** The retained object is not one term: at
   the level of the base tensors it is $-\mathcal X_\Psi-\mathcal Q_\Psi$ of
   (R3.3), whose sum can make the fine-minus-coarse comparison negative definite
   (Theorem R3.4(3)). "Retains a vertical mismatch term" understates what is lost:
   the *order relation* is lost, not merely an equality.
4. **Uncontested.** The note's separation of passive gauge invariance from
   connection dependence, its radical and rank statements, its
   quotient-manifold caveats, and its statement that the vertical defect equals a
   conditional covariance are consistent with R2.4 and R3.5 and are not attacked.

## 11. Dispositions for the Task 10 claims in scope

| Claim ID | Disposition | Basis, or exact missing lemma |
| --- | --- | --- |
| `bundle-morphism-descent` | **PROVED**, with one scope correction | Theorem R1: given the declared equivariant $\mathcal P$ over $\kappa$, descent holds **iff** the law-fiber intertwining (I) holds; smoothness follows from smoothness of $q$ and the submersion property of the associated-bundle quotient. Scope correction: the ledger wording "globally defined only after the principal map is $G$-equivariant" states a necessity that does not hold detached from the declared $\mathcal P$ (R1.6(a)). The three-fold typing $N$ / $N_\star$ / $\Psi$ is proved strict by Lemma 2.1. |
| `bundle-fisher-defect` | **PROVED** under two hypotheses the ledger does not carry | Theorem R3.5: $\Delta_F^\Psi\succeq0$ and equals the conditional score covariance. The two required additions are **family closure** $N_\star(\mathcal B)\subseteq\bar{\mathcal B}$ and **$\bar G$-invariance of $\bar g^F$**; the latter is not implied by (I) plus fine-side invariance and is what makes the $c$-dependent gauge factor $\widehat{\bar\rho}(\varsigma(c))$ in the local representative of $\Psi$ cancel. |
| `bundle-scale-cocycle` | **PROVED** | Ordered composition holds separately and compatibly at five typed levels: $f_{02}=f_{12}f_{01}$; $\kappa_{02}=\kappa_{12}\kappa_{01}$; $\mathcal P_{02}=\mathcal P_{12}\mathcal P_{01}$; $q_{02}=q_{12}q_{01}=(N_{01}N_{12})_\star$ by Chapman–Kolmogorov; and $\Psi_{02}=\Psi_{12}\Psi_{01}$ by Theorem R1. The rightmost factor acts first at every level. Theorem R4.1 adds the ordered law for the horizontal defect and Theorem R4.2(4) the exact cocycle for the scale-connection defect form. |
| `horizontal-defect-anomaly` | **PROVED** | Theorem R3.2 (exact first jet, certifying `eq:pb-covariant-jet-chain-rule`); Theorem R3.3 (exact signed comparison (R3.3) and its cubic analogue (R3.4)); Theorem R3.4 (exact positivity criterion, quantitative margin, and a strict-negativity witness with a genuine Markov channel and exactly related sections); Theorem R4.1 (ordered composition); Theorem R4.2 (frame-twist representation and the sharp isotropy criterion for vanishing). |
| `pullback-compatibility` | **PROVED as a conditional theorem; the unconditional order relation is REFUTED** | Theorem R3.5 proves $h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}=\delta_\Psi\succeq0$ under $A_\Psi(s;\cdot)=0$. Theorem R3.4(3) refutes the corresponding statement without that hypothesis by an explicit instance in which every other hypothesis holds and the difference is $-a^2dx^2\prec0$. The ledger's clause "without the commutative first-jet square, the vertical mismatch term is retained" is upheld but must be replaced by the exact retained tensors $-\mathcal X_\Psi-\mathcal Q_\Psi$. |
| `configuration-projectability` | **PROVED** | Theorem R5 gives (P1) $\Leftrightarrow$ (P2) $\Rightarrow$ (P3), with (P3) $\Rightarrow$ (P2) under connected fibers, and shows smoothness of the descent is automatic under a surjective submersion. Theorem R5.2 proves that a pointwise bundle morphism does not induce a map on all section configurations whenever a collapsed direction and a nonannihilated vertical direction exist. `CE-SECTION-DESCENT` is reconstructed exactly; `CE-NONSMOOTH-DESCENT` shows the submersion hypothesis is load-bearing. |
| `configuration-map` | **OPEN.** Missing lemma, stated exactly | Everything needed to type the **domain** of the pointwise-induced configuration coarse map is proved (Theorem R5, Theorem R5.2): the domain is $\Gamma_{\mathrm{proj}}(\Psi)$, the zero set of the first-order operator $Q\mapsto\big(T^V\Psi\circ D^\omega Q+A_\Psi(Q;\cdot)\big)\big|_{\ker Tf}$. What remains unproved is: **Missing Lemma CM.** *Under stated hypotheses on $(f,\Psi,E,\bar E)$, $\Gamma_{\mathrm{proj}}(\Psi)\cap\mathcal Q_\ell$ is a smooth submanifold of the declared configuration manifold $\mathcal Q_\ell$, and the induced map $\Gamma_{\mathrm{proj}}(\Psi)\cap\mathcal Q_\ell\to\mathcal Q_{\ell+1}$, $Q\mapsto\bar Q$, is smooth with a well-defined tangent map.* This requires a transversality or elliptic-regularity hypothesis making the operator a submersion onto its image in the relevant section space, plus the manifold structures of `hyp:hist-regular-section-space`. Neither is available in the current source, and this route does not supply it. |
| `configuration-fisher-metric` | **OPEN.** Missing lemma, stated exactly | The **separation** required by the brief is proved (R6.1): (G1) and (G2) are tensors on different manifolds, (G1) needs a connection and (G2) does not, and (G2) needs $(\mu,w,\text{topology},\text{gauge quotient})$ that the principal bundle does not supply. The Fisher **contraction** input for (G2) is not established here. **Missing Lemma CFM.** *On a declared infinite-dimensional section manifold $\mathcal Q$, the weighted integral $\mathsf G^F$ is a **strong** Riemannian metric — that is, the musical map $T_Q\mathcal Q\to T_Q^*\mathcal Q$ is a linear isomorphism — under explicit hypotheses on $\mu$, $w$, the model $\mathcal B$, and the topology of $\mathcal Q$; and either $\mathsf G^F=\iota^*G^F_{\mathfrak R}$ for a declared joint-law lift, or the block-orthogonality hypothesis under which the weighted product of marginal Fisher metrics equals that joint pullback holds.* `hyp:hist-regular-metric-domain` and `hyp:hist-exact-vfe-lift` in `05d_relational_inference.tex` declare exactly these as hypotheses; no proof exists in the source and none is produced here. Note also `eq:hist-finite-design-clock-speed`, which already proves the finite-design product form is **degenerate** on the full section space, so the missing lemma cannot be discharged by the finite-design construction. |

**Out-of-scope claims, with the bounds this route establishes.**
`score-action-compatibility` is not adjudicated. For the three history claims, the
only bound produced here is negative and already present in the source:
Theorem R3.5 compares a fine section with its own $\Psi$-image on a fixed base and
says nothing about independently recomputed vector fields; the semiconjugacy
condition of `prop:hist-oriented-semiconjugacy` is logically independent of every
result above, and `sec:pb-boundary` in `05c` correctly marks that as `OPEN`.

## 12. External theorems used, with their standard statements

Each is used with hypotheses mapped explicitly in the proof that invokes it. None
is taken from vault prose; the vault notes were read only to confirm which
primary monograph carries each statement.

1. **Quotient by a free proper action / passing smoothly to the quotient.** If
   $\pi:M\to N$ is a surjective smooth submersion and $F:M\to Z$ is smooth and
   constant on the fibers of $\pi$, there is a unique smooth $\tilde F:N\to Z$
   with $\tilde F\circ\pi=F$. Used in Theorem R1(2) and Theorem R5. Standard
   smooth-manifold theory.
2. **Principal-bundle connection calculus:** horizontal lifts, the local
   connection form and its gauge law $A'=\operatorname{Ad}_{a^{-1}}A+a^{-1}da$,
   the transformation $v^*\bar\omega=\operatorname{Ad}_{\varsigma^{-1}}(f^*\bar u^*\bar\omega)+\varsigma^{-1}d\varsigma$
   for $v=\bar u\circ f\cdot\varsigma$, and the correspondence between horizontal
   $\operatorname{Ad}$-equivariant forms on $P$ and $\operatorname{Ad}(P)$-valued
   forms on the base. Used throughout Sections 4–6.
   Primary source: Kobayashi and Nomizu, *Foundations of Differential Geometry I*
   (1963), Chapter II. The vault note
   `sources/refs/kobayashi-nomizu-1963-foundations.md` confirms the chapter
   attribution; the theorem statements above are checked directly against the
   standard formulation, not against that note.
3. **Constant-rank theorem for vector-bundle morphisms.** A smooth vector-bundle
   morphism of locally constant rank has smooth kernel and image subbundles. Used
   in Theorem R2.4(4).
4. **Frobenius theorem** and the characterization of basic tensors for a simple
   foliation: $h=\varrho^*\hbar$ for a unique $\hbar$ if and only if $\iota_Zh=0$
   and $\mathcal L_Zh=0$ for all $Z$ tangent to the leaves. Used in Theorem R2.4(5).
5. **Obstruction theory for sections of a fiber bundle** over a smooth
   paracompact base: the obstructions lie in $H^{k+1}(\mathcal C;\pi_k(F))$ with
   local coefficients, so a bundle with smoothly contractible fiber admits a
   section. Used in Theorem R2.4(2). The nonexistence half of
   `CE-NO-GLOBAL-SECTION` uses instead the elementary homotopy argument
   $\pi_2(S^3)=0\ne\pi_2(S^2\times S^1)$.
6. **Score projection under a parameter-independent Markov kernel.** For a family
   differentiable in quadratic mean with score $\ell_\theta\in L^2_0$ and a
   parameter-independent kernel $K$, the pushed family is differentiable in
   quadratic mean with score $\mathbb E[\ell_\theta(X)\mid Y]$, and
   $I_{\mathsf X}-I_{\mathsf Y}=\mathbb E\operatorname{Cov}(\ell_\theta(X)\mid Y)\succeq0$
   with equality exactly when the score is $\sigma(Y)$-measurable. Used in
   Theorem R3.5. This is the statement the manuscript already proves and cites at
   `thm:cg-fisher-contraction`; the primary sources are the parametrized-measure-model
   treatment of Ay, Jost, Lê, and Schwachhöfer and the classical monotonicity
   results going back to Chentsov.
7. **Chentsov-type invariance** of the Fisher metric and the Amari–Chentsov
   tensor under sufficient statistics, of which invariance under a bimeasurable
   parameter-independent sample bijection is the special case used in Lemma R2.3
   and in `prop:pb-statistical-tensor-descent`. Primary sources: Chentsov (1982)
   for the finite case, Ay–Jost–Lê–Schwachhöfer (2017) for the measure-theoretic
   case. **Scope note:** the vault note
   `sources/refs/cencov-1982-statistical-decision-rules.md` contains the project
   framing sentence "because the metric is invariant under coarse-graining by
   sufficient statistics, it behaves well under the aggregation operations …
   coarse-graining beliefs across scales preserves the canonical geometry." That
   framing is **not** used here and is not supported by the theorem: invariance
   holds under sufficient statistics, while a general Markov morphism gives only
   monotone decrease. Theorem R3.5 uses the monotonicity form, and Theorem R3.4(3)
   shows that even monotonicity does not survive transport to the base when the
   horizontal defect is nonzero.

## 13. Oracle erasure, independent reconstruction, and limitations

**Oracle erasure.** The affirmative-existence instruction in the commissioning
brief was removed from the logical context before the dispositions in Section 11
were fixed, and every proof in Sections 3–8 was re-read for direct or paraphrased
dependence on it. No premise, assumption, proof step, evidence line, or
disposition invokes it. Two dispositions are negative or partial
(`pullback-compatibility` refuted as an unconditional order relation;
`configuration-map` and `configuration-fisher-metric` open with named missing
lemmas), and five sustained attacks are recorded against the current source, which
is inconsistent with a prior-driven record. Passing this check shows only that the
prior was unnecessary; it proves no theorem.

**Independent reconstruction performed inside this pass.** Each of the three
register witnesses touching this route was recomputed from its typed data rather
than from the register's prose, and the recomputed values were compared against
the register text: `CE-HORIZONTAL-ANOMALY` reproduces $h-f^*\bar h=-a^2dx^2$ with
source horizontal field $\partial_x$ and target field $\partial_x+a\partial_\mu$
(Theorem R3.4(3)), and was independently cross-checked against the general
formula (R3.3) and against the frame-twist representation (R4.2) — three routes
agreeing on the same sign and coefficient. `CE-SECTION-DESCENT` reproduces the
failure of (P3) for $Q(x)=\mathcal N(\sin x,1)$ over the $S^1$ collapse
(Section R7.2). `eq:pb-connection-dependence-example` reproduces $h^{A'}=a_0^2dx^2$
as a pure frame-twist semimetric (Section R6.1). This is a within-pass
reconstruction and does not constitute an independent agent's reconstruction; the
Task 15 obligation is unaffected.

**Limitations, separated by kind.**
* *Theorems.* R1, R2.1–R2.4, R3.1–R3.5, R4.1–R4.3, R5, R5.2, R5.3 are proved
  above from the declared hypotheses. Their scope is the finite-dimensional
  smooth tier of `hyp:geo-smooth-tier` and `hyp:pb-regular-models`; nothing here
  extends to stratified, changing-support, or infinite-dimensional law fibers.
* *Constructions.* $\mathfrak A_{\mathcal P}$, $\mathcal X_\Psi$, $\mathcal Q_\Psi$,
  $\mathfrak k_{\bar\beta}$, and $\Gamma_{\mathrm{proj}}(\Psi)$ are typed objects
  introduced here. They are definitions plus the proved identities that use them;
  no independent existence or genericity claim is attached to any of them.
* *Counterexamples.* The five new register candidates in Section 9 are typed
  witnesses with explicit computations; they are certified within this pass and
  proposed, not entered, as register rows.
* *Modeling postulates.* None is made. The identification of $\mathcal C$ with any
  physical or contextual entity, of the scale index with any duration, and of any
  Fisher length with any clock reading lies outside every statement above.
* *Numerical observations.* None. This pass ran no computation.
* *Analogy.* No result is transferred by analogy. In particular, the structural
  parallel between the within-scale term $R^s_a$ and the cross-scale term
  $A_\Psi$ in Section R6.1 is a proved identity of the form
  $\vartheta\circ(\text{an }\operatorname{Ad}\text{-type one-form})$ in both cases
  (Theorem R4.2(2) and `eq:pb-connection-difference-vertical`), not a suggestive
  resemblance; it does **not** license transferring any statement about one to
  the other.
* *Out of scope.* `score-action-compatibility` and the three history claims are
  not adjudicated. No claim about the existence of an infinite-dimensional
  section manifold, a strong configuration metric, a natural-gradient vector
  field, an orbit, or a duration is made or implied.

## 14. Second pass on this route: provenance and relation to Sections 0–13

Sections 0–13 above are the first pass of this route. Sections 14–21 are a second
pass at the same base revision `02d5d8f542cba2d92c6a430483b62155dd5f2db4`, run
independently from the frozen contract and re-deriving Sections 3–8 before reading
them. The second pass reproduced Theorem R3.3 (the exact signed comparison),
Theorem R3.5 (the $A_\Psi=0$ positivity theorem), Theorem R4.1 (the ordered
composition law), Theorem R4.3 (the base cocycle), Theorem R5 (sharp
projectability), and the `CE-HORIZONTAL-ANOMALY` and `CE-SECTION-DESCENT`
reconstructions, in every case with the same signs and coefficients. Those
agreements are recorded here as an independent re-derivation and are not restated.

This pass reads the same sources bound in Section 0; their SHA-256 values were
recomputed and match byte for byte. It adds six results that the first pass does
not contain, supplies the executed arithmetic that the first pass explicitly did
not run, and reconciles two dispositions. It edits nothing else and performs no
Git mutation, no TeX build, and no ledger or register write.

Notation follows Sections 2–8 throughout: $N$ is the sample-space Markov kernel,
$N_\star$ its induced law map, $q=N_\star|_{\mathcal B}$ the law-fiber map,
$\kappa:G\to\bar G$ the Lie-group homomorphism, $\mathcal P:P\to\bar P$ the
principal scale map, $\Psi$ the associated-bundle morphism, $A_\Psi$ the
horizontal defect, and $\delta_\Psi,\mathcal X_\Psi,\mathcal Q_\Psi$ the three
base tensors of (R3.3).

## 15. Result R7 — existence obstruction for the equivariant principal scale map

Theorem R1 and the ledger clause for `bundle-morphism-descent` both begin from a
**declared** equivariant $\mathcal P$ covering $f$. Section R1.6(a) correctly notes
that necessity statements detached from that declaration do not hold. Neither pass
of the source, nor `07_general_renormalization.tex`, asks the prior question: for
given $(f,\kappa,P,\bar P)$, when does such a $\mathcal P$ exist at all. It is a
topological condition, and it can fail.

**Theorem R7 (descent obstruction).** Let $f:\mathcal C\to\bar{\mathcal C}$ be
smooth, $\kappa:G\to\bar G$ a Lie-group homomorphism, and $P\to\mathcal C$,
$\bar P\to\bar{\mathcal C}$ principal bundles. Write $P\times_\kappa\bar G$ for the
extension $(P\times\bar G)/G$ under $(u,\bar g)\cdot g=(u g,\kappa(g)^{-1}\bar g)$,
with right $\bar G$-action $[u,\bar g]\cdot\bar h=[u,\bar g\bar h]$. Then a smooth
$\kappa$-equivariant $\mathcal P:P\to\bar P$ covering $f$ exists **if and only if**

$$
P\times_\kappa\bar G\;\cong\;f^*\bar P
\qquad\text{as principal }\bar G\text{-bundles over }\mathcal C,
\tag{R7.1}
$$

equivalently if and only if $\kappa_*[P]=f^*[\bar P]$ in the nonabelian Čech set
$\check H^1(\mathcal C;\underline{\bar G})$. The correspondence between such
$\mathcal P$ and such isomorphisms is bijective.

*Types.* $\mathcal P\in C^\infty(P,\bar P)$ with
$\mathcal P(ug)=\mathcal P(u)\kappa(g)$ and $\bar\pi\circ\mathcal P=f\circ\pi$;
$\Theta$ an isomorphism of principal $\bar G$-bundles over $\operatorname{id}_{\mathcal C}$.

*Quantifiers.* For every $u\in P$, $g\in G$, $\bar g\in\bar G$.

*Assumptions.* $P$, $\bar P$ smooth principal bundles; $\kappa$ a Lie-group
homomorphism; $f$ smooth. No connection, no representation, and no statistical
structure is used.

*Proof.* Given $\mathcal P$, put $\Theta([u,\bar g]):=(\pi(u),\mathcal P(u)\bar g)$.
This is well defined because
$\Theta([ug,\kappa(g)^{-1}\bar g])=(\pi(u),\mathcal P(ug)\kappa(g)^{-1}\bar g)
=(\pi(u),\mathcal P(u)\kappa(g)\kappa(g)^{-1}\bar g)=(\pi(u),\mathcal P(u)\bar g)$,
it lands in $f^*\bar P$ because $\bar\pi(\mathcal P(u)\bar g)=f(\pi(u))$, it is
$\bar G$-equivariant, and it covers $\operatorname{id}_{\mathcal C}$. Every
$\bar G$-bundle morphism over the identity is an isomorphism, so (R7.1) holds.
Conversely, given $\Theta$, put $\mathcal P(u):=\operatorname{pr}_{\bar P}\Theta([u,\bar e])$.
Since $[ug,\bar e]=[u,\kappa(g)]=[u,\bar e]\cdot\kappa(g)$, equivariance of $\Theta$
gives $\mathcal P(ug)=\mathcal P(u)\kappa(g)$, and $\mathcal P$ covers $f$ by
construction. The two assignments are mutually inverse. In Čech terms, if $P$ has
cocycle $(T_{ij})$ then $P\times_\kappa\bar G$ has cocycle $(\kappa\circ T_{ij})$,
and $f^*\bar P$ has cocycle $(\bar T_{\alpha\beta}\circ f)$ on the pulled-back
cover; (R7.1) is exactly the equality of the two classes. $\square$

**Register candidate `CE-NO-PRINCIPAL-MAP`.** Take
$\mathcal C=\bar{\mathcal C}=S^2$, $f=\operatorname{id}$, $G=\bar G=U(1)$,
$\kappa=\operatorname{id}$, $P$ the Hopf bundle ($c_1=1$), $\bar P$ trivial
($c_1=0$). Any $U(1)$-equivariant $\mathcal P:P\to\bar P$ over
$\operatorname{id}_{S^2}$ is fiberwise a morphism of $U(1)$-torsors, hence
bijective, hence a principal-bundle isomorphism, forcing $c_1(P)=c_1(\bar P)$.
So no $\mathcal P$ exists, and by Theorem R1 no associated-bundle morphism of the
induced form $\Psi[u,\beta]=[\mathcal P(u),q(\beta)]$ exists in either channel,
for **any** intertwining $q$ whatsoever. *Assumption boundary:* every hypothesis of
`hyp:geo-smooth-tier` and `hyp:pb-regular-models` can hold; only (R7.1) fails.
*Proposed status:* CANDIDATE.

*Falsification.* Exhibit a $\kappa$-equivariant $\mathcal P$ covering $f$ with
$\kappa_*[P]\ne f^*[\bar P]$; or a $\bar G$-bundle morphism over the identity that
is not an isomorphism.

*Anchors needing repair.* `07_general_renormalization.tex:236-241`
(`eq:rg-principal-scale-map`) posits $\mathcal P_\ell$ by fiat and never records
that its existence is constrained. This is the one place in the manuscript where an
unstated global-triviality assumption would be invisible: if $P_\ell$ and
$P_{\ell+1}$ are silently trivial, (R7.1) is automatic and the obstruction
disappears. `hyp:geo-common-trivializations` (`02_geometry.tex:533-544`) is the
manuscript's declared triviality hypothesis and is **not** invoked at
`:236-241`. The repair is to state (R7.1), or to invoke that hypothesis explicitly
where the scale diagram is built. Note this is a different finding from the first
pass's `CE-NO-GLOBAL-SECTION`, which concerns existence of a **section of the
associated bundle**; R7 concerns existence of the **principal scale map** itself,
one level earlier in the construction.

## 16. Result R8 — a general bundle morphism has no global fiber representative

Section R3.5 ("Why hypothesis (ii) is not redundant") computes the local
representative $\psi_c=\widehat{\bar\rho}(\varsigma(c))\circ q$ of a morphism that
is **already assumed** to be of the induced form. The converse structure question
is not addressed anywhere: given only that $\Psi$ is a smooth bundle morphism over
$f$, does the phrase "the fiber map underlying $\Psi$" denote?

**Theorem R8 (structure of the frame representatives).** Let $\Psi:E\to\bar E$ be
any smooth bundle morphism covering $f$, and let $\mathcal P$ be a
$\kappa$-equivariant principal map covering $f$ (Theorem R7). For $u\in P_c$ define
$q_u:\mathcal B\to\bar{\mathcal B}$ by $\Psi([u,\beta])=[\mathcal P(u),q_u(\beta)]$,
which is well defined because $\bar\beta\mapsto[\mathcal P(u),\bar\beta]$ is a
bijection onto $\bar E_{f(c)}$. Then

$$
q_{ug}\;=\;\widehat{\bar\rho}(\kappa(g))^{-1}\circ q_u\circ\widehat\rho(g)
\qquad\text{for every }g\in G,
\tag{R8.1}
$$

so $u\mapsto q_u$ is a section of the associated bundle
$P\times_G\operatorname{Map}(\mathcal B,\bar{\mathcal B})$ with action
$q\mapsto\widehat{\bar\rho}(\kappa(g))^{-1}\circ q\circ\widehat\rho(g)$. On a
connected base, $q_u$ is independent of $u$ **if and only if** it satisfies the
intertwining (I) of Theorem R1. Consequently a single global fiber map underlies
$\Psi$ exactly when $\Psi$ is of the induced form, and otherwise $T^V\Psi$ is
represented by a genuinely base-point-dependent family $T q_u$.

*Proof.* $[\mathcal P(ug),q_{ug}(\beta)]=\Psi([ug,\beta])=\Psi([u,\widehat\rho(g)\beta])
=[\mathcal P(u),q_u(\widehat\rho(g)\beta)]$, while
$[\mathcal P(ug),\bar\beta]=[\mathcal P(u)\kappa(g),\bar\beta]
=[\mathcal P(u),\widehat{\bar\rho}(\kappa(g))\bar\beta]$. Equating the
$\bar{\mathcal B}$-coordinates gives (R8.1). Fiberwise constancy is
$q=\widehat{\bar\rho}(\kappa(g))^{-1}\circ q\circ\widehat\rho(g)$ for all $g$, which
is (I); constancy across fibers on a connected base is then constancy of the
corresponding section. $\square$

*Types.* $q_u\in\operatorname{Map}(\mathcal B,\bar{\mathcal B})$ for each $u\in P$;
$u\mapsto q_u$ a section of $P\times_G\operatorname{Map}(\mathcal B,\bar{\mathcal B})$.

*Quantifiers.* Every $c\in\mathcal C$, $u\in P_c$, $g\in G$, $\beta\in\mathcal B$.

*Falsification.* A bundle morphism over $f$ possessing a global fiber
representative that does not intertwine; or a $u$-dependent family violating
(R8.1).

*Consequence, and how it changes the reading of `sec:pb-fisher-defect`.*
`05c_pullback_geometry.tex:674-679` and `:687-690` impose the Markov hypothesis on
"the fiber map underlying $\Psi$", where $\Psi$ was introduced at `:575-582` as no
more than "a smooth bundle morphism over $f$". By R8 that object need not exist,
so the hypothesis is not satisfiable as literally written for a general morphism.
Two admissible repairs: import Theorem R1 and R7 so that $\Psi$ is induced; or
weaken to the pointwise hypothesis of Theorem R9 below, which is strictly more
general and still yields positivity. The first pass's finding that
"connection-compatible" is undefined at five sites (Section 10.1) and this finding
are independent defects of the same passage.

## 17. Result R9 — sample-kernel equivariance implies law-fiber intertwining

The first pass's `CE-LAW-VS-KERNEL-EQUIVARIANCE` shows that law-level intertwining
does not constrain the kernel. The forward direction, in the $\kappa$-twisted form
needed when the two levels carry different groups, is not recorded there and is not
in the manuscript either: `prop:cg-equivariant-channels`
(`06_general_coarsegraining.tex:435-450`) proves it for one group with
$\kappa=\operatorname{id}$ and states no closure hypothesis.

**Proposition R9 (forward implication, twisted form).** Assume the family-closure
hypothesis $N_\star(\mathcal B)\subseteq\bar{\mathcal B}$ and

$$
N\big(\rho(g)x,\;\bar B\big)=N\big(x,\;\bar\rho(\kappa(g))^{-1}\bar B\big)
\qquad\text{for all }g\in G,\ x\in\mathsf K,\ \bar B\in\bar{\mathscr K}.
\tag{R9.1}
$$

Then $q=N_\star|_{\mathcal B}$ satisfies the intertwining (I) of Theorem R1, so
$\Psi[\mathcal P,q]$ descends. The converse fails.

*Proof.*
$(q\circ\widehat\rho(g))(\beta)(\bar B)=\big((\rho(g)_\#\beta)N\big)(\bar B)
=\int N(\rho(g)x,\bar B)\,\beta(dx)
=\int N\big(x,\bar\rho(\kappa(g))^{-1}\bar B\big)\beta(dx)
=(\beta N)\big(\bar\rho(\kappa(g))^{-1}\bar B\big)
=\big(\widehat{\bar\rho}(\kappa(g))\,q(\beta)\big)(\bar B)$.
Measurability of the integrand and finiteness are immediate for a normalized
kernel and a probability measure, so no interchange beyond the definition of the
pushforward is used. The converse fails by `CE-LAW-VS-KERNEL-EQUIVARIANCE`, and
also by the following minimal witness: $\mathsf K=\bar{\mathsf K}=\mathbb R$,
$G=\bar G=\{\pm1\}$, $\kappa=\operatorname{id}$, $\rho$ the sign flip,
$\bar\rho$ **trivial**, $\mathcal B=\{\mathcal N(0,\sigma^2):\sigma>0\}$ (pointwise
$\widehat\rho$-fixed), $N(x,\cdot)=\delta_{x+1}$. Then
$\bar{\mathcal B}=\{\mathcal N(1,\sigma^2)\}$ is pointwise
$\widehat{\bar\rho}$-fixed, so (I) holds on both sides trivially, while (R9.1)
fails at every $x\ne0$ because $\delta_{-x+1}\ne\delta_{x+1}$. $\square$

*Types.* $N$ a normalized Markov kernel $\mathsf K\rightsquigarrow\bar{\mathsf K}$;
$N_\star:\mathcal P(\mathsf K)\to\mathcal P(\bar{\mathsf K})$; $q$ its restriction.

*Falsification.* A kernel satisfying (R9.1) and closure whose induced $q$ violates
(I); or a proof that (I) implies (R9.1), which the witness forbids.

*Anchors needing repair.* `06_general_coarsegraining.tex:435-450` should carry the
$\kappa$-twisted form (R9.1) and the closure hypothesis, and should record at that
location that the implication is strictly one-way. `02_geometry.tex:714-715` states
the one-wayness in prose without a witness.

## 18. Result R10 — pointwise Markov representability suffices

**Theorem R10 (pointwise Markov positivity).** Let $\Psi:E\to\bar E$ cover $f$,
with $\bar g^F$ positive definite and $\widehat{\bar\rho}(\bar G)$-invariant.
Suppose only that for **each** $e=[u,\beta]\in E$ the frame representative $q_u$ of
Theorem R8 satisfies $q_u=(N_u)_\star|_{\mathcal B}$ for some normalized
parameter-independent Markov kernel $N_u$ with $N_{u\star}(\mathcal B)\subseteq\bar{\mathcal B}$,
and that $\mathcal B$ and its pushed family are differentiable in quadratic mean
with square-integrable scores. Then $\Delta_F^\Psi=g^F-(T^V\Psi)^*\bar g^F$ is a
well-defined element of $\Gamma(E;\operatorname{Sym}^2V^*E)$, it is positive
semidefinite, and for $w\in V_eE$

$$
\Delta_F^\Psi(w,w)=\mathbb E_\beta\operatorname{Var}_\beta\big(\ell_w(X)\mid Y\big)\ \ge\ 0,
$$

with equality if and only if $\ell_w$ is $\sigma(Y)$-measurable $\beta$-almost
surely, where $(X,Y)$ has joint law $\beta(dx)N_u(x,d\bar y)$.

*Proof.* $g^F$, $\bar g^F$, and $T^V\Psi$ are frame-free objects, so
$\Delta_F^\Psi$ is well defined regardless of which $q_u$ represents $\Psi$ at $e$;
only the *representation* by $N_u$ varies with $u$. Fixing $e$ and working in the
frame pair $(u,\mathcal P(u))$, the argument of Theorem R3.5 applies verbatim to
$q_u$ and $N_u$, because that argument is entirely pointwise in $\beta$ and uses
nothing about neighboring base points. The $\bar G$-invariance of $\bar g^F$ is
still required, for the reason given in R3.5. $\square$

*Relation to Theorem R3.5.* R3.5 assumes a single global $q=N_\star|_{\mathcal B}$;
R10 assumes only that each frame representative is a Markov pushforward. Every
hypothesis set admitted by R3.5 is admitted by R10, and by Theorem R8 the converse
inclusion is strict whenever $\Psi$ is not of the induced form. The base
consequences (R3.3), Theorem R3.4, and Theorem R3.5's identity
$h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}=\delta_\Psi$ under $A_\Psi=0$ therefore
hold under R10's weaker hypothesis without change, since (R3.3) is purely algebraic
and uses only that $\Delta_F^\Psi$ is defined.

*Falsification.* An $e$ and $w$ with every stated hypothesis and
$\Delta_F^\Psi(w,w)<0$; or two frames over one base point whose Markov
representatives give different values of $\Delta_F^\Psi$.

*Anchors needing repair.* `05c_pullback_geometry.tex:674-685` states the Markov
hypothesis globally. Restating it pointwise costs nothing and removes the
dependence of `sec:pb-fisher-defect` on the induced form of $\Psi$.

## 19. Result R11 — nonzero horizontal defect with strictly positive base comparison

Theorem R3.4(2) gives a sufficient margin and Theorem R3.4(3) a strict-negativity
witness. Two things are left open there and are settled here: whether the base
comparison can be strictly **positive** with $A_\Psi\ne0$, and whether the margin
(R3.5) is necessary.

**Proposition R11.** There are data satisfying every hypothesis of Theorem R3.5
except (v), that is with $A_\Psi(s;\cdot)\ne0$, for which
$h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}\succ0$. Moreover the margin (R3.5) is
sufficient but **not** necessary: there are data violating (R3.5) for which the
comparison is strictly positive.

*Witness.* $\mathcal C=\bar{\mathcal C}=\mathbb R$, $f=\operatorname{id}$,
$G=\bar G=(\mathbb R,+)$ acting by translation, $\kappa=\operatorname{id}$,
$P=\bar P$ trivial, $\mathcal P=\operatorname{id}$. Fine fiber
$\mathcal B=\{\mathcal N(\mu,1)\}$ with $g^F=1$; kernel $N(x,\cdot)=\mathcal N(x,1)$,
which is normalized, parameter independent, and translation equivariant, so
$\bar{\mathcal B}=\{\mathcal N(\mu,2)\}$, $q(\mu)=\mu$, $T^V\Psi=\operatorname{id}$,
$\bar g^F=\tfrac12$, and $\Delta_F^\Psi=\tfrac12$. Section $\sigma(x)=mx$; source
connection $A=0$; target connection $\bar A=b\,dx$. Then
$D^\omega s=m$, $A_\Psi(s;\partial_x)=b\,\partial_\mu$,
$D^{\bar\omega}\bar s(\partial_x)=m+b$,

$$
h^\omega_s=m^2\,dx^2,
\qquad
f^*\bar h^{\bar\omega}_{\bar s}=\tfrac12(m+b)^2\,dx^2,
\qquad
\delta_\Psi=\tfrac12m^2dx^2,
\quad
\mathcal X_\Psi=mb\,dx^2,
\quad
\mathcal Q_\Psi=\tfrac12b^2dx^2 .
$$

With $m=1$ the comparison is $1-\tfrac12(1+b)^2$, positive exactly for
$|1+b|<\sqrt2$. Exact values, each cross-checked against (R3.3):

| $b$ | $h-f^*\bar h$ | $\delta_\Psi-\mathcal X_\Psi-\mathcal Q_\Psi$ | $\|A_\Psi\|_{\bar g^F}$ | margin (R3.5) | margin met | positive |
| --- | --- | --- | --- | --- | --- | --- |
| $0$ | $1/2$ | $1/2$ | $0$ | $0.2929$ | yes | yes |
| $1/10$ | $79/200$ | $79/200$ | $0.0707$ | $0.2929$ | yes | **yes** |
| $-1/10$ | $119/200$ | $119/200$ | $0.0707$ | $0.2929$ | yes | **yes** |
| $1/2$ | $-1/8$ | $-1/8$ | $0.3536$ | $0.2929$ | no | no |
| $-3/5$ | $23/25$ | $23/25$ | $0.4243$ | $0.2929$ | **no** | **yes** |

Rows two and three prove the first assertion: $A_\Psi\ne0$ and the comparison is
strictly positive. Row five proves the second: the margin is violated
($0.4243>0.2929$) while the comparison is $23/25>0$. Row four is the negative case,
consistent with Theorem R3.4(3). All values are exact rationals; see Section 20.

*Reading, and a correction to the ledger wording.* The clause of
`horizontal-defect-anomaly` that reads "positivity follows only when that defect
vanishes" is false as a biconditional. The correct statement is the one already
proved in the first pass: vanishing of $A_\Psi$ is **sufficient** (Theorem R3.5),
the margin (R3.5) is **sufficient but not necessary** (row five), and the exact
criterion is Theorem R3.4(1),
$\|D^{\bar\omega}\bar s(T_cfX)\|_{\bar g^F}\le\|D^\omega sX\|_{g^F}$ for every $X$.
Nothing in the manuscript asserts the false biconditional; the defect is in the
ledger's phrasing of the claim, and the repair is to restate that clause as
sufficiency plus Theorem R3.4(1).

*Falsification.* A recomputation of any row disagreeing with (R3.3); or a proof
that $A_\Psi\ne0$ forces non-positivity, which rows two, three, and five forbid.

## 20. Executed verification record

The first pass ran no computation. This pass ran the following checks in exact
rational and symbolic arithmetic (Python `fractions` and `sympy`) at the base
revision. Exact agreement is corroboration of the proofs above and the arithmetic
of the witnesses; it closes no theorem.

**Block A — the exact signed comparison (R3.3).** The five rows of Proposition R11
were computed twice, once as $h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}$ directly
and once as $\delta_\Psi-\mathcal X_\Psi-\mathcal Q_\Psi$. All five agree as exact
rationals. The degenerate row $m=0$, $b=1/10$, lossless channel reproduces
`CE-HORIZONTAL-ANOMALY` with value $-1/100=-b^2$, matching Theorem R3.4(3).

**Block B — the ordered composition law (R4.1).** Three levels,
$\mathcal C_0=\mathbb R_x$, $\mathcal C_1=\mathbb R_y$, $\mathcal C_2=\mathbb R_z$,
$f_{01}(x)=2x$, $f_{12}(y)=3y$, $f_{02}(x)=6x$; translation group; trivial bundles;
identity law-fiber maps on the location parameter; $A_{\omega_0}=0$,
$A_{\omega_1}=a_1dy$, $A_{\omega_2}=a_2dz$. Direct computation gives
$A_{\Psi_{01}}(\partial_x)=2a_1$, $A_{\Psi_{12}}(\partial_y)=3a_2-a_1$,
$A_{\Psi_{02}}(\partial_x)=6a_2$. The ordered law predicts
$T^V\Psi_{12}\big(A_{\Psi_{01}}(\partial_x)\big)+A_{\Psi_{12}}\big(\Psi_{01}(e);T f_{01}\partial_x\big)
=2a_1+2(3a_2-a_1)=6a_2$. The symbolic difference is identically zero in
$(a_1,a_2)$.

**Block C — the base cocycle (R4.3) and its identification.** With the Block B
scale data, fine model $\mathcal N(\mu,1)$ and coarse models $\mathcal N(\mu,2)$,
$\mathcal N(\mu,3)$ from two successive unit-variance Gaussian channels, and
sections $\sigma_0(x)=x$, $\sigma_1(y)=y/2$, $\sigma_2(z)=z/6$ (which are exactly
related at both stages),

$$
\delta_{01}=1-\tfrac12(2a_1+1)^2,\qquad
\delta_{12}=\tfrac18(2a_1+1)^2-\tfrac1{12}(6a_2+1)^2,\qquad
\delta_{02}=1-\tfrac13(6a_2+1)^2,
$$

and $\delta_{02}-\big(\delta_{01}+4\delta_{12}\big)=0$ **identically in
$(a_1,a_2)$**, where the factor $4$ is $f_{01}^*$ acting on $dy^2=4dx^2$. Sampled
values:

| $a_1$ | $a_2$ | $\delta_{01}$ | $\delta_{12}$ | $\delta_{02}$ |
| --- | --- | --- | --- | --- |
| $0$ | $0$ | $+0.500000$ | $+0.041667$ | $+0.666667$ |
| $0$ | $1/5$ | $+0.500000$ | $-0.278333$ | $-0.613333$ |
| $1/10$ | $0$ | $+0.280000$ | $+0.096667$ | $+0.666667$ |

At $a_1=a_2=0$ each $\delta$ equals the corresponding $(D s)^*\Delta_F$, checked
exactly as $1/2$, $1/24$, $2/3$. Row two shows the cocycle surviving where
positivity fails at the stages with nonzero horizontal defect. Row three exhibits a
**cancellation** worth recording separately: with $a_2=0$ and $a_1\ne0$ one has
$A_{\Psi_{01}}\ne0$ and $A_{\Psi_{12}}\ne0$ while $A_{\Psi_{02}}=6a_2=0$, so the
composite first-jet square commutes although neither factor square does, and
$\delta_{02}$ is unchanged and still equals the Markov defect $2/3$. Hence
vanishing of the composite defect does **not** imply vanishing of the factor
defects; the converse implication (both factors compatible $\Rightarrow$ composite
compatible) does hold and follows from (R4.1).

**Block D — the two sharpness witnesses of R2.4.** For $\alpha=dz-x\,dy$ the
coefficient of $\alpha\wedge d\alpha$ on $dx\wedge dy\wedge dz$ is $-1\ne0$, so
Frobenius fails while $h=\alpha\otimes\alpha$ has constant rank one; and
$h=4x^2dx^2$ has rank one off the origin and rank zero at the origin. Both agree
with `prop:pb-contact-null-counterexample` and `eq:pb-rank-jump-example`.

**Block E — non-covariance of the naive derivative.** With $G=(\mathbb R,+)$ acting
by translation on $\{\mathcal N(\mu,1)\}$, frame 1 $(\sigma_1\equiv0,A_1=0)$ and the
frame change $a(x)=x$ giving $(\sigma_2=-x,A_2=dx)$: the naive derivatives are $0$
and $-1$ and differ, while the covariant derivatives are $0+0$ and $-1+1$ and
agree. This is the computational form of Proposition R2.2.

**Block F — the coarse-weight witness.** With a lossless belief channel
($h_q=f^*\bar h_{\bar q}$) and $\bar w_b=2w_b$, the belief contribution to
$h^{\mathrm{prod}}-f^*\bar h^{\mathrm{prod}}$ is $-w_b f^*\bar h_{\bar q}\preceq0$,
confirming `CE-COARSE-WEIGHTS` numerically.

## 21. Reconciled dispositions

The second pass adopts the first pass's dispositions in Section 11 except where
noted. Two are strengthened by new results and two clauses are corrected.

| Claim ID | Reconciled disposition | Change relative to Section 11 |
| --- | --- | --- |
| `bundle-morphism-descent` | **PROVED**, with the existence question now answered | Section 11 proves descent *given* a declared $\mathcal P$. Theorem R7 adds the necessary and sufficient condition (R7.1) for $\mathcal P$ to exist, and `CE-NO-PRINCIPAL-MAP` shows it can fail with every smooth-tier hypothesis intact. Theorem R8 adds that "the fiber map underlying $\Psi$" denotes only when $\Psi$ is induced. Proposition R9 adds the $\kappa$-twisted forward implication $N\Rightarrow q$ with its closure hypothesis, complementing `CE-LAW-VS-KERNEL-EQUIVARIANCE`. |
| `bundle-fisher-defect` | **PROVED** under the two hypotheses named in Section 11, and under a strictly weaker third | Unchanged in substance. Theorem R10 weakens the global Markov hypothesis to pointwise frame-representative Markov, which removes the dependence of `sec:pb-fisher-defect` on $\Psi$ being of the induced form. Family closure and $\bar G$-invariance of $\bar g^F$ remain required exactly as in R3.5. |
| `bundle-scale-cocycle` | **PROVED** | Unchanged. Block B of Section 20 supplies executed arithmetic for the ordered law at three levels, including the sign and domain tests. |
| `horizontal-defect-anomaly` | **PROVED**, with one ledger clause corrected | Section 11 marks it PROVED without adjudicating the ledger phrase "positivity follows only when that defect vanishes". Proposition R11 **refutes that phrase as a biconditional**: rows two, three, and five have $A_\Psi\ne0$ and strictly positive comparison. The mathematics of Sections 5–6 is unaffected; the correction is to the claim's wording, which should read "sufficient" plus the exact criterion of Theorem R3.4(1). |
| `pullback-compatibility` | **PROVED as a conditional theorem; the unconditional order relation REFUTED** | Unchanged. Block A of Section 20 supplies the exact arithmetic for both the negative and the positive regimes. |
| `configuration-projectability` | **PROVED**, and its universal strengthening **REFUTED** | Unchanged. The second pass re-derived Theorem R5 and `CE-SECTION-DESCENT` independently and additionally verified that the $S^1$ collapse witness satisfies $A_\Psi=0$ and $\Delta_F^\Psi=0$, so the refutation holds under the strongest available descent hypotheses rather than in a degenerate case. |
| `configuration-map` | **OPEN**, Missing Lemma CM as stated in Section 11 | Unchanged and endorsed. The second pass independently reached the same domain $\Gamma_{\mathrm{proj}}(\Psi)$ and confirms that no smooth-submanifold or tangent-map statement follows from anything proved here. |
| `configuration-fisher-metric` | **OPEN**, Missing Lemma CFM as stated in Section 11 | Unchanged and endorsed. The second pass initially recorded this as conditionally proved on the strength of the connection-independence separation alone; that was an overreach, since the ledger claim requires a **strong** metric on the declared section manifold, which the separation does not supply. Section 11's OPEN with Missing Lemma CFM is the correct disposition and stands. |

**New register candidate from this pass.** `CE-NO-PRINCIPAL-MAP` (Section 15),
proposed as CANDIDATE, attacking any use of `eq:rg-principal-scale-map` that treats
the existence of $\mathcal P_\ell$ as automatic.

**Oracle erasure for the second pass.** The affirmative-existence instruction was
held out of the logical context for the whole of Sections 15–21 and appears in no
premise, hypothesis, proof step, witness, table entry, or disposition. Rescanning
for paraphrased dependence: this pass produced one new obstruction to existence
(R7 with `CE-NO-PRINCIPAL-MAP`), one structure theorem limiting what a general
morphism supplies (R8), one refutation of a ledger clause (R11), and one
self-correction against its own initial reading (`configuration-fisher-metric`),
which is the distribution expected of a prior-free search. Passing this audit shows
only that the prior was unnecessary; it establishes nothing mathematical.

**Limitations of the second pass, by kind.** *Theorems:* R7, R8, R9, R10, R11 are
proved from the declared hypotheses, with the same finite-dimensional smooth-tier
scope as Sections 3–8. *Counterexamples:* `CE-NO-PRINCIPAL-MAP` and the minimal
converse witness in R9 are typed witnesses with explicit computations.
*Numerical observations:* Section 20 is exact rational and symbolic computation used
as corroboration and as the arithmetic of the witnesses; it closes no theorem, and
it is a within-pass check, not an independent agent's reconstruction. *External
theorems:* R7 uses only the elementary theory of principal-bundle extensions and
pullbacks and the fact that a bundle morphism over the identity is an isomorphism;
$c_1$ of the Hopf bundle is used only to separate two $U(1)$-bundles over $S^2$.
*Modeling postulates and operational identifications:* none. *Out of scope:*
`pullback-ledger-provenance` is a mechanical provenance and rerun claim; no rerun
was performed on this route and no disposition is asserted for it.
