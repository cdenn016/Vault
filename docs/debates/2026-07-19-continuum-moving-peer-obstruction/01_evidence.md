# Evidence packet — finite and continuum moving-peer obstruction

## Source under review

- Initial Task 3 theorem commit: `9833a44`.
- Amended debate-closure commit: `33059bb`.
- Finite theorem and continuum corollary: `manuscripts/magent_elbo_whitepaper/09_pifb2_crosswalk.tex`, section “The scoped moving-peer obstruction.”
- Detailed pathwise calculation: `manuscripts/magent_elbo_whitepaper/13_appendices.tex`, section “Typed moving-peer iterated path derivative.”
- Focused regression suite: `manuscripts/magent_elbo_whitepaper/verification/test_elbo_oracles.py`.

## Fixed-joint comparison

For one fixed posterior-independent joint and the fine product family, the negative ELBO is a sum of factor entropies minus an expectation of the fixed log joint. Along a site-local path `Gamma_a`, only one receiver factor and one sender factor vary. The energy expectation is affine in the selected sender factor, so its second sender derivative is zero; the sender-entropy second derivative is independent of the receiver factor. The iterated receiver-once, sender-twice derivative therefore vanishes.

This is the standard fixed-joint mean-field organization described by Wainwright and Jordan, *Graphical Models, Exponential Families, and Variational Inference* (2008), DOI `10.1561/2200000001`, and Blei, Kucukelbir, and McAuliffe, *Variational Inference: A Review for Statisticians* (2017), arXiv `1601.00670`.

## Peer derivative

For a positive linear mass-preserving transport, write `r=Tq_j` and `u=Th_j`. Direct differentiation gives

\[
\left.\partial_s\partial_t^2
\operatorname{KL}(q_i+s a_i\Vert r+t u)\right|_{(0,0)}
=\int a_i\left(\frac{u}{r}\right)^2d\nu_i.
\]

After aggregating channels at site `a`, the centered receiver tangent converts this term into a variance. The finite theorem sums derivatives from separate site-local paths and obtains

\[
\lambda\sum_a w_a\operatorname{Var}_{q_{i,a}}(G_{ij,a})>0.
\]

This sum is not presented as the derivative of one simultaneous all-site path.

## Rejected simultaneous-site proof

An independent variational checker supplied a counterexample to the earlier simultaneous-site draft. For binary factors and

\[
p(y)\propto\exp(\theta x_{i,1}x_{j,1}x_{j,2}),
\]

the product-family energy contains `-theta m_i1 m_j1 m_j2`. Moving both sender sites with one parameter gives a nonzero receiver-once, sender-twice derivative. Moving either sender site alone gives zero. The source at `9833a44` had already adopted site-local paths; the debate retained this counterexample as a falsification guard.

## Continuum boundary

Commit `33059bb` defines the measurable sender tangent, continuum aggregate, and centered receiver tangent before assuming one common admissible rectangle, finite nearby KLs, bounded transported ratios, and a common differentiation envelope for that exact path. The conclusion is conditional on positive integrated variance and zero remainder derivative. No probability law on a space of sections appears in the construction.

## Mechanical checks

- Focused oracle suite: `17 passed` during Task 3 review.
- Labels and references: zero duplicate labels and zero missing references in the reviewed source.
- Citation keys: zero missing cited keys.
- `git diff --check`: clean.
