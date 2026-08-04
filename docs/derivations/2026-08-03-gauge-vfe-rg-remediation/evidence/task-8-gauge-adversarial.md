<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 8 gauge and interaction adversarial audit

## Scope and provenance

This read-only audit attacked the full finite-network interaction theorem from
the product-reference, gauge-realization, Radon--Nikodym, nonlinear-derivative,
and projection-residual interfaces. It was performed separately from the
source writer. The auditor and writer share the repository, runtime, and model
family, so this is mechanism-separated adversarial evidence rather than
statistical independence.

The final audited bytes are:

- 06_general_coarsegraining.tex:
  5E7028EBCD5B2A311F67E3AFA39AED116CE357C47284DDE4E92808B07E9E0E79
- 07_general_renormalization.tex:
  5F0604C948220A22C3321918C0634481AD9ADB5FB4A25B1AEF78ED91A6858080
- 07b_agent_network_rg.tex:
  902E6ECF583CF084ADDCCDB3E84A265CFC8EEF5D4BA3BD3749E533295E6BD95C
- task-8-interaction-proof.md:
  B5F3B294AF0958E4E9CFEF02F8F1DF29471295419B0F913565DB187EB0F0C4B7

## Attack 1: product equivalence is not preserved by a Markov arrow

Let the fine law be uniform on one bit and let the deterministic channel send
\(x\) to \((x,x)\). Its output gives mass \(1/2\) to each diagonal atom and
zero to each off-diagonal atom. If a product law
\(\nu_1=\nu_{11}\otimes\nu_{12}\) were equivalent to it, positivity of both
diagonal atoms would force each marginal to charge both zero and one. The
product would then give positive mass to both off-diagonal atoms, contradicting
absolute continuity with respect to the diagonal law.

The repaired theorem therefore assumes separately at every admitted scale

\[
 \nu_\ell=\bigotimes_i\nu_{\ell i}\sim\pi_\ell,
 \qquad
 \pi_{\ell+1}=\pi_\ell K_\ell\sim\nu_{\ell+1}.
\]

It does not infer the target product tier from normalization or from the fine
product tier. The attack is rejected after this scope repair.

## Attack 2: product-measure preservation does not preserve interaction degree

On the Haar product torus, the shear

\[
 (x_1,x_2)\longmapsto(x_1,x_1+x_2\bmod1)
\]

preserves the product measure. It nevertheless sends a nonconstant singleton
function of \(x_2\) to a function of both coordinates. Hence product-measure
preservation alone does not intertwine the Hoeffding grading.

The repaired theorem uses a componentwise Borel realization, with an
explicitly tracked coordinate permutation, as its declared sufficient
hypothesis. It correctly says only that some grading-intertwining condition is
necessary; it does not claim that this realization is logically unique.

## Attack 3: coordinate covariance does not imply nonlinear RG covariance

The first source version proved only the intertwinings of coordinate
expectations, Hoeffding projectors, assembly, and extraction, then claimed
covariance of the nonlinear map and residuals. That inference was invalid
without the scale-kernel square.

The repaired source now transforms the full measure pair and assumes

\[
 \widehat K_\ell(\vartheta_\ell x,
                  \vartheta_{\ell+1}B)=K_\ell(x,B).
\]

Consequently

\[
 \widehat m_\ell\widehat K_\ell
 =(\vartheta_{\ell+1})_\#(m_\ell K_\ell),
\]

and the same identity holds for the perturbed numerator. Transport of the
Radon--Nikodym derivative under one Borel isomorphism gives, as equivalence
classes,

\[
 \widehat Q_\ell\Theta_\ell
 =\Theta_{\ell+1}Q_\ell.
\]

This proof does not select or promote a pointwise equivariant reverse-kernel
version. Differentiation gives

\[
 \widehat U_\ell^{\Theta_\ell\phi}\Theta_\ell h
 =\Theta_{\ell+1}U_\ell^\phi h,
\]

and composition with the assembly/extraction intertwinings yields covariance
of the exact nonlinear interaction map. If the retained projections also
intertwine, both the coordinate and action-quotient residuals transform
covariantly. The missing square is therefore closed.

## Attack 4: the derivative was initially asserted outside its proved chart

The initial Task 8 text cited the origin-centered Task 7 chart while asserting
the tilted derivative at every bounded interaction. The repaired source adds
the exact recentering identity

\[
 Q(\phi+h)-Q(\phi)=-\log U^\phi(e^{-h}),
 \qquad
 U^\phi k=\frac{U(e^{-\phi}k)}{U(e^{-\phi})}.
\]

For bounded \(\phi\), positivity and unitality give

\[
 e^{-\lVert\phi\rVert_\infty}
 \le U(e^{-\phi})
 \le e^{\lVert\phi\rVert_\infty}.
\]

Thus \(U^\phi\) is positive and unital. If
\(\lVert h\rVert_\infty<\epsilon<\log2\), then

\[
 \lVert U^\phi(e^{-h})-1\rVert_\infty
 \le e^\epsilon-1<1.
\]

The Banach-algebra logarithm series converges and proves local Frechet
analyticity at every bounded center with \(DQ(\phi)=U^\phi\). The exact
interaction derivative is therefore valid on the entire bounded interaction
space, locally at each point.

## Final verdict

PASS. The two load-bearing blockers and the shear wording defect found in the
first audit were repaired and rechecked. The diagonal product boundary,
common-null-set tier, finite Boolean-lattice algebra, sharp dimension-dependent
bound, empty-network convention, evidence-mass scalar, nonlinear tilted
derivative, exact residual identities, and exact-image-invariance biconditional
all survive the post-repair audit. No TeX build or source edit was performed by
the auditor.

This verdict is falsified by any change to a bound byte, any admitted arrow
without target product equivalence, any nonlinear covariance claim lacking the
RN/kernel square, any derivative outside a proved local chart, or any projected
flow called exact with nonzero residual.
