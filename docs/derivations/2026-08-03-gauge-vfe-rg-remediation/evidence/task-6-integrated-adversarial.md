# Task 6 integrated adversarial audit

## Scope

Four mechanism-separated read-only passes attacked the Task 6 gauge,
Gaussian/information-geometric, philosophy/source, and Campbell-primary-source
claims.  The auditors were not shown a preferred repair and did not edit the
source.  Their agreement is not closure evidence; each accepted repair below
is paired with the decisive type check, equation, counterexample, or primary
theorem in the Task 6 proof records.

## Findings found and repaired

### A6-1: edge Fisher/KL formula mixed (K)- and (NK)-dimensional objects

The first information-geometry draft inserted the assembled
(NK\times NK) precision (Lambda) into a quadratic of one edge difference
(mu_i-mu_jinmathbb R^K).  The product was undefined for (N>1).

The repaired `08_infogeometry.tex` uses one edge covariance
(C_{ij}=J_{ij}^{-1}inoperatorname{Sym}_{++}^K) and proves

\[
\operatorname{KL}\bigl(N(\mu_i,C_{ij})\Vert N(\mu_j,C_{ij})\bigr)
=\tfrac12(\mu_i-\mu_j)^\top J_{ij}(\mu_i-\mu_j).
\]

Only the sum of these typed edge quadratics defines the assembled
(NK\times NK) connection Laplacian.  The information-geometry auditor
recomputed the repaired formula and the evidence-record hash and returned
`PASS`.

### A6-2: the active gauge image was overstated as a full diagonal

The first gauge draft correctly described passive coordinate choices as an
evaluation-map image, but asserted that the image of
(operatorname{Aut}_G(P)) was the entire pointwise (h_i)-twisted diagonal.
This fails when the active gauge evaluation map is not surjective.  On a
connected base with (G=mathbb R^\times), a smooth gauge function stays in
one connected component, so pointwise diagonal values (1) and (-1) at two
design points cannot come from one gauge function.

The repaired `04_generative.tex` states containment in the twisted diagonal,
with equality only under an explicit evaluation-surjectivity hypothesis.  The
gauge auditor rechecked the revision and returned `PASS`.

### A6-3: philosophy positions carried a forbidden theorem status

The first source repair marked the van Fraassen and Esfeld--Lam position
summaries `ESTABLISHED`, contrary to `SPEC.md`'s chapter-specific rule that
interpretive claims in Chapter 12 are not theorems.  The revised prose declares
the chapter-local meanings of the two positions, cites the checked sources,
and tags them `DEFINITION`; the manuscript-to-ontology fit remains `OPEN`.

### A6-4: the operational-holonomy proposal was neither precise nor controlled

The first revision retained `CONJECTURE` without a named connection, record
map, observable class, sensitivity test, or evidence.  A subsequent positive
condition allowed two connection data sets to differ arbitrarily, so a record
difference could be caused by a non-holonomy confound.  Its claimed equivalence
to factorization through holonomy class was also too strong.

The final source labels the route `OPEN`.  A positive witness must hold every
declared non-holonomy input fixed, use distinct represented loop-holonomy
conjugacy classes, and produce different laws for one gauge-invariant
population-record statistic.  Nontrivial factorization of the controlled
record-law map through holonomy class is correctly stated as a stronger
sufficient formulation, not an equivalent condition.  The negative theorem
quantifies over the same controlled class.  The philosophy auditor returned
`PASS` after these changes.

### A6-5: evidence digests became stale during adversarial repair

Edits made in response to A6-1 through A6-4 invalidated the initial proof and
source-map digests.  The Gaussian proof now binds the repaired
`08_infogeometry.tex` digest
`0B91582CAE8E540C96E89CCD4AFAF591A3882998F26D7C493F62280688CA3BDC`.
The philosophy map now binds `12_philosophy.tex` digest
`5E717AD6C701CAA479A91308CF3C789FB3D9F56397C36FA88A06A399D8221F01`
and bibliography digest
`EA0F0B4F2800A0E711F246689CA8D54E2F57EF445B0C34491D5A3A06687A8B41`.
The gauge proof records final hashes for all three owned chapters.

## Attacks that did not break the repaired claims

- Three-frame composition preserves the declared old-to-new gauge convention;
  cross-map conversion has the required Hom-bundle gluing type.
- The mixed reference (lambda+delta_0) under (ymapsto2y) refutes a
  universal determinant density but not the general pushforward/Radon--Nikodym
  statement.
- The explicit (GL(2,mathbb R)) matrices
  (S=operatorname{diag}(2,1)) and
  (C=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}) reproduce the claimed
  nonclosure of the shared-link solution set.
- The Gaussian precision kernel and the one-positive-definite-self-term per
  connected-component criterion follow by equality in a sum of nonnegative
  quadratic forms.
- Symbolic recomputation gives zero residual for the expectation-tangent
  quotient Schur complement and for the full-rank aggregation identity.
  A 200-draw stress pass gives minimum Loewner eigenvalue
  (1.944\times10^{-3}), maximum transverse-(arepsilon) KL residual
  (1.172\times10^{-12}), and maximum relative quotient-pseudodeterminant
  residual (3.904\times10^{-15}).  These numbers corroborate but do not
  prove the identities.
- Gaussian stabilizers are closed under the continuous represented action, so
  invariance under (mathcal H) equals invariance under its closure.  Haar
  averaging is used only after (overline{mathcal H}) is assumed compact.
- Campbell (1986), p. 137, gives the cross-dimensional two-function family
  (A(s)+delta_{ij}sB(s)/x_i), with (B>0) and (A+B>0); p. 140 supplies
  the fixed-total simplex restriction.  The source auditor found no mismatch.
- The van Fraassen and Esfeld--Lam claims now say no more than the checked OUP,
  Springer, and primary-text records.

## Final adjudication

The four local adversarial lanes return `PASS` on the repaired Task 6 scope.
The separate static audit returns `PASS`.  What would falsify this conclusion
is any changed bound source byte, a type-invalid gauge or edge-Fisher
composition, a reference measure outside the stated RN tier admitted by a
determinant formula, a nontrivial vector in a precision claimed positive
definite, a primary-source theorem with different hypotheses, or a surviving
interpretive `ESTABLISHED` claim for the repaired philosophical positions.
