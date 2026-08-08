<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 10 — independent information-geometric and configuration-manifold route

Scores, Fisher contraction defects, action-quotient compatibility, configuration
manifolds, joint versus marginal Fisher geometry, configuration coarse-map typing,
and integrated metrics and durations.

This record is an independent certification pass for the Task 10 interface of the
gauge-VFE renormalization remediation. It is written against the frozen problem
contract `contract-sha256-b6f7aee…c526b` and closes each in-scope ledger claim as
`PROVED`, `REFUTED`, or `OPEN` with an exact obligation. Every affirmative closure
rests on a derivation reproduced here; every refutation rests on a typed
counterexample reproduced here. Agent agreement, numerical agreement, and the
existence of a prior narrative are not evidence and are not used as such.

---

## 0. Run metadata, scope, and source binding

### 0.1 Contract binding

| Field | Value |
| --- | --- |
| `schema_version` | `rigorous-theory-search/v1` |
| `contract_id` | `contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b` |
| `target_digest` | `b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b` |
| Base revision | `02d5d8f542cba2d92c6a430483b62155dd5f2db4` (branch `codex/gauge-vfe-rg-task10-pullbacks-20260804`, clean at start) |
| Route label | `FAM-IG-CONFIG` — information-geometric / configuration-manifold route |
| Search prior | `SEARCH_PRIOR_AFFIRMATIVE` is recorded in `problem-contract.target.search_priors` only. It allocated effort to this route; it appears in no premise, assumption, evidence record, claim, dependency edge, certificate, or conclusion below. Section 9.2 records the erasure audit. |

In-scope ledger claims (the twelve outgoing `target -> …` edges of
`dependency-dag.json` lines 26–37 that Task 10 owns): `score-action-compatibility`,
`bundle-fisher-defect`, `bundle-morphism-descent`, `bundle-scale-cocycle`,
`horizontal-defect-anomaly`, `pullback-compatibility`, `configuration-fisher-metric`,
`configuration-map`, `configuration-projectability`, `history-semiconjugacy`,
`history-noncollapse`, `history-duration-relation`.

### 0.2 Source digests bound by this report

This checkout has `core.autocrlf=true`, so the working tree carries CRLF line
terminators while the committed blob content is LF. **Both digests are recorded**,
because the two differ for every text file and the remediation ledger's
`artifact_sha256` fields use the LF-normalized (committed-content) value. Confusing
the two produces spurious drift reports; the recomputation in §0.3 depends on
getting this right.

| Path | Working-tree SHA-256 (CRLF) | Committed-content SHA-256 (LF) |
| --- | --- | --- |
| `manuscripts/gauge_vfe_rg/SPEC.md` | `3557038b57f008a1453f29f3abaa2b8c7ddea822bc610dd6945adc811b97bf2d` | `47043c258d34542d3280e68ca9e83390c8c61dbe2c7e70a17fbed8c6c40a69b0` |
| `manuscripts/gauge_vfe_rg/03_probability.tex` | `1be541dccaf957376cf50c1f4c09da6f7fb67a9d1e74ebf327d408149ccc0e2d` | `ab67aeb0f1574221448d17c2992eb5f91075804781cadd85324b3a419e20f37a` |
| `manuscripts/gauge_vfe_rg/05_elbo.tex` | `a4aa559cc160ae0a2547f8f2b0d929b4e1c51bf2a7c0831e1eb34d2ef3bcf3a4` | `16eb45251ad3ec219a01f0bba1d04d16706b8c8321f3f10749c8eee201bf1b11` |
| `manuscripts/gauge_vfe_rg/05b_local_collective_elbo.tex` | `22d35509fa707e46de71e331df614ccf2aa48572cc456a02ee717a7a9dc39b60` | `fee7c5a90230909e4e5433c31f5f4f20768f7d7661e82082b3228ac67bfb9245` |
| `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex` | `a87bc2b3d7d8d76412a299fbd3220464802bd1cc2d853f1f6c287f96e5a73279` | `4c241c1a810da739732e7201b6bc51fe1412d4fc00761b8019ad38a4b673a8e3` |
| `manuscripts/gauge_vfe_rg/05d_relational_inference.tex` | `138e4f86f107f5bd0307e049dc5368a6c36584a827bf98bf4eb396e30016d0a1` | `6df55b6c7f98ea0c0a3f959be1bfc0988fd4667d315e5c10f8711495a2e0b61a` |
| `manuscripts/gauge_vfe_rg/06_general_coarsegraining.tex` | `a6a60a19a7c263915e749787b12470a84d6fafcaf9d55c69b71c0490c45c064a` | `4e1bd10738bb01941b5d8de35efd2da828ceb3483a530a57c54b6c2e0319155a` |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `a3a7ae2fed2eb4a1ea4668393a69b4d56aa2c9dd071af06ddbcba717d7365797` | `df78fe8d346a0f09c86fea919e844497074458303ea7540f6c08c2f20e343edf` |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `148d9652229eb6d3c40a41b48c1eb938328ca697a37e8113111567c580cc61be` | `e7489104a704a7549c1739449e259770e7f5d041589f7a409a89cfd10ceb9b59` |
| `manuscripts/gauge_vfe_rg/08_infogeometry.tex` | `55bfcdff0eebec24f2231852467255d13a0c02d1369621d04ede53cad3b7c31b` | `2f7cb3a7e10c630f591fdea5a1f5cb1bbcab3d2e2f9e1e521fc5b2d94448ef12` |
| `manuscripts/gauge_vfe_rg/appendix_notation.tex` | `d39936499c9673c1b4ed75ae31bf294f8d4df9fd1fd0cef1dae4a9ec5a572fa4` | `b1ff34b52bb9572dacd2b5b7d522f116faf44b2a4e0f8b42a3d8d99a0ad8671c` |
| `manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex` | `bbb02a24ed0875ff287aa072fddae359f4ccd59058157503d4e93502a4e6b436` | `f324df4b038a6b7f4b94a442bfd3c2234306994bdf6da631b1a967a884512635` |
| `docs/derivations/…/problem-contract.json` | `7cba2e9bbfe34028d6a994359e53c761779bd255c5405bfa3996c50ca575bc22` | `a9e1999c85ee333f23a1aacb90a6a51b526565d1e89f958374201a55d06878de` |
| `docs/derivations/…/claim-ledger.json` | `53d9a2ae2ceab6a20c0486facc68e07bfb66731ebdccdfcc7c87f9890357c5f7` | `effb5663af4e51339464f1765185fb0c35d767b9141614a7f3b0fe28a33099d3` |
| `docs/derivations/…/dependency-dag.json` | `bb296da12424fdd766727f0236aa6b91b1cb8fcfb93e3016882532049a119c16` | `3ac995b8c2a03b770174e78fe9abd06da55eed105a675c02cfa9bd0df3d41dc1` |
| `docs/derivations/…/counterexample-register.md` | `c7e0fa8d576ab60c2d4060f423e4222e800116a0293e0097c8d38ab55e6b6853` | `5d18bbd4d6887a851bd3b5a660568da2a0b675192ab5f9205ca61138e6d96b34` |
| `docs/derivations/…/evidence/task-9-score-dqm-analysis.md` | `7b302f9d7759453068d1791bb90ce86d42c50a261d445cc45301694f8cf2f886` | (not recomputed; not load-bearing below) |
| `sources/manuscripts/gauge-vfe-rg-pullback-geometry-2026-08-01.md` | `e9cb6e4cd360ee477f60459856a33fd76b1f7d17b32f65f7a1dee61345318c68` | `f48cc923205584f61d6205208541efa362c5eff8523d9e4ec2ea09623c3d5923` |
| `docs/superpowers/plans/2026-08-03-gauge-vfe-rg-review-remediation.md` | `9e3d0c64b81a27782729e62f9485ff17eea9e687d79cbdea7b7bed69e94bb36c` | (not recomputed; not load-bearing below) |
| `manuscripts/gauge_vfe_rg/main.pdf` | `83b1d9b92f1cbbd9385e0b965448cefdf561021f8ee72763bf4be7fc0fac01de` | (binary; identical) |

Every line reference below (`file:line`) is to the **working-tree** bytes whose CRLF
digest appears in the left column.

### 0.3 Verification of the stale 2026-08-01 wiki record

`sources/manuscripts/gauge-vfe-rg-pullback-geometry-2026-08-01.md` was supplied as an
object to verify, not as authority. Recomputation gives a split verdict, and the split
matters.

**Confirmed current.** The record's stated digests

- `05c_pullback_geometry.tex`: `4C241C1A…B673A8E3`
- `05d_relational_inference.tex`: `6DF55B6C…A2E0B61A`
- `main.pdf`: `83B1D9B9…0FAC01DE`

reproduce **exactly** as the committed-content digests at `02d5d8f` (§0.2). Both
chapters were added at commit `0af1cbd` and have not been modified since; the tracked
PDF likewise dates from `0af1cbd`. So the record's file-level binding is not stale.

**Confirmed stale.** Three separate staleness findings follow from the same
recomputation and must not be conflated with the above.

1. *Revision binding.* The record binds to an uncommitted working-tree snapshot on
   branch `codex/gauge-vfe-rg-pullback-geometry-20260801` based on `43eb7e7`. The
   present base is `02d5d8f`, twenty-plus commits later. The record is therefore not a
   binding for the current source state, and its "29 PASS, 0 FAIL" verifier count and
   "215 pages" figure are attested only for `43eb7e7`-era inputs.
2. *Rendered artifact.* `main.pdf` at `02d5d8f` is byte-identical to the 2026-08-01
   snapshot, while `03_probability.tex`, `05_elbo.tex`, `05b_local_collective_elbo.tex`,
   `06_general_coarsegraining.tex`, `07_general_renormalization.tex`,
   `07b_agent_network_rg.tex`, `08_infogeometry.tex`, `appendix_notation.tex`, and
   `appendix_claim_ledger.tex` were all modified by the Task 5–9 commits `2a4f7fe`,
   `a2cca53`, `17b59ae`, `3dbe4c6`, and `02d5d8f`. **The tracked PDF does not render the
   current sources.** Any Task 10 conclusion that reads the PDF as evidence for current
   chapter text is invalid. This report reads only `.tex` bytes.
3. *Mathematical content.* One identity in the record is stated with a hypothesis
   weaker than its proof supports. The record asserts (line 264) that "under related
   sections and compatible connections" the base defects compose as
   `δ₀₂ = δ₀₁ + f₀₁* δ₁₂`. The derivation in §1.6 below shows the composition needs
   only `𝒟Ψ₀₁ = 0` along the fine section together with the fine section relation; the
   second arrow's horizontal defect is irrelevant to that identity. The record's
   hypothesis is sufficient but not minimal. This is a scope, not a correctness, defect,
   and `05c_pullback_geometry.tex:779-808` states the vertical cocycle correctly.

### 0.4 What this record is not

This is a derivation record. It runs no code, builds no TeX, and modifies no file other
than itself. It records no numerical observation, so no claim below is closed by
computation. Where an external theorem is used it is named with its hypothesis mapping;
where a result is the manuscript's own, the manuscript is cited as a *location*, never
as independent authority for its own claim.

---

## 1. Pushed scores, family closure, and the exact Fisher contraction defect

### 1.1 Typed setting and the hypotheses that are actually load-bearing

Let $(\mathsf X,\mathscr X)$ and $(\mathsf Y,\mathscr Y)$ be measurable spaces, and let
$\Theta\subseteq\mathbb R^d$ be open with $\theta_0\in\Theta$.

**(H1) Dominated family.** $\{P_\theta\}_{\theta\in\Theta}$ are probability laws on
$\mathsf X$ with $P_\theta\ll\mu$ for one $\sigma$-finite $\mu$, and $p_\theta=dP_\theta/d\mu$
is a fixed jointly measurable version. This is the family-level domination tier of
`H-PROBABILITY`; it is what makes the Hellinger amplitude
$a_\theta:=\sqrt{p_\theta}\in L^2(\mu)$ a single well-defined object across $\theta$.

**(H2) Differentiability in quadratic mean at $\theta_0$.** There is
$\ell_{\theta_0}\in L^2(P_{\theta_0};\mathbb R^d)$ with
$$
\int\Big[\sqrt{p_{\theta_0+u}}-\sqrt{p_{\theta_0}}-\tfrac12\,u^{\!\top}\ell_{\theta_0}\sqrt{p_{\theta_0}}\Big]^2 d\mu
= o(\lVert u\rVert^2),\qquad u\to0 .
$$
The displayed integral is independent of the choice of dominating $\mu$, so (H2) is a
property of the family, not of the chart. Centering $\mathbb E_{\theta_0}\ell_{\theta_0}=0$
is forced, not assumed (`07b_agent_network_rg.tex:550-557`).

**(H3) Parameter-independent normalized Markov kernel.** $K:\mathsf X\rightsquigarrow\mathsf Y$
with $x\mapsto K(x,B)$ measurable for each $B\in\mathscr Y$ and $K(x,\mathsf Y)=1$ for
**every** $x$ — not merely almost every $x$, since the exceptional set would otherwise
depend on $\theta$. $K$ carries no $\theta$ dependence.

**(H4) Joint law and reverse conditioning.** $\mathbb P_\theta(dx,dy)=P_\theta(dx)K(x,dy)$
on $\mathsf X\times\mathsf Y$; $P^Y_\theta:=P_\theta K$ is the $Y$-marginal. Conditional
expectation given $\sigma(Y)$ under $\mathbb P_{\theta_0}$ exists by Radon–Nikodym and
requires **no** standard-Borel hypothesis. A *regular conditional law* $\Pi(dx\mid y)$
does require standard Borel; it is used below only where named.

**(H5) Family closure (the hypothesis the manuscript uses without naming).** There is a
declared coarse smooth parametrized-measure model $\bar{\mathcal B}$ on $\mathsf Y$, and
a map $\varphi$ with $\varphi(P_\theta)=P_\theta K$ for $\theta$ near $\theta_0$, whose
image lies in $\bar{\mathcal B}$.

(H5) is not a formality. `07_general_renormalization.tex:872-874` records the failing
instance in the manuscript's own words: a nonlinear Gaussian pushforward is not in
general Gaussian. Without (H5) the coarse Fisher tensor $\bar g^F$ of a declared coarse
fiber is not evaluated on the pushed path at all, and $T^V\Psi$ has no codomain. This is
the single largest unnamed hypothesis in `05c_pullback_geometry.tex:675-700`, which
opens "Suppose now that the fiber map underlying $\Psi$ is the pushforward of a
parameter-independent Markov kernel *between the two regular statistical experiments*."
The italicized phrase presupposes (H5) and is the only place it is even implied.

### 1.2 Two lemmas that carry the interchange burden

The whole point of formulating (H2) as quadratic-mean differentiability rather than as
pointwise differentiation of $\log p_\theta$ is that **no differentiation under an
integral sign is performed anywhere in §1**. The price is that every conclusion is an
$L^2$-equivalence-class statement. Both halves of that trade are made explicit here.

**Lemma 1.1 (DQM rigidity).** Let $(P_t)_{|t|<t_0}$ and $(P'_t)_{|t|<t_0}$ be paths of
probability laws with $P_0=P'_0=P$, each differentiable in quadratic mean at $t=0$.
(i) If both have the same score $h\in L^2_0(P)$, then the Hellinger distance satisfies
$H(P_t,P'_t)=o(|t|)$. (ii) Conversely, if $(P_t)$ is DQM with score $h$ and
$H(P_t,P'_t)=o(|t|)$, then $(P'_t)$ is DQM with the same score $h$.

*Proof.* Fix any $\sigma$-finite $\nu$ dominating $P$ and all $P_t,P'_t$ (for instance
$\nu=\sum_{n}2^{-n}(P_{t_n}+P'_{t_n})+P$ along a countable set $\{t_n\}$ dense in
$(-t_0,t_0)$, together with the values of $t$ under consideration). Write
$a_t=\sqrt{dP_t/d\nu}$, $a'_t=\sqrt{dP'_t/d\nu}$, $a=\sqrt{dP/d\nu}$. DQM says
$\lVert a_t-a-\tfrac t2 ha\rVert_{L^2(\nu)}=o(|t|)$ and likewise for $a'_t$. The
triangle inequality gives $\lVert a_t-a'_t\rVert_2=o(|t|)$, which is (i), because
$H(P,Q)=\lVert\sqrt{dP/d\nu}-\sqrt{dQ/d\nu}\rVert_{L^2(\nu)}$ is independent of $\nu$.
Statement (ii) is the same triangle inequality read in the other direction. $\square$

**Lemma 1.2 (Markov contraction of Hellinger distance).** For probability laws $P,Q$ on
$\mathsf X$ and a normalized Markov kernel $K$, $H(PK,QK)\le H(P,Q)$.

*Applicable theorem with hypothesis mapping.* Squared Hellinger distance is the
$f$-divergence $D_f(P\Vert Q)$ with the convex $f(u)=(\sqrt u-1)^2$, $f(1)=0$. The
data-processing inequality for $f$-divergences under a Markov kernel
(Csiszár 1967; Liese–Vajda) requires exactly: $f$ convex on $(0,\infty)$ with the usual
extended-value conventions, $P,Q$ probability laws, $K$ a normalized Markov kernel. All
three hold under (H3). No standard-Borel, dominatedness, or absolute-continuity
hypothesis is needed. $\square$

### 1.3 Theorem A — the pushed score is a conditional expectation

**Theorem A.** Assume (H1)–(H4) and fix a direction $u\in\mathbb R^d$; write
$h:=u^{\!\top}\ell_{\theta_0}\in L^2_0(P_{\theta_0})$. Then the pushed family
$\{P^Y_{\theta_0+tu}\}$ is differentiable in quadratic mean at $t=0$ with score
$$
\bar h \;=\; R h,\qquad
(Rh)(y):=\mathbb E_{\mathbb P_{\theta_0}}\!\big[h(X)\;\big|\;Y=y\big],
$$
the identity holding in $L^2_0(P^Y_{\theta_0})$. The map
$R:L^2_0(P_{\theta_0})\to L^2_0(P^Y_{\theta_0})$ is linear with $\lVert R\rVert\le1$, so
$u\mapsto R(u^{\!\top}\ell_{\theta_0})$ is linear and the coarse family is DQM in the
$d$-dimensional sense with score $\bar\ell_{\theta_0}=R\ell_{\theta_0}$ applied
coordinatewise.

*Proof.* **Step 1 (density of the pushed path).** Let $(P_t)$ be any path with
$dP_t/dP_0=:p_t$ existing (so $P_t\ll P_0$). For $B\in\mathscr Y$,
$$
(P_tK)(B)=\int K(x,B)\,p_t(x)P_0(dx)
=\mathbb E_{\mathbb P_0}\!\big[p_t(X)\mathbf 1_B(Y)\big]
=\int_B \mathbb E_{\mathbb P_0}[p_t(X)\mid Y=y]\,(P_0K)(dy),
$$
using $\mathbb P_0(dx,dy)=P_0(dx)K(x,dy)$ and the tower property. Hence
$$
\frac{d(P_tK)}{d(P_0K)}=\mathbb E_{\mathbb P_0}\big[p_t(X)\mid Y\big]
\qquad P_0K\text{-a.e.}
\tag{1.1}
$$

**Step 2 (bounded scores).** Let $h\in L^2_0(P_0)$ be bounded, put $a=\lVert h\rVert_2^2/4$,
and take the canonical two-sided path
$p_t=(1+th/2)^2/(1+at^2)$ (`07b_agent_network_rg.tex:559-599`; reproduced independently
in `evidence/task-9-score-dqm-analysis.md` Lemma 1). Boundedness gives
$p_t=1+th+O(t^2)$ *uniformly in $x$*. Conditional expectation of a uniformly $O(t^2)$
remainder is uniformly $O(t^2)$, so (1.1) yields
$d(P_tK)/d(P_0K)=1+t\,Rh+O(t^2)$ uniformly, and
$\sqrt{1+w}=1+w/2+O(w^2)$ uniformly on $|w|\le1/2$ gives
$\sqrt{d(P_tK)/d(P_0K)}=1+\tfrac t2 Rh+O(t^2)$ in $L^\infty$, hence in
$L^2(P_0K)$. That is DQM with score $Rh$.

**Step 3 (general scores).** Let $h\in L^2_0(P_0)$ be arbitrary and choose bounded
centered $h_n\to h$ in $L^2(P_0)$ (bounded functions are dense in $L^2$; centering is
$L^2$-continuous). Let $(P_t)$, $(P_t^{(n)})$ be the canonical paths for $h$, $h_n$. By
Lemma 1.1 applied to the two DQM expansions,
$\limsup_{t\to0}H(P_t,P_t^{(n)})/|t|\le\tfrac12\lVert h-h_n\rVert_2$, and by Lemma 1.2 the
same bound holds for $H(P_tK,P_t^{(n)}K)$. Conditional Jensen gives
$\lVert R(h-h_n)\rVert_2\le\lVert h-h_n\rVert_2$. Combining with Step 2 for $h_n$,
$$
\limsup_{t\to0}\frac1{|t|}\Big\lVert\sqrt{\tfrac{d(P_tK)}{d(P_0K)}}-1-\tfrac t2 Rh\Big\rVert_2
\;\le\;\tfrac12\lVert h-h_n\rVert_2+\tfrac12\lVert R(h-h_n)\rVert_2
\;\le\;\lVert h-h_n\rVert_2 .
$$
The left side does not depend on $n$; letting $n\to\infty$ makes it zero.

**Step 4 (arbitrary DQM path with score $h$).** The family $\{P_{\theta_0+tu}\}$ need not
be the canonical path. But by Lemma 1.1(i) it is $o(|t|)$-close in Hellinger distance to
the canonical path with the same score, by Lemma 1.2 its image is $o(|t|)$-close to the
canonical image, and by Lemma 1.1(ii) the image is therefore DQM with the same score
$Rh$. **Step 4 is the step that is silently skipped whenever a proof computes the score
of one convenient path and asserts it for the family.**

Linearity of $R$ and $\lVert R\rVert\le1$ are conditional Jensen; mean preservation
$\mathbb E[Rh]=\mathbb E[h]=0$ is the tower property. $\square$

**What Theorem A does not say.** (a) $\bar h$ is an element of $L^2(P^Y_{\theta_0})$, that
is, an equivalence class. Any pointwise formula for $\bar h$ on a
$P^Y_{\theta_0}$-null set is undetermined — the manuscript's own
`CE-RCP-EXCEPTION` register entry is the same phenomenon at the level of regular
conditional laws. (b) $\bar h$ is defined by the joint law **at $\theta_0$ only**;
nothing here produces a $\theta$-indexed family of versions, let alone a jointly
measurable or smooth one. (c) Nothing here places $P^Y_\theta$ inside a declared
coarse manifold; that is (H5).

### 1.4 Theorem B — the Fisher contraction defect is a conditional score covariance

**Theorem B.** Under (H1)–(H4), with
$I_{\mathsf X}(\theta_0)=\mathbb E_{\theta_0}[\ell_{\theta_0}\ell_{\theta_0}^{\!\top}]$ and
$I_{\mathsf Y}(\theta_0)=\mathbb E[\bar\ell_{\theta_0}\bar\ell_{\theta_0}^{\!\top}]$,
$$
I_{\mathsf X}(\theta_0)-I_{\mathsf Y}(\theta_0)
=\mathbb E_{\mathbb P_{\theta_0}}\!\big[\operatorname{Cov}\big(\ell_{\theta_0}(X)\mid Y\big)\big]\;\succeq\;0 .
\tag{1.2}
$$

*Proof.* Both scores are centered, so $I_{\mathsf X}=\operatorname{Cov}(\ell)$ and
$I_{\mathsf Y}=\operatorname{Cov}(\mathbb E[\ell\mid Y])$. The law of total covariance,
valid because $\ell\in L^2$, gives
$\operatorname{Cov}(\ell)=\operatorname{Cov}(\mathbb E[\ell\mid Y])+\mathbb E[\operatorname{Cov}(\ell\mid Y)]$.
Rearranging is (1.2); positive semidefiniteness is that of a conditional covariance,
integrated. $\square$

**Equality, characterized exactly.** For $u\in\mathbb R^d$,
$$
u^{\!\top}\big(I_{\mathsf X}-I_{\mathsf Y}\big)u
=\mathbb E_{\mathbb P_{\theta_0}}\operatorname{Var}\big(u^{\!\top}\ell_{\theta_0}(X)\mid Y\big)=0
\iff
u^{\!\top}\ell_{\theta_0}(X)=g(Y)\ \ \mathbb P_{\theta_0}\text{-a.s.}
$$
for some $g\in L^2(P^Y_{\theta_0})$; and then necessarily $g=R(u^{\!\top}\ell_{\theta_0})$.
Three qualifications are required and are not interchangeable.

1. *Almost sure, not pointwise.* "The fine score is measurable with respect to the
   coarse output" (`05c_pullback_geometry.tex:698-700`) must be read as $\mathbb P_{\theta_0}$-a.s.
   equality with a $\sigma(Y)$-measurable function, not as $\sigma(Y)$-measurability of
   the chosen representative. A representative altered on a null set can be
   non-$\sigma(Y)$-measurable while equality still holds.
2. *Directional.* Equality can hold on a proper subspace of directions. The defect is a
   positive semidefinite **form**, and its kernel is
   $\{u: u^{\!\top}\ell_{\theta_0}\text{ is a.s. }\sigma(Y)\text{-measurable}\}$.
3. *Local, not sufficiency.* Equality at one $\theta_0$ is not sufficiency of $K$. The
   register's `CE-FISHER-EQUALITY` witness is correct and is reproduced here:
   independent $A,B$ with $\Pr_\theta(A=1)=\tfrac12+\tfrac\theta4$ and
   $\Pr_\theta(B=1)=\tfrac12+\tfrac{\theta^2}4$, channel retaining only $A$. At
   $\theta=0$ the $B$-score is $\partial_\theta\log(\tfrac12+\tfrac{\theta^2}4)|_0=0$, so
   the full score is $A$-measurable and (1.2) is an equality; yet
   $\Pr_\theta(B=1\mid A)$ moves with $\theta$, so no parameter-independent reverse
   kernel reconstructs the experiment.

### 1.5 The bundle statement, with (H5) made a hypothesis and $T^V\Psi$ identified

Under (H5) the map $\varphi:\mathcal B\to\bar{\mathcal B}$, $P\mapsto PK$, is
*differentiable in the DQM sense at $p$* with derivative given in score coordinates by
$R_p$: this is precisely Theorem A, which shows that the score of the pushed path is
linear in the fine score. Define $T^V_p\Psi:T_p\mathcal B\to T_{\varphi(p)}\bar{\mathcal B}$
to be that induced map. Then, by definition of the Fisher form of a DQM model as the
$L^2$ norm of its score,
$$
\big[(T^V\Psi)^*\bar g^F\big]_p(u,u)
=\bar g^F_{\varphi(p)}\big(T^V\Psi\,u,\;T^V\Psi\,u\big)
=\lVert R_p\ell_u\rVert^2_{L^2(\varphi(p))},
$$
so the vertical Fisher defect of `05c_pullback_geometry.tex:680-685` is
$$
\Delta^\Psi_F(u,u)\;=\;\lVert\ell_u\rVert^2-\lVert R_p\ell_u\rVert^2
\;=\;\mathbb E\operatorname{Var}\big(\ell_u(X)\mid Y\big)\;\ge\;0 ,
\tag{1.3}
$$
which is `eq:pb-fisher-defect-score-variance` with every hypothesis now named. The
manuscript's proof of `thm:pb-pullback-fisher-defect` is correct; what it omits is (H5)
and the identification of $T^V\Psi$ with $R_p$ as a *definition* rather than an
assumption.

**Additional obligation exposed here.** For $\Psi$ to be a *smooth* bundle morphism, the
assignment $p\mapsto T^V_p\Psi$ must be smooth. Since $R_p$ acts between the varying
spaces $L^2(p)\to L^2(\varphi(p))$, smoothness must be phrased in a fixed reference
Hilbert space — for instance by transporting to $L^2(\mu)$ and $L^2(\nu)$ for fixed
$\sigma$-finite $\mu,\nu$ via multiplication by amplitudes. That transport is available
under (H1) plus a corresponding coarse domination hypothesis, and it is an obligation,
not a consequence.

### 1.6 The defect cocycle, with the minimal hypothesis

Let $E_0\xrightarrow{\Psi_{01}}E_1\xrightarrow{\Psi_{12}}E_2$ be composable with
vertical Fisher metrics $g^F_0,g^F_1,g^F_2$. Contravariance of pullback gives, purely
algebraically,
$$
\Delta_F^{\Psi_{12}\Psi_{01}}
=g^F_0-(T^V\Psi_{01})^*(T^V\Psi_{12})^*g^F_2
=\underbrace{\big[g^F_0-(T^V\Psi_{01})^*g^F_1\big]}_{\Delta_F^{\Psi_{01}}}
+(T^V\Psi_{01})^*\underbrace{\big[g^F_1-(T^V\Psi_{12})^*g^F_2\big]}_{\Delta_F^{\Psi_{12}}},
\tag{1.4}
$$
which is `eq:pb-fisher-defect-cocycle`. This identity needs **no** Markov hypothesis; it
needs only that all three defects be defined. Positivity of both summands needs both
arrows to be parameter-independent Markov.

**Base-level composition, minimal hypothesis.** Put
$\delta_{k,k+1}:=(D^{\omega_k}s_k)^*\Delta_F^{\Psi_{k,k+1}}$. Suppose the fine section
relation $\Psi_{01}\circ s_0=s_1\circ f_{01}$ holds and $\mathcal D\Psi_{01}=0$ along
$s_0$. Then the first-jet chain rule (`eq:pb-covariant-jet-chain-rule`) gives
$T^V\Psi_{01}\circ D^{\omega_0}s_0=D^{\omega_1}s_1\circ Tf_{01}$, so pulling (1.4) back by
$D^{\omega_0}s_0$ yields
$$
\delta_{02}=\delta_{01}+f_{01}^*\,\delta_{12}.
\tag{1.5}
$$
No hypothesis on $\Psi_{12}$'s horizontal defect and no relation of $s_1$ to $s_2$ enters
(1.5). Those extra hypotheses are needed only to *reinterpret* $\delta_{12}$ as
$h_{s_1}-f_{12}^*h_{s_2}$. This is the minimality point recorded in §0.3(3).

---

## 2. Compatibility with the bounded-action quotient from Task 9

### 2.1 The score map and its representative independence

Fix a scale with base law $\pi$ on $\mathsf X$. For $\varphi\in L^\infty(\pi;\mathbb R)$
the normalized exponential-action path is
$\widehat\pi^{t\varphi}(dx)=e^{-t\varphi(x)}\pi(dx)/\pi(e^{-t\varphi})$, and
`prop:rg-action-score-isometry` (`07b_agent_network_rg.tex:762-810`) computes its score
$$
\mathscr S_\pi[\varphi]=-\big(\varphi-\pi(\varphi)\big)\in L^2_0(\pi).
\tag{2.1}
$$
Representative independence modulo constants is immediate:
$\mathscr S_\pi[\varphi+c]=-\big((\varphi+c)-\pi(\varphi)-c\big)=\mathscr S_\pi[\varphi]$.
So $\mathscr S_\pi$ descends to the quotient $\overline{\mathfrak B}=L^\infty(\pi)/\mathbb R\mathbf 1$.
The sign in (2.1) is the manuscript's convention and matches the ledger statement of
`score-action-compatibility`; it is a convention, and it cancels in every quadratic form
below.

### 2.2 Fisher isometry on the bounded quotient

Define the Fisher quotient norm $\lVert[\varphi]\rVert_F:=\inf_{c\in\mathbb R}\lVert\varphi-c\rVert_{L^2(\pi)}$.
Since
$\lVert\varphi-c\rVert_2^2=\lVert\varphi-\pi(\varphi)\rVert_2^2+(\pi(\varphi)-c)^2$,
the infimum is attained uniquely at $c=\pi(\varphi)$ and
$$
\lVert[\varphi]\rVert_F=\lVert\varphi-\pi(\varphi)\rVert_{L^2(\pi)}=\lVert\mathscr S_\pi[\varphi]\rVert_{L^2(\pi)} .
\tag{2.2}
$$
Hence $\mathscr S_\pi:(\overline{\mathfrak B},\lVert\cdot\rVert_F)\to L^2_0(\pi)$ is a
linear isometry. **It is not surjective.** Its range is the bounded centered subspace
$\{h\in L^\infty(\pi):\pi(h)=0\}$, which is dense in $L^2_0(\pi)$ (bounded functions are
$L^2$-dense; centering is continuous) and proper whenever $L^2_0(\pi)$ contains an
unbounded element — for $\pi=N(0,1)$, take $h(x)=x$.

### 2.3 Dense $L^2$ completion and the exact scope of the ledger claim

The ledger states `score-action-compatibility` as "an isometric isomorphism from
`L2/R1` with Fisher norm to `L2_0`", quantified over "every $\varphi$ in $L^2(\pi_l)$".
That statement is **true** on $L^2(\pi)/\mathbb R\mathbf 1$: the algebraic map
$\varphi\mapsto-(\varphi-\pi\varphi)$ is a surjective isometry onto $L^2_0(\pi)$ (given
$h\in L^2_0$, take $\varphi=-h$), and $L^2_0(\pi)$ is exactly the Fisher-norm completion
of the bounded quotient by §2.2.

But it is a *different statement* from `prop:rg-action-score-isometry`, and the
difference is load-bearing. On $L^2\setminus L^\infty$ the exponential-action path is
generally undefined: for $\pi=N(0,1)$ and $\varphi(x)=-x^2\in L^2(\pi)$, the normalizer
$\pi(e^{-t\varphi})=\pi(e^{tx^2})$ is infinite for every $t\ge1/2$, and no two-sided
neighborhood exists — this is the register's `CE-ACTION-LP`. What *is* true on all of
$L^2_0$ is that every element is realized as a two-sided quadratic-mean score, by the
quadratic path $p_t=(1+th/2)^2/(1+at^2)$ of `lem:rg-dqm-realization`. So:

> On $L^2(\pi)/\mathbb R\mathbf 1$, $\mathscr S_\pi$ is the centering isometry and every
> class is realized as a two-sided DQM score; the realizing path is the **quadratic**
> path, not the exponential-action path, and the nonlinear bounded action map of
> `thm:rg-bounded-action-calculus` is not defined there.

`prop:ig-hermite-exponential-domain` (`08_infogeometry.tex:364-396`) makes the failure
exact rather than merely possible: for $\gamma=N(0,1)$, $N_k(t)=\int e^{-t\mathrm{He}_k}d\gamma$
is finite for all $t$ when $k=1$; equals $e^t(1+2t)^{-1/2}$ for $t>-\tfrac12$ when $k=2$;
is $+\infty$ for every $t\ne0$ when $k\ge3$ is odd; and is finite exactly for $t\ge0$
when $k\ge4$ is even. Every $\mathrm{He}_k$ lies in $L^2_0(\gamma)$, so from degree three
upward the Fisher tangent contains directions with **no** two-sided exponential action
neighborhood. The nonlinear chart and the Fisher tangent are therefore genuinely
different objects, and the manuscript already says so
(`07b_agent_network_rg.tex:812-819`; `08_infogeometry.tex:398-412`).

### 2.4 The restriction / conditional-expectation square

Let $K$ be a parameter-independent normalized Markov kernel, $\pi^c=\pi K$, and let
$U:L^2(\pi)\to L^2(\pi^c)$, $(U\varphi)(z)=\mathbb E_{\pi\otimes K}[\varphi(X)\mid Z=z]$, be
the reverse conditional expectation. Then $U\mathbf 1=\mathbf 1$, $U$ maps $L^\infty(\pi)$
into $L^\infty(\pi^c)$ with $\lVert U\rVert_\infty\le1$, and $U(\varphi+c)=U\varphi+c$, so
$U$ descends to $\overline U$ on the quotients. The tower property gives
$\pi^c(U\varphi)=\pi(\varphi)$. Therefore
$$
\mathscr S_{\pi^c}\big[\overline U[\varphi]\big]
=-\big(U\varphi-\pi^c(U\varphi)\big)
=-\big(U\varphi-\pi(\varphi)\big)
=U\big(-(\varphi-\pi(\varphi))\big)
=U\,\mathscr S_\pi[\varphi].
\tag{2.3}
$$
The square (2.3) commutes on the bounded quotient and, since $U$ is an $L^2$
contraction with $U\mathbf 1=\mathbf 1$, extends by continuity to the Fisher completion.
Comparing (2.3) with Theorem A: $U$ restricted to $L^2_0$ *is* the operator $R$ of §1.3.
So the action-tier restriction and the score-tier pushforward are the same operator seen
through the isometry $\mathscr S$. This is exactly the compatibility Task 10 Step 1
requires, and it is proved, not asserted.

**Consequence for the $L^2$ defect.** Applying (2.2) and Theorem B to $h=\mathscr S_\pi[\varphi]$,
$$
\lVert[\varphi]\rVert_F^2-\lVert\overline U[\varphi]\rVert_F^2
=\lVert h\rVert^2_{L^2(\pi)}-\lVert Uh\rVert^2_{L^2(\pi^c)}
=\mathbb E\operatorname{Var}\big(h(X)\mid Z\big)\;\ge\;0 ,
\tag{2.4}
$$
so the scalar $L^2$ defect on the action quotient *is* the Fisher information loss, with
the same equality condition as §1.4. That closes Task 10 Step 1's second half.

### 2.5 The distinction that must not collapse

The bounded quotient carries two norms doing different work:
$\lVert\cdot\rVert_{\mathrm{osc}}$ controls the nonlinear map $Q$ of
`thm:rg-bounded-action-calculus`; $\lVert\cdot\rVert_F$ controls the quadratic-mean
tangent. They are ordered, $\lVert[\varphi]\rVert_F\le\lVert[\varphi]\rVert_{\mathrm{osc}}$
by $\inf_c\lVert\varphi-c\rVert_2\le\inf_c\lVert\varphi-c\rVert_\infty$, and the ordering
is strict in general. **A spectral statement proved on $L^2_0$ is not a statement about
the nonlinear bounded action chart**, and conversely. The extensive block lift
$\mathscr I_b$ of `prop:rg-score-block-lift`, with $\lVert\mathscr I_b\rVert=\sqrt b>1$,
lives on the $L^2_0$ tangent and is *not* a Markov pushforward; §6.3 shows that this is
precisely the mechanism by which a coarse Fisher duration can exceed a fine one without
contradicting Theorem B.

---

## 3. A rigorous nonempty configuration manifold at each scale

### 3.1 The gap being filled

`hyp:hist-regular-section-space` (`05d_relational_inference.tex:91-97`) declares a
"regular space of pairs of smooth sections" and `hyp:hist-regular-metric-domain`
(`05d_relational_inference.tex:204-211`) declares a configuration manifold
$\mathcal Q_i$ "equipped with a positive-definite Fisher Riemannian metric
$\mathsf G_i^F$" that is "a strong metric" in an infinite-dimensional realization. Both
are hypotheses. A source-wide search for a nonemptiness result finds only
`prop:gauss-interaction-nonempty` (`06_gaussian.tex:307`), which is about the Gaussian
*interaction* family, a different object; and the phrase "strong metric" occurs exactly
once in the manuscript, in the hypothesis itself. **No configuration manifold is
exhibited anywhere, and no strong-metric verification is performed anywhere.** A
hypothesis with an empty model class is vacuous, so this is a real obligation, and §§3.2–3.5
discharge the existence half of it.

### 3.2 Nonemptiness of the section space

**Lemma 3.1 (convex-fiber sections exist).** Let $\mathcal C$ be a paracompact smooth
manifold, $\pi:P\to\mathcal C$ a principal $G$-bundle, and $E=P\times_{\widehat\rho}\mathcal B$
an associated bundle whose typical fiber $\mathcal B$ is a nonempty convex subset of a
locally convex topological vector space $W$, with $\widehat\rho(g)$ acting as the
restriction to $\mathcal B$ of a continuous linear automorphism of $W$ preserving
$\mathcal B$. Then $E$ admits a global smooth section, so $\Gamma(E)\ne\varnothing$.

*Proof.* Choose a trivializing open cover $\{U_\alpha\}$ with
$E|_{U_\alpha}\cong U_\alpha\times\mathcal B$ and a subordinate smooth partition of
unity $\{\chi_\alpha\}$ (paracompactness). Pick any $z\in\mathcal B$ and let $s_\alpha$
be the constant local section $z$ in the $\alpha$-trivialization. Define
$s(c):=\sum_\alpha\chi_\alpha(c)\,s_\alpha(c)$, the sum taken in the fiber $E_c$. The sum
is well defined because the transition maps
$\widehat\rho(g_{\alpha\beta}(c))$ are restrictions of linear automorphisms, so they
commute with convex combinations, and each $E_c$ inherits the convex structure of
$\mathcal B$ unambiguously. Since $\sum_\alpha\chi_\alpha=1$ with $\chi_\alpha\ge0$, the
value $s(c)$ is a convex combination of points of $\mathcal B$ and hence lies in
$\mathcal B$. Local finiteness gives smoothness. $\square$

Lemma 3.1 covers the cases the manuscript actually uses: Gaussian moment charts
($\mu\in\mathbb R^K$ and $\Sigma\in\operatorname{Sym}^{++}_K$ are convex, and the
congruence action $\Sigma\mapsto g\Sigma g^{\!\top}$, $\mu\mapsto g\mu$ is linear), and
finite simplices under congruent Markov embeddings.

**Boundary of Lemma 3.1.** Convexity, or at least contractibility, is doing the work.
For a *non-contractible* fiber the conclusion fails: take $\mathcal C=S^1$,
$G=\mathbb Z/2$ acting on $\mathcal B=\{\pm1\}$, and $P\to S^1$ the connected double
cover. The associated bundle has no continuous section, because a section would be a
continuous $\mathbb Z/2$-equivariant map from a connected total space to a two-point set
with free action. So nonemptiness is a genuine hypothesis on the declared fiber, not a
formality. Any belief fiber declared as a sphere of fixed Fisher norm, or as a
statistical family with a removed point, falls outside Lemma 3.1.

### 3.3 Tier (a) — a finite-dimensional parameterized section family

**Construction 3.2.** Fix a paracompact smooth base $\mathcal C_i$ and a finite positive
Borel measure $\mu_i$ on it. Take $P=\mathcal C_i\times G$ trivial, $\omega$ any chosen
principal connection with local form $A\in\Omega^1(\mathcal C_i,\mathfrak g)$, and the
belief fiber to be the nondegenerate Gaussian family
$\mathcal B_b=\{\mathcal N(m,\Sigma):m\in\mathbb R^K,\ \Sigma\in\operatorname{Sym}^{++}_K\}$,
whose Fisher metric in the moment chart is positive definite by
`prop:ig-fisher-moment-chart` (`08_infogeometry.tex:79-94`),
$g^F_{(m,\Sigma)}((u,A),(u,A))=u^{\!\top}\Sigma^{-1}u+\tfrac12\operatorname{Tr}(\Sigma^{-1}A\Sigma^{-1}A)$.

Fix smooth $\phi_1,\dots,\phi_{N_1}:\mathcal C_i\to\mathbb R^K$ and smooth symmetric
matrix fields $\Psi_1,\dots,\Psi_{N_2}:\mathcal C_i\to\operatorname{Sym}_K$, and set
$$
\Xi=\mathbb R^{N_1}\times\mathbb R^{N_2},\qquad
s_\xi(c)=\mathcal N\Big(\textstyle\sum_{a}\xi_a\phi_a(c),\ \exp\big(\sum_b\xi'_b\Psi_b(c)\big)\Big).
$$
Every $s_\xi$ is a smooth section (the matrix exponential lands in
$\operatorname{Sym}^{++}_K$, and the fiber bundle is trivial), so
$\mathcal Q^{(a)}_i:=\{(s_\xi,s'_\eta)\}\cong\Xi\times\Xi'$ is a **nonempty finite-dimensional
smooth manifold**, diffeomorphic to $\mathbb R^{N_1+N_2+N_1'+N_2'}$. Nonemptiness is
constructive: $\xi=0$ gives the section $c\mapsto\mathcal N(0,I_K)$.

**The metric.** Declare measurable channel weights $w_b,w_m:\mathcal C_i\to(0,\infty)$
and set, for $V\in T_\xi\mathcal Q^{(a)}_i$,
$$
\mathsf G^{w,\mu}_\xi(V,V)
=\int_{\mathcal C_i}\Big[w_b(c)\,g^F_{b,s_\xi(c)}\big(\partial_V s_\xi(c),\partial_V s_\xi(c)\big)
+w_m(c)\,g^F_{m}\big(\cdots\big)\Big]\,\mu_i(dc).
\tag{3.1}
$$

**Proposition 3.3 (finiteness, smoothness, and exact nondegeneracy).** Assume
$\mu_i(\mathcal C_i)<\infty$, $w_b,w_m$ locally bounded, and the integrand locally
bounded in $(c,\xi)$ — automatic when $\mathcal C_i$ is compact. Then (3.1) is a smooth
positive semidefinite symmetric $2$-tensor on the finite-dimensional manifold
$\mathcal Q^{(a)}_i$, and it is a Riemannian metric (necessarily **strong**, since the
manifold is finite-dimensional and every inner product on a finite-dimensional space
induces the norm topology) if and only if
$$
\Big\{V\in T_\xi\mathcal Q^{(a)}_i:\ \partial_V s_\xi(c)=0\ \text{for }\mu_i\text{-a.e. }c\Big\}=\{0\}.
\tag{3.2}
$$

*Proof.* The integrand is a nonnegative quadratic form in $V$ with smooth coefficients;
finiteness and smooth dependence on $\xi$ follow from dominated convergence under the
stated local bounds. $\mathsf G^{w,\mu}_\xi(V,V)=0$ forces the nonnegative integrand to
vanish $\mu_i$-a.e., and $w_b,w_m>0$ together with positive definiteness of the fiber
Fisher metrics forces $\partial_Vs_\xi(c)=0$ $\mu_i$-a.e.; the converse is immediate.
$\square$

**Checkable instance.** For the pure location submodel ($\Sigma$ fixed, $N_2=0$), (3.1)
is the Gram matrix
$$
\big[\mathsf G^{w,\mu}\big]_{ab}=\int_{\mathcal C_i}\phi_a(c)^{\!\top}\Sigma^{-1}\phi_b(c)\,w_b(c)\,\mu_i(dc),
$$
so (3.2) holds **iff $\{\phi_a\}$ are linearly independent in $L^2(w_b\mu_i;\Sigma^{-1})$**
— not merely pointwise independent. This sharpens the manuscript's remark at
`05d_relational_inference.tex:485-489` that a finite-design speed has a radical: with
$\mu_i=\sum_{a=1}^M\rho_a\delta_{c_a}$ the Gram matrix has rank at most $MK$, so
whenever $N_1>MK$ the metric is degenerate and, by
`prop:hist-semidefinite-gradient-obstruction` (`05d_relational_inference.tex:344-355`),
the natural-gradient equation can have no solution or many. Degeneracy of a finite-design
configuration metric is therefore a *counting* condition, checkable in advance.

### 3.4 Tier (b) — a Hilbert section manifold, and exactly where the metric is weak

Take $\mathcal C_i$ a compact smooth $n$-manifold with Riemannian volume $\mu_i$, a
trivial principal bundle with flat connection, and the belief fiber the Gaussian location
family with **fixed** $\Sigma_0\succ0$, so that a section is exactly a map
$m:\mathcal C_i\to\mathbb R^K$ and the fiber Fisher metric is the constant form
$\Sigma_0^{-1}$.

**(b1) The $L^2$ tier: strong.** Put
$\mathcal Q^{(b1)}_i:=L^2(\mu_i;\mathbb R^K)$, a separable Hilbert space and hence a
nonempty Hilbert manifold, with
$$
\mathsf G^{L^2}(V,W)=\int_{\mathcal C_i}V(c)^{\!\top}\Sigma_0^{-1}W(c)\,w(c)\,\mu_i(dc).
$$
**Proposition 3.4.** If $w$ is measurable with $0<w_-\le w\le w_+<\infty$ and
$\lambda_-I\preceq\Sigma_0^{-1}\preceq\lambda_+I$, then $\mathsf G^{L^2}$ is equivalent
to the $L^2$ inner product,
$w_-\lambda_-\lVert V\rVert^2_{L^2}\le\mathsf G^{L^2}(V,V)\le w_+\lambda_+\lVert V\rVert^2_{L^2}$,
so the musical map $\flat:\mathcal Q^{(b1)}_i\to(\mathcal Q^{(b1)}_i)^*$ is a topological
isomorphism (Lax–Milgram, or Riesz after renorming). Hence $\mathsf G^{L^2}$ is a
**strong** Riemannian metric and every $C^1$ functional on $\mathcal Q^{(b1)}_i$ has a
unique gradient. *The two-sided bounds on $w$ and on the fiber Fisher form are exactly the
boundedness and coercivity conditions; either failing alone destroys the conclusion.*

**(b2) The $H^s$ tier with the same integrated metric: weak.** Suppose instead the VFE
requires smoother sections — for example because it contains a gradient-energy term — and
one takes $\mathcal Q^{(b2)}_i:=H^s(\mathcal C_i;\mathbb R^K)$ with $s>0$, retaining the
**integrated fiber Fisher metric** $\mathsf G^{L^2}$. Then $\mathsf G^{L^2}$ is a
continuous, positive definite, but **weak** metric: its topology is the $L^2$ topology,
strictly coarser than $H^s$, and $\flat:H^s\to(H^s)^*$ is injective and bounded but not
surjective.

**Counterexample 3.5 (no gradient, explicit).** Take $\mathcal C_i=S^1$ with normalized
arclength, $K=1$, $\Sigma_0=1$, $w\equiv1$, $\mathcal Q=H^1(S^1;\mathbb R)$,
$\mathsf G^{L^2}(V,W)=\int_{S^1}VW\,d\mu$, and the smooth quadratic functional
$\mathcal F(Q)=\tfrac12\int_{S^1}|Q'|^2 d\mu$, whose differential is
$d\mathcal F_Q[V]=\int_{S^1}Q'V'\,d\mu$. A $\mathsf G^{L^2}$-gradient at $Q$ would be
$G\in H^1$ with $\int GV\,d\mu=\int Q'V'\,d\mu$ for all $V\in H^1$, that is $G=-Q''$
distributionally. Take
$$
Q(\theta)=\sum_{k\ge1}k^{-2}\sin(k\theta),
$$
so $\lVert Q\rVert^2_{H^1}\asymp\sum_k k^{-4}k^2=\sum_k k^{-2}<\infty$ (hence $Q\in H^1$)
while $-Q''=\sum_{k\ge1}\sin(k\theta)$ has $\lVert\cdot\rVert^2_{L^2}\asymp\sum_k1=\infty$.
So no $G\in L^2$, a fortiori none in $H^1$, exists: **the natural-gradient vector field
is not defined at $Q$.** No amount of positivity or smoothness of $\mathcal F$ repairs
this; the missing ingredient is Riesz representability of $d\mathcal F_Q$ in the weak
metric.

**Corollary 3.6 (the added hypothesis, stated exactly).** On a weak metric the
natural-gradient equation is solvable at $Q$ if and only if
$d\mathcal F_Q\in\operatorname{ran}(\flat)$. A sufficient and checkable form of this
**Riesz hypothesis** is an elliptic-regularity statement: $d\mathcal F_Q$ extends to a
bounded functional on the $\mathsf G^{L^2}$-completion $L^2$, that is
$|d\mathcal F_Q[V]|\le C_Q\lVert V\rVert_{L^2}$ for all $V$ in the dense domain. In
Counterexample 3.5 this fails precisely because $|d\mathcal F_Q[V]|\le C\lVert V\rVert_{L^2}$
would force $Q\in H^2$.

**The honest dichotomy for Tier (b).** Either
(i) take $\mathcal Q_i=L^2$ and the integrated fiber Fisher metric, obtaining a strong
metric and unconditional gradients, at the cost of requiring $\mathcal F$ to be $C^1$ on
$L^2$ (which excludes gradient-energy VFEs); or
(ii) take $\mathcal Q_i=H^s$, $s>0$, and either replace the metric by an $H^s$-equivalent
one — which is then **not** the integrated fiber Fisher metric and must be declared as a
different geometry — or retain the integrated Fisher metric and add the Riesz hypothesis
of Corollary 3.6 as an explicit standing assumption with its failure witness recorded.
There is no third option, and the manuscript currently declares neither.

### 3.5 Gauge quotient in the Hilbert tier

`05d_relational_inference.tex:529-536` asserts, as a `HYPOTHESIS`, that in infinite
dimensions "free, proper, and isometric action is not by itself enough" for the
quotient-speed formula `eq:hist-quotient-gauge-speed`, and demands a smooth principal
quotient with closed split orbit-tangent subbundles. In the strong Hilbert tier (b1) the
requirement simplifies and can be proved.

**Proposition 3.7.** Let $\mathcal Q$ be a Hilbert manifold with a strong metric and let
$\mathfrak o_Q\subseteq T_Q\mathcal Q$ be the orbit tangent at $Q$. If $\mathfrak o_Q$ is
**closed**, the infimum in `eq:hist-quotient-gauge-speed` is attained and equals
$\lVert P_{\mathfrak o_Q^{\perp}}\dot Q\rVert$. *Proof.* The orthogonal projection theorem
in a Hilbert space applies to any closed subspace; complementedness is automatic. $\square$

**Counterexample 3.8 (nonclosed orbit tangent collapses the clock).** Let
$\mathcal Q=\ell^2$ with its inner product, and let the gauge group be the additive
subgroup $\mathcal G=h^1:=\{v\in\ell^2:\sum_n n^2v_n^2<\infty\}$ acting by translation.
The action is free and isometric, and $\mathfrak o_Q=h^1$ for every $Q$. Since $h^1$ is
dense in $\ell^2$, for **every** $\dot Q\in\ell^2$ the infimum
$\inf_{\zeta\in h^1}\lVert\dot Q-\zeta\rVert=0$, and it is attained only when
$\dot Q\in h^1$. The quotient speed is therefore identically zero and defines no clock.

Proposition 3.7 and Counterexample 3.8 together give the sharp reading: in the strong
Hilbert tier the decisive extra hypothesis is **closedness of the orbit tangent**, and
the manuscript's longer list (smooth principal quotient, closed split subbundles, smooth
orthogonal complements) is the correct generalization to Banach manifolds, where closed
no longer implies complemented. The manuscript's specific sentence "free, proper, and
isometric action is not by itself enough" is stated without a witness; Counterexample 3.8
witnesses only the weaker *free and isometric* version, since the translation action of a
dense non-closed subgroup is not proper. That gap is recorded in §8 as an obligation on
`configuration-fisher-metric`, not silently repaired.

---

## 4. Joint-law Fisher pullback versus a weighted product of marginal fiber metrics

### 4.1 The two objects, typed apart

`hyp:hist-exact-vfe-lift` (`05d_relational_inference.tex:213-268`) requires the exact
recognition metric to be $\mathsf G_i^F=\iota_i^*G^F_{\mathfrak R_B}$, the pullback along
a smooth right inverse of the configuration extraction, and warns that "a weighted
product of marginal-fiber metrics equals this joint pullback only under a separately
proved block-orthogonality or fixed-dependence hypothesis."
`hyp:pb-weighted-product-geometry` (`05c_pullback_geometry.tex:219-228`) declares the
competing object $h^{\mathrm{prod}}=w_b h^{\omega_b}_{i,b}+w_m h^{\omega_m}_{i,m}$ with
arbitrary constants $w_b,w_m>0$. Neither the exact equality criterion nor the direction
of the discrepancy is proved anywhere. This section proves the criterion.

### 4.2 The exact pointwise defect identity

Fix a context $c$ and let $r_\zeta(dy_b,dy_m)$ be the declared joint recognition law on
$\mathsf Y_b\times\mathsf Y_m$, smooth in $\zeta$ in the DQM sense, with marginals
$r^b_\zeta,r^m_\zeta$ and $\pi^{\mathrm{conf}}(\zeta)=(r^b_\zeta,r^m_\zeta)$. Fix a tangent
direction and let $L\in L^2_0(r_\zeta)$ be the corresponding joint score.

Marginalization is a *deterministic, parameter-independent, normalized Markov kernel*
(project onto $Y_b$, respectively $Y_m$), so Theorem A applies verbatim and gives the
marginal scores as conditional expectations:
$$
L_b:=\mathbb E_{r_\zeta}[L\mid Y_b]=\Pi_b L,\qquad
L_m:=\mathbb E_{r_\zeta}[L\mid Y_m]=\Pi_m L,
$$
where $\Pi_b,\Pi_m$ are the orthogonal projections of $L^2_0(r_\zeta)$ onto the closed
subspaces of centered $\sigma(Y_b)$- and $\sigma(Y_m)$-measurable square-integrable
functions. Thus
$$
\iota^*G^F=\lVert L\rVert^2,\qquad g^F_b=\lVert L_b\rVert^2,\qquad g^F_m=\lVert L_m\rVert^2 .
$$

**Theorem C (exact comparison).** With the above notation,
$$
\boxed{\;
\lVert L\rVert^2-\big(\lVert L_b\rVert^2+\lVert L_m\rVert^2\big)
=\underbrace{\lVert L-L_b-L_m\rVert^2}_{\text{interaction residual }\ \ge0}
\;-\;2\underbrace{\langle L_b,L_m\rangle}_{\text{cross term, signed}} \; }
\tag{4.1}
$$
where $\langle L_b,L_m\rangle=\operatorname{Cov}_{r_\zeta}\!\big(L_b(Y_b),L_m(Y_m)\big)$.

*Proof.* Idempotence and self-adjointness of $\Pi_b$ give
$\langle L,L_b\rangle=\langle\Pi_bL,\Pi_bL\rangle=\lVert L_b\rVert^2$, and likewise
$\langle L,L_m\rangle=\lVert L_m\rVert^2$. Expanding,
$$
\lVert L-L_b-L_m\rVert^2
=\lVert L\rVert^2+\lVert L_b\rVert^2+\lVert L_m\rVert^2-2\lVert L_b\rVert^2-2\lVert L_m\rVert^2+2\langle L_b,L_m\rangle,
$$
which rearranges to (4.1). Both scores are centered, so the inner product is the stated
covariance. $\square$

### 4.3 Consequences, including a refutation of every naive ordering

**(C1) Each marginal alone contracts.** $\lVert L_b\rVert\le\lVert L\rVert$ and
$\lVert L_m\rVert\le\lVert L\rVert$, since $\Pi_b,\Pi_m$ are orthogonal projections. This
is Fisher data processing and is unconditional.

**(C2) The unit-weight sum is neither an upper nor a lower bound.** The sign of (4.1) is
the sign of $\lVert L-L_b-L_m\rVert^2-2\langle L_b,L_m\rangle$, and both terms are
realizable at any magnitude. Two decisive witnesses:

*Degenerate coupling.* If $Y_b=Y_m$ almost surely, then $\Pi_b=\Pi_m=\mathrm{Id}$, so
$L_b=L_m=L$ and $\lVert L_b\rVert^2+\lVert L_m\rVert^2=2\lVert L\rVert^2>\lVert L\rVert^2$
whenever $L\ne0$. The weighted product with unit weights **exceeds** the joint pullback
by a factor of two. (Check against (4.1): the residual is $\lVert L-2L\rVert^2=\lVert L\rVert^2$
and the cross term is $2\lVert L\rVert^2$, giving $-\lVert L\rVert^2$, which is
$\lVert L\rVert^2-2\lVert L\rVert^2$.)

*Gaussian indefiniteness.* Let $(Y_b,Y_m)$ be jointly Gaussian on $\mathbb R\times\mathbb R$
with mean $\mu=(\mu_b,\mu_m)$ and fixed precision
$\Lambda=\begin{pmatrix}1&\rho\\ \rho&1\end{pmatrix}$, $0<|\rho|<1$, the parameter being
the mean. In the moment chart the joint mean Fisher form is $\Lambda$
(`prop:ig-fisher-moment-chart`); the $b$-marginal is $\mathcal N(\mu_b,(\Lambda^{-1})_{bb})$
with mean Fisher $((\Lambda^{-1})_{bb})^{-1}=1-\rho^2$, and likewise for $m$. So the
unit-weight product metric is $(1-\rho^2)I_2$ and
$$
\Lambda-(1-\rho^2)I_2=\begin{pmatrix}\rho^2&\rho\\ \rho&\rho^2\end{pmatrix},
\qquad \det=\rho^4-\rho^2=\rho^2(\rho^2-1)<0 .
$$
The difference is **indefinite**. Concretely, along $\dot\mu=(1,1)$ the joint form is
$2+2\rho$ and the product is $2(1-\rho^2)$, a difference $2\rho(1+\rho)>0$ for $\rho>0$;
along $\dot\mu=(1,-1)$ the joint form is $2-2\rho$ and the product is $2(1-\rho^2)$, a
difference $2\rho(\rho-1)<0$. So **no Loewner ordering between the joint pullback and the
weighted product of marginal fiber metrics holds in general, in either direction.** Any
statement that the marginal sum bounds the joint metric, or is bounded by it, is refuted
by this witness.

**(C3) Exact equality criterion.** With unit weights, equality holds if and only if
$\lVert L-L_b-L_m\rVert^2=2\langle L_b,L_m\rangle$. The clean sufficient structural
condition is **independence**: if $Y_b\perp Y_m$ under $r_\zeta$ for all $\zeta$ near the
base point, then $\log r_\zeta=\log r^b_\zeta+\log r^m_\zeta$, so $L=L_b+L_m$ with
$L_b=L_b(Y_b)$, $L_m=L_m(Y_m)$ centered and independent; the residual vanishes and
$\langle L_b,L_m\rangle=\mathbb E L_b\cdot\mathbb E L_m=0$. Hence equality with unit
weights. The Gaussian instance confirms this: $\rho=0$ makes the difference matrix zero.

**(C4) Nonunit weights are incompatible with exactness.** Suppose $Y_b\perp Y_m$ and both
marginal Fisher forms are nondegenerate. Then exactness of
$w_b g^F_b+w_m g^F_m=\iota^*G^F$ **for every tangent direction** requires
$(w_b-1)\lVert L_b\rVert^2+(w_m-1)\lVert L_m\rVert^2=0$ identically, which under
nondegeneracy forces $w_b=w_m=1$. So the arbitrary positive constants of
`hyp:pb-weighted-product-geometry` are a declared modeling choice; they can be exact only
at unit value, and only under independence.

**(C5) "Fixed copula" does not suffice.** If $r_\zeta$ has density
$c\big(F^b_\zeta(y_b),F^m_\zeta(y_m)\big)\,r^b_\zeta(y_b)\,r^m_\zeta(y_m)$ with the copula
density $c$ held fixed, the joint score still contains
$\partial_\zeta\log c(F^b_\zeta,F^m_\zeta)$, which is generally nonzero because the
marginal transforms $F^b_\zeta,F^m_\zeta$ move with $\zeta$. Only the **independence
copula** $c\equiv1$ gives additivity. The phrase "fixed dependence" in
`hyp:hist-exact-vfe-lift` must therefore be read as the independence-copula condition or
as the literal identity (4.1)$=0$; it is not discharged by fixing an arbitrary copula.

### 4.4 The full declaration set for an integrated configuration metric

Passing from the pointwise identity to a configuration metric requires all of the
following, and none is supplied by the bundle data:

1. **Base measure** $\mu_i$: a finite positive Borel measure on $\mathcal C_i$. Different
   $\mu_i$ give inequivalent metrics; see §6.2 for the reversal witness.
2. **Channel weights** $w_b,w_m:\mathcal C_i\to(0,\infty)$, measurable, and two-sidedly
   bounded if the metric is to be strong (Proposition 3.4).
3. **Cross terms.** The joint pullback has $b$–$m$ cross terms of size
   $\langle L_b,L_m\rangle$; the product metric has none by construction. Suppressing them
   is exactly the error (C2) refutes.
4. **Dependence / copula.** The lift $\iota_i$, not the pair of marginal sections,
   determines the dependence coordinates, and therefore determines $\mathsf G^F_i$. Two
   right inverses of the same $\pi^{\mathrm{conf}}$ give different metrics: on
   $\{0,1\}^2$, the product lift $(p,q)\mapsto\mathrm{Ber}(p)\otimes\mathrm{Ber}(q)$ gives
   the block-diagonal $dp^2/(p(1-p))+dq^2/(q(1-q))$, while a lift holding a nonzero
   correlation fixed gives a metric with a nonvanishing interaction residual by (C3).
   **The configuration Fisher metric is not a function of the displayed configuration.**
5. **Contextual locality.** Writing the configuration metric as a single integral
   $\int_{\mathcal C_i}[\cdots]\mu_i(dc)$ presumes that the joint-law Fisher metric has no
   cross-*context* terms, that is, that the declared $\mathfrak R_B$ factorizes over
   contexts or that $\pi^{\mathrm{conf}}$ reads only pointwise data. If the recognition
   law couples sections at $c\ne c'$, then $\iota_i^*G^F$ carries a double-integral term
   that no single integral can represent. `eq:hist-continuum-clock-speed`
   (`05d_relational_inference.tex:495-502`) presents the single-integral form without
   naming this hypothesis; it should.
6. **Gauge quotient rule**, per §3.5.
7. **Finiteness**: square-integrability of evaluation velocities against $w\,\mu_i$.
8. **Nondegeneracy**: condition (3.2), which in the finite-design case is the rank count
   of §3.3.

---

## 5. Typing the configuration coarse map, and projectability

### 5.1 Six distinct arrows, and a live symbol collision

At each scale step the manuscript carries at least six different "coarse" arrows:

| Tier | Arrow | Type | Source location |
| --- | --- | --- | --- |
| law | $K_\ell$ | Markov kernel $\mathsf X_\ell\rightsquigarrow\mathsf X_{\ell+1}$ | `07_general_renormalization.tex:110-125` |
| action | $\mathcal R^H$, $\overline U_\ell$ | nonlinear map on the $L^\infty$ action quotient; derivative $U_\ell$ | `07b_agent_network_rg.tex:185-190` |
| interaction | $M_\ell=P_{\ell+1}\overline U_\ell E_\ell$ | bounded map of Hoeffding spaces | `07b_agent_network_rg.tex:1161-1197` |
| bundle | $C_{\ell,s}$ | associated-bundle morphism covering $c_\ell$ | `07_general_renormalization.tex:253-259` |
| reference space | $\widehat{\mathcal R}_\ell=I_{\ell+1}C_{\ell,\ell+1}I_\ell^{-1}$ | endomorphism of $\mathfrak X_\star$ | `07_general_renormalization.tex:45-48` |
| **configuration** | currently $\mathcal R$, $\mathcal R_\ell$ | smooth map $\mathcal Q_\ell\to\mathcal Q_{\ell+1}$ | `05d_relational_inference.tex:719-746`, `769-783` |

The symbol $\mathcal R$ is presently assigned to **four** distinct objects in the
manuscript: the root-vertex set $\mathcal R=\{r:\operatorname{pa}(r)=\varnothing\}$
(`04_generative.tex:22`; used in `05_elbo.tex:395-434`); the VFE descent ray
$\mathcal R^-_{\mathcal F_i}$ (`05d_relational_inference.tex:287`); the action map
$\mathcal R^H$ (`07b_agent_network_rg.tex:185`); and the configuration coarse map
(`05d_relational_inference.tex:719`). It differs from the reference-space endomorphism
$\widehat{\mathcal R}_\ell$ only by a hat, and the notation appendix
(`appendix_notation.tex`) has **no row for a configuration coarse map** — the appendix
lists $\mathfrak S_i$, $\mathscr H_i$, $\Sigma_i$, $\pi^{\mathrm{conf}}_i$, $\iota_i$,
$\overline{\mathcal F}_{B,o}$, $\mathsf G^F_i$, and the clock triple, but nothing of type
$\mathcal Q_\ell\to\mathcal Q_{\ell+1}$. The falsifier recorded in the ledger for
`configuration-map` — "a configuration symbol already assigned to a reference-space
endomorphism" — is therefore live in substance. §8 closes that claim `OPEN` with the
rename obligation $\widehat R_\ell$ specified by the plan's Task 10 Step 5.

### 5.2 Theorem D — descent of a pointwise bundle morphism

**Theorem D.** Let $f:\mathcal C\to\bar{\mathcal C}$ be smooth and surjective, let
$\varpi:E\to\mathcal C$ and $\bar\varpi:\bar E\to\bar{\mathcal C}$ be smooth fiber
bundles, and let $\Psi:E\to\bar E$ be a smooth bundle morphism over $f$. Let
$s\in\Gamma(E)$.

1. *(Existence.)* There exists a map $\bar s:\bar{\mathcal C}\to\bar E$ with
   $\Psi\circ s=\bar s\circ f$ **if and only if** $\Psi\circ s$ is constant on the fibers
   of $f$: $f(c)=f(c')\Rightarrow\Psi(s(c))=\Psi(s(c'))$. When it exists it is unique, and
   it is automatically a section: $\bar\varpi(\bar s(\bar c))=\bar\varpi(\Psi(s(c)))=f(\varpi(s(c)))=f(c)=\bar c$.
2. *(Smoothness.)* If in addition $f$ is a **surjective submersion**, then $\bar s$ is
   smooth.
3. *(Sharpness.)* Without the submersion hypothesis, (2) can fail: a smooth surjection
   need not be a smooth quotient map, and the induced $\bar s$ need only be continuous.
   Without surjectivity, $\bar s$ is determined only on $f(\mathcal C)$ and extension is a
   separate obligation.

*Proof.* (1) Necessity is immediate from $\Psi(s(c))=\bar s(f(c))$. For sufficiency,
surjectivity lets one define $\bar s(\bar c):=\Psi(s(c))$ for any $c\in f^{-1}(\bar c)$;
fiber constancy makes this independent of the choice; the section property is the
displayed computation. (2) is the standard descent theorem for surjective submersions: a
smooth map constant on the fibers of a surjective submersion descends smoothly (Lee,
*Introduction to Smooth Manifolds*, 2nd ed., Thm. 4.30, applied to $\Psi\circ s$ with
quotient map $f$; the hypotheses required are exactly "surjective smooth submersion" and
"constant on fibers", both assumed here). $\square$

`05c_pullback_geometry.tex:584-593` adopts the section relation
`eq:pb-coarse-related-sections` as a `HYPOTHESIS` and correctly observes that for a
surjective submersion it "excludes fine sections whose $\Psi$-images vary along a fiber of
$f$." What it does not supply is the converse direction (2), the failure mode (3), or any
witness that the exclusion has bite. Theorem D and §5.3 supply all three.

### 5.3 The circle-to-a-point counterexample, reconstructed

**Counterexample 5.1 (`CE-SECTION-DESCENT`, certified).** Take $\mathcal C=S^1$,
$\bar{\mathcal C}=\{*\}$, and $f\equiv *$. Note that $f$ **is** a surjective submersion —
every linear map onto the zero vector space is surjective — so this witness attacks the
descent hypothesis itself, not the smoothness step. Take the trivial bundles
$E=S^1\times\mathbb R$ and $\bar E=\{*\}\times\mathbb R$ with fiber the unit-variance
Gaussian location family (so a section is a mean field), and $\Psi=\mathrm{id}$ on fibers.
Take the fine section $Q(x)=\sin x$. Then $\Psi\circ Q=Q$ is not constant on
$f^{-1}(*)=S^1$, so by Theorem D(1) **no** $\bar s$ exists. The pointwise bundle morphism
induces no configuration map at $Q$.

**The failure is generic, not exceptional.** In the linear tier
$\mathcal Q=L^2(S^1;\mathbb R)$ of §3.4(b1), the set of descendable sections is exactly
the constants, a closed subspace of infinite codimension. So the pointwise-induced
configuration map has **empty interior domain**: it is defined on no open subset of
$\mathcal Q$, and in particular on no neighborhood of any nonconstant configuration. A
history theorem quantified over an open set of configurations therefore cannot use it.
This upgrades the register entry from "a bundle morphism does not induce a configuration
map on all section spaces" to the sharper "on a genuinely infinite-dimensional
configuration manifold it induces one nowhere."

### 5.4 Valid alternative I — gauge-equivariant fiberwise averaging

**Construction 5.2.** Let $f:\mathcal C\to\bar{\mathcal C}$ be measurable with
$\mathcal C,\bar{\mathcal C}$ standard Borel, let $\mu$ be a finite positive measure on
$\mathcal C$ with $\bar\mu:=f_\#\mu$, and let $\{\kappa_{\bar c}\}$ be a disintegration of
$\mu$ over $f$ (existence: standard-Borel disintegration). Let $\Psi:E\to\bar E$ be a
bundle morphism over $f$ whose target fiber $\bar{\mathcal B}$ is a convex subset of a
locally convex space on which the structure group acts by restrictions of linear maps
(Lemma 3.1's setting). Define
$$
\big(\widehat R\,s\big)(\bar c):=\int_{f^{-1}(\bar c)}\Psi\big(s(c)\big)\,\kappa_{\bar c}(dc).
\tag{5.1}
$$
Because $\Psi$ covers $f$, every integrand value lies in the **single** fiber
$\bar E_{\bar c}$, so the integral is a Bochner integral in one fiber. It lands in
$\bar{\mathcal B}$ by convexity and normalization of $\kappa_{\bar c}$. Because the
transition maps act linearly, the value is independent of the trivialization, so
$\widehat R\,s$ is a genuine section: (5.1) is **gauge equivariant**. Measurability of
$\bar c\mapsto(\widehat R s)(\bar c)$ follows from measurability of the disintegration;
smoothness requires the usual smooth-parameter-dependence hypotheses on $\kappa$.

On Counterexample 5.1 with $\kappa_*$ normalized arclength,
$(\widehat R\,Q)(*)=\frac1{2\pi}\int_0^{2\pi}\sin x\,dx=0$: the map is everywhere defined,
is a bounded linear operator $L^2(S^1)\to\mathbb R$ in the linear tier, and has kernel the
mean-zero fields. It is a legitimate coarse map that **loses information**; it is not a
descent, and it must not be described as one.

**Warning that must accompany (5.1).** The averaging map is a barycenter *in the fiber of
laws or of parameters*. It is **not** the pushforward of a Markov kernel on the sample
space, so Theorem B does not apply to it directly. §6.1 gives the correct Markov statement
that does apply.

### 5.5 Valid alternative II — a variational coarse map

**Construction 5.3.** Let $\mathscr D$ be a gauge-invariant contrast on the coarse fiber
and define
$$
\widehat R(s):=\operatorname*{arg\,min}_{\bar s\in\mathcal Q_{\ell+1}}
\int_{\mathcal C}\mathscr D\big(\Psi(s(c)),\,\bar s(f(c))\big)\,\mu(dc).
$$
Existence and uniqueness are separate obligations: they hold when the objective is
strictly convex and coercive in a declared chart, or when the coarse family is a regular
exponential family and the induced mean parameter lies in the interior of the natural
domain, in which case the minimizer is the moment-matching projection.

**Coherence check.** For the fixed-covariance Gaussian location tier with
$\mathscr D(p,q)=\lVert m_p-m_q\rVert^2_{\Sigma_0^{-1}}$, disintegrating $\mu$ over $f$
gives
$$
\int_{\bar{\mathcal C}}\Big[\int_{f^{-1}(\bar c)}\lVert m(c)-\bar m(\bar c)\rVert^2_{\Sigma_0^{-1}}\kappa_{\bar c}(dc)\Big]\bar\mu(d\bar c),
$$
minimized pointwise in $\bar c$ by $\bar m(\bar c)=\int m\,d\kappa_{\bar c}$. **The
variational coarse map reduces exactly to the averaging map (5.1)** in this tier. The two
alternatives are therefore not independent guesses; they agree where both are defined,
which is a nontrivial consistency check on both.

---

## 6. What fiberwise Fisher contraction does and does not imply for integrated configuration metrics and durations

### 6.1 A positive result: the integrated configuration metric *is* a joint Fisher information

The following identification is the bridge Task 10 item 6 requires, and it is what makes
the averaging coarse map of §5.4 amenable to Theorem B after all.

**Theorem G.** Let $\theta\mapsto s_\theta$ be a DQM family of sections, let $\kappa$ be a
probability measure on $\mathcal C$, and consider the **joint context-and-sample
experiment**
$$
\mathbb P_\theta(dc,dy):=\kappa(dc)\,p_{s_\theta(c)}(dy)\quad\text{on }\mathcal C\times\mathsf Y .
$$
Since $\kappa$ carries no $\theta$ dependence, the joint score is $\ell_{s_\theta(c)}(y)$
and
$$
I_{\mathbb P}(\theta)=\int_{\mathcal C} I_{p_{s_\theta(c)}}(\theta)\,\kappa(dc)
=\mathsf G^{\kappa}(\dot\theta,\dot\theta)\Big|_{\text{unit weights}} ,
\tag{6.1}
$$
that is, **the integrated configuration Fisher metric (3.1) with base measure $\kappa$ and
unit channel weights is exactly the Fisher information of the joint experiment.**
Moreover, "forget the context" is a deterministic, parameter-independent, normalized
Markov kernel $\mathcal C\times\mathsf Y\rightsquigarrow\mathsf Y$, whose pushforward is
the mixture $\bar P_\theta=\int p_{s_\theta(c)}\kappa(dc)$, so Theorems A and B give
$$
\bar\ell_\theta(y)=\mathbb E_{\mathbb P_\theta}\big[\ell_{s_\theta(C)}(Y)\mid Y=y\big],
\qquad
\mathsf G^{\kappa}(\dot\theta,\dot\theta)-I_{\bar P}(\theta)[\dot\theta]
=\mathbb E\operatorname{Var}\big(\ell_{s_\theta(C)}(Y)\mid Y\big)\ \ge\ 0 .
\tag{6.2}
$$

*Proof.* The joint density with respect to $\kappa\otimes\nu$ is
$p_{s_\theta(c)}(y)$, whose logarithm has $\theta$-derivative $\ell_{s_\theta(c)}(y)$;
the $\kappa$-factor contributes nothing. Squaring and integrating gives (6.1). The
forgetting kernel satisfies (H3), so (6.2) is Theorem B applied to $\mathbb P_\theta$.
$\square$

Theorem G says something sharper than "Fisher contracts": it says the *integrated
configuration metric* is an upper bound for the Fisher information of the mixture-averaged
coarse law, with the defect equal to the conditional variance of the score given the
observed sample — that is, exactly the information carried by *which context produced the
sample*. This is the precise sense in which averaging over the base loses information, and
it is the correct statement to attach to the averaging coarse map (5.1).

### 6.2 The base-measure and weight transformation, with an exact Jacobian

Pointwise, under the hypotheses of `thm:pb-pullback-fisher-defect`, one has on
$T_c\mathcal C$
$$
h_s^\omega-f^*h_{\bar s}^{\bar\omega}=(D^\omega s)^*\Delta^\Psi_F\succeq0 .
$$
Integrating requires a change of variables, and that is where the base measure enters.

**Theorem E (integrated contraction).** Let $V$ be a vector field on $\mathcal C$ that is
$f$-related to a vector field $\bar V$ on $\bar{\mathcal C}$, that is
$T_cf\,V(c)=\bar V(f(c))$ for all $c$. Then
$$
\int_{\mathcal C}\big(f^*\bar h_{\bar s}^{\bar\omega}\big)(V,V)\,d\mu
=\int_{\bar{\mathcal C}}\bar h_{\bar s}^{\bar\omega}(\bar V,\bar V)\,d(f_\#\mu) .
$$
Consequently, **if and only if $f_\#\mu=\bar\mu$**,
$$
\int_{\mathcal C}h_s^\omega(V,V)\,d\mu
\;-\;\int_{\bar{\mathcal C}}\bar h_{\bar s}^{\bar\omega}(\bar V,\bar V)\,d\bar\mu
=\int_{\mathcal C}\big[(D^\omega s)^*\Delta^\Psi_F\big](V,V)\,d\mu\;\ge\;0 .
\tag{6.3}
$$
If instead $f_\#\mu\ll\bar\mu$ with Radon–Nikodym density $J=d(f_\#\mu)/d\bar\mu$, the
coarse integral acquires the weight $J$:
$$
\int_{\mathcal C}\big(f^*\bar h\big)(V,V)\,d\mu=\int_{\bar{\mathcal C}}\bar h(\bar V,\bar V)\,J\,d\bar\mu .
\tag{6.4}
$$
*Proof.* The first display is the abstract change-of-variables formula for a pushforward
measure applied to the nonnegative measurable function
$c\mapsto\bar h(\bar V,\bar V)(f(c))$; (6.4) is the same with the density inserted; (6.3)
is then the pointwise inequality integrated. $\square$

**Counterexample 6.1 (base measure alone reverses the contraction).** Let
$\mathcal C=\bar{\mathcal C}=\{1,2\}$ with the discrete structure, $f=\mathrm{id}$, and
$\Psi$ the identity fiber map, so that $\Delta^\Psi_F=0$ and $h=f^*\bar h$ **pointwise
with equality**. Take $h(1)=0$, $h(2)=1$ on the relevant tangent direction, and take
$\mu=\delta_1$, $\bar\mu=\delta_2$. Then the fine integrated metric is $0$ and the coarse
integrated metric is $1$: the coarse integrated metric strictly exceeds the fine one even
though the fiberwise defect vanishes identically. The same reversal is produced by
channel weights alone, taking $\mu=\bar\mu$ and $\bar w>w$. **Fiberwise Fisher contraction
carries no information whatever about integrated configuration metrics until $f_\#\mu=\bar\mu$
and $\bar w\circ f\le w$ are separately declared and proved.**

### 6.3 Durations: the exact criterion, and why contraction does not supply it

**Theorem F (duration comparison).** Let $\widehat R_\ell:\mathcal Q_\ell\to\mathcal Q_{\ell+1}$
be smooth, let $Q:I\to\mathcal Q_\ell$ be a $C^1$ regular curve, and let
$\tau_\ell,\tau_{\ell+1}$ be the cumulative Fisher clocks of
`def:hist-fisher-clock`. If
$$
\widehat R_\ell^{\,*}\,\mathsf G_{\ell+1}\ \preceq\ \mathsf G_\ell
\qquad\text{along the curve,}
\tag{6.5}
$$
then for corresponding subarcs $\tau_{\ell+1}\big(\widehat R_\ell\circ Q\big)\le\tau_\ell(Q)$.

*Proof.* The image curve has velocity $T\widehat R_\ell\,\dot Q$, so its Fisher speed is
$\sqrt{\mathsf G_{\ell+1}(T\widehat R_\ell\dot Q,T\widehat R_\ell\dot Q)}
=\sqrt{(\widehat R_\ell^{\,*}\mathsf G_{\ell+1})(\dot Q,\dot Q)}\le\sqrt{\mathsf G_\ell(\dot Q,\dot Q)}$.
Integrate; reparameterization invariance (`thm:hist-fisher-clock-invariance`) makes the
comparison independent of the parameterization. $\square$

Two separations are forced by this proof and are routinely conflated.

*(i) Semiconjugacy is not needed for Theorem F, and Theorem F is not needed for
semiconjugacy.* Theorem F compares a fine curve with **its own image** and uses only
$T\widehat R_\ell$. The oriented semiconjugacy condition
$T\widehat R_\ell X_\ell=a_\ell\,(X_{\ell+1}\circ\widehat R_\ell)$, $a_\ell>0$
(`prop:hist-oriented-semiconjugacy`), is what additionally identifies that image with an
**independently recomputed** coarse natural-gradient orbit. Either without the other
leaves a gap, exactly as `05d_relational_inference.tex:753-762` states.

*(ii) Hypothesis (6.5) does not follow from fiberwise Fisher contraction.* This is the
substance of the register entry `CE-DURATION-MISMATCH`, and it is here reconstructed and
strengthened into a statistically admissible witness.

**Counterexample 6.2 (`CE-DURATION-MISMATCH`, certified, with a statistical realization).**
Take $\mathcal Q_\ell=\mathcal Q_{\ell+1}=\mathbb R$, $\widehat R_\ell=\mathrm{id}$,
$X_\ell=X_{\ell+1}=-\partial_x$ — so the semiconjugacy holds with $a\equiv1$ — and the two
configuration metrics $\mathsf G_\ell=dx^2$, $\mathsf G_{\ell+1}=4\,dx^2$. Then
$\nu^{(\ell)}_F\equiv1$ and $\nu^{(\ell+1)}_F\equiv2$, so the coarse Fisher duration is
**twice** the fine duration: (6.5) fails and the conclusion of Theorem F fails with it.

This is not a pathological metric choice. Realize $\mathcal Q_\ell$ as the location family
$\{\mathcal N(x,1):x\in\mathbb R\}$, whose Fisher metric is $dx^2$, and $\mathcal Q_{\ell+1}$
as the four-fold independent replication $\{\mathcal N(x\mathbf 1_4,I_4)\}$, whose Fisher
metric is $4\,dx^2$. The map $\widehat R_\ell=\mathrm{id}$ on the parameter is smooth, and
both are legitimate configuration manifolds under `H-CONFIG`. What the replication is
**not** is a Markov pushforward: it is exactly the extensive score lift $\mathscr I_b$ of
`prop:rg-score-block-lift` (`07b_agent_network_rg.tex:601-646`), whose norm is
$\lVert\mathscr I_b\rVert=\sqrt b>1$. So the same finite-network construction that carries
the *relevant* modes of Task 9 is the mechanism that makes coarse duration exceed fine
duration.

**The reconciliation, stated once.** Theorem B contracts along **one** parameter-independent
Markov arrow at a fixed statistical experiment. The configuration tier composes that arrow
with an **extensive replication** $\mathscr I_b$ of norm $\sqrt b$ and with an integration
against a possibly different base measure and weights (§6.2). The composite
$\mathscr L_b=U_b\mathscr I_b$ has $\lVert\mathscr L_b\rVert\le\sqrt b$, not $\le1$
(`thm:rg-score-pushforward-defect`, `07b_agent_network_rg.tex:654-683`). There is no
contradiction, and no route from Theorem B to (6.5). This is the configuration-tier form
of the plan's global constraint that normalized action and score contraction must not be
used to infer the absence of relevant extensive modes.

### 6.4 Noncollapse

**Proposition 6.3 (`CE-HISTORY-COLLAPSE`, certified; and the repair).** The oriented
semiconjugacy equation alone permits total collapse: take $\widehat R_\ell\equiv Q^*$
constant and $X_{\ell+1}\equiv0$. Then $T\widehat R_\ell X_\ell=0=a\,(X_{\ell+1}\circ\widehat R_\ell)$
for every $a>0$, so the equation holds, while every nonconstant fine orbit maps to the
single point $Q^*$ and every coarse Fisher duration is zero. A nonconstant shared history
therefore requires the **additional** hypotheses

1. $T_{Q}\widehat R_\ell\,X_\ell(Q)\ne0$ on every nontrivial subarc — equivalently
   $X_{\ell+1}(\widehat R_\ell Q)\ne0$ there, given $a>0$; and
2. a maximal-interval condition: the coarse flow $\bar\Phi_u$ must exist on
   $\sigma_Q(I)=\int_0^\cdot a(\Phi_sQ)\,ds$, since finite $I$ can map to an interval on
   which $\bar\Phi$ blows up, and conversely.

*Proof of the collapse witness.* Both sides of the semiconjugacy equation vanish
identically. $\square$

The manuscript's `prop:hist-oriented-semiconjugacy` is itself correct — its uniqueness step
uses local Lipschitz dependence of $X_m$, which is supplied by `H-CONFIG` — but it is
stated for local flows and does not record either (1) or (2). Neither is implied by the
displayed equation.

---

## 7. Adversarial register for this route

Each row states the attack, the disposition, and the decisive object. `SUSTAINED` means
the attack survives and becomes an obligation; `REJECTED` means the derivation above
answers it; `PARTIAL` means it survives in a narrowed form.

| ID | Attack | Disposition | Decisive object |
| --- | --- | --- | --- |
| A-1 | Singular Fisher strata invalidate the rank/quotient theory | REJECTED for the stated theorems, SUSTAINED as a domain restriction | `eq:pb-rank-jump-example`: $s(x)=\mathcal N(x^2,1)$ over $\mathbb R$ gives $h_s=4x^2dx^2$ (score direction $2x$, location Fisher $1$), rank $1$ off the origin and $0$ at it, so pointwise quotients do not assemble into a vector bundle. `thm:pb-pullback-rank-quotient` correctly assumes constant rank. The configuration manifolds of §3 must exclude such loci or restrict to a regular stratum. |
| A-2 | Constant rank suffices for a quotient manifold | REJECTED | `prop:pb-contact-null-counterexample`: $\alpha=dz-x\,dy$ on $\mathbb R^3$ gives $h_s^\omega=\alpha^2$ of constant rank one with $\alpha\wedge d\alpha=-dz\wedge dx\wedge dy\ne0$, so $\ker\alpha$ is contact, not integrable. Involutivity, a regular leaf space, and basicness (`eq:pb-null-basicness`) are three further hypotheses. |
| A-3 | Fisher-metric completeness at a variance boundary | REJECTED | For $\mathcal N(0,\sigma^2)$ the Fisher line element in $\sigma$ is $\sqrt2\,d\sigma/\sigma$, so $\sigma\to0^+$ has infinite Fisher length: the degenerate boundary is not reachable in finite duration. The Gaussian natural-domain boundary of SPEC §5d.3 is at infinite information distance and cannot be crossed by a finite-duration history. |
| A-4 | Nonclosed gauge orbits break the quotient clock | SUSTAINED, narrowed | Counterexample 3.8: $h^1$ acting by translation on $\ell^2$ is free and isometric with dense orbit tangent, so the quotient speed is identically zero. Proposition 3.7 shows that in the strong Hilbert tier **closedness of the orbit tangent** is the exact repair. The manuscript's "free, proper, and isometric is not enough" remains without a witness (properness would force closed orbits); recorded as an obligation, not repaired. |
| A-5 | Weak metrics admit no natural gradient | SUSTAINED | Counterexample 3.5: $\mathcal Q=H^1(S^1)$, $\mathsf G=L^2$, $\mathcal F=\tfrac12\int|Q'|^2$, $Q=\sum k^{-2}\sin k\theta\in H^1\setminus H^2$; the gradient equation demands $-Q''=\sum\sin k\theta\notin L^2$. The Riesz hypothesis of Corollary 3.6 is genuinely extra. |
| A-6 | A missing joint-law lift makes $\mathsf G^F_i$ undefined or ambiguous | SUSTAINED | §4.4(4): on $\{0,1\}^2$ the product lift and a fixed-correlation lift are both smooth right inverses of the same $\pi^{\mathrm{conf}}$ and induce **different** metrics; the pair of marginal sections does not determine the configuration Fisher metric. `hyp:hist-exact-vfe-lift` is load bearing and its existence half remains `OPEN` (`appendix_claim_ledger.tex:50-56`). |
| A-7 | Parameter-dependent kernels break Theorem A | REJECTED as an attack on the theorem, SUSTAINED as a scope fence | With a dominated channel of density $k_\lambda(y\mid x)$ the output score is $\mathbb E[\ell^X_\lambda+\partial_\lambda\log k_\lambda(Y\mid X)\mid Y]$ (`eq:hist-parameter-dependent-channel-score`), which can **create** information: a parameter-independent input with a channel emitting $\mathrm{Bernoulli}((1+e^{-\lambda})^{-1})$ has zero fine Fisher speed and output Fisher speed $\sigma(\lambda)(1-\sigma(\lambda))>0$, since $\sigma'=\sigma(1-\sigma)$. (H3) is not decorative. |
| A-8 | Conditional-score version issues undermine the bundle statement | PARTIAL | The Fisher forms of §1 are version independent, being $L^2$ norms. What is *not* supplied is a jointly measurable, $\theta$-smooth **selection** of versions across $\theta$ and across varying $L^2(P^Y_\theta)$; that is required for $\Psi$ to be a smooth bundle morphism (§1.5) and is an obligation. The register's `CE-RCP-EXCEPTION` is the same phenomenon at the RCP level. |
| A-9 | Marginal and joint Fisher geometry are equal | REFUTED | Theorem C and §4.3(C2): with jointly Gaussian precision $\begin{psmallmatrix}1&\rho\\ \rho&1\end{psmallmatrix}$ the difference $\Lambda-(1-\rho^2)I_2$ has determinant $\rho^2(\rho^2-1)<0$, hence is **indefinite**. No ordering holds in either direction, and equality with unit weights holds under independence. |
| A-10 | Positivity of the base defect survives a nonzero horizontal defect | REFUTED | Counterexample 7.1 below. |
| A-11 | A pointwise bundle morphism induces a configuration map | REFUTED | Counterexample 5.1, strengthened in §5.3 to "nowhere defined on an infinite-dimensional configuration manifold". |
| A-12 | Semiconjugacy gives a nonconstant shared history | REFUTED | Proposition 6.3. |
| A-13 | Fiberwise contraction gives duration contraction | REFUTED | Counterexample 6.2, with the extensive-replication realization. |
| A-14 | Integrated metrics inherit pointwise contraction | REFUTED | Counterexample 6.1: with a vanishing fiberwise defect, differing base measures reverse the inequality. |

**Counterexample 7.1 (`CE-HORIZONTAL-ANOMALY`, certified).** Take the trivial line bundle
$E=\bar E=\mathbb R_x\times\mathbb R_y\to\mathbb R_x$ with the unit-variance Gaussian
location fiber (so $g^F_{yy}=1$), $f=\mathrm{id}$, $\Psi=\mathrm{id}$, the zero section
$s=\bar s$, source horizontal distribution $H^\omega=\operatorname{span}\{\partial_x\}$
and target $H^{\bar\omega}=\operatorname{span}\{\partial_x+a\,\partial_y\}$ with $a\ne0$.
Then $D^\omega s(\partial_x)=\operatorname{ver}^\omega(\partial_x)=0$, so $h_s^\omega=0$;
while $\partial_x=(\partial_x+a\partial_y)-a\partial_y$ gives
$D^{\bar\omega}\bar s(\partial_x)=-a\,\partial_y$ and $h_{\bar s}^{\bar\omega}=a^2dx^2$.
Hence
$$
h_s^\omega-f^*h_{\bar s}^{\bar\omega}=-a^2\,dx^2\ \prec\ 0 ,
$$
**negative**, even though $\Psi$ is the identity and $\Delta^\Psi_F=0$. The horizontal
defect is $(\mathcal D\Psi)(\partial_x)=\partial_x-(\partial_x+a\partial_y)=-a\partial_y\ne0$,
so the hypothesis $\mathcal D\Psi=0$ of `thm:pb-pullback-fisher-defect` is violated: the
theorem is not contradicted, but any statement of base-level positivity without that
hypothesis is refuted.

**The exact retained form.** Writing $A:=T^V\Psi(D^\omega sX)$ and
$B:=(\mathcal D\Psi)_{s(c)}(X)$, the first-jet chain rule
`eq:pb-covariant-jet-chain-rule` gives $D^{\bar\omega}\bar s(TfX)=A+B$ and hence
$$
h_s^\omega(X,X)-f^*h_{\bar s}^{\bar\omega}(X,X)
=\underbrace{\big[(D^\omega s)^*\Delta^\Psi_F\big](X,X)}_{\ge0\text{ under (H3), (H5)}}
\;-\;2\,\bar g^F(A,B)\;-\;\bar g^F(B,B).
\tag{7.1}
$$
The anomaly contributes a **nonpositive** quadratic term $-\bar g^F(B,B)$ and a
**sign-indefinite** cross term $-2\bar g^F(A,B)$. In Counterexample 7.1, $A=0$ kills the
cross term and the total is $-a^2$. Identity (7.1) is what `horizontal-defect-anomaly`
asks for, and it is not displayed anywhere in `05c_pullback_geometry.tex`, which states
only the zero-defect case.

---

## 8. Claim dispositions

### 8.1 Two bundle lemmas, proved here because the manuscript asserts them

**Lemma 8.1 (associated-bundle descent).** With
$\mathcal P_\ell(p\cdot g)=\mathcal P_\ell(p)\cdot\kappa_\ell(g)$
(`eq:rg-principal-scale-map`) and the fiber intertwiner
$q_{\ell,s}\circ\widehat\rho_{\ell,s}(g)=\widehat\rho_{\ell+1,s}(\kappa_\ell(g))\circ q_{\ell,s}$
(`eq:rg-scale-intertwiner`), the assignment
$C_{\ell,s}[p,z]:=[\mathcal P_\ell(p),q_{\ell,s}(z)]$ is well defined on the associated
quotient and covers $c_\ell$.

*Proof.* Under the quotient convention $[p,z]=[p g,\widehat\rho_{\ell,s}(g)^{-1}z]$,
$$
C_{\ell,s}\big[pg,\widehat\rho_{\ell,s}(g)^{-1}z\big]
=\big[\mathcal P_\ell(p)\kappa_\ell(g),\,q_{\ell,s}\big(\widehat\rho_{\ell,s}(g)^{-1}z\big)\big]
=\big[\mathcal P_\ell(p)\kappa_\ell(g),\,\widehat\rho_{\ell+1,s}(\kappa_\ell(g))^{-1}q_{\ell,s}(z)\big]
=\big[\mathcal P_\ell(p),q_{\ell,s}(z)\big].
$$
Covering $c_\ell$ is the base equivariance of $\mathcal P_\ell$. $\square$

Conversely, if the intertwiner fails, two representatives of one associated point map to
different target classes and the assignment is not a map — which is exactly the falsifier
recorded for `bundle-morphism-descent`. The manuscript's caution at
`07_general_renormalization.tex:321-322` is also correct: for a nonfaithful representation,
vanishing of the *represented* transport defect does not recover the principal identity
`eq:rg-principal-connection-naturality`.

**Lemma 8.2 (scale cocycle).** If $c$, $\kappa$, $\mathcal P$, and $q_{\cdot,s}$ each
satisfy their own identity and ordered composition laws, then so does $C_{\cdot,s}$:
$C_{\ell+1,s}\circ C_{\ell,s}=C_{\ell\to\ell+2,s}$ and $C_{\ell\to\ell,s}=\mathrm{id}$.

*Proof.* $C_{\ell+1,s}C_{\ell,s}[p,z]=[\mathcal P_{\ell+1}\mathcal P_\ell(p),\,q_{\ell+1,s}q_{\ell,s}(z)]$,
and the hypotheses identify the two components with $\mathcal P_{\ell\to\ell+2}$ and
$q_{\ell\to\ell+2,s}$; the composite is equivariant with respect to
$\kappa_{\ell+1}\kappa_\ell$, so Lemma 8.1 applies to it. Identity is immediate. $\square$

Lemma 8.2 is a *conditional* statement, and that is precisely what the claim asserts:
without the component composition laws, adjacent arrows form only a sequence of coarse
steps, not a functor. The rightmost factor acts first; a two-parameter cocycle is not a
semigroup (register entry `CE-MODE-ORDER`).

### 8.2 Dispositions

| Claim | Disposition | Basis | Exact remaining obligation |
| --- | --- | --- | --- |
| `score-action-compatibility` | **PROVED** | §2.1–2.4: (2.1) representative independence; (2.2) Fisher isometry; §2.3 dense proper range and the $L^2/\mathbb R\mathbf 1$ isomorphism; (2.3) the centering/conditional-expectation square; (2.4) the $L^2$ defect equals the Fisher loss. | Record in `07b_agent_network_rg.tex` that on $L^2/\mathbb R\mathbf 1$ the realizing path is the quadratic DQM path of `lem:rg-dqm-realization`, **not** the exponential-action path, and that `thm:rg-bounded-action-calculus` is undefined there. Without that sentence the true $L^2$ statement can be misread as extending the nonlinear chart (`CE-ACTION-LP`). |
| `bundle-fisher-defect` | **PROVED** under named hypotheses | Theorems A and B, and (1.3). Positivity and the conditional-covariance identity are established with all interchange burden discharged by Lemmas 1.1–1.2 (no differentiation under an integral is used). | Name **(H5) family closure** as a hypothesis of `thm:pb-pullback-fisher-defect` in `05c_pullback_geometry.tex:675-700`, and record that $T^V\Psi$ *is defined* as the induced score map $R_p$ rather than assumed to exist. Add the version-selection obligation of §1.5 for smoothness of $p\mapsto T^V_p\Psi$. |
| `bundle-morphism-descent` | **PROVED** | Lemma 8.1. | None mathematical. Retain the nonfaithful-representation caveat already at `07_general_renormalization.tex:321-322`. |
| `bundle-scale-cocycle` | **PROVED** (conditionally, as stated) | Lemma 8.2. | Display the two-line verification in `07_general_renormalization.tex:260-264`, which currently asserts the composition law without proof. |
| `horizontal-defect-anomaly` | **PROVED**, and its counterexample certified | Identity (7.1) with both signed terms; Counterexample 7.1 with the explicit computation $h_s^\omega=0$, $h_{\bar s}^{\bar\omega}=a^2dx^2$, difference $-a^2dx^2\prec0$. Register entry `CE-HORIZONTAL-ANOMALY` moves from `CANDIDATE` to reconstructed. | Display (7.1) in `05c_pullback_geometry.tex` immediately after `eq:pb-covariant-jet-chain-rule`; the chapter currently states only the $\mathcal D\Psi=0$ case, so the signed cross term and the nonpositive quadratic anomaly appear nowhere. |
| `pullback-compatibility` | **PROVED** under its stated hypotheses | `thm:pb-pullback-fisher-defect` with (H3), (H5), related sections, and $\mathcal D\Psi=0$; the derivation is reproduced at (1.3) and §1.6. | Record the minimality of §1.6: the base cocycle (1.5) needs only $\mathcal D\Psi_{01}=0$ and the *fine* section relation. The 2026-08-01 wiki record's "compatible connections and related sections at each scale" is sufficient but not minimal (§0.3(3)). |
| `configuration-fisher-metric` | **OPEN** | The manuscript exhibits no configuration manifold, proves no nonemptiness, and performs no strong-metric verification (§3.1). §§3.2–3.5 discharge the **existence** half: Lemma 3.1 (nonemptiness with its non-contractible-fiber boundary), Construction 3.2 and Proposition 3.3 (finite-dimensional tier with the exact nondegeneracy criterion (3.2) and its Gram/rank instance), Proposition 3.4 (strong $L^2$ tier under boundedness and coercivity), Counterexample 3.5 and Corollary 3.6 (the weak-metric failure and the exact Riesz hypothesis), Proposition 3.7 and Counterexample 3.8 (gauge quotient). | Import Construction 3.2, Proposition 3.4, and Counterexample 3.5 into `05d_relational_inference.tex` next to `hyp:hist-regular-metric-domain`, and choose explicitly between dichotomy (i) and (ii) of §3.4. Supply a *free, proper, and isometric* infinite-dimensional witness for the sentence at `05d_relational_inference.tex:529-536`, or restate it as Proposition 3.7 plus the Banach complementedness caveat. |
| `configuration-map` | **OPEN** | §5.1: $\mathcal R$ is assigned to four distinct objects across `04_generative.tex:22`, `05_elbo.tex:395`, `05d_relational_inference.tex:287`, `05d_relational_inference.tex:719`, and differs from the reference-space endomorphism $\widehat{\mathcal R}_\ell$ (`07_general_renormalization.tex:45-48`) only by a hat. `appendix_notation.tex` has no row of type $\mathcal Q_\ell\to\mathcal Q_{\ell+1}$. The ledger's own falsifier condition is met in substance. | Rename the configuration coarse map to $\widehat R_\ell$ throughout `05d_relational_inference.tex` (plan Task 10 Step 5's symbol), add a notation-appendix row stating its type $\mathcal Q_\ell\to\mathcal Q_{\ell+1}$ and its non-identification with $K_\ell$, $\mathcal R^H$, $M_\ell$, $C_{\ell,s}$, and $\widehat{\mathcal R}_\ell$, and add the smoothness requirement that its tangent map exist (needed by `history-semiconjugacy`). |
| `configuration-projectability` | **PROVED**, counterexample certified | Theorem D (existence iff fiber constancy; smoothness under a surjective submersion; sharpness); Counterexample 5.1 with the observation that $S^1\to\{*\}$ *is* a surjective submersion, so the failure is in descent, not smoothness; §5.3's strengthening to empty interior domain; Constructions 5.2 and 5.3 as valid alternatives, with the coherence check that they coincide in the Gaussian location tier. Register entry `CE-SECTION-DESCENT` moves from `CANDIDATE` to reconstructed. | State Theorem D and at least one of Constructions 5.2, 5.3 in `05c_pullback_geometry.tex:584-593`, which currently adopts the descent relation as a hypothesis with neither a converse, a witness, nor an alternative. Attach the warning of §5.4 that averaging is not a Markov pushforward, together with Theorem G as the statement that *is* available. |
| `history-semiconjugacy` | **PROVED** | `prop:hist-oriented-semiconjugacy` verified: both sides of `eq:hist-oriented-flow-semiconjugacy` solve $\dot u=a(\Phi_tQ)X_m(u)$, $u(0)=\mathcal RQ$; uniqueness uses local Lipschitz dependence of $X_m$, supplied by `H-CONFIG`; the converse is the chain rule at $t=0$. | Record the maximal-interval qualifier: the identity holds on the common interval of existence, and $\sigma_Q(I)$ must lie in the coarse flow's interval (§6.4(2)). |
| `history-noncollapse` | **PROVED**, counterexample certified | Proposition 6.3: $\widehat R_\ell\equiv Q^*$ with $X_{\ell+1}\equiv0$ satisfies the semiconjugacy equation for every $a>0$ while collapsing every orbit. The two additional hypotheses are stated. Register entry `CE-HISTORY-COLLAPSE` moves from `CANDIDATE` to reconstructed. | Add hypotheses (1) and (2) of Proposition 6.3 wherever nonconstant or global shared-history language is used, including `05d_relational_inference.tex:764-786`. |
| `history-duration-relation` | **PROVED**, counterexample certified | Theorem F with criterion (6.5); Theorem E and (6.4) for the base-measure Jacobian; Counterexample 6.1 (reversal with vanishing fiberwise defect) and Counterexample 6.2 with the extensive-replication realization. Register entry `CE-DURATION-MISMATCH` moves from `CANDIDATE` to reconstructed and is strengthened to a statistically admissible witness. | State (6.5) explicitly as the duration hypothesis in `05d_relational_inference.tex:611-683`, and record §6.3's reconciliation: $\lVert\mathscr L_b\rVert\le\sqrt b$, not $\le1$, so no route runs from `thm:cg-fisher-contraction` to (6.5). |

**Summary.** Nine of the twelve in-scope claims close `PROVED`; none closes `REFUTED`;
two close `OPEN` (`configuration-fisher-metric`, `configuration-map`) with the exact
obligations above. `bundle-fisher-defect` closes `PROVED` under a hypothesis the
manuscript uses but does not name, so its obligation is a hypothesis-naming repair rather
than a mathematical gap. Four register entries that were `CANDIDATE`
(`CE-HORIZONTAL-ANOMALY`, `CE-SECTION-DESCENT`, `CE-HISTORY-COLLAPSE`,
`CE-DURATION-MISMATCH`) are reconstructed here with their decisive computations, which is
the reconstruction the register itself flags as owed at
`counterexample-register.md:59`.

**Effect on the target's dependency closure.** The target node depends on all twelve
claims through the edges at `dependency-dag.json:26-37`. Two `OPEN` ancestors mean the
target cannot reach `COMPLETE_AFFIRMATIVE` on this route. The correct terminal status for
this route considered alone is `INCONCLUSIVE`, with the strongest verified result being
the conjunction of §§1–7 under their named hypotheses. This record does not set a terminal
status for the run; that is the release artifact's function.

---

## 9. Independent reconstruction and oracle erasure

### 9.1 Independent reconstruction

Every load-bearing interface was re-derived from the frozen contract's declared types
without reading the manuscript's proof first, and then compared:

- *Score pushforward.* Reconstructed as Lemmas 1.1–1.2 plus Theorem A. Comparison: the
  manuscript's `thm:cg-fisher-contraction` proof (`06_general_coarsegraining.tex:192-199`)
  cites the $L^2$-projection theorem for parametrized-measure models and does not display
  Step 4 (transfer from the canonical path to an arbitrary DQM family). That step is
  necessary and is supplied here. No discrepancy in the conclusion.
- *Fisher defect.* Reconstructed as Theorem B from total covariance. Agrees with
  `eq:cg-fisher-loss` and `eq:pb-fisher-defect-score-variance`. The equality
  characterization required three qualifications (§1.4) not present in the manuscript's
  one-line statement; the conclusion is unchanged, the scope is narrowed.
- *Action/score square.* Reconstructed as (2.3) from $U\mathbf 1=\mathbf 1$ and the tower
  property, independently of `prop:rg-action-score-isometry`. Agrees. The scope split
  between $L^\infty/\mathbb R\mathbf 1$ and $L^2/\mathbb R\mathbf 1$ (§2.3) is a
  discrepancy between the ledger statement and the manuscript proposition; both are true,
  and the resolution is recorded rather than suppressed.
- *Cocycle.* Reconstructed as (1.4)–(1.5). Agrees with `thm:pb-fisher-defect-cocycle`, and
  yields a strictly weaker hypothesis than the 2026-08-01 record's (§0.3(3)).
- *Joint versus marginal.* Reconstructed as Theorem C from scratch. This has **no**
  manuscript counterpart: `hyp:hist-exact-vfe-lift` states the requirement and
  `hyp:pb-weighted-product-geometry` states the alternative, but neither the identity
  (4.1) nor the indefiniteness of the difference appears anywhere. Cross-checked against
  the manuscript's independent Gaussian machinery: the marginal mean-Fisher form
  $((\Lambda^{-1})_{bb})^{-1}$ is the Schur complement, matching
  `prop:ig-pullback-vs-pushforward` (`08_infogeometry.tex:279-290`) and
  `cor:ig-expectation-mean-quotient`. The two routes agree.
- *Descent.* Reconstructed as Theorem D from the smooth-submersion quotient theorem, then
  matched against `05c_pullback_geometry.tex:584-593`. The manuscript's parenthetical
  exclusion is the necessity half; the sufficiency half and the failure mode are new here.

### 9.2 Oracle erasure

The affirmative-existence instruction was removed from the working context and the closure
of every claim in §8.2 was recomputed. Findings:

1. No premise, hypothesis, lemma, theorem, counterexample, or disposition in §§1–8 cites
   the existence of an affirmative answer, the desirability of one, or any prior narrative
   about what the construction "should" yield. The hypotheses (H1)–(H5), `H-CONFIG`,
   `H-GAUGE`, `H-DQM`, `H-HISTORY` are taken from the frozen contract and the ledger's
   assumption list, not from the prior.
2. Two dispositions changed **against** the prior and were retained: `configuration-fisher-metric`
   and `configuration-map` close `OPEN`. A prior-driven pass would have been under pressure
   to close them `PROVED` on the strength of the declared hypotheses; the hypotheses are
   declarations, and a declaration with no exhibited model is not a theorem.
3. Four counterexamples were reconstructed to completion even though each *narrows* the
   affirmative construction. In particular Counterexample 6.2 was strengthened from the
   register's bare metric-scaling witness to a statistically admissible one, which makes it
   harder, not easier, to close the duration claim affirmatively.
4. Paraphrase scan: no sentence below asserts that a route "works", "goes through", or
   "confirms" a favored construction. Where a construction is supplied (§§3, 5.4, 5.5,
   6.1) it is supplied with its exact hypotheses and its failure witness adjacent.

Passing oracle erasure shows only that the prior was unnecessary to reach these
conclusions. It does not prove any theorem.

---

## 10. Minimal repairs, ordered by dependency

1. `05c_pullback_geometry.tex`, after `eq:pb-covariant-jet-chain-rule`: display the exact
   anomaly identity (7.1) with both signed terms, and attach Counterexample 7.1.
2. `05c_pullback_geometry.tex:675-700`: name **(H5) family closure** as a hypothesis of
   `thm:pb-pullback-fisher-defect`; state that $T^V\Psi$ is *defined* by the induced score
   map; add the version-selection obligation of §1.5.
3. `05c_pullback_geometry.tex:584-593`: state Theorem D, attach Counterexample 5.1, and add
   Construction 5.2 (or 5.3) with the warning that averaging is not a Markov pushforward
   and with Theorem G as the correct available contraction statement.
4. `05c_pullback_geometry.tex:779-808`: record the minimal hypothesis for the base cocycle
   (1.5): $\mathcal D\Psi_{01}=0$ and the fine section relation suffice.
5. `05d_relational_inference.tex`, at `hyp:hist-regular-metric-domain`: import
   Construction 3.2 with Proposition 3.3, Proposition 3.4, and Counterexample 3.5 with
   Corollary 3.6; declare which horn of the §3.4 dichotomy the theory takes.
6. `05d_relational_inference.tex:213-268`: add Theorem C, the equality criterion (C3), the
   unit-weight corollary (C4), the fixed-copula correction (C5), and the contextual-locality
   requirement §4.4(5); the last should also annotate `eq:hist-continuum-clock-speed`.
7. `05d_relational_inference.tex:509-536`: replace or supplement the gauge-quotient
   hypothesis with Proposition 3.7 and Counterexample 3.8, and either supply the
   free-proper-isometric witness or restate the sentence.
8. `05d_relational_inference.tex:611-786`: rename the configuration coarse map to
   $\widehat R_\ell$; add hypotheses (1) and (2) of Proposition 6.3; state (6.5) as the
   duration hypothesis and attach Counterexample 6.2 with the $\sqrt b$ reconciliation.
9. `07_general_renormalization.tex:260-264`: display the two-line proof of Lemma 8.2.
10. `07b_agent_network_rg.tex`, at `prop:rg-action-score-isometry`: add the sentence
    distinguishing the $L^\infty$ and $L^2$ quotients and naming the quadratic path as the
    $L^2$ realizer.
11. `appendix_notation.tex`: add a row for $\widehat R_\ell:\mathcal Q_\ell\to\mathcal Q_{\ell+1}$
    with its non-identifications; extend the "three uses of pullback" paragraph to record
    the joint-versus-marginal distinction of §4.
12. `counterexample-register.md`: promote `CE-HORIZONTAL-ANOMALY`, `CE-SECTION-DESCENT`,
    `CE-HISTORY-COLLAPSE`, and `CE-DURATION-MISMATCH` from `CANDIDATE` on the strength of
    §§5.3, 6.3, 6.4, and 7, and update the closing paragraph at line 59.
13. Task 14 prerequisite: `main.pdf` at `02d5d8f` predates the Task 5–9 source changes
    (§0.3(2)). No visual or page-level conclusion may be drawn from it until it is rebuilt.

Repairs 1–4 and 9–11 are text-level and consume no new mathematics. Repairs 5–8 import the
constructions and witnesses proved here. Repair 12 is a ledger update. Repair 13 is a
build-order finding, recorded because it invalidates any Task 10 conclusion drawn from the
tracked artifact.

---

## 11. Scope and limitations

**Theorems.** Theorems A, B, C, D, E, F, G, Lemmas 1.1, 1.2, 3.1, 8.1, 8.2, Propositions
3.3, 3.4, 3.7, 6.3, and Corollary 3.6 are proved above from their stated hypotheses.
Lemma 1.2 and Theorem D(2) are applicable theorems used with explicit hypothesis mappings
(the $f$-divergence data-processing inequality; the smooth-descent theorem for surjective
submersions); every other proof is self-contained.

**Constructions.** Construction 3.2 (finite-dimensional tier), the $L^2$ tier of §3.4(b1),
Construction 5.2 (averaging), and Construction 5.3 (variational) are typed objects with
verified nonemptiness and stated regularity. They are *examples* discharging existence;
they are not claimed to be canonical, and no theorem asserts that a declared recognition
family must take one of these forms.

**Counterexamples.** Counterexamples 3.5, 3.8, 5.1, 6.1, 6.2, and 7.1 are exact typed
witnesses with their computations displayed. Each refutes a specific universal reading and
nothing broader. In particular, Counterexample 7.1 does not contradict
`thm:pb-pullback-fisher-defect`; it refutes base-level positivity claimed without the
zero-horizontal-defect hypothesis.

**Declared assumptions carried, not proved.** (H1)–(H5), `H-DQM`, `H-REVERSE`, `H-GAUGE`,
`H-CONFIG`, `H-HISTORY`, and the manuscript's own regular-model hypothesis
`hyp:pb-regular-models` are hypotheses. Nothing here shows that a given belief or model
fiber satisfies them.

**Not established.** The existence of a smooth joint-law lift $\iota_i$ for any declared
recognition family, and nondegeneracy of its Fisher pullback, remain `OPEN`
(`appendix_claim_ledger.tex:50-56`); §4.4(4) shows only that the choice of lift changes the
metric. The oriented semiconjugacy condition for the manuscript's independently recomputed
RG flows remains `OPEN` (`appendix_claim_ledger.tex:147-154`); Theorem F is a statement
about a fine curve and its image, and Proposition 6.3 shows semiconjugacy alone is
insufficient for a nonconstant shared history.

**No modeling or operational bridge is asserted.** Fisher duration $\tau$ is a statistical
arc length on a selected oriented orbit. No identification with physical time, a global
clock, or a synchronized coordinate is made or implied anywhere above; the contract's
exclusion list forbids it and nothing here approaches it. RG depth $\ell$ and the orbit
coordinate $r$ are distinct indices throughout.

**No numerical observation.** No computation was performed and no numerical claim is
recorded, so nothing here is closed by computation. The SHA-256 values in §0.2 and the
git-history findings in §0.3 are mechanical facts about the repository, not mathematical
evidence, and they support only the provenance statements they appear in.

**Analogy.** None is used. The word "pullback" appears in three typed senses in this
program (`appendix_notation.tex:367-375`); §§1–7 use only the first (tensor pullback along
$D^\omega s$ or along $\iota_i$) and never transfer a theorem between senses.
