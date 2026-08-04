<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 9 independent DQM score and action-interface derivation

## Scope and source snapshot

This is an independent derivation of the score tier. It does not assume an
exponential-action representation for an arbitrary score and does not import
the proposed Hermite RG spectrum. Its source snapshot is:

- 07b_agent_network_rg.tex:
  902E6ECF583CF084ADDCCDB3E84A265CFC8EEF5D4BA3BD3749E533295E6BD95C
- 08_infogeometry.tex:
  0B91582CAE8E540C96E89CCD4AFAF591A3882998F26D7C493F62280688CA3BDC

All probability spaces below are completed only after the displayed
equivalence-class statements are made. A Markov channel is fixed and
parameter independent.

## Lemma 1: every centered square-integrable score has a two-sided DQM path

Let \((\mathsf X,\mathscr X,\pi)\) be a probability space and let
\[
h\in L^2_0(\pi)
:=\left\{f\in L^2(\pi):\int f\,d\pi=0\right\}.
\]
Set \(a=\|h\|_2^2/4\). For every \(t\in\mathbb R\), define
\[
p_t(x)
=\frac{(1+t h(x)/2)^2}{1+a t^2},
\qquad
\pi_t(dx)=p_t(x)\pi(dx).
\]
Then \(\pi_t\) is a probability law for every positive and negative \(t\),
\(\pi_0=\pi\), and the path is differentiable in quadratic mean at zero with
score \(h\):
\[
\left\|
\sqrt{p_t}-1-\frac t2h
\right\|_{L^2(\pi)}
=o(|t|).
\]

### Proof

Centering gives
\[
\int(1+t h/2)^2\,d\pi
=1+t\pi(h)+\frac{t^2}{4}\pi(h^2)
=1+a t^2,
\]
so \(p_t\ge0\) and integrates to one. Put \(s_t=1+t h/2\) and
\(N_t=1+a t^2\). Then
\[
\sqrt{p_t}-s_t
=\frac{|s_t|-s_t}{\sqrt{N_t}}
+s_t\left(\frac1{\sqrt{N_t}}-1\right).
\]
On \(A_t=\{s_t<0\}\), one has \(|h|>2/|t|\) and
\(|s_t|-s_t=2|s_t|\le |t h|\). Hence
\[
\frac1{t^2}
\left\|
\frac{|s_t|-s_t}{\sqrt{N_t}}
\right\|_2^2
\le
\int h^2\mathbf1_{\{|h|>2/|t|\}}\,d\pi
\longrightarrow0
\]
by integrability of \(h^2\). For the normalization term,
\[
\left\|
s_t\left(N_t^{-1/2}-1\right)
\right\|_2
=|1-\sqrt{N_t}|=O(t^2).
\]
The two bounds prove the DQM expansion from either sign of \(t\). Thus every
\(h\in L^2_0(\pi)\), bounded or unbounded, is an actual two-sided score. No
moment-generating function or exponential integrability is required.

### Falsifier

Any claim that the ambient DQM tangent set is only the set of bounded scores
is false. For \(\pi=N(0,1)\), \(h(x)=x\) is unbounded and belongs to
\(L^2_0(\pi)\); the construction above realizes it two-sided.

## Lemma 2: iid blocking gives the additive score with exact norm

Fix an integer \(b\ge1\). Let \(\pi_t\) be any DQM path at \(\pi\) with
score \(h\in L^2_0(\pi)\), and form the iid product path
\(\Pi_t=\pi_t^{\otimes b}\) at
\(\Pi=\pi^{\otimes b}\). Then \(\Pi_t\) is DQM with score
\[
(E_bh)(x_1,\ldots,x_b)
=\sum_{i=1}^b h(x_i).
\]
The score lift is a bounded linear map
\[
E_b:L^2_0(\pi)\longrightarrow L^2_0(\Pi),
\qquad
\|E_bh\|_{L^2(\Pi)}^2=b\|h\|_{L^2(\pi)}^2.
\]
Thus \(\|E_b\|=\sqrt b\), while \(b^{-1/2}E_b\) is an isometry.

### Proof

Write the one-coordinate Hellinger amplitude as
\[
r_t=1+\frac t2h+t\varepsilon_t,
\qquad \|\varepsilon_t\|_2\to0.
\]
The product amplitude is \(\prod_{i=1}^b r_t(x_i)\). Expanding this finite
product in \(L^2(\Pi)\) gives
\[
\prod_{i=1}^b r_t(x_i)
=1+\frac t2\sum_{i=1}^bh(x_i)+o_{L^2(\Pi)}(|t|).
\]
Indeed, every first-order error has norm
\(|t|\|\varepsilon_t\|_2\), and every term involving at least two
first-order factors is \(O(t^2)\); tensor-product \(L^2\) norms factor.
This proves the DQM statement. Independence and centering give
\[
\mathbb E_\Pi(E_bh)=0,\qquad
\mathbb E_\Pi(E_bh)^2
=\sum_i\mathbb E h(X_i)^2
+\sum_{i\ne j}\mathbb Eh(X_i)\mathbb Eh(X_j)
=b\|h\|_2^2.
\]

### Falsifier

The iid score is the sum, not the arithmetic mean. Replacing \(E_bh\) by
\(b^{-1}\sum_i h(X_i)\) without simultaneously rescaling the path parameter
changes Fisher information from \(b\|h\|_2^2\) to
\(\|h\|_2^2/b\).

## Lemma 3: a fixed coarse channel pushes the score by conditional expectation

Let
\[
C:\mathsf X^b\rightsquigarrow\mathsf Z
\]
be a parameter-independent Markov kernel. Form
\[
J(dx,dz)=\Pi(dx)C(x,dz),
\qquad
\Pi^c=\Pi C.
\]
For \(s\in L^2(\Pi)\), let
\[
(Rs)(z)=\mathbb E_J[s(X)\mid Z=z].
\]
Then \(R:L^2(\Pi)\to L^2(\Pi^c)\) is the orthogonal conditional-expectation
contraction. The pushed path \(\Pi_tC\) is DQM at \(\Pi^c\), and its score is
\[
L_bh:=RE_bh
=\mathbb E_J\!\left[
\sum_{i=1}^bh(X_i)\,\middle|\,Z
\right].
\]
Consequently
\[
L_b:L^2_0(\pi)\longrightarrow L^2_0(\Pi^c),
\qquad
\|L_b\|\le\sqrt b.
\]
The normalized score RG
\(\widetilde L_b=b^{-1/2}L_b\) is a contraction.

### Proof from Hellinger contraction

First suppose \(h\) is bounded and use the canonical path of Lemma 1. For
small \(|t|\), its one-coordinate Hellinger amplitude has no sign change,
and the block likelihood has the uniform expansion
\[
\frac{d\Pi_t}{d\Pi}
=1+tE_bh+O(t^2).
\]
Conditional integration gives
\[
\frac{d(\Pi_tC)}{d\Pi^c}
=1+tR(E_bh)+O(t^2),
\]
and the square-root Taylor expansion proves DQM with score \(RE_bh\).
Every other DQM path with the same score is \(o(|t|)\) away from this
canonical path in Hellinger norm. Hellinger contraction makes their pushed
paths \(o(|t|)\) apart, so they have the same pushed score.

For general \(h\in L^2_0(\pi)\), choose bounded centered \(h_n\to h\) in
\(L^2(\pi)\), and let \(\Pi_{t,n}\) be the products of their canonical
Lemma 1 paths. The squared Hellinger distance contracts under a Markov
kernel. One direct proof writes output densities as conditional expectations
and applies conditional Cauchy--Schwarz to show that Hellinger affinity cannot
decrease. Therefore, for the original arbitrary DQM product path,
\[
\left\|
\sqrt{\frac{d(\Pi_tC)}{d\Pi^c}}
-\sqrt{\frac{d(\Pi_{t,n}C)}{d\Pi^c}}
\right\|_2
\le
\left\|
\sqrt{\frac{d\Pi_t}{d\Pi}}
-\sqrt{\frac{d\Pi_{t,n}}{d\Pi}}
\right\|_2.
\]
Divide by \(|t|\), use the two input DQM expansions, and take
\(t\to0\). The limsup is at most
\(\frac12\|E_b(h-h_n)\|_2\). The proposed output scores differ by
\[
\|RE_b(h-h_n)\|_2\le\|E_b(h-h_n)\|_2.
\]
The bounded-score output expansion, the two displayed bounds, and
\(n\to\infty\) prove the general output DQM expansion. Mean preservation and
the norm estimate follow from conditional Jensen and Lemma 2.

### Domain statement

The source of \(L_b\) is the one-coordinate Hilbert tangent
\(L^2_0(\pi)\). Its intermediate score lies in
\(L^2_0(\pi^{\otimes b})\), and its target lies in
\(L^2_0(\pi^{\otimes b}C)\). Unless explicit isometric identifications are
supplied, \(L_b\) is not an endomorphism and an equation
\(L_bh=\lambda h\) is ill-typed.

### Falsifier

If \(C\) sends every block to one point, then \(L_bh=0\) for every centered
\(h\), although \(E_bh\ne0\) when \(h\ne0\). A fixed channel can erase the
entire score tangent.

## Lemma 4: exact Fisher defect and equality condition

For every \(h\in L^2_0(\pi)\),
\[
b\|h\|_2^2-\|L_bh\|_2^2
=\mathbb E_J\operatorname{Var}_J(E_bh\mid Z)
\ge0.
\]
Equivalently,
\[
\|h\|_2^2-\|\widetilde L_bh\|_2^2
=\frac1b\mathbb E_J\operatorname{Var}_J(E_bh\mid Z).
\]
Equality holds exactly when there is \(k\in L^2(\Pi^c)\) such that
\[
E_bh(X)=k(Z)
\qquad J\text{-almost surely}.
\]

### Proof

The conditional variance identity gives
\[
\|E_bh\|_2^2
=\|R(E_bh)\|_2^2
+\mathbb E_J\operatorname{Var}(E_bh\mid Z).
\]
Use Lemma 2. The nonnegative defect vanishes exactly when the conditional
variance vanishes almost surely, which is precisely coarse measurability of
the block score under the joint law.

### Falsifier to a global sufficiency overclaim

Equality for one score at one parameter is not recovery of the experiment.
Let \(A,B\) be independent Bernoulli variables with
\[
\Pr_\theta(A=1)=\frac12+\frac\theta4,\qquad
\Pr_\theta(B=1)=\frac12+\frac{\theta^2}{4},
\]
and let the channel retain only \(A\). At \(\theta=0\), the \(B\)-score is
zero, so the full score is \(A\)-measurable and Fisher equality holds.
Nevertheless the conditional law of \(B\) varies with \(\theta\), so no
single parameter-independent reverse kernel recovers the full experiment.

## Lemma 5: bounded action classes embed isometrically into the Fisher tangent

Let
\[
\overline{\mathfrak B}_\infty
=L^\infty(\pi)/\mathbb R1.
\]
For \(\phi\in L^\infty(\pi)\), the normalized exponential-action path is
\[
\pi_t^\phi(dx)
=\frac{e^{-t\phi(x)}}{\pi(e^{-t\phi})}\pi(dx).
\]
It is DQM with score
\[
\mathscr S_\pi[\phi]
=-\phi+\pi(\phi).
\]
Equip the quotient with the Fisher norm
\[
\|[\phi]\|_F
:=\inf_{c\in\mathbb R}\|\phi-c\|_2
=\|\phi-\pi(\phi)\|_2.
\]
Then
\[
\mathscr S_\pi:
(\overline{\mathfrak B}_\infty,\|\cdot\|_F)
\longrightarrow L^2_0(\pi)
\]
is a linear isometry. Its image is the bounded centered tangent subspace,
which is dense but generally not all of \(L^2_0(\pi)\). The Fisher-norm
completion of the bounded action quotient is canonically \(L^2_0(\pi)\).

### Proof

The bounded exponential and normalizer have uniform Taylor expansions:
\[
e^{-t\phi}=1-t\phi+O(t^2),\qquad
\pi(e^{-t\phi})=1-t\pi(\phi)+O(t^2).
\]
Taking the square root of their ratio gives
\[
\sqrt{\frac{d\pi_t^\phi}{d\pi}}
=1+\frac t2[-\phi+\pi(\phi)]+O_{L^\infty}(t^2).
\]
This proves the score formula. It is independent of the additive
representative. The quotient \(L^2\) minimizer is the mean, proving the norm
identity. Bounded simple functions are dense in \(L^2\), and centering
preserves convergence, proving density.

Let \(U:L^2(\pi)\to L^2(\pi^c)\) be the reverse conditional expectation of
the fixed channel and let \(\overline U\) be its action on quotient classes.
Mean preservation gives the exact commuting identity
\[
\mathscr S_{\pi^c}(\overline U[\phi])
=-U\phi+\pi^c(U\phi)
=U[-\phi+\pi(\phi)]
=U\mathscr S_\pi[\phi].
\]
For an iid block action
\(\Phi_\phi(x_1,\ldots,x_b)=\sum_i\phi(x_i)\), its score is
\[
\mathscr S_{\pi^{\otimes b}}[\Phi_\phi]
=E_b\mathscr S_\pi[\phi],
\]
and after blocking it is \(L_b\mathscr S_\pi[\phi]\).

### Required distinction

The bounded quotient carries at least two different useful norms. Its
supremum quotient norm controls the nonlinear action map. Its Fisher norm
controls the DQM tangent completion. The identity map between these normed
realizations is continuous in the direction
\[
\|[\phi]\|_F\le\|\phi-\pi(\phi)\|_\infty
\le2\|[\phi]\|_{\infty/\mathbb R},
\]
but the Fisher completion introduces unbounded scores on which the nonlinear
bounded action map is not defined.

## Lemma 6: exact Hermite domain boundary

Let \(\gamma=N(0,1)\), and let \(H_k\) be the probabilists' Hermite
polynomial of degree \(k\ge1\). Then \(H_k\in L^2_0(\gamma)\), so Lemma 1
provides a two-sided DQM path with score \(H_k\). Every \(H_k\) is unbounded
and hence lies outside \(L^\infty(\gamma)/\mathbb R1\).

The exponential-action normalizer has the following exact behavior:

1. \(k=1\): \(\gamma(e^{-tH_1})<\infty\) for every \(t\in\mathbb R\).
2. \(k=2\): since \(H_2(x)=x^2-1\), the normalizer is finite exactly when
   \(t>-1/2\), which contains a two-sided neighborhood of zero.
3. Odd \(k\ge3\): for every \(t\ne0\), one tail has
   \(-tH_k(x)-x^2/2\to+\infty\), so the normalizer diverges.
4. Even \(k\ge4\): it is finite for \(t>0\) sufficiently, but diverges for
   every \(t<0\); no two-sided exponential neighborhood exists.

The leading monomial \(x^k\) proves the last two statements because it
dominates the Gaussian quadratic tail. Thus a Hermite score basis may be a
complete Hilbert tangent basis while failing to define a two-sided
exponential-action chart. DQM spectral statements and nonlinear bounded
action statements must be kept on separate domains.

## Source map and necessary repairs

The line anchors below refer to the source hashes recorded at the top.

1. 07b lines 333--357, especially
   eq:rg-normalized-perturbation-action, correctly compute the score of a
   bounded normalized exponential action as
   \(-h+\pi(h)\). Add the quotient isometry \(\mathscr S_\pi\), its dense
   image, and the commuting conditional-expectation diagram. Do not call it
   surjective before Fisher completion.

2. 07b lines 370--415, especially
   thm:rg-action-lp-contraction and
   eq:rg-action-l2-conditional-defect, correctly prove the one-arrow
   conditional-expectation contraction. Add the iid score lift \(E_b\), its
   exact \(\sqrt b\) norm, \(L_b=RE_b\), and the factor \(b\) in the Fisher
   defect. This factor cannot be inferred from the one-copy theorem.

3. 07b lines 259--306 establish local analyticity for bounded actions after
   recentering. Keep its domain \(L^\infty\). It does not supply a nonlinear
   action map on the Fisher completion \(L^2_0\).

4. 08 lines 45--50, eq:ig-fisher-hessian, concern the finite-dimensional
   tangent of a declared regular Gaussian exponential family. State
   explicitly when the ambient \(L^2_0(\gamma)\) score Hilbert space is being
   used instead. These spaces agree only on scores generated by a declared
   Gaussian submodel; a formal Hermite expansion is not automatically a
   finite-dimensional model-parameter chart.

5. 08 lines 89--97, eq:ig-score, give the Gaussian mean/covariance scores.
   They lie in the Hermite sectors of degrees one and two and do possess
   two-sided exponential neighborhoods, but the degree-three and higher
   ambient Hermite directions generally do not. Any manuscript claim that
   all Hermite modes lie in one two-sided exponential action chart must be
   replaced by the DQM construction above.

## Atomic falsification checklist

- If a purported two-sided score path is not normalized for both signs of
  \(t\), Lemma 1 is not established.
- If iid Fisher information is written without the factor \(b\), the path
  parameter or score has been silently rescaled.
- If \(L_bh=\lambda h\) is written before source and target tangent spaces are
  identified, the equation is ill-typed.
- If Fisher equality for one \(h\) is promoted to recovery of a whole
  experiment, the Bernoulli control refutes it.
- If \(L^\infty/\mathbb R1\) is identified with all of \(L^2_0\) without
  completion, the Gaussian score \(x\) refutes surjectivity.
- If every Hermite score is asserted to define a two-sided exponential chart,
  \(H_3\) refutes the assertion: its exponential normalizer diverges for every
  nonzero parameter.
- If an output score is represented by an arbitrary pointwise reverse-kernel
  version rather than a conditional-expectation equivalence class, the claim
  is stronger than DQM pushforward supplies.
