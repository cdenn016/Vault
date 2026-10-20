# Mathematical content of the three Theory documents

This file states what the main manuscript and its two supplements must contain, and the typed
constructions they rely on. `SPEC.md` in this folder governs the writing rules, the status system, the
notation, and the mechanics; symbols below follow its section 3 table. The destination of every
existing label, the file plan, and the cut list are in MultiAgentELBO
`docs/reviews/2026-09-23-theory-streamlining-review/phase2/PLAN.md` and `phase2/label-destinations.json`.
The content is condensed from sections 3 and 5 to 8 of the earlier spec and from its dated
consolidations (now in MultiAgentELBO `docs/research-log/theory-consolidations.md`), updated to the Phase 1
corrections and to the author's decisions D1 to D13. Reproduce these results faithfully; do not
weaken or overstate them. A result listed here keeps its proof unless the plan cuts it to a
checked primary-source citation. Where a statement below is quoted as a fact, its status in the
documents is ESTABLISHED at the stated hypotheses unless the text says STANDARD, OPEN, or
CONJECTURE.

## A. Main manuscript (`main.tex`)

### Part I. Single-point foundations

**Chapter 1, program, scope, and standing conventions.** The program aim is stated in the
manuscript's own vocabulary (D4): agents are local sections, collectives form through coupled
inference, and parents act back on children through normalized laws. The local-first architecture
(`eq:intro-local-to-global-architecture`) runs from local descriptive data to one normalized joint
`\mathbb P_{\theta,V}`, one selected correlated recognition coupling `\mathbb Q_{V,o,X}`, its
posterior slice `\boldsymbol\Pi_{\theta,V,o,X}`, and one ELBO; population laws are complete
probability objects, not additional agents. The reading map is ordered by Parts I to III and names
each supplement once as a document. The standing-conventions section carries the defaults of SPEC
R6, the declined claims of SPEC R5 (physical time, spacetime, agency, ontology, canonical
selectors, graph links as base transport, base maps, neighborhoods, connection descent), the
distinction between the inference index or RG depth and physical time, the three transports that
must remain distinct (pointwise frame comparison, independent graph link, base parallel
transport), the two uses of "coarse", and the convention on the interaction multigraph (D8, revised:
its copy set is a structural datum declared before the rows and contains the reversal closure of the
source-prior supports, with one-way attention; a mutually attending pair uses two distinct copies with
independent links, `\Theta_{ij}\neq\Theta_{ji}^{-1}` in general, forming the 2-cycle `i\to j\to i` with
holonomy `\Theta_{ij}\Theta_{ji}`, which belongs to the declared loop family of the generator prior once
based at each endpoint, so a large loop coefficient gives reciprocal links as a hard-constraint limit;
an agent-level self edge carries the identity link, while coarse loop copies carry internal holonomy).
The status table `tab:status-taxonomy` follows SPEC R4. The links are written in the exponential chart,
and in the latent-link model their Lie-algebra generators are latent coordinates with a normalized
prior, inferred jointly with the agents; held links whose twists lie in `\exp\mathfrak g` are the
zero-width limit of that model (Chapter 9, `prop:link-chart-image`).

**Chapter 2, geometry at one base point.** One principal bundle `\pi:\mathscr P_G\to\mathcal C`
induces the belief and model associated bundles
`\mathcal E_x=\mathscr P_G\times_{\widehat\rho_x}\mathcal B_x`; the representations `\rho_b,\rho_m`
may be inequivalent and act on fibers of different dimensions. At `c_*` the fiber
`(\mathscr P_G)_{c_*}` is a `G`-torsor. Each agent has one common frame `u_i` (D2, a gauge
choice). One passive re-expression convention `g_i` is fixed once. The active gauge group at one
base point is one copy of `G` inside the passive vertex group `\prod_iG`
(`prop:geo-active-image-point`); the per-vertex group of the link network is passive. Cross maps
`\Phi:\mathcal E_b\to\mathcal E_m` and `\widetilde\Phi:\mathcal E_m\to\mathcal E_b` are measurable
fiber-preserving morphisms over the identity; they are not principal-bundle morphisms, gauge
automorphisms, same-channel transports, or assumed inverses, and their existence is additional
structure. Equivariant fiber maps induce cross morphisms (`prop:geo-intertwining-cross-map`); a
nonzero linear cross map between inequivalent linear representations needs an intertwiner.

The interaction multigraph `\mathfrak I` at `c_*` carries independent links `\Theta^x_e\in G` on
oriented edge copies with `\Theta^x_{\bar e}=(\Theta^x_e)^{-1}`, transforming under vertex gauge
(`def:geo-graph-links`). The copy set, with parallel and loop copies admitted, is a structural datum
declared before the rows. A mutually attending pair uses two distinct copies, each with its own
reversal, so its links are independent (`\Theta_{ij}\neq\Theta_{ji}^{-1}` in general) and it forms the
closed walk `i\to j\to i` with holonomy `\Theta_{ij}\Theta_{ji}`. Endpoint notation `\Theta^x_{ij}`
denotes the link of the source copy `j\to i` of row `i`, and where no row is involved it is allowed
only for a unique copy. An agent-level self edge is a loop copy with the identity link; coarse loop
copies carry internal holonomy (`def:full-graph-coarse-links`). The link map
`\mathsf t^x_e(u_j\cdot g)=u_i\cdot\Theta^x_eg` of the fiber is frame independent and
right-equivariant, and `\mathsf t^x_e(\sigma)=\sigma\cdot\mathring\Theta^x_e` for the per-edge
twist `\mathring\Theta^x_e=U_i^{-1}\Theta^x_eU_j` relative to a reference point `\sigma`. Every edge
carries an invariant conjugacy class, and the invariant link content is the twist tuple modulo
one simultaneous conjugation (`prop:geo-edge-twist-invariance`). Links are graph-flat on a
subgraph exactly when every closed-walk product is the identity, equivalently when they are a
graph coboundary in arbitrary vertex potentials; frame-aligned links `\Theta=T` (the former
`hyp:geo-flat-links`, now a definition) are strictly stronger. Singletons and trees are
trivializing. The trivializing criterion carries the coboundary uniqueness clause
(`prop:geo-trivializing-criterion` with `prop:gauss-coboundary-trivialization`). Three notions are
pairwise independent and stated on law fibers: frame agreement (trivial holonomy over every
closed internal walk), law agreement on edges, and law coherence up to holonomy stabilizers
(`def:geo-law-coherence`, `prop:geo-three-agreements`, `eq:phil-law-coherence`). General `GL`
conjugation has no positive invariant norm on `\mathfrak{gl}(n)`; a positive construction needs
covariant SPD metric data. For compact `G` with unitary `\rho_x`, the normalized loop penalty
`\frac1{2n}\Tr((I-\mathsf U)^*(I-\mathsf U))` lies in `[0,2]`, so a finite nonnegative combination
of them against the product of Haar probability measures on the links has normalizer in
`[e^{-2\sum_p\mathrm c_p},1]` (`rem:geo-loop-penalties`); normalizability of that Haar-referenced law for noncompact or general
linear `G` is not asserted, while the generator chart of Chapter 9 supplies a normalizable prior for
every structure group with a declared inner product on its Lie algebra (`prop:link-generator-prior`). The running example has three agents on a triangle with nontrivial
loop holonomy, per-edge twist classes, one passive vertex change, and one record kernel.

**Chapter 3, probability semantics at `c_*`.** Kernels come first and densities second, on
standard Borel spaces; density presentations use declared reference measures. A mixed family's
common domination is characterized by `thm:prob-mixed-family-common-domination`, proved in the
measure appendix. The access map
`\operatorname{Acc}_i:\mathsf O\times\mathsf X\to\mathsf I_i` and the local kernel `\mathbb Q_i` give
`\mathbb Q_{i,o,X}=\mathbb Q_i(\operatorname{Acc}_i(o,X),\cdot)`; access restricts local laws only,
and decentralization also requires a selector indexed by `((\operatorname{Acc}_i(o,X))_i,X)`. The
coupling selection is declared once (`hyp:prob-measurable-coupling-selector`, absorbing
`def:elbo-recognition-kernel` and the constrained-selection hypotheses):
`\mathbb Q_{V,o,X}\in\operatorname{Cpl}(\mathbb Q_{\bullet,o,X})`. A model presentation `m_i` is
not a law; its generative meaning comes through a measurable evaluator
`\operatorname{ev}_i:m_i\mapsto K^X_{i,m_i}`.

Three levels are declared (`def:prob-description-levels`): samples, law points `\mathfrak q_i^x` in
`\mathsf Y^{\mathrm{law}}_i`, and configurations `(w,y)` with a presentation map `\operatorname{pres}`
and presentation kernel `\kappa^{\mathrm{cfg}}`. Every energy names its level. Transported
divergences `\KL(q_i\Vert(\Theta_e)_\#q_j)` are law-point energies; by strict convexity of
`-\log` no recognition-independent sample energy reproduces them at two source laws and one strict
mixture. Point-mass recognition of a non-atomic law point has infinite cost
(`prop:prob-law-point-point-mass`); the configuration lift has its identity
(`prop:prob-configuration-lift-identity`); the prior over law points is `open:prob-law-point-prior`.
The access-gap floor (`eq:prob-access-gap-floor`) uses the corrected Chernoff value. The one KL
chain rule (`lem:prob-kl-chain-rule`) is stated in `[0,+\infty]` in disintegration form, with
product-reference and fixed-marginal corollaries, the extended data-processing clause
(`thm:cg-kl-dpi-extended`), and bijection invariance (`eq:cg-rn-bimeasurable`,
`eq:cg-kl-bimeasurable-invariance`); it is STANDARD only with checked locators (Kullback 1951 and
Csiszár 1967 for data processing; Gray or Pinsker for the chain rule), otherwise ESTABLISHED with
its proof in the measure appendix. Parameterized posterior disintegration is
`prop:prob-parameterized-disintegration`. The joint-measure evidence chain
`prop:prob-measure-evidence` needs no likelihood densities; a scalar evidence bound needs only
domination of the record marginal, with the reference and null-version distinctions of
`rem:prob-measure-reference`. Local energy presentations for nondominated record kernels remain
`open:prob-nondominated-likelihood`. Finite designs, sampling compatibility, and continuum law
theory go to Supplement B.

**Chapter 4, the fixed normalized generative law.** The constructed joint
`\mathbb P_{\theta,V}(dy,do\given X)` is normalized on arbitrary interaction cycles
(`prop:gen-exact-normalization`); each record kernel `K_a` is owned once by the joint, while
coordinate-local free energies include every incident factor. The typing prohibition (a standing
hypothesis, label `req:gen-typing-prohibition`) is stated in two-argument form `F(Q;\theta)`: a
generative kernel is fixed once `(\theta,X)` is fixed and takes no recognition law, recognition
parameter, or posterior as input; this bans `\theta(Q)` inside one evaluation and admits accepted
M-coordinates and model-channel recognition dynamics. The finite directed latent law (label
`cons:gen-finite-directed-law`) becomes a definition. One sentence types the fast and slow
variables and cites the two-timescale chapter.

**Chapter 5, one evidence bound and local-collective free energy.** Under
`hyp:elbo-evidence-domain` (finite positive evidence; clause (H3) absolute continuity
`\mathbb Q_{V,o,X}\ll\boldsymbol\Pi_{\theta,V,o,X}`; log-integrability),
`\log p_{\theta,V}(o\given X)=\Lelbo_V(\mathbb Q_{V,o,X};X,o)+\KL(\mathbb Q_{V,o,X}\Vert\boldsymbol\Pi_{\theta,V,o,X})`,
with equality exactly when the selected coupling equals the posterior slice as measures. The
extended ELBO assigns `-\infty` to the singular branch, which is what excludes recognition laws
supported on subspaces. Reciprocal participation occurs in inference under a fixed normalized
joint. The total-correlation chain rule, the E-coordinate, the local VFE, and the local-global
potential identity follow from the Chapter 3 chain rule: with the outside marginal fixed, the
block objective is the outside-averaged conditional VFE, and its differential equals that of the
collective VFE restriction under the stated support, finiteness, integrability, and
differentiation hypotheses. Observations enter as interactions through the record-density
presentation (`hyp:local-interaction-kernels`); accepted M-coordinates are the slow update; the
damped block update is `eq:obs-damped-block-update`. Since the acceptance inequality is weak, the
null step is an accepted M-coordinate, so `open:elbo-alternating-convergence` is posed for finitely
many latent states, parameters in an open cone, `C^2` joint densities, and the exact M-coordinate
with a unique maximizer: conditions checkable on the model, met by some model of parameter
dimension at least two whose stationary set at the limit value of an orbit is not discrete, that
give convergence of every orbit to one stationary point, or an orbit with more than one limit
point under compact upper level sets. Both chapter labels `ch:elbo` and
`ch:local-collective-elbo` are kept. The measure-level extension keeps block descent and
incident-record locality without record densities (`prop:elbo-measure-block-descent`).
`prop:elbo-nondominated-record-witness` separates finite posterior KL from infinite prior KL;
`prop:elbo-record-event` gives finite-resolution event evidence without asserting TV convergence
to point conditioning.

**Chapter 6, attention and selective communication.** The copy set of the interaction multigraph is
a structural datum declared before the rows (`def:obs-attention-label-model`); it contains the
reversal closure of the union of the row supports of `\pi` (D8, revised), and a model may add further
copies (the triangle-chain bridges of Chapter 14 are such added copies). If row `i` reads `j` through
`e:j\to i` and row `j` reads `i` through `e':i\to j`, then `e'\neq\bar e`, the links
`\Theta_{ij}:=\Theta_e` and `\Theta_{ji}:=\Theta_{e'}` are independent, and the pair forms the closed
walk `(e,e')` with holonomy `\Theta_{ij}\Theta_{ji}`. A self edge, when the model includes one, is a
loop copy carrying the identity link at the agent level. Energies are typed at the description level
of the declared model (sample, law point, or configuration); `D_{ii}=0` is a consequence of the
identity self link for energies that read the transported residual or a transported divergence
vanishing at equal arguments, not for energies with distinct query and key maps, and it fails in
general on coarse loop copies with nontrivial holonomy. Each support is
complete unless masked and need not be symmetric (one-way attention), and each attention row is
strictly positive on its own source set when its costs are finite; discrete
edge creation and deletion is `open:obs-edge-creation` (the grand-canonical program note is
motivation only); the open problem fixes a threshold rule (deletion at a rate reading the
recognition row weight, creation at a rate reading the averaged comparison energy, bounded
multiplicity) and asks for a normalized joint with the source sets as a structural coordinate whose
collective VFE the rule's master equation does not increase, or a proof that for every such rule
none exists. In the per-receiver source-label model the source prior `\pi_{ij}`, the
generative posterior row `\beta^P_{ij}`, the recognition row `\beta^Q_{ij}`, the receiver
occupancy `\alpha^x_i`, and the event law `\eta=\alpha\beta` stay distinct. The law defining
`\alpha` is declared: a structural selection law in the per-receiver model, or the receiver
marginal of one joint edge label in the single-edge model (`hyp:rg-single-edge-attention`, a
definition). A product-of-rows label model fixes receiver occupancy, so `\alpha` needs a null
label or a different joint label model with its own likelihood. Rows are indexed `(i,h)`; `\eta`
carries no head index. The exact one-scale `H`-head receiver update is proved
(`prop:obs-selective-receiver-update`(f), below), and the label-level recursion across scales is
`open:obs-multihead-attention`, posed for heads
whose projected queries are correlated under the receiver's conditional Gaussian law and whose
integrated positive label table does not factor. Query covariance alone does not force label
coupling; `rem:obs-head-coupling-criterion` gives the exact two-head criterion for
label-independent predictive covariance, and `prop:obs-selective-head-coupling` supplies an instance.
The factorizing subclass, including untied channel-split heads under a channel-product receiver law,
is excluded; the
problem asks for an exact recursion with bounded head count through a declared head-merging channel,
or a block whose posterior mean no comparison-record model with fewer heads than rows reproduces. Events,
rows, links, and divergences are indexed by oriented edge copies, and pair quantities are sums
over copies. The row results are the Jensen-gap identity, row potentials, the affine row, the
joint rate, the reduced potential and reduced Hessian (`prop:obs-attention-reduced-hessian`), the
constant row gap (`prop:obs-attention-constant-row-gap`, whose random-source clause is stated for row
`i`'s source copy and has a self-copy clause: at the identity self link the self logit is raised by
`\Tr(W_i\operatorname{Cov}Y_i)/(2\tau_i)`, so the receiver's own uncertainty penalizes every other
source and not the self copy), and the replicator flow with its dissipation. Exact coarse attention pushes
`\eta`; `\alpha` is recovered by marginalizing `\eta` and `\beta` by disintegration on positive
occupancy; a conditional row alone is not recursive state.

Selective communication adds normalized encoder, transmission, and decoder kernels with explicit
receiver side information `\Upsilon`. Vector sample fibers are distinct from law fibers. The
linear factors compose to `\mathsf L_e=\mathsf L^{\mathrm{dec}}_e\mathsf L^{\mathrm{tr}}_e\mathsf
L^{\mathrm{enc}}_e`, and the composed Markov kernel is `K^v_e`, not `\mathsf L_e`; message-coordinate
changes cancel between factors, and sample coordinates use the Chapter 2 convention. Links stay
invertible with inverse reversal; a singular communication map is not a group element and a
singular loop product is not holonomy. The edge factor `F_e=\mathsf L_e\rho_x(\Theta^x_e)^{-1}`
exists once an invertible link is chosen, and one shared receiver map is an extra condition.
Encoding kernels and quotients are intrinsic; an orthogonal sending complement requires a metric;
the signal image `\operatorname{im}\mathsf L_e` may be smaller than the decoder image.
Role-comparison cospans do not supply a decoder, and the metric lift, the Gaussian conditional
mean, and the natural-gradient insertion are distinct operations. Keep the shared
comparison/content conditional correction, the content conditional-KL term, and the posterior
versus recognition row distinction. The dot-product reduction requires shared projected key
covariance and keeps its key-norm bias unless an explicit condition cancels it; the quadratic
disagreement and its response stay in the core. The exact comparison-record receiver update
(`prop:obs-selective-receiver-update`) ties the value map to the query and key maps; it is distinct
from the metric lift (its noiseless limit) and from the natural-gradient insertion. Its sources are
`j\neq i`, and it has six parts: (a) the weights, components, and conditional mean; (b) the
comparison-record weights in dot-product form (`eq:obs-selective-record-dot-product`), a dot-product
logit plus a key-norm bias in the metric `(\Sigma^{\mathrm{pred}}_i)^{-1}`, which contains the
receiver's covariance; (c) the Woodbury identity and the metric-lift limit; (d) copy-dependent query
maps or precisions on a common comparison space, where distinct comparison spaces need a declared
common record space; (e) a self copy, with weight and component `eq:obs-selective-self-component`,
which for tied query and key maps is an attention sink with factor
`\det(I+\widetilde W_iS^Q_i\Sigma_iS_i^{Q\top})^{1/2}` (`eq:obs-selective-self-sink`) and residual
weight `w_{ii}I+(1-w_{ii})\Sigma^+_i\Sigma_i^{-1}`, leaving the mean unshrunk; and (f) the exact
`H`-head receiver update (`eq:obs-selective-multihead-update`, covariances
`eq:obs-selective-multihead-covariances`), the operator form of `eq:obs-selective-attention-residual`
with per-head rows the head marginals of a coupled label table rather than separate softmax rows. The
kernel-level passive law is `eq:obs-selective-kernel-gauge`. The theory defines three attention rows
(the generative posterior row, the constant recognition row, and the predictive-covariance row of the
comparison-record model), and the text before the table names them without choosing one. The
transformer correspondence table (`tab:obs-transformer-correspondence`) gives row standing as table
content (SPEC R4); each row names its model (label, law-point, or comparison-record), the query and
key row has a comparison-record entry, a positional-encoding row reads ALiBi as `\log\pi_{ij}`
(derived) and rotary embeddings as a coboundary twist of the comparison space (declared), the value
row covers one receiver given its sources' states, and the multi-head row reads "derived at one scale,
recursion open". Normalized
cyclic records instantiate fixed rectangular maps but settle neither canonical compression nor
moving-interface coarse-graining. Conditional data processing uses receiver side information; rank
is not capacity; a common measurement KL leaves a private conditional KL; evolving measurements
need the extra derivative term in their projectability identity. Interface learning, private
retention, and source or history closure are open: `open:obs-selective-formation` is posed for a
vector-tier block with surjective interfaces of one fixed rank learned as generative parameters at
mobility `\epsilon_{\mathrm M}` under the kinetics of `def:rg-formation-cycle-experiment`, and asks
for a retained-mechanism parent of fixed dimension below the block's whose path relative entropy
vanishes on horizons of order `1/\epsilon_{\mathrm M}` uniformly in the temperature, or a learned
rest point or lower bound that excludes one. The linear Gaussian record goes to Supplement G.

The finite complex-message intensity record (`thm:obs-intensity-born`) includes a null outcome
and a common bound on every transported emission. With setting-independent positive emission
moment and detector total it gives a setting-independent click rate and a Born-form conditional
table with globally positive, normalized effects. Its passive covariance transforms emissions,
detectors, and the link together (`prop:obs-intensity-gauge`). Random links are weighted by their
click rates (`cor:obs-intensity-random-link`); a law with unbounded scalar link directions does
not satisfy the fixed-efficiency hypothesis. The distinction between generated records,
accessible recognition registers, and later feedback (`rem:obs-intensity-access`) uses the
existing access maps and leaves collective incident-record descent unchanged. These are
specialized observation kernels, not a selection theorem for quantum dynamics.

**Chapter 7, fiber information geometry and inference histories.** Law fibers and kernel fibers
are distinct; neither a manifold, a dominating measure, an affine chart, a cone, nor a Fisher
metric is inferred from the word belief or model. The standing tier is a finite-dimensional
regular statistical manifold with a `C^1` positive-definite metric, or its constant-rank Fisher
quotient (differentiability in quadratic mean, square-integrable scores, the integrability each
tensor needs, and nondegeneracy before a Fisher form is called a metric); the Gaussian mean tier is
an example. Vertical Fisher and Amari–Chentsov tensors are invariant under the represented action;
the orbit Fisher form `\mathfrak k_q` and isotropy algebra `\mathfrak g_q`
(`cor:pb-orbit-fisher-form`), KL jets, and the vertical defect cocycle are single-point results.
The phase application (`prop:pb-phase-visibility`) identifies phase information with the
central-generator orbit Fisher form and distinguishes invariance of the second moment from
invariance of the full law. Its smooth non-Gaussian example has zero mean and pseudo-covariance,
a phase-sensitive fourth mixed moment, and finite positive phase information. It imposes no
Gaussian restriction on the channel models and introduces no base connection.
The Markov coarse-morphism hypothesis (`hyp:pb-markov-morphism`) carries no common-domination
clause. The invariance characterizations of the Fisher metric (`prop:ig-fisher-characterizations`,
STANDARD) state Cencov's theorem as uniqueness, up to one positive factor, of the family of continuous
metrics over the simplices of all finite sets under congruent Markov embeddings between simplices,
cited to Cencov 1982 Theorem 11.1 as restated in Ay–Jost–Lê–Schwachhöfer 2015 Proposition 3.19(3).

The Fisher contraction theorem (`thm:cg-fisher-contraction`, section 7.3; Chapter 10 cites it): a
parameter-independent normalized record channel replaces a score by its conditional expectation
and contracts Fisher information by the exact conditional-covariance defect. It applies to the
coarse image of the same fine orbit and does not compare independently recomputed orbits without
an oriented semiconjugacy; a parameter-dependent channel, a fitted coarse approximation, and a
generative-versus-recognition parameter mismatch lie outside it. Galerkin aggregation is inside it
along fixed-precision histories and outside when `\operatorname{range}(\Lambda S)` changes, because
the Galerkin law is a `\Lambda`-dependent pushforward (`prop:ig-galerkin-pushforward`, Supplement G).
For the retained-law map `\operatorname{ret}` and a positive-semidefinite target tensor `g`,
`\operatorname{rad}(\operatorname{ret}^*g)=d\operatorname{ret}^{-1}(\operatorname{rad}g)`, equal to
`\ker d\operatorname{ret}` exactly when `\operatorname{im}d\operatorname{ret}` meets
`\operatorname{rad}g` trivially; constant rank gives a positive-definite quotient bundle, not a
quotient manifold, and under transversality and a regular connected-leaf quotient the pullback is
basic. This does not make arbitrary tensors or declared block projectors basic.

VFE selects an orbit only after a metric or mobility is declared: on a regular (quotient) metric
configuration space the positive ray of `-\operatorname{grad}\Fenergy` is the oriented
unparameterized natural-gradient orbit; scalar mobility changes only the parameterization,
anisotropic mobility can change the orbit, and a semidefinite metric is not inverted before a
justified quotient. An exact multi-agent VFE needs a joint-law lift: a smooth extraction map with a
smooth right inverse `\iota_i` reproducing the configuration; the recognition Fisher metric is the
pullback along `\iota_i`, and a weighted sum of marginal metrics is exact only after a
block-orthogonality result. `hyp:hist-exact-vfe-lift` also defines an equivariant exact lift (a
declared represented action that preserves the joint metric, intertwines the extraction map and
`\iota_i`, and is compatible with the outside-marginal frames); the channel-weighted and block-diagonal
metrics are frame independent, while the exact-lift metric is frame independent only for equivariant
lifts and is otherwise frame relative. The parity witness: for three paired binary agents,
`p_\varkappa=p_0+\varkappa\chi D` with `|\varkappa|<1` is a strictly positive normalized smooth right
inverse of the six one-bit marginal map and an immersion; every proper marginal is the product
marginal; for each marginal tuple it is one parity line in the 57-dimensional Fréchet fiber; it is
equivariant under simultaneous complement of both channels of an agent and typed agent
permutations, while an odd independent channel complement flips the sign of `\varkappa`. For a
regular joint score,
`\mathsf G_J-\mathsf G_w=\mathfrak K-\mathfrak C+\sum_i(1-w_i)\mathsf G_i` with
`\mathfrak K=\E[RR^\top]` and `\mathfrak C=\sum_{i\neq j}\E[L_iL_j^\top]` over the marginal scores; in
the witness `\mathfrak C=0` and `\mathfrak K\succ0` for `\varkappa\neq0`, and at the symmetric point
with hyperedge correlation `\varkappa/64` the joint metric is `4I_6/(1-(\varkappa/64)^2)`, so equality
with a weighted marginal metric needs every `w_i=1/(1-(\varkappa/64)^2)`. The symmetric posterior is
realized by an engineered hyperedge record. Promoting `\varkappa` gives full-joint rank seven against
singleton rank six with kernel `\operatorname{span}\{\partial_\varkappa\}`
(`cor:hist-promoted-parity-rank`). Full-joint VFE and Fisher tensors do not factor through singleton
marginals (`thm:hist-correlated-refinement-nogo`, `prop:hist-parity-hyperedge-vfe` with excess
`-\tfrac12\log(1-(\varkappa/64)^2)`, `cor:hist-parity-fisher-residual`).

Canonical dependence selection: naturality under fixed-arity coordinatewise finite Markov kernels
with independently tensored channel randomness forces the product section; on a wide
marginal-compatible category a natural section exists exactly when every added morphism preserves
product laws. The absolute selector natural under both declared split kernels (split parameters
`1/3` and `1/2`, pushforward atom multisets `\{1/3,1/3,1/6,1/6\}` and `\{3/8,3/8,1/8,1/8\}` from one
fair/fair marginal datum) is refuted, an ESTABLISHED negative result. The relative replacement is
the reference-relative I-projection (existence exactly when the moment lies in
`\operatorname{conv}T(\operatorname{supp}p)`, uniqueness, support on the minimal face; cut to
Csiszár 1975 if the locator is checked) and the deterministic reference completion
`r(f(x))p(x)/(f_\#p)(f(x))` (a consequence of the chain-rule lemma), composing along nested maps;
retained-optimizer descent requires retained equivalence, meaning equal retained posterior
`f_\#p` and evidence.

The Fisher duration `\mathfrak t` is Fisher length on an already selected orbit, invariant under
orientation-preserving reparameterization; it can stall on null or critical segments. An
orthogonal clock is locally a decreasing function of `\Fenergy` and exists exactly when
`\Vert\operatorname{grad}\Fenergy\Vert` is locally a function of `\Fenergy` and the period condition
holds; a non-orthogonal unit-speed clock exists given a global cross-section
(`prop:hist-cross-section-clock`). Record clocks, analytic finite duration, and discrete histories
are single-point results; the core states that no parameter-independent Markov kernel realizes the
joint barycenter of two normal laws and names Supplement G for the proof. Semiconjugacy: functional compatibility
forces basicness; natural-gradient sufficiency covers symmetry quotients; for
information-discarding maps the exact route is the reduced slow flow of Chapter 8, with the
finite-rate limit open. New units: `def:hist-configuration-manifold`,
`def:hist-coarse-configuration-map`, `open:hist-meta-clock-ratio`,
`open:hist-retained-fisher-quotient`.

**Chapter 8, two-timescale dynamics.** Repeated source draws have an exact native
evidence score and count-normalized natural learning drive under the declared
complete-prefix categorical Fisher metric (`prop:obs-native-source-drive`). The
recognition drive differs by its expected-count error. Conditional contraction in
one common metric gives a moving-prior estimate (`prop:obs-moving-prior-tracking`);
for the conditioned law of `prop:link-compact-comparison`, the native count bound
charges the endpoint tail once (`cor:obs-conditional-count-tracking`). These results
cover deterministic schedules. Positive finite label-pattern likelihoods give
an explicit Lipschitz constant for the native prior field and a finite-time
trajectory comparison (`prop:obs-source-finite-time-learning`); its possibly
large constants supply no useful long-time or growing-network stability or
formation result. A fast-slow coordinatization
(`def:obs-fast-slow-blocks`) maps `(f,s)`, `s=(s_{\mathrm m},\theta)`, to a population recognition law
and generative parameters, with objective `F(f,s)` the extended VFE with its generative argument
explicit. The envelope identity and reduced slow flow (`lem:obs-envelope-slow-flow`) use
`F_{\mathrm{red}}(s)=\min_fF(f,s)`; the rate-separated flow with
`\mathsf G_\varepsilon=\varepsilon\mathsf G_{\mathrm f}\oplus\mathsf G_{\mathrm s}` and its reduced
semiconjugacy is `prop:obs-rate-separated-flow`. A correlated belief-model metric requires the rate
declaration to name its slow manifold, `open:obs-slow-manifold`. On the four-cycle,
`prop:obs-slow-model-link-dichotomy` moves belief means at rate one, model means at a supplied rate
`\varepsilon_{\mathrm m}`, and links at `\varepsilon_\omega` (in the latent-link model, the rate-separated flow with the
generator recognition means in the slow block, `rem:link-rates`): on a held matching the mean flow is the
rate-separated flow, whose selected-edge blocks meet the three slow-manifold hypotheses with
constant 4 uniformly in the temperature while the full sheet has curvature `3\mathrm T` along the
pair means; at zero temperature a fast link or fast model means remove the model disagreement at
rate at least `4-2\sqrt2`, while slow means and links give a belief-agreeing, model-disagreeing
interval from `\frac14\log(4/\varepsilon_{\mathrm m})` to `1/(12\varepsilon_{\mathrm m})`; and a model
residual of size one persists along every assignment path up to a time of order
`1/\varepsilon_{\mathrm m}`. Outside the three arms the bound `eq:obs-cycle-general-slow-rate`
brackets the slow rate and bounds the decay of the model residual for rates in `[0,1/2]`, so a
model-disagreeing interval of order `1/\varepsilon_{\mathrm m}` requires
`\varepsilon_\omega=O(\varepsilon_{\mathrm m})`. `open:obs-slow-manifold` is posed for the sampled four-cycle dynamics
with source jumps and slow model means and links, asking for a tracking bound explicit in
`\varepsilon_{\mathrm m}`, the temperature, and the number of assignment changes, holding for
every positive bound on the number of changes per unit slow time, or a tracking failure at some
such bound; the learning case lies outside its class. The local natural-gradient section
moves here. Simultaneous block updates (`rem:obs-simultaneous-block-updates`, ESTABLISHED): blocks
that share no record and are conditionally independent under the baseline, updated at once, equal a
sequential sweep in any order; in conditionally conjugate exponential-family strategies,
mean-coordinate damping satisfies both inequalities of `eq:obs-damped-block-update`, while
natural-coordinate damping still descends but can violate the chord bound (Poisson witness);
simultaneous natural damping with weight `w` is the explicit Euler step of the Fisher block flow
`eq:obs-local-natural-gradient`, and the three-agent Gaussian witness `eq:obs-simultaneous-witness`
shows simultaneous best responses increasing the free energy (factor `36/25` on the mean term), the
weighted update increasing it along the all-ones direction exactly when `w>10/11=2/c_G`
(`eq:hist-discrete-descent-bound`). The memory-inference
descent (`thm:rg-memory-inference-descent`(iv)) is stated for the marked sweep on `q(x)\psi'`, and its
equality characterization includes `\psi'=\psi`. The prepared-parent semiconjugacy `JT=LJ` is the instantaneous-equilibration case: the
Markov property of a prepared parent rests on the instantaneous within-parent refresh hypothesis
(`hyp:rg-memory-instantaneous-refresh`), not on preparation alone; partial refresh gives a
non-Markov parent whose closure cost is `D^{(1)}_N` (`eq:rg-memory-partial-refresh-witness`).

**Chapter 9, Lie-algebra links as latent fields.** The links of Chapter 2 are written in the
exponential chart at the reference point: a generator family `\mathring\omega^x` on one orientation
`E_+` of each reversal pair, in the link space `\mathscr T=\mathfrak g^{E_+}` (per channel), with
twist `\mathring\Theta^x_e=\exp\mathring\omega^x_e`, link
`\Theta^x_e=U_i\exp(\mathring\omega^x_e)U_j^{-1}`, and `\mathring\omega^x_{\bar
e}=-\mathring\omega^x_e` (`def:link-exponential-chart`, `lem:link-exp-naturality`). A mutually
attending pair reads two distinct copies, hence two reversal pairs with independent generators in the
two directions, and with one copy per ordered pair the link space has dimension
`N(N-1)\dim\mathfrak g`. Passive
re-expressions leave every generator unchanged; a reference change acts on all generators by one
`\operatorname{Ad}` map and an active automorphism by another (`prop:link-generator-gauge`). The
chart covers exactly the families whose twists lie in `\exp\mathfrak g`; for `\GL^+(K)` this is a
proper subset by Culver's real-logarithm criterion (`prop:link-real-logarithm`, STANDARD with Culver
1966 Theorem 1), while reference holonomies of chart links reach all of `\GL^+(K)`
(`prop:link-chart-image`). Every continuous class function on `\GL(K,\R)` or `\GL^+(K)`, `K\geq2`,
is blind to unipotent elements (`prop:link-class-function-blindness`), so no continuous
conjugation-invariant penalty vanishes only at the identity (`cor:link-no-invariant-defect`). The
loop defect `\mathfrak Q^x_p` of a closed walk, measured with the declared fiber metric
(`def:link-loop-defect`, `lem:link-trace-form-scale`), is nonnegative with zero set
`\rho_x(\mathring\Theta^x_p)=I`, passive invariant, invariant under reference changes by nonzero
multiples of metric isometries (and under every reference change once the metric is transported),
half the invariant penalty of `rem:geo-loop-penalties` when the metric at the base vertex is the
frame image of the reference metric, `\dim\mathbb V-\Tr` on isometries, and quadratic in the cycle
map `\mathbf C` with an explicit cubic remainder bound (`prop:link-loop-defect`). The generator
prior is a Gaussian base law with anchor `\mathring\alpha^x_e` and covariance `\mathring\Sigma^x_e`
(generative parameters) tilted by `\mathscr S=\sum_p\mathrm c_p\mathfrak Q_p`; its normalizer
satisfies `e^{-\E\mathscr S}\leq Z_{\mathscr S}\leq1` for every Lie group with a declared inner
product on its Lie algebra, compact or not, so the hypotheses of `prop:elbo-random-link-vfe` hold
(`def:link-generator-prior`, `prop:link-generator-prior`). Walks of the loop family carry their base
vertex, and by default the loop family contains, for every mutually attending pair, the 2-cycle
`(e,e')` based at `i` and `(e',e)` based at `j`. The two based 2-cycle defects vanish together, exactly
at reciprocal links `\Theta_{e'}=\Theta_e^{-1}` (injective `\rho`), and the prior mass of
`\{\mathfrak Q_p\geq\epsilon\}` at `\mathrm c_p=\mathrm c` is at most
`\mathrm m_\epsilon^{-1}e^{-\mathrm c\epsilon/2}` (`eq:link-reciprocal-limit`), so a large 2-cycle
coefficient concentrates the prior on reciprocal links: the one-reversal-pair convention is the
hard-constraint limit, claimed in this defect sense only (`rem:link-reciprocal-limit`, ESTABLISHED).
The exponential on `\mathfrak{gl}(K,\R)` is not injective (`rem:link-chart-injectivity`, ESTABLISHED):
generator families giving one link have posterior density ratio equal to the base-density ratio;
`\exp` is injective on the principal domain `\mathring{\mathcal D}` of generators whose eigenvalues
satisfy `|\operatorname{Im}\lambda|<\pi`; with skew-symmetric part `\mathring\omega_{\mathrm{sk}}`,
`\max_k|\operatorname{Im}\mathring\lambda_k|\leq\Vert\mathring\omega_{\mathrm{sk}}\Vert_{\mathrm{op}}` and
`\sum_k(\operatorname{Im}\mathring\lambda_k)^2\leq\Vert\mathring\omega_{\mathrm{sk}}\Vert_{\mathrm F}^2`;
under the base law `\mathcal N(\mathring\alpha_e,\mathrm s^2\mathrm{Id})` with `\mathsf G^{\mathrm{fib}}=I_K`
the mass outside `\mathring{\mathcal D}` is at most
`\pi^{-2}(\Vert(\mathring\alpha_e)_{\mathrm{sk}}\Vert_{\mathrm F}^2+\tfrac12K(K-1)\mathrm s^2)`; Gaussian
generator recognition is read on `\mathring{\mathcal D}` (a new symbol in `tab:link-notation`). The abelian translation links of the
formation chapter are the instance `G=(\R^d,+)`, with an exactly quadratic defect; the
triangle-chain prior is not claimed as an instance (`prop:link-translation-instance`,
`rem:link-running-example`). The latent-link model types the generators as a root latent block under
the typing prohibition (`def:link-latent-model`); it is normalized and its free energy is
`\KL(R\Vert\text{prior})` plus the `R`-average of the held-link free energy
(`prop:link-latent-normalization`, `lem:link-growth`), with a closed form for Gaussian generator
recognition (`prop:link-gaussian-recognition-vfe`). The field equation (`lem:link-exp-derivative`,
`lem:link-gaussian-gradients`, `prop:link-field-equation`) states mean and precision stationarity,
with the current entering through the adjoint Frechet derivative of the exponential; its point limit
concerns the stationarity conditions only, and point masses are inadmissible. For a linear-Gaussian
comparison record the current is the precision-weighted prediction error times the source state plus
a cross-covariance term minus a source-covariance term, with an attention-gated form
(`cor:link-delta-rule`); the correspondence with the delta rule is one of form. Law-level
transported divergences are invariant under the stabilizer double cosets, with the Gaussian
stabilizers and the Mahalanobis criterion for exact transport, and their Hessian is the orbit Fisher
form only at exact transports (`prop:link-law-level-energy`). Without the prior, the sample-level
minimizer under product recognition has rank at most one, stationary generators exist at folds of
the chart, the chart infimum equals the singular minimum exactly when
`\mu_j^\top\Sigma_j^{-1}\mu_i\geq0`, and for `K=2` in the negative case it is not attained; the
prior restores coercivity (`cor:link-prior-necessary`). Held links whose twists lie in `\exp\mathfrak g`
(all of them for `SO(K)`, `prop:link-chart-image`) are the zero-width limit of the latent model for a
declared recognition class, with concentration of the link recognition at the
anchor (`thm:link-held-limit`); statements proved at every held link value transfer to the
conditional laws given the generators, and mixture statements do not
(`prop:link-conditional-transfer`). Directed record extensions induce no link action, while jointly
normalized undirected matter induces `\mathscr S^{\mathrm{ind}}=-\log Z` whenever the joint
normalizer is finite, which can fail although `Z_{\mathscr S}\leq1` (`prop:link-induced-action`).
The Gaussian generator recognition family is a regular statistical manifold; the joint
natural-gradient flow is a free-energy ray of the inference histories, first order, with free energy
decreasing at the squared gradient norm, and its explicit Euler step is the Gaussian Bayesian
learning rule with a descent bound (`prop:link-recognition-flow`). The anchor M-coordinate is moment
matching through `-\log Z_{\mathscr S}` and reduces to the recognition mean when `\mathscr S=0`
(`prop:link-anchor-m-coordinate`). The normalizer `\log Z_{\mathscr S}` is recognition independent, so
it cancels in inference at a fixed prior, and it is needed for the bound value and for the anchor,
covariance, and loop-coefficient M-coordinates; it is convex in the loop coefficients with
`\partial\log Z_{\mathscr S}/\partial\mathrm c_p=-\E_{\mathbb P}[\mathfrak Q_p]`,
`\log Z_{\mathscr S}(\mathrm c)=-\int_0^1\sum_p\mathrm c_p\E_{\mathbb P_{t\mathrm c}}[\mathfrak Q_p]dt`
(`eq:link-normalizer-integral`), and `-\E_\nu\mathscr S\leq\log Z_{\mathscr S}\leq-\E_{\mathbb P}\mathscr S`
(`rem:link-normalizer-role`, ESTABLISHED). The supplied link rate of the two-timescale four-cycle is the
rate-separated flow with generator means in the slow block (`rem:link-rates`). Generator histories
over learning episodes carry a Gibbs prior whose kinetic term is the defect of time-like loops with
mass `\mathbf m` under static frames (`def:link-history-prior`); it is normalized, Markov with
Gibbs-conditional transition kernels, a latent route of `def:full-graph-episode-joint`, and in
temporal gauge (`prop:link-history-prior`). The most probable history obeys a discrete Newton
equation in the inverted potential, with a monotone kink between the wells of a one-dimensional
double well (`prop:link-map-inertia`), and the linearized operator `\mathbf K`, made of the anchor
precision, the cycle-space curl term, the episode second difference and the matter term, is bounded
below by the anchor precision, so the linearized history is unique
(`prop:link-linearized-equation`). The loop term vanishes on the exact and harmonic generators of the
two-complex declared by the loop family, whose dimensions are counted, and the quadratic anchor update
corrects only the circulating part (`cor:link-cycle-splitting`). Under exact coarse-graining the dressed coarse link of Gaussian
generators has no real logarithm with positive probability on `\GL^+(K)`, and at small width its
principal logarithm is not Gaussian when the leading cumulant forms are nonzero
(`prop:link-coarse-generator-law`, Chapter 13), so closure is `open:link-coarse-closure`; the
holonomy-conditioned Gaussian parent score is infinite almost surely under every absolutely
continuous generator law (`cor:link-holonomy-parent-almost-sure`, Chapter 11).
A finite product-domain comparison (`prop:link-compact-comparison`) uses mixed
action oscillations and a weighted column influence condition to contract an exact
conditional sampler uniformly over positive source priors. The native-law TV
bound adds the discarded mass once; the exact truncation KL is in the
approximation-to-target direction (`rem:link-comparison-scope`). This is a
conditional inference result, not an identification with recognition dynamics.
On the full unbounded domain, a positive loop containing two independently
variable central dilation directions makes the mixed-oscillation envelope
infinite under the stated axis-growth and no-repeat hypotheses
(`prop:link-global-oscillation-failure`). No positive site weights repair that
envelope. This is a failure of one sufficient estimate, not of actual mixing
or formation (`rem:link-global-oscillation-scope`).

### Part II. Exact coarse-graining at one base point

**Chapter 10, coarse channels.** A coarse channel is a recognition-independent normalized Markov
kernel on latent coordinates that leaves observations unchanged and is vertical over the identity
of `c_*`; it is never a matrix or a deterministic map by default. Data processing and recovery come
from the Chapter 3 lemma. The common-channel coarse VFE chain rule (`thm:rg-exact-coarse-vfe`): one
channel pushes the generative joint, the selected posterior-version family, and the recognition
law; the KL chain is additive in `[0,+\infty]`; adding the finite `-\log p_X(o)` gives an
extended-real VFE identity (a finite VFE may be negative); without finiteness `\Delta_A=0` exactly
when the discarded conditional recognition and posterior laws agree `\mathbb Q_A`-almost surely;
finite fine KL is needed for `\Fenergy_I-\Fenergy_A=\Delta_A` and for the two-way pairwise
common-recovery equivalence. Family-wide recovery (`prop:cg-descent-common-recovery`): one Markov
kernel recovers the reference and every member of a dominated family, for any coarse channel and any
index set, exactly when every likelihood ratio descends to the coarse coordinate, with no
finite-divergence hypothesis (necessity through the Hellinger affinity); the reference conditional
law is then such a kernel and, for a statistic, the unique fiber-supported one; a kernel that does
not read a retained coordinate recovers exactly under descent plus conditional independence, and a
two-point witness shows descent alone does not give it (classical sufficiency, Halmos–Savage and
Blackwell; locators pending, so the statement stays ESTABLISHED with proof).

The full pointwise datum (`thm:rg-pointwise-parent-datum`): a nonempty finite child block `I`,
parent label `A`, fixed `X` with `X_A=\chi_A(X)` outside the random channel, the random parent state
`\mathsf Z_A=\mathsf B_A\times\mathsf M_A\times\boldsymbol\Xi_A\times\mathsf H_A`, and one channel
`C_{A,c_*}:\mathsf Y_{I,c_*}\rightsquigarrow\mathsf Z_{A,c_*}` pushing the fine triple
`\mathbb P_I(do,dy\given X)`, `\boldsymbol\Pi_{I,o,X}`, `\mathbb Q_{I,o,X}` to the parent triple. The
parent posterior identity holds at the observation-kernel level. The parent model coordinate is
generative only through a jointly measurable normalized evaluator
`\operatorname{ev}_A:m_A\mapsto K^{X_A}_{A,m_A}`; standard-Borel disintegration supplies an induced
evaluator, and a predeclared one needs almost-sure compatibility. Marginals are forward projections
of the typed full laws and do not reconstruct them. Equivariant Bayes versions
(`prop:cg-equivariant-bayes-versions`): version transport, finite equivariant Bayes, and Haar
averaging settle the compact and finite cases, and a posterior version weakly continuous on the
support of `QK` extends to an everywhere-defined version equivariant under every stabilizer
(`cor:cg-continuous-version-equivariant`); noncompact stabilizers with no weakly continuous
posterior version, and jointly measurable cross-orbit selection, remain
`open:cg-equivariant-versions`, posed for locally compact second countable groups acting
continuously on Polish spaces. The Galerkin
exactness display `eq:cg-galerkin-exactness` stays here.

The scale category (section 10.6, `sec:rg-scale-category`): one target category is chosen (maps,
normalized Markov kernels, or a declared operator or product category); arrows compose; right-acting
kernels compose as `K_{\ell r}=K_{\ell k}K_{kr}`; a reference-space expression needs declared
isomorphisms, and reference-measure transformations stay explicit. Functoriality is automatic on a
chain, and its content lies in non-chain posets and rule semigroups; there is no stochastic
comparison between finite levels with different numbers of configurations. Autonomous
endomorphisms and scale-dependent cocycles are distinct. The Dobrushin one-step bound is STANDARD
once Dobrushin 1956 is checked. The labeled Fisher decomposition (from the finite thermodynamic
section) has three experiments, label-retained complete data, complete observation, and observed
data, with the missing-information identity (`prop:rg-thermo-finite-missing-information`) and the
labeled within-loss (`prop:rg-thermo-finite-fisher-loss`); `def:rg-thermo-finite-channel` is its
hypothesis. The lattice-free finite-mixture Fisher theorem (`sec:cg-retained-label-asymptotics`;
D9, ESTABLISHED) is stated for one definition of the finite labeled family (merging
`def:rg-thermo-label-family` and `def:rg-thermo-finite-score`) with extensive size `N`, weights the
softmax of effective log masses, and branch densities `N^{-1}\mathcal I`; its strict-phase case, its
fixed-tie `N^2` tensor (label-observation information), and its `1/N` window
`\theta=\theta_0+\mathsf w/N` have different hypotheses and coordinates, and the tie
counterexamples (`prop:rg-thermo-label-tie-counterexamples`) show the hypotheses cannot be dropped.
The nondominated common-channel extension is `cor:cg-measure-evidence`.
Selection includes the general-law and conditional finest-independent partition, its scalar
objective and naturality (`prop:cg-finest-independent-partition`), and its non-Gaussian
nondegeneracy and weak-coupling instability (`prop:cg-independent-selector-instability`).
Permutation symmetry excludes universal intermediate deterministic hard selection from an
exchangeable law alone (`prop:cg-exchangeable-hard-selector`). The information hierarchy
`prop:cg-information-hierarchy` and its finite-alphabet TV stability estimate
`prop:cg-partition-information-stability` do not choose a single physical level.
`open:cg-natural-selector` retains stable selection on a stated interacting-law class and
intrinsic level or membership choice. The evidence-internal criterion remains
`open:restrict-intrinsic-criterion`.

**Chapter 11, gauge-retained network state and fixed sectors.** Tree transports
`\Theta^x_{I\leftarrow i}` with stated tree dependence, rooted holonomy `\mathrm{Hol}^x_I`, and
block-dressed boundary edges `\widehat\Theta^x_e=\Theta^x_{I\leftarrow i}\Theta^x_e(\Theta^x_{J\leftarrow j})^{-1}`
with their endpoint gauge law are retained as raw root-framed marks (primary spanning-tree
construction; Creutz 1977 for maximal-tree gauge fixing). Tree transports compose across depths
(`prop:rg-forest-tree-composition`) when the depth-zero tree of each parent is the union of its
children's trees and a depth-one tree of dressed links, rooted at the root of the root child; one
rooted spanning forest fixed before nested connected-subtree partitions is the special case. This
supplies the composition hypothesis of `prop:rg-linear-cross-scale`(ii), holds for any group, and
concerns group-valued links; matrix communication maps are dressed at their endpoints but not
composed. Holonomy blindness is conditional on
typed fine and parent actions, full fine-law covariance, compatible selected posterior versions,
channel equivariance, and evaluator covariance; same-slice invariance holds only for isotropy
arrows fixing the slice and its versions; neither branch selects membership. For a connected block
the fixed fiber is `\mathbb V_{I,\mathrm{fix}}=\ker L_I` for positive-semidefinite weights and
`\mathbb V_{I,\mathrm{fix}}\cong\mathrm{Fix}(\mathrm{Hol}_I)` under positive-definite weights, by spanning-tree
transport; the retained rank `f_I=\dim\mathbb V_{I,\mathrm{fix}}` gives
full (`f_I=K`, exactly trivial represented holonomy), partial, or no retained degree. Principal
holonomy may be nontrivial when the representation is not faithful; with semidefinite weights the
exact edgewise constraint is `W_e^{1/2}(z_i-\rho(\Theta_e)z_j)=0`. The criterion is admissibility,
not cost; within the Gaussian aggregation flow it does not select a partition; it is not a
consensus-of-beliefs condition.

The holonomy-conditioned marginal-law projection (`thm:cg-holonomy-kl-marginal`): transporting
each marginal to one root and minimizing weighted forward KL over a declared holonomy-fixed parent
family gives an infimum independent of paths, root, and frame; attained zero exactly for a
holonomy-stabilized parallel marginal-law section; an empty family gives infinite distortion;
without attainment zero means approximability only. It is a marginal-law statement, not partition
selection, a coarse channel, or joint recovery. For compact holonomy the closed form is the Haar
symmetrized mixture with automatic attainment (`prop:cg-holonomy-compact-closed-form`); for
Gaussian laws the fixed family is nonempty exactly when the holonomy is conjugate into `O(K)`, and
generic `\GL(K)` links give infinite score (`cor:cg-holonomy-noncompact-gaussian`). The kernel
holonomy proposition is stated on the edge-copy multigraph; `eq:full-graph-holonomy-stabilization`
cites Chapter 2 law coherence. The completed-square lemma (`lem:cg-cut-completed-square`): with a
newly generated positive-semidefinite self term, one invertible link exists exactly when
`\det B\neq0` (a `\GL^+` link exactly when `\det B>0`), the admissible weights form a Loewner
interval, the link is unique exactly when `\Delta=0`, and minimal rectangular compression is
determined up to `O(E)`; without a new self term `\Delta=0` settles it. In `sec:cg-sheaf-closure` the
cut energy is written without the factor one half: `W_e` and the `\Lambda` blocks are quadratic-form
coefficients, the precision blocks of a law proportional to `\exp(-E_{\mathrm{cut}})` are
`2\Lambda_{II}`, `-2\Lambda_{IJ}`, `2\Lambda_{JJ}`, and Supplement G's weights and precision blocks
are twice these. The strict subfamily is
`def:cg-no-new-anchor-pair` (D6). The balanced presentation (`prop:cg-balanced-cut-presentation`):
for an invertible cross block `\Lambda_{IJ}` (`B` above) exactly one anchored presentation carries
the self term at `J` along its own link onto the self term at `I`, equivalently
`\Theta^\top\Lambda_{II}\Theta=\Lambda_{JJ}`; its weight is the matrix geometric mean of the Loewner
endpoints `\Lambda_{IJ}\Lambda_{JJ}^{-1}\Lambda_{IJ}^\top` and `\Lambda_{II}`, it is gauge covariant
and end symmetric, and for scalar weights with orthogonal twists it is the orthogonal polar
presentation. No balanced presentation at the level of laws (`prop:cg-no-balanced-law-presentation`):
for parallel copies between nondegenerate Gaussian laws whose dressed edges are not all equal, and for
any law class at `J` closed under rescaling of the covariance, no presentation of the summed
transported divergences as one divergence to a Gaussian image of the law at `J` plus self terms
reading one law each has the balanced presentation of the transported-precision cut as its Gaussian
mean part (the self term at `I` would have to carry `\Lambda_{II}-W_{\mathrm{bal}}`, which is
homogeneous of degree `-1` in the covariance of `J`). The negative statement
`open:cg-cut-compression` (label retained) rules out a continuous matrix-valued extension of the
balanced link to all singular cuts: two identity-weight SO(2) twists have cross block `2t I`,
so the balanced link has incompatible limits `I` and `-I` at `t=0`. This already excludes a
rule with the additional covariance, reversal, or rank requirements. Exact rectangular
endpoint-map closure remains available. The frame sector: the coarse
frame cancels, the frame occupies a `K^2`-dimensional orbit, a faithful representation makes the
level set one gauge orbit, and no left-equivariant permutation-symmetric map
`\GL^+(K)^n\to\GL^+(K)` exists for `K,n\geq2` (order-`n` rotation argument); the general-`G` form is
proved or left open with the `\GL^+(K)` statement kept. New: `thm:cg-loop-operational-holonomy`, an
operational record at `c_*` sensitive to network-loop holonomy (from the cover operational-holonomy
proof; if the proof does not carry over, it becomes an open problem), the holonomy-score example on
the running loop, and the structural-versus-marginal examples.

**Chapter 12, exact agent-network coarse-graining.** The product-referenced network scale
(`def:rg-network-scale`) with finite-step multipliers `D_\ell`, `D_{n\leftarrow\ell}`. Membership is
a normalized Markov kernel `\mathfrak m_\ell(I\given i,R_\ell)`; a hard partition is its
deterministic case; correlated endpoints use one joint kernel `\mathfrak M_\ell(I,J\given i,j,R_\ell)`,
whose product form needs a declared conditional independence; literal unit weight in overlapping
blocks replicates mass and is not a normalized pushforward; multi-step membership needs
Chapman–Kolmogorov composition and retention of every mark the next assignment reads. The adaptive
step uses one structural channel
`C^{\mathrm{struct}}_{\ell+1\leftarrow\ell}:\mathsf Y_{\ell,c_*}\rightsquigarrow\mathsf R_\ell\times\mathsf Y_{\ell+1,c_*}`;
the current state contains `\eta^b_\ell,\eta^m_\ell`, rooted-holonomy and dressed-boundary marks, and
any record or memory marks the claimed closure needs; the augmented transition state
`\widehat{\mathsf Y}_{\ell+1\leftarrow\ell}=(\mathsf Y_{\ell,c_*},R_\ell,\mathsf Y_{\ell+1,c_*})` does
not duplicate `R_\ell`; the same channel pushes the generative, posterior, and recognition laws
even when they induce different laws of `R_\ell`; composition is exact only when the augmented state
is sufficient for the next structural kernel; depth-`(\ell+1)` links are the dressed marks of all
copies (`eq:full-graph-coarse-links`); multi-depth channels are Chapman–Kolmogorov composites; loop
copies use the diagonal endpoint kernel. The block-product channel is `eq:rg-block-product-channel`.

Results: the effective action (`thm:rg-effective-action`) with its residual, the bounded action
calculus, contraction, the two-sided divergence bounds of a bounded action perturbation
(`cor:rg-perturbation-divergence-bounds`: both directed KLs at most `\min\{\omega,\omega^2/8\}` for
range `\omega`, evidence and complete-VFE offsets kept separate from posterior error, additive
essential bounds along a tower; Hoeffding's lemma with the checked locator Hoeffding 1963 Section 4,
Eq. (4.16), and confined to the bounded tier), the contracted tower (`cor:rg-contracted-perturbation-tower`: widths obey
`\omega_{\ell+1}\le\min\{\log(1+\delta_\ell(e^{\omega_\ell}-1)),\tanh(\Delta_\ell/4)\omega_\ell\}+\omega^{\mathrm{st}}_{\ell+1}`,
the first branch the exact supremum for Dobrushin coefficient `\delta`, depth-uniform bounds for
stochastic channels, additive widths attained by deterministic arrows, offsets never contracting;
Birkhoff and Le Gland–Oudjane attributed), Hoeffding interaction coordinates with the two-agent example, hyperedges,
bridge kernels, the interaction step (`lem:rg-interaction-step`, whose tilted operator equals `U_\ell`
also where `\psi_g` is constant on the reverse rows, as for `\psi_g=f\circ\chi` under a deterministic
channel), intra-block invariance, cocycle telescoping, the native growth bound (the whole
exact derivative cocycle `D_{n\leftarrow\ell}` has norm at most `3^{|V_n|}-1` in the oscillation
quotient norm at every depth, and at most `(3^{|V_n|}-1)\prod_k\delta_k` with `\delta_k` the Dobrushin
coefficient of the tilted reverse kernel, `\delta_k\leq1-e^{-2\Vert[\psi_k]\Vert_{\mathrm{osc}}}(1-\delta_k^\circ)`,
`eq:rg-interaction-dobrushin-growth-bound`; `prop:rg-interaction-native-growth-bound`), and the finite-network obstruction (a finite alphabet
obstructs typed comparisons and vertex-ratio termination,
`prop:rg-interaction-finite-network-obstruction`). Meta-attention is stated for the declared
single-edge model (`prop:rg-attention-single-edge-weights`, `eq:rg-attention-prior-weighted-row`),
with its collapse in the per-receiver model (`prop:rg-attention-per-receiver-collapse`). Path laws and
memory (section 12.8): projection memory, strong lumpability (Kemeny–Snell, chapter 6), the finite
memory KL projection, its extension to standard Borel records and arbitrary Borel history
statistics (`thm:rg-memory-borel-projection`: path KL equals the summed conditional information
`D^{\mathbf f}_N` plus the summed expected row divergence, in `[0,+\infty]` with no dominance or
finiteness hypothesis; the source rows attain the minimum, uniqueness is not claimed for general
statistics), and the memory duration (condensed, STANDARD citation); a projected
hidden-state process need not be Markov, and the signed pointwise memory action has nonnegative
mean KL, not pointwise positivity. The retained-state table `tab:rg-retained-state` replaces the
closure theorem. `rem:rg-trivial-invariant-pairs` records three families of invariant pairs: the
grouping sectors of a base law that is a product over groups of blocks, the fixed sectors of a
finite symmetry of the measure pair and the channel, and the pullback sectors of a deterministic
channel under every base law, with the pullback retained projection
`eq:rg-pullback-retained-projection`. `open:rg-invariant-retained-subspace` is posed for
deterministic block-product channels whose block maps read every coordinate of their block, in the
product and the general classes of full-support base laws, and asks for a proper invariant pair on
an open set of base laws beyond the sum of the pullback and grouping sectors, or a proof that
generically every proper invariant pair lies in that sum. `open:rg-pointwise-parent-dynamics` is
posed for switching diffusions of the four-cycle type whose channels hide coordinates read by the
receiver rows, for time-homogeneous Markov parents or parents with a filter in the explicitly
restricted regular class `def:rg-regular-finite-filter`, at the level of fixed windows up to the
switching time and of the complete history; dimension alone does not exclude Borel history coding;
without such a class the existing lumpability, refresh, filter, and witness statements decide it in
both directions. The chapter keeps the agentization no-go. No Wilsonian
vocabulary (D5); one pointer names Supplement B.

Auxiliary posterior integration has its own finite-network comparison:
`prop:rg-conditional-refresh-entropy` bounds entropy dissipation of outside-dependent
conditional refresh, conditional on a weighted dependence inequality or entropy factorization.
`prop:rg-refresh-target-transfer` charges prescribed target changes and numerical path TV.
`rem:rg-refresh-accuracy-scope` separates initialization, numerical KL, endogenous learning,
and scientific parent dynamics. The sufficient size/depth transfer
`prop:rg-refresh-operational-diagonal` belongs to Supplement B and assumes convergence of the
targets rather than constructing it.

**Chapter 13, the multiscale graph VFE and closing the tower.** The adaptive tower law: the
top-down factorization conditions each depth-`\ell` factor on the whole next-depth state
`Y_{\ell+1}=(Z_{\ell+1},\mathfrak N_{\ell+1})` and on `R_\ell` (`lem:full-graph-adaptive-reversal`,
`eq:full-graph-adaptive-tower-law`); when the graph-datum and coordinate factors read only
`(Z_{\ell+1},R_\ell)` while the partition factor still reads `Y_{\ell+1}`, dropping the graph datum costs
`\sum_\ell I(Y_\ell;\mathfrak N_{\ell+1}\given Z_{\ell+1},R_\ell)` (`prop:full-graph-dropped-datum`,
`eq:full-graph-dropped-datum-cost`), and when the partition factor also reads only `Z_{\ell+1}` the
cost is `\sum_\ell I((R_\ell,Y_\ell);\mathfrak N_{\ell+1}\given Z_{\ell+1})`. The adaptive tower adds no
objective (`cor:full-graph-adaptive-tower-vfe`, ESTABLISHED): with generative input `\mathbb P_0` and
composite structural channel `\mathbf C`, the tower has the depth-0 evidence and posterior version
`\boldsymbol\Pi_{0,o}\otimes\mathbf C`, and every tower recognition law satisfies
`\Fenergy_{\mathrm{tower}}(\mathbb Q)=\Fenergy_0(\mathbb Q_0)+\E_{\mathbb Q_0}\KL(\mathbb Q(\cdot\given y_0)\Vert\mathbf C(y_0;\cdot))`
in `(-\infty,+\infty]` (`eq:full-graph-adaptive-tower-vfe`), with equality for finite `\Fenergy_0`
exactly for the pushed law `\mathbb Q_0\otimes\mathbf C`, equal infima, and, for the pushed law, the
five terms of `eq:full-graph-vfe-factorized` summing to `\Fenergy_0`; (ii) if a structural step has a
deterministic component `\varphi(Y_{\ell+1})=f(Y_\ell,R_\ell)`, every recognition law charging
`\{\varphi\neq f\}` has infinite tower free energy, in particular a coarse factor giving the parent
coordinates an atomless law independent of the children. Parents that carry their own inference
therefore need a declared hierarchy. The one-level Gaussian star with link transports
`z_i\given z_A\sim\mathcal N(\Theta_{e_i}z_A,\Sigma_i)`, a proper apex prior, and a Gaussian record of
the children is a declared hierarchy (`L=1`) whose nondegenerate Gaussian recognition laws, including
product laws with a free parent factor, have finite tower free energy, at least the free energy of the
children's marginal model (`rem:full-graph-anchored-star`, ESTABLISHED; it names Supplement G's
anchored-star section in words, since the main manuscript has no `\cref` into a supplement).
`open:full-graph-declared-gaussian-hierarchy` asks for the multilevel declared Gaussian hierarchy
(stars of stars) whose depth-`\ell` conditionals use inverse tree transports, cut terms along non-loop
copies with the links of `def:full-graph-coarse-links`, and PSD self terms; it is settled by such a law
that is also the adaptive tower of its depth-0 marginal through weighted-transported-mean channels
with Gaussian noise for every datum with nontrivial holonomy in a first-level block (`L\geq2`), or by
a datum of that kind for which no law in the class is such an adaptive tower.
The row free energy `\Fenergy^{\mathrm{att},x}_i` is defined once in energy units, with its
dimensionless form as a one-line rescaling. Tree dependence cites Chapter 11. The random partition
catalog for membership (D12): the normalization models with finite geometry labels
`\gamma\in\mathfrak G`, typed as the structural mark `R_\ell` at `c_*`; the branch carrier is random
and `X` stays outside the channel; hierarchical normalization preserves declared label priors while
globally normalized factors reweight labels by their branch partitions; the VFE includes those
partitions and the full recognition entropy; reference, raw factor, anchor scalar, prior reverse
fiber, induced likelihood, evidence, and posterior are distinct objects; null fibers and zero
evidence are explicit; parameter derivatives include every varying generative factor
(`def:rg-geometry-ensemble`, `prop:rg-geometry-weights`); it creates no edge.

Closing the tower (`sec:full-graph-closing-tower`): a declared root or apex latent with a proper
prior on a truncated tower; anchored normalized cycles; participation in three loci, namely the
same-time inference loop (block coordinate ascent, generic to connected hierarchical models),
parameter learning (the ELBO-optimal prior over an unrestricted family is the aggregate recognition
law, empirical Bayes), and delayed feedback across a sequence of fixed normalized joints as an
episode-indexed joint (`def:full-graph-episode-joint`, `eq:obs-episode-update`,
`eq:obs-aggregate-prior`), with `open:full-graph-episode-accounting` and the dynamic closure
`open:rg-pointwise-parent-dynamics`. The episode-indexed joint admits a latent record copy
`\widetilde o_n` observed through a Dirac kernel, with the extended free energy. The lifted joint
(`prop:full-graph-episode-lifted-joint`): for a parameter route whose update reads a coupling
selected by a declared rule, the joint on the tower states `(\theta_n,y_n,\widetilde o_n)` that
evaluates the selection at the latent record copy is a latent route of the definition; its
conditional episode law is the route's episode joint, its evidence is the product of the episode
evidences, its posterior is the product of the episode posterior slices (filtering), and its free
energy is the sum of the episode extended bounds plus the cross-episode total correlation, equal to
the summed bounds at product laws. An update that reads the recognition law being scored stays
excluded by `req:gen-typing-prohibition`, whose wording is unchanged.
`open:full-graph-episode-accounting` is posed for label-sufficient latent routes at first order: a
route whose per-episode discrepancy from the aggregate update of constant step
`\epsilon_{\mathrm e}` is `o(\epsilon_{\mathrm e})` uniformly on horizons of order
`1/\epsilon_{\mathrm e}`, with silent and informative or Zariski-dense records, or a lower bound of
order `\epsilon_{\mathrm e}` for every such route. The declared-root proposition states its latent-parent typing
hypothesis. At a variational fixed point each agent's effective prior is constituted by the
population's beliefs through a latent inside the joint, not by a kernel reading a posterior.
Bidirectional parent-child optimization is not implied by normalization of a downward kernel; it
needs nontrivial dependence of that kernel on the parent coordinate, a parameterization that
transmits it to the cross-scale VFE, and, for a universal claim, a proved nonzero cross-derivative.
The hierarchy question is `open:full-graph-hierarchy`, posed for models with a partition catalog
inside both laws that descend the multiscale free energy by a reversible diffusion with rate-one
mark redraws and temperature-independent data as `\mathrm T\to0`. Its closure residual is defined
branchwise, since the tower state has a random vertex set and edge variables: for each value of
`R_\ell` of positive mass and almost every value of the graph data, the residual of the step on agent
coordinates whose base is the conditional law of `Z_\ell`, whose arrow is the conditioned structural
channel, and whose product references live on `V_\ell` and on the vertex set of the branch carrier,
averaged over the law of the conditioning data; the settling condition is unchanged. Its positive branch carries the
handoff comparison of SPEC R14 and the restoring and horizon clauses of R15 for the second level,
together with the selector and the slow manifold, and its negative branch is a proof that no
second level produced by descent, apart from a supplied-scale sequence in the sense of R14, meets
them. The preparation and handoff quantifiers are distinguished in
`rem:full-graph-formation-quantifiers` without changing those settling conditions.
`rem:full-graph-marked-limit` shows why continuous-sheet hyperbolicity alone does
not make the complete marked event law deterministic at zero thermostat
temperature; the elementary example is a test of that implication only.

### Part III. Formation and interpretation

**Chapter 14, formation witnesses** (title "Finite-Depth Formation under a Supplied Energy
Hierarchy" for the theorem's section). One fixed `c_*` in the principal/associated-bundle model,
independent translation links, and every network loop retained; no base transport. The chapter
defines the normalized physical joint, its observation and posterior, the separately normalized
restricted optimizer of the declared VFE, and the correlated recognition law; it specifies the
source support, nonlinear source factors, proper correlated prior, calibration, inherited metric,
and complete parameter score before their bounds. Diffusion, source jumps, and the model natural
gradient are a declared VFE-descending realization; VFE does not select their kinetics. The joined
regime (formation-local letters are renamed per SPEC section 3; the level index is `\ell`) is
`Q_L=0`, `Q_\ell=2Q_{\ell+1}+20`, energy strengths `\varepsilon^{-Q_\ell}` (unit at the top level),
squared amplitude `\varepsilon^{3Q_1+20}`, temperature equal to the squared amplitude times
`\varepsilon^6`, horizon `2/\varepsilon`, unit mobility and proposal rate, and source nonlinearity
`10^{-4}/n`; in closed form `Q_1=20(2^{L-1}-1)` and the temperature is
`\varepsilon^{60\cdot2^{L-1}-34}` (`eq:rg-formation-regime-closed-form`), a low-temperature limit with
doubly exponential energy separation. The admissible common-center preparation is stated,
including how its neighborhood may shrink with `\varepsilon` and depend on `L`. Every parent
activates from the preceding retained law and parameter and learns from its own law through its
full inherited score and metric; inherited jump rates are conditional averages, not new heat baths.
The physical-optimizer gap is `eq:rg-formation-physical-optimizer-gap`. The theorem
(`thm:finite-depth-adaptive-formation`) quantifies its constants before the regime and carries one
status over conclusions (a) to (e). Its scope paragraph: coherence is linear hierarchical relaxation
of the prepared mean; the record saturates at the coherence scale
(`eq:rg-formation-source-saturation`); learning is calibration-dominated up to
`\varepsilon^{2Q_1+20}`; slow per-agent models, order-one or nonabelian holonomy, model-channel
records, and coarse agents are not realized; supplied contrasts, internal-neighbor source support,
and calibration are explicit, and source learning is not claimed to create the contrasts. The
doubling comes from the Fisher-budget estimate and is not shown to be required. The Gaussian core
(`prop:rg-formation-gaussian-core`) has, besides its loss formula and upper bound (a), a two-sided
asymptotic across every early interface (b): the core loss is
`(\mathrm A^2/\mathrm T)(\mathrm J_{\ell+1}^4/\mathrm J_\ell^3)` times a core coefficient bounded
below, and the forcing block has full row rank for every choice of bridge endpoints; and a
separation criterion (c): with power laws the core loss is `O(\epsilon^{\mathrm Q_\Delta})` on every
early window exactly when `3\mathrm Q_\ell-4\mathrm Q_{\ell+1}\ge\mathrm Q_{\mathrm T}+\mathrm Q_\Delta`,
which forces a doubly exponential separation of inner base `4/3`. The scope paragraph therefore
declines only that the doubling recursion is required, and `open:rg-formation-regime-sharpness` is
posed for the base-`4/3` schedules `3\mathrm Q_\ell\ge4\mathrm Q_{\ell+1}+20`, `\mathrm Q_\ell\ge14`:
conclusions (a) to (e) with depth-uniform constants, or a preparation and schedule of the class under
which a conclusion fails. The continuous-path
conclusion is concentration of both processes on a common deterministic path with a displacement
bound under every coupling (`eq:rg-formation-common-path-concentration`), not total-variation
convergence of path laws. New: a half-page heuristic on why formation happens, and the endogenous
four-cycle witness (`prop:rg-formation-endogenous-cycle`, `sec:rg-formation-endogenous-cycle`) with
its restrictions (source gating, random matching seeds, symmetric circulation, temperature
`\varepsilon^8`, a Euclidean kinetic metric, a duration-one episode, no parameter learning), from the
2026-09-20 derivation in MultiAgentELBO `docs/derivations/2026-09-11-meta-agent-formation-frontier-and-locality/`.
Its episode event (part (a)) carries an entrance clause (the internal belief relative entropy of
each matched pair exceeds `1/4` at time zero), a restoring clause (normal rates `8+\mathrm T` and
`4+5\mathrm T` on the held sheet, so the least rate times the squared resolution `\epsilon^2` over
the temperature is `4\epsilon^{-4}`), and a horizon clause by margin (the kinetics leave `q^\star`
invariant and realize the event from it with probability at most `4e^{-1/(4\mathrm T)}<p_0/2`). The
gated translation family (`def:rg-gated-translation-family`) places the four-cycle's laws, residual
pairs, exclusive source labels, records, and kinetics on a finite simple graph without isolated
vertices, and `prop:rg-gated-depth-one` shows depth one in it: (a) every sheet `H_S+\mathrm T\Omega`
has a band of order `\mathrm T` of dimension `2N+|E|-\operatorname{rank}H_S` and a band of order one,
and the prior enters only the sheet weights; (b) the gating wells have depth at most
`\mathrm T\sum_i\log(1/\min_j\pi_{ij})` and are flat under block translations; (c)
`\operatorname{rank}\mathbf a_F=|F|+N-\operatorname{cc}(F)`, the minimum rank `2(N-\mathfrak n)`
(`\mathfrak n` the matching number) is attained exactly at minimum edge covers, which are the
spanning star forests with `\mathfrak n` components, the sheet weights obey two-sided bounds, and
sheets with `m` merges carry stationary mass at most `\mathrm K_m\mathrm T^m`; (d) the stationary
coherent-block partition is a minimum-edge-cover partition except with probability
`\mathrm K_1\mathrm T+O(\mathrm a^2)+4|E|e^{-\mathrm a^2/(4\mathrm T)}`. The proposition makes no
dynamic statement (freezing of separated blocks below the thermal time) and has no several-rows
clause; both stay in the research records.
Open items: formation with order-one or nonabelian loop holonomy, a model-channel record, and slow
per-agent models; a source record informative at the coherence scale; depth-uniform constants and a
non-doubling regime; arbitrary families, arbitrary initial laws, mixed-level source support,
intrinsic contrast selection, and infinite depth. `open:rg-formation-adaptive-family`, retitled "A
family in which learning or holonomy selects the components", is posed on the four-cycle of
`prop:phil-seeded-contrast-formation` for Gaussian initial means outside a null set: a law-level
total-variation difference of the first formed block, conditional on contrast formation and bounded
below, between the learned and the frozen-row arm or between initial means differing only in the
loop coordinate, with parent estimates, or its vanishing for almost every mean; its ingredient list
asks for model means and links both slow (`prop:obs-slow-model-link-dichotomy`).
`open:rg-formation-general` is posed for source-gated models with temperature-independent data
outside the gated family, with the handoff declarations of SPEC R14 and the restoring and horizon
clauses of R15 in its positive branch and the supplied-scale exclusion of R14 in both branches. The proof appendix opens with the
lemma-dependency table (`tab:rg-formation-lemma-dependencies`); the textbook entropy inequalities
are cited with their checked locators (Boucheron–Lugosi–Massart, Bakry–Émery, Stam, Carlen,
Csiszár), and a proof is removed only where the plan cuts it.

**Chapter 15, interpretation and its limits.** Declared readings are definitions, commitments
the mathematics uses are standing hypotheses (`hyp:phil-observational-closure`,
`hyp:phil-boundary-agents`), and unsettled readings are open problems (`open:phil-testability`,
citing `thm:cg-loop-operational-holonomy`). The one theorem-type statement is
`prop:phil-seeded-contrast-formation` (ESTABLISHED; proof in the formation appendix, after the proof
of `prop:rg-formation-endogenous-cycle`): on the four-cycle of `def:rg-formation-cycle-experiment`
with product receiver rows learned by `eq:phil-source-learning` at mobility epsilon and initial law
`N(m_0, I_12)` times uniform assignments, (a) the coupled row-and-kinetics system is well posed
and `|pi_ij(t) - 1/2| <= epsilon t/2`; (b) for every `m_0` and every `epsilon <= 1/100`, contrast
formation (a connected block with `2 <= |I| <= |V|-1`, an internal edge with belief KL above 1/4 at
time zero, and internal belief and model KLs at most `epsilon^4` and boundary belief KLs above 1/2
on a unit interval inside `[0, 2/epsilon]`) has probability at least
`(e^{-1/4}/16)[N(m_0,I)(B(x°,1/100)) + N(m_0,I)(B(-x°,1/100))]`, with or without learning, and the
bound is carried by a matched-pair sub-event that is a coherence episode, exceeding its stationary
value under every fixed row configuration by a margin bounded below; (c) from an initial law invariant under the cycle automorphisms (`m_0 = (c_1 1,
c_2 1, 0)`) the rows stay at 1/2. Its heading is "Seeded contrast formation with a
learning-independent lower bound". Its lower bound is supplied by the preparation's matching seed
and is the same with or without learning; the proof uses learning only on the seed interval, the
learned and frozen probabilities of contrast formation are not compared, and the bound is a
positivity statement of size at most `3\times10^{-30}` for every initial mean. It keeps the local-first verdict, cites the three agreements of Chapter
2, rebases the participatory reading on formation, defines the idle wheel (`def:phil-idle-wheel`),
and keeps graph-link holonomy, base-connection holonomy, and bundle topology apart. The
participatory and noumenal readings pull against each other; the chapter sets out what each buys
and costs. It proves the D13' selection statement (`conj:phil-contrast-formation`, now a theorem),
whose mechanism Chapters 1 and 15 describe as the continuous-time learning rule for the mixture
proportions of the source prior, an instance of the parameter-learning locus that does not separate
the program from a hierarchical model with the same learned prior: on the
unchanged four-cycle at every sufficiently small fixed temperature, with the product rows learned by
`eq:phil-source-learning` at mobility `epsilon_L`, the recognition mass off one perfect matching
tends to zero as `epsilon_L -> 0` on a window of order `epsilon_L^{-1} log(1/epsilon_L)` for almost
every Gaussian initial mean, while the frozen-prior arm's pairing law becomes symmetric at long
times. The commentary names the initial law as the supplied asymmetry and points to part (c) as the
symmetry constraint. Its proof is `sec:phil-pairing-selection-proof`; it has no open-problem row.
The proof includes actual-law entropy balance, frozen entropy contraction, a nonzero analytic
transient imprint, the small-temperature matching landscape, and relative saddle escape. It does
not establish event-level formation or parent closure. Its continuation, `cor:phil-joint-selection`, establishes a joint temperature/mobility limit along implicit common thresholds, allowing the matching to vary with temperature; for any prescribed positive caps `h_n`, in particular `h_n=\mathrm T_n^a` with any `a>0`, the thresholds can also satisfy `d_n\leq h_n` (the threshold `7/2` belongs to `prop:phil-temperature-tracking`, not to the corollary). `prop:phil-temperature-tracking` proves a power-law condition for tracking only; explicit power-law selection still requires quantitative imprint control. The new proofs are `ca_joint_selection.tex` and `ca_temperature_bounds.tex`.
Delayed feedback through a declared kernel is the free energy of one joint
(`prop:full-graph-episode-lifted-joint`). Physical-law identification
(`claim:physical-law-identification`) stays open, posed for a named target system observed through a
record kernel that separates, under the model's own law, two objects differing in a gauge-invariant
datum, with held-out evidence that a baseline margin is met or is not met as its two branches;
`open:phil-testability` is posed for a target system observed through a kernel that reads the links
of a closed walk or the coordinates of a candidate block.

**Chapter 16, related work.** Positioning against Bayesian renormalization, network
renormalization, channel and information-geometric renormalization, algebraic multigrid,
matrix-weighted consensus, cellular sheaves, connection Laplacians, and gauge fixing, with the
attribution constraints of section D. Wilsonian vocabulary is allowed here for other authors'
constructions. Bayesian posterior flow is a separate construction: composing it with this model
needs an explicit transition between normalized models and a common comparison target, since
differences of ELBOs otherwise mix evidence and tightness; the bridge is an open row of Supplement G.

**Appendices.** The measure appendix holds the proofs of the Chapter 3 measure results, the
regular-conditional version witness, the STANDARD kernel-measurability statements with checked
locators (Dellacherie–Meyer; Kallenberg 2021), `prop:elbo-relative-log-representation`, the proof of
the chain-rule lemma if it is not STANDARD, and the integrability witnesses
(`sec:app-integrability-witnesses`). Then the formation proofs, the notation table generated from
SPEC section 3, one open-problem table (`tab:open-problems`, core OPEN items only), and
the numerical index (`tab:numerical-index`).

## B. Supplement G (`supplement_gaussian.tex`)

Supplement G cites only the main manuscript. Its introduction states the D6 wording (coarse
families admit newly generated positive-semidefinite self terms; the strict no-new-anchor pair
family is `def:cg-no-new-anchor-pair`), the Gaussian dimensions (belief `K`, model `d_m`, not assumed
equal), `\Gamma_b=\rho_b(G)` with the specialization `\GL^+(K)` (`hyp:gen-lg-frame-group`), the common
frame, and that the belief-sector precision is that of `p(k\given m,o,X)`; membership requires
`A_i+O_i\succeq0`, so the prior balance is sufficient but not necessary.

**Exponential families and the operator layer.** A dominated finite-dimensional canonical family
with reference `\nu`, statistic `T`, natural parameter, log partition, and natural domain; regularity
and minimality are separate hypotheses, and only here do the affine chart, Bregman formulas, and the
Hessian form of Fisher information follow. A graph-exponential representation (node and pair
statistics, graph-indexed affine energy, diagonal affinity) and a closed operator cone `\mathcal W`
are further declarations; the cone need not be the closure of the natural domain. The cumulant and
minimality facts are one STANDARD proposition citing Brown 1986 with checked locators; the affine
information projection carries the Pythagorean identity (`eq:exp-projection-pythagorean`).

**Gaussian realization and the interaction family.** Information parameters `(\mathsf h,\Lambda)`;
the interaction family `\Lambda_{ii}=A_i+\sum_{j\neq i}W_{ij}`, `\Lambda_{ij}=-W_{ij}`,
`W_{ij}=W_{ji}\succeq0`, `A_i\succeq0`, Laplacian part `L`, trivialized coordinates
`z_i=U_i^{-1}\mu_i`. The family is a declared subfamily: an unrestricted directed linear-Gaussian
transition gives an off-diagonal block that need be neither symmetric nor sign-correct
(`\Lambda_i=\begin{psmallmatrix}2&1\\1&3\end{psmallmatrix}` with transition
`\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}` gives
`\begin{psmallmatrix}1&-2\\3&-1\end{psmallmatrix}`). The rotation witness holds only in the
link-trivializing chart; on a forest, gains with positive determinant are absorbed by `\GL^+`
frames (`prop:gauss-gain-absorption`); a two-agent precision with invertible off-diagonal block
`\Lambda_{12}` is reached by `\GL^+(K)` frames exactly when `(-1)^K\det\Lambda_{12}>0`
(`eq:gauss-orientation-criterion`); the chart-independent witnesses are a negative-determinant gain and, for odd `K`, a
v-structure (`prop:gauss-law-level-witnesses`). Under nonflat links an internal edge contributes
`(I-\Theta)^\top W(I-\Theta)` to the coarse self term, vanishing exactly when
`W^{1/2}(I-\Theta)=0`; cut blocks must separately be symmetric, sign-correct, and diagonally
representable. Invariants are invariance under the block reframing group, with two invariant
families (pencil spectra and agent-aligned law functionals); for `\Gamma_b\subseteq O(K)` ordinary
spectra are invariant. The Sylvester integer label needs `\Gamma_b\supseteq\GL^+(K)`; under `SO(K)` or
`O(K)` there are `K` continuous moduli. The Gaussian M-step (`eq:elbo-gaussian-m-step`), the moment
pushforward, the vector residual identities (`sec:geo-flatness`), the linear Gaussian record, and the
Schur-complement and internal-edge lemmas live here.

**Recognition restrictions.** Identification is a generative construction: a recognition law with
one common value per cluster violates absolute continuity and costs `+\infty`, with regularized cost
`\tfrac m2\log(1/\varepsilon)`, `m=NK-n_{\mathrm c}K`. The admissible restriction is on the recognition
mean, with exact cost `\tfrac12m_\perp^\top(B_\perp^\top\Lambda^{-1}B_\perp)^{-1}m_\perp`, the marginal
precision of the identified directions, which agrees with `B_\perp^\top\Lambda B_\perp` only under
`\Lambda`-orthogonality. The mean-tie cost vanishes at the finest partition, the determinant gap
decreases under merging, and the volume term needs an external coefficient, so the analyzed costs
supply no nondegenerate scale; the general question is the core `open:cg-natural-selector`. Under the
observation-free joint precision hypothesis of `prop:restrict-conditional-precision-observation-free`,
the Gaussian evidence has the information form
`\log p_\theta(o\given X)=\widehat{\mathsf h}_o^\top o-\tfrac12o^\top\widehat\Lambda_{oo}o+\mathsf A(\widehat{\mathsf h}_Y-\widehat\Lambda_{Yo}o,\widehat\Lambda_{YY})-\mathsf A(\widehat{\mathsf h},\widehat\Lambda)`
in the joint information parameters, and the bound at the exact block optimum
(`thm:restrict-exact-block-optimum`) is this value minus the determinant gap
(`prop:restrict-gaussian-evidence`, `eq:restrict-gaussian-evidence`, ESTABLISHED).

**Fisher geometry, Hermite spectrum, operator coarse-graining.** Gaussian Fisher charts and the
model-space Fisher transfer; score tangents `L^2_0(\mu)`, the spectrum theorem, the score lift, and
the Hermite domain (relevance conventions go to Supplement B). The operator component
`\Lambda^{(\ell+1)}=\zeta_\ell^{-1}S_\ell^\top\Lambda^{(\ell)}S_\ell` is not the definition of the general
coarse-graining; aggregation alone is a precision-increasing semigroup, so a declared rescaling is
required before a flow or fixed point is typed. Bi-additive closure: `W_{ij}=x_ix_jM`, `A_i=x_iA` with
additive `x` is closed under additive pushforward and becomes invariant only after a hierarchical
identification, which belongs to Supplement B (Supplement G states no fixed point). For a regular
pencil `(L,\Lambda)` there are exactly `NK` finite generalized
roots only when `\Lambda` is invertible; at the singular fixed ray quotient, mass, and pinning are
distinct declared repairs, never a silent pseudoinverse or pseudodeterminant. The scale-free ray
with vanishing self terms is a boundary operator of the Gaussian interaction representation (no
full-space normalizer, no Fisher metric there, no admissible recognition law, an irregular pencil),
not a theorem about every belief fiber. Hard aggregation is the `P_\Lambda` pushforward with an
interior law-level step (`prop:grg-interior-law-step`); monotonicity is open only for varying
`\operatorname{range}(\Lambda S)`, the singular boundary ray, and infinite depth.

**Coarse maps: aggregation, Kron, nonflat links.** Aggregation closure:
`(\Lambda_{\mathrm c})_{IJ}=-\sum_{i\in I,j\in J}W_{ij}`,
`(\Lambda_{\mathrm c})_{II}=\sum_{i\in I}A_i+\sum_{i\in I,j\notin I}W_{ij}`, internal edges annihilated;
this is the Galerkin operator of aggregation algebraic multigrid (cite Notay 2010 and Livne–Brandt
2012), and the Galerkin law is the fine law conditioned on zero within-cluster disagreement, a
`\Lambda`-dependent pushforward (`prop:ig-galerkin-pushforward`, `eq:ig-galerkin-projector`,
`prop:cg-aggregation-conditioning`). The exterior-informed linear interface
(`prop:cg-exterior-interface`, g07): for a Gaussian reference and a linear Gaussian record, the
rank-`r` linear statistic maximizing exterior-predictive information keeps the top generalized
eigenvectors of the pencil `(\Lambda+\Lambda_{\mathrm{rec}},\Lambda)`, whose images are the squared
canonical correlations; the minimal loss is `-\tfrac12\sum_{k>r}\log(1-\check\rho_k^2)`, the coarse
posterior is exact for complete eigenspaces with a `\Lambda`-orthogonal projector (both hypotheses
necessary), the projector is the Galerkin projector, and the Hilbert–Schmidt tails bound the loss
on both sides (Chechik et al. 2005 attributed; the fixed-rank optimality is proved here). For graph-exponential families aggregation precomposes the
unnormalized energy with the identification map; the coarse reference measure, integrability, and
finite normalizer are three separate obligations. Pair-statistic invariance under a site action is a
conditional selection principle; translation invariance is its Gaussian instance. Closure does not
select the family: `\Lambda_{ij}=-\lambda W_{ij}`, `\lambda\in[-1,1]`, is closed under every partition
(`\lambda=-1` is the signless Laplacian), every aggregation factors into pair merges, and what selects
the form is translation invariance (purely additive coarse self terms, consensus as a null
direction). Unlike network renormalization, whose rule is nonlinear, the functional equation here
yields only the invariant bi-additive family `w(x,y)=xyM`, `\alpha(x)=xA` under a measurability
hypothesis. Kron reduction is a different operation and is not closed in general (exact rational
three-agent counterexample); the fixed congruence-diagonal cone is closed, and maximal under the
closed-convex-cone, SPD-order-unit, independent-coefficient, and positive-scaling hypotheses; with
one fixed SPD hidden anchor, maximal independently pair-tested families are exactly the full
anchor-congruence-diagonal cones; for a flat graph with independent SPD weights and fiber dimension
at least two, universal closure is equivalent to at most two retained terminals per hidden component
(counting ground); the prior-carrying corollary (SPD anchors on all hidden agents: universal closure
exactly when each hidden component touches at most one retained agent, failure otherwise generic,
`cor:cg-kron-anchored-agents`); the Möbius order-two statement; the marked nonflat degree-two
sector closes in every order; a proper Gaussian marginal has no positive one-node and two-node
decomposition on its retained nodes. Unrestricted Kron closure is refuted, never described as open.
Finite semialgebraic domains have a complete decision theorem (Tarski quantifier elimination); the
regime table is `tab:cg-kron-regimes`; sequence-producing program descriptions have a decision
obstruction. The finite singular extension uses energy-quotient laws with a declared SPD
representative metric and quotient volume; rank changes can break total-variation continuity and
differentiability in quadratic mean, so finite classification and smooth Fisher continuation are
separate claims. Nonflat links, relaxation, barycenters (with the normal-barycenter no-kernel
proposition `prop:hist-normal-barycenter-kernel`, moved from the core), and the quotient metric
(`prop:cg-quotient-metric`) close the coarse-map chapters; nonflat-link compression cites the core
`open:cg-cut-compression`. The decision metatheory appendix (optional) holds the only treatment of
singular Gaussian laws.

**Reciprocal pairs, anchored stars, loop holonomy.** The flat unanchored reciprocal fold (two
parallel edge copies in opposite directions, each obeying inverse orientation, not assumed inverse)
has singular assembled precision for every SPD link covariance, with kernel the transport-consistent
configurations; outside a fixed joint there is no evidence to bound; proper SPD anchors restore
definiteness; a globally normalized cyclic Gaussian Markov random field is legitimate, with a
transport-dependent partition function; the no-go is never generalized to all cycles. Visible
nontrivial holonomy relieves the fold (the kernel dimension equals that of holonomy minus identity);
holonomy in weight-null directions is a separate effective-support case. Precision addition is cited
to Bishop 2006 (`eq:obs-precision-addition`); star definiteness is one sentence (PSD plus PD); the
anchored-star fixed-point contraction is STANDARD only after the Amit 1991 and Roberts–Sahu 1997
locators are checked. Back matter: notation (resolving `T, m, n, H, A, G, \Theta, h, B, R, U` against
the core), open rows of this supplement only (Bayesian-RG bridge, update robustness,
information-geometric transfer, stochastic inverse RG, nonsemialgebraic Kron families, nonlinear
attraction at the Gaussian tangent), and the numerical index.

**Latent Lie-algebra links (`ch:gauss-latent-links`).** For Gaussian belief laws and
`\Gamma_b=\GL^+(K)`: the law-level transported divergence in reference coordinates in closed form,
with a log-volume term linear in `\Tr\mathring\omega` and its gradient through the exponential
derivative (`prop:glink-law-level-energy`); the comparison record with its current, rank-one
minimizer `\mathbf M^\star`, the sign dichotomy, and an explicit saddle at a critical point of the
exponential (`prop:glink-sample-record`); expected holonomies and loop defects under product
Gaussian generator recognition as ordered products of per-edge moments, with the failure for a
repeated reversal pair (`prop:glink-expected-loop`); the induced action `\tfrac12\log\det` of the
link-dependent interaction precision, its lower bound, single-edge mass terms of noncompact
directions, the cycle determinant, and the values at fixed links of the earlier normalizer results
(`prop:glink-induced-action`); an unanchored cycle with latent links has no joint law
(`cor:glink-unanchored-cycle`), while for `K=1` an unanchored connected multigraph of cycle rank at
least two has a finite joint normalizer and a unicyclic one does not
(`prop:glink-unanchored-scalar`); the chart infimum of the record energy in the negative case is
attained by no chart link whose negative eigenvalues are semisimple, so it is not attained for
`K=2,3` (`prop:glink-chart-infimum-semisimple`); the closed-walk (hopping) series with the triangle
coefficient and an explicit remainder (`prop:glink-hopping`); and the exact spectrum of the
linearized operator on a ring times learning episodes (`prop:glink-linear-spectrum`).
The finite native-law section (`prop:glink-native-tail-envelope`) gives the exact
matter-collapsed record action and a source-prior-uniform Gaussian-reference tail
envelope. `cor:glink-finite-comparison-regime` proves a nonempty finite parameter
domain with positive generator variance and positive record precision where both
the tail and contraction premises hold. The thresholds may depend on the whole
finite graph, history, data, and error tolerance; this supplies no admission at
unchanged experiment parameters or uniform growing-network regime.
Primitive fine Gaussian records and the declared simple-face/two-cycle loop
family meet the axis-growth hypotheses for that global oscillation failure
(`cor:glink-global-oscillation-failure`). The same finite likelihood envelope
gives a conservative source-learning Lipschitz bound `1+M exp(B)`.
A cycle-rooted-forest expansion of the induced action in rank three or more is declined in the scope
paragraph. Open: normalization of unanchored latent links at a stated `K\geq2`
(`open:glink-unanchored-normalization`), and the chart infimum for `K\geq4` at minimizers with a
non-semisimple negative eigenvalue (`open:glink-chart-infimum`).

## C. Supplement B (`supplement_base.tex`)

Supplement B may cite the main manuscript and Supplement G. Its introduction states the deferral
and that the two-atlas generality returns to the core only if frames become dynamical agent states.

**Part B-I, base transport and multi-point designs.** Base curves order contexts and are not agent
histories. The relative frame `h_i` with `u^m_i=u^b_ih_i` exists for representations of different
dimensions and maps no representation spaces; the two frame atlases give cohomologous cocycles, one
Čech class. Principal connections `\omega_b,\omega_m` induce Ehresmann distributions and parallel
transports; the covariant defect of a cross map is defined by horizontal lifts,
`(\mathcal D\Phi)_e(w)=T_e\Phi(H^b_ew)-H^m_{\Phi(e)}w` for a base tangent vector `w`, abbreviated
`\nabla^m\circ\Phi-\Phi\circ\nabla^b` only for fiberwise-linear maps. Four notions are independent:
the transition cocycle is a coboundary exactly when the principal bundle is trivial over the covered
region; graph flatness; connection flatness; trivial holonomy on specified loops (a flat connection
can keep monodromy). A graph link is a base transport only given endpoint contexts, edge-labeled
curves, and an equality hypothesis; a smooth reframing induces vertex gauge only after a vertex
context is chosen. Identified graph links mean equal link maps, `\Theta^m_e=h_i^{-1}\Theta^b_eh_j`.
A common frame is sufficient for literal equality; compatible relative frames can also preserve the same link maps. The product-gauge extension `G_b\times G_m` is an
optional labeled extension. Finite designs use the design index `d` (the core reserves `a` for record
factors); constraining one shared link across design points leaves the exact setwise stabilizer of
`prop:gen-shared-link-stabilizer` (a context-independent rechoice times a central twist common to both
endpoints of each constrained edge), and the fixed-datum admissible family is a set of groupoid
arrows, not a group. Continuum law theory is `open:prob-continuum-theory`; base scale maps
`f_\ell:\mathcal C_\ell\to\mathcal C_{\ell+1}` are never inferred from an increase in depth.

Base-direction information geometry: the covariant pullback `(D^{\omega_x}\sigma)^*g^F_x` is global and
gauge invariant but connection-relative (exact linear and quadratic corrections under
`\omega_x+a`; no connection-independent metric from the bundle alone); its radical is
`\ker D^{\omega_x}\sigma`; constant rank gives a quotient bundle, not a quotient manifold; Frobenius
involutivity, a regular foliation, and basicness are separate hypotheses, with a rank-jump witness
and a constant-rank nonintegrable contact witness; a combined belief-model tensor needs declared
weights. The base-Fisher positivity and cocycle criteria have a complete finite-dimensional
parameterization through the fundamental-action image (contractions from the residual quotient;
indefinite defects need the restricted-image radical, its cross-pairing, inertia admission, and a
totally isotropic residual image); smooth statements need constant ranks; realization by changing
only the target connection needs descent of the adjoint-valued difference. The classifications
concern relaxed pointwise problems under `eq:pb-intrinsic-kernel-constraint`; the base Fisher
contraction corollary `cor:pb-base-fisher-contraction`; cross-scale first jets commute only under
descent and connection compatibility, otherwise the vertical mismatch term is kept. Section-space
histories: configuration curves whose evaluations are vertical, section clocks needing a base
measure, channel weights, and a gauge-quotient rule; strong Hilbert quotients versus the weak Fisher
boundary (a weak metric can fail to give the orthogonal lift); the averaging defect. Covers and
connection descent: one ambient law over a cover induces compatible local data (one consolidated
proposition, `thm:rg-cover-compatible-laws`); compatibility, gluing, and base descent hold by
construction and the descent criterion is the substantive result; conditional attention is
undefined at zero occupancy while event masses extend; every nonzero connection defect and its
composition law are kept; graph-to-base identification is declined, with recovery open; the
base-loop operational holonomy cites the core network-loop theorem.

The collective construction (`def:pb-collective-target`, `prop:pb-collective-minimizer`) uses
specified source-to-target comparison maps and a weighted product Fisher metric. It selects a
smooth local minimizing connection class modulo regular isotropy and is covariant under
independent source coordinate changes. The aggregate rank criterion (`cor:pb-collective-rank`)
distinguishes surjectivity on all horizontal tangents from rank along the chosen section.
Four centered complex Gaussian sections give a local full-rank example with explicit rational
jets (`prop:pb-collective-gaussian-soldering`). The determinant form and a positive compensator
then give a conditional Lorentz metric; a separately supplied circle connection and radius give
its circle completion (`prop:pb-collective-determinant-metric`). These additional moment and
circle forms do not change the positive Fisher tensor. Uniform preservation along coupled
inference and reducing coarse channels is `open:pb-collective-interface-preservation`; local
existence neither selects these additional data nor proves their dynamical persistence.

**Part B-II, infinite networks and Wilsonian limits.** Comparison data, modes, and interaction beta
functions; relevance conventions (`def:rg-hermite-relevance`, `prop:rg-hermite-scope`); the Lyapunov
filtration; finite depth gives no asymptotics (`prop:rg-finite-depth-no-asymptotics`,
`cor:rg-interaction-no-relevant-mode`); asymptotic relevance needs declared scale labels, a two-index
limit, or an infinite network. Continuous scale, fixed points, spectra, and two-index limits. On
the identified homogeneous Gaussian endomorphism `A'=bA`, `W'=b^2W` the spectrum is `b^2` and `b`, each
with multiplicity `K(K+1)/2`, so the ratio outside the dominant eigenspace is `1/b`, self terms
contract, and the coupling ray is not selected; this exact finite-sector gate keeps its label
`sec:grg-numerical-gate`, and the full-cone dynamics (`sec:grg-cones`) sit beside it; attraction on
an infinite hierarchy is not established by any finite blocking sequence. Constant action of fixed
pairs for irreducible finite rescaled kernels
(`prop:rg-fixed-pair-unique-ergodicity`); the fixed-`b` attraction (label
`conj:grg-fixed-b-attraction`, now a proposition) and scalarized attraction; universality remains a
program (rank is an established discrete label, a spectral exponent is a candidate only after a
reference form, a thermodynamic family, and convergence are declared and proved).

**Part B-III, the lattice cluster.** It opens with `open:rg-lattice-typing`. The high-temperature
`\mathbb Z_2` construction: every-exterior coarse specifications, complete generated interactions,
an open-ball RG operator, finite-amplitude approximation, weighted-basin entrance, and regular
fixed-depth Fisher geometry, with `b=\tanh h`, `t=\tanh j`, `0<b<1`, `0<t<1/12`, and character
coefficients `J_S`; norm, reference, block identification, and scalar conversion are explicit; a
common regular region for a finite hierarchy is not a uniform Fisher inverse at unbounded depth. The
classical antecedents (Wegner; Fradkin–Shenker; Osterwalder–Seiler; Dobrushin and Georgii;
Kolmogorov; Kozlov; Israel; van Enter–Fernández–Sokal) are named, no priority is claimed, and the
block-size-uniform every-exterior specification is the principal candidate for a new result.
Geometry and pressure: centered bulk windows, normalized four-state cell counting, a fixed blocking
word of area factor `B^2`, pressure from finite sums; strict gaps select labels and ties need
normalized subextensive ratios; the complete fine observation experiment is pushed, not replaced;
the constant all-positive observation record (`hyp:rg-pressure-positive-record`), the quenched
general-record limit (`open:rg-pressure-quenched-record`), and the specific-VFE minimum, minus the
evidence density, attained on the maximal posterior-score set with shifted Gibbs branches
(`prop:rg-pressure-vfe-minimum`, Georgii section 15.4). The native free partition of
`def:rg-pressure-native` equals `\sum_St^{|S|}b^{|\partial_2S|}` over plaquette sets for all real `b,t`
(`eq:rg-pressure-native-dual`), and for `0<b,t<1` it is a nearest-neighbor ferromagnetic Ising model on
the `(L-1)\times(L-1)` plaquette grid with coupling `\tfrac12\log(1/b)` and negative fields
`\tfrac12\log t+\tfrac{n_\square}2\log b`, `n_\square` the number of edges of the plaquette in no
other plaquette (`rem:rg-pressure-native-ising`, `eq:rg-pressure-native-ising`,
ESTABLISHED). Through it, the free pressure `\lim L^{-2}\log Z_L` exists and is real-analytic on the
whole square `0<b,t<1`, and so are `\mathsf A` and its Hessian on the quadrant `h,j>0`, agreeing with
`thm:rg-thermo-native-cfour-pressure` on its domain (`prop:rg-pressure-native-analytic`, ESTABLISHED
from Lebowitz and Penrose 1968, Section IV, with the Lee-Yang theorem; the boundary fields change
`\log Z_L` by `O(L)`); the Fisher identifications stay on the constructive domain. Thermodynamic Fisher geometry (D9,
ESTABLISHED at the stated hypotheses): native source maps are `C^4` into compact positive boxes, raw
log-weight representatives obey `C^3` volume bounds, and every fixed blocking word precedes volume
limits; finite free laws, exact pushes, infinite-law marginals, and independently normalized coarse
ensembles stay distinct; the strict-phase `C^2` density, the fixed-tie squared-volume tensor, and the
reciprocal-volume `C^2` experiment have different hypotheses; center ratios and regular-chart floors
are not inferred from pressure equality or scalar boundary bounds; natural and raw pressure differ
by finite log-cosh corrections, and the raw pressure is not convex:
`\lim_{j\downarrow0}\partial_j^2\mathfrak p(h,j)=4b^6-5b^8`, negative for `b^2>4/5`, so the raw Hessian
is not a metric there and only `\mathsf H=\nabla_{\mathsf g}^2\mathsf A` is positive semidefinite (`rem:rg-thermo-native-raw-nonconvex`, `eq:rg-thermo-native-raw-nonconvex`,
ESTABLISHED); gauge, Fisher, and base curvature are distinct, and a trace-square
action needs its pairing, sign, base metric, measure, coupling, and normalization; self-consistent
curvature actions are open. The lattice part declares its local symbols in one table at its head.
The Appendix C condensation of C.1.2, C.1.4, and C.1.6 is checked against the falsifier before any
re-proof is replaced; the transfer lemma is hosted at `lem:rg-thermo-native-free-contraction`.

## D. Prior art to cite and attribution constraints

Bayesian renormalization (Berman, Klinger and Stapleton 2023; the Berman–Klinger inverse-flow
companion; the neural-network field theory follow-up; the dynamical-Bayes prequel arXiv:2204.12939)
supplies the Fisher-as-scale idea and the stiff/sloppy vocabulary. Do not attribute to it a spectral
cutoff (its implemented criterion is diagonal), a statement about singular Fisher metrics (it
implicitly requires invertibility), or a concession that it is merely analogical (its Discussion
claims a one-to-one adaptation of momentum-shell renormalization); any disagreement is voiced as
ours. Network renormalization (the Gabrielli et al. review; Garuccio–Lalli–Garlaschelli; Villegas et
al. for the Laplacian renormalization group): the Laplacian specific heat also peaks on structureless
graphs, so use the spectral gap. Bény–Osborne 2015 for channel and information-geometric
renormalization. Aggregation and smoothed-aggregation algebraic multigrid (Notay 2010; Livne–Brandt
2012) for the coarse operator; matrix-weighted consensus for the matrix-weighted Laplacian;
Hansen–Ghrist 2019 (section 4.2, Theorems 3.1 and 4.3) for cellular sheaves and Kron reduction;
Singer–Wu 2012 for connection Laplacians; Tarski 1951 for quantifier elimination; Sylvester's law of
inertia; Birkhoff–Hilbert projective contraction; Creutz 1977 for maximal-tree gauge fixing. The
independent-family, graph-boundary, and marked nonflat series results extend the qualified
congruence-diagonal theorem in different directions; broader correlated or branching classifications
need a declared admissibility class. Check every key in this folder's `references.bib` before use.

For the latent Lie-algebra links: Wilson 1974 Eq. (3.29) for the plaquette action, and
Kogut–Susskind 1975 with Creutz 1983 Ch. 15 Eq. (15.41) for the temporal-gauge derivation in which
time-like plaquettes supply the electric term; Kazakov–Migdal 1993 Sec. 2 for induced gauge actions;
Kenyon 2011 Theorems 1 and 9 for cycle-rooted spanning-forest expansions of connection-Laplacian
determinants in rank one and two (higher rank is open there, Sec. 14); Culver 1966 Theorem 1 for
real logarithms; Schlag–Irie–Schmidhuber 2021 (Sec. 4.2, Eq. (24)) for the delta rule of fast-weight
programmers, with their Sec. 2 for the lineage to Schmidhuber 1992, a correspondence of form only;
Khan–Rue 2023 Eq. (12) (and Eq. (37) for the diagonal form) for the Gaussian Bayesian learning rule;
Opper–Archambeau 2009 Eqs. (18)–(19) for the Gaussian gradient identities and Higham 2008 Ch. 10 for
the Frechet derivative of the exponential, both of which the manuscript proves.

## E. Content that leaves the documents

The typed-intervention identifiability section of 05d, with its certificate digests, goes to
MultiAgentELBO `docs/derivations/2026-09-23-typed-intervention-identifiability/`; the finite probability jets and
native partition jets of Appendix C go to MultiAgentELBO
`docs/derivations/2026-09-10-thermodynamic-fisher-rg/finite-jet-interface.tex`; the verification
narratives, binary64 and API text, and the protocol records of the retired numerical passages go to
MultiAgentELBO `docs/research-log/theory-verification-narratives.md`; Appendix F's package table, run command,
stress-protocol strata, and script locators go to this folder's `verification/VERIFICATION.md`; certificate
states, release digests, and ledger settlement history go to MultiAgentELBO `docs/theory-provenance.md`; the
grand-canonical formation note goes to MultiAgentELBO `docs/research/program-notes/`. The cut list is PLAN section
3; a cut to a citation happens only with a checked locator.

## Selected coherence and early first-block comparison

ca_selected_coherence.tex and ca_first_block_comparison.tex, included by
ca_selection_proofs.tex, prove actual-path persistence and the early-window
conditional first-block null. Chapter 15 states their different observables
and horizons; Chapter 14 retains the original adaptive-family problem.

## Actual conditioned parent activation

ca_parent_conditional.tex and ca_parent_dynamics.tex, included after the
coherence proofs, establish averaged conditional-information and retained-path
bounds for the existing channel activated on the completed late coherence
prefix. The parent starts from the actual conditioned retained law and learns
from its own law. Chapter 15 explains that scope; the original first-contrast
and recursive-formation obligations remain distinct.
