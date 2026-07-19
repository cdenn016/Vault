# Claim — finite and continuum moving-peer obstruction

At Research commit `33059bb`, under the hypotheses stated in `manuscripts/magent_elbo_whitepaper/09_pifb2_crosswalk.tex` and proved in `13_appendices.tex`, the sum of separate site-local iterated derivatives excludes equality, up to a constant on the stated open neighborhood, between the finite moving-peer functional and the negative ELBO of any fixed posterior-independent joint evaluated on the fine design-point-factorized mean-field family

\[
Q=\bigotimes_{\ell,b}q_{\ell,b}.
\]

The conditional continuum corollary proves only a deterministic base-integral incompatibility along one exact admissible centered path. It does not construct a probability measure on section space, extend finite marginals uniquely, or establish a finite-to-continuum limit.

The debate began against commit `9833a44`. Red and the independent manuscript reviewer found two scope defects: the finite comparison family was not distinguished clearly enough from the coarser cross-design families in Chapter 6, and the continuum corollary assumed admissibility before defining the centered tangent it used. Commit `33059bb` is the amended source submitted for the final red and blue positions and for adjudication.
