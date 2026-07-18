# Evidence Pack — beyond-mean-field gauge VFE

## Manuscript references

- manuscripts/PIFB2.tex:522 classifies the peer-KL block as an engineered consensus energy rather than a derivation from the free-energy principle.
- manuscripts/PIFB2.tex:3273 proves the scoped obstruction to representing live peer-KL terms as the mean-field negative ELBO of one fixed state-level joint.
- manuscripts/PIFB2.tex:3413 defines the proposed normalized state/configuration hierarchy and its exact joint KL identity.
- manuscripts/PIFB2.tex:3465 introduces tree-exact node and edge beliefs, loopy region approximations, and a sparse block-Gaussian correlated family.
- manuscripts/PIFB2.tex:3497 defines the state-reduced configuration action, connected generating functional, 1PI action, local one-loop correction, and proposed 2PI extension.
- manuscripts/PIFB2.tex:3569 gives the pre-existing configuration Gibbs lift; its random variable is a whole belief configuration, not the original state latent.
- manuscripts/PIFB2.tex:3626 begins the pre-existing exact Gibbs pushforward RG construction and separates exact pushforward from truncation closure.
- manuscripts/meta_entropy.tex:167 distinguishes belief entropy, attention-row entropy, and configuration meta-entropy.
- manuscripts/meta_entropy.tex:362 derives the large-deviation form of the configuration meta-entropy under an exchangeable compact-container reference law.
- manuscripts/meta_entropy.tex:549 gives the Riemannian-Langevin interpretation of positive configuration temperature.

## Canon excerpts

- Wainwright and Jordan, Foundations and Trends in Machine Learning 1 (2008), DOI 10.1561/2200000001: ordinary variational inference starts from a fixed normalized graphical model; mean field is a restricted variational family, while tree-structured marginal polytopes permit exact inference.
- Yedidia, Freeman, and Weiss, IEEE Transactions on Information Theory 51 (2005), DOI 10.1109/TIT.2005.850085: belief propagation is exact on trees; Bethe stationary points characterize loopy BP, and region-graph/Kikuchi constructions enlarge the approximation.
- Blei, Kucukelbir, and McAuliffe, Journal of the American Statistical Association 112 (2017), DOI 10.1080/01621459.2017.1285773: the ELBO is defined relative to a fixed joint distribution and a separately chosen variational family.
- Cornwall, Jackiw, and Tomboulis, Physical Review D 10 (1974), DOI 10.1103/PhysRevD.10.2428: a double Legendre transform yields an effective action for the mean field and full two-point function.
- Abbott, Acta Physica Polonica B 13 (1982), pp. 33–50: the background-field method preserves background gauge covariance in the effective action.
- Faddeev and Popov, Physics Letters B 25 (1967), DOI 10.1016/0370-2693(67)90067-6: redundant gauge-orbit integration requires a gauge-fixing determinant.
- Wilson and Kogut, Physics Reports 12 (1974), DOI 10.1016/0370-1573(74)90023-4: integrating out short-scale degrees of freedom generates an effective action whose symmetry-allowed operator content need not close in the original ansatz.

## What this evidence does not settle

The evidence does not prove that the proposed state variables and pair potentials are the unique best generative model for language or multi-agent cognition. It does not prove normalizability of the noncompact \(\mathrm{GL}^+(K)\) configuration theory without a specified regulator. It does not select a 2PI truncation, establish its convergence, or show that the five-term functional is quantitatively close to the exact RG image. It also does not decide which local frame transformations are physical epistemic changes and which are true redundancies; the quotient must follow that modeling declaration.
