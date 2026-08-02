# Lens review — differential geometry / SPD manifolds

**Reviewer lens.** Smooth structure and regularity hypotheses; jet bundles and the covariant
vertical first jet; horizontal lifts and horizontal-compatibility; rank / radical / quotient claims
and whether constant rank is assumed where a quotient is taken; integrability (Frobenius);
leaf-space regularity and Hausdorffness; basicness of induced tensors; SPD geometry
(affine-invariant metric, exp/log, congruence/sandwich action); positive-definiteness and
degeneracy; dimension and shape consistency.

**Chapters read in full.** `05c_pullback_geometry.tex`, `06a_generative_gaussian.tex`,
`06_gaussian.tex`. `02_geometry.tex` consulted for definitions; `04_generative.tex:265-321`,
`06_general_coarsegraining.tex:135-180`, `09_coarsegraining.tex:108-171` consulted only to check
cross-chapter consistency of statements made inside my chapters.

**Scope discipline.** Everything on the settled-ground list (R01–R21, FINAL-01–08, LG-1/2, RG-1/2,
PB-1–4) and every manuscript-declared OPEN/CONJECTURE obligation was treated as out of scope. In
particular I do **not** re-raise: connection-relativity of the pullback, non-canonicity of the
connection, constant rank as an obligation, integrability of the radical, leaf-space regularity,
basicness, channel weights, or the $A=0$ singular-pencil facts. What follows is confined to
hypotheses those entries are *conditioned on*, steps *between* them, and notation/typing.

**Scoping note (out of lens, recorded once).** `pullback-geometry-ledger.json` anchors PB-1/PB-3 to
`artifact_revision git:43eb7e74…` with evidence located at `05c_pullback_geometry.tex:20-566` and
`:574-849`. `git ls-tree 43eb7e7 manuscripts/gauge_vfe_rg/` shows `05c_pullback_geometry.tex` did
not exist at that revision (it was added in `0af1cbd`, merged in `9ea9969`). That is a
verification-provenance issue, not a geometry finding; I flag it only because it means PB-1/PB-3
evidence is anchored to a revision that cannot contain the cited lines. I still treated their
*statements* as settled.

---

## Summary

Twelve findings. **None critical, one medium, eleven low.** Every load-bearing geometric identity
in these three chapters that I could recompute is **correct**, including all of the ones I most
expected to break. The chapters are unusually disciplined about exactly the failure modes this lens
hunts: the null distribution is not assumed integrable (and a contact counterexample is supplied
and is correct), the quotient is taken only under an explicitly stated constant-rank hypothesis,
non-Hausdorff leaf spaces are flagged, basicness is stated as an additional requirement in the
correct form, and the difference between passive gauge change and connection change is kept
straight. The single substantive finding is a positive-definiteness gap in the Gaussian chapter:
the interaction subfamily is never shown to intersect the cone $\Sym^{NK}_{++}$ that the
recognition density itself requires, while the prose asserts that "positive definiteness is
proved."

---

## Findings

### G-1 — The interaction family is never shown to meet the recognition family's own $J\succ0$ requirement, and the prose asserts that it is proved

- **Claim.** "Positive definiteness is proved by `prop:gauss-interaction-energy-kernel`."
- **Location.** `06_gaussian.tex:323` (prose); `06_gaussian.tex:307-319`
  (`prop:gauss-interaction-nonempty`, esp. line 308); `06_gaussian.tex:109-120`
  (`prop:gauss-interaction-energy-kernel`); `06_gaussian.tex:13-19` (`eq:gauss-density`).
- **Severity.** medium
- **Status.** `prop:gauss-interaction-energy-kernel` is tagged `\status{ESTABLISHED}` and is
  correct *as stated* — it proves $\Lambda\succeq0$ plus an exact iff-criterion for $\Lambda\succ0$.
  `prop:gauss-interaction-nonempty` is tagged `\status{ESTABLISHED}` and correctly proves only
  *membership* in $\mathcal I(V)$. **The prose at line 323 inflates both.**
- **Evidence.**
  1. `eq:gauss-density` (`06_gaussian.tex:13-19`) declares the recognition family over
     $(h,J)\in\R^n\times\Sym^n_{++}$. A recognition law therefore requires $J\succ0$, not $J\succeq0$.
  2. `prop:gauss-interaction-energy-kernel` proves "$\Lambda\succeq0$ for every admissible choice of
     parameters" and then a *conditional* criterion. It contains no unconditional
     positive-definiteness statement. Line 323's sentence contrasts proved facts against the
     numerical conditioning check, so "positive definiteness" there is read as proved. It is not.
  3. `prop:gauss-interaction-nonempty` hypothesizes "each agent carry a **proper prior** of
     precision $A_i\succeq0$". This is internally contradictory: a Gaussian prior with singular
     precision is improper. The conclusion delivered is only "the associated precision lies in
     $\mathcal I(V)$" — no definiteness.
  4. Recomputation (`numpy`, $N=4$, $K=3$, random PSD $A_i$ and $W_{ij}$): the energy identity
     `eq:gauss-interaction-energy` holds exactly (residual `0.0`) and $\lambda_{\min}(\Lambda)=1.718$
     when $A_i\succ0$. Setting $A_i=0$ (admissible under $A_i\succeq0$) gives
     $\lambda_{\min}(\Lambda)=-9.48\times10^{-16}$ with **nullity 3 = $K$** — the consensus subspace.
     So the constructed "nonemptiness" witness can be exactly singular and is then not a density.
  5. Consequently the chapter nowhere establishes $\mathcal I(V)\cap\Sym^{NK}_{++}\neq\varnothing$,
     which is what `hyp:gauss-global-interaction` (`06_gaussian.tex:296-297`, "acts on recognition
     precisions that belong globally to `eq:gauss-interaction-family`") actually needs.
- **Fix.** Two lines. (a) In `prop:gauss-interaction-nonempty`, replace "a proper prior of precision
  $A_i\succeq0$" by "$A_i\succeq0$, with $\sum_i A_i\succ0$" and add the corollary: since every
  $W_{ij}\succ0$ by construction and the graph is connected, `prop:gauss-interaction-energy-kernel`'s
  criterion gives $\Lambda\succ0$, hence
  $\mathcal I(V)\cap\Sym^{NK}_{++}\neq\varnothing$ (verified: $\lambda_{\min}=1.718$ above).
  (b) At line 323 write "positive **semi**definiteness is proved by
  `prop:gauss-interaction-energy-kernel`; positive definiteness follows from its kernel criterion
  under the nondegeneracy of (a)."
- **Falsifies.** Nothing downstream, if fixed as above. Left unfixed it falsifies the sentence at
  line 323 and leaves `hyp:gauss-global-interaction` acting on a family not proved nonempty inside
  the declared recognition domain.

---

### G-2 — The overbar is overloaded inside `05c`: quotient metric vs. coarse-level semimetric, and one theorem is displayed twice with inconsistent decoration

- **Claim.** `eq:pb-pullback-quotient-metric` introduces $\bar h_s^\omega$ as the *quotient* metric
  on $Q_s^\omega=T\mathcal U/K_s^\omega$; `eq:pb-meta-perceived-geometry` reuses
  $\bar h_{\bar s}^{\bar\omega}$ for the *coarse-level* pullback semimetric on $\bar{\mathcal C}$.
- **Location.** `05c_pullback_geometry.tex:281-283` vs `:724-728`, `:731-734`, `:738-742`; compare
  `:694` where the same coarse object is written **without** the bar, as $h_{\bar s}^{\bar\omega}$.
- **Severity.** low
- **Status.** `thm:pb-pullback-rank-quotient` and `cor:pb-meta-perceived-geometry` both
  `\status{ESTABLISHED}`; both are mathematically correct. This is a notation defect, not a proof
  defect.
- **Evidence.** `eq:pb-pullback-fisher-contraction` (line 694) reads
  $h_s^\omega-f^*h_{\bar s}^{\bar\omega}=(D^\omega s)^*\Delta_F^\Psi\succeq0$;
  `eq:pb-meta-perceived-defect` (line 739-741) reads
  $h_s^\omega-f^*\bar h_{\bar s}^{\bar\omega}=(D^\omega s)^*\Delta_F^\Psi\succeq0$. These are the
  same statement; the corollary's own proof says so ("the third is
  `eq:pb-pullback-fisher-contraction`"). Everywhere else in the chapter the overbar means
  "coarse level" ($\bar E,\bar{\mathcal C},\bar s,\bar\omega,\bar g^F,\bar\tau,\bar{\mathcal T}$),
  so a reader who has internalised `eq:pb-pullback-quotient-metric` will read
  `cor:pb-meta-perceived-geometry` as a statement about the *quotient* geometry — which would be
  false without the constant-rank hypothesis that the corollary does not carry.
- **Fix.** Reserve the overbar for the coarse level throughout. Write the quotient tensors as
  $h^{Q}_s,\;c^{Q}_s$ (or $\check h_s^\omega$) in `thm:pb-pullback-rank-quotient`, and drop
  `cor:pb-meta-perceived-geometry`'s third display or state it as an explicit restatement.
- **Falsifies.** Nothing. Readability and the constant-rank scoping of the quotient claim.

---

### G-3 — $\omega'$ denotes two different things twenty-five lines apart, in the one place where the chapter's whole point is that they differ

- **Claim.** `eq:pb-covariant-jet-gauge-law` writes $D^{\omega'}s'(X)=T\widehat\rho_x(g^{-1})D^\omega
  s(X)$ inside the *passive gauge* theorem, where $\omega'$ is the **same** connection in a re-chosen
  frame. `sec:pb-connection-dependence:140` then declares "Let $\omega'$ be a **second principal
  connection** on $P$."
- **Location.** `05c_pullback_geometry.tex:119-123` vs `:140`; the distinction is asserted at
  `:133-135` ("It does not say that two different connections give the same pullback").
- **Severity.** low
- **Status.** `thm:pb-pullback-gauge-invariance` `\status{ESTABLISHED}` — correct; verified
  numerically below. The defect is that the notation collapses the very distinction the surrounding
  prose is defending.
- **Evidence (recomputation).** I realized the construction on the SPD-associated bundle: $G=\GL(2)$
  in the defining representation acting on centered Gaussians by the congruence (sandwich)
  action $\Sigma\mapsto R\Sigma R^\top$, fiber $=\Sym^2_{++}$, fiber Fisher metric
  $g^F_\Sigma(U,V)=\tfrac12\Tr(\Sigma^{-1}U\Sigma^{-1}V)$ (= one-half the affine-invariant metric),
  base $\mathcal C=\R$, trivial principal bundle, nonconstant section, nonconstant $\mathfrak{gl}(2)$
  local connection $A(x)=A_0+xA_1$, and a **nonconstant** frame change $g(x)$ with
  $A'=\mathrm{Ad}_{g^{-1}}A+g^{-1}dg$ (`eq:geo-local-connection-b`) and
  $\Sigma'=\widehat\rho(g)^{-1}\Sigma=g^{-1}\Sigma g^{-\top}$ (`eq:geo-quotient-convention`):
  - $\|D^{\omega'}s'-T\widehat\rho(g^{-1})D^\omega s\|_\infty = 3.94\times10^{-10}$
    (central-difference limited; scale $\|D^\omega s\|_\infty=14.4$)
  - $|h^{\omega'}_{s'}(\partial_x,\partial_x)-h^\omega_s(\partial_x,\partial_x)|
     = 1.21\times10^{-9}$ against a value of $28.03$ (relative $4\times10^{-11}$)
  So `eq:pb-covariant-jet-gauge-law` and `thm:pb-pullback-gauge-invariance` are **correct**, and the
  sign convention $D_A=d+\widehat\rho_{x*}(A)$ declared at `:153-155` is genuinely compatible with
  `eq:geo-quotient-convention` — I also verified this symbolically:
  $D_{A'}v'=\rho(a)^{-1}D_Av$ under $A'=\mathrm{Ad}_{a^{-1}}A+a^{-1}da$, $v'=\rho(a)^{-1}v$.
- **Fix.** Use $\omega^{[g]}$, or simply $(A',s')$ in the frame-change theorem, and reserve $\omega'$
  for the second connection.
- **Falsifies.** Nothing.

---

### G-4 — $s$ is simultaneously the section and the continuous RG scale in `eq:pb-metric-beta-reference`

- **Claim.** "On a differentiable reference-space curve $s\mapsto\widetilde h_s$, its continuous
  counterpart is $\beta_h(s)=\partial_s\widetilde h_s$."
- **Location.** `05c_pullback_geometry.tex:771-774`.
- **Severity.** low
- **Status.** `\status{DEFINITION}` — the typing content is correct (see evidence).
- **Evidence.** Throughout the chapter $s$ is the section and the subscript in $h_s^\omega$,
  $c_s^\omega$, $\bar h_s^\omega$, $h_{s,\mathscr D}^\omega$ means "pulled back along the section
  $s$". So "$\widetilde h_s$" reads as "the transported pullback of the section $s$", not "the
  reference-space tensor at scale $s$". Separately, the typing of
  $\widetilde h_\ell=(i_\ell^{-1})^*h_\ell$ is **correct**: $i_\ell:\mathcal C_\ell\to\mathcal
  C_\star$ is a diffeomorphism, so $(i_\ell^{-1})^*$ carries a covariant tensor from $\mathcal
  C_\ell$ to $\mathcal C_\star$, and the difference in `eq:pb-metric-beta-reference` is then a
  well-typed symmetric 2-tensor on $\mathcal C_\star$.
- **Fix.** Use $\tau$ or $\sigma$ for the continuous scale.
- **Falsifies.** Nothing.

---

### G-5 — `sec:pb-two-channels` uses $h^{\omega_b}_{i,b}$, $q_i$, $s_i$ without their defining equations in-chapter

- **Claim.** `eq:pb-two-channel-pair` displays $(h_{i,b}^{\omega_b},h_{i,m}^{\omega_m})$ and
  `eq:pb-product-radical` displays $\ker D^{\omega_b}q_i\cap\ker D^{\omega_m}s_i$.
- **Location.** `05c_pullback_geometry.tex:208-214` and `:230-249`.
- **Severity.** low
- **Status.** `prop:pb-product-radical` `\status{ESTABLISHED}` — correct.
- **Evidence.** $q_i$ and $s_i$ are the belief and model sections of `def:geo-agent`
  (`02_geometry.tex:375-388`) and are never reintroduced in `05c`. The identification
  $h_{i,b}^{\omega_b}=(D^{\omega_b}q_i)^*g_b^F$ is required to read `eq:pb-product-radical` but is
  never displayed; the reader must reconstruct it from the proof at `:242-246`. The proposition
  itself is correct: both summands are PSD with positive weights, so the null cone of the sum is the
  intersection of the null cones, and for a PSD form the null cone equals the radical
  (Cauchy–Schwarz — the proof says "polarization", which is the right conclusion by the wrong
  lemma name).
- **Fix.** One display: $h_{i,b}^{\omega_b}:=(D^{\omega_b}q_i)^*g_b^F$,
  $h_{i,m}^{\omega_m}:=(D^{\omega_m}s_i)^*g_m^F$ at line 208; and replace "polarization" by
  "Cauchy–Schwarz for a positive semidefinite form" at line 249.
- **Falsifies.** Nothing.

---

### G-6 — "a partition mixing the two sectors is admissible wherever a partition is required" is a shape error for `def:gauss-interaction-family` when $K\neq d_m$

- **Claim.** `06_gaussian.tex:8`.
- **Location.** `06_gaussian.tex:8` vs `def:gauss-interaction-family` at `:98-105`.
- **Severity.** low
- **Status.** untagged chapter preamble; `def:gauss-interaction-family` is `\status{DEFINITION}`.
- **Evidence.** `def:gauss-interaction-family` reads "Let $\Lambda\in\Sym^{NK}$ be partitioned into
  $K\times K$ blocks indexed by agents" and requires $W_{ij}=W_{ji}\in\PSD^K$. If a block $b$ is a
  belief block ($\dim K$) and block $c$ a model block ($\dim d_m$), then $\Lambda_{bc}\in\R^{K\times
  d_m}$, $W_{bc}\in\R^{K\times d_m}$ and $W_{cb}\in\R^{d_m\times K}$, so the requirement
  $W_{bc}=W_{cb}$ is a type error unless $K=d_m$. The blanket "wherever a partition is required"
  therefore over-reaches; it is correct only for the free block partition $\mathfrak B$ of
  `sec:gauss-conditional-reading` (`:54`), where block dimensions $n_b$ are unconstrained and where
  `prop:gauss-conditional-precision` and `eq:gauss-marginal-block` are indeed dimension-agnostic
  (both verified: residuals $2.2\times10^{-16}$ and $2.8\times10^{-17}$ on a random $n=6$ split).
- **Fix.** Restrict the sentence: "a partition mixing the two sectors is admissible wherever a free
  block partition is required (`sec:gauss-conditional-reading`); the interaction family of
  `def:gauss-interaction-family` requires uniform block dimension and therefore $K=d_m$ for a mixed
  partition."
- **Falsifies.** Nothing, once scoped.

---

### G-7 — "the Fisher information of the family in the natural parameter $h$ is exactly $C=J^{-1}$" drops the qualifier its own proposition carries

- **Claim.** `06_gaussian.tex:49`.
- **Location.** `06_gaussian.tex:49`; compare `prop:gauss-log-normalizer-moments` at `:38`
  ("the Hessian of $\mathsf A$ in $h$ **at fixed $J$** is $C$").
- **Severity.** low
- **Status.** `prop:gauss-log-normalizer-moments` `\status{ESTABLISHED}` — correct and correctly
  qualified. The interpretive sentence at line 49 is the one that drops the qualifier, and that
  sentence is load-bearing ("The precision is therefore simultaneously a coupling matrix and a
  metric, and the renormalization chapters use both readings").
- **Evidence (recomputation).** For the $(h,J)$ family the Fisher matrix is $\nabla^2\mathsf A$ in
  the natural coordinates $(h,\Theta=-\tfrac12 J)$. Its $h$–$J$ cross block is
  $\partial_J(J^{-1}h)[\delta J]=-J^{-1}\delta J\,\mu$, which is nonzero whenever $\mu\neq0$.
  Central-difference check at $n=3$, random $J\succ0$, random symmetric $\delta J$:
  cross block $=0.1319$, matching $-J^{-1}\delta J\mu$ to $9.3\times10^{-7}$; at $h=0$ the cross
  block is exactly $0$. So $C=J^{-1}$ is the $hh$-*block*, not the family's Fisher information for
  $h$ after profiling $J$ (the profile information is $C-I_{hJ}I_{JJ}^{-1}I_{Jh}\prec C$ for $\mu\neq
  0$). I separately confirmed the proposition's own content: $d\mathsf A/dh-\mu$ residual
  $1.2\times10^{-10}$, and $d\mathsf A/dJ$ against $-\tfrac12\Tr[(C+\mu\mu^\top)dJ]$ residual
  $2.8\times10^{-10}$; Monte-Carlo mean/covariance agree to $6\times10^{-4}$ over $4\times10^5$ draws.
- **Fix.** Insert "at fixed $J$" into the first clause of line 49, matching the second clause.
- **Falsifies.** Nothing that I can find in these chapters; it would falsify any downstream use of
  "$C$ is the Fisher information for $h$" in a setting where $J$ is also being estimated.

---

### G-8 — $G$ carries four meanings in `06_gaussian`; $h$ carries two in `06a`

- **Claim.** Symbol reuse.
- **Location.**
  - `06_gaussian.tex:145` — "$G=(V,E)$ a connected **graph**" (`prop:gauss-coboundary-trivialization`);
  - `06_gaussian.tex:185` — "$G_i\in\R^{K\times K}$", the receiving **gain**;
  - `06_gaussian.tex:130` — "Congruence by $G=\operatorname{diag}(I_2,S)$", a **congruence matrix**;
  - and $G$ is the principal **structure group** in `02_geometry.tex` / `06a` throughout.
  - `06a_generative_gaussian.tex:35` — $h_{a,i}^x$, the **frame rechoice** (inherited from
    `04_generative.tex:291`); `06a_generative_gaussian.tex:159-160` — $h_i=U_i^b(U_i^m)^{-1}$, the
    **relative principal-frame field** (inherited from `02_geometry.tex:58-63`). Both are $G$-valued
    and agent-indexed, in one chapter.
- **Severity.** low
- **Status.** All affected statements are correct; this is notation only.
- **Evidence.** Direct reading. `prop:gauss-coboundary-trivialization` is correct as stated and its
  proof is correct under the transport reading of "the ordered product of graph links along the tree
  path from $r$ to $i$" (i.e. $U_i=\Theta_{i\,i_{k-1}}\cdots\Theta_{i_1 r}$, leftmost factor = last
  leg), which is the reading forced by $\Theta_{ij}$ transporting $j\to i$ everywhere else in the
  manuscript. Under the opposite (left-to-right) reading the construction yields $U_iU_j^{-1}=
  \Theta_{ji}$. That is an expository ambiguity, not an error, and I do not raise it separately.
- **Fix.** Rename the graph to $\mathfrak G$ (or reuse $\mathfrak I$ from
  `def:geo-graph-links`), the congruence matrix at line 130 to $S_\ast$ or $M$, and the relative
  frame field in `06a` to $r_i$.
- **Falsifies.** Nothing.

---

### G-9 — $\rho_b(\Theta_{ij}^b)\in\GL^+(K)$ is asserted without a hypothesis that makes $\rho_b$ orientation-preserving

- **Claim.** "write $\Theta_{ij}:=\rho_b(\Theta_{ij}^b)\in\GL^{+}(K)$ for the represented graph link".
- **Location.** `06_gaussian.tex:138-139`; the $\GL^+$ decoration recurs in
  `prop:gauss-coboundary-trivialization` (`:145`) and `prop:gauss-global-condition-witnesses`
  (`:224`).
- **Severity.** low
- **Status.** `prop:gauss-coboundary-trivialization` `\status{ESTABLISHED}` — its proof works in any
  group, so nothing depends on the decoration.
- **Evidence.** `02_geometry.tex:81-86` declares only $\rho_b:G\to\operatorname{Aut}(\mathsf K)$,
  with "the representations need not be equivalent, faithful, or of equal dimension" and no
  orientation or connectedness condition on $G$. Hence $\rho_b(g)\in\GL(K)$ is what is licensed;
  $\det\rho_b(g)>0$ requires $G$ connected (or an explicit declaration). The frames $U_i$ built in
  the proof are ordered products of the $\Theta_{ij}$, so they inherit whichever group the links
  live in; the argument is group-agnostic.
- **Fix.** Either write $\GL(K)$ throughout, or add "$G$ is connected, so $\rho_b(G)\subseteq
  \GL^+(K)$" as a one-clause hypothesis at line 138.
- **Falsifies.** Nothing.

---

### G-10 — No non-vacuity witness for the joint hypotheses of the Fisher-defect theorem

- **Claim.** `thm:pb-pullback-fisher-defect` assumes simultaneously: the descent relation
  `eq:pb-coarse-related-sections`, horizontal compatibility $\mathcal D\Psi=0$ along $s$, and that
  the fiber map is the pushforward of a parameter-independent Markov kernel that is equivariant
  under the represented actions.
- **Location.** `05c_pullback_geometry.tex:675-700`, `:722-749`.
- **Severity.** low
- **Status.** `\status{ESTABLISHED}` — the theorem is correct (verified below). The gap is
  presentational: the chapter supplies explicit counterexamples for every *negative* claim
  (`prop:pb-contact-null-counterexample`, the rank-jump example, the
  connection-dependence example) and no positive witness for its main coarse-graining theorem, so a
  reader cannot check that the three hypotheses are jointly satisfiable nontrivially.
- **Evidence.** The theorem's mathematics is right. The score-projection step is exactly
  `thm:cg-fisher-contraction` (`06_general_coarsegraining.tex:138-158`), which is proved
  independently — I checked there is no circularity: `06_general_coarsegraining.tex:169-180` cites
  `thm:pb-pullback-fisher-defect` only as an application, not as an ingredient. The naturality step
  `eq:pb-covariant-tensor-naturality` is a direct consequence of
  `eq:pb-covariant-jet-chain-rule`, whose derivation I reproduced: differentiating
  $\Psi\circ s=\bar s\circ f$ and splitting $TsX=H^\omega_sX+D^\omega sX$, the vertical parts give
  $(\mathcal D\Psi)(X)+T^V\Psi(D^\omega sX)=D^{\bar\omega}\bar s(TfX)$; the defect is vertical
  because $\bar\varpi\circ\Psi=f\circ\varpi$ forces both terms to project to $T_cfX$.
  A witness exists and is cheap: take $\bar{\mathcal C}=\mathcal C$, $f=\mathrm{id}$,
  $\bar\omega=\omega$, and let the fiber map be pushforward along a linear intertwiner
  $P:\mathsf K\to\bar{\mathsf K}$ with $P\rho_b(g)=\bar\rho_b(g)P$ for all $g$. Then the fiber map
  is a deterministic parameter-independent Markov kernel, it is equivariant, and $\Psi$ carries
  $\omega$-horizontal curves to $\omega$-horizontal curves, so $\mathcal D\Psi\equiv0$.
- **Fix.** Add that three-line example after `thm:pb-pullback-fisher-defect`.
- **Falsifies.** Nothing.

---

### G-11 — "Let $s:\mathcal U\to E$ satisfy `hyp:pb-regular-models`" is a category error

- **Claim.** `thm:pb-pullback-rank-quotient`, opening clause.
- **Location.** `05c_pullback_geometry.tex:263-264`.
- **Severity.** low
- **Status.** `\status{ESTABLISHED}` — the theorem is correct.
- **Evidence.** `hyp:pb-regular-models` (`:25-37`) constrains the *models* $\mathcal B_x$ (smooth
  parametrized-measure model, DQM, positive-definite Fisher form, third-power integrability,
  domination, represented action induced by a parameter-independent bimeasurable sample-coordinate
  change). A section cannot satisfy it. What the proof actually needs from $s$ is smoothness, which
  comes from the standing declaration at `eq:pb-covariant-first-jet` ("For a smooth section $s$"),
  plus positive definiteness of $g^F$, which is what `hyp:pb-regular-models` supplies. The
  radical/rank identity itself is correct and pointwise: $D^\omega sX=0\Rightarrow h_s^\omega(X,\cdot)
  =0$, and conversely $h_s^\omega(X,X)=g^F(D^\omega sX,D^\omega sX)=0$ with $g^F\succ0$ forces
  $D^\omega sX=0$.
- **Fix.** "Assume `hyp:pb-regular-models` and let $s:\mathcal U\to E$ be a smooth section."
- **Falsifies.** Nothing.

---

### G-12 — "The constant-rank theorem" is the wrong name for the lemma actually used, and no reference is given

- **Claim.** "The constant-rank theorem makes the kernel and image smooth subbundles."
- **Location.** `05c_pullback_geometry.tex:300`.
- **Severity.** low
- **Status.** `\status{ESTABLISHED}` — the *content* is correct; the *name* is not.
- **Evidence.** The constant-rank theorem (Lee, *Introduction to Smooth Manifolds*, 2nd ed., Thm.
  4.12) is a local normal-form theorem for a smooth **map of manifolds** whose differential has
  locally constant rank. What is needed here is the different statement about a smooth
  **vector-bundle homomorphism** $\Phi:T\mathcal U\to s^*VE$ of locally constant rank: its kernel
  and image are smooth subbundles. $D^\omega s=\operatorname{ver}^\omega\circ Ts$ is fiberwise linear
  in $X$ and smooth, and $s^*VE\to\mathcal U$ is a smooth vector bundle because $VE=\ker T\varpi$ is
  a subbundle of $TE$ over $E$ of rank $\dim\mathcal B$, so the bundle-homomorphism lemma applies
  directly. The manuscript's downstream statements are correct: constant rank is also genuinely
  *necessary*, since a subbundle has locally constant rank by definition, and the manuscript's own
  witness ($s(x)=\mathcal N(x^2,1)$, zero connection, $h_s=4x^2dx^2$, `:364-366`) is correct —
  $D^\omega s=2x\,dx\otimes\partial_\mu$, $g^F=1$, so $\ker D^\omega s$ has rank 1 at the origin and
  rank 0 elsewhere and is not a subbundle.
- **Fix.** "A constant-rank smooth bundle homomorphism has smooth kernel and image subbundles",
  with a citation.
- **Falsifies.** Nothing.

---

## Examined adversarially and **cleared** (no finding)

Recorded so the next pass does not redo the work. All residuals from
`C:/Python314/python.exe` (numpy/sympy/scipy).

**`05c` — covariant first jet and gauge invariance.**
- `prop:pb-statistical-tensor-descent` is correct. The pushforward map $f\mapsto f\circ r_g^{-1}$ is
  a genuine $L^2$ isometry ($\int|f\circ r_g^{-1}|^2\,d(r_g)_\#p=\int|f|^2dp$); for a
  parameter-independent $r_g$ the pushed model's density against the pushed reference is
  $p_\theta\circ r_g^{-1}$, so the score is $\ell_u\circ r_g^{-1}$, and both the second and third
  score moments are preserved. Descent through the associated-bundle quotient is legitimate: the
  $G$-action on $P\times\mathcal B$ is free and proper (freeness inherited from $P$), and
  $T_\beta\mathcal B\to V_{[u,\beta]}\mathcal E$ is an isomorphism because an orbit direction
  $(\xi_P(u),-\widehat\rho_*(\xi)\beta)$ lies in $\{0\}\times T_\beta\mathcal B$ only for $\xi=0$.
  **Concrete SPD check:** for the Gaussian family the congruence action $\mu\mapsto R\mu$,
  $\Sigma\mapsto R\Sigma R^\top$ is an exact Fisher isometry — residual $8.2\times10^{-16}$
  (relative $9.5\times10^{-15}$) on the full metric
  $\delta\mu_1^\top\Sigma^{-1}\delta\mu_2+\tfrac12\Tr(\Sigma^{-1}\delta\Sigma_1\Sigma^{-1}
  \delta\Sigma_2)$ at $K=4$ with random invertible $R$. The Amari–Chentsov tensor is likewise
  congruence-invariant (Monte-Carlo, $4\times10^6$ draws, agreement to $1.1\%$ — MC-noise limited).
  This is the affine-invariance of the SPD metric
  $\langle U,V\rangle_\Sigma=\Tr(\Sigma^{-1}U\Sigma^{-1}V)$ under $\Sigma\mapsto A\Sigma A^\top$,
  $A\in\GL(n)$ (Pennec–Fillard–Ayache, *A Riemannian Framework for Tensor Computing*, IJCV 66(1),
  2006; the Gaussian covariance Fisher block is one-half that metric).
- The sign convention $D_A=d+\widehat\rho_{x*}(A)$ is genuinely compatible with
  `eq:geo-quotient-convention` and `eq:geo-local-connection-b` — verified symbolically and
  numerically (G-3 above).
- `prop:pb-pullback-connection-change`: jet residual $3.6\times10^{-15}$; Fisher residual
  $7.1\times10^{-15}$ on the SPD bundle. The $2^3$-term count for the Amari polarization is right.
- The connection-dependence example (`eq:pb-connection-dependence-example`) is correct:
  translation bundle, $\mathcal B=\{\mathcal N(\mu,1)\}$, constant section, $A'=a_0dx$ gives
  $D^{A'}s=a_0dx\otimes\partial_\mu$ and $h^{A'}=a_0^2dx^2$.
- `eq:pb-transported-section-velocity` is correct: I integrated the horizontal lift on the SPD bundle
  ($\dot M=-A(\dot\gamma)M$, $\Omega(\Sigma_0)=M\Sigma_0M^\top$) and finite-differenced
  $\Omega^{-1}s(\gamma(\epsilon))$; residual $8.2\times10^{-7}$ against $\|D^\omega s\|=14.4$
  (relative $6\times10^{-8}$, FD-limited).

**`05c` — rank, radical, quotient, integrability, basicness.**
- `thm:pb-pullback-rank-quotient` is correct, and constant rank *is* assumed where the quotient is
  taken. Well-definedness of $\bar c_s^\omega$ is correct because $D^\omega s(X+Z)=D^\omega s(X)$ for
  $Z\in K_s^\omega$.
- `prop:pb-contact-null-counterexample` is correct. Recomputed:
  $\alpha=dz-x\,dy$, $D^\omega s=\alpha\otimes\partial_\mu$, $h_s^\omega=\alpha^2$ of constant rank 1,
  and the coefficient of $dx\wedge dy\wedge dz$ in $\alpha\wedge d\alpha$ is exactly $-1$
  (symbolic), matching $-dz\wedge dx\wedge dy$. Since $\ker\alpha$ has corank 1 and $\alpha$ is
  nowhere zero, the Frobenius criterion applies verbatim.
- The basicness condition `eq:pb-null-basicness` is stated in the **correct** form. For forms the
  standard definition of basic is $\iota_X\alpha=\iota_Xd\alpha=0$ for $X\in\Gamma(T\mathcal F)$,
  which by Cartan's formula is equivalent to $\iota_X\alpha=0$ and $\mathcal L_X\alpha=0$; for a
  symmetric 2- or 3-tensor Cartan's formula is unavailable, so $\mathcal L_Zh=0$ is the right
  condition, and the manuscript's remark that it does **not** follow from $\iota_Zh=0$ is correct
  ($h=\alpha\otimes\alpha$ with $\iota_Z\alpha=0$ has $\mathcal L_Zh=(\iota_Zd\alpha)\otimes\alpha+
  \alpha\otimes(\iota_Zd\alpha)$, generally nonzero).
- "Even an involutive distribution can have a non-Hausdorff leaf space" is correct and standard.
- The claim that the $\epsilon^3$ coefficient of `eq:pb-transported-divergence-expansion` is not
  determined by $c_{s,\mathscr D}^\omega$ alone is correct: expanding
  $\mathscr D(\theta,\theta+\delta)$ with $\delta=\epsilon v+\tfrac{\epsilon^2}{2}w$ gives
  $\tfrac12g(v,w)+\tfrac16C(v,v,v)$ with $C=\partial'_i\partial'_j\partial'_k\mathscr D|_{\rm diag}$,
  a **one-sided** third jet ($=-\E[\partial_i\partial_j\partial_k\ell]$ for KL), not
  $\Gamma-\Gamma^*$.

**`05c` — divergence jets.** `prop:pb-kl-divergence-jets` verified **symbolically to exact zero** on
a genuinely curved chart (the normal model $\mathcal N(t_1,e^{t_2})$, whose score Hessian does not
vanish):
- $-\partial_i\partial'_j\KL-\E[\ell_i\ell_j]=0$ (all four entries);
- $(\Gamma_{\mathscr D}-\Gamma^*_{\mathscr D})_{ijk}-\E[\ell_i\ell_j\ell_k]=0$ (all eight entries);
- $\partial'_i\partial'_j\KL-g_{ij}=0$, which is what `cor:pb-transported-divergence-quadratic`
  silently needs and which does hold for any contrast (differentiate $\partial'_i\mathscr
  D(\theta,\theta)=0$ in $\theta_j$).
The identification $\Gamma_{\mathscr D}=\Gamma^{(-1)}$ (m-connection), $\Gamma^*_{\mathscr
D}=\Gamma^{(1)}$ (e-connection), $\Gamma^{(-1)}-\Gamma^{(1)}=T$ matches Amari–Nagaoka's
$\Gamma^{(\alpha)}=\Gamma^{(0)}-\tfrac\alpha2 T$; the sign convention claim at `:407-410` is correct.

**`05c` — coarse naturality and the defect cocycle.** `thm:pb-covariant-jet-naturality`,
`cor:pb-coarse-null-map`, `thm:pb-pullback-fisher-defect`, `thm:pb-fisher-defect-cocycle` and the
Amari-defect remark are all correct (derivations reproduced; see G-10). The descent obligation at
`:590-593` is if anything over-cautious: for a surjective smooth submersion $f$, a smooth map
constant on the fibers descends *smoothly* automatically (Lee, ISM 2nd ed., Thm. 4.30), so only
fiberwise constancy is a real obligation. `eq:pb-metric-beta-reference`'s typing is correct.
The chapter's `\status{NOT-CLAIMED}` and `\status{OPEN}` registers at `:552-557`, `:566-570`,
`:826-842` are honest and I found nothing they under-declare.

**Cleared candidate I raised against myself and dropped.** I suspected that requiring the *coarse*
experiment to be "regular" in the sense of `hyp:pb-regular-models` (positive-definite Fisher form,
`:675-679`) silently excludes the interesting coarse-grainings — those that annihilate a direction.
It does not: total information loss along $u$ means the coarse score $\bar\ell_u$ vanishes, i.e.
$T^V\Psi(u)=0$, which is compatible with $\bar g^F\succ0$ on $\bar{\mathcal B}$ because $\Psi$'s
fiber map is not required to be an immersion. No finding.

**`06_gaussian` — everything recomputed.**
- `prop:gauss-log-normalizer-moments`: see G-7 evidence. Convexity transfer via the affine map
  $J\mapsto-\tfrac12J$ is correct.
- `prop:gauss-conditional-precision`, `eq:gauss-precision-not-covariance`, `eq:gauss-marginal-block`:
  residuals $2.2\times10^{-16}$, $1.1\times10^{-16}$, $2.8\times10^{-17}$. The claim "the two
  coincide exactly when $J_{b,-b}=0$" is correct because $J_{-b,-b}\succ0$ forces
  $MJ_{-b,-b}^{-1}M^\top=0\Rightarrow M=0$.
- `prop:gauss-interaction-energy-kernel`: energy identity exact (`0.0`); the $\sum_iA_i\succ0$
  necessary condition is correct (if $(\sum A_i)v=0$ with $A_i\succeq0$ then $A_iv=0$ for all $i$,
  so $\mathbf1\otimes v\in\ker\Lambda$).
- `prop:gauss-interaction-family-thin`: codimension bound $\binom N2\tfrac{K(K-1)}2$ is correct and
  **tight** at $N=K=2$ — I computed $\dim\operatorname{span}\mathcal I(V)=9$ in
  $\dim\Sym^4=10$, codimension exactly $1$. The congruence witness at `:130` is exact:
  $G^\top\Lambda G$ with $G=\operatorname{diag}(I_2,S)$, $S=\left(\begin{smallmatrix}1&1\\0&1
  \end{smallmatrix}\right)$ sends the $(1,2)$ block $-I_2\mapsto-S$, not symmetric.
- `prop:gauss-coboundary-trivialization`, `hyp:gauss-flat-comparison` including the
  $W_{ij}^{1/2}(I-\widehat\Theta_{ij})=0$ annihilation criterion (correct: $M^\top WM=0\iff
  W^{1/2}M=0$), and the congruence/inertia remark at `:175` (with $\Lambda\succ0$ the pencil
  $(L,\Lambda)$ is regular and its generalized spectrum is congruence-invariant): all correct.
- `prop:gauss-assembled-precision-blocks`, `prop:gauss-global-condition-witnesses`
  ($-\Lambda_iT_i=\left(\begin{smallmatrix}1&-2\\3&-1\end{smallmatrix}\right)$, asymmetry Frobenius
  norm $7.0711=5\sqrt2$, $\det\Lambda_i=5$, $\det T_i=1$), `prop:gauss-global-interaction-condition`
  (formula residual $4.4\times10^{-16}$ on a random $N=5$, $K=2$ tree), the cancellation witness
  `eq:gauss-global-cancellation-witness` ($\det=1$, eigenvalues $0.610,1.640$), `eq:gauss-trivialized-transition`
  (I re-derived that `eq:gauss-directed-blocks` does hold verbatim with $(\widetilde\Lambda_i,
  \widetilde T_i)$), `prop:gauss-edge-local-characterization` and `cor:gauss-invertible-gain-factor`:
  all correct. The projection characterization was independently replicated at $K=3$ over $4000$
  trials (2000 constructed $\Lambda$-orthogonal projections of ranks $0$–$3$, 2000 generic gains):
  **0 mismatches** between the three-inequality membership test and "$X=\Lambda^{-1/2}\Lambda
  T\Lambda^{-1/2}$ is an orthogonal projection".
- `sec:gauss-open`'s forward summary of `thm:cg-congruence-diagonal-kron` is **accurate**, which I
  did not assume. Recomputed at $N=4$, $K=2$, $H=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}
  \right)$, eliminating one node block: every reduced off-diagonal block is exactly symmetric
  (residual `0.0`), and $H^{-1}A_iH^{-\top}$, $H^{-1}W_{ij}H^{-\top}$ are exactly diagonal with
  nonnegative entries (off-diagonal residual `0.0`, min diagonals $0.31$–$0.82$). The
  non-commutation witness is exact: $XY-YX=\left(\begin{smallmatrix}0&-5\\5&0\end{smallmatrix}
  \right)$.

**`06a` — everything recomputed.**
- `prop:gen-lg-normalization` and `eq:gen-lg-induced-law-map` correct; the output covariance
  $\Sigma^b_{r,0}+B_rC_mB_r^\top$ is automatically SPD because $\Sigma^b_{r,0}\succ0$, so
  $\widetilde\phi_r$ lands in the nondegenerate belief fiber. Shapes in
  `eq:gen-lg-model`–`eq:gen-lg-shapes-obs` are all consistent.
- The gauge laws are **correct including the direction**, which I checked explicitly because the
  carried-over candidate finding #3 concerns exactly this. With `06a:172-175`'s convention
  $u^{x\prime}_i=u^x_i\cdot(g^x_i)^{-1}$, i.e. $a_i=(g^b_i)^{-1}$, $b_i=(g^m_i)^{-1}$,
  `eq:geo-tildephi-gauge-law` becomes $\widetilde\phi'_i=\widehat\rho_b(g^b)\circ\widetilde\phi_i
  \circ\widehat\rho_m(g^m)^{-1}$. Applying `eq:gen-gauge-bridge-offsets`,
  `eq:gen-gauge-covariances` and `eq:gen-gauge-root-model/state` to
  `eq:gen-lg-induced-law-map` gives mean $R^b(B_r\mu_m+\eta)$ and covariance
  $R^b(\Sigma^b+B_rC_mB_r^\top)(R^b)^\top$ — exactly that law. The sentence at `06a:176-177` is
  right. `eq:gen-gauge-mean-identity` follows from `eq:gen-gauge-links`
  (`04_generative.tex:293-297`, $\Theta^{b\prime}_{ij}=h^b_i\Theta^b_{ij}(h^b_j)^{-1}$), and
  `eq:gen-gauge-observation-identity` is immediate. `eq:gen-relative-principal-frame` is consistent
  with `eq:geo-frame-field`: $u^b_ih_i=\sigma_0(U^b_i)^{-1}U^b_i(U^m_i)^{-1}=\sigma_0(U^m_i)^{-1}
  =u^m_i$.
- `06a:279-281` on real logarithms is correct: $\operatorname{diag}(-1,-2)$ has $\det=2>0$ so it is
  in $\GL^+(2)$, and `scipy.linalg.logm` returns a matrix with imaginary part $\pi$ — no real
  logarithm, matching Culver's criterion (each Jordan block of a negative eigenvalue must occur an
  even number of times; here each occurs once).
- `06a`'s honesty about $\widetilde\phi_r$ being a *candidate local realization* rather than an
  equivariant fiber map is correct and important: a fixed $(B_r,\eta,\Sigma^b_{r,0})$ is
  equivariant in the sense of `prop:geo-intertwining-cross-map` only if $\rho_b(g)B_r=B_r\rho_m(g)$,
  $\rho_b(g)\eta=\eta$ and $\rho_b(g)\Sigma^b_{r,0}\rho_b(g)^\top=\Sigma^b_{r,0}$ for all $g$. The
  chapter claims only the local gauge law, which is what it verifies.

---

## Primary sources used

- J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer GTM 218, 2012 — Thm. 4.12
  (constant-rank theorem, the statement `05c:300` misnames), Thm. 4.30 (passing smoothly to the
  quotient along a surjective submersion, relevant to `05c:590-593`), Ch. 10 (vector bundles and
  bundle homomorphisms). <https://www.math.colostate.edu/~renzo/teaching/DiffGeo2011/Introduction%20to%20Smooth%20Manifolds%20-%20J.%20Lee.pdf>
- M. Nakahara, *Geometry, Topology and Physics*, 2nd ed., 2003, §10 — principal connections,
  horizontal lifts, associated-bundle parallel transport; the manuscript already cites this
  correctly at `02_geometry.tex:321`.
- P. Molino, *Riemannian Foliations*, Birkhäuser 1988; and the standard basic-form definition
  $\iota_X\alpha=\iota_Xd\alpha=0$ for $X\in\Gamma(T\mathcal F)$ as restated in
  *Modified differentials and basic cohomology for Riemannian foliations*, arXiv:1007.2955 —
  confirms `eq:pb-null-basicness` is the correct generalization to symmetric tensors.
  <https://ar5iv.labs.arxiv.org/html/1007.2955>
- X. Pennec, P. Fillard, N. Ayache, *A Riemannian Framework for Tensor Computing*, IJCV 66(1):41–66,
  2006 — the affine-invariant metric on $\Sym^n_{++}$ and its invariance under the congruence
  action $\Sigma\mapsto A\Sigma A^\top$, $A\in\GL(n)$; the numerical isometry check above realizes
  the manuscript's `prop:pb-statistical-tensor-descent` in exactly this geometry.
  <https://www.cis.upenn.edu/~cis6100/Pennec.IJCV05.pdf>
- Y. Thanwerdas, X. Pennec, *Is affine invariance well defined on SPD matrices? A principled
  continuum of metrics*, arXiv:1906.01349 — affine-invariance is defined precisely by invariance
  under $\eta:(A,\Sigma)\mapsto A\Sigma A^\top$, $A\in\GL(n)$; the general invariant form is
  $g_\Sigma(V,W)=\alpha\Tr(\Sigma^{-1}V\Sigma^{-1}W)+\beta\Tr(\Sigma^{-1}V)\Tr(\Sigma^{-1}W)$.
  <https://arxiv.org/pdf/1906.01349>
- S.-i. Amari, H. Nagaoka, *Methods of Information Geometry*, AMS/OUP 2000, §3.2 and §3.4 —
  $\alpha$-connections and $\Gamma^{(\alpha)}=\Gamma^{(0)}-\tfrac\alpha2T$, confirming the sign
  convention in `eq:pb-divergence-amari-jet`; already cited by the manuscript.
- W. J. Culver, *On the existence and uniqueness of the real logarithm of a matrix*, Proc. AMS 17
  (1966) 1146–1151 — already cited at `06a:281` and correctly applied.
- R. Bhatia, *Positive Definite Matrices*, Princeton 2007, Ch. 4 and 6 — congruence, Schur
  complements, and the geometry of the SPD cone underlying `prop:gauss-edge-local-characterization`
  and the congruence-diagonal cone.

## Reproduction

Scripts: `<scratchpad>/chk1.py` … `chk6.py`, run with `C:/Python314/python.exe`
(numpy 2.x, sympy, scipy). Seeds fixed (7, 3, —, 11, 21, 5). No CUDA involved.
