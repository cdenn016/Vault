# Deep review — gauge-theory lens

**Reviewer lens:** principal/associated bundles, right action and quotient convention, representations
`rho_b`/`rho_m` and their hatted pushforward versions, local trivializations and passive reframing,
relative frames, connections, parallel transport, holonomy, cocycle conditions, equivariance,
curvature, gauge-covariance of the defect operators.

**Chapters read in full:** `02_geometry.tex`, `04_generative.tex`, `appendix_notation.tex`.
**Consulted for cross-checks only:** `03_probability.tex` (reference measures, §3.2–3.3),
`06a_generative_gaussian.tex` (the realization that fixes the `R` convention), `06_gaussian.tex`
(structure group actually used), `07b_agent_network_rg.tex` (`\mathcal R_b` adjudication).

**Method.** Every load-bearing identity in these two chapters was re-derived from the declared
conventions (`eq:geo-quotient-convention`, `eq:geo-local-reframing`) rather than read off the page,
and the composition-direction-sensitive ones were additionally checked numerically on random
`GL(2,R)` elements (script: scratchpad `gauge_check.py`; results inline below).

---

## 0. What I verified as CORRECT (no finding; recorded so it is not re-litigated)

Every one of the following was re-derived independently and matched the manuscript, including all
inverse placements and product orders. This is the bulk of Chapter 2 and it is sound.

| Claim | Location | My recomputation |
|---|---|---|
| Quotient convention is Kobayashi–Nomizu / Nakahara standard | `eq:geo-quotient-convention` | `(ug,β)~(u,gβ)` ⇔ KN `(u,β)~(ug,ρ(g)^{-1}β)`. Matches. |
| Passive coordinate law `β' = ρ̂(a_i)^{-1} β` | 02:156–158 | `e=[u_i a_i, β'] = [u_i, ρ̂(a_i)β']` ⇒ `β = ρ̂(a_i)β'`. ✓ |
| Relative-frame law `h_i' = a_i^{-1} h_i b_i` | `eq:geo-relative-frame-law` | `u_i^m b_i = u_i^b a_i h_i'` ⇒ `h_i b_i = a_i h_i'`. ✓ |
| Gauge-function conjugation `k_i^m = h_i^{-1} k_i^b h_i` | `eq:geo-diagonal-gauge-functions` | `F(u_i^b h_i)=F(u_i^b)h_i` ⇒ `k_i^b h_i = h_i k_i^m`. ✓ |
| Cross-map gauge laws | `eq:geo-phi-gauge-law`, `eq:geo-tildephi-gauge-law` | `φ' = ρ̂_m(b_i)^{-1} φ ρ̂_b(a_i)`. ✓ (numeric ✓) |
| Intertwining ⇒ well-defined cross morphism | `prop:geo-intertwining-cross-map` | `[pg,φ(β)]=[p,ρ̂_m(g)φ(β)]` vs `[p,φ(ρ̂_b(g)β)]`. ✓ |
| Morphism gluing law | `eq:geo-cross-map-gluing` | `β_b^{(i)} = ρ̂_b(T_ij^b)β_b^{(j)}` ⇒ `φ_i ρ̂_b(T^b) = ρ̂_m(T^m) φ_j`. ✓ |
| `Φ`-representative twist `ρ̂_m(h_i^{-1})∘φ` | 02:257–260 | `[u_i^b,φ(β)] = [u_i^m h_i^{-1}, φ(β)] = [u_i^m, ρ̂_m(h_i^{-1})φ(β)]`. ✓ |
| Local connection law `Ad_{a^{-1}}A + a^{-1}da` | `eq:geo-local-connection-b/m` | Nakahara §10.1.3. ✓ |
| Difference of connections is `Ad(P)`-valued 1-form | 02:292–294 | Both `ω(σ(A))=A`, both `Ad`-equivariant ⇒ tensorial of type Ad. ✓ |
| Endpoint transport law | `eq:geo-pt-gauge-b/m` | `Ω' = ρ̂_b(a_1)^{-1} Ω ρ̂_b(a_0)`. ✓ |
| Defect is vertical; parallelness ⇔ commuting squares | `eq:geo-nonlinear-defect-phi`, `eq:geo-phi-parallelness` | Both terms project to `X`; types on both sides of each square match. ✓ |
| Linear reduction `DΦ = ∇^m∘Φ − Φ∘∇^b` and its tensoriality | `eq:geo-linear-covariant-defects` | `TΦ(H^b_s X) − H^m_{Φs}X = ∇^m_X(Φs) − Φ(∇^b_X s)`; sign and order correct. ✓ |
| Čech cocycle `T_ij T_jl = T_il`, `T_ji = T_ij^{-1}` | `eq:geo-cech-cocycle` | Three-frame composition ✓ (numeric ✓). Prose "change from l to j then j to i" matches `β^{(i)} = ρ̂(T_ij)β^{(j)}`. ✓ |
| Coboundary/triviality `T_ij = U_i U_j^{-1}` with rechoice `u_i' = u_i U_i` | `eq:geo-coboundary-form` | `T' = U_i^{-1}(U_iU_j^{-1})U_j = e`. ✓ |
| Trivialization data `u_i^x = σ_0 (U_i^x)^{-1}`, `h_i = U_i^b (U_i^m)^{-1}` | `eq:geo-frame-field` | Consistent with `T_ij = U_iU_j^{-1}`; **and this is the corrected form that discharges ledger item R02** (old `u_i = σ_0 U_i` gave `U_i^{-1}U_j`). ✓ (numeric ✓) |
| `T^m = h_i^{-1} T^b h_j` is exactly the Čech coboundary equivalence | `eq:geo-frame-comparison-relation`, 02:483 | ✓ (numeric ✓) |
| Graph-link gauge law and walk holonomy conjugation | `eq:geo-regime-two-gauge-law`, `eq:geo-link-holonomy` | `∏(a_{i_a}^{-1}Θ a_{i_{a+1}}) = a_{i_0}^{-1} H a_{i_0}`. ✓ |
| Trivializing criterion (coboundary ⇔ trivial closed-walk products) | `prop:geo-trivializing-criterion` | **I initially flagged a missing `Ξ_{ē}=Ξ_e^{-1}` hypothesis and then withdrew it**: because both sides quantify over *all* oriented edge copies including reversals, the walk `(ē,e)` forces `Ξ_ē Ξ_e = e`, and the coboundary form forces it too. The proposition is correct as stated. |
| Flat-link residual identities | `eq:geo-trivialized-residual`, `eq:geo-regime-two-residual`, `eq:geo-subfamily-trivialized-residual` | All three reduce to `μ_i − ρ_b(Θ_e^b)μ_j` by substitution. ✓ |
| Fixed point ⇒ global associated section without trivializing `P` | 02:521 | `[pg,β_0]=[p,ρ̂(g)β_0]=[p,β_0]`. ✓ |
| Product-extension action is a left `G_b×G_m` action | `eq:geo-product-cross-map-bundle` | ✓ |
| `Aut_G(P)` ≠ right `G`-action | 04:317–318 | `R_g` is `G`-equivariant iff `g ∈ Z(G)`. ✓ |
| Link/transport separation is a genuine holonomy statement, not a topology claim | 02:599–602 | Correct: connection holonomy is independent of bundle triviality (Nakahara §10.2). ✓ |
| Root-bridge covariance ⇒ `eq:geo-tildephi-gauge-law` | 04:348–351 | `φ̃'_i ρ̂_m(g_i^m) = ρ̂_b(g_i^b) φ̃_i`, and with `a_i=(g_i^b)^{-1}, b_i=(g_i^m)^{-1}` this is **exactly** `eq:geo-tildephi-gauge-law`. ✓ Cross-chapter claim confirmed. |
| Ch.2 ↔ Ch.4 link law agreement | `eq:geo-regime-two-gauge-law` vs `eq:gen-gauge-links` | With `a_i^x = (h_i^x)^{-1}`, `(a_i)^{-1}Θ a_j = h_i Θ h_j^{-1}`. Identical. ✓ |
| Moment congruence `RΣRᵀ` | `prop:geo-moment-pushforward` | Correct sandwich for a `Sym²V` object under `P×_{ρ_b}R^K` (Nakahara §9.4, §10.4). ✓ |

The passive/active distinction (02:165–178, 04:312–320) is drawn correctly and is the strongest
gauge-theoretic content in the manuscript: `eq:geo-local-reframing` is *not* a `G×G` gauge symmetry,
and the manuscript says so and proves the constraint `k_i^m = h_i^{-1}k_i^b h_i` that shows it.

---

## Finding G1 — `R_b, R_m` are undefined at point of use; the ESTABLISHED law is correct only under a convention first stated two chapters later

- **claim:** `eq:geo-defect-gauge-laws` is *not* a direction error, but both of its symbols are
  undefined where they appear, and the only same-chapter definition of a symbol of that shape uses a
  second undefined symbol and points the opposite way.
- **location:** `02_geometry.tex:361–367` (`eq:geo-defect-gauge-laws`); collides with
  `02_geometry.tex:660–666` (`eq:geo-represented-frame-change`); resolved only at
  `04_generative.tex:280–285` and `06a_generative_gaussian.tex:166–177`.
- **severity:** medium
- **status:** `\status{ESTABLISHED}` (02:368). The prose does not inflate the *content*, but tagging
  ESTABLISHED an equation whose two symbols have no definition in scope is a status/definition defect.
- **evidence (recomputation, adjudicating carried-over candidate #3):**
  - In the linear specialization, `DΦ` is tensorial of the same type as `Φ`, so it must obey the same
    law as `eq:geo-phi-gauge-law`: `φ' = ρ̂_m(b_i)^{-1} ∘ φ ∘ ρ̂_b(a_i)`.
  - Reading `R_x := ρ̂_x(section rechoice)` (i.e. `R_b = ρ̂_b(a_i)`, `R_m = ρ̂_m(b_i)`) gives
    `φ' = R_m^{-1} φ R_b`, which is the **inverse** of the displayed `R_m (DΦ) R_b^{-1}`.
  - Reading `R_x :=` the *coordinate-change operator* (`β' = R_b β`, i.e. `R_b = ρ̂_b(a_i)^{-1}`) gives
    `φ' = R_m φ R_b^{-1}`, which **matches** the display.
  - Numeric confirmation on random `GL(2,R)`: `(DΦ)' = R_m (DΦ) R_b^{-1}` with `R` = coordinate change:
    `True`; with `R = ρ(section rechoice)`: `False`.
  - The manuscript's global convention is the second one, but it is fixed only at 04:280–285
    ("this sample-coordinate transformation corresponds to the section rechoice
    `u_i^{x'} = u_i^x·(g_{a,i}^x)^{-1}`") and spelled out at 06a:170–177 ("This accounts for the
    opposite-sided inverse in the geometric local-map law"). Neither statement exists in Chapter 2.
  - Worse, `02:661` writes `R_i^b = ρ_b(g_i)` with **`g_i` never defined in Chapter 2**, in a section
    (`sec:geo-diagonal`, common-frame specialization) whose immediately preceding equation is
    `u_i^b = u_i^m = u_i`. A reader who takes `g_i` to be the section rechoice — the only rechoice
    letter Chapter 2 has introduced (`a_i, b_i` at `eq:geo-local-reframing`) — gets `R` pointing the
    wrong way at 02:361.
  - Additional inconsistency inside the pair: 02:361 puts the channel label in a **subscript**
    (`R_b, R_m`) while 02:661 puts it in a **superscript** (`R_i^b, R_i^m`), and the notation appendix
    declares (`appendix_notation.tex:5–8`) "Superscripts `b` and `m` always denote the belief and model
    channels." `R_b, R_m` occur **nowhere else in the manuscript** (whole-tree grep).
- **fix:** at 02:361 replace "If `R_b,R_m` denote the represented coordinate changes" with a
  definition tied to the equations already on the page, e.g.
  "Write `R_i^b = ρ̂_b(a_i)^{-1}` and `R_i^m = ρ̂_m(b_i)^{-1}` for the represented coordinate changes
  induced by `eq:geo-local-reframing`, so that `β' = R β` in each channel"; then the displayed law is
  literally `eq:geo-phi-gauge-law`. At 02:661 define `g_i` (it is the *re-expression* element of
  04:273, whose section rechoice is `g_i^{-1}`) and use the same super/subscript placement.
- **falsifies:** exhibiting a definition of `R_b, R_m` anywhere in Chapters 1–2 would kill this
  finding; so would a cross-reference at 02:361 to 04:280–285.
- **adjudication of the carried-over candidate:** the prior session's stronger claim (that
  `eq:geo-defect-gauge-laws` is *wrong*, and that Chapter 7b uses the opposite convention) is
  **not sustained**. `\mathcal R_b` in `07b_agent_network_rg.tex:614–771` is the block-`b`
  renormalization operator (`b > 1` a blocking ratio, `\log b`), a different glyph and a different
  object; that part of the prior finding was a symbol confusion. See G11 for the residual notation
  point that remains.

---

## Finding G2 — the ESTABLISHED density/Jacobian law assumes a reference measure that is relatively invariant under the represented action; false on the manuscript's own mixed-coordinate tier

- **claim:** `p_{θ'}(o,y'|X') = |det R|^{-1} p_θ(o, R^{-1}y' | X)` requires `ν_D^Y` to satisfy
  `R_# ν_D^Y = |det R|^{-1} ν_D^Y`. That holds on the pure-Lebesgue tier and fails on the mixed real
  coordinates that Chapter 3 explicitly declares admissible.
- **location:** `04_generative.tex:353–377`, `eq:gen-gauge-joint-pushforward`
  (`prop:gen-product-evidence-invariance`). Interacts with
  `03_probability.tex:71–82` (`def:prob-reference-measures`) and
  `prop:prob-mixed-coordinate-dominating-measure`.
- **severity:** medium
- **status:** `\status{ESTABLISHED}` (04:371). The hypothesis carried is only "when the local actions
  are linear and densities exist" — that is not enough.
- **evidence (recomputation):** Chapter 3 declares `ν^k_{i,a}` may be the mixed measure
  `ν = λ|_{A^c} + #|_A` for a countable atom set `A`. Take `R = 2` on one real latent coordinate,
  `A = {0}`, so `ν = λ + δ_0`. Then `R_#ν = ½λ + δ_0`, and
  `d(R_#ν)/dν = ½` off the atom, `= 1` at the atom. Hence
  `d(R_#P)/dν (y) = p(R^{-1}y)·(d(R_#ν)/dν)(y)`, which equals `|det R|^{-1}p(R^{-1}y) = ½p(y/2)`
  off the atom but equals `p(0)` at `y = 0`. The atom carries `ν`-mass 1, so this is a failure on a
  `ν`-non-null set, not a null-set quibble. More generally `R_#ν = |det R|^{-1}ν` characterizes
  Haar/Lebesgue-type relative invariance, which `def:prob-reference-measures` does not impose.
  The manuscript **states the correct principle itself** at `03_probability.tex:163`: "A frame change
  that does not preserve the reference measure changes the density and the base-measure Jacobian
  together, and only their combination is invariant" — but
  `prop:gen-product-evidence-invariance` does not carry that as a hypothesis.
- **what survives:** the measure-level statement `P_{θ'}(·|X') = T_# P_θ(·|X)` is correct with no
  extra hypothesis, and the load-bearing conclusion `eq:gen-gauge-evidence-invariance` follows from it
  directly (`T` is the identity on `o`, so the `o`-marginals coincide as measures). Only the
  intermediate density display is defective. This is why I did not rate it higher.
- **fix:** add to the proposition "and the latent reference measure is relatively invariant under the
  represented action with multiplier `|det R|`, e.g. when every latent coordinate is continuous
  Euclidean with its Lebesgue base measure"; or state the density identity as
  `p_{θ'}(o,y'|X') = p_θ(o,R^{-1}y'|X)·(d(R_#ν_D^Y)/dν_D^Y)(y')^{-1}` and note it reduces to
  `|det R|^{-1}` on the Lebesgue tier. Derive `eq:gen-gauge-evidence-invariance` from the measure
  identity rather than from the density.
- **falsifies:** a declaration elsewhere restricting all latent coordinates carrying a nontrivial
  linear `ρ_b`/`ρ_m` action to continuous Euclidean coordinates would kill this finding. I found none;
  `def:prob-reference-measures` explicitly admits discrete, mixed, and "any other fiber".

---

## Finding G3 — "the full residual group is the stabilizer of the shared-link constraints" — the admissible-rechoice set at a fixed shared link is not a group

- **claim:** the set of frame rechoices satisfying the displayed shared-link admissibility condition is
  not closed under composition, so it is not a residual gauge group; and the setwise stabilizer of the
  constraint set (which *is* a group) is strictly smaller than that set.
- **location:** `04_generative.tex:299–311` (the unnumbered display at 04:303–306 and the sentence
  "the full residual group is the stabilizer of the shared-link constraints").
- **severity:** medium
- **status:** the surrounding block is `\status{DEFINITION}\label{def:gen-product-action}` (04:321).
  The prose nonetheless makes a group-theoretic assertion ("the full residual group is ...") that the
  definition does not license — mild status inflation.
- **evidence (numeric counterexample, `GL(2,R)`, two design points `a ∈ {1,2}`, vertices `i,j`, shared
  link `Θ = I`, gauge law `Θ'_a = h_{a,i} Θ h_{a,j}^{-1}` per `eq:gen-gauge-links`):**
  - `h`: `h_{1,i}=h_{1,j}=k_1`, `h_{2,i}=h_{2,j}=k_2` (context-**dependent**). Admissible: `True`
    (both design points give `Θ' = I`).
  - `h'`: `h'_{a,i}=C`, `h'_{a,j}=I` (context-**independent**). Admissible: `True`.
  - Pointwise product `h·h'`: `(h h')_{a,i} = k_a C`, `(h h')_{a,j} = k_a`, giving
    `Θ'_a = k_a C k_a^{-1}`, which depends on `a`. Admissible: **`False`**.
    Numeric output: `link(a=1) = [[0.5488, 1.2049], [-0.0196, -1.4968]]`,
    `link(a=2) = [[0.5061, -0.1152], [-0.5377, -1.4540]]`.
  - Algebraically: if `h_{a,i}Θh_{a,j}^{-1} = Θ^{(1)}` (const in `a`) and `h'_{a,i}Θh'_{a,j}^{-1}`
    is const, then `(h'h)_{a,i}Θ(h'h)_{a,j}^{-1} = h'_{a,i}Θ^{(1)}h'^{-1}_{a,j}`, which is constant only
    if `h'` stabilizes `Θ^{(1)}` — a *different* link. So the condition is link-dependent and the set is
    not a subgroup for nonabelian `G`. (For abelian `G` it is a subgroup, which is why the claim reads
    plausibly.)
  - The setwise stabilizer of the whole constraint set is `{h : h_{a,i}h_{a',i}^{-1} ∈ Z(G)` and
    `h_{a,i}h_{a,j}^{-1}` const in `a}` — strictly smaller than the displayed admissibility set, so the
    two readings of the sentence are genuinely different objects.
  - The two neighboring claims *are* correct and I verified them: context-independent rechoices form a
    subgroup and are sufficient; they are not necessary (take `k_a` in the centralizer of `Θ`).
- **fix:** replace "the full residual group is the stabilizer of the shared-link constraints" with
  "the admissible rechoices at a given constrained `Θ` are the solution set of the displayed
  condition; for nonabelian `G` this set need not be a subgroup, and the largest subgroup acting on the
  constrained submodel is the setwise stabilizer of the shared-link constraint set."
- **falsifies:** a demonstration that the intended composition law is not the pointwise product
  `(h'h)_{a,i} = h'_{a,i}h_{a,i}` would falsify this; but that product is forced by iterating
  `eq:gen-gauge-links`.

---

## Finding G4 — `h` carries two unrelated gauge meanings, and the notation appendix (advertised as a type checker) lists both without flagging the collision

- **claim:** `h_i` (relative principal-frame field, `u_i^m = u_i^b h_i`) and `h_i^x` (discrete vertex
  frame change, `h_{a,i}^x = g_i^x(c_a)`) are unrelated objects sharing a glyph, appearing together in
  the same chapter; and the same `Θ`-gauge law is displayed twice with opposite-sided inverses under
  two different letters with no reconciling sentence.
- **location:** `02_geometry.tex:58–65` (`eq:geo-relative-frame`, `h_i`) and
  `02_geometry.tex:537–547` (`eq:geo-regime-two-gauge-law`, letter `a_i^x`) vs
  `04_generative.tex:290–298` (`eq:gen-gauge-links`, letter `h_i^x`) and
  `appendix_notation.tex:40–43` vs `appendix_notation.tex:131–138, 214–222`. Both meanings co-occur in
  `06a_generative_gaussian.tex:155–161` (`h_i = U_i^b(U_i^m)^{-1}`) and `06a:249` (links obey
  `eq:gen-gauge-links`, i.e. `h_i^b`).
- **severity:** medium
- **status:** `\status{ESTABLISHED}` / `\status{DEFINITION}` respectively; the mathematics is right,
  the naming is not.
- **evidence:** I confirmed the two link laws are *consistent*, not contradictory:
  `eq:geo-regime-two-gauge-law` gives `Θ'_e = (a_i^b)^{-1} Θ_e^b a_j^b`;
  `eq:gen-gauge-links` gives `Θ'_{ij} = h_i^b Θ_{ij}^b (h_j^b)^{-1}`. These agree exactly under
  `a_i^x = (h_i^x)^{-1}`, which follows from 04:283 (`u_i^{x'} = u_i^x (g_{a,i}^x)^{-1}`) plus
  02:546 (`a_i^b = a_i(c_i)`). **Neither equation cross-references the other and the relation
  `h_i^x = (a_i^x)^{-1}` is never written down.** Given that ledger item R02 was exactly a direction
  error of this shape, leaving two opposite-sided displays of the same law unreconciled is a live
  hazard, not a cosmetic one.
  `appendix_notation.tex` claims to be "a type checker, not a second development of the theory"
  (line 4) and then lists `h_i` at line 40 and `h_i^x` at line 135 as if they were the same family.
- **fix:** rename the vertex frame changes (e.g. `v_i^x` or keep Chapter 2's `a_i^x`), or add one
  sentence at 04:291 and in the appendix: "`h_i^x = (a_i^x)^{-1}` in the notation of
  `eq:geo-regime-two-gauge-law`; it is unrelated to the relative principal-frame field `h_i` of
  `eq:geo-relative-frame`." Add a row to the appendix distinguishing them.
- **falsifies:** a sentence somewhere already stating `h_i^x = (a_i^x)^{-1}` or distinguishing `h_i`
  from `h_i^x`. Grep found none.

---

## Finding G5 — the finite-design passive coordinate group `∏_{a,i}(G×G)` requires `G` connected (or design points in distinct components of `C_i`)

- **claim:** for a connected support `C_i` and a **disconnected** Lie group `G`, the values of a smooth
  section rechoice at several design points must all lie in one connected component of `G`, so the
  group realized by frame rechoices is a proper subgroup of `∏_{a,i}(G×G)`.
- **location:** `04_generative.tex:312–314` ("Across the unconstrained finite design the passive
  coordinate group is `∏_{a,i}(G×G)`"), depending on `04:271–273` (`g_{a,i}^b = g_i^b(c_a)`) and
  `def:geo-principal-systems` (02:46, "a Lie group `G`" — no connectedness declared).
- **severity:** medium-low
- **status:** `\status{DEFINITION}` (04:321). As a *declaration* of a coordinate group it is
  unobjectionable; the defect is the implicit claim that this group is *induced by* section rechoices,
  which is what makes it passive bookkeeping rather than new structure.
- **evidence:** given two smooth sections `u, u'` of `P` over connected `C_i`, the unique `a: C_i → G`
  with `u' = u·a` is smooth, hence continuous, hence lands in a single component of `G`. So the
  realizable value-tuples `(a(c_1),…,a(c_M))` form
  `{(g_1,…,g_M) : all g_a in one component}`, a proper subgroup of `G^M` whenever `|π_0(G)| > 1` and
  `M ≥ 2`. Conversely for connected `G` surjectivity holds: any `g` is a finite product of
  exponentials, so `t ↦ exp(tξ_1)···exp(tξ_n)` composed with disjoint bump functions realizes arbitrary
  prescribed values at finitely many points. `GL(K,R)` — the natural group for this program — is
  disconnected. The realization dodges this: `06_gaussian.tex:138,145` and
  `06a_generative_gaussian.tex:280` work in `GL^+(K)`, which **is** connected, so nothing downstream
  breaks. This is a gap in the general chapter only.
- **fix:** either add "assume `G` connected, or that `C_i` has one component per design point" at
  04:312, or state the group as the image of the evaluation map
  `C^∞(C_i,G)^{×2} → (G×G)^M` and note it equals `∏_{a,i}(G×G)` when `G` is connected.
- **falsifies:** a declaration of connectedness of `G` (or of `C_i`'s components) that I missed; or an
  argument that the finite-design formulas never require the rechoice to extend to a smooth section.
  Note the latter is blocked by 02:544–546, which explicitly says the vertex rechoices "are induced by
  smooth frame rechoices" after anchoring.

---

## Finding G6 — "acts diagonally on both associated bundles" is an `h_i`-twisted diagonal, not a diagonal

- **claim:** the sentence contradicts `eq:geo-diagonal-gauge-functions` in the general case.
- **location:** `04_generative.tex:316–318`.
- **severity:** low
- **status:** `\status{DEFINITION}` (04:321); no inflation, a wording defect.
- **evidence:** `F ∈ Aut_G(P)` induces coordinate actions `ρ̂_b(k_i^b)` and `ρ̂_m(k_i^m)` with
  `k_i^m = h_i^{-1}k_i^b h_i` (`eq:geo-diagonal-gauge-functions`, which I verified). So the image of
  `Aut_G(P)` inside the passive group `∏_{a,i}(G×G)` is the **`h_i`-twisted diagonal**
  `{(g, h_i^{-1} g h_i)}`, which equals the diagonal `{(g,g)}` only under the common-frame
  specialization `h_i = e` (`eq:geo-diagonal-principal`). A reader who takes "diagonally" literally
  will misidentify the active subgroup.
- **fix:** "it acts on both associated bundles through one and the same automorphism, whose two local
  descriptions are related by `eq:geo-diagonal-gauge-functions`; it is the `h_i`-twisted diagonal in
  `∏_{a,i}(G×G)`, reducing to the diagonal exactly when `h_i = e`."
- **falsifies:** reading "diagonally" as merely "on both simultaneously" — which is presumably the
  intent, and is why this is low and not medium.

---

## Finding G7 — "its inverse multiplies the principal frame on the right" conflates `G` with `ρ_x(G)`

- **claim:** the object multiplying the principal frame is `(g_{a,i}^x)^{-1} ∈ G`, not
  `R_{a,i}^x{}^{-1} ∈ ρ_x(G)`; the sentence types a represented matrix into the principal bundle.
- **location:** `04_generative.tex:283–285`.
- **severity:** low
- **status:** `\status{DEFINITION}`; wording only.
- **evidence:** Chapter 2 makes exactly this distinction load-bearing at 02:141–143: "when a
  representation is nonfaithful, represented frame data alone determine at most a coset modulo its
  kernel; the principal sections, rather than their represented images, are what make `h_i` unique."
  Under a nonfaithful `ρ_b`, `R^{-1}` does not determine the group element that multiplies the frame,
  so the sentence is false as written for the generality Chapter 2 insists on.
- **fix:** "…while the group element `(g_{a,i}^x)^{-1}`, of which `R_{a,i}^x` is the representative,
  multiplies the principal frame on the right."
- **falsifies:** a standing assumption of faithfulness — explicitly disclaimed at 02:87 and
  `appendix_notation.tex:26–30`.

---

## Finding G8 — "this compatible family is equivalently a section of the associated map bundle" is off by the `h_i` twist

- **claim:** the local representatives of a section of `P ×_λ Map(B_b,B_m)` are `ρ̂_m(h_i)∘φ_i`, not
  `φ_i`; the bijection is correct, the identification of representatives is not.
- **location:** `02_geometry.tex:254–256`.
- **severity:** low (clarity)
- **status:** unstatused prose following `eq:geo-cross-map-gluing`.
- **evidence:** put `f_i := ρ̂_m(h_i)∘φ_i`. Using `T^m_{ij} = h_i^{-1}T^b_{ij}h_j` and the gluing law
  `φ_i ρ̂_b(T^b_{ij}) = ρ̂_m(T^m_{ij})φ_j`, I get exactly
  `f_i = ρ̂_m(T^b_{ij}) ∘ f_j ∘ ρ̂_b(T^b_{ij})^{-1}` — the map-bundle transition with the **single**
  group element `T^b_{ij}`, as the displayed action `f ↦ ρ̂_m(g)∘f∘ρ̂_b(g)^{-1}` requires. The family
  `{φ_i}` itself obeys a **two-element** law (`T^b` on the right, `T^m` on the left) and is therefore
  not a section's local family. Consistency check: for `Φ` induced by an intertwiner `φ`, the
  manuscript's own 02:259 gives `φ_i = ρ̂_m(h_i^{-1})∘φ`, hence `f_i = φ` constant — correct, a
  `G`-invariant map is a constant section.
- **fix:** "…this compatible family is equivalently, after the frame conversion `f_i = ρ̂_m(h_i)∘φ_i`,
  a section of the associated map bundle…". The next two sentences already supply the twist; one clause
  makes it a statement rather than an inference.
- **falsifies:** a declaration that `φ_i` is defined in the `u_i^b` frame for both channels — but
  02:200–201 says "In the frames `u_i^b, u_i^m`", i.e. two frames.

---

## Finding G9 — §2.10's closing sentence shifts from law-level `ρ̂`-equivariance to sample-level linear intertwiners

- **claim:** the obstruction claim is stated at the wrong level; the condition actually in force
  (`eq:geo-intertwining`) is equivariance of maps `B_b → B_m` on *laws*, which is strictly weaker than
  existence of a linear intertwiner `K → M`.
- **location:** `02_geometry.tex:673–676`.
- **severity:** low (clarity)
- **status:** unstatused prose closing a `\status{HYPOTHESIS}` section.
- **evidence:** any `G`-equivariant Markov kernel `K ⇝ M` induces a `ρ̂`-equivariant map on laws
  without being (or inducing) a linear intertwiner — and this is precisely the construction Chapter 4
  uses at `eq:gen-root-law-bridge` ("Only this pushforward-on-laws map can represent the local
  associated-bundle morphism"). Moreover, if `B_m` contains a `G`-fixed law — the very situation the
  manuscript exploits at 02:521 — the constant map is always `ρ̂`-equivariant, so *some* cross morphism
  always exists. The sentence is saved only by the word "linear", which is doing unannounced work at a
  different type level from `eq:geo-intertwining`.
- **fix:** "…they may obstruct the existence of a nonzero linear intertwiner between the sample fibers;
  law-level `ρ̂`-equivariance is weaker, and `eq:gen-root-law-bridge` supplies an example realized by a
  Markov kernel rather than a linear map."
- **falsifies:** reading "linear intertwiner" as already scoped to sample fibers — which is my
  charitable reading, and why this is low and flagged as a clarity item rather than an error.

---

## Finding G10 — Chapter 3 collapses the channel-specific gauge data into unsuperscripted symbols and introduces an undefined link symbol

- **claim:** `03_probability.tex:51` says a structural configuration "may carry the finite interaction
  complex `𝕴` of `def:geo-graph-links` with its edge set, the frames `U_i` or the links `L_{ij}`" —
  but Chapter 2's frames are `U_i^b, U_i^m` (channel-specific, `eq:geo-frame-field`) and its links are
  `Θ_e^b, Θ_e^m` (channel-specific, `eq:geo-regime-two-links`). `L_{ij}` occurs nowhere else in the
  manuscript.
- **location:** `03_probability.tex:51`, referencing `def:geo-graph-links` (`02_geometry.tex:527`).
- **severity:** low-medium
- **status:** `\status{DEFINITION}`.
- **evidence:** whole-tree grep: `L_{ij}` appears exactly once, at 03:51, with no definition. Dropping
  the channel superscript on `U_i` silently imposes the common-frame specialization that
  `sec:geo-diagonal` (02:649–671) declares a strictly stronger `\status{HYPOTHESIS}`
  ("None of these three stronger hypotheses follows from the others"). This is exactly the confusion
  Chapter 2 spends §2.2–§2.3 preventing.
- **secondary:** `𝕴` is declared "a finite interaction multigraph declared independently of `C`" with a
  fixed-point-free reversal involution (02:528–530), while Chapter 4 attaches links to the **directed
  acyclic** `Γ = (V,E)` of `04:16`. The identification `𝕴 ↔ Γ` (presumably `𝕴` = the double of `Γ`) is
  never stated, and Chapter 4's `Θ_{ij}` never restates the reversal convention `Θ_{ji} = Θ_{ij}^{-1}`
  that `eq:geo-regime-two-links` supplies and that `prop:geo-trivializing-criterion` needs.
- **fix:** at 03:51 write "the channel frames `U_i^b, U_i^m` or the channel links `Θ_e^b, Θ_e^m`", and
  add one sentence in Chapter 4 identifying `𝕴` with the double of `Γ` and inheriting the reversal
  convention.
- **falsifies:** a definition of `L_{ij}` elsewhere, or a declaration that Chapter 3 operates only in
  the common-frame specialization.

---

## Finding G11 — gauge-symbol glyph collisions across the manuscript

- **claim:** four glyphs central to the gauge development carry incompatible meanings in different
  chapters, without the notation appendix recording the conflict.
- **location / severity:** low each, collectively low-medium.
  1. **`G`** — the structure group throughout Ch. 2/4 (`def:geo-principal-systems`), but a *graph* at
     `06_gaussian.tex:145` ("Let `G=(V,E)` be a connected graph") and a *congruence matrix* at
     `06_gaussian.tex:130` (`G = diag(I_2,S)`) — in a proposition and a paragraph that are entirely
     about `GL^+(K)`-valued gauge links.
  2. **`b`** — belief-channel label everywhere; but the *model*-channel section rechoice in
     `eq:geo-local-reframing` (`u_i^{m'} = u_i^m·b_i`); and the *blocking ratio* in
     `07b_agent_network_rg.tex:600–640` (`b > 1`, `\log b`, `\mathcal R_b`, `K_b`, `C_b`).
  3. **`ρ`** — the belief/model representations `ρ_b, ρ_m` in Ch. 2/4; the *baseline probability
     measure* in `07b` (`\mathcal R_b^ρ ρ = ρK_b`), so `ρ_b` in 07b's idiom would read "baseline at
     scale `b`".
  4. **`a`** — the design index `c_a` (Ch. 4) and the walk-step index in `eq:geo-link-holonomy`
     (`Θ_{e_a}`, `a = 0..r-1`) and the belief-channel section rechoice `a_i` (`eq:geo-local-reframing`);
     `Θ_{e_a}` (walk step) versus `Θ_{a,ij}` (design point) is a direct clash on the same symbol.
- **status:** all `\status{DEFINITION}`/`\status{ESTABLISHED}`; no inflation, purely notational.
- **evidence:** whole-tree greps as cited; `appendix_notation.tex` records none of the four.
- **fix:** rename the graph at 06_gaussian:145 (`\mathfrak G` or `\Gamma`), the congruence matrix at
  06_gaussian:130, and the model-channel rechoice `b_i` (to `a_i^m`, which Ch. 2 already uses at
  02:539–546); add an appendix paragraph on reused letters, in the style of the existing "Three
  transports" and "Three uses of pullback" paragraphs.
- **also settles:** `R_b, R_m` occur **only** at 02:361–365 in the whole manuscript;
  `\mathcal R_b` in 07b is a distinct glyph and a distinct object. The `R_b`/`\mathcal R_b`
  "collision" alleged by the interrupted session does not exist as a gauge-convention conflict; the
  only residual issue is the *undefined* `R_b, R_m` recorded as G1.

---

## Summary table

| # | Finding | Severity | Location |
|---|---|---|---|
| G1 | `R_b,R_m` undefined; ESTABLISHED law correct only under a Ch.4 convention; `g_i` undefined at 02:661 | medium | 02:361–367, 02:660–666 |
| G2 | Jacobian density law needs a relatively-invariant reference measure; fails on declared mixed coordinates | medium | 04:353–377 |
| G3 | Shared-link "residual group" is not a group (numeric counterexample) | medium | 04:299–311 |
| G4 | `h_i` vs `h_i^x` collision; `Θ` gauge law displayed twice with opposite-sided inverses, unreconciled | medium | 02:58–65, 02:537–547, 04:290–298, appendix:40/135/218 |
| G5 | `∏_{a,i}(G×G)` needs `G` connected | medium-low | 04:312–314 |
| G6 | Active gauge group is the `h_i`-twisted diagonal, not the diagonal | low | 04:316–318 |
| G7 | Represented matrix typed into the principal bundle | low | 04:283–285 |
| G8 | Map-bundle section representatives are `ρ̂_m(h_i)∘φ_i`, not `φ_i` | low | 02:254–256 |
| G9 | Law-level equivariance vs sample-level linear intertwiner | low | 02:673–676 |
| G10 | Ch.3 drops channel superscripts; `L_{ij}` undefined; `𝕴` vs `Γ` unidentified | low-medium | 03:51, 02:527 |
| G11 | Glyph collisions `G`, `b`, `ρ`, `a` | low | multiple |

**Findings I raised against myself and withdrew:** (i) a missing `Ξ_ē = Ξ_e^{-1}` hypothesis in
`prop:geo-trivializing-criterion` — withdrawn, both sides quantify over all oriented copies and the
condition is self-enforcing; (ii) `eq:geo-defect-gauge-laws` being a direction error — withdrawn,
downgraded to G1; (iii) failure of evidence invariance in `prop:gen-product-evidence-invariance` —
withdrawn, the measure-level route is sound, only the density display is defective (G2).

---

## Canonical sources used

- **Kobayashi, S. & Nomizu, K., _Foundations of Differential Geometry_, Vol. I (Interscience, 1963),
  Ch. II.** §1 (connections in a principal bundle; the local forms and their transformation),
  §5 (curvature and the structure equation), §7 (holonomy groups). The affine-space structure of the
  space of connections — "the difference of two connection forms is a tensorial 1-form of type
  `ad G`" — is the source for 02:292–294. Cited by the manuscript at 02:321 and 02:497; the citation
  supports the sentence.
- **Nakahara, M., _Geometry, Topology and Physics_, 2nd ed. (IoP, 2003).** §9.4 associated bundles
  (the convention `(u,v) ~ (ug, ρ(g)^{-1}v)`, which is `eq:geo-quotient-convention`); §10.1.3 the local
  connection form / gauge potential and its transformation `A_j = g_{ij}^{-1}A_i g_{ij} +
  g_{ij}^{-1}dg_{ij}`, which is `eq:geo-local-connection-b`; §10.2 holonomy; §10.3 curvature; §10.4 the
  covariant derivative on associated bundles, which is the source for the congruence
  `Σ ↦ RΣRᵀ` on a `Sym²`-valued associated section (`prop:geo-moment-pushforward`). Note for the
  record: the sandwich rule is a §9.4 + §10.4 statement, **not** §10.3, which is curvature.
- **Bleecker, D., _Gauge Theory and Variational Principles_ (Addison-Wesley, 1981), Ch. 3.** The gauge
  group as `Aut_G(P)` over `id_M` and its identification with sections of the conjugation bundle
  `P ×_{conj} G` — the source for the correct reading of 04:316–318 and for G6.
- **Steenrod, N., _The Topology of Fibre Bundles_ (Princeton, 1951), §2–§8.** Coordinate bundles,
  cocycle conditions, and the equivalence of coordinate bundles under a coboundary — the source for
  `eq:geo-cech-cocycle`, `eq:geo-coboundary-form`, and the claim that
  `eq:geo-frame-comparison-relation` is the coboundary equivalence. Cited at 02:497; supports it.
- **Husemoller, D., _Fibre Bundles_, 3rd ed. (Springer, 1994), Ch. 4–5.** Global-section
  characterization of a trivial principal bundle. Cited at 02:497; supports it.
- **Baez, J. & Muniain, J.P., _Gauge Fields, Knots and Gravity_ (World Scientific, 1994), Part II.**
  Lattice/graph holonomy as an ordered product of edge group elements and its conjugation law under
  vertex gauge transformations — the elementary model behind `eq:geo-link-holonomy` and
  `prop:geo-trivializing-criterion`.
- **Fulton, W. & Harris, J., _Representation Theory_ (Springer, 1991), §1.2 (Schur's lemma).** Relevant
  to G9: Schur gives `Hom_G(ρ_b,ρ_m) = 0` only for irreducible inequivalent complex representations;
  Chapter 2 assumes neither irreducibility nor a complex field, so the obstruction language at
  02:673–676 needs its hedge.

## Newly-discovered canon worth adding to `01b_extended_evidence.md`

- **Weiler, M., Forré, P., Verlinde, E., Welling, M., _Equivariant and Coordinate Independent
  Convolutional Networks_ (2023), Ch. 3–5.** Derives, from first principles, that demanding
  coordinate-independence plus weight sharing *forces* local gauge equivariance, with explicit
  `G`-structure, associated-bundle, and parallel-transport bookkeeping — the closest ML-side canon to
  Chapter 2's construction, and it uses the same right-action/quotient convention. Relevant to G1
  because it writes the coordinate-change operator explicitly rather than leaving `R` implicit.
  (Already in the vault as `[[weiler-2021-coordinate-independent-cnns]]`.)
- **Culver, W.J., "On the existence and uniqueness of the real logarithm of a matrix",
  _Proc. AMS_ 17 (1966), 1146–1151.** Already cited by the manuscript at `06a:281` for the
  `exp`-nonsurjectivity caveat. Worth surfacing in the shared evidence file because it is the source
  for why `GL^+(K)` (connected, but not exponential) is the operative group — which is what defuses
  G5 in the realization while leaving the general chapter exposed.
