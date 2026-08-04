# Task 7 independent exact-action reconstruction

## Scope and evidential role

- Starting artifact revision: a2cca53c094077dad763c9c6d4e6226fc2695895.
- The reconstructor was given the Task 7 obligations and definitions but did
  not edit the manuscript and did not receive the implementation proof.
- This record supplies a derivation and quantified counterexamples.  Agent
  agreement is not closure evidence; the equations below and their explicit
  hypotheses are the evidence used by the parent verifier.

## Measure pair and reverse kernel

At scale \(\ell\), let \(\rho_\ell\) be a probability measure on a
standard-Borel space, let
\[
m_\ell=e^{-H_\ell}\rho_\ell,\qquad
0<M_\ell=m_\ell(\mathsf X_\ell)<\infty,\qquad
\pi_\ell=M_\ell^{-1}m_\ell,
\]
and let \(K_\ell\) be a normalized parameter-independent Markov kernel.  Then
\[
\rho_{\ell+1}=\rho_\ell K_\ell,\qquad
m_{\ell+1}=m_\ell K_\ell,\qquad
\pi_{\ell+1}=\pi_\ell K_\ell,
\]
and the evidence mass is preserved.  Standard Borelness supplies a fixed
reverse-kernel version \(\Pi_\ell(z,dx)\), unique only
\(\pi_{\ell+1}\)-almost everywhere, satisfying
\[
\pi_\ell(dx)K_\ell(x,dz)
=\pi_{\ell+1}(dz)\Pi_\ell(z,dx).
\]
Thus
\[
(U_\ell f)(z)=\int f(x)\Pi_\ell(z,dx)
\]
is a typed conditional-expectation map from fine to coarse observables.

## Conditional log-Laplace action

For \(0<\epsilon<\log 2\) and
\(\|\varphi\|_{L^\infty(\pi_\ell)}<\epsilon\), define the evidence-mass
tracking increment by the Radon--Nikodym ratio
\[
Q_\ell(\varphi)
=-\log\frac{d((e^{-\varphi}m_\ell)K_\ell)}
{d(m_\ell K_\ell)}
=-\log U_\ell(e^{-\varphi}).
\]
This definition is valid on the normalized coarse support even if the base
action is extended valued; it never forms
\(+\infty-(+\infty)\).  Since
\[
\|U_\ell(e^{-\varphi})-1\|_\infty
\le e^\epsilon-1<1,
\]
the Banach-algebra logarithm series proves real analyticity on the declared
open ball.  Direct Fréchet differentiation gives
\[
DQ_\ell(\varphi)[h]
=\frac{U_\ell(e^{-\varphi}h)}
{U_\ell(e^{-\varphi})},
\]
and, for the tilted reverse law
\[
\Pi_\ell^\varphi(z,dx)
=\frac{e^{-\varphi(x)}\Pi_\ell(z,dx)}
{U_\ell(e^{-\varphi})(z)},
\]
\[
D^2Q_\ell(\varphi)[h,k]
=-\operatorname{Cov}_{\Pi_\ell^\varphi(z,\cdot)}(h,k).
\]
At the origin these reduce to
\[
DQ_\ell(0)=U_\ell,\qquad
D^2Q_\ell(0)[h,k]
=-\operatorname{Cov}_{\Pi_\ell(z,\cdot)}(h,k).
\]
A two-atom symbolic reconstruction yielded
\[
D^2_{tu}Q(0)
=-p(1-p)(a-c)(b-d),
\]
which is exactly the negative conditional covariance.

The full action and normalized-probability conventions differ.  If
\[
\widehat\pi^\varphi
=\frac{e^{-\varphi}\pi_\ell}{\pi_\ell(e^{-\varphi})},
\]
then
\[
\widehat Q_\ell(\varphi)
=Q_\ell(\varphi)+\log\pi_\ell(e^{-\varphi}),
\]
\[
D\widehat Q_\ell(0)[h]
=U_\ell h-\pi_\ell(h),
\]
\[
D^2\widehat Q_\ell(0)[h,k]
=-\operatorname{Cov}_{\Pi_\ell(z,\cdot)}(h,k)
+\operatorname{Cov}_{\pi_\ell}(h,k).
\]
The two conventions agree only modulo constants.  Therefore the unnormalized
measure-pair derivative cannot be described as the normalized full-space
derivative without this correction.

## \(L^p\) contraction and Fisher defect

Conditional Jensen and disintegration give, for every
\(1\le p\le\infty\),
\[
\|U_\ell f\|_{L^p(\pi_{\ell+1})}
\le \|f\|_{L^p(\pi_\ell)},\qquad
\int U_\ell f\,d\pi_{\ell+1}
=\int f\,d\pi_\ell.
\]
For \(f\in L^2(\pi_\ell)\), total conditional variance is the exact identity
\[
\|f\|_{L^2(\pi_\ell)}^2
-\|U_\ell f\|_{L^2(\pi_{\ell+1})}^2
=\int\operatorname{Var}_{\Pi_\ell(z,\cdot)}(f)
\,\pi_{\ell+1}(dz)\ge0.
\]
Equality holds exactly when \(f(X)=g(Z)\) under the joint law for some
measurable coarse \(g\).  Applied componentwise to a DQM score, this is the
positive-semidefinite Fisher-information defect
\[
I_{\mathrm{fine}}-I_{\mathrm{coarse}}
=\mathbb E\operatorname{Cov}(s(X)\mid Z)\succeq0.
\]
This linear \(L^2\) result does not enlarge the nonlinear \(L^\infty\) chart.

## Dobrushin theorem and two incompatible controls

On \(L^\infty(\pi_\ell)/\mathbb R1\), use half the essential oscillation as
the quotient norm and define
\[
\delta_\ell
=\operatorname*{ess\,sup}_{z,z'}
\sup_A|\Pi_\ell(z,A)-\Pi_\ell(z',A)|.
\]
Then
\[
\|\overline U_\ell\|_{\mathrm{osc}\to\mathrm{osc}}
\le\delta_\ell,\qquad
\|\overline U_{n-1}\cdots\overline U_\ell\|
\le\prod_{k=\ell}^{n-1}\delta_k.
\]
For \(B_{n\leftarrow\ell}=\prod_{k=\ell}^{n-1}b_k\to\infty\), the condition
\[
\limsup_{n\to\infty}
\frac{\sum_{k=\ell}^{n-1}\log\delta_k}
{\log B_{n\leftarrow\ell}}<0,\qquad
\log0=-\infty,
\]
is therefore sufficient for negative oscillation growth.

It is not necessary.  Take reverse matrices
\[
R_0=
\begin{pmatrix}
1&0\\0&1\\1/2&1/2
\end{pmatrix},
\qquad
R_1=
\begin{pmatrix}
1/2&1/2&0\\0&0&1
\end{pmatrix}.
\]
They are compatible with
\[
\pi_0=(1/2,1/2),\quad
\pi_1=(1/3,1/3,1/3),\quad
\pi_2=(2/3,1/3).
\]
Each one-step coefficient equals one, but both rows of \(R_1R_0\) equal
\((1/2,1/2)\); the two-step quotient operator is zero.

Conversely, strict contraction at every step is not enough without an
accumulated rate.  On two states let
\[
R_k=(1-a_k)I+a_kJ,\qquad a_k=2^{-k-2},
\]
where both rows of \(J\) are uniform.  Then
\(\delta_k=1-a_k<1\) for all \(k\), but
\(\prod_k\delta_k>0\).  Thus neither one-step language nor failure of the
sufficient certificate can be promoted to a necessary classification.

## Domain and zero-temperature boundaries

The reverse kernel is an almost-everywhere object.  If the evidence mass is
zero or infinite, its normalized law and this reverse kernel are unavailable.
If the coarse density vanishes on positive reference mass, the action is
\(+\infty\), so no finite action subtraction or beta functional exists there.

For finite inverse temperature \(\beta\), the same calculation applied to
\[
-\beta^{-1}\log U_\ell(e^{-\beta f})
\]
requires a finite positive conditional partition function.  As
\(\beta\to\infty\), it tends to the conditional essential infimum and is
generally nondifferentiable.  On a two-atom conditional law the limit is a
minimum, whereas the Hessian is
\(-\beta\operatorname{Cov}\) and can diverge.  No analytic zero-temperature
limit is inferred from the finite-\(\beta\) theorem.

## Reconstruction conclusion

The independent route reproduces the measure-pair map, conditional
log-Laplace derivatives, \(L^p\) contraction, Fisher defect, and sufficient
Dobrushin criterion.  It also supplies quantifier-matched falsifiers for
broader action-domain, normalized/full-space, one-step, necessity, and
zero-temperature claims.  Essential-spectrum and circle-topology claims were
assigned to a separate operator audit so that this reconstruction does not
manufacture agreement by sharing their proof route.
