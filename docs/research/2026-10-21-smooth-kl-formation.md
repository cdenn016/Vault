# Smooth KL formation with distinct internal laws

The requested target is formation under the original smooth KL/Fisher dynamics, with internally distinct agents and exact inherited parent dynamics, without a Gaussian restriction, imposed synchronization, or an added fusion penalty. The starting Research revision was `4228b26e3ded34c3339e34d14857640f2678665d`. Three bounded constructive rounds produced a general-law closure construction and an engineered first-stage formation example. They do not establish a recursive hierarchy or further compression of the public child states.

The source baseline is the live `manuscripts/MAgent_Theory_2.0/` package, especially Chapters 2, 3, and 5, its authoring contract, the prior `2026-10-21-endogenous-formation.md` record, and the current formation section in `manuscripts/pifb2/13_section.tex`. The retired parent-dynamics and formation chapters were read from Git history to distinguish their conditional approximation claims from exact inheritance. Their old scope was not adopted as a new restriction. The wiki's hierarchy discussion supplied context, including its distinction between collective organization and consensus. No wiki synthesis or index was edited.

## General-law result

The new Chapter 7, `chapters/07_smooth_closure.tex`, derives the exact force after a measurable marginalization. If a fine Fisher flow has score force \(h_Q\), its retained law obeys

\[
\dot\mu=-\mu\bigl(\mathbb E_Q[h_Q\mid C]-\mathbb E_Qh_Q\bigr).
\]

For a local KL, the missing contribution is the entire conditional KL profile over the retained coordinate. An average conditional loss generally does not suffice.

The constructive architecture uses state and model spaces that split into public and private coordinates, a fixed reference \(R_i^c\otimes A_i^q\otimes A_i^s\), and receiver conditional reconstruction. The public evaluator still couples belief and model laws. Peer KL cancels the private conditional exactly on the full admitted law domain. Consequently, differentiating the identity includes incoming source terms and every derivative of the law-dependent channel. No link or receiving conditional is frozen in the variation.

For an arbitrary correlated conditional law \(\kappa_z\), set \(\ell_z=\log(d\kappa_z/dA)\) and retain its reference-weighted distribution \(\xi_z=(\ell_z)_\#A\). The original flow gives

\[
\dot\mu=-\mu[h^c+H-\mathbb E_\mu(h^c+H)],\qquad
\dot\ell_z=H(z)-\ell_z,\qquad
H(z)=\int r e^r\xi_z(dr).
\]

The spectral state is closed. Its exact solution sends \(r\) to \(e^{-t}r-\log\int e^{e^{-t}u}\xi_z^0(du)\). This is an inherited transport equation for a possibly infinite-dimensional law; it is not asserted to be an ordinary Fisher equation on the spectrum distribution. The law-dependent sample statistic is differentiated explicitly. Analytic hypotheses are stated, including dominated regular flows and a bounded-log sufficient condition. No Gaussian, covariance, or finite exponential-family closure is imposed.

Equal spectra across public coordinates make the conditional entropy profile constant, so the public marginals follow the original coarse Fisher dynamics. Different private conditionals can have the same spectrum; product preparation is unnecessary. This includes correlated public/private laws and different laws across agents. The spectral update is invertible at every finite time, so equality of spectra cannot first arise by this relaxation at a finite time.

For private-sensitive records, retain the joint reference law of the log density and every declared readout mark. Record probabilities, posterior normalizers, and the next marked spectrum then have explicit closed formulas. Their composition with the inherited flow preserves finite record-and-feedback histories. Hidden-sensitive records without their marks fail: swapped binary conditionals have identical spectra but record probabilities \(5/8\) and \(3/8\). Joint belief/model conditioning is not silently treated as product recognition. These are exact results for specified interfaces and protocols, not universal sufficiency claims.

## A first-stage smooth erasure construction

Chapter 8, `chapters/08_smooth_erasure.tex`, remains inside the original local KL plus Gibbs-reduced peer-KL potential. It uses four homogeneous agents on an invariant product family of positive three-bit state and model laws. A normalized Ising evaluator couples their public coordinates. Private coordinates affect source preferences. Internal gate-law means relax toward a fixed reference and enter the flat zero region of a prescribed smooth channel function.

The gate is an explicit constitutive mechanism, global in the population's gate means. Its derivative is retained in the full Fisher equation. The proof bounds that derivative and chooses the private gain sufficiently small relative to the transition width, giving finite permanent entry into the erasing region. The function is smooth but nonanalytic. Exact finite erasure depends on the flat region; a merely small positive gate would not give the result.

Two public states lie in each of two invariant sign boxes. Every label assignment is admitted; the dynamics contain no pair labels. Initially crossed private similarities select pairs spanning the sign boxes. After erasure, public similarity selects the within-box pairs, and those source preferences persist. All cross-pair Gibbs weights remain positive. Children chosen distinct initially remain publicly distinct at every finite later time. The proof does not give a separation bounded away from zero as time tends to infinity.

After both gates close, the energy and Fisher metric separate exactly into a public system and independent private/gate relaxations. Before closure, the row normalization has a nonzero mixed public/private derivative. An explicit calculation within the crossed-pair preparation shows that equal public states can have different public forces before closure. The transition therefore creates exact autonomy that was previously absent for that retention.

Each parent retains its size and the empirical measure of paired public belief/model means. That measure has an exact inherited weak evolution under the unchanged public vector field, including incoming source derivatives. It reproduces the declared fresh public boundary protocols, including shared-child joint responses. The private and gate laws are discarded. The empirical public measure itself only removes labels and retains every public child state. Mixture belief/model marginals alone do not close.

This meets a bounded first-stage existence claim with distinct children and discarded private and gate coordinates under the original smooth potential. It supplies the erasing architecture, finite product preparation, and public response class. It does not derive a sufficient interface from generic ungated channels, compress the remaining public child degrees of freedom, preserve later private-sensitive feedback, or generate a second stage. The invariant sign boxes keep the two parents apart.

## Proof development and external context

Round 1 derived conditional mean-force projectability, exact conditional cancellation of peer KL, and positivity of finite-cost source rows. Round 2 constructed the spectral completion and marked feedback, and identified a flat channel gate as a possible finite-entry mechanism. Round 3 completed the smooth gate example, the crossed-preference inequalities, the fixed-private mixed-derivative calculation, and the inherited empirical evolution. The parent reconstructions and the gate's load-bearing inequalities were checked analytically during authoring. No numerical experiment, GPU operation, Lean work, audit panel, or adversarial adjudication ran.

The primary-source context was checked in [Ay, Jost, Lê, and Schwachhöfer, *Information geometry and sufficient statistics*](https://arxiv.org/abs/1207.6736), [Barnett and Seth, *Dynamical independence*](https://arxiv.org/abs/2106.06511), and [Shalizi and Crutchfield, *Computational Mechanics*](https://arxiv.org/abs/cond-mat/9907176). The first supplies the statistical sufficiency/Fisher context; the second explicitly states flow intertwining for deterministic coarse dynamics; the third relates predictive sufficiency to future observation laws. The present conditional-spectrum and erasure constructions are proved locally and are not attributed to those sources. No literature-wide novelty claim is made.

The main manuscript contains the decisive proofs. The companion's new `c08_smooth.tex` explains the conditional force, the spectrum, marked records, and the engineered erasure example. The abstract, outlook, README, and authoring contract distinguish these results from the earlier nonsmooth fusion construction. The supplement is unchanged.

## Remaining obligation

The next substantive target is a collective retention that discards some distinct public child degrees of freedom, with sufficient interfaces and feedback selected by the original dynamics. It must pass the existing equal-retained-state derivative and boundary tests. A recursive result must also produce a subsequent formation stage from the inherited equations. The completed constructions provide neither implication. Repeating the invariant-spectrum preparation, adding another prescribed gate, or renaming the empirical child tuple would not close that gap.

## Document validation

TeX Live 2025 produced the 56-page main manuscript and 26-page companion. Both final logs contain no warnings, missing characters, unresolved references or citations, or overfull/underfull boxes. A source check covered 33 TeX files and found no prohibited spacing macros, trailing whitespace, or missing citation keys. All 82 final pages were rendered with Poppler and inspected in contact sheets; the new spectrum, feedback, erasure, and parent equations were also inspected at readable size. These checks establish build and presentation status, not independent mathematical verification. The supplement was unchanged.
