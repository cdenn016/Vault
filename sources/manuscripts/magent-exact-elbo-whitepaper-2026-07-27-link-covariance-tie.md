---
type: source
subtype: manuscript
title: "MAgent exact-ELBO white paper — the link-covariance tie graded a postulate (2026-07-27)"
aliases:
  - "link covariance tie"
  - "covariance tie postulate"
  - "B0a covariance tie"
tags:
  - cluster/vfe
  - cluster/attention
  - cluster/variational
  - project/multi-agent
  - project/transformer
status: verified
created: 2026-07-27
updated: 2026-07-27
---

# MAgent exact-ELBO white paper — the link-covariance tie graded a postulate

## Provenance

| Field | Value |
|---|---|
| Research commit | `70d4b9583f11581b277c9f71f04977340911baee` |
| Whitepaper subtree | `48a2636a5c9f1af48b4982f6da1366b0e9ea8e10` |
| `06_mean_field_theory.tex` blob | `a6f4c3368d025d3b47be64e5d61f30007707f910` |
| `09_pifb2_crosswalk.tex` blob | `3dfae187e4eb4228d2f8aef93fc911b3c31835df` |
| `13_appendices.tex` blob | `d880d45fa90909129a96b67426ec77bbe48bb3e8` |
| `PIFB2.tex` blob | `9f7aed8377e2f2ba3d6073381da091d4121d32a0` |
| Oracle (MAgent) | `verification/b0_covariance_tie.py`, 15 checks, seed 20260727 |
| Ledger (MAgent) | `.verification/ledger-b0a-tie-2026-07-27.json`, 6 claims, closure mode |
| Build | whitepaper 115 pages, PIFB2 173 pages, 0 errors, 0 undefined |

Predecessor: [[magent-exact-elbo-whitepaper-2026-07-27-attention-derivation]], which
constructed the source-label lift and left this tie explicitly open.

## The question

The attention-row derivation established that PIFB2's row is the exact mean-field coordinate
update of a declared source label, under four hypotheses. One was left ungraded: whether

$$R_{ij} = \Omega_{ij}\Sigma_j\Omega_{ij}^\top =: S_{ij}$$

can be justified from within the theory, discharged as an M-step fixed point, or must stand
as a declared postulate. It is the one step setting a generative (slow-timescale) parameter
from a recognition (fast-timescale) quantity.

## Answer: a declared postulate

The M-step route is **refuted**, not merely unproved, and no selection principle drawn from
information geometry picks the tie out. What survives is a uniqueness result that is honest
but circular — the tie is the unique link covariance *producing the desired row*, which is a
statement about the target rule rather than a derivation of it. In the vocabulary of
model-based clustering this is a constrained-covariance choice: declared and compared between
candidate models, never justified as an estimator.

## Three results

### 1. The tie and the unit temperature are one hypothesis, not two

Require the offset $E_{ij} - \tau^{-1}\KL_{ij}$ to be source-free *as an identity in the
sender mean*, which is unconstrained and sweeps $\mathbb R^d$ because $\Omega_{ij}$ is
invertible. Only the quadratic form in $\Delta_{ij}$ carries that dependence, with coefficient
$\tfrac12(R_{ij}^{-1} - \tau^{-1}S_{ij}^{-1})$, so source-freeness forces $R_{ij} = \tau S_{ij}$.
Substituting back, the surviving term varies with $\log\det S_{ij}$ at rate $(\tau-1)/(2\tau)$,
which vanishes only at $\tau = 1$. Fixing the scale fixes the temperature.

Corollary: $R_{ij} = cS_{ij}$ reproduces the tempered row exactly at $\tau = c$, including its
per-source log-determinant logit. The generative link-covariance scale and the recognition
softmax temperature are **the same parameter**, so the earlier "temperature is not free"
finding and this tie are one one-parameter family rather than two separate results.

Consequence: a divergence-scored row at nonunit temperature is not the exact label coordinate
of any model in the family — tied, scaled, or free. The lift does not reach the deployed
$\tau = \kappa\sqrt K$.

### 2. The M-step refutes the tie; the deficit is a Stein loss

Since $\Delta^\top R^{-1}\Delta = \operatorname{tr}(R^{-1}\Delta\Delta^\top)$, the edge energy
depends on $R$ only through $C_{ij} := \Sigma_i + S_{ij} + \Delta_{ij}\Delta_{ij}^\top$, and the
unique stationary point is $R^\star_{ij} = C_{ij}$. Hence

$$R^\star_{ij} - S_{ij} = \Sigma_i + \Delta_{ij}\Delta_{ij}^\top \succ 0 \quad\text{always},$$

so the tie is never stationary. The evidence lower bound forgone per edge is exactly the Stein
loss $\tfrac12[\operatorname{tr}(S^{-1}C) - \log\det(S^{-1}C) - d]$, strictly positive.

Reading: the divergence-scored row prices its sources as though the receiver were already
certain and already in agreement. The two omitted terms have names — $\Sigma_i$ is the
mean-field residual spread, present because the predicted quantity is itself a belief rather
than an observation, and $\Delta\Delta^\top$ is the squared prediction error an M-step exists
to absorb.

### 3. Impossibility: a correlated family buys stationarity OR the row, never both

This bears directly on the correlated-VFE program, which is an independently motivated
direction rather than an artificial escape. Let the pair recognition factor be jointly Gaussian
with cross-covariance $C$. The tie becomes an M-step fixed point **iff**

$$C\Omega_{ij}^\top + \Omega_{ij}C^\top = \Sigma_i + \Delta_{ij}\Delta_{ij}^\top,$$

which is solvable and Schur-admissible on a nonempty set. But the row is divergence-scored iff
$\operatorname{tr}(S_{ij}^{-1}(C\Omega^\top + \Omega C^\top))$ is source-free, and the
stationarity condition fixes that symmetric combination *uniquely*, leaving no freedom. Under
it the trace becomes $\operatorname{tr}(S_{ij}^{-1}(\Sigma_i + \Delta\Delta^\top))$, which is
generically source-dependent. Mean field ($C = 0$) is the unique member of the family yielding
the row, and it is exactly the member where the tie fails to be stationary.

## Further findings

**The tie's intuitive story is incoherent.** Setting the link covariance to the transported
sender covariance does not make the link reproduce the transported sender: the predictive
covariance is $2S_{ij}$, twice as dispersed as the belief it carries. The choice reproducing
the transported belief is $R_{ij} = 0$, outside the positive-definite cone.

**The untied edge energy is a cross-entropy, not a divergence.** With $P_{ij} :=
\mathcal N(\Delta_{ij}, \Sigma_i + S_{ij})$ the residual law, $E_{ij}(R) = \KL(P_{ij}\Vert
\mathcal N(0,R)) + H(P_{ij})$. It goes negative and does not vanish at coincidence, so it is a
Fenchel-Young pairing missing the dual potential of its first argument. The general principle:
*a score induces a divergence row iff its entropy part is source-free*.

**The profiled alternative should be rejected.** Eliminating $R$ gives an exact, gauge-invariant,
genuinely stationary rule $\beta_{ij}\propto\pi_{ij}\det(C_{ij})^{-1/2}$, but its logit grows like
$\log(1+m^2)$ against the KL row's $m^2/2$, so it cannot select on means (weight on a badly
mismatched source 0.148 versus $1.1\times10^{-7}$ at $m^2=64$); and at $\Delta = 0$ it is
Loewner-monotone in $S_{ij}$, ranking sender *confidence* rather than agreement, with no minimum
at coincidence. Its tail is $\lVert\Delta\rVert^{-1}$, heavier than any multivariate Student-$t$.
It shares only the $\det(A)^{-1/2}$ prefactor of the $\rho=1$ probability product kernel
(Jebara–Kondor–Howard), not its Gaussian tail.

**The ordered mask is forced by edge reciprocity, not by flatness.** A proposed dissolution via
the non-flat connection does not work: `gauge_agent/non_flat_connection.py:234-236` builds
$V_{ji} = V_{ij}^{-1}$, so $\Omega_{ij}\Omega_{ji} = I$ and the reciprocal pair stays singular
even at large 3-cycle holonomy. Escaping the mask means surrendering edge reversibility, which
lattice gauge theory takes as basic ($U_{ji} = U_{ij}^\dagger$).

## What the manuscripts may and may not claim

May: the divergence-scored row **at unit temperature** is realizable as the exact CAVI label
coordinate of a declared normalized joint under an ordered source mask, and $R_{ij} = S_{ij}$ is
the unique link covariance realizing it.

May not, unqualified: that the deployed rule "is an exact variational coordinate rather than an
engineered scalar." The model was selected by demanding the rule, and the deployed temperature
is excluded from the family.

## Ledger

Five claims closed `EVIDENCE_VERIFIED`; one deliberately `INCONCLUSIVE` — the universal negative
that *no* principle and *no* recognition family can discharge the tie, which the checked
principles (maximum entropy, m-projection, profile maximum likelihood, minimum description
length, inverse-Wishart MAP) do not exhaust. Its open obligations name richer structured
families, Wishart marginalization instead of profiling, and whether the profiled bound is
bounded above.

## Relevance to this research

Converts the last open hypothesis of the attention-derivation program into a graded one, and in
doing so merges two hypotheses that were being tracked separately. The impossibility result is
the load-bearing item for planning: it tells the correlated-VFE track that relaxing mean field
will not rescue the divergence-scored row, so that track should be pursued for its own reasons
rather than as a repair of this one.

## Related

[[GL(K) gauge-equivariant attention]] · [[Evidence lower bound (ELBO)]] ·
[[Multi-agent variational free energy]] · [[Mean-Field Approximation]] · [[Softmax]] ·
[[Gauge-Theoretic Multi-Agent VFE Model]] · [[Variational EM]] · [[Holonomy]]

## Sources

[[magent-exact-elbo-whitepaper-2026-07-27-attention-derivation]] ·
[[bishop-2006-pattern-recognition-machine-learning]] ·
[[dempster-1977-em-algorithm]] · [[neal-1998-variational-em]]

Bib-only (no vault note): Celeux and Govaert, *Gaussian parsimonious clustering models*, Pattern
Recognition 28(5):781–793, 1995, for the constrained-covariance classification; Jebara, Kondor
and Howard, *Probability product kernels*, JMLR 5:819–844, 2004, for the kernel the profiled row
resembles but is not; Roweis and Ghahramani, *A unifying review of linear Gaussian models*,
Neural Computation 11(2):305–345, 1999, for why the posterior second moment rather than the mean
outer product enters the noise M-step.
