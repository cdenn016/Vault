# Verdict — finite and continuum moving-peer obstruction

## Binding verdict

`CLAIM_TRUE` at Research commit `33059bb`.

## Decisive evidence

On the expressly stated fine product family

\[
Q=\bigotimes_{\ell,b}q_{\ell,b},
\]

the negative ELBO of one fixed posterior-independent joint has factor-separable entropy and an energy expectation that is affine in each selected factor while the others are held fixed. Every site-local path therefore has zero receiver-once, sender-twice iterated derivative. This is the standard fixed-joint mean-field form described by Wainwright and Jordan (2008, DOI `10.1561/2200000001`) and Blei, Kucukelbir, and McAuliffe (2017, arXiv `1601.00670`).

The moving-peer term has the pathwise derivative

\[
\left.\partial_s\partial_t^2
\operatorname{KL}(q_i+s a_i\Vert r+t u)\right|_{(0,0)}
=\int a_i\left(\frac{u}{r}\right)^2d\nu_i.
\]

The centered receiver tangent converts the finite sum of separate site-local derivatives into

\[
\lambda\sum_a w_a\operatorname{Var}_{q_{i,a}}(G_{ij,a})>0.
\]

Equality of functionals on the stated neighborhood would imply equality along every site-local path. Summing those separate derivative equalities would give zero, contradicting the positive variance sum. The rejected simultaneous-site proof is unnecessary.

An exact symbolic reconstruction returned zero for the fixed-joint site-local derivative and `27/3200` for the two-state peer witness. It also reproduced the nonzero simultaneous-site counterexample, confirming that the amendment changed the relevant path rather than hiding the objection. The focused regression suite passed with `17 passed` during adjudication.

## Continuum scope

The continuum corollary defines its centered tangent before assuming joint measurability, zero fiber mass, one common admissible rectangle, finite nearby KLs, bounded transported ratios, a common differentiation envelope, zero remainder derivative, and positive integrated variance for that exact path. It proves only a conditional derivative property of a deterministic base integral. It does not construct a section-space probability law, supply a unique extension of finite marginals, or prove a continuum limit.

## Exclusions

The verdict does not cover the coarser cross-design recognition families in Chapter 6, restricted parametric families lacking the required tangents, the envelope obtained after substituting state-dependent optimal attention rows, auxiliary-variable lifts, a probability law on continuum sections, or any finite-to-continuum convergence claim.

## Required manuscript action

Accept the amended theorem and continuum corollary without further mathematical correction. Preserve the current scope fences. The preregistered `27/3200` finite-difference regression remains future verification work, as the manuscript states; that is a coverage obligation rather than a proof defect.
