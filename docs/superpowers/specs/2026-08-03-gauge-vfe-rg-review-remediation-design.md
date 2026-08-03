# Gauge-VFE RG Review Remediation Design

## 1. Decision and intended outcome

This remediation will repair every surviving finding in the 2026-08-02 referee report while preserving the manuscript's established bundle geometry, exact normalized ELBO, exact finite law-level coarse theory, and explicit epistemic-status boundaries. Its central mathematical addition is a well-typed cross-scale stability theory. The derivative of an exact coarse action is a bounded map between declared tangent spaces, not automatically an endomorphism of one unnamed space. Wilsonian relevance will be defined only after the comparison, norm, extensivity, and scale conventions that make growth across those spaces meaningful have been supplied.

The selected construction has two compatible stages. The normalized-law stage gives an exact conditional-expectation theorem and Fisher contraction on canonical \(L^p\) tangent spaces. The interaction stage assembles extensive local potentials or scores, transports them through the exact coarse action, and extracts the complete coarse interaction. Its scale-indexed operator is the proper home for relevant, marginal, and irrelevant couplings. These stages factor one operator; they are not asserted to be complemented invariant subspaces or a direct-sum decomposition.

The remediation will not identify RG depth with time. The contextual base remains fixed and timeless. Inference histories remain oriented curves in a section space, while RG is a scale-indexed cocycle between effective theories. A relation between their flows requires an explicit semiconjugacy and is not inferred from shared notation.

## 2. Repository and safety boundary

All implementation work will occur on branch codex/gauge-vfe-rg-review-remediation-20260803 in the isolated worktree

    C:\tmp\Research-gauge-vfe-rg-review-remediation-20260803

The branch begins at reconciliation commit aa71c9bd5edd7e451221f897e1516c9c186b676f, which contains both the local deep-review record and the sanitized Research-vault ingest. The dirty live checkout at C:\Users\chris and christine\Desktop\Research is read-only during authoring. Its tracked and untracked WIP will not be stashed, reset, deleted, overwritten, or imported into the remediation worktree.

The remote is the publication authority. Publication will use a clean integration worktree after a fresh fetch and explicit comparison with origin/main. The live checkout will be advanced only after an incoming-path/WIP overlap audit and a disposable rehearsal demonstrate that its local work is preserved.

## 3. Scope

### 3.1 In scope

For this remediation, a general agent network means every finite standard-Borel agent network of arbitrary, unbounded cardinality, every finite interaction hypergraph on it, and every blocking channel satisfying the stated hypotheses. The construction and proof must be uniform in \(|V|\), use no maximum graph size, and quantify over the graph and blocking data; checking any fixed collection of sizes is not closure evidence. A countably infinite or thermodynamic-limit theory is a separate claim because it requires quasilocality, summability, and convergence hypotheses not present in the manuscript.

The source repair may touch the following surfaces when the corresponding proof or audit requires it:

- The affected gauge_vfe_rg chapters, appendices, main.tex, and SPEC.md.
- manuscripts/references.bib, but only for checked primary-source records or corrections.
- manuscripts/gauge_vfe_rg/verification for stable numerics, a fail-closed manifest verifier, tests, and current result generation.
- .verification, docs/derivations, and docs/reviews for current proof, provenance, and adversarial-closure records.
- The existing Research-wiki project and RG/coarse-graining concept pages, plus a new immutable manuscript source note and the required index.md and log.md entries.

### 3.2 Out of scope

This pass will not import PIFB2, runtime code, historical five-term objectives, or executable configuration claims into gauge_vfe_rg. It will not restore the deleted averaged-connection construction merely to preserve a philosophical sentence; that sentence will instead be corrected to match the geometry actually proved. It will not claim an empirical prediction, a blocking-scheme-independent universality class, an infinite-volume limit, or physical time unless a new proof independently closes the corresponding existing open obligation.

It will not revive findings that the referee panel already refuted: the total-correlation gap, a cross-chapter gauge-convention conflict, the alleged \(P_b\), \(\Theta\), or \(\mathcal R\) symbol defects, RG-F2, RG-F3, P-2's missing-arrow rationale, V1, or V2.

## 4. Approach portfolio and decision

### 4.1 Family A: normalized \(L^p\) action tangents

At each scale, normalize the effective likelihood measure and take the action tangent space to be \(L^p\) modulo constants, or its centered representative. The linearized exact action is conditional expectation, hence a contraction by Jensen. This family is canonical, proves data processing and Fisher loss exactly, and makes every bounded or two-sided evidence-integrable eigenmode nonrelevant when the cross-scale identifications are isometric.

Its limitation is equally informative: the normalized Markov channel alone cannot represent the extensive volume lift that produces Wilsonian relevant couplings. Treating this family as the entire RG theory would turn a useful contraction theorem into a category mistake.

### 4.2 Family B: a scale-indexed extensive interaction bundle

At scale \(\ell\), a declared Banach space \(\mathfrak G_\ell\) contains gauge-covariant interaction coordinates, including all Mobius potentials needed for exact closure. A bounded assembly map

\[
E_\ell:\mathfrak G_\ell\longrightarrow\overline{\mathfrak B}_\ell
\]

forms the extensive action, the exact action derivative

\[
\overline U_\ell:\overline{\mathfrak B}_\ell\longrightarrow\overline{\mathfrak B}_{\ell+1}
\]

performs conditional expectation, and a bounded extraction map

\[
P_{\ell+1}:\overline{\mathfrak B}_{\ell+1}\longrightarrow\mathfrak G_{\ell+1}
\]

returns the complete coarse interaction. The induced coupling operator is

\[
M_\ell(g_\ell)=P_{\ell+1}\overline U_\ell(g_\ell)E_\ell.
\]

The volume factor and support growth live in \(E_\ell\), the information loss lives in \(\overline U_\ell\), and the choice of exact versus truncated effective theory lives in \(P_{\ell+1}\). The evidence-mass constant is tracked separately from the action quotient. This separation prevents the normalized contraction from being confused with coupling relevance. It also matches the manuscript's existing exact Mobius completion and residual accounting.

This is the selected ambient construction. Family A will be proved as the middle conditional-expectation factor of this operator. The manuscript will use generalized cross-scale modes or Lyapunov growth for the derivative cocycle \(M_\ell(g_\ell)\) along an exact RG orbit, and ordinary eigenvalues only after a declared autonomous identification makes the derivative an endomorphism of one normed space. No closed complemented statistical-versus-scaling decomposition or spectral projection is assumed.

### 4.3 Family C: one weighted action space

A weighted sup, Holder, or Orlicz-type space can make the same conditional-expectation derivative bounded with spectral radius greater than one. Existing reset-chain and Mehler witnesses show that such relevant modes can be real. Other natural weighted extensions make the spectral radius infinite. Conditional exponential integrability by itself supplies neither a vector space nor a norm and therefore cannot support spectral language.

This family will be retained as a counterexample and falsification sector, not selected as the ambient theory. Any later use of a weighted space must separately prove nonlinear closure, two-sided evidence integrability where required, boundedness of the first two derivatives, finite spectral radius, and controlled norm comparison across scales.

## 5. Frozen mathematical contract

### 5.1 Exact scale-indexed measure pair

For every scale \(\ell\), let \((\mathsf X_\ell,\mathscr X_\ell)\) be standard Borel, let \(\rho_\ell\) be a probability reference, and let

\[
m_\ell=e^{-H_\ell}\rho_\ell,
\qquad
0<m_\ell(\mathsf X_\ell)<\infty.
\]

Let

\[
K_\ell:\mathsf X_\ell\rightsquigarrow\mathsf X_{\ell+1}
\]

be a normalized, parameter-independent Markov kernel, including any separately declared scale rescaling. Define

\[
\rho_{\ell+1}=\rho_\ell K_\ell,
\qquad
m_{\ell+1}=m_\ell K_\ell,
\]

\[
\mathcal R_\ell^H[H_\ell;\rho_\ell]
=-\log\frac{dm_{\ell+1}}{d\rho_{\ell+1}}.
\]

Nested kernels compose as measure-pair morphisms. If the state spaces or kernels change with \(\ell\), this is a cocycle. It becomes an autonomous semigroup only after explicit compatible identifications with one reference object.

### 5.2 Reverse kernel and Frechet derivative

Let

\[
\pi_\ell=\frac{m_\ell}{m_\ell(\mathsf X_\ell)},
\qquad
\pi_{\ell+1}=\pi_\ell K_\ell.
\]

Disintegrate the joint law \(\pi_\ell(dx)K_\ell(x,dz)\) to obtain a fixed jointly measurable version of the reverse kernel \(\Pi_\ell(dx\mid z)\). The ambient nonlinear action chart for the general theorem is

\[
\mathfrak B_\ell=L^\infty(\pi_\ell;\mathbb R).
\]

For some declared \(\varepsilon>0\), set

\[
\mathcal U_{\ell,\varepsilon}
=
\{\varphi\in L^\infty(\pi_\ell):\lVert\varphi\rVert_\infty<\varepsilon\}.
\]

The remediation must prove that the typed action increment

\[
Q_\ell(\varphi)
:=
\mathcal R_\ell^H[H_\ell+\varphi;\rho_\ell]
-
\mathcal R_\ell^H[H_\ell;\rho_\ell]
\]

defines, \(\pi_{\ell+1}\)-almost everywhere, a locally real-analytic map

\[
Q_\ell:
\mathcal U_{\ell,\varepsilon}
\longrightarrow
L^\infty(\pi_{\ell+1};\mathbb R),
\]

and in particular is twice Frechet differentiable, with

\[
U_\ell\varphi(z)
:=
D\mathcal R_\ell^H(H_\ell)[\varphi](z)
=
DQ_\ell(0)[\varphi](z)
=\mathbb E_{\Pi_\ell(\cdot\mid z)}[\varphi],
\]

\[
D^2\mathcal R_\ell^H(H_\ell)[\varphi,\psi](z)
=
D^2Q_\ell(0)[\varphi,\psi](z)
=-\operatorname{Cov}_{\Pi_\ell(\cdot\mid z)}(\varphi,\psi).
\]

The derivative then extends uniquely as a contraction between the \(L^p\) spaces in Section 5.3. No claim is made that the nonlinear logarithmic action map is defined on an arbitrary \(L^p\) neighborhood. A larger Orlicz or weighted nonlinear chart is licensed only after its domain, codomain, norm, open neighborhood, and uniform moment bounds have been proved. Pointwise conditional exponential integrability is only a pointwise differentiability condition; it is not an action-space definition.

Constants are tracked when evidence mass is tracked. If mass is deliberately forgotten, \(U_\ell1=1\) permits descent to

\[
\overline{\mathfrak B}_\ell=\mathfrak B_\ell/\mathbb R1.
\]

The manuscript must never alternate between the full and quotient spaces without saying which theory is being used.

### 5.3 Canonical contraction theorem

For every \(1\le p\le\infty\), conditional expectation gives

\[
\lVert U_\ell\varphi\rVert_{L^p(\pi_{\ell+1})}
\le
\lVert\varphi\rVert_{L^p(\pi_\ell)}.
\]

For finite \(p\), means are preserved, so the map restricts to centered tangent spaces. For \(p=2\), the proof must include

\[
\lVert\varphi\rVert_{L^2(\pi_\ell)}^2
-\lVert U_\ell\varphi\rVert_{L^2(\pi_{\ell+1})}^2
=
\mathbb E_{\pi_{\ell+1}}
\operatorname{Var}_{\Pi_\ell(\cdot\mid Z)}(\varphi)
\ge0.
\]

The nonlinear action map is order preserving and additively homogeneous, hence sup-norm nonexpansive on bounded actions. Therefore all \(L^p\)-admissible eigenvalues have modulus at most one under isometric scale identification. This is a bounded-sector theorem, not a theorem about every weighted action space.

On \(L^\infty/\mathbb R1\), use the oscillation quotient norm

\[
\lVert[\varphi]\rVert_{\mathrm{osc}}
=\inf_{c\in\mathbb R}\lVert\varphi-c\rVert_\infty
=\frac12
\left(
\operatorname*{ess\,sup}\varphi
-\operatorname*{ess\,inf}\varphi
\right).
\]

For the fixed reverse-kernel version above, define the Dobrushin coefficient

\[
\delta_\ell
=
\operatorname*{ess\,sup}_{(z,z')\sim\pi_{\ell+1}^{\otimes2}}
\sup_A
\left|
\Pi_\ell(z,A)-\Pi_\ell(z',A)
\right|
\]

where the inner supremum is over measurable \(A\). If \(\delta_\ell<1\), then the induced quotient operator \(\overline U_\ell\) obeys

\[
\lVert\overline U_\ell\rVert_{\mathrm{osc}\to\mathrm{osc}}
\le\delta_\ell,
\]

For an autonomous operator identified across scales with a fixed block factor \(b>1\), \(\delta<1\) makes every nonconstant bounded mode strictly irrelevant in oscillation norm. For a nonautonomous cocycle, one-step strict contraction is insufficient. Assuming \(B_{n\leftarrow\ell}\to\infty\), a sufficient Dobrushin certificate for irrelevance is

\[
\limsup_{n\to\infty}
\frac{
\sum_{k=\ell}^{n-1}\log\delta_k
}{
\log B_{n\leftarrow\ell}
}
<0.
\]

Here \(\log0=-\infty\). Because the Dobrushin bound need not be sharp, failure of this certificate is not a proof of marginality or relevance; the actual cocycle growth rate remains decisive.

The identity channel and a two-cycle are sharp controls: the former makes every bounded mode marginal, while the latter has eigenvalue \(-1\) and proves that sign or complex phase cannot be discarded.

The remediation will also prove the qualified essential-spectrum result. Let \(U\) be a bounded positive unital operator on a complex Banach lattice \(X\), or use the canonical complexification of a real Banach lattice, and suppose its unit is quasi-interior. Define

\[
r_{\mathrm{ess}}(U)
:=
r\!\left(
U+\mathcal K(X)
\right)
\]

as the spectral radius of the coset of \(U\) in the Calkin algebra \(\mathcal L(X)/\mathcal K(X)\). Assume specifically that whenever \(r(U)>r_{\mathrm{ess}}(U)\), the value \(r(U)\) is a pole and \(U^*\) admits a nonzero positive eigenfunctional at \(r(U)\). Then

\[
r(U)>1
\quad\Longrightarrow\quad
r(U)=r_{\mathrm{ess}}(U).
\]

Indeed, a nonzero positive functional is strictly positive on the quasi-interior unit, while \(U1=1\); pairing the eigen-equation with \(1\) forces \(r(U)=1\). Thus relevance of the bare unital operator, when admitted by a larger weighted space, cannot under the stated pole hypothesis be represented as an isolated dominant Perron eigenvalue. This is not called a quasi-compact hypothesis, because quasi-compactness would contradict the displayed conclusion when \(r(U)>1\).

Norm dependence itself will be proved by an exact common-map witness. On the circle \(\mathbb T\) with its geodesic metric and Haar law, let \(D(z)=2z\bmod1\), take

\[
K(y,dz)
=
\frac12
\left(
\delta_{y/2}
+
\delta_{(y+1)/2}
\right)(dz),
\]

and take the resulting reverse kernel

\[
\Pi(z,dy)=\delta_{D(z)}(dy),
\qquad
Uf=f\circ D.
\]

For \(0<\alpha\le1\), equip periodic \(C^\alpha(\mathbb T)\) with the standard sup-plus-Holder norm. The remediation must prove the upper bound from \([f\circ D^n]_\alpha\le2^{\alpha n}[f]_\alpha\) and the matching lower bound from the growth of a fixed nonconstant Fourier mode under \(D^n\). Hence \(r(U)=1\) on \(L^\infty\), whereas \(r(U)=2^\alpha\) on \(C^\alpha(\mathbb T)\). The exact same conditional-expectation map therefore has different relevance content in two legitimate topologies. This witness rules out every topology-free spectral claim.

### 5.4 Exact interaction operator and truncation residual

For a finite vertex set \(V_\ell\), the interaction tier requires the finite standard-Borel product decomposition

\[
(\mathsf X_\ell,\mathscr X_\ell)
=
\prod_{i\in V_\ell}
(\mathsf X_{\ell,i},\mathscr X_{\ell,i}).
\]

The gauge action must preserve this factor structure, either componentwise or through an explicitly tracked permutation, and must push each coordinate reference law covariantly. Fix the resulting covariantly transforming product reference law

\[
\nu_\ell
=
\bigotimes_i\nu_{\ell,i}
\sim
\pi_\ell.
\]

Thus \(\nu_\ell\) and \(\pi_\ell\) have exactly the same null sets. Define \(\mathfrak G_\ell\) to be the full power-set Hoeffding interaction space

\[
\mathfrak G_\ell
=
\bigoplus_{\varnothing\ne A\subseteq V_\ell}
L^\infty_{0,A}(\nu_{\ell,A}),
\qquad
\lVert g\rVert_{\mathfrak G_\ell}
=
\sum_{\varnothing\ne A\subseteq V_\ell}
\lVert\Phi_{\ell,A}\rVert_\infty,
\]

where \(L^\infty_{0,A}\) means zero conditional mean in every coordinate of \(A\). Thus the space contains one gauge-covariant potential for every nonempty subset, including the top-order term. A sparse hypergraph is only an input or truncation subspace and is not claimed to be exactly closed. Impose the hierarchical zero-mean gauge

\[
\int
\Phi_{\ell,A}(x_A)
\,\nu_{\ell,i}(dx_i)
=0
\qquad
(\varnothing\ne A,\ i\in A).
\]

Writing \(\mathsf E_i\) for integration in coordinate \(i\) against \(\nu_{\ell,i}\), the component extraction formula is

\[
(P_\ell[f])_A
=
\left(
\prod_{i\in A}(I-\mathsf E_i)
\right)
\left(
\prod_{j\notin A}\mathsf E_j
\right)f.
\]

The evidence-mass constant is carried as a separate scalar. On nonempty interactions this normalization removes every lower-order redistribution gauge, so assembly and Mobius/Hoeffding extraction are typed inverse maps

\[
E_\ell:\mathfrak G_\ell\longrightarrow\overline{\mathfrak B}_\ell,
\qquad
P_\ell:\overline{\mathfrak B}_\ell\longrightarrow\mathfrak G_\ell,
\qquad
P_\ell E_\ell=I,
\qquad
E_\ell P_\ell=I.
\]

Consequently, \(L^\infty(\nu_\ell)\) and \(L^\infty(\pi_\ell)\) are the same normed equivalence-class space. The interaction tier is restricted to these bounded action classes. The inverse identities, gauge covariance of the chosen normalization, and preservation of the declared \(\nu_\ell\sim\pi_\ell\) domination tier across every admitted scale map are release-gated theorems rather than assumed notation. Let

\[
\overline{\mathcal R}_\ell^H:
\overline{\mathfrak B}_\ell
\longrightarrow
\overline{\mathfrak B}_{\ell+1}
\]

and \(\overline U_\ell\) denote the action map and derivative induced on the quotient; they exist because adding a constant to an action adds the same constant to its coarse action.

Every truncation must declare a closed retained subspace and a bounded idempotent

\[
\mathfrak G_{\ell,Q}
\subseteq
\mathfrak G_\ell,
\qquad
\mathsf Q_\ell:
\mathfrak G_\ell
\longrightarrow
\mathfrak G_{\ell,Q},
\qquad
\mathsf Q_\ell^2=\mathsf Q_\ell.
\]

The operator norm of \(\mathsf Q_\ell\) and the quotient norm \(\lVert\cdot\rVert_{\overline{\mathfrak B}_\ell}\) used for residuals are part of the truncation contract.

The exact next-scale interaction and its retained projection are distinct:

\[
g_{\ell+1}^{\mathrm{ex}}
=
P_{\ell+1}
\overline{\mathcal R}_\ell^H(E_\ell g_\ell),
\qquad
g_{\ell+1}^{Q}
=
\mathsf Q_{\ell+1}g_{\ell+1}^{\mathrm{ex}}.
\]

For a retained subspace with projection \(\mathsf Q_\ell\), write entirely in the quotient

\[
\overline{\mathcal R}_\ell^H(E_\ell g_\ell)
=E_{\ell+1}g_{\ell+1}^{Q}+\overline r_{\ell+1}^{Q},
\]

\[
\overline r_{\ell+1}^{Q}
=
\left(
I-E_{\ell+1}\mathsf Q_{\ell+1}P_{\ell+1}
\right)
\overline{\mathcal R}_\ell^H(E_\ell g_\ell)
\in
\overline{\mathfrak B}_{\ell+1}.
\]

The exact theory retains \(g_{\ell+1}^{\mathrm{ex}}\), or equivalently all induced hyperedges. A finite truncation is an approximation and must report \(\lVert\overline r_{\ell+1}^{Q}\rVert_{\overline{\mathfrak B}_{\ell+1}}\). No projected beta function will be called exact unless invariance of its retained interaction space is proved.

Define the exact nonlinear interaction map by

\[
\mathcal R_\ell^G
:=
P_{\ell+1}
\overline{\mathcal R}_\ell^H
E_\ell:
\mathfrak G_\ell
\longrightarrow
\mathfrak G_{\ell+1}.
\]

For a declared truncation, define instead

\[
\mathcal R_{\ell,Q}^G
:=
\mathsf Q_{\ell+1}
P_{\ell+1}
\overline{\mathcal R}_\ell^H
E_\ell.
\]

The latter is accompanied by \(\overline r_{\ell+1}^{Q}\) and is not silently substituted for the exact map.

Along the exact orbit \(g_{\ell+1}^{\mathrm{ex}}=\mathcal R_\ell^G(g_\ell)\), require \(E_\ell g_\ell=[H_\ell]\). The reverse kernel and derivative depend on this base action. Write

\[
\overline U_\ell(g_\ell)
:=
D\overline{\mathcal R}_\ell^H(E_\ell g_\ell).
\]

Linearization then gives the typed coupling map

\[
M_\ell(g_\ell)
=
P_{\ell+1}\overline U_\ell(g_\ell)E_\ell:
T_{g_\ell}\mathfrak G_\ell
\longrightarrow
T_{g_{\ell+1}^{\mathrm{ex}}}\mathfrak G_{\ell+1},
\]

with \(\mathsf Q_{\ell+1}\) inserted only for a declared truncation. Gauge equivariance of \(K_\ell\), \(E_\ell\), and \(P_\ell\) must be proved before \(M_\ell(g_\ell)\) descends to gauge-equivalence classes.

The truncated derivative is the separately named map

\[
M_\ell^Q(g_\ell)
=
\mathsf Q_{\ell+1}M_\ell(g_\ell),
\]

and is never substituted into the exact cocycle without changing the orbit and residual accounting.

### 5.5 Exact score-tangent realization and an inhabited relevance spectrum

The manuscript will include a concrete theorem showing that the extensive lift, rather than the bare Markov restriction, produces the standard relevant sector. For an integer block size \(b\ge2\), an iid fixed one-agent law \(\mu_*\), and a declared block statistic \(Z\) with law \(\zeta_b\), first define the full operators

\[
E_b^{\mathrm{full}}:L^2(\mu_*)
\longrightarrow
L^2(\mu_*^{\otimes b}),
\qquad
(E_b^{\mathrm{full}}h)(x_1,\ldots,x_b)
=
\sum_{i=1}^b h(x_i),
\]

\[
R_b^{\mathrm{full}}:
L^2(\mu_*^{\otimes b})
\longrightarrow
L^2(\zeta_b),
\qquad
R_b^{\mathrm{full}}F(z)
=
\mathbb E
\left[
F(X_1,\ldots,X_b)
\mid Z=z
\right],
\qquad
L_b^{\mathrm{full}}
=
R_b^{\mathrm{full}}E_b^{\mathrm{full}}.
\]

The constant mode now lies in the declared domain and satisfies \(L_b^{\mathrm{full}}1=b1\). These operators map the corresponding centered subspaces into one another; denote the restrictions by \(E_b\), \(R_b\), and \(L_b=R_bE_b\). Only when \(\zeta_b=\mu_*\) does \(L_b\) become an endomorphism to which a spectrum can be assigned. Then

\[
\lVert E_bh\rVert_2
=
\sqrt b\lVert h\rVert_2,
\qquad
\lVert R_b\rVert\le1,
\qquad
\lVert L_b\rVert\le\sqrt b.
\]

If \(\mu_t\) is differentiable in quadratic mean at \(\mu_*\) with centered score \(h\), the product path has score \(E_bh\), and the pushed coarse law has score \(L_bh\). A two-sided path realizing every \(h\in L_0^2(\mu_*)\) is

\[
\frac{d\mu_t}{d\mu_*}
=
\frac{(1+th/2)^2}
{1+t^2\lVert h\rVert_2^2/4}.
\]

For the Gaussian fixed law \(\gamma=N(0,1)\), the block statistic

\[
Z=b^{-1/2}\sum_{i=1}^bX_i,
\]

and normalized probabilists' Hermites

\[
e_k=\operatorname{He}_k/\sqrt{k!},
\]

the Mehler conditional-expectation identity proves

\[
L_be_k=b^{1-k/2}e_k.
\]

Completeness of the Hermite basis gives

\[
\sigma(L_b)
=
\{b^{1-k/2}:k\ge1\}\cup\{0\}
\quad
\text{on }L_0^2(\gamma).
\]

The \(k=1\) mode is relevant, \(k=2\) is marginal, and \(k\ge3\) is irrelevant. On the full space, \(e_0=1\) has eigenvalue \(b\); it is absent from the centered restriction and removed from the action theory only in the explicitly projective treatment. Fixing the mean removes the \(k=1\) direction, and fixing mean and variance leaves a strict contraction. For correlated blocks, the covariance cross terms in \(\lVert E_bh\rVert_2^2\) must be retained, so the iid spectrum is not reused.

This is a score-tangent theorem. Higher Hermite scores need not generate a two-sided exponential-action chart. The manuscript will not silently identify score tangents with finite-valued action perturbations; their relation will be stated through differentiability in quadratic mean. In a finite exact interaction family, the analogous coupling matrix along an orbit is \(P_{\ell+1}\overline U_\ell(g_\ell)E_\ell\). Without exact family closure it is a projected operator accompanied by the residual of Section 5.4.

### 5.6 Generalized modes, cocycle law, and relevance

Fix an exact interaction orbit \(g_{k+1}=\mathcal R_k^G(g_k)\). An ordinary equation \(M_\ell(g_\ell)v=\lambda v\) is forbidden when its two sides live at different scales. There are two licensed replacements.

First, declared isomorphisms

\[
J_\ell:\mathfrak G_\star\longrightarrow\mathfrak G_\ell
\]

define the reference-space endomorphism

\[
\widetilde M_\ell(g_\ell)
=
J_{\ell+1}^{-1}M_\ell(g_\ell)J_\ell.
\]

Second, a normalized mode section \(v_{\ell,a}\) may satisfy

\[
M_\ell(g_\ell)v_{\ell,a}
=
\lambda_{\ell,a}v_{\ell+1,a}.
\]

The norm, sign or phase convention, and per-volume normalization of \(v_{\ell,a}\) must be fixed. Otherwise

\[
v_{\ell,a}\longmapsto c_\ell v_{\ell,a}
\]

changes \(\lambda_{\ell,a}\) by \(c_\ell/c_{\ell+1}\) and makes the exponent arbitrary. With a fixed normalization, composition proves

\[
\lambda_{n\leftarrow\ell,a}
=
\prod_{k=\ell}^{n-1}\lambda_{k,a}.
\]

This is the cross-scale eigenvalue cocycle. Its mapping to Jona-Lasinio's tangent-space formulation will be cited only after every imported hypothesis has been checked.

More generally, changing the normalization is harmless only for a tempered scale gauge satisfying

\[
\frac{
\log|c_n|
}{
\sum_{k=\ell}^{n-1}\log b_k
}
\longrightarrow0.
\]

A non-tempered basis rescaling can change even the sign of the reported exponent and therefore falsifies any claim of invariant relevance.

For block factors \(b_\ell>1\), define

\[
B_{n\leftarrow\ell}
=
\prod_{k=\ell}^{n-1}b_k.
\]

When the limit exists,

\[
y_a
=
\lim_{n\to\infty}
\frac{
\log|\lambda_{n\leftarrow\ell,a}|
}{
\log B_{n\leftarrow\ell}
}.
\]

Without an invariant line, use the upper cocycle growth rate

\[
\chi_\ell(v)
=
\limsup_{n\to\infty}
\frac{
\log
\lVert
M_{n-1}(g_{n-1})\cdots M_\ell(g_\ell)v
\rVert_n
-
\log\lVert v\rVert_\ell
}{
\log B_{n\leftarrow\ell}
}.
\]

Relevant, marginal, and irrelevant mean positive, zero, and negative growth only after these choices. The trichotomy itself is a DEFINITION. Existence of a limit, invariant splitting, spectral projection, or universal exponent is ESTABLISHED only under a proved autonomous, periodic, uniformly hyperbolic, quasi-compact, or applicable multiplicative-ergodic hypothesis. Otherwise the corresponding claim remains OPEN.

### 5.7 Fixed objects and beta functions

The normalized fixed measure-pair equations already proved in the manuscript remain unchanged. On a nonautonomous scale diagram, invariant sections are stated separately in each tier:

\[
(\rho_{\ell+1},m_{\ell+1})
=
\mathcal R_\ell^{\mathrm{pair}}(\rho_\ell,m_\ell),
\]

\[
[H_{\ell+1}]
=
\overline{\mathcal R}_\ell^H[H_\ell],
\qquad
g_{\ell+1}
=
\mathcal R_\ell^G(g_\ell),
\qquad
q_{\ell+1}
=
\widehat{\mathcal R}_\ell(q_\ell).
\]

The last equation is used only after the configuration map in Section 5.8 has been constructed. Periodic and stationary-random cocycles use their own typed invariants. An ordinary fixed point exists only after reference-space identifications produce an autonomous endomorphism in the same declared tier.

A discrete interaction beta function is a difference in one vector space. With \(J_\ell\) as above,

\[
\beta_\ell^G(g)
=
\frac{
J_{\ell+1}^{-1}
\mathcal R_\ell^G
J_\ell(g)
-g
}{
\log b_\ell
}.
\]

The discrete theory uses these comparison transports and no differential connection along \(\ell\). A covariant derivative along scale is available only in a separately declared continuous extension: one must introduce a smooth scale manifold with coordinate \(s\), a smooth Banach bundle over it, a smooth interpolation of the RG maps, and a scale connection. That auxiliary connection is not a connection on the contextual principal bundle and \(s\) is not physical or inference time. Without either the discrete reference trivialization or this complete continuous extension, subtraction across scales and hence a beta function are undefined; the cocycle remains the primary object.

### 5.8 Fisher, pullback geometry, and timeless histories

For an \(L^2\) action tangent class

\[
[\varphi]
\in
\overline{\mathfrak T}_{\ell,2}
:=
L^2(\pi_\ell)/\mathbb R1,
\]

define its normalized score by

\[
\mathscr S_{\ell,H}[\varphi]
=
-
\left(
\varphi
-
\mathbb E_{\pi_\ell}\varphi
\right).
\]

This is an isometric isomorphism from \(\overline{\mathfrak T}_{\ell,2}\), equipped with the Fisher norm

\[
\lVert[\varphi]\rVert_{F,\ell}^2
=
\operatorname{Var}_{\pi_\ell}(\varphi)
\]

to \(L_0^2(\pi_\ell)\). The exact compatibility equation is

\[
\mathscr S_{\ell+1,\mathcal R_\ell H}
\left[
U_\ell\varphi
\right]
=
\mathbb E
\left[
\mathscr S_{\ell,H}[\varphi]
\mid Z
\right].
\]

Thus the action derivative and score projection are related by centering; they are not literally the same uncentered function. The \(L^2\) identity above is the scalar form of the Fisher defect.

At the bundle level, let the selected fine statistical family be differentiable in quadratic mean with finite Fisher norm, and require its pushforward through the channel to lie in a selected coarse family with the same properties. Let \(\Psi_\ell\) be the resulting smooth, parameter-independent normalized Markov fiber morphism covering \(f_\ell\), not merely an abstract kernel with no tangent map. Require a smooth score-tangent pushforward, family closure, related sections, and horizontal-lift compatibility. Only then is the following defect defined pointwise at \(p\) and \(\Psi_\ell(p)\):

\[
\Delta_F^{\Psi_\ell}
=
g_\ell^F
-
(T^V\Psi_\ell)^*
g_{\ell+1}^F
\succeq0.
\]

For connection-compatible bundle morphisms and related fine/coarse sections, pulling this defect to the contextual bases gives the already established tensor cocycle

\[
\Delta_\ell^{\mathrm{base}}
=
h_\ell^{\omega_\ell}
-
f_\ell^*
h_{\ell+1}^{\omega_{\ell+1}}
\succeq0.
\]

The remediation will cross-reference these versions and state the compatibility hypotheses once. Relevant interaction couplings do not contradict Fisher contraction: \(U_\ell\) contracts normalized statistical tangents, while \(E_\ell\) may amplify extensive interaction coordinates before \(U_\ell\) acts.

An inference history is still an oriented curve in a section configuration space and acquires information duration from Fisher length only after its VFE orbit is selected. RG depth \(\ell\) labels effective descriptions. The correct state notation has two independent indices, \(Q^{(\ell)}(r)\): \(\ell\) is scale depth and \(r\) is a position on an oriented, unparameterized inference orbit.

At every scale, introduce a smooth regular configuration manifold \(\mathcal Q_\ell\) of admissible sections and a separate configuration-space Fisher metric \(G_\ell^{\mathrm{conf}}\). In a continuum section space, this metric requires a declared base measure, channel weights, gauge quotient, finiteness, and nondegeneracy or quotient hypotheses. It is not the contextual pullback tensor \(h_\ell^{\omega_\ell}\), which lives on the base manifold. Local existence and uniqueness for the selected VFE vector field are required before its orbit is used.

For independently recomputed fine and coarse vector fields \(X_\ell\), a shared history is claimed only after proving an oriented semiconjugacy

\[
T\widehat{\mathcal R}_\ell\circ X_\ell
=
a_\ell
\left(
X_{\ell+1}
\circ
\widehat{\mathcal R}_\ell
\right),
\qquad
a_\ell>0.
\]

Here

\[
\widehat{\mathcal R}_\ell:
\mathcal Q_\ell
\longrightarrow
\mathcal Q_{\ell+1}
\]

is a separately declared smooth configuration coarse map and \(a_\ell:\mathcal Q_\ell\to(0,\infty)\). It is neither \(\mathcal R_\ell^H\) nor \(\mathcal R_\ell^G\). The semiconjugacy induces an orbit-dependent orientation-preserving reparameterization. Without this equation, Markov Fisher contraction compares a fine path only with its pushforward, not with an independently optimized meta-agent path. No theorem will identify \(\ell\), \(r\), Fisher duration, or physical time.

## 6. Finding-by-finding repair contract

| Finding | Required source repair | Required closure evidence |
|---|---|---|
| P-1, stale Chapter 12 credit | Rewrite the conjectural sentence so it no longer attributes an averaged-connection theorem to Chapter 2; give the operational-trace claim its own CONJECTURE tag; remove the orphan sec:geo-induced-connection label. | Cross-reference scan, status scan, philosophy skeptic, clean build. |
| Pullback ledger provenance | Preserve the invalid historical record in Git history; rerun PB-1 through PB-4 against the repaired source and create a current closure ledger. The new record must cite files that exist at its bound revision. | Verification-gate validation and direct git ls-tree/source-location audit. |
| Undefined \(\mathcal L^{\mathrm{ext}}\) | Promote the canonical relative-log extension to a tagged definition in Chapter 5, state its measure-level domain and extended-real convention, distinguish it from \(\widetilde{\mathcal L}\) and from the H4-dependent integrated ELBO, cross-reference it in Chapter 6, and add it to the notation appendix. | Independent derivation of the fixed-evidence monotonicity theorem with and without H4. |
| Unstable determinant gap | Add the Schur/canonical-correlation form \(-\frac12\sum_i\log(1-\rho_i^2)\), evaluated with triangular solves and log1p; extend it along a declared refinement tree; replace the runner implementation and absolute tolerance. | Deterministic stress tests through condition number \(10^{14}\), high-precision controls, and JUnit output. |
| Fail-open source manifest | Add a nonmutating verify mode, UTC timestamp, source Git revision, semantic payload digest, and complete input manifest. Verification must compare and fail rather than rewrite. | Byte hash before/after verification, mutation tests for each input class, and malformed/missing/unexpected input tests. |
| Gaussian positive definiteness | Require \(A_i\succ0\) in the constructive nonemptiness witness; state the energy-kernel result as positive semidefiniteness plus its exact null-space criterion. | Analytic quadratic-form proof and zero-self counterexample. |
| Campbell attribution | Replace the false nonnormalized uniqueness-up-to-scale claim with Campbell's mass-dependent two-function family and explain why it strengthens the manuscript's nonuniqueness caution. | Checked primary-source passage and Ay et al. theorem cross-check. |
| Probability hypotheses | Make the common dominating reference measure a fixed family-level hypothesis; for mixed coordinates require one fixed countable atomic support covering the admitted family. Separate probability-kernel integration from integration against a fixed sigma-finite measure, and declare or cite the jointly measurable density version actually used. | Measure-theoretic derivation, adversarial moving-atom witness, and downstream type checks. |
| Gauge medium cluster | Define the direction of \(R_i^x\) at first use; retain the measure-level pushforward law generally and restrict the determinant Jacobian formula to the appropriate Lebesgue/quasi-invariant tier; rename the nonclosed shared-link residual group as a constraint-preserving family while retaining the actual context-independent subgroup. | Direct transformation-law reconstruction, mixed-measure counterexample, and the existing \(GL(2)\) closure witness. |
| RG action-space defect | Implement Sections 5.1 through 5.8: declared normed spaces, bounded cross-scale derivative, exact \(L^p\) theorem, extensive score/interaction lift, inhabited Gaussian relevance spectrum, generalized modes, cocycle law, qualified essential-spectrum result, and DEFINITION status for relevance. | Full derivation, circle/reset/Mehler counterexamples, Gaussian Hermite theorem, and independent theorem reconstruction. |
| Jona-Lasinio gap | Cite the checked primary source for conditional expectation as RG linearization, the generalized tangent-space eigenvalue, and the cocycle law; map every imported hypothesis. | Source audit against the primary paper, not the existing manuscript prose. |
| Minor notation/build/citation cluster | Reconcile \(h_i\) and \(h_i^x\) and the two inverse laws; define Chapter 9's \(B,B_\perp,G,Q,\operatorname{pdet}\); state \(K(x,\mathsf Y)=1\); use \(\overline{\mathcal H}\); add the RG operator tier to the notation appendix; remove the spurious nested-forest qualification from measure-pair composition; distinguish the two additive constants presently named \(c_b\); add checked Kemeny-Snell and Nakajima-Zwanzig sources; rename the Abelian result; repair the Chapter 11 cross-reference; narrow the Esfeld and van Fraassen readings; remove or reconcile the emergent-time keyword; separate double status tags; make status tags unbreakable; keep generated auxiliary files ignored and build them fresh. | Static scans, primary-source checks, label/citation inventory, and clean visual build. |

No item may be closed by prose alone. A source edit after its evidence run invalidates the affected closure and restarts the corresponding gate.

## 7. Verification architecture

### 7.1 Rigorous-theory-search record

The durable run directory will be

    docs/derivations/2026-08-03-gauge-vfe-rg-remediation/

and will contain problem-contract.json, approach-registry.json, claim-ledger.json, dependency-dag.json, counterexample-register.md, construction-or-strongest-theorem.md, adversarial-report.json, release.json, and final-report.md. Evidence subrecords will include the action-space proof, extended-ELBO proof, positive-definiteness proof, probability hypotheses, source-citation mappings, numerical stability, manifest verification, TeX build, independent reconstruction, and oracle erasure.

The problem contract will atomize the remediation claims instead of using the circular target "the manuscript is fixed." The affirmative-search prior will be recorded but hidden from independent reconstructors. Release mode requires every load-bearing ancestor to close and every contained artifact hash to match.

### 7.2 Source, evidence, closure, and wiki revisions

The workflow will freeze four non-self-referential commits:

1. Source revision \(S\): manuscript, bibliography, verification code, tests, and build-audit code.
2. Evidence revision \(E\): generated current results, regenerated PDF, proof artifacts, build records, and adversarial review records, all binding \(S\).
3. Closure revision \(C\): a durable closure attestation, rigorous release record, and adjudication produced against clean \(E\), all binding \(E\).
4. Wiki revision \(W\): the immutable source note and synthesis-page propagation recording \(S\), \(E\), and \(C\).

The command git diff --name-only S..E must contain no theorem source, bibliography, test logic, build logic, verification-runner code, or wiki record. Any such change creates a new \(S\) and invalidates all dependent evidence. Likewise, E..C may contain closure records only, and C..W may contain wiki records only.

The generated results and regenerated PB ledger will bind \(S\) and be committed in \(E\). At \(E\), verification must prove that every manifest-bound path is byte-identical to its version at \(S\). The durable closure artifacts committed in \(C\) will bind clean \(E\), and their generation must prove that every source and evidence path is byte-identical to its version at \(E\). The wiki note committed in \(W\) records the already-known hashes \(S\), \(E\), and \(C\), never its own commit hash.

After \(W\) exists, the verification skill will create a separate active .verification/ledger.json against clean candidate publication revision \(W\). Because .verification is excluded from the artifact digest, this live ledger can bind \(W\) without self-reference. It must reproduce or hash-check the \(S\), \(E\), and \(C\) artifacts, validate the wiki-only \(C..W\) diff, and pass the deterministic closure validator while current HEAD remains \(W\). The live ledger is not committed; the durable \(C\) attestation preserves the auditable closure record.

Publication prefers a fast-forward with \(\texttt{origin/main}=W\). If fresh remote work requires an integration commit \(F\ne W\), the clean integration worktree must prove that every task-owned and manifest-bound path is byte-identical to \(W\), and a new active ledger must be started and validated against \(F\) before \(F\) is pushed. The ledger at the eventual published revision \(P\in\{W,F\}\) must contain the complete Section 7.3 claim inventory, with every claim and every eligible evidence record rebound to \(P\). At \(F\), byte-identity checks are recorded as current reproduced evidence; they do not replace any PB, remediation, build, or complete-disposition claim. Any overlap affecting protected paths restarts the appropriate source or evidence gate. The worktree containing the active ledger for the exact published revision is preserved through the final response and Stop validation; its cleanup is a later operation. This removes every self-reference and stale-HEAD transfer. The stale git:43eb7e... pullback ledger will not be cosmetically relabeled; PB-1 through PB-4 will be genuinely rerun.

### 7.3 Verification ledger claims

The durable \(C\) attestation and the active live ledger at the eventual published revision \(P\) will contain separate claims for PB-1 through PB-4 and for each row in Section 6, plus clean-build and complete-disposition claims. Every claim has an explicit polarity. Positive repair, theorem, completeness, source, numerical, manifest, and build claims must close as EVIDENCE_VERIFIED. A claim may close as REFUTED only when it is phrased as persistence of an alleged defect or another negative proposition whose falsity is the desired outcome. The final complete-disposition claim itself must be EVIDENCE_VERIFIED. Mathematics closes only with a current derivation or formal proof. Citation claims close only with current primary or reproduced-source evidence. Runner, manifest, numerical, and build claims close only with current mechanical or reproduced output. High-severity claims receive four or eight views, a structured skeptic, and an adjudicator. Unresolved disagreement produces INCONCLUSIVE, never a vote-based result, and an INCONCLUSIVE remediation claim blocks release.

### 7.4 Numerical and manifest tests

The numerical test lane will cover dimensions 2 through 16, multiple blockings, exact block-diagonal controls, near-decoupled blocks, condition numbers through \(10^{14}\), the report's 3,138 deterministic adversarial draws, and selected 100-digit reference evaluations. A negative result will never be hidden by unconditional clipping. Eigenvalue clipping is permitted only within a derived floating-point error bound; a larger excursion fails.

Manifest tests will mutate temporary copies of every bound input class, including TeX, SPEC.md, bibliography, style, build script, claim map, runner, requirements, and verification protocol. They will also test malformed JSON, missing and unexpected inputs, line-ending changes, Git-revision mismatch, and byte preservation of the verified result file.

The runner interface will make mutation explicit: update mode generates an output, while verify mode accepts an existing result and never writes it. Invoking neither mode or both modes fails. Verification returns nonzero for a binding or payload mismatch and emits a separate machine-readable report when requested.

Test counts and failures will come from JUnit XML, not terminal summaries.

### 7.5 TeX and visual build

A detached worktree at exact evidence revision \(E\) will run the four-pass TeX/BibTeX build. A machine-readable build audit will record tool versions, revision, input inventory, source-manifest digest, PDF hash, byte count, page count, label uniqueness, undefined references and citations, rerun requests, overfull boxes, literal double question marks, invalid status tags, and stale auxiliary files. Every changed page and its neighbors will be rendered and visually inspected for clipping, broken status tags, equation overflow, and bad cross-references.

### 7.6 Independent and adversarial review

Independent reconstructors will receive the frozen claim contract, source diff, and cited primary sources without the previous review diagnosis or selected solution. Separate adversaries will attack the action-space theorem, extended ELBO, common domination, gauge laws, stable numerics, manifest failure behavior, source provenance, and philosophical attribution.

If locally callable, Claude Opus 5 and/or Fable 5 may be used as additional independent lenses. Their agreement remains LLM judgment and cannot replace eligible evidence.

The final adjudicator will derive the surviving punch list from the validated ledger. Oracle erasure must show that an independent reader can reconstruct the central theorem from definitions, assumptions, proof, and cited sources without hidden chat context.

## 8. Wiki propagation

After the source, evidence, and closure gates close, wiki revision \(W\) will add a new immutable manuscript source note recording \(S\), \(E\), \(C\), the theorem contract, the exact established results, and all retained open boundaries. The existing immutable pullback source note will not be edited.

The following synthesis pages will be updated where their present wording is superseded:

- wiki/projects/Gauge-Theoretic Multi-Agent VFE Model.md
- wiki/concepts/Coarse Graining.md
- wiki/concepts/Renormalization group flow.md
- wiki/concepts/Renormalization-group flow of beliefs.md

The update must distinguish the exact law-level channel, the normalized \(L^p\) contraction, the extensive interaction operator, finite exact closure, projected residuals, and still-open infinite-volume universality. It must also retain the separation of scale depth from inference duration. index.md and the append-only log.md will be updated. The wiki lint must report zero broken links, graph-gray nodes, empty shadow stubs, basename collisions, and cross-file identity collisions.

## 9. Commit, publication, and cleanup sequence

The implementation sequence after this design is approved is:

1. Write and commit a detailed execution plan.
2. Scaffold and freeze the rigorous-theory-search run.
3. Implement and self-review the source revision \(S\).
4. Commit \(S\), then run proofs, tests, source verification, adversarial reconstruction, and a detached TeX build against it.
5. Write the generated evidence, review records, regenerated PB ledger, current results, and PDF; commit evidence revision \(E\).
6. Run the durable closure attestation against clean \(E\), then commit closure revision \(C\) containing only that attestation, the rigorous release record, and adjudication that bind \(E\).
7. Validate \(C\), propagate the closed result to the wiki, and commit wiki revision \(W\) containing only wiki records that name \(S\), \(E\), and \(C\).
8. Start and validate the active .verification/ledger.json against clean candidate revision \(W\), including hash checks of \(S\), \(E\), and \(C\); do not commit a new artifact after \(W\).
9. Fetch the remote, audit divergence, and push the feature branch. Fast-forward origin/main to exactly \(W\) when possible. If an integration commit \(F\) is required, create it in a clean worktree, prove task and manifest paths byte-identical to \(W\), rebuild the complete Section 7.3 ledger with all claims and eligible evidence rebound to \(F\), validate it, then push \(F\). Verify the exact origin/main object identity.
10. Rehearse the live-checkout update, verify every protected WIP hash before and after, fast-forward only when safe, and confirm HEAD equals origin/main while reporting dirtiness separately.
11. Remove only task-owned scratch artifacts and superseded worktrees after proving that every committed artifact is reachable from origin/main. Preserve the clean worktree and active ledger bound to the exact published revision through the final response and Stop validation; remove them only in a later cleanup operation.

Any external export gate will be given the exact remote, branch, commits, and file inventory. No force push, reset, stash, or destructive WIP cleanup is part of this design.

## 10. Release gates

The remediation is complete only if all of the following are true:

- Every positive remediation and completeness claim, including final complete disposition, is EVIDENCE_VERIFIED. REFUTED is accepted only for an explicitly negative claim whose falsity closes an alleged defect. Any polarity mismatch or any INCONCLUSIVE, CANDIDATE, or LLM_SUPPORTED remediation state blocks release. Existing manuscript claims that were already honestly OPEN may remain OPEN when they are outside this remediation contract.
- The cross-scale operator theorem is fully typed and proved, and no ordinary eigenvalue crosses unnamed spaces.
- The normalized \(L^p\) contraction and Fisher-defect identities are proved without erasing the separate extensive coupling sector.
- The explicit score lift produces the proved Gaussian relevant, marginal, and irrelevant modes.
- The generalized-mode normalization and cocycle law prevent arbitrary exponent rescaling.
- The interaction normalization and common-null-set tier are fixed and preserved, extraction and assembly are proved inverse on the action quotient, and the exact effective interaction or its explicit truncation residual is present at every scale for arbitrary finite networks with no size bound.
- Primary-source mappings for Campbell, Jona-Lasinio, Kemeny-Snell, Nakajima-Zwanzig, Esfeld, and van Fraassen survive source audit.
- The manifest verifier can fail, does fail on every mutation control, and never mutates the file it verifies.
- Numerical stress tests and high-precision controls pass with zero JUnit failures or errors.
- The detached TeX build and visual audit are clean.
- The durable rigorous-theory-search release record and closure attestation in \(C\) bind clean \(E\), while the surviving active .verification/ledger.json contains the complete Section 7.3 claim inventory rebound to and validated against the exact published revision, either \(W\) after a fast-forward or a separately validated integration commit \(F\).
- git diff S..E contains evidence only, E..C contains closure records only, and C..W contains wiki records only.
- The feature branch, exact ledger-bound published revision, origin/main, and safely advanced live checkout have verified object identities, and all preexisting live WIP hashes are unchanged.

If a load-bearing mathematical claim does not survive reconstruction, publication stops. The report will name the exact failed obligation rather than laundering a partial derivation into an affirmative result.
