# Boundary closure under the original smooth KL dynamics

The strongest result is an exact recursive hierarchy with a genuinely coupled evaluator, unchanged identity peer channels, general base laws, and distinct public children. It preserves fresh uniform-descendant response laws, the ensuing finite response histories, and common base-record conditioning. At every representation join it discards a continuously variable public partition field. The hierarchy and the invariant initial family are supplied. The compression is continuous in total variation, not a smooth reduction of Fisher dimension on an open law chart. Endogenous formation remains open.

This continues the public-compression record at `2026-10-21-public-compression.md`, starting from Research commit `c1537645d660bb770fd475d90a3ee59da218da0a`. The user asked to find a parent compressing distinct public laws while exactly inheriting dynamics and responses and composing recursively, with the original smooth dynamics and no prescribed erasure gates. Earlier publication authorization remains applicable. Source consultation covered the live manuscript's original potential, complete channel derivative, record model, inheritance definitions, conditional-spectrum construction, phase theorem, and previous response obstructions. No numerical experiments, GPU work, Lean, or independent adjudication ran.

## Original-model recursive construction

The complete construction and decisive proof are in `manuscripts/MAgent_Theory_2.0/chapters/10_boundary_closure.tex`; the self-contained explanation is in `companion/c10_boundary.tex`.

Fix a supplied binary tree of depth d with N=2^d leaf agents. Each sector has an arbitrary standard Borel base with probability reference A or B, and one independent Haar circle per internal node. A normalized positive bounded joint density rho(r,w) supplies the fixed proper coupled evaluator, independently of the circle coordinates. Every primitive recognition law remains q_i tensor s_i. All physical peer channels are identities, all nonself edges are present, and the original source priors are uniform.

At internal node v put sigma_v=sign cos(theta_v-alpha_v(r)), where alpha_v is any measurable phase field. A leaf reads its signed path bits u_j=epsilon_j sigma_v. For an arbitrary bounded positive profile f(r,u), normalized against A times the uniform d-bit law U, let q_i(r,theta)=f(r,u(i,theta)); define model laws through an independent profile g. Each child has base marginal f_0 A, but the full public laws need not agree. Their dependence on the circle coordinates is part of the original public state.

For sources separating after k shared edges, let n_k=2^(d-k-1), and let each fine edge have weight b_k/n_k. Uniform original rows correspond to pi_k=n_k/(N-1). Define P_k to keep the first k bits, flip the next, and average the remaining bits. This is a finite profile operator for an exact average over original labels; it is not a substituted physical channel. It is Markov and self-adjoint for U.

Every original directed cost in that class equals

$$
D_k(f)=\int f(\log f-P_k\log f) dA dU.
$$

The original energy and Fisher metric are exactly N times the profile energy and metric. The profile energy contains the local entropies, the coupled term -integral f_0 g_0 log rho, the sums of b_k D_k, and the original row entropies KL(b||pi). The profile metric is the ordinary product Fisher metric on f,g,b. No new mobility or timescale is inserted.

The complete derivative is

$$
\delta D_k=\int\delta f\left(\log f+1-P_k\log f-\frac{P_kf}{f}\right) dA dU.
$$

Thus the full profile force is

$$
h_q=2\log f+V_q-\sum_kb_k^q\left(P_k\log f+\frac{P_kf}{f}\right),
\qquad V_q(r)=-\int g_0(w)\log\rho(r,w) dB(w),
$$

with dot f=-f(h_q-E_f h_q), the exchanged model equation, and the original Fisher row equation. The incoming ratios are retained. Pointwise averaging all descendants in a sibling subtree gives exactly P_k f and P_k log f, so these equations are the full fine field, not a projected approximation. Every leaf has the same normalizer. The family is invariant on its regular existence interval. The same argument applies with the original Gibbs-reduced class weights pi_k exp(-D_k/T) normalized across k.

The inherited cost is not generally KL to the average source. Its difference from KL(f||P_k f) is the nonnegative term integral f[log(P_k f)-P_k log f]. It is itself exactly KL(J_k||J_k reversed), where J_k(dr,du,dv)=A(dr)f(r,u)U(du)P_k(u,dv). Dropping the Jensen term changes the original dynamics.

At a subtree retain the complete nested unordered tree of descendant profile values, as a function of the base and still-public ancestor coordinates. Keep row-class data, primitive counts, and the remaining connections. A flat multiset is insufficient: lowest-common-ancestor grouping affects D_k. The parent public response law is the subtree mean; the profile tree supplies the additional dynamical state.

Changing a physical partition sign only exchanges branches. Rooted tree automorphisms preserve U, P_k, the energy, and the metric. They commute with the full profile field, including measurable base-dependent exchanges. The local evaluator reads only f_0,g_0, so separately retaining the two sectors loses no branch copula used by this evaluator. Partial retentions give a closed joint parent network with its complement in the prepared family. This is not closure under every possible external law.

Joining sibling descriptors forms their unordered pair. Nested joins compose and disjoint joins commute. Every representation describes the same already coupled N-agent graph. Adding edges between previously isolated systems or reassociating arbitrary leaves would be a different operation. The result supplies a recursive representation hierarchy, not dynamically selected membership.

## Exact response and feedback scope

The response protocol is fixed independently of the retention: freshly choose a descendant uniformly, freshly sample its full original public coordinate, and conceal the label. At depth l its density is f_l=E[f|first l path bits], which is exactly the mean of its retained subtree. Full output coordinates are preserved. Uniform parent choice followed by uniform descendant choice equals direct uniform descendant choice at every level. The model protocol uses a separate fresh label. Existing observed history is carried forward as controller state at representation joins.

A normalized common likelihood L_e(o|r) has the same probability under every child because their base marginal is f_0. Conditioning the mixture components therefore leaves their label weights uniform and gives f^+=L_e f/Z, Z=integral f_0 L_e dA. This scales every profile value at a base point by the same factor and commutes with every retention and join. Model updates work separately. Inputs may depend on observed history. Induction gives equality of every finite adaptive response-history law, with the original continuous flow between regular record updates.

Reusing a hidden child for multiple samples does not generally descend. For q_±=m(1±a sigma), its two-draw law contains m(k)m(k')[1+a(k)a(k')sigma(k)sigma(k')]. A shared belief/model child label can expose relative contrasts. Unrestricted external identity probes also lie outside the inherited interface. These are concrete limitations, rather than missing normalizers in the proved protocol.

To witness public loss at every level, choose initially f=f_0 product_j(1+a_j u_j), with 0<a_j<1 and regular bounds. This factorization is only an initial condition; the full positive profile evolves thereafter. The two child-parent response laws at each next branch differ. Rotating that node's phase changes those laws while its joined unordered tree is unchanged. The strict differences persist on a nonzero regular time interval. A phase displacement delta changes a fraction |delta|/pi of the circle signs, giving a nonzero total variation distance proportional to |delta|. The phase fields may be arbitrary measurable functions of the base, so the loss is not merely a global child permutation.

The squared Hellinger distance is also proportional to |delta|. These phase paths have no finite Fisher tangent and are discontinuous in the bounded-log-density norm. The original time evolution is smooth on each fixed-partition profile chart. The retained amplitude tree can grow with the number of children; this is not a constant-size sufficient statistic or a smooth dimension reduction on an open density chart.

## A separate associative construction with selective channels

This second exact result is retained here because it has stronger freedom of regrouping but a weaker evaluator assumption. It uses the product-evaluator special case of the original potential. It does not replace the coupled identity-channel construction in the main manuscript.

Let (X,A) be a standard Borel probability space, T:X to R^d a fixed bounded observable with norm at most R, and q_i=f_i A arbitrary positive bounded-log densities. The local term is KL(q_i||A). An independent copy can be used in the model sector with a product joint reference. Put

$$
m=N^{-1}\sum_iE_{q_i}T,\qquad
\mathcal A(\lambda)=\log\int e^{\lambda\cdot T}dA,
\qquad \nu_{m,e}=e^{\lambda(m,e)\cdot T-\mathcal A(\lambda(m,e))}A,
$$

where e is compact-valued and lambda is a prescribed smooth function. Before defining the retention, prescribe the original channels

$$
K_{ij}(x,dy)=\varepsilon\delta_x(dy)+\nu_{m,e}(dy)-\varepsilon q_j(dy).
$$

A fixed epsilon can be chosen so that the residual is uniformly positive along the admitted complete flow. These are normalized channels with nonconstant sample dependence, and q_j K_ij=nu. They deliberately normalize the aggregate output from the start; they have no gate or trigger. The full variation is (dq_j)K=epsilon dq_j and q_j DK=dnu-epsilon dq_j, so d(q_j K)=dnu. The cancellation includes all source and channel derivatives.

Every source in a receiver row has the same cost. Consequently the exact matter potential is

$$
E=2\sum_i\operatorname{KL}(q_i\Vert A)+NW(m,e),\qquad
W=\mathcal A(\lambda(m,e))-\lambda(m,e)\cdot m.
$$

Rows either optimize to their priors or evolve independently of the matter laws. With

$$
c=\nabla_mW=(D_m\lambda)^T(\nabla\mathcal A-m)-\lambda,
$$

the full unit-Fisher log equation is

$$
\dot\ell_i=-2\ell_i-c\cdot T+C_i,\qquad
C_i=E_{q_i}(2\ell_i+c\cdot T),\qquad\ell_i=\log f_i.
$$

Choosing lambda=e+kappa m generally produces genuine dependence on other agents' laws. The coefficient two follows from the original energy.

For a block I, retain its primitive count N_I and the probability law P_I of (L_I,S_I)=(sum_i log f_i(X_i),sum_i T(X_i)) under independent X_i sampled from q_i. If eta_I is the same statistic's law under A^I, then P_I=e^L eta_I and eta_I=e^-L P_I. Both are normalized. Put

$$
C_I=E_{P_I}(2L+c\cdot S),\qquad v_I=-2L-c\cdot S+C_I.
$$

Differentiating the statistic under the fixed reference and then its exponential tilt gives the exact closed weak equation

$$
\frac{d}{dt}E_{P_I}\varphi
=E_{P_I}[(\partial_L\varphi+\varphi)v_I],\qquad
m=\frac{\sum_I E_{P_I}S}{\sum_I N_I}.
$$

This is an inherited transport and reweighting field, not a claim about the standard Fisher metric on arbitrary parent laws. It has an explicit solution. Set a(t)=exp(-2t), b(0)=0, dot b=-2b-c, and Z_I(a,b)=integral exp(aL+b dot S)d eta_I^0. Then eta_I^t is the pushforward by (L,S) to (aL+b dot S-log Z_I,S), and P_I^t=e^L eta_I^t. The retained mean is a smooth function of a,b. This gives a locally Lipschitz common tilt equation and uniqueness for bounded initial log densities.

For a global regular domain, suppose the initial log densities have sup norm at most L_0 and on the compact mean/input domain norm(lambda)<=L_lambda, norm(D_m lambda)<=L_D. Then norm(c)<=C=2R L_D+L_lambda and norm(b(t))<=C/2. The exact fine density is exp(a ell_i^0+b dot T), normalized against A, so exp(-2B)<=f_i<=exp(2B), with B=L_0+CR/2. The target density is at least exp(-2L_lambda R). A fixed 0<epsilon<(1/2)exp(-2L_lambda R-2B) keeps every channel residual positive for all admitted times and controls. The bounded tilt equation gives global continuation.

Joining is exactly (N_I,P_I) star (N_J,P_J)=(N_I+N_J,P_I*P_J). Independent sampling proves the identity; C_I and v_I add under convolution. Thus this operation intertwines the inherited dynamics and is associative under arbitrary regrouping, with primitive counts used in the global mean.

There are two predeclared nonconstant record protocols. A fresh transmitted source sample has law nu_{m,e}, inherited from the actual original channel. A fixed normalized collective readout H(do|sum_i T(X_i)) uses unmodified public samples and has law integral H(do|S)dP_I. It does not inspect the log density. A policy may choose the next input e from the record history; equality of retained states gives equality of all subsequent response and controlled-state laws by induction. This claim excludes arbitrary Bayesian resetting of the fine q_i, repeated use of one latent source sample, and observation of source-input/output correlations. Reusing just a source label is harmless when its content is freshly sampled.

The parent is noninjective beyond agent permutation. Let A=A_U tensor A_V, T=(t_U,t_V), and let a(U),b(V) be nonconstant normalized bounded positive densities. The pairs (f_1,f_2)=(ab,1) and (a,b) have the same joint reference law of (sum log f_i,sum T): swap only the two V slots under A^2. Their eta_I and P_I therefore agree. Their full public child laws differ, and one pair contains the reference while the other need not. The retention loses collective factor assignment, rather than keeping a separate spectrum for every child.

A general coupled evaluator is not included. A term J T(k)U(m) introduces J n_i T(k) into the belief force, n_i=E_{s_i}U. The block equation then requires sum_i n_i T(X_i), which (L_I,S_I) need not determine. The model equation has the corresponding assignment dependence. This is the precise missing closure, not a reason to claim that all general laws must be Gaussian.

## Local obstruction for ordinary mixture responses

The main chapter also proves a sharper obstruction than unrestricted Gibbs-probe identifiability. In the original two-agent binary model with q_i=b_{x_i}, s_i=b_{y_i}, coupled evaluator exp(Jkm)/(2 cosh J), and identity peers, put x_1,2=m±a, y_1,2=n±b. Fresh belief/model mixture responses expose m,n. The exact fine equation is

$$
\dot x_i=-(1-x_i^2)[2\operatorname{atanh}x_i-\operatorname{atanh}x_j-Jy_i]-(x_i-x_j),
$$

and its sector exchange. The final difference is the incoming derivative. The response velocities expand as F_x=f_x(m,n)+(6m-Jn)a^2-2Jmab+O(5), and the exchanged expression for F_y. At m=n=epsilon c, a=b=epsilon d, cd nonzero, the observation map H=(m,n,F_x,F_y) has

$$
\det DH=4\epsilon^4c^2d^2(6-3J)(6-J)+O(\epsilon^6).
$$

For |J|<1/4 and sufficiently small nonzero epsilon, this is nonzero on a heterogeneous open region. If a retention preserves both responses and their future evolution, equality of retained states implies equality of H. The inverse function theorem forces singleton local fibers. No smoothness of the retention is needed. This does not claim global identifiability or a universal obstruction for selective interfaces.

## Bounded unsuccessful routes and scope changes

An attempted smooth angular contrast q_±=m(1±a(theta)) does not generally keep a rotation-invariant fresh mixture under the full identity-peer force. Its angular mixture velocity contains -F(a)+d a, where F(a)=0.5 log(1-a^2)+3a atanh a and F''(a)=(5-a^2)/(1-a^2)^2>0. Constancy therefore permits at most two contrast values at each base point. A continuous contrast on a connected circle must be constant. This motivated balanced measurable partitions rather than a claimed smooth rotational profile manifold.

A calibrated-location construction also closes means, summed sample responses, and weighted-mean joins on supplied location families with arbitrary fixed non-Gaussian shapes. A proper quadratic reference and source Gaussianization make the restricted-family energy quadratic and metric constant. However, those location families are generally not invariant under the unrestricted density Fisher flow. This route was therefore not used to establish the general-law result.

The investigation used three bounded constructive rounds: response observability and continuous-symmetry obstructions; explicit two-stage atomless and selective-channel constructions; then the arbitrary-depth coupled profile hierarchy and its complete incoming-force and response proof. The final round produced a checkable extension, so no further mechanisms were pursued. Agreement among agents was not treated as verification. Load-bearing algebra was reconstructed from the original potential, class averages, and Fisher metric.

## Remaining formation obligation

The new theorem supplies the previously missing combination of public compression, exact original dynamics, an existing nonconstant response protocol, record conditioning, and recursive representation joins. It assumes a common base marginal, a supplied binary hierarchy, balanced public partitions, and a compatible profile preparation. It proves regular local-time inheritance and nonzero-interval distinctness witnesses, not persistent separation at arbitrarily long times.

The next decisive problem is to obtain an admissible hierarchy or its sufficient response structure from less structured preparations under the same original dynamics. Replacing the retained nested profile by a smaller statistic, allowing arbitrary external probes, or preserving same-child multi-record dependence are separate stronger targets. A future continuation should specify which of these it addresses rather than treating the present conditional hierarchy as endogenous formation.

## Primary-source context

[Hermann and Krener, “Nonlinear Controllability and Observability”](https://www.math.ucdavis.edu/~krener/1-25/10.IEEETAC77.pdf), IEEE Transactions on Automatic Control 22(5), 728–740 (1977), DOI 10.1109/TAC.1977.1101601, provides the classical context for using output derivatives to distinguish states. The author-hosted paper and its introductory formulation were consulted. The local determinant argument above is supplied explicitly and does not depend on an unquoted global realization theorem. The recursive KL constructions are derived here; this citation is not evidence for their formation claims.

## Document validation

The final main manuscript has 68 pages and the companion has 31. Both TeX Live builds completed without LaTeX warnings, unresolved references or citations, or overfull/underfull boxes. Source checks covered 37 TeX files and 347 labels, with no duplicate labels, missing citation keys, prohibited spacing commands, or trailing whitespace. All 99 pages were rendered at 110 dpi and inspected in nine contact sheets; main pages 55-61 and companion pages 25-27 were also inspected at readable size. The companion contents overflow was removed. The main chapter ends with a partial proof page; the preexisting short page 21 was unchanged. The supplement was unchanged. These are document checks, not independent mathematical verification.

Main PDF SHA-256: `9fd8d2cf1da2f4987fe94fe64feb05bf2146459208b458fd08158325abb8f921`. Companion PDF SHA-256: `51e130f8cd9762afdad48e4887873628c6852fd017afa550bd1fc803d6fb4547`.
