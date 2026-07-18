# Red Opening

## Steelman

The strongest version of the claim is that PIFB2 should preserve an ordinary normalized evidence model for latent states, enlarge its variational family to carry inter-agent correlations, and place slower structural uncertainty in a separately normalized gauge-reduced ensemble whose effective actions and RG images describe collective fluctuations without misidentifying the live posterior-to-posterior KL penalty as the state-model ELBO.

## Position

The fixed-joint and correlated-posterior tier is well motivated, and the conclusion that the live peer KL is not the state-level ELBO is correct. The claim fails at its load-bearing superlative: the nested KL identity neither requires nor selects a Gibbs/effective-action tier. It is the chain rule for one ordinary hierarchical joint with an arbitrary proper prior on \(X\). The proposed completion then joins three operations on two different sample spaces—state-posterior region approximation, configuration 1PI/2PI construction, and configuration RG—without deriving the maps that make them one approximation hierarchy. The gauge quotient and its measure remain conditional objects rather than a defined global configuration theory. The live peer KL consequently has a precise status as an engineered consensus energy or a generalized-Bayes potential over belief fields, but not yet as a controlled truncation of the state-reduced structural action.

## Evidence

### The nested theorem proves admissibility, not necessity or principled selection

For any proper \(P_0(dX)\) and normalized \(p_\theta(dY,o\mid X)\), set

\[
P_\theta(dX,dY,o)=P_0(dX)p_\theta(dY,o\mid X),
\qquad
\mathcal Q(dX,dY)=R(dX)Q_X(dY).
\]

The KL chain rule gives

\[
-\operatorname{ELBO}(\mathcal Q)
=D_{\mathrm{KL}}(R\Vert P_0)
+\mathbb E_R\mathcal F_{\mathrm{state}}[Q_X;X,o].
\]

This is the entire content of the nested identity up to multiplication by \(T_{\mathrm{cfg}}\). It holds for every proper \(P_0\); it contains no criterion that prefers a Gibbs prior, a gauge quotient, or an effective action. A direct counterexample to necessity is \(P_0=\delta_{X_0}\) and \(R=\delta_{X_0}\): the model retains a normalized fixed state joint and an arbitrarily correlated \(Q_{X_0}\), while the configuration KL, configuration fluctuations, quotient, and effective action disappear. If uncertainty in \(X\) is desired, ordinary hierarchical Bayes already supplies it through a chosen proper \(P_0\). This is the standard fixed-model variational construction, in which the model and log partition are defined before selecting an exact or approximate inference family [Wainwright and Jordan 2008, §§3–5, DOI 10.1561/2200000001](https://doi.org/10.1561/2200000001).

Writing \(P_0\) in Gibbs form does not add a selection theorem. Whenever \(P_0\ll\nu_0\), one may define

\[
\mathcal F_{\mathrm{vac}}(X)
=-T_{\mathrm{cfg}}\log\frac{dP_0}{d\nu_0}(X)+c,
\]

which reproduces \(P_0\) after normalization. This is a representation of a selected prior, not evidence that the represented prior is the best extension of PIFB2. A loss-exponential law can be a coherent generalized-Bayesian update, but that construction is explicitly a loss-based target rather than an approximation to a conventional likelihood model [Bissiri, Holmes, and Walker 2016, DOI 10.1111/rssb.12158](https://doi.org/10.1111/rssb.12158). The claim must therefore supply an independent modeling or predictive argument for the nondegenerate configuration ensemble; the fixed-joint theorem cannot supply it.

### The proposed quotient effective action is local and conditional

The construction at manuscripts/PIFB2.tex:3510 begins with a physical quotient \(\mathfrak X_{\mathrm{phys}}\), a quotient measure \(d\nu_{\mathrm{phys}}\), normal coordinates, and a nondegenerate positive Hessian. None of these follows from scalar gauge invariance. For a noncompact group action, the slice and quotient-manifold machinery requires hypotheses such as properness; Palais proves slices for proper noncompact actions rather than for arbitrary actions [Palais 1961, DOI 10.2307/1970335](https://doi.org/10.2307/1970335). The manuscript does not define the redundancy subgroup on the complete \(X\), prove that its action is free or proper, treat stabilizer strata, or construct a finite measure for the remaining noncompact active directions. Without those results, \(J_A\xi^A\), \(\operatorname{Exp}_{\bar X}\xi\), the Hessian determinant, and the Legendre transform are chart-level formulas, not a global gauge-covariant effective action.

Gauge fixing does not repair this by notation alone. Faddeev and Popov derive the determinant required when redundant gauge orbits are integrated in a field representation [Faddeev and Popov 1967, DOI 10.1016/0370-2693(67)90067-6](https://doi.org/10.1016/0370-2693(67)90067-6), while Singer proves that a continuous global gauge choice can fail even when local gauges exist [Singer 1978, DOI 10.1007/BF01609471](https://doi.org/10.1007/BF01609471). Singer's theorem concerns a different gauge-field setting, so it is not a no-go theorem for this finite model; it establishes why a global slice cannot be assumed. PIFB2 must prove the corresponding quotient conditions for its own configuration action and show chart compatibility of \(W\) and \(\Gamma\).

### Bethe, 2PI, and RG are not yet one controlled ladder

The Bethe construction approximates state inference through locally consistent node and edge pseudomarginals. On loopy graphs those pseudomarginals can fail to arise from any global distribution; Wainwright and Jordan exhibit this failure and distinguish ordinary Bethe from tree-reweighted constructions that furnish a convex upper bound [Wainwright and Jordan 2008, §4.1 and Theorem 7.2](https://doi.org/10.1561/2200000001). Yedidia, Freeman, and Weiss identify generalized-belief-propagation fixed points with stationary points of chosen region free energies, not with a monotone sequence of state ELBOs [Yedidia, Freeman, and Weiss 2005, DOI 10.1109/TIT.2005.850085](https://doi.org/10.1109/TIT.2005.850085).

The CJT 2PI action is a different operation: a double Legendre transform with respect to linear and bilocal sources, producing a functional of a mean field and a full two-point function [Cornwall, Jackiw, and Tomboulis 1974, DOI 10.1103/PhysRevD.10.2428](https://doi.org/10.1103/PhysRevD.10.2428). In a gauge theory, finite 2PI truncations acquire gauge-fixing dependence unless an order-controlled construction and the relevant identities are supplied [Arrizabalaga and Smit 2002, DOI 10.1103/PhysRevD.66.065014](https://doi.org/10.1103/PhysRevD.66.065014). Wilsonian RG is different again: integrating eliminated modes generally generates a larger operator basis, so closure in the five-term family is a tested projection hypothesis rather than a consequence of symmetry [Wilson and Kogut 1974, DOI 10.1016/0370-1573(74)90023-4](https://doi.org/10.1016/0370-1573(74)90023-4).

PIFB2 correctly distinguishes the state covariance \(C_{ij}\) from the configuration covariance \(G^{AB}\) and labels the gauge-consistent 2PI step as future work. Those disclaimers defeat the stronger architectural claim. No equation currently maps a Bethe or sparse-Gaussian state approximation into the same configuration action used by the 2PI transform and then into the exact RG pushforward with a commuting approximation diagram or an error bound. The canon validates each tool under its own hypotheses; it does not validate their juxtaposition as one completed theory.

### “Configuration-level consensus truncation” conflates two placements

There are two distinct configuration constructions. In the nested state model, \(X\) explicitly excludes live \(q_i\) and \(s_i\), so \(D_{\mathrm{KL}}(q_i\Vert\Omega_{ij}q_j)\) cannot be a term in \(P_0(dX)\) without promoting new measure-valued generative fields and specifying their relation to \(Q_X\). In the pre-existing belief-configuration Gibbs lift, the live beliefs themselves are coordinates of the random configuration, and the peer KL can be used exactly as a loss-based energy when its partition function is finite. That exact Gibbs representation is not a truncation of the state-level ELBO. The alternative claim—that peer KL approximates the state-reduced action after mapping \(Q_X\) to belief summaries—would be a truncation, but no summary map, fitted operator projection, norm, or residual bound has been derived. The defensible current label is therefore “engineered consensus potential; exact only in the separate generalized-Bayes belief-configuration ensemble, and a candidate ansatz for a state-reduced action.” Calling it a configuration truncation before the projection error is defined claims the result that the RG program is meant to test.

## Falsification conditions

The first objection fails if a theorem or decision criterion is supplied that distinguishes the proposed nondegenerate Gibbs prior from arbitrary proper \(P_0\), proves that the state-only countermodel or an ordinary hierarchical prior cannot meet the declared scientific requirements, and derives the selected \(\mathcal F_{\mathrm{vac}}\) rather than defining it from \(P_0\).

The quotient objection fails if the redundancy group and its action on every component of \(X\) are given, the relevant quotient is proved smooth or treated as an explicit stratified space, a proper finite reference measure yields \(0<Z<\infty\), and the effective action or its observables are shown to agree across overlapping charts and admissible gauge choices.

The approximation-stack objection fails if one normalized joint and one configuration measure generate a documented chain from correlated state inference to \(\mathcal A_o\), 1PI/2PI sources, and RG pushforward, with the state and configuration covariances kept distinct, a gauge-consistent 2PI truncation satisfying the required identities, and quantitative errors at each projection.

The peer-KL objection fails if PIFB2 defines the promoted belief fields or the map \(Q_X\mapsto(\widehat q_i,\widehat s_i)\), derives the peer-KL operator in the projected action, and reports a nontrivial energy and force residual against the exact state-reduced or RG-pushed action. If it is retained only as a generalized-Bayes belief-configuration energy, the objection also fails by replacing “truncation” with that exact, narrower status.
