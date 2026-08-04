<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 7 exact finite-network measure-pair and action proof

## Scope and verification boundary

This derivation supplies the source-level proof obligations for the
measure-pair map, local action analyticity and derivatives, projective action
quotient, conditional \(L^p\) contraction, exact \(L^2\) defect, Dobrushin
cocycle certificate, positive-unital essential-spectrum theorem, and circle
topology witness. It applies to every finite standard-Borel agent network and
every finite composition of its normalized parameter-independent blocking
kernels. No upper bound on the number of agents enters the proof.

It does not assert an infinite-volume result, an unproved weighted nonlinear
action chart, a topology-independent relevance classification, or an
autonomous identification of a general scale cocycle. This is a derivation
artifact, not an independent adjudication or a claim-ledger update. The
central protected ledger is intentionally untouched.

The starting revision is
\(a2cca53c094077dad763c9c6d4e6226fc2695895\).  The reconciled source
SHA-256 values are
\(FB24FE2864C34C61253C60E2E3258A4BFAAFAC8EF2DE08133E9968A07CCF8925\)
for 07_general_renormalization.tex and
\(18FC259CE52A834F1EA536123032AAC60D83B857551F568D028819C3E5F9FF87\)
for 07b_agent_network_rg.tex.

The associated manuscript statements are Proposition
\(\mathrm{prop:rg\text{-}measure\text{-}pair\text{-}composition}\), Theorem
\(\mathrm{thm:rg\text{-}bounded\text{-}action\text{-}calculus}\), Theorem
\(\mathrm{thm:rg\text{-}action\text{-}lp\text{-}contraction}\), Proposition
\(\mathrm{prop:rg\text{-}dobrushin\text{-}cocycle}\), Theorem
\(\mathrm{thm:rg\text{-}unital\text{-}essential\text{-}spectrum}\), and
Proposition \(\mathrm{prop:rg\text{-}circle\text{-}norm\text{-}witness}\).

## Exact typed measure pair

Fix adjacent scales \(\ell,\ell+1\). Let
\((X_\ell,\mathcal X_\ell)\) and
\((X_{\ell+1},\mathcal X_{\ell+1})\) be standard-Borel spaces. The
finite-network realization takes \(X_\ell\) to be a finite product of
standard-Borel agent coordinate spaces. Let \(\rho_\ell\) be a probability
law and
\[
 m_\ell(dx)=e^{-H_\ell(x)}\rho_\ell(dx),\qquad
 0<M_\ell=m_\ell(X_\ell)<\infty,\qquad
 \pi_\ell=m_\ell/M_\ell .
\tag{7.1}
\]
The convention is \(e^{-\infty}=0\), so \(H_\ell\) is only an
almost-everywhere extended-real representative. Let
\[
 K_\ell:X_\ell\rightsquigarrow X_{\ell+1}
\tag{7.2}
\]
be a measurable normalized parameter-independent Markov kernel, including
any separately declared rescaling. Define
\[
 \rho_{\ell+1}=\rho_\ell K_\ell,\qquad
 m_{\ell+1}=m_\ell K_\ell,\qquad
 H_{\ell+1}=-\log\frac{dm_{\ell+1}}{d\rho_{\ell+1}}.
\tag{7.3}
\]

If \((\rho_\ell K_\ell)(A)=0\), then
\(K_\ell(x,A)=0\) for \(\rho_\ell\)-almost every \(x\), hence for
\(m_\ell\)-almost every \(x\), so \(m_{\ell+1}\ll\rho_{\ell+1}\).
Normalization preserves the mass \(M_\ell\), which proves
\[
 \pi_{\ell+1}=m_{\ell+1}/M_\ell=\pi_\ell K_\ell.
\tag{7.4}
\]
For a second normalized kernel, Tonelli's theorem yields
\[
 (\rho_\ell,m_\ell)(K_\ell K_{\ell+1})
 =((\rho_\ell K_\ell)K_{\ell+1},
   (m_\ell K_\ell)K_{\ell+1}).
\tag{7.5}
\]
The two components therefore compose exactly, while \(M_\ell\) remains a
separately retained evidence scalar.

Standard Borelness gives a regular conditional version. Fix a jointly
measurable reverse kernel \(\Pi_\ell(z,dx)\) such that
\[
 \pi_\ell(dx)K_\ell(x,dz)
 =\pi_{\ell+1}(dz)\Pi_\ell(z,dx).
\tag{7.6}
\]
For each fixed collection of input equivalence classes, every conditional
formula below is understood \(\pi_{\ell+1}\)-almost everywhere.  No one
pointwise representative is asserted simultaneously for an uncountable
family of perturbations.

## Bounded analytic action chart

Let \(\mathfrak B_\ell=L^\infty(\pi_\ell;\mathbb R)\), take
\(0<\epsilon<\log2\), and set
\[
 \mathcal U_{\ell,\epsilon}
 =\{\varphi\in\mathfrak B_\ell:\|\varphi\|_\infty<\epsilon\}.
\tag{7.7}
\]
For every \(\varphi\in\mathfrak B_\ell\), perturb the full pair by
\(m_\ell^\varphi=e^{-\varphi}m_\ell\). Define the coarse action increment
primarily as the Radon--Nikodym ratio
\[
 Q_\ell(\varphi)(z)
 =-\log\frac{d((e^{-\varphi}m_\ell)K_\ell)}{d(m_\ell K_\ell)}(z)
 =-\log\int e^{-\varphi(x)}\Pi_\ell(z,dx).
\tag{7.8}
\]
The second equality uses the reverse conditional for the normalized
\(\pi_\ell(dx)K_\ell(x,dz)\) joint. It gives
\[
 -\|\varphi\|_\infty\leq Q_\ell(\varphi)
 \leq\|\varphi\|_\infty
\tag{7.9}
\]
and so types \(Q_\ell\) on all of \(\mathfrak B_\ell\) as a map into
\(L^\infty(\pi_{\ell+1};\mathbb R)\).  Its analyticity claim below is
restricted to \(\mathcal U_{\ell,\epsilon}\).  Where both actions are finite
it is the ordinary action difference. When the base action is extended valued,
(7.8), and not an undefined expression of the form
\(+\infty-(+\infty)\), is the definition.

Define the positive unital operator
\[
 (U_\ell f)(z)=\int f(x)\Pi_\ell(z,dx).
\tag{7.10}
\]
Then
\[
 \|U_\ell(e^{-\varphi})-1\|_\infty
 \leq e^\epsilon-1<1.
\tag{7.11}
\]
The exponential power series converges in the source Banach algebra;
\(U_\ell\) is bounded; and the logarithm series converges in the target
unit ball about \(1\). Thus
\[
 Q_\ell=-\log(U_\ell e^{-\bullet})
\tag{7.12}
\]
is real analytic on the declared chart.

For a point \(\varphi\) in the chart, define
\[
 \Pi_\ell^\varphi(z,dx)
 =\frac{e^{-\varphi(x)}\Pi_\ell(z,dx)}
        {\int e^{-\varphi(u)}\Pi_\ell(z,du)}.
\tag{7.13}
\]
Its denominator is uniformly at least \(e^{-\epsilon}\). The Banach chain
rule gives
\[
 DQ_\ell(\varphi)[h](z)
 =\int h(x)\Pi_\ell^\varphi(z,dx).
\tag{7.14}
\]
Differentiating the normalized integral in direction \(k\) gives
\[
 \frac{d}{dt}\bigg|_{t=0}
 \int h(x)\Pi_\ell^{\varphi+tk}(z,dx)
 =-\int hk d\Pi_\ell^\varphi
  +\left(\int h d\Pi_\ell^\varphi\right)
   \left(\int k d\Pi_\ell^\varphi\right).
\tag{7.15}
\]
Therefore
\[
 D^2Q_\ell(\varphi)[h,k](z)
 =-\operatorname{Cov}_{\Pi_\ell^\varphi(z,\cdot)}(h,k).
\tag{7.16}
\]
At zero this specializes to
\[
 DQ_\ell(0)[h]=U_\ell h,\qquad
 D^2Q_\ell(0)[h,k]
 =-\operatorname{Cov}_{\Pi_\ell(z,\cdot)}(h,k).
\tag{7.17}
\]
The uniform denominator bound and bounded \(h,k\) supply the required
Fréchet norm bounds. The proof does not apply on arbitrary \(L^p\)
neighborhoods: for a Gaussian reference, a finite-\(L^p\) direction such as
\(-x^2\) makes \(e^{-\varphi}=e^{x^2}\) nonintegrable.

The same formula gives nonlinear sup-norm control. If
\(\varphi\leq\psi+c\), then
\(e^{-\varphi}\geq e^{-c}e^{-\psi}\), hence positivity and unitality of
\(U_\ell\) imply
\[
 Q_\ell(\varphi)\leq Q_\ell(\psi)+c.
\]
Using this inequality in both directions with
\(c=\|\varphi-\psi\|_\infty\) proves
\[
 \|Q_\ell(\varphi)-Q_\ell(\psi)\|_\infty
 \leq\|\varphi-\psi\|_\infty.
\tag{7.17a}
\]
Thus the bounded measure-pair action sector cannot acquire a relevant mode
after isometric scale identification. This conclusion does not apply to an
extensive interaction lift or to a weighted space without its own nonlinear
chart proof.

## Projective and normalized actions

Equation (7.8) gives \(Q_\ell(\varphi+c)=Q_\ell(\varphi)+c\), and
\(U_\ell1=1\). Thus, only after deliberately forgetting the evidence mass,
the maps descend to
\[
 \overline{\mathfrak B}_\ell
 =L^\infty(\pi_\ell;\mathbb R)/\mathbb R1.
\tag{7.18}
\]

The normalized perturbed probability is different:
\[
 \widehat\pi_\ell^\varphi
 =\frac{e^{-\varphi}\pi_\ell}{\pi_\ell(e^{-\varphi})},\qquad
 \widehat Q_\ell(\varphi)
 =-\log\frac{d(\widehat\pi_\ell^\varphi K_\ell)}
                 {d\pi_{\ell+1}}
 =Q_\ell(\varphi)+\log\pi_\ell(e^{-\varphi}).
\tag{7.19}
\]
It agrees with \(Q_\ell\) only modulo a constant. In particular,
\[
 D\widehat Q_\ell(0)[h]=U_\ell h-\pi_\ell(h),
\tag{7.20}
\]
\[
 D^2\widehat Q_\ell(0)[h,k]
 =-\operatorname{Cov}_{\Pi_\ell(z,\cdot)}(h,k)
  +\operatorname{Cov}_{\pi_\ell}(h,k).
\tag{7.21}
\]
The score of \(t\mapsto\widehat\pi_\ell^{th}\) is
\(-h+\pi_\ell(h)\), and the pushed score is
\(-U_\ell h+\pi_\ell(h)\). This is the score/Fisher interpretation of the
conditional-variance defect below. It is an \(L^2\) tangent statement and
does not enlarge the nonlinear action chart. At an extended-action boundary
or outside (7.7), a literal action difference and a differential beta are
not licensed; the measure pair is primary until a separate finite-valued
action-space theorem supplies subtraction and differentiability.

## \(L^p\) contraction and exact Fisher defect

For \(1\leq p<\infty\), conditional Jensen and (7.6) give
\[
 \int |U_\ell f|^p d\pi_{\ell+1}
 \leq\int U_\ell(|f|^p)d\pi_{\ell+1}
 =\int|f|^p d\pi_\ell.
\tag{7.22}
\]
The pointwise conditional bound gives the \(p=\infty\) case. Thus
\[
 \|U_\ell f\|_{L^p(\pi_{\ell+1})}
 \leq\|f\|_{L^p(\pi_\ell)}
\quad(1\leq p\leq\infty).
\tag{7.23}
\]
Means are preserved, so finite-\(p\) centered tangent spaces map to their
coarse counterparts.

For \(f\in L^2(\pi_\ell)\), the total conditional variance identity is
\[
 \|f\|_{L^2(\pi_\ell)}^2
 -\|U_\ell f\|_{L^2(\pi_{\ell+1})}^2
 =\int\operatorname{Var}_{\Pi_\ell(z,\cdot)}(f)
    d\pi_{\ell+1}(z)\geq0.
\tag{7.24}
\]
Equality holds exactly when the nonnegative conditional variance vanishes
\(\pi_{\ell+1}\)-almost everywhere. Equivalently, there is a measurable
\(g\) with \(f(x)=g(z)\) for
\(\pi_\ell(dx)K_\ell(x,dz)\)-almost every \((x,z)\). For a deterministic
coarse statistic \(z=c(x)\), this says \(f=g\circ c\)
\(\pi_\ell\)-almost everywhere. Applying (7.24) to the centered score in
(7.20) identifies the left side with Fisher information lost by the channel.

## Dobrushin certificate and controls

On the action quotient use
\[
 \|[f]\|_{\mathrm{osc}}
 =\frac12(\operatorname*{ess sup}f-\operatorname*{ess inf}f)
\tag{7.25}
\]
and define
\[
 \delta_\ell=
 \operatorname*{ess sup}_{(z,z')\sim\pi_{\ell+1}^{\otimes2}}
 \sup_{A\in\mathcal X_\ell}
 |\Pi_\ell(z,A)-\Pi_\ell(z',A)|.
\tag{7.26}
\]
The total-variation inequality
\[
 \left|\int f d\mu-\int f d\nu\right|
 \leq\operatorname{osc}(f)\sup_A|\mu(A)-\nu(A)|
\tag{7.27}
\]
implies
\[
 \|\overline U_\ell\|_{\mathrm{osc}\to\mathrm{osc}}
 \leq\delta_\ell.
\tag{7.28}
\]
For \(b_k>1\), set
\[
 B_{n\leftarrow\ell}=\prod_{k=\ell}^{n-1}b_k,\qquad
 \overline U_{n\leftarrow\ell}
 =\overline U_{n-1}\cdots\overline U_\ell.
\tag{7.29}
\]
Then
\[
 \|\overline U_{n\leftarrow\ell}\|
 \leq\prod_{k=\ell}^{n-1}\delta_k.
\tag{7.30}
\]
If \(B_{n\leftarrow\ell}\to\infty\) and
\[
 \limsup_{n\to\infty}
 \frac{\sum_{k=\ell}^{n-1}\log\delta_k}
      {\log B_{n\leftarrow\ell}}<0,\qquad
 \log0=-\infty,
\tag{7.31}
\]
every bounded quotient perturbation has strictly negative upper growth rate
in this norm.

This is sufficient only. For a full two-step nonnecessity witness, take
\[
 R_0=\begin{pmatrix}1&0\\0&1\\1/2&1/2\end{pmatrix},\qquad
 R_1=\begin{pmatrix}1/2&1/2&0\\0&0&1\end{pmatrix},
\tag{7.32}
\]
with compatible laws
\(\pi_0=(1/2,1/2)\), \(\pi_1=(1/3,1/3,1/3)\), and
\(\pi_2=(2/3,1/3)\). Each one-step coefficient is one, but both rows of
\(R_1R_0\) equal \((1/2,1/2)\), so the composed coefficient is zero.
Conversely, on two states take \(\pi_k=(1/2,1/2)\) at every scale, let
\(J\) have uniform rows, and use the compatible reverse kernels
\[
 R_k=(1-a_k)I+a_kJ,\qquad a_k=2^{-k-2}.
\tag{7.33}
\]
Then every \(\delta_k=1-a_k<1\), but
\(\prod_k\delta_k>0\); with fixed \(b_k=b>1\) the normalized log rate can
be zero. One-step strict contraction is not sufficient nonautonomously. The
identity channel and a two-cycle respectively retain all bounded modes and
exhibit eigenvalue \(-1\), so failure of (7.31) proves neither marginality,
relevance, nor a phase-free conclusion.

## Positive-unital essential spectrum

Let \(X\) be a complex Banach lattice, \(\mathbf1\in X_+\) a quasi-interior
unit, and \(U\in\mathcal L(X)\) positive and unital. With
\[
 q:\mathcal L(X)\longrightarrow\mathcal L(X)/\mathcal K(X),\qquad
 r_{\mathrm{ess}}(U)=r(q(U)),
\tag{7.34}
\]
assume that whenever \(r(U)>r_{\mathrm{ess}}(U)\), \(r(U)\) is a resolvent
pole and \(U^*\) has a nonzero positive eigenfunctional
\(U^*\lambda=r(U)\lambda\). The Calkin quotient is contractive, so
\(r_{\mathrm{ess}}(U)\leq r(U)\). If \(r(U)>1\) and strict inequality held,
the assumed \(\lambda\) would satisfy \(\lambda(\mathbf1)>0\). Indeed,
vanishing on the quasi-interior unit forces a positive functional to vanish
on its dense principal ideal and hence everywhere. But
\[
 r(U)\lambda(\mathbf1)
 =(U^*\lambda)(\mathbf1)
 =\lambda(U\mathbf1)=\lambda(\mathbf1),
\tag{7.35}
\]
a contradiction. Therefore
\[
 r(U)>1\Longrightarrow r(U)=r_{\mathrm{ess}}(U).
\tag{7.36}
\]
No quasi-compactness conclusion is invoked. The resolvent-pole clause is
retained as an exact stated hypothesis even though the pairing uses its
positive-eigenfunctional consequence.

## Circle topology witness

Let \(\mathbb T=\mathbb R/\mathbb Z\) carry geodesic distance and Haar law
\(\lambda\), and let \(D(z)=2z\bmod1\). Define the forward kernel invariantly
by
\[
 K(y,A)=\frac12\sum_{z\in D^{-1}\{y\}}\mathbf1_A(z).
\tag{7.37}
\]
For bounded \(f,g\), a two-branch change of variables shows
\[
 \int f(y)\int g(z)K(y,dz)d\lambda(y)
 =\int g(z)f(Dz)d\lambda(z).
\tag{7.38}
\]
Thus the reverse is \(\Pi(z,dy)=\delta_{D(z)}(dy)\) and \(Uf=f\circ D\).

Haar preservation gives \(\|U^nf\|_\infty=\|f\|_\infty\), hence
\[
 r_{L^\infty}(U)=1.
\tag{7.39}
\]
For \(0<\alpha\leq1\), use complex periodic \(C^\alpha(\mathbb T)\) with
the sup-plus-Holder norm. At \(\alpha=1\) this is the Lipschitz space
\(C^{0,1}\), not \(C^1\). Its seminorm obeys
\[
 [f\circ D^n]_\alpha\leq2^{\alpha n}[f]_\alpha.
\tag{7.40}
\]
For \(f(t)=e^{2\pi it}\), the points \(0\) and \(2^{-(n+1)}\) have function
values under \(f\circ D^n\) differing by two and have original distance
\(2^{-(n+1)}\). Therefore
\[
 [f\circ D^n]_\alpha\geq2^{1+\alpha(n+1)}.
\tag{7.41}
\]
The upper and lower bounds give
\[
 r_{C^\alpha}(U)=2^\alpha.
\tag{7.42}
\]
The standard Holder space with this norm is not the Banach lattice assumed in
the preceding positive-unital theorem, so this is a separate topology
comparison. Equations (7.39)--(7.42) use the same measurable kernel and
reverse conditional and directly rule out a topology-free spectral claim.

## Independent checks

A mechanism-separated probability reconstruction checked the normalized
reverse law, the Radon--Nikodym action ratio, every Fréchet derivative and
domain, the \(L^p\) and conditional-variance identities, quotient saturation,
and both Dobrushin controls.  After five local repairs it returned PASS.  A
separate operator adversary reconstructed the all-compacts Calkin argument and
the circle radii, caught the inverse-branch, complex-space, Lipschitz-endpoint,
and nonlattice guardrails, and returned PASS after repair.  The detailed
records are task-7-independent-reconstruction.md and
task-7-operator-adversarial.md.

One scratch two-pass TeX check occurred before the coordinator's stop
instruction.  It is recorded only as a non-production syntax probe and is not
release evidence; the authenticated release build remains assigned to the
later build gate.
