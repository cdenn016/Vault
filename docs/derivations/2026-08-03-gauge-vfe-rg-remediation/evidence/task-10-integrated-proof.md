<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 10 integrated construction: bundle pullbacks, signed anomalies, configuration geometry, and timeless histories

## 1. Scope and revision binding

This is a construction record for the Task 10 integration pass. It is not a
proposal. Every theorem named below is stated and proved in the released source
at the digests of Section 3, and every load-bearing identity was recomputed
here in exact rational or symbolic arithmetic before it was written into the
source (Section 8).

**Pre-edit base.** Commit `02d5d8f542cba2d92c6a430483b62155dd5f2db4`
(`docs: derive RG modes beta functions and fixed objects`) on branch
`codex/gauge-vfe-rg-task10-pullbacks-20260804`. At the start of this pass the
working tree carried, in addition to that commit, six untracked Task 10
evidence artifacts and nothing else.

**Pre-edit digests of the six initially targeted source files**, as independently recorded by
`evidence/task-10-interface-reconciliation.md` Section 0.1 and reconfirmed by
this pass before the first edit:

| Path | Pre-edit SHA-256 |
| --- | --- |
| `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex` | `a87bc2b3d7d8d76412a299fbd3220464802bd1cc2d853f1f6c287f96e5a73279` |
| `manuscripts/gauge_vfe_rg/05d_relational_inference.tex` | `138e4f86f107f5bd0307e049dc5368a6c36584a827bf98bf4eb396e30016d0a1` |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `a3a7ae2fed2eb4a1ea4668393a69b4d56aa2c9dd071af06ddbcba717d7365797` |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `148d9652229eb6d3c40a41b48c1eb938328ca697a37e8113111567c580cc61be` |
| `manuscripts/gauge_vfe_rg/08_infogeometry.tex` | `55bfcdff0eebec24f2231852467255d13a0c02d1369621d04ede53cad3b7c31b` |
| `manuscripts/gauge_vfe_rg/appendix_notation.tex` | `d39936499c9673c1b4ed75ae31bf294f8d4df9fd1fd0cef1dae4a9ec5a572fa4` |

No TeX build and no Git operation was run by this pass. No file under
`.verification/`, no `main.tex`, no `references.bib`, no `SPEC.md`, and no
prior evidence report was modified. `manuscripts/gauge_vfe_rg/main.pdf` was not
regenerated and therefore still does not render the current sources; that is
recorded as an open provenance obligation in Section 10 and is not this pass's
to close.

## 2. Independence boundary of the inputs

Six historical Task 10 analyses preceded this integration and none was edited
by it. The source map added during repair is a current primary-source artifact.
Their digests, recomputed here on the working-tree bytes:

| Artifact | SHA-256 | Role |
| --- | --- | --- |
| `evidence/task-10-interface-reconciliation.md` | `28eaa80a51223f0a6a7922700ca00bc3f419fd7f3563da239a8bb4936e5fffdb` | reconciled theorem source |
| `evidence/task-10-fable-mechanism-audit.md` | `f5aa5fde49716c4fb4c4f6146d99784786ff64cc8e35fcc0f2fa86716323c277` | independent mechanism check |
| `evidence/task-10-preintegration-adversarial.md` | `ff81719406628644a3cde746cb88dc91ca7c282ab1eed51a217cf1b584abf44c` | falsification obligations |
| `evidence/task-10-timeless-history-analysis.md` | `e1bbfa7c32dbcae010e4e2f62e5a8e356907c4ecabf0e604ae4a461e3f57f7f4` | typed-history route |
| `evidence/task-10-bundle-pullback-analysis.md` | `124010f91e7bc2a7569d5d85bc9dcf5ba44581da508eb246a836ca222b00e63b` | superseded bundle route |
| `evidence/task-10-score-configuration-analysis.md` | `9161b0f0941ed7b2061ba1102b2a5df5acbe318a8c2d57fc391003f7a782de4f` | superseded score/configuration route |
| `evidence/task-10-dqm-transfer-source-map.md` | `2776d62ca12633d10ddf91c57f9327e51e60dda22d9b63aaad59203bc5996794` | Pollard primary-source transfer map |

The digests of the four shared inputs agree with the binding tables of both the
reconciliation and the adversarial pass. **No input drift is reported.**

The six historical analyses share the repository, runtime, and model family.
They are
mechanism-diverse search inputs, **not** independent corroborating evidence, and
this pass uses no agreement among them as a reason to close anything. Where two
of them disagree, the disagreement is decided here by recomputation, and two
such decisions went against the artifact that stated the number (Section 8.7).
The affirmative search prior attached to the commissioning brief occurs in no
hypothesis, premise, counterexample, disposition, or status assigned below;
Section 9 records the erasure audit.

## 3. Final source digests

These are SHA-256 digests of the committed Git-blob bytes in the immutable
Task 11 provenance snapshot. The final column records the exact counts of CRLF
pairs and bare LF bytes returned by `git show REVISION:path`; every row has
zero bare CR bytes. The table is
deliberately acyclic: it binds the edited sources and the forward control
artifacts that do not themselves bind this record.
`claim-ledger.json` and `adversarial-report.json` are excluded because each
carries the digest of this proof; after this file is frozen, those two controls
bind it in the reverse direction. Including either digest here would require a
cryptographic fixed point rather than an auditable dependency graph.

| Path | Post-edit SHA-256 | Committed-blob EOL counts (CRLF; bare LF) |
| --- | --- | --- |
| `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex` | `de8bac720312cb6c9d4c1dfaaa26574ceb692f7d2c76de91acef487a08b0aaff` | `0; 1380` |
| `manuscripts/gauge_vfe_rg/05d_relational_inference.tex` | `fc78ad04d241818b5e2a3c20304fc70b62b4da8ed9e8336fc86523070d17f51a` | `0; 1549` |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `c995a4543312932513566ae8c592fb4692b32a128f5680853c5240d95b9d862f` | `0; 1034` |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `7b1528bbabe9849644c777e740ec9f2e6accf944178fdb267e537e8fe759851f` | `0; 2788` |
| `manuscripts/gauge_vfe_rg/08_infogeometry.tex` | `8a3917fd8ac4861df6ae7ced72368bd31d3a98cfac3acb95e251badf60ec5ee0` | `0; 574` |
| `manuscripts/gauge_vfe_rg/appendix_notation.tex` | `11fffe9a9b36cc071d280a40ab277e5ad3260337462f02eb1d33bb679591ab24` | `0; 515` |
| `manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex` | `096057eb33f02ea659f914bad3befaedc280cfa15c27e5587500e5d3926ab596` | `0; 302` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/dependency-dag.json` | `1d7ab02e05f8e95ee1e4be7e5d03308ed07863315c05378ae99ea5ad210de711` | `0; 166` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/approach-registry.json` | `6d020b5769853e4293019bb9bb7e51e4c2c80b057a2d2fce32e14474ff88d611` | `0; 393` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/counterexample-register.md` | `37d92b1ca801c37218dbb6e668ce948cf014017d8eac87fc46036820199c15dd` | `0; 83` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/evidence/task-10-dqm-transfer-source-map.md` | `2776d62ca12633d10ddf91c57f9327e51e60dda22d9b63aaad59203bc5996794` | `0; 72` |

### 3.1 Two digest conventions are in use, and one of them silently drifts

This is a control-plane hygiene finding, established mechanically and reported
rather than repaired, since repairing it would rewrite twenty-one bindings that
belong to Tasks 5 through 9.

The `artifact_sha256` values already bound in `claim-ledger.json` for the Task 5
through Task 9 evidence artifacts are digests of the **Git blob**, that is of the
LF-normalized bytes. The source-digest tables inside the Task 10 analysis
artifacts, including the pre-edit table of Section 1 above, are digests of the
**working-tree bytes**, which on this checkout are CRLF because
`core.autocrlf` is `true`. The two conventions coincide only for files whose
working-tree copy already uses LF.

The mechanical consequence: a validator that hashes working-tree bytes and
compares against the bound `artifact_sha256` reports apparent drift on **all
twenty-one** Task 5 through Task 9 evidence rows. Verified here by recomputing each
row three ways — raw working-tree bytes, LF-normalized bytes, and the Git blob —
and confirming that every bound value equals the LF-normalized and Git-blob
digest and none equals the raw working-tree digest. There is no content drift in
any of those artifacts.

The Task 11 provenance correction uses the **committed Git-blob convention**
for every row in the forward table and for the proof digest bound in reverse by
`claim-ledger.json` and `adversarial-report.json`. These are SHA-256 digests of
the LF-normalized bytes returned by `git show REVISION:path`, so the immutable
review revision reproduces them independently of `core.autocrlf`. The source
map and this proof are also normalized to LF before the final snapshot, making
their current working-tree digests equal to their committed-blob digests.
Existing historical Task 5 through Task 9 evidence rows were not reinterpreted
or rewritten.

Recommendation for Task 12 or Task 16: state the digest convention once in the
schema and migrate the remaining historical rows to the committed Git-blob
convention, so a validator never compares a blob digest with platform-specific
working-tree bytes.

## 4. The type table

Fifteen objects, none of which may be identified with another. Rows 1–3 and
12–13 are the ones the pre-integration material either identified or left
untyped; every row now has a notation-appendix entry or an explicit
non-identification list in the source.

| # | Symbol | Kind | Domain to codomain | Determined by | Never identified with |
| --- | --- | --- | --- | --- | --- |
| 1 | `N` | sample kernel | `N: K x Kbar-sigma -> [0,1]`, `N(x, Kbar) = 1` for **every** `x` | modeling declaration | `N_*`, `q`, `Psi`, `R_l` |
| 2 | `N_*` | affine law map | `P(K) -> P(Kbar)` | `N`; not conversely | `N`; `q` off `B` |
| 3 | `q = N_*|_B` | law-fiber map | `B -> Bbar`, exists only under family closure | `N` plus closure; smoothness is a further hypothesis | `N_*` on all of `P(K)` |
| 4 | `P_l` | principal scale map | `P -> Pbar`, smooth, `kappa`-equivariant over `f` | declared; exists iff `P x_kappa Gbar = f^* Pbar` | `f`, `Psi` |
| 5 | `Psi` | associated-bundle morphism | `E -> Ebar` over `f` | `(P_l, kappa, q)` plus the law-fiber intertwining | `N`, `N_*`, `q`, `R_l` |
| 6 | `T^V Psi` | vertical tangent map | `VE -> VEbar` over `Psi`; equals `Tq` only in a frame pair `(u, P_l(u))` | `Psi` | `T Psi`; `q` itself |
| 7 | `D^omega s` | covariant vertical first jet | `T U -> s^* VE` | `(omega, s)` | `Ts`; a coordinate derivative |
| 8 | `A_Psi = D Psi` | horizontal defect (anomaly) | section of `varpi^* T^*C tensor Psi^* VEbar` | `(Psi, omega, omegabar)` | `Delta_F`; a scalar |
| 9 | `Delta_F^Psi` | vertical Fisher defect | section of `Sym^2 V^*E` | `(g^F, gbar^F, T^V Psi)` | `delta_Psi`, its base pullback |
| 10 | `f` | base coarse map | `C -> Cbar`, surjective submersion wherever descent is used | declared | `K_l`, `R_l` |
| 11 | `Psi s = sbar f` | **section relation**, not a map | predicate on `(s, sbar)` | equivalent to fiber constancy | a definition of `sbar` from `s` |
| 12 | `Q_l` | configuration manifold | exhibited tier: `= R^N`; or `L^2(mu; R^K)` | declared `(mu, w, basis, topology)` | the set of all smooth sections |
| 13 | `R_l` (source: `\mathsf R_\ell`) | configuration coarse map | `Q_l -> Q_{l+1}`, smooth | **separately declared** | `K_l`, `R^H`, `R_b`, `M_l`, `C_{l,s}`, `Rhat_l`, `Rwidehat_l`, `Psi`, the root set `R`, the descent ray `R^-` |
| 14 | `G_l` (source: `\mathsf G_\ell`) | configuration metric | section of `Sym^2 T^* Q_l`, **strong** | `(mu, w, g^F, product label or lift)` | `h_s^omega`, `g^F`, `gbar^F` |
| 15 | `S_pi`, `U = R`, `I_b` | score isometry, restriction, extensive lift | `L^2(pi)/R1 -> L^2_0(pi)`; `L^2(pi) -> L^2(pi K)` with norm `<= 1`; `L^2_0(pi) -> L^2_0(pi^b)` with norm `sqrt b` | `pi`; `(pi, K)`; `b` | each other |

**Lemma 4.1 (strictness of rows 1-3, repaired q statement).** `N` determines
`N_*` and hence `q`, and the converse fails; sample-level equivariance of `N`
implies the law-level intertwining, and the converse fails. For fixed principal
map `P` and associated-bundle morphism `Psi`,
`q = iota_{P(u)}^{-1} Psi iota_u` is unique. A target-frame change acts by the
full represented target gauge action, not merely image isotropy; `Psi` never
determines `N`.

<!-- SUPERSEDED historical q-isotropy wording follows; it is explicitly
refuted by the repaired statement above and is not supporting evidence.

**Lemma 4.1 (strictness of rows 1–3).** `N` determines `N_*` and hence `q`, and
the converse fails; sample-level equivariance of `N` implies the law-level
intertwining, and the converse fails; `Psi` determines `q` only up to the
isotropy of the image point and never determines `N`.
-->

*Proof.* For fixed `P`, the displayed formula is an equality defining `q`, hence
gives uniqueness; changing the target frame conjugates it by the represented
target gauge action. For the forward implication, with `B` in the coarse sigma-algebra,
`(N_* rhohat(g) beta)(B) = int N(rho(g)x, B) beta(dx) = int N(x, rhobar(kappa g)^{-1} B) beta(dx) = (rhobarhat(kappa g) N_* beta)(B)`.
Both converses share one witness: sample spaces `R^2` and `R`, `G = SO(2)`
acting by rotation, `Gbar` trivial, and
`B = {N(0, sigma^2 I_2) : sigma > 0}`. The action fixes every point of `B`, so
the law-level relation holds for every kernel whatsoever. The three kernels
`N_1(x, .) = delta_{x_1}`, `N_2(x, .) = delta_{x_2}`, and
`N_3(x, .) = delta_{(x_1+x_2)/sqrt 2}` all send `N(0, sigma^2 I_2)` to
`N(0, sigma^2)`, so `q_1 = q_2 = q_3` while the three kernels are pairwise
distinct, and none is equivariant as a kernel. The last statement is immediate
from `Psi[u, beta] = [P_l(u), q beta]`. `QED`

## 5. The bundle tier, proved

Notation in this section: `u_X = D^omega s X`, `L = T^V Psi`,
`a_X = A_Psi(s(c); X)`, `ubar_X = D^omegabar sbar(T_c f X)`.

### T1. Horizontal defect, sign convention, and type

`eq:pb-coarse-horizontal-defect`. The defect is
`A_Psi(e; X) = ver^omegabar(T_e Psi(H^omega_e X)) = T_e Psi(H^omega_e X) - H^omegabar_{Psi(e)}(T_c f X)`:
**transported fine horizontal lift minus coarse horizontal lift**. It is
vertical because both terms project to `T_c f X`, and the two displayed forms
agree because the `omegabar`-horizontal part of `T Psi(H^omega_e X)` is exactly
`H^omegabar(T_c f X)`. Its type is a section of
`varpi^* T^*C tensor Psi^* VEbar`, and along a section a one-form valued in
`f^* sbar^* VEbar`.

### T2. Exact one-step first jet

`thm:pb-covariant-jet-naturality`, `eq:pb-covariant-jet-chain-rule`. Under the
section relation, `ubar_X = L u_X + a_X`.

*Proof.* Split `T_c s X = H^omega_{s(c)} X + u_X` and apply `T Psi`. The
horizontal summand gives `H^omegabar(T f X) + a_X` by T1, and the vertical
summand gives `L u_X` because a bundle morphism preserves verticality.
Differentiating the section relation gives
`T Psi(T_c s X) = H^omegabar_{sbar(f(c))}(T f X) + ubar_X`, and the horizontal
terms cancel because `Psi(s(c)) = sbar(f(c))`. `QED`

### T3. Exact signed base comparison, with every cross term

`thm:pb-signed-base-comparison`, `eq:pb-signed-base-comparison`. With
`delta_Psi(X,Y) = Delta_F^Psi(u_X, u_Y)`,
`X_Psi(X,Y) = gbar^F(L u_X, a_Y) + gbar^F(a_X, L u_Y)`, and
`Q_Psi(X,Y) = gbar^F(a_X, a_Y)`, **with no compatibility hypothesis of any
kind**,

```
h_s^omega - f^* hbar_sbar^omegabar = delta_Psi - X_Psi - Q_Psi ,
```

where `X_Psi` is symmetric and sign indefinite and `Q_Psi >= 0`. Both retained
tensors enter with a minus sign, and neither may be summarized as one vertical
mismatch term.

*Proof.* `f^* hbar(X,Y) = gbar^F(L u_X + a_X, L u_Y + a_Y) = gbar^F(L u_X, L u_Y) + X_Psi + Q_Psi`
by T2, and `gbar^F(L u_X, L u_Y) = g^F(u_X, u_Y) - Delta_F^Psi(u_X, u_Y)` by
the definition of the vertical defect. Subtract from
`h(X,Y) = g^F(u_X, u_Y)`. `QED`

### T4. Exact signed positivity criterion

`thm:pb-signed-positivity-criterion`, `eq:pb-positivity-criterion`. Assume the
Markov hypotheses of T6 so that `delta_Psi >= 0`. Then at a fixed base point the
following are equivalent: the base comparison is positive semidefinite; the
coarse jet is no longer than the fine jet in the two Fisher norms; and

```
2 gbar^F(L u_X, a_X) + || a_X ||^2_{gbar^F}  <=  delta_Psi(X, X)   for every X.
```

*Proof.* The first two are the identity of T3 read on the diagonal. Expanding
`|| L u_X + a_X ||^2` and substituting
`|| L u_X ||^2_{gbar^F} = || u_X ||^2_{g^F} - delta_Psi(X,X)` gives the
third. `QED`

**Consequence, and the exact repair of the ledger's "only when".** Vanishing of
the horizontal defect is **sufficient** for base positivity, because it makes
the left side vanish while the right side is nonnegative. It is **not
necessary**: whenever `gbar^F(L u_X, a_X)` is negative and large enough in
modulus the criterion holds strictly with `a_X` nonzero. The recomputed table
below (Section 8.2) exhibits three such rows. The triangle-inequality margin
`|| a_X || <= sqrt(h(X,X)) - sqrt(h(X,X) - delta_Psi(X,X))` is likewise
sufficient and not necessary, and is violated at the third row while the
comparison is strictly positive.

Strict negativity is realizable at **zero information loss**: identity kernel,
so `Delta_F^Psi = 0`, constant related sections, source horizontal field `d/dx`,
target `d/dx + a d/dmu` with `a` nonzero. Then `u = 0`, `a_X = -a d/dmu`, and
the comparison is `-a^2 dx^2`, negative definite.

### T5. Isotropy criterion — the definition of connection compatibility

`thm:pb-isotropy-criterion`, `eq:pb-scale-connection-defect`,
`eq:pb-anomaly-fundamental-field`, `eq:pb-isotropy-criterion`. For a morphism
induced by `(P_l, kappa, q)`, define the scale-connection defect form
`A_frak = P_l^* omegabar - d kappa . omega`. Then `A_frak` is horizontal and
`Ad . kappa`-equivariant, hence descends to a one-form on the base valued in
`f^* Ad Pbar`; the horizontal defect is the fundamental vertical field
`A_Psi(e; X) = vartheta_{Psi(e)}(A_frak(X))`; and `A_Psi` vanishes along a
coarse section **iff** `A_frak(X)` lies in the isotropy subalgebra of
`sbar(f(c))` for every `c` and `X`. The principal-level identity `A_frak = 0`
is sufficient, and necessary only under infinitesimal effectiveness. Moreover
`Q_Psi` is the pullback of the positive semidefinite form
`k(xi, eta) = gbar^F(zetabar_xi betabar, zetabar_eta betabar)` whose radical is
exactly that isotropy subalgebra, which is consistent.

*Proof.* Evaluating `P_l^* omegabar` on the fundamental field of `xi` gives
`d kappa xi`, so the difference annihilates vertical vectors; equivariance
follows from `R_g^* P_l^* omegabar = Ad_{kappa(g)^{-1}} P_l^* omegabar`
together with `d kappa . Ad_{g^{-1}} = Ad_{kappa(g)^{-1}} . d kappa`. In
trivializations write `Psi(c, beta) = (f(c), psi_c beta)` with
`psi_c = rhobarhat(varsigma(c)) . q`; using
`H^omega_{(c,beta)} X = (X, -zeta_{A(X)} beta)` and the differentiated
intertwining `Tq . zeta_xi = zetabar_{d kappa xi} . q`, one gets
`A_Psi(X) = zetabar_{a_frak(X)}(psi_c beta)` with
`a_frak = Ad_varsigma(u^* A_frak)`. A fundamental field vanishes at a point
exactly when its generator lies in the isotropy algebra there, and conjugation
moves generator and algebra together. `QED`

This is the sole meaning attached in the manuscript to "the connections are
compatible". The phrase previously occurred at five source sites and was
defined at none; three of those five are inside this pass's permitted scope and
now read the isotropy criterion, and the two outside it are recorded in
Section 10.

### T6. Positive Markov Fisher defect, with its full hypothesis list

`thm:pb-pullback-fisher-defect`, `eq:pb-fisher-defect-positive`,
`eq:pb-pullback-fisher-contraction`. Under (H0) regularity at **both** scales;
(H1) one family-level dominating measure with a fixed jointly measurable
density version; (H2) quadratic-mean differentiability with centered
finite-`L^2` scores; (H3) `N(x, Kbar) = 1` for **every** `x`, not almost every
`x`, since an exceptional set would otherwise be allowed to depend on the
parameter; (H4) the joint law and its reverse conditioning; (H5) family closure
`N_*(B) subset Bbar` with `q` smooth between the declared parametrized-measure
models and a jointly measurable parameter-smooth version selection for the
vertical differential; (H6) a declared equivariant principal scale map with the
law-fiber intertwining; and coarse-scale invariance of `gbar^F` under the
represented action, one has

```
Delta_F^Psi(w, w) = E Var( l_w(X) | Y ) >= 0 ,
```

with equality exactly when the fine score in direction `w` is measurable with
respect to the coarse output; and, adding the isotropy hypothesis (H7),
`h_s^omega - f^* hbar_sbar^omegabar = delta_Psi >= 0`.

*Proof.* Work in a frame pair `(u(c), P_l(u(c)))` where `T^V Psi = Tq`; this is
where coarse-scale invariance of `gbar^F` is consumed, since in any other frame
pair the local representative carries the context-dependent factor
`rhobarhat(varsigma(c))`. The DQM transfer is source-closed by
`evidence/task-10-dqm-transfer-source-map.md`: form
`J_theta(dx,dy) = P_theta(dx) N(x,dy)` and
`nu(dx,dy) = mu(dx) N(x,dy)`, so `dJ_theta/dnu = p_theta(x)`. The fine DQM
remainder therefore has the same squared `L^2(nu)` norm, and the preservation
theorem in Section 3 of Pollard (2013), applied to the statistic `(x,y) -> y`, gives the score
`E[l_w(X) | Y]`. Hellinger contraction is corroboration only, not a sufficient
substitute for this score identification. The law of total variance gives the
displayed identity, and pulling back by `D^omega s` preserves positive
semidefiniteness. The base statement is T3 with `X_Psi = Q_Psi = 0`. `QED`

The guard is not droppable silently, and what survives when it is dropped is
stated exactly in the source: the vertical conclusion is unchanged, and the
base conclusion is replaced by T3 together with the criterion of T4.

### T7. Ordered composition of horizontal defects

`thm:pb-anomaly-composition`, `eq:pb-anomaly-composition`. For composable
morphisms,

```
A_{Psi_02}(e; X) = T^V Psi_12 |_{Psi_01(e)} ( A_{Psi_01}(e; X) )
                 + A_{Psi_12}( Psi_01(e) ; T_c f_01 X ) ,
```

with connection-level form
`A_frak_02 = P_01^* A_frak_12 + d kappa_12 . A_frak_01`.

*Proof.* Expand `T Psi_01(H^{omega_0}_e X)` by T1, apply `T Psi_12`, use T1
again at the second stage on the horizontal summand and verticality
preservation on the vertical summand, and subtract the composite horizontal
lift. `QED`

**Order is not cosmetic.** `A_01` takes values in `V Ebar_1` and `A_12` in
`V E_2`, so an unweighted sum is a type error before any question of
correctness arises. The exact vanishing condition is
`T^V Psi_12(A_01(e;X)) = -A_12(Psi_01(e); T f_01 X)`. Factorwise vanishing on
the indicated domains is sufficient, not necessary. Recomputed instance
(Section 8.3): with `f_01(x) = 2x`, `f_12(y) = 3y`, translation group, and local
connection forms `0`, `a_1 dy`, `a_2 dz`, the law reads
`2 a_1 + 2(3 a_2 - a_1) = 6 a_2` identically. Thus `a_2 = 0`, `a_1 != 0` has
two nonzero factor defects which cancel, while dropping the base pushforward
gives `a_1 + 3 a_2` and fails. The factorwise-necessity statement in the
historical search inputs is refuted and is not supporting evidence for T7.

### T8. Vertical cocycle (unconditional) and the corrected sharp base cocycle

`thm:pb-fisher-defect-cocycle`, `eq:pb-fisher-defect-cocycle`;
`thm:pb-base-defect-cocycle`, `eq:pb-base-cocycle-residual-a` through
`eq:pb-base-cocycle-criterion`.

The vertical identity
`Delta_F^{Psi_12 . Psi_01} = Delta_F^{Psi_01} + (T^V Psi_01)^* Delta_F^{Psi_12}`
holds unconditionally, by adding and subtracting `(T^V Psi_01)^* g_1^F`. It
uses neither the connections nor any section.

Its base pullback does **not** telescope. With `delta_{jk}` the three base
defects, `v_X = T^V Psi_01(u_X)`, `A_X` the stage-one anomaly along the
section, and `ubar_X = v_X + A_X`, the residual
`Nres = delta_02 - delta_01 - f_01^* delta_12` has the three equivalent exact
forms

```
(a)  Nres(X,Y) = Delta_12(v_X, v_Y) - Delta_12(ubar_X, ubar_Y)
(b)            = -[ Delta_12(ubar_X, A_Y) + Delta_12(A_X, ubar_Y) ] + Delta_12(A_X, A_Y)
(c)            = -[ Delta_12(v_X,    A_Y) + Delta_12(A_X, v_Y)    ] - Delta_12(A_X, A_Y) .
```

The sign of the quadratic term is coupled to the choice of argument in the
cross terms. A mixed convention — pushed fine jet in the cross slots with a
plus sign on the quadratic term — exceeds the true residual by exactly
`2 Delta_12(A, A)`, two copies of the second-arrow vertical defect evaluated on
the first-arrow anomaly. The sharp cocycle holds **iff**

```
Delta_12(v_X,v_X) = Delta_12(ubar_X,ubar_X)
```

for every `X`, equivalently `Delta_12(A_X, 2 v_X + A_X) = 0`. This is a
quadratic-form equality without a Markov hypothesis; it may be called equality
of `Delta_12` seminorms only when the second arrow is Markov and hence
`Delta_12` is positive semidefinite.

*Proof.* Apply `(D^{omega_0} s_0)^*` to the vertical cocycle, note that
`f_01^* delta_12(X,Y) = Delta_12(ubar_X, ubar_Y)` by definition, and subtract to
get (a). Substituting `ubar = v + A` in the second term gives (c) and
substituting `v = ubar - A` in the first gives (b). Symmetry of `Nres` makes
vanishing on the diagonal equivalent to vanishing. `QED`

**Sufficient conditions, in decreasing strength, none necessary.** (S1) the
stage-one anomaly vanishes, which by T5 is the isotropy criterion at the first
arrow; (S2) the second arrow is Fisher lossless; (S3) the stage-one anomaly
lies in the radical of `Delta_12`, which suffices because `Nres` is linear in
the product `Delta_12 A`. Non-necessity is exhibited by the recomputed instance
of Section 8.4, where the residual is `-(2/3) a_1(a_1 + 1)`, vanishing at
`a_1 = -1` with anomaly `-2`.

**Two hypotheses, not one.** The sharp cocycle needs only the stage-one
criterion. Reading the middle term `delta_12` as the stage-two information loss
`h_1 - f_12^* h_2` requires in addition that the stage-two horizontal defect
vanish, by T3 applied at the second arrow. Only under both is the identity an
additive decomposition of information loss on the base. The source now states
these separately.

### T9. Sharp projectability, with smoothness proved

`thm:pb-section-descent`, `eq:pb-projectability-criterion`;
`prop:pb-nonfunctorial-descent`. For a surjective smooth submersion `f`,
smooth `Psi` over `f`, and a fine section `Q`: (P1) a coarse section `Qbar` with
`Psi Q = Qbar f` exists; (P2) `Psi Q` is constant on each fiber of `f`; (P3)
`T^V Psi(D^omega Q(X)) + A_Psi(Q(c); X) = 0` for every `X` in `ker T_c f`. Then
(P1) and (P2) are equivalent, both imply (P3), and (P3) implies (P2) under
connected fibers. Under (P2) the descended section is unique, **automatically
smooth**, and automatically a section.

*Proof.* A surjective smooth submersion is a smooth quotient map, so a smooth
map constant on its fibers descends uniquely and smoothly; smoothness is
therefore a theorem, not an obligation. For (P2) implies (P3), split
`T_c Q X = H^omega_{Q(c)} X + D^omega Q(X)`, apply `T Psi`, and use
`T_c f X = 0` to annihilate the coarse horizontal lift; constancy forces the
remainder to vanish. The converse under connected fibers is that a smooth map
with vanishing derivative along a connected embedded submanifold is constant on
it. `QED`

The submersion hypothesis is load bearing: with `f(x) = x^3`, a smooth bijection
that fails to be a submersion at the origin, the unique descent of
`Q(x) = N(x, 1)` is `Qbar(y) = N(y^{1/3}, 1)`, continuous and not differentiable
at zero.

A pointwise bundle morphism therefore induces only a **partial** map on
configurations. Whenever `ker T_{c_0} f` is nonzero, some vertical direction
there is not annihilated by `T^V Psi`, and a **given global smooth section**
passes through the chosen `e_0`, the projectable set is a proper subset. Choose
the bump function supported inside that section's trivializing chart and keep
the perturbed section equal to the given global section off the support; its
derivative at zero is `d_1 chi(c_0) . T^V Psi(w)`, nonzero by construction. The
witness is the total
collapse of the circle to a point with `Q(x) = N(sin x, 1)`, where the
descendable set in the `L^2` tier is exactly the constants: closed, of infinite
codimension, with empty interior. **This is scoped to a collapsing base map**;
if `f` is a diffeomorphism every section descends, so the unscoped claim that a
bundle morphism induces a configuration map nowhere is false and is not carried.

## 6. The configuration tier, constructed

### T10. An exhibited finite-dimensional tier with a strong Gram metric

`def:hist-finite-configuration-tier`, `thm:hist-finite-tier-regularity`,
`eq:hist-configuration-gram`. Declare a compact base with a finite positive
Borel measure, a trivial bundle with translation group acting on the mean and a
flat connection, the fixed-covariance normal fiber, smooth basis fields
a two-sidedly bounded positive weight, and smooth basis fields
`phi_1 ... phi_N` declared linearly independent in
`L^2(w mu; Sigma_0^{-1})` whose span contains every constant mean field,

```
Q_l = { s_xi : xi in R^N },   s_xi(c) = N( sum_a xi_a phi_a(c), Sigma_0 ) ,
G_l(V, V) = int w(c) g^F( d_V s_xi(c), d_V s_xi(c) ) dmu(c) ,
```

labeled as a **weighted product of marginal fiber metrics**, not as a joint-law
pullback. Then `Q_l` is a nonempty smooth manifold diffeomorphic to `R^N`; the
metric is the constant Gram form
`Phi_ab = int phi_a^T Sigma_0^{-1} phi_b w dmu`, independent of `xi`, smooth,
finite, and positive definite by the declared independence; any Riemannian metric in finite dimensions is
automatically **strong**; every `C^1` functional has a unique gradient and every
`C^2` objective a locally Lipschitz natural-gradient field with locally unique
integral curves. The constant-field inclusion defines the unique coefficient
map `L_l: R^K -> R^N`, so mean translations act affinely by
`Theta_g^l(xi) = xi + L_l g`; their orbit tangent is the linear subspace
`L_l(R^K)`, hence closed and complemented, so the quotient-speed infimum is
attained.

*Proof.* The tangent `d_V s_xi(c) = sum_a v_a phi_a(c)` does not depend on
`xi`, so the integrand is the quadratic form `v^T Phi v`; finiteness is
compactness plus boundedness of the weight; `v^T Phi v = 0` forces
`sum_a v_a phi_a = 0` in the weighted space because the weight is positive and
the fiber form positive definite; strongness in finite dimensions is the
statement that every inner product induces the norm topology and its musical
map is a linear isomorphism. `QED`

Nondegeneracy is a **rank test checkable in advance**: with an `M`-atom design
the Gram matrix has rank at most `M K`, so `N > M K` forces degeneracy and the
natural-gradient equation then has no solution or many. Executed instance
(Section 8.5): on the circle with `K = 1`, unit weight, normalized arclength,
and basis `{1, cos, sin}`, one has `Phi = diag(1, 1/2, 1/2)`, determinant
`1/4`, eigenvalues `{1, 1/2}`, positive definite.

### T11. The infinite-dimensional strong/weak boundary, retained

Two options and no third. On `L^2(mu; R^K)` with the weighted metric, two-sided
bounds on the weight and on the fiber Fisher form give
`w_- lambda_- ||V||^2 <= G(V,V) <= w_+ lambda_+ ||V||^2`, so the musical map is
a topological isomorphism and the metric is **strong**, at the cost of requiring
the objective to be `C^1` on `L^2`, which excludes gradient-energy functionals;
either bound failing alone destroys the conclusion. On a Sobolev tier with the
same integrated metric the topology is strictly coarser, the musical map is
injective and bounded but not surjective, and the metric is **weak**. The
failure is realized: on the circle with `Q = H^1`, `F(Q) = (1/2) int |Q'|^2`,
and `Q = sum_k k^{-2} sin(k theta)`, the `H^1` norm is finite while a gradient
would be `-Q'' = sum_k sin(k theta)` with infinite `L^2` norm, so no
natural-gradient field exists there. The exact missing ingredient is Riesz
representability of the differential.

In the strong Hilbert tier the decisive gauge-quotient condition is
**closedness** of the orbit tangent; complementedness is then automatic because
each tangent space is Hilbertable, and the pair of conditions bites only in the
weak or Banach tier. The available failure witness is free and isometric with a
dense orbit tangent, so the quotient speed vanishes identically; it does not
settle the properness question, which is recorded as open rather than claimed.

### T12. Exact averaging defect, and the retirement of generic contraction

`thm:hist-averaging-defect`, `hyp:hist-joint-convexity`,
`eq:hist-averaging-defect`, `eq:hist-averaging-three-term`. For the declared
averaging map `(R_l s)(cbar) = int_{f^{-1}(cbar)} Psi(s(c)) kappa_cbar(dc)`,
under measurability and disintegration hypotheses, convexity of the coarse fiber
with a linear structure-group action and an affine fiberwise `Psi` with linear
part `L`, chart joint convexity (JC), the fiberwise contraction
`Delta_F^Psi >= 0`, and the weight condition `wbar . f <= w`, the defect
`Delta_avg(Z)` is nonnegative. Under the stronger (JC-const) it is exactly

```
Delta_avg(Z) = int w Delta_F^Psi(Z,Z) dmu                      [channel loss]
             + int (w - wbar.f) (L^* gbar^F)(Z,Z) dmu          [weight gap]
             + int wbar Var^{gbar^F}_{kappa_cbar}( L Z ) dmubar [context gap]
```

with all three terms separately nonnegative.

*Proof.* Affineness makes the coarse pair the `kappa_cbar`-barycenter of the
fine pair. Jensen under (JC) bounds the coarse integrand by the barycenter of
the fine integrands; multiplying by `wbar`, integrating, and disintegrating
converts the bound into `int (wbar . f)(L^* gbar^F)(Z,Z) dmu`, after which the
weight condition and the fiberwise contraction give nonnegativity. Under
(JC-const) the Jensen step is an equality minus the variance term, and expanding
`g^F = Delta_F^Psi + L^* gbar^F` separates channel from weight. `QED`

**(JC) is not decorative and generic averaging is retired.** With two contexts,
uniform disintegration, unit weights, an identity fiber map so the channel loss
is exactly zero, and the centered normal fiber in the moment chart, the
configuration `(1, delta)` with tangent `(1, 0)` gives fine energy `1/4` and
coarse energy `1/(2(1+delta)^2)`, a ratio of `2/(1+delta)^2` that equals
`20000/10201 = 1.9605920988...` at `delta = 10^{-2}` and tends to the block size
`2`. The defect is negative exactly for `delta < sqrt 2 - 1` and tends to
`-1/4`. Every other hypothesis holds on this datum, including base-measure
matching. Only (JC) fails, and exactly so: the Hessian of `A^2/(2 Sigma^2)` has
determinant `-A^2 Sigma^{-6} < 0` for nonzero `A`, whereas the law-chart
integrand `pdot^2/p` has Hessian determinant `0` and trace
`2/p + 2 pdot^2/p^3 > 0` and is jointly convex. Accordingly no contraction
theorem is attached to an averaging or variational coarse map anywhere in the
source without (JC) or the weight-dominated hypothesis.

### T13. The coarse configuration map: symbol, smoothness, equivariance, compatibility

`sec:hist-configuration-coarse-map`, `eq:hist-configuration-coarse-map`;
`prop:hist-coarse-map-smoothness`, `eq:hist-coarse-map-compatibility`. The map
is written `\mathsf R_\ell` and is separately declared. At the exhibited tier,
if the fiberwise average of each fine basis field lies in the coarse span with
constant matrix `E`, then `R_l(xi) = E xi` is **linear, hence smooth**, with
tangent map `E` everywhere. The declared fine and coarse basis spans contain
the constants, with their unique coefficient maps `L_l` and `L_{l+1}`; gauge
equivariance for the affine translation actions is exactly
`E L_l = L_{l+1}`. Its metric compatibility is the matrix inequality
`E^T Phibar E <= Phi`, with `E` the constant coefficient matrix written
`\mathsf E` in the source, which is
exactly `R_l^* G_{l+1} <= G_l` and is implied by T12. Compatibility is carried
as an explicit hypothesis discharged by T12, never as a corollary of a fiberwise
contraction theorem.

**Symbol decision, against two prior recommendations.** Both the score route and
the adversarial pass recommended renaming the configuration coarse map to
`\widehat R_\ell`. That symbol is **already taken**:
`07b_agent_network_rg.tex:2196` defines it as the reference-space-conjugated
retained projection, recurring at `07b:2198, 2227, 2251`. Adopting the
recommendation would replace one collision with another. Verified by direct
search on the current bytes: `\mathsf{R}`, `\mathfrak{r}`, `\mathfrak{q}`, and
`\mathsf{C}` occur **zero** times in `manuscripts/gauge_vfe_rg/*.tex`. The
adopted symbol is `\mathsf R_\ell`, and the notation appendix now carries a row
typing it with its full non-identification list.

### T14. Cross-scale declaration compatibility

`eq:pb-cross-scale-declarations`, `eq:pb-two-channel-comparison`. Any comparison
of **integrated** configuration metrics across scales consumes two further
declarations, and neither follows from any fiberwise contraction theorem:
(X1) `f_# mu = mubar`, and (X2) `wbar_x . f <= w_x` for both channels. The
two-channel difference is
`sum_x [ w_x (h_x - f^* hbar_x) + (w_x - wbar_x . f) f^* hbar_x ]`, which fails
positivity as soon as `wbar_x . f > w_x` in some channel, even at zero anomaly with
genuine Markov channels. Failure of (X1) reverses the comparison outright: on
the disjoint union of two copies of the line with the identity base map, a
tensor vanishing on the first copy and equal to `dx^2` on the second, and point
masses on different copies, the fine integrated tensor is `0` and the coarse one
is `1` with vanishing fiberwise defect. The witness must be typed on a
positive-dimensional base; a two-point discrete set is a zero-manifold on which
no tangent direction exists.

## 7. The history tier, typed and proved

### T15. Typed curves without imposed time

`def:hist-curve-types`. The primary labels are **pointwise**: stationary,
vertical, horizontal, mixed. These four partition every parameter value. The
interval labels are obtained by quantification and are therefore **not
exhaustive**, since a curve may change pointwise type. Every downstream use is
on a subinterval of one fixed pointwise type, so nothing downstream changes.
Verticality is connection free; horizontality and the mixed decomposition are
connection relative. A base curve carries neither predicate, and a configuration
curve does not live in the total space at all — verticality statements about it
are statements about its adjoint evaluation at a fixed context, by
`eq:hist-pointwise-history-verticality`. For a constant base probe, the
diagonal curve is vertical only when the remaining vertical velocity is
nonzero; it is stationary when that velocity vanishes. Applying a verticality predicate to a
base curve or to a configuration curve is a type error. The contextual base is
fixed and timeless throughout.

### T16. Oriented semiconjugacy, regularity, and maximal intervals

`def:hist-oriented-semiconjugacy`, `lem:hist-semiconjugacy-factor`,
`thm:hist-oriented-semiconjugacy`. The condition is
`T_Q R_l X_l(Q) = a_l(Q) X_{l+1}(R_l Q)` with `a_l` continuous and strictly
positive. Off the coarse critical set the factor is **determined and as regular
as the data**, by pairing with `X_{l+1}(R_l Q)` and dividing; on the coarse
critical set the condition forces `T_Q R_l X_l(Q) = 0` and every positive number
satisfies it, so `a_l > 0` is vacuous there. Continuity is therefore a
consequence, not an extra assumption, and "noncritical" must name its field: the
load-bearing reading is `X_{l+1} != 0` on the image.

Given the condition on an open set with `X_{l+1}` locally Lipschitz, the
coarse-flow-parameter reparameterization `sigma_Q(t) = int_0^t a_l(Phi_s Q) ds` is a strictly increasing `C^1`
diffeomorphism onto an open interval, and

```
Sigma_Q  subset  Jbar^max ,      R_l(Phi_t(Q)) = Phibar_{sigma_Q(t)}(R_l Q) .
```

*Proof, in the order that matters.* Put `c(t) = R_l(Phi_t Q)`, so
`cdot = a_l(Phi_t Q) X_{l+1}(c)`. Build `d = c . sigma_Q^{-1}` on `Sigma_Q`
first and check `d'(u) = X_{l+1}(d(u))`; then the maximal integral curve through
`R_l Q` contains `d` by local Lipschitz continuity, which yields both the domain
inclusion and the flow identity. Assuming instead that `Phibar_{sigma_Q(t)}` is
defined presupposes what must be proved. `QED`

Completeness does not transfer without `inf a_l > 0`: with `X_l = d/dx`,
`X_{l+1} = d/dy`, and `R_l = arctan`, the factor `(1+x^2)^{-1}` is positive,
both flows are complete, and `Sigma_0 = (-pi/2, pi/2)` is proper. Positivity
carries the entire orientation content: with `F_l = x^2/2`,
`F_{l+1} = -y^2/2`, and `R_l(x) = -x`, the orbit sets agree, `a = -1`, and
descent becomes ascent.

**Converse.** Differentiating a flow semiconjugacy of the displayed form at
`t = 0` returns the vector-field condition. Thus `a_l = d sigma / dr` is unique
off the coarse critical set, but is not determined where `X_{l+1}=0`.

### T17. Noncollapse

`prop:hist-noncollapse`. The condition alone permits total collapse: a constant
coarse map with a zero coarse field satisfies it for every positive factor while
sending every nonconstant fine orbit to a point and every coarse duration to
zero. A nonconstant shared oriented history therefore additionally requires
`T_Q R_l X_l(Q) != 0` on every nontrivial subarc, together with the
maximal-interval condition, upgraded to equality only under completeness and a
positive infimum of the factor. The refutation is scope matched: it refutes
"positive semiconjugacy implies a nonconstant shared history", not the flow
identity.

### T18. The factor cancels from duration; the exact comparison criterion

`thm:hist-duration-relation`, `eq:hist-image-speed`, `eq:hist-coarse-duration`;
`thm:hist-duration-criterion`, `eq:hist-duration-criterion`. Under the
condition, the image speed is `a_l` times the coarse speed at the image point,
and the accumulated coarse duration over an orbit arc equals the intrinsic
coarse arc length of the image arc, **independently of `a_l`**: the factor in
the integrand cancels exactly against the Jacobian of the substitution
`u = sigma_Q(s)`. The factor `a_l = d sigma/dr` is the coarse-flow-parameter
rate relative to the chosen fine orbit parameter, not a physical-time or
<!-- REFUTED historical prose: the following leftover wording treated a negative
factor as incompatible with ordinary arc length.
absolute value. Calling `a_l` a rate is therefore a category error — it is a
reparameterization datum, invisible to duration, and precisely the object that
must not appear in a final arc length.
-->
For an unoriented relation with negative factor, ordinary arc length uses
`|a_l|` and is unchanged by orientation reversal; positivity is the additional
orientation choice. Metric dilation, not `a_l`, controls length.

The comparison criteria are necessary and sufficient and are **scalar**, in the
single direction `X_l` along the orbit: equality of durations iff the two speeds
agree almost everywhere; a constant ratio iff the same with that factor; and
nonincreasing increments iff
`|| T R_l X_l ||_{G_{l+1}} <= || X_l ||_{G_l}` pointwise. The tensorial Loewner
condition `R_l^* G_{l+1} <= G_l` is **sufficient and strictly stronger**, and is
what T12 and T13 deliver.

**Duration equality does not follow from fiberwise Markov contraction**, and
two logically independent mechanisms show it. First, the two configuration
metrics are separately declared data: with the identity map, identical fields,
no collapse, and metrics `dx^2` and `4 dx^2`, the coarse duration doubles. The
one-context identity-fiber/weight realization has zero information loss; the
separate identity-parameter map `N(mu,1) -> N(mu,1/4)` is a non-Markov
Fisher-increase witness with `Delta = -3`. Second,
a contraction theorem compares the **image** of the fine orbit, never an
independently recomputed coarse orbit: with the identity map and an identity
fiber map, `F_l = (x^2+y^2)/2` and `F_{l+1} = (x^2+4y^2)/2` give a fine history
of length `sqrt 2` and an independently recomputed coarse history of length
about `1.60023`, strictly greater, and the semiconjugacy condition itself fails
there. Neither mechanism implies the other.

**When the fiberwise contraction does lift.**
`thm:hist-pointwise-contraction-lift`. If the two scales share the base and the
base measure and channel weights, if the coarse configuration map acts
pointwise by a normalized parameter-independent Markov pushforward, if both
configuration metrics are the corresponding weighted integrals of the fiber
Fisher metrics, and if all integrals are finite, then the difference of squared
speeds is the weighted integral of the fiberwise defects, hence nonnegative,
with equality exactly on the fine-score measurability condition. This is the
shared-base case; T12 is an alternative sufficient extension admitting a
**collapsing** base map, which is what a renormalization step performs. It adds
affine-fiber, convexity, and barycenter hypotheses, so no general
logical-strength comparison with the shared-base result is asserted. Its Markov hypothesis
excludes the manuscript's own Galerkin aggregation, which is a restriction and
not a pushforward, larger in the Loewner order by a positive semidefinite Schur
term; its shared-metric hypothesis is exactly what the metric-declaration
witness violates.

### T19. Natural-gradient sufficiency, stated as sufficiency

`hyp:hist-functional-compatibility`,
`prop:hist-natural-gradient-sufficiency`,
`eq:hist-conformal-semiconjugacy-factor`. Nothing here is automatic. Equality of
objectives does **not** intertwine natural gradients: the differential is metric
free and the gradient is not, and with the identity map, one objective
`(x^2 + 2y^2)/2`, and metrics `diag(1,1)` and `diag(1, kappa)`, the condition
would force `a = 1` and then `kappa = 1`, so it fails on a dense open set.

Under functional compatibility `F_l = chi_l . F_{l+1} . R_l` with `chi_l' > 0`
on an open set containing the orbit, and with `R_l` a surjective submersion
with closed orbit-tangent splitting: if `R_l` is a Riemannian submersion the
condition holds with `a_l = chi_l'`; if `R_l` is horizontally conformal with
dilation `varphi_l > 0` it holds with `a_l = chi_l' varphi_l^2 > 0`.

*Proof.* Functional compatibility puts the fine gradient in the horizontal
distribution. For horizontal `Z`, horizontal conformality and the chain rule
give
`G_{l+1}(T R_l u, T R_l Z) = varphi_l^2 chi_l' G_{l+1}(w, T R_l Z)` with `w`
the coarse gradient at the image; surjectivity of `T R_l` on the horizontal
distribution and nondegeneracy give `T R_l u = varphi_l^2 chi_l' w`. `QED`

Sanity check and nonempty model: on Euclidean `R` with `R_l(x) = lambda x`, the
proposition predicts `a_l = lambda^2`, matching the direct computation; and on
the exhibited tier with `R_l` the identity and `G_{l+1} = (1/2) G_l`, it
predicts `a_l = 1/2`, which the direct computation returns, with speed ratio
`1/sqrt 2` and both flows complete.

**Where the manuscript's own maps stand, exactly.** Under the pointwise Markov
hypotheses, horizontal conformality at the declared configuration tier is
necessary and sufficient exactly when
`int sum_x w_x Delta_F^{Psi_c}(Z_x(c),W_x(c)) dmu(c) =
(1-varphi_l^2) G_l(Z,W)` for every pair of declared horizontal tangents. This
integrated Gram identity does not imply its pointwise analogue in a finite
span: at two equal-weight contexts, fine `N(mu,1)` fibers and independent
Gaussian-noise kernels of variances `3` and `1/3` give pulled-back location
Fishers `1/4` and `3/4`, respectively. The shared constant tangent has
integrated ratio `varphi_l^2=1/2`, but no common pointwise ratio. A pointwise
converse requires a declared tangent module closed under compactly supported
localization together with a full-support base measure. For the exact-contraction coarse objective, functional
compatibility with `chi_l` the identity holds exactly on the attaining set and
nowhere else, so its differential consequence needs the orbit to lie in the
interior of that set. A structured sufficient route to semiconjugacy is:
exhibit `chi_l` and an open set on which functional compatibility holds; for the
exact-contraction objective prove the orbit lies in the interior of the
attaining set; then verify horizontal conformality of the declared `R_l`. This
route is not asserted necessary or minimal, and it does not establish
semiconjugacy for the manuscript's own maps. It is stated in objects the
manuscript already declares and is satisfiable in the exhibited tier. It is
carried as `OPEN` at
`prop:hist-natural-gradient-sufficiency` and in the obligation appendix.

### T20. Typed non-identification of depth, orbit parameter, and duration

`prop:hist-coordinate-independence`. Scale depth `l`, a chosen oriented orbit
parameter `r`, and Fisher duration `tau^(l)` are distinct typed quantities.
After metric, origin, orientation, and parameterized path are chosen, `tau` can
be a function of `r`; therefore the former "pairwise independent/no two
determine the third" claim is refuted. There is instead no canonical duration
from an unparameterized orbit or scale depth: scaling the metric by `rho^2`
scales duration by `rho`, and origin or orientation choices change the
parameterized representation. The duration is not physical time. Strict
monotonicity is not regularity: with `h_s = 4x^2 dx^2` one gets `tau(r) = r^2`,
whose inverse is not differentiable at the origin, while a zero-speed
subinterval destroys strict monotonicity. A regional clock potential requires a
closed clock one-form with vanishing periods, and for `F = xy` the normalized
descent one-form has `d alpha_F = (x^2 - y^2)(x^2 + y^2)^{-3/2} dx wedge dy`,
vanishing only on the diagonal and hence on no open set.

### T21. Score and action tiers, with the corrected witness

`prop:rg-action-score-isometry` and the material now following it. On the
bounded action quotient the score map is a Fisher isometry onto the bounded
centered subspace whose Fisher completion is `L^2_0`; the centering square
commutes; and the restriction of the conditional-expectation operator to the
centered subspace **is** the score pushforward operator, so the scalar `L^2`
defect on the action quotient is exactly the Fisher information loss
`E Var(h(X) | Z) >= 0`.

Two separations are now fenced with correct witnesses. Every class in the Fisher
completion is realized two-sided by the **quadratic** path of
`lem:rg-dqm-realization`, not by the exponential-action path. The witness
separating the two must diverge on **both** sides: for the odd Hermite
`He_3 = x^3 - 3x`, which lies in `L^2_0` with second moment `6`, the normalizer
`N_3(t)` is infinite for **every** nonzero `t`, because the log integrand
behaves like `t |x|^3` and diverges on one tail for each sign. The degree-two
direction `-x^2` is **not** such a witness and is now explicitly excluded in
both the source and the register: its normalizer `(1 - 2t)^{-1/2}` is finite on
the two-sided interval `(-1/2, 1/2)`, with values `sqrt 6 / 3` at `t = -1/4` and
`sqrt 2` at `t = 1/4`.

Second, the extensive replication lift has norm `sqrt b > 1` and is **not** a
channel. No parameter-independent normalized Markov kernel realizes `b`-fold
replication for `b >= 2`, since the conditional-variance defect would force
`b <= 1`. The replication pair may therefore not be cited as a
Markov-contraction counterexample; the factor `sqrt b` belongs to the reference
identification and to a declared configuration-metric normalization, and to
nothing else.

## 8. Executed verification record

Exact symbolic and rational arithmetic with SymPy 1.14.0 on CPython, run inside
this pass before the corresponding source text was written. **Agreement
corroborates arithmetic and closes no theorem.** No block created or modified a
repository file. Nothing in Sections 4 through 7 rests on a numerical value;
the single quadrature-adjacent statement (the length `1.60023`) separates two
quantities that the symbolic argument already separates.

**8.1 Base-cocycle residual, type level.** With `D` a symbolic symmetric
three-by-three form standing for `Delta_12`, and `V`, `A` symbolic three-by-two
matrices on a two-dimensional fine base, all as identities of two-by-two
symbolic matrices:

```
D symmetric                                                : True
Nres == form (b)  (coarse jet in cross slots, + quadratic) : True
Nres == form (c)  (fine  jet in cross slots, - quadratic)  : True
Nres == mixed convention (fine jet, + quadratic)           : False
mixed - Nres == 2 A^T D A                                  : True
Nres(X,X) == -<A_X, 2 v_X + A_X>_D                         : True
Nres(X,X) == -<A_X, 2 ubar_X - A_X>_D                      : True
Nres == V^T D V - (V+A)^T D (V+A)                          : True
S1 (A = 0) : True   S2 (D = 0) : True   S3 (D A = 0) : True
Nres == -(V^T DA + (DA)^T V) - A^T DA   (linear in D A)    : True
```

**8.2 Signed comparison and positivity criterion, exact rational.** Fine fiber
`N(mu,1)` with `g^F = 1`, kernel `N(x,.) = N(x,1)` so `gbar^F = 1/2` and
`Delta_F = 1/2`, identity base map, section slope `m = 1`, anomaly `b`:

```
identity  h - f^*hbar == delta - [ 2 gbar(v,a) + |a|^2 ]  : True (identically in m, b)
    b     h - f^*hbar    criterion LHS   delta   met    positive
    0          1/2               0        1/2   True     True
  1/10       79/200          21/200       1/2   True     True
 -1/10      119/200         -19/200       1/2   True     True
   1/2         -1/8             5/8       1/2  False    False
 -3/5        23/25          -21/50        1/2   True     True
margin = 1 - sqrt(2)/2 = 0.2928932 ; ||a|| at b=-3/5 = 3 sqrt(2)/10 = 0.4242641
   -> margin violated while the comparison is +23/25 > 0 : margin is not necessary
strict negativity witness (identity kernel, u = 0, anomaly -a) : h - f^*hbar = -a^2 dx^2
```

**8.3 Ordered composition.** Base maps `2x` and `3y`, connection forms `0`,
`a_1 dy`, `a_2 dz`, identity fiber maps:

```
A01 = 2 a1     A12(T f01 X) = -2 a1 + 6 a2     A02 = 6 a2
ordered law A02 == T^V Psi12(A01) + A12(image; pushed vector) : True
wrong variant, base pushforward dropped : a1 + 3 a2  -> differs : True
```

**8.4 Three-level base cocycle, exact rational.** Fibers of variance `1, 2, 3`;
sections `x`, `y/2`, `z/6`:

```
vertical cocycle  D02 == D01 + (T^V)^* D12 : True
residual  Nres(X,X) = -2 a1 (a1 + 1) / 3
mixed convention        = +2 a1 (a1 - 1) / 3
mixed - Nres == 2 D12 A^2 : True
at a1 = 1/10 : true = -11/150 , mixed = -3/50
zero set of the residual : { -1, 0 }
at a1 = -1 : v = 1, ubar = -1, equal Delta-seminorm : True, with anomaly A = -2 != 0
```

**8.5 Exhibited tier, exact.**

```
Gram Phi = diag(1, 1/2, 1/2) ,  det = 1/4 ,  eigenvalues {1, 1/2} , positive definite : True
R^* G_{l+1} = (1/2) Phi  <=  Phi = G_l   (Loewner) : True
semiconjugacy  T R X_l = a X_{l+1} with a = 1/2   : True
nu_img / nu_l = sqrt(2)/2   (strict contraction)
```

Collapsing variant, exact split:

```
G_l - R^* G_{l+1} = diag(1/2, 1/2, 1/2) , positive definite : True
channel term      = diag(1/2, 1/4, 1/4)
Jensen  term      = diag(0,   1/4, 1/4)
channel + Jensen == G_l - R^* G_{l+1} : True
independent Jensen check: Var_kappa(Z) = (v1^2 + v2^2)/2 ; wbar gbar Var = (v1^2 + v2^2)/4
   equals the Jensen quadratic form : True
```

**8.6 Averaging defect, symbolic three-term identity.** Constant coarse fiber
metric, three fine contexts with disintegration weights summing to one,
symbolic linear part, weights, and tangents:

```
Davg == channel loss + weight gap + coarse-metric context variance : True
  channel  >= 0 iff Delta_F^Psi >= 0
  weight   >= 0 iff wbar . f <= w
  variance >= 0 iff gbar >= 0
```

**8.7 Joint convexity and the averaging witness, exact.**

```
moment chart F(Sigma, A) = A^2 / (2 Sigma^2)
   Hessian = [[1/Sigma^2, -2A/Sigma^3], [-2A/Sigma^3, 3A^2/Sigma^4]] , det = -A^2 / Sigma^6
law chart    G(p, pdot) = pdot^2 / p
   Hessian det = 0 , trace = 2/p + 2 pdot^2 / p^3  -> jointly convex
fine = 1/4 ; coarse = 1/(2(1+delta)^2) ; ratio = 2/(1+delta)^2
ratio at delta = 1/100 : 20000/10201 = 1.9605920988138419 ; limit = 2
Delta_avg = 1/4 - 1/(2(1+delta)^2) , limit -> -1/4 , negative exactly for delta < sqrt(2)-1
```

**Two corrections against prior Task 10 artifacts, decided by recomputation and
not by preference.** The interface-reconciliation artifact prints the exact
ratio as `5000/10201` beside the correct decimal `1.9605921`; the exact fraction
is `20000/10201`, since `5000/10201 = 0.4901...`. The adversarial pass and the
mechanism audit report the moment-chart Hessian determinant as
`-4 A^2 Sigma^{-6}`; the correct coefficient is `-1`, as the displayed Hessian
shows. Neither correction changes any sign or any conclusion, and both are now
recorded in the counterexample register rather than silently absorbed.

**8.8 Corrected action-chart witness.**

```
pi(e^{t x^2}) = (1 - 2t)^{-1/2}
   t = -1/4 -> sqrt(6)/3 = 0.816497   FINITE
   t =  1/4 -> sqrt(2)   = 1.414214   FINITE
   t = 9/20 -> sqrt(10)  = 3.162278   FINITE
   -> "no two-sided neighbourhood exists for phi = -x^2" is FALSE
He_3 = x^3 - 3x :  E[He_3] = 0 , E[He_3^2] = 6
   t > 0 : log-integrand -> +oo as x -> -oo   ;  t < 0 : -> +oo as x -> +oo
   -> N_3(t) = +oo for every t != 0 ; N_3(0) = 1
```

**8.9 History-tier witnesses.**

```
equal objectives, metrics diag(1,1) vs diag(1,kappa) : (SC) forces a = 1 then kappa = 1
horizontal conformality sanity check R(x) = lam x    : a = lam^2 , matches
partial traversal, R = arctan : a = 1/(1+x^2) > 0 , Sigma_0 = (-pi/2, pi/2) proper, inf a = 0
orientation reversal, R(x) = -x : T R X_l = x , X_{l+1}(R x) = -x , a = -1
independently recomputed orbit : fine length = sqrt(2) = 1.41421 ,
   coarse length = 1.60023 (strictly greater) ; (SC) itself has no solution
isolated zero : h_s = 4x^2 dx^2 -> tau(R) = R^2 , inverse not differentiable at 0
clock potential : F = xy -> d alpha_F = (x^2 - y^2)/(x^2 + y^2)^{3/2} dx ^ dy , not identically 0
```

**8.10 Byte-level checks on the current sources.** These establish repository
state and nothing mathematical.

| Check | Result |
| --- | --- |
| `\mathsf{R}`, `\mathfrak{r}`, `\mathfrak{q}`, `\mathsf{C}` in `manuscripts/gauge_vfe_rg/*.tex` | zero occurrences before the edit, so `\mathsf R_\ell` is free |
| `\widehat R_\ell` already assigned | yes, `07b:2196`, recurring at `07b:2198, 2227, 2251` — the recommended rename would have collided |
| assignments of `\mathcal R` before the edit | six: `04_generative.tex:22`; `05_elbo.tex:388-434`; `05d:287`; `05d:719-783`; `07b:185`; `07b:2074`; plus `\widehat{\mathcal R}_\ell` at `07_general_renormalization.tex:45-48` |
| assignments of `\mathcal R` in `05d` after the edit | only the descent ray `\mathcal R^-_{\Fenergy_i}` and the explicit non-identification list |
| "connection-compatible" / "the connections are compatible" | five sites before the edit, defined at none; three were repaired in Task 10, and Task 11 subsequently made the remaining Chapter 6 use explicit through the isotropy and related-section criteria |
| undefined `\cref`/`\eqref` targets across all chapters | zero |
| duplicate labels across all chapters | zero |
| banned spacing macros in the edited files | zero introduced; the pre-existing `\,` occurrences in `07b` are outside the edited regions |
| doubled `\status` on one line in the edited files | zero introduced at the Task 10 freeze; Task 11 subsequently split all multi-status prose paragraphs, and its current scan reports zero outside the explicit taxonomy table |
| British spellings, banned phrases in the edited files | none |

## 9. Search-prior isolation

The affirmative-existence instruction attached to the commissioning brief was
removed from the working context before any disposition or ledger state below
was fixed, and this artifact was then rescanned for direct and paraphrased
dependence. It occurs in no hypothesis, premise, counterexample, dependency
edge, disposition, or status.

**Result: PASS.** The outcome distribution is inconsistent with a prior-driven
pass. One ledger conjunct was recorded false as written and its wording
replaced; a recommendation shared by two prior artifacts was rejected on the
bytes; two arithmetic values reported by prior artifacts were corrected against
them; a narrative claim of the portfolio (generic averaging as a contraction)
was retired rather than rescued; and four claims remain unclosed with named
obligations. Passing this audit shows only that the prior was unnecessary; it
proves nothing.

## 10. Residual obligations and provenance

**Outside the Task 10 pass at the time, and closed downstream by Task 11.**

1. `06_general_coarsegraining.tex:170`, `thm:cg-fisher-contraction`, was outside
   the Task 10 permitted file set. Task 11 now supplies the full nondominated
   joint-lift proof and the Pollard citation at that anchor. The narrower Task
   10 application remains source-closed by
   `task-10-dqm-transfer-source-map.md`, which records the preservation theorem
   in Section 3 of Pollard (2013), DOI `10.1214/12-IMSCOLL919`, arXiv
   `1107.3797`, and the exact common-dominated reduction
   `J_theta=P_theta K` followed by projection to `Y`. Jointly measurable
   parameter-smooth conditional-score versions remain separate bundle
   hypotheses. Hellinger contraction is corroboration only, not a sufficient
   DQM-score proof. `H-DQM-TRANSFER` contains only its applicability data.

<!-- SUPERSEDED historical text retained only to record the prior erroneous
external-owed characterization; it is not support for any repaired claim.
1. `06_general_coarsegraining.tex:170`, `thm:cg-fisher-contraction`: the
   quadratic-mean transfer step is asserted from parameter independence rather
   than proved. The needed argument is Hellinger contraction under a normalized
   Markov kernel — the `f`-divergence data-processing inequality with
   `f(u) = (sqrt u - 1)^2`, convex on the positive half line with `f(1) = 0`,
   applied to two probability laws and a normalized Markov kernel — together
   with rigidity of the quadratic-mean derivative. `05c_pullback_geometry.tex`
   now records that argument and its two ingredients at the point of use; the
   repair at the cited anchor was assigned to Task 11 or Task 12 scope. **This was the single
   external input on which T6 rests and it is not re-derived here.** It is
   carried visibly in the bound ledger as the declared premise
   `H-DQM-TRANSFER`, attached to `bundle-fisher-defect`,
   `pullback-compatibility`, `base-defect-cocycle`,
   `configuration-coarse-map-compatibility`, `history-duration-relation`, and
   the target, so that no claim closes over it silently. The frozen contract
   admits it under `permitted_theorems`; a checked primary-source statement for
   it was then still owed as a Task 12 or Task 15 obligation.
-->
2. At the Task 10 freeze, `06_general_coarsegraining.tex` and
   `08_infogeometry.tex` contained two of the five formerly informal
   "connection-compatible" sites. Task 10 repaired the `08` site. Task 11
   subsequently repaired the Chapter 6 anchor following
   `thm:cg-fisher-contraction` by
   naming `eq:pb-isotropy-criterion` and
   `eq:pb-coarse-related-sections` explicitly.
3. `manuscripts/gauge_vfe_rg/main.pdf` has not been regenerated and does not
   render the current sources, so `pullback-ledger-provenance` and
   `minor-emergent-time-keyword` cannot close. Task 13 and Task 14 scope.
4. Route-C evidence line anchors have shifted against the current ledger digest
   and must be re-anchored before any citation of those lines is entered as
   evidence.
5. At the time of the Task 10 pass, the control plane used two digest
   conventions, so a working-tree-bytes validator reported apparent drift on
   all twenty-one Task 5 through Task 9 evidence bindings. Task 11 adopts the
   committed-Git-blob convention for the Task 10 forward and reverse bindings;
   broader historical-ledger normalization remains Task 12 or Task 16 scope.
6. The remaining connection-compatibility wording lay outside the Task 10
   permitted files; its downstream Task 11 closure is recorded in item 2.

**Inside the theory, and recorded as `OPEN` in the manuscript's obligation
appendix.**

7. Functional compatibility and horizontal conformality for the manuscript's own
   renormalization maps (`O-SC`), stated at
   `prop:hist-natural-gradient-sufficiency`.
8. Whether the recognition families a particular application declares can be
   brought to one of the two standing configuration tiers.
9. Smooth structure of the projectable set, which would need a transversality or
   elliptic-regularity hypothesis; the integrated stack avoids it by declaring
   `\mathsf R_\ell` separately, so this is an optional refinement rather than a
   load-bearing gap.
10. Whether free, **proper**, and isometric gauge action alone can fail to give
   the orthogonal quotient speed. The available witness is free and isometric
   with a dense orbit tangent; properness would force closed orbits, so it does
   not settle the question.
11. Classification of the accidental solutions of the quadratic-form cocycle
   criterion and of the signed positivity criterion, in intrinsic terms.

## 11. What this construction does not claim

No global section, hence no global base semimetric, without a section-existence
hypothesis. No principal scale map without its topological condition. No
active-gauge invariance of the pullback tensors; only passive covariance. No
quotient manifold from constant rank alone — involutivity, a regular leaf space,
and basicness are three further hypotheses, and the contact form
`dz - x dy` exhibits constant rank with a nonintegrable radical. No Loewner
ordering between a joint-law pullback and a weighted product of marginal fiber
metrics, in either direction. No duration comparison from any fiberwise
contraction theorem. No identification of Fisher duration with physical time, no
clock potential without a closed zero-period one-form, no Lorentzian signature,
no causal structure, and no canonical connection anywhere. The scale index is
renormalization depth and nothing else. The Task 10 pass did not alter the
then-pending citation, notation, status, or minor-repair scope; Task 11 closes
those downstream items separately. The interaction tier, retained projection,
beta data, and fixed objects remain outside the Task 10 edit set.

## 12. Ledger dispositions assigned by this pass

Eighteen claims are bound. Twelve were already in the ledger and six were added
because the compound target is not atomized without them.

| Claim | State | Basis, and what would have blocked it |
| --- | --- | --- |
| `score-action-compatibility` | EVIDENCE_VERIFIED | T21. The registered witness fencing it was false and is replaced; the fence itself survives intact. |
| `bundle-morphism-descent` | EVIDENCE_VERIFIED | Lemma 4.1 and the biconditional with its degenerate case and existence obstruction recorded. |
| `bundle-fisher-defect` | EVIDENCE_VERIFIED | T6, with primitive applicability data in `H-DQM-TRANSFER` and the transfer conclusion supplied directly by the bound Pollard source map. |
| `bundle-scale-cocycle` | EVIDENCE_VERIFIED | T7 and the five-level composition laws now displayed rather than asserted. |
| `horizontal-defect-anomaly` | EVIDENCE_VERIFIED **after wording repair** | T2, T3, T4, T7. The clause "positivity follows only when that defect vanishes" was **false as written** and is replaced by the exact signed criterion; that conjunct would otherwise have blocked release. |
| `pullback-compatibility` | EVIDENCE_VERIFIED **after wording repair** | T3, T5, T6. The undefined phrase is replaced by the isotropy condition and the singular "vertical mismatch term" by the two retained tensors. |
| `base-defect-cocycle` (new) | EVIDENCE_VERIFIED | T8, checked at type level and at instance level. |
| `configuration-fisher-metric` | EVIDENCE_VERIFIED **on the exhibited finite tier** | T10, T11. Closed by the derivation from its stated primitive data, not by a hypothesis restating regularity, gauge closure, or nonemptiness; other tiers remain conditional on separate verification. |
| `configuration-map` | EVIDENCE_VERIFIED **after the symbol repair** | T13. The notation conjunct was **false on the bytes** before this pass and is closable only by edit; the rename recommended by two prior artifacts would have created a fresh collision. |
| `configuration-projectability` | EVIDENCE_VERIFIED | T9, with the infinite-dimensional statement scoped to a collapsing base map and the averaging branch fenced. |
| `configuration-coarse-map-compatibility` (new) | EVIDENCE_VERIFIED | T12, with generic averaging-as-contraction retired by name. |
| `cross-scale-declaration-compatibility` (new) | EVIDENCE_VERIFIED | T14, with both reversal witnesses. |
| `curve-typing` (new) | EVIDENCE_VERIFIED | T15. |
| `history-semiconjugacy` | EVIDENCE_VERIFIED | T16 as a criterion. What is *not* claimed is that this manuscript's own recomputed maps satisfy it; that is obligation 7 of Section 10 and is `OPEN` in the source. |
| `history-noncollapse` | EVIDENCE_VERIFIED | T17. |
| `history-duration-relation` | EVIDENCE_VERIFIED | T18, with both independent mechanisms witnessed. |
| `natural-gradient-semiconjugacy` (new) | EVIDENCE_VERIFIED | T19, stated as sufficiency and never as automatic. |
| `coordinate-independence` (new) | EVIDENCE_VERIFIED | T20. Its regularity and selected-metric data are in the quantifier; `H-HISTORY` is only the nonphysical-time modeling scope. |

No Task 10 claim is left `CANDIDATE`. At the Task 10 freeze, the remaining
`CANDIDATE` claims belonged to Task 11 minor repairs, Task 13 numerical and
manifest evidence, Task 14 build integrity, and the target itself. Task 11 now
closes its downstream subset; nothing here asserts terminal release.

## 13. Falsification conditions for this record

This record is falsified by any of the following: a scope-matched
counterexample to any of T1 through T21 under its stated hypotheses; a
demonstration that the exhibited configuration tier fails one of the properties
proved in T10, which would refute that finite-tier derivation without treating
`H-CONFIG` as a nonemptiness or regularity conclusion; an admitted instance in which the
base-cocycle residual differs from the three forms of T8; an admitted instance
in which the signed base comparison differs from T3; a proof that the
quadratic-mean transfer step of T6 is false, which would break the vertical
Fisher defect identity; a source-level demonstration that `\mathsf R_\ell` or
any newly introduced symbol collides with an existing assignment; or a
demonstration that any status assigned in the bound ledger rests on agreement
among the input artifacts rather than on a derivation reproduced here.
