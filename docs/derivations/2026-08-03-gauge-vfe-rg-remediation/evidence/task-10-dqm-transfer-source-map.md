# Task 10 — DQM transfer source map

## Claim closed by this record

For a normalized parameter-independent Markov kernel \(K\), the image of a
common-dominated DQM experiment is DQM and its directional score is the
conditional expectation of the fine directional score.  Consequently its
Fisher information is no larger, with equality exactly when the fine score is
measurable with respect to the output statistic.

This record closes the external-source provenance of the DQM-transfer
conclusion used by `bundle-fisher-defect`.  `H-DQM-TRANSFER` records only the
applicability hypotheses.  This record does not replace the manuscript's
separately declared bundle hypotheses for jointly measurable,
parameter-smooth conditional-score versions.

## Primary source

- David Pollard, "A note on insufficiency and the preservation of Fisher
  information," *IMS Collections* **9** (2013), 266–275, Theorem 3.
- DOI: [10.1214/12-IMSCOLL919](https://doi.org/10.1214/12-IMSCOLL919).
- Preprint: [arXiv:1107.3797](https://arxiv.org/abs/1107.3797).

Pollard's Theorem 3 gives the DQM score of a statistic as the conditional
expectation of the original score and characterizes Fisher equality by
statistic-measurability of that score.

## Exact reduction to Pollard's statistic theorem

Let \(P_\theta\) be the fine experiment on \(\mathsf X\), dominated by a fixed
\(\sigma\)-finite \(\mu\) with selected density version \(p_\theta\), and let
\(K(x,\mathrm dy)\) be a normalized kernel independent of \(\theta\).  Form the
joint experiment

\[
 J_\theta(\mathrm dx,\mathrm dy)=P_\theta(\mathrm dx)K(x,\mathrm dy),
 \qquad
 \nu(\mathrm dx,\mathrm dy)=\mu(\mathrm dx)K(x,\mathrm dy).
\]

Then \(\nu\) is \(\sigma\)-finite: for a \(\mu\)-finite exhaustion
\(\mathsf X_n\), normalization gives
\(\nu(\mathsf X_n\times\mathsf Y)=\mu(\mathsf X_n)\).  Moreover
\(\mathrm dJ_\theta/\mathrm d\nu=p_\theta(x)\).  Hence the DQM remainder
for \(J_\theta\) has exactly the same squared \(L^2(\nu)\) norm as the DQM
remainder for \(P_\theta\).  Apply Pollard's Theorem 3 to the deterministic
statistic \(T(x,y)=y\).  Its image experiment is precisely \(P_\theta K\), and
for a fine directional score \(\ell_w(X)\) its DQM score is

\[
 \bar\ell_w(Y)=\mathbb E_{J_\theta}[\ell_w(X)\mid Y].
\]

The variance decomposition yields

\[
 I_{P_\theta}(w,w)-I_{P_\theta K}(w,w)
 =\mathbb E_{J_\theta}\operatorname{Var}(\ell_w(X)\mid Y)\geq0,
\]

with equality exactly under the source's statistic-measurability condition.

## Scope boundary

Common domination above is sufficient for the Task 10 transfer.  This record
does not claim a broader nondominated version, so no singular-part lift is
needed here.  The Hellinger data-processing inequality is useful corroboration
of contraction, but by itself does not identify the DQM score or prove the
equality characterization.  The manuscript's pointwise geometric use also
retains separate hypotheses selecting jointly measurable, parameter-smooth
conditional-score versions and a smooth bundle-level vertical differential.
