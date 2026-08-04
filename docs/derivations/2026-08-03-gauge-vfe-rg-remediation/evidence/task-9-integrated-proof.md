<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 9 integrated construction: score lift, Hermite spectrum, generalized modes, cocycles, beta functions, and fixed objects

## 1. Scope and revision binding

This record binds the Task 9 integration pass. It is a construction record, not
a proposal: every theorem named below is stated and proved in the released
source at the digests in Section 3.

**Pre-edit base.** Commit `3dbe4c6` (`docs: construct exact finite-network
interaction RG`) on branch
`codex/gauge-vfe-rg-theory-remediation-20260804`. At the start of this pass the
working tree carried, in addition to that commit, only the three untracked
independent Task 9 analyses listed in Section 2 and three untracked
`.verification/*.json` files that this pass did not read for content, did not
modify, and does not bind.

**Pre-edit digests of the modified sources**, as recorded independently by
`evidence/task-8-static-proof-control.md` and by the Task 9 analyses:

| Path | Pre-edit SHA-256 |
| --- | --- |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `5F0604C948220A22C3321918C0634481AD9ADB5FB4A25B1AEF78ED91A6858080` |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `902E6ECF583CF084ADDCCDB3E84A265CFC8EEF5D4BA3BD3749E533295E6BD95C` |
| `manuscripts/gauge_vfe_rg/08_infogeometry.tex` | `0B91582CAE8E540C96E89CCD4AFAF591A3882998F26D7C493F62280688CA3BDC` |
| `manuscripts/gauge_vfe_rg/appendix_notation.tex` | `0CD7926AAC4568FA771136400B04F46808E4384791C7D2A11D7151304D64884B` |
| `manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex` | `10D5C12A97CBCDD48EBF7E46854BF56FA01D00DC5F52D091E7513AEEDB1E4FA1` |

No TeX build and no Git operation was run by this pass. No file under
`.verification/` and no
`manuscripts/gauge_vfe_rg/verification/current-results.json` was read for
binding, modified, or bound.

## 2. Independence boundary of the inputs

Three mechanism-separated Task 9 analyses were produced independently of this
integration and are not edited by it. They are search and audit inputs; the
displayed derivations in the released source, not agreement among the analyses,
supply closure.

| Artifact | SHA-256 | Family |
| --- | --- | --- |
| `evidence/task-9-score-dqm-analysis.md` | `78b5b72730fc6ec4a2482137cc9911e9995955c61de74438259ec347e7cb3694` | `family-score-dqm-tangents` |
| `evidence/task-9-hermite-analysis.md` | `7a94cdf1776d7d7fb88a8672bedd042c739c66b4a5c61e8dcc98f27d1d83beeb` | `family-gaussian-hermite-spectrum` |
| `evidence/task-9-cocycle-beta-analysis.md` | `cca923e14e943680636e9e27e0840385d04587fe1423597ec5e0f376fb3eb267` | `family-transfer-cocycle` |

The three share the repository, runtime, and model family. They are
mechanism-diverse inputs, not independent corroborating evidence. Their
convergences and the redirects imposed on them are recorded in
`approach-registry.json`.

The Task 8 oracle-separated reconstruction that this pass builds on,
`evidence/task-8-independent-reconstruction.md`, has digest
`7c0ae6de11da4f50abdd0cb246cc99dd08abd13e5e6bdfeafdca67858efd1429` and was not
re-run here; it is bound only so that the interfaces this pass consumes are
traceable.

Two independent type separations were produced by all three routes without
contact: the bounded \(L^\infty\) nonlinear action chart is not the \(L^2\)
quadratic-mean tangent, and a cross-scale mode is a compatible line rather than
an eigenvector. Because their derivations are disjoint, that agreement is
convergence of type discipline and is not treated as corroboration of any
theorem.

## 3. Final source digests

| Path | Post-edit SHA-256 |
| --- | --- |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `a3a7ae2fed2eb4a1ea4668393a69b4d56aa2c9dd071af06ddbcba717d7365797` |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `148d9652229eb6d3c40a41b48c1eb938328ca697a37e8113111567c580cc61be` |
| `manuscripts/gauge_vfe_rg/08_infogeometry.tex` | `55bfcdff0eebec24f2231852467255d13a0c02d1369621d04ede53cad3b7c31b` |
| `manuscripts/gauge_vfe_rg/appendix_notation.tex` | `d39936499c9673c1b4ed75ae31bf294f8d4df9fd1fd0cef1dae4a9ec5a572fa4` |
| `manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex` | `bbb02a24ed0875ff287aa072fddae359f4ccd59058157503d4e93502a4e6b436` |
| `manuscripts/references.bib` | `f520c0a7a20e994786e5946f2b6484120d371d8b90a79f37895e22666e93bded` |

`07b_agent_network_rg.tex` carries a later revision than the other five rows.
Its digest at the close of the integration pass was
`d4fd13fcdacf464b781456d2388c2521ddafe57418a008e01ce679cf5e57804f`. An
independent adversarial audit then returned **FAIL** against exactly those bytes
for a LaTeX-semantics defect in four heading calls, and the four-line repair
recorded in section 7.1 produced the digest in the table. Reversing those four
line joins reproduces `d4fd13fc...` byte for byte, which establishes mechanically
that the repair changed nothing else. No other source in the table changed, and
no theorem statement, proof, equation, notation, citation, or status tag was
touched, so the theorem inventory in section 4 stands unchanged.

## 4. Theorem inventory

Every entry gives the exact statement, its source anchor, and the load-bearing
step of its proof. The anchors are label names, which are stable under
repagination.

### T1. Quadratic-mean tangent is exactly the centered square-integrable space

*Source:* `def:rg-dqm-score` and the centering paragraph, plus
`lem:rg-dqm-realization`, in `07b_agent_network_rg.tex`.

For a probability space \((\mathsf W,\mathscr W,\mu)\), a family
\(\mu_t\ll\mu\) with \(\mu_0=\mu\) is differentiable in quadratic mean with
score \(h\) when
\(\lVert\sqrt{d\mu_t/d\mu}-1-\tfrac t2h\rVert_{L^2(\mu)}=o(|t|)\) as
\(t\to0\) from both sides.

*Centering is forced.* With \(p_t=d\mu_t/d\mu\), the exact identity
\(\int(\sqrt{p_t}-1)d\mu=-\tfrac12\int(\sqrt{p_t}-1)^2d\mu\) follows from
\(\int p_t d\mu=1\) and \((\sqrt{p_t}-1)^2=p_t-2\sqrt{p_t}+1\). Inserting the
expansion makes the left side \(\tfrac t2\mu(h)+o(|t|)\) and the right side
\(-\tfrac{t^2}8\lVert h\rVert_2^2+o(t^2)\), so \(\mu(h)=0\).

*Realization.* For \(h\in L^2_0(\mu)\), \(a=\lVert h\rVert_2^2/4\),
\(s_t=1+th/2\), \(N_t=1+at^2\), the path \(p_t=s_t^2/N_t\) is a probability
density for every real \(t\), and
\[
\sqrt{p_t}-s_t=\frac{|s_t|-s_t}{\sqrt{N_t}}+s_t\left(N_t^{-1/2}-1\right).
\]
On \(\{s_t<0\}\) one has \(|th/2|>1\), hence
\(|s_t|=|th/2|-1\le|th|/2\) and \(|s_t|-s_t=2|s_t|\le|th|\). Since
\(N_t\ge1\), the first term has squared norm at most
\(t^2\int h^2\mathbf 1_{\{|h|>2/|t|\}}d\mu=o(t^2)\) by dominated convergence.
Because \(\lVert s_t\rVert_2=\sqrt{N_t}\), the second term has norm exactly
\(|1-\sqrt{N_t}|=O(t^2)\). No exponential moment and no boundedness is used;
the path is two-sided.

*Falsifier discharged:* the claim that the tangent set is only the bounded
scores. For \(\mu=N(0,1)\) and \(h(x)=x\) the construction realizes an
unbounded score.

### T2. Independent block replication and its exact norm

*Source:* `prop:rg-score-block-lift`, `eq:rg-score-replication`,
`eq:rg-score-replication-norm`.

\(\mathscr I_bh(x_1,\dots,x_b)=\sum_ih(x_i)\) is the score of
\(\mu_t^{\otimes b}\), and
\(\lVert\mathscr I_bh\rVert^2_{L^2(\mu^{\otimes b})}=b\lVert h\rVert^2_{L^2(\mu)}\),
so \(\lVert\mathscr I_b\rVert=\sqrt b\) exactly and \(b^{-1/2}\mathscr I_b\) is
an isometry onto its range.

*Proof step.* With \(r_t=1+\tfrac t2h+t\varepsilon_t\) and
\(\lVert\varepsilon_t\rVert_2\to0\), expand the finite product
\(\prod_i(1+u_i)\), \(u_i=\tfrac t2h(x_i)+t\varepsilon_t(x_i)\). Independence
makes \(L^2\) norms of coordinate products factor, so every term with at least
two factors is \(O(t^2)\), and the first-order remainder is bounded by
\(b|t|\lVert\varepsilon_t\rVert_2\). The norm identity is independence plus
centering, which kills the \(b(b-1)\) cross terms.

*Falsifier discharged:* replacing the sum by the arithmetic mean without
rescaling the path parameter changes the Fisher information from
\(b\lVert h\rVert^2\) to \(\lVert h\rVert^2/b\).

### T3. Pushed score and the exact extensive Fisher defect

*Source:* `thm:rg-score-pushforward-defect`,
`eq:rg-score-renormalization-operator`, `eq:rg-extensive-fisher-defect`.

For a normalized parameter-independent Markov kernel \(C_b\) between
standard-Borel spaces, the pushed path is differentiable in quadratic mean with
score \(\mathscr L_bh=U_b\mathscr I_bh=\mathbb E[\sum_ih(X_i)\mid Z]\), and
\[
b\lVert h\rVert^2-\lVert\mathscr L_bh\rVert^2
=\int\operatorname{Var}(\mathscr I_bh\mid Z=z)\,\mu^{(b),c}(dz)\ge0,
\]
with equality exactly when \(\mathscr I_bh\) is jointly almost surely a
measurable function of \(Z\).

*Proof steps.* For bounded \(h\) the canonical path has a uniform expansion
\(d\mu_t^{\otimes b}/d\mu^{(b)}=1+t\mathscr I_bh+O(t^2)\); conditional
expectation preserves uniform \(O(t^2)\) control, and the square root has a
uniform expansion, so the pushed path is differentiable in quadratic mean with
the conditional score. For general \(h\) the argument is an approximation in
which the only nontrivial input is the data-processing inequality for squared
Hellinger distance, an \(f\)-divergence with \(f(u)=(\sqrt u-1)^2\) convex; the
resulting limit superior is bounded by \(\sqrt b\lVert h-h_n\rVert_2\) for every
\(n\), and the left side does not depend on \(n\). The budget identity is the
total conditional variance decomposition applied to \(\mathscr I_bh\).

*Falsifiers discharged.* A channel collapsing each block to a point annihilates
the whole tangent, so no lower bound on \(\lVert\mathscr L_b\rVert\) is
available in general. Fisher equality at one parameter is not experiment
recovery: with independent \(A,B\),
\(\Pr_\theta(A=1)=\tfrac12+\tfrac\theta4\),
\(\Pr_\theta(B=1)=\tfrac12+\tfrac{\theta^2}4\), and the channel retaining only
\(A\), equality holds at \(\theta=0\) while the conditional law of \(B\) still
moves with \(\theta\).

### T4. Bounded action quotient, isometry, and Fisher completion

*Source:* `prop:rg-action-score-isometry`, `eq:rg-action-score-map`,
`eq:rg-action-fisher-norm`, `eq:rg-score-action-square`.

\(\mathscr S_\pi[\varphi]=-\varphi+\pi(\varphi)\) is the score of the normalized
exponential path, depends only on the class, and is an isometry from
\((\overline{\mathfrak B},\lVert\cdot\rVert_F)\) onto the bounded centered
subspace of \(L^2_0(\pi)\); that subspace is dense and generally proper, so the
Fisher completion of the bounded action quotient is canonically
\(L^2_0(\pi)\). The two quotient norms satisfy
\(\lVert[\varphi]\rVert_F\le\lVert[\varphi]\rVert_{\mathrm{osc}}\) because the
\(L^2\) infimum over constants is bounded by the \(L^\infty\) infimum. The
centering square \(\mathscr S_{\pi^c}(\overline U[\varphi])=U\mathscr S_\pi[\varphi]\)
is mean preservation of \(U\), and the replicated action satisfies
\(\mathscr S_{\mu^{(b)}}[\Phi_\varphi]=\mathscr I_b\mathscr S_\mu[\varphi]\).

This is the exact seam between the nonlinear \(L^\infty\) chart and the
\(L^2\) tangent: the completion introduces unbounded scores on which the
nonlinear bounded action map is undefined, so a spectral statement proved on
\(L^2_0\) is not a statement about the nonlinear chart and conversely.

### T5. Gaussian block spectrum for every integer \(b\ge2\)

*Source:* `thm:rg-gaussian-hermite-spectrum`, `eq:rg-hermite-eigenvalues`,
`eq:rg-hermite-spectrum`, `eq:rg-mehler-generating`.

With \(\gamma=N(0,1)\), \(Z=b^{-1/2}\sum_{i=1}^bX_i\) (whose law is again
\(\gamma\), which is what makes \(\mathscr L_b\) an endomorphism), and
\(e_k=\mathrm{He}_k/\sqrt{k!}\):

\[
\mathscr L_be_k=b^{1-k/2}e_k\ (k\ge1),
\qquad
\sigma(\mathscr L_b)=\{b^{1-k/2}:k\ge1\}\cup\{0\}.
\]

\(\mathscr L_b\) is self-adjoint, positive, diagonal, Hilbert--Schmidt with
\(\sum_{k\ge1}b^{2-k}=b^2/(b-1)\), hence compact; its norm and spectral radius
are \(\sqrt b\); every nonzero spectral value is a simple eigenvalue; and \(0\)
is not an eigenvalue but lies in the continuous spectrum.

*Proof steps.* \((X_i,Z)\) is jointly centered Gaussian with unit variances and
correlation \(b^{-1/2}\), so \(X_i\mid Z=z\sim N(z/\sqrt b,1-1/b)\). Conditioning
the generating function and completing the square gives
\(\mathbb E[e^{tX_i-t^2/2}\mid Z=z]=e^{sz-s^2/2}\) with \(s=t/\sqrt b\); the two power
series may be compared term by term because the generating expansion converges
in \(L^2(\gamma)\) locally uniformly in the parameter and conditional
expectation is \(L^2\) continuous. This yields
\(\mathbb E[\mathrm{He}_k(X_i)\mid Z]=b^{-k/2}\mathrm{He}_k(Z)\); summing the \(b\)
replicated coordinates gives the eigenvalue. The argument is uniform in \(b\)
and is not an induction from the binary case. For the spectrum: a bounded
operator agreeing with a diagonal action on a complete orthonormal basis is that
diagonal operator; eigenvalues are positive and strictly decreasing, so the
kernel is trivial and the spectrum is the closure of the eigenvalue set. The
range is dense because it contains all finite Hermite expansions, and proper
because \(y=\sum_kb^{1-k/2}e_k\) lies in the space while its formal preimage has
all coefficients \(1\), which is not square summable. An injective operator with
dense nonclosed range has \(0\) in the continuous spectrum.

*Relevance classes.* `def:rg-hermite-relevance` fixes the four conventions
(replication sum, block statistic, fixed Fisher norm at every scale, cumulative
log block scale \(\Delta s=\log b\)) and then \(y_k=1-k/2\): degree one
relevant, degree two marginal, degree three and higher irrelevant. The constant
mode is absent from the normalized tangent.

*Why the relevant branch is inhabited here and not in the bounded action
sector.* The bounded action map is nonexpansive by
`eq:rg-nonlinear-action-sup-contraction` and the one-arrow conditional
expectation is a contraction by `thm:rg-action-lp-contraction`. The eigenvalue
exceeds one only through the extensive replication factor
\(\lVert\mathscr I_b\rVert=\sqrt b\) with the norm held fixed across scales.
Relevance is a joint property of the operator, the extensive normalization, the
declared norms, and the block scale; removing any one removes the conclusion.

### T6. Convention dependence and the forbidden extensions

*Source:* `prop:rg-hermite-scope`, `eq:rg-hermite-correlated`.

Four exact boundaries. Jointly centered Gaussian coordinates with unit variances
and common pairwise correlation \(\rho>-1/(b-1)\), renormalized to unit output
variance, give
\(\mathscr L_{b,\rho}e_k=b^{1-k/2}[1+(b-1)\rho]^{k/2}e_k\), which differs from
the independent formula for every \(\rho\ne0\); retaining the uncorrelated
normalization instead destroys the property that the output law is \(\gamma\),
so the operator is then not an endomorphism at all. The isotropic multivariate
case has \(\mathscr L_be_\alpha=b^{1-|\alpha|/2}e_\alpha\) with multiplicity
\(\binom{d+k-1}{k}\) at degree \(k\), not one. A common orthogonal action
preserves each degree space, while a general \(\mathrm{GL}(d)\) action changes the
reference covariance and needs a transported family of laws and tangent norms;
no gauge link, curvature, or holonomy datum enters the scalar theorem.
Replication is a restricted direction of \(L^2_0(\gamma^{\otimes b})\) and says
nothing about interaction scores or higher Hoeffding sectors.

### T7. Exact Hermite exponential-action domain boundary

*Source:* `prop:ig-hermite-exponential-domain` in `08_infogeometry.tex`.

With \(N_k(t)=\int e^{-t\mathrm{He}_k}d\gamma\): \(N_1\) is finite for every
\(t\); \(N_2(t)=e^t(1+2t)^{-1/2}\) is finite exactly for \(t>-1/2\); for odd
\(k\ge3\), \(N_k(t)=+\infty\) for every \(t\ne0\); for even \(k\ge4\),
\(N_k\) is finite exactly for \(t\ge0\).

*Proof step.* For \(k\ge3\) the exponent \(-t\mathrm{He}_k(x)-x^2/2\) has
leading behavior \(-tx^k\), which dominates the Gaussian quadratic. For odd
\(k\) exactly one tail diverges for each \(t\ne0\); for even \(k\) both tails
diverge when \(t<0\) and both are super-Gaussianly suppressed when \(t>0\).

*Consequence recorded in the source.* A complete Hermite basis of
\(L^2_0(\gamma)\) is neither a chart of the Gaussian exponential family nor a
set of directions of the bounded action space. The Gaussian mean and covariance
scores of `eq:ig-score` occupy Hermite degrees one and two and therefore do
possess two-sided neighborhoods, with the variance constraint \(t>-1/2\) being
the natural-domain boundary \(J\succ0\) seen through the exponential chart.

### T8. Ordered derivative cocycle and generalized modes

*Source:* `def:rg-derivative-cocycle`, `prop:rg-cocycle-composition`,
`def:rg-mode-line`, `prop:rg-mode-product` in
`07_general_renormalization.tex`; instantiated at
`def:rg-interaction-modes` in `07b_agent_network_rg.tex` with
\(M_\ell=DT_\ell^{\mathcal G}(g_\ell)=P_{\ell+1}\overline{U_\ell^{\phi_{g_\ell}}}E_\ell\).

Ordered composition
\(\Phi_{r\leftarrow n}\Phi_{n\leftarrow\ell}=\Phi_{r\leftarrow\ell}\),
\(M_{n\leftarrow\ell}=D\Phi_{n\leftarrow\ell}(x_\ell)\), and
\(M_{r\leftarrow n}M_{n\leftarrow\ell}=M_{r\leftarrow\ell}\) are proved by the
Frechet chain rule and induction. Mode lines are defined by
\(M_\ell v_{\ell,a}=\lambda_{\ell,a}v_{\ell+1,a}\) and obey the ordered product
law \(\lambda_{n\leftarrow\ell,a}=\prod_{k=\ell}^{n-1}\lambda_{k,a}\), with the
empty product one and annihilation from any zero factor.

*Falsifiers discharged.* Order matters:
\(A=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\),
\(B=\begin{psmallmatrix}1&0\\1&1\end{psmallmatrix}\) give
\(BA\neq AB\), so an unordered or reversed product is wrong in dimension two.
Typing matters: with \(X_0=\mathbb R\), \(X_1=\mathbb R^2\), \(M_0x=(x,0)\), the
expression \(M_0v=\lambda v\) equates elements of different spaces, while the
compatible line \(v_0=1\), \(v_1=(1,0)\), \(\lambda_0=1\) is well typed.

### T9. Growth rates, tempered comparison, and superexponential distortion

*Source:* `def:rg-mode-exponents`, `prop:rg-mode-tempered-normalization`,
`thm:rg-tempered-comparison`, `prop:rg-superexponential-distortion`;
`cor:rg-interaction-tempered` in `07b_agent_network_rg.tex`.

Growth is measured only relative to the cumulative log block scale
\(s_{n\leftarrow\ell}=\sum_{k=\ell}^{n-1}\log b_k\) and the declared norms.
The exact relation
\(\chi_{n\leftarrow\ell}(v_{\ell,a})=y_{n\leftarrow\ell,a}+[\log\lVert v_{n,a}\rVert_n-\log\lVert v_{\ell,a}\rVert_\ell]/s_{n\leftarrow\ell}\)
separates scalar coefficient growth from norm growth. Under scalar regauging
\(v'_{\ell,a}=c_{\ell,a}v_{\ell,a}\) the coefficients transform by
\(c_{\ell,a}/c_{\ell+1,a}\) and telescope, so the scalar exponent survives
exactly under \(|\log|c_{n,a}||/s_{n\leftarrow\ell}\to0\).

Exponent invariance under a change of comparison trivialization
\(J_\ell:X_\star\to X_\ell\) is proved only under the two-sided tempering
condition
\((\log^+\lVert J_n\rVert+\log^+\lVert J_n^{-1}\rVert)/s_{n\leftarrow\ell}\to0\),
via the operator-norm sandwich
\(\lVert x_n\rVert_n/\lVert J_n\rVert\le\lVert J_n^{-1}x_n\rVert_\star\le\lVert J_n^{-1}\rVert\lVert x_n\rVert_n\).

*Superexponentially distorted identity-cocycle falsifier.* Take \(X_k=\mathbb R\)
with the absolute value, every \(M_k\) the identity, \(b_k=e\), and every scalar
gauge factor one, so the native exponent is zero and the scalar normalization is
tempered. Take \(J_ku=e^{k^2}u\). Then
\(\widehat M_k=e^{-2k-1}\), \(\widehat M_{n\leftarrow0}=e^{-n^2}\),
\(s_{n\leftarrow0}=n\), and the apparent reference exponent is \(-n\to-\infty\).
Tempering the mode sections alone is therefore insufficient; the complete
trivialization and its inverse must be tempered.

*Interaction-tier consequence.* The sharp extraction bound
\(\lVert P_\ell\rVert\le3^{|V_\ell|}-1\) makes any trivialization assembled from
the Hoeffding maps satisfy
\(\log^+\lVert J_n\rVert+\log^+\lVert J_n^{-1}\rVert\le c(1+|V_n|)\), so
tempering holds whenever \(|V_n|/s_{n\leftarrow\ell}\to0\), in particular for
every blocking sequence with nonincreasing vertex counts and \(b_k\ge b>1\).
This converts the Task 8 finite-size bound into a checkable hypothesis of the
mode theory.

*Oseledets.* The source defines the growth rates and explicitly declines an
Oseledets splitting, listing the missing hypotheses (measure-preserving base
flow, measurability of the cocycle in the base variable, integrability of
\(\log^+\lVert M\rVert\) and \(\log^+\lVert M^{-1}\rVert\), finite dimension or a
compactness hypothesis) and citing Arnold's monograph for the theorem, with
status `NOT-CLAIMED`. A definition was chosen over an existence claim.

### T10. Typed beta functions

*Source:* `prop:rg-action-beta-reference-change`, `def:rg-interaction-beta`,
`prop:rg-retained-beta-residual`, `def:rg-scale-connection`,
`prop:rg-continuous-beta-underdetermined`.

**Change of reference for the action beta.** With \(m=e^{-H}\rho\), bounded
\(\Delta\) satisfying \(\rho(e^{-\Delta})=1\), \(\rho'=e^{-\Delta}\rho\) and
\(H'=H-\Delta\) (so \(e^{-H'}\rho'=m\)):
\[
\mathcal R_b^H[H';\rho']=\mathcal R_b^H[H;\rho]-\mathcal R_b^H[\Delta;\rho],
\qquad
\mathfrak B_b^H[H';\rho']=\mathfrak B_b^H[H;\rho]-\mathfrak B_b^H[\Delta;\rho].
\]
The proof is the Radon--Nikodym chain rule
\(d(mK_b)/d(\rho'K_b)=[d(mK_b)/d(\rho K_b)][d(\rho'K_b)/d(\rho K_b)]^{-1}\)
together with the conditional-partition formula, which identifies the second
factor as \(\exp(-\mathcal R_b^H[\Delta;\rho])\), strictly positive and finite
because \(\Delta\) is bounded. The law is inhomogeneous, not a linear
reparameterization, and the added term vanishes exactly when
\(\mathcal R_b^H[\Delta;\rho]=\Delta\).

**Typed discrete interaction beta.** For declared
\(J_\ell:\mathcal G_\star\to\mathcal G_\ell\) (the inverse orientation of
\(I_\ell\)),
\[
\widehat T_\ell^{\mathcal G}=J_{\ell+1}^{-1}T_\ell^{\mathcal G}J_\ell,
\qquad
\beta_\ell^{\mathrm{ex}}(g)=\frac{\widehat T_\ell^{\mathcal G}(g)-g}{\Delta s_\ell},
\qquad \Delta s_\ell=\log b_\ell .
\]
Both numerator terms lie in \(\mathcal G_\star\); the subtraction
\(T_\ell^{\mathcal G}(g)-g\) across \(\mathcal G_{\ell+1}\) and
\(\mathcal G_\ell\) is never formed. The retained projection symbol \(R_\ell\)
is not reused for this map.

**Retained beta and transported residual.** With
\(\widehat R_\ell=J_\ell^{-1}R_\ell J_\ell\),
\[
\delta\beta_\ell(g)
=\frac{(I-\widehat R_{\ell+1})\widehat T_\ell^{\mathcal G}(g)}{\Delta s_\ell}
=\frac{J_{\ell+1}^{-1}r_{\ell+1}^{\mathcal G}(J_\ell g)}{\Delta s_\ell},
\qquad
\delta\overline\beta_{\ell+1}^{Q}
=\frac{E_{\ell+1}r_{\ell+1}^{\mathcal G}}{\Delta s_\ell},
\]
and \(\delta\beta_\ell\) vanishes on the whole retained sector if and only if
\(T_\ell^{\mathcal G}(\operatorname{Ran}R_\ell)\subseteq\operatorname{Ran}R_{\ell+1}\).
Injectivity of \(J_{\ell+1}^{-1}\) and positivity of \(\Delta s_\ell\) reduce the
biconditional to the already established exact-image invariance criterion.

*Falsifier discharged.* On \(\mathbb R^2\) with \(b=e\), \(R(x,y)=(x,0)\) and
\(T(x,y)=(x,x)\): every retained input has \(\beta^{\mathrm{ret}}=(0,0)\) while
\(\beta^{\mathrm{ex}}=(0,x)\). Bounded idempotence is not closure.

*Scheme dependence.* Under \(J'_\ell=J_\ell S_\ell\),
\(\widehat T'_\ell=S_{\ell+1}^{-1}\widehat T_\ell S_\ell\); with
\(T_\ell=\operatorname{id}\), \(b_\ell=e\), and \(J_\ell u=a_\ell u\), the beta
is \((a_\ell/a_{\ell+1}-1)g\). Even an identity native step has a nonzero beta
in a moving comparison frame.

**Continuous tier.** A continuous beta is declared separately as
\(\beta^{\mathrm{scale}}(s)=\nabla^{\mathrm{scale}}_{\partial_s}g(s)\) on a
\(C^1\) Banach bundle over an oriented one-dimensional scale manifold, with the
frame law \(A'_s=S_sA_sS_s^{-1}-(\partial_sS_s)S_s^{-1}\); the trivial-line-bundle
witness \(S_s=e^{s^2}\) shows a raw coordinate derivative does not obey it. The
scale connection is explicitly distinguished from the two contextual principal
connections (different base and tangent type) and from the inference-orbit
parameter and Fisher duration. The pre-existing continuous semigroup density
formula is retained verbatim and is now introduced as one realization of this
separate tier. Discrete endpoints do not determine it: on the trivial line
bundle, \(\mathsf V^{(0)}(s,t)=1\) and
\(\mathsf V^{(\epsilon)}(s,t)=\exp\{\epsilon[\sin(2\pi s)-\sin(2\pi t)]\}\) both
satisfy the two-parameter law, agree at all integer endpoints, and have
generators \(0\) and \(2\pi\epsilon\cos(2\pi s)\).

### T11. Fixed objects and flows

*Source:* `def:rg-typed-fixed-objects`,
`prop:rg-fixed-object-nonimplication`, and the two closing prohibitions.

Invariant sections \(y_{\ell+1}=F_\ell(y_\ell)\) are the general objects and need
no identification. Reference fixed objects require
\(J_{\ell+1}^{-1}F_\ell J_\ell(y_\star)=y_\star\). Periodic identified sequences
give monodromy objects \(\mathcal M_\ell(y_\ell)=y_\ell\) with \(p\)-cycles.
Tiers are separated: normalized law and tracked measure pair; attention event
law; action relative to a reference and the additive action class; full
interaction coordinates; retained interaction coordinates; bundle state; and
configuration manifolds. No equality or subtraction is written across unequal
spaces or across tiers.

*Non-implication witnesses.* Fixed law does not fix a reference-dependent
action (alternate \(\rho_0=(1/4,3/4)\) and \(\rho_1=(3/4,1/4)\) at fixed
\(\mu=(1/2,1/2)\)). Fixed action class does not fix a tracked pair (masses
differ by \(e^{-c}\)). Fixed retained interaction does not fix the exact
interaction (the \(R,T\) witness of T10). Fixed law does not fix a configuration
(\(S^1\) with antipodal step and constant extraction). Fixed conditional
attention row does not fix the event law (alternating receiver occupancy). A
monodromy object is not a one-step fixed object (\(F_0(x)=x+1\),
\(F_1(x)=x-1\)).

*Two prohibitions recorded in the source.* Relevance is relative to declared
norms, extensive normalization, block ratios, and comparison maps. No fixed
object of any tier is identified with a physical law; that identification is
routed to the existing open problem `claim:physical-law-identification`, tagged
`NOT-CLAIMED`.

### T12. Lumpability and projection memory, proved rather than cited

*Source:* `thm:rg-strong-lumpability`, `thm:rg-projection-memory`,
`cor:rg-resolved-autonomy`.

**Strong lumpability, standard Borel.** If a coarse Markov kernel \(T^c\)
satisfies \(c_\#(\mu T)=(c_\#\mu)T^c\) for every probability \(\mu\), then
taking \(\mu=\delta_y\) gives \(T(y,c^{-1}B)=T^c(c(y),B)\), which both proves the
fiberwise-constancy criterion and makes \(T^c\) unique by surjectivity of \(c\).
Conversely, given the criterion and a Borel right inverse \(\varsigma\), the
formula \(T^c(z,B)=T(\varsigma(z),c^{-1}B)\) is a Markov kernel: countable
additivity follows because \(c^{-1}\) preserves disjoint countable unions and
\(c^{-1}\mathsf Z=\mathsf Y\), and measurability in \(z\) is the composition of
\(\varsigma\) with the measurable map \(y\mapsto T(y,c^{-1}B)\); the pushforward
identity then follows by integrating
\(T^c(c(y),B)=T(y,c^{-1}B)\). A Borel right inverse exists in the two cases the
chapter uses (countable coarse space; product projection with nonempty discarded
factor); otherwise the selection must be declared.

*Weak-lumpability witness.* \(\mathsf Y=\{1,2,3\}\), \(c(1)=c(2)=a\),
\(c(3)=\beta\), with \(1\mapsto3\) surely, \(2\mapsto\{1,2\}\) uniformly, and
\(3\mapsto\{1,3\}\) uniformly. Then \(T(1,\{1,2\})=0\ne1=T(2,\{1,2\})\), so strong
lumpability fails, yet started at \(\delta_3\) the chain stays in \(\{1,3\}\)
where \(c\) is injective, so the coarse process is Markov.

*Source scope.* Kemeny and Snell are cited only for the classical finite-state
criterion, at chapter granularity; the standard-Borel biconditional is proved
here.

**Projection memory.** With \(\Pi^{\mathrm{res}}=\mathsf P\mathsf C\),
\(\mathsf Q=I-\Pi^{\mathrm{res}}\), and \(w_n=\mathsf Cx_n\), applying the two
projections to \(x_{n+1}=Tx_n\) gives the coupled system
\(w_{n+1}=\mathsf{CTP}w_n+\mathsf{CTQ}(\mathsf Qx_n)\) and
\(\mathsf Qx_{n+1}=\mathsf{QTQ}(\mathsf Qx_n)+\mathsf{QTP}w_n\). Induction solves
the second, and substitution yields the exact closed recurrence
\[
w_{n+1}=\mathsf{CTP}w_n
+\sum_{k=0}^{n-1}\mathsf{CTQ}(\mathsf{QTQ})^{n-1-k}\mathsf{QTP}w_k
+\mathsf{CTQ}(\mathsf{QTQ})^{n}\mathsf Qx_0 .
\]
Autonomy on an admitted initial class is exactly vanishing of the total
correction. On the resolved class, \(\mathsf{QTP}=0\) is sufficient but not
necessary: with \(\mathsf X=\mathbb R^2\), \(\mathsf C(x,y)=x\),
\(\mathsf P(w)=(w,0)\), \(T(x,y)=(x,x)\), one has
\(\mathsf{QTP}w=(0,w)\ne0\) while \(\mathsf{CTQ}=0\), so all memory kernels
vanish and \(w_{n+1}=w_n\) exactly.

*Source scope.* Nakajima and Zwanzig are cited as the historical
projection-operator antecedent, in continuous time on ensemble densities, and
not as proofs of the displayed discrete recurrence.

## 5. Source applicability

**Jona-Lasinio 2001.** Metadata verified directly against the arXiv abstract
record on 2026-08-04: Giovanni Jona-Lasinio, "Renormalization Group and
Probability Theory", submitted 14 September 2000, arXiv `cond-mat/0009219`,
journal DOI `10.1016/S0370-1573(01)00042-4`, Physics Reports 352 (2001)
439--458. The bibliography entry now carries number, DOI, eprint, and archive
prefix.

The manuscript cites this source, at section granularity, for exactly four
items: the binary normalized-sum Gaussian/Hermite linearization with eigenvalues
\(2^{1-k/2}\) under normalization, centering, and variance constraints
(Section 2); the identification of the linearization at a self-similar Gaussian
fixed point with a conditional expectation, and the corresponding generalized
Hermite eigenvalue equation (Section 5); the two-tangent-space form of that
eigenvalue equation and its multiplicative composition law across scales
(Section 7); and the author's own statement that the nonlinear terms needed to
complete a limit theorem are not pursued there. Everything else is proved in the
manuscript: the arbitrary-integer-\(b\) theorem, the quadratic-mean realization,
the extensive Fisher budget, the exact spectrum including the status of \(0\),
the correlated and multivariate boundaries, and the typed cocycle and beta
apparatus.

*Recorded limitation.* Section-level rather than equation-level citation was
chosen deliberately. Equation-level anchors ((2.13)--(2.14), (5.10)--(5.11),
(7.2)--(7.5)) are recorded concordantly by two independent in-repository
records, `evidence/task-9-hermite-analysis.md` and
`docs/reviews/gauge-vfe-rg-deep-2026-08-02/REPORT.md`, but the primary PDF text
could not be opened in this environment (no PDF text extractor and no Python
execution available), so those finer anchors are not asserted in the manuscript.
The local vault note
`sources/papers/jona-lasinio-2001-renormalization-probability.md` describes the
spectrum as "proving the CLT as a stable-manifold theorem"; that phrasing is
stronger than the primary paper's stated scope and is not used. The vault note
is treated as a wiki record, not as authority.

**Kemeny and Snell 1976.** Cited only for the classical finite-state strong
lumpability criterion, at chapter granularity (Chapter 6, "Lumpability"),
publication metadata Springer, New York, 1976, Undergraduate Texts in
Mathematics, reprint of the 1960 Van Nostrand edition. No theorem number is
asserted. The standard-Borel biconditional the manuscript actually needs is
proved in `thm:rg-strong-lumpability`.

*Recorded limitation.* The chapter location was corroborated by a bibliographic
search that returned a course-hosted scan of the 1976 edition's Chapter 6.3--6.4
under the title "Kemeny, Snell 1976. Finite Markov Chains"; that scan could not
be fetched in this environment, and the physical text was not opened. The
citation is therefore deliberately coarse-grained to the chapter, and no
manuscript proof step depends on it.

**Nakajima 1958 and Zwanzig 1960.** Metadata: Progress of Theoretical Physics
20(6) 948--959, DOI `10.1143/PTP.20.948`; Journal of Chemical Physics 33(5)
1338--1341, DOI `10.1063/1.1731409`. Both are cited only as the historical
projection-operator antecedent. The discrete recurrence
`eq:rg-memory-recurrence` is proved here.

**Arnold 1998.** Random Dynamical Systems, Springer Monographs in Mathematics,
Springer, Berlin, 1998, ISBN 3-540-63758-3. Cited once, for the hypotheses of
the multiplicative ergodic theorem, inside a `NOT-CLAIMED` statement that
declines an Oseledets splitting for the RG cocycle.

No DOI, page range, quotation, or theorem number was invented. Where a
finer-grained anchor could not be checked in this environment, the citation was
coarsened rather than guessed.

## 6. Notation collisions resolved

The integration introduced no new glyph collision and removed one pre-existing
ambiguity.

* The score replication lift is \(\mathscr I_b\), explicitly distinguished from
  the Hoeffding assembly \(E_\ell\).
* The block conditional expectation reuses the chapter's existing \(U\) with a
  block subscript \(U_b\), so no new symbol competes with the retained
  projection \(R_\ell\).
* The score renormalization operator is \(\mathscr L_b\), in script font,
  distinguished from the ELBO \(\mathcal L\).
* The comparison trivialization is \(J_\ell:\mathcal G_\star\to\mathcal G_\ell\),
  declared as the inverse orientation of the pre-existing \(I_\ell\).
* The pulled exact map is \(\widehat T_\ell^{\mathcal G}\); \(R_\ell\) is not
  reused for it.
* The scale evolution family is \(\mathsf V(s,t)\), chosen because
  \(\mathcal U_\epsilon\) is already the bounded action chart.
* The scale connection is \(\nabla^{\mathrm{scale}}\), separated in the text and
  in the notation appendix from \(\omega_b,\omega_m\) and from Fisher duration.
* The resolved projection of the memory section was renamed
  \(\Pi^{\mathrm{res}}\), removing its pre-existing collision with the reverse
  kernel \(\Pi_\ell\) and the posterior \(\Pi_o\). The reverse conditional
  \(R_\rho\) of the reference measure now has its own notation-appendix row
  separating it from \(R_\ell\) and from the stochastic refinement kernel.

## 7. Mechanical control results

All checks were run read-only. The bibliography, whitespace, encoding, phrase,
brace-balance, and status bullets were run over the integration bytes and are
unaffected by the later repair, which touched one file and changed no character
outside four heading lines. The label and cross-reference bullets carry
LaTeX-semantic counts recomputed over the current bytes whose digests appear in
Section 3; section 7.1 records that recomputation and the audit that forced it.

* Banned spacing macros in the five owned TeX files: zero matches for
  `\,`, `\;`, `\!`.
* Checked British spellings in the five owned TeX files: zero matches.
* Non-ASCII characters in the five owned TeX files: zero. In
  `manuscripts/references.bib` the only non-ASCII characters are three
  pre-existing legitimate diacritics in two author names, at lines 1684, 2156,
  and 2178, namely a u-umlaut and two c-hacek characters; the entries added by
  this pass are ASCII, and no mojibake sequence is present.
* Banned phrase list from `SPEC.md` section 1 in the five owned TeX files: zero
  matches.
* Brace balance and environment nesting across each owned TeX file: final depth
  zero, minimum depth zero, empty environment stack, no mismatched `\end`.
* Label inventory across all twenty-four manuscript TeX files, counting both
  explicit `\label` and heading-generated labels: **1201** unique labels, of
  which 260 are generated by heading macros and 941 are written as explicit
  `\label`; zero duplicates.
* Cross-reference resolution across the same files: **557** unique
  `\Cref`/`\ref`/`\eqref` targets over 1064 reference sites, zero unresolved.

  Both figures are LaTeX-semantic counts, produced by the heading-arity-aware
  scanner specified in section 7.1 and given verbatim in
  `evidence/task-9-heading-repair.md`. The figures first published in this record,
  1212 labels and 557 targets with zero unresolved, came from a string-level
  scan and are **withdrawn**. That scan resolved reference keys against the
  literal text `\label{...}` and `heading{...}{...}`, which is not what TeX
  defines: it credited four labels that TeX never defines, and it counted eleven
  keys that are not labels at all (`#4`, plus the ten counter names, all read out
  of the `\newcommand` bodies in `main.tex`). Section 7.1 records the audit that
  falsified it, the repair, and the replacement check. The string-level scan
  returns the identical numbers before and after that repair, so it could not
  have detected the defect in either direction.
* Bibliography: 464 unique keys, zero duplicates; 79 cited keys, zero missing.
  The four keys added by this pass are `KemenySnell1976`, `Nakajima1958`,
  `Zwanzig1960`, `Arnold1998`; `JonaLasinio2001` was already present, was
  previously uncited, and is now cited and enriched with number, DOI, eprint,
  and archive prefix.
* Whitespace: zero blank-at-EOL, zero space-before-tab, zero tabs, zero
  blank-at-EOF across the five owned TeX files and `references.bib`.
* Multiple `\status` tags on one physical line: none introduced by this pass.
  Three pre-existing occurrences remain in `08_infogeometry.tex` inside the
  unmodified `sec:ig-notclaimed` paragraphs, where each tag scopes a distinct
  sentence-level claim; they are line-length artifacts of long single-line
  paragraphs and belong to the Task 11 status sweep.

*Recorded limitation, since discharged.* `git diff --check` could not be executed
in the integration environment: Git invocation was gated there. The three
whitespace classes that command reports under Git's default configuration
(blank-at-eol, space-before-tab, blank-at-eof) were instead checked directly over
the modified files, with the zero results above. Read-only Git was available in
the later audit and repair environments, where `git diff --check` was executed
and exited `0`; see section 7.1. No TeX build was run at any point and none is
claimed.

### 7.1 Independent FAIL audit, the four-line heading repair, and the replacement check

This subsection is later than the rest of the record. It documents an
independent audit that **falsified** the reference-resolution claim published
above, and the repair that followed.

**The audit.** Two independent reports were produced against the integration
bytes, and neither is edited by this pass; they stand as the historical
falsification evidence.

| Report | SHA-256 | Verdict |
| --- | --- | --- |
| `evidence/task-9-opus-adversarial.md` | `75fb7674319a0a20f338c648669ab148ae20f4c7186bbe6ab8808744415f97fe` | **FAIL** on one blocker, B-1; **no mathematical blocker** |
| `evidence/task-9-static-proof-control.md` | `f7045145725357ccb1eb52f0358e27e7c48b2fc47b3ad000ebdfcc53218ec5c9` | **FAIL** on one check, SC-5; nine of ten checks pass |

The audit reproduced every load-bearing derivation of obligations 1 through 9
independently and defeated each attempted counterexample, so sections 4 and 5 of
this record are untouched. Its non-blocking findings N-1 through N-6 are
likewise untouched and remain open exactly as recorded there; N-5 concerns a
characterization in this record's status-tag bullet above, whose repair the audit
assigns to the Task 11 status sweep.

**B-1, the defect.** `main.tex:86-100` defines every result heading through

```latex
\newcommand{\resultheading}[4]{%
  \syncstatementcounter{#2}%
  \label{#4}%
  \paragraph{#1~\csname the#2\endcsname\ (#3).}%
}
\newcommand{\propositionheading}[2]{\resultheading{Proposition}{proposition}{#1}{#2}}
```

so each wrapper takes **two** mandatory arguments and emits the second as the
label key. Four call sites in `07b_agent_network_rg.tex` supplied only the title
group and put `\label{key}` on the following line. TeX scans an undelimited
argument by skipping spaces, including the end-of-line, and taking the next
token; that token is the control sequence `\label` itself. So `#2` became
`\label`, the body expanded to `\label{\label}`, the intended key was never
passed to `\label`, and the trailing brace group was typeset as body text. Four
labels were therefore undefined and six `\Cref` sites unresolved. No
`\renewcommand`, `\providecommand`, or `\DeclareRobustCommand` anywhere in the
directory touches these macros.

**The repair.** Four line joins, no prose change, exactly as the audit's minimal
repair prescribes. Each malformed two-line construct became one call with both
mandatory arguments as brace groups:

```latex
% 07b:259-260   -> 259
\propositionheading{Bounded recentering gives analyticity at every bounded action}{prop:rg-action-bounded-recentering}
% 07b:1109-1110 -> 1108
\propositionheading{Product equivalence is an admitted, not an automatic, scale premise}{prop:rg-product-equivalence-not-preserved}
% 07b:1174-1175 -> 1172
\theoremheading{Hoeffding assembly is an exact finite-network action isomorphism}{thm:rg-hoeffding-action-isomorphism}
% 07b:1243-1244 -> 1240
\propositionheading{Radon--Nikodym covariance of the nonlinear interaction step}{prop:rg-interaction-rn-gauge-covariance}
```

The file lost 32 bytes and four physical lines, CRLF endings and the trailing
newline are preserved, and `git diff --numstat` moved from `1062 25` to
`1066 33` against `HEAD`, which is exactly four lines added and eight removed.

**The replacement check.** The string-level scan is retired for this obligation
and replaced by a scanner that models TeX argument scanning: a control word is a
backslash followed by letters; before each mandatory argument the scanner skips
space tokens, a single end-of-line, and percent-comments, and treats a blank line
as `\par`; a mandatory argument is the next **brace group**, and otherwise the
single next token; and `\newcommand`-family bodies are skipped wholesale, so
macro definitions are never mistaken for call sites. A heading call passes only
when every mandatory argument is a brace group, and only then does its last
argument enter the defined-label set. The scanner source is given verbatim in
`evidence/task-9-heading-repair.md`.

| Quantity, all 24 manuscript TeX files | Before repair | After repair |
| --- | --- | --- |
| Heading call sites scanned | 260 | 260 |
| Calls with both mandatory arguments as brace groups | 256 | **260** |
| Malformed heading calls | **4** | **0** |
| Unique labels defined at LaTeX semantics | 1197 | **1201** |
| Duplicate labels | 0 | 0 |
| Unique reference targets | 557 | 557 |
| Unresolved reference targets | **3 keys over 6 sites** | **0** |
| Scanner errors | 0 | 0 |
| Verdict | **FAIL** | **PASS** |

The four repaired keys are now defined by their heading macros at `07b:259`,
`1108`, `1172`, and `1240`. The fourth,
`prop:rg-product-equivalence-not-preserved`, had no reference site, which is why
four undefined labels produced only three unresolved keys.

**Why the original check was blind.** Run over the same 24 files, the
string-level scan reports 1212 labels, 557 targets, and zero unresolved both
before and after the repair; the two label sets are byte-identical. Its 1212
decomposes exactly as `1201` semantic labels, plus eleven non-labels read out of
`main.tex` (`#4` from the `\label{#4}` in `\resultheading`'s own body, and the ten
counter names `definition`, `lemma`, `proposition`, `theorem`, `corollary`,
`conjecture`, `openproblem`, `hypothesis`, `construction`, `requirement`, taken
as second groups of the wrapper definitions). Before the repair it also credited
the four keys TeX never defines; `1197 + 11 + 4 = 1212`, and after the repair
`1201 + 11 = 1212`. String coincidence, not LaTeX semantics, is what made the
obligation appear closed.

**Scope of the repair pass.** Only `07b_agent_network_rg.tex` and the evidence and
control records were touched. No file under `.verification/` and no
`manuscripts/gauge_vfe_rg/verification/current-results.json` was modified; their
digests are unchanged. `git diff --check` exits `0`. No TeX build was run, so B-1
rests on the macro arity quoted above and on standard TeX undelimited-argument
scanning, as the audit itself records. The full control transcript, including
the pre- and post-repair digests, the JSON parse results, and the bibliography
and scope checks, is `evidence/task-9-heading-repair.md`; that artifact binds
this record by digest, so this record deliberately cites it by path only and no
circular hash dependency is created.

### Verification control-plane drift, reported and not silenced

A separate control plane, the verification-skill session, is active and has
drifted. Its activation marker `.verification/active.json` pins
`.verification/task3-factorization-closure-ledger.json` to

```text
git:bcc80a032ea761669bdcb244ed51f5d8380b6c05:sha256:bf6b86ab39de748ccb7bdbb8021df799fbac70b70f5454fdc81b65496be27de7
```

and the Stop hook reports, verbatim,
`live artifact changed after verification activation`.

That pin covers the Git index together with every tracked and non-ignored
untracked path, so any uncommitted edit invalidates it. The drift is real and
predates this pass. The activation marker is timestamped 2026-08-03, the branch
has since advanced to `3dbe4c6` with the Task 5 through Task 8 commits landing
after activation, and the three untracked Task 9 analyses were written after it
as well. This pass adds further drift, as any edit necessarily would.

The consequence is confined to that ledger: at this worktree state the Task 3
factorization-closure ledger may close nothing, its claims are `INCONCLUSIVE`,
and the open obligation is to re-verify at a current artifact revision. This
pass did not silence the alarm and must not: no file under `.verification/` was
created, deleted, moved, re-pinned, or edited; no `artifact_revision` was
recomputed; and no activation was restarted. The alarm is the finding.

The two control planes are separate and neither substitutes for the other. The
Task 9 closures recorded here belong to the rigorous-theory-search run package
under `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/`, whose binding
discipline is the frozen contract identifier, the target digest, and
recomputation of every evidence artifact digest. That discipline was checked
independently and holds: all nineteen recorded evidence digests match current
bytes. Drift of the verification-skill pin neither certifies nor decertifies
those closures, and the rigorous-theory-search binding does not discharge the
verification-skill obligation.

*Recorded limitation.* The validator
`verification_gate.py validate .verification/task3-factorization-closure-ledger.json`
could not be executed here because Python invocation is gated, so the hook's
verbatim message is reported as the finding rather than a validator transcript.

## 8. Scoped search-prior isolation

This is a scoped check over the Task 9 claims only. It does not discharge the
run-level oracle erasure, which remains scheduled before any terminal release
and is recorded as not run in `adversarial-report.json`.

The affirmative-existence instruction is carried only as
`SEARCH_PRIOR_AFFIRMATIVE` in `problem-contract.target.search_priors`. Each
Task 9 theorem was rechecked against the frozen assumptions for direct or
paraphrased dependence on that prior. None was found: every displayed proof
runs from the declared hypotheses, and the four results that could most easily
have been inflated by a desire for a positive answer are instead fenced.
Specifically, the relevance trichotomy is stated as a definition relative to
declared data rather than as an intrinsic property; the Gaussian spectrum is
accompanied by four exact boundaries that delimit it; the mode exponents are
defined rather than asserted to exist, with the Oseledets route explicitly
declined; and the retained beta is exact only under a proved invariance
condition, with the residual reported otherwise. Two source anchors were
coarsened rather than asserted at a granularity that could not be checked.
Passing this scoped check shows only that the prior was unnecessary for the
Task 9 construction; it proves no theorem.

## 9. Residual obligations

The following remain open and are recorded in `appendix_claim_ledger.tex`:
extensive relevance beyond the scalar independent Gaussian realization;
nonlinear attraction at the Gaussian tangent; multiplicative ergodic structure
for the interaction cocycle; canonical smooth scale tier and continuous beta;
and existence of a nontrivial invariant retained subspace. Task 10 claims
(bundle Fisher defect, pullback compatibility, configuration geometry, history
semiconjugacy, noncollapse, and duration) are untouched by this pass and remain
`CANDIDATE`.

## 10. Falsification conditions for this record

This record becomes stale if any byte of the six sources in Section 3 changes.
It is refuted by any of the following: a centered square-integrable score for
which the displayed quadratic path fails to normalize or to be two-sided; an
independent block lift whose Fisher information differs from
\(b\lVert h\rVert_2^2\); a normalized parameter-independent channel violating
the extensive conditional-variance budget; a Hermite index for which the Mehler
regression identity or the eigenvalue \(b^{1-k/2}\) fails; a nonzero element of
\(\ker\mathscr L_b\), or a proof that \(0\) is an eigenvalue; a Hermite degree
whose exponential normalizer contradicts the four-case domain classification; a
composable segment for which ordered derivative composition or the mode product
law fails; a tempered pair of trivializations that nevertheless changes an
exponent; a retained projection with zero residual whose exact image leaves the
retained range, or a nonzero residual reported as exact; a reference change
whose action beta transforms without the displayed inhomogeneous term; a
subtraction or equality written across unequal spaces; a fixed object of one
tier asserted to force fixedness in another; a lumpable-for-every-initial-law
kernel violating fiberwise constancy, or a fiberwise-constant kernel with a
Borel section for which the displayed coarse kernel fails the pushforward
identity; a projection-memory instance contradicting the closed recurrence; or a
primary-source check showing that Jona-Lasinio, Kemeny and Snell, Nakajima,
Zwanzig, or Arnold does not support the narrowed scope attributed to it here.
