# Audit of the manuscripts against private frames (2026-11-14)

The author requested this audit on November 14, 2026, after a discussion of how the federated-inference scheme of Friston et al. (2024) relates to the gauge-theoretic agent model. The discussion ended on the premise that an agent's frame is private: no other agent can access it. The audit asks where the manuscripts under `manuscripts/` use, in a role that an agent would have to evaluate, a quantity that an agent with a private frame cannot compute. Nine investigator lanes ran in parallel, each restricted to the files listed for it. The lanes were read-only and ran no scripts, numerical checks or web lookups.

This report is the direct output of those lanes. No skeptic, defender or verifier pass has adjudicated any finding, and no manuscript was changed. The text of each finding, including its notation, is the investigator's own; formulas are written in plain text as the investigators returned them. The coordinator wrote this overview, the lane table and the grouping in the section on patterns, and ordered the findings within each lane by class and severity. The coordinator opened three cited locations (`Psych-Sociology/belief_inertia.tex:100` to `:113`, `MAgent_Theory_2.0/chapters/03_dynamics.tex:136` and `MAgent_Theory_2.0/chapters/18_link_dynamics.tex:50` to `:54`) and found there the text the findings quote. No other finding was checked.

## The axiom and the classes

The axiom, called P below, says that each agent has an internal frame, a belief and a prior or model that no other agent can access. An agent has its own belief, prior, model and internal coordinates; the objects it owns and learns, such as a receiver-held dictionary or code model for each sender; the messages it receives, which may be low-rank coded content with a posted coded covariance; and its own sensory observations, including shared referents. It does not have another agent's frame, a transport defined as a function of both agents' frames, another agent's full belief or model, a divergence between full beliefs, any global quantity such as a sum over all agents or a holonomy around edges it does not own, or the true state of the world.

Each occurrence received one class. Class A is a quantity that the text has an agent compute, minimize or follow although P makes it inaccessible. Class B is a quantity used by an external describer, where the text says so or clearly implies it. Class C is a quantity for which the text does not settle who evaluates it. Class D is a setting in which one system computes everything, such as one transformer layer. Class E is a construction that already respects P. A finding is major when a central definition, objective or result depends on the inaccessible quantity and the lane found no counterpart that respects P in its files, minor when the issue is one of labeling or a counterpart exists, and a note otherwise. The lanes also recorded hidden requirements: places where an agent needs a sender's covariance, a known public code, a common prior, a shared reference space or an exchange of dictionaries.

## Totals and lane status

The nine lanes returned 182 findings and 172 hidden requirements. No lane failed.

| Lane | Scope | A major | A minor | C major | C minor | B | D | E | Hidden requirements |
|---|---|---|---|---|---|---|---|---|---|
| fnd | Multi-agent theory, chapters 1 and 2 | 1 | 0 | 0 | 5 | 3 | 0 | 1 | 15 |
| dyn | Multi-agent theory, chapters 3 and 4; belief inertia | 5 | 1 | 0 | 5 | 4 | 0 | 6 | 20 |
| fma | Multi-agent theory, chapters 5 to 9 | 2 | 0 | 0 | 9 | 6 | 0 | 9 | 21 |
| fmb | Multi-agent theory, chapters 10 to 14 | 0 | 2 | 0 | 7 | 7 | 0 | 4 | 16 |
| ctx | Multi-agent theory, chapters 15, 16 and 19; notation | 0 | 0 | 1 | 4 | 4 | 0 | 1 | 18 |
| lnk | Multi-agent theory, chapters 17 and 18 | 1 | 2 | 0 | 6 | 3 | 1 | 6 | 19 |
| att | Attention manuscripts | 0 | 0 | 0 | 5 | 4 | 6 | 3 | 20 |
| pif | PIFB2 and the two foundation notes | 1 | 2 | 0 | 5 | 7 | 0 | 8 | 21 |
| col | Collective agents, main sections | 0 | 0 | 0 | 9 | 16 | 0 | 10 | 22 |
| Total | | 10 | 7 | 1 | 55 | 54 | 7 | 48 | 172 |

## Patterns across lanes

This section groups the findings and does not rule on them.

The frame-built transport with a full-belief divergence, followed as agent dynamics, appears in two manuscripts. In `Psych-Sociology/belief_inertia.tex` the transport is $\Omega_{ij}=U_iU_j^{-1}$, the edge energy is the divergence between the receiver's belief and the transported full belief of the sender, and the attention rows, the Fisher flow and the sender recoil force are built from it (findings dyn-1 to dyn-4, all major). That lane found no dictionary or coded-message counterpart in the file, and it notes that the text never names an evaluator, so a reading in which an external modeler integrates the system would move the four findings to class C. The Gaussian consensus passages of PIFB2 use the same objective with $\Omega_{ik}=e^{\phi_i}e^{-\phi_k}$ and say that agents follow it (pif-1, major; pif-2 and pif-3, minor). PIFB2 already contains the receiver-side counterpart, a received message law with a coded mean and covariance; the lane found no counterpart there for the sender-row terms, the frame update or the latent-link learning rule.

The source-role force of the reciprocal potential is the most widespread item in the multi-agent theory. A source is moved by the laws and attention rows of the receivers that attend to it. Chapter 3 states the requirement itself, that the reciprocal flow is realized by communicating agents only if a reverse message is modeled, and does not construct that message (dyn-5, major). The same dependence recurs, with no evaluator named, in chapters 1, 5, 7 to 12, 15 and 18 (fnd-4, fma-6, fma-8, fma-9, fma-11, fmb-3, fmb-4, fmb-6, ctx-2, lnk-4, and lnk-2 for the global flow of chapter 18). Chapter 3 calls the potential a configuration-level device. Two repairs are named by the lanes: a declared return message from receiver to source, or a statement that reciprocal flows are describer-level and that the per-agent objective is what agents compute.

Comparisons of complete laws enter through invertible links and identity channels. Chapter 2 of the multi-agent theory has agents read costs built from an exponential link that, in the text's words, compares complete laws and discards nothing (fnd-1, major); a coded-marginal comparison is named in one sentence there and no cost is built from it. Identity channels in worked examples pass a peer's full law to the receiver (dyn-6, fmb-1, fmb-2, minor; fma-10 and fmb-3 in class C).

Three constructions use a population-level quantity inside each agent's dynamics. The erasure gate of chapter 8 is a population average of internal laws that modulates every channel (fma-1, major). The fusion flow of chapter 6 is the minimal-norm element of a subdifferential of the whole configuration, and the text says an agent's own selection gives a different dynamics (fma-2, major). The contextual transport of chapter 15 is fixed by a stationarity condition summed over all agents and enters every agent's flow (ctx-1, major, class C).

The loop prior on dictionaries needs agents to exchange how they read each other. For a positive loop weight the per-agent objective of chapter 18 contains means and covariances of dictionaries that other receivers own (lnk-1, major); the text states the requirement and lists the protocol as open, and the path with zero loop weight has no such dependence. Chapter 17 has the same requirement in its remark on receiver-owned factors (lnk-3, minor), and chapter 19 in its wall terms (ctx-4).

The constructions that already respect P are chapters 17 to 19 of the multi-agent theory, where dictionaries are receiver-owned and costs are built from message laws; chapter 4; the per-agent objective of chapters 13 and 14 apart from its identity channels; the collective-agents manuscript, in which the lane found no class A finding and none it would rate major; and the attention manuscripts, in which the lane found no class A finding. The collective-agents lane classified nine items as C because the text declares a scope such as a grounded round or a hypothesis that every member knows a quantity; it notes that five of them would be class A by the letter of the formulas if those declarations are not accepted, and that the two bearing on a central result are in the two-group formation model, where translation learning is fed the true angle between frames plus noise and calibration uses the true world state (col-1, col-2). In the attention lane, two notes describe a single network and never say so (class D without a stated scope), and two covariance updates read a coded sender covariance that the text does not list among the emitted quantities (att-2, att-5).

The hidden requirements recur across lanes: a posted coded covariance of the sender, a known sender code or shared language, a common reference presentation, co-observed referents, and, in the consensus filters of the collective-agents manuscript, the number of members and the summed information matrix.

## Limits of this audit

The findings are unadjudicated, and the classification turns on how each lane read the question of who evaluates a quantity. Several class C findings depend on definitions in chapters outside the lane that raised them, which the lanes list under coverage.

Coverage was incomplete in the following ways. `Attention/GL(K)_supplementary_v2.tex` and the uncommitted folder `Attention/adaptive_vfe_interfaces/` were not assigned. `Attention/GL(K)_attention_v2.tex` was searched and read in part; the unread ranges are listed in that lane. In the collective-agents manuscript only the main sections 1 to 11 and 13 were assigned; the abstract, the related-work and open-problems sections, the supplement, the proofs, the checks and the extensions were not read, and several class C findings turn on propositions that live there. The appendices, companion files and working documents of the multi-agent theory were not assigned. Nine files of PIFB2 were searched without being read in full, and the proof bodies of its sections 36a and 36b were not read. `manuscripts/Stable_Physics_Research_Questions.md`, `manuscripts/tikz.tex` and `manuscripts/verified-ledger.md` were not audited, apart from one search of the ledger.

No lane re-derived the mathematics of a manuscript. Where an investigator did hand algebra to classify a quantity, the finding says so, and that algebra was not checked. The agent-computable replacements proposed in the findings are suggestions of the investigators and are not established results.

## Lane fnd: Multi-agent theory, chapters 1 and 2

Investigator type `audit-gauge-theorist`. Lane magent-foundations: all three assigned files were read in full. The general objects (Markov channel K_ij, peer divergence D_ij, record readout, single-agent free energy F_i) are privacy-neutral or privacy-respecting as defined, and the text states that frames act as a dressing and that the collective connection is a diagnostic. The conflict with P sits in the one worked interaction family: the exponential/group link Theta_ij = U_i exp(L_ij(reference laws of all agents)) U_j^{-1}, which the text itself says "compares complete laws and discards nothing", while 01_foundations.tex:92 has agents read "the outputs of their channels and the costs built from them". No sentence in the three files says who evaluates the link, the law-dependent generator, the source-role force, the global recognition law Q, or the contextual energy; those are filed as class C. A privacy-respecting channel form is named (common message space at 02_interactions.tex:37, low-rank content map M_ij at :83, selective content at :156) but no cost is written with it in these files; receiver-owned dictionaries appear only as forward pointers (:225, :238). No class D declaration (one system computing all frames) appears in any of the three files, and no update rule for a frame U_i appears in them.

### Coverage

- Read in full: MAgent_Theory_2.0/chapters/01_foundations.tex; MAgent_Theory_2.0/chapters/02_geometry.tex; MAgent_Theory_2.0/chapters/02_interactions.tex
- Searched only: MAgent_Theory_2.0/chapters/03_dynamics.tex (outside lane; grep plus excerpts at lines 1-8, 146-153 and 358-391, used only to report how the cross-referenced reciprocal potential and per-agent dynamics are labeled); MAgent_Theory_2.0 (tree-wide grep for privacy, inaccessible, receiver-held, receiver-owned; hits are in chapters 17-19, the Item\_\* working documents and the companion files, none in the assigned files); wiki (grep for 'privacy axiom' and receiver-held or receiver-owned dictionary; no hits, so no prior verdict on P was reused)
- Not covered: MAgent_Theory_2.0 chapters 03 through 19 beyond the excerpts listed, including the definitions of the reciprocal potential, source rows, per-agent model, contextual coupling, communication links and link dynamics that the assigned files reference; All appendices referenced by the assigned files (app:connection, app:records, app:conditional-memory, app:determinant) and the companion and Item\_\* files; The vault theme and concept pages on gauge equivariance were not opened; they concern equivariance, not P; No script, symbolic computation or numerical check was run; the two displayed-coordinate identities for the moment family (Theta_ij = U_i U_j^{-1} + U_i (exp(L) - I) U_j^{-1}, and T_j U_j^{-1} = mu_j^T Sigma_j^{-1} in displayed moments) are hand algebra from eq:int-exponential-link and eq:int-moment-generator

### Findings

#### fnd-1. Agents read a complete-law divergence under the exponential/group link

- Location: `MAgent_Theory_2.0/chapters/02_interactions.tex:156`
- Class A, major
- Quantity: D_ij^a = KL(nu_i^a || nu_j^a K_ij^a) specialized to KL(nu_i || (Theta_ij)\_# nu_j) = KL(bar nu_i || exp(L_ij)\_# bar nu_j), with Theta_ij = U_i exp(L_ij) U_j^{-1}
- Evidence: 02_interactions.tex:156 'an exponential link of a low-rank generator compares complete laws and discards nothing', with KL(nu_i || (Theta_ij)\_# nu_j) = KL((Theta_ij^{-1})\_# nu_i || nu_j). Definition of D_ij at :44. :59-62 (eq:int-dressed-cost) rewrites the cost as a divergence between the two reference laws in the common reference space, so the frames cancel but the sender's full reference law is required. 01_foundations.tex:92 puts in the population algebra what 'the agents themselves read: their source rows, the outputs of their channels and the costs built from them'. 01_foundations.tex:185 'peers' communicated laws are added as further sources'. 01_foundations.tex:299 'Each interaction cost ... and each receiver force, depends on a transport only through the transported law'. Severity is set to major because every cost and force discussed in the three files is of this complete-law form and no coded-marginal cost is written out; the counterpart is one sentence at :37.
- Who evaluates: 01_foundations.tex:92 assigns reading of channel outputs and of the costs built from them to the agents. No sentence in 02_interactions.tex says who applies Theta_ij; with an invertible link the receiver ends with the sender's complete law in its own coordinates whoever applies it.
- Replacement: A divergence between coded marginals in a common message space, of the form KL((T Theta_ij^{-1})\_# nu_i || T\_# nu_j). The files name this at 02_interactions.tex:37 ('two channels can send the receiver and source laws into a common message space, where their communicated predictions are compared'), give the low-rank content map M_ij = U_i O_i T_j U_j^{-1} at :83, and distinguish 'sending only the selective content OTv' at :156, but no cost or result in the three files is built from it.
- Falsifies: A statement that the 'costs' of the population algebra are describer-level and never read by an agent; or a statement that only noninvertible coded channels are read by agents and the exponential-link cost is an analysis device; or a declared scope making the sender's complete law available to the receiver. If the sentence at :37 and the map at :83 are counted as an existing counterpart, severity drops to minor.

#### fnd-2. Link defined through both agents' frames; evaluator not stated

- Location: `MAgent_Theory_2.0/chapters/02_interactions.tex:89`
- Class C, minor
- Quantity: Theta_ij^a = U_i^a exp(L_ij^a) (U_j^a)^{-1}; theta_ij = U_i bar theta_ij U_j^{-1}; M_ij^a = U_i^a O_i^a T_j^a (U_j^a)^{-1}
- Evidence: eq:int-exponential-link at :89; eq:int-group-links at :99; M_ij at :83. Splitting exp(L) = I + (exp(L) - I) gives Theta_ij = U_i U_j^{-1} + U_i (exp(L) - I) U_j^{-1} (my algebra, not in the text), so the 'identity action in unread directions' (:156, prop:int-rank :150-151) is the frame ratio U_i U_j^{-1} in displayed coordinates; :185 'Centered laws give zero generators in this family' then gives Theta_ij = U_i U_j^{-1} exactly. The text treats the reference form as description: :63 'per-agent covariance constrains no reference rule', :145 'holds for every generator rule and constrains nothing', 01_foundations.tex:85 'This is a change of description, not an inference step'. Positive evidence in the same definition: :107 'Opposite edges remain independent: theta_ji is not required to equal theta_ij^{-1}' and :5 'it does not require the interaction to be a frame identification', so the link is not forced to be the coboundary.
- Who evaluates: The text does not say. It says links are 'assigned' to directed edges (:97) and are 'constitutive choices' (:199); no agent, medium or describer is named as the evaluator.
- Replacement: A receiver-held dictionary Theta_ij taken as a primitive edge variable with the transformation law g_i Theta g_j^{-1}, learned from received messages. Not constructed in the three files; forward pointers only at :225 ('Grounded edge messages can also identify dictionaries' -> ch:communication-links) and :238 (latent generators with an anchored loop prior, ch:communication-links and ch:link-dynamics).
- Falsifies: A sentence assigning the evaluation of Theta_ij to an external describer or to the communication medium, or a declared scope in which frames relative to the common reference are mutually known.

#### fnd-3. Law-dependent generator and channel read every agent's reference law or the full configuration

- Location: `MAgent_Theory_2.0/chapters/02_interactions.tex:86`
- Class C, minor
- Quantity: L_ij^a = cal L_ij^a(bar nu^a) with bar nu^a = (bar nu_i^a)\_i; K_ij^a : S x E_j^a ~> E_i^a; moment family L_ij = lambda_ij mu_i mu_j^T Sigma_j^{-1}
- Evidence: :86 'a measurable function of the tuple of reference laws bar nu^a, and of any explicitly declared interface data'; :92 'Dependence on the two endpoint laws alone is the special case'; :29 the channel kernel takes the complete configuration x in S; :66 'A rule whose sector-a kernel reads laws of both sectors'; :105 a tied law-dependent link 'is then a function of the reference laws of both sectors'; moment family :165-168 'O_i(t) = mu_i t, T_j(v) = (mu_j)^T (Sigma_j)^{-1} v' with 'supplied scalar lambda_ij'. In displayed coordinates the sending map T_j U_j^{-1} equals mu_j^T Sigma_j^{-1} computed from the sender's own displayed moments and the receiving map U_i O_i equals multiplication by the receiver's own displayed mean (my computation), so the factorized content map is local to each endpoint; the exponentiation is not, because Tr L_ij = lambda_ij mu_j^T Sigma_j^{-1} mu_i pairs the two reference means and the identity part carries U_i U_j^{-1}.
- Who evaluates: The text does not say who evaluates cal L_ij or the configuration-dependent kernel.
- Replacement: Restrict the generator to the receiver's own law plus the received coded message, or use the factorized content map M_ij (:83) with the sender applying T_j U_j^{-1} and the receiver applying U_i O_i. The files contain M_ij at :83 and the configuration-independent channel at :31, but no restricted law-dependent rule. Outside this lane, 03_dynamics.tex:364 (excerpt read only) requires incoming channels of agent i to be independent of agent i's own laws in the per-agent model.
- Falsifies: Text stating that generator evaluation belongs to the mechanism or to the describer, or a restriction of cal L_ij to endpoint-local inputs with the cross-agent inputs declared as received messages.

#### fnd-4. Source-role force and total variation need other agents' laws at the updating agent

- Location: `MAgent_Theory_2.0/chapters/01_foundations.tex:299`
- Class C, minor
- Quantity: source-role force y -> -(d nu_i / d H\_# nu_j)(H y) of the cost KL(nu_i || H\_# nu_j); d cal E = d_nu cal E + sum\_{a,i,j} \<d\_{L_ij^a} cal E, D cal L_ij^a[d bar nu^a]>
- Evidence: 01_foundations.tex:299 'The source-role force of a cost KL(nu_i || H\_# nu_j) is the receiver likelihood ratio pulled back through H itself', and :303 the two-cycle separates at first order 'because the source forces at the initial configuration already differ'. 02_interactions.tex:225 'The reciprocal dynamics can still separate such loop maps along trajectories through its source forces'. 02_interactions.tex:246-251 (eq:int-total-variation) sums over all a,i,j and 'includes both the sender and receiver occurrences, and every other law on which the generator depends'. The force on sender j's law is a function of receiver i's complete law; the link-dependence term reaches edges not incident to the updating agent.
- Who evaluates: The three files do not say. Outside this lane, 03_dynamics.tex:6 (excerpt read only) calls the reciprocal potential 'a configuration-level device' and says the per-agent free energies 'describe what each agent computes when its peers' laws are data'; 03_dynamics.tex:389 says the per-agent force omits the source-role terms and the channel derivatives of edges the agent does not receive.
- Replacement: The per-agent dynamics (own-law first variations at the current received peer laws), and the frozen-link dynamics. The assigned files name them at 01_foundations.tex:185 and :248 and at 02_interactions.tex:251 ('Freezing the link during an update defines another declared dynamics'); their definitions are in ch:dynamics, not in these files.
- Falsifies: A statement in these chapters that the source-role force and eq:int-total-variation belong to a configuration-level flow that no agent evaluates (then class B), or a declared return message carrying the receiver's law to the sender. If the reciprocal flow is meant as agent-executed, this becomes class A.

#### fnd-5. Global content law and its free energy have no named holder

- Location: `MAgent_Theory_2.0/chapters/01_foundations.tex:263`
- Class C, minor
- Quantity: recognition law Q on the coefficient space Z, Q_D = (F_D)\_# Q, and cal F(Q;o) = KL(Q || Pi_o) - log Z_o
- Evidence: :253 'The global choice needs a joint law over the contents of all agents'; :263 one recognition law Q on Z with agent sections zeta_i^Q(c) = (f\_{i,c})\_# Q as marginals, and record mechanisms that 'may read field evaluations, model presentations, communication maps, and parallel transports along declared paths'; :248 'In one choice all agents are parts of one normalized joint over their contents and records'; :279 the reciprocal potential is 'a separate constitutive object defined on such lists' of marginals. Q, Pi_o and Z_o are global quantities.
- Who evaluates: The text does not say who holds or minimizes Q. It does not state that one system computes everything, so class D is not established.
- Replacement: The single-agent free energy cal F_i(zeta_i;o) of eq:agent-free-energy (01_foundations.tex:198, called 'a single-agent object' at :248) and the per-agent choice in which 'each agent's generative model treats the communicated laws of its peers as data' (:248). Both are in the assigned file; the per-agent model itself is defined in ch:dynamics.
- Falsifies: A sentence declaring Q to be an external describer's object (class B) or the state of one computing system (class D). 03_dynamics.tex:4 (outside lane, excerpt read) says each agent's local free energy is the global one 'viewed as a function of its own recognition factor', which would need checking by the lane that covers it.

#### fnd-6. Contextual energy with eliminated collective connection enters a flow elsewhere

- Location: `MAgent_Theory_2.0/chapters/02_geometry.tex:272`
- Class C, minor
- Quantity: cal E_ctx[p, A] = (1/2) int gamma^{mu nu} G(D^A_mu p, D^A_nu p) dvol, with G_p = sum_i w_i g^F\_{p_i} and A minimized to A^F
- Evidence: :272-276 defines the energy and states 'at fixed p its minimizers over A are the minimizing connections'; :7 'The separate construction in ch:contextual-coupling adds the minimized contextual energy to the reciprocal potential'; :279 'Auxiliary elimination diffuses the law shape and leaves frame and source-row equations without independent diffusion'. The energy sums over all participating agents and its connection solves a normal equation (:212-216) in all agents' laws and their contextual derivatives.
- Who evaluates: In this file the energy is defined, not minimized by anyone; the flow that uses it is in ch:contextual-coupling, outside this lane. The file does not say who evaluates A^F there.
- Replacement: None evident in the assigned files.
- Falsifies: A declaration in ch:contextual-coupling that the contextual flow is a configuration-level or single-system construction, or that each agent's contextual force is built from quantities it owns or receives.

#### fnd-7. Collective connection, pullback tensors, curvature and retention comparisons are declared diagnostics

- Location: `MAgent_Theory_2.0/chapters/02_geometry.tex:7`
- Class B, note
- Quantity: A^F, h^min, k_p, J_p F, e(X) = dM(X) + rho\_\*(A^F(X)) M, h^omega_zeta, a_Psi, Delta_F
- Evidence: :7 'No vector field, source row, channel, or record kernel in ch:dynamics through ch:open-formation depends on a connection, on the collective connection selected below, or on their curvature ... The formation chapters compute connections, pullback tensors, and curvature as diagnostics of those evolved sections.' Collective data at :193-203, minimizing class at :207-217, aggregate jet at :282-287, retention criterion at :406-411. The per-agent tensor uses a 'supplied connection' (:114) and the transported relative entropy at :116-126 compares one section with itself along a curve, so no cross-agent access arises there.
- Who evaluates: An external describer; the text says these are diagnostics and that no vector field or channel in the formation chapters depends on them.
- Falsifies: A vector field, row or channel in the chapters named at :7 that reads A^F, h^min or a holonomy; the file itself flags ch:contextual-coupling as the exception (previous finding).

#### fnd-8. Backtrack loop, reciprocal split, mismatch, law-adjoint condition and loop defect are stated as theorems

- Location: `MAgent_Theory_2.0/chapters/02_interactions.tex:230`
- Class B, note
- Quantity: N_j = Theta_ji Theta_ij, Omega_ij = Theta_ij N_j^{-1/2}, Xi_ij = tilde theta_ij theta_ij^{-1}, Theta_ji = M_j^{-1} Theta_ij^T M_i, Q_ij = (1/2) Tr(Sigma_i (I-W)^T Sigma_i^{-1} (I-W))
- Evidence: :238 of the loop defect: 'It is not a term of the original potential of ch:dynamics.' Reciprocal split at :204-207, mismatch at :112, law-adjoint condition at :223 ('the reciprocal part carries the sender covariance onto the receiver covariance'), quiver invariants at :199. Each is a proposition about transformation laws or invariants. Each needs the opposite-edge link Theta_ji, which belongs to the other agent as receiver, and the law-adjoint condition needs both agents' precisions.
- Who evaluates: An external describer in this file. :238 forwards to ch:communication-links and ch:link-dynamics, which 'introduce latent generators with an anchored loop prior'; whether an agent evaluates a loop product there is outside this lane.
- Falsifies: A use of N_j, Omega_ij or Q_ij inside an agent's update, objective or row weight in these files; none was found.

#### fnd-9. Frames, reference point, reference laws, passive tuples and the species relation are descriptive

- Location: `MAgent_Theory_2.0/chapters/01_foundations.tex:78`
- Class B, note
- Quantity: u_i = sigma U_i^{-1}, bar q_i = ((U_i^q)^{-1})\_# q_i, passive tuple g = (g_i)\_i, U_j g U_i^{-1}, KL(s_j || phi\_# s_i)
- Evidence: :78 'Fix c\_\* and a reference point sigma in P\_{c\_\*}. A frame of agent i is a point u_i'; :85 'This is a change of description, not an inference step'; :87 'covariance under independent passive changes at each agent holds for any rule expressed in reference laws and constrains nothing by itself. The frames act here as a dressing field'; :153 passive change as a tuple acting on the configuration space; :232 sharing up to frame, with the isomorphism given by 'the actions of U_j g U_i^{-1}'; :234 'Sharing a generative model is a statement about mechanisms. Agreement of beliefs over models, KL(s_j || phi\_# s_i) = 0, is a statement about states.' The same descriptive setup is restated at 02_interactions.tex:15-24. No update rule for a frame U_i appears in the three files.
- Who evaluates: An external describer. The text does not say that any agent holds sigma, another agent's U_j, or the map U_j g U_i^{-1}.
- Falsifies: An agent rule in these files that takes sigma, U_j or bar nu_j as an input without declaring it a received message; the law-dependent generator (third finding) is the place where this could occur.

#### fnd-10. Privacy-respecting elements already present

- Location: `MAgent_Theory_2.0/chapters/01_foundations.tex:127`
- Class E, note
- Quantity: rho_i : S_i -> O_i, O\_{ij,t} = rho_i(pr_i Z\_{t+1}), cal F_i(zeta_i;o), general Markov channel K_ij, M_ij, r_ij(k_i,k_j,eps) = A_i k_i - B_ij k_j + eps
- Evidence: 01_foundations.tex:127-136 the record readout is a function of agent i's own internal state; :139 'A list kept outside the agent does not supply this accessibility'; :163 'This definition introduces no observing agent outside the population'; :198 and :248 the free energy cal F_i 'is a single-agent object' built from the agent's own r_i, G_i, l_i and record; :92-94 the observable algebra separates what agents read from a functional 'that no agent, channel, record, or admitted query reads'; :234 'What records can test is weaker than either form of sharing'; :165-172 an r-dimensional comparison record delivered by a mechanism. 02_interactions.tex:37 channels need not be invertible and 'two channels can send the receiver and source laws into a common message space'; :83 the low-rank content map; :156 'Information-discarding, or selective, channels are noninvertible kernels'; :107 directed edges are independent.
- Who evaluates: The agent, from its own state, its own model and what its record mechanism or channel delivers.
- Falsifies: A record readout or single-agent free energy in these files that takes another agent's internal state as an argument; none was found. The comparison record at 01_foundations.tex:165-172 has B_ij co-transforming with the sender's frame, so it is a mechanism-side or sender-side object and not receiver-computed.

### Hidden requirements

- One principal bundle P for all agents and one reference point sigma in P\_{c\_\*} relative to which every frame U_i is defined (MAgent_Theory_2.0/chapters/01_foundations.tex:78; one bundle stated at :16).
- Common reference spaces V_q, V_s, described as 'the common coordinates in which interaction parameters are written' (MAgent_Theory_2.0/chapters/02_interactions.tex:24; spaces introduced at :15).
- A common message space H_a shared by the sending and receiving interfaces, 'provided both maps refer to the same H_a and V_a' (MAgent_Theory_2.0/chapters/02_interactions.tex:92; interfaces at :78-82).
- The law-dependent generator takes the tuple of reference laws of all agents in a sector as input (MAgent_Theory_2.0/chapters/02_interactions.tex:86).
- The channel kernel K_ij^a takes the complete configuration x in S as an argument (MAgent_Theory_2.0/chapters/02_interactions.tex:29).
- The moment family needs the sender's mean and precision, T_j(v) = mu_j^T Sigma_j^{-1} v, the receiver's mean, and a supplied edge scalar lambda_ij (MAgent_Theory_2.0/chapters/02_interactions.tex:167; scalar at :163).
- The receiver is delivered a law, the channel output nu_j K_ij, not a sample: agents read 'the outputs of their channels and the costs built from them' (MAgent_Theory_2.0/chapters/01_foundations.tex:92; cost at 02_interactions.tex:44).
- The law-adjoint condition Theta_ji = M_j^{-1} Theta_ij^T M_i needs both agents' precisions M_i = Sigma_i^{-1} and both directed links (MAgent_Theory_2.0/chapters/02_interactions.tex:223).
- The reciprocal split and the loop defect need the opposite-edge link Theta_ji, held on the other agent's incoming edge, which would require an exchange of dictionaries if an agent computed them (MAgent_Theory_2.0/chapters/02_interactions.tex:204; loop defect at :230).
- A species is a population whose members pairwise share a generative model up to frame, statements using 'channels, codes, or dictionaries within a species require the frame version', and 'a shared language is a separately declared datum' (MAgent_Theory_2.0/chapters/01_foundations.tex:232).
- A record sensitive to a loop transport must read a coupling of the same sample along the routes, which requires a content law over all agents (MAgent_Theory_2.0/chapters/01_foundations.tex:303; restated at 02_interactions.tex:225).
- Record mechanisms of the content model may read 'communication maps, and parallel transports along declared paths' (MAgent_Theory_2.0/chapters/01_foundations.tex:263).
- The collective connection needs comparisons S_i placing all participating laws in compatible fibers with a common target change g, plus constant weights w_i declared as constitutive data (MAgent_Theory_2.0/chapters/02_geometry.tex:183; weights at :193 and :203).
- The per-agent contextual tensor needs a supplied principal connection omega (MAgent_Theory_2.0/chapters/02_geometry.tex:66; 'records the supplied connection' at :114).
- Presentation priors r_i and evaluators G_i are held fixed in every result, so no learning rule for them is modeled (MAgent_Theory_2.0/chapters/01_foundations.tex:208).

## Lane dyn: Multi-agent theory, chapters 3 and 4; belief inertia

Investigator type `audit-variational`. All three assigned files were read in full. belief_inertia.tex has the only frame-built transport in the lane, Omega_ij = U_i U_j^{-1}; its edge energy KL(q_i || Omega_ij# q_j), Gibbs attention, Fisher flow and retained sender-recoil force all make an agent's update depend on other agents' frames, full beliefs, precisions and attention rows, with no dictionary or coded-message counterpart in that file (four class-A major findings). The text never names an evaluator there, so an external-modeler reading would move those four to C. 03_dynamics.tex has no frames and separates three objectives. Its reciprocal Fisher flow needs each source to read its receivers' laws and rows, which the text states itself (03:136, 04:90) without constructing the reverse message. Its per-agent free energy F_i uses only own data plus the communicated law nu_ij = q_j K_ij, so it respects P except in identity-channel specializations. 04_prediction.tex is largely privacy-respecting (sender code T_j, receiver map O_i, own-likelihood assimilation, Jeffrey reconstruction, coded-marginal divergence KL(mu || T\_# p)) but relies on stated common-model, known-code and common-presentation assumptions, and leaves the ownership of the model link Theta^s_ij open. No file declares a single-system (class D) reading.

### Coverage

- Read in full: MAgent_Theory_2.0/chapters/03_dynamics.tex (lines 1-527); MAgent_Theory_2.0/chapters/04_prediction.tex (lines 1-236); Psych-Sociology/belief_inertia.tex (lines 1-1545)
- Searched only: none reported
- Not covered: Cross-referenced material outside the lane that could change classifications: def:int-channel and eq:int-reference-equivariance in 02_interactions.tex, def:generative-model and eq:agent-free-energy in 01_foundations.tex, eq:sample-comparison, the link chapters 16-18 (possible reverse-message or receiver-owned link constructions), ch:fusion to ch:open-formation, and the appendices app:conditional-memory and app:interacting-memory (cmem and imem labels).; The Research vault wiki was not consulted; findings rest only on the three assigned .tex files.; No scripts, numerical checks or symbolic checks were run, per the task's read-only rule; the mathematics was not re-derived, only read for who evaluates each quantity.; references.bib and the cited primary sources were not opened.

### Findings

#### dyn-1. Transport defined from both agents' frames, Omega_ij = U_i U_j^{-1}

- Location: `Psych-Sociology/belief_inertia.tex:100`
- Class A, major
- Quantity: Omega_ij = U_i U_j^{-1} (exponential chart: e^{phi_i} e^{-phi_k})
- Evidence: "The inter-agent transport used below is the linear specialization Omega_ij = U_i U_j^{-1}" (98-105); repeated in the edge-energy definition (113) and "given canonically by Omega_ik = U_i U_k^{-1} ... Omega_ik = e^{phi_i}e^{-phi_k}" (1225). It enters every agent-level expression: edge energy (111), transported precision (376), force balance (418-424), edge current (692-694), gradients (1285-1315). "No dynamics for the frames or connection is introduced" (1014).
- Who evaluates: The text does not name an evaluator. Omega_ij appears inside the flow that agent i's own belief follows (336-339 with 418-424) and inside the attention row assigned to receiver i (180-183). Line 986 calls transport maps "mathematical state variables".
- Replacement: A receiver-owned dictionary Theta_ij learned by agent i for sender j. Not present in belief_inertia.tex. The nearest objects in the lane are the receiver map O_i: H -> E_i and the model link Theta^s_ij in 04_prediction.tex (lines 90 and 16), neither of which is declared receiver-owned there.
- Falsifies: A sentence in the file stating that Omega_ij is supplied externally or held by the receiver as its own learned object, or that the equations are an outside modeler's description that no agent evaluates. I found none. Under the external-modeler reading the class would be C.

#### dyn-2. Full-belief edge energy E_ij = KL(q_i || Omega_ij# q_j) drives the attention row

- Location: `Psych-Sociology/belief_inertia.tex:111`
- Class A, major
- Quantity: E_ij = KL(q_i || Omega_ij# q_j); beta\*\_ij = pi_ij exp(-E_ij/tau)/Z_i; F_i,red = -tau log Z_i
- Evidence: Definition "E_ij = KL(q_i || Omega_ij# q_j)" (111). Row objective Phi_i(beta_i) = sum_j [beta_ij E_ij + tau beta_ij log(beta_ij/pi_ij)] (163-170) with minimizer beta\*\_ij (180-183). The row is read variationally: "factor the variational row as Q_i(c,z=j) = q_i(c) beta_ij ... the transported source templates Omega_ij# q_j ... are held fixed" (158) and "The templates r_ij = Omega_ij# q_j are other agents' variational beliefs" (1520-1536). The flat isotropic form uses the other agents' means directly (848-850). Also the surrogate S_i (216) and the reduced Hessian (437-440).
- Who evaluates: The text does not say who evaluates it. Attention is "optimized" row by row for receiver i, and the appendix gives receiver i a variational row model built from the other agents' transported full beliefs.
- Replacement: A divergence between coded marginals, KL((T Theta_ij^{-1})\_# q_i || T\_# q_j), with a receiver-owned Theta_ij. Not in belief_inertia.tex. Elsewhere in the lane, 03_dynamics.tex:31-34 has the channel form D_ij = KL(q_i || q_j K_ij), and 04_prediction.tex:127-130 has the coded-marginal divergence KL(mu || T\_# p).
- Falsifies: A passage restricting the template r_ij to a received coded marginal (a pushforward T\_# q_j), or stating that the weights beta_ij are assigned by an outside modeler and not formed by the receiver.

#### dyn-3. Primary Fisher flow: agent i's update uses sender means and sender precisions

- Location: `Psych-Sociology/belief_inertia.tex:336`
- Class A, major
- Quantity: mu_i-dot = -eta_mu Sigma_i grad\_{mu_i} F, Sigma_i-dot = -2 eta_Sigma Sigma_i (grad\_{Sigma_i} F) Sigma_i, with F = F_full summed over all agents; receiver term sum_k beta_ik Lambda~\_qk (mu_i - Omega_ik mu_k)
- Evidence: "The primary belief dynamics are first order ... mu_i-dot = -eta_mu Sigma_i grad\_{mu_i} F" (333-341). The force contains "sum_k beta_ik Lambda~\_qk (mu_i - Omega_ik mu_k)" with Lambda~\_qk = Omega_ik^{-T} Lambda_qk Omega_ik^{-1} (376, 418-424, 1285-1286, 1306, 1315). The scalar is the population sum F_full (144-150). The incoming relational stiffness sum_k beta_ik Lambda~\_qk is used in the four-part theorem (366-375). The two-cluster flow uses the other cluster's mean (870-872).
- Who evaluates: Not stated. The flow is written as the dynamics of agent i's own Gaussian parameters, so agent i's update is a function of sender k's mean, covariance and frame.
- Replacement: The own-block gradient of a coded-marginal divergence, using the received T\_# q_j with its posted coded covariance and a receiver-owned dictionary. Not in belief_inertia.tex. The per-agent own-law flow at 03_dynamics.tex:387 is the closest counterpart in the lane.
- Falsifies: A statement that the flow is a population-level description with no agent-level realization claimed, or a version of the receiver force built from a posted coded mean and covariance.

#### dyn-4. Retained sender/recoil force needs the receivers' attention weights, means and covariances

- Location: `Psych-Sociology/belief_inertia.tex:423`
- Class A, major
- Quantity: sum_j beta_ji Lambda_qi (mu_i - Omega_ji^{-1} mu_j); sender covariance gradient (1292, 1315); outgoing stiffness sum_j beta_ji Lambda_qi; recoil -Omega_ik^T J\_{k->i}
- Evidence: The force balance includes "sum_j beta_ji Lambda_qi (mu_i - Omega_ji^{-1} mu_j)" (423-424; also 1291-1292, 1306, 1315, 1481), where beta_ji is receiver j's attention row and the Sigma-gradient contains receiver j's Sigma_j. The text requires this term: "The theorem concerns the complete scalar and includes both receiver and sender derivatives" (430); "every directed edge contributes both a receiver force and a sender recoil" (664, 697-708); "Dropping the sender derivative would manufacture a receiver-only directed update, but that is the detached truncation excluded" (810). The outgoing stiffness term is at 373 and 1353.
- Who evaluates: Not stated. The term is part of the flow that agent i's belief follows as a source, so agent i's update depends on every attending receiver's weight beta_ji, mean, covariance and frame.
- Replacement: A reverse message computed by each receiver from its own belief and the received coded law, namely the weighted likelihood ratio on the message space. 03_dynamics.tex:136 names this requirement ("only if this reverse message is also modeled") but does not construct it. The alternative is receiver-only per-agent dynamics (03_dynamics.tex:387), which belief_inertia.tex:810 explicitly excludes as a truncation.
- Falsifies: A constructed reverse message from receiver to sender carrying this force in coded form, or a statement that the recoil is bookkeeping by an outside modeler. Neither is in the file.

#### dyn-5. Reciprocal Fisher flow: each source is moved by its receivers' laws and rows

- Location: `MAgent_Theory_2.0/chapters/03_dynamics.tex:136`
- Class A, major
- Quantity: Source-role force -beta_ij sum_u [q_i(u)/nu^q_ij(u)] K^q_ij(v,u) (eq:dyn-incoming); h^a_z = dE/du^a_z for the total E = E_0 + sum_i[...] in the Fisher flow (eq:dyn-fisher-flow)
- Evidence: "Every agent descends the same total E, so the population plays an identical-interest game" (136). The incoming term is at 130-131. "Its gradient flow moves each source toward the receivers that attend to it" (4). Flow definition at 164-169. Gaussian instances: "the source force on the variance v_j from one receiver N(m_i,v_i) is (v_j - v_i - (m_i - m_j)^2)/(2v_j^2)" (150) and "the source term of a Gaussian source q_i contains q_k/q_i for each attending receiver" (215, 220, 257). The text states the access requirement itself: "A population of communicating agents realizes the reciprocal flow only if this reverse message is also modeled; otherwise each source must be able to read the laws of every receiver that attends to it" (136), repeated at 04_prediction.tex:90. Later constructions are proved for this flow (4, 233, 495).
- Who evaluates: Line 136 has every agent descend the total E. Lines 6 and 54 call the potential "a configuration-level device" and "a constitutive choice at the level of agent laws". The text is therefore explicit that an agent-level realization needs either receiver-law access or a reverse message.
- Replacement: A reverse message beta_ij (q_i/nu_ij) on the message alphabet, computed by receiver i from its own law and the received nu_ij and composed by the source with its own readout ("for a deterministic readout T it is a function of T(v)", 136). This is named but not constructed in my files. The pooled form W_j KL(q-bar\_{->j} || q_j K_j) at 139-150 shows a single pooled receiver law would suffice at fixed rows. The per-agent flow (387) is the privacy-respecting dynamics, but the text says reciprocal-flow results do not transfer to it (389, 527).
- Falsifies: A construction of the reverse message in chapters outside this lane (for example the link chapters 17-18). If the dispatcher takes line 6 as governing, the finding becomes class B at note severity. I am unsure which reading the author intends for the later formation chapters.

#### dyn-6. Per-agent dynamics with identity channels: receiver descends a divergence to the peer's full law

- Location: `MAgent_Theory_2.0/chapters/03_dynamics.tex:392`
- Class A, minor
- Quantity: nu^q_ij = q_j under an identity channel, so D^q_ij = KL(q_i || q_j) inside F_i
- Evidence: "Take three agents with Bernoulli belief laws ... identity channels ... The per-agent belief dynamics at these frozen rows is (1+w) l_i-dot = -(l_i - rho_i) - w(l_i - l\_{i+1})" (392-396). Theorem three-limits (iii) gives the per-agent force (mu_i - a_i) + sum_j beta_ij (mu_i - mu_j) with identity channels (505, 517, 521). With free Gaussian variances the stationary point "weights each peer cost by the inverse source variance" (524). Declared scope: "identity channels", and "an identity between agents sharing lambda" (241, 249), with K_i = K_j (420).
- Who evaluates: Agent i, in the per-agent picture that "describe[s] what each agent computes when its peers' laws are data" (6). With an identity channel the datum is the peer's whole belief on a shared state space, which the text declares as a hypothesis of these examples.
- Replacement: A non-identity fixed channel or deterministic readout, so nu_ij = q_j K_ij is a coded marginal. This is already the general definition at 03:28-36 and 350-364, with the readout form at 136 and 04_prediction.tex:90.
- Falsifies: If P counts a full-rank identity message on a declared shared space as received content, this is class E. The text presents these as declared special cases used in proofs, not as the general model.

#### dyn-7. Law-dependent channels K_ij[q]: who evaluates a channel that reads the whole configuration is not stated

- Location: `MAgent_Theory_2.0/chapters/03_dynamics.tex:28`
- Class C, minor
- Quantity: K^q_ij[q]: K_j ~> K_i depending on all belief laws q; channel derivative q_j DK^q_ij[q](dq)
- Evidence: "choose normalized channels K^q_ij[q] ... Their dependence on the laws is part of the specified interaction ... A law-dependent channel is required to be a kernel K^q_ij: S x K_j ~> K_i, jointly in the configuration and the source value" (28). "an agent contributes when it is a receiver, when it is a source, and whenever its law changes a channel elsewhere" (128, with 121-127 and 134). The per-agent picture restricts this: "Every incoming channel ... of agent i is required to be independent of agent i's own laws" (364), and the per-agent force omits "the channel derivatives ... of edges that i(a) does not receive" (389).
- Who evaluates: The text does not say. The channel is a constitutive datum of the interaction and no agent is named as forming it. In the reciprocal flow, an agent's force includes derivatives of channels on edges it does not own.
- Replacement: Fixed channels, or a sender-owned coding map T_j composed with a receiver-owned map O_i (04_prediction.tex:90). Fixed channels are the hypothesis of several results here (182-183, 249, 405, 500).
- Falsifies: A definition (possibly def:int-channel in 02_interactions.tex, outside this lane) assigning each channel to the sender or the receiver and limiting its arguments to that agent's own laws and received content.

#### dyn-8. Global mean-field picture: agent i's block update needs expectations under peers' factors and one common joint

- Location: `MAgent_Theory_2.0/chapters/03_dynamics.tex:298`
- Class C, minor
- Quantity: e-bar_i(y_i) = int log p(y_i, y\_{-i}) Q\_{-i}(dy\_{-i}); Q_i\* = exp(e-bar_i) lambda_i / Z_i; global F(Q;o)
- Evidence: "each agent minimizing its own local free energy, with its peers' current factors given, performs coordinate descent of one collective functional. The identification requires that every agent's model be a conditional of the same joint and that peers act through expectations of their contents" (298). Mean field defined at 280-293: "The peers enter e-bar_i only through expectations". Factorized source row cost C_ij = E\_{Q_Y}[-log ell_i(o_i | Y, j)] (300). Label-model rows beta_ij proportional to pi_ij exp(-(D_ij + G_ij)/T) with G_ij = int KL(q_j || q_j^w) q_i(dw) (319-329).
- Who evaluates: Agent i performs the block minimization "with its peers' current factors given". The text does not say how the peers' factors, or the expectations e-bar_i, reach agent i.
- Replacement: Messages equal to the peer-side expectations of the incident log-likelihood factors, which are functions on agent i's own space Y_i (variational-message-passing form). The text notes peers act only through expectations (293, 298) but defines no such message. The global free energy is called the objective in which formation is posed (6), so severity would rise if no delivery mechanism exists elsewhere.
- Falsifies: A passage specifying that agent i receives only the expected incident log-likelihood factors as messages, or one stating that the global picture is a describer's model with no per-agent access claim.

#### dyn-9. Model link Theta^s_ij and evaluator compatibility: ownership of the link is not stated

- Location: `MAgent_Theory_2.0/chapters/04_prediction.tex:16`
- Class C, minor
- Quantity: Theta^s_ij: M_j -> M_i; compatibility K_i^rec(Theta^s_ij m, A) = K_j^rec(m, A); s_i = (Theta^s_ij)\_# s_j
- Evidence: "Suppose a model link Theta^s_ij: M_j -> M_i is a bimeasurable bijection. Exact compatibility of the two evaluators, after identifying their record alphabets, means K_i^rec(Theta^s_ij m, A) = K_j^rec(m, A). Consequently, s_i = (Theta^s_ij)\_# s_j implies equal predictive record laws" (16-21). "If the model link depends on the current laws ..." (39).
- Who evaluates: The text does not say who holds or computes the link. The compatibility condition relates both agents' evaluators and is stated as a condition, not as something an agent checks.
- Replacement: Declare Theta^s_ij a receiver-owned dictionary and read the compatibility equation as a describer's condition. The file does not make that declaration.
- Falsifies: A definition elsewhere (the link chapters 16-18 or 02_interactions.tex) declaring Theta^s_ij receiver-owned and learned from received content.

#### dyn-10. Predictive coding criterion: representation selection uses the joint law of sender content and receiver side information

- Location: `MAgent_Theory_2.0/chapters/04_prediction.tex:234`
- Class C, minor
- Quantity: I(X;U|Z) + lambda D(T), with D(T) = I(Y;X|U,Z); optimal decoder P(dy|u,z)
- Evidence: "The functional I(X;U|Z) + lambda D(T) ... is one possible criterion for selecting a representation" (234). "let P(X,Y,Z) be a declared preparation law ... Let Z be accessible receiver information" (205). "The optimal decoder is P(dy|u,z)" (222). Distortion E KL(P(Y|X,Z) || Delta(Y|U,Z)) (213-221).
- Who evaluates: The text does not say who selects the encoder. The criterion depends on the joint law of the source content X and the receiver's Z. The decoder itself reads only (U,Z).
- Replacement: Not evident from the file. The decoder side is already receiver-computable given the declared preparation law.
- Falsifies: A statement that the criterion is a designer-level or describer-level selection rule. The declared preparation law is the stated scope, so this may be intended as class B.

#### dyn-11. Kinetic extension: agent momentum defined through other agents' velocities and a coupled metric

- Location: `Psych-Sociology/belief_inertia.tex:524`
- Class C, minor
- Quantity: pi_i^mu = sum_k M_ik^mu mu_k-dot; H = (1/2) pi^T M^{-1} pi + F(mu); pi-dot = -grad_mu F - Gamma mu-dot + f_ext
- Evidence: "the momentum assigned to agent i is the full coupled row pi_i^mu = sum_k M_ik^mu mu_k-dot" (521-527). Stacked Hamiltonian (531-535) and balance law (670-677, 699-707). Hamilton's equations (1470-1473) use the same grad F as the first-order flow. The tests are experimenter-level: "A useful test must estimate the kinetic metric M and restoring stiffness K through different interventions" (757).
- Who evaluates: Not stated. The mechanics is written for the stacked population state, and estimation of M, K and Gamma is assigned to an outside experimenter.
- Replacement: None evident. The force term inherits the two flow findings above.
- Falsifies: A statement that the kinetic law is a population-level phenomenological model only (the kinetic-metric postulate at 481-485 calls it a modeling choice but does not address access).

#### dyn-12. Reciprocal potential, reduced potential and their theorems are declared configuration-level

- Location: `MAgent_Theory_2.0/chapters/03_dynamics.tex:6`
- Class B, note
- Quantity: E (eq:dyn-potential), E_red = E_0 - T_q sum_i log Z_i^q - T_s sum_i log Z_i^s, E_o, F_tot = sum_i F_i
- Evidence: "The reciprocal potential is a configuration-level device" (6); "This potential is a constitutive choice at the level of agent laws" (54). Global sums at 44-50, 76-78, 389 and 491. The theorems on dissipation, Morse structure, no-global-VFE and the three limits (157-202, 417-456, 507-522) are statements about the configuration. The record-interrupted dynamics uses record kernels R_k(x,do) "evaluated at the pre-record state" and assimilation maps on the whole configuration (476-484), also a describer-level process definition.
- Who evaluates: An external describer, by the text's own statement at lines 6 and 54.
- Falsifies: Text treating E_red or its global dissipation as something an individual agent monitors. The one sentence that does assign E to agents is recorded in the reciprocal-flow finding.

#### dyn-13. Losses KL(q || q-hat), KL(q || p) and the predictive chain rule involve the sender's full law as analysis

- Location: `MAgent_Theory_2.0/chapters/04_prediction.tex:113`
- Class B, note
- Quantity: KL(q || q-hat) = int KL(q(.|h) || p(.|h)) mu(dh); KL(q || p) = KL(q || q-hat) + KL(q-hat || p); KL(s || t) = KL(sK || tK) + int KL(s^o || t^o)(sK)(do); common-family recovery
- Evidence: Eq. conditional-lift-loss (113-115); Pythagorean identity (127-130); "the loss term measures exactly what a receiver's prior conditional fails to restore" (137); predictive chain theorem (23-33); common recovery and "Recovery without reading the exterior" (139-199).
- Who evaluates: An external describer. These are identities and sufficiency theorems about pairs of laws, and no agent is said to evaluate the loss.
- Falsifies: A use of KL(q || q-hat) or KL(s || t) as an objective a receiver minimizes. None appears in this file.

#### dyn-14. Gauge covariance, Noether charge and loop holonomy are used as analysis and observables

- Location: `Psych-Sociology/belief_inertia.tex:725`
- Class B, note
- Quantity: E'\_ij = E_ij under g_i; Q_a = sum_i a_i^T pi_i^mu with a_i = Omega_ik a_k; W_gamma = Omega_ij Omega_jk ... Omega_li, tr(W_gamma^r)
- Evidence: Covariance proposition (119-136). Noether charge "Q_a = sum_i a_i^T pi_i^mu" (715-723). "a loop holonomy W_gamma = Omega_ij Omega_jk ... transforms by conjugation ... Wilson traces are the conventional compact-group observables" (725, 1179-1188). Stiffness congruence laws (1044-1105).
- Who evaluates: An external describer. These are invariance statements and observables, and no agent is said to compute them.
- Falsifies: A use of W_gamma or Q_a inside an update rule. None appears in this file.

#### dyn-15. DeGroot and Friedkin-Johnsen reductions under declared flat transport; stationary measure rho enters the energy and rates

- Location: `Psych-Sociology/belief_inertia.tex:774`
- Class B, note
- Quantity: F_DG = (lambda_s/2) sum_i rho_i sum_j w_ij KL(q_i || q_j); G_rho = sigma^{-2}(D_rho x I) or eta_i = eta_mu/rho_i; mu-dot = -eta_mu lambda_s [(I - W) x I] mu; F_anchor
- Evidence: "Assume flat transport, fixed common covariance Sigma_i = sigma^2 I ... fixed attention beta_ij = w_ij" (774). "the same cancellation can be implemented under the unweighted product metric by choosing agent-specific learning rates eta_i = eta_mu/rho_i" (783). Flow (785-787); anchored equilibrium (816-833).
- Who evaluates: The reductions are derivations by the modeler under a declared flat common frame. The resulting DeGroot rule has agent i average its neighbors' means directly, as in the classical model.
- Falsifies: A claim that agents themselves compute rho_i or F_DG. The file makes no such claim, and the rate choice is presented as a modeling convention.

#### dyn-16. Per-agent free energy F_i and per-agent flow use own laws, own rows and communicated compared laws

- Location: `MAgent_Theory_2.0/chapters/03_dynamics.tex:370`
- Class E, note
- Quantity: F_i (eq:dyn-per-agent-free-energy); unit-temperature Gibbs rows from costs D^q_ij = KL(q_i || nu^q_ij); own-block Fisher flow h^a = dF\_{i(a)}/du^a; prior-row flow pi_i-dot = T_q(beta_i - pi_i)
- Evidence: "the communicated laws of its peers enter that model as data" (347). "Those peer laws are then parameters of agent i's model, not variables over which it infers" (364). F_i is at 366-376 and the per-agent dynamics at 387. "agent i controls only the first part" (389). "In the per-agent picture the peers' laws are data, so no source term appears" (228). The receiver-side pooling rule (56) and prior-row learning (103-107) use only own quantities and nu_ij.
- Who evaluates: Agent i, from its own (q_i, s_i, beta_i, gamma_i), its own evaluator G_i, reference r_i and record o, and the received compared laws nu_ij = q_j K_ij.
- Falsifies: If the compared law nu_ij is not what is actually transmitted (for example only samples are sent), agent i would not have the law-level D_ij.

#### dyn-17. Sample-message models: rows and costs from received batches and the agent's own law

- Location: `MAgent_Theory_2.0/chapters/03_dynamics.tex:442`
- Class E, note
- Quantity: Registered agreement: agent i receives n messages of law nu^q_iJ and registers whether their empirical type equals q_i; posterior of J equals the Gibbs row at T = 1/n. M_n comparison record o_ij. Frozen-source episodes.
- Evidence: "agent i receives n independent messages from a source J ~ pi_i^q with law nu^q_iJ and registers whether their empirical type equals q_i" (442; theorem at 446-456). "the deviation of the average of n messages of law N(X_j, 1/beta_ij) from its own mean" (511). "Hold the compared laws nu_ij of agent i fixed" (462-474).
- Who evaluates: The receiving agent, from actually received messages and its own law.
- Falsifies: If the registration event were evaluated with knowledge of the configuration x itself and not the received batches. The text's free energy in (iii) takes a point recognition delta_x of the configuration, which is a describer-level object (451).

#### dyn-18. Receiver reconstruction from a coded message: T_j, O_i, own-likelihood assimilation, Jeffrey lift, coded-marginal divergence

- Location: `MAgent_Theory_2.0/chapters/04_prediction.tex:90`
- Class E, note
- Quantity: mu_j = (T_j)\_# q_j; O_i: H -> E_i; q_i^+ proportional to ell_i(h|k) q_i^-; q-hat = int p(dk|h) mu(dh); KL(q-hat || p) = KL(mu || T\_# p)
- Evidence: "A sending map T_j: E_j -> H induces the message law mu_j = (T_j)\_# q_j ... Messages travel from source to receiver" (90). Bayesian assimilation with "a received value h and a declared likelihood ell_i(h|k)" (97-102). Conditional lift q-hat(dk) = int p(dk|h) mu(dh) (106-110). "KL(q-hat || p) = KL(mu || T\_# p)" (127-130). "a receiver contributes structure that the message alone does not specify" (122).
- Who evaluates: The receiver, from the message law or value and its own prior conditional and likelihood.
- Falsifies: If forming p(dk | T = h) needs information about T that the receiver cannot hold. The text assumes the receiver can condition on T and assumes a common content presentation (122).

#### dyn-19. Two-agent conditional-predictor protocol: updates use the transcript and own private record under a supplied common model

- Location: `MAgent_Theory_2.0/chapters/04_prediction.tex:76`
- Class E, note
- Quantity: Gamma_t(dz,dd) = W(d,dz) lambda_t(dd), lambda_t = P(D in . | H\_{1:t}); each agent conditions lambda_t on its own private value
- Evidence: "The receiver integrates the resulting message likelihood over the unknown peer record conditional on its own represented state and available information" (76). "Each agent conditions lambda_t on its own private value and reconstructs its local joint law with W" (84). "These conclusions concern a supplied common-model protocol" (86).
- Who evaluates: Each agent, from the shared transcript, its own private record and the declared common preparation. The peer's private record stays unknown and is integrated out.
- Falsifies: If the appendix (app:interacting-memory, not in this lane) lets an agent read the peer's private record or posterior directly.

#### dyn-20. Within-agent conditional prediction and local free energy use only the agent's own model and record

- Location: `MAgent_Theory_2.0/chapters/04_prediction.tex:53`
- Class E, note
- Quantity: F = KL(s || w^o) + int KL(q_m || Pi_m^o) s(dm) - log Z(o); D_xi E[Y | O = xi] = Cov(Y,X | O = xi) C^{-1}; KL(Pi^o\_{M,Y} || w^o x q_G)
- Evidence: Section "Conditional prediction within an agent" (41-71); equations at 53, 60 and 67.
- Who evaluates: The single agent, on its own joint model and its own record.
- Falsifies: Nothing found. No cross-agent quantity enters this section.

#### dyn-21. Own-data terms: prior KL, sensory likelihood, adaptive prior precision, Fisher arc-length clock

- Location: `Psych-Sociology/belief_inertia.tex:258`
- Class E, note
- Quantity: KL(q_i || p_i); -E\_{q_i} log p(o_i | c_i); alpha_i\* = c_0/(b_0 + D_i) with D_i = KL(q_i || p_i); d-ell = sqrt(d-mu^T Sigma^{-1} d-mu)
- Evidence: Prior and sensory summands of F_full (145-146). "alpha_i\* = c_0/(b_0 + D_i)" (258). Prior and sensory stiffness alpha_i Lambda-bar\_{p_i} + Lambda\_{o_i} (370-371). Arc-length clock (303). Gradients (275-280, 1276-1277, 1298-1299).
- Who evaluates: Agent i, from its own belief, prior and observation.
- Falsifies: Nothing found. These terms contain no other-agent quantity.

### Hidden requirements

- The receiver needs the sender's precision Lambda_qk, transported into its frame, to form its relational force and incoming stiffness (Psych-Sociology/belief_inertia.tex:372).
- A source needs each attending receiver's attention weight beta_ji, an object owned by the receiver's row, for the recoil force and outgoing stiffness (Psych-Sociology/belief_inertia.tex:373).
- All agents' beliefs live on "a common latent dimension d" and frames U_i are defined relative to the same latent variables, which presupposes a shared reference space (Psych-Sociology/belief_inertia.tex:92).
- The DeGroot and Friedkin-Johnsen reductions require a fixed common covariance sigma^2 I for all agents and flat transport Omega = I (Psych-Sociology/belief_inertia.tex:774).
- The reversible DeGroot transient requires each agent's stationary-measure weight rho_i, a global property of W, either in the metric G_rho or as an agent-specific rate eta_i = eta_mu/rho_i (Psych-Sociology/belief_inertia.tex:783).
- Realizing the reciprocal flow by communicating agents requires a reverse message from receiver to source, or sources reading their receivers' laws; the text states this and does not construct the message (MAgent_Theory_2.0/chapters/03_dynamics.tex:136).
- The per-agent picture assumes the whole compared law nu_ij = q_j K_ij is communicated and already expressed on the receiver's state space K_i, without saying who applies the channel (MAgent_Theory_2.0/chapters/03_dynamics.tex:347).
- Identity channels require K_i = K_j and agents sharing one reference measure lambda, which is a shared reference space (MAgent_Theory_2.0/chapters/03_dynamics.tex:241).
- The receiver-and-source pooling identity assumes all receivers of source j use one common fixed channel K_j, which is a public code (MAgent_Theory_2.0/chapters/03_dynamics.tex:139).
- The global mean-field identification requires every agent's model to be a conditional of the same joint, which is a common population model (MAgent_Theory_2.0/chapters/03_dynamics.tex:298).
- With free Gaussian variances the stationary point weights each peer cost by the inverse source variance, so the receiver needs the sender's covariance (MAgent_Theory_2.0/chapters/03_dynamics.tex:524).
- In the model M_n the receiver's comparison record presupposes it knows the message law's variance 1/beta_ij and that messages are centered on the sender's latent mean in a shared coordinate (MAgent_Theory_2.0/chapters/03_dynamics.tex:511).
- The open problem asks whether a species "with matched evaluators and information" admits a common joint, so a common species model is an unresolved requirement for the global picture (MAgent_Theory_2.0/chapters/03_dynamics.tex:527).
- Evaluator compatibility across a model link requires the two agents' record alphabets to be identified and relates both agents' evaluators (MAgent_Theory_2.0/chapters/04_prediction.tex:16).
- The two-agent protocol assumes a common preparation law, known encoders, a reliably shared transcript and a fixed known schedule (MAgent_Theory_2.0/chapters/04_prediction.tex:76).
- Bayesian reception uses a declared likelihood ell_i(h|k), so the receiver must hold a model of how the sender's code produces h from content (MAgent_Theory_2.0/chapters/04_prediction.tex:97).
- The conditional lift requires the receiver to condition its own prior on T = h, so it must know the sending map T, and it "assumes a common content presentation; a link or a separately declared correspondence is needed" across fibers (MAgent_Theory_2.0/chapters/04_prediction.tex:122).
- Common recovery uses one reference conditional R_0 built from a shared reference law P_0 (MAgent_Theory_2.0/chapters/04_prediction.tex:143).
- The optimal decoder P(dy|u,z) requires the receiver to know the declared joint preparation law P(X,Y,Z) and the encoder (MAgent_Theory_2.0/chapters/04_prediction.tex:222).
- The text notes that "Transmitting a sample from (T_j)\_# q_j and transmitting that whole probability law are also different protocols", so law-level divergences presuppose the law-transmission protocol (MAgent_Theory_2.0/chapters/04_prediction.tex:234).

## Lane fma: Multi-agent theory, chapters 5 to 9

Investigator type `audit-variational`. All seven assigned files were read in full. Two places conflict with P as written and have no agent-computable counterpart in these files: the erasure gate of 08_smooth_erasure.tex, a population average of internal gate laws that modulates every peer channel and enters each agent's own gate velocity through a sum over all receiver-source pairs, and the fusion dynamics of 06_fusion.tex, whose sticking velocity is the minimal-norm element of the subdifferential of the whole-configuration potential, with a pair-coordinated antisymmetric selection that the text says an agent cannot choose for itself. The fusion chapter also defines a link Theta_ij = U_i exp(L_ij) U_j^{-1} from both frames and both beliefs, but it declares a common reference coordinate and proves the link pure gauge, so that conflict is removable. Every construction in 06 to 09, and the examples in 05_inheritance.tex, runs on the reciprocal potential, whose Fisher flow moves a sender by the receiver's law and row weight and often uses identity channels on shared reference spaces; the text never says who evaluates these forces and calls the potential a 'configuration-level device', so those uses are class C. The global-formation chapter keeps agent updates local but relies on a structural recognition factor Q_nu that reads every agent's statistics and belongs to no agent or parent. Privacy-respecting pieces already present are the inherited-parent clauses (post-handoff updates factor through the retained state), the shielded channels of 07 with KL(q_i||q_j K_ij) = KL(mu_i||mu_j B_ij), the restored-message kernels of 06, and the fixed-channel Gibbs interface of 09.

### Coverage

- Read in full: MAgent_Theory_2.0/chapters/05_global_formation.tex; MAgent_Theory_2.0/chapters/05_inheritance.tex; MAgent_Theory_2.0/chapters/06_fusion.tex; MAgent_Theory_2.0/chapters/06_outlook.tex; MAgent_Theory_2.0/chapters/07_smooth_closure.tex; MAgent_Theory_2.0/chapters/08_smooth_erasure.tex; MAgent_Theory_2.0/chapters/09_public_compression.tex
- Searched only: none reported
- Not covered: The definitions the assigned chapters cite but do not contain: the reciprocal potential, its reduced form and envelope identity (def:dyn-potential, eq:dyn-reduced, eq:dyn-envelope), the per-agent free energies (prop:dyn-per-agent, def:dyn-per-agent-flow) and the global model (sec:dyn-likelihood, prop:dyn-global-local) in the dynamics chapter. Whether those definitions say who evaluates the source-role force was not checked, and the class C findings on reciprocal flows depend on it.; Chapters 01 to 04 and 10 to 19, the supplement and the appendices (including app:interacting-memory and prop:boundary-joint-spectrum), which the assigned files cite.; The Research wiki was not consulted; this lane was limited to the assigned files.; No derivation or numerical statement in the files was re-derived or checked; findings concern only who has access to which quantity.

### Findings

#### fma-1. Global gate: a population average of internal laws modulates every channel and drives each agent's gate coordinate

- Location: `MAgent_Theory_2.0/chapters/08_smooth_erasure.tex:39`
- Class A, major
- Quantity: H_q=(1/4) sum_i h_i, H_s=(1/4) sum_i hat h_i, alpha(H)=chi((H-h_0)/Delta); the sum over (a,j) of beta\*\_aj d/dalpha d(z_a, alpha rho z_j)
- Evidence: L39-44: 'H_q=1/4 sum_i h_i ... alpha(H)=chi((H-h_0)/Delta)' and 'The gate is a nonlocal function of internal laws.' L46-51: compared law nu_ij^q = b\_{(1-eps)x_i+eps x_j} (x) b\_{alpha(H_q) rho z_j} (x) b\_{h\_\*}. L57-61: D_ij^q contains d(z_i, alpha(H_q) rho z_j). L78-84: dot h_i contains (alpha'(H_q)/4) sum\_{a,j} beta\*\_aj d_alpha d(z_a, alpha rho z_j), a sum over every receiver-source pair. L206: the alternative gate 'driven by a public statistic, such as the polarization 1/4 sum_i d_0(x_i)' is again a population sum.
- Who evaluates: Not stated. The gate is called 'constitutive data' and 'an engineered constitutive choice' (L5, L44); the channel on each edge draws its private output from a law that depends on H_q, and each agent's gate mean follows a flow containing the population-wide sum. No broadcast, record or message that delivers H_q is declared.
- Replacement: None evident in the assigned files. The only variant mentioned (L206) is still a sum over all agents. A receiver-local gate (a function of the receiver's own gate law or of received messages) would be agent-computable, but the entry estimate of erase:gate-entry is not given for it.
- Falsifies: A sentence declaring that H_q is delivered to each agent or channel by a stated public record or message, or that the gate is applied by an external mechanism rather than by agents; or a version of the gate built from the receiver's own h_i or from received coded content.

#### fma-2. Fusion flow is the minimal-norm element of a whole-configuration subdifferential; the per-agent choice is rejected by the text

- Location: `MAgent_Theory_2.0/chapters/06_fusion.tex:215`
- Class A, major
- Quantity: W dot mu in -dF(mu), with pair selections eps_ij = -eps_ji in Sign(mu_i - mu_j); the proximal step argmin_x {F(x) + ||x - mu^k||\_W^2/(2 Delta t)}
- Evidence: L218-219: 'dF is the subdifferential of F as a function of the whole configuration.' L233-237: 'Every pair uses one antisymmetric selection; letting each agent choose its own element of Sign(0), as a product of partial subdifferentials would, admits spurious solutions.' L239-242: 'Each agent performs overdamped planar motion ... under the pair potential.' L258-262: the right derivative is the minimal-norm element in the W norm. L677-682: the discrete update is an argmin over the whole configuration. L698-702: 'An explicit Euler step with sign selections ... does not create exact ties generically.'
- Who evaluates: Not stated; the velocity at coincidence is defined through the global potential and W metric, and the text says an agent's own selection gives the wrong dynamics. Away from coincidence each velocity -a mu_i^q + c mu_i^s - lambda sum\_{j != i} n_j eps_ij (L225-228) needs only the signs of mean differences and the other agents' multiplicities.
- Replacement: None in the assigned files. The agent-local explicit step with sign selections is stated not to produce the chapter's result (L698-702).
- Falsifies: A statement that coincident agents obtain the sticking selection from their own data and received messages, or a proof that the minimal-norm selection decomposes agent by agent; or a declaration that the flow is a describer-level law of motion that no agent evaluates (06_outlook.tex:6 calls the reciprocal potential, of which this is a modification, 'a configuration-level device'; under that reading this would be class C). I am unsure which reading the author intends.

#### fma-3. Link Theta_ij is defined from both agents' frames and both agents' beliefs

- Location: `MAgent_Theory_2.0/chapters/06_fusion.tex:139`
- Class C, minor
- Quantity: L_ij^alpha = chi_alpha(mu_i^alpha - mu_j^alpha), Theta_ij^alpha = U_i exp(L_ij^alpha) U_j^{-1} = V_i^alpha (V_j^alpha)^{-1}; cost d_ij^alpha = sqrt(2 KL(LN(mu_i,1) || (exp L_ij)\_# LN(mu_j,1)))/(1-chi_alpha)
- Evidence: L138-139 define the link from U_i, U_j, mu_i, mu_j. L144-148: 'These links are pure gauge ... Theta_ij = V_i (V_j)^{-1}.' L153-161: the cost equals |mu_i - mu_j|. L168: 'The equality includes the dependence of the link on both endpoint laws', and L171-176 differentiate through it. Declared scope: L10 'Work over one context'; L29-32 'Laws are first written in a common reference coordinate ... Frames do not evolve in this example.' The symbol Theta_ij here is a two-frame transport, not a receiver-held dictionary.
- Who evaluates: Not stated. The text declares a common reference coordinate and fixed passive frames, and shows that the cost and flow are the same for every chi 'including the limit of identity transport' (L162-164).
- Replacement: Identity transport in the declared common reference coordinate: the cost |mu_i - mu_j| between the two restored message laws LN(mu_i,1) and LN(mu_j,1). Already in the file at L159-164.
- Falsifies: A statement that the link is formed by the receiver from its own frame and a received message only; or a use of the link in which chi or the frames survive in the cost.

#### fma-4. Structural recognition factor Q_nu and selector hat Pi read every agent's law and belong to no agent

- Location: `MAgent_Theory_2.0/chapters/05_global_formation.tex:121`
- Class C, minor
- Quantity: F(Q;o) = KL(Q||P_0) - E_Q sum_i log l_i(o_i|y_i); g_i(z) = exp int log p_i(y|z) Q_i(dy); Z_Pi; Q\*(Pi); hat Pi(m) = argmax_Pi pi(Pi) N(m;0,C_Pi); m' = a o + b K_Pi m
- Evidence: L71-77: the objective is the global free energy. L125-131, L134-147: the block minimizer of Q_nu is built from g_i of every agent. L199-203: the selector is 'Bayesian model selection on the means', the full vector m. L226-229: each sweep 'replaces Q_nu by its block minimizer given Q_y'. L242-244: 'the non-agent coordinate as one more block'. L259-264: each mean update uses K_Pi m, a function of all means. L390-393: 'the full selector compares structures with other first levels, whose scores read the within-block contrasts', so individual member means are read, not only block sums.
- Who evaluates: Not stated. Q_nu is a recognition factor of the population-level variational family; no agent, parent or external recognizer is named as holding it, and the catalog and its prior (L39-50) are common data.
- Replacement: Under exponential-type children the factor depends on the agents only through t_B = sum\_{i in B} E\_{Q_i} T_i (L148-158; Gaussian case L203-206), so each agent posting its own E\_{Q_i} T_i (in the Gaussian case m_i/s_i^2 and 1/s_i^2) is a coded message that suffices. The file has the statistic but not the attribution of who receives it.
- Falsifies: A sentence assigning Q_nu to a named holder (a parent, a declared non-agent recognizer, an external describer) and saying what it receives from the agents; or a statement that the sweep is a describer-level algorithm.

#### fma-5. Handoff initializes the parent from the actual fine state without saying what members transmit

- Location: `MAgent_Theory_2.0/chapters/05_inheritance.tex:1291`
- Class C, minor
- Quantity: R_I(x) at the handoff, including 'the source marks and memory read by future interactions'
- Evidence: L1291-1293: 'A handoff initializes the parent from the actual fine state or its declared conditional law, including the source marks and memory read by future interactions.' L813-817: the retention is a Borel map on the invariant set of post-handoff configurations.
- Who evaluates: Not stated. The parent's initial state is a function of every member's complete state; the text does not say whether members post it, a channel assembles it, or it is a describer's assignment.
- Replacement: Sample compression through a normalized channel C, Q_x^c(A) = int C(y,A) Q_x(dy), is already defined at L27-32; in the constructions the retained statistics are low-dimensional (block means, multiplicities, precision-weighted records) that members could post themselves. The files do not state this.
- Falsifies: A sentence saying the parent state is assigned by the describer, or that it is assembled from named member messages.

#### fma-6. Reciprocal-potential flows in the examples: a sender moves by the receiver's law and row weight

- Location: `MAgent_Theory_2.0/chapters/05_inheritance.tex:1047`
- Class C, minor
- Quantity: P(x_1,x_2) = d(x_1,f(x_2)) + d(x_2,f(x_1)) with dot x_i = -(1-x_i^2) d\_{x_i}E; the source term -sum_l sum_j beta_lj sum_u (q_l(u)/C[M](u)) dC[M](u)/dM . T(v); channel C[M] with M = sum_i E\_{q_i} T; E = sum_i (x_i-c_i)^2/2 + (1/4) sum_i sum\_{j != i} (x_i-x_j)^2/2
- Evidence: L1046-1051 and L1060-1064: the flow of agent 1 differentiates d(x_2, f(x_1)), agent 2's cost. L1545-1548: every peer channel outputs C[M], a law of the additive moment of all agents. L1570-1574: 'As a source, q_i enters every cost only through M, so it contributes' a sum over all receivers l with their laws q_l and rows beta_lj. L1912-1919 and L1948-1949: identity channels and 'the source role contributing the same term as the receiver role'. L2079-2080: 'the reciprocal potential as the configuration-level device it is'.
- Who evaluates: Not stated. The flows are given as the dynamics of the agent laws; the text does not say agents compute their forces, and it labels the potential a configuration-level device. The propositions themselves are analyses of these flows. The defining objective is in the dynamics chapter, outside this lane, so severity here reflects inherited use only.
- Replacement: The per-agent free energies F_i with self costs KL(s_i||r_i) and int KL(q_i||G_i(m,.)) s_i(dm) are referred to at L1678-1683 and in 06_outlook.tex:6 ('its own evaluator and its peers' communicated laws compete as sources of prior information'); their definition is outside the assigned files, and 06_outlook.tex:6 says conclusions are not known to transfer between objectives.
- Falsifies: A statement in the dynamics chapter that the reciprocal flow is a describer-level law of motion, or that the source-role force is delivered to the sender as a declared back-action message.

#### fma-7. Selectors are functions of the configuration of all agent laws

- Location: `MAgent_Theory_2.0/chapters/05_inheritance.tex:1720`
- Class C, minor
- Quantity: selector S_c(x): centroid-distance threshold; exact equality of means; mode of the structure factor; connected components of the preferred-source graph
- Evidence: L1720-1722: 'The selector is a declared measurable function of the configuration of agent laws, the accessible records, and the declared interfaces.' L1802-1803: 'Each handoff is a measurable function of the state or of accessible history.' L1922-1924: joins blocks when 'the distance of their count-weighted centroids reaches delta'. Instances in other assigned files: 06_fusion.tex:791-794 (equal means, 'reads laws only'), 05_global_formation.tex:235-238, 08_smooth_erasure.tex:266.
- Who evaluates: Not stated. The wording 'readout convention' (L1797-1798) and the use in control comparisons suggest a describer's readout, but the handoff it triggers changes which description evolves.
- Replacement: In 08_smooth_erasure.tex:266 the first step is already agent-owned ('each agent's preferred source ... is the source of smallest reciprocal row cost'); only the assembly into graph components is population-level.
- Falsifies: A sentence saying the selector is evaluated by the describer only and triggers no operation of any agent; or one naming the agent or parent that evaluates it and the messages it uses.

#### fma-8. Public flow uses 'every interaction role' and channels that depend on the tuple of all public laws

- Location: `MAgent_Theory_2.0/chapters/07_smooth_closure.tex:124`
- Class C, minor
- Quantity: h_i^q = delta E_c/delta mu_i 'including every interaction role and channel derivative'; B_ij^q[mu] with mu the tuple of public laws
- Evidence: L5: 'This chapter works with the reciprocal law potential ... its conclusions concern that potential, not the per-agent or global free energies.' L67: channels B_ij^q[mu] are 'differentiable in the laws'. L112: the derivative Db_ij[mu](delta mu_k) runs over any agent k. L124 and L135: h_i includes every interaction role; 'every peer contribution is a functional of mu alone'.
- Who evaluates: Not stated. As a source, agent i's public velocity contains the derivative of other receivers' costs KL(mu_l || mu_i B_li), which reads their public laws and rows; a channel on edge j to i may read third agents' public laws.
- Replacement: The receiver-role cost KL(mu_i || mu_j B_ij^q) at L78-84 is agent-computable when B_ij depends on the sender's public law only. The private-sector result (L129, L140) contains no other agent and does not depend on the source-role terms. No source-role-free version of the public flow is given in the assigned files.
- Falsifies: A declaration that public laws are posted to all agents (which would make these quantities received content), or that the flow is a describer-level law of motion.

#### fma-9. Erasure flow: incoming source terms and a parent field that reads the counting measure of all public states

- Location: `MAgent_Theory_2.0/chapters/08_smooth_erasure.tex:146`
- Class C, minor
- Quantity: public force with 'one outgoing row and three incoming sources'; V[v; M] with M = sum_I |I| eta_I
- Evidence: L5: the chapter concerns the Gibbs-reduced reciprocal potential and 'nothing in it is a statement about the per-agent or global free-energy pictures'. L146: 'The full public force has one outgoing row and three incoming sources.' L243: V[v;M] 'is determined by v and the counting measure M ... the derivative includes both receiver and incoming source terms'. L257: 'A single eta_I has no autonomous dynamics, since V[v;M] depends on the counting measure of both pairs.'
- Who evaluates: Not stated. As a source an agent's public mean is pushed by the receivers' public means and Gibbs weights; the parent of one pair needs the other pair's retained measure as exterior state.
- Replacement: The receiver-role costs D_eps(x_i,x_j) are built from the receiver's own public law mixed with transmitted public samples (L46-52). No source-role-free version is given.
- Falsifies: A declaration that public means are posted to all agents, or that the reduced flow is describer-level.

#### fma-10. Identity channels: each agent is compared with the complete belief and model laws of every other agent

- Location: `MAgent_Theory_2.0/chapters/09_public_compression.tex:23`
- Class C, minor
- Quantity: peer costs KL(q_i||q_j) and KL(s_i||s_j) under identity channels; Z(r) = sum_j w_j exp[-KL(r lambda || q_j)/T]
- Evidence: L4: 'the reciprocal law potential ... with identity channels'. L23: 'Take N >= 2 identical agents, identity peer channels, all other agents as sources.' L39: 'The channels are identities between agents sharing A and B.' L180-185: an identity-channel receiver sees Z(r) built from the 'exposed belief laws' q_j.
- Who evaluates: The receiver, under a declared identity channel on shared reference spaces A and B; the communicated law is then the sender's complete belief or model law, with no frame or code in between. The text uses the word 'exposed' for these laws.
- Replacement: cor:public-gibbs-channel at L209-213 passes every comparison through a fixed Markov kernel K, with compared laws nu_j = q_j K, and shows the interface then determines the channelled laws 'and nothing more'. The phase theorem is not stated for that channelled version.
- Falsifies: A statement that the identity channel is shorthand for a coded channel, or a coded version of thm:public-phase.

#### fma-11. Incoming Fisher force on a source uses the receiver's law r and row weight beta

- Location: `MAgent_Theory_2.0/chapters/09_public_compression.tex:215`
- Class C, minor
- Quantity: d_t log q_j = beta (K(r/nu_j) - 1); dot nu_j = beta (r - nu_j); dot f_j = alpha_j (r_theta - f_j); kappa_N = 2N/(N-1)
- Evidence: L215: 'The incoming Fisher force of one Gibbs receiver with law r and weight beta on source j is d_t log q_j = beta(K(r/nu_j) - 1).' L224-229: the same force for a restricted receiver family. L72 and L137: the spectral gap 'comes from the receiver and sender roles of the peer costs'. L147-153: 'Including the incoming peer derivative gives' the binary flow.
- Who evaluates: Not stated. The source's law is moved by a quantity that depends on the receiver's own law and attention weight; no return message carrying r or beta is declared.
- Replacement: Receiver-role-only forces would use only received channelled laws nu_j; the file does not state the phase theorem or the gap constant for that case.
- Falsifies: A declared back-action message from receiver to source, or a statement that the flow is describer-level (06_outlook.tex:6 describes the source-role force as the back-action of comparison records in a global model on the linear-Gaussian slice).

#### fma-12. Controls, cavity prior, counterfactual class and exact posteriors are describer-level

- Location: `MAgent_Theory_2.0/chapters/05_global_formation.tex:505`
- Class B, note
- Quantity: null flows, frozen-environment control with Q\_{-i}^{(0)}, cavity prior c_i(y_i) = int p_i(y_i|z) P(dz|o\_{-i},Pi), counterfactual class, MAP structure of the records
- Evidence: L505-511: the nulls give each agent a private copy of (Pi,w,z) and the frozen control uses (Q_i, Q\_{-i}^{(0)}). L446-452: the cavity prior 'uses the records of the other agents'. L304-312, L562-571, L703-708: comparisons with the posterior of the records and the counterfactual handoffs.
- Who evaluates: The analyst: these are control experiments and comparisons used to grade the construction against the formation standard.
- Falsifies: A passage in which an agent uses the cavity prior or a control flow in its own update.

#### fma-13. Retention, lumping and inheritance criteria are maps of the complete configuration, stated as mathematics

- Location: `MAgent_Theory_2.0/chapters/05_inheritance.tex:33`
- Class B, note
- Quantity: R: S -> S^c on the complete agent configuration x; R o F = F^c o R; canonical retention pi(x) = (Q(F^n x))\_n; mixture retention; w = Rot(kappa y) z
- Evidence: L24-35: 'A configuration retention is a measurable map R: S -> S^c'. L83-98, L144-153, L415-426, L519-541: fiber test, projectability, lumpability, canonical parent. L367-375: an example retention 'reads the first agent in a frame turned by the second'. L988-990, L1068-1077: the arithmetic mixture as candidate parent. L1315-1318 and L1454-1473: partition results 'need a cross-agent joint law' and 'are therefore constraints on admissible selectors rather than formation mechanisms'.
- Who evaluates: The analyst; these are existence and uniqueness criteria for a parent description, with classical attributions. No agent is said to evaluate R.
- Falsifies: A statement that a member or the parent computes R(x) from the other members' laws during the dynamics.

#### fma-14. Null flows, frozen-environment control and counterfactual handoff class are control experiments

- Location: `MAgent_Theory_2.0/chapters/05_inheritance.tex:1647`
- Class B, note
- Quantity: Phi^0_lp, Phi^0_rn, Phi^fr; counterfactual class C; membership histories H, P
- Evidence: L1657-1676: the nulls delete peer costs and the frozen control holds 'each law of an agent j != i ... at its initial value'. L1766-1781: the counterfactual class. L1837-1838: 'Clause (F5) is a control experiment'.
- Who evaluates: The analyst grading a construction.
- Falsifies: Use of a control flow or of the counterfactual class inside an agent's update.

#### fma-15. Per-agent frames are stated to be passive re-expressions

- Location: `MAgent_Theory_2.0/chapters/05_inheritance.tex:1030`
- Class B, note
- Quantity: K_ij(u_j k, {u_i l}) = K\_{x_j}(l|k); K'\_ij(g_j v, g_i A) = K_ij(v, A)
- Evidence: L1030-1042: the channel is presented on atoms of both fibers, and 'These frames are per-agent coordinates on each agent's fiber; the identity is a passive re-expression and constrains nothing in the dynamics.' L768-774: 'Neither a parent frame chosen for this purpose nor the square itself determines a base connection.' L1021-1027: the channel parameter depends on the sender's own law only.
- Who evaluates: The describer, for covariance bookkeeping; the transmission coefficient is a function of the sender's own law.
- Falsifies: A cost or force in this chapter whose value changes with u_i or u_j.

#### fma-16. Phase parent is a virtual collective state computed from the whole flow

- Location: `MAgent_Theory_2.0/chapters/09_public_compression.tex:57`
- Class B, note
- Quantity: Pi(x) = lim\_{t -> infinity} phi\_{-t}(mean of Phi_t x); controlled projection with exterior retention R_ext
- Evidence: L56-59: the definition as a limit over the population flow. L122-127: 'the phase parent is evaluated ... by one forward and one backward integration'. L135: 'The parent is a virtual collective state ... Fine states remain unchanged by the construction.' L237-249: controlled projectability is a definition about vector fields and retentions.
- Who evaluates: The describer; the text calls the parent virtual and says nothing is selected.
- Falsifies: A passage in which the phase law enters a child's update or is sampled by an agent as an admitted response (L173 says that 'would specify a new interface').

#### fma-17. Outlook states the status of the three objectives

- Location: `MAgent_Theory_2.0/chapters/06_outlook.tex:6`
- Class B, note
- Quantity: global free energy; per-agent free energies; reciprocal law potential
- Evidence: L6: 'The global free energy is the primary objective for formation, since it alone has an evidence, a target posterior, and one functional that every local update descends; the per-agent free energies describe agent dynamics, and the reciprocal potential is a configuration-level device.' Also L6: 'Every construction of ch:fusion to ch:open-formation concerns the reciprocal potential', and transfer between objectives is open. L16: 'Within the formation constructions the gauge structure supplies the orbits that a parent forgets and does no dynamical work, and the connection remains diagnostic.'
- Who evaluates: The text assigns agent dynamics to the per-agent free energies and calls the reciprocal potential configuration-level; it does not say who evaluates the reciprocal forces in the constructions that use it.
- Falsifies: A statement elsewhere that agents themselves descend the reciprocal potential.

#### fma-18. Agent update in the global model is local to the agent

- Location: `MAgent_Theory_2.0/chapters/05_global_formation.tex:231`
- Class E, note
- Quantity: Q_i^{(n+1)}(dy) proportional to l_i(o_i|y) exp(int log p_i(y|z) Q_nu^{(n+1)}(dz\_{B(i)})) lambda_i(dy)
- Evidence: L230-234: the update reads the agent's own record o_i, its own child kernel p_i and the block-latent law. L92-93: 'Agents interact in this model only through the shared non-agent coordinates. No comparison record ... is included.' L441-445: the parent acts on child i only through that factor.
- Who evaluates: Agent i, given its own record and the block-latent marginal of Q_nu as a received top-down factor.
- Falsifies: An agent update in this chapter that reads another agent's law or record directly.

#### fma-19. Post-handoff parent sweep reads only the block retention R_A

- Location: `MAgent_Theory_2.0/chapters/05_global_formation.tex:337`
- Class E, note
- Quantity: R_B = (lambda_B, hat m_B, hat o_B); parent sweep hat m_B' = a_B hat o_B + b_B (K^c hat m)\_B
- Evidence: L336-341 define the retention; L349-357 the parent sweep; L361-363: 'the channels read by the parent update ... factor through R_A'. L358-360: the parent response is an average of one fresh sample per member. L476-488: the parent is again a model of the same class with the blocks as agents.
- Who evaluates: The parent, from retained block statistics. Forming R_B needs each member's mean, record and both noise variances (see hidden requirements); the text does not say how these reach the parent.
- Falsifies: A step of the parent sweep that reads a member's individual mean or record after the handoff.

#### fma-20. Inherited-parent clauses make the parent independent of members' discarded data after the handoff

- Location: `MAgent_Theory_2.0/chapters/05_inheritance.tex:837`
- Class E, note
- Quantity: clauses (L), (D), (B), (C) of the inherited parent; protocol rule (A)
- Evidence: L837-839: 'Every channel and evaluator read by a protocol in A_I or by the parent update factors through R_I, including its dependence on the configuration.' L781-786: a parent protocol 'addresses I only through channels and records that read the block as a whole; it does not name a member.' L787-793: child-level probes are applied by 'some agent, channel, record kernel, or declared external querier'.
- Who evaluates: The parent and outside receivers, through declared channels and responses.
- Falsifies: A parent update or parent protocol in these files that reads a member's law outside R_I after the handoff.

#### fma-21. Restored messages, parent protocols and stored readout are built from samples and message kernels

- Location: `MAgent_Theory_2.0/chapters/06_fusion.tex:103`
- Class E, note
- Quantity: B_n(k,dw) = LN(log k, 1-1/n)(dw); q_n B_n = LN(mu^q,1); G_n B_n^{h_G} = B_n G_1
- Evidence: L101-116: the message kernel restores unit log variance and is 'the conditional law of one child sample given the parent sufficient statistic'. L133-134: 'a parent can emit the original predictive message by either normalized route'. L198-199: the receiver's law is replaced by its own restored message before comparison. L772-773: 'Retention copies this accessible o exactly; it does not claim access to cached private residual samples.' L796-799: parent protocols address 'the block as a whole'.
- Who evaluates: Sender (its own message kernel), receiver (its own restored message) and parent (retained statistics).
- Falsifies: A comparison cost in this chapter that reads the sender's unrestored law LN(mu_j, 1/n_j) or a cached private sample.

#### fma-22. Shielded channels: the peer cost is a divergence between the receiver's public marginal and the channelled sender marginal

- Location: `MAgent_Theory_2.0/chapters/07_smooth_closure.tex:80`
- Class E, note
- Quantity: K_ij^q[q]((z_j,v_j), d(z_i,v_i)) = B_ij^q[mu](z_j,dz_i) kappa\_{i,z_i}(dv_i); KL(q_i || q_j K_ij^q) = KL(mu_i || mu_j B_ij^q)
- Evidence: L53: private coordinates are those of which 'no channel reads the sender's value'. L68-72: the channel reconstructs the private part with the receiver's own conditional. L78-84: the identity above. L140: 'Private information never influences an interaction in this architecture.' L270: a channel that transmits the sender's private coordinate breaks the per-agent completion.
- Who evaluates: The receiver, from its own public marginal, its own conditional and the channelled public message.
- Falsifies: A peer cost in this chapter that depends on the sender's private conditional kappa_j.

#### fma-23. Marked feedback and row equations use the agent's own records and costs

- Location: `MAgent_Theory_2.0/chapters/07_smooth_closure.tex:292`
- Class E, note
- Quantity: mu^+(dz) = N_z(o) mu(dz)/N(o); eta_z^+; dot theta_jk = -(D_j - D_k) - T_q theta_jk
- Evidence: L277-281: every allowed private readout factors through a declared mark T. L292-300: exact conditioning of the agent's own sector on its own record. L320-328: the row ratio evolves from the receiver's own costs.
- Who evaluates: The agent, on its own law, mark and record.
- Falsifies: A record update in this chapter that conditions one agent's law on another agent's private record.

#### fma-24. Declared public/private observable algebra; preferred sources come from the receiver's own row costs

- Location: `MAgent_Theory_2.0/chapters/08_smooth_erasure.tex:15`
- Class E, note
- Quantity: public coordinate transmitted as samples; row costs D_ij^q; response class reading public coordinates only
- Evidence: L15: 'the peer channel below transmits samples of the public coordinate, it reads the private coordinate of a source only through that source's mean multiplied by the gate, and the admitted response class ... reads public coordinates only'. L148: after closure 'Gibbs ranking uses D_eps alone'. L261: cached private readouts and protocols that inspect discarded private coordinates 'are outside the response class'. L266: each agent's preferred source is the minimizer of its own row cost.
- Who evaluates: Sender (its own private mean), receiver (its own row costs), parent (public empirical measure).
- Falsifies: A response or channel after closure that reads a private or gate coordinate.

#### fma-25. Fixed-channel Gibbs interface retains only channelled laws

- Location: `MAgent_Theory_2.0/chapters/09_public_compression.tex:210`
- Class E, note
- Quantity: nu_j = q_j K; sum_j w_j exp[-KL(r lambda || nu_j)/T]
- Evidence: L209-213: the normalizer 'determines sum_j w_j delta\_{d nu_j/d lambda} and nothing more ... exact compression of this interface is possible precisely on the fibers of q -> qK'. L215: for a deterministic coarse-graining channel 'the incoming force also descends to the channelled laws'.
- Who evaluates: The receiver, from its own law and the channelled laws.
- Falsifies: A response in this corollary that separates two senders with equal channelled laws.

#### fma-26. Outlook records receiver-side dictionaries and lists what agents must exchange as open

- Location: `MAgent_Theory_2.0/chapters/06_outlook.tex:4`
- Class E, note
- Quantity: code, stabilizer, receiver's conditional reconstruction; dictionaries modulo stabilizers
- Evidence: L4: 'General-law reconstruction and identifiability statements distinguish a code, its stabilizer, and the receiver's conditional reconstruction; identification of dictionaries modulo stabilizers assumes a known code.' L8: the interacting-memory composition uses 'a common preparation, private records, and a known posterior-sampling communication protocol'. L42: open problem 'What agents must exchange.' L4 also: 'inheritance of a learned link sector remain[s] open'.
- Who evaluates: Receivers (dictionaries and reconstruction), in chapters outside this lane; the formation chapters of this lane do not use that sector.
- Falsifies: A formation construction in chapters 05 to 09 that already uses receiver-held dictionaries; none was found.

### Hidden requirements

- MAgent_Theory_2.0/chapters/05_global_formation.tex:204 - the block statistic t_B = (lambda_B hat m_B, lambda_B) needs every member's mean and child-noise precision s_i^{-2}.
- MAgent_Theory_2.0/chapters/05_global_formation.tex:338 - the parent record hat o_B is a weighted mean of the members' private records with weights alpha_i = eta_i/(s_i^2 rho_i^2), so forming it needs each member's record and both of its noise variances.
- MAgent_Theory_2.0/chapters/05_global_formation.tex:69 - the kernels r, k and p_i 'do not depend on the block' and the finite catalog with its prior (L45-48) are common structural data assumed known wherever Q_nu is evaluated.
- MAgent_Theory_2.0/chapters/05_global_formation.tex:231 - every sweep each agent must receive the marginal of Q_nu on its own block latent, a top-down factor computed from all agents' laws.
- MAgent_Theory_2.0/chapters/05_global_formation.tex:358 - the parent response protocol averages fresh member samples with weights s_i^{-2}/lambda_B, which requires the members' precisions.
- MAgent_Theory_2.0/chapters/05_inheritance.tex:1543 - the common-clock class assumes a common belief alphabet, one evaluator G_0 for all agents, and a channel C[M] that reads the additive moment M = sum_i E\_{q_i} T of every agent.
- MAgent_Theory_2.0/chapters/05_inheritance.tex:1912 - the anchored-consensus example uses identity channels on a common real line with known unit variances, so each agent reads the other agents' means directly.
- MAgent_Theory_2.0/chapters/05_inheritance.tex:1291 - a handoff needs the actual fine state of all members, including source marks and memory, to initialize the parent.
- MAgent_Theory_2.0/chapters/06_fusion.tex:29 - all laws are 'first written in a common reference coordinate', a shared reference space on which the comparison of restored messages depends.
- MAgent_Theory_2.0/chapters/06_fusion.tex:96 - 'Physical samples are first returned through U_j^{-1}' and the retention keeps the children's frames (L635), without saying whether each child applies its own frame before posting.
- MAgent_Theory_2.0/chapters/06_fusion.tex:226 - an agent's velocity is weighted by the multiplicities n_j of all other agents, which are the senders' log-precisions, and the rows beta_ij = n_j/N (L191) need the population total N.
- MAgent_Theory_2.0/chapters/06_fusion.tex:103 - the message kernel B_n depends on the sender's multiplicity and all agents must share the unit-log-variance comparison family, a public code.
- MAgent_Theory_2.0/chapters/07_smooth_closure.tex:73 - 'Public/private maps and reference factors are declared interface data', and identity channels are admitted only 'between agents sharing a public reference space' (L112).
- MAgent_Theory_2.0/chapters/07_smooth_closure.tex:67 - law-dependent public channels B_ij[mu] may read the public laws of agents other than the sender and the receiver.
- MAgent_Theory_2.0/chapters/08_smooth_erasure.tex:30 - 'All agents have the same reference and evaluator' and 'The bits are reference coordinates', a common species prior and a shared reference space.
- MAgent_Theory_2.0/chapters/08_smooth_erasure.tex:52 - the channel 'uses the source's private mean rather than its private sample', a functional of the sender's private marginal multiplied by the population gate.
- MAgent_Theory_2.0/chapters/08_smooth_erasure.tex:243 - the parent field V[v;M] needs the counting measure of the public states of both pairs, so a parent reads the other parent's full retained state.
- MAgent_Theory_2.0/chapters/09_public_compression.tex:39 - the agents are identical with a common reference R and evaluator, and 'The channels are identities between agents sharing A and B'.
- MAgent_Theory_2.0/chapters/09_public_compression.tex:185 - reading the block normalizer Z(r) as a routing response requires 'a known outside source' and known source weights w_j.
- MAgent_Theory_2.0/chapters/06_outlook.tex:4 - 'identification of dictionaries modulo stabilizers assumes a known code'.
- MAgent_Theory_2.0/chapters/06_outlook.tex:8 - the interacting-memory composition assumes 'a common preparation, private records, and a known posterior-sampling communication protocol'.

## Lane fmb: Multi-agent theory, chapters 10 to 14

Investigator type `audit-gauge-theorist`. No finding in this lane reaches major. The five files contain no transport Omega_ij built from two agents' frames, no receiver-owned dictionary, and no single-system (class D) declaration. Chapters 10 to 12 work with the reciprocal law potential, whose flow reads peer laws and peer routing rows; none of the three says who evaluates that flow, and only 03_dynamics.tex:6 (outside the lane) calls it a configuration-level device, so those uses are class C, minor. Chapter 10 is the weakest case: identity peer channels deliver every peer's full density on a shared public sample space, and the lane has no coded-channel version of the boundary hierarchy. Chapters 13 and 14 use the per-agent own objective built from communicated laws, own evaluator and own records (class E); the two class A items are the declared identity channels that pass a peer's full Bernoulli belief or presentation (model-sector) law. Selectors are global rules with no stated evaluator (class C), while retentions, response protocols and collective connections are stated to be external or diagnostic (class B), except the chapter 14 retention, which leaves the reader unspecified (class C).

### Coverage

- Read in full: MAgent_Theory_2.0/chapters/10_boundary_closure.tex; MAgent_Theory_2.0/chapters/11_conditional_formation.tex; MAgent_Theory_2.0/chapters/12_open_formation.tex; MAgent_Theory_2.0/chapters/13_per_agent_inheritance.tex; MAgent_Theory_2.0/chapters/14_collective_local_parent.tex
- Searched only: MAgent_Theory_2.0/chapters/03_dynamics.tex (read lines 1-62 and 340-409 only, for def:dyn-potential, def:dyn-per-agent, def:dyn-per-agent-flow and the statement on who computes each objective); MAgent_Theory_2.0/chapters/01_foundations.tex, 04_prediction.tex, 05_inheritance.tex, 05_global_formation.tex (label grep only); wiki (grep for privacy axiom and receiver-owned dictionary terms; no matches)
- Not covered: Definitions cited by the lane files but located elsewhere and not read: inh:null-flow, inh:recursive-formation and inh:protocol-classes (05_inheritance.tex), def:observable-algebra (01_foundations.tex), def:dyn-record-interrupted, prop:dyn-gibbs and eq:dyn-incoming (03_dynamics.tex), geo:collective and geo:retained-connection (02_geometry.tex), def:int-channel (02_interactions.tex). Classifications of null and frozen controls and of observable algebras rest on how the lane files describe them.; The vault theme and concept pages on gauge equivariance were not opened; this lane audits access under P, not equivariance.; No scripts, numerical checks or web sources were used, per the task constraints.

### Findings

#### fmb-1. Ch. 13 identity peer channels pass the peer's full Bernoulli belief and presentation law into the agent's own update

- Location: `MAgent_Theory_2.0/chapters/13_per_agent_inheritance.tex:132`
- Class A, minor
- Quantity: peer log odds l_j and n_j in full; costs KL(q_i||q_j), KL(s_i||s_j)
- Evidence: 'three agents with positive Bernoulli belief and presentation laws of log odds l_i, n_i, uniform self reference and evaluator, and identity peer channels' (132); dot l_i = -l_i + sum\_{j != i} beta_ij l_j + eps o_i, dot n_i = -n_i + sum gamma_ij n_j (152-153); 'the peer KL derivative contributes l_i - l_j' (156). The presentation sector is carried into the angular extension: 'Retain the independent Bernoulli presentation laws and priors' (228).
- Who evaluates: Agent i; this is the per-agent objective (5). The identity channel is a declared assumption, and the belief space here is one bit, so the full law coincides with what the chapter calls the public odds (210).
- Replacement: A coded channel in place of the identity. For the content sector the same file has it: the angular extension transmits only mu_j (235, 254). For the presentation (model) sector the only non-identity instance is the four-state nu_j^s = s_j W (50), and that channel is invertible (42).
- Falsifies: A statement that P admits a declared identity channel on a fully public coordinate as a message would make this E. It would also be withdrawn if the presentation law is not the agent's model in the sense of P.

#### fmb-2. Ch. 14 presentation peers use the identity channel, so the peer's full presentation law enters the agent's update

- Location: `MAgent_Theory_2.0/chapters/14_collective_local_parent.tex:32`
- Class A, minor
- Quantity: peer presentation log odds n_j in full; gamma_ij from KL(s_i||s_j)
- Evidence: 'Presentation peers use the identity channel' (32); dot n_i = -n_i + sum\_{j != i} gamma_ij n_j, 'gamma is the original presentation Gibbs row' (60-64).
- Who evaluates: Agent i (per-agent objective, 5 and 9). The identity channel is a declared assumption on a one-bit model space.
- Replacement: A coded channel on the model sector, as nu_j^s = s_j W in 13_per_agent_inheritance.tex:50. Chapter 14 itself has no non-identity presentation channel.
- Falsifies: A statement that P admits a declared identity channel as a message, or that the presentation law is not the model of P.

#### fmb-3. Ch. 10 reciprocal force reads every peer's full density (identity channels) and the peers' routing rows

- Location: `MAgent_Theory_2.0/chapters/10_boundary_closure.tex:54`
- Class C, minor
- Quantity: q_j pointwise (log q_j), q_l/q_i, peer rows beta_li, KL(q_i||q_j)=D_k(f)
- Evidence: h_i^q = log q_i + V_i^q + sum_j beta_ij(log q_i - log q_j) - sum_l beta_li q_l/q_i (54-56); flow dot l_i = -(h_i^q - E h_i^q) (63-64). Declared scope: 'All physical peer channels are identities, every other agent is an allowed source' (32); 'identity channels between agents sharing a reference' (48, 51). Further uses: KL(q_i||q_j)=D_k(f) (77), profile force with P_k log f and P_k f/f 'the incoming source contribution' (102, 111-113), evolving rows (119-121), Gibbs-reduced variant (148), binary pair flow (337).
- Who evaluates: Not stated in this file; the chapter speaks of 'the reciprocal law potential ... and its Fisher flow' (4). Outside the lane, 03_dynamics.tex:6 calls the reciprocal potential 'a configuration-level device' and says the per-agent free energies 'describe what each agent computes'.
- Replacement: Own-objective field with a non-identity (coded) channel, i.e. KL(q_i || q_j K) with the source-role term dropped, as in 13_per_agent_inheritance.tex:16 and :70-73, or the bit-marginal cost of 12_open_formation.tex:30-41. Neither is applied to the boundary hierarchy; the lane has no coded-channel version of thm:boundary-tree-flow.
- Falsifies: A sentence in chapter 10 stating that the reciprocal flow is a configuration-level description not computed by any agent would make this B. A statement that P admits a declared identity channel as a message would remove the full-density part, leaving only the peer rows beta_li (agent l's internal state in the evolving-row version). If instead the flow is meant as each agent's own update under P, this becomes A and major.

#### fmb-4. Ch. 11 channel target and complete force depend on the population moment summed over all agents

- Location: `MAgent_Theory_2.0/chapters/11_conditional_formation.tex:67`
- Class C, minor
- Quantity: M_q = sum_i E\_{q_i} X, Lambda_q = I_2 + kappa M_q/N, C_q, channel-derivative term (kappa/N)(M_q - N alpha_0 Lambda_q^{-1})
- Evidence: K^q_ij[q](k,dX) = W_2(alpha_0, Lambda_q)(dX) (67-69); 'Each channel ignores its particular source sample k but reads the current laws through the total moment. It therefore depends on the whole configuration' (75-76); C_q and dot P = -2P + I_2 + C_q (102-107); h_i(X) = 2 log q_i - 2 c_0 log det X + Tr[(I_2+C_q)X] (128); 'The channel variation is not zero' (131-133); 'Varying another agent's shape ... changes the coefficient of the linear statistic X in the force on q_i' (192); parent energy uses the same C_q (267-273).
- Who evaluates: Not stated. The channel is 'declared' architecture (8) and the text never says an agent computes M_q; line 4 says the chapter 'does not concern the global or per-agent free energies'.
- Replacement: Receiver side: agent i needs only the received channel output law W_2(alpha_0, Lambda_q), which is an aggregate message. The channel-derivative term is a source-role force; an own-objective (per-agent) field omits it (13_per_agent_inheritance.tex:16, :48). Chapter 11 has no per-agent version of this construction.
- Falsifies: A sentence assigning the moment aggregation to an external channel and stating that agents see only its output law, together with a statement that the channel-derivative term is configuration-level, would make this E plus B. A sentence having each agent form M_q from peers' belief means would make it A.

#### fmb-5. Ch. 11 threshold selector reads belief shapes that no declared channel transmits

- Location: `MAgent_Theory_2.0/chapters/11_conditional_formation.tex:307`
- Class C, minor
- Quantity: b_I = A_I/n_I - alpha_0 for every current block, join when |b_I - b_J| reaches delta
- Evidence: Rule at 307-316; 'This rule reads only retained laws and counts, is invariant under relabeling' (318-319); 'Membership is selected by a declared threshold' (8); the channel 'ignores its particular source sample' and reads only the total moment (75), so no message carries alpha_i; 'Already observed sample records remain with the controller' (417-418).
- Who evaluates: The text does not say who applies the rule; a 'controller' holds the records.
- Replacement: Not evident in this file. Chapters 13 and 14 use a selector stated to read public laws only (13_per_agent_inheritance.tex:23, :145).
- Falsifies: A sentence stating that the selector is the theorist's coarse-graining criterion (then B), or one stating that agents themselves decide membership from received content.

#### fmb-6. Ch. 12 reciprocal force contains the incoming term weighted by other receivers' rows

- Location: `MAgent_Theory_2.0/chapters/12_open_formation.tex:57`
- Class C, minor
- Quantity: - sum_k beta_ki mu_k(z)/mu_i(z); binary form sum_k beta_ki (x_k - x_i); limit (w_ij + w_ji)(u_j - u_i)
- Evidence: h_i^q = 2 log q_i - sum_j beta_ij log mu_j - sum_k beta_ki mu_k/mu_i (56-58); 'Varying a source marginal in every incoming row gives -sum_k beta_ki mu_k/mu_i' (65); binary field (107-109); limit field (157); identity-coupled test force h_1 = 2 log q_1 - log r_1 - log q_2 - q_2/q_1 (574). Line 4: 'no statement below is transferred to the per-agent or global free energies'.
- Who evaluates: Not stated; the chapter attributes the field to the reciprocal potential, not to an agent.
- Replacement: With all-source uniform priors and one temperature, beta_ki is a function of the transmitted bit marginals (38-41), so agent i could compute it from received content if it receives every mu_l and knows T and the priors. Otherwise the own-objective field drops the term (13_per_agent_inheritance.tex:16). Chapter 12 has no per-agent version.
- Falsifies: A sentence stating that the reciprocal flow is configuration-level (then B), or that receivers return their weights beta_ki to their sources (then E).

#### fmb-7. Ch. 12 preferential pair selector reads the block rows of all blocks

- Location: `MAgent_Theory_2.0/chapters/12_open_formation.tex:88`
- Class C, minor
- Quantity: B^a_IJ = |I|^{-1} sum\_{i in I} sum\_{j in J} beta_ij and the contrast B^a_IJ - sum_K B^a_IK
- Evidence: Block rows (72-78); 'Its experiment chooses a receiver uniformly in I, draws its native source index, and reports the source block' (79); qualifying rule in both sectors and directions (88-96); 'Rows and events depend only on the bit marginals' (516).
- Who evaluates: Not stated. The inputs are receiver-owned rows, but the rule aggregates them over all agents; line 413 says the querier 'is not an agent of the population'.
- Replacement: Not evident. The inputs are already functions of public bit marginals; what is missing is a statement of who applies the rule.
- Falsifies: A sentence stating that the selector is applied by the external describer or querier (then B).

#### fmb-8. Ch. 13 selectors read public laws of all agents; the evaluator of the selector is unspecified

- Location: `MAgent_Theory_2.0/chapters/13_per_agent_inheritance.tex:140`
- Class C, minor
- Quantity: S_c on (l_i, l_j) or public odds L_i with connected components; conditional-sign selector on all eight conditional means E[a|x], E[b|u]
- Evidence: 'It reads public laws only, treats labels symmetrically' (145); 'the selector reads public laws only' (23); S_c 'applied to the actual public odds L_i' (278); four-state selector: 'all eight conditional means exceed c' (125), computed from the full tables.
- Who evaluates: Not stated. The inputs are communicated laws, but the rule is a global grouping decision.
- Replacement: Not needed for the inputs in the Bernoulli and angular cases, which are public odds. In the four-state case the conditional means are functions of the full table, which the communicated law determines only because K[p] is invertible (42).
- Falsifies: A sentence stating that the selector is the describer's criterion (then B).

#### fmb-9. Ch. 14 whole-block retention and phase memories read every agent's full native parameters and rows

- Location: `MAgent_Theory_2.0/chapters/14_collective_local_parent.tex:111`
- Class C, minor
- Quantity: S = sum_i B_i(x_o), U(S), Omega = det(S,V_S)/|S|^2, S_loc, omega_loc, x(c) = (l_i,A_i,C_i,B_i,n_i)\_i
- Evidence: x(c) in R^24 (99); retention y = R_U x(c) with S = sum_i B_i(x_o) (111-116); 'Retain j_c^2 y, the full finite native tuple x-hat_o, all primitive ports ...' (120); Omega (124-126); 'The reference is deterministic internal memory, not an extra independent sample or agent' (147); omega_loc 'uses the actual native Gibbs rows' (209-220); 'The parent samples the laws at x-tilde' (289); a retention that 'read[s] the entire value path x(c,s)' (378).
- Who evaluates: Not stated. The chapter treats the retention as a realization with memory and says what it reads, but not whether the reader is a system subject to access limits or the describer. l_i, A_i and C_i are not carried by any channel (25).
- Replacement: Not evident. S and S_loc alone are sums of transmitted quantities B_j, so they are formable from received content; the full tuple is not.
- Falsifies: A sentence stating that the parent is a description by the theorist, as 13_per_agent_inheritance.tex:354 says for the phase parent, would make this B. A statement that the parent is the collective itself, whose own state is its children's laws, would make access trivial.

#### fmb-10. Ch. 10 symmetry group, joint spectrum and unordered-profile-tree retention are analysis objects

- Location: `MAgent_Theory_2.0/chapters/10_boundary_closure.tex:191`
- Class B, note
- Quantity: group S of (Phi, varpi), Fix(H_alpha), joint conditional spectrum mu^q = law of (r, q_1(xi),...,q_N(xi)), unordered profile tree
- Evidence: 'they are gauge: no agent, channel, record, or energy term of this construction reads them' (191); group acts by agent permutations and fibered maps (166); spectrum descent (196); parent descriptor 'Retain this tree with unordered children' (218-220); 'These are representation changes inside one fixed N-agent interaction graph' (230).
- Who evaluates: The describer; the text says no agent reads the discarded orbit data and treats the retention as a representation change.
- Falsifies: A passage in which an agent or parent uses the profile tree, the spectrum or a group element in its own update.

#### fmb-11. Ch. 11 additive parents, null and frozen controls and the block-sum response interface are descriptions of one preparation

- Location: `MAgent_Theory_2.0/chapters/11_conditional_formation.tex:232`
- Class B, note
- Quantity: n_I, A_I = sum alpha_i, B_I = sum eta_i, q_I = W_2(A_I,P), pi^c_IJ = n_J/N, Z_Pi = ((X_I,Y_I))
- Evidence: Retention at 232-237 and 242; 'The corollary compares two descriptions of each given preparation' (479); response: 'draw fresh samples independently across children and sectors' and return block sums (439-450); controls Phi^0_rn, Phi^fr (329-330).
- Who evaluates: The describer and an external querier; the parent is a second description of the same fine system.
- Falsifies: A passage in which a parent, acting as an agent, must read the individual child shapes alpha_i or eta_i.

#### fmb-12. Ch. 11 collective connection and curvature are declared diagnostics

- Location: `MAgent_Theory_2.0/chapters/11_conditional_formation.tex:510`
- Class B, note
- Quantity: trivial bundle C x SO(2), common comparison frame, A^F, F^F = dA^F, h^min
- Evidence: 'no vector field, row, channel, or record depends on the connection: the connection below is a diagnostic of the evolved sections' (510); common left action X -> g X g^T on all agents (494-499); A^F and F^F (565-578).
- Who evaluates: The describer, stated explicitly.
- Falsifies: Any update rule, row or channel in the chapter that takes A^F or F^F as input.

#### fmb-13. Ch. 12 anchored retention uses each child's absolute phase and block means; the text places this outside the population

- Location: `MAgent_Theory_2.0/chapters/12_open_formation.tex:324`
- Class B, note
- Quantity: vartheta_i = arg u_i(c\_\*), phi_I = mean of vartheta_i, a_i = phi_I - vartheta_i, q_I = product of tau\_{a_i} q_i, omega_i, omega-bar_I
- Evidence: Anchor (324-330), parent law (333-337), join phase (351-355), moving flow with omega_i 'computable from retained factors' (369-380). 'no agent, channel, row, or evaluator of the population resolves it, and only the external response protocol of the next section can' (317); 'The querier is not an agent of the population ... it reads angles in a fixed angular frame that no agent holds, since every channel twirls the angle' (413).
- Who evaluates: The describer and the external querier, stated explicitly.
- Falsifies: A passage in which a primitive agent, or a parent acting as an agent toward its peers, must know a_i or another agent's absolute angle.

#### fmb-14. Ch. 12 separates the population-readable algebra from the external algebra; connection and holonomy are diagnostics

- Location: `MAgent_Theory_2.0/chapters/12_open_formation.tex:416`
- Class B, note
- Quantity: A_pop, A_P, A^F_t, F^F_t, holonomy of the common connection modulo Z_n
- Evidence: A_pop is generated by 'rows, channel output laws, evaluators, and costs' (416); 'no active rotation is resolved within the population' (418); 'No row, channel, record, or vector field of this construction reads the connection; A^F is a diagnostic of the evolved sections' (427); 'the parent sees the holonomy of the common connection only modulo Z_n' (362).
- Who evaluates: The describer, stated explicitly. The holonomy sentence concerns what the parent description resolves, not an agent computation.
- Falsifies: A row, channel or update in the chapter that takes the connection or a holonomy as input.

#### fmb-15. Ch. 13 phase parent, response protocol and collective geometry are external or diagnostic by declaration

- Location: `MAgent_Theory_2.0/chapters/13_per_agent_inheritance.tex:347`
- Class B, note
- Quantity: hidden phase theta_i, diagnostic E e^{i Psi}, protocol rules A_I and B_I, joint law P\_{c,t}, common S^1 frame change g, connection and curvature F
- Evidence: 'a law functional that no agent, channel, evaluator, record kernel or admitted query reads' (347); 'An external source-label readout does not change the agent's conditioning convention; revealing such a label to the inferring agent would specify another source-row update' (337); 'No claim is made that it is a fixed-size agent with one new source row' (354); 'Under a frame change g, transport phi and the record angle by addition of g' (366); 'does not posit a global latent generative model' (368); 'The common marked connection is a diagnostic of these evolved sections; it does not enter the present dynamical equations' (389).
- Who evaluates: The describer and an external protocol, stated explicitly.
- Falsifies: An agent update in the chapter that takes theta_j, a source label of another agent, or the marked connection as input.

#### fmb-16. Ch. 14 relative-angle queries, marked frame changes and collective Fisher cost belong to the external protocol

- Location: `MAgent_Theory_2.0/chapters/14_collective_local_parent.tex:85`
- Class B, note
- Quantity: c_ij = E e^{i(Psi_i - Psi_j)}, structure group G = S^1, cost C(X,xi), A\_{0,t}, F\_{0,t}
- Evidence: Protocol admits 'relative-angle queries on the complete graph' and 'No absolute psi response is admitted at any stage' (85); pair moment (87-91); 'Only the child-level law diagnostic E e^{i Psi_i}, which no agent, channel, record or admitted query reads, resolves it' (41); 'A passive marked frame change rotates the local embeddings of these fixed lab labels and the evaluator direction' (41); cost identity (157-162); 'a phase field that no agent, channel or admitted query resolves' (328).
- Who evaluates: An external protocol holding 'fixed lab data', and the describer.
- Falsifies: An agent update that takes c_ij from a query, or the marked connection, as input.

#### fmb-17. Ch. 10 broadcast base-only records are assimilated on each agent's own law; responses are an external interface

- Location: `MAgent_Theory_2.0/chapters/10_boundary_closure.tex:240`
- Class E, note
- Quantity: record kernel L_e^q(o|r), update f^+ = L f / Z_o, fresh uniform-descendant response f_l
- Evidence: 'applied as a readout to the original samples of every agent' with Z_o = int f_0 L dA (240-243) and f^+(r,u) = L_e^q(o|r) f(r,u)/Z_o (246); response: 'choose a descendant freshly and uniformly, draw its full original public sample, and conceal its label' (232); 'Unrestricted external identity-channel probes ... are outside the stated inherited interface' (262).
- Who evaluates: Each agent conditions its own law on a record it receives; the response sampling is done by an external protocol.
- Falsifies: A record update whose normalizer or likelihood needs another agent's law beyond the common base marginal f_0.

#### fmb-18. Ch. 12 rows and costs are built from the receiver's own law and received bit marginals

- Location: `MAgent_Theory_2.0/chapters/12_open_formation.tex:30`
- Class E, note
- Quantity: KL(q_i || mu_j x Haar) = H_i^q + KL(mu_i||mu_j), Gibbs row beta_ij
- Evidence: Channel 'transmits the bit and replaces the angle by an independent uniform draw'; 'the bit is the public coordinate ... the angle is a private coordinate'; 'communication between parties that share no angular reference frame' (14-20); cost (30-34); beta_ij from KL(mu_i||mu_j) alone (38-41). This has the coded-marginal form KL(T\_# q_i || T\_# q_j).
- Who evaluates: The receiver, from its own belief and the channel output; A_pop is 'the quantities the population reads: rows, channel output laws, evaluators, and costs' (416).
- Falsifies: A row or cost in the chapter that depends on a peer's angular law f_j(theta|z).

#### fmb-19. Ch. 13 own-objective field uses communicated laws, own evaluator and own records only

- Location: `MAgent_Theory_2.0/chapters/13_per_agent_inheritance.tex:16`
- Class E, note
- Quantity: h_i^q with log nu_j^q, nu_j^q = q_j W; angular field with public odds L_j; rows beta_ij; records H_i^q, o_i, omega_i
- Evidence: 'Each agent changes its own recognition laws while treating the communicated laws of its peers as current model data' (5); 'Each law follows its own agent's Fisher field, so derivatives of another agent's free energy are absent' (16); 'the receiver sees the sender only through pK[p]=pW' (48); potentials (70-73); nonself channel 'copies z and resamples both circles from Haar measure', output mu_j x H x H (235); dot l_i = -l_i + sum beta_ij L_j + eps o_i (254); weights (263-265); 'no agent of the construction reads the hidden angle' (356).
- Who evaluates: Agent i, stated explicitly.
- Falsifies: A term in (70-73) or (254-257) that depends on a peer's non-transmitted coordinates (A_j, C_j, b_j, theta_j) other than through L_j.

#### fmb-20. Ch. 14 transmitted-angle field is built from the received coded law and own data

- Location: `MAgent_Theory_2.0/chapters/14_collective_local_parent.tex:48`
- Class E, note
- Quantity: nu_j(z,phi,psi), w_ij with L_j m_i/2 + B_j . M(B_i), dot B_i = -B_i + sum beta_ij B_j
- Evidence: 'The nonself content channel copies z, psi and resamples phi from Haar measure' (25); transmitted density (27-30); weights (47-50); field (56-60); 'without a Euclidean approximation or source-role forces from other agents' objectives' (68); 'the rows read only B_j . M(B_i) and |B_j|' (41).
- Who evaluates: Agent i, from the channel output and its own law.
- Falsifies: Evidence that B_j . M(B_i) cannot be formed without a psi coordinate shared by sender and receiver that the text does not declare. The copy channel does declare it (25); see hidden requirements.

### Hidden requirements

- All agents share one public sample space with a common reference and public node coordinates theta_v, and identity channels compare densities pointwise in it (MAgent_Theory_2.0/chapters/10_boundary_closure.tex:16, :48, :51).
- The source-role term needs the routing rows beta_li of every receiver that attends to agent i, and in the evolving-row version these are the receivers' own state variables (MAgent_Theory_2.0/chapters/10_boundary_closure.tex:56, :119).
- Admitted records are one base-only likelihood broadcast to every agent, and the common normalizer Z_o relies on all agents sharing the base marginal f_0 (MAgent_Theory_2.0/chapters/10_boundary_closure.tex:240).
- Every channel target needs the total moment M_q summed over all agents, so something must aggregate all belief means, and the complete force also uses the common constants N, kappa and alpha_0 (MAgent_Theory_2.0/chapters/11_conditional_formation.tex:67, :102).
- All agents share the same reference W_2(eta_0, I_2), the same evaluator W_2(alpha_0, I_2) and a common precision in each sector, which is a common species prior (MAgent_Theory_2.0/chapters/11_conditional_formation.tex:62, :8).
- The threshold selector needs each block's belief shape sum A_I, which no declared channel transmits (MAgent_Theory_2.0/chapters/11_conditional_formation.tex:307).
- The bit is a public code known to every agent, with uniform all-source priors 1/N including self and one common temperature, and the receiver must marginalize its own law to the bit to form KL(mu_i||mu_j) (MAgent_Theory_2.0/chapters/12_open_formation.tex:12, :20, :38).
- The reciprocal force on agent i needs beta_ki for every receiver k, computable by i only if it receives every bit marginal and knows the common temperature and priors (MAgent_Theory_2.0/chapters/12_open_formation.tex:57).
- The response protocol assumes an external querier holding a fixed angular frame that no agent holds (MAgent_Theory_2.0/chapters/12_open_formation.tex:413).
- The four-state channel K[p] is invertible, so the communicated law pW determines the sender's full table (MAgent_Theory_2.0/chapters/13_per_agent_inheritance.tex:42).
- Identity peer channels deliver the peer's full Bernoulli belief and full presentation (model-sector) law, on a shared binary alphabet (MAgent_Theory_2.0/chapters/13_per_agent_inheritance.tex:132, :228).
- All agents share one evaluator with fixed direction e_1 and strength J = epsilon^3, homogeneous source priors, and one record likelihood family whose angle omega is given in a fixed lab frame for phi (MAgent_Theory_2.0/chapters/13_per_agent_inheritance.tex:230, :241, :366).
- The content channel copies psi exactly, so sender and receiver must share a psi coordinate for the row term B_j . M(B_i) to be meaningful; only the common rotation of all psi_i is free (MAgent_Theory_2.0/chapters/14_collective_local_parent.tex:25, :41).
- Presentation peers use the identity channel, so the peer's full presentation law is delivered (MAgent_Theory_2.0/chapters/14_collective_local_parent.tex:32).
- The local realization needs reference-context data: the full native tuple of all agents at c_0 and the sum S over all agents (MAgent_Theory_2.0/chapters/14_collective_local_parent.tex:111, :120).
- Geometric inheritance of the causal parent needs the initial collective direction S_loc/|S_loc| to be the same at every context, a preparation condition the recurrence does not generate (MAgent_Theory_2.0/chapters/14_collective_local_parent.tex:283, :296).

## Lane ctx: Multi-agent theory, chapters 15, 16 and 19; notation

Investigator type `audit-gauge-theorist`. Lane magent-coupling-transport: no class-A occurrence in the four assigned files; no sentence there has a named agent compute a cross-agent frame transport, and no transport of the form exp(phi_i)exp(-phi_j) or U_iU_j^{-1} is used as an agent-evaluated quantity. The largest exposure is chapter 15, whose two main theorems are Fisher flows of every agent's law under a global reduced energy: the contextual force uses one collective transport U\*\_e (or A\*) per contextual edge, fixed by a stationarity condition summed over all agents at two contexts, and the local force includes source-role and channel-role derivatives that need receivers' full laws and rows. The text calls this "a direct potential on laws" and never says who evaluates it, so I classed it C; the only agent-local counterpart in the file is the own-block remark, which carries no dissipation identity and still uses the collective transport. Chapter 16 declares itself kinematic with supplied fields and a declared common reference presentation, so its both-frame expressions and collective message matrix are class B. Chapter 19 is the privacy-respecting part of the lane: receiver-owned dictionaries, coded comparison records, and an edge-local stationary dictionary equation, while its global energy, exact dictionary marginal, loop holonomies and rigid parent density are theorist-level. No file states a single-system (class D) scope.

### Coverage

- Read in full: MAgent_Theory_2.0/chapters/15_contextual_coupling.tex (all 1023 lines, in three pages); MAgent_Theory_2.0/chapters/16_link_base_transport.tex; MAgent_Theory_2.0/chapters/19_curvature_hierarchy.tex; MAgent_Theory_2.0/appendices/notation.tex
- Searched only: wiki (one search for privacy-axiom and receiver-owned-dictionary terms; no matches); The three assigned chapters, searched for ownership and evaluator wording (receiver-owned, owner, private, external, theorist); the only hits are 19_curvature_hierarchy.tex:10, :128, :176 and 15_contextual_coupling.tex:74
- Not covered: Chapters that the assigned files cite for definitions: ch:dynamics (the three objectives, def:dyn-restricted-flow), ch:interactions (prop:int-reciprocal), geo:collective, 17_communication_links.tex and 18_link_dynamics.tex (it1:tangent-model, it2:model, the agent-factorized global recognition), ch:inheritance. Several class B and C calls above depend on what those chapters say about who evaluates links, channels and the loop prior.; The vault theme and concept pages on gauge equivariance were not read; the lane question concerns access under P, and the one vault search returned nothing on it.; No scripts, numerical checks or web lookups were run, as the task forbids them; no mathematical correctness of the theorems was checked.; Rows of notation.tex that belong to constructions outside this lane (formation standard, Wishart example, coding construction, record-process and interacting-memory appendices) were read but not classified.

### Findings

#### ctx-1. Collective contextual transport U\*\_e and connection A\* enter every agent's law flow

- Location: `MAgent_Theory_2.0/chapters/15_contextual_coupling.tex:245`
- Class C, major
- Quantity: U_e^\*(p_u,p_v)=argmin_U (1/2)d_N(p_v,U.p_u)^2 over collective laws p_v=(p_iv)\_i; B_v(p)=sum_e w_e Log\_{p_v}(U\*\_{v\<-u}.p_u); continuum A\*\_mu solving k_p(A\*\_mu,xi)=-G_p(d_mu p,J_p xi)
- Evidence: Boxed flow l.245: "dot p_v = -grad_G E_v + (lambda/m_v) B_v(p)", with B_v at l.240 and C\_\* at l.160. The stationarity condition l.110 "G_z(Log_z x, J_z xi)=0" uses the product metric G=sum_i g^F (l.27), so one group element per contextual edge is fixed by all n agents' laws at both contexts. The witness makes this explicit: R\_\*=(CI+SJ)/rho with C=\<Y,X>\_F summed over both agents and both sectors (l.372, l.381). Continuum analogue: normal equation l.553, A\*=-p^\*theta l.564, flow l.630-634 and l.667, alpha\_\*=-\<P_x,JP>\_F/||P||\_F^2 l.939. Because agent i is the same agent at u and v (l.17), the only cross-agent ingredient of agent i's contextual force is U\*\_e. Severity is major on the reading that each agent generates its own velocity; on the theorist reading this is class B.
- Who evaluates: The text does not say. It calls the transports "auxiliary" and says they "follow their algebraic minimizers" while "transport branch selection remain[s] supplied" (l.433); l.128 says the equation "selects comparisons between neighboring collective laws". The remarks on a "numerical branch rule" (l.209) and on discretization (l.954) suggest a modeler integrating the system, but no sentence assigns evaluation to an agent or to an external describer.
- Replacement: My inference: a receiver-selected or per-agent transport in place of the collective U\*\_e. Chapter 16 has a receiver-selected connection at 16_link_base_transport.tex:173 ("Applying the formula gives a receiver-selected connection. Different receivers' selections need not agree") and a flat transport from one agent's own frame at l.48-61, but both are kinematic and are not inserted into any flow; 15:1019 says substituting that selector "would require its full constitutive variation and a new evolution theorem". Chapter 15 has no agent-local contextual force, and its own remarks (l.195 one-agent contexts fail the branch hypothesis for GL(K), K>=3; l.429 "collective laws are needed") indicate a single-agent alignment would degenerate.
- Falsifies: A sentence in chapter 15 or in the chapters it cites (ch:dynamics, geo:collective) stating that the contextual flow is an external description of the population and not a rule each agent executes, or that U_e is supplied to agents as data. Equally, a per-agent version of B_v built only from agent i's own laws at u and v.

#### ctx-2. Reciprocal potential gradient includes source-role and channel-role derivatives

- Location: `MAgent_Theory_2.0/chapters/15_contextual_coupling.tex:74`
- Class C, minor
- Quantity: grad of E_v=sum_i[KL(q_iv x s_iv||R_iv)+sum_j beta_ijv D^q_ijv+...] with d nu^q_ijv=(dq_jv)K^q_ijv+q_jv DK^q_ijv(dp_v)
- Evidence: l.74: "This objective is a direct potential on laws... The derivative of [E_v] contains all receiver, source, and channel roles." l.81: "differentiating a source law must include the costs of receivers attending to it." Also l.6 ("its full derivative includes every receiver, source, and channel role"), l.253 ("All local derivatives include [roles]"), continuum l.512 and l.516. The velocity of source law q_jv therefore contains the derivative of beta_ijv KL(q_iv||q_jv K_ijv) in q_jv, which needs receiver i's full law q_iv and row beta_ijv; the channel-role term needs the derivative of K[p_v] in every law at the context. Theorems ctx:f:thm:ode (l.268) and ctx:c:thm:local (l.712) and both dissipation identities are stated for this gradient.
- Who evaluates: Not stated. The text contrasts the objective with "an agent's own normalized model treating peers as external sources" (l.74), which implies the reciprocal flow is not a per-agent computation, but it does not say who generates it.
- Replacement: The own-block per-agent field A_iv=grad_iv F_iv "with peers held fixed" is in the same file at l.305-310. It is flagged there as a different construction: "the own-block field need not be a gradient", the extra term "has no fixed sign", and l.6 says the chapter "proves no dissipation identity" for it. As written it still adds the collective contextual force of the preceding finding.
- Falsifies: A statement that the reciprocal flow is a population-level description, or that source-role terms are delivered to the source as received messages. Alternatively a dissipation result for the own-block field, which would make the counterpart complete.

#### ctx-3. Peer divergence against a compared law through law-dependent or identity channels

- Location: `MAgent_Theory_2.0/chapters/15_contextual_coupling.tex:58`
- Class C, minor
- Quantity: nu^q_ijv=q_jv K^q_ijv[p_v], D^q_ijv=KL(q_iv||nu^q_ijv); row flow dot beta_ijv=-beta_ijv(h^q_ijv-bar h^q_iv); Gibbs rows beta\*\_ijv proportional to pi^q_ijv exp(-D^q_ijv/T_q)
- Evidence: l.56-61: "For normalized, possibly law-dependent, channels at that same context set nu^q_ijv=q_jv K^q_ijv[p_v], D^q_ijv=KL(q_iv||nu^q_ijv)"; continuum l.498-501 with K[x,p]. Receiver i's row update (l.262, l.642) and Gibbs row (l.300) use D_ij. This is agent-computable only if nu_ij reaches i as a message, and the files do not say so; the channel may depend on the whole collective law p_v. In both witnesses the channel is the identity, so the compared law is the peer's full belief: l.359 "Give each agent the other agent as its singleton source in each sector, with an identity channel" giving ||mu_1-mu_2||^2, and l.918. notation.tex l.46-47 defines the same objects with no evaluator.
- Who evaluates: Not stated. Channels are "fixed" constitutive data (l.72) and "Links between agents at one context remain independent directed communication data" (l.72); the files do not say who applies K_ij or whether the receiver ever holds q_j.
- Replacement: A channel factored as message law then receiver map: notation.tex:48-49 already lists "T_j^a, O_i^a: Sending and receiving maps" and "mu_j: Message law (T_j)\_# q_j", and 19_curvature_hierarchy.tex:176 gives a coded edge cost (beta_e/2)||bar T_e(mu_i-mu_j-omega_e c_i)||^2 in the (R_e+bar T_e Sigma_j bar T_e^T)^{-1} norm. Chapter 15 itself does not restrict K to that form.
- Falsifies: A definition (in ch:interactions or ch:dynamics, outside this lane) that K_ij factors through the sender's message law and a receiver-owned map, so that nu_ij is received coded content; or a statement that the identity-channel witnesses are single-context illustrations with a declared full-belief message.

#### ctx-4. Loop prior wall terms couple dictionaries held by different owners

- Location: `MAgent_Theory_2.0/chapters/19_curvature_hierarchy.tex:211`
- Class C, minor
- Quantity: (lambda/2)||sum\_{e in gamma cap E_b} omega_e||^2\_{W_gamma}, the restriction of the anchored loop prior of it2:model
- Evidence: l.211: "as the anchored loop prior of [it2:model] does around loops containing both... for the Gaussian loop prior this restriction retains the wall terms (lambda/2)||sum\_{e in gamma cap E_b} omega_e||^2\_{W_gamma}... which couple bridge dictionaries." Also l.272 ("above a loop-weight threshold"). A sum of dictionary generators around a walk involves dictionaries of several receivers (l.10 makes each omega_e receiver-owned). This chapter's own model avoids it: l.25 "no explicit loop factor: the loop weight is lambda=0", so none of its theorems depends on the term.
- Who evaluates: Not stated in this file; the prior is defined in it2:model, outside this lane. Here it appears only as a density in a supplied joint model.
- Replacement: The file offers two loop-free or agent-side routes: the evidence-induced coupling at lambda=0 (l.5, l.149 "records couple dictionaries through shared contents in the declared joint"), and a "shared-sample relay around a loop" (l.149) that probes the loop action with the agent's own sample. Neither is written as a replacement objective.
- Falsifies: it2:model stating that the loop prior belongs to a theorist-level joint, or that each owner evaluates it only through relayed records and never through other owners' dictionaries.

#### ctx-5. Receiver-selected connection uses the reciprocal part and the sender's mean

- Location: `MAgent_Theory_2.0/chapters/16_link_base_transport.tex:173`
- Class C, minor
- Quantity: receiver's displayed columns mu_i, Omega_ij mu_j, Theta_ij mu_j, with Omega_ij=Theta_ij(Theta_ji Theta_ij)^{-1/2}
- Evidence: l.173: "A receiver's displayed columns mu_i, Omega_ij mu_j, Theta_ij mu_j also transform by left multiplication by g_i. Applying the formula gives a receiver-selected connection. Different receivers' selections need not agree." This is the lane's closest object to an agent-local transport rule. Two ingredients are not settled as receiver-accessible: Omega_ij contains the reverse link Theta_ji (l.72-78), and the columns need the sender's full first moment mu_j in E_j (l.95), not a low-rank code of it.
- Who evaluates: Implied to be the receiver ("receiver-selected"), but the text does not say the receiver computes it, and chapter 16 does not state who owns Theta_ji.
- Replacement: Drop the reciprocal columns: l.88 already says "The construction may use raw Theta fields directly, without any square-root branch", which leaves mu_i and Theta_ij mu_j (own mean, own link applied to a received mean).
- Falsifies: A statement that links in both directions are available to the receiver, or that the receiver-selected rule is defined with raw-link columns only.

#### ctx-6. Collective message matrix and alignment selector are declared kinematic with supplied fields

- Location: `MAgent_Theory_2.0/chapters/16_link_base_transport.tex:102`
- Class B, note
- Quantity: X(c)=[{bar mu_i},{R_ij bar mu_j},{bar Theta_ij bar mu_j}], C(c',c)=X(c')Q_X(c), a=-dX Q_X, alignment branch t(c',c), B_i=U_i a U_i^{-1}-dU_i U_i^{-1}
- Evidence: X at l.102-104 collects every agent's mean in common reference coordinates, bar mu_i=U_i^{-1}mu_i (l.95); a at l.140; alignment minimizer at l.314-322; dressed form at l.38. Declared scope: l.7 "The selectors are kinematic: they take supplied fields as input and belong to none of the three objectives"; l.13 "On a patch choose a reference presentation of E"; l.173 "The collective reference construction instead selects one a, displayed by all agents"; l.390 "The contextual laws, rows, interfaces and links remain supplied fields; no evolution theorem is implied." notation.tex l.87-90 lists the same objects.
- Who evaluates: An external constructor: the chapter says the selectors take supplied fields and add no evolution equation.
- Falsifies: Any passage in which an agent uses a=-dX Q_X or t(c',c) in its own update. Chapter 15 l.1019 says this substitution has not been made.

#### ctx-7. Both-frame expressions for links are re-expressions between presentations

- Location: `MAgent_Theory_2.0/chapters/16_link_base_transport.tex:25`
- Class B, note
- Quantity: Theta_ij=U_i bar Theta_ij U_j^{-1}; bar Theta_ij=U_i^{-1}Theta_ij U_j; R_ij=U_i^{-1}Omega_ij U_j; Omega_ij'=g_i Omega_ij g_j^{-1}; N_ij,j=Theta_ji Theta_ij
- Evidence: l.25: "Theta_ij=U_i bar Theta_ij U_j^{-1}: E_j -> E_i"; l.97-98 the inverse relations; l.82 the passive law; notation.tex l.45 (backtrack) and l.89 ("U_i^{-1}Theta_ij U_j and U_i^{-1}Omega_ij U_j"). These have the two-frame form P lists as inaccessible, but they relate a link's agent-coordinate and reference-coordinate presentations; with bar Theta=I the first would be U_iU_j^{-1}, and the text never sets that. l.29 gives the example bar Theta_ij=exp(L_ij), L_ij=O_i T_j, a receiving-sending product "that may depend on the current laws". The reciprocal part Omega_ij needs both directed links. Links are "supplied fields" (l.390).
- Who evaluates: An external describer, by the chapter's declared kinematic scope (l.7, l.390); no agent is said to form Theta_ij from U_j.
- Falsifies: A passage (for instance prop:int-reciprocal in the interactions chapter, outside this lane) where an agent constructs its link from the sender's frame U_j or computes Omega_ij itself; that would make this class A.

#### ctx-8. Global posterior energy, exact dictionary marginal and loop holonomies are analysis of a declared joint

- Location: `MAgent_Theory_2.0/chapters/19_curvature_hierarchy.tex:65`
- Class B, note
- Quantity: E(y,omega); S_marg(omega) with C_P=R+delta P^{-1}delta^T; Lambda_omega; pi(d omega|o); (B omega)\_gamma=sum\_{e in gamma} omega_e; H_gamma; bar theta_g bar theta_e; Q(H;Sigma); KL(q||H\_# q)
- Evidence: l.12 "The comparison records and global posterior energy"; l.63-75 S_marg and Lambda_omega; l.57 the dictionary posterior. C_P couples every agent's self precision, code and noise. The text separates this from what owners hold: l.128 "The precision Lambda_omega and the coupling of dictionaries through shared contents belong to the exact dictionary marginal. Under the agent-factorized global recognition of [ch:link-dynamics] the optimal recognition covariance has no cross-owner blocks, and only the stationary means carry the induced action." Loop quantities appear in results about stationary states (l.180-188, l.242-250) and in a remark comparing observables (l.142-147); l.149: "The evidence calculation requires neither direct loop observations nor such an identification procedure."
- Who evaluates: An external analyst of the declared joint model; no owner is said to minimize S_marg or evaluate a loop product.
- Falsifies: A passage in which a dictionary owner minimizes S_marg or uses Lambda_omega, C_P or a loop product in its own update.

#### ctx-9. Supplied hierarchy and rigid parent density pool the children's self densities

- Location: `MAgent_Theory_2.0/chapters/19_curvature_hierarchy.tex:213`
- Class B, note
- Quantity: p_A'(z)=Z_A^{-1}p_A(z)prod\_{i in I}p_i(z); P_A'=P_A+sum_i P_i; cross-scale factor exp(-(tau/2)||y_i-y_A-omega_iA c_A||^2)
- Evidence: l.213 parent density; l.220-221 Gaussian parameters; l.40 cross-scale factor "with identity code" (l.44). The parent self density is a functional of every child's self model and exists only on a common content space with a common reference measure (l.206). Declared scope: l.44 "The partition, parents, and cross-scale factors are supplied model data"; l.266 "These statements do not select a partition... or construct an inherited response and update kernel." Ownership of the cross-scale dictionary omega_iA is not stated.
- Who evaluates: An external constructor restricting the joint density; the text says the hierarchy is supplied and claims no formation dynamics.
- Falsifies: A passage where a parent agent computes p_A' from its children's densities, or where children evaluate the identity-code cross-scale factor as part of an update.

#### ctx-10. Receiver-owned dictionaries, coded comparison records and an edge-local stationary equation

- Location: `MAgent_Theory_2.0/chapters/19_curvature_hierarchy.tex:10`
- Class E, note
- Quantity: omega_e (receiver-owned), bar T_e, R_e; o_e=bar T_e(y_i-y_j-kappa_i omega_e)+eps_e; exact form bar T_e(e^{-omega_e}y_i-y_j); stationary omega_e; effective code hat A=bar T bar theta^{-1}
- Evidence: l.10: "An edge e: j -> i has receiver-owned dictionary generator omega_e in gl(K,R), code bar T_e... and positive-definite noise covariance R_e." The record (l.14) and its exact form (l.25) compare the receiver's reinterpreted content with the sender's coded content, the same shape as KL((T Theta^{-1})\_# q_i || T\_# q_j). The stationary dictionary equation (l.157-159) uses only bar T_e Delta_e, o_e and c_i; l.171 "Only the anchor and the edge record depend on omega_e"; l.176 "In the per-agent objectives only the owner's record and anchor contain this dictionary." The law-level variants need the sender's covariance only in coded form, bar T_e Sigma_j bar T_e^T (l.169). notation.tex l.91 lists "the effective code hat A=bar T bar theta^{-1} that messages identify" and l.48-49 the message law (T_j)\_# q_j.
- Who evaluates: The dictionary's owner, the receiver (l.10, l.176).
- Falsifies: A use of omega_e, in these files, by an agent other than its receiver, or a record that depends on y_j other than through bar T_e.

### Hidden requirements

- Chapter 15 needs fixed comparisons S_iv that place every agent's joint law in compatible target spaces at each context, i.e. a shared target space, declared as supplied data (MAgent_Theory_2.0/chapters/15_contextual_coupling.tex:24, continuum form at :461).
- Chapter 15 has one group element act on all agents and both sectors at a context by diagonal pushforward, so the contextual transport is common to the collective and not per agent (MAgent_Theory_2.0/chapters/15_contextual_coupling.tex:33).
- Chapter 15 identifies agent i across contexts, so the edge cost compares agent i at u with agent i at v and each agent needs its own law at neighboring contexts (MAgent_Theory_2.0/chapters/15_contextual_coupling.tex:17).
- The comparison channels K_ij[p_v] may depend on the whole collective law at the context, so applying or differentiating a channel needs every agent's law there (MAgent_Theory_2.0/chapters/15_contextual_coupling.tex:56, continuum form at :498).
- Both worked witnesses in chapter 15 use identity channels, which makes the peer's full belief the compared law (MAgent_Theory_2.0/chapters/15_contextual_coupling.tex:359 and :918).
- The transport branch is continued along the solution and is not a function of the current laws, so whoever evaluates the flow must carry the collective transport state U\*(t) as memory (MAgent_Theory_2.0/chapters/15_contextual_coupling.tex:283).
- Chapter 16 requires a common reference presentation of E on a patch and each agent's invertible map U_i from it, so reference means bar mu_i=U_i^{-1}mu_i need every agent's frame (MAgent_Theory_2.0/chapters/16_link_base_transport.tex:13 and :95).
- The reciprocal part Omega_ij=Theta_ij(Theta_ji Theta_ij)^{-1/2} needs both directed links of a pair, which amounts to an exchange of links between the two agents (MAgent_Theory_2.0/chapters/16_link_base_transport.tex:72).
- The message construction assumes persistent message labels identified across contexts and a fixed context-independent message metric (MAgent_Theory_2.0/chapters/16_link_base_transport.tex:93).
- The example link generator L_ij=O_iT_j is a product of a receiver map and a sender map in reference coordinates and may depend on the current laws, without saying whose laws (MAgent_Theory_2.0/chapters/16_link_base_transport.tex:29).
- Chapter 19 works in one reference content space R^K with codes and dictionaries written in reference coordinates, a shared reference space (MAgent_Theory_2.0/chapters/19_curvature_hierarchy.tex:10).
- The same code bar T_e is applied to the receiver's and the sender's contents on an edge, so the receiver must know the sender's code (a public code) or hold the effective code bar T bar theta^{-1} (MAgent_Theory_2.0/chapters/19_curvature_hierarchy.tex:33).
- The law-level and reciprocal versions of the stationary dictionary equation need the sender's covariance in coded form, bar T_e Sigma_j bar T_e^T, i.e. a posted coded covariance (MAgent_Theory_2.0/chapters/19_curvature_hierarchy.tex:169).
- Several chapter 19 results assume a common operating content c shared by all receivers (MAgent_Theory_2.0/chapters/19_curvature_hierarchy.tex:96 and :180).
- The cross-scale factor of the supplied hierarchy uses an identity code, so the parent's full content is the compared object (MAgent_Theory_2.0/chapters/19_curvature_hierarchy.tex:44).
- The rigid restriction requires child and parent contents in one standard Borel space with a common sigma-finite reference measure, and identity internal and cross-scale dictionaries (MAgent_Theory_2.0/chapters/19_curvature_hierarchy.tex:206).
- Probing a loop needs either a shared-sample relay around it or identification of the constituent dictionaries from grounded edge records followed by composition, the latter requiring access to dictionaries of other owners (MAgent_Theory_2.0/chapters/19_curvature_hierarchy.tex:149).
- The notation appendix defines laws bar q_i, bar s_i in common reference coordinates on a trivializing patch and frames U_i relative to one reference point sigma (MAgent_Theory_2.0/appendices/notation.tex:42 and :39).

## Lane lnk: Multi-agent theory, chapters 17 and 18

Investigator type `audit-gauge-theorist`. Both chapters work in reference coordinates with receiver-owned dictionaries, and no agent objective in either file is a full-belief transported divergence: reception, identification, source rows and the reciprocal edge cost are all built from message laws, the receiver's own prior, and a receiver-held dictionary. One conflict with P is rated major: with lambda > 0 the per-agent objective E_i in chapter 18 contains the means and covariances of dictionaries owned by other receivers (full gl(K) elements, not coded content). The text states that this needs agents to exchange how they read each other and lists the protocol as an open problem; the lambda = 0 path is free of it. Three source-side or sender-side dependencies are minor: the global flow moves a sender through a record held by the receiver, the reciprocal potential moves a source through the receiver's row weight and predicted message law without declaring a return message, and the chapter 17 receiver-factor remark needs other agents' dictionary means. The rest are wording issues where an inaccessible-looking symbol (displayed theta_ij with U_j^{-1}, transported sender mean, "peer laws as data") reduces identically to coded content, plus declared hypotheses that the lane records as hidden requirements: a known sender code, a common reference presentation with identity anchor, supplied message laws with coded covariance, and co-observed referents. Chapter 18 contains no frame symbol and no ground-truth dictionary; chapter 17 uses the true dictionary only in describer-level theorems, one of which says outright that the quantity cannot be estimated from messages.

### Coverage

- Read in full: MAgent_Theory_2.0/chapters/17_communication_links.tex (lines 1-522); MAgent_Theory_2.0/chapters/18_link_dynamics.tex (lines 1-666)
- Searched only: MAgent_Theory_2.0/chapters/02_interactions.tex (label lookup for def:int-group-links and prop:int-loop-defect only); MAgent_Theory_2.0/chapters/03_dynamics.tex (label lookup for def:dyn-potential, def:dyn-per-agent, def:dyn-restricted-flow only; bodies not read); MAgent_Theory_2.0/chapters (keyword search for a declared return or reverse channel and for describer-level wording; only two unrelated hits in 05_inheritance.tex); wiki (search for an existing verdict on receiver-owned dictionaries or a privacy axiom; no matches)
- Not covered: ch:foundations and ch:dynamics, which these chapters cite for the common reference presentation, the observable-algebra convention, the three objectives, prop:conditional-lift and cor:pythagorean; whether they declare who evaluates the global joint or the reciprocal potential was not checked; The model-sector (varrho_s) version of the constructions, which chapter 17 line 7 mentions and does not develop; The vault theme and concept pages on gauge equivariance, which were not opened because the task was limited to the two assigned files; references.bib and the cited primary sources (no web access in this lane); No symbolic or numerical check was run on any formula; the reductions cited (A-hat theta-bar = T-bar, coded dependence of q-hat and of E_i) were verified by hand from the displayed equations

### Findings

#### lnk-1. Per-agent objective contains loop factors built from dictionaries the agent does not own

- Location: `MAgent_Theory_2.0/chapters/18_link_dynamics.tex:40`
- Class A, major
- Quantity: a_f and V_f for f in gamma minus in(i) (means and covariances of dictionary laws r_f owned by other receivers); Omega\_{i gamma}; off-diagonal blocks of A_omega = sigma^{-2} I + lambda B^T W B + diag(G_e)
- Evidence: Line 36: "Fix agent i and the current peer laws, ... r_f=N(a_f,V_f) for the dictionaries that i does not own." Line 40: loop term || sum\_{e in gamma cap in(i)} omega_e + sum\_{f in gamma minus in(i)} a_f ||^2\_{Omega\_{i gamma}}. Line 47: Omega\_{i gamma} = ((lambda W_gamma)^{-1} + sum_f V_f)^{-1}. Line 54: "agent i holds a Gaussian Q_i on x_i and lowers its own free energy F_i." Same dependence at 27 (global loop term), 128-130 (covariance map Phi reads V_f), 199-205 (echo and cavity use partners' dictionary laws), 249 (E\_{r\_{-e}} log pi_omega), 271, 329, 345 ("Off-diagonal prior blocks still couple the dictionary means"), 354, 401. a_f is a full element of gl(K), not a coded quantity. The text concedes the requirement at 664-665: "A receiver using a loop prior needs information about dictionaries owned elsewhere ... Formulate that exchange through declared codes and record kernels" (listed as an open problem).
- Who evaluates: Agent i: it "lowers its own free energy" (line 54), with the peer dictionary laws declared "parameters of i's model and not variables over which it infers" (line 52). The text does not say how those parameters reach agent i.
- Replacement: None in the two files for lambda > 0. The lambda = 0 path is declared and reachable (line 50: "At lambda=0 the loop terms are omitted"; used in the three-agent theorem at line 466) and has no dependence on other agents' dictionaries. The cavity variant (line 205) still needs partners' dictionary laws with one contribution removed. A coded exchange of dictionary information is named as open at 664-665.
- Falsifies: A passage in these chapters or the definitions they cite that declares the dictionary laws r_f public or transmitted by a specified message, or a statement that E_i with lambda > 0 is a describer's device and not an objective an agent lowers.

#### lnk-2. Global flow moves the sender through a record held by the receiver

- Location: `MAgent_Theory_2.0/chapters/18_link_dynamics.tex:119`
- Class A, minor
- Quantity: On an edge e: j -> i, the registered record o_e and the receiver's coded prediction T_e(mu_i - kappa_i a_e), entering the sender j's block of the gradient of the global free energy F_G; also the loop terms of the previous finding
- Evidence: Line 5: "A global model differentiates every comparison record at both endpoints." Line 54: "each local update varies one factor of a single global free energy." Line 119: "(iii) Each agent's block of the force is the gradient of its local free energy, the global free energy as a function of its own factor. A record therefore moves the receiver's content, the sender's content and the receiver's dictionary through one functional." Further uses: 26 (E(x) sums all records), 89-91 (delta y_j = -Sigma_j^0 T_e^T S^{-1} r in the global joint), 171 (E_known). The needed data are message-space objects of rank n_e, but they sit at the receiver and the edge runs j -> i.
- Who evaluates: The text assigns each block to the agent's "local free energy" but does not say how the sender obtains the receiver-held record. I am unsure whether the global joint is meant as an agent protocol or as the reference objective against which the per-agent model is compared.
- Replacement: The per-agent record model in the same file: lines 36-54 and 136-147, with line 52 "Agent i's model contains no record in which i is the sender" and line 147 "Ownership removes sender-role content derivatives from the per-agent update."
- Falsifies: A statement that o_e and the receiver's coded prediction are returned to the sender, or that the global joint is a describer's benchmark that no agent follows.

#### lnk-3. Loop prior: joint posterior over all receivers' dictionaries, and a receiver factor that needs other agents' dictionary means

- Location: `MAgent_Theory_2.0/chapters/17_communication_links.tex:504`
- Class A, minor
- Quantity: Joint law on omega in g^E with precision Lambda_0 = Pi_0 + lambda B^T W B; linearized holonomy (B omega)\_gamma = sum\_{e in gamma} omega_e over edges owned by different receivers; means of dictionaries held by other agents; the base agent's covariance inside a dressed W_gamma
- Evidence: Line 292: prior density exp(-1/2 omega^T Pi_0 omega - lambda/2 sum_gamma ||(B omega)\_gamma||^2\_{W_gamma}). Lines 303-305: one information filter updates the joint (Lambda, eta) with every edge's messages. Line 308: "This is one normalized joint over the dictionaries of all receivers, so the tangent learning model is the global picture." Line 504: "To update its factor, receiver i needs the current means of the dictionaries that other agents hold along its loops: a loop prior can be used only if agents communicate about how they read each other, in addition to communicating about the world." Lines 252 and 312: the GL(K)-covariant loop form uses "the reference covariance of the belief of the agent at which gamma is based".
- Who evaluates: For the joint posterior the holder is not named beyond "the global picture". For the factorized version it is receiver i (line 504), and the text states the requirement itself.
- Replacement: None in the file for lambda > 0. With lambda = 0 only the receiver's own anchor remains (line 385: "With an isotropic anchor and no loop term, the recognition law on the invisible coordinates stays at its anchor marginal"). Rated minor because the chapter's theorems (it1:learning, it1:complementary) are stated for the declared joint and line 504 is a remark that discloses the requirement.
- Falsifies: A declared mechanism that makes other receivers' dictionary means, and the base agent's covariance, available to each receiver on the loop.

#### lnk-4. Reciprocal potential moves a source through the receiver's row weight and predicted message law, with no declared return message

- Location: `MAgent_Theory_2.0/chapters/18_link_dynamics.tex:353`
- Class C, minor
- Quantity: For source i on e in out(i) with receiver k: beta_e; d_e = T_e(mu_k - mu_i - kappa_k a_e); Q_e = S\_{k,e} + d_e d_e^T + K_e V_e K_e^T; the summed potential E_T
- Evidence: Line 218: "It moves each source through the costs of receivers that attend to it." Line 353: g\_{mu_i} contains "- sum\_{e in out(i)} beta_e T_e^T J_e d_e". Lines 357-358: 2G\_{Sigma_i} contains "sum\_{e in out(i)} beta_e T_e^T (J_e - J_e Q_e J_e) T_e". Also 279, 298 (source-covariance derivative), 318 ("the source matches ... its own posterior reconstruction of the receiver's message law"). Results that rest on these terms: 409 (global existence and convergence), 466-477 (threshold), 556-574 (pitchfork). Everything the source needs from the receiver is a message-space object of size n_e plus one scalar, and line 266 already describes m_e^rec as "the law of the message the receiver would send about its own content read in the sender's coordinates".
- Who evaluates: Not stated. The flow is written as the "unit-mobility product Fisher equations" of one potential (line 363); no sentence says whether sources compute their own block or a describer integrates the system.
- Replacement: Declare a return message from receiver to source carrying beta_e and the first two moments of the dictionary-averaged predicted message law (mean T_e(mu_k - kappa_k a_e), covariance S\_{k,e} + K_e V_e K_e^T); the formulas are unchanged. The files do not declare it. The receiver-only truncation is the per-agent law-level model by line 281 (iv), whose flow the text shows can be non-gradient (line 156) and whose convergence is open (line 656).
- Falsifies: A declared reverse message, or a statement that the reciprocal flow is a population-level description; def:dyn-potential in 03_dynamics.tex (outside this lane, label looked up only) may settle it.

#### lnk-5. "Peer laws as data" is worded as the full sender law; the equations use only its coded marginal

- Location: `MAgent_Theory_2.0/chapters/18_link_dynamics.tex:36`
- Class C, minor
- Quantity: q_j = N(mu_j, Sigma_j), the sender's full content law, against the coded marginal N(T_e mu_j, T_e Sigma_j T_e^T)
- Evidence: Line 5: "treating the source law as data". Line 36: "Fix agent i and the current peer laws, q_k=N(mu_k,Sigma_k) for contents". Line 94: "with the sender's law N(m_j,Sigma_j^0) as data". The equations read the sender only through T_e mu_j (line 39) and R~\_e = R_e + T_e Sigma_j T_e^T (line 46); line 52 gives the convolution; the plug-in model uses the coded mean alone (line 50).
- Who evaluates: Receiver i.
- Replacement: State the data as the sender's message law m_e^src = N(T_e mu_j, S\_{j,e}), which the file already defines at line 263. The law-level model then needs a posted coded covariance; the plug-in model needs only the coded mean.
- Falsifies: Any term of E_i that depends on mu_j or Sigma_j outside T_e(.). I found none.

#### lnk-6. Chapter 18 uses the sender's reference code inside the receiver's prediction without restating the known-code hypothesis

- Location: `MAgent_Theory_2.0/chapters/18_link_dynamics.tex:15`
- Class C, minor
- Quantity: The sender's reference code T_e as a separate known factor in A_i = T_e theta_e^{-1}, in K_e = T_e kappa_i, and in N_e = {delta : T_e delta = 0}
- Evidence: Line 12: "A_i = T_e theta_e^{-1}, the receiver's prediction of the message from its own content translated into the sender's coordinates." Line 15: "the sender's attending code T_e". Line 20: "All codes, operating contents, grounding data, and prior forms are fixed." No sentence in this file says the receiver knows T_e. Chapter 17 declares the hypothesis where it uses it: 17_communication_links.tex:30 ("Codes are agent specific ... a shared language is an additional declared hypothesis"), :141 ("Assume that the receiver knows the sender's reference code"), and :157 ("If the reference code is unknown, the grounded experiment therefore identifies A-hat and nothing about theta separately").
- Who evaluates: The receiver, in forming its prediction and its record model.
- Replacement: The receiver-owned effective code A-hat_e = T_e theta_e^{-1} (17_communication_links.tex:43) or the reading S of it1:query-dictionary (17_communication_links.tex:203-208). Splitting it into T_e and omega_e, and defining N_e, needs the known-code or shared-language hypothesis, which exists in chapter 17 but is not carried into the chapter 18 model definition.
- Falsifies: A sentence in chapter 18, or in a definition it cites, that carries the known-code hypothesis into the tangent communication model.

#### lnk-7. Displayed dictionary is defined with both agents' frames and headed as the receiver's object

- Location: `MAgent_Theory_2.0/chapters/17_communication_links.tex:35`
- Class C, minor
- Quantity: theta_ij = U_i theta-bar_ij U_j^{-1}; at theta-bar_ij = I this is U_i U_j^{-1}
- Evidence: Lines 33-35: "Receiver i's dictionary for sender j is theta_ij = U_i theta-bar_ij U_j^{-1} in G". Line 41: "It is owned by the receiver: it is i's hypothesis about how j's internal reference coordinates sit relative to its own." Line 50: "the bundle identification of the two frames is itself the value theta-bar_ij = I". Every later calculation uses the reference value: line 43 (A-hat = T-bar_j theta-bar_ij^{-1}), line 55 ("In i's reference coordinates"). A search of chapter 18 for U_i, U_j and g_i g_j returns nothing.
- Who evaluates: Not stated for the displayed element. The owned hypothesis is the reference value theta-bar_ij (line 41); the displayed formula reads as covariance bookkeeping, but the heading attributes it to the receiver.
- Replacement: theta-bar_ij, or the effective code in the receiver's displayed coordinates, T-bar_j theta-bar_ij^{-1} U_i^{-1}, which uses only the receiver's own frame. The file has the reference-coordinate form at line 43.
- Falsifies: A step in which the receiver evaluates theta_ij in displayed coordinates or otherwise needs U_j. I found none in the two files.

#### lnk-8. Reception formulas are written with the transported sender belief but depend on it only through the code

- Location: `MAgent_Theory_2.0/chapters/17_communication_links.tex:122`
- Class C, minor
- Quantity: q = (theta-bar)\_# q-bar_j; theta-bar_ij mu-bar_j; the sender moments a and Sigma_q in the receiver's coordinates
- Evidence: Line 55: "let q=(theta-bar)\_# q-bar_j be the sender's belief carried into i's coordinates by the dictionary." Line 122: mu_i' = mu_i + O_0 A-hat_ij (theta-bar_ij mu-bar_j - mu_i). Lines 84 and 113: reconstruction moments written with a and Sigma_q. Since A-hat_ij theta-bar_ij = T-bar_j, the update equals mu_i + O_0 (T-bar_j mu-bar_j - A-hat_ij mu_i), and Sigma_q enters only as A Sigma_q A^T (line 117: "Mixing over h ~ N(Aa, A Sigma_q A^T)").
- Who evaluates: The receiver, in the reconstruction; the text does not say at line 122 that only the message-law mean is used.
- Replacement: Write the update with the message-law mean T-bar_j mu-bar_j and the coded covariance. The file states the principle at lines 59-62 ("It keeps exactly what the code transmits, the message law T\_# q") and at line 72 ("q-hat depends on the dictionary only through the effective code").
- Falsifies: A term of q-hat that depends on a or Sigma_q outside A(.). I found none.

#### lnk-9. Consensus condition is glossed as a comparison each receiver performs on the sender's full belief

- Location: `MAgent_Theory_2.0/chapters/17_communication_links.tex:233`
- Class C, minor
- Quantity: mu_i = theta-bar_ij mu_j; q_i = (theta-bar_ij)\_# q_j; consensus energy E(mu) = sum w_ij ||mu_i - theta-bar_ij mu_j||^2
- Evidence: Line 230: mu_i = theta-bar_ij mu_j for every edge. Line 233: "so that every receiver, translating each sender's belief through its dictionary, finds agreement." Line 236: transported consensus laws q_i = (theta-bar_ij)\_# q_j. Line 244: E(mu) as a positive-semidefinite form over all edges. No update rule in the file minimizes E(mu).
- Who evaluates: The theorem and corollary (236, 244) are statements about a configuration. The gloss at 233 has receivers doing the comparison, which would need the full sender mean.
- Replacement: The coded test already in the file at line 262: "Comparing coded means tests the weaker condition T-bar_j^c (mu_j - theta-bar_ij^{-1} mu_i) = 0 on each edge and modality."
- Falsifies: A statement that the consensus condition is defined for the describer only, or an agent rule that evaluates mu_i - theta-bar_ij mu_j.

#### lnk-10. True dictionary, truth omega-star and coboundary truth appear only in describer-level theorems

- Location: `MAgent_Theory_2.0/chapters/17_communication_links.tex:72`
- Class B, note
- Quantity: KL(q || q-hat) = KL(q || p) - KL(T\_# q || T\_# p) with q = (theta-bar)\_# q-bar_j; C = theta-bar^{-1} M theta-bar^{-T}; omega-star; theta-bar-star_ij = g_i g_j^{-1}
- Evidence: Line 67: loss identity containing the full-belief divergence KL(q || p). Line 72: "The loss is evaluated at the true dictionary ... and therefore cannot be estimated from messages". Line 147: Fisher form at the dictionary point. Line 328: "let the truth be omega-star". Line 472: "true dictionaries of two agents be reciprocal". Line 486: "Let the truth be a coboundary configuration, theta-bar-star_ij = g_i g_j^{-1}". Line 278: data-processing comparison KL(qK || q_j K) \<= KL(q || q_j).
- Who evaluates: An external describer. Line 72 says the loss cannot be estimated from messages; the remaining items are hypotheses and conclusions of identification and consistency theorems.
- Falsifies: An agent update or objective in the file that takes the loss, omega-star, or g_i g_j^{-1} as an input.

#### lnk-11. Holonomy, dissonance, frustration and detectable dissonance are defined and analyzed, not assigned to an agent

- Location: `MAgent_Theory_2.0/chapters/17_communication_links.tex:228`
- Class B, note
- Quantity: H_gamma = product of receivers' dictionaries along a closed walk; Q(H_gamma; Sigma\_{i_0}); KL(q || H\_# q); D(omega) = min\_{nu in N} ||B(omega + nu)||^2_W
- Evidence: Line 228: holonomy as "the composite of the receivers' dictionaries along the walk". Lines 236 and 244-246: consensus and frustration theorems. Line 252: dissonance and the dressed defect "with the covariance of the base agent". Line 260: KL(q || H\_# q) introduced as a comparison; no agent minimizes it. Lines 392 and 400: detectable dissonance, "messages determine it" (the messages of every edge on the loops). Line 409: "the community assumes an agreement it cannot check".
- Who evaluates: Describer-level definitions and theorems. These quantities become agent-level only through the loop prior, which is reported separately.
- Falsifies: An agent rule in the file that evaluates H_gamma or D(omega) outside the loop prior.

#### lnk-12. Gauge, identification, equivalence and dissipation statements in chapter 18 are about the system

- Location: `MAgent_Theory_2.0/chapters/18_link_dynamics.tex:63`
- Class B, note
- Quantity: Invariance subspace G of the record laws; Fisher information of the records; E^S; dissipation of E_T; reduced Hessian H_red
- Evidence: Lines 60 and 63-72: the record law depends on (y, omega) only through coded discrepancies, with kernel G. Lines 276-280: E = E^S(mu, a) + c(Sigma, V). Lines 387-394: dissipation identity summed over all agents and edges. Line 409: global existence and convergence. Lines 438-445: Hessian and stability indices.
- Who evaluates: A describer; these are theorems about the declared objectives and flows, and no agent is said to compute E_T, its dissipation or its Hessian.
- Falsifies: A rule that has an agent evaluate the summed potential or its Hessian.

#### lnk-13. Attention-heads remark is a comparison; no single-system scope is declared

- Location: `MAgent_Theory_2.0/chapters/17_communication_links.tex:223`
- Class D, note
- Quantity: Query, key, value and output maps of multi-head attention read as sending map, receiver reading, decoder and routing row
- Evidence: Line 223: "provides a structural comparison with multi-head attention"; "Such an architecture is not automatically the Bayesian message model above." Neither chapter states that one system computes every agent's quantities; I found no other single-system passage in the two files.
- Who evaluates: The text does not say; the remark compares structures and assigns no computation.
- Falsifies: A passage in these chapters stating that all agents' frames, beliefs and dictionaries are computed by one system.

#### lnk-14. Codes, messages and single-message reception are built from the receiver's own data

- Location: `MAgent_Theory_2.0/chapters/17_communication_links.tex:24`
- Class E, note
- Quantity: h = T_j^c y_j + eps; q-hat(dy) = integral p(dy|h) (T\_# q)(dh); gain O = Sigma_p A^T (A Sigma_p A^T + R)^{-1}
- Evidence: Line 24: "The message space carries no frame of its own: its coordinates are public conventions"; the sender forms T_j^c = T-bar_j^c U_j^{-1} with its own frame. Line 30: "Public messages therefore do not depend on the sender's frame". Lines 59-62: the reconstruction keeps the message law and fills the rest with the receiver's conditional. Lines 89 and 101: the gain is "fixed by the receiver's own uncertainty Sigma_p and by its model A of the sender's code". Line 47: theta_ji "is an independent datum, learned by a different agent".
- Who evaluates: The sender encodes with its own frame; the receiver decodes with its own prior and its own model of the code.
- Falsifies: A reception step that reads the sender's frame or content other than through the message.

#### lnk-15. Identification runs on received messages, co-observed referents and a declared known code

- Location: `MAgent_Theory_2.0/chapters/17_communication_links.tex:141`
- Class E, note
- Quantity: h | y-bar ~ N(T-bar theta-bar^{-1} y-bar, R); Stab_G(T-bar); reading S = T-bar theta-bar^{-1}; routed information sum_c beta^{(c)}\_ij F_c^{(j)}
- Evidence: Lines 133-135: referent with law rho "in i's reference coordinates" and the receiver's message model. Line 141: "Assume that the receiver knows the sender's reference code T-bar, for example through a declared shared language in reference coordinates". Line 157: with an unknown code only A-hat is identified. Lines 189-193: routed modalities with observed or latent labels. Line 208: a receiver reading a code through S "holds exactly the identifiable part of a dictionary". Lines 303-305: the filter uses h_t, y-bar_t and T-bar_e^c.
- Who evaluates: The receiver. The Fisher form at line 147 and the limits are describer-level analysis of that experiment.
- Falsifies: An identification step that uses the sender's content or frame directly.

#### lnk-16. Source rows are posteriors over senders computed from received messages

- Location: `MAgent_Theory_2.0/chapters/17_communication_links.tex:278`
- Class E, note
- Quantity: Gibbs row pi_j exp(-n C\_{j,n})/Z_n with C\_{j,n} = -(1/n) sum_t log nu_j(h_t)
- Evidence: Line 268: each candidate source is "modeled as emitting independent messages with density nu_j on the message space". Line 278: "The finite-sample posterior is exactly the Gibbs row"; "The costs are divergences between message laws." The true message density nu enters only the almost-sure limit at line 270, which is a statement about the experiment.
- Who evaluates: The receiver, from its own models nu_j and the messages it received.
- Falsifies: A row weight in this section that depends on a content-law divergence such as KL(q || q_j) as something the receiver computes.

#### lnk-17. Common reference presentation and identity anchor are declared hypotheses

- Location: `MAgent_Theory_2.0/chapters/17_communication_links.tex:314`
- Class E, note
- Quantity: Reference coordinates common to all agents; prior anchor at theta-bar = I; Pi_0 and W_gamma as reference-presentation data
- Evidence: Line 7: "The constructions take place at one context of the principal bundle P". Line 283: "Centering the prior at identity is a declared alignment hypothesis: before observing messages, the receiver expects the sender's dictionary to take its bundle-identification value theta-bar=I." Line 314: "reference coordinates are common to all agents, not owned by the receiver". Line 312: "In this model Sigma is fixed data at the operating point." Chapter 18 line 20: "declared reference-coordinate data". Under this declared scope the receiver works with its own frame and theta-bar_ij; the frame relation U_i U_j^{-1} is encoded as the anchor value and is never evaluated by an agent.
- Who evaluates: The receiver holds the anchor; the common reference is declared, with a pointer to ch:foundations, which is outside this lane.
- Falsifies: A passage showing the common reference is not available to each agent, in which case the identity anchor would amount to knowledge of U_i U_j^{-1}.

#### lnk-18. Per-agent record model is receiver-only by construction

- Location: `MAgent_Theory_2.0/chapters/18_link_dynamics.tex:52`
- Class E, note
- Quantity: o_e = T_e(y_i - y_j - kappa_i omega_e) + eps_e; record term || o_e - T_e(y_i - mu_j - kappa_i omega_e) ||^2 in E_i
- Evidence: Line 12: the record compares the receiver's prediction of the message with the sender's message. Line 52: "Agent i's model contains no record in which i is the sender; such records belong to the receivers' models." Line 141 (iv): edge e: j -> i contributes to H\_{y_i y_j} and nothing to H\_{y_j y_i}. Line 147: "Ownership removes sender-role content derivatives from the per-agent update." Line 177: receiver-only content equations in the grounded limit. The self term, the grounded term and the anchor are the receiver's own (line 20).
- Who evaluates: Receiver i, from its own content, its own dictionary, the received coded mean and, in the law-level model, the coded covariance.
- Falsifies: A record term in E_i on an edge where i is the sender.

#### lnk-19. Reciprocal edge cost and Gibbs rows are divergences between message laws

- Location: `MAgent_Theory_2.0/chapters/18_link_dynamics.tex:268`
- Class E, note
- Quantity: Delta_e = KL(A_e(omega_e) || B_e) with A_e = q_i K_e^rec(omega_e), B_e = q_j K_e^src; E_r[KL(m_e^rec(omega_e) || m_e^src)]; beta_e^\* = pi_e exp(-C_e/T_i)/Z_i
- Evidence: Line 221: both laws live "on a common message space". Line 225: Delta_e. Line 236: Gibbs row. Lines 262-263: m_e^rec = N(T_e(mu_i - kappa_i omega_e), S\_{i,e}) and m_e^src = N(T_e mu_j, S\_{j,e}). Line 273: "the costs are divergences between message laws, rather than comparisons between independent content samples." Line 338: C_e in closed form. This is the coded-marginal divergence with noise, and neither file uses a full-belief transported divergence as an objective. The scalar examples at lines 150 and 466 take K = 1 and T_e = 1, an injective code, so there the coded marginal is the whole belief plus noise.
- Who evaluates: The receiver can evaluate C_e and its own row from its belief, its dictionary law and the sender's message law.
- Falsifies: An edge cost in the file that depends on q_j other than through q_j K_e^src.

### Hidden requirements

- Law reconstruction needs the sender's whole message law, not one realized message: "This is a law-reconstruction protocol when the message law is supplied" (MAgent_Theory_2.0/chapters/17_communication_links.tex:17).
- Gaussian reconstruction needs the sender's coded covariance A Sigma_q A^T as well as the coded mean (MAgent_Theory_2.0/chapters/17_communication_links.tex:113, also :84 and :117).
- The message space H_c and the noise covariance R_c of each modality are public conventions known to the receiver (MAgent_Theory_2.0/chapters/17_communication_links.tex:24).
- Identification of the dictionary assumes the receiver knows the sender's reference code, for example through a declared shared language; without it only the effective code is identified (MAgent_Theory_2.0/chapters/17_communication_links.tex:141, also :30 and :157).
- A shared language is a species-level hypothesis that codes are related by one group element in reference coordinates, and whether learned codes satisfy it is open (MAgent_Theory_2.0/chapters/17_communication_links.tex:30, also :513).
- Chapter 18 uses the sender's code inside the receiver's prediction and in N_e without restating the known-code hypothesis (MAgent_Theory_2.0/chapters/18_link_dynamics.tex:15, also :12).
- Reference coordinates are common to all agents, and the anchor and loop forms are declared in that common presentation (MAgent_Theory_2.0/chapters/17_communication_links.tex:314, also :7).
- The receiver's prior is centered on the bundle-identification value theta-bar = I, a declared alignment hypothesis that presupposes the common reference (MAgent_Theory_2.0/chapters/17_communication_links.tex:283, also :50).
- Grounded learning needs a referent the receiver observes in its own reference coordinates for each message, with positive-definite second moment, and observed source labels (MAgent_Theory_2.0/chapters/17_communication_links.tex:133, also :191 and :295).
- Pooling modalities needs one dictionary shared by all modalities and the receiver's knowledge of every modality's code (MAgent_Theory_2.0/chapters/17_communication_links.tex:174, also :184).
- A loop prior needs the current means of dictionaries held by other agents along the receiver's loops, which the text says requires agents to communicate how they read each other (MAgent_Theory_2.0/chapters/17_communication_links.tex:504).
- The law-level per-agent loop factor needs the covariances V_f as well as the means a_f of dictionaries the agent does not own (MAgent_Theory_2.0/chapters/18_link_dynamics.tex:47, also :36 and :40).
- The exchange of dictionary information and the echo-free removal of prior contributions from transmitted laws are stated as an open problem (MAgent_Theory_2.0/chapters/18_link_dynamics.tex:665, also :205).
- The GL(K)-covariant loop form is dressed by the belief covariance of one declared base agent, which every other receiver on the loop would need in full (MAgent_Theory_2.0/chapters/17_communication_links.tex:312, also :252 and :290).
- The law-level per-agent model needs the sender's coded covariance T_e Sigma_j T_e^T; the plug-in model needs only the coded mean (MAgent_Theory_2.0/chapters/18_link_dynamics.tex:46, also :50).
- Reciprocal edge costs and Gibbs rows need the sender's message covariance S\_{j,e} = T_e Sigma_j T_e^T + R_e (MAgent_Theory_2.0/chapters/18_link_dynamics.tex:338, also :260).
- The source-role force of the reciprocal potential needs the receiver's row weight beta_e and the mean and covariance of the receiver's dictionary-averaged predicted message law (MAgent_Theory_2.0/chapters/18_link_dynamics.tex:353, also :357).
- The sender-role force of the global flow needs the record registered at the receiver and the receiver's coded prediction (MAgent_Theory_2.0/chapters/18_link_dynamics.tex:119).
- The per-agent mean flow holds every peer covariance at the joint fixed point of the map Phi, which presupposes repeated exchange of coded content covariances and of dictionary covariances (MAgent_Theory_2.0/chapters/18_link_dynamics.tex:136, also :128).

## Lane att: Attention manuscripts

Investigator type `audit-transformer-ml`. No class A conflict was found in the attention lane: nowhere do the five files have a single agent compute with another agent's frame. The two agent-framed papers (GL(K)\_attention_v2.tex and minimal_agent_model.tex) declare a shared reference space and a layer-wide shared protocol, and every agent-side computation factors as a sender-side read through U_j^{-1}, a coded emission, and a receiver-side write through U_i. Five class C items remain, all minor. Two are wording that equates the receiver's routing decision with a full-belief divergence through a two-frame link (GL(K) abstract and introduction; the minimal-agent full-rank reading and KL-routed variant), where the coded counterpart sits in the same file. Two are covariance updates that read the sender's content-coded covariance T_h C_j T_h'^T, which the text never lists among the emitted quantities: the GL(K) moment-matched covariance and the per-receiver latent-link energy in edge_latent_links.tex, the latter also reading sender factors B_j and loops through edges the receiver does not own. The fifth is the minimal-agent conditioning itself, which needs the coded sender covariance and a cross-head condition on the sender's private covariance while the emission is described only as an "observable". dynamic_links.tex and the amortized part of edge_latent_links.tex are single-system (class D) and never use agent language, but neither states that scope; cue_result_memory.tex is privacy-respecting given its declared shared bank. With tiled heads or full-rank maps the emitted code is an invertible image of the sender's whole reference belief, so what stays private in those cases is the frame alone.

### Coverage

- Read in full: Attention/minimal_agent_model.tex; Attention/dynamic_links.tex; Attention/edge_latent_links.tex; Attention/cue_result_memory.tex
- Searched only: Attention/GL(K)\_attention_v2.tex: searched for agent, sender, receiver, private, shared reference, communicate, message, forward pass, local inference, backprop, free energy, holonomy, global; then read lines 50-178, 340-401, 448-1001, 1056-1190, 1250-1254, 1290-1354, 1436-1440, 1474-1484 and 1590-1621. Not read: 1-49 (preamble), 179-339 and 402-447 (TikZ figure code), 1002-1055 (dual-coordinate and dot-product reductions), 1191-1249 and 1255-1289 (experimental results), 1355-1435, 1441-1473, 1485-1589 (appendix proofs), 1622-1846 (experimental record and placeholder tables). Search hits in the unread ranges were for notation-table rows and run-record text only.
- Not covered: GL(K)\_supplementary_v2.tex, which holds the receiver-inference section, the latent-link model, the tied-record remark and the comparison-lift section that the assigned files cite; statements about those are taken only from what the assigned files say of them.; The uncommitted folder manuscripts/Attention/adaptive_vfe_interfaces and the two 2026-10-21 foundation notes, which are outside this lane.; The vfe3 code and the check scripts; no script was run and no code was read, so every class D attribution rests on what the manuscripts say about the implementation.; The Research vault wiki was not consulted; findings rest on the assigned files alone.

### Findings

#### att-1. Routing decision stated as a full-belief divergence through a two-frame comparison link

- Location: `Attention/GL(K)_attention_v2.tex:72`
- Class C, minor
- Quantity: D_KL(q_i || (Theta^cmp_ij)\_\* q_j) with Theta^cmp_ij = U_i S_Q^{-1} S_K U_j^{-1}; special case D_KL(q_i || (Omega_ij)\_\* q_j) with Omega_ij = U_i U_j^{-1}
- Evidence: Line 72-77: 'The routing weights beta_ij, the decision of whom to hear, are a Gibbs distribution over relative entropies between the receiver's query law and the senders' key laws; for square invertible query and key maps the comparison is D_KL(q_i||(Theta^cmp_ij)\_\*q_j) ... the divergence of the receiver's belief from the sender's, carried into the receiver's coordinates by a group-valued comparison link that is the flat identification Omega_ij=U_iU_j^{-1} when S_Q=S_K'. Same statement at 53 (abstract: 'routing is the divergence D_KL(q_i||(Theta^cmp_ij)\_\*q_j) of the receiver's belief from the sender's belief carried into its coordinates'), 503-508 (Proposition comparison_link, stated as an identity), 518 ('the routing cost is the divergence of the receiver's belief from the sender's belief transported by it'), 1089 ('Complete-state alignment, S_Q=S_K=I_K, scores sender j by D_KL(q_i||(Omega_ij)\_\*q_j)'). Settling statements elsewhere: 401 ('query and key are what it is computed from'), 518 ('the evaluated predictor uses only D_ij'), 669 (table: comparison link 'not formed (r_h\<K)'), 1089 ('the evaluated model imposes neither').
- Who evaluates: At lines 53, 72-77, 518 and 1089 the text does not say who evaluates the two-frame form; it calls the weight the receiver's 'decision of whom to hear'. Line 401 says the weight is computed from the receiver's query and the sender's emitted key law, and line 669 says the comparison link is not formed in the evaluated model.
- Replacement: The comparison-space divergence D_ij = D_KL((S_Q)\_\* q~\_i || (S_K)\_\* q~\_j) between the receiver's own query law and the received key law. The file already has it as the definition at 478-480 and as the left side of Eq. comparison_link at 502; the sender-emits-key-law statement is at 401. At r_h = K (or S_K = I) the emitted key law is an invertible code of the sender's whole reference belief, so the full belief is then received content and only the frame U_j stays private.
- Falsifies: A sentence at 53, 72-77 or 518 stating that the two-frame form is an equivalent rewriting used only for analysis, with the receiver evaluating the comparison-space form; that would make this class B. I regard this as a B/C boundary case: the body settles the computation, the abstract and introduction wording does not.

#### att-2. Moment-matched covariance reads the sender's content-coded covariance, which the text does not list as emitted

- Location: `Attention/GL(K)_attention_v2.tex:1107`
- Class C, minor
- Quantity: C_i^att containing sum_j sum\_{h,h'} c_ij^{hh'} M_h C_j M_h'^T with M_h = O~\_h T_h, i.e. the sender blocks T_h C_j T_h'^T including cross-head blocks
- Evidence: Line 1104-1113: 'With independent source states k_j ~ N(mu_j,Sigma_j), the self edge included, its moment-matched covariance in reference coordinates is C_i^att = Q~\_i + c_res[...] + sum_j sum\_{h,h'} c_ij^{hh'} M_h C_j M\_{h'}^T + ...'. Used at 587 ('under moment matching, attention returns the covariance of the predictive kernel'), 946 (Corollary normal_form), 1164 (Algorithm step: 'Set Sigma_i^(l+1) to the moment-matched covariance'). The emitted content is described as a mean only: 72 ('content T xi_j'), 396 ('sending map T_h, emits T_h xi_j'), 401 ('its content T_h xi_j, what it says'), while the key is described as a law at 401 ('its key (S\_{K,h})\_\* q~\_j').
- Who evaluates: The text says 'attention returns' it (587) and the algorithm of the evaluated network sets it (1164); no agent is named. In the agent reading the receiver's next covariance depends on a sender quantity that the communication table at 396-397 does not list as transmitted.
- Replacement: Have the sender post the content law (T_h)\_\* q~\_j, or the stacked (T)\_\* q~\_j when cross-head blocks are needed, in place of the mean T_h xi_j. The assigned files already contain the pieces: minimal_agent_model.tex:141-146 uses the coded sender covariance V_K,j = T_h C_j T_h^T inside the receiver's update, minimal_agent_model.tex:162-166 states the cross-head condition T_h C_j T_g^T = 0 under which cross blocks vanish, and edge_latent_links.tex:229 isolates the head-pair source blocks s_j^{hh'} = T_h C_j T\_{h'}^T. With tiled heads and invertible stacked T (728) the posted law is an invertible code of the full reference covariance C_j.
- Falsifies: A statement in the file that the sender's content emission is the pushforward law including its covariance, or that the covariance update is performed by the layer as one system and not by the receiving agent.

#### att-3. Full-rank reading and KL-routed variant written with a two-frame link and the sender's full belief

- Location: `Attention/minimal_agent_model.tex:220`
- Class C, minor
- Quantity: Theta^cmp_ij = U_i (S_Q^{-1} T) U_j^{-1}; D_KL(q_i || (Theta^cmp_ij)\_\* q_j); message sum_j beta_ij Theta^cmp_ij mu_j; induced link M^cmp_ij = U_i R\_{Q,i} T U_j^{-1}
- Evidence: Line 220: 'The comparison link Theta^cmp_ij fixes the source weight through the overlap of the receiver's belief with the transported sender belief ... Replacing the expected-likelihood weights by the Gibbs weights beta_ij ∝ pi_ij exp(-KL(q_i||(Theta^cmp_ij)\_\*q_j)/tau) ... and keeping the message sum_j beta_ij Theta^cmp_ij mu_j defines a KL-routed variant of the model. That variant is declared, not derived'. Further uses: 110-115 (Lemma link (b), identity), 124 ('the comparison of the receiver's full belief with the sender's full belief carried into the receiver's frame'), 179-183 (local form with M^cmp_ij), 184-190 (item (d), limit mu_i^+ = sum_j w^0_ij Theta^cmp_ij mu_j), 215, 253-257 (tiled form). The premise at 47 and 55 is that each agent 'holds a full Gaussian belief privately but can transmit only a partial representation of it'.
- Who evaluates: For the KL-routed variant the text does not say; it is 'declared'. For the exact model the receiver conditions on its own record (138), and the two-frame forms are introduced with 'In local coordinates' (178) or as identities (Lemma link (b)).
- Replacement: The comparison-space cost D^(h)\_ij = D_KL(q^(h)\_{Q,i} || p^(h)\_{K,j}) of Eq. gibbs at line 93 and the first expression of Eq. link_identity at line 112, evaluated from the received utterance law (T xi_j, T C_j T^T) and the receiver's own query law. Both are in this file. At full rank with invertible T the utterance law is an invertible code of the sender's whole reference belief, so the premise of a privately held full belief reduces to privacy of the frame U_j.
- Falsifies: A sentence stating that the KL-routed variant is evaluated in the comparison space from the transmitted utterance law, or that the full-rank case is one in which the sender transmits its complete reference belief by declaration.

#### att-4. Per-receiver latent-link objective reads senders' full reference moments, sender factors, and loops through edges the receiver does not own

- Location: `Attention/edge_latent_links.tex:294`
- Class C, minor
- Quantity: F_i(A_i) = E_i(A_i) + ||A_i - A_i^0||\_F^2/(2 sigma_L^2) + lambda_W W_i(A_i), with E_i = tr V_i(A_i)/(2 c_i); V_i contains G_ij Pi_h C_j Pi_h'^T G_ij^T and n_ij^h = G_ij Pi_h xi_j; G_ij = F exp(A_i B_j^T); loop W_ijk^l = (E_kk^l)^{-1} e^{-L_l} (E_ik^{l+1})^{-1} E_ij^{l+1} e^{L_l} E_jk^l
- Evidence: Line 294-297: 'The per-receiver energy is F_i(A_i)=E_i(A_i)+(1/2 sigma_L^2)||A_i-A_i^0||\_F^2+lambda_W W_i(A_i)'. Line 258: 'Suppose each receiver's energy F_i depends only on its own latent factor A_i and on quantities of tokens j\<=i'. Line 264: 'each receiver's inference problem is independent of the others'. Line 268: recognition law of the inputs held at q(k_j)=N(xi_j,C_j). Lines 212-220: covariance with G_ij Pi_h C_j Pi_h'^T G_ij^T. Line 105: Phi_ij = phi_1(B_j^T A_i). Lines 344, 355, 364: loop energy over k\<j\<=i, 'the layer-l factors were inferred at layer l and are held fixed'; these include E_jk^l = exp(A_j^l B_k^{lT}) and E_kk^l, edges into tokens j and k. Line 304: gradient is the pulled-back current times B_j. Line 433: 'infer_latent_receivers runs the damped iteration with torch.autograd.grad' and 'The previous layer's link state for the loop energy is threaded through the stack'.
- Who evaluates: The text makes 'each receiver' the subject of the inference and gives it its own prior and energy, but attributes the evaluation to one code path (433). The note never uses the word agent and declares no privacy scope; it adopts the companion manuscript's notation (64), in which tokens are agents. I am unsure between C and D and file C because the objective is explicitly per receiver.
- Replacement: What is already receiver-local: the latent factor A_i, its prior N(A_i^0, sigma_L^2 I) (270) and the causal restriction to tokens j\<=i (258). The sender-side inputs the energy needs are isolated by the note's own factored evaluation: v_j^h = T_h xi_j and p_j^h = (B~\_j)\_h^T v_j^h (176-180), the head-pair blocks s_j^{hh'} = T_h C_j T\_{h'}^T (229), and the sender factor B_j for Phi_ij (105). An agent-computable version would have each sender post exactly these coded quantities. The loop term has no receiver-local counterpart in the file: at lambda_W = 0 'nothing is threaded between layers' (371), which is the privacy-respecting setting already present.
- Falsifies: A statement that the receiver-factor inference is a computation of the layer as one system with all token states available, or a statement listing B_j, the coded covariance blocks and the previous-layer factors as transmitted quantities.

#### att-5. Receiver's exact conditioning needs the sender's coded covariance and a cross-head property of it

- Location: `Attention/minimal_agent_model.tex:144`
- Class C, minor
- Quantity: V^{rec,(h)}\_ij = V^(h)\_{Q,i} + V^(h)\_{K,j} + N_h with V^(h)\_{K,j} = T_h C_j T_h^T; gain G^(h)\_ij = C_i S\_{Q,h}^T (V^{rec,(h)}\_ij)^{-1}; sender condition T_h C_j T_g^T = 0
- Evidence: Lines 141-146: 'the comparison covariances are V\_{Q,i}=S\_{Q,h}C_iS\_{Q,h}^T and V\_{K,j}=T_hC_jT_h^T. Define the record covariance, the gain, and the expected-likelihood weights by V^rec_ij=V\_{Q,i}+V\_{K,j}+N_h, G_ij=C_iS\_{Q,h}^T(V^rec_ij)^{-1}, w_ij ∝ pi_ij N(T_h xi_j; S\_{Q,h} xi_i, V^rec_ij)'. Lines 162-166 and 195: the several-head factorization needs 'T_hC_jT_g^T=0' for every sender, 'the utterances of different heads from one sender must be uncorrelated under that sender's belief'. Line 133: 'Each source j has a state X_j ~ q~\_j = N(xi_j,C_j)'. The emission is described as 'one linear observable of its belief per head, the utterance' (47) without saying whether its covariance is posted. Line 274: the implementation lets 'each head hear its own independent snapshot of every source, which coincides with Definition model when T_hC_jT_g^T=0'.
- Who evaluates: The receiver: 'each receiver conditions its belief exactly on a noisy comparison record' (47), 'Each receiver conditions on its own records only' (138). Whether the receiver obtains V_K,j from the sender is not stated.
- Replacement: State that the utterance is the pushforward law (T_h)\_\* q~\_j, mean and covariance, which is coded content with a posted coded covariance. The file already writes the key observable as a law at 81-87 (p\_{K,j} = (S\_{K,h})\_\* q~\_j); the source-independent case V_K,j = V_K (156) removes the per-sender covariance altogether; point-mass senders satisfy the cross-head condition automatically (195).
- Falsifies: A sentence saying the sender transmits the law of its utterance (mean and covariance), or one saying the receiver uses an assumed common V_K in place of each sender's own.

#### att-6. Two-frame links, holonomies, loop products and gauge covariance are used as descriptions and diagnostics

- Location: `Attention/GL(K)_attention_v2.tex:824`
- Class B, note
- Quantity: H_ijk = Theta_ik^{-1} Theta_ij Theta_jk; routed loop product H_gamma = M\_{i0 i1} ... M\_{i(n-1) i0}; Omega_ij Omega_jk = Omega_ik; passive action g = (g_i) in G^N; joint-state layer I + L_beta on R^{NK}
- Evidence: Lines 820-849 (triangle holonomy, flatness, 'H_ijk=U_k e^L U_k^{-1} on every triangle'), 648-650 (flat identification is pure gauge), 668 (table: flat identification implemented as 'the frame field'), 806-810 (joint state), 878-886 (covariance and loop products), 890 ('a covariance under changes of each agent's coordinates'), 1254 ('holonomy and inverse-edge diagnostics must be computed analytically in log space'), 1307 ('trained-link spectra and holonomies should be recorded'), 1335 (gauge group of the token construction is G^N), 1346 ('Omega_ij=U_iU_j^{-1} is the transition function between the sections u_j and u_i').
- Who evaluates: An external describer: these appear in propositions, in a table of edge objects, and as post-hoc diagnostics on a trained checkpoint. No update rule or weight of an agent uses a holonomy.
- Falsifies: A place where a holonomy or a loop product enters a routing weight, an update, or a loss that a token agent evaluates. None was found in the lines read; lines 1355-1435, 1441-1473, 1485-1589 and 1622-1846 were not read.

#### att-7. Compatibility record, source-selection joint and predictive kernel are declared modeling devices

- Location: `Attention/GL(K)_attention_v2.tex:1098`
- Class B, note
- Quantity: P(o_i^(h)=1 | J_i^(h)=j) = exp(-D_ij^(h)/tau_h); P_i(y,J=j) = pi_ij p\_{K,j}(y); kernel k_i' | k, J_i ~ N(c_res k_i + sum_h M^(h)\_{i J} k_J, Q_i)
- Evidence: Line 1098 (record), 1069-1072 ('The states enter as data fixed by the prefix before routing'), 1101 (kernel), 1117 ('Records attached to different receivers and heads are conditionally independent children of the states and labels, so the joint is normalized'), 1119 ('The record is a declared modeling event ... not an observed datum').
- Who evaluates: The theorist declares the joint; the per-receiver label posterior it yields is built from the comparison-space costs D_ij.
- Falsifies: A statement that an agent observes the record or samples the kernel using another agent's full state.

#### att-8. Population regression links and the induced link action are analyses over a population or an integrated-out model

- Location: `Attention/dynamic_links.tex:236`
- Class B, note
- Quantity: Population regression link C_ab C_bb^{-1} with cross-covariance C_ab between vertices; S_ind(X) = (1/2) log det J(X); partial cross-covariance C\_{ac|b}
- Evidence: Line 236: 'Averaged over a population of contexts, the same normal equation gives ... the population regression link C_ab C_bb^{-1}'. Lines 292 and 310-314 (directed matter induces no action; induced action of undirected matter). Lines 379-404, with 404: 'The regression links need cross-covariances between distinct vertices, which vanish under a single mean-field recognition law and appear only in the population law'.
- Who evaluates: An external analyst averaging over contexts or integrating out states; the text presents these as propositions about the model.
- Falsifies: A rule in which a token computes a cross-covariance with another token's state during a forward pass.

#### att-9. Passive covariance and local-coordinate forms of the minimal model are rewritings of a reference-coordinate computation

- Location: `Attention/minimal_agent_model.tex:179`
- Class B, note
- Quantity: mu_i^+ = U_i (I - Pi_i) U_i^{-1} mu_i + sum_j w_ij M^cmp_ij mu_j; passive action (U_i, mu_i, Sigma_i) -> (g_i U_i, g_i mu_i, g_i Sigma_i g_i^T)
- Evidence: Lines 178-183 ('In local coordinates ...'), 70 ('Every quantity computed from reference moments and from maps that act on reference coordinates is therefore invariant'), 129 ('work in reference coordinates'), 329 (derivation of the local form by substituting xi_k = U_k^{-1} mu_k).
- Who evaluates: The theorist rewrites the receiver's reference-coordinate update; the model itself is stated and solved in reference coordinates.
- Falsifies: A statement that the receiver forms M^cmp_ij from U_j.

#### att-10. Evaluated language model is one network that builds every frame and trains by backpropagation of a global loss

- Location: `Attention/GL(K)_attention_v2.tex:1153`
- Class D, note
- Quantity: U_i = exp(phi\_{x_i}) exp(Y_i) for all i; xi_i = U_i^{-1} mu_i, C_i for all i; D_ij, beta_ij, m_i; mean next-token cross-entropy over all positions
- Evidence: Algorithm lines 1153-1170: 'realize the frame U_i=exp(phi\_{x_i})exp(Y_i) once for all layers'; 'Form xi_i=U_i^{-1}mu_i and C_i=U_i^{-1}Sigma_i U_i^{-T}'; 'Backpropagate the mean next-token cross-entropy to every trainable parameter'. Line 1302: 'The evaluated model is a hybrid ... every parameter is trained by backpropagation of the next-token cross-entropy' and 'whether these agents can learn their priors, frames, and interface maps by local inference is untested'. Lines 377-384: priors and frame coefficients come from a per-token-type bank and per-position generators, so a frame is a function of token type and position read from shared tables. Line 91: the prototype 'claims no free energy for the whole stack'.
- Who evaluates: The network. The text states this for the evaluated model (1139, 1302) and states that agent-level learning is untested; it does not state in so many words that privacy between token agents is therefore not at issue.
- Falsifies: A passage attributing the algorithm's steps to individual agents acting on privately held frames, or a learning rule in which an agent updates its frame from a quantity other than the global loss gradient.

#### att-11. Latent-link free energy is one global functional with one recognition density over all tokens, layers and links

- Location: `Attention/dynamic_links.tex:180`
- Class D, note
- Quantity: F[q] = sum_i E_q[-log p(o_i | U_i zeta_i^L)] + sum_i KL(q(zeta_i^0)||p) + sum\_{l,i}[KL(q(zeta_i^{l+1})||N(m-bar_i^l,Q-bar)) + (1/2)tr(Q-bar^{-1}V_i^l)] + sum\_{l,i,h} KL(beta||pi) + E_q[S_X] - H[q(X)] + log Z_X
- Evidence: Lines 180-188 (boxed functional). Line 112: joint density p(o,zeta,J,X) over all tokens. Line 143: recognition 'q(zeta,J,X)=prod N(zeta_i^l;xi_i^l,C_i^l) prod beta_i^{l,h} q(X)'. Line 48: 'Recognition is mean field over token states, routing labels and links'. Line 53: 'Each token carries a frame U_i, built once per forward pass and shared across layers as in the current architecture'. Line 131: 'the frames ... enter the joint only through the decoder'. The word agent occurs only at line 81 ('the multi-agent code').
- Who evaluates: The model as one system within a forward pass (260: 'Within a forward pass the links relax toward the stationary point of F'). The text does not use agent language and does not state a privacy scope.
- Falsifies: A passage in this note identifying tokens with privacy-bound agents that each minimize their own share of F.

#### att-12. Link field equation, Fisher preconditioner and loop energy read sender moments and non-incident edges

- Location: `Attention/dynamic_links.tex:208`
- Class D, note
- Quantity: J_ij^l = beta_ij^l A[(xi_i^{l+1} - G_ij^l xi_j^l) xi_j^{lT} - G_ij^l C_j^l]; I_ij^l[E,E'] = beta_ij^l tr(A L(X,E) S_j^l L(X,E')^T) with S_j^l = C_j^l + xi_j^l xi_j^{lT}; W_ijk^l = (G_ik^{l+1} G_kk^l)^{-1} G_ij^{l+1} G_jk^l; local link Theta_ij^l = U_i G_ij^l U_j^{-1}
- Evidence: Lines 202-209 (field equation and one-head current). Line 262 (Fisher form). Lines 62 and 124-127 (loops and loop weights w_ijk^l = pi-bar_ij^{l+1} pi-bar_jk^l). Line 57 (local link as a function of both frames). Lines 242-246 (linearized equation coupling edges through delta^T w delta). Line 260: 'the flow M-dot = -I(M)^{-1} grad_M F'. Line 337: a first implementation would 'infer per-context deviations M - X-bar with a few Gauss-Newton steps' or by 'amortization, in which a network predicts M - X-bar from the states'. The loop for receiver i contains G_jk^l and G_kk^l, edges into tokens j and k.
- Who evaluates: The system during a forward pass; the owner of an edge variable X_ij^l is not stated (the generators 'live on the edges', line 40). Under a token-as-agent reading a link owner would need the sender's full reference mean and covariance, the receiver's next-layer mean, and links on edges it is not incident to.
- Replacement: Not needed for class D. For reference, the restriction in edge_latent_links.tex makes the latent object a receiver factor A_i with a per-receiver energy (edge_latent_links.tex:258-264, 294-297) and compares the two models in its Table at 385-404.
- Falsifies: A statement in this note assigning each X_ij^l to one token agent that updates it from its own data, which would move this to class A or C.

#### att-13. Amortized edge link field is computed by the layer from both endpoints' reference states

- Location: `Attention/edge_latent_links.tex:85`
- Class D, note
- Quantity: G_ij = g_i F E_ij, E_ij = I + A_i Phi_ij B_j^T, Phi_ij = phi_1(B_j^T A_i); Theta_ij = U_i G_ij U_j^{-1}; A_i = vec^{-1}(W_A x^\_i), B_j = vec^{-1}(W_B x^\_j)
- Evidence: Lines 85-92 (definition), 96-107 (factors 'read from the RMS-normalized reference state ... by learned linear maps'), 110-113 (pure-gauge mode), 128 ('The receiver chooses where the edge writes and the sender chooses what the edge reads'), 178-190 (message via p_j^h, c_ij, y_i = sum_j Phi_ij c_ij), 433 ('edge_factors and edge_coefficients build A_i, B_j, g_i, and Phi_ij'). Line 53: the note 'records how they are implemented in the vfe3 code'.
- Who evaluates: The implementation, one code path per layer (433). The note does not use agent language; line 128 is the only sentence that assigns choices to receiver and sender. Phi_ij needs A_i and the K x r sender factor B_j together.
- Falsifies: A passage stating that the receiver token alone forms Phi_ij without being sent B_j, or that tokens here are privacy-bound agents.

#### att-14. Minimal agent model is implemented as a readout of one network; no learning rule is specified

- Location: `Attention/minimal_agent_model.tex:274`
- Class D, note
- Quantity: Reference moments (xi_i, C_i) of all tokens; shared maps S\_{Q,h}, T_h; learned isotropic channel noise n_h
- Evidence: Line 274: 'The VFE_3.0 implementation (vfe3/model/minimal_agent.py ...) makes the choices this note leaves open. The moments xi_i and C_i are the reference moments of the layer input ... The priors pi_ij are the attention log-prior, causal mask included'. Line 271: 'The components a full architecture would need beyond it, such as ... a decoder, and a learning rule, are not specified here'. Line 47: 'implemented as a selectable attention readout of the VFE_3.0 code'.
- Who evaluates: The network in the implementation. The text states that the implementation is a code path and that no learning rule for the shared maps is given.
- Falsifies: A learning rule in the note under which an agent updates S_Q or T from another agent's private quantities.

#### att-15. Memory bank is trained by backpropagation of the next-token loss

- Location: `Attention/cue_result_memory.tex:371`
- Class D, note
- Quantity: Bank parameters nu_a, lambda_a, omega_a, q_a, pi_a, F_a (and transition T) trained on the global next-token loss
- Evidence: Line 371: 'All parameters are trained by backpropagation of the next-token loss through the exact posterior; no expectation-maximization term fits the bank to the cues'. Line 414: 'The parameters are learned by backpropagation of the task loss, not by local inference'.
- Who evaluates: The network; the text says so explicitly and says local inference is not used.
- Falsifies: A statement that each token agent learns the bank from its own records.

#### att-16. Routing and mean content are built from the receiver's own query law, the emitted key law and emitted content

- Location: `Attention/GL(K)_attention_v2.tex:401`
- Class E, note
- Quantity: D_ij^(h) = D_KL(q\_{Q,i}^(h) || p\_{K,j}^(h)); beta_ij^(h) = softmax_j(-D_ij^(h)/tau_h + log pi_ij^(h)); v_j^(h) = T_h xi_j; m_i = U_i sum_h O~\_h z_i^(h); head map factored as (U_i O~\_h)(T_h U_j^{-1})
- Evidence: Line 401: 'The sender emits two partial representations of its belief: its key (S\_{K,h})\_\* q~\_j ... and its content T_h xi_j ... The receiver forms a query ... which is never transmitted ... The interface maps are a protocol shared by all agents of a layer; the private frames translate to the reference space, the sender reading through U_j^{-1} and the receiver writing through U_i'. Also 70 ('private coordinates' and 'shared reference space'), 396-397 (sender/receiver table), 478-480 (cost in the comparison space), 484-494 (cospan and the content composition E_j -> Z_h -> E_i), 526-548 (per-receiver objective and content), 554-556, 871 ('depends on the states only through the reference moments'), 1302 ('its frames private coordinates, its interface maps a protocol shared within a layer').
- Who evaluates: Sender j applies its own U_j^{-1} and the shared maps and emits; receiver i applies the shared maps and its own U_i. No agent applies the other's frame.
- Falsifies: A step in which the receiver applies U_j^{-1} itself, or in which the query is transmitted to the sender.

#### att-17. Receiver conditions only on its own records, built from its query observable and the received utterance

- Location: `Attention/minimal_agent_model.tex:133`
- Class E, note
- Quantity: o_h = S\_{Q,h} X_i - T_h X\_{J^h} + eps_h observed at 0; w^(h)\_ij; G^(h)\_ij; mean-field label cost KL(q\_{Q,i} || N(T xi_j, V\_{K,j} + N))
- Evidence: Lines 133-138: 'Each receiver conditions on its own records only'. Line 141: 'Conditioning every receiver jointly on all records would couple the receivers through shared source states; the declaration that each receiver conditions on its own records ... keeps the round parallel across receivers'. Line 47: 'An agent that holds a full Gaussian belief privately but can transmit only a partial representation of it'. Line 206: the receiving map, residual and routing 'are derived from them and from the receiver's covariance'. Lines 227-231 (mean-field family q(X_i)q(J) per receiver). Line 215: below full rank 'the weighing happens in the comparison space'.
- Who evaluates: The receiver, from its own (xi_i, C_i), the shared query map, and the utterance law of each source.
- Falsifies: A term in the posterior of Proposition minimal that depends on xi_j or C_j other than through T_h xi_j and T_h C_j T_g^T.

#### att-18. Memory block reads only the token's own reference moments and a declared shared bank

- Location: `Attention/cue_result_memory.tex:42`
- Class E, note
- Quantity: w_a ∝ pi^\_a N(xi; nu_a, L_a + C); (xi^+, C^+) from the result mixture; carried prior pi^^{l+1}\_{ib} ∝ pi^\_b (sum_a w^l\_{ia} T_ab)^theta
- Evidence: Line 42: 'The position-wise MLP of a transformer is the one sublayer in which an agent computes privately'. Line 71: the block 'acts on each token separately'. Line 86: 'The record covariance C is side information supplied with the record' (the token's own C_i). Line 301: 'The block reads only (xi_i,C_i) ... and the component bank is shared data in reference space'. Line 304: 'The bank lives in the reference space, so it is one global object rather than a field over tokens'. Lines 338-343: the carried prior uses the token's own previous posterior w_i^l. Line 395: the senders are 'a fixed bank shared by all tokens rather than other tokens of the context, so it computes privately'.
- Who evaluates: Each token agent, from its own belief and a model shared by all tokens.
- Falsifies: A dependence of token i's block output on another token's moments or frame.

### Hidden requirements

- A reference space and reference trivialization sigma_0 common to all agents is declared, and every emission is expressed in it (Attention/GL(K)\_attention_v2.tex:70; also 160, 1344 'one a in GL(K) for all agents').
- The interface maps S_Q, S_K, T, O and the comparison and content spaces are a public code known to every agent of a layer (Attention/GL(K)\_attention_v2.tex:401; also 461 'both shared by all agents', and 1344 'Holding the interface matrices fixed while changing the reference basis would specify a different communication rule').
- The receiver needs the sender's coded key covariance S_K C_j S_K^T, since the key is a Gaussian law and the cost is a KL between laws (Attention/GL(K)\_attention_v2.tex:475).
- The moment-matched covariance needs the sender blocks T_h C_j T_h'^T including cross-head blocks, although the content emission is described as the mean T_h xi_j (Attention/GL(K)\_attention_v2.tex:1107).
- With tiled heads the stacked sending map T is invertible, so the stacked content T xi_j is an invertible code of the sender's whole reference mean and only the frame remains private (Attention/GL(K)\_attention_v2.tex:728).
- Priors and frame coefficients are shared by all occurrences of a token type and positional generators by all tokens at a position, a common-type prior and frame table (Attention/GL(K)\_attention_v2.tex:377; also 384, 1153).
- The program's prediction that priors, frames and interface maps are learned by local inference has no rule in the file, and the interface maps are a layer-wide shared protocol, so a local rule would have to keep them common across agents (Attention/GL(K)\_attention_v2.tex:66; also 1302).
- The receiver's weights and gain need each sender's coded covariance V_K,j = T_h C_j T_h^T (Attention/minimal_agent_model.tex:144).
- The several-head factorization needs T_h C_j T_g^T = 0 for every sender, a property of the sender's private covariance that the receiver must assume or be told (Attention/minimal_agent_model.tex:164; also 195, 274).
- The common-gain update form needs a source-independent coded sender covariance V_K,j = V_K (Attention/minimal_agent_model.tex:156).
- The reduction to a standard attention layer needs one covariance C_i = C for every receiver and shared V_K and N_h across sources and receivers (Attention/minimal_agent_model.tex:239).
- Agents share a single context, a reference space and per-head maps S\_{Q,h}, T_h that are single matrices common to all agents although described as belonging to sender or receiver (Attention/minimal_agent_model.tex:65; also 78).
- Link stationarity and its preconditioner need the sender's full reference second moment S_j = C_j + xi_j xi_j^T and the receiver's next-layer mean (Attention/dynamic_links.tex:208; also 262).
- The loop weights use the routing prior of an edge not incident on the receiver, pi-bar_jk^l, and the loop itself uses links G_jk^l and G_kk^l (Attention/dynamic_links.tex:125; also 62).
- Forming Phi_ij = phi_1(B_j^T A_i) needs the K x r sender factor B_j together with the receiver factor A_i, and B_j is a linear image of the sender's normalized reference state (Attention/edge_latent_links.tex:105; also 103).
- The edge covariance and the latent energy need the head-pair source blocks s_j^{hh'} = T_h C_j T\_{h'}^T of every source (Attention/edge_latent_links.tex:229).
- The loop energy of receiver i needs the layer-l factors inferred by other tokens j and k, threaded between layers (Attention/edge_latent_links.tex:364; also 433).
- The amortization maps W_A, W_B and the shared generator L = OT are common to all tokens of a layer (Attention/edge_latent_links.tex:103).
- The component bank is one global object in the shared reference space, known to every token (Attention/cue_result_memory.tex:304).
- Diagonal cue and noise covariances declare a reference chart fixed up to monomial maps, a global choice about the shared space (Attention/cue_result_memory.tex:329).

## Lane pif: PIFB2 and the two foundation notes

Investigator type `audit-philosophy-of-science`. The only places where the text has agents follow or solve something built from P-inaccessible quantities are the Gaussian "consensus specialization" passages of PIFB2 (pifb2/08, 31, 33, with the same flow written as update equations in 28 and 07). There the objective uses KL(q_i || Omega_ij q_j) with Omega_ij = U_i U_j^{-1}, the transported sender precision, and, in the canonical gradient, sender-row terms that need the attention rows, means and covariances of every agent attending to i. A receiver-side privacy-respecting counterpart already exists in the same manuscript (received message law N(L mu_j, L Sigma_j L^T + D) in 08:218-241 and 29:14-48, comparison records in 05:75-90, exact receiver update in 36c:228-245, reduced-space comparison in 04:196 and 20:49-52); I found no counterpart for the sender-row terms, the frame update, or the latent-link learning rule. The principal construction (collective F_V and its Fisher flow, 05/05b) never says who evaluates it, so it is class C; no file declares a single-system scope (class D), although 28:184 costs the update as one global computation. Claims about what agents share or agree on (04:207-214, 09:99-103, 20:46-56, 23:40-46) are stated on communicated observables in a declared common output space and do not rest on P-forbidden access. The two foundation notes are theorist-level by their own wording, state access conditions explicitly, and concede that locally implementable correlated inference is not yet constructed. The verified ledger has no PIFB entries (grep only).

### Coverage

- Read in full: PIFB2.tex; 2026-10-21-observer-free-gauge-agent-foundation.md; 2026-10-21-shared-predictions-from-gauge-model-agreement.md; pifb2/00_preamble.tex; pifb2/01_section.tex; pifb2/02_section.tex; pifb2/03_section.tex; pifb2/04_section.tex; pifb2/05_section.tex; pifb2/05b_lie_links.tex; pifb2/06_section.tex; pifb2/07_section.tex; pifb2/08_section.tex; pifb2/09_section.tex; pifb2/10_section.tex; pifb2/11_section.tex; pifb2/12_section.tex; pifb2/13_section.tex; pifb2/17_section.tex; pifb2/18_section.tex; pifb2/20_section.tex; pifb2/21_section.tex; pifb2/22_section.tex; pifb2/23_section.tex; pifb2/24_section.tex; pifb2/28_section.tex; pifb2/30_section.tex; pifb2/31_section.tex; pifb2/32_section.tex; pifb2/33_section.tex; pifb2/34_section.tex; pifb2/35_section.tex; pifb2/36_section.tex; pifb2/37_section.tex
- Searched only: pifb2/19_section.tex (read lines 20-213; lines 1-19 and anything after 213 only searched for Omega and agent-evaluation phrases); pifb2/29_section.tex (read lines 1-100; remainder only searched); pifb2/36a_selection_proof.tex (read lines 1-90, the model declaration and theorem statement; the proof body only searched); pifb2/36c_supporting_proofs.tex (read lines 1-306, which covers every subsection heading found by search; any text after line 306 not read); pifb2/36b_latent_link_proofs.tex (searched for Omega, Theta and agent mentions; proofs not read); pifb2/14_section.tex; pifb2/15_section.tex; pifb2/16_section.tex; pifb2/25_section.tex; pifb2/26_section.tex; pifb2/27_section.tex; verified-ledger.md (searched for PIFB and participatory entries; none found)
- Not covered: pifb2/README.md (not a .tex file); PIFB2.pdf; The derivation documents linked from the observer-free note under docs/derivations/2026-10-21-gauge-agent-foundation/ (outside the assigned files); The archived MultiAgentELBO_Theory chapters cited by the observer-free note (outside the assigned files); No mathematics was re-derived; identities were taken as written, and the remark that the receiver-map derivative at 28_section.tex:130 contracts to coded moments was not asserted as a finding for that reason; No web search was run, per the task instructions

### Findings

#### pif-1. Consensus potential is called the potential of the agent dynamics; its gradient needs transported neighbor beliefs and the private quantities of the agents attending to i

- Location: `pifb2/08_section.tex:33`
- Class A, major
- Quantity: E[{q_i}] = sum_i KL(q_i||p_i) + sum\_{i,k} beta_ik KL(q_i || Omega_ik[q_k]) - sum_i E\_{q_i} log p(o_i|k_i); Omega_ik = e^{phi_i} e^{-phi_k}; transported precision Omega_ik^{-T} Lambda\_{q_k} Omega_ik^{-1}; sender-row gradient sum_j beta_ji Lambda\_{q_i} Omega_ji^{-1}(Omega_ji mu_i - mu_j)
- Evidence: Line 7: the natural-gradient flow 'descends the consensus potential E ..., which is therefore the potential of the agent dynamics'. Line 16: 'Each agent i maintains a belief distribution q_i'. Line 22: 'transported quantities mu~\_k = Omega_ik mu_k and Sigma~\_k = Omega_ik Sigma_k Omega_ik^T, where Omega_ik ... in Regime I the frame quotient e^{phi_i} e^{-phi_k}'. Line 78 (total gradient) contains both the receiver term beta_ik Lambda~\_{q_k}(mu_i - mu~\_k) and the sender term beta_ji Lambda\_{q_i} Omega_ji^{-1}(mu~\_i^{(j)} - mu_j). Line 185: 'the sender block resists moves that would disturb the agents attending to i'. Further lines: 59-66, 102, 116, 140, 150-153, 182-184. The same sender-row structure is in 06_section.tex:85-91 ('The second sum records the agent's role as a source'). Declared scope: line 12 says the calculation concerns 'the legacy consensus potential E, with invertible full-state transports'; 04_section.tex:107 restricts Omega_ij to frames that 'share a reference trivialization'. By 04_section.tex:137-147 the receiver comparison in that scope equals KL of the two beliefs pushed to the reference fiber, so the receiver-side need reduces to the sender's full belief in reference coordinates; the sender-row terms are not covered by any declared scope.
- Who evaluates: The agents, by the wording of lines 7 and 16. No sentence says how agent i obtains Omega_ik, the full q_k, or the beta_ji, mu_j, Sigma_j of the agents attending to it.
- Replacement: Receiver side: the received message law N(L_ij mu_j, L_ij Sigma_j L_ij^T + D_ij) with W_ij = C_ij^{-1}, already in this file at lines 218-241, in 29_section.tex:14-48, and as a comparison record in 05_section.tex:75-90 with the exact receiver update of 36c_supporting_proofs.tex:228-245. Sender-row terms: no privacy-respecting counterpart found; the receiver-only field of 34_section.tex:251-258 and 28_section.tex:169 drops them but is declared an optional nonpotential approximation and not the consensus update.
- Falsifies: A sentence in 07, 08 or 28 stating that the flow is evaluated by one system holding every agent's state, or that each agent posts its full reference-frame belief and its attention row to its sources, or that the stiffness blocks are claimed only as a describer's second variation of E with no agent following the flow.

#### pif-2. Receiver-only covariance flow 'of all agents' uses the transported sender precision and softmax of full-belief divergences

- Location: `pifb2/31_section.tex:17`
- Class A, minor
- Quantity: E_i = KL(q_i||p_i) + sum_j beta_ij KL(q_i || Omega_ij q_j) - E log p(o_i|k_i); fixed point Sigma_i^{-1} = (1/2)[Sigma\_{p,i}^{-1} + sum_j beta_ij (Omega_ij Sigma_j Omega_ij^T)^{-1} + Lambda\_{o_i}]; beta_ij proportional to exp[-KL(q_i || Omega_ij q_j)/tau]
- Evidence: Line 12: 'the gradient of agent i's block E_i of the consensus functional'. Lines 17-21: the block. Line 90: 'each agent's precision is half the sum of its prior and sensory precision and the beta-weighted transported neighbor precisions'. Line 114: 'the simultaneous receiver-only natural-gradient flow of all agents, d Sigma_i/dt = -2 eta Sigma_i (dE_i/dSigma_i) Sigma_i'. Lines 157-169: beta_ij as a softmax of KL(q_i || Omega_ij q_j). Line 216: 'each agent's problem with its neighbors frozen is strictly convex in Sigma_i'. Lines 219-222: mean step with Sigma_i (Omega_ij Sigma_j Omega_ij^T)^{-1}(mu_i - Omega_ij mu_j). Declared scope, lines 6 and 12: 'a local, fixed-attention, receiver-only surrogate'; 'invertible noiseless links are fixed'; 'the normalized collective VFE and general noisy selective channels have different equations'.
- Who evaluates: Each agent, by the wording of lines 12, 90, 114 and 216. The text does not say how the transported sender precision or the full transported belief reaches the receiver.
- Replacement: The received-law version: r = N(L mu_j, L Sigma_j L^T + D), objective KL(q||p) + beta KL(q||r), stationary precision (P + beta W)/(1+beta), in 29_section.tex:14-56; the likelihood version at 29_section.tex:81-91. Both need only the coded mean and a posted coded covariance. No sender-row terms arise because this appendix is receiver-only.
- Falsifies: A statement that the neighbor precision in Eq. sigma_fixed_point_beta is a posted message already expressed in the receiver's coordinates, or that the flow is a describer's surrogate that no agent runs.

#### pif-3. Best-response theorem is posed as 'agent i solves' with the full transported neighbor density as template

- Location: `pifb2/33_section.tex:9`
- Class A, minor
- Quantity: min over q_i of KL(q_i||p_i) + sum_j beta_ij D(q_i, Omega_ij q_j), with r_j = (Omega_ij)\_# q_j as a density on the receiver's sample space; marginal attention cost C_ij = D(q_i^\*, Omega_ij q_j)
- Evidence: Line 9: 'With the neighbor beliefs q_j and the weights beta_ij >= 0 held fixed, agent i solves' the minimization. Line 5: 'Put r_j = (Omega_ij)\_# q_j and use its density in the receiver's sample space'. Line 42: 'With r_j = Omega_ij q_j ... the unique minimizer is q_i^\* = g'. Lines 128-131: the marginal attention cost 'identifies the cost of attention with the divergence between the agent's best response and the neighbor's transported law'. Line 137: 'Gauge covariance fixes what is compared, the law q_i and the transported law Omega_ij q_j in one frame'. Counterpart sentence, line 5: 'More general normalized channels can supply the fixed template r_j when it has a density. ... it is not automatically a theorem about every restricted channel image'.
- Who evaluates: Agent i (line 9). The template is treated as given; the text does not say who performs the transport or how the full density reaches i.
- Replacement: A channel-supplied template r_j = q_j K_ij, stated at line 5 of this file and defined in 04_section.tex:181-193. I am unsure the theorem transfers to low-rank coded content: its converse quantifies over all nonsingular Gaussian templates on the receiver's full space, and a pushforward T\_# q_j on a smaller space is not such a density; line 5 flags this limit itself.
- Falsifies: Showing that the appendix intends r_j only as an arbitrary fixed density with no claim that agent i can form it, or a derivation in the assigned files of the same characterization for coded marginals in a message space.

#### pif-4. Complete update equations, including the frame update, are written per agent with no evaluator named; cost paragraph implies one global computation

- Location: `pifb2/28_section.tex:175`
- Class C, minor
- Quantity: mu_i, Sigma_i, U_i updates from grad E_red; E_ij = KL(q_i || Omega_ij[q_j]); beta_ij = softmax(-E_ij/tau); frame gradient sum_j beta_ij N_ij U_i^{-T} - sum_k beta_ki Omega_ki^T N_ki U_k^{-T}
- Evidence: Line 10: 'Omega_ij = U_i U_j^{-1}'. Lines 14-18: pair energies E_ij := KL(q_i || Omega_ij[q_j]) and rows beta_ij, 'so that beta_ij = beta_ij({q},{U}) depends on the beliefs and frames of the receiver i and of every source m in its row'. Line 22: 'A state variable x_i of agent i appears in the row of agent i and, as the sender, in the row of every agent k that attends to i'. Lines 49-58: full mean and covariance gradients with Omega_ij mu_j, A_ij = Omega_ij Sigma_j Omega_ij^T, Sigma_k, d_ki. Line 85: frame gradient uses U_k^{-T} of each receiver k. Lines 173-180: 'Every derivative below is the complete receiver-plus-sender envelope gradient of E_red', followed by mu_i^{t+1}, Sigma_i^{t+1}, U_i^{t+1} = U_i^t exp(-eta_phi xi_i^t). Line 184: 'Per gradient step with N agents ... forming the links costs O(N K_q^3) for the frames and their inverses plus O(N^2 K_q^3) for the pairwise products'. Declared scope, line 6: 'inverse-link formulas ... assume ... invertible noiseless links. Frame-factorized derivatives additionally assume Omega_ij = U_i U_j^{-1}. They are a specialization of the general channel model'.
- Who evaluates: The text does not say. The passive phrasing ('The update uses') and the O(N^2 K_q^3) cost at line 184 read as one centralized computation over all agents, but no sentence states that a single system holds all frames and beliefs.
- Replacement: For belief updates, the selective-link form at lines 118-130 of this file uses only L_ij mu_j and L_ij Sigma_j L_ij^T + N_ij on the receiver side. Line 130 gives endpoint derivatives (grad_L E) S_j^T and R_i^T (grad_L E) without assigning them to an endpoint. No agent-computable replacement for the frame update or for the sender-row terms was found in the assigned files.
- Falsifies: A sentence in 28 or 07 declaring that these equations are run by a single system with access to all U_i and q_i (class D), or a rule assigning each term of the frame gradient to messages an endpoint actually receives.

#### pif-5. Latent-link stationarity, current and learning rule read both endpoints' full moments; the holder of the link recognition law is not named

- Location: `pifb2/05b_lie_links.tex:64`
- Class C, minor
- Quantity: Theta_e = U_i exp(omega_e) U_j^{-1}; recognition R = N(mu-ring, Lambda-ring^{-1}) on generators; current J_e = W_a[(mu_i - M_e mu_j) mu_j^T + Sigma_ij - M_e Sigma_j]; Bayesian learning rule for (mu-ring, Lambda-ring); loop action A_loop over a supplied family of closed walks
- Evidence: 04_section.tex:233: the link chart 'Theta_e = U_i exp(omega_e) U_j^{-1}' with a 'reference frame at c\_\*'; 04_section.tex:240: 'The interaction graph and the frames remain structural'. 05_section.tex:53: 'Structural data X contain the graph, frames and interfaces'. This file, line 4: 'R recognizes the generator family'. Lines 10-11: 'Hold the agents' recognition Q_Y and restrict the joint recognition to R x Q_Y'. Line 64: the current with mu_i, mu_j, Sigma_j and 'Sigma_ij ... the cross covariance under Q_Y'. Lines 95-107: 'the joint inference law is Q-dot = -grad^G F_V' and the boxed generator learning rule. 05_section.tex:42: the loop defect uses 'a supplied finite family of closed walks' and a fiber metric at the reference.
- Who evaluates: The text does not say. The link recognition law is placed 'inside the same collective evidence bound as the agents' (01_section.tex:12), which reads as a collective object, but no sentence assigns R, the current, or the loop term to an endpoint, to the collective, or to a describer.
- Replacement: A receiver-owned dictionary learned from coded messages would be the P-compatible form; I found none in the assigned files. The nearest items are the unowned endpoint derivatives for L_ij = R_i S_j at 28_section.tex:130 and the supplied typed comparison Theta_ij of the shared-predictions note (line 30), neither of which states an owner or a learning rule from received content.
- Falsifies: A sentence stating that R is a describer's or collective law that no agent holds, or one assigning the generator of edge j to i to the receiver and deriving its update from quantities the receiver receives.

#### pif-6. Local agent equations and a parameter-acceptance rule are stated on the collective potential with no evaluator

- Location: `pifb2/07_section.tex:202`
- Class C, minor
- Quantity: V in {F_V, E}; mu_i-dot = -eta Sigma_i grad\_{mu_i} V, Sigma_i-dot, U_i-dot = -eta_phi U_i xi_i; acceptance test 'does not increase F_V'
- Evidence: Line 189: 'Let V denote either the normalized collective free energy F_V or the separately declared consensus potential E'. Line 202: 'a new parameter value is accepted only if it does not increase F_V at the fixed recognition law'. Lines 311-317: 'the local equations can be written' with mu_i-dot, Sigma_i-dot and U_i-dot driven by gradients of V. Line 301: 'In the frame-factorized special case Omega_ij = U_i U_j^{-1}, common-pushforward invariance removes the frames from alignment terms by using (U_i^{-1})\_# q_i'. Lines 251-256 give a case where the node gradient needs only neighbor means: mu-dot = -eta diag(s_i) H mu with H = eps I + k L.
- Who evaluates: The text does not say who evaluates F_V for the acceptance decision or who forms grad\_{x_i} V. F_V is the free energy of the whole population law (05_section.tex:19-23).
- Replacement: The block objective F_i(Q_i; Q\_{-i}, o) with factor messages m\_{a to i} in the observer-free note (lines 246-252) is the local counterpart for product families; that note warns that the sum of the local objectives is not the collective one. No local acceptance rule is stated in the assigned files.
- Falsifies: A sentence assigning the acceptance test to a describer or to a named collective mechanism, or showing that the change in F_V under the parameter move depends only on one agent's own block.

#### pif-7. Collective free energy and its recognition law are the foundation, but no passage says who holds or minimizes them

- Location: `pifb2/05_section.tex:19`
- Class C, minor
- Quantity: F_V[Q; X, o] = KL(Q || P_0 Pi) - E_Q log l_o, with Q(dy, dJ) a joint law over all agents and X collecting all frames and interfaces; correlated edge cost with cross covariance Sigma_ij
- Evidence: Line 4: 'The probabilistic foundation is one normalized law for the population'. Line 7: 'Let X collect structural parameters: available edges, interface maps, noise parameters and frame presentations'. Lines 19-23: F_V. Line 27: 'The local sections zeta_i are marginals of Q, with dependence on the records restricted by their access maps if required'. Lines 95-103: the expected link cost contains A_i Sigma_ij B_ij^T, 'one place where a collective law conveys information that separate marginal beliefs miss'. 04_section.tex:87 defines an agent as including 'its access to records', the one place access is made part of the definition.
- Who evaluates: The text does not say. Access maps are mentioned (line 27) but not defined, and no agent, collective mechanism or describer is named as the minimizer of F_V.
- Replacement: The observer-free note supplies the accounting: its lines 192-232 show marginal agents cannot close the correlated dynamics in general, and lines 234-252 give the product-family block objective with an explicit access condition. PIFB2 itself does not import that condition.
- Falsifies: A definition of the access maps in pifb2 that makes each agent's update a function of its own marginal and received records, or a sentence stating that F_V is a describer's functional.

#### pif-8. Cross-scale shadow assigns a child's prior as the parent's full belief transported by a two-frame map

- Location: `pifb2/10_section.tex:49`
- Class C, minor
- Quantity: p_i^{n+1} = (Omega_iI)\_# q_I^n and r_i^{n+1} = (Omega~\_iI)\_# s_I^n; link kernel N(k_i; Omega\_{i,pi(i)} k\_{pi(i)}, sigma^2 I) with Omega\_{i,pi(i)} = exp(phi_i) exp(-phi\_{pi(i)})
- Evidence: Lines 47-53: 'If a child is a deterministic transported copy of a parent latent in the previous episode', followed by the two pushforward formulas. Line 54: 'A general selective downward kernel replaces Omega\_# by K_iI ... derived under a transported-copy transition, not a universal source of priors'. 34_section.tex:21: 'Omega\_{i,pi(i)} = exp(phi_i^{(l)}) exp(-phi\_{pi(i)}^{(l+1)})'. 34_section.tex:68: 'The first expectation is the top-down message from the parent of agent i ... the sum collects the bottom-up messages from its children'. 34_section.tex:82: predictive density N(Omega mu_parent, Omega Sigma_parent Omega^T + sigma^2 I). 09_section.tex:48: 'Express child states in a chosen parent frame'.
- Who evaluates: The text presents the formula as a transition kernel of a declared process law, so the transport is part of the generative model; it does not say whether the child, the parent or neither computes the pushforward, or how the parent's full belief and frame reach the child.
- Replacement: The selective downward kernel K_iI (line 54 of this file) and the channel k_i | k_parent ~ N(L k_parent, N_i) with predictive law N(L mu, L Sigma L^T + N_i) at 34_section.tex:95-96; the cavity message at lines 26-32 of this file for the same-time case.
- Falsifies: A sentence stating that the downward message is the already-transported law delivered to the child, or that the shadow formula is a describer's identity for a process no agent evaluates.

#### pif-9. Omega_ij is defined as a reference identification under a declared shared trivialization, in propositions about coordinates

- Location: `pifb2/04_section.tex:100`
- Class B, note
- Quantity: Omega_ij = U_i U_j^{-1}; cocycle and trivial loop products; KL(q_i || (Omega_ij)\_# q_j) = KL(q-bar_i || q-bar_j) with q-bar_i = (U_i^{-1})\_# q_i
- Evidence: Line 93: 'On a common trivializing neighborhood let U_i present the reference sample fiber in agent i's coordinates'. Lines 100-105: Omega_ij 'expresses the same reference vector in different coordinates ... It does not specify which sender directions are communicated'. Line 107: 'Where the frames share a reference trivialization'. Lines 137-148: removability, then 'This removes only the reference frames'. Line 218: 'Regime I names only the flat identification'. 37_section.tex:26: 'Flat reference identification U_i U_j^{-1}. It does not encode a general selective message'. Related describer-level uses: 20_section.tex:37-43, 19_section.tex:192-206, 35_section.tex:102.
- Who evaluates: No agent. These are definitions, a lemma and propositions about coordinate presentations; the text separates them from communication at line 4 ('a change of coordinates is not an exchange of information').
- Falsifies: A passage in section 04 that has an agent form Omega_ij from another agent's frame as part of an update.

#### pif-10. Loop operators, network holonomy and scientific agreement are stated as relational invariants with an explicit observability caveat

- Location: `pifb2/23_section.tex:31`
- Class B, note
- Quantity: L_gamma = L\_{i0 i1} ... L\_{i(r-1) i0}; its rank, characteristic polynomial and traces; agreement on a public statistic
- Evidence: Lines 31-36: the loop operator and its invariants; 'Neither construction alone is curvature of a connection'. Line 38: 'A nontrivial internal loop operator is observable only to the extent that those records distinguish its action; a law invariant under that action can hide it'. Line 42: 'A record appears once in its generative factorization even when several agents can access it ... A community that agrees is therefore not, on that fact alone, calibrated'. Line 44: comparison 'under the same access constraints'. Line 52: 'observer access remains mediated by records and inference'.
- Who evaluates: A describer of the network; the text proposes 'targeted relational observations' through records and does not have an agent compute a loop product through edges it does not own.
- Falsifies: A passage in which an agent's update or decision uses L_gamma or a holonomy around a loop containing edges it does not own.

#### pif-11. Parent laws, moment projections, the parent frame and the holonomy-fixed Gaussian family are describer constructions

- Location: `pifb2/09_section.tex:48`
- Class B, note
- Quantity: Q^c = QC; mu_I = sum w_i mu~\_i, Sigma_I with dispersion; U_I in argmin sum w_i d_G(U, U_i)^2; C_i L_ij = L^c_IJ C_j; holonomy-fixed family G_rho and coherence score
- Evidence: Line 4: 'Given a fine law and a normalized coarse channel, its law is induced exactly'. Lines 48-53: 'Express child states in a chosen parent frame' and the moment projection. Line 81: 'This is a fitted population distribution, not automatically a posterior on a new physical object'. Lines 92-97: 'A frame can simply be chosen ... it is not part of what makes a parent'. Line 45 and 36c_supporting_proofs.tex:144-150: the family fixed 'by the pushforward of every holonomy of a closed walk of the block' is empty almost surely. Line 103: 'A parent may be coherent in what it exchanges while its members retain distinct internal descriptions'.
- Who evaluates: A describer who is given the fine law and the channel; the text does not have children or the parent compute the projection or the holonomy.
- Falsifies: A passage in which a member agent computes mu_I, Sigma_I or U_I from the other members' beliefs and frames as part of its own update.

#### pif-12. Four-cycle selection theorem is a statement about one declared joint stochastic process with shared edge variables

- Location: `pifb2/36a_selection_proof.tex:10`
- Class B, note
- Quantity: D_e = (1/2)[(k\_{i+1} - k_i - w_e)^2 + (m\_{i+1} - m_i - w_e)^2]; Langevin motion of x in R^12 under U_J; redraw of the full assignment from beta_J(X; pi); pi_ij-dot = eps_L (q_t(J_i = j) - pi_ij)
- Evidence: 13_section.tex:7: 'four scalar belief coordinates, four model coordinates and one shared scalar translation on each unoriented edge'; 13_section.tex:12: 'Both directions of source selection use the same edge variable and cost ... learn from the actual recognition law'; 13_section.tex:17: 'These ingredients, including the reference and kinetics, are part of the model'. This file, line 18: 'Each agent i, acting as a receiver, has both neighbors as candidate sources'. Lines 33-37: one diffusion on the whole configuration and a redraw of 'the complete assignment'; 'The recognition law q_t is the law of (X_t, J_t)'. Line 44: 'The redraw therefore refreshes the assignment from its conditional law'.
- Who evaluates: The declared kinetics of the whole configuration; the theorem is about the law q_t. The text does not discuss which endpoint holds w_e or how a receiver obtains its neighbor's coordinate for D_e.
- Falsifies: A passage presenting the four-cycle kinetics as each agent's private computation from its own data.

#### pif-13. State-dependent couplings built from the transported sender covariance are a describer's value-level matching

- Location: `pifb2/32_section.tex:32`
- Class B, note
- Quantity: W^(q)\_ij := c_ij (Omega_ij Sigma\_{q,j} Omega_ij^T)^{-1}; (1/4) E[(k_i - Omega_ij k_j)^T W (k_i - Omega_ij k_j)] = (c/2) KL(q_i || Omega_ij q_j) + constants + log-det term
- Evidence: Line 3: 'This appendix treats the invertible, noiseless, product-Gaussian consensus specialization at c\_\*'. Lines 30-36: 'we choose state-dependent couplings ... the identification below is a value-level matching at the current variational state, not a property of a fixed generative model ... The normalized comparison-record model of Section free_energy instead supplies a fixed likelihood precision and is a different objective'. 35_section.tex:113: the live alignment term 'may remain a configuration-level consensus potential, or it may be replaced by a fixed state-transition or pair potential'.
- Who evaluates: The authors ('we choose'); an identity relating two expressions, with no agent computing W.
- Falsifies: A passage in which a receiver sets its coupling precision from the sender's current covariance during an update.

#### pif-14. Observer-free note: collective recognition law and its Fisher flow are an existence construction that the note says marginal agents cannot close

- Location: `2026-10-21-observer-free-gauge-agent-foundation.md:190`
- Class B, note
- Quantity: Q on Z with zeta_i^Q(c) = (f\_{i,c})\_# Q; F(Q; o) = KL(Q||P_0) - E_Q log l_o; theta-dot = -G^{-1} dF with G the Fisher metric of the collective law; conditional cost C_t(x) in the marginal velocity
- Evidence: Line 5: 'This is an existence construction with supplied geometric and probabilistic data. It does not yet derive ... the agents' interaction mechanisms, locally implementable correlated inference'. Line 65: 'the relational probability data must be retained explicitly'. Line 102: 'Writing their joint probability law does not posit an external observer'. Line 145: the Fisher flow 'is an additional kinetic choice'. Line 190: 'The full Fisher metric ... is the metric of the collective recognition law. It is generally not the sum of the Fisher metrics of its one-agent marginals. This distinction affects both dynamics and the possibility of local implementation'. Lines 210 and 232: 'an exact dependence on retained joint information'; 'even the complete list of singleton marginals does not determine their exact Fisher velocities'. Line 274: 'This protocol is a constitutive choice'. Line 414: 'The construction has not yet made full correlated inference an autonomous law of the marginal sections'.
- Who evaluates: No agent and, by line 102, no external observer: the flow is specified as a constitutive law of the collective law Q. I class it B by function (an existence construction and theorems about the system); the note's own wording denies that a describer outside the system holds Q, so who holds Q is left open by the text.
- Falsifies: A passage in the note having a participating agent compute G^{-1} dF or the conditional cost C_t from its own marginal.

#### pif-15. Shared-predictions note: transported model disagreement is a describer's hypothesis; the comparison map has no stated owner

- Location: `2026-10-21-shared-predictions-from-gauge-model-agreement.md:30`
- Class B, note
- Quantity: Theta_ij: M_j to M_i; s~ = Theta_ij# s_j; L(m, A) = K_j(Theta_ij^{-1} m, A); hypothesis D(s || s~) \<= eps; rho_i = sK, rho\_{j to i} = s~L; mixture rho-bar = sum w_i rho_i; I(I;O)
- Evidence: Line 21: 'Writing a global process law does not assert that any internal agent possesses or computes it. Likewise, an expectation in a mathematical inequality does not require an actual observer averaging'. Lines 30-33: Theta_ij is 'a fixed bimeasurable bijection'. Lines 37-42: 'In agent i's presentation define' s~ and L. Lines 63-67: 'Assume exact predictive compatibility and finite transported model disagreement'. Line 193: Theta'\_ij = g_i Theta_ij g_j^{-1}, so Theta_ij is independent data and not a function of two frames. Line 237: 'Such a presentation is additional compatibility data'. Line 245: rho-bar 'is a mathematical reference'. Line 409: members 'supply nearly the same probabilities for corresponding internally generated records'. Line 415: 'The next concrete obligation is to ... identify its normalized predictive evaluator and establish a compatibility residual'. Line 417: 'Comparing only a finite collection of record events can test those predictions'.
- Who evaluates: A describer: the divergence between full model laws is assumed, not computed by either agent, and the agreement conclusion is about record probabilities. The text does not say whether Theta_ij is owned by the receiver, the sender or neither.
- Falsifies: A passage in the note having agent i evaluate D(s_i || Theta_ij# s_j) or use it in an update or decision.

#### pif-16. Selective sending and receiving factor each link through a message space with each endpoint using only its own frame

- Location: `pifb2/04_section.tex:151`
- Class E, note
- Quantity: S_j: E_j to H, R_i: H to E_i, L_ij = R_i S_j; attention realization S_j = T U_j^{-1}, R_i = U_i O; channel output q_j K_ij = N(L_ij mu_j, L_ij Sigma_j L_ij^T + N_ij); reduced comparison of A_ij# q_i and B_ij# q_j; public/private chain rule
- Evidence: Lines 151-155: message space H with sender map S_j and receiver map R_i. Line 173: 'The attention realization S_j = T U_j^{-1}, R_i = U_i O'. Lines 187-193: Gaussian channel output. Line 196: 'Alternatively compare A_ij# q_i and B_ij# q_j in a common measured space ... Comparison interfaces determine attention and content maps determine the message'. Lines 208-214: KL(q||p) = KL(T\_# q || T\_# p) + conditional term; 'Perfect communicated agreement can coexist with different private conditional laws'. Figure caption, line 62: 'a sender exposes information through S_j and the receiver reconstructs it through R_i'.
- Who evaluates: Sender applies S_j, receiver applies R_i (caption and line 171). The text does not say who owns the comparison maps A_ij, B_ij.
- Falsifies: A passage showing that S_j or R_i must be built from the other endpoint's frame.

#### pif-17. Comparison records and the channel-consensus cost are built from interface outputs, not from Omega-transported beliefs

- Location: `pifb2/05_section.tex:77`
- Class E, note
- Quantity: o_i = A_i k_i - B_ij k_j + eps_i; D_ij(y) = (1/2)|A_i k_i - B_ij k_j|^2 in Gamma_i^{-1}; source attention proportional to pi_ij exp(-D_ij/tau_i); E^K_ij = KL(q_i || q_j K_ij)
- Evidence: Lines 77-83: the record and 'The maps have a common output space within row i, and Gamma_i is the same for its candidate sources'. Lines 108-121: the conditional and restricted attention rows. Lines 150-152: 'E^K_ij = KL(q_i || q_j K_ij)'. Line 167: 'Reduced-space divergences can replace the costs when comparison is defined in message space'. Lines 222-223: the delta kernel at Omega_ij x 'recovers the old transported Gaussian consensus model', kept 'separate' from the principal construction. Line 29: 'The generative law reads latent coordinates and declared parameters, not the live recognition law Q'.
- Who evaluates: The row-i record is read by receiver i's row; the text does not say who owns B_ij ('The interfaces are generative parameters unless made latent', line 105).
- Falsifies: A passage showing that B_ij k_j or q_j K_ij is formed by the receiver from the sender's uncoded state.

#### pif-18. Open single-agent response to a received law, and its likelihood alternative, use only the received message

- Location: `pifb2/29_section.tex:14`
- Class E, note
- Quantity: received law r = N(m, C), m = L mu_j, C = L Sigma_j L^T + D; E_KL(q) = KL(q||p) + beta KL(q||r); alternative F_V(q) = KL(q||p) + (beta/2) E_q[(z-m)^T W (z-m)]
- Evidence: Lines 14-20: 'A sender supplies a fixed law through the channel z = L z_j + eps, L = R_i S_j ... Its received law is r = N(m, C) ... This is an open single-agent response calculation, not the complete two-agent variational update, which also differentiates sender contributions'. Lines 22-27: the objective. Lines 81-91: 'Suppose a registered message m is an observation with Gaussian likelihood ... Replacing one by the other requires specifying whether the message is a distribution to imitate or a registered datum in a likelihood'.
- Who evaluates: The receiving agent alone, from its own prior and the received law (line 20).
- Falsifies: A step in lines 14-91 that reads the sender's mu_j or Sigma_j other than through m and C.

#### pif-19. Exact receiver update and the downward-coupling identity read coded source states and latent coordinates, never another agent's belief

- Location: `pifb2/36c_supporting_proofs.tex:228`
- Class E, note
- Quantity: E[k_i | k\_{-i}, o] = mu_i + sum_j w_ij K_i (B_ij k_j - A_i mu_i), K_i = Sigma_i A_i^T (Sigma_i^pred)^{-1}; cross-scale term E\_{Q_Z} KL(Q_Y || K_down(.|Z))
- Evidence: Lines 228-244: the receiver update uses pi_ij, A_i, tau_i Gamma_i, the receiver's own (mu_i, Sigma_i) and B_ij k_j; 'In the full-state receiving form A_i = I, B_ij = Omega_ij'. Line 299: 'Its generative denominator reads the parent's latent coordinate z and never the parent's recognition law'. 35_section.tex:67: 'the construction does not treat a variational belief of another agent as a fixed generative factor'.
- Who evaluates: The receiver, conditional on the coded source states; the statement is a conditional-law identity inside the population model.
- Falsifies: A term in Eq. sp_receiver_update that depends on the sender's state other than through B_ij k_j.

#### pif-20. Operational agreement and the objectivity entry are defined on communicated laws in a declared common output space

- Location: `pifb2/20_section.tex:49`
- Class E, note
- Quantity: K_ij = KL(r\_{i|ij} || r\_{j|ij}); objectivity as 'Agreement on communicated records'; collective Fisher tensor of Q(c) and weighted marginal sum G-bar
- Evidence: Lines 49-54: 'the interface model compares laws on a declared common output space ... obtained from the endpoint laws by their respective receiving and sending kernels ... Communication gives perfect public agreement while private means differ'. Line 104 (table): 'Objectivity | Agreement on communicated records | Persistence and successful predictions under intervention'. Lines 9-15: the collective tensor 'reads the joint law, including correlations' and the weighted sum is 'A convenient descriptive alternative'. 09_section.tex:100: 'Coherence is agreement in declared communicated observables'.
- Who evaluates: The text does not say who computes K_ij; both arguments are coded marginals. The collective Fisher tensor and G-bar are describer-level (class B) by the word 'descriptive' at line 9.
- Falsifies: A passage defining agreement or objectivity through KL(q_i || Omega_ij q_j) or through a consensus set over all agents.

#### pif-21. State-level obstruction and self-consistent source model are written for general channels T_ij q_j and receiver responses

- Location: `pifb2/34_section.tex:128`
- Class E, note
- Quantity: T_ij a mass-preserving map on densities 'induced by a normalized communication channel, including (Omega_ij)\_# as a special case'; E_ij(q) = KL(q_i || T_ij q_j); beta_ij(q); response map B_i(q); receiver-only field V_i^rec
- Evidence: Line 128: definition of T_ij. Lines 195-200: E_ij and beta_ij from T_ij q_j. Lines 204-215: geometric-pooling response and 'receiver-response equilibrium'. Line 246: 'Because the response holds incoming source roles fixed, its equilibrium is not thereby a stationary point of the global smoothing scalar'. Lines 251-258: the receiver-only field 'is an optional update approximation'. Line 5: 'no generative kernel reads a recognition law'.
- Who evaluates: The receiver for B_i and beta_ij, given the channel images T_ij q_j; the text does not say that T_ij q_j is the message actually delivered, which is the reading under which this is privacy-respecting.
- Falsifies: A statement that T_ij q_j must be formed by the receiver from the sender's uncoded belief, which would move this to class A.

#### pif-22. Participation decision uses the agent's own predictive prior and its own observation channels

- Location: `pifb2/12_section.tex:31`
- Class E, note
- Quantity: I_a = E\_{o|a} KL(P(dk|o,a) || p^-(dk)); J(pi) = sum_a pi(a)[l(a) - lambda I_a] + tau_A KL(pi||rho); pi^\*(a)
- Evidence: Lines 31-50: 'Choosing a link, experiment or action is a decision ... a finite action set, a strictly positive reference policy rho(a), and an action-independent predictive prior p^-(k). A normalized observation channel for each action gives expected information gain'. Line 52: 'This is an optional decision model'.
- Who evaluates: The deciding agent, from its own predictive law, channels, costs and reference policy.
- Falsifies: A term in J(pi) that depends on another agent's belief or frame.

#### pif-23. Observer-free note: product-family block objective states an explicit access condition; Hopf record is built from arrivals in the receiver's fiber

- Location: `2026-10-21-observer-free-gauge-agent-foundation.md:252`
- Class E, note
- Quantity: F_i(Q_i; Q\_{-i}, o) = KL(Q_i||P\_{0,i}) - sum over incident a of E_Q log k_a; messages m\_{a to i}(z_i); record kernel k_b(1|a) = 1/2 + eps h(|v_r|^2) h(|T_gamma1 v_s - T_gamma0 v_s|^2)
- Evidence: Line 252: 'The required message from factor a is the function m\_{a to i}(z_i) ... The update can be implemented from these functions and the local prior if the declared communication mechanisms supply them. This is an explicit access condition, not a consequence of drawing an interaction graph ... The sum of the local objectives (21) generally counts shared factors repeatedly and is not (20)'. Line 69: a record kernel 'may depend on selected field evaluations, model presentations, communication maps, and parallel transports along declared paths'. Lines 354-362: 'The receiver also has a represented state ... Its binary register follows the normalized kernel ... both arrivals transform in the receiver's fiber ... an intrinsic kernel'. Line 373: 'the record belongs to the receiver, and both transmissions originate from the sender'.
- Who evaluates: Agent block i, from its local prior and the factor messages, conditional on the declared communication mechanisms supplying them; in the Hopf example the receiver's register, with the connection supplied.
- Falsifies: A demonstration that m\_{a to i} cannot be formed without another block's full law in a case the note claims as locally implementable; the note makes no such claim beyond the conditional.

### Hidden requirements

- A shared reference trivialization is required for Omega_ij = U_i U_j^{-1} to exist at all (pifb2/04_section.tex:93 and :107).
- In Regime I the transported comparison equals a comparison of both beliefs pushed to the reference fiber, so the receiver-side need is the sender's full belief in public reference coordinates, a full-rank message (pifb2/04_section.tex:137).
- Selective links need a message space H known at both ends, and the attention realization S_j = T U_j^{-1}, R_i = U_i O needs the code maps T and O to be common knowledge (pifb2/04_section.tex:151 and :173).
- The receiver needs the sender's coded covariance L_ij Sigma_j L_ij^T and the channel noise covariance N_ij or D_ij to form the received law and W_ij (pifb2/04_section.tex:189; pifb2/08_section.tex:219; pifb2/29_section.tex:20).
- Comparison records need a common output space within row i, a noise shape Gamma_i common to all candidate sources, and maps B_ij whose owner is not stated (pifb2/05_section.tex:83 and :105).
- The correlated edge cost needs the cross covariance Sigma_ij between two agents' states, which belongs to the joint recognition law and to no single agent (pifb2/05_section.tex:95).
- The full-state consensus gradient needs the sender's precision transported into the receiver frame (pifb2/08_section.tex:24; pifb2/31_section.tex:66; pifb2/32_section.tex:32).
- The canonical gradient makes agent i need the attention weight beta_ki, mean, covariance and link of every agent k attending to it (pifb2/06_section.tex:88; pifb2/08_section.tex:78; pifb2/28_section.tex:22).
- The frame update for U_i needs the frame U_k of each receiver k, and each attention row depends on the frames of every source in the row (pifb2/28_section.tex:85 and :18).
- The latent link chart needs both endpoint frames and a common reference frame at c\_\*, and the loop prior needs a supplied family of closed walks and a fiber metric at the reference (pifb2/04_section.tex:231; pifb2/05_section.tex:42).
- The link current needs the sender's uncoded mean and covariance and the cross covariance of the two endpoints (pifb2/05b_lie_links.tex:64).
- The parameter-learning acceptance rule needs the value of the population free energy F_V (pifb2/07_section.tex:202).
- The homogeneous covariance limit assumes a prior covariance Sigma_0 shared by all agents and links that preserve it (pifb2/31_section.tex:137).
- The cross-scale shadow needs the parent's full belief, a parent frame and a child-parent transport built from both frames (pifb2/10_section.tex:49; pifb2/34_section.tex:21; pifb2/09_section.tex:48).
- Operational agreement K_ij needs a declared common output space and the sender's coded marginal as a law, not a sample (pifb2/20_section.tex:49).
- In the Gibbs source-selection example the receiver's cost reads the source variance delta directly (pifb2/21_section.tex:24).
- The four-cycle model uses one translation variable per unoriented edge shared by both directions of source selection, and each comparison cost reads both endpoint coordinates (pifb2/13_section.tex:7; pifb2/36a_selection_proof.tex:10).
- Reading all four components of the Hermitian moment requires 'access to the two components and a calibrated relative phase', which the text says arbitrary selective links do not supply (pifb2/19_section.tex:32).
- Local block updates need factor messages m\_{a to i} that the declared communication mechanisms must supply, and record kernels may read parallel transports along declared paths of a supplied connection (2026-10-21-observer-free-gauge-agent-foundation.md:252 and :69).
- The shared-prediction theorem needs a common record space with a declared translation of record labels, a fixed comparison bijection Theta_ij with no stated owner, and the sender's predictive kernel K_j for the compatibility condition K = L (2026-10-21-shared-predictions-from-gauge-model-agreement.md:35, :30 and :41).
- Predictions compared across agents need matched, transported or common-information histories, and population statements need one common model presentation chosen as additional compatibility data (2026-10-21-shared-predictions-from-gauge-model-agreement.md:53 and :237).

## Lane col: Collective agents, main sections

Investigator type `audit-variational`. The manuscript's stated architecture is privacy-respecting and I confirmed it with locations: frames U_i are private encodings, messages are coded content H_j m_j that pass through external states, each receiver holds its own code model H-hat_ij or learned translation Theta_ij, and the true translation U_i U_j^{-1}, mistranslation, world-conditional law, contrast, holonomy, frustration, order parameter and group expected free energy are describer-level objects. I found no class-A occurrence (an agent computing an inaccessible quantity with no declared scope), no class-D (single-system) setting, no exchange of dictionaries between agents, and no finding I would rate major. I found nine class-C items in which an agent rule, as its formula is written, consumes a P-inaccessible quantity under a label or hypothesis whose mechanism is not given in the assigned files; the two that bear on a central result are in the two-group formation model, where translation learning is fed the true inter-frame angle plus noise (07_formation.tex:40) and C1g calibration uses the true world state eta_t (07_formation.tex:39, :215). The others are the sender's sensing gain g_j inside the receiver's model (06_coherence.tex:31), the consensus filter of H1(d)/H5a that grants members n, the summed information matrix, centralized covariances and the coarse act (05_agency.tex:132, 10a_meta_agents.tex:249), partners' codes or conventions inside an agent's expected free energy (06_coherence.tex:134, 10b_hierarchy.tex:176), belief-dependent routing written as a function of neighbors' internal states (08_scale.tex:84), and aggregation 'after true translation' (10c_renormalization.tex:189). If the 'grounded' and 'let every member know' declarations are not accepted as scopes, the first five of these would be class A by the letter of the formulas; I classified them C because the text declares the scope and the supporting derivations are in the out-of-scope supplement. Exact fusion, class C2 and the exact-fusion null require cross-covariances, provenance or the mistranslation itself, and the text says so and states that exact fusion enters only as a reference and a null (13_discussion.tex:49).

### Coverage

- Read in full: Collective_Agents/sections/01_introduction.tex; Collective_Agents/sections/02_framework.tex; Collective_Agents/sections/03_misreading.tex; Collective_Agents/sections/04_collectives.tex; Collective_Agents/sections/05_agency.tex; Collective_Agents/sections/06_coherence.tex; Collective_Agents/sections/07_formation.tex; Collective_Agents/sections/08_scale.tex; Collective_Agents/sections/09_minimal.tex; Collective_Agents/sections/10_abstract_collectives.tex; Collective_Agents/sections/10a_meta_agents.tex; Collective_Agents/sections/10b_hierarchy.tex; Collective_Agents/sections/10c_renormalization.tex; Collective_Agents/sections/10d_environments.tex; Collective_Agents/sections/11_predictions.tex; Collective_Agents/sections/13_discussion.tex
- Searched only: Collective_Agents/sections/10e_open_problems.tex (not assigned; appeared only as hits of one grep for 'know', not read)
- Not covered: Supplement sections s\*.tex, proofs app\*.tex, checks chk\*.tex and extensions ext\*.tex, appext\*.tex, chkext\*.tex (declared out of scope). Several findings turn on statements that live there and that I did not check: prop:fw-rls (reduction of grounded learning to the angle rule), prop:fw-efe-communication, prop:coh-frustration-grounding, prop:coh-coded, prop:ren-codes and prop:ren-code-levels, thm:agy-joint-acts, prop:met-level0, sec:prv.; 00_abstract.tex, 12_related.tex and 10e_open_problems.tex (not assigned).; Figure source files under Collective_Agents/figures (only the captions in the assigned section files were read).; No scripts, numerical checks or web lookups were run, per the lane instructions; the one agent-computable replacement I propose for calibration (second moment of y~\_ij - s_i minus R^s) is my own unverified inference from the model's independence structure.

### Findings

#### col-1. Two-group model: translation learning is driven by a noisy observation of the true inter-frame angle

- Location: `Collective_Agents/sections/07_formation.tex:40`
- Class C, minor
- Quantity: alpha\*\_ij = theta_i - theta_j, i.e. the true translation U_i U_j^{-1} = Rot(alpha\*\_ij), entering the update of the learned translation Theta_ij = Rot(alpha-hat_ij)
- Evidence: Line 40: 'alpha-hat_ij \<- alpha-hat_ij + alpha(alpha\*\_ij + nu^alpha_ij(t) - alpha-hat_ij), a grounded observation of the angle with noise nu^alpha ~ N(0, sigma_alpha^2)'. The true angle is defined at line 37. Line 53 asserts 'learning is the steady-gain form of the grounded estimator of prop:fw-rls with forgetting toward the identity' (prop:fw-rls is in the supplement, not read). The theorem-level clauses use sigma_alpha^2 = 0, 'noiseless angle observations' (lines 6, 164, 258, 260).
- Who evaluates: Receiver i applies the update. The text does not say, in the assigned files, how the noisy sample of alpha\*\_ij is formed from i's received messages and own observations; it labels it 'grounded'.
- Replacement: Grounded regression of j's messages on i's own observation of a jointly attended referent (prop:fw-grounded-identification), present at 02_framework.tex:166-180. The reduction of that estimator to a scalar-angle rule with constant noise sigma_alpha^2 is asserted at 07_formation.tex:53 and not shown in my files.
- Falsifies: A derivation (for example in prop:fw-rls of the supplement) showing that alpha\*\_ij + nu^alpha is the output of an estimator built only from y_ij and i's own observations. Absent that, the formula at line 40 by its letter has the receiver update with a function of both frames, which would be class A; I am unsure which reading the supplement supports.

#### col-2. Two-group model: C1g calibration uses the true world state eta_t (idealized form and online form)

- Location: `Collective_Agents/sections/07_formation.tex:39`
- Class C, minor
- Quantity: sigma-hat^2_ij = (1/K) E||y~\_ij(t) - eta_t||^2; online residuals (1/2)||y~\_ij - eta_t||^2
- Evidence: Line 39: 'Calibration is of class C1g, idealized: sigma-hat^2_ij = (1/K) E||y~\_ij(t) - eta_t||^2 at the current error phi_ij'. Lines 68-72: value R_c + MSE_j + D_cal(1 - cos phi) with D_cal = 2 Cov_1(eta_t, m_j(t)). Line 81: frozen calibration. Line 215: 'an exponential average ... of the grounded residuals (1/2)||y~\_ij - eta_t||^2 on attended rounds'. The model's only stated sensing is s_i = eta_t + v_i with variance R^s (line 36). C1g is defined at 02_framework.tex:141 as learned 'on grounded rounds, on which the receiver observes the referent'.
- Who evaluates: Receiver i assigns sigma-hat^2_ij. The idealized form is a population expectation involving the true state, the sender's true error and the true translation error that no agent is said to compute; the online form is an agent rule that takes eta_t as given on every attended round. The text does not say how eta_t is observed without noise in this model.
- Replacement: (i) Innovation calibration C1i from the receiver's own data (02_framework.tex:142; static model at 06_coherence.tex:31 and :49), which my files do not work out for the dynamic model, although conj:frm-formation names 'C1g or C1i' (07_formation.tex:265). (ii) Evident but not stated in my files, my own inference: (1/K) E||y~\_ij - s_i||^2 - R^s, since v_i(t) is independent of y~\_ij(t).
- Falsifies: A statement that in the two-group model every attended round is a grounded round with noiseless observation of eta_t (then it is a declared scope under P(d)), or a derivation of the calibrated noise from s_i alone.

#### col-3. Static two-group model: the receiver's message model contains the sender's sensing gain g_j

- Location: `Collective_Agents/sections/06_coherence.tex:31`
- Class C, minor
- Quantity: g_j = sigma_eta^2/(sigma_eta^2 + R^s_j), a function of the sender's sensing noise, inside receiver i's likelihood and its calibrated precision varpi_ij = g_j^2 / r-hat_ij
- Evidence: Line 31: 'under C1g and C1i receiver i models y~\_ij as g_j eta plus isotropic noise whose variance r-hat_ij matches the second moment of y~\_ij - g_j eta on grounded rounds (C1g) or of the innovation y~\_ij - g_j g_i s_i (C1i)'. Lines 49-50: 'r-hat_ij = R_c + g_j^2 R^s_j + r-hat^mt_ij', 'varpi_ij = g_j^2 / r-hat_ij'.
- Who evaluates: Receiver i uses g_j in its own model; the text does not say how i comes to hold it.
- Replacement: A receiver-owned attenuated code model learned by grounded regression (02_framework.tex:166-180; attenuation is noted at 03_misreading.tex:21 and 06_coherence.tex:22). My files do not apply this to the static model, and such a regression would also expose the mistranslation, which the C1 model is said not to use (06_coherence.tex:60).
- Falsifies: A statement that g_j is part of i's learned code model, or that senders' sensing noises are public in this model.

#### col-4. Consensus on information contributions: members are given n, the summed information matrix, the centralized steady-state covariances and the centralized start

- Location: `Collective_Agents/sections/05_agency.tex:132`
- Class C, minor
- Quantity: n = |C|, Lambda^s = sum_i Lambda^s_i, P-bar and P-bar^- of the centralized filter, the centralized initial estimate
- Evidence: Line 122: exact closure holds 'if every member knows, at every step, the averages of the information matrices and of the weighted measurements ... and every member knows n'. Line 132: 'let every member know Lambda^s = sum_i Lambda^s_i ... P-bar and P-bar^- are the steady-state posterior and prior covariances of the centralized filter and all members start from the centralized estimate'; update uses n h~\_i(t). Line 127 (static case): Lambda_i = Lambda_o + n sum_j (W^{n_c})\_ij Lambda^s_j. Restated in thm:agy-h1(d), line 392.
- Who evaluates: Members run the update. What they exchange is their own information contributions h^s_i, Lambda^s_i (own-data statistics, privacy-respecting). The global sum, the count and the centralized covariances are granted by hypothesis ('let every member know'); no agent is said to compute them in the dynamic case.
- Replacement: Consensus on Lambda^s_j, as the static part already does at 05_agency.tex:127, yields Lambda^s from messages; n must still be known. Contributions are full-dimension vectors in common world coordinates, not low-rank coded messages.
- Falsifies: A protocol in the assigned files by which members acquire n, Lambda^s and the common start from messages; I found none. As written it is a declared hypothesis, not an unstated one.

#### col-5. Meta-agent theorem (H5a): the member filter uses n, Lambda^s, P-bar, the coarse model and a reading of the coarse act; (H-act) grants common covariance and true effects

- Location: `Collective_Agents/sections/10a_meta_agents.tex:249`
- Class C, minor
- Quantity: n h~\_i, Lambda^s = H^T R_S^{-1} H, P-bar, F-bar, B-bar, a_C = P_A X_A (aggregate of all members' active channels); M_i = H\_\* B-bar P\_{A,i}
- Evidence: Line 225 (eq:met-member-filter): eta-hat^(i)\_t = F-bar[eta-hat^(i)\_{t-1} + P-bar(n h~\_i(t) - Lambda^s eta-hat^(i)\_{t-1})] + B-bar a\_{C,t-1}. Line 249: '(H-prot) The members read a_C, store it for one round and run the consensus filter ... with a matrix W that preserves sums ... and the steady-state covariances'. Line 250: '(H-act) ... beliefs N(m_i, P) ... with a common P ... a shared preference precision Lambda\*, common targets o\* ... and the true effects M_i'. Line 223: own contribution h^s_i = H_i^T R\_{S,i}^{-1} X\_{S_i}.
- Who evaluates: Members, under declared hypotheses (H-prot) and (H-act). Their own contribution is own-data; the count, the summed information matrix, the steady-state covariances, the shared coarse model and the aggregate act are supplied by the hypotheses.
- Replacement: Line 255: part (ii) 'holds for any fixed matrices in place of (F-bar, P-bar, B-bar, Lambda^s) ..., in particular for members that run a bounded model'. Line 232: at n_c = 0 'no contribution passes between members'. Level-0 (literal) protocols are pointed to in the supplement (line 266), not read.
- Falsifies: A statement of how a_C reaches each member (a channel carrying the aggregate) and how the summed quantities are obtained; (H-prot) says only that members 'read a_C'.

#### col-6. Code game: an agent's expected free energy counts how many partners use each code

- Location: `Collective_Agents/sections/06_coherence.tex:134`
- Class C, minor
- Quantity: u_i(sigma), the number of i's partners using code sigma, inside G_i(sigma) = -F_i(u_i(sigma)) - h_i sigma
- Evidence: Line 134: 'If i has d_i partners, u_i(sigma) of whom use code sigma, its believed information with code sigma is F_i(u_i(sigma))'. Line 138: 'G_i(sigma) = -F_i(u_i(sigma)) - h_i sigma'. Line 148: an agent 'resamples its code from q_i(sigma) proportional to e^{-gamma G_i(sigma)}'.
- Who evaluates: Agent i evaluates G_i for both codes; the text does not say how i knows its partners' code choices.
- Replacement: For binary codes the count follows from which partners i's own C1 calibration registers as matched (precision varpi^= against varpi^!=, line 134). This is my inference; the files do not state it.
- Falsifies: A statement that a sender's code is public, or that u_i is read from i's own calibrated precisions.

#### col-7. Linear conformity: an agent's expected free energy contains partners' conventions and a leave-one-out record reading

- Location: `Collective_Agents/sections/10b_hierarchy.tex:176`
- Class C, minor
- Quantity: x_j of attended partners and z-bar\_{alpha,-i}, the mean of the other group members' conventions
- Evidence: Line 176: 'G_i(x) = sum_j J_ij (x - x_j)^2 + a_p (x - x^0_i)^2 + beta_r (x - z-bar\_{alpha,-i})^2'. Line 178: 'the cavity reading z-bar\_{alpha,-i} of the record of i's group K_alpha, the mean of the other members' conventions'. Line 174: conventions are ones 'which no member senses'.
- Who evaluates: Agent i. The record is an external state that members write and read; how i reads partners' conventions x_j is not said beyond the couplings being 'attended', and the cavity reading needs the group size and removal of i's own contribution.
- Replacement: x_j as message content on attended edges; cavity reading as (record total minus own contribution). The literal alternative, a record mean that includes the agent's own convention, is at 10b_hierarchy.tex:182.
- Falsifies: A statement that conventions are expressed in messages or records that i reads.

#### col-8. Belief-dependent routing: update and expected free energy are written as functions of neighbors' internal states

- Location: `Collective_Agents/sections/08_scale.tex:84`
- Class C, minor
- Quantity: mu_k for neighbors k in G[i], as arguments of the local rule U_i and of G_i(pi; mu)
- Evidence: Line 68: 'mu_i(t+1) = U^(t)\_i(mu\_{G[i]}(t), zeta_i(t))' and 'this form covers messages, attention chosen from what an agent holds, and reads of records'. Line 84: policy posterior 'q_i(pi | mu) proportional to E_i(pi) e^{-gamma G_i(pi; mu)} ... expected free energy evaluated at the current states', with 'Lip_ik a Lipschitz constant of G_i(pi; .) in mu_k'.
- Who evaluates: Agent i. As written the arguments are other agents' internal states; line 68 says the form is a reduced description that covers messages.
- Replacement: Dependence through received messages y_ik, which is the stated intent at line 68; the files do not rewrite the routing proposition in that form.
- Falsifies: Nothing in the text contradicts the reduced-form reading; this is a wording observation and would be withdrawn if 'current states' is read as 'what agent i holds', as line 68 suggests.

#### col-9. Coarse-graining of codes: 'aggregation after true translation' does not say who holds the true translation

- Location: `Collective_Agents/sections/10c_renormalization.tex:189`
- Class C, minor
- Quantity: true translations U_i U_j^{-1} applied before aggregation; aggregate code T_c U-bar_J with U-bar_J = sum_j w_j U_j
- Evidence: Line 189: 'A meta-agent J that aggregates the public messages of its members with weights w_j ... has the aggregate code T_c U-bar_J ... aggregation after true translation loses nothing'. Line 199: 'aggregation after true translation preserves codes'. Line 221 (table): 'codes H_j: T_c U-bar_X (public); unchanged (translated)'.
- Who evaluates: Aggregation in public coordinates uses only posted messages. For the translated case the text here does not say who applies the true translation; the propositions (prop:ren-codes, prop:ren-code-levels) are in the supplement, not read.
- Replacement: Learned translations Theta_ij with mistranslation Upsilon_ij (02_framework.tex:239-243).
- Falsifies: The supplement stating the true-translation case as a describer-level limiting case, or as aggregation with learned translations in the limit of exact learning.

#### col-10. Exact fusion and class C2 need cross-covariances and provenance; the text declares them a reference

- Location: `Collective_Agents/sections/02_framework.tex:108`
- Class B, note
- Quantity: p^ex_i(y_ij | eta, Z_i) under the true joint process; A_ij = H_j(I - Sigma_ji Sigma_ii^{-1}), R^ex_ij (cross-covariance of the two agents' errors)
- Evidence: Line 108: exact fusion 'is the conditional law of y_ij given (eta, Z_i) under the true joint process'. Lines 112-119: track-model form with Sigma_ji Sigma_ii^{-1}. Line 132: 'on graphs with cycles exact fusion needs provenance'. Line 143: C2 is correct 'on the subspace that grounded data identify'. Line 159 (table): 'The receiver must know ... the cross-covariance in the track model, or the common information and the sender's information structure, which is provenance'. 01_introduction.tex:36: 'Exact fusion ... is the calibrated reference, and it needs provenance'. 13_discussion.tex:49: 'Exact fusion enters only as a reference and as a null'.
- Who evaluates: A hypothetical exact receiver used as the calibrated reference; the text states what it would have to know.
- Falsifies: A result in the assigned files in which exact fusion is the operating rule of the studied population rather than a reference or null. The nearest case is consensus on information contributions, called 'the information form of exact fusion' (05_agency.tex:146), recorded separately.

#### col-11. True value, provenance and the exact-inference proposition are reference constructions

- Location: `Collective_Agents/sections/03_misreading.tex:193`
- Class B, note
- Quantity: V\*\_i(J) = I(eta; y_iJ | Z_i) under the true joint process; A_ij = H_j P_j Lambda\_{j\\i}; members' exact inference 'including the senders' models and all correlations'
- Evidence: Line 13: true value 'under the true joint process'. Line 42: 'Computing it requires P_j, Lambda\_{j\\i} and the shared information vector, that is, knowledge of which of its sources the sender also used. We call this requirement provenance'. Line 193: 'Suppose every member of C does exact Bayesian inference ... under the true linear-Gaussian joint model including the senders' models and all correlations'. Line 202: 'The demands of exact fusion are informational: the receiver must know which of its sources the sender used and ... the cross-covariance'. Line 206: 'The exact-fusion receiver is also the reference against which collectives are attributed'.
- Who evaluates: The describer, through a hypothetical exact receiver; the text says so.
- Falsifies: A passage that has the level-0 or level-1 receivers of the network results use A_ij or the shared information vector.

#### col-12. Translation-aware null: receivers are granted the mistranslation itself

- Location: `Collective_Agents/sections/07_formation.tex:243`
- Class B, note
- Quantity: Upsilon_ij = U_i^{-1} Theta_ij U_j = Rot(phi_ij), a function of the true translation
- Evidence: Line 243: 'Let every receiver know the mistranslation Upsilon_ij = Rot(phi_ij) of every message, the part of class C2 that concerns translations (with T_c = I_2 the identifiable subspace is the whole plane)'. Line 252: 'A single receiver at the base point that fuses exactly against the split's stationary law'. 06_coherence.tex:31: 'under C2 it knows Upsilon_ij'; 06_coherence.tex:60: 'A receiver that knows Upsilon_ij, as a C2 receiver does, undoes it'.
- Who evaluates: Receivers inside a declared null of type S (05_agency.tex:350), used by the describer to attribute the split to misreading. The text ties the knowledge to what grounded data identify.
- Falsifies: Use of known Upsilon_ij outside the null, in the formation model proper; I found none.

#### col-13. True translation, mistranslation and the error recursion are describer-level

- Location: `Collective_Agents/sections/02_framework.tex:239`
- Class B, note
- Quantity: U_i U_j^{-1}; Upsilon_ij = U_i^{-1} Theta_ij U_j; W_ij = F K_ij H_j; B^mis_i = F sum_j K_ij (H_j - H-hat_ij)
- Evidence: Line 239: 'Receiver i reads sender j's internal coordinates through a translation Theta_ij in GL(K), learned or fixed, its model of the map ... The true translation is U_i U_j^{-1}. The mistranslation of the edge is the world-coordinate error'. Line 246: 'True translations compose without holonomy'. Line 271: error-transfer blocks in terms of H_j. 07_formation.tex:37 defines alpha\*\_ij and phi_ij the same way.
- Who evaluates: The describer; the receiver uses only Theta_ij, its own U_i and the public code (line 243).
- Falsifies: A receiver update written with U_j or H_j in place of Theta_ij or H-hat_ij without an exact-code hypothesis.

#### col-14. Meaning-lost identity: full-belief divergence is a measure; the reconstruction uses only the coded pushforward

- Location: `Collective_Agents/sections/02_framework.tex:78`
- Class B, note
- Quantity: KL(q_j || q_i) and KL(q_j || q-hat_ij); q-hat_ij = integral q_i(. | y) (T\_# q_j)(dy)
- Evidence: Line 78: 'q-hat_ij = int q_i(.|y)(T\_# q_j)(dy), KL(q_j || q-hat_ij) = KL(q_j || q_i) - KL(T\_# q_j || T\_# q_i)'. Line 85: part (c) 'measures what is lost, the divergence that the code does not transmit; in the Gaussian case a noiseless mean message with its law header transmits T\_# q_j exactly'. Line 94: 'What the code does not carry is supplied by the receiver'.
- Who evaluates: The full-belief divergences are evaluated by the describer as a measure of loss. The reconstruction is the receiver's own conditional law combined with the received coded marginal.
- Falsifies: A rule in which the receiver minimizes or computes KL(q_j || q_i).

#### col-15. Collectives, contrast and baselines are defined on the world-conditional law by an analyst

- Location: `Collective_Agents/sections/04_collectives.tex:131`
- Class B, note
- Quantity: Sigma^c, Pi^c (law of all agents' errors given the whole world path); r(C); r-bar_hom; ultrametric contrast; coarse media
- Evidence: Line 131: 'regular conditional law given the whole world path'. Lines 183-187: contrast from Pi^c 'of the whole population'. Line 195: 'an upper bound for an analyst who observes only the members'. Line 198: comparison medium 'declared with the model'. Line 215: 'a level r_0 be declared before the analysis'. Lines 314-318, 400-404. 07_formation.tex:13 selects 'by contrast on the world-conditional precision at a level r_0 declared in advance'.
- Who evaluates: An external analyst; the text says so.
- Falsifies: A passage in which members compute contrast or the baseline to decide membership.

#### col-16. Measurement of collectives needs a record of the world path

- Location: `Collective_Agents/sections/11_predictions.tex:9`
- Class B, note
- Quantity: world-conditional law, Pi^c, Omega_int
- Evidence: Line 9: 'Every quantity that selects or measures a collective belongs to the world-conditional law of the agents' errors, so a test needs a record of the world path or of a proxy for it'. Line 154: 'The framework also assumes grounded models of one shared world'.
- Who evaluates: An experimenter or analyst.
- Falsifies: None expected; this is the text's own statement of who evaluates.

#### col-17. Group expected free energy and agency index are as-if descriptions

- Location: `Collective_Agents/sections/05_agency.tex:157`
- Class B, note
- Quantity: G_C(pi), group posterior P_C, declared belief q_C, agency index
- Evidence: Line 152: 'Each member minimizes only its own expected free energy'. Line 155: group model has 'a belief q_C about eta_C, declared as a function of the collective's coarse state'. Line 172: member's G_i uses its own q_i. Line 194: 'The declared belief q_C does not enter'. Line 239: index uses 'the actual conditional laws'. Line 249: 'The index measures as-if agency'. 02_framework.tex:32 and 01_introduction.tex:60: 'there is no team objective'.
- Who evaluates: The describer compares the stationary law of deliberation with a declared group model; no member evaluates G_C.
- Falsifies: A protocol step in which a member evaluates G_C or q_C without (P0).

#### col-18. Interaction order parameter and null family condition on the shared exogenous drive

- Location: `Collective_Agents/sections/05_agency.tex:297`
- Class B, note
- Quantity: Omega_int(C) = mean pairwise I(mu_i path; mu_j path | X_sh); nulls including the exact-fusion null
- Evidence: Line 297: definition conditioning on X_sh. Line 331: 'A null is an intervention on the full model'. Line 350: exact-fusion null replaces 'every receiver's literal likelihood, fusion and attention ... by exact fusion, with provenance for records'. Line 364: 'replicate windows in which the shared drive is recorded'.
- Who evaluates: An analyst with access to internal-state paths and the shared drive.
- Falsifies: A passage in which agents compute Omega_int.

#### col-19. Echo-chamber measures use the true state; agents' own innovations cannot see shared error

- Location: `Collective_Agents/sections/03_misreading.tex:137`
- Class B, note
- Quantity: D_C = max E||m_i - m_j||^2, A_C = min E||m_i - eta||^2
- Evidence: Line 137: definitions. Line 121: social innovation y_ij - m_i and sensory innovation s_i - m_i are the agent's own data; 'only sensory innovations carry information about' a shared error. Line 178: 'members who calibrate their trust from social innovations cannot find out'.
- Who evaluates: The describer; the text states that members cannot evaluate the inaccuracy from social innovations.
- Falsifies: A member rule that uses A_C.

#### col-20. Coherence components are scored by the describer; believed fidelity is the receiver's own

- Location: `Collective_Agents/sections/06_coherence.tex:14`
- Class B, note
- Quantity: I(eta_t; y_ij), I(eta_t; y_ij | I_i); calibration criterion R-hat_ij = Cov(nu~\_ij) and Cov(nu~\_i, e_i); inaccuracy A_C
- Evidence: Line 14: 'believed fidelity is the mutual information between eta_t and y_ij under i's own generative model'. Line 15: calibrated 'if R-hat_ij = Cov(nu~\_ij)'. Line 17: coherence score pairs a quantity with the inaccuracy A_C. Line 22: 'only sensory innovations, that is grounding, can certify accuracy'; 'An exactly specified receiver must therefore represent the attenuated code H_j(P_0 - P)P_0^{-1} and the sender's estimation noise'.
- Who evaluates: The describer, except believed fidelity, which the receiver computes from its own model.
- Falsifies: A receiver rule that sets R-hat_i equal to the true covariance outside declared calibration classes.

#### col-21. Holonomy, consensus space and frustration are not assigned to any agent

- Location: `Collective_Agents/sections/06_coherence.tex:85`
- Class B, note
- Quantity: Hol(c) = Theta^(L)...Theta^(1) around a closed walk; F(mu) = sum\_{j->i} varpi_ij ||mu_i - Theta_ij mu_j||^2\_{M_i}
- Evidence: Line 4: components are 'each a property of the edges or cycles of the attention graph'. Line 16: holonomy composes translations held by different receivers. Line 68: 'Receivers learn their translations of one another independently, so Theta_ji need not be Theta_ij^{-1}'. Line 85: frustration defined on all agents' internal means. Line 60: 'Withdrawal from inconsistent edges is therefore a calibration-level effect'. Line 98: 'With rank-limited codes only what is talked about must agree' (coded consensus, supplement). 13_discussion.tex:55: 'holonomy measures learning or model error, not the curvature of a connection'.
- Who evaluates: The text does not have an agent compute a holonomy or minimize F in the assigned files; they appear in theorems about the system, and formation runs through each receiver's own calibration. Line 98 cites a supplement result on 'agents that average transported content', which I did not check.
- Falsifies: A supplement result (prop:coh-frustration-grounding) in which agents descend F using senders' full internal means mu_j with rank-limited codes.

#### col-22. Coarse states and the meta-agent's belief are declared by the describer

- Location: `Collective_Agents/sections/10a_meta_agents.tex:14`
- Class B, note
- Quantity: y_C, s_C, a_C, eta_C as linear maps of the joint process; the 'meta-agent's predictive law'
- Evidence: Line 14: 'Coarse variables of C are declared before the analysis through linear maps'. Line 204: coarse generative model and 'the meta-agent's predictive law'. Line 269: H5a 'describes a meta-agent and selects none'. 01_introduction.tex:87: 'declared before the analysis'. 10c_renormalization.tex:16-22: coarse-graining maps act on the world-conditional law.
- Who evaluates: The describer; members only run the filter recorded in the separate consensus finding.
- Falsifies: A passage that has a member compute s_C or y_C directly from other members' channels without messages.

#### col-23. Scale theory quantities are properties of the world-conditional error law

- Location: `Collective_Agents/sections/08_scale.tex:17`
- Class B, note
- Quantity: Sigma(t) = Cov(e(t)) given the world path; xi, xi_2, tau; correlational coherence theta_Z(C)
- Evidence: Line 17: 'Given the world path, e(t) is the fluctuation of the errors about their conditional mean'. Line 19: schedules are 'exogenous, or chosen from deterministic quantities such as claimed covariances'. Lines 134-143 and 330: lengths and coherence defined on world-conditional correlations.
- Who evaluates: The describer.
- Falsifies: An agent rule that uses xi or Sigma.

#### col-24. Walrasian price: sufficiency of the price presumes each agent knows its joint law; the pooled precision is a population sum

- Location: `Collective_Agents/sections/10_abstract_collectives.tex:122`
- Class B, note
- Quantity: p = eta-hat_pool; Lambda_pool = 1/P_0 + sum_i 1/R^s_i; h_p
- Evidence: Line 117: each agent demands from its own belief. Line 122: 'A price that reveals this statistic is sufficient ... and the price p = eta-hat_pool clears the market when every agent conditions on it'. Line 123: 'With h_p = Lambda_pool, the precision of the price as an estimate of eta, its believed precision exceeds the true precision'. Line 149 (polity): 'A model must declare its rule'.
- Who evaluates: The price is a public signal each agent reads; the sufficiency statement is a theorem about the model. Conditioning on the price correctly, or assigning it h_p = Lambda_pool, needs a sum over all agents' sensing precisions and the common prior, which the text supplies as a hypothetical value.
- Falsifies: A statement that agents learn h_p from their own innovations.

#### col-25. Optimal-sensor results are statements about a declared objective and the agent's own exterior

- Location: `Collective_Agents/sections/10d_environments.tex:94`
- Class B, note
- Quantity: G^att_h(H) = -I(s; S_m eta\_{t+h}) + min_a E[-ln p~(o)]; canonical variates of (eta_t, eta\_{t+h})
- Evidence: Line 5: 'what a sensor optimal for a declared horizon-h predictive-information objective reads'. Line 88: 'the agent chooses a sensor s = H eta_t + v and then an act a = a(s), a measurable function of the reading'. Line 100: 'The epistemic term is a declared choice'. Line 153: 'a public message M eta_t'.
- Who evaluates: The describer characterizes the optimum from the true exterior law (F, P_0); the agent acts on its own reading. No other agent's internal state enters.
- Falsifies: A result here that needs another agent's belief rather than exterior aggregates read through channels.

#### col-26. Positive: interaction only through blankets; frames private; messages are coded content

- Location: `Collective_Agents/sections/01_introduction.tex:9`
- Class E, note
- Quantity: y_ij = T_c U_j m_j + nu_ij = H_j m_j + nu_ij; receiver map O_ij
- Evidence: Line 9: 'agents interact only through their blankets: a direct message, a persistent record and a performative act are all paths from one agent's active states through external states to another agent's sensory states ... Frames, the private coordinates ..., are optional encodings whose effects appear only through communication'. Line 15: 'agent j may store its belief in private coordinates'; 'The map O is the right inverse O_ij of the receiver's code model'. Line 60: 'Each agent selects its policies by its own expected free energy, and there is no team objective'.
- Who evaluates: Each agent, from its own states and received messages.
- Falsifies: A factor in the model that joins mu_i to another agent's internal state directly.

#### col-27. Positive: receiver-owned code models and translations; reception uses the receiver's own prior

- Location: `Collective_Agents/sections/02_framework.tex:26`
- Class E, note
- Quantity: H-hat_ij, Theta_ij, O_ij = P_i H-hat^T (H-hat P_i H-hat^T)^{-1}, gain K
- Evidence: Line 24: 'the internal states of j influence those of i only along the path mu_j -> a_j -> X -> s_i -> mu_i ... no factor of (2.2) joins mu_i to a variable outside b_i'. Line 26: 'For each sender j it contains a message model: a code model H-hat_ij, a noise model and a model of what j's content summarizes'. Line 40: 'receiver i's model H-hat_ij of H_j is part of its generative model'. Lines 46-50: update from own prior and H-hat. Line 243: receiver carries a message with 'U_i^{-1} Theta_ij T_c^{-1} y_ij'. Line 250: everything 'depends on the encodings only through the effective codes H_j = T_c U_j and the receivers' models H-hat_ij of them'. Line 255: 'Frames are identifiable from messages only modulo the set {X: T_c X = 0}'. Line 263: gains 'computed from its claimed covariances and assigned noises'.
- Who evaluates: The receiver, from objects it owns.
- Falsifies: A reception update that uses H_j or U_j without an exact-code hypothesis.

#### col-28. Positive: codes are learned by the receiver from grounded co-occurrence

- Location: `Collective_Agents/sections/02_framework.tex:168`
- Class E, note
- Quantity: least-squares estimate H-hat_T from (y_t, phi-hat_t), with phi-hat_t formed from the receiver's own data
- Evidence: Line 168: 'a receiver can learn a sender's code from the co-occurrence of messages with its own observations of the world ... The receiver forms a regressor phi-hat_t from its own data Z_t without using y_t'. Line 157 (table): the receiver must know 'the sender's code, learned from grounded co-occurrence'. Lines 174-176: identification only on col(M_2); attenuation unless the calibrated statistic is used.
- Who evaluates: The receiver.
- Falsifies: A learning rule in this section that uses the sender's U_j.

#### col-29. Positive: levels 0 and 1 and calibration classes C0, C1g, C1i use assigned noise, posted headers or own innovations

- Location: `Collective_Agents/sections/02_framework.tex:107`
- Class E, note
- Quantity: R-hat_ij; level-1 noise H-hat P-hat_ij H-hat^T + R_c with the posted coded covariance H_j P_j H_j^T
- Evidence: Line 40: 'a sender may also post a law header, the coded covariance H_j P_j H_j^T of its belief'. Line 107: level 1 errors have covariance 'learned or read from a law header'. Line 142: C1i matches 'the second moment of the innovations y_ij - H-hat_ij m_i'. Line 141: C1g is learned 'on grounded rounds, on which the receiver observes the referent'. 03_misreading.tex:19: believed values 'depend on a sender only through its code, noise and posted confidence, never through the cross-covariance'.
- Who evaluates: The receiver, from posted content and own data; C1g uses a referent it observes on declared grounded rounds.
- Falsifies: A literal receiver that uses the sender's uncoded covariance P_j when the code has rank below K.

#### col-30. Positive with requirements: deliberation runs on shared data and announced intentions

- Location: `Collective_Agents/sections/05_agency.tex:163`
- Class E, note
- Quantity: G_i(pi_i, pi\_{-i}) = -I\_{q_i}(eta_C; o\_{B(pi)}) + psi^(i)(q_i)
- Evidence: Line 163: '(P2) Data and intention sharing: each member expects to receive all opened slots, its co-members' included ... and knows the others' current policies'. Line 165: (P4) resamples with G_i(pi_i, pi\_{-i}). Line 172: G_i is evaluated 'with belief q_i'. Line 206: 'what makes the collective an agent is what the members share: data and announced intentions'. Line 155: slot likelihoods 'that every belief shares'. Line 161: (P0) shared belief 'is used only where stated'.
- Who evaluates: Each member, from its own belief plus announced policies and shared slot data.
- Falsifies: A use of pi\_{-i} without announcement, or of another member's belief q_j inside G_i.

#### col-31. Positive: withdrawal and attention are driven by the receiver's own calibrated precisions; a C0 receiver's expected free energy is blind to mistranslation

- Location: `Collective_Agents/sections/06_coherence.tex:37`
- Class E, note
- Quantity: believed information from claimed covariances; calibrated precisions varpi_ij
- Evidence: Line 37: 'the expected free energy of an attention policy depends on the actual mistranslations only through the receiver's current belief, never through a term for the mistranslation itself'. Line 38: 'depends only on claimed covariances'. Line 50: receiver attends 'the kappa senders with the largest calibrated precisions'. Line 60: under C1i 'a receiver that does not sense is as blind as a C0 receiver'. Line 207: a level-0 receiver setting precision by free energy 'matches a moment that contains no shared error'.
- Who evaluates: The receiver.
- Falsifies: An attention rule that uses Upsilon_ij directly outside class C2.

#### col-32. Positive: in the two-group model translation, attention and fusion use the receiver's own frame, learned angle and claimed quantities

- Location: `Collective_Agents/sections/07_formation.tex:37`
- Class E, note
- Quantity: y~\_ij = U_i^{-1} Theta_ij y_ij; V^0_i(J); gains k^0_i, k^s_i, k_ij
- Evidence: Line 37: receiver 'translates it through the learned translation Theta_ij = Rot(alpha-hat_ij)'. Line 38: attention from 'the believed value V^0_i(J)' with own Lambda_0 and calibrated precisions. Line 39: gains from own claimed quantities. Line 40: declared start 'every receiver assumes that every sender shares its frame'.
- Who evaluates: The receiver. The calibration input and the learning input are recorded separately as class C.
- Falsifies: A fusion step that uses U_j or alpha\*\_ij directly.

#### col-33. Declared hypotheses: receivers know effective codes and read law headers; noiseless grounding rounds

- Location: `Collective_Agents/sections/09_minimal.tex:38`
- Class E, note
- Quantity: H-hat_ij = H_j; R-hat_ij = R_c + H_j P_j H_j^T; alpha_j = theta_j^2/(1 + theta_j^2 T_c P_j T_c^T); noiseless observation of eta_t with probability p_g
- Evidence: Line 15: 'let receivers know the codes and read at level 1'. Line 38: 'let receivers know the senders' effective codes H_j, of any rank, and read at level 1 with assigned noise R-hat_ij = R_c + H_j P_j H_j^T ... in each round each agent, independently of everything else and with probability p_g, observes eta_t without noise'. 08_scale.tex:53: 'level-1 receivers that know the codes and read the senders' law headers'. Same hypothesis as 'exact code models' at 02_framework.tex:275 and 03_misreading.tex:24.
- Who evaluates: The receiver uses its own code model and the posted coded covariance; the propositions assume the model is exact. The grounding rounds are declared.
- Falsifies: If exactness of H-hat_ij were meant as direct access to U_j rather than the limit of grounded learning (02_framework.tex:157, :168), this would not be privacy-respecting; the text gives the learned route.

#### col-34. Positive with requirements: hierarchical messages are likelihoods up and leave-one-out priors down

- Location: `Collective_Agents/sections/10b_hierarchy.tex:26`
- Class E, note
- Quantity: (Lambda^up_u, h^up_u); cavity (Lambda^post_u - Lambda^up_c, h^post_u - h^up_c); downward prior for child c
- Evidence: Lines 22-26: upward and downward message definitions. Line 28: 'upward messages carry likelihoods, and no prior enters them'. Line 29: 'downward messages are leave-one-out priors'. Line 35: 'the cavity is the provenance device of the channel filters'. Line 41: literal reading uses 'the collective's posted covariance as the law header'. Line 132: social and top-down innovations are the member's own data.
- Who evaluates: Each node from messages it receives. The parent must compute a separate cavity message per child, and all nodes share the link model (G_u, Psi_u) and coordinates.
- Falsifies: A downward message that requires the child's private data other than what the child sent up.

#### col-35. Positive: the discussion states that top-down priors reach members only through sensory channels and that frames act only through communication

- Location: `Collective_Agents/sections/13_discussion.tex:33`
- Class E, note
- Quantity: top-down prior as message, record, price or act
- Evidence: Line 33: 'the prior that a member receives from the level above is built by other agents, often from the members' own reports, and reaches the member only through its sensory channels, as messages, records, prices and acts. The exact top-down message is therefore the collective's estimate with the member's own contribution removed'. Line 13: 'the receiver's O is the right inverse of its code model that its own prior selects'. Line 55: 'frames are optional private encodings that act only through communication'.
- Who evaluates: Members, from what they receive.
- Falsifies: None expected.

### Hidden requirements

- A public code T_c per modality is shared by all its speakers and is known to receivers, who apply T_c^{-1} when it is invertible (Collective_Agents/sections/02_framework.tex:36, :243).
- All generative models are about one world state eta in common world coordinates, a declared shared reference space (Collective_Agents/sections/01_introduction.tex:9; 02_framework.tex:17; 11_predictions.tex:154).
- Level-1 reading needs the sender to post its coded covariance H_j P_j H_j^T as a law header, and the misreading section takes P-hat_ij = P_j by default (Collective_Agents/sections/02_framework.tex:40, :107; 03_misreading.tex:24).
- Many network theorems assume exact code models H-hat_ij = H_j, i.e. that the receiver's dictionary equals the sender's effective code T_c U_j (Collective_Agents/sections/02_framework.tex:275; 03_misreading.tex:24; 04_collectives.tex:167; 06_coherence.tex:192; 08_scale.tex:52; 09_minimal.tex:15, :38).
- Grounded code learning needs content calibration and exact joint attention in which 'the sender knows it exactly and sends it', and the regression-calibration repair needs the second moment M_phi of the sender's content and the grounding noise R^g (Collective_Agents/sections/02_framework.tex:168, :176).
- C1g calibration needs grounded rounds on which the receiver observes the referent, with population value the second moment of y_ij - H-hat_ij eta (Collective_Agents/sections/02_framework.tex:141; 07_formation.tex:39, :215).
- Exact fusion needs the cross-covariance of the two agents' errors, or the common information and the sender's information structure (provenance), and an evidence message needs 'the sender to know what the receiver lacks' (Collective_Agents/sections/02_framework.tex:132, :159; 03_misreading.tex:42, :202).
- A proper common prior shared by all agents is assumed in the static common-source world and in pooling (Collective_Agents/sections/03_misreading.tex:24; 05_agency.tex:111).
- Consensus on information contributions needs every member to know n, the summed information matrix Lambda^s, the centralized steady-state covariances and a common centralized start, and it exchanges full-dimension information vectors in common coordinates (Collective_Agents/sections/05_agency.tex:122, :132; 10a_meta_agents.tex:227).
- The meta-agent theorem needs members to read the coarse act a_C, to share the coarse model (F-bar, B-bar) and, for agency, a common covariance P, a shared preference precision, common targets and the true effects of their interventions (Collective_Agents/sections/10a_meta_agents.tex:249, :250).
- The deliberation protocol needs members to receive all opened slots, to know the others' current policies, to share slot likelihoods and to use one precision gamma (Collective_Agents/sections/05_agency.tex:155, :163, :164).
- In the static two-group model the receiver's likelihood uses the sender's sensing gain g_j, which depends on the sender's sensing noise (Collective_Agents/sections/06_coherence.tex:31, :49).
- In the two-group formation model translation learning receives a noisy observation of the true inter-frame angle on attended rounds (Collective_Agents/sections/07_formation.tex:40).
- The translation-aware null and class C2 need each receiver to know the mistranslation Upsilon_ij of every message (Collective_Agents/sections/07_formation.tex:243; 06_coherence.tex:31).
- The cycle-amplification theorem builds each receiver's gain with the sender's true effective code H_i, 'even when every code and every translation is correct' (Collective_Agents/sections/06_coherence.tex:102, :105).
- The code game needs each agent to know how many of its partners use each code (Collective_Agents/sections/06_coherence.tex:134).
- Linear conformity needs each agent to read attended partners' conventions and a leave-one-out mean of its group's record, which requires the group size and removal of its own contribution (Collective_Agents/sections/10b_hierarchy.tex:176, :178).
- Exact hierarchical inference needs the parent to compute a separate cavity (leave-one-out) message for each child and a shared link model across nodes (Collective_Agents/sections/10b_hierarchy.tex:26, :35).
- Sufficiency of the Walrasian price needs every agent to condition on the price under its true joint law, and the level-0 comparison assigns it the pooled precision Lambda_pool, a sum over all agents (Collective_Agents/sections/10_abstract_collectives.tex:122, :123).
- Aggregation of codes 'after true translation' needs the true translations between members' frames (Collective_Agents/sections/10c_renormalization.tex:189, :199).
- Measuring any collective needs a record of the world path or a proxy, and the interaction test needs a recorded shared drive (Collective_Agents/sections/11_predictions.tex:9; 05_agency.tex:364).
- I found no place in the assigned files where agents exchange dictionaries or code models with one another; receivers learn translations independently (Collective_Agents/sections/06_coherence.tex:68).
