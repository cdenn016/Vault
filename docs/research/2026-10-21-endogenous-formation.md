# Endogenous formation: exact obstruction and a nonsmooth construction

The continuation starts from Research revision `ac07890d17fda8b59881c9b0a4baef0dcbc9b4a7`. The target is an initially unpartitioned statistical-agent population whose dynamics select persistent blocks, whose parents inherit their laws and future responses, and whose inherited dynamics produce a second formation stage. The work is confined to one context, with gauge-covariant interfaces and both belief and model sectors. General probability laws remain the surrounding framework; a particular family may be used for an explicit example.

The live starting sources were Chapters 2, 3, 5, and 6 of `manuscripts/MAgent_Theory_2.0/`, the formation construction in `manuscripts/pifb2/13_section.tex`, and the prior recursive-formation and saddle-protocol investigations under `MultiAgentELBO/docs/research/2026-10-02-renormalization-completion/`. The earlier supplied sixteen-to-eight-to-four-state hierarchy establishes exact inherited histories but does not select its own retentions. Prior externally organized episodes and stationary conditional agreement also leave the required dynamical inheritance unresolved.

## Exact obstruction in the existing smooth potential

The new section in `chapters/05_inheritance.tex` uses strictly positive binary laws, a normalized coupled evaluator, nonconstant law-dependent channels, and unit Fisher mobilities. For the arithmetic mixture retention, two fine configurations retain identical belief, model, and averaged joint laws but have different retained belief derivatives. With the notation of that section, the derivatives are

\[
\dot{\bar x}(A)=Jc,\qquad
\dot{\bar x}(B)=Jc(1-a^2).
\]

The discrepancy is nonzero for arbitrarily small nonzero separation. It is not caused by heterogeneous child roles. The same retention also loses a boundary response: the uniformly selected child's communicated bit has output means differing by \(3ma^2/4\) for two populations with identical retained laws. These are exact counterexamples to this retention, not to every smaller parent state.

Smooth interior uniqueness gives a separate obstruction to finite-time synchronization: a trajectory cannot first enter an invariant equality diagonal at finite time. This does not exclude asymptotic synchronization, other quotients, or dynamics reaching a nonsmooth boundary.

## Constructive result and its changed assumption

The new main Chapter 6, `chapters/06_fusion.tex`, replaces smooth peer KL costs by explicitly normalized square-root KL costs between primitive message laws. This is a constitutive extension. Its finite-time fusion mechanism belongs to the established family of nonsmooth consensus and convex fusion constructions, as described in [Cortés (2006)](https://doi.org/10.1016/j.automatica.2006.06.015) and [Hocking et al. (2011)](https://icml.cc/2011/papers/419_icmlpaper.pdf). Their results are background for the mechanism; the statistical inheritance and the particular trajectory are derived directly in the manuscript.

The example uses lognormal laws with fixed log variances. For a component of multiplicity \(n\), the belief and model log variances are \(1/n\), and the Fisher metric on their two log means is \(n\) times the unit metric. The reference joint law and normalized evaluator are the geometric-mean pushforwards of the primitive laws. The inherited local KL differs from the sum of primitive local KLs only by a displayed state-independent constant. Contact weights add to \(n_In_J\). No new attraction or mobility is installed after fusion.

The positive scalar transport has a log generator proportional to the difference of the endpoint log means. Thus the transport depends on the laws and transforms under endpoint frame changes. Restoring primitive message resolution by a normalized conditional kernel makes the square-root KL cost exactly an absolute difference of log means. The calculation includes the derivative of the law-dependent link.

On the declared invariant family with a common difference between belief and model log means, the coupled flow reduces to a contracting common mode and a one-dimensional sticking flow. For four unit agents initially at common-mode positions \((-3d,-2d,2d,3d)\), two size-two parents form at

\[
t_1=\frac{1}{a-c}\log\left(1+\frac{(a-c)d}{2\lambda}\right).
\]

They remain distinct and interact before merging at

\[
t_2=\frac{1}{a-c}\log\left(1+\frac{5(a-c)d}{4\lambda}\right).
\]

The pairing is selected by the initial positions and the unchanged equations. A strict gap condition gives an open admitted class within that invariant family. The proof constructs the piecewise solution, establishes uniqueness by convex subgradient monotonicity, and proves persistence and exact reduction on each fusion stratum. It does not assume a preassigned partition or use a numerical clustering threshold.

The sample retention is noninjective: it keeps a geometric mean. The corresponding location-parameter reduction, once children are exactly synchronized, removes redundant coordinates and is injective modulo labels. This is not a theorem about autonomous compression of distinct child parameters. That distinction limits the formation claim.

Fresh boundary messages and fresh model-generated records have exact inherited kernels. Joint reconstruction of constituent samples requires correlated residuals; independent residual draws conditioned on one shared average are incorrect. Internal registers may store the declared fresh outputs, but no observation-feedback, persistent hidden sample, or repeated private-readout equivalence is claimed.

## Other route considered

A finite public/private conditional-lift construction gives exact channel and evaluator descent. Weighted forward-KL pooling also gives an exact recursively closed coalescent when an event binds all children's future public updates. That binding rule is extra dynamics, rather than a consequence of the original Fisher flow. This route was not inserted as a solution of the formation target. It identifies a concrete alternative mechanism and the obligation it would need to satisfy.

## Scope and continuation

Two substantive construction rounds produced the smooth-flow counterexample and the nonsmooth fusion example. No audit or adjudication panel was run. The decisive formulas were reconstructed analytically; no numerical simulation, GPU operation, or Lean work was used. Document compilation and rendering are recorded separately in the daily edit log.

The strongest result is an exact two-stage fusion example under stated additional assumptions. The remaining original-model obligation is formation and parent closure under the smooth KL potential. A stronger compression target would retain a smaller autonomous state while children remain internally distinct, with future record feedback included in the same inherited process. Neither obligation is closed by the fusion construction. The immediate continuation should choose which of these two gaps to address and retain the counterexample as a test of any proposed parent.
