<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 9, route B: Gaussian/Hermite block renormalization

## Result and scope

For every integer block size \(b\geq 2\), the linearized normalized-sum map on the real normalized Gaussian score tangent
\[
\mathsf H:=L^2_0(\gamma;\mathbb R),\qquad \gamma=N(0,1),
\]
is the bounded operator
\[
\mathcal L_b=\mathcal R_b\mathcal E_b:\mathsf H\longrightarrow\mathsf H,
\]
where
\[
(\mathcal E_bh)(x_1,\ldots,x_b)=\sum_{i=1}^b h(x_i),
\qquad
(\mathcal R_bF)(z)=\mathbb E_{\gamma^{\otimes b}}[F(X_1,\ldots,X_b)\mid Z=z],
\]
and \(Z=b^{-1/2}\sum_iX_i\).  In the normalized probabilists' Hermite basis
\[
e_k(x)=\frac{\operatorname{He}_k(x)}{\sqrt{k!}},\qquad k\geq1,
\]
one has exactly
\[
\boxed{\mathcal L_b e_k=b^{1-k/2}e_k.}
\]
Consequently
\[
\sigma(\mathcal L_b)=\{b^{1-k/2}:k\geq1\}\cup\{0\}.
\]
Every displayed nonzero spectral value is a simple eigenvalue.  The point \(0\) is **not** an eigenvalue: it is the unique spectral accumulation point (and lies in the continuous spectrum).  This theorem is a linear tangent-space statement.  It is not, without additional nonlinear estimates, a global convergence theorem for probability laws.

## 1. The normalized Gaussian score tangent is not merely formal

A differentiable-in-quadratic-mean path through \(\gamma\) has score \(h\) when
\[
\sqrt{\frac{d\mu_t}{d\gamma}}=1+\frac t2h+o_{L^2(\gamma)}(t).
\]
Normalization forces \(\mathbb E_\gamma h=0\), and the Fisher norm is \(\|h\|_{L^2(\gamma)}\).  Conversely, every \(h\in\mathsf H\), including an unbounded Hermite polynomial, is realized by the nonnegative normalized path
\[
\frac{d\mu_t^h}{d\gamma}
=\frac{(1+t h/2)^2}{1+t^2\|h\|_2^2/4}.
\]
Indeed, the denominator is the integral of the numerator because \(\mathbb E h=0\).  Put \(a_t=1+th/2\) and \(c_t=(1+t^2\|h\|_2^2/4)^{-1/2}\).  Then
\[
\|c_t|a_t|-1-th/2\|_2
\leq |c_t-1|\,\||a_t|\|_2+\||a_t|-a_t\|_2.
\]
The first term is \(O(t^2)\).  After division by \(|t|\), the second is bounded by an \(L^2\)-tail of \(|h|\), supported on \(\{|h|>2/|t|\}\), and therefore tends to zero.  Thus the full Hilbert space \(L^2_0(\gamma)\), rather than only bounded scores, is the correct DQM tangent used below.

This distinction is load-bearing.  Hermite polynomials are unbounded, so the spectrum below does not live in a bounded-density or \(L^\infty\) chart unless that chart is enlarged or a different local model is specified.

## 2. Typed block maps

Let
\[
\mathsf H_b=L^2_0(\gamma^{\otimes b};\mathbb R).
\]
The replication map and block-statistic score map have types
\[
\mathcal E_b:\mathsf H\to\mathsf H_b,
\qquad
\mathcal R_b:\mathsf H_b\to\mathsf H.
\]
For independent centered coordinates,
\[
\|\mathcal E_bh\|^2
=\mathbb E\!\left[\left(\sum_i h(X_i)\right)^2\right]
=b\|h\|^2,
\]
so \(\|\mathcal E_b\|=\sqrt b\).  Conditional expectation is an orthogonal projection followed by the isometric identification of \(Z\sim\gamma\), hence \(\|\mathcal R_b\|\leq1\).  It also preserves zero mean.  Therefore
\[
\mathcal L_b:=\mathcal R_b\mathcal E_b:\mathsf H\to\mathsf H,
\qquad \|\mathcal L_b\|\leq\sqrt b,
\]
is a well-defined bounded operator.

The probabilistic linearization is exact at DQM order: the product path \((\mu_t^h)^{\otimes b}\) has product score \(\sum_i h(X_i)=\mathcal E_bh\), and pushing it forward through the parameter-independent statistic \(Z\) gives the conditional score \(\mathbb E[\mathcal E_bh\mid Z]=\mathcal L_bh\).  No observation channel, interaction term, or gauge identification enters this scalar iid theorem.

## 3. Hermite diagonalization for every integer \(b\geq2\)

Use the probabilists' generating function
\[
\exp(tx-t^2/2)=\sum_{k=0}^{\infty}\operatorname{He}_k(x)\frac{t^k}{k!}.
\]
The functions \(e_k=\operatorname{He}_k/\sqrt{k!}\) form a complete orthonormal basis of \(L^2(\gamma)\); deleting \(e_0=1\) gives a complete orthonormal basis of \(\mathsf H\).

For each \(i\), \((X_i,Z)\) is a jointly standard Gaussian pair with correlation \(b^{-1/2}\).  Equivalently,
\[
X_i\mid Z=z\sim N\!\left(\frac z{\sqrt b},1-\frac1b\right).
\]
Taking the conditional expectation of the generating function gives
\[
\begin{aligned}
\mathbb E[\exp(tX_i-t^2/2)\mid Z=z]
&=\exp\!\left(\frac{tz}{\sqrt b}-\frac{t^2}{2b}\right)\\
&=\sum_{k=0}^{\infty}\operatorname{He}_k(z)
   \frac{(t/\sqrt b)^k}{k!}.
\end{aligned}
\]
Coefficient comparison yields the Mehler regression identity
\[
\mathbb E[\operatorname{He}_k(X_i)\mid Z]
=b^{-k/2}\operatorname{He}_k(Z).
\]
Summing over the \(b\) replicated coordinates proves
\[
\mathcal L_b e_k
=\sum_{i=1}^b\mathbb E[e_k(X_i)\mid Z]
=b^{1-k/2}e_k,
\qquad k\geq1.
\]
This proof works uniformly for every integer \(b\geq2\); it is not an induction from the binary case.

## 4. Completeness and exact spectrum

For \(h=\sum_{k\geq1}h_ke_k\in\mathsf H\), boundedness plus completeness of the Hermite basis gives
\[
\mathcal L_bh=\sum_{k\geq1}\lambda_kh_ke_k,
\qquad \lambda_k=b^{1-k/2}.
\]
Thus \(\mathcal L_b\) is a real self-adjoint positive diagonal operator.  Since \(\lambda_k\to0\), it is compact; in fact it is Hilbert--Schmidt because
\[
\sum_{k\geq1}\lambda_k^2
=\sum_{k\geq1}b^{2-k}=\frac{b^2}{b-1}<\infty.
\]
Its operator norm and spectral radius are \(\sqrt b\).

The diagonal-operator spectral theorem now gives
\[
\sigma(\mathcal L_b)=\overline{\{\lambda_k:k\geq1\}}
=\{b^{1-k/2}:k\geq1\}\cup\{0\}.
\]
The eigenvalues are distinct and each has multiplicity one.  Because every \(\lambda_k>0\),
\[
\ker\mathcal L_b=\{0\},
\]
so \(0\) is not an eigenvalue.  Finite Hermite expansions belong to the range, making the range dense.  The range is not all of \(\mathsf H\): the vector
\[
y=\sum_{k\geq1}\lambda_ke_k
\]
belongs to \(\mathsf H\), but a preimage would have every Hermite coefficient equal to \(1\), which is not square summable.  Hence \(0\) lies in the continuous spectrum and is precisely the spectral accumulation point.

The Hilbert--Schmidt sum above is \(b^2/(b-1)\); for example, at \(b=2\) it is \(2+1+1/2+\cdots=4\).

## 5. Relevance classes under the stated normalization

With the replication **sum** \(\mathcal E_bh=\sum_i h(x_i)\), normalized block variable \(Z=b^{-1/2}\sum_iX_i\), and the same Fisher \(L^2(\gamma)\) norm at every scale:

| Hermite degree | eigenvalue | exponent \(y_k=\log_b\lambda_k\) | class |
|---:|---:|---:|---|
| \(k=1\) | \(\sqrt b\) | \(1/2\) | relevant |
| \(k=2\) | \(1\) | \(0\) | marginal |
| \(k\geq3\) | \(b^{1-k/2}<1\) | \(1-k/2<0\) | irrelevant |

The constant mode \(k=0\) would have eigenvalue \(b\) on full \(L^2(\gamma)\), but it is absent from the normalized probability tangent because scores have zero mean.  If the RG chart additionally fixes mean and variance, the \(k=1\) and \(k=2\) coefficients are constrained to vanish; only the contracting \(k\geq3\) sector remains.  Therefore "the Gaussian fixed point is linearly attractive" is true only on that constrained tangent, not on all normalized score perturbations.

These classifications are convention-dependent.  Replacing the replication sum by an average, changing the block normalization, or inserting an additional field-amplitude rescaling multiplies the spectrum and changes the reported relevance exponents.  Any manuscript theorem must state these conventions adjacent to the eigenvalues.

## 6. Falsifiers and forbidden overextensions

1. **Correlated inputs change the spectrum.**  Let the scalar \(X_i\) be standard Gaussian with common pairwise correlation \(\rho>-1/(b-1)\), and normalize
   \[
   Z=\frac{\sum_iX_i}{\sqrt{b[1+(b-1)\rho]}}.
   \]
   Then \(\operatorname{Corr}(X_i,Z)=a=\sqrt{[1+(b-1)\rho]/b}\), so
   \[
   \mathcal L_{b,\rho}e_k=ba^ke_k
   =b^{1-k/2}[1+(b-1)\rho]^{k/2}e_k.
   \]
   For \(\rho\ne0\) this falsifies the iid eigenvalue formula.  Keeping \(b^{-1/2}\sum_iX_i\) instead does not repair it, because the output no longer has law \(\gamma\).

2. **The multivariate extension has degeneracies.**  For iid \(N(0,I_d)\) inputs and componentwise normalized sums, tensor Hermites \(e_\alpha\) satisfy
   \[
   \mathcal L_b e_\alpha=b^{1-|\alpha|/2}e_\alpha.
   \]
   Degree \(k\) has multiplicity \(\binom{d+k-1}{k}\), not one.  An iid \(N(0,\Sigma)\) version can be obtained after a declared whitening/transport identification.  Cross-agent covariance, nonidentical covariances, or a non-Gaussian reference invalidates the displayed scalar proof.

3. **Gauge covariance does not follow from the scalar result.**  In the isotropic multivariate case, a common orthogonal action commutes with the normalized-sum map, and degree spaces are invariant, while individual tensor Hermites mix within a degree.  A general \(GL(d)\) transformation does not preserve the fixed standard Gaussian or its fixed Fisher norm; it changes the covariance and requires an explicitly transported family of laws and tangent metrics.  Gauge links, headwise actions, curvature, and holonomy are absent from this theorem.  Describing scalar Hermites as general \(GL(d)\) irreducibles would be false; even under \(O(d)\), fixed-degree polynomial spaces have trace/harmonic decompositions.

4. **Replication is a restricted tangent direction.**  \(\mathcal E_bh=\sum_i h(X_i)\) is the score of an iid product perturbation.  It is not a theorem about every element of \(L^2_0(\gamma^{\otimes b})\), interaction scores, or higher-order Hoeffding sectors.

5. **Linearization is not nonlinear convergence.**  The spectrum controls the derivative at the Gaussian fixed point.  It does not alone establish a basin of attraction, control nonlinear remainders, or prove convergence at a marginal direction.

Concrete falsification tests are therefore: alter \(\rho\) and recover the correlated eigenvalue above; change sum to average and observe the extra factor \(b^{-1}\); include constants and recover the \(b\) eigenvalue; or claim a nonzero vector in the kernel, which contradicts the complete positive diagonal.

## 7. Primary-source attribution audit

### What the Jona-Lasinio paper supports

The primary record is:

- Giovanni Jona-Lasinio, "Renormalization Group and Probability Theory," *Physics Reports* **352** (2001), 439--458.
- DOI: `10.1016/S0370-1573(01)00042-4`.
- arXiv: `cond-mat/0009219`, submitted September 14, 2000: <https://arxiv.org/abs/cond-mat/0009219>.
- Primary PDF: <https://arxiv.org/pdf/cond-mat/0009219>.

The paper's Section II defines the **binary** normalized sum and its distributional RG in equations (2.2)--(2.3).  Around a centered unit-variance Gaussian it writes a perturbation with normalization, centering, and variance constraints, derives the linearized operator (2.13), and states the Hermite eigenvalues
\[
\lambda_k=2^{1-k/2}
\]
in equation (2.14).  It then states that the constrained \(k>2\) modes contract.  In Section V, equation (5.10) identifies the linearization for self-similar random fields with conditional expectation, followed by a generalized Hermite eigen-equation (5.11).  Section VII, equations (7.2)--(7.5), gives the conditional-expectation/tangent-space composition and generalized eigen-cocycle viewpoint.

The source therefore supports attribution of the binary Gaussian/Hermite linearization, the conditional-expectation formulation, and the generalized tangent-space viewpoint.  It does **not** explicitly prove the arbitrary-integer-\(b\) theorem, the DQM realization above, the exact compact-operator spectrum including the status of \(0\), the correlated counterexample, or a gauge-covariant extension.  Those are derivations in this evidence note.

The paper also says immediately after the linear analysis that nonlinear terms are required to complete the central-limit proof and are not pursued there.  Thus it must not be cited as proving nonlinear global attraction in the generality of this task.

### Local Research-vault record

`sources/papers/jona-lasinio-2001-renormalization-probability.md` correctly records the title, author, journal, pages, year, arXiv identifier, binary transformation, and eigenvalue formula.  Its phrase that the spectrum is obtained "proving the CLT as a stable-manifold theorem" is stronger than the primary paper's stated scope: the cited paper explicitly stops short of the nonlinear remainder analysis needed for such a proof.  The shared `manuscripts/references.bib` contains the journal metadata but presently omits the DOI and arXiv identifier.  A precise manuscript citation should use the metadata above and limit the attributed claim to what the paper actually establishes.

### Lumpability and projection-memory sources

These named frameworks are genuinely invoked elsewhere in the current manuscript, but not in the Gaussian/Hermite proof:

- `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:1355-1366` states the strong-lumpability criterion: transition probabilities into every coarse cell are constant within each fine block, with weak-lumpability exceptions for selected initial laws.
- `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:1368-1388` uses the discrete projection-memory operators \(\mathcal C\mathcal T\mathcal Q(\mathcal Q\mathcal T\mathcal Q)^n\mathcal Q\mathcal T\mathcal P\), together with an unresolved-initial-state term, to characterize exact autonomous closure.

No Kemeny--Snell or Nakajima--Zwanzig primary-source record or BibTeX entry was found in the local Research wiki/manuscript bibliography, and the Jona-Lasinio paper does not supply those attributions.  This is a separate source gap; neither framework should be cited as evidence for the Hermite theorem.  The exact historical/primary citations should be added only when those manuscript statements are sourced and checked on their own terms.

## Verdict

**PASS for the scalar iid tangent theorem, with the conventions and scope above.**  The complete integer-block derivation, exact spectrum, relevance classification, and falsifiers are established.  Any claim extending it to nonlinear global RG flow, correlated agents, unrestricted multivariate covariance, or a general gauge bundle remains unproved unless additional hypotheses and transport operators are supplied.
