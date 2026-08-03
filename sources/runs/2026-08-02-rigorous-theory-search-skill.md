---
type: run
title: "Rigorous theory search global skill: design, evaluation, and mathematical reconstruction (2026-08-02)"
aliases:
  - "2026-08-02 rigorous theory search implementation record"
  - "Rigorous theory search skill implementation record"
  - "Rigorous theory search baseline and reconstruction record"
tags:
  - cluster/methodology
  - cluster/vfe
  - cluster/gauge-theory
  - cluster/info-geometry
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/mathematics
  - field/physics
  - field/statistics
year: 2026
created: 2026-08-03
updated: 2026-08-03
---

# Rigorous theory search global skill: design, evaluation, and mathematical reconstruction (2026-08-02)

## Scope and sanitized provenance

This immutable note records the research content of five project-authored documents about the
`rigorous-theory-search` protocol. The source bundle has SHA-256
`DE59FA073A5B2278974D55A1EC3AA4B8FC8F742286130A8F36EB8B5931065DB7`. Its five authored files
are identified by relative path and byte hash:

| Archived document | SHA-256 |
|---|---|
| `docs/2026-08-02-edits.md` | `6C9653FCF0BE45B37C8239E3BFDA76A1D3DA6737BD8C52AE9029BAD5B9537BBF` |
| `docs/evals/2026-08-02-rigorous-theory-search-baseline.md` | `412092A908FB72F59D3EBD3C9A5617B2CC1988AA46080D46141F111081AD6FE7` |
| `docs/superpowers/plans/2026-08-02-rigorous-theory-search.md` | `70B9159EF251D2FAABD45E9E914997CA842C0CE51A8FDBC5D3D90B917FA02CE6` |
| `docs/superpowers/specs/2026-08-02-rigorous-theory-search-design.md` | `1129FAA8DABA57E8C2D0B996654625DD4996635575A7C9091E127FED8735D1D3` |
| `docs/verification/2026-08-02-rigorous-theory-search/independent-mathematical-reconstruction.md` | `A1E4466722D4FB72C4DC790B67CE10E73B8998F475C3E68DADCE321F517C745F` |

The hashes identify the archived bytes only. They do not certify the current implementation, any
later skill revision, or any theorem produced by using the method. This ingest deliberately omits
absolute paths, branch and worktree instructions, protected-WIP filenames, runtime and model
identifiers, process or session metadata, raw event streams, test totals, coverage figures,
installer internals, and historical approval language. No raw evaluation stream or private scratch
artifact was copied into the vault.

## Epistemic contract

The protocol separates **discovery** from **certification**. A request to assume that an affirmative
construction exists may direct search effort, but it is recorded only as an affirmative search
prior. It is not an admissible theorem premise, evidence item, or proof dependency. Before release,
an oracle-erasure audit removes that search prior and rechecks the target's full dependency closure.

Every investigation freezes a problem contract: target formula and quantifiers, domains and
codomains, regularity, measures, boundary conditions, group actions, equivalence relations,
permitted background results, modeling postulates, falsification criterion, and literature policy.
This prevents a construction for a nearby or weakened statement from being reported as a solution
to the original target.

Search proceeds through a mechanism-diverse portfolio rather than a fixed number of agents assigned
to cosmetic variants of one idea. A route must return a typed construction, a proved lemma, a
scope-matched counterexample, or a named obstruction with the exact obligation needed to remove it.
Cross-pollination begins only after the parent routes expose their assumptions and gaps; every
hybrid acquires a new interface obligation.

Atomic claims live in an acyclic dependency graph. Mathematical closure requires a derivation,
formal proof, or an applicable theorem whose hypotheses have been checked. Finite computation,
symbolic simplification without side conditions, figures, citations alone, or agreement among
solvers cannot establish a universal theorem. Structural validation can check contracts, paths,
states, dependencies, and evidence metadata, but cannot establish mathematical truth.

The terminal vocabulary is:

- `COMPLETE_AFFIRMATIVE`: the exact frozen target and every load-bearing ancestor are proved;
- `COMPLETE_NEGATIVE`: a certificate negates the exact frozen target, with quantifier scope checked;
- `INCONCLUSIVE`: the strongest proved result and a minimal explicit obligation set are recorded.

The third state is a legitimate closure of the search record. It is not permission to disguise an
unproved affirmative result as a nearly complete theorem.

## Mathematical reconstruction retained from the dossier

The archived reconstruction checks the domain gates that motivated this method. The results below
are conditional mathematical statements; each displayed hypothesis is load-bearing.

### Associated-bundle Fisher pullback

Let $P\to B$ be a principal right $G$-bundle and $E=P\times_G S\to B$ an associated statistical
bundle. A connection gives the connection-relative vertical first jet of a section,

$$
D^\omega s_x=\operatorname{ver}_{s(x)}^\omega\circ T_xs:T_xB\to V_{s(x)}E.
$$

If the fiberwise Fisher tensor $I$ is finite and smooth, directional scores are square-integrable,
and differentiation under the defining integral is justified, then

$$
h_x^\omega(X,Y)=I_{s(x)}(D^\omega s_xX,D^\omega s_xY)
$$

is a symmetric positive-semidefinite tensor on the base. Passive-gauge invariance is guaranteed
when the statistical $G$-action is a Fisher isometry and the induced connection and section
transform compatibly. This is a sufficient general condition, not a necessity in degenerate or
special cases. The tensor generally remains dependent on the chosen connection.

Where $I$ is positive definite on the relevant vertical directions,

$$
\operatorname{rad}h_x^\omega=\ker D^\omega s_x,
\qquad
\operatorname{rank}h_x^\omega=\operatorname{rank}D^\omega s_x.
$$

Thus the pullback is ordinarily a semimetric. A vector-bundle quotient needs constant rank; a
quotient-manifold metric additionally needs an involutive radical distribution, a regular leaf
space, and basicness. This agrees with the more complete program record
[[gauge-vfe-rg-pullback-geometry-2026-08-01]].

### Vertical histories and information duration

A curve $\gamma:J\to E_x$ inside one fiber satisfies $\pi_E\circ\gamma=x$, hence
$T\pi_E(\dot\gamma)=0$: it is intrinsically vertical. Endpoints do not determine the path,
orientation, or duration. A general total-space curve $\Gamma$ with base projection $c$ has the
connection-relative split

$$
\dot\Gamma=\operatorname{hor}^\omega\dot\Gamma+
\operatorname{ver}^\omega\dot\Gamma.
$$

A family of sections is pointwise vertical after fixing a base point and is globally a curve in
section space. Its supplied parameter is not emergent time. The Fisher length

$$
L[\gamma]=\int\sqrt{I_\gamma(\dot\gamma,\dot\gamma)}\,d\lambda
$$

is invariant under regular orientation-preserving reparameterization. On a nonzero-speed segment
it yields intrinsic arclength up to origin and orientation, but degeneracy, stalls, closed histories,
and synchronization failures obstruct a global clock. Even an exact clock one-form supplies only a
scalar potential; an operational bridge to physical time remains an additional postulate.

### ELBO and local--global bookkeeping

For $p(y)>0$, $q\ll p(\cdot\mid y)$, and finite displayed terms,

$$
\log p(y)=\mathcal L(q;y)+\operatorname{KL}\!\left(q\,\|\,p(\cdot\mid y)\right),
\qquad \mathcal F=-\mathcal L.
$$

For joint laws $Q,P$ with densities $q,p$ relative to a common product measure and finite terms,

$$
\operatorname{KL}(Q\|P)
=\operatorname{TC}(Q)
+\sum_i\operatorname{KL}(Q_i\|P_i)
+\mathbb E_Q\log\frac{\prod_i p_i}{p}.
$$

The total-correlation and interaction corrections are essential. Setting $Q=P$ to a correlated
law gives an immediate sign check: the last term must cancel $\operatorname{TC}(P)$. Conditional
KL disintegration provides the exact local decomposition,

$$
\operatorname{KL}(Q_{XY}\|P_{XY})
=\operatorname{KL}(Q_X\|P_X)
+\mathbb E_{Q_X}\operatorname{KL}(Q_{Y\mid X}\|P_{Y\mid X}).
$$

In a factor graph with mean-field $q=\prod_iq_i$, the $q_i$-dependent local free-energy term has
the same coordinate variation as the global functional. Summing such local functionals generally
double-counts factors by incidence degree, so equality of coordinate variations is not equality of
full objectives.

On spaces admitting regular conditional probabilities, a joint law may be written
$P(dz,dy)=\mu(dz)K(dy\mid z)$. This makes an observation likelihood representable as an
interaction channel when the same joint law and conditional independences are preserved. It does
not prove that the observed variable is ontologically an agent: different latent environments and
noise kernels can induce the same observed law.

### Exact coarse theory and stochastic channels

For a Markov kernel $C$, the exact coarse law is the pushforward

$$
(C_\#P)(A)=\int C(A\mid z)P(dz).
$$

A coarse action $-\log(dC_\#P/d\mu')$ requires $C_\#P\ll\mu'$ or an explicit singular/extended
convention. An exact contracted functional can instead be defined by

$$
\mathcal F'_C[Q]=\inf_{q:C_\#q=Q}\mathcal F[q],
$$

with an empty feasible set assigned $+\infty$. It is not automatically a KL divergence.

For a deterministic measurable map $T$ on standard Borel spaces, disintegration gives

$$
\inf_{q:T_\#q=Q}\bigl(\operatorname{KL}(q\|P)+c\bigr)
=\operatorname{KL}(Q\|T_\#P)+c
$$

under the stated absolute-continuity and lift-admissibility hypotheses. The analogous
input-constrained identity can be strict for a stochastic channel. An exact stochastic alternative
minimizes the KL of a lifted joint law at fixed coarse marginal over reverse kernels; the posterior
reverse kernel attains the output KL when regular conditionals exist. These are different
optimization problems and must not be conflated.

### Effective interactions, attention, and truncation

Marginalization can generate higher-body, nonlocal, boundary, entropy, Jacobian, memory, or
constraint terms. It does not automatically close on a pairwise attention ansatz. For a
row-stochastic fine interaction matrix $B$ and hard partition matrix $H$, an exact state-independent
coarse Markov matrix $\bar B$ requires the lumpability intertwiner

$$
BH=H\bar B.
$$

Without it, an averaged block interaction depends on the within-block distribution. Attention
weights, energy couplings, and inverse temperatures also obey different normalization rules, so the
semantics of each $\beta_{ij}$ must be fixed before coarse aggregation.

Let $\mathcal A$ be an ambient normed operator space or quotient, $\mathcal T$ a retained ansatz,
$\iota:\mathcal T\to\mathcal A$ an embedding, and $\Pi:\mathcal A\to\mathcal T$ a retraction. The
typed truncation residual is

$$
\epsilon_S=\mathcal R(\iota S)-\iota\Pi\mathcal R(\iota S)\in\mathcal A.
$$

Then $\epsilon_S=0$ for every $S\in\mathcal T$ exactly when
$\mathcal R(\iota\mathcal T)\subseteq\iota\mathcal T$. Outside this closure theorem, the projected
flow is a truncation. Iterating it also needs a stability estimate that controls accumulated
residuals.

### Scale maps, beta data, and invariant objects

Cross-scale maps $C_{\ell\leftarrow n}:X_n\to X_\ell$ for $\ell\le n$ must satisfy

$$
C_{n\leftarrow n}=\operatorname{Id},
\qquad
C_{\ell\leftarrow n}=C_{\ell\leftarrow m}\circ C_{m\leftarrow n}.
$$

They form a contravariant functor from the ordinary scale order, equivalently a covariant functor
from its opposite category. Composition alone does not create a one-parameter semigroup. After
identifying all level spaces, using an additive scale, and imposing translation invariance
$C_{s\leftarrow t}=T_{t-s}$, one obtains $T_{a+b}=T_a\circ T_b$. A driven cocycle instead needs a
base flow and the law

$$
\Phi(t+s,\omega)=\Phi(t,\theta_s\omega)\circ\Phi(s,\omega).
$$

Operators at different scales cannot be subtracted until injective reference identifications place
the compared classes in a common linear or affine space, or the information lost by a noninjective
map is explicitly propagated. For a differentiable, scale-independent coordinate change
$g'=f(g)$, an infinitesimal beta field transforms as

$$
\beta'^a=\frac{\partial f^a}{\partial g^b}\beta^b.
$$

Scale-dependent coordinates add an explicit scale derivative, a change of scale coordinate adds a
Jacobian factor, and finite nonlinear differences use divided differences rather than this formula.
Ordinary zeros and their stability are therefore defined only after declaring a single autonomous
map or flow, modulo explicitly named equivalences. A nonautonomous cocycle generally calls for an
invariant section or another scale-dependent invariant object, although the family can share a
common fixed object as a special case.

## Evaluation status preserved without overclaim

The archived baseline contains forty sanitized final answers, five for each of eight pressure
families. It is a final-answer-only record: raw traces and unsafe runner metadata were excluded. An
earlier manual assessment reported all 240 required/forbidden assertion checks passing, but no
durable per-assertion grading record was retained. The `240/240` count is therefore provisional and
is not a closed benchmark result. The dossier requires a hash-bound paired benchmark before making
an efficacy claim about the skill.

The eight pressure families cover an affirmative false premise, finite checks offered as a
universal proof, missing local--global gluing, interaction-to-ontology overreach, pullback-to-time
overreach, exact-RG truncation overreach, a known constructive theorem, and gauge-fixed expressions
misidentified as invariants. These are evaluation categories, not embedded answers to future
problems.

## Relevance to this research

The protocol gives the gauge-VFE program a reusable research method for ambitious derivations. It
forces exact typing of principal and associated bundles, Fisher pullbacks, ELBO decompositions,
coarse maps, generated operators, scale identifications, and physical bridge principles before an
affirmative construction can be released. The method is synthesized at [[Rigorous theory search]]
and complements the domain curriculum [[Gauge VFE ELBO curriculum]].

The mathematical reconstruction is a methodology audit, not a replacement for the program's
current theorem records. For pullback geometry and timeless inference, use
[[gauge-vfe-rg-pullback-geometry-2026-08-01]]. For local/global VFE and renormalization claims, use
the evidence-bound manuscript and review records linked from [[Gauge-Theoretic Multi-Agent VFE Model]].

## Related

[[Rigorous theory search]] · [[Gauge VFE ELBO curriculum]] · [[Evidence lower bound (ELBO)]] ·
[[Agents as fibre-bundle sections|Agents as fiber-bundle sections]] · [[Fisher information metric]] ·
[[Multi-agent variational free energy]] · [[Renormalization-group flow of beliefs]] ·
[[VFE Transformer Program]] · [[Gauge-Theoretic Multi-Agent VFE Model]]
