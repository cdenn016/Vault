# Task 6: Gaussian, information-geometry, and coarse-graining proof record

## Revision binding

- Base revision: `2a4f7fea2da25afef2867f15632b8f96e2780f73`
- `06_gaussian.tex` SHA-256: `1FD385BF899B4A719FAA212580EA6E2CD0B90EE7ED19A72EE6D184DCBFABC916`
- `08_infogeometry.tex` SHA-256: `0B91582CAE8E540C96E89CCD4AFAF591A3882998F26D7C493F62280688CA3BDC`
- `09_coarsegraining.tex` SHA-256: `6D6A3BA9FCD2FCC001B97AC6DDF225CE4B23401A92312A25810816F196328911`

This is the task-local mathematical evidence record. The repository-wide
verification ledger and proof-control JSON remain root-owned.

## Closed claims

### G6-1 — Constructed interaction precision: `EVIDENCE_VERIFIED`

For self terms \(A_i\succeq0\) and represented edge weights
\(W_{ij}\succ0\),
\[
z^\top\Lambda z
=\sum_i z_i^\top A_i z_i
+\sum_{(i,j)\in E}(z_i-z_j)^\top W_{ij}(z_i-z_j).
\]
Every summand is nonnegative. Equality holds exactly when
\(A_i z_i=0\) for every vertex and \(z_i=z_j\) on every edge. Hence a vector
is constant on each connected component \(V_\alpha\), with its component
value in \(\bigcap_{i\in V_\alpha}\ker A_i\). This proves the displayed exact
kernel and the if-and-only-if SPD criterion. It also separates a general PSD
self term from a proper full-dimensional Gaussian prior, which requires
\(A_i\succ0\).

### IG6-1 — Expectation-chart quotient mean metric: `EVIDENCE_VERIFIED`

Partition the expectation-coordinate Fisher matrix into the mean and
second-moment blocks. The metric on the quotient by the second-moment
directions is its Schur complement \(S_g\). Block inversion gives
\(S_g^{-1}=(g_\tau^{-1})_{hh}\). Exponential-family duality gives
\(g_\tau^{-1}=g_\eta\), whose \(hh\) block is
\(\operatorname{Cov}(Y)=\Lambda^{-1}\). Therefore \(S_g=\Lambda\). The
coordinate restriction remains the larger matrix already derived in the
manuscript; restriction and quotient are now explicitly separated.

### IG6-2 — Conditional model Fisher typing: `EVIDENCE_VERIFIED`

For a fixed declared input \(X\), the conditional Fisher tensor is the
conditional expectation of the product of directional scores. For a declared
input law \(r(dX)\), the design-averaged tensor is
\(I_r=\int I_X r(dX)\). Its rank can change with \(X\) or \(r\), so it is a
Riemannian metric only on loci where the selected tensor is nondegenerate.
This removes the unstated design measure.

### IG6-3 — Fixed-covariance Gaussian KL factor: `EVIDENCE_VERIFIED`

For one edge $(i,j)$, the exact Gaussian KL formula with common
$K\times K$ covariance $C_{ij}=J_{ij}^{-1}$ is
\[
\operatorname{KL}(\mathcal N(\mu_i,C_{ij})\Vert\mathcal N(\mu_j,C_{ij}))
=\tfrac12(\mu_i-\mu_j)^\top J_{ij}(\mu_i-\mu_j).
\]
The Fisher squared norm is the quadratic without the factor \(1/2\).
The revised text therefore identifies edge KL as one half of the typed Fisher
quadratic; summing the edge quadratics assembles the $NK\times NK$ connection
Laplacian rather than inserting that assembled matrix into one edge term.

### IG6-4 — Full-rank aggregation formula: `EVIDENCE_VERIFIED`

For full-column-rank \(S\), set \(M_S=S^\top S\),
\(S^\dagger=M_S^{-1}S^\top\), and \(B=SM_S^{-1/2}\). The pushed covariance is
\[
S^\dagger\Lambda^{-1}(S^\dagger)^\top
=M_S^{-1}S^\top\Lambda^{-1}SM_S^{-1},
\]
so its precision is
\(M_S(S^\top\Lambda^{-1}S)^{-1}M_S\). Congruence of the orthonormal
restriction-versus-marginal Schur identity by \(M_S^{1/2}\) proves the stated
Loewner inequality and equality criterion.

### IG6-5 — Generalized-spectrum endpoints: `EVIDENCE_VERIFIED`

The interval and endpoint claims use only \(L\succeq0\),
\(A=\Lambda-L\succeq0\), and \(\Lambda\succ0\), through the Rayleigh quotient.
The dimension bound \(\dim\ker L\geq K\) additionally requires the
matrix-weighted interaction-Laplacian difference form. The revised
proposition now states that extra hypothesis exactly where it is used.

### IG6-6 — Campbell's nonnormalized cone family: `EVIDENCE_VERIFIED`

Campbell's characterization on \(\mathbb R_+^m\) is
\[
g_x(\partial_i,\partial_j)
=A(s)+\delta_{ij}sB(s)/x_i,\qquad s=\sum_i x_i,
\]
where \(A,B\) are arbitrary smooth functions subject to
\(B(s)>0\) and \(A(s)+B(s)>0\). On the normalized-simplex tangent space,
\(\sum_i u_i=\sum_i v_i=0\), the \(A\) term vanishes and only the constant
multiple \(B(1)\) of Fisher remains. The cone theorem is therefore a
two-function characterization, not uniqueness up to scale.

### CG6-1 — Parent family and holonomy: `EVIDENCE_VERIFIED`

The full Gaussian parent is now a separate declaration. Trivial represented
holonomy only makes its invariant subfamily equal to that parent. For a
possibly nonclosed represented holonomy subgroup \(\mathcal H\), a Gaussian
stabilizer is closed under the continuous pushforward action, so
\(\mathcal H\)-invariance is equivalent to
\(\overline{\mathcal H}\)-invariance. Haar averaging is consequently performed
over the compact closure \(\overline{\mathcal H}\), not over a potentially
nonclosed subgroup.

### CG6-2 — Quotient determinant and volume convention: `EVIDENCE_VERIFIED`

With \(d_q=(m-1)K\), the relative determinant is
\[
\det_{H\otimes I_K}(\Lambda_{\rm c})
=\operatorname{pdet}(\Lambda_{\rm c})/
(\operatorname{pdet}H)^K.
\]
For the same unnormalized quadratic factor, direct Gaussian integration gives
\(Z_{\rm std}=(2\pi)^{d_q/2}\operatorname{pdet}(\Lambda_{\rm c})^{-1/2}\)
and
\(Z_{\rm ind}=(2\pi)^{d_q/2}
\det_{H\otimes I_K}(\Lambda_{\rm c})^{-1/2}
=J_{\mathcal P}Z_{\rm std}\).
Thus the normalized density is convention independent while raw normalizers
are not.

### CG6-3 — Mean tie and transverse regularization: `EVIDENCE_VERIFIED`

The Schur complement of \(B^\top\Lambda B\) gives the exact optimized
mean-tie cost. For
\[
\Sigma_\varepsilon
=B(B^\top\Lambda B)^{-1}B^\top
+\varepsilon B_\perp B_\perp^\top,
\]
the trace is \(mK+\varepsilon\operatorname{Tr}
(B_\perp^\top\Lambda B_\perp)\), and the determinant is
\(\det(B^\top\Lambda B)^{-1}\varepsilon^r\). Substitution in Gaussian KL,
together with the block determinant identity, yields every term in the
revised exact formula; no undefined \(O(\varepsilon)\) remainder remains.

## Authoritative sources

- L. L. Campbell, “An extended Čencov characterization of the information
  metric,” `Proceedings of the AMS` 98(1), 135–141 (1986),
  DOI: 10.1090/S0002-9939-1986-0848890-5. Primary source for the
  two-function cone family. The theorem is on p. 137 and the fixed-total
  simplex restriction is on p. 140; the DOI is the durable retrieval key.
- N. N. Čencov, `Statistical Decision Rules and Optimal Inference`
  (1982). Primary monograph source for finite-simplex uniqueness.
- S.-I. Amari, “Natural gradient works efficiently in learning,”
  `Neural Computation` 10 (1998). Primary source for natural-gradient
  typing.
- S.-I. Amari and H. Nagaoka, `Methods of Information Geometry`
  (2000). Authoritative source for Fisher/KL local geometry and monotonicity.
- R. A. Horn and C. R. Johnson, `Matrix Analysis`, 2nd ed. (2013).
  Authoritative source for Schur complements and block inversion.

## Static validation

Checks were run on all three owned TeX files:

- inline delimiters: 06 = 43/43, 08 = 20/20, 09 = 275/275;
- unescaped brace counts: 06 = 530/530, 08 = 437/437, 09 = 697/697;
- begin/end environment multisets agree in every file;
- no duplicate labels within any owned file;
- no banned spacing commands `\;`, `\,`, or `\!`;
- no residual malformed `-left(` token;
- `git diff --check` passed for all owned TeX files.

No LaTeX build was run, as required by the task boundary.

## Root-owned follow-up

1. Add Campbell's issue number and DOI to `Campbell1986` in
   `references.bib`.
2. Add the new symbols and equation labels to the repository-wide notation and
   proof-control appendices if those inventories are maintained centrally.
3. Enter the claims above in the central verification ledger at the final
   integrated revision.
4. Separately repair the normalized-kernel statement in
   `06_general_coarsegraining.tex` by stating
   \(K(x,\mathsf Y)=1\); that file is outside Task 6 ownership.
