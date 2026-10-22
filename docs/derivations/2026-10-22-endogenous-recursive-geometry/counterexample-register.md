<!-- rigorous-theory-search-metadata {"schema_version":"rigorous-theory-search/v1","contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->
# Failure tests and counterexamples

No counterexample to the scoped existential construction was found in the bounded three-round investigation. The following proved failures prevent its extension beyond its assumptions.

Discarded contextual model-shape variation destroys geometric equality. Change two model shapes in opposite contextual directions while holding their sum and precisions fixed. The fine centered log-determinant difference has positive variance and is orthogonal to conjugation orbits; the parent tangent is zero. Hence the fine residual metric is positive and the coarse metric vanishes in that direction. See the explicit score in [wishart-geometry.md](routes/wishart-geometry.md).

Common precision does not first form at finite time. Even outside the common-precision subfamily, the exact Wishart field gives \(P_i-P_j=e^{-2t}(P_i(0)-P_j(0))\). Unequal initial precisions remain unequal at finite time. The admitted initial equality is a preparation assumption. See [coupled-wishart-flow.md](routes/coupled-wishart-flow.md).

Repeated hidden-child sampling prevents general public compression. For \(N\) equally weighted arbitrary laws on a standard Borel space, \(N\) independent draws from one hidden child identify the unordered collection of child laws. A bounded function separating the finite candidate union reduces equality to Newton power sums. \(N-1\) draws do not suffice in general; the strictly positive Bernoulli polynomial-root example proves sharpness. For arbitrary positive weights with at most \(N\) components, the sharp corresponding bound is \(2N-1\). See [response.md](routes/response.md). These protocols are different from the predeclared extensive-sum interface.

Queries cutting a block require more state. Shared-draw observations of primitive subsets have cross covariance proportional to the shape of their intersection. A parent containing only the total shape does not generally determine that intersection. Unions of whole current blocks remain covered. See [wishart-response.md](routes/wishart-response.md).

Fine energy is not a function of the retained parent state. The opposite shape perturbation around two reference-shape laws at identity precision leaves their sum and global moment unchanged, while the energy increases by twice the sum of two strictly positive KL divergences. See the exact formula in [coupled-wishart-flow.md](routes/coupled-wishart-flow.md). Same-time gradient inheritance is established by direct force calculation, not energy descent.

Selection can fail after an otherwise exact compression. A later event time must be constant on the retained fibers. The source-selection route gives a same-parent local-KL example in which a hidden-child-distance rule gives different later crossing times. The final Wishart selector avoids that failure by using only retained shape averages. See [selection.md](routes/selection.md).

Recording a birth time can remove a putative scalar loss. A two-child alpha gap is known at the threshold and can be reconstructed from event time and parent sum. The final witness therefore uses independent model-shape allocations for loss at both stages. See [wishart-selection.md](routes/wishart-selection.md).

Analytic future equivalence cannot newly collapse at finite regular time for a fixed waiting-closed analytic protocol. The elementary continuation proof in [analytic-behavior.md](routes/analytic-behavior.md) has analytic and common-domain hypotheses. Its deliberately gated smooth-output counterexample disproves a universal smooth extension; that gate is not used in the formation witness.

Changing primitive count or replacing the last channel changes the model. Replacing \(N=\sum_I n_I\) by the number of current parents changes \(\Lambda\). Replacing the final nonidentity self channel by identity deletes an inherited KL term. Neither alteration occurs in the construction.

These failures refute stronger route claims only. None is a nonexistence certificate for the frozen existential target.
