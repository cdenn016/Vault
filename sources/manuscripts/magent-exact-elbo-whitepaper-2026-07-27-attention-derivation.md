---
type: manuscript
title: "MAgent Exact-ELBO White Paper: 2026-07-27 Attention-Row Derivation Record"
aliases:
  - "MAgent exact ELBO attention derivation"
  - "Source-label augmented model"
  - "Tempered source row"
authors:
  - Robert C. Dennis
year: 2026
status: in preparation
tags:
  - cluster/vfe
  - cluster/multi-agent
  - cluster/attention
  - cluster/gauge-theory
  - cluster/info-geometry
  - project/multi-agent
  - project/transformer
  - field/mathematics
  - field/statistics
  - field/cs-ml
created: 2026-07-27
updated: 2026-07-27
---

# MAgent Exact-ELBO White Paper: 2026-07-27 Attention-Row Derivation Record

## Scope and immutable provenance

This immutable record binds the attention-row derivation added to
`manuscripts/MAgent_exact_elbo_whitepaper.tex` to Research commit
`34f1a6c107c5a6937cd9b050c6474cf0bd79ccc5`, relative to the baseline
`24cd5e6`. The chapter subtree `manuscripts/magent_elbo_whitepaper` is
`84c823ce89bf8be72216827f98adba122331c5cc`. The three edited subfiles have Git blobs
`039f4111e4fa6983573ae3905ea2a5d478eadc88` (`06_mean_field_theory.tex`),
`681eafe12aaeeca50761b42b16a6cc67f162171b` (`09_pifb2_crosswalk.tex`), and
`027636453130a8863e7a95dbc47ac78c28ee9f5d` (`13_appendices.tex`). The document compiles at
112 pages with zero errors and zero undefined references.

The supporting oracle and claim ledger live in the MAgent repository at commit
`0714173`, as `verification/b0_attention_derivation.py` and
`verification/build_b0_ledger.py`. Earlier immutable records, including
[[magent-exact-elbo-whitepaper-2026-07-19-continuum-finite-remediation]] and
[[vfe-population-generative-status-2026-07-12]], remain unchanged.

## What question this answers

Under the author's stated document hierarchy, the exact-ELBO white paper is the foundation and
[[participatory-it-from-bit|PIFB2]] is the target, so the program asks whether the white paper
GENERATES PIFB2's structures rather than merely classifying them. The first target is the attention
rule

$$\beta_{ij}=\operatorname{softmax}_j\left(-\tfrac1\tau\KL\left(q_i\Vert\Omega_{ij}q_j\right)\right).$$

Before this record the white paper classified that row as an engineered scalar. Its own fixed-source
row model is exact only for frozen normalized templates and only at unit temperature, and it stated
that a row-local construction does not by itself define a normalized population joint when the state
variables are shared. Chapter 9 named a genuine exception, that a fixed normalized model carrying a
declared source label can have an exact ELBO once compatibility and global normalization are proved,
but did not carry it out. This record carries it out.

## Result 1: the temperature is not free

The tempered component is $f_{ij}^{(\tau)}=f_{ij}^{1/\tau}/Z_{ij}(\tau)$. For any densities,

$$\KL\left(\varrho_i\Vert f_{ij}^{(\tau)}\right)=\tfrac1\tau\KL(\varrho_i\Vert f_{ij})+\left(\tfrac1\tau-1\right)H(\varrho_i)+\log Z_{ij}(\tau),$$

whose middle term is source-free and cancels under row normalization. The normalizer does not cancel.
In the Gaussian regime $f_{ij}^{(\tau)}=\mathcal N(m_{ij},\tau S_{ij})$ and the only source-dependent
part of $\log Z_{ij}(\tau)$ is $\tfrac12(1-1/\tau)\log\det S_{ij}$, so the exact tempered row is

$$\beta_{ij}^{\star(\tau)}\propto\pi_{ij}\exp\left[-\tfrac1\tau\KL(\varrho_i\Vert f_{ij})-\tfrac12\left(1-\tfrac1\tau\right)\log\det S_{ij}\right].$$

With $S_{ij}=\Omega_{ij}\Sigma_j\Omega_{ij}^\top$ the extra logit reads
$\log\det\Sigma_j+2\log\lvert\det\Omega_{ij}\rvert$. It vanishes only at $\tau=1$, or when
$\det S_{ij}$ is source-free, or when the declared prior absorbs the normalizer. For $\tau>1$ its
coefficient is positive, so the exact model discounts sources whose transported belief occupies more
volume, beyond what the divergence records. Measured row separation at the executable's operating
point $\tau=\sqrt7$ is **0.069** in total variation, and exactly $0$ at $\tau=1$.

The transport enters only through $\lvert\det\Omega_{ij}\rvert$, which the $f$-divergence invariance
theorem cancels inside the divergence itself, so this term is a property of the tempering and not a
violation of that invariance.

## Result 2: with a source label, the live-peer obstruction narrows to one tied parameter

Adjoin a label $j_i\in\mathcal J_i$ per agent with $p(J)=\prod_i\pi_{ij_i}$ and link factors
$p(y_i\mid y_{j_i},j_i)=\mathcal N(y_i;\Omega_{ij_i}y_{j_i},R_{ij_i})$. Under a mean-field family
$\prod_i q_i\prod_i\beta_i$, the exact CAVI coordinate for $\beta_i$ is
$\beta_{ij}^\star\propto\pi_{ij}\exp(-E_{ij})$ with

$$E_{ij}=\tfrac12\left[d\log2\pi+\log\det R_{ij}+\Delta_{ij}^\top R_{ij}^{-1}\Delta_{ij}+\operatorname{tr}\left(R_{ij}^{-1}\Sigma_i\right)+\operatorname{tr}\left(R_{ij}^{-1}S_{ij}\right)\right].$$

Tying $R_{ij}=S_{ij}$ gives
$E_{ij}-\KL(q_i\Vert(\Omega_{ij})_\#q_j)=\tfrac d2\log2\pi+\tfrac12\log\det\Sigma_i+d$, which carries
no source index, so the normalized rows coincide and PIFB2's unit-temperature row IS the exact label
coordinate.

The scope needs stating precisely, because "live peers" overstates it. The sender MEAN is free
throughout and is never replaced by a template, which is strictly weaker than the frozen-source
hypothesis. The sender COVARIANCE is not equally free, because the tie constrains a generative
parameter to agree with $\Sigma_j$. Within one coordinate update the model is fixed and the row is
exact; refreshing $R_{ij}$ to follow a moved $\Sigma_j$ changes the model between updates, which is
the same caution the white paper already raises against refreshing $f_{ij}$. So the obstruction is
narrowed to the covariance channel, not removed. Untied, the edge energy is a Mahalanobis term in the
model's own link metric plus separate dispersion penalties on receiver and pushforward sender; the
tied case is its specialization. Measured: untying moves the row by up to **0.99992**, so the tie is
substantive rather than cosmetic.

## Result 3: global normalization forces an ordered mask, and the cocycle is why

Every assignment giving each agent exactly one parent has a cycle, by iterating the parent map on a
finite set, so the unrestricted product is never a directed factorization. Exhaustive enumeration
finds $0$ acyclic maps of $46656$ at $N=6$.

The failure is not an unknown constant. Under a cocycle transport $\Omega_{ij}=U_iU_j^{-1}$, so that
$\Omega_{ji}=\Omega_{ij}^{-1}$, the assembled precision of a reciprocal pair is SINGULAR for every SPD
link covariance: the vector $(v,\Omega_{ij}^{-1}v)$ is in its kernel for all $v$. Both link factors
express the same linear agreement relation, so the joint is flat along the gauge-consistent ray and
has infinite mass. In one dimension the assembled determinant is $(ab-1)^2/r^2$ and the pair mass is
$\lvert ab-1\rvert^{-1}$, which diverges exactly at $ab=1$, the cocycle case.

Restricting the source sets so the parent relation admits a topological order, of which a causal mask
is the canonical instance, makes every label configuration a genuine directed factorization with
partition function one identically; verified across $368$ label configurations with
$\lvert\log Z\rvert\le3.2\times10^{-14}$. Excluding only the self edge is insufficient, since
two-cycles survive it.

Adjoining a proper self-prior instead restores positive definiteness but yields an undirected
specification whose partition function depends on the label configuration, so $-\log Z(J)$ enters the
label objective and does not separate across receivers. Measured spread of $\log Z(J)$ reached
**1.76 nats** at $N=3$, so the coupling is not negligible; in that route the row is exact only under a
further declared approximation.

## Result 4: the self term is a slot in the same row

A distinguished label value with $p(y_i\mid j_i=\varnothing)=p_i(y_i)$ keeps the model in the same
class and contributes $-\E_{q_i}[\log p_i]=\KL(q_i\Vert p_i)+H(q_i)$. A self term and the source terms
are therefore competing slots of one simplex, and moving a self term inside costs exactly one receiver
entropy. This reaches the same entropy bookkeeping recorded for the observation coupling from the
generative side rather than by direct computation.

## Verdict and what is not claimed

The attention target is graded DERIVABLE UNDER STATED EXTRA HYPOTHESES. The hypotheses are a declared
source-label auxiliary coordinate, an ordered source mask, the tie
$R_{ij}=\Omega_{ij}\Sigma_j\Omega_{ij}^\top$, and either unit temperature or the tempered model with
its normalizer. The exact-ELBO theory does not itself select three of the four.

The construction enlarges the latent inventory, so it is exactly the case Chapter 9 exempts and does
NOT contradict the finite-design moving-peer obstruction, which is scoped to a fixed joint on the
original shared agent-state variables. No claim is made that PIFB2's complete population functional is
the negative ELBO of any single joint; only the attention row is addressed. The coarse-graining and
the tower, the other two derivation targets, are untouched.

> [!note] Editorial: the open question is whether the tie can be justified from within the theory,
> discharged as an M-step fixed point, or must stand as a declared postulate. The supporting claim
> ledger records the overall verdict as INCONCLUSIVE for exactly this reason, with four component
> claims closed as EVIDENCE_VERIFIED.

## Relevance to this research

This is the first of the three derivation targets to be settled, and it converts the program's central
attention rule from a posited scoring function into an exact variational coordinate of a declared
normalized model, at a stated and bounded cost. Two consequences propagate. The mask requirement is
comfortable for the causal transformer and uncomfortable for the multi-agent setting, where the source
relation is bidirectional by design. The temperature logit is a concrete, measurable divergence
between the exact construction and what the executable computes, and is therefore testable rather than
merely formal.

## Related

[[GL(K) gauge-equivariant attention]] · [[Evidence lower bound (ELBO)]] ·
[[Mean-Field Approximation]] · [[Multi-agent variational free energy]] · [[Softmax]] ·
[[Variational free energy]] · [[Gauge-Theoretic Multi-Agent VFE Model]] · [[Belief coupling]] ·
[[Precision weighting]] · [[Attention Mechanism]] · [[Lattice gauge theory]]

## Sources

[[magent-exact-elbo-whitepaper-2026-07-19-continuum-finite-remediation]] ·
[[participatory-it-from-bit]] · [[gl-k-attention]] · [[vfe-population-generative-status-2026-07-12]] ·
[[bishop-2006-pattern-recognition-machine-learning]] ·
[[cover-thomas-2006-elements-information-theory]]

The manuscript additionally cites, without dedicated source notes in this vault, Lauritzen's
*Graphical Models* (1996) for the directed-factorization normalization and Bissiri, Holmes and Walker
(2016) for the normalized power-likelihood construction. Both already appear in
`manuscripts/references.bib` as `Lauritzen1996` and `BissiriHolmesWalker2016`.
