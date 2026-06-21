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
updated: 2026-06-21
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

Formally, partition the state $x$ of an ergodic random dynamical system at nonequilibrium steady
state into four disjoint subsets,

$$x = (\eta,\; s,\; a,\; \mu),$$

with

- **external states** $\eta$ — the environment / hidden causes outside the system;
- **sensory states** $s$ — blanket states the external states influence but the internal states do not directly set;
- **active states** $a$ — blanket states the internal states influence but the external states do not directly set;
- **internal states** $\mu$ — the system's "interior", carrying its beliefs.

The **blanket** is the union of the sensory and active states, $b = (s, a)$. The defining property
is the conditional-independence (screening-off) condition

$$\eta \perp\!\!\!\perp \mu \;\big|\; b,
\qquad\text{equivalently}\qquad
p(\eta, \mu \mid b) = p(\eta \mid b)\, p(\mu \mid b),$$

so that internal and external states communicate *only through* the blanket — never directly.
At the level of the system's flow this is enforced by a sparsity structure on the coupling: the
drift on internal states does not depend on external states and vice versa, so $\partial_\eta f_\mu = 0$
and $\partial_\mu f_\eta = 0$, with the two halves talking exclusively via $s$ and $a$
([[friston-2013-life-as-we-know-it]], [[parr-2020-markov-blankets-thermodynamics]]). The
sensory/active asymmetry encodes the perception–action loop: sensory states carry the world's
influence *inward*, active states carry the system's influence *outward*.

## The agent boundary and the inference reading

The reason the blanket matters for this program is that the screening-off condition licenses an
*inferential interpretation* of an otherwise purely physical partition. Because internal states are
conditionally independent of external states given the blanket, at steady state each internal state
$\mu$ indexes a conditional density over external states, $p(\eta \mid b)$; one can then read the
internal state as *parametrizing a belief* $q_\mu(\eta)$ about the world. Friston's derivation shows
that, for an ergodic system with such a blanket, internal states *appear to* perform variational
inference — they evolve as if descending [[Variational free energy]], a tractable upper bound on
surprise (negative log model evidence) ([[friston-2013-life-as-we-know-it]]). This is the formal
content of the slogan "a thing that persists must look like it models its environment", and it is
what turns a Markov blanket into a candidate definition of an *agent boundary*: the blanket is the
interface across which an agent couples to its world, perception flowing in through $s$ and action
flowing out through $a$.

[[parr-2020-markov-blankets-thermodynamics]] make the geometry of this reading explicit. The map
from internal states to conditional densities $\mu \mapsto p(\eta \mid b)$ is a parametrization of a
*statistical manifold*; the natural metric on that manifold is the [[Fisher information metric]], so
belief updating is a [[Natural gradient]] flow, and the thermodynamic cost of maintaining the steady
state is bookkept as entropy production. This is the precise sense in which the blanket is a
*coupling interface* whose interior carries an information geometry — the structure the gauge-theoretic
program later pulls back and transports.

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
   whose internal states carry a belief manifold; the blanket is its coupling interface, and the
   inter-agent coupling assembles a higher-order blanket whose free energy is the sum of pairwise
   transported KL terms — the canonical form used in [[Multi-agent variational free energy]]. The
   blanketed-section picture is sharpened in [[Agents as fibre-bundle sections]].
2. **The hierarchy.** The nested-blanket ("blankets of blankets") construction of
   [[kirchhoff-2018-markov-blankets-of-life]] is the canonical precedent for the project's recursive
   meta-agent tower: scale-$(s{+}1)$ agents are coarse-grainings of clusters of scale-$s$ agents, and a
   parent's beliefs become its constituents' priors. This underwrites [[Meta-agents and hierarchical emergence]],
   [[Ouroboros multi-scale dynamics]], and the [[Renormalization-group flow of beliefs]].
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
