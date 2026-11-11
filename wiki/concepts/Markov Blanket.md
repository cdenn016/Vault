---
type: concept
title: "Markov Blanket"
aliases:
  - "Markov blankets"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
status: draft
created: 2026-06-21
updated: 2026-11-11
---

# Markov Blanket

## Definition

A **Markov blanket** of a set of variables is the minimal set of other variables that, once
conditioned on, renders the target *conditionally independent* of everything else in the system.
The notion originates with Pearl's graphical models, where the blanket of a node is its parents,
its children, and its children's other parents (co-parents); conditioning on that set screens the
node off from the rest of the network. In the [[Free-energy principle active inference|free-energy principle]]
(FEP) the same construct is lifted from static graphs to the states of a stochastic dynamical
system and given a physical reading: the blanket becomes the *statistical boundary* of a system,
the surface across which an "inside" and an "outside" can be distinguished
([[friston-2013-life-as-we-know-it]]).

For a steady-state FEP construction, partition the state $x$ into four disjoint subsets

$$x = (\eta, s, a, \mu),$$

with

- **external states** $\eta$ — the environment / hidden causes outside the system
- **sensory states** $s$ — blanket states the external states influence but the internal states do not directly set
- **active states** $a$ — blanket states the internal states influence but the external states do not directly set
- **internal states** $\mu$ — the system's "interior", carrying its beliefs.

The **blanket** is the union of the sensory and active states, $b = (s, a)$. The defining property
is the conditional-independence (screening-off) condition

$$\eta \mathrel{\perp\perp} \mu \mid b,
\text{equivalently}
p(\eta, \mu \mid b) = p(\eta \mid b) p(\mu \mid b),$$

where $p$ is the declared joint law, here the steady-state law. This is a statistical
screening-off condition. Conditions on the drift, such as $\partial_\eta f_\mu = 0$ and
$\partial_\mu f_\eta = 0$, specify absent direct dynamical couplings; they do not in general
enforce the displayed conditional independence. [[biehl-2021-technical-critique]] distinguishes
these inequivalent assumptions. The sensory/active split adds a directional interpretation of
the perception–action loop and requires its own coupling assumptions
([[friston-2013-life-as-we-know-it]], [[parr-2020-markov-blankets-thermodynamics]]).

Path blankets concern entire trajectories and must be distinguished from a blanket of the
instantaneous or steady-state distribution. [[beck-2025-dynamic-markov-blanket-detection]]
explicitly makes this distinction. A claim about one law should not be transferred to another
without checking its assumptions.

## The agent boundary and the inference reading

[[friston-2013-life-as-we-know-it]] proposes an inferential reading in which internal states
parametrize beliefs about external states and their dynamics can be related to
[[Variational free energy]]. Conditional independence alone does not establish that reading:
it does not provide a map from each $\mu$ to the blanket-dependent density $p(\eta\mid b)$,
or prove that the internal dynamics minimize a variational objective.
[[biehl-2021-technical-critique]] identifies additional assumptions needed in the examined
derivations. A blanket is therefore a candidate statistical agent boundary; belief encoding
and variational dynamics are further claims.

[[parr-2020-markov-blankets-thermodynamics]] develops the thermodynamic and geometric account
under a specified dynamical construction. When an internal-state parametrization of a family
of probability laws has been supplied, its [[Fisher information metric]] defines an information
geometry. Identifying the physical flow with a [[Natural gradient]] flow requires a further
derivation; it is not a consequence of screening-off alone.

## Collective-boundary constructions

[[palacios-2020-hierarchical-markov-blankets]] permits changing membership while supplying
priors about possible blanket roles. [[waade-2025-as-one-and-many]] fits a group-level model
with a predefined blanket arrangement. These are different starting assumptions for collective
agency. In the flock preprint [[maisto-2025-flock-joint-agency]], Appendix A.4 of version 2
assigns candidate roles using a spectral partition of a shared-heading graph. As discussed in
[[Active inference communication and collective boundaries]], that procedure does not itself
prove screening-off under the flock's joint probability law.

[[beck-2025-dynamic-markov-blanket-detection]] instead infers changing labels under a
structured generative model. Its blanket constraints are part of the detector; the method does
not establish that arbitrary individual EFE policies generate such a boundary. The probability
law, partition, and time scope must be stated when comparing these results.

## Nested blankets: blankets of blankets

The construction is recursive, and that recursion is what makes it useful for a multi-scale theory.
[[kirchhoff-2018-markov-blankets-of-life]] introduce **ensemble Markov blankets** ("blankets of
blankets"): a collection of Markov-blanketed subsystems can, under the right coupling, self-assemble
into a superordinate system that itself possesses a Markov blanket. Concretely, when fast microscale
dynamics are slaved to slow macroscale order parameters (the synergetics / slaving picture), the same
statistical partition reappears one level up, with the macroscale blanket encoding the collective's
order parameter. Living systems are then hierarchies of nested blankets spanning organelles, cells,
tissues, organisms, and on out into the environment, and the boundary of an autonomous system need
not coincide with its biophysical boundary (the paper's examples — the water boatman's plastron air
bubble, caterpillar–pupa–butterfly metamorphosis — make the point that the *statistical* boundary can
extend beyond, or shift relative to, the obvious physical one).

[[kirchhoff-2018-markov-blankets-of-life]] also draw a crucial line between *mere* and *adaptive*
active inference. Any coupled dynamical system with a blanket (Huygens' coupled pendulums) technically
"performs active inference" in the synchrony sense; genuine autonomy requires a *temporally deep*
generative model that infers probable futures and minimizes *expected* free energy. Only the latter
earns the label "agent". This distinction guards the framework against the objection that the blanket
formalism makes everything an agent.

## Critiques

The inferential reading of the blanket is contested, and the wiki records the debate in full on
[[Markov blanket interpretation debate]]. Three critiques form a graded trio:

- **Conceptual (Pearl vs Friston).** [[bruineberg-2022-emperors-markov-blankets]] distinguish a
  **"Pearl blanket"** — the original epistemic, modeller-relative construct that merely *describes*
  conditional independence among chosen variables — from a **"Friston blanket"** — a putatively
  *ontological* boundary said to carve a real, mind-independent agent out of the world. Their charge is
  that the FEP literature slides illicitly from the former (an unobjectionable formal device) to the
  latter (a metaphysical claim the mathematics does not license). Any "physics of beliefs" program must
  say *which* blanket it means.
- **Quantitative.** [[aguilera-2022-particular-physics]] solve linear Ornstein–Uhlenbeck non-equilibrium
  systems in closed form and show that the clean blanket-and-belief structure holds only when the
  *solenoidal* (irreversible, non-equilibrium) part of the coupling is small. The inference reading is
  therefore *not generic*: dense or strongly irreversible coupling breaks the tidy partition. This is a
  direct warning for [[Multi-agent variational free energy]], where heavy inter-agent coupling generates
  exactly the irreversible flow the critique flags.
- **Technical.** [[biehl-2021-technical-critique]] argue that the foundational derivations equivocate
  between *inequivalent* definitions of "Markov blanket" (an instantaneous conditional-independence
  condition versus a sparsity condition on the flow, which need not coincide), and that the headline
  claim — "internal states parametrize beliefs about external states" — does not follow as stated from
  the assumptions actually used.

> [!note] Editorial: For this research program the critiques are inherited rather than refuted.
> [[participatory-it-from-bit]] presumes blanketed boundaries across which internal states encode
> beliefs and which nest into [[Meta-agents and hierarchical emergence|meta-agents]]; it does not
> *derive* that such blankets exist, are consistent across scales, or pick out real individuals. The
> participatory wager is that the conceptual critique can be turned into a partial answer — if reality
> is observer-relative ("it from bit"), a Pearl-style *perspectival* blanket is a feature, not a bug,
> and the [[Gauge transformation]] freedom over belief frames (no privileged frame for comparing
> beliefs) is its formal expression. That move does not touch the *quantitative* worry: the program
> still owes a check that the synchronization map stays non-degenerate in the strongly-coupled,
> irreversible regime the multi-agent model lives in. See [[Markov blanket interpretation debate]] for
> the full treatment.

## Relevance to this research

The Markov blanket is the bridge between physics and inference that the whole gauge-theoretic VFE
program stands on. Three uses recur:

1. **Agents as blanketed subsystems.** Each node in the multi-agent model is a Markov-blanketed system
   whose internal states carry a belief manifold; the blanket is its coupling interface, while
   inter-agent coupling alone establishes neither a higher-order blanket nor a fixed-joint ELBO.
   The transported peer-KL energy in [[Multi-agent variational free energy]] needs its own statistical interpretation. The
   blanketed-section picture is sharpened in [[Agents as fibre-bundle sections]].
2. **The hierarchy.** The nested-blanket ("blankets of blankets") construction of
   [[kirchhoff-2018-markov-blankets-of-life]] is the canonical precedent for the project's recursive
   meta-agent tower: scale-$(s{+}1)$ agents are coarse-grainings of clusters of scale-$s$ agents, and a
   parent's beliefs become its constituents' priors. This underwrites [[Meta-agents and hierarchical emergence]],
   [[Ouroboros multi-scale dynamics]], and the [[Renormalization group flow]].
3. **The geometry.** [[parr-2020-markov-blankets-thermodynamics]] supply the exact precedent for the
   *pullback* move: internal states parametrize a density over the external world, the metric on that
   parameter space is the [[Fisher information metric]], and belief updating is [[Natural gradient]]
   descent — the statistical-manifold structure on which the project's gauge-covariant transport,
   [[Hamiltonian belief dynamics]], [[Belief inertia]], and [[Mass as Fisher information]] are all built.

In short, the blanket gives the program its *agent boundary* (where one inference system ends and the
next begins), its *coupling interface* (how agents and scales talk), and — through the conditional-
independence condition — its license to read internal states as beliefs at all. The critiques fix the
exact debts that license still owes.

## Related

[[Markov blanket interpretation debate]], [[Free-energy principle active inference]],
[[Bayesian mechanics]], [[Variational free energy]], [[Fisher information metric]],
[[Multi-agent variational free energy]], [[Meta-agents and hierarchical emergence]],
[[Agents as fibre-bundle sections]], [[Participatory realism (it from bit)]]

## Sources

- [[friston-2013-life-as-we-know-it]] — the nonequilibrium-steady-state derivation: a blanket implies internal states appear to infer external states.
- [[kirchhoff-2018-markov-blankets-of-life]] — nested "ensemble" blankets; mere vs adaptive active inference; multi-scale individuality.
- [[parr-2020-markov-blankets-thermodynamics]] — information-geometric reading: internal states parametrize a Fisher-metric statistical manifold.
- [[bruineberg-2022-emperors-markov-blankets]] — conceptual critique: Pearl blanket vs Friston blanket; the illicit epistemic→ontological slide.
- [[aguilera-2022-particular-physics]] — quantitative critique: the blanket-and-belief structure holds only for small solenoidal coupling.
- [[biehl-2021-technical-critique]] — technical critique: inequivalent blanket definitions; the belief-encoding claim does not follow as stated.
- [[parr-friston-2019-generalised]] — generalised/expected free energy underpinning the adaptive (action-selecting) reading.

## Communication boundaries in Fields's framework

Fields, Glazebrook, and Levin represent finite interactions between systems in a separable pure joint state through a boundary of prepared and measured bits. They interpret that interface as a Markov blanket and use it to discuss cognition across scales. The separability and finite-resource premises belong to the construction; the result is not a theorem that every interacting classical collection automatically acquires a higher-order conditional-independence boundary. [[fields-2021-minimal-physicalism-as-a-scale-free-substrate-for-cognition-and-consciousness]]

The distinction matters when comparing a boundary, an observation protocol, and a variational objective. The quantum-FEP and thermodynamic-cost papers add their own physical and control assumptions. A complete application must state the probability law under which the blanket property holds and keep statistical VFE separate from the physical cost of maintaining the interface. [[fields-2022-a-free-energy-principle-for-generic-quantum-systems]], [[fields-2024-making-the-thermodynamic-cost-of-active-inference-explicit]], [[Chris Fields and physics as communication]]

## Collective agents references, November 10, 2026

[[Collective agents literature map]] groups the references ingested on November 10, 2026. Its section on active inference, expected free energy and Markov blankets holds the exchange on whether sparse coupling yields a blanket, in [[friston-2021-stochastic-chaos-markov]], [[aguilera-2023-knitting-markov-blanket]], [[heins-2022-sparse-coupling-markov]] and [[friston-2022-very-particular-comment]], and the sources on the decay of conditional mutual information, [[kuwahara-2020-clustering-conditional-mutual]] and [[sang-2025-stability-mixed-state]].

## An approximate meta-agent when coarse blanket conditions fail, November 11, 2026

In the linear-Gaussian model of the collective-agents manuscript, the pair of coarse sensory state and coarse act of a collective is an exact coarse path blanket only under conditions on what the members' sensors read and on how the exterior reads the members. [[dennis-2026-collective-agents-approximate-blanket-conditions]] treats the case in which those conditions fail in any of five ways: sensors that read exterior coordinates outside the coarse exterior, a coarse sensory state formed with weights other than those of the information-form statistic, sensors with memory, sensors that read members' acts or internal states, and an exterior that reads the members one by one. The coarse pair then need not screen off, in the weak or in the strong sense, and the theorem asserts no bound on its leak. What it keeps is a filtering statement under weaker hypotheses, the canonical partition, in which no internal and no active variable reads the exterior and the exterior reads no internal variable, per-channel noise, a stable joint process, members that run a consensus filter and a Gaussian start: the members' sensory channels, net of what they read inside the collective, are a sufficient record for the exterior, whose law given the paths of all collective variables is Gaussian with a covariance that no member's computation or act changes. This is a statement about one conditional law. It is not the fine path blanket, which can fail under the same violations.

With the members' channels as the record, the belief of the collective is measured against the law of the coarse exterior given those channels, and the error terms of the approximate meta-agent for the path law and the belief are of second order in the violations. The law given a coarse record is a second reference. For a coarse record that contains the coarse blanket path and determines the mean of the belief, the two excesses differ by a conditional mutual information that is at most the leak of the coarse blanket on the window, stays bounded as the window grows, and vanishes when the coarse blanket is exact. A bound on the leak itself through the defects of the declared models is open. The synthesis is [[Approximate meta-agent theorem]].
