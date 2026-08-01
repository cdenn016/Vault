# Expert 08 — RG dynamics, limits, and the pre-MVG two-bundle spine

## Disposition

The chapter has repaired the first-pass defects concerning boundary fixed rays, singular pencils, full-cone primitivity, and the distinction between component preservation and convergence. Those repairs survive this review. The remaining difficulty is more structural: Definition 11.2 currently gives a **scale-indexed diagram of positive coarse operators**, not yet a Wilsonian dynamical system on the manuscript's full pre-MVG object. In particular, it does not yet flow the two independent associated-bundle morphisms, the two independent smooth connection sectors, their covariant compatibility defects, or the identifications required to turn arrows between changing fibers into endomorphisms.

This memo does not repeat the BKS, LRG, graph-ML, Markov-map, or effective-support findings from lanes 01–05. It instead adjudicates what those findings imply for the RG spine.

### Evidence convention

Each item below is an investigator claim for the coordinator's verification ledger. A mathematical status such as `EVIDENCE_VERIFIED` means that the displayed derivation or counterexample closes the mathematical subclaim at the cited revision. It does not replace the independent high-severity closure views required by the audit protocol.

| ID | Severity | Mathematical disposition | Ledger handoff |
|---|---:|---|---|
| RG8-1 | High | `REFUTED`: the current one-sector recursion cannot be the author's required full RG state | Candidate; source + type derivation |
| RG8-2 | High | `EVIDENCE_VERIFIED`: the declared general scheme is not an endomorphism without identification/rescaling data | Candidate; source + typing proof |
| RG8-3 | Medium-high | `EVIDENCE_VERIFIED`: uniform positive contraction of a nonautonomous scheme need not yield one fixed ray | Candidate; exact counterexample |
| RG8-4 | High | `EVIDENCE_VERIFIED`: RG depth and thermodynamic size are independent limits and need not commute | Candidate; exact path-graph counterexample |
| RG8-5 | Medium | `REFUTED` as stated: raw running couplings are not scheme-independent falsifiable observables | Candidate; coordinate-change derivation |
| RG8-6 | Low / positive closure | `EVIDENCE_VERIFIED` for one-step quadratic quotienting; `INCONCLUSIVE` for a projective continuum law | Candidate; finite-dimensional proof |

---

## RG8-1 — The full RG state omits both associated-morphism and both connection sectors

**Severity:** High
**Placement:** General pre-MVG foundations, with an MVG realization only after the general object is defined
**Locations:** `manuscripts/gauge_vfe_rg/02_geometry.tex:44-140`; `manuscripts/gauge_vfe_rg/05a_expfamily.tex:394-398`; `manuscripts/gauge_vfe_rg/09_coarsegraining.tex:205-206`; `manuscripts/gauge_vfe_rg/10_renormalization.tex:54-100`; `manuscripts/gauge_vfe_rg/10_renormalization.tex:269-387`

### Finding

The current foundation starts from one principal bundle and two representations of the same group element, while the RG recursion flows one generic operator parameter \(\pi\). That does not implement the author's clarified model:

\[
\Phi_\ell:E^b_\ell\longrightarrow E^m_\ell,\qquad
\widetilde\Phi_\ell:E^m_\ell\longrightarrow E^b_\ell
\]

are independent **associated-bundle morphisms** covering the identity on the base, and

\[
\Omega^b_{\ell,\gamma}:E^b_{\ell,x}\to E^b_{\ell,y},
\qquad
\Omega^m_{\ell,\gamma}:E^m_{\ell,x}\to E^m_{\ell,y}
\]

are parallel transports induced by two separate smooth principal connections. Neither pair is required to be inverse, equal, or parallel. The current scalar normalization \(\zeta_\ell\) and operator pullback \(S_\ell^*(\cdot)\) cannot encode these sectors or their covariant defects.

This is not a demand that the two bundles be identified. The missing general state is precisely the independent two-bundle state; a shared frame is only a later reduction.

### Type derivation

At scale \(\ell\), the minimal geometric RG object is

\[
\mathfrak X_\ell=
\left(
E^b_\ell,\nabla^b_\ell;\
E^m_\ell,\nabla^m_\ell;\
\Phi_\ell,\widetilde\Phi_\ell;\
\pi^b_\ell,\pi^m_\ell,\ldots
\right).
\]

Let \(C^b_\ell:E^b_\ell\to E^b_{\ell+1}\) and
\(C^m_\ell:E^m_\ell\to E^m_{\ell+1}\) be the two coarse maps, covering the declared base coarse map \(c_\ell\). The cross-scale associated-morphism defects are

\[
\Delta^\Phi_\ell
=C^m_\ell\Phi_\ell-\Phi_{\ell+1}C^b_\ell,
\qquad
\Delta^{\widetilde\Phi}_\ell
=C^b_\ell\widetilde\Phi_\ell-\widetilde\Phi_{\ell+1}C^m_\ell.
\tag{RG8.1}
\]

For a smooth base curve \(\gamma:x\to y\), the two cross-scale connection defects are

\[
\Delta^b_{\ell,\gamma}
=C^b_{\ell,y}\Omega^b_{\ell,\gamma}
-\Omega^b_{\ell+1,c_\ell\gamma}C^b_{\ell,x},
\]
\[
\Delta^m_{\ell,\gamma}
=C^m_{\ell,y}\Omega^m_{\ell,\gamma}
-\Omega^m_{\ell+1,c_\ell\gamma}C^m_{\ell,x}.
\tag{RG8.2}
\]

Independently, the within-scale failure of the cross-fiber morphisms to be connection-parallel is measured by

\[
\mathcal A^\Phi_{\ell,\gamma}
=\Omega^m_{\ell,\gamma}\Phi_{\ell,x}
-\Phi_{\ell,y}\Omega^b_{\ell,\gamma},
\]
\[
\mathcal A^{\widetilde\Phi}_{\ell,\gamma}
=\Omega^b_{\ell,\gamma}\widetilde\Phi_{\ell,x}
-\widetilde\Phi_{\ell,y}\Omega^m_{\ell,\gamma}.
\tag{RG8.3}
\]

All four defects may be nonzero. Under independent belief/model gauges
\(g_b(x)\) and \(g_m(x)\), they transform as sections of the appropriate Hom bundles. For example,

\[
\Phi_x\mapsto g_m(x)\Phi_xg_b(x)^{-1},
\qquad
\mathcal A^\Phi_{\gamma}\mapsto
g_m(y)\mathcal A^\Phi_{\gamma}g_b(x)^{-1}.
\]

Thus their vanishing is gauge invariant, while their norms require a declared metric. The two compositions

\[
\widetilde\Phi_\ell\Phi_\ell\in\operatorname{End}(E^b_\ell),
\qquad
\Phi_\ell\widetilde\Phi_\ell\in\operatorname{End}(E^m_\ell)
\]

are independent running endomorphisms; neither is an identity unless that extra condition is imposed.

Smooth parallel transport must remain distinct from graph-edge transport. A graph link
\(\Theta^b_{ij}\) or \(\Theta^m_{ij}\) can be compared with
\(\Omega_{\gamma_{ij}}\) only after a curve assignment \(e_{ij}\mapsto\gamma_{ij}\) and a declared link-to-curve comparison map. An RG equation should not silently replace one by the other.

### Consequence for the current chapter

The operator recursion can remain as one component of \(\mathfrak X_\ell\), but it cannot be called the full RG flow. The full transformation is a skew-product:

\[
\mathcal R_\ell:
(\pi^b_\ell,\pi^m_\ell,\nabla^b_\ell,\nabla^m_\ell,
\Phi_\ell,\widetilde\Phi_\ell)
\longmapsto
(\pi^b_{\ell+1},\pi^m_{\ell+1},\nabla^b_{\ell+1},
\nabla^m_{\ell+1},\Phi_{\ell+1},\widetilde\Phi_{\ell+1}),
\]

with explicit evolution or projection rules for (RG8.1)–(RG8.3).

### When a diagonal/shared-frame specialization is legitimate

A diagonal specialization requires all of the following data:

1. a reduction of the independent gauge product to a specified diagonal subgroup, or a declared associated-bundle isomorphism \(J_\ell:E^b_\ell\to E^m_\ell\);
2. compatible smooth connections,
   \(\Omega^m_{\ell,\gamma}J_{\ell,x}
   =J_{\ell,y}\Omega^b_{\ell,\gamma}\), unless the nonzero defect is retained explicitly;
3. RG preservation of the reduction,
   \(C^m_\ell J_\ell=J_{\ell+1}C^b_\ell\);
4. coherent partitions, rescalings, and scale identifications across both sectors.

Even under this reduction, \(\Phi_\ell\) and \(\widetilde\Phi_\ell\) need not be inverses. If ranks or representation types differ, no such \(J_\ell\) exists and the diagonal reduction is unavailable.

### Repair

Add a pre-MVG definition of \(\mathfrak X_\ell\), the two coarse maps, and the four covariant defect families above before specializing to matrix-valued Gaussians. Recast the present \(\pi\)-recursion as the operator component of this larger transformation. In the MVG chapter, state the additional assumptions under which the two sectors share node partitions or matrix coordinates.

### Falsification condition

This finding is falsified if the manuscript supplies, before the MVG specialization, a typed RG map whose domain and codomain include both associated-bundle morphisms and both separate smooth connection sectors, together with their independent gauge actions and cross-scale compatibility rules. A one-principal-bundle/two-representation construction does not meet that condition.

---

## RG8-2 — Definition 11.2 is a scale diagram, not yet an RG endomorphism

**Severity:** High
**Placement:** General pre-MVG RG definition
**Locations:** `manuscripts/gauge_vfe_rg/05a_expfamily.tex:394-398`; `manuscripts/gauge_vfe_rg/09_coarsegraining.tex:706`; `manuscripts/gauge_vfe_rg/10_renormalization.tex:102-179`, especially `:141-154` and `:177-179`

### Finding

Definition 11.2 declares a scheme to be partitions \(S_\ell\) and positive scalars \(\zeta_\ell\), with

\[
\pi_{\ell+1}=\zeta_\ell^{-1}S_\ell^*\pi_\ell.
\tag{RG8.4}
\]

The text correctly notes at line 179 that these arrows generally connect different projective spaces. That concession is decisive: without scale identifications, (RG8.4) is not a self-map, so it has no ordinary fixed point, basin, derivative, or autonomous beta function. The scalar \(\zeta_\ell\) changes units but does not specify coordinate, field, base-space, time, or measure rescaling.

This is exactly the distinction visible in primary RG constructions. Villegas et al. integrate out Laplacian modes and then explicitly rescale diffusion time and the remaining Laplacian before comparing scales. Catanzaro et al. likewise separate coarse elimination from the redefinitions that restore the selected model family. Those procedures are differently typed from this manuscript's graph aggregation, but both confirm the need to declare the comparison map.

### Minimal categorical repair

Let \(\mathsf S\) be a scale category with objects \(\ell\) and composable coarse arrows
\(c_{\ell\to k}\). Let \(\mathcal X:\mathsf S\to\mathsf{State}\) assign the state space \(\mathcal X_\ell\), and let

\[
C_{\ell\to\ell+1}:\mathcal X_\ell\to\mathcal X_{\ell+1}
\]

be coarse reduction. A genuine RG comparison additionally requires a family of scale identifications or re-embeddings

\[
I_{\ell+1}:\mathcal X_{\ell+1}\to\mathcal X_\star
\quad\text{or}\quad
J_\ell:\mathcal X_{\ell+1}\to\mathcal X_\ell,
\]

together with the field/base/measure rescalings that make the dimensions and units match. Then either

\[
R_\ell=J_\ell C_{\ell\to\ell+1}:\mathcal X_\ell\to\mathcal X_\ell
\]

is a levelwise endomorphism, or

\[
\widehat R_\ell
=I_{\ell+1}C_{\ell\to\ell+1}I_\ell^{-1}:
\mathcal X_\star\to\mathcal X_\star
\tag{RG8.5}
\]

is a cocycle on a reference state space. Only after \(\widehat R_\ell\equiv\widehat R\), or after a periodic/stationary replacement is proved, do the standard terms “fixed point,” “basin,” and “linearized scaling dimensions” have their autonomous meanings.

For probability laws, the comparison also needs a reference-measure rule. Chapter 9 correctly observes that the energy pullback with a newly declared coarse reference measure is not automatically a marginal or restriction. Therefore a measure/Jacobian prescription is part of the RG object, not an optional normalization detail.

### Repair

Rename Definition 11.2 “positive operator coarse diagram” or extend it with:

- a scale category and composition law;
- the two-sector state object from RG8-1;
- coarse maps and scale-identification/rescaling maps;
- reference-measure/Jacobian transformations;
- an explicit declaration of autonomous, periodic, random, or general cocycle dynamics.

Keep the existing aggregation theorem as the coarse-reduction component.

### Falsification condition

This finding is falsified if the definition provides maps that identify all successive state spaces with one declared comparison space, including units and reference measures, and proves that the resulting transformation is an endomorphism or a specified cocycle. The current statement that such identifications are still needed confirms rather than falsifies the finding.

---

## RG8-3 — Uniform Birkhoff contraction of a level-dependent scheme does not select one fixed ray

**Severity:** Medium-high
**Placement:** General positive-operator dynamics; MVG cones are examples
**Locations:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:144-152`; `:264-301`; `:374-389`

### Finding

The fixed-map Birkhoff theorem and fixed-\(B\) Conjecture 11.8 are correctly typed. The risk is extrapolating them to the general level-dependent scheme. After all scale spaces have been identified, a hierarchical scheme normally produces a cocycle

\[
x_{\ell+1}=\widehat R_\ell x_\ell,
\]

not one map \(\widehat R\). Uniformly finite projective diameters can give exponential forgetting of initial rays, but they need not give a common fixed ray.

### Exact counterexample

On the positive cone \(\mathbb R^2_{>0}\), take

\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},
\qquad
B=\begin{pmatrix}1&1\\1&2\end{pmatrix}.
\]

Both matrices are strictly positive. The finite family \(\{A,B\}\) therefore has a uniform Hilbert-projective contraction coefficient strictly below one. Their Perron rays differ:

\[
r_A=[\varphi,1],\qquad r_B=[1,\varphi],
\quad
\varphi=\frac{1+\sqrt5}{2}.
\]

For the alternating cocycle \(A,B,A,B,\ldots\),

\[
BA=\begin{pmatrix}3&2\\4&3\end{pmatrix},
\]

whose Perron ray is \([1,\sqrt2]\). Even iterates converge projectively to
\([1,\sqrt2]\), while odd iterates converge to
\[
A[1,\sqrt2]=[2+\sqrt2,1+\sqrt2],
\]
a distinct ray. Thus the cocycle has a unique attracting period-two section and forgets initial data exponentially, but it has no single common fixed ray.

This refutes the implication

\[
\text{uniform Birkhoff contraction}
\Longrightarrow
\text{one scale-independent fixed ray}.
\]

It does **not** refute Conjecture 11.8, because that conjecture explicitly assumes one fixed spatial endomorphism \(B\).

### Correct dynamical alternatives

- **Autonomous:** \(\widehat R_\ell=\widehat R\). Seek a Perron fixed ray and its basin.
- **Periodic:** \(\widehat R_{\ell+p}=\widehat R_\ell\). Seek a \(p\)-cycle or a fixed ray of the monodromy.
- **Stationary random:** seek a measurable random invariant section and a projective Lyapunov exponent.
- **General cocycle:** seek pullback/forward attracting sections, not a common fixed point.

A product estimate is theorem-ready: if
\(\tau(\widehat R_\ell)\le q<1\) in Hilbert distance for every \(\ell\), then

\[
d_H(\widehat R_{\ell-1}\cdots\widehat R_0x,
\widehat R_{\ell-1}\cdots\widehat R_0y)
\le q^\ell d_H(x,y),
\]

where defined. This proves loss of initial-ray information, not time independence of the attracting section.

### Repair

Split Open Problem 11.7 into autonomous, periodic, stationary-random, and general-cocycle variants. Reserve “fixed ray” for the autonomous map or monodromy; use “invariant section” or “attracting cycle” for the others. State explicitly that Conjecture 11.8 occupies the autonomous branch.

### Falsification condition

This finding is falsified if the general scheme is proved conjugate to a single fixed endomorphism, or if the claimed object is changed from a fixed ray to the appropriate cocycle-invariant section. Strict positivity alone cannot falsify the counterexample.

---

## RG8-4 — The RG-depth and thermodynamic limits are independent and need not commute

**Severity:** High
**Placement:** General limit theory, before spectral universality claims
**Locations:** `manuscripts/gauge_vfe_rg/05a_expfamily.tex:365-366`, `:394-398`; `manuscripts/gauge_vfe_rg/09_coarsegraining.tex:101-122`; `manuscripts/gauge_vfe_rg/10_renormalization.tex:134`, `:166-177`, `:264-265`, `:389`, `:533-544`

### Finding

The chapter alternates between an infinite hierarchy and a thermodynamic family, but these are two different indices. A correct finite-volume RG family is triangular:

\[
X_{n,\ell},\qquad
0\le \ell\le L(n),
\]

where \(n\) controls system size and \(\ell\) controls RG depth. The limits

\[
\lim_{\ell\to\infty}\lim_{n\to\infty}X_{n,\ell},
\qquad
\lim_{n\to\infty}X_{n,L(n)},
\qquad
\lim_{n\to\infty}X_{n,\ell(n)}
\tag{RG8.6}
\]

are not interchangeable without tightness, compatibility, and uniform error bounds. Definition 11.10 uses a one-index thermodynamic family for the integrated density of states, while the RG recursion uses a level index. Consequently, “the exponent is constant along the flow” is not fully typed until the two indices are related.

### Exact path-graph counterexample

Let \(X_{n,0}\) be the combinatorial Laplacian of the path \(P_{b^n}\). Partition consecutive vertices into blocks of size \(b\), use the membership map \(S\), and use the manuscript's nearest-neighbor topological scaling \(\zeta=1\). Then one aggregation step gives another path Laplacian (up to the harmless endpoint convention):

\[
X_{n,\ell}\simeq L(P_{b^{n-\ell}}).
\]

For each fixed \(\ell\), taking \(n\to\infty\) gives the infinite path. Its integrated density near the lower edge satisfies

\[
N(\lambda)-N(0)\asymp \lambda^{1/2},
\]

so the spectral dimension is \(d_s=1\). By contrast, taking the maximal depth \(\ell=n\) collapses every finite graph to one vertex:

\[
X_{n,n}=0,\qquad \mu_{n,n}=\delta_0.
\]

Thus the fixed-depth thermodynamic limit retains the one-dimensional spectral edge, while the fully blocked diagonal sequence is the trivial zero operator. The two limits in (RG8.6) do not commute.

### Heat susceptibility and the normalization choice

If the infinite-volume IDS obeys
\[
N(\lambda)-N(0)\sim c\lambda^\alpha,
\qquad \alpha>0,
\]
and a Tauberian hypothesis controls the edge, then the nonzero heat trace obeys
\[
Z(t)\sim c\,\Gamma(\alpha+1)t^{-\alpha}.
\]
For the unnormalized spectral entropy
\[
S(t)=\log Z(t)+t\langle\lambda\rangle_t,
\]
the positive heat susceptibility
\[
C(t)=-\frac{dS}{d\log t}
=t^2\operatorname{Var}_t(\lambda)
\]
tends to \(\alpha=d_s/2\). If instead \(S\) is divided by \(\log |V_n|\), as in the finite-network normalized-entropy convention, then \(C\) is divided by the same factor and its thermodynamic limit generally collapses to zero. A nonzero plateau therefore requires the unnormalized quantity or an explicitly renormalized thermodynamic convention.

This is the main RG consequence of the LRG comparison: the heat-kernel heuristic can motivate a finite-size blocking scale, but its entropy normalization cannot be imported unchanged into an IDS limit.

### Projective-law consequence

The energy recursion \(S^T\Lambda S\) alone does not produce a projectively consistent probability family. Chapter 9 correctly distinguishes:

- pushforward laws under measurable coarse statistics;
- energy pullbacks evaluated on embedded coarse configurations;
- newly normalized trace laws relative to declared coarse measures.

A continuum/projective limit needs explicit kernels
\(K_{n\to m}\) with
\(\mu_m=(K_{n\to m})_\#\mu_n\) and composition
\(K_{m\to r}K_{n\to m}=K_{n\to r}\), plus tightness or a standard-Borel cylinder theorem. Smooth-section support, connection convergence, ELBO convergence, and the RG limit remain additional obligations.

### Repair

Introduce \(X_{n,\ell}\) and state which of the three limits in (RG8.6) is intended. Require:

1. projective consistency at fixed RG level;
2. uniform control in \(n\) for each coarse step;
3. a declared diagonal scaling \(\ell(n)\) for finite-size scaling;
4. a chosen heat-entropy normalization;
5. separate convergence criteria for operators, laws, connections, and associated morphisms.

### Falsification condition

This finding is falsified if the manuscript supplies a two-index system and proves the needed exchange-of-limits or diagonal-limit theorem under stated hypotheses. Existence of each limit separately is insufficient.

---

## RG8-5 — Raw running couplings are scheme dependent; the falsifiable residue must be invariant

**Severity:** Medium
**Placement:** General RG interpretation
**Locations:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:154`, `:177-179`, `:579-599`

### Finding

Line 599 identifies running couplings, attraction, linearization, and a declared scheme as the falsifiable residue. Attraction and linearization can be genuine dynamical claims, but the numerical components of a running coupling or beta function are not scheme-independent observables.

Let \(g(t)\) be couplings with
\[
\beta(g)=\frac{dg}{dt}.
\]
Under a smooth reparameterization \(g'=f(g)\),
\[
\beta'(g')=Df(g)\,\beta(g).
\tag{RG8.7}
\]
Under a scale-coordinate change \(t'=ct\),
\[
\beta'(g')=\frac1cDf(g)\,\beta(g).
\tag{RG8.8}
\]
Therefore the curve coordinates, beta components, and numerical linearized exponents depend on coupling coordinates and scale normalization. The physically testable object must instead be a matched observable, an invariant manifold, a conjugacy class, a critical exponent with a fixed block factor, or a dimensionless amplitude ratio.

For a homogeneous cone map with fixed ray \(r\), let \(\mu_0\) be the radial eigenvalue and \(\mu_a\) a transverse eigenvalue of the derivative. The projective eigenvalue is
\[
\rho_a=\frac{\mu_a}{\mu_0}.
\]
If the declared spatial block factor is \(b\), the scaling dimension is
\[
y_a=\frac{\log|\rho_a|}{\log b}.
\tag{RG8.9}
\]
This quotient removes the unphysical radial normalization. It is invariant under smooth coordinate conjugacy at the fixed ray, provided the same scale normalization and quotient tangent are used. It is not defined for a changing-space arrow before the identifications of RG8-2.

### Repair

Replace “running couplings are the falsifiable residue” by a hierarchy:

- scheme-dependent diagnostics: coordinates \(g_\ell\), beta components, chosen blocking statistics;
- conjugacy-covariant dynamics: invariant manifolds and stable/unstable splittings;
- candidate universal observables: projective eigenvalue ratios, scaling dimensions normalized by \(\log b\), matched heat/IDS exponents, and dimensionless amplitude ratios;
- model-specific predictions: observables reconstructed in the original belief/model fibers.

For the two-bundle model, also quotient redundant gauge directions and retain the covariant defects (RG8.1)–(RG8.3) as running Hom-bundle fields, not scalar couplings.

### Falsification condition

This finding is falsified if every reported running quantity is tied to a fixed scheme and is not claimed universal, while all cross-scheme claims are formulated in invariant or explicitly matched observables.

---

## RG8-6 — Conjecture 6.27 can be closed at one quadratic step, but not promoted to a projective continuum theorem

**Severity:** Low / positive closure
**Placement:** MVG quadratic quotient result, with a warning against generalization
**Locations:** `manuscripts/gauge_vfe_rg/05a_expfamily.tex:365-366`; `manuscripts/gauge_vfe_rg/09_coarsegraining.tex:101-122`; `manuscripts/gauge_vfe_rg/10_renormalization.tex:255-260`

### Finding

The one-step statement “quotienting commutes with aggregation” is provable for the finite-dimensional quadratic consensus quotient, including the measure factor. It does not establish a multi-scale projective law, a thermodynamic limit, or a pre-MVG theorem.

### Theorem-ready finite-dimensional result

Let
\[
F=\mathbb R^{NK},\qquad
C=\mathbb R^{nK},
\]
with consensus spaces
\[
V_f=\mathbf1_N\otimes\mathbb R^K,\qquad
V_c=\mathbf1_n\otimes\mathbb R^K.
\]
Let \(P\in\{0,1\}^{N\times n}\) be a nonempty hard membership matrix and
\(S=P\otimes I_K\). Then \(S\) is injective and
\[
S(V_c)=\operatorname{range}(S)\cap V_f.
\]
Hence
\[
\bar S:C/V_c
\longrightarrow
\operatorname{range}(S)/
\bigl(\operatorname{range}(S)\cap V_f\bigr),
\qquad
[z]\longmapsto[Sz],
\tag{RG8.10}
\]
is a linear isomorphism.

If \(L\succeq0\) and \(V_f\subseteq\ker L\), then
\[
[z]^T(S^TLS)[z]=[Sz]^TL[Sz],
\tag{RG8.11}
\]
so the quotient quadratic forms commute exactly under \(\bar S\). Any two translation-invariant measures on these finite-dimensional quotient spaces differ by a positive constant. Therefore the **normalized Gaussian probability laws** agree under (RG8.10); only the raw normalizer changes by the Jacobian.

Using Euclidean quotient complements, let
\[
D=\operatorname{diag}(n_1,\ldots,n_n),\qquad
\boldsymbol n=(n_1,\ldots,n_n)^T,\qquad
N=\sum_I n_I.
\]
The Gram matrix of \(\bar S\) on \(\mathbf1_n^\perp\) is the restriction of
\[
D-\frac1N\boldsymbol n\boldsymbol n^T.
\]
Thus
\[
J_S
=
\left[
\det_{\mathbf1_n^\perp}
\left(D-\frac1N\boldsymbol n\boldsymbol n^T\right)
\right]^{K/2}.
\tag{RG8.12}
\]
For equal block size \(b\),
\[
J_S=b^{K(n-1)/2}.
\]
The corresponding additive \(\log J_S\) term is partition dependent. It cancels from a normalized one-step law but matters if raw free energies are compared across scales without a declared measure counterterm.

### Limits of the theorem

Equations (RG8.10)–(RG8.12) do not prove:

- compatibility of successive quotient measures;
- existence of stochastic refinement kernels;
- convergence of smooth connections or the two associated morphisms;
- commutation of the RG and thermodynamic limits;
- preservation of a general exponential family outside the quadratic MVG locus.

### Repair

Replace Conjecture 6.27 by the finite-dimensional proposition above and move the genuinely open claims into a separate “projective quotient-law limit” problem.

### Falsification condition

The finite-dimensional claim is falsified by an empty block, a coarse map that does not carry \(V_c\) onto the represented fine consensus subspace, or a quadratic form that does not annihilate \(V_f\). The continuum/projective claim remains `INCONCLUSIVE` until compatible laws and kernels are constructed.

---

## Theorem-ready RG package

The following statements can be inserted with minimal dependence on MVG coordinates.

### T1. Typed RG object and autonomous reduction

An RG scheme is a functorial scale diagram \((\mathfrak X_\ell,C_{\ell\to k})\) together with comparison maps \(I_\ell:\mathfrak X_\ell\to\mathfrak X_\star\). The reference-space maps
\[
\widehat R_\ell=I_{\ell+1}C_{\ell\to\ell+1}I_\ell^{-1}
\]
form a cocycle. A fixed object is defined only when the cocycle is autonomous, periodic through its monodromy, or supplied with an invariant section. A fixed **ray** additionally requires a positive cone and projectivization.

### T2. Covariance of the two-bundle RG defects

The four defects (RG8.1)–(RG8.3) are sections of the corresponding Hom bundles and transform by left/right endpoint gauges. Their zero loci are therefore gauge invariant. Exact naturality is the special case \(\Delta=0\); the general theory may retain \(\Delta\neq0\) and flow it covariantly.

### T3. Nonautonomous positive contraction

Uniform Hilbert contraction gives exponential forgetting of initial rays. It gives a common fixed ray only with an additional autonomous/common-invariant-ray hypothesis. Periodic cocycles produce attracting projective cycles; stationary random cocycles produce random invariant sections under the usual integrability assumptions.

### T4. Projective linearization

For a differentiable homogeneous positive endomorphism at a fixed ray, scaling eigenvalues are transverse/radial ratios \(\rho_a=\mu_a/\mu_0\). With declared block factor \(b\), the scaling dimensions are (RG8.9). Gauge and normalization directions must be quotiented before these are interpreted physically.

### T5. IDS-to-heat susceptibility

Under an edge asymptotic
\(N(\lambda)-N(0)\sim c\lambda^\alpha\) and a suitable Tauberian condition,
\[
Z(t)\sim c\Gamma(\alpha+1)t^{-\alpha},
\qquad
-\frac{dS}{d\log t}\to\alpha,
\qquad
d_s=2\alpha,
\]
for unnormalized spectral entropy. A \(\log |V|\)-normalized entropy needs a separate thermodynamic renormalization and does not share this nonzero limit automatically.

### T6. Finite quadratic quotient aggregation

Under the hypotheses of RG8-6, quotienting and aggregation commute through the isomorphism (RG8.10); normalized Gaussian laws agree, and raw normalizers differ by (RG8.12).

---

## Reconciliation with the four named RG literatures

| Literature | What it legitimately supplies | What it does **not** supply here | Consequence for the manuscript |
|---|---|---|---|
| Berman–Klinger–Stapleton (Bayesian RG) | An information-geometric comparison of inference at different resolutions and a data-processing/inverse-problem viewpoint | A proof that this manuscript's graph pullback, metric tensor, two-bundle connections, or cross-fiber maps realize their construction | Use it as motivation for scale-sensitive information geometry; do not use it to close the operator or two-bundle RG map |
| Villegas et al. (LRG) | Heat-kernel spectral diagnostics, explicit mode elimination, and explicit rescaling of diffusion time/Laplacian | Gauge covariance of heat-kernel entries; a unique node partition; a thermodynamic theorem for the \(\log N\)-normalized entropy | Use the IDS/heat result only after choosing normalization and proving the double limit; keep the blocking threshold heuristic |
| Garuccio et al. (multiscale network RG) | Exact closure constraints for hidden-variable aggregation and the distinction between scale-free and scale-invariant structure | A two-sided inverse to coarse graining; a general interacting-network fixed-point theory; the manuscript's associated-bundle geometry | Keep the additive hidden-variable comparison as a closure example, not as inverse refinement |
| Catanzaro–Garlaschelli–Patil (interacting graph RG) | A genuine statistical-ensemble RG with elimination plus redefinition; exact closure only in restricted interaction structure | A general exact flow at arbitrary coordination, or an identification with deterministic Laplacian aggregation | Cite it as evidence that interaction closure and redefinition are separate obligations; use its failure of general closure as a caution, not as a replacement |

The four programs are complementary but differently typed. None eliminates the need for the manuscript to define its own state object, comparison maps, measure transformations, and two-bundle geometric flow.

---

## Open directions

1. **Two-bundle skew-product RG.** Construct the flow of
   \((\nabla^b,\nabla^m,\Phi,\widetilde\Phi)\) together with the operator/law sectors, and classify fixed objects by the covariant defects (RG8.1)–(RG8.3), not by forcing those defects to vanish.

2. **Cocycle attraction beyond one fixed map.** Prove a projective contraction theorem for periodic, stationary-random, or asymptotically autonomous scale schemes. Identify when the attractor is a ray, cycle, or measurable section.

3. **Double-scaling thermodynamic RG.** Build \(X_{n,\ell}\), prove fixed-\(\ell\) IDS convergence uniformly over a useful range of \(\ell\), and determine which diagonal regimes \(\ell(n)\) retain nontrivial spectral dimension and heat susceptibility.

4. **Scheme equivalence and universal observables.** Define admissible changes of blocking, scale coordinate, reference measure, and gauge reduction. Determine which projective eigenvalue ratios, IDS exponents, defect strata, or dimensionless amplitudes survive those changes.

5. **Projective law and stochastic refinement.** Combine exact coarse Markov kernels with compatible refinement kernels or conditional laws. Prove cylinder-law existence first; treat smooth-section support, connection convergence, ELBO convergence, and inverse reconstruction as separate theorems.

---

## Concise physicist summary

The present recursion is a useful positive coarse-operator construction, and the repaired fixed-\(B\) Birkhoff conjecture is mathematically coherent. It is not yet the full pre-MVG RG. A Wilsonian theory needs an explicit scale category, rescaling/identification maps, a reference-measure rule, and a decision between autonomous dynamics and a cocycle. In this manuscript it must additionally flow two independent associated-bundle morphisms and two independent smooth connection sectors, with nonzero covariant defects allowed. Fixed rays, basins, and scaling dimensions become well typed only after those choices. Thermodynamic size and RG depth then form a two-index problem; the path-graph example proves that the limits can disagree. Universality should consequently be stated in invariant observables—projective eigenvalue ratios, declared heat/IDS exponents, or matched defect data—not in raw running couplings.

## Primary sources used for adjudication

- G. Birkhoff, “Extensions of Jentzsch's theorem,” *Transactions of the AMS* 85 (1957), [doi:10.1090/S0002-9947-1957-0087058-6](https://doi.org/10.1090/S0002-9947-1957-0087058-6).
- R. D. Nussbaum, *Hilbert's Projective Metric and Iterated Nonlinear Maps*, Memoirs AMS 75 (1988), [doi:10.1090/memo/0391](https://doi.org/10.1090/memo/0391).
- G. Berman, J. Klinger, and R. Stapleton, “Bayesian renormalization,” [arXiv:2305.10491](https://arxiv.org/abs/2305.10491).
- P. Villegas et al., “Laplacian renormalization group for heterogeneous networks,” *Nature Physics* 19 (2023), [doi:10.1038/s41567-022-01866-8](https://doi.org/10.1038/s41567-022-01866-8).
- E. Garuccio et al., “Multiscale network renormalization: Scale-invariance without geometry,” *Physical Review Research* 5, 043101 (2023), [doi:10.1103/PhysRevResearch.5.043101](https://doi.org/10.1103/PhysRevResearch.5.043101).
- M. Catanzaro, D. Garlaschelli, and A. Patil, “Renormalization group for interacting networks,” *Physical Review E* (2026), [doi:10.1103/34n8-pw8x](https://doi.org/10.1103/34n8-pw8x), [arXiv:2510.07186](https://arxiv.org/abs/2510.07186).
- K. G. Wilson and J. Kogut, “The renormalization group and the \(\epsilon\) expansion,” *Physics Reports* 12 (1974), [doi:10.1016/0370-1573(74)90023-4](https://doi.org/10.1016/0370-1573(74)90023-4).
