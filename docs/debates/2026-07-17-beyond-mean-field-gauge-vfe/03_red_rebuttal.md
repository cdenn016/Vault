# Red Rebuttal

## Concession

Blue is correct on three points. First, a fixed normalized conditional state model with a correlated posterior is the proper way to enlarge the state variational family without making the generative target depend on that posterior; this is the canonical fixed-model organization of variational inference [Blei, Kucukelbir, and McAuliffe 2017, §§2.1–2.2](https://doi.org/10.1080/01621459.2017.1285773). Second, if structural configurations are themselves declared uncertain, a proper prior \(P_0(dX)\) and the KL chain rule give a valid hierarchical ELBO. Third, a live term \(D_{\mathrm{KL}}(q_i\Vert\Omega_{ij\#}q_j)\) remains a gauge-covariant consensus discrepancy but is not thereby a fixed state-model factor. Those concessions establish that Blue's architecture is admissible under its hypotheses.

## Core attack

Blue defends a weaker claim than the one under debate. Its opening changes “the most principled extension” into “among extensions that retain ordinary state evidence semantics while also retaining PIFB2's configuration thermodynamics.” The second requirement builds the configuration tier into the comparison class. Under that antecedent, two probabilistic levels are a clean bookkeeping choice, but the argument no longer shows that the configuration Gibbs/effective-action tier is required by going beyond state mean field or that it is preferred to a correlated state model with an ordinary structural prior. The exact identity

\[
D_{\mathrm{KL}}(RQ\Vert P_0p_\theta)
=D_{\mathrm{KL}}(R\Vert P_0)
+\mathbb E_R D_{\mathrm{KL}}(Q_X\Vert p_\theta(\cdot\mid X))
\]

holds for an arbitrary proper \(P_0\). Exponentiating a selected \(\mathcal F_{\mathrm{vac}}\) proves normalization when \(0<Z_0<\infty\); it does not derive that energy, select its variables, or establish the superlative. Bissiri, Holmes, and Walker support coherent loss-exponential updating, but their result identifies a generalized-Bayesian target once a loss is chosen; it does not select the loss or convert it into state evidence [Bissiri, Holmes, and Walker 2016, Eqs. 7–8](https://doi.org/10.1111/rssb.12158).

Blue's strict no-double-counting contract also exposes an unresolved contradiction in the advertised two-level theory. Its structural configuration satisfies

\[
X_{\mathrm{struct}}\not\ni q_i,s_i,
\]

whereas the existing belief-configuration Gibbs lift uses

\[
X_{\mathrm{belief}}=(q,s,\alpha,\beta,\gamma,\phi,\ldots).
\]

The live peer KL cannot be part of \(\mathcal F_{\mathrm{vac}}(X_{\mathrm{struct}})\). Blue offers three possible placements: a projection of the state-reduced action, an algorithmic penalty around an ELBO, or a separate Gibbs ensemble over measure-valued beliefs. These are not interchangeable. The algorithmic-penalty reading is outside the generative hierarchy. The separate Gibbs reading introduces a second configuration sample space in addition to \(X_{\mathrm{struct}}\), so the result is not the asserted two-level model. The projection reading would preserve two levels, but it requires the very object Blue concedes is absent: an explicit \(\Pi:Q_X\mapsto\widehat X\), an operator projection, and a quantitative energy or force residual. Until one placement is derived, “configuration-level consensus truncation” names an option set rather than a mathematical status.

Blue's quotient argument has the same conditional form. The displayed factorization

\[
Z=\operatorname{Vol}(G)\int_{\mathfrak X/G}
e^{-\mathcal A_o([X])/T_{\mathrm{cfg}}}d\nu_{\mathrm{phys}}([X])
\]

already assumes that the orbit space and measure disintegration are well defined. Faddeev and Popov show how a determinant enters a gauge-fixed redundant-field integral [Faddeev and Popov 1967](https://doi.org/10.1016/0370-2693(67)90067-6); they do not prove that PIFB2's undeclared redundancy subgroup acts freely and properly on its mixed structural fields, nor that active and redundant frame directions can be separated globally. If a frame direction is physical, a proper confining reference law can normalize it without quotienting it. If it is redundant, PIFB2 must define the action, quotient or gauge condition, stabilizers, and measure. The shared evidence states that this modeling declaration is unsettled. Normalizability therefore constrains a declared model; it does not decide which transformations are redundancy or validate the proposed quotient before that declaration.

## Defense

Blue's statement that the levels answer distinct questions supports modular separation, not a single completed approximation ladder. Bethe or Kikuchi methods approximate state marginals and entropy; on loopy graphs their locally consistent beliefs need not be globally realizable, and ordinary Bethe does not inherit the bound supplied by tree-reweighted constructions [Wainwright and Jordan 2008, §4.1 and Theorem 7.2](https://doi.org/10.1561/2200000001). The CJT construction is a double Legendre transform of one generating functional in its mean and two-point sources [Cornwall, Jackiw, and Tomboulis 1974](https://doi.org/10.1103/PhysRevD.10.2428). Wilsonian RG integrates eliminated modes and generally expands the operator basis [Wilson and Kogut 1974](https://doi.org/10.1016/0370-1573(74)90023-4). These sources validate three operations under separate hypotheses. They do not supply the missing maps between PIFB2's state posterior, structural configuration action, belief-configuration energy, 2PI sources, and RG projection. Gauge-theory 2PI truncations add another obligation because finite truncations have controlled but nonzero gauge-fixing dependence [Arrizabalaga and Smit 2002](https://doi.org/10.1103/PhysRevD.66.065014).

The red objection is falsifiable. It fails if Blue supplies one declared redundancy action and finite measure on \(X_{\mathrm{struct}}\), proves the needed quotient or gauge-fixed construction, derives a single map from correlated \(Q_X\) to generative belief-summary fields, shows that peer KL is the projected operator with a nontrivial residual bound, and demonstrates that the same configuration measure underlies the 1PI/2PI and RG steps without double counting. It also fails if an independent decision criterion shows that a simpler correlated state model with a proper hierarchical prior cannot retain the stipulated evidence, fluctuation, and gauge-volume properties.

Without those results, the source-backed conclusion is narrower: the correlated fixed-joint tier is a principled state-level extension; a gauge-reduced configuration Gibbs and effective-action tier is a conditional research program for a distinct question; and live peer KL is presently an engineered consensus potential, a separate generalized-Bayesian belief-configuration energy, or an unvalidated projection ansatz. Blue has defended that narrowed program, not the original ranking and truncation claim.
