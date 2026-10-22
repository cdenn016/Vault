# Public compression under the original smooth KL dynamics

The exact request was: “Continue toward recursive formation under the original smooth KL dynamics, without a prescribed erasure gate. Find a parent that compresses distinct public child states and inherits exact dynamics. Keep the laws general.” This continuation began from Research `536efa6a666984d74afae2dacac6b38d271ad6d1`, following the conditional-spectrum and smooth-erasure release. The earlier restrictions against imposed fine-state synchronization and an added fusion penalty remain in force.

The strongest new result is an exact autonomous parent that discards continuously varying public child-law differences on an open bounded-density neighborhood. It uses the original Gibbs-reduced KL potential, identity peer channels, a fixed coupled evaluator, and unit Fisher mobility. It introduces no erasure gate. The fine children remain distinct at every finite time. The parent fails an ordinary fresh-child response test, so recursive formation remains unresolved. This distinction is now proved inside the same example, rather than left as a generic caution.

## Source continuity and scope

The live sources were `manuscripts/MAgent_Theory_2.0/chapters/03_dynamics.tex`, `05_inheritance.tex`, `07_smooth_closure.tex`, `08_smooth_erasure.tex`, and the package's authoring conventions. The prior record was `docs/research/2026-10-21-smooth-kl-formation.md`. The relevant meta-agent wiki discussion and the current `manuscripts/pifb2/13_section.tex` were consulted. The latter's stochastic learned-row construction does not use the same deterministic potential and was not transferred as a formation theorem.

The original potential includes all receiver derivatives, all incoming source derivatives, and derivatives of state-dependent channels. The phase construction uses its explicitly permitted exact Gibbs-reduced version. It does not freeze a row, source, evaluator, or comparison law during differentiation. General-law statements use bounded positive density charts; neither Gaussian closure nor a finite-statistic family is assumed. The local theorem does require reference spaces admitting balanced binary features and a small fixed coupling. No claim is made for every reference measure, every evaluator, every channel, or arbitrary initial conditions.

The investigation used three constructive analytical rounds. No numerical experiment, training run, GPU work, Lean proof, adversarial panel, or independent verification workflow ran. The main proof was reconstructed from the exact vector field, a convergent phase integral, and an explicit binary response counterexample. Compilation and rendering establish document validity, not mathematical certification.

## The autonomous general-law parent

Let $A,B$ be reference probability measures on standard Borel spaces, and let $\varphi,\psi$ be balanced functions taking values in $\{-1,1\}$. Set

$$
R(dk,dm)=\frac{e^{J\varphi(k)\psi(m)}}{\cosh J}A(dk)B(dm),\qquad |J|<1/4.
$$

This is a proper joint reference with model marginal $B$ and a normalized evaluator. Its local energy is

$$
E_0(q,s)=\operatorname{KL}(q\Vert A)+\operatorname{KL}(s\Vert B)-J(q\varphi)(s\psi)+\log\cosh J.
$$

For $J\ne0$ the sectors are coupled. Every law in a small full chart

$$
q_u=e^u A/A(e^u),\qquad s_v=e^v B/B(e^v),\qquad
(u,v)\in L^\infty_0(A)\times L^\infty_0(B)
$$

is admitted; the laws need not factor over the binary features and the remaining sample coordinates. Take $N$ agents with identity channels, uniform nonself priors, fixed positive temperatures, and the original reduced potential. In the chart, the diagonal flow is

$$
f(u,v)=(-u+J\varphi s_v\psi,-v+J\psi q_u\varphi).
$$

The peer contribution to the linearized difference modes is $-\kappa_N(z_i-\bar z)$, where $\kappa_N=2N/(N-1)$. Both sender and receiver derivatives contribute. The common modes decay at least at rate $1-|J|$; the difference modes decay at least at rate $1+\kappa_N-|J|$. Gibbs-row derivatives vanish to first order at equality because the costs start quadratically.

Writing $\Phi_t$ for the fine flow and $\phi_t$ for the diagonal flow gives

$$
\Pi(x)=\lim_{t\to\infty}\phi_{-t}(\overline{\Phi_t x}),\qquad
\Pi\Phi_t=\phi_t\Pi.
$$

The proof in `chapters/09_public_compression.tex` is direct in the Banach chart. The diagonal field is globally Lipschitz, with complete forward and backward flow. Permutation symmetry makes the average residual quadratic in the child differences. Both the differences and their initial-state derivatives decay at a rate $b>1+2|J|$. The residual and its derivative therefore decay as $e^{-2bt}$, which dominates the inverse-flow derivatives in the phase integral. The resulting map is $C^1$, retracts the diagonal, and has averaging derivative there. The Banach implicit function theorem gives genuine continuous fibers parametrized by $N-1$ difference fields.

The parent has proper belief and model laws. Its field equals the Fisher flow of the restricted energy $NE_0$ under the restricted metric $Ng_{\rm single}$. This does not imply that the fine energy is constant on phase fibers. Actual children are not replaced or constrained. Exchange symmetry and backward uniqueness prevent two distinct complete child states from first coinciding at a finite time. All configurations in the local theorem nevertheless approach the same equilibrium, so this does not establish persistent nonzero heterogeneity or selected membership.

The map is an implicit infinite-time construction. No finite-cost evaluation algorithm was developed. Its existence gives an exact dynamical reduction rather than a practical compression routine.

## Explicit failure of an existing public response

For $N=2$ binary agents with $q_i=s_i=\operatorname{Ber}_{\pm1}(x_i)$, write $x_1=m+a$, $x_2=m-a$. There is only one source in each row. Direct differentiation of the original potential gives

$$
\dot x_i=-(1-x_i^2)[2\operatorname{atanh}x_i-\operatorname{atanh}x_j-Jx_i]-(x_i-x_j).
$$

The local diagonal field is $f_b(x)=-(1-x^2)(\operatorname{atanh}x-Jx)$. Expansion yields

$$
\dot m=f_b(m)+(6-3J)ma^2+O(5),\qquad
\dot a=-(5-J)a+O(3).
$$

The exact phase mean consequently has expansion

$$
p=m+\frac{3(2-J)}{2(5-J)}ma^2+o((|m|+|a|)^3).
$$

The coefficient follows by substituting into the exact intertwining identity; the two-agent gap also supports three derivatives of the convergent integral. Along $m=a>0$ sufficiently small, $p\ne m$. The heterogeneous configuration and the diagonal configuration $(p,p)$ have identical phase parents but different fresh uniform-child bit means, $m$ and $p$. Sampling the phase law instead would be a new interface, not inheritance of the existing one. This is a failure within the exact positive construction, not only a counterexample for another pooling rule.

## Unrestricted Gibbs interfaces identify the children

For bounded positive densities $f_j$ against a probability reference $\lambda$, positive weights $w_j$, and fixed $T>0$, the identity-channel block response is

$$
Z(r)=\sum_jw_j e^{-\operatorname{KL}(r\lambda\Vert f_j\lambda)/T}.
$$

A block-selection probability against a known outside competitor determines $Z$. Knowledge of $Z$ for every positive receiver near $r=1$ determines the weighted empirical measure $\sum_jw_j\delta_{f_j}$. The proof removes the receiver entropy, producing a finite sum of $\exp(\int r\log f_j/T)$. A bounded zero-mean probe separates the finitely many distinct normalized log densities. Restriction to the resulting line and differentiation gives an invertible Vandermonde system. Identical laws can be merged by adding their weights; distinct exposed laws cannot be forgotten.

Thus a single ordinary KL parent reproduces all those responses only when all its children already have the same law. This is scoped to fixed identity comparison channels and unrestricted receiver probes. It does not rule out restricted protocols or different original channels, and it does not contradict the isolated phase quotient.

For affine probes $r_\theta=r_0+\sum_a\theta_a h_a$, the exact response descriptor is instead

$$
\mu=\sum_jw_j e^{b_j/T}\delta_{v_j},\qquad
b_j=\int r_0\log f_j d\lambda,\quad (v_j)_a=\int h_a\log f_j d\lambda.
$$

Equal slopes may merge through their tilted weights. The incoming force is $\dot f_j=\alpha_j(r_\theta-f_j)$, so the descriptor's derivatives require reciprocal moments $\int r_0r_\theta/f_j$ and $\int h_ar_\theta/f_j$. Boundary equivalence alone does not close them. For the single uniform receiver on three atoms, the probability vectors $(1/4,1/4,1/2)$ and $(c,c,1-2c)$, $c=(1+\sqrt5)/8$, have the same coordinate product $1/32$ and hence the same log-law intercept. Under $\dot q=r-q$, their intercept derivatives are $1/9$ and $(5\sqrt5-10)/9$. The descriptor already fails its own incoming update.

## Other constructive and failed approaches

The following calculations record what should not be rediscovered in the next continuation. They are not additional formation claims.

### Geometric pooling

For two identity-peer laws with energy $D(q_1\Vert q_2)+D(q_2\Vert q_1)$, the full derivatives are $h_1=\log(q_1/q_2)-q_2/q_1$ and its exchanged version. The normalized geometric pool $g$ obeys

$$
\dot g=g(C-\mathbb E_g C),\qquad C=\tfrac12(q_1/q_2+q_2/q_1).
$$

The receiver logarithms cancel, but incoming ratios remain. On three atoms the laws proportional to $(e^a,e^{-a},1)$ and $(e^{-a},e^a,1)$ have uniform geometric pool, whose peer velocity is $(\cosh(2a)-1)(1,1,-2)/9$. Identical uniform children have the same pool and zero velocity. A proper coupled evaluator with model bit $m$, uniform reference, and $G(k\mid m)\propto e^{Jm(1,-1,0)_k}$ embeds this failure in the two-sector system at uniform model laws: the averaged local belief force is constant. This is not repaired by naming the geometric pool a parent.

### Convolution of density spectra

For uncoupled KL relaxation against fixed references, let $\ell_i=\log(dq_i/dr_i)$ and $\xi_i=(\ell_i)_\#r_i$. The convolution $\xi_I=*_{i\in I}\xi_i$ evolves exactly by

$$
T_t\xi=[r\mapsto e^{-t}r-\log\int e^{e^{-t}u}\xi(du)]_\#\xi,
\qquad T_t(\xi*\eta)=T_t\xi*T_t\eta.
$$

This associative quotient loses factorization information, but it has no interacting formation mechanism. Identity-peer KL breaks it. On two independent fair bits put $a=1+\alpha u$, $b=1+\beta v$. The density pairs $(ab,1)$ and $(a,b)$ have the same convolution log-spectrum. Under local KL plus both directed peer KL terms, the derivative of the retained statistic $\sum_iD(r\Vert q_i)$ differs by

$$
-\frac{\alpha^2\beta^2}{(1-\alpha^2)(1-\beta^2)}.
$$

This follows from the incoming ratio integral; the local and peer energies agree in the two preparations. Independent reference coupling cannot be substituted for the original shared-reference alignment.

### A supplied two-stage symmetry quotient

There is a distinct exact construction that keeps original interactions and compatible restricted responses, but generally discards orientation branches rather than continuous dimensions. It is retained here as a conditional construction, not promoted into the main phase theorem.

Take four agents $A+,A-,B+,B-$, identity channels, identical references, and uniform nonself source priors. On each sector's reference space take commuting measure-preserving involutions $\tau_A,\tau_B$. Require the joint reference $R$ to be invariant under each belief involution acting on its argument alone and each model involution acting on its argument alone. Diagonal invariance is insufficient. Set

$$
q_{I,\pm}=m_I(1\pm a_I),\quad w_I=a_I^2,
$$

with $m_I$ invariant under both involutions, $a_I$ odd under $\tau_I$ and even under the other. Use analogous model densities $n_I(1\pm b_I)$ and $v_I=b_I^2$. Rows assign weight $p_I$ to the paired child and $(1-p_I)/2$ to each outside child. The family is the fixed set of label exchanges combined with the sample involutions, so invariance of the original energy and Fisher metric proves invariance of the full flow, including the rows.

Define

$$
\Psi(w)=\frac{1+\sqrt w}{2}\log(1+\sqrt w)+\frac{1-\sqrt w}{2}\log(1-\sqrt w),\quad
C(w)=2\sqrt w\operatorname{atanh}\sqrt w,\quad B(w)=-\tfrac12\log(1-w).
$$

The within and cross costs are exactly

$$
D_I=\int m_I C(w_I),\qquad
D_{IJ}=D(m_I\Vert m_J)+\int m_I\Psi(w_I)+\int m_I B(w_J).
$$

Writing the full energy as $2F$, the retained energy is

$$
F=\sum_I D(m_I\otimes n_I\Vert R)
+\sum_{I,a=q,s}\left[\int m_I^a\Psi(w_I^a)+p_I^aD_I^a+(1-p_I^a)D_{IJ}^a+T_aD(\operatorname{Ber}(p_I^a)\Vert\operatorname{Ber}(1/3))\right].
$$

The original metric restricts to twice the sum over pairs and sectors of

$$
\int\frac{(\delta m)^2}{m}+\int\frac{m(\delta w)^2}{4w(1-w)}+\frac{(\delta p)^2}{p(1-p)}.
$$

The signed contrast is the regular coordinate at $w=0$. The exact retained equations, writing $h_I$ for the local derivative, are

$$
\begin{aligned}
H_I={}&h_I+(2-p_I)\Psi(w_I)+p_IC(w_I)
+(1-p_I)[\log(m_I/m_J)+B(w_J)]-(1-p_J)m_J/m_I,\\
\dot m_I={}&-m_I(H_I-\mathbb E_{m_I}H_I),\\
\dot w_I={}&-4w_I(1-w_I)[(2-p_I)\Psi'(w_I)+p_IC'(w_I)+(1-p_J)(m_J/m_I)B'(w_I)],\\
\dot p_I={}&-p_I(1-p_I)[D_I-D_{IJ}+T\log(2p_I/(1-p_I))].
\end{aligned}
$$

The ratio terms explicitly retain incoming forces. The signs of contrasts on separate sample orbits may change without changing this retained state, and such changes need not be a global child exchange. However, where $a\ne0$, $a\mapsto a^2$ is locally invertible. On finite alphabets this is generally a discrete orientation quotient, not a continuous dimension reduction. With a nonatomic base it forgets a measurable orientation field. It is an active sample symmetry, not a passive gauge transformation.

A second supplied quotient is possible with an additional involution $\chi$ exchanging the pair involutions, separately preserving the reference, and a preparation $m_B=\chi_\#m_A$, $w_B=w_A\circ\chi$, $p_A=p_B$, in both sectors. At each sample point retain the joint unordered pair

$$
\Xi_x=\tfrac12\delta_{(m_A(x),w_A(x))}+\tfrac12\delta_{(m_B(x),w_B(x))}.
$$

The association between density and contrast must remain joint. Symmetry makes the two normalization constants equal. The displayed equations then move the two atoms by the same rule using their retained partner; their weak two-atom transport and the common row equation close. The local evaluator reads only the mixture of the other sector because it is separately invariant under $\chi$. Local exchanges on a proper invariant region give a noninjective second retention. This is a supplied quotient tower on an imposed invariant preparation.

Fresh uniform choice of one child for each single-sector response has law $m_I$ or $n_I$; fresh parent choice followed by fresh child choice composes to the uniform mixture of all four. Reusing a child does not generally descend: the two-draw law contains $m(x)m(y)[1+a(x)a(y)]$, and a same-child belief/model response contains the relative contrast $a(k)b(m)$. Unrestricted external Gibbs probes also invalidate the symmetry interface.

There is only a local selection statement. Initially set $w_A=w_B=\varepsilon$, let $m_B=\chi_\#m_A\ne m_A$, and take every row uniform. If $C(\varepsilon)/2<D(m_A\Vert m_B)$, then $D_{\rm cross}>D_{\rm within}$ and $\dot p=(2/9)(D_{\rm cross}-D_{\rm within})>0$. Strict gaps persist for a nonzero interval. No all-time gap or dynamically selected second-stage handoff was proved. The potential and priors contain no pair labels, but the admitted symmetry preparation supplies the relations that make the quotients possible.

### Two scoped obstructions

On an open full product family, a common-rate ansatz $\dot\ell_i=a_q(\mathbf q,\mathbf s)(H_i-\ell_i)$ implies $d_{q_i}E=a_qdH_i$. In the original architecture, cross-agent mixed derivatives $d_{q_i}d_{s_j}E$ vanish for $i\ne j$. Varying $q_i$ forces $a_q$ to be independent of every model law, after which the same-agent mixed derivatives vanish too. This requires $\log G_i(m,k)=u_i(k)+v_i(m)$, and normalization makes the evaluator independent of its model argument. Thus this specific common-rate ansatz cannot hold on such an open family with a genuinely coupled evaluator. Restricted invariant families and additional spectrum-preserving motion are outside this statement.

For an analytic vector field in a connected analytic product chart and a fixed analytic retention $R(z,w)=z$, projectability is $\partial_wV_z=0$. If it holds on a nonempty open region, analytic continuation makes it hold throughout the chart. This only rules out the first onset of that fixed analytic quotient on an open region. It does not rule out membership selection, preexisting quotients, lower-dimensional invariant families, or smooth nonanalytic channels.

## Next decisive obligation

The next construction must exhibit a nonconstant boundary protocol already present in the original model that factors through a genuinely compressive public retention, and prove controlled projectability under the resulting external interactions. For subsystem retentions this is

$$
DR_I(x_I)V_I(x_I;e)=\bar V_I(R_Ix_I;R_{\rm ext}e).
$$

Joining must also descend: $R_{I\cup J}\mathcal J_{I,J}=\bar{\mathcal J}_{I,J}(R_I,R_J)$. Membership selection and a later formation stage remain separate obligations. A newly declared phase-sampling channel does not discharge them. The unrestricted identity-Gibbs theorem shows that some restriction or an additional sufficient structure is necessary for public information loss in that interface class.

The phase proof is now in the main manuscript with a self-contained explanation in `companion/c09_public_compression.tex`. The symmetry calculation remains in this research record because its preparation and the kind of compression differ from the requested continuous collective reduction.

## External primary sources

[Horstmeyer and Atay, “Characterization of exact lumpability for vector fields on smooth manifolds”](https://doi.org/10.1016/j.difgeo.2016.06.001), Differential Geometry and its Applications 48 (2016), 46–60, supplies the general flow-projection context. Its primary repository PDF was read. The present proof does not use a maximal-time claim from that paper.

[Eldering, Kvalheim, and Revzen, “Global linearization and fiber bundle structure of invariant manifolds”](https://arxiv.org/abs/1711.03646), Nonlinearity 31 (2018), 4202–4245, describes stable-foliation structure for finite-dimensional normally attracting manifolds. The paper was read for the relevant hypotheses. Its finite-dimensional theorem is not invoked as a general probability-law theorem; the Banach-chart phase argument above is supplied directly. Neither reference is evidence for endogenous recursive formation in this model.

## Document validation

The final main manuscript has 61 pages and the companion has 28. Both TeX Live builds succeeded with no LaTeX warnings, overfull boxes, or underfull boxes. Source checks covered 35 TeX files and 311 labels, with no duplicate labels, missing citation keys, prohibited spacing commands, or trailing whitespace. All 89 pages were rendered at 110 dpi and inspected in contact sheets; the new main pages 50–54 and companion pages 23–24 were also inspected at readable resolution. A new short spill page was removed; the preexisting short main page 21 was left unchanged. The supplement was unchanged.

Main PDF SHA-256: `366b8991a8bc50b9dd28938012145188a6e7ca26ffa61716ceabe1426c53e4d6`. Companion PDF SHA-256: `a141d3b1377989c86c305dae46187f1b00c2f15cdf75370ee536db000d9d7a3e`. Local build receipts are in the package build directory; these are document checks, not independent mathematical verification.
