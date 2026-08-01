# Pass-3 implementation verification: holonomy, KL, and coarse-graining

Date: 2026-08-01
Artifact: `manuscripts/gauge_vfe_rg/main.pdf`

## Plain-language verdict

The manuscript now gives a rigorous version of the proposed mechanism. Holonomy and belief KL
have different jobs:

- represented holonomy determines which parallel degrees of freedom a candidate block can retain;
- transported forward KL measures whether the current marginal laws actually occupy one of those
  permitted common law modes;
- a normalized coarse Markov channel with common recovery decides whether the full joint
  experiment, rather than only its one-agent marginals, is preserved; and
- a separately declared rate, complexity, free-energy, or description-length rule selects a
  nontrivial partition and scale.

Thus trivial represented holonomy permits a full-dimensional parallel sector, but does not force
belief agreement. Nontrivial holonomy can retain a lower-dimensional sector, and it can also
stabilize a symmetric law whose marginal KL distortion is zero. Holonomy and KL are therefore
complementary variables, not equivalent criteria.

## What was implemented

### General theorem

`06_general_coarsegraining.tex:419-617` now defines, for each channel
`x in {b,m}`, a holonomy-fixed parent-law family and the transported forward-KL score

    D_I^x = inf_Q sum_i w_i D_KL(P_i^x || Q).

For bimeasurable bijective transports, an equivariant parent family, and positive weights, the
manuscript proves:

1. the score is independent of rooted paths, root, and passive gauge coordinates;
2. if the infimum is attained, zero score is equivalent to a holonomy-stabilized parallel section
   of marginal laws;
3. if the zero infimum is not attained, only approximation by admissible fixed parent laws follows;
4. exact joint preservation requires a normalized coarse channel `C` and one recovery channel `R`
   satisfying `P_theta C R = P_theta` for the whole experiment; and
5. parallel cross morphisms `Phi:E_b -> E_m` and `Phi~:E_m -> E_b` carry fixed marginal-law
   sections in the stated directions. Base-connection parallelness is kept distinct from a
   separately assumed graph-link intertwining law.

### Linear and multivariate-Gaussian realization

`09_coarsegraining.tex:332-775` now proves and specializes the general result:

- root evaluation identifies the connection-Laplacian kernel with the common fixed subspace of
  represented internal holonomy;
- the full, partial, and zero fixed-sector cases are distinguished;
- the `R`-orthogonal projector and constant-metric relaxation have exact convergence, decay-rate,
  dissipation, congruence, and time-dependent covariance statements;
- the Fisher natural-gradient identification is exact only on the fixed-covariance Gaussian mean
  family, while a general statistical family receives only the local Fisher expansion;
- the unrestricted forward-KL Gaussian parent matches the first two moments,

      m_bar = sum_i a_i m_i,
      C_bar = sum_i a_i [C_i + (m_i-m_bar)(m_i-m_bar)^T],

  and has minimized score

      (1/2)[log det C_bar - sum_i a_i log det C_i];

- compact represented holonomy is handled by Haar averaging of first and second moments; expanding
  noncompact holonomy can leave no invariant nondegenerate Gaussian; and
- the common-covariance pairwise symmetrized-KL identity is stated with its exact scope.

Two exact counterexamples prevent overclaiming. Identity transport can have arbitrarily large
belief KL, while nonidentity holonomy can preserve an isotropic Gaussian and yield zero transported
marginal KL. A further `H={I,-I}` witness shows that ordinary pairwise disagreement can vanish even
though the holonomy-fixed parent score is strictly positive.

### Structure and source boundaries

General coarse maps and general renormalization now precede the multivariate-Gaussian realization.
The general RG chapter uses one principal bundle with two associated statistical bundles,
potentially inequivalent representations and separate connection choices. The Berman-Klinger-
Stapleton Fisher ordering, scalar Laplacian-RG scale diagnostic, network-renormalization closure
principles, and graph-learning analogies are represented as distinct inputs; none is promoted to a
proved holonomy-based partition or exact gauge-covariant blocking theorem.

## Verification evidence

### Independent mathematical rereview

- General holonomy-KL theorem: clean rereview; source SHA-256
  `85FD05F4E35F2C1EC7770CEFC1D72D07DF722107DAEBECCB54A3FB45057C6138`.
- Gaussian realization: clean rereview; source SHA-256
  `230F072DEF467F4BE0B4C0B6D825FF386A6C5B271B54CA426887819BE7AEA2AB`.
- Integration rereview: all eight previously identified cross-chapter defects were rechecked and
  found resolved.

The reviewers specifically rechecked the attainment qualification, channel typing, fixed-sector
rank theorem, projector hypotheses, Gaussian barycenter and compact-holonomy formulas, pairwise-KL
scope, cross-morphism directions, and general-before-Gaussian ordering.

### Symbolic corroboration

Independent symbolic checks returned zero residual for the fixed-covariance pairwise identity, the
Gaussian barycenter first-order conditions, `P^2-P`, `LP`, and `P^T R-RP`. They also reproduced
`det(I+uu^T)=1+||u||^2` and the path-dependent Gaussian KL witness. These checks corroborate the
displayed algebra; the proofs in the manuscript, not numerical or symbolic agreement alone, close
the mathematical claims.

### Numerical and production checks

- Deterministic verification suite: 29 PASS, 0 FAIL, 0 INCONCLUSIVE; inventory PASS; all nine
  substantive numerical claims mapped to passing checks.
- PDF: 162 pages, 1,101,044 bytes, SHA-256
  `F1275DC2DAA3CDA4410273FDB910DD9FDD286A00F30A47286DF83D9067FE80E7`.
- Final log: no LaTeX/package warnings, unresolved references or citations, overfull/underfull
  boxes, or fatal errors matched the production scan.
- Extracted PDF text: no literal `??`, TODO, FIXME, placeholder, or undefined-reference token.
- TeX source: 532 labels, all unique; no banned spacing macros or banned vague phrases remained.
- Visual inspection: the reordered contents pages, general theorem/proof, Gaussian barycenter, and
  counterexample pages are readable and unclipped.
- `git diff --check`: no whitespace errors.

The rigor scanner's candidates were triaged as hypotheses, exact measure-theoretic qualifiers,
explicit scope limitations, or ordinary non-load-bearing prose. No unpriced load-bearing hedge was
found in the new theorem, Gaussian specialization, or physicist summaries.

## Primary-source scope rechecked

- Berman, Klinger, and Stapleton, *Bayesian Renormalization*,
  <https://arxiv.org/abs/2305.10491>.
- Villegas et al., *Laplacian renormalization group for heterogeneous networks*,
  <https://doi.org/10.1038/s41567-022-01866-8>.
- Garuccio, Lalli, and Garlaschelli, *Multiscale network renormalization*,
  <https://doi.org/10.1103/PhysRevResearch.5.043101>.
- Gabrielli et al., *Network Renormalization*, <https://arxiv.org/abs/2412.12988>.

## Deliberately open obligations

The revision does not claim that the full research program is closed. It states four remaining
obligations precisely:

1. construct a normalized gauge-equivariant joint coarse channel for each admissible block;
2. prove a common recovery/sufficiency theorem for the relevant joint experiment;
3. justify a nondegenerate intrinsic partition and scale selector; and
4. prove closure of normalized law, connection, cut-link, rescaling, and cross-morphism data under
   repeated nonflat blocking.

Physical-law status also remains open until a specified system, observables, competing baselines,
uncertainty-bearing predictions, and a prospective falsification threshold are supplied.
