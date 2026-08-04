<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 8 exact finite-network interaction construction

## Scope and source binding

This derivation constructs the full bounded-action interaction coordinate
space for every finite standard-Borel agent network. It proves the
Hoeffding/Mobius assembly and extraction identities, types the exact nonlinear
interaction map and its derivative, and separates an exact map from a retained
projection and residual. It makes no infinite-network, product-preservation,
pairwise-closure, or release-build claim.

The source base revision supplied for this task is 17b59ae. The source
SHA-256 values after the Task 8 edits are:

- 06_general_coarsegraining.tex:
  5E7028EBCD5B2A311F67E3AFA39AED116CE357C47284DDE4E92808B07E9E0E79
- 07_general_renormalization.tex:
  5F0604C948220A22C3321918C0634481AD9ADB5FB4A25B1AEF78ED91A6858080
- 07b_agent_network_rg.tex:
  902E6ECF583CF084ADDCCDB3E84A265CFC8EEF5D4BA3BD3749E533295E6BD95C

The operative statements are Proposition
prop:rg-product-equivalence-not-preserved, Theorem
thm:rg-hoeffding-action-isomorphism, and Equations
eq:rg-exact-nonlinear-interaction-map through
eq:rg-interaction-exact-image-invariance.

## Assumptions and the product-reference boundary

At one scale let \(V\) be finite and
\(\mathsf X=\prod_{i\in V}\mathsf X_i\), where each coordinate is standard
Borel. Let \(\nu=\bigotimes_i\nu_i\) be a product probability and let
\(\pi\sim\nu\). At the adjacent scale the same assumptions are separately
declared for \((\mathsf X',\nu',\pi')\), with \(\pi'=\pi K\) for the admitted
normalized Markov kernel \(K\). This is a premise for the coordinate
decomposition, not a consequence of the Markov arrow.

Mutual absolute continuity identifies the \(L^\infty(\pi)\) and
\(L^\infty(\nu)\) classes and their essential-supremum norms without requiring
bounded density ratios. The product structure of \(\nu\), not equivalence by
itself, makes coordinate averaging independent of an \(L^\infty\)
representative: Fubini pushes a product-null difference to a null set of
sections.

For \(V=\varnothing\), the product is the one-point probability space and
the interaction space, assembly, extraction, and interaction maps are all
zero. The nontrivial norm quotient below is used only when the output vertex
set is nonempty.

The exact falsifier is diagonal cloning. From a uniform bit \(X\), send
\(X\) deterministically to \((X,X)\). The pushed law is supported on the
diagonal. No product probability can be equivalent to this law: positivity of
both diagonal atoms forces each marginal to charge both values, hence forces
positive off-diagonal product mass. Thus no assertion in this construction
applies at this target.

Evidence mass is not quotiented: with the canonical representative
\(\phi_g=\sum_{A\ne\varnothing}g_A\), the unnormalized measure pair retains
\(M\), while a bounded action changes it to
\(M(g)=M\,\pi(e^{-\phi_g})\). Kernel normalization gives equality of this
scalar at the output, not a normalization convention for the action quotient.

## Boolean-lattice construction

For \(A\subseteq V\), define the lifted coordinate expectation

\[
C_Af(x_A)=\int f(x_A,y_{A^c})\,\nu_{A^c}(dy_{A^c}).
\]

Fubini gives \(C_AC_B=C_{A\cap B}=C_BC_A\). Define

\[
P_A=\sum_{B\subseteq A}(-1)^{|A|-|B|}C_B.
\]

Equivalently, the commuting factors remove the mean in every active
coordinate and average every inactive coordinate. Hence

\[
P_AP_B=\mathbf1_{\{A=B\}}P_A,\qquad
\sum_{A\subseteq V}P_A=I.
\]

Put \(\mathcal H_A=P_AL^\infty(\nu)\), and take the full interaction Banach
space

\[
\mathcal G=\bigoplus_{\varnothing\ne A\subseteq V}^{\ell^1}\mathcal H_A,
\qquad \|g\|_{\mathcal G}=\sum_{A\ne\varnothing}\|g_A\|_\infty.
\]

On \(\overline{\mathfrak B}=L^\infty(\nu)/\mathbb R1\), set

\[
\phi_g=\sum_{A\ne\varnothing}g_A,\qquad E(g)=[\phi_g],\qquad
P[f]=(P_Af)_{A\ne\varnothing}.
\]

The first displayed algebra gives \(PE=I_{\mathcal G}\) and
\(EP[f]=[f-C_\varnothing f]=[f]\). The triangle inequality yields
\(\|E\|\le1\). Since \(P_A\) is a sum of \(2^{|A|}\) contractions,
\(\|P_A\|\le2^{|A|}\), hence

\[
\|P\|\le\sum_{A\ne\varnothing}2^{|A|}=3^{|V|}-1.
\]

The bound has genuine finite-network dimension dependence. For independent
\(\{-1,1\}\)-coordinates with \(\Pr(X_i=1)=p\ge1/2\) and
\(f=\prod_iX_i\), direct expansion yields

\[
\sum_{A\ne\varnothing}\|P_Af\|_\infty
=(4p-1)^{|V|}-(2p-1)^{|V|}\longrightarrow3^{|V|}-1
\quad(p\uparrow1).
\]

This establishes worst-case sharpness; it does not claim a dimension-free
extraction norm.

## Gauge covariance and its falsifier

Suppose a gauge transformation has a componentwise/permutation Borel
realization: a permutation \(\sigma\) and a product Borel isomorphism
\(\vartheta\) that pushes \(\nu\) to \(\widehat\nu\). With
\(\Theta f=f\circ\vartheta^{-1}\), Fubini then gives

\[
\Theta C_A^\nu=C_{\sigma A}^{\widehat\nu}\Theta,\qquad
\Theta P_A^\nu=P_{\sigma A}^{\widehat\nu}\Theta.
\]

Therefore both assembly and extraction intertwine the induced interaction
action. This is precisely a statement about function equivalence classes if
the underlying reverse kernels are given only almost everywhere. It does not
select a pointwise equivariant version of a disintegration.

Product-measure preservation alone is insufficient. The Haar-preserving shear
\((x_1,x_2)\mapsto(x_1,x_1+x_2)\) on \(\mathbb T^2\) sends a nonconstant
function of \(x_2\) to a function of both variables. It turns a singleton
Hoeffding component into an interaction component. A grading-intertwining
hypothesis is therefore necessary for a hyperedge-degree covariance claim.
The componentwise/permutation form is the sufficient realization declared
here; the shear does not prove it is the only possible realization.

For full action covariance, use adjacent Borel isomorphisms
\(\vartheta,\vartheta'\), transform
\(\widehat\rho=\vartheta_\#\rho\),
\(\widehat m=\vartheta_\#m\), and
\(\widehat\pi=\vartheta_\#\pi\), and assume

\[
\widehat K(\vartheta x,\vartheta'B)=K(x,B).
\]

Then

\[
\widehat m\widehat K=\vartheta'_\#(mK),\qquad
(e^{-\Theta\phi}\widehat m)\widehat K
=\vartheta'_\#((e^{-\phi}m)K).
\]

The Radon--Nikodym derivative of two measures pushed through the same Borel
isomorphism is the transported original derivative. Therefore, at the level
of equivalence classes and without choosing a pointwise reverse conditional,

\[
\widehat Q(\Theta\phi)=\Theta'Q(\phi).
\]

Differentiation at any bounded \(\phi\) gives

\[
\widehat U^{\Theta\phi}\Theta h=\Theta'U^\phi h.
\]

Combining these identities with the assembly/extraction intertwinings proves
\(\widehat T\Theta^{\mathcal G}=\Theta'^{\mathcal G}T\). If the retained
projections satisfy
\(\widehat R\Theta^{\mathcal G}=\Theta^{\mathcal G}R\) at both scales, direct
substitution gives covariance of both \(r^{\mathcal G}\) and
\(\overline r^Q\).

## Exact nonlinear map, derivative, and projection residual

For the RN-first action map \(Q\), additive homogeneity yields a quotient
map \(\overline Q\). The exact interaction step is

\[
T^{\mathcal G}=P'\overline Q E:\mathcal G\to\mathcal G'.
\]

For every bounded center \(\phi\) and bounded increment \(h\), exact algebra
gives the recentering identity

\[
Q(\phi+h)-Q(\phi)=-\log U^\phi(e^{-h}),\qquad
U^\phi k=\frac{U(e^{-\phi}k)}{U(e^{-\phi})}.
\]

The denominator is bounded above and away from zero. The operator \(U^\phi\)
is positive and unital, so for
\(\|h\|_\infty<\epsilon<\log2\),

\[
\|U^\phi(e^{-h})-1\|_\infty\le e^\epsilon-1<1.
\]

The Banach-algebra logarithm power series therefore proves local Frechet
analyticity at every bounded \(\phi\), with \(DQ(\phi)=U^\phi\). Applying
the chain rule at \(\phi_g\) gives

\[
DT^{\mathcal G}(g)=P'\,\overline{U^{\phi_g}}\,E,\qquad
U^{\phi_g}h=\frac{U(e^{-\phi_g}h)}{U(e^{-\phi_g})}.
\]

This is a bounded map between its stated different interaction spaces. The
untwisted \(U\) occurs only at \(g=0\). Along a scale sequence these are
therefore derivative-cocycle arrows, not an untyped common-space eigenvalue
equation.

Let \(R':\mathcal G'\to\mathcal G'\) be any declared bounded idempotent that
intertwines the realized gauge action. Define

\[
r^{\mathcal G}=(I-R')T^{\mathcal G}(g),\qquad
\overline r^Q=\overline QE(g)-E'R'P'\overline QE(g).
\]

Using \(E'P'=I\) on the quotient proves the exact identities

\[
\overline r^Q=E'r^{\mathcal G},\qquad
P'\overline r^Q=r^{\mathcal G}.
\]

Thus

\[
\frac{\|r^{\mathcal G}\|_{\mathcal G'}}{3^{|V'|}-1}
\le\|\overline r^Q\|_{\overline{\mathfrak B}'}
\le\|r^{\mathcal G}\|_{\mathcal G'}.
\]

Because \(E'\) is injective, either residual vanishes exactly when the other
does. Consequently the retained scheme is exact on the retained input image
if and only if

\[
T^{\mathcal G}(\operatorname{Ran}R)\subseteq\operatorname{Ran}R',
\]

equivalently if and only if \(r^{\mathcal G}(g)=0\) for every retained input.
Without that condition the retained update is explicitly a projection, not an
exact finite-dimensional RG closure.

## Falsification conditions

This construction fails on the stated interaction coordinate tier if any of
the following occurs: target product equivalence is absent; \(V\) is not
finite; a selected a.e. kernel is asserted pointwise equivariant without an
equivariant Borel version; hyperedge-degree covariance is asserted without a
grading-intertwining realization; transformed measure-pair or kernel
covariance is absent while full nonlinear covariance is claimed; the
nonlinear derivative is replaced by \(U\) away from zero; or a retained
update is called exact while either residual is nonzero. These are scope
failures, not merely missing estimates.
