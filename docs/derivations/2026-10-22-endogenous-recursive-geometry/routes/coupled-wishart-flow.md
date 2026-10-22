<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","schema_version":"rigorous-theory-search/v1","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->
# Exact coupled Wishart flow and aggregation

The proposed law-dependent reference channel gives a genuinely coupled original Fisher flow. Its full channel derivative is nonzero and is retained below. On the declared common-precision Wishart family, addition of independent represented matrices gives exact parent laws, exact original-time parent Fisher dynamics, and associative normalized parent channels. The fine potential is not constant on the compression fibers. The result is an invariant-family construction; it does not establish selection of that family or of a hierarchy.

## Scope, law model, and regularity

This derivation uses the original potential and gradient convention of `manuscripts/MAgent_Theory_2.0/chapters/03_dynamics.tex`, the full channel differential there, and the exact response construction in `routes/wishart-response.md`. It is the final bounded constructive route under the frozen contract, not a new audit or verification panel.

Let `X` range over the standard Borel cone `S_2^{++}` of real symmetric positive-definite matrices, with Lebesgue measure on its three independent entries. Write

\[
 w_{a,P}(X)=\frac{\det(P)^a}{\Gamma_2(a)}\det(X)^{a-3/2}
             e^{-\operatorname{tr}(PX)},\qquad
 \Gamma_2(a)=\sqrt\pi\Gamma(a)\Gamma(a-1/2),
 \quad a>1/2,\quad P\succ0.
\]

The normalization, finite exponential moments around each regular parameter point, and convolution identity are derived in `wishart-response.md`. In particular,

\[
 \mathbb E_{W_2(a,P)}X=aP^{-1},\qquad
 W_2(a,P)*W_2(b,P)=W_2(a+b,P),
\]

where the convolution is the pushforward of independent samples by fixed matrix addition. These are distributions of represented contents; no distribution over configurations is introduced.

Fix a finite primitive population of size `N`, `alpha_0>1/2`, and `kappa>0`. A configuration consists initially of arbitrary normalized belief laws `q_i` with positive densities and finite first moments. Define

\[
 M=\sum_{i=1}^N\int Xq_i(dX),\qquad k=\kappa/N,
 \qquad \Lambda(M)=I+kM.
\]

Finite first moments make this well-defined. Since `M` is positive definite for laws supported on this open cone, `Lambda` is positive definite. Take the proper belief reference `A_0=W_2(alpha_0,I)` and prescribe every comparison channel by

\[
 \mathcal K^q_{ij}[\mathbf q](x,dX)=W_2(\alpha_0,\Lambda(M))(dX)=:\nu_M(dX).
\]

The channel is normalized for every admitted configuration. It ignores the sender's sample but reads the current aggregate law moment; this is a constitutive feedback interaction. It has no time gate and no change at a join. Use all source labels, including the receiver label, with original priors `pi_ij=1/N` and any fixed temperature `T_q>0`. The self channel here is explicitly this nonidentity channel; no identity-self zero-cost convention is invoked.

For the model sector repeat the construction with `s_i`, reference shape `beta_0>1/2`, moment `M_s`, precision `Lambda_s=I+kappa_s M_s/N`, and fixed `kappa_s>0`. The local joint reference is the proper product `A_0 tensor B_0`, with constant normalized evaluator `G(m,dX)=A_0(dX)`. Both sectors have population coupling through their respective channels. They do not have an additional cross-sector evaluator coupling in this specialization.

To define the potential beyond the Wishart family, require the displayed local and peer relative entropies to be finite. For the expanded differential below, additionally require integrability of `log q_i`, `log det X`, and `tr X`, and differentiation under the displayed integrals along the admitted paths. On compact Wishart parameter neighborhoods with shape strictly above `1/2` and precision eigenvalues bounded above and away from zero, all these conditions and square-integrability of the scores follow from the small exponential-moment perturbations in shape and precision. The exact aggregation theorem below is for this regular invariant family, not for every finite-moment probability law.

## Source reduction and complete channel variation

For any sender `j`, normalization gives `q_j K_ij=nu_M`. Thus the original receiver cost is independent of the source label:

\[
 D_{ij}=D_i=\int\log\frac{dq_i}{d\nu_M}dq_i.
\]

For each normalized source row `b_i`, its original row energy is `D_i+T_q KL(b_i||pi_i)`. The exact Gibbs optimizer is therefore the original prior `b_i^*=pi_i`, and the reduced matter potential is exactly

\[
 E_q(\mathbf q)=\sum_i\left[
       \int\log\frac{dq_i}{dA_0}dq_i+
       \int\log\frac{dq_i}{d\nu_M}dq_i\right].
\]

The full potential is `E_q+E_s`. This uses the contract's permitted exact Gibbs reduction; the original temperatures remain positive. If dynamic rows were used instead, their row entropy dynamics would be another state component. They are not silently discarded here.

For mass-preserving law variations, the direct sender term is zero because the channel is constant in its input sample:

\[
 (dq_j)\mathcal K_{ij}=(\int dq_j)\nu_M=0.
\]

The channel derivative is not zero. Writing `dLambda=k dM`, differentiation of its normalized density gives

\[
 d\log w_{\alpha_0,\Lambda}(X)
 =\alpha_0\operatorname{tr}(\Lambda^{-1}d\Lambda)
       -\operatorname{tr}(d\Lambda X),
\]

whose mean under `nu_M` is zero because `E_nu X=alpha_0 Lambda^{-1}`. Consequently

\[
 d(q_j\mathcal K_{ij})=q_jD\mathcal K_{ij}=d\nu_M.
\]

This is the complete compared-law derivative. Every agent affects every compared law through its contribution to `M`. Freezing `Lambda` would remove this term and produce a different dynamics.

## Full density Fisher force

Set `c_0=alpha_0-3/2`. Expanding the two expectation terms, including all normalizers, gives

\[
 E_q=2\sum_i\int q_i\log q_i dX
 -2c_0\sum_i\int\log\det(X)q_i(dX)
 +\operatorname{tr}M+\operatorname{tr}(\Lambda M)
 -N\alpha_0\log\det\Lambda+2N\log\Gamma_2(\alpha_0).
\]

The final gamma term is constant under the matter variation. It is not dropped while changing the reference shapes below; the corresponding parent constants are supplied by their own normalized references.

Since `dLambda=k dM`, the moment-dependent differential is

\[
 \begin{aligned}
 d\{\operatorname{tr}(\Lambda M)-N\alpha_0\log\det\Lambda\}
 &=\operatorname{tr}(\Lambda dM)
   +\operatorname{tr}[(M-N\alpha_0\Lambda^{-1})d\Lambda]\\
 &=\operatorname{tr}(C(M)dM),\\
 C(M)&=\Lambda+k(M-N\alpha_0\Lambda^{-1})
       =I+2kM-\kappa\alpha_0\Lambda^{-1}.
 \end{aligned}
\]

Thus, up to a scalar constant irrelevant on the normalized tangent space, the complete variational derivative is

\[
 h_i(X)=2\log q_i(X)-2c_0\log\det X
             +\operatorname{tr}[(I+C(M))X].
\]

With the unit Fisher metric, the actual original flow is

\[
 \dot q_i=-q_i\left(h_i-\int h_i dq_i\right).
\]

Indeed, a mass-preserving tangent `v_i` pairs with the centered Fisher gradient as `int h_i dv_i`; this proves the gradient identification on the regular score domain. The part of the force absent from a frozen-channel calculation is precisely

\[
 \operatorname{tr}\{k(M-N\alpha_0\Lambda^{-1})X\}
\]

before centering. The calculations include this term throughout.

## Mutual coupling is nonzero

For a symmetric moment perturbation `H`, direct differentiation gives

\[
 DC_M[H]=\frac{2\kappa}{N}H
       +\frac{\kappa^2\alpha_0}{N}\Lambda^{-1}H\Lambda^{-1}.
\]

For different agents `i` and `j`, choose regular mass-preserving variations with moment derivatives `H_i,H_j`. Their mixed second variation of the potential is

\[
 d_i d_j E_q=
 \frac{2\kappa}{N}\operatorname{tr}(H_iH_j)
 +\frac{\kappa^2\alpha_0}{N}
       \operatorname{tr}(H_i\Lambda^{-1}H_j\Lambda^{-1}).
\]

Taking `H_i=H_j=H!=0` makes this strictly positive: the first trace is the squared Frobenius norm, and the second is the squared Frobenius norm of `Lambda^{-1/2} H Lambda^{-1/2}`. Such moment variations occur inside regular Wishart families. For example, varying only the shape of agent `j` at a common precision gives `H_j=P^{-1} delta alpha_j`.

Holding `q_i` fixed and varying agent `j` changes its instantaneous velocity by

\[
 d_j\dot q_i(X)=-q_i(X)\operatorname{tr}
       \left(DC_M[H_j](X-\mathbb E_{q_i}X)\right).
\]

For `H_j=P^{-1} delta alpha_j!=0`, the matrix `DC_M[H_j]` is nonzero. A Wishart law has a positive density on the open cone, so a nonzero linear matrix functional is not almost surely constant; the displayed velocity change is nonzero. This establishes actual cross-agent influence, rather than merely renaming a frozen common target. The source channel still transmits no sender sample; the coupling is through the declared law dependence.

## Exact invariant family and global positive solution

Take `q_i=W_2(alpha_i,P_i)` initially. Substituting its log density into the complete force gives

\[
 h_i(X)=2(\alpha_i-\alpha_0)\log\det X
       +\operatorname{tr}[(I+C(M)-2P_i)X]+\text{constant}.
\]

Comparison with the tangent log density `dot alpha_i log det X-tr(dot P_i X)+normalizer` yields the exact equations

\[
 \dot\alpha_i=-2(\alpha_i-\alpha_0),\qquad
 \dot P_i=-2P_i+I+C(M),\qquad
 M=\sum_i\alpha_iP_i^{-1}.
\]

The variable log-determinant and linear-matrix statistics are independent modulo constants on the open cone, so these coefficient equations are forced. Their normalizing scalar agrees automatically by differentiation of unit mass. They are the unrestricted density Fisher velocity evaluated on this family, not a parameter-gradient approximation.

In particular, `d(P_i-P_j)/dt=-2(P_i-P_j)`. Therefore an initially common precision remains common; it is not first reached at a finite positive time from unequal precisions. The construction assumes common precision in its preparation class and does not claim that the flow selects it.

On the common-precision family put `A=sum_i alpha_i`, `a=A/N`. Then

\[
 \dot a=-2(a-\alpha_0),\qquad M=A P^{-1},\qquad
 \dot P=-2P+2I+2\kappa aP^{-1}
            -\kappa\alpha_0(I+\kappa aP^{-1})^{-1}.
\]

This proves local closure by a smooth finite-dimensional ODE on `a>1/2,P positive`. It also gives global positive existence. To check this, set `a_-=min(a(0),alpha_0)>1/2` and `a_+=max(a(0),alpha_0)`. The right side for `P` is a matrix function of `P`, so diagonalizing the initial `P` reduces the equation to the same fixed eigenbasis, with each positive eigenvalue obeying

\[
 \dot p=-2p+2+\frac{2\kappa a(t)}p
               -\frac{\kappa\alpha_0}{1+\kappa a(t)/p}.
\]

Let `delta=min(1/2,a_-/alpha_0)` and `R=2+kappa a_+`. If `0<p<=delta`, then `2 kappa a(t)/p>=2 kappa alpha_0` and the negative last term is at least `-kappa alpha_0`; hence `dot p>=1+kappa alpha_0>0`. If `p>=R`, then `p>=1` and dropping the last negative term gives `dot p<=-2p+2+2 kappa a_+<=-2`. Every eigenvalue consequently stays between `min(p(0),delta)` and `max(p(0),R)`. The shape parameters remain between their initial values and `alpha_0`, all strictly above `1/2`. The vector field remains smooth on the resulting compact parameter set, so the local solution continues for all `t>=0`.

The same proof applies to the model sector. The score moments and differentiation bounds stay finite on these compact sets. A regular full-density solution with Wishart initial data also remains in this family: integrate its log-density equation with factor `exp(2t)`; its only sample-dependent terms are the initial log density, `log det X`, and a time-dependent linear functional of `X`. Normalization fixes the scalar. Its parameters therefore satisfy the same locally unique ODE. This supplies uniqueness in that positive dominated regular solution class.

## Normalized comparison channels after aggregation

For a current disjoint block `I`, retain `n_I=|I|`, `A_I=sum_{i in I}alpha_i`, and the common `P`; define its law by a fresh independent extensive response,

\[
 Q_I=\operatorname{Law}\left(\sum_{i\in I}X_i\right)=W_2(A_I,P),
 \qquad X_i\text{ independently distributed as }q_i.
\]

Keep the primitive total `N=sum_I n_I` fixed. It is not replaced by the number of current parents. Its total moment is exactly

\[
 M_c=\sum_I\mathbb E_{Q_I}S_I
     =\sum_I A_IP^{-1}=M.
\]

For each receiver block use local reference `A_{I,0}=W_2(n_I alpha_0,I)` and comparison kernel

\[
 \mathcal K^c_{IJ}(S_J,dS_I)=W_2(n_I\alpha_0,\Lambda(M_c))(dS_I).
\]

This is normalized and is exactly the sum-pushforward of `n_I` independent primitive channel outputs `W_2(alpha_0,Lambda)`. Independence of these channel draws is explicitly part of this joint receiver experiment. Because all primitive channels ignore the source sample, the comparison square with sender sum-retention commutes: both paths produce this same receiver law independently of the supplied sender content. No source distribution was replaced by a numerical mean in taking this square.

Aggregate the original uniform source prior to `pi^c_IJ=n_J/N`. It is normalized and positive. All parent source costs are again equal in a receiver row, so its exact Gibbs row is this prior for every positive temperature. This prior is the pushforward of one original source-label draw. A batch of `n_I` independent primitive source labels would have the corresponding product mark law, not one common parent label; if such marks are jointly exposed, that product experiment must be retained. The extensive-response class used here does not expose those marks. No identification of these different mark experiments is asserted.

## Parent full Fisher gradient and exact joining square

The parent matter potential has exactly the original form with these normalized inherited data:

\[
 E_q^c=\sum_I\left[
   \int\log\frac{dQ_I}{dA_{I,0}}dQ_I+
   \int\log\frac{dQ_I}{dW_2(n_I\alpha_0,\Lambda(M_c))}dQ_I\right].
\]

The total coefficient of `log det Lambda` is `-alpha_0 sum_I n_I=-N alpha_0`. Consequently its full channel derivative is the same `C(M_c)` as above, and the complete parent density force is

\[
 h_I^c(S)=2\log Q_I(S)-2(n_I\alpha_0-3/2)\log\det S
                    +\operatorname{tr}[(I+C(M_c))S]+\text{constant}.
\]

On `Q_I=W_2(A_I,P)`, its unit-mobility Fisher flow is therefore

\[
 \dot A_I=-2(A_I-n_I\alpha_0),\qquad
 \dot P=-2P+I+C(M_c).
\]

These are exactly the sums of the fine shape equations and the same common-precision equation. The model sector gives `dot B_I=-2(B_I-n_I beta_0)` and its corresponding common-precision equation. This proves same-time full-gradient inheritance on the admitted family. There is no time change or mobility correction.

For disjoint blocks, addition joins give

\[
 (n_I,A_I,B_I)\star(n_J,A_J,B_J)
 =(n_I+n_J,A_I+A_J,B_I+B_J).
\]

They keep the common precisions and the total `N`. The shape vector fields add, the total moment `M_c` is unchanged, and therefore the common forcing `C` is unchanged. This proves the exact evolution-joining square. Matrix addition of independent parent samples gives the corresponding joined laws and comparison channels, so the sample and channel squares commute as well. Associativity follows from addition. These statements hold for every regrouping permitted by a separately specified selector; they supply no preferred grouping.

## The fine energy does not factor through the parent

There is no need to assume energy constancy on the fibers. In fact, it fails here. Set the common `P=I`, choose all initial shapes `alpha_i=alpha_0`, and then perturb two of them to `alpha_0+epsilon` and `alpha_0-epsilon`, with nonzero sufficiently small `epsilon`. The total `A`, the total moment `M=N alpha_0 I`, the comparison precision `Lambda`, and every aggregate state of a block containing that pair are unchanged.

At this fixed `Lambda`, the density ratio `log(dA_0/dnu_M)` is a constant plus `tr((Lambda-I)X)`. Its summed expectation is therefore fixed by `M`. The change of the fine energy is exactly

\[
 E_q(\epsilon)-E_q(0)
 =2\operatorname{KL}(W_2(\alpha_0+\epsilon,I)\Vert A_0)
 +2\operatorname{KL}(W_2(\alpha_0-\epsilon,I)\Vert A_0)>0.
\]

The laws have distinct shape parameters and positive densities, so each nonzero divergence is strict. Thus the fine potential varies while the parent state is constant. Exact gradient inheritance above was proved by the full force calculation, not inferred from a factored potential or from Fisher contraction.

## Responses, passive presentation, and remaining obligations

The complete finite-history proof in `wishart-response.md` remains valid after replacing its uncoupled precision ODE by the closed coupled equation proved here. At every time the laws still have common precisions, extensive independent sampling still gives the same product Wishart block kernel, all joins preserve the state controlling the subsequent precision flow, and the flow is unique and global. Adaptive readout times and normalized postprocessing kernels chosen from carried history and retained state therefore preserve the entire admitted joint history law. Queries cutting current blocks, persistent hidden-child sampling, and implicit Bayesian state resets remain outside that protocol.

In the displayed coordinates `I` is a fixed Euclidean reference form, making simultaneous orthogonal sample congruences an active symmetry. Passive general linear frame changes are compatible when the reference form is carried as part of the constitutive data. If that precision form is `H`, the typed expressions are

\[
 \Lambda=H+\frac\kappa N HMH,
 \qquad C=\Lambda+\frac\kappa N H(M-N\alpha_0\Lambda^{-1})H,
 \qquad \dot P_i=-2P_i+H+C.
\]

Under `X'=gXg^T`, take `M'=gMg^T`, `H'=g^{-T}Hg^{-1}`, and `P'=g^{-T}Pg^{-1}`. Both `Lambda` and `C` then transform as precision forms. The density Jacobian is carried with the laws, so normalized channels and the original relative entropies transform consistently. Holding the numerical identity matrix fixed under an arbitrary nonorthogonal change would instead change the constitutive model. No equivalence between active sample symmetry and passive frame change is assumed.

The mechanism fingerprint is an affine aggregate-moment precision in normalized Wishart comparison channels, the complete `-N alpha_0 log det Lambda` derivative, convolution-additive shape counts, and a common precision driven by the retained total first moment. Unlike the constant-reference specialization, this force has a nonzero mixed agent derivative. It still uses a declared regular family and product local evaluator.

A falsifier for the derived force would be a regular mass-preserving variation for which the displayed energy differential disagrees with the stated `C`; the expansion above reduces that check to finite matrix differentiation. A counterexample to inheritance would need to remain in the declared common-precision family and use the stated block references, fixed primitive `N`, and complete channel derivative. Dropping any one of these hypotheses defines a different claim. The construction is not a general-law aggregation theorem off this family.

The strongest result is exact coupled original-time Fisher inheritance, normalized associative channel aggregation, global positive flow on the declared family, and the previously established extensive response histories. The remaining formation obligation is to prove the actual endogenous selector, persistence, and two successive noninjective handoffs; the separate geometry route must check collective connection and residual retention. No numerical experiment, GPU query, Lean work, or panel ran. This assigned derivation is the only file written in this round.
