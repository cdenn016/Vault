# Task 6 gauge and geometry proof record

## Scope and evidence status

- Starting artifact revision: 2a4f7fea2da25afef2867f15632b8f96e2780f73.
- Owned sources: manuscripts/gauge_vfe_rg/02_geometry.tex,
  manuscripts/gauge_vfe_rg/04_generative.tex, and
  manuscripts/gauge_vfe_rg/11_obstructions.tex.
- Final owned-source SHA-256 values:
  `728AEE6C8F2FC3A3EA9B934F44EDB25C94CDEF5F4E34726665D696B0EF968A3F`,
  `FBD5181B70729B17BA5420714E97EE84763835C2470029CC02F38B4DFFD0A18B`,
  and `0895618EC0D2232015FF9ED3223AEE9C4B26DD342F8CAB1275E13DD27DB714CA`,
  respectively.
- This is mathematical proof evidence for the parent verifier. It neither edits nor adjudicates
  the central claim ledger. Every established result remains conditional on its displayed types
  and hypotheses; no hypothesis is promoted by numerical agreement or agent consensus.

## Associated-bundle and coordinate directions

The ontology at 02_geometry.tex:4-10, 46-65, 67-97, and 117-143 is type-consistent: one principal
right \(G\)-bundle induces two possibly inequivalent associated law bundles. The relative field
\(h_i\) compares two sections of that same principal bundle; it is not a cross-channel map.

For the quotient convention \((ug,v')\sim(u,gv')\), the equality
\([ug,v']=[u,v]\) is equivalent to \(gv'=v\), hence \(v'=g^{-1}v\). Therefore the old-to-new maps
in eq:geo-linear-coordinate-maps are
\[
R_i^b=\rho_b(a_i)^{-1}:V_b\to V_b,\qquad
R_i^m=\rho_m(b_i)^{-1}:V_m\to V_m.
\]
If \(A:V_b\to V_m\), then \(v_b'=R_i^bv_b\) and \(v_m'=R_i^mv_m\) give
\[
A'=R_i^mA(R_i^b)^{-1}.
\]
Interchanging the channels proves eq:geo-defect-gauge-laws. These \(R_i^x\) are invertible
same-channel coordinate maps, not cross-channel morphisms and not coarse restriction operators.

## Map-bundle conversion

From \(T_{ij}^m=h_i^{-1}T_{ij}^bh_j\) and the cross-map overlap law,
with \(f_i=\widehat\rho_m(h_i)\phi_i\),
\[
\begin{aligned}
f_i\widehat\rho_b(T_{ij}^b)
&=\widehat\rho_m(h_i)\widehat\rho_m(T_{ij}^m)\phi_j\\
&=\widehat\rho_m(T_{ij}^b)\widehat\rho_m(h_j)\phi_j
=\widehat\rho_m(T_{ij}^b)f_j.
\end{aligned}
\]
Likewise \(h_i^{-1}T_{ij}^b=T_{ij}^mh_j^{-1}\) gives
\[
\widetilde f_i\widehat\rho_m(T_{ij}^b)
=\widehat\rho_b(T_{ij}^b)\widetilde f_j,\qquad
\widetilde f_i=\widetilde\phi_i\widehat\rho_m(h_i^{-1}).
\]
These are the local-section laws for the two Hom-type associated bundles. Thus the statement at
02_geometry.tex:254-274 is valid after the explicit conversion in
eq:geo-map-bundle-frame-conversion; \(h_i\) never replaces the fiber map.

## Congruence and inverse congruence

For \(X\sim q\), \(X'=RX\), and finite second moment,
\[
\mathbb E[X']=R\mu,\qquad
\operatorname{Cov}(X')=
\mathbb E[R(X-\mu)(X-\mu)^\top R^\top]=R\Sigma R^\top.
\]
If \(\Sigma\succ0\), then
\[
(R\Sigma R^\top)^{-1}=R^{-\top}\Sigma^{-1}R^{-1}.
\]
This proves prop:geo-moment-pushforward and eq:geo-precision-inverse-congruence without requiring
equal belief and model dimensions.

## Contextual links and the non-group solution set

Chapter 2 writes a principal-section rechoice as \(u'=ua\), so old-to-new sample coordinates use
\(\rho(a)^{-1}\). Chapter 4 names that old-to-new element \(h=g=a^{-1}\). Substitution yields
\[
\Theta'=h_i\Theta h_j^{-1},\qquad
\rho_x(\Theta')=R_i^x\rho_x(\Theta)(R_j^x)^{-1}.
\]
This reconciles eq:geo-regime-two-gauge-law with eq:gen-gauge-links. The contextual
\(h_{a,i}^x\) is unrelated to the unsuperscripted relative frame \(h_i\).

At finitely many design points, the values of independently declared passive
coordinate maps fill the pointwise product only when their evaluation map is
surjective.  The values of one active principal gauge transformation are more
restricted: the overlap law places their image inside the pointwise
\(h_i\)-twisted diagonal, with equality only when the active-gauge evaluation
map onto that diagonal is surjective.  For example, on a connected base with
the disconnected group \(G=\mathbb R^\times\), a smooth gauge function takes
values in one connected component.  Hence the diagonal pointwise assignment
with value \(1\) at one design point and \(-1\) at another is not realized.
This proves why the revised source states containment rather than equality.

For the shared-link condition, take \(G=\mathrm{GL}(2,\mathbb R)\), two design points,
\(\Theta=I\), and
\[
S=\begin{pmatrix}2&0\\0&1\end{pmatrix},\qquad
C=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
The endpoint pairs \((I,I),(S,S)\) preserve \(I\) at both points. The pairs \((C,I),(C,I)\)
produce \(C\) at both points. Their pointwise product produces
\[
C\quad\hbox{and}\quad SCS^{-1}=
\begin{pmatrix}1&2\\0&1\end{pmatrix}.
\]
Thus the fixed-datum solution set in eq:gen-shared-link-admissibility is not closed under
multiplication. The manuscript now reserves the group term for the setwise stabilizer of the
entire constraint set.

## Measure pushforward and density tiers

Let \(P=p(\nu_O\otimes\nu_Y)\), \(T(o,y)=(o,Ry)\), and \(R\) be invertible. The general result is
\(P'=T_\#P\). For every bounded measurable \(F\),
\[
\int F(o,y')P'(do,dy')
=\int F(o,Ry)p(o,y)\,\nu_O(do)\nu_Y(dy).
\]
Writing \(\nu_Y'=R_\#\nu_Y\) turns the right side into
\[
\int F(o,y')p(o,R^{-1}y')\,\nu_O(do)\nu_Y'(dy').
\]
If \(\nu_Y'\ll\nu_Y\), with \(j_R=d(R_\#\nu_Y)/d\nu_Y\), uniqueness of Radon--Nikodym
derivatives proves
\[
p'(o,y')=p(o,R^{-1}y')j_R(y')
\quad(\nu_O\otimes\nu_Y)\text{-a.e.}
\]
Only for equal-dimensional Euclidean source and target coordinates with Lebesgue reference does
\(j_R=|\det R|^{-1}\). Dimensions need match only within each channel; \(K=d_m\) is not required.

The mixed-reference counterexample is \(\nu=\lambda+\delta_0\) on \(\mathbb R\) and \(R(y)=2y\):
\[
R_\#\nu=\tfrac12\lambda+\delta_0,\qquad
\frac{d(R_\#\nu)}{d\nu}(y)=
\begin{cases}1/2,&y\ne0,\\1,&y=0.\end{cases}
\]
The measure pushforward survives, while a universal determinant factor fails at the atom. This
proves the repaired scope of prop:gen-product-evidence-invariance and directly supports central
claim gauge-jacobian-scope. Since \(\pi_O\circ T=\pi_O\), observation evidence invariance itself
needs no latent density hypothesis.

## Kernel normalization and the Chapter 11 cut claim

For a probability kernel \(K:X\rightsquigarrow Y\), the explicit condition \(K(x,Y)=1\) gives
\[
(PK)(Y)=\int_XK(x,Y)P(dx)=1.
\]
The joint channel \((o,x)\mapsto\delta_o\otimes K(x,\cdot)\) fixes observations. Applying it to
posterior and recognition laws preserves the observation marginal and gives the ELBO ordering by
KL data processing. A sub-Markov kernel may lose mass, so it is outside the statement at
11_obstructions.tex:163-175.

Chapter 9 proves
\[
\Delta=\sum_e(\Theta_e-\bar\Theta)^\top W_e(\Theta_e-\bar\Theta)\succeq0,
\]
with \(\Delta=0\) exactly when cut twists coincide. Once two nonempty clusters are individually
trivializing, equality across their cut makes their union trivializing. With one cluster,
whole-population triviality is already the cluster condition. This is the exact result now used at
11_obstructions.tex:391-406.

## Compact-closure handoff proof

The sibling edit at 09_coarsegraining.tex:672-735 now integrates over
\(\overline{\mathcal H}\). If a represented subgroup is bounded, its inverses are in the same
bounded subgroup, so least singular values are bounded away from zero; its matrix closure acquires
no singular elements and is compact in \(\mathrm{GL}(K)\). The Gaussian action
\[
(h,m,C)\mapsto(hm,hCh^\top)
\]
is continuous, so a Gaussian stabilizer is closed. Therefore \(\mathcal H\)-invariance is
equivalent to \(\overline{\mathcal H}\)-invariance, and normalized Haar measure belongs on the
compact closure.

## Outside-scope handoffs

- 06_general_coarsegraining.tex:14-26 still calls \(K\) a Markov kernel without displaying
  \(K(x,\mathsf Y)=1\). Lines 229-270 say “normalized channel,” but the primary definition or
  theorem site should display the equation. This was handed to the Chapter 6/9 sibling.
- 09_coarsegraining.tex:672-735 now contains the compact-closure repair in the shared worktree; no
  Task 6 source edit was made there.
- 09_coarsegraining.tex:291-304 must retain \(R_{i,e}:\mathbb R^K\to E_e\) and
  \(R^c=R\circ S\); these are not the same-channel invertible \(R_i^x\) defined here.
- 12_philosophy.tex:103-115 now owns the base-connection conjecture and its CONJECTURE status.
  The stale Chapter 2 label sec:geo-induced-connection was removed, and no reference remains.
- Appendix owners should keep \(h_i\) and \(h_i^x\) distinct and register the new labels.
- No new bibliography key is required. Existing anchors include Kobayashi1963, Nakahara2003,
  Bleecker1981, Baez1994, and Klenke2020.

## Static validation

Run on the final owned-file state:

- Unescaped-brace balance: passed in all three owned TeX files.
- LaTeX environment stack: passed in all three owned TeX files.
- Global manuscript label scan: 804 labels, all unique.
- Removed-label scan: no occurrence of sec:geo-induced-connection.
- Added-line spacing-macro scan: no new banned manual-spacing control sequences.
- Added-line language scan: no listed UK spellings; American English check passed.
- git diff --check on all owned sources plus this artifact: passed.
- Per parent instruction, no TeX build and no commit/stage operation were performed by this task.
