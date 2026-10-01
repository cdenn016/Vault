---
type: manuscript
title: "MultiAgentELBO spin-foam methods review, theory integration, and Fable adjudication, September 30, 2026"
aliases: ["Spin-foam boundary methods review September 2026", "MultiAgentELBO September 30 spin-foam integration"]
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, cluster/info-geometry, project/multi-agent, field/mathematics, field/statistics, field/physics]
created: 2026-09-30
---

# MultiAgentELBO spin-foam methods review, theory integration, and Fable adjudication

## Source record

This records the local review `C:/Users/chris and christine/Desktop/MultiAgentELBO/docs/reviews/2026-09-30-spin-foam-theory-integration/`: the synthesis `REPORT.md` with its appended adjudication section, eight investigator reports (`01-` to `08-`), three integration records (`integration/W-c09.md`, `W-c10.md`, `W-c11.md`), ten adjudication records (`adjudication/`), and copies of every executed check (`evidence/`). The object reviewed is [[dennis-2026-spin-foam-boundary-methods]] and its derivation record, written in a Codex run by GPT models (authors dispatched as gpt-6.1-sol, checker gpt-6-astra). Investigators, integration writers, and the synthesis were Claude Opus 5.5; all verification roles were Claude Fable 5.1. The review files were not committed to Git at the time of this note.

## Review verdicts

The companion's mathematics is correct wherever it was reconstructed, and no false statement was found. Eleven of its 29 theorem-type statements restate labeled theory results without citing them, and by the literature count 24 of 29 are direct applications of classical results (sufficiency, the relative-entropy chain rule, Hoeffding's lemma, filter stability). Every quantitative bound is vacuous for the program's executed classes: a bounded log-residual forces a Gaussian approximation to be exact, OU and sheet-diffusion kernels have Dobrushin coefficient one, and global mixing coefficients tend to one with agent count for product-like kernels. The work strengthens the RG theory narrowly, strengthens the 512-agent experiments only by formalizing a chain rule they already use, and meets no settling condition of any open-problem table. The spin-foam framing is inferentially inert; the authors' own independent check says that removing it leaves the calculations unchanged.

## Integrated statements (all EVIDENCE_VERIFIED by Fable panels)

Four statements were rewritten into the MultiAgentELBO theory under its SPEC, with proofs, as ESTABLISHED. `thm:rg-memory-borel-projection` (Chapter 11) extends the finite-alphabet memory projection to standard Borel records and arbitrary Borel history statistics: path relative entropy equals the summed conditional information plus the summed expected row divergence, in $[0,+\infty]$ with no dominance or finiteness hypothesis; the source rows attain the minimum. `cor:rg-perturbation-divergence-bounds` (Chapter 11) bounds both directed relative entropies of a bounded action perturbation of range $\omega$ by $\min\{\omega,\omega^2/8\}$, keeps evidence and complete-VFE offsets separate from posterior error, and propagates essential bounds additively along a tower, all confined to the bounded tier. `prop:rg-forest-tree-composition` (Chapter 10) shows that tree transports compose across depths when each parent's depth-zero tree is the union of its children's trees and a depth-one tree of dressed links, which supplies the composition hypothesis of `prop:rg-linear-cross-scale`(ii) for any group. `prop:cg-descent-common-recovery` (Chapter 9) shows that one Markov kernel recovers a whole dominated family exactly when every likelihood ratio descends, with no finite-divergence hypothesis. Primary-source locators for their classical counterparts remain unchecked, so none is STANDARD yet.

## Adjudicated investigator-derived results

The contracted residual tower is verified: $\log(1+\delta(e^w-1))$ is the exact one-step supremum for Dobrushin coefficient $\delta$ and residual range $w$, and the Birkhoff form $\tanh(\Delta/4)w$ needs finite projective diameter. The Gaussian exterior-informed interface is verified: the optimal rank-$r$ linear boundary statistic keeps the top canonical directions and discards exactly $-\tfrac12\sum_{a>r}\log(1-\rho_a^2)$. The non-tensorization factor of interval budgets is exactly $\min\{N,8/w\}(1+O(w^2))$, up to $N$ rather than of order $N$. The regulator's Gibbs-variational form is verified. The quadratic-residual tier is verified mathematically but inconclusive in the claim that it fills the gap `rem:rg-bounded-tier-scope` names. In the stabilizer results, one clause ("every metric projection breaks a noncompact stabilizer") is refuted by a checked counterexample, while the compactness, genericity, and unitary-representation parts stand.

## Decisions recorded in the same session

The user decided that locality at $c_*$ is carried by the source prior: sparse, possibly directed supports and priors decaying with a declared distance on the agent set (graph distance by default, ALiBi-type and power-law profiles), with hard masks as the rigorous tier because a soft prior bounds attention only up to $e^{\Delta/\tau}$. One-way attention is intended, as when a follower attends to a celebrity who does not attend back. The theory now reads the interaction multigraph as containing the reversal closure of the row supports. Joint descent of the collective free energy stays the default dynamics, so a non-attending source still feels the sender term of every row that attends to it; per-agent descent is an opt-in variant.

## Relevance to this research

Updates [[Spin foam coarse-graining for agent networks]], [[Coarse Graining]], and [[Gauge-Theoretic Multi-Agent VFE Model]]. The locality decision bears on [[Graphon limits of agent networks]] and on the network families discussed in [[Network structure — small-world and scale-free]].
