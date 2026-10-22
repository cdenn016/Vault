<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","schema_version":"rigorous-theory-search/v1","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->
schema_version: rigorous-theory-search/v1
contract_id: contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e
target_digest: cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e
artifact_type: constructive-route
route_id: selection
status: PARTIAL_CONSTRUCTION_AND_NECESSARY_CONDITIONS

# Selection and exact handoff under KL relaxation

The frozen target asks for the existence of at least four agents, normalized constitutive data, and a nonempty initially unpartitioned preparation class for which the original autonomous two-sector KL/Fisher dynamics select persistent first parents and then a parent containing at least two of them. Every admitted preparation and response/control history must admit exact same-time dynamics, responses, joining, and collective geometry, with actual information loss and distinct children. A supplied tree or a newly imposed parent attraction does not satisfy this target.

This route proves a positive, restricted selection mechanism and two necessary conditions. The positive construction selects a hierarchy from an open inequality class of general laws, supplies both formation times, and has exact compressive joins and response histories. Its constitutive specialization has a product evaluator and common-reference comparison channels: the fine matter equations are uncoupled KL relaxation. Its collective Fisher geometry is not established. It is therefore not a witness for the requested interacting geometric formation mechanism. The conditional result locates an interface at which a stronger construction could replace the uncoupled flow.

The live sources read were the complete `03_dynamics.tex`, the descent, boundary, composition, and formation material in `05_inheritance.tex`, collective-connection inheritance in `02_geometry.tex`, and the supplied profile construction in `10_boundary_closure.tex`, together with the two October 21 research records. The associative log-spectrum retention below is prior work from `2026-10-21-boundary-closure.md`. The new result is its explicit state-selected membership rule, open preparation class, separated two-stage handoff, and persistence proof. No supplied balanced profile tree, phase quotient, or nonsmooth fusion has been rediscovered as a new construction.

## 1. A positive selection mechanism on a preexisting exact quotient

Let `(X,A)` and `(Y,B)` be standard Borel probability spaces. Let all four primitive agents have arbitrary densities `f_i` and `g_i` against these references, with bounded logarithms. Their recognition laws are `q_i tensor s_i`, and the proper joint reference is `A tensor B`. Thus the normalized evaluator is `G_i(m,dk)=A(dk)`. This additional product-evaluator assumption is not supplied by the target and removes its general cross-sector coupling.

Allow every nonself source with positive uniform prior and the original positive temperatures. Choose the fixed normalized channels

$$
\mathcal K^q_{ij}(x,dk)=A(dk),\qquad
\mathcal K^s_{ij}(y,dm)=B(dm).
$$

These are common-reference comparison channels. They discard source content at every state, rather than switching it off at a formation time. The resulting equations supply no interaction-mediated attraction. This constitutive specialization must be stated explicitly when assessing the requested absence of a prescribed erasure gate; there is no time-dependent or state-triggered erasure mechanism in the construction. An alternative with only identity self-channels has no erasing channel but is equally uncoupled and changes the rate below from two to one. The positive theorem here uses the nonempty nonself rows just specified.

For these channels, `q_j K^q_ij=A` and `s_j K^s_ij=B`, so their variations vanish exactly. Every source in a given receiver row has the same cost. Substitution into the original potential, with every original derivative included, gives

$$
\mathcal E=2\sum_i\operatorname{KL}(q_i\Vert A)
 +2\sum_i\operatorname{KL}(s_i\Vert B)
 +T_q\sum_i\operatorname{KL}(\beta_i\Vert\pi_i^q)
 +T_s\sum_i\operatorname{KL}(\gamma_i\Vert\pi_i^s).
$$

Start the rows at their original priors. Their Fisher equations then vanish, and no reset occurs at any later handoff. The Gibbs-reduced potential gives the same matter evolution. Write `ell_i=log f_i`, and use `c=2`. The original unit-mobility field is

$$
\dot\ell_i=-c\ell_i+c\mathbb E_{q_i}\ell_i,
\qquad
f_i(t)=\frac{f_i(0)^{a(t)}}{\int f_i(0)^{a(t)}dA},
\qquad a(t)=e^{-ct}.
$$

The model equation is identical with `g_i,B`. These formulas prove existence, uniqueness, normalization, positivity, and global forward continuation in the bounded-log-density chart. If `|log f_i(0)|<=L`, then `|log f_i(t)|<=2L` for every nonnegative time. The formulas concern a continuous deterministic flow, with original time and no noise or discretization. Its energy decreases by the original Fisher dissipation identity; specifically its matter contribution has derivative `-c^2 sum_i Var_q_i(log f_i)` and the corresponding model term.

Choose one bounded measurable observable `T:X -> R` before specifying any retention, with `E_A T=0`. For a block `I`, independently sample `X_i` from its actual child laws and define

$$
L_I=\sum_{i\in I}\log f_i(X_i),\qquad
S_I=\sum_{i\in I}T(X_i),\qquad
P_I=\mathcal L_{\bigotimes_{i\in I}q_i}(L_I,S_I).
$$

Let `eta_I` be the same statistic's law under `A^{tensor |I|}`. The two normalized laws satisfy `P_I=e^L eta_I`, equivalently `eta_I=e^{-L}P_I`. Retain `(|I|,P_I)` in the belief sector and the analogous model statistic for a previously declared centered bounded model observable. The constant row priors, primitive counts, and selected membership labels are also retained. No probability distribution over fine law configurations is introduced.

Independence of the represented samples gives the associative join

$$
(|I|,P_I)\star(|J|,P_J)=(|I|+|J|,P_I*P_J)
$$

for disjoint blocks. This is not a tuple of the child laws. It is the convolution law of the two summed statistics.

For completeness, its exact inherited equation follows directly. Set

$$
v_I=-cL+c\mathbb E_{P_I}L.
$$

For every bounded continuously differentiable test with bounded derivative on the current compact statistic range,

$$
\frac{d}{dt}\mathbb E_{P_I}\varphi(L,S)
=\mathbb E_{P_I}[(\partial_L\varphi+\varphi)v_I].
$$

The derivative of the summed log statistic is `v_I`; the log derivative of the product sampling density is also `v_I`. These are the two terms in this equation. More explicitly, given the retained initial law, set

$$
Z_I(a)=\int e^{aL}d\eta_I^0.
$$

Then `eta_I^t` is the pushforward of `eta_I^0` by `(L,S) -> (aL-log Z_I(a),S)`, and `P_I^t=e^L eta_I^t`. This specifies a unique same-time parent flow without reconstructing the children. Since the normalizers multiply under convolution, evolution commutes with joining.

The useful selector scalar is already measurable from this parent:

$$
b_I=\frac{1}{|I|}\mathbb E_{\eta_I}[LS]
=\frac{1}{|I|}\sum_{i\in I}\int T\log f_i dA.
$$

The second equality follows by expanding the double sum. Every off-diagonal term vanishes because `E_A T=0`. The same centering removes the log normalizer in the explicit flow, proving

$$
b_I(t)=a(t)b_I(0),\qquad
b_{I\cup J}=\frac{|I|b_I+|J|b_J}{|I|+|J|}.
$$

This exact relation is the positive selection interface. It does not assert that ordinary mixture means obey the same law.

**Proposition 1 (explicit two-stage selection).** Fix a threshold `delta>0`. Start with four singleton blocks. At the first time a distance `|b_I-b_J|` between current blocks reaches `delta` from above, join those blocks using `star`. Recompute the current distances after each join. In a simultaneous event, join each connected component of the threshold graph. Retain the resulting membership history. Suppose the initial four scores, sorted without prescribing agent labels, are

$$
v_1<v_2<v_3<v_4,
\qquad d_1=v_2-v_1,\quad d_2=v_3-v_2,\quad d_3=v_4-v_3,
$$

and satisfy

$$
\delta<\min(d_1,d_3),\qquad d_2>\max(d_1,d_3).
$$

Then the selector forms the pair at the two lower scores at time

$$
t_L=c^{-1}\log(d_1/\delta),
$$

and the pair at the two upper scores at time

$$
t_R=c^{-1}\log(d_3/\delta).
$$

It subsequently joins these two first-stage parents at

$$
t_2=c^{-1}\log(D/\delta),\qquad
D=d_2+(d_1+d_3)/2.
$$

Both first parents coexist on the nonempty interval `(max(t_L,t_R),t_2)`. Each joined relation remains inside its threshold thereafter when its original two child-block scores are continued under the inherited flow. All four primitive child laws remain distinct at every finite time.

*Proof.* Before any join, every distance equals its initial distance times `a(t)`. The smallest initial distance is one of the two outer gaps. Suppose `d_1<=d_3`. The lower pair joins first at `t_L`, and its score becomes `a(t)(v_1+v_2)/2`. Its nearest distance to a remaining singleton is `a(t)(d_2+d_1/2)`, strictly larger than `a(t)d_3`. Thus the upper pair joins next at `t_R`, without any cross join. The case `d_3<d_1` is identical with the order reversed. After both joins their distance is exactly `a(t)D`. Since `D>max(d_1,d_3)`, it reaches the threshold at the stated later time. There are no other current blocks. Each joined child-block distance is the same decreasing exponential after the join, so the threshold relation cannot subsequently fail. At all finite times the primitive scalar scores remain distinct, which forces the corresponding full belief laws to remain distinct. The bounded-density solution formula supplies existence throughout every interval used. QED.

The preparation class is open in the bounded-log-density chart: the four score functionals are continuous, and all inequalities are strict. It is nonempty, for example with balanced `T` taking values `+1,-1` and exponential tilts having scores `(-4,-3,3,4)` when `delta=1/2`. Unions over label permutations admit no prescribed pairing. The prepared inequalities create separated scales, but they impose no exact profile equalities, supplied binary tree, or tree-shaped invariant statistical family. The selection rule is relabeling-natural. A passive re-expression of samples carries `A,T,f_i` together and leaves every scalar and decision unchanged.

Membership is newly selected at the displayed times; the quotient algebra exists before these times. The joins neither modify the fine equations nor supply a second-level attraction. Persistence here is proved for the declared threshold relation, not inferred merely from storing an irreversible membership flag. All contrasts decay to zero as time tends to infinity, so no permanent nonzero separation is claimed.

The response class is declared as follows. At a query time, independently sample every descendant once, compute its previously chosen observable, and apply any fixed normalized readout `H_e(do|S_I)` to their sum. The choice of `e` and the next sampling time may depend on preceding records. All samples are fresh. The model sector uses its own samples. This protocol can be nonconstant in the retained laws; for example, observing the full sum distinguishes different belief tilts. The parent supplies exactly `integral H_e(do|S) P_I(dL,dS)`. At a join, independent parent sums add, which gives exactly the direct descendant response. Since both the continuous parent flow and every join agree, induction over the sequence of query and join events proves equality of the entire finite adaptive response-history law. This class does not include Bayesian resetting of individual children, arbitrary source-input/output correlations, or unrestricted external fine-law probes.

Actual information is lost. Take three independent fair reference bits `U,V,W`, choose `T=U`, let `A_i(U)` be positive normalized tilted bit densities with different prescribed scores, and let `a(V),b(W)` be nonconstant normalized positive densities. Compare the two fine pairs

$$
(f_1,f_2)=(A_1(U)a(V)b(W),A_2(U))
$$

and

$$
(\widetilde f_1,\widetilde f_2)=(A_1(U)a(V),A_2(U)b(W)).
$$

Swapping only `W_1,W_2` under the product reference preserves `S=U_1+U_2` and carries one summed log density to the other. Hence both `eta_I` and `P_I` agree. This is not a global agent permutation because the unequal `U` scores remain attached to their original agents. The full public laws differ. Choose the remaining two agents' scores to satisfy Proposition 1; every selector event is identical in these two preparations. This establishes noninjective handoff on the selection class, while retaining distinct children.

The exact inherited flow above is a transport-and-reweighting flow on the retained law. It has not been identified with a Fisher gradient on a regular parent statistical manifold. In particular, on finite samples the `L` atom locations move with the fine laws; their changing-support family cannot simply be declared differentiable in quadratic mean. No collective connection, stabilizer equality, or nonzero contextual residual tensor follows from Proposition 1. This is the principal geometric gap, separate from the absence of interaction in the chosen constitutive specialization.

## 2. A necessary condition for any later handoff

**Proposition 2 (selection must descend through the current retention).** Let `R:S -> Z` be an exact deterministic retention, including the accessible controller history and membership already acquired. Suppose the fine flow is unique, and a deterministic future handoff has first time `tau(x)`, event label `m(x)`, and posthandoff retained value `J(x)`. A deterministic parent initialized only from `R(x)` reproduces this marked handoff for every admitted fine initial state only if all three quantities are constant on every fiber of `R`. Conversely, if they factor measurably through `R`, and the posthandoff retained flow and responses are exact, the marked handoff and subsequent response histories descend.

*Proof.* Two states with the same parent initial condition give the same parent evolution and marked event. Exact reproduction therefore forces equality of their times, labels, and parent states after the event. Conversely use the three factorizations to define the parent event time, event label, and new initialization, then apply inherited flow uniqueness and the response-kernel identity after the event. Induction handles further handoffs. QED.

An announcing oracle that supplies a previously hidden event time adds a new input. It does not establish autonomous selection from the retained state. For stochastic readouts and policies, deterministic event equality is replaced by equality of the appropriate conditional joint event-and-state kernels; matching marginal event probabilities is insufficient.

There is a differential test. Suppose a first event is locally isolated and transverse, with smooth trigger `chi` and

$$
\chi(\Phi_{\tau(x)}x)=0,\qquad
D\chi_y B(y)\ne0,\qquad y=\Phi_{\tau(x)}x.
$$

Assume the no-earlier-crossing condition persists in the neighborhood. Implicit differentiation gives, for every `v` in `ker DR_x`,

$$
D\tau_xv=-\frac{D\chi_y D\Phi_{\tau(x)}(x)v}{D\chi_yB(y)}.
$$

Consequently a nonzero numerator prevents inherited autonomous timing. Adding the scalar event time to the retention repairs a single autonomous event only when its value is genuinely computable and remains sufficient for every admitted future control; it is not a general repair of controlled formation.

## 3. Serious failure test: a hidden-child distance breaks exact selection

The successful selector above uses the retained statistic. Replacing it by a nearest-descendant KL rule can fail even though the same exact associative quotient exists. The following example stays in the common-reference original-model specialization of Section 1, so every source row is nonempty and every derivative and rate is unchanged.

On three independent fair bits let `a(U)=1+alpha U`, `b(V)=1+beta V`, `h(W)=1+gamma W`, and `k(W)=1+delta_0 W`, with `alpha,beta>0` and `0<gamma<delta_0<1`. Compare the complete four-child preparations

$$
X=(ab,1,h,k),\qquad Y=(a,b,h,k).
$$

Take the already joined blocks `I={1,2}` and `J={3,4}` and use the vector-valued response observable `T=(U,V,W)` for their log-spectrum/sum parents. Swapping `V_1,V_2` under the product reference proves equality of the two `I` parents; the `J` parents coincide trivially. All four laws are distinct in either preparation. The same equalities hold throughout the exact inherited flow.

Define a proposed next-join score from the hidden children,

$$
d(I,J)=\min_{i\in I,j\in J}\operatorname{KL}(q_i\Vert q_j).
$$

Put

$$
\psi(z)=\frac{1+z}{2}\log(1+z)+\frac{1-z}{2}\log(1-z),
\qquad c(z)=-\tfrac12\log(1-z^2).
$$

Independence of the bit coordinates gives

$$
d_X(I,J)=c(\gamma),\qquad
d_Y(I,J)=c(\gamma)+\min\{\psi(\alpha),\psi(\beta)\}.
$$

Indeed `KL(f(U,V)||h(W))=KL(f||A_U tensor A_V)+KL(A_W||h A_W)`. The latter term is `c(gamma)`, and `c(delta_0)>c(gamma)`. The reference child in `X` has zero first term, whereas both children in `Y` have a strictly positive one.

Under the exact rate-`c=2` relaxation, each bit contrast evolves as

$$
z_t=\tanh(e^{-ct}\operatorname{atanh}z_0).
$$

Both displayed distances decrease strictly and continuously to zero. Choose any threshold `theta` with `0<theta<c(gamma)`. Their first crossing times are finite and satisfy `tau_X<tau_Y`, because the second distance is strictly larger at every finite time. More explicitly,

$$
\tau_X=c^{-1}\log\left(
\frac{\operatorname{atanh}\gamma}{\operatorname{arcosh}(e^\theta)}
\right).
$$

The denominator is positive and smaller than the numerator by the chosen threshold. Thus identical exact parent states require different later membership events. Proposition 2 rules out this selector. This is a failure of the proposed handoff, not a failure of the quotient's already proved flow or sample-sum responses.

## 4. Exact operational redundancy cannot first appear in finite analytic time

There is a further restriction on mechanisms claiming that the fine flow itself creates new exact response equivalence. Let `U` be a finite-dimensional analytic positive-law chart with analytic fine vector field `B`, and let `F` be a declared collection of real analytic functions `f:U -> [0,1]`. Each function is the probability of an event in a finite admitted experiment. Require the collection to include the same experiments after any sufficiently short interval of free evolution. Define `x ~ y` when `f(x)=f(y)` for every `f` in this collection. Domains must contain a common connected regular trajectory interval for each experiment used.

**Proposition 3 (finite-time equivalence is transported, not newly created).** For any two fine solutions `x_t,y_t` on a connected common regular interval, if `x_t0 ~ y_t0` at one time, then `x_t ~ y_t` at every time in that interval.

*Proof.* Fix an experiment probability `f`. Delay closure and equivalence at `t0` imply `f(x_t)=f(y_t)` on a nonempty interval immediately after `t0`. The difference is analytic in `t`. It vanishes on that interval, so the one-variable analytic identity theorem makes it vanish on the entire connected common interval. Apply this argument separately to every experiment. No countability assertion is needed for pointwise equality of all of them. QED.

For clarity, the analytic-flow fact used here has a local proof: extend the analytic vector field to a bounded holomorphic vector field on a sufficiently small complex polydisc. Its Picard integral operator is a contraction for sufficiently small complex time on a smaller polydisc. The iterates are holomorphic and converge uniformly, so their limit is holomorphic. Restriction to real time gives the required analytic solution, and continuation covers a regular trajectory interval. This use makes no boundary or global-existence claim.

The original finite-table potential and its Fisher field are analytic when the constitutive channels are analytic and all compared-law entries are positive. The logarithms, positive finite Gibbs sums, and inverse positive finite Fisher matrices are analytic there. Thus Proposition 3 applies to both the full and Gibbs-reduced original flow in this specialization. Fixed identity channels are included. Finite record alphabets with analytic kernel probabilities and analytic finite response/update compositions supply examples of admissible analytic experiments. Unrestricted smooth or merely measurable response maps are not covered.

If a retention introduced at time `t` preserves all these experiment laws, two states it identifies were already operationally equivalent when pulled back by the fine flow. This conclusion allows a dynamically selected hierarchy of preexisting quotients, as in Proposition 1. It rules out a finite-time first appearance of the corresponding exact observational redundancy. It is stronger than the prior obstruction for one fixed analytic retention on an open region, because no fixed retention or open preparation class is assumed here. It remains an analytic, interface-relative result and cannot refute the frozen smooth existential target.

The analyticity restriction is substantive. In an original local binary KL specialization, the logit coordinate can obey `dot z=1-z`; from `z(0)=-1` it crosses zero at `log 2`. Let a second logit obey `dot w=-w`. The smooth normalized output with success probability `1/2+epsilon b(z)tanh(w)`, where `b(z)=exp(-1/z^2)` for `z<0` and `b(z)=0` for `z>=0`, distinguishes different `w` values before the crossing and discards them afterward. This example uses an expressly manufactured smooth response gate and is therefore excluded as a target construction. It shows why analytic continuation cannot be promoted to a theorem about all smooth constitutive data.

## 5. Remaining obligation and decisive next action

The strongest positive result is exact, persistent, two-stage membership selection from a nonempty open class of general bounded positive laws, using a preexisting associative compression under uncoupled original KL relaxation. The newly selected object is membership; no new redundancy or attraction is generated at the handoff. The retained-statistic selector succeeds, while the nearest-hidden-child selector provably fails on exact parent fibers.

The unresolved target obligation is to replace the uncoupled specialization with an admissible interacting, sector-coupled realization that still has a genuinely compressive exact quotient, an observable selector with a proved later handoff, and regular inherited collective geometry. A proposed replacement should first verify the small interface identities `dot b_I=-c b_I` (or a comparably closed monotone selector), count-weighted joining, and the joint response kernels. It must then establish the actual coarse statistical manifold and the conditions `Delta(r_X,J xi)=0` and `ker J=ker J_bar`, with a nonzero contextual residual when nontrivial geometry is claimed. Existing log-spectrum laws alone do not discharge that last step. The positive mechanism is not a nonexistence proof and does not exclude smooth nonanalytic, invariant-stratum, asymptotic, or other admissible constructions.

Only analytical derivations and read-only source inspection were used. No simulation, symbolic or numerical calculation, GPU operation, Lean proof, or external-result invocation ran. This file is the sole route artifact edited by this worker; the parent should record it in the session change log.
