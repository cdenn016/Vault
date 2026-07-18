# Blue Rebuttal

## Concession

Red is correct on four points. First, the KL chain rule does not select a Gibbs prior. It holds for every proper \(P_0(dX)\), including the degenerate choice \(\delta_{X_0}\), so the nested theorem proves admissibility of the hierarchy rather than necessity of configuration thermodynamics. Second, the present quotient effective action is local and conditional: a redundancy subgroup, a free or proper action or an explicit stratified substitute, a proper physical measure, and chart compatibility have not been proved. Palais's slice hypotheses and Singer's obstruction to a global gauge choice show why those conditions cannot be supplied by notation alone [Palais 1961](https://doi.org/10.2307/1970335), [Singer 1978](https://doi.org/10.1007/BF01609471). Third, Bethe inference, configuration 2PI resummation, and Wilsonian RG are different operations; the current draft does not provide a commuting approximation diagram or error bounds between them. Fourth, “consensus truncation” is too strong if it means an already controlled approximation to the exact state-reduced action. The present exact status of live peer KL is an engineered consensus energy and, when its partition function exists, a generalized-Bayesian energy on belief configurations. Its status in the structural effective action is a candidate operator truncation.

These concessions reject a completed-theory reading. They do not reject the two-level architecture or the placement of live peer KL outside the state ELBO.

## Core attack

Red's central argument substitutes logical necessity for principled model selection. The claim is not that the nested identity forces a Gibbs prior. It is that, given the declared goals of retaining ordinary state evidence, correlated posterior uncertainty, positive-temperature fluctuations of whole configurations, gauge-volume control, effective-action correlators, and RG-generated operators without double counting, the two-level construction is the least committal architecture that accommodates all of them.

The countermodel \(P_0=\delta_{X_0}\) preserves state evidence and correlated inference, but it removes the phenomena the requested extension is meant to represent: configuration entropy, susceptibility, connected configuration correlators, loop corrections, and scale-dependent structural fluctuations. It is therefore a valid state-only model and not a counterexample to the conditional ranking. An arbitrary hierarchical prior has the same limitation unless its configuration law, reference measure, temperature, and observables are supplied. Conversely, the fact that any dominated \(P_0\) can be written as

\[
\mathcal F_{\mathrm{vac}}(X)
=-T_{\mathrm{cfg}}\log\frac{dP_0}{d\nu_0}(X)+c
\]

does not make all choices scientifically equivalent. The modeling direction matters: one specifies a gauge-invariant or gauge-reduced structural energy and a proper reference law, checks \(0<Z_0<\infty\), and obtains a configuration distribution. Bissiri, Holmes, and Walker establish that expected loss plus KL distance from a prior selects the exponentiated-loss law coherently [Bissiri, Holmes, and Walker 2016, Equations 7–8](https://doi.org/10.1111/rssb.12158). That result does not convert the configuration law into state evidence; it supports the separate generalized-Bayesian level that the claim asserts.

Red also asks for one commuting map across Bethe, 2PI, and RG. Commutation is not required to define a layered theory. What is required is an ordered construction and separate error accounting. The canonical order is: fix the normalized state joint; choose a genuine correlated posterior family; reduce the state free energy at each \(X\); define the proper gauge-reduced configuration ensemble; construct its connected and 1PI functionals; apply the exact RG pushforward; then project to a finite operator basis. Wainwright and Jordan support the first variational reduction [Wainwright and Jordan 2008](https://doi.org/10.1561/2200000001); Cornwall, Jackiw, and Tomboulis support the distinct double-Legendre two-point construction [Cornwall, Jackiw, and Tomboulis 1974](https://doi.org/10.1103/PhysRevD.10.2428); Wilson and Kogut show why RG projection need not close in the original ansatz [Wilson and Kogut 1974](https://doi.org/10.1016/0370-1573(74)90023-4). Their noncommutation is a source of approximation error to measure, not a proof that the levels cannot be composed.

## Defense

The missing state-to-configuration map can be written exactly for every globally normalized correlated family. Let

\[
\mathcal F_{\mathrm{state}}^{*}(X)
=-\log p_\theta(o\mid X)
\]

be the unrestricted optimum and let \(\mathcal Q_{\mathrm{corr}}\) be a proper correlated family. Define its inference gap

\[
\epsilon_{\mathcal Q}(X)
:=\inf_{Q\in\mathcal Q_{\mathrm{corr}}}
D_{\mathrm{KL}}\bigl(Q\|p_\theta(\cdot\mid o,X)\bigr)\geq0.
\]

The state-reduced action then satisfies the exact pointwise relation

\[
\mathcal A_o^{\mathcal Q}(X)
=\mathcal F_{\mathrm{vac}}(X)
+T_{\mathrm{cfg}}\inf_{Q\in\mathcal Q_{\mathrm{corr}}}
\mathcal F_{\mathrm{state}}[Q;X,o]
=\mathcal A_o^{*}(X)+T_{\mathrm{cfg}}\epsilon_{\mathcal Q}(X).
\]

This equation supplies the map Red says is absent for normalized sparse-Gaussian or other genuine joint families. It also states the error quantity. If \(0\leq\epsilon_{\mathcal Q}(X)\leq\delta\) uniformly, then the corresponding configuration partition functions obey

\[
e^{-\delta}Z_{*}\leq Z_{\mathcal Q}\leq Z_{*},
\]

and their configuration free energies differ by at most \(T_{\mathrm{cfg}}\delta\). If no such bound or empirical estimate exists, the reduction is variationally defined but not quantitatively controlled. Generic loopy Bethe pseudomarginals do not enter this identity because they need not define any global \(Q\); Yedidia, Freeman, and Weiss support only stationary region-free-energy semantics on loopy graphs [Yedidia, Freeman, and Weiss 2005](https://doi.org/10.1109/TIT.2005.850085). This is why the architecture keeps normalized correlated families and loopy region approximations in different evidential categories.

The quotient objection likewise fixes the scope rather than defeating the level. A global smooth quotient is not yet established, so the current effective action is a local background-chart object. That local object is still legitimate when a slice exists and its measure and overlap transformations are specified. A global gauge section is unnecessary if physical observables are defined on a quotient atlas or stratified orbit space and agree on overlaps. Redundant integration instead requires one gauge condition and its determinant, as Faddeev and Popov derive [Faddeev and Popov 1967](https://doi.org/10.1016/0370-2693(67)90067-6). Active epistemic frame transformations must not be removed; they remain physical coordinates with a confining reference law. The defense therefore claims a conditional local effective theory now and a global theory only after the quotient hypotheses are proved.

Live peer KL has a similarly precise boundary. Its posterior-dependent target prevents it from serving as a fixed factor in \(p_\theta(dY,o\mid X)\). It can nevertheless be exact as a generalized-Bayesian energy when the random variable is a whole belief configuration, or it can be proposed in a finite configuration operator basis after a summary map \(\widehat X=\Pi(Q_X)\). In the second placement the honest label is “candidate consensus truncation,” and its coefficients and adequacy must be tested against the exact or variationally reduced action using both energy and force residuals. Red wins the adjective “controlled” until those tests exist; Red does not overturn the configuration-level placement or the conclusion that peer KL is not the state ELBO.

The defense is falsified if the scientific requirements can be met by a simpler state-only or ordinary hierarchical model without a configuration ensemble; if no proper quotient, gauge-fixed measure, regulator, or confining reference law makes the configuration partition finite; if the pointwise reduction above cannot be defined for the selected correlated family; if a fixed posterior-independent state joint reproduces live peer KL on an open family of simultaneously varying beliefs; or if no summary map and no nontrivial residual test supports peer KL as a configuration operator. It is also falsified if the manuscript presents the local 1PI, future 2PI, and RG projections as one controlled ladder before their separate errors and gauge identities are established.
