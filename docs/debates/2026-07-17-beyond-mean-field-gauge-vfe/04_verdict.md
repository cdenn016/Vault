# Verdict — beyond-mean-field gauge VFE

## Verdict

`RED_WINS`. The claim is rejected as written. The normalized correlated-state tier is principled, and the configuration effective-action and RG tiers form a coherent conditional research program, but the evidence does not justify the unconditional ranking “most principled” or the present-tense classification of live peer KL as an established configuration truncation.

## Decisive evidence

The decisive equation is the KL chain rule used in Eq. `\eqref{eq:nested_state_configuration_identity}`:

\[
D_{\mathrm{KL}}(R(dX)Q_X(dY)\Vert P_0(dX)p_\theta(dY\mid X,o))
=D_{\mathrm{KL}}(R\Vert P_0)
+\mathbb E_R D_{\mathrm{KL}}(Q_X\Vert p_\theta(\cdot\mid X,o)).
\]

It holds for every proper configuration prior \(P_0\), including the degenerate choice \(P_0=\delta_{X_0}\). The identity therefore validates hierarchical nesting but cannot select a nondegenerate Gibbs prior, an effective action, or the claimed superlative. This is the standard fixed-model variational organization described by Wainwright and Jordan (2008, DOI `10.1561/2200000001`). Bissiri, Holmes, and Walker (2016, DOI `10.1111/rssb.12158`) support exponentiated-loss generalized Bayesian laws after a loss has been chosen; they do not select that loss or turn it into a state-level likelihood.

## Reasoning

“Most principled” is justified only after conditioning the comparison class on the scientific aims of retaining ordinary fixed-joint evidence semantics while also modeling positive-temperature fluctuations of whole configurations, configuration correlators, loop corrections, and Wilsonian coarse-graining. Beyond-mean-field state inference alone requires none of those objects: a fixed normalized state model with a globally normalized correlated posterior already suffices. A nondegenerate configuration Gibbs tier is therefore optional for correlated state inference and required only relative to the additional configuration-thermodynamic goals. Under those declared goals, the two-level separation is a coherent architecture because it prevents posterior-dependent live beliefs from entering the state generative target and prevents double counting.

The local quotient construction is sufficiently qualified for its stated local role. The section divides out only transformations declared redundant, retains active epistemic frame directions, restricts the effective action to a background quotient chart, states that chart compatibility has not been supplied, excludes raw noncompact Haar integration, and distinguishes direct quotient integration from gauge fixing. It must not be described as a global gauge-invariant effective action until the redundancy group and its action, stabilizers or strata, a proper physical measure, and overlap compatibility are established. The slice result of Palais (1961, DOI `10.2307/1970335`) supports this boundary: properness supplies slices for noncompact actions; scalar invariance alone does not.

State Bethe or sparse-Gaussian inference, configuration 1PI/2PI constructions, and RG form a coherent ordered program, not a controlled approximation ladder. Tree Bethe inference is exact, loopy Bethe and region objectives have stationary-point semantics without a generic evidence bound, and globally normalized sparse-Gaussian families retain ordinary variational-gap semantics. The state-reduced action can then feed a configuration generating functional; a CJT-style double Legendre transform supplies the proposed 2PI form; and exact RG pushforward can be followed by a measured operator projection. The absent uniform inference-gap bounds, gauge identities for finite 2PI truncations, and RG energy/force residuals prevent claims of convergence, monotone improvement, or quantitative control. They do not make the ordering incoherent.

The live peer-KL functional has four distinct current statuses. It is not the state-level ELBO of one fixed posterior-independent joint on the original state latents. In the live five-term functional it is an engineered gauge-covariant consensus energy. It is exactly an exponentiated-loss generalized-Bayesian energy only in the separate belief-configuration ensemble, conditional on a proper reference measure and finite partition function. In the structural state-reduced effective theory it is only a candidate operator ansatz: calling it a configuration truncation requires an explicit summary map \(\Pi:Q_X\mapsto\widehat X\), fitted coefficients, and nontrivial energy and force residuals. Blue concedes this boundary, so its defense does not preserve the original present-tense truncation claim.

## Required manuscript action

Revise the closing characterization in `sec:beyond_mean_field_gauge_vfe` so it does not make an unconditional ranking. Replace “The resulting hierarchy is the principled gauge-VFE completion proposed here” with language equivalent to: “Conditional on retaining fixed-joint state evidence semantics while adding configuration thermodynamics, connected configuration fluctuations, effective-action corrections, and RG coarse-graining, the resulting hierarchy is a principled proposed completion.” Add immediately that the nondegenerate Gibbs/effective-action tier is not required merely to move beyond a mean-field state posterior.

Replace every unqualified present-tense description of live peer KL as a “configuration-level consensus truncation” with this exact status: “The live peer-KL term is an engineered gauge-covariant consensus energy and, when its belief-configuration partition function is finite, an exact generalized-Bayesian energy on that separate sample space; within the structural state-reduced action it is only a candidate consensus-operator truncation pending an explicit summary map and quantitative energy and force residuals.” Retain the existing local-quotient qualifications and the ordered Bethe/sparse-Gaussian → state reduction → 1PI/future 2PI → exact RG pushforward → tested projection program, but label it a research program rather than a controlled approximation ladder until the stated bounds and residuals exist.
