<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Oracle-erasure reconstruction of the finite gauge--VFE--RG theory

## Isolation, source binding, and scope

This is a fresh derivation from the corrected proof-erased packet and ordinary
mathematics. The only project-content source consulted was
`task-15-oracle-packet.md`, raw SHA-256
`7bab5363c02dce7026598c0c4e4c23a58242cfd8b77b8d947215c415279f7a23`
(9,255 bytes, 172 LF line endings, no CRLF or bare CR). I did **not** consult
the manuscript theorem or proof text, the problem contract, the claim ledger,
any Task 5--14 derivation, any Task 15 sibling memo, Git history, build output,
test output, or a PDF. The packet's wording is not evidence for any conclusion
below.

All equalities between Radon--Nikodym derivatives or conditional expectations
are equalities in the indicated almost-everywhere equivalence class unless a
pointwise version is explicitly fixed. `KL` is the extended relative entropy
in \([0,\infty]\). Every finite product below has a nonempty finite index set;
constants are kept separate from normalized probabilities and from interaction
coordinates.

## P. Probability, action, ELBO, and conditional agents

### Theorem P1 (mass preservation, exact action, and composition)

Let \(Z_\ell:=m_\ell(X_\ell)\). Then

\[
 \rho_{\ell+1}(X_{\ell+1})=1,
 \qquad m_{\ell+1}(X_{\ell+1})=Z_\ell,
 \qquad \pi_{\ell+1}=\pi_\ell K_\ell.
\]

For \(\varphi\in L^\infty(m_\ell)\), define the unnormalized coarse action

\[
 \mathcal A_{K_\ell}^{m_\ell}(\varphi)(z)
 :=-\log\frac{d((e^{-\varphi}m_\ell)K_\ell)}
 {d(m_\ell K_\ell)}(z).
\]

Boundedness of \(\varphi\) makes the two pushed measures equivalent. With the
fixed reverse conditional law in the packet,

\[
 e^{-\mathcal A_{K_\ell}^{m_\ell}(\varphi)(z)}
 =\int e^{-\varphi(x)}\Pi_\ell(dx\mid z),                 \tag{P1.1}
\]

and hence

\[
 \operatorname*{ess\,inf}\varphi
 \leq \mathcal A_K(\varphi)
 \leq \operatorname*{ess\,sup}\varphi,
 \qquad
 \mathcal A_K(\varphi+c)=\mathcal A_K(\varphi)+c.       \tag{P1.2}
\]

If \(K:X\rightsquigarrow Y\) and \(L:Y\rightsquigarrow W\) are normalized
parameter-independent kernels, then, with the reference measure displayed,

\[
 \mathcal A_{KL}^{m}(\varphi)
 =\mathcal A_L^{mK}\!\left(\mathcal A_K^m(\varphi)\right)
 \quad mKL\text{-a.e.}                                  \tag{P1.3}
\]

Here \(KL(x,dw):=\int K(x,dy)L(y,dw)\); thus the rightmost
action is applied first.

For \(c_\varphi:=\pi(e^{-\varphi})\), the normalized perturbation
\(q_\varphi=e^{-\varphi}\pi/c_\varphi\) has coarse action

\[
 \widehat{\mathcal A}_{K}^{\pi}(\varphi)
 :=-\log\frac{d(q_\varphi K)}{d(\pi K)}
 =\mathcal A_K^m(\varphi)+\log c_\varphi.                \tag{P1.4}
\]

Thus normalization removes additive constants, whereas the evidence mass
\(m^\varphi(X)=Zc_\varphi\) remains a separate positive scalar. Normalized
actions obey the same typed composition law.

**Proof.** Kernel normalization gives \((\mu K)(Y)=\mu(X)\) for every finite
measure \(\mu\), proving the mass identities. The joint law
\(\pi(dx)K(x,dz)=(\pi K)(dz)\Pi(dx\mid z)\) gives (P1.1) by testing both
sides against bounded measurable functions of \(z\). Bounds and constant
covariance follow from averaging \(e^{-\varphi}\). Pushing
\((e^{-\varphi}m)K=e^{-\mathcal A_K^m(\varphi)}mK\) once more through \(L\)
gives (P1.3). Dividing both numerator and denominator by their respective
masses gives (P1.4). \(\square\)

**Boundary and counterexample.** An RN derivative is not a value on a null
slice. Changing its representative on an \(mK\)-null set leaves every theorem
above unchanged but can change a purported pointwise likelihood there.
Moreover, if a kernel is not normalized, mass preservation fails by exactly
\(\int K(x,Y)m(dx)-m(X)\).

### Theorem P2 (Fréchet derivatives and normalization correction)

On any bounded open \(L^\infty\) chart, define the tilted reverse kernel

\[
 \Pi_\varphi(dx\mid z)
 :=\frac{e^{-\varphi(x)}\Pi(dx\mid z)}
 {\int e^{-\varphi}\,d\Pi(\cdot\mid z)}.
\]

The action is twice Fréchet differentiable, and for
\(u,v\in L^\infty(\pi)\),

\[
 D\mathcal A_K(\varphi)[u](z)=\mathbb E_{\Pi_\varphi(\cdot\mid z)}u,
                                                                    \tag{P2.1}
\]
\[
 D^2\mathcal A_K(\varphi)[u,v](z)
 =-\operatorname{Cov}_{\Pi_\varphi(\cdot\mid z)}(u,v).             \tag{P2.2}
\]

Consequently \(D^2\mathcal A_K(\varphi)[u,u]\leq0\), with equality at
\(z\) exactly when \(u\) is constant
\(\Pi_\varphi(\cdot\mid z)\)-a.s. The derivative bounds

\[
 \|D\mathcal A_K(\varphi)[u]\|_\infty\leq\|u\|_\infty,
 \qquad
 \|D^2\mathcal A_K(\varphi)[u,v]\|_\infty
 \leq\|u\|_\infty\|v\|_\infty                            \tag{P2.3}
\]

hold. If \(q_\varphi=e^{-\varphi}\pi/c_\varphi\), normalization changes
the derivatives to

\[
 D\widehat{\mathcal A}_K(\varphi)[u](z)
 =\mathbb E_{\Pi_\varphi(\cdot\mid z)}u-\mathbb E_{q_\varphi}u,     \tag{P2.4}
\]
\[
 D^2\widehat{\mathcal A}_K(\varphi)[u,v](z)
 =-\operatorname{Cov}_{\Pi_\varphi(\cdot\mid z)}(u,v)
  +\operatorname{Cov}_{q_\varphi}(u,v).                             \tag{P2.5}
\]

The normalized Hessian has no pointwise sign. Its quadratic mean under
\(q_\varphi K\) is, however,

\[
 \int D^2\widehat{\mathcal A}_K(\varphi)[u,u]\,(q_\varphi K)(dz)
 =\operatorname{Var}_{q_\varphi K}
   \!\left(\mathbb E_{\Pi_\varphi}[u\mid Z]\right)\geq0,           \tag{P2.6}
\]

with equality exactly when the tilted conditional mean is constant
\(q_\varphi K\)-a.e.

**Proof.** Uniform exponential bounds on the chart justify the uniform Taylor
expansion of \(e^{-(\varphi+tu)}\) inside each conditional integral. Taking
one and two derivatives of minus its logarithm gives (P2.1)--(P2.2).
Cauchy--Schwarz gives (P2.3). Differentiating
\(\log\pi(e^{-\varphi})\) contributes \(-\mathbb E_{q_\varphi}u\)
and \(+\operatorname{Cov}_{q_\varphi}(u,v)\), proving (P2.4)--(P2.5).
Equation (P2.6) is the law of total variance. \(\square\)

**Boundary.** Strict concavity fails precisely in directions already
measurable at the coarse output. Probability normalization adds a global
constant functional and therefore destroys pointwise concavity; claiming the
same Hessian sign after normalization is false.

### Theorem P3 (all Banach \(L^p\) bounds, adjunction, defects, and DQM)

For the joint probability
\(J(dx,dz)=\pi(dx)K(x,dz)=(\pi K)(dz)\Pi(dx\mid z)\), define

\[
 (Ug)(x):=\int g(z)K(x,dz),\qquad
 (Rh)(z):=\int h(x)\Pi(dx\mid z).
\]

For every \(1\leq p\leq\infty\),

\[
 \|U\|_{L^p(\pi K)\to L^p(\pi)}
 =\|R\|_{L^p(\pi)\to L^p(\pi K)}=1,                                \tag{P3.1}
\]

and \(R=U^*\) in the \(L^2\) pairing. The exact defects are

\[
 \|h\|_{L^2(\pi)}^2-\|Rh\|_{L^2(\pi K)}^2
 =\int\operatorname{Var}_{\Pi(\cdot\mid z)}(h)\,(\pi K)(dz),       \tag{P3.2}
\]

The same statements hold for the tilted reverse operator \(R_\varphi\), with
\((\pi,\pi K)\) replaced by \((q_\varphi,q_\varphi K)\). In addition,
\(\|\mathcal A_K(\varphi)-\mathcal A_K(\psi)\|_\infty
\leq\|\varphi-\psi\|_\infty\). Thus \(U\) and \(R\) are the exact
observable-lifting and score-restriction operators for a block viewed as a
meta-agent; (P3.2) is precisely the information discarded by that view.
\[
 \|g\|_{L^2(\pi K)}^2-\|Ug\|_{L^2(\pi)}^2
 =\int\operatorname{Var}_{K(x,\cdot)}(g)\,\pi(dx).                 \tag{P3.3}
\]

Equality in (P3.2) holds exactly when \(h(X)=Rh(Z)\), \(J\)-a.s.; the
analogous statement holds for (P3.3). There is no Banach operator-norm claim
here for \(0<p<1\).

Now let \((P_t)_{|t|<\epsilon}\) be a possibly nondominated two-sided DQM
path at \(P=P_0\). Write its Lebesgue decomposition relative to \(P\) as
\(P_t=p_tP+P_t^\perp\), and assume

\[
 \left\|\sqrt{p_t}-1-\tfrac t2h\right\|_{L^2(P)}=o(|t|),
 \qquad P_t^\perp(X)=o(t^2),qquad h\in L_0^2(P).                    \tag{P3.4}
\]

Then \(P_tK\) is DQM at \(PK\), with score

\[
 h_K(z)=\mathbb E[h(X)\mid Z=z],                                    \tag{P3.5}
\]

and Fisher information

\[
 \|h_K\|_{L^2(PK)}^2
 =\|h\|_{L^2(P)}^2-\mathbb E\operatorname{Var}(h\mid Z).          \tag{P3.6}
\]

The pushed singular measure \(S_t=P_t^\perp K\) may cease to be singular.
If \(S_t=s_tPK+S_t^{\perp,PK}\), both its absolutely continuous spillover
and its remaining singular mass have total mass at most \(o(t^2)\); their
Hellinger contribution is \(o(|t|)\), so neither changes (P3.5).

**Proof.** Conditional Jensen proves both contractions, and constants prove
the norms are exactly one. Fubini gives adjunction. Orthogonal projection in
\(L^2(J)\) gives (P3.2)--(P3.3). Applying this contraction to the square-root
remainder in (P3.4), and bounding the Hellinger norm of a positive measure by
the square root of its mass, proves output DQM. The first-order absolutely
continuous term is conditional expectation, giving (P3.5)--(P3.6). The
Lipschitz bound follows by inserting
\(e^{-\|\varphi-\psi\|_\infty}\leq e^{-\varphi}/e^{-\psi}
\leq e^{\|\varphi-\psi\|_\infty}\) into (P1.1). \(\square\)

**Boundary.** A parameter-dependent kernel contributes its own score and can
increase Fisher information; (P3.5) is false without parameter independence.
The singular component cannot simply be called singular after pushforward.

### Theorem P4 (extended ELBO and exact block relation)

For the finite evidence slice \(M_o=z_o\Pi_o\) and any probability \(Q\), set

\[
 D(Q\|M_o):=
 \begin{cases}
  \displaystyle\int\log\frac{dQ}{dM_o}\,dQ,&Q\ll M_o,\\
  +\infty,&\text{otherwise},
 \end{cases}
 \qquad
 \mathcal L_o(Q):=-D(Q\|M_o).                                      \tag{P4.1}
\]

Then, without splitting an expected log likelihood from an entropy,

\[
 \mathcal L_o(Q)=\log z_o-\operatorname{KL}(Q\|\Pi_o),
 \qquad
 \log z_o-\mathcal L_o(Q)=\operatorname{KL}(Q\|\Pi_o).             \tag{P4.2}
\]

Thus \(\mathcal L_o\in[-\infty,\log z_o]\), and equality at the upper bound
holds exactly when \(Q=\Pi_o\). For any normalized parameter-independent
kernel \(K\),

\[
 \mathcal L_{M_oK}(QK)\geq\mathcal L_{M_o}(Q),                      \tag{P4.3}
\]

and, on standard-Borel spaces, the exact gap loss is

\[
 \operatorname{KL}(Q\|\Pi_o)
 =\operatorname{KL}(QK\|\Pi_oK)
 +\int\operatorname{KL}\!\left(Q(dx\mid z)\|\Pi_o(dx\mid z)\right)
       (QK)(dz).                                                     \tag{P4.4}
\]

When \(\operatorname{KL}(Q\|\Pi_o)<\infty\), data-processing equality holds
exactly when the two reverse conditionals agree \(QK\)-a.e. If both sides of
the inequality are \(+\infty\), numerical equality of extended values is not
an equality certificate; the conditional remainder in (P4.4) is decisive.

For a nonempty block \(B\) and complement \(C\), fixed regular conditional
versions give the extended chain rule

\[
 \operatorname{KL}(Q\|\Pi_o)
 =\operatorname{KL}(Q_C\|\Pi_{o,C})
 +\int\operatorname{KL}\!\left(Q_B(\cdot\mid c)
          \|\Pi_{o,B}(\cdot\mid c)\right)Q_C(dc).                  \tag{P4.5}
\]

With \(Q_C\) fixed, define

\[
 \mathcal J_B(Q_B\mid Q_C)
 :=-\int\operatorname{KL}\!\left(Q_B(\cdot\mid c)
          \|\Pi_{o,B}(\cdot\mid c)\right)Q_C(dc).
\]

Then \(\mathcal L_o(Q)=C(Q_C)+\mathcal J_B(Q_B\mid Q_C)\). Therefore
the block and collective variations agree exactly, but their full objective
values differ by the outside term \(C(Q_C)\). Shared and higher-body factors
are already present in \(\Pi_{o,B}(\cdot\mid c)\); no sum of independent
block objectives follows.

**Proof.** Since \(dM_o=z_o,d\Pi_o\), (P4.2) is immediate. The KL chain
rule applied to the joint laws before and after \(K\) gives (P4.4), hence
(P4.3). Applying the same disintegration to coordinates \((X_B,X_C)\) gives
(P4.5). All terms are nonnegative extended quantities, so no
\(\infty-\infty\) subtraction occurs. \(\square\)

**Counterexample.** Two correlated binary agents have positive mutual
information. Summing their two marginal KL objectives omits that interaction
term, so it cannot equal the joint objective even though both marginal
objectives are well-defined.

### Theorem P5 (exact observational internalization, not deconditioning)

Let \(R\) contain all retained agent variables and \(O\) the selected-record
variables. On standard-Borel spaces, a joint law admits a normalized measurable
kernel \(C(do\mid r)\) such that

\[
 P_{R,O}(dr,do)=P_R(dr)C(do\mid r).                                  \tag{P5.1}
\]

Relabeling the output of \(C\) as another agent node, or as one meta-agent
whose state is the whole record, reproduces the same joint law and therefore
the same expectations on \(\sigma(R,O)\). This is the exact sense in which an
observation can be represented by agent--agent interaction.

A product message representation

\[
 C(do\mid r)=\prod_{a=1}^m C_a(do_a\mid r_{j(a)})                    \tag{P5.2}
\]

holds if and only if the displayed kernels are normalized and the corresponding
ordered conditional laws satisfy

\[
 P(do_a\mid r,o_{<a})=C_a(do_a\mid r_{j(a)})
 \quad P_{R,O_{<a}}\text{-a.s.}                                    \tag{P5.3}
\]

Pairwise marginals do not prove (P5.2). An equivalent bounded energy
interaction additionally requires domination by a declared product reference,
strictly positive density on the relevant support, and a bounded log density;
(P5.1) alone supplies none of these.

Selecting \(O=o\) still gives \(P_R(dr\mid O=o)\). Node relabeling does not
remove conditioning, choose a version on a null observation, prove an
agent-only ontology, or encode interventions and exogenous noise unless those
are separately included.

**Proof.** Standard-Borel disintegration gives (P5.1). Replacing the name of a
coordinate preserves the measure identically. Repeated conditioning proves the
equivalence of (P5.2) and (P5.3). Conditioning on a selected coordinate is a
different operation from adjoining that coordinate to the joint state, so it
survives relabeling. \(\square\)

**Minimal counterexample.** Let \(X_1,X_2\) be independent fair bits and
\(O=X_1\oplus X_2\). The record is independent of each agent separately, yet
is determined by the pair. Individual pairwise channels cannot reproduce the
joint law without a shared or higher-body factor.

### Theorem P6 (attention posterior and variational row)

Let a categorical label \(A\) take values in a finite nonempty set \(J\), with
\(a_j>0\), finite source energies \(E_j\), and a complete selected-record
likelihood \(L_j(o)\geq0\). Assume no other factor reads \(A\), and

\[
 0<W(o):=\sum_{j\in J}a_j e^{-E_j}L_j(o)<\infty.
\]

Then the exact label posterior is

\[
 r_j(o):=P(A=j\mid o)
 =\frac{a_j e^{-E_j}L_j(o)}{W(o)}.                                  \tag{P6.1}
\]

When all \(L_j(o)>0\), this is the softmax of
\(\log a_j-E_j+\log L_j(o)\). For any categorical recognition row
\(q=(q_j)\), with the usual extended conventions,

\[
 \mathcal J_A(q;o)
 :=\sum_jq_j\!\left[\log(a_je^{-E_j}L_j(o))-\log q_j\right]
 =\log W(o)-\operatorname{KL}(q\|r).                               \tag{P6.2}
\]

The unrestricted unique optimum on the posterior support is \(q=r\). In a
restricted recognition family \(\mathcal Q\), the optimum is only an
information projection \(\arg\min_{q\in\mathcal Q}\operatorname{KL}(q\|r)\),
if attained. With other recognized latents, the coordinate formula becomes

\[
 q_j\ \propto\ \exp\!\left(
   \mathbb E_{q_{-A}}[\log p(A=j,\text{complete record})]
 \right),                                                          \tag{P6.3}
\]

only when the recognition factorization, support, and finite-expectation
hypotheses make this expression valid.

**Proof.** Bayes normalization gives (P6.1); direct algebra gives (P6.2), and
nonnegativity of KL gives the optimum. Coordinate variation with a Lagrange
multiplier gives (P6.3). \(\square\)

**Boundary.** An omitted label-dependent factor changes every numerator in
(P6.1). A zero-likelihood source has zero posterior mass, and assigning it
positive variational mass makes (P6.2) \(-\infty\).

## I. Complete interactions, retained residuals, and Fisher modes

### Theorem I1 (finite Hoeffding--Möbius isomorphism)

Write \(V=\{1,\ldots,n\}\), \(\nu=\bigotimes_i\nu_i\), and for
\(A\subseteq V\) let

\[
 (C_Af)(x_A):=\int f(x_A,x_{A^c})\,\nu_{A^c}(dx_{A^c}).
\]

For \(f\in L^\infty(\nu)\), define

\[
 f_A:=\sum_{B\subseteq A}(-1)^{|A|-|B|}C_Bf.                       \tag{I1.1}
\]

Then

\[
 f=\sum_{A\subseteq V}f_A,\qquad
 f_\varnothing=\int f,d\nu,\qquad
 \int f_A\,d\nu_i=0\quad(i\in A).                                \tag{I1.2}
\]

The representation is unique. Consequently the extraction \(P[f]=(f_A)_{A
\ne\varnothing}\) and assembly \(E(f_A)=\sum_{A\ne\varnothing}f_A\)
are inverse between bounded actions modulo constants and the full hierarchical
interaction space.

With \(\|[f]\|_{\mathrm q}:=\inf_c\|f-c\|_\infty\) and
\(\|(f_A)\|_1:=\sum_{A\ne\varnothing}\|f_A\|_\infty\),

\[
 \|f_A\|_\infty\leq2^{|A|}\|[f]\|_{\mathrm q},
 \qquad
 \|P[f]\|_1\leq(3^n-1)\|[f]\|_{\mathrm q},
 \qquad
 \|E(f_A)\|_\infty\leq\|(f_A)\|_1.                              \tag{I1.3}
\]

For the maximum component norm, \(\|E\|\leq2^n-1\). These are finite-size
bounds; they are not uniform as \(n\to\infty\).

**Proof.** Boolean-lattice Möbius inversion gives the first identity in
(I1.2). Pairing subsets in (I1.1) that differ by \(i\) proves hierarchical
zero mean. Applying the same integration recursively proves uniqueness.
Conditional averaging is an \(L^\infty\) contraction, so the triangle
inequality gives \(2^{|A|}\); summing over nonempty \(A\) gives
\(\sum_A2^{|A|}-1=3^n-1\). \(\square\)

**Product-reference obstruction.** Equivalence \(\nu\sim\pi\) gives the same
null sets, not independence under \(\pi\). Replacing the product averaging
operators by correlated \(\pi\)-conditionals destroys their commutation and
the Möbius proof. For example, let \(X_1,X_2\in\{-1,1\}\) have fair marginals
and the strictly positive symmetric law
\(P(X_1=a,X_2=b)=(1+rab)/4\), with \(r\in(0,1)\). For \(f=X_1\), successive
conditional projections give \(rX_2\) in one order and \(r^2X_1\) in the
other. Thus product structure is load-bearing.

### Theorem I2 (exact interaction RG and derivative away from the origin)

Let \(\mathcal I_\ell\) be the full nonempty-subset interaction space and
write \(\phi=E_\ell J\). Define the exact interaction update and its scalar
part by

\[
 \mathscr T_\ell(J)
 :=P_{\ell+1}\mathcal A_{K_\ell}(E_\ell J),
 \qquad
 a_\ell(J):=\int\mathcal A_{K_\ell}(E_\ell J)\,d\nu_{\ell+1}.       \tag{I2.1}
\]

Then

\[
 \mathcal A_{K_\ell}(E_\ell J)
 =a_\ell(J)+E_{\ell+1}\mathscr T_\ell(J).                          \tag{I2.2}
\]

For \(\dot J\in\mathcal I_\ell\), with the reverse law tilted by
\(e^{-E_\ell J}\),

\[
 D\mathscr T_\ell(J)[\dot J]
 =P_{\ell+1}R_{E_\ell J}E_\ell\dot J,                              \tag{I2.3}
\]
\[
 Da_\ell(J)[\dot J]
 =\int R_{E_\ell J}(E_\ell\dot J)\,d\nu_{\ell+1}.                 \tag{I2.4}
\]

In particular the linearization is an interaction extraction of a conditional
expectation only at the chosen base interaction; replacing \(R_{EJ}\) by the
untilted \(R_0\) away from \(J=0\) is incorrect. The Hessian is the extraction
of the negative tilted conditional covariance from Theorem P2.

**Proof.** Theorem I1 applied at level \(\ell+1\) gives (I2.2). The chain rule,
Theorem P2, and boundedness of \(P,E\) give (I2.3)--(I2.4). \(\square\)

**Boundary.** The scalar part in (I2.1) depends on the declared reference
\(\nu_{\ell+1}\), while the reconstructed action modulo constants does not.
No interaction-coordinate formula is available if the coarse action leaves the
bounded action class.

### Theorem I3 (retained update and exact closure criterion)

Let \(\mathsf Q_{\ell+1}:\mathcal I_{\ell+1}\to\mathcal I_{\ell+1}\) be
the declared bounded idempotent and
\(\mathcal T_{\ell+1}=\operatorname{ran}\mathsf Q_{\ell+1}\). For a
full input \(J\), define

\[
 J_{\ell+1}^{\rm ret}:=\mathsf Q_{\ell+1}\mathscr T_\ell(J),
 \qquad
 \epsilon_\ell(J):=(I-\mathsf Q_{\ell+1})\mathscr T_\ell(J).       \tag{I3.1}
\]

Then

\[
 \mathscr T_\ell(J)=J_{\ell+1}^{\rm ret}+\epsilon_\ell(J),
 \qquad \mathsf Q_{\ell+1}\epsilon_\ell(J)=0.                    \tag{I3.2}
\]

For one input, \(\epsilon_\ell(J)=0\) if and only if
\(\mathscr T_\ell(J)\in\mathcal T_{\ell+1}\). If inputs are retained in
\(\mathcal T_\ell\), exact ansatz closure is equivalent to each of

\[
 \mathscr T_\ell(\mathcal T_\ell)\subseteq\mathcal T_{\ell+1},
 \qquad
 (I-\mathsf Q_{\ell+1})\mathscr T_\ell|_{\mathcal T_\ell}=0.       \tag{I3.3}
\]

No norm estimate on later errors follows from idempotence alone; that requires
norm bounds or stability/Lipschitz estimates for subsequent exact maps.

**Proof.** These are the range/kernel identities for an idempotent. \(\square\)

**Boundary.** An idempotent need not be orthogonal or contractive. Thus
\(\|\epsilon_\ell\|\) is not automatically a best-approximation error, and a
small one-step residual need not remain small after further updates.

### Theorem I4 (every centered score has a two-sided DQM path)

For any probability \(\pi\) and \(h\in L_0^2(\pi)\), set

\[
 p_t(x):=\frac{(1+\tfrac t2h(x))^2}
 {1+\tfrac{t^2}{4}\|h\|_2^2},
 \qquad P_t(dx):=p_t(x)\pi(dx),\qquad t\in\mathbb R.               \tag{I4.1}
\]

This is a normalized, nonnegative, two-sided path through \(\pi\), and

\[
 \left\|\sqrt{p_t}-1-\tfrac t2h\right\|_2=o(|t|).                  \tag{I4.2}
\]

Thus every centered \(L^2\) vector is a genuine DQM score, without an
exponential-moment assumption.

For \(b\) independent replicas and extensive replication, the fine score is
\(H_b=\sum_{i=1}^bh(X_i)\), and for any coarse statistic \(Z\),

\[
 I_{\rm fine}=\|H_b\|_2^2=b\|h\|_2^2,
 \quad I_{\rm coarse}=\|\mathbb E[H_b\mid Z]\|_2^2,
 \quad I_{\rm fine}-I_{\rm coarse}
 =\mathbb E\operatorname{Var}(H_b\mid Z).                          \tag{I4.3}
\]

**Proof.** Normalization in (I4.1) uses \(\mathbb Eh=0\). The only difference
between \(|1+th/2|\) and \(1+th/2\) lies on
\(\{|h|>2/|t|\}\), where its squared \(L^2\) norm is bounded by
\(t^2\mathbb E[h^2\mathbf1_{|h|>2/|t|}]=o(t^2)\). The denominator differs
from one by \(O(t^2)\), proving (I4.2). Product DQM adds independent scores;
centering kills cross terms. Theorem P3 gives the last two identities. \(\square\)

**Boundary.** Formula (I4.1) constructs a dominated path even though Theorem P3
also permits nondominated paths. It proves tangent realizability, not the
existence of higher derivatives or finite exponential moments.

### Theorem I5 (Gaussian block spectrum and Fisher budget)

Let \(\gamma=N(0,1)\), \(b\geq1\),
\(Z=b^{-1/2}\sum_iX_i\), and define the extensive block operator

\[
 (B_bh)(z):=\mathbb E\!\left[\sum_{i=1}^bh(X_i)\mid Z=z\right].     \tag{I5.1}
\]

For the normalized probabilists' Hermite basis,

\[
 B_be_k=b^{1-k/2}e_k.                                               \tag{I5.2}
\]

For \(b>1\), on all of \(L^2(\gamma)\),

\[
 \sigma(B_b)=\{b^{1-k/2}:k=0,1,2,\ldots\}\cup\{0\}.               \tag{I5.3}
\]

The zero value is a spectral accumulation point, not an eigenvalue; \(B_b\)
is injective and compact. On the centered tangent space the \(k=0\) value
\(b\) is absent, so the values begin \(\sqrt b,1,b^{-1/2},\ldots\).
For \(b=1\), \(B_1=I\) and the spectrum is \(\{1\}\).

If \(h=\sum_{k\geq1}a_ke_k\), then

\[
 I_{\rm coarse}=\sum_{k\geq1}a_k^2b^{2-k},
 \qquad
 I_{\rm fine}-I_{\rm coarse}
 =\sum_{k\geq1}a_k^2\bigl(b-b^{2-k}\bigr).                        \tag{I5.4}
\]

The linear mode loses no Fisher information; every \(k\geq2\) mode loses
information for \(b>1\). If replication is averaged by \(b^{-1}\), the
eigenvalues become \(b^{-k/2}\); if it is normalized by \(b^{-1/2}\), they
become \(b^{(1-k)/2}\). In \(d\) dimensions, total-degree \(k\) multivariate
Hermites have the extensive eigenvalue \(b^{1-k/2}\) with multiplicity
\(\binom{d+k-1}{k}\).

**Proof.** The pair \((X_i,Z)\) is jointly standard Gaussian with correlation
\(b^{-1/2}\). The Hermite generating function, or coefficient comparison in
its Gaussian conditional expectation, gives
\(\mathbb E[e_k(X_i)\mid Z]=b^{-k/2}e_k(Z)\). Summing over \(i\) proves
(I5.2). Diagonal operator theory and Parseval give (I5.3)--(I5.4). \(\square\)

**Boundary.** The displayed spectrum depends on independent Gaussian inputs,
the equal-weight block, dimension, and the extensive normalization, not on an
unspecified network topology. For standard jointly Gaussian \((X,Z)\) with
correlation \(r\), the one-copy eigenvalue is \(r^k\); weighted replicas give
\(\sum_i c_ir_i^k\). Correlation, cancellation, or discarded graph modes can
create actual zero eigenvalues. No topology-dependent spectrum follows from
the scalar probe alone.

## G. Statistical bundles, anomalies, and descent

### Theorem G1 (connection-relative Fisher pullback)

For \(x\in\mathcal C\) and \(X,Y\in T_x\mathcal C\), define

\[
 h_s^\omega(X,Y)
 :=g^F_{s(x)}(D^\omega s(X),D^\omega s(Y)),
 \qquad D^\omega s=P^\omega\circ Ts.                               \tag{G1.1}
\]

This is a smooth positive-semidefinite base tensor. Under the convention
\(s^g=\rho(g)^{-1}s\) and
\(\omega^g=\operatorname{Ad}(g^{-1})\omega+g^{-1}dg\),

\[
 D^{\omega^g}s^g=T\rho(g)^{-1}\circ D^\omega s.                    \tag{G1.2}
\]

Therefore (G1.1) is gauge-invariant if, and only if on the tangent directions
used, the associated action is a Fisher isometry:

\[
 g^F_{\rho(g)^{-1}p}(T\rho(g)^{-1}u,T\rho(g)^{-1}v)=g^F_p(u,v).     \tag{G1.3}
\]

Without (G1.3), one has covariance with the transformed fiber metric, not a
gauge-independent scalar tensor. For a second connection \(\omega'\),

\[
 D^{\omega'}s=D^\omega s+(P^{\omega'}-P^\omega)Ts,                 \tag{G1.4}
\]

so the pullback is connection-relative.

In local trivializations, transition maps satisfy
\(g_{\alpha\beta}g_{\beta\gamma}=g_{\alpha\gamma}\) on triple overlaps, and
the local jets transform by (G1.2). The local tensors therefore glue exactly
when (G1.3) holds for every transition; a transition defect is an obstruction,
not a gauge choice.

If \(g^F\) is positive definite, then

\[
 \operatorname{rad}h_s^\omega=\ker D^\omega s,
 \qquad \operatorname{rank}h_s^\omega=\operatorname{rank}D^\omega s. \tag{G1.5}
\]

For a semidefinite fiber tensor, the radical is
\((D^\omega s)^{-1}(\operatorname{rad}g^F)\). A base Riemannian metric
requires injectivity of \(D^\omega s\). Inequivalent representations on
\(E^b\) and \(E^m\) supply no canonical fiber identification or metric
comparison.

**Proof.** Positivity is immediate from pullback. Equivariance of the
connection splitting gives (G1.2), after which (G1.3) is exactly the condition
that the scalar be unchanged. Equations (G1.4)--(G1.5) follow directly from
the definitions and positive definiteness. \(\square\)

**Boundary.** Regularity of each statistical fiber does not prove that the
chosen group representation acts by Fisher isometries, nor that the pullback
has full rank on the base.

### Theorem G2 (covariant-jet chain rule and anomaly cocycle)

For a bundle morphism \(\Psi:E_0\to E_1\) over \(f:C_0\to C_1\), let
\(L_\Psi=T^V\Psi:VE_0\to VE_1\). With source and target vertical projections
\(P_0,P_1\), define the **positive-sign horizontal anomaly**

\[
 \mathfrak A_\Psi:=P_1T\Psi-L_\Psi P_0:TE_0\to VE_1.               \tag{G2.1}
\]

It vanishes on vertical vectors and equals \(P_1T\Psi(I-P_0)\). If
\(\Psi\circ s=\bar s\circ f\), then

\[
 D^{\omega_1}\bar s\circ Tf
 =L_\Psi\circ D^{\omega_0}s+\mathfrak A_\Psi\circ Ts.              \tag{G2.2}
\]

For \(E_0\xrightarrow{\Psi}E_1\xrightarrow{\Phi}E_2\), the vertical maps
and anomalies compose in the order

\[
 L_{\Phi\circ\Psi}=L_\Phi\circ L_\Psi,
 \qquad
 \mathfrak A_{\Phi\circ\Psi}
 =\mathfrak A_\Phi\circ T\Psi+L_\Phi\circ\mathfrak A_\Psi.        \tag{G2.3}
\]

**Proof.** Apply \(P_1\) to
\(T\Psi Ts=T\bar s\,Tf\), split \(Ts=P_0Ts+(I-P_0)Ts\), and use
\(T\Psi|_{VE_0}=L_\Psi\), proving (G2.2). Expanding (G2.1) for the composite
and adding/subtracting \(L_\Phi P_1T\Psi\) proves (G2.3). \(\square\)

**Boundary.** Declaring a bundle map does not make it connection-preserving.
The chain rule without \(\mathfrak A_\Psi\) is valid exactly when the relevant
horizontal vectors are carried to target-horizontal vectors.

### Theorem G3 (vertical Fisher defect and full base comparison)

Suppose the fiber-law part of \(\Psi\) is a normalized
parameter-independent Markov map. If \(u,v\) are fine score tangents and
\(L u=\mathbb E[u\mid Y]\), then

\[
 \mathfrak D_K(u,v)
 :=g^F(u,v)-\bar g^F(Lu,Lv)
 =\mathbb E[(u-\mathbb E[u\mid Y])(v-\mathbb E[v\mid Y])].         \tag{G3.1}
\]

Thus \(\mathfrak D_K\succeq0\), and
\(\mathfrak D_K(u,u)=0\) exactly when \(u\) is determined by \(Y\) a.s.

For \(X\in T_xC_0\), put
\(u_X=D^{\omega_0}s(X)\) and
\(a_X=\mathfrak A_\Psi(TsX)\). Then the complete base formula is

\[
 (f^*h_{\bar s}^{\omega_1})(X,Y)
 =h_s^{\omega_0}(X,Y)-\mathfrak D_K(u_X,u_Y)
  +\bar g^F(Lu_X,a_Y)+\bar g^F(a_X,Lu_Y)+\bar g^F(a_X,a_Y).         \tag{G3.2}
\]

Accordingly, the exact necessary and sufficient pointwise criterion for base
Fisher contraction is

\[
 h_s^{\omega_0}-f^*h_{\bar s}^{\omega_1}\succeq0
 \iff
 \mathfrak D_K(u_X,u_X)
 \geq2\bar g^F(Lu_X,a_X)+\bar g^F(a_X,a_X)
 \quad\text{for every }X.                                         \tag{G3.3}
\]

If \(\mathfrak A_\Psi Ts=0\), contraction follows, with equality at the
chosen parameter exactly when every section-generated score is
coarse-measurable. This pointwise tangent equality does not imply global
sufficiency of the statistical experiment.

**Proof.** Equation (G3.1) is the \(L^2\) conditional-variance identity.
Insert (G2.2) into the target pullback metric, expand the square, and replace
\(\bar g^F(Lu,Lv)\) using (G3.1), giving (G3.2). A symmetric bilinear form is
positive semidefinite exactly when its quadratic values are nonnegative,
giving (G3.3). \(\square\)

**Counterexample.** Even with an identity fiber channel, so
\(\mathfrak D_K=0\), two different connections can give \(a_X\ne0\). Taking
locally \(a_X=u_X\ne0\) makes the target squared speed four times the source
squared speed. Vertical data processing alone therefore does not imply base
metric contraction.

### Theorem G4 (sharp global descent criterion)

Let \(t:=\Psi\circ s:C\to\bar E\), which covers \(f:C\to\bar C\). A global
smooth section \(\bar s:\bar C\to\bar E\) satisfying
\(t=\bar s\circ f\) exists if and only if all three conditions hold:

1. **fiber constancy:** \(f(c_1)=f(c_2)\Rightarrow t(c_1)=t(c_2)\);
2. the induced map \(u:f(C)\to\bar E\), \(u(f(c))=t(c)\), is smooth for the
   smooth structure carried by the image;
3. \(u\) extends to a smooth section on all of \(\bar C\).

If \(f\) is a surjective submersion, local smooth sections of \(f\) make
condition 2 automatic, condition 3 has no outside-image part, and fiber
constancy alone is necessary and sufficient. If \(f\) is not surjective, the
extension is separate and generally nonunique.

The infinitesimal condition

\[
 \ker Tf_c\subseteq\ker Tt_c                                      \tag{G4.1}
\]

is necessary, but in general not sufficient. It implies local constancy along
connected regular fiber components, not equality across disconnected
components, quotient smoothness, or extension.

**Proof.** Any factorization is constant on fibers and induces the stated
smooth extendable \(u\). Conversely the extension composed with \(f\) is
\(t\). For a surjective submersion, around every target point choose a local
section \(\sigma\); then \(u=t\circ\sigma\) is smooth and independent of the
choice by fiber constancy. Differentiating a factorization gives (G4.1).
\(\square\)

**Minimal counterexamples.** For the covering \(f:S^1\to S^1\),
\(f(z)=z^2\), take the trivial bundle \(\bar E=S^1\times\mathbb C\) and the
section along \(f\), \(t(z)=(z^2,z)\). Condition (G4.1) is vacuous, while
\(t\) does not descend because its values at \(z\) and \(-z\) differ. For the
inclusion \((0,1)\hookrightarrow\mathbb R\), the section along the inclusion
\(t(x)=(x,1/x)\) of the trivial real line bundle is fiber-constant but has no
smooth global extension.

### Theorem G5 (data required for a strong configuration metric)

Pointwise fiber or base tensors do not by themselves define a metric on a
configuration space. One sufficient finite-network construction is the
following. Let \(\mathcal M=\prod_{i=1}^nM_i\) be a declared smooth
configuration manifold, let \(h_i\) be smooth positive-definite metrics, and
let \(w_i:\mathcal M\to(0,\infty)\) be smooth. Then

\[
 G_q(v,w)=\sum_{i=1}^nw_i(q)h_{i,q_i}(v_i,w_i)                      \tag{G5.1}
\]

is a strong Riemannian metric in finite dimensions. Semidefinite \(h_i\), zero
weights, or missing tangent-manifold structure prevent this conclusion.

For a coarse map \(R:\mathcal M\to\bar{\mathcal M}\), a selected smooth
right inverse \(r:\bar{\mathcal M}\to\mathcal M\), \(Rr=\operatorname{Id}\),
defines

\[
 \bar G_{\bar q}(u,v):=G_{r(\bar q)}(Tr\,u,Tr\,v).                  \tag{G5.2}
\]

Without \(r\), or an equivalent horizontal-lift rule, (G5.2) is multivalued.
Two different right inverses \(r,r'\) induce the same metric exactly when the
two right sides of (G5.2) agree for every \(\bar q,u,v\); distinct lifts can
indeed agree. For example, for \(R(x,y)=x\) with the Euclidean metric, the
lifts \(r_\pm(x)=(x,\pm x)\) both induce \(2\,dx^2\).

For a gauge quotient, direct tensor descent requires a smooth quotient and a
basic tensor: gauge invariance plus annihilation of vertical fundamental
directions. It is nondegenerate on the quotient exactly when the source
radical equals the gauge-vertical distribution. Alternatively, if a group
acts freely, properly, and isometrically on a positive-definite configuration
metric, a declared invariant horizontal complement defines the quotient
metric by horizontal lifts. Gauge fixing without these facts is insufficient.

**Proof.** Positivity of the finite weighted sum proves (G5.1). Pullback by a
right inverse proves (G5.2). Basic-tensor descent and the radical criterion
follow by checking independence of representatives and lifts. \(\square\)

**Boundary.** Standard-Borel state spaces alone carry no tangent bundles, and
finite network size alone does not make an infinite-dimensional weak metric
strong. The manifold, regularity, and musical-isomorphism data must be declared.

## H. Histories and duration without primitive time

### Theorem H1 (typed curve classification)

Let \(J\subset\mathbb R\) be only an oriented parameter interval.

* A fixed-fiber curve \(\gamma:J\to E_x\) is vertical.
* A total-space curve \(e:J\to E\), over \(c=\pi_Ee\), is vertical when
  \(\dot c=0\), connection-horizontal when \(P^\omega\dot e=0\), mixed when
  both horizontal and vertical components are nonzero, and stationary when
  \(\dot e=0\).
* A base curve \(c:J\to\mathcal C\) has no vertical/horizontal label until a
  lift and connection are chosen.
* A curve of sections \(\sigma:J\to\Gamma(E)\) yields a vertical curve
  \(\lambda\mapsto\sigma_\lambda(x)\in E_x\) only after fixing \(x\). Along a
  moving base point,
  \(\frac d{d\lambda}\sigma_\lambda(c(\lambda))
  =\partial_\lambda\sigma_\lambda(c(\lambda))+T\sigma_\lambda\dot c\).
* On a declared strong Riemannian configuration manifold \((\mathcal M,G)\),
  a differentiable VFE \(\mathcal F\) defines
  \(X=-\operatorname{grad}_G\mathcal F\); its integral curves satisfy
  \(\dot q=X(q)\) and are stationary at \(X=0\).

These are geometric classifications. None turns \(\lambda\) into physical
time. A horizontal curve can move in the base while having zero covariant
vertical belief velocity.

**Proof.** Each classification follows by applying \(T\pi_E\) and the direct
splitting \(TE=HE^\omega\oplus VE\), or by evaluating a section at a fixed
base point. The natural-gradient statement is the defining metric-dual
identity \(G(\operatorname{grad}_G\mathcal F,\cdot)=d\mathcal F\). \(\square\)

**Boundary.** Endpoints do not determine whether a lift was vertical,
horizontal, or mixed, and a curve in section space is not a fixed-fiber curve
until an evaluation point is selected.

### Theorem H2 (oriented coarse-orbit criterion)

Let \(q:I\to\mathcal M_\ell\) be a maximal integral curve of \(X_\ell\), let
\(R=\mathsf R_\ell\) be smooth along it, and set \(y=R\circ q\). On an open
subinterval \(I_0\subseteq I\), assume the coarse vector field has local
uniqueness. Then \(y\) is a positively reparameterized integral
curve of \(X_{\ell+1}\) if and only if there is a continuous function
\(a:I_0\to(0,\infty)\) such that

\[
 TR_{q(t)}X_\ell(q(t))=a(t)X_{\ell+1}(R(q(t)))                      \tag{H2.1}
\]

and \(\tau(t)=\tau_0+\int_{t_0}^ta(u)du\) has image inside the relevant
maximal coarse interval. It covers the entire maximal coarse orbit exactly
when \(\tau(I_0)\) is that maximal interval.

At a noncritical coarse point, \(a\) is unique and (H2.1) says the two tangent
vectors lie on the same oriented ray. If \(X_{\ell+1}(y)=0\), compatibility
requires \(TRX_\ell=0\); uniqueness of the coarse ODE then makes the image
stationary on its connected orbit interval and leaves \(a\) unidentifiable.
If \(TRX_\ell=0\) while \(X_{\ell+1}\ne0\), coarse collapse makes positive
reparameterization impossible. Negative proportionality reverses orientation;
a zero proportionality factor gives a pause, not a positive reparameterization.

**Proof.** If \(y(t)=\bar q(\tau(t))\), the chain rule gives (H2.1) with
\(a=\tau'>0\). Conversely, positive \(a\) makes \(\tau\) invertible on its
image, and
\(d(y\circ\tau^{-1})/d\tau=X_{\ell+1}(y\circ\tau^{-1})\). Standard local
uniqueness handles critical points and maximal intervals. \(\square\)

**Boundary.** Dropping strict positivity permits pauses and a noninvertible
parameter change. Dropping local uniqueness allows several coarse integral
curves through one critical point, so the critical-point conclusion need not
hold.

### Theorem H3 (when natural gradients semiconjugate)

Let \(R:(\mathcal M,G)\to(\bar{\mathcal M},\bar G)\) be smooth between
strong Riemannian manifolds and let
\(\mathcal F=\bar{\mathcal F}\circ R+c\). For this objective, exact
natural-gradient intertwining is equivalent to

\[
 TR\,G^\sharp TR^*(d\bar{\mathcal F})
 =\bar G^\sharp(d\bar{\mathcal F})\circ R.                         \tag{H3.1}
\]

For every compatible objective, the necessary and sufficient geometric
condition is the cometric identity

\[
 TR\,G^\sharp TR^*=\bar G^\sharp.                                  \tag{H3.2}
\]

A sufficient concrete hypothesis is that \(R\) is a surjective Riemannian
submersion: \(TR\) restricts to an isometry from
\((\ker TR)^{\perp_G}\) onto the target tangent space. If the vector fields
are regular enough for unique flows, then

\[
 TR\,X=X_{\rm coarse}\circ R,
 \qquad
 R\circ\Phi_t=\bar\Phi_t\circ R                                    \tag{H3.3}
\]

whenever both sides are defined.

**Proof.** Pullback compatibility gives
\(d\mathcal F=TR^*d\bar{\mathcal F}\). Applying the two musical inverses and
then \(TR\) proves (H3.1); requiring it for all covectors gives (H3.2). The
horizontal-lift characterization of a Riemannian submersion proves (H3.2).
Uniqueness of integral curves proves (H3.3). \(\square\)

**Counterexample.** Take \(R=\operatorname{Id}_{\mathbb R^2}\) and the same
objective \(\mathcal F(x,y)=x\) on both sides. Use the Euclidean coarse metric
but a fine positive-definite cometric sending \(dx\) to
\(\partial_x+\tfrac12\partial_y\). The two negative gradients are not even
colinear. Objective compatibility alone gives neither (H2.1) nor
semiconjugacy.

### Theorem H4 (Fisher arc duration and its exact boundary)

For an absolutely continuous curve \(q:J\to\mathcal M\) in a regular Fisher
stratum, or a fixed-fiber curve with its fiber Fisher metric, define

\[
 v_F(\lambda)=\sqrt{G_{q(\lambda)}(\dot q,\dot q)},
 \qquad
 \tau_F(\lambda)=\tau_0+\int_{\lambda_0}^{\lambda}v_F(u)du.         \tag{H4.1}
\]

For a section-induced base curve, use
\(G=h_s^\omega\); its duration is then connection-relative. The accumulated
length is invariant under regular orientation-preserving reparameterization
and nondecreasing. It is strictly increasing exactly when every nontrivial
subinterval has positive accumulated length. If \(q\) is \(C^1\) and
\(v_F>0\) everywhere, \(\tau_F\) is a regular arc-length coordinate.

A zero-speed interval destroys strict increase. An isolated zero can preserve
strict increase but destroys regular invertibility there. Semimetric-null
motion has zero duration. A closed history can return to the same state with a
larger \(\tau_F\), so \(\tau_F\) is not a single-valued state function or a
global clock. It supplies no orientation until one is selected, no
synchronization between different histories, no causal structure, and no
operational clock reading. It is distinct from the discrete scale depth
\(\ell\) and from physical time; either identification needs an additional
operational bridge. A global clock potential further requires a declared
closed clock one-form with zero periods (and hence exactness on the region).

**Proof.** Change of variables proves reparameterization invariance. The
strictness and regularity statements are the fundamental theorem of calculus
and the inverse-function theorem. The closed-loop observation proves failure
of a state function. \(\square\)

**Boundary.** A singular-stratum crossing is outside this smooth-stratum
theorem unless the pathwise metric speed is separately shown to extend
finitely and with the required positivity.

## R. Exact finite nonautonomous scale theory

### Theorem R1 (ordered nonlinear and derivative cocycles)

For integers \(m<n\), define

\[
 F_{n\leftarrow m}:=F_{n-1}\circ\cdots\circ F_m,
 \qquad F_{m\leftarrow m}=\operatorname{Id}_{Y_m}.                  \tag{R1.1}
\]

Then, for \(m\leq n\leq p\),

\[
 F_{p\leftarrow m}=F_{p\leftarrow n}\circ F_{n\leftarrow m}.      \tag{R1.2}
\]

Along \(y_{\ell+1}=F_\ell(y_\ell)\), with
\(M_\ell=DF_\ell(y_\ell)\),

\[
 M_{n\leftarrow m}:=M_{n-1}\cdots M_m
 =D F_{n\leftarrow m}(y_m),
 \qquad
 M_{p\leftarrow m}=M_{p\leftarrow n}M_{n\leftarrow m}.            \tag{R1.3}
\]

If compatible one-dimensional subspaces have selected nonzero frames
\(v_\ell\) satisfying \(M_\ell v_\ell=\mu_\ell v_{\ell+1}\), then

\[
 M_{n\leftarrow m}v_m
 =\left(\prod_{k=m}^{n-1}\mu_k\right)v_n.                          \tag{R1.4}
\]

Under a frame change \(v_\ell'=a_\ell v_\ell\),
\(\mu_\ell'=(a_\ell/a_{\ell+1})\mu_\ell\), so only endpoint-controlled
products are meaningful without fixed normalization. A zero multiplier
collapses the line; positive multipliers preserve its selected orientation.

**Proof.** Equations (R1.2)--(R1.4) are associativity and the chain rule in the
displayed order. \(\square\)

**Boundary.** Spectra and vector subtraction remain undefined before the
different tangent spaces are identified. A multiplier depends on the selected
line frames even though its zero/nonzero status does not.

### Theorem R2 (exact and retained beta data, residual, and scheme law)

Assume \(Y_*\) and the \(Y_\ell\) are normed linear spaces (or fixed affine
charts with declared differences), with bounded isomorphisms
\(J_\ell:Y_*\to Y_\ell\), and put \(x_\ell=J_\ell^{-1}y_\ell\). The exact
discrete state and tangent beta data are

\[
 \beta_\ell^{\rm ex}(x_\ell)
 :=\frac{J_{\ell+1}^{-1}F_\ell(J_\ell x_\ell)-x_\ell}{\Delta s_\ell},
                                                                    \tag{R2.1}
\]
\[
 \mathcal B_\ell^{\rm ex}
 :=\frac{J_{\ell+1}^{-1}M_\ell J_\ell-I}{\Delta s_\ell}.          \tag{R2.2}
\]

Let \(\iota_\ell:T_\ell\hookrightarrow Y_\ell\) and
\(Q_\ell:Y_\ell\to T_\ell\) satisfy \(Q_\ell\iota_\ell=I\). For
\(t_\ell\in T_\ell\), set

\[
 y_{\ell+1}^{\rm ex}=F_\ell(\iota_\ell t_\ell),\quad
 t_{\ell+1}=Q_{\ell+1}y_{\ell+1}^{\rm ex},\quad
 \epsilon_\ell=y_{\ell+1}^{\rm ex}-\iota_{\ell+1}t_{\ell+1}.    \tag{R2.3}
\]

Set \(x_\ell=J_\ell^{-1}\iota_\ell t_\ell\). Defining
\(\beta^{\rm ret}\) by replacing the exact next state in (R2.1) with
\(\iota_{\ell+1}t_{\ell+1}\), one has the exact residual law

\[
 \beta_\ell^{\rm ex}-\beta_\ell^{\rm ret}
 =\frac{J_{\ell+1}^{-1}\epsilon_\ell}{\Delta s_\ell}.             \tag{R2.4}
\]

For another reference \(\widetilde J_\ell=J_\ell A_\ell\), where each
\(A_\ell:Y_*\to Y_*\) is a bounded isomorphism,

\[
 \widetilde\beta_\ell
 =A_{\ell+1}^{-1}\beta_\ell
  +\frac{(A_{\ell+1}^{-1}-A_\ell^{-1})x_\ell}{\Delta s_\ell},     \tag{R2.5}
\]
\[
 I+\Delta s_\ell\widetilde{\mathcal B}_\ell
 =A_{\ell+1}^{-1}(I+\Delta s_\ell\mathcal B_\ell)A_\ell,        \tag{R2.6}
\]
\[
 \widetilde\epsilon_\ell^*=A_{\ell+1}^{-1}\epsilon_\ell^*.
                                                                    \tag{R2.7}
\]

Here \(\epsilon_\ell^*:=J_{\ell+1}^{-1}\epsilon_\ell\) and
\(\widetilde\epsilon_\ell^*:=\widetilde J_{\ell+1}^{-1}\epsilon_\ell\).

Thus a scale-dependent reference contributes the inhomogeneous second term in
(R2.5). Only a scale-independent \(A\) gives ordinary conjugation for tangent
data. Beta components and residual norms are scheme-dependent; controlled
two-sided norms on \(J_\ell,A_\ell\) give corresponding error bounds.

**Proof.** Substitute (R2.3) into the two finite differences for (R2.4).
Since \(\widetilde x_\ell=A_\ell^{-1}x_\ell\), direct substitution gives
(R2.5)--(R2.7). \(\square\)

**Boundary.** A lossy reference map is not an isomorphism and cannot be used
in (R2.1)--(R2.7) without carrying its kernel and a reconstruction error.

### Theorem R3 (nonautonomous fixed objects)

Across unequal spaces, the exact invariant object is a coherent orbit or
section

\[
 y_{\ell+1}=F_\ell(y_\ell),                                        \tag{R3.1}
\]

or, for laws, a coherent family
\(\mu_{\ell+1}=(F_\ell)_\#\mu_\ell\). With reference isomorphisms, define
\(\widetilde F_\ell=J_{\ell+1}^{-1}F_\ell J_\ell:Y_*\to Y_*\). A
constant \(x_*\) is an identified common fixed point only if

\[
 \widetilde F_\ell(x_*)=x_*\quad\text{for every relevant }\ell.   \tag{R3.2}
\]

This condition depends on the chosen identifications.

If \(\widetilde F_{\ell+p}=\widetilde F_\ell\), the monodromy

\[
 \mathcal P_\ell
 :=\widetilde F_{\ell+p-1}\circ\cdots\circ\widetilde F_\ell       \tag{R3.3}
\]

acts on one space. Its fixed points correspond exactly to \(p\)-periodic
orbits, and stability is governed by \(D\mathcal P_\ell\), not by a spectrum
of one map between unequal spaces. A one-step fixed point is meaningful only
for a literal endomorphism, a declared identification producing one, an
autonomous repeated map, or the common-fixed-point condition (R3.2).

**Proof.** Iterating (R3.1) proves coherence. Periodic composition returns to
the same comparison space, so fixed points of (R3.3) and periodic sequences
determine one another. \(\square\)

**Boundary.** A fixed point of one member of a periodic sequence need not be a
fixed point of the monodromy or define a periodic orbit. Changing the
identifications can also change whether a constant representative satisfies
(R3.2).

### Theorem R4 (finite exact closure and generated interactions)

At every finite level, the full interaction space of Theorem I1 is exactly
closed under the bounded action map: the coarse bounded action has one unique
constant plus all nonempty-subset interactions. This is **full-space closure**,
not sparse closure. Any retained family \(T_\ell\) is exact only under (I3.3);
otherwise the omitted term is the typed residual (I3.1).

Marginalization generically creates allowed higher-body interactions. For a
minimal explicit mechanism, take visible spins \(x_1,x_2,x_3\in\{-1,1\}\), a
hidden spin \(u\), a nonzero hidden field \(a\), and fine pair couplings
\(uJ_ix_i\). Summing out \(u\) contributes

\[
 H_{\rm eff}(x)=-\log\!\left[2\cosh\!\left(a+\sum_{i=1}^3J_ix_i\right)\right]. \tag{R4.1}
\]

Its Walsh expansion has a three-body coefficient that, for small \(J_i\), is

\[
 -\frac{d^3}{da^3}\log(2\cosh a)\,J_1J_2J_3+O(\|J\|^5),           \tag{R4.2}
\]

which is nonzero generically when \(a\ne0\) and every \(J_i\ne0\). Hence a
pairwise ansatz is not automatically closed. Boundary, nonlocal, normalization,
and entropy terms are likewise components of the full coarse action and may
not be discarded.

**Proof.** Boundedness in P1 and the isomorphism I1 prove full-space closure.
The hidden-spin sum gives (R4.1); Taylor expansion and the term
\(6J_1J_2J_3x_1x_2x_3\) in \((\sum_iJ_ix_i)^3\) give (R4.2). \(\square\)

### Theorem R5 (the exact finite/universal boundary)

The preceding results prove finite-network identities at declared scales. They
do not imply any of the following:

1. **Infinite volume.** One needs an exhaustion or projective system of
   networks, compatible boundary conditions, existence/tightness of limiting
   laws, stability and uniform integrability of energies, control of partition
   functions or free-energy densities, and justified interchange of the
   limit with conditioning, differentiation, and coarse-graining. Uniqueness
   or phase coexistence must be proved separately.
2. **Criticality and universal exponents.** One needs an infinite-volume or
   other genuine scaling limit, a critical object with divergent scale, an RG
   fixed point or invariant family in an appropriate complete operator space,
   differentiability and spectral control after quotienting redundant
   directions, and a basin/universality-class theorem. A finite residual or a
   finite Hermite spectrum does not supply these facts.
3. **Continuous scale.** One needs an embedding of the discrete cocycle into a
   strongly continuous semigroup or nonautonomous evolution family and a
   generator domain. Not every discrete map has such an embedding or a
   logarithm.
4. **Scheme-independent universality.** One needs an admissible class of
   regular invertible reference/coupling changes that conjugate the limiting
   dynamics. Equation (R2.5) shows that raw finite beta components are not
   invariant. Only quantities proved invariant under that class, such as
   spectra under a genuine differentiable conjugacy, may be called universal.

These are missing hypotheses, not small-error consequences of finiteness.

**Proof.** The finite identities contain no quantified limiting family, so
none can establish existence or uniqueness of a limit. The same finite prefix
of a scale diagram can be continued by identity maps, contractions, or
expansions with different asymptotics. Likewise the real one-dimensional map
\(x\mapsto-x\) cannot be the time-one map of a one-dimensional continuous
flow, whose time maps preserve orientation, showing that discrete evolution
does not imply embeddability. Finally (R2.5) explicitly changes finite beta
components under a scale-dependent reference. These countermodels preserve
all finite premises while changing the proposed conclusions. \(\square\)

**Boundary.** The listed conditions are necessary categories of data, not a
claim that any one generic list is sufficient for every infinite-volume model;
the exact tightness, topology, and regularity conditions are model-dependent.

## Finite conditional assembly and exact verdict

The packet supports a complete **finite conditional construction** in the
following precise sense. For every declared finite level and every declared
kernel, reference, interaction extraction, connection, bundle morphism,
configuration map, and comparison isomorphism satisfying the hypotheses stated
above, the construction has:

\[
\begin{array}{c}
\text{exact mass and RN action with composition}\\
\Downarrow\\
\text{extended ELBO, conditional-agent law, and DQM/Fisher contraction}\\
\Downarrow\\
\text{unique full interactions = retained part + explicit residual}\\
\Downarrow\\
\text{bundle jet = vertical pushforward + explicit horizontal anomaly}\\
\Downarrow\\
\text{ordered scale cocycle with reference-typed beta and fixed objects.}
\end{array}                                                        \tag{V.1}
\]

No normalization, interaction, Fisher-loss, anomaly, or truncation term is
left implicit in this finite chain. The following stronger statements are
either refuted above or not inferable from the primitives:

* equivalence to a product reference, sparse/product interaction closure, or
  factorization of observation channels;
* existence or smoothness of a configuration coarse map, a global descended
  section, a right-inverse lift, or a nondegenerate gauge quotient;
* natural-gradient semiconjugacy from objective compatibility alone;
* removal of conditioning by renaming an observation as an agent;
* a physical or global time coordinate from Fisher arc length;
* an ordinary fixed point for a genuinely nonautonomous unequal-space diagram;
* infinite-volume existence, criticality, universal exponents, continuous
  scale interpolation, or scheme-independent universality.

The explicit additional obligations include the conditions named in
P5.2--P5.3, I3.3, G1.3, G2.1--G2.3, G3.3, G4, G5, H2.1, H3.1--H3.2, and R5.
None is supplied merely by finite size or by the existence of the other
layers.

**Terminal verdict: `COMPLETE_AFFIRMATIVE` for the packet-scoped finite
conditional theorem package.** This verdict does not extend to any of the
listed stronger statements. If "complete" is instead taken to mean an
unconditional physical theory, a product-closed truncation, an existing
configuration dynamics, or a universal/infinite-volume RG theory, the packet
does not determine such a claim; those meanings are outside this terminal
verdict and remain unproved until the named bridge hypotheses are supplied.

## Oracle-erasure falsification check

The derivation uses only the primitive typed data plus hypotheses written at
the exact theorem where they enter. Erasing every desired conclusion from the
logical context leaves each proof unchanged. The principal attacks and their
dispositions are:

| Attack | Disposition | Decisive derivation |
|---|---|---|
| RN actions may depend on null-set versions | Rejected for a.e. claims; sustained for selected null slices | P1 |
| Normalized action remains concave | Rejected | P2.5--P2.6 |
| Nondominated singular mass can be ignored without accounting | Rejected | P3.4--P3.6 |
| Local ELBOs sum to the collective objective | Rejected | P4.5 and correlated-bit counterexample |
| Pairwise observation messages are complete | Rejected | P5 XOR counterexample |
| Equivalent reference implies product interaction calculus | Rejected | I1 correlated-projection counterexample |
| Retained projection is exact by idempotence | Rejected | I3.3 and R4 |
| Fisher data processing implies base-metric contraction | Rejected | G3.2--G3.3 |
| Infinitesimal descent implies global descent | Rejected | G4 covering counterexample |
| Compatible objectives imply semiconjugacy | Rejected | H3 counterexample |
| Arc length is a global physical clock | Rejected | H4 closed-history argument |
| Finite exact RG establishes universality | Rejected | R2.5 and R5 |

The affirmative finite verdict depends on the displayed direct derivations,
not on a hidden theorem statement, another model's agreement, numerical
testing, or any erased source.
