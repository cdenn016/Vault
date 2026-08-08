<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 10 interface reconciliation — one conditional effective theory

**Terminal status for integration readiness: `INCONCLUSIVE`.** See Part XII. The
mathematics is integrable today under the hypothesis set of Part X, whose domains
are proved nonempty by an explicit composite witness (Part V, Tier F). What blocks
`PASS` is not a mathematical gap: three conjuncts of in-scope ledger claims are
*currently false on the bytes* and can be repaired only by edits to the manuscript,
the ledger, and the build — files this pass is forbidden to touch. Each edit is
specified exactly in Part IX.

---

## 0. Binding, scope, and method

### 0.1 Input digests

Base revision `02d5d8f542cba2d92c6a430483b62155dd5f2db4`, branch
`codex/gauge-vfe-rg-task10-pullbacks-20260804`. All digests are SHA-256 of the
working-tree bytes read by this pass.

| Path (relative to repository root) | SHA-256 |
| --- | --- |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/problem-contract.json` | `7cba2e9bbfe34028d6a994359e53c761779bd255c5405bfa3996c50ca575bc22` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/claim-ledger.json` | `53d9a2ae2ceab6a20c0486facc68e07bfb66731ebdccdfcc7c87f9890357c5f7` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/dependency-dag.json` | `bb296da12424fdd766727f0236aa6b91b1cb8fcfb93e3016882532049a119c16` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/approach-registry.json` | `73c9cc54e9626750547d7e8eea530a9367b9c29f813621cdde7b408f75b9f891` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/counterexample-register.md` | `c7e0fa8d576ab60c2d4060f423e4222e800116a0293e0097c8d38ab55e6b6853` |
| `.../evidence/task-10-bundle-pullback-analysis.md` | `124010f91e7bc2a7569d5d85bc9dcf5ba44581da508eb246a836ca222b00e63b` |
| `.../evidence/task-10-score-configuration-analysis.md` | `9161b0f0941ed7b2061ba1102b2a5df5acbe318a8c2d57fc391003f7a782de4f` |
| `.../evidence/task-10-timeless-history-analysis.md` | `e1bbfa7c32dbcae010e4e2f62e5a8e356907c4ecabf0e604ae4a461e3f57f7f4` |
| `.../evidence/task-10-preintegration-adversarial.md` | `ff81719406628644a3cde746cb88dc91ca7c282ab1eed51a217cf1b584abf44c` |
| `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex` | `a87bc2b3d7d8d76412a299fbd3220464802bd1cc2d853f1f6c287f96e5a73279` |
| `manuscripts/gauge_vfe_rg/05d_relational_inference.tex` | `138e4f86f107f5bd0307e049dc5368a6c36584a827bf98bf4eb396e30016d0a1` |
| `manuscripts/gauge_vfe_rg/06_general_coarsegraining.tex` | `a6a60a19a7c263915e749787b12470a84d6fafcaf9d55c69b71c0490c45c064a` |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `a3a7ae2fed2eb4a1ea4668393a69b4d56aa2c9dd071af06ddbcba717d7365797` |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `148d9652229eb6d3c40a41b48c1eb938328ca697a37e8113111567c580cc61be` |
| `manuscripts/gauge_vfe_rg/08_infogeometry.tex` | `55bfcdff0eebec24f2231852467255d13a0c02d1369621d04ede53cad3b7c31b` |
| `manuscripts/gauge_vfe_rg/appendix_notation.tex` | `d39936499c9673c1b4ed75ae31bf294f8d4df9fd1fd0cef1dae4a9ec5a572fa4` |

Every digest agrees with the corresponding row of the falsifier's binding table
(`task-10-preintegration-adversarial.md:34-54`). **No input drift is reported.**

### 0.2 Method and independence boundary

Route agreement is used nowhere as evidence. Every identity that a route uses to
close a claim was re-derived here from the frozen contract's declared types, and
every arithmetic witness was recomputed in exact rational or symbolic form
(Part XI). Where the three routes disagree, the disagreement is decided by
derivation, not by count (Part VIII). Where the falsifier sustained a defect, this
pass supplies the repaired object rather than restating the defect.

The affirmative-existence instruction attached to the commissioning brief is a
search prior. It allocated effort. It occurs in no premise, hypothesis,
counterexample, disposition, or terminal status. Part XII records the erasure audit.

### 0.3 What this pass created

Exactly one file, this one. No Git mutation, no TeX build, no ledger or register
write, no edit to any manuscript, control, or other evidence artifact. Two symbolic
and numerical verification sessions were executed; their transcripts are Part XI.
Numerical and symbolic agreement corroborates arithmetic and closes no theorem.

---

## Part I — The type table and the commuting/noncommuting diagram

This part discharges brief item 1.

### I.1 Standing data

Fix one channel at a time; the two-channel version is Part V.6. Bases
$\mathcal C,\bar{\mathcal C}$ are finite-dimensional, second-countable, Hausdorff
smooth manifolds with $f\in C^\infty(\mathcal C,\bar{\mathcal C})$; $G,\bar G$ are
Lie groups with a homomorphism $\kappa:G\to\bar G$; $\pi:P\to\mathcal C$ and
$\bar\pi:\bar P\to\bar{\mathcal C}$ are principal bundles;
$(\mathsf K,\mathscr K)$ and $(\bar{\mathsf K},\bar{\mathscr K})$ are standard
Borel; $\rho,\bar\rho$ are represented sample actions by bimeasurable bijections
with induced law actions $\widehat\rho,\widehat{\bar\rho}$;
$\mathcal B\subseteq\mathcal P(\mathsf K)$ and
$\bar{\mathcal B}\subseteq\mathcal P(\bar{\mathsf K})$ are smooth parametrized-measure
models in the sense of `hyp:geo-smooth-tier` and `hyp:pb-regular-models`
(`05c_pullback_geometry.tex:25`), each invariant under its represented action,
each DQM with square-integrable scores and positive definite Fisher forms
$g^F,\bar g^F$; $E=P\times_{\widehat\rho}\mathcal B$ and
$\bar E=\bar P\times_{\widehat{\bar\rho}}\bar{\mathcal B}$ with the manuscript's
quotient convention `eq:geo-quotient-convention`; $\omega,\bar\omega$ are principal
connections with Ehresmann horizontal distributions and vertical projectors
$\operatorname{ver}^\omega,\operatorname{ver}^{\bar\omega}$;
$\zeta,\bar\zeta$ are the infinitesimal fiber actions and $\vartheta$ the
fundamental vertical map of `eq:pb-connection-difference-vertical`.

### I.2 Type table

Fifteen objects. Rows 1–3 are the three the brief requires never be identified;
rows 12–15 are the four that the current manuscript does identify or leave untyped.

| # | Symbol | Kind | Domain → codomain | Determined by | Must never be identified with |
| --- | --- | --- | --- | --- | --- |
| 1 | $K_\ell$, written $N$ here | sample kernel | $N:\mathsf K\times\bar{\mathscr K}\to[0,1]$; $N(x,\bar{\mathsf K})=1$ for **every** $x$ | modeling declaration (`H-MARKOV`, (H3)) | $N_\star$, $q$, $\Psi$, $\mathsf R_\ell$ |
| 2 | $N_\star$ (the induced law map, $K_\#$) | affine map of laws | $\mathcal P(\mathsf K)\to\mathcal P(\bar{\mathsf K})$, $(N_\star\beta)(B)=\int N(x,B)\beta(dx)$ | $N$; **not** conversely | $N$; $q$ off $\mathcal B$ |
| 3 | $q:=N_\star|_{\mathcal B}$ | law-fiber map | $\mathcal B\to\bar{\mathcal B}$; **exists only under (H5)** $N_\star(\mathcal B)\subseteq\bar{\mathcal B}$ | $N$ + (H5); smoothness is a further hypothesis | $N_\star$ on all of $\mathcal P(\mathsf K)$ |
| 4 | $\mathcal P$ | principal scale map | $P\to\bar P$, smooth, $\kappa$-equivariant, $\bar\pi\mathcal P=f\pi$ | **declared**; exists iff $P\times_\kappa\bar G\cong f^*\bar P$ (R7) | $f$, $\Psi$ |
| 5 | $\Psi$ | associated-bundle morphism | $E\to\bar E$, $\bar\varpi\Psi=f\varpi$ | $(\mathcal P,\kappa,q)$ **and** the intertwining (I) | $N$, $N_\star$, $q$, $\mathsf R_\ell$ |
| 6 | $T^V\Psi$ | vertical tangent map | $VE\to V\bar E$ over $\Psi$; equals $T_\beta q$ in the frame pair $(u,\mathcal P(u))$ | $\Psi$ | $T\Psi$; $q$ itself |
| 7 | $D^\omega s=\operatorname{ver}^\omega\circ Ts$ | covariant vertical first jet | $\Gamma(\mathcal U;T^*\mathcal U\otimes s^*VE)$ | $(\omega,s)$ | $Ts$; $ds_u$ |
| 8 | $A_\Psi=\mathcal D\Psi$ | horizontal defect (anomaly) | $\Gamma(E;\varpi^*T^*\mathcal C\otimes\Psi^*V\bar E)$ | $(\Psi,\omega,\bar\omega)$; $=\vartheta(\mathfrak A_{\mathcal P})$ in the induced case | $\Delta_F^\Psi$; a scalar |
| 9 | $\Delta_F^\Psi=g^F-(T^V\Psi)^*\bar g^F$ | vertical Fisher defect | $\Gamma(E;\operatorname{Sym}^2V^*E)$ | $(g^F,\bar g^F,T^V\Psi)$ | $\delta_\Psi$ (its base pullback) |
| 10 | $f$ | base coarse map | $\mathcal C\to\bar{\mathcal C}$; surjective submersion wherever descent is used | declared | $K_\ell$, $\mathsf R_\ell$, $\widehat{\mathcal R}_\ell$ |
| 11 | $\Psi\circ s=\bar s\circ f$ | **section relation**, not a map | a predicate on $(s,\bar s)$ | equivalent to (P2) fiber constancy | a definition of $\bar s$ from $s$ |
| 12 | $\mathcal Q_\ell$ | configuration manifold | Tier F: $\cong\mathbb R^{N}$; Tier b1: $L^2(\mu;\mathbb R^K)$ | **declared** $(\mu,w,\text{basis},\text{topology})$ | $\Gamma(\mathcal C,E)$ as a bare set |
| 13 | $\mathsf R_\ell$ | configuration coarse map | $\mathcal Q_\ell\to\mathcal Q_{\ell+1}$, smooth | **separately declared** (Part V) | $K_\ell$, $\mathcal R^H$, $\mathcal R_b$, $M_\ell$, $C_{\ell,s}$, $\widehat{\mathcal R}_\ell$, $\widehat R_\ell$, $\Psi$, the root-vertex set $\mathcal R$, the descent ray $\mathcal R^-$ |
| 14 | $\mathsf G_\ell$ | configuration metric | $\Gamma(\operatorname{Sym}^2T^*\mathcal Q_\ell)$, **strong** | $(\mu,w,g^F,\text{lift or product label})$ | $h^\omega_s$, $g^F$, $\bar g^F$ |
| 15 | $\mathscr S_\pi$, $U{=}R$, $\mathscr I_b$ | score isometry / restriction / extensive lift | $L^2(\pi)/\mathbb R\mathbf 1\to L^2_0(\pi)$; $L^2(\pi)\to L^2(\pi K)$ with $\|R\|\le1$; $L^2_0(\pi)\to L^2_0(\pi^{\otimes b})$ with $\|\mathscr I_b\|=\sqrt b$ | $\pi$; $(\pi,K)$; $b$ | each other (Part IV) |

**Lemma I.1 (strictness of rows 1–3, and of rows 5–6).** (i) $N$ determines
$N_\star$ and hence $q$; the converse fails. (ii) Sample-level $\kappa$-equivariance
of $N$ implies the law-level intertwining
$q\circ\widehat\rho(g)=\widehat{\bar\rho}(\kappa g)\circ q$; the converse fails.
(iii) $\Psi$ determines $q$ only up to the isotropy group of the image point, and
never determines $N$.

*Proof.* (ii) forward: for $B\in\bar{\mathscr K}$,
$(N_\star\widehat\rho(g)\beta)(B)=\int N(\rho(g)x,B)\beta(dx)
=\int N(x,\bar\rho(\kappa g)^{-1}B)\beta(dx)=(\widehat{\bar\rho}(\kappa g)N_\star\beta)(B)$.
The converses share one witness: $\mathsf K=\mathbb R^2$, $\bar{\mathsf K}=\mathbb R$,
$G=SO(2)$ by rotation, $\bar G=\{e\}$, $\kappa$ trivial,
$\mathcal B=\{\mathcal N(0,\sigma^2I_2):\sigma>0\}$. The action fixes every point of
$\mathcal B$, so the law-level relation holds for **every** kernel. The three kernels
$N_1(x,\cdot)=\delta_{x_1}$, $N_2(x,\cdot)=\delta_{x_2}$,
$N_3(x,\cdot)=\delta_{(x_1+x_2)/\sqrt2}$ all send $\mathcal N(0,\sigma^2I_2)$ to
$\mathcal N(0,\sigma^2)$, so $q_1=q_2=q_3$ while $N_1\ne N_2\ne N_3$; none is
$SO(2)$-equivariant as a kernel. (iii) is immediate from
$\Psi[u,\beta]=[\mathcal P(u),q\beta]$. $\square$

This is Lemma 2.1 of the bundle route, re-derived; the witness is verified here
by direct computation of the three pushforwards.

### I.3 The diagram: what commutes and what does not

Write the nine squares that the integrated theory needs. **C** = commutes
unconditionally; **C(h)** = commutes exactly under the stated hypothesis;
**N** = does not commute, with the exact defect named.

```
                                 (D1)  C
        E  --------------- Psi ---------------->  Ebar
        |                                           |
     varpi                                      varpibar
        |                                           |
        v                                           v
        C  ---------------  f  ----------------> Cbar
        bar varpi o Psi = f o varpi           always, for any Psi over f


                                 (D2)  C(I)
   P x B  ---- P x q ---->  Pbar x Bbar
     |                          |
   quotient                  quotient
     |                          |
     v                          v
     E  ------- Psi ------->   Ebar
   commutes  <=>  q o rhohat(g) = rhobarhat(kappa g) o q  for every g   ... (I)
   (given a declared kappa-equivariant P; detached from that datum (I) is not
    necessary — if Bbar is a single Gbar-fixed point it is vacuous)


                                 (D3)  C(frame)
   In the frame pair (u(c), Pcal(u(c))):   T^V Psi  =  T q .
   In an arbitrary frame pair (u, ubar o f):  psi_c = rhobarhat(varsigma(c)) o q ,
   so (T psi_c)^* gbar^F = (Tq)^* ( rhobarhat(varsigma)^* gbar^F ) ,
   and the c-dependent factor cancels ONLY under Gbar-invariance of gbar^F.


                                 (D4)  N   <-- the anomaly lives here
     T_c C  --- D^omega s --->  V_{s(c)} E
       |                              |
      T_c f                       T^V Psi
       |                              |
       v                              v
   T_{f(c)} Cbar --D^omegabar sbar--> V_{sbar(f(c))} Ebar

   D^omegabar sbar (T_c f X)  =  T^V Psi (D^omega s X)  +  A_Psi(s(c); X)
   Commutes  <=>  A_Psi(s;.) = 0  <=>  Afrak_P(X) in gbar_{sbar(f(c))} (isotropy).


                                 (D5)  one-way triangle
        N  ==>  N_star  ==>  q = N_star|_B      (needs (H5) for the second arrow)
        q  =/=>  N ;   Psi  =/=>  q ;   Psi =/=> N            (Lemma I.1)


                                 (D6)  partial map
   Gamma(C,E) ---- Q |-> Psi o Q ---->  {maps C -> Ebar}
   descends to Gamma(Cbar,Ebar) exactly on Gamma_proj(Psi) = { (P2) holds },
   a PROPER subset whenever ker T_c f =/= 0 and T^V Psi is nonzero on some
   vertical direction there.  Smoothness of the descent is then automatic.


                                 (D7)  N in general, C(decl) by declaration
   Q_l ------------ R_l ------------> Q_{l+1}          <-- separately declared
    |                                     |
  (pointwise-induced descent, defined only on Gamma_proj)
   The two agree on Gamma_proj(Psi) n Q_l and nowhere else in general.


                                 (D8)  C   <-- the score/action square
   L^inf(pi)/R1 --- Ubar ---> L^inf(pi K)/R1
        |                           |
      S_pi                       S_{pi K}
        |                           |
        v                           v
     L^2_0(pi) ------ R ------> L^2_0(pi K)
   S_{piK}[Ubar[phi]] = U S_pi[phi] ;  U|_{L^2_0} = R ;  ||R|| <= 1 .
   Extends by continuity to the Fisher completion.  Commutes unconditionally.


                                 (D9)  C(SC) up to a time change
   Q_l --- Phi_t ---> Q_l                R_l Phi_t(Q) = Phibar_{sigma_Q(t)}(R_l Q)
    |                  |                 sigma_Q(t) = int_0^t a_l(Phi_s Q) ds
   R_l                R_l                holds  <=>  T R_l X_l = a_l (X_{l+1} o R_l),
    v                  v                             a_l > 0 continuous       ...(SC)
   Q_{l+1} -Phibar_u-> Q_{l+1}           and then Sigma_Q subset Jbar^max .
```

**Reading.** (D1), (D5), (D8) are unconditional. (D2) is the descent condition.
(D3) is why coarse-side $\bar G$-invariance is an independent hypothesis. (D4) is
where the entire Task 10 anomaly lives; every positivity, cocycle, and pullback
statement downstream is a statement about how far (D4) is from commuting. (D6) and
(D7) are why a bundle morphism does not give a configuration map. (D9) is the
history interface, which touches (D4) not at all.

---

## Part II — The signed anomaly, the ordered composition law, and the corrected sharp cocycle

This part discharges brief item 2 and resolves the falsifier's **M-1**, **M-2**,
and **M-6**.

### II.1 The exact first jet (D4)

**Theorem II.1.** Let $s\in\Gamma(\mathcal U,E)$, $\bar s\in\Gamma(f(\mathcal U),\bar E)$
satisfy $\Psi\circ s=\bar s\circ f$. Then for every $c\in\mathcal U$, $X\in T_c\mathcal C$,

$$
D^{\bar\omega}\bar s\big(T_cfX\big)=T^V\Psi\big(D^\omega sX\big)+A_\Psi\big(s(c);X\big),
\qquad
A_\Psi(e;X):=\operatorname{ver}^{\bar\omega}\!\big(T_e\Psi(H^\omega_eX)\big).
\tag{II.1}
$$

*Proof.* $T\bar\varpi\big(T\Psi(H^\omega_eX)\big)=Tf\big(T\varpi H^\omega_eX\big)=T_cfX$,
so $T\Psi(H^\omega_eX)$ projects onto $T_cfX$; its $\bar\omega$-horizontal part is
$H^{\bar\omega}_{\Psi(e)}(T_cfX)$ and its vertical part is $A_\Psi(e;X)$, which is
therefore linear in $X$ and equals
$T_e\Psi(H^\omega_eX)-H^{\bar\omega}_{\Psi(e)}(T_cfX)$ — the manuscript's
`eq:pb-coarse-horizontal-defect`. Now split $T_csX=H^\omega_{s(c)}X+D^\omega sX$ and
apply $T\Psi$; verticality is preserved on the second summand. On the other side,
$\Psi s=\bar s f$ gives
$T\Psi(T_csX)=H^{\bar\omega}_{\bar s(f(c))}(TfX)+D^{\bar\omega}\bar s(TfX)$. Since
$\Psi(s(c))=\bar s(f(c))$ the horizontal terms cancel; comparing vertical parts
gives (II.1). $\square$

This certifies `eq:pb-covariant-jet-chain-rule` (`05c_pullback_geometry.tex:609`)
exactly as printed.

### II.2 The exact signed Fisher comparison, and the exact positivity criterion

Write $u_X:=D^\omega sX$, $v_X:=T^V\Psi(u_X)$, $a_X:=A_\Psi(s(c);X)$, so that by
(II.1) the coarse jet is $\bar u_X:=D^{\bar\omega}\bar s(T_cfX)=v_X+a_X$. Set
$\delta_\Psi:=(D^\omega s)^*\Delta_F^\Psi$,
$\mathcal X_\Psi(X,Y):=\bar g^F(v_X,a_Y)+\bar g^F(a_X,v_Y)$,
$\mathcal Q_\Psi(X,Y):=\bar g^F(a_X,a_Y)$.

**Theorem II.2 (exact signed comparison; no compatibility hypothesis).**

$$
h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}
=\delta_\Psi-\mathcal X_\Psi-\mathcal Q_\Psi .
\tag{II.2}
$$

$\mathcal X_\Psi$ is symmetric and **signed**; $\mathcal Q_\Psi\succeq0$.

*Proof.* $(f^*\bar h)(X,Y)=\bar g^F(v_X+a_X,v_Y+a_Y)
=\bar g^F(v_X,v_Y)+\mathcal X_\Psi(X,Y)+\mathcal Q_\Psi(X,Y)$, and
$\bar g^F(v_X,v_Y)=\big((T^V\Psi)^*\bar g^F\big)(u_X,u_Y)=g^F(u_X,u_Y)-\Delta_F^\Psi(u_X,u_Y)$.
Subtract from $h^\omega_s(X,Y)=g^F(u_X,u_Y)$. $\square$

**Theorem II.3 (exact signed criterion — the repair of the ledger's "only when").**
Assume the Markov hypotheses of Theorem II.5 below, so $\delta_\Psi\succeq0$. Then
the following are equivalent at $c$:

1. $h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}\succeq0$;
2. $\big\|D^{\bar\omega}\bar s(T_cfX)\big\|_{\bar g^F}\le\big\|D^\omega sX\big\|_{g^F}$ for every $X$;
3. $$\boxed{\;2\,\bar g^F\!\big(T^V\Psi D^\omega sX,\;A_\Psi(s(c);X)\big)+\big\|A_\Psi(s(c);X)\big\|^2_{\bar g^F}\;\le\;\delta_\Psi(X,X)\quad\text{for every }X.\;}$$

*Proof.* (1)$\Leftrightarrow$(2) is (II.2) read on the diagonal, using
$h(X,X)=\|u_X\|_{g^F}^2$ and $f^*\bar h(X,X)=\|v_X+a_X\|^2_{\bar g^F}$.
(2)$\Leftrightarrow$(3): expand $\|v_X+a_X\|^2=\|v_X\|^2+2\bar g^F(v_X,a_X)+\|a_X\|^2$
and substitute $\|v_X\|^2_{\bar g^F}=\|u_X\|^2_{g^F}-\delta_\Psi(X,X)$. $\square$

**Corollary II.4 (the exact status of "only when").** $A_\Psi(s;\cdot)=0$ is
**sufficient** for base positivity, because it makes the left side of II.3(3)
vanish while the right side is $\ge0$. It is **not necessary**: whenever
$\bar g^F(v_X,a_X)<0$ is large enough in modulus, II.3(3) holds strictly with
$a_X\ne0$, and the signed difference is strictly positive. The pointwise margin
$\|a_X\|_{\bar g^F}\le\sqrt{h(X,X)}-\sqrt{h(X,X)-\delta_\Psi(X,X)}$ (the bundle
route's R3.5) is sufficient and **not** necessary.

**Verification.** Recompute R11's declared data: $\mathcal C=\bar{\mathcal C}=\mathbb R$,
$f=\mathrm{id}$, $\mathcal B=\{\mathcal N(\mu,1)\}$ with $g^F=1$, kernel
$N(x,\cdot)=\mathcal N(x,1)$ so $\bar{\mathcal B}=\{\mathcal N(\mu,2)\}$ with
$\bar g^F=\tfrac12$ and $\Delta_F^\Psi=\tfrac12$; section $\sigma(x)=mx$, $A_\omega=0$,
$\bar A=b\,dx$, so $a_X=b\,\partial_\mu$ and $v_X=m$. At $m=1$ (Part XI, Block 3):

| $b$ | $h-f^*\bar h$ | II.3(3) left side | $\delta_\Psi$ | criterion met | positive |
| --- | --- | --- | --- | --- | --- |
| $0$ | $1/2$ | $0$ | $1/2$ | yes | yes |
| $1/10$ | $79/200$ | $21/200$ | $1/2$ | yes | **yes** |
| $-1/10$ | $119/200$ | $-19/200$ | $1/2$ | yes | **yes** |
| $1/2$ | $-1/8$ | $5/8$ | $1/2$ | no | no |
| $-3/5$ | $23/25$ | $-21/50$ | $1/2$ | yes | **yes** |

The identity $h-f^*\bar h=\delta_\Psi-[\,2\bar g^F(v,a)+\|a\|^2]$ holds identically in
$(m,b)$ (symbolic check, Part XI Block 3). Rows 2, 3, 5 have $A_\Psi\ne0$ with
strictly positive base comparison. **The ledger's clause "positivity follows only
when that defect vanishes" is false on its material reading and must be replaced by
Theorem II.3(3)** (Part IX, edit L-1).

**Theorem II.5 (positive Markov Fisher defect).** Assume (A1) a declared smooth
$\kappa$-equivariant $\mathcal P$ over $f$; (A2) family closure
$N_\star(\mathcal B)\subseteq\bar{\mathcal B}$; (A3) the intertwining (I); (A4)
smoothness of $q$ between the declared parametrized-measure models; (A5)
invariance of $\mathcal B,\bar{\mathcal B}$ under their represented actions; (A6)
$\bar g^F$ positive definite **and $\widehat{\bar\rho}(\bar G)$-invariant**; (A7)
$\Psi\circ s=\bar s\circ f$; (A8) DQM with square-integrable scores and a jointly
measurable $\theta$-smooth version selection for $p\mapsto T^V_p\Psi$; and (A9)
$A_\Psi(s(c);X)=0$ for all $c,X$. Then

$$
h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}=\delta_\Psi=(D^\omega s)^*\Delta_F^\Psi\succeq0,
\qquad
\Delta_F^\Psi(w,w)=\mathbb E_\beta\operatorname{Var}_\beta\big(\ell_w(X)\mid Y\big)\ge0,
$$

with equality at $X$ exactly when $\ell_{D^\omega sX}$ is $\sigma(Y)$-measurable
$\beta$-almost surely.

*Proof.* The base identity is (II.2) with $\mathcal X_\Psi=\mathcal Q_\Psi=0$. For the
vertical statement, work in the frame pair $(u(c),\mathcal P(u(c)))$, where
$T^V\Psi=Tq$ (D3). The DQM-transfer step — that $t\mapsto q(\beta_t)=\beta_tN$ is DQM
with score $\bar\ell_w=\mathbb E[\ell_w(X)\mid Y]$ — is **not** immediate from
parameter independence and must be cited, not asserted: it is Theorem A of the score
route (`task-10-score-configuration-analysis.md:205-267`), whose Step 4 closes the gap
using Hellinger contraction under a normalized Markov kernel (Csiszár's
$f$-divergence data-processing inequality with $f(u)=(\sqrt u-1)^2$) plus DQM
rigidity. Given that, the law of total variance gives
$\mathbb E[\ell_w^2]-\mathbb E[\bar\ell_w^2]=\mathbb E\operatorname{Var}(\ell_w\mid Y)\ge0$,
which is $g^F(w,w)-\bar g^F(Tq\,w,Tq\,w)$. Pulling back by $D^\omega s$ preserves
positive semidefiniteness. $\square$

**Decision on the M-10 contradiction.** The bundle route's R3.5 writes "because $N$
carries no parameter dependence", which is the conclusion, not an argument; the score
route proves it. The portfolio as a whole has the proof. *Decided in favor of the
score route*; the integrated stack cites Theorem A at this step, and the same
substitution is owed at `thm:cg-fisher-contraction`
(`06_general_coarsegraining.tex:170`).

**Decision on the M-11 contradiction.** The bundle route records "missing coarse
$\bar G$-invariance of the coarse Fisher metric" as SUSTAINED; the falsifier
downgrades it. Checked on the bytes: `hyp:pb-regular-models`
(`05c_pullback_geometry.tex:25`) assumes the represented action is induced by a
parameter-independent bimeasurable sample re-coordinatization preserving
$\mathcal B_x$, and `prop:pb-statistical-tensor-descent` (`05c:54`) already needs
that to make $\bar g^F$ a vertical tensor at all. Applied at the coarse scale it *is*
$\widehat{\bar\rho}(\bar G)$-invariance. **The downgrade is correct**; the genuine
residue is that `sec:pb-fisher-defect` (`05c:673`) never instantiates
`hyp:pb-regular-models` at the coarse scale, so a reader cannot see where (A6) comes
from. Severity: cross-reference, not missing hypothesis.

### II.3 Minimal isotropy condition for zero anomaly

**Theorem II.6 (frame-twist form and the sharp vanishing criterion).** Suppose $\Psi$
is induced by $(\mathcal P,\kappa,q)$ with (I). Define the **scale-connection defect
form** $\mathfrak A_{\mathcal P}:=\mathcal P^*\bar\omega-d\kappa\circ\omega\in\Omega^1(P,\bar{\mathfrak g})$.
Then:

1. $\mathfrak A_{\mathcal P}$ is horizontal and $\operatorname{Ad}\circ\kappa$-equivariant,
   hence descends to $\mathfrak A_{\mathcal P}\in\Omega^1(\mathcal C;f^*\operatorname{Ad}\bar P)$.
2. $A_\Psi(e;X)=\vartheta_{\Psi(e)}\big(\mathfrak A_{\mathcal P}(X)\big)$: **the horizontal
   defect is a fundamental vertical field**, so it is determined by a
   $\bar{\mathfrak g}$-valued one-form on the base and not by the fiber point.
3. **Minimal condition.** $A_\Psi$ vanishes along $s$ **if and only if**
   $$
   \mathfrak A_{\mathcal P}(X)\in\bar{\mathfrak g}_{\,\bar s(f(c))}\quad\text{for every }c,X,
   $$
   the isotropy subalgebra of the coarse section value under $\widehat{\bar\rho}$.
   The principal-level identity $\mathcal P^*\bar\omega=d\kappa\circ\omega$ (i.e.
   $\mathfrak A_{\mathcal P}=0$) is sufficient, and necessary only when the represented
   action is infinitesimally effective at $\bar s(f(c))$.
4. $\mathcal Q_\Psi=\mathfrak a^*\mathfrak k_{\bar s(f(c))}$ with
   $\mathfrak k_{\bar\beta}(\xi,\eta)=\bar g^F(\bar\zeta_\xi\bar\beta,\bar\zeta_\eta\bar\beta)\succeq0$,
   whose radical is exactly $\bar{\mathfrak g}_{\bar\beta}$ — consistent with 3.

*Proof.* 1: $\mathcal P^*\bar\omega(\zeta_\xi)=\bar\omega(\bar\zeta_{d\kappa\xi})=d\kappa\,\xi$,
so the difference annihilates vertical vectors; equivariance follows from
$R_g^*\mathcal P^*\bar\omega=\operatorname{Ad}_{\kappa(g)^{-1}}\mathcal P^*\bar\omega$
and $d\kappa\circ\operatorname{Ad}_{g^{-1}}=\operatorname{Ad}_{\kappa(g)^{-1}}\circ d\kappa$.
2: in the trivializations $\Psi(c,\beta)=(f(c),\psi_c\beta)$ with
$\psi_c=\widehat{\bar\rho}(\varsigma(c))\circ q$; using
$H^\omega_{(c,\beta)}X=(X,-\zeta_{A(X)}\beta)$ together with the equivariance of the
differential $Tq\circ\zeta_\xi=\bar\zeta_{d\kappa(\xi)}\circ q$ — obtained by
differentiating (I) at $g=\exp(t\xi)$, $t=0$ — one gets
$A_\Psi(X)=\bar\zeta_{\mathfrak a(X)}(\psi_c\beta)$ with
$\mathfrak a(X)=\bar A(TfX)+\theta_R(X)-\operatorname{Ad}_{\varsigma}(d\kappa A(X))$
and $\mathfrak a=\operatorname{Ad}_\varsigma(u^*\mathfrak A_{\mathcal P})$. 3: a
fundamental field vanishes at $\bar\beta$ iff its generator lies in
$\bar{\mathfrak g}_{\bar\beta}$; conjugation by $\operatorname{Ad}_\varsigma$ moves the
statement between $\mathfrak a$ and $u^*\mathfrak A_{\mathcal P}$ and moves the isotropy
algebra with it. 4 is 2 substituted into $\mathcal Q_\Psi$. $\square$

**This is the definition of the undefined phrase.** "Connection-compatible" /
"the connections are compatible" occurs at exactly five sites and is defined at none:
`05c_pullback_geometry.tex:15`, `:652` (the `fig:pb-pullback-naturality` caption),
`:791` (inside `thm:pb-fisher-defect-cocycle`), `06_general_coarsegraining.tex:202`,
`08_infogeometry.tex:512`. Confirmed on the bytes by direct search. Theorem II.6(3)
is the criterion that replaces it.

### II.4 Ordered composition of anomalies

**Theorem II.7 (ordered composition).** For
$E_0\xrightarrow{\Psi_{01}}E_1\xrightarrow{\Psi_{12}}E_2$ over
$f_{01},f_{12}$, with $\Psi_{02}=\Psi_{12}\Psi_{01}$, $f_{02}=f_{12}f_{01}$:

$$
A_{\Psi_{02}}(e;X)=T^V\Psi_{12}\big|_{\Psi_{01}(e)}\big(A_{\Psi_{01}}(e;X)\big)
+A_{\Psi_{12}}\big(\Psi_{01}(e);\,T_cf_{01}X\big).
\tag{II.3}
$$

*Proof.* Expand $T\Psi_{01}(H^{\omega_0}_eX)=H^{\omega_1}_{\Psi_{01}e}(Tf_{01}X)+A_{\Psi_{01}}(e;X)$,
apply $T\Psi_{12}$, use Theorem II.1's first display at the second stage on the
horizontal summand and verticality preservation on the vertical summand, then apply
$\operatorname{ver}^{\omega_2}$. $\square$

**Order matters and the naive sum is a type error.** $A_{01}$ takes values in
$V\bar E_1$ and $A_{12}$ in $VE_2$; $A_{02}=A_{01}+A_{12}$ does not typecheck. The
earlier anomaly is pushed by the **later** vertical differential; the later anomaly
is evaluated at the **image point** and on the **pushed** base vector. The
corresponding domain refinement: $A_{\Psi_{02}}=0$ needs $A_{\Psi_{01}}=0$ on
$T\mathcal C_0$ and $A_{\Psi_{12}}=0$ only on the sub-bundle
$Tf_{01}(T\mathcal C_0)\subseteq T\mathcal C_1$ at the points $\Psi_{01}(e)$.

At the connection level (II.3) is
$\mathfrak A_{\mathcal P_{02}}=\mathcal P_{01}^*\mathfrak A_{\mathcal P_{12}}+d\kappa_{12}\circ\mathfrak A_{\mathcal P_{01}}$,
which descends to $\mathfrak a_{02}=f_{01}^*\mathfrak a_{12}+d\kappa_{12}\circ\mathfrak a_{01}$,
consistent via $T^V\Psi_{12}\circ\vartheta=\vartheta\circ d\kappa_{12}$.

**Verification (Part XI, Block 2).** On the three-level instance ($f_{01}(x)=2x$,
$f_{12}(y)=3y$, abelian translation group, $A_{\omega_0}=0$, $A_{\omega_1}=a_1dy$,
$A_{\omega_2}=a_2dz$): $\mathfrak a_{01}=2a_1$, $\mathfrak a_{12}=3a_2-a_1$,
$\mathfrak a_{02}=6a_2$, and $2a_1+2(3a_2-a_1)=6a_2$ identically in $(a_1,a_2)$.

### II.5 The corrected sharp base cocycle — derived from first principles

**The vertical cocycle is unconditional.**

$$
\Delta_F^{\Psi_{12}\circ\Psi_{01}}=\Delta_F^{\Psi_{01}}+(T^V\Psi_{01})^*\Delta_F^{\Psi_{12}},
\tag{II.4}
$$

by adding and subtracting $(T^V\Psi_{01})^*g_1^F$ in
$g_0^F-(T^V\Psi_{01})^*(T^V\Psi_{12})^*g_2^F$. This is
`eq:pb-fisher-defect-cocycle` (`05c_pullback_geometry.tex:788`) and is certified.

**Theorem II.8 (base cocycle: exact residual and sharp criterion).** With
$s_0,s_1,s_2$ related at each stage, $\delta_{jk}:=(D^{\omega_j}s_j)^*\Delta_F^{\Psi_{jk}}$,
$v_X:=T^V\Psi_{01}(D^{\omega_0}s_0X)$, $A_X:=A_{\Psi_{01}}(s_0;X)$, and
$\bar u_X:=D^{\omega_1}s_1(T f_{01}X)=v_X+A_X$, the residual
$\mathcal N:=\delta_{02}-\delta_{01}-f_{01}^*\delta_{12}$ satisfies the following
**three equivalent exact forms**:

$$
\mathcal N(X,Y)=\Delta_F^{\Psi_{12}}(v_X,v_Y)-\Delta_F^{\Psi_{12}}(\bar u_X,\bar u_Y)
\tag{II.5a}
$$
$$
=-\Big[\Delta_F^{\Psi_{12}}\big(\bar u_X,A_Y\big)+\Delta_F^{\Psi_{12}}\big(A_X,\bar u_Y\big)\Big]
\;{\color{green}+}\;\Delta_F^{\Psi_{12}}\big(A_X,A_Y\big)
\tag{II.5b}
$$
$$
=-\Big[\Delta_F^{\Psi_{12}}\big(v_X,A_Y\big)+\Delta_F^{\Psi_{12}}\big(A_X,v_Y\big)\Big]
\;{\color{red}-}\;\Delta_F^{\Psi_{12}}\big(A_X,A_Y\big).
\tag{II.5c}
$$

Consequently the **sharp base cocycle**
$\delta_{02}=\delta_{01}+f_{01}^*\delta_{12}$ holds **if and only if**

$$
\boxed{\;\big\|T^V\Psi_{01}D^{\omega_0}s_0X\big\|_{\Delta_F^{\Psi_{12}}}
=\big\|D^{\omega_1}s_1(Tf_{01}X)\big\|_{\Delta_F^{\Psi_{12}}}\quad\text{for every }X,\;}
\tag{II.6}
$$

equivalently $\Delta_F^{\Psi_{12}}\big(A_X,\,2v_X+A_X\big)=0$, equivalently
$\Delta_F^{\Psi_{12}}\big(A_X,\,2\bar u_X-A_X\big)=0$, for every $X$.

*Proof.* Apply $(D^{\omega_0}s_0)^*$ to (II.4):
$\delta_{02}=\delta_{01}+(D^{\omega_0}s_0)^*(T^V\Psi_{01})^*\Delta_F^{\Psi_{12}}$, and
the last term is $\Delta_F^{\Psi_{12}}(v_X,v_Y)$. By definition
$f_{01}^*\delta_{12}(X,Y)=\Delta_F^{\Psi_{12}}(\bar u_X,\bar u_Y)$. Subtracting gives
(II.5a). Substituting $\bar u=v+A$ in the second term of (II.5a) and expanding gives
(II.5c); substituting $v=\bar u-A$ in the first term gives (II.5b). (II.6) is (II.5a)
on the diagonal, and $\mathcal N$ is symmetric, so vanishing on the diagonal is
vanishing. The two bracketed reformulations are
$\Delta(v,v)-\Delta(v+A,v+A)=-\Delta(A,2v+A)$ and
$\Delta(\bar u-A,\bar u-A)-\Delta(\bar u,\bar u)=-\Delta(A,2\bar u-A)$. $\square$

**Corrected formula, and the exact size of the printed error.** The bundle route
prints (`task-10-bundle-pullback-analysis.md:976-983`) the **hybrid**: the cross
terms of (II.5c), with the fine pushed jet $L_{01}D^{\omega_0}s_0$ in both slots,
together with the $+$ sign of (II.5b) on the quadratic term. That is neither form.
Its excess is exactly

$$
\text{printed}-\mathcal N=2\,\Delta_F^{\Psi_{12}}\big(A_{\Psi_{01}}(s_0;\cdot),A_{\Psi_{01}}(s_0;\cdot)\big),
$$

**two copies of the second-arrow (coarse) vertical Fisher defect evaluated on the
first-arrow horizontal defect.** The falsifier's characterization is confirmed
exactly. Both corrections named at `:167-170` — flip the sign, or swap the cross
arguments to the coarse jet — produce a correct identity, and they produce the
*same* identity; the consistency check the falsifier asks for is II.5b $\equiv$
II.5c, proved above and verified symbolically in Part XI, Block 1.

**Sufficient conditions for (II.6), in decreasing strength.**

| # | Condition | Reading |
| --- | --- | --- |
| S1 | $A_{\Psi_{01}}(s_0;\cdot)=0$ | stage-one anomaly vanishes (Theorem II.6(3) at stage one) |
| S2 | $\Delta_F^{\Psi_{12}}=0$ | the second arrow is Fisher-lossless |
| S3 | $A_X\in\operatorname{rad}\Delta_F^{\Psi_{12}}$ for every $X$ | **the stage-one anomaly is invisible to the stage-two information loss** |

S3 is strictly weaker than S1 and S2 and is new: $\mathcal N$ is a linear expression
in $\Delta_F^{\Psi_{12}}A$ (Part XI, Block 1), so it vanishes whenever that product
does. None of S1–S3 is necessary: (II.6) is an equality of seminorms and admits
accidental solutions.

**Interpretation needs more than the cocycle (a separation the manuscript does not
make).** Reading $\delta_{12}$ as $h_1-f_{12}^*h_2$ additionally requires
$A_{\Psi_{12}}(s_1;\cdot)=0$ by Theorem II.2 at stage two. So the **cocycle** needs
only stage-one compatibility, while the **additive-decomposition-of-information-loss
reading** needs stage-two compatibility as well. `thm:pb-fisher-defect-cocycle`
(`05c:779-795`) currently asserts both under the single undefined phrase "if the
connections are compatible".

### II.6 A genuine symbolic/type-level check of the corrected sharp statement

The falsifier's **M-2** is upheld: the bundle route's Block C
(`task-10-bundle-pullback-analysis.md:1925-1956`) evaluates
$\mathcal E_{jk}:=h_j-f_{jk}^*h_k$, not $\delta_{jk}:=(D^{\omega_j}s_j)^*\Delta_F^{\Psi_{jk}}$,
so its headline identity is the *unconditional telescoping*
$\mathcal E_{02}=\mathcal E_{01}+f_{01}^*\mathcal E_{12}$ — a tautology in
$(a_1,a_2)$, and no test of the sharp cocycle. Under the R3.3 definition,
$\delta_{\Psi_{01}}=\tfrac12$ independently of $a_1$, whereas Block C's
$\delta_{01}$ at $a_1=1/10$ is $7/25$. Confirmed by reproducing all three of Block
C's displayed polynomials from $h_j-f^*_{jk}h_k$ exactly.

**Replacement check, at two levels.**

*Type level (Part XI, Block 1).* With $\Delta_F^{\Psi_{12}}$ a symbolic symmetric
$3\times3$ form $D$, and $V,A$ symbolic $3\times2$ matrices representing $v_\bullet$
and $A_\bullet$ on a two-dimensional fine base, all of the following are verified as
identities of $2\times2$ symbolic matrices, with no numerical substitution:

- $\mathcal N=V^{\!\top}DV-(V{+}A)^{\!\top}D(V{+}A)$ equals form (II.5b): **True**;
- equals form (II.5c): **True**;
- equals the printed hybrid: **False**;
- $\text{printed}-\mathcal N=2A^{\!\top}DA$: **True**;
- $\mathcal N(X,X)=-\langle A_X,2v_X+A_X\rangle_D=-\langle A_X,2\bar u_X-A_X\rangle_D$: **True**;
- $\mathcal N\equiv0$ under S1, under S2, and under S3 ($DA=0$): **True, True, True**.

*Instance level (Part XI, Block 2).* On the bundle route's own Block B data, in
exact rational arithmetic: $\mathcal N=-\tfrac23a_1(a_1+1)$; printed
$=+\tfrac23a_1^2-\tfrac23a_1$; difference $=\tfrac43a_1^2=2\Delta_F^{\Psi_{12}}(A,A)$.
At $a_1=1/10$, $a_2=0$: $\mathcal N=-11/150$, printed $=-3/50$. Zero set
$\{0,-1\}$. At $a_1=-1$ the equal-seminorm criterion (II.6) is verified directly
($v=1$, $\bar u=-1$, $|v|_{\Delta}=|\bar u|_{\Delta}$), so **(II.6) holds with
$A_{\Psi_{01}}=-2\ne0$**: S1 is sufficient and not necessary, exactly as II.8
predicts and as the falsifier noted in passing.

---

## Part III — Score, action quotient, and the extensive replication operator

This part discharges brief item 3 and resolves the falsifier's **M-3**.

### III.1 The three operators, typed apart

Fix a scale with base law $\pi$ on $\mathsf X$ and a normalized parameter-independent
Markov kernel $K$ with $\pi^c:=\pi K$.

| Operator | Type | Norm | Direction |
| --- | --- | --- | --- |
| $\mathscr S_\pi[\varphi]=-(\varphi-\pi\varphi)$ | $L^2(\pi)/\mathbb R\mathbf 1\to L^2_0(\pi)$ | isometry for $\|\cdot\|_F$, **onto** | within one scale |
| $U\varphi=\mathbb E_{\pi\otimes K}[\varphi(X)\mid Z]$; $R:=U|_{L^2_0}$ | $L^2(\pi)\to L^2(\pi^c)$ | $\|R\|\le1$ | fine $\to$ coarse |
| $\mathscr I_b\,h=\sum_{i=1}^b h(x_i)$ | $L^2_0(\pi)\to L^2_0(\pi^{\otimes b})$ | $\|\mathscr I_b\|=\sqrt b>1$ | **coarse $\to$ fine (a lift)** |

**Proposition III.1 (the score/action square (D8) commutes).** $U\mathbf 1=\mathbf 1$,
$U(\varphi+c)=U\varphi+c$, and $\pi^c(U\varphi)=\pi(\varphi)$ by the tower property.
Hence $U$ descends to $\overline U$ on the quotients and

$$
\mathscr S_{\pi^c}\big[\overline U[\varphi]\big]
=-\big(U\varphi-\pi^c(U\varphi)\big)=-\big(U\varphi-\pi\varphi\big)=U\,\mathscr S_\pi[\varphi].
$$

Restricted to $L^2_0(\pi)$, $U$ **is** the operator $R$ of the DQM pushforward
theorem. Consequently the action-tier restriction and the score-tier pushforward are
one operator seen through the isometry $\mathscr S$, and

$$
\|[\varphi]\|_F^2-\|\overline U[\varphi]\|_F^2
=\|h\|^2_{L^2(\pi)}-\|Uh\|^2_{L^2(\pi^c)}
=\mathbb E\operatorname{Var}\big(h(X)\mid Z\big)\ \ge 0,\qquad h=\mathscr S_\pi[\varphi].
$$

**Corollary III.2 (a normalized Markov channel cannot increase Fisher).** $R$ is a
conditional expectation followed by restriction to a sub-$\sigma$-algebra, hence an
$L^2$ contraction; the Fisher form of the pushed family is $\|Rh\|^2\le\|h\|^2$. This
is unconditional given (H1)–(H4) and does **not** require standard Borel.

### III.2 Where the $\sqrt b$ replication norm belongs, and where it is forbidden

**Proposition III.3.** $\|\mathscr I_b h\|^2_{L^2(\pi^{\otimes b})}=b\|h\|^2_{L^2(\pi)}$
for centered $h$, by independence and centering; so $b^{-1/2}\mathscr I_b$ is an
isometry and $\|\mathscr I_b\|=\sqrt b$.

**Proposition III.4 (no Markov realization; the forbidden use).** There is **no**
parameter-independent normalized Markov kernel $K$ with
$\mathcal N(x,1)K=\mathcal N(x\mathbf 1_b,I_b)$ for all $x$, for any $b\ge2$.

*Proof.* The input family is DQM with Fisher information $1$; if such a $K$ existed,
Theorem II.5's transfer plus the law of total variance would force the output Fisher
information $b$ to satisfy $b\le1$. $\square$

**Placement.** The factor $\sqrt b$ belongs to exactly two places, and to no others:

1. **The reference identification $i_\ell:\mathcal A_\ell\to\mathcal A_*$ of
   `H-REFERENCE`.** Comparing a single-site score with an extensive block score is a
   change of reference tangent space, not a channel. $\mathscr I_b$ is the lift; its
   norm records how much the identification rescales.
2. **The declared configuration metric.** Replicating an experiment multiplies
   $\mathsf G_\ell$ by $b$. That is a re-declaration of $\mathsf G$, which by
   `configuration-fisher-metric` is separately declared data.

**Forbidden.** $\{\mathcal N(x\mathbf 1_4,I_4)\}$ versus $\{\mathcal N(x,1)\}$ may
**not** be cited as a Markov-contraction counterexample or as evidence that "Fisher
increased along a coarse-graining arrow". By Proposition III.4 there is no arrow.
What the pair *does* witness is `CE-DURATION-MISMATCH`: two legitimately declared
configuration metrics related by a lift, for which coarse Fisher duration exceeds
fine Fisher duration with **zero** information loss. That is a statement about metric
declarations (Part VI.5, mechanism 1), and it is compatible with Corollary III.2 because the
composite $\mathscr L_b=U_b\mathscr I_b$ has $\|\mathscr L_b\|\le\sqrt b$, not $\le1$.

**Both routes state this correctly** (`task-10-score-configuration-analysis.md:1157-1165`;
`task-10-timeless-history-analysis.md:857-892`), and the falsifier rejected the attack
on this point. Recorded here as settled, with the nonexistence argument supplied.

### III.3 The bounded chart and the Fisher tangent are different objects — with a valid witness

On $L^2(\pi)/\mathbb R\mathbf 1$ the map $\varphi\mapsto-(\varphi-\pi\varphi)$ is a
surjective isometry onto $L^2_0(\pi)$ (given $h\in L^2_0$ take $\varphi=-h$), and
every class is realized as a two-sided DQM score by the **quadratic** path
$p_t=(1+th/2)^2/(1+at^2)$ of `lem:rg-dqm-realization` (`07b_agent_network_rg.tex:559`).
This is what `score-action-compatibility` asserts, and it is true.

It is a *different* statement from `prop:rg-action-score-isometry`
(`07b:762`), which concerns the **exponential-action** path
$\widehat\pi^{t\varphi}=e^{-t\varphi}\pi/\pi(e^{-t\varphi})$, defined only where the
normalizer is finite. Separating the two needs a witness with **no** two-sided
exponential-action neighborhood.

**M-3 sustained; witness replaced.** The score route's restatement
(`task-10-score-configuration-analysis.md:432-436`) says that for $\pi=\mathcal N(0,1)$
and $\varphi(x)=-x^2$ "no two-sided neighborhood exists". That is **false**:
$\pi(e^{tx^2})=(1-2t)^{-1/2}$, finite for every $t<1/2$ and in particular on the
two-sided $(-1/2,1/2)$; at $t=-1/4$ the value is $\sqrt6/3$ and at $t=1/4$ it is
$\sqrt2$ (Part XI, Block 11). The report contradicts itself nine lines later by
correctly citing `prop:ig-hermite-exponential-domain` (`08_infogeometry.tex:364-396`),
which gives $N_2(t)=e^t(1+2t)^{-1/2}$ finite for every $t>-\tfrac12$. The register
entry `counterexample-register.md:11` is **not** at fault: it asserts only
nonintegrability of $e^{x^2}$, which is the true $t=1$ statement.

**Correct witness (odd Hermite of degree $\ge3$).** Take
$\varphi=\mathrm{He}_3(x)=x^3-3x\in L^2_0(\gamma)$. For $t>0$,
$-t\,\mathrm{He}_3(x)-x^2/2\to+\infty$ as $x\to-\infty$ (the cubic dominates the
Gaussian quadratic); for $t<0$ the same happens as $x\to+\infty$. Hence
$N_3(t)=\int e^{-t\mathrm{He}_3}\,d\gamma=+\infty$ for **every** $t\ne0$: the
exponential-action path exists at no $t\ne0$, while $\mathrm{He}_3\in L^2_0(\gamma)$
is a perfectly good Fisher tangent direction realized by the quadratic path. This is
exactly the case `prop:ig-hermite-exponential-domain` already supplies. Part XI,
Block 11 exhibits the divergence numerically on $[-80,20]$ for $t\in\{1/2,1/10,1/100\}$.

**Repair of the register entry.** `CE-ACTION-LP` should read: "$\varphi=\mathrm{He}_k$
with $k\ge3$ odd lies in $L^2_0(\gamma)$ and has $N_k(t)=+\infty$ for every $t\ne0$,
so the nonlinear bounded-action chart is undefined in that Fisher direction. The
$\mathrm{He}_2$ direction $\varphi=-x^2$ is **not** such a witness: its normalizer is
finite exactly on $t>-1/2$, a one-sided-unbounded but two-sided-nonempty domain."

### III.4 The two norms on the bounded quotient

$\|[\varphi]\|_F\le\|[\varphi]\|_{\mathrm{osc}}$, strictly in general, because
$\inf_c\|\varphi-c\|_2\le\inf_c\|\varphi-c\|_\infty$. The oscillation norm controls
the nonlinear map of `thm:rg-bounded-action-calculus` (`07b:190`); the Fisher norm
controls the quadratic-mean tangent. **A spectral statement proved on $L^2_0$ is not
a statement about the nonlinear bounded-action chart, and conversely.** This
separation and Proposition III.4 together are the whole content of the "extensive
modes versus Markov contraction" reconciliation.

---

## Part IV — Closing the configuration-manifold interface

This part discharges brief item 4 and resolves the falsifier's **M-7** and the
missing lemmas **L-CFM** and **L-CONFIG-NONEMPTY**. The construction is noncircular:
nothing below assumes the existence of a configuration manifold or of a strong metric.

### IV.1 Why the manuscript's declaration does not close the claim

`hyp:hist-regular-section-space` (`05d_relational_inference.tex:91`) and
`hyp:hist-regular-metric-domain` (`05d:204`) **declare** a configuration manifold and
a strong Fisher metric. A source-wide search finds no configuration manifold
exhibited anywhere and no strong-metric verification anywhere; the phrase "strong
metric" occurs once, inside the hypothesis. The only nonemptiness result in the
source, `prop:gauss-interaction-nonempty` (`06_gaussian.tex:307`), concerns the
Gaussian **interaction** family, a different object.

**M-7 sustained.** Route D closes `configuration-fisher-metric` PROVED on the
strength of its own standing hypothesis H-D1, which states the claim. That is
circular and must not enter the integration as third-route corroboration. Route D's
row is restated as "assumed, not established." The other two routes' `OPEN` stands
against the manuscript's declared objects.

### IV.2 Tier F — an explicit finite-dimensional family with a strong Gram metric

**Construction IV.1 (Tier F).** Declare, at scale $\ell$:

* **Base.** $\mathcal C_\ell$ a compact smooth manifold with a finite positive Borel
  measure $\mu_\ell$. (Witness: $\mathcal C_\ell=S^1$, $\mu_\ell$ normalized arclength.)
* **Bundle.** $P=\mathcal C_\ell\times G$ trivial with $G=(\mathbb R^K,+)$ acting on
  the mean by translation, $\omega$ the flat connection ($A\equiv0$).
* **Fiber.** $\mathcal B=\{\mathcal N(m,\Sigma_0):m\in\mathbb R^K\}$ with **fixed**
  $\Sigma_0\succ0$; fiber Fisher form the constant $g^F=\Sigma_0^{-1}$.
* **Sections.** Fix smooth $\phi_1,\dots,\phi_N:\mathcal C_\ell\to\mathbb R^K$ and set
  $$
  \mathcal Q_\ell:=\{s_\xi:\xi\in\mathbb R^N\},\qquad
  s_\xi(c)=\mathcal N\Big(\textstyle\sum_a\xi_a\phi_a(c),\;\Sigma_0\Big).
  $$
* **Weights.** A measurable $w:\mathcal C_\ell\to(0,\infty)$, bounded above and below.
* **Metric.** $\mathsf G_\ell(V,V):=\int_{\mathcal C_\ell}w(c)\,
  g^F\big(\partial_Vs_\xi(c),\partial_Vs_\xi(c)\big)\,\mu_\ell(dc)$, **labeled as the
  weighted product of marginal fiber metrics**, not as a joint-law pullback.

**Theorem IV.2.** Under Construction IV.1:

1. $\mathcal Q_\ell$ is a **nonempty** finite-dimensional smooth manifold
   diffeomorphic to $\mathbb R^N$; $\xi=0$ gives $c\mapsto\mathcal N(0,\Sigma_0)$.
2. $\mathsf G_\ell$ is the **constant Gram form** $\mathsf G_\ell=\Phi$ with
   $\Phi_{ab}=\int_{\mathcal C_\ell}\phi_a(c)^{\!\top}\Sigma_0^{-1}\phi_b(c)\,w(c)\,\mu_\ell(dc)$,
   independent of $\xi$; it is smooth and finite (compact base, bounded integrand).
3. $\mathsf G_\ell$ is a Riemannian metric **iff** $\{\phi_a\}$ are linearly
   independent in $L^2(w\mu_\ell;\Sigma_0^{-1})$; and any Riemannian metric on a
   finite-dimensional manifold is automatically **strong**, since every inner product
   on a finite-dimensional space induces the norm topology and the musical map is a
   linear isomorphism.
4. Every $C^1$ functional $\mathcal F_\ell$ on $\mathcal Q_\ell$ has a unique gradient
   $\Phi^{-1}\nabla\mathcal F_\ell$; the natural-gradient field
   $X_\ell=-\Phi^{-1}\nabla\mathcal F_\ell$ exists, is locally Lipschitz for
   $\mathcal F_\ell\in C^2$, and has locally unique integral curves.
5. The gauge orbit tangent (constant translations of the mean) is a linear subspace of
   $\mathbb R^N$, hence **automatically closed and complemented**, so the quotient-speed
   infimum of `eq:hist-quotient-gauge-speed` is attained and equals the orthogonal
   projection onto its $\Phi$-orthogonal complement.

*Proof.* 1: the fiber bundle is trivial and $s_\xi$ is smooth in $(c,\xi)$; the
parameter space is $\mathbb R^N$. 2: $\partial_Vs_\xi(c)=\sum_a v_a\phi_a(c)$ is
independent of $\xi$, so the integrand is the quadratic form $v^{\!\top}\Phi v$ with
$\Phi$ as displayed; finiteness is compactness plus boundedness of $w$. 3: $\Phi$ is
positive semidefinite, and $v^{\!\top}\Phi v=0$ forces $\sum_av_a\phi_a=0$ in
$L^2(w\mu_\ell;\Sigma_0^{-1})$ because $w>0$ and $\Sigma_0^{-1}\succ0$; strongness in
finite dimensions is the stated linear-algebra fact. 4: $\flat$ is the invertible
matrix $\Phi$. 5: linear subspaces of $\mathbb R^N$ are closed and complemented. $\square$

**Nondegeneracy is a counting condition, checkable in advance.** With
$\mu_\ell=\sum_{a=1}^M\rho_a\delta_{c_a}$ the Gram matrix has rank at most $MK$, so
whenever $N>MK$ the metric is degenerate and, by
`prop:hist-semidefinite-gradient-obstruction` (`05d:344`), the natural-gradient
equation has no solution or many. This sharpens the manuscript's remark at
`05d:485-489` from a warning into a rank test.

**Executed instance (Part XI, Block 6).** $\mathcal C_\ell=S^1$, $K=1$,
$\Sigma_0=1$, $w\equiv1$, $\mu$ normalized arclength,
$\{\phi_a\}=\{1,\cos\theta,\sin\theta\}$: $\Phi=\operatorname{diag}(1,\tfrac12,\tfrac12)$,
$\det\Phi=1/4$, eigenvalues $\{1,\tfrac12\}$, positive definite. $\mathcal Q_\ell\cong\mathbb R^3$.

### IV.3 The infinite-dimensional strong/weak boundary, retained

Tier F does not retire the infinite-dimensional analysis; it is retained verbatim as
the boundary of the closure.

* **(b1) $L^2$ tier, strong.** $\mathcal Q^{(b1)}=L^2(\mu;\mathbb R^K)$ with
  $\mathsf G^{L^2}(V,W)=\int V^{\!\top}\Sigma_0^{-1}W\,w\,d\mu$. If
  $0<w_-\le w\le w_+<\infty$ and $\lambda_-I\preceq\Sigma_0^{-1}\preceq\lambda_+I$
  then $w_-\lambda_-\|V\|^2_{L^2}\le\mathsf G^{L^2}(V,V)\le w_+\lambda_+\|V\|^2_{L^2}$,
  so $\flat$ is a topological isomorphism (Lax–Milgram, or Riesz after renorming) and
  the metric is **strong**, at the cost of requiring $\mathcal F$ to be $C^1$ on $L^2$
  — which excludes gradient-energy objectives. The two-sided bounds are exactly the
  boundedness and coercivity conditions; either failing alone destroys the conclusion.
* **(b2) $H^s$ tier with the same integrated metric, weak.** The topology of
  $\mathsf G^{L^2}$ is the $L^2$ topology, strictly coarser than $H^s$; $\flat$ is
  injective and bounded but not surjective. **Witness:** $\mathcal C=S^1$,
  $\mathcal Q=H^1(S^1)$, $\mathcal F(Q)=\tfrac12\int|Q'|^2$,
  $Q=\sum_{k\ge1}k^{-2}\sin k\theta$. Then $\|Q\|^2_{H^1}\asymp\sum k^{-2}<\infty$
  while a gradient would be $-Q''=\sum_k\sin k\theta$ with
  $\|\cdot\|^2_{L^2}\asymp\sum_k1=\infty$. **No natural-gradient vector field exists at
  $Q$.** The missing ingredient is Riesz representability of $d\mathcal F_Q$; the exact
  extra hypothesis is $d\mathcal F_Q\in\operatorname{ran}\flat$, sufficiently ensured by
  $|d\mathcal F_Q[V]|\le C_Q\|V\|_{L^2}$ on the dense domain.
* **Gauge quotient in the Hilbert tier.** With a strong metric and a **closed** orbit
  tangent the infimum is attained (orthogonal projection; complementedness is
  automatic in a Hilbertable space). **Witness for nonclosed:** $\mathcal Q=\ell^2$
  with $\mathcal G=h^1=\{v:\sum n^2v_n^2<\infty\}$ acting by translation is free and
  isometric with dense orbit tangent, so the quotient speed is identically zero and
  defines no clock. This witnesses only the *free and isometric* version; the
  manuscript's sentence at `05d:529-536` says "free, **proper**, and isometric is not
  by itself enough" and remains without a witness, since properness would force
  closed orbits. That gap is recorded, not repaired.
* **Redundancy note (falsifier M-12(e), decided).** Route D's N5 "closed **and
  complemented**" is redundant in the strong tier, where each tangent space is
  Hilbertable; it bites only in the weak/Banach tier. The falsifier is right.

**There is no third option in the infinite-dimensional case:** either $L^2$ with a
strong metric and a $C^1$-on-$L^2$ objective, or $H^s$ with the Riesz hypothesis
declared as a standing assumption together with the failure witness above.

### IV.4 Does this close `configuration-fisher-metric`?

The claim requires: *an explicitly selected finite-dimensional or Banach/Hilbert
section manifold*, and *a strong Fisher metric that is either the pullback of a
declared joint-law Fisher metric* **or** *a labeled weighted product metric with base
measure, channel weights, gauge quotient, finiteness, and nondegeneracy data*.

Tier F supplies the **second disjunct in full**:

| Required datum | Tier F |
| --- | --- |
| explicitly selected manifold | $\mathcal Q_\ell\cong\mathbb R^N$, nonempty (IV.2.1) |
| strong metric | automatic in finite dimensions (IV.2.3) |
| base measure | $\mu_\ell$, declared finite positive Borel |
| channel weights | $w_b,w_m$, declared, two-sidedly bounded |
| gauge quotient | closed orbit tangent, automatic (IV.2.5) |
| finiteness | compact base + bounded integrand (IV.2.2) |
| nondegeneracy | Gram invertibility, exactly (IV.2.3), rank-testable |
| **label** | declared as a weighted product, **not** as the joint Fisher metric |

**Verdict.** `configuration-fisher-metric` **closes** under the added declaration
**(H-CONFIG-F)**: *at every scale where a natural-gradient vector field or a Fisher
duration is asserted, the configuration manifold and metric are those of
Construction IV.1 (or of tier (b1) with its two-sided bounds).* Without such a
declaration it stays `OPEN`, because the manuscript exhibits nothing. This is a
**conditional closure with a nonempty model class**, which is exactly what a
`DECLARED_ASSUMPTION` needs in order not to be vacuous. **L-CFM is discharged for the
weighted-product branch; it remains open for the joint-law-lift branch**, which the
integrated stack does not use.

**The joint-law branch, and why the stack avoids it.** The exact comparison between
the joint pullback and the weighted product is

$$
\|L\|^2-\big(\|L_b\|^2+\|L_m\|^2\big)=\underbrace{\|L-L_b-L_m\|^2}_{\ \ge0}
-2\underbrace{\langle L_b,L_m\rangle}_{\text{signed}},
$$

with $L_b=\Pi_bL$, $L_m=\Pi_mL$ the orthogonal projections onto the centered
$\sigma(Y_b)$- and $\sigma(Y_m)$-measurable subspaces (marginalization is a
deterministic parameter-independent Markov kernel, so Theorem A applies). Each
marginal alone contracts, but **no Loewner ordering holds in either direction**: with
jointly Gaussian precision $\Lambda=\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)$,
$\Lambda-(1-\rho^2)I_2=\left(\begin{smallmatrix}\rho^2&\rho\\\rho&\rho^2\end{smallmatrix}\right)$
has $\det=\rho^2(\rho^2-1)<0$, giving $+2\rho(1+\rho)$ along $(1,1)$ and
$2\rho(\rho-1)$ along $(1,-1)$. Equality with unit weights holds **iff**
$\|L-L_b-L_m\|^2=2\langle L_b,L_m\rangle$; the clean sufficient structural condition
is independence, and under independence with nondegenerate marginals the weights are
forced to $w_b=w_m=1$ (given that the two marginal Fisher forms are independently
excitable — the falsifier's M-12(a) qualification, which holds in the Gaussian
instance). A fixed non-independence copula does **not** suffice, since
$\partial_\zeta\log c(F^b_\zeta,F^m_\zeta)$ is generally nonzero. Two right inverses
of the same configuration extraction give different metrics, so **the configuration
Fisher metric is not a function of the displayed configuration**; the lift is data.
The stack therefore uses the labeled weighted product and states the equality
criterion, rather than asserting the joint pullback.

---

## Part V — Projectability, the separately declared coarse configuration map, and the exact averaging defect

This part discharges brief item 5 and resolves **M-4**, **M-5**, **M-8**,
**L-AVG**, **L-CM**, and **L-CONFIG-NONEMPTY**.

### V.1 Sharp projectability, with smoothness proved rather than assumed

**Theorem V.1.** Let $f:\mathcal C\to\bar{\mathcal C}$ be a surjective smooth
submersion, $\Psi:E\to\bar E$ a smooth bundle morphism over $f$, and
$Q\in\Gamma(\mathcal C,E)$. Consider

* **(P1)** $\exists\,\bar Q\in\Gamma(\bar{\mathcal C},\bar E)$ with $\Psi Q=\bar Qf$;
* **(P2)** $\Psi\circ Q$ is constant on each fiber of $f$;
* **(P3)** $T^V\Psi\big(D^\omega Q(X)\big)+A_\Psi\big(Q(c);X\big)=0$ for every $c$ and
  every $X\in\ker T_cf$.

Then (P1)$\Leftrightarrow$(P2)$\Rightarrow$(P3), and (P3)$\Rightarrow$(P2) when the
fibers of $f$ are connected. Under (P2), $\bar Q$ is unique, is **automatically
smooth**, and is automatically a section.

*Proof.* (P1)$\Rightarrow$(P2) is immediate. (P2)$\Rightarrow$(P1): a surjective
smooth submersion is a smooth quotient map, so a smooth map constant on its fibers
descends uniquely and smoothly; uniqueness is surjectivity; and
$\bar\varpi\bar Qf=\bar\varpi\Psi Q=f\varpi Q=f$ with $f$ surjective gives
$\bar\varpi\bar Q=\mathrm{id}$. (P2)$\Rightarrow$(P3): for $X\in\ker T_cf$, split
$T_cQX=H^\omega_{Q(c)}X+D^\omega Q(X)$, apply $T\Psi$, and use $T_cfX=0$ to kill the
horizontal term, leaving $T(\Psi Q)(X)=A_\Psi(Q(c);X)+T^V\Psi(D^\omega Q(X))$, which
constancy forces to vanish. (P3)$\Rightarrow$(P2): the same computation shows
$T(\Psi Q)$ annihilates $\ker Tf$; a smooth map with vanishing derivative along a
connected embedded submanifold is constant on it. $\square$

**Two hedges discharged, one sharpness witness.** (i) `05c_pullback_geometry.tex:588`
lists "smoothness of the descended factor" as an open descent obligation. Under the
stated submersion hypothesis it is a **theorem**, not an obligation, and the hedge
should be discharged. (ii) The submersion hypothesis is load-bearing:
$\mathcal C=\bar{\mathcal C}=\mathbb R$, $f(x)=x^3$ (smooth bijection, not a submersion
at $0$), trivial bundle with $\mathcal B=\{\mathcal N(\mu,1)\}$, $\Psi=\mathrm{id}$ on
fibers, $Q(x)=\mathcal N(x,1)$: the unique descent $\bar Q(y)=\mathcal N(y^{1/3},1)$ is
continuous but not differentiable at $0$.

**Theorem V.2 (a pointwise bundle morphism is not a map on configurations).** With
$f$ a surjective submersion, $c_0$ with $\ker T_{c_0}f\ne0$, and some $e_0\in E_{c_0}$,
$w\in V_{e_0}E$ with $T^V\Psi(w)\ne0$, and $\Gamma(\mathcal C,E)\ne\varnothing$ with
$\mathcal B$ **connected** (so that a global section can be adjusted to pass through
$e_0$ — the falsifier's M-12(c), adopted), the projectable set
$\Gamma_{\mathrm{proj}}(\Psi)$ is a **proper** subset of $\Gamma(\mathcal C,E)$.

*Proof.* Frobenius gives a chart with $\ker Tf=\operatorname{span}\{\partial_1,\dots,\partial_k\}$,
$k\ge1$. Take $Q_0$ through $e_0$; if it is not projectable we are done. Otherwise let
$W$ be a smooth field on $\mathcal B$ with $W(\beta_0)=w$ and local flow $\Phi^W$, and
let $\chi\in C^\infty_c$ with $\chi(c_0)=0$, $\partial_1\chi(c_0)\ne0$. Set
$\beta_\epsilon(c)=\Phi^W_{\epsilon\chi(c)}(\beta_0(c))$. Since $\chi(c_0)=0$, both
$A_\Psi(Q_\epsilon(c_0);\partial_1)$ and $T^V\Psi$ at that point are
$\epsilon$-independent, and
$\tfrac{d}{d\epsilon}\big|_0\big[T^V\Psi(D^\omega Q_\epsilon\partial_1)+A_\Psi(Q_\epsilon(c_0);\partial_1)\big]
=\partial_1\chi(c_0)\,T^V\Psi(w)\ne0$, so (P3) fails for small $\epsilon\ne0$. $\square$

**Witness.** $\mathcal C=S^1$, $\bar{\mathcal C}=\{*\}$ (note $f$ **is** a surjective
submersion), trivial bundles with the unit-variance Gaussian location fiber,
$\Psi=\mathrm{id}$ on fibers, $Q(x)=\mathcal N(\sin x,1)$: $A_\Psi=0$, $\ker Tf=TS^1$,
$T^V\Psi(D^\omega Q\partial_x)=\cos x\,\partial_\mu\not\equiv0$, so no coarse section
exists. In the linear tier $\mathcal Q=L^2(S^1)$ the descendable set is exactly the
constants: a closed subspace of infinite codimension with **empty interior**.

**Scope correction (falsifier N-3, decided).** The score route's upgrade to "on a
genuinely infinite-dimensional configuration manifold it induces one nowhere"
overreaches: if $f$ is a diffeomorphism every section descends. The correct, scoped
statement is the one above, for a **collapsing** $f$ in the $L^2$ tier. Only the
scoped form may be transcribed.

**Two channels are independent.** Take the $S^1$ collapse in both channels; a belief
kernel sending every sample to one point makes $T^V\Psi_b=0$, so every belief section
is projectable, while an identity model kernel with $s(x)=\mathcal N(\sin x,1)$ is not
projectable. Exchanging roles gives the converse. A meta-agent therefore exists only
when **both** channel conditions (P2) hold.

### V.2 Retiring L-CM: declare the configuration coarse map separately

The pointwise-induced route requires **L-CM** — that
$\Gamma_{\mathrm{proj}}(\Psi)\cap\mathcal Q_\ell$ be a smooth submanifold with a smooth
induced map — which needs a transversality or elliptic-regularity hypothesis that no
route supplies, and which V.2's empty-interior result makes harder rather than easier.

**Decision.** The integrated stack does **not** use the pointwise-induced map as its
configuration coarse map. It follows the brief's own preference: a **separately
declared smooth coarse configuration map $\mathsf R_\ell$, with its metric
compatibility carried as an explicit hypothesis discharged by a theorem.** L-CM is
thereby retired from the load-bearing path; it survives only as an optional refinement
for anyone who insists on the pointwise route. Diagram (D7) records that the two maps
agree exactly on $\Gamma_{\mathrm{proj}}(\Psi)\cap\mathcal Q_\ell$.

**Symbol decision, against both prior recommendations.** The score route (`:1303`)
and the falsifier (M-8 minimal repair) both recommend renaming the configuration
coarse map to $\widehat R_\ell$. **That symbol is already taken.** On the current
bytes, `07b_agent_network_rg.tex:2196` reads "With $\widehat R_\ell=J_\ell^{-1}R_\ell J_\ell$
for the bounded idempotent retained projections", and $\widehat R_k$ recurs at
`07b:1275, 2198, 2201, 2211, 2227, 2240, 2241, 2251` as the reference-space-conjugated
retained-interaction projection. Adopting that recommendation would replace one
collision with another. Verified by direct search:
`\mathsf{R}`, `\mathfrak{r}`, `\mathfrak{q}`, and `\mathsf{C}` occur **zero** times in
`manuscripts/gauge_vfe_rg/*.tex`.

> **Adopt $\mathsf R_\ell:\mathcal Q_\ell\to\mathcal Q_{\ell+1}$** (upright sans-serif),
> with a notation-appendix row typing it and recording its non-identification with
> $K_\ell$, $\mathcal R^H$, $\mathcal R_b$, $M_\ell$, $C_{\ell,s}$,
> $\widehat{\mathcal R}_\ell$, $\widehat R_\ell$, $\Psi$, the root-vertex set
> $\mathcal R$, and the descent ray $\mathcal R^-_{\mathcal F_i}$.

**M-8 confirmed and extended.** The symbol $\mathcal R$ currently carries six
assignments: root-vertex set (`04_generative.tex:22`, used at `05_elbo.tex:388-434`);
VFE descent ray (`05d:287`); configuration coarse map (`05d:719-783`); nonlinear
action map $\mathcal R^H$ (`07b:185`); block measure-pair map $\mathcal R_b$
(`07b:2074`); reference-space endomorphism $\widehat{\mathcal R}_\ell$
(`07_general_renormalization.tex:45-48`). `appendix_notation.tex` has **no** row of
type $\mathcal Q_\ell\to\mathcal Q_{\ell+1}$. Route D's "PROVED (typing)" is
contradicted on the bytes; **`configuration-map`'s notation conjunct is currently
false**, and no derivation can close it — only an edit can.

### V.3 Theorem AVG — the exact averaging defect, with the hypothesis that excludes M-5

**M-5 sustained and reproduced.** With base $\{c_1,c_2\}$, $\kappa$ uniform, unit
weights, $\Psi=\mathrm{id}$ so $\Delta_F^\Psi\equiv0$, centered Gaussian fiber
$\{\mathcal N(0,\Sigma)\}$ in the **moment chart** with $g^F(A,A)=A^2/(2\Sigma^2)$,
configuration $(\Sigma_1,\Sigma_2)=(1,\delta)$ and tangent $Z=(1,0)$: the fine
integrated metric is $\tfrac14$ and the chart-barycenter image metric is
$1/\big(2(1+\delta)^2\big)\to\tfrac12$. At $\delta=10^{-2}$ the coarse/fine ratio is
$5000/10201=1.9605921$ (Part XI, Block 4). Generic averaging **is not** a contraction.

**Mechanism, corrected.** The obstruction is failure of joint convexity of the fiber
Fisher form in the chart. For $F(\Sigma,A)=A^2/(2\Sigma^2)$ the Hessian determinant is
$-A^2\Sigma^{-6}<0$ for $A\ne0$. (The falsifier reports $-4A^2\Sigma^{-6}$; the
correct coefficient is $-1$, verified symbolically. The sign, and hence the
conclusion, is unaffected.) By contrast the law-chart integrand
$G(p,\dot p)=\dot p^2/p$ has Hessian
$\left(\begin{smallmatrix}2\dot p^2/p^3&-2\dot p/p^2\\-2\dot p/p^2&2/p\end{smallmatrix}\right)$
with determinant $0$ and trace $2/p+2\dot p^2/p^3>0$: positive semidefinite, so
**jointly convex on $p>0$**.

**Hypothesis (JC).** In the declared affine chart, the map
$(\bar\beta,v)\mapsto\bar g^F_{\bar\beta}(v,v)$ is jointly convex on
$\bar{\mathcal B}\times\bar W$. **(JC-const)** is the special case in which
$\bar g^F$ is constant in the chart.

**Theorem V.3 (AVG — exact defect and contraction).** Assume

* **(A-i)** $f:\mathcal C\to\bar{\mathcal C}$ measurable between standard Borel spaces,
  $\mu$ finite positive on $\mathcal C$, $\bar\mu:=f_\#\mu$, and $\{\kappa_{\bar c}\}$ a
  disintegration of $\mu$ over $f$;
* **(A-ii)** $\bar{\mathcal B}$ convex in a locally convex $\bar W$, the structure group
  acting by restrictions of linear maps, and $\Psi$ acting fiberwise as the restriction
  of a continuous **affine** map with linear part $L$; the integrand Bochner integrable,
  and for a non-closed convex target such as $\operatorname{Sym}^{++}_K$ the barycenter
  lies in the set by strict positivity, $v^{\!\top}(\int\Sigma d\kappa)v=\int v^{\!\top}\Sigma v\,d\kappa>0$;
* **(A-iii)** hypothesis **(JC)**;
* **(A-iv)** fiberwise Fisher contraction $\Delta_F^\Psi=g^F-L^*\bar g^FL\succeq0$
  (automatic under the Markov hypotheses of Theorem II.5);
* **(A-v)** $\bar w\circ f\le w$ with $w,\bar w>0$ measurable, all integrals finite.

Define $\big(\mathsf R s\big)(\bar c):=\int_{f^{-1}(\bar c)}\Psi\big(s(c)\big)\,\kappa_{\bar c}(dc)$.
Then $\mathsf Rs$ is a genuine section, $\mathsf R$ is gauge equivariant (the transition
maps act linearly, so the value is trivialization independent), and for every
$Z\in T_s\mathcal Q_\ell$

$$
\Delta_{\mathrm{avg}}(Z):=\int_{\mathcal C}w\,g^F_{s(c)}(Z,Z)\,d\mu
-\int_{\bar{\mathcal C}}\bar w\,\bar g^F_{(\mathsf Rs)(\bar c)}\big(T\mathsf RZ,T\mathsf RZ\big)\,d\bar\mu
\;\ge\;0 .
$$

Under the stronger **(JC-const)** the defect is **exact**:

$$
\boxed{\;
\Delta_{\mathrm{avg}}(Z)=
\underbrace{\int_{\mathcal C}w\,\Delta_F^{\Psi}(Z,Z)\,d\mu}_{\text{channel loss}}
+\underbrace{\int_{\mathcal C}\big(w-\bar w\circ f\big)\big(L^*\bar g^F\big)(Z,Z)\,d\mu}_{\text{weight gap}}
+\underbrace{\int_{\bar{\mathcal C}}\bar w\,\operatorname{Var}^{\bar g^F}_{\kappa_{\bar c}}\!\big(LZ\big)\,d\bar\mu}_{\text{context (Jensen) gap}} ,\;}
$$

with $\operatorname{Var}^{\bar g}_{\kappa}(V)=\int\bar g(V,V)d\kappa-\bar g\big(\int Vd\kappa,\int Vd\kappa\big)\ge0$,
and each of the three terms nonnegative under (A-iv), (A-v), and $\bar g^F\succeq0$
respectively.

*Proof.* $T\mathsf RZ(\bar c)=\int LZ(c)\,\kappa_{\bar c}(dc)$ by affineness, and
$(\mathsf Rs(\bar c),T\mathsf RZ(\bar c))$ is the $\kappa_{\bar c}$-barycenter of
$(\Psi s(c),LZ(c))$. Under (JC), Jensen gives
$\bar g^F_{\mathsf Rs(\bar c)}(T\mathsf RZ,T\mathsf RZ)\le\int\bar g^F_{\Psi s(c)}(LZ,LZ)\,d\kappa_{\bar c}$.
Multiply by $\bar w$, integrate against $\bar\mu$, and use the disintegration
$\int_{\bar{\mathcal C}}\int_{f^{-1}(\bar c)}(\cdot)\,d\kappa_{\bar c}\,d\bar\mu=\int_{\mathcal C}(\cdot)\,d\mu$
to get $\int(\bar w\circ f)(L^*\bar g^F)(Z,Z)\,d\mu$, then apply (A-v) and (A-iv). For
the exact identity, with $\bar g^F$ constant the Jensen step is an equality minus the
variance term, and expanding $g^F=\Delta_F^\Psi+L^*\bar g^F$ separates the channel and
weight terms. $\square$

**This is L-AVG, discharged, with its exact boundary.** (JC) is not decorative: M-5
is a counterexample in which every other hypothesis of Theorem V.3 holds ($\Psi=\mathrm{id}$
so (A-iv) is an equality, $\bar\mu=f_\#\mu$, unit weights) and only (JC) fails, and
$\Delta_{\mathrm{avg}}\to-\tfrac14$ as $\delta\to0^+$. Therefore:

* **(JC) holds** in the location sector with fixed fiber covariance (there
  $\bar g^F\equiv\bar\Sigma_0^{-1}$ is constant, so (JC-const) and the exact identity
  apply), and in the **law chart** (the perspective function $\dot p^2/p$ is jointly
  convex);
* **(JC) fails** in the covariance sector of the Gaussian moment chart. Averaging must
  not be described as information-losing there.

**The coherence check survives, and is now explained.** The score route's observation
that the variational coarse map reduces exactly to the averaging map in the
fixed-covariance Gaussian location tier is correct **and** is precisely the tier in
which (JC-const) holds. It does not extend to the covariance sector — the falsifier's
M-5(iv) caveat, decided in the falsifier's favor with the reason supplied.

### V.4 M-4 decided: Theorem G is the mixture-tier instance of Theorem V.3

The score route attaches Theorem G's defect
$\mathsf G^\kappa(\dot\theta,\dot\theta)-I_{\bar P}(\theta)=\mathbb E\operatorname{Var}(\ell\mid Y)$
to the fiberwise barycenter (5.1); the falsifier says detach. **Neither is right, and
the correct statement is sharper than both.**

Theorem G's coarse object is the **mixture** $\bar P_\theta=\int p_{s_\theta(c)}\kappa(dc)$,
i.e. the barycenter taken **in the law chart**. Theorem V.3 with $\Psi=\mathrm{id}$,
$w=\bar w=1$, $\bar{\mathcal C}=\{*\}$, and the law chart gives
$\mathsf R s=\bar P$, $T\mathsf R Z=\partial_\theta\bar P$, hence
$\Delta_{\mathrm{avg}}=\mathsf G^\kappa-I_{\bar P}$ — **identically Theorem G's defect**.
So:

> **Theorem G *is* the exact averaging defect precisely when the barycenter is taken
> in the law chart and the coarse family is closed under $\kappa$-mixtures.** It is
> *not* the defect of a chart barycenter into a family that is not mixture-closed,
> such as the Gaussians.

**Verification (Part XI, Block 10).** Two contexts, $\kappa$ uniform, unit-variance
Gaussian location fiber, $m_1(\theta)=\theta+1$, $m_2(\theta)=\theta-1$:
$\mathsf G^\kappa=1$; $I_{\bar P}(0)=0.5504$ by quadrature; mixture-tier
$\Delta_{\mathrm{avg}}=0.4496>0$. The Gaussian-moment-chart barycenter gives
$\bar m(\theta)=\theta$ with Fisher $1$, so its $\Delta_{\mathrm{avg}}=0$. The two
numbers differ because the two maps differ — M-4's separation is confirmed — and both
are nonnegative because both charts satisfy (JC) in the location sector.

**Family closure is the discriminating hypothesis.** In the mixture tier
$\bar{\mathcal B}$ must be mixture-closed, or $\bar P_\theta\notin\bar{\mathcal B}$ and
(H5) fails; `07_general_renormalization.tex:872-874` records exactly this failure for
Gaussians. So the mixture tier is available for a full-simplex or otherwise
convex-mixture-closed coarse family, and the chart tier for a parametric coarse family
satisfying (JC); the two are different constructions with different closure
requirements, and each carries its own instance of Theorem V.3.

### V.5 Smoothness and gauge descent at the chosen tier — proved, not called routine

**Proposition V.4 (Tier F, smoothness).** In Construction IV.1, extend the declaration
to scale $\ell+1$: $\bar{\mathcal C}$, $\bar\mu$, $\bar w$, coarse fiber
$\bar{\mathcal B}=\{\mathcal N(m,\bar\Sigma_0)\}$ with fixed $\bar\Sigma_0\succeq\Sigma_0$,
and a coarse basis $\psi_1,\dots,\psi_M$ linearly independent in
$L^2(\bar w\bar\mu;\bar\Sigma_0^{-1})$. Suppose the fiberwise average of each fine basis
field lies in the coarse span:
$\int_{f^{-1}(\bar c)}\phi_a\,d\kappa_{\bar c}=\sum_bT_{ba}\psi_b(\bar c)$ for a constant
matrix $T\in\mathbb R^{M\times N}$. Then

$$
\mathsf R_\ell:\mathcal Q_\ell\to\mathcal Q_{\ell+1},\qquad \mathsf R_\ell(\xi)=T\xi,
$$

is the averaging map of Theorem V.3 read in coordinates. It is **linear, hence
$C^\infty$**, with $T\mathsf R_\ell=T$ everywhere; it is gauge equivariant because the
translation action is by linear maps and commutes with $\kappa_{\bar c}$-barycenters;
and its metric compatibility is the matrix inequality

$$
T^{\!\top}\,\bar\Phi\,T\;\preceq\;\Phi,
\qquad
\bar\Phi_{bc}=\int\psi_b^{\!\top}\bar\Sigma_0^{-1}\psi_c\,\bar w\,d\bar\mu,
$$

which is **exactly** $\mathsf R_\ell^*\mathsf G_{\ell+1}\preceq\mathsf G_\ell$ and is
implied by Theorem V.3 under (A-iv), (A-v).

*Proof.* Averaging a section of the declared family gives the mean field
$\bar c\mapsto\sum_a\xi_a\int\phi_a\,d\kappa_{\bar c}=\sum_b(T\xi)_b\psi_b(\bar c)$,
which is $s_{T\xi}$ in the coarse family; smoothness and the tangent map are those of
a linear map. Gauge equivariance: for $g\in\mathbb R^K$ the action sends the mean field
$m$ to $m+g$, and $\int(m+g)d\kappa_{\bar c}=\int m\,d\kappa_{\bar c}+g$ since
$\kappa_{\bar c}$ is a probability measure; the same computation in any trivialization
gives the same answer because the transition maps are translations. Compatibility is
Theorem V.3 evaluated on the finite-dimensional tangent, and equals the displayed
matrix inequality because both metrics are constant Gram forms. $\square$

**Executed composite witness — L-CONFIG-NONEMPTY discharged (Part XI, Blocks 6, 9).**

*Tier F (no base collapse).* $\mathcal C_\ell=\bar{\mathcal C}=S^1$, $f=\mathrm{id}$,
$\mu=\bar\mu$ normalized arclength (so $f_\#\mu=\bar\mu$), $w=\bar w=1$ (so
$\bar w\circ f\le w$), $\Sigma_0=1$, $\bar\Sigma_0=2$ realized by the sample kernel
$N(x,\cdot)=\mathcal N(x,1)$ — normalized, parameter-independent, translation
equivariant, with family closure and $q(m)=m$ smooth. Flat connections give
$\mathfrak A_{\mathcal P}=0$, hence $A_\Psi\equiv0$ (Theorem II.6(3), zero anomaly).
Basis $\{1,\cos\theta,\sin\theta\}$, $T=I_3$. Then

$$
\mathcal Q_\ell\cong\mathcal Q_{\ell+1}\cong\mathbb R^3,\quad
\mathsf G_\ell=\Phi=\operatorname{diag}(1,\tfrac12,\tfrac12)\succ0,\quad
\mathsf G_{\ell+1}=\tfrac12\Phi\succ0,\quad
\mathsf R_\ell=\mathrm{id},
$$

so $\mathsf R_\ell^*\mathsf G_{\ell+1}=\tfrac12\Phi\prec\Phi=\mathsf G_\ell$: the
compatibility hypothesis holds strictly. With $\mathcal F_{\ell+1}(\xi)=\tfrac12|\xi|^2$
and $\mathcal F_\ell=\mathcal F_{\ell+1}\circ\mathsf R_\ell$, the natural-gradient fields
are $X_\ell=-\Phi^{-1}\xi$ and $X_{\ell+1}=-2\Phi^{-1}\xi$, so **(SC) holds exactly
with $a_\ell\equiv\tfrac12>0$**, the flows are complete linear flows, no collapse
occurs off $\xi=0$, and $\nu^{\mathrm{img}}_{\ell+1}/\nu_\ell=1/\sqrt2$.

*Tier F′ (genuine base collapse, exercising V.1–V.3).* Same fine data, with
$\bar{\mathcal C}=\{*\}$, $f\equiv*$, $\bar\mu=f_\#\mu$ the unit point mass,
$\mathcal Q_{\ell+1}=\mathbb R$ (constant coarse mean), $\mathsf R_\ell(\xi)=\xi_0$ the
fiberwise average, $\mathsf G_{\ell+1}=\tfrac12$. Then $T=\begin{pmatrix}1&0&0\end{pmatrix}$,
and

$$
\mathsf G_\ell-\mathsf R_\ell^*\mathsf G_{\ell+1}
=\operatorname{diag}\big(\tfrac12,\tfrac12,\tfrac12\big)\succ0,
$$

which splits **exactly** into the channel term $\tfrac12\Phi=\operatorname{diag}(\tfrac12,\tfrac14,\tfrac14)$
and the Jensen term $\operatorname{diag}(0,\tfrac14,\tfrac14)$ of Theorem V.3, with zero
weight gap. Verified symbolically. Note that the pointwise-induced map is **undefined**
at every nonconstant $\xi$ here (Theorem V.2), while $\mathsf R_\ell$ is defined and
smooth everywhere: this is exactly why the stack declares $\mathsf R_\ell$ separately.

**Consequence.** The triple $(\mathcal Q_\ell,\mathcal Q_{\ell+1},\mathsf R_\ell)$ with
strong metrics, locally existing unique VFE vector fields, and a smooth coarse map
exists in two nontrivial instances. `H-CONFIG` has a nonempty model class, so the
three history theorems are not vacuous.

### V.6 Two-channel assembly and the cross-scale declaration conditions

For a weighted product $h^{\mathrm{prod}}=w_bh^{\omega_b}_q+w_mh^{\omega_m}_s$ at the
fine scale and $\bar h^{\mathrm{prod}}$ at the coarse scale,

$$
h^{\mathrm{prod}}-f^*\bar h^{\mathrm{prod}}
=\sum_{x\in\{b,m\}}\Big[w_x\big(h_x-f^*\bar h_x\big)+(w_x-\bar w_x)\,f^*\bar h_x\Big],
$$

which is positive semidefinite under the channelwise hypotheses **only if in addition
$\bar w_x\le w_x$ for both channels.** Independently declared coarse weights with
$\bar w_x>w_x$ break positivity even with zero anomaly and genuine Markov channels.

Together with the base-measure condition, this gives the two **cross-scale declaration
compatibility** conditions that currently live in no ledger claim (falsifier N-7,
confirmed):

$$
\textbf{(X1)}\quad f_\#\mu=\bar\mu,
\qquad\qquad
\textbf{(X2)}\quad \bar w_x\circ f\le w_x\ \ (x\in\{b,m\}).
$$

**(X1) is not optional, and its failure is not exotic.** With a vanishing fiberwise
defect and $h=f^*\bar h$ pointwise, take $\mathcal C=\bar{\mathcal C}$ the disjoint
union of two copies of $\mathbb R$, $f=\mathrm{id}$, $h$ vanishing on the first
component and equal to $dx^2$ on the second, $\mu$ a point mass on the first component
and $\bar\mu$ a point mass on the second: the fine integrated metric is $0$ and the
coarse is $1$. (The score route states this witness on the two-point set
$\{1,2\}$ "with the discrete structure", where $\operatorname{Sym}^2T^*\mathcal C=0$ and
no tangent direction exists — falsifier N-4, sustained; the disjoint-union retyping
above repairs it and preserves the content.) The same reversal follows from weights
alone with $\bar w>w$.

---

## Part VI — Semiconjugacy, noncollapse, maximal intervals, natural-gradient sufficiency, Fisher speed, and duration

This part discharges brief item 6.

### VI.1 The condition, and the automatic regularity of the factor

**Definition (SC).** For open $U\subseteq\mathcal Q_\ell$, the pair
$(\mathsf R_\ell,a_\ell)$ is an **oriented semiconjugacy** of $X_\ell$ onto
$X_{\ell+1}$ over $U$ when $a_\ell:U\to(0,\infty)$ is continuous and
$T_Q\mathsf R_\ell X_\ell(Q)=a_\ell(Q)X_{\ell+1}(\mathsf R_\ell Q)$ for every $Q\in U$.

**Lemma VI.1.** (1) If $X_{\ell+1}(\mathsf R_\ell Q)\ne0$ then $a_\ell(Q)$ is unique and

$$
a_\ell(Q)=\frac{\mathsf G_{\ell+1}\big(T_Q\mathsf R_\ell X_\ell(Q),\,X_{\ell+1}(\mathsf R_\ell Q)\big)}
{\big\|X_{\ell+1}(\mathsf R_\ell Q)\big\|^2_{\mathsf G_{\ell+1}}},
$$

so $a_\ell$ is $C^k$ wherever $\mathsf R_\ell$, $X_\ell$, $X_{\ell+1}$, $\mathsf G_{\ell+1}$
are $C^k$ and $X_{\ell+1}\circ\mathsf R_\ell\ne0$. (2) If $X_{\ell+1}(\mathsf R_\ell Q)=0$
then (SC) forces $T_Q\mathsf R_\ell X_\ell(Q)=0$ and **every** positive number satisfies
(SC) there: the factor is undetermined on the coarse critical set. *Proof:* pair with
$X_{\ell+1}(\mathsf R_\ell Q)$ and divide; strong nondegeneracy of $\mathsf G_{\ell+1}$
makes the denominator positive. $\square$

Continuity of $a_\ell$ is therefore a **consequence** on the noncritical part, not an
extra assumption, and "$a>0$" is vacuous exactly on the coarse critical set. The
manuscript's `prop:hist-oriented-semiconjugacy` (`05d:723-751`) states $a(Q)>0$ and
then integrates $a$ along an orbit without declaring any regularity.

### VI.2 Maximal intervals, in the right order

**Theorem VI.2.** Assume (SC) on open $U$, with $X_{\ell+1}$ locally Lipschitz. Fix
$Q\in U$, let $J_Q\subseteq J_Q^{\max}$ be the connected component of $0$ in
$\{t:\Phi_s(Q)\in U\ \forall s\ \text{between}\ 0\ \text{and}\ t\}$, and set
$\sigma_Q(t)=\int_0^ta_\ell(\Phi_sQ)\,ds$. Then $\sigma_Q$ is a strictly increasing
$C^1$ diffeomorphism of $J_Q$ onto an open interval $\Sigma_Q\ni0$, and

$$
\Sigma_Q\subseteq\bar J^{\max}_{\mathsf R_\ell Q},
\qquad
\mathsf R_\ell\big(\Phi_t(Q)\big)=\bar\Phi_{\sigma_Q(t)}\big(\mathsf R_\ell Q\big)
\quad\text{for all }t\in J_Q .
$$

*Proof.* Put $c(t)=\mathsf R_\ell(\Phi_tQ)$; then $\dot c=a_\ell(\Phi_tQ)X_{\ell+1}(c)$.
The integrand is continuous and strictly positive, so $\sigma_Q$ is a $C^1$
diffeomorphism onto an open interval; let $\theta=\sigma_Q^{-1}$ and $d=c\circ\theta$.
Then $d'(u)=X_{\ell+1}(d(u))$ on $\Sigma_Q$ with $d(0)=\mathsf R_\ell Q$, so $d$ is an
integral curve; by local Lipschitz continuity the maximal integral curve through
$\mathsf R_\ell Q$ contains it, giving $\Sigma_Q\subseteq\bar J^{\max}$ and the flow
identity. $\square$

**The order of construction is the repair.** The manuscript's proof (`05d:744-751`)
writes that "the right side ... solves the same initial-value problem after the stated
time change" and invokes flow uniqueness. That presupposes $\bar\Phi_{\sigma_Q(t)}$ is
**defined**, which is what must be proved. Building $d$ on $\Sigma_Q$ first costs three
lines and delivers the domain inclusion as a bonus.

**Completeness does not transfer without a positive infimum.** If (SC) holds on all of
$\mathcal Q_\ell$, $J_Q^{\max}=\mathbb R$, and $\underline a:=\inf_ta_\ell(\Phi_tQ)>0$,
then $\Sigma_Q=\mathbb R$ and the coarse orbit is traversed in full. Without
$\underline a>0$ the inclusion is proper: $X_\ell=\partial_x$, $X_{\ell+1}=\partial_y$,
$\mathsf R_\ell=\arctan$, $a=(1+x^2)^{-1}>0$ gives
$\Sigma_0=(-\pi/2,\pi/2)\subsetneq\mathbb R$ with both flows complete.

**Orientation is the whole content of $a>0$.** With
$\mathcal Q=\mathbb R$, $\mathcal F_\ell=x^2/2$, $\mathcal F_{\ell+1}=-y^2/2$,
$\mathsf R_\ell(x)=-x$: the orbit **sets** agree, $a\equiv-1$, and coarse descent
becomes ascent. Requiring only $a\ne0$ loses orientation entirely.

### VI.3 Noncollapse

**Proposition VI.3.** (SC) alone permits total collapse: take $\mathsf R_\ell\equiv Q^*$
constant and $X_{\ell+1}\equiv0$. Both sides vanish identically, so (SC) holds for
every $a>0$ while every nonconstant fine orbit maps to a point and every coarse Fisher
duration is zero. A **nonconstant shared oriented history** therefore additionally
requires

1. $T_Q\mathsf R_\ell X_\ell(Q)\ne0$ on every nontrivial subarc — equivalently, given
   $a>0$, $X_{\ell+1}(\mathsf R_\ell Q)\ne0$ there; and
2. the maximal-interval condition of Theorem VI.2, upgraded to $\Sigma_Q=\bar J^{\max}$
   only under $J_Q^{\max}=\mathbb R$ and $\inf a_\ell>0$.

Neither is implied by the displayed equation. In Tier F both hold off the single
critical point $\xi=0$: $a_\ell\equiv\tfrac12$, $X_{\ell+1}=-2\Phi^{-1}\xi\ne0$ for
$\xi\ne0$, and both flows are complete.

**"Noncritical" must be given a referent.** `prop:hist-oriented-semiconjugacy` opens
"On a noncritical domain" without naming which field is noncritical. By Lemma VI.1 the
load-bearing reading is $X_{\ell+1}\ne0$ on $\mathsf R_\ell(U)$.

### VI.4 The positive time-change factor cancels from geometric length

**Theorem VI.4.** Under (SC), with $\nu_\ell(r)=\|X_\ell(Q^{(\ell)}(r))\|_{\mathsf G_\ell}$
and $\nu^{\mathrm{img}}_{\ell+1}(r)=\|\tfrac{d}{dr}\mathsf R_\ell Q^{(\ell)}(r)\|_{\mathsf G_{\ell+1}}$:

$$
\nu^{\mathrm{img}}_{\ell+1}(r)=a_\ell\big(Q^{(\ell)}(r)\big)\,
\big\|X_{\ell+1}\big(\mathsf R_\ell Q^{(\ell)}(r)\big)\big\|_{\mathsf G_{\ell+1}},
$$

and for $r_0<r_1$ in $J_Q$,

$$
\tau^{(\ell+1)}(r_1)-\tau^{(\ell+1)}(r_0)
=\int_{\sigma_Q(r_0)}^{\sigma_Q(r_1)}\big\|X_{\ell+1}\big(\bar\Phi_u(\mathsf R_\ell Q)\big)\big\|_{\mathsf G_{\ell+1}}\,du,
$$

which is the intrinsic $\mathsf G_{\ell+1}$-arc length of the coarse orbit arc.
**$\tau^{(\ell+1)}$ does not depend on $a_\ell$ at all.**

*Proof.* The first display is (SC) plus absolute homogeneity of the norm and
$a_\ell>0$. For the second, substitute (SC) and change variables $u=\sigma_Q(s)$, whose
Jacobian is $du=a_\ell(\Phi_sQ)\,ds$; the factor $a_\ell$ in the integrand cancels
against the Jacobian exactly. Positive homogeneity is what makes the cancellation
exact; with $a<0$ allowed, the absolute value would break the substitution. $\square$

**Answer to the brief's question.** *Yes — the positive time-change factor cancels from
geometric length.* Calling $a_\ell$ a "rate" is a category error: it is a
reparameterization datum, invisible to duration, and it is precisely the object that
must **not** appear in a final arc length.

### VI.5 Which metric compatibility is required — necessary and sufficient

**Theorem VI.5.** Under (SC), along a fixed orbit and with the common origin $r_0$:

1. $\tau^{(\ell+1)}\equiv\tau^{(\ell)}$ **iff**
   $\|T\mathsf R_\ell X_\ell\|_{\mathsf G_{\ell+1}}=\|X_\ell\|_{\mathsf G_\ell}$ almost
   everywhere along the orbit;
2. $\tau^{(\ell+1)}\equiv\kappa\,\tau^{(\ell)}$ for a constant $\kappa>0$ **iff** the
   same with the factor $\kappa$;
3. $\tau^{(\ell+1)}$ has nonincreasing increments relative to $\tau^{(\ell)}$ on every
   subinterval **iff**
   $$
   \boxed{\;\big\|T\mathsf R_\ell X_\ell\big\|_{\mathsf G_{\ell+1}}\le\big\|X_\ell\big\|_{\mathsf G_\ell}
   \ \text{ pointwise along the orbit.}\;}
   $$

*Proof.* Both durations are integrals of continuous nonnegative densities from a common
origin; two such integrals agree for all upper limits iff the densities agree almost
everywhere (Lebesgue differentiation), and analogously for the scaled and ordered
versions. $\square$

**The exact answer to "which compatibility".** The **necessary and sufficient**
condition is the *scalar* inequality VI.5(3), evaluated on the **single direction
$X_\ell$** along the orbit. The tensorial Loewner condition

$$
\mathsf R_\ell^{\,*}\mathsf G_{\ell+1}\preceq\mathsf G_\ell
\qquad\text{along the curve}
$$

is **sufficient and strictly stronger**; it is the condition one declares when the
comparison must hold for every direction, and it is what Theorem V.3 and Proposition V.4
deliver. Neither follows from any fiberwise Fisher contraction theorem.

**Why it does not follow (two independent mechanisms).**

*Mechanism 1 — the metrics are separately declared data.* $\mathcal Q_\ell=\mathcal Q_{\ell+1}=\mathbb R$,
$X_\ell=X_{\ell+1}=\partial_x$, $\mathsf R_\ell=\mathrm{id}$: (SC) holds with $a\equiv1$,
no collapse, a diffeomorphism. Declare $\mathsf G_\ell=dx^2$ and $\mathsf G_{\ell+1}=4\,dx^2$;
then $\tau^{(\ell+1)}=2\tau^{(\ell)}$. Two independent legitimate realizations: (a) one
context, identity fiber map (so $\Delta_F^\Psi=0$ **exactly**), channel weights
$w^{(\ell)}=1$ and $w^{(\ell+1)}=4$ — **information loss is exactly zero and duration
still doubles**; (b) fine fiber $\{\mathcal N(\mu,1)\}$ and coarse
$\{\mathcal N(\mu,\tfrac14)\}$, identity parameter map. Both violate hypothesis 1 of
Theorem VI.6 below.

*Mechanism 2 — contraction compares the image, not an independently recomputed orbit.*
$\mathsf R_\ell=\mathrm{id}$ on $\mathbb R^2$ with $\Psi=\mathrm{id}$, so contraction is an
equality and image durations agree; but with $\mathcal F_\ell=\tfrac12(x^2+y^2)$ and
$\mathcal F_{\ell+1}=\tfrac12(x^2+4y^2)$ the fine history from $(1,1)$ is the straight
segment $(e^{-t},e^{-t})$ of total duration $\sqrt2$, while the independently
recomputed coarse history is $(e^{-t},e^{-4t})$, not a straight segment, hence of
strictly greater duration; and (SC) itself fails, since $(-x,-y)=a(-x,-4y)$ forces
$a=1$ then $y=4y$. **With perfect information preservation, compatible metrics, and no
collapse, the independently recomputed coarse duration still differs.**

The two mechanisms are logically independent and neither implies the other; that is the
exact content of the manuscript's sentence "Either condition without the other is
insufficient" (`05d:753-759`), which is currently asserted with neither witness.

### VI.6 When the fiberwise contraction does lift

**Theorem VI.6.** Assume (1) $\mathcal C_{\ell+1}=\mathcal C_\ell$ with the same finite
base measure $\mu_i$ and the same positive channel weights $w_x$; (2) $\mathsf R_\ell$
acts pointwise, $(\mathsf R_\ell Q)(c)=\Psi_c(Q(c))$, each $\Psi_c$ the pushforward of a
normalized parameter-independent Markov kernel with vertical differential $T^V\Psi_c$;
(3) both configuration metrics are the corresponding weighted integrals of the fiber
Fisher metrics; (4) all integrals finite. Then for every $Z\in T_Q\mathcal Q_\ell$,

$$
\|Z\|^2_{\mathsf G_\ell}-\|T\mathsf R_\ell Z\|^2_{\mathsf G_{\ell+1}}
=\int_{\mathcal C_i}\sum_xw_x\,\Delta_F^{\Psi_c}\big(Z_x(c),Z_x(c)\big)\,d\mu_i
=\int_{\mathcal C_i}\sum_xw_x\,\mathbb E\operatorname{Var}\big(\ell_{Z_x(c)}\mid Y_c\big)\,d\mu_i\ \ge0,
$$

hence $\nu^{\mathrm{img}}_{\ell+1}\le\nu_\ell$ pointwise and $\tau^{(\ell+1)}\le\tau^{(\ell)}$
increment by increment, with equality on a subinterval exactly when the fine score in
the direction $Z_x(c)$ is $Y_c$-measurable for $\mu_i$-almost every $c$ and every
channel.

*Proof.* Differentiate the pointwise action; insert into (3) at level $\ell+1$ and
subtract (3) at level $\ell$; the integrand is $\Delta_F^{\Psi_c}$, nonnegative by
Theorem II.5. Monotonicity of the integral and of the square root gives the speed
inequality; integrating in $r$ gives the duration inequality. $\square$

**Theorem VI.6 is the special case $f=\mathrm{id}$ of Theorem V.3** with zero Jensen and
zero weight gap. Theorem V.3 is the strict generalization that admits a **collapsing**
base map, which is what an RG step actually does; it is the version the stack uses, and
it is what Tier F′ realizes.

**Hypothesis 2 excludes the manuscript's own Galerkin aggregation.** By
`prop:ig-pullback-vs-pushforward` (`08_infogeometry.tex:505-527`) that coarse operator
is a **restriction**, not a Markov pushforward, and the two differ by a
positive-semidefinite Schur term with the restriction **larger** in the Loewner order.
Hypothesis 1 is exactly what mechanism-1 realization (a) violates.

### VI.7 Natural-gradient sufficiency

Throughout, $X_\ell=-\operatorname{grad}^{\mathsf G_\ell}\mathcal F_\ell$ and
$X_{\ell+1}=-\operatorname{grad}^{\mathsf G_{\ell+1}}\mathcal F_{\ell+1}$ with
$\mathcal F_\bullet\in C^2$ and both metrics strong.

**VI.7.1 Equality of objectives does not intertwine gradients.** The differential
$d\mathcal F$ is metric-free; the gradient is not. Witness:
$\mathsf R_\ell=\mathrm{id}$ on $\mathbb R^2$, one objective $\tfrac12(x^2+2y^2)$, metrics
$\operatorname{diag}(1,1)$ and $\operatorname{diag}(1,\kappa)$ with $\kappa\ne1$. Then
(SC) would require $(x,2y)=a(x,2y/\kappa)$, forcing $a=1$ and then $\kappa=1$: (SC)
fails on the dense open set $\{xy\ne0\}$.

**VI.7.2 Functional compatibility (FC).** Declare $\chi_\ell$ with $\chi_\ell'>0$ and
$\mathcal F_\ell=\chi_\ell\circ\mathcal F_{\ell+1}\circ\mathsf R_\ell$ on an open
$U\supseteq\mathcal O$ containing the fine orbit. (FC) supplies orientation and
noncollapse for free; it does **not** by itself supply (SC).

**Theorem VI.7 (metric sufficient conditions).** Let $\mathsf R_\ell$ be a surjective
submersion with closed orbit-tangent splitting, let
$\mathcal H=(\ker T\mathsf R_\ell)^{\perp_{\mathsf G_\ell}}$, and assume (FC).

1. If $\mathsf R_\ell$ is a **Riemannian submersion** ($T\mathsf R_\ell|_{\mathcal H}$ a
   linear isometry onto $T\mathcal Q_{\ell+1}$), then (SC) holds with $a_\ell=\chi_\ell'>0$.
2. If $\mathsf R_\ell$ is **horizontally conformal with dilation $\varphi_\ell>0$**, then
   (SC) holds with $a_\ell=\chi_\ell'\varphi_\ell^2>0$.

*Proof.* $u:=\operatorname{grad}^{\mathsf G_\ell}\mathcal F_\ell\in\mathcal H$ under (FC).
For $Z\in\mathcal H$,
$\mathsf G_{\ell+1}(T\mathsf R_\ell u,T\mathsf R_\ell Z)=\varphi_\ell^2\mathsf G_\ell(u,Z)
=\varphi_\ell^2\,d\mathcal F_\ell[Z]=\varphi_\ell^2\chi_\ell'\,d\mathcal F_{\ell+1}[T\mathsf R_\ell Z]
=\varphi_\ell^2\chi_\ell'\,\mathsf G_{\ell+1}(w,T\mathsf R_\ell Z)$ with
$w=\operatorname{grad}^{\mathsf G_{\ell+1}}\mathcal F_{\ell+1}\circ\mathsf R_\ell$. Since
$T\mathsf R_\ell(\mathcal H)=T\mathcal Q_{\ell+1}$, nondegeneracy gives
$T\mathsf R_\ell u=\varphi_\ell^2\chi_\ell'w$; negate. Part 1 is part 2 with
$\varphi_\ell\equiv1$. $\square$

*Sanity check.* $\mathsf R_\ell(x)=\lambda x$ on Euclidean $\mathbb R$: $\varphi_\ell=|\lambda|$
and $\mathcal F_\ell'=\lambda\mathcal F_{\ell+1}'(\lambda x)$ give
$T\mathsf R_\ell\operatorname{grad}\mathcal F_\ell=\lambda^2\mathcal F_{\ell+1}'$, matching
$a_\ell=\lambda^2$.

**Tier F satisfies Theorem VI.7(2) exactly.** There $\mathsf R_\ell=\mathrm{id}$,
$\mathcal H=T\mathcal Q_\ell$, $\mathsf G_{\ell+1}=\tfrac12\mathsf G_\ell$, so
$\varphi_\ell^2=\tfrac12$; with $\chi_\ell=\mathrm{id}$ this predicts $a_\ell=\tfrac12$,
which is what the direct computation returns. **This is a nonempty model of
natural-gradient semiconjugacy sufficiency.**

**Where the manuscript's own maps stand.** Under Theorem VI.6's hypotheses the pointwise
Markov configuration map is a contraction, so it can be a Riemannian submersion only if
$\Delta_F^{\Psi_c}$ vanishes on the horizontal space $\mu_i$-a.e. (Fisher sufficiency in
every horizontal direction), and horizontally conformal with $\varphi_\ell\in(0,1]$ only
if $\Delta_F^{\Psi_c}|_{\mathcal H}=(1-\varphi_\ell^2)g^F|_{\mathcal H}$ — the information
loss must be a **constant multiple** of the metric there. And for the exact-RG contracted
functional $\mathcal F_{\ell+1}[Q']=\inf\{\mathcal F_\ell[q]:\mathsf R_\ell q=Q'\}$ one has
$\mathcal F_{\ell+1}(\mathsf R_\ell q)\le\mathcal F_\ell(q)$ with equality **exactly on the
attaining set** $\mathcal A_\ell$, so (FC) with $\chi_\ell=\mathrm{id}$ holds there and
nowhere else, and its differential consequence needs $\mathcal A_\ell$ to have nonempty
interior containing the orbit. The minimal remaining obligation for the manuscript's own
RG histories is therefore:

> **O-SC.** Exhibit $\chi_\ell$ with $\chi_\ell'>0$ and an open $U\supseteq\mathcal O$ on
> which (FC) holds — for the exact-RG contraction, prove
> $\mathcal O\subseteq\operatorname{int}\mathcal A_\ell$ — and then verify horizontal
> conformality of the declared $\mathsf R_\ell$.

O-SC is strictly weaker than proving (SC) directly and is stated in objects the
manuscript already declares. Tier F shows the obligation is satisfiable.

### VI.8 The three coordinates are pairwise independent

| Symbol | Type | Determined up to |
| --- | --- | --- |
| $\ell$ | scale depth: a discrete index on a finite ordered scale set | nothing; it is an index, not a real coordinate |
| $r$ | orbit position: a chart on one oriented orbit | the full group of orientation-preserving $C^1$ reparameterizations |
| $\tau^{(\ell)}(r)$ | accumulated Fisher duration | a choice of origin $r_0$ **and** the declared metric $\mathsf G_\ell$ |

* $\tau$ is invariant under orientation-preserving reparameterization of $r$ and is
  **not** determined by $r$; $r$ is not determined by $\tau$ unless the speed is
  positive.
* $\tau$ is **metric-relative**: scaling $\mathsf G_\ell$ by $\rho^2$ scales every
  duration by $\rho$. Mechanism 1 of VI.5 is exactly this.
* $\ell$ is independent of both: Tier F has one orbit, one duration, and two levels;
  Tier F′ has two levels and different durations for the same orbit.
* **Strict monotonicity is not regularity.** $\tau$ is nondecreasing always, strictly
  increasing exactly when there is positive accumulated length on every nontrivial
  subinterval. An **isolated** zero preserves strict monotonicity but destroys regular
  invertibility: with $h_s=4x^2dx^2$ one gets $\tau(r)=r^2$, whose inverse $\sqrt{\cdot}$
  is not differentiable at $0$. A zero-speed **interval** destroys strict monotonicity
  outright. A Fisher-null tangent destroys regularity at that point.
* **$\tau$ is not a function on the contextual base and not physical time.** A regional
  clock potential requires a closed clock one-form with zero periods on the region;
  for $\mathcal F=xy$ the normalized descent one-form
  $\alpha_F=-(y\,dx+x\,dy)/\sqrt{x^2+y^2}$ has
  $d\alpha_F=\frac{x^2-y^2}{(x^2+y^2)^{3/2}}\,dx\wedge dy$, which vanishes only on the
  diagonal and hence on no open set: $\alpha_F$ is not closed, so no local potential
  exists. Any operational identification of $\tau$ with a clock reading remains a
  separate postulate outside the theorem target, and is **not** made here.

---

## Part VII — Atomic dispositions and dependency ordering

This part discharges brief item 7.

### VII.1 Legend

| Code | Meaning |
| --- | --- |
| **PROVED** | complete derivation present here or cited to a completed derivation whose hypotheses were checked here |
| **PROVED‑C** | proved under an **added** declared hypothesis, named in the row; the model class of that hypothesis is proved nonempty |
| **REFUTED** | a scope‑matched counterexample against the stated universal reading is exhibited |
| **OPEN** | neither; the exact missing obligation is named |
| **OPEN(BYTES)** | every mathematical conjunct is proved, but a conjunct is a statement about the repository state that is **currently false on the bytes**; it can be closed only by an edit, not by a derivation |

"Inherited" closures are not counted as evidence anywhere below. Every row was
re‑derived here from the frozen contract or is explicitly marked as a byte fact.

### VII.2 Atomized dispositions for the twelve in‑scope claims

`claim-ledger.json:78-89`, reached by the twelve `target -> …` edges at
`dependency-dag.json:26-37`.

**1. `score-action-compatibility` — PROVED (all three conjuncts).**

| Conjunct | Disposition | Basis |
| --- | --- | --- |
| (a) $\mathscr S_{l,H}[\varphi]=-(\varphi-\mathbb E_\pi\varphi)$ descends to the quotient | PROVED | III.1: $\mathscr S_\pi[\varphi+c]=\mathscr S_\pi[\varphi]$ |
| (b) isometric isomorphism $L^2/\mathbb R\mathbf 1\to L^2_0$ for the Fisher norm | PROVED | III.1: $\|[\varphi]\|_F=\|\varphi-\pi\varphi\|_2$; surjective since $\varphi=-h$ realizes $h$ |
| (c) $\mathscr S_{l+1,R_lH}[U_l\varphi]=\mathbb E[\mathscr S_{l,H}[\varphi]\mid Z]$ | PROVED | III.1, diagram (D8); $U|_{L^2_0}=R$ |

*Fence required, not a gap:* on $L^2\setminus L^\infty$ the realizing path is the
**quadratic** DQM path, not the exponential‑action path. Witness for the separation:
odd $\mathrm{He}_k$, $k\ge3$ (III.3). The route's $\mathrm{He}_2$ witness is false and
must be replaced (M‑3, sustained).

**2. `bundle-fisher-defect` — PROVED‑C.** Added hypotheses beyond the ledger's
`[H-GAUGE, H-DQM]`: (H1) family‑level domination with a fixed jointly measurable
density version; (H3) $K(x,\mathsf Y)=1$ for **every** $x$; **(H5) family closure**
$N_\star(\mathcal B)\subseteq\bar{\mathcal B}$; smoothness of $q$ between the declared
parametrized‑measure models; **$\widehat{\bar\rho}(\bar G)$‑invariance of $\bar g^F$**
(diagram (D3)); and a jointly measurable $\theta$‑smooth version selection for
$p\mapsto T^V_p\Psi$. Basis: Theorem II.5, with the DQM‑transfer step cited to the
score route's Theorem A rather than asserted (M‑10, decided). The ledger's
`assumption_ids` list is **incomplete** and must be extended (edit L‑4).

**3. `bundle-morphism-descent` — PROVED, with one scope correction.** Descent holds
**iff** the law‑fiber intertwining (I) holds, *given* a declared $\kappa$‑equivariant
$\mathcal P$; smoothness follows from smoothness of $q$ and the submersion property of
the associated‑bundle quotient (diagram (D2)). Scope correction: detached from the
declared $\mathcal P$ the necessity fails — if $\bar{\mathcal B}$ is a single
$\bar G$‑fixed point then (I) is vacuous, not necessary. The three‑fold typing
$N/N_\star/\Psi$ is proved strict by Lemma I.1. **Existence of $\mathcal P$ is a
declared datum admitted by `H-GAUGE`, and it can fail**: it exists iff
$P\times_\kappa\bar G\cong f^*\bar P$, which is a genuine topological condition. That
is a scope note, not a refutation, and belongs at `eq:rg-principal-scale-map`.

**4. `bundle-scale-cocycle` — PROVED.** Ordered composition holds and is compatible at
five typed levels: $f_{02}=f_{12}f_{01}$; $\kappa_{02}=\kappa_{12}\kappa_{01}$;
$\mathcal P_{02}=\mathcal P_{12}\mathcal P_{01}$;
$q_{02}=q_{12}q_{01}=(N_{01}N_{12})_\star$ by Chapman–Kolmogorov; and
$\Psi_{02}=\Psi_{12}\Psi_{01}$. The rightmost factor acts first at every level.
Theorem II.7 supplies the ordered law for the anomaly and Theorem II.6(4) the
connection‑level cocycle. **The bundle route's "executed verification" for this claim
is mislabeled** (M‑2, sustained): its Block C verifies the unconditional telescoping
$\mathcal E_{02}=\mathcal E_{01}+f_{01}^*\mathcal E_{12}$, not the sharp cocycle. The
replacement check is II.6, at both type and instance level.

**5. `horizontal-defect-anomaly` — PROVED on its mechanism; one conjunct REFUTED.**

| Conjunct | Disposition | Basis |
| --- | --- | --- |
| (a) the covariant first‑jet chain rule retains the vertical horizontal‑defect term | PROVED | Theorem II.1, certifying `eq:pb-covariant-jet-chain-rule` |
| (b) its exact composition law | PROVED | Theorem II.7; order matters, the naive sum is a type error |
| (c) every signed cross term is retained in the base comparison | PROVED | Theorem II.2: $\delta_\Psi-\mathcal X_\Psi-\mathcal Q_\Psi$, with $\mathcal X_\Psi$ signed and $\mathcal Q_\Psi\succeq0$ |
| (d) "positivity follows **only when** that defect vanishes" | **REFUTED** | Corollary II.4 and the five‑row table of II.2: rows $b=\pm1/10$ and $b=-3/5$ have $A_\Psi\ne0$ with strictly positive signed difference |

The exact replacement is the signed criterion II.3(3). Under
`problem-contract.json`'s `falsification_criterion`, a refuted conjunct of a
`UNIVERSAL` claim blocks affirmative release for that conjunct until the wording is
repaired (edit L‑1).

**6. `pullback-compatibility` — PROVED‑C; the unconditional order relation REFUTED.**
Under Theorem II.5's hypothesis set including $A_\Psi(s;\cdot)=0$,
$h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}=\delta_\Psi\succeq0$. Without it, the
difference can be **negative definite**: identity kernel, exactly related sections,
$A=0$, $\bar A=-a\,dx$ gives $-a^2dx^2\prec0$. Two ledger wording defects: the phrase
"horizontal‑lift‑compatible" is the undefined phrase and must be replaced by the
isotropy condition II.6(3); and "the vertical mismatch term" (singular) must become the
**two** retained tensors $-\mathcal X_\Psi-\mathcal Q_\Psi$ (edit L‑2).

**7. `configuration-fisher-metric` — PROVED‑C at Tier F; OPEN for the manuscript's
declared objects.**

| Conjunct | Disposition | Basis |
| --- | --- | --- |
| (a) an explicitly selected finite‑dimensional or Banach/Hilbert section manifold | PROVED‑C | Construction IV.1; $\mathcal Q_\ell\cong\mathbb R^N$, nonempty constructively |
| (b) the metric is **strong** | PROVED‑C | Theorem IV.2(3): automatic in finite dimensions; tier (b1) under two‑sided bounds |
| (c) it is a joint‑law pullback **or** a labeled weighted product with $(\mu,w,\text{gauge quotient},\text{finiteness},\text{nondegeneracy})$ | PROVED‑C | second disjunct discharged in full, IV.4 table |
| (d) the same at **every** scale where a natural‑gradient field or duration is asserted | **OPEN** | the manuscript exhibits no configuration manifold at any scale |

Added hypothesis **(H‑CONFIG‑F)**: at every such scale the configuration manifold and
metric are those of Construction IV.1, or of tier (b1) with its two‑sided bounds.
Under (H‑CONFIG‑F) the claim closes; without it, conjunct (d) is `OPEN`. **Route D's
`PROVED` is circular** — it closes the claim on its own standing hypothesis H‑D1,
which *is* the claim (M‑7, sustained) — and must not be entered as corroboration.
**L‑CFM** is discharged for the weighted‑product branch and remains open for the
joint‑law‑lift branch, which the stack does not use.

**8. `configuration-map` — PROVED (mathematical conjuncts) / OPEN(BYTES) (notation
conjunct).**

| Conjunct | Disposition | Basis |
| --- | --- | --- |
| (a) separately typed as $\mathcal Q_\ell\to\mathcal Q_{\ell+1}$ | PROVED‑C | Proposition V.4: $\mathsf R_\ell(\xi)=T\xi$, a declared object distinct from $N,N_\star,\Psi,K_\ell,\mathcal R^H,\mathcal R_b,M_\ell,C_{\ell,s},\widehat{\mathcal R}_\ell,\widehat R_\ell$ |
| (b) smooth, with a well‑defined tangent map | PROVED‑C | Proposition V.4: linear, hence $C^\infty$, $T\mathsf R_\ell=T$ |
| (c) not identified with the law, action, interaction, reference‑space, or bundle coarse map | PROVED‑C | Type table I.2, rows 1–13 |
| (d) **symbolically disambiguated** in the source | **OPEN(BYTES)** | $\mathcal R$ carries six assignments; `appendix_notation.tex` has no row of type $\mathcal Q_\ell\to\mathcal Q_{\ell+1}$ (V.2, verified by search) |

Route D's "PROVED (typing)" is contradicted on the bytes (M‑8, sustained and
extended). **L‑CM is retired**, not discharged: the stack declares $\mathsf R_\ell$
separately instead of inducing it pointwise, which is the brief's own preference.
Conjunct (d) is closable only by edit N‑1, and **the rename recommended by both the
score route and the falsifier is itself a collision** (V.2).

**9. `configuration-projectability` — PROVED; one route's generalization overreaches.**
(P1)$\Leftrightarrow$(P2)$\Rightarrow$(P3), with (P3)$\Rightarrow$(P2) under connected
fibers; smoothness of the descent is a **theorem** under a surjective submersion, not
an obligation; the submersion hypothesis is load‑bearing ($f(x)=x^3$ witness); and a
pointwise bundle morphism induces no map on all section configurations whenever a
collapsed direction meets a non‑annihilated vertical direction (Theorem V.2, with
$\mathcal B$ connected — M‑12(c) adopted). The score route's upgrade to "on a
genuinely infinite‑dimensional configuration manifold it induces one nowhere" is
**false in general** (a diffeomorphism $f$ descends every section); only the scoped
$L^2$‑tier collapse statement may be carried (N‑3, decided).

**10. `history-semiconjugacy` — PROVED as a criterion; OPEN as a fact about the
manuscript's flows.** Sufficiency with the domain inclusion $\Sigma_Q\subseteq\bar J^{\max}$
(Theorem VI.2), the converse on regular arcs, automatic regularity and uniqueness of
$a_\ell$ off the coarse critical set (Lemma VI.1), the orientation content of $a>0$,
and composition across scales are all proved. What is **not** proved is that the
manuscript's independently recomputed RG maps satisfy (SC); the minimal obligation is
**O‑SC** (VI.7). Tier F satisfies (SC) exactly with $a_\ell\equiv\tfrac12$, so the
criterion has a nonempty model class.

**11. `history-noncollapse` — PROVED; the universal reading of the semiconjugacy
conclusion REFUTED.** Proposition VI.3: $\mathsf R_\ell\equiv Q^*$ with $X_{\ell+1}\equiv0$
satisfies (SC) for every $a>0$ while collapsing every nonconstant orbit. The refutation
is scope‑matched: it refutes "(SC) with $a>0$ implies a nonconstant shared history",
**not** the flow identity, which remains true. The two additional hypotheses are stated
and are satisfied off the single critical point in Tier F.

**12. `history-duration-relation` — PROVED; the fiberwise‑contraction reading
REFUTED.** The factor $a_\ell$ cancels exactly from geometric length (Theorem VI.4);
the agreement, constant‑factor, and ordering criteria are necessary and sufficient in
the single direction $X_\ell$ (Theorem VI.5); the tensorial condition
$\mathsf R_\ell^*\mathsf G_{\ell+1}\preceq\mathsf G_\ell$ is sufficient and strictly
stronger; fiberwise contraction lifts exactly under Theorem VI.6's four hypotheses, and
Theorem V.3 is the strict generalization admitting a collapsing base. Two independent
refutations of the naive reading: metric declaration alone reverses the comparison with
**zero** information loss, and contraction compares the image rather than an
independently recomputed orbit. **The portfolio's own repair path was holed** by M‑4
and M‑5; it is repaired here by Theorem V.3 and the (JC) hypothesis, so this claim's
inputs are now available.

### VII.3 Missing claims that must be added to the ledger

`dependency-dag.json:26-37` carries no edge for any of the following and
`claim-ledger.json` no id. Under the atomization rule this is a certification‑blocking
coverage gap. The first three are the ones the brief names; the last three are forced
by the derivations above.

| Proposed id | Statement | Quantifiers | Assumptions | Falsifier | Disposition here |
| --- | --- | --- | --- | --- | --- |
| **`curve-typing`** | The five typed objects — fixed‑fiber vertical curve, total‑space curve over a base curve, $\omega$‑horizontal lift, mixed curve, and configuration curve — are pairwise distinct; verticality is connection‑free while horizontality is not; and the pointwise trichotomy plus the stationary case is a partition, whereas the interval‑level labels are not exhaustive. | every connected parameter interval, every principal connection, every curve | `H-GAUGE`, `H-CONFIG` | a curve label applied at interval scope where the pointwise type varies, or a verticality/horizontality predicate applied to a base curve or to a configuration curve | **PROVED** (route D T1–T7, interface checked here; a configuration curve does not live in $E$ at all, so verticality statements about it are statements about the adjoint evaluation) |
| **`natural-gradient-semiconjugacy`** | Equality of objectives does not intertwine natural gradients; under functional compatibility with $\chi_\ell'>0$, horizontal conformality of $\mathsf R_\ell$ with dilation $\varphi_\ell>0$ is sufficient for (SC) with $a_\ell=\chi_\ell'\varphi_\ell^2$; a pointwise Markov configuration map is horizontally conformal only on a Fisher‑sufficiency locus. | every pair of $C^2$ objectives and strong metrics, every submersive $\mathsf R_\ell$ | `H-CONFIG`, `H-HISTORY` | a claimed gradient intertwining from equality of objectives alone, or from a submersion without a metric‑compatibility hypothesis | **PROVED** (Theorem VI.7 with its sanity check; refutation witness in VI.7.1; nonempty model at Tier F with $\varphi_\ell^2=\tfrac12$) |
| **`coordinate-independence`** | Scale depth $\ell$, orbit position $r$, and Fisher duration $\tau^{(\ell)}$ are pairwise independent coordinates: $\tau$ is reparameterization invariant and metric‑relative, $r$ is determined only up to orientation‑preserving reparameterization, $\ell$ is a discrete index, and strict monotonicity of $\tau$ does not imply that it is a regular coordinate. | every regular oriented orbit segment with finite Fisher speeds | `H-CONFIG`, `H-HISTORY` | an identification of any two of the three, an inversion of $\tau$ at a Fisher‑null point, or a global clock asserted without a closed zero‑period clock one‑form | **PROVED** (VI.8; isolated‑zero witness $\tau(r)=r^2$; clock‑potential obstruction $d\alpha_F\ne0$ for $\mathcal F=xy$). *Ledger note:* this content is currently carried as the **assumption** `H-HISTORY`; a provable statement should not be an assumption. Split `H-HISTORY` into this theorem plus a residual declared refusal covering only the physical‑time identification. |
| **`base-defect-cocycle`** | The base Fisher‑defect residual $\delta_{02}-\delta_{01}-f_{01}^*\delta_{12}$ equals $\Delta_F^{\Psi_{12}}(v,v)-\Delta_F^{\Psi_{12}}(\bar u,\bar u)$ in the three equivalent forms (II.5a–c); the sharp cocycle holds iff the fine pushed jet and the coarse jet have equal $\Delta_F^{\Psi_{12}}$‑seminorm; vanishing stage‑one anomaly is sufficient and not necessary. | every finite composable sequence of scale arrows and both channels | `H-GAUGE`, `H-DQM` | a printed correction term differing from (II.5b)/(II.5c), or a claimed necessity of $A_{\Psi_{01}}=0$ | **PROVED** (Theorem II.8; type‑level and instance‑level checks, Part XI Blocks 1–2). *This claim is where M‑1 lives; the vertical cocycle in `bundle-scale-cocycle` does not cover it.* |
| **`cross-scale-declaration-compatibility`** | Any comparison of **integrated** configuration metrics across scales requires the two separately declared conditions (X1) $f_\#\mu=\bar\mu$ and (X2) $\bar w_x\circ f\le w_x$ for both channels; neither follows from any fiberwise contraction theorem. | every scale arrow at which an integrated metric or duration comparison is asserted | `H-CONFIG`, `H-GAUGE` | an integrated comparison asserted with $f_\#\mu\ne\bar\mu$ or $\bar w_x>w_x$ | **PROVED** (V.6; disjoint‑union reversal witness with vanishing fiberwise defect; weight‑only reversal) |
| **`configuration-coarse-map-compatibility`** | For a separately declared smooth $\mathsf R_\ell$, the exact averaging defect is the three‑term identity of Theorem V.3 under (A‑i)–(A‑v) with (JC‑const), and is $\ge0$ under (JC); generic averaging is **not** a contraction without (JC). | every declared $\mathsf R_\ell$ used in a duration or metric comparison | `H-CONFIG`, `H-GAUGE`, `H-DQM` | an averaging or variational coarse map asserted to lose information in a chart where $(\bar\beta,v)\mapsto\bar g^F_{\bar\beta}(v,v)$ is not jointly convex | **PROVED** (Theorem V.3; M‑5 is the sharp boundary witness, ratio $5000/10201$) — *this is **L‑AVG**, discharged* |

### VII.4 Dependency ordering

`from -> to` means *from depends on to*. The graph is acyclic; the target depends on
every node listed. New nodes are marked **[new]**.

```
target
 |
 +-- score-action-compatibility            [H-DQM, H-REVERSE]
 +-- bundle-morphism-descent               [H-GAUGE; +P declared, (H5), q smooth]
 |
 +-- bundle-fisher-defect            ----> score-action-compatibility
 |                                   ----> bundle-morphism-descent
 +-- bundle-scale-cocycle            ----> bundle-morphism-descent
 |
 +-- horizontal-defect-anomaly       ----> bundle-morphism-descent
 |                                   ----> bundle-scale-cocycle
 +-- pullback-compatibility          ----> bundle-fisher-defect
 |                                   ----> horizontal-defect-anomaly
 +-- base-defect-cocycle       [new] ----> pullback-compatibility
 |                                   ----> bundle-scale-cocycle
 |                                   ----> horizontal-defect-anomaly
 |
 +-- configuration-fisher-metric           [H-CONFIG-F; independent of the bundle chain]
 +-- configuration-projectability    ----> horizontal-defect-anomaly     (P3 uses A_Psi)
 +-- cross-scale-declaration-compatibility [new]  ----> configuration-fisher-metric
 |
 +-- configuration-map               ----> configuration-fisher-metric
 |                                   ----> configuration-projectability
 +-- configuration-coarse-map-compatibility [new]
 |                                   ----> configuration-map
 |                                   ----> bundle-fisher-defect
 |                                   ----> cross-scale-declaration-compatibility
 |
 +-- curve-typing              [new]       [H-GAUGE, H-CONFIG]
 +-- history-semiconjugacy           ----> configuration-map
 |                                   ----> configuration-fisher-metric
 +-- natural-gradient-semiconjugacy [new]
 |                                   ----> history-semiconjugacy
 |                                   ----> configuration-fisher-metric
 +-- history-noncollapse             ----> history-semiconjugacy
 +-- history-duration-relation       ----> history-semiconjugacy
 |                                   ----> configuration-coarse-map-compatibility
 |                                   ----> curve-typing
 +-- coordinate-independence   [new] ----> curve-typing
                                     ----> history-duration-relation
```

**Certification consequence.** `configuration-map` is `OPEN(BYTES)` and is an ancestor
of `history-semiconjugacy`, `natural-gradient-semiconjugacy`, `history-noncollapse`,
`history-duration-relation`, `configuration-coarse-map-compatibility`, and
`coordinate-independence`. `configuration-fisher-metric` conjunct (d) is `OPEN` and is
an ancestor of the same set. Under `proof-obligations.md`, no terminal affirmative
status is available while a dependency ancestor is `OPEN`. Both blockages are closable
by the specified edits, and neither is a mathematical gap.

---

## Part VIII — Contradictions between the four reports, decided by derivation

Each row states the disagreement, the decisive object recomputed here, and the
decision. No row is decided by counting routes.

### C‑1. Is the printed base‑cocycle correction right?

*Bundle route* prints the cross terms with the **fine** pushed jet
$L_{01}D^{\omega_0}s_0$ and a **plus** sign on the quadratic term. *Falsifier* (M‑1)
says the sign is wrong. **Decision: the falsifier is right, and the reason is sharper
than a sign slip.** There are two correct forms, (II.5b) with the *coarse* jet and
$+\Delta(A,A)$, and (II.5c) with the *fine* pushed jet and $-\Delta(A,A)$; the report
printed a hybrid of the two. The excess is exactly
$2\,\Delta_F^{\Psi_{12}}(A_{\Psi_{01}},A_{\Psi_{01}})$ — two copies of the
second‑arrow vertical Fisher defect on the first‑arrow anomaly — matching the brief's
characterization exactly. Derived from first principles in Theorem II.8, checked
type‑level and instance‑level in Part XI, Blocks 1–2.

### C‑2. Does the bundle route's Block C verify the base cocycle?

*Bundle route* titles Block C "the base cocycle (R4.3) and its identification".
*Falsifier* (M‑2) says it verifies a telescoping tautology under a symbol collision.
**Decision: the falsifier is right.** Block C's displayed polynomials reproduce
exactly from $\mathcal E_{jk}=h_j-f_{jk}^*h_k$, whose telescoping is unconditional;
under the report's own $\delta$ definition, $\delta_{\Psi_{01}}=\tfrac12$ independently
of $a_1$, while Block C's $\delta_{01}$ at $a_1=1/10$ is $7/25$. The sharp cocycle
**fails** on exactly that data, with residual $-\tfrac23a_1(a_1+1)$. The replacement
is II.6: a symbolic identity in a symbolic symmetric form $D$ and symbolic matrices
$V,A$, plus the exact rational instance. This pass supplies the check the falsifier
demanded rather than restating the objection.

### C‑3. Does base positivity require a vanishing anomaly?

*Ledger* (`:82`) says "positivity follows **only when** that defect vanishes".
*Bundle route* refutes that clause. *Score route* (`:1300`) and *timeless route*
(`:1537`) close the claim `PROVED` without adjudicating it. **Decision: the strict
reading is refuted**, by a table reproduced here in exact rational arithmetic (II.2).
Zero anomaly is **sufficient**; the exact criterion is II.3(3); the pointwise margin is
sufficient and not necessary. Two of three routes closed a claim one of whose
conjuncts is false as written; that is a ledger‑wording defect (edit L‑1), not a
mathematical disagreement.

### C‑4. Is `configuration-fisher-metric` proved?

*Bundle* and *score* routes: `OPEN`. *Timeless route*: `PROVED, with a strengthening`,
on the basis that `05d:458-536` declares base measure, weights, gauge quotient,
finiteness, and the submersion caveat. **Decision: route D's closure is circular.** Its
own standing hypothesis H‑D1 declares a smooth Hausdorff Banach manifold "with a
declared strong Riemannian metric", which is precisely what the claim asks to be
established. Declaring is not exhibiting. Independently confirmed on the bytes: no
configuration manifold is exhibited anywhere, "strong metric" occurs once — inside the
hypothesis — and the only nonemptiness result concerns the Gaussian **interaction**
family, a different object. `OPEN` stands for the manuscript. This pass then closes the
claim constructively at Tier F under (H‑CONFIG‑F), which is a different and honest
route: Construction IV.1 assumes no manifold and no metric, and derives both.

### C‑5. Is `configuration-map`'s typing separated?

*Timeless route*: "PROVED (typing) / OPEN (existence)", asserting the typing "is
separated at `07b` and route‑C Section 7". *Score route* and *falsifier*: `OPEN` on a
live symbol collision. **Decision: `OPEN`.** Verified by search on the current bytes:
$\mathcal R$ carries six assignments and `appendix_notation.tex` has no row of type
$\mathcal Q_\ell\to\mathcal Q_{\ell+1}$. **New finding, against all three prior
reports:** the rename to $\widehat R_\ell$ recommended by the score route (`:1303`)
and endorsed by the falsifier (M‑8) **is itself a collision** —
`07b_agent_network_rg.tex:2196` already defines $\widehat R_\ell=J_\ell^{-1}R_\ell J_\ell$
for the reference‑space‑conjugated retained projection, recurring at `07b:1275, 2198,
2201, 2211, 2227, 2240, 2241, 2251`. Adopting the recommended repair would replace one
collision with another. Decision: adopt $\mathsf R_\ell$; `\mathsf{R}`, `\mathfrak{r}`,
`\mathfrak{q}`, `\mathsf{C}` all occur zero times in `manuscripts/gauge_vfe_rg/*.tex`.

### C‑6. What is Theorem G the defect of?

*Score route*: Theorem G's defect "is the correct statement to attach to the averaging
coarse map (5.1)". *Falsifier* (M‑4): detach it; the two are different maps into
different spaces, and for a Gaussian coarse family the mixture leaves
$\bar{\mathcal B}$, so family closure fails. **Decision: the falsifier's separation is
correct and its remedy is too weak.** Theorem G *is* the exact averaging defect — but
only when the barycenter is taken **in the law chart** and the coarse family is closed
under $\kappa$‑mixtures. Theorem V.3 with $\Psi=\mathrm{id}$, unit weights, and a
one‑point coarse base returns $\mathsf Rs=\bar P$, $T\mathsf RZ=\partial_\theta\bar P$,
hence $\Delta_{\mathrm{avg}}=\mathsf G^\kappa-I_{\bar P}$, which is Theorem G verbatim.
The Gaussian **moment‑chart** barycenter is a different map with a different defect
($0$ versus $0.4496$ on the falsifier's own data). So the correct instruction is
**retype, then prove**, not detach: state which chart the barycenter is taken in, and
carry the closure requirement for that chart.

### C‑7. Does averaging lose information?

*Score route*: "This is the precise sense in which averaging over the base loses
information." *Falsifier* (M‑5): refuted; the integrated configuration Fisher metric
can strictly increase, ratio $1.96$. **Decision: the falsifier's counterexample stands
and is reproduced exactly** ($5000/10201=1.9605921$ at $\delta=10^{-2}$, limit $2$).
Generic averaging‑as‑contraction is **retired**. It is replaced by Theorem V.3 under
the new hypothesis **(JC)**, which excludes the counterexample by name: the Gaussian
moment‑chart Fisher form $A^2/(2\Sigma^2)$ has Hessian determinant $-A^2\Sigma^{-6}<0$
and is not jointly convex, whereas the law‑chart integrand $\dot p^2/p$ has a positive
semidefinite Hessian and is. *Correction to the falsifier's supporting arithmetic:* it
reports the determinant as $-4A^2\Sigma^{-6}$; the correct coefficient is $-1$. The
sign, and therefore every conclusion drawn from it, is unaffected.

### C‑8. Does the coherence check between the averaging and variational maps extend?

*Score route* offers the agreement of Constructions 5.2 and 5.3 in the Gaussian
location tier as "a nontrivial consistency check on both". *Falsifier* (M‑5(iv)): the
two are inequivalent constructions and the check does not extend. **Decision: both are
right about different things, and the reason is now available.** The agreement is real
and is not a coincidence: the fixed‑covariance location tier is exactly a tier in which
(JC‑const) holds, so both constructions are instances of Theorem V.3 with the same
exact defect. It does **not** extend to the covariance sector, where (JC) fails. The
check should be kept with the hypothesis attached.

### C‑9. Is the DQM‑transfer step proved or asserted?

*Bundle route* R3.5: the pushed family "is DQM with score $\mathbb E[\ell\mid Y]$
**because $N$ carries no parameter dependence**". *Score route*: that is the step that
is silently skipped, and supplies it via Hellinger contraction plus DQM rigidity.
**Decision: the score route is right; the bundle route states the conclusion.** The
integrated stack cites the score route's Theorem A at that step (Theorem II.5's proof),
with the $f$‑divergence data‑processing hypotheses mapped: $f(u)=(\sqrt u-1)^2$ convex
on $(0,\infty)$ with $f(1)=0$, $P,Q$ probability laws, $K$ normalized Markov. The same
substitution is owed in the manuscript at `thm:cg-fisher-contraction`
(`06_general_coarsegraining.tex:170`). The bundle route's §12 names Ay–Jost–Lê–Schwachhöfer
and Chentsov without a theorem number or hypothesis mapping, which
`proof-obligations.md` requires of an `APPLICABLE_THEOREM`; that citation cannot close
the step as it stands.

### C‑10. Is coarse $\bar G$‑invariance a missing hypothesis?

*Bundle route*: SUSTAINED, "missing $\bar G$‑invariance of the coarse Fisher metric".
*Falsifier* (M‑11): PARTIALLY SUSTAINED, downgraded to a cross‑reference. **Decision:
the downgrade is correct.** `hyp:pb-regular-models` (`05c:25`) assumes the represented
action is induced by a parameter‑independent bimeasurable sample re‑coordinatization
preserving the model, and `prop:pb-statistical-tensor-descent` (`05c:54`) already
requires that to make $\bar g^F$ a vertical tensor at all; applied at the coarse scale
that **is** the invariance. The residue is real but small: `sec:pb-fisher-defect`
(`05c:673`) never instantiates `hyp:pb-regular-models` at the coarse scale, so diagram
(D3)'s cancellation of the $c$‑dependent gauge factor $\widehat{\bar\rho}(\varsigma(c))$
has no visible source. Severity: cross‑reference (edit S‑1), not a new hypothesis.

### C‑11. Is the `CE-ACTION-LP` witness valid?

*Score route* (`:432-436`): for $\pi=\mathcal N(0,1)$ and $\varphi=-x^2$, "no two‑sided
neighborhood exists". *Falsifier* (M‑3): false. **Decision: the falsifier is right, and
the register entry is not at fault.** $\pi(e^{tx^2})=(1-2t)^{-1/2}$ is finite on the
two‑sided $(-1/2,1/2)$; the report contradicts itself nine lines later by correctly
citing `prop:ig-hermite-exponential-domain`. The register entry
(`counterexample-register.md:11`) asserts only nonintegrability of $e^{x^2}$, the true
$t=1$ statement. Replacement witness: odd $\mathrm{He}_k$ with $k\ge3$, e.g.
$\mathrm{He}_3=x^3-3x$, for which the normalizer diverges for **every** $t\ne0$ because
the cubic dominates the Gaussian quadratic on one tail (III.3, Part XI Block 11). The
conclusion the witness supports — that the $L^2/\mathbb R\mathbf 1$ score isometry and
the nonlinear bounded‑action chart are different objects — survives intact, so
`score-action-compatibility` was never endangered.

### C‑12. Does Theorem G's proof establish joint DQM?

*Score route*: "the joint density … whose logarithm has $\theta$‑derivative … Squaring
and integrating gives (6.1)." *Falsifier* (M‑9): fiberwise DQM plus $\kappa$‑measurability
does not give joint DQM. **Decision: the falsifier is right; the conclusion is true
under a hypothesis that must be stated.** The obstruction is standard: with
$\kappa(\{n\})=2^{-n}$ and inner remainders $r_n(u)=u^2\,2^n\mathbf 1\{|u|\in(2^{-n-1},2^{-n}]\}$,
each $r_n(u)=o(u^2)$ while $\sum_n\kappa_nr_n(u)/u^2\equiv1$ along a sequence $u\to0$.
The repair is the hypothesis **$\kappa$‑uniform DQM**: the family of Hellinger
remainders admits a $\kappa$‑integrable dominating envelope, or $\mathcal C$ is finite,
or the remainder is uniform in $c$. **This is L‑JDQM, discharged for every tier the
stack uses:** Tier F has a compact base and a smooth finite‑dimensional Gaussian
location family whose Hellinger remainder is uniform in $c$ by compactness, and the
mixture tier of C‑6 is used only on finite bases. Note also that §1 of the score route
goes to some length to avoid differentiating under an integral sign; §6 reintroduces the
interchange silently.

### C‑13. Is "nonunit weights are incompatible with exactness" as stated?

*Score route* (C4). *Falsifier* (M‑12(a)): needs the two marginal Fisher forms to be
independently excitable. **Decision: the falsifier is right**; the qualification holds
in the report's own Gaussian instance and must be stated. Adopted in IV.4.

### C‑14. Is Theorem E's biconditional a biconditional?

*Score route* (`:1077`): "**if and only if** $f_\#\mu=\bar\mu$". *Falsifier* (M‑12(b)):
sufficient for a fixed instance, necessary only when quantified over all admissible
coarse data. **Decision: the falsifier is right.** V.6 states (X1) as a declaration
condition rather than as an instancewise biconditional.

### C‑15. Is "closed and complemented" redundant?

*Timeless route* N5 requires both. *Falsifier* (M‑12(e)): redundant in the strong tier.
**Decision: the falsifier is right.** A strong metric makes each tangent space
Hilbertable, so closed subspaces are automatically complemented; the pair of conditions
bites only in the weak/Banach tier. Recorded in IV.3.

### C‑16. Are "inherited" closures corroboration?

*Timeless route* closes five of twelve claims `PROVED (inherited)`. **Decision: they are
not evidence.** Under `adversarial-verification.md`, role agreement is not evidence. The
effective independent route count is two for those five claims and one for
`score-action-compatibility`. Every row of Part VII was re‑derived here rather than
inherited, which is why no row of Part VII cites an inheritance.

---

## Part IX — Exact repair instructions, by file and anchor

This part discharges brief item 8. Prefixes: **L** ledger/register, **S** source
(manuscript), **N** notation, **P** provenance. Line numbers are those of the bound
digests in §0.1. **This pass applies none of these edits**; it specifies them.

**Scope guard, binding on every edit below.** Task 11 scope is preserved: nothing
here touches the interaction tier, the retained projection, the beta data, or the
fixed objects. No edit introduces physical time, a Lorentzian signature, a causal
structure, or a canonical connection. Every connection remains a declared datum, every
duration remains connection‑ and metric‑relative, and the refusal to bridge $\tau$ to a
clock reading is retained verbatim.

### IX.1 Ledger and register (`claim-ledger.json`, `dependency-dag.json`, `counterexample-register.md`)

| Id | Target | Edit |
| --- | --- | --- |
| **L‑1** | `claim-ledger.json:82` (`horizontal-defect-anomaly`) | Delete "positivity follows only when that defect vanishes." Replace with: "*Vanishing of the horizontal defect is sufficient for base positivity. The exact criterion is $2\,\bar g^F(T^V\Psi D^\omega sX,A_\Psi(s;X))+\|A_\Psi(s;X)\|^2_{\bar g^F}\le\delta_\Psi(X,X)$ for every $X$, equivalently $\|D^{\bar\omega}\bar s(T_cfX)\|_{\bar g^F}\le\|D^\omega sX\|_{g^F}$. The pointwise margin is sufficient and not necessary.*" Update the falsifier to: "a positivity claim asserted from $A_\Psi\ne0$ alone, or a necessity claim for $A_\Psi=0$." |
| **L‑2** | `claim-ledger.json:83` (`pullback-compatibility`) | Replace "horizontal‑lift‑compatible bundle morphisms" by "bundle morphisms whose scale‑connection defect form satisfies the isotropy condition $\mathfrak A_{\mathcal P}(X)\in\bar{\mathfrak g}_{\bar s(f(c))}$". Replace "the vertical mismatch term is retained" (singular) by "the **two** retained tensors $-\mathcal X_\Psi-\mathcal Q_\Psi$ are retained, with $\mathcal X_\Psi$ signed and $\mathcal Q_\Psi\succeq0$". |
| **L‑3** | `claim-ledger.json:85` (`configuration-map`) | Keep `OPEN`. Record in the statement that the coarse configuration map is written $\mathsf R_\ell$, **and that $\widehat R_\ell$ is unavailable** because `07b_agent_network_rg.tex:2196` assigns it to $J_\ell^{-1}R_\ell J_\ell$. Update the falsifier to name all six current $\mathcal R$ assignments. |
| **L‑4** | `claim-ledger.json:79,83,84` | Extend `assumption_ids`. `bundle-fisher-defect`: add family‑level domination, $K(x,\mathsf Y)=1$ for every $x$, **family closure**, smoothness of $q$ between the declared models, $\widehat{\bar\rho}(\bar G)$‑invariance of $\bar g^F$, and the measurable $\theta$‑smooth version selection for $p\mapsto T^V_p\Psi$. `pullback-compatibility`: the same, plus the isotropy condition. `configuration-fisher-metric`: add **(H‑CONFIG‑F)**, (X1), and (X2). |
| **L‑5** | `claim-ledger.json`, `dependency-dag.json` | Add the six claims of VII.3 with the ids, statements, quantifiers, assumptions, and falsifiers given there, and the edges of VII.4. Without them the compound target is not atomized. |
| **L‑6** | `claim-ledger.json:84` (`configuration-fisher-metric`) | Add to the falsifier list: "a configuration manifold declared but not exhibited", and "a strong metric asserted on an infinite‑dimensional manifold without two‑sided bounds on $w$ and on the fiber Fisher form". |
| **L‑7** | `counterexample-register.md:11` (`CE-ACTION-LP`) | Keep the true $t=1$ statement. **Replace the witness** by odd $\mathrm{He}_k$, $k\ge3$: $\varphi=\mathrm{He}_3=x^3-3x\in L^2_0(\gamma)$ has $N_3(t)=+\infty$ for every $t\ne0$. Add the explicit correction that $\varphi=-x^2$ is **not** such a witness, since $\pi(e^{tx^2})=(1-2t)^{-1/2}$ is finite on the two‑sided $(-1/2,1/2)$. |
| **L‑8** | `counterexample-register.md` | Promote to reconstructed, with this artifact as the evidence link: `CE-HORIZONTAL-ANOMALY`, `CE-SECTION-DESCENT`, `CE-HISTORY-COLLAPSE`, `CE-DURATION-MISMATCH`. Add new entries: `CE-AVG-NONCONTRACTION` (V.3, ratio $5000/10201$, target = generic averaging‑as‑contraction); `CE-MIXTURE-VS-CHART` (V.4, target = identifying the mixture defect with the chart‑barycenter defect); `CE-BASE-COCYCLE-RESIDUAL` (II.6, target = the printed correction, residual $-\tfrac23a_1(a_1+1)$); `CE-NONSMOOTH-DESCENT` ($f(x)=x^3$); `CE-ORIENTATION-REVERSAL`, `CE-PARTIAL-TRAVERSAL`, `CE-INDEPENDENT-ORBIT`, `CE-EQUAL-OBJECTIVE`; and `CE-NO-PRINCIPAL-MAP` / `CE-NO-GLOBAL-SECTION` as scope notes on declared data. Re‑type the base‑measure reversal witness on a disjoint union of two copies of $\mathbb R$, since a two‑point discrete set has $\operatorname{Sym}^2T^*\mathcal C=0$. |
| **L‑9** | `claim-ledger.json` `H-HISTORY` | Split: the mathematical content becomes the theorem `coordinate-independence` (VII.3); the residual declared refusal retains **only** the physical‑time identification. A provable statement must not be carried as an assumption. |

### IX.2 `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex`

| Id | Anchor | Edit |
| --- | --- | --- |
| **S‑1** | `sec:pb-fisher-defect`, `:673` | Name the two unstated hypotheses: **family closure** $N_\star(\mathcal B)\subseteq\bar{\mathcal B}$ and **smoothness of the law‑fiber map $q$** between the declared parametrized‑measure models (affinity of $N_\star$ on the cone of measures does not give either). **Instantiate `hyp:pb-regular-models` at the coarse scale** and cite it for $\widehat{\bar\rho}(\bar G)$‑invariance of $\bar g^F$, which is what cancels the $c$‑dependent factor $\widehat{\bar\rho}(\varsigma(c))$ in the local representative $\psi_c=\widehat{\bar\rho}(\varsigma(c))\circ q$ (diagram (D3)). |
| **S‑2** | after `eq:pb-covariant-jet-chain-rule`, `:609` | Display the exact signed comparison $h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}=\delta_\Psi-\mathcal X_\Psi-\mathcal Q_\Psi$ (II.2) with $\mathcal X_\Psi$ marked **signed** and $\mathcal Q_\Psi\succeq0$; add the exact criterion II.3(3); add the strict‑negativity witness ($A=0$, $\bar A=-a\,dx$, identity kernel, difference $-a^2dx^2$). The caption of `fig:pb-pullback-naturality` says the missing vertical term is recorded rather than suppressed; the missing **tensors** currently appear nowhere. |
| **S‑3** | `thm:pb-pullback-fisher-defect`, `:687` | Retain the `\mathcal D\Psi=0` guard (it is correct as written and is certified). Add the quantified statement of what is retained when the guard is dropped. In the proof, replace the DQM‑transfer assertion by a citation of the score route's Theorem A with its $f$‑divergence data‑processing hypothesis mapping. |
| **S‑4** | `thm:pb-fisher-defect-cocycle`, `:779-795` | (a) Type the two arrows: declare the base maps, connections, and sections; "composable smooth statistical bundle morphisms" is currently untyped. (b) Keep `eq:pb-fisher-defect-cocycle` (`:788`) — it is certified. (c) **Add the base cocycle** with the corrected residual in one of the two equivalent forms (II.5b) or (II.5c), never the hybrid, together with the one‑line consistency check that the two forms agree. (d) Replace the final sentence's "If the connections are compatible" by the isotropy criterion II.6(3), and separate the **two distinct hypotheses**: the cocycle needs only stage‑one vanishing; reading $\delta_{12}$ as $h_1-f_{12}^*h_2$ needs stage‑two vanishing as well. (e) State the sharp criterion II.6 and record that S1 is sufficient and **not** necessary. |
| **S‑5** | `:15`, `:652` (figure caption), `:791` | Replace "connection‑compatible" / "the connections are compatible" by the isotropy condition $\mathfrak A_{\mathcal P}(X)\in\bar{\mathfrak g}_{\bar s(f(c))}$, defined once. The phrase occurs at five sites in the manuscript and is defined at none; the other two are `06_general_coarsegraining.tex:202` (S‑21) and `08_infogeometry.tex:512` (S‑27). |
| **S‑6** | `eq:pb-coarse-related-sections`, `:588` | **Discharge the smoothness hedge**: under a surjective submersion, smoothness of the descended factor is a theorem, not an obligation. Add (P1)$\Leftrightarrow$(P2)$\Rightarrow$(P3) with (P3)$\Rightarrow$(P2) under connected fibers; the $S^1\to\{*\}$ witness; the $f(x)=x^3$ witness showing the submersion hypothesis is load‑bearing; and the statement that the descendable set can have empty interior in the $L^2$ tier — **scoped to a collapsing $f$**, since a diffeomorphism descends everything. |
| **S‑7** | `hyp:pb-weighted-product-geometry`, `:219` | Add the cross‑scale conditions (X1) $f_\#\mu=\bar\mu$ and (X2) $\bar w_x\circ f\le w_x$, with the display of V.6 showing that positivity of the two‑channel comparison fails without (X2) even at zero anomaly. State that the weights are a declared modeling choice, exact only at unit value and only under independence. |
| **S‑8** | `prop:pb-statistical-tensor-descent`, `:54` | Replace the one‑sentence proof by the two‑line argument: $\iota_{ug}=\iota_u\circ\widehat\rho(g)$, so $\tau^{ug}=\tau^u$ exactly when $\widehat\rho(g)^*\tau=\tau$; smoothness by local sections of $P$. |
| **S‑9** | `thm:pb-pullback-gauge-invariance`, `:111` | Retitle to **passive covariance** and record that the tensors are **not** invariant under the active gauge group at fixed connection (witness: trivial $\mathbb R$‑bundle, $h=0$ becomes $dx^2$ under $F(u(x)g)=u(x)(x+g)$), so that the `ESTABLISHED` tag is not read as an active‑gauge invariance claim. The following remark already separates passive invariance from connection independence and should be kept. |
| **S‑10** | the convention sentence "$D_A=d+\widehat\rho_{x*}(A)$" preceding `prop:pb-pullback-connection-change` | $\widehat\rho_{x*}(A)$ is a linear representation of $\mathfrak g$ and is undefined for a nonlinear law fiber $\mathcal B\subseteq\mathcal P(\mathsf K)$. Replace by the fundamental vector field $\zeta_{A(X)}$, as the frame‑free `eq:pb-connection-difference-vertical` already does, or restrict the sentence to a linear associated‑vector‑bundle realization. The **sign** is verified correct under the corrected object. |
| **S‑11** | `thm:pb-pullback-rank-quotient`, `:262`; `eq:pb-null-basicness` | Cite the constant‑rank theorem **for vector‑bundle morphisms**, not for smooth maps. Add the checkable basicness criterion $g^F(\mathcal L_Z(D^\omega s)X,D^\omega sY)+g^F(D^\omega sX,\mathcal L_Z(D^\omega s)Y)=0$ for $Z\in\Gamma(\ker D^\omega s)$, and note that it does not depend on the choice of metric connection. |

### IX.3 `manuscripts/gauge_vfe_rg/05d_relational_inference.tex`

| Id | Anchor | Edit |
| --- | --- | --- |
| **S‑12** | `hyp:hist-regular-metric-domain`, `:204`; `hyp:hist-regular-section-space`, `:91` | Import Construction IV.1 and Theorem IV.2 as an **exhibited** tier: the finite‑dimensional parameterized family, the constant Gram metric $\Phi_{ab}=\int\phi_a^{\!\top}\Sigma_0^{-1}\phi_bw\,d\mu$, strongness automatic in finite dimensions, and nondegeneracy as the rank test (degenerate whenever $N>MK$ for an $M$‑atom design). Then choose explicitly between the $L^2$ tier (strong, $\mathcal F$ required $C^1$ on $L^2$) and the $H^s$ tier (weak, Riesz hypothesis declared), and attach the $H^1(S^1)$ failure witness. A declared hypothesis with no exhibited model is vacuous. |
| **S‑13** | `:719-783` | Rename the configuration coarse map $\mathcal R\to\mathsf R_\ell$ throughout (see N‑1). Add Proposition V.4: at the declared tier the map is linear in the coefficients, hence $C^\infty$, gauge equivariant because the translation action is linear and commutes with $\kappa_{\bar c}$‑barycenters, and its compatibility is the matrix inequality $T^{\!\top}\bar\Phi T\preceq\Phi$. State the compatibility as an explicit **hypothesis discharged by Theorem V.3**, not as a corollary of any contraction theorem. |
| **S‑14** | `prop:hist-oriented-semiconjugacy`, `:723-751` | (a) State (SC) with $a_\ell$ **continuous**, and add Lemma VI.1 so that continuity and uniqueness are consequences off the coarse critical set, and so that the vacuity of "$a>0$" on that set is visible. (b) Name the field in "On a noncritical domain": the load‑bearing reading is $X_{\ell+1}\ne0$ on $\mathsf R_\ell(U)$. (c) **Reorder the proof**: build the reparameterized curve on $\Sigma_Q$ first, verify it solves the autonomous equation, and conclude the domain inclusion from maximality. The current proof asserts that $\bar\Phi_{\sigma_Q(t)}$ is defined, which is what must be proved; the repair costs three lines and yields $\Sigma_Q\subseteq\bar J^{\max}$ as a bonus. (d) Add the completeness‑transfer corollary and the $\arctan$ witness showing $\inf a_\ell>0$ is needed. |
| **S‑15** | `:764-786` | Add the two noncollapse hypotheses wherever nonconstant or global shared‑history language is used, with the collapse witness ($\mathsf R_\ell\equiv Q^*$, $X_{\ell+1}\equiv0$). |
| **S‑16** | `def:hist-curve-types`, `:42-63` | Declare the **pointwise** trichotomy plus the stationary case, then define the interval labels as "of that type at every parameter", and record that the interval labels are no longer exhaustive. No downstream theorem changes, because every downstream use is on a subinterval of one pointwise type. |
| **S‑17** | `thm:hist-record-clock-contraction`, `:627`; `:611-683`; `:753-759` | State the duration criterion: the **necessary and sufficient** condition is the scalar inequality $\|T\mathsf R_\ell X_\ell\|_{\mathsf G_{\ell+1}}\le\|X_\ell\|_{\mathsf G_\ell}$ along the orbit; the tensorial $\mathsf R_\ell^*\mathsf G_{\ell+1}\preceq\mathsf G_\ell$ is sufficient and strictly stronger. Record that $a_\ell$ **cancels** from geometric length, so it is a reparameterization datum and not a rate. Attach both witnesses to the existing sentence "Either condition without the other is insufficient", which is currently asserted with neither: the metric‑declaration reversal (zero information loss, doubled duration) and the independently‑recomputed‑orbit witness. Record the reconciliation $\|\mathscr L_b\|\le\sqrt b$, not $\le1$. |
| **S‑18** | `eq:hist-continuum-clock-speed`, `:501` | Name the **contextual‑locality** hypothesis that the single‑integral form presumes: the declared recognition law has no cross‑context terms. If it couples sections at $c\ne c'$, the pullback carries a double integral that no single integral represents. |
| **S‑19** | `:529-536` | Restate the gauge‑quotient sentence: in the strong Hilbert tier the decisive condition is **closedness of the orbit tangent**, which gives attainment by orthogonal projection; the longer list is the correct Banach generalization, where closed no longer implies complemented. The current sentence "free, proper, and isometric is not by itself enough" is asserted **without a witness**, and the available witness establishes only the *free and isometric* version, since a dense non‑closed translation subgroup does not act properly. Either supply a proper witness or restate. |
| **S‑20** | `hyp:hist-exact-vfe-lift`, `:213` | Record the exact joint‑versus‑product criterion: equality with unit weights holds iff $\|L-L_b-L_m\|^2=2\langle L_b,L_m\rangle$; independence is the clean sufficient condition; a fixed non‑independence copula does **not** suffice; nonunit weights are exact only at unit value; and no Loewner ordering holds in either direction. Record that two right inverses of the same configuration extraction give different metrics, so the configuration Fisher metric is **not** a function of the displayed configuration. |

### IX.4 Other source files

| Id | File and anchor | Edit |
| --- | --- | --- |
| **S‑21** | `06_general_coarsegraining.tex` `thm:cg-fisher-contraction`, `:170`; `:202` | Supply the DQM‑transfer proof (Hellinger contraction plus DQM rigidity) rather than asserting it from parameter independence; replace "connection‑compatible" at `:202` per S‑5. |
| **S‑22** | `07_general_renormalization.tex` `eq:rg-scale-intertwiner`, `:251`; `eq:rg-associated-scale-map`, `:258` | State the necessity as a **biconditional under the declared $\mathcal P$**, and supply the two‑line quotient computation on representatives $(u,\beta)$ and $(ug,\widehat\rho(g)^{-1}\beta)$. Add family closure and smoothness of $q$ as hypotheses. Record the degenerate case: if $\bar{\mathcal B}$ is a single $\bar G$‑fixed point, (I) is vacuous rather than necessary. Display the composition law at `:260-264`, which currently asserts it. |
| **S‑23** | `07_general_renormalization.tex` `eq:rg-principal-scale-map`, `:243` | State the existence obstruction: an equivariant $\mathcal P$ over $f$ exists **iff** $P\times_\kappa\bar G\cong f^*\bar P$. This is a scope note on a declared datum admitted by `H-GAUGE`, not a refutation. |
| **S‑24** | `07_general_renormalization.tex` `eq:rg-cross-morphism-defects`, `:288`; `eq:rg-cross-connection-defects`, `:300`; `eq:rg-principal-connection-naturality`, `:319` | These record cross‑scale defects as ordered pairs of maps to be compared and give only the sufficient principal‑level condition. Add the **ordered composition law** (II.3) and the **connection‑level cocycle** $\mathfrak A_{\mathcal P_{02}}=\mathcal P_{01}^*\mathfrak A_{\mathcal P_{12}}+d\kappa_{12}\circ\mathfrak A_{\mathcal P_{01}}$, with the warning that $A_{02}=A_{01}+A_{12}$ is a type error. |
| **S‑25** | `07b_agent_network_rg.tex` after `prop:rg-action-score-isometry`, `:762-819` | Record that on $L^2/\mathbb R\mathbf 1$ the realizing path is the **quadratic** DQM path of `lem:rg-dqm-realization` (`:559`), not the exponential‑action path, and that `thm:rg-bounded-action-calculus` (`:190`) is undefined there. Cite the odd‑$\mathrm{He}_k$ witness ($k\ge3$), **not** the $\mathrm{He}_2$ direction. The existing text at `:812-819` already makes the distinction and needs only the corrected witness. |
| **S‑26** | `07b_agent_network_rg.tex` `prop:rg-score-block-lift`, `:601`; `thm:rg-score-pushforward-defect`, `:654` | Record explicitly that $\mathscr I_b$ is a **lift between different reference tangents**, not a pushforward along any channel, and that **no** parameter‑independent normalized Markov kernel realizes $b$‑fold replication (a one‑line data‑processing contradiction, $b\le1$). Forbid citing the replication pair as a Markov‑contraction counterexample. |
| **S‑27** | `08_infogeometry.tex` `:505-527`; `:512` | Keep `prop:ig-pullback-vs-pushforward`; cross‑reference it as the reason hypothesis 2 of the configuration‑level contraction theorem fails for the Galerkin aggregation (a restriction, larger in the Loewner order by a positive‑semidefinite Schur term). Replace "connection‑compatible" at `:512` per S‑5. `prop:ig-hermite-exponential-domain` (`:364-396`) needs no change and is the source of the corrected witness. |

### IX.5 Notation and provenance

| Id | Target | Edit |
| --- | --- | --- |
| **N‑1** | `appendix_notation.tex` | Add a row typing the configuration coarse map $\mathsf R_\ell:\mathcal Q_\ell\to\mathcal Q_{\ell+1}$, smooth, with explicit non‑identification against $K_\ell$, $N_\star$, $\Psi$, $\mathcal R^H$, $\mathcal R_b$, $M_\ell$, $C_{\ell,s}$, $\widehat{\mathcal R}_\ell$, $\widehat R_\ell$, the root‑vertex set $\mathcal R$, and the descent ray $\mathcal R^-_{\mathcal F_i}$. **Do not use $\widehat R_\ell$** (taken at `07b:2196`). `\mathsf{R}`, `\mathfrak{r}`, `\mathfrak{q}`, `\mathsf{C}` are all free. |
| **N‑2** | `appendix_notation.tex` | Add rows for $A_\Psi=\mathcal D\Psi$, $\mathfrak A_{\mathcal P}$, $\Delta_F^\Psi$, $\delta_\Psi$, $\mathcal X_\Psi$, $\mathcal Q_\Psi$, and $\mathsf G_\ell$, each with its bundle of definition, so that the fiber tensor, its base pullback, and the configuration metric are visibly three different objects. |
| **N‑3** | `05d_relational_inference.tex:287`, `04_generative.tex:22`, `05_elbo.tex:388-434`, `07b:185,2074`, `07_general_renormalization.tex:45-48` | Leave these five $\mathcal R$ uses in place; they are prior occupants. Only the configuration coarse map moves. Record the disambiguation in the notation appendix rather than renaming five established symbols. |
| **P‑1** | `manuscripts/gauge_vfe_rg/main.pdf` | The bundled PDF at the base revision is byte‑identical to the 2026‑08‑01 build while nine `.tex` inputs changed in the Task 5–9 commits, so it does not render the current sources. `pullback-ledger-provenance` and `minor-emergent-time-keyword` cannot close until it is regenerated. Mechanical; not adjudicated here beyond confirming the three routes agree. |
| **P‑2** | route‑C evidence line anchors | Anchors have shifted by five lines against the current ledger digest. Re‑anchor before any citation of those lines is entered as evidence. |

### IX.6 What must **not** be transcribed

1. The printed base‑cocycle correction from `task-10-bundle-pullback-analysis.md:976-983`
   in its hybrid form. Use (II.5b) or (II.5c).
2. The Block C headline "the base cocycle holds identically". It is the unconditional
   telescoping under a symbol collision.
3. The $\mathrm{He}_2$ / $\varphi=-x^2$ witness for `CE-ACTION-LP`.
4. "Averaging over the base loses information" as an unconditional statement, and
   Theorem G attached to a chart barycenter into a non‑mixture‑closed family.
5. "On a genuinely infinite‑dimensional configuration manifold it induces one nowhere"
   unscoped.
6. Route D's `PROVED` for `configuration-fisher-metric` and `PROVED (typing)` for
   `configuration-map`.
7. The rename of the configuration coarse map to $\widehat R_\ell$.
8. Any "inherited" closure counted as a third route.

---

## Part X — The proposed integrated theorem stack

One conditional effective theory. The hypothesis set is stated once, the theorems are
stated in dependency order, and §X.3 proves the hypotheses jointly satisfiable with a
nonempty domain by verifying every one of them on a single explicit witness.

### X.1 The hypothesis set

| Id | Hypothesis |
| --- | --- |
| **H0 Regularity** | `hyp:geo-smooth-tier` and `hyp:pb-regular-models` in full, **at both the fine and the coarse scale**, including positive definiteness of $g^F,\bar g^F$ and their invariance under the represented actions. |
| **H1 Domination** | One $\sigma$‑finite family‑level dominating measure with a fixed jointly measurable density version. |
| **H2 DQM** | Statistical paths differentiable in quadratic mean with centered finite‑$L^2$ scores. |
| **H3 Normalization** | $K$ is a parameter‑independent Markov kernel with $K(x,\mathsf Y)=1$ for **every** $x$ — not almost every $x$, since the exceptional set would otherwise depend on $\theta$. |
| **H4 Joint law** | $\mathbb P_\theta(dx,dy)=P_\theta(dx)K(x,dy)$ and its reverse conditioning. |
| **H5 Family closure** | $N_\star(\mathcal B)\subseteq\bar{\mathcal B}$, with $q=N_\star|_{\mathcal B}$ smooth between the declared parametrized‑measure models, and a jointly measurable $\theta$‑smooth version selection for $p\mapsto T^V_p\Psi$. |
| **H6 Bundle** | A declared $\kappa$‑equivariant $\mathcal P$ over $f$ — whose existence is the topological condition $P\times_\kappa\bar G\cong f^*\bar P$, **to be stated, not assumed away** — together with the law‑fiber intertwining (I). |
| **H7 Isotropy** | For base positivity and for the sharp cocycle: $A_\Psi(s;\cdot)=0$, equivalently $\mathfrak A_{\mathcal P}(X)\in\bar{\mathfrak g}_{\bar s(f(c))}$. This is the definition that replaces the undefined phrase "connection‑compatible". |
| **H8 Descent** | Where a section descent is used: $f$ a surjective submersion with connected fibers. Then (P1)$\Leftrightarrow$(P2)$\Leftrightarrow$(P3) and the descended section is automatically smooth. |
| **H9 Cross‑scale declaration** | (X1) $f_\#\mu=\bar\mu$ and (X2) $\bar w_x\circ f\le w_x$ for both channels. Without these, **no** integrated‑metric comparison across scales is available even at zero anomaly and zero information loss. |
| **H10 Configuration tier** | **(H‑CONFIG‑F)**: Construction IV.1 at every scale where a natural‑gradient field or a Fisher duration is asserted; or tier (b1) with two‑sided bounds on $w$ and on the fiber Fisher form, with $\mathcal F$ required $C^1$ on $L^2$. There is no third option in the infinite‑dimensional case. |
| **H11 Coarse configuration map** | $\mathsf R_\ell:\mathcal Q_\ell\to\mathcal Q_{\ell+1}$ **separately declared** and smooth, with (A‑i)–(A‑v) and hypothesis **(JC)** where an averaging construction is used. |
| **H12 History tier** | $a_\ell$ continuous and strictly positive; "noncritical" read as $X_{\ell+1}\ne0$ on $\mathsf R_\ell(U)$; the maximal‑interval condition $\Sigma_Q\subseteq\bar J^{\max}$, upgraded to equality only under $J_Q^{\max}=\mathbb R$ and $\inf a_\ell>0$; and the duration criterion of Theorem VI.5(3), which does **not** follow from any fiberwise contraction theorem. |
| **H13 Retained refusals** | No operational bridge from Fisher duration to a clock reading. $\ell$, $r$, and $\tau^{(\ell)}$ kept as three distinct coordinates. The metric relativity of $\tau$ recorded alongside the operational obligations. No physical time, no Lorentzian signature, no causal structure, no canonical connection. |

### X.2 The stack, in dependency order

| # | Theorem | Hypotheses | Where proved |
| --- | --- | --- | --- |
| **T1** | Strictness of the sample/law/bundle typing: $N\Rightarrow N_\star\Rightarrow q$, and no arrow reverses. | H0, H5 | Lemma I.1 |
| **T2** | Descent: $\widetilde\Psi$ factors through the associated‑bundle quotient **iff** (I); $\Psi$ is then smooth, preserves verticality, and $T^V\Psi=Tq$ in the frame pair. | H0, H5, H6 | (D2), (D3) |
| **T3** | Score/action compatibility: $\mathscr S_\pi$ is a Fisher isometry onto $L^2_0$, $U|_{L^2_0}=R$, and the square (D8) commutes; the scalar $L^2$ defect on the action quotient **is** the Fisher information loss. | H1–H4 | III.1 |
| **T4** | Markov Fisher contraction: $\|R\|\le1$, and $\Delta_F^\Psi(w,w)=\mathbb E\operatorname{Var}(\ell_w\mid Y)\ge0$ with equality iff the fine score is $\sigma(Y)$‑measurable. No normalized channel can increase Fisher. | H1–H5, H0 | III.1–III.2, Theorem II.5 |
| **T5** | Replication placement: $\|\mathscr I_b\|=\sqrt b$, and **no** parameter‑independent normalized Markov kernel realizes $b$‑fold replication for $b\ge2$. $\sqrt b$ belongs to the reference identification and to the metric declaration, never to a channel. | H1–H4 | Propositions III.3, III.4 |
| **T6** | Exact first jet: $D^{\bar\omega}\bar s(Tf X)=T^V\Psi(D^\omega sX)+A_\Psi(s;X)$. | H0, H6 | Theorem II.1 |
| **T7** | Exact signed comparison: $h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}=\delta_\Psi-\mathcal X_\Psi-\mathcal Q_\Psi$, with $\mathcal X_\Psi$ signed and $\mathcal Q_\Psi\succeq0$; and the exact positivity criterion II.3(3). | H0, H6 | Theorems II.2, II.3 |
| **T8** | Zero anomaly: under H7, $h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}=\delta_\Psi\succeq0$; the criterion for $A_\Psi=0$ is the isotropy condition, sufficient always and necessary under infinitesimal effectiveness. | H0, H5, H6, H7 | Theorems II.5, II.6 |
| **T9** | Ordered composition and connection cocycle: (II.3) and $\mathfrak A_{\mathcal P_{02}}=\mathcal P_{01}^*\mathfrak A_{\mathcal P_{12}}+d\kappa_{12}\circ\mathfrak A_{\mathcal P_{01}}$; the unweighted sum is a type error. | H0, H6 | Theorems II.6(4), II.7 |
| **T10** | Vertical cocycle (unconditional) and **corrected sharp base cocycle**: (II.4), (II.5a–c), and the equal‑seminorm criterion (II.6) with sufficient conditions S1–S3. | H0, H5, H6 | Theorem II.8 |
| **T11** | Configuration manifold and strong metric: Construction IV.1 gives a nonempty finite‑dimensional $\mathcal Q_\ell$ with a constant Gram metric, strong automatically, nondegenerate iff the design is linearly independent; the infinite‑dimensional strong/weak boundary is exactly the $L^2$/$H^s$ dichotomy. | H10 | Theorem IV.2, IV.3 |
| **T12** | Projectability: (P1)$\Leftrightarrow$(P2)$\Rightarrow$(P3), converse under connected fibers, smoothness automatic; a pointwise bundle morphism induces only a **partial** map on section configurations. | H0, H8 | Theorems V.1, V.2 |
| **T13** | Separately declared coarse configuration map: at the declared tier $\mathsf R_\ell$ is linear, hence $C^\infty$, gauge equivariant, with compatibility the matrix inequality $T^{\!\top}\bar\Phi T\preceq\Phi$. | H10, H11 | Proposition V.4 |
| **T14** | **Exact averaging defect (L‑AVG)**: $\Delta_{\mathrm{avg}}\ge0$ under (JC); and the exact three‑term identity channel loss $+$ weight gap $+$ context (Jensen) gap under (JC‑const). Generic averaging is **not** a contraction without (JC). | H0, H5, H9, H11 | Theorem V.3 |
| **T15** | Theorem G is the mixture‑tier instance of T14: the law‑chart barycenter into a mixture‑closed coarse family has $\Delta_{\mathrm{avg}}=\mathsf G^\kappa-I_{\bar P}=\mathbb E\operatorname{Var}(\ell\mid Y)$. | H0–H5, H11 | V.4 |
| **T16** | Semiconjugacy: (SC) with $a_\ell$ automatically unique and $C^k$ off the coarse critical set; the flow identity with $\Sigma_Q\subseteq\bar J^{\max}$; completeness transfers iff $\inf a_\ell>0$; $a>0$ carries the entire orientation content. | H10, H12 | Lemma VI.1, Theorem VI.2 |
| **T17** | Noncollapse: (SC) alone permits total collapse; a nonconstant shared history needs the two additional hypotheses. | H10, H12 | Proposition VI.3 |
| **T18** | Duration: $a_\ell$ **cancels** from geometric length; the necessary and sufficient comparison condition is the scalar inequality in the direction $X_\ell$; the tensorial Loewner condition is sufficient and strictly stronger; fiberwise contraction lifts exactly under Theorem VI.6, of which T14 is the strict generalization admitting a collapsing base. | H10–H12 | Theorems VI.4, VI.5, VI.6 |
| **T19** | Natural‑gradient sufficiency: equality of objectives does not intertwine gradients; under (FC), horizontal conformality gives (SC) with $a_\ell=\chi_\ell'\varphi_\ell^2$; a pointwise Markov configuration map qualifies only on a Fisher‑sufficiency locus. | H10–H12 | Theorem VI.7 |
| **T20** | Coordinate independence: $\ell$, $r$, $\tau^{(\ell)}$ pairwise independent; $\tau$ reparameterization invariant and metric‑relative; strict monotonicity $\ne$ regular coordinate; no regional clock potential without a closed zero‑period one‑form. | H12, H13 | VI.8 |

### X.3 Joint satisfiability, with a nonempty domain

The stack is worthless if H0–H13 cannot hold together. They can. **Tier F and Tier F′
of §V.5 satisfy every one of them simultaneously**, and every quantity below
was computed in exact arithmetic (Part XI, Blocks 6 and 9).

**The witness.** $\mathcal C_\ell=S^1$ with normalized arclength $\mu$;
$G=\bar G=(\mathbb R,+)$ acting by translation of the mean, $\kappa=\mathrm{id}$;
$P=\bar P$ trivial, $\mathcal P=\mathrm{id}$, both connections flat;
$\mathcal B=\{\mathcal N(m,1)\}$, $\bar{\mathcal B}=\{\mathcal N(m,2)\}$; sample kernel
$N(x,\cdot)=\mathcal N(x,1)$; basis $\{1,\cos\theta,\sin\theta\}$; $w=\bar w=1$;
$\mathcal F(\xi)=\tfrac12|\xi|^2$.

| Hypothesis | Verified on the witness |
| --- | --- |
| H0 | Gaussian location families with $g^F=1$, $\bar g^F=\tfrac12$, both positive definite; translation invariance at both scales |
| H1–H2 | Lebesgue dominates; a Gaussian location family is DQM with score $\ell_{\dot m}=\dot m(x-m)$, centered and in $L^2$ |
| H3 | $N(x,\cdot)=\mathcal N(x,1)$ is a probability measure for **every** $x$, and carries no parameter |
| H4 | $\mathbb P_m(dx,dy)=\mathcal N(m,1)(dx)\mathcal N(x,1)(dy)$; reverse conditioning is Gaussian |
| H5 | $N_\star\mathcal N(m,1)=\mathcal N(m,2)\in\bar{\mathcal B}$; $q(m)=m$ is $C^\infty$; $T^V\Psi=\mathrm{id}$ |
| H6 | $P=\bar P$ trivial, so $P\times_\kappa\bar G\cong f^*\bar P$ holds; $\mathcal P=\mathrm{id}$ is equivariant; (I) is translation equivariance of a convolution kernel |
| H7 | both connections flat and $\kappa=\mathrm{id}$, so $\mathfrak A_{\mathcal P}=0$ and $A_\Psi\equiv0$ — **zero anomaly** |
| H8 | Tier F: $f=\mathrm{id}$, a submersion with singleton (connected) fibers. Tier F′: $f\equiv*$, a surjective submersion with connected fiber $S^1$ |
| H9 | Tier F: $f_\#\mu=\mu=\bar\mu$ and $\bar w=w=1$. Tier F′: $\bar\mu=f_\#\mu$ is the unit point mass by construction, $\bar w=w=1$ |
| H10 | $\mathcal Q_\ell\cong\mathbb R^3$; $\mathsf G_\ell=\Phi=\operatorname{diag}(1,\tfrac12,\tfrac12)$, $\det\Phi=\tfrac14$, eigenvalues $\{1,\tfrac12\}$; strong automatically; the design is linearly independent in $L^2(\mu)$ |
| H11 | Tier F: $\mathsf R_\ell=\mathrm{id}$. Tier F′: $\mathsf R_\ell(\xi)=\xi_0$, linear. (JC‑const) holds because the fiber covariance is fixed, so $\bar g^F\equiv\tfrac12$ is constant in the chart |
| H12 | $a_\ell\equiv\tfrac12>0$ constant; $X_{\ell+1}=-2\Phi^{-1}\xi\ne0$ off $\xi=0$; both flows are complete linear flows, so $J^{\max}=\Sigma_Q=\mathbb R$ and $\inf a_\ell=\tfrac12>0$; $\mathsf R_\ell^*\mathsf G_{\ell+1}=\tfrac12\Phi\prec\Phi$ |
| H13 | no clock bridge is made anywhere; $\ell\in\{0,1\}$, $r$ the flow parameter, $\tau^{(\ell)}$ the Fisher length, all three exhibited as distinct |

**Nonempty conclusions on the witness.**

* $\Delta_F^\Psi=\tfrac12\succ0$: the channel is genuinely lossy.
* $A_\Psi\equiv0$, so T8 applies and
  $h^\omega_s-f^*\bar h^{\bar\omega}_{\bar s}=\delta_\Psi\succeq0$.
* Tier F: $\mathsf G_\ell-\mathsf R_\ell^*\mathsf G_{\ell+1}=\tfrac12\Phi\succ0$;
  (SC) holds exactly with $a_\ell\equiv\tfrac12$; $\nu^{\mathrm{img}}_{\ell+1}/\nu_\ell=1/\sqrt2$,
  so duration strictly contracts. T19 predicts $a_\ell=\chi_\ell'\varphi_\ell^2=\tfrac12$
  from horizontal conformality, matching the direct computation.
* Tier F′: $\mathsf G_\ell-\mathsf R_\ell^*\mathsf G_{\ell+1}=\operatorname{diag}(\tfrac12,\tfrac12,\tfrac12)$,
  which splits **exactly** into T14's channel term
  $\operatorname{diag}(\tfrac12,\tfrac14,\tfrac14)$ and Jensen term
  $\operatorname{diag}(0,\tfrac14,\tfrac14)$, with zero weight gap. The
  pointwise‑induced configuration map is undefined at every nonconstant $\xi$ here,
  while $\mathsf R_\ell$ is smooth everywhere — the concrete reason the stack declares
  $\mathsf R_\ell$ separately.

**Therefore.** H0–H13 are jointly satisfiable; the domain of the integrated theory is
nonempty and contains a witness with a genuinely lossy channel, a genuine base
collapse, a strictly contracting duration, and a nontrivial exact defect
decomposition. `H-CONFIG` has a nonempty model class, so T16–T20 are not vacuous.
No hypothesis in X.1 is idle: H3 fails for a parameter‑dependent channel (a
$\mathrm{Bernoulli}(\sigma(\lambda))$ emitter has zero fine speed and positive output
Fisher, since $\sigma'=\sigma(1-\sigma)$); H5 fails for a nonlinear Gaussian
pushforward; H7 fails in the $-a^2dx^2$ witness; H9 fails in the disjoint‑union
reversal; (JC) fails in the Gaussian moment chart with ratio $1.96$; H12's duration
criterion fails in the metric‑declaration witness with zero information loss.

### X.4 What the stack does **not** claim

* No global section, hence no global base semimetric, without a section‑existence
  hypothesis. Witness: Hopf bundle over $S^2$ with a von Mises fiber, where
  $E\cong P$ and $\pi_2(S^3)=0\ne\mathbb Z=\pi_2(S^2\times S^1)$.
* No principal scale map without the topological condition of H6.
* No active‑gauge invariance of the pullback tensors; only passive covariance.
* No quotient manifold from constant rank alone: involutivity, a regular leaf space,
  and basicness are three further hypotheses, and the contact form $dz-x\,dy$ shows
  constant rank with a nonintegrable radical.
* No Loewner ordering between the joint‑law pullback and a weighted product of marginal
  fiber metrics, in either direction.
* No duration comparison from any fiberwise contraction theorem.
* No identification of $\tau$ with physical time, no clock potential without a closed
  zero‑period one‑form, and no Lorentzian or causal structure anywhere.

---

## Part XI — Executed verification record

Two sessions, run at the base revision inside this pass, with SymPy 1.14.0 and NumPy
2.4.4 on CPython. Every value marked *exact* is rational or symbolic; the two marked
*quadrature* are numerical. **Agreement corroborates arithmetic and closes no
theorem.** Nothing in Parts I–X rests on a numerical value; the two quadratures serve
only to separate two quantities that a symbolic argument already shows are different
maps.

### XI.1 Reproduction recipe

The blocks are self‑contained and were executed from a scratch directory outside the
repository (no repository file was created or modified by them). To reproduce, run
each block's stated setup; every block is a few lines and its full inputs are printed
below. Blocks 1–7 formed session A, blocks 8–11 session B.

### XI.2 Block transcripts

**Block 1 — type‑level check of the corrected sharp base cocycle (exact, symbolic).**
Setup: $D$ a symbolic symmetric $3\times3$ form standing for $\Delta_F^{\Psi_{12}}$;
$V,A$ symbolic $3\times2$ matrices standing for $v_\bullet$ and $A_\bullet$ on a
two‑dimensional fine base; $U=V+A$. Results, all as identities of $2\times2$ symbolic
matrices:

```
Delta_F^{Psi12} symmetric                                     : True
N == corrected form 1 (coarse jet in cross slots, +quadratic) : True
N == corrected form 2 (fine  jet in cross slots, -quadratic)  : True
N == printed hybrid   (fine  jet in cross slots, +quadratic)  : False
printed - N == 2 * Delta_F^{Psi12}(A,A)                       : True
N(X,X) == -<A_X, 2 v_X + A_X>_D                               : True
N(X,X) == -<A_X, 2 u_X - A_X>_D                               : True
N == V^T D V - U^T D U   (equal-seminorm criterion)           : True
sufficient conditions:  (S1) A = 0        : True
                        (S2) Delta12 = 0  : True
                        (S3) Delta12 A = 0: True   (N is linear in D*A)
```

**Block 2 — three‑level rational instance (exact).** Bundle‑route Block B data:
$f_{01}(x)=2x$, $f_{12}(y)=3y$; fibers $\mathcal N(\mu,1),\mathcal N(\mu,2),\mathcal N(\mu,3)$
so $g_0^F=1$, $g_1^F=\tfrac12$, $g_2^F=\tfrac13$; sections $\sigma_0(x)=x$,
$\sigma_1(y)=y/2$, $\sigma_2(z)=z/6$; $A_{\omega_0}=0$, $A_{\omega_1}=a_1dy$,
$A_{\omega_2}=a_2dz$.

```
vertical cocycle  Delta02 = Delta01 + L01^* Delta12 : True
ordered composition A02 = L12(A01) + f01^*A12       : True
residual N(X,X)                                     : -2*a1*(a1 + 1)/3
check u_X - v_X == A_X                              : True
N == d12*(v^2 - u^2)                                : True
printed RHS                                         : 2*a1*(a1 - 1)/3
printed - true == 2*d12*A^2                         : True
at a1=1/10, a2=0 : true = -11/150 , printed = -3/50
zero set of the residual                            : [-1, 0]
equal-seminorm check |v| = |u| at a1 = -1           : True, with A_X = -2 != 0
```

**Block 3 — exact signed positivity criterion (exact).** R11 data, $m=1$; the
identity $h-f^*\bar h=\delta_\Psi-[2\bar g^F(v,A)+\|A\|^2]$ holds identically in
$(m,b)$.

```
identity  h - f^*hbar == delta - [2 gbar(v,A) + |A|^2] : True
 b        h-f^*hbar   LHS(crit)   delta   crit met  positive
       0        1/2           0     1/2     True      True
    1/10     79/200      21/200     1/2     True      True
   -1/10    119/200     -19/200     1/2     True      True
     1/2       -1/8         5/8     1/2    False     False
    -3/5      23/25      -21/50     1/2     True      True
```

**Block 4 — joint convexity, and the M‑5 witness (exact + one limit).**

```
moment-chart Fisher form F(Sigma,A) = A^2/(2 Sigma^2)
Hessian det = -A**2/Sigma**6            -> NOT jointly convex for A != 0
law-chart integrand G(p,pdot) = pdot^2/p
Hessian = [[2*pdot**2/p**3, -2*pdot/p**2], [-2*pdot/p**2, 2/p]]
det = 0 , trace = 2/p + 2*pdot**2/p**3  -> positive semidefinite, jointly convex
M-5 witness: fine = 1/4 , coarse = 1/(2*(delta+1)^2) , limit delta->0+ : 1/2
ratio at delta = 1/100 : 5000/10201 = 1.9605920988138419
```

The falsifier reports the Hessian determinant as $-4A^2\Sigma^{-6}$; the correct
coefficient is $-1$. Sign and conclusion unaffected (C‑7).

**Block 5 — Gaussian normalizer (exact, partly superseded).** SymPy returned
$\pi(e^{tx^2})=(1-2t)^{-1/2}$ on the principal branch and did not evaluate the
$\mathrm{He}_3$ integrals in closed form; Block 11 supplies the divergence argument
directly. Retained for the $\mathrm{He}_2$ value, which is the load‑bearing half of C‑11.

**Block 6 — Tier F Gram metric and semiconjugacy (exact).**

```
Gram matrix Phi = [[1, 0, 0], [0, 1/2, 0], [0, 0, 1/2]]
det Phi = 1/4 , eigenvalues = [1, 1/2] , positive definite: True
Rhat^* G_{l+1} = (1/2) Phi  <=  Phi = G_l  (Loewner): True
semiconjugacy T Rhat X_l = a X_{l+1} with a = 1/2   : True
nu_img / nu_l = sqrt(2)/2      (strict contraction)
```

**Block 7 — replication is not a Markov pushforward (argument, not computation).**
Recorded verbatim as Proposition III.4: if $K$ were parameter‑independent, normalized,
and Markov with $\mathcal N(x,1)K=\mathcal N(x\mathbf 1_b,I_b)$ for all $x$, then
$b=I_{\mathrm{out}}\le I_{\mathrm{in}}=1$, so $b\le1$; hence no such $K$ exists for
$b\ge2$. And $\|\mathscr I_bh\|^2=b\|h\|^2$ for centered $h$ by independence.

**Block 8 — Theorem AVG three‑term decomposition (exact, symbolic).** Setup: constant
coarse fiber metric $\bar g$ ($2\times2$ symbolic), three fine fiber metrics $g^F_a$,
symbolic linear part $L$, three tangents $Z_a$, weights $w_a$, $\bar w$, and
disintegration weights $\kappa_a$; single coarse point.

```
Davg == channel loss + weight gap + coarse-metric context variance : True
  channel  = int w (g^F - L^* gbar L)(Z,Z) dmu       >= 0 iff Delta_F^Psi >= 0
  weight   = int (w - wbar o f)(L^* gbar L)(Z,Z) dmu >= 0 iff wbar o f <= w
  variance = int wbar Var^gbar_kappa(L Z) dmubar     >= 0 iff gbar >= 0
```

**Block 9 — Tier F′ collapse, exact split (exact).**

```
Phi (fine configuration metric) = [[1, 0, 0], [0, 1/2, 0], [0, 0, 1/2]]
G_l - R^* G_{l+1} = [[1/2,0,0],[0,1/2,0],[0,0,1/2]] , positive definite: True
channel term = [[1/2,0,0],[0,1/4,0],[0,0,1/4]]
Jensen  term = [[0,0,0],[0,1/4,0],[0,0,1/4]]
channel + Jensen == G_l - R^* G_{l+1} : True
```

**Block 10 — mixture tier versus chart tier (quadrature).** Two contexts, $\kappa$
uniform, unit‑variance Gaussian location fiber, $m_1(\theta)=\theta+1$,
$m_2(\theta)=\theta-1$; trapezoid on $[-40,40]$ with $1.6\times10^6$ nodes and a
central difference $h=10^{-4}$.

```
integrated fine configuration metric  G^kappa  = 1.0
Fisher information of the mixture     I_bar(0) = 0.5504
Theorem G defect = G^kappa - I_bar             = 0.4496
Gaussian-moment-chart barycentre: mbar(theta) = theta, Fisher 1, Delta_avg = 0
```

The two numbers differ because the two maps differ; both are nonnegative because both
charts satisfy (JC) in the location sector. This is the only place a quadrature is
used, and it separates two maps that Part V.4 already separates symbolically.

**Block 11 — the corrected `CE-ACTION-LP` witness.**

```
t = 0.5    sup log-integrand on [-80,20] = 2.5268e+05 at x = -80.00
t = 0.1    sup log-integrand on [-80,20] = 4.7976e+04 at x = -80.00
t = 0.01   sup log-integrand on [-80,20] = 1.9176e+03 at x = -80.00
   -> for t>0 the log-integrand -> +oo as x -> -oo, so N_3(t) = +oo;
      for t<0 the same as x -> +oo. Hence N_3(t) = +oo for every t != 0.
He_2 normalizer pi(exp(t x^2)) = (1-2t)^(-1/2):
   t = -1/4  value = sqrt(6)/3 = 0.816497
   t =  1/4  value = sqrt(2)   = 1.414214
   t = 9/20  value = sqrt(10)  = 3.162278
   -> "no two-sided neighborhood exists" for phi = -x^2 is FALSE.
```

The numerical rows illustrate a divergence that the one‑line tail estimate already
proves: for $t>0$, $-t(x^3-3x)-x^2/2\sim t|x|^3\to+\infty$ as $x\to-\infty$.

### XI.3 Byte‑level checks

Performed by direct search on the bound digests of §0.1; these establish repository
state and nothing mathematical.

| Check | Result |
| --- | --- |
| "connection‑compatible" / "the connections are compatible" | five sites, **no definition**: `05c:15`, `05c:652`, `05c:791`, `06:202`, `08:512` |
| `appendix_notation.tex` row of type $\mathcal Q_\ell\to\mathcal Q_{\ell+1}$ | **none** |
| assignments of $\mathcal R$ | **six**: `04_generative.tex:22`; `05d:287`; `05d:719-783`; `07b:185`; `07b:2074`; `07_general_renormalization.tex:45-48` |
| $\widehat R_\ell$ already assigned | **yes** — `07b:2196` defines $\widehat R_\ell=J_\ell^{-1}R_\ell J_\ell$; recurs at `07b:1275, 2198, 2201, 2211, 2227, 2240, 2241, 2251` |
| free symbols | `\mathsf{R}`, `\mathfrak{r}`, `\mathfrak{q}`, `\mathsf{C}` occur **zero** times in `manuscripts/gauge_vfe_rg/*.tex` |
| `thm:pb-pullback-fisher-defect` guard | `05c:687-700` carries `$\mathcal D\Psi=0$ along $s$` explicitly; `cor:pb-coarse-null-map` (`05c:658`) is likewise guarded — the manuscript does **not** claim base positivity without the guard |
| `thm:pb-fisher-defect-cocycle` | `05c:779-795`; `eq:pb-fisher-defect-cocycle` at `:788` is the vertical cocycle only; no base cocycle is displayed |
| `sec:pb-fisher-defect` opening | `05c:673-677` names equivariance of the fiber map but **not** family closure or smoothness of $q$ |
| `prop:hist-oriented-semiconjugacy` | `05d:723-751`; hypothesis reads "On a noncritical domain" with **no field named**, and the proof asserts the right‑hand side "solves the same initial-value problem" before establishing that $\bar\Phi_{\sigma_Q(t)}$ is defined |
| input drift against the falsifier's binding table | **none**; every shared digest agrees |

---

## Part XII — Independent reconstruction, oracle erasure, limitations, and terminal status

### XII.1 Independent reconstruction

**Covered claims.** All twelve in‑scope ledger claims, the six proposed claims of
VII.3, and the sixteen contradiction rows of Part VIII.

**Method.** Every identity on which a disposition in Parts II–VII rests was re‑derived
here from the frozen contract's declared types and the declared data of the instance,
without reusing any route's algebra: the exact first jet (II.1); the exact signed
comparison and its criterion (II.2, II.3); the frame‑twist representation and the
isotropy criterion (II.6); the ordered composition law (II.7) and the connection
cocycle; the vertical cocycle and the **corrected** base cocycle in three equivalent
forms (II.8); the score/action square and the operator identification $U|_{L^2_0}=R$
(III.1); the nonexistence of a Markov realization of replication (III.4); the Gram
metric, its strongness, and its exact nondegeneracy criterion (IV.2); the joint‑versus‑
product comparison and its Gaussian indefiniteness witness (IV.4); sharp projectability
and the non‑functoriality theorem (V.1, V.2); the exact averaging defect and its
three‑term split (V.3); the mixture‑tier identification of Theorem G (V.4); smoothness
and gauge descent of the declared coarse map (V.4, Proposition V.4); the semiconjugacy
factor's automatic regularity and the reordered flow argument (VI.1, VI.2); the
cancellation of $a_\ell$ from geometric length (VI.4); the necessary‑and‑sufficient
duration criterion (VI.5); the lifting theorem (VI.6); and the horizontal‑conformality
criterion with its sanity check (VI.7).

Four manuscript locations were read directly rather than through a route:
`05c_pullback_geometry.tex:25-37,54-58,673-700,779-812`,
`05d_relational_inference.tex:713-762`, `07b_agent_network_rg.tex:1270-1280,2193-2200`,
and `appendix_notation.tex`. The $\widehat R_\ell$ collision of C‑5 was found this way
and is not reported by any route.

**Result: PASS**, with the dispositions of Part VII. Two prior closures did not survive
reconstruction (`configuration-fisher-metric` and `configuration-map` as closed by route
D), one printed identity did not survive (the hybrid base‑cocycle correction), one
witness did not survive (the $\mathrm{He}_2$ direction), and one recommended repair did
not survive (the rename to $\widehat R_\ell$).

### XII.2 Oracle erasure

The affirmative‑existence instruction attached to the commissioning brief was removed
from the working context before any disposition in Parts VII–X was fixed, and this
artifact was then rescanned for direct and paraphrased dependence. It occurs in no
hypothesis, premise, counterexample, dependency edge, severity assignment, disposition,
or terminal status.

**Result: PASS.** The distribution of outcomes is inconsistent with a prior‑driven
pass: the terminal status is `INCONCLUSIVE` rather than affirmative; one ledger
conjunct is recorded **REFUTED**; two claims remain `OPEN`/`OPEN(BYTES)`; a
recommendation shared by two prior artifacts is rejected on the bytes (C‑5); a
supporting number in the falsifier is corrected against it (C‑7); and one finding
(C‑10) is recorded **in favor of** the manuscript and against a route's sustained
attack, which a uniformly negative prior would also not produce. Passing this audit
shows only that the prior was unnecessary; it proves nothing.

### XII.3 Limitations, separated by kind

* **Theorems.** New here: Theorem II.3 (the exact signed criterion), Theorem II.8 (the
  corrected sharp base cocycle with the equal‑seminorm criterion and condition S3),
  Theorem IV.2 (the Gram tier), Theorem V.3 (the exact averaging defect — **L‑AVG**),
  Proposition V.4 (smoothness and gauge descent of the declared coarse map), and the
  identification V.4 of Theorem G as the mixture‑tier instance of V.3. Everything else
  is a re‑derivation with hypotheses checked.
* **Counterexamples.** Each refutes exactly its stated reading and nothing broader.
  The averaging witness violates (JC) and contradicts no theorem in the stack. The
  metric‑declaration duration witness violates hypothesis 1 of Theorem VI.6. The
  $-a^2dx^2$ witness violates H7. The $b=-3/5$ row of II.2 refutes only the material
  reading of the ledger's "only when".
* **Constructions.** Tier F and Tier F′ are witnesses of joint satisfiability, not
  claims that the manuscript's declared recognition family has this form. Whether the
  manuscript's own configuration objects can be brought to Tier F is edit S‑12, not a
  theorem proved here.
* **Modeling postulates and operational identifications.** **None made.** No bridge
  from Fisher duration to a clock reading; no physical time; no Lorentzian signature;
  no causal structure; no canonical connection. Every connection remains declared data
  and every duration remains connection‑ and metric‑relative.
* **Numerical observations.** Two quadratures, both in Block 10, used only to separate
  two maps that Part V.4 separates symbolically. Every other value in Part XI is exact.
* **Provenance.** The byte‑level checks of XI.3 establish repository state and nothing
  mathematical. P‑1 and P‑2 were confirmed as reported by the routes and were not
  re‑derived; they are mechanical.
* **Not adjudicated.** The non‑Task‑10 ledger claims; the Task 5–9 evidence artifacts
  except where a Task 10 route cites them; the release artifact's terminal status,
  which is not this pass's to set; and the interaction, projection, beta, and
  fixed‑object tiers of Task 11, which are untouched by every edit in Part IX.

### XII.4 Terminal status for integration readiness

**The mathematics is integrable today.** The four Part D missing lemmas of the
falsifier are resolved: **L‑AVG** is discharged by Theorem V.3 with the hypothesis
(JC) that excludes the counterexample by name; **L‑CFM** is discharged for the
weighted‑product branch by Theorem IV.2 and is not used in the other branch;
**L‑JDQM** is discharged for every tier the stack uses, with the $\kappa$‑uniform
hypothesis stated; **L‑CONFIG‑NONEMPTY** is discharged by the composite witness of
X.3; and **L‑CM** is *retired* rather than discharged, because the stack declares
$\mathsf R_\ell$ separately instead of inducing it pointwise, which is what the brief
directed. All five Part A repairs are applied: the base‑cocycle correction is derived
from first principles and checked at type level, the mislabeled verification block is
replaced by a genuine symbolic check of the sharp statement, the false Gaussian witness
is replaced by an odd Hermite of degree three, generic averaging‑as‑contraction is
retired in favor of a hypothesis‑fenced exact defect identity, and the ledger's
"only when" is replaced by an exact signed criterion. The hypothesis set X.1 is jointly
satisfiable with a nonempty domain, proved on an explicit witness in exact arithmetic.

**What blocks `PASS` is not mathematics.** Three conjuncts of in‑scope claims are
statements about the repository that are **currently false on the bytes**, and no
derivation can close them:

1. `configuration-map` conjunct (d): the symbol $\mathcal R$ carries six assignments and
   `appendix_notation.tex` has no row typing the configuration coarse map. Closable by
   edits **N‑1**, **N‑2**, **S‑13**. Note that the rename recommended by two prior
   artifacts would create a fresh collision and must not be applied.
2. `configuration-fisher-metric` conjunct (d): no configuration manifold is exhibited at
   any scale. Closable by edit **S‑12** together with the declaration **(H‑CONFIG‑F)**.
3. `horizontal-defect-anomaly` conjunct (d) is **REFUTED** as written, and
   `pullback-compatibility` carries the undefined phrase. Closable by edits **L‑1** and
   **L‑2**.

Additionally, the compound target is not atomized until the six claims of VII.3 and
their edges are entered (**L‑5**), and `pullback-ledger-provenance` /
`minor-emergent-time-keyword` cannot close until **P‑1** and **P‑2** are done.

`configuration-map` and `configuration-fisher-metric` are ancestors of every history
claim, so under `proof-obligations.md` no terminal affirmative status is available while
they stand open. Nothing in the portfolio is refuted at the level of a load‑bearing
mechanism, so the status is not negative either. The correct pre‑edit status is
therefore neither `PASS` nor `FAIL`.

INCONCLUSIVE
