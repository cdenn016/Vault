<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","schema_version":"rigorous-theory-search/v1","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->

# Exact selection scope of the interacting Wishart construction

This third-round addendum assesses the precise formation clauses of the frozen contract and `05_inheritance.tex`, `inh:recursive-formation`. It does not introduce another construction or change the target. The law-dependent-channel flow, normalized responses, and geometric calculations are being derived in the companion routes. The conclusions below are conditional on those calculations being completed on the claimed existence interval. No agreement among workers is used as evidence.

The frozen quantifier is existential: there must exist admissible data and a nonempty declared preparation class giving the required sequence. It does not require every original smooth KL model, every positive initial law, every response protocol, or every possible grouping to work. Its codomain expressly permits state- or accessible-history-selected membership, and the live formation clause expressly permits a declared persistence criterion. Under this quantifier, a fixed threshold applied to a closed retained scalar is an admissible selection rule. Requiring that no quotient exist before its selection would be a stronger target, absent from the frozen contract.

The source rows in this example stay at their priors because each receiver compares every source to the same current law. Thus the selected blocks are not demonstrated to become preferential-attention cliques, and internal/external routing weights do not separate. The proved persistence criterion is the declared shape-distance criterion. A requirement of endogenous routing modularity would be another substantive condition, not a consequence of the displayed membership theorem.

## The proposed interacting specialization

Retain the common-precision Wishart preparation

$$
q_i=W_d(\alpha_i,P),\qquad s_i=W_d(\beta_i,Q),
$$

with context-constant shapes above `(d-1)/2`, positive-definite common precisions, the original positive source priors and temperatures, and a proper product evaluator/reference. The belief channel is the same normalized constitutive rule on every allowed edge:

$$
\mathcal K^q_{ij}[\mathbf q](x,dX)=W_d(\alpha_0,\Lambda_q)(dX),
\qquad
\Lambda_q=I+\frac\kappa N M_q,
\qquad M_q=\sum_i\mathbb E_{q_i}X,
\quad\kappa>0.
$$

The model channel is analogous with `beta_0,M_s`. Each rule is independent of the sampled source content but depends on the current population laws. It has no switch, gate, selected-block argument, event-time argument, or change of formula at a handoff. This limitation of the source-content interface must remain explicit. The peer dependence is nevertheless nonzero at the law level, rather than the constant-channel situation of the preceding round.

For orientation, the complete matter derivative of the mean-dependent portion in the belief sector is the matrix

$$
C(M)=2I+\frac{2\kappa}{N}M-\kappa\alpha_0
\left(I+\frac\kappa N M\right)^{-1}.
$$

This follows from differentiating

$$
\operatorname{tr}((I+\Lambda)M)-N\alpha_0\log\det\Lambda,
\qquad \Lambda=I+\kappa M/N.
$$

The second copy of `kappa M/N` and the inverse-matrix term are the channel-dependence contributions. Freezing the channel would omit them. For a symmetric mean perturbation `H`,

$$
DC_M[H]=\frac{2\kappa}{N}H+
\frac{\kappa^2\alpha_0}{N}\Lambda^{-1}H\Lambda^{-1}.
$$

Its Frobenius pairing with nonzero `H` is strictly positive. Changing another agent's mean therefore changes the force on a receiver. This is a concrete cross-agent interaction within each sector. It does not establish cross-sector coupling: the evaluator remains a product specialization.

The inherited family equations proposed in the companion derivation are

$$
\dot\alpha_i=-2(\alpha_i-\alpha_0),\qquad
\dot\beta_i=-2(\beta_i-\beta_0),
$$

and

$$
\dot P=-2P+C(M_q),\qquad
\dot Q=-2Q+C_s(M_s).
$$

Since `M_q=(sum_i alpha_i)P^{-1}` and `M_s=(sum_i beta_i)Q^{-1}`, shape allocations with the same totals give the same precision evolution. Block counts and total shape parameters reconstruct the population means exactly. The model-shape loss witnesses in `wishart-selection.md` consequently survive this additional interaction: they change neither the population means nor any selector event.

The interacting precision equations replace the explicit uncoupled formula in `wishart-selection.md`; that formula must not be copied into the final theorem for `kappa>0`. The shape equations and every selection-time formula in that file are unchanged. Regularity must be proved from the actual precision equation, not inferred from the previous round's independent relaxation.

There is an elementary bound supplying global positive-definite continuation for sufficiently small fixed positive coupling. Set `a(t)=sum_i alpha_i(t)/N`. The precision vector field commutes with `P`, so its fixed eigenvectors diagonalize the evolution and each eigenvalue obeys

$$
\dot p=-2p+2+\frac{2\kappa a(t)}p
-\kappa\alpha_0\frac p{p+\kappa a(t)}.
$$

For `0<kappa alpha_0<=1`, the last fraction is between zero and one, hence `dot p>=-2p+1`. Integration gives `p(t)>=1/2+(p(0)-1/2)e^{-2t}`, in particular `p(t)>=p_min=min(p(0),1/2)>0`. Since `a(t)<=a_max=max(a(0),alpha_0)`, also

$$
\dot p\le-2p+2+2\kappa a_{\max}/p_{\min}.
$$

The analogous integrated upper bound prevents finite-time escape. Local smooth ODE continuation then gives a global solution in the positive-definite domain. The same argument applies to `Q` if `kappa beta_0<=1`. On a compact admitted set of initial parameters these bounds are uniform, and the vector field has bounded derivatives on every bounded time interval. Differentiating its integral equation and applying the elementary integrating-factor estimate gives smooth dependence on initial precision, context, and coupling. These bounds establish regularity; they do not by themselves establish a nonzero collective curvature.

## What the state/history selector proves

For a current parent retain its primitive count `n_I`, its shapes `A_I=sum alpha_i`, `B_I=sum beta_i`, and the common precisions. Use exactly one fixed threshold `delta>0` and the current scalar `b_I=A_I/n_I-alpha_0`. It obeys `dot b_I=-2b_I`, and joining uses the primitive-count weighted average. Thus no new time scale, source prior, or attraction is inserted after the first join.

The open sorted-gap preparation class and event times proved in `wishart-selection.md` remain valid. Write the sorted initial belief shapes as `a_1<a_2<a_3<a_4`, with gaps `d_1,d_2,d_3`, and require

$$
\delta<\min(d_1,d_3),\qquad d_2>\max(d_1,d_3).
$$

The two pairs form at `t_L=(1/2)log(d_1/delta)` and `t_R=(1/2)log(d_3/delta)`; their parent forms at

$$
t_2=\frac12\log\left(\frac{d_2+(d_1+d_3)/2}{\delta}\right)
>\max(t_L,t_R).
$$

Before each event the selector reads only the current retained laws and counts; after each event it applies the same rule to their inherited evolution. No fine shape split is consulted at the second stage. The selected relation is persistent because every joined child-block score difference continues to decrease exponentially. Both first parents and all primitive children remain distinct at the relevant finite times. Membership marks record this selection, while the actual continuous fine state follows the same autonomous vector field throughout.

The class includes all label permutations of these shape inequalities. It contains no named pair or binary tree. Its common precisions are all-agent symmetric statistical structure, and its gap inequalities are asymmetric initial data; neither supplies a tree-shaped profile family. Different allowed orderings assign different physical labels to the two selected pairs. The selected object is therefore a membership hierarchy read from the evolving state and accessible history. It is not a claim that a previously nonexistent quotient has appeared.

This distinction also answers the earlier analytic obstruction. Exact sum-law quotients exist for every grouping in the admitted common-precision family already at time zero. The flow and selector choose when and where to use them. Analytic preservation of preexisting operational equivalence is compatible with this result. The argument does not claim finite-time destruction of distinctions observable through unrestricted fine probes.

## Clause-by-clause match and the scope that must remain visible

The live formation clause asks for nontrivial blocks selected from initially unpartitioned configurations. Initial partition marks here are all singletons, and the threshold rule constructs subsequent membership. It asks for a declared persistence criterion and state/history handoff. The decreasing retained-shape distances and exact event map provide both. It asks for inherited belief laws, model laws, evaluators, boundary responses, and dynamics. These are separate mathematical obligations discharged only by the actual Wishart sum, reference/evaluator, flow, and response calculations in the companion construction; selection alone does not prove them.

The clause then asks that resulting parents select a block containing at least two first parents under inherited interactions, without source reset or newly tuned attraction. The second event uses the same scalar, threshold, original-time field, global mean, and primitive counts. Since the interaction depends on the complete population mean, `N=sum_I n_I` must be preserved at every stage. Replacing `N` by the number of current parents would change the dynamics and fail the clause.

The frozen contract admits explicitly justified regular statistical families. The construction supplies such a non-Gaussian family on a standard Borel matrix cone. It does not prove closure for arbitrary laws outside it, and the final statement must name the Wishart/common-precision preparation. An analytic positive example can establish an existential claim within smooth dynamics, since it is itself smooth; an obstruction limited to analytic dynamics could not exclude all smooth examples. Neither observation permits changing the target to a universal statement about arbitrary smooth channels.

The no-synchronization premise requires care in presentation. No children are replaced by equal laws, projected onto equality during evolution, or forced to merge in the fine state. Their differing shapes remain distinct. Common precision is nevertheless a supplied equality among some statistical parameters, valid before formation; the flow is not shown to create common precision from unequal values. The proof must state this preparation restriction, rather than describing it as dynamical synchronization. If the phrase “no imposed child synchronization” were intended to forbid every common statistical parameter in the initial preparation, this construction would not satisfy that stronger reading. The frozen contract's explicit allowance for a declared regular preparation class, together with its prohibition specifically on a tree-shaped invariant preparation, does not itself impose that stronger condition. No mathematical claim about generation of common precision should be made.

The response interface is extensive: it preserves declared joint sum-matrix kernels and their finite adaptive histories, with the already observed records carried forward at handoffs. It does not preserve every individual-child probe, reused latent sample, or fine-state reset. These restrictions are part of the construction before testing preservation. A final proof must distinguish full joint laws within this declared class from unrestricted response equivalence. Observable child-level data already in an external record are retained as history, not erased by joining.

The forbidden erasure-gate premise is satisfied in the temporal sense by a constitutive channel formula that is smooth throughout the run and never changes at a formation event, together with a fixed sample-addition retention. The source-independent sampled output is a permanent interface choice and must be disclosed. The stronger demand that every original physical channel transmit nontrivial sampled source content is not among the frozen premises. It would be a different construction problem. This route introduces no arbitrary added potential: every mean force above comes from a displayed normalized original channel and its complete derivative.

The information-loss clause is met by the independent beta-shape allocations, not by an alpha split recoverable from an exact birth time. Within a first pair, opposite beta perturbations preserve its sum, all event times, its retained laws, and the population mean. Between the two first parents, opposite beta-total perturbations preserve the root state and all event times. These are continuous differences in actual public probability laws with nonzero fine Fisher tangents. They are not permutations or storage of the full child tuple.

Finally, collective geometry requires more than a normalized sum channel. The companion proof must show on the declared contextual section that the sample-sum score retains every common-precision covariant tangent and orbit direction, that the stabilizer kernels agree, and that the minimizing connection and contextual residual tensor are inherited. A nonzero tensor and actual connection curvature must be calculated rather than inferred from data processing. Context-constant shape allocations are necessary for the stated exact tensor equality: allowing discarded beta allocations to vary along the context produces the positive residual loss already exhibited in `wishart-geometry.md`. The initial common-precision section and the base/represented-coordinate distinction must stay explicit.

## Logical conclusion and remaining mathematical gate

There is no additional semantic obstruction to a declared threshold selector under the frozen state/history-selected formation definition. Conditional on the complete normalized interacting flow, response, and geometric proofs, the selection theorem supplies the missing two-stage membership and handoff clauses. It supports an exact existential construction on the named invariant preparation and response class. It does not support a claim that the dynamics intrinsically create a quotient absent at time zero, dynamically attract arbitrary preparations into the common-precision family, or preserve unrestricted fine responses.

The remaining mathematical gate for this third-round replacement is precise: establish the claimed regular nontrivial contextual geometry for the interacting precision equation throughout an interval containing both first joins, the second join, and a nonzero interval afterward, while preserving the exact response and inherited-flow identities. The previous uncoupled formulas for `P(t),Q(t)` are insufficient for that gate. A bounded small-positive-`kappa` continuation argument with explicit compact preparation/context bounds would suffice if it proves positivity, constant orbit rank, nonzero curvature/residual rank, and smooth dependence on the required interval. A proof for all finite times is stronger than needed for a clearly stated finite formation interval, but cannot be claimed from a finite-window continuation argument.

This route neither assigns a release status nor treats semantic agreement as mathematical evidence. It identifies exactly which formation clauses the selection proof settles and which interacting geometric argument still needs to be supplied. No numerical experiment, heavy computation, external literature claim, or further agent panel was used.
