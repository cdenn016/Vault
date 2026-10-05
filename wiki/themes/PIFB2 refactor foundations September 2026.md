---
type: theme
title: "PIFB2 refactor foundations September 2026"
aliases: ["PIFB2 monograph foundations 2026-09-26"]
tags: [cluster/multi-agent, cluster/vfe, cluster/gauge-theory, cluster/info-geometry, cluster/participatory, project/multi-agent]
status: draft
created: 2026-09-26
updated: 2026-09-26
---

# PIFB2 refactor foundations September 2026

The September 26 refactor treats PIFB2 as a long-form foundational physics monograph and the MultiAgentELBO theory as its mathematical companion. [[dennis-2026-pifb2-refactor-foundations]] records the source snapshot and the conditional derivations. The organizing question is what an explicitly specified normalized probabilistic model and its updates actually produce, with physical interpretations kept separate from algebraic constructions.

## One statistical state and the origin of slow memory

A joint posterior can contain both rapidly changing state beliefs and uncertainty about parameters. This removes the need to treat a model law as an unrelated second kind of probabilistic object. It does not prove that a fast–slow decomposition, representation, or generative family is selected intrinsically. [[friston-2016-active-inference-learning]] already treats state inference and parameter learning as probabilistic updating. [[dacosta-2020-discrete-state-synthesis]] gives an explicit discrete-state formulation with sufficient-statistic learning. The refactor's directly observed Dirichlet example is derived separately, and its shrinking update size is distinguished from a dynamical slow-manifold theorem.

[[friston-2024-supervised-structure-learning]] studies structure selection within supplied candidate families and priors. It therefore helps identify the remaining input rather than eliminate it: a model may learn structure while its admissible alternatives and selection law remain part of the construction. The ordinary VFE, expected free energy, and supplied preference priors have different roles. The geometric slow-manifold route still requires normal hyperbolicity and regularity; [[tikhonov-1952-small-derivative-parameters]] and [[fenichel-1979-geometric-singular-perturbation]] are historical citations, not evidence that every agent configuration satisfies those hypotheses. See [[Generative model]] and [[Geometric singular perturbation theory]].

## Hierarchical structure with explicit grouping

[[friston-2025-pixels-planning]] constructs hierarchical active-inference models by combining state and path variables with spatial grouping, quantization, and temporal blocking. Its Figure 3 and Algorithm 1 support a conditional hierarchy whose slower upper updates follow a prescribed grouping of lower transitions. The latent graph has no shared children, while overlapping weighted image patches can still be used during preprocessing. This architecture is a useful comparison for PIFB2; it does not provide a blanket obstruction to base-manifold overlap or a proof that VFE uniquely selects grouping. The source note records why its informal deterministic-continuous entropy argument in Equation 10 is not adopted as a general theorem.

The refactor also contains an [exact collective slow-mode derivation](../../sources/archives/pifb2-slow-collective-memory-2026-09-26.tex). For a normalized correlated Gaussian target on a connected regular graph, a factorized Gaussian posterior has an invariant covariance slice on which the collective mean relaxes more slowly than internal disagreement. The separation depends on the supplied graph and weak collective restoring curvature. An unrestricted full Gaussian at the same target covariance cancels that separation under natural gradient flow. This gives a conditional one-state memory mechanism and a precise failure case; it does not select the coarse variable or establish agent formation.

## Selective communication and covariance response

A matrix link can discard cognitive directions. For a Gaussian message, a positive noise covariance makes the received law well defined even when the link is rank deficient. The sender's mean stiffness then takes the form $L^TWL$, so directions invisible through the link contribute no stiffness through that edge. This formula belongs to the explicitly declared Gaussian consensus potential, not automatically to every normalized collective VFE. The derivation and scope are recorded in [[dennis-2026-pifb2-refactor-foundations]].

The refactor also separates imitating a distribution from conditioning on a registered observation. Summing several full receiver KL penalties counts receiver entropy several times and can produce a finite relative covariance change even for a very sharp prior. A normalized Gaussian likelihood model can have the same optimal mean but a different covariance response. The replacement does not silently identify those objectives. This sharpens the distinctions already recorded in [[Belief inertia]], [[Mass as Fisher information]], and [[Multi-agent variational free energy]].

## Persistence from hidden coordinates

[[zwanzig-1961-memory-effects]] and [[mori-1965-transport-collective-motion]] provide the statistical-mechanical precedent for memory produced by projection. The refactor independently eliminates hidden coordinates from a stable quadratic gradient system and retains the initial hidden-state contribution, the memory kernel, and a quantitative short-memory bound. The leading instantaneous correction is friction. A scalar second-order rewriting retains real negative poles and a filtered forcing law, so its acceleration coefficient does not establish mechanical mass.

With explicitly supplied Brownian noise and conditional equilibrium preparation, the reduced noise is colored and its covariance is linked to the memory kernel. A stationary Gaussian counterexample shows that matching one-time marginals does not make the retained process Markov. [[bovier-2004-metastability-diffusions]] supplies context for another persistence mechanism, long basin residence at small noise; the monograph derives its own reflected one-dimensional exit-time integral. A supplied barrier, slow parameter, or hidden state is not thereby a derivation of recursive agent formation.

## Full Lorentz algebra and its physical obligations

Complex two-component classical messages have Hermitian second moments. Their two-by-two determinant gives a Lorentz quadratic form, and congruence by SL(2,C) gives the proper orthochronous Lorentz group through its double cover. [[han-1997-stokes-minkowski]] supplies the classical optics precedent; [[simon-2006-hamilton-lorentz]] supplies a related covering-map construction. The latter's sign-of-trace statement requires a causal-domain qualification, which the refactor respects. [[verstraete-2001-local-filtering]] uses related algebra for quantum filtering; its entanglement results are not transferred to classical agents.

The refactor's constructive proofs are recorded in [[dennis-2026-pifb2-refactor-foundations]]. They do not establish that VFE selects this complex representation, a rank-four spacetime readout, an operational time orientation, or causal propagation. A positive Fisher pullback remains Riemannian. Selective channels can preserve positivity while changing determinant nullity, so matrix-valued communication alone does not imply Lorentz dynamics. See [[Emergent spacetime and holography]] and [[Agents as fibre-bundle sections]].

## Reference archive and remaining work

The new primary references have local PDFs except Mori, whose complete 33-page indexed text extraction is archived with an explicit OCR caveat. The existing Friston 2016 primary PDF and immutable source note are reused. The existing Amari 2016 note is retained; [publisher frontmatter](../../sources/pdfs/amari-2016-information-geometry-frontmatter.pdf) is archived, but the complete book was not downloaded. Tikhonov's archived primary metadata is not full text, and direct Fenichel full-text retrieval was denied. Those limitations are preserved in the ingest manifest rather than treated as successful full-paper downloads.

The next discriminating work is an explicit normalized model selecting the required collective observables and their response law. For persistence, compute its retained response kernel under a specified perturbation. For physical Lorentz geometry, derive the representation/readout selection and show that propagation characteristics match the proposed cone. The present refactor gives conditional constructions and precise remaining obligations; it does not establish emergent matter or spacetime.


## Inherited-reference coverage

The [dated citation census](../../sources/archives/pifb2-citation-coverage-2026-09-26.json) maps all 61 cited keys in the recorded staged revision to source notes and available primary text. Thirteen previously missing inherited article PDFs were recovered. Complete archives, local author manuscripts, metadata-only records, and unresolved full-text gaps remain distinct. The earlier four-module ZIP remains a prefinal source snapshot; it is not the final installed PIFB2 manuscript. Inherited references with bibliographic records only include [[abbott-1981-background-field-beyond-one-loop]], [[dewitt-1967-manifestly-covariant-gravity]], [[kikuchi-1951-cooperative-phenomena]], [[salamon-berry-1983-thermodynamic-length]], [[milgrom-segal-2002-envelope-theorems]], [[lauritzen-1996-graphical-models]], [[hansen-ghrist-2021-discourse-sheaves]], [[lawson-lim-2001-geometric-mean]], [[nussbaum-1988-projective-metric]], [[vandergraft-1968-invariant-cones]] and [[wheeler-1983-law-without-law]].

Two openly supplied books close further archive gaps: the [complete Bishop 2006 PDF](../../sources/pdfs/Bishop2006.pdf) comes from Microsoft Research; the [complete Absil publisher text](../../sources/archives/absil-2008-complete-publisher-text.zip) contains sixteen publisher PDFs with provenance and preserves its September 2007 prepublication date. Existing [[bishop-2006-pattern-recognition-machine-learning]] and [[absil-2008-optimization-matrix-manifolds]] notes are reused unchanged. The final 62 key census now has 40 PDFs, the Absil chapter set, Mori text, four local author sources, and 16 remaining full-text gaps. Parr 2022 is openly licensed, but its publisher endpoint was inaccessible in this session; it is not described as paywalled.

## Final delivered monograph

The [live 115-page monograph](../../manuscripts/PIFB2.pdf) and [modular source entrypoint](../../manuscripts/PIFB2.tex) are installed. The [final source and PDF archive](../../sources/archives/pifb2-refactor-final-2026-09-26.zip) and [hash manifest](../../sources/archives/pifb2-refactor-final-2026-09-26-manifest.json) identify this delivery separately from the prefinal four-module snapshot. Compilation and reference checks pass; the detailed mathematical qualifications and open physical obligations remain part of the text. Full source coverage is the 62-key census above, including its 16 recorded full-text gaps.
