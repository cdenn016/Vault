---
type: theme
title: "Staged hierarchy formation and RG composability"
aliases:
  - "staged assembly"
  - "typed cocycle RG"
  - "composability of coarse-graining"
tags:
  - cluster/multi-agent
  - cluster/social-physics
  - project/multi-agent
  - project/social-physics
status: draft
created: 2026-08-17
updated: 2026-08-17
---

# Staged hierarchy formation and RG composability

Two literatures meet at one question the multi-agent program can now measure: does it matter in
what stages a hierarchy is built? The kinetic literature says the *path* matters for what forms;
the renormalization literature says the *description* of the aggregate depends on the path taken
to coarse-grain it. On 2026-08-17 the MultiAgentELBO finite laboratory measured both halves of
this on its own declared system, and this page records the synthesis.

## The kinetic strand: hierarchies are built in stages

[[simon-1962-architecture-complexity]] is the founding argument: assembly through stable
subassemblies (the watchmakers parable) is overwhelmingly faster than all-at-once assembly, so
the complex systems that exist are nearly-decomposable hierarchies built stagewise.
[[maynard-smith-1995-major-transitions]] is the same claim as evolutionary history: every major
transition formed higher-level units from previously stabilized lower-level units, never de
novo. Empirically, [[palla-2007-social-group-evolution]] finds real social groups growing by
gradual accretion, with small groups persisting through stable cores and large ones through
turnover, and [[zhou-2005-discrete-hierarchy-group-sizes]] finds human group sizes layered in a
geometric hierarchy with preferred branching ratio near three. The physics prototype of staged
growth is binary-merger kinetics, [[smoluchowski-1916-coagulation]]; and
[[mengistu-2016-evolutionary-origins-hierarchy]] adds the causal simulation result that
hierarchy emerges from *connection costs* — pricing structure is what produces it.

## The composability strand: coarse-graining is path-dependent

Exact composability of real-space RG maps is the exception. It holds for pure decimation, which
is marginalization and composes trivially; asymptotically at fixed points, where the couplings
outside the retained family have died; and on the hierarchical lattices of
[[berker-1979-hierarchical-lattice-rg]] and [[kadanoff-1976-migdal-recursion]], which compose
exactly because the substrate is built self-similarly, one recursion step undoing one
construction step. Away from these cases, [[griffiths-1979-rg-transformations]] and
[[van-enter-1993-rg-pathologies]] show real-space maps can fail even to produce well-defined
theories of the declared type. The probabilistic cousin is
[[kemeny-snell-1960-finite-markov-chains]]: lumpability of a Markov chain is an exceptional
condition, and generic coarse-grainings of generic chains are not Markov in the lumped states.

## What the laboratory measured (2026-08-17)

The finite categorical laboratory's rescaling map (design and amendments in
`MultiAgentELBO/docs/superpowers/specs/2026-08-17-rescaling-map-design.md`) made this concrete
on the declared two-channel gauge system:

- **C3, compatibility, refuted.** Blocking six agents at once versus in stages disagrees by
  $0.204$ in sup norm against a pre-registered $10^{-10}$ criterion, with a provably lossless
  intermediate projection — the defect is the Bayes kernel composition itself. The flow is a
  **typed cocycle**, not an autonomous semigroup, and the composition defect is order one
  ($0.12$–$0.19$) at every accessible depth, including the $2{\times}3$ versus $3{\times}2$
  panel on a homogeneous 6-cycle.
- **Per-ratio fixed structures exist and are factorized.** Each declared ratio's reduced
  self-map (blocking plus self-similar re-tiling) is a measured local contraction (spectral
  radius $\approx 0.78$–$0.83$) onto a fixed structure whose pairwise block is machine zero —
  the factorized subspace is provably invariant (the block-local Bayes kernel sends factorized
  theories to factorized theories) and measured attracting, with pair-sector eigenvalues near
  $0.17$.
- **Even the endpoints are typed.** The ratio-two and ratio-three fixed structures differ by
  $0.81$ relative sup: pairs-first and triples-first aggregation settle into different
  equilibrium potentials.
- **The triviality is architectural.** Single-boundary-agent towers are quasi-one-dimensional
  (Perron–Frobenius transfer-matrix argument on rings), so decoupled fixed structures are the
  expected 1D outcome; hierarchical lattices show that boundary multiplicity — bundles of
  parallel cross-links per coarse edge — is what sustains interacting fixed structures. For a
  directed $\beta_{ij}$ agent network, the lattice question "in what dimension does interaction
  survive" becomes "**which architectures renormalize to interacting fixed structures**".

## The 2026-08-18 reversal: regeneration restores interaction, typing survives

> [!warning] Verification status: everything in this section and below is tentative.
> The entire 2026-08-17/18 rescaling-laboratory chain (regeneration, the capacity reversal,
> M-info, M-part, M-bind, M-anchor, M-flow, M-cross-env, M-share) is a single-implementation
> body of findings: numbers were reproduced and cross-checked inside the MultiAgentELBO
> codebase, but no independent implementation, external replication, cross-model
> verification, or verification-ledger closure exists. Treat the verdicts as tentative; the
> only claims exempt are the actual theorems (e.g. $R_{\mathrm{MI}} \le 1$ by data
> processing), whose *measured values* remain tentative all the same.

The follow-up measurements (amendments 3–8 of the design) bounded the triviality result to the
**passive channel** — coupling inherited through blocking with attention frozen — and reversed
the headline. Structural rescues leave the passive channel below one: one-step pair retention
grows sublinearly with boundary multiplicity ($0.156$, $0.441$, $0.564$ at $k = 1, 3, 6$ cut
couplings per block boundary) and saturates below one, while the smallest sector enlargement of
the parent alphabet (the block's belief-channel $Z_3$ charge, the singlet/triplet reading of
marks, root-framed through the spanning-tree transport) **raises** retention without crossing
one — $0.209$ against $0.156$ at $k = 1$, $0.568$ against $0.441$ at $k = 3$, constant-sector
control exact. The 2026-08-17 capacity null ($0.144$/$0.406$) was a frame artifact: the
original charge was referenced to the first family member and shifted under the sample-shift
gauge, and the 2026-08-18 audit retired it
([[2026-08-18-rescaling-audit-capacity-reversal]]) — a measurement failing the covariance
discipline the theory imposes on everything else. What
restores interaction is the theory's own **re-binding rule**: regenerating each level's
attention from the flow-averaged transported divergence over the conserved connection
($\beta \propto e^{-\overline D/\tau}$) and folding the alignment energy into the coarse
action. Under that rule — itself gauge covariant to $10^{-11}$ — the per-ratio composites
converge to interacting fixed structures (pairwise sup $0.579$ at ratio two, $0.625$ at ratio
three, each about a quarter above its own one-step injection), so horizontal glue in a tall
hierarchy is actively re-established per level from the two objects blocking conserves, the
connection and the coarse beliefs, rather than inherited. Regeneration does not restore
composability: defects stay order one across factorizations ($0.17$–$0.27$) and the interacting
fixed structures remain ratio-typed ($0.64$ relative sup). The staged-assembly moral
strengthens: which aggregation grain a hierarchy uses matters in both channels, all the way to
the endpoints.

The same day's M-info measurement (amendment 9,
[[2026-08-18-minfo-information-retention]]) put the retention story in law units: boundary
mutual-information retention is bounded by one as a data-processing theorem, measures 2–7% at
the declared seed against sup-norm readings of 0.156–0.568, and deflates the sector gain to
+10%/+5% (mostly anchored-coordinate inflation in the sup norm). The sharp reading:
**regeneration restores interaction without restoring information** — the rebuilt glue is
synthesized per level from the conserved connection and coarse beliefs, while microscale
boundary information dies at roughly $t^2 \approx 2\%$ per step
([[Data processing inequality]]). Hierarchies of this kind keep structure all the way up and information only
locally, which is the composability strand's path-dependence stated in a second instrument.

M-part (amendment 10, [[2026-08-18-mpart-participatory-blocking]]) then asked the staged-vs-direct
question inside the theory's own selection mechanism: the Proposition-4 partition posterior,
flow-averaged to the level and offered every cycle blocking, puts its modal mass on the
*singleton* partition (0.586) at the declared seed — no aggregation is favored, direct collapse
outranks staged among the aggregates, and the pair-free null control sits within 1% of the
coupled posteriors. The formation-kinetics hypothesis is unsupported at this seed in its
free-energy form, for the same reason M-info found: nothing to bind. The open split that
survives is sharper than the original question: free-energy preference at full sight (measured,
negative here) versus proposability under bounded sight — a depth-limited agent cannot propose
a block beyond its sight radius, so bounded visibility forces staged aggregation kinetically
regardless of the full-sight ranking, and hierarchy is what extends sight (a level-$\ell$
parent with depth-1 coarse sight commands depth-$r^\ell$ fine structure, and carries its
block's interior [[Holonomy]] as marks).

The follow-ups ran the same day and closed the story with scopes attached. M-bind
([[2026-08-18-mbind-coupling-sweep]]) swept the coupling four decades and found no formation
transition — the singleton preference is structural, not weak-coupling, and the blocking
channel is kernel-limited (the $t \approx 0.15$ transmission does not adapt to signal). The
resolution came from the agent-only ontology: observations are couplings to environmental
agents, and the lab had been integrating those agents out after level zero. Restoring the
environment as a blockable class ([[2026-08-18-environmental-blocking]]) licenses binding on
clean controls — uniform anchors flip the modal class to direct collapse, distinct anchors
anti-bind, shared-pair anchors pull the *anchor-aligned placement* eightfold — and running the
theory as a process (joint annealed dynamics on states and partition) reverses the quenched
verdict even on the bare instance. **Condensation follows shared evidence, not mutual
attraction**, and the formation negatives of M-part/M-bind stand as true statements about the
quenched update on environment-free levels. The staged-assembly question is now live rather
than refuted: the annealed process favors aggregation, bounded sight forces it to be staged,
and the anchor-sharing pattern selects which blocks form.

The last measurement of the arc ([[2026-08-18-mshare-finite-inertia]]) sharpened the
shared-evidence mechanism itself: a point-mass environment aligns but cannot correlate (the
per-site field factorizes), and finite-inertia shared agents — integrated out exactly — do
carry the correlation channel (ninefold over private duplicates at zero inertia) yet never
beat pure alignment for the aligned-placement statistic at this seed. Alignment and
correlation are competing channels, not composing ones; in the
[[Mass as Fisher information|mass-as-Fisher-information]] language, evidence with infinite
mass is a frame, not a bond, and evidence light enough to move anchors nothing. The formation
barrier that survives every instrument of the week is the derived energy's width penalty,
which points at the level-invariant kernel family itself. The chain is rendered as a
reviewable figure suite in the repository (`figures/rescaling-lab/`, seven figures with
captions, regenerated live from the validated seed).

## The synthesis

The two strands are one phenomenon seen from two sides. Because coarse descriptions are
path-dependent (composability strand, C3), *which* aggregation path a system takes is physically
meaningful — and the kinetic strand says real systems take staged paths. The program's own
version of the question is now internal: the partition posterior assigns free energies to
blockings, so whether staged aggregation is free-energy-favored over direct aggregation is a
measurement, not an imported analogy. The externally calibrating lesson runs the other way too:
`Theory/07b`'s autonomous-semigroup claim was stronger than standard RG lore warrants, since
even classical real-space RG composes only at fixed points or on self-similar substrates, and
the laboratory correctly caught that.

> [!note] Editorial: as a formal home for staged, typed composition — maps composing only along
> a tower of levels, with typed slots — operads are the standard algebraic structure (May's
> *Geometry of Iterated Loop Spaces*, 1972); this is a pointer, not yet a used tool, and the
> citation has not been verified against the primary source.

> [!note] Editorial: the 1D triviality argument (Perron–Frobenius uniqueness of the transfer
> matrix's top eigenvalue for strictly positive finite-range weights, hence no phase transition
> on rings) is textbook material asserted from memory; it should be pinned to a standard text
> before entering a manuscript.

## Open measurements this frames

Whether the composition defect contracts under iteration on deeper flows (asymptotic semigroup)
or persists (irreducibly typed); the pair-sector contraction rate as a function of boundary
multiplicity in bundled towers, whose crossing of one would be the architecture analog of a
lower critical dimension; and the staged-versus-direct free-energy comparison under the
partition posterior — the model's own "nine humans do not suddenly form a gang".

## See also

- [[Renormalization group flow]] · [[Renormalization-group flow of beliefs]]
- [[Meta-agents and hierarchical emergence]] · [[Coarse Graining]]
- [[Ouroboros multi-scale dynamics]]
- [[garuccio-2023-multiscale-network-renormalization]] — closure relative to a declared family
  and aggregation protocol, the network-science form of the same lesson
- [[csiszar-1975-i-divergence-geometry]] — the I-projection theorem behind the laboratory's
  variational coupling read-back
- [[Gauge-Theoretic Multi-Agent VFE Model]]
