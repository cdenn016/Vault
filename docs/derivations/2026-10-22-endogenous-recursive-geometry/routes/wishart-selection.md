<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","schema_version":"rigorous-theory-search/v1","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->
schema_version: rigorous-theory-search/v1
contract_id: contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e
target_digest: cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e
artifact_type: constructive-route-addendum
route_id: wishart-selection
status: CONDITIONAL_SELECTION_AND_INFORMATION_LOSS_THEOREM

# Shape-selected Wishart parents with two exact handoffs

This addendum proves the membership-selection part of the Wishart construction supplied by the parent research route. It assumes the displayed original-flow restriction and normalized Wishart convolution identity; their derivation and the collective-geometry calculation belong to the companion route. The result is conditional on that constitutive specialization, including its product evaluator, common precisions, and fixed reference-returning comparison channels. It makes no claim of mutual source-content coupling. Selection changes a membership mark and a coarse representation; it leaves the fine vector field unchanged.

Fix matrix size `d>=1` and put `a_min=(d-1)/2`. Use the rate-precision convention

$$
W_d(a,P)(dX)=\frac{\det(P)^a}{\Gamma_d(a)}
\det(X)^{a-(d+1)/2}e^{-\operatorname{tr}(PX)}dX,
\qquad X\in\operatorname{SPD}(d),\quad a>a_{\min},\quad P\in\operatorname{SPD}(d).
$$

The supplied fine laws are

$$
q_i=W_d(\alpha_i,P_1),\qquad
s_i=W_d(\beta_i,P_2),\qquad i=1,2,3,4,
$$

with common precisions across agents and reference shapes `alpha_0,beta_0>a_min`. No equality of the primitive shape parameters is imposed. The original full-density Fisher flow on this family is assumed, as established in the companion construction, to be

$$
\dot\alpha_i=-2(\alpha_i-\alpha_0),\qquad
\dot\beta_i=-2(\beta_i-\beta_0),\qquad
\dot P_r=-2(P_r-I),\quad r=1,2.
$$

All source rows remain their original positive priors. There is no source-row reset at a handoff. These equations have the explicit global forward solution

$$
\alpha_i(t)=\alpha_0+e^{-2t}(\alpha_i(0)-\alpha_0),\qquad
\beta_i(t)=\beta_0+e^{-2t}(\beta_i(0)-\beta_0),
$$

and `P_r(t)=I+e^{-2t}(P_r(0)-I)`. Shapes remain strictly above `a_min` by convexity, and precisions remain positive definite with eigenvalues bounded below by `min(1,lambda_min(P_r(0)))`. Thus every finite event below occurs on the regular positive Wishart family. There is no discretization, stochastic matter motion, rescaled time, or boundary limit.

For a block `I`, let `n_I=|I|`, `A_I=sum_{i in I}alpha_i`, and `B_I=sum_{i in I}beta_i`. Independent addition of the actual represented matrices gives the parent laws

$$
q_I=W_d(A_I,P_1),\qquad s_I=W_d(B_I,P_2).
$$

The retained state contains `(n_I,A_I,B_I,P_1,P_2)` and the constant source data needed by the original specialization, rather than the tuple of primitive shapes. Joining disjoint blocks adds `(n,A,B)` and keeps the common precisions. The shape equations descend exactly:

$$
\dot A_I=-2(A_I-n_I\alpha_0),\qquad
\dot B_I=-2(B_I-n_I\beta_0).
$$

Consequently addition commutes with the original-time flow. In particular, the reference shape for a parent with `n_I` primitives is `n_I alpha_0` or `n_I beta_0`, inherited from its children rather than reset to the single-agent reference shape.

## A state-selected open preparation class

Fix one positive selection threshold `delta` as constitutive data. The selector reads only the present parent law and primitive count through

$$
b_I=\frac{A_I}{n_I}-\alpha_0.
$$

It obeys

$$
\dot b_I=-2b_I,\qquad
b_{I\cup J}=\frac{n_Ib_I+n_Jb_J}{n_I+n_J}.
$$

The model-sector shapes `beta_i` do not enter membership selection. This separation will supply continuous information loss even when every event time is retained.

Start with four singletons. While a partition is fixed, evolve its exact inherited parent laws. When the distance `|b_I-b_J|` first reaches `delta` from above, join those two current blocks. If several distances reach the threshold simultaneously, join the connected components of the threshold graph. After every join, recompute the distances using the count-weighted shape average. This rule uses no prescribed binary tree and is invariant under relabeling. On the class below, simultaneous cascades and larger initial connected components do not arise.

Let `a_1<a_2<a_3<a_4` denote the sorted initial belief shapes, without assigning their ordering to predetermined agent labels. Put

$$
d_1=a_2-a_1,\qquad d_2=a_3-a_2,\qquad d_3=a_4-a_3.
$$

Admit precisely those shapes satisfying

$$
a_i>a_{\min},\qquad
\delta<\min(d_1,d_3),\qquad
d_2>\max(d_1,d_3).
\tag{S}
$$

The model shapes may vary independently throughout `beta_i>a_min`, and the common initial precisions may vary throughout their positive-definite domain. These are strict inequalities in finite-dimensional statistical parameters, so the initial class is open within the declared common-precision Wishart family. It is not open in the space of all positive density tuples, and no such stronger claim is intended. The class contains all relabelings of its members. It imposes separated scalar gaps but no profile equalities, latent tree, or invariant matching of model shapes.

For any fixed `delta>0` and any reference shapes in the admissible domain, the class is nonempty: choose a sufficiently large `h>a_min` and `(a_1,a_2,a_3,a_4)=(h,h+2delta,h+8delta,h+11delta)`. Its gaps are `(2delta,6delta,3delta)`.

**Theorem (two first parents followed by their parent).** For every preparation in (S), let `L` be the two labels with the lower initial belief shapes, and `R` the two with the upper initial shapes. The selector first forms these two pairs, in whichever order their outer gaps dictate, at

$$
t_L=\frac12\log(d_1/\delta),\qquad
t_R=\frac12\log(d_3/\delta).
$$

It then forms their union at

$$
t_2=\frac12\log(D/\delta),\qquad
D=d_2+\frac{d_1+d_3}{2}.
$$

There are no intervening cross joins or immediate cascades, and `t_2>max(t_L,t_R)>0`. Both first-stage parents therefore coexist as distinct objects on a nonzero open time interval. Every chosen child-block threshold relation remains true thereafter, and all four fine belief laws remain distinct at every finite time.

*Proof.* For any two primitive shapes, their difference at time `t` is their initial difference times `e^{-2t}`. Before a join, the smallest current gap is therefore one of the two outer sorted gaps. Suppose first that `d_1<d_3`. The lower pair is uniquely first, at `t_L`. Its count-weighted score corresponds to the mean initial shape `(a_1+a_2)/2`, scaled relative to `alpha_0`. Its closest distance to a remaining singleton is

$$
e^{-2t}\left(a_3-\frac{a_1+a_2}{2}\right)
=e^{-2t}(d_2+d_1/2).
$$

By (S), `d_2+d_1/2>d_3`. The upper singleton pair thus reaches the threshold before any cross distance does, at `t_R`. At either event all cross distances are strictly above `delta`, so recomputing the means cannot produce an immediate cascade. If `d_3<d_1`, interchange the upper and lower arguments. If `d_1=d_3`, the two disjoint outer edges reach the threshold simultaneously, while every cross edge is still strictly above it. The connected-component convention forms exactly the two pairs.

After both joins, the only current interparent distance is

$$
e^{-2t}\left(\frac{a_3+a_4}{2}-\frac{a_1+a_2}{2}\right)
=e^{-2t}D.
$$

Since `D>max(d_1,d_3)`, the union event occurs strictly later at the stated time. The retained laws and counts supply every quantity used at both stages.

For persistence, continue the score of each child block along the original fine flow, whether or not its representation remains stored. Their postjoin difference remains its initial value times `e^{-2t}`. It equals `delta` at the chosen join and is strictly smaller afterward. Thus persistence of the admitted relation follows from the dynamics, in addition to the membership history being retained. The primitive shape gaps are nonzero for every finite time. Since distinct Wishart shapes at the same precision give distinct laws, all primitive children remain distinct. The same argument gives distinct first-parent laws before and at their join because `A_L/2-A_R/2` is nonzero. QED.

The theorem selects a hierarchy using the actual evolving retained laws. The algebra permitting shape-sum quotients was present from the beginning; no new operational redundancy is created by crossing the threshold. There is also no new attraction at a parent level. The threshold is a declared state-based membership criterion under uniform relaxation. It is not evidence that peer interactions produce that criterion or maintain nonzero separation in the infinite-time limit.

## Continuous loss survives all formation-time information

Retaining exact birth times can eliminate apparent information loss in a two-child scalar construction. In the present example, the first alpha gap is known to be `delta` at birth. Together with the parent alpha sum, birth time, and current time, it can determine the unordered alpha pair. Therefore the alpha split is not used as the required loss witness.

The model-sector split gives a continuous witness which is independent of all event times. Fix all four alpha parameters, both precisions, and all source data. The entire membership schedule, labels, and formation times are now fixed. At the first join of labels `i,j`, vary their initial model shapes by

$$
(\beta_i(0),\beta_j(0))\longmapsto
(\beta_i(0)+\epsilon,\beta_j(0)-\epsilon).
$$

For every sufficiently small positive or negative `epsilon`, both shapes remain above `a_min`. Their sum, and hence the joined model law, agrees at every time. Their individual laws change. All belief laws and every selector decision remain unchanged. Thus the first parent identifies a continuous family of different complete fine configurations even when every formation time, membership mark, primitive count, and common precision is retained. This cannot be a permutation because every alpha label remains fixed and distinct.

For the second join, vary the model shape sums of the first parents in opposite directions while keeping the total fixed. In initial primitive parameters one explicit variation is

$$
\beta_i(0)\longmapsto\beta_i(0)+\epsilon/2\quad(i\in L),
\qquad
\beta_i(0)\longmapsto\beta_i(0)-\epsilon/2\quad(i\in R).
$$

For small `epsilon` this stays in the admitted shape domain. Each first-parent model law changes, but their sum shape and the root model law do not. Every alpha parameter and every formation time remain unchanged. The root therefore forgets a further continuous difference between its two children, beyond the losses already made inside them.

These are nonzero Fisher directions before the relevant quotient. For a single model Wishart law, the beta score is

$$
\partial_\beta\log p_{\beta,P_2}(Y)
=\log\det Y+\log\det P_2-\partial_\beta\log\Gamma_d(\beta).
$$

Its variance is strictly positive because `log det Y` is nonconstant under a law with positive density on all positive-definite matrices. Thus changing two beta shapes oppositely is a genuine statistical tangent, not the nonsmooth phase relabeling of the prior balanced-profile construction. The coarse sum-shape derivative vanishes on this tangent. The companion geometry route must still check how this loss interacts with the collective connection; positivity alone does not prove connection inheritance.

## Histories and contextual scope

The declared response at a current block draws fresh independent represented matrices from its descendants, adds them in each sector, and applies the predeclared normalized record kernels to the sums. The Wishart convolution identity makes these exactly the parent responses. Current retained parameters give their whole joint next-record law. A response protocol may adapt its next admitted kernel and query time to previously observed records. There is no child-specific Bayesian reset in this statement.

At each handoff the already observed history is carried forward as external controller state. The law of earlier records is not overwritten or identified across different fine preparations. The correct path-law statement is chronological: before the first join the primitive representation supplies the correct factors, between joins the first-parent representation supplies them, and after the second join the root representation supplies them. Equality of the conditional next-record kernels and event maps at each transition proves equality of the entire finite response history for each preparation separately. It does not assert that two different initial preparations have identical records from time zero.

The continuous beta-loss witnesses survive attaching exact formation times. For finitely many ordinary matrix samples or strictly positive record kernels, the same realized record values have positive densities throughout a neighborhood of these beta variations. Carrying those values does not encode a deterministic inverse of the discarded beta split. Infinite observation limits, direct disclosure of each child's parameter, and unrestricted fine-state interventions are outside the declared interface.

For compatibility with a smooth contextual precision section, take alpha and beta shapes constant over the context base while allowing the common precisions `P_1(c),P_2(c)` to vary smoothly. The selector and event times then are independent of context, and a single selected partition applies to the entire chart. The joining map is the same smooth shape-addition map before and after each global time event. Context-dependent shapes would require separate treatment of regions where the membership order or event time changes; this addendum does not silently assume a global smooth retention across such switching boundaries.

The remaining obligations are those explicitly delegated to the companion construction: normalized full-density realization of the displayed field, full inherited response/evaluator specification, and a nonzero contextual geometry whose collective minimizing connection and stabilizer class survive both joins. This file establishes the exact selection, two-stage timing, no-cascade property, threshold persistence, finite-time distinctness, and continuous information loss even after all membership-event times are retained. No computation or external theorem search was used.
