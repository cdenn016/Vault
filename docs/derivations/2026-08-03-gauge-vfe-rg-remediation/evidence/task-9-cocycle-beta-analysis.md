<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 9 route C: typed cocycles, modes, beta functions, and fixed objects

## Independence boundary and source binding

This route was reconstructed from the typed interfaces and elementary chain
rules. It does not use another Task 9 reconstruction. The checked input bytes
at the start of the reconstruction were:

- 07_general_renormalization.tex:
  5F0604C948220A22C3321918C0634481AD9ADB5FB4A25B1AEF78ED91A6858080
- 07b_agent_network_rg.tex:
  902E6ECF583CF084ADDCCDB3E84A265CFC8EEF5D4BA3BD3749E533295E6BD95C
- 05d_relational_inference.tex:
  138E4F86F107F5BD0307E049DC5368A6C36584A827BF98BF4EB396E30016D0A1
- claim-ledger.json:
  16A1538C266D4490BDE6745B20C2F95BD363E88B5D4045AFEF1B711446ABDA30

The result below is conditional on the declared Banach-space, smoothness,
comparison, and regular-configuration hypotheses. No autonomous spectrum or
continuous scale flow is inferred from a bare sequence of coarse maps.

## 1. Exact two-parameter evolution and derivative cocycle

Let \(X_\ell\) be Banach spaces and let

\[
 T_\ell:X_\ell\longrightarrow X_{\ell+1}
\]

be \(C^1\) on the relevant domains. For integers \(n\geq \ell\), define the
ordered nonlinear evolution by

\[
 \Phi_{n\leftarrow\ell}
 :=T_{n-1}\circ\cdots\circ T_{\ell},
 \qquad
 \Phi_{\ell\leftarrow\ell}:=\operatorname{id}_{X_\ell}.
\]

The arrows record domain and codomain:

\[
 \Phi_{n\leftarrow\ell}:X_\ell\longrightarrow X_n,
 \qquad
 \Phi_{r\leftarrow n}\circ\Phi_{n\leftarrow\ell}
 =\Phi_{r\leftarrow\ell}.
 \tag{1.1}
\]

Let \(x_{\ell+1}=T_\ell(x_\ell)\) be an exact orbit and put

\[
 M_\ell:=DT_\ell(x_\ell):X_\ell\longrightarrow X_{\ell+1}.
\]

For the established full-interaction map this specialization is

\[
 x_\ell=g_\ell,\qquad
 T_\ell=T_\ell^{\mathcal G}
 =P_{\ell+1}\overline Q_\ell E_\ell,\qquad
 M_\ell
 =P_{\ell+1}\overline{U_\ell^{\phi_{g_\ell}}}E_\ell.
\]

The untilted operator \(U_\ell\) is obtained only at \(g_\ell=0\).

Then the chain rule gives the exact ordered derivative cocycle

\[
 M_{n\leftarrow\ell}
 :=M_{n-1}\cdots M_\ell
 =D\Phi_{n\leftarrow\ell}(x_\ell),
 \qquad
 M_{r\leftarrow n}M_{n\leftarrow\ell}
 =M_{r\leftarrow\ell},
 \tag{1.2}
\]

with \(M_{\ell\leftarrow\ell}=I_{X_\ell}\). The rightmost factor acts first.

**Falsifier 1 (reversing the ordered product).** Let

\[
 A=\begin{pmatrix}1&1\\0&1\end{pmatrix},
 \qquad
 B=\begin{pmatrix}1&0\\1&1\end{pmatrix},
 \qquad M_0=A,\quad M_1=B.
\]

Then

\[
 M_{2\leftarrow0}=BA
 =\begin{pmatrix}1&1\\1&2\end{pmatrix}
 \neq
 AB=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]

Thus an unordered product, or a product with the scale order reversed, fails
even in two dimensions.

**Lemma 1 (cocycle is not semigroup).** Equation (1.1) is a two-parameter
cocycle law. After bounded identifications \(J_\ell:X_*\to X_\ell\), define

\[
 \widehat T_\ell
 :=J_{\ell+1}^{-1}T_\ell J_\ell:X_*\to X_*.
 \tag{1.3}
\]

Only when the identified maps are stationary,
\(\widehat T_\ell=\widehat T\), does
\(\widehat\Phi_{n\leftarrow\ell}=\widehat T^{\,n-\ell}\) form the usual
discrete semigroup. Periodicity gives monodromy, not a one-step autonomous
map. General scale dependence gives only the ordered two-parameter family.

**Falsifier 2 (semigroup overreach).** If the steps alternate between the
distinct matrices \(A\) and \(B\) above, no one map can equal both one-step
maps. The two-step monodromy is \(BA\) at even base points and \(AB\) at odd
base points; writing every segment as a power of one unnamed operator erases
the base scale and gives the wrong order.

For a mixed state, (1.1) must hold in every component category. Composition
of the interaction derivative alone does not prove composition of the base,
principal-bundle, law-fiber, associated-bundle, action, or configuration maps.
The full state is a functor or cocycle only when all of its declared component
maps have compatible identities and ordered compositions.

## 2. Compatible cross-scale modes

### 2.1 Rank-one mode sections

A typed rank-one mode section is a family

\[
 v_{\ell,a}\in X_\ell\setminus\{0\},
 \qquad
 \lambda_{\ell,a}\in\mathbb C,
\]

satisfying

\[
 \boxed{M_\ell v_{\ell,a}
 =\lambda_{\ell,a}v_{\ell+1,a}.}
 \tag{2.1}
\]

This is a compatibility equation between adjacent fibers, not an eigenvector
equation. Its normalization record must name the native norm, sign or complex
phase convention, and any per-volume scalar factor. These choices are scalar
gauge data of the form analyzed in (2.9). Induction using (1.2) gives

\[
 M_{n\leftarrow\ell}v_{\ell,a}
 =\lambda_{n\leftarrow\ell,a}v_{n,a},
 \qquad
 \boxed{\lambda_{n\leftarrow\ell,a}
 =\prod_{k=\ell}^{n-1}\lambda_{k,a}.}
 \tag{2.2}
\]

The empty product is one, and if a factor is zero then the propagated mode is
annihilated from that step onward. The complex phase or real sign is retained
separately from the growth exponent.

For a \(d_a\)-dimensional invariant mode bundle, choose frames
\(V_{\ell,a}:\mathbb C^{d_a}\to X_\ell\) and matrices
\(A_{\ell,a}\) such that

\[
 M_\ell V_{\ell,a}=V_{\ell+1,a}A_{\ell,a}.
 \tag{2.3}
\]

Then the finite-step matrix is the ordered product
\(A_{n-1,a}\cdots A_{\ell,a}\). It becomes a Jordan or ordinary spectral
problem only after a single endomorphism on one declared space has been
obtained and the usual point-spectrum hypotheses hold.

**Falsifier 3 (ordinary eigen-equation across unequal fibers).** Take
\(X_0=\mathbb R\), \(X_1=\mathbb R^2\), and
\(M_0x=(x,0)\). The expression \(M_0v=\lambda v\) equates an element of
\(\mathbb R^2\) with one of \(\mathbb R\) and is ill typed. Equation (2.1) is
well typed with \(v_0=1\), \(v_1=(1,0)\), and \(\lambda_0=1\).

### 2.2 Exact finite-time and asymptotic exponents

Let \(b_k>1\) be the declared adjacent scale ratios and set

\[
 s_{n\leftarrow\ell}
 :=\log B_{n\leftarrow\ell}
 :=\sum_{k=\ell}^{n-1}\log b_k,
 \qquad s_{n\leftarrow\ell}\longrightarrow\infty.
 \tag{2.4}
\]

For \(u\in X_\ell\setminus\{0\}\), the norm-dependent finite-time upper
growth rate is

\[
 \chi_{n\leftarrow\ell}(u)
 :=\frac{
 \log\lVert M_{n\leftarrow\ell}u\rVert_n
 -\log\lVert u\rVert_\ell}
 {s_{n\leftarrow\ell}}.
 \tag{2.5}
\]

Define

\[
 \chi^+_\ell(u):=\limsup_{n\to\infty}
 \chi_{n\leftarrow\ell}(u),
 \qquad
 \chi^-_\ell(u):=\liminf_{n\to\infty}
 \chi_{n\leftarrow\ell}(u).
 \tag{2.6}
\]

A Lyapunov exponent is asserted when the two agree. If a nonzero vector is
mapped to zero, its subsequent exponent is \(-\infty\).

For the compatible mode (2.1), define the scalar finite-time exponent

\[
 y^{\mathrm{sc}}_{n\leftarrow\ell,a}
 :=\frac{\log|\lambda_{n\leftarrow\ell,a}|}
 {s_{n\leftarrow\ell}}
 =\frac{\sum_{k=\ell}^{n-1}\log|\lambda_{k,a}|}
 {s_{n\leftarrow\ell}}.
 \tag{2.7}
\]

Equations (2.1), (2.5), and (2.7) give the exact relation

\[
 \chi_{n\leftarrow\ell}(v_{\ell,a})
 =y^{\mathrm{sc}}_{n\leftarrow\ell,a}
 +\frac{
 \log\lVert v_{n,a}\rVert_n
 -\log\lVert v_{\ell,a}\rVert_\ell}
 {s_{n\leftarrow\ell}}.
 \tag{2.8}
\]

Thus scalar and norm growth agree for unit-normalized mode sections, or more
generally when the endpoint norm term is sublinear in cumulative log scale.
The labels relevant, marginal, and irrelevant mean positive, zero, and
negative exponent only after the norm, comparison scheme, and limiting
convention have been declared.

### 2.3 Scalar gauge and tempered comparison theorem

Under a scalar change of mode section

\[
 v'_{\ell,a}=c_{\ell,a}v_{\ell,a},
 \qquad c_{\ell,a}\neq0,
\]

the adjacent coefficients and their product change by

\[
 \lambda'_{\ell,a}
 =\lambda_{\ell,a}\frac{c_{\ell,a}}{c_{\ell+1,a}},
 \qquad
 \lambda'_{n\leftarrow\ell,a}
 =\lambda_{n\leftarrow\ell,a}
   \frac{c_{\ell,a}}{c_{n,a}}.
 \tag{2.9}
\]

Hence the scalar exponent is invariant if

\[
 \frac{|\log|c_{n,a}||}{s_{n\leftarrow\ell}}
 \longrightarrow0.
 \tag{2.10}
\]

This is the required tempered scalar normalization condition. It is not the
whole comparison theorem.

**Lemma 2 (sufficient tempered comparison trivialization).** Let
\(J_k:X_*\to X_k\) be bounded linear isomorphisms, and equip \(X_*\) and every
\(X_k\) with the declared norms. Put

\[
 \widehat M_k:=J_{k+1}^{-1}M_kJ_k,
 \qquad
 \widehat M_{n\leftarrow\ell}
 =J_n^{-1}M_{n\leftarrow\ell}J_\ell.
 \tag{2.11}
\]

If

\[
 \frac{
 \log^+\lVert J_n\rVert
 +\log^+\lVert J_n^{-1}\rVert}
 {s_{n\leftarrow\ell}}
 \longrightarrow0,
 \tag{2.12}
\]

then the native norm exponent of \(u\in X_\ell\setminus\{0\}\) and the
reference norm exponent of \(J_\ell^{-1}u\) agree, whenever either limit is
interpreted as the corresponding limsup or liminf. Together, (2.10) and
(2.12) preserve both the scalar-mode exponent and the norm Lyapunov exponent.

**Proof.** For \(x_n=M_{n\leftarrow\ell}u\), bounded invertibility gives

\[
 \frac{\lVert x_n\rVert_n}{\lVert J_n\rVert}
 \leq\lVert J_n^{-1}x_n\rVert_*
 \leq\lVert J_n^{-1}\rVert\lVert x_n\rVert_n.
 \tag{2.13}
\]

The analogous two-sided bound at the fixed initial scale \(\ell\) changes the
finite-time numerator by at most

\[
 \log^+\lVert J_n\rVert+
 \log^+\lVert J_n^{-1}\rVert+C_{\ell,J}.
\]

Divide by (2.4) and use (2.12). Equation (2.9) proves the scalar part. \(\square\)

For a product state, complete comparison means an isomorphism in the
declared category on every component used by the claimed invariant:
law/reference data, action or interaction space, base and bundle data, and
configuration space as applicable. The bilateral bounded-tempered condition
(2.12) applies to each normed linear component entering a Lyapunov claim. A
tempered scalar field normalization does not provide the missing component
comparisons. For a claim confined to one linear tier, Lemma 2 only needs the
comparison of that tier.

**Falsifier 4 (tempered scalar normalization alone is insufficient).** Let
\(X_k=\mathbb R\) with native norm \(|\cdot|\), \(M_k=I\), \(b_k=e\), and
\(c_k=1\). The native exponent is zero and the scalar normalization is
tempered. Choose the non-tempered comparison

\[
 J_k u=e^{k^2}u.
\]

Then

\[
 \widehat M_k=e^{-2k-1}I,
 \qquad
 \widehat M_{n\leftarrow0}=e^{-n^2}I,
\]

so the apparent reference-space norm exponent is
\(-n^2/n=-n\to-\infty\). The exact transported reference mode
\(J_k^{-1}1=e^{-k^2}\) still has scalar coefficient one; renormalizing that
mode to unit reference norm uses the non-tempered scalar \(e^{k^2}\). This
separates the algebraic coefficient cocycle from the norm Lyapunov exponent
and shows why both hypotheses in Lemma 2 are required.

## 3. Typed discrete beta functions

Let the exact interaction step be

\[
 T_\ell^{\mathcal G}:\mathcal G_\ell\longrightarrow
 \mathcal G_{\ell+1},
\]

and orient the comparison isomorphisms as

\[
 J_\ell:\mathcal G_*\xrightarrow{\sim}\mathcal G_\ell.
\]

This is the inverse orientation of the manuscript's
\(I_\ell:\mathcal G_\ell\to\mathcal G_*\). The reference-space exact map is

\[
 \widehat T_\ell^{\mathcal G}
 :=J_{\ell+1}^{-1}T_\ell^{\mathcal G}J_\ell:
 \mathcal G_*\longrightarrow\mathcal G_*.
 \tag{3.1}
\]

For \(h_\ell:=\log b_\ell>0\), the exact discrete beta functional is

\[
 \boxed{
 \beta_\ell^{\mathrm{ex}}(g)
 :=\frac{
 J_{\ell+1}^{-1}T_\ell^{\mathcal G}J_\ell(g)-g}
 {h_\ell}.}
 \tag{3.2}
\]

Both terms in the numerator lie in the same declared Banach space
\(\mathcal G_*\). If the coupling object is a manifold rather than a vector
space, (3.2) must be replaced by a declared chart difference, logarithm map,
or retraction into one tangent space; a bare subtraction is undefined.

**Falsifier 5 (subtracting across fibers).** Let
\(\mathcal G_0=\mathbb R\), \(\mathcal G_1=\mathbb R^2\), and
\(T_0x=(x,0)\). Then \(T_0x-x\) has no type. Choosing
\(J_0u=u\) and \(J_1u=(u,0)\) only compares the one-dimensional image sector;
it is not an isomorphism onto all of \(\mathbb R^2\). A beta on the full output
therefore requires a genuine common reference object or a separately declared
embedded-sector theory.

The beta functional is scheme dependent. If
\(J'_\ell=J_\ell S_\ell\) for bounded isomorphisms
\(S_\ell:\mathcal G_*\to\mathcal G_*\), then

\[
 \widehat T'_{\ell}
 =S_{\ell+1}^{-1}\widehat T_\ell S_\ell,
 \qquad
 \beta'_\ell(g)
 =\frac{S_{\ell+1}^{-1}\widehat T_\ell(S_\ell g)-g}{h_\ell}.
 \tag{3.3}
\]

Only a scale-independent change of coordinates reduces this to the usual
pushforward relation. A scale-dependent comparison contributes its own term.

**Falsifier 6 (comparison-independent beta).** On
\(\mathcal G_\ell=\mathbb R\), let \(T_\ell=I\) and \(b_\ell=e\). With
\(J_\ell=I\), (3.2) is zero. With \(J_\ell u=a_\ell u\), it is

\[
 \beta_\ell(g)=\left(\frac{a_\ell}{a_{\ell+1}}-1\right)g.
\]

Thus even the identity native cocycle has a nonzero beta in a moving scale
frame. The comparison scheme must be part of the statement.

## 4. Exact, retained, and residual beta seam

Let \(R_\ell:\mathcal G_\ell\to\mathcal G_\ell\) be bounded idempotent
retained projections, and put

\[
 \widehat R_\ell:=J_\ell^{-1}R_\ell J_\ell.
\]

For a retained input \(g\in\operatorname{Ran}\widehat R_\ell\), define

\[
 \begin{aligned}
 \beta_\ell^{\mathrm{ex}}(g)
 &=\frac{\widehat T_\ell^{\mathcal G}(g)-g}{h_\ell},\\
 \beta_\ell^{\mathrm{ret}}(g)
 &=\frac{\widehat R_{\ell+1}
              \widehat T_\ell^{\mathcal G}(g)-g}{h_\ell},\\
 \delta\beta_\ell(g)
 &:=\beta_\ell^{\mathrm{ex}}(g)-
     \beta_\ell^{\mathrm{ret}}(g)\\
 &=\frac{(I-\widehat R_{\ell+1})
              \widehat T_\ell^{\mathcal G}(g)}{h_\ell}\\
 &=\frac{J_{\ell+1}^{-1}
              r_{\ell+1}^{\mathcal G}(J_\ell g)}{h_\ell}.
 \end{aligned}
 \tag{4.1}
\]

Here

\[
 r_{\ell+1}^{\mathcal G}(x)
 =(I-R_{\ell+1})T_\ell^{\mathcal G}(x).
\]

Therefore

\[
 \delta\beta_\ell(g)=0
 \quad\Longleftrightarrow\quad
 T_\ell^{\mathcal G}(J_\ell g)
 \in\operatorname{Ran}R_{\ell+1},
 \tag{4.2}
\]

and the retained beta is exact on the whole retained sector exactly when

\[
 T_\ell^{\mathcal G}(\operatorname{Ran}R_\ell)
 \subseteq\operatorname{Ran}R_{\ell+1}.
 \tag{4.3}
\]

At action-quotient level, the already established inverse identity gives the
corresponding omitted beta class

\[
 \delta\overline\beta_{\ell}^{Q}
 =\frac{E_{\ell+1}r_{\ell+1}^{\mathcal G}}{h_\ell},
 \qquad
 P_{\ell+1}\delta\overline\beta_{\ell}^{Q}
 =\frac{r_{\ell+1}^{\mathcal G}}{h_\ell}.
 \tag{4.4}
\]

**Falsifier 7 (projected fixed point called exact).** Take
\(\mathcal G=\mathbb R^2\), \(b=e\),

\[
 R(x,y)=(x,0),
 \qquad
 T(x,y)=(x,x).
\]

For the retained input \(g=(x,0)\),

\[
 \beta^{\mathrm{ret}}(g)=(0,0),
 \qquad
 \beta^{\mathrm{ex}}(g)=(0,x),
 \qquad
 \delta\beta(g)=(0,x).
\]

Every retained coordinate appears fixed, but the exact step generates an
omitted component unless \(x=0\). Bounded idempotence of \(R\) does not imply
closure.

## 5. Continuous covariant scale derivative

### 5.1 Required smooth extension

Let \(S\) be an oriented one-dimensional \(C^1\) scale manifold with local
coordinate \(s\), and let

\[
 \pi:\mathscr G\longrightarrow S
\]

be a \(C^1\) Banach vector bundle. A scale connection is a covariant
derivative

\[
 \nabla^{\mathrm{sc}}:\Gamma^1(\mathscr G)
 \longrightarrow\Omega^1(S;\mathscr G)
\]

satisfying the usual linearity and Leibniz rule. For a \(C^1\) running
coupling section \(g(s)\in\mathscr G_s\), define

\[
 \boxed{
 \beta^{\mathrm{sc}}(s)
 :=\nabla^{\mathrm{sc}}_{\partial_s}g(s)
 \in\mathscr G_s.}
 \tag{5.1}
\]

In a local trivialization \(I_s:\mathscr G_s\to\mathcal G_*\), write
\(\widetilde g(s)=I_sg(s)\) and let
\(A_s\in\mathcal L(\mathcal G_*)\) be the connection form. Then

\[
 I_s\beta^{\mathrm{sc}}(s)
 =\partial_s\widetilde g(s)+A_s\widetilde g(s).
 \tag{5.2}
\]

Under a frame change \(I'_s=S_sI_s\), covariance requires

\[
 A'_s=S_sA_sS_s^{-1}-(\partial_sS_s)S_s^{-1},
 \qquad
 I'_s\beta^{\mathrm{sc}}=S_sI_s\beta^{\mathrm{sc}}.
 \tag{5.3}
\]

Equation (5.3) follows by differentiating
\(\widetilde g'=S_s\widetilde g\). A raw derivative of coordinates does not
have this transformation law.

**Falsifier 8 (raw derivative under a moving frame).** On the trivial line
bundle, let \(g(s)=1\) be parallel in a frame with \(A_s=0\). Change frame by
\(S_s=e^{s^2}\). The raw derivative is
\(2se^{s^2}\neq0\), although the geometric beta is zero. Equation (5.3) gives
\(A'_s=-2s\), and

\[
 \partial_s(e^{s^2})-2se^{s^2}=0.
\]

### 5.2 Scale flow and generator

Let \(V_s\) be a \(C^1\) vertical vector field on \(\mathscr G_s\), locally
Lipschitz in the coupling. The nonautonomous scale-flow equation is

\[
 \nabla^{\mathrm{sc}}_{\partial_s}g(s)=V_s(g(s)).
 \tag{5.4}
\]

Its local evolution maps, where existence and uniqueness hold, are typed as

\[
 U(s,t):\mathscr G_t\longrightarrow\mathscr G_s,
 \qquad
 U(r,s)\circ U(s,t)=U(r,t),
 \qquad U(t,t)=I_{\mathscr G_t}.
 \tag{5.5}
\]

In a local trivialization, (5.4) reads

\[
 \partial_s\widetilde g
 =\widetilde V_s(\widetilde g)-A_s\widetilde g.
 \tag{5.6}
\]

Conversely, for a differentiable evolution family its covariant infinitesimal
generator is

\[
 V_t(x)
 =\left.
 \nabla^{\mathrm{sc}}_{\partial_s}U(s,t)x
 \right|_{s=t}.
 \tag{5.7}
\]

The one-parameter semigroup form \(U(s,t)=\Psi_{s-t}\) needs a stationary
bundle trivialization, stationary connection, and autonomous vector field,
plus the required global existence domain. It is not a consequence of (5.5).

**Falsifier 9 (discrete endpoints determine a continuous beta).** On
\(S=\mathbb R\) and the trivial line bundle, both evolution families

\[
 U_0(s,t)x=x,
 \qquad
 U_\epsilon(s,t)x
 =\exp\{\epsilon[\sin(2\pi s)-\sin(2\pi t)]\}x
 \tag{5.8}
\]

satisfy (5.5) and agree at every pair of integer endpoints. Their generators
are respectively \(V_s(x)=0\) and
\(V_s(x)=2\pi\epsilon\cos(2\pi s)x\). Thus a discrete RG sequence admits inequivalent
smooth interpolations with different continuous beta functions. Smooth scale
base, bundle, interpolation, and connection data are all additional input.

### 5.3 Separation from contextual gauge connections

The scale connection \(\nabla^{\mathrm{sc}}\) has base \(S\) and compares
coupling fibers at different resolutions. A contextual principal connection
\(\omega_s\) lives on a principal bundle \(P_s\to B_s\) at one resolution;
its local gauge potential \(A_s^{\mathrm{ctx}}\) compares associated fibers
along directions in \(TB_s\). Their types are

\[
 \nabla^{\mathrm{sc}}:
 \Gamma(TS)\times\Gamma(\mathscr G)\to\Gamma(\mathscr G),
 \qquad
 \omega_s\in\Omega^1(P_s;\mathfrak g),
 \qquad
 A_s^{\mathrm{ctx}}\in\Omega^1(B_s;\mathfrak g).
 \tag{5.9}
\]

They can be related only after supplying extra geometry, such as a connection
on a two-base bundle over \(S\times B\) and compatibility of its mixed
directions. Reusing \(\omega_s\) as the scale derivative is ill typed.

**Falsifier 10 (context connection supplies scale transport).** Let every
context base \(B_s\) be a point. Its local contextual gauge potential has no
nonzero base direction; a principal connection still has its required
vertical normalization, but neither datum compares distinct scale fibers.
The scale line bundle may nevertheless use the moving frame of Falsifier 8
and require the nonzero scale connection form \(-2s\). Contextual connection
data cannot recover that scale comparison.

## 6. Tier-specific invariant and fixed objects

Let \(Y_\ell^{(\tau)}\) denote one of the following tiers and let
\(F_\ell^{(\tau)}:Y_\ell^{(\tau)}\to Y_{\ell+1}^{(\tau)}\) be its declared
step:

| Tier \(\tau\) | Object | Exact invariant-section equation | Extra condition before a fixed-object claim |
|---|---|---|---|
| law | normalized law \(\mu_\ell\), event law \(\eta_\ell\), or tracked pair \((\rho_\ell,m_\ell)\) | \(\mu_{\ell+1}=F_\ell^{\rm law}\mu_\ell\), and separately for every tracked component | common rescaled law space; a fixed conditional row also needs a fixed receiver marginal; a fixed normalized pair tracks evidence mass |
| action | \(H_\ell\) relative to \(\rho_\ell\), or an additive-gauge class \([H_\ell]\) | \(H_{\ell+1}=F_\ell^H[H_\ell;\rho_\ell]\) | common reference and reference-law invariance; equality modulo constants is weaker than full pair invariance |
| interaction | full \(g_\ell\in\mathcal G_\ell\) | \(g_{\ell+1}=T_\ell^{\mathcal G}g_\ell\) | common interaction space; a retained fixed point is exact only if (4.2) vanishes |
| configuration | \(q_\ell\in\mathcal Q_\ell\) | \(q_{\ell+1}=C_\ell^{\mathcal Q}(q_\ell)\) | smooth comparison diffeomorphisms between configuration manifolds; this map is not the law, action, interaction, or bundle map |

For any tier, a nonautonomous invariant section is exactly a sequence

\[
 y_{\ell+1}=F_\ell(y_\ell).
 \tag{6.1}
\]

After isomorphisms \(J_\ell:Y_*\to Y_\ell\), a scale-constant reference
object \(y_*\in Y_*\) satisfies

\[
 J_{\ell+1}^{-1}F_\ell J_\ell(y_*)=y_*
 \quad\text{for every }\ell.
 \tag{6.2}
\]

In an autonomous scheme, (6.2) is the ordinary fixed-point equation
\(\widehat F(y_*)=y_*\). Without the common object, the expression
\(F_\ell(y)=y\) is ill typed. A positive fixed ray additionally requires a
declared cone and projectivization; an action class modulo additive constants
is a different quotient and must keep its evidence-mass seam explicit.

### 6.1 Periodic and monodromy objects

If the identified maps are \(p\)-periodic,
\(\widehat F_{\ell+p}=\widehat F_\ell\), define the base-\(\ell\) monodromy

\[
 \mathcal M_\ell
 :=\widehat F_{\ell+p-1}\circ\cdots\circ\widehat F_\ell.
 \tag{6.3}
\]

A monodromy point \(y_\ell\) obeys
\(\mathcal M_\ell(y_\ell)=y_\ell\). Its successive images form a \(p\)-cycle:

\[
 y_{\ell+j}
 =\widehat F_{\ell+j-1}\circ\cdots\circ\widehat F_\ell(y_\ell),
 \qquad y_{\ell+p}=y_\ell.
 \tag{6.4}
\]

It need not be fixed by any one-step map.

**Falsifier 11 (monodromy point called one-step fixed).** Let the period-two
maps on \(\mathbb R\) be

\[
 F_0(x)=x+1,
 \qquad F_1(x)=x-1.
\]

The monodromy \(F_1\circ F_0=I\) fixes every point, while \(F_0\) and \(F_1\)
have no one-step fixed points. The invariant object is a two-cycle
\((x,x+1)\), not a common fixed point.

### 6.2 Non-implications between tiers

The following counterexamples prevent fixedness from being transferred
between named tiers without a commuting and sufficiently injective bridge.

**Falsifier 12a (fixed law does not fix an action coordinate).** On the
two-point set, hold
\(\mu=(1/2,1/2)\) fixed but alternate the reference laws

\[
 \rho_0=(1/4,3/4),
 \qquad \rho_1=(3/4,1/4).
\]

The actions \(H_i=-\log(d\mu/d\rho_i)\) are swapped and are not equal even
though the normalized law is unchanged. A fixed law therefore does not give a
fixed reference-dependent action unless the reference is also invariant.

**Falsifier 12b (fixed action class does not fix a tracked pair).** In an
additive action quotient, \(H\) and \(H+c\) are identical. Their unnormalized
measures \(e^{-H}\rho\) and \(e^{-c}e^{-H}\rho\) have different evidence
masses when \(c\neq0\). Hence fixedness modulo constants is weaker than
fixedness of the tracked reference/evidence pair; under a normalized
mass-preserving RG with fixed reference, mass preservation forces \(c=0\).

**Falsifier 12c (fixed retained interaction does not fix the exact
interaction).** Falsifier 7 has zero retained beta at every \((x,0)\) but a
nonzero exact residual for \(x\neq0\).

**Falsifier 12d (fixed law does not fix a configuration).** Let
\(\mathcal Q=S^1\), let the smooth configuration step be the antipodal map
\(C(q)=-q\), and let the configuration-to-law extraction be the constant map
\(\Pi(q)=\mu_*\). The law \(\mu_*\) is fixed, but the configuration map has no
fixed point. Noninjective extraction erases the configuration motion.

**Falsifier 12e (fixed conditional row does not fix an event law).** If a
conditional row \(\beta(dj\mid i)\) is held fixed while the receiver marginal
\(\alpha_\ell(di)\) alternates, the event laws
\(\eta_\ell(di,dj)=\alpha_\ell(di)\beta(dj\mid i)\) alternate. Row fixedness
is only one component of law fixedness.

## 7. Configuration flow is not scale flow

At each scale, let \(\mathcal Q_\ell\) be the separately declared regular
configuration manifold, \(X_\ell^{\rm VFE}\) its locally unique VFE vector
field, and

\[
 C_\ell^{\mathcal Q}:\mathcal Q_\ell\to\mathcal Q_{\ell+1}
\]

the separately smooth configuration coarse map. The integer \(\ell\) is RG
depth, whereas an integral-curve parameter \(r\) belongs to the inference
flow. Independently recomputed fine and coarse histories describe the same
oriented orbit only if

\[
 T_qC_\ell^{\mathcal Q}\,X_\ell^{\rm VFE}(q)
 =a_\ell(q)
   X_{\ell+1}^{\rm VFE}(C_\ell^{\mathcal Q}q),
 \qquad a_\ell(q)>0.
 \tag{7.1}
\]

Equation (7.1) is an orbit semiconjugacy with positive reparameterization. It
is independent of the scale-bundle connection in Section 5. A scale beta is a
derivative in \(TS\); an inference velocity is tangent to
\(\mathcal Q_\ell\) at fixed scale.

**Falsifier 13 (coarse configuration sequence called an inference
history).** Let \(C(q)=q_0\) be constant and let the coarse vector field vanish.
Then (7.1) can hold while every nonconstant fine orbit collapses to one point.
Semiconjugacy alone does not make the pushed history nonconstant, and the
sequence \(q_{\ell+1}=C_\ell(q_\ell)\) remains an RG-depth sequence rather
than a time trajectory.

## 8. Claim and source map

The line anchors below refer to the source bytes listed in the binding above.

| Ledger claim | Ledger anchor and state | Current executable mathematical source | Route-C result or remaining seam |
|---|---|---|---|
| generalized-modes | claim-ledger.json:69, CANDIDATE | 07b_agent_network_rg.tex:837-882 supplies the exact nonlinear interaction orbit and typed derivative; 07b_agent_network_rg.tex:1577-1593 states only the relevance convention | Equations (2.1)-(2.13), Lemma 2, and Falsifiers 3-4 supply the missing compatible-mode, exponent, scalar-gauge, and bilateral tempered-comparison derivation |
| cocycle-law | claim-ledger.json:70, CANDIDATE | 07_general_renormalization.tex:14-32 gives typed composition; 07b_agent_network_rg.tex:1393-1415 distinguishes compatible semigroup from typed cocycle | Equations (1.1)-(1.3) and (2.2), with Falsifiers 1-2, prove ordering and delimit semigroup language |
| fixed-objects | claim-ledger.json:71, CANDIDATE | 07_general_renormalization.tex:418-469 distinguishes autonomous, periodic, stationary-random, and general cocycles; 07b_agent_network_rg.tex:1503-1538 distinguishes pair, action, action-class, and attention-law fixedness | Equations (6.1)-(6.4) and Falsifiers 11-12e add the typed law/action/interaction/configuration split and monodromy theory |
| beta-functions | claim-ledger.json:72, CANDIDATE | 07_general_renormalization.tex:34-53 defines reference comparisons; 07_general_renormalization.tex:474-482 records scheme dependence; 07b_agent_network_rg.tex:1417-1475 gives a same-space discrete action beta and a separate density-semigroup generator | Equations (3.1)-(3.3) type the discrete interaction subtraction; (5.1)-(5.9) state the additional smooth Banach-bundle data and the distinct scale connection |
| exact-interaction-map | claim-ledger.json:65, EVIDENCE_VERIFIED | 07b_agent_network_rg.tex:837-882 | Supplies the exact nonlinear \(T_\ell^{\mathcal G}\) and \(DT_\ell^{\mathcal G}\) used in Sections 1, 3, and 4 |
| projected-interaction-residual | claim-ledger.json:66, EVIDENCE_VERIFIED | 07b_agent_network_rg.tex:884-928 | Equations (4.1)-(4.4) divide the established exact residual by the declared log-scale step and keep exact and retained beta functions separate |
| configuration-map and history-semiconjugacy | claim-ledger.json:80 and :82, both CANDIDATE | 05d_relational_inference.tex:713-762 proves the oriented semiconjugacy criterion; 05d_relational_inference.tex:764-786 separates RG depth from inference time | Section 7 imports only the typed criterion needed to prevent a configuration fixed-object or scale-flow overreach; it does not close the separate configuration-map existence claim |

## 9. Closure conditions and direct falsifiers

The reconstructed claims survive exactly the following checks:

1. Every displayed adjacent map has codomain equal to the next displayed
   domain, and every finite product is ordered with the earliest step on the
   right.
2. Every mode uses (2.1), not an eigen-equation across unequal spaces.
3. Every reported scalar exponent records its section normalization; every
   norm Lyapunov comparison records both \(J_\ell\) and \(J_\ell^{-1}\) and
   satisfies (2.12).
4. Every discrete beta subtraction occurs only after (3.1), in one vector
   space or one declared chart.
5. Every retained beta is accompanied by the exact residual (4.1); exactness
   is equivalent to (4.2) or (4.3), not to idempotence alone.
6. Every continuous beta names the smooth scale base, Banach bundle,
   interpolation, and scale connection. Discrete endpoint data alone fail by
   (5.8).
7. The scale connection is not a contextual gauge connection; their bases and
   tangent types differ as in (5.9).
8. Fixed law, action, interaction, and configuration objects are tested in
   their own tiers. A periodic object is a monodromy point or cycle, and a
   general nonautonomous object is a typed invariant section.

A source statement violating any numbered condition is directly falsified by
the counterexample carrying the same subject above. These are mathematical
closure conditions, not evidence that the manuscript has already inserted
all of them.
