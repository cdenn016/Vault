<!-- rigorous-theory-search-metadata {"schema_version":"rigorous-theory-search/v1","contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->

# Simultaneous retention of optimized collective geometry

This result sharpens the live manuscript's separate conditions for retaining a minimizing collective connection and its residual tensor. It applies to a context-independent equivariant statistical map with nonnegative Fisher loss, in the same metric normalization at both levels. It is not asserted for arbitrary prescribed connections or moving sample channels.

Let \(R:\mathcal N\to\bar{\mathcal N}\) be smooth and equivariant under a common finite-dimensional group \(G\). Work on regular finite-dimensional statistical strata with positive Fisher metrics \(g,\bar g\). Let \(J,\bar J\) be the infinitesimal action maps and assume
\[
\Delta=g-R^*\bar g\succeq0.
\]
A fixed parameter-independent Markov kernel with differentiability in quadratic mean gives this inequality through conditional score projection. A state-dependent kernel requires its full derivative and does not generally meet the premise.

For a fine section \(p(c)\), let \(A\) minimize \(g(dp(X)+J\xi,dp(X)+J\xi)\) and let \(\bar A\) minimize the corresponding coarse cost. Define
\[
r_X=dp(X)+JA(X),\qquad a_X=\bar A(X)-A(X).
\]
Equivariance implies \(dR J=\bar J\), so the coarse minimizing residual is
\[
\bar r_X=dRr_X+\bar J a_X.
\]
Fine and coarse orthogonality give
\[
g(r_X,J\xi)=0,\qquad
\bar g(dRr_X+\bar J a_X,\bar J\xi)=0.
\]
Inserting \(\xi=a_X\) into the second equation and expanding the squared norm proves
\[
h(X,X)-\bar h(X,X)
=\Delta(r_X,r_X)+\|\bar J a_X\|_{\bar g}^2\ge0.
\tag{G1}
\]
Polarization yields the bilinear version
\[
h(X,Y)-\bar h(X,Y)
=\Delta(r_X,r_Y)+\bar g(\bar J a_X,\bar J a_Y).
\tag{G2}
\]

Consequently the entire minimized contextual tensor is preserved if and only if \(\Delta(r_X,r_X)=0\) for every contextual direction. To prove the converse implication carefully, a positive semidefinite bilinear form satisfies Cauchy--Schwarz, so zero diagonal loss on \(r_X\) implies \(\Delta(r_X,J\xi)=0\) for all \(\xi\). Fine orthogonality then says that \(A\) also satisfies the coarse normal equation. Hence \(\bar J a_X=0\), and (G1) vanishes. The two affine minimizing classes agree if additionally \(\ker J=\ker\bar J\); preservation of one representative alone does not prove equality of stabilizers.

This is a score condition on the actual contextual residuals, not statistical sufficiency for the entire family. Nonzero Fisher information may be lost in other directions. In the Wishart construction in this run, shape-allocation directions carry such loss, while the common-precision contextual and orbit scores are measurable from the aggregate matrix samples.

For composable equivariant fixed Markov retentions \(R_{01},R_{12}\), use the same contextual base and the actual minimizing geometry at each stage. Applying (G1) to both stages gives
\[
h_0-h_2=(h_0-h_1)+(h_1-h_2),
\]
with both terms nonnegative. Thus exact final contextual geometry entails equality at every intervening stage. A later fixed Markov retention cannot restore a contextual tensor already lost. This conclusion is conditional on the fixed-channel, equivariance, normalization, and regular-stratum hypotheses; it does not extend to the manuscript's general signed comparison for arbitrary connections.

The only external ingredient here is fixed-channel score projection, already proved in the live manuscript at \(\texttt{geo:fisher-loss}\); (G1)--(G2) follow by the displayed normal-equation calculation. No numerical or physical claim is made.

