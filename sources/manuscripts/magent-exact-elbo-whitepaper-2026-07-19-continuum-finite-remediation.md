---
type: manuscript
title: "MAgent Exact-ELBO White Paper: 2026-07-19 Continuum--Finite Remediation Record"
aliases:
  - "MAgent exact ELBO continuum finite remediation"
  - "MAgent Exact-ELBO White Paper remediation record"
authors:
  - Robert C. Dennis
year: 2026
status: in preparation
tags:
  - cluster/vfe
  - cluster/multi-agent
  - cluster/gauge-theory
  - cluster/info-geometry
  - project/multi-agent
  - field/mathematics
  - field/statistics
  - field/cs-ml
created: 2026-07-19
updated: 2026-07-19
---

# MAgent Exact-ELBO White Paper: 2026-07-19 Continuum--Finite Remediation Record

## Scope and immutable provenance

This immutable record binds the continuum--finite remediation of `manuscripts/MAgent_exact_elbo_whitepaper.tex` to Research manuscript content commit `03c2e16bb4c6a70824056b25146f1b95e8f4df6d`, relative to baseline `b93d01f57dc0a55a11bf26ec13562f7019a5c84b`. The manuscript subtree is `4e6adf3776f105a920ae1a7ac7062f372116c3bf`. The master TeX file has Git blob `d9a67d5247d15bca1a263dae605fd9e3db48a11c` and SHA-256 `1595CFEA6A42C38A56E23B4821ECE7DDA5EC10969FCAB868E54D798310D30C34`. The committed bibliography at `manuscripts/references.bib` has Git blob `1b92941cb62c5f2c0e947e29bc1671b602386521` and SHA-256 `4B876F63130328D24A458815788D20E38A9222AFA1019EB836F103FB44B3E540`.

The executable crosswalk is independently bound to the MAgent code snapshot `3f5f094ab66c4f209fc3eb3c5b35f6f38dc13df0`. The crosswalk does not assign that executable the new paper's exact ELBO semantics. Earlier immutable records, including [[participatory-it-from-bit]] and [[vfe-population-generative-status-2026-07-12]], remain unchanged.

## Continuum-primary theory and finite probability construction

Continuum distribution-valued sections over the contextual base are the primary theory-level objects. For a finite design $D=\{c_a\}_{a=1}^{M}$, section sampling and finite marginalization are separate maps. Sampling sends supplied posterior-indexed sections $q_i^{o,X}$ and $s_i^{o,X}$ to their values on $D$. Marginalization sends the correlated finite recognition law $Q_X(dY\mid o)$ to the coordinate probability measures $q_{i,a}^{o,X}$ and $s_{i,a}^{o,X}$. The two outputs may be identified only under the explicit compatibility hypothesis

$$
q_i^{o,X}(c_a)=q_{i,a}^{o,X},
\qquad
s_i^{o,X}(c_a)=s_{i,a}^{o,X}.
$$

Neither map defines the other. The finite recognition kernel supplies no unique off-design extension and no probability law on the space of continuum sections. The paper proves no continuum-limit theorem.

A finite design is also not automatically a lattice gauge theory. Finite coordinate laws are site or matter data. A lattice construction additionally requires a separately declared interaction complex, group-valued link variables on oriented edges, and declared two-cells or plaquettes before a discrete-curvature statement is available. These finite interaction data remain distinct from the smooth principal connection over the contextual base.

## Exact finite ELBO and typed mean-field reduction

For fixed structural data $X$, the generative object is the normalized probability kernel $P_\theta(do,dY\mid X)$, and the recognition object is the normalized, generally correlated kernel $Q_X(dY\mid o)$. Densities are Radon--Nikodym derivatives relative to declared finite product reference measures; they are not interchangeable with the probability measures. Under positive finite evidence, posterior absolute continuity, and the stated logarithmic integrability assumptions, the paper obtains the exact identity

$$
\log p_\theta(o\mid X)
=\mathcal L_{\mathrm{state}}(Q_X;\theta,o,X)
+D_{\mathrm{KL}}\left(
Q_X(\mathord\cdot\mid o)
\middle\Vert
P_\theta(\mathord\cdot\mid o,X)
\right).
$$

Mean field is a restriction of this correlated finite law. The agent-block measures $Q_{X,i}$, state-factor measures $Q^k_{X,i}$, and model-factor measures $Q^m_{X,i}$ are probability measures on complete design blocks. Their distinct densities are $\xi^{\mathrm{block}}_{X,i}$, $\xi^k_{X,i}$, and $\xi^m_{X,i}$ relative to the corresponding design-product base measures. A generic coordinate density obeys

$$
q_b^\star(y_b)
=\frac{\exp\left(\mathbb E_{Q_{-b}}[\log p_\theta(o,Y\mid X)]\right)}
{\int\exp\left(\mathbb E_{Q_{-b}}[\log p_\theta(o,u_b,Y_{-b}\mid X)]\right)\nu_b(du_b)}.
$$

The normalized coordinate-maximizing probability measure is $q_b^\star\nu_b$; its density is unique only up to $\nu_b$-null sets. The agent-block and state--model product families retain dependence across the design points inside each factor. They are therefore coarser than the separate site-factorized comparison family used by the obstruction below.

## Fine site-factorized moving-peer obstruction

The finite theorem is restricted to the independently variable family $Q=\bigotimes_{\ell,b}q_{\ell,b}$, with mixture-open site factors. For each site $a$, a separate site-local path $\Gamma_a$ varies only $q_{i,a}$ and $q_{j,a}$. It does not use one simultaneous path that varies every design point. With positive quadrature and channel weights, fixed positive linear mass-preserving transports, bounded transported tangent ratios, a common admissible rectangle, the stated domination, and a remainder with zero iterated derivative along every $\Gamma_a$, the centered receiver tangent gives

$$
\sum_{a=1}^{M}
\left.\partial_s\partial_t^2
(\mathcal C_D\circ\Gamma_a)(s,t)\right|_{(0,0)}
=\lambda\sum_{a=1}^{M}w_a
\operatorname{Var}_{q_{i,a}^{o,X}}(G_{ij,a})>0.
$$

For the negative ELBO of a fixed posterior-independent joint on the same fine family, each corresponding site-local iterated derivative is zero. The moving-peer functional therefore cannot equal that fixed-joint negative ELBO plus a constant throughout the stated open product neighborhood.

The conditional continuum corollary first selects a measurable sender tangent $h_j(c)$, then forms the transported aggregate $G_{ij}(c)$, and then defines the exact centered receiver tangent $a_i(c)=q_i(c)[G_{ij}(c)-\mathbb E_{q_i(c)}G_{ij}(c)]$. Its conclusion requires joint measurability, fiberwise zero mass, one common admissible rectangle for that exact path, finite nearby KL divergences, bounded transported ratios, a common differentiation envelope, zero remainder derivative, and positive integrated variance. It proves only a positive iterated derivative of a deterministic base integral. It does not construct a continuum section-space law or a finite-to-continuum limit.

The theorem makes no claim about the coarser Chapter 6 cross-design families, restricted families without the required tangents, auxiliary-variable lifts, or the reduced functional obtained after substituting state-dependent $\beta^\star(q)$. It also makes no claim about a probability law on continuum sections.

## Adversarial review and binding verdict

The tracked packet at `docs/debates/2026-07-19-continuum-moving-peer-obstruction/` records the red case, blue case, rebuttals, exact fixtures, binding verdict, and adopted action. The first proposed simultaneous-site proof was rejected because a two-site counterexample produces a mixed cross term. The amended claim uses separate site-local paths and sums their iterated derivatives. A second challenge restricted the claim to the fine site-factorized family and required the exact centered continuum tangent plus common admissibility and domination hypotheses. After those amendments, the red and blue sides independently accepted the claim and the judge returned `CLAIM_TRUE`. The exact finite fixture gives zero for the fixed-joint derivative and $27/3200$ for the peer variance term. This verdict verifies the scoped theorem; it does not extend its domain.

## Attention response identity

For a fixed normalized row prior $\widetilde\pi_i$, positive temperature $\tau$, and edge energies $E_{ij}$, the optimized entropy-retaining row satisfies

$$
\mathcal R_i^{\mathrm{red}}
=S_i+\tau D_{\mathrm{KL}}(\beta_i^\star\Vert\widetilde\pi_i)
\geq S_i,
\qquad
S_i=\sum_j\beta_{ij}^\star E_{ij}.
$$

Equality holds exactly when $\beta_i^\star=\widetilde\pi_i$, equivalently when $E_{ij}=E_{ik}$ for every $j,k$ in the positive prior support $\mathcal J_i^+=\{j:\widetilde\pi_{ij}>0\}$. Energies outside that support are unrestricted. The covariance term in $dS_i$ is a response contribution; its cancellation in one direction does not imply equality of the two scalars.

## Literal and runtime code crosswalk

At code snapshot `3f5f094ab66c4f209fc3eb3c5b35f6f38dc13df0`, the literal `CONFIG` in `run_experiment.py:4599--4872` selects `mode='ouroboros'`, twelve agents, latent dimension seven, a $12\times12$ spherical grid, `vfe_class='full'`, smooth initialization, fixed synthetic Gaussian observations, and gauge-fixed model fibers. The literal also assigns `tau_belief=1.0`, `tau_model=1.0`, `learnable_kappa=False`, and `kl_regulariser_eps=None`. Omitted dataclass fields inherit divergence order one, `sigma_natural_gradient=False`, the Frobenius frame metric, a frozen hyperprior, disabled top-down prior propagation, disabled manifold pair transport, and a uniform attention prior before support folding. The loader and runtime materialize `kl_regulariser_eps=None` as $\texttt{KL\_REGULARISER\_EPS}=10^{-4}$ rather than zero.

The selected weights are $(1,0.5,1,0.5,1,0.5,0.01,0.1)$ for the self, model-self, belief-alignment, model-alignment, observation, hyperprior, frame-smoothness, and Yang--Mills-labeled slots. The reached scalar is

$$
F_{\mathrm{live}}
=(T_1+R_{\alpha^q})+0.5(T_2+R_{\alpha^s})+T_3+0.5T_4+T_5
+0.5T_6+0.01R_{\mathrm{smooth}}+0.1R_{\mathrm{YM}}.
$$

The belief and model pair transports are built from stored vertex frames in `gauge_agent/full_vfe.py:1463--1478`, `1554--1575`, and `1584--1599`, and their application uses $\mu\mapsto\Omega\mu$ and $\Sigma\mapsto\Omega\Sigma\Omega^{\mathsf T}$ in `gauge_agent/lie_groups.py:64--94`. Independently stored base lattice links reach $R_{\mathrm{YM}}$, not the active matter transport. `NaturalGradientDynamics.step` differentiates the assembled scalar once and updates connected fast and slow sectors in the same phase; Ouroboros closure then performs an external apex-prior overwrite when its conditions hold. The runtime therefore constructs an engineered differentiable scalar, not the paper's fixed normalized population joint and correlated recognition law.

At the base scale, $R_{\mathrm{YM}}$ is the fixed-frame Frobenius plaquette deficit on the independently stored base-lattice twists. At higher scales the same slot can fall back to a finite-difference penalty on vertex frames. A Frobenius norm of a based holonomy deficit is not invariant under conjugation by a general $\mathrm{GL}^{+}(K)$ frame change. The executable regularizer consequently has no general $\mathrm{GL}^{+}(K)$ continuum gauge-action interpretation, and no continuum target is claimed without a mesh family, scaling law, and convergence theorem.

## Revision-bound verification

The finite-oracle command was

```powershell
$env:PYTHONDONTWRITEBYTECODE = '1'
& 'C:\Python314\python.exe' -m pytest manuscripts\magent_elbo_whitepaper\verification\test_elbo_oracles.py -q -p no:cacheprovider --junitxml=C:\tmp\magent-exact-elbo-oracles-03c2e16-95d969c5f8554e5dbb71ea587f60f178.xml
```

Under Python 3.14.4 and pytest 9.0.2, the JUnit record reports 17 tests, 0 failures, 0 errors, 0 skipped, and 0.487 seconds. Its SHA-256 is `D502C6CA55020FC8656326875DDE9F84D5952040EB0821FE47EC1C30C92BBD6B`.

The clean isolated build used pdfTeX 1.40.27 from TeX Live 2025 and BibTeX 0.99d. The sequence was a first `pdflatex` pass, copying the committed `references.bib` into the isolated build directory, `bibtex`, and three further `pdflatex` convergence passes. The resulting 105-page PDF has SHA-256 `AC7630AC03C96F1B730B5D674F1E0B57554812AA996FCAA985DB2C59863692CA`. The final log, BBL, and BLG hashes are `FA3E7110290711732332850618902D1087AB96A7C4D252833FF39547CBF54D40`, `69E547749F84B0E7EF6B50080E781212B776D402CB40D899CD4A7689146AC6BD`, and `797D8EC5D572FB686B54A49EA0B7A3951FB3F93E11C4BCD5BABE0E922A57DF80`.

The final log contains 0 fatal errors, 0 undefined references or citations, 0 duplicate destinations, and 0 overfull boxes. Eight underfull bibliography lines from long immutable URLs are nonblocking. Visual inspection of pages 1, 16, 54, 64, 74, 80--84, and 104 found no clipping, overlap, unreadable glyphs, or broken page furniture.

## Residual limits

No probability law on continuum section space, continuum reconstruction from finite marginals, or finite-to-continuum convergence theorem is supplied. The moving-peer obstruction does not cover the coarser Chapter 6 mean-field family, reduced attention after substituting $\beta^\star(q)$, or auxiliary-variable lifts. The executable Frobenius plaquette deficit is a fixed-frame regularizer, not a general $\mathrm{GL}^{+}(K)$ continuum gauge action. The focused exact-oracle fixtures test the finite formulas and regressions but do not by themselves prove the general mathematical statements; closure of those claims rests on the written derivations, adversarial challenges, and explicit hypotheses.

## Relevance to this research

This record gives [[Gauge-Theoretic Multi-Agent VFE Model]] a revision-bound separation among continuum statistical-bundle theory, exact finite probability, mean-field restrictions, the legacy moving-peer scalar, and the selected executable. It updates the stored accounts in [[Evidence lower bound (ELBO)]], [[Mean-Field Approximation]], and [[Multi-agent variational free energy]] without turning a finite design into a continuum law or retrofitting exact-ELBO semantics onto `FullVFE`.

## Sources

- `docs/debates/2026-07-19-continuum-moving-peer-obstruction/04_verdict.md` -- binding red--blue verdict for the amended site-local theorem.
- [[participatory-it-from-bit]] -- continuum multi-agent statistical-bundle and legacy population-functional source.
- [[vfe-population-generative-status-2026-07-12]] -- earlier fixed-state obstruction and auxiliary/configuration constructions.
- [[wainwright-2008-graphical-models-variational]] -- fixed-joint mean-field variational structure.
- [[Gauge-Theoretic Multi-Agent VFE Model]] -- project-level synthesis and executable scope.
