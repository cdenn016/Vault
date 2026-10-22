<!-- rigorous-theory-search-metadata {"schema_version":"rigorous-theory-search/v1","contract_id":"contract-sha256-b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe","target_digest":"b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe"} -->
# Two stages of native preferential routing on an open law domain

## Statement and relation to the target

There exist a fixed positive temperature, six homogeneous agents with fixed uniform source priors, normalized identity comparison channels including self channels, a common uniform evaluator and reference law, and a nonempty open subset of the full twelve-dimensional interior binary-law domain, such that the original two-sector Fisher flow has the following behavior. Every off-diagonal native routing weight is initially below the same threshold. Three preferential pairs then form and coexist for a positive interval. Two of these parents subsequently join while the third remains a nonempty exterior against which their routing preference is strict. All event times are finite and interior. The same selector and the exact aggregated native routing rows are used at both stages. No parameter changes, time gates, resets, new attraction, or externally supplied membership tree occur.

This is a theorem about the routing and temporal-selection part of the frozen target. It does not by itself prove that the selected parents have a compressive autonomous realization, that a specified joint response interface descends, or that collective geometry survives a handoff. In particular, an arithmetic aggregate of routing rows is not asserted to be a fresh ordinary KL-softmax row evaluated at one averaged child law. Those are separate interface obligations. The six-agent extension below is needed because a four-agent construction alone would make the complement empty at its second join.

The supplied assumptions are the smooth two-sector KL/Fisher model, equal unit mobilities, fixed positive temperatures and priors, and permission to use normalized deterministic channels and finite alphabets. The route-specific choices are a binary alphabet, a uniform local reference joint, self-inclusive identity comparison, the threshold and contrast rule below, and an open initial multiscale separation regime. The theorem is existential over this regime. It is not a claim for every initial law or for an unspecified random initialization.

## Exact model, state space, and selector

Let both sample spaces be \(\{-1,1\}\) with counting measure, and set

\[
q_i(k)=\frac{1+kx_i}{2},\qquad
s_i(m)=\frac{1+my_i}{2},\qquad
z=(x,y)\in M_N=(-1,1)^{2N}.
\tag{S1}
\]

All \(2N\) coordinates vary independently. Set the normalized reference and evaluator to \(r(m)=1/2\) and \(G(k\mid m)=1/2\); this is the \(J=0\) specialization of the binary evaluator in the companion route. Every agent is an allowed source for every receiver, including itself. In both sectors take \(\pi_{ij}=1/N\), a fixed \(T>0\), and the identity comparison kernel. Put

\[
\begin{aligned}
\psi(u)&=\frac{1+u}{2}\log(1+u)+\frac{1-u}{2}\log(1-u),\\
d(u,v)&=\operatorname{KL}(q_u\Vert q_v),\\
\beta_{ij}(x)&=\frac{\exp[-d(x_i,x_j)/T]}{\sum_{k=1}^N\exp[-d(x_i,x_k)/T]}.
\end{aligned}
\tag{S2}
\]

The energy, metric, and dynamics are exactly

\[
\begin{aligned}
E_T(x,y)&=\sum_i[\psi(x_i)+\psi(y_i)]
-T\sum_i\log\left(\frac1N\sum_j e^{-d(x_i,x_j)/T}\right)
-T\sum_i\log\left(\frac1N\sum_j e^{-d(y_i,y_j)/T}\right),\\
g_z&=\sum_i\left[\frac{dx_i^2}{1-x_i^2}+\frac{dy_i^2}{1-y_i^2}\right],
\qquad \dot z=-\operatorname{grad}_{g}E_T.
\end{aligned}
\tag{S3}
\]

This is a continuous deterministic system with its original time \(t\geq0\), no noise, no discrete update, and no boundary identification. All densities and compared laws are positive in \(M_N\). The constitutive data are analytic there. Both sectors have identical independent vector fields because the chosen local evaluator is uniform; independence here describes the equations, not an equality constraint on initial coordinates.

For a partition \(\mathcal P\) into current blocks define, separately in each sector,

\[
B_{IJ}=\frac1{|I|}\sum_{i\in I}\sum_{j\in J}\beta_{ij},
\qquad I,J\in\mathcal P.
\tag{S4}
\]

These are normalized rows and retain \(B_{II}\). Their response experiment is: choose a receiver uniformly in \(I\), sample its native source index, and report that source's current block. At the next coarsening, the exact identity is

\[
B_{CD}=\frac1{|C|}\sum_{I\subset C}|I|\sum_{J\subset D}B_{IJ}.
\tag{S5}
\]

Thus receiver rows are averaged with inherited cardinalities, source columns are summed, and no prior or temperature is refitted. Equation (S5) follows by interchanging finite sums and is associative under any sequence of coarsenings.

Fix once and for all

\[
\eta=\frac1{10},\qquad \delta=\frac1{20}.
\tag{S6}
\]

Two distinct current blocks \(I,J\) qualify when, in both sectors and both directions,

\[
B_{IJ}>\eta,
\qquad
B_{IJ}-\sum_{K\in\mathcal P\setminus\{I,J\}}B_{IK}>\delta.
\tag{S7}
\]

The sum on the right is routing mass to the complement of the candidate pair. Self mass is retained in normalization but does not count as a peer edge or as exterior mass. No claim that a peer must beat the self loop is part of this criterion. A qualifying current vertex has at most one qualifying partner: if two partners qualified, each would have to exceed the other by more than \(\delta\). Consequently qualifying edges are disjoint and all may be merged at an event without a label-dependent tie rule. At the first threshold contact assign the event using the closed inequalities; the constructed crossings are transverse and the strict inequalities hold immediately afterward. The construction keeps the contrast inequality strict at every entry, so it is the edge threshold that sets the event time. This is a state-based detector and aggregation rule; it changes no fine-level force.

## Complete derivative and global contraction

The elementary binary derivatives are

\[
\partial_ud(u,v)=\operatorname{atanh}u-\operatorname{atanh}v,
\qquad
\partial_vd(u,v)=\frac{v-u}{1-v^2}.
\]

Differentiating both receiver and sender occurrences in every log normalizer gives

\[
\dot x_i=(1-x_i^2)\left[-\operatorname{atanh}x_i
-\sum_j\beta_{ij}(x)(\operatorname{atanh}x_i-\operatorname{atanh}x_j)\right]
+\sum_k\beta_{ki}(x)(x_k-x_i).
\tag{S8}
\]

The equation for \(y_i\) is identical. The terms with coincident indices vanish, as they must because \(d(x_i,x_i)=0\). In particular, the last sum is present; omitting it would give a different model.

Let \(\theta_i=\operatorname{atanh}x_i\). At a maximum of the coordinates \(\theta_i\), all receiver differences are nonnegative and all sender differences are nonpositive. At a minimum the inequalities reverse. The one-sided derivatives of the finite maximum and minimum therefore satisfy

\[
D^+\max_i\theta_i\leq-\max_i\theta_i,
\qquad
D_+\min_i\theta_i\geq-\min_i\theta_i.
\]

Multiplication by \(e^t\), followed by integration on each interval where an extremizing index is fixed and continuity across its switches, yields

\[
\min_i\theta_i(0)e^{-t}\leq\theta_i(t)
\leq\max_i\theta_i(0)e^{-t}.
\tag{S9}
\]

The same bounds apply in the model sector. They keep every solution in a compact interior box for all forward time. On that box the vector field is continuously differentiable and bounded. Local existence and uniqueness therefore extend globally: a finite maximal time would have a limit in the box, where local existence extends the solution. Equation (S9) proves convergence to the sole equilibrium \(x=y=0\). It also shows that the exact routing rows converge to \(1/N\), though that asymptotic fact alone does not establish the required order of finite events.

For completeness, the actual continuous flow has

\[
\frac{dE_T}{dt}=-\sum_i\left[\frac{\dot x_i^2}{1-x_i^2}+\frac{\dot y_i^2}{1-y_i^2}\right]\leq0.
\tag{S10}
\]

No assertion about a discretized algorithm follows from (S10). The finite-stage proof below uses the full vector field directly.

## A regular small-scale limit without a time change

Introduce a positive parameter \(h\), set \(T=h^2\), and write \(x_i=hu_i\). This is used to choose one fixed positive temperature, not to change it during a trajectory. On every fixed compact set of \(u\)-coordinates,

\[
\frac{d(hu,hv)}{h^2}\longrightarrow\frac{(u-v)^2}{2}
\tag{S11}
\]

with all derivatives needed below as \(h\downarrow0\). For example this follows by inserting the convergent power series of \(\log(1\pm hu)\) and \(\log(1\pm hv)\) on a compact set with \(h\max(|u|,|v|)<1\). Divide (S8) by \(h\) without changing time. Its limiting field is

\[
\dot u_i=-u_i+\sum_j(w_{ij}+w_{ji})(u_j-u_i),
\qquad
w_{ij}=\frac{e^{-(u_i-u_j)^2/2}}{\sum_k e^{-(u_i-u_k)^2/2}}.
\tag{S12}
\]

The vector fields and routing functions converge in \(C^1\) on compact sets. This limit is a calculation in binary-law coordinates. It makes no Gaussian-law assumption. The self summand is one, so no denominator approaches zero.

The vector field in (S12) is smooth. Its maximum coordinate has derivative at most minus that coordinate, and its minimum has derivative at least minus that coordinate. Thus solutions exist globally and remain bounded on finite intervals. A solution of the exact scaled field stays close to a solution of (S12) on a fixed finite interval: on a compact tube let the limiting field have Lipschitz constant \(K\), and let the uniform field error be \(\epsilon_h\to0\). Until exit from the tube, their difference is bounded by \(\epsilon_h(e^{Kt}-1)/K\), with \(t\epsilon_h\) when \(K=0\). Choosing this bound smaller than the tube radius prevents exit. The same estimate with an initial discrepancy proves continuous dependence on initial coordinates. Combining it with \(C^1\) convergence of the routing functions preserves strict windows and transverse crossings. These are the only perturbation facts used below.

## Four-agent core: first events and an explicit separation estimate

First analyze (S12) with four agents on the reflection-invariant configuration

\[
u=(-a-b,-a+b,a-b,a+b),\qquad a(0)=A,\quad b(0)=2.
\tag{S13}
\]

Reflection equivariance and uniqueness preserve this form. Let

\[
\begin{gathered}
w=e^{-2b^2},\quad v_0=e^{-2a^2},\quad
v_+=e^{-2(a+b)^2},\quad v_-=e^{-2(a-b)^2},\\
Z_+=1+w+v_0+v_+,\qquad Z_-=1+w+v_0+v_-,\\
c_p=w(Z_+^{-1}+Z_-^{-1}),\qquad c_0=v_0(Z_+^{-1}+Z_-^{-1}).
\end{gathered}
\]

Substitution into all terms of (S12) gives

\[
\begin{aligned}
\dot a&=-a-2ac_0-2\left[\frac{(a+b)v_+}{Z_+}+\frac{(a-b)v_-}{Z_-}\right],\\
\dot b&=-b-2bc_p-2\left[\frac{(a+b)v_+}{Z_+}-\frac{(a-b)v_-}{Z_-}\right].
\end{aligned}
\tag{S14}
\]

These equations include the unequal row normalizers. Replacing the two normalizers by one before estimating would not be exact.

For \(a\geq4\) and \(0\leq b\leq2\), set \(c=1+w+v_0\geq1\) and

\[
g_c(r)=\frac{r e^{-2r^2}}{c+e^{-2r^2}}.
\]

Differentiation gives

\[
|g_c'(r)|\leq(1+4r^2)e^{-2r^2}.
\]

The right side decreases for \(r\geq2\). Applying the mean value theorem while holding the instantaneous \(c\) fixed yields

\[
|g_c(a+b)-g_c(a-b)|
\leq2b[1+4(a-2)^2]e^{-2(a-2)^2}
\leq34be^{-8}.
\]

Since \(0\leq c_p\leq1\), (S14) therefore implies

\[
-4b\leq\dot b\leq-\frac b2.
\tag{S15}
\]

Similarly, positivity of all terms and

\[
\frac{-\dot a}{a}
\leq1+4e^{-2a^2}+4e^{-2(a-b)^2}<2
\]

give

\[
-2a\leq\dot a\leq-a.
\tag{S16}
\]

The axes \(a=0\) and \(b=0\) are invariant wherever the reflection form is regular, and uniqueness prevents a positive coordinate from reaching them in finite time. In the region used here, (S15)-(S16) keep \(b\leq2\) and \(a>0\) until \(a=4\).

Take \(A\geq4096\). Let \(\tau\) be the first time \(b=1/2\), and let \(t_A\) be the first time \(a=4\). Equations (S15)-(S16) show

\[
\tau\leq2\log4,\qquad a(t)\geq A/256\geq16
\quad(0\leq t\leq\tau).
\tag{S17}
\]

At time zero each within-pair off-diagonal weight is at most \(e^{-8}\), and each cross-pair weight is at most \(e^{-2(A-2)^2}\). Thus all off-diagonal weights are initially strictly below \(\eta\).

Every within-pair directed weight has the form

\[
p_\pm=\frac{w}{1+w+v_0+v_\pm}.
\]

For \(0\leq t\leq\tau\), \(b\geq1/2\), so \(\dot w=-4b\dot b w\geq w/2\). Also (S15)-(S16) imply

\[
|\dot v_0+\dot v_\pm|
\leq8a^2e^{-2a^2}
+4(a+2)(2a+8)e^{-2(a-2)^2}<\frac1{100}
\quad(a\geq8).
\tag{S18}
\]

The last inequality follows by differentiating its two elementary positive summands to check they decrease on \([8,\infty)\), and evaluating their upper bounds there. Consequently

\[
\dot p_\pm=
\frac{\dot w(1+v_0+v_\pm)-w(\dot v_0+\dot v_\pm)}{(1+w+v_0+v_\pm)^2}>0.
\tag{S19}
\]

At \(t=\tau\),

\[
p_\pm\geq\frac{e^{-1/2}}{1+e^{-1/2}+2e^{-8}}>\frac14.
\tag{S20}
\]

Each within-pair row therefore crosses \(\eta\) once and transversely before \(\tau\). Throughout this first formation window all its exterior mass is at most \(2e^{-2(a-b)^2}\), hence less than \(2e^{-8}\) and in fact much smaller because \(a\geq16\). The contrast condition in (S7) is strict at the threshold. The left and right pairs can be selected at different times under perturbation; each pair's time is the last of its two directional, two-sector threshold crossings.

After \(\tau\) and until \(t_A\), the bounds \(b\leq1/2\), \(a\geq4\) preserve (S20), while every primitive cross-pair weight is at most \(e^{-8}\). A source column belonging to a formed pair contains only two primitive entries, so its aggregated cross mass is at most \(2e^{-8}<\eta\), regardless of whether the other pair has already formed. This excludes a premature cross join while some vertices are still singletons. Both selected pairs persist, with strict contrast, throughout \([\tau,t_A]\). Finally,

\[
t_A\geq\frac12\log(A/4),\qquad
0<b(t_A)\leq2e^{-t_A/2}\leq2(A/4)^{-1/4}.
\tag{S21}
\]

Thus their residual internal half-gap at \(a=4\) can be made arbitrarily small by choosing one sufficiently large finite \(A\), while their coexistence interval has positive length.

## Four-agent core: the later parent event

Compare the late part of (S14), starting at \(a=4\), with its invariant duplicated-pair trajectory \(b=0\). On this comparison trajectory, put

\[
v=e^{-2a^2},\qquad B=\frac{v}{1+v}.
\]

The primitive within-pair peer weight, the exact parent cross weight, and the center equation are respectively

\[
p=\frac{1-B}{2},\qquad
B_{\{1,2\},\{3,4\}}=B_{\{3,4\},\{1,2\}}=B,
\qquad
\dot a=-a(1+4B).
\tag{S22}
\]

There is no renormalization that discards self loops: the inherited self mass is \(1-B\). Direct differentiation gives

\[
\dot B=\frac{4a^2v(1+4B)}{(1+v)^2}>0
\quad(a>0).
\tag{S23}
\]

Starting from \(a=4\), this trajectory crosses \(B=\eta\) exactly once, at

\[
a_c=\sqrt{\frac12\log9}.
\]

Let \(S>0\) be its unique time of reaching \(B=1/5\), equivalently \(a=\sqrt{\log4/2}\). It is finite because \(\dot a\leq-a\), and

\[
S\leq\log\left(\frac4{\sqrt{\log4/2}}\right).
\tag{S24}
\]

On the entire compact interval \([0,S]\), each primitive peer weight is at least \(2/5\), its total opposite-pair mass is at most \(1/5\), and hence its original pair contrast is at least \(1/5>\delta\). The parent crossing is transverse and is strictly inside this interval. These margins avoid relying on a time after the first pairs have already lost their preferential contrast.

Smooth dependence of (S14) and its routing rows on the initial half-gap gives an \(\varepsilon_b>0\) such that the same strict windows and a transverse parent crossing hold for \(a(0)=4\), \(0\leq b(0)<\varepsilon_b\). For example, surround the unique comparison crossing by a closed small interval where \(\dot B\) has a positive minimum; outside it the sign of \(B-\eta\) has a nonzero compact minimum. Small \(C^1\) changes preserve both facts and all contrast margins. Equation (S21) lets us choose a finite \(A\geq4096\) with \(b(t_A)<\varepsilon_b\). Fix that \(A\). This proves the two temporal stages on the fixed finite horizon

\[
L=t_A+S.
\tag{S25}
\]

For four agents the second event only gives a mutual parent edge, because the two parents exhaust the population. The next step supplies a nonempty exterior without changing either mechanism.

## A distant third pair gives nonvacuous second-level preference

Use six agents in (S12), with reference initial coordinates

\[
u(0)=(-A-2,-A+2,A-2,A+2,R-2,R+2).
\tag{S26}
\]

Compare this with the decoupled system consisting of the proved four-agent core and an isolated pair. For that pair write

\[
u_5=Re^{-t}-b_c,\qquad u_6=Re^{-t}+b_c,
\qquad b_c(0)=2.
\]

Its exact isolated equations and peer weight are

\[
\dot b_c=-b_c(1+4p_c),\qquad
p_c=\frac{e^{-2b_c^2}}{1+e^{-2b_c^2}}.
\tag{S27}
\]

Thus \(p_c(0)<\eta\), \(\dot p_c>0\), and \(b_c\leq2e^{-t}\); by time \(\log4\) it has a peer weight above \(1/4\). Its threshold crossing is transverse, and its exterior mass in the decoupled comparison is zero.

Here is the required finite-time decoupling estimate. Subtract \(Re^{-t}\) from coordinates 5 and 6. In these moving coordinates the decoupled pair field is independent of \(R\), since the interaction depends only on coordinate differences and the local drift is exactly \(-u_i\). On a fixed radius-one tube about the decoupled trajectories for \(0\leq t\leq L\), the core coordinates have absolute value at most \(A+3\), and the two moving coordinates have absolute value at most 3. Every cross-group separation is therefore at least

\[
D_R=Re^{-L}-A-6.
\tag{S28}
\]

Choose \(R\) so that \(D_R>2\). Every self-inclusive row denominator is at least one. Direct differentiation of the numerator gives

\[
\left|\frac{d}{dr}e^{-r^2/2}\right|=|r|e^{-r^2/2},\qquad
\left|\frac{d}{dr}\left(re^{-r^2/2}\right)\right|
\leq(1+r^2)e^{-r^2/2}.
\]

The denominator difference between a six-agent row and its isolated-group row is a sum of at most four cross numerators. Applying the quotient rule, and using the bounded within-group differences in this tube, bounds the difference of the two fields and their first derivatives by

\[
\epsilon_R\leq C_A\sup_{r\geq D_R}(1+r^2)e^{-r^2/2}\longrightarrow0.
\tag{S29}
\]

The finite constant \(C_A\) can depend on the fixed core bound \(A+3\), but not on \(R\) or time. Products of numerator and denominator derivatives obey the same bound after enlarging it: a cross derivative supplies at most one factor \(r\), and differentiation of its force factor supplies at most a second. The same estimates give convergence of routing values and their spatial derivatives on the tube. For their explicit time derivatives in the moving coordinates, differentiating \(Re^{-t}\) supplies at most \(Re^{-t}|r|\); since \(Re^{-t}\leq |r|+A+6\) in this tube, (S29) bounds these derivatives as well after enlarging \(C_A\). Consequently the routing time derivatives converge along trajectories. Thus this is convergence of the full six-agent field, including incoming effects and the changed normalizers; distant agents have not simply been omitted from a row.

In moving coordinates the decoupled field has a finite Lipschitz constant \(K_A\) on this compact tube, independent of \(R\). The difference of trajectories is bounded, up to a possible first exit, by \(\epsilon_R(e^{K_A L}-1)/K_A\). Choose a finite \(R\) for which this is smaller than half the tube radius and smaller than all finite event and contrast tolerances above. The bound then precludes exit. The exact six-agent trajectory inherits the three initial pair events, a positive interval with all three pairs present, and the later transverse cross-edge event between the two core parents. It also keeps every row mass between the core and the third pair as small as desired throughout \([0,L]\), for instance below \(10^{-3}\) after aggregation.

At the later event, both directed core-parent masses cross \(\eta\), while their masses to the third parent are less than \(10^{-3}\). Hence their routing contrast is larger than \(0.099>\delta\) immediately after entry. The same estimates keep the third parent's mass to either core parent below \(\eta\), and keep its mass to their union below \(\eta\) after that join. It therefore supplies a genuine exterior and does not join during the proved window. At earlier times aggregated unwanted source columns contain at most four primitive entries, so choosing the cross-group tolerance this small also excludes joins of a pair with a remaining singleton. Inside the core, (S17)-(S20) already exclude these premature events.

The first-stage pairs retain strict primitive peer-versus-complement contrast until the second event and beyond it for a positive interval. The selected core-parent pair also retains (S7), against the third parent, on a positive interval after its entry. All of these are finite strict inequalities. The construction proves three first-stage pairs, of which two form a second-stage parent; it does not claim that the third pair stays isolated forever.

## Transfer to one exact positive temperature and a full open law set

The order of choices matters. First fix the comparison tolerance and a sufficiently large finite \(A\) using (S21). Then fix a sufficiently large finite \(R\) using (S28)-(S29), for the resulting finite horizon \(L\). Finally take one sufficiently small \(h>0\) so that the exact binary scaled field and its routing functions are \(C^1\)-close to the six-agent field on a compact tube containing this reference trajectory, and so that \(h\max_i|u_i|<1\) on that tube. Fix \(T=h^2>0\) permanently.

In both sectors take the exact reference initial means to be \(h\) times (S26). Equation (S11) and the finite-tube estimate following (S12) transfer all initial bounds, formation windows, absence of unwanted joins, positive persistence intervals, and transverse threshold crossings to this exact binary model. The uniform priors are now exactly \(1/6\); their common row factor cancels in the Gibbs normalization. In particular, \(\eta<1/6\), as required for initial self isolation followed by eventual communication.

Now vary every initial \(x_i\) and \(y_i\) independently in a sufficiently small neighborhood of this exact reference point. Smoothness and compact-tube continuous dependence preserve all the preceding strict inequalities. For each threshold crossing retain a small time interval with a strictly positive crossing derivative and preserve the threshold sign outside that interval. Each of the finitely many directional sector crossings then remains unique in its interval. A pair's event is the latest of its four crossings, and all four have occurred before the next separated event window. This proves that a nonempty open

\[
U_0\subset(-1,1)^{12}
\tag{S30}
\]

has the stated behavior. No equality of beliefs, models, laws, or parameters is imposed on \(U_0\). The equal-sector and reflection forms were comparison trajectories used to establish open strict windows, not restrictions on admissible initial data.

Choose the neighborhood small enough that all means in each sector are initially distinct. The diagonal \(x_i=x_j\) is invariant under the equivariant sector field; local uniqueness in both time directions prevents first collision at a finite interior time. Thus these child laws remain distinct throughout the finite construction. Finally replace \(U_0\) by the union of all its population permutations. The resulting \(U\) is nonempty, open, and invariant under relabeling. The fixed evaluator, channels, priors, temperature, threshold, and contrast contain no block labels. Labels in (S26) only describe one neighborhood in this union. Membership and the later pairing are read from the evolving native rows by (S7).

## Supported result and remaining interface obligation

The result is an exact finite-time existence theorem for two stages of native preferential routing under the original full Fisher flow, with a nonempty exterior at the second stage. The use of limiting fields is confined to a proof of existence of finite constants \(A,R,h\); the actual witness has six agents, one fixed \(T>0\), analytic positive interior laws, the original clock, and no stochastic or numerical approximation. The proof supplies parameter inequalities and a constructive order of choices, rather than a calibrated numerical interval for \(T\).

The exact block-response identity (S5) is proved, but it does not make \(B\) alone an autonomous parent state. Nor does it imply that retaining the whole tuple and forgetting no public information is an admissible compression. The minimal missing interface is a concrete retention that preserves the fine-dependent rows and original-time dynamics, descends a predeclared class of finite joint response histories, forgets a continuous nongauge public-law distinction after retained memory and event times, and preserves the specified collective Fisher geometry. A companion physical-phase construction may address that interface; it is not assumed here. The theorem also does not prove unlimited recursion or permanent separation of the last exterior pair.

This route uses the same live source basis as the companion `native-cliques.md`: `MAgent_Theory_2.0/chapters/03_dynamics.tex` for the potential and full derivative, `05_inheritance.tex` for the binary evaluator specialization, and the formation and scope chapters recorded in `source-manifest.json`, at Research revision `8d870cd956253f06d7c89f1627ab05e0a3946445`. It preserves that earlier bistable result. All estimates here are analytical. No numerical experiment, symbolic script, GPU computation, Lean proof, or additional agent was run for this assignment.
