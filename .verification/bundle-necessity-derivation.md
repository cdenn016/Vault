# Derivation: one common principal bundle is sufficient

## Claim tested

Separate belief and model gauge frames require two independent principal
bundles over the common base.

## Counterderivation

Let \(\pi:P\to\mathcal C\) be one principal \(G\)-bundle and let
\(\widehat\rho_b:G\curvearrowright\mathcal B_b\) and
\(\widehat\rho_m:G\curvearrowright\mathcal B_m\) be two actions. Then

\[
\mathcal E_b=P\times_{\widehat\rho_b}\mathcal B_b,
\qquad
\mathcal E_m=P\times_{\widehat\rho_m}\mathcal B_m
\]

are two distinct associated statistical bundles over the same base. Their
fibers and representations may differ.

On any common trivializing open set \(U\), choose two frame sections
\(u^b,u^m:U\to P\). Freeness and transitivity of the principal right action
give a unique smooth relative-frame field \(h:U\to G\) such that

\[
u^m(c)=u^b(c)\cdot h(c).
\]

Thus different belief and model frames are already possible inside one
principal fiber \(P_c\); a second principal bundle is not implied.

If the sections are independently re-chosen as
\(u^{b\prime}=u^b a\) and \(u^{m\prime}=u^m b\), then uniqueness gives

\[
h'=a^{-1}hb.
\]

For a common re-choice \(a=b=k\), this reduces to conjugation
\(h'=k^{-1}hk\). These are changes of local principal frame. They do not turn
the structure group of \(P\) into \(G\times G\).

Let the two frame atlases have transition functions defined by
\(u_j^x=u_i^xT_{ij}^x\). Since \(u_i^m=u_i^bh_i\), their transitions satisfy

\[
T_{ij}^m=h_i^{-1}T_{ij}^b h_j.
\]

The two Cech cocycles are therefore cohomologous representatives of one
principal-bundle class, not independent topological data.

A single connection \(\omega\) on \(P\) induces transports on both associated
bundles through the two representations. If genuinely different transports
are desired, one may choose two connections \(\omega_b,\omega_m\) on the same
\(P\). Their difference is a horizontal equivariant adjoint-valued one-form,
so this choice is globally well typed without a second principal bundle.

A fixed fiber map \(f:\mathcal B_b\to\mathcal B_m\) induces
\([p,b]\mapsto[p,f(b)]\) precisely when it intertwines the two \(G\)-actions.
More general base-dependent associated-bundle morphisms may be declared
directly. Different frame sections alone do not manufacture such a cross-fiber
map, and neither direction is forced to be inverse to the other.

This distinction survives inequivalent representations. The same principal
relative field \(h\) has represented images \(\rho_b(h)\) and \(\rho_m(h)\),
which may be matrices of different sizes. Neither image is a linear map from
the belief representation space to the model representation space. Such a
map \(A:V_b\to V_m\) descends to the associated bundles exactly when

\[
A\rho_b(g)=\rho_m(g)A
\qquad\text{for every }g\in G.
\]

Equivalently, \(A\in\operatorname{Hom}_G(V_b,V_m)\). This space can be zero;
for example, it is zero between inequivalent irreducible representations.
Nonlinear cross maps obey the corresponding equivariance identity. If only
the represented frames are observed and a representation has a nontrivial
kernel or stabilizer, \(h\) cannot in general be reconstructed uniquely from
those represented data, although it remains unique for the chosen principal
sections.

Therefore two principal bundles are necessary only for a strictly larger
model in which the channels have independent gauge groups, independent
principal-bundle topology, or independent gauge transformations modeled by
\(G_b\times G_m\). A pair \((P_b,P_m)\) can equivalently be packaged as the
fiber-product principal \(G_b\times G_m\)-bundle
\(P_b\times_{\mathcal C}P_m\). If the intended primitive symmetry is one
\(G\), the minimal construction is one \(P\) with two associated statistical
bundles.

## Counterexample to necessity

Take any principal \(G\)-bundle \(P\to\mathcal C\), two nonisomorphic
\(G\)-spaces \(\mathcal B_b,\mathcal B_m\), and two local sections of \(P\).
The associated bundles and distinct local frames exist while only one
principal bundle has been introduced. This directly refutes the necessity
claim.
