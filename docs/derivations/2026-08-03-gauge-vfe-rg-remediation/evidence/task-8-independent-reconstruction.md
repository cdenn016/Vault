<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 8 independent finite-product reconstruction

## Independence boundary and final binding

Two read-only reconstructors derived the finite-product theorem from the
frozen interfaces rather than from the manuscript proof. One concentrated on
the probability/action map and one on the Banach/Hoeffding algebra. They share
the Codex runtime, repository, and model family with the writer, so their
agreement is not itself closure; the equations below are the evidence.

The final checked source bytes are:

- 07_general_renormalization.tex:
  5F0604C948220A22C3321918C0634481AD9ADB5FB4A25B1AEF78ED91A6858080
- 07b_agent_network_rg.tex:
  902E6ECF583CF084ADDCCDB3E84A265CFC8EEF5D4BA3BD3749E533295E6BD95C
- task-8-interaction-proof.md:
  B5F3B294AF0958E4E9CFEF02F8F1DF29471295419B0F913565DB187EB0F0C4B7

## Product classes and coordinate operators

Let \(V\) be finite, \(n=|V|\), and

\[
 \nu=\bigotimes_{i\in V}\nu_i\sim\pi.
\]

Mutual absolute continuity identifies the \(L^\infty(\nu)\) and
\(L^\infty(\pi)\) equivalence classes and essential-supremum norms; no bounded
Radon--Nikodym ratios are needed. Product structure remains essential. Define
coordinate averaging by

\[
 (\mathsf E_i f)(x)
 =\int f(x_{V\setminus\{i\}},y_i)\nu_i(dy_i).
\]

Fubini gives commuting norm-one idempotents. For \(A\subseteq V\), define

\[
 \mathsf D_A
 =\left(\prod_{i\in A}(I-\mathsf E_i)\right)
  \left(\prod_{j\notin A}\mathsf E_j\right).
\]

Then

\[
 \mathsf D_A\mathsf D_B=\mathbf1_{\{A=B\}}\mathsf D_A,
 \qquad
 \sum_{A\subseteq V}\mathsf D_A=I,
 \qquad
 \mathsf D_\varnothing f=\nu(f).
\]

Equivalence alone without a product averaging law is insufficient. On the
two-point diagonal law in \(\{0,1\}^2\), an off-diagonal indicator represents
zero in \(L^\infty\) of that law, while coordinate averaging a displayed
off-diagonal representative against marginal laws can be nonzero. Thus the
product law is an operative part of the definition.

## Exact inverse theorem and norm bounds

For nonempty \(A\), put

\[
 \mathcal Z_A
 =\{h(x_A)\in L^\infty(\nu_A):
       \mathsf E_i h=0\text{ for every }i\in A\},
\]

and

\[
 \mathcal G_\nu
 =\bigoplus_{\varnothing\ne A\subseteq V}^{\ell^1}\mathcal Z_A,
 \qquad
 \|g\|_{\mathcal G_\nu}
 =\sum_{A\ne\varnothing}\|g_A\|_\infty.
\]

On
\(\mathsf B_\nu=L^\infty(\nu)/\mathbb R1\), define

\[
 E(g)=\left[\sum_{A\ne\varnothing}g_A\right],
 \qquad
 P[f]=(\mathsf D_Af)_{A\ne\varnothing}.
\]

The nonempty projectors kill constants, so \(P\) is well defined on the
quotient. Orthogonality of the commuting idempotents and the Boolean-lattice
resolution of the identity give

\[
 PE=I_{\mathcal G_\nu},
 \qquad
 EP[f]=[f-\nu(f)]=[f].
\]

The quotient norm and the \(\ell^1\) direct-sum norm yield

\[
 \|E\|\le1,
 \qquad
 \|\mathsf D_A\|\le2^{|A|},
 \qquad
 \|P\|\le3^n-1.
\]

The last constant is uniformly sharp over product probabilities. Let each
coordinate take values \(\{-1,1\}\), let
\(\Pr(X_i=1)=p>1/2\), and set \(f=\prod_iX_i\). With
\(a=2p-1\) and \(b=2p\),

\[
 \|\mathsf D_Af\|_\infty=a^{n-|A|}b^{|A|},
\]

so

\[
 \|P[f]\|_{\mathcal G_\nu}
 =(a+b)^n-a^n
 =(4p-1)^n-(2p-1)^n
 \longrightarrow3^n-1.
\]

Since \(\|[f]\|=1\), no smaller bound depending only on \(n\) is valid.
This proves the theorem for every finite \(n\), not a dimension-free bound.
For \(V=\varnothing\), both spaces and both maps are the declared trivial
zero objects.

## Nonlinear action and its derivative

Let \(Q\) be the RN-first bounded action map and \(\overline Q\) its
additively homogeneous quotient map. The exact interaction map is

\[
 T^{\mathcal G}=P'\overline QE.
\]

For the canonical representative
\(\phi_g=\sum_{A\ne\varnothing}g_A\), recentering at any bounded action gives

\[
 Q(\phi_g+h)-Q(\phi_g)
 =-\log U^{\phi_g}(e^{-h}),
\]

\[
 U^{\phi_g}k
 =\frac{U(e^{-\phi_g}k)}{U(e^{-\phi_g})}.
\]

Because \(U^{\phi_g}\) is positive and unital, the origin-centered logarithm
argument applies on every increment ball
\(\|h\|_\infty<\epsilon<\log2\). Therefore

\[
 DT^{\mathcal G}(g)
 =P'\overline{U^{\phi_g}}E.
\]

The positive sign follows by expanding \(e^{-h}=1-h+O(h^2)\) and then
applying the leading minus logarithm. The untilted \(U\) occurs only at
\(g=0\). The source initially exceeded its cited origin chart; the recentering
proposition repairs that exact defect.

The unnormalized scalar is separate:

\[
 M(g)=M\,\pi(e^{-\phi_g}),
 \qquad
 M'(g)=M(g)
\]

under a normalized scale kernel. This does not identify an action quotient
with a normalized probability path.

## Projection and exact residual

Let \(R':\mathcal G'\to\mathcal G'\) be a bounded idempotent. Set

\[
 h=\overline Q(Eg),\qquad
 g^{\mathrm{ex}}=P'h,\qquad
 r^{\mathcal G}=(I-R')g^{\mathrm{ex}},
\]

\[
 \overline r^Q=(I-E'R'P')h.
\]

Since \(E'P'=I\) on the quotient and \(P'E'=I\) on interactions,

\[
 \overline r^Q=E'r^{\mathcal G},
 \qquad
 P'\overline r^Q=r^{\mathcal G}.
\]

For nonempty output network,

\[
 \frac{\|r^{\mathcal G}\|_{\mathcal G'}}{3^{|V'|}-1}
 \le\|\overline r^Q\|_{\mathsf B'}
 \le\|r^{\mathcal G}\|_{\mathcal G'}.
\]

Hence the retained map is exact on every retained input exactly when

\[
 T^{\mathcal G}(\operatorname{Ran}R)
 \subseteq\operatorname{Ran}R'.
\]

Boundedness, idempotence, and closed range alone do not prove this invariance.

## Reconstruction verdict

PASS after repair. The current source agrees with both independent
reconstructions on the per-scale product premise, exact Boolean-lattice
inverse, sharp finite-size bound, canonical representative, nonlinear
recentered derivative, separate mass scalar, and projection residual. The
diagonal-cloning witness proves the product premise cannot be inferred from an
arbitrary normalized Markov arrow. The source and proof hashes above were
recomputed after the final recentering and RN-covariance repairs.

The verdict is falsified by a missing product target, a coordinate average not
defined from a product law, a fixed-\(U\) derivative away from zero, a
dimension-free extraction claim, or a zero-residual claim without exact-image
invariance.
