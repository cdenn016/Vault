<!-- rigorous-theory-search-metadata {"schema_version":"rigorous-theory-search/v1","contract_id":"contract-sha256-b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe","target_digest":"b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe"} -->
# Native preferential cliques from an open law domain

## Result and scope

The clique-formation conjunct has an explicit existence construction in the original smooth KL model. Four homogeneous agents, with positive binary belief and model laws, uniform fixed source priors, normalized identity comparison channels, and a common Ising evaluator develop two permanently preferential pairs from an open set in all eight independent law coordinates. Initially every source weight is below one half. At finite times, each selected pair acquires mutual belief and model source weights above nine tenths, and those inequalities persist forever. The children need not start on an equal-law or equal-parameter submanifold. The complete incoming derivatives are included, all Fisher mobilities are one, and no source prior learns.

This is a first-stage routing theorem. It supplies neither a genuinely compressive parent state nor a second join. The proof actually ends in an attracting two-clique configuration, so it cannot be interpreted as a proof of later coalescence. A strictly positive noisy-channel perturbation is included below; the identity-channel witness is already allowed by the manuscript's assumptions.

The frozen target is existential over an architecture and a full open initial domain. The result here proves that one conjunct without claiming the target. The general setting remains probability laws and normalized kernels. Binary laws are a witness, not a restriction of the surrounding theory to a chosen moment closure.

## Model, normalization, and full Fisher vector field

Let both sample spaces be \(\{-1,1\}\), with counting measure. Write

\[
q_i(k)=\frac{1+kx_i}{2},\qquad
s_i(m)=\frac{1+my_i}{2},\qquad
z=(x_1,\ldots,x_4,y_1,\ldots,y_4)\in M=(-1,1)^8.
\tag{C1}
\]

Every point of \(M\) is admitted. The only recognition factorization is the original \(q_i\otimes s_i\). There is no equality constraint between coordinates. Take the same proper reference and normalized evaluator for every agent,

\[
r_i(m)=\frac12,\qquad
G_J(k\mid m)=\frac{e^{Jkm}}{2\cosh J},\qquad J=8.
\tag{C2}
\]

The reference joint is strictly positive and normalized. Define

\[
\psi(u)=\frac{1+u}{2}\log(1+u)
       +\frac{1-u}{2}\log(1-u).
\]

Direct summation gives exactly

\[
\operatorname{KL}(q_i\otimes s_i\Vert r_iG_J)
=\psi(x_i)+\psi(y_i)-Jx_iy_i+\log\cosh J.
\tag{C3}
\]

The evaluator, rather than a modified kinetic coefficient, couples the two sectors. The value \(J=8\) is a supplied common interaction parameter. It does not encode any agent pairing.

Every other agent is an allowed source: \(\mathcal N_i=\{1,2,3,4\}\setminus\{i\}\). Self-edges are excluded at every agent in this construction. Both source priors are \(\pi_{ij}=1/3\) on these sets. Initially use the identity Markov kernel. Its entries need not all be positive; its compared law is strictly positive at every point of \(M\). Put

\[
d(u,v)=\operatorname{KL}(q_u\Vert q_v),\qquad
B_{ij}(x)=\frac{e^{-d(x_i,x_j)/T}}
                  {\sum_{k\ne i}e^{-d(x_i,x_k)/T}},\qquad T>0,
\tag{C4}
\]

with \(B_{ij}(y)\) for the model sector. These are the exact optimized rows of the original potential. All permitted weights are strictly positive. The reduced energy, with its normalizers retained, is

\[
E_T(z)=\sum_i[\psi(x_i)+\psi(y_i)-Jx_iy_i+\log\cosh J]
-T\sum_i\log\left(\frac13\sum_{j\ne i}e^{-d(x_i,x_j)/T}\right)
-T\sum_i\log\left(\frac13\sum_{j\ne i}e^{-d(y_i,y_j)/T}\right).
\tag{C5}
\]

All sums and derivatives are finite on compact interior sets. The metric and dynamics are

\[
g_z=\sum_i\left[\frac{dx_i^2}{1-x_i^2}+\frac{dy_i^2}{1-y_i^2}\right],
\qquad \dot z=-\operatorname{grad}_{g}E_T.
\tag{C6}
\]

In particular,

\[
\partial_ud(u,v)=\operatorname{atanh}u-\operatorname{atanh}v,
\qquad
\partial_vd(u,v)=\frac{v-u}{1-v^2}.
\]

Differentiating the exact log normalizers, and then using both occurrences of \(x_i\), yields

\[
\begin{aligned}
\dot x_i={}&(1-x_i^2)\left[Jy_i-\operatorname{atanh}x_i
 -\sum_{j\ne i}B_{ij}(x)
    (\operatorname{atanh}x_i-\operatorname{atanh}x_j)\right]\\
&+\sum_{k\ne i}B_{ki}(x)(x_k-x_i).
\end{aligned}
\tag{C7}
\]

The \(y\) equation exchanges \(x\) and \(y\). The last sum is the incoming sender derivative. Omitting it changes both the scalar equation below and the formation proof. The derivative of an optimized row is accounted for by differentiating the normalizer; it is not added as another force term. No channel derivative occurs for the fixed identity channel.

The vector field is analytic on \(M\). It has unique maximal interior solutions, and

\[
\frac{dE_T}{dt}=-\sum_i[(1-x_i^2)(\partial_{x_i}E_T)^2
                         +(1-y_i^2)(\partial_{y_i}E_T)^2]\le0.
\tag{C8}
\]

Global interior existence will be established for the open basin used in the theorem; it is not asserted here for every point of \(M\).

## A polarized strict minimum for sufficiently small fixed temperature

There is a unique \(r_0\in(0,1)\) satisfying

\[
\operatorname{atanh}r_0=Jr_0.
\tag{C9}
\]

Indeed, \(\operatorname{atanh}r/r\) increases strictly from one to infinity: it is the average of the strictly increasing function \((1-u^2)^{-1}\) on \([0,r]\). Since \(J=8>1\), the intermediate value theorem gives the unique root. Also \(r_0>1/2\), because \(\operatorname{atanh}(1/2)/(1/2)=\log3<8\).

For the proof only, choose the sign vector \(\sigma=(1,1,-1,-1)\) and the involution \(p=(12)(34)\). Define \(z_0\) by \(x_i=y_i=\sigma_i r_0\). These labels do not occur in the constitutive model (C2)--(C5). On a sufficiently small compact neighborhood of \(z_0\), the source \(p(i)\) is uniquely cheaper than either opposite-sign source in each sector, with a uniform cost gap \(c>0\).

On that neighborhood rewrite the actual energy exactly as

\[
E_T=E_*+8T\log3+R_T,
\tag{C10}
\]

where

\[
E_* = \sum_i[\psi(x_i)+\psi(y_i)-Jx_iy_i+\log\cosh J]
      +\sum_i[d(x_i,x_{p(i)})+d(y_i,y_{p(i)})],
\]

and, for each row, the corresponding summand of \(R_T\) is

\[
-T\log\left[1+\sum_{j\notin\{i,p(i)\}}
e^{-[d(x_i,x_j)-d(x_i,x_{p(i)})]/T}\right],
\tag{C11}
\]

or the same expression in \(y\). Differentiation on this compact set gives \(\|R_T\|_{C^2}\le C(1+T^{-1})e^{-c/T}\) after enlarging a finite constant \(C\). Thus the gradients and Hessians converge to those of \(E_*\). This is an approximation used to establish existence at positive \(T\); the final dynamics remains exactly (C5).

At \(z_0\), every local term and internal divergence is stationary. The local Hessian in \((x_i,y_i)\) is

\[
\begin{pmatrix}a_0&-J\\-J&a_0\end{pmatrix},\qquad
a_0=(1-r_0^2)^{-1}>\operatorname{atanh}r_0/r_0=J.
\tag{C12}
\]

The strict inequality follows because an increasing function's endpoint exceeds its average. Each divergence Hessian at equal arguments \(u=v=\pm r_0\) is

\[
a_0\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\succeq0.
\]

Consequently \(\nabla^2E_*(z_0)\succeq(a_0-J)I_8\succ0\). The implicit function theorem, applied to the gradient, gives a unique nearby critical point \(z_T\) for every sufficiently small positive \(T\), with \(z_T\to z_0\) and positive-definite Hessian. To include \(T=0\) in that theorem, the exponentially small correction may be extended by zero for negative \(T\); the strictly positive local cost gap makes this extension smooth. No assertion about a zero-temperature vector field outside this neighborhood is used.

The actual energy is invariant under all agent permutations, simultaneous reversal of the two binary sample coordinates, and exchange of the belief and model sectors. The subgroup generated by swaps within the two displayed pairs, simultaneous exchange of the pairs and sign reversal, and sector exchange fixes exactly the line

\[
x_i=y_i=\sigma_i r.
\tag{C13}
\]

Uniqueness of the critical point in a symmetric neighborhood therefore gives \(z_T=z(r_T)\) on this line, with \(r_T\to r_0\). Positive definiteness is in all eight directions, not only along the line.

Because the Fisher metric is smooth and positive definite near \(z_T\), this critical point is locally asymptotically stable. A direct Lyapunov justification suffices: choose a small closed ball on which \(\nabla^2E_T\succeq mI\) and the inverse Fisher metric has eigenvalues bounded below by \(b>0\). A sufficiently small connected sublevel component \(W\) around the strict minimum lies inside the ball. Equation (C8) makes its closure forward invariant, while strong convexity gives \(\|\nabla E_T\|^2\ge 2m(E_T-E_T(z_T))\). Hence the energy gap decays at least as \(e^{-2bm t}\), and trajectories in \(W\) converge to \(z_T\) while remaining in a compact subset of \(M\).

At the critical point, the within-pair source weight in either sector is

\[
w_T(r_T)=\frac{1}{1+2e^{-D(r_T)/T}},\qquad
D(r)=d(r,-r)=2r\operatorname{atanh}r.
\tag{C14}
\]

It tends to one as \(T\downarrow0\). Fix \(\delta=1/10\). For sufficiently small fixed \(T\), choose \(W\) so that every state in its closure has all four directed within-pair weights in both sectors strictly above \(1-\delta\). The cross-pair weights are then strictly below \(\delta\). These inequalities hold permanently after entry into \(W\).

## Reachability from initially weak source preference

The line (C13) is invariant by the same symmetries. Substitution in the full vector field (C7) gives the exact scalar equation

\[
\dot r=f_T(r)
=(1-r^2)[Jr-(3-2w_T(r))\operatorname{atanh}r]
 -2(1-w_T(r))r.
\tag{C15}
\]

There are two cross sources, each with weight \((1-w_T(r))/2\). The final term of (C15) is their total incoming force. For \(r>0\), \(1/3\le w_T(r)<1\). Therefore, on \(0<r\le1/2\),

\[
\frac{f_T(r)}{(1-r^2)r}
\ge 8-\frac73\frac{\operatorname{atanh}r}{r}
       -\frac{4}{3(1-r^2)}
\ge 8-\frac73\log3-\frac{16}{9}>0.
\tag{C16}
\]

This inequality is uniform in \(T>0\). In particular, the origin is repelling along the positive ray; its actual linear coefficient is \(J-11/3>0\).

For each compact interval in \((0,1)\), \(w_T\to1\) with its derivatives as \(T\downarrow0\), provided that interval is bounded away from zero. Thus \(f_T\to f_0\) in \(C^1\) there, where

\[
f_0(r)=(1-r^2)[Jr-\operatorname{atanh}r].
\tag{C17}
\]

The function \(f_0\) is positive on \((0,r_0)\), and

\[
f_0'(r_0)=J(1-r_0^2)-1<0.
\tag{C18}
\]

Choose \(\eta>0\) with \(r_0-\eta>1/2\) and \(f_0'<-b_0<0\) on \([r_0-\eta,r_0+\eta]\subset(0,1)\). Uniform convergence makes \(f_T>0\) on \([1/2,r_0-\eta]\) and \(f_T'<-b_0/2\) on the latter neighborhood for all sufficiently small \(T\). The root there is exactly \(r_T\), since \(z(r_T)\) is stationary. Together with (C16), this proves

\[
f_T(r)>0\quad(0<r<r_T),
\qquad
r(t)\uparrow r_T
\quad\text{for every }r(0)\in(0,r_T).
\tag{C19}
\]

The solution is global, remains in the compact interval between its positive initial value and \(r_T<1\), and enters \(W\) at a finite time.

Fix such a small temperature once and for all. The strictly increasing function \(D(r)\) starts at zero. Choose \(\epsilon\in(0,1/2)\) by

\[
D(\epsilon)=\frac{T}{4}\log2.
\tag{C20}
\]

For the reference initial state \(z(\epsilon)\), every within-pair source weight equals \(1/(1+2^{3/4})<1/2\), while each cross weight is smaller. Consequently no directed source edge in either sector has weight one half, much less nine tenths, at time zero. Nevertheless (C19) brings this trajectory into \(W\).

Let \(t_1<\infty\) be a time when this reference trajectory lies in the interior of \(W\). Its segment on \([0,t_1]\) lies in a compact subset of \(M\). Local ODE continuous dependence supplies an open neighborhood \(U\subset M\) of \(z(\epsilon)\) whose solutions exist through \(t_1\), remain close to that segment, and enter \(W\) at \(t_1\). Shrink \(U\) so that every initial row still has maximum below one half. From \(t_1\) onward the compact invariant sublevel gives global existence and permanent within-pair preference above nine tenths. Thus \(U\) is an open set in all eight independent belief/model-law coordinates; the symmetry line is a proof device, not an initial-state assumption.

Taking the union of all agent permutations of \(U\) gives a permutation-invariant admitted open class. Which two pairs form is determined by the initial law configuration. The dynamics and selector contain no pair labels. This class is not claimed to be all initial laws or a dense subset of them. The exactly symmetric origin stays fixed, and other basins may have different outcomes.

## A state-only selector and persistent membership events

For the four primitive agents define an undirected edge \(\{i,j\}\) exactly when

\[
\min\{B_{ij}(x),B_{ji}(x),B_{ij}(y),B_{ji}(y)\}>9/10.
\tag{C21}
\]

The threshold \(9/10\) is declared constitutive data. The criterion reads the native optimized rows; it does not introduce a force. Because two entries in the same normalized row cannot both exceed \(9/10\), this graph has degree at most one. Its nontrivial components are therefore unambiguous pairs. At equality, take the event at the first crossing and use the closed inequality to assign the event time; strict membership holds immediately afterward. Relabeling acts naturally on this selector.

On the reference trajectory, every correct within-pair weight increases strictly with \(r\), and every cross weight is at most \(1/3\). The within-pair threshold is crossed at the unique \(r_c\in(\epsilon,1/2)\) satisfying

\[
D(r_c)=T\log18,
\tag{C22}
\]

after making \(T\) smaller if needed. The crossing derivative is strictly positive because \(w_T'(r_c)>0\) and \(f_T(r_c)>0\). This also makes the derivative positive on a compact time interval around that crossing. Outside that interval and before \(t_1\), compactness gives a strict sign margin from the threshold. Continuous dependence of the trajectories and vector field therefore permits one further shrinking of \(U\) such that each relevant directed weight crosses the threshold exactly once, no cross-pair edge ever crosses it, and every within-pair weight stays above it until entry into \(W\). After entry, invariance of \(W\) supplies persistence for all later times. Each pair becomes selected at the last of its four sector/direction crossings and remains selected. The two pair times need not coincide after perturbation.

One may further intersect \(U\) with the open dense set on which every two agents have different pairs \((x_i,y_i)\). The resulting nonempty open set contains no identical child configurations. A pair equality \((x_i,y_i)=(x_j,y_j)\) is an invariant submanifold under the full equivariant smooth field. Local uniqueness in both time directions prevents first entry into it at any finite interior time. These selected children remain distinct at every finite time, although their differences decay asymptotically inside each attracting clique.

## Strictly positive comparison kernels

The construction also survives replacing the identity by the common fixed binary channel

\[
K_\rho(\ell\mid k)=\frac{1+\rho k\ell}{2},\qquad 0<\rho<1.
\tag{C23}
\]

Its output on \(q_x\) is \(q_{\rho x}\), so it is normalized, has strictly positive entries, and genuinely transmits the sender sample. Replace every cost by \(d(x_i,\rho x_j)\), with the same change in \(y\). The exact belief equation becomes

\[
\begin{aligned}
\dot x_i=(1-x_i^2)\Bigg[&Jy_i-\operatorname{atanh}x_i
-\sum_{j\ne i}B^{\rho}_{ij}(x)
  (\operatorname{atanh}x_i-\operatorname{atanh}(\rho x_j))\\
&-\sum_{k\ne i}B^{\rho}_{ki}(x)
  \frac{\rho(\rho x_i-x_k)}{1-\rho^2x_i^2}\Bigg].
\end{aligned}
\tag{C24}
\]

The last sum is again the full incoming derivative. On the compact interior reference segment and near its strict minimum, the energy depends smoothly on \(\rho\) through \(\rho=1\). The positive Hessian, attracting critical point, strict initial row bounds, finite-time entry into a trapping sublevel, and transverse threshold crossings all persist for \(\rho<1\) sufficiently close to one. More explicitly, the implicit function theorem continues the positive-Hessian critical point; a small enclosing sublevel remains in the open strict-clique region; and continuous dependence carries an open initial neighborhood into that sublevel. Compact margins and positive crossing derivatives give the same selector conclusion. This proves the result with strictly positive normalized kernels as well as with identity kernels.

No limiting temperature or channel parameter is used during the evolution. First choose a sufficiently small positive \(T\), then a fixed \(\rho<1\) sufficiently close to one, and keep both constant. The argument is analytic; it gives an existence neighborhood, not a numerically calibrated parameter interval.

## Interface to the unfinished recursive target

All source priors remain uniform and fixed. Every external routing weight remains positive at finite \(T\). Pair formation is therefore preferential communication, not an exact graph disconnection. The belief and model coordinates evolve under the same original time parameter and equal unit Fisher mobility. The only supplied architecture is a common normalized evaluator and a common channel; neither contains a hidden pair assignment.

For passive gauge covariance, present each binary alphabet as \(\{\pm u_i\}\) in its one-dimensional content fiber. Push its laws, identity or noisy channel, and evaluator together under any invertible change of presentation. The scalar cost and optimized row are unchanged. This establishes coordinate covariance of this finite example; it does not establish a nontrivial collective connection or preserve one under a parent retention.

The ordinary empirical tuple of the selected children is an exact enlarged description, but it is not the requested continuous compression. Moreover, the existing identity-channel boundary result in the live public-compression chapter applies: a block Gibbs response against arbitrary receiver probes in an open interval determines the distinct exposed binary child laws. For \(K_\rho\), the same finite-exponential argument determines \(\rho x_j\), hence \(x_j\) when \(\rho>0\). Thus unrestricted such responses cannot simply be replaced by one average law while forgetting continuous child distinctions. This is a restriction on that broad interface, not a nonexistence proof for every admitted restricted interface.

The exact formation theorem here must be combined with a new retention proof, rather than with an unproved assumption that strong preference makes descendants redundant. The minimal remaining interface obligation is an actual configuration retention and predeclared joint response class on this open basin that both descend under (C7) or (C24), discard a continuous public-law distinction, and preserve the relevant collective contextual and orbit scores. Even that would not cause the second join: this particular attractor permanently separates the two wells. A recursive mechanism must alter that long-time geometry through inherited state already present in the original architecture, without resetting priors or adding a new attraction after the first events.

## Provenance and checks

This route reads the live \(\texttt{03_dynamics.tex}\) potential and derivative, the binary evaluator construction in \(\texttt{05_inheritance.tex}\), and the preparation and scope statements in \(\texttt{11_conditional_formation.tex}\) and \(\texttt{06_outlook.tex}\), all at Research revision recorded in the source manifest. The fixed-temperature four-cycle theorem in \(\texttt{pifb2/13_section.tex}\) uses learned priors and stochastic kinetics, so it was not transplanted. The theorem above is a separate direct calculation in the original deterministic Gibbs-reduced model.

The mechanism family is local variational bistability plus smooth Gibbs selection, with a full-dimensional attracting basin as the removal of equality preparation. The exact failure test for claiming recursive formation is the absence of a compressive intertwining map and of a subsequent join. No numerical simulation, symbolic script, GPU computation, Lean work, or external review panel was run for this route.
