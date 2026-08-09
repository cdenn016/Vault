<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 15 proof-erased oracle packet

## Purpose and isolation rule

This packet contains types, primitive data, and questions only. It deliberately
omits the manuscript's theorem statements, proofs, claim ledger, construction
record, and earlier reconstruction memos. An oracle-erasure reconstruction must
derive what follows from these data or state the exact missing hypothesis.

## P. Probability and ELBO primitives

At scale \(\ell\), let \(V_\ell\) be any finite set and
\(X_\ell=\prod_{i\in V_\ell}X_{\ell,i}\) a finite product of standard-Borel
spaces. Let \(\rho_\ell\) be a probability, let
\(m_\ell=e^{-H_\ell}\rho_\ell\) be a finite positive measure with
\(0<m_\ell(X_\ell)<\infty\), and set
\(\pi_\ell=m_\ell/m_\ell(X_\ell)\).

Let \(K_\ell:X_\ell\rightsquigarrow X_{\ell+1}\) be a normalized,
parameter-independent Markov kernel. Define the pushed measures only by
\(\rho_{\ell+1}=\rho_\ell K_\ell\) and
\(m_{\ell+1}=m_\ell K_\ell\). A fixed jointly measurable reverse conditional
law \(\Pi_\ell(dx\mid z)\) disintegrates
\(\pi_\ell(dx)K_\ell(x,dz)\).

For bounded real \(\varphi\), define the perturbed finite measure
\(m_\ell^\varphi=e^{-\varphi}m_\ell\). Work on an open bounded
\(L^\infty\) chart on which all needed exponentials are uniformly bounded.
The coarse perturbation is the Radon--Nikodym action increment determined by
the pair \(((m_\ell^\varphi)K_\ell,m_\ell K_\ell)\). Constants and evidence
mass are separate typed quantities.

For a selected observation \(o\), let \(M_o=z_o\Pi_o\) be a finite evidence
slice with \(0<z_o<\infty\), and let \(Q\) be any probability law. For a
nonempty agent block \(B\), fix a measurable regular conditional version given
the outside variables. Environment nodes are standard-Borel state laws with
normalized measurable message kernels. Categorical attention labels have
positive priors, finite source energies, and a complete selected-record
likelihood in which no undeclared factor reads the label.

Questions P1--P6:

1. Determine the mass law and the exact coarse action, including its composition
   rule and the role of Radon--Nikodym versions.
2. Derive the first two Frechet derivatives of the bounded nonlinear action map,
   with their signs, equality cases, and the change caused by probability
   normalization.
3. Determine every \(L^p\) operator bound and the exact \(L^2\) defect. Extend
   the result, if valid, to a nondominated Le Cam DQM path and account for its
   singular component.
4. Define an extended-real ELBO that is safe without a classical expected-log
   split. Derive its gap, data-processing behavior, block disintegration, and
   local-versus-collective relation.
5. Decide exactly in what sense observations can be represented by agent--agent
   interactions, and whether that representation removes conditioning.
6. Derive the attention-label posterior and variational row only under the
   stated label-exclusivity and recognition assumptions.

## I. Full interaction and score primitives

At each admitted interaction scale, let \(\nu_\ell\) be a declared product
probability equivalent to \(\pi_\ell\). Let \(E_\ell\) assemble all nonempty
subset interactions in hierarchical zero-mean gauge into a bounded action
class, and let \(P_\ell\) be the corresponding extraction map. No sparse
closure is assumed. Let \(\mathsf Q_\ell\) be a separately declared bounded
idempotent projection onto a retained closed subspace.

A DQM tangent is a centered \(h\in L^2(\pi)\). In the scalar Gaussian probe,
\(X_1,\ldots,X_b\) are independent \(N(0,1)\),
\(Z=b^{-1/2}\sum_iX_i\), and \(e_k\) is the normalized probabilists' Hermite
basis. Replication is extensive: the fine score is the sum of the \(b\) copied
scores before conditional expectation onto \(Z\).

Questions I1--I5:

1. Determine whether \(P_\ell\) and \(E_\ell\) are inverse, and state the
   finite-size norm bounds and the product-reference obstruction.
2. Transport the exact nonlinear action through these maps. Derive its
   derivative at a general interaction, not only at the origin.
3. Compare the exact and retained updates and identify the necessary and
   sufficient condition for a zero truncation residual.
4. Construct a two-sided DQM path for every centered \(L^2\) score and derive
   the extensive Fisher budget.
5. Diagonalize the Gaussian block operator and classify its spectral values,
   including the status of zero and the dependence on topology, correlation,
   dimension, and normalization.

## G. Bundle and pullback primitives

Let \(P\to\mathcal C\) be a principal \(G\)-bundle and let \(E^b,E^m\) be two
associated bundles whose fibers are regular statistical manifolds. The two
representations need not be equivalent. Choose a section \(s\), a principal
connection \(\omega\), vertical projection \(P^\omega\), and fiber Fisher
metric \(g^F\). Define the covariant vertical first jet only by
\(D^\omega s=P^\omega\circ Ts\).

For a scale arrow, let \(f:\mathcal C\to\bar{\mathcal C}\) be a base map and
\(\Psi:E\to\bar E\) a typed associated-bundle morphism induced by separately
declared equivariant principal and fiber-law maps. Let
\(L=T^V\Psi\). Related sections obey \(\Psi\circ s=\bar s\circ f\). The
horizontal comparison is not assumed to commute.

Questions G1--G5:

1. Pull the fiber Fisher metric to the base and determine its gauge covariance,
   connection dependence, radical, and rank.
2. Derive the exact covariant-jet chain rule and define the horizontal anomaly
   with an explicit sign convention. Compose two arrows in the correct order.
3. Derive the vertical Fisher defect under a normalized parameter-independent
   Markov fiber map. Then derive the full base comparison with every anomaly
   cross term and give the exact positivity criterion.
4. Determine the sharp global criterion for a pointwise transformed section to
   descend through \(f\). Separate fiber constancy, smooth descent, global
   extension, and the weaker infinitesimal condition.
5. State what extra data are required to turn fiber/base tensors into a strong
   configuration metric. Account for a selected right-inverse lift, weighted
   product metrics, gauge quotients, nondegeneracy, and the possibility that
   distinct lifts induce equal metrics.

## H. Histories without primitive time

Distinguish: a curve in one fixed fiber, a total-space curve over a base curve,
a base curve, a curve of sections, and an integral curve of a VFE natural
gradient on a declared configuration manifold. A configuration coarse map
\(\mathsf R_\ell\) is separate data and is assumed smooth only where stated.
Fine and coarse objectives and strong metrics independently define vector
fields \(X_\ell\) and \(X_{\ell+1}\).

Questions H1--H4:

1. Classify vertical, connection-horizontal, mixed, stationary, base, and
   section-space curves without assigning a physical time variable.
2. Find the necessary and sufficient tangent condition for the image of a fine
   integral curve to traverse an oriented coarse orbit up to positive
   reparameterization. Include critical points, collapse, and maximal intervals.
3. Determine the additional geometric hypotheses under which compatible
   objectives imply natural-gradient semiconjugacy.
4. Define Fisher arc duration and state exactly what it does and does not provide:
   parameter invariance, zero-speed behavior, global-clock failure, and its
   separation from scale depth and physical time.

## R. Scale and effective-theory primitives

For an exact nonautonomous scale diagram, let
\(F_\ell:Y_\ell\to Y_{\ell+1}\), and along an orbit let
\(M_\ell=DF_\ell(y_\ell)\). Ordinary subtraction, spectra, or fixed points are
not formed across unequal spaces. Where comparison is needed, declare bounded
isomorphisms \(J_\ell:Y_*\to Y_\ell\), with both directions controlled. Let
\(\Delta s_\ell=\log b_\ell>0\). A retained interaction update and its residual
are separately typed.

Questions R1--R5:

1. Derive the ordered nonlinear and derivative cocycles and the compatible-line
   multiplier law.
2. Define exact and retained discrete beta data in the comparison space and
   derive their residual and reference-change laws.
3. Identify fixed objects for a genuinely nonautonomous diagram and for a
   periodic identified sequence. State when a one-step fixed point is meaningful.
4. Determine what the finite exact theory says about generated higher-body
   interactions and why a projected ansatz is not automatically closed.
5. Separate finite-network exactness from thermodynamic limits, universal
   exponents, continuous scale interpolation, and scheme-independent
   universality. State the hypotheses that would be needed to cross that boundary.

## Required output

Return a typed theorem package with direct derivations, equality conditions,
minimal counterexamples to stronger readings, and an explicit list of missing
hypotheses. Do not infer truth from the existence of this packet, the wording of
the questions, or agreement with another model.
