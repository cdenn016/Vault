<!-- rigorous-theory-search-metadata {"schema_version":"rigorous-theory-search/v1","contract_id":"contract-sha256-b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe","target_digest":"b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe"} -->
# An exact physical-symmetry retention on an open law domain

## Result and scope

There is an explicit homogeneous two-sector KL model for which every regular positive configuration admits a genuinely noninjective physical-symmetry quotient. The quotient removes one continuous relative orientation at a two-child join and another at a subsequent two-parent join. It closes the original-time dynamics and a predeclared class of native routing and aggregate-angle response histories. A section-valued realization by actual normalized parent laws preserves contextual Fisher costs and a commuting collective minimizing connection exactly. None of these assertions requires the initial laws to share a profile or belong to a supplied reconstruction family.

The closure theorem alone is conditional on the chosen blocks. Section 8 now matches its all-source extension to the finite-time two-stage formation theorem in `staged-cliques.md` and the equivariant contextual family in `geometry-symmetry-interface.md`. Together these give a finite-time witness for the frozen target on a full open class of independent law values, under the following declared scope. The architecture has fixed selective comparison channels; the response class excludes arbitrary constituent absolute-angle probes; the parent is a section-valued state anchored at one reference context; its size grows with the block; and its kinetic vector field is the inherited moving-representative field, rather than an asserted ordinary Fisher gradient of a new parent KL. Local lifted phase charts suffice on the proved finite horizon. No unrestricted-probe, pointwise-state, fixed-memory, global-chart, or infinite-recursion conclusion is asserted.

The exact target in the contract is existential over fixed constitutive data and an open subset of independently variable positive laws. At both state-selected handoffs it requires original-time dynamics, all histories in one declared response class, actual public-law loss, and collective Fisher geometry. The construction below addresses the closure and loss conjuncts on an unrestricted regular law domain. It introduces the circle sample spaces, selective channels, anchor context, commuting collective action, and response protocol as route-specific constitutive choices. They are not premises supplied by the user.

Source continuity is with the live `MAgent_Theory_2.0/chapters/03_dynamics.tex`, especially the reduced potential, envelope identity, incoming derivative, and unit-mobility Fisher flow; `05_inheritance.tex` and `07_smooth_closure.tex` supply the distinction between normalized descriptors and closed dynamics. `09_public_compression.tex`, the prior `2026-10-21-public-compression.md`, and `2026-10-22-endogenous-recursive-geometry/routes/response.md` already establish identity-channel response identifiability and incoming-force failures. `10_boundary_closure.tex`, Sections `sec:boundary-tree-inheritance` and `sec:boundary-tree-loss`, already uses physical orientation loss inside a prepared family. The new statement here is an equivariant closure on a full open law domain, with section-valued normalized parent laws. It does not reclassify the earlier prepared family as open.

## 1. Joint law, unrestricted regular domain, and exact dynamics

Let every belief and model sample space be

\[
K=M=\{-1,1\}\times S^1,
\qquad d\nu=\tfrac12\sum_{z=\pm1}\delta_z\otimes\frac{d\theta}{2\pi}.
\tag{P1}
\]

Densities below are with respect to the probability measure \(\nu\). Let \(q_i(z,\theta)>0\) and \(s_i(m,\varphi)>0\) be independently variable normalized smooth densities. On a compact contextual neighborhood, take uniformly positive densities with bounded derivatives. A sufficiently small open neighborhood in the normalized \(C^k\) charts, \(k\geq3\), has these properties. There is no factorization requirement between a bit and its circle within either law. The only recognition factorization is the original within-agent \(q_i\otimes s_i\). The reference joint is the normalized density

\[
p_i(z,\theta,m,\varphi)=r(m,\varphi)G(z,\theta\mid m,\varphi),
\quad r=1,
\quad G=\frac{\exp[Jzm+\lambda\cos(\theta-\varphi)]}
 {\cosh J I_0(\lambda)},
\tag{P2}
\]

where the denominator means the product \(\cosh(J)I_0(\lambda)\), and
\(I_0(\lambda)=\int_{S^1}e^{\lambda\cos u}du/(2\pi)\).
Thus \(\int G(\cdot\mid m,\varphi)d\nu=1\). All densities have full support and bounded log ratios on the declared regular neighborhood, so all KL terms and their displayed variations are finite. No latent joint correlation across agents is asserted. Products introduced below are declared statistical experiments made from independent samples.

Define the binary marginal densities, moments, and circular moments by

\[
\mu_i(z)=\int q_i(z,\theta)\frac{d\theta}{2\pi},
\quad \eta_i(m)=\int s_i(m,\varphi)\frac{d\varphi}{2\pi},
\quad X_i=\mathbb E_{q_i}z,\quad Y_i=\mathbb E_{s_i}m,
\quad u_i=\mathbb E_{q_i}e^{i\theta},\quad v_i=\mathbb E_{s_i}e^{i\varphi}.
\tag{P3}
\]

Both sectors use the same fixed normalized comparison channel

\[
K((z,\theta),d(z',\theta'))
=\delta_z(dz')\frac{d\theta'}{2\pi}.
\tag{P4}
\]

Thus \(q_jK\) has density \(\mu_j(z)\), and \(s_jK\) has density \(\eta_j(m)\). The model channel uses no belief-derived quantity. This channel is selective from the outset; it is not a state-dependent or newly activated erasure gate. Circle variables remain present in the evaluator, the vector field, the parent laws, and the declared aggregate responses.

For \(j\ne i\), take fixed uniform source priors \(\pi_{ij}=1/(N-1)\), temperatures \(T_q,T_s>0\), and the original potential

\[
\begin{aligned}
E={}&\sum_i\mathbb E_{q_i\otimes s_i}
 \log\frac{q_i(z,\theta)s_i(m,\varphi)}{r(m,\varphi)G(z,\theta\mid m,\varphi)}\\
&+\sum_{i,j\ne i}\beta_{ij}\mathbb E_{q_i}
 \log\frac{q_i}{q_jK}
 +T_q\sum_{i,j\ne i}\beta_{ij}\log\frac{\beta_{ij}}{\pi_{ij}}\\
&+\sum_{i,j\ne i}\gamma_{ij}\mathbb E_{s_i}
 \log\frac{s_i}{s_jK}
 +T_s\sum_{i,j\ne i}\gamma_{ij}\log\frac{\gamma_{ij}}{\pi_{ij}}.
\end{aligned}
\tag{P5}
\]

The row constraints are \(\beta_{ij},\gamma_{ij}>0\) and \(\sum_{j\ne i}\beta_{ij}=\sum_{j\ne i}\gamma_{ij}=1\). Varying a row with a Lagrange multiplier gives
\(D_{ij}+T_q(1+\log(\beta_{ij}/\pi_{ij}))+\ell_i=0\).
Strict convexity of \(T_q\sum_j\beta_{ij}\log\beta_{ij}\) gives the unique interior minimizer

\[
\beta_{ij}=\frac{\pi_{ij}e^{-D^q_{ij}/T_q}}
 {\sum_{k\ne i}\pi_{ik}e^{-D^q_{ik}/T_q}},
\qquad D^q_{ij}=\operatorname{KL}(q_i\Vert\mu_j\otimes\mathrm{Haar}),
\tag{P6}
\]

and the analogous model row. This is an exact optimizer over the source-label axis, not an assertion about a finite attention-update algorithm. The entropy temperature is \(T_a\), separately for the two sectors.

The exact identities

\[
\begin{aligned}
L_i&=\int q_i\log q_i d\nu+\int s_i\log s_i d\nu
 -JX_iY_i-\lambda\operatorname{Re}(u_i\overline v_i)
 +\log(\cosh(J)I_0(\lambda)),\\
D^q_{ij}&=H_i^q+\operatorname{KL}(\mu_i\Vert\mu_j),
\qquad H_i^q=\operatorname{KL}(q_i\Vert\mu_i\otimes\mathrm{Haar})
\end{aligned}
\tag{P7}
\]

show that the Gibbs rows depend only on the binary marginals for every admitted law. The receiver term \(H_i^q\) cancels between logits in its row. It is not a constant in the law optimization and must not be dropped from the vector field. Correlations between the bit and circle still affect marginal dynamics.

For normalized tangent variations \(\int\dot q_i d\nu=0\), the Fisher metric is
\(g_q(a,b)=\int ab/q d\nu\), with the same normalization for \(s\). Differentiating the exactly reduced energy by its envelope identity gives, up to a scalar independent of \((z,\theta)\),

\[
\begin{aligned}
h_i^q(z,\theta)={}&2\log q_i(z,\theta)
-\sum_{j\ne i}\beta_{ij}\log\mu_j(z)
-\sum_{k\ne i}\beta_{ki}\frac{\mu_k(z)}{\mu_i(z)}\\
&-JzY_i-\lambda\operatorname{Re}(e^{i\theta}\overline v_i),\\
V_i^q&=-q_i\left(h_i^q-\mathbb E_{q_i}h_i^q\right).
\end{aligned}
\tag{P8}
\]

Exchange \(q,\mu,\beta,X,u\) with \(s,\eta,\gamma,Y,v\) for the model equation, with coupling term \(-JmX_i\). The incoming ratio in (P8) is the full sender derivative. The factor \(2\) comes from one local entropy and one normalized receiver row. There are no channel derivatives because (P4) is fixed. On a neighborhood bounded away from zero, logarithms, marginal ratios, moment integrals, and Gibbs normalization are locally Lipschitz in \(C^k\). Equation (P8) is therefore an ordinary differential equation on a Banach chart of densities, with a unique local interior flow. Its centered form preserves normalization. The result is asserted only while regularity and strict positivity hold.

## 2. Physical symmetry and genuine information loss

For \(a\in S^1\), write \((\tau_a f)(z,\theta)=f(z,\theta-a)\). The physical group \(A=(S^1)^N\) acts by simultaneous rotation of each agent's belief and model law:

\[
(q_i,s_i)\longmapsto(\tau_{a_i}q_i,\tau_{a_i}s_i).
\tag{P9}
\]

Equation (P7), the comparison channels, and the product Fisher metric are invariant under this action. In particular \(u_i\overline v_i\) is unchanged, binary marginals are unchanged, and the circle entropy is unchanged. Consequently (P8) is equivariant for every admitted configuration, including correlated nonproduct densities. This is a direct formula check, not an invariant-family preparation assumption.

For a current block \(I\), define

\[
H_I=\{(a_i)_{i\in I}:\sum_{i\in I}a_i=0\pmod{2\pi}\}.
\tag{P10}
\]

Its dimension is \(|I|-1\). Frames and the physical output angles are fixed when applying (P9), so these transformations change actual public laws. For example \(u_i\mapsto e^{ia_i}u_i\), which an absolute-angle sample distinguishes whenever \(u_i\ne0\). They are not mere relabelings or passive coordinate changes. Relative rotations are also distinct from the single common rotation used for collective geometry below. The continuous Lie algebras of \(H_I\) and that diagonal action intersect trivially.

Any native row-based event time is invariant under the entire physical group \(A\). Thus retaining such times does not recover the discarded angles. At a later union \(I\cup J\), the subgroup \(H_I\times H_J\) is properly contained in \(H_{I\cup J}\), and the dimension grows by one. The second join removes an additional relative block orientation. This is positive-dimensional loss in public laws, even though most law-shape information is retained.

The abstract quotient already closes the flow: if two states differ by an element of \(H_I\), equivariance and uniqueness make their trajectories differ by the same element for every common regular time. Hence their quotient trajectories agree at the original time, without reparametrization. Outside agents and all retained edge data belong to the joint parent-network state; closure does not mean ignoring a changing complement.

## 3. Actual normalized parent laws and recursive composition

A pointwise orbit quotient alone does not establish the required contextual Fisher realization. Use the following stronger section-valued retention. Let \(c\mapsto(q_i(c),s_i(c))\) be a smooth contextual section, choose one fixed reference context \(c_*\), and require \(u_i(c_*)\ne0\). This is an open condition. On a local lifted-angle chart set

\[
\vartheta_i=\arg u_i(c_*),\qquad
\phi_I=\frac1{|I|}\sum_{i\in I}\vartheta_i,\qquad
\alpha_i=\phi_I-\vartheta_i.
\tag{P11}
\]

The same \(\alpha_i\), independent of the evaluation context \(c\), rotates the entire section. Define

\[
\widetilde q_i(c)=\tau_{\alpha_i}q_i(c),\qquad
\widetilde s_i(c)=\tau_{\alpha_i}s_i(c),\qquad
q_I(c)=\bigotimes_{i\in I}\widetilde q_i(c),\qquad
s_I(c)=\bigotimes_{i\in I}\widetilde s_i(c).
\tag{P12}
\]

These are actual normalized densities on \(K^{|I|}\) and \(M^{|I|}\). Their factors are recovered by marginalization, so no extra hidden reconstruction datum is required. The normalized parent evaluator and reference can be represented by \(G_I=\bigotimes_iG_i\) and \(r_I=\bigotimes_ir_i\). Their local KL is the sum of the primitive local KLs. Inherited peer terms remain the original sums evaluated from retained factors and source data; no assertion is made that these sums equal a single ordinary KL between two parent product laws.

The inherited channels can be typed explicitly. For \(i\in I\), \(j\in J\), project a source-parent sample onto constituent \(j\), apply (P4), and compare it with the \(i\)-marginal of \(q_I\). This is a normalized kernel from \(K^{|J|}\) to the recipient port \(K_i\). If a kernel ending in the full parent sample space is desired, append independent fresh recipient-factor draws on all other coordinates:

\[
L_{IJ}^{ij}(\mathbf x_J,d\mathbf w_I)
=K(x_j,dw_i)\bigotimes_{r\in I\setminus\{i\}}\widetilde q_r(dw_r),
\qquad
q_JL_{IJ}^{ij}
=(\mu_j\otimes\mathrm{Haar})\otimes
 \bigotimes_{r\in I\setminus\{i\}}\widetilde q_r.
\tag{P12a}
\]

Consequently \(\operatorname{KL}(q_I\Vert q_JL_{IJ}^{ij})=D^q_{ij}\) exactly, by cancellation of the normalized matching factors. The model kernel uses only the model factors. These kernels represent the existing primitive terms and preserve their distinct source rows; they do not replace the sum by one parent-row cost. If differentiating this padded representation, the derivative of its recipient-factor fill is part of the channel derivative and must be included; the exact KL identity then recovers the original derivative. No extra interaction has been introduced.

This retention forgets only constant relative orientation offsets. The functions \(\arg u_i(c)-\arg u_i(c_*)\), when locally defined, remain retained. Thus it is nonlocal in context and is not the pointwise map obtained by re-centering separately at every \(c\). It keeps a whole section, or the portion of that section needed for the stated dynamics and geometry. This enlarged state is permitted by the contract, but its size is not uniformly bounded.

Within the lifted chart the fibers of (P12) are exactly the constant \(H_I\) orbits. To check composition, first normalize \(I\) and \(J\). Their anchor phases are \(\phi_I\) and \(\phi_J\). Rotate their factors by

\[
\delta_I=\phi_{I\cup J}-\phi_I,\qquad
\delta_J=\phi_{I\cup J}-\phi_J,\qquad
\phi_{I\cup J}=\frac{|I|\phi_I+|J|\phi_J}{|I|+|J|}.
\tag{P13}
\]

The total rotation of constituent \(i\) is then exactly \(\phi_{I\cup J}-\vartheta_i\). Sequential and direct retention agree. Counts in (P13) are inherited primitive counts, not new attraction parameters or adjustable priors. Joins of disjoint blocks commute. The construction works for any state-selected partition; fixed constitutive data contain no membership tree. The time corrections compose as well: the first correction \(\overline\omega_I-\omega_i\) and the subsequent block correction \(\overline\omega_{I\cup J}-\overline\omega_I\) sum to the direct union correction \(\overline\omega_{I\cup J}-\omega_i\).

Dividing an angle by \(|I|\) is not globally single-valued. Equations (P11)--(P13) are explicitly local, on compatible lifted charts for the time interval under discussion. The global object is the \(H_I\) orbit, with local representatives related on overlaps. A simultaneous nonzero root-of-unity rotation can preserve total phase, so global stabilizer claims cannot be inferred from this chart formula.

## 4. Original-time parent vector field

The reference context is fixed in space but its laws evolve in time. Define its instantaneous angular velocity

\[
\omega_i=
\frac{\operatorname{Im}\left(e^{-i\vartheta_i}
 \int e^{i\theta}V_i^q(c_*)d\nu\right)}{|u_i(c_*)|},
\qquad \overline\omega_I=\frac1{|I|}\sum_{i\in I}\omega_i.
\tag{P14}
\]

Then \(\dot\alpha_i=\overline\omega_I-\omega_i\). Equivariance and differentiation of the moving representative give

\[
\begin{aligned}
\partial_t\widetilde q_i(c)
 &=V_i^q(\widetilde x(c))
 -(\overline\omega_I-\omega_i)\partial_\theta\widetilde q_i(c),\\
\partial_t\widetilde s_i(c)
 &=V_i^s(\widetilde x(c))
 -(\overline\omega_I-\omega_i)\partial_\varphi\widetilde s_i(c).
\end{aligned}
\tag{P15}
\]

The scalar \(\omega_i\) is rotation-invariant, so it is computed from the retained representative at \(c_*\). The parent product-law derivative follows by the product rule. All terms in (P15), including the moving-frame correction, are determined by the retained section and its inherited network data. With \(C^k\) input, the displayed rotation derivative is a \(C^{k-1}\) identity; it does not assert a bounded rotation derivative from \(C^k\) to itself. Smooth sample densities avoid a finite derivative budget. Uniqueness of the quotient trajectory follows from the original flow and equivariance, rather than from an unproved Banach-space ODE theorem for this moving representative. This is an exact intertwining at the original time and adds no physical force to the fine system.

The Fisher metric on an abstract isometric quotient, when used to express quotient-gradient dynamics, must be distinguished from the Fisher metric induced on a particular canonical product-law slice. The latter generally differs. In particular, this paper does not assert that (P15) is an uncorrected unit-Fisher-gradient update of the parent product KL. The exact vector field is (P15). This distinction avoids substituting an arithmetic phase average for a harmonic quotient inertia.

## 5. Native responses, inherited routing, and histories

Declare the protocol before selecting any blocks. At a current block \(I\), a public query draws independent full primitive samples \((Z_i,\Theta_i)\sim q_i\) for all \(i\in I\), and returns

\[
\left((Z_i)_{i\in I},\ \sum_{i\in I}\Theta_i\pmod{2\pi}\right).
\tag{P16}
\]

A simultaneous model response uses an independent product of the \(s_i\) and returns its corresponding bit vector and angle sum. A label-free version may return the bit count instead. The displayed version fixes constituent indexing and makes the normalization and recursive computation immediate. The response kernel is the pushforward of a product probability law by the stated measurable map; it is therefore normalized on every input law. It equals the pushforward of the actual retained product law (P12), because \(\sum_i\alpha_i=0\).

This response retains a nontrivial absolute block angle: its first circular moment is \(\prod_{i\in I}u_i\), generally nonzero and dependent on the law. It does not retain an individual constituent absolute angle. At the second join the two former block sums are replaced by their sum, removing their relative phase. Bit vectors concatenate and circle sums add, so querying two children independently and then applying this combination has exactly the union response law, including within-child bit-angle dependence. This is an explicit recursive loss, not a claim that all microscopic angle probes remain available after fusion.

Native communication (P4), all Gibbs source rows, and primitive source selections depend only on retained binary marginals. A parent routing mass can be defined by the inherited average

\[
B_{IJ}^q=\frac1{|I|}\sum_{i\in I}\sum_{j\in J}\beta_{ij},
\tag{P17}
\]

including \(J=I\) when the parent has internal fine edges. These masses are normalized across the current partition. At subsequent joins the same primitive rows and counts are aggregated; no new source prior or parent attraction is introduced. Equation (P17) is not generally a new Gibbs row computed from one KL between parent laws. Any claimed two-stage formation must use a declared contrast criterion for these actual inherited masses.

For finite adaptive histories, predeclare that allowed queries at each time use the current blocks, (P16), native communication, or joint measurable functions of these invariant outputs. Queries may reuse samples within a block aggregate or jointly query several whole current blocks; no query cuts a retained block to expose a constituent angle. Policies depend only on the retained history. If no feedback is added, equality of future histories follows inductively: equal retained states have equal closed flow, the next response kernel agrees, and conditioning on its output gives the same policy and next kernel. Equivariant feedback could be included only after separately checking its descent. None is assumed here.

Past recorded outputs are carried forward verbatim. Exact future equivalence is conditional on the same retained past history. With finitely many sampled pre-fusion angle records, all densities are strictly positive, so every such record has positive density under the continuously many phase configurations in a retention fiber. A finite record does not deterministically reconstruct the erased angle. If the protocol instead stores the entire exact constituent law, infinitely informative angle data, or a source label reused in an identifying measurement, the loss claim can fail. Those protocols are excluded explicitly, not argued to be harmless.

Unrestricted individual absolute-angle probes falsify descent immediately: \(\mathbb E e^{i\Theta_i}=u_i\) changes under an \(H_I\) rotation with \(a_i\ne0\), while the retained state does not. Thus the construction has nontrivial physical angle responses but is not sufficient for every physical angle experiment.

## 6. Actual contextual Fisher geometry

Hold time fixed and differentiate with respect to the evaluation context \(c\). Since the anchor in (P11) is a fixed context, \(\alpha_i\) is constant in this derivative. Hence

\[
d_c\widetilde q_i=\tau_{\alpha_i}d_cq_i,
\qquad d_c\widetilde s_i=\tau_{\alpha_i}d_cs_i.
\tag{P18}
\]

For the actual product law in (P12), the score is a sum of independent factor scores. Each has zero mean because each factor is normalized. Cross terms therefore vanish, giving exactly

\[
g_{q_I}(d q_I,d q_I)=\sum_{i\in I}g_{q_i}(d q_i,d q_i),
\qquad
g_{s_I}(d s_I,d s_I)=\sum_{i\in I}g_{s_i}(d s_i,d s_i).
\tag{P19}
\]

There is no division by block size and no new Fisher normalization. This is a calculation from normalized laws, rather than the assertion that some invariant tensor descends abstractly. It would fail for a different retention that re-centers each evaluation context independently, because then \(d_c\alpha_i\) would contribute.

Let the declared collective action be a common simultaneous circle rotation of the retained belief and model factors. More generally, an admitted common action must commute with the physical rotations (P9). Write \(J_x\xi\) for its vertical tangent, and use the minimizing cost convention

\[
Q_x(v,\xi)=g_x(v+J_x\xi,v+J_x\xi).
\tag{P20}
\]

Rotation is an isometry and intertwines \(J\), so (P18)--(P19) give

\[
Q_{R(x)}(d_cR(x),\xi)=Q_x(d_cx,\xi)
\quad\text{for every }\xi.
\tag{P21}
\]

Therefore all minimizing connection classes, their Lie-algebra stabilizer kernels, and the minimized contextual tensor agree exactly. On a regular local gauge chart the connection coefficients agree as functions of context, so their curvatures agree as well. This is not a claim that the global group stabilizers of the abstract quotient and a chosen representative coincide; the finite root ambiguity after (P13) remains. The conclusion uses the actual parent laws and their contextual derivatives. It is separate from the kinetic metric warning following (P15).

A nonflat geometry is available within this statistical family. For one primitive pair take independent binary factors and circle marginals
\(p_k(\theta-\chi)\) in \(q\) and \(p_l(\varphi)\) in \(s\), where
\(p_k(\theta)=e^{k\cos\theta}/I_0(k)\), \(k,l>0\). Use contexts \((k,\chi)\) and hold \(l\) fixed. The rotation Fisher inertia of \(p_k\) is

\[
A(k)=\mathbb E_{p_k}(k\sin\theta)^2
=k\frac{I_1(k)}{I_0(k)}>0,
\tag{P22}
\]

where the equality follows by integrating the derivative of \(\sin\theta p_k(\theta)\) around the circle. The concentration score is orthogonal to the rotation score by parity. With \(B=A(l)>0\), minimization of
\(A(k)(d\chi+\xi)^2+B\xi^2\) yields

\[
\mathcal A=-\frac{A(k)}{A(k)+B}d\chi,
\qquad
\mathcal F=-\frac{B A'(k)}{(A(k)+B)^2}dk\wedge d\chi,
\qquad
h_{\chi\chi}=\frac{A(k)B}{A(k)+B}>0.
\tag{P23}
\]

Here \(I_1(k)/I_0(k)=\mathbb E_{p_k}\cos\theta>0\) for \(k>0\), and its derivative is \(\operatorname{Var}_{p_k}(\cos\theta)>0\). Thus \(A'(k)>0\), the curvature is nonzero, and \(h_{kk}=\operatorname{Var}_{p_k}(\cos\theta)>0\). Replicating this contextual pattern across a finite population multiplies both inertias and the Fisher tensor by the same count while preserving the connection. The exact retention preserves these nonzero quantities. Small smooth perturbations preserve positivity and nonzero curvature locally, so geometry is not confined to this displayed product section. This calculation establishes an available geometric section, not its simultaneous occurrence at both endogenous formation events.

## 7. Relation to the first-stage clique theorem

The separate `native-cliques.md` proves first-stage binary preferential pairs for the nonself uniform-prior architecture, but its opposite-well attractors do not subsequently join. A product witness embeds that binary trajectory into (P8). Choose common circle marginals \(p_k\) in both sectors, with \(a=\mathbb E_{p_k}\cos\theta\) and \(2k=\lambda a\). The circle part of (P8) is then
\(2\log p_k-\lambda a\cos\theta\), a constant, so the product family is invariant along that witness and its binary flow is unchanged. For \(\lambda>4\), a nonzero solution exists: the map
\(F(a)=I_1(\lambda a/2)/I_0(\lambda a/2)\)
has \(F(0)=0\), \(F'(0)=\lambda/4>1\), and \(F(1)<1\). Continuity gives a root of \(F(a)-a\) in \((0,1)\).

This witness is used only to transfer strict finite-time inequalities. Continuous dependence on initial laws gives full open neighborhoods, including bit-circle correlations and independently varying profiles, that retain any specified strict routing inequalities over a compact time interval with a positive margin. It does not by itself transfer an infinite-time persistence theorem to that enlarged domain, and it does not create the missing second join. If a new self-comparison convention is used, the receiver entropy coefficient must be recomputed; the stationary product embedding above cannot be silently reused.

## 8. A finite-horizon bridge to self-loop staged routing

The fixed Haar channel also admits a simpler bridge than the nonself, coupled Ising witness in Section 7. Fix the same (P1) and (P4), set \(J=\lambda=0\), include every source \(j=1,\ldots,N\), and fix \(\pi_{ij}=1/N\). The evaluator and reference are then uniform proper densities. This is a different fixed constitutive choice within the same original KL model; it is not a change made between hierarchy levels. The two sectors decouple, and the existing joint physical rotation symmetry remains valid. All quotient, response, normalized-law, time, and contextual-geometry formulas above continue to apply.

The full force is (P8) with all sources in both sums. In particular, the self-channel law is \(q_iK=\mu_i\otimes\mathrm{Haar}\), so its peer cost is \(H_i^q\), generally nonzero. The self incoming ratio is \(\mu_i/\mu_i=1\), a constant removed by tangent centering. The entropy coefficient is still \(2\). Treating the self-channel as the full identity on the circle would give a different model and invalidate this coefficient.

For any positive binary laws \(\mu_i(t),\eta_i(t)\) and independently chosen normalized positive angular profiles \(f_i(t),g_i(t)\), the product ansatz

\[
q_i(z,\theta,t)=\mu_i(z,t)f_i(\theta,t),
\qquad
s_i(m,\varphi,t)=\eta_i(m,t)g_i(\varphi,t)
\tag{P24}
\]

is invariant. Indeed, the Gibbs rows depend only on \(\mu,\eta\) by (P7), and the full force separates as
\(h_i^q(z,\theta)=h_i^{\mathrm{bin}}(z)+2\log f_i(\theta)\), with the identical incoming binary terms. Centering the two parts gives exactly the product rule for \(\dot\mu_i f_i+\mu_i\dot f_i\). Thus \(\mu,\eta\) follow the original binary identity-channel, uniform-prior, self-loop, \(J=0\) equations, while

\[
\dot f_i=-2f_i\left(\log f_i-\mathbb E_{f_i}\log f_i\right),
\qquad
f_i(\theta,t)=\frac{f_i(\theta,0)^{e^{-2t}}}
 {\int f_i(\psi,0)^{e^{-2t}}d\psi/(2\pi)},
\tag{P25}
\]

and likewise for \(g_i\). Differentiating the displayed normalized power proves the formula directly. The coefficient \(2\) and the time in (P25) are inherited; no mobility is inserted. For a von Mises initial profile \(p_k(\theta-a)\), (P25) is precisely \(p_{ke^{-2t}}(\theta-a)\). Every positive initial concentration stays positive at every finite time. A phase chart around these fixed phases therefore survives any chosen finite horizon on this reference trajectory.

The following transfer statement is exact and separates the reference ansatz from the actual open class. Suppose the binary system has a positive reference trajectory on \([0,L]\), with strict native routing inequalities on specified compact observation windows, finite event brackets whose endpoint inequalities have nonzero margins, and a selection rule unchanged under sufficiently small trajectory perturbations. Then the bit-circle system has a full open set of initial positive joint densities, containing (P24), with the same bracketed selection and strict-window routing properties.

To prove this, regard the vector field as a map on normalized \(C^k(K)^{2N}\), not on the product submanifold. Its formulas consist of smooth logarithms and ratios bounded away from their singular sets, bounded linear integrations, and finite smooth Gibbs normalizations. It is continuously differentiable with locally bounded derivative. The compact reference trajectory has a regular neighborhood on which one common Lipschitz constant \(C\) and a positive distance \(\epsilon\) to the boundary of that neighborhood can be chosen by a finite cover. For initial perturbations of size less than \(\epsilon e^{-CL}/2\), the difference estimate

\[
\|x(t)-x^0(t)\|_{C^k}\leq e^{Ct}\|x(0)-x^0(0)\|_{C^k},
\qquad 0\leq t\leq L,
\tag{P26}
\]

holds until any first exit and excludes that exit. Native Gibbs rows and their finite block sums are continuous functions of these laws. Shrinking the initial neighborhood preserves each finite set of strict inequalities with its stated margin. The perturbations may independently change every law and introduce arbitrary bit-circle correlation. The resulting neighborhood is open in the full normalized law chart. Product factorization proves one reference trajectory only; it is not imposed on this open set.

This statement does not derive a staged binary trajectory from nothing. The completed `staged-cliques.md` supplies that trajectory with six agents, three first-stage pairs, and a later join of two parents while an exterior parent remains. Its equations (S2)--(S8) are exactly the binary subsystem obtained from (P24): all-source uniform priors, one fixed positive temperature, a uniform local joint, and the complete identity-channel receiver and sender derivatives. Its (S4) equals (P17), and its (S5) is the same inherited count-weighted aggregation. Its fixed selector (S7) requires both directions in both sectors to have cross mass above \(1/10\) and a margin above total exterior mass greater than \(1/20\). It proves transverse directional crossings, separated finite event windows, persistence intervals, and exterior masses below \(10^{-3}\) through the later event. Thus it supplies the transfer hypotheses, with its exact thresholds and margins unchanged. Every physical angle rotation leaves all row trajectories unchanged, so the deterministic row-based event rule descends exactly.

The geometric witness can accompany the whole finite horizon. Set all binary initial laws independent of context, use the selected staged binary trajectory, and choose a compact contextual patch \((k,\chi)\) with \(k>0\). In the belief sector take \(p_k(\theta-\chi)\); in the model sector take \(p_l(\varphi)\), with fixed \(l>0\). Write \(r_t=e^{-2t}\), \(A_t(k)=A(r_tk)\), and \(B_t=A(r_tl)\). At time \(t\), the actual collective connection and curvature for the full population are

\[
\mathcal A_t=-\frac{A_t(k)}{A_t(k)+B_t}d\chi,
\qquad
\mathcal F_t=-\frac{B_t r_t A'(r_tk)}{(A_t(k)+B_t)^2}dk\wedge d\chi.
\tag{P27}
\]

The minimized tensor has

\[
h_{kk}(t)=N r_t^2\operatorname{Var}_{p_{r_tk}}(\cos\theta)>0,
\qquad
h_{\chi\chi}(t)=N\frac{A_t(k)B_t}{A_t(k)+B_t}>0,
\qquad h_{k\chi}(t)=0.
\tag{P28}
\]

Every numerator and denominator needed for rank two, nonzero curvature, and nonzero anchor moments remains bounded away from zero on a compact context patch and a finite interval \([0,L]\). These bounds may be very small when \(L\) is large; they are strictly positive, which is sufficient for this existence argument. The normalized product retention preserves (P27)--(P28) at either handoff by (P18)--(P21).

One may also perturb the contextual section in \(C^2\) of context with values in \(C^k\) of sample coordinates. Differentiating the smooth vector field once and twice in context gives linear inhomogeneous variational equations with bounded coefficients on the same regular tube. Their integral estimates give continuous dependence of both contextual derivatives throughout \([0,L]\). Hence a sufficiently small full section neighborhood preserves the strict geometric bounds as well as the routing windows.

For an open class stated in independent initial law values, the assigned contextual family must itself be equivariant; a fixed external template can otherwise encode the discarded orientations in the extra section data. Use the lift proved in `geometry-symmetry-interface.md`, equation (S23). At the anchor \(c_*=(k_*,0)\), for an arbitrary nearby configuration \(x=(q_i,s_i)_i\), put \(\vartheta_i(x)=\arg\mathbb E_{q_i}e^{i\theta}\) and define

\[
q_{i,x}(k,\chi)=\tau_\chi
\left[
\frac{e^{(k-k_*)\cos(\theta-\vartheta_i(x))}q_i(z,\theta)}
 {\int e^{(k-k_*)\cos(\psi-\vartheta_i(x))}q_i(w,\psi)d\nu(w,\psi)}
\right],
\qquad s_{i,x}(k,\chi)=s_i.
\tag{P29}
\]

At \(c_*\) this equals the independently specified laws \(x\), with no factorization condition. At the product witness it equals the contextual family in (P27)--(P28). Positivity, normalization, and smooth dependence follow directly from the positive normalizer and the nonzero-moment chart. If \((q_i,s_i)\) are rotated by \(a_i\), then \(\vartheta_i\) changes by \(a_i\), and the whole section in (P29) is rotated by that same constant \(a_i\). The lift therefore preserves the exact \(H_I\) fibers after all section data are retained. Evolving these sections by the equivariant original flow preserves this property. The geometry assertion is on this declared regular family through the full open law class, not on every conceivable contextual jet.

Select the partition and event time from the native rows at the fixed anchor \(c_*\), and hand off the whole section on that common absolute-time slice. This is one state-selected event for the retained contextual field. The derivative used in (P18) is then \(d_c p_\tau\) at fixed \(\tau\). Choosing a different time \(\tau(c)\) at every context would add the term \(V(p_{\tau(c)}(c))d_c\tau\); that different protocol is outside the present theorem. Event times at the fixed anchor remain invariant under all discarded physical rotations.

Combining the open binary neighborhood (S30) in `staged-cliques.md`, the finite-horizon extension (P26), and the equivariant lift (P29), then shrinking the neighborhood to preserve the geometric lower bounds, yields a nonempty full open class of all twelve independently variable positive bit-circle laws. Taking the union of its population permutations preserves homogeneity and introduces no fixed membership labels. Every member has the three first-stage pairs and the second join supplied by the same native selector, and at each handoff has the exact noninjective parent construction proved here. Strict positivity of the circle moments gives genuine continuous physical-law loss at both levels. The six-agent witness has a nonempty exterior at its second join.

The transfer uses no stationary angular factor, no state-dependent channel, no receiver-aligned kernel, and no conditional reconstruction preparation. It applies only to finite regular horizons with strict margins. It does not establish uniform infinite-time angular information or a nonzero curvature bound as \(t\to\infty\), since (P25) tends toward Haar measure.

## 9. What is proved and what remains

Equations (P1)--(P21) give an exact parent-closure and recursive-loss construction for this fixed selective-channel architecture on its full regular law domain. It preserves original-time evolution, its predeclared joint response histories, and the actual contextual Fisher minimizing costs. It discards continuous physical orientations at each join and preserves a nonconstant aggregate absolute-angle response. Equations (P22)--(P23) exhibit positive contextual rank and nonzero collective curvature compatible with the retention.

Section 8 matches the completed strict binary staged-routing witness to the full bit-circle law domain, including the same inherited masses and selector. The combined theorem has exact closure, continuous physical information loss, and nonzero geometry on its declared equivariant contextual family for the finite two-stage horizon. It uses the original primitive interaction sums and the complete moving-representative term. The older nonself first-stage theorem is a separate result, and is not used to claim the second join.

No further mathematical premise is missing for this particular combined finite-time construction, but its scope remains the explicit section-valued, locally represented parent and the response protocol above. A stronger parent requirement, such as all constituent absolute-angle probes, a globally single-valued canonical density, a context-local state, or an uncorrected unit-Fisher-gradient update of the canonical product KL, is not established here. The next action that would change the scope is to formulate and solve one such stronger requirement; merely extending the time horizon would not resolve it. No numerical experiment, symbolic script, GPU computation, or Lean work was run for this artifact; the evidence here is the displayed derivation. Research-vault sources were read only.
