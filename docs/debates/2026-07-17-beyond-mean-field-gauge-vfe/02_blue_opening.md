# Blue Opening: Beyond-Mean-Field Gauge VFE

## Steelman

The claim is not that every term in the live PIFB2 functional can be renamed an ELBO, nor that a two-level construction is uniquely forced by probability theory. Its strongest defensible form is conditional: among extensions that retain ordinary evidence semantics for latent-state inference while also retaining PIFB2's configuration thermodynamics, the clean architecture separates two random-variable levels. At the state level, a posterior-independent normalized conditional model \(p_\theta(dY,o\mid X)\) is approximated by a correlated posterior \(Q_X(dY)\). At the configuration level, slow structural fields \(X\) are assigned a proper Gibbs law on the physical, gauge-quotiented configuration space, and their connected fluctuations are organized by an effective action. The live belief-to-belief peer functional remains a useful projected consensus energy or a separate generalized-Bayesian configuration ensemble; it is not inserted into the fixed state joint and is not counted twice.

This formulation grants the draft's stated limitations. It does not establish uniqueness of the state factors, normalizability before a reference measure or regulator is specified, a generic evidence bound for loopy Bethe or Kikuchi pseudomarginals, convergence of a loop expansion, or an already completed gauge-consistent 2PI theory. Those are conditions and research tasks, not consequences of the five-term functional.

## Position

The claim is defensible in this qualified form. The two levels answer different questions. The state ELBO asks how well a correlated law over latent states \(Y\) approximates the posterior of one fixed observation model at fixed \(X\). The configuration Gibbs law asks how whole structural configurations \(X\) fluctuate and coarse-grain after state uncertainty has been integrated or variationally reduced. Conflating them would either erase state correlations or promote live variational posteriors into the generative law that they are supposed to approximate.

The strongest attack is circularity and double counting: if \(X\) contains the same live \(q_i,s_i\) that define \(Q_X\), or if a physical edge appears both as a fixed state transition and as \(D_{\mathrm{KL}}(q_i\|\Omega_{ij\#}q_j)\), the nested-ELBO identity loses its fixed-prior interpretation and the interaction is counted twice. The defense therefore stands only with a strict contract: structural \(X\) excludes the variational posterior; the observation likelihood enters once; every physical interaction is placed either in the normalized state joint or in a declared configuration approximation; and any map from \(Q_X\) to live belief summaries is explicit.

## Evidence

### A fixed normalized joint is required for state evidence, while correlation belongs to the posterior family

For normalized \(p_\theta(dY,o\mid X)=p_\theta(dY\mid X)p_\theta(o\mid Y,X)\), independent of \(Q_X\), define

\[
\mathcal F_{\mathrm{state}}[Q_X;X,o]
=D_{\mathrm{KL}}\bigl(Q_X\|p_\theta(\cdot\mid X)\bigr)
-\mathbb E_{Q_X}\log p_\theta(o\mid Y,X).
\]

Bayes' rule gives the exact identity

\[
\mathcal F_{\mathrm{state}}
=-\log p_\theta(o\mid X)
+D_{\mathrm{KL}}\bigl(Q_X\|p_\theta(\cdot\mid o,X)\bigr).
\]

Normalization and posterior-independence are what make (p_\theta(o\mid X)) and its posterior well-defined. If a putative factor in (p_\theta) contains a live (q_j), varying (Q_X) also varies the target, so this evidence decomposition no longer follows. This is the canonical organization of variational inference: a fixed model and a separately chosen approximation family [Blei, Kucukelbir, and McAuliffe 2017, Sections 2.1-2.2](https://doi.org/10.1080/01621459.2017.1285773).

Moving beyond mean field changes (Q_X), not (p_\theta). If (q_i) are the marginals of a joint (Q_X) and the reference prior factorizes, then

\[
D_{\mathrm{KL}}\left(Q_X\middle\|\prod_i p_i\right)
=\sum_iD_{\mathrm{KL}}(q_i\|p_i)
+D_{\mathrm{KL}}\left(Q_X\middle\|\prod_iq_i\right).
\]

The last term is total correlation. A node-marginal inventory omits it, whereas a globally normalized sparse block Gaussian, a tree-structured posterior, or another proper correlated family carries it through the joint entropy. Wainwright and Jordan derive the exact marginal-polytope variational principle and distinguish exact tree inference, mean field, and approximate region relaxations [Wainwright and Jordan 2008](https://doi.org/10.1561/2200000001). Yedidia, Freeman, and Weiss establish exactness for acyclic region constructions and stationary-point, rather than generic bound, semantics for loopy region free energies [Yedidia, Freeman, and Weiss 2005](https://doi.org/10.1109/TIT.2005.850085). This supports the draft's limitation: a loopy Bethe or Kikuchi objective is not automatically an ELBO.

### The configuration Gibbs law and effective action are a distinct valid level

Let the structural configuration prior be

\[
P_0(dX)=Z_0^{-1}e^{-\mathcal F_{\mathrm{vac}}(X)/T_{\mathrm{cfg}}}\nu_0(dX),
\qquad
0<Z_0<\infty.
\]

For every (R\ll\nu_0) with finite terms, direct KL algebra gives

\[
T_{\mathrm{cfg}}D_{\mathrm{KL}}(R\|P_0)
=\mathbb E_R\mathcal F_{\mathrm{vac}}
+T_{\mathrm{cfg}}D_{\mathrm{KL}}(R\|\nu_0)
+T_{\mathrm{cfg}}\log Z_0.
\]

This is an exact configuration variational principle. Bissiri, Holmes, and Walker derive the same exponentiated-negative-loss form as the coherent minimizer of expected loss plus KL distance from a prior [Bissiri, Holmes, and Walker 2016, Equations 7-8](https://doi.org/10.1111/rssb.12158). It is legitimate without being a state ELBO because its random variable is (X), not (Y).

Nesting the two levels preserves evidence semantics. For the joint variational law (R(dX)Q_X(dY)), the KL chain rule yields

\[
T_{\mathrm{cfg}}D_{\mathrm{KL}}(R\|P_0)
+T_{\mathrm{cfg}}\mathbb E_R\mathcal F_{\mathrm{state}}
=-T_{\mathrm{cfg}}\log p_\theta(o)
+T_{\mathrm{cfg}}D_{\mathrm{KL}}\bigl(RQ\|P_\theta(X,Y\mid o)\bigr).
\]

After reducing the state level, one may define (\mathcal A_o[X]=\mathcal F_{\mathrm{vac}}[X]+T_{\mathrm{cfg}}\inf_Q\mathcal F_{\mathrm{state}}[Q;X,o]), then

\[
W[J]=T_{\mathrm{cfg}}\log\int e^{-(\mathcal A_o[X]-J_A\xi^A)/T_{\mathrm{cfg}}}d\nu_{\mathrm{phys}},
\qquad
\Gamma[\varphi]=J_A\varphi^A-W[J].
\]

It follows that \(\varphi^A=\delta W/\delta J_A\) and
\(\operatorname{Cov}(\xi)=T_{\mathrm{cfg}}(\Gamma^{(2)})^{-1}\) on physical nonzero modes. A future double Legendre transform in the mean and two-point function has the canonical 2PI precedent of [Cornwall, Jackiw, and Tomboulis 1974](https://doi.org/10.1103/PhysRevD.10.2428). This validates the level, not a completed PIFB2 2PI truncation. Wilsonian elimination also generates all symmetry-allowed operators, so closure in the live five-term ansatz must be measured rather than presumed [Wilson and Kogut 1974](https://doi.org/10.1016/0370-1573(74)90023-4).

### Gauge redundancy requires a quotient or gauge fixing

If a group (G) acts redundantly and (\mathcal A_o[g\cdot X]=\mathcal A_o[X]), a factorized orbit measure gives

\[
Z=\operatorname{Vol}(G)\int_{\mathfrak X/G}e^{-\mathcal A_o([X])/T_{\mathrm{cfg}}}d\nu_{\mathrm{phys}}([X]).
\]

For noncompact (G=\mathrm{GL}^+(K)), invariant Haar orbit volume is infinite. Integrating those copies is not a physical fluctuation calculation. One must integrate directly on the quotient or impose one gauge condition and its Jacobian; the latter is the Faddeev-Popov construction [Faddeev and Popov 1967](https://doi.org/10.1016/0370-2693(67)90067-6). The quotient and gauge-fixed prescriptions are alternatives, not factors to multiply. Only transformations declared redundant are divided out. Active epistemic frame directions remain in (X) and instead require a proper confining reference law. Thus the quotient is forced by the modeling declaration plus normalizability, not by the word "gauge" alone.

### The live peer KL remains useful as consensus without becoming the state ELBO

Under (q_i\mapsto(G_i)_\#q_i) and (\Omega_{ij}\mapsto G_i\Omega_{ij}G_j^{-1}), invariance of KL under a common bijective pushforward gives

\[
D_{\mathrm{KL}}\bigl((G_i)_\#q_i\|(G_i)_\#(\Omega_{ij\#}q_j)\bigr)
=D_{\mathrm{KL}}(q_i\|\Omega_{ij\#}q_j).
\]

The live term is therefore a well-defined gauge-covariant discrepancy that can drive routing, alignment, and distributed consensus. Its target nevertheless moves with (q_j). Its honest placements are as a projected truncation of the state-reduced configuration action after an explicit summary map (\widehat X=\Pi(Q_X)), as an algorithmic consensus penalty around an underlying ELBO, or as a separate generalized-Bayesian Gibbs energy on measure-valued belief configurations. None of these placements makes it the fixed state-level likelihood or prior. Preserving this term is a strength only if its approximation error, force residual, and held-out consequences are measured and the corresponding state edge is not counted again.

## Falsification conditions

This defense is not defensible if no posterior-independent normalized gauge-covariant conditional (p_\theta(dY,o\mid X)) with a proper observation likelihood can be specified, or if the proposed correlated family lacks a globally normalized joint law or a valid bound-preserving replacement.

It is not defensible if every quotient, gauge condition, regulator, or proper reference measure leaves (Z_0) divergent, or if the claimed physical configuration space cannot be separated from active frame degrees of freedom without changing the model's observables.

It is not defensible if an explicit fixed joint on the original state variables reproduces the live peer-KL functional over an open family of simultaneously varying (q_i) and (q_j) without posterior-dependent generative factors. Such a construction would defeat the stated reason for assigning peer KL to the configuration level.

It is not defensible if the implementation or theory counts one observation, entropy, or physical edge at both levels; if a loopy region objective is labeled an ELBO without a bound proof; or if a 2PI or RG closure is claimed without the corresponding source construction and quantitative residual. Finally, the ranking "most principled" is falsified by a simpler competing hierarchy that preserves the same evidence semantics, gauge-volume control, correlation content, and no-double-counting guarantees while making fewer unsupported assumptions.
